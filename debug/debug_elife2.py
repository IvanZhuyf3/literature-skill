"""debug_elife2.py — 深入探测 eLife PDF 和 metadata"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        url = "https://elifesciences.org/articles/106728"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except:
            pass

        # 1. fetch Article PDF link
        pdf_link = await page.evaluate("""() => {
            const el = document.querySelector('a.article-download-links-list__link');
            return el ? el.href : null;
        }""")
        print(f"Article PDF link: {pdf_link}")

        if pdf_link:
            r = await page.evaluate("""async (url) => {
                try {
                    const r = await fetch(url);
                    const buf = await r.arrayBuffer();
                    const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                    const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                    return {status:r.status, size:buf.byteLength, prefix:ps,
                            type:r.headers.get('content-type')||''};
                } catch(e) { return {error:e.message}; }
            }""", pdf_link)
            print(f"  Fetch: {r}")

        # 2. Try direct CDN PDF URL (decoded from base64 in download link)
        article_id = "106728"
        cdn_url = f"https://cdn.elifesciences.org/articles/{article_id}/elife-{article_id}-v1.pdf"
        print(f"\nDirect CDN URL: {cdn_url}")
        r = await page.evaluate("""async (url) => {
            try {
                const r = await fetch(url);
                const buf = await r.arrayBuffer();
                const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                return {status:r.status, size:buf.byteLength, prefix:ps,
                        type:r.headers.get('content-type')||''};
            } catch(e) { return {error:e.message}; }
        }""", cdn_url)
        print(f"  Fetch: {r}")

        # 3. Check all meta tags
        all_metas = await page.evaluate("""() => {
            return Array.from(document.querySelectorAll('meta'))
                .filter(m => m.name || m.getAttribute('property'))
                .map(m => ({
                    name: m.name || m.getAttribute('property'),
                    content: (m.content || '').substring(0, 100),
                }))
                .filter(m => /title|doi|date|author|citation|dc\.|og:/i.test(m.name));
        }""")
        print(f"\nRelevant meta tags ({len(all_metas)}):")
        for m in all_metas:
            print(f"  {m['name']}: {m['content']}")

        # 4. Check DOI from URL or page content
        doi = await page.evaluate("""() => {
            // Check for DOI in page text
            const body = document.body.innerText;
            const m = body.match(/https?:\/\/doi\.org\/(10\.\d+\/[^\s]+)/);
            return m ? m[1] : '(not found)';
        }""")
        print(f"\nDOI from page text: {doi}")

        await page.close()

asyncio.run(main())
