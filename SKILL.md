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

# 新版 CLI（推荐）

```bash
python -m lit scholar <URL>           # 抓取 Scholar → 注册 Zotero
python -m lit scholar <URL> --scrape-only  # 仅抓取，不注册
python -m lit import <DOI/URL>         # 注册 Zotero → 自动快速下载 PDF（Sci-Hub CDP, ≤2021）
python -m lit import <image_path>      # 图片 OCR → 注册 Zotero → 自动快速下载
python -m lit pdf <DOI>                # 查本地 PDF → 没有则下载（输出文件路径）
python -m lit pdf <DOI> --no-download  # 仅查本地，不触发下载
python -m lit digest <collection>      # 读 Zotero → 生成消化报告
python -m lit maintain [--collection "Ji-Xin Cheng"] [--fix]  # 文件库健康检查与清理 + DOI索引刷新
python -m lit parse <pdf_path> [--output <md>] [--item-key <key>]  # MinerU 解析 + 可选 bibliography
python -m lit qr <DOI>                # 生成 QR 码
python -m lit download <DOI>           # [已废弃] 用 `lit import` 替代
```

旧版入口（`people.py`, `zot.py`, `main.py` 等）已弃用，但代码保留兼容。

# 规则

- 把当前 `SKILL.md` 所在目录视为 `<skill-base>`。所有本地资源从 `<skill-base>` 解析，不依赖调用方工作目录。
- **Zotero 是唯一数据源**。不再使用 `papers.json` 中间文件。所有状态读自 Zotero API。
- **Zotero 同步方式**：`config.yaml` 的 `zotero.sync_method` 控制附件挂载方式。`webdav`（推荐）：JSON API 建条目 + 本地拷文件，不消耗 Zotero 云配额。`cloud`：API multipart 上传（走配额）。`webdav` 会自动回退云模式遇到 413 quota 错误。详见 `references/webdav-setup.md`。
- **DOI 是稳定 key**：始终用 DOI 查找 Zotero 条目，不信任本地缓存的 key。
- **`lit.core.zotero.check_duplicate()` 内置去重**：按 DOI/URL/title 搜索，已存在则返回现有 key。所有调用路径都受益。
- **Chromium 启动**：推荐手动启动（有机构登录状态，`--remote-debugging-port=19222`）。`lit download` / `lit attach` 默认用 CDP 连接。
- Elsevier 论文额外依赖 Foxit Reader（Print to PDF 虚拟打印机）。
- Python 依赖：`playwright`, `pyautogui`, `requests`, `pyyaml`, `rich`, `pyzotero`。首次使用运行 `<skill-base>/setup.bat`。
- 支持的出版商由 `<skill-base>/url_parser.py` 的 `PUBLISHER_PATTERNS` 自动匹配。适配器在 `<skill-base>/download/adapters/`。
- 下载失败时，先查 `<skill-base>/error_log.md` 该出版商的条目。深度调试读 `<skill-base>/references/architecture.md`。
- **OCR DOI 和 CrossRef 匹配都不可全信**。检查 `crossref_score`：<30 时匹配不可信。

# 工作流程

## Step 1：判定任务类型

|| 用户意图 | 推荐命令 | 旧版（已弃用） |
||---------|---------|------------|
|| 收集某学者所有论文 | `lit scholar <URL>` | `people.py "URL" --scrape-only` |
|| 清洗后补缺 PDF | `lit attach <collection>` | `zotero_attach.py --collection "X"` |
|| 生成消化报告 | `lit digest <collection>` | `people.py --template-only --scholar-name "X"` |
|| **导入单篇（加 ref + 快速下载）** | `lit import <DOI/URL>` | 三步：import_ref → quick_download → attach_pdf |
|| **图片 OCR 导入** | `lit import <image_path>` | `ocr_citation.py <image>` |
|| 批量补缺 PDF | `lit attach <collection>` | 优先 Sci-Hub CDP，失败走出版商 adapter |
|| PDF 解析（带 bibliography） | `lit parse <pdf> --item-key <key>` | `pdf_parser.py <pdf_path>` |
|| 文件库体检/清理 | `lit maintain [--collection X] [--fix]` | 手动检查 |
|| 生成 QR 码 | `lit qr <DOI>` | `generate_qr.py <DOI>` |
|| 添加新出版商 | 手动 | 手动 |

