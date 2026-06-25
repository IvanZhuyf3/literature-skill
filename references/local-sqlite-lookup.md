# Local SQLite DOI Lookup

> 2026-06-18 发现 Zotero Web API 的 `q=` 全文搜索**不索引 DOI 字段**。修复方案：复制本地 zotero.sqlite 到临时文件，用 SQL 精确匹配 DOI。

## 根因

Zotero Web API 的 `q` 参数走 SQLite FTS（全文搜索），只索引标题、作者、摘要、全文内容。**DOI 作为字段值不在 FTS 范围内。**

测试验证：
```python
zot.items(q="10.1117/12.3042444")              # 0 条结果
zot.items(q="Fingerprinting organelles")        # 1 条（标题搜索） ✓
requests.get(items_url, params={"DOI": doi})    # DOIs 参数被忽略 — 传假 DOI 也返回结果
```

## 方案：SQLite 副本 + mtime 缓存

### 代码位置
`lit/core/zotero.py` — `_local_db()` 和 `resolve_local_pdf()`

### 流程
1. `_local_db()` 复制 `zotero.sqlite` 到 `%TEMP%/lit_zotero_query.sqlite`
2. 比较源文件 mtime vs 副本 mtime（`shutil.copy2` 保留 mtime）
   - 相同 → 跳过复制，直连副本
   - 不同 → 重新复制
3. 固定路径，不产生孤儿文件

### 查询
```sql
-- DOI → parent item key
SELECT i.key
FROM items i
JOIN itemData id ON i.itemID = id.itemID
JOIN fields f ON id.fieldID = f.fieldID
JOIN itemDataValues idv ON id.valueID = idv.valueID
WHERE f.fieldName = 'DOI' AND LOWER(idv.value) = ?

-- DOI → attachment key（一条查询）
SELECT att.key AS att_key
FROM items parent
JOIN itemData id ON parent.itemID = id.itemID
JOIN fields f ON id.fieldID = f.fieldID
JOIN itemDataValues idv ON id.valueID = idv.valueID
JOIN itemAttachments ia ON ia.parentItemID = parent.itemID
JOIN items att ON att.itemID = ia.itemID
WHERE f.fieldName = 'DOI' AND LOWER(idv.value) = ?
AND ia.contentType = 'application/pdf'
```

### Zotero Schema（核心表）

| 表 | 说明 |
|---|---|
| `items` | itemID, key, itemTypeID |
| `itemData` | itemID → fieldID → valueID |
| `itemDataValues` | valueID → value |
| `fields` | fieldID → fieldName (如 'DOI', 'title', 'date') |
| `itemAttachments` | itemID, parentItemID, contentType, path |
| `collectionItems` | collectionID → itemID |
| `collections` | collectionID, collectionName |

### 性能
- 冷启动（复制 200MB）：0.13s
- 热查询（跳过复制）：0.02s
- 批量场景共用同一副本

### 注意
- 只读副本，不写 Zotero。zotero.sqlite 本身不会被修改
- 磁盘验证：必须 `os.path.isdir(storage/{att_key})` + 找 `.pdf` 文件，防止 ghost attachment
- WAL 模式未 checkpoint 的事务可能不达副本，但影响极小（新条目延迟几秒可见）
- **云 API 创建后的 sync lag**：`import_run()` 通过 Zotero 云 API 创建条目，但 `find_by_doi()` 检查本地 SQLite 副本。刚创建的条目还没同步到本地 DB，`find_by_doi` 会返回 None。**解决方案**：`quick_single()` 和 `attach_single()` 接受可选 `item_key` 参数，import 后直接传递，跳过 `find_by_doi` 查找。详见 `references/tracking-architecture.md` 的 "import → download 的 item_key 传递" 章节。
