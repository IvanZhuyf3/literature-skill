# Error Log — 出版商适配器问题记录

记录每个出版商接入过程中遇到的问题、排查过程和最终解决方案。
供后续接入新出版商时参考，避免重复踩坑。

---

## ACS Publications (`publisher/acs.py`)

### E-ACS-01: 下载方案迭代 6 次才找到可行方案

**现象：** 所有常规下载方案全部失败，每个都返回不同错误。

**排查过程：**

| # | 方案 | 错误 | 原因 |
|---|------|------|------|
| 1 | `pyautogui` 物理点击 PDF 链接 | 点击无反应 | 链接带 `target="_blank"`，Chrome 弹窗拦截器阻止 |
| 2 | `requests` + 手动传 cookie | HTTP 403 | Python 的 TLS 指纹与 Chrome 不同，服务端识别为爬虫 |
| 3 | `page.goto(pdf_url)` + `response.body()` | 返回 HTML 非 PDF | Chrome 内置 PDF 查看器劫持了响应，`response` 对象拿到的是查看器页面 |
| 4 | Playwright `route.fetch()` | HTTP 403 | `route.fetch()` 的 TLS 指纹不同于真实浏览器导航 |
| 5 | CDP `Network.getResponseBody` | 返回 HTML | 同样被 Chrome PDF 查看器拦截 |

**最终方案：** `page.evaluate(fetch())` — 在页面 JS 上下文中执行 `fetch()`，使用 Chrome 原生网络栈（TLS + Cookie 完全真实），PDF 查看器不拦截 `fetch()` 请求，返回原始 PDF 字节。

**教训：**
- 出版商反爬检测主要靠 TLS 指纹，不是 Cookie/IP
- Chrome 内置 PDF 查看器会拦截所有"导航到 PDF URL"的尝试
- `page.evaluate(fetch())` 是通用解法，后续出版商应直接用

---

### E-ACS-02: 相对 URL 导致 fetch 失败

**现象：** `find_download_url()` 返回的 href 是 `/doi/pdf/10.1021/...`（相对路径），直接传给 `fetch()` 报错。

**原因：** DOM 中 `a[title='PDF']` 的 href 属性是相对路径。`page.evaluate(fetch())` 在页面上下文执行时，相对路径是相对于当前页面的，通常能工作，但 `download_monitor.py` 中的 URL 校验逻辑需要绝对路径。

**解决：** 在 `base.py` 的 `find_download_url()` 中用 `urljoin(page.url, href)` 统一转绝对路径。

**教训：** 所有从 DOM 提取的 href 都应默认做 `urljoin` 处理，不要假设是绝对路径。

---

### E-ACS-03: `networkidle` 超时

**现象：** `page.goto()` 配合 `wait_until="networkidle"` 经常超时。

**原因：** ACS 页面加载大量分析脚本（Google Analytics, Hotjar 等），持续发送网络请求，`networkidle` 条件（500ms 内无新请求）难以满足。

**解决：** 改用 `wait_until="domcontentloaded"` 作为主要等待条件，`networkidle` 超时做 `try/except` 静默处理（非关键）。

**教训：** 学术出版商页面普遍有大量第三方脚本，`networkidle` 不可靠。优先用 `domcontentloaded` 或 `load`。

---

## Optica Publishing Group (`publisher/optica.py`)

### E-OPT-01: 重定向链中 Chrome PDF 查看器截断 URL 追踪

**现象：** `resolve_pdf_url()` 导航到 `viewmedia.cfm` 后，重定向链走到 `view_article.cfm?pdfKey=...` 就停了，30 秒内 `page.url` 始终是 `view_article.cfm`，看不到最终的 `directpdfaccess/*.pdf` URL。但用户肉眼看到 Chrome 已经显示了 PDF。

**原因：** `view_article.cfm` → `directpdfaccess` 的跳转走 Chrome 内置 PDF 查看器的内部机制（可能通过 `chrome-extension://` 中转），Playwright 的 `page.url` 和 `framenavigated` 事件无法可靠追踪这个跳转。PDF 可能在新标签页或通过内部导航打开。

**解决：** 不追踪完整重定向链，改为从中间页 `view_article.cfm` 的 URL 参数中提取 `pdfKey`，手动构造最终直链：

