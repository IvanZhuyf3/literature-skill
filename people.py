"""
people.py — Scholar Profile → Zotero → 文献消化

Usage:
    set PYTHONIOENCODING=utf-8 && python people.py "https://scholar.google.com/citations?user=XXXX"
    python people.py "URL" --scrape-only       # 只抓取论文列表
    python people.py "URL" --max-papers 5       # 限制篇数（测试用）
    python people.py "URL" --dry-run            # 只打印，不执行
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import random
import logging
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import requests
import yaml
from rich.console import Console
from rich.table import Table

SKILL_BASE = Path(__file__).resolve().parent
CONFIG_PATH = SKILL_BASE / "config.yaml"
DATA_DIR = SKILL_BASE / "people" / "data"
DIGEST_DIR = SKILL_BASE / "people" / "digests"

console = Console()


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def load_config() -> dict:
    if not CONFIG_PATH.exists():
        console.print("[red]config.yaml not found.[/red]")
        sys.exit(1)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_people_config(cfg: dict) -> dict:
    """Get people-specific config with defaults."""
    defaults = {
        "parent_collection": "People",
        "exclude_types": ["Patent"],
        "exclude_venues": [],  # 会议关键词，默认排空但实际会排常见会议
        "scholar": {
            "page_delay": 3000,
            "max_show_more": 50,
            "min_delay": 5,
            "max_delay": 15,
        },
        "digest_dir": str(DIGEST_DIR),
    }
    user_cfg = cfg.get("people", {})
    # Deep merge: scholar sub-dict
    for key in defaults:
        if key not in user_cfg:
            user_cfg[key] = defaults[key]
    if "scholar" not in user_cfg:
        user_cfg["scholar"] = {}
    for key in defaults["scholar"]:
        if key not in user_cfg["scholar"]:
            user_cfg["scholar"][key] = defaults["scholar"][key]
    return user_cfg


# ---------------------------------------------------------------------------
# Common conference venue keywords to exclude by default
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
# Phase 1: Scholar Profile Scraping
# ---------------------------------------------------------------------------

def parse_scholar_url(url: str) -> str:
    """Extract user ID from Scholar URL."""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    user_id = params.get("user", [""])[0]
    if not user_id:
        console.print(f"[red]Could not extract user ID from URL: {url}[/red]")
        sys.exit(1)
    return user_id


def scrape_scholar_profile(url: str, cfg: dict, max_papers: int | None = None) -> list[dict]:
    """
    Use Playwright CDP to scrape a Google Scholar Profile page.
    
    Returns list of papers:
        {title, authors, venue, year, citations, scholar_id}
    """
    from chromium_helper import ChromiumHelper
    
    scfg = get_people_config(cfg)["scholar"]
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
        console.print(f"  Navigating to Scholar profile...")
        page.goto(url, wait_until="networkidle", timeout=30000)
        time.sleep(3)
        
        # Get scholar name
        try:
            name_el = page.query_selector("#gsc_prf_in")
            scholar_name = name_el.inner_text().strip() if name_el else "Unknown"
        except:
            scholar_name = "Unknown"
        console.print(f"  Scholar: [bold green]{scholar_name}[/bold green]")
        
        # Click "Show More" repeatedly to load all papers
        console.print(f"  Loading papers (clicking Show More)...")
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
                # No new papers loaded, try clicking once more
                pass
            
            # Find and click "Show More" button
            show_more = page.query_selector("#gsc_bpf_more")
            if not show_more:
                console.print(f"  No 'Show More' button found, all papers loaded.")
                break
            
            # Check if button is disabled
            is_disabled = show_more.get_attribute("disabled")
            if is_disabled is not None:
                console.print(f"  'Show More' button disabled, all papers loaded.")
                break
            
            show_more.click()
            click_count += 1
            prev_count = curr_count
            time.sleep(page_delay / 1000)
            
            if click_count % 5 == 0:
                console.print(f"    ... loaded ~{curr_count} papers ({click_count} clicks)")
        
        # Parse all paper rows
        console.print(f"  Parsing paper entries...")
        papers = parse_paper_rows(page, scholar_name)
        
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


def parse_paper_rows(page, scholar_name: str) -> list[dict]:
    """Parse paper entries from the Scholar profile table."""
    papers = []
    rows = page.query_selector_all("#gsc_a_b .gsc_a_tr")
    
    for row in rows:
        try:
            # Title
            title_el = row.query_selector(".gsc_a_at")
            title = title_el.inner_text().strip() if title_el else ""
            
            # Google Scholar DOM structure:
            # <td class="gsc_a_t">
            #   <a class="gsc_a_at">Title</a>
            #   <div class="gs_gray">Authors</div>
            #   <div class="gs_gray">Venue vol (issue)<span class="gs_oph">, Year</span></div>
            # </td>
            gray_divs = row.query_selector_all(".gs_gray")
            
            authors = ""
            venue = ""
            
            if len(gray_divs) >= 1:
                authors = gray_divs[0].inner_text().strip()
            if len(gray_divs) >= 2:
                # Venue div contains "Venue info, Year" — strip the year span
                venue_raw = gray_divs[1].inner_text().strip()
                # Remove ", YYYY" at the end (from gs_oph span)
                venue = re.sub(r",\s*\d{4}\s*$", "", venue_raw).strip()
            
            # Year (separate column — more reliable)
            year_el = row.query_selector("td.gsc_a_y span")
            year_text = year_el.inner_text().strip() if year_el else ""
            year = 0
            try:
                year = int(year_text)
            except:
                pass
            
            # Citations
            cite_el = row.query_selector(".gsc_a_c a")
            cite_text = cite_el.inner_text().strip() if cite_el else "0"
            try:
                citations = int(cite_text)
            except:
                citations = 0
            
            # Scholar link for this paper
            href = title_el.get_attribute("href") if title_el else ""
            scholar_paper_id = ""
            if href and "citation?" in href:
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
                "doi": "",  # Will be filled by CrossRef
                "type": "journal",  # Will be refined by filtering
            })
            
        except Exception as e:
            console.print(f"[yellow]  Warning: Failed to parse a row: {e}[/yellow]")
            continue
    
    return papers


def filter_papers(papers: list[dict], cfg: dict) -> list[dict]:
    """Filter out patents and conference papers."""
    pcfg = get_people_config(cfg)
    exclude_types = set(pcfg.get("exclude_types", []))
    exclude_venues = pcfg.get("exclude_venues", [])
    
    # Combine default conference keywords with user config
    all_exclude_venues = set(CONFERENCE_KEYWORDS + (exclude_venues or []))
    
    filtered = []
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
        is_conference = False
        for kw in all_exclude_venues:
            if kw.lower() in venue_lower:
                is_conference = True
                break
        
        if is_conference:
            paper["type"] = "conference"
            excluded_count["conference"] += 1
            continue
        
        filtered.append(paper)
    
    if any(excluded_count.values()):
        console.print(f"  [dim]Excluded: {excluded_count}[/dim]")
    
    # Deduplicate: preprint vs published version
    deduped, dup_count = deduplicate_papers(filtered)
    if dup_count:
        console.print(f"  [dim]Deduplicated: {dup_count} preprint/published pair(s) resolved[/dim]")
    
    return deduped


def deduplicate_papers(papers: list[dict]) -> tuple[list[dict], int]:
    """Detect preprint/published pairs and keep the published version.
    
    Heuristics:
    - Same title (fuzzy match) + one is preprint (bioRxiv/arXiv) → keep the other
    - Same DOI → keep the one with higher citations or earlier year
    """
    PREPRINT_VENUES = {"biorxiv", "arxiv", "chemrxiv", "medrxiv", "preprint"}
    
    result = []
    removed = set()
    
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
            
            # Same title — determine which to keep
            v1 = p1.get("venue", "").lower()
            v2 = p2.get("venue", "").lower()
            p1_preprint = any(pr in v1 for pr in PREPRINT_VENUES)
            p2_preprint = any(pr in v2 for pr in PREPRINT_VENUES)
            
            if p1_preprint and not p2_preprint:
                removed.add(i)
                break  # p1 removed, p2 kept
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


# ---------------------------------------------------------------------------
# Phase 1b: CrossRef DOI matching
# ---------------------------------------------------------------------------

def match_dois(papers: list[dict], cfg: dict) -> list[dict]:
    """Match each paper to a DOI via CrossRef bibliographic search."""
    console.print(f"\n[bold cyan]━━━ CrossRef DOI 匹配 ━━━[/bold cyan]\n")
    
    scfg = get_people_config(cfg)["scholar"]
    min_delay = scfg["min_delay"]
    max_delay = scfg["max_delay"]
    
    matched = 0
    unmatched = 0
    
    for i, paper in enumerate(papers):
        title = paper.get("title", "")
        if not title:
            paper["doi_status"] = "no_title"
            unmatched += 1
            continue
        
        console.print(f"  [{i+1}/{len(papers)}] {title[:70]}...")
        
        try:
            resp = requests.get(
                "https://api.crossref.org/works",
                params={
                    "query.bibliographic": title,
                    "rows": 3,
                    "select": "DOI,title,author,container-title,published,score,type",
                },
                headers={"User-Agent": "ZotTool/1.0 (mailto:zot@localhost)"},
                timeout=15,
            )
            
            if resp.status_code != 200:
                paper["doi_status"] = "crossref_error"
                unmatched += 1
                continue
            
            data = resp.json()
            items = data.get("message", {}).get("items", [])
            
            if not items:
                paper["doi_status"] = "no_match"
                unmatched += 1
                continue
            
            # Find best match by title similarity
            # Skip supplementary material DOIs (e.g. .s001, .s002)
            best = None
            best_score = 0
            for item in items:
                item_doi = item.get("DOI", "")
                # Skip supplementary material
                if re.search(r"\.s\d{3}$", item_doi, re.IGNORECASE):
                    continue
                
                item_title = item.get("title", [""])[0] if item.get("title") else ""
                sim = title_similarity(title, item_title)
                
                # Prefer journal articles over preprints
                item_type = item.get("type", "")
                if item_type in ("posted-content", "report"):
                    sim *= 0.95  # Slight penalty for preprints
                
                if sim > best_score:
                    best_score = sim
                    best = item
            
            if best and best_score >= 0.7:
                paper["doi"] = best.get("DOI", "")
                paper["doi_status"] = "matched"
                paper["doi_score"] = round(best_score, 3)
                
                # Enrich metadata from CrossRef
                if best.get("container-title"):
                    paper["venue"] = best["container-title"][0]
                if best.get("published", {}).get("date-parts", [[]])[0]:
                    paper["year"] = best["published"]["date-parts"][0][0]
                
                matched += 1
                console.print(f"    [green]✓ DOI: {paper['doi']} (score: {best_score:.2f})[/green]")
            else:
                # Fallback: try arXiv API for preprints
                arxiv_doi = try_arxiv_match(title, paper.get("venue", ""))
                if arxiv_doi:
                    paper["doi"] = arxiv_doi
                    paper["doi_status"] = "matched_arxiv"
                    paper["doi_score"] = round(best_score, 3)
                    matched += 1
                    console.print(f"    [green]✓ arXiv DOI: {arxiv_doi}[/green]")
                else:
                    paper["doi_status"] = "low_score"
                    paper["doi_score"] = round(best_score, 3)
                    unmatched += 1
                    console.print(f"    [yellow]⊘ Low match score: {best_score:.2f}[/yellow]")
        
        except Exception as e:
            paper["doi_status"] = "error"
            paper["doi_error"] = str(e)
            unmatched += 1
            console.print(f"    [red]✗ Error: {e}[/red]")
        
        # Rate limit
        time.sleep(random.uniform(min_delay / 3, max_delay / 3))
    
    console.print(f"\n  Matched: [green]{matched}[/green], Unmatched: [yellow]{unmatched}[/yellow]")
    return papers


def try_arxiv_match(title: str, venue: str) -> str:
    """Try to find arXiv DOI via arXiv API when CrossRef fails.
    
    Returns arXiv DOI (e.g. '10.48550/arXiv.2504.12345') or empty string.
    """
    # Only try if venue suggests arXiv, or always try as fallback
    try:
        # arXiv API search
        resp = requests.get(
            "http://export.arxiv.org/api/query",
            params={
                "search_query": f"ti:{requests.utils.quote(title)}",
                "max_results": 3,
                "sortBy": "relevance",
            },
            headers={"User-Agent": "ZotTool/1.0 (mailto:zot@localhost)"},
            timeout=15,
        )
        if resp.status_code != 200:
            return ""
        
        # Parse Atom XML
        import xml.etree.ElementTree as ET
        root = ET.fromstring(resp.text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        
        for entry in root.findall(".//atom:entry", ns):
            entry_title = entry.find("atom:title", ns)
            if entry_title is None:
                continue
            entry_title_text = re.sub(r"\s+", " ", entry_title.text or "").strip()
            
            sim = title_similarity(title, entry_title_text)
            if sim >= 0.75:
                # Extract arXiv ID from the entry URL
                entry_id = entry.find("atom:id", ns)
                if entry_id is not None and entry_id.text:
                    # URL format: http://arxiv.org/abs/2504.12345v1
                    arxiv_url = entry_id.text.strip()
                    m = re.search(r"arxiv\.org/abs/(.+?)(v\d+)?$", arxiv_url, re.IGNORECASE)
                    if m:
                        arxiv_id = m.group(1).rstrip("v0123456789")
                        arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
                        return f"10.48550/arXiv.{arxiv_id}"
        
        return ""
    except Exception:
        return ""


def title_similarity(t1: str, t2: str) -> float:
    """Compute title similarity score (0-1) using token overlap."""
    from difflib import SequenceMatcher
    
    # Normalize
    t1 = re.sub(r"[^\w\s]", "", t1.lower()).strip()
    t2 = re.sub(r"[^\w\s]", "", t2.lower()).strip()
    
    # SequenceMatcher ratio
    return SequenceMatcher(None, t1, t2).ratio()


# ---------------------------------------------------------------------------
# Phase 1c: Author Database (corresponding authors only)
# ---------------------------------------------------------------------------

AUTHORS_DB_PATH = SKILL_BASE / "people" / "data" / "authors_db.json"


def load_authors_db() -> dict:
    """Load the persistent author database."""
    if AUTHORS_DB_PATH.exists():
        with open(AUTHORS_DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"authors": {}}


def save_authors_db(db: dict):
    """Save the author database."""
    AUTHORS_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(AUTHORS_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)


def _normalize_abbrev(name: str) -> str:
    """Normalize an author name for matching (lowercase, strip dots/spaces/dashes)."""
    # Replace all unicode dash variants with ASCII hyphen, then strip
    name = name.replace("\u2010", "-").replace("\u2011", "-").replace("\u2012", "-")
    name = name.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    return re.sub(r"[\.\s\-]+", "", name).lower()


def fetch_crossref_authors(doi: str) -> list[dict] | None:
    """Fetch full author list from CrossRef by DOI.

    Returns list of {given, family, affiliations, sequence} or None on failure.
    sequence is 'first' (first author) or 'additional'.
    Corresponding author is identified by 'corresponding' in sequence or
    by matching the last author (heuristic).
    """
    try:
        r = requests.get(
            f"https://api.crossref.org/works/{doi}",
            headers={"User-Agent": "lit-skill/1.0 (mailto:noreply@example.com)"},
            timeout=15,
        )
        if not r.ok:
            return None
        msg = r.json().get("message", {})
        authors = []
        for a in msg.get("author", []):
            given = a.get("given", "")
            family = a.get("family", "")
            affils = [af.get("name", "") for af in a.get("affiliation", []) if af.get("name")]
            seq = a.get("sequence", "")
            # CrossRef sometimes marks corresponding author
            if a.get("corresponding"):
                seq = "corresponding"
            authors.append({
                "given": given,
                "family": family,
                "full_name": f"{given} {family}".strip(),
                "affiliations": affils,
                "sequence": seq,
            })
        return authors if authors else None
    except Exception:
        return None


def _identify_corresponding(authors: list[dict], doi: str) -> list[dict]:
    """Identify corresponding author(s) from a CrossRef author list.

    Priority:
    1. sequence == 'corresponding'
    2. Last author (heuristic: senior/corresponding in many fields)
    """
    corr = [a for a in authors if a.get("sequence") == "corresponding"]
    if corr:
        return corr
    # Heuristic: last author is corresponding in life sciences / chemistry
    if authors:
        return [authors[-1]]
    return []


def update_authors_from_doi(doi: str, db: dict) -> dict:
    """Fetch CrossRef author data for a DOI and update the DB.

    Only corresponding authors are stored. Returns the updated db.
    """
    authors = fetch_crossref_authors(doi)
    if not authors:
        return db

    corresponding = _identify_corresponding(authors, doi)
    all_names = [a["full_name"] for a in authors]

    for ca in corresponding:
        full = ca["full_name"]
        if not full or len(full) < 3:
            continue

        # Generate abbreviation: initials + family
        # Handle hyphenated names: "Man-Chung" → "MC" not "M"
        parts = full.split()
        if len(parts) >= 2:
            given_parts = parts[:-1]
            family = parts[-1]
            # Split hyphenated given name parts for initials
            initials = ""
            for gp in given_parts:
                for sub in re.split(r"[-‐–—]", gp):
                    if sub and sub[0].isalpha():
                        initials += sub[0]
            abbrev = f"{initials} {family}"
            # Also add variant with no dash expansion (e.g. "KM" for "Keith Man-Chung")
            simple_initials = "".join(gp[0] for gp in given_parts if gp and gp[0].isalpha())
            abbrevs = [abbrev]
            if simple_initials != initials:
                abbrevs.append(f"{simple_initials} {family}")
        else:
            abbrevs = [full]

        key = _normalize_abbrev(full)

        if key not in db["authors"]:
            db["authors"][key] = {
                "full_name": full,
                "abbreviations": list(abbrevs),
                "affiliations": ca.get("affiliations", []),
                "papers_as_corresponding": [],
                "papers_as_coauthor": [],
                "dirty": False,
                "last_updated": time.strftime("%Y-%m-%d"),
            }
        else:
            entry = db["authors"][key]
            for ab in abbrevs:
                if ab not in entry["abbreviations"]:
                    entry["abbreviations"].append(ab)
            for af in ca.get("affiliations", []):
                if af and af not in entry["affiliations"]:
                    entry["affiliations"].append(af)

        if doi not in db["authors"][key]["papers_as_corresponding"]:
            db["authors"][key]["papers_as_corresponding"].append(doi)
        db["authors"][key]["last_updated"] = time.strftime("%Y-%m-%d")

    # Track all authors as coauthors for abbreviation matching
    for a in authors:
        akey = _normalize_abbrev(a["full_name"])
        if akey not in db["authors"]:
            # Only create entry for corresponding authors; but record
            # abbreviation mapping for lookup
            continue
        if doi not in db["authors"][akey].get("papers_as_coauthor", []):
            db["authors"][akey].setdefault("papers_as_coauthor", []).append(doi)

    return db


def resolve_author_name(abbrev: str, doi: str | None = None,
                        db: dict | None = None) -> tuple[str, bool]:
    """Resolve an abbreviated author name to full name.

    Lookup priority:
    1. CrossRef (if DOI available) → also updates DB
    2. Local DB (match by abbreviation)
    3. Return abbreviation as-is, mark dirty=True

    Returns (full_name, is_dirty).
    """
    if db is None:
        db = load_authors_db()

    norm = _normalize_abbrev(abbrev)

    # 1. Try CrossRef if DOI available
    if doi:
        authors = fetch_crossref_authors(doi)
        if authors:
            for a in authors:
                a_norm = _normalize_abbrev(a["full_name"])
                # Match: abbreviation matches initials+family pattern
                a_family = _normalize_abbrev(a.get("family", ""))
                a_initials = "".join(p[0] for p in a.get("given", "").split()
                                     if p and p[0].isalpha()).lower()
                # Check if abbrev matches this author
                if norm == a_norm or norm == f"{a_initials}{a_family}":
                    # Found in CrossRef, update DB
                    db = update_authors_from_doi(doi, db)
                    save_authors_db(db)
                    return a["full_name"], False
            # CrossRef returned authors but none matched — still update DB
            db = update_authors_from_doi(doi, db)
            save_authors_db(db)

    # 2. Try local DB
    for key, entry in db["authors"].items():
        known_abbrevs = [_normalize_abbrev(x) for x in entry.get("abbreviations", [])]
        if norm in known_abbrevs or norm == key:
            return entry["full_name"], entry.get("dirty", False)

    # 3. Dirty data — record it
    dirty_key = f"dirty_{norm}"
    if dirty_key not in db["authors"]:
        db["authors"][dirty_key] = {
            "full_name": abbrev,
            "abbreviations": [abbrev],
            "affiliations": [],
            "papers_as_corresponding": [],
            "papers_as_coauthor": [],
            "dirty": True,
            "last_updated": time.strftime("%Y-%m-%d"),
            "note": "Could not resolve to full name via CrossRef or DB",
        }
        save_authors_db(db)

    return abbrev, True


def build_authors_db(papers: list[dict]) -> dict:
    """Batch build the author database from a list of papers.

    Queries CrossRef for each paper with a DOI, extracts corresponding
    authors, and populates the DB.
    """
    db = load_authors_db()
    console.print(f"  [dim]Building author DB from {len(papers)} papers...[/dim]")

    for i, p in enumerate(papers):
        doi = p.get("doi")
        if not doi or p.get("doi_status", "").startswith("no_doi"):
            continue
        console.print(f"  [{i+1}/{len(papers)}] DOI: {doi[:40]}...", end="")
        try:
            db = update_authors_from_doi(doi, db)
            console.print(" [green]✓[/green]")
        except Exception as e:
            console.print(f" [red]✗ {e}[/red]")
        time.sleep(0.5)  # CrossRef rate limit

    save_authors_db(db)

    total = len(db["authors"])
    dirty = sum(1 for v in db["authors"].values() if v.get("dirty"))
    console.print(f"  [bold green]Author DB: {total} entries ({dirty} dirty)[/bold green]")
    return db


# ---------------------------------------------------------------------------
# Phase 2: Zotero Collection Management
# ---------------------------------------------------------------------------

def ensure_scholar_collection(scholar_name: str, cfg: dict) -> str:
    """Find or create a Zotero collection for this scholar under People/.
    Returns collection key.
    """
    from pyzotero import zotero as zotero_mod
    
    console.print(f"\n[bold cyan]━━━ Phase 2: Zotero Collection ━━━[/bold cyan]\n")
    
    pcfg = get_people_config(cfg)
    parent_name = pcfg.get("parent_collection", "People")
    
    zcfg = cfg["zotero"]
    zot = zotero_mod.Zotero(zcfg["library_id"], zcfg.get("library_type", "user"), zcfg["api_key"])
    
    # Find or create parent collection
    all_cols = zot.collections()
    parent_key = None
    
    for col in all_cols:
        if (col["data"]["name"] == parent_name 
            and not col["data"].get("parentCollection", False)):
            parent_key = col["key"]
            break
    
    if not parent_key:
        # Create parent
        resp = zot.create_collections([{
            "name": parent_name,
            "parentCollection": False,
        }])
        parent_key = resp["successful"]["0"]["key"]
        console.print(f"  Created parent collection: [bold]{parent_name}[/bold] ({parent_key})")
    else:
        console.print(f"  Found parent collection: [bold]{parent_name}[/bold] ({parent_key})")
    
    # Find or create scholar sub-collection
    scholar_key = None
    for col in all_cols:
        if (col["data"]["name"] == scholar_name 
            and col["data"].get("parentCollection") == parent_key):
            scholar_key = col["key"]
            break
    
    if not scholar_key:
        resp = zot.create_collections([{
            "name": scholar_name,
            "parentCollection": parent_key,
        }])
        scholar_key = resp["successful"]["0"]["key"]
        console.print(f"  Created scholar collection: [bold]{scholar_name}[/bold] ({scholar_key})")
    else:
        console.print(f"  Found scholar collection: [bold]{scholar_name}[/bold] ({scholar_key})")
    
    return scholar_key


# ---------------------------------------------------------------------------
# Data persistence
# ---------------------------------------------------------------------------

def save_papers(papers: list[dict], scholar_name: str, scholar_id: str,
                scholar_url: str = "") -> Path:
    """Save paper list to JSON."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^\w]", "_", scholar_name)
    path = DATA_DIR / f"{safe_name}_papers.json"
    
    data = {
        "scholar_name": scholar_name,
        "scholar_id": scholar_id,
        "scholar_url": scholar_url,
        "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "paper_count": len(papers),
        "papers": papers,
    }
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    console.print(f"\n  Saved papers list: [dim]{path}[/dim]")
    return path


