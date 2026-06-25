"""
AACR (American Association for Cancer Research) 适配器。

URL 模式: https://aacrjournals.org/<journal>/article/<vol>/<issue>/<page>/<id>/<slug>
          覆盖 Cancer Research, Clinical Cancer Research, Cancer Research Communications,
          Molecular Cancer Research, Cancer Immunology Research, Blood Cancer Discovery 等
          所有 AACR 旗下期刊（均托管在 Silverchair 平台 aacrjournals.org）。

下载流程: 简单型 + cookie_download 兜底
  1. 文章页 <a class="al-link pdf ..."> 的 href 指向
     /<journal>/article-pdf/<vol>/<issue>/<page>/<id>/<doi>.pdf
     （citation_pdf_url meta 标签同值）
  2. 该 URL 返回 302 重定向到 watermark*.silverchair.com（带签名 token）。
  3. 页面上下文 fetch() 因跨域重定向 (CORS) 失败 →
     引擎自动 fallback 到 cookie_download（requests 跟随 302，无 CORS 限制）→ 成功。

关键发现:
  - 必须走 cookie_download（browser_download 的 fetch() 会被跨域 CDN 拦截）。
  - /article-pdf/ 链接是真正的全文 PDF；-s01/-s02.pdf 是 supplementary material，
    选择器用 a[href*="/article-pdf/"] 精确匹配，避免误选 supplementary 链接。
"""

import logging
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class AACRAdapter(PublisherAdapter):
    """AACR 适配器。覆盖 aacrjournals.org 域名。"""

    @property
    def name(self) -> str:
        return "aacr"

    def detect(self, url: str) -> bool:
        return "aacrjournals.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=15000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"AACR page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load AACR page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位全文 PDF 下载链接。

        AACR (Silverchair) 文章页的全文 PDF 链接:
        - <a class="al-link pdf openInAnotherWindow ..."> → /<journal>/article-pdf/...

        用 a[href*="/article-pdf/"] 精确匹配，避免误选:
          - supplementary material 链接 (silverchair-cdn.com/...-s01.pdf)
          - 引文导出链接 (/Citation/Download)
        """
        selectors = [
            'a[href*="/article-pdf/"]',
            'a.pdf',
        ]
        for selector in selectors:
            try:
                element = page.query_selector(selector)
                if element:
                    href = element.get_attribute("href") or ""
                    # 排除 supplementary（href 含 -s0 数字 的不是全文）
                    if "/article-pdf/" in href:
                        logger.info(f"Found download element: '{selector}' -> {href}")
                        return element
            except Exception as e:
                logger.debug(f"Selector '{selector}' failed: {e}")

        logger.error("Could not find any full-text download element on AACR page")
        return None

    def find_download_url(self, page) -> Optional[str]:
        """
        提取 PDF URL。优先 citation_pdf_url meta（最权威），其次元素 href。
        """
        # 1. citation_pdf_url meta 标签
        try:
            pdf_url = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_pdf_url"]');
                return el ? el.content : '';
            }""")
            if pdf_url and "/article-pdf/" in pdf_url:
                logger.info(f"PDF URL from citation_pdf_url: {pdf_url}")
                return pdf_url
        except Exception as e:
            logger.debug(f"citation_pdf_url extraction failed: {e}")

        # 2. 回退到元素 href
        return super().find_download_url(page)

    def check_access(self, page) -> bool:
        """AACR 权限检测：有全文 PDF 下载链接 = 有权限。

        不用基类的文本匹配（避免误判）。
        """
        pdf_link = page.query_selector('a[href*="/article-pdf/"]')
        if pdf_link:
            return True
        # citation_pdf_url 存在也视为有权限
        try:
            has_meta = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_pdf_url"]');
                return !!(el && el.content && el.content.includes('/article-pdf/'));
            }""")
            if has_meta:
                return True
        except Exception:
            pass
        logger.warning("No PDF download link found - likely no access")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 AACR 论文元数据。"""
        info = PaperInfo(publisher="aacr")
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
