"""Debug Elsevier: check where pdfft redirects."""
import asyncio
from playwright.async_api import async_playwright

async def main():
    pw = await async_playwright().start()
    browser = await pw.chromium.connect_over_cdp("http://localhost:9222")
    ctx = browser.contexts[0]

    # Article page
    page = await ctx.new_page()
    await page.goto("https://www.sciencedirect.com/science/article/pii/S0092867426003958",
                     timeout=60000, wait_until="domcontentloaded")
    await page.wait_for_timeout(3000)
    print(f"Article: {page.url}")

    # Navigate to pdfft URL
    pdfft_url = "/science/article/pii/S0092867426003958/pdfft?md5=12efe2adc5ca68919d9ed238f95a082e&pid=1-s2.0-S0092867426003958-main.pdf"
    pdf_page = await ctx.new_page()
    resp = await pdf_page.goto("https://www.sciencedirect.com" + pdfft_url, timeout=30000)
    await pdf_page.wait_for_timeout(3000)
    print(f"pdfft page URL: {pdf_page.url}")
    print(f"pdfft status: {resp.status if resp else None}")
    if resp:
        print(f"content-type: {resp.headers.get('content-type')}")

    # Try fetching from this page
    result = await pdf_page.evaluate("""async () => {
        try {
            const response = await fetch(window.location.href);
            const ct = response.headers.get('content-type');
            const buf = await response.arrayBuffer();
            const first4 = Array.from(new Uint8Array(buf.slice(0, 4)));
            return { ok: response.ok, ct: ct, size: buf.byteLength, first4: first4 };
        } catch (e) {
            return { error: e.message };
        }
    }""")
    print(f"Fetch from pdfft page: {result}")

    await pdf_page.close()
    await page.close()
    await pw.stop()

asyncio.run(main())
