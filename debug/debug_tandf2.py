"""debug_tandf2.py — 深入探测 T&F 页面，看是否有隐藏的 PDF 链接"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        
        url = "https://www.tandfonline.com/doi/full/10.1080/17576180.2026.2668687"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        # 等久一点
        await page.wait_for_timeout(10000)
        
        print(f"Final URL: {page.url}")
        
        # 检查所有 meta 标签
        all_metas = await page.evaluate("""() => {
            return Array.from(document.querySelectorAll('meta')).map(m => ({
                name: m.name || m.getAttribute('property') || '',
                content: (m.content || '').substring(0, 100),
            })).filter(m => m.name);
        }""")
        print(f"\nAll meta tags ({len(all_metas)}):")
        for m in all_metas:
            if any(k in m['name'].lower() for k in ['citation', 'dc.', 'og:', 'title', 'doi']):
                print(f"  {m['name']}: {m['content']}")
        
        # 检查所有 a 标签（不限 PDF 关键词）
        all_links = await page.evaluate("""() => {
            return Array.from(document.querySelectorAll('a[href]')).slice(0, 50).map(a => ({
                href: (a.href || '').substring(0, 120),
                text: (a.innerText || '').trim().substring(0, 40),
                class: (a.className || '').substring(0, 60),
            }));
        }""")
        print(f"\nFirst 50 links:")
        for l in all_links:
            if any(k in l['href'].lower() for k in ['pdf', 'download', 'epdf']):
                print(f"  >>> {l['href']}  [{l['text']}]  class={l['class']}")
            elif any(k in l['text'].lower() for k in ['pdf', 'download']):
                print(f"  >>> {l['href']}  [{l['text']}]  class={l['class']}")
        
        # 看看页面有没有 "Access" 相关文字
        access_text = await page.evaluate("""() => {
            const body = document.body.innerText;
            const lines = body.split('\\n').filter(l => /access|purchase|subscribe|sign in|login|buy/i.test(l));
            return lines.slice(0, 5);
        }""")
        print(f"\nAccess-related text:")
        for t in access_text:
            print(f"  {t[:100]}")
        
        await page.close()

asyncio.run(main())
