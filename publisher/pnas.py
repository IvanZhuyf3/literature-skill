"""
PNAS (Proceedings of the National Academy of Sciences) 适配器。

URL 模式: https://www.pnas.org/doi/10.1073/pnas.XXXXXX
下载流程: 论文页 -> 提取 PDF 直链 (/doi/pdf/...) -> fetch() 下载

PNAS 使用 Silverchair 平台，PDF 链接模式与 AAAS 类似。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class PNASAdapter(PublisherAdapter):
    """PNAS 适配器。覆盖 pnas.org 域名。"""

    @property
    def name(self) -> str:
        return "pnas"

    def detect(self, url: str) -> bool:
        return "pnas.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"PNAS page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load PNAS page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        PNAS (Silverchair) 页面的 PDF 链接通常:
        - /doi/pdf/10.1073/pnas.XXXX
        - 可能有 PDF 按钮或 "Download PDF" 链接
        """
        selectors = [
            'a[href*="/doi/pdf/"]',
            'a:has-text("PDF")',
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

        logger.error("Could not find any download element on PNAS page")
        return None

    def check_access(self, page) -> bool:
        """PNAS 权限检测：有 PDF 下载链接 = 有权限。"""
        pdf_link = page.query_selector('a[href*="/doi/pdf/"]')
        if pdf_link:
            return True

        # 试试其他 PDF 指示
        pdf_text = page.query_selector('a:has-text("PDF")')
        if pdf_text:
            return True

        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 PNAS 论文元数据。"""
        info = PaperInfo(publisher="pnas")

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
