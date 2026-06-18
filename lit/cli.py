"""
lit/cli.py — 单一 CLI 入口。

用法:
    lit scholar <URL>             抓取 Scholar → 注册 Zotero（无 PDF）
    lit import <DOI/URL>          注册 Zotero → 自动快速下载 PDF
    lit import <image_path>       图片 OCR → 注册 Zotero → 自动快速下载
    lit attach <collection>       补缺 PDF（读 Zotero collection）
    lit download <DOI/URL>        仅下载 PDF（不入 Zotero）（已废弃）
    lit parse <pdf_path>          MinerU 解析 PDF → Markdown
    lit digest <collection>       生成消化报告
    lit maintain [--collection X] [--fix] [--dry-run]  文件库健康检查与清理
    lit qr <DOI>                  生成 QR 码

架构:
    import_ref.run()       → 仅加 ref 到 Zotero（不下载）
    quick_download.run()   → 用最快免费源下载 PDF（不碰 Zotero）
    lit import 由 CLI 编排: import_ref → quick_download → attach_pdf
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

    # ── import ──
    p = sub.add_parser("import", help="注册 Zotero → 自动快速下载 PDF")
    p.add_argument("source", help="DOI, URL, 或图片路径")

    # ── download (DEPRECATED — use ``lit import <DOI>``) ──
    p = sub.add_parser("download", help="[DEPRECATED] 仅下载 PDF（不入 Zotero）")
    p.add_argument("source", help="DOI 或 URL")
    p.add_argument("--no-deprecation-warning", action="store_true", help=argparse.SUPPRESS)

    # ── attach ──
    p = sub.add_parser("attach", help="读 Zotero collection → 批量补 PDF")
    p.add_argument("collection", help="Zotero collection name (e.g. Ji-Xin Cheng)")
    p.add_argument("--parent", default="People", help="父文件夹名（默认 People）")
    p.add_argument("--limit", type=int, default=None, help="限制篇数")

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

    # ── pdf ──
    p = sub.add_parser("pdf", help="按 DOI 查本地 PDF（没有则下载）")
    p.add_argument("doi", help="DOI（精确匹配）")
    p.add_argument("--no-download", action="store_true", help="仅查本地，不下载")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scholar":
        from lit.discover.scholar import run
        run(args.url, max_papers=args.max_papers, scrape_only=args.scrape_only)

    elif args.command == "import":
        from lit.discover.import_ref import run as import_run
        from lit.download.quick_download import run as quick_run

        result = import_run(args.source)

        # Quick download runs by default after import
        if result.get("doi") and result.get("item_key"):
            pdf_path = quick_run(result["doi"], result.get("year"))
            if pdf_path:
                from lit.core.zotero import attach_pdf
                att_key = attach_pdf(result["item_key"], pdf_path)
                if att_key:
                    console.print(
                        f"[green]✓ PDF attached:[/green] {att_key}"
                    )
                    result["att_key"] = att_key
                else:
                    console.print(
                        "[yellow]⚠ Quick download succeeded but "
                        "attachment failed.[/yellow]"
                    )
            else:
                console.print(
                    "[dim]Quick download: no PDF available — "
                    "try Zotero Find Full Text (manual)[/dim]"
                )

    elif args.command == "download":
        from lit.download.engine import download_pdf
        if not getattr(args, "no_deprecation_warning", False):
            console.print(
                "[yellow]⚠ `lit download` is deprecated. "
                "Use `lit import <DOI>` instead "
                "(imports to Zotero + downloads automatically).[/yellow]"
            )
        result = download_pdf(args.source)
        print(f"PDF saved to: {result}")

    elif args.command == "attach":
        from lit.batch.attach import run
        run(args.collection, parent=args.parent, limit=args.limit)

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
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
        from generate_qr import generate_qr as _qr, slugify_doi
        out_dir = str(Path(__file__).resolve().parent.parent / "download" / "temp")
        out = _qr(args.doi, out_dir)
        print(f"  QR code: {out}")

    elif args.command == "pdf":
        from lit.core.zotero import resolve_local_pdf
        from lit.download.quick_download import run as quick_run

        pdf_path = resolve_local_pdf(args.doi)
        if pdf_path:
            print(pdf_path)
        elif args.no_download:
            console.print("[red]本地未找到[/red]")
            sys.exit(1)
        else:
            console.print("[dim]本地未找到，尝试下载...[/dim]")
            pdf_path = quick_run(args.doi)
            if pdf_path:
                print(str(pdf_path))
            else:
                console.print("[red]下载失败[/red]")
                sys.exit(1)


if __name__ == "__main__":
    main()
