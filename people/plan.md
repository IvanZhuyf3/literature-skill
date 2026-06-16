# Plan: `/literature-skill -people` 功能

> **状态**: DRAFT v2 — 等待师兄确认后实施
> **更新**: 2025-06-15
> **变更**: v2 融入师兄反馈——Playwright CDP、会议直接排除、CrossRef+出版商组合匹配、cron 线性下载、cross-talk 迭代 workflow

---

## 一、功能概述

用户提供一位学者的 Google Scholar Profile URL，自动完成：
1. 在 Zotero 指定位置找到/新建该学者的 collection
2. 按年份顺序下载该学者所有论文（排除专利、会议）
3. 生成结构化文献消化模板，按 4 个 block 系统性阅读和总结

---

## 二、整体流程

```
用户给出 Scholar Profile URL
        │
        ▼
┌─ Phase 1: Scholar 抓取 ──────────────────────┐
│  Playwright CDP 连接 Chrome                    │
│  → 加载 Profile 页面                            │
│  → 反复点击 "Show More" 直到加载全部论文           │
│  → 解析每条论文: 标题/作者/venue/年份/citations   │
│  → 过滤: 排除 Patent + 会议                      │
│  → 输出 <name>_papers.json                     │
└────────────────────────────────────────────────┘
        │
        ▼
┌─ Phase 2: DOI 匹配 ──────────────────────────┐
│  逐篇 CrossRef query.bibliographic 匹配         │
│  → score > 70: 直接采用                         │
│  → score ≤ 70 或无匹配: 标记为 "需出版商页面"      │
│  → 对低分论文: 点进 Scholar→出版商页面提取 DOI     │
│  → 输出 <name>_matched.json                    │
└────────────────────────────────────────────────┘
        │
        ▼
┌─ Phase 3: Zotero Collection ─────────────────┐
│  查找 parent collection（config 配置）            │
│  → 找到/新建 "People/<学者名>" sub-collection    │
│  → 记录 collection key                          │
└────────────────────────────────────────────────┘
        │
        ▼
┌─ Phase 4: 批量下载（cron 线性执行）──────────────┐
│  按年份从早到晚排序                              │
│  → 每次 cron tick 处理 1 篇                      │
│  → main.py 下载 PDF                             │
│  → zot.py 添加到 Zotero + 挂载 PDF + 归入 collection │
│  → 更新 state file（断点续传）                    │
│  → 全部完成后通知师兄                            │
└────────────────────────────────────────────────┘
        │
        ▼
┌─ Phase 5: 文献消化（Agent 驱动）────────────────┐
│  迭代式 workflow（详见第五节）                    │
│  → 输出 <学者名>_digest.md                      │
└────────────────────────────────────────────────┘
```

---

## 三、配置设计

在 `config.yaml` 新增 `people` 段：

```yaml
people:
  # Zotero 中存放学者 collection 的父 collection
  parent_collection: "People"

  # 过滤规则——会议和专利直接排除
  exclude_types:
    - "Patent"
  exclude_venues:
    - "SPIE"
    - "CLEO"
    - "Conference"
    - "Proceedings"
    - "OSA"
    - "COSI"
    - "BiOS"
  # 注意：exclude_venues 是关键词匹配（不区分大小写，子串匹配）
  # 可能误伤，如 "OSA Frontiers in Optics" 是会议但 "OSA Continuum" 是期刊
  # → 用两级过滤：先关键词粗筛，再人工确认（dry-run 输出被排除列表）

  # Scholar 抓取设置（Playwright CDP）
  scholar:
    page_delay: 3000        # Show More 点击间隔（毫秒）
    max_show_more: 50       # 最大点击次数

  # 下载设置——cron 线性执行
  download:
    mode: cron              # cron 线性执行模式
    cron_interval: "*/10 * * * *"  # 每 10 分钟处理一篇
    papers_per_tick: 1      # 每次 cron tick 处理几篇

  # 文献消化输出目录
  digest_dir: "./people/digests"
```

