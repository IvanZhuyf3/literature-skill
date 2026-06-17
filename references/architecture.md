# Literature Skill — 项目知识文档

## 项目概述

学术论文自动下载 + Zotero 管理工具。核心功能：
- **发现**：从 Google Scholar 抓取学者论文列表，CrossRef 匹配 DOI，注册到 Zotero
- **下载**：通过 Playwright CDP 连接 Chromium 浏览器，绕过出版商反爬检测下载 PDF
- **挂载**：WebDAV 方式将 PDF 附到 Zotero 条目（不消耗云配额）
- **消化**：读 Zotero 数据生成结构化文献消化报告

## 架构概览

```
lit/                              ← python -m lit <command> （主入口）
├── cli.py                        ← argparse 调度（8 子命令）
├── core/
│   ├── config.py                 ← 配置单例（取代各模块各自 load_config）
│   ├── crossref.py               ← CrossRef DOI 解析 + 元数据查询
│   └── zotero.py                 ← Zotero API 封装（Collection / Item / Attachment）
├── discover/
│   ├── scholar.py                ← Scholar 抓取 → 直接建 Zotero 条目
│   └── cite.py                   ← 单篇 DOI/URL/图片 → 注册 Zotero
├── download/
│   ├── engine.py                 ← CDP 下载引擎（导入 publisher/ 适配器）
│   └── attacher.py               ← PDF 挂载封装
├── batch/
│   ├── attach.py                 ← 读 Zotero collection → 批量补 PDF
│   └── register.py               ← 批量注册条目
└── digest/
    ├── template.py               ← 读 Zotero → 生成 4-Block 消化模板
    └── parser.py                 ← MinerU PDF → Markdown 解析

publisher/                        ← 25 家出版商适配器（被 download/engine.py 导入）
├── base.py                       ← PublisherAdapter 抽象基类
├── acs.py, npg.py, elsevier.py, ...  ← 各出版商适配器

# 旧版入口（弃用但保留兼容，详见 references/legacy.md）
main.py, zot.py, people.py, chromium_helper.py, url_parser.py, ...
```

## 模块职责

| 模块 | 职责 |
|------|------|
| `lit/cli.py` | argparse 调度入口，8 子命令映射到各模块 |
| `lit/core/config.py` | 配置加载（单例），自动从 `lit/` 父目录找 `config.yaml` |
| `lit/core/crossref.py` | CrossRef REST API：按标题搜索、按 DOI 获取元数据 |
| `lit/core/zotero.py` | Zotero API 封装：集合 CRUD、条目创建/去重/删除、附件挂载 |
| `lit/discover/scholar.py` | Playwright CDP 抓取 Scholar Profile → 过滤专利/会议 → CrossRef DOI 匹配 → Zotero 注册 |
| `lit/discover/cite.py` | 单篇论文入口：DOI/URL 查 CrossRef 建条目，或图片 OCR 提取引用 |
| `lit/download/engine.py` | PDF 下载引擎：DOI→URL→出版商识别→CDP 连接→适配器分发→fetch()/打印下载→验证 |
| `lit/download/attacher.py` | 薄封装：下载 + 调用 `core.zotero` 挂载附件 |
| `lit/batch/attach.py` | 读 Zotero collection 找出无 PDF 条目 → 逐篇下载 + 挂载 |
| `lit/batch/register.py` | 批量用 CrossRef 元数据注册条目到 Zotero（无 PDF） |
| `lit/digest/template.py` | 读 Zotero collection → 生成 4-Block 消化模板 Markdown |
| `lit/digest/parser.py` | MinerU 在线 API PDF→Markdown 解析 |

### 旧版入口（保留兼容，路径见 `references/legacy.md`）

