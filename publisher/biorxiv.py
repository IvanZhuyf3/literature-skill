"""bioRxiv/medRxiv 适配器。

URL 模式: biorxiv.org, medrxiv.org
下载流程: 简单型 — citation_pdf_url meta 标签直接指向 PDF
覆盖: bioRxiv, medRxiv 全部预印本（开放获取）
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class BiorxivAdapter(PublisherAdapter):
    """bioRxiv/medRxiv 预印本适配器。

    PDF 直链模式: /content/<doi>/<doi>v1.full.pdf
    有 citation_pdf_url meta 标签直接指向 PDF。
    """

    @property
    def name(self) -> str:
        return "biorxiv"

    def detect(self, url: str) -> bool:
        return "biorxiv.org" in url.lower() or "medrxiv.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"bioRxiv page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load bioRxiv page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        # Delegate to find_download_url which handles both meta tag and DOM
        return None  # We handle URL extraction directly in find_download_url

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
                absolute = urljoin(page.url, pdf_url)
                logger.info(f"Found PDF via citation_pdf_url: {absolute[:80]}")
                return absolute
        except Exception:
            pass
        
        # fallback: look for "Download" links to .full.pdf
        try:
            elements = page.query_selector_all('a[href*=".full.pdf"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if href:
                    absolute = urljoin(page.url, href)
                    logger.info(f"Found download link: {absolute[:80]}")
                    return absolute
        except Exception:
            pass

        logger.warning("Could not find any download URL on bioRxiv page")
        return None

    def get_paper_metadata(self, page) -> PaperInfo:
        info = PaperInfo(publisher="biorxiv")
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
