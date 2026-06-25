"""
JoVE (Journal of Visualized Experiments) 适配器。

URL 模式: https://www.jove.com/t/64882/<slug>
          https://www.jove.com/v/63484/<slug>    (video 文章页)
          https://www.jove.com/pdf/64882/<slug>
DOI 前缀: 10.3791/
下载流程: 跨域 CDN 型（构造 api.jove.com PDF 直链）

重要发现（CDP 探测，见 debug/debug_jove*.py）：
  - 文章页的 "Download PDF" 是个 <button>（chakra-button），点击后用 window.open
    打开 /pdf/<id>/<slug> 页面，那是个 PDF.js 查看器，DOM 里没有真正的 PDF <a> 链接。
  - /pdf/ 页面返回的是 HTML wrapper（~31KB），不是 PDF。
  - 真正的 PDF 由 PDF.js 查看器从跨域 API 拉取：
      https://api.jove.com/api/article/pdf/<id>   → application/pdf
  - 在 www.jove.com 页面上下文里 fetch() 该 API 会被 CORS 拦截（TypeError: Failed to fetch），
    因此本适配器只返回 URL，依赖 engine 的 cookie_download 兜底（requests + 浏览器 cookie，
    不受 CORS 限制）。机构登录态（SSO）cookie 在 .jove.com 域，覆盖 api.jove.com。

article id 提取顺序：
  1. 当前 page.url 里的数字 id（/t/<id>/ 或 /v/<id>/ 或 /pdf/<id>/）
  2. citation_doi meta（10.3791/<id>）去掉前缀
"""

import logging
import re
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)

# 数字 article id 提取（/t/64882/ 或 /v/63484/ 或 /pdf/64882/）
_ID_RE = re.compile(r"/(?:t|v|pdf)/(\d+)(?:/|$)")
_DOI_PREFIX = "10.3791/"


class JoVEAdapter(PublisherAdapter):
    """JoVE 适配器。覆盖 jove.com 域名（DOI 前缀 10.3791）。"""

    @property
    def name(self) -> str:
        return "jove"

    def detect(self, url: str) -> bool:
        return "jove.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=15000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"JoVE page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load JoVE page: {e}")
            return False

    def _extract_article_id(self, page) -> Optional[str]:
        """从 page.url 或 citation_doi meta 提取数字 article id。"""
        try:
            current = page.url or ""
        except Exception:
            current = ""
        m = _ID_RE.search(current)
        if m:
            return m.group(1)

        # Fallback: citation_doi meta tag (10.3791/<id>)
        try:
            doi = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_doi"]');
                return el ? el.content : '';
            }""") or ""
        except Exception:
            doi = ""
        if doi.lower().startswith(_DOI_PREFIX):
            return doi[len(_DOI_PREFIX):].strip()

        return None

    def find_download_element(self, page) -> Optional[Any]:
        """JoVE 没有 DOM PDF 链接，返回 None（由 find_download_url 构造 URL）。"""
        return None

    def find_download_url(self, page) -> Optional[str]:
        """构造跨域 API PDF 直链。

        返回 https://api.jove.com/api/article/pdf/<id>。
        engine 的 browser_download (fetch) 会因 CORS 失败，
        随后 cookie_download (requests + cookie) 成功拿到 PDF。
        """
        article_id = self._extract_article_id(page)
        if not article_id:
            logger.error("Could not extract JoVE article id from page")
            return None
        pdf_url = f"https://api.jove.com/api/article/pdf/{article_id}"
        logger.info(f"JoVE PDF API URL: {pdf_url}")
        return pdf_url

    def check_access(self, page) -> bool:
        """JoVE 文章页对所有人可见；PDF 下载需要机构订阅。

        若 cookie_download 拿到 HTML（登录/付费墙）而非 PDF，engine 会自然失败。
        这里默认返回 True，让下载流程继续，由 PDF 校验把关。
        """
        return True

    def get_paper_metadata(self, page) -> PaperInfo:
        info = PaperInfo(publisher="jove")
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
            logger.warning(f"JoVE metadata extraction partial failure: {e}")
        return info
