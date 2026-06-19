"""
lit/download/unpaywall.py — Unpaywall OA PDF download.

Query Unpaywall API for open access PDF locations.
Download the best OA location.

No API key needed. Just needs an email (config: unpaywall.email).
Without email, uses a placeholder (may be rate-limited).

Usage:
    from lit.download.unpaywall import try_unpaywall
    pdf_path = try_unpaywall("10.1038/s41586-021-03819-2")
"""
from __future__ import annotations

import logging
import re
from pathlib import Path
from urllib.parse import quote

import requests

from lit.core.config import load as get_config

logger = logging.getLogger(__name__)

_UNPAYWALL_API = "https://api.unpaywall.org/v2"
_BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def try_unpaywall(
    doi: str,
    year: str | int | None = None,
) -> Path | None:
    """Query Unpaywall for OA PDF and download.

    Args:
        doi:  DOI string.
        year: Publication year (unused — no year gate for Unpaywall).

    Returns:
        Path to downloaded PDF, or None.
    """
    if not doi or not doi.strip():
        return None

    doi = doi.strip()
    cfg = get_config()
    email = cfg.get("unpaywall", {}).get("email", "").strip()
    if not email:
        email = "lit-skill@example.edu"  # fallback placeholder

    # Don't URL-encode the slashes in DOI — Unpaywall expects raw DOI in path
    url = f"{_UNPAYWALL_API}/{doi}?email={email}"
    headers = {"User-Agent": _BROWSER_UA}

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logger.warning("Unpaywall: API query failed for %s: %s", doi, e)
        return None

    # Try best_oa_location first, then oa_locations list
    best = data.get("best_oa_location")
    all_locs = data.get("oa_locations") or []

    candidates = []
    if best:
        candidates.append(best)
    for loc in all_locs:
        if loc not in candidates:
            candidates.append(loc)

    for loc in candidates:
        pdf_url = loc.get("url_for_pdf") or ""
        if not pdf_url:
            # Fall back to landing page (not ideal but some only have this)
            continue

        logger.info("Unpaywall: trying %s", pdf_url[:80])
        pdf_path = _download_pdf(pdf_url, doi)
        if pdf_path:
            return pdf_path

    logger.info("Unpaywall: no accessible OA PDF for %s", doi)
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
            logger.debug("Unpaywall: %s returned %d", url[:60], resp.status_code)
            return None

        content = resp.content
        if len(content) < 10240:  # < 10KB
            logger.debug("Unpaywall: too small (%d bytes)", len(content))
            return None

        if content[:4] != b"%PDF":
            logger.debug("Unpaywall: not a PDF (header: %r)", content[:8])
            return None

        out_dir = Path(download_dir) if download_dir else Path.home() / "Downloads" / "temp"
        out_dir.mkdir(parents=True, exist_ok=True)
        safe = re.sub(r'[\\/:*?"<>|]', "_", doi)[:60]
        out_path = out_dir / f"unpaywall_{safe}.pdf"
        out_path.write_bytes(content)
        logger.info("Unpaywall: saved to %s", out_path)
        return out_path

    except Exception as e:
        logger.debug("Unpaywall: download failed: %s", e)
        return None
