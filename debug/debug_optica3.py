"""debug_optica3.py — 测试构造的直链"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        # 先到文章页拿 session
        await page.goto("https://opg.optica.org/ol/fulltext.cfm?uri=ol-51-10-2784",
                        wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except:
            pass

        # 测试构造的直链
        pdf_key = "6e2e9fca-a755-4dca-93695ceb2187c000_591313"
        doi_part = "ol-51-10-2784"
        article_id = "591313"
        direct_url = f"https://opg.optica.org/directpdfaccess/{pdf_key}/{doi_part}.pdf?da=1&id={article_id}&seq=0&mobile=no"

        print(f"Testing: {direct_url}")
        r = await page.evaluate("""async (url) => {
            try {
                const r = await fetch(url);
                const buf = await r.arrayBuffer();
                const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                return {status:r.status, size:buf.byteLength, prefix:ps,
                        type:r.headers.get('content-type')||''};
            } catch(e) { return {error:e.message}; }
        }""", direct_url)
        if 'error' in r:
            print(f"  ERROR: {r['error']}")
        else:
            print(f"  Status:{r['status']} Size:{r['size']} PDF:{r['prefix'].startswith('%PDF')} Type:{r['type']}")

        await page.close()

asyncio.run(main())
