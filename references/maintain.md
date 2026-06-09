# Paper-at-Home — 维护指南

当现有 publisher 下载失败或需要添加新 publisher 时，按本流程操作。

## 流程 A：修复现有 Publisher

触发条件：下载报告显示某个 publisher 的论文失败。

### 1. 复现问题

```bash
python main.py "<失败URL>" --no-warmup --debug
```

观察日志，确定失败阶段：
- `navigate_failed` → 导航问题，检查页面加载
- `access_denied` → PDF 链接选择器失效，检查 DOM
- `no_download_url` → 下载按钮选择器失效
- `resolve_failed` → 重定向链变化
- `download_failed` → fetch() 或打印失败

### 2. 用 CDP 探测页面

**必须用 Playwright CDP 探测，不能只用 Chrome DevTools 手动看。** 原因：
- 手动浏览时页面结构和 CDP 连接时可能不同（bot detection 会改变 DOM）
- 需要确认在 CDP session 下选择器是否有效
- fetch() 在页面上下文中的行为和浏览器地址栏不同

写一个 `debug/debug_<publisher>.py` 脚本，用 CDP 连接真实 Chromium 探测：

> **查找已有探测脚本：** `debug/` 目录中的脚本按版本号递增（`debug_elife.py` → `debug_elife2.py` → `debug_elife3.py`），版本号越大越接近最终结论。需要复用时从最大版本号开始看。

```python
"""debug_<publisher>.py — 用 CDP 探测页面结构"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = await ctx.new_page()
        
        await page.goto("URL", wait_until="domcontentloaded", timeout=60000)
        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except:
            pass
        
        print(f"Final URL: {page.url}")
        
        # 1. 检查所有 PDF/download 相关链接
        links = await page.evaluate("""() => {
            const all = document.querySelectorAll('a[href], button');
            return Array.from(all)
                .filter(a => /pdf|download|PDF|Download/i.test(
                    (a.href || '') + (a.innerText || '')))
                .map(a => ({
                    href: a.href || '',
                    text: (a.innerText || '').trim().substring(0, 60),
                    tag: a.tagName,
                    class: (a.className || '').substring(0, 80),
                    aria: a.getAttribute('aria-label') || '',
                }));
        }""")
        for i, l in enumerate(links):
            print(f"\n--- Link {i+1} ---")
            print(f"  tag:    {l['tag']}")
            print(f"  href:   {l['href']}")
            print(f"  text:   {l['text']}")
            print(f"  class:  {l['class']}")
            print(f"  aria:   {l['aria']}")
        
        # 2. 检查 citation meta 标签（metadata 提取用）
        metas = await page.evaluate("""() => {
            const tags = ['citation_title', 'citation_doi', 'citation_date'];
            const result = {};
            for (const tag of tags) {
                const el = document.querySelector(`meta[name="${tag}"]`);
                result[tag] = el ? el.content : '(not found)';
            }
            return result;
        }""")
        print(f"\nMetadata: {metas}")
        
        # 3. 测试 fetch() 是否能拿到 PDF
        # 找到第一个 /pdf/ 或 /pdfdirect/ 链接试试
        pdf_href = await page.evaluate("""() => {
            const links = document.querySelectorAll('a[href]');
            for (const a of links) {
                if (/\\/pdf/i.test(a.href) && !/epdf/i.test(a.href)) {
                    return a.href;
                }
            }
            return null;
        }""")
        if pdf_href:
            print(f"\nTesting fetch() on: {pdf_href}")
            result = await page.evaluate("""async (url) => {
                const r = await fetch(url);
                const buf = await r.arrayBuffer();
                const prefix = Array.from(new Uint8Array(buf.slice(0, 4)));
                return { status: r.status, size: buf.byteLength, prefix, 
                         contentType: r.headers.get('content-type') };
            }""", pdf_href)
            is_pdf = bytes(result['prefix']) == b'%PDF'
            print(f"  Status: {result['status']}, Size: {result['size']}, "
                  f"PDF: {is_pdf}, Type: {result['contentType']}")
        
        await page.close()

asyncio.run(main())
```

