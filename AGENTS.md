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

## 架构关键变更

- **`lit/discover/cite.py` → `import_ref.py`**：只做 Zotero 条目注册，不碰下载
- **`lit/download/quick_download.py`**：编排器，按序调各平台下载方法
- **`lit/download/scihub_cdp.py`**：Edge CDP 过 DDoS-Guard，替代旧的 cloudscraper 版
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
- 旧版入口（`main.py`, `zot.py`, `people.py`）代码保留兼容但不再主动维护
- `lit/download/engine.py` 有 fallback：CDP + adapter 失败时调 `main.py` 子进程
- Sci-Hub CDP 下载：DDoS-Guard 需~5s 解析，`wait_for_load_state("domcontentloaded")` + 轮询 title
