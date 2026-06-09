# Paper-at-Home — 项目知识文档

## 项目概述

学术论文自动下载工具。通过 Playwright CDP 连接 Chromium 浏览器（可手动启动或自动启动），从 DOM 提取 PDF 链接，用页面上下文 `fetch()` 下载原始 PDF 字节，绕过出版商反爬检测。

## 架构

```
Chromium 启动（两种方式，main.py 自动处理）:
  A) 用户手动启动 (--remote-debugging-port=9222，已登录机构账号) ← 推荐
  B) main.py 自动启动 (临时 profile，无登录状态，访问需订阅的论文会失败)
    ↓
main.py → ChromiumHelper.connect() → Playwright connect_over_cdp()
    │  连接失败时自动 fallback: launch_browser() + 轮询重连 (最多 15s)
    ↓
url_parser: 解析 URL/DOI → 识别出版商
    ↓
publisher/acs.py, publisher/optica.py, publisher/aaas.py, publisher/npg.py, publisher/springer.py: 从 DOM 提取 PDF 链接
    ↓
download_monitor.py: page.evaluate(fetch()) 下载 PDF（绕过 PDF 查看器 + TLS 检测）
    ↓
按论文标题重命名文件
```

## 文件职责

| 文件 | 职责 |
|------|------|
| `main.py` | CLI 入口，完整工作流编排 |
| `chromium_helper.py` | Chromium 启动/CDP 连接/暖场页面 |
| `click_engine.py` | 坐标转换 + pyautogui 人类式点击（备用，当前未使用） |
| `download_monitor.py` | `page.evaluate(fetch())` PDF 下载（主方案） + 目录监控 fallback |
| `rate_limiter.py` | 延迟控制（60-180s）、模拟阅读、session 限制 |
| `url_parser.py` | URL/DOI 解析、出版商自动识别 |
| `publisher/base.py` | 适配器抽象基类 (PublisherAdapter) |
| `publisher/acs.py` | ACS Publications 适配器 |
| `publisher/optica.py` | Optica Publishing Group 适配器 |
| `publisher/aaas.py` | AAAS (Science) 适配器 |
| `publisher/npg.py` | Nature Publishing Group 适配器 |
| `publisher/springer.py` | Springer (link.springer.com) 适配器 |
| `publisher/aip.py` | AIP (Silverchair 平台) 适配器 |
| `publisher/elsevier.py` | Elsevier ScienceDirect 适配器 (Ctrl+P 打印下载) |
| `publisher/pnas.py` | PNAS (Proceedings of the National Academy of Sciences) 适配器 |
| `publisher/wiley.py` | Wiley Online Library 适配器 (epdf → pdfdirect) |
| `publisher/aps.py` | APS (Physical Review系列) 适配器 |
| `publisher/tandf.py` | Taylor & Francis (tandfonline.com) 适配器 |
| `publisher/rsc.py` | RSC (Royal Society of Chemistry) 适配器 |
| `publisher/iop.py` | IOP (Institute of Physics, IOPscience) 适配器 |
| `publisher/annualreviews.py` | Annual Reviews 适配器 |
| `publisher/mdpi.py` | MDPI 适配器 |
| `publisher/frontiers.py` | Frontiers 适配器 |
| `publisher/elife.py` | eLife 适配器 |
| `publisher/royalsociety.py` | Royal Society 适配器 (Silverchair CDN 跨域) |
| `publisher/bmj.py` | BMJ 适配器 |
| `publisher/ieee.py` | IEEE Xplore 适配器 (getPDF.jsp 构造) |
| `publisher/spie.py` | SPIE Digital Library 适配器 |
| `config.yaml` | 所有可调参数 |

## 核心下载机制：`page.evaluate(fetch())`

**为什么有效：**
- 在页面上下文中执行，使用 Chrome 原生网络栈（TLS + Cookie 全真实）
- PDF 查看器扩展不拦截 `fetch()` 请求
- 返回原始 PDF 字节，不走 DOM

**为什么其他方案失败：**

