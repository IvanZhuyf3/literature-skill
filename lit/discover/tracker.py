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

def _crossref_fetch_dois(aliases: list[str], since: str) -> set[str]:
    """Fetch DOIs from CrossRef matching author name, created since `since` (YYYY-MM-DD).

    Only fetches the first page per alias (sorted by relevance).
    Filters false positives by checking author list.
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
        alias_lower = alias.lower()
        alias_parts = alias_lower.split()
        alias_family = alias_parts[-1] if alias_parts else ""

        for item in items:
            authors = item.get("author", [])
            for a in authors:
                family = a.get("family", "").lower()
                given = a.get("given", "").lower()
                if family == alias_family:
                    given_initials = [w[0] for w in given.split() if w]
                    alias_initials = [w[0] for w in alias_parts[:-1] if w]
                    if any(ai in given_initials for ai in alias_initials):
                        dois.add(item["DOI"].lower())
                        break

        time.sleep(0.5)

    return dois


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
