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
# 注册（不下载 PDF）
python -m lit scholar <URL> [--max-papers N] [--scrape-only]
python -m lit import <DOI_or_URL_or_image_path>

# 快速下载（Sci-Hub + OA 源，秒级，~50% 覆盖）
python -m lit quick <DOI|collection> [--parent People] [--limit N]

# Publisher adapter 兜底（分钟级，几乎全覆盖）
python -m lit attach <DOI|collection> [--parent People] [--limit N]

# 查本地 PDF 路径
python -m lit pdf <DOI>

# 其他
python -m lit parse <pdf_path> [--output <md>] [--item-key <key>]
python -m lit digest <collection_name>
python -m lit maintain [--collection X] [--fix] [--dry-run]
python -m lit qr <DOI>
python -m lit track <author> [--download]
```

## 下载架构（两层，三个独立命令）

下载是两个独立命令，各管一层。`lit import` 只注册，不碰下载。Agent 编排执行顺序。

### lit quick — 快速通道
- **模块**：`lit/batch/quick.py` → `lit/download/quick_download.py` → `scihub_cdp.py`
- **定位**：低资源、低成功率的"先试一把"通道
- **当前方法**：Sci-Hub CDP，5s 过 DDoS-Guard，秒级返回
- **覆盖率**：~50%（Sci-Hub 最大年份 2021）
- **未来扩展**：Unpaywall、PMC、CORE 等 OA 源注册到 `_METHODS` 列表

### lit attach — Publisher adapter 兜底
- **模块**：`lit/batch/attach.py` → `lit/download/engine.py` → `publisher/*.py`
- **定位**：几乎必需的兜底通道
- **原理**：CDP 连接 Edge（机构登录态）→ 导航出版商页面 → CSS 选择器定位 PDF 按钮 → 下载
- **27 个 adapter**：aaas, acs, aip, aps, biorxiv, bmj, elife, elsevier, frontiers, ieee,
  iop, jci_insight, lww, mdpi, npg, optica, pmc, pnas, royalsociety, rsc, sage, spie,
  springer, tandf, wiley, wulixb
- **engine.py 内部 fallback**：CDP + adapter 失败 → 调 `main.py` 子进程重试

### 共享代码
- `lit/batch/common.py`：`collect_missing()` 遍历 collection 查缺口，`batch_download()` 批量循环。quick 和 attach 共用

## 架构关键变更

- **`lit import` 只注册**：不再内嵌下载逻辑。下载走 `lit quick` / `lit attach`
- **`lit/batch/common.py`**：quick 和 attach 的批量逻辑抽到这里（遍历 collection → 查缺口 → 下载 → 挂载）
- **`lit/batch/quick.py`**：快速下载，单篇 + 批量
- **`lit/batch/attach.py`**：Publisher adapter 兜底，单篇 + 批量
- **`lit/download/quick_download.py`**：快速通道编排器（`_METHODS` 列表）
- **`lit/download/scihub_cdp.py`**：Sci-Hub CDP 方案
- **`lit/download/engine.py`**：Publisher adapter 引擎（27 个适配器）
- **元数据统一从 Zotero 拉**：`zotero.py` 的 `fetch_item()` 和 `item_to_meta()`
- **DOI 作为 .md 文件名**：`format_doi_filename()` 实现，天然去重

## 开发约定

- 新建 publisher 适配器后，更新 `references/architecture.md`、`SKILL.md`、`url_parser.py`、`engine.py` 的 `_ADAPTERS` dict
- 所有 Python 脚本前缀 `PYTHONIOENCODING=utf-8`（Windows GBK）
- 全局安装依赖，不建 venv
- `config.yaml` 包含 Chrome/Zotero/下载/速率/调试配置
- `lit/core/config.py` 是配置单例，所有模块从此处加载

## 关键 Gotchas

- `lit.core.zotero.delete_item()`：必须先 `fetch` item 拿 version info 再删（pyzotero 要求）
- Chromium 手动启动（`--remote-debugging-port=19222`），有机构登录状态
- Windows Hyper-V 可能保留端口 9222，用 19222 避免冲突
- 旧版入口（`main.py`, `zot.py`, `people.py`）代码保留兼容，`engine.py` 失败时作为子进程 fallback 调 `main.py`
- Sci-Hub CDP 下载：DDoS-Guard 需~5s 解析，`wait_for_load_state("domcontentloaded")` + 轮询 title
- Publisher adapter 选择器全部硬编码在各 adapter 的 `find_download_element()` 中。config.yaml 不含 `publishers` 块（已清理）

## TODO / Ideas（未排期）

### 被引链接图（Citation Map）

检测库内论文的互相引用关系。每篇 .md（DOI 命名）的参考文献段落扫描 DOI，跟库里已有的 DOI 交叉匹配，生成引用网络数据。库够大（跨多个学者、整个领域）时价值显著，单学者仅自引意义不大。

**条件成熟再动手。**
