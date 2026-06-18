"""CDP probe: APS/PRL page for 10.1103/physrevlett.87.023901."""
import json, sys, asyncio
sys.path.insert(0, r"C:\Users\Ivanz\OneDrive\Hermes_workspace\Literature_skill")
from playwright.async_api import async_playwright

CDP_URL = "http://127.0.0.1:19222"

async def probe():
    async with async_playwright() as pw:
        browser = await pw.chromium.connect_over_cdp(CDP_URL)
        ctx = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await ctx.new_page()
        
        doi_url = "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.87.023901"
        print("=== NAVIGATING ===")
        await page.goto(doi_url, wait_until="domcontentloaded", timeout=30000)
        try:
            await page.wait_for_load_state("networkidle", timeout=10000)
        except:
            pass
        print("Final URL:", page.url)
        print("Title:", await page.title())
        
        # Check all PDF-related links
        print("\n=== ALL LINKS WITH 'pdf' ===")
        links = await page.evaluate("""() => {
            const all = document.querySelectorAll('a');
            const results = [];
            for (const a of all) {
                const href = a.href || '';
                if (href.toLowerCase().includes('pdf') || a.textContent.toLowerCase().includes('pdf')) {
                    results.push({text: a.textContent.trim().slice(0,80), href: href, classes: a.className});
                }
            }
            return results;
        }""")
        for l in links:
            print(f"  [{l['classes']}] \"{l['text']}\" -> {l['href']}")
        
        # Check sm-primary-button
        print("\n=== sm-primary-button elements ===")
        btns = await page.evaluate("""() => {
            const els = document.querySelectorAll('.sm-primary-button');
            return Array.from(els).map(e => ({
                tag: e.tagName,
                text: e.textContent.trim().slice(0,80),
                href: e.href || e.getAttribute('href') || ''
            }));
        }""")
        for b in btns:
            print(f"  <{b['tag']}> \"{b['text']}\" -> {b['href']}")
        
        # Check access indicators
        print("\n=== BODY TEXT (first 3000 chars) ===")
        body = (await page.inner_text("body"))[:3000]
        print(body)
        
        await page.close()
        await browser.close()

asyncio.run(probe())
