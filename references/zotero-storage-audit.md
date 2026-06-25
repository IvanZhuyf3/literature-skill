# Zotero WebDAV Storage Audit

> Systematic methodology for detecting ghost attachments, broken PDFs, and orphan directories after batch operations go wrong.
>
> **Automated**: `lit maintain` command implements this entire workflow. See `lit/maintain.py`.
> Manual methodology below for understanding and edge cases.

## When to Run

- After bulk attach/download operations that may have partially failed
- After manual cleanup (user deleted "messed up" PDFs)
- Before resuming cron batch downloads (ensure clean baseline)
- Periodic health check for large collections (500+ items)

```bash
# Quick full-library alignment check (seconds)
python -m lit maintain

# Full per-item health check for one collection
python -m lit maintain --collection "Ji-Xin Cheng"

# Fix issues (orphans → recycle bin, ghosts → Zotero delete)
python -m lit maintain --fix

# Preview what --fix would do
python -m lit maintain --fix --dry-run
```

## Problem 1: Attachment Health Check (per-collection)

### ⚠️ Performance: use batch query, NOT per-item `children()`

**Never use `z.children(key)` in a loop for 100+ items** — it's one API call per parent and will timeout at 300s for a 500-item collection.

**Batch approach** (used by `lit maintain`): fetch all attachments in one paginated call:

```python
import os, yaml
from pyzotero import zotero as zotero_mod

cfg = yaml.safe_load(open('config.yaml'))['zotero']
z = zotero_mod.Zotero(cfg['library_id'], 'user', cfg['api_key'])
storage = cfg['storage_path']
COLLECTION_KEY = '4XXVA5CR'

# ONE paginated call for all attachments (vs N children() calls)
atts = z.everything(z.collection_items(COLLECTION_KEY, itemType="attachment"))
# Also fetch top-level items for title lookup
top_items = z.everything(z.collection_items(COLLECTION_KEY, itemType="-attachment"))
parent_titles = {i["key"]: i["data"].get("title","")[:50] for i in top_items}

for child in atts:
    d = child["data"]
    if d.get("itemType") != "attachment":
        continue
    if d.get("linkMode","") not in ("imported_file", "imported_url"):
        continue

    att_key = child["key"]
    parent_key = d.get("parentItem", "")
    rec_fn = d.get("filename", "")
    dir_path = os.path.join(storage, att_key)

    # 4-point check:
    # 1. storage/{att_key}/ exists?  → ghost if missing
    # 2. contains a .pdf?           → empty shell if not
    # 3. filename field present?     → patch if missing
    # 4. actual PDF name == rec_fn?  → mismatch if different
```

This turns a 500-call O(N) operation into a ~5-call paginated fetch — **60x faster**.

### Categories

| Status | Meaning | Action |
|--------|---------|--------|
| Ghost | Zotero has att item, `storage/{att_key}/` missing | Delete ghost att item from Zotero |
| Empty shell | Dir exists but no PDF inside | Delete att item + empty dir |
| Filename mismatch | PDF exists but name != `filename` field | PATCH att item with correct filename |
| No filename field | `filename` empty or absent | PATCH att item |
| Healthy | All 4 checks pass | No action |

### Fix: Delete ghost attachment

```python
item = z.item(att_key)  # MUST fetch first to get version
z.delete_item(item)     # needs version-tagged item, not bare key
```

### Fix: PATCH filename

```python
patch = {'filename': actual_pdf_name}
z.patch_item(att_key, patch)  # returns 204 on success
```

## Problem 2: Orphan Directory Detection (library-wide)

Find `storage/` directories with no corresponding Zotero attachment item — leftovers from failed batch operations.

```python
# Step 1: Get ALL attachment keys from Zotero API
all_att_keys = set()
start = 0
while True:
    result = z.items(itemType='attachment', limit=100, start=start)
    if not result or len(result) < 100:
        all_att_keys.update(i['key'] for i in result
                           if i['data'].get('linkMode','') in ('imported_file','imported_url'))
        break
    all_att_keys.update(i['key'] for i in result
                       if i['data'].get('linkMode','') in ('imported_file','imported_url'))
    start += 100

# Step 2: List storage dirs
storage_dirs = {d for d in os.listdir(storage) if os.path.isdir(os.path.join(storage, d))}

# Step 3: Compute difference
orphans = storage_dirs - all_att_keys        # dirs with no Zotero entry
ghosts  = all_att_keys - storage_dirs         # Zotero entries with no dir
valid   = storage_dirs & all_att_keys         # all good
```

