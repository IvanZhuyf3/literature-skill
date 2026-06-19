"""
lit/discover/scholar.py — Google Scholar profile scraping + CrossRef DOI matching + direct Zotero registration.

Removes the intermediate papers.json and ``people/data/`` dependency: all state
lives in Zotero.  ``lit.core`` modules provide config, CrossRef, and Zotero helpers.

CLI entry (from ``lit.cli``):
    lit scholar <URL> [--max-papers N] [--scrape-only]

Public function:
    run(url: str, max_papers: int | None = None, scrape_only: bool = False) -> None
"""

from __future__ import annotations

import logging
import random
import re
import sys
import time
from difflib import SequenceMatcher
from urllib.parse import urlparse, parse_qs

import requests
from rich.console import Console
from rich.table import Table

from lit.core.config import load as get_config, people as get_people_config
from lit.core.crossref import search_by_title
from lit.core.zotero import (
    assign_to_collection,
    check_duplicate,
    create_item,
    find_or_create_collection,
)

logger = logging.getLogger(__name__)
console = Console()


# ---------------------------------------------------------------------------
# Common conference venue keywords to exclude
# ---------------------------------------------------------------------------

CONFERENCE_KEYWORDS = [
    "proceedings", "conference", "symposium", "workshop",
    "SPIE", "CLEO", "OSA", "IEEE Sensors", "IEEE Int",
    "ABCD", "BiOS", "Photonics West", "EOSAM",
    "summit", "forum", "meeting",
    # Journal-name-like conference venues
    "Frontiers in Optics", "Imaging Systems and Applications",
    "Microscopy Histopathology", "Photonic Diagnosis",
    "Advanced Photonics Congress", "Optica Advanced Photonics",
    "European Conferences on Biomedical Optics",
    "microscopy.",  # e.g. "Microscopy. 2024"
    "Fio.", "FM6E", "M1A", "MM1A", "JTU",
    "Advanced Chemical Microscopy",  # SPIE conference
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_scholar_url(url: str) -> str:
    """Extract user ID from a Google Scholar profile URL."""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    user_id = params.get("user", [""])[0]
    if not user_id:
        console.print(f"[red]Could not extract user ID from URL: {url}[/red]")
        sys.exit(1)
    return user_id


def title_similarity(t1: str, t2: str) -> float:
    """Compute title similarity score (0-1) using token overlap."""
    # Normalise
    t1 = re.sub(r"[^\w\s]", "", t1.lower()).strip()
    t2 = re.sub(r"[^\w\s]", "", t2.lower()).strip()
    return SequenceMatcher(None, t1, t2).ratio()


def try_arxiv_match(title: str) -> str:
    """Try to find an arXiv DOI when CrossRef fails.

    Returns arXiv DOI (e.g. ``10.48550/arXiv.2504.12345``) or empty string.
    """
    try:
        resp = requests.get(
            "http://export.arxiv.org/api/query",
            params={
                "search_query": f"ti:{requests.utils.quote(title)}",
                "max_results": 3,
                "sortBy": "relevance",
            },
            headers={"User-Agent": "LiteratureSkill/1.0 (mailto:user@example.com)"},
            timeout=15,
        )
        if resp.status_code != 200:
            return ""

        import xml.etree.ElementTree as ET
        root = ET.fromstring(resp.text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        for entry in root.findall(".//atom:entry", ns):
            entry_title_el = entry.find("atom:title", ns)
            if entry_title_el is None:
                continue
            entry_title = re.sub(r"\s+", " ", entry_title_el.text or "").strip()

            sim = title_similarity(title, entry_title)
            if sim >= 0.75:
                entry_id_el = entry.find("atom:id", ns)
                if entry_id_el is not None and entry_id_el.text:
                    arxiv_url = entry_id_el.text.strip()
                    m = re.search(r"arxiv\.org/abs/(.+?)(v\d+)?$", arxiv_url, re.IGNORECASE)
                    if m:
                        arxiv_id = m.group(1).rstrip("v0123456789")
                        arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
                        return f"10.48550/arXiv.{arxiv_id}"
        return ""
    except Exception:
        return ""


def deduplicate_papers(papers: list[dict]) -> tuple[list[dict], int]:
    """Detect preprint/published pairs and keep the published version.

    Heuristics:
    - Same title (fuzzy match ≥ 0.85) + one is preprint → keep the other
    - Both same type → keep higher citation count
    """
    PREPRINT_VENUES = {"biorxiv", "arxiv", "chemrxiv", "medrxiv", "preprint"}

    result: list[dict] = []
    removed: set[int] = set()

    for i, p1 in enumerate(papers):
        if i in removed:
            continue
        for j in range(i + 1, len(papers)):
            if j in removed:
                continue
            p2 = papers[j]
            sim = title_similarity(p1["title"], p2["title"])
            if sim < 0.85:
                continue

            v1 = p1.get("venue", "").lower()
            v2 = p2.get("venue", "").lower()
            p1_preprint = any(pr in v1 for pr in PREPRINT_VENUES)
            p2_preprint = any(pr in v2 for pr in PREPRINT_VENUES)

            if p1_preprint and not p2_preprint:
                removed.add(i)
                break
            elif p2_preprint and not p1_preprint:
                removed.add(j)
                continue
            else:
                # Both preprint or both published — keep higher citations
                if p1.get("citations", 0) >= p2.get("citations", 0):
                    removed.add(j)
                else:
                    removed.add(i)
                    break

    for i, p in enumerate(papers):
        if i not in removed:
            result.append(p)

    return result, len(removed)


def filter_papers(papers: list[dict], cfg: dict) -> list[dict]:
    """Filter out patents and conference proceedings."""
    pcfg = get_people_config()
    exclude_types = set(pcfg.get("exclude_types", []))
    exclude_venues = pcfg.get("exclude_venues", [])
    all_exclude_venues = set(CONFERENCE_KEYWORDS + (exclude_venues or []))

    filtered: list[dict] = []
    excluded_count = {"patent": 0, "conference": 0, "empty": 0}

    for paper in papers:
        title = paper.get("title", "").lower()
        venue = paper.get("venue", "")
        venue_lower = venue.lower()

        # Skip empty titles
        if not title:
            excluded_count["empty"] += 1
            continue

        # Check for patent
        if "patent" in title or "patent" in venue_lower:
            paper["type"] = "patent"
            if "Patent" in exclude_types:
                excluded_count["patent"] += 1
                continue

        # Check for conference venues
        is_conference = any(kw.lower() in venue_lower for kw in all_exclude_venues)
        if is_conference:
            paper["type"] = "conference"
            excluded_count["conference"] += 1
            continue

        filtered.append(paper)

    if any(excluded_count.values()):
        console.print(f"  [dim]Excluded: {excluded_count}[/dim]")

    # Deduplicate preprint/published pairs
    deduped, dup_count = deduplicate_papers(filtered)
    if dup_count:
        console.print(f"  [dim]Deduplicated: {dup_count} preprint/published pair(s) resolved[/dim]")

    return deduped


# ---------------------------------------------------------------------------
# Phase 1: Scholar Profile Scraping
# ---------------------------------------------------------------------------

def scrape_scholar_profile(
    url: str,
    cfg: dict,
    max_papers: int | None = None,
) -> tuple[list[dict], str]:
    """Use Playwright CDP to scrape a Google Scholar Profile page.

    Args:
        url: Full Google Scholar profile URL (e.g.
             ``https://scholar.google.com/citations?user=XXXX``).
        cfg: Full config dict (from ``lit.core.config.load()``).
        max_papers: Optional limit on the number of papers to return.

    Returns:
        ``(papers, scholar_name)`` where each paper dict has keys:
        ``title``, ``authors``, ``venue``, ``year``, ``citations``,
        ``scholar_paper_id``, ``doi``, ``type``.
    """
    from chromium_helper import ChromiumHelper

    scfg = get_people_config()["scholar"]
    page_delay = scfg["page_delay"]
    max_show_more = scfg["max_show_more"]

    helper = ChromiumHelper(cfg)

    console.print(f"\n[bold cyan]━━━ Phase 1: Scholar Profile 抓取 ━━━[/bold cyan]\n")
    console.print(f"  URL: {url}")

    # Connect to Chrome via CDP
    pw_browser = helper.connect()
    if not pw_browser:
        console.print("[red]Failed to connect to Chrome via CDP.[/red]")
        console.print("[dim]Make sure Chrome is running with --remote-debugging-port=19222[/dim]")
        sys.exit(1)

    pw, browser = pw_browser
    page, ctx = helper.get_or_create_page(browser)

    try:
        # Navigate to Scholar profile
        console.print("  Navigating to Scholar profile...")
        page.goto(url, wait_until="networkidle", timeout=30000)
        time.sleep(3)

        # Get scholar name
        try:
            name_el = page.query_selector("#gsc_prf_in")
            scholar_name = name_el.inner_text().strip() if name_el else "Unknown"
        except Exception:
            scholar_name = "Unknown"
        console.print(f"  Scholar: [bold green]{scholar_name}[/bold green]")

        # Click "Show More" repeatedly to load all papers
        console.print("  Loading papers (clicking Show More)...")
        click_count = 0
        prev_count = 0

        while click_count < max_show_more:
            # Count current papers
            rows = page.query_selector_all("#gsc_a_b .gsc_a_t")
            curr_count = len(rows)

            if max_papers and curr_count >= max_papers:
                console.print(f"  Reached max_papers limit ({max_papers}), stopping.")
                break

            if curr_count == prev_count:
                pass  # no new papers loaded, try clicking once more

            # Find and click "Show More" button
            show_more = page.query_selector("#gsc_bpf_more")
            if not show_more:
                console.print("  No 'Show More' button found, all papers loaded.")
                break

            # Check if button is disabled
            is_disabled = show_more.get_attribute("disabled")
            if is_disabled is not None:
                console.print("  'Show More' button disabled, all papers loaded.")
                break

            show_more.click()
            click_count += 1
            prev_count = curr_count
            time.sleep(page_delay / 1000)

            if click_count % 5 == 0:
                console.print(f"    ... loaded ~{curr_count} papers ({click_count} clicks)")

        # Parse all paper rows
        console.print("  Parsing paper entries...")
        papers = _parse_paper_rows(page)

        # Sort by year (newest first by default, Scholar shows this way)
        console.print(f"  Found [bold]{len(papers)}[/bold] papers total (before filtering)")

        # Filter
        papers = filter_papers(papers, cfg)
        console.print(f"  After filtering: [bold]{len(papers)}[/bold] papers")

        if max_papers:
            papers = papers[:max_papers]
            console.print(f"  Limited to {max_papers} papers")

        # Sort by year ascending (oldest first for chronological reading)
        papers.sort(key=lambda p: p.get("year", 9999))

        return papers, scholar_name

    finally:
        helper.disconnect()


def _parse_paper_rows(page) -> list[dict]:
    """Parse paper entries from the Scholar profile table."""
    papers: list[dict] = []
    rows = page.query_selector_all("#gsc_a_b .gsc_a_tr")

    for row in rows:
        try:
            # Title
            title_el = row.query_selector(".gsc_a_at")
            title = title_el.inner_text().strip() if title_el else ""

            # Authors and venue from gray divs
            gray_divs = row.query_selector_all(".gs_gray")

            authors = ""
            venue = ""

            if len(gray_divs) >= 1:
                authors = gray_divs[0].inner_text().strip()
            if len(gray_divs) >= 2:
                venue_raw = gray_divs[1].inner_text().strip()
                # Remove ", YYYY" at the end (from gs_oph span)
                venue = re.sub(r",\s*\d{4}\s*$", "", venue_raw).strip()

            # Year (separate column — more reliable)
            year_el = row.query_selector("td.gsc_a_y span")
            year_text = year_el.inner_text().strip() if year_el else ""
            year = 0
            try:
                year = int(year_text)
            except Exception:
                pass

            # Citations
            cite_el = row.query_selector(".gsc_a_c a")
            cite_text = cite_el.inner_text().strip() if cite_el else "0"
            try:
                citations = int(cite_text)
            except Exception:
                citations = 0

            # Scholar paper ID from the href
            scholar_paper_id = ""
            if title_el:
                href = title_el.get_attribute("href") or ""
                if "citation?" in href:
                    m = re.search(r"citations?view_op=view_citation.*?citation_for=([^&]+)", href)
                    if m:
                        scholar_paper_id = m.group(1)

            papers.append({
                "title": title,
                "authors": authors,
                "venue": venue,
                "year": year,
                "citations": citations,
                "scholar_paper_id": scholar_paper_id,
                "doi": "",       # Will be filled by CrossRef
                "type": "journal",  # Will be refined by filtering
            })

        except Exception as e:
            console.print(f"[yellow]  Warning: Failed to parse a row: {e}[/yellow]")
            continue

    return papers


# ---------------------------------------------------------------------------
# Phase 1b: CrossRef DOI matching
# ---------------------------------------------------------------------------

def match_dois(papers: list[dict], cfg: dict) -> list[dict]:
    """Match each paper to a DOI via CrossRef title search.

    Uses ``lit.core.crossref.search_by_title()`` for each paper, with arXiv
    fallback for unmatched preprints.

    Args:
        papers: List of paper dicts (as returned by ``scrape_scholar_profile``).
        cfg: Full config dict.

    Returns:
        Updated paper list with ``doi``, ``doi_status``, and optionally
        ``doi_score`` fields.
    """
    scfg = get_people_config()["scholar"]
    min_delay = scfg["min_delay"]
    max_delay = scfg["max_delay"]

    console.print(f"\n[bold cyan]━━━ CrossRef DOI 匹配 ━━━[/bold cyan]\n")

    matched = 0
    unmatched = 0

    for i, paper in enumerate(papers):
        title = paper.get("title", "")
        if not title:
            paper["doi_status"] = "no_title"
            unmatched += 1
            continue

        console.print(f"  [{i + 1}/{len(papers)}] {title[:70]}...")

        try:
            result = search_by_title(title)
            if result and result.get("doi"):
                paper["doi"] = result["doi"]
                paper["doi_status"] = "matched"
                paper["doi_score"] = 1.0  # best match from search_by_title

                # Enrich metadata from CrossRef
                if result.get("journal"):
                    paper["venue"] = result["journal"]
                if result.get("year"):
                    paper["year"] = int(result["year"]) if result["year"].isdigit() else paper["year"]

                matched += 1
                console.print(f"    [green]✓ DOI: {paper['doi']}[/green]")
            else:
                # Fallback: try arXiv API
                arxiv_doi = try_arxiv_match(title)
                if arxiv_doi:
                    paper["doi"] = arxiv_doi
                    paper["doi_status"] = "matched_arxiv"
                    matched += 1
                    console.print(f"    [green]✓ arXiv DOI: {arxiv_doi}[/green]")
                else:
                    paper["doi_status"] = "no_match"
                    unmatched += 1
                    console.print(f"    [yellow]⊘ No DOI match[/yellow]")

        except Exception as e:
            paper["doi_status"] = "error"
            paper["doi_error"] = str(e)[:200]
            unmatched += 1
            console.print(f"    [red]✗ Error: {e}[/red]")

        # Polite rate limit between CrossRef API calls
        time.sleep(random.uniform(min_delay / 3, max_delay / 3))

    console.print(f"\n  Matched: [green]{matched}[/green], Unmatched: [yellow]{unmatched}[/yellow]")
    return papers


# ---------------------------------------------------------------------------
# Phase 2: Zotero Registration (direct, no intermediate JSON)
# ---------------------------------------------------------------------------

def register_papers(papers: list[dict], scholar_name: str, cfg: dict) -> list[dict]:
    """Register DOI-matched papers as Zotero items directly.

    Skips papers that already have a ``zotero_key``.  Uses CrossRef metadata
    via ``lit.core.zotero.create_item()``.  Papers without a DOI are skipped
    silently.

    Args:
        papers: List of paper dicts (may already have ``zotero_key`` from a
                previous run).
        scholar_name: Name displayed in Zotero collection (``People/<name>``).
        cfg: Full config dict.

    Returns:
        Updated paper list with ``zotero_key`` and ``zotero_status`` fields
        populated for processed papers.
    """
    console.print(f"\n[bold cyan]━━━ Zotero 批量注册 ({len(papers)} 篇) ━━━[/bold cyan]\n")

    # Find or create the Zotero collection
    collection_key = find_or_create_collection(scholar_name, parent_name="People")
    console.print(f"  Collection: [bold]{scholar_name}[/bold] (key: {collection_key})\n")

    # Determine which papers actually need registration
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

    for i, paper in enumerate(to_register):
        title = paper.get("title", "")[:70]
        doi = paper.get("doi", "")
        console.print(f"\n  [{i + 1}/{len(to_register)}] {title}")

        try:
            # Check for duplicates in Zotero before creating
            existing_key, match_reason = check_duplicate(doi=doi, title=paper.get("title", ""))
            if existing_key:
                paper["zotero_key"] = existing_key
                paper["zotero_status"] = "already_exists"
                console.print(f"    [dim]Already exists: {existing_key} ({match_reason})[/dim]")
            else:
                # Build metadata dict for create_item
                author_str = paper.get("authors", "")
                authors: list[str] = []
                if author_str:
                    raw = [a.strip() for a in author_str.split(",")]
                    authors = [a for a in raw if a and a != "..." and len(a) > 1]

                meta = {
                    "DOI": doi,
                    "title": paper.get("title", ""),
                    "url": f"https://doi.org/{doi}",
                    "journal": paper.get("venue", ""),
                    "year": str(paper.get("year", "")),
                    "authors": authors,
                }

                item_key = create_item(meta)
                paper["zotero_key"] = item_key
                paper["zotero_status"] = "registered"
                console.print(f"    [green]✓ {item_key}[/green]")

            # Assign to the scholar collection (idempotent)
            assign_to_collection(paper["zotero_key"], collection_key)

        except Exception as e:
            paper["zotero_status"] = "failed"
            paper["zotero_error"] = str(e)[:200]
            console.print(f"    [red]✗ {str(e)[:80]}[/red]")

    registered = sum(1 for p in papers if p.get("zotero_key"))
    failed = sum(1 for p in papers if p.get("zotero_status") == "failed")
    console.print(f"\n  [bold green]Done: {registered} registered, {failed} failed[/bold green]")

    return papers


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_summary(papers: list[dict], scholar_name: str) -> None:
    """Print a summary table of scraped (and optionally DOI-matched) papers."""
    table = Table(title=f"\n{scholar_name} — 论文列表 ({len(papers)} 篇)")
    table.add_column("#", style="dim", width=4)
    table.add_column("Year", width=6)
    table.add_column("Title", ratio=3)
    table.add_column("Venue", ratio=1.5)
    table.add_column("Cites", justify="right", width=6)
    table.add_column("DOI", width=15)
    table.add_column("Status", width=10)

    for i, p in enumerate(papers):
        doi_full = p.get("doi", "")
        doi_short = f"{doi_full[:20]}..." if len(doi_full) > 20 else doi_full
        status = p.get("doi_status", "")
        status_color = {"matched": "green", "matched_arxiv": "green",
                        "no_match": "yellow", "no_title": "red"}.get(status, "red")

        zot_status = p.get("zotero_status", "")
        if zot_status:
            display_status = zot_status
            if zot_status == "registered":
                display_status = "[green]registered[/green]"
        else:
            display_status = f"[{status_color}]{status}[/{status_color}]" if status else ""

        table.add_row(
            str(i + 1),
            str(p.get("year", "?")),
            p.get("title", "?")[:60],
            p.get("venue", "?")[:30],
            str(p.get("citations", 0)),
            doi_short,
            display_status,
        )

    console.print(table)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def run(
    url: str,
    max_papers: int | None = None,
    scrape_only: bool = False,
) -> None:
    """Scrape a Google Scholar profile, match DOIs, and optionally register
    papers directly to Zotero — no intermediate ``papers.json`` file.

    Args:
        url: Full Google Scholar profile URL.
        max_papers: Limit number of papers to process (for testing).
        scrape_only: If True, only scrape and match DOIs — do NOT register
                     to Zotero.
    """
    cfg = get_config()

    # Phase 1: Scrape
    papers, scholar_name = scrape_scholar_profile(url, cfg, max_papers=max_papers)

    # Phase 1b: DOI matching
    papers = match_dois(papers, cfg)

    # Report
    print_summary(papers, scholar_name)

    # Phase 2: Register to Zotero (unless scrape-only)
    if not scrape_only:
        papers = register_papers(papers, scholar_name, cfg)
        # Final summary with Zotero status
        print_summary(papers, scholar_name)
    else:
        console.print(f"\n[bold yellow]--scrape-only mode: Zotero registration skipped.[/bold yellow]")

    console.print(f"\n[bold green]✓ Done![/bold green] {len(papers)} papers processed.\n")
