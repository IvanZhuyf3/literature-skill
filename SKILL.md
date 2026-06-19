---
name: literature-skill
description: |
  学术文献一站式工具。主命令 `/literature-skill`，子命令作为参数传入：
  - `/literature-skill -paper <DOI/URL>` → 做全套：下载 PDF + 生成 QR 码 + 提取元数据 + 添加到 Zotero + 挂载附件。
  - `/literature-skill -pdf <DOI/关键词>` → 查找已下载的 PDF 文件路径，通过微信/Telegram 发送文件。
  - `/literature-skill -qr <DOI>` → 根据 DOI 生成 QR 码图片（指向 https://doi.org/xxx）。
  - `/literature-skill -zot <DOI/URL>` → 只加进 Zotero：提取元数据 + 创建条目 + 挂载 PDF（不触发下载）。
  - `/literature-skill -people <Scholar_URL>` → 批量下载某人全部论文 + 结构化文献消化报告。
  也支持从图片（PPT 拍照、截图）提取引用再走上述流程。触发词："extract citations from image", "这个图里的文献", "图片引用"。
  自然语言同义词也会触发："download paper", "get PDF", "fetch paper", "下载论文", "抓取论文", "批量下载" 走下载路径；"add to zotero", "save paper", "import paper", "收藏论文" 走 Zotero 路径；"二维码", "QR code" 走 QR 路径。
allowed-tools: Bash(uv:*), Bash(python:*), Bash(node:*)
---

# CLI 命令

```bash
# === 注册（不下载 PDF）===
python -m lit scholar <URL>           # 抓取 Scholar → 批量注册 Zotero
python -m lit import <DOI/URL>        # 单篇注册 Zotero（DOI / URL / 图片 OCR）
python -m lit import <image_path>     # 图片 OCR → 注册 Zotero

# === 快速下载（Sci-Hub + OA 源，秒级，~50% 成功率）===
python -m lit quick <DOI>             # 单篇：查缺口 → Sci-Hub 下载 → 挂载
python -m lit quick <collection>      # 批量：遍历 collection 缺 PDF 的条目
python -m lit quick <collection> --limit 5

# === Publisher adapter 兜底（分钟级，覆盖 Sci-Hub 拿不到的）===
python -m lit attach <DOI>            # 单篇：查缺口 → 出版商页面下载 → 挂载
python -m lit attach <collection>     # 批量
python -m lit attach <collection> --limit 5

# === 查找本地 PDF ===
python -m lit pdf <DOI>               # 查本地 PDF 路径（不下载）

# === 其他 ===
python -m lit digest <collection>     # 首次生成消化模板（全量）
# 增量更新 digest 不用命令——agent 读已有 digest.md → diff Zotero → 手术式更新
python -m lit parse <pdf> [--item-key <key>]  # MinerU 解析 PDF → Markdown
python -m lit maintain [--collection X] [--fix]  # 文件库健康检查
python -m lit qr <DOI>               # 生成 QR 码
python -m lit track <author> [--download]  # 检测作者新论文
```

旧版入口（`people.py`, `zot.py`, `main.py`）已弃用，代码保留兼容。

# 下载架构（两层）

PDF 下载是两个独立命令，agent 按需编排：

| 层 | 命令 | 原理 | 速度 | 覆盖率 |
|----|------|------|------|--------|
| 快速通道 | `lit quick` | Sci-Hub CDP（利用已有 Edge 连接，5s 过 DDoS-Guard） | 秒级 | ~50%（≤2021） |
| 兜底通道 | `lit attach` | 27 个出版商适配器，CDP 导航到出版商页面，机构登录态下载 | 分钟级 | 几乎全覆盖 |

**两层都先检查本地是否已有 PDF**（`resolve_local_pdf`），已有则跳过。

# 规则

- 把当前 `SKILL.md` 所在目录视为 `<skill-base>`。所有本地资源从 `<skill-base>` 解析，不依赖调用方工作目录。
- **Zotero 是唯一数据源**。不再使用 `papers.json` 中间文件。所有状态读自 Zotero API。
- **Zotero 同步方式**：`config.yaml` 的 `zotero.sync_method` 控制附件挂载方式。`webdav`（推荐）：JSON API 建条目 + 本地拷文件，不消耗 Zotero 云配额。`cloud`：API multipart 上传（走配额）。详见 `references/webdav-setup.md`。
- **DOI 是稳定 key**：始终用 DOI 查找 Zotero 条目，不信任本地缓存的 key。
- **`lit.core.zotero.check_duplicate()` 内置去重**：按 DOI/URL/title 搜索，已存在则返回现有 key。
- **Chromium 启动**：推荐手动启动（有机构登录状态，`--remote-debugging-port=19222`）。`lit attach` 默认用 CDP 连接。
- Elsevier 论文额外依赖 Foxit Reader（Print to PDF 虚拟打印机）。
- Python 依赖：`playwright`, `pyautogui`, `requests`, `pyyaml`, `rich`, `pyzotero`。首次使用运行 `<skill-base>/setup.bat`。
- 支持的出版商由 `<skill-base>/url_parser.py` 的 `PUBLISHER_PATTERNS` 自动匹配。
- 下载失败时，先查 `<skill-base>/error_log.md` 该出版商的条目。深度调试读 `references/architecture.md`。
- **OCR DOI 和 CrossRef 匹配都不可全信**。检查 `crossref_score`：<30 时匹配不可信。

# 工作流程

## 判定任务类型

