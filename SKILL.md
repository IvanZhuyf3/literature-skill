---
name: literature-skill
description: |
  学术文献一站式工具。主命令 `/literature-skill`，子命令作为参数传入：
  - `/literature-skill -paper <DOI/URL>` → 做全套：下载 PDF + 生成 QR 码 + 提取元数据 + 添加到 Zotero + 挂载附件。
  - `/literature-skill -download <DOI/URL>` → 只下载论文 PDF，不涉及 Zotero。
  - `/literature-skill -pdf <DOI/关键词>` → 查找已下载的 PDF 文件路径，通过微信/Telegram 发送文件。
  - `/literature-skill -qr <DOI>` → 根据 DOI 生成 QR 码图片（指向 https://doi.org/xxx）。
  - `/literature-skill -zot <DOI/URL>` → 只加进 Zotero：提取元数据 + 创建条目 + 挂载 PDF（不触发下载）。
  - `/literature-skill -people <Scholar_URL>` → 批量下载某人全部论文 + 结构化文献消化报告。
  也支持从图片（PPT 拍照、截图）提取引用再走上述流程。触发词："extract citations from image", "这个图里的文献", "图片引用"。
  自然语言同义词也会触发："download paper", "get PDF", "fetch paper", "下载论文", "抓取论文", "批量下载" 走下载路径；"add to zotero", "save paper", "import paper", "收藏论文" 走 Zotero 路径；"二维码", "QR code" 走 QR 路径。
allowed-tools: Bash(uv:*), Bash(python:*), Bash(node:*)
---

# 规则

- 把当前 `SKILL.md` 所在目录视为 `<skill-base>`。所有本地资源从 `<skill-base>` 解析，不依赖调用方工作目录。
- **功能入口**（子命令作为参数传入 `/literature-skill`）：
  - `-paper` → `python "<skill-base>/zot.py"` — 全套
  - `-zot` → `python "<skill-base>/zot.py" --no-download` — 仅 Zotero
  - `-download` → `python "<skill-base>/main.py"` — 仅下载
  - `-qr` → `python "<skill-base>/generate_qr.py"` — 生成 QR 码
  - `-pdf` → 文件搜索查找已下载的 PDF
- **Chromium 启动**：推荐手动启动（有机构登录状态，`--remote-debugging-port=19222`）。main.py 的 fallback `launch_browser()` 使用独立临时 profile，**无机构登录状态**。
- Elsevier 论文额外依赖 Foxit Reader（Print to PDF 虚拟打印机）。
- Python 依赖：`playwright`, `pyautogui`, `requests`, `pyyaml`, `rich`, `pyzotero`。首次使用运行 `<skill-base>/setup.bat`。PDF 解析额外依赖 MinerU API（`config.yaml` 配置 token，无需额外安装）。
- 所有命令设置 `PYTHONIOENCODING=utf-8` 避免 Windows GBK 编码问题。
- 支持的出版商由 `<skill-base>/url_parser.py` 的 `PUBLISHER_PATTERNS` 自动匹配。
- 下载失败时，先查 `<skill-base>/error_log.md` 该出版商的条目，再用 `--debug` 重跑。深度调试读 `<skill-base>/references/architecture.md`。
- **OCR DOI 和 CrossRef 匹配都不可全信**。检查 `crossref_score`：<30 时匹配不可信，需用 OCR 原文手动搜索正确 DOI。两个 DOI 冲突时，分别查 CrossRef，以标题+作者+期刊三方匹配为准。
- 图片引用提取走 `ocr_citation.py`（依赖 DeepSeek Vision API `http://127.0.0.1:3000`）。
- PDF 结构化解析走 `pdf_parser.py`（依赖 MinerU online API，需 `config.yaml` 的 `mineru.token`）。

# 工作流程

## Step 1：判定任务类型

