"""
Remove suspect papers from each person's Zotero collection.
Items stay in the library (NOT deleted), just removed from the collection.
They'll appear in Unfiled for manual review.
"""
import json, os, sys, requests, sqlite3, shutil, tempfile

# Add lit to path
SKILL_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SKILL_BASE)
from lit.core.config import load as load_config

config = load_config()
LIBRARY_ID = str(config.get("zotero", {}).get("library_id", ""))
API_KEY = config.get("zotero", {}).get("api_key", "")
BASE_URL = f"https://api.zotero.org/users/{LIBRARY_ID}"

HEADERS = {
    "Zotero-API-Key": API_KEY,
    "Content-Type": "application/json",
}

print(f"Zotero library: {LIBRARY_ID}")


def get_collection_key(collection_name):
    """Find collection key by name via Zotero API."""
    # Fetch all collections (paginated)
    start = 0
    while True:
        resp = requests.get(
            f"{BASE_URL}/collections",
            params={"limit": 100, "start": start},
            headers=HEADERS,
            timeout=15,
        )
        if resp.status_code != 200:
            print(f"    Collections API error: {resp.status_code}")
            return None
        data = resp.json()
        results = data if isinstance(data, list) else data.get("results", [])
        if not results:
            return None
        for c in results:
            if c["data"]["name"] == collection_name:
                return c["data"]["key"]
        # Check if more pages
        total = int(resp.headers.get("Total-Results", len(results)))
        start += len(results)
        if start >= total:
            return None


def remove_from_collection(collection_key, item_keys):
    """Remove items from a collection via Zotero API.

    Uses PATCH to update each item's 'collections' field, removing the
    target collection key. This is the reliable way — DELETE endpoint
    often returns 500.
    """
    removed = 0
    failed = 0

    for item_key in item_keys:
        # 1. Fetch the item's current data
        resp = requests.get(
            f"{BASE_URL}/items/{item_key}",
            headers=HEADERS,
            timeout=15,
        )
        if resp.status_code != 200:
            failed += 1
            continue

        data = resp.json()["data"]
        current_collections = data.get("collections", [])

        # 2. Remove target collection key
        if collection_key not in current_collections:
            # Already not in collection
            removed += 1
            continue

        new_collections = [c for c in current_collections if c != collection_key]

        # 3. PATCH with updated collections
        version = resp.headers.get("Last-Modified-Version", str(data.get("version", 0)))
        patch_headers = {**HEADERS, "If-Unmodified-Since-Version": version}

        patch_resp = requests.patch(
            f"{BASE_URL}/items/{item_key}",
            json={"collections": new_collections},
            headers=patch_headers,
            timeout=15,
        )
        if patch_resp.status_code in (200, 204):
            removed += 1
        else:
            print(f"    PATCH {item_key}: HTTP {patch_resp.status_code}")
            failed += 1

    return removed, failed


# Load suspect list
suspect_path = os.path.join(SKILL_BASE, "debug", "audit_suspect.json")
with open(suspect_path, "r", encoding="utf-8") as f:
    suspects = json.load(f)

print(f"Total suspect papers: {len(suspects)}")

# Group by author
from collections import defaultdict
by_author = defaultdict(list)
for s in suspects:
    by_author[s["author"]].append(s)

# Cache collection keys
PEOPLE_DIR = os.path.join(SKILL_BASE, "people")
collection_cache = {}

total_removed = 0
total_kept = 0

for author, items in sorted(by_author.items()):
    # Find author dir name
    author_dir = None
    for d in os.listdir(PEOPLE_DIR):
        prof = os.path.join(PEOPLE_DIR, d, "profile.json")
        if not os.path.exists(prof):
            continue
        with open(prof) as f:
            p = json.load(f)
        if p.get("name") == author:
            author_dir = d
            collection_name = p.get("zotero_collection", author)
            break

    if not author_dir:
        print(f"\n  {author}: no profile found, skipping")
        continue

    # Get collection key
    if collection_name not in collection_cache:
        ck = get_collection_key(collection_name)
        collection_cache[collection_name] = ck
        print(f"\n  Collection '{collection_name}' → key={ck}")
    else:
        ck = collection_cache[collection_name]

    if not ck:
        print(f"  {author}: collection key not found!")
        continue

    # Categorize items
    si_items = [s for s in items if ".s00" in s["doi"]]
    mismatch_items = [s for s in items if s["reason"] == "institution mismatch"]
    not_found_items = [s for s in items if s["reason"] == "author not found"]

    print(f"\n  {author} ({len(items)} suspect):")
    print(f"    supplementary (.s00*): {len(si_items)}")
    print(f"    institution mismatch:  {len(mismatch_items)}")
    print(f"    author not found:      {len(not_found_items)}")

    # Remove ALL suspect items from collection
    all_keys = [s["key"] for s in items if s["key"]]
    if all_keys:
        n, fail = remove_from_collection(ck, all_keys)
        print(f"    → Removed {n} items from collection '{collection_name}'" + (f" ({fail} failed)" if fail else ""))
        total_removed += n
    else:
        print(f"    → No item keys available")

    # Print details for user reference
    if mismatch_items:
        print(f"\n    ── Institution mismatch (most likely false positive) ──")
        for s in mismatch_items:
            inst = ", ".join(s["institutions"])[:60]
            print(f"      {s['year']} | {s['doi'][:45]:45s} | {inst}")

    if si_items:
        print(f"\n    ── Supplementary materials (not real papers) ──")
        for s in si_items:
            print(f"      {s['year']} | {s['doi'][:45]}")

print(f"\n\n{'='*60}")
print(f"  TOTAL: {total_removed} items removed from collections")
print(f"  Items are still in the Zotero library (check Unfiled)")
print(f"{'='*60}")

# Save a manifest for user reference
manifest_path = os.path.join(SKILL_BASE, "debug", "audit_removed_manifest.json")
manifest = defaultdict(list)
for s in suspects:
    manifest[s["author"]].append({
        "doi": s["doi"],
        "year": s["year"],
        "key": s["key"],
        "reason": s["reason"],
        "institutions": s.get("institutions", []),
    })

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(dict(manifest), f, indent=2, ensure_ascii=False)
print(f"\n  Removal manifest saved to debug/audit_removed_manifest.json")
