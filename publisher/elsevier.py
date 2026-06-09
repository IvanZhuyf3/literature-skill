"""
Elsevier (ScienceDirect) 适配器。

URL 模式: https://www.sciencedirect.com/science/article/pii/...
下载流程: 论文页 -> 点击 View PDF -> 新 tab 打开 Chrome PDF 查看器
         -> pyautogui 点击查看器下载按钮 -> 监控下载目录

Elsevier 的 /pdfft URL 被 Chrome 内置 PDF 查看器劫持，所有 Playwright
事件（response、request）都被抑制。无法通过 fetch() 或网络拦截获取 S3 URL。
改用物理点击方式：在新 tab 的 PDF 查看器中点击下载按钮。
"""

import logging
import os
import re
import time
from typing import Optional, Any

import pyautogui

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class ElsevierAdapter(PublisherAdapter):
    """Elsevier ScienceDirect 适配器。

    View PDF 打开新 tab（Chrome PDF 查看器），用 pyautogui 点击
    查看器工具栏的下载按钮，监控下载目录等待文件落盘。
    """

    # 标记：不走 fetch() 流程，用点击下载
    use_click_download = True
    fetch_from_pdf_page = False

    @property
    def name(self) -> str:
        return "elsevier"

    def detect(self, url: str) -> bool:
        return "sciencedirect.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            # 等 View PDF 链接出现（Elsevier 页面需要时间渲染）
            try:
                page.wait_for_selector('a[aria-label*="PDF"]', timeout=15000)
            except Exception:
                logger.warning("View PDF link not found after 15s, continuing...")
            try:
                page.wait_for_load_state("networkidle", timeout=30000)
            except Exception:
                logger.warning("networkidle timeout (non-critical), continuing...")
            logger.info(f"Elsevier page loaded: {page.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to load Elsevier page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        """
        定位 PDF 链接。

        Elsevier 的 "View PDF" 按钮链接到 /pdfft?md5=...&pid=...
        需要匹配当前文章的 PII，排除推荐文献中的链接。
        """
        pii_match = re.search(r'/pii/([^/?#]+)', page.url)
        current_pii = pii_match.group(1) if pii_match else ""

        # 查找所有 View PDF 链接，取匹配当前 PII 的
        try:
            elements = page.query_selector_all('a[aria-label*="PDF"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href and "/pdfft" in href:
                    logger.info(f"Found download element: href={href[:80]}...")
                    return el
        except Exception as e:
            logger.debug(f"aria-label search failed: {e}")

        # Fallback: text matching
        try:
            elements = page.query_selector_all('a:has-text("View PDF")')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href:
                    logger.info(f"Found download via text match: {href[:80]}...")
                    return el
        except Exception as e:
            logger.debug(f"Text match failed: {e}")

        logger.error("Could not find any download element on Elsevier page")
        return None

    def check_access(self, page) -> bool:
        """用 PDF 链接存在性判断权限。"""
        try:
            pii_match = re.search(r'/pii/([^/?#]+)', page.url)
            current_pii = pii_match.group(1) if pii_match else ""
            elements = page.query_selector_all('a[aria-label*="PDF"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href and "/pdfft" in href:
                    return True
        except Exception:
            pass
        logger.warning("No PDF link found - likely no access")
        return False

    def resolve_pdf_url(self, page, initial_pdf_url: str) -> Optional[str]:
        """
        点击 View PDF 打开新 tab，在新 tab 上用 pyautogui 点下载按钮。

        Chrome PDF 查看器会接管 /pdfft 的导航。window.open 打开的 tab 
        Playwright CDP 看不到（不触发 ctx.on("page")，不在 ctx.pages 里）。
        
        策略：用 Playwright click 点击 View PDF 链接，用
        page.expect_popup() 捕获新 tab。如果 popup 没触发，
        就直接在当前 page 导航到 /pdfft（Chrome PDF 查看器接管），
        然后用 pyautogui 点下载。

        返回特殊标记 "__click_download__" 通知 main.py 不走 fetch() 流程。
        """
        logger.info("Opening View PDF in new tab...")
        ctx = page.context
        logger.debug(f"  Pages before ({len(ctx.pages)}): {[p.url[:60] for p in ctx.pages]}")

        # 找到 View PDF 链接元素
        pii_match = re.search(r'/pii/([^/?#]+)', page.url)
        current_pii = pii_match.group(1) if pii_match else ""

        pdf_link = None
        try:
            elements = page.query_selector_all('a[aria-label*="PDF"]')
            for el in elements:
                href = el.get_attribute("href") or ""
                if current_pii and current_pii in href and "/pdfft" in href:
                    pdf_link = el
                    break
        except Exception:
            pass

        if not pdf_link:
            try:
                elements = page.query_selector_all('a:has-text("View PDF")')
                for el in elements:
                    href = el.get_attribute("href") or ""
                    if current_pii and current_pii in href:
                        pdf_link = el
                        break
            except Exception:
                pass

        new_page = None

        # 方法1: Playwright click + expect_popup
        if pdf_link:
            try:
                with page.expect_popup(timeout=30000) as popup_info:
                    pdf_link.click()
                new_page = popup_info.value
                logger.info(f"  Got popup: {new_page.url[:80]}...")
            except Exception as e:
                logger.debug(f"  expect_popup failed: {e}")

        # 方法2: 如果 popup 没成功，用中间页导航
        if not new_page:
            logger.info("  Popup not captured, trying navigation approach...")
            # 不用 window.open，直接 page.goto 到 /pdfft
            # Chrome PDF 查看器会接管这个页面
            try:
                page.goto(initial_pdf_url, timeout=60000)
            except Exception as e:
                logger.debug(f"  Navigation to /pdfft: {e}")
            # 此时 page 已经在 PDF 查看器中
            new_page = page
            # 标记：不要关闭这个 page（它就是原来的 page）
            self._reuse_original_page = True

        # 等待 PDF 加载
        time.sleep(5)

        # 把 tab 带到前台
        try:
            new_page.bring_to_front()
        except Exception as e:
            logger.debug(f"  bring_to_front: {e}")
        time.sleep(1)

        # 在文章页获取窗口信息（PDF 查看器页面 evaluate 可能失败）
        window_info = None
        try:
            window_info = page.evaluate("""() => ({
                screenX: window.screenX,
                screenY: window.screenY,
                outerWidth: window.outerWidth,
                outerHeight: window.outerHeight,
            })""")
            logger.debug(f"  Window: ({window_info['screenX']},{window_info['screenY']}) "
                        f"{window_info['outerWidth']}x{window_info['outerHeight']}")
        except Exception as e:
            logger.warning(f"  Could not get window info: {e}")

        # 记录 Ctrl+P 之前的时间，供 click_download 按创建时间查找文件
        self._print_start_time = time.time()

        # 用 pyautogui 点击 Chrome PDF 查看器的下载按钮
        self._click_pdf_download_button(new_page, window_info)

        # 保存引用
        self._pdf_tab = new_page if not getattr(self, '_reuse_original_page', False) else None
        self._article_page = page

        return "__click_download__"

    def _click_pdf_download_button(self, pdf_page, window_info: dict | None = None) -> None:
        """
        在 Chrome PDF 查看器中用 Ctrl+P 打印为 PDF。
        
        关键：pyautogui 是 OS 级别的，快捷键发给当前 focus 的窗口。
        必须先确保 Chrome 窗口在前台，再发送 Ctrl+P。
        """
        # 通过 CDP 设置下载路径到 temp_dir
        try:
            temp_dir = os.path.expandvars(r"C:\Users\IvanZhuyf\Downloads\temp")
            cdp = pdf_page.context.new_cdp_session(pdf_page)
            cdp.send("Browser.setDownloadBehavior", {
                "behavior": "allowAndName",
                "downloadPath": temp_dir,
                "eventsEnabled": True,
            })
            logger.info(f"  CDP download path set to: {temp_dir}")
        except Exception as e:
            logger.debug(f"  CDP set download behavior: {e}")

        # 确保 Chrome 窗口在前台
        if window_info:
            # 点击窗口标题栏中间位置（激活窗口）
            title_x = window_info["screenX"] + window_info["outerWidth"] // 2
            title_y = window_info["screenY"] + 5
            pyautogui.click(title_x, title_y)
            logger.info(f"  Clicked Chrome title bar at ({title_x}, {title_y}) to focus")
            time.sleep(1)
            # 再点击内容区域确认激活
            content_x = window_info["screenX"] + window_info["outerWidth"] // 2
            content_y = window_info["screenY"] + window_info["outerHeight"] // 2
            pyautogui.click(content_x, content_y)
            time.sleep(0.5)
        else:
            logger.warning("  No window info, trying bring_to_front as fallback")
            try:
                pdf_page.bring_to_front()
            except Exception:
                pass
            time.sleep(1)

        # 现在发送 Ctrl+P 打开打印对话框
        pyautogui.hotkey('ctrl', 'p')
        logger.info("  Sent Ctrl+P (print)")

        # 第一次确认：打印对话框（等 3s 让它加载）
        time.sleep(3)
        pyautogui.press('enter')
        logger.info("  Pressed Enter (confirm print dialog)")

        # 第二次确认：另存为对话框（等 10s 让它加载）
        time.sleep(10)
        pyautogui.press('enter')
        logger.info("  Pressed Enter (confirm save dialog)")
        time.sleep(2)

    def click_download(self, monitor) -> Optional[str]:
        """
        Ctrl+P 打印已发起，等文件落盘后找到它。
        
        策略：记录 Ctrl+P 之前的时间戳，在 temp 目录找比该时间戳更新的 PDF。
        不依赖文件名匹配（文件名可能被截断或叫 main.pdf）。
        """
        import glob as glob_mod
        temp_dir = monitor.get_temp_dir()
        logger.info("Waiting for PDF print to complete...")

        # 记录 Ctrl+P 发起时的时间（已在 resolve_pdf_url 中执行）
        # 用 _print_start_time，如果没设就用当前时间
        start_time = getattr(self, '_print_start_time', time.time())

        # 轮询等待新 PDF 出现（最多 120 秒）
        filepath = None
        for i in range(60):
            time.sleep(2)
            # 找比 start_time 新的 PDF 文件
            candidates = []
            for f in glob_mod.glob(os.path.join(temp_dir, "*.pdf")):
                try:
                    mtime = os.path.getmtime(f)
                    if mtime >= start_time - 1:  # 1 秒容差
                        size = os.path.getsize(f)
                        if size > 10000:  # 至少 10KB，排除垃圾文件
                            candidates.append((f, mtime, size))
                except OSError:
                    continue
            if candidates:
                # 取最新的（按修改时间排序）
                candidates.sort(key=lambda x: x[1], reverse=True)
                f, mtime, size = candidates[0]
                # 等文件大小稳定（Foxit Reader 写完后大小不变）
                time.sleep(3)
                new_size = os.path.getsize(f)
                if new_size == size and size > 100000:  # 大小不变且 >100KB
                    size_mb = size / 1024 / 1024
                    logger.info(f"Found new PDF: {os.path.basename(f)} ({size_mb:.1f} MB)")
                    filepath = f
                    break
                # 否则继续等（文件还在写）

        # 清理：关闭 PDF 查看 tab
        if hasattr(self, '_pdf_tab') and self._pdf_tab:
            try:
                self._pdf_tab.close()
            except Exception:
                pass
            self._pdf_tab = None
        self._reuse_original_page = False

        if filepath is None:
            logger.error("PDF print not detected after 120s")
        return filepath

    def get_paper_metadata(self, page) -> PaperInfo:
        """提取 Elsevier 论文元数据。"""
        info = PaperInfo(publisher="elsevier")

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