### Orphan Recovery vs Deletion

Orphan dirs often contain valid PDFs (batch scripts created the dir + downloaded the PDF, but Zotero item creation failed or was later deleted). **Check before deleting:**

```python
for d in sorted(orphans):
    full = os.path.join(storage, d)
    files = os.listdir(full)
    pdfs = [f for f in files if f.endswith('.pdf')]
    size_mb = sum(os.path.getsize(os.path.join(full, f)) for f in files) / 1024 / 1024
    # orphan_with_pdf → try to recover (match to parent item by title/DOI)
    # orphan_empty → safe to delete
```

**Recovery strategy**: Match orphan PDF filename to a Zotero item by DOI or title substring, then create a new attachment via `_attach_webdav()` pointing to the existing PDF (copy into correct `{att_key}/` if the key differs).

### ⚠️ Orphan recovery pitfall: search returns attachment items

When matching orphan PDFs to Zotero items via `z.items(q="title keywords")`, **the search returns ALL item types including attachments**. Attachment items have `title` = PDF filename ≈ paper title, so they appear in results. Using an attachment key as `parentItem` causes:

```
{'0': {'code': 400, 'message': 'Parent item XXXX cannot be a child item'}}
```

**Fix**: Always check `itemType` of search results. If it's `attachment`, resolve through `data.parentItem` to get the real journal article key:

```python
for result in z.items(q=query, limit=5):
    itype = result['data'].get('itemType')
    if itype == 'attachment':
        real_parent = result['data'].get('parentItem')  # resolve to journal article
    else:
        real_parent = result['key']  # already a top-level item
```

### ⚠️ Common pattern: orphans are ALL duplicates

In practice (observed in 2026-06-17 Cheng cleanup, 25/25 orphans), orphan directories from batch operations are almost always **redundant copies** — the parent item already has a working attachment under a different key. The batch script created the dir + downloaded the PDF, then a separate successful attach created a second (working) attachment, leaving the orphan behind.

**Before attempting recovery**: check each orphan's target parent for existing working attachments. If the parent already has a PDF in `storage/{other_key}/`, the orphan is a duplicate → delete the directory instead of attaching. This avoids creating yet another redundant attachment.

**Deletion strategy**: Only delete empty orphan dirs or dirs where PDFs are confirmed redundant (already attached under a different key). Use safe-delete (recycle bin), not `rm -rf`.

## Key Gotchas

- **⚠️ Never loop `z.children(key)` for bulk checks** — it's O(N) API calls and will timeout at 300s for 500+ items. Use `z.collection_items(key, itemType="attachment")` for a single paginated fetch instead. `lit maintain` already uses this pattern.
- **Full-library per-item check is impractical** — only do per-item attachment health for `--collection` scope. Full-library mode (`lit maintain` without `--collection`) does only the fast set-difference alignment check (orphan dirs + ghost entries), which completes in seconds for 2000+ items.
- Zotero API `delete_item()` needs a version-tagged item object, not a bare key string. Always `z.item(key)` first.
- `patch_item` returns HTTP **204** (not 200) for success.
- pyzotero has **no `patch_attachment()` method**. Use `z.update_item(item_dict)` (PUT, full replace — read item first, modify, write back) or raw `requests.patch()` to the REST API for partial updates.
- When deleting multiple orphan dirs, use `send2trash` (recycle bin), not `rm -rf` — user preference for safe deletion.
- Orphan dir names look like valid Zotero keys (8-char uppercase) — they were assigned keys during batch creation, just never persisted to the API.
- When user says "I deleted the messed-up PDFs," assume both ghost attachments AND orphan dirs may exist — run both checks.
- **Most orphans are duplicates** (observed 25/25 in Cheng cleanup): batch operations that partially succeeded leave behind PDF copies whose parent items already have working attachments under different keys. Always verify redundancy before attempting recovery.
