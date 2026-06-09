"""
APS (American Physical Society) 适配器。

URL 模式: https://journals.aps.org/prl/abstract/10.1103/...
下载流程: 论文页 -> 提取 PDF 直链 (/journal/pdf/DOI) -> fetch() 下载

APS 页面简单，PDF 链接是 /journal/pdf/DOI，fetch() 直接返回 %PDF。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class APSAdapter(PublisherAdapter):
    """APS 适配器。覆盖 journals.aps.org 域名（PRL, PRC, PRB, PRA 等所有 APS 期刊）。"""

    @property
    def name(self) -> str:
        return "aps"

    def detect(self, url: str) -> bool:
        return "aps.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"APS page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load APS page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        APS 页面上有一个 PDF 按钮（sm-primary-button class），href 是 /journal/pdf/DOI。
        排除 supplemental 材料链接。
        """
        selectors = [
            'a.sm-primary-button[href*="/pdf/"]',
            'a[href*="/pdf/"]:not([href*="/supplemental/"])',
            'a:has-text("PDF")',
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

        logger.error("Could not find any download element on APS page")
        return None

    def check_access(self, page) -> bool:
        """APS 权限检测：有 PDF 下载链接 = 有权限。"""
        pdf_link = page.query_selector('a.sm-primary-button[href*="/pdf/"]')
        if pdf_link:
            return True

        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 APS 论文元数据。citation_* meta 标签完整。"""
        info = PaperInfo(publisher="aps")

        try:
            info.title = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_title"]');
                return el ? el.content : '';
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
