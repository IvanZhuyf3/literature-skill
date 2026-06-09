"""
IEEE Xplore 适配器。

URL 模式: https://ieeexplore.ieee.org/document/XXXXXX
下载流程: 论文页 -> 提取 arnumber -> getPDF.jsp fetch() 下载

IEEE 的 PDF 按钮指向 stamp.jsp（HTML 包装页，内含 iframe），
实际 PDF 在 getPDF.jsp。直接 fetch getPDF.jsp 即可拿到 PDF。
无 citation_* meta 标签，metadata 从 DOM 提取。
"""

import re
import logging
from typing import Optional, Any
from urllib.parse import urljoin

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class IEEEAdapter(PublisherAdapter):
    """IEEE Xplore 适配器。覆盖 ieeexplore.ieee.org 域名。"""

    @property
    def name(self) -> str:
        return "ieee"

    def detect(self, url: str) -> bool:
        return "ieeexplore.ieee.org" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"IEEE page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load IEEE page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 下载链接。

        IEEE 有多个 PDF 链接（按钮和文字链接），都指向 stamp.jsp。
        我们用 a.xpl-btn-pdf 或 a[href*="stamp.jsp"] 定位。
        实际下载时改用 getPDF.jsp 而非 stamp.jsp。
        """
        selectors = [
            'a.xpl-btn-pdf',
            'a[href*="stamp.jsp"]',
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

        logger.error("Could not find any download element on IEEE page")
        return None

    def find_download_url(self, page) -> Optional[str]:
        """
        覆盖基类方法：不从 element href 取，而是构造 getPDF.jsp 直链。

        基类 find_download_url() 会从 element href 拿到 stamp.jsp（HTML 包装页），
        但我们实际需要 getPDF.jsp（直接返回 PDF 字节）。
        """
        # 先调 find_download_element 确认页面有 PDF 按钮
        element = self.find_download_element(page)
        if element is None:
            return None
        return self.get_pdf_url(page, element)

    def get_pdf_url(self, page, element) -> Optional[str]:
        """
        从页面 URL 提取 arnumber，构造 getPDF.jsp 直链。

        stamp.jsp 是 HTML 包装页（含 iframe + 反爬 JS），不能直接 fetch。
        getPDF.jsp 直接返回 PDF 字节。
        """
        current_url = page.url
        # 从 URL 提取 arnumber: /document/594865
        match = re.search(r'/document/(\d+)', current_url)
        if match:
            arnumber = match.group(1)
            pdf_url = f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={arnumber}"
            logger.info(f"Constructed IEEE PDF URL: {pdf_url}")
            return pdf_url

        # Fallback: 从 stamp.jsp href 中提取 arnumber
        href = element.get_attribute("href") or ""
        match = re.search(r'arnumber=(\d+)', href)
        if match:
            arnumber = match.group(1)
            pdf_url = f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={arnumber}"
            logger.info(f"Constructed IEEE PDF URL from href: {pdf_url}")
            return pdf_url

        logger.error("Could not extract arnumber from page URL or element href")
        return None

    def check_access(self, page) -> bool:
        """有 PDF 按钮表示有权限（IEEE 可能需要订阅，但检测链接存在即可）。"""
        pdf_link = page.query_selector('a.xpl-btn-pdf')
        if pdf_link:
            return True
        logger.warning("No PDF download link found - may need subscription")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        """
        提取 IEEE 论文元数据。
        
        IEEE 没有 citation_* meta 标签。
        - 标题: document.title（格式 "Title | IEEE ... | IEEE Xplore"）
        - DOI: a[href*="doi.org"] 链接
        - 日期: 页面 DOM 中查找
        """
        info = PaperInfo(publisher="ieee")

        try:
            # Title from document.title, strip " | IEEE ..." suffix
            info.title = page.evaluate("""() => {
                const title = document.title || '';
                // Remove trailing " | IEEE ... | IEEE Xplore" 
                return title.split(' | ')[0].trim();
            }""") or ""

            # DOI from doi.org link
            info.doi = page.evaluate("""() => {
                const link = document.querySelector('a[href*="doi.org"]');
                if (link) {
                    const href = link.href || '';
                    // Extract DOI from URL like https://doi.org/10.1109/3.594865
                    return href.replace('https://doi.org/', '').replace('http://doi.org/', '');
                }
                return '';
            }""") or ""

            # Date from page — try publication date element
            info.year = page.evaluate("""() => {
                // Try meta tags first (some IEEE pages have them)
                const dateMeta = document.querySelector('meta[name="citation_date"]') ||
                                 document.querySelector('meta[name="dc.date"]');
                if (dateMeta) return dateMeta.content || '';
                
                // Try to find date in the document-info section
                const dateEl = document.querySelector('.doc-subtitle');
                if (dateEl) {
                    const text = dateEl.textContent || '';
                    const yearMatch = text.match(/\\b(19|20)\\d{2}\\b/);
                    if (yearMatch) return yearMatch[0];
                }
                
                // Try any element with publication date text
                const allText = document.querySelector('.stats-document-header-published') ||
                                document.querySelector('[class*="publication-date"]');
                if (allText) {
                    const yearMatch = allText.textContent.match(/\\b(19|20)\\d{2}\\b/);
                    if (yearMatch) return yearMatch[0];
                }
                return '';
            }""") or ""

            # Authors
            info.authors = page.evaluate("""() => {
                const authorEls = document.querySelectorAll('meta[name="citation_author"]');
                if (authorEls.length > 0) {
                    return Array.from(authorEls).map(m => m.content).join(', ');
                }
                // Fallback: try author links on page
                const authors = document.querySelectorAll('a[id*="author-name"]');
                if (authors.length > 0) {
                    return Array.from(authors).map(a => a.textContent.trim()).join(', ');
                }
                return '';
            }""") or ""

            info.url = page.url

        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")

        return info
