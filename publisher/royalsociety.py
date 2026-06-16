"""
Royal Society Publishing 适配器。

URL 模式: https://royalsocietypublishing.org/doi/10.1098/...
下载流程: 论文页 -> 提取 article-pdf 链接 -> resolve 跟随 CDN 重定向
         -> 在 CDN 页面 fetch() 下载（跨域处理）

Royal Society 使用 Silverchair 平台，PDF URL 重定向到 trs.silverchair-cdn.com。
与 AIP 相同的跨域问题，需要 fetch_from_pdf_page = True。
citation_pdf_url meta 标签直接指向 PDF。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class RoyalSocietyAdapter(PublisherAdapter):
    """Royal Society Publishing 适配器。覆盖 royalsocietypublishing.org 域名。"""

    # resolve 后留在 PDF 页面做 fetch（CDN 跨域，同 AIP）
    fetch_from_pdf_page = True

    @property
    def name(self) -> str:
        return "royalsociety"

    def detect(self, url: str) -> bool:
        return "royalsocietypublishing.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"Royal Society page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load Royal Society page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        Silverchair 平台的 PDF 链接是 a.stats-item-pdf-download，
        href 是 /<journal>/article-pdf/doi/<DOI>/.../xxx.pdf。
        也可能有 citation_pdf_url meta 标签。
        """
        selectors = [
            'a.stats-item-pdf-download',
            'a.al-link.pdf[href*="article-pdf"]',
            'a[href*="/article-pdf/"]',
        ]

        for selector in selectors:
            try:
                element = page.query_selector(selector)
                if element:
                    href = element.get_attribute("href") or ""
                    logger.info(f"Found download element: '{selector}' -> {href[:80]}...")
                    return element
            except Exception as e:
                logger.debug(f"Selector '{selector}' failed: {e}")

        logger.error("Could not find any download element on Royal Society page")
        return None

    def resolve_pdf_url(self, page, initial_pdf_url: str) -> Optional[str]:
        """
        跟随 CDN 重定向，返回最终 PDF 页面的 URL。

        article-pdf URL 重定向到 trs.silverchair-cdn.com（带签名 token）。
        从文章页 fetch CDN URL 会 CORS 失败，必须先导航到 PDF URL 让 Chrome 跟随重定向。
        """
        import time
        logger.info(f"Resolving Royal Society PDF URL through CDN redirect...")
        try:
            page.goto(initial_pdf_url, timeout=60000)
            # 等一下让重定向完成
            time.sleep(3)
        except Exception as e:
            logger.debug(f"Navigation exception (non-critical): {e}")

        # Chrome 可能停在 PDF 查看器页面，page.url 应该是 CDN URL
        current = page.url
        if "silverchair" in current or current.endswith(".pdf"):
            logger.info(f"Resolved to CDN URL: {current[:80]}...")
            return current

        # 没到 CDN，可能停在文章页（重定向没发生）
        logger.warning(f"Did not reach CDN, current URL: {current[:80]}...")
        return initial_pdf_url

    def check_access(self, page) -> bool:
        """Royal Society 权限检测：有 PDF 下载链接 = 有权限。"""
        pdf_link = page.query_selector('a.stats-item-pdf-download')
        if pdf_link:
            return True
        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """
        提取 Royal Society 论文元数据。

        citation_* meta 标签大部分完整。
        citation_date 可能不存在，尝试其他 meta 标签兜底。
        """
        info = PaperInfo(publisher="royalsociety")

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
                // fallback: citation_publication_date or citation_online_date
                const alt1 = document.querySelector('meta[name="citation_publication_date"]');
                if (alt1) return alt1.content;
                const alt2 = document.querySelector('meta[name="citation_online_date"]');
                return alt2 ? alt2.content : '';
            }""") or ""

            info.authors = page.evaluate(r"""() => {
                const metas = document.querySelectorAll('meta[name="citation_author"]');
                return Array.from(metas).map(m => m.content).join(', ');
            }""") or ""

            info.url = page.url

        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")

        return info
