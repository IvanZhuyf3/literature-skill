"""
ACS Publications 适配器。

URL 模式: https://pubs.acs.org/doi/10.1021/...
下载流程: 论文页 → 点击 PDF 按钮 → 下载 PDF
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class ACSAdapter(PublisherAdapter):
    """American Chemical Society (ACS) Publications 适配器。"""

    @property
    def name(self) -> str:
        return "acs"

    def detect(self, url: str) -> bool:
        return "pubs.acs.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        """
        导航到 ACS 论文页。
        ACS 的 /doi/abs/ 和 /doi/full/ 都可以，但我们要确保到全文页面。
        """
        # 规范化 URL：确保是 /doi/full/ 或 /doi/ 页面
        url = url.replace("/doi/abs/", "/doi/").replace("/doi/full/", "/doi/")

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            # networkidle 在 ACS 页面上经常超时（太多分析脚本），放宽到 60s
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"ACS page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load ACS page: {e}")
            return False

    def check_access(self, page) -> bool:
        """
        检查是否有权限访问 ACS 论文。

        用 PDF 链接存在性判断，不依赖基类的文本匹配。
        ACS 页面正文/侧栏常包含 "Purchase"、"Access" 等字样，
        基类文本匹配会误报（参见 error_log E-AAAS-01、E-SPRINGER-01）。
        """
        try:
            # 有任何 PDF 相关链接就说明有权限
            pdf_link = page.query_selector('a[href*="/doi/pdf/"]')
            if pdf_link:
                return True
            # 也检查 Hi-Res PDF 按钮
            hires = page.query_selector('a:has-text("Hi-Res PDF")')
            if hires and hires.is_visible():
                return True
            # 通用 PDF 按钮
            for sel in ['a[title="PDF"]', 'a.pdf-link']:
                el = page.query_selector(sel)
                if el and el.is_visible():
                    return True
        except Exception as e:
            logger.debug(f"check_access exception: {e}")

        # 最后 fallback：如果页面有 citation_doi meta 标签，说明论文页确实加载了
        try:
            doi = page.query_selector('meta[name="citation_doi"]')
            if doi:
                logger.info("check_access: citation_doi found, assuming access OK")
                return True
        except Exception:
            pass

        logger.warning("check_access: no PDF link or citation_doi found, access denied")
        return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        在 ACS 页面中定位 PDF 下载链接。

        尝试顺序：
        1. PDF 按钮链接（顶栏）
        2. 链接中包含 /doi/pdf/ 的
        3. 文本包含 "PDF" 的链接
        4. 高保真 PDF 链接（Hi-Res PDF）
        """
        selectors = [
            # 高保真 PDF（ACS 特色）
            'a:has-text("Hi-Res PDF")',
            # 普通 PDF 链接
            'a[href*="/doi/pdf/"]',
            # PDF 按钮
            'a.pdf-link',
            'a[title="PDF"]',
            # 通用 fallback
            'a:has-text("PDF")',
        ]

        for selector in selectors:
            try:
                element = page.query_selector(selector)
                if element and element.is_visible():
                    href = element.get_attribute("href") or ""
                    logger.info(
                        f"Found download element with selector '{selector}': {href}"
                    )
                    return element
            except Exception as e:
                logger.debug(f"Selector '{selector}' failed: {e}")
                continue

        # 最终兜底：遍历所有链接找 PDF
        logger.warning("Primary selectors failed, trying link scan...")
        try:
            links = page.query_selector_all("a")
            for link in links:
                try:
                    href = link.get_attribute("href") or ""
                    text = link.inner_text().strip()
                    if "/doi/pdf/" in href or text.lower() in ["pdf", "download pdf"]:
                        if link.is_visible():
                            logger.info(f"Found PDF link via scan: {href} ({text})")
                            return link
                except Exception:
                    continue
        except Exception as e:
            logger.error(f"Link scan failed: {e}")

        logger.error("Could not find any download element on ACS page")
        return None

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 ACS 论文元数据。"""
        info = PaperInfo(publisher="acs")

        try:
            # ACS 使用 citation_ 前缀的 meta 标签
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

    def handle_post_click(self, page, browser) -> bool:
        """
        ACS 点击 PDF 后的处理。

        通常直接触发下载，但有时会打开新标签页显示 PDF。
        """
        import time

        # 等待下载触发或新标签页
        time.sleep(3)

        # 检查是否有新标签页打开（PDF 预览）
        for ctx in browser.contexts:
            for p in ctx.pages:
                url = p.url
                if url.endswith(".pdf") or "/doi/pdf/" in url:
                    logger.info(f"PDF opened in new tab: {url}")
                    # 这种情况下，PDF URL 就是下载链接，可以直接用 requests 下载
                    # 但我们优先让浏览器的下载流程处理
                    return True

        return True