| 用户意图 | 命令编排 |
|---------|---------|
| "下载这篇论文" | `lit import <DOI>` → `lit quick <DOI>` → `lit attach <DOI>` |
| "只加进 Zotero" | `lit import <DOI>` |
| "帮我填满这个库的 PDF" | `lit quick <collection>` → `lit attach <collection>` |
| 收集某学者所有论文 | `lit scholar <URL>` → 清洗 → `lit quick` → `lit attach` → `lit digest` |
| **"更新 digest"** | 读已有 digest.md → diff Zotero 找新论文 → 逐篇深读 → 手术式更新（详见 `references/digest-workflow.md`） |
| **"精读这篇论文"** | `lit parse <pdf>` → 深读全文 → paper digest（详见 `references/paper-digest-workflow.md`） |
| 图片 OCR 导入 | `lit import <image_path>` → `lit quick <DOI>` → `lit attach <DOI>` |

## 下载编排（Agent 责任）

三个命令各做一件事，agent 按场景编排：

### 单篇论文（最常见的场景）

```
lit import <DOI>     # 注册到 Zotero
lit quick <DOI>      # 快速尝试 Sci-Hub（秒级）
lit attach <DOI>     # 兜底（如果 quick 没拿到）
```

Agent 默认连续执行 quick → attach。quick 成功则跳过 attach（attach 内部会检查已有 PDF）。

### 批量填满（条目已在 Zotero，只差 PDF）

```
lit quick <collection>    # 先快速批量
lit attach <collection>   # 再兜底批量
```

### 仅注册（不下载）

```
lit import <DOI>          # 只注册
```

## 下载排查 & 适配器

### 排查修复

**先查 `error_log.md`**。运行时错误（超时/导航）→ 检查 Chrome；页面结构变化 → 读 `references/maintain.md` 流程 A；"Access denied" 但有订阅 → 查 `error_log` 中 `check_access` 误报条目。

### 添加新出版商

1. 读 `references/maintain.md` **流程 B** 完整执行
2. 必须用 Playwright CDP 探测页面，不能只靠 DevTools
3. 创建适配器后注册到 `lit/download/adapters/__init__.py` + `url_parser.py` + `engine.py` 的 `_ADAPTERS`
4. **常见 bug**：`find_download_url(self, page)` 签名不能多参数；OA 出版商必须覆盖 `check_access()` 返回 `True`（JCI Insight、bioRxiv）；`url_parser.py` 正则用 `\\.` 转义 dot

## 人机合作流程（大型学者）

**分阶段执行，人在中间清洗数据**：

### Phase 1：Agent — 建文件夹 + 注册条目

```bash
python -m lit scholar "SCHOLAR_URL"
```

### Phase 2：用户手动清洗数据

在 Zotero `People/<学者名>` 文件夹中修元数据、删不相关、去重、补遗漏。

### Phase 3：Agent — 补 PDF + 解析 + 消化

```bash
python -m lit quick "学者名"              # 批量 Sci-Hub
python -m lit attach "学者名"             # 批量 publisher adapter 兜底
python -m lit parse <pdf> --item-key <key>  # 解析 PDF
python -m lit digest "学者名"             # 生成消化报告
```

### 为什么不一把走完？

Scholar 数据很脏（截断作者名、专利/会议混入、重复），人机合作把清洗放中间，agent 只负责机械重复的工作。

## 旧版命令（兼容）

```bash
PYTHONIOENCODING=utf-8 python "main.py" "URL"           # 下载
PYTHONIOENCODING=utf-8 python "zot.py" "URL"            # Zotero
PYTHONIOENCODING=utf-8 python "people.py" "URL"         # 学者
PYTHONIOENCODING=utf-8 python "pdf_parser.py" "path"    # 解析
```

## 支持的出版商（27 家）

| 出版商 | 域名 |
|--------|------|
| AAAS (Science) | science.org |
| ACS Publications | pubs.acs.org |
| AIP (Silverchair) | pubs.aip.org |
| Annual Reviews | annualreviews.org |
| APS (Physical Review) | journals.aps.org |
| bioRxiv / medRxiv | biorxiv.org, medrxiv.org |
| BMJ | bmj.com |
| eLife | elifesciences.org |
| Elsevier (ScienceDirect) | sciencedirect.com |
| Frontiers | frontiersin.org |
| IEEE | ieeexplore.ieee.org |
| IOP Publishing | iopscience.iop.org |
| JCI Insight | insight.jci.org |
| LWW (Lippincott) | journals.lww.com |
| MDPI | mdpi.com |
| Nature Publishing Group | nature.com |
| Optica (OSA) | opg.optica.org |
| PNAS | pnas.org |
| PMC | ncbi.nlm.nih.gov |
| Royal Society | royalsocietypublishing.org |
| RSC | pubs.rsc.org |
| SAGE | journals.sagepub.com |
| SPIE | spiedigitallibrary.org |
| Springer / SpringerLink | springer.com, link.springer.com |
| Taylor & Francis | tandfonline.com |
| Wiley | onlinelibrary.wiley.com |
| 物理学报 | wulixb.iphy.ac.cn |

## 参考文档

| 文档 | 内容 |
|------|------|
| `references/architecture.md` | 代码架构、`lit/` 包结构、适配器详解 |
| `references/legacy.md` | 旧版入口参考（已弃用）|
| `references/maintain.md` | 添加/修复 publisher 流程模板 |
| `references/cron-automation.md` | 批量下载 cron 格式规范 + 模板（**创建 cron 前必读**） |
| `references/people-guide.md` | 人机合作流程详细说明 |
| `references/digest-workflow.md` | Scholar digest 填充方法论 + 增量消化工作流 |
| `references/paper-digest-workflow.md` | Paper digest 单篇精读工作流 |
| `references/webdav-setup.md` | WebDAV 配置说明 |
| `references/mineru-api.md` | MinerU PDF 解析 API 说明 |
