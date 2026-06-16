---
name: literature-skill
description: |
  学术文献一站式工具。主命令 `/literature-skill`，子命令作为参数传入：
  - `/literature-skill -paper <DOI/URL>` → 做全套：下载 PDF + 生成 QR 码 + 提取元数据 + 添加到 Zotero + 挂载附件。
  - `/literature-skill -download <DOI/URL>` → 只下载论文 PDF，不涉及 Zotero。
  - `/literature-skill -pdf <DOI/关键词>` → 查找已下载的 PDF 文件路径，通过微信/Telegram 发送文件。
  - `/literature-skill -qr <DOI>` → 根据 DOI 生成 QR 码图片（指向 https://doi.org/xxx）。
  - `/literature-skill -zot <DOI/URL>` → 只加进 Zotero：提取元数据 + 创建条目 + 挂载 PDF（不触发下载）。
  也支持从图片（PPT 拍照、截图）提取引用再走上述流程。触发词："extract citations from image", "这个图里的文献", "图片引用"。
  自然语言同义词也会触发："download paper", "get PDF", "fetch paper", "下载论文", "抓取论文", "批量下载" 走下载路径；"add to zotero", "save paper", "import paper", "收藏论文" 走 Zotero 路径；"二维码", "QR code" 走 QR 路径。
allowed-tools: Bash(uv:*), Bash(python:*), Bash(node:*)
---

# 规则

- 把当前 `SKILL.md` 所在目录视为 `<skill-base>`。所有本地资源从 `<skill-base>` 解析，不依赖调用方工作目录。
- **五个功能入口**（子命令作为参数传入 `/literature-skill`）：
  - `-paper` → `python "<skill-base>/zot.py"` — 全套：下载 PDF + 生成 QR + 添加到 Zotero + 挂载
  - `-zot` → `python "<skill-base>/zot.py" --no-download` — 只加 Zotero：元数据 + 创建条目（不下载 PDF）
  - `-download` → `python "<skill-base>/main.py"` — 只下载 PDF
  - `-qr` → `python "<skill-base>/generate_qr.py"` — 只生成 QR 码
  - `-pdf` → 查找已下载的 PDF 文件路径（纯文件搜索，无脚本）
- **Chromium 启动有两种方式**（main.py 会自动处理）：
  - **已手动启动**（推荐，有机构登录状态）：用户用 `start_browser.bat` 或手动加 `--remote-debugging-port=9222` 启动，已登录机构账号。main.py 直接 CDP 连接。
  - **自动启动**（fallback）：如果 main.py 连接失败，会自动调用 `launch_browser()` 启动 Chromium。但自动启动使用独立临时 profile，**没有机构登录状态**，访问需要订阅的论文会失败。
- Elsevier 论文额外依赖 Foxit Reader（Print to PDF 虚拟打印机）。
- Python 依赖：`playwright`, `pyautogui`, `requests`, `pyyaml`, `rich`, `pyzotero`。首次使用运行 `<skill-base>/setup.bat`。
- 所有命令设置 `PYTHONIOENCODING=utf-8` 避免 Windows GBK 编码问题。
- 支持的出版商由 `<skill-base>/url_parser.py` 的 `PUBLISHER_PATTERNS` 自动匹配。
- 下载失败时，先根据错误信息判断是运行时问题还是出版商适配器问题，再决定排查路径。
- **图片引用提取**：用户发来 PPT 拍照、截图等图片时，先调 `ocr_citation.py` 提取引用，再根据用户意图走下载或 Zotero 流程。
- `ocr_citation.py` 依赖 DeepSeek Vision API（`http://127.0.0.1:3000`）。如果服务未运行，先加载 `deepseek_vision` skill 启动它。
- **OCR DOI 和 CrossRef 匹配都不可全信**：DeepSeek Vision 读出的 DOI 可能不准，`ocr_citation.py` 会用 CrossRef 验证。但 CrossRef 在 OCR 只提供了作者+期刊+年份（无标题、无摘要）时，也可能匹配到完全无关的论文（如已将 `Freudiger et al., Science, 2008` 匹配到 archaeological 论文，`crossref_score` 仅 23.44）。**不要无条件信任 CrossRef**。检查 `crossref_score`：score < 30 或匹配标题明显不相关时，用 OCR 读到的原始文本（作者+期刊+年份）手动搜索正确 DOI，不要盲信 CrossRef 的匹配。CrossRef 的 score 在 0-100 区间，高分（>80）可信，低分（<30）需要人工核实。
- **OCR DOI 与 CrossRef DOI 分歧时的验证**：当 OCR 读到的 DOI（如 `10.1038/s41377-025-01715-w`）与 CrossRef 匹配的 DOI（如 `10.1038/s41377-025-01895-x`）不同时，**分别用 CrossRef API 查询两个 DOI**。OCR 的 DOI 可能完全不存在于 CrossRef（字符识别错误），CrossRef 的 DOI 标题可能对但作者对不上（匹配到了同标题的不同论文）。最终以标题 + 作者 + 期刊三方匹配的 DOI 为准。
- **`-people` 子命令**：给定 Google Scholar Profile URL，批量抓取、下载某学者的全部论文并生成结构化文献消化报告。四阶段流水线：Scholar 抓取 → DOI 匹配 → 批量下载 → 消化模板生成。设计文档+实测笔记见 `references/people-feature-design.md`，核心方法论见 Cross-Talk Workflow 段落。

