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
