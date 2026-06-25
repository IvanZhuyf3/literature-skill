# `-people` 子功能设计参考

> 状态: Phase 1-4 全部实现并端到端测试通过（2026-06-15 最小量测试）
> 设计日期: 2025-06-15
> 最后更新: 2026-06-15（端到端全链路测试，3个bug修复，conf路径修正）

## 功能概述

给定一位学者的 Google Scholar Profile URL，自动：
1. 抓取全部论文（排除专利+会议）
2. 在 Zotero 指定 collection 下建立该学者的子文件夹
3. 按年份顺序 cron 线性下载所有论文
4. 生成结构化文献消化报告

## 关键设计决策（师兄拍板）

| 决策点 | 结论 | 理由 |
|--------|------|------|
| Scholar 抓取方案 | Playwright CDP（不用 Semantic Scholar API） | S2 API 找人不准 |
| 会议论文过滤 | 直接排除（关键词匹配） | 该领域会议不重要 |
| DOI 匹配策略 | CrossRef 优先 + 出版商页面兜底 | Scholar 不直接提供 DOI |
| 下载方式 | Cron 线性（10min/篇，`--next` 模式） | 连续下载触发 access 限制 |
| 消化 workflow | 三圈螺旋 + ⚡标记 + 统一时间线 | 处理 Block 间 cross-talk |

## Cross-Talk Workflow（核心方法论）

4 个 Block 不是线性 1→2→3→4，它们之间存在耦合：
- Block 1（研究脉络）↔ Block 2（合作者网络）：合作者变化与研究主题变迁耦合
- Block 1 ↔ Block 3（综述）：综述定义研究阶段划分
- Block 1 ↔ Block 4（高引论文）：高引论文定义方向起点

### 三圈螺旋

```
第一圈：鸟瞰（Skeleton Pass）
  → 通读标题+摘要 → 4 个 Block 同时搭骨架 + 建统一时间线

第二圈：深读（Deep-Read Pass）
  → 先读综述（建框架）→ 再读高引 → 补读关键节点
  → 每篇触发 ⚡ Cross-Talk Check（打标记，不跳走）

第三圈：整合（Integration Pass）
  → 回头处理所有 ⚡ 标记 → 完善 Block 1/2 → 检查时间一致性
```

### 统一时间线（`timeline.json`）

所有 Block 共享一个时间线数据结构。任何时间相关的发现都锚定到此：
- Block 1 写研究脉络时引用 `research_objects` / `core_methods`
- Block 2 写合作网络时引用 `key_collaborators`
- 当 Block 2 发现新合作者，更新 timeline → Block 1 自动有据可依

### ⚡ 标记系统

深读时发现跨 Block 关联 → 只打标记 + 关键词，保持当前阅读流：
```markdown
⚡ → Block 1: 合作者 XXX (2010-) 引入了 SRS 方法，
   需在 Block 1 的方法论转折点中补充
```
处理规则：当前子任务完成后批量处理该 Block 产生的 ⚡ 标记。

## 测试用例

师兄指定自己的 Google Scholar Profile 作为测试：`https://scholar.google.com/citations?user=tSWxyLwAAAAJ`

### 测试结果（2026-06-15：端到端全链路最小量测试）

| 项目 | 结果 |
|------|------|
| Scholar 抓取 | 33 篇→过滤 1 专利+7 会议+1 去重→24 篇 |
| 会议过滤改善 | 原始 `CONFERENCE_KEYWORDS` 漏 5 篇，补充后全过滤 |
| 去重处理 | 1 对 preprint/正式版（entacapone 论文）正确保留正式版 |
| CrossRef DOI 匹配 | 20/24 (83%)，score ≥ 0.95；4 篇未匹配 = arXiv preprint |
| Zotero Collection | `People/Yifan Zhu` (ER9XJDQM) 成功创建 |
| 消化模板 | 24 篇模板生成，Top-10 高引表已填充 |
| **Phase 3 下载（实测）** | ✅ 全链路通过 |
| — DOI resolve | 修复：`HEAD`→`GET` + User-Agent（RSC 拒绝 HEAD） |
| — PDF download | ✅ 1.7 MB RSC 论文成功 |
| — Zotero create | ✅ HTK532AW（修复：过滤 `...` truncated 作者） |
| — Attach PDF | ✅ VRBDQH87 |
| — Collection 归入 | ✅ ER9XJDQM |