```
view_article.cfm?pdfKey=0e615e15-14a7-4588-a209b80271ffca8a_591237
  → pdfKey = 0e615e15-14a7-4588-a209b80271ffca8a_591237
  → doi    = ol-51-9-2708 (从原始 viewmedia.cfm URL)
  → id     = 591237 (pdfKey 下划线后的数字)

构造: https://opg.optica.org/directpdfaccess/{pdfKey}/{doi}.pdf?da=1&id={id}&seq=0&mobile=no
```

然后用 `page.evaluate(fetch(构造的URL))` 下载。

**教训：**
- 当重定向链经过 Chrome 内部机制（PDF 查看器、扩展）时，`page.url` 不可靠
- 寻找中间页的 URL 参数，手动构造最终 URL 是更稳定的策略
- "用户看到了 PDF 但代码看不到" 是典型的 Chrome PDF 查看器截断问题

---

### E-OPT-02: JS 挑战页面（HTTP 202）

**现象：** 直接 `fetch()` viewmedia.cfm 的 URL 返回 HTTP 202，内容是 JS 挑战页面而非 PDF。

**原因：** Optica 的反爬机制：首次访问 viewmedia.cfm 返回 202 + JS 挑战（`/checkjs.cfm`），浏览器执行 JS 后设置 cookie/token，之后才允许访问真实 PDF。

**解决：** 必须先让 Chrome 导航到 viewmedia.cfm（`page.goto()`），让 Chrome 自动完成 JS 挑战，然后才能构造直链或 fetch 下载。

**教训：** 有些出版商的"下载链接"不是直接 PDF URL，而是需要浏览器先完成 JS 挑战才能解锁。不能跳过导航直接 fetch。

---

### E-OPT-03: CDP 连接时已有残留标签页

**现象：** `ChromiumHelper` 连接 CDP 时复用了之前的标签页（还在 `directpdfaccess/*.pdf` 页面），导致后续导航行为异常。

**原因：** `connect_over_cdp()` 返回的是当前已打开的标签页列表。如果上次测试留下了 PDF 查看器标签页，`get_first_non_blank_page()` 可能选中它。

**解决：** `chromium_helper.py` 的 `get_first_non_blank_page()` 已过滤 `about:blank` 和 Chromium 内部页面（`chrome-extension://`, `chrome-search://` 等），优先选择非特殊页面。

**教训：** CDP 连接复用用户已有浏览器，必须处理标签页状态不确定的情况。优先选择内容页面，排除 PDF 查看器和内部页面。

---

## AAAS / Science (`publisher/aaas.py`)

### E-AAAS-01: DOI 中的 "403" 触发 check_access 误报

**现象：** Science Advances 论文 `sciadv.adr4039` 被判定为 "Access denied"。

**原因：** 基类 `check_access()` 扫描页面文本中的 "403" 字符串，而 `DOI: 10.1126/sciadv.adr**403**9` 里的 "403" 被误匹配。

**解决：** AAAS 适配器覆盖 `check_access()`，改为直接检测 PDF 下载链接是否存在（有链接 = 有权限），不用文本匹配。

**教训：** `check_access()` 的文本匹配不可靠。DOI、标题、正文都可能偶然包含 "403"、"Access Denied" 等字符串。应优先用 DOM 结构（PDF 按钮存在性）判断权限。

---

### E-AAAS-02: 折叠菜单中的 PDF 链接 is_visible=False

**现象：** AAAS 页面有两个 `Download PDF` 链接，DOM 顺序更早的那个（带 `?download=true`）在折叠菜单里，`is_visible()` 返回 False，被过滤掉了。

**原因：** AAAS 的 PDF 下载按钮有两处：顶栏折叠工具栏（默认不可见）和页面底部（可见）。CSS 选择器按 DOM 顺序匹配到不可见的那个。

**解决：** AAAS 适配器的 `find_download_element()` 不检查 `is_visible()`，因为折叠菜单里的链接功能完全正常，只是当前不在视口中。

**教训：** `is_visible()` 不等于"链接有效"。折叠菜单、需要滚动的区域、响应式隐藏元素中的链接都能正常使用。不要盲目过滤。

---

### E-AAAS-03: 残留标签页导致 ERR_BLOCKED_BY_RESPONSE

**现象：** 多次测试后，Chrome 中残留的标签页导航同一 URL 时返回 `net::ERR_BLOCKED_BY_RESPONSE`。但新开标签页访问正常。

**原因：** Chrome 对重复快速访问同一页面的标签有内部限制。之前测试的标签页虽然 URL 正确，但内部渲染状态已损坏。

**解决：** `main.py` 的 `download_paper()` 中加入导航重试：首次失败后自动新开标签页重新导航。`chromium_helper.py` 的 `get_or_create_page()` 改为从最新标签页开始检查（`reversed`），倾向于使用更健康的页面。

