"""
Paper-at-Home: 学术论文自动下载工具

入口文件。CLI 接口 + 完整工作流。
"""

import argparse
import logging
import os
import sys
import time
import yaml
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table

from chromium_helper import ChromiumHelper
from click_engine import HumanLikeClicker, viewport_to_screen
from download_monitor import DownloadMonitor
from rate_limiter import RateLimiter
from url_parser import parse_input, is_doi
from publisher.aaas import AAASAdapter
from publisher.acs import ACSAdapter
from publisher.aip import AIPAdapter
from publisher.elsevier import ElsevierAdapter
from publisher.npg import NPGAdapter
from publisher.optica import OpticaAdapter
from publisher.springer import SpringerAdapter
from publisher.pnas import PNASAdapter
from publisher.wiley import WileyAdapter
from publisher.aps import APSAdapter
from publisher.tandf import TandFAdapter
from publisher.rsc import RSCAdapter
from publisher.iop import IOPAdapter
from publisher.annualreviews import AnnualReviewsAdapter
from publisher.mdpi import MDPIAdapter
from publisher.frontiers import FrontiersAdapter
from publisher.elife import eLifeAdapter
from publisher.royalsociety import RoyalSocietyAdapter
from publisher.bmj import BMJAdapter
from publisher.ieee import IEEEAdapter
from publisher.spie import SPIEAdapter

console = Console()


def setup_logging(debug: bool = False):
    """配置日志。"""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, show_path=False, rich_tracebacks=True)],
    )


def load_config(path: str | None = None) -> dict:
    """加载 YAML 配置文件。"""
    default_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    config_path = path or default_path
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


# ---------------------------------------------------------------------------
# 截图调试（暂时禁用 — AI 不能看图片，等能看了再启用）
# ---------------------------------------------------------------------------

# def # debug_screenshot(page, config: dict, label: str = "") -> str | None:
#     """保存调试截图。"""
#     debug_cfg = config.get("debug", {})
#     if not debug_cfg.get("enabled", True):
#         return None
#     screenshot_dir = debug_cfg.get("screenshot_dir", "./debug_screenshots")
#     os.makedirs(screenshot_dir, exist_ok=True)
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     filename = f"{timestamp}_{label}.png" if label else f"{timestamp}.png"
#     filepath = os.path.join(screenshot_dir, filename)
#     try:
#         page.screenshot(path=filepath, full_page=False)
#         console.print(f"[dim]Screenshot saved: {filepath}[/dim]")
#         return filepath
#     except Exception as e:
#         console.print(f"[red]Screenshot failed: {e}[/red]")
#         return None

# ---------------------------------------------------------------------------
# Publisher 注册
# ---------------------------------------------------------------------------

def get_adapter(publisher: str, config: dict):
    """根据出版商名称获取适配器。"""
    adapters = {
        "aaas": AAASAdapter,
        "acs": ACSAdapter,
        "aip": AIPAdapter,
        "elsevier": ElsevierAdapter,
        "npg": NPGAdapter,
        "optica": OpticaAdapter,
        "springer": SpringerAdapter,
        "pnas": PNASAdapter,
        "wiley": WileyAdapter,
        "aps": APSAdapter,
        "tandf": TandFAdapter,
        "rsc": RSCAdapter,
        "iop": IOPAdapter,
        "annualreviews": AnnualReviewsAdapter,
        "mdpi": MDPIAdapter,
        "frontiers": FrontiersAdapter,
        "elife": eLifeAdapter,
        "royalsociety": RoyalSocietyAdapter,
        "bmj": BMJAdapter,
        "ieee": IEEEAdapter,
        "spie": SPIEAdapter,
    }
    adapter_cls = adapters.get(publisher)
    if adapter_cls is None:
        console.print(f"[red]No adapter for publisher: {publisher}[/red]")
        return None
    return adapter_cls(config)


# ---------------------------------------------------------------------------
# 核心下载流程
# ---------------------------------------------------------------------------

