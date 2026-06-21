"""
lit/download/scihub_cdp.py — Sci-Hub PDF download via CDP (Edge browser).

用已有的 Edge CDP 连接打开 Sci-Hub 页面，让浏览器自然过 DDoS-Guard，
然后从页面 HTML 提取 PDF URL，通过浏览器 fetch API 下载（带 DDoS-Guard cookie）。

支持多镜像轮转：config 的 scihub.mirrors 列表配置多个镜像，
请求时轮流使用，captcha 检测到时自动拉黑当前镜像并切换下一个。
所有镜像都被拉黑后才全局熔断。

不新开浏览器，不影响用户正常使用。

Usage:
    from lit.download.scihub_cdp import try_scihub
    pdf_path = try_scihub("10.1234/example", year=2021)
    # -> Path to downloaded PDF, or None
"""
from __future__ import annotations

import logging
import os
import random
import re
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

from lit.core.config import load as get_config

logger = logging.getLogger(__name__)

_DEFAULT_MIRRORS = ["https://sci-hub.ru", "https://sci-hub.ee", "https://sci-hub.st"]
_MAX_YEAR = 2021

# ── Mirror rotation state ───────────────────────────────────────────────────
_mirrors: list[str] = []           # populated on first call from config
_blacklisted: set[str] = set()     # mirrors that hit captcha this session
_mirror_idx = 0                    # round-robin counter

# Min seconds between Sci-Hub requests (polite throttling)
_MIN_INTERVAL = 5
_last_request_time = 0.0

# ── Persistent browser (reused across calls) ────────────────────────────────
_pw = None
_browser = None


def _ensure_browser():
    """Get or lazily launch the persistent Playwright Chromium browser."""
    global _pw, _browser
    if _browser:
        try:
            _browser.contexts  # health check
            return _browser
        except Exception:
            pass  # dead, relaunch
    if _pw:
        try:
            _pw.stop()
        except Exception:
            pass
    _pw = sync_playwright().start()
    _browser = _pw.chromium.launch(headless=False)
    logger.info("Sci-Hub: launched persistent Chromium browser")
    return _browser


def close_browser():
    """Close the persistent browser. Call at program exit."""
    global _pw, _browser
    if _browser:
        try:
            _browser.close()
        except Exception:
            pass
    if _pw:
        try:
            _pw.stop()
        except Exception:
            pass
    _browser = None
    _pw = None

_CAPTCHA_PATTERNS = (
    "are you human", "are you a robot", "captcha",
    "robot check", "prove you are", " cloudflare",
    "attention required", "ddos protection",
)

_NOT_FOUND_PATTERNS = (
    # English mirrors (.st .su .box .red .ru)
    "article is not available through sci-hub",
    "no articles found for your request",
    "i do not have any papers matching your request",
    "not available through sci-hub",
    # Russian mirror (.ru)
    "статья относительно новой",
    "published after 2021",
    # Generic fallbacks
    "doesn't exist", "no paper",
    "sci-hub doesn't have this paper",
    "could not retrieve",
    "i do not have any papers matching",
    "no articles found for your request",
)

# Sentinel: DOI not in Sci-Hub DB (all mirrors share the same DB, no point retrying)
_NOT_FOUND = object()


def _get_mirrors() -> list[str]:
    """Load mirror list from config (cached after first call)."""
    global _mirrors
    if _mirrors:
        return _mirrors
    cfg = get_config()
    scihub_cfg = cfg.get("scihub", {})
    mirrors = scihub_cfg.get("mirrors")
    if not mirrors:
        # backward compat: single base_url
        base = scihub_cfg.get("base_url")
        mirrors = [base] if base else list(_DEFAULT_MIRRORS)
    _mirrors = [m.rstrip("/") for m in mirrors]
    return _mirrors


def _pick_mirror() -> str | None:
    """Round-robin pick the next non-blacklisted mirror, or None if all dead."""
    global _mirror_idx
    mirrors = _get_mirrors()
    available = [m for m in mirrors if m not in _blacklisted]
    if not available:
        return None
    # Round-robin among available mirrors
    m = available[_mirror_idx % len(available)]
    _mirror_idx += 1
    return m


def _all_blacklisted() -> bool:
    """True if every mirror has been blacklisted."""
    return len(_blacklisted) >= len(_get_mirrors())


