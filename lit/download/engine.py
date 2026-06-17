"""
lit/download/engine.py — PDF download engine for a single paper.

Extracts the core download logic from ``main.py``'s ``download_paper()``,
providing a clean standalone ``download_pdf()`` function.

Workflow:
  1. Resolve DOI → URL (if input is a DOI)
  2. Detect publisher from URL
  3. Connect to Chrome/Edge via CDP (``ChromiumHelper``)
  4. Get the publisher adapter, navigate to the paper page
  5. Locate PDF download URL via adapter's ``find_download_url()``
  6. Handle redirect resolution (Optica, Elsevier, etc.)
  7. Download PDF via browser fetch() or cookie-based requests
  8. Verify file (exists, >100 KB, starts with %%PDF)
  9. Return Path

Fallback: if direct CDP + adapter flow fails, runs ``main.py`` as subprocess
(keeps existing ``main.py`` available as a fallback).

Does NOT handle Zotero operations — that is the caller's responsibility.
"""

from __future__ import annotations

import logging
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from rich.console import Console

from lit.core.config import load as get_config
from lit.core.config import skill_base

# ──────────────────────────────────────────────────────────────────
# Resolve skill base directory so we can import root-level modules
# (chromium_helper, url_parser, publisher/adapters, download_monitor)
# ──────────────────────────────────────────────────────────────────
_SKILL_BASE = skill_base()
if str(_SKILL_BASE) not in sys.path:
    sys.path.insert(0, str(_SKILL_BASE))

from chromium_helper import ChromiumHelper
from download_monitor import DownloadMonitor
from url_parser import is_doi, resolve_doi, detect_publisher

# Publisher adapter registry (mirrors main.py)
from publisher.aaas import AAASAdapter
from publisher.acs import ACSAdapter
from publisher.aip import AIPAdapter
from publisher.elsevier import ElsevierAdapter
from publisher.npg import NPGAdapter
from publisher.optica import OpticaAdapter
from publisher.springer import SpringerAdapter
from publisher.pnas import PNASAdapter
from publisher.wiley import WileyAdapter
from publisher.aps import APSAdapter
from publisher.tandf import TandFAdapter
from publisher.rsc import RSCAdapter
from publisher.iop import IOPAdapter
from publisher.annualreviews import AnnualReviewsAdapter
from publisher.mdpi import MDPIAdapter
from publisher.frontiers import FrontiersAdapter
from publisher.elife import eLifeAdapter
from publisher.royalsociety import RoyalSocietyAdapter
from publisher.bmj import BMJAdapter
from publisher.ieee import IEEEAdapter
from publisher.spie import SPIEAdapter
from publisher.biorxiv import BiorxivAdapter
from publisher.jci_insight import JCIInsightAdapter

console = Console()
logger = logging.getLogger(__name__)

_ADAPTERS: dict[str, type] = {
    "aaas": AAASAdapter,
    "acs": ACSAdapter,
    "aip": AIPAdapter,
    "elsevier": ElsevierAdapter,
    "npg": NPGAdapter,
    "optica": OpticaAdapter,
    "springer": SpringerAdapter,
    "pnas": PNASAdapter,
    "wiley": WileyAdapter,
    "aps": APSAdapter,
    "tandf": TandFAdapter,
    "rsc": RSCAdapter,
    "iop": IOPAdapter,
    "annualreviews": AnnualReviewsAdapter,
    "mdpi": MDPIAdapter,
    "frontiers": FrontiersAdapter,
    "elife": eLifeAdapter,
    "royalsociety": RoyalSocietyAdapter,
    "bmj": BMJAdapter,
    "ieee": IEEEAdapter,
    "spie": SPIEAdapter,
    "biorxiv": BiorxivAdapter,
    "jci_insight": JCIInsightAdapter,
}

# ──────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────


def _get_adapter(publisher: str, config: dict):
    """Instantiate a publisher adapter by name.

    Returns ``None`` if the publisher is not registered.
    """
    adapter_cls = _ADAPTERS.get(publisher)
    if adapter_cls is None:
        return None
    return adapter_cls(config)


def _verify_pdf(filepath: Path) -> bool:
    """Verify the file looks like a genuine PDF.

    Checks:
      - File exists
      - Size > 100 KB
      - Header starts with ``%PDF``
    """
    if not filepath.exists():
        logger.error("File does not exist: %s", filepath)
        return False
    size = filepath.stat().st_size
    if size < 102400:  # 100 KB
        logger.error("File too small (%d bytes), not a valid PDF", size)
        return False
    with open(filepath, "rb") as f:
        header = f.read(4)
    if header != b"%PDF":
        logger.error("File does not start with %%PDF header: %r", header)
        return False
    logger.info("Verified PDF: %s (%.1f KB)", filepath, size / 1024.0)
    return True