# 工作流程

## Step 1：判定任务类型

根据用户请求判断走哪条路径：

| 用户意图 | 命令入口 | 路径 |
|---------|---------|------|
| `-people`、收集某学者所有论文、批量下载某人的文章 | `people.py` | Step 2d：人物处理 |
| `-retry`、重试失败下载 | `people.py --retry` | Step 2d |
| `-download`、下载论文、批量下载 | `main.py` | Step 2a：执行下载 |
| 下载失败、报错、找不到按钮 | `main.py --debug` | Step 2b：排查修复 |
| 支持新出版商、URL 不认识 | 手动 | Step 2c：添加出版商 |
| `-paper`、做全套 | `zot.py` | Step 3：全套工作流 |
| `-zot`、只加 Zotero | `zot.py --no-download` | Step 4：仅 Zotero |
| 图片提取引用、PPT 文献 | `ocr_citation.py` | Step 5：图片→引用 |
| `-qr`、二维码、QR code | `generate_qr.py` | Step 6：生成 QR 码 |
| `-pdf`、找 PDF、论文文件 | 文件搜索 | Step 7：查找 PDF |

如果意图不明确（如"这个怎么下载不了"），优先走排查路径。

## Step 2a：执行下载

1. **单篇下载**：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/main.py" "URL或DOI"
   ```
   如果需要自动启动 Chromium：加 `--launch-browser`（临时 profile 无登录状态）。
2. **批量下载**：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/main.py" --input urls.txt
   ```
   ⚠️ **批量/单篇下载必须设 timeout**。`main.py` 被 `zot.py` 通过 `subprocess.run()` 调用时，无 timeout 会导致出版商页面卡住→进程永久挂起→大量 token 白费。`zot.download_pdf()` 接受 `timeout=120`，超时后自动抛异常继续下篇。
3. **指定输出目录**：加 `--output <目录>`。
4. **调试模式**：加 `--debug` 查看详细日志。
5. **跳过 warmup**（批量场景）：加 `--no-warmup` 节省 ~15s/篇。Chromium 已稳定时 warmup 多余。
6. 下载完成后确认：文件存在、大小 > 100KB、是有效 PDF（`%PDF` 头）。

## Step 2b：排查修复

**最重要：先查 `error_log.md`，再看代码。** error_log 按出版商分类记录了历史踩坑和解决方案，多数 "下载失败" 问题在里面都有答案。不要跳过这一步直接读源码。

