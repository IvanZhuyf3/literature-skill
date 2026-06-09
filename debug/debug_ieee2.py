"""
CDP 探测脚本 — IEEE stamp.jsp 中间页行为
目标: 看 stamp.jsp 是直接返回 PDF 还是嵌入/重定向
"""
import asyncio
from playwright.async_api import async_playwright

STAMP_URL = "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=594865"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = await context.new_page()

        print(f"Navigating to stamp.jsp ...")
        resp = await page.goto(STAMP_URL, wait_until="domcontentloaded", timeout=60000)
        print(f"Status: {resp.status if resp else 'None'}")
        print(f"Final URL: {page.url}")

        await asyncio.sleep(5)

        # Check if this is a PDF page or HTML wrapper
        content_type = await page.evaluate("""() => {
            // Check if there's an embed/iframe/object for PDF
            const embed = document.querySelector('embed');
            const iframe = document.querySelector('iframe');
            const obj = document.querySelector('object');
            
            // Check page content type hint
            const body = document.body ? document.body.innerHTML.substring(0, 500) : 'no body';
            
            return {
                hasEmbed: !!embed,
                embedSrc: embed ? embed.src : null,
                embedType: embed ? embed.type : null,
                hasIframe: !!iframe,
                iframeSrc: iframe ? iframe.src : null,
                hasObject: !!obj,
                objectData: obj ? obj.data : null,
                bodyPreview: body.substring(0, 300),
            };
        }""")
        print(f"\n=== PAGE CONTENT ===")
        for k, v in content_type.items():
            print(f"  {k}: {v}")

        # Check URL after any redirects
        print(f"\n=== FINAL URL AFTER LOAD ===\n{page.url}")

        # Try fetch on the stamp URL to see what it returns
        fetch_test = await page.evaluate("""async () => {
            try {
                const resp = await fetch('/stamp/stamp.jsp?tp=&arnumber=594865');
                const contentType = resp.headers.get('content-type');
                const status = resp.status;
                const url = resp.url;
                
                if (contentType && contentType.includes('pdf')) {
                    const buf = await resp.arrayBuffer();
                    const bytes = new Uint8Array(buf);
                    const header = String.fromCharCode(...bytes.subarray(0, 5));
                    return { status, contentType, url, size: buf.byteLength, header };
                } else {
                    const text = await resp.text();
                    return { status, contentType, url, textPreview: text.substring(0, 300) };
                }
            } catch(e) {
                return { error: e.message };
            }
        }""")
        print(f"\n=== FETCH TEST ===")
        for k, v in fetch_test.items():
            print(f"  {k}: {str(v)[:200]}")

        await page.close()
        print("\nDone.")

asyncio.run(main())
