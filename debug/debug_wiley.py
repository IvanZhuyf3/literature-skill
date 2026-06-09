"""Debug: check metadata on Wiley epdf page."""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        
        await page.goto("https://onlinelibrary.wiley.com/doi/epdf/10.1002/anie.1518521",
                        wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except:
            pass
        
        # Check meta tags
        metas = await page.evaluate("""() => {
            const tags = ['citation_title', 'citation_doi', 'citation_date', 'citation_author'];
            const result = {};
            for (const tag of tags) {
                const el = document.querySelector(`meta[name="${tag}"]`);
                result[tag] = el ? el.content : '(not found)';
            }
            // Also check dc.title
            const dc = document.querySelector('meta[name="dc.title"]');
            result['dc.title'] = dc ? dc.content : '(not found)';
            // og:title
            const og = document.querySelector('meta[property="og:title"]');
            result['og:title'] = og ? og.content : '(not found)';
            // page title
            result['title_tag'] = document.title;
            return result;
        }""")
        for k, v in metas.items():
            print(f"{k}: {v}")
        
        await page.close()

asyncio.run(main())