1. 先搜 `error_log.md` 中该出版商的条目（如 `## ACS Publications` 段落），看是否有匹配的错误模式和解决方案。
2. 先用 `--debug` 重跑：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/main.py" "<失败URL>" --no-warmup --debug
   ```
3. 根据错误阶段判断：
   - 运行时错误（超时、导航失败）→ 检查 Chrome 是否启动、网络
   - 出版商页面结构变化 → 读 `<skill-base>/references/maintain.md` 流程 A
   - "Access denied" 但实际有订阅 → 查 error_log 中 `check_access` 误报条目（E-AAAS-01、E-SPRINGER-01 等），大概率是基类文本匹配误报，需要给该出版商 adapter 加 `check_access()` 覆盖
4. 深度调试需要理解代码机制时，读 `<skill-base>/references/architecture.md`。
5. 具体出版商出 bug 时，读 `<skill-base>/publisher/<name>.py` 顶部 docstring。

## Step 2c：添加新出版商

1. 读 `<skill-base>/references/maintain.md` **流程 B**，按完整流程执行。
2. 核心原则：**必须用 Playwright CDP 探测页面**，不能只靠手动 DevTools。
3. 探测结果判断下载类型，选对应适配器模板。
4. 创建适配器后，在 `<skill-base>/main.py` 注册、在 `<skill-base>/url_parser.py` 添加 URL 模式。
5. 用真实 Chrome 测试。

### 适配器 API 注意事项（常见 bug）

- **`find_download_url(self, page)` 签名**：base 类方法是 `def find_download_url(self, page) -> str | None`，只有一个额外参数 `page`。**不要写成 `(self, page, element)`**。如果适配器需要从 meta tag 或构造 URL 提取 PDF 链接（而非从 DOM element 取 href），直接覆盖 `find_download_url(self, page)`，返回绝对 URL。同时让 `find_download_element()` 返回 `None` 以避免 base 类调用 `element.get_attribute("href")` 报错。
- **OA 出版商的 `check_access`**：base 类的默认 `check_access()` 检查页面是否有 \"Access denied\" 等文本，这对 OA 期刊是误报。OA 适配器必须覆盖 `check_access(self, page) -> bool` 返回 `True`。见于 JCI Insight、bioRxiv/medRxiv。
- **`url_parser.py` 正则模式**：`PUBLISHER_PATTERNS` 中的 regex 用 `\.`（单反斜杠转义 dot）。在原始字符串 `r"domain\.org"` 中 `\.` 匹配字面 dot。多级子域名用 `r"sub\.domain\.org"`。

## Step 2d：人物处理（`-people`）

给定 Google Scholar Profile URL，抓取某学者的全部论文、下载、生成消化报告。

**前提**：Edge/Chrome 需先通过 `chromium_helper.launch_browser()` 启动，或已手动打开（`--remote-debugging-port=19222`）。

1. **完整流程**（抓取+DOI+下载+模板）：
   ```bash
   set PYTHONIOENCODING=utf-8 && python \"<skill-base>/people.py\" \"SCHOLAR_URL\" --download
   ```
2. **仅抓取**（测试用，不下载）：
   ```bash
   python \"<skill-base>/people.py\" \"SCHOLAR_URL\" --scrape-only
   ```
3. **断点续传下载**（已有 papers.json）：
   ```bash
   python \"<skill-base>/people.py\" --download-only --scholar-name \"学者名\"
   ```
4. **仅生成消化模板**（已有 papers.json）：
   ```bash
   python \"<skill-base>/people.py\" --template-only --scholar-name \"学者名\"
   ```
5. **限制篇数测试**：
   ```bash
   python "<skill-base>/people.py" "URL" --scrape-only --max-papers 5
   ```
6. **第二轮重试**（加载已有数据，重试失败论文）：
   ```bash
   python "<skill-base>/people.py" --retry --scholar-name "学者名"
   ```

**处理流程**：
  - Phase 1: Playwright CDP 抓取 Scholar Profile → 过滤专利/会议 → 去重 preprint/正式版
  - Phase 1b: CrossRef 搜索标题匹配 DOI（排除补充材料 `.sNNN`，preprint 降权）
  - Phase 1c: 作者数据库构建 — 从 CrossRef 提取每篇论文的通讯作者全名、affiliation、已知缩写，存入 `people/data/authors_db.json`（跨 session 持久累积）
  - Phase 2: 在 Zotero 创建 `People/<学者名>` collection
  - Phase 3: 按年份先后线性下载（默认关闭，需 `--download` 启用）
  - Phase 4: 生成文献消化模板（4 Block + ⚡ cross-talk 区）

**批量下载策略**：默认关闭（`--download` 显式启用）。建议 cron 线性下载（10-15min/篇），用 `--download-only` 做断点续传。一次性大量下载会触发出版商 access 封禁。

**关键陷阱**：
  1. **`subprocess.run()` 必须加 timeout**（`zot.py` 的 `download_pdf()`）。
     - 不加 timeout，出版商页面卡住（如 Wiley 加载 2min+）→ 整个 batch 永久挂起 → 浪费大量 token。
     - 修复：传 `timeout=120`。调用时通过 `people.py` → `zot.download_pdf(url, cfg, timeout=120)` 传递。
     - 超时后 `raise RuntimeError`，`download_one_paper` 的 `except` 捕获后标记 `dl_status=failed` 继续下篇。
  2. **每篇下载后必须保存进度**（`download_batch` 的 `save_callback` 参数）。
     - 不保存 → 进程被 kill 后全部重来。
     - 实现：调用方传 `save_callback=lambda papers: save_papers(...)`，每篇后自动 JSON 落盘。
     - 重跑时 `resume=True` 跳过 `dl_status=success` 的篇。
  3. **`--no-warmup` 加速**：单篇下载加 `--no-warmup` 跳过 Chromium 热身（节省 ~15s/篇）。
     - `zot.py` 的 `download_pdf()` 调用 `main.py` 时默认带 warmup。批量场景下 Chromium 已稳定，warmup 多余。
     - 可改 `cmd` 加 `--no-warmup` 参数提速。
  4. **DOI 解析失败（RSC `RemoteDisconnected`）**：
     - `resolve_doi()` 用 `requests.head()` → RSC/pubs.rsc.org 拒绝 HEAD 连接。
     - 已在 `url_parser.py` 改为 `requests.get()` + 浏览器 UA header。
     - 如果新增出版商类似问题，先检查 `resolve_doi()` 是否用 HEAD，换 GET 重试。
  5. **Scholar 截断作者 `...` 破坏 Zotero API**：
     - Scholar 抓取的 `authors` 字符串结尾有 `, ...`，`add_to_zotero()` 会创建 `lastName="..."` 的 creator。
     - Zotero API 400: `'firstName' creator field must be set if 'lastName' is set`。
     - 修复：`download_one_paper` 过滤 `[a for a in raw if a and a != "..." and len(a) > 1]`。

  6. **第二轮重试：`--retry`**（`people.py`）。加载已有 papers.json，对第一轮失败的论文自动分类处理：
     - SPIE 会议（DOI `10.1117/12.`）→ 标记 `conference` 不再重试
     - 超时失败 → 用 180s timeout 重试
     - "did not produce PDF" → 重试（可能因新适配器已就绪而成功）
     - 每篇重试后自动保存进度
     ```bash
     python "<skill-base>/people.py" --retry --scholar-name "学者名"
     ```

  7. **配置 path 注意**：`config.yaml` 被 gitignore，clone 后需手动修正 `temp_dir` 和 `storage_path` 中的用户名。用 `sed` 或 Python 批量替换。

**已知不支持/易失败的出版商**（按文献收集时的经验）：
  - **SPIE** (`spiedigitallibrary.org`) — 页面加载极慢，经常 120s timeout。会议论文（DOI 前缀 `10.1117/12.`）居多，已在 `CONFERENCE_KEYWORDS` + `--retry` 中自动过滤。
  - **Elsevier ScienceDirect** (`sciencedirect.com`) — 部分页面 120s timeout；依赖 Foxit Reader 虚拟打印，更慢。需要机构登录。
  - **Nature Microbiology / Nature 子刊** — 需要机构登录才能下载。NPG 适配器识别正常但 check_access 无订阅则失败。
  - **Communications Chemistry 等 Springer Nature 子刊** — 适配器偶发失败（页面结构差异），重现后需 CDP 探测修复。

**过滤规则**：默认排除 Patent + 会议（领域内会议不重要）。会议匹配关键词见 `CONFERENCE_KEYWORDS`（`people.py`）。如果遗漏新会议，在 `CONFERENCE_KEYWORDS` 列表追加。SPIE 会议也可按 DOI 前缀 `10.1117/12.` 识别（`retry_failed()` 中自动处理）。

**注意事项**：
  - Scholar Profile 页面渲染需要 3-5 秒，`page_delay: 3000` 足够
  - 每页 20 条，`Show More` 按钮 disabled 时全部加载完毕
  - 论文从旧到新排序（年序）
  - 下载前确保 Edge/Chrome 已启动（`chromium_helper.launch_browser()`）

**`-people` 故障排查**：

| 问题 | 原因 | 解决 |
|------|------|------|
| DOI resolve 失败（如 RSC `RemoteDisconnected`） | 部分出版商（RSC）拒绝 `requests.head()` | 已在 `url_parser.py` 修复为 `GET` + 浏览器 UA。如新增出版商类似问题，先查 `resolve_doi()` 是否用 HEAD |
| Zotero API `'firstName' field must be set` | Scholar 截断作者 `...` 传入 `add_to_zotero()` | `people.py` 的 `download_one_paper()` 已自动过滤 `...` 和单字符作者 |
| 论文抓取后数量不对 | `CONFERENCE_KEYWORDS` 漏了该会议 | 在 `people.py` 的 `CONFERENCE_KEYWORDS` 列表追加会议关键词 |
| `config.yaml` 路径不匹配 | gitclone 后路径中的用户名不同 | 手动修正 `temp_dir` 和 `storage_path` 中的用户名。config.yaml 被 gitignore 不跟踪 |
| CDP 连接失败 | Edge 未启动或端口不对 | 先运行 `chromium_helper.launch_browser()` 或手动 `start_browser.bat` |
| **批量下载永远跑不完**（进程挂起） | `subprocess.run()` 无 timeout，出版商页面卡住 | 已在 `zot.download_pdf()` 加 `timeout=120` 参数。调用方通过 `zot.download_pdf(url, cfg, timeout=120)` 传入。超时后自动 `raise RuntimeError`，`download_one_paper` 捕获并标记 `failed` 继续下篇 |
| PDF 下载失败率高（SPIE、bioRxiv 等） | 部分出版商无适配器或页面结构变化 | 查看 SKILL.md 的「已知不支持/易失败的出版商」列表。SPIE 可直接在 `CONFERENCE_KEYWORDS` 中过滤掉 |
| **批量下载有失败项** | 部分出版商超时或无订阅 | 用 `--retry` 启动第二轮重试：SPIE 自动按 DOI 过滤，timeout 的用 180s 重试，新增的适配器自动生效 |

## Step 3：全套工作流（`-paper`）

**前提**：`<skill-base>/config.yaml` 中的 `zotero` 部分已配置（API key + library ID）。

1. **执行命令**：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/zot.py" "出版商URL"
   ```
