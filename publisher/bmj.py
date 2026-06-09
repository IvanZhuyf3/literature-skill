"""
BMJ 适配器。

URL 模式: https://xxx.bmj.com/content/...
下载流程: 论文页 -> 提取 PDF 直链 (.full.pdf) -> fetch() 下载

BMJ 子域名众多（bmj.com, bmjimmunology.bmj.com, gut.bmj.com 等），
统一用 bmj.com 匹配。页面有 a.article-pdf-download 链接和 citation_pdf_url meta 标签。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class BMJAdapter(PublisherAdapter):
    """BMJ 适配器。覆盖所有 *.bmj.com 子域名。"""

    @property
    def name(self) -> str:
        return "bmj"

    def detect(self, url: str) -> bool:
        return ".bmj.com" in url.lower() or "//bmj.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"BMJ page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load BMJ page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        BMJ 页面有 a.article-pdf-download 链接，href 是 .full.pdf。
        """
        selectors = [
            'a.article-pdf-download',
            'a[href$=".full.pdf"]',
            'a[href*=".full.pdf"]',
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

        logger.error("Could not find any download element on BMJ page")
        return None

    def check_access(self, page) -> bool:
        """BMJ 权限检测：有 PDF 下载链接 = 有权限。"""
        pdf_link = page.query_selector('a.article-pdf-download')
        if pdf_link:
            return True
        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """
        提取 BMJ 论文元数据。

        citation_* meta 标签大部分完整。
        citation_date 可能不存在，尝试其他 meta 标签兜底。
        """
        info = PaperInfo(publisher="bmj")

        try:
            info.title = page.evaluate(r"""() => {
                const el = document.querySelector('meta[name="citation_title"]');
                return el ? el.content : '';
            }""") or ""

            info.doi = page.evaluate(r"""() => {
                const el = document.querySelector('meta[name="citation_doi"]');
                return el ? el.content : '';
            }""") or ""

            info.year = page.evaluate(r"""() => {
                const el = document.querySelector('meta[name="citation_date"]');
                if (el) return el.content;
                const alt = document.querySelector('meta[name="citation_online_date"]');
                return alt ? alt.content : '';
            }""") or ""

            info.authors = page.evaluate(r"""() => {
                const metas = document.querySelectorAll('meta[name="citation_author"]');
                return Array.from(metas).map(m => m.content).join(', ');
            }""") or ""

            info.url = page.url

        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")

        return info
