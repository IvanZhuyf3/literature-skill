"""
Wiley Online Library 适配器。

URL 模式: https://onlinelibrary.wiley.com/doi/10.1002/...
下载流程: 文章信息页（提取 metadata）-> 跳转 epdf 查看器 -> 提取 pdfdirect 直链 -> fetch() 下载

Wiley 有两种页面：
- /doi/DOI      → 文章信息页（有完整的 citation_* meta 标签，/doi/pdf/ 返回 HTML 不是 PDF）
- /doi/epdf/DOI → 内嵌 PDF 查看器（有 /doi/pdfdirect/DOI?download=true，真正的 PDF）

策略：
1. navigate_to_paper: 去文章信息页（metadata 完整）
2. get_paper_metadata: 在文章页提取 citation_* meta
3. resolve_pdf_url: 跳到 epdf 页面，提取 pdfdirect 直链
4. 回到文章页做 fetch()（保持 session）
"""

import logging
import re
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class WileyAdapter(PublisherAdapter):
    """Wiley Online Library 适配器。覆盖 onlinelibrary.wiley.com 域名。"""

    # resolve 后留在 epdf 页面做 fetch（同域，无 CORS 问题）
    fetch_from_pdf_page = True

    @property
    def name(self) -> str:
        return "wiley"

    def detect(self, url: str) -> bool:
        return "wiley.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        """导航到文章信息页（不跳 epdf）。metadata 在这里提取。"""
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"Wiley page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load Wiley page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接（文章信息页上）。

        注意：文章页上的 /doi/pdf/ 链接返回 HTML，不是真正的 PDF。
        真正的 PDF 在 epdf 页面的 /doi/pdfdirect/ 链接。
        这里仅用于 check_access 和流程兼容。
        """
        selectors = [
            'a:has-text("Download PDF")',
            'a[href*="/doi/pdf/"]:not([href*="/doi/epdf/"])',
            'a:has-text("PDF")',
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

        logger.error("Could not find any download element on Wiley page")
        return None

    def resolve_pdf_url(self, page, initial_pdf_url: str) -> Optional[str]:
        """
        跳转到 epdf 页面，提取 /doi/pdfdirect/ 真正的 PDF 下载链接。

        文章信息页的 /doi/pdf/ 返回 HTML，不是 PDF。
        epdf 页面有 /doi/pdfdirect/DOI?download=true（真正的 PDF）。
        """
        # 从当前 URL 提取 DOI
        doi = self._extract_doi(page.url)
        if not doi:
            logger.error(f"Cannot extract DOI from URL: {page.url}")
            return None

        epdf_url = f"https://onlinelibrary.wiley.com/doi/epdf/{doi}"
        logger.info(f"Navigating to epdf viewer: {epdf_url}")

        try:
            page.goto(epdf_url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
        except Exception as e:
            logger.error(f"Failed to load epdf page: {e}")
            return None

        # 在 epdf 页面找 pdfdirect 链接
        for sel in [
            'a[href*="/doi/pdfdirect/"][href*="download=true"]',
            'a[href*="/doi/pdfdirect/"]',
        ]:
            try:
                element = page.query_selector(sel)
                if element:
                    href = element.get_attribute("href") or ""
                    if not href.startswith("http"):
                        from urllib.parse import urljoin
                        href = urljoin(page.url, href)
                    logger.info(f"Found pdfdirect link: {href}")
                    return href
            except Exception as e:
                logger.debug(f"Selector '{sel}' failed: {e}")

        logger.error("No pdfdirect link found on epdf page")
        return None

    def _extract_doi(self, url: str) -> str:
        """从 URL 提取 DOI（如 10.1002/anie.1518521）。"""
        m = re.search(r'/doi/(?:epdf|pdf|abs|full)?/?(10\.\d{3,}/[^\s?#]+)', url)
        return m.group(1) if m else ""

    def check_access(self, page) -> bool:
        """Wiley 权限检测：有 PDF 下载链接 = 有权限。"""
        for sel in [
            'a:has-text("Download PDF")',
            'a[href*="/doi/pdf/"]:not([href*="/doi/epdf/"])',
        ]:
            if page.query_selector(sel):
                return True

        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 Wiley 论文元数据（在文章信息页，有完整的 citation_* meta 标签）。"""
        info = PaperInfo(publisher="wiley")

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
