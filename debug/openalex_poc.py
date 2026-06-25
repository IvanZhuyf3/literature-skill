"""
OpenAlex PoC: 3 questions to answer
1. Author ID + bio → can it find ALL papers (coverage vs Zotero)?
2. Author ID → does it have old/historical papers?
3. DOI reverse lookup → false positive rate for author discovery?

Test subjects: Ji-Xin Cheng (569 in Zotero), Ping Wang (49), Dan Fu (common name)
"""
import requests, json, sqlite3, shutil, tempfile, os, time
from collections import Counter

MAILTO = "lit-skill/1.0 (mailto:research@example.com)"
HEADERS = {"User-Agent": MAILTO}

def get_zotero_dois(collection_name):
    """Get all DOIs from a Zotero collection."""
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


def openalex_work_to_doi(work):
    """Extract DOI from OpenAlex work (strip 'https://doi.org/' prefix)."""
    doi = work.get("doi", "") or ""
    return doi.replace("https://doi.org/", "").lower().strip()


def openalex_get_author_papers(openalex_id, max_papers=500):
    """Get all paper DOIs for an OpenAlex author ID. Paginate via cursor."""
    all_dois = set()
    cursor = "*"
    base_url = f"https://api.openalex.org/works"
    
    while cursor and len(all_dois) < max_papers:
        resp = requests.get(base_url, params={
            "filter": f"author.id:{openalex_id}",
            "per-page": 200,
            "cursor": cursor,
        }, headers=HEADERS, timeout=30)
        if resp.status_code != 200:
            print(f"    HTTP {resp.status_code}")
            break
        data = resp.json()
        works = data.get("results", [])
        if not works:
            break
        for w in works:
            doi = openalex_work_to_doi(w)
            if doi:
                all_dois.add(doi)
        cursor = data.get("meta", {}).get("next_cursor")
        time.sleep(0.1)  # be polite
    
    return all_dois


def openalex_doi_reverse_lookup(dois):
    """Batch DOI lookup: returns {doi: [{author_id, author_name, institutions}]}."""
    # OpenAlex doesn't have batch API, but individual lookups are fast
    # Use /works?filter=doi:xxx (pipe-separated for batch of up to 50)
    results = {}
    doi_list = list(dois)
    batch_size = 50  # OpenAlex supports pipe-separated filter values
    
    for i in range(0, len(doi_list), batch_size):
        batch = doi_list[i:i+batch_size]
        # Use filter with | separator
        doi_filter = "|".join(batch)
        resp = requests.get(
            "https://api.openalex.org/works",
            params={
                "filter": f"open_access:*,doi:{doi_filter}" if False else f"doi:{doi_filter}",
                "per-page": batch_size,
            },
            headers=HEADERS,
            timeout=30,
        )
        if resp.status_code != 200:
            print(f"  Batch {i}: HTTP {resp.status_code}")
            time.sleep(0.5)
            continue
        data = resp.json()
        for w in data.get("results", []):
            doi = openalex_work_to_doi(w)
            if doi not in dois:
                continue
            authors_info = []
            for au in w.get("authorships", []):
                author = au.get("author", {})
                aid = (author.get("id") or "").split("/")[-1]
                name = author.get("display_name", "")
                insts = [inst.get("display_name", "") for inst in au.get("institutions", [])]
                authors_info.append({
                    "id": aid,
                    "name": name,
                    "institutions": insts,
                })
            results[doi] = authors_info
        time.sleep(0.2)
    
    return results


def openalex_author_search(name):
    """Search for author by name, return top candidates with affiliations."""
    resp = requests.get(
        "https://api.openalex.org/authors",
        params={"search": name, "per-page": 5},
        headers=HEADERS,
        timeout=15,
    )
    if resp.status_code != 200:
        return []
    return resp.json().get("results", [])


# ═══════════════════════════════════════════════════════════════
# TEST 1: Coverage — does OpenAlex author ID cover all Zotero papers?
# ═══════════════════════════════════════════════════════════════
print("=" * 70)
print("TEST 1: Coverage (Author ID → all papers vs Zotero)")
print("=" * 70)

test_subjects = [
    ("Ji-Xin Cheng", "Ji-Xin Cheng"),
    ("Ping Wang", "Ping Wang"),
    ("Dan Fu", "Dan Fu"),
]

