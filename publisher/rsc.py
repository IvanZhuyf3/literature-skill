"""
RSC (Royal Society of Chemistry) 适配器。

URL 模式: https://pubs.rsc.org/en/content/articlelanding/...
下载流程: 论文页 -> 提取 PDF 直链 (/content/articlepdf/...) -> fetch() 下载

RSC 页面简单，有 citation_pdf_url meta 标签直接指向 PDF，fetch() 即可。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class RSCAdapter(PublisherAdapter):
    """RSC 适配器。覆盖 pubs.rsc.org 域名（Chemical Science, Chem. Commun. 等 RSC 期刊）。"""

    @property
    def name(self) -> str:
        return "rsc"

    def detect(self, url: str) -> bool:
        return "rsc.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"RSC page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load RSC page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        RSC 页面上有 "Download this article" 按钮，href 指向 /content/articlepdf/...。
        排除 supplementary 材料链接。
        """
        selectors = [
            'a.btn--primary[href*="articlepdf"]',
            'a[href*="/content/articlepdf/"]',
            'a:has-text("Download this article")',
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

        logger.error("Could not find any download element on RSC page")
        return None

    def check_access(self, page) -> bool:
        """RSC 权限检测：有 PDF 下载链接 = 有权限。"""
        pdf_link = page.query_selector('a[href*="/content/articlepdf/"]')
        if pdf_link:
            return True

        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 RSC 论文元数据。citation_title 和 citation_doi 完整。"""
        info = PaperInfo(publisher="rsc")

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
                // 从 citation_online_date 或 citation_publication_date 兜底
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