def download_paper(
    url: str,
    publisher: str,
    config: dict,
    browser,
    clicker: HumanLikeClicker,
    monitor: DownloadMonitor,
    rate_limiter: RateLimiter,
) -> dict:
    """
    下载单篇论文的完整流程。

    Returns:
        结果字典 {"success": bool, "filepath": str|None, "error": str|None, ...}
    """
    log = logging.getLogger("download")
    result = {"success": False, "url": url, "filepath": None, "error": None}

    # 1. 获取适配器
    adapter = get_adapter(publisher, config)
    if adapter is None:
        result["error"] = f"No adapter for publisher: {publisher}"
        return result

    # 2. 获取页面
    page, ctx = ChromiumHelper(config).get_or_create_page(browser)

    # 3. 导航到论文页面
    log.info(f"Navigating to: {url}")
    try:
        if not adapter.navigate_to_paper(page, url):
            # 导航失败，可能是页面状态坏了，新开标签页重试
            log.warning("Navigation failed on existing tab, trying new tab...")
            ctx = browser.contexts[0] if browser.contexts else browser.new_context()
            page = ctx.new_page()
            if not adapter.navigate_to_paper(page, url):
                result["error"] = "Failed to load page (even with new tab)"
                # # debug_screenshot(page, config, "navigate_failed")
                return result
    except Exception as e:
        result["error"] = f"Navigation error: {e}"
        # debug_screenshot(page, config, "navigate_error")
        return result

    # 4. 检查访问权限
    if not adapter.check_access(page):
        result["error"] = "Access denied / no subscription"
        log.warning(f"Access denied for: {url}")
        # debug_screenshot(page, config, "access_denied")
        return result

    # 5. 提取元数据
    paper_info = adapter.get_paper_metadata(page)
    result["paper_info"] = paper_info
    log.info(f"Paper: {paper_info.title[:80]}..." if paper_info.title else "Paper: (title not found)")

    # 5.5 去重检查：如果下载目录已有同名文件，跳过下载
    if paper_info.title:
        expected_name = sanitize_filename(paper_info.title) + ".pdf"
        temp_dir = config.get("download", {}).get("temp_dir", ".")
        expected_path = os.path.join(temp_dir, expected_name)
        if os.path.exists(expected_path):
            log.info(f"Already downloaded: {expected_name}")
            result["success"] = True
            result["filepath"] = expected_path
            result["skipped"] = True
            return result

    # 6. 模拟阅读行为
    rate_limiter.simulate_reading(page)

    # 7. 从 DOM 提取 PDF 下载 URL
    log.info("Locating download URL...")
    pdf_url = adapter.find_download_url(page)
    if pdf_url is None:
        result["error"] = "Download URL not found in page DOM"
        # debug_screenshot(page, config, "no_download_url")
        return result

    log.info(f"PDF URL: {pdf_url}")

    # 8. 某些出版商需要解析重定向链（如 Optica 的 JS 挑战）
    if hasattr(adapter, "resolve_pdf_url"):
        log.info("Publisher requires redirect resolution...")
        article_url = page.url  # 保存文章页 URL 用于回退
        resolved_url = adapter.resolve_pdf_url(page, pdf_url)
        if resolved_url is None:
            result["error"] = "Failed to resolve PDF URL through redirects"
            # debug_screenshot(page, config, "resolve_failed")
            return result
        pdf_url = resolved_url
        log.info(f"Resolved PDF URL: {pdf_url}")

        # Elsevier: 返回特殊标记，不走 fetch()，改用点击下载
        if pdf_url == "__click_download__":
            log.info("Using click-download flow (PDF viewer)...")
            # Ctrl+P 已在 resolve_pdf_url 中执行，直接等文件落盘
            filepath = adapter.click_download(monitor)
            if filepath is None:
                result["error"] = "Click download failed (timeout or no file)"
                # debug_screenshot(page, config, "download_failed")
                return result
            result["success"] = True
            result["filepath"] = filepath
            # 重命名（文件可能还被 Foxit Reader 占用，重试几次）
            if paper_info.title:
                new_name = sanitize_filename(paper_info.title) + ".pdf"
                new_path = os.path.join(os.path.dirname(filepath), new_name)
                for retry in range(5):
                    try:
                        if not os.path.exists(new_path):
                            os.rename(filepath, new_path)
                            result["filepath"] = new_path
                            log.info(f"Renamed to: {new_name}")
                        break
                    except PermissionError:
                        if retry < 4:
                            log.debug(f"File locked, retrying ({retry+1}/5)...")
                            time.sleep(3)
                        else:
                            log.warning(f"Rename failed after 5 retries: file still locked")
            rate_limiter.increment()
            return result

        # AIP 等出版商的 PDF URL 跨域（silverchair CDN），需要在 PDF 页面上 fetch
        # 其他出版商（Optica）回到文章页 fetch
        if getattr(adapter, "fetch_from_pdf_page", False):
            log.info("Staying on PDF page for cross-origin fetch...")
        else:
            log.info("Returning to article page for download...")
            adapter.navigate_to_paper(page, article_url)

    # 9. 点击前延迟（模拟人类行为）
    rate_limiter.pre_click_delay()

    # 10. 截图记录
    # debug_screenshot(page, config, "pre_download")

    # 11. 用页面上下文 fetch() 下载 PDF（真实 Chrome TLS + Cookie）
    log.info("Downloading PDF via fetch()...")
    filepath = monitor.browser_download(
        page=page,
        pdf_url=pdf_url,
    )

    if filepath is None:
        result["error"] = "PDF download failed"
        # debug_screenshot(page, config, "download_failed")
        return result

    # 14. 成功！
    result["success"] = True
    result["filepath"] = filepath

    # 15. 重命名文件（如果有元数据）
    if paper_info.title:
        new_name = sanitize_filename(paper_info.title) + ".pdf"
        new_path = os.path.join(os.path.dirname(filepath), new_name)
        try:
            if not os.path.exists(new_path):
                os.rename(filepath, new_path)
                result["filepath"] = new_path
                log.info(f"Renamed to: {new_name}")
        except Exception as e:
            log.warning(f"Rename failed: {e}")

    rate_limiter.increment()
    return result


