# Cron 自动化下载

批量下载 cron 的设计规范和格式参考。

## Schedule 格式（重要！）

Hermes cron 的 `schedule` 字段格式：

| 格式 | 含义 | 重复？ |
|------|------|--------|
| `"30m"` | 每 30 分钟 | ✅ 重复 |
| `"every 2h"` | 每 2 小时 | ✅ 重复 |
| `"0 9 * * *"` | 每天 9am（5-field cron） | ✅ 重复 |
| `"2026-06-01T09:00:00"` | 指定时间跑一次 | ❌ 一次性 |

**⚠ 坑：`once in Xm` 是一次性定时器！** 不是重复执行。用 `cronjob` 工具创建时，如果 `schedule` 写 `"once in 5m"`，cron 只会在 5 分钟后触发**一次**就标记 completed，即使设了 `repeat: 500`。

**正确写法**：纯时长字符串如 `"5m"`、`"10m"`、`"30m"` 才是重复执行。

## 批量下载 Cron 模板

### 创建（每 10 分钟一篇）

```
cronjob(action="create"):
  schedule: "10m"           # ← 纯时长，不是 "once in 10m"
  repeat: 500               # 最多跑 500 个 tick
  deliver: "origin"         # 结果发回当前对话
  workdir: "<skill-base>"
  enabled_toolsets: ["terminal", "file"]
```

### Cron prompt 结构

```
Step 1: 并发锁（防止 tick 重叠）
Step 2: 找下一篇缺 PDF 的论文（排除 skip list + engine 黑名单）
Step 3: 判断结果（ALL_DONE → 汇报并暂停 / JSON → 继续下载）
Step 4: lit attach <DOI>（publisher adapter 下载）
Step 5: 记录结果（成功 [SILENT] / 失败加 skip list [SILENT]）
Step 6: Blocker 汇报（仅 ALL_DONE / CDP 挂 / 连续5篇失败）
```

### 关键约束

- **必须用 venv python**：`"C:\Users\Ivanz\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe"`，不要用 `python3`（系统 Python 3.14 与 venv 3.11 依赖不兼容）
- **Publisher 黑名单在 engine.py 层面**（`_PUBLISHER_BLACKLIST`），cron 不需要关心
- **每个 author 一个 skip list**：`people/data/<author>_attach_skip.json`，DOI 为 key
- **正常 tick = [SILENT]**，只有 ALL_DONE / blocker 才汇报
- **不锁定 collection**：用独立 skip list 文件名区分不同 author 的 cron

### 多 author 并行

每个 author 独立 cron + 独立 lock 文件 + 独立 skip list。不需要全局锁——两个 cron 可以同时跑，因为它们操作不同的 collection 和 skip list。

如果担心 CDP 竞态（同一台 Edge 同时下两篇），可以在 Step 1 检查其他 lock 文件：
```bash
for lock in people/data/*_attach.lock; do
    if [ -f "$lock" ]; then echo "其他 cron 在跑，跳过"; exit 0; fi
done
```
