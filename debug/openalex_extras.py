"""
Analyze the "extra" papers that OpenAlex has but Zotero doesn't.
Goal: classify what these are — real journal papers we missed? 
Conferences? Preprints? Abstracts? False positives?
"""
import requests, json, sqlite3, shutil, tempfile, os, time
from collections import Counter, defaultdict

MAILTO = "lit-skill/1.0 (mailto:research@example.com)"
HEADERS = {"User-Agent": MAILTO}


def get_zotero_dois(collection_name):
    src = r"C:\Users\Ivanz\Zotero\zotero.sqlite"
    tmp = os.path.join(tempfile.gettempdir(), "zotero_copy.sqlite")
    shutil.copy2(src, tmp)
    conn = sqlite3.connect(tmp)
    rows = conn.execute("""
        SELECT DISTINCT idv.value
        FROM collectionItems ci
        JOIN collections c ON ci.collectionID = c.collectionID
        JOIN itemData id ON ci.itemID = id.itemID
        JOIN fields f ON id.fieldID = f.fieldID
        JOIN itemDataValues idv ON id.valueID = idv.valueID
        WHERE c.collectionName = ? AND f.fieldName = 'DOI'
    """, (collection_name,)).fetchall()
    conn.close()
    os.unlink(tmp)
    return set(r[0].lower().strip() for r in rows if r[0])


def openalex_get_author_works(openalex_id, max_papers=800):
    """Get all works for an author with full metadata."""
    all_works = []
    cursor = "*"
    while cursor and len(all_works) < max_papers:
        resp = requests.get("https://api.openalex.org/works", params={
            "filter": f"author.id:{openalex_id}",
            "per-page": 200,
            "cursor": cursor,
            "select": "doi,publication_year,type,title,primary_location,authorships",
        }, headers=HEADERS, timeout=30)
        if resp.status_code != 200:
            print(f"    HTTP {resp.status_code}")
            break
        data = resp.json()
        works = data.get("results", [])
        if not works:
            break
        all_works.extend(works)
        cursor = data.get("meta", {}).get("next_cursor")
        time.sleep(0.15)
    return all_works


def classify_work(w):
    """Classify a work into a category."""
    wtype = w.get("type", "unknown")
    doi = (w.get("doi") or "").replace("https://doi.org/", "").lower().strip()
    title = w.get("title", "") or ""
    title_lower = title.lower()
    
    # Primary classification by type
    if wtype == "journal-article":
        # Check if it's actually junk
        if any(kw in title_lower for kw in [
            "front matter", "back matter", "inside cover", "innentitelbild",
            "editorial board", "subject index", "contents", "table of contents",
            "author index", "volume index", "erratum", "corrigendum",
        ]):
            return "junk"
        # Check DOI prefix for conferences disguised as journal articles
        conf_prefixes = [
            "10.1117/12.",  # SPIE conference papers
            "10.1109/cleo", "10.1109/icleo",  # IEEE CLEO
            "10.1364/cleo", "10.1364/cosi", "10.1364/ls", "10.1364/ntm",  # OSA conferences
            "10.1364/up", "10.1364/amo", "10.1364/ sensors",  # more OSA
            "10.1364/ Microscopy", "10.1364/ microscopy",
            "10.1109/4655",  # IEEE EMBS (conference)
            "10.1109/phil",  # IEEE PHIL
            "10.25920/",  # Research Square preprints
            "10.21203/rs.",  # Research Square preprints
            "10.1101/",  # bioRxiv/medRxiv preprints
            "10.20944/preprints",  # Preprints.org
            "10.6084/m9.figshare",  # Figshare datasets
        ]
        for prefix in conf_prefixes:
            if doi.startswith(prefix):
                if "preprint" in prefix or "10.1101/" == prefix or "10.21203/" in prefix or "10.20944/" in prefix:
                    return "preprint"
                if "10.6084/" in prefix:
                    return "dataset"
                return "conference"
        return "journal"
    
    # Explicit types
    type_map = {
        "proceedings-article": "conference",
        "conference-paper": "conference",
        "book-chapter": "book_chapter",
        "book": "book",
        "preprint": "preprint",
        "dataset": "dataset",
        "paratext": "junk",
        "report": "report",
        "standard": "standard",
        "dissertation": "thesis",
        "editorial": "junk",
        "letter": "letter",
        "review": "journal",  # review articles are real journal papers
    }
    return type_map.get(wtype, f"other:{wtype}")


