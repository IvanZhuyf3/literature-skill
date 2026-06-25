# Zotero 批量操作优化

> 场景：需要判断 Zotero collection 中的哪些条目已有 PDF 附件。

## 问题

```python
# ❌ 反模式：逐项查子项（N+1 次 API 调用）
for item in items:
    children = zot.children(item['key'])  # N 次 API 调用！
    has_pdf = any(c.get('data',{}).get('contentType')=='application/pdf' for c in children)
```

- 472 条目 → 472 次 API 调用 → ~60 秒超时
- Zotero API 对逐项查询有速率限制
- 用户等待体验极差

## 解决

```python
# ✅ 单次 API：用 collection_items（带 children）一次拉齐
all_items = zot.collection_items(collection_key)  # 1 次 API 调用

# 本地建 parent → children 字典
parents = {}
attached = set()
for item in all_items:
    d = item.get('data', {})
    if d.get('itemType') in ('attachment', 'note'):
        parent = d.get('parentItem')
        if parent and d.get('contentType') == 'application/pdf':
            attached.add(parent)
    else:
        parents[item['key']] = d

# 比对
for key in parents:
    has_pdf = key in attached  # O(1) 本地查找
```

- 472 条目 → 2-3 次 API 调用（分页）→ <1 秒
- 无速率限制问题
- 逻辑简洁，易于维护

## 适用场景

- `lit batch/attach.py` — 扫描 200+ 条目标识缺 PDF
- `lit digest/template.py` — 读取条目元数据
- 任何需要遍历 Zotero collection 子项的操作

## 原理

`zot.collection_items()` 返回的 API 响应包含所有子条目（notes, attachments），pyzotero 将其展平为列表。无需额外调用 `children()`。