### 会议论文过滤策略

师兄确认"我们领域会议不重要，直接排除"。实现方式：

1. **Google Scholar 页面线索**：Profile 页面的 venue 文字
2. **关键词匹配**：上表 `exclude_venues` 列表，子串匹配（不区分大小写）
3. **人工确认**：`--dry-run` 时输出被排除列表，师兄可检查误伤
4. **关键词可配置**：师兄可在 config 中增删关键词

**已知局限**：Scholar venue 格式不统一（如 `Proc. SPIE` vs `SPIE BiOS`），关键词可能遗漏或误伤。dry-run 时人工确认是必要的。

---

## 四、Google Scholar 抓取方案（Playwright CDP）

### 4.1 技术实现

复用现有 `chromium_helper.py` 的 CDP 连接基础设施：

```python
# people.py 核心抓取流程
async def scrape_scholar_profile(page_url, config):
    browser = await connect_cdp(config['cdp_url'])
    page = await browser.new_page()

    # 1. 加载 Profile 页面
    await page.goto(page_url)

    # 2. 按年份排序（Scholar Profile 有 "Sort by Date" 按钮）
    #    Scholar Profile 默认按 "Last added" 排序
    #    点击 "Sort by Date" 改为按年份排序

    # 3. 反复点击 "Show More" 加载全部
    papers = []
    for _ in range(config['max_show_more']):
        # 解析当前页面的论文条目
        items = await page.query_selector_all('.gsc_a_tr')
        for item in items:
            paper = parse_scholar_entry(item)
            papers.append(paper)

        # 点击 Show More
        show_more = await page.query_selector('#gsc_bpf_more')
        if not show_more or await show_more.is_disabled():
            break
        await show_more.click()
        await page.wait_for_timeout(config['page_delay'])

    # 4. 过滤专利和会议
    papers = filter_papers(papers, config)

    return papers
```

### 4.2 条目解析

每个 Scholar 条目 (`<tr class="gsc_a_tr">`) 包含：

```
┌─────────────────────────────────────────┐
│ 标题（链接到详情页）                        │  ← .gsc_a_at
│ 作者列表, Venue, 年份                      │  ← .gs_gray div
│ [CITATION] / [PDF] / [LINK] 标记          │
└─────────────────────────────────────────┘
```

解析字段：
- **标题**: `.gsc_a_at` 文本
- **作者+venue**: `.gs_gray` 两个 div，第一个是作者，第二个是 venue+年份
- **年份**: `.gsc_a_h` 文本
- **引用数**: `.gsc_a_c` 文本
- **专利标记**: 条目含 `[PATENT]` 或链接到 google patents

### 4.3 DOI 匹配（CrossRef + 出版商页面）

```python
def match_dois(papers):
    for paper in papers:
        # Step 1: CrossRef 匹配
        result = crossref_query(paper['title'], paper['authors'], paper['year'])
        if result and result['score'] > 70:
            paper['doi'] = result['doi']
            paper['match_method'] = 'crossref'
            continue

        # Step 2: 低分 → 打开 Scholar 详情页找出版商链接
        paper['doi'] = find_doi_from_publisher(paper['scholar_detail_url'])
        paper['match_method'] = 'publisher_page'

        # Step 3: 仍然找不到 → 标记
        if not paper['doi']:
            paper['doi'] = None
            paper['match_method'] = 'unmatched'

    return papers
```

出版商页面 DOI 提取：
- 点进 Scholar 条目的标题链接 → Scholar 文章详情页
- 详情页有 "View [PDF]" 或 publisher 链接 → 跟踪到出版商页面
- 出版商页面的 DOI 通常在 meta 标签：`<meta name="citation_doi">`

---

## 五、文献消化 Workflow（核心设计）

### 5.1 Cross-Talk 问题

4 个 Block 不是独立的信息孤岛，它们之间存在交叉关联：

