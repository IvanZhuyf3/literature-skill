"""
lit/batch/register.py — Batch Zotero registration from metadata dicts.

Registers a list of paper metadata dicts as Zotero journal article items.
No intermediate JSON files are written.
Adapted from ``people.py``'s ``register_to_zotero()``.

Usage:
    from lit.batch.register import register_papers
    papers = register_papers(papers, collection_key, cfg)
"""

from __future__ import annotations

from typing import Callable

from rich.console import Console

from lit.core import zotero as zot
from lit.core.config import load as load_config

console = Console()


def register_papers(
    papers: list[dict],
    collection_key: str,
    cfg: dict | None = None,
    save_callback: Callable[[list[dict]], None] | None = None,
) -> list[dict]:
    """Register all DOI-matched papers as Zotero items. No PDF needed.

    Iterates over a list of paper dicts, checks for existing Zotero items
    (via DOI/title dedup), creates new journal-article items, and assigns
    them to the given collection.

    Args:
        papers: List of paper dicts. Each should have:
            ``doi``, ``title``, ``year``, ``venue`` (journal), ``authors``.
            Papers with an existing ``zotero_key`` are skipped.
            Papers without a ``doi`` get ``zotero_status = "no_doi"``.
        collection_key: Target Zotero collection key (string).
        cfg: Legacy config dict (kept for compatibility; may be ``None``).
        save_callback: Optional callable(papers) called every 10 papers and
            at the end. Defaults to a no-op. Callers that want progress
            tracking or persistence can pass a custom callback.

    Returns:
        Updated ``papers`` list with ``zotero_key`` and ``zotero_status``
        (and ``zotero_error`` on failure) fields populated.
    """
    load_config()

    console.print(f"\n[bold cyan]━━━ Zotero Batch Registration ({len(papers)} papers) ━━━[/bold cyan]\n")

    # ── Filter: skip already-registered, skip no-DOI ──────────────
    to_register: list[dict] = []
    for p in papers:
        if p.get("zotero_key"):
            continue  # already registered
        if not p.get("doi"):
            p["zotero_status"] = "no_doi"
            continue
        to_register.append(p)

    if not to_register:
        console.print("  [green]All papers already registered or no DOIs.[/green]")
        return papers

    console.print(f"  To register: {len(to_register)} (skipped {len(papers) - len(to_register)})")

    # ── Register each paper ───────────────────────────────────────
    for i, paper in enumerate(to_register):
        title = paper.get("title", "")[:70]
        doi = paper.get("doi", "")
        console.print(f"\n  [{i + 1}/{len(to_register)}] {title}")

        try:
            # 1. Dedup check
            existing_key, match_reason = zot.check_duplicate(
                doi=doi,
                title=paper.get("title", ""),
                url=f"https://doi.org/{doi}",
            )
            if existing_key:
                paper["zotero_key"] = existing_key
                paper["zotero_status"] = f"exists_{match_reason}"
                console.print(f"    [yellow]↻ Exists ({match_reason}): {existing_key}[/yellow]")
                # Still ensure it's in the target collection
                zot.assign_to_collection(existing_key, collection_key)
                continue

            # 2. Build metadata for new item
            meta: dict = {
                "DOI": doi,
                "title": paper.get("title", ""),
                "url": f"https://doi.org/{doi}",
                "journal": paper.get("venue", ""),
                "year": str(paper.get("year", "")),
            }
            author_str = paper.get("authors", "")
            if author_str:
                raw = [a.strip() for a in author_str.split(",")]
                meta["authors"] = [
                    a for a in raw if a and a != "..." and len(a) > 1
                ]

            # 3. Create Zotero item
            item_key = zot.create_item(meta)
            paper["zotero_key"] = item_key
            paper["zotero_status"] = "registered"
            console.print(f"    [green]✓ Created: {item_key}[/green]")

            # 4. Assign to collection
            zot.assign_to_collection(item_key, collection_key)

        except Exception as e:
            paper["zotero_status"] = "failed"
            paper["zotero_error"] = str(e)[:200]
            console.print(f"    [red]✗ {str(e)[:80]}[/red]")

        # Periodic save callback (every 10 papers)
        if save_callback and (i + 1) % 10 == 0:
            save_callback(papers)

    # Final save callback
    if save_callback:
        save_callback(papers)

    # ── Summary ───────────────────────────────────────────────────
    registered = sum(1 for p in papers if p.get("zotero_key"))
    failed = sum(1 for p in papers if p.get("zotero_status") == "failed")
    console.print(
        f"\n  [bold green]Done: {registered} registered/verified, "
        f"{failed} failed[/bold green]"
    )

    return papers
