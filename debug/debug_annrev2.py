"""debug_annrev2.py — 深入探测 Annual Reviews PDF 获取方式"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        url = "https://www.annualreviews.org/content/journals/10.1146/annurev-physchem-082624-013453"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except:
            pass

        # 1. Try constructing PDF URL patterns
        doi = "10.1146/annurev-physchem-082624-013453"
        test_urls = [
            f"https://www.annualreviews.org/doi/pdf/{doi}",
            f"https://www.annualreviews.org/content/journals/{doi}?crawler=true&mimetype=application/pdf",
            f"https://www.annualreviews.org/doi/pdfdirect/{doi}?download=true",
        ]

        for test_url in test_urls:
            print(f"\nFetch test: {test_url}")
            r = await page.evaluate("""async (url) => {
                try {
                    const r = await fetch(url);
                    const buf = await r.arrayBuffer();
                    const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                    const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                    return {status:r.status, size:buf.byteLength, prefix:ps,
                            type:r.headers.get('content-type')||''};
                } catch(e) { return {error:e.message}; }
            }""", test_url)
            if 'error' in r:
                print(f"  ERROR: {r['error']}")
            else:
                print(f"  Status:{r['status']} Size:{r['size']} PDF:{r['prefix'].startswith('%PDF')} Type:{r['type']}")

        # 2. Check the PDF button's onclick/data attributes
        btn_info = await page.evaluate("""() => {
            const btn = document.querySelector('a[aria-label="Download PDF"]');
            if (!btn) return null;
            return {
                href: btn.href,
                onclick: btn.getAttribute('onclick'),
                dataAttrs: Array.from(btn.attributes)
                    .filter(a => a.name.startsWith('data-'))
                    .map(a => ({name: a.name, value: a.value})),
                outerHTML: btn.outerHTML.substring(0, 300),
                parentTag: btn.parentElement?.tagName,
                parentClass: (btn.parentElement?.className || '').substring(0, 100),
            };
        }""")
        print(f"\nPDF button details: {btn_info}")

        # 3. Check all links with /doi/ in href (not just pdf)
        doi_links = await page.evaluate("""() => {
            return Array.from(document.querySelectorAll('a[href*="/doi/"]'))
                .map(a => ({href: (a.href||'').substring(0,120),
                            text: (a.innerText||'').trim().substring(0,40),
                            class: (a.className||'').substring(0,60)}));
        }""")
        print(f"\nAll /doi/ links ({len(doi_links)}):")
        for l in doi_links:
            print(f"  {l['href']}  [{l['text']}]  class={l['class']}")

        # 4. Try navigate to /doi/pdf/ DOI and see what happens
        print("\n--- Navigating to /doi/pdf/ ---")
        page2 = await ctx.new_page()
        try:
            resp = await page2.goto(f"https://www.annualreviews.org/doi/pdf/{doi}",
                                     wait_until="domcontentloaded", timeout=30000)
            print(f"  Status: {resp.status if resp else 'None'}")
            print(f"  URL: {page2.url}")
            if resp:
                print(f"  Content-Type: {resp.headers.get('content-type','')}")
            # Try fetch from this page
            r = await page2.evaluate("""async () => {
                try {
                    const r = await fetch(window.location.href);
                    const buf = await r.arrayBuffer();
                    const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                    const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                    return {status:r.status, size:buf.byteLength, prefix:ps,
                            type:r.headers.get('content-type')||''};
                } catch(e) { return {error:e.message}; }
            }""")
            print(f"  Fetch self: {r}")
        except Exception as e:
            print(f"  Error: {e}")
        await page2.close()

        await page.close()

asyncio.run(main())