| 方案 | 失败原因 |
|------|---------|
| pyautogui 点击 PDF 链接 | `target="_blank"` 被 Chrome 弹窗拦截 |
| `requests` + cookie | Python TLS 指纹 → 403 |
| `page.goto()` + `response.body()` | Chrome PDF 查看器劫持响应，返回查看器 HTML |
| `route.fetch()` | TLS 指纹不同于真实导航 → 403 |
| CDP `Network.getResponseBody` | 同样被 PDF 查看器拦截 |

## 出版商适配器详解

### ACS Publications (`publisher/acs.py`)

**URL 模式：** `pubs.acs.org`

**下载流程（简单型）：**
1. 导航到论文页面（`/doi/10.1021/...`）
2. DOM 查找 `a[title='PDF']` → 提取 href（`/doi/pdf/10.1021/...`）
3. `page.evaluate(fetch(pdf_url))` → 直接返回 PDF 字节
4. 保存 + 重命名

**选择器优先级：**
1. `a[title='PDF']` — 顶栏 PDF 按钮
2. `a[href*='/doi/pdf/']` — URL 包含 /doi/pdf/ 的链接
3. `a:has-text("PDF")` — 文本匹配兜底

**注意事项：**
- ACS 页面 `networkidle` 经常超时（太多分析脚本），已做非关键处理
- 相对 URL 需用 `urljoin` 转绝对路径（base.py 的 `find_download_url` 已处理）

### Optica Publishing Group (`publisher/optica.py`)

**URL 模式：** `opg.optica.org`, `optica.org`, `osapublishing.org`

**下载流程（重定向解析型）：**
1. 导航到论文页面（`/ol/fulltext.cfm?uri=ol-51-9-2708`）
2. DOM 查找 `a:has-text("Get PDF")` → 提取 href（`viewmedia.cfm?uri=...&seq=0`）
3. **重定向解析**（`resolve_pdf_url` 方法）：
   - 导航到 viewmedia.cfm → Chrome 完成 JS 挑战（`/checkjs.cfm`）
   - 重定向到 `view_article.cfm?pdfKey=UUID_ID`
   - 从 URL 提取 pdfKey
   - **构造直链**：`/directpdfaccess/{pdfKey}/{doi}.pdf?da=1&id={ID}&seq=0&mobile=no`
4. 回到文章页（维持 session）
5. `page.evaluate(fetch(direct_url))` → 返回 PDF 字节
6. 保存 + 重命名

**为什么需要构造直链：**
- `view_article.cfm` → `directpdfaccess` 的跳转走 Chrome PDF 查看器内部机制
- `page.url` 看不到最终 URL，始终停留在 `view_article.cfm`
- 但 pdfKey 可以从中间页 URL 提取，直接拼出直链

**URL 构造模式：**
```
pdfKey = 0e615e15-14a7-4588-a209b80271ffca8a_591237
doi    = ol-51-9-2708
id     = 591237  (pdfKey 下划线后的数字)

→ https://opg.optica.org/directpdfaccess/{pdfKey}/{doi}.pdf?da=1&id={id}&seq=0&mobile=no
```

**注意事项：**
- 必须先导航到 viewmedia.cfm 完成 JS 挑战，否则 fetch() 会拿到 202 挑战页
- `seq=0` 是完整论文 PDF，`figure=` 开头的是图表 PDF，需过滤

### AAAS / Science / SPJ (`publisher/aaas.py`)

**URL 模式：** `science.org`（含 `spj.science.org`）

**覆盖期刊：** Science, Science Advances (OA), Science Translational Medicine 等 AAAS 主刊；以及 Science Partner Journals (SPJ) 系列

**下载流程（简单型）：**
1. 导航到论文页面（`/doi/10.1126/...`）
2. DOM 查找 `a[href*="/doi/pdf/"][href*="download=true"]` → 提取 href
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- AAAS 有两个 PDF 链接：折叠菜单里的（`?download=true`）和页面底部的（无 download 参数）
- 不检查 `is_visible()`，折叠菜单里的链接功能正常
- `check_access()` 用 PDF 链接存在性判断，不用文本匹配（避免 DOI 中的 "403" 误报）
- 页面加载较慢，timeout 设为 60s

### NPG / Nature Publishing Group (`publisher/npg.py`)

**URL 模式：** `nature.com`

