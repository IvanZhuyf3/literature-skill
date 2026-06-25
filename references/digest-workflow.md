# Digest 填充工作流（Step 8）

> `-people` 的 Phase 4 生成模板后，由 agent 手动填充 4 个 Block。模板在 `people/digests/<name>_digest.md`。

## 作者名解析规则（Block 2 合作者表必用）

Scholar 抓取的作者名是缩写（如 `KMC Wong`、`JX Cheng`），**绝对不能脑补展开**（曾将 Keith Man-Chung Wong 错写成 Kenneth MC Wong）。填充 Block 2 合作者表时，必须按以下优先级解析全名：

1. **CrossRef 查询**（最可靠）：用论文 DOI 调 `fetch_crossref_authors(doi)` 拿完整作者列表。CrossRef 的 `given` + `family` 是全名。
2. **本地作者数据库**（`people/data/authors_db.json`）：调 `resolve_author_name(abbrev, doi, db)`，自动走 CrossRef→DB→dirty 流程。DB 只存通讯作者，跨 session 持久累积。
3. **dirty 标记**：CrossRef 和 DB 都找不到 → 保留缩写原样，标 `dirty=True`。不要猜测全名。

**调用方式**：
```python
from people import resolve_author_name, load_authors_db
db = load_authors_db()
full_name, is_dirty = resolve_author_name("KMC Wong", "10.1039/c6cc03431d", db)
# → ("Keith Man-Chung Wong", False)
```

**已处理的坑**：
- CrossRef 返回的连字符有 unicode 变体（`‐` U+2010 vs `-` U+002D），`_normalize_abbrev()` 已统一处理
- 连字符姓名缩写：`Man-Chung` → `MC`（不是 `M`），代码会同时记录 `KMC Wong` 和 `KM Wong` 两种缩写
- DB 只记录通讯作者（CrossRef `sequence=corresponding`，否则取末位作者）

## 三圈螺旋工作流

4 个 Block 之间存在耦合（合作者影响研究方向、综述定义阶段划分、高引论文定义起点），不能线性 1→2→3→4。用三圈螺旋：

```
第一圈：鸟瞰（Skeleton Pass）
  → 通读标题+摘要
  → 同时搭 4 个 Block 的骨架
  → 建统一时间线（research_objects, core_methods, key_collaborators）

第二圈：深读（Deep-Read Pass）
  → 先读综述（建理解框架）
  → 再读高引论文（理解核心贡献）
  → 补读关键节点论文
  → 每篇发现跨 Block 关系 → 打 ⚡ 标记，不跳走

第三圈：整合（Integration Pass）
  → 回头处理所有 ⚡ 标记
  → 完善 Block 1 的时间线和 Block 2 的合作者网络
  → 检查时间一致性
```

## 统一时间线

所有 Block 共享时间线。发现跨 Block 关联时（如 Block 2 发现新合作者在 2019 年引入了 SRS），不仅更新 Block 2 也更新 Block 1 的方法论转折点。

## ⚡ 标记规则

深读时发现跨 Block 关联 → 只打标记，保持当前阅读流：

```markdown
⚡ → Block 1: 合作者 XXX (2019-) 引入 SRS 方法，
   需在 Block 1 方法论转折点中补充
```

处理时机：当前 Block 填完后，批量处理所有积累的 ⚡ 标记。

## 增量消化（Reinforcement Digest）

当学者有新论文时，**不要重新生成 digest**。已有分析（深读笔记、cross-talk 标记、合作者推理）是不可再生的，全量重新生成会冲掉。

### 触发条件

用户说"更新 digest"/"补消化"/"有新论文了"等，或者 `lit track` 发现新论文后自动衔接。

### 工作流

#### Step 1：发现新论文

```bash
# 读已有 digest.md 的附录 A（完整论文列表），提取所有 DOI
# → 读 Zotero 当前 collection 的条目 DOI
# → 差集 = 新增论文
```

附录 A 的表格格式固定：`| # | 年份 | 标题 | Venue | DOI |`，可以用 `read_file` + 正则提取 DOI 列。

#### Step 2：逐篇分析新论文

对每篇新论文：

1. **确保 PDF 已下载**：`lit quick <DOI>` → `lit attach <DOI>`（如果还没下）
2. **解析 PDF**：`lit parse <pdf> --item-key <key>` → 拿到全文 Markdown
3. **深读分析**：按 digest-workflow 的深读标准，提取：
   - 研究对象和核心方法
   - 合作者
   - 是否综述
   - 与已有研究的关联

#### Step 3：手术式更新 digest.md

**原则：只追加/修改受影响的部分，绝不覆盖已有分析。**

对每篇新论文，判断它影响哪些 Block：

| 新论文特征 | 影响的 Block | 操作 |
|-----------|-------------|------|
| 新方法/新方向 | Block 1 方法论转折点 | 追加条目 |
| 新合作者 | Block 2 合作者表 | 新增行或更新共作篇数 |
| 综述/review | Block 3 综述清单 | 新增行 + 补充要点 |
| 高引（改变 Top 10） | Block 4 高引表 | 更新排名表 |
| 任何论文 | 附录 A | 追加行 |

更新时用 `patch` 工具做定向编辑，不是重写整个文件。

#### Step 4：Cross-talk 检查

新论文是否与已有 Block 内容有关联？
- 新合作者引入了新方法 → Block 1 + Block 2 都要更新
- 新论文引用了已有高引论文 → 在 Block 4 补充关联
- 发现关联 → 打 ⚡ 标记，然后立即处理（新论文通常量少，不需要三圈螺旋）

## 结构化证据矩阵（跨论文比较）

> 来源：AI4Research 综述 (Lee 2025)。在写综述正文之前先建结构化证据矩阵，避免「证据压缩失真」——模型倾向把不同实验条件的多篇论文概括为统一结论，抹掉重要差异。

### 何时使用

scholar digest 的 Block 4（高引论文）或需要 cross-paper 比较时。不是每篇论文都要填——只对**需要互相比较的关键论文**（通常 Block 4 的 Top 10）建矩阵。

### 格式

每篇关键论文一行，字段对齐：

| 论文 | 研究问题 | 数据来源 | 样本/样品 | 方法 | 基线/对照 | 关键指标 | 主要结果 | 局限 |
|------|----------|----------|-----------|------|-----------|----------|----------|------|
| Cheng 2015 (SIP-SRS) | 活细胞代谢成像 | 固定+活细胞 | HeLa, 3T3 | SIP-SRS 2900/2940 cm⁻¹ | Spontaneous Raman | 化学对比度 | 定位脂质/蛋白比 | 无法区分同构异构体 |
| ... | | | | | | | | |

**关键约束**：
- 「主要结果」必须带定量数字，不能只写"有效"
- 「局限」从论文 Discussion 或 Block 5 Critique 提取
- 多篇论文用同一指标时，标注**指标定义差异**（如"分辨率"的定义不同）

### 与已有内容的关系

矩阵是 Block 4 高引论文表的结构化补充，放在 Block 4 之后或附录中。Block 1-4 的现有内容不做改动。

### 更新头部元数据

更新 digest.md 头部的论文总数和时间跨度：

```markdown
> 论文总数: 572 篇（+3 since 2026-06-16）
> 时间跨度: 1975–2026
> 最后更新: 2026-06-18
```