def load_papers(scholar_name: str) -> dict | None:
    """Load previously saved paper list."""
    safe_name = re.sub(r"[^\w]", "_", scholar_name)
    path = DATA_DIR / f"{safe_name}_papers.json"
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_summary(papers: list[dict], scholar_name: str):
    """Print a summary table of scraped papers."""
    table = Table(title=f"\\n{scholar_name} — 论文列表 ({len(papers)} 篇)")
    table.add_column("#", style="dim", width=4)
    table.add_column("Year", width=6)
    table.add_column("Title", ratio=3)
    table.add_column("Venue", ratio=1.5)
    table.add_column("Cites", justify="right", width=6)
    table.add_column("DOI", width=12)
    table.add_column("Status", width=8)
    
    for i, p in enumerate(papers):
        doi_short = p.get("doi", "")[:20] + "..." if len(p.get("doi", "")) > 20 else p.get("doi", "")
        status = p.get("doi_status", "")
        status_color = {"matched": "green", "no_match": "yellow", "low_score": "yellow"}.get(status, "red")
        
        table.add_row(
            str(i + 1),
            str(p.get("year", "?")),
            p.get("title", "?")[:60],
            p.get("venue", "?")[:30],
            str(p.get("citations", 0)),
            doi_short,
            f"[{status_color}]{status}[/{status_color}]" if status else "",
        )
    
    console.print(table)