| 文件 | 状态 | 用途 |
|------|------|------|
| `main.py` | 弃用 | `lit/download/engine.py` 的 fallback 子进程 |
| `zot.py` | 弃用 | 旧版 Zotero 完整工作流 |
| `people.py` | 弃用 | 旧版学者批量处理 |
| `chromium_helper.py` | 弃用 | Chromium 启动/CDP 连接（`lit/download/engine.py` 导入） |
| `url_parser.py` | 弃用 | URL/DOI 解析（被 `lit/download/engine.py` 导入） |
| `publisher/` | **活跃** | 25 家适配器，**仍被 `lit/download/engine.py` 导入使用** |

## 数据流转

### Scholar → Zotero 注册路径
```
Google Scholar (Playwright CDP)
    → 抓取论文列表（标题、作者、年份、引用数）
    → 过滤专利/会议/重复
    → CrossRef 搜索标题匹配 DOI
    → Zotero API 创建 People/<学者名> 集合
    → 逐篇创建条目（含 DOI、作者、年份等元数据）
    → 无 PDF 附件
```

### PDF 下载路径
```
DOI/URL
    → url_parser 识别出版商
    → Chromium CDP 连接（手动启动，有机构登录）
    → publisher/<name>.py 适配器：navigate → check_access → metadata → find_download_url
    → 路径 A：page.evaluate(fetch(pdf_url)) 返回 PDF 字节（大部分出版商）
    → 路径 B：Ctrl+P 打印为 PDF（Elsevier ScienceDirect）
    → 验证：文件存在、>100KB、%PDF 头
    → 按论文标题重命名
```

### Zotero 附件挂载
```
PDF 下载完成
    → 检查 Zotero 条目是否存在（按 DOI 查重）
    → 已有条目：创建 attachment + 拷文件到 storage/{att_key}/
    → 无条目：先创建条目再 attach
    → sync_method = webdav（不消耗云配额）
```

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
- `use_click_download = True`：通知 engine 不走 fetch() 流程
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

1. 在 `publisher/` 下创建新文件，继承 `PublisherAdapter`（模板见 `references/maintain.md` 流程 B）
2. 实现 `detect()`、`find_download_element()`、`navigate_to_paper()`、`get_paper_metadata()`
3. 如果出版商有 JS 挑战/重定向链，实现 `resolve_pdf_url()`
4. 在 `url_parser.py` 的 `PUBLISHER_PATTERNS` 中添加 URL 模式
5. 在 `lit/download/adapters/__init__.py` 中注册
6. 在 `config.yaml` 的 `publishers` 下添加选择器配置
7. 在 `SKILL.md` 和 `references/architecture.md` 中更新出版商列表

## 已知限制

- 截图在 Chrome PDF 查看器页面超时（非关键）
- 大文件通过 base64 传输（page.evaluate 返回），超大 PDF 可能慢
- Windows GBK 编码：控制台不能显示 Unicode 特殊字符，已用 ASCII 替代
- Optica 的 pdfKey URL 构造依赖当前已知的 URL 模式，如果 Optica 改版可能需要更新
- Elsevier 依赖 Foxit Reader Print to PDF 打印机（Ctrl+P 方式非原始 PDF）
- pyautogui OS 级别操作需要 Chrome 窗口可见且在前台
- Foxit Reader 打印的 PDF 是重新渲染的，非原始 PDF 字节

## 常用命令

```bash
# Scholar → Zotero 注册（无 PDF）
python -m lit scholar "GOOGLE_SCHOLAR_URL"

# 单篇加 Zotero
python -m lit import "DOI_or_URL"

# 单篇下载 PDF（不入 Zotero）
python -m lit download "DOI_or_URL"

# 批量补 PDF（读 Zotero collection）
python -m lit attach "Ji-Xin Cheng" --limit 5

# 生成消化报告
python -m lit digest "Ji-Xin Cheng"

# MinerU 解析 PDF
python -m lit parse "paper.pdf" -o "paper.md"

# QR 码
python -m lit qr "10.1038/s41566-026-01891-6"
```
