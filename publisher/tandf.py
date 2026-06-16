"""
Taylor & Francis 适配器。

URL 模式: https://www.tandfonline.com/doi/full/10.1080/...
下载流程: 论文页 -> 提取 PDF 直链 (/doi/pdf/DOI) -> fetch() 下载

T&F 没有 citation_* meta 标签，标题从 <title> 提取，DOI 从 URL 提取。
"""

import logging
import re
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class TandFAdapter(PublisherAdapter):
    """Taylor & Francis 适配器。覆盖 tandfonline.com 域名。"""

    @property
    def name(self) -> str:
        return "tandf"

    def detect(self, url: str) -> bool:
        return "tandfonline.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"T&F page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load T&F page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        T&F 页面有 /doi/pdf/DOI 链接（"Download PDF" 文本，show-pdf class）。
        排除 /doi/epdf/（内嵌查看器）和 supplemental 材料链接。
        """
        selectors = [
            'a.show-pdf[href*="/doi/pdf/"]',
            'a:has-text("Download PDF")[href*="/doi/pdf/"]',
            'a[href*="/doi/pdf/"]',
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

        logger.error("Could not find any download element on T&F page")
        return None

    def check_access(self, page) -> bool:
        """T&F 权限检测：有 PDF 下载链接 = 有权限。"""
        pdf_link = page.query_selector('a[href*="/doi/pdf/"]')
        if pdf_link:
            return True

        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 T&F 论文元数据。

        T&F 没有 citation_* meta 标签。标题从 <title> 提取（去掉后缀），
        DOI 从 URL 提取。
        """
        info = PaperInfo(publisher="tandf")

        try:
            info.title = page.evaluate(r"""() => {
                let title = document.title || '';
                // 去掉 "Full article: " 前缀和 " - Get Access" 等后缀
                title = title.replace(/^Full article:\s*/i, '');
                title = title.replace(/\s*[-|]\s*(Taylor & Francis|Tandfonline|Get Access|Full article).*$/i, '');
                return title.trim();
            }""") or ""

            info.doi = page.evaluate(r"""() => {
                const el = document.querySelector('meta[name="citation_doi"]');
                if (el) return el.content;
                // 从 URL 提取 DOI
                const m = window.location.pathname.match(/\/doi\/(?:full|abs|epdf)?\/?(10\.\d{4,}\/[^\s?#]+)/);
                return m ? m[1] : '';
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