**覆盖期刊：** Nature, Nature Photonics, Nature Physics 等 Nature 系列期刊

**下载流程（简单型）：**
1. 导航到论文页面（`/articles/s41566-026-01891-6`）
2. DOM 查找 `a.u-button--primary[href$=".pdf"]` → 提取 href（`/articles/...pdf`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- NPG 页面有多个 PDF 链接（主文 + 补充材料），需排除 `static-content.springer.com` 的补充材料
- 主文 PDF 是 `/articles/<id>.pdf`，补充材料在 `static-content.springer.com`
- `Download PDF` 按钮可能 visible=False（侧边栏折叠），但链接功能正常

### Springer (`publisher/springer.py`)

**URL 模式：** `link.springer.com`

**注意：** Springer 和 NPG (nature.com) 同属 Springer Nature 集团，但网站架构完全不同，分开处理。

**下载流程（简单型）：**
1. 导航到论文页面（`/article/10.1186/...`）
2. DOM 查找 `a[data-track-action="download pdf"]` → 提取 href（`/content/pdf/<doi>.pdf`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- Springer 用 `data-track-action="download pdf"` 精确标记下载按钮
- PDF 直链模式：`/content/pdf/<doi>.pdf`
- `check_access()` 用 PDF 链接存在性判断，不用文本匹配

### AIP / Silverchair (`publisher/aip.py`)

**URL 模式：** `pubs.aip.org`

**下载流程（跨域重定向型）：**
1. 导航到论文页面
2. DOM 查找 `a[href*="/article-pdf/"]` → 提取 href（`/aip/jcp/article-pdf/...`）
3. **resolve_pdf_url()**：`page.goto(pdf_url)` 跟随重定向到 `watermark02.silverchair.com/...?token=...`
4. **留在 PDF 页面**（`fetch_from_pdf_page = True`），因为 CDN 和文章页不同源（CORS）
5. `page.evaluate(fetch())` 从 PDF 页面上下文下载 → 返回 PDF 字节

**为什么需要特殊处理：**
- AIP 用 Silverchair 平台，PDF URL 重定向到 CDN（`watermark02.silverchair.com`）
- CDN URL 带签名 token，有时效性
- 从文章页 `fetch()` CDN URL 会因 CORS 被浏览器拦截
- 必须在 PDF 页面（CDN 域）的上下文中做 fetch

### Elsevier / ScienceDirect (`publisher/elsevier.py`)

**URL 模式：** `sciencedirect.com`

**下载流程（Ctrl+P 打印型）：**
1. 导航到论文页面（`/science/article/pii/...`）
2. DOM 查找 `a[aria-label*="PDF"]` 匹配当前 PII 的 `/pdfft` 链接
3. Playwright click + `expect_popup` 打开新 tab（Chrome PDF 查看器接管 `/pdfft`）
4. 在文章页获取窗口坐标 → pyautogui 点击标题栏激活 Chrome 窗口
5. pyautogui `Ctrl+P` → 3 秒 → Enter（确认打印对话框）→ 10 秒 → Enter（确认另存为对话框）
6. Foxit Reader Print to PDF 打印到 temp 目录
7. 按 mtime 检测新 PDF（比 `_print_start_time` 新的文件），等文件大小稳定
8. 重命名（带文件锁重试）
9. 关闭 PDF 查看 tab，清理

**为什么需要 Ctrl+P 打印：**
- Elsevier 的 `/pdfft` URL 被 Chrome 内置 PDF 查看器完全劫持
- `page.goto(pdfft)` → Chrome PDF 查看器接管，Playwright 事件全部被抑制
- `page.on("response")`、`page.on("request")` 都不触发
- PDF 查看器的"下载"按钮保存的是 HTML wrapper（不是原始 PDF）
- Ctrl+S 同样保存 HTML
- 唯一可行方案：Ctrl+P 打印为 PDF

**选择器优先级：**
1. `a[aria-label*="PDF"]` 匹配当前 PII + `/pdfft`
2. `a:has-text("View PDF")` 匹配当前 PII（fallback）