# ═══════════════════════════════════════════════════════════════
# Process each author
# ═══════════════════════════════════════════════════════════════

openalex_ids = {
    "Ji-Xin Cheng": "A5086153927",
    "Ping Wang": "A5011310852",
    "Dan Fu": "A5020132617",
}

for author, oa_id in openalex_ids.items():
    print("=" * 70)
    print(f"  {author} (OpenAlex: {oa_id})")
    print("=" * 70)
    
    zotero_dois = get_zotero_dois(author)
    print(f"  Zotero DOIs: {len(zotero_dois)}")
    
    print(f"  Fetching OpenAlex works...")
    works = openalex_get_author_works(oa_id)
    print(f"  OpenAlex works: {len(works)}")
    
    # Build DOI set
    oa_dois = set()
    for w in works:
        doi = (w.get("doi") or "").replace("https://doi.org/", "").lower().strip()
        if doi:
            oa_dois.add(doi)
    
    # Find extra papers (in OA, not in Zotero)
    extra_dois = oa_dois - zotero_dois
    print(f"  Extra papers (in OA, not Zotero): {len(extra_dois)}")
    
    # Classify extras
    extra_works = [w for w in works 
                   if (w.get("doi") or "").replace("https://doi.org/", "").lower().strip() in extra_dois]
    
    categories = Counter()
    category_details = defaultdict(list)
    
    for w in extra_works:
        cat = classify_work(w)
        categories[cat] += 1
        doi = (w.get("doi") or "").replace("https://doi.org/", "").lower().strip()
        title = (w.get("title") or "")[:80]
        year = w.get("publication_year", "?")
        
        # Get venue
        loc = w.get("primary_location", {})
        source = loc.get("source", {}) if loc else {}
        venue = source.get("display_name", "") if source else ""
        
        # Get this author's institutions on this paper
        institutions = []
        for au in w.get("authorships", []):
            a = au.get("author", {})
            aid = (a.get("id") or "").split("/")[-1]
            if aid == oa_id:
                institutions = [i.get("display_name", "") for i in au.get("institutions", [])]
                break
        
        category_details[cat].append({
            "doi": doi,
            "title": title,
            "year": year,
            "venue": venue[:40],
            "institutions": institutions[:2],
        })
    
    # Print summary
    print(f"\n  Classification of {len(extra_works)} extra papers:")
    print(f"  {'Category':<20} {'Count':>6}  {'%'}")
    print(f"  {'-'*20} {'-'*6}  {'-'*5}")
    total = sum(categories.values())
    for cat in sorted(categories, key=lambda x: -categories[x]):
        pct = 100 * categories[cat] / total
        print(f"  {cat:<20} {categories[cat]:>6}  {pct:.0f}%")
    
    # For journal papers, show details (these need human analysis)
    journal_extras = category_details.get("journal", [])
    if journal_extras:
        print(f"\n  ── Journal papers not in Zotero ({len(journal_extras)}) ──")
        # Sort by year desc
        journal_extras.sort(key=lambda x: str(x["year"]), reverse=True)
        for p in journal_extras[:30]:
            inst_str = ", ".join(p["institutions"]) if p["institutions"] else "?"
            print(f"    {p['year']} | {p['doi'][:40]:40s} | {p['venue'][:30]:30s} | {inst_str}")
            print(f"         {p['title']}")
        if len(journal_extras) > 30:
            print(f"    ... and {len(journal_extras) - 30} more")
    
    print()
    time.sleep(1)

print("\nDone!")
