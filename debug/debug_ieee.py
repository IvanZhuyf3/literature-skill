"""
CDP 探测脚本 — IEEE Xplore
目标: 了解页面 DOM、PDF 链接、metadata 结构
"""
import asyncio
from playwright.async_api import async_playwright

URL = "https://ieeexplore.ieee.org/document/594865"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = await context.new_page()

        print(f"Navigating to {URL} ...")
        resp = await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        print(f"Status: {resp.status}")

        # Wait for content
        await asyncio.sleep(8)

        # 1. Title
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

        # 3. Find PDF-related links/buttons
        pdf_elements = await page.evaluate("""() => {
            const results = [];
            // Check common PDF selectors
            const selectors = [
                'a[href*="pdf"]',
                'a[href*="PDF"]',
                'a[href*="stamp"]',
                'a[href*="download"]',
                'a[href*="full-text"]',
                'button[class*="pdf"]',
                'a[class*="pdf"]',
                'a[class*="document-pdf"]',
                'a[ng-click*="pdf"]',
                'a[title*="PDF"]',
                'a[aria-label*="PDF"]',
                'a[data-target*="pdf"]',
                '.pdf-download',
                '#pdf-link',
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
                            class: el.className,
                        });
                    }
                } catch(e) {}
            }
            return results;
        }""")
        print(f"\n=== PDF ELEMENTS ({len(pdf_elements)}) ===")
        for el in pdf_elements:
            print(f"  {el['selector']}: tag={el['tag']} href={el['href']} text='{el['text'][:60]}' class={el['class'][:60] if el['class'] else ''}")

        # 4. Check for any links with document ID pattern
        doc_links = await page.evaluate("""() => {
            const links = document.querySelectorAll('a[href]');
            const results = [];
            for (const a of links) {
                const href = a.href || '';
                if (href.includes('stamp') || href.includes('iel7') || href.includes('stampPDF') || 
                    href.includes('/iel/') || href.includes('document/594865') || href.includes('.pdf')) {
                    results.push({
                        href: href,
                        text: a.textContent.trim().substring(0, 60),
                        class: a.className.substring(0, 60)
                    });
                }
            }
            return results;
        }""")
        print(f"\n=== DOC-RELATED LINKS ({len(doc_links)}) ===")
        for l in doc_links:
            print(f"  href={l['href'][:120]} text='{l['text'][:40]}'")

        # 5. Check page URL after load (any redirects?)
        print(f"\n=== FINAL URL ===\n{page.url}")

        # 6. Try to find the article number / DOI from page
        article_info = await page.evaluate("""() => {
            const doi = document.querySelector('meta[name="citation_doi"]') ||
                        document.querySelector('meta[name="dc.identifier"]');
            const docId = document.querySelector('meta[name="citation_articleNumber"]') ||
                          document.querySelector('meta[name="articleNumber"]');
            // Also try to find DOI in page text
            const doiLinks = document.querySelectorAll('a[href*="doi.org"]');
            const doiHrefs = [];
            for (const a of doiLinks) {
                doiHrefs.push(a.href);
            }
            return {
                doi: doi ? doi.content : null,
                articleNumber: docId ? docId.content : null,
                doiHrefs: doiHrefs
            };
        }""")
        print(f"\n=== ARTICLE INFO ===\n{article_info}")

        # 7. Try accessing the PDF stamp URL pattern
        # IEEE common pattern: /stampPDF/getPDF.jsp?tp=&arnumber=XXXXX
        pdf_test = await page.evaluate("""() => {
            const arnumber = '594865';
            // Try known IEEE PDF URL patterns
            return {
                stampPDF: `/stampPDF/getPDF.jsp?tp=&arnumber=${arnumber}`,
                ielPDF: `/iel7/${arnumber}/${arnumber}.pdf`,
            };
        }""")
        print(f"\n=== CONSTRUCTED PDF URLs ===\n{pdf_test}")

        await page.close()
        print("\nDone.")

asyncio.run(main())
