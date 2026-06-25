# Storage File Gap — Zotero attachment 缺文件排查

> 2026-06-16 调试 6 小时发现的隐患，2026-06-17 更新修复方案为 `lit maintain` + `lit attach`。

## 现象

Zotero 条目显示有 PDF 附件（`linkMode=imported_file`），但另一台电脑同步后"只同步了个地址"——双击提示文件不存在。检查 `Zotero/storage/{att_key}/` 目录为空，但 `Downloads/temp/` 下有 PDF。

## 根因

`attach_pdf()` 在 Zotero API 成功创建了 attachment 记录，但 **拷贝 PDF 到本地 storage 目录这一步被跳过**。具体诱因：

| 诱因 | 机制 |
|------|------|
| **Cloud 413 降级** | 旧版代码（2026-06-16 WebDAV 重写前）Cloud API 413 后 fallback 未完整执行，attachment 记录已部分创建但文件未拷 |
| **`storage_path` 未配置** | `attach_pdf()` 检查 `zcfg.get("storage_path","")`，为空则跳过 `shutil.copy2()` |
| **跨电脑同步** | 附件记录中的 `filename` 字段存了完整 temp 路径（如 `C:\Users\Yifan\Downloads\temp\xxx.pdf`），到另一台电脑上该路径不存在 |

## 诊断步骤

```python
from pyzotero import zotero
z = zotero.Zotero(lib_id, 'user', api_key)
children = z.children(parent_key)
for c in children:
    cd = c['data']
    if cd.get('contentType') == 'application/pdf':
        att_key = c['key']
        print(f"Att: {att_key}, linkMode={cd.get('linkMode')}")
        print(f"  filename={cd.get('filename','')}")
        # 检查 storage 目录
        import os
        storage_dir = f"C:/Users/Ivanz/Zotero/storage/{att_key}"
        has_files = os.path.exists(storage_dir) and any(
            f.endswith('.pdf') for f in os.listdir(storage_dir)
        ) if os.path.exists(storage_dir) else False
        print(f"  storage/{att_key}/ has PDF: {has_files}")
```

## 修复

```bash
# 方法 1: lit maintain 自动诊断 + 修复
python -m lit maintain --collection "学者名"   # 体检：报告 ghost/empty/mismatch
python -m lit maintain --fix                    # 修复：删孤儿目录 + ghost 条目

# 方法 2: lit attach 批量补缺
python -m lit attach "学者名"                   # 遍历 collection，下载缺的 PDF
```

`lit maintain` 检查三类问题：ghost（Zotero有条目无文件）、empty（目录无PDF）、
filename mismatch。`--fix` 模式删孤儿目录（送回收站）+ 删 Zotero ghost 条目。
`lit attach` 负责下载缺失的 PDF 并 attach 到 Zotero。

## 预防

1. 确保 `config.yaml` 的 `zotero.storage_path` 指向正确的 Zotero storage 目录
2. 首次 `lit scholar` + 用户清洗后，跑一遍 `lit attach "学者名"` 确保所有条目有 storage 文件
3. 定期跑 `lit maintain --collection "学者名"` 体检，发现 ghost/empty 及时修
4. 不要在 `config.yaml` 里混用不同电脑的路径
