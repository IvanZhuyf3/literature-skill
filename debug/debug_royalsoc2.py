"""debug_royalsoc2.py — 测试 Royal Society PDF fetch"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        await page.goto("https://royalsocietypublishing.org/doi/10.1098/rsbl.2025.0405",
                        wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except:
            pass

        # Test fetch on article-pdf URL (from citation_pdf_url)
        pdf_url = "https://royalsocietypublishing.org/rsbl/article-pdf/doi/10.1098/rsbl.2025.0405/4149583/rsbl.2025.0405.pdf"
        print(f"Fetch test: {pdf_url}")
        r = await page.evaluate("""async (url) => {
            try {
                const r = await fetch(url);
                const buf = await r.arrayBuffer();
                const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                return {status:r.status, size:buf.byteLength, prefix:ps,
                        type:r.headers.get('content-type')||''};
            } catch(e) { return {error:e.message}; }
        }""", pdf_url)
        if 'error' in r:
            print(f"  ERROR: {r['error']}")
        else:
            print(f"  Status:{r['status']} Size:{r['size']} PDF:{r['prefix'].startswith('%PDF')} Type:{r['type']}")

        await page.close()

asyncio.run(main())
