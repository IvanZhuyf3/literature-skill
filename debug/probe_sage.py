"""CDP probe: SAGE (journals.sagepub.com) page structure analysis.
Loads config from config.yaml so CDP URL is correct (19222).
"""

import json
import sys
import os
from urllib.parse import urljoin

# Add skill base to path
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

# Load config
import yaml
cfg_path = os.path.join(BASE, "config.yaml")
with open(cfg_path, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

from chromium_helper import ChromiumHelper

TARGET_URL = "https://journals.sagepub.com/doi/10.2310/7290.2007.00018"

def probe():
    helper = ChromiumHelper(config)
    result = helper.connect()
    if result is None:
        print("CDP_ERROR: Cannot connect to Edge at port 19222")
        return

    pw, browser = result
    page, ctx = helper.get_or_create_page(browser)

    try:
        print(f"Navigating to: {TARGET_URL}")
        page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=45000)
        try:
            page.wait_for_load_state("networkidle", timeout=20000)
        except Exception:
            print("  (networkidle timeout, continuing)")

        print(f"\n=== PAGE URL: {page.url} ===\n")

        # 1. Check all meta tags
        print("--- Meta Tags ---")
        meta_info = page.evaluate("""() => {
            const results = {};
            document.querySelectorAll('meta').forEach(m => {
                const name = m.getAttribute('name') || m.getAttribute('property') || '';
                const content = m.getAttribute('content') || '';
                if (name) results[name] = content;
            });
            return results;
        }""")
        for k, v in meta_info.items():
            print(f"  {k}: {v[:300]}")

        # 2. Check all links for PDF references
        print("\n--- PDF-related links ---")
        links = page.evaluate("""() => {
            const results = [];
            document.querySelectorAll('a[href]').forEach(a => {
                const href = a.getAttribute('href') || '';
                const text = (a.innerText || '').trim().toLowerCase();
                if (href.includes('.pdf') || href.includes('download') || text.includes('pdf') || text.includes('download') || text.includes('full text')) {
                    results.push({ href: href.slice(0, 300), text: (a.innerText||'').trim().slice(0, 100) });
                }
            });
            return results;
        }""")
        for link in links:
            print(f"  href={link['href']}")
            print(f"  text={link['text']}")
            print()

        # 3. citation_pdf_url
        print("\n--- Citation PDF URL ---")
        pdf_url = page.evaluate("""() => {
            const el = document.querySelector('meta[name="citation_pdf_url"]');
            return el ? el.content : null;
        }""")
        print(f"  citation_pdf_url: {pdf_url}")

        # 4. Check selectors for download buttons/links
        print("\n--- Download buttons/links ---")
        buttons = page.evaluate("""() => {
            const results = [];
            const selectors = [
                '[class*="download"]', '[class*="Download"]', '[class*="pdf"]', '[class*="PDF"]',
                '[id*="download"]', '[id*="Download"]',
                'a[href*="full.pdf"]', 'a[href*="pdf"]',
                'a[href*="/doi/pdf"]', 'button[class*="download"]',
                '[data-testid*="download"]', '[data-testid*="Download"]',
                '[data-testid*="pdf"]', '[data-testid*="PDF"]'
            ];
            selectors.forEach(sel => {
                document.querySelectorAll(sel).forEach(el => {
                    const href = el.getAttribute('href') || '';
                    const text = (el.innerText || el.textContent || '').trim().slice(0, 100);
                    const onclick = el.getAttribute('onclick') || '';
                    results.push({ selector: sel, href: href.slice(0, 300), text, onclick: onclick.slice(0,100) });
                });
            });
            return results;
        }""")
        for btn in buttons:
            print(f"  selector={btn['selector']}")
            if btn['href']: print(f"  href={btn['href']}")
            if btn['text']: print(f"  text={btn['text']}")
            if btn['onclick']: print(f"  onclick={btn['onclick']}")
            print()

        # 5. Check for iframes
        print("\n--- Iframes ---")
        iframes = page.evaluate("""() => {
            const results = [];
            document.querySelectorAll('iframe').forEach(f => {
                results.push({ src: f.getAttribute('src') || '', id: f.id, name: f.name });
            });
            return results;
        }""")
        for ifr in iframes:
            print(f"  id={ifr['id']}, name={ifr['name']}, src={ifr['src'][:200]}")
        if not iframes:
            print("  (none)")

        # 6. Check page for article PDF viewer
        print("\n--- Objects/Embeds ---")
        objs = page.evaluate("""() => {
            const results = [];
            document.querySelectorAll('object, embed').forEach(o => {
                results.push({ tag: o.tagName, data: o.getAttribute('data') || o.getAttribute('src') || '', type: o.getAttribute('type') || '' });
            });
            return results;
        }""")
        if objs:
            for obj in objs:
                print(f"  tag={obj['tag']}, data={obj['data']}, type={obj['type']}")
        else:
            print("  (none)")

        # 7. Look for 'article' or 'main' content divs
        print("\n--- Content areas ---")
        content = page.evaluate("""() => {
            const results = {};
            ['article', 'main', '.article', '.article-content', '#article', '#main-content', '.content'].forEach(sel => {
                const el = document.querySelector(sel);
                if (el) {
                    results[sel] = { tag: el.tagName, id: el.id, class: el.className.slice(0, 100) };
                }
            });
            const maybePdfViewer = document.querySelector('[class*="pdf"]') || document.querySelector('[class*="PDF"]') || document.querySelector('#pdf');
            if (maybePdfViewer) results['pdf_viewer_section'] = { tag: maybePdfViewer.tagName, id: maybePdfViewer.id, class: maybePdfViewer.className.slice(0, 100) };
            return results;
        }""")
        for k, v in content.items():
            print(f"  {k}: {v}")

        print("\n--- PROBE COMPLETE ---")

    except Exception as e:
        import traceback
        print(f"ERROR: {e}")
        traceback.print_exc()
    finally:
        try:
            helper.disconnect()
        except Exception:
            pass

if __name__ == "__main__":
    probe()