2. 脚本自动执行五步：去重检查 → 元数据提取 → PDF 下载 → 创建 Zotero 条目 → 挂载 PDF
3. **不需要手动提供 DOI**。脚本自动从页面提取 DOI 并通过 CrossRef API 补全元数据。
4. 成功后输出机器可读行：
   ```
   ZOT_RESULT: zot_key=XXXXXXXX|att_key=YYYYYYYY|local_pdf=C:\...\paper.pdf|title=Paper Title
   ```
5. 即使 PDF 下载失败，也会先创建 Zotero 条目（保存元数据）。
6. **生成 QR 码**：从输出中提取 DOI，运行：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/generate_qr.py" "<DOI>"
   ```
   生成 QR 码保存到 `<skill-base>/download/temp/<DOI>.png`。

## Step 4：仅 Zotero（`-zot`）

**前提**：`<skill-base>/config.yaml` 中的 `zotero` 部分已配置。

1. **执行命令**：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/zot.py" --no-download "出版商URL"
   ```
2. 跳过 PDF 下载，只做：去重检查 → 元数据提取 → 创建 Zotero 条目
3. 成功后输出机器可读行（无 `att_key` 和 `local_pdf`）：
   ```
   ZOT_RESULT: zot_key=XXXXXXXX|title=Paper Title
   ```

