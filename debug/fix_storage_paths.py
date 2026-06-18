"""
Fix misplaced Zotero storage: move from storage/{filename}/{filename}
to storage/{att_key}/{filename}. Also fix mtime to milliseconds.
"""
import hashlib
import json
import shutil
from pathlib import Path

papers_path = Path(
    r"C:/Users/Ivanz/OneDrive/Hermes_workspace/Literature_skill"
    "/people/data/Ji_Xin_Cheng_papers.json"
)
storage = Path(r"C:/Users/Ivanz/Zotero/storage")

d = json.load(open(papers_path, encoding="utf-8"))

# Build att_key → paper mapping
att_map = {}
for p in d["papers"]:
    att_key = p.get("attachment_key")
    if att_key:
        att_map[att_key] = p

# Find all misplaced dirs (name doesn't match 8-char key pattern)
bad_dirs = []
for item in storage.iterdir():
    if not item.is_dir():
        continue
    name = item.name
    # Valid Zotero storage dirs are 8-char uppercase alphanumeric keys
    if len(name) == 8 and name.isupper() and name.isalnum():
        continue
    # This is a misplaced dir
    bad_dirs.append(item)

print(f"Found {len(bad_dirs)} misplaced directories")

# For each bad dir, find the PDF inside, match to att_key, move
fixed = 0
unmatched = 0

for bad_dir in bad_dirs:
    pdfs = list(bad_dir.glob("*.pdf"))
    if not pdfs:
        continue
    pdf = pdfs[0]
    filename = pdf.name

    # Find matching att_key by searching all papers
    matched_key = None
    for att_key, p in att_map.items():
        title = (p.get("title", "") or "")
        # The filename usually starts with the title
        if title and (filename.startswith(title[:30]) or title[:30].startswith(filename[:30])):
            matched_key = att_key
            break

    if not matched_key:
        # Try looser match
        fn_lower = filename.lower()[:40]
        for att_key, p in att_map.items():
            title = (p.get("title", "") or "").lower()[:40]
            if not title:
                continue
            # Word overlap
            fn_words = set(fn_lower.split())
            t_words = set(title.split())
            if len(fn_words & t_words) >= 3:
                matched_key = att_key
                break

    if not matched_key:
        print(f"  NO MATCH: {filename[:60]}")
        unmatched += 1
        continue

    # Move to correct location
    correct_dir = storage / matched_key
    if correct_dir.exists() and list(correct_dir.glob("*.pdf")):
        # Already has a PDF, just remove the bad dir
        shutil.rmtree(bad_dir)
        print(f"  ALREADY OK: {matched_key} — removed bad dir")
        fixed += 1
        continue

    correct_dir.mkdir(parents=True, exist_ok=True)
    dest = correct_dir / filename
    shutil.move(str(pdf), str(dest))
    shutil.rmtree(bad_dir)
    print(f"  FIXED: {matched_key} ← {filename[:50]}")
    fixed += 1

print(f"\nDone: {fixed} fixed, {unmatched} unmatched")

# Now fix mtime to milliseconds on all attachments via API
print("\n--- Fixing mtime to milliseconds ---")
import requests

api_key = "XK3rOEGEyrRq4rxs4VrbcPB8"
user_id = 8856385
headers = {"Zotero-API-Key": api_key, "Content-Type": "application/json"}

mtime_fixed = 0
for att_key, p in att_map.items():
    correct_dir = storage / att_key
    if not correct_dir.exists():
        continue
    pdfs = list(correct_dir.glob("*.pdf"))
    if not pdfs:
        continue
    pdf_path = pdfs[0]

    # Check if mtime needs fixing (fetch from API)
    r = requests.get(
        f"https://api.zotero.org/users/{user_id}/items/{att_key}",
        headers=headers,
    )
    if r.status_code != 200:
        continue
    item = r.json()
    version = item["version"]
    data = item["data"]
    current_mtime = data.get("mtime", 0)

    # If mtime is less than 10^12, it's in seconds, needs *1000
    if current_mtime and current_mtime < 1e12:
        # Also recompute md5 and mtime from actual file
        md5_hash = hashlib.md5()
        with open(pdf_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                md5_hash.update(chunk)
        new_mtime = int(pdf_path.stat().st_mtime * 1000)  # ms

        new_data = dict(data)
        new_data["mtime"] = new_mtime
        new_data["md5"] = md5_hash.hexdigest()

        patch_headers = dict(headers)
        patch_headers["If-Unmodified-Since-Version"] = str(version)

        r = requests.patch(
            f"https://api.zotero.org/users/{user_id}/items/{att_key}",
            headers=patch_headers,
            json=new_data,
        )
        if r.status_code in (200, 204):
            mtime_fixed += 1
        else:
            print(f"  MTIME FAIL {att_key}: HTTP {r.status_code}")

print(f"mtime fixed: {mtime_fixed}")
