"""debug/debug_aacr.py — 用 CDP 探测 AACR (aacrjournals.org) 页面结构

探测目标：
  1. 页面最终 URL / 重定向
  2. PDF 下载按钮位置与 href
  3. citation_* meta 标签
  4. 对候选 PDF 链接逐一 fetch() 测试是否返回 %PDF
"""

import asyncio
from playwright.async_api import async_playwright

URL = "https://aacrjournals.org/cancerrescommun/article/3/10/2195/729886/Sigma1-Regulates-Lipid-Droplet-Mediated-Redox"
CDP = "http://127.0.0.1:19222"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP)
        ctx = browser.contexts[0]
        page = await ctx.new_page()

        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except Exception:
            pass

        print(f"Final URL: {page.url}")
        print(f"Title: {await page.title()}")

        # 1. 所有 PDF/download 相关链接
        links = await page.evaluate("""() => {
            const all = document.querySelectorAll('a[href], button');
            return Array.from(all)
                .filter(a => /pdf|download|full|supplement/i.test(
                    (a.href || '') + (a.innerText || '') + (a.getAttribute('aria-label') || '')))
                .map(a => ({
                    href: a.href || '',
                    text: (a.innerText || '').trim().substring(0, 60),
                    tag: a.tagName,
                    class: (a.className || '').toString().substring(0, 80),
                    aria: a.getAttribute('aria-label') || '',
                }));
        }""")
        print("\n=== PDF/download/full links ===")
        for i, l in enumerate(links):
            print(f"\n--- Link {i+1} ---")
            print(f"  tag:   {l['tag']}")
            print(f"  href:  {l['href']}")
            print(f"  text:  {l['text']}")
            print(f"  class: {l['class']}")
            print(f"  aria:  {l['aria']}")

        # 2. citation meta 标签
        metas = await page.evaluate("""() => {
            const tags = ['citation_title', 'citation_doi', 'citation_date',
                          'citation_pdf_url', 'citation_full_html_url'];
            const result = {};
            for (const tag of tags) {
                const els = document.querySelectorAll(`meta[name="${tag}"]`);
                result[tag] = Array.from(els).map(e => e.content);
            }
            return result;
        }""")
        print("\n=== Metadata ===")
        for k, v in metas.items():
            print(f"  {k}: {v}")

        # 3. 对候选 PDF 链接逐一 fetch() 测试
        candidates = []
        for l in links:
            href = l.get("href", "")
            if href and ("/pdf" in href.lower() or "download" in href.lower()
                         or href.lower().endswith(".pdf")):
                candidates.append(href)
        # 也加上 citation_pdf_url
        cpu = metas.get("citation_pdf_url") or []
        for u in cpu:
            candidates.append(u)

        seen = set()
        unique_candidates = []
        for c in candidates:
            if c and c not in seen:
                unique_candidates.append(c)
                seen.add(c)

        print("\n=== fetch() test on candidates ===")
        for c in unique_candidates:
            try:
                result = await page.evaluate("""async (url) => {
                    try {
                        const r = await fetch(url, {credentials: 'include'});
                        const buf = await r.arrayBuffer();
                        const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
                        return { status: r.status, size: buf.byteLength, prefix,
                                 contentType: r.headers.get('content-type') };
                    } catch(e) { return { error: String(e) }; }
                }""", c)
                prefix_bytes = bytes(result.get("prefix", []))
                is_pdf = prefix_bytes == b"%PDF"
                print(f"\n  URL: {c}")
                print(f"    status={result.get('status')} size={result.get('size')} "
                      f"PDF={is_pdf} type={result.get('contentType')} err={result.get('error')}")
            except Exception as e:
                print(f"\n  URL: {c}\n    FETCH ERROR: {e}")

        await page.close()


asyncio.run(main())
