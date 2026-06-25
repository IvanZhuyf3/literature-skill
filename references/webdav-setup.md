# WebDAV Attachment Mode

`zotero.sync_method: webdav` 在 `config.yaml` 中启用。避免 Zotero 云存储配额（300MB free tier）。

## 原理

Zotero API 有两种方式附加 PDF：

| 模式 | `sync_method` | 方式 | 配额消耗 |
|------|--------------|------|---------|
| Cloud | `cloud` (default) | `attachment_simple()` multipart 上传 | 走云配额（免费 300MB） |
| WebDAV | `webdav` | JSON API 建 `imported_file` 条目 + 本地拷贝文件 | 不消耗云配额 |

`webdav` 模式通过 Zotero REST API 创建附件条目（linkMode="imported_file"，仅 metadata，不上传文件内容），然后将 PDF 拷贝到 `{storage_path}/{att_key}/{filename}`。Zotero 桌面客户端同步时检测到本地文件，通过 WebDAV 上传到用户的同步服务器.

## 故障回退

`attach_pdf()` 的 cloud 模式遇到 413 (quota exceeded) 会自动降级到 webdav 模式：

```python
# 在 zot.py 中自动处理
try:
    resp = zot.attachment_simple(...)
except Exception as e:
    if "413" in str(e):
        cfg["zotero"]["sync_method"] = "webdav"
        return attach_pdf(item_key, pdf_path, cfg)  # recurse with webdav
```

## 文件位置

PDF 文件在：
```
{storage_path}/{attachment_key}/{original_filename}.pdf
```

例如 `C:\Users\Ivanz\Zotero\storage\ABCDEFGH\paper.pdf`

## Troubleshooting：附件"空壳"问题

### 症状
在另一台电脑上打开 Zotero，附件条目存在但显示"无文件"或只有文件路径文本。本地 `storage/{att_key}/` 目录为空。

### 根因
`attach_pdf()` 成功创建了 attachment API 记录（`linkMode=imported_file`），但 PDF 未拷贝到 `storage/{att_key}/` 目录。Zotero API 的 `filename` 字段存的是原始下载路径的绝对路径（如 `C:\Users\Yifan\Downloads\temp\paper.pdf`），这台机器能通过路径找到文件，但另一台机器上 storage 目录为空，WebDAV 同步只同步了一条空记录。

### 诊断：批量扫描
```python
storage_base = Path('C:/Users/Ivanz/Zotero/storage')
items = zot.collection_items(collection_key, limit=500)
for item in items:
    for child in zot.children(item['key']):
        cd = child.get('data', {})
        if cd.get('linkMode') == 'imported_file' and cd.get('contentType') == 'application/pdf':
            sd = storage_base / child['key']
            has = sd.exists() and any(sd.glob('*.*'))
            if not has:
                print(f'MISSING: {child["key"]} → {Path(cd.get("filename","")).name}')
```

### 修复
1. 在 `Downloads/temp/` 搜索同名 PDF
2. 拷贝到 `storage/{att_key}/`:
```python
shutil.copy2(str(temp_dir / filename), str(storage_base / att_key / filename))
```
3. 下次 Zotero WebDAV 同步将检测到文件并上传到服务器

### 预防
批量下载后（`people.py --download-only`）加一步验证：检查 `storage/{att_key}/` 下文件是否存在。WebDAV 分支自带 `shutil.copy2`，但 cloud→webdav 降级路径可能：
- `attachment_simple` 部分创建附件记录再抛异常，webdav 递归建第二个附件（造重复）
- 早期版本（WebDAV 实现前）的附件缺拷贝步骤（存量问题）

## 注意事项

- Zotero 桌面客户端必须运行并配置了 WebDAV 同步才能将文件推送到远程
- 文件被创建为 `imported_file`（linkMode 0，Zotero 托管文件），这是 WebDAV 同步的正确类型
- `linked_file`（linkMode 2，存绝对路径）不适用于 WebDAV 同步——换电脑路径就断了
- 附件 `filename` 字段可能存全路径（pyzotero 行为），这不影响 WebDAV 同步，只要 `storage/{att_key}/` 下有文件即可
