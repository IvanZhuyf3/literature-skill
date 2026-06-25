"""debug_taylorfrancis3.py — robust access-state probe (handles page close)."""
import asyncio
from playwright.async_api import async_playwright

URL = "https://www.taylorfrancis.com/books/9780429437654/chapters/10.1201/b12907-21"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:19222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        try:
            resp = await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
            print(f"HTTP: {resp.status if resp else 'N/A'}")
            try:
                await page.wait_for_load_state("networkidle", timeout=25000)
            except Exception:
                pass
            await asyncio.sleep(3)
            print(f"Final URL: {page.url}")

            data = await page.evaluate("""() => {
                const body = document.body ? document.body.innerText : '';
                // login / access state
                const out = {};
                out.login_visible = /\\bLogin\\b|\\bSign in\\b|\\bLog in\\b/i.test(body);
                out.trial = /Request a trial|Request trial/i.test(body);
                out.purchase = /Purchase|Buy|Rent|Add to cart/i.test(body);
                out.download = /Download (PDF|chapter|book)/i.test(body);
                out.read = /Read (online|this chapter|book chapter)/i.test(body);
                out.preview = /Preview|Free preview|Abstract/i.test(body);
                out.inst_access = /Institutional access|You have access|Access provided by|University of|via your institution/i.test(body);
                out.denied = /Access denied|No access|Not available|Restricted/i.test(body);
                // count all clickable with access words
                const clicks = Array.from(document.querySelectorAll('a, button, [role="button"]'));
                out.access_buttons = clicks.filter(c => {
                    const t = ((c.innerText||'') + ' ' + (c.getAttribute('aria-label')||''));
                    return /download|read|access|pdf|purchase|trial|get access|view chapter/i.test(t);
                }).map(c => (c.innerText||'').trim().substring(0,40)).slice(0,15);
                // snippet of main content area
                const main = document.querySelector('main, .main, #main-content, .page-content, .chapter-detail');
                out.main_snippet = main ? main.innerText.substring(0, 600) : '(no main element)';
                out.title = document.title;
                return out;
            }""")
            for k, v in data.items():
                if k == 'main_snippet':
                    print(f"\n--- main snippet ---\n{v}")
                elif k == 'access_buttons':
                    print(f"access_buttons ({len(v)}): {v}")
                else:
                    print(f"{k}: {v}")
        except Exception as e:
            print(f"ERROR during probe: {e}")
        finally:
            try:
                await page.close()
            except Exception:
                pass


asyncio.run(main())
