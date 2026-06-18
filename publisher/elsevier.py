"""
Elsevier (ScienceDirect) 适配器。

URL 模式: https://www.sciencedirect.com/science/article/pii/...
下载流程（优先级）:
  1. Extended PDF (CDN 直链): ars.els-cdn.com/.../mmc3.pdf — article + supplemental
  2. Standard PDF (CDN 直链): ars.els-cdn.com/.../main.pdf
  3. Ctrl+P 回退: pdfft URL → Chrome PDF 查看器 → pyautogui 打印

CDN 直链是首选方式，通过 browser_download() 的 fetch() 下载，
无需 Foxit Reader 或 pyautogui，速度更快更可靠。
"""

import logging
import os
import re
import time
from typing import Optional, Any
from urllib.parse import urljoin

import pyautogui

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class ElsevierAdapter(PublisherAdapter):
    """Elsevier ScienceDirect 适配器。

    优先使用 CDN 直链下载（Extended PDF > Standard PDF）。
    仅当 CDN 直链不可用时回退到 Ctrl+P + pyautogui 打印方式。
    """

    # Ctrl+P 回退标记
    use_click_download = True
    fetch_from_pdf_page = False

    @property
    def name(self) -> str:
        return "elsevier"

    def detect(self, url: str) -> bool:
        return "sciencedirect.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            # 等 View PDF 链接出现（Elsevier 页面需要时间渲染）
            try:
                page.wait_for_selector('a[aria-label*="PDF"]', timeout=15000)
            except Exception:
                logger.warning("View PDF link not found after 15s, continuing...")
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"Elsevier page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load Elsevier page: {e}")
            return False

    def find_download_url(self, page) -> str | None:
        """
        提取 PDF 下载 URL（优先 CDN 直链，回退 pdfft）。

        优先级：
        1. Extended PDF: ars.els-cdn.com/.../mmc3.pdf
           ScienceDirect 页面有 "Document S2. Article plus Supplemental Information"
           下载链接。这是 article+supplemental 合并版。
        2. Standard PDF: ars.els-cdn.com/.../main.pdf
        3. pdfft URL: 回退到 Ctrl+P 流程（resolve_pdf_url 处理）
        """
        pii_match = re.search(r'/pii/([^/?#]+)', page.url)
        current_pii = pii_match.group(1) if pii_match else ""

        # 1. 查找 Extended PDF (CDN 直链)
        try:
            elements = page.query_selector_all('a[href*="ars.els-cdn.com"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                text = (el.inner_text() or "").strip()
                if current_pii and href.endswith(".pdf"):
                    # Extended PDF: mmc3 或 "Article plus Supplemental Information"
                    if "mmc3" in href or "Article plus Supplemental" in text:
                        logger.info(f"Found extended PDF (CDN): {href[:100]}")
                        return href
            # 2. Standard PDF via CDN (main.pdf)
            if current_pii:
                for el in elements:
                    href = el.get_attribute("href") or ""
                    if "main.pdf" in href and current_pii in href:
                        logger.info(f"Found standard PDF (CDN): {href[:100]}")
                        return href
        except Exception as e:
            logger.debug(f"CDN link search failed: {e}")

        # 3. 回退：pdfft URL (Ctrl+P 流程)
        try:
            elements = page.query_selector_all('a[aria-label*="PDF"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href and "/pdfft" in href:
                    absolute = urljoin(page.url, href)
                    logger.info(f"Fallback to pdfft URL (Ctrl+P): {absolute[:80]}...")
                    return absolute
        except Exception as e:
            logger.debug(f"pdfft search failed: {e}")

        # 4. 文本兜底
        try:
            elements = page.query_selector_all('a:has-text("View PDF")')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href:
                    absolute = urljoin(page.url, href)
                    logger.info(f"Found via text match: {absolute[:80]}...")
                    return absolute
        except Exception as e:
            logger.debug(f"Text match failed: {e}")

        logger.error("Could not find any download URL on Elsevier page")
        return None

    def find_download_element(self, page) -> Optional[Any]:
        """仅用于 check_access，实际下载走 find_download_url。"""
        pii_match = re.search(r'/pii/([^/?#]+)', page.url)
        current_pii = pii_match.group(1) if pii_match else ""

        try:
            elements = page.query_selector_all('a[aria-label*="PDF"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href and "/pdfft" in href:
                    return el
        except Exception as e:
            logger.debug(f"aria-label search failed: {e}")

        try:
            elements = page.query_selector_all('a:has-text("View PDF")')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href:
                    return el
        except Exception as e:
            logger.debug(f"Text match failed: {e}")

        logger.error("Could not find any download element on Elsevier page")
        return None

    def check_access(self, page) -> bool:
        """用 PDF 链接或 CDN 链接存在性判断权限。"""
        # 检查 View PDF 链接
        try:
            pii_match = re.search(r'/pii/([^/?#]+)', page.url)
            current_pii = pii_match.group(1) if pii_match else ""
            elements = page.query_selector_all('a[aria-label*="PDF"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href and "/pdfft" in href:
                    return True
        except Exception:
            pass
        # 也检查 CDN 链接
        try:
            elements = page.query_selector_all('a[href*="ars.els-cdn.com"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and href.endswith(".pdf"):
                    return True
        except Exception:
            pass
        logger.warning("No PDF link found - likely no access")
        return False

    def resolve_pdf_url(self, page, initial_pdf_url: str) -> Optional[str]:
        """
        解析 PDF URL。

        如果 find_download_url 返回了 CDN 直链（ars.els-cdn.com），
        直接返回该 URL，browser_download() 会用 fetch() 下载，无需 Ctrl+P。

        如果返回的是 pdfft URL，优先导航到 pdfft 让浏览器跟随 302 重定向到
        pdf.sciencedirectassets.com 的签名 S3 直链，从该页面上下文同源 fetch()
        即可拿到 PDF（无需 pyautogui Ctrl+P，更适合无头/cron 场景）。
        重定向解析失败时再回退到 Ctrl+P + pyautogui 方式。
        """
        # CDN 直链：直接返回，走 browser_download
        if initial_pdf_url and "ars.els-cdn.com" in initial_pdf_url:
            logger.info(f"CDN direct download, skipping redirect: {initial_pdf_url[:100]}")
            return initial_pdf_url

        # pdfft URL：优先重定向解析（签名 S3 直链，同源 fetch）
        if initial_pdf_url and "/pdfft" in initial_pdf_url:
            resolved = self._resolve_pdfft_redirect(page, initial_pdf_url)
            if resolved:
                return resolved
            logger.warning("pdfft redirect resolution failed, falling back to Ctrl+P")

        # 其他情况 / 回退：Ctrl+P + pyautogui
        logger.info("Using Ctrl+P fallback for PDF URL...")
        return self._ctrl_p_download(page, initial_pdf_url)

    def _resolve_pdfft_redirect(self, page, pdfft_url: str) -> Optional[str]:
        """导航到 /pdfft URL，跟随客户端 JS 重定向到签名 S3 直链。

        ScienceDirect 的 /pdfft 端点返回一个 HTML 页面，页面内 JS 会重定向到一个
        带 AWS 签名的 S3 直链 (pdf.sciencedirectassets.com/.../main.pdf?X-Amz-...)，
        Chrome 随后用内置 PDF 查看器渲染它。

        关键点：该重定向是客户端 JS 触发的（不是 302），发生在 domcontentloaded
        之后约 1-5 秒。Playwright 的 ``page.url`` 在跳入 PDF 查看器期间会滞后/失真，
        因此必须用 ``page.evaluate("window.location.href")`` 读取真实 URL，并在
        "Execution context was destroyed"（重定向过渡期）时重试。

        从该页面上下文 ``fetch(window.location.href)`` 可直接拿到 PDF 字节（同源，
        无 CORS），browser_download() 会完成实际下载。签名 URL 有效期约 5 分钟
        （X-Amz-Expires=300）。适用于老论文（无 ars.els-cdn.com main.pdf CDN 直链）。
        """
        try:
            logger.info(f"Navigating to pdfft for redirect resolution: {pdfft_url[:80]}...")
            page.goto(pdfft_url, wait_until="domcontentloaded", timeout=60000)

            # 轮询 window.location.href，等待 JS 重定向到 S3 签名直链并稳定
            final_url = None
            last_url = None
            stable = 0
            deadline = time.time() + 18
            while time.time() < deadline:
                time.sleep(1)
                try:
                    cur = page.evaluate("() => window.location.href")
                except Exception:
                    # 重定向过渡期：执行上下文被销毁，继续等待
                    stable = 0
                    continue
                if cur and cur != pdfft_url and ".pdf" in cur.lower():
                    if cur == last_url:
                        stable += 1
                    else:
                        stable = 1
                        last_url = cur
                    # 连续两次相同 → 重定向已稳定，PDF 查看器就绪
                    if stable >= 2:
                        final_url = cur
                        break
            if final_url:
                logger.info(f"pdfft redirected to S3 direct link: {final_url[:120]}...")
                return final_url
            logger.warning("pdfft JS redirect to S3 did not settle within 18s")
            return None
        except Exception as e:
            logger.error(f"pdfft navigation failed: {e}")
            return None

    def fallback_download(self, page, monitor, failed_cdn_url: str):
        """
        CDN fetch 失败时的自动回退（backup 版本）。
        
        由 main.py 在 browser_download() 返回 None 后调用。
        切换到 Ctrl+P + pyautogui 流程下载。
        
        适用于：
        - CDN 直链需要特殊 cookie/referrer 但 fetch 拿不到
        - 某些 Elsevier 期刊页面结构不同，CDN 链接不匹配
        - CDN 临时不可用
        """
        logger.warning(f"CDN download failed ({failed_cdn_url[:80]}...), falling back to Ctrl+P")
        
        # 从 CDN URL 提取 pdfft URL
        pii_match = re.search(r'1-s2\.0-([^-]+)', failed_cdn_url)
        if not pii_match:
            # 从当前页面 URL 提取 PII
            pii_match = re.search(r'/pii/([^/?#]+)', page.url)
        
        if not pii_match:
            logger.error("Cannot determine PII for Ctrl+P fallback")
            return None
            
        # 确保页面在文章页（不是 PDF 查看器）
        if "/pdfft" in page.url or "ars.els-cdn.com" in page.url:
            # 导航回文章页
            pii = pii_match.group(1)
            article_url = f"https://www.sciencedirect.com/science/article/pii/{pii}"
            logger.info(f"Navigating back to article page: {article_url[:80]}...")
            self.navigate_to_paper(page, article_url)
        
        # 构造 pdfft URL 并走 Ctrl+P
        pii = pii_match.group(1)
        pdfft_url = f"{page.url.split('/pii/')[0]}/pii/{pii}/pdfft?isDTMRedir=true&download=true"
        logger.info(f"Trying Ctrl+P with pdfft URL: {pdfft_url[:80]}...")
        
        result = self._ctrl_p_download(page, pdfft_url)
        if result == "__click_download__":
            return self.click_download(monitor)
        return None

    def _ctrl_p_download(self, page, initial_pdf_url: str) -> str:
        """Ctrl+P 回退下载流程（原有逻辑）。"""
        logger.info("Opening View PDF in new tab...")
        ctx = page.context

        pii_match = re.search(r'/pii/([^/?#]+)', page.url)
        current_pii = pii_match.group(1) if pii_match else ""

        pdf_link = None
        try:
            elements = page.query_selector_all('a[aria-label*="PDF"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href and "/pdfft" in href:
                    pdf_link = el
                    break
        except Exception:
            pass

        if not pdf_link:
            try:
                elements = page.query_selector_all('a:has-text("View PDF")')
                for el in elements:
                    href = el.get_attribute("href") or ""
                    if current_pii and current_pii in href:
                        pdf_link = el
                        break
            except Exception:
                pass

        new_page = None

        # 方法1: Playwright click + expect_popup
        if pdf_link:
            try:
                with page.expect_popup(timeout=30000) as popup_info:
                    pdf_link.click()
                new_page = popup_info.value
                logger.info(f"  Got popup: {new_page.url[:80]}...")
            except Exception as e:
                logger.debug(f"  expect_popup failed: {e}")

        # 方法2: 直接导航到 pdfft
        if not new_page:
            logger.info("  Popup not captured, trying navigation approach...")
            try:
                page.goto(initial_pdf_url, timeout=60000)
            except Exception as e:
                logger.debug(f"  Navigation to /pdfft: {e}")
            new_page = page
            self._reuse_original_page = True

        time.sleep(3)

        # Check if we landed on a signed S3 URL (HTML interstitial instead of inline PDF)
        current_url = new_page.url
        if "pdf.sciencedirectassets.com" in current_url:
            logger.info("  Detected signed S3 URL (%s...), using CDP fetch download instead of Ctrl+P", current_url[:80])
            # Try to download via CDP evaluate + fetch
            try:
                result = new_page.evaluate("""async (url) => {
                    try {
                        const resp = await fetch(url);
                        if (!resp.ok) return {error: 'HTTP ' + resp.status};
                        const ct = resp.headers.get('content-type') || '';
                        if (!ct.includes('pdf')) return {error: 'Not PDF: ' + ct};
                        const buf = await resp.arrayBuffer();
                        return {size: buf.byteLength, data: Array.from(new Uint8Array(buf))};
                    } catch(e) { return {error: e.message}; }
                }""", current_url)
                if result.get("error"):
                    logger.error("  S3 fetch failed: %s", result["error"])
                elif result.get("size", 0) > 10000:
                    import os
                    temp_dir = self._config.get("download", {}).get("temp_dir", os.path.expandvars(r"C:\Users\Ivanz\Downloads\temp"))
                    os.makedirs(temp_dir, exist_ok=True)
                    filepath = os.path.join(temp_dir, f"elsevier_{int(time.time())}.pdf")
                    with open(filepath, "wb") as f:
                        f.write(bytes(result["data"]))
                    logger.info("  Saved S3 PDF via fetch: %s (%d bytes)", filepath, result["size"])
                    self._s3_download_path = filepath
                    return "__click_download__"  # Bypass Ctrl+P, click_download will pick up _s3_download_path
            except Exception as e:
                logger.error("  S3 fetch exception: %s", e)

        # 等待 PDF 加载
        time.sleep(2)

        try:
            new_page.bring_to_front()
        except Exception as e:
            logger.debug(f"  bring_to_front: {e}")
        time.sleep(1)

        # 在文章页获取窗口信息
        window_info = None
        try:
            window_info = page.evaluate("""() => ({
                screenX: window.screenX,
                screenY: window.screenY,
                outerWidth: window.outerWidth,
                outerHeight: window.outerHeight,
            })""")
        except Exception as e:
            logger.warning(f"  Could not get window info: {e}")

        self._print_start_time = time.time()
        self._click_pdf_download_button(new_page, window_info, None)

        self._pdf_tab = new_page if not getattr(self, '_reuse_original_page', False) else None
        self._article_page = page

        return "__click_download__"

    def _click_pdf_download_button(self, pdf_page, window_info: dict | None = None, monitor=None) -> None:
        """在 Chrome PDF 查看器中用 Ctrl+P 打印为 PDF。"""
        if monitor:
            temp_dir = monitor.get_temp_dir()
        else:
            temp_dir = os.path.expandvars(r"C:\Users\Ivanz\Downloads\temp")
        try:
            cdp = pdf_page.context.new_cdp_session(pdf_page)
            cdp.send("Browser.setDownloadBehavior", {
                "behavior": "allowAndName",
                "downloadPath": temp_dir,
                "eventsEnabled": True,
            })
            logger.info(f"  CDP download path set to: {temp_dir}")
        except Exception as e:
            logger.debug(f"  CDP set download behavior: {e}")

        if window_info:
            title_x = window_info["screenX"] + window_info["outerWidth"] // 2
            title_y = window_info["screenY"] + 5
            pyautogui.click(title_x, title_y)
            logger.info(f"  Clicked Chrome title bar at ({title_x}, {title_y}) to focus")
            time.sleep(1)
            content_x = window_info["screenX"] + window_info["outerWidth"] // 2
            content_y = window_info["screenY"] + window_info["outerHeight"] // 2
            pyautogui.click(content_x, content_y)
            time.sleep(0.5)
        else:
            logger.warning("  No window info, trying bring_to_front as fallback")
            try:
                pdf_page.bring_to_front()
            except Exception:
                pass
            time.sleep(1)

        pyautogui.hotkey('ctrl', 'p')
        logger.info("  Sent Ctrl+P (print)")

        time.sleep(3)
        pyautogui.press('enter')
        logger.info("  Pressed Enter (confirm print dialog)")

        time.sleep(10)
        pyautogui.press('enter')
        logger.info("  Pressed Enter (confirm save dialog)")
        time.sleep(2)

    def click_download(self, monitor) -> Optional[str]:
        """Return S3-fetched PDF if already downloaded, otherwise wait for Ctrl+P PDF to land."""
        # Check if _ctrl_p_download already saved via S3 fetch
        if hasattr(self, '_s3_download_path') and self._s3_download_path:
            path = self._s3_download_path
            self._s3_download_path = None  # reset
            size = os.path.getsize(path) if os.path.exists(path) else 0
            if size > 10000:
                logger.info("Returning S3-fetched PDF: %s (%d bytes)", path, size)
                return path
            logger.warning("S3-fetched file invalid, falling through to Ctrl+P wait...")

        import glob as glob_mod
        temp_dir = monitor.get_temp_dir()
        logger.info("Waiting for PDF print to complete...")

        start_time = getattr(self, '_print_start_time', time.time())

        filepath = None
        for i in range(60):
            time.sleep(2)
            candidates = []
            for f in glob_mod.glob(os.path.join(temp_dir, "*.pdf")):
                try:
                    mtime = os.path.getmtime(f)
                    if mtime >= start_time - 1:
                        size = os.path.getsize(f)
                        if size > 10000:
                            candidates.append((f, mtime, size))
                except OSError:
                    continue
            if candidates:
                candidates.sort(key=lambda x: x[1], reverse=True)
                f, mtime, size = candidates[0]
                time.sleep(3)
                new_size = os.path.getsize(f)
                if new_size == size and size > 100000:
                    size_mb = size / 1024 / 1024
                    logger.info(f"Found new PDF: {os.path.basename(f)} ({size_mb:.1f} MB)")
                    filepath = f
                    break

        # 清理：关闭 PDF 查看 tab
        if hasattr(self, '_pdf_tab') and self._pdf_tab:
            try:
                self._pdf_tab.close()
            except Exception:
                pass
            self._pdf_tab = None
        self._reuse_original_page = False

        if filepath is None:
            logger.error("PDF print not detected after 120s")
        return filepath

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 Elsevier 论文元数据。"""
        info = PaperInfo(publisher="elsevier")

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
