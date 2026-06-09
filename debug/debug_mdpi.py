"""debug_mdpi.py — 用 CDP 探测 MDPI 页面结构"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        url = "https://www.mdpi.com/1424-8220/26/10/2941"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except:
            pass

        print(f"Final URL: {page.url}")

        # 1. All PDF/download related elements
        links = await page.evaluate("""() => {
            const all = document.querySelectorAll('a[href], button');
            return Array.from(all)
                .filter(a => /pdf|download|PDF|Download/i.test(
                    (a.href || '') + (a.innerText || '')))
                .map(a => ({
                    href: a.href || '',
                    text: (a.innerText || '').trim().substring(0, 60),
                    tag: a.tagName,
                    class: (a.className || '').substring(0, 80),
                    aria: a.getAttribute('aria-label') || '',
                }));
        }""")
        print(f"\nPDF/download elements ({len(links)}):")
        for i, l in enumerate(links):
            print(f"\n--- {i+1} ---")
            print(f"  tag:   {l['tag']}")
            print(f"  href:  {l['href']}")
            print(f"  text:  {l['text']}")
            print(f"  class: {l['class']}")
            print(f"  aria:  {l['aria']}")

        # 2. Metadata
        metas = await page.evaluate("""() => {
            const tags = ['citation_title','citation_doi','citation_date',
                          'citation_author','citation_pdf_url'];
            const r = {};
            for (const t of tags) {
                const els = document.querySelectorAll('meta[name="'+t+'"]');
                r[t] = els.length > 1
                    ? Array.from(els).slice(0,2).map(e=>e.content).concat(['...'])
                    : (els[0] ? els[0].content : '(not found)');
            }
            r['title_tag'] = document.title;
            return r;
        }""")
        print(f"\nMetadata:")
        for k, v in metas.items():
            print(f"  {k}: {v}")

        # 3. Try constructing PDF URL from DOI
        doi = metas.get('citation_doi', '')
        if doi:
            pdf_urls = [
                f"https://www.mdpi.com/1424-8220/26/10/2941/pdf",
                f"https://www.mdpi.com/1424-8220/26/10/2941/pdf?version=1",
            ]
            for pu in pdf_urls:
                print(f"\nFetch test: {pu}")
                r = await page.evaluate("""async (url) => {
                    try {
                        const r = await fetch(url);
                        const buf = await r.arrayBuffer();
                        const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                        const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                        return {status:r.status, size:buf.byteLength, prefix:ps,
                                type:r.headers.get('content-type')||''};
                    } catch(e) { return {error:e.message}; }
                }""", pu)
                if 'error' in r:
                    print(f"  ERROR: {r['error']}")
                else:
                    print(f"  Status:{r['status']} Size:{r['size']} PDF:{r['prefix'].startswith('%PDF')} Type:{r['type']}")

        # 4. fetch test on any PDF links found
        pdf_links = [l for l in links if l['href'] and '/pdf' in l['href'].lower()]
        for l in pdf_links[:3]:
            print(f"\nFetch test on found link: {l['href'][:120]}")
            r = await page.evaluate("""async (url) => {
                try {
                    const r = await fetch(url);
                    const buf = await r.arrayBuffer();
                    const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                    const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                    return {status:r.status, size:buf.byteLength, prefix:ps,
                            type:r.headers.get('content-type')||''};
                } catch(e) { return {error:e.message}; }
            }""", l['href'])
            if 'error' in r:
                print(f"  ERROR: {r['error']}")
            else:
                print(f"  Status:{r['status']} Size:{r['size']} PDF:{r['prefix'].startswith('%PDF')} Type:{r['type']}")

        await page.close()

asyncio.run(main())
