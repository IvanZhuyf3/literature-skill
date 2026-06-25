# Sci-Hub 多镜像配置

`scihub_cdp.py` 的多镜像轮转 + captcha 熔断 + 节流机制。

详细架构说明见 `references/architecture.md` 的 "Sci-Hub 多镜像 + 熔断机制" 章节。

## config.yaml 配置

```yaml
scihub:
  mirrors:
    - "https://sci-hub.ru"
    - "https://sci-hub.st"
    - "https://sci-hub.su"
    - "https://sci-hub.box"
    - "https://sci-hub.red"
  max_year: 2021
```

## 可用镜像（2026-06 验证）

| 镜像 | 状态 | 备注 |
|------|------|------|
| sci-hub.ru | ✅ | 俄语 not-found 页面 |
| sci-hub.st | ✅ | 英语 not-found 页面 |
| sci-hub.su | ✅ | |
| sci-hub.box | ✅ | |
| sci-hub.red | ✅ | |
| sci-hub.al | ❌ | 用户验证不可用，已剔除 |
| sci-hub.mk | ❌ | 用户验证不可用，已剔除 |
| sci-hub.ee | ❌ | 页面结构不同，已剔除 |

## 四层保护机制

1. **镜像轮转**：5 镜像 round-robin，captcha 拉黑当前镜像自动换下一个
2. **节流 + 随机延迟**：请求间隔 ≥5s，页面加载后等 5+rand(0,2)s，PDF 存后等 5+rand(0,2)s
3. **Captcha 检测**：`_CAPTCHA_PATTERNS` 关键词匹配 → 拉黑镜像
4. **Not-found 检测**：`_NOT_FOUND_PATTERNS` → `_NOT_FOUND` sentinel → 跳过整个 DOI（所有镜像同库）

## 关键设计决策

### Captcha vs Not-found 必须区分

- **Captcha**（`return None`）→ 外层试下一个镜像
- **Not-found**（`return _NOT_FOUND`）→ 外层放弃整个 DOI
- 搞混了 = 浪费请求额度（not-found 去试 5 个镜像）或漏掉可下载的论文（captcha 当 not-found）

### Not-found 模式需持续维护

不同镜像的 not-found 文案不同：
- `.ru`：`"i do not have any papers matching your request"`
- `.st`：`"article is not available through sci-hub"`
- 遇到新表述需加入 `_NOT_FOUND_PATTERNS`

### 多方法 PDF 下载链（`_download_pdf()`）

PDF storage URL 和 Sci-Hub 页面通常不同域（如页面在 `sci-hub.ru`，PDF 在 `sci-hub.cat`）。不同镜像、不同时刻 CORS 行为不同，没有单一可靠方法。`_download_pdf()` 按序尝试 4 种方法，第一个成功即返回：

| # | 方法 | 原理 | 何时有效 |
|---|------|------|---------|
| 1 | `page.request.get()` ×2 | Playwright API context，共享 cookie，不走浏览器 CORS | 大多数情况（实测 3/3 一次命中） |
| 2 | `page.evaluate(fetch())` | 页面内浏览器 fetch（base64 传回） | 同源 storage 或 CORS 恰好放开时 |
| 3 | `requests.get()` + cookies | 纯 HTTP，从浏览器提取 cookie，完全绕过 CORS | CDN 封了浏览器 IP、request API 超时时 |
| 4 | `expect_download()` | 导航到 PDF URL，浏览器原生下载触发 | 前三种全挂时 |

**历史 bug**：之前只有 `page.evaluate(fetch())` 一种方法，跨域请求被浏览器拦截报 `TypeError: Failed to fetch`，导致 ~20 篇 Sci-Hub 有的论文下不到。加了 Method 1 (`page.request.get()`) 后问题消失。

### Playwright Chromium（非 Edge CDP）

Sci-Hub 用 Playwright 自带 Chromium（`pw.chromium.launch(headless=False)`），不用 Edge CDP。原因：Edge 对某些镜像的 PDF storage URL 有 CORS 限制，`page.evaluate(fetch())` 报 `TypeError: Failed to fetch`。

持久浏览器（`_ensure_browser()`）：模块级 `_browser`/`_pw` 变量，首次调用 launch，后续复用。`finally` 只关 page 不关 browser。

### 批量下载建议

300+ 篇的 collection 不要裸跑 `lit quick`。即使有 5 镜像轮转 + 节流，密集访问仍可能逐个触发 captcha。建议：
- `--limit 50` 分批
- 或直接走 `lit attach`（出版商 adapter 不碰 Sci-Hub）
