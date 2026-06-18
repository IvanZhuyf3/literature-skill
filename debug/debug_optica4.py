"""debug_optica4.py — 探测 DOI 10.1364/ao.39.002221 的页面结构

问题：DOI 解析到 viewmedia.cfm?html=true (HTML 视图)，
      adapter 找不到 Get PDF 按钮。
目标：找到从 HTML 视图或文章页提取 PDF 链接的方法。
"""
import asyncio
from playwright.async_api import async_playwright

CDP_PORT = 19222

async def probe_page(page, label, url):
    """探测一个页面的链接结构。"""
    print(f"\n{'='*60}")
    print(f"[{label}] URL: {url}")
    await page.goto(url, wait_until="domcontentloaded", timeout=60000)
    try:
        await page.wait_for_load_state("networkidle", timeout=15000)
    except:
        pass

    print(f"  Final URL: {page.url}")

    # 1. 所有 PDF/download/viewmedia 相关链接
    links = await page.evaluate("""() => {
        const all = document.querySelectorAll('a[href]');
        return Array.from(all)
            .filter(a => /pdf|download|viewmedia|getpdf|fulltext|abstract|citation_pdf/i.test(
                (a.href || '') + (a.innerText || '') + (a.getAttribute('aria-label') || '')))
            .map(a => ({
                href: a.href || '',
                text: (a.innerText || '').trim().substring(0, 80),
                class: (a.className || '').substring(0, 80),
                aria: a.getAttribute('aria-label') || '',
            }));
    }""")
    print(f"  Found {len(links)} candidate links:")
    for i, l in enumerate(links):
        print(f"    [{i}] text='{l['text']}' class='{l['class']}'")
        print(f"        href={l['href']}")

    # 2. citation_pdf_url meta tag
    pdf_meta = await page.evaluate("""() => {
        const el = document.querySelector('meta[name="citation_pdf_url"]');
        return el ? el.content : null;
    }""")
    print(f"  citation_pdf_url: {pdf_meta}")

    # 3. citation_title
    title = await page.evaluate("""() => {
        const el = document.querySelector('meta[name="citation_title"]');
        return el ? el.content : '(not found)';
    }""")
    print(f"  citation_title: {title[:80] if title else '(none)'}")

    return pdf_meta

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(f"http://localhost:{CDP_PORT}")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        uri = "ao-39-13-2221"

        # 1. 先看 HTML 视图页（DOI 解析到的）
        await probe_page(page, "HTML view", f"https://opg.optica.org/ao/viewmedia.cfm?uri={uri}&html=true")

        # 2. 文章摘要页
        await probe_page(page, "abstract.cfm", f"https://opg.optica.org/ao/abstract.cfm?uri={uri}")

        # 3. fulltext 页
        await probe_page(page, "fulltext.cfm", f"https://opg.optica.org/ao/fulltext.cfm?uri={uri}")

        # 4. 直接试 viewmedia.cfm 不带 html=true（PDF 路径）
        print("\n" + "="*60)
        print("[PDF viewmedia] Testing viewmedia.cfm without html=true")
        pdf_view = f"https://opg.optica.org/ao/viewmedia.cfm?uri={uri}&seq=0"
        await page.goto(pdf_view, wait_until="domcontentloaded", timeout=60000)
        await asyncio.sleep(3)
        print(f"  Final URL after viewmedia.cfm?seq=0: {page.url}")

        # 检查是否重定向到了 directpdfaccess 或 view_article
        current = page.url
        if "directpdfaccess" in current:
            print(f"  → Direct PDF access reached!")
            # 测试 fetch
            r = await page.evaluate("""async (url) => {
                try {
                    const r = await fetch(url);
                    const buf = await r.arrayBuffer();
                    const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                    const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                    return {status:r.status, size:buf.byteLength, prefix:ps,
                            type:r.headers.get('content-type')||''};
                } catch(e) { return {error:e.message}; }
            }""", current)
            if 'error' in r:
                print(f"  fetch ERROR: {r['error']}")
            else:
                print(f"  Status:{r['status']} Size:{r['size']} PDF:{r['prefix'].startswith('%PDF')} Type:{r['type']}")
        elif "view_article.cfm" in current:
            print(f"  → view_article.cfm reached (redirect chain A)")
        else:
            print(f"  → Stuck at: {current}")
            # 检查页面内容
            body_start = await page.evaluate("() => document.body ? document.body.innerText.substring(0, 300) : '(no body)'")
            print(f"  Body preview: {body_start[:200]}")

        await page.close()

asyncio.run(main())
