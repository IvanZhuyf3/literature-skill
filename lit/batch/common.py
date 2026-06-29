"""
lit/batch/common.py — quick 和 attach 共享的批量逻辑。

两个命令（lit quick / lit attach）都需要：
  1. 找到 Zotero collection
  2. 遍历条目，筛选出缺 PDF 的
  3. 逐篇下载 → 挂载

唯一区别是下载方法。本模块抽出 1 和 2，以及批量循环框架。

停止机制：
  - `lit stop` 命令读取 .batch.pid，发送 SIGTERM 杀进程树
  - batch_download() 注册信号处理器，收到信号后在当前论文完成后退出
  - PID 文件在 batch_download() 进入和退出时自动维护
"""

from __future__ import annotations

import os
import signal
import sys
from pathlib import Path
from typing import Callable

from publisher.base import VideoOnlyError

from rich.console import Console

from lit.core import zotero as zot
from lit.core.config import load as load_config
from lit.core.config import skill_base

console = Console()

# ── 停止信号 ──────────────────────────────────────────────────────────
_stop_requested = False
_pid_file = skill_base() / ".batch.pid"
_stop_file = skill_base() / ".batch.stop"  # sentinel: lit stop creates this


def _check_stop_file() -> bool:
    """检查是否存在停止 sentinel 文件（lit stop 创建）。"""
    return _stop_file.exists()


def _clear_stop_file():
    """清除停止 sentinel 文件。"""
    try:
        _stop_file.unlink(missing_ok=True)
    except Exception:
        pass


def _signal_handler(signum, frame):
    """SIGINT handler — Ctrl+C 在终端里有效。"""
    global _stop_requested
    _stop_requested = True
    console.print(
        f"\n  [yellow bold]⚠ Stop requested"
        f" ({signal.Signals(signum).name}) — finishing current paper, then exiting.[/yellow bold]"
    )


def _write_pid():
    """写入当前进程 PID 到 .batch.pid，供 `lit stop` 使用。"""
    _pid_file.write_text(str(os.getpid()), encoding="utf-8")


def _clear_pid():
    """清除 PID 文件。"""
    try:
        _pid_file.unlink(missing_ok=True)
    except Exception:
        pass


def is_batch_running() -> bool:
    """检查是否有批量任务正在运行（PID 文件存在且进程活着）。"""
    if not _pid_file.exists():
        return False
    try:
        pid = int(_pid_file.read_text(encoding="utf-8").strip())
        os.kill(pid, 0)  # signal 0 = check if process exists
        return True
    except (ProcessLookupError, ValueError, OSError):
        # Process dead or invalid PID — clean up stale file
        _clear_pid()
        return False


def collect_missing(
    collection: str,
    parent: str = "People",
) -> tuple[list[dict], dict]:
    """遍历 collection，返回缺 PDF 的条目列表。

    Returns:
        (to_process, stats)
        to_process: [{key, doi, title}, ...]
        stats: {already_have, skipped_no_doi, total}
    """
    load_config()

    collection_key = zot.find_collection(collection, parent)
    if collection_key is None:
        console.print(
            f"  [red]Collection '{parent}/{collection}' not found.[/red]"
        )
        console.print(
            f"  Run [bold]lit scholar <URL>[/bold] first."
        )
        sys.exit(1)

    console.print(
        f"\n  Collection: [bold]{parent}/{collection}[/bold] ({collection_key})"
    )

    stats: dict = {
        "skipped_no_doi": 0,
        "already_have": 0,
        "collection_key": collection_key,
        "total": 0,
    }

    all_items = zot.collection_items(collection_key)
    console.print(f"  Items (incl. children): {len(all_items)}")

    parents: dict[str, dict] = {}
    attached_pdf_keys: set[str] = set()
    for item in all_items:
        d = item.get("data", {})
        key = item.get("key")
        itype = d.get("itemType", "")
        if itype in ("attachment", "note"):
            parent_key = d.get("parentItem", "")
            if parent_key and d.get("contentType") == "application/pdf":
                attached_pdf_keys.add(parent_key)
        else:
            parents[key] = d

    console.print(
        f"    Parents: {len(parents)}, have PDF: {len(attached_pdf_keys)}"
    )

    to_process: list[dict] = []
    for key, d in parents.items():
        doi = (d.get("DOI") or "").strip()
        if not doi:
            stats["skipped_no_doi"] += 1
            continue
        if key in attached_pdf_keys:
            stats["already_have"] += 1
            continue
        # 额外检查：磁盘上文件真实存在（ghost 附件）
        if zot.resolve_local_pdf(doi):
            stats["already_have"] += 1
            continue
        to_process.append({
            "key": key,
            "doi": doi,
            "title": (d.get("title") or "")[:70],
        })

    stats["total"] = len(to_process)
    console.print(f"  Already have PDF: {stats['already_have']}")
    console.print(f"  Skipped (no DOI): {stats['skipped_no_doi']}")
    console.print(f"  Missing PDF:      {stats['total']}")

    if not to_process:
        console.print("\n  [green]✓ All items already have PDFs.[/green]")

    return to_process, stats


