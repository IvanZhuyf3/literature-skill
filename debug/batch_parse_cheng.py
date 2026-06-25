"""
Batch parse all Cheng PDFs -> Markdown via MinerU API.

Optimized: batch-fetch parent titles instead of per-item API calls.
"""
import os
import sys
import re
import time
import yaml
from pathlib import Path
from pyzotero import zotero as zotero_mod

SKILL_BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_BASE))

from lit.digest.parser import run as mineru_parse

cfg = yaml.safe_load(open(SKILL_BASE / "config.yaml"))["zotero"]
z = zotero_mod.Zotero(cfg["library_id"], "user", cfg["api_key"])
storage = cfg["storage_path"]
CHENG_KEY = "4XXVA5CR"
OUTPUT_DIR = SKILL_BASE / "people" / "Ji-Xin Cheng"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Step 1: Batch fetch parent titles (one API call, not 322)
print("Fetching Cheng items for titles...", flush=True)
top_items = z.everything(z.collection_items(CHENG_KEY, itemType="-attachment"))
parent_titles = {}
for item in top_items:
    parent_titles[item["key"]] = item["data"].get("title", "untitled")
print(f"Got {len(parent_titles)} parent titles", flush=True)

# Step 2: Get attachments with PDFs
atts = z.everything(z.collection_items(CHENG_KEY, itemType="attachment"))
print(f"Got {len(atts)} attachments", flush=True)

pdf_list = []
for att in atts:
    d = att["data"]
    if d.get("linkMode", "") not in ("imported_file", "imported_url"):
        continue
    att_key = att["key"]
    dir_path = os.path.join(storage, att_key)
    if not os.path.isdir(dir_path):
        continue
    pdfs = [f for f in os.listdir(dir_path) if f.endswith(".pdf")]
    if not pdfs:
        continue
    pdf_path = os.path.join(dir_path, pdfs[0])
    parent_key = d.get("parentItem", "")
    title = parent_titles.get(parent_key, pdfs[0].replace(".pdf", ""))
    safe_title = re.sub(r'[<>:"/\\|?*]', "", title)[:80].strip()
    out_path = OUTPUT_DIR / f"{safe_title}.md"
    pdf_list.append((pdf_path, out_path, safe_title))

print(f"PDFs with files: {len(pdf_list)}", flush=True)

# Step 3: Filter already done
already_done = [p for p in pdf_list if p[1].exists()]
todo = [p for p in pdf_list if not p[1].exists()]
print(f"Already parsed: {len(already_done)}", flush=True)
print(f"To parse: {len(todo)}", flush=True)

if not todo:
    print("All done already!", flush=True)
    sys.exit(0)

# Step 4: Parse each
ok = 0
skipped = 0
failed = 0
total = len(todo)
start_time = time.time()

for i, (pdf_path, out_path, title) in enumerate(todo):
    elapsed = time.time() - start_time
    eta = elapsed / (i + 1) * (total - i - 1) if i > 0 else 0
    print(f"\n[{i+1}/{total}] (~{eta:.0f}s remaining)", flush=True)
    print(f"  {title[:60]}", flush=True)

    try:
        md_content = mineru_parse(pdf_path)
        if md_content and len(md_content) > 100:
            out_path.write_text(md_content, encoding="utf-8")
            size_kb = len(md_content) / 1024
            print(f"  OK: {size_kb:.1f}KB -> {out_path.name}", flush=True)
            ok += 1
        else:
            print(f"  SKIP: empty/too short", flush=True)
            skipped += 1
    except Exception as e:
        print(f"  FAIL: {str(e)[:80]}", flush=True)
        failed += 1

    if (i + 1) % 10 == 0:
        print(f"\n--- {i+1}/{total} done (ok={ok} skip={skipped} fail={failed}) ---", flush=True)

elapsed_total = time.time() - start_time
print(f"\n{'='*60}", flush=True)
print(f"DONE: ok={ok} skip={skipped} fail={failed}", flush=True)
print(f"Time: {elapsed_total:.0f}s ({elapsed_total/60:.1f}min)", flush=True)
print(f"Total .md files: {len(list(OUTPUT_DIR.glob('*.md')))}", flush=True)