**教训：** CDP 复用浏览器时，测试/调试会留下残留标签页，可能导致后续导航失败。导航失败时自动新开标签页是可靠的 fallback。

---

## Springer (`publisher/springer.py`)

### E-SPRINGER-01: 基类 check_access 文本匹配误报（第二次）

**现象：** Springer OA 文章被判定 "Access denied"。

**原因：** 与 E-AAAS-01 相同的根因。基类 `check_access()` 扫描页面文本时匹配到了误报词。

**解决：** 覆盖 `check_access()`，用 `a[data-track-action="download pdf"]` 存在性判断权限。

**教训：** 这是第二次踩这个坑（AAAS 是第一次）。基类的文本匹配方案应废弃——所有新适配器都应覆盖 `check_access()` 用 DOM 结构判断。应考虑将基类默认行为改为"有 PDF 链接 = 有权限"。

---

## AIP / Silverchair (`publisher/aip.py`)

### E-AIP-01: Silverchair CDN 跨域导致 fetch() 失败

**现象：** `page.evaluate(fetch(pdf_url))` 返回 `TypeError: Failed to fetch`，但 `page.goto(pdf_url)` 正常（HTTP 200，content-type: application/pdf）。

**原因：** AIP 的 PDF URL（`pubs.aip.org/aip/jcp/article-pdf/...`）会重定向到 Silverchair CDN（`watermark02.silverchair.com/...?token=...`）。CDN 域和文章页不同源，浏览器的 CORS 策略阻止了跨域 `fetch()` 请求。

**解决：**
1. `resolve_pdf_url()` 先 `page.goto(pdf_url)` 跟随重定向，拿到 CDN 的带 token URL
2. 设置 `fetch_from_pdf_page = True` 标志，让 main.py 留在 PDF 页面上
3. 在 PDF 页面（CDN 域）的上下文中做 `fetch(window.location.href)`，同源无 CORS 限制

**教训：**
- 当 PDF 存放在 CDN（不同域名）时，从文章页 fetch 会 CORS 失败
- `page.goto()` 跟随重定向不受 CORS 限制（是导航不是 XHR）
- 解决方案：先导航到 PDF URL 让 Chrome 跟随重定向，再在结果页面上 fetch
- `fetch_from_pdf_page = True` 标志是通用机制，其他使用 CDN 的出版商也可能需要

---

## Elsevier / ScienceDirect (`publisher/elsevier.py`)

### E-ELSEVIER-01: Chrome PDF 查看器完全劫持 /pdfft URL

**现象：** Elsevier 的 PDF URL（`/pdfft?md5=...&pid=...`）被 Chrome 内置 PDF 查看器完全接管。所有 Playwright 事件（`response`、`request`）被抑制，无法通过网络拦截获取 PDF。

**排查过程：**

| # | 方案 | 结果 | 原因 |
|---|------|------|------|
| 1 | `page.goto(pdfft_url)` + `page.on("response")` | response 不触发 | Chrome PDF 查看器接管，Playwright 事件全被抑制 |
| 2 | `page.evaluate(fetch(pdfft_url))` | TypeError: Failed to fetch | PDF 查看器页面上下文中 fetch 自身 URL 失败 |
| 3 | `page.evaluate(fetch())` 在 PDF 查看器页 | 返回 HTML | PDF 查看器不暴露 PDF 字节给 JS 上下文 |
| 4 | `page.goto()` + `response.body()` | 返回查看器 HTML | 同 E-ACS-01，Chrome PDF 查看器劫持响应 |

**最终方案：** Ctrl+P 打印为 PDF（pyautogui）。用 Playwright `click()` + `expect_popup()` 打开 View PDF 新 tab，在 PDF 查看器中用 pyautogui 发送 `Ctrl+P` → Enter → Enter，通过 Foxit Reader Print to PDF 打印到 temp 目录。

**教训：**
- Elsevier 的 `/pdfft` 是 ACS 问题的加强版——不仅 fetch 不行，连导航后的所有 Playwright 事件都被抑制
- 必须走 OS 级别的物理操作（pyautogui），这是目前唯一需要 `use_click_download = True` 的出版商
- `__click_download__` 特殊标记机制由此诞生

---

### E-ELSEVIER-02: window.open 新 tab 不被 CDP 捕获

**现象：** 用 `page.evaluate('window.open(pdfft_url)')` 打开新 tab，但 `ctx.on("page")` 不触发，`ctx.pages` 里也找不到新 tab。

