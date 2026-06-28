# People Feature Guide (`people.py`)

> 给定 Google Scholar Profile URL，批量抓取、下载某学者的全部论文并生成结构化文献消化报告。

**前提**：Edge/Chrome 需先通过 `chromium_helper.launch_browser()` 启动，或已手动打开（`--remote-debugging-port=19222`）。

## CLI 命令速查

| 模式 | 推荐命令 | 旧版兼容 |
|------|---------|---------|
| 完整流程（抓取+DOI+下载+模板） | `lit scholar <URL>` | `python people.py "URL" --download` |
| 仅抓取测试 | `lit scholar <URL> --scrape-only` | `python people.py "URL" --scrape-only` |
| 批量注册 Zotero（不下载 PDF） | `lit scholar <URL>` | `python people.py --register-only --scholar-name "学者名"` |
| **补缺PDF（人机合作）** | `lit attach <collection>` | `python -m lit attach "学者名"` |
| 生成消化报告 | `lit digest <collection>` | `python -m lit digest "学者名"` |
| 限制篇数测试 | `lit scholar <URL> --max-papers 5` | `python people.py "URL" --scrape-only --max-papers 5` |

## 处理流程

- **Phase 1**: Playwright CDP 抓取 Scholar Profile → 过滤专利/会议 → 去重 preprint/正式版
- **Phase 1b**: CrossRef 搜索标题匹配 DOI（排除补充材料 `.sNNN`，preprint 降权）
- **Phase 1c**: 作者数据库构建 — 从 CrossRef 提取通讯作者全名、affiliation、缩写，存入 `people/data/authors_db.json`
- **Phase 2**: 在 Zotero 创建 `People/<学者名>` collection
- **Phase 2b**: `--register-only` — 批量用 CrossRef 元数据创建 Zotero 条目（无 PDF），跳过已有 `zotero_key` 的篇目
- **Phase 3**: 按年份先后线性下载（默认关闭，需 `--download` 启用）。`download_one_paper` 使用 **state-aware flow**（状态①：已有 PDF → 跳过；状态②：Zotero 有条目无 PDF → DOI 查找 + 下载 + 挂载；状态③：无条目 → 创建 + 下载 + 挂载）
- **Phase 4**: 生成文献消化模板（4 Block + ⚡ cross-talk 区）

## 人机合作推荐流程（大型学者 200+ 篇）

这是当前推荐的 `-people` 工作方式——**分阶段执行，人在中间清洗数据**：

### Phase 1：Agent 自动 — 建文件夹 + 注册条目

```bash
# 1a. 抓取 Scholar Profile（可选，lit scholar 内置抓取）
lit scholar "SCHOLAR_URL" --scrape-only
# 1b. 抓取 + DOI 匹配 + 注册到 Zotero
lit scholar "SCHOLAR_URL"
```

结果：Zotero 里 `People/<学者名>` 文件夹建好，每篇有 CrossRef 元数据（标题、作者、DOI、年份），**无 PDF 附件**。

### 步骤 2：你手动清洗数据

打开 Zotero，在 `People/<学者名>` 文件夹中：
- 删除不相关的论文
- 修正错误的元数据
- 合并重复条目
- 从 Google Scholar（或其他来源）手动导入你认为重要的遗漏论文
- 确保所有保留的条目都有正确的 DOI

**清洗完毕通知 agent。**

### Phase 3：Agent 继续 — 补 PDF + 消化

```bash
# 3a. 读取 Zotero 文件夹，下载并挂载缺 PDF 的条目
lit attach "学者名"

# 3b. 生成消化模板
lit digest "学者名"
```

代码行为：
- **不依赖 `papers.json`**（之前抓取的数据）——直接从 Zotero API 读取 `People/<学者名>` 文件夹的当前状态
- 只处理有 DOI 且无 PDF 附件的条目
- 已有 PDF 的条目自动跳过（通过一次 API 拉取全部条目含子项，本地交叉比对，无逐项 N+1 开销）
- 每次下载一篇，失败不影响其他篇

### ⚠️ 为什么不一把走完 `-people "URL" --download`？

Scholar 抓取的数据很脏（截断作者名、专利/会议混入、preprint/正式版重复），直接一把全自动会导致 Zotero 里大量需要事后清理的条目。人机合作流程把**清洗**放在中间，agent 只负责机械重复的工作（注册 + 下载 PDF）。

## `lit scholar` 执行时间

`lit scholar` 一条命令跑完 Phase 1+2（抓取 + CrossRef DOI 匹配 + Zotero 注册），**不分步**。

| 论文数 | CrossRef 匹配耗时 | 说明 |
|--------|------------------|------|
| ≤50 篇 | 2-3 min | 前台运行 OK |
| 50-150 篇 | 5-10 min | 前台 timeout=300 可能够，保险起见后台 |
| 150+ 篇 | 15-25 min | **必须后台运行**（`background=true, notify_on_complete=true`） |

CrossRef API 逐篇查询（含 polite pool 节流），速度 ~10 篇/min。200+ 篇的学者（如 Garth Simpson 274 篇 → ~25min）前台 300s 必然超时。**第一次就放后台**，别浪费一轮 300s timeout。

## 批量下载策略

默认关闭（`lit scholar` 不含下载）。建议 cron 线性下载（10-15min/篇），用 `lit attach` 做断点续传（从 Zotero 读状态）。一次性大量下载会触发出版商 access 封禁。

## 关键陷阱

1. **`subprocess.run()` 必须加 timeout**。`lit/download/engine.py` 的 `download_pdf()` 传 `timeout=120`，超时后 `raise RuntimeError`，`lit/batch/attach.py` 捕获后标记失败继续下篇。

