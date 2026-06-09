"""debug_optica2.py — 探测 viewmedia.cfm 重定向链"""
import asyncio
import time
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        # 1. 先加载文章页
        url = "https://opg.optica.org/ol/fulltext.cfm?uri=ol-51-10-2784"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except:
            pass
        print(f"Article page: {page.url}")

        # 2. 找 Get PDF 链接
        pdf_link = await page.evaluate("""() => {
            const links = document.querySelectorAll('a');
            for (const a of links) {
                if (a.innerText.trim() === 'Get PDF' && a.href.includes('viewmedia')) {
                    return a.href;
                }
            }
            return null;
        }""")
        print(f"PDF link: {pdf_link}")

        # 3. 导航到 viewmedia.cfm，观察重定向
        print(f"\nNavigating to viewmedia...")
        try:
            resp = await page.goto(pdf_link, wait_until="domcontentloaded", timeout=30000)
            print(f"  Initial status: {resp.status if resp else 'None'}")
        except Exception as e:
            print(f"  goto exception: {e}")

        # 4. 轮询 URL 变化
        print(f"\nPolling URL changes...")
        for i in range(30):
            current = page.url
            print(f"  [{i+1}s] {current}")
            if "view_article.cfm" in current and "pdfKey=" in current:
                print(f"\n  => Got view_article.cfm with pdfKey!")
                break
            if "directpdfaccess" in current:
                print(f"\n  => Reached directpdfaccess directly!")
                break
            time.sleep(1)

        # 5. 检查页面内容（可能停在 JS 挑战页面）
        page_info = await page.evaluate("""() => {
            return {
                title: document.title,
                bodyText: document.body?.innerText?.substring(0, 300) || '',
                forms: document.querySelectorAll('form').length,
                scripts: document.querySelectorAll('script[src]').length,
                metaRefresh: document.querySelector('meta[http-equiv="refresh"]')?.content || '',
            };
        }""")
        print(f"\nPage info after 30s:")
        for k, v in page_info.items():
            print(f"  {k}: {v}")

        # 6. 试直接 fetch /doi/pdf/ DOI
        doi = "10.1364/OL.51.002784"
        for test_url in [
            f"https://opg.optica.org/doi/pdf/{doi}",
            f"https://opg.optica.org/doi/pdfdirect/{doi}?download=true",
        ]:
            print(f"\nFetch test: {test_url}")
            r = await page.evaluate("""async (url) => {
                try {
                    const r = await fetch(url);
                    const buf = await r.arrayBuffer();
                    const prefix = Array.from(new Uint8Array(buf.slice(0,4)));
                    const ps = prefix.map(b=>String.fromCharCode(b)).join('');
                    return {status:r.status, size:buf.byteLength, prefix:ps,
                            type:r.headers.get('content-type')||''};
                } catch(e) { return {error:e.message}; }
            }""", test_url)
            if 'error' in r:
                print(f"  ERROR: {r['error']}")
            else:
                print(f"  Status:{r['status']} Size:{r['size']} PDF:{r['prefix'].startswith('%PDF')} Type:{r['type']}")

        await page.close()

asyncio.run(main())