**原因：** Chrome PDF 查看器接管 `/pdfft` 导航后，新 tab 的创建走内部机制，Playwright CDP session 感知不到。

**解决：** 改用 Playwright `click()` + `expect_popup()` 组合。Playwright 的 popup 监听机制能捕获 click 触发的 `window.open`（虽然 PDF 查看器后续接管，但 popup 事件本身能触发）。

**教训：** 不要用 `page.evaluate('window.open()')` 来打开 PDF URL——Chrome PDF 查看器会截断 CDP 事件链。用 Playwright 的 `click()` + `expect_popup()` 更可靠。

---

### E-ELSEVIER-03: pyautogui 快捷键发给了错误窗口

**现象：** `pyautogui.hotkey('ctrl', 'p')` 发送后没有任何反应（打印对话框没弹出）。

**原因：** `pyautogui` 是 OS 级别的，快捷键发给当前 focus 的窗口。如果 Chrome 窗口不在前台（比如终端/IDE 在前台），Ctrl+P 发给了终端。

**解决：** 在发 Ctrl+P 之前：
1. 用 `page.evaluate()` 获取 Chrome 窗口的 `screenX/screenY/outerWidth/outerHeight`
2. `pyautogui.click(title_bar_center)` 点击标题栏中间位置激活 Chrome 窗口
3. 再点击内容区域确认激活
4. 然后才发 Ctrl+P

**教训：** `pyautogui` 和 Playwright 是两个完全不同的层次。Playwright 操作 browser context，pyautogui 操作 OS 桌面。两者的"焦点"概念不同——必须显式切换 OS 焦点。

---

### E-ELSEVIER-04: Foxit Reader 打印文件锁导致重命名失败

**现象：** 打印完成后，`os.rename()` 报 `PermissionError`，文件被 Foxit Reader 锁住。

**原因：** Foxit Reader Print to PDF 完成后短暂持有文件句柄，rename 操作与文件写入存在竞争。

**解决：** main.py 的 rename 加入重试逻辑（最多 5 次 × 3 秒间隔），同时 `click_download()` 中等文件大小稳定（连续两次读取大小一致）后才返回文件路径。

**教训：** 通过打印生成 PDF 的方案涉及多个进程（Chrome → 打印队列 → Foxit Writer），文件锁是常态。所有文件操作都需要重试。

---

## PNAS (`publisher/pnas.py`)

### E-PNAS-01: URL 带 ?download=true 参数的 PDF 直链

**现象：** PNAS 的 PDF 链接是 `/doi/pdf/10.1073/pnas.XXXX?download=true`，带 `?download=true` 后缀。

**原因：** PNAS 使用 Silverchair 平台（与 AIP 相同平台），但 Silverchair 的不同客户配置不同。AIP 的 PDF 会重定向到 CDN（`watermark02.silverchair.com`），而 PNAS 的 PDF 直接由主站提供，`?download=true` 参数让浏览器直接下载而非在查看器中打开。

**解决：** 直接 `page.evaluate(fetch(pdf_url))`，简单型下载。不需要像 AIP 那样处理跨域 CDN。

**教训：** 同一平台（Silverchair）的不同出版商行为可能完全不同。AIP 需要跨域处理，PNAS 只需简单 fetch。不能假设同平台 = 同方案。

---

## Wiley Online Library (`publisher/wiley.py`)

### E-WILEY-01: /doi/pdf/ 返回 HTML wrapper，不是 PDF

**现象：** Wiley 文章页上的 `/doi/pdf/DOI` 链接，`page.evaluate(fetch())` 返回 HTML 内容（一个 PDF 内嵌查看器 wrapper），不是 `%PDF` 字节。

**原因：** Wiley 的 `/doi/pdf/` URL 返回的是一个 HTML 页面，里面内嵌了 PDF 查看器（类似 epdf 页面）。真正的 PDF 字节在 `/doi/pdfdirect/DOI?download=true`。

**解决：** 不使用 `/doi/pdf/` 链接，改为导航到 epdf 页面（`/doi/epdf/DOI`），找到 `/doi/pdfdirect/DOI?download=true` 链接做 fetch。

**教训：**
- `/doi/pdf/` 不一定返回 PDF——出版商可能用它做 HTML wrapper
- `/doi/pdfdirect/` 更可能是真正的 PDF 字节
- 这个规律在多个出版商中验证过（Wiley, AAAS 例外）

---