| Cross-Talk | 说明 | 示例 |
|------------|------|------|
| Block 1 ↔ Block 2 | 合作者变化与研究主题变迁耦合 | 新合作者引入了新方法 → Block 1 的方法论转折点 |
| Block 1 ↔ Block 3 | 综述覆盖的研究脉络影响时间线划分 | 综述定义了"阶段划分"→ 更新 Block 1 的研究主题分类 |
| Block 1 ↔ Block 4 | 高引论文定义研究方向的起点/转折 | 高引论文开辟新方向 → Block 1 新增研究时期 |
| Block 2 ↔ Block 4 | 高引论文的合作模式 | 核心合作者关系的形成 → Block 2 合作模式分析 |
| Block 3 ↔ Block 4 | 综述引用/总结了高引论文 | 综述对高引论文的定位 → 深读时参考综述框架 |

### 5.2 迭代式 Workflow：三圈螺旋

**核心理念**：不是线性 1→2→3→4，而是 **骨架 → 深读 → 整合** 的螺旋迭代，每深读一篇都可能触发跨 Block 更新。

```
第一圈：鸟瞰（Skeleton Pass）
═══════════════════════════════
  读所有标题+摘要+元数据
      │
      ├──→ Block 1 骨架: 按年份分组，划分研究时期，粗略标注研究对象/方法
      ├──→ Block 2 骨架: 合作者频次表，识别核心合作者
      ├──→ Block 3 骨架: 标记综述候选
      └──→ Block 4 骨架: 按引用数排序，标记高引候选

  同时建立「统一时间线」作为所有 Block 的共享基座（见 5.3）


第二圈：深读（Deep-Read Pass）
═══════════════════════════════
  深读顺序: Block 3（综述）→ Block 4（高引）→ Block 1/2 关键节点

  为什么先读综述？
  → 综述提供了领域全景和技术框架，是理解其他论文的 lens
  → 用综述建立框架后，读高引和关键论文更高效

  每读完一篇 → 触发 Cross-Talk Check：
  ┌──────────────────────────────────────────────────┐
  │ Cross-Talk Check（每篇论文读完后执行）              │
  │                                                    │
  │ 1. 研究主题？ → 是否更新 Block 1 的研究时期划分？     │
  │ 2. 关键合作者？ → 是否更新 Block 2 的合作网络？       │
  │ 3. 方法学转变？ → 是否更新 Block 1 的转折点？         │
  │ 4. 高影响力？ → 是否需要提升到 Block 4？             │
  │ 5. 被综述覆盖？ → 是否与 Block 3 的框架呼应？         │
  │                                                    │
  │ → 如有更新: 在目标 Block 添加 ⚡ 标记 + 待写内容       │
  └──────────────────────────────────────────────────┘


第三圈：整合（Integration Pass）
═══════════════════════════════
  回到 Block 1: 用深读获得的洞察完善时间线，写分析段落
  回到 Block 2: 用深读发现的合作细节完善网络，写合作模式
  检查所有 ⚡ 标记: 确认每条 cross-talk 更新都已处理
  检查时间一致性: Block 1/2/3/4 的时间线是否矛盾
  最终输出: 清理标记，输出完整 digest.md
```

### 5.3 统一时间线（共享基座）

所有 Block 共享一个时间线数据结构，任何时间相关的发现都锚定到此：

```python
# people/data/<name>_timeline.json
{
  "scholar": "Peter T. C. So",
  "timeline": [
    {
      "period": "1995-2000",
      "research_objects": ["multiphoton microscopy", "fluorescence"],
      "core_methods": ["Ti:Sapphire laser", "TCSPC"],
      "key_collaborators": ["...", "..."],
      "representative_papers": [{"doi": "...", "title": "..."}],
      "notes": "早期聚焦仪器开发",
      # ⚡ 标记: deep-read 后可能更新
      "pending_updates": ["⚡ Block 2: 与 XX 的合作始于此时期"]
    },
    ...
  ]
}
```

