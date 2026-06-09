"""
CDP 探测脚本 — IEEE getPDF.jsp 实际 PDF 获取
"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        
        # 先去文章页建立 session
        page = await context.new_page()
        print("Loading article page first...")
        await page.goto("https://ieeexplore.ieee.org/document/594865", wait_until="domcontentloaded", timeout=60000)
        await asyncio.sleep(5)
        print(f"Article page loaded: {page.url}")

        # 试试 fetch getPDF.jsp
        fetch_result = await page.evaluate("""async () => {
            try {
                const url = '/stampPDF/getPDF.jsp?tp=&arnumber=594865';
                const resp = await fetch(url);
                const contentType = resp.headers.get('content-type');
                const status = resp.status;
                const finalUrl = resp.url;
                
                if (contentType && contentType.includes('pdf')) {
                    const buf = await resp.arrayBuffer();
                    const bytes = new Uint8Array(buf);
                    const header = [];
                    for (let i = 0; i < Math.min(10, bytes.length); i++) header.push(bytes[i]);
                    return { status, contentType, url: finalUrl, size: buf.byteLength, header };
                } else {
                    const text = await resp.text();
                    return { status, contentType, url: finalUrl, textPreview: text.substring(0, 500) };
                }
            } catch(e) {
                return { error: e.message };
            }
        }""")
        print(f"\n=== FETCH getPDF.jsp ===")
        for k, v in fetch_result.items():
            print(f"  {k}: {str(v)[:300]}")

        # 也试导航到 getPDF.jsp 看最终 URL
        page2 = await context.new_page()
        print("\nNavigating to getPDF.jsp...")
        resp2 = await page2.goto("https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=594865", wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(3)
        print(f"Status: {resp2.status if resp2 else 'None'}")
        print(f"Final URL: {page2.url}")
        
        # Check if this is PDF content
        is_pdf = await page2.evaluate("""() => {
            const body = document.body ? document.body.innerHTML.substring(0, 200) : 'no body';
            return { bodyPreview: body, contentType: document.contentType };
        }""")
        print(f"Content: {is_pdf}")

        await page.close()
        await page2.close()
        print("\nDone.")

asyncio.run(main())
