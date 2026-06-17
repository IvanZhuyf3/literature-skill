"""
zotero_attach.py — Read Zotero collection, find items without PDF, download & attach.

Designed for the human-in-the-loop workflow:
  1. Agent registers items to Zotero (via people.py --register-only)
  2. User cleans data in Zotero (delete irrelevant, fix metadata, deduplicate)
  3. Agent runs this module to batch-download + attach missing PDFs

The Zotero collection is the Single Source of Truth — no dependency on
scraped papers.json or Scholar data.

Usage:
    python zotero_attach.py --collection "Ji-Xin Cheng"
    python zotero_attach.py --collection "Ji-Xin Cheng" --max-papers 5
    python zotero_attach.py --collection "Ji-Xin Cheng" --parent "People"

Import from code:
    from zotero_attach import attach_missing_pdfs
    stats = attach_missing_pdfs("Ji-Xin Cheng", cfg)
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import yaml
from rich.console import Console

SKILL_BASE = Path(__file__).resolve().parent
CONFIG_PATH = SKILL_BASE / "config.yaml"

console = Console()


# ---------------------------------------------------------------------------
# Config helpers
# ---------------------------------------------------------------------------

def load_config() -> dict:
    """Load config.yaml; die with actionable message if missing."""
    if not CONFIG_PATH.exists():
        console.print(f"[red]config.yaml not found at {CONFIG_PATH}[/red]")
        sys.exit(1)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ---------------------------------------------------------------------------
# Core: find collection + read items + filter + download
# ---------------------------------------------------------------------------

def find_collection_key(collection_name: str, cfg: dict,
                        parent_collection: str = "People") -> str:
    """Find or create a Zotero collection by name under a parent.

    Args:
        collection_name: The leaf collection name (e.g. "Ji-Xin Cheng")
        parent_collection: The parent collection name (default "People")

    Returns:
        The Zotero collection key.
    """
    from pyzotero import zotero as zotero_mod

    zcfg = cfg["zotero"]
    zot = zotero_mod.Zotero(zcfg["library_id"], zcfg.get("library_type", "user"),
                             zcfg["api_key"])

    all_cols = zot.collections()

    # Find parent
    parent_key = None
    for col in all_cols:
        if (col["data"]["name"] == parent_collection
                and not col["data"].get("parentCollection", False)):
            parent_key = col["key"]
            break

    if not parent_key:
        console.print(f"  [yellow]Parent collection '{parent_collection}' not found, creating...[/yellow]")
        resp = zot.create_collections([{
            "name": parent_collection,
            "parentCollection": False,
        }])
        parent_key = resp["successful"]["0"]["key"]

    # Find leaf
    for col in all_cols:
        if (col["data"]["name"] == collection_name
                and col["data"].get("parentCollection") == parent_key):
            return col["key"]

    console.print(f"  [red]Collection '{parent_collection}/{collection_name}' not found.[/red]")
    console.print(f"  Run [bold]people.py --register-only --scholar-name \"{collection_name}\"[/bold] first.")
    sys.exit(1)


def attach_missing_pdfs(collection_name: str, cfg: dict,
                         parent_collection: str = "People",
                         max_downloads: int | None = None) -> dict:
    """Read a Zotero collection, find items without PDF attachments, download & attach.

    The collection is the source of truth — reads directly from Zotero API,
    not from any scraped JSON file.

    Args:
        collection_name: Zotero collection name (e.g. "Ji-Xin Cheng")
        cfg: Full config dict from config.yaml
        parent_collection: Parent collection name (default "People")
        max_downloads: Max papers to process (None = no limit)

    Returns:
        dict with keys: attached, failed, skipped_no_doi, already_have, total
    """
    from pyzotero import zotero as zotero_mod

    zcfg = cfg["zotero"]
    zot = zotero_mod.Zotero(zcfg["library_id"], zcfg.get("library_type", "user"),
                             zcfg["api_key"])
    stats = {"attached": 0, "failed": 0, "skipped_no_doi": 0,
             "already_have": 0, "total": 0}

    # Step 1: locate collection
    collection_key = find_collection_key(collection_name, cfg, parent_collection)
    console.print(f"\n  Collection: [bold]{parent_collection}/{collection_name}[/bold] ({collection_key})")

    # Step 2: read ALL items including children (more efficient than checking
    # each parent's children individually, which would be N API calls)
    # pyzotero's collection_items returns both parents and children.
    all_items: list[dict] = []
    start = 0
    while True:
        # NOTE: collection_items (not _top) returns children as well
        batch = zot.collection_items(collection_key, limit=100, start=start)
        if not batch:
            break
        all_items.extend(batch)
        start += 100
        if len(batch) < 100:
            break
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

    console.print(f"    Parents: {len(parents)}, have PDF: {len(attached_pdf_keys)}")

    # Step 3: filter — parents without PDF + with DOI
    to_process: list[dict] = []
    for key, d in parents.items():
        doi = d.get("DOI", "").strip()
        if not doi:
            stats["skipped_no_doi"] += 1
            continue
        if key in attached_pdf_keys:
            stats["already_have"] += 1
            continue
        to_process.append({
            "key": key,
            "doi": doi,
            "title": d.get("title", "")[:70],
        })

    stats["total"] = len(to_process)
    console.print(f"  Already have PDF:  {stats['already_have']}")
    console.print(f"  Skipped (no DOI):  {stats['skipped_no_doi']}")
    console.print(f"  Missing PDF:       {stats['total']}")

    if not to_process:
        console.print("\n  [green]✓ All items already have PDFs attached.[/green]")
        return stats

    # Step 4: download + attach
    import zot as zot_mod
    from url_parser import resolve_doi

    for i, paper in enumerate(to_process):
        if max_downloads is not None and i >= max_downloads:
            console.print(f"\n  [yellow]Reached --max-papers limit ({max_downloads}), stopping.[/yellow]")
            break

        console.print(f"\n  [{i+1}/{stats['total']}] {paper['title']}")
        doi = paper["doi"]

        try:
            # Resolve DOI → publisher URL
            try:
                resolved = resolve_doi(doi)
                dl_url = resolved if resolved else f"https://doi.org/{doi}"
            except Exception:
                dl_url = f"https://doi.org/{doi}"

            console.print(f"    [dim]Downloading {doi} ...[/dim]")
            pdf_path = zot_mod.download_pdf(dl_url, cfg, timeout=120)

            att_key = zot_mod.attach_pdf(paper["key"], pdf_path, cfg)
            stats["attached"] += 1
            console.print(f"    [green]✓ Attached: {att_key}[/green]")

        except Exception as e:
            err = str(e)[:200]
            stats["failed"] += 1
            console.print(f"    [red]✗ Failed: {err[:80]}[/red]")

    console.print(f"\n  [bold]Summary:[/bold] "
                  f"✓ {stats['attached']} attached, "
                  f"✗ {stats['failed']} failed, "
                  f"⊘ {stats['skipped_no_doi']} no DOI")
    return stats


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="zotero_attach: Batch-attach PDFs to Zotero collection items",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            '  python zotero_attach.py --collection "Ji-Xin Cheng"\n'
            '  python zotero_attach.py --collection "Ji-Xin Cheng" --max-papers 5\n'
            '  python zotero_attach.py --collection "Yifan Zhu" --parent "People"\n'
        ),
    )
    parser.add_argument("--collection", required=True,
                        help="Zotero collection name under People/ (e.g. 'Ji-Xin Cheng')")
    parser.add_argument("--parent", default="People",
                        help="Parent collection name (default: People)")
    parser.add_argument("--max-papers", type=int, default=None,
                        help="Limit number of papers to process")
    args = parser.parse_args()

    cfg = load_config()
    stats = attach_missing_pdfs(
        args.collection,
        cfg,
        parent_collection=args.parent,
        max_downloads=args.max_papers,
    )

    # Exit code: 0 if all succeeded, 1 if any failed
    sys.exit(1 if stats["failed"] > 0 else 0)


if __name__ == "__main__":
    main()
