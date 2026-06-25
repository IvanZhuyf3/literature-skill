"""debug/debug_aacr2.py — 模拟 cookie_download 路径验证 AACR PDF 可下载性

验证 /article-pdf/... URL 经 requests (带 session cookies) 是否返回真实 PDF。
requests 会跟随 302 重定向到 silverchair-cdn，不受 CORS 限制。
"""

import asyncio
import requests
from urllib.parse import urlparse
from playwright.async_api import async_playwright

PAGE_URL = "https://aacrjournals.org/cancerrescommun/article/3/10/2195/729886/Sigma1-Regulates-Lipid-Droplet-Mediated-Redox"
PDF_URL = "https://aacrjournals.org/cancerrescommun/article-pdf/3/10/2195/3378821/crc-22-0371.pdf"
CDP = "http://127.0.0.1:19222"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP)
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        await page.goto(PAGE_URL, wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=20000)
        except Exception:
            pass

        cookies = await ctx.cookies()
        await page.close()

    # ---- Simulate cookie_download ----
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(
            cookie["name"], cookie["value"],
            domain=cookie.get("domain", ""), path=cookie.get("path", "/"),
        )
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/147.0.0.0 Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": PAGE_URL,
    }
    print(f"\nGET {PDF_URL}")
    r = session.get(PDF_URL, headers=headers, stream=True, timeout=120, allow_redirects=True)
    print(f"  final URL: {r.url}")
    print(f"  status: {r.status_code}")
    print(f"  content-type: {r.headers.get('Content-Type')}")
    print(f"  content-length: {r.headers.get('Content-Length')}")
    print(f"  redirect history: {[ (h.status_code, h.url) for h in r.history]}")

    # Read first 4 bytes + total
    chunks = []
    total = 0
    for chunk in r.iter_content(chunk_size=65536):
        chunks.append(chunk)
        total += len(chunk)
        if total > 200000:
            break
    data = b"".join(chunks)
    print(f"  bytes read: {total}")
    print(f"  prefix: {data[:4]}")
    print(f"  is PDF: {data[:4] == b'%PDF'}")
    print(f"  has %%EOF in read portion: {b'%%EOF' in data}")


asyncio.run(main())