**特殊标记：**
- `use_click_download = True`：通知 main.py 不走 fetch() 流程
- `resolve_pdf_url()` 返回 `"__click_download__"`：触发 click_download 路径
- `_print_start_time`：Ctrl+P 前的时间戳，用于按 mtime 查找文件

**注意事项：**
- pyautogui 是 OS 级别的，必须先点击 Chrome 标题栏激活窗口再发快捷键
- `expect_popup` 能捕获 View PDF 的新 tab（`window.open` 不行）
- Foxit Reader 打印文件锁：rename 需要重试（最多 5 次 × 3 秒）
- 文件大小稳定检查：防止在 Foxit Writer 写入过程中误读不完整文件
- `get_or_create_page` 过滤 `pdf.sciencedirectassets` 页面（PDF 查看器冻结）
- `navigate_to_paper` 加 `wait_for_selector('a[aria-label*="PDF"]')` 确保 DOM 就绪

### PNAS (`publisher/pnas.py`)

**URL 模式：** `pnas.org`

**下载流程（简单型）：**
1. 导航到论文页面（`/doi/10.1073/pnas.XXXXXX`）
2. DOM 查找 `a[href*="/doi/pdf/"]` → 提取 href（`/doi/pdf/10.1073/pnas.XXXXXX?download=true`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- PNAS 使用 Silverchair 平台，PDF 链接模式与 AAAS 类似
- PDF URL 自带 `?download=true` 参数，浏览器直接触发下载
- `check_access()` 用 PDF 链接存在性判断

### Wiley Online Library (`publisher/wiley.py`)

**URL 模式：** `onlinelibrary.wiley.com`

**下载流程（epdf 解析型）：**
1. 导航到文章信息页（`/doi/10.1002/...`）— 提取 metadata（citation_* meta 标签）
2. `resolve_pdf_url()`：跳转到 epdf 查看器页面（`/doi/epdf/10.1002/...`）
3. DOM 查找 `a[href*="/doi/pdfdirect/"]` → 提取 pdfdirect 直链
4. 留在 epdf 页面做 `page.evaluate(fetch(pdfdirect_url))` → 返回 PDF 字节
5. 保存 + 按标题重命名

**为什么需要两步：**
- 文章信息页（`/doi/DOI`）有完整的 citation meta 标签，但 `/doi/pdf/` 链接返回 HTML 不是 PDF
- epdf 查看器页面有 `/doi/pdfdirect/DOI?download=true`（真正的 PDF），但没有 citation meta 标签
- 所以先去文章页拿 metadata，再跳 epdf 拿 PDF

**注意事项：**
- `fetch_from_pdf_page = True`：resolve 后留在 epdf 页面做 fetch（同域无 CORS 问题）
- pdfdirect URL 带 `?download=true` 参数
- Wiley 页面加载很慢，networkidle 经常超时（非关键）

### APS / Physical Review (`publisher/aps.py`)

**URL 模式：** `journals.aps.org`

**覆盖期刊：** Physical Review Letters (PRL), Physical Review A/B/C/D/E, Review of Modern Physics 等

**下载流程（简单型）：**
1. 导航到论文页面（`/prl/abstract/10.1103/...`）
2. DOM 查找 `a.sm-primary-button[href*="/pdf/"]` → 提取 href（`/prl/pdf/10.1103/...`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- 排除 `/supplemental/` 链接（补充材料 PDF）
- citation_* meta 标签完整，metadata 提取无特殊处理

### Taylor & Francis (`publisher/tandf.py`)

**URL 模式：** `tandfonline.com`

**下载流程（简单型）：**
1. 导航到论文页面（`/doi/full/10.1080/...`）
2. DOM 查找 `a.show-pdf[href*="/doi/pdf/"]` → 提取 href（`/doi/pdf/10.1080/...`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- T&F 没有 `citation_*` meta 标签，标题从 `<title>` 提取（去掉 "Full article: " 前缀和后缀）
- DOI 从 URL pathname 提取
- `/doi/epdf/` 是内嵌 PDF 查看器，`/doi/pdf/` 才是下载链接

### RSC / Royal Society of Chemistry (`publisher/rsc.py`)

**URL 模式：** `pubs.rsc.org`