## Step 2：下载排查 & 适配器

### 排查修复

**先查 `error_log.md`**。运行时错误（超时/导航）→ 检查 Chrome；页面结构变化 → 读 `references/maintain.md` 流程 A；"Access denied" 但有订阅 → 查 `error_log` 中 `check_access` 误报条目。

### 添加新出版商

1. 读 `references/maintain.md` **流程 B** 完整执行
2. 必须用 Playwright CDP 探测页面，不能只靠 DevTools
3. 创建适配器后注册到 `download/adapters/__init__.py` + `url_parser.py`
4. **常见 bug**：`find_download_url(self, page)` 签名不能多参数；OA 出版商必须覆盖 `check_access()` 返回 `True`（JCI Insight、bioRxiv）；`url_parser.py` 正则用 `\\.` 转义 dot

## Step 3：人机合作流程（大型学者）

推荐的 `-people` 工作方式——**分阶段执行，人在中间清洗数据**：

### Phase 1：Agent 自动 — 建文件夹 + 注册条目

```bash
python -m lit scholar "SCHOLAR_URL"
# 或分两步：
python -m lit scholar "URL" --scrape-only    # 仅抓取
python -m lit scholar "URL"                   # 抓取 + 注册
```

### 步骤 2：你手动清洗数据

在 Zotero `People/<学者名>` 文件夹中修元数据、删不相关、去重、补遗漏。

### Phase 3：Agent 继续 — 补 PDF + 解析 + 消化

```bash
python -m lit attach "学者名"              # 批量补缺 PDF（Sci-Hub CDP + 出版商 adapter）
python -m lit attach "学者名" --limit 5   # 先测5篇
python -m lit parse <pdf> --item-key <key>  # 解析 PDF + 加 bibliography 头
python -m lit digest "学者名"               # 生成消化报告
```

### 为什么不一把走完？

Scholar 数据很脏（截断作者名、专利/会议混入、重复），人机合作把清洗放中间，agent 只负责机械重复的工作。

## Step 4：旧版命令（兼容）

```bash
# 旧版入口仍可用，但会打印弃用警告
PYTHONIOENCODING=utf-8 python "main.py" "URL"           # 下载
PYTHONIOENCODING=utf-8 python "zot.py" "URL"            # Zotero
PYTHONIOENCODING=utf-8 python "people.py" "URL"         # 学者
PYTHONIOENCODING=utf-8 python "pdf_parser.py" "path"    # 解析
```

## 支持的出版商（25 家）

| 出版商 | 域名 |
|--------|------|
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
| RSC | pubs.rsc.org |
| SPIE | spiedigitallibrary.org |
| Springer / SpringerLink | springer.com, link.springer.com |
| Taylor & Francis | tandfonline.com |
| Wiley | onlinelibrary.wiley.com |

## 参考文档

| 文档 | 内容 |
|------|------|
| `references/architecture.md` | 代码架构、`lit/` 包结构、适配器详解 |
| `references/legacy.md` | 旧版入口参考（已弃用）|
| `references/maintain.md` | 添加/修复 publisher 流程模板 |
| `references/people-guide.md` | 人机合作流程详细说明 |
| `references/digest-workflow.md` | 消化模板填充方法论 |
|| `references/webdav-setup.md` | WebDAV 配置说明 |
|| `references/mineru-api.md` | MinerU PDF 解析 API 说明 |
|| `references/merge-notes.md` | 合并/PR 记录 |


