"""
lit/download/scihub_native.py — Sci-Hub download via browser-native navigation.

Anti-detection lessons (from comparing AHK script vs old scihub_cdp.py):

  AHK script works because:
    - Run, url → OS-level browser launch, zero automation fingerprint
    - PixelGetColor + Click → Windows API injection, invisible to browser
    - DDoS-Guard sees a perfectly normal browser session

  Old scihub_cdp.py got CAPTCHA'd because:
    - page.evaluate(fetch()) → injects JS, makes API calls from page context
    - page.request.get() → Playwright API request, detectable
    - requests.get() → separate HTTP client, different TLS fingerprint
    - All three are "too sophisticated" for a normal user

  This module's approach:
    - page.goto() for navigation (same as typing URL in address bar)
    - page.query_selector() for DOM inspection (read-only, no JS injection)
    - page.goto(pdf_url) for download (browser-native navigation)
    - CDP Browser.setDownloadBehavior to force download path
    - Random delays + mouse movement throughout
    - NEVER: page.evaluate(), page.request.get(), requests.get()

Usage:
    from lit.download.scihub_native import try_scihub
    pdf_path = try_scihub("10.1234/example", year=2021)
"""
from __future__ import annotations

import logging
import random
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright

from lit.core.config import load as get_config

logger = logging.getLogger(__name__)

_MAX_YEAR = 2021
_BLACKLIST_DURATION = 3600  # 1 hour cooldown per mirror

# ── Mirror blacklist (runtime, with expiry) ─────────────────────────────────
_blacklist: dict[str, float] = {}  # mirror_url → blacklist timestamp

# ── Persistent browser connection (reused across calls) ─────────────────────
_pw = None
_browser = None

# ── Detection patterns ──────────────────────────────────────────────────────
_CAPTCHA_PATTERNS = (
    "are you human", "are you a robot", "captcha",
    "robot check", "prove you are", "cloudflare",
    "attention required", "ddos protection",
    "just a moment",
)

_NOT_FOUND_PATTERNS = (
    "article is not available through sci-hub",
    "no articles found for your request",
    "i do not have any papers matching your request",
    "not available through sci-hub",
    "статья относительно новой",
    "published after 2021",
    "sci-hub doesn't have this paper",
    "could not retrieve",
)

_NOT_FOUND = object()  # sentinel: DOI not in Sci-Hub DB


# ── Helpers ─────────────────────────────────────────────────────────────────

def _rsleep(min_s: float, max_s: float):
    """Random sleep to mimic human timing."""
    time.sleep(random.uniform(min_s, max_s))


def _is_blacklisted(mirror: str) -> bool:
    if mirror in _blacklist:
        if time.time() - _blacklist[mirror] < _BLACKLIST_DURATION:
            return True
        del _blacklist[mirror]
    return False


def _do_blacklist(mirror: str, mirrors: list[str]):
    _blacklist[mirror] = time.time()
    dead = sum(1 for m in mirrors if _is_blacklisted(m))
    logger.warning(
        "Sci-Hub: CAPTCHA on %s — blacklisted (%d/%d mirrors dead)",
        mirror, dead, len(mirrors),
    )


def _get_mirrors() -> list[str]:
    cfg = get_config()
    mirrors = cfg.get("scihub", {}).get("mirrors", ["https://sci-hub.su"])
    if isinstance(mirrors, str):
        mirrors = [mirrors]
    return [m.rstrip("/") for m in mirrors]


def _ensure_browser():
    """Connect to existing Edge via CDP. Does NOT launch new browser."""
    global _pw, _browser
    if _browser:
        try:
            _browser.contexts  # health check
            return _browser
        except Exception:
            pass
    if _pw:
        try:
            _pw.stop()
        except Exception:
            pass

    cfg = get_config()
    cdp_url = cfg.get("chrome", {}).get("cdp_url", "http://127.0.0.1:19222")
    _pw = sync_playwright().start()
    _browser = _pw.chromium.connect_over_cdp(cdp_url)
    logger.info("Sci-Hub: connected to Edge via CDP at %s", cdp_url)
    return _browser


def close_browser():
    """Disconnect from CDP. Call at program exit."""
    global _pw, _browser
    if _pw:
        try:
            _pw.stop()
        except Exception:
            pass
    _pw = None
    _browser = None


def _simulate_human(page):
    """Random mouse movement + scroll to look less robotic."""
    try:
        page.mouse.move(random.randint(200, 1000), random.randint(200, 800))
        _rsleep(0.3, 0.8)
        page.mouse.wheel(0, random.randint(30, 150))
        _rsleep(0.5, 1.0)
    except Exception:
        pass


# ── DOM analysis (read-only, no JS injection) ───────────────────────────────

