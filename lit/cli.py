"""
lit/cli.py — 单一 CLI 入口。

用法:
    lit scholar <URL>             抓取 Scholar → 注册 Zotero（无 PDF）
    lit import <DOI/URL>          单篇→注册 Zotero
    lit import <image_path>       图片 OCR → 注册 Zotero
    lit attach <collection>       补缺 PDF（读 Zotero collection）
    lit download <DOI/URL>        仅下载 PDF（不入 Zotero）
    lit parse <pdf_path>          MinerU 解析 PDF → Markdown
    lit digest <collection>       生成消化报告
    lit maintain [--collection X] [--fix] [--dry-run]  文件库健康检查与清理
    lit qr <DOI>                  生成 QR 码
"""
from __future__ import annotations

import sys
import argparse
from pathlib import Path


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
    p = sub.add_parser("import", help="单篇论文→注册 Zotero（可选下载 PDF）")
    p.add_argument("source", help="DOI, URL, 或图片路径")
    p.add_argument("--download", action="store_true", help="同时下载 PDF")

    # ── download ──
    p = sub.add_parser("download", help="下载 PDF 到本地（不入 Zotero）")
    p.add_argument("source", help="DOI 或 URL")

    # ── attach ──
    p = sub.add_parser("attach", help="读 Zotero collection → 批量补 PDF")
    p.add_argument("collection", help="Zotero collection name (e.g. Ji-Xin Cheng)")
    p.add_argument("--parent", default="People", help="父文件夹名（默认 People）")
    p.add_argument("--limit", type=int, default=None, help="限制篇数")

    # ── parse ──
    p = sub.add_parser("parse", help="MinerU 解析 PDF → Markdown")
    p.add_argument("pdf_path", help="PDF 文件路径")
    p.add_argument("-o", "--output", help="输出文件路径（默认 stdout）")

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

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scholar":
        from lit.discover.scholar import run
        run(args.url, max_papers=args.max_papers, scrape_only=args.scrape_only)

    elif args.command == "import":
        from lit.discover.cite import run
        run(args.source, download=args.download)

    elif args.command == "download":
        from lit.download.engine import download_pdf
        result = download_pdf(args.source)
        print(f"PDF saved to: {result}")

    elif args.command == "attach":
        from lit.batch.attach import run
        run(args.collection, parent=args.parent, limit=args.limit)

    elif args.command == "parse":
        from lit.digest.parser import run
        run(args.pdf_path, output=args.output)

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


if __name__ == "__main__":
    main()