### 3. 修复

阅读 `ARCHITECTURE.md` 中对应 publisher 的章节，了解当前实现。
阅读 `publisher/<name>.py` 的 docstring 了解选择器和特殊处理。

修改对应的 `publisher/<name>.py`。

### 4. 测试

```bash
python main.py "<失败URL>" --no-warmup --debug
```

确认文件下载成功、大小合理（>100KB）、是有效 PDF（`%PDF` 头）。

### 5. 记录问题

在 `error_log.md` 中记录排查过程和解决方案（格式：`E-<PUBLISHER>-<编号>: <现象>` → 排查过程 → 解决 → 教训）。

---

## 流程 B：添加新 Publisher

触发条件：URL 匹配不到任何已知 publisher，或用户要求支持新出版商。

### 1. 用 CDP 探测页面（必须）

**这一步不能跳过。** 出版商都有 bot detection，手动浏览器看到的页面和 CDP 连接时可能不同。所有探索必须通过 Playwright CDP 做真实 Chrome 里。

写 `debug_<publisher>.py`（模板见上方流程 A.2），重点探测：

| 要回答的问题 | 怎么探测 |
|-------------|---------|
| 页面最终 URL 是什么？ | `page.url` — 可能被重定向 |
| PDF 下载按钮在哪？ | 遍历所有 `<a>` 标签，过滤 pdf/download 关键词 |
| 哪个链接是真正的 PDF？ | 对候选链接逐一 `fetch()` 测试，看返回的 prefix 是否是 `%PDF` |
| metadata 在哪？ | 检查 `citation_*` meta 标签；如果没有，检查 `<title>` 和 URL |
| 是否需要跨页？ | 检查下载链接和 metadata 是否在同一页面上（如 Wiley：metadata 在文章页，PDF 在 epdf 页） |
| fetch() 是否能直接拿到 PDF？ | 在页面上下文里 `fetch()` 候选 URL，看返回的是 PDF 还是 HTML |

**关键经验：**
- `/doi/pdf/` 经常返回 HTML wrapper，不是原始 PDF（AAAS 例外）
- `/doi/pdfdirect/` 或带 `?download=true` 的 URL 更可能是真正的 PDF
- 某些出版商（如 Wiley）有多个页面变体（文章页 vs epdf 查看器），下载链接和 metadata 可能在不同页面上
- 先找到所有候选链接，逐个 fetch() 测试，不要猜

### 2. 判断下载类型

根据 CDP 探测结果判断：

| 类型 | 特征 | 实现方式 |
|------|------|---------|
| **简单型** | fetch(链接) 直接返回 `%PDF` | 只需 `find_download_element()` + `fetch()` |
| **多页型** | metadata 和下载链接在不同页面 | 先去 metadata 页，`resolve_pdf_url()` 跳到下载页 |
| **跨域 CDN 型** | PDF 在不同域名上（CORS 问题） | `resolve_pdf_url()` + `fetch_from_pdf_page = True` |
| **PDF 查看器劫持型** | Chrome PDF 查看器拦截所有事件 | `use_click_download = True` + pyautogui Ctrl+P |
| **浏览器自动下载型** | 点击按钮后浏览器直接下载到默认目录 | `use_click_download = True` + CDP 目录监控 |

### 3. 创建适配器

在 `publisher/` 下创建新文件，模板：

