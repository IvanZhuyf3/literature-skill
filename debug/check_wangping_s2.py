"""Check which S2 profiles are real Ping Wang by looking at his Zotero DOIs."""
import requests, json, time, sqlite3, shutil, tempfile, os

# 1. Get all DOIs from Wang Ping's Zotero collection
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
    WHERE c.collectionName = 'Ping Wang' AND f.fieldName = 'DOI'
""").fetchall()
conn.close()
os.unlink(tmp)

zotero_dois = set(r[0].lower().strip() for r in rows if r[0])
print(f"Zotero collection DOIs: {len(zotero_dois)}")

# 2. For each S2 profile, check what % of its papers overlap with Zotero
s2_profiles = {
    "2152209297": "Ping Wang (16 co-authored)",
    "2152207049": "Ping Wang (5 co-authored)",
    "2108269067": "Pu Wang (4 co-authored)",
    "2152209329": "Ping Wang (1 co-authored)",
    "2152209499": "Ping Wang (1 co-authored)",
}

for s2_id, label in s2_profiles.items():
    try:
        # Get all papers for this profile
        all_dois = set()
        offset = 0
        while True:
            resp = requests.get(
                f"https://api.semanticscholar.org/graph/v1/author/{s2_id}/papers",
                params={"fields": "externalIds", "offset": offset, "limit": 500},
                timeout=30,
            )
            if resp.status_code == 429:
                print(f"  {s2_id}: rate limited, sleeping 5s...")
                time.sleep(5)
                continue
            if resp.status_code != 200:
                print(f"  {s2_id} ({label}): HTTP {resp.status_code}")
                break
            data = resp.json()
            papers = data.get("data", [])
            if not papers:
                break
            for p in papers:
                ext = p.get("externalIds", {})
                doi = ext.get("DOI", "").lower().strip() if ext else ""
                if doi:
                    all_dois.add(doi)
            offset += len(papers)
            if offset >= data.get("total", 0):
                break
            time.sleep(1)

        overlap = all_dois & zotero_dois
        print(f"\n  {s2_id} ({label}):")
        print(f"    Total papers: {len(all_dois)}")
        print(f"    In Zotero: {len(overlap)}/{len(all_dois)} ({100*len(overlap)/max(len(all_dois),1):.0f}%)")
        if overlap:
            print(f"    Overlap sample: {list(overlap)[:3]}")
    except Exception as e:
        print(f"  {s2_id}: ERROR {e}")
    time.sleep(2)
