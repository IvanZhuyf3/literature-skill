"""debug_jove6.py — Verify api.jove.com/api/article/pdf/<id> returns a real PDF via fetch."""
import asyncio
from playwright.async_api import async_playwright

ARTICLE = "https://www.jove.com/t/64882/coherent-raman-microscopy-from-instrumentation-to-applications"
API = "https://api.jove.com/api/article/pdf/64882"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:19222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        # First load the article page so we have session/cookies context
        await page.goto(ARTICLE, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=20000)
        except Exception:
            pass

        # Fetch the API PDF from the www.jove.com page context (credentials included)
        result = await page.evaluate("""async (url) => {
            try {
                const r = await fetch(url, {credentials: 'include'});
                const buf = await r.arrayBuffer();
                const prefix = Array.from(new Uint8Array(buf.slice(0, 8)));
                const tail = Array.from(new Uint8Array(buf.slice(buf.byteLength-8)));
                return { status: r.status, size: buf.byteLength, prefix, tail,
                         contentType: r.headers.get('content-type'),
                         disposition: r.headers.get('content-disposition') };
            } catch (e) { return { error: String(e) }; }
        }""", API)
        print(f"Result: {result}")
        if 'prefix' in result:
            print(f"PDF header: {bytes(result['prefix'])}")
            print(f"Is %PDF: {bytes(result['prefix']).startswith(b'%PDF')}")
            print(f"Has %%EOF tail: {b'%%EOF' in bytes(result['tail'])}")

        await page.close()


asyncio.run(main())