| 用户意图 | 命令入口 | 路径 |
|---------|---------|------|
| `-people`、收集某学者所有论文 | `people.py` | Step 2d |
| `-retry`、重试失败下载 | `people.py --retry` | Step 2d |
| `-download`、下载论文 | `main.py` | Step 2a |
| 下载失败、报错 | `main.py --debug` | Step 2b |
| 支持新出版商 | 手动 | Step 2c |
| `-paper`、全套 | `zot.py` | Step 3 |
| `-zot`、仅 Zotero | `zot.py --no-download` | Step 4 |
| 图片提取引用 | `ocr_citation.py` | Step 5 |
| `-qr`、二维码 | `generate_qr.py` | Step 6 |
| `-pdf`、找 PDF | 文件搜索 | Step 7 |
| `-parse`、解析 PDF | `pdf_parser.py` | Step 9 |

## Step 2a：执行下载

1. **单篇**：`set PYTHONIOENCODING=utf-8 && python "<skill-base>/main.py" "URL"`（加 `--launch-browser` 自动启动 Chromium）
2. **批量**：`set PYTHONIOENCODING=utf-8 && python "<skill-base>/main.py" --input urls.txt`
3. **加速**：批处理加 `--no-warmup` 省 ~15s/篇；加 `--output <dir>` 指定目录；`--debug` 看日志
4. **⚠️ timeout**：`zot.download_pdf()` 必须传 `timeout=120`，否则卡死浪费 token。超时自动抛异常继续下篇。
5. 验证：文件存在、> 100KB、`%PDF` 头。

## Step 2b：排查修复

**先查 `error_log.md`**，再用 `--debug` 重跑。根据错误判断：运行时错误（超时/导航）→ 检查 Chrome；页面结构变化 → 读 `references/maintain.md` 流程 A；"Access denied" 但有订阅 → 查 `error_log` 中 `check_access` 误报条目。

## Step 2c：添加新出版商

1. 读 `references/maintain.md` **流程 B** 完整执行
2. 必须用 Playwright CDP 探测页面，不能只靠 DevTools
3. 创建适配器后注册到 `main.py` + `url_parser.py`
4. **常见 bug**：`find_download_url(self, page)` 签名不能多参数；OA 出版商必须覆盖 `check_access()` 返回 `True`（JCI Insight、bioRxiv）；`url_parser.py` 正则用 `\\.` 转义 dot

## Step 2d：人物处理

【新推荐】`zotero_attach.py` — 独立模块，读 Zotero 文件夹补缺失 PDF（人机合作流程 Phase 3）

```bash
# 直接使用
python "<skill-base>/zotero_attach.py" --collection "学者名"
python "<skill-base>/zotero_attach.py" --collection "学者名" --max-papers 5

# 也支持通过 people.py 调用（薄封装）
python "<skill-base>/people.py" --attach-missing --scholar-name "学者名"
```

详见下方「人机合作推荐流程」。

1. Agent：`--scrape-only` → 抓取 Scholar profile
2. Agent：`--register-only` → 批量注册到 Zotero（纯 CrossRef 元数据，~0.7s/篇，不下载 PDF）
3. **你**：在 Zotero 中清洗数据（删不相关、修元数据、去重、补遗漏）
4. Agent：`--attach-missing --scholar-name "学者名"` → 读取 Zotero 文件夹，下载并挂载缺 PDF 的条目
5. Agent：`--template-only --scholar-name "学者名"` → 生成消化模板

详见 `references/people-guide.md`「人机合作推荐流程」。

CLI 速查：
```bash
# 人机合作流程
python "<skill-base>/people.py" "SCHOLAR_URL" --scrape-only      # 1. 抓取
python "<skill-base>/people.py" --register-only --scholar-name "X"  # 2. 注册
# → 你清洗 Zotero →
python "<skill-base>/people.py" --attach-missing --scholar-name "X"  # 4. 补PDF
python "<skill-base>/people.py" --template-only --scholar-name "X"   # 5. 消化

# 旧版全自动（Scholar 干净时可用）
python "<skill-base>/people.py" "SCHOLAR_URL" --download         # 全套
python "<skill-base>/people.py" --download-only --scholar-name "X"  # 断点续传
python "<skill-base>/people.py" --retry --scholar-name "X"         # 重试
python "<skill-base>/people.py" --template-only --scholar-name "X"   # 仅模板
```