### 端到端测试发现的 Bug（已修复，2026-06-15）

1. **DOI resolve 被 RSC 拒绝**：`url_parser.py:resolve_doi()` 用 `requests.head()`，RSC 的 `pubs.rsc.org` 断开 HEAD 连接。改为 `requests.get()` + 浏览器 User-Agent + `stream=True` + `response.close()`。⚠️ 其他出版商也可能有类似行为，未来若出现 DOI resolve 失败，首先尝试此修复。

2. **Scholar 截断作者 `...` 破坏 Zotero API**：Scholar 抓取到的作者列表以 `, ...` 结尾（截断标记），传递到 `zot.add_to_zotero()` 后 Zotero API 返回 `400 'firstName' creator field must be set if 'lastName' is set`。修复：在 `download_one_paper()` 中过滤 `a == "..."` 或 `len(a) <= 1` 的作者。

3. **`config.yaml` 路径与当前机器不匹配**：路径中用户名为 `Yifan` 但实际为 `Ivanz`。⚠️ `config.yaml` 被 gitignore 不跟踪，但 clone 后需要手动修正 `temp_dir` 和 `storage_path` 中的用户名。

### 尚存的限制

- **arXiv DOI 回退**：4 篇 arXiv preprint 未匹配，标题太长 arXiv API search 不 working。考虑从 Scholar 上 arXiv 条目的链接直接提取 arXiv ID。
- **Conference 过滤**：纯关键词匹配仍有遗漏风险，考虑维护期刊白名单。

### 实施状态（2026-06-15）

## Zotero Collection 结构（实现时参考）

师兄的 Zotero library 有 56 个 collections，层级结构。主要顶层 parent collections：
- `PBL7KTGF` — 研究（Spectroscopy, Lasers, Photoacoustic, Hyperspectral 等子文件夹）
- `DXLXPFGU` — 生物学相关（Single-cell, Basic biology, Lipid raft 等）
- `SEYRVUVH` — Video-rate / AOP 相关
- `ZLTEL6K5` — 2_New Knowledge
- `IGWLPV54` — 3_Supplementary Knowledge
- `S67VP3I9` — z_Non_research

**当前不存在 "People" collection**，people feature 实现时需要新建。建议作为顶层 collection 创建（与 PBL7KTGF 平级）。

实现时不要硬编码 collection key，而是在运行时用 `pyzotero` 查询 name→key 映射。

## Phase 1c: 作者数据库（通讯作者）

> 新增 2026-06-16。起因：digest 中将 `KMC Wong` 脑补展开为 `Kenneth MC Wong`，实际全名是 `Keith Man-Chung Wong`（CrossRef 确认，affiliation 南科大）。

### 设计

`people/data/authors_db.json` 持久存储通讯作者的全名、affiliation、已知缩写。跨 session 累积。

**只记录通讯作者**（CrossRef `sequence=corresponding`，否则取末位作者 heuristic）。

### Lookup 优先级（`resolve_author_name()`）

1. **CrossRef**（最可靠）：用 DOI 查完整作者列表，匹配缩写 → 拿全名 + 更新 DB
2. **本地 DB**：按 abbreviation 匹配（`KMC Wong` 和 `KM Wong` 都能命中同一人）
3. **Dirty 标记**：都找不到 → 保留缩写原样，标 `dirty=True`。**绝不猜测全名**

### 已处理的坑