def batch_download(
    papers: list[dict],
    stats: dict,
    download_fn: Callable[[str], object],
    label: str,
    limit: int | None = None,
) -> dict:
    """批量下载循环。download_fn(doi) → Path | None。

    支持优雅停止：收到 SIGINT/SIGTERM 后在当前论文完成后退出。
    """

    global _stop_requested

    # ── 注册信号处理器 + 写 PID + 清除旧 stop sentinel ──
    _stop_requested = False
    _clear_stop_file()
    _write_pid()
    signal.signal(signal.SIGINT, _signal_handler)

    stats["attached"] = 0
    stats["failed"] = 0
    stats["video_only"] = 0

    try:
        for i, paper in enumerate(papers):
            # ── 检查停止信号（sentinel file + signal flag）──
            if _stop_requested or _check_stop_file():
                console.print(
                    f"\n  [yellow]Stopped at [{i + 1}/{stats['total']}]. "
                    f"{len(papers) - i} papers remaining.[/yellow]"
                )
                break

            if limit is not None and i >= limit:
                console.print(
                    f"\n  [yellow]Reached limit ({limit}), stopping.[/yellow]"
                )
                break

            console.print(f"\n  [{i + 1}/{stats['total']}] {paper['title']}")
            doi = paper["doi"]

            # ── Re-check: PDF may have been added since collect_missing ──
            if zot.resolve_local_pdf(doi):
                stats["already_have"] = stats.get("already_have", 0) + 1
                console.print(f"    [dim]⊘ Already has PDF (skipped)[/dim]")
                continue

            try:
                console.print(f"    [dim]{label}: {doi} ...[/dim]")
                pdf_path = download_fn(doi)

                if pdf_path:
                    att_key = zot.attach_pdf(paper["key"], pdf_path)
                    if att_key:
                        stats["attached"] += 1
                        console.print(f"    [green]✓ Attached: {att_key}[/green]")
                    else:
                        stats["failed"] += 1
                        console.print(f"    [yellow]⚠ Downloaded but attach failed[/yellow]")
                else:
                    stats["failed"] += 1
                    console.print(f"    [dim]✗ {label}: no PDF[/dim]")

            except VideoOnlyError:
                # 会议视频，无 PDF — 移出当前 collection
                stats["video_only"] += 1
                col_key = stats.get("collection_key")
                if col_key:
                    try:
                        client = zot._client()
                        item = client.item(paper["key"])
                        collections = item["data"].get("collections", [])
                        if col_key in collections:
                            collections.remove(col_key)
                            client.update_item(item)
                    except Exception:
                        pass
                console.print(f"    [cyan]📺 Video-only — removed from collection[/cyan]")

            except Exception as e:
                err = str(e)[:200]
                stats["failed"] += 1
                console.print(f"    [red]✗ Failed: {err[:80]}[/red]")

    finally:
        _clear_pid()
        _clear_stop_file()

    stopped_note = " (stopped)" if (_stop_requested or _check_stop_file()) else ""
    console.print(
        f"\n  [bold]Summary:{stopped_note}[/bold] "
        f"✓ {stats['attached']} attached, "
        f"✗ {stats['failed']} failed, "
        f"📺 {stats.get('video_only', 0)} video-only, "
        f"⊘ {stats['skipped_no_doi']} no DOI"
    )
    return stats
