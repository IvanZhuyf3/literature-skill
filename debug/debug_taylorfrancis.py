"""debug_taylorfrancis.py — probe taylorfrancis.com book chapter page via CDP.

Target DOI: 10.1201/b12907-21
Goal: find PDF download flow for CRC Press / T&F books (taylorfrancis.com).
"""
import asyncio
from playwright.async_api import async_playwright

DOI = "10.1201/b12907-21"
URL = "https://www.taylorfrancis.com/books/9780429437654/chapters/10.1201/b12907-21"
# Also try the edit/ URL the engine produced
URL_EDIT = "https://www.taylorfrancis.com/chapters/edit/10.1201/b12907-21/multiplex-stimulated-raman-scattering-microscopy-dan-fu-xiaoliang-sunney-xie"


async def probe(page, url, label):
    print(f"\n{'='*70}\n[{label}] Navigating to:\n  {url}\n{'='*70}")
    try:
        resp = await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        print(f"  HTTP status: {resp.status if resp else 'N/A'}")
    except Exception as e:
        print(f"  Navigation FAILED: {e}")
        return
    try:
        await page.wait_for_load_state("networkidle", timeout=20000)
    except Exception:
        pass
    print(f"  Final URL: {page.url}")
    print(f"  Title: {(await page.title())[:100]}")

    # 1. Body text snippet (to detect paywall / login / access denied)
    body_snippet = await page.evaluate("() => document.body ? document.body.innerText.substring(0, 400) : '(no body)'")
    print(f"\n  --- Body snippet ---\n  {body_snippet[:400]}")

    # 2. All pdf/download-related links
    links = await page.evaluate("""() => {
        const all = document.querySelectorAll('a[href], button');
        return Array.from(all)
            .filter(a => /pdf|download|chapter|read|access|preview|chapter.pdf|full\\s*text/i.test(
                (a.href || '') + ' ' + (a.innerText || '') + ' ' + (a.getAttribute('aria-label')||'')))
            .map(a => ({
                href: (a.href || '').substring(0, 140),
                text: (a.innerText || '').trim().substring(0, 60),
                tag: a.tagName,
                class: (a.className || '').toString().substring(0, 80),
                aria: a.getAttribute('aria-label') || '',
            }));
    }""")
    print(f"\n  --- PDF/download/read links ({len(links)}) ---")
    for i, l in enumerate(links):
        print(f"  [{i}] tag={l['tag']} text={l['text']!r}")
        print(f"       href={l['href']}")
        print(f"       class={l['class']!r} aria={l['aria']!r}")


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:19222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        try:
            await probe(page, URL, "books URL")
            await probe(page, URL_EDIT, "edit URL")
        finally:
            await page.close()


asyncio.run(main())