def _fallback_subprocess(url: str, config: dict, timeout: int) -> Path:
    """Fallback: run ``main.py <URL>`` as a subprocess and parse the output.

    This mirrors ``zot.py``'s ``download_pdf()`` method exactly, so if the
    direct CDP + adapter flow fails, we can still download via the CLI.

    Raises:
        RuntimeError: if main.py is missing, times out, or fails to produce a PDF.
    """
    main_py = _SKILL_BASE / "main.py"
    if not main_py.exists():
        raise RuntimeError("main.py not found for subprocess fallback")

    download_dir = config.get("download", {}).get("temp_dir", "")
    cmd: list[str] = [
        sys.executable,
        str(main_py),
        url,
        "--config",
        str(_SKILL_BASE / "config.yaml"),
        "--fast",
        "--no-warmup",
    ]
    if download_dir:
        cmd.extend(["--output", download_dir])

    logger.info("Running fallback subprocess: %s", " ".join(cmd[:6]) + "...")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"main.py subprocess timed out after {timeout}s")

    # Parse output for the downloaded file path (same pattern as zot.py)
    output = result.stdout + result.stderr
    m = re.search(r"(?:Downloaded|Already exists):\s*([\s\S]+?\.pdf)", output)
    if m:
        raw = re.sub(r"\s+", " ", m.group(1)).strip()
        p = Path(raw)
        if p.exists():
            return p

    # Show last lines of output for diagnostic
    tail = "\n".join(output.splitlines()[-20:])
    logger.error("Fallback subprocess produced no PDF. Last output:\n%s", tail)
    raise RuntimeError("main.py subprocess did not produce a PDF file")


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────


def download_pdf(url_or_doi: str, timeout: int = 120) -> Path:
    """Download a paper's PDF given a URL or DOI.

    Args:
        url_or_doi:
            DOI (e.g. ``"10.1038/s41586-024-07208-4"``) or a full URL
            (e.g. ``"https://pubs.acs.org/doi/10.1021/..."``).
        timeout:
            Maximum seconds for the overall download operation (applied as a
            per-operation timeout; the full function may run longer across
            multiple retries/fallbacks).

    Returns:
        ``Path`` to the downloaded PDF file on disk.

    Raises:
        RuntimeError:
            If any step of the download fails (DOI resolution, CDP connection,
            page navigation, PDF retrieval, or file verification).

    Example:
        >>> from lit.download.engine import download_pdf
        >>> path = download_pdf("10.1021/acs.jmedchem.4c01234")
        >>> print(path)
        C:\\Users\\Ivanz\\Downloads\\temp\\paper.pdf
    """
    cfg = get_config()

    # ── 1. Resolve input ──────────────────────────────────────
    raw = url_or_doi.strip()
    if is_doi(raw):
        logger.info("Resolving DOI: %s", raw)
        url = resolve_doi(raw, timeout=min(timeout, 30))
        if url is None:
            raise RuntimeError("Failed to resolve DOI: %s" % raw)
    elif raw.startswith(("http://", "https://")):
        url = raw
    else:
        # Try as DOI anyway
        url = resolve_doi(raw, timeout=min(timeout, 30))
        if url is None:
            raise RuntimeError("Cannot parse input: %s" % raw)

    logger.info("Resolved URL: %s", url)

    # ── 2. Detect publisher ──────────────────────────────────
    publisher = detect_publisher(url)
    if publisher is None:
        raise RuntimeError("Unknown publisher for URL: %s" % url)
    logger.info("Detected publisher: %s", publisher)

    # ── 3. Direct CDP + adapter flow ─────────────────────────
    try:
        return _download_via_cdp(url, publisher, cfg, timeout)
    except Exception as exc:
        logger.warning(
            "Direct CDP download failed: %s. Trying subprocess fallback...", exc
        )

    # ── 4. Fallback: subprocess main.py ──────────────────────
    return _fallback_subprocess(url, cfg, timeout)


# ──────────────────────────────────────────────────────────────────
# Internal: CDP-based download flow
# ──────────────────────────────────────────────────────────────────


