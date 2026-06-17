"""
lit/digest/parser.py — MinerU PDF parser wrapper.

Thin wrapper around ``pdf_parser.py`` that uses ``lit.core.config.load()``
for the MinerU token instead of pdf_parser's own ``load_config()``.

Usage:
    from lit.digest.parser import run
    md = run("path/to/paper.pdf")
    # → returns full markdown string, or None on failure

    run("path/to/paper.pdf", output="output.md")
    # → saves to file and returns output path

CLI:
    python -m lit.digest.parser <pdf_path> [--output <md_path>]
"""

from __future__ import annotations

import sys
from pathlib import Path

from lit.core.config import load as get_config

# pdf_parser is at the skill base root, not inside lit/.
# Add the skill base to sys.path so we can import it.
_THIS_DIR = Path(__file__).resolve().parent  # lit/digest/
_SKILL_BASE = _THIS_DIR.parent.parent  # skill base (contains pdf_parser.py)
if str(_SKILL_BASE) not in sys.path:
    sys.path.insert(0, str(_SKILL_BASE))


def run(pdf_path: str, output: str | None = None) -> str | None:
    """
    Parse a PDF using MinerU online API.

    Args:
        pdf_path: Path to PDF file.
        output: Optional output file path (None = print to stdout).

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
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    if args.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(message)s")

    result = run(args.pdf_path, output=args.output)
    if result is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