# ---------------------------------------------------------------------------
# Phase 3: Batch Download (linear, one paper per invocation for cron)
# ---------------------------------------------------------------------------

def download_one_paper(paper: dict, cfg: dict, collection_key: str,
                       timeout: int | None = None) -> dict:
    """Download a single paper, ensure Zotero item, attach PDF.
    
    State-aware flow (handles all 3 states efficiently):
      ① Already has PDF (dl_status=success) → skip entirely
      ② In Zotero, no PDF (zotero_key set) → only download + attach
      ③ Not in Zotero (no zotero_key) → create item + download + attach
    
    Key design: Zotero item creation is decoupled from PDF download.
    Item is created/found FIRST (fast, always works), then PDF is
    downloaded and attached. Download failure does NOT prevent
    Zotero registration.
    """
    title = paper.get("title", "")
    doi = paper.get("doi", "")
    
    console.print(f"\n  Processing: {title[:70]}")
    
    # State ①: already done
    if paper.get("dl_status") == "success":
        console.print("    [green]✓ Already downloaded, skipping[/green]")
        return paper
    
    if not doi:
        paper["dl_status"] = "no_doi"
        console.print("    [yellow]⊘ No DOI, skipping[/yellow]")
        return paper
    
    doi_url = f"https://doi.org/{doi}"
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        import zot
        from pyzotero import zotero as zotero_mod
        
        # ── Step 1: Resolve Zotero item by DOI (always, don't trust stored key) ──
        # Zotero auto-retrieves metadata which may change item identity.
        # DOI is the stable identifier — always look up by DOI first.
        zcfg = cfg["zotero"]
        zot_client = zotero_mod.Zotero(zcfg["library_id"], zcfg.get("library_type", "user"), zcfg["api_key"])
        
        item_key = ""
        # Search by DOI in the library
        try:
            results = zot_client.items(q=doi, qmode="everything", limit=5)
            for r in results:
                rd = r.get("data", {})
                if rd.get("itemType") in ("attachment", "note"):
                    continue
                if rd.get("DOI", "").lower().strip() == doi.lower().strip():
                    item_key = r["key"]
                    break
        except Exception:
            pass
        
        if item_key:
            console.print(f"    [dim]Found by DOI: {item_key}[/dim]")
            paper["zotero_key"] = item_key
        else:
            # Not found by DOI — create new (add_to_zotero has built-in dedup)
            meta = {
                "DOI": doi,
                "title": title,
                "url": doi_url,
                "journal": paper.get("venue", ""),
                "year": str(paper.get("year", "")),
            }
            author_str = paper.get("authors", "")
            if author_str:
                raw = [a.strip() for a in author_str.split(",")]
                meta["authors"] = [a for a in raw if a and a != "..." and len(a) > 1]
            
            item_key = zot.add_to_zotero(meta, cfg)
            paper["zotero_key"] = item_key
            console.print(f"    [dim]Created Zotero item: {item_key}[/dim]")
        
        # Assign to collection (idempotent — skips if already assigned)
        _assign_to_collection(item_key, collection_key, cfg)
        
        # ── Step 2: Check if item already has a PDF attachment ──
        children = zot_client.children(item_key)
        has_pdf = any(
            c.get("data", {}).get("contentType") == "application/pdf"
            for c in children
        )
        if has_pdf:
            paper["dl_status"] = "success"
            paper["dl_note"] = "PDF already attached to existing item"
            console.print("    [green]✓ PDF already attached, marking success[/green]")
            return paper
        
        # ── Step 3: Download PDF ──
        from url_parser import resolve_doi
        try:
            resolved = resolve_doi(doi)
            download_url = resolved if resolved else doi_url
        except Exception:
            download_url = doi_url
        
        console.print(f"    [dim]Downloading PDF...[/dim]")
        dl_timeout = timeout if timeout is not None else 120
        pdf_path = zot.download_pdf(download_url, cfg, timeout=dl_timeout)
        
        # ── Step 4: Attach PDF ──
        att_key = zot.attach_pdf(item_key, pdf_path, cfg)
        paper["attachment_key"] = att_key
        
        paper["dl_status"] = "success"
        console.print(f"    [green]✓ Done: item={item_key}, att={att_key}[/green]")
        
    except Exception as e:
        err = str(e)[:200]
        # Distinguish: Zotero item was created but PDF download failed
        if paper.get("zotero_key"):
            paper["dl_status"] = "failed"
            paper["dl_error"] = err
            console.print(f"    [red]✗ PDF failed (item {paper['zotero_key']} exists): {err[:80]}[/red]")
        else:
            paper["dl_status"] = "failed"
            paper["dl_error"] = err
            console.print(f"    [red]✗ Failed: {err[:80]}[/red]")
    
    return paper


