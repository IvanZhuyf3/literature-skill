"""
lit/discover/import_ref.py — 单篇论文导入 Zotero（仅注册，不下载）。

只做一件事：输入 DOI / URL / 图片路径，提取 metadata → Zotero 去重 → 创建条目。
不碰任何下载逻辑。若要同时下载 PDF，由 CLI 层编排 quick_download。

Public function:
    run(source: str) -> dict
        返回 {"item_key", "doi", "title", "url", "dup", "year"}
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import requests
from rich.console import Console

from lit.core.config import load as get_config
from lit.core.crossref import fetch_metadata, resolve_doi
from lit.core.zotero import (
    check_duplicate,
    create_item,
)

console = Console()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _normalize_source(source: str) -> tuple[str, str]:
    """Normalize input source into (type, value).

    Returns one of:
        ("doi", "10.xxxx/xxxxx")
        ("url", "https://...")
        ("image", "/path/to/image.png")
        ("unknown", source)
    """
    s = source.strip()

    # Image file
    if s.lower().endswith((".png", ".jpg", ".jpeg")):
        p = Path(s)
        if p.exists():
            return ("image", str(p.resolve()))
        return ("unknown", s)

    # Bare DOI
    if re.match(r"^10\.\d{4,}", s):
        return ("doi", s)

    # doi.org URL
    m = re.search(r"doi\.org/(10\.\S+)", s)
    if m:
        return ("doi", m.group(1))

    # Regular URL
    if s.startswith(("http://", "https://")):
        return ("url", s)

    # Try to find embedded DOI
    m = re.search(r"(10\.\d{4,}/[^\s,;]+)", s)
    if m:
        return ("doi", m.group(1).rstrip(".,;"))

    return ("unknown", s)


def _extract_doi_from_text(text: str) -> str:
    """Extract a DOI from various text forms."""
    text = text.strip()
    if not text:
        return ""
    if re.match(r"^10\.\d{4,}", text):
        return text
    m = re.search(r"doi\.org/(10\.\S+)", text)
    if m:
        return m.group(1)
    m = re.search(r"(10\.\d{4,}/\S+)", text)
    if m:
        return m.group(1).rstrip(".;,")
    return text


def _extract_metadata_from_html(url: str) -> dict:
    """Fetch page HTML, parse citation meta tags, enrich via CrossRef.

    Replicates the logic from ``zot.py:extract_metadata`` without depending on
    the standalone script.  Fields returned are compatible with
    ``lit.core.zotero.create_item``:
        title, authors (list[str]), DOI, url, year, journal, volume, issue,
        pages, ISSN, abstract, publisher.
    """
    meta = {"url": url}

    # 1. Fetch page HTML
    try:
        resp = requests.get(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36"
                )
            },
            timeout=30,
        )
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        console.print(f"[yellow]⚠ Could not fetch page for metadata: {e}[/yellow]")
        return meta

    # 2. Parse citation meta tags
    def _meta(name: str) -> str:
        m = re.search(
            rf'<meta\s+name="{re.escape(name)}"\s+content="([^"]*)"',
            html,
            re.IGNORECASE,
        )
        if not m:
            m = re.search(
                rf'<meta\s+property="{re.escape(name)}"\s+content="([^"]*)"',
                html,
                re.IGNORECASE,
            )
        return m.group(1).strip() if m else ""

    meta["title"] = _meta("citation_title") or _meta("og:title")
    meta["DOI"] = _extract_doi_from_text(_meta("citation_doi") or _meta("DOI"))
    meta["journal"] = _meta("citation_journal_title") or _meta("citation_journal_abbrev")
    meta["year"] = _meta("citation_date")[:4] if _meta("citation_date") else ""
    meta["volume"] = _meta("citation_volume")
    meta["issue"] = _meta("citation_issue")
    meta["ISSN"] = _meta("citation_ISSN")
    meta["publisher"] = _meta("citation_publisher")

    first = _meta("citation_firstpage")
    last = _meta("citation_lastpage")
    meta["pages"] = f"{first}-{last}" if first and last else (first or "")

    author_names = re.findall(
        r'<meta\s+name="citation_author"\s+content="([^"]*)"', html, re.IGNORECASE
    )
    if not author_names:
        author_names = re.findall(
            r'<meta\s+name="dc\.Creator"\s+content="([^"]*)"', html, re.IGNORECASE
        )
    meta["authors"] = [a.strip() for a in author_names if a.strip()]

    abstract = _meta("citation_abstract") or _meta("abstract") or _meta("description")
    meta["abstract"] = re.sub(r"<[^>]+>", "", abstract) if abstract else ""

    console.print(
        f"[dim]  Page metadata: title={meta.get('title','?')[:60]}, "
        f"DOI={meta.get('DOI','?')}[/dim]"
    )

    # 3. CrossRef enrichment if DOI found
    doi = meta.get("DOI", "")
    if doi:
        cr = fetch_metadata(doi)
        if cr:
            for key in ("title", "journal", "year", "volume", "issue", "pages",
                        "ISSN", "abstract", "publisher"):
                if cr.get(key):
                    meta[key] = cr[key]
            if cr.get("authors"):
                meta["authors"] = cr["authors"]
            console.print(
                f"[dim]  CrossRef enriched: {meta.get('journal','')} "
                f"{meta.get('year','')} v{meta.get('volume','')}[/dim]"
            )
        else:
            console.print("[dim]  CrossRef lookup failed, using page metadata[/dim]")

    return meta


def _extract_from_image(image_path: str) -> dict:
    """Extract citation metadata from an image via OCR + CrossRef.

    Uses the ``ocr_citation`` standalone module:
        1. DeepSeek Vision API reads the image
        2. Parse structured JSON references from OCR output
        3. CrossRef enrichment to find DOI

    Returns a dict with at least ``DOI``, ``title``, ``url`` if found,
    or an empty dict.
    """
    try:
        skill_base = Path(__file__).resolve().parent.parent.parent
        if str(skill_base) not in sys.path:
            sys.path.insert(0, str(skill_base))

        import ocr_citation  # noqa: F811
    except ImportError:
        console.print("[red]Could not import ocr_citation module.[/red]")
        return {}

    console.print("[dim]  Running OCR via DeepSeek Vision...[/dim]")
    try:
        ocr_raw = ocr_citation.call_vision(image_path, ocr_citation.OCR_PROMPT)
    except Exception as e:
        console.print(f"[yellow]⚠ OCR failed: {e}[/yellow]")
        return {}

    refs = ocr_citation.extract_doi_from_ocr(ocr_raw)
    if not refs:
        console.print("[yellow]⚠ No structured references found in image.[/yellow]")
        return {}

    console.print(f"[dim]  Verifying {len(refs)} reference(s) via CrossRef...[/dim]")
    enriched = ocr_citation.enrich_with_crossref(refs)

    for ref in enriched:
        doi = ref.get("crossref_doi") or ref.get("doi", "")
        if doi:
            title = ref.get("crossref_title") or ref.get("title", "")
            console.print(f"[dim]  Found: {title[:60]} (DOI: {doi})[/dim]")
            return {
                "DOI": doi,
                "title": title,
                "url": f"https://doi.org/{doi}",
            }

    console.print("[yellow]⚠ No DOI found in image references.[/yellow]")
    return {}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def run(source: str) -> dict:
    """
    Import a single paper citation into Zotero (no PDF download).

    Args:
        source: DOI (e.g. ``"10.1038/s41586-023-06139-9"``),
                URL (e.g. ``"https://doi.org/10.1038/..."``), or a path to an
                image file (``.png`` / ``.jpg`` / ``.jpeg``).

    Returns:
        A dict with keys:
            ``item_key`` (str | None) — Zotero item key
            ``doi``      (str | None) — DOI found
            ``title``    (str | None) — Paper title
            ``url``      (str | None) — Landing page URL
            ``year``     (str | None) — Publication year (for downstream use)
            ``dup``      (bool)       — ``True`` if the item already existed
                                         in Zotero (no changes made)
    """
    result: dict = {
        "item_key": None,
        "doi": None,
        "title": None,
        "url": None,
        "year": None,
        "dup": False,
    }

    cfg = get_config()

    source_type, source_value = _normalize_source(source)
    trunc = source[:80] + ("..." if len(source) > 80 else "")
    console.print(f"\n[bold cyan]━━━ import_ref: {trunc} ━━━[/bold cyan]\n")
    console.print(f"[bold]Detected source type:[/bold] {source_type}")

    # ── Step 1: Extract metadata ──────────────────────────────────────────

    meta: dict = {}

    if source_type == "image":
        console.print("[bold]Step 1/3:[/bold] Extracting citation from image via OCR...")
        meta = _extract_from_image(source_value)
        if not meta.get("DOI"):
            console.print("[red]No DOI could be extracted from the image. Aborting.[/red]")
            return result

    elif source_type == "doi":
        doi = source_value
        console.print(f"[bold]Step 1/3:[/bold] Fetching CrossRef metadata for DOI {doi}...")
        cr = fetch_metadata(doi)
        if cr:
            meta = {
                "DOI": cr.get("doi", doi),
                "title": cr.get("title", ""),
                "authors": cr.get("authors", []),
                "journal": cr.get("journal", ""),
                "year": cr.get("year", ""),
                "volume": cr.get("volume", ""),
                "issue": cr.get("issue", ""),
                "pages": cr.get("pages", ""),
                "ISSN": cr.get("ISSN", ""),
                "abstract": cr.get("abstract", ""),
                "publisher": cr.get("publisher", ""),
                "url": cr.get("url", f"https://doi.org/{doi}"),
            }
        else:
            console.print(
                "[yellow]CrossRef lookup failed — "
                "falling back to page HTML extraction...[/yellow]"
            )
            meta = _extract_metadata_from_html(f"https://doi.org/{doi}")
            if not meta.get("DOI"):
                meta["DOI"] = doi

    elif source_type == "url":
        console.print("[bold]Step 1/3:[/bold] Extracting metadata from URL...")
        meta = _extract_metadata_from_html(source_value)
        # Also check if the URL itself contains a DOI
        embedded = _extract_doi_from_text(source_value)
        if embedded and not meta.get("DOI"):
            meta["DOI"] = embedded

    else:
        console.print(f"[red]Unknown source type: {source}. "
                      f"Supply a DOI, URL, or image path.[/red]")
        return result

    # Ensure required fields are present
    if not meta.get("url"):
        doi = meta.get("DOI", "")
        meta["url"] = (
            source_value
            if source_type == "url"
            else f"https://doi.org/{doi}" if doi
            else source
        )

    if not meta.get("title") and not meta.get("DOI"):
        console.print("[red]Could not extract any metadata. Aborting.[/red]")
        return result

    result["doi"] = meta.get("DOI", "")
    result["title"] = meta.get("title", "")
    result["url"] = meta.get("url", "")
    result["year"] = str(meta.get("year", ""))
    console.print(f"  Title: {result['title'][:80] if result['title'] else '?'}")
    console.print(f"  DOI:   {result['doi'] or 'N/A'}")

    # ── Step 2: Dedup ────────────────────────────────────────────────────

    console.print(f"\n[bold]Step 2/3:[/bold] Checking for duplicates in Zotero...")

    dup_key, dup_reason = check_duplicate(
        doi=meta.get("DOI", ""),
        title=meta.get("title", ""),
        url=meta.get("url", ""),
    )

    if dup_key:
        console.print(
            f"[yellow]↻ Duplicate found ({dup_reason}): "
            f"{dup_key}, skipping creation.[/yellow]"
        )
        result["item_key"] = dup_key
        result["dup"] = True
    else:
        # ── Step 3: Create Zotero item ───────────────────────────────────
        console.print("[bold]Step 3/3:[/bold] Creating Zotero item...")
        try:
            item_key = create_item(meta)
            result["item_key"] = item_key
            console.print(f"[green]✓ Item created:[/green] {item_key}")
        except Exception as e:
            console.print(f"[red]Failed to create Zotero item: {e}[/red]")
            return result

    # ── Summary ───────────────────────────────────────────────────────────

    console.print(f"\n[bold green]━━━ Done! ━━━[/bold green]")
    console.print(f"  Item:  {result['item_key']}")
    console.print(f"  Title: {result['title'][:80] if result['title'] else '?'}")
    console.print(f"  DOI:   {result['doi'] or 'N/A'}")
    if result["dup"]:
        console.print(f"  [yellow](existing item — no changes made)[/yellow]")

    return result