- **Unicode 连字符**：CrossRef 返回 `‐` (U+2010) 而非 `-` (U+002D)，`_normalize_abbrev()` 统一替换 6 种 dash variant
- **连字符姓名缩写**：`Man-Chung` → `MC`（拆分 hyphen 取首字母），同时记录 `KM Wong`（不拆分）作为 alternate abbreviation
- **去重**：同一人因 unicode dash 差异被拆成两条 → normalization 修复

### 当前数据（2026-06-16，24 篇论文）

| 通讯作者 | 缩写 | corr 论文数 |
|---------|------|------------|
| Ji-Xin Cheng | JX Cheng, J Cheng | 12 |
| Keith Man‐Chung Wong | KMC Wong, KM Wong | 3 |
| Chen Yang | C Yang | 2 |
| Denis Jacquemin | D Jacquemin | 1 |
| Chun-Yu Ho | CY Ho, C Ho | 1 |
| Michael Wagner | M Wagner | 1 |

### 核心教训

**Scholar 只提供缩写名（如 `KMC Wong`），绝不能脑补展开**。必须走 CrossRef → DB → dirty 流程。digest Block 2 合作者表填充时，每个名字都要经过 `resolve_author_name()` 验证。

## Cron 线性下载模式

State file (`<name>_state.json`) 记录下载队列和进度。每次 cron tick 执行 `--next`：
1. 读 state file → 找第一个 pending 论文
2. 下载 PDF → 添加 Zotero → 挂载 + 归入 collection
3. 更新 status → 保存 state file
4. 全部完成 → 通知用户

Hermes cron 配置：`*/10 * * * *`，deliver 到 origin（微信对话）。

## 实施状态（2025-06-15）

### Phase 3: 下载 — 已测试通过 ✅

`people.py` 新增函数：

- `download_one_paper(paper, cfg, collection_key)` — 单篇下载流程：
  1. `zot.download_pdf(doi_url, cfg)` — 调用 main.py 下载PDF
  2. `zot.add_to_zotero(meta, cfg)` — CrossRef 元数据创建Zotero item
  3. `zot.attach_pdf(item_key, pdf_path, cfg)` — 挂载附件
  4. `_assign_to_collection(item_key, collection_key, cfg)` — 归入 collection
- `download_batch(papers, cfg, collection_key, resume=True)` — 按年份升序批量下载
- `_assign_to_collection(item_key, collection_key, cfg)` — pyzotero 的 item→collection 分配

批量下载特性：断点续传（跳过 `dl_status='success'`）、每篇保存进度到 JSON、`--download` flag 显式启用。

### Phase 4: 消化模板 — 已实现已验证

`generate_digest_template(papers, scholar_name, scholar_url, cfg)` → 写入 `people/digests/<name>_digest.md`

自动填充：论文总数、时间跨度、DOI 匹配率、Top-10 高引表、review 识别、下载状态统计
手动填充：4 Block 骨架 + ⚡ cross-talk 区

### CLI 参数

| 参数 | 功能 |
|------|------|
| `url` | Scholar Profile URL（必需，除 `--download-only`/`--template-only`） |
| `--scrape-only` | 只抓取，不建 Zotero 不下载 |
| `--download` | **启用 Phase 3 下载**（默认关闭防误操作） |
| `--download-only` | 载入已有 papers.json 执行下载（断点续传） |
| `--template-only` | 载入已有 papers.json 生成模板 |
| `--max-papers N` | 限制篇数（测试用） |
| `--dry-run` | 抓取+DOI 匹配，不做 Zotero/下载 |
| `--no-doi-match` | 跳过 DOI 匹配 |
| `--scholar-name` | 覆盖学者名（`--download-only`/`--template-only` 时需要） |

### 去重逻辑

`deduplicate_papers()` 在 `filter_papers()` 中调用：
- `title_similarity ≥ 0.85` 检测相同论文
- preprint venue（bioRxiv/arXiv/chemRxiv/medRxiv/preprint）vs 正式版 → 保留正式版
- 同为 preprint 或同为正式版 → 保留高引用者

### save_papers 更新

