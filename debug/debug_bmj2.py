"""debug_bmj2.py — 测试 BMJ PDF fetch"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        await page.goto("https://bmjimmunology.bmj.com/content/1/1/e000001",
                        wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except:
            pass
        pdf_url = "https://bmjimmunology.bmj.com/content/bmjimm/1/1/e000001.full.pdf"
        print(f"Fetch: {pdf_url}")
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
        print(f"  Result: {r}")
        await page.close()

asyncio.run(main())