def sanitize_filename(name: str, max_length: int = 100) -> str:
    """清理文件名，移除非法字符。"""
    import re
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:max_length]


# ---------------------------------------------------------------------------
# CLI 入口
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Paper-at-Home: 学术论文自动下载工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python main.py "https://pubs.acs.org/doi/10.1021/acs.jmedchem.4c01234"
  python main.py "10.1021/acs.jmedchem.4c01234"
  python main.py --input urls.txt --output ./papers/
        """,
    )
    parser.add_argument("url", nargs="?", help="论文 URL 或 DOI")
    parser.add_argument("--input", "-i", help="包含 URL/DOI 列表的文件路径")
    parser.add_argument("--output", "-o", help="下载文件存放目录", default=None)
    parser.add_argument("--config", "-c", help="配置文件路径", default=None)
    parser.add_argument("--debug", action="store_true", help="启用调试模式")
    parser.add_argument(
        "--launch-browser", action="store_true",
        help="自动启动 Chromium（需要先关闭所有 Chromium 窗口）",
    )
    parser.add_argument(
        "--no-warmup", action="store_true",
        help="跳过暖场页面",
    )

    args = parser.parse_args()

    # 日志
    setup_logging(debug=args.debug)
    log = logging.getLogger("main")

    # 配置
    config = load_config(args.config)
    if args.output:
        config.setdefault("download", {})["temp_dir"] = args.output

    # Banner
    console.print(Panel(
        "[bold]Paper-at-Home[/bold] — 学术论文自动下载工具\n"
        "[dim]Playwright CDP + pyautogui 真实鼠标点击[/dim]",
        style="blue",
    ))

    # 收集 URL 列表
    urls = []
    if args.url:
        urls.append(args.url)
    if args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        urls.append(line)
        except FileNotFoundError:
            console.print(f"[red]Input file not found: {args.input}[/red]")
            sys.exit(1)

    if not urls:
        console.print("[red]No URLs provided. Use positional argument or --input file.[/red]")
        parser.print_help()
        sys.exit(1)

    console.print(f"[green]Loaded {len(urls)} URL(s) to process.[/green]")

    # 初始化组件
    browser_helper = ChromiumHelper(config)
    clicker = HumanLikeClicker(config)
    monitor = DownloadMonitor(config)
    rate_limiter = RateLimiter(config)

    # 启动 Chromium（可选）
    if args.launch_browser:
        if browser_helper.is_browser_running():
            console.print("[yellow]Chromium is already running.[/yellow]")
            console.print("[yellow]Please close all Chromium windows first, or use without --launch-browser.[/yellow]")
            sys.exit(1)
        browser_helper.launch_browser()
        time.sleep(3)

    # 连接到 Chromium
    result = browser_helper.connect()
    if result is None:
        # 连接失败，尝试自动启动 Chromium 后重连
        console.print("[dim]Chromium not reachable, attempting auto-launch...[/dim]")
        browser_helper.launch_browser()
        # 轮询等待 Chromium 就绪（最多 15 秒）
        for attempt in range(5):
            time.sleep(3)
            result = browser_helper.connect()
            if result is not None:
                break
            console.print(f"[dim]  Retry {attempt+1}/5...[/dim]")
        if result is None:
            console.print("[red]Cannot connect to Chromium after auto-launch.[/red]")
            console.print("[dim]Run start_browser.bat manually, or check Chromium installation.[/dim]")
            sys.exit(1)

    pw, browser = result

    # results 必须在 try 之前初始化，防止异常导致汇总时 NameError
    results = []

    try:
        # 暖场
        if not args.no_warmup:
            page, ctx = browser_helper.get_or_create_page(browser)
            browser_helper.warmup(page)

        # 逐篇处理
        for i, raw_url in enumerate(urls, 1):
            console.print(f"\n[bold cyan]━━━ Paper {i}/{len(urls)} ━━━[/bold cyan]")

            # 解析 URL / DOI
            url, publisher = parse_input(raw_url)
            if url is None:
                console.print(f"[red]Cannot parse: {raw_url}[/red]")
                results.append({"success": False, "url": raw_url, "error": "Parse failed"})
                continue

            if publisher is None:
                console.print(f"[red]Unknown publisher for: {url}[/red]")
                results.append({"success": False, "url": url, "error": "Unknown publisher"})
                continue

            console.print(f"Publisher: [bold]{publisher}[/bold]")
            console.print(f"URL: [link={url}]{url[:80]}...[/link]" if len(url) > 80 else f"URL: [link={url}]{url}[/link]")

            # 检查 session 限制
            if rate_limiter.check_session_limit():
                console.print(
                    "[yellow]Session limit reached. "
                    "Consider restarting Chrome for safety.[/yellow]"
                )
                resp = input("Continue anyway? (y/N): ")
                if resp.lower() != "y":
                    break

            # 下载（最多 3 次尝试）
            dl_result = {"success": False, "url": url, "error": "no attempt made"}
            for attempt in range(1, 4):
                dl_result = download_paper(
                    url, publisher, config, browser, clicker, monitor, rate_limiter
                )
                if dl_result["success"]:
                    break
                if attempt < 3:
                    log_msg = f"Attempt {attempt}/3 failed: {dl_result.get('error', '?')}"
                    console.print(f"[yellow]  {log_msg}, retrying...[/yellow]")
                    time.sleep(5)
            results.append(dl_result)

            # 显示结果
            if dl_result["success"]:
                if dl_result.get("skipped"):
                    console.print(f"[bold cyan][SKIP] Already exists:[/bold cyan] {dl_result['filepath']}")
                else:
                    console.print(f"[bold green][OK] Downloaded:[/bold green] {dl_result['filepath']}")
            else:
                console.print(f"[bold red][FAIL][/bold red] {dl_result['error']} (3 attempts)")

            # 清理 tab：只保留一个 about:blank，关闭其他（PDF 查看器等）
            # 注意：skip 的情况下没有新 tab，不需要清理
            if not dl_result.get("skipped"):
                browser_helper.cleanup_tabs(browser)

            # 论文间延迟（最后一篇不需要）
            if i < len(urls):
                delay = rate_limiter.wait_between_papers()

    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user.[/yellow]")

    # 汇总报告（在 disconnect 之前，确保输出）
    console.print("\n" + "━" * 50)
    success = sum(1 for r in results if r["success"] and not r.get("skipped"))
    skipped = sum(1 for r in results if r.get("skipped"))
    failed = sum(1 for r in results if not r["success"])
    summary_parts = [f"{success} downloaded"]
    if skipped:
        summary_parts.append(f"{skipped} skipped (already exists)")
    if failed:
        summary_parts.append(f"{failed} failed")
    console.print(f"[bold]Results: {', '.join(summary_parts)}[/bold]")

    if failed > 0:
        console.print("\n[red]Failed papers:[/red]")
        for r in results:
            if not r["success"]:
                console.print(f"  - {r.get('url', '?')}: {r.get('error', 'unknown')}")

    # 保存失败报告到文件（仅在有失败时）
    if failed > 0:
        report_path = os.path.join(
            config.get("download", {}).get("temp_dir", "."),
            f"download_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        )
        with open(report_path, "w", encoding="utf-8") as f:
            for r in results:
                if not r["success"]:
                    f.write(f"[FAIL] {r.get('url', '?')} -> {r.get('error', '?')}\n")
        console.print(f"\n[dim]Failure report saved: {report_path}[/dim]")
    else:
        console.print("\n[dim]All downloads succeeded, no report file needed.[/dim]")

    browser_helper.disconnect()


if __name__ == "__main__":
    main()
