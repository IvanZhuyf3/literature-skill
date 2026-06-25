#!/usr/bin/env python
"""
Daily tracker: run find_new_papers for all tracked authors SEQUENTIALLY.
Cron script-only (no_agent=True): stdout = delivered verbatim, empty = SILENT.

Output contract:
  - All high → [SILENT] (empty stdout). Cron agent auto-imports+downloads.
  - Any low  → Output low-confidence papers as structured text for human review.
  - No new papers → [SILENT].

Usage: python scripts/track_all.py
"""
import sys
import os
os.environ.setdefault("PYTHONIOENCODING", "utf-8")

# Ensure parent dir (containing lit/) is on path
_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

# Suppress rich console output (cron context)
from io import StringIO
import lit.discover.tracker as tr

# Redirect tracker's console to suppress debug logs
tr.console.file = StringIO()

# Dynamically scan people/ for all tracked authors
from pathlib import Path
people_dir = Path(__file__).resolve().parent.parent / "people"
AUTHORS = sorted(
    d.name
    for d in people_dir.iterdir()
    if d.is_dir() and (d / "profile.json").exists()
)

high_papers = {}   # author -> [papers]
low_papers = {}    # author -> [papers]

for author in AUTHORS:
    try:
        new = tr.find_new_papers(author)
        if not new:
            continue
        for p in new:
            bucket = low_papers if p.get("confidence") == "low" else high_papers
            bucket.setdefault(author, []).append(p)
    except Exception:
        # Errors are silent — retry next tick
        pass

# Auto-process high-confidence papers: import + download
if high_papers:
    try:
        from lit.discover.import_ref import run as import_run
        from lit.batch.quick import run_single as quick_single
        from lit.batch.attach import run_single as attach_single
        from lit.core.zotero import attach_to_collection, find_collection

        for author, papers in high_papers.items():
            # Resolve collection for auto-assignment
            coll_name = author.replace("_", " ")
            coll_key = find_collection(coll_name)

            for p in papers:
                doi = p["doi"]
                try:
                    result = import_run(doi)
                    ik = result.get("item_key")
                    if not ik:
                        continue
                    qr = quick_single(doi, item_key=ik)
                    if not (qr and qr["status"] in ("attached", "already_has")):
                        attach_single(doi, item_key=ik)
                except Exception:
                    pass  # download failure is non-fatal
    except Exception:
        pass  # import/download infrastructure not available in cron env

# Only output if we have low-confidence papers for human review
if not low_papers:
    sys.exit(0)  # [SILENT]

lines = ["⚠️ Low-confidence papers need review:\n"]
for author, papers in low_papers.items():
    name = author.replace("_", " ")
    lines.append(f"\n【{name}】{len(papers)} suspicious:")
    for p in papers:
        doi = p["doi"]
        src = p["source"]
        lines.append(f"  [{src}] {doi}")
    lines.append("  (CrossRef affiliation does not match known_affiliations)")
lines.append("")
print("\n".join(lines))