def _download_via_cdp(
    url: str,
    publisher: str,
    config: dict,
    timeout: int,
) -> Path:
    """Download a paper via CDP-connected browser + publisher adapter.

    This is the primary download path, extracted from ``main.py``'s
    ``download_paper()`` but stripped of:
      - Rich CLI progress / banner
      - Rate limiter / simulated reading delays
      - Zotero interactions
      - Multi-paper result aggregation

    Raises:
        RuntimeError: on any failure.
    """
    # 3a. Connect to Chromium via CDP
    browser_helper = ChromiumHelper(config)
    result = browser_helper.connect()
    if result is None:
        logger.info("CDP connection failed, attempting browser auto-launch...")
        browser_helper.launch_browser()
        for attempt in range(5):
            time.sleep(3)
            result = browser_helper.connect()
            if result is not None:
                break
            logger.info("  Retry %d/5...", attempt + 1)
        if result is None:
            raise RuntimeError("Cannot connect to Chromium via CDP")

    pw, browser = result

    try:
        # 3b. Get adapter
        adapter = _get_adapter(publisher, config)
        if adapter is None:
            raise RuntimeError("No adapter for publisher: %s" % publisher)

        # 3c. Get a page and navigate to the paper URL
        page, ctx = browser_helper.get_or_create_page(browser)

        logger.info("Navigating to: %s", url)
        if not adapter.navigate_to_paper(page, url):
            # Navigation failed — try a fresh tab
            logger.warning("Navigation failed on existing tab, trying new tab...")
            new_ctx = browser.contexts[0] if browser.contexts else browser.new_context()
            page = new_ctx.new_page()
            if not adapter.navigate_to_paper(page, url):
                raise RuntimeError("Failed to load page (even with new tab): %s" % url)

        # 3d. Check access
        if not adapter.check_access(page):
            raise RuntimeError("Access denied / no subscription for: %s" % url)

        # 3e. Extract metadata (for file naming) + find download URL
        paper_info = adapter.get_paper_metadata(page)
        title = (paper_info.title or "").strip()
        logger.info(
            "Paper: %s", (title[:80] + "...") if title else "(title not found)"
        )

        logger.info("Locating download URL...")
        pdf_url = adapter.find_download_url(page)
        if pdf_url is None:
            raise RuntimeError("Download URL not found in page DOM")

        logger.info("PDF URL: %s", pdf_url)

        # 3f. Redirect resolution (some publishers: Optica, Elsevier, AIP, ...)
        if hasattr(adapter, "resolve_pdf_url"):
            logger.info("Publisher requires redirect resolution...")
            article_url = page.url
            resolved_url = adapter.resolve_pdf_url(page, pdf_url)
            if resolved_url is None:
                raise RuntimeError("Failed to resolve PDF URL through redirects")
            pdf_url = resolved_url
            logger.info("Resolved PDF URL: %s", pdf_url)

            # Special flow: click-download (Elsevier Ctrl+P path)
            if pdf_url == "__click_download__":
                logger.info("Using click-download flow (PDF viewer)...")
                monitor = DownloadMonitor(config)
                filepath = adapter.click_download(monitor)
                if filepath is None:
                    raise RuntimeError("Click download failed (timeout or no file)")
                result_path = _rename_with_title(Path(filepath), title)
                if _verify_pdf(result_path):
                    return result_path
                raise RuntimeError(
                    "Click-download file is not a valid PDF: %s" % filepath
                )

        # 3g. Download via browser fetch()
        logger.info("Downloading PDF via browser fetch()...")
        monitor = DownloadMonitor(config)
        filepath = monitor.browser_download(page=page, pdf_url=pdf_url)

        # Fallback: cookie-based requests download
        if filepath is None:
            logger.info("fetch() download failed, trying cookie-based download...")
            filepath = monitor.cookie_download(
                ctx=ctx,
                pdf_url=pdf_url,
                referer=page.url,
            )

        # Adapter-level fallback (e.g. Elsevier CDN failure → Ctrl+P)
        if filepath is None and hasattr(adapter, "fallback_download"):
            logger.info("Cookie download failed, trying adapter fallback...")
            filepath = adapter.fallback_download(page, monitor, pdf_url)

        if filepath is None:
            raise RuntimeError("PDF download failed (all methods exhausted)")

        p = Path(filepath)

        # Rename with paper title if available
        result_path = _rename_with_title(p, title)

        if not _verify_pdf(result_path):
            raise RuntimeError(
                "Downloaded file is not a valid PDF: %s" % result_path
            )

        return result_path

    finally:
        # Cleanup: disconnect from CDP browser
        try:
            browser_helper.disconnect()
        except Exception:
            pass


# ──────────────────────────────────────────────────────────────────
# Utility
# ──────────────────────────────────────────────────────────────────


def _rename_with_title(path: Path, title: str) -> Path:
    """Rename a downloaded PDF to use the paper title as filename.

    If ``title`` is empty or the rename fails, returns the original path.
    """
    if not title:
        return path

    safe_name = re.sub(r'[<>:"/\\|?*]', "", title)
    safe_name = re.sub(r"\s+", " ", safe_name).strip()[:100]
    if not safe_name.endswith(".pdf"):
        safe_name += ".pdf"

    new_path = path.parent / safe_name
    if new_path.exists():
        return path  # don't overwrite

    try:
        path.rename(new_path)
        logger.info("Renamed to: %s", safe_name)
        return new_path
    except Exception as e:
        logger.warning("Rename failed: %s", e)
        return path
