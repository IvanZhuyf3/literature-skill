"""debug_jove2.py — 探测 JoVE Download PDF 按钮点击行为.

Strategy:
  - Listen to network requests, click "Download PDF" button
  - Check for download triggers, new tabs, network PDF requests
"""
import asyncio
from playwright.async_api import async_playwright

URL = "https://www.jove.com/t/64882/coherent-raman-microscopy-from-instrumentation-to-applications"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:19222")
        ctx = browser.contexts[0]

        # Capture new pages (tabs) opened
        new_pages = []
        ctx.on("page", lambda pg: new_pages.append(pg))

        page = await ctx.new_page()

        # Capture relevant network requests
        interesting = []
        page.on("request", lambda req: interesting.append(
            {"type": "request", "method": req.method, "url": req.url,
             "rtype": req.resource_type}
        ) if any(k in req.url.lower() for k in [".pdf", "/pdf", "download", "/api/", "file"]) else None)
        page.on("response", lambda resp: interesting.append(
            {"type": "response", "status": resp.status, "url": resp.url,
             "ctype": resp.headers.get("content-type", "")}
        ) if any(k in resp.url.lower() for k in [".pdf", "/pdf", "download", "/api/", "file"]) else None)

        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except Exception:
            pass

        print(f"Loaded: {page.url}")

        # Try the main Download PDF button
        btn = page.query_selector('button[aria-label="Download PDF"]')
        if not btn:
            btn = page.query_selector('button.download-pdf-button, .text-article-action-buttons-download-pdf-button')
        print(f"Found Download PDF button: {btn is not None}")

        if btn:
            try:
                await btn.click(timeout=10000)
                print("Clicked Download PDF button")
            except Exception as e:
                print(f"Click failed: {e}")

            # Wait for things to happen
            await asyncio.sleep(6)

            print(f"\nPage URL after click: {page.url}")
            print(f"New pages opened: {len(new_pages)}")
            for np_ in new_pages:
                try:
                    print(f"  new page URL: {np_.url}")
                except Exception:
                    pass

        print(f"\n=== Interesting network events ({len(interesting)}) ===")
        for ev in interesting[-40:]:
            print(f"  {ev}")

        # Check if a menu opened with a direct download option
        menu_items = await page.evaluate("""() => {
            const items = document.querySelectorAll('a, button, [role="menuitem"], [role="menuitemradio"]');
            return Array.from(items)
                .filter(a => /download|pdf/i.test((a.innerText || '') + (a.getAttribute('aria-label') || '') + (a.href || '')))
                .map(a => ({
                    tag: a.tagName,
                    href: a.href || '',
                    text: (a.innerText || '').trim().substring(0, 80),
                    aria: a.getAttribute('aria-label') || '',
                    class: (a.className || '').toString().substring(0, 100),
                }));
        }""")
        print(f"\n=== Menu items after click ({len(menu_items)}) ===")
        for m in menu_items:
            print(f"  {m}")

        # Try direct download URL patterns
        for pattern in [
            "https://www.jove.com/pdf/64882?download=true",
            "https://www.jove.com/download/pdf/64882",
        ]:
            print(f"\n=== Testing fetch: {pattern} ===")
            try:
                result = await page.evaluate("""async (url) => {
                    try {
                        const r = await fetch(url, {credentials: 'include'});
                        const buf = await r.arrayBuffer();
                        const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
                        return { status: r.status, size: buf.byteLength, prefix,
                                 contentType: r.headers.get('content-type') };
                    } catch (e) { return { error: String(e) }; }
                }""", pattern)
                print(f"  {result}")
                if 'prefix' in result:
                    print(f"  Is PDF: {bytes(result['prefix']) == b'%PDF'}")
            except Exception as e:
                print(f"  failed: {e}")

        await page.close()


asyncio.run(main())
