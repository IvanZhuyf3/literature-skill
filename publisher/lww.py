"""LWW (Lippincott Williams & Wilkins / Wolters Kluwer EJP) adapter.

URL 模式: journals.lww.com  (e.g. Medicine & Science in Sports & Exercise,
AJN, etc. — all journals hosted on the Wolters Kluwer "Oaks/EJP" platform)

下载流程: 点击型 (click-download)。
  - 文章页 "PDF" 工具按钮 (class js-ejp-login-btn) 携带 data-config，
    其 eventName=PDFDownloadInit，eventDetail.url 指向:
      .../_layouts/15/oaks.journals/downloadpdf.aspx?trckng_src_pg=ArticleViewer&an=<ACCESSION>
  - gating:false / isLoginOptional:true / promptLogin:false ⇒ 无需登录即可下载。
  - 该 downloadpdf.aspx 直链用 fetch() 取会返回 HTML（302 回文章页），
    必须触发按钮 click（fire PDFDownloadInit 事件），由浏览器原生发起
    Content-Disposition 附件下载，再用 expect_download 捕获。
  - accession 号 (an) 形如 00005768-200611001-00127，可从页面 HTML 或按钮
    data-config 提取，作为构造 URL 的回退。
"""

import logging
import os
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class LWWAdapter(PublisherAdapter):
    """LWW / Wolters Kluwer EJP 平台适配器，覆盖 journals.lww.com。"""

    # data-config 中 PDF 按钮的关键 JS（复用，避免重复字符串）
    _PICK_PDF_BTN_JS = """() => {
        let pdfBtn = null;
        document.querySelectorAll('.js-ejp-login-btn').forEach(b => {
            let c = null;
            try { c = JSON.parse(b.getAttribute('data-config') || '{}'); } catch(e){}
            if (c && c.eventName === 'PDFDownloadInit') pdfBtn = b;
        });
        return pdfBtn;
    }"""

    @property
    def name(self) -> str:
        return "lww"

    def detect(self, url: str) -> bool:
        return "journals.lww.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"LWW page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load LWW page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        # PDF 由 JS 事件驱动下载，不存在可直接取 href 的元素。
        # 实际逻辑在 find_download_url / resolve_pdf_url 中处理。
        return None

    def _extract_pdf_info(self, page) -> Optional[dict]:
        """从 PDF 按钮的 data-config 提取 {url, gating}。无则返回 None。"""
        try:
            return page.evaluate("""() => {
                let out = null;
                document.querySelectorAll('.js-ejp-login-btn').forEach(b => {
                    let c = null;
                    try { c = JSON.parse(b.getAttribute('data-config') || '{}'); } catch(e){}
                    if (c && c.eventName === 'PDFDownloadInit' && c.eventDetail) {
                        out = { url: c.eventDetail.url, gating: c.eventDetail.gating };
                    }
                });
                return out;
            }""")
        except Exception as e:
            logger.debug(f"_extract_pdf_info failed: {e}")
            return None

    def _construct_pdf_url(self, page) -> Optional[str]:
        """回退：从页面 accession 号 (an=) 构造 downloadpdf.aspx URL。"""
        try:
            an = page.evaluate("""() => {
                const m = document.documentElement.outerHTML.match(
                    /an=([0-9]{8}-[0-9]{5,9}-[0-9]{4,5})/i);
                return m ? m[1] : null;
            }""")
            if not an:
                return None
            journal = page.url.split("journals.lww.com/", 1)[1].split("/", 1)[0]
            return (f"https://journals.lww.com/{journal}/_layouts/15/oaks.journals/"
                    f"downloadpdf.aspx?trckng_src_pg=ArticleViewer&an={an}")
        except Exception:
            return None

    def find_download_url(self, page) -> Optional[str]:
        """返回 downloadpdf.aspx URL（占位 + 日志用；实际下载走 resolve_pdf_url 点击流）。"""
        info = self._extract_pdf_info(page)
        if info and info.get("url"):
            logger.info(f"LWW PDF URL (button config): {info['url'][:90]}")
            return info["url"]
        constructed = self._construct_pdf_url(page)
        if constructed:
            logger.info(f"LWW PDF URL (constructed from accession): {constructed[:90]}")
            return constructed
        logger.error("Could not find LWW PDF download URL on page")
        return None

    def check_access(self, page) -> bool:
        """PDF 按钮存在且 gating != True ⇒ 可下载（无需订阅）。

        LWW 即使未登录也会渲染 PDF 工具按钮；gating:false / isLoginOptional:true
        表示该内容开放，点击即得 PDF。
        """
        info = self._extract_pdf_info(page)
        if info and info.get("url"):
            if info.get("gating") in (None, False, "false"):
                return True
            logger.warning(
                f"LWW PDF is gated (subscription required): gating={info.get('gating')}"
            )
            return False
        logger.warning("LWW: no PDF tool button found - not an article or no access")
        return False

    def resolve_pdf_url(self, page, initial_pdf_url: Optional[str]) -> Optional[str]:
        """触发 PDF 按钮 click 并捕获浏览器下载。

        downloadpdf.aspx 用 fetch() 取返回 HTML，因此必须点击按钮
        （fire PDFDownloadInit）让浏览器发起 Content-Disposition 附件下载，
        再用 page.expect_download() 捕获并保存。
        返回哨兵 '__click_download__'；click_download() 返回已存路径。
        """
        outdir = os.path.expandvars(
            self.config.get("download", {}).get(
                "temp_dir", os.path.join(os.path.expanduser("~"), "Downloads", "temp")
            )
        )
        os.makedirs(outdir, exist_ok=True)
        self._click_path = None
        try:
            with page.expect_download(timeout=45000) as dl_info:
                clicked = page.evaluate("""() => {
                    let pdfBtn = null;
                    document.querySelectorAll('.js-ejp-login-btn').forEach(b => {
                        let c = null;
                        try { c = JSON.parse(b.getAttribute('data-config') || '{}'); } catch(e){}
                        if (c && c.eventName === 'PDFDownloadInit') pdfBtn = b;
                    });
                    if (!pdfBtn) return false;
                    pdfBtn.click();
                    return true;
                }""")
                if not clicked:
                    raise RuntimeError("PDF tool button (PDFDownloadInit) not found")
            download = dl_info.value
            fname = download.suggested_filename or "lww_article.pdf"
            if not fname.lower().endswith(".pdf"):
                fname += ".pdf"
            fname = os.path.basename(fname)
            path = os.path.join(outdir, fname)
            base, ext = os.path.splitext(fname)
            counter = 1
            while os.path.exists(path):
                path = os.path.join(outdir, f"{base}_{counter}{ext}")
                counter += 1
            download.save_as(path)
            size = os.path.getsize(path)
            logger.info(f"LWW click-download saved: {path} ({size / 1024:.1f} KB)")
            self._click_path = path
            return "__click_download__"
        except Exception as e:
            logger.error(f"LWW click-download failed: {e}")
            return None

    def click_download(self, monitor) -> Optional[str]:
        """返回 resolve_pdf_url 已保存的路径（哨兵流）。"""
        return getattr(self, "_click_path", None)

    def get_paper_metadata(self, page) -> PaperInfo:
        info = PaperInfo(publisher="lww")
        try:
            info.title = page.evaluate("""() => {
                const el = document.querySelector('meta[property="og:title"]');
                let t = el ? el.content : '';
                // og:title 格式 "<Title> : <Journal>" — 去掉尾部 " : <Journal>"
                const idx = t.lastIndexOf(' : ');
                if (idx > 0) t = t.slice(0, idx);
                if (!t) {
                    const h1 = document.querySelector('h1');
                    t = h1 ? h1.innerText.trim() : '';
                }
                return t;
            }""") or ""
            info.url = page.url
            info.doi = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_doi"]');
                return el ? el.content : '';
            }""") or ""
            info.year = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_date"]');
                return el ? el.content : '';
            }""") or ""
            info.authors = page.evaluate("""() => {
                const metas = document.querySelectorAll('meta[name="citation_author"]');
                return Array.from(metas).map(m => m.content).join(', ');
            }""") or ""
        except Exception as e:
            logger.warning(f"LWW metadata extraction partial failure: {e}")
        return info
