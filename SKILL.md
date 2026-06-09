---
name: literature-skill
description: |
  学术文献一站式工具。三个 slash 命令，精确匹配：
  - `/paper` → 做全套：下载 PDF + 提取元数据 + 添加到 Zotero + 挂载附件。
  - `/zot` → 只加进 Zotero：提取元数据 + 创建条目 + 挂载 PDF（不触发下载）。
  - `/paper download` → 只下载论文 PDF，不涉及 Zotero。
  自然语言同义词也会触发："download paper", "get PDF", "fetch paper", "下载论文", "抓取论文", "批量下载" 走下载路径；"add to zotero", "save paper", "import paper", "收藏论文" 走 Zotero 路径。
allowed-tools: Bash(uv:*), Bash(python:*)
---

# 规则

- 把当前 `SKILL.md` 所在目录视为 `<skill-base>`。所有本地资源从 `<skill-base>` 解析，不依赖调用方工作目录。
- **三个功能入口**：
  - `/paper` → `python "<skill-base>/zot.py"` — 全套：下载 PDF + 添加到 Zotero + 挂载
  - `/zot` → `python "<skill-base>/zot.py" --no-download` — 只加 Zotero：元数据 + 创建条目（不下载 PDF）
  - `/paper download` → `python "<skill-base>/main.py"` — 只下载 PDF
- **Chromium 启动有两种方式**（main.py 会自动处理）：
  - **已手动启动**（推荐，有机构登录状态）：用户用 `start_browser.bat` 或手动加 `--remote-debugging-port=9222` 启动，已登录机构账号。main.py 直接 CDP 连接。
  - **自动启动**（fallback）：如果 main.py 连接失败，会自动调用 `launch_browser()` 启动 Chromium。但自动启动使用独立临时 profile，**没有机构登录状态**，访问需要订阅的论文会失败。
- Elsevier 论文额外依赖 Foxit Reader（Print to PDF 虚拟打印机）。
- Python 依赖：`playwright`, `pyautogui`, `requests`, `pyyaml`, `rich`, `pyzotero`。首次使用运行 `<skill-base>/setup.bat`。
- 所有命令设置 `PYTHONIOENCODING=utf-8` 避免 Windows GBK 编码问题。
- 支持的出版商由 `<skill-base>/url_parser.py` 的 `PUBLISHER_PATTERNS` 自动匹配。
- 下载失败时，先根据错误信息判断是运行时问题还是出版商适配器问题，再决定排查路径。

# 工作流程

## Step 1：判定任务类型

根据用户请求判断走哪条路径：

| 用户意图 | 命令入口 | 路径 |
|---------|---------|------|
| `/paper download`、下载论文、批量下载 | `main.py` | Step 2a：执行下载 |
| 下载失败、报错、找不到按钮 | `main.py --debug` | Step 2b：排查修复 |
| 支持新出版商、URL 不认识 | 手动 | Step 2c：添加出版商 |
| `/paper`、做全套 | `zot.py` | Step 3：全套工作流 |
| `/zot`、只加 Zotero | `zot.py --no-download` | Step 4：仅 Zotero |

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
3. **指定输出目录**：加 `--output <目录>`。
4. **调试模式**：加 `--debug` 查看详细日志。
5. 下载完成后确认：文件存在、大小 > 100KB、是有效 PDF（`%PDF` 头）。

## Step 2b：排查修复

1. 先用 `--debug` 重跑：
   ```bash
   set PYTHONIOENCODING=utf-8 && python "<skill-base>/main.py" "<失败URL>" --no-warmup --debug
   ```
2. 根据错误阶段判断：
   - 运行时错误（超时、导航失败）→ 检查 Chrome 是否启动、网络
   - 出版商页面结构变化 → 读 `<skill-base>/references/maintain.md` 流程 A
3. 深度调试需要理解代码机制时，读 `<skill-base>/references/architecture.md`。
4. 具体出版商出 bug 时，读 `<skill-base>/publisher/<name>.py` 顶部 docstring。

## Step 2c：添加新出版商

1. 读 `<skill-base>/references/maintain.md` **流程 B**，按完整流程执行。
2. 核心原则：**必须用 Playwright CDP 探测页面**，不能只靠手动 DevTools。
3. 探测结果判断下载类型，选对应适配器模板。
4. 创建适配器后，在 `<skill-base>/main.py` 注册、在 `<skill-base>/url_parser.py` 添加 URL 模式。
5. 用真实 Chrome 测试。

## Step 3：全套工作流（`/paper`）

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

## Step 4：仅 Zotero（`/zot`）

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

# 支持的出版商（23 家）

| 出版商 | 域名示例 |
|--------|---------|
| AAAS (Science) | science.org |
| ACS Publications | pubs.acs.org |
| AIP (Silverchair) | pubs.aip.org |
| Annual Reviews | annualreviews.org |
| APS (Physical Review) | journals.aps.org |
| BMJ | bmj.com |
| eLife | elifesciences.org |
| Elsevier (ScienceDirect) | sciencedirect.com |
| Frontiers | frontiersin.org |
| IEEE | ieeexplore.ieee.org |
| IOP Publishing | iopscience.iop.org |
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
