"""
lit/digest/template.py — Digest template generator from Zotero data.

Adapted from people.py:generate_digest_template.
Reads paper data from a Zotero collection instead of from papers.json.

Usage:
    from lit.digest.template import run
    path = run("Ji-Xin Cheng", parent="People")
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from rich.console import Console

from lit.core.config import load as get_config, people as get_people_config
from lit.core.zotero import find_collection, collection_items_top
from lit.core.crossref import fetch_metadata

console = Console()


def _extract_year(date_str: str) -> str:
    """Extract year from a Zotero date string (e.g. '2023', '2023-06-15', 'June 2023')."""
    if not date_str:
        return ""
    m = re.search(r"(\d{4})", date_str)
    return m.group(1) if m else ""


def _format_authors(creators: list[dict]) -> str:
    """Format Zotero creators list into a comma-separated author string."""
    authors: list[str] = []
    for c in creators:
        if c.get("creatorType") in ("author", None):
            first = (c.get("firstName") or "").strip()
            last = (c.get("lastName") or "").strip()
            if first and last:
                authors.append(f"{first} {last}")
            elif last:
                authors.append(last)
    return ", ".join(authors)


def run(collection: str, parent: str = "People", output: str | None = None) -> str:
    """
    Generate a literature digest template from a Zotero collection.

    Args:
        collection: Collection name (e.g. "Ji-Xin Cheng").
        parent: Parent collection name (default "People").
        output: Custom output path (default: people/digests/<name>_digest.md).

    Returns:
        Path to the generated digest file.
    """
    # ── 1. Find collection ──
    console.print(f"\n[bold cyan]━━━ Phase 4: 文献消化模板 ━━━[/bold cyan]\n")
    console.print(f"  Looking up collection: [bold]{parent}/{collection}[/bold] ...")

    collection_key = find_collection(collection, parent)
    if not collection_key:
        console.print(
            f"[red]Collection '{parent}/{collection}' not found in Zotero.[/red]"
        )
        sys.exit(1)

    # ── 2. Read top-level items ──
    console.print(f"  Reading items from collection ...")
    items = collection_items_top(collection_key)
    if not items:
        console.print(
            f"[yellow]No items found in collection '{parent}/{collection}'.[/yellow]"
        )
        sys.exit(1)

    # ── 3. Extract paper metadata ──
    papers: list[dict] = []
    for item in items:
        data = item.get("data", {})
        if data.get("itemType") in ("attachment", "note"):
            continue

        doi = (data.get("DOI") or "").strip()
        title = (data.get("title") or "").strip()
        if not title:
            continue

        year = _extract_year(data.get("date") or "")
        creators = data.get("creators", [])
        authors_str = _format_authors(creators)
        journal = (data.get("publicationTitle") or data.get("publisher") or "").strip()

        # Citation count: fetched later only for Top 10 candidates
        citations = 0

        paper = {
            "title": title,
            "doi": doi,
            "year": year,
            "venue": journal,
            "authors": authors_str,
            "citations": citations,
            "zotero_key": item.get("key", ""),
        }
        papers.append(paper)

    console.print(f"  Extracted {len(papers)} papers from Zotero collection.\n")

    # ── 4. Sort by year ──
    def _year_sort_key(p: dict) -> int:
        y = p.get("year", "")
        return int(y) if y.isdigit() else 0

    papers_sorted = sorted(papers, key=_year_sort_key)

    # ── 5. Build template ──

    # Stats
    years = [int(p["year"]) for p in papers if p["year"].isdigit()]
    year_range = f"{min(years)}–{max(years)}" if years else "?"
    total = len(papers)

    # Compute digest dir
    people_cfg = get_people_config()
    default_digest_dir = Path(people_cfg["digest_dir"])
    default_digest_dir.mkdir(parents=True, exist_ok=True)

    safe_name = re.sub(r"[^\w]", "_", collection)
    out_path = Path(output) if output else default_digest_dir / f"{safe_name}_digest.md"

    lines: list[str] = []
    lines.append(f"# {collection} — 文献消化报告\n")
    lines.append(f"> 生成时间: {time.strftime('%Y-%m-%d')}")
    lines.append(f"> 论文总数: {total} 篇（来自 Zotero collection: {parent}/{collection}）")
    lines.append(f"> 时间跨度: {year_range}")
    lines.append(f"> 数据来源: Zotero API\n")
    lines.append("---\n")

    # ── Block 1: Research trajectory ──
    lines.append("## Block 1: 研究脉络 — 研究对象与核心方法的变迁\n")
    lines.append("> 通读所有论文标题和摘要，按时间线梳理研究对象和核心方法如何演变。\n")
    lines.append("### 时间线总览\n")
    lines.append("| 时期 | 研究对象 | 核心方法 | 代表论文 |")
    lines.append("|------|---------|---------|---------|")
    lines.append("| YYYY–YYYY | ... | ... | [标题] (DOI) |\n")
    lines.append("### 方法论转折点\n")
    lines.append("- **YYYY**: [关键转变描述]")
    lines.append("  - 触发: ...")
    lines.append("  - 论文: [标题] (DOI)\n")
    lines.append("### 研究主题分类\n")
    lines.append("1. **主题 A** (YYYY–YYYY): ...")
    lines.append("2. **主题 B** (YYYY–YYYY): ...\n")

    # ── Block 2: Research themes (collaborator network) ──
    lines.append("---\n")
    lines.append("## Block 2: 合作者网络\n")
    lines.append("> 从作者列表中提取高频合作者，识别核心团队和外部合作。\n")
    lines.append("### 核心合作者（≥3 篇共作）\n")
    lines.append("| 合作者 | 共作篇数 | 机构（推测） | 主要合作主题 | 活跃时期 |")
    lines.append("|--------|---------|-------------|-------------|---------|\n")
    lines.append("### 合作模式\n")
    lines.append("- **实验室内部**: ...")
    lines.append("- **跨机构合作**: ...")
    lines.append("- **产业合作**: ...\n")

    # ── Block 3: Review/tutorial papers ──
    lines.append("---\n")
    lines.append("## Block 3: 综述文章精读\n")
    lines.append("> 识别该学者的 review/survey 论文，作为理解其研究领域的入口。\n")

    reviews = [
        p
        for p in papers
        if re.search(r"review|survey|perspective|outlook", p.get("title", ""), re.IGNORECASE)
    ]
    if reviews:
        lines.append("### 综述清单\n")
        lines.append("| 年份 | 标题 | 期刊 | DOI |")
        lines.append("|------|------|------|-----|")
        for r in reviews:
            doi = r.get("doi", "")
            lines.append(
                f"| {r.get('year', '')} | {r['title'][:50]} | {r.get('venue', '')[:30]} | {doi} |"
            )
        lines.append("")
    else:
        lines.append("_（暂未发现明确综述论文，检查后补充）_\n")

    lines.append("### 综述要点\n")
    lines.append("对每篇综述：")
    lines.append("- **覆盖范围**: ...")
    lines.append("- **核心观点**: ...")
    lines.append("- **技术框架**: ...\n")

    # ── Block 4: Top cited papers deep read ──
    lines.append("---\n")
    lines.append("## Block 4: 核心高引论文深读\n")
    lines.append("> 按引用数排序的前 10 篇论文，深入分析其贡献。\n")

    # Fetch citation counts from CrossRef — only for papers with DOI
    # Limit to avoid hammering API: fetch all, but CrossRef is fast (~0.1s/call)
    # and only runs during digest generation (infrequent)
    console.print("  [dim]Fetching citation counts from CrossRef...[/dim]")
    from lit.core.crossref import fetch_metadata
    fetched = 0
    for p in papers:
        if p.get("doi"):
            cr = fetch_metadata(p["doi"])
            if cr:
                p["citations"] = cr.get("citations", 0)
            fetched += 1
            if fetched % 50 == 0:
                console.print(f"  [dim]  ...{fetched} papers queried[/dim]")

    top10 = sorted(papers, key=lambda p: p.get("citations", 0), reverse=True)[:10]
    lines.append("### 高引论文 Top 10\n")
    lines.append("| 排名 | 引用数 | 年份 | 标题 | DOI |")
    lines.append("|------|--------|------|------|-----|")
    for rank, p in enumerate(top10, 1):
        lines.append(
            f"| {rank} | {p.get('citations', 0)} | {p.get('year', '')} | {p['title'][:50]} | {p.get('doi', '')} |"
        )
    lines.append("")
    lines.append("### 逐篇深读\n")
    lines.append("对每篇高引论文：")
    lines.append("- **解决的问题**: ...")
    lines.append("- **核心创新**: ...")
    lines.append("- **方法细节**: ...")
    lines.append("- **影响**: ...\n")

    # ── Cross-talk section ──
    lines.append("---\n")
    lines.append("## ⚡ Cross-talk 更新区\n")
    lines.append("> 不同 Block 之间的关联发现。在填充各 Block 时发现的跨 Block 联系记录于此，")
    lines.append("> 并在对应 Block 中插入 ⚡ 标记。\n")

    # ── Appendix ──
    lines.append("---\n")
    lines.append("## 附录\n")
    lines.append("### A. 完整论文列表\n")
    lines.append("| # | 年份 | 标题 | Venue | DOI |")
    lines.append("|---|------|------|-------|-----|")
    for i, p in enumerate(papers_sorted, 1):
        lines.append(
            f"| {i} | {p.get('year', '')} | {p['title'][:40]} | {p.get('venue', '')[:25]} | {p.get('doi', '')[:25]} |"
        )
    lines.append("")

    # Download / attachment status
    # (Not available from pure Zotero collection query — placeholder)
    lines.append("### B. 附件状态\n")
    lines.append("| 状态 | 数量 |")
    lines.append("|------|------|")
    lines.append(f"| 共收录 | {total} |")
    lines.append(f"| (PDF 状态需通过 lit.digest.parser 进一步检查) | ... |\n")

    # ── Write file ──
    content = "\n".join(lines)
    with open(str(out_path), "w", encoding="utf-8") as f:
        f.write(content)

    console.print(f"  [green]✓ Template generated:[/green] {out_path}")
    console.print(
        f"  [dim]{total} papers, {len(reviews)} reviews identified, top-10 citations table populated[/dim]"
    )

    return str(out_path.resolve())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate literature digest template from Zotero collection"
    )
    parser.add_argument("collection", help="Zotero collection name (e.g. 'Ji-Xin Cheng')")
    parser.add_argument("--parent", default="People", help="Parent collection name (default: People)")
    parser.add_argument("--output", "-o", help="Custom output path")
    args = parser.parse_args()

    run(args.collection, parent=args.parent, output=args.output)
