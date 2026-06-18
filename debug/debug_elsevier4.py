"""debug_elsevier4.py — SYNC replication of adapter resolve flow.

Replicate EXACTLY what the engine does (sync playwright), to see why
page.goto(pdfft) in the adapter doesn't redirect to the S3 URL the way
the async probe did. Connects to Edge:19222.
"""
import sys, time
sys.path.insert(0, ".")
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import re

CDP = "http://127.0.0.1:19222"
PII = "S1386142598001577"
ARTICLE_URL = "https://www.sciencedirect.com/science/article/pii/" + PII


def main():
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp(CDP)
    ctx = browser.contexts[0]

    # Use an existing/new page like the engine does
    page = ctx.new_page()

    # 1. Navigate to article (same as adapter.navigate_to_paper)
    print("[1] Navigating to article page...")
    page.goto(ARTICLE_URL, wait_until="domcontentloaded", timeout=60000)
    try:
        page.wait_for_selector('a[aria-label*="PDF"]', timeout=15000)
    except Exception as e:
        print("    View PDF selector wait failed:", e)
    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception:
        pass
    print("    Article URL:", page.url)

    # 2. Extract pdfft URL exactly like adapter.find_download_url
    pii_match = re.search(r"/pii/([^/?#]+)", page.url)
    current_pii = pii_match.group(1) if pii_match else ""
    pdfft_url = None
    elements = page.query_selector_all('a[aria-label*="PDF"]')
    for el in elements:
        href = el.get_attribute("href") or ""
        if current_pii and current_pii in href and "/pdfft" in href:
            pdfft_url = urljoin(page.url, href)
            break
    print("[2] Extracted pdfft URL:", (pdfft_url or "NONE")[:140])
    if not pdfft_url:
        print("    FAILED to extract pdfft URL")
        page.close(); pw.stop(); return

    # 3. Replicate _resolve_pdfft_redirect on the SAME page
    print("[3] Navigating SAME page to pdfft (wait_until=domcontentloaded)...")
    t0 = time.time()
    try:
        page.goto(pdfft_url, wait_until="domcontentloaded", timeout=60000)
        print(f"    goto returned in {time.time()-t0:.1f}s")
    except Exception as e:
        print(f"    goto THREW after {time.time()-t0:.1f}s: {e}")
    time.sleep(4)
    final = page.url
    print("    page.url after navigation:", final[:160])

    # 4. Check content type / viewer
    try:
        ct = page.evaluate("() => document.contentType")
        print("    document.contentType:", ct)
    except Exception as e:
        print("    evaluate contentType failed:", e)

    # 5. Try fetch(window.location.href) from this page
    print("[5] fetch(window.location.href) from current page:")
    try:
        result = page.evaluate("""async () => {
            try {
                const r = await fetch(window.location.href);
                const buf = await r.arrayBuffer();
                const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
                return { status: r.status, size: buf.byteLength, prefix,
                         ct: r.headers.get('content-type') };
            } catch (e) { return { error: e.message }; }
        }""")
        is_pdf = result.get("prefix") == [37, 80, 68, 70]
        print(f"    status={result.get('status')} size={result.get('size')} "
              f"pdf={is_pdf} ct={result.get('ct')} err={result.get('error')}")
    except Exception as e:
        print("    fetch evaluate failed:", e)

    # 6. ALTERNATIVE: try wait_until="commit" or "load" for the pdfft nav
    print("[6] Retry nav with wait_until='load' on a FRESH page...")
    page2 = ctx.new_page()
    t0 = time.time()
    try:
        page2.goto(pdfft_url, wait_until="load", timeout=60000)
        print(f"    goto(load) returned in {time.time()-t0:.1f}s, url={page2.url[:120]}")
    except Exception as e:
        print(f"    goto(load) threw after {time.time()-t0:.1f}s: {e}")
    time.sleep(3)
    print("    page2.url:", page2.url[:160])
    try:
        result2 = page2.evaluate("""async () => {
            try {
                const r = await fetch(window.location.href);
                const buf = await r.arrayBuffer();
                return { status: r.status, size: buf.byteLength,
                         prefix: Array.from(new Uint8Array(buf.slice(0,4))),
                         ct: r.headers.get('content-type') };
            } catch (e) { return { error: e.message }; }
        }""")
        is_pdf2 = result2.get("prefix") == [37, 80, 68, 70]
        print(f"    fetch from page2: status={result2.get('status')} "
              f"size={result2.get('size')} pdf={is_pdf2} ct={result2.get('ct')} "
              f"err={result2.get('error')}")
    except Exception as e:
        print("    page2 fetch failed:", e)

    page.close()
    page2.close()
    pw.stop()


main()
