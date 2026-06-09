"""debug_aps.py — 用 CDP 探测 APS 页面结构"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        
        url = "https://journals.aps.org/prl/abstract/10.1103/p2bv-hv5s"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except:
            pass
        
        print(f"Final URL: {page.url}")
        
        # 1. 检查所有 PDF/download 相关链接
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
        print(f"\nFound {len(links)} PDF/download-related elements:")
        for i, l in enumerate(links):
            print(f"\n--- Element {i+1} ---")
            print(f"  tag:    {l['tag']}")
            print(f"  href:   {l['href']}")
            print(f"  text:   {l['text']}")
            print(f"  class:  {l['class']}")
            print(f"  aria:   {l['aria']}")
        
        # 2. 检查 citation meta 标签
        metas = await page.evaluate("""() => {
            const tags = ['citation_title', 'citation_doi', 'citation_date', 'citation_author'];
            const result = {};
            for (const tag of tags) {
                const els = document.querySelectorAll(`meta[name="${tag}"]`);
                if (els.length > 1) {
                    result[tag] = Array.from(els).map(e => e.content);
                } else {
                    const el = els[0];
                    result[tag] = el ? el.content : '(not found)';
                }
            }
            result['title_tag'] = document.title;
            return result;
        }""")
        print(f"\nMetadata:")
        for k, v in metas.items():
            if isinstance(v, list):
                print(f"  {k}: {v[0]}... ({len(v)} items)")
            else:
                print(f"  {k}: {v}")
        
        # 3. 逐个 fetch() 测试候选 PDF 链接
        pdf_links = [l for l in links if l['href'] and '/pdf' in l['href'].lower()]
        if not pdf_links:
            pdf_links = [l for l in links if 'pdf' in l['text'].lower() or 'download' in l['text'].lower()]
        
        if pdf_links:
            print(f"\n--- Testing fetch() on {len(pdf_links)} candidate links ---")
            for l in pdf_links:
                href = l['href']
                print(f"\n  Testing: {href[:100]}")
                result = await page.evaluate("""async (url) => {
                    try {
                        const r = await fetch(url);
                        const buf = await r.arrayBuffer();
                        const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
                        const prefixStr = prefix.map(b => String.fromCharCode(b)).join('');
                        return { status: r.status, size: buf.byteLength, prefix: prefix,
                                 prefixStr, contentType: r.headers.get('content-type') || '' };
                    } catch(e) {
                        return { error: e.message };
                    }
                }""", href)
                if 'error' in result:
                    print(f"    ERROR: {result['error']}")
                else:
                    print(f"    Status: {result['status']}, Size: {result['size']}, "
                          f"Prefix: '{result['prefixStr']}', Type: {result['contentType']}")
        
        await page.close()

asyncio.run(main())
