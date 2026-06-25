# Literature Skill

> 单目录开发：直接在此目录（prod skill dir）编辑代码 + `git add && git commit && git push origin main`。GitHub 做备份。不需要 dev/prod sync。

## 文档导航

| 文件 | 什么时候看 |
|------|-----------|
| `SKILL.md` | 用法、各子命令、故障排查 |
| `references/architecture.md` | 代码架构、`lit/` 包结构、适配器详解 |
| `references/legacy.md` | 旧版入口参考（`main.py`, `zot.py`, `people.py`） |
| `references/maintain.md` | 添加/修复 publisher 时的流程模板 |
| `references/digest-workflow.md` | Scholar digest 填充方法论 + 增量消化工作流 |
| `references/paper-digest-workflow.md` | Paper digest 单篇精读工作流 |
| `references/people-guide.md` | 人机合作流程详细说明 |

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
- **模块**：`lit/batch/quick.py` → `lit/download/quick_download.py`
- **定位**：低资源、低成功率的"先试一把"通道
- **方法链**（`_METHODS` 列表，按序尝试）：
  1. **Crossref TDM**（`crossref_tdm.py`）：查 Crossref API `link[]` 提取出版商提供的 PDF 直链。无年份限制
  2. **Preprint**（`preprint.py`）：arXiv 直连下载（`10.48550/arXiv.*`）。bioRxiv 有 Cloudflare 不走此路
  3. **Sci-Hub CDP**（`scihub_cdp.py`）：Edge CDP 过 DDoS-Guard，≤2021 年
  4. **Unpaywall**（`unpaywall.py`）：OA 聚合，查 `best_oa_location` 下载合法开放获取 PDF。无年份限制。需 `unpaywall.email`（config，非必需）
- **都不需要 API key**

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
- **`lit/download/quick_download.py`**：快速通道编排器（`_METHODS` 列表，四源：Crossref TDM → Preprint → Sci-Hub → Unpaywall）
- **`lit/download/crossref_tdm.py`**：Crossref API `link[]` PDF 直链提取
- **`lit/download/preprint.py`**：arXiv 预印本直连下载
- **`lit/download/scihub_cdp.py`**：Sci-Hub CDP 方案（≤2021）
- **`lit/download/unpaywall.py`**：Unpaywall OA 聚合下载
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

**状态：设计阶段，plan 见 `../Deep_research/plan.md` Phase 1B**

S2 API 直接提供引用关系 + context，不需要自己 parse 全文。两个方向：
- ref（引用了谁）= 死数据，永久缓存
- fwd（被谁引用）= 活数据，TTL 30 天

CLI：`lit cite ref|fwd|ctx <DOI>`，输出带 `in_zotero` 标记。
模块：`lit/cite/{s2_client,cache,cli}.py`。
