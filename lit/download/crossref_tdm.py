"""
lit/download/crossref_tdm.py — Crossref TDM link extraction.

Query Crossref /works/{doi}, extract PDF links from the `link[]` array.
Download the first accessible PDF.

No API key needed. Polite pool benefits from mailto in User-Agent.

Usage:
    from lit.download.crossref_tdm import try_crossref_tdm
    pdf_path = try_crossref_tdm("10.1038/s41586-021-03819-2")
"""
from __future__ import annotations

import logging
import re
from pathlib import Path
from urllib.parse import quote

import requests

from lit.core.config import load as get_config

logger = logging.getLogger(__name__)

_CROSSREF_API = "https://api.crossref.org/works"
_BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def try_crossref_tdm(
    doi: str,
    year: str | int | None = None,
) -> Path | None:
    """Query Crossref for TDM (full-text) PDF links and download.

    Args:
        doi:  DOI string.
        year: Publication year (unused — no year gate for Crossref TDM).

    Returns:
        Path to downloaded PDF, or None.
    """
    if not doi or not doi.strip():
        return None

    doi = doi.strip()
    url = f"{_CROSSREF_API}/{doi}"
    headers = {"User-Agent": _BROWSER_UA}

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logger.warning("Crossref TDM: API query failed for %s: %s", doi, e)
        return None

    message = data.get("message", {})
    links = message.get("link") or []

    if not links:
        logger.info("Crossref TDM: no links for %s", doi)
        return None

    # Filter for PDF links — some Crossref entries use "unspecified" content-type
    # but the URL ends in .pdf or points to a PDF resource
    pdf_links = []
    for link in links:
        ct = (link.get("content-type") or "").lower()
        link_url = link.get("URL") or ""
        if "pdf" in ct or link_url.lower().endswith(".pdf"):
            pdf_links.append(link)

    # Sort: vor first, then others
    pdf_links.sort(
        key=lambda l: 0 if l.get("intended-application") == "vor" else 1
    )

    for link in pdf_links:
        pdf_url = link.get("URL") or ""
        if not pdf_url:
            continue

        logger.info("Crossref TDM: trying %s", pdf_url[:80])
        pdf_path = _download_pdf(pdf_url, doi)
        if pdf_path:
            return pdf_path

    logger.info("Crossref TDM: no accessible PDF for %s", doi)
    return None


def _download_pdf(url: str, doi: str) -> Path | None:
    """Download a PDF from URL, verify it's a real PDF."""
    cfg = get_config()
    download_dir = cfg.get("download", {}).get("temp_dir", "")

    headers = {
        "User-Agent": _BROWSER_UA,
        "Accept": "application/pdf",
    }

    try:
        resp = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        if resp.status_code != 200:
            logger.debug("Crossref TDM: %s returned %d", url[:60], resp.status_code)
            return None

        content = resp.content
        if len(content) < 10240:  # < 10KB
            logger.debug("Crossref TDM: too small (%d bytes)", len(content))
            return None

        if content[:4] != b"%PDF":
            logger.debug("Crossref TDM: not a PDF (header: %r)", content[:8])
            return None

        out_dir = Path(download_dir) if download_dir else Path.home() / "Downloads" / "temp"
        out_dir.mkdir(parents=True, exist_ok=True)
        safe = re.sub(r'[\\/:*?"<>|]', "_", doi)[:60]
        out_path = out_dir / f"crossref_{safe}.pdf"
        out_path.write_bytes(content)
        logger.info("Crossref TDM: saved to %s", out_path)
        return out_path

    except Exception as e:
        logger.debug("Crossref TDM: download failed: %s", e)
        return None