### E-WILEY-02: epdf 查看器页面没有 citation meta 标签

**现象：** `debug_wiley.py` 探测发现 epdf 页面（`/doi/epdf/DOI`）没有 `citation_title`、`citation_doi` 等 meta 标签，metadata 提取全部返回空。

**原因：** Wiley 的两种页面内容不同：
- 文章信息页（`/doi/DOI`）：有完整的 `citation_*` meta 标签，但 `/doi/pdf/` 链接返回 HTML
- epdf 查看器（`/doi/epdf/DOI`）：有 `/doi/pdfdirect/` 真正 PDF 链接，但没有 `citation_*` meta 标签

**解决：** 两步策略——先导航到文章信息页提取 metadata，再 `resolve_pdf_url()` 跳到 epdf 页面提取 pdfdirect 下载链接。`fetch_from_pdf_page = True` 留在 epdf 页做 fetch（同域无 CORS 问题）。

**教训：**
- metadata 和下载链接可能在不同的页面上
- 新出版商接入时必须同时探测两种页面的 meta 和链接
- `fetch_from_pdf_page = True` 最初为 AIP CDN 跨域发明，这里用在 Wiley 的跨页场景（虽然不是跨域，但需要留在 resolve 后的页面上）

---

## APS / Physical Review (`publisher/aps.py`)

### E-APS-01: Supplemental PDF 链接混在主文 PDF 中

**现象：** `find_download_element()` 匹配到的第一个 `/pdf/` 链接指向补充材料而非主文。

**原因：** APS 页面上有多个 `href*="/pdf/"` 链接：主文 PDF（`/prl/pdf/10.1103/...`）和补充材料（`/supplemental/10.1103/...`）。简单的 `href*="/pdf/"` 选择器可能先匹配到 supplemental。

**解决：** 使用 `a.sm-primary-button[href*="/pdf/"]` 精确匹配主 PDF 按钮（APS 的主 PDF 按钮用 `sm-primary-button` class），同时 fallback 选择器用 `:not([href*="/supplemental/"])` 排除补充材料。

**教训：** 学术出版商页面上经常有多个 PDF（主文 + 补充材料 + SI）。选择器必须精确区分，不能假设第一个匹配的就是主文。

---

## Taylor & Francis (`publisher/tandf.py`)

### E-TF-01: 没有 citation_* meta 标签

**现象：** `debug_tandf.py` 探测发现 T&F 页面上没有任何 `citation_title`、`citation_doi`、`citation_date` meta 标签。`debug_tandf2.py` 进一步确认所有 meta 标签中都没有 citation 相关内容。

**原因：** T&F 不使用标准学术 meta 标签（HighWire Press 格式）。

**解决：**
- 标题：从 `document.title` 提取，去掉 `"Full article: "` 前缀和 `" - Taylor & Francis"` 等后缀
- DOI：从 URL pathname 用正则提取（`/doi/full/10.1080/...` → `10.1080/...`）
- 作为 fallback，也尝试 `meta[name="citation_doi"]`（部分 T&F 期刊可能有）

**教训：**
- 不能假设所有出版商都有 `citation_*` meta 标签
- `document.title` 和 URL pathname 是可靠的 metadata fallback 来源
- 标题清理逻辑（去前后缀）因出版商而异，需要针对每个站点的 title 格式做处理

---

### E-TF-02: /doi/epdf/ 和 /doi/pdf/ 是不同的东西

**现象：** T&F 页面上有两种 PDF 相关链接：`/doi/epdf/...`（内嵌 PDF 查看器）和 `/doi/pdf/...`（下载链接）。

**原因：** `/doi/epdf/` 是 T&F 的内嵌 PDF 查看器页面，`/doi/pdf/` 才是真正的 PDF 下载链接。

**解决：** 选择器优先用 `a.show-pdf[href*="/doi/pdf/"]`，避免匹配到 `/doi/epdf/` 链接。

**教训：** 很多出版商区分 `epdf`（内嵌查看器）和 `pdf`（下载）。选择器应明确排除 `/epdf/`。

---

## RSC / Royal Society of Chemistry (`publisher/rsc.py`)

### 无重大问题

RSC 是最顺利的出版商之一：
- 有 `citation_pdf_url` meta 标签直接指向 PDF URL
- `/content/articlepdf/...` 链接直接返回 PDF 字节
- `page.evaluate(fetch())` 一次成功
- 选择器 `a.btn--primary[href*="articlepdf"]` 精确匹配

