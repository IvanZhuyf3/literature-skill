"""
debug/backfill_attach.py — 批量把已下载但未入库的 PDF 挂到 Zotero。

匹配 temp/ 中的 PDF → JSON 中的 DOI → Zotero item_key → attach_pdf()。
"""
import json
import sys
from pathlib import Path

# Skill base
SKILL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL))

from lit.core.zotero import attach_pdf


def main():
    papers_path = SKILL / "people" / "data" / "Ji_Xin_Cheng_papers.json"
    temp_dir = Path(r"C:/Users/Ivanz/Downloads/temp")

    d = json.load(open(papers_path, encoding="utf-8"))
    papers_by_doi = {}
    for p in d["papers"]:
        if p.get("doi"):
            papers_by_doi[p["doi"]] = p

    pdfs = sorted(temp_dir.glob("*.pdf"), key=lambda x: x.stat().st_mtime, reverse=True)

    matched = []
    for pdf in pdfs:
        name = pdf.stem.lower()
        best = None
        best_score = 0
        for doi, p in papers_by_doi.items():
            title = (p.get("title", "") or "").lower()
            if not title:
                continue
            name_words = set(name[:80].split())
            title_words = set(title[:80].split())
            overlap = len(name_words & title_words)
            if overlap > best_score:
                best_score = overlap
                best = (doi, p)
        if best and best_score >= 3:
            doi, p = best
            zkey = p.get("zotero_key", "")
            has_att = bool(p.get("attachment_key"))
            if zkey and not has_att:
                matched.append((pdf, doi, zkey, p))

    print(f"Total to attach: {len(matched)}")
    print()

    success = 0
    failed = 0
    for i, (pdf, doi, zkey, p) in enumerate(matched):
        title = (p.get("title", "") or "")[:50]
        try:
            att_key = attach_pdf(zkey, pdf)
            # Update JSON
            p["attachment_key"] = att_key
            print(f"  [{i+1}/{len(matched)}] ✅ {title}")
            success += 1
        except Exception as e:
            print(f"  [{i+1}/{len(matched)}] ❌ {title}: {e}")
            failed += 1

    # Save updated JSON
    json.dump(d, open(papers_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"\nDone: {success} attached, {failed} failed")


if __name__ == "__main__":
    main()
