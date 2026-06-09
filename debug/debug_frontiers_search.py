"""debug_frontiers_search.py — 用 CDP 搜索 Frontiers 论文"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        # 搜索 Frontiers 上的 OA 论文
        await page.goto("https://www.frontiersin.org/search?query=machine+learning&tab=articles",
                        wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except:
            pass

        print(f"Search page: {page.url}")

        # 提取搜索结果中的文章链接
        articles = await page.evaluate("""() => {
            const links = document.querySelectorAll('a[href*="/articles/"]');
            return Array.from(links).slice(0, 5).map(a => ({
                href: a.href,
                text: (a.innerText || '').trim().substring(0, 80),
            }));
        }""")
        print(f"\nFound {len(articles)} article links:")
        for a in articles:
            print(f"  {a['href']}")
            print(f"    [{a['text']}]")

        await page.close()

asyncio.run(main())
