# Literature Skill — 开发环境入口

> 本文件供 OpenCode / Claude Code / 人工开发时使用。打包为 skill 后，agent 读 `SKILL.md` 入口。

## 文档导航

| 文件 | 什么时候看 |
|------|-----------|
| `SKILL.md` | 用法、各子命令、故障排查 |
| `references/architecture.md` | 代码架构、`lit/` 包结构、适配器详解 |
| `references/legacy.md` | 旧版入口参考（`main.py`, `zot.py`, `people.py`） |
| `references/maintain.md` | 添加/修复 publisher 时的流程模板 |
| `references/people-guide.md` | 人机合作流程详细说明 |
| `references/digest-workflow.md` | 消化模板填充方法论 |

## 主入口：`python -m lit <command>`

```bash
# Scholar → Zotero 注册（无 PDF）
python -m lit scholar <URL> [--max-papers N] [--scrape-only]

# 单篇注册 Zotero（DOI / URL / 图片 OCR）→ 自动快速下载 PDF
python -m lit import <DOI_or_URL_or_image_path>
# 下载流程：import_ref(仅注册) → quick_download(Sci-Hub CDP) → attach_pdf(WebDAV)

# 补缺 PDF（读 Zotero collection）
python -m lit attach <collection_name> [--limit N]

# 文件库体检与清理
python -m lit maintain                          # 全库快速检查
python -m lit maintain --collection "Ji-Xin Cheng"  # 含 per-item 检查
python -m lit maintain --fix                    # 执行修复

# 解析 PDF + 可选 bibliography
python -m lit parse <pdf_path> [--output <md>] [--item-key <key>]

# 生成消化报告
python -m lit digest <collection_name>

# QR 码
python -m lit qr <DOI>

# 已废弃
python -m lit download <DOI>   # 用 `lit import` 替代
```

## 下载架构（两层）

PDF 下载是两层设计，缺一不可：

### 第一层：快速免费通道（`quick_download.py`）
- **定位**：低资源占用、低成功率的"先试一把"通道
- **当前方法**：Sci-Hub CDP（`scihub_cdp.py`），利用已有 Edge CDP 连接，5s 过 DDoS-Guard
- **预期覆盖率**：~50%。Sci-Hub 最大年份 2021，且不覆盖所有出版商
- **未来扩展**：Unpaywall、PMC、CORE 等 OA 源会注册到 `_METHODS` 列表
- **特点**：不开新浏览器 tab、不导航到出版商页面、不模拟阅读，秒级返回

### 第二层：出版商适配器（`engine.py` + `publisher/*.py`）— 兜底系统
- **定位**：几乎必需的兜底通道，覆盖快速通道拿不到的 ~50% 文献
- **原理**：通过 CDP 连接已有 Edge（带机构登录态），导航到出版商页面，
  用每个出版商专属的 CSS 选择器定位 PDF 按钮并下载
- **27 个 adapter**：aaas, acs, aip, aps, biorxiv, bmj, elife, elsevier,
  frontiers, ieee, iop, jci_insight, lww, mdpi, npg, optica, pmc, pnas,
  royalsociety, rsc, sage, spie, springer, tandf, wiley, wulixb
- **选择器**：除 ACS 外全部硬编码在各 adapter 的 `find_download_element()` 中。
  `config.yaml` 的 `publishers:` 块仅 ACS 有（调试残留），其余 adapter 不读 config
- **engine.py 内部 fallback**：CDP + adapter 失败 → 调 `main.py` 子进程重试

### ⚠ 当前断链
`lit import` 目前只调 `quick_download`，Sci-Hub 失败后直接放弃，
**没有接上 `engine.py`**。deprecated 的 `lit download` 才走 publisher adapter。
需要把 publisher adapter 作为 fallback 接入 `lit import` 和 `lit pdf` 的流程。

## 架构关键变更

- **`lit/discover/cite.py` → `import_ref.py`**：只做 Zotero 条目注册，不碰下载
- **`lit/download/quick_download.py`**：第一层编排器，按序调各免费源
- **`lit/download/scihub_cdp.py`**：Edge CDP 过 DDoS-Guard，替代旧的 cloudscraper 版
- **`lit/download/engine.py`**：第二层 publisher adapter 引擎（27 个适配器）
- **元数据统一从 Zotero 拉**：`zotero.py` 新增 `fetch_item()` 和 `item_to_meta()`
- **`lit parse --item-key <key>`**：解析 PDF 时从 Zotero 拉 bibliography
- **DOI 作为 .md 文件名**：`format_doi_filename()` 实现，天然去重

## 开发约定

- 新建 publisher 适配器后，更新 `references/architecture.md`、`SKILL.md` 和 `lit/download/adapters/__init__.py`
- 所有 Python 脚本前缀 `PYTHONIOENCODING=utf-8`（Windows GBK）
- 全局安装依赖，不建 venv
- `config.yaml` 包含 Chrome/Zotero/下载/速率/调试配置
- `lit/core/config.py` 是配置单例，所有模块从此处加载

## 关键 Gotchas

- `lit/core/zotero.delete_item()`：必须先 `fetch` item 拿 version info 再删（pyzotero 要求）
- Chromium 手动启动（`--remote-debugging-port=19222`），有机构登录状态
- Windows Hyper-V 可能保留端口 9222，用 19222 避免冲突
- 旧版入口（`main.py`, `zot.py`, `people.py`）代码保留兼容，`engine.py` 失败时作为子进程 fallback 调 `main.py`
- **下载两层架构**：quick_download（Sci-Hub 等免费源，~50% 覆盖）→ publisher adapter（27 个出版商适配器，兜底）。详见上方"下载架构"节
- `lit import` 当前**缺少**第二层 fallback：quick_download 失败后没接 engine.py（已知 TODO）
- Sci-Hub CDP 下载：DDoS-Guard 需~5s 解析，`wait_for_load_state("domcontentloaded")` + 轮询 title
- Publisher adapter 选择器维护：出版商改版 DOM 后选择器会失效，需 CDP 探测新选择器（流程见 `references/maintain.md`）

## TODO / Ideas（未排期）

### 被引链接图（Citation Map）

检测库内论文的互相引用关系。每篇 .md（DOI 命名）的参考文献段落扫描 DOI，跟库里已有的 DOI 交叉匹配，生成引用网络数据。库够大（跨多个学者、整个领域）时价值显著，单学者仅自引意义不大。

**条件成熟再动手。**
