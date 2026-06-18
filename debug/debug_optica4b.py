"""debug_optica4b.py — check_access false positive diagnosis"""
import asyncio
from playwright.async_api import async_playwright

CDP_PORT = 19222

BLOCKED = [
    "Access Denied", "Purchase this article", "Buy this article",
    "Sign in to access", "You do not have access", "Not available", "403",
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(f"http://localhost:{CDP_PORT}")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        await page.goto("https://opg.optica.org/ao/viewmedia.cfm?uri=ao-39-13-2221&html=true",
                        wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=15000)
        except:
            pass

        print(f"Final URL: {page.url}")

        body_text = await page.inner_text("body")
        for indicator in BLOCKED:
            if indicator.lower() in body_text.lower():
                # Find context around the match
                idx = body_text.lower().find(indicator.lower())
                start = max(0, idx - 80)
                end = min(len(body_text), idx + len(indicator) + 80)
                context = body_text[start:end].replace('\n', ' ').replace('\r', '')
                print(f"MATCH: '{indicator}' → context: ...{context}...")

        await page.close()

asyncio.run(main())
