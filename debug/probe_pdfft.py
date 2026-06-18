"""Probe pdfft redirect flow for this Elsevier paper."""
import logging, sys, time, os
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

# Directly navigate to the pdfft URL
pdfft_url = "https://www.sciencedirect.com/science/article/pii/S0006349505727065/pdfft?md5=9d4c3d045ad60d7193a287845b5a4c5d&pid=1-s2.0-S0006349505727065-main.pdf"
print(f"Navigating to pdfft: {pdfft_url}")
page.goto(pdfft_url, wait_until="domcontentloaded", timeout=60000)

# Wait and track redirects
for i in range(25):
    time.sleep(1)
    try:
        cur = page.evaluate("() => window.location.href")
        print(f"  [{i+1}s] URL: {cur[:120]}")
        
        # Check if it's a PDF URL
        if ".pdf" in cur.lower() and "sciencedirectassets" in cur:
            print(f"  -> PDF URL detected! Full: {cur}")
            
            # Try to download via fetch
            result = page.evaluate("""async (url) => {
                try {
                    const resp = await fetch(url);
                    if (!resp.ok) return {error: 'HTTP ' + resp.status};
                    const ct = resp.headers.get('content-type') || '';
                    if (!ct.includes('pdf')) return {error: 'Not PDF: ' + ct};
                    const buf = await resp.arrayBuffer();
                    return {size: buf.byteLength, data: Array.from(new Uint8Array(buf))};
                } catch(e) { return {error: e.message}; }
            }""", cur)
            
            print(f"  Fetch result: {result.get('error', 'OK')}")
            if result.get('size', 0) > 0:
                print(f"  PDF size: {result['size']} bytes")
                
                # Save it
                save_dir = r"C:\Users\Ivanz\OneDrive\Hermes_workspace\Literature_skill\people\data"
                filepath = os.path.join(save_dir, "biophysj_2005_pdfft.pdf")
                with open(filepath, "wb") as f:
                    f.write(bytes(result["data"]))
                print(f"  Saved to: {filepath}")
            break
    except Exception as e:
        print(f"  [{i+1}s] Error: {e}")
        continue

# Save screenshot
page.screenshot(path=r"C:\Users\Ivanz\OneDrive\Hermes_workspace\Literature_skill\people\data\elsevier_pdfft.png")
print("Screenshot saved.")

helper.disconnect()
