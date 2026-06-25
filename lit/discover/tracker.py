"""
lit/discover/tracker.py — 增量论文追踪

双源检测：Semantic Scholar (author ID) + CrossRef (name query)
输出新 DOI 列表，与 Zotero SQLite 比对去重。

用法:
    from lit.discover.tracker import find_new_papers
    new_dois = find_new_papers("Ji-Xin Cheng")
"""

from __future__ import annotations

import json
import time
import unicodedata
from datetime import datetime, timedelta
from pathlib import Path

import requests
from rich.console import Console

from lit.core.config import skill_base, load as load_config
from lit.core.zotero import _local_db

console = Console()


def _s2_headers() -> dict[str, str]:
    """Build S2 API headers with optional API key."""
    headers = {}
    try:
        key = load_config().get("semantic_scholar", {}).get("api_key", "")
        if key:
            headers["x-api-key"] = key
    except Exception:
        pass
    return headers


def _load_profile(author_dir: str) -> dict:
    """Load profile.json from people/<author_dir>/profile.json."""
    path = skill_base() / "people" / author_dir / "profile.json"
    if not path.exists():
        raise FileNotFoundError(f"Profile not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _get_zotero_dois() -> set[str]:
    """Get all DOIs currently in Zotero via SQLite copy."""
    conn = _local_db()
    if not conn:
        return set()
    try:
        rows = conn.execute("""
            SELECT LOWER(idv.value) AS doi
            FROM itemData id
            JOIN fields f ON id.fieldID = f.fieldID
            JOIN itemDataValues idv ON id.valueID = idv.valueID
            WHERE f.fieldName = 'DOI'
        """).fetchall()
        return {r["doi"] for r in rows if r["doi"]}
    except Exception:
        return set()
    finally:
        conn.close()


# ── Semantic Scholar ──

def _s2_get_paper_count(author_id: str) -> int | None:
    """Get total paper count from S2 author endpoint (single API call)."""
    url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}?fields=paperCount"
    try:
        resp = requests.get(url, headers=_s2_headers(), timeout=15)
        resp.raise_for_status()
        return resp.json().get("paperCount")
    except Exception as e:
        console.print(f"[red]S2 author API error ({author_id}): {e}[/red]")
        return None


def _s2_fetch_dois(author_id: str, known_count: int | None = None) -> tuple[set[str], int]:
    """Fetch DOIs for an author from Semantic Scholar.

    First run (known_count=None): record paperCount as baseline via author
    endpoint, fetch NOTHING. Avoids pulling back items the user manually
    deleted from Zotero/Scholar.

    Subsequent runs: fetch only papers at offset >= known_count (newly added
    since last check). Returns (dois, total_count).
    """
    # First run: just record the baseline count, don't fetch any papers
    if known_count is None:
        total = _s2_get_paper_count(author_id)
        if total is None:
            return set(), 0
        return set(), total

    # Incremental: fetch only papers beyond the known offset
    dois: set[str] = set()
    limit = 100
    url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"
    offset = known_count
    max_count = known_count

    while True:
        params = {"fields": "externalIds", "limit": limit, "offset": offset}
        try:
            resp = requests.get(url, params=params, headers=_s2_headers(), timeout=15)
            resp.raise_for_status()
        except Exception as e:
            console.print(f"[red]S2 API error (offset={offset}): {e}[/red]")
            break

        data = resp.json()
        papers = data.get("data", [])
        if not papers:
            break

        for p in papers:
            ext = p.get("externalIds", {})
            doi = ext.get("DOI")
            if doi:
                dois.add(doi.lower())

        max_count = offset + len(papers)

        if "next" not in data:
            break
        offset = data["next"]
        time.sleep(0.5)

    return dois, max_count


# ── CrossRef ──

def _normalize_name(s: str) -> str:
    """Normalize a name for comparison: lowercase, strip accents/hyphens/dots/spaces."""
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return "".join(c for c in s if c.isalnum())