**覆盖期刊：** Chemical Science, Chem. Commun., Dalton Trans., Nanoscale 等 RSC 期刊

**下载流程（简单型）：**
1. 导航到论文页面（`/content/articlelanding/2026/sc/d6sc01123c`）
2. DOM 查找 `a.btn--primary[href*="articlepdf"]` → 提取 href（`/content/articlepdf/2026/sc/d6sc01123c`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- RSC 甚至有 `citation_pdf_url` meta 标签直接指向 PDF URL
- `citation_date` 可能不存在，用 `citation_online_date` 兜底

### IOP / IOPscience (`publisher/iop.py`)

**URL 模式：** `iopscience.iop.org`

**覆盖期刊：** New Journal of Physics, Nanotechnology, Journal of Physics 系列, Biofabrication 等 IOP 期刊

**下载流程（简单型）：**
1. 导航到论文页面（`/article/10.1088/...`）
2. DOM 查找 `a.wd-jnl-art-pdf-button-main` → 提取 href（`/article/DOI/pdf`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- 有 `citation_pdf_url` meta 标签直接指向 PDF
- `citation_date` 可能不存在，用 `citation_online_date` 兜底

### Annual Reviews (`publisher/annualreviews.py`)

**URL 模式：** `annualreviews.org`

**覆盖期刊：** Annual Review of Physical Chemistry, Annual Review of Biochemistry, Annual Review of Psychology 等 Annual Reviews 系列期刊

**下载流程（简单型，URL 构造）：**
1. 导航到论文页面（`/content/journals/10.1146/...`）
2. 从页面 URL 提取 DOI → 构造 PDF 直链 `/doi/pdf/DOI`
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节（2MB+）
4. 保存 + 重命名

**注意事项：**
- 页面上的 PDF 按钮在 `<form>` 内，`href="#"`，不是直接链接，必须从 DOI 构造 URL
- `/doi/pdf/DOI` 直接返回 PDF 字节（Silverchair 平台，但不同于 AIP 需要跨域处理）
- 导航到 `/doi/pdf/` 会重定向到 `docserver/fulltext/...pdf?expires=...&checksum=...`，但 fetch() 在文章页直接拿到
- 没有 `/doi/pdfdirect/` 路径（404）
- citation_* meta 标签完整，metadata 提取无特殊处理

### MDPI (`publisher/mdpi.py`)

**URL 模式：** `mdpi.com`

**覆盖期刊：** Sensors, Materials, Energies, Molecules 等 MDPI 全部 OA 期刊

**下载流程（简单型）：**
1. 导航到论文页面（`/1424-8220/26/10/2941`）
2. DOM 查找 `a.UD_ArticlePDF` → 提取 href（`/1424-8220/26/10/2941/pdf?version=...`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- MDPI 是完全开放获取出版商，所有论文都可下载
- 页面上 Download 按钮展开是下拉菜单（PDF/XML），但 DOM 中有独立的 `a.UD_ArticlePDF` 链接，不需要点击展开菜单
- 也有 `citation_pdf_url` meta 标签直接指向 PDF
- `citation_date` 可能不存在（如 Correction 类文章），用 `citation_online_date` 兜底

### Frontiers (`publisher/frontiers.py`)

**URL 模式：** `frontiersin.org`

**覆盖期刊：** Frontiers in Physics, Frontiers in Chemistry, Frontiers in Neuroscience 等 Frontiers 全部 OA 期刊

**下载流程（简单型）：**
1. 导航到论文页面（`/journals/physics/articles/10.3389/.../full`）
2. DOM 查找 `a.DownloadArticleButton__action` → 提取 href（`/.../pdf`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- Frontiers 是完全开放获取出版商
- 有 `citation_pdf_url` meta 标签直接指向 PDF
- `citation_date` 可能不存在

### eLife (`publisher/elife.py`)

**URL 模式：** `elifesciences.org`

**覆盖期刊：** eLife（单一期刊，OA）