2. **每篇下载后必须保存进度**（`download_batch` 的 `save_callback` 参数）。不保存 → 进程被 kill 后全部重来。调用方传 `save_callback=lambda papers: save_papers(...)`，每篇后自动 JSON 落盘。重跑时 `resume=True` 跳过 `dl_status=success` 的篇。

3. **`lit download` 自动跳过 warmup**：`lit/download/engine.py` 的 `download_pdf()` 默认不带 warmup（Chromium 已在手动模式下运行）。批量场景使用 `lit attach` 自动处理。

4. **DOI 解析失败（RSC `RemoteDisconnected`）**：`resolve_doi()` 用 `requests.head()` → RSC 拒绝 HEAD 连接。已在 `url_parser.py` 改为 `requests.get()` + 浏览器 UA header。新增出版商类似问题先查 `resolve_doi()` 是否用 HEAD。

5. **Scholar 截断作者 `...` 破坏 Zotero API**：Scholar 抓取的 `authors` 字符串结尾有 `, ...`，`create_item()` 会创建 `lastName="..."` 的 creator，Zotero API 400。修复：`lit/discover/scholar.py` 中过滤 `[a for a in raw if a and a != "..." and len(a) > 1]`。

6. **`lit attach` 天然支持重试**：`lit attach` 直接从 Zotero collection 读状态（有 DOI + 无 PDF → 需要下载），每次运行相当于自动检测哪些篇缺 PDF。不需要手动 `--retry` 标记。

7. **配置 path 注意**：`config.yaml` 被 gitignore，clone 后需手动修正 `temp_dir` 和 `storage_path` 中的用户名。

## 已知不支持/易失败的出版商

- **SPIE** (`spiedigitallibrary.org`) — 页面加载极慢，经常 120s timeout。会议论文（DOI 前缀 `10.1117/12.`）居多，已在 `CONFERENCE_KEYWORDS` + `--retry` 中自动过滤。
- **Elsevier ScienceDirect** (`sciencedirect.com`) — 部分页面 120s timeout；依赖 Foxit Reader 虚拟打印，更慢。需要机构登录。
- **Nature Microbiology / Nature 子刊** — 需要机构登录才能下载。NPG 适配器识别正常但 check_access 无订阅则失败。
- **Communications Chemistry 等 Springer Nature 子刊** — 适配器偶发失败（页面结构差异），重现后需 CDP 探测修复。

## 过滤规则

默认排除 Patent + 会议（领域内会议不重要）。会议匹配关键词见 `CONFERENCE_KEYWORDS`（`people.py`）。如果遗漏新会议，在 `CONFERENCE_KEYWORDS` 列表追加。SPIE 会议也可按 DOI 前缀 `10.1117/12.` 识别（`retry_failed()` 中自动处理）。

## 注意事项

- Scholar Profile 页面渲染需要 3-5 秒，`page_delay: 3000` 足够
- 每页 20 条，`Show More` 按钮 disabled 时全部加载完毕
- 论文从旧到新排序（年序）
- 下载前确保 Edge 已启动（`--remote-debugging-port=19222`）

## 故障排查

| 问题 | 原因 | 解决 |
|------|------|------|
| DOI resolve 失败（如 RSC `RemoteDisconnected`） | 部分出版商（RSC）拒绝 `requests.head()` | 已在 `url_parser.py` 修复为 `GET` + 浏览器 UA |
| Zotero API `'firstName' field must be set` | Scholar 截断作者 `...` 传入 `create_item()` | `lit/discover/scholar.py` 已自动过滤 |
| 论文抓取后数量不对 | `CONFERENCE_KEYWORDS` 漏了该会议 | 在 `lit/discover/scholar.py` 的 `CONFERENCE_KEYWORDS` 列表追加 |
| `config.yaml` 路径不匹配 | gitclone 后路径中的用户名不同 | 手动修正 `temp_dir` 和 `storage_path` |
| CDP 连接失败 | Edge 未启动或端口不对 | 先手动启动 Edge（`--remote-debugging-port=19222`）|
| CDP 端口连不上但 msedge.exe 在运行 | Edge 已有实例占用了 user-data-dir，新进程不继承 debug 端口 | `taskkill /F /IM msedge.exe` 全杀 → 删 `SingletonLock`/`SingletonSocket`/`SingletonCookie`（User Data 目录下）→ 重启 Edge 带 `--remote-debugging-port=19222` → `curl http://127.0.0.1:19222/json/version` 验证 |
| 批量下载永远跑不完（进程挂起） | `subprocess.run()` 无 timeout | 已在 `lit/download/engine.py` 加 `timeout=120` |
| PDF 下载失败率高 | 部分出版商无适配器或页面结构变化 | 查看 `references/architecture.md` 的「已知限制」|
| 附件在另一台电脑上显示空壳 | `imported_file` 路径是绝对路径，不跨机器 | 查看 `references/storage-file-gap.md` |
| 批量下载有失败项 | 部分出版商超时或无订阅 | 重跑 `lit attach` 会自动处理失败的篇 |
| 验证 Zotero 条目数远少于预期 | `collection_items(key)` 默认只返回 **100 条**（pyzotero 分页限制） | 分页查询：循环 `collection_items(key, limit=100, start=0/100/200...)` 直到返回 <100 条 |
| `lit scholar` 超时中断后不敢重跑 | 担心重复注册 | **安全重跑**：`lit scholar` 基于 DOI 去重，重跑时已注册的篇标记 `Already exists` 自动跳过，不会产生重复条目 |