**唯一注意：** `citation_date` meta 标签可能不存在，用 `citation_online_date` 兜底。

---

## IOP / IOPscience (`publisher/iop.py`)

### 无重大问题

IOP 也是顺利的出版商：
- 有 `citation_pdf_url` meta 标签
- `/article/DOI/pdf` 链接直接返回 PDF
- `page.evaluate(fetch())` 一次成功
- `a.wd-jnl-art-pdf-button-main` 是主下载按钮的精确 class

**唯一注意：** `citation_date` 可能不存在，用 `citation_online_date` 兜底。IOP 页面加载后需要额外等待（`wait_for_timeout(5000)`），DOM 渲染较慢。

---

## SPJ / Science Partner Journals

### E-SPJ-01: 不需要新适配器

**现象：** `spj.science.org` 的 URL 包含 `science.org`，被 AAAS 适配器自动匹配。

**排查过程：** 写了 `debug_spj.py`、`debug_spj2.py`、`debug_spj3.py` 三个脚本分别探测：
1. SPJ 文章页面的 PDF 链接结构
2. epdf 页面的差异
3. PDF fetch 测试（`?download=true` vs 不带参数）

**结论：** SPJ 使用和 AAAS 主站相同的页面架构（Science 平台），AAAS 适配器的 `detect()` 匹配 `science.org in url` 自动覆盖 `spj.science.org`，选择器和下载流程完全通用。

**教训：** 新出版商接入前先检查是否被现有适配器的 URL 匹配覆盖。子域名（`spj.science.org` ⊂ `science.org`）经常共享同一平台。

---

## Annual Reviews (`publisher/annualreviews.py`)

### 无重大问题

接入顺利，CDP 探测一次搞定：
- `/doi/pdf/DOI` 直接返回 PDF 字节（2MB+），fetch() 一次成功
- citation_* meta 标签完整
- Silverchair 平台（与 AIP、PNAS 同平台），但无需跨域处理（PDF 由主站提供，不重定向到 CDN）

**唯一注意：** 页面上的 PDF 下载按钮在 `<form>` 内（`href="#"`），不是直接链接。必须从页面 URL 的 DOI 构造 `/doi/pdf/DOI` 直链，不能直接从 DOM 的 href 提取。这是第一家用"按钮存在性检测 + URL 构造"而非"从按钮 href 提取"的出版商。

---

## MDPI (`publisher/mdpi.py`)

### 无重大问题

接入极其顺利——MDPI 是完全开放获取出版商：
- `a.UD_ArticlePDF` 直接指向 PDF 链接
- `citation_pdf_url` meta 标签也有
- fetch() 一次成功返回 `%PDF`

**注意：** 用户描述 Download 按钮展开是下拉菜单（PDF/XML），但 DOM 中实际有独立的 `<a>` 链接（`UD_ArticlePDF` class），不需要模拟点击展开菜单。很多"下拉菜单"场景其实在 DOM 中都有隐藏的直接链接，CDP 探测能看到。

---

## Frontiers (`publisher/frontiers.py`)

### 无重大问题

接入顺利，CDP 探测一次搞定：
- `a.DownloadArticleButton__action` 直接指向 PDF 链接
- `citation_pdf_url` meta 标签也有
- fetch() 一次成功返回 `%PDF`（316KB）
- OA 出版商，不需要登录

---

## eLife (`publisher/elife.py`)

### E-ELIFE-01: /download/ URL 触发导航导致 Execution context destroyed

**现象：** `page.evaluate(fetch('/download/...'))` 报错 `Execution context was destroyed, most likely because of a navigation`。

**解决：** 不使用 DOM 中的 `/download/` 链接，改为从文章 ID 构造 CDN 直链：`cdn.elifesciences.org/articles/{id}/elife-{id}-v1.pdf`。

**教训：** 有些下载 URL 是重定向端点而非直接文件链接。fetch() 触发导航时，改用可构造的 CDN 静态 URL。

### E-ELIFE-02: 没有 citation_* meta 标签

**解决：** 从 `dc.*` (Dublin Core) meta 标签提取：`dc.title`、`dc.identifier`（DOI，需去 `doi:` 前缀）、`dc.date`、`dc.contributor`。

**教训：** 不能假设所有出版商都用 `citation_*` (HighWire Press) 格式。Dublin Core 是另一套常见 metadata 格式。

---

## Royal Society (`publisher/royalsociety.py`)

### E-ROYALSOC-01: Silverchair CDN 子域名与 AIP 不同

