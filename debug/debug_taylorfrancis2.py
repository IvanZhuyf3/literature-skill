"""debug_taylorfrancis2.py — deeper probe: login state, buttons, access."""
import asyncio
from playwright.async_api import async_playwright

URL = "https://www.taylorfrancis.com/chapters/edit/10.1201/b12907-21/multiplex-stimulated-raman-scattering-microscopy-dan-fu-xiaoliang-sunney-xie"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:19222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        try:
            await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
            try:
                await page.wait_for_load_state("networkidle", timeout=20000)
            except Exception:
                pass
            print(f"Final URL: {page.url}")
            print(f"Title: {await page.title()}")

            # Check for institutional access indicators
            access_info = await page.evaluate("""() => {
                const body = document.body.innerText;
                const checks = {
                    has_login: /\\bLogin\\b|\\bSign in\\b/i.test(body),
                    has_request_trial: /Request a trial/i.test(body),
                    has_purchase: /Purchase|Buy this|Rent|Subscribe/i.test(body),
                    has_download_pdf: /Download PDF|Download chapter|Download Book/i.test(body),
                    has_read_online: /Read online|Read this chapter|Read Book/i.test(body),
                    has_get_access: /Get Access|Open Access|Preview/i.test(body),
                    has_inst: /Institution|University|Shibboleth|Athens|IP access|Authenticated/i.test(body),
                    has_full_text: document.querySelector('.chapter-content, .book-content, .reader-container, #content') !== null,
                };
                return checks;
            }""")
            print("\n--- Access indicators ---")
            for k, v in access_info.items():
                print(f"  {k}: {v}")

            # All buttons on page
            buttons = await page.evaluate("""() => {
                return Array.from(document.querySelectorAll('button, a.btn, [role="button"], a[href]'))
                    .filter(b => {
                        const t = (b.innerText||'') + ' ' + (b.getAttribute('aria-label')||'');
                        return /download|read|access|purchase|trial|pdf|chapter|sign|login|open/i.test(t);
                    })
                    .map(b => ({tag: b.tagName, text:(b.innerText||'').trim().substring(0,50), href:(b.href||'').substring(0,100)}));
            }""")
            print(f"\n--- Buttons/links (access/download/read) ({len(buttons)}) ---")
            for b in buttons:
                print(f"  {b['tag']} text={b['text']!r} href={b['href']}")

            # Check for content reader / iframe
            frames = await page.evaluate("""() => {
                return Array.from(document.querySelectorAll('iframe')).map(f => ({src:(f.src||'').substring(0,120), id:f.id}));
            }""")
            print(f"\n--- Iframes ({len(frames)}) ---")
            for f in frames:
                print(f"  id={f['id']} src={f['src']}")

            # Check if there's a logged-in user indicator
            user = await page.evaluate("""() => {
                const m = document.body.innerText.match(/(?:Welcome|Hi|Hello|Logged in|You are|My Account)[^\\n]{0,60}/i);
                return m ? m[0] : '(no user indicator)';
            }""")
            print(f"\n--- User/login state: {user}")
        finally:
            await page.close()


asyncio.run(main())
