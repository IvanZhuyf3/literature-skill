"""
lit/digest/parser.py — MinerU PDF parser wrapper.

Thin wrapper around ``pdf_parser.py`` that uses ``lit.core.config.load()``
for the MinerU token instead of pdf_parser's own ``load_config()``.

Usage:
    from lit.digest.parser import run, format_doi_filename
    md = run("path/to/paper.pdf")
    # → returns full markdown string, or None on failure

    # With metadata (prepends YAML bibliography frontmatter):
    run("path/to/paper.pdf", metadata={...})

    fn = format_doi_filename("10.1234/example")
    # → "10.1234_example.md"

CLI:
    python -m lit parse <pdf_path> [--output <md_path>] [--item-key <key>]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from lit.core.config import load as get_config

# pdf_parser is at the skill base root, not inside lit/.
# Add the skill base to sys.path so we can import it.
_THIS_DIR = Path(__file__).resolve().parent  # lit/digest/
_SKILL_BASE = _THIS_DIR.parent.parent  # skill base (contains pdf_parser.py)
if str(_SKILL_BASE) not in sys.path:
    sys.path.insert(0, str(_SKILL_BASE))


def format_doi_filename(doi: str) -> str:
    """Convert a DOI to a safe, unique .md filename.

    Replaces ``/`` and other filesystem-unsafe chars with ``_``.
    Example: ``10.1038/s41586-021-03819-2`` → ``10.1038_s41586-021-03819-2.md``
    """
    safe = re.sub(r'[\\/:*?"<>|]', "_", doi.strip())[:120]
    return f"{safe}.md"


def format_bibliography(meta: dict) -> str:
    """Format a YAML bibliography frontmatter from a metadata dict.

    Fields supported: doi, title, authors, journal, year, volume,
    issue, pages, publisher.  Only non-empty fields are included.

    Args:
        meta: Dict with keys like DOI, title, authors (list[str]), journal,
              year, volume, issue, pages, publisher, url.

    Returns:
        A YAML frontmatter string ready to prepend to a paper .md file.
    """
    lines = ["---", "bibliography:"]

    doi = meta.get("DOI") or meta.get("doi", "")
    if doi:
        lines.append(f"  doi: {doi}")

    title = meta.get("title", "")
    if title:
        escaped = title.replace('"', "'")
        lines.append(f'  title: "{escaped}"')

    authors = meta.get("authors", [])
    if authors:
        if isinstance(authors, list):
            joined = "; ".join(a.strip() for a in authors if a.strip())
        else:
            joined = str(authors).strip()
        escaped = joined.replace('"', "'")
        lines.append(f'  authors: "{escaped}"')

    journal = meta.get("journal", "")
    if journal:
        lines.append(f'  journal: "{journal}"')

    year = meta.get("year", "")
    if year:
        lines.append(f"  year: {str(year).strip()[:4]}")

    vol = meta.get("volume", "")
    if vol:
        lines.append(f"  volume: {vol}")

    issue = meta.get("issue", "")
    if issue:
        lines.append(f"  issue: {issue}")

    pages = meta.get("pages", "")
    if pages:
        lines.append(f'  pages: "{pages}"')

    publisher = meta.get("publisher", "")
    if publisher:
        lines.append(f'  publisher: "{publisher}"')

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def run(
    pdf_path: str,
    output: str | None = None,
    metadata: dict | None = None,
) -> str | None:
    """
    Parse a PDF using MinerU online API.

    Args:
        pdf_path: Path to PDF file.
        output: Optional output file path (None = print to stdout).
        metadata: Optional metadata dict. If provided, a YAML bibliography
                  frontmatter section is prepended to the markdown.

    Returns:
        Markdown string if no output path given, or the output file path
        if ``output`` was specified. Returns None on failure.
    """
    from pdf_parser import parse_pdf

    config = get_config()
    markdown = parse_pdf(pdf_path, config=config)

    if markdown is None:
        print("FAILED: PDF parsing failed", file=sys.stderr)
        return None

    # Prepend bibliography frontmatter if metadata provided
    if metadata:
        bib = format_bibliography(metadata)
        markdown = bib + markdown

    if output:
        out_path = Path(output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(str(out_path), "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"OK: {len(markdown)} chars → {out_path}")
        return str(out_path.resolve())

    return markdown


def main() -> None:
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Parse PDF via MinerU online API (lit.digest.parser wrapper)"
    )
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--output", "-o", help="Output markdown file path")
    parser.add_argument(
        "--item-key",
        help="Zotero item key for bibliography metadata (auto-fetched)",
    )
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    if args.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(message)s")

    # Fetch metadata from Zotero if item_key provided
    metadata = None
    if args.item_key:
        from lit.core.zotero import fetch_item, item_to_meta
        item = fetch_item(args.item_key)
        if item:
            metadata = item_to_meta(item)
            title = metadata.get("title", "?")[:60]
            print(f"  Bibliography: {title}", file=sys.stderr)
        else:
            print(f"  [yellow]⚠ Item {args.item_key} not found in Zotero[/yellow]",
                  file=sys.stderr)

    result = run(args.pdf_path, output=args.output, metadata=metadata)
    if result is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
