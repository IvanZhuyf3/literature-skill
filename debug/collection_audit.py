"""
Collection audit: find false positive papers in each person's Zotero collection.
For each paper, check if the target author's institution matches known_affiliations.
"""
import json, sqlite3, shutil, tempfile, os, sys, time, requests
from collections import defaultdict

# Add lit to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lit.discover.tracker import (
    _openalex_batch_affiliations, _normalize_family, _match_author_in_authorships
)

SKILL_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEOPLE_DIR = os.path.join(SKILL_BASE, "people")

_OA_HEADERS = {"User-Agent": "lit-skill/1.0 (mailto:research@example.com)"}


def get_collection_papers(collection_name):
    """Get all DOIs + item keys from a Zotero collection."""
    src = r"C:\Users\Ivanz\Zotero\zotero.sqlite"
    tmp = os.path.join(tempfile.gettempdir(), "zotero_audit.sqlite")
    shutil.copy2(src, tmp)
    conn = sqlite3.connect(tmp)
    try:
        rows = conn.execute("""
            SELECT DISTINCT ci.itemID, i.key, idv.value, idv2.value
            FROM collectionItems ci
            JOIN collections c ON ci.collectionID = c.collectionID
            JOIN items i ON ci.itemID = i.itemID
            JOIN itemData id ON ci.itemID = id.itemID
            JOIN fields f ON id.fieldID = f.fieldID
            JOIN itemDataValues idv ON id.valueID = idv.valueID
            LEFT JOIN itemData id2 ON ci.itemID = id2.itemID
            LEFT JOIN fields f2 ON id2.fieldID = f2.fieldID
            LEFT JOIN itemDataValues idv2 ON id2.valueID = idv2.valueID
            WHERE c.collectionName = ? AND f.fieldName = 'DOI'
              AND f2.fieldName = 'date'
        """, (collection_name,)).fetchall()
    finally:
        conn.close()
    os.unlink(tmp)

    papers = []
    for row in rows:
        item_id = row[0]
        key = row[1]
        doi = row[2].lower().strip()
        date_str = row[3] or ""
        year = date_str[:4] if date_str[:4].isdigit() else "?"
        papers.append({"doi": doi, "year": year, "key": key, "item_id": item_id})
    return papers


