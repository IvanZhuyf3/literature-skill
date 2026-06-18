"""debug_elsevier3.py — test constructed CDN PDF URL + pdfft navigation.

Key question: can fetch() get the real PDF if we build the CDN URL from the
pid token in the pdfft link?  pid=1-s2.0-S1386142598001577-main.pdf
=> CDN candidate: https://ars.els-cdn.com/content/image/1-s2.0-...-main.pdf
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

    # ---- Test from article-page context (has institutional cookies) ----
    page = await ctx.new_page()
    await page.goto(ARTICLE_URL, wait_until="domcontentloaded", timeout=60000)
    await page.wait_for_timeout(3000)

    # Build candidate CDN direct URLs from the pid token
    pid = "1-s2.0-S1386142598001577-main.pdf"
    candidates = [
        f"https://ars.els-cdn.com/content/image/{pid}",
        # alternate CDN host sometimes used
        f"https://pdf.sciencedirectassets.com/{pid}",
        # the /pdf variant of the article
        f"https://www.sciencedirect.com/science/article/pii/{PII}/pdf?md5=&pid={pid}",
    ]

    print("=== fetch() from ARTICLE page context ===")
    for cand in candidates:
        print(f"\nTesting: {cand}")
        result = await page.evaluate("""async (url) => {
            try {
                const r = await fetch(url, {credentials: 'include'});
                const buf = await r.arrayBuffer();
                const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
                return { status: r.status, size: buf.byteLength, prefix,
                         contentType: r.headers.get('content-type'),
                         redirected: r.redirected };
            } catch (e) { return { error: e.message }; }
        }""", cand)
        is_pdf = result.get("prefix") == [37, 80, 68, 70]
        print(f"  status={result.get('status')} size={result.get('size')} "
              f"pdf={is_pdf} ct={result.get('contentType')} "
              f"redirected={result.get('redirected')} err={result.get('error')}")

    # ---- Test actual NAVIGATION to pdfft (what browser renderer does) ----
    pdfft = (f"https://www.sciencedirect.com/science/article/pii/{PII}/pdfft"
             "?md5=c2f3fd49e98a8e698bb4817a28e5d177&pid=1-s2.0-S1386142598001577-main.pdf")
    nav_page = await ctx.new_page()
    resp = await nav_page.goto(pdfft, wait_until="domcontentloaded", timeout=60000)
    await nav_page.wait_for_timeout(4000)
    print(f"\n=== NAVIGATION to pdfft ===")
    print(f"  final URL: {nav_page.url}")
    print(f"  status: {resp.status if resp else None}")
    if resp:
        print(f"  content-type: {resp.headers.get('content-type')}")
    # Is it a chrome PDF viewer? (embed[type="application/pdf"])
    viewer = await nav_page.evaluate("""() => {
        const embed = document.querySelector('embed[type="application/pdf"]');
        const obj = document.querySelector('object[type="application/pdf"]');
        const iframe = document.querySelector('iframe');
        return {
            hasEmbed: !!embed, embedSrc: embed ? embed.src : null,
            hasObject: !!obj, objData: obj ? obj.data : null,
            hasIframe: !!iframe, iframeSrc: iframe ? iframe.src : null,
            contentType: document.contentType,
            bodyLen: document.body ? document.body.innerHTML.length : 0,
        };
    }""")
    print(f"  viewer probe: {viewer}")

    # Try fetch() from the pdfft page context itself (same-origin redirect may give PDF)
    result2 = await nav_page.evaluate("""async () => {
        try {
            const r = await fetch(window.location.href, {credentials: 'include'});
            const buf = await r.arrayBuffer();
            const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
            return { status: r.status, size: buf.byteLength, prefix,
                     ct: r.headers.get('content-type') };
        } catch (e) { return { error: e.message }; }
    }""")
    is_pdf2 = result2.get("prefix") == [37, 80, 68, 70]
    print(f"  refetch from pdfft page: status={result2.get('status')} "
          f"size={result2.get('size')} pdf={is_pdf2} ct={result2.get('ct')}")

    await nav_page.close()
    await page.close()
    await pw.stop()


asyncio.run(main())