**统一时间线的价值**：
- Block 1 写"研究脉络"时，直接引用 timeline 的 `research_objects` 和 `core_methods`
- Block 2 写"合作者网络"时，直接引用 timeline 的 `key_collaborators`
- 当 Block 2 发现新合作者，更新 timeline → Block 1 的研究时期描述自动有据可依
- 消除"Block 1 说了 A，Block 2 说了 B，但 A 和 B 在时间上矛盾"的问题

### 5.4 Cross-Talk 处理机制

**⚡ 待更新标记系统**：

在深读过程中，发现某内容需要更新另一个 Block 时：

```markdown
<!-- 在 Block 2 中读到关于某合作者引入 SRS 技术 -->
⚡ → Block 1: 合作者 XXX (2010-) 引入了 SRS 方法，
   需在 Block 1 的 "方法论转折点" 中补充 SRS 的引入

<!-- 在 Block 3 的综述中发现综述定义了三个研究阶段 -->
⚡ → Block 1: 综述(2015)将研究分为 "仪器→生物应用→临床转化"，
   需更新 Block 1 的研究主题分类
```

**处理规则**：
1. 深读时只打标记 + 写关键词，不立即跳到其他 Block（保持当前阅读流）
2. 当前 Block 的一个子任务（如"读所有综述"）完成后，批量处理该 Block 产生的所有 ⚡ 标记
3. Integration Pass 统一检查所有 ⚡ 标记是否已处理

### 5.5 具体 Workflow（Agent 执行顺序）

```
Step 0: 准备
  → 读取 <name>_papers.json（所有论文元数据）
  → 按年份排序

Step 1: 鸟瞰（Skeleton Pass）
  1a. 通读所有标题+摘要
      → 建立 timeline.json（统一时间线）
      → 填充 Block 1: 研究时期划分 + 粗略描述
  1b. 统计合作者频次
      → 填充 Block 2: 合作者频次表 + 核心团队
  1c. 标记综述和高引论文
      → 填充 Block 3/4 的候选列表

Step 2: 深读综述（Block 3 Deep-Read）
  → 逐篇读综述 PDF
  → 填充 Block 3: 综述要点
  → 每篇触发 ⚡ Cross-Talk Check

Step 3: 深读高引论文（Block 4 Deep-Read）
  → 按 Top 10 逐篇读 PDF
  → 填充 Block 4: 逐篇深读
  → 每篇触发 ⚡ Cross-Talk Check

Step 4: 补读关键节点论文
  → 根据 Block 1 时间线中的转折年份，
     补读该年份的非高引但关键论文
  → 触发 ⚡ Cross-Talk Check

Step 5: 整合（Integration Pass）
  5a. 回到 Block 1: 用深读洞察完善时间线
      → 处理所有指向 Block 1 的 ⚡ 标记
      → 写研究主题分类和方法论转折点分析段落
  5b. 回到 Block 2: 用深读发现的合作细节完善网络
      → 处理所有指向 Block 2 的 ⚡ 标记
      → 写合作模式分析段落
  5c. 检查所有 ⚡ 标记是否已处理
  5d. 检查时间一致性
  5e. 清理标记，输出最终 digest.md
```

---

## 六、Cron 线性下载方案

### 6.1 为什么用 Cron

连续批量下载会触发出版商 access 限制（IP 封禁、session 过期）。师兄建议用 cron job，每 10 分钟处理一篇，线性执行。

### 6.2 实现方式

**方案 A（推荐）：Hermes Cron Job**

在 people.py 中实现 `--next` 模式：每次执行只处理状态文件中的下一篇论文。

```bash
# cron 每 10 分钟执行一次
*/10 * * * * cd /path/to/skill && python people.py "URL" --next
```

**状态文件** `people/data/<name>_state.json`：

