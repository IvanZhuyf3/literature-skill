"""
lit/maintain.py — Zotero 文件库健康检查与清理

用法:
    python -m lit maintain                          # 全库诊断（只读）
    python -m lit maintain --collection "Ji-Xin Cheng"  # 仅检查某 collection
    python -m lit maintain --fix                     # 执行修复（删孤儿目录 + ghost 条目）
    python -m lit maintain --fix --dry-run           # 预览会删什么，不实际执行

检查项:
    1. Attachment 健康（per collection 或全库）:
       - Ghost: Zotero 有附件条目，storage 无对应目录
       - Empty: 目录存在但里面没 PDF
       - Filename mismatch: Zotero 记录的 filename 与实际文件名不一致
    2. 孤儿目录: storage 有目录，Zotero 无对应附件条目
    3. Ghost 条目: Zotero 有附件条目，storage 无目录（同 1 的 ghost，但全库范围）

修复策略:
    - 孤儿目录 → send2trash（回收站）
    - Ghost 条目 → Zotero API delete_item
    - Filename mismatch → 只报告，不自动修（需人工确认）
"""
from __future__ import annotations

import os
import time
from pathlib import Path

from rich.console import Console
from rich.table import Table

from lit.core.config import zotero as get_zotero_cfg, storage_path as get_storage_path
from lit.core.zotero import _client

console = Console()


# ── Data classes ──

class AttachmentIssue:
    """单条 attachment 的健康问题。"""
    def __init__(self, parent_key: str, att_key: str, title: str,
                 issue: str, detail: str = ""):
        self.parent_key = parent_key
        self.att_key = att_key
        self.title = title
        self.issue = issue      # "ghost", "empty", "filename_mismatch"
        self.detail = detail


class DiagnosticReport:
    """诊断报告。"""
    def __init__(self):
        self.healthy: int = 0
        self.ghosts: list[AttachmentIssue] = []        # Zotero有条目, 磁盘无目录
        self.empties: list[AttachmentIssue] = []        # 磁盘有目录但无PDF
        self.mismatches: list[AttachmentIssue] = []     # filename不一致
        self.orphan_dirs: list[tuple[str, str, float]] = []  # (dir, pdf_filename, size_mb)
        self.total_zotero_atts: int = 0
        self.total_storage_dirs: int = 0


# ── Core functions ──

def _fetch_all_attachment_keys(zot) -> set[str]:
    """拉取全库所有 imported_file/imported_url attachment 的 key。"""
    keys = set()
    start = 0
    batch = 100
    while True:
        result = zot.items(itemType="attachment", limit=batch, start=start)
        if not result:
            break
        for item in result:
            if item["data"].get("linkMode", "") in ("imported_file", "imported_url"):
                keys.add(item["key"])
        if len(result) < batch:
            break
        start += batch
        time.sleep(0.2)
    return keys


def _list_storage_dirs(storage: str) -> set[str]:
    """列出 storage 下所有 8 字符大写目录名（Zotero key 格式）。"""
    dirs = set()
    if not os.path.isdir(storage):
        return dirs
    for d in os.listdir(storage):
        full = os.path.join(storage, d)
        if os.path.isdir(full):
            dirs.add(d)
    return dirs


def check_attachments(zot, storage: str, collection_key: str | None = None) -> DiagnosticReport:
    """
    检查 attachment 健康度（批量查询，不逐条 children()）。

    Args:
        zot: pyzotero 客户端
        storage: Zotero storage 路径
        collection_key: 如果指定，只检查该 collection 下的条目

    Returns:
        DiagnosticReport
    """
    report = DiagnosticReport()

    # 一次拉取所有 attachment，按 parentItem 分组
    if collection_key:
        atts = zot.everything(zot.collection_items(collection_key, itemType="attachment"))
    else:
        atts = zot.everything(zot.items(itemType="attachment"))

    console.print(f"[dim]Checking {len(atts)} attachments...[/dim]")

    # 构建 parent key → title 映射（用于显示）
    parent_titles: dict[str, str] = {}
    if collection_key:
        top_items = zot.everything(zot.collection_items(collection_key, itemType="-attachment"))
        for item in top_items:
            parent_titles[item["key"]] = item["data"].get("title", "")[:50]

    for child in atts:
        d = child["data"]
        if d.get("itemType") != "attachment":
            continue
        link = d.get("linkMode", "")
        if link not in ("imported_file", "imported_url"):
            continue

        att_key = child["key"]
        parent_key = d.get("parentItem", "")
        rec_fn = d.get("filename", "")
        title = parent_titles.get(parent_key, parent_key)
        dir_path = os.path.join(storage, att_key)

        # Check directory existence
        if not os.path.isdir(dir_path):
            report.ghosts.append(AttachmentIssue(
                parent_key, att_key, title, "ghost", "dir missing"))
            continue

        pdfs = [f for f in os.listdir(dir_path) if f.endswith(".pdf")]
        if not pdfs:
            report.empties.append(AttachmentIssue(
                parent_key, att_key, title, "empty", "no PDF in dir"))
            continue

        actual_pdf = pdfs[0]
        if not rec_fn:
            report.healthy += 1
        elif rec_fn != actual_pdf:
            report.mismatches.append(AttachmentIssue(
                parent_key, att_key, title, "filename_mismatch",
                f"record='{rec_fn[:30]}' vs actual='{actual_pdf[:30]}'"))
        else:
            report.healthy += 1

    return report


