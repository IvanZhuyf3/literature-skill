"""
lit/batch/common.py — quick 和 attach 共享的批量逻辑。

两个命令（lit quick / lit attach）都需要：
  1. 找到 Zotero collection
  2. 遍历条目，筛选出缺 PDF 的
  3. 逐篇下载 → 挂载

唯一区别是下载方法。本模块抽出 1 和 2，以及批量循环框架。
"""

from __future__ import annotations

import sys
from typing import Callable

from rich.console import Console

from lit.core import zotero as zot
from lit.core.config import load as load_config

console = Console()


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

    stats: dict = {
        "skipped_no_doi": 0,
        "already_have": 0,
        "total": 0,
    }

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
    """批量下载循环。download_fn(doi) → Path | None。"""

    stats["attached"] = 0
    stats["failed"] = 0

    for i, paper in enumerate(papers):
        if limit is not None and i >= limit:
            console.print(
                f"\n  [yellow]Reached limit ({limit}), stopping.[/yellow]"
            )
            break

        console.print(f"\n  [{i + 1}/{stats['total']}] {paper['title']}")
        doi = paper["doi"]

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

        except Exception as e:
            err = str(e)[:200]
            stats["failed"] += 1
            console.print(f"    [red]✗ Failed: {err[:80]}[/red]")

    console.print(
        f"\n  [bold]Summary:[/bold] "
        f"✓ {stats['attached']} attached, "
        f"✗ {stats['failed']} failed, "
        f"⊘ {stats['skipped_no_doi']} no DOI"
    )
    return stats
