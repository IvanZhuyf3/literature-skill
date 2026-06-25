#!/usr/bin/env python
"""
Daily tracker: run find_new_papers for all tracked authors SEQUENTIALLY.
Cron script-only (no_agent=True): stdout = delivered verbatim, empty = SILENT.

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
results = {}

for author in AUTHORS:
    try:
        new = tr.find_new_papers(author)
        if new:
            results[author] = new
    except Exception as e:
        # Errors are silent — retry next tick
        pass

# Only output if we found something (empty stdout = SILENT)
if not results:
    sys.exit(0)

lines = ["📚 New papers detected:\n"]
for author, papers in results.items():
    # Pretty name: Ji-Xin_Cheng → Ji-Xin Cheng
    name = author.replace("_", " ")
    lines.append(f"\n【{name}】{len(papers)} new:")
    for p in papers:
        doi = p["doi"]
        src = p["source"]
        lines.append(f"  [{src}] {doi}")
lines.append("")
print("\n".join(lines))