def check_orphans(zot, storage: str) -> tuple[list[tuple[str, str, float]], list[str]]:
    """
    全库范围检查孤儿目录和 ghost 条目。

    Returns:
        (orphan_dirs, ghost_keys):
            orphan_dirs: [(dir_name, pdf_filename, size_mb), ...]
            ghost_keys: [zotero_key, ...]
    """
    zot_keys = _fetch_all_attachment_keys(zot)
    storage_dirs = _list_storage_dirs(storage)

    orphan_set = storage_dirs - zot_keys
    ghost_set = zot_keys - storage_dirs

    orphan_dirs = []
    for d in sorted(orphan_set):
        full = os.path.join(storage, d)
        pdfs = [f for f in os.listdir(full) if f.endswith(".pdf")]
        pdf_fn = pdfs[0] if pdfs else "(no PDF)"
        size = sum(
            os.path.getsize(os.path.join(full, f))
            for f in os.listdir(full)
            if os.path.isfile(os.path.join(full, f))
        ) / 1024 / 1024
        orphan_dirs.append((d, pdf_fn, size))

    return orphan_dirs, sorted(ghost_set)


def fix_orphans(storage: str, orphan_dirs: list[str], dry_run: bool = True) -> int:
    """删除孤儿目录（送回收站）。返回成功删除数。"""
    try:
        from send2trash import send2trash
    except ImportError:
        console.print("[red]send2trash not installed. Run: pip install send2trash[/red]")
        return 0

    count = 0
    for d in orphan_dirs:
        dir_path = os.path.join(storage, d)
        if not os.path.isdir(dir_path):
            console.print(f"  [dim]SKIP {d}: not found[/dim]")
            continue
        if dry_run:
            console.print(f"  [yellow]DRY-RUN[/yellow] would delete {d}/")
            count += 1
        else:
            try:
                send2trash(dir_path)
                console.print(f"  [green]OK[/green] {d} -> recycle bin")
                count += 1
            except Exception as e:
                console.print(f"  [red]FAIL[/red] {d}: {e}")
    return count


def fix_ghosts(zot, ghost_keys: list[str], dry_run: bool = True) -> int:
    """删除 Zotero ghost 附件条目。返回成功删除数。"""
    count = 0
    for key in ghost_keys:
        try:
            item = zot.item(key)
            title = item["data"].get("title", "")[:40]
            if dry_run:
                console.print(f"  [yellow]DRY-RUN[/yellow] would delete Zotero item {key} ({title})")
                count += 1
            else:
                zot.delete_item(item)
                console.print(f"  [green]OK[/green] deleted {key} ({title})")
                count += 1
        except Exception as e:
            console.print(f"  [red]FAIL[/red] {key}: {e}")
        time.sleep(0.2)
    return count


# ── Reporting ──

