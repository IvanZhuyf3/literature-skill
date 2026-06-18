"""
Acta Physica Sinica (《物理学报》) 适配器。

域名: wulixb.iphy.ac.cn
DOI 前缀: 10.7498
URL 模式: https://wulixb.iphy.ac.cn/article/doi/<DOI>

该站是开放获取（OA）中文期刊。论文页是 Angular 单页应用（SPA），
DOM 中的下载链接以 {{...}} 模板形式存在，无法直接 query_selector。
但 PDF 直链遵循确定性的 URL 模式：

    https://wulixb.iphy.ac.cn/cn/article/pdf/preview/<DOI>.pdf

因此本适配器不依赖 DOM，而是从论文页 URL 中提取 DOI，直接构造 PDF 直链。
下载本身无需登录/Cookie（OA）。
"""

import logging
import re
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)

_DOMAIN = "wulixb.iphy.ac.cn"


class WulixbAdapter(PublisherAdapter):
    """Acta Physica Sinica (物理学报) 适配器，覆盖 wulixb.iphy.ac.cn。"""

    @property
    def name(self) -> str:
        return "wulixb"

    def detect(self, url: str) -> bool:
        return _DOMAIN in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            # SPA bootstrap — give Angular time to render, but don't hard-fail
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("networkidle timeout (non-critical); SPA may still be bootstrapping")
            # Find download URL does NOT depend on DOM, so partial render is OK
            logger.info("wulixb page loaded (SPA): %s", page.url)
            return True
        except Exception as e:
            logger.error("Failed to load wulixb page: %s", e)
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """SPA 模板未渲染出可点击元素，返回 None；由 find_download_url 直接构造。"""
        return None

    def find_download_url(self, page) -> Optional[str]:
        """
        从论文页 URL 中提取 DOI，构造确定性 PDF 直链。

        论文页: https://wulixb.iphy.ac.cn/article/doi/<DOI>
        PDF:    https://wulixb.iphy.ac.cn/cn/article/pdf/preview/<DOI>.pdf
        """
        url = page.url or ""
        # 去掉 query / fragment
        bare = url.split("#", 1)[0].split("?", 1)[0]
        m = re.search(r"/article/doi/(.+)$", bare)
        if not m:
            logger.error("Could not extract DOI from wulixb URL: %s", url)
            return None
        doi = m.group(1).strip("/")
        pdf_url = f"https://{_DOMAIN}/cn/article/pdf/preview/{doi}.pdf"
        logger.info("Constructed wulixb PDF URL: %s", pdf_url)
        return pdf_url

    def check_access(self, page) -> bool:
        """物理学报是 OA 期刊，始终可访问。"""
        return True

    def get_paper_metadata(self, page) -> PaperInfo:
        info = PaperInfo(publisher="wulixb")
        try:
            info.url = page.url or ""
            # SPA 可能未渲染 meta；尽力提取
            info.title = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_title"]');
                return el ? el.content : '';
            }""") or ""
            info.doi = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_doi"]');
                return el ? el.content : '';
            }""") or ""
            if not info.doi:
                m = re.search(r"/article/doi/(.+)$", info.url.split("#", 1)[0].split("?", 1)[0])
                if m:
                    info.doi = m.group(1).strip("/")
        except Exception as e:
            logger.warning("wulixb metadata extraction partial failure: %s", e)
        return info
