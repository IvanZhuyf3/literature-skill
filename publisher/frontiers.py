"""
Frontiers 适配器。

URL 模式: https://www.frontiersin.org/journals/.../articles/10.3389/.../full
下载流程: 论文页 -> 提取 PDF 直链 (/.../pdf) -> fetch() 下载

Frontiers 是完全开放获取出版商，页面有直接 PDF 下载链接。
citation_pdf_url meta 标签也直接指向 PDF。fetch() 即可。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class FrontiersAdapter(PublisherAdapter):
    """Frontiers 适配器。覆盖 frontiersin.org 域名。"""

    @property
    def name(self) -> str:
        return "frontiers"

    def detect(self, url: str) -> bool:
        return "frontiersin.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"Frontiers page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load Frontiers page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        Frontiers 有两处 PDF 链接：
        - a.DownloadArticleButton__action：主下载按钮
        - a.ToolbarDownload__action：工具栏下载链接
        """
        selectors = [
            'a.DownloadArticleButton__action',
            'a.ToolbarDownload__action',
            'a[href$="/pdf"]',
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

        logger.error("Could not find any download element on Frontiers page")
        return None

    def check_access(self, page) -> bool:
        """Frontiers 是 OA 出版商，有 PDF 链接 = 有权限。"""
        pdf_link = page.query_selector('a.DownloadArticleButton__action')
        if pdf_link:
            return True
        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 Frontiers 论文元数据。citation_* meta 标签大部分完整。"""
        info = PaperInfo(publisher="frontiers")

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