def _find_pdf_url(page) -> str | None:
    """Extract PDF URL from Sci-Hub page using CSS selectors.

    Uses page.query_selector() (DOM read) instead of page.evaluate() (JS exec).
    """
    # CSS selectors for PDF embed/iframe/download link
    selectors = [
        ("embed#pdf", "src"),
        ("iframe#pdf", "src"),
        ("embed[type='application/pdf']", "src"),
        ("iframe[src*='.pdf']", "src"),
        ("object[data*='.pdf']", "data"),
        ("#download", "href"),
        ("#buttons a[href]", "href"),
        ("a[download]", "href"),
        ("a[href*='.pdf']", "href"),
    ]

    for selector, attr in selectors:
        try:
            el = page.query_selector(selector)
            if el:
                url = el.get_attribute(attr)
                if url and ".pdf" in url.lower():
                    logger.info("Sci-Hub: PDF URL from %s", selector)
                    return _make_absolute(url, page.url)
        except Exception:
            continue

    # Regex fallback on page content (handles citation_pdf_url meta tag)
    try:
        html = page.content()
        for pattern in (
            r'citation_pdf_url.*?content=["\']([^"\']+)',
            r'(?:src|data|href)=["\']([^"\']+\.pdf[^"\']*)["\']',
            r'(https?://\S+?\.pdf)',
        ):
            m = re.search(pattern, html, re.IGNORECASE)
            if m:
                logger.info("Sci-Hub: PDF URL from regex")
                return _make_absolute(m.group(1).split("#")[0], page.url)
    except Exception:
        pass

    logger.info("Sci-Hub: no PDF URL found in page")
    return None


def _make_absolute(url: str, base: str) -> str:
    """Convert relative URL to absolute."""
    url = url.split("#")[0]  # strip fragment
    if url.startswith(("http://", "https://")):
        return url
    if url.startswith("//"):
        return "https:" + url
    return urljoin(base, url)


def _check_page_state(page) -> str:
    """Check page content for CAPTCHA / not-found / OK.

    Returns: 'captcha', 'not_found', or 'ok'
    """
    try:
        html = page.content()[:8000].lower()
    except Exception:
        return "ok"  # can't read, assume ok

    for pat in _CAPTCHA_PATTERNS:
        if pat in html:
            return "captcha"

    for pat in _NOT_FOUND_PATTERNS:
        if pat in html:
            return "not_found"

    return "ok"


# ── Browser-native download ─────────────────────────────────────────────────

def _download_via_browser(page, pdf_url: str, download_dir: Path, doi: str) -> Path | None:
    """Download PDF using browser-native navigation only.

    No fetch(), no page.request.get(), no requests.get().
    The browser itself downloads the file — we just watch the filesystem.
    """
    download_dir.mkdir(parents=True, exist_ok=True)
    safe_doi = re.sub(r'[\\/:*?"<>|]', "_", doi)[:60]
    target = download_dir / f"scihub_{safe_doi}.pdf"

    # Snapshot existing files to detect new downloads
    before = {f.name for f in download_dir.glob("*.pdf")}
    before |= {f.name for f in download_dir.glob("*.crdownload")}

    # Set CDP download behavior to force download (not open in viewer)
    try:
        client = page.context.new_cdp_session(page)
        client.send("Browser.setDownloadBehavior", {
            "behavior": "allow",
            "downloadPath": str(download_dir.resolve()),
        })
    except Exception as e:
        logger.debug("Sci-Hub: CDP download behavior setup failed: %s", e)

    # Simulate human: pause, move mouse before action
    _simulate_human(page)
    _rsleep(0.5, 1.5)

    # Navigate to PDF URL — browser handles it natively
    # Content-Disposition: attachment → browser downloads
    # If viewer opens instead, we check filesystem for partial downloads
    try:
        page.goto(pdf_url, wait_until="commit", timeout=30_000)
    except Exception as e:
        logger.debug("Sci-Hub: navigation to PDF returned: %s", str(e)[:80])

    # Poll for file appearance (check every 2s, up to 30s)
    for attempt in range(15):
        _rsleep(1.5, 3.0)

        # Check for new .pdf files
        new_pdfs = [f for f in download_dir.glob("*.pdf")
                    if f.name not in before and f.stat().st_size > 10240]
        if new_pdfs:
            # Pick the most recently modified
            pdf = max(new_pdfs, key=lambda f: f.stat().st_mtime)
            try:
                if pdf != target:
                    pdf.rename(target)
            except Exception:
                target = pdf  # use original path
            logger.info("Sci-Hub: ✓ downloaded via browser navigation (%d bytes)",
                        target.stat().st_size)
            return target

        # Check for .crdownload (Chrome partial download in progress)
        crdownloads = [f for f in download_dir.glob("*.crdownload")
                       if f.name not in before]
        if crdownloads:
            continue  # still downloading, keep waiting

    logger.info("Sci-Hub: no PDF appeared in download dir after 30s")
    return None


