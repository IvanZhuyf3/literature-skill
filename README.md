# Literature Skill

学术文献一站式工具：**注册元数据** → **下载 PDF** → **挂载到 Zotero** → **解析全文** → **生成消化报告**。

为 [Hermes Agent](https://github.com/NousResearch/hermes-agent) 设计的 skill，也可作为独立 CLI 使用。

## 快速开始

```bash
# 安装依赖（全局）
pip install -r requirements.txt
playwright install chromium

# 配置
cp config.yaml.example config.yaml
# 编辑 config.yaml：Zotero API key、library ID、Chrome 路径等

# 启动带调试端口的 Edge（机构登录态）
start_browser.bat

# 用法
python -m lit import 10.1038/s41586-024-07386-0    # 注册到 Zotero
python -m lit quick 10.1038/s41586-024-07386-0     # 快速下载（秒级）
python -m lit attach 10.1038/s41586-024-07386-0    # 兜底下载（分钟级）
```

## 命令一览

| 命令 | 用途 |
|------|------|
| `lit import <DOI/URL/图片>` | 注册论文到 Zotero（不下载 PDF） |
| `lit quick <DOI/collection>` | 快速下载（Crossref TDM → arXiv → Sci-Hub → Unpaywall） |
| `lit attach <DOI/collection>` | Publisher adapter 兜底下载（27 家出版商，CDP + 机构登录态） |
| `lit scholar <Scholar_URL>` | 批量抓取学者所有论文 → 注册到 Zotero |
| `lit pdf <DOI>` | 查找本地 PDF 路径 |
| `lit parse <pdf>` | MinerU API 解析 PDF → Markdown |
| `lit digest <collection>` | 生成文献消化模板 |
| `lit discover-s2 <author>` | S2 profile 发现 + 全量审计 |
| `lit track <author>` | 增量检测作者新论文 |
| `lit build-affiliations <author>` | 构建年度 affiliation 数据库（OpenAlex） |
| `lit maintain` | 文件库健康检查 |
| `lit qr <DOI>` | 生成 QR 码 |

## 两层下载架构

下载和注册分离。`lit import` 只注册元数据，下载由 agent 按需编排：

| 层 | 命令 | 方法 | 速度 | 覆盖率 |
|----|------|------|------|--------|
| 快速通道 | `lit quick` | Crossref TDM → arXiv → Sci-Hub (CDP) → Unpaywall | 秒级 | ~50% |
| 兜底通道 | `lit attach` | 27 个出版商适配器，CDP 导航 + 机构登录态 | 分钟级 | 几乎全覆盖 |

**典型单篇流程**：`import` → `quick` → `attach`（quick 成功则跳过 attach）

**典型批量流程**：`scholar` → 用户清洗 → `quick <collection>` → `attach <collection>` → `digest`

## 支持的出版商（27 家）

AAAS (Science) · ACS · AIP · Annual Reviews · APS · bioRxiv/medRxiv · BMJ · eLife · Elsevier · Frontiers · IEEE · IOP · JCI Insight · LWW · MDPI · Nature · Optica (OSA) · PMC · PNAS · Royal Society · RSC · SAGE · SPIE · Springer · Taylor & Francis · Wiley · 物理学报

## 论文追踪系统

基于 Semantic Scholar + OpenAlex + CrossRef 三源：

```
lit discover-s2 <author> --save      # 发现 S2 profile + DOI 反查 + 全量审计
lit track <author>                   # 增量检测新论文（置信度分层）
lit build-affiliations <author>      # OpenAlex 年度 institution 数据
```

- **S2** 负责论文发现（profile-scoped）
- **OpenAlex** 负责 institution 数据（batch 查询，~90% 覆盖率）
- **CrossRef** 做 fallback
- **DOI 是唯一稳定 key**：查重、注册、下载全程用 DOI

## Zotero 同步

`config.yaml` 的 `zotero.sync_method` 控制：

- **`webdav`**（推荐）：JSON API 建条目 + 本地拷贝 PDF，不消耗 Zotero 云配额
- **`cloud`**：API multipart 上传（走配额，quota 满时自动降级 webdav）

## 项目结构

```
├── lit/                    # 主包
│   ├── cli.py              # CLI 入口
│   ├── core/               # 配置、Zotero API、CrossRef、截图
│   ├── batch/              # 批量下载（quick / attach / register）
│   ├── download/           # 下载引擎
│   │   ├── engine.py       # Publisher adapter 引擎
│   │   ├── quick_download.py  # 快速通道编排器（四源链）
│   │   ├── scihub_cdp.py   # Sci-Hub CDP（多镜像 + 熔断）
│   │   ├── crossref_tdm.py
│   │   ├── preprint.py
│   │   └── unpaywall.py
│   ├── discover/           # Scholar 抓取、import、tracker
│   ├── digest/             # 文献消化模板 + 解析
│   └── maintain.py         # 健康检查
├── publisher/              # 出版商适配器（27 个）
├── references/             # 架构文档（25 篇）
├── debug/                  # 调试/批量脚本
├── config.yaml.example     # 配置模板
├── requirements.txt
└── setup.bat               # 一键安装
```

## 前置要求

- **Windows** + Chromium 内核浏览器（Edge 推荐，需机构登录态）
- **Python 3.10+**
- **Zotero** 账户（API key + library ID）
- **MinerU** API token（PDF 解析用，[mineru.net](https://mineru.net) 免费注册）
- Elsevier 论文额外需要 Foxit Reader（Print to PDF 虚拟打印机）

## 配置

编辑 `config.yaml`：

```yaml
chrome:
  executable_path: "C:/Program Files/Microsoft/Edge/Application/msedge.exe"
  debug_port: 19222              # 不用 9222（Hyper-V 保留）

zotero:
  api_key: "YOUR_KEY"
  library_id: "YOUR_ID"
  storage_path: "C:/Users/.../Zotero/storage"
  sync_method: webdav            # webdav 或 cloud

download:
  temp_dir: "C:/Users/.../Downloads/temp"
  timeout: 60

rate_limit:
  per_paper_delay: 5
  max_sessions: 3
```

## 开发

单目录开发，此目录即唯一工作目录：

```bash
git add -A && git commit -m "描述" && git push origin main
```

详见 `AGENTS.md`（开发约定）、`references/`（架构文档）、`SKILL.md`（完整 skill 定义）。

## License

Personal use.