def register_to_zotero(papers: list[dict], cfg: dict, collection_key: str,
                       save_callback=None) -> list[dict]:
    """Register all DOI-matched papers as Zotero items (no PDF needed).
    
    Creates Zotero entries from CrossRef metadata only. Papers that already
    have zotero_key are skipped. This decouples Zotero registration from
    PDF downloading — the cron download phase only needs to attach PDFs later.
    
    Args:
        save_callback: Optional callable(papers) to save progress periodically.
    """
    console.print(f"\n[bold cyan]━━━ Zotero 批量注册 ({len(papers)} 篇) ━━━[/bold cyan]\n")
    
    to_register = []
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
    
    import zot
    sys.path.insert(0, str(Path(__file__).parent))
    
    for i, paper in enumerate(to_register):
        title = paper.get("title", "")[:70]
        doi = paper.get("doi", "")
        console.print(f"\n  [{i+1}/{len(to_register)}] {title}")
        
        try:
            meta = {
                "DOI": doi,
                "title": paper.get("title", ""),
                "url": f"https://doi.org/{doi}",
                "journal": paper.get("venue", ""),
                "year": str(paper.get("year", "")),
            }
            author_str = paper.get("authors", "")
            if author_str:
                raw = [a.strip() for a in author_str.split(",")]
                meta["authors"] = [a for a in raw if a and a != "..." and len(a) > 1]
            
            item_key = zot.add_to_zotero(meta, cfg)
            paper["zotero_key"] = item_key
            paper["zotero_status"] = "registered"
            
            _assign_to_collection(item_key, collection_key, cfg)
            console.print(f"    [green]✓ {item_key}[/green]")
            
        except Exception as e:
            paper["zotero_status"] = "failed"
            paper["zotero_error"] = str(e)[:200]
            console.print(f"    [red]✗ {str(e)[:80]}[/red]")
        
        # Save every 10 papers
        if save_callback and (i + 1) % 10 == 0:
            save_callback(papers)
    
    if save_callback:
        save_callback(papers)
    
    registered = sum(1 for p in papers if p.get("zotero_key"))
    failed = sum(1 for p in papers if p.get("zotero_status") == "failed")
    console.print(f"\n  [bold green]Done: {registered} registered, {failed} failed[/bold green]")
    
    return papers