```python
"""Publisher Name 适配器。

URL 模式: example.com
下载流程: [简单型/多页型/跨域型/打印型]
[重要发现：哪些链接是真正的 PDF，哪些是 HTML wrapper]
"""

import logging
import re
import time
from typing import Optional, Any

from .base import PublisherAdapter, PaperInfo

logger = logging.getLogger(__name__)


class NewPublisherAdapter(PublisherAdapter):
    # resolve 后留在 PDF 页面做 fetch（跨域时需要）
    fetch_from_pdf_page = False
    # 不走 fetch()，用点击/打印下载
    use_click_download = False

    @property
    def name(self) -> str:
        return "publisher_key"

    def detect(self, url: str) -> bool:
        return "example.com" in url.lower()

    def navigate_to_paper(self, page, url: str) -> bool:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            # 可选：等特定元素出现
            # page.wait_for_selector('CSS_SELECTOR', timeout=15000)
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception:
                pass
            return True
        except Exception as e:
            logger.error(f"Failed to load page: {e}")
            return False

    def find_download_element(self, page) -> Optional[Any]:
        # 选择器从 CDP 探测步骤中获得
        try:
            el = page.query_selector('a.download-pdf')
            if el:
                logger.info(f"Found download element")
                return el
        except Exception:
            pass
        return None

    def check_access(self, page) -> bool:
        """默认：有下载按钮 = 有权限。"""
        return self.find_download_element(page) is not None

    def get_paper_metadata(self, page) -> PaperInfo:
        info = PaperInfo(publisher=self.name)
        try:
            info.title = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_title"]');
                return el ? el.content : '';
            }""") or ""
            info.doi = page.evaluate("""() => {
                const el = document.querySelector('meta[name="citation_doi"]');
                return el ? el.content : '';
            }""") or ""
            info.url = page.url
        except Exception as e:
            logger.warning(f"Metadata extraction failed: {e}")
        return info
```

### 4. 注册

1. `main.py` — 添加 import + `get_adapter()` 字典中添加映射
2. `url_parser.py` — `PUBLISHER_PATTERNS` 字典中添加 URL 匹配模式

### 5. 用真实 Chrome 测试

```bash
python main.py "<新publisher的论文URL>" --no-warmup --debug
```

确认：
- 出版商正确识别
- 页面加载成功
- Metadata 提取完整（标题、DOI）
- PDF 下载成功（>100KB，`%PDF` 头）
- 文件按论文标题重命名

### 6. 清理调试脚本

调试脚本已自动放在 `debug/` 目录中（`debug/debug_<publisher>.py`），未来修复同一 publisher 时可复用。

### 7. 更新文档

- 在 `publisher/<name>.py` 顶部 docstring 中记录下载流程和注意事项
- 在 `ARCHITECTURE.md` 的出版商详解章节添加新条目
- 在 `SKILL.md` 的支持出版商表格添加新行
- 在 `error_log.md` 中记录接入过程中遇到的问题和解决方案（编号：`E-<PUBLISHER>-<编号>`）

---

## 调试技巧

### CDP 探测（首选）

写 `debug_<publisher>.py` 脚本通过 CDP 连接真实 Chromium。这是唯一可靠的方式，
因为 bot detection 会改变页面结构。

### Chrome DevTools（辅助）

在 Chromium 中手动打开论文页面 → F12 → Console：
```javascript
// 测试选择器
document.querySelectorAll('a[href*="/doi/pdf/"]')
// 测试 meta 标签
document.querySelector('meta[name="citation_title"]')?.content
// 测试 fetch
fetch('/doi/pdf/10.xxx').then(r => r.arrayBuffer().then(b => console.log(Array.from(new Uint8Array(b.slice(0,4))))))
```

注意：手动 DevTools 的结果仅作参考，CDP 探测才是权威。

### 常见失败原因

| 症状 | 原因 | 解决 |
|------|------|------|
| `networkidle` 超时 | 页面分析脚本太多 | 非关键，降低 timeout |
| PDF 链接找不到 | DOM 结构变化 或 bot detection 改变了页面 | 用 CDP 探测确认 |
| fetch() 返回 HTML | `/doi/pdf/` 返回 HTML wrapper，不是真正的 PDF | 找 pdfdirect 或带 `?download=true` 的链接 |
| fetch() 403 | CORS 或 TLS 指纹 | 改用页面上下文 fetch 或导航到 PDF 页面再做 fetch |
| metadata 为空 | epdf 查看器页面没有 citation meta 标签 | 先去文章信息页提取 metadata，再跳到下载页 |
| 文件太小 (<100KB) | 保存了 HTML wrapper | 检查下载方式 |
