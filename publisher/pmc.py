"""PubMed Central (PMC) 适配器。

URL 模式:
    https://pmc.ncbi.nlm.nih.gov/articles/PMCXXXX/        (新域名)
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMCXXXX/     (旧域名，会 301 跳转)

下载流程:
    PMC 使用 CloudFront CDN + reCAPTCHA 挑战保护 PDF 端点。
    简单 fetch() / requests 会返回 403 或挑战页面。

    成功策略:
    1. 先加载文章页建立浏览器会话 (get_paper_metadata / find_download_url)
    2. 获取 citation_pdf_url meta 标签中的 PDF URL
    3. 浏览器导航到 PDF URL，等待云挑战自动解决（约 5-10 秒）
    4. 挑战通过后，从 PDF 页面上下文执行 fetch() 获取实际 PDF 字节

覆盖: 所有 PMC 开放获取全文（含大量出版商论文的 green-OA 副本）。
"""

import logging
import time
from typing import Optional, Any
from urllib.parse import urljoin

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class PMCAdapter(PublisherAdapter):
    """PubMed Central (PMC) 适配器。

    PDF 直链模式: citation_pdf_url meta 标签 -> .../pdf/<filename>.pdf
    PMC 全文均为开放获取。
    """

    @property
    def name(self) -> str:
        return "pmc"

    def detect(self, url: str) -> bool:
        u = url.lower()
        # 新域名 pmc.ncbi.nlm.nih.gov / 旧域名 www.ncbi.nlm.nih.gov/pmc/
        return "pmc.ncbi.nlm.nih.gov" in u or "ncbi.nlm.nih.gov/pmc" in u

    def navigate_to_paper(self, page, url: str) -> bool:
        """导航到 PMC 文章页，并等待真实内容加载。"""
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except Exception as e:
            logger.error(f"Failed to load PMC page: {e}")
            return False

        # PMC 有时有 reCAPTCHA 挑战中间页。
        # 等待文章内容标志出现。
        ready = False
        for selector in [
            'meta[name="citation_pdf_url"]',
            'h1.content-title',
            'main',
        ]:
            try:
                page.wait_for_selector(selector, timeout=20000)
                ready = True
                break
            except Exception:
                continue

        if not ready:
            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                logger.warning("PMC page readiness uncertain (non-critical)")

        # 确认有 PDF URL
        try:
            has_pdf = page.query_selector('meta[name="citation_pdf_url"]')
            if not has_pdf:
                logger.warning("PMC page loaded but no citation_pdf_url meta tag")
        except Exception:
            pass

        logger.info(f"PMC page loaded: {page.url}")
        return True

    def find_download_element(self, page) -> Optional[Any]:
        return None  # 由 find_download_url 处理

    def find_download_url(self, page) -> str | None:
        """从 citation_pdf_url meta 标签提取 PDF URL。"""
        try:
            pdf_url = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_pdf_url"]');
                return el ? el.content : null;
            }""")
            if pdf_url:
                absolute = urljoin(page.url, pdf_url)
                logger.info(f"Found PDF via citation_pdf_url: {absolute[:90]}")
                return absolute
        except Exception:
            pass

        # 兜底: DOM 中查找指向 PDF 的链接
        try:
            elements = page.query_selector_all('a[href*="/pdf/"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if "/pdf/" in href:
                    absolute = urljoin(page.url, href)
                    logger.info(f"Found PDF link in DOM: {absolute[:90]}")
                    return absolute
        except Exception:
            pass

        logger.warning("Could not find any PDF download URL on PMC page")
        return None

    def check_access(self, page) -> bool:
        """PMC 全文均为开放获取。只要有 citation_pdf_url 即视为可访问。"""
        if page.query_selector('meta[name="citation_pdf_url"]'):
            return True
        if page.query_selector('a[href*="/pdf/"]'):
            return True
        logger.warning("No citation_pdf_url / PDF link found on PMC page")
        return False

    def get_paper_metadata(self, page) -> PaperInfo:
        info = PaperInfo(publisher="pmc")
        try:
            info.title = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_title"]');
                if (el) return el.content;
                const h1 = document.querySelector('h1.content-title, h1');
                return h1 ? h1.innerText.trim() : '';
            }""") or ""

            info.doi = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_doi"]');
                return el ? el.content : '';
            }""") or ""

            info.year = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_publication_date"]');
                if (el) return el.content;
                const el2 = document.querySelector('meta[name="citation_date"]');
                return el2 ? el2.content : '';
            }""") or ""

            info.authors = page.evaluate("""() => {
                const metas = document.querySelectorAll('meta[name="citation_author"]');
                return Array.from(metas).map(m => m.content).join(', ');
            }""") or ""

            info.url = page.url
        except Exception as e:
            logger.warning(f"Metadata extraction partial failure: {e}")
        return info

    def fallback_download(self, page, monitor, pdf_url: str) -> Optional[str]:
        """PMC 专属下载策略：浏览器导航到 PDF URL，等待云挑战解决，然后 fetch()。

        标准 fetch/requests 在 CloudFront 挑战面前会失败。
        此方法：让浏览器完成挑战后再从页面上下文 fetch。
        """
        logger.info("PMC fallback: navigating to PDF URL for challenge resolution...")

        try:
            # 导航到 PDF URL，让浏览器处理 CloudFront/reCAPTCHA 挑战
            page.goto(pdf_url, wait_until="load", timeout=60000)
            # 等待挑战彻底解决（CloudFront PoW 约 5-10 秒）
            logger.info("PMC fallback: waiting for CloudFront challenge to resolve...")
            time.sleep(10)
            logger.info(f"PMC fallback: PDF page loaded: {page.url[:80]}")
        except Exception as e:
            logger.error(f"PMC fallback: PDF navigation failed: {e}")
            return None

        # 从 PDF 页面上下文执行 fetch() - 此时挑战已解决
        try:
            import base64

            result = page.evaluate("""async (url) => {
                const response = await fetch(url);
                if (!response.ok) {
                    return { error: 'HTTP ' + response.status, status: response.status };
                }
                const buffer = await response.arrayBuffer();
                const bytes = new Uint8Array(buffer);
                const prefix = Array.from(bytes.slice(0, 4));

                let binary = '';
                const chunkSize = 8192;
                for (let i = 0; i < bytes.length; i += chunkSize) {
                    const chunk = bytes.subarray(i, Math.min(i + chunkSize, bytes.length));
                    binary += String.fromCharCode.apply(null, chunk);
                }
                const b64 = btoa(binary);

                return {
                    prefix: prefix,
                    totalLength: bytes.length,
                    base64: b64,
                    contentType: response.headers.get('content-type') || ''
                };
            }""", pdf_url)

            if "error" in result:
                logger.error(f"PMC fallback fetch() failed: {result['error']}")
                return None

            prefix = bytes(result["prefix"])
            if prefix != b"%PDF":
                logger.warning(f"PMC fallback fetch() response is not PDF (prefix={prefix})")
                return None

            body = base64.b64decode(result["base64"])
            content_type = result.get("contentType", "")
            total_kb = len(body) / 1024
            logger.info(f"PMC fallback: got {total_kb:.1f} KB PDF (Content-Type: {content_type})")

            if len(body) < 1000:
                logger.warning(f"PMC fallback: file suspiciously small ({len(body)} bytes)")

            # 使用 monitor 的推断文件名方法
            filename = monitor._infer_filename_from_url(pdf_url) if hasattr(monitor, '_infer_filename_from_url') else None
            if not filename:
                import re
                from urllib.parse import urlparse
                path = urlparse(pdf_url).path
                basename = os.path.basename(path)
                if basename and basename.endswith(".pdf"):
                    filename = basename
                else:
                    filename = "pmc_paper.pdf"

            import os
            filepath = os.path.join(monitor.temp_dir, filename)

            if os.path.exists(filepath):
                base_name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(filepath):
                    filepath = os.path.join(monitor.temp_dir, f"{base_name}_{counter}{ext}")
                    counter += 1

            with open(filepath, "wb") as f:
                f.write(body)

            logger.info(f"PMC fallback: saved to {filepath}")
            return filepath

        except Exception as e:
            logger.error(f"PMC fallback fetch failed: {e}")
            return None
