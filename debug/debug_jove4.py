"""debug_jove4.py — Click JoVE Download PDF button, listen for downloads + nav events."""
import asyncio
from playwright.async_api import async_playwright

URL = "https://www.jove.com/t/64882/coherent-raman-microscopy-from-instrumentation-to-applications"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:19222")
        ctx = browser.contexts[0]

        new_pages = []
        ctx.on("page", lambda pg: new_pages.append(pg))

        page = await ctx.new_page()
        downloads = []
        ctx.on("download", lambda d: downloads.append(d))

        # Capture responses with PDF content-type or pdf in URL
        pdf_resps = []
        page.on("response", lambda r: pdf_resps.append(
            {"status": r.status, "url": r.url, "ctype": r.headers.get("content-type","")}
        ) if ("pdf" in r.url.lower() or "pdf" in r.headers.get("content-type","").lower()) else None)

        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except Exception:
            pass
        print(f"Loaded: {page.url}")

        # Check body text for access indicators
        body_text = await page.evaluate("() => document.body.innerText.substring(0, 1500)")
        access_hints = [l for l in body_text.split('\n') if any(k in l.lower() for k in ['subscribe','access','login','sign in','trial','download'])]
        print(f"\nAccess-related text lines:")
        for l in access_hints[:15]:
            print(f"  | {l.strip()[:100]}")

        btn = await page.query_selector('button[aria-label="Download PDF"]')
        print(f"\nFound Download PDF button: {btn is not None}")

        if btn:
            # Try expect_download
            try:
                async with ctx.expect_download(timeout=15000) as di:
                    await btn.click()
                d = await di.value
                print(f"DOWNLOAD triggered: filename={d.suggested_filename}, url={d.url}")
            except Exception as e:
                print(f"No ctx download event: {e}")

        await asyncio.sleep(4)
        print(f"\nDownloads: {len(downloads)} | New pages: {len(new_pages)}")
        for np_ in new_pages:
            try:
                print(f"  new page: {np_.url}")
            except Exception:
                pass

        print(f"\nPDF-ish responses ({len(pdf_resps)}):")
        for r in pdf_resps[-15:]:
            print(f"  {r}")

        # Inspect any new page
        if new_pages:
            np = new_pages[-1]
            try:
                await np.wait_for_load_state("domcontentloaded", timeout=10000)
                print(f"\nNew page final URL: {np.url}")
                np_info = await np.evaluate("""() => ({
                    iframes: Array.from(document.querySelectorAll('iframe')).map(i=>i.src),
                    embeds: Array.from(document.querySelectorAll('embed,object[data]')).map(e=>e.src||e.data),
                    title: document.title,
                    bodyStart: document.body ? document.body.innerText.substring(0,300) : ''
                })""")
                print(f"  title: {np_info['title']}")
                print(f"  iframes: {np_info['iframes']}")
                print(f"  embeds: {np_info['embeds']}")
                print(f"  body: {np_info['bodyStart'][:200]}")
            except Exception as e:
                print(f"  new page inspect failed: {e}")

        await page.close()


asyncio.run(main())