### Zotero 故障排查

| 问题 | 解决 |
|------|------|
| `config.yaml not found` | 确保 config.yaml 存在且填入了 zotero 部分 |
| `zotero.{key} not configured` | 填入真实 Zotero API key 和 library ID |
| `403 / Write access denied` | API key 需要写权限 |
| PDF 下载失败 | 检查 Chromium 是否启动、出版商是否支持 |

## Step 5：图片引用提取

**前提**：DeepSeek Vision API 服务在 `http://127.0.0.1:3000` 运行。如果未运行，先加载 `deepseek_vision` skill 启动。

1. **执行命令**：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/ocr_citation.py" "<图片路径>" --json
   ```
2. 脚本自动：DeepSeek Vision OCR → 解析引用 → CrossRef 确认 DOI
3. 输出 JSON 格式的引用列表，每条包含 `crossref_doi` 和 `crossref_title`
4. 拿到 DOI 后，根据用户意图走 Step 2a（下载）或 Step 3（全套）或 Step 4（仅 Zotero）
5. **批量图片**：对每张图片分别运行 `ocr_citation.py`，收集所有 DOI 后统一处理

### 图片引用故障排查

| 问题 | 解决 |
|------|------|
| `DeepSeek Vision API` 连接失败 | 检查 `http://127.0.0.1:3000/health`，未运行则加载 `deepseek_vision` skill 启动 |
| OCR 没有识别出引用 | 图片可能模糊或引用不完整，尝试 `--json` 看原始输出 |
| `CrossRef 找不到匹配或匹配明显错误` | OCR 标题可能有误，用 OCR 原文手动搜索。检查 `crossref_score`：<30 时匹配不可信，用 OCR 的原始作者+期刊+年份搜索正确 DOI |
| `browser closed` error | 重启 DeepSeekWeb2API 服务 |