```json
{
  "scholar": "Peter T. C. So",
  "scholar_url": "https://scholar.google.com/...",
  "total_papers": 150,
  "downloaded": 47,
  "failed": 3,
  "skipped": 2,
  "status": "downloading",
  "queue": [
    {"doi": "10.1038/...", "title": "...", "status": "done"},
    {"doi": "10.1021/...", "title": "...", "status": "pending"},
    {"doi": null, "title": "...", "status": "failed", "reason": "no DOI"}
  ],
  "last_run": "2025-06-15T14:30:00",
  "collection_key": "ABCDEFGH"
}
```

每次 `--next` 执行：
1. 读取 state file
2. 找到第一个 `status: "pending"` 的论文
3. 下载 PDF → 添加 Zotero → 挂载 PDF
4. 更新 status → 保存 state file
5. 如果全部完成 → status 改为 `complete`，通知师兄

### 6.3 Hermes Cron Job 配置

```yaml
# Hermes cron job（通过 hermes cron create 或 plan 执行时创建）
schedule: "*/10 * * * *"
prompt: |
  继续下载 <学者名> 的论文。
  运行: cd $SKILL_DIR && python people.py "URL" --next
  如果输出显示 "All papers downloaded"，通知师兄下载完成。
deliver: origin   # 发到当前微信对话
```

---

## 七、文献消化模板

文件名: `people/digests/<学者姓>_digest.md`

```markdown
# <学者全名> — 文献消化报告

> 生成时间: YYYY-MM-DD
> 论文总数: N 篇（去重、过滤后）
> 时间跨度: YYYY – YYYY
> Scholar Profile: <URL>
> Workflow: 三圈螺旋（骨架→深读→整合）

---

## Block 1: 研究脉络 — 研究对象与核心方法的变迁

> 通读所有论文标题和摘要，按时间线梳理研究对象和核心方法如何演变。
> ⚡ 本 Block 在 Integration Pass 中会用深读洞察进一步完善。

### 时间线总览

| 时期 | 研究对象 | 核心方法 | 代表论文 |
|------|---------|---------|---------|
| YYYY–YYYY | ... | ... | [标题] (DOI) |
| YYYY–YYYY | ... | ... | [标题] (DOI) |

### 方法论转折点

- **YYYY**: [关键转变描述]
  - 触发: [什么推动了转变 — 新技术/新合作/新领域]
  - 论文: [标题] (DOI)
- ...

### 研究主题分类

按研究内容聚类，标注每类的核心贡献：
1. **主题 A** (YYYY–YYYY): ...
2. **主题 B** (YYYY–YYYY): ...
3. ...

---

## Block 2: 合作者网络

> 从作者列表中提取高频合作者，识别核心团队和外部合作。
> ⚡ 合作者变化与 Block 1 的研究主题变迁耦合，参见 Block 1 对应时期的描述。

### 核心合作者（≥3 篇共作）

| 合作者 | 共作篇数 | 机构（推测） | 主要合作主题 | 活跃时期 |
|--------|---------|-------------|-------------|---------|
| ... | N | ... | ... | YYYY–YYYY |

### 合作模式

- **实验室内部**: [学生/博后序列，从作者位置变化看培养路径]
- **跨机构合作**: [关键外部合作者及其贡献领域]
- **产业合作**: [如有]

---

## Block 3: 综述文章精读

> 识别该学者的 review/survey 论文，作为理解其研究领域的入口。
> ⚡ 综述提供的框架已反馈到 Block 1 的研究时期划分。

### 综述清单

| 年份 | 标题 | 期刊 | DOI |
|------|------|------|-----|
| YYYY | ... | ... | ... |

### 综述要点

对每篇综述：
- **覆盖范围**: ...
- **核心观点**: ...
- **技术框架**: ...
- **与其他综述的关系**: ...

---

## Block 4: 核心高引论文深读

> 按引用数排序的前 N 篇论文，深入分析其贡献。
> ⚡ 高引论文的研究方向已反馈到 Block 1 的研究主题分类。

### 高引论文 Top 10

| 排名 | 引用数 | 年份 | 标题 | DOI |
|------|--------|------|------|-----|
| 1 | N | YYYY | ... | ... |

### 逐篇深读

对每篇高引论文：
- **解决的问题**: ...
- **核心创新**: ...
- **方法细节**: ...
- **影响**: 为什么被高引？开辟了什么方向？
- **与该学者其他工作的关系**: ...

---

## 附录

### A. 完整论文列表

| # | 年份 | 标题 | Venue | Citations | DOI |
|---|------|------|-------|-----------|-----|
| 1 | YYYY | ... | ... | N | ... |

### B. 下载状态

| 状态 | 数量 |
|------|------|
| 已下载 | N |
| 下载失败 | N |
| 无 DOI（未匹配） | N |

### C. 失败列表

- [标题] — 原因: [timeout/no_access/unmatched DOI]
```

