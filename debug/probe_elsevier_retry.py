"""CDP probe for Elsevier retry — diagnose the page structure."""
import logging, sys, json
sys.path.insert(0, r"C:\Users\Ivanz\OneDrive\Hermes_workspace\Literature_skill")
logging.basicConfig(level=logging.INFO)

from lit.core.config import load
from chromium_helper import ChromiumHelper

cfg = load()
helper = ChromiumHelper(cfg)
result = helper.connect()
if result is None:
    print("CDP_CONNECT_FAILED")
    sys.exit(1)
pw, browser = result
print("Connected!")

page, ctx = helper.get_or_create_page(browser)
url = "https://www.sciencedirect.com/science/article/pii/S0006349505727065"
page.goto(url, wait_until="domcontentloaded", timeout=60000)
import time; time.sleep(5)

print(f"Page URL: {page.url}")
print(f"Page title: {page.evaluate('() => document.title')}")

# CDN links
els = page.query_selector_all('a[href*="ars.els-cdn.com"]')
print(f"CDN links count: {len(els)}")
for el in els:
    href = el.get_attribute("href") or ""
    text = (el.inner_text() or "").strip()
    print(f"  CDN: href={href[:200]} text={text[:80]}")

# Aria-label PDF links
els2 = page.query_selector_all('a[aria-label*="PDF"]')
print(f"Aria-label PDF links: {len(els2)}")
for el in els2:
    href = el.get_attribute("href") or ""
    print(f"  href={href[:200]}")

# View PDF text match
els3 = page.query_selector_all('a:has-text("View PDF")')
print(f"View PDF links: {len(els3)}")
for el in els3:
    href = el.get_attribute("href") or ""
    print(f"  href={href[:200]}")

# pdfft links
els4 = page.query_selector_all('a[href*="/pdfft"]')
print(f"pdfft links: {len(els4)}")
for el in els4:
    href = el.get_attribute("href") or ""
    print(f"  href={href[:200]}")

# All PDF/download related links
pdf_data = page.evaluate("""() => {
    return Array.from(document.querySelectorAll('a')).map(a => ({
        href: a.href,
        text: a.innerText.trim().substring(0,80),
        cls: a.className.substring(0,80),
        aria: a.getAttribute('aria-label') || ''
    })).filter(x =>
        /pdf/i.test(x.href) || /download/i.test(x.href) ||
        /pdf/i.test(x.text) || /download/i.test(x.text) ||
        /pdf/i.test(x.aria) || /download/i.test(x.aria)
    );
}""")
print(f"All PDF/download links: {len(pdf_data)}")
for l in pdf_data:
    print(f"  href={l['href'][:200]} text='{l['text']}' aria='{l['aria']}'")

# Check for download buttons
btn_data = page.evaluate("""() => {
    const sel = 'button, [role="button"], .btn, [class*="button"], [class*="download"]';
    return Array.from(document.querySelectorAll(sel)).map(b => ({
        text: (b.innerText || b.textContent || '').trim().substring(0,80),
        cls: (b.className || '').substring(0,80),
        tag: b.tagName
    })).filter(x => /pdf|download|PDF|Download/i.test(x.text));
}""")
print(f"PDF/Download buttons: {len(btn_data)}")
for b in btn_data:
    print(f"  text='{b['text']}' class='{b['cls']}' tag={b['tag']}")

# Find any element containing "Download" or "View PDF" as pure text
text_nodes = page.evaluate("""() => {
    const results = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let node;
    while (node = walker.nextNode()) {
        const t = (node.textContent || '').trim();
        if (t === 'Download PDF' || t === 'View PDF' || t === 'Download') {
            const parent = node.parentElement;
            if (parent) {
                const rect = parent.getBoundingClientRect();
                if (rect.width > 0 && rect.height > 0) {
                    results.push({text: t, tag: parent.tagName, href: parent.href || parent.getAttribute('href') || '', cls: parent.className.substring(0,60)});
                }
            }
        }
        if (results.length > 20) break;
    }
    return results;
}""")
print(f"Text node matches: {len(text_nodes)}")
for n in text_nodes:
    print(f"  text='{n['text']}' tag={n['tag']} href='{n['href']}' class='{n['cls']}'")

# Also check the main content area for download buttons
main_area = page.evaluate("""() => {
    const results = [];
    const els = document.querySelectorAll('[class*="toolbar"], [class*="action"], [class*="button-group"], .article-actions, [id*="download"], [id*="action"]');
    for (const el of els) {
        results.push({
            html: el.innerHTML.substring(0, 300),
            cls: (el.className || '').substring(0,80),
            id: el.id || ''
        });
    }
    return results;
}""")
print(f"Toolbar/action sections: {len(main_area)}")
for s in main_area:
    print(f"  cls={s['cls']} id={s['id']}")
    print(f"  html={s['html'][:300]}")

# Save screenshot
save_dir = r"C:\Users\Ivanz\OneDrive\Hermes_workspace\Literature_skill\people\data"
page.screenshot(path=save_dir + "/elsevier_probe.png")
print("Screenshot saved.")

helper.disconnect()