# First, find the right OpenAlex author ID for each via DOI reverse lookup
for zotero_collection, display_name in test_subjects:
    print(f"\n--- {display_name} ---")
    zotero_dois = get_zotero_dois(zotero_collection)
    print(f"  Zotero DOIs: {len(zotero_dois)}")
    
    # Sample 10 DOIs for author discovery
    sample_dois = list(zotero_dois)[:10]
    author_data = openalex_doi_reverse_lookup(set(sample_dois))
    
    # Count author ID appearances
    author_counter = Counter()
    author_insts = {}
    for doi, authors in author_data.items():
        for au in authors:
            name_lower = au["name"].lower()
            family = display_name.rsplit()[-1].lower()
            if family in name_lower:
                author_counter[au["id"]] += 1
                if au["id"] not in author_insts:
                    author_insts[au["id"]] = (au["name"], au["institutions"])
    
    if not author_counter:
        print("  No author matches found!")
        continue
    
    print(f"  Top OpenAlex author IDs (from 10 DOI sample):")
    for aid, count in author_counter.most_common(5):
        name, insts = author_insts.get(aid, ("?", []))
        print(f"    {aid}: {name} ({count}/10) | {insts[:2]}")
    
    # Pick the most frequent ID
    best_id = author_counter.most_common(1)[0][0]
    best_name = author_insts[best_id][0]
    print(f"\n  Selected: {best_id} ({best_name})")
    
    # Get ALL papers for this author
    print(f"  Fetching all papers for {best_id}...")
    oa_dois = openalex_get_author_papers(best_id, max_papers=800)
    print(f"  OpenAlex total papers: {len(oa_dois)}")
    
    # Coverage analysis
    overlap = zotero_dois & oa_dois
    in_zotero_not_oa = zotero_dois - oa_dois
    in_oa_not_zotero = oa_dois - zotero_dois
    
    print(f"\n  Coverage:")
    print(f"    In both (overlap):     {len(overlap)}")
    print(f"    In Zotero, not OA:     {len(in_zotero_not_oa)} ({'these are gaps!' if in_zotero_not_oa else 'perfect coverage'})")
    print(f"    In OA, not in Zotero:  {len(in_oa_not_zotero)} ({'these are papers we missed!' if in_oa_not_zotero else 'no new papers'})")
    
    if in_zotero_not_oa:
        print(f"\n  Sample DOIs in Zotero but NOT in OpenAlex:")
        for d in list(in_zotero_not_oa)[:5]:
            print(f"    {d}")
    
    if in_oa_not_zotero:
        print(f"\n  Sample DOIs in OpenAlex but NOT in Zotero (might be real misses):")
        for d in list(in_oa_not_zotero)[:5]:
            print(f"    {d}")
    
    time.sleep(1)


# ═══════════════════════════════════════════════════════════════
# TEST 2: Historical coverage — old papers present?
# ═══════════════════════════════════════════════════════════════
print("\n\n" + "=" * 70)
print("TEST 2: Historical paper coverage (old papers in OpenAlex?)")
print("=" * 70)

# Cheng has papers from 1990s. Check year distribution.
print("\n--- Ji-Xin Cheng: year distribution ---")
zotero_dois = get_zotero_dois("Ji-Xin Cheng")
# Use the best author ID found in Test 1
# We'll re-discover it quickly
sample_dois = list(zotero_dois)[:5]
author_data = openalex_doi_reverse_lookup(set(sample_dois))
author_counter = Counter()
for doi, authors in author_data.items():
    for au in authors:
        if "cheng" in au["name"].lower():
            author_counter[au["id"]] += 1

if author_counter:
    best_id = author_counter.most_common(1)[0][0]
    # Get papers with years
    cursor = "*"
    year_counter = Counter()
    while cursor and sum(year_counter.values()) < 800:
        resp = requests.get("https://api.openalex.org/works", params={
            "filter": f"author.id:{best_id}",
            "per-page": 200,
            "cursor": cursor,
            "select": "doi,publication_year",
        }, headers=HEADERS, timeout=30)
        if resp.status_code != 200:
            break
        data = resp.json()
        for w in data.get("results", []):
            yr = w.get("publication_year")
            if yr:
                year_counter[yr] += 1
        cursor = data.get("meta", {}).get("next_cursor")
        time.sleep(0.1)
    
    print(f"  OpenAlex author ID: {best_id}")
    print(f"  Total papers with year: {sum(year_counter.values())}")
    print(f"  Year range: {min(year_counter)} - {max(year_counter)}")
    print(f"\n  By decade:")
    decades = Counter()
    for yr, cnt in year_counter.items():
        decades[f"{yr//10*10}s"] += cnt
    for decade in sorted(decades):
        print(f"    {decade}: {decades[decade]} papers")


# ═══════════════════════════════════════════════════════════════
# TEST 3: DOI reverse lookup false positive rate
# ═══════════════════════════════════════════════════════════════
print("\n\n" + "=" * 70)
print("TEST 3: DOI reverse lookup → false positive author discovery")
print("=" * 70)

for collection, display_name, surname in [
    ("Ping Wang", "Ping Wang", "wang"),
    ("Dan Fu", "Dan Fu", "fu"),
    ("Ji-Xin Cheng", "Ji-Xin Cheng", "cheng"),
]:
    print(f"\n--- {display_name} (surname={surname}) ---")
    zotero_dois = get_zotero_dois(collection)
    # Use MORE DOIs (30) for better stats
    sample_dois = list(zotero_dois)[:30]
    author_data = openalex_doi_reverse_lookup(set(sample_dois))
    
    # Find all author IDs matching surname + initial
    given_initial = display_name[0].lower()
    author_counter = Counter()
    author_names = {}
    author_insts = {}
    matched_dois = {}
    
    for doi, authors in author_data.items():
        for au in authors:
            name_parts = au["name"].lower().split()
            # Check family name match (last name)
            if name_parts and surname in name_parts[-1]:
                # Check given initial
                given = name_parts[0] if len(name_parts) > 1 else ""
                if given.startswith(given_initial) or given_initial in "".join(name_parts[:-1]):
                    author_counter[au["id"]] += 1
                    author_names[au["id"]] = au["name"]
                    author_insts[au["id"]] = au["institutions"]
                    matched_dois.setdefault(au["id"], []).append(doi)
    
    total_matched = sum(author_counter.values())
    print(f"  DOIs queried: {len(sample_dois)}")
    print(f"  Author matches (surname+initial): {total_matched} across {len(author_counter)} unique IDs")
    print()
    
    for aid, count in author_counter.most_common(10):
        name = author_names.get(aid, "?")
        insts = author_insts.get(aid, [])
        matched = matched_dois.get(aid, [])
        # Estimate overlap with FULL Zotero
        full_overlap = len(set(matched) & zotero_dois)
        print(f"  {aid}: {name}")
        print(f"    Matched {count}/{len(sample_dois)} sampled | institutions: {insts[:2]}")
    
    time.sleep(1)

print("\n\nDone!")