## Step 6：生成 QR 码（`-qr`）

给定 DOI，生成指向 `https://doi.org/<DOI>` 的 QR 码图片。

1. **执行命令**：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/generate_qr.py" "<DOI>"
   ```
2. 输出：`<skill-base>/download/temp/<DOI_slug>.png` 的绝对路径
3. 可选 `--output <目录>` 指定输出目录
4. DOI 格式自动处理：`10.1039/d1an00412c`、`https://doi.org/10.1039/d1an00412c` 均可

## Step 7：查找并发送 PDF（`-pdf`）

根据 DOI、标题关键词或文件名在下载目录中查找已有的 PDF 文件，然后发送给用户。

1. **搜索范围**（按优先级）：
   - `C:\Users\Ivanz\Downloads\temp`（用户默认下载文件夹，优先搜）
   - `<skill-base>/download/`（skill 自己的下载目录）
2. 用 `search_files` 工具按文件名或内容搜索
3. **发送文件**：在回复末尾单独一行写 `MEDIA:<pdf绝对路径>`（注意是英文冒号，路径不含空格）。示例：
   ```
   MEDIA:C:\Users\Ivanz\OneDrive\Hermes_workspace\Literature_skill\download\10.1039_d1an00412c.pdf
   ```
   Gateway 会自动检测 `MEDIA:` 标签并调用平台的原生文件发送方法（微信→`send_document`，Telegram→`send_document`）。
4. **CLI 模式**：如果用户在 CLI（非 gateway），`MEDIA:` 标签不会被处理，只需报告文件路径即可。
5. **多个 PDF**：可以写多行 `MEDIA:`，每行一个文件。
6. **PDF 不存在**：只报告路径，不发 `MEDIA:` 标签。
7. **QQ 平台限制**：QQ gateway 不支持 `MEDIA:` 文件发送（仅 telegram/discord/matrix/weixin/signal/yuanbao/feishu 支持）。在 QQ 上发送 PDF 需用 `send_message(action='send', target='qqbot', message='MEDIA:<path>')` 测试，若失败则告知用户文件路径自行打开。

## Step 8：填充文献消化模板

`-people` 的 Phase 4 生成模板后，由 agent 手动填充 4 个 Block。模板在 `people/digests/<name>_digest.md`。

### 作者名解析规则（Block 2 合作者表必用）