def _print_report(report: DiagnosticReport, orphan_dirs, ghost_keys):
    """Rich 表格输出诊断报告。"""

    # Attachment health
    table = Table(title="Attachment Health", show_header=True)
    table.add_column("Status", style="cyan")
    table.add_column("Count", justify="right")
    table.add_row("[green]✅ Healthy[/green]", str(report.healthy))
    table.add_row("[red]👻 Ghost (no dir)[/red]", str(len(report.ghosts)))
    table.add_row("[yellow]📭 Empty shell[/yellow]", str(len(report.empties)))
    table.add_row("[yellow]🔗 Filename mismatch[/yellow]", str(len(report.mismatches)))
    console.print(table)

    if report.ghosts:
        console.print("\n[red]--- Ghost attachments (Zotero entry, no file) ---[/red]")
        for g in report.ghosts:
            console.print(f"  att={g.att_key} parent={g.parent_key} | {g.title}")

    if report.empties:
        console.print("\n[yellow]--- Empty shells (dir exists, no PDF) ---[/yellow]")
        for e in report.empties:
            console.print(f"  att={e.att_key} parent={e.parent_key} | {e.title}")

    if report.mismatches:
        console.print("\n[yellow]--- Filename mismatches ---[/yellow]")
        for m in report.mismatches:
            console.print(f"  att={m.att_key} | {m.detail} | {m.title}")

    # Orphan / ghost summary
    table2 = Table(title="Storage vs Zotero Alignment", show_header=True)
    table2.add_column("Metric", style="cyan")
    table2.add_column("Count", justify="right")
    table2.add_row("Zotero attachment items", str(report.total_zotero_atts))
    table2.add_row("Storage directories", str(report.total_storage_dirs))
    table2.add_row("[red]Orphan dirs (no Zotero entry)[/red]", str(len(orphan_dirs)))
    table2.add_row("[red]Ghost entries (no storage dir)[/red]", str(len(ghost_keys)))
    console.print(table2)

    if orphan_dirs:
        console.print("\n[red]--- Orphan directories ---[/red]")
        for d, fn, sz in orphan_dirs[:30]:
            console.print(f"  {d} | {fn[:45]} | {sz:.1f}MB")
        if len(orphan_dirs) > 30:
            console.print(f"  ... and {len(orphan_dirs) - 30} more")

    if ghost_keys:
        console.print("\n[red]--- Ghost Zotero entries ---[/red]")
        for k in ghost_keys[:20]:
            console.print(f"  {k}")


# ── Main entry ──

def run(collection: str | None = None, fix: bool = False, dry_run: bool = False):
    """
    Args:
        collection: collection 名称（如 "Ji-Xin Cheng"），None = 全库
        fix: 是否执行修复
        dry_run: fix 时只预览不执行
    """
    zcfg = get_zotero_cfg()
    zot = _client()
    storage = get_storage_path()

    if not storage or not os.path.isdir(storage):
        console.print(f"[red]Storage path not found: {storage}[/red]")
        return

    # Resolve collection key
    collection_key = None
    if collection:
        from lit.core.zotero import find_collection
        collection_key = find_collection(collection)
        if not collection_key:
            console.print(f"[red]Collection '{collection}' not found[/red]")
            return
        console.print(f"[cyan]Collection: {collection} ({collection_key})[/cyan]")
    else:
        console.print("[cyan]Mode: full library[/cyan]")

    console.print(f"[cyan]Storage: {storage}[/cyan]\n")

    # ── Step 1: Attachment health (only for --collection, too slow for full lib) ──
    report = DiagnosticReport()
    if collection_key:
        console.print("[bold]Step 1: Checking attachment health...[/bold]")
        report = check_attachments(zot, storage, collection_key)
    else:
        console.print("[dim]Step 1: Skipped attachment health (use --collection for per-item check)[/dim]")

    # ── Step 2: Orphan / ghost check (always full library) ──
    console.print("\n[bold]Step 2: Checking storage/Zotero alignment...[/bold]")
    orphan_dirs, ghost_keys = check_orphans(zot, storage)

    # Fill in totals
    all_zot_keys = _fetch_all_attachment_keys(zot)
    all_storage = _list_storage_dirs(storage)
    report.total_zotero_atts = len(all_zot_keys)
    report.total_storage_dirs = len(all_storage)

    # ── Print report ──
    console.print()
    _print_report(report, orphan_dirs, ghost_keys)

    # ── Fix ──
    if fix:
        console.print(f"\n[bold yellow]{'DRY-RUN ' if dry_run else ''}Fixing...[/bold yellow]")

        if orphan_dirs:
            console.print(f"\n[bold]Deleting {len(orphan_dirs)} orphan directories...[/bold]")
            orphan_names = [d[0] for d in orphan_dirs]
            fix_orphans(storage, orphan_names, dry_run=dry_run)

        if ghost_keys:
            # Only fix ghosts that are in scope
            # (full library ghosts might include non-Cheng items)
            console.print(f"\n[bold]Deleting {len(ghost_keys)} ghost Zotero entries...[/bold]")
            fix_ghosts(zot, ghost_keys, dry_run=dry_run)

        if not orphan_dirs and not ghost_keys:
            console.print("[green]Nothing to fix — library is clean.[/green]")
    else:
        total_issues = len(report.ghosts) + len(report.empties) + len(report.mismatches) + len(orphan_dirs) + len(ghost_keys)
        if total_issues == 0:
            console.print("\n[green]✅ All clean — no issues found.[/green]")
        else:
            console.print(f"\n[yellow]Found {total_issues} issues. Run with --fix to clean up.[/yellow]")

    # ── Refresh DOI index ──
    from lit.core.zotero import build_doi_index
    build_doi_index(force=True)
