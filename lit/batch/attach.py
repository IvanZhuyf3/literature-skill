"""
lit/batch/attach.py — Publisher adapter 兜底下载（Step 3）。

两个模式：
  - 单篇：run_single(doi) → 查 Zotero item → 检查缺口 → engine.download_pdf() → attach
  - 批量：run(collection)  → 遍历 collection → 同上

本模块只做 publisher adapter 兜底（Step 3），不含 Sci-Hub（那是 lit quick 的事）。
"""

from __future__ import annotations

from pathlib import Path

from rich.console import Console

from lit.core import zotero as zot
from lit.core.config import load as load_config
from lit.download.engine import download_pdf
from lit.batch.common import collect_missing, batch_download

console = Console()


def _adapter_download(doi: str) -> Path | None:
    """包装 engine.download_pdf，统一返回 Path | None（不抛异常）。"""
    try:
        return download_pdf(doi, timeout=120)
    except Exception:
        return None


def run_single(doi: str, item_key: str | None = None) -> dict:
    """对单篇 DOI 运行 publisher adapter 兜底下载。

    Args:
        doi: DOI string.
        item_key: Optional Zotero item key (skip find_by_doi if provided).

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

    # ── 3. Publisher adapter 下载 ──
    console.print(f"  [dim]Publisher adapter: {doi} ...[/dim]")
    try:
        pdf_path: Path = download_pdf(doi, timeout=120)
        att_key = zot.attach_pdf(item_key, pdf_path)
        if att_key:
            console.print(f"  [green]✓ Attached: {att_key}[/green]")
            result["att_key"] = att_key
            result["status"] = "attached"
        else:
            console.print(f"  [yellow]⚠ 下载成功但挂载失败[/yellow]")
            result["status"] = "failed"
    except Exception as e:
        err = str(e)[:200]
        console.print(f"  [red]✗ Failed: {err}[/red]")
        result["status"] = "failed"

    return result


def run(
    collection: str,
    parent: str = "People",
    limit: int | None = None,
) -> dict:
    """批量 publisher adapter 兜底下载。"""
    papers, stats = collect_missing(collection, parent)
    if not papers:
        return stats
    return batch_download(papers, stats, _adapter_download, "Publisher", limit)