**下载流程（CDN 直链构造型）：**
1. 导航到论文页面（`/articles/106728`）
2. 从 URL 提取文章 ID → 构造 CDN 直链 `cdn.elifesciences.org/articles/{id}/elife-{id}-v1.pdf`
3. `page.evaluate(fetch(cdn_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- 页面上的 `/download/` URL 会触发导航导致 Execution context destroyed，不能直接用
- 必须用 CDN 直链（从文章 ID 构造）
- 没有 `citation_*` meta 标签，metadata 从 `dc.title`、`dc.identifier`、`dc.date`、`dc.contributor` 提取
- DOI 在 `dc.identifier` 中，格式为 `doi:10.7554/eLife.XXXXX`（需去掉 `doi:` 前缀）

### Royal Society (`publisher/royalsociety.py`)

**URL 模式：** `royalsocietypublishing.org`

**覆盖期刊：** Biology Letters, Proceedings B, Philosophical Transactions B, Interface 等 Royal Society 期刊

**下载流程（Silverchair CDN 跨域型，同 AIP）：**
1. 导航到论文页面（`/doi/10.1098/rsbl.2025.0405`）
2. DOM 查找 `a.stats-item-pdf-download` → 提取 href（`/rsbl/article-pdf/doi/.../xxx.pdf`）
3. `resolve_pdf_url()`：`page.goto(pdf_url)` 跟随重定向到 `watermark02.silverchair.com/...?token=...`
4. **留在 PDF 页面**（`fetch_from_pdf_page = True`），同域 fetch 无 CORS 限制
5. `page.evaluate(fetch())` 从 CDN 页面下载 → 返回 PDF 字节

**注意事项：**
- Silverchair 平台，CDN 域是 `watermark02.silverchair.com`（不是 `silverchair-cdn.com`）
- `citation_date` 可能不存在，用 `citation_publication_date` 或 `citation_online_date` 兜底
- 与 AIP 使用完全相同的跨域处理方案（`fetch_from_pdf_page = True`）

### BMJ (`publisher/bmj.py`)

**URL 模式：** `*.bmj.com`（子域名众多：bmj.com, bmjimmunology.bmj.com, gut.bmj.com 等）

**覆盖期刊：** BMJ, BMJ Immunology, Gut, Heart, Thorax 等 BMJ 集团全部期刊

**下载流程（简单型）：**
1. 导航到论文页面（`/content/1/1/e000001`）
2. DOM 查找 `a.article-pdf-download` → 提取 href（`/content/bmjimm/1/1/e000001.full.pdf`）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- 有 `citation_pdf_url` meta 标签直接指向 `.full.pdf` URL
- `citation_date` 可能不存在，用 `citation_online_date` 兜底
- BMJ 子域名众多，`detect()` 匹配 `.bmj.com` 覆盖所有子期刊
- **⚠️ 未完成测试**：CDP 探测确认链接和 metadata 存在，但 fetch 测试超时，可能 PDF 较大或有重定向，待进一步调试

### IEEE Xplore (`publisher/ieee.py`)

**URL 模式：** `ieeexplore.ieee.org`

**覆盖期刊：** IEEE 所有期刊、会议论文、标准（IEEE Photonics Technology Letters, IEEE Journal of Quantum Electronics 等）

**下载流程（getPDF.jsp 构造型）：**
1. 导航到论文页面（`/document/594865`）
2. DOM 查找 `a.xpl-btn-pdf` 确认 PDF 存在（href 指向 `stamp.jsp`）
3. 从页面 URL 提取 arnumber → 构造 `stampPDF/getPDF.jsp?tp=&arnumber={arnumber}`
4. `page.evaluate(fetch(getPDF_url))` → 返回 PDF 字节
5. 保存 + 重命名

**注意事项：**
- 页面上的 PDF 按钮指向 `stamp.jsp`（HTML 包装页，内含 iframe 指向 `getPDF.jsp` + 反爬 JS），**不能直接 fetch stamp.jsp**
- 需要从 URL 提取 arnumber 构造 `getPDF.jsp` 直链
- 覆盖了 `find_download_url()` 而非使用基类默认的 href 提取，因为 element href 是 stamp.jsp 而非 getPDF.jsp
- 没有 `citation_*` meta 标签，metadata 从 DOM 提取：标题从 `document.title`（需去 ` | IEEE ...` 后缀），DOI 从 `a[href*="doi.org"]`

### SPIE (`publisher/spie.py`)

**URL 模式：** `spiedigitallibrary.org`

**覆盖期刊：** Advanced Photonics, SPIE 会议论文, Optical Engineering 等 SPIE 出版物

**下载流程（简单型）：**
1. 导航到论文页面
2. 从 `citation_pdf_url` meta 标签提取 PDF 直链（`.pdf` URL）
3. `page.evaluate(fetch(pdf_url))` → 返回 PDF 字节
4. 保存 + 重命名

**注意事项：**
- SPIE 页面有完整的 `citation_*` meta 标签，非常标准
- `citation_pdf_url` 直接指向 PDF 文件，fetch 一次成功
- 也有 `DOWNLOAD PAPER` 按钮（`a.btn-DownloadPaper`），指向 `journalArticle/Download?urlId=...` API
- 优先用 `citation_pdf_url` 而非按钮 href（更直接）
- `citation_publication_date` 格式为 `YYYY/MM`（不是 `citation_date`）
- 页面 URL 中 `issue-01` 但 `citation_pdf_url` 中是 `issue-1`（无关紧要，都用 meta 标签）

## 适配器接口

```python
class PublisherAdapter(ABC):
    @property
    def name(self) -> str                    # "acs", "optica"
    def detect(self, url) -> bool            # URL 匹配
    def find_download_element(self, page)    # DOM 定位下载按钮
    def find_download_url(self, page)        # 提取 href（base 默认实现）
    def resolve_pdf_url(self, page, url)     # 可选：重定向解析（Optica 需要）
    def get_paper_metadata(self, page)       # 提取标题/DOI/作者
    def navigate_to_paper(self, page, url)   # 导航到论文页
    def check_access(self, page)             # 检查权限
