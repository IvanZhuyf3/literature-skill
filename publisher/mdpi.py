"""
MDPI 适配器。

URL 模式: https://www.mdpi.com/1424-8220/26/10/2941
下载流程: 论文页 -> 提取 PDF 直链 (/.../pdf?version=...) -> fetch() 下载

MDPI 是完全开放获取出版商，页面有直接的 PDF 下载链接（a.UD_ArticlePDF）。
虽然 Download 按钮展开是下拉菜单（PDF/XML），但 DOM 中有独立的 PDF 链接元素。
citation_pdf_url meta 标签也直接指向 PDF。fetch() 即可。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class MDPIAdapter(PublisherAdapter):
    """MDPI 适配器。覆盖 mdpi.com 域名。"""

    @property
    def name(self) -> str:
        return "mdpi"

    def detect(self, url: str) -> bool:
        return "mdpi.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"MDPI page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load MDPI page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        MDPI 页面上有多个 PDF 链接：
        - a.UD_ArticlePDF：文章 PDF 下载链接（在下载下拉菜单中）
        - a.button--color-inversed：同上，不同 CSS class
        - a[href$="/pdf"]：URL 以 /pdf 结尾的链接

        优先用 UD_ArticlePDF class 精确匹配。
        """
        selectors = [
            'a.UD_ArticlePDF',
            'a.button--color-inversed[href*="/pdf"]',
            'a[href*="/pdf"][href*="mdpi.com"]',
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

        logger.error("Could not find any download element on MDPI page")
        return None

    def check_access(self, page) -> bool:
        """MDPI 是 OA 出版商，有 PDF 链接 = 有权限。"""
        pdf_link = page.query_selector('a.UD_ArticlePDF')
        if pdf_link:
            return True
        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 MDPI 论文元数据。citation_* meta 标签大部分完整。"""
        info = PaperInfo(publisher="mdpi")

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
                // fallback: citation_online_date
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