def _assign_to_collection(item_key: str, collection_key: str, cfg: dict):
    """Add a Zotero item to a collection."""
    from pyzotero import zotero as zotero_mod
    zcfg = cfg["zotero"]
    zot = zotero_mod.Zotero(zcfg["library_id"], zcfg.get("library_type", "user"), zcfg["api_key"])
    
    # Get item, add collection
    item = zot.item(item_key)
    collections = item["data"].get("collections", [])
    if collection_key not in collections:
        collections.append(collection_key)
        item["data"]["collections"] = collections
        zot.update_item(item)


def retry_failed(papers: list[dict], cfg: dict,
                 scholar_name: str, scholar_id: str) -> list[dict]:
    """Second-round retry for papers that failed in the first batch.
    
    Classification:
      - SPIE conference (DOI 10.1117/12.) -> mark as 'conference', skip
      - Timeout failures -> retry with 180s timeout
      - 'did not produce a PDF' -> retry (new adapters may exist now)
      - Already success/no_doi -> skip
    
    Returns updated papers list.
    """
    console.print(f"\n[bold cyan]━━━ Round 2 Retry ━━━[/bold cyan]\n")
    
    failed = [p for p in papers if p.get("dl_status") == "failed"]
    if not failed:
        console.print("  [green]No failed papers to retry.[/green]")
        return papers
    
    collection_key = ensure_scholar_collection(scholar_name, cfg)
    retried = 0
    skipped = 0
    
    for i, paper in enumerate(failed):
        doi = paper.get("doi", "")
        err = paper.get("dl_error", "")
        title = paper.get("title", "")[:60]
        
        console.print(f"\n  [{i+1}/{len(failed)}] {title}")
        
        # 1. SPIE conference DOI prefix -> mark as conference, skip
        if doi.startswith("10.1117/12."):
            paper["dl_status"] = "conference"
            paper["dl_error"] = "SPIE conference proceeding, filtered out"
            console.print(f"    [yellow]skip SPIE conference[/yellow]")
            skipped += 1
            save_papers(papers, scholar_name, scholar_id)
            continue
        
        # 2. Timeout failures -> retry with longer timeout
        if "timed out" in err:
            paper["dl_status"] = ""
            console.print(f"    [dim]Timeout -> retry 180s[/dim]")
            download_one_paper(paper, cfg, collection_key, timeout=180)
            retried += 1
        
        # 3. "did not produce a PDF" -> retry (may have new adapter)
        elif "did not produce a PDF" in err:
            paper["dl_status"] = ""
            console.print(f"    [dim]Publisher issue -> retry[/dim]")
            download_one_paper(paper, cfg, collection_key)
            retried += 1
        
        # 4. Other -> retry with default
        else:
            paper["dl_status"] = ""
            console.print(f"    [dim]Unknown failure -> retry[/dim]")
            download_one_paper(paper, cfg, collection_key)
            retried += 1
        
        save_papers(papers, scholar_name, scholar_id)
    
    success = sum(1 for p in failed if p.get("dl_status") == "success")
    failed_again = sum(1 for p in failed if p.get("dl_status") == "failed")
    conference = sum(1 for p in failed if p.get("dl_status") == "conference")
    
    console.print(f"\n  [bold]Retry Summary:[/bold]")
    console.print(f"    OK: {success}  Failed: {failed_again}  Conference: {conference}")
    
    return papers


