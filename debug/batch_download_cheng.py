#!/usr/bin/env python
"""Batch import + download for Cheng audit DOIs."""
import sys, os, time
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from io import StringIO
from rich.console import Console
console = Console()

from lit.discover.import_ref import run as import_run
from lit.batch.quick import run_single as quick_single
from lit.batch.attach import run_single as attach_single

# Suppress tracker console
import lit.core.zotero as zot
if hasattr(zot, 'console'):
    zot.console.file = StringIO()

DOIS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cheng_audit_dois.txt")
with open(DOIS_FILE, "r") as f:
    dois = [line.strip() for line in f if line.strip()]

print(f"Processing {len(dois)} DOIs...\n", flush=True)

ok = 0
fail = 0
for i, doi in enumerate(dois):
    print(f"[{i+1}/{len(dois)}] {doi}", flush=True)
    try:
        result = import_run(doi)
        if not result.get("item_key"):
            print(f"  import failed", flush=True)
            fail += 1
            continue

        item_key = result["item_key"]
        qr = quick_single(result.get("doi", doi), item_key=item_key)
        if qr and qr["status"] in ("attached", "already_has"):
            print(f"  quick OK", flush=True)
            ok += 1
        else:
            ar = attach_single(result.get("doi", doi), item_key=item_key)
            if ar and ar["status"] in ("attached", "already_has"):
                print(f"  attach OK", flush=True)
                ok += 1
            else:
                print(f"  download failed", flush=True)
                fail += 1
    except Exception as e:
        print(f"  error: {e}", flush=True)
        fail += 1

print(f"\nDone: {ok} ok, {fail} failed out of {len(dois)}", flush=True)