## Step 3：全套工作流（`-paper`）

**前提**：`config.yaml` 的 `zotero` 部分已配置。

```bash
set PYTHONIOENCODING=utf-8 && python "<skill-base>/zot.py" "URL"
```

自动：去重检查 → 元数据提取 → PDF 下载 → 创建 Zotero 条目 → 挂载 PDF。即使 PDF 下载失败也会先建条目。成功后输出 `ZOT_RESULT: zot_key=...|att_key=...|local_pdf=...|title=...`。从输出中提 DOI 走 Step 6 生成 QR 码。

## Step 4：仅 Zotero（`-zot`）

```bash
set PYTHONIOENCODING=utf-8 && python "<skill-base>/zot.py" --no-download "URL"
```

输出：`ZOT_RESULT: zot_key=...|title=...`

**故障排查**：`config.yaml not found` → 检查文件；`zotero.{key} not configured` → 填入 API key 和 library ID；`403 Write access denied` → API key 需要写权限。

## Step 5：图片引用提取

**前提**：DeepSeek Vision API 在 `http://127.0.0.1:3000` 运行。

```bash
set PYTHONIOENCODING=utf-8 && python "<skill-base>/ocr_citation.py" "<图片路径>" --json
```

自动：DeepSeek Vision OCR → 解析引用 → CrossRef 确认 DOI。拿到 DOI 后根据用户意图走 Step 2a/3/4。多张图分别跑后统一处理。

## Step 6：生成 QR 码（`-qr`）

```bash
set PYTHONIOENCODING=utf-8 && python "<skill-base>/generate_qr.py" "<DOI>"
```

输出：`<skill-base>/download/temp/<DOI_slug>.png`。DOI 格式自动处理（`10.xxx/yyy` 或 `https://doi.org/...` 均可）。

## Step 7：查找并发送 PDF（`-pdf`）

搜索 `C:\Users\Ivanz\Downloads\temp` 和 `<skill-base>/download/`，找到后通过 `MEDIA:<绝对路径>` 发送。支持多行 `MEDIA:`。QQ 平台不支持 MEDIA 文件发送。

## Step 8：填充文献消化模板

Phase 4 生成模板后，由 agent 手动填充。详细方法论见 `references/digest-workflow.md`。

**核心要点**：
- 作者名缩写**绝对不能脑补展开**（曾踩坑：KMC Wong→Kenneth MC Wong，实为Keith Man-Chung Wong）
- 解析优先级：CrossRef 查询 → 本地 `authors_db.json` → dirty 保留缩写
- 4 Block 非线性填充，用三圈螺旋工作流（鸟瞰→深读→整合）
- 跨 Block 关联打 ⚡ 标记，统一时间线

## Step 9：PDF 结构化解析（`-parse`）

**前提**：`config.yaml` 的 `mineru.token` 已填入（从 https://mineru.net/apiManage 获取）。

```bash
# 单篇解析 → stdout
set PYTHONIOENCODING=utf-8 && python "<skill-base>/pdf_parser.py" "<pdf_path>"

# 指定输出文件
python "<skill-base>/pdf_parser.py" "<pdf_path>" -o "<output.md>"

# 批量解析（模块调用）
# from pdf_parser import parse_pdf_batch
# results = parse_pdf_batch(["paper1.pdf", "paper2.pdf"])
```

输出：高质量 Markdown，保留表格结构、公式、阅读顺序、图表标注。结果按文件 SHA256 缓存在 `<skill-base>/cache/mineru/`，重复解析同文件直接返回缓存。

**用途**：digest 工作流的"深读"阶段——用解析后的 Markdown 替代人眼读 PDF，提取 methods/results 细节。不用于 abstract/元数据提取（那是 CrossRef + 页面 DOM 的任务）。

**API 配额**：免费 5000 页/天，单文件 ≤200 页/200MB。VLM 模型精度最高，pipeline 模型更快。

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
