"""theses.fr (French national thesis repository) 适配器。

URL 模式: theses.fr
下载流程: 简单型 — PDF 在 /document 子路径直接下载
覆盖: 所有法国博士论文（开放获取）

Theses.fr 是法国国家博士学位论文库（ABES），所有论文开放获取。
PDF 直接在 https://theses.fr/<thesis_id>/document 下载，无需登录。
Content-Disposition: attachment; 返回 application/pdf。

关键发现（curl HEAD 测试）:
  curl -sIL https://theses.fr/2018AIXM0580/document
  → HTTP 200, Content-Type: application/pdf, ~7MB, Content-Disposition: attachment

注意: theses.fr 是 Vue/Vuetify SPA，静态 HTML 不含下载链接。
必须从 URL 构造 /document 路径，不能从 DOM 抓取。
"""

import logging
from typing import Optional, Any
from urllib.parse import urlparse

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class ThesesFrAdapter(PublisherAdapter):
    """theses.fr French thesis repository adapter.

    PDF direct link: https://theses.fr/<thesis_id>/document
    Open access — no institutional login required.
    """

    @property
    def name(self) -> str:
        return "theses_fr"

    def detect(self, url: str) -> bool:
        return "theses.fr" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            # theses.fr is a Vue/Vuetify SPA — give it time to render
            try:
                page.wait_for_load_state("networkidle", timeout=30000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"theses.fr page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load theses.fr page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        return None  # handled via find_download_url

    def find_download_url(self, page) -> Optional[str]:
        """Construct PDF URL from thesis page URL.

        theses.fr PDFs are at https://theses.fr/<thesis_id>/document
        The thesis ID is the first path segment (e.g. 2018AIXM0580).
        """
        current_url = page.url
        parsed = urlparse(current_url)
        segments = [s for s in parsed.path.split("/") if s]
        if not segments:
            logger.warning("No thesis ID in URL: %s", current_url)
            return None
        thesis_id = segments[0]
        pdf_url = f"https://theses.fr/{thesis_id}/document"
        logger.info(f"Constructed PDF URL: {pdf_url}")
        return pdf_url

    def check_access(self, page) -> bool:
        """theses.fr is open access — always True."""
        return True

    def get_paper_metadata(self, page) -> PaperInfo:
        info = PaperInfo(publisher="theses_fr")
        try:
            # theses.fr SPA: title in <title> or og:title meta
            info.title = page.evaluate("""() => {
                const og = document.querySelector('meta[property="og:title"]');
                if (og) return og.content;
                const t = document.title || '';
                return t.replace(/\\s*\\|\\s*Theses\\.fr\\s*$/i, '').trim();
            }""") or ""
            info.url = page.url
        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")
        return info
