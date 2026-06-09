"""debug_spj2.py — 直接探测 SPJ epdf 页面"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        
        # 试两个 URL
        for url in [
            "https://spj.science.org/doi/10.34133/research.1248",
            "https://spj.science.org/doi/epdf/10.34133/research.1248",
        ]:
            print(f"\n{'='*60}")
            print(f"URL: {url}")
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                print(f"Loaded: {page.url}")
            except Exception as e:
                print(f"goto failed: {e}")
                continue
            
            await page.wait_for_timeout(3000)
            print(f"Final URL: {page.url}")
            
            links = await page.evaluate("""() => {
                const all = document.querySelectorAll('a[href]');
                return Array.from(all)
                    .filter(a => /pdf|download|PDF|Download/i.test((a.href||'')+(a.innerText||'')))
                    .map(a => ({href: (a.href||'').substring(0,120), text: (a.innerText||'').trim().substring(0,40)}));
            }""")
            print(f"PDF links ({len(links)}):")
            for l in links:
                print(f"  {l['href']}  [{l['text']}]")
            
            metas = await page.evaluate("""() => {
                const r = {};
                for (const t of ['citation_title','citation_doi','citation_pdf_url']) {
                    const el = document.querySelector('meta[name="'+t+'"]');
                    r[t] = el ? el.content.substring(0,80) : '(not found)';
                }
                return r;
            }""")
            print(f"Metas: {metas}")
        
        await page.close()

asyncio.run(main())
