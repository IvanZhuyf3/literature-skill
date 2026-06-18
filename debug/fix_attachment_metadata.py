"""Patch existing attachment items to add proper filename, md5, mtime fields."""
import hashlib
import json
import requests
from pathlib import Path

# Config
api_key = "XK3rOEGEyrRq4rxs4VrbcPB8"
user_id = 8856385
storage = Path(r"C:/Users/Ivanz/Zotero/storage")
headers = {"Zotero-API-Key": api_key, "Content-Type": "application/json"}

papers_path = Path(
    r"C:/Users/Ivanz/OneDrive/Hermes_workspace/Literature_skill"
    "/people/data/Ji_Xin_Cheng_papers.json"
)
d = json.load(open(papers_path, encoding="utf-8"))

fixed = 0
skipped = 0
failed = 0

for p in d["papers"]:
    att_key = p.get("attachment_key")
    if not att_key:
        continue
    att_dir = storage / att_key
    if not att_dir.exists():
        continue
    pdfs = list(att_dir.glob("*.pdf"))
    if not pdfs:
        continue
    pdf_path = pdfs[0]
    filename = pdf_path.name

    # Compute md5 + mtime
    md5_hash = hashlib.md5()
    with open(pdf_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            md5_hash.update(chunk)
    mtime_ts = int(pdf_path.stat().st_mtime)

    # Fetch current item
    r = requests.get(
        f"https://api.zotero.org/users/{user_id}/items/{att_key}",
        headers=headers,
    )
    if r.status_code != 200:
        print(f"FETCH FAIL {att_key}: HTTP {r.status_code}")
        failed += 1
        continue

    item = r.json()
    version = item["version"]
    current_data = item["data"]

    if current_data.get("filename"):
        print(f"SKIP {att_key}: already has filename")
        skipped += 1
        continue

    # PATCH
    new_data = dict(current_data)
    new_data["filename"] = filename
    new_data["md5"] = md5_hash.hexdigest()
    new_data["mtime"] = mtime_ts

    patch_headers = dict(headers)
    patch_headers["If-Unmodified-Since-Version"] = str(version)

    r = requests.patch(
        f"https://api.zotero.org/users/{user_id}/items/{att_key}",
        headers=patch_headers,
        json=new_data,
    )
    if r.status_code == 200:
        print(f"FIXED {att_key}: {filename}")
        fixed += 1
    else:
        print(f"PATCH FAIL {att_key}: HTTP {r.status_code} - {r.text[:100]}")
        failed += 1

print(f"\nDone: {fixed} fixed, {skipped} skipped, {failed} failed")
