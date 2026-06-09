"""
AIP (American Institute of Physics) 适配器。

URL 模式: https://pubs.aip.org/aip/.../article/...
下载流程: 论文页 -> 提取 PDF 链接 -> 导航跟随重定向 -> 在 PDF 页面 fetch() 下载

AIP (Silverchair 平台) 的 PDF 存放在 watermark.silverchair.com CDN，
带签名 token。直接 fetch() 原始 /article-pdf/ URL 会失败（CORS），
需要先 page.goto() 跟随重定向拿到 CDN URL，再在 CDN 页面上 fetch。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class AIPAdapter(PublisherAdapter):
    """American Institute of Physics (AIP) 适配器。
    
    覆盖 pubs.aip.org 域名下的 AIP 期刊（JCP, APL, PRL 等）。
    AIP 使用 Silverchair 平台，PDF 直链含 article-pdf 路径段。
    """

    # 告诉 main.py 不要回文章页，在 PDF 页面上做 fetch（跨域需要）
    fetch_from_pdf_page = True

    @property
    def name(self) -> str:
        return "aip"

    def detect(self, url: str) -> bool:
        return "pubs.aip.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"AIP page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load AIP page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。
        
        AIP 的 PDF 链接文本是 "Open the PDF for ... in another window"，
        href 包含 /article-pdf/ 路径段。
        """
        for selector in [
            'a[href*="/article-pdf/"]',
            'a[href*="article-pdf"]',
        ]:
            try:
                element = page.query_selector(selector)
                if element:
                    href = element.get_attribute("href") or ""
                    logger.info(f"Found download element: '{selector}' -> {href}")
                    return element
            except Exception as e:
                logger.debug(f"Selector '{selector}' failed: {e}")

        logger.error("Could not find any download element on AIP page")
        return None

    def check_access(self, page) -> bool:
        """用 PDF 链接存在性判断权限。"""
        pdf_link = page.query_selector('a[href*="/article-pdf/"]')
        if pdf_link:
            return True
        logger.warning("No PDF download link found - likely no access")
        return False

    def resolve_pdf_url(self, page, initial_pdf_url: str) -> Optional[str]:
        """
        AIP 的 PDF URL 会重定向到 silverchair CDN（带签名 token）。
        
        需要 page.goto() 跟随重定向，拿到最终的 CDN URL。
        CDN URL 和文章页不同源，所以 fetch() 必须在 PDF 页面上执行。
        """
        logger.info("Resolving AIP PDF URL (following redirect to CDN)...")
        try:
            page.goto(initial_pdf_url, timeout=60000)
        except Exception as e:
            logger.debug(f"Navigation exception: {e}")

        actual_url = page.url
        if "silverchair" in actual_url or actual_url.endswith(".pdf"):
            logger.info(f"Resolved to CDN URL: {actual_url[:80]}...")
            return actual_url
        
        logger.error(f"Unexpected redirect target: {actual_url}")
        return None

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 AIP 论文元数据。"""
        info = PaperInfo(publisher="aip")

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