Scholar 抓取的作者名是缩写（如 `KMC Wong`、`JX Cheng`），**绝对不能脑补展开**（曾将 Keith Man-Chung Wong 错写成 Kenneth MC Wong）。填充 Block 2 合作者表时，必须按以下优先级解析全名：

1. **CrossRef 查询**（最可靠）：用论文 DOI 调 `fetch_crossref_authors(doi)` 拿完整作者列表。CrossRef 的 `given` + `family` 是全名。
2. **本地作者数据库**（`people/data/authors_db.json`）：调 `resolve_author_name(abbrev, doi, db)`，自动走 CrossRef→DB→dirty 流程。DB 只存通讯作者，跨 session 持久累积。
3. **dirty 标记**：CrossRef 和 DB 都找不到 → 保留缩写原样，标 `dirty=True`。不要猜测全名。

**调用方式**：
```python
from people import resolve_author_name, load_authors_db
db = load_authors_db()
full_name, is_dirty = resolve_author_name("KMC Wong", "10.1039/c6cc03431d", db)
# → ("Keith Man-Chung Wong", False)
```

**已处理的坑**：
- CrossRef 返回的连字符有 unicode 变体（`‐` U+2010 vs `-` U+002D），`_normalize_abbrev()` 已统一处理
- 连字符姓名缩写：`Man-Chung` → `MC`（不是 `M`），代码会同时记录 `KMC Wong` 和 `KM Wong` 两种缩写
- DB 只记录通讯作者（CrossRef `sequence=corresponding`，否则取末位作者）

### 三圈螺旋工作流

由于 4 个 Block 之间存在耦合（合作者影响研究方向、综述定义阶段划分、高引论文定义起点），不能线性 1→2→3→4。用三圈螺旋：

```
第一圈：鸟瞰（Skeleton Pass）
  → 通读标题+摘要
  → 同时搭 4 个 Block 的骨架
  → 建统一时间线（research_objects, core_methods, key_collaborators）

第二圈：深读（Deep-Read Pass）
  → 先读综述（建理解框架）
  → 再读高引论文（理解核心贡献）
  → 补读关键节点论文
  → 每篇发现跨 Block 关系 → 打 ⚡ 标记，不跳走

第三圈：整合（Integration Pass）
  → 回头处理所有 ⚡ 标记
  → 完善 Block 1 的时间线和 Block 2 的合作者网络
  → 检查时间一致性
```

### 统一时间线

所有 Block 共享时间线。发现跨 Block 关联时（如 Block 2 发现新合作者在 2019 年引入了 SRS），不仅更新 Block 2 也更新 Block 1 的方法论转折点。

### ⚡ 标记规则

深读时发现跨 Block 关联 → 只打标记，保持当前阅读流：

```markdown
⚡ → Block 1: 合作者 XXX (2019-) 引入 SRS 方法，
   需在 Block 1 方法论转折点中补充
```

处理时机：当前 Block 填完后，批量处理所有积累的 ⚡ 标记。

# 支持的出版商（25 家）

| 出版商 | 域名示例 |
|--------|---------|
| AAAS (Science) | science.org |
| ACS Publications | pubs.acs.org |
| AIP (Silverchair) | pubs.aip.org |
| Annual Reviews | annualreviews.org |
| APS (Physical Review) | journals.aps.org |
| **bioRxiv / medRxiv** | **biorxiv.org, medrxiv.org** |
| BMJ | bmj.com |
| eLife | elifesciences.org |
| Elsevier (ScienceDirect) | sciencedirect.com |
| Frontiers | frontiersin.org |
| IEEE | ieeexplore.ieee.org |
| IOP Publishing | iopscience.iop.org |
| **JCI Insight** | **insight.jci.org** |
| MDPI | mdpi.com |
| Nature Publishing Group | nature.com |
| Optica (OSA) | opg.optica.org |
| PNAS | pnas.org |
| Royal Society | royalsocietypublishing.org |
| RSC (Royal Society of Chemistry) | pubs.rsc.org |
| SPIE | spiedigitallibrary.org |
| Springer / SpringerLink | springer.com, link.springer.com |
| Taylor & Francis | tandfonline.com |
| Wiley | onlinelibrary.wiley.com |
