"""
lit/cli.py — 单一 CLI 入口。

用法:
    lit scholar <URL>             抓取 Scholar → 注册 Zotero（无 PDF）
    lit import <DOI/URL>          仅注册到 Zotero（不下载）
    lit import <image_path>       图片 OCR → 注册 Zotero（不下载）
    lit quick <DOI|collection>    快速下载（Sci-Hub + OA 源）→ 挂载
    lit attach <DOI|collection>   Publisher adapter 兜底下载 → 挂载
    lit pdf <DOI>                 查本地 PDF 路径
    lit parse <pdf_path>          MinerU 解析 PDF → Markdown
    lit digest <collection>       生成消化报告
    lit maintain [--collection X] [--fix] [--dry-run]  文件库健康检查与清理
    lit qr <DOI>                  生成 QR 码
    lit track <author>            检测作者新论文

架构:
    import_ref.run()       → 仅加 ref 到 Zotero
    quick_download.run()   → Sci-Hub 快速下载 PDF（不碰 Zotero）
    engine.download_pdf()  → Publisher adapter 兜底下载
    Agent 编排: import → quick → attach（或按需组合）
"""
from __future__ import annotations

import sys
import argparse
from pathlib import Path

from rich.console import Console

console = Console()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lit",
        description="Literature Skill — 论文管理工具",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # ── scholar ──
    p = sub.add_parser("scholar", help="抓取 Scholar Profile 并注册到 Zotero")
    p.add_argument("url", help="Google Scholar profile URL")
    p.add_argument("--max-papers", type=int, default=None, help="限制篇数（测试用）")
    p.add_argument("--scrape-only", action="store_true", help="仅抓取，不注册")

    # ── import (仅注册，不下载) ──
    p = sub.add_parser("import", help="仅注册到 Zotero（不下载 PDF）")
    p.add_argument("source", help="DOI, URL, 或图片路径")

    # ── quick (快速下载: Sci-Hub + OA) ──
    p = sub.add_parser(
        "quick",
        help="快速下载（Sci-Hub + OA 源）— 单篇 DOI 或批量 collection",
    )
    p.add_argument(
        "target",
        help="DOI（单篇）或 Zotero collection 名（批量）",
    )
    p.add_argument("--parent", default="People", help="父文件夹名（默认 People）")
    p.add_argument("--limit", type=int, default=None, help="限制篇数（仅批量）")

    # ── attach (Publisher adapter 兜底下载) ──
    p = sub.add_parser(
        "attach",
        help="Publisher adapter 兜底下载 — 单篇 DOI 或批量 collection",
    )
    p.add_argument(
        "target",
        help="DOI（单篇）或 Zotero collection 名（批量）",
    )
    p.add_argument("--parent", default="People", help="父文件夹名（默认 People）")
    p.add_argument("--limit", type=int, default=None, help="限制篇数（仅批量）")

    # ── parse ──
    p = sub.add_parser("parse", help="MinerU 解析 PDF → Markdown（可选带 bibliography）")
    p.add_argument("pdf_path", help="PDF 文件路径")
    p.add_argument("-o", "--output", help="输出文件路径（默认 stdout）")
    p.add_argument("--item-key", help="Zotero item key，自动拉 bibliography 加到文件头")

    # ── digest ──
    p = sub.add_parser("digest", help="读 Zotero collection → 生成消化报告模板")
    p.add_argument("collection", help="Zotero collection name")
    p.add_argument("--parent", default="People")
    p.add_argument("-o", "--output", help="自定义输出路径")

    # ── maintain ──
    p = sub.add_parser("maintain", help="Zotero 文件库健康检查与清理")
    p.add_argument("--collection", default=None, help="仅检查某 collection (如 'Ji-Xin Cheng')")
    p.add_argument("--fix", action="store_true", help="执行修复（删孤儿目录 + ghost 条目）")
    p.add_argument("--dry-run", action="store_true", help="配合 --fix：只预览不执行")

    # ── qr ──
    p = sub.add_parser("qr", help="生成 DOI QR 码")
    p.add_argument("doi", help="DOI")

    # ── pdf (仅查本地) ──
    p = sub.add_parser("pdf", help="按 DOI 查本地 PDF 路径")
    p.add_argument("doi", help="DOI（精确匹配）")

    # ── track ──
    p = sub.add_parser("track", help="检测作者最新论文并导入 Zotero")
    p.add_argument("author", help="people/ 下的作者目录名 (如 Ji-Xin_Cheng)")
    p.add_argument("--download", action="store_true", help="检测后自动下载 PDF")

    # ── discover-s2 ──
    p = sub.add_parser("discover-s2", help="通过 DOI 反查发现所有 S2 author ID + 审计新论文")
    p.add_argument("author", help="people/ 下的作者目录名 (如 Ji-Xin_Cheng)")
    p.add_argument("--save", action="store_true", help="将发现的 ID 写入 profile.json")
    p.add_argument("--download", action="store_true", help="注册新论文到 Zotero 并下载 PDF (implies --save)")

    return parser


