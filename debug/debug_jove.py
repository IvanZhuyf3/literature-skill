"""debug_jove.py — 用 CDP 探测 JoVE 页面结构.

Target: https://www.jove.com/t/64882/coherent-raman-microscopy-from-instrumentation-to-applications
"""
import asyncio
from playwright.async_api import async_playwright

URL = "https://www.jove.com/t/64882/coherent-raman-microscopy-from-instrumentation-to-applications"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:19222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except Exception:
            pass

        print(f"Final URL: {page.url}")
        print(f"Title: {await page.title()}")

        # 1. All PDF/download-related links
        links = await page.evaluate("""() => {
            const all = document.querySelectorAll('a[href], button');
            return Array.from(all)
                .filter(a => /pdf|download|PDF|Download/i.test(
                    (a.href || '') + (a.innerText || '') + (a.getAttribute('aria-label') || '')))
                .map(a => ({
                    href: a.href || '',
                    text: (a.innerText || '').trim().substring(0, 80),
                    tag: a.tagName,
                    class: (a.className || '').toString().substring(0, 100),
                    aria: a.getAttribute('aria-label') || '',
                }));
        }""")
        print(f"\n=== PDF/Download links: {len(links)} ===")
        for i, l in enumerate(links):
            print(f"\n--- Link {i+1} ---")
            print(f"  tag:    {l['tag']}")
            print(f"  href:   {l['href']}")
            print(f"  text:   {l['text']}")
            print(f"  class:  {l['class']}")
            print(f"  aria:   {l['aria']}")

        # 2. Citation meta tags
        metas = await page.evaluate("""() => {
            const tags = ['citation_title', 'citation_doi', 'citation_date',
                          'citation_pdf_url', 'citation_journal_title'];
            const result = {};
            for (const tag of tags) {
                const els = document.querySelectorAll(`meta[name="${tag}"]`);
                result[tag] = els.length ? Array.from(els).map(e => e.content) : '(not found)';
            }
            return result;
        }""")
        print(f"\n=== Metadata ===")
        for k, v in metas.items():
            print(f"  {k}: {v}")

        # 3. Look for any link with .pdf extension or /pdf/ path
        pdf_candidates = await page.evaluate("""() => {
            const links = document.querySelectorAll('a[href]');
            const out = [];
            for (const a of links) {
                const h = a.href || '';
                if (/\\.pdf($|\\?)|\\/pdf\\//i.test(h)) {
                    out.push({href: h, text: (a.innerText || '').trim().substring(0, 60)});
                }
            }
            return out;
        }""")
        print(f"\n=== PDF path candidates: {len(pdf_candidates)} ===")
        for c in pdf_candidates:
            print(f"  {c['href']}  |  {c['text']}")

        # 4. Test fetch on citation_pdf_url if present
        citation_pdf = metas.get('citation_pdf_url')
        test_url = None
        if isinstance(citation_pdf, list) and citation_pdf and citation_pdf[0] != '(not found)':
            test_url = citation_pdf[0]
        elif pdf_candidates:
            test_url = pdf_candidates[0]['href']

        if test_url:
            print(f"\n=== Testing fetch() on: {test_url} ===")
            try:
                result = await page.evaluate("""async (url) => {
                    try {
                        const r = await fetch(url, {credentials: 'include'});
                        const buf = await r.arrayBuffer();
                        const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
                        return { status: r.status, size: buf.byteLength, prefix,
                                 contentType: r.headers.get('content-type'),
                                 finalUrl: r.url };
                    } catch (e) {
                        return { error: String(e) };
                    }
                }""", test_url)
                print(f"  Result: {result}")
                if 'prefix' in result:
                    print(f"  Is PDF: {bytes(result['prefix']) == b'%PDF'}")
            except Exception as e:
                print(f"  fetch failed: {e}")

        await page.close()


asyncio.run(main())
