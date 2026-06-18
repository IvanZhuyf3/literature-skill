"""SAGE Publications 适配器。

URL 模式: journals.sagepub.com
下载流程: 论文页 -> 提取 PDF 直链 (/doi/pdf/<DOI>) -> fetch() 下载

SAGE 页面没有 citation_pdf_url meta 标签。
PDF 直链模式: https://journals.sagepub.com/doi/pdf/<DOI>
"""

import logging
from typing import Optional, Any
from urllib.parse import urljoin

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class SAGEAdapter(PublisherAdapter):
    """SAGE Publications 适配器。覆盖 journals.sagepub.com 域名。"""

    @property
    def name(self) -> str:
        return "sage"

    def detect(self, url: str) -> bool:
        return "journals.sagepub.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=15000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"SAGE page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load SAGE page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF/EPUB 下载链接。

        SAGE 页面上有 "PDF/EPUB" 或 "View PDF/EPUB" 链接，
        href 指向 /doi/reader/<DOI>。
        """
        selectors = [
            'a[href*="/doi/reader/"]',
            'a:has-text("PDF/EPUB")',
            'a:has-text("View PDF")',
            'a[href*="/doi/pdf/"]',
            'section.format--pdf_epub a',
            '[class*="pdf"] a[href*="/doi/"]',
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

        logger.error("Could not find any download element on SAGE page")
        return None

    def find_download_url(self, page) -> str | None:
        """Extract PDF URL from the page.

        Strategy:
        1. Try direct /doi/pdf/<DOI> URL pattern first (most reliable)
        2. Fallback to /doi/reader/<DOI> link
        """
        # Strategy 1: Construct direct PDF URL from the DOI in the page URL
        page_url = page.url
        import re
        doi_match = re.search(r'/doi/(?:full/)?(10\.\d{4,}/[^/?#]+)', page_url)
        if doi_match:
            doi = doi_match.group(1)
            pdf_url = urljoin(page_url, f"/doi/pdf/{doi}")
            logger.info(f"Constructed direct PDF URL: {pdf_url}")
            return pdf_url

        # Strategy 2: Find /doi/reader/ link and convert to /doi/pdf/
        try:
            reader_link = page.query_selector('a[href*="/doi/reader/"]')
            if reader_link:
                href = reader_link.get_attribute("href") or ""
                if href:
                    # Convert reader path to pdf path
                    pdf_href = href.replace("/doi/reader/", "/doi/pdf/")
                    absolute = urljoin(page_url, pdf_href)
                    logger.info(f"Converted reader URL to PDF URL: {absolute}")
                    return absolute
        except Exception as e:
            logger.debug(f"Reader link fallback failed: {e}")

        # Strategy 3: Find any /doi/pdf/ link
        try:
            pdf_link = page.query_selector('a[href*="/doi/pdf/"]')
            if pdf_link:
                href = pdf_link.get_attribute("href") or ""
                if href:
                    absolute = urljoin(page_url, href)
                    logger.info(f"Found /doi/pdf/ link: {absolute}")
                    return absolute
        except Exception:
            pass

        logger.warning("Could not find any PDF URL on SAGE page")
        return None

    def check_access(self, page) -> bool:
        """SAGE 权限检测：有 PDF/EPUB 链接 = 有权限。"""
        pdf_link = page.query_selector('a[href*="/doi/reader/"]')
        if pdf_link:
            return True

        # Also check for access denied indicators
        try:
            body_text = page.inner_text("body")
            blocked = ["Access Denied", "Purchase this article", "Sign in to access"]
            for b in blocked:
                if b.lower() in body_text.lower():
                    logger.warning(f"Access blocked: '{b}' found on page")
                    return False
        except Exception:
            pass

        logger.warning("No PDF/EPUB link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 SAGE 论文元数据。

        SAGE uses Dublin Core metadata (dc.Title, dc.Creator, dc.Date, dc.Identifier).
        Falls back to Open Graph and citation tags.
        """
        info = PaperInfo(publisher="sage")

        try:
            # SAGE primarily uses dc.* meta tags
            info.title = page.evaluate("""() => {
                const el = document.querySelector('meta[name="dc.Title"], meta[name="DC.Title"], meta[property="og:title"], meta[name="citation_title"]');
                return el ? el.content : '';
            }""") or ""

            info.doi = page.evaluate("""() => {
                const el = document.querySelector('meta[name="dc.Identifier"], meta[name="citation_doi"], meta[name="publication_doi"]');
                return el ? el.content : '';
            }""") or ""

            info.year = page.evaluate("""() => {
                const el = document.querySelector('meta[name="dc.Date"], meta[name="citation_date"], meta[name="citation_online_date"]');
                if (el) {
                    const v = el.content;
                    const m = v.match(/\\b(\\d{4})\\b/);
                    return m ? m[1] : v;
                }
                return '';
            }""") or ""

            info.authors = page.evaluate("""() => {
                const el = document.querySelector('meta[name="dc.Creator"], meta[name="citation_author"], meta[property="article:author"]');
                return el ? el.content : '';
            }""") or ""

            info.url = page.url

        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")

        return info
