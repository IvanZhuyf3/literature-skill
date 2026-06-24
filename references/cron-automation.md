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

**正确写法**：纯时长字符串如 `"5m"`、`"10m"`、`"30m"` 或 `"every 5m"` 才是重复执行。

## 批量下载 Cron — 完整模板

### 核心设计原则（踩过的坑）

1. **while 语义，不是 for 次数**：`repeat: 200` 只是保险上限。实际终止靠 ALL_DONE 时 agent 自我暂停（`cronjob pause`）。**不能靠固定次数自然耗尽**——空转 tick 每个都会发通知，刷屏。
2. **正常 tick 必须 [SILENT]**：成功、失败、加 skip list 都**不输出任何内容**。只有 ALL_DONE 或 blocker（CDP 挂、连续 5 篇失败）才输出。输出 = 发通知给用户。
3. **DOI 在 `data["DOI"]` 字段**（大写键名），不在 `extra` 字段。
4. **enabled_toolsets 必须含 `cronjob`**：agent 需要调 `cronjob pause` 暂停自己。

### 创建参数

```python
cronjob(action="create"):
  name: "<author>-attach"           # 如 "delong-attach"
  schedule: "every 5m"              # 纯时长或 every Xm，不是 "once in Xm"
  repeat: 200                       # 保险上限，不靠它终止
  deliver: "origin"                 # 结果发回当前对话
  workdir: "<skill-base>"
  enabled_toolsets: ["terminal", "file", "cronjob"]  # ← cronjob 用于自我暂停
```

### 完整 Prompt 模板

> 以下 prompt 中 `«PARAM»` 标记的部分按实际 author 替换。

```
你是 «AUTHOR» 论文批量下载 cron（adapter 兜底通道）。每 tick 处理一篇论文。

## 绝对规则

1. [SILENT] 纪律：成功、失败、加 skip list 都不输出任何内容。只有以下三种情况才输出：
   - ALL_DONE：最终汇总
   - CDP/Edge 连续 3 篇导航错误：汇报并暂停
   - 连续 5 篇失败：汇报进度
2. ALL_DONE 时必须自我暂停：调 cronjob(action="list") 找到自己的 job_id（name="«AUTHOR»-attach"），再调 cronjob(action="pause", job_id="...")。

## 常量

VENV_PYTHON = "C:\Users\Ivanz\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe"
SKIP_FILE = "people/data/«AUTHOR_UNDERSCORE»_attach_skip.json"
LOCK_FILE = "people/data/«AUTHOR_UNDERSCORE»_attach.lock"
COLLECTION = "«COLLECTION_NAME»"

## Step 1: 并发锁
检查 LOCK_FILE 是否存在且创建时间 <10 分钟。如果是，说明上一个 tick 还在跑，不输出直接退出。否则创建 LOCK_FILE。

## Step 2: 找下一篇缺 PDF 的论文
DOI 在 Zotero 的 data["DOI"] 字段（大写键名）。

cd "C:\Users\Ivanz\AppData\Local\hermes\skills\research\literature-skill"
PYTHONIOENCODING=utf-8 "$VENV_PYTHON" -c "
import json, os, pathlib
from lit.core.zotero import collection_items_top, find_collection, get_children, get_storage_path
coll = find_collection('«COLLECTION_NAME»')
items = collection_items_top(coll)
sp = get_storage_path()
skip = set()
if os.path.exists('«SKIP_FILE»'):
    skip = set(json.load(open('«SKIP_FILE»')).keys())
for item in items:
    d = item['data']
    doi = d.get('DOI', '').strip()
    if not doi or doi in skip:
        continue
    children = get_children(d['key'])
    has_real = False
    for ch in children:
        cd = ch['data']
        if cd.get('itemType') == 'attachment' and cd.get('contentType') == 'application/pdf':
            fdir = pathlib.Path(sp) / ch['key']
            if fdir.exists() and any(fdir.iterdir()):
                has_real = True
                break
    if has_real:
        continue
    print(json.dumps({'doi': doi, 'key': d['key'], 'title': d['title'][:80]}))
    break
else:
    print('ALL_DONE')
"

## Step 3: 判断结果
- 输出 ALL_DONE → 删 LOCK_FILE，调 cronjob pause 暂停自己，输出最终汇总（总篇数、有PDF数、skip数），结束。
- 输出 JSON → 继续 Step 4
- 无输出/报错 → 删 LOCK_FILE，不输出，退出

## Step 4: 下载
PYTHONIOENCODING=utf-8 "$VENV_PYTHON" -m lit attach <DOI>

⚠️ 关键约束：
- lit attach 报 "Unknown publisher" → 不跳过。web_search 查出版商域名，检查 url_parser.py PUBLISHER_PATTERNS。不覆盖则读 references/maintain.md 流程 B 建 adapter。
- 不用 web_search 找替代下载源，只走 lit attach。
- supplementary material DOI（.s001/.s002 后缀）或会议 abstract → 加 skip list。

## Step 5: 记录结果
- 成功 → 删 LOCK_FILE，不输出
- 失败 → DOI 加 skip list（格式 {"doi": {"reason": "...", "date": "YYYY-MM-DD"}}），删 LOCK_FILE，不输出
```