def _is_doi(target: str) -> bool:
    """判断参数是 DOI 还是 collection 名。"""
    # skill-base 根目录的 url_parser 有 is_doi
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from url_parser import is_doi
    return is_doi(target)


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scholar":
        from lit.discover.scholar import run
        run(args.url, max_papers=args.max_papers, scrape_only=args.scrape_only)

    elif args.command == "import":
        from lit.discover.import_ref import run as import_run

        result = import_run(args.source)
        if result.get("item_key"):
            console.print(
                f"[green]✓ Registered:[/green] {result['item_key']}"
            )
            console.print(
                f"[dim]Run `lit quick {result.get('doi', '<DOI>')}` to download PDF[/dim]"
            )

    elif args.command == "quick":
        from lit.batch.quick import run as batch_run, run_single

        if _is_doi(args.target):
            result = run_single(args.target)
            if result["status"] == "failed":
                sys.exit(1)
        else:
            batch_run(args.target, parent=args.parent, limit=args.limit)

    elif args.command == "attach":
        from lit.batch.attach import run as batch_run, run_single

        if _is_doi(args.target):
            result = run_single(args.target)
            if result["status"] == "failed":
                sys.exit(1)
        else:
            batch_run(args.target, parent=args.parent, limit=args.limit)

    elif args.command == "parse":
        from lit.digest.parser import run
        from lit.core.zotero import fetch_item, item_to_meta
        metadata = None
        if args.item_key:
            item = fetch_item(args.item_key)
            if item:
                metadata = item_to_meta(item)
        run(args.pdf_path, output=args.output, metadata=metadata)

    elif args.command == "digest":
        from lit.digest.template import run
        run(args.collection, parent=args.parent, output=args.output)

    elif args.command == "maintain":
        from lit.maintain import run
        run(collection=args.collection, fix=args.fix, dry_run=args.dry_run)

    elif args.command == "qr":
        from generate_qr import generate_qr as _qr
        out_dir = str(Path(__file__).resolve().parent.parent / "download" / "temp")
        out = _qr(args.doi, out_dir)
        print(f"  QR code: {out}")

    elif args.command == "pdf":
        from lit.core.zotero import resolve_local_pdf

        pdf_path = resolve_local_pdf(args.doi)
        if pdf_path:
            print(pdf_path)
        else:
            console.print("[red]本地未找到[/red]")
            console.print(
                f"[dim]运行 `lit quick {args.doi}` 下载[/dim]"
            )
            sys.exit(1)

    elif args.command == "track":
        from lit.discover.tracker import find_new_papers
        from lit.discover.import_ref import run as import_run
        from lit.batch.quick import run_single as quick_single
        from lit.batch.attach import run_single as attach_single

        new = find_new_papers(args.author)
        if not new:
            console.print("[green]没有新论文[/green]")
            return

        console.print(f"\n[bold]发现 {len(new)} 篇新论文:[/bold]")
        for p in new:
            console.print(f"  [{p['source']}] {p['doi']}")

        if args.download:
            for p in new:
                console.print(f"\n[dim]处理 {p['doi']}...[/dim]")
                result = import_run(p["doi"])
                if not result.get("item_key"):
                    console.print(f"  [yellow]⚠ 注册失败: {p['doi']}[/yellow]")
                    continue

                ik = result["item_key"]
                qr = quick_single(result["doi"], item_key=ik)
                if qr and qr["status"] in ("attached", "already_has"):
                    console.print(f"  [green]✓ {p['doi']}[/green]")
                else:
                    console.print(f"  [dim]quick 未命中，尝试 publisher adapter...[/dim]")
                    ar = attach_single(result["doi"], item_key=ik)
                    if ar and ar["status"] in ("attached", "already_has"):
                        console.print(f"  [green]✓ {p['doi']} (attach)[/green]")
                    else:
                        console.print(f"  [yellow]⚠ 下载失败: {p['doi']}[/yellow]")
        else:
            console.print("\n使用 --download 自动导入 + 快速下载 + 兜底")

    elif args.command == "discover-s2":
        from lit.discover.tracker import discover_s2_ids, audit_new_papers

        save = args.save or args.download
        discover_s2_ids(args.author, save=save)

        if save:
            new_papers = audit_new_papers(args.author)
            if new_papers and args.download:
                from lit.discover.import_ref import run as import_run
                from lit.batch.quick import run_single as quick_single
                from lit.batch.attach import run_single as attach_single

                console.print(f"\n[bold]━━━ 下载 {len(new_papers)} 篇新论文 ━━━[/bold]")
                ok = 0
                for i, p in enumerate(new_papers):
                    doi = p["doi"]
                    title = (p.get("title") or "")[:50]
                    console.print(f"\n  [{i+1}/{len(new_papers)}] {doi}")
                    console.print(f"  [dim]{title}[/dim]")

                    result = import_run(doi)
                    if not result.get("item_key"):
                        console.print(f"    [yellow]⚠ import failed[/yellow]")
                        continue

                    ik = result["item_key"]
                    qr = quick_single(result.get("doi", doi), item_key=ik)
                    if qr and qr["status"] in ("attached", "already_has"):
                        console.print(f"    [green]✓ quick[/green]")
                        ok += 1
                    else:
                        ar = attach_single(result.get("doi", doi), item_key=ik)
                        if ar and ar["status"] in ("attached", "already_has"):
                            console.print(f"    [green]✓ attach[/green]")
                            ok += 1
                        else:
                            console.print(f"    [yellow]⚠ download failed[/yellow]")

                console.print(f"\n[bold green]Done: {ok}/{len(new_papers)} downloaded[/bold green]")


if __name__ == "__main__":
    main()
