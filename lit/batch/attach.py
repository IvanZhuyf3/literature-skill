"""
lit/batch/attach.py — Batch PDF attachment module.

Reads a Zotero collection, finds items without PDF attachments,
downloads & attaches PDFs for them. Adapted from ``zotero_attach.py``
using the new ``lit.core.*`` modules.

Usage:
    from lit.batch.attach import run
    stats = run("Ji-Xin Cheng")
    stats = run("Ji-Xin Cheng", limit=5)
"""

from __future__ import annotations

import sys
from pathlib import Path

from rich.console import Console

from lit.core import zotero as zot
from lit.core.config import load as load_config
from lit.download.engine import download_pdf

console = Console()


def run(
    collection: str,
    parent: str = "People",
    limit: int | None = None,
) -> dict:
    """Batch-attach PDFs to items in a Zotero collection.

    Args:
        collection: Collection name (e.g. ``"Ji-Xin Cheng"``).
        parent: Parent collection name (default ``"People"``).
        limit: Max papers to process (``None`` = no limit).

    Returns:
        dict with stats: ``attached``, ``failed``, ``skipped_no_doi``,
        ``already_have``, ``total``.
    """
    load_config()  # ensure config is valid; will sys.exit(1) if missing

    stats: dict = {
        "attached": 0,
        "failed": 0,
        "skipped_no_doi": 0,
        "already_have": 0,
        "total": 0,
    }

    # ── Step 1: locate collection ──────────────────────────────
    collection_key = zot.find_collection(collection, parent)
    if collection_key is None:
        console.print(
            f"  [red]Collection '{parent}/{collection}' not found.[/red]"
        )
        console.print(
            f"  Run [bold]lit scholar --name \"{collection}\"[/bold] first."
        )
        sys.exit(1)

    console.print(
        f"\n  Collection: [bold]{parent}/{collection}[/bold] ({collection_key})"
    )

    # ── Step 2: read ALL items (including children) ────────────
    all_items = zot.collection_items(collection_key)
    console.print(f"  Items in collection (incl. children): {len(all_items)}")

    # Separate parents and children
    parents: dict[str, dict] = {}  # key → item data
    attached_pdf_keys: set[str] = set()  # parent keys that have PDF attachments
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

    # ── Step 3: filter — parents without PDF + with DOI ────────
    to_process: list[dict] = []
    for key, d in parents.items():
        doi = (d.get("DOI") or "").strip()
        if not doi:
            stats["skipped_no_doi"] += 1
            continue
        if key in attached_pdf_keys:
            stats["already_have"] += 1
            continue
        to_process.append({
            "key": key,
            "doi": doi,
            "title": (d.get("title") or "")[:70],
        })

    stats["total"] = len(to_process)
    console.print(f"  Already have PDF:  {stats['already_have']}")
    console.print(f"  Skipped (no DOI):  {stats['skipped_no_doi']}")
    console.print(f"  Missing PDF:       {stats['total']}")

    if not to_process:
        console.print("\n  [green]✓ All items already have PDFs attached.[/green]")
        return stats

    # ── Step 4: download + attach ──────────────────────────────
    from lit.download.engine import download_pdf

    for i, paper in enumerate(to_process):
        if limit is not None and i >= limit:
            console.print(
                f"\n  [yellow]Reached limit ({limit}), stopping.[/yellow]"
            )
            break

        console.print(f"\n  [{i + 1}/{stats['total']}] {paper['title']}")
        doi = paper["doi"]

        try:
            console.print(f"    [dim]Downloading {doi} ...[/dim]")
            pdf_path: Path = download_pdf(doi, timeout=120)

            att_key = zot.attach_pdf(paper["key"], pdf_path)
            stats["attached"] += 1
            console.print(f"    [green]✓ Attached: {att_key}[/green]")

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
