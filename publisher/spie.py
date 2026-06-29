"""
SPIE Digital Library 适配器。

URL 模式: https://www.spiedigitallibrary.org/journals/.../10.1117/...
下载流程: 论文页 -> citation_pdf_url meta 标签 -> fetch() 下载

SPIE 页面有完整的 citation_* meta 标签，citation_pdf_url 直接指向 PDF。
Open Access 文章可直接下载，订阅文章需机构权限。
"""

import logging
from typing import Optional, Any
from urllib.parse import urljoin

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class SPIEAdapter(PublisherAdapter):
    """SPIE Digital Library 适配器。覆盖 spiedigitallibrary.org 域名。"""

    @property
    def name(self) -> str:
        return "spie"

    def detect(self, url: str) -> bool:
        return "spiedigitallibrary.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"SPIE page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load SPIE page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载按钮。

        SPIE 有 'DOWNLOAD PAPER' 按钮 (a.btn-DownloadPaper)。
        但实际下载用 citation_pdf_url meta 标签更可靠。
        """
        selectors = [
            'a.btn-DownloadPaper',
            'a.DownloadSaveButton1',
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

        logger.error("Could not find any download element on SPIE page")
        return None

    def find_download_url(self, page) -> Optional[str]:
        """
        构造 SPIE PDF 直链。

        citation_pdf_url meta 标签指向 HTML interstitial（返回 HTML 非 PDF）。
        实际 PDF 下载端点是 /Proceedings/Download?urlId={DOI_URL_ENCODED}，
        需带 Referer header（engine 的 cookie_download 会自动处理）。
        来源：CDP recording 实测 2026-06-29。
        """
        # Extract DOI from page meta or URL
        doi = page.evaluate("""() => {
            const el = document.querySelector('meta[name="citation_doi"]');
            return el ? el.content : '';
        }""") or ""

        if not doi:
            # Fallback: try citation_pdf_url (may be HTML interstitial)
            pdf_url = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_pdf_url"]');
                return el ? el.content : null;
            }""")
            if pdf_url:
                if not pdf_url.startswith(("http://", "https://")):
                    pdf_url = urljoin(page.url, pdf_url)
                return pdf_url
            return None

        # Build direct download URL from DOI
        from urllib.parse import quote
        pdf_url = f"https://www.spiedigitallibrary.org/Proceedings/Download?urlId={quote(doi, safe='')}"
        logger.info(f"SPIE PDF URL (direct): {pdf_url}")
        return pdf_url

    def check_access(self, page) -> bool:
        """有 citation_doi meta 标签就说明是论文页面，可构造下载 URL。"""
        has_doi = page.evaluate("""() => {
            const el = document.querySelector('meta[name="citation_doi"]');
            return !!el;
        }""")
        if has_doi:
            return True
        # Fallback: any download element present
        has_pdf = page.evaluate("""() => {
            const pdfMeta = document.querySelector('meta[name="citation_pdf_url"]');
            const dlBtn = document.querySelector('a.btn-DownloadPaper');
            return !!(pdfMeta || dlBtn);
        }""")
        if has_pdf:
            return True
        logger.warning("No citation_doi or download link found")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 SPIE 论文元数据。citation_* meta 标签完整。"""
        info = PaperInfo(publisher="spie")

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
                const el = document.querySelector('meta[name="citation_publication_date"]');
                if (el) return el.content;
                const alt = document.querySelector('meta[name="citation_date"]');
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
