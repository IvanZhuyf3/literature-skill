"""CDP probe: World Scientific — try alternatives & check cookies."""
import json, sys, asyncio
sys.path.insert(0, r"C:\Users\Ivanz\OneDrive\Hermes_workspace\Literature_skill")
from playwright.async_api import async_playwright

CDP_URL = "http://127.0.0.1:19222"

async def probe():
    async with async_playwright() as pw:
        browser = await pw.chromium.connect_over_cdp(CDP_URL)
        ctx = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await ctx.new_page()

        doi_url = "https://www.worldscientific.com/doi/abs/10.1142/9789812778307_0030"
        await page.goto(doi_url, wait_until="domcontentloaded", timeout=45000)
        for i in range(15):
            await asyncio.sleep(2)
            title = await page.title()
            if "Just a moment" not in title:
                print(f"Cloudflare cleared after ~{(i+1)*2}s")
                break

        # Check cookies
        cookies = await page.context.cookies()
        wspc_cookies = [c for c in cookies if "worldscientific" in c.get("domain", "")]
        print(f"\nWorldScientific cookies: {len(wspc_cookies)}")
        for c in wspc_cookies:
            print(f"  {c['name']} = {c['value'][:50]}...")

        # Try fetch() with referer
        print("\n=== fetch() PDF with Referer header ===")
        pdf_url = "https://www.worldscientific.com/doi/pdf/10.1142/9789812778307_0030?download=true"
        result = await page.evaluate("""async (url) => {
            const r = await fetch(url, {
                method: 'GET',
                credentials: 'include',
                headers: {'Referer': document.location.href}
            });
            const blob = await r.blob();
            const type = r.headers.get('content-type') || '';
            return {status: r.status, type: type, size: blob.size, url: r.url, is_pdf: type.includes('pdf')};
        }""", pdf_url)
        print(f"  {json.dumps(result)}")

        # Try the reader page - maybe it has an embedded PDF
        reader_url = "https://www.worldscientific.com/doi/reader/10.1142/9789812778307_0030"
        print(f"\n=== Navigate to reader page ===")
        await page.goto(reader_url, wait_until="domcontentloaded", timeout=30000)
        try:
            await page.wait_for_load_state("networkidle", timeout=8000)
        except:
            pass
        print(f"Final URL: {page.url}")
        title = await page.title()
        print(f"Title: {title}")

        # Check for PDF viewer elements
        print("\n=== PDF viewer elements ===")
        embed = await page.evaluate("""() => {
            const embeds = document.querySelectorAll('embed[type="application/pdf"], iframe[src*="pdf"], object[type="application/pdf"]');
            return Array.from(embeds).map(e => ({tag: e.tagName, src: e.src || e.getAttribute('src') || e.getAttribute('data') || ''}));
        }""")
        print(f"  Embed/Iframe: {embed}")

        # Check for any PDF-like URL patterns in the page source
        print("\n=== Any URL containing 'pdf' in all resources ===")
        pdf_resources = await page.evaluate("""() => {
            const results = [];
            const all = document.querySelectorAll('*');
            for (const el of all) {
                if (el.tagName === 'SCRIPT' || el.tagName === 'LINK') continue;
                for (const attr of ['src', 'href', 'data', 'action']) {
                    const val = el.getAttribute(attr);
                    if (val && val.toLowerCase().includes('pdf')) {
                        results.push({tag: el.tagName, attr: attr, val: val.slice(0,120)});
                    }
                }
            }
            return results.slice(0, 15);
        }""")
        for r in pdf_resources:
            print(f"  <{r['tag']}> [{r['attr']}] {r['val']}")

        body = (await page.inner_text("body"))[:800]
        print(f"\nBody: {body}")

        await page.close()
        await browser.close()

asyncio.run(probe())