def download_batch(papers: list[dict], cfg: dict, collection_key: str,
                   resume: bool = True,
                   retry_timeout: int | None = None,
                   save_callback=None,
                   max_downloads: int | None = None) -> list[dict]:
    """Download papers linearly (one at a time).
    
    With resume=True, skips papers that already have dl_status='success'.
    Each download uses the full rate-limiting from config.
    Designed to be called by a cron job that runs once per ~10 minutes.
    
    Args:
        save_callback: Optional callable(papers) to save progress after each paper
        retry_timeout: If set, override per-paper timeout (for retrying failed papers)
    """
    console.print(f"\n[bold cyan]━━━ Phase 3: 批量下载 ({len(papers)} 篇) ━━━[/bold cyan]\n")
    
    # Sort by year ascending (oldest first, per user spec)
    papers_sorted = sorted(papers, key=lambda p: p.get("year", 0))
    
    to_download = []
    for p in papers_sorted:
        status = p.get("dl_status", "")
        if resume and status == "success":
            continue
        if not p.get("doi"):
            p["dl_status"] = "no_doi"
            continue
        to_download.append(p)
    
    if not to_download:
        console.print("  [green]All papers already downloaded or no DOIs.[/green]")
        return papers
    
    console.print(f"  To download: {len(to_download)} (skipped {len(papers_sorted) - len(to_download)})")
    
    for i, paper in enumerate(to_download):
        if max_downloads and i >= max_downloads:
            console.print(f"\n  [yellow]Reached max_downloads limit ({max_downloads}), stopping.[/yellow]")
            break
        console.print(f"\n  [{i+1}/{len(to_download)}]")
        download_one_paper(paper, cfg, collection_key, timeout=retry_timeout)
        
        # Save progress after each paper (for resume / crash recovery)
        if save_callback:
            try:
                save_callback(papers)
            except Exception as e:
                console.print(f"    [yellow]Progress save failed: {e}[/yellow]")
    
    # Summary
    success = sum(1 for p in papers if p.get("dl_status") == "success")
    failed = sum(1 for p in papers if p.get("dl_status") == "failed")
    no_doi = sum(1 for p in papers if p.get("dl_status") == "no_doi")
    
    console.print(f"\n  [bold]Download Summary:[/bold]")
    console.print(f"    ✓ Success: {success}")
    console.print(f"    ✗ Failed:  {failed}")
    console.print(f"    ⊘ No DOI:  {no_doi}")
    
    return papers


