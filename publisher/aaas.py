"""
AAAS (Science) 适配器。

URL 模式: https://www.science.org/doi/10.1126/...
下载流程: 论文页 -> 提取 PDF 直链 -> fetch() 下载
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class AAASAdapter(PublisherAdapter):
    """American Association for the Advancement of Science (AAAS) 适配器。
    
    覆盖 science.org 域名下的 Science, Science Advances, Science Translational Medicine 等。
    """

    @property
    def name(self) -> str:
        return "aaas"

    def detect(self, url: str) -> bool:
        return "science.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"AAAS page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load AAAS page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。
        
        AAAS 页面有两个 PDF 链接：
        - 折叠菜单里的 (visible=False): /doi/pdf/...?download=true
        - 页面底部的 (visible=True): /doi/pdf/... (无 download param)
        
        优先取带 ?download=true 的（浏览器直接触发下载），不检查 is_visible
        因为折叠菜单里的链接功能正常只是当前不可见。
        """
        selectors = [
            'a[href*="/doi/pdf/"][href*="download=true"]',
            'a[href*="/doi/pdf/"]',
            'a:has-text("Download PDF")',
        ]

        for selector in selectors:
            try:
                element = page.query_selector(selector)
                if element:
                    href = element.get_attribute("href") or ""
                    logger.info(f"Found download element: '{selector}' -> {href}")
                    return element
            except Exception as e:
                logger.debug(f"Selector '{selector}' failed: {e}")

        logger.error("Could not find any download element on AAAS page")
        return None

    def check_access(self, page) -> bool:
        """
        AAAS 权限检测：有 PDF 下载链接 = 有权限。
        
        不用基类的文本匹配（DOI 中的 "403" 会误触发）。
        """
        pdf_link = page.query_selector('a[href*="/doi/pdf/"]')
        if pdf_link:
            return True
        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 AAAS 论文元数据。"""
        info = PaperInfo(publisher="aaas")

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