def _crossref_fetch_dois(aliases: list[str], since: str) -> set[str]:
    """Fetch DOIs from CrossRef matching author name, created since `since` (YYYY-MM-DD).

    Uses exact full-name matching (normalized) to filter false positives.
    Abbreviated aliases (e.g. "JX", "H.") are skipped — too ambiguous.
    """
    dois: set[str] = set()
    base = "https://api.crossref.org/works"

    for alias in aliases:
        params = {
            "query.author": alias,
            "filter": f"from-created-date:{since}",
            "rows": 50,
            "select": "DOI,author",
        }
        headers = {"User-Agent": "lit-skill/1.0 (mailto:research@example.com)"}
        try:
            resp = requests.get(base, params=params, headers=headers, timeout=15)
            resp.raise_for_status()
        except Exception as e:
            console.print(f"[red]CrossRef error ({alias}): {e}[/red]")
            continue

        items = resp.json().get("message", {}).get("items", [])
        alias_parts = alias.lower().split()
        alias_family = _normalize_name(alias_parts[-1]) if alias_parts else ""
        alias_given = _normalize_name(" ".join(alias_parts[:-1]))

        # Skip abbreviated aliases (e.g. "JX", "H.") — too short for
        # reliable full-name matching against CrossRef fuzzy results.
        if len(alias_given) < 4:
            continue

        for item in items:
            authors = item.get("author", [])
            for a in authors:
                if _normalize_name(a.get("family", "")) == alias_family and \
                   _normalize_name(a.get("given", "")) == alias_given:
                    dois.add(item["DOI"].lower())
                    break

        time.sleep(0.5)

    return dois


# ── S2 ID Discovery (via DOI cross-reference) ──