def audit_person(author_dir):
    """Audit one person's collection."""
    prof_path = os.path.join(PEOPLE_DIR, author_dir, "profile.json")
    with open(prof_path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    name = profile.get("name", author_dir)
    collection = profile.get("zotero_collection", name)
    known_affiliations = profile.get("known_affiliations", [])

    # Parse family name
    parts = name.rsplit(None, 1)
    if len(parts) == 2:
        family_name = parts[1]
        given_initial = parts[0][0] if parts[0] else None
    else:
        family_name = name
        given_initial = None

    print(f"\n{'='*70}")
    print(f"  AUDIT: {name} ({author_dir})")
    print(f"  family={family_name}, initial={given_initial}")
    print(f"  known_affiliations: {known_affiliations}")
    print(f"{'='*70}")

    papers = get_collection_papers(collection)
    print(f"  Total papers in collection: {len(papers)}")

    if not papers:
        return

    # Batch query OpenAlex
    all_dois = [p["doi"] for p in papers]
    print(f"  Batch querying OpenAlex ({len(all_dois)} DOIs)...")

    # Need to also get full authorship data for checking
    # Use batch API, but we need to check the raw authorship
    results = {}  # doi -> {found: bool, institutions: list, all_institutions: list}
    batch_size = 50

    for i in range(0, len(all_dois), batch_size):
        batch = all_dois[i:i+batch_size]
        doi_filter = "|".join(batch)
        try:
            resp = requests.get(
                "https://api.openalex.org/works",
                params={"filter": f"doi:{doi_filter}", "per-page": batch_size},
                headers=_OA_HEADERS,
                timeout=30,
            )
            if resp.status_code != 200:
                print(f"    Batch {i}: HTTP {resp.status_code}")
                time.sleep(0.5)
                continue
        except Exception as e:
            print(f"    Batch {i}: ERROR {e}")
            continue

        for w in resp.json().get("results", []):
            doi = (w.get("doi") or "").replace("https://doi.org/", "").lower().strip()
            if doi not in {d.lower() for d in batch}:
                continue
            authorships = w.get("authorships", [])
            insts = _match_author_in_authorships(authorships, family_name, given_initial)
            results[doi] = insts

        time.sleep(0.2)

    print(f"  OpenAlex returned data for {len(results)}/{len(all_dois)} DOIs")

    # Classify each paper
    confirmed = []
    suspect = []
    uncertain = []

    known_lower = [a.lower() for a in known_affiliations]

    for p in papers:
        doi = p["doi"]
        insts = results.get(doi)

        if insts is None:
            # OpenAlex didn't return this DOI → uncertain
            uncertain.append(p)
        elif len(insts) == 0:
            # Target author not found in author list at all → very suspicious
            suspect.append({**p, "reason": "author not found", "institutions": []})
        else:
            # Check if any institution matches
            insts_lower = [i.lower() for i in insts]
            matched = False
            for inst_lower in insts_lower:
                for known in known_lower:
                    if known in inst_lower or inst_lower in known:
                        matched = True
                        break
                if matched:
                    break
            if matched:
                confirmed.append(p)
            else:
                suspect.append({**p, "reason": "institution mismatch", "institutions": insts})

    # Report
    print(f"\n  Results:")
    print(f"    ✓ CONFIRMED (matches known affiliation): {len(confirmed)}")
    print(f"    ⚠ SUSPECT (likely false positive):       {len(suspect)}")
    print(f"    ? UNCERTAIN (no OpenAlex data):          {len(uncertain)}")

    if suspect:
        print(f"\n  ── SUSPECT papers (recommend remove from collection) ──")
        for p in sorted(suspect, key=lambda x: x.get("year", ""), reverse=True):
            inst_str = ", ".join(p["institutions"]) if p["institutions"] else "(none)"
            print(f"    {p['year']} | {p['doi'][:45]:45s} | key={p['key']:8s} | {p['reason']}")
            print(f"         institutions: {inst_str}")

    if uncertain:
        print(f"\n  ── UNCERTAIN (no data, manual check needed) ──")
        for p in sorted(uncertain, key=lambda x: x.get("year", ""), reverse=True)[:10]:
            print(f"    {p['year']} | {p['doi'][:45]:45s} | key={p['key']:8s}")
        if len(uncertain) > 10:
            print(f"    ... and {len(uncertain) - 10} more")

    return {
        "author": name,
        "total": len(papers),
        "confirmed": len(confirmed),
        "suspect": suspect,
        "uncertain_count": len(uncertain),
    }


# Run audit for all people
all_results = []
for name in sorted(os.listdir(PEOPLE_DIR)):
    full = os.path.join(PEOPLE_DIR, name)
    if not os.path.isdir(full) or name in ("data", "digests"):
        continue
    if not os.path.exists(os.path.join(full, "profile.json")):
        continue
    result = audit_person(name)
    if result:
        all_results.append(result)
    time.sleep(1)

# Summary
print(f"\n\n{'='*70}")
print(f"  AUDIT SUMMARY")
print(f"{'='*70}")
total_suspect = 0
for r in all_results:
    n_suspect = len(r["suspect"])
    total_suspect += n_suspect
    print(f"  {r['author']:<25s} | {r['total']:>4d} papers | ✓{r['confirmed']:>4d} | ⚠{n_suspect:>3d} | ?{r['uncertain_count']:>3d}")
print(f"\n  Total suspect papers to review: {total_suspect}")

# Save suspect list for removal
suspect_output = []
for r in all_results:
    for p in r["suspect"]:
        suspect_output.append({
            "author": r["author"],
            "doi": p["doi"],
            "key": p["key"],
            "year": p["year"],
            "reason": p["reason"],
            "institutions": p["institutions"],
        })

with open(os.path.join(SKILL_BASE, "debug", "audit_suspect.json"), "w") as f:
    json.dump(suspect_output, f, indent=2, ensure_ascii=False)
print(f"\n  Suspect list saved to debug/audit_suspect.json")
