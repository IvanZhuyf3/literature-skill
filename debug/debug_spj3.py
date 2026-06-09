"""debug_spj3.py — 测试 SPJ PDF fetch"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        
        await page.goto("https://spj.science.org/doi/10.34133/research.1263",
                        wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(5000)
        
        print(f"Page: {page.url}")
        
        # Test both PDF URLs
        for pdf_url in [
            "/doi/pdf/10.34133/research.1263?download=true",
            "/doi/pdf/10.34133/research.1263",
        ]:
            print(f"\nTesting: {pdf_url}")
            r = await page.evaluate("""async (url) => {
                try {
                    const r = await fetch(url);
                    const buf = await r.arrayBuffer();
                    const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                    const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                    return {status:r.status, size:buf.byteLength, prefix:ps, type:r.headers.get('content-type')||''};
                } catch(e) { return {error:e.message}; }
            }""", pdf_url)
            if 'error' in r:
                print(f"  ERROR: {r['error']}")
            else:
                print(f"  Status:{r['status']} Size:{r['size']} PDF:{r['prefix'].startswith('%PDF')} Type:{r['type']}")
        
        # Try navigating directly to the PDF
        print("\nNavigating to /doi/pdf/...")
        try:
            resp = await page.goto("https://spj.science.org/doi/pdf/10.34133/research.1263", timeout=30000)
            print(f"  Status: {resp.status if resp else 'None'}")
            print(f"  URL: {page.url}")
            print(f"  Type: {resp.headers.get('content-type','') if resp else 'N/A'}")
        except Exception as e:
            print(f"  Error: {e}")
        
        await page.close()

asyncio.run(main())