def discover_s2_ids(author_dir: str, save: bool = False) -> list[dict]:
    """Discover all S2 author IDs for a tracked person via DOI cross-reference.

    Batch-queries S2 paper API with all DOIs from the person's Zotero
    collection, collects all author appearances, then filters by
    surname + given-first-initial match.

    Since the DOI set is already scoped to the person's own papers,
    false-positive rate is near zero — any author with matching surname
    and first initial on multiple papers is almost certainly a duplicate
    S2 profile.

    Args:
        author_dir: Directory name under people/ (e.g. "Ji-Xin_Cheng").
        save: If True, write discovered IDs to profile.json.

    Returns:
        List of dicts: {s2_id, name, count, paper_count, confirmed}.
    """
    from collections import Counter

    profile = _load_profile(author_dir)
    target_name = profile.get("name", "")
    collection = profile.get("zotero_collection", target_name)
    if not target_name:
        console.print("[red]No 'name' field in profile.json[/red]")
        return []

    # Parse surname + given first initial
    norm_target = _normalize_name(target_name)
    # _normalize_name strips everything to alnum lowercase, e.g. "jixincheng"
    # We need the raw parts for surname/initial — re-normalize preserving structure
    import re as _re
    import unicodedata as _ud
    def _norm_preserve(s: str) -> str:
        """Normalize name preserving word boundaries (accents stripped, dashes→space)."""
        s = _ud.normalize("NFKD", s)
        s = "".join(c for c in s if not _ud.combining(c))
        s = _re.sub(r"[\u2010-\u2015\u2212\-]", " ", s)  # all dash variants → space
        return s.strip()

    target_parts = _norm_preserve(target_name).lower().split()
    if len(target_parts) < 2:
        console.print(f"[red]Cannot parse name: {target_name!r}[/red]")
        return []
    surname = target_parts[-1]
    given_first_initial = target_parts[0][0]
    console.print(f"[dim]Target: {target_name} → surname={surname!r}, initial={given_first_initial!r}[/dim]")

    # Get DOIs from Zotero local DB for this collection
    conn = _local_db()
    if not conn:
        console.print("[red]Cannot access Zotero local DB[/red]")
        return []
    try:
        rows = conn.execute("""
            SELECT DISTINCT idv.value
            FROM collectionItems ci
            JOIN collections c ON ci.collectionID = c.collectionID
            JOIN itemData id ON ci.itemID = id.itemID
            JOIN fields f ON id.fieldID = f.fieldID
            JOIN itemDataValues idv ON id.valueID = idv.valueID
            WHERE c.collectionName = ? AND f.fieldName = 'DOI'
        """, (collection,)).fetchall()
    finally:
        conn.close()

    dois = [r[0] if isinstance(r, str) else r["value"] for r in rows]
    if not dois:
        console.print(f"[yellow]No DOIs found in collection '{collection}'[/yellow]")
        return []

    console.print(f"[dim]Zotero collection '{collection}': {len(dois)} DOIs[/dim]")

    # Batch query S2 paper API (500/batch, fields=authors)
    s2_headers = _s2_headers()
    s2_headers["Content-Type"] = "application/json"
    s2_input = [f"DOI:{d}" for d in dois]
    all_papers: list[dict] = []
    found = 0

    for i in range(0, len(s2_input), 500):
        batch = s2_input[i : i + 500]
        try:
            resp = requests.post(
                "https://api.semanticscholar.org/graph/v1/paper/batch",
                params={"fields": "authors"},
                headers=s2_headers,
                json={"ids": batch},
                timeout=60,
            )
            if resp.status_code == 429:
                console.print("[yellow]S2 rate limited, retrying in 5s...[/yellow]")
                time.sleep(5)
                resp = requests.post(
                    "https://api.semanticscholar.org/graph/v1/paper/batch",
                    params={"fields": "authors"},
                    headers=s2_headers,
                    json={"ids": batch},
                    timeout=60,
                )
            if resp.status_code != 200:
                console.print(f"[red]S2 batch API HTTP {resp.status_code}[/red]")
                break
            papers = resp.json()
            all_papers.extend(papers)
            found += sum(1 for p in papers if p)
            console.print(f"[dim]  Batch {i//500+1}: {sum(1 for p in papers if p)}/{len(batch)} found[/dim]")
        except Exception as e:
            console.print(f"[red]S2 batch error: {e}[/red]")
            break
        time.sleep(0.5)

    total_papers = len(all_papers)
    console.print(f"[dim]S2 found {found}/{len(dois)} papers[/dim]")

    # Collect all author appearances
    author_counter: Counter[tuple[str, str]] = Counter()
    for paper in all_papers:
        if not paper:
            continue
        for a in paper.get("authors", []):
            aid = a.get("authorId")
            aname = a.get("name", "")
            if aid and aid != "None":
                author_counter[(aid, aname)] += 1

    # Filter: surname matches + given first initial matches
    candidates: list[dict] = []
    for (aid, aname), count in author_counter.most_common():
        norm_parts = _norm_preserve(aname).lower().split()
        if len(norm_parts) < 2:
            continue
        if norm_parts[-1] != surname:
            continue
        given_initials = [p[0] for p in norm_parts[:-1] if p]
        if not given_initials or given_initials[0] != given_first_initial:
            continue

        # Confirm: if any non-surname word starts with the target's
        # second initial too, it's a stronger match.
        # E.g. target "Ji-Xin" → given_parts = [ji, xin] → check if
        # the name contains a word starting with "x"
        target_given = _norm_preserve(" ".join(target_parts[:-1])).split()
        confirmed = False
        if len(target_given) >= 2:
            second_initial = target_given[1][0]
            for p in norm_parts[:-1]:
                if p.startswith(second_initial):
                    confirmed = True
                    break
        else:
            confirmed = True  # single given name, initial match is enough

        candidates.append({
            "s2_id": aid,
            "name": aname,
            "count": count,
            "confirmed": confirmed,
        })

    if not candidates:
        console.print("[yellow]No matching S2 profiles found.[/yellow]")
        return []

    # Enrich with paper counts from S2 author API
    console.print(f"[dim]Fetching paper counts for {len(candidates)} candidates...[/dim]")
    for c in candidates:
        if c.get("paper_count") is None:
            c["paper_count"] = _s2_get_paper_count(c["s2_id"])
            time.sleep(1.0)

    # Print results
    console.print(f"\n[bold cyan]━━━ S2 Profile Discovery: {target_name} ━━━[/bold cyan]")
    console.print(f"  DOI pool: {len(dois)} papers | S2 matched: {found} | "
                  f"Candidates: {len(candidates)}\n")

    from rich.table import Table
    table = Table(title=f"S2 profiles matching surname={surname!r} + initial={given_first_initial!r}")
    table.add_column("Count", justify="right", style="bold")
    table.add_column("%", justify="right")
    table.add_column("S2 ID", style="cyan")
    table.add_column("Name in S2")
    table.add_column("S2 Papers", justify="right")
    table.add_column("Match", justify="center")

    for c in candidates:
        pct = f"{c['count']/found*100:.1f}%" if found else "?"
        match_label = "[green]✓[/green]" if c["confirmed"] else "[yellow]?[/yellow]"
        table.add_row(
            str(c["count"]),
            pct,
            c["s2_id"],
            c["name"],
            str(c["paper_count"] or "?"),
            match_label,
        )

    console.print(table)

    # Show which ones are new vs already in profile
    existing_ids = set(str(x) for x in profile.get("s2_ids", []))
    new_ids = [c for c in candidates if c["s2_id"] not in existing_ids]
    if new_ids:
        console.print(f"\n[bold yellow]New IDs not in profile.json: {len(new_ids)}[/bold yellow]")
        for c in new_ids:
            console.print(f"  {c['s2_id']}  {c['name']}  ({c['count']} co-authored)")

    if save:
        all_ids = sorted(
            set(list(profile.get("s2_ids", [])) + [c["s2_id"] for c in candidates]),
            key=lambda x: -next((c["count"] for c in candidates if c["s2_id"] == x), 0),
        )
        profile["s2_ids"] = all_ids

        # Update paper counts
        counts = profile.get("s2_paper_counts", {})
        for c in candidates:
            if c["paper_count"] is not None:
                counts[c["s2_id"]] = c["paper_count"]
        profile["s2_paper_counts"] = counts
        profile["s2_paper_count"] = max(counts.values()) if counts else 0

        profile_path = skill_base() / "people" / author_dir / "profile.json"
        with open(profile_path, "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)
        console.print(f"\n[green]✓ Saved {len(all_ids)} S2 IDs to profile.json[/green]")

    return candidates


def find_new_papers(author_dir: str) -> list[dict]:
    """Find papers not yet in Zotero for a tracked author.

    Args:
        author_dir: directory name under people/ (e.g. "Ji-Xin_Cheng")

    Returns:
        List of {"doi": str, "source": str} for new papers.
    """
    profile = _load_profile(author_dir)
    # Support multiple S2 IDs (S2 sometimes has duplicate profiles for the same person)
    s2_ids = profile.get("s2_ids") or (
        [profile["s2_author_id"]] if profile.get("s2_author_id") else []
    )
    aliases = profile.get("aliases", [profile.get("name", "")])

    # Determine "since" date for CrossRef (default: 30 days ago)
    since_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

    # Fetch from both sources
    s2_dois: set[str] = set()
    crossref_dois: set[str] = set()

    if s2_ids:
        known_counts = profile.get("s2_paper_counts", {})
        s2_totals: dict[str, int] = {}
        for s2_id in s2_ids:
            kc = known_counts.get(s2_id)
            is_first_run = kc is None
            console.print(f"[dim]Querying Semantic Scholar (author {s2_id}, "
                          f"{'baseline setup' if is_first_run else f'incremental from {kc}'})...[/dim]")
            dois_i, total_i = _s2_fetch_dois(s2_id, kc)
            console.print(f"  S2 [{s2_id}]: {len(dois_i)} DOIs (total {total_i})")
            s2_dois |= dois_i
            s2_totals[s2_id] = total_i
        profile["s2_paper_counts"] = s2_totals
        # backward-compat aggregate
        profile["s2_paper_count"] = max(s2_totals.values())

    console.print(f"[dim]Querying CrossRef (since {since_date})...[/dim]")
    crossref_dois = _crossref_fetch_dois(aliases, since_date)
    console.print(f"  CrossRef: {len(crossref_dois)} DOIs (after name filter)")

    # Union
    all_remote = s2_dois | crossref_dois
    console.print(f"[dim]Union: {len(all_remote)} unique DOIs[/dim]")

    # Diff with Zotero
    zotero_dois = _get_zotero_dois()
    new_dois = all_remote - zotero_dois
    console.print(f"[dim]In Zotero: {len(zotero_dois)} | New: {len(new_dois)}[/dim]")

    # Tag source
    result = []
    for doi in sorted(new_dois):
        source = []
        if doi in s2_dois:
            source.append("S2")
        if doi in crossref_dois:
            source.append("CrossRef")
        result.append({"doi": doi, "source": "+".join(source)})

    # Update profile timestamps
    profile_path = skill_base() / "people" / author_dir / "profile.json"
    profile["s2_last_check"] = datetime.now().strftime("%Y-%m-%d")
    profile["crossref_last_check"] = datetime.now().strftime("%Y-%m-%d")
    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)

    return result


if __name__ == "__main__":
    import sys

    author = sys.argv[1] if len(sys.argv) > 1 else "Ji-Xin_Cheng"
    new = find_new_papers(author)
    if new:
        print(f"\n{len(new)} new papers:")
        for p in new:
            print(f"  [{p['source']}] {p['doi']}")
    else:
        print("\nNo new papers found.")
