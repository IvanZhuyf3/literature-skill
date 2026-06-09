"""
CDP 探测脚本 — SPIE Digital Library
目标: 了解页面 DOM、PDF 链接、metadata 结构
"""
import asyncio
from playwright.async_api import async_playwright

URL = "https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-5/issue-01/015001/Topological-transformation-and-free-space-transport-of-photonic-hopfions/10.1117/1.AP.5.1.015001.full"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = await context.new_page()

        print(f"Navigating to {URL} ...")
        resp = await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        print(f"Status: {resp.status if resp else 'None'}")

        await asyncio.sleep(8)

        # 1. Title + meta
        title = await page.evaluate("""() => {
            const t = document.querySelector('meta[name="citation_title"]');
            const d = document.querySelector('meta[name="dc.title"]');
            return {
                citation_title: t ? t.content : null,
                dc_title: d ? d.content : null,
                doc_title: document.title
            };
        }""")
        print(f"\n=== TITLE ===\n{title}")

        # 2. All citation_* and dc.* meta tags
        metas = await page.evaluate("""() => {
            const tags = document.querySelectorAll('meta[name]');
            const result = {};
            for (const t of tags) {
                const name = t.getAttribute('name');
                if (name.startsWith('citation_') || name.startsWith('dc.')) {
                    if (result[name]) {
                        if (!Array.isArray(result[name])) result[name] = [result[name]];
                        result[name].push(t.content);
                    } else {
                        result[name] = t.content;
                    }
                }
            }
            return result;
        }""")
        print(f"\n=== META TAGS ===\n{metas}")

        # 3. PDF-related links
        pdf_elements = await page.evaluate("""() => {
            const results = [];
            const selectors = [
                'a[href*="pdf"]',
                'a[href*="PDF"]',
                'a[href*="download"]',
                'a[href*="Download"]',
                'button[class*="pdf"]',
                'a[class*="pdf"]',
                'a[class*="PDF"]',
                'a[title*="PDF"]',
                'a[aria-label*="PDF"]',
                '.pdf-download',
                'a[class*="article-pdf"]',
                'a[class*="FullText"]',
            ];
            for (const sel of selectors) {
                try {
                    const els = document.querySelectorAll(sel);
                    for (const el of els) {
                        results.push({
                            selector: sel,
                            tag: el.tagName,
                            href: el.href || el.getAttribute('href') || null,
                            text: el.textContent.trim().substring(0, 100),
                            class: (el.className || '').toString().substring(0, 80),
                        });
                    }
                } catch(e) {}
            }
            return results;
        }""")
        print(f"\n=== PDF ELEMENTS ({len(pdf_elements)}) ===")
        for el in pdf_elements:
            print(f"  {el['selector']}: tag={el['tag']} href={el['href']} text='{el['text'][:60]}' class={el['class'][:60]}")

        # 4. DOI
        article_info = await page.evaluate("""() => {
            const doi = document.querySelector('meta[name="citation_doi"]') ||
                        document.querySelector('meta[name="dc.identifier"]');
            const dateEl = document.querySelector('meta[name="citation_date"]') ||
                           document.querySelector('meta[name="citation_online_date"]');
            const pdfUrl = document.querySelector('meta[name="citation_pdf_url"]');
            return {
                doi: doi ? doi.content : null,
                date: dateEl ? dateEl.content : null,
                citation_pdf_url: pdfUrl ? pdfUrl.content : null,
            };
        }""")
        print(f"\n=== ARTICLE INFO ===\n{article_info}")

        # 5. Final URL
        print(f"\n=== FINAL URL ===\n{page.url}")

        # 6. Try fetch on citation_pdf_url if available
        if article_info.get('citation_pdf_url'):
            fetch_test = await page.evaluate("""async (pdfUrl) => {
                try {
                    const resp = await fetch(pdfUrl);
                    const contentType = resp.headers.get('content-type');
                    if (contentType && contentType.includes('pdf')) {
                        const buf = await resp.arrayBuffer();
                        const bytes = new Uint8Array(buf);
                        const header = [];
                        for (let i = 0; i < Math.min(10, bytes.length); i++) header.push(bytes[i]);
                        return { status: resp.status, contentType, size: buf.byteLength, header };
                    } else {
                        const text = await resp.text();
                        return { status: resp.status, contentType, url: resp.url, textPreview: text.substring(0, 300) };
                    }
                } catch(e) {
                    return { error: e.message };
                }
            }""", article_info['citation_pdf_url'])
            print(f"\n=== FETCH citation_pdf_url ===")
            for k, v in fetch_test.items():
                print(f"  {k}: {str(v)[:200]}")

        await page.close()
        print("\nDone.")

asyncio.run(main())
