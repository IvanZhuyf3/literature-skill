"""debug_jove3.py — Properly click JoVE Download PDF button + listen for downloads."""
import asyncio
from playwright.async_api import async_playwright

URL = "https://www.jove.com/t/64882/coherent-raman-microscopy-from-instrumentation-to-applications"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:19222")
        ctx = browser.contexts[0]

        # Check subscription state via cookies/LS
        page = await ctx.new_page()
        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except Exception:
            pass

        # Read subscription response by re-fetching the API
        sub = await page.evaluate("""async () => {
            const r = await fetch('https://api.jove.com/api/free/subscription', {credentials:'include'});
            return {status: r.status, body: await r.text()};
        }""")
        print(f"=== subscription API ===\n  status={sub['status']}\n  body={sub['body'][:500]}")

        prof = await page.evaluate("""async () => {
            try {
                const r = await fetch('https://api.jove.com/api/profile', {credentials:'include'});
                return {status: r.status, body: (await r.text())[:500]};
            } catch(e) { return {error: String(e)}; }
        }""")
        print(f"\n=== profile API ===\n  {prof}")

        # Set up download listener
        downloads = []
        ctx.on("download", lambda d: downloads.append(d))

        # Click the Download PDF button
        btn = await page.query_selector('button[aria-label="Download PDF"]')
        print(f"\nFound button: {btn is not None}")

        if btn:
            # Use expect_download pattern
            try:
                async with page.expect_download(timeout=15000) as di:
                    await btn.click()
                d = await di.value
                print(f"DOWNLOAD triggered: {d.suggested_filename}, url={d.url}")
                downloads.append(d)
            except Exception as e:
                print(f"No download event from main button click: {e}")

        await asyncio.sleep(3)
        print(f"\nDownloads count: {len(downloads)}")

        # Now navigate to /pdf/ page and inspect
        print("\n=== Navigating to /pdf/ viewer page ===")
        pdf_page_url = "https://www.jove.com/pdf/64882/coherent-raman-microscopy-from-instrumentation-to-applications"
        await page.goto(pdf_page_url, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=20000)
        except Exception:
            pass
        print(f"Final URL: {page.url}")

        # Look for embedded PDF / iframe / download button on viewer page
        view_info = await page.evaluate("""() => {
            const out = {};
            out.iframes = Array.from(document.querySelectorAll('iframe')).map(i => i.src);
            out.embeds = Array.from(document.querySelectorAll('embed, object[data]')).map(e => e.src || e.data);
            out.buttons = Array.from(document.querySelectorAll('button, a')).filter(
                a => /download|pdf/i.test((a.innerText||'')+(a.getAttribute('aria-label')||'')+(a.href||''))
            ).map(a => ({tag:a.tagName, href:a.href||'', text:(a.innerText||'').trim().substring(0,60), aria:a.getAttribute('aria-label')||''}));
            out.bodyStart = document.body ? document.body.innerText.substring(0, 300) : '(no body)';
            return out;
        }""")
        print(f"iframes: {view_info['iframes']}")
        print(f"embeds: {view_info['embeds']}")
        print(f"buttons: {view_info['buttons']}")
        print(f"body start: {view_info['bodyStart'][:200]}")

        await page.close()


asyncio.run(main())