**现象：** `resolve_pdf_url()` CDN 检查只匹配 `silverchair-cdn.com`，但 Royal Society 用的是 `watermark02.silverchair.com`，导致返回原始 URL，后续 fetch 因 CORS 失败。

**解决：** CDN 检查改为 `"silverchair" in url`，宽松匹配所有 Silverchair CDN 变体。

**教训：** 同一平台（Silverchair）的不同出版商 CDN 子域名可能不同。CDN 检查应用宽松匹配。

---

## BMJ (`publisher/bmj.py`)

### E-BMJ-01: fetch 测试超时（待调查）

**现象：** CDP 探测中 `page.evaluate(fetch('.full.pdf'))` 超时无返回。页面加载正常，PDF 链接和 metadata 都能正确提取。

**状态：** ✅ 主流程测试通过（154.4KB），debug 脚本超时是假阳性。

---

## IEEE Xplore (`publisher/ieee.py`)

### E-IEEE-01: stamp.jsp 是 HTML 包装页，不能直接 fetch

**现象：** 页面 PDF 按钮指向 `stamp.jsp?tp=&arnumber=XXX`，但直接 fetch 返回 HTML（反爬 JS 包装），不是 PDF。

**原因：** `stamp.jsp` 是 HTML 页面，内含 iframe 指向 `getPDF.jsp`。fetch stamp.jsp 拿到的是 HTML 包装而非 PDF 字节。

**解决：** 从页面 URL 提取 arnumber，构造 `getPDF.jsp?tp=&arnumber={arnumber}` 直链。覆盖 `find_download_url()` 绕过基类默认的 href 提取（基类会拿到 stamp.jsp）。

**教训：** 有些出版商的 PDF 按钮指向包装页（含 iframe/JS），实际 PDF 在另一个 URL。需要探测中间页结构。

### E-IEEE-02: 无 citation_* meta 标签

**解决：** 标题从 `document.title` 提取（去 ` | IEEE ...` 后缀），DOI 从 `a[href*="doi.org"]` 提取。

---

## SPIE (`publisher/spie.py`)

### 无重大问题

接入非常顺利：
- `citation_*` meta 标签完整（title, doi, date, authors, pdf_url 全有）
- `citation_pdf_url` 直接指向 PDF，fetch() 一次成功（3.2MB）
- 标准简单型适配器，无需特殊处理

---

## 通用经验

### 下载方案选择（优先级）

1. **`page.evaluate(fetch(url))`** — 首选，适用于 17/21 家出版商
2. **URL/CDN 构造** — 从 DOI 或文章 ID 构造直链（Annual Reviews, eLife, IEEE）；重定向链中间页参数构造直链（Optica）
3. **跨页策略** — metadata 和 PDF 在不同页面时，先拿 metadata 再跳转（Wiley）
4. **跨域 fetch** — 先 `page.goto()` 跟随重定向到 CDN，再在结果页面 fetch（AIP）
5. **Ctrl+P 打印** — 仅当 Chrome PDF 查看器完全劫持时使用（Elsevier），最后手段

### 常见反爬模式

| 模式 | 出版商 | 应对 |
|------|--------|------|
| TLS 指纹检测 | ACS, Optica | `page.evaluate(fetch())` 用 Chrome 原生栈 |
| JS 挑战（HTTP 202） | Optica | `page.goto()` 让 Chrome 自动完成 |
| Chrome PDF 查看器劫持 | Elsevier | `__click_download__` + pyautogui Ctrl+P 打印 |
| Chrome PDF 查看器劫持（轻度） | ACS, AAAS 等 | 不导航到 PDF URL，用 fetch() 直接取字节 |
| `/doi/pdf/` 返回 HTML | Wiley | 用 `/doi/pdfdirect/` 或带 `?download=true` 的链接 |
| CDN 跨域 CORS | AIP (Silverchair) | `page.goto()` 跟随重定向 + `fetch_from_pdf_page = True` |
| Silverchair 同平台不同行为 | PNAS vs AIP | 同平台不同客户配置，AIP 需跨域，PNAS/Annual Reviews 直接 fetch |
| PDF 按钮是 form（href="#"） | Annual Reviews | 从 DOI 构造 `/doi/pdf/DOI` 直链 |
| `/download/` URL 触发导航 | eLife | 用 CDN 直链 `cdn.elifesciences.org/articles/{id}/...` |
| PDF 按钮指向 HTML 包装页（stamp.jsp） | IEEE | 构造 `getPDF.jsp?tp=&arnumber={id}` 直链，覆盖 `find_download_url()` |
| 无 citation_* meta | eLife, T&F | 用 `dc.*` (Dublin Core) 或 `<title>` + URL 提取 |
| Silverchair CDN 子域名不同 | Royal Society vs AIP | CDN 检查用宽松匹配 `"silverchair" in url` |
| citation meta 缺失 | T&F | 从 `<title>` 和 URL pathname 提取 |
| Supplemental PDF 干扰 | APS | 精确选择器 + `:not([href*="/supplemental/"])` |
| 相对 URL | ACS | `urljoin()` 转绝对路径 |
| `check_access` 文本误报 | AAAS, Springer | 用 PDF 链接存在性判断，不覆盖文本匹配 |
| `networkidle` 不稳定 | 通用 | 用 `domcontentloaded` 替代，`networkidle` 超时做非关键处理 |

