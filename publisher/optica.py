"""
Optica Publishing Group 适配器。

URL 模式: https://opg.optica.org/ol/fulltext.cfm?uri=...
下载流程:
  1. 文章页 → 提取 viewmedia.cfm 链接
  2. 导航到 viewmedia → Chrome 自动完成 JS 挑战 + 重定向链
  3. 拿到最终 directpdfaccess URL
  4. 回到文章页，用 fetch() 下载 PDF
"""

import logging
import time
from typing import Optional, Any

from .base import PublisherAdapter

logger = logging.getLogger(__name__)


class OpticaAdapter(PublisherAdapter):
    """Optica Publishing Group 适配器（包括 OSA 期刊）。"""

    @property
    def name(self) -> str:
        return "optica"

    def detect(self, url: str) -> bool:
        return "optica.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                pass
            logger.info(f"Optica page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load Optica page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """定位 "Get PDF" 按钮。"""
        for selector in ['a:has-text("Get PDF")', 'a:has-text("PDF Article")']:
            try:
                element = page.query_selector(selector)
                if element and element.is_visible():
                    logger.info(f"Found download element: '{selector}'")
                    return element
            except Exception:
                continue

        # Fallback: viewmedia.cfm + seq=0
        try:
            for link in page.query_selector_all("a"):
                href = link.get_attribute("href") or ""
                if "viewmedia.cfm" in href and "seq=0" in href and "figure=" not in href:
                    if link.is_visible():
                        return link
        except Exception:
            pass
        return None

    def resolve_pdf_url(self, page, initial_pdf_url: str) -> Optional[str]:
        """
        让 Chrome 走完 Optica 的 JS 挑战，拿到直链 PDF URL。

        已知的重定向链：
          链路 A: viewmedia.cfm →(JS挑战)→ view_article.cfm?pdfKey=XXX → directpdfaccess/XXX/name.pdf
          链路 B: viewmedia.cfm →(JS挑战)→ directpdfaccess/XXX/name.pdf（直接跳到 PDF）

        链路 A 时从 view_article.cfm 的 pdfKey 构造直链；
        链路 B 时页面已经到了 directpdfaccess，直接提取 URL。
        """
        logger.info(f"Resolving Optica PDF URL through redirect chain...")

        # 1. 导航到 viewmedia.cfm，让 Chrome 完成 JS 挑战
        try:
            page.goto(initial_pdf_url, timeout=60000)
        except Exception as e:
            logger.debug(f"Navigation exception (may be normal for PDF redirect): {e}")

        # 2. 等待重定向完成（两种链路）
        #    链路 A: URL 变成 view_article.cfm?pdfKey=XXX
        #    链路 B: URL 变成 directpdfaccess/...
        for i in range(60):
            current = page.url
            # 链路 B: 直接到了 directpdfaccess
            if "directpdfaccess" in current:
                logger.info(f"Direct redirect to PDF: {current}")
                return current
            # 链路 A: 到了 view_article.cfm
            if "view_article.cfm" in current and "pdfKey=" in current:
                break
            time.sleep(1)
        else:
            # 60 秒超时，最后再检查一次 directpdfaccess
            current = page.url
            if "directpdfaccess" in current:
                logger.info(f"Final check found direct PDF: {current}")
                return current
            # 也检查新开标签页（PDF 可能在新 tab 打开）
            for ctx in page.context.browser.contexts:
                for p in ctx.pages:
                    if "directpdfaccess" in p.url:
                        logger.info(f"Found direct PDF in new tab: {p.url}")
                        return p.url
            logger.error(f"Never reached view_article.cfm or directpdfaccess, stuck at: {page.url}")
            return None

        # 3. 从 URL 提取 pdfKey
        import re
        match = re.search(r"pdfKey=([a-f0-9\-_]+)", page.url)
        if not match:
            logger.error(f"Cannot extract pdfKey from: {page.url}")
            return None

        pdf_key = match.group(1)
        logger.info(f"Extracted pdfKey: {pdf_key}")

        # 4. 从原始 URI 提取 DOI 后缀（如 ol-51-9-2708）
        uri_match = re.search(r"uri=([^&]+)", initial_pdf_url)
        doi_part = uri_match.group(1) if uri_match else ""

        # 从 pdfKey 提取 id（下划线后面的数字）
        id_match = re.search(r"_(\d+)$", pdf_key)
        article_id = id_match.group(1) if id_match else ""

        # 5. 构造 directpdfaccess 直链
        direct_url = (
            f"https://opg.optica.org/directpdfaccess/"
            f"{pdf_key}/{doi_part}.pdf"
            f"?da=1&id={article_id}&seq=0&mobile=no"
        )
        logger.info(f"Constructed direct URL: {direct_url}")
        return direct_url

    def get_paper_metadata(self, page) -> Any:
        """提取论文元数据。"""
        from .base import PaperInfo
        info = PaperInfo(publisher="optica")
        try:
            info.title = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_title"]');
                return el ? el.content : (document.querySelector('h1')?.innerText || '');
            }""") or ""
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
            info.url = page.url
        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")
        return info
