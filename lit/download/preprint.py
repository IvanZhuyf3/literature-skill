"""
lit/download/preprint.py — arXiv 预印本直连下载。

arXiv 无反爬，URL 可预测，纯 HTTP 秒级下载。
bioRxiv/medRxiv 有 Cloudflare 保护，纯 HTTP 会被 403，需要走 attach（CDP adapter）。

Usage:
    from lit.download.preprint import try_preprint
    pdf_path = try_preprint("10.48550/arXiv.2603.25534")
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

import requests

from lit.core.config import load as get_config

logger = logging.getLogger(__name__)

_BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def try_preprint(
    doi: str,
    year: str | int | None = None,
) -> Path | None:
    """Download a preprint PDF from bioRxiv/medRxiv/arXiv.

    Detects the preprint server from the DOI prefix and constructs
    the direct PDF URL.

    Args:
        doi:  DOI string (e.g. "10.1101/2025.03.26.645466").
        year: Publication year (unused).

    Returns:
        Path to downloaded PDF, or None.
    """
    if not doi or not doi.strip():
        return None

    doi = doi.strip()

    # Determine PDF URL based on DOI prefix
    pdf_urls = _get_pdf_urls(doi)
    if not pdf_urls:
        return None

    for url in pdf_urls:
        logger.info("Preprint: trying %s", url[:80])
        pdf_path = _download_pdf(url, doi)
        if pdf_path:
            return pdf_path

    logger.info("Preprint: no accessible PDF for %s", doi)
    return None


def _get_pdf_urls(doi: str) -> list[str]:
    """Construct candidate PDF URLs from DOI prefix."""
    urls = []

    # bioRxiv: 10.1101/...
    if doi.startswith("10.1101/"):
        # https://www.biorxiv.org/content/10.1101/2025.03.26.645466v1.full.pdf
        # Try v1 first (most common), then versionless
        suffix = doi[len("10.1101/"):]
        urls.append(f"https://www.biorxiv.org/content/10.1101/{suffix}v1.full.pdf")
        urls.append(f"https://www.biorxiv.org/content/{doi}v1.full.pdf")

    # medRxiv: 10.1101/... (same prefix, server auto-detects)
    # bioRxiv and medRxiv share the 10.1101 prefix, handled above

    # arXiv DOIs: 10.48550/arXiv.2401.12345
    if doi.startswith("10.48550/arXiv."):
        arxiv_id = doi[len("10.48550/arXiv."):]
        urls.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")

    # ChemRxiv: 10.26434/chemrxiv-...
    if doi.startswith("10.26434/chemrxiv"):
        # ChemRxiv doesn't have a predictable PDF URL pattern
        # Fall through — Unpaywall or publisher adapter can handle it
        pass

    return urls


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
            logger.debug("Preprint: %s returned %d", url[:60], resp.status_code)
            return None

        content = resp.content
        if len(content) < 10240:
            logger.debug("Preprint: too small (%d bytes)", len(content))
            return None

        if content[:4] != b"%PDF":
            logger.debug("Preprint: not a PDF (header: %r)", content[:8])
            return None

        out_dir = Path(download_dir) if download_dir else Path.home() / "Downloads" / "temp"
        out_dir.mkdir(parents=True, exist_ok=True)
        safe = re.sub(r'[\\/:*?"<>|]', "_", doi)[:60]
        out_path = out_dir / f"preprint_{safe}.pdf"
        out_path.write_bytes(content)
        logger.info("Preprint: saved to %s", out_path)
        return out_path

    except Exception as e:
        logger.debug("Preprint: download failed: %s", e)
        return None
