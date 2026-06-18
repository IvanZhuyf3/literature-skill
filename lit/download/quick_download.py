"""
lit/download/quick_download.py — 快速免费 PDF 下载编排器。

按序调用各平台的下载方法，第一个成功就返回。每步互不依赖，各是一个独立文件。
不碰 Zotero，不更新任何状态。调用方（CLI）负责 attach。

扩展：在 _METHODS 列表加 (名字, 函数) 即可。
    每个函数签名: fn(doi: str, year: str | int | None) -> Path | None

当前方法链:
    [0] scihub_cdp — 在已有 Edge 浏览器打开 Sci-Hub，提取 PDF URL 后下载
    [1] (预留) unpaywall, pmc, core 等

Usage:
    from lit.download.quick_download import run
    pdf_path = run("10.1038/s41586-021-03819-2", year="2021")

Public function:
    run(doi: str, year: str | int | None = None) -> Path | None
"""
from __future__ import annotations

import logging
from pathlib import Path

from rich.console import Console

from lit.download.scihub_cdp import try_scihub

logger = logging.getLogger(__name__)
console = Console()


# ── 方法注册表 ──────────────────────────────────────────────────────────────
# 每项: (显示名, 调用函数)
# 函数签名: (doi: str, year: str | int | None) -> Path | None
_METHODS: list[tuple[str, callable]] = [
    ("Sci-Hub (CDP)", try_scihub),
    # 未来在此追加: ("Unpaywall", try_unpaywall), ...
]


def run(doi: str, year: str | int | None = None) -> Path | None:
    """
    Try to download a paper PDF via the quickest available free source.

    Calls methods in registration order; returns on first success.

    Args:
        doi:  The DOI string (e.g. ``"10.1038/s41586-023-06139-9"``).
        year: Publication year.  Individual methods may skip based on this.

    Returns:
        ``Path`` to the downloaded PDF, or ``None`` if no source had it.
    """
    doi = doi.strip()
    if not doi:
        return None

    for name, fn in _METHODS:
        console.print(f"[dim]  quick_download: trying {name}...[/dim]")
        try:
            pdf_path = fn(doi, year=year)
            if pdf_path:
                console.print(f"[green]  ✓ {name}: {pdf_path.name}[/green]")
                return pdf_path
        except Exception as e:
            logger.warning("quick_download: %s failed for %s: %s", name, doi, e)
            console.print(
                f"[dim]  ✗ {name}: {type(e).__name__} — skipped[/dim]"
            )

    console.print("[dim]  quick_download: all methods exhausted[/dim]")
    return None