def try_scihub(
    doi: str,
    year: str | int | None = None,
) -> Path | None:
    """
    Open Sci-Hub in CDP browser, sniff for PDF URL, download it.

    Tries multiple mirrors in rotation. If a mirror shows captcha/robot
    check, it is blacklisted for the session and the next mirror is tried.
    If all mirrors are blacklisted or exhausted, returns None.

    Args:
        doi:  The DOI string (e.g. "10.1038/s41586-021-03819-2").
        year: Publication year. If > max_year, skips silently.

    Returns:
        ``Path`` to the downloaded PDF, or ``None``.
    """
    global _last_request_time

    cfg = get_config()
    scihub_cfg = cfg.get("scihub", {})
    max_year = scihub_cfg.get("max_year", _MAX_YEAR)
    download_dir = scihub_cfg.get(
        "download_dir",
        cfg.get("download", {}).get("temp_dir", ""),
    )

    # ── All mirrors blacklisted? ──
    if _all_blacklisted():
        logger.info("Sci-Hub CDP: all mirrors blacklisted, skipping %s", doi)
        return None

    # Year gate
    if year is not None:
        try:
            y = int(str(year).strip()[:4])
            if y > max_year:
                logger.info("Sci-Hub CDP: skipped (year %s > %d)", year, max_year)
                return None
        except (ValueError, TypeError):
            pass

    if not doi:
        return None

    # ── Try mirrors in rotation ──
    mirrors = _get_mirrors()
    tried = set()
    for _ in range(len(mirrors)):
        mirror = _pick_mirror()
        if mirror is None or mirror in tried:
            break
        tried.add(mirror)

        # ── Throttle before every Sci-Hub request ──
        elapsed = time.time() - _last_request_time
        if elapsed < _MIN_INTERVAL:
            time.sleep(_MIN_INTERVAL - elapsed)

        result = _try_one_mirror(doi, mirror, download_dir)
        if isinstance(result, Path):
            return result           # success
        if result is _NOT_FOUND:
            return None             # not in Sci-Hub DB, no point trying other mirrors
        # result is None → captcha or transient error, try next mirror

    logger.info("Sci-Hub CDP: all mirrors exhausted for %s", doi)
    return None


