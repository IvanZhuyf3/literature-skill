"""
eLife 适配器。

URL 模式: https://elifesciences.org/articles/106728
下载流程: 论文页 -> 从 DOM 提取 PDF 下载链接 -> fetch() 下载

eLife 是完全开放获取出版商。页面有 Article PDF 下载链接（article-download-links-list__link）。
也可从文章 ID 构造 CDN 直链（cdn.elifesciences.org/articles/{id}/elife-{id}-v1.pdf）。
没有 citation_* meta 标签，metadata 从 dc.* meta 标签和 <title> 提取。
"""

import logging
import re
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class eLifeAdapter(PublisherAdapter):
    """eLife 适配器。覆盖 elifesciences.org 域名。"""

    @property
    def name(self) -> str:
        return "elife"

    def detect(self, url: str) -> bool:
        return "elifesciences.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"eLife page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load eLife page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 Article PDF 下载链接。

        eLife 的 Article PDF 链接是 a.article-download-links-list__link，
        需要排除 Figures PDF 链接。
        """
        try:
            elements = page.query_selector_all('a.article-download-links-list__link')
            for el in elements:
                href = el.get_attribute("href") or ""
                text = el.inner_text() or ""
                if "Article PDF" in text or ("elife-" in href and "-v" in href
                                             and "figures" not in href):
                    logger.info(f"Found download element: Article PDF -> {href[:80]}...")
                    return el
        except Exception as e:
            logger.debug(f"article-download-links-list__link search failed: {e}")

        # Fallback: Download 按钮
        try:
            el = page.query_selector('a.button--action.icon-download')
            if el:
                logger.info("Found download button (fallback)")
                return el
        except Exception:
            pass

        logger.error("Could not find any download element on eLife page")
        return None

    def find_download_url(self, page) -> str:
        """
        从文章 ID 构造 CDN 直链。

        eLife 的 /download/ URL 会触发导航导致 Execution context destroyed。
        直接用 CDN URL 更稳定：cdn.elifesciences.org/articles/{id}/elife-{id}-v1.pdf
        """
        import re
        # 从 URL 提取文章 ID
        m = re.search(r'/articles/(\d+)', page.url)
        if m:
            article_id = m.group(1)
            cdn_url = f"https://cdn.elifesciences.org/articles/{article_id}/elife-{article_id}-v1.pdf"
            logger.info(f"Constructed CDN URL: {cdn_url}")
            return cdn_url
        return ""

    def check_access(self, page) -> bool:
        """eLife 是 OA 出版商，有 PDF 链接 = 有权限。"""
        pdf_link = page.query_selector('a.article-download-links-list__link')
        if pdf_link:
            return True
        logger.warning("No PDF download link found")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """
        提取 eLife 论文元数据。

        eLife 没有 citation_* meta 标签，使用 dc.* meta 标签：
        - dc.title -> 标题
        - dc.identifier -> DOI（格式：doi:10.7554/eLife.XXXXX）
        - dc.date -> 日期
        - dc.contributor -> 作者
        """
        info = PaperInfo(publisher="elife")

        try:
            info.title = page.evaluate(r"""() => {
                const el = document.querySelector('meta[name="dc.title"]');
                if (el) return el.content;
                // fallback: <title> 去掉 " | eLife" 后缀
                let t = document.title || '';
                t = t.replace(/\s*\|\s*eLife\s*$/i, '');
                return t;
            }""") or ""

            info.doi = page.evaluate(r"""() => {
                const el = document.querySelector('meta[name="dc.identifier"]');
                if (el) {
                    let v = el.content;
                    // 去掉 "doi:" 前缀
                    return v.replace(/^doi:\s*/i, '');
                }
                return '';
            }""") or ""

            info.year = page.evaluate("""() => {
                const el = document.querySelector('meta[name="dc.date"]');
                return el ? el.content : '';
            }""") or ""

            info.authors = page.evaluate("""() => {
                const metas = document.querySelectorAll('meta[name="dc.contributor"]');
                return Array.from(metas).map(m => m.content).join(', ');
            }""") or ""

            info.url = page.url

        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")

        return info
