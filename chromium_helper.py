"""
Chromium 连接管理模块。

通过 CDP (Chrome DevTools Protocol) 连接到用户已启动的 Chromium 浏览器。
关键：不启动新浏览器，不设置 navigator.webdriver 标记。
"""

import subprocess
import time
import os
import logging
from typing import Optional

from playwright.sync_api import sync_playwright, Browser, BrowserContext

logger = logging.getLogger(__name__)


class ChromiumHelper:
    """管理 Chromium 浏览器的启动和 CDP 连接。"""

    def __init__(self, config: dict):
        self.config = config
        self._browser_config = config.get("chrome", {})
        self.cdp_url = self._browser_config.get("cdp_url", "http://localhost:9222")
        self._browser_path = self._browser_config.get(
            "chrome_path",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        )
        self.user_data_dir = os.path.expandvars(
            self._browser_config.get(
                "user_data_dir", r"%LOCALAPPDATA%\Google\Chrome\User Data"
            )
        )
        self.warmup_url = self._browser_config.get("warmup_url", "")
        # 从浏览器路径提取进程名（如 chrome.exe、msedge.exe）
        self._browser_exe = os.path.basename(self._browser_path)
        self._playwright = None
        self._browser = None

    def _parse_cdp_port(self) -> str:
        """Extract port number from cdp_url."""
        import re
        m = re.search(r":(\d+)", self.cdp_url)
        return m.group(1) if m else "9222"

    def launch_browser(self) -> bool:
        """启动带调试端口的 Chromium 浏览器。

        使用 config 中的 user_data_dir（保留登录状态）和 cdp_url 中的端口。
        如果浏览器已在运行，先关闭再重启。
        """
        if not os.path.exists(self._browser_path):
            logger.error(f"Chromium not found at: {self._browser_path}")
            return False

        port = self._parse_cdp_port()

        # 确保旧 Chromium 进程完全退出
        if self.is_browser_running():
            logger.info("Killing existing Chromium processes before launch...")
            subprocess.run(
                ["taskkill", "/IM", self._browser_exe, "/F"],
                capture_output=True, timeout=10,
            )
            time.sleep(3)

        cmd = [
            self._browser_path,
            f"--remote-debugging-port={port}",
            "--remote-debugging-address=127.0.0.1",
            f"--user-data-dir={self.user_data_dir}",
        ]

        logger.info(f"Launching Chromium with CDP on port {port}...")
        try:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # 等待 Chromium 启动
            time.sleep(3)
            logger.info("Chromium launched successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to launch Chromium: {e}")
            return False

    def connect(self) -> Optional[tuple]:
        """
        通过 CDP 连接到已运行的 Chromium。

        Returns:
            (playwright_instance, browser) 或 None
        """
        logger.info(f"Connecting to Chromium via CDP at {self.cdp_url}...")
        try:
            pw = sync_playwright().start()
            self._playwright = pw  # 先保存，失败时能清理
            browser = pw.chromium.connect_over_cdp(self.cdp_url)
            self._browser = browser
            logger.info(
                f"Connected. Browser version: {browser.version}, "
                f"contexts: {len(browser.contexts)}"
            )
            return pw, browser
        except Exception as e:
            logger.error(f"Failed to connect to Chromium: {e}")
            logger.error(
                f"Make sure Chromium is running with --remote-debugging-port={self._parse_cdp_port()}"
            )
            # 清理失败的 playwright 实例，防止后续 connect 冲突
            if self._playwright:
                try:
                    self._playwright.stop()
                except Exception:
                    pass
                self._playwright = None
            return None

    def get_or_create_page(self, browser: Browser):
        """获取或创建页面。优先复用已有页面，但跳过坏状态页面。"""
        if browser.contexts:
            ctx = browser.contexts[0]
            if ctx.pages:
                # 从后往前找第一个状态正常的页面
                for page in reversed(ctx.pages):
                    url = page.url
                    if (url and url != "about:blank"
                        and "chrome-error" not in url
                        and "pdf.sciencedirectassets" not in url):
                        logger.info(f"Using existing page: {url}")
                        return page, ctx
                # 所有页面都不可用，新开标签
                logger.info("All existing pages in bad state, creating new tab")
                page = ctx.new_page()
                return page, ctx
            else:
                page = ctx.new_page()
                return page, ctx
        else:
            ctx = browser.new_context()
            page = ctx.new_page()
            return page, ctx

    def warmup(self, page) -> None:
        """打开一个暖场页面，模拟正常浏览行为。"""
        if not self.warmup_url:
            return

        logger.info(f"Warmup: navigating to {self.warmup_url}")
        try:
            page.goto(self.warmup_url, wait_until="domcontentloaded", timeout=15000)
            time.sleep(3)
            logger.info("Warmup page loaded.")
        except Exception as e:
            logger.warning(f"Warmup page failed (non-critical): {e}")

    def cleanup_tabs(self, browser: Browser) -> None:
        """
        清理所有 tab，只保留一个并导航到 about:blank。

        每次下载完成后调用，防止陈旧 tab 累积（PDF 查看器、
        重定向中间页等）导致后续下载卡住。

        使用 JS location.href 而非 page.goto()，避免某些情况下
        goto timeout 被忽略导致无限阻塞。
        """
        try:
            if not browser.contexts:
                return
            ctx = browser.contexts[0]
            pages = ctx.pages
            if len(pages) <= 1:
                if pages:
                    try:
                        pages[0].evaluate("() => { location.href = 'about:blank'; }")
                    except Exception:
                        pass
                return

            # 保留第一个 tab，关闭其余
            keep = pages[0]
            for p in pages[1:]:
                try:
                    p.close()
                except Exception:
                    pass
            try:
                keep.evaluate("() => { location.href = 'about:blank'; }")
            except Exception:
                pass
            logger.info(f"Cleaned up tabs: {len(pages)} -> 1")
        except Exception as e:
            logger.debug(f"cleanup_tabs error (non-critical): {e}")

    def disconnect(self) -> None:
        """断开连接（不关闭浏览器）。disconnect 失败时 taskkill 强制关闭 Chromium。

        如果 playwright.stop() 出错（卡死/线程问题），
        用 taskkill 强制结束 Chromium 进程释放资源。
        这是一种防御性措施——对 agent 场景来说 Chromium 没有需要长期保持的任务。

        注意：如需保留 Chromium 进程，注释掉 taskkill 部分即可。
        """
        if self._playwright:
            try:
                self._playwright.stop()
                logger.info("Disconnected from Chromium.")
            except Exception as e:
                logger.debug(f"playwright.stop() error: {e}")
                # disconnect 失败 → taskkill 强制关闭 Chromium
                try:
                    subprocess.run(
                        ["taskkill", "/IM", self._browser_exe, "/F"],
                        capture_output=True, timeout=5,
                    )
                    logger.info("Chromium force-killed via taskkill (disconnect failed).")
                except Exception as e2:
                    logger.debug(f"taskkill also failed: {e2}")
            finally:
                self._playwright = None
                self._browser = None

    def is_browser_running(self) -> bool:
        """检测配置的 Chromium 浏览器是否已在运行。"""
        result = subprocess.run(
            ["tasklist", "/FI", f"IMAGENAME eq {self._browser_exe}"],
            capture_output=True,
            text=True,
        )
        return self._browser_exe in result.stdout