### 接入新出版商的 Checklist

1. 写 `debug/debug_<publisher>.py` CDP 探测脚本（必须，不能跳过）
2. 探测页面上所有 PDF/download 相关链接（href、class、text）
3. 逐个 `fetch()` 测试候选链接，确认哪个返回 `%PDF`
4. 检查 `citation_*` meta 标签是否存在；如果没有，确认 `<title>` 和 URL 能否提取 metadata
5. 检查 `/doi/pdf/` 返回的是 PDF 还是 HTML wrapper
6. 检查是否需要跨页（metadata 页 vs 下载页）
7. 确定下载类型（简单型 / 多页型 / 跨域型 / 打印型）
8. 实现适配器 + 注册 + 测试
9. **记录问题到 `error_log.md`**

## 2026-06-16 — Ji_Xin_Cheng: 10.1002/jccs.197500045 (Type B: Access/Subscription)
- Paper: "The Neutral Part of the Bark of Pinus Luchuensis Mayer" (J. Chinese Chem. Soc., 1975)
- Publisher: Wiley (adapter registered, "Download PDF" selector works, PDF URL resolved to /doi/pdf/DOI)
- Error: epdf redirect resolution fails — navigating /doi/epdf/DOI redirects to /doi/abs/DOI with login/register prompts (Individual login, Institutional login, REGISTER). No pdfdirect link present.
- Root cause: Article is subscription-restricted; current Edge session has no authenticated access. Type B.
- Action: Not fixable via code. Logged + skipped. Status stays 'failed'.

##  — Ji_Xin_Cheng cron tick
- **Paper:** The Neutral Part of the Bark of Pinus Luchuensis Mayer
- **DOI:** 10.1002/jccs.197500045 (wiley / jccs, 1975)
- **Category:** B (Access denied / subscription)
- **Symptom:** epdf URL redirects to /doi/abs/ (no viewer loads); "No pdfdirect link found on epdf page" x3
- **Action:** Logged + skipped. Not fixable (no open access).
[2026-06-16 22:12:05]
DOI: 10.1002/jccs.197500045 (Wiley - onlinelibrary.wiley.com)
Error: Failed to resolve PDF URL through redirects (3 attempts) - Type A runtime/navigation
Action: Skipped - not fixable via cron
---
## E-WILEY-001: Wiley 403 access denied (2026-06-16)

**Paper:** The Neutral Part of the Bark of Pinus Luchuensis Mayer
**DOI:** 10.1002/jccs.197500045
**URL:** https://onlinelibrary.wiley.com/doi/10.1002/jccs.197500045
**Symptom:** PDF links (epdf/pdf/pdfdirect) all return HTTP 403 text/html.  
  Article page loads normally, PDF download buttons visible in DOM, but fetch() returns 403.
**Category:** Access denied / subscription (type B)
**Resolution:** Skipped — not fixable without subscription access.
## 2026-06-16 Wiley paper failed (subscription)

- DOI: 10.1002/jccs.197500045
- Title: The Neutral Part of the Bark of Pinus Luchuensis Mayer
- Publisher: Wiley (onlinelibrary.wiley.com)
- Error: Subscription required — /doi/pdf/ returned 403, /doi/epdf/ redirected to abstract
- Type: B (access denied)
- Resolution: Marked as failed, no adapter fix applicable


## 2026-06-16 23:41 - Ji_Xin_Cheng cron
DOI: 10.1016/S1386-1425(98)00157-7
Title: The high resolution spectrum of AsH3 (4 0 0) local mode state
Fix: Patched NameError in elsevier.py:312 (undefined 'monitor')
Retry result: timeout (120s) - publisher page hung (cat A)