def _try_one_mirror(
    doi: str,
    base_url: str,
    download_dir: str,
) -> Path | type[_NOT_FOUND] | None:
    """
    Attempt download from a single mirror using Playwright's own Chromium.

    Returns:
        Path on success.
        _NOT_FOUND if DOI is not in Sci-Hub DB (don't try other mirrors).
        None if captcha/robot check or transient error (try next mirror).
    """
    global _last_request_time

    url = f"{base_url}/{doi.lstrip('/')}"
    logger.info("Sci-Hub: navigating to %s", url)

    page = None

    try:
        browser = _ensure_browser()
        ctx = browser.new_context()
        page = ctx.new_page()

        # Navigate — browser handles DDoS-Guard automatically
        _last_request_time = time.time()
        page.goto(url, wait_until="domcontentloaded", timeout=30_000)

        # Wait up to 40s for DDoS-Guard to resolve
        ddos_resolved = False
        for _ in range(40):
            time.sleep(1)
            title = page.title()
            if "DDoS" not in title and "Checking" not in title and title.strip():
                ddos_resolved = True
                logger.info("Sci-Hub CDP: DDoS-Guard resolved at %s", title[:60])
                break

        if not ddos_resolved:
            logger.warning("Sci-Hub CDP: DDoS-Guard did not resolve for %s", doi)
            return None

        # Let the page stabilize after DDoS-Guard resolves
        try:
            page.wait_for_load_state("networkidle", timeout=15_000)
        except Exception:
            pass

        # ── Wait 5+rand(0,2)s before grabbing PDF — let page fully render ──
        _wait = 5 + random.random() * 2
        time.sleep(_wait)
        logger.info("Sci-Hub CDP: page settled after %.1fs", _wait)

        # Get page HTML
        html = ""
        for _ in range(5):
            try:
                html = page.content()
                break
            except Exception:
                time.sleep(2)

        body_lower = html[:5000].lower()

        # ── Captcha / robot check → blacklist THIS mirror, try next ──
        for pat in _CAPTCHA_PATTERNS:
            if pat in body_lower:
                _blacklisted.add(base_url)
                logger.warning(
                    "Sci-Hub CDP: CAPTCHA on %s — blacklisted (%d/%d mirrors dead)",
                    base_url, len(_blacklisted), len(_get_mirrors()),
                )
                return None

        # ── Not available → same DB on all mirrors, stop ──
        for pat in _NOT_FOUND_PATTERNS:
            if pat in body_lower:
                logger.info("Sci-Hub CDP: paper not available for %s", doi)
                return _NOT_FOUND

        # ── Extract PDF URL ──
        # Detect actual page origin (Sci-Hub may redirect to sci-net.xyz etc.)
        from urllib.parse import urlparse
        parsed = urlparse(page.url)
        page_origin = f"{parsed.scheme}://{parsed.netloc}"  # https://sci-net.xyz

        pdf_url = None

        # Method 1: JS querySelector for iframe/embed/object (browser auto-decodes HTML entities)
        for selector, attr in [
            ("iframe[src]", "src"),
            ("embed[src]", "src"),
            ("object[data]", "data"),
        ]:
            try:
                el_url = page.evaluate(f"""
                    () => {{
                        const el = document.querySelector('{selector}');
                        return el ? el.{attr} : null;
                    }}
                """)
                if el_url and ".pdf" in el_url.lower():
                    pdf_url = el_url
                    logger.info("Sci-Hub CDP: PDF URL from %s: %s", selector, pdf_url[:100])
                    break
            except Exception:
                pass

        # Method 2: regex fallback on HTML (handles citation_pdf_url meta tag)
        if not pdf_url:
            for pat in (
                r'citation_pdf_url.*?content=["\']([^"\']+)',
                r'<object[^>]*data=["\']([^"\']+\.pdf)["\']',
                r'<embed[^>]*src=["\']([^"\']+\.pdf)["\']',
                r'class=["\']download["\'][^>]*>.*?<a[^>]*href=["\']([^"\']+\.pdf)',
            ):
                m = re.search(pat, html, re.IGNORECASE | re.DOTALL)
                if m:
                    pdf_url = m.group(1)
                    logger.info("Sci-Hub CDP: PDF URL from regex: %s", pdf_url[:100])
                    break

        if not pdf_url:
            logger.info("Sci-Hub CDP: no PDF URL found in page for %s", doi)
            return None

        # Strip fragment (e.g. #view=FitH)
        pdf_url = pdf_url.split("#")[0]

        # Make absolute — use page_origin (handles sci-net.xyz redirects)
        if pdf_url.startswith("https://") or pdf_url.startswith("http://"):
            pass  # already absolute
        elif pdf_url.startswith("//"):
            pdf_url = "https:" + pdf_url
        elif pdf_url.startswith("/"):
            pdf_url = page_origin + pdf_url

        logger.info("Sci-Hub CDP: PDF URL found: %s", pdf_url[:100])

        # Download PDF via Playwright request API.
        # page.request.get() uses browser cookies (DDoS-Guard session) but
        # bypasses Edge tracking prevention that blocks page.evaluate(fetch()).
        pdf_data = None

        # Attempt 1-2: Playwright request API (bypasses tracking prevention)
        for attempt in range(2):
            try:
                resp = page.request.get(pdf_url, timeout=30_000)
                if resp.ok:
                    body = resp.body()
                    if body and len(body) > 100:
                        pdf_data = body
                        break
                logger.info("Sci-Hub CDP: request attempt %d got HTTP %s for %s",
                            attempt+1, resp.status, doi)
            except Exception as req_err:
                logger.info("Sci-Hub CDP: request attempt %d failed for %s: %s",
                            attempt+1, doi, req_err)
            if attempt < 1:
                time.sleep(3)

        # Attempt 3: browser fetch fallback (works for same-origin storage)
        if not pdf_data:
            try:
                import base64 as _b64
                b64_data = page.evaluate("""
                    async (url) => {
                        const resp = await fetch(url);
                        if (!resp.ok) throw new Error('HTTP ' + resp.status);
                        const blob = await resp.blob();
                        const buf = await blob.arrayBuffer();
                        const bytes = new Uint8Array(buf);
                        let binary = '';
                        const chunk = 8192;
                        for (let i = 0; i < bytes.length; i += chunk) {
                            binary += String.fromCharCode.apply(null, bytes.subarray(i, i + chunk));
                        }
                        return btoa(binary);
                    }
                """, pdf_url)
                pdf_data = _b64.b64decode(b64_data)
            except Exception:
                pass

        if not pdf_data or len(pdf_data) < 100:
            logger.warning("Sci-Hub CDP: could not download PDF for %s after all attempts", doi)
            return None
        if pdf_data[:4] != b"%PDF":
            logger.warning("Sci-Hub CDP: downloaded content is not a PDF for %s", doi)
            return None

        # Save
        out_dir = Path(download_dir) if download_dir else Path.home() / "Downloads" / "temp"
        out_dir.mkdir(parents=True, exist_ok=True)
        safe = re.sub(r'[\\/:*?"<>|]', "_", doi)[:60]
        out_path = out_dir / f"scihub_{safe}.pdf"
        out_path.write_bytes(pdf_data)
        logger.info("Sci-Hub CDP: saved to %s", out_path)

        # ── Wait 5+rand(0,2)s before closing — mimic human reading ──
        time.sleep(5 + random.random() * 2)

        return out_path

    except Exception as e:
        logger.warning("Sci-Hub CDP: failed for %s: %s", doi, e)
        return None
    finally:
        if page:
            try:
                page.close()
            except Exception:
                pass
