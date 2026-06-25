"""
lit/batch/quick.py — 快速免费下载（Sci-Hub + 未来 OA 源）。

两个模式：
  - 单篇：run_single(doi) → 查 Zotero item → 检查缺口 → quick_download → attach
  - 批量：run(collection)  → 遍历 collection → 同上

本模块只做快速下载（Step 1），不含 publisher adapter（那是 lit attach 的事）。
"""

from __future__ import annotations

from rich.console import Console

from lit.core import zotero as zot
from lit.core.config import load as load_config
from lit.download.quick_download import run as quick_download
from lit.batch.common import collect_missing, batch_download

console = Console()


def run_single(doi: str, item_key: str | None = None) -> dict:
    """对单篇 DOI 运行快速下载。

    Args:
        doi: DOI string.
        item_key: Optional Zotero item key (skip find_by_doi if provided,
                  e.g. when called right after import_ref).

    Returns:
        {"status": "attached"|"already_has"|"failed"|"not_in_zotero", ...}
    """
    load_config()
    doi = doi.strip()
    result = {"doi": doi, "item_key": None, "att_key": None, "status": None}

    # ── 1. 查 Zotero item ──
    if not item_key:
        item_key = zot.find_by_doi(doi)
    if item_key is None:
        console.print(f"  [red]DOI 不在 Zotero 库中: {doi}[/red]")
        console.print(f"  [dim]先运行 lit import {doi} 注册条目[/dim]")
        result["status"] = "not_in_zotero"
        return result

    result["item_key"] = item_key
    console.print(f"  Zotero item: [bold]{item_key}[/bold]")

    # ── 2. 检查是否已有 PDF ──
    existing_pdf = zot.resolve_local_pdf(doi)
    if existing_pdf:
        console.print(f"  [green]✓ 已有 PDF（跳过）[/green]")
        console.print(f"  [dim]{existing_pdf}[/dim]")
        result["status"] = "already_has"
        return result

    # ── 3. Quick download ──
    console.print(f"  [dim]Quick download: {doi} ...[/dim]")
    pdf_path = quick_download(doi)
    if pdf_path:
        att_key = zot.attach_pdf(item_key, pdf_path)
        if att_key:
            console.print(f"  [green]✓ Attached: {att_key}[/green]")
            result["att_key"] = att_key
            result["status"] = "attached"
        else:
            console.print(f"  [yellow]⚠ 下载成功但挂载失败[/yellow]")
            result["status"] = "failed"
    else:
        console.print(f"  [dim]✗ Quick download: no PDF — try lit attach[/dim]")
        result["status"] = "failed"

    return result


def run(
    collection: str,
    parent: str = "People",
    limit: int | None = None,
) -> dict:
    """批量快速下载。"""
    papers, stats = collect_missing(collection, parent)
    if not papers:
        return stats
    return batch_download(papers, stats, quick_download, "Quick", limit)
