# People Feature Guide (`people.py`)

> 给定 Google Scholar Profile URL，批量抓取、下载某学者的全部论文并生成结构化文献消化报告。

**前提**：Edge/Chrome 需先通过 `chromium_helper.launch_browser()` 启动，或已手动打开（`--remote-debugging-port=19222`）。

## CLI 命令速查

| 模式 | 命令 |
|------|------|
| 完整流程（抓取+DOI+下载+模板） | `python <skill-base>/people.py "SCHOLAR_URL" --download` |
| 仅抓取测试 | `python <skill-base>/people.py "SCHOLAR_URL" --scrape-only` |
| 断点续传下载 | `python <skill-base>/people.py --download-only --scholar-name "学者名"` |
| 仅生成消化模板 | `python <skill-base>/people.py --template-only --scholar-name "学者名"` |
| 限制篇数测试 | `python <skill-base>/people.py "URL" --scrape-only --max-papers 5` |
| 第二轮重试（失败论文） | `python <skill-base>/people.py --retry --scholar-name "学者名"` |

## 处理流程

- **Phase 1**: Playwright CDP 抓取 Scholar Profile → 过滤专利/会议 → 去重 preprint/正式版
- **Phase 1b**: CrossRef 搜索标题匹配 DOI（排除补充材料 `.sNNN`，preprint 降权）
- **Phase 1c**: 作者数据库构建 — 从 CrossRef 提取通讯作者全名、affiliation、缩写，存入 `people/data/authors_db.json`
- **Phase 2**: 在 Zotero 创建 `People/<学者名>` collection
- **Phase 3**: 按年份先后线性下载（默认关闭，需 `--download` 启用）
- **Phase 4**: 生成文献消化模板（4 Block + ⚡ cross-talk 区）

## 批量下载策略

默认关闭（`--download` 显式启用）。建议 cron 线性下载（10-15min/篇），用 `--download-only` 做断点续传。一次性大量下载会触发出版商 access 封禁。

## 关键陷阱

1. **`subprocess.run()` 必须加 timeout**。`zot.download_pdf()` 传 `timeout=120`，超时后 `raise RuntimeError`，`download_one_paper` 捕获后标记 `dl_status=failed` 继续下篇。

2. **每篇下载后必须保存进度**（`download_batch` 的 `save_callback` 参数）。不保存 → 进程被 kill 后全部重来。调用方传 `save_callback=lambda papers: save_papers(...)`，每篇后自动 JSON 落盘。重跑时 `resume=True` 跳过 `dl_status=success` 的篇。

3. **`--no-warmup` 加速**：单篇下载加 `--no-warmup` 跳过 Chromium 热身（节省 ~15s/篇）。批量场景下 Chromium 已稳定，warmup 多余。`zot.py` 的 `download_pdf()` 调用 `main.py` 时默认带 warmup，可改 cmd 加 `--no-warmup` 提速。

4. **DOI 解析失败（RSC `RemoteDisconnected`）**：`resolve_doi()` 用 `requests.head()` → RSC 拒绝 HEAD 连接。已在 `url_parser.py` 改为 `requests.get()` + 浏览器 UA header。新增出版商类似问题先查 `resolve_doi()` 是否用 HEAD。

5. **Scholar 截断作者 `...` 破坏 Zotero API**：Scholar 抓取的 `authors` 字符串结尾有 `, ...`，`add_to_zotero()` 会创建 `lastName="..."` 的 creator，Zotero API 400。修复：`download_one_paper` 过滤 `[a for a in raw if a and a != "..." and len(a) > 1]`。

6. **第二轮重试 `--retry`**：加载已有 papers.json，对第一轮失败的论文自动分类处理：
   - SPIE 会议（DOI `10.1117/12.`）→ 标记 `conference` 不再重试
   - 超时失败 → 用 180s timeout 重试
   - "did not produce PDF" → 重试（可能因新适配器已就绪而成功）
   - 每篇重试后自动保存进度

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
- 下载前确保 Edge/Chrome 已启动（`chromium_helper.launch_browser()`）

## 故障排查

| 问题 | 原因 | 解决 |
|------|------|------|
| DOI resolve 失败（如 RSC `RemoteDisconnected`） | 部分出版商（RSC）拒绝 `requests.head()` | 已在 `url_parser.py` 修复为 `GET` + 浏览器 UA |
| Zotero API `'firstName' field must be set` | Scholar 截断作者 `...` 传入 `add_to_zotero()` | `people.py` 的 `download_one_paper()` 已自动过滤 |
| 论文抓取后数量不对 | `CONFERENCE_KEYWORDS` 漏了该会议 | 在 `people.py` 的 `CONFERENCE_KEYWORDS` 列表追加 |
| `config.yaml` 路径不匹配 | gitclone 后路径中的用户名不同 | 手动修正 `temp_dir` 和 `storage_path` |
| CDP 连接失败 | Edge 未启动或端口不对 | 先运行 `chromium_helper.launch_browser()` 或手动 `start_browser.bat` |
| 批量下载永远跑不完（进程挂起） | `subprocess.run()` 无 timeout | 已在 `zot.download_pdf()` 加 `timeout=120` 参数 |
| PDF 下载失败率高 | 部分出版商无适配器或页面结构变化 | 查看本指南的「已知不支持/易失败的出版商」 |
| 批量下载有失败项 | 部分出版商超时或无订阅 | 用 `--retry` 启动第二轮重试 |