### 参数替换表

| 占位符 | 含义 | 示例 |
|--------|------|------|
| `«AUTHOR»` | cron name 用的短名 | `delong` |
| `«AUTHOR_UNDERSCORE»` | skip/lock 文件名用的下划线名 | `Delong_Zhang` |
| `«COLLECTION_NAME»` | Zotero collection 名（find_collection 参数） | `Delong Zhang` |

### 关键约束

- **必须用 venv python**：`"C:\Users\Ivanz\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe"`，不要用 `python3`（系统 Python 3.14 与 venv 3.11 依赖不兼容）
- **Publisher 黑名单在 engine.py 层面**（`_PUBLISHER_BLACKLIST`），cron 不需要关心
- **每个 author 一个 skip list**：`people/data/<author>_attach_skip.json`，DOI 为 key
- **不锁定 collection**：用独立 skip list 文件名区分不同 author 的 cron

### 多 author 并行

每个 author 独立 cron + 独立 lock 文件 + 独立 skip list。不需要全局锁——两个 cron 可以同时跑，因为它们操作不同的 collection 和 skip list。

如果担心 CDP 竞态（同一台 Edge 同时下两篇），可以在 Step 1 检查其他 lock 文件：
```bash
for lock in people/data/*_attach.lock; do
    if [ -f "$lock" ]; then echo "其他 cron 在跑，跳过"; exit 0; fi
done
```

## 论文侦测 Cron（不变）

每日定时检测学者新论文，有新论文时通知用户。与下载 cron 不同——这个只检测不下载。

### 推荐方案：no_agent script-only（0 token）

用 `no_agent=True` + `script` 方式跑一个 Python 脚本，串行遍历所有作者。不消耗 token，不需要 agent 推理。

```python
cronjob(action="create"):
  schedule: "0 9 * * *"           # ← 5-field cron，每天 9am
  repeat: forever
  deliver: "origin"               # 通知发回当前对话
  no_agent: True                  # ← 纯脚本，0 token
  script: "track_all.py"  # ← ~/.hermes/scripts/ 下的纯文件名
  workdir: "<skill-base>"
```

### Script 路径规则（⚠ 必读）

Hermes cron 的 `script` 字段**只接受 `~/.hermes/scripts/` 下的纯文件名**。如果实际脚本在 workdir 子目录里，必须在 `~/.hermes/scripts/` 放一个薄 wrapper（绝对路径调真实脚本）。

系统 `python3` 是 3.14，lit 依赖装在 venv 3.11（C 扩展不兼容）。必须用 venv python。

### track_all.py 结构

```python
# 串行遍历所有 authors
AUTHORS = ["Ji-Xin_Cheng", "Wei_Min", "Herve_Rigneault"]
results = {}
for author in AUTHORS:
    try:
        new = tr.find_new_papers(author)
        if new:
            results[author] = new
    except Exception:
        pass  # errors are silent, retry next tick
# 有新论文 → print 摘要（stdout delivered verbatim）
# 无新论文 → sys.exit(0)（空 stdout = SILENT）
```
