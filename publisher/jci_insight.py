"""JCI Insight 适配器。

URL 模式: insight.jci.org
下载流程: 简单型 — citation_pdf_url meta 标签直接指向 PDF
覆盖: JCI Insight 全部论文（开放获取）
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class JCIInsightAdapter(PublisherAdapter):
    """JCI Insight 适配器。

    美国临床研究学会 (ASCI) 出版的开放获取期刊。
    PDF 直链模式: /articles/view/<id>/pdf
    有 citation_pdf_url meta 标签。
    """

    @property
    def name(self) -> str:
        return "jci_insight"

    def detect(self, url: str) -> bool:
        return "insight.jci.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"JCI Insight page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load JCI Insight page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        # JCI Insight is OA — skip check_access text matching
        # (the default check_access looks for "Access" text and false-positives)
        return None  # URL extraction handled in find_download_url

    def find_download_url(self, page) -> str | None:
        """Extract PDF URL from citation_pdf_url meta tag or DOM."""
        from urllib.parse import urljoin
        
        # primary: citation_pdf_url meta tag
        try:
            pdf_url = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_pdf_url"]');
                return el ? el.content : null;
            }""")
            if pdf_url:
                # Fix: JCI returns http:// but the site runs on https://
                absolute = urljoin(page.url, pdf_url)
                absolute = absolute.replace("http://", "https://")
                logger.info(f"Found PDF via citation_pdf_url: {absolute[:80]}")
                return absolute
        except Exception:
            pass

        # fallback: <a> with /pdf in href
        try:
            elements = page.query_selector_all('a[href*="/pdf"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if "view" in href:  # /articles/view/<id>/pdf
                    absolute = urljoin(page.url, href)
                    logger.info(f"Found download link: {absolute[:80]}")
                    return absolute
        except Exception:
            pass

        logger.warning("Could not find any download URL on JCI Insight page")
        return None

    def check_access(self, page) -> bool:
        """JCI Insight is open access — override default text matching."""
        return True

    def get_paper_metadata(self, page) -> PaperInfo:
        info = PaperInfo(publisher="jci_insight")
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
