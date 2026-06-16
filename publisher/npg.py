"""
NPG (Nature Publishing Group) 适配器。

URL 模式: https://www.nature.com/articles/...
下载流程: 论文页 -> 提取 PDF 直链 -> fetch() 下载
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class NPGAdapter(PublisherAdapter):
    """Nature Publishing Group 适配器。
    
    覆盖 nature.com 域名下的 Nature, Nature Photonics, Nature Physics 等。
    PDF 直链模式：/articles/<article-id>.pdf
    """

    @property
    def name(self) -> str:
        return "npg"

    def detect(self, url: str) -> bool:
        return "nature.com" in url.lower()

    def check_access(self, page) -> bool:
        """用 PDF 下载链接存在性判断权限，不靠文本匹配。"""
        try:
            el = self.find_download_element(page)
            if el is not None:
                return True
        except Exception:
            pass
        logger.warning("No PDF download link found - likely no access")
        return False

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"NPG page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load NPG page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。
        
        NPG 页面有多个 PDF 链接（主文 PDF + 补充材料 PDF）。
        主文 PDF 选择器优先级：
        1. a[href$=".pdf"] + text "Download PDF"（最精确）
        2. a[data-track="content_download"]（Analytics 跟踪标记的下载按钮）
        3. a[href$=".pdf"]（兜底，取第一个不含 static-content 的）
        """
        # 1. 精确匹配：Download PDF 按钮
        for selector in [
            'a.u-button--primary[href$=".pdf"]',
            'a[data-track="content_download"]',
        ]:
            try:
                elements = page.query_selector_all(selector)
                for el in elements:
                    href = el.get_attribute("href") or ""
                    # 排除补充材料（static-content.springer.com）
                    if "static-content" in href:
                        continue
                    # 排除非文章 PDF（如 supplementary）
                    if "/articles/" not in href and not href.endswith(".pdf"):
                        continue
                    logger.info(f"Found download element: '{selector}' -> {href}")
                    return el
            except Exception as e:
                logger.debug(f"Selector '{selector}' failed: {e}")

        # 2. 兜底：文本匹配
        try:
            elements = page.query_selector_all('a:has-text("Download PDF")')
            for el in elements:
                href = el.get_attribute("href") or ""
                if "static-content" not in href and href.endswith(".pdf"):
                    logger.info(f"Found download via text match: {href}")
                    return el
        except Exception as e:
            logger.debug(f"Text match failed: {e}")

        logger.error("Could not find any download element on NPG page")
        return None

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 NPG 论文元数据。"""
        info = PaperInfo(publisher="npg")

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
