"""
下载模块。

两种下载策略：
1. cookie_download — 用浏览器 session cookies + requests 直接下载（推荐，避免弹窗拦截）
2. wait_for_download — 监控下载目录等待文件出现（旧方案，作为 fallback）
"""

import time
import os
import re
import glob
import logging
from typing import Optional
from urllib.parse import urlparse

import requests

logger = logging.getLogger(__name__)


class DownloadMonitor:
    """下载管理器。"""

    def __init__(self, config: dict):
        dl_cfg = config.get("download", {})
        self.temp_dir = os.path.expandvars(
            dl_cfg.get("temp_dir", r"C:\Users\IvanZhuyf\Downloads\temp")
        )
        self.timeout = dl_cfg.get("timeout", 120)

        # 确保下载目录存在
        os.makedirs(self.temp_dir, exist_ok=True)

    def cookie_download(
        self,
        ctx,
        pdf_url: str,
        referer: str | None = None,
        filename: str | None = None,
    ) -> Optional[str]:
        """
        用浏览器 session cookies 通过 requests 下载文件。

        优势：绕过 Chrome 弹窗拦截，不受 target="_blank" 影响，
        仍然使用真实 Chrome 的认证 cookie。

        Args:
            ctx: Playwright BrowserContext（用于提取 cookies）
            pdf_url: 要下载的 PDF URL
            referer: Referer 头（通常设为论文页面 URL）
            filename: 保存的文件名，None 则从 URL/响应头推断

        Returns:
            下载完成的文件路径，失败返回 None
        """
        logger.info(f"Cookie-downloading: {pdf_url}")

        # 1. 提取浏览器 cookies
        cookies = ctx.cookies()
        session = requests.Session()

        # 解析目标域名，只设置相关 cookie
        target_domain = urlparse(pdf_url).netloc

        for cookie in cookies:
            cookie_domain = cookie.get("domain", "").lstrip(".")
            # 设置所有 cookie（不过滤域名，让 requests 自动匹配）
            session.cookies.set(
                cookie["name"],
                cookie["value"],
                domain=cookie.get("domain", ""),
                path=cookie.get("path", "/"),
            )

        # 2. 设置请求头，模拟真实浏览器
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/147.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        if referer:
            headers["Referer"] = referer

        # 3. 发起请求（流式下载，支持大文件）
        try:
            response = session.get(
                pdf_url, headers=headers, stream=True, timeout=self.timeout
            )
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            logger.info(f"Response: {response.status_code}, Content-Type: {content_type}")

            # 检查是否真的是 PDF
            if "text/html" in content_type and "pdf" not in content_type.lower():
                logger.warning(f"Response is HTML, not PDF. Content-Type: {content_type}")
                # 可能被重定向到了登录页
                if len(response.content) < 5000:
                    logger.debug(f"Response body preview: {response.text[:500]}")
                return None

        except requests.RequestException as e:
            logger.error(f"Download request failed: {e}")
            return None

        # 4. 确定文件名
        if not filename:
            filename = self._infer_filename(response, pdf_url)

        filepath = os.path.join(self.temp_dir, filename)

        # 避免覆盖已有文件
        if os.path.exists(filepath):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(filepath):
                filepath = os.path.join(self.temp_dir, f"{base}_{counter}{ext}")
                counter += 1

        # 5. 写入文件
        total_size = 0
        try:
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    total_size += len(chunk)

            file_size_kb = total_size / 1024
            logger.info(f"Downloaded: {filepath} ({file_size_kb:.1f} KB)")

            # 基本校验：PDF 文件不应太小
            if total_size < 1000:
                logger.warning(f"File suspiciously small ({total_size} bytes), might not be a valid PDF")

            return filepath

        except IOError as e:
            logger.error(f"Failed to write file: {e}")
            return None

    def _infer_filename(self, response, url: str) -> str:
        """从响应头或 URL 推断文件名。"""
        # 尝试从 Content-Disposition 获取
        cd = response.headers.get("Content-Disposition", "")
        if cd:
            match = re.search(r'filename[*]?=["\']?([^"\';\s]+)["\']?', cd)
            if match:
                return match.group(1)

        # 从 URL 路径推断
        path = urlparse(url).path
        basename = os.path.basename(path)
        if basename and basename.endswith(".pdf"):
            return basename

        # 用 DOI 或路径生成文件名
        doi_part = path.rstrip("/").split("/")[-1]
        safe_name = re.sub(r'[<>:"/\\|?*]', '_', doi_part)
        return f"{safe_name}.pdf"

    def browser_download(
        self,
        page,
        pdf_url: str,
        referer: str | None = None,
        filename: str | None = None,
    ) -> Optional[str]:
        """
        用页面上下文的 fetch() API 下载 PDF。

        原理：在 Playwright page 上下文中执行 JavaScript fetch()，
        请求走 Chrome 原生网络栈（TLS + Cookie 全真实），
        PDF 查看器扩展不会拦截 fetch() 请求，返回原始字节。

        Args:
            page: Playwright Page 对象（需停留在论文页面）
            pdf_url: PDF 下载 URL
            referer: 未使用（fetch 自动带页面 Referer）
            filename: 保存的文件名

        Returns:
            下载完成的文件路径，失败返回 None
        """
        import base64

        logger.info(f"Browser-downloading via fetch(): {pdf_url}")

        try:
            result = page.evaluate("""async (url) => {
                const response = await fetch(url);
                if (!response.ok) {
                    return { error: 'HTTP ' + response.status, status: response.status };
                }
                const buffer = await response.arrayBuffer();
                const bytes = new Uint8Array(buffer);
                const prefix = Array.from(bytes.slice(0, 4));

                // base64 编码传输
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
                logger.error(f"fetch() returned error: {result['error']}")
                return None

            # 验证是 PDF
            prefix = bytes(result["prefix"])
            if prefix != b"%PDF":
                logger.warning(f"Response is not PDF (starts with {prefix})")
                return None

            # 解码并保存
            body = base64.b64decode(result["base64"])
            content_type = result.get("contentType", "")
            total_kb = len(body) / 1024
            logger.info(f"Got {total_kb:.1f} KB PDF (Content-Type: {content_type})")

            if len(body) < 1000:
                logger.warning(f"File suspiciously small ({len(body)} bytes)")

            # 确定文件名
            if not filename:
                filename = self._infer_filename_from_url(pdf_url)

            filepath = os.path.join(self.temp_dir, filename)

            if os.path.exists(filepath):
                base_name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(filepath):
                    filepath = os.path.join(self.temp_dir, f"{base_name}_{counter}{ext}")
                    counter += 1

            with open(filepath, "wb") as f:
                f.write(body)

            logger.info(f"Saved: {filepath}")
            return filepath

        except Exception as e:
            logger.error(f"browser_download failed: {e}")
            return None

    def _infer_filename_from_url(self, url: str) -> str:
        """从 URL 推断文件名。"""
        path = urlparse(url).path
        basename = os.path.basename(path)
        if basename and basename.endswith(".pdf"):
            return basename
        doi_part = path.rstrip("/").split("/")[-1]
        safe_name = re.sub(r'[<>:"/\\|?*]', '_', doi_part)
        return f"{safe_name}.pdf"

    def get_temp_dir(self) -> str:
        """返回下载临时目录路径。"""
        return self.temp_dir

    # --- Fallback: 旧方案，监控下载目录 ---

    def _get_files_before(self) -> set:
        """获取下载目录中已有文件的集合。"""
        return set(
            glob.glob(os.path.join(self.temp_dir, "*"))
            + glob.glob(os.path.join(self.temp_dir, "*.crdownload"))
        )

    def wait_for_download(
        self, page, timeout: Optional[int] = None
    ) -> Optional[str]:
        """
        等待新的下载文件出现并完成（旧方案 fallback）。

        Args:
            page: Playwright Page 对象
            timeout: 超时秒数

        Returns:
            下载完成的文件路径，超时返回 None
        """
        timeout = timeout or self.timeout
        files_before = self._get_files_before()

        try:
            cdp_session = page.context.new_cdp_session(page)
            cdp_session.send(
                "Browser.setDownloadBehavior",
                {
                    "behavior": "allowAndName",
                    "downloadPath": self.temp_dir,
                    "eventsEnabled": True,
                },
            )
        except Exception as e:
            logger.debug(f"CDP download behavior setup: {e}")

        logger.info(f"Waiting for download (timeout: {timeout}s)...")

        start_time = time.time()
        while time.time() - start_time < timeout:
            current_files = set(glob.glob(os.path.join(self.temp_dir, "*")))
            new_files = current_files - files_before
            if new_files:
                downloading = [f for f in new_files if f.endswith(".crdownload")]
                if not downloading:
                    completed = [f for f in new_files if os.path.isfile(f)]
                    if completed:
                        filepath = completed[-1]
                        logger.info(f"Download completed: {filepath}")
                        return filepath
                else:
                    logger.debug(f"Download in progress: {downloading[0]}")
            time.sleep(2)

        logger.warning(f"Download timed out after {timeout}s")
        return None