---

## 八、文件结构

```
Literature_skill/
├── people.py                     ← 新增: 主入口脚本
├── people/
│   ├── plan.md                   ← 本文件
│   ├── digests/                  ← 文献消化报告输出目录
│   │   └── <name>_digest.md
│   └── data/                     ← 中间数据
│       ├── <name>_papers.json    ← Scholar 抓取的原始论文列表
│       ├── <name>_matched.json   ← CrossRef + 出版商 DOI 匹配结果
│       ├── <name>_state.json     ← 下载进度状态（cron 断点续传）
│       └── <name>_timeline.json  ← 统一时间线（cross-talk 基座）
├── templates/
│   └── digest_template.md        ← 文献消化模板
└── （现有文件不变）
```

---

## 九、命令接口

```bash
# === 完整流程 ===
set PYTHONIOENCODING=utf-8 && python people.py "https://scholar.google.com/citations?user=XXXX"

# === 分步执行 ===

# Step 1: 只抓取论文列表（不下载），生成 papers.json
python people.py "URL" --scrape-only

# Step 2: 只做 DOI 匹配（需要已有 papers.json）
python people.py "URL" --match-only

# Step 3: 创建 Zotero collection
python people.py "URL" --setup-collection

# Step 4: 下载下一篇（cron 模式）
python people.py "URL" --next

# Step 5: 只生成消化模板（论文已下载到 Zotero）
python people.py "URL" --template-only

# === 辅助 ===

# Dry run: 打印计划 + 被排除的论文列表，不执行
python people.py "URL" --dry-run

# 限制篇数（测试用）
python people.py "URL" --max-papers 5

# 查看下载进度
python people.py "URL" --status

# 指定 Zotero collection（覆盖 config）
python people.py "URL" --collection-key XXXXXXXX
```

---

## 十、实施步骤（确认后执行）

1. **`people.py`** — Scholar 抓取 + CrossRef/出版商 DOI 匹配 + Zotero collection 管理 + cron --next 下载
2. **`templates/digest_template.md`** — 文献消化模板
3. **`config.yaml`** — 添加 `people` 段
4. **`SKILL.md`** — 添加 `-people` 子命令文档
5. **测试 Scholar 抓取** — 用师兄给的 Scholar Profile 实际跑一次 `--scrape-only`
6. **测试下载** — 用 `--max-papers 3` 测试 cron 下载流程
7. **测试消化** — 手动执行三圈螺旋 workflow
8. **同步到生产环境** — git commit → push → 生产 pull

---

## 十一、已知风险与缓解

| 风险 | 缓解 |
|------|------|
| Scholar CAPTCHA/封禁 | 用 CDP 连接真实 Chrome；`page_delay` 间隔；被封暂停 |
| CrossRef 匹配率不足 | 低分论文打开出版商页面提取 DOI；仍不行记录到 unmatched |
| 会议论文过滤误伤 | `--dry-run` 输出被排除列表，师兄确认后再正式执行 |
| Cron 下载中断（电脑休眠等） | state file 记录进度，下次 `--next` 自动续传 |
| 出版商不在支持列表 | 记录到 failed.json，后续按 maintain.md 添加适配器 |
| 文献消化 cross-talk 遗漏 | ⚡ 标记系统 + Integration Pass 统一检查 |
