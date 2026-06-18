"""debug_elsevier2.py — CDP probe for DOI 10.1016/s1386-1425(98)00157-7

Old Elsevier paper (Spectrochim Acta A, 1998). Normal retry failed with
"PDF print not detected after 120s" — the Ctrl+P pyautogui fallback ran but
produced nothing. Probe the live page structure via CDP on Edge:19222.
"""
import asyncio
from playwright.async_api import async_playwright

CDP = "http://localhost:19222"
PII = "S1386142598001577"
ARTICLE_URL = "https://www.sciencedirect.com/science/article/pii/" + PII


async def main():
    pw = await async_playwright().start()
    browser = await pw.chromium.connect_over_cdp(CDP)
    ctx = browser.contexts[0]
    page = await ctx.new_page()

    await page.goto(ARTICLE_URL, wait_until="domcontentloaded", timeout=60000)
    try:
        await page.wait_for_load_state("networkidle", timeout=30000)
    except Exception:
        pass
    await page.wait_for_timeout(3000)
    print(f"Final URL: {page.url}")

    title = await page.title()
    print(f"Page title: {title}")

    # Access / paywall check
    body_sample = await page.evaluate("() => document.body.innerText.substring(0, 400)")
    print(f"\nBody sample:\n{body_sample}")

    # 1. All PDF/download related links
    links = await page.evaluate("""() => {
        const all = document.querySelectorAll('a[href], button');
        return Array.from(all)
            .filter(a => /pdf|download|PDF|Download/i.test(
                (a.href || '') + (a.innerText || '') + (a.getAttribute('aria-label') || '')))
            .map(a => ({
                href: a.href || '',
                text: (a.innerText || '').trim().substring(0, 80),
                tag: a.tagName,
                aria: a.getAttribute('aria-label') || '',
            }));
    }""")
    print(f"\n=== PDF/download links ({len(links)}) ===")
    for i, l in enumerate(links):
        print(f"\n--- Link {i+1} ---")
        print(f"  tag:  {l['tag']}")
        print(f"  href: {l['href']}")
        print(f"  text: {l['text']}")
        print(f"  aria: {l['aria']}")

    # 2. CDN links specifically
    cdn = await page.evaluate("""() => {
        const els = document.querySelectorAll('a[href*="ars.els-cdn.com"]');
        return Array.from(els).map(a => ({
            href: a.href,
            text: (a.innerText || '').trim().substring(0, 80),
        }));
    }""")
    print(f"\n=== CDN links (ars.els-cdn.com) ({len(cdn)}) ===")
    for c in cdn:
        print(f"  {c['href']}  |  {c['text']}")

    # 3. citation meta tags
    metas = await page.evaluate("""() => {
        const tags = ['citation_title', 'citation_doi', 'citation_date', 'citation_pdf_url'];
        const result = {};
        for (const tag of tags) {
            const el = document.querySelector(`meta[name="${tag}"]`);
            result[tag] = el ? el.content : '(not found)';
        }
        return result;
    }""")
    print(f"\nMetadata: {metas}")

    # 4. Try fetch() on candidate PDF links
    pdf_candidates = []
    for l in links:
        h = l.get("href", "")
        if "/pdfft" in h or "ars.els-cdn.com" in h:
            pdf_candidates.append(h)
    # also citation_pdf_url
    if metas.get("citation_pdf_url", "(not found)") != "(not found)":
        pdf_candidates.append(metas["citation_pdf_url"])

    pdf_candidates = list(dict.fromkeys(pdf_candidates))  # dedupe
    print(f"\n=== fetch() test on {len(pdf_candidates)} candidates ===")
    for cand in pdf_candidates[:6]:
        print(f"\nTesting: {cand[:120]}")
        result = await page.evaluate("""async (url) => {
            try {
                const r = await fetch(url);
                const buf = await r.arrayBuffer();
                const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
                return { status: r.status, size: buf.byteLength, prefix,
                         contentType: r.headers.get('content-type') };
            } catch (e) {
                return { error: e.message };
            }
        }""", cand)
        is_pdf = result.get("prefix") == [37, 80, 68, 70]
        print(f"  status={result.get('status')} size={result.get('size')} "
              f"pdf={is_pdf} ct={result.get('contentType')} err={result.get('error')}")

    await page.close()
    await pw.stop()


asyncio.run(main())
