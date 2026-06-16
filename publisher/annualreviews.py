"""
Annual Reviews 适配器。

URL 模式: https://www.annualreviews.org/content/journals/10.1146/...
下载流程: 论文页 -> 构造 /doi/pdf/DOI 直链 -> fetch() 下载

Annual Reviews 使用 Silverchair 平台，/doi/pdf/DOI 直接返回 PDF 字节。
页面上的 PDF 按钮在 <form> 内（href="#"），但 URL 可从 DOI 构造。
citation_* meta 标签完整。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class AnnualReviewsAdapter(PublisherAdapter):
    """Annual Reviews 适配器。覆盖 annualreviews.org 域名。"""

    @property
    def name(self) -> str:
        return "annualreviews"

    def detect(self, url: str) -> bool:
        return "annualreviews.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"Annual Reviews page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load Annual Reviews page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载按钮。

        Annual Reviews 的 PDF 按钮在 <form> 内，href="#"，不是直接链接。
        用 aria-label="Download PDF" 匹配，然后从页面 URL 构造 /doi/pdf/ 直链。
        """
        # 按钮存在性检查（用于 check_access）
        selectors = [
            'a[aria-label="Download PDF"]',
            'a.access-options-icon.fa-file-pdf-o',
            'a:has-text("PDF")',
        ]
        for selector in selectors:
            try:
                element = page.query_selector(selector)
                if element:
                    logger.info(f"Found download element: '{selector}'")
                    return element
            except Exception as e:
                logger.debug(f"Selector '{selector}' failed: {e}")

        logger.error("Could not find any download element on Annual Reviews page")
        return None

    def find_download_url(self, page) -> str:
        """
        从页面 URL 构造 PDF 直链。

        页面 URL: /content/journals/10.1146/annurev-physchem-...
        PDF URL:  /doi/pdf/10.1146/annurev-physchem-...
        """
        import re
        doi_match = re.search(r'(10\.\d{4,}/[^\s?#]+)', page.url)
        if doi_match:
            doi = doi_match.group(1)
            pdf_url = f"https://www.annualreviews.org/doi/pdf/{doi}"
            logger.info(f"Constructed PDF URL: {pdf_url}")
            return pdf_url

        # Fallback: 从 citation_doi meta 提取
        try:
            doi = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_doi"]');
                return el ? el.content : '';
            }""")
            if doi:
                pdf_url = f"https://www.annualreviews.org/doi/pdf/{doi}"
                logger.info(f"Constructed PDF URL from meta: {pdf_url}")
                return pdf_url
        except Exception:
            pass

        logger.error("Could not construct PDF URL")
        return ""

    def check_access(self, page) -> bool:
        """Annual Reviews 权限检测：有 PDF 下载按钮 = 有权限。"""
        pdf_link = page.query_selector('a[aria-label="Download PDF"]')
        if pdf_link:
            return True
        logger.warning("No PDF download button found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 Annual Reviews 论文元数据。citation_* meta 标签完整。"""
        info = PaperInfo(publisher="annualreviews")

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
