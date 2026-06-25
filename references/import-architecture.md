# import 架构说明（2026-06 重构）

## 背景

`cite.py` 被拆分为三文件，职责彻底解耦。不再存在一个文件既管引用又管下载的情况。

## 文件映射

| 旧文件 | 新文件 | 职责 |
|--------|--------|------|
| `lit/discover/cite.py` | → `lit/discover/import_ref.py` | 只做条目注册 |
| `lit/discover/cite.py` | → `lit/download/quick_download.py` | 编排快速下载 |
| `lit/download/scihub.py` (cloudscraper) | → `lit/download/scihub_cdp.py` | CDP 版 Sci-Hub |
| `lit/batch/attach.py` | 保留 | 批量补缺（独立路径） |

## CLI 编排（`lit/cli.py`）

```python
# lit import <DOI>
result = import_ref.run(source)           # 只加 ref
if result["doi"] and result["item_key"]:
    pdf_path = quick_download.run(doi, year)  # 尝试免费源
    if pdf_path:
        attach_pdf(item_key, pdf_path)    # WebDAV 挂载
```

## 添加新快速下载源

在 `lit/download/quick_download.py` 的 `_METHODS` 表加一行：

```python
_METHODS = [
    ("Sci-Hub (CDP)", try_scihub),
    # 加在这里:
    ("Unpaywall", try_unpaywall),
]
```

新方法文件放 `lit/download/` 下，函数签名统一：
```
fn(doi: str, year: str | int | None = None) -> Path | None
```

## parse — bibliography frontmatter

`lit parse <pdf> --doi <DOI>` 会自动在 .md 文件头加 YAML frontmatter。

parser.run() 接受可选 metadata dict，纯函数设计，不关心数据从哪来。CLI 层负责：`fetch_metadata(doi)` → `parser.run(pdf, metadata=meta)`。

## 已知 pitfall

### `_attach_webdav` 必须包含 md5/mtime/filename

Zotero API 在 `imported_file` link mode 下需要这三个字段才能正确定位 storage 文件。

### Zotero API 响应解析用 `next(iter(...))` 而非 `[0]`

pyzotero 在 HTTP 204 响应时返回的 "successful" 字段是 dict 而非 list：
```python
# ❌ 会 KeyError: 0
att_key = result["successful"][0]["data"]["key"]

# ✅ 正确
first_success = next(iter(result["successful"]))
att_key = result["successful"][first_success]["data"]["key"]
```