新增 `scholar_url` 字段，使 `--template-only` 能恢复 Scholar Profile 链接到模板头。
注：`--download-only` 路径的 `scholar_url` 来自已持久化的 JSON，新抓取时从 args.url 传入。

## Implementation Notes（实测验证，2025-06-15）

### Google Scholar DOM 结构（实测）

每篇论文行 `#gsc_a_b .gsc_a_tr` 的 HTML：

```html
<td class="gsc_a_t">
  <a class="gsc_a_at" href="/citations?...citation_for_view=USER:HASH">Title</a>
  <div class="gs_gray">Y Zhu, JX Cheng</div>           <!-- 作者 -->
  <div class="gs_gray">Venue 152 (2)<span class="gs_oph">, 2020</span></div>  <!-- venue+year -->
</td>
<td class="gsc_a_c"><a class="gsc_a_ac gs_ibl">96</a></td>  <!-- citations -->
<td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2020</span></td>  <!-- year -->
```

**Pitfall**: 作者和 venue 在 `.gs_gray` divs 里，**不是** `.gsc_a_g`（旧猜测）。用 `row.query_selector_all(".gs_gray")` 取，第一个是作者，第二个是 venue（含 `<span class="gs_oph">, YYYY` 需 strip）。

### "Show More" 按钮

- Selector: `#gsc_bpf_more`
- 判断加载完成：`get_attribute("disabled") is not None`（按钮 disabled = 全部加载）
- Page delay: 3000ms 足够（Scholar 默认 20 条/页）

### CrossRef DOI 匹配 Pitfalls（实测）

1. **补充材料 DOI**：CrossRef 返回 `10.1021/acs.analchem.1c03604.s001`（`.sNNN` 后缀）。必须用 regex `\.s\d{3}$` 过滤掉，否则匹配到补充材料而非正文。
2. **Preprint 优先级**：CrossRef 可能同时返回 bioRxiv preprint（type=`posted-content`）和正式发表版。给 preprint 乘 0.95 penalty，确保正式版优先。
3. **arXiv preprint 无法匹配**：arXiv 论文不在 CrossRef，score=0。需要单独走 arXiv API 或出版商页面兜底。
4. **同一论文的 preprint + 正式版**：Scholar Profile 可能同时列出 bioRxiv preprint 和正式版（如 Yifan Zhu 的 entacapone 论文，bioRxiv 1 引用 vs Nature Microbiology 15引用），需要在 `deduplicate_papers()` 中用 title_similarity ≥ 0.85 检测 + venue 判断。保留正式版（高引用或非 preprint venue）。
5. **阈值**：`title_similarity` (SequenceMatcher) ≥ 0.7 采用。实测 25/30 匹配率，未匹配的全是 arXiv preprint。

### 会议论文过滤的遗漏

`CONFERENCE_KEYWORDS` 关键词匹配有遗漏。实测以下 venue 文本未被捕获（因不含标准会议关键词）：
- `"Frontiers in Optics"` → 实际是 OSA 会议
- `"Imaging Systems and Applications"` → 会议
- `"Microscopy Histopathology and ..." ` → 会议

**改进方向**：Scholar Profile 的 venue 字段格式不统一，纯关键词匹配不够。可能需要维护一个已知期刊白名单，不在白名单中的按可疑处理。

### Zotero Collection 创建（实测）

- 父 collection "People" (key: WI2ZXCM3) 作为顶层 collection
- 子 collection "Yifan Zhu" (key: ER9XJDQM)
- `pyzotero` 的 `create_collections()` 返回 `resp["successful"]["0"]["key"]` 获取 key

## 文件结构（规划）

```
literature-skill/
├── people.py                    ← 主入口
├── people/
│   ├── plan.md                  ← 详细设计文档
│   ├── digests/<name>_digest.md ← 消化报告输出
│   └── data/                    ← 中间数据
│       ├── <name>_papers.json   ← Scholar 抓取结果
│       ├── <name>_state.json    ← 下载进度（断点续传）
│       └── <name>_timeline.json ← 统一时间线
├── templates/digest_template.md ← 消化模板
```