```

## 添加新出版商

1. 在 `publisher/` 下创建新文件，继承 `PublisherAdapter`
2. 实现 `detect()`、`find_download_element()`
3. 如果出版商有 JS 挑战/重定向链，实现 `resolve_pdf_url()`
4. 在 `main.py` 的 `get_adapter()` 中注册
5. 在 `url_parser.py` 的 `PUBLISHER_PATTERNS` 中添加 URL 模式
6. 在 `config.yaml` 的 `publishers` 下添加选择器配置

## main.py 下载流程

```
navigate_to_paper → check_access → get_paper_metadata → simulate_reading
  → find_download_url → [resolve_pdf_url 如果有] → navigate_back
  → [若 use_click_download: click + Ctrl+P 打印] → [否则: pre_click_delay → fetch() download]
  → save → rename → cleanup_tabs
```

**特殊路径：**
- `__click_download__`：Elsevier 返回此标记触发 click_download 流程（Ctrl+P 打印）

## Tab Cleanup

After each download, `browser_helper.cleanup_tabs(browser)` closes all tabs except one and navigates it to `about:blank`. This prevents stale PDF viewer tabs from accumulating and causing subsequent downloads to hang.

## 已知限制

- 截图在 Chrome PDF 查看器页面超时（非关键）
- 大文件通过 base64 传输（page.evaluate 返回），超大 PDF 可能慢
- Windows GBK 编码：控制台不能显示 Unicode 特殊字符，已用 ASCII 替代
- Optica 的 pdfKey URL 构造依赖当前已知的 URL 模式，如果 Optica 改版可能需要更新
- Elsevier 依赖 Foxit Reader Print to PDF 打印机（Ctrl+P 方式非原始 PDF）
- pyautogui OS 级别操作需要 Chrome 窗口可见且在前台
- Foxit Reader 打印的 PDF 是重新渲染的，非原始 PDF 字节

## 构建/运行

```bat
:: 首次
setup.bat

:: 方式 A：手动启动 Chromium（推荐，有登录状态）
start_browser.bat         :: 启动 Chromium (端口 9222)
run.bat "DOI或URL"        :: 下载单篇（main.py 自动 CDP 连接）

:: 方式 B：让 main.py 自动启动（临时 profile，无登录状态）
run.bat --launch-browser "DOI或URL"

:: 批量下载
run.bat --input urls.txt
```

全部 global install，无 venv。可在另一 Chromium 窗口正常浏览，互不影响。
