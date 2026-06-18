"""
lit/download/scihub_cdp.py — Sci-Hub PDF download via CDP (Edge browser).

用已有的 Edge CDP 连接打开 Sci-Hub 页面，让浏览器自然过 DDoS-Guard，
然后从页面 HTML 提取 PDF URL，通过浏览器 fetch API 下载（带 DDoS-Guard cookie）。

不新开浏览器，不影响用户正常使用。

Usage:
    from lit.download.scihub_cdp import try_scihub
    pdf_path = try_scihub("10.1234/example", year=2021)
    # -> Path to downloaded PDF, or None
"""
from __future__ import annotations

import logging
import os
import re
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

from lit.core.config import load as get_config

logger = logging.getLogger(__name__)

_SCI_HUB_BASE = "https://sci-hub.ru"
_MAX_YEAR = 2021


def try_scihub(
    doi: str,
    year: str | int | None = None,
) -> Path | None:
    """
    Open Sci-Hub in CDP browser, sniff for PDF URL, download it.

    The browser (Edge) handles DDoS-Guard JS challenges naturally.
    Once we have the direct storage URL, we fetch via plain HTTP.

    Args:
        doi:  The DOI string (e.g. "10.1038/s41586-021-03819-2").
        year: Publication year. If > max_year, skips silently.

    Returns:
        ``Path`` to the downloaded PDF, or ``None``.
    """
    cfg = get_config()
    scihub_cfg = cfg.get("scihub", {})
    base_url = scihub_cfg.get("base_url", _SCI_HUB_BASE)
    max_year = scihub_cfg.get("max_year", _MAX_YEAR)
    cdp_url = cfg.get("chrome", {}).get(
        "cdp_url", "http://localhost:19222"
    )
    download_dir = scihub_cfg.get(
        "download_dir",
        cfg.get("download", {}).get("temp_dir", ""),
    )

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

    url = f"{base_url.rstrip('/')}/{doi.lstrip('/')}"
    logger.info("Sci-Hub CDP: navigating to %s", url)

    pw = None
    browser = None
    page = None

    try:
        pw = sync_playwright().start()
        browser = pw.chromium.connect_over_cdp(cdp_url)
        ctx = browser.contexts[0] if browser.contexts else browser.new_context()
        page = ctx.new_page()

        # Navigate — browser handles DDoS-Guard automatically
        # DDoS-Guard returns 403 initially, then resolves via JS challenge
        page.goto(url, wait_until="domcontentloaded", timeout=30_000)

        # Wait up to 40s for DDoS-Guard to resolve and real content to load
        # Detection: page title changes from "DDoS-Guard" to the paper title
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

        # Let the page stabilize after navigation completes
        try:
            page.wait_for_load_state("networkidle", timeout=15_000)
        except Exception:
            pass
        time.sleep(1)

        # Extra guard: if page is still navigating, wait a bit more
        for _ in range(5):
            try:
                html = page.content()
                break
            except Exception:
                time.sleep(2)

        # Check for "not available"
        body_lower = html[:3000].lower()
        for pat in ("not available", "not found", "doesn't exist",
                    "no paper", "sci-hub doesn't have this paper",
                    "could not retrieve"):
            if pat in body_lower:
                logger.info("Sci-Hub CDP: paper not available for %s", doi)
                return None

        # Extract PDF URL from page
        pdf_url = None
        for pat in (
            r'citation_pdf_url.*?content=["\']([^"\']+)',
            r'<object[^>]*data=["\']([^"\']+\.pdf)["\']',
            r'<embed[^>]*src=["\']([^"\']+\.pdf)["\']',
            r'class=["\']download["\'][^>]*>.*?<a[^>]*href=["\']([^"\']+\.pdf)',
        ):
            m = re.search(pat, html, re.IGNORECASE | re.DOTALL)
            if m:
                pdf_url = m.group(1)
                break

        if not pdf_url:
            logger.info("Sci-Hub CDP: no PDF URL found in page for %s", doi)
            return None

        # Make absolute
        if pdf_url.startswith("//"):
            pdf_url = "https:" + pdf_url
        elif pdf_url.startswith("/"):
            pdf_url = base_url.rstrip("/") + pdf_url

        logger.info("Sci-Hub CDP: PDF URL found: %s", pdf_url[:100])

        # Download PDF through the browser (has DDoS-Guard cookies)
        # Use page.evaluate() to fetch via native browser fetch API
        pdf_bytes = page.evaluate("""
            async (url) => {
                const resp = await fetch(url);
                if (!resp.ok) throw new Error('HTTP ' + resp.status);
                const blob = await resp.blob();
                const buf = await blob.arrayBuffer();
                return Array.from(new Uint8Array(buf));
            }
        """, pdf_url)

        if not pdf_bytes or len(pdf_bytes) < 100:
            logger.warning("Sci-Hub CDP: empty or tiny response for %s", doi)
            return None

        pdf_data = bytes(pdf_bytes)
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
        if pw:
            try:
                pw.stop()
            except Exception:
                pass
