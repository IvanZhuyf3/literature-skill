"""debug_jove5.py — Inspect /pdf/ viewer page; try page.expect_download + expect_popup."""
import asyncio
from playwright.async_api import async_playwright

ARTICLE = "https://www.jove.com/t/64882/coherent-raman-microscopy-from-instrumentation-to-applications"
PDF_VIEWER = "https://www.jove.com/pdf/64882/coherent-raman-microscopy-from-instrumentation-to-applications"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:19222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        # ---- Part A: inspect /pdf/ viewer page ----
        print("=== Inspecting /pdf/ viewer page ===")
        responses = []
        page.on("response", lambda r: responses.append(
            {"status": r.status, "url": r.url, "ctype": r.headers.get("content-type","")}
        ))

        await page.goto(PDF_VIEWER, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=20000)
        except Exception:
            pass
        print(f"Final URL: {page.url}")

        info = await page.evaluate("""() => ({
            title: document.title,
            iframes: Array.from(document.querySelectorAll('iframe')).map(i=>i.src),
            embeds: Array.from(document.querySelectorAll('embed,object[data]')).map(e=>e.src||e.data||''),
            canvases: document.querySelectorAll('canvas').length,
            buttons: Array.from(document.querySelectorAll('button,a')).filter(a => /download|pdf|save|print/i.test((a.innerText||'')+(a.getAttribute('aria-label')||'')+(a.href||''))).map(a=>({tag:a.tagName,href:a.href||'',text:(a.innerText||'').trim().substring(0,50),aria:a.getAttribute('aria-label')||''})),
            bodyText: document.body ? document.body.innerText.substring(0,500) : ''
        })""")
        print(f"  title: {info['title']}")
        print(f"  iframes ({len(info['iframes'])}): {info['iframes'][:5]}")
        print(f"  embeds: {info['embeds']}")
        print(f"  canvases: {info['canvases']}")
        print(f"  buttons: {info['buttons']}")
        print(f"  bodyText: {info['bodyText'][:300]}")

        # Show all responses that look like PDF/binary
        print(f"\n  PDF/binary responses:")
        for r in responses:
            cl = r['ctype'].lower()
            if 'pdf' in r['url'].lower() or 'pdf' in cl or 'octet' in cl or 'binary' in cl:
                print(f"    {r}")

        # ---- Part B: go back to article, click button with expect_popup/expect_download ----
        print("\n=== Clicking Download PDF on article page ===")
        await page.goto(ARTICLE, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=20000)
        except Exception:
            pass
        btn = await page.query_selector('button[aria-label="Download PDF"]')

        clicked_ok = False
        if btn:
            # Try popup first
            try:
                async with ctx.expect_page(timeout=10000) as pi:
                    await btn.click()
                popup = await pi.value
                clicked_ok = True
                print(f"Popup opened, URL: {popup.url}")
                try:
                    await popup.wait_for_load_state("domcontentloaded", timeout=15000)
                except Exception:
                    pass
                print(f"Popup final URL: {popup.url}")
                pinfo = await popup.evaluate("""() => ({
                    title: document.title,
                    iframes: Array.from(document.querySelectorAll('iframe')).map(i=>i.src),
                    embeds: Array.from(document.querySelectorAll('embed,object[data]')).map(e=>e.src||e.data||''),
                    bodyText: document.body ? document.body.innerText.substring(0,400) : ''
                })""")
                print(f"  title: {pinfo['title']}")
                print(f"  iframes: {pinfo['iframes'][:5]}")
                print(f"  embeds: {pinfo['embeds']}")
                print(f"  bodyText: {pinfo['bodyText'][:300]}")
            except Exception as e:
                print(f"No popup: {e}")

        if btn and not clicked_ok:
            try:
                async with page.expect_download(timeout=10000) as di:
                    await btn.click()
                d = await di.value
                print(f"Download: {d.suggested_filename}, url={d.url}")
            except Exception as e:
                print(f"No download: {e}")

        await page.close()


asyncio.run(main())
