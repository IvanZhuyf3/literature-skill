"""
lit/core/crossref.py — CrossRef DOI resolution and metadata query module.

Functions:
    resolve_doi(doi, timeout) -> str | None   — Resolve a DOI to its publisher landing page URL.
    search_by_title(title)     -> dict | None — Search CrossRef by title, return best match metadata.
    fetch_metadata(doi)        -> dict | None — Fetch CrossRef metadata for a specific DOI.
"""

from __future__ import annotations

import json
import logging
import re
import time
from typing import Optional
from urllib.parse import quote

import requests

from lit.core.config import load as get_config

logger = logging.getLogger(__name__)

# CrossRef API base URLs
CROSSREF_API = "https://api.crossref.org/works"
DOI_RESOLVER = "https://doi.org"

# Browser-like User-Agent to avoid being blocked
_BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)

# Polite pool: https://api.crossref.org/swagger-ui/index.html#/Works
_POLITE_UA = "LiteratureSkill/1.0 (mailto:user@example.com)"


def _strip_doi_prefix(raw: str) -> str:
    """Normalize a raw DOI string (strip scheme/doi: prefix)."""
    doi = raw.strip()
    if doi.startswith("https://doi.org/"):
        doi = doi[len("https://doi.org/"):]
    elif doi.startswith("http://doi.org/"):
        doi = doi[len("http://doi.org/"):]
    elif doi.startswith("doi:"):
        doi = doi[len("doi:"):].strip()
    return doi


def resolve_doi(doi: str, timeout: int = 15) -> str | None:
    """
    Resolve a DOI to its publisher landing page URL.

    Uses GET (not HEAD) — some publishers (e.g. RSC) abort HEAD requests
    or return incomplete responses.

    Args:
        doi: DOI string (e.g. "10.1021/acs.jmedchem.4c01234").
        timeout: Request timeout in seconds (default 15).

    Returns:
        Resolved publisher landing-page URL, or None on failure.
    """
    doi = _strip_doi_prefix(doi)
    url = f"{DOI_RESOLVER}/{doi}"
    logger.info("Resolving DOI: %s ...", doi)

    try:
        headers = {"User-Agent": _BROWSER_UA}
        response = requests.get(
            url,
            allow_redirects=True,
            timeout=timeout,
            stream=True,  # Don't download full body
            headers=headers,
        )
        resolved = response.url
        response.close()
        logger.info("DOI resolved to: %s", resolved)
        return resolved
    except Exception as exc:
        logger.error("DOI resolution failed: %s", exc)
        return None


def search_by_title(title: str) -> dict | None:
    """
    Search CrossRef by article title and return the best matching metadata.

    Queries the CrossRef REST API with a title search, retrieves up to 3
    results, and picks the best match based on title similarity.

    Args:
        title: Article title to search for.

    Returns:
        A dict with keys (doi, title, authors, journal, year,
        volume, issue, pages, ISSN, abstract, publisher, url)
        or None if no match is found.
    """
    if not title or not title.strip():
        logger.warning("search_by_title called with empty title")
        return None

    query = quote(title.strip())
    search_url = f"{CROSSREF_API}?query.title={query}&rows=3"
    headers = {"User-Agent": _POLITE_UA}

    logger.info("Searching CrossRef by title: %s", title[:80])

    try:
        resp = requests.get(search_url, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:
        logger.error("CrossRef title search failed: %s", exc)
        return None

    items = (data.get("message") or {}).get("items") or []
    if not items:
        logger.info("No results from CrossRef title search")
        return None

    # Pick the best match — simple heuristic: choose the first result
    # (CrossRef sorts by relevance).
    best = items[0]
    return _extract_work(best)


def fetch_metadata(doi: str) -> dict | None:
    """
    Fetch CrossRef metadata for a specific DOI.

    Args:
        doi: The DOI to look up (with or without https://doi.org/ prefix).

    Returns:
        A dict with keys (doi, title, authors, journal, year,
        volume, issue, pages, ISSN, abstract, publisher, url)
        or None if the DOI is not found or the request fails.
    """
    doi = _strip_doi_prefix(doi)
    url = f"{CROSSREF_API}/{quote(doi, safe='')}"
    headers = {"User-Agent": _POLITE_UA}

    logger.info("Fetching CrossRef metadata for DOI: %s", doi)

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.HTTPError as exc:
        if resp.status_code == 404:
            logger.warning("DOI not found in CrossRef: %s", doi)
        else:
            logger.error("CrossRef metadata HTTP error for %s: %s", doi, exc)
        return None
    except Exception as exc:
        logger.error("CrossRef metadata fetch failed for %s: %s", doi, exc)
        return None

    message = data.get("message")
    if not message:
        logger.warning("CrossRef returned empty message for DOI: %s", doi)
        return None

    return _extract_work(message)


def _extract_work(msg: dict) -> dict:
    """
    Extract structured metadata from a CrossRef 'work' message dict.

    Args:
        msg: The 'message' dict from a CrossRef API response.

    Returns:
        Normalised dict with keys:
            doi, title, authors, journal, year,
            volume, issue, pages, ISSN, abstract, publisher, url
    """
    # --- DOI ---
    doi = msg.get("DOI", "")

    # --- Title ---
    title_raw = msg.get("title") or []
    title = title_raw[0] if title_raw else ""

    # --- Authors ---
    authors_raw = msg.get("author") or []
    authors: list[str] = []
    for a in authors_raw:
        given = a.get("given", "")
        family = a.get("family", "")
        if family:
            authors.append(f"{given} {family}".strip())
        elif given:
            authors.append(given)

    # --- Journal / container ---
    container = msg.get("container-title") or []
    journal = container[0] if container else (
        msg.get("short-container-title") or [""]
    )[0]

    # --- Year (from published-print, published-online, or issued) ---
    year = _extract_year(msg)

    # --- Volume, Issue, Pages ---
    volume = msg.get("volume") or ""
    issue = msg.get("issue") or ""
    pages = msg.get("page") or ""

    # --- ISSN ---
    issn_list = msg.get("ISSN") or []
    issn = issn_list[0] if issn_list else ""

    # --- Abstract ---
    abstract = msg.get("abstract", "")

    # --- Publisher ---
    publisher = msg.get("publisher", "")

    # --- URL ---
    url = msg.get("URL", "")

    # --- Citation count ---
    citations = msg.get("is-referenced-by-count", 0)

    return {
        "doi": doi,
        "title": title,
        "authors": authors,
        "journal": journal,
        "year": year,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "ISSN": issn,
        "abstract": abstract,
        "publisher": publisher,
        "url": url,
        "citations": citations,
    }


def _extract_year(msg: dict) -> str:
    """Extract the publication year from a CrossRef message dict."""
    for date_field in ("published-print", "published-online", "issued"):
        parts = (msg.get(date_field) or {}).get("date-parts")
        if parts and len(parts) > 0 and len(parts[0]) > 0:
            return str(parts[0][0])
    return ""