# ── Single mirror attempt ───────────────────────────────────────────────────

def _try_mirror(doi: str, mirror: str, download_dir: str) -> Path | None | object:
    """Try one mirror. Returns Path, None (failed), or _NOT_FOUND."""
    url = f"{mirror}/{doi.lstrip('/')}"
    logger.info("Sci-Hub: navigating to %s", url)

    page = None
    try:
        browser = _ensure_browser()
        ctx = browser.contexts[0] if browser.contexts else browser.new_context()
        page = ctx.new_page()

        # ── Navigate (browser-native, like typing URL) ──
        page.goto(url, wait_until="domcontentloaded", timeout=30_000)

        # ── Wait for DDoS-Guard challenge to resolve ──
        # Poll page title: DDoS-Guard shows "Just a moment..." or similar
        for attempt in range(10):
            _rsleep(2, 4)
            title = page.title()
            if title.strip() and not any(
                kw in title.lower() for kw in ("just a moment", "checking", "ddos")
            ):
                logger.info("Sci-Hub: DDoS-Guard resolved → %s", title[:50])
                break
            logger.info("Sci-Hub: waiting for DDoS-Guard (%d/10)...", attempt + 1)
        else:
            logger.warning("Sci-Hub: DDoS-Guard did not resolve on %s", mirror)
            return None

        # ── Extra human-like delay after challenge resolves ──
        _rsleep(2, 5)
        _simulate_human(page)

        # ── Check page state ──
        state = _check_page_state(page)
        if state == "captcha":
            return "captcha"
        if state == "not_found":
            logger.info("Sci-Hub: paper not available for %s", doi)
            return _NOT_FOUND

        # ── Find PDF URL in DOM ──
        _rsleep(1, 2)
        pdf_url = _find_pdf_url(page)
        if not pdf_url:
            return None

        logger.info("Sci-Hub: PDF URL: %s", pdf_url[:100])

        # ── Download via browser-native navigation ──
        _rsleep(1, 3)  # human-like pause before clicking download
        result = _download_via_browser(page, pdf_url, Path(download_dir), doi)

        if result:
            # Human-like delay after successful download (reading the paper)
            _rsleep(3, 7)

        return result

    except Exception as e:
        logger.warning("Sci-Hub: error on %s: %s", mirror, str(e)[:100])
        return None
    finally:
        if page:
            try:
                page.close()
            except Exception:
                pass


# ── Public API ──────────────────────────────────────────────────────────────

def try_scihub(
    doi: str,
    year: str | int | None = None,
) -> Path | None:
    """Download a paper PDF from Sci-Hub using browser-native navigation.

    Anti-detection: page.goto() + page.query_selector() only.
    No fetch(), no page.request, no requests.get().
    Random delays + mouse movement throughout.

    Args:
        doi: DOI string (e.g. "10.1038/s41586-024-07208-4")
        year: Publication year (papers after max_year are skipped)

    Returns:
        Path to downloaded PDF, or None if all mirrors failed.
    """
    cfg = get_config()
    scihub_cfg = cfg.get("scihub", {})
    max_year = scihub_cfg.get("max_year", _MAX_YEAR)

    # Year gate
    if year is not None:
        try:
            y = int(str(year).strip()[:4])
            if y > max_year:
                logger.info("Sci-Hub: skipped (year %s > %d)", year, max_year)
                return None
        except (ValueError, TypeError):
            pass

    if not doi:
        return None

    mirrors = _get_mirrors()

    # Filter alive mirrors + shuffle order (unpredictable)
    alive = [m for m in mirrors if not _is_blacklisted(m)]
    if not alive:
        logger.info("Sci-Hub: all mirrors blacklisted, skipping %s", doi)
        return None
    random.shuffle(alive)

    download_dir = cfg.get("download", {}).get("temp_dir", "")
    if not download_dir:
        download_dir = str(Path.home() / "Downloads" / "temp")

    # Random initial delay (anti-detection — don't hammer immediately)
    _rsleep(1, 3)

    for mirror in alive:
        result = _try_mirror(doi, mirror, download_dir)

        if isinstance(result, Path):
            return result  # success

        if result is _NOT_FOUND:
            return None  # not in Sci-Hub DB, no point trying other mirrors

        if result == "captcha":
            _do_blacklist(mirror, mirrors)
            _rsleep(3, 8)  # longer delay after CAPTCHA
            continue

        # None = transient failure, try next mirror
        _rsleep(2, 5)  # inter-mirror delay

    logger.info("Sci-Hub: all mirrors exhausted for %s", doi)
    return None