# ---------------------------------------------------------------------------
# Phase 4: Digest Template Generation
# ---------------------------------------------------------------------------

def generate_digest_template(papers: list[dict], scholar_name: str,
                             scholar_url: str, cfg: dict) -> Path:
    """Generate a structured literature digest template markdown file."""
    
    console.print(f"\n[bold cyan]━━━ Phase 4: 文献消化模板 ━━━[/bold cyan]\n")
    
    digest_dir = SKILL_BASE / "people" / "digests"
    digest_dir.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^\w]", "_", scholar_name)
    out_path = digest_dir / f"{safe_name}_digest.md"
    
    # Sort by year
    papers_sorted = sorted(papers, key=lambda p: p.get("year", 0))
    
    # Stats
    years = [p.get("year", 0) for p in papers if p.get("year")]
    year_range = f"{min(years)}–{max(years)}" if years else "?"
    total = len(papers)
    matched = sum(1 for p in papers if p.get("doi") and p.get("doi_status", "").startswith("matched"))
    
    # Build template
    lines = []
    lines.append(f"# {scholar_name} — 文献消化报告\n")
    lines.append(f"> 生成时间: {time.strftime('%Y-%m-%d')}")
    lines.append(f"> 论文总数: {total} 篇（去重、过滤后）")
    lines.append(f"> 时间跨度: {year_range}")
    lines.append(f"> DOI 匹配: {matched}/{total}")
    lines.append(f"> Scholar Profile: {scholar_url}\n")
    lines.append("---\n")
    
    # ── Block 1 ──
    lines.append("## Block 1: 研究脉络 — 研究对象与核心方法的变迁\n")
    lines.append("> 通读所有论文标题和摘要，按时间线梳理研究对象和核心方法如何演变。\n")
    lines.append("### 时间线总览\n")
    lines.append("| 时期 | 研究对象 | 核心方法 | 代表论文 |")
    lines.append("|------|---------|---------|---------|")
    lines.append("| YYYY–YYYY | ... | ... | [标题] (DOI) |\n")
    lines.append("### 方法论转折点\n")
    lines.append("- **YYYY**: [关键转变描述]")
    lines.append("  - 触发: ...")
    lines.append("  - 论文: [标题] (DOI)\n")
    lines.append("### 研究主题分类\n")
    lines.append("1. **主题 A** (YYYY–YYYY): ...")
    lines.append("2. **主题 B** (YYYY–YYYY): ...\n")
    
    # ── Block 2 ──
    lines.append("---\n")
    lines.append("## Block 2: 合作者网络\n")
    lines.append("> 从作者列表中提取高频合作者，识别核心团队和外部合作。\n")
    lines.append("### 核心合作者（≥3 篇共作）\n")
    lines.append("| 合作者 | 共作篇数 | 机构（推测） | 主要合作主题 | 活跃时期 |")
    lines.append("|--------|---------|-------------|-------------|---------|\n")
    lines.append("### 合作模式\n")
    lines.append("- **实验室内部**: ...")
    lines.append("- **跨机构合作**: ...")
    lines.append("- **产业合作**: ...\n")
    
    # ── Block 3 ──
    lines.append("---\n")
    lines.append("## Block 3: 综述文章精读\n")
    lines.append("> 识别该学者的 review/survey 论文，作为理解其研究领域的入口。\n")
    
    # Find reviews
    reviews = [p for p in papers if re.search(r"review|survey|perspective|outlook", 
               p.get("title", ""), re.IGNORECASE)]
    if reviews:
        lines.append("### 综述清单\n")
        lines.append("| 年份 | 标题 | 期刊 | DOI |")
        lines.append("|------|------|------|-----|")
        for r in reviews:
            doi = r.get("doi", "")
            lines.append(f"| {r.get('year','')} | {r['title'][:50]} | {r.get('venue','')[:30]} | {doi} |")
        lines.append("")
    else:
        lines.append("_（暂未发现明确综述论文，检查后补充）_\n")
    
    lines.append("### 综述要点\n")
    lines.append("对每篇综述：")
    lines.append("- **覆盖范围**: ...")
    lines.append("- **核心观点**: ...")
    lines.append("- **技术框架**: ...\n")
    
    # ── Block 4 ──
    lines.append("---\n")
    lines.append("## Block 4: 核心高引论文深读\n")
    lines.append("> 按引用数排序的前 10 篇论文，深入分析其贡献。\n")
    
    # Top 10 by citations
    top10 = sorted(papers, key=lambda p: p.get("citations", 0), reverse=True)[:10]
    lines.append("### 高引论文 Top 10\n")
    lines.append("| 排名 | 引用数 | 年份 | 标题 | DOI |")
    lines.append("|------|--------|------|------|-----|")
    for rank, p in enumerate(top10, 1):
        lines.append(f"| {rank} | {p.get('citations',0)} | {p.get('year','')} | {p['title'][:50]} | {p.get('doi','')} |")
    lines.append("")
    lines.append("### 逐篇深读\n")
    lines.append("对每篇高引论文：")
    lines.append("- **解决的问题**: ...")
    lines.append("- **核心创新**: ...")
    lines.append("- **方法细节**: ...")
    lines.append("- **影响**: ...\n")
    
    # ── Cross-talk section ──
    lines.append("---\n")
    lines.append("## ⚡ Cross-talk 更新区\n")
    lines.append("> 不同 Block 之间的关联发现。在填充各 Block 时发现的跨 Block 联系记录于此，")
    lines.append("> 并在对应 Block 中插入 ⚡ 标记。\n")
    
    # ── Appendix ──
    lines.append("---\n")
    lines.append("## 附录\n")
    lines.append("### A. 完整论文列表\n")
    lines.append("| # | 年份 | 标题 | Venue | Citations | DOI | 状态 |")
    lines.append("|---|------|------|-------|-----------|-----|------|")
    for i, p in enumerate(papers_sorted, 1):
        dl = p.get("dl_status", "")
        lines.append(f"| {i} | {p.get('year','')} | {p['title'][:40]} | {p.get('venue','')[:25]} | {p.get('citations',0)} | {p.get('doi','')[:25]} | {dl} |")
    lines.append("")
    
    # Download status
    dl_success = sum(1 for p in papers if p.get("dl_status") == "success")
    dl_failed = sum(1 for p in papers if p.get("dl_status") == "failed")
    dl_no_doi = sum(1 for p in papers if p.get("dl_status") == "no_doi")
    dl_pending = total - dl_success - dl_failed - dl_no_doi
    
    lines.append("### B. 下载状态\n")
    lines.append("| 状态 | 数量 |")
    lines.append("|------|------|")
    lines.append(f"| 已下载 | {dl_success} |")
    lines.append(f"| 下载失败 | {dl_failed} |")
    lines.append(f"| 无 DOI | {dl_no_doi} |")
    lines.append(f"| 待下载 | {dl_pending} |\n")
    
    content = "\n".join(lines)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    console.print(f"  [green]✓ Template generated:[/green] {out_path}")
    console.print(f"  [dim]{total} papers, {len(reviews)} reviews identified, top-10 citations table populated[/dim]")
    
    return out_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="people: Scholar Profile → Zotero → 文献消化",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("url", nargs="?", help="Google Scholar Profile URL")
    parser.add_argument("--scrape-only", action="store_true", 
                        help="Only scrape Scholar, don't download or create Zotero items")
    parser.add_argument("--download-only", action="store_true",
                        help="Skip scrape+DOI, load existing papers.json and download")
    parser.add_argument("--template-only", action="store_true",
                        help="Skip scrape+download, load existing papers.json and generate digest template")
    parser.add_argument("--max-papers", type=int, default=None,
                        help="Limit number of papers (for testing)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Scrape + DOI match only, no downloads or Zotero operations")
    parser.add_argument("--no-scrape", action="store_true",
                        help="Skip scraping, use existing papers.json")
    parser.add_argument("--no-doi-match", action="store_true",
                        help="Skip CrossRef DOI matching")
    parser.add_argument("--download", action="store_true",
                        help="Enable Phase 3 download (default: disabled for safety)")
    parser.add_argument("--scholar-name", type=str, default=None,
                        help="Override scholar name (for --download-only/--template-only)")
    parser.add_argument("--retry", action="store_true",
                        help="Retry failed papers: load existing json, retry failed downloads")
    parser.add_argument("--register-only", action="store_true",
                        help="Register all DOI-matched papers to Zotero (no PDF download)")
    
    args = parser.parse_args()
    
    if not args.url and not (args.download_only or args.template_only or args.retry or args.register_only):
        console.print("Usage: [bold]python people.py <Scholar URL>[/bold]")
        console.print('  python people.py "https://scholar.google.com/citations?user=XXXX" --scrape-only')
        console.print('  python people.py "URL" --download          # scrape + DOI + download')
        console.print('  python people.py --download-only --scholar-name "Yifan Zhu"  # resume download')
        console.print('  python people.py --template-only --scholar-name "Yifan Zhu"  # gen template')
        sys.exit(1)
    
    cfg = load_config()
    
    # ── Load existing data for download-only / template-only / register-only ──
    if args.download_only or args.template_only or args.register_only:
        sn = args.scholar_name or "Yifan Zhu"
        data = load_papers(sn)
        if not data:
            console.print(f"[red]No saved papers found for '{sn}'. Run --scrape-only first.[/red]")
            sys.exit(1)
        papers = data["papers"]
        scholar_name = data.get("scholar_name", sn)
        scholar_url = data.get("scholar_url", "")
        
        if args.template_only:
            generate_digest_template(papers, scholar_name, scholar_url, cfg)
            return
        
        # register-only: batch create Zotero items from CrossRef metadata
        if args.register_only:
            collection_key = ensure_scholar_collection(scholar_name, cfg)
            sname, sid = scholar_name, data.get("scholar_id", "")
            papers = register_to_zotero(papers, cfg, collection_key,
                                        save_callback=lambda p: save_papers(p, sname, sid))
            save_papers(papers, sname, sid)
            return
        
        # download-only
        collection_key = ensure_scholar_collection(scholar_name, cfg)
        sname, sid = scholar_name, data.get("scholar_id", "")
        papers = download_batch(papers, cfg, collection_key, resume=True,
                                save_callback=lambda p: save_papers(p, sname, sid),
                                max_downloads=args.max_papers)
        save_papers(papers, sname, sid)
        return
    
    # ── Retry failed papers ──
    if args.retry:
        sn = args.scholar_name or "Yifan Zhu"
        data = load_papers(sn)
        if not data:
            console.print(f"[red]No saved papers found for '{sn}'. Run --scrape-only first.[/red]")
            sys.exit(1)
        papers = data["papers"]
        scholar_name = data.get("scholar_name", sn)
        papers = retry_failed(papers, cfg, scholar_name, data.get("scholar_id", ""))
        save_papers(papers, scholar_name, data.get("scholar_id", ""))
        return
    
    # ── Phase 1: Scrape Scholar ──
    if args.no_scrape:
        # Try loading existing data
        scholar_name = ""
        if args.url:
            scholar_name = args.url  # Not ideal, but try
        console.print("[yellow]Loading existing papers.json (no scrape)...[/yellow]")
        console.print("[red]--no-scrape requires existing data. Use --scrape-only first.[/red]")
        sys.exit(1)
    
    scholar_id = parse_scholar_url(args.url) if args.url else ""
    
    papers, scholar_name = scrape_scholar_profile(
        args.url, cfg, max_papers=args.max_papers
    )
    
    # Save scraped data
    save_papers(papers, scholar_name, scholar_id, scholar_url=args.url)
    
    # Print summary
    print_summary(papers, scholar_name)
    
    if args.scrape_only:
        console.print("\n[bold green]✓ Scrape-only complete.[/bold green]")
        return
    
    # ── Phase 1b: CrossRef DOI matching ──
    if not args.no_doi_match:
        papers = match_dois(papers, cfg)
        save_papers(papers, scholar_name, scholar_id, scholar_url=args.url)  # Update with DOIs
    
    if args.dry_run:
        console.print("\n[bold yellow]Dry run complete — no downloads or Zotero operations.[/bold yellow]")
        return
    
    # ── Phase 2: Zotero Collection ──
    collection_key = ensure_scholar_collection(scholar_name, cfg)
    
    # ── Phase 3: Download ──
    if args.download:
        papers = download_batch(papers, cfg, collection_key, resume=True,
                                save_callback=lambda p: save_papers(p, scholar_name, scholar_id, scholar_url=args.url))
        save_papers(papers, scholar_name, scholar_id, scholar_url=args.url)
    else:
        console.print(f"\n[dim]Phase 3 (download) skipped. Use --download to enable.[/dim]")
    
    # ── Phase 4: Digest template ──
    generate_digest_template(papers, scholar_name, args.url, cfg)


if __name__ == "__main__":
    main()
