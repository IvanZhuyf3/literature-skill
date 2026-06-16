"""
IOP (Institute of Physics) 适配器。

URL 模式: https://iopscience.iop.org/article/10.1088/...
下载流程: 论文页 -> 提取 PDF 直链 (/article/DOI/pdf) -> fetch() 下载

IOP 页面简单，有 citation_pdf_url meta 标签，fetch() 直接返回 PDF。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class IOPAdapter(PublisherAdapter):
    """IOP 适配器。覆盖 iopscience.iop.org 域名（New Journal of Physics, Nanotechnology 等）。"""

    @property
    def name(self) -> str:
        return "iop"

    def detect(self, url: str) -> bool:
        return "iop.org" in url.lower() or "iopscience" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"IOP page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load IOP page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        IOP 页面上有 "Download Article PDF" 按钮，href 是 /article/DOI/pdf。
        """
        selectors = [
            'a.wd-jnl-art-pdf-button-main',
            'a.pdf-button-2nd',
            'a[href$="/pdf"][href*="/article/"]',
            'a:has-text("Download Article PDF")',
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

        logger.error("Could not find any download element on IOP page")
        return None

    def check_access(self, page) -> bool:
        """IOP 权限检测：有 PDF 下载链接 = 有权限。"""
        pdf_link = page.query_selector('a.wd-jnl-art-pdf-button-main')
        if pdf_link:
            return True

        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 IOP 论文元数据。citation_title 和 citation_doi 完整。"""
        info = PaperInfo(publisher="iop")

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
                if (el) return el.content;
                const alt = document.querySelector('meta[name="citation_online_date"]');
                return alt ? alt.content : '';
            }""") or ""

            info.authors = page.evaluate("""() => {
                const metas = document.querySelectorAll('meta[name="citation_author"]');
                return Array.from(metas).map(m => m.content).join(', ');
            }""") or ""

            info.url = page.url

        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")

        return info
