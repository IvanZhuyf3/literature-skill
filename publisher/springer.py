"""
Springer 适配器。

URL 模式: https://link.springer.com/article/...
下载流程: 论文页 -> 提取 PDF 直链 -> fetch() 下载

注意：Springer 和 NPG (nature.com) 虽然同属 Springer Nature 集团，
但网站架构和页面风格完全不同，需要分开处理。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class SpringerAdapter(PublisherAdapter):
    """Springer (link.springer.com) 适配器。
    
    覆盖 link.springer.com 域名下的 Springer 期刊和图书章节。
    注意：nature.com 的内容由 NPGAdapter 处理。
    """

    @property
    def name(self) -> str:
        return "springer"

    def detect(self, url: str) -> bool:
        return "link.springer.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"Springer page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load Springer page: {e}")
            return False

    def check_access(self, page) -> bool:
        """用 PDF 下载链接存在性判断权限，不用文本匹配。"""
        pdf_link = page.query_selector('a[data-track-action="download pdf"]')
        if pdf_link:
            return True
        logger.warning("No PDF download link found - likely no access")
        return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。
        
        Springer 用 data-track-action="download pdf" 标记下载按钮。
        PDF 直链模式：/content/pdf/<doi>.pdf
        """
        selectors = [
            'a[data-track-action="download pdf"]',
            'a[href*="/content/pdf/"]',
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

        logger.error("Could not find any download element on Springer page")
        return None

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 Springer 论文元数据。"""
        info = PaperInfo(publisher="springer")

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
