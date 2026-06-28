# S2 + CrossRef + OpenAlex Tracking

用于 `lit track <author>` 的增量论文检测系统。

## 三源架构

| 源 | 角色 | 用途 |
|----|------|------|
| **Semantic Scholar** | 论文发现（主源） | author profile-scoped DOI 拉取 |
| **CrossRef** | 论文发现（补源） | 近 30 天 name-based 搜索，补 S2 时效盲区 |
| **OpenAlex** | 身份验证（affiliation） | DOI 反查标准化 institution 数据 |

```
论文发现：
  S2 (author profile) ──→ DOI set ──┐
                                     ├──→ union ──→ diff Zotero ──→ 新论文
  CrossRef (name search) ──→ DOI ──┘

身份验证（对新论文逐篇）：
  OpenAlex /works/doi:xxx
    ──→ authorships[matching author].institutions[]
    ──→ vs known_affiliations / affiliation_history
    ──→ confidence: high | low
```

## 双源设计

| 维度 | Semantic Scholar | CrossRef |
|------|-----------------|----------|
| 查询方式 | `graph/v1/author/{id}/papers` | `works?query.author=xxx&filter=from-created-date:yyyy-mm-dd` |
| 覆盖 | 全量（444 篇论文） | 近 30 天（按 created date 过滤） |
| 假阳性 | 0（author ID 精确） | 有（name collision），需 author list 过滤 |
| 增量 | 首次全量，后续仅新论文 | 天然增量（by date） |
| 速度 | ~5-8s（分页 444 篇） | ~1-2s（单页 50 条，relevance 排序） |
| 速率限制 | 100 req/5min（无 key），1 req/s（有 key） | 宽松，无显式限制 |

### S2 API Key（config.yaml）

```yaml
semantic_scholar:
  api_key: ""                 # semanticscholar.org/product/api#api-key 申请，留空走公共额度
```

3 个作者增量追踪每天 ~20 次请求，公共额度（100 req/5min）完全够用。首次全量拉取（如 480 篇）或 10+ 作者时建议配 key（独享 1 req/s = ~5000/day）。Key 从 https://www.semanticscholar.org/product/api#api-key 免费申请。

## Name Matching（CrossRef 假阳性过滤）

**2026-06-21 更新：已从初字母匹配改为全名归一化匹配。**

```python
def _normalize_name(s: str) -> str:
    """lowercase, strip accents/hyphens/punctuation → pure alnum."""
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return "".join(c for c in s if c.isalnum())

# 匹配条件：family AND given 都必须归一化后全等
matched = (_normalize_name(family) == alias_family and
           _normalize_name(given) == alias_given)
```

`_normalize_name("Ji-Xin") → "jixin"` ≠ `"jianxiang"` → 拒绝。
`_normalize_name("Hervé") → "herve"` == `"herve"` → 匹配（accent 归一化）。
缩写 alias（`"JX Cheng"→"jxcheng"`）仍然能匹配 CrossRef 里恰好缩写成同样形式的作者。

### 历史教训：初字母匹配为何被废弃

旧方案用 `any(ai in given_initials for ai in alias_initials)`，对 "Ji-Xin Cheng"（initials J,X）来说，**任何姓 Cheng、名字以 J 或 X 开头的人都会通过**。2026-06-21 实测一个 tick 检出 4 篇 "Cheng 新论文"，其中 3 篇是假阳性：

| DOI | 实际作者 | 为什么通过旧过滤 |
|-----|---------|---------------|
| `10.1007/s00028-026-01205-x` | **Cheng Bi**（数学） | 中文姓名顺序：CrossRef 解析成 given="Cheng" family="Bi" |
| `10.1016/j.neucom.2026.134116` | **Jianxiang Cheng**（脑网络） | family=Cheng ✓，given initial=J ∈ {J,X} ✓ |
| `10.31237/osf.io/n5mzy_v2` | **Jinjun Cheng**（化学势能） | family=Cheng ✓，given initial=J ∈ {J,X} ✓ |

全名匹配后这三个全被拒绝，同时**多捞到 2 篇真论文**（Cheng 在作者列表第 7、8 位，旧方案的 `break` 在前面的 FP 作者处就退出了）。

## Author Profile 格式

`people/<author_dir>/profile.json`:

```json
{
  "name": "Ji-Xin Cheng",
  "aliases": ["Ji-Xin Cheng", "JX Cheng"],
  "affiliation": "Boston University",
  "s2_author_id": "144507368",
  "s2_ids": ["144507368", "2244002386"],
  "scholar_url": "https://scholar.google.com/citations?user=M7fTV28AAAAJ",
  "zotero_collection": "Ji-Xin Cheng",
  "crossref_last_check": "2026-06-19",
  "s2_last_check": "2026-06-19",
  "created": "2026-06-18",
  "s2_paper_counts": {
    "144507368": 444,
    "2244002386": null
  }
}
```

### 字段说明

| 字段 | 说明 |
|------|------|
| `s2_author_id` | 主 S2 ID（backward-compat，单 ID 场景用） |
| `s2_ids` | **多 S2 ID 列表**（S2 有重复 profile 时用）。存在时 tracker 遍历所有 ID 取并集 |
| `s2_paper_counts` | per-ID 增量 offset 字典。`null` = 未初始化（首次全量扫） |
| `s2_paper_count` | backward-compat 聚合值（= max of s2_paper_counts.values()） |
| `birth_year` *(已否决)* | ~~出生年。year < birth_year 的论文直接排除假阳性。~~ 用户否决：老爷爷文章只在加新人时出现一次，人工排除后不会再出现，不值得加字段 |
| `known_affiliations` | 历史单位列表（如 `["Boston University", "Purdue"]`），用于 OpenAlex affiliation 身份验证。`_check_affiliation()` 查 OpenAlex `authorships[].institutions[].display_name` 匹配（CrossRef fallback）。**空列表时默认 LOW**（2026-06-25 修复：原来默认 high 导致 Delong Zhang 的同名假阳性静默入库） |
| `affiliation_history` | 年度单位字典 `{"2015": ["Purdue University"], "2017": ["Boston University"]}`。`lit build-affiliations --save` 自动生成。用于 year-aware 匹配（查论文年份 ±1 年的单位）。解决搬家问题 |

### 多 S2 ID（重复 profile）

S2 有时会为同一人创建多个 profile（最常见的：name 里的 dash 编码不同，如 `Ji-Xin` vs `Ji‑Xin`）。
这导致论文分散在两个 profile 里。`s2_ids` 列表让 tracker 遍历所有 ID 并取 DOI 并集。
添加第二个 ID 时，把它的 `s2_paper_counts` 值设为 `null`，首次运行自动全量扫建立 baseline。

## S2 Author ID 发现（DOI 反查法）

**S2 `author/search` 对常见姓名不可靠**（如 Dan Fu、Delong Zhang 返回大量同名条目，无法区分）。但只要该作者已在 Zotero 有论文（哪怕只有几篇 DOI），就可以用 **DOI 批量反查** 精确发现所有 S2 profile。

### 原理

```
Zotero collection 的所有 DOI
    → S2 batch API POST /paper/batch (500/批，<1s)
    → 每篇论文的 authors[].authorId
    → 汇总频次 + 姓名/首字母筛选
    → 目标人物的全部 S2 ID（包括重复 profile）
```

### 为什么不用频次？

频次看似好指标但**有致命缺陷**：长期合作者频次同样很高。Cheng 424 篇 DOI 实测：

| 频次排名 | authorId | 姓名 | 频次 | 身份 |
|---------|----------|------|------|------|
| 1 | 144507368 | Ji‐Xin Cheng | 292 | ✓ 本人（主 profile） |
| 2 | 5718747 | M. Slipchenko | 34 | ✗ 合作者 |
| 3 | 2108269067 | Pu Wang | 32 | ✗ 合作者 |
| 4 | 2158371947 | Ji-Xin Cheng | 30 | ✓ 本人（重复 profile） |
| 5 | 30948969 | Haonan Lin | 30 | ✗ 合作者 |
| 6 | 1492113551 | Junjie Li | 28 | ✗ 合作者 |
| 7 | 145637490 | Delong Zhang | 27 | ✗ 合作者 |

Top 15 里一半是合作者。**必须加姓名筛选**。

### 匹配策略（用户纠正后的正确逻辑）

1. **姓精确匹配**：surname 归一化后全等（`Cheng` == `cheng`）
2. **名首字母匹配**：given name 第一个首字母匹配（`J`），**不是全名首字母**（如 `JXC`）
   - 原因：连字符不总是出现。S2 里同时有 `Ji-Xin Cheng`（initials J,X,C）、`Jixin Cheng`（J,C）、`J. Cheng`（J,C）
   - 用 `JXC` 筛会漏掉 `J. Cheng`（只有首字母 J）
   - 用 `J` 筛能全部捞到，零误匹配（Cheng 的数据集里没有其他 J-Cheng）
3. **Unicode 归一化（必须！）**：S2 用多种 Unicode 连字符变体：
   - `Ji‐Xin Cheng`（U+2010 ‐ HYPHEN，主 profile 292 篇全是这个！）
   - `Ji-Xin Cheng`（U+002D - ASCII HYPHEN-MINUS）
   - `Ji–Xin Cheng`（U+2013 – EN DASH）
   - **不归一化直接 split → 连字符解析错误 → 漏掉主 profile**
   - Fix：`re.sub(r'[\u2010-\u2015\u2212]', '-', s)` 统一成 ASCII `-`

### 验证分层

| 候选类型 | 示例 | 处理 |
|---------|------|------|
| 全名变体（含 ji/xin 子串） | `Ji-Xin Cheng`, `Jixin Cheng`, `Ji Xin Cheng` | 自动确认 |
| 缩写变体（只有首字母） | `J. Cheng`, `JX Cheng` | 低频（1-2篇）可忽略或人工确认 |

### 实测效果

Cheng（424 DOI）：
- **1 个 batch POST**（<1s），399/424 论文在 S2 找到
- 筛选 `surname=Cheng + given首字母=J` → **17 个 S2 profile**，零误匹配
- profile.json 原来只记了 3 个 → 发现 14 个新的（其中 5 个有 ≥4 篇论文）
- API 消耗：**1 request**（batch API 最多 500 ID/请求）

### 代码片段

```python
import requests, json, re, unicodedata
from collections import Counter

# 1. Batch query: up to 500 DOIs per POST
resp = requests.post(
    "https://api.semanticscholar.org/graph/v1/paper/batch",
    params={"fields": "authors"},
    headers={"x-api-key": S2_KEY, "Content-Type": "application/json"},
    json={"ids": [f"DOI:{d}" for d in dois]},
    timeout=60,
)

# 2. Count author appearances
author_counter = Counter()
for paper in resp.json():
    if not paper: continue
    for a in paper.get("authors", []):
        if a.get("authorId"):
            author_counter[(a["authorId"], a["name"])] += 1

# 3. Normalize + filter
def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[\u2010-\u2015\u2212]", "-", s)
    return s.strip()

surname = "cheng"
given_initial = "J"  # first letter of given name only
for (aid, aname), count in author_counter.most_common():
    parts = norm(aname).lower().split()
    if len(parts) < 2 or parts[-1] != surname:
        continue
    given = re.split(r"[- .]", " ".join(parts[:-1]))
    initials = [w[0] for w in given if w]
    if initials and initials[0] == given_initial.lower():
        print(f"  {count:4d}  {aid:>12s}  {aname}")
```

## S2 Full Audit（发现缺失论文）

发现全部 S2 profile ID 后，顺带做一次全量审计：拉每个 profile 的所有论文 DOI → diff Zotero → 过滤出真正缺失的期刊论文。

```bash
lit discover-s2 <Author> --save       # 发现 ID + 审计（只看，不下载）
lit discover-s2 <Author> --download   # 发现 ID + 审计 + 注册下载缺失论文
```

`--download` implies `--save`。下载走标准 import → quick → attach 链。

### 为什么需要审计？

Scholar 抓取天然有盲区（标题匹配率 ~17-81%）。S2 全量扫可以把 Scholar 漏掉的论文全部捞出。Cheng 实测：424 篇在 Zotero，S2 20 个 profile 合计 607 篇 unique DOI → **213 篇缺口**。

### S2 数据质量问题（关键！）

S2 数据极脏，213 raw 缺口经过三层过滤才降到 40 篇有效论文：

| 过滤层 | 策略 | 砍掉数量 |
|--------|------|---------|
| **DOI denylist（最高优先级）** | SPIE `10.1117/12.*`、OSA 会议 `10.1364/(cleo|fio|...)`、IEEE 会议 `10.1109/cleo.*`、FASEB摘要 `10.1096/fasebj.*`、AACR摘要 `10.1158/1538-7445.*`、bioRxiv预印本 `10.1101/*`、书章 `10.(1007/978|1016/b978|1201/b|1142/978)` 等 | ~150 |
| **垃圾标题过滤** | title 含 `advertising`/`front matter`/`subject index`/`editorial board`/`inside cover`/`innentitelbild` → 排除 | ~15 |
| **低置信 profile 独有论文** | 只出现在 `confirmed=False` 的 profile（如 `J. Cheng`，11 篇里只有 1 篇是本人的）上的论文 → 排除。这些是同名不同人的论文 | ~7 |

**核心教训：DOI denylist 必须优先于 S2 publicationTypes**。S2 把 ~20% 的会议论文错误标为 `JournalArticle`，如果先看 S2 type 再看 denylist，这 20% 会漏过去。

### 低置信 profile 判定

`discover_s2_ids()` 返回 `confirmed` 标志：
- **confirmed=True**：名字里含第二首字母线索（如 `Ji-Xin` 的 `X`，在 `Ji-Xin Cheng`/`Jixin Cheng` 中匹配到 `xin`/`xi` 开头的词）
- **confirmed=False（⚠️）**：纯缩写如 `J. Cheng`、`Jixin Cheng`（只有一个 given word，无法验证第二首字母）

⚠️ profile 不一定全是假——Cheng 的 `2107265746 J. Cheng` 有 1 篇确实是他的（breast cancer co-culture paper，合作者 Thuc T. Le）。但其余 10 篇是另一个做毛细管电泳的 J. Cheng。所以**独有论文排除，共现论文保留**。

### ⚠️ 极端常见姓名：Zotero 重合率验证（Ping Wang 案例）

对于 "Ping Wang" 这类极度常见的名字，surname + given initial 匹配会返回大量候选 profile，**全部同名同首字母**，name-based 判定完全失效。唯一可靠的区分方法是 **Zotero 重合率验证**：

1. 拉每个候选 S2 profile 的全部论文 DOI
2. 计算与作者 Zotero collection 的交集比例：`overlap = s2_profile_dois ∩ zotero_dois / len(s2_profile_dois)`
3. **>50% → 真 profile**；**<10% → 假阳性**

**Ping Wang 实测**（2026-06-25）：

| S2 ID | 名字 | S2 论文数 | Zotero 重合 | 重合率 | 判定 |
|-------|------|----------|-----------|--------|------|
| 2152209297 | Ping Wang | 18 | 16/18 | **89%** | ✓ 主 profile |
| 2152207049 | Ping Wang | 27 | 13/27 | **48%** | ✓ 第二 profile（有重复论文） |
| 2108269067 | Pu Wang | 48 | 4/48 | 8% | ❌ Cheng 组合作者 |
| 2152209329 | Ping Wang | 57 | 1/57 | 2% | ❌ 同名不同人 |
| 2152209499 | Ping Wang | 5 | 1/5 | 20% | ❌ 噪音 |

OpenAlex 搜 "Ping Wang" 返回 **2610 个 author profile**——这种名字 surname+initial 毫无区分力，只有定量重合率才管用。

**何时用**：当 `lit discover-s2` 返回 ≥3 个 same-name 候选 profile 时，agent 应主动跑重合率验证（debug 脚本示例：`debug/check_wangping_s2.py`），而不是把所有候选都存进 profile.json。

### 审计后的人工检查

审计输出的期刊论文列表仍需人工过一遍。Cheng 40 篇里发现：
- Publisher's Note（勘误页，不是论文）
- 1984 年 Pediatric Research "Subject Index"（目录页，junk filter 没抓到因为 title 不含标准关键词）
- 中文期刊同名作者（`10.3969/j.issn...` 锌化合物，来自 `J.-x. Cheng` profile）
- 90 年代论文看似可疑但可能是早期工作（需要合作者交叉验证）
- **1973 年液晶论文**：Cheng 1971 年生，不可能在 2 岁发论文 → 假阳性。S2 主 profile 混入了大量非本人旧论文（液晶、毛细管电泳、UHMWPE）。**年份 < 作者出生年 → 直接排除**。

## 目录结构

```
people/
  Ji-Xin_Cheng/
    profile.json        ← 追踪配置（S2 ID, aliases, 时间戳）
    papers/             ← 解析后的 .md 文件
      10.1038_s41467-021-23202-z.md
    digest.md           ← 消化报告
```

## 添加新追踪作者（步骤）

1. **查 S2 author ID**：优先用 DOI 反查法（见上方「S2 Author ID 发现」章节）：直接运行 `lit discover-s2 <Author_Name> --save`，1 个 API 请求自动发现全部 S2 profile + 写入 profile.json。对常见姓名（Dan Fu, Delong Zhang）唯一可靠方法。
   - 备选：`curl -s "https://api.semanticscholar.org/graph/v1/author/search?query=First+Last&fields=name,paperCount"` → 选 paperCount 最高的 ID（适合独特姓名）。
2. **注册论文到 Zotero**：`lit scholar "https://scholar.google.com/citations?user=XXXX&hl=en"`。**Scholar URL 必须用 `hl=en`**——非英文页（如法语 `hl=fr`）会影响页面解析。**CrossRef 标题匹配率低时（<30%，常见于法语/早期欧洲期刊学者）**，用 S2 DOI 直注方案补注册（详见 `references/people-guide.md` 的「S2 DOI 直注」+「S2 批量注册」小节）。`lit scholar` 自动创建 `people/<dir>/profile.json`（via `_ensure_profile()`），目录名由 `_dir_name_from_scholar()` 自动生成（空格→下划线，去重音符：`Hervé Rigneault` → `Herve_Rigneault`）。
3. **补 `profile.json` 的 S2 字段**：填入 `s2_ids`、`aliases`（含缩写形式）。`s2_paper_counts` 值设为 `null`（首次运行 baseline-only）。
4. **跑一次 `lit track <Author_Name>`** 建立 baseline：S2 记录 paperCount，CrossRef 检测近期论文。验证 `s2_paper_counts[id]` 从 null 变为实际数字。
5. **构建 affiliation 数据库**：`lit build-affiliations <Author_Name> --save`。**必须做**——否则 `known_affiliations` 为空 → 所有新论文默认 LOW → 每天发审阅请求。数据源为 OpenAlex（覆盖率 ~90%，batch 查询秒级）。
6. **⚠️ 手动补充 + 汇报 double check**：将 build-affiliations 结果（年度轨迹表）汇报给用户确认。同时**主动向用户索要个人简介页**（Google Scholar 旁边的 lab page / university faculty page / HAL CV 等）。
   - **为什么需要**：即使 OpenAlex 覆盖率 ~90%，仍有 ~10% 空白（某些出版商不填）。Phinceton PhD、MIT postdoc 这类早期经历可能查不全（如 Dan Fu 的 Princeton 期间论文 OpenAlex 也未覆盖）。
   - **用户偏好**：用户说"以后我尽量在给你 Google Scholar 时同时给你一个个人简介页"——**收到 Scholar URL 时主动问有没有 bio page**。
   - 用 bio 页面信息**手动补写** `affiliation_history` 里 OpenAlex 覆盖不到的年份，然后 commit。
   - 用户的轨迹知识是 ground truth，OpenAlex/CrossRef 只是辅助验证。当两者冲突时，以用户的 bio 为准。

无需碰 cron 配置——`track_all.py` 动态扫描 `people/*/profile.json`，建好目录即自动纳入每日追踪。

## CLI 用法

```bash
lit track Ji-Xin_Cheng               # 检测新论文（不下载）
lit track Ji-Xin_Cheng --download    # 检测 + 注册 + 下载
lit build-affiliations Ji-Xin_Cheng  # 从 Zotero 论文自动构建年度 affiliation 数据库
lit build-affiliations Ji-Xin_Cheng --sample 5 --save  # 每年采样5篇 + 写入 profile.json
```

## Affiliation 数据库构建（lit build-affiliations）

新增追踪人物后，**必须**运行一次 `build-affiliations` 建立单位历史库。否则 `known_affiliations` 为空 → 所有新论文默认 LOW → 每天都给你发审阅请求。

### 数据源：OpenAlex（2026-06-25 起，替代 CrossRef）

**为什么从 CrossRef 切换到 OpenAlex**：

| 维度 | CrossRef（旧） | OpenAlex（新） |
|------|-------------|--------------|
| 覆盖率 | ~40%（ACS 好 / SPIE+Wiley+IEEE 空） | **~90%**（几乎所有期刊都有） |
| 速度 | 逐个查，87 篇 ~26s | **batch 查（50 DOI/请求），87 篇 ~3s** |
| 数据格式 | 自由文本系级地址 | **标准化机构名**（`"Boston University"` 直接可用） |
| 归一化 | 需要 `_extract_institution()` regex + `_is_institution_like()` 过滤 | **不需要**——OpenAlex 已经做了实体归一化 |
| 老论文覆盖 | 2005 年前几乎全空 | **有**（Cheng 1995 年 USTC 论文可见） |

**CrossRef 保留为 fallback**：当 OpenAlex 查不到时（极少数情况），`_crossref_get_author_affiliations()` 作为后备。

### 原理（OpenAlex 版）

1. 从 Zotero collection 按 DOI+年份分组
2. 每年随机采样 N 篇（默认 3）
3. **batch 查 OpenAlex** `/works?filter=doi:doi1|doi2|...|doi50`（50 DOI/请求）
4. 对每篇论文，`_match_author_in_authorships()` 按 family name + given initial 筛选目标作者
5. 提取该作者的 `institutions[].display_name`（已是标准化名称）
6. 出现频率 >50% 的机构计为该年 confirmed affiliation
7. 年度结果保存为 `affiliation_history` + 扁平化 `known_affiliations`

### 关键函数

- `_openalex_batch_affiliations(dois, family_name, given_initial)` — batch DOI 反查（50/批），返回 `{doi: [inst_names]}`
- `_openalex_get_author_affiliations(doi, family_name, given_initial)` — 单 DOI 查询（track 管线用）
- `_match_author_in_authorships(authorships, family_name, given_initial)` — 从 OpenAlex authorships 数组中提取目标作者的单位
- `_crossref_get_author_affiliations()` — **fallback**，仅当 OpenAlex 查不到时用

### ⚠️ 历史教训：作者级 affiliation 过滤（适用于 OpenAlex 和 CrossRef）

**旧代码** 遍历论文的**所有作者**，收集所有人的 affiliation。这导致：
- Delong Zhang 2018 论文：返回了 USTC（合著者 Wei Chen 的）+ California Medical Innovations（合著者 Huan Chen 的）→ 误判为 Delong 的单位
- "San Diego" 被用户误读为 UCSD

**修复**：无论 OpenAlex 还是 CrossRef，都必须按 family name + given initial 筛选目标作者本人。`_match_author_in_authorships()` 和 `_crossref_get_author_affiliations()` 都实现了这一过滤。

### ⚠️ OpenAlex 的弱点：profile 消歧（不能用作论文发现源）

OpenAlex 把同名作者**合并到一个 profile**（S2 是分成多个干净 profile）。实测：
- Ping Wang `A5011310852`：223 篇"多出"论文里混入环境科学、农业、医学等领域的同名作者
- 138 篇连 DOI 都没有（从中文数据库爬来）

**结论**：OpenAlex **只做 affiliation 数据源**（DOI 反查），**不做论文发现**。论文发现仍走 S2（profile 碎但干净）+ CrossRef（name match 补时效）。

### 覆盖率实测（OpenAlex vs CrossRef 对比）

**Cheng（87 篇采样 / 31 年）**：

| 指标 | CrossRef | OpenAlex |
|------|---------|---------|
| 有 affil 数据 | 35/87 (40%) | **78/87 (90%)** |
| 确认年份 | 10/31 | **29/31** |
| 早期可见 | Harvard(02-04) | **USTC(95-02)→HKUST(00-01)→Harvard(02-04)** |

Cheng 完整轨迹（OpenAlex 验证）：USTC → HKUST → Harvard(02-04) → Purdue(05-17) → BU(18-26)

## Collection 审计与降噪（debug/collection_audit.py）

已有的 Zotero collection 里可能混入假阳性论文（Scholar 抓取噪音、S2 同名混入、同名合作者论文）。用 OpenAlex 逐篇审计，移除可疑论文。

### 审计流程

1. 对 collection 里每篇论文的 DOI，batch 查 OpenAlex `/works?filter=doi:doi1|doi2|...`
2. `_match_author_in_authorships()` 按 family + initial 找目标作者
3. 分类：
   - **✓ CONFIRMED**：目标作者的 institution 匹配 known_affiliations → 保留
   - **⚠ SUSPECT**：目标作者不在作者列表（"author not found"）或 institution 不匹配（"institution mismatch"）→ 移除
   - **? UNCERTAIN**：OpenAlex 查不到该 DOI → 保留，人工审

### ⚠️ Zotero API: 从 collection 移除 item（不要用 DELETE）

`DELETE /collections/{key}/items` 会返回 HTTP 500。**正确做法**：逐个 PATCH item 的 `collections` 字段，移除目标 collection key：

```python
# 1. GET item → 拿 version + current collections
resp = requests.get(f"{BASE_URL}/items/{item_key}", headers=HEADERS)
data = resp.json()["data"]
version = resp.headers["Last-Modified-Version"]

# 2. 移除 collection key
new_collections = [c for c in data["collections"] if c != collection_key]

# 3. PATCH
requests.patch(
    f"{BASE_URL}/items/{item_key}",
    json={"collections": new_collections},
    headers={**HEADERS, "If-Unmodified-Since-Version": version},
)
```

Item 留在库里（出现在 Unfiled），用户可手动复查。

### 2026-06-25 首次审计结果

| 作者 | 总论文 | ✓确认 | ⚠移除 | ?无数据 |
|------|--------|--------|--------|---------|
| Dan Fu | 77 | 71 | 6 | 0 |
| Delong Zhang | 76 | 61 | 12 | 3 |
| Hervé Rigneault | 326 | 269 | 55 | 2 |
| Ji-Xin Cheng | 459 | 416 | 39 | 4 |
| Ping Wang | 49 | 39 | 3 | 7 |
| Wei Min | 133 | 120 | 13 | 0 |

**128 篇移除**。移除清单保存在 `debug/audit_removed_manifest.json`。
脚本：`debug/collection_audit.py`（审计）+ `debug/remove_from_collections.py`（移除）。

### "author not found" vs "institution mismatch"

- **institution mismatch**（高置信假阳性）：目标作者在 OpenAlex 作者列表里，但 institution 跟 known_affiliations 完全对不上（如 Hervé 的 Cegep de Saint Jerome / Cezanne Italy）
- **author not found**（中等置信）：OpenAlex 有这篇论文，但作者列表里找不到 family+initial 匹配。可能是名字变体、补充材料（.s001）、或真假阳性。用户在 Unfiled 手动复查。

### 已知 OpenAlex 数据错误

OpenAlex 偶尔把 institution 标错（如 Cheng 的 Purdue 论文被标为 "Weldon City Schools"）。这类 false alarm 的 institution mismatch 不应直接移除——需要人工确认。

## 状态管理

- 只存 `last_check` 时间戳在 profile.json（谁：Zotero 没有的信息）
- 论文状态全在 Zotero（有没有 PDF、在哪个 collection）
- 不冗余，不会 desync
- **审计结果不自动保存**：`audit_new_papers()` 只输出表格供人工检查，`--download` 才注册到 Zotero。防止脏数据自动入库。

## S2 增量分页（per-ID `s2_paper_counts`）

S2 author papers API **不支持 sort by date**（默认 oldest-first），新论文追加在高 offset。
利用这一点做增量：profile.json 存 `s2_paper_counts`（per-ID dict），下次只拉 `offset >= known_count`。

```python
# 多 ID 场景：每个 s2_id 独立增量
# for s2_id in s2_ids:
#     kc = s2_paper_counts.get(s2_id)  # None = 首次（baseline）
#     dois_i, total_i = _s2_fetch_dois(s2_id, kc)
#     s2_dois |= dois_i               # 并集
#     s2_totals[s2_id] = total_i
```

### Baseline-only 首次运行（重要！）

首次运行（某 ID 的 count 为 `null`）→ **不拉任何论文**，只调 author 端点拿 `paperCount` 记为 baseline：

```
GET /author/{id}?fields=paperCount  →  {"paperCount": 444}
```

存入 `s2_paper_counts[id] = 444`，返回空 set。

**为什么不全量扫？** 用户可能已经在 Zotero/Scholar 里手动删掉了某些条目（如只有摘要的会议记录）。全量扫描会把它们全部扒回来。Baseline-only 策略确保只有 baseline 之后新发表的论文才会被检测。

后续运行 → `incremental from {count}`，通常 1 次 API 调用（~1s）。

profile.json 会自动维护 `s2_paper_counts`（per-ID）和 `s2_paper_count`（聚合，= max）。

## 多作者 cron 设计

**单个 cron 遍历所有作者**（`scripts/track_all.py`），不建多个 cron：
- **动态扫描 `people/*/profile.json`**，自动发现所有追踪作者（不再硬编码列表）
- S2/CrossRef rate limit 是全局的，多 cron 并发反而更容易被限
- 加新作者只需 `lit scholar`（自动建 profile.json），不碰 cron 配置也不改代码
- 5 个作者 × ~4s/人 ≈ 20s（增量模式下）
- `track_all.py` 是 `no_agent=True` 纯脚本：stdout 非空 → 发消息；空 → [SILENT]

## 已知限制

- S2 首次拉取（全量）：444 篇约 15s（5 页 API + delay）。后续增量：~1s
- CrossRef 全名归一化匹配（2026-06-21 起）：精度高，但依赖 CrossRef 给的 given name 是完整拼写。极少数论文只存缩写名（如 "J. Cheng"）时，只有 profile.json alias 里恰好有同形式缩写才会匹配
- CrossRef `from-created-date` 基于 CrossRef 的注册日期，不是论文的出版日期。新论文可能注册延迟
- S2 收录论文的时间可能晚于 CrossRef（S2 需要爬取→索引）
- S2 author search 返回多个同名条目（"Ji-Xin Cheng" 有多个 ID），需手动选 paperCount 最高的。**推荐改用 DOI 反查法**（见上方章节），可自动发现全部重复 profile

## 身份验证信号（Identity Verification）

审计 / track 发现新论文时，如何判断一篇 DOI 确实属于目标作者？三层信号：

### 1. S2 affiliations — 不可用

**S2 `author.affiliations` 字段始终为空 `[]`**。实测：Cheng 的所有 20 个 S2 profile，无论主 profile 还是重复 profile，affiliations 全空。S2 paper API 的 `authors[].affiliations` 同样为空。**不要尝试从 S2 获取作者单位信息。**

### 2. OpenAlex affiliation — 强判据（推荐，2026-06-25 起）

OpenAlex `/works/doi:xxx` 返回结构化的 `authorships[].institutions[].display_name`。

**每篇论文的每个作者都带标准化 institution**（如 `"Boston University"` / `"Purdue University West Lafayette"`），不需要 regex 归一化。

**⚠️ 必须按作者过滤**：`_match_author_in_authorships()` 通过 family name + given initial 筛选目标作者，**只查目标作者本人的 institution**，不是所有合著者的。

CrossRef 作为 fallback：当 OpenAlex 返回空时（极少数），`_crossref_get_author_affiliations()` 接管。

### 3. 年份合理性 — 一票否决

如果 profile.json 有 `birth_year` 字段，year < birth_year 的论文可直接排除。

**Cheng 1971 年生**，S2 主 profile (144507368) 混入了 1973 年液晶论文、1995 年 UHMWPE 论文等非本人早期工作。这些只在 `lit discover-s2` 首次审计时出现，人工排除后不会再出现在增量 track 中。**不需要 `birth_year` 字段自动化**（用户明确否决：加新人时审计一次就够了）。

### 置信度分层 track 管线（已实现）

`find_new_papers()` 返回每篇论文带 `confidence: "high"|"low"`：

| 信号 | 判定 | 行为 |
|------|------|------|
| OpenAlex institution 匹配 known_affiliations | **HIGH** | track_all 自动 import+download，[SILENT] |
| OpenAlex 返回数据但 institution 不匹配 | **LOW** | track_all 输出到 stdout，cron agent 生成 .md 发用户审 |
| OpenAlex 查不到（fallback CrossRef 也空） | **HIGH**（默认信任，DOI 池已 scoped） | 自动处理 |
| known_affiliations 为空 | **LOW**（无法验证 → 人工审） | 输出到 stdout，cron agent 生成 .md |

**`track_all.py` 双通道**：
- HIGH → `import_run()` → `quick_single(item_key=...)` → `attach_single(item_key=...)`，全自动，[SILENT]
- LOW → 输出 DOI + source 到 stdout，cron agent 接管生成 .md 报告

**`_check_affiliation(doi, known_affiliations, affiliation_history, paper_year, family_name, given_initial)` 返回值**：
- `True` — 目标作者 institution 匹配 known_affiliations 或 affiliation_history（high）
- `False` — OpenAlex/CrossRef 有目标作者的数据但 institution 不匹配（low）
- `None` — 查不到 / 目标作者无 institution / known_affiliations 为空（默认 high，DOI 池已 scoped）

注意：每篇 LOW 论文会额外消耗 1 次 OpenAlex API 调用（+ 可能 1 次 CrossRef fallback）。大量新论文时（如首次审计）建议用 `lit discover-s2 --download` 一次性处理，不走 track_all 的逐条检查。

## import → download 的 item_key 传递（关键）

`import_run()` 通过 Zotero **云 API** 创建条目，但 `find_by_doi()` 检查**本地 SQLite**（`zotero.sqlite` 副本）。云创建 → 本地同步有延迟（几秒到分钟级），导致 import 后立即调 `quick_single` / `attach_single` 时 `find_by_doi` 返回 None。

**修复**：`quick_single(doi, item_key=None)` 和 `attach_single(doi, item_key=None)` 接受可选 `item_key`。import 后直接传递：

```python
result = import_run(doi)
if result.get("item_key"):
    qr = quick_single(doi, item_key=result["item_key"])  # skip find_by_doi
```

`lit track --download` 和 `lit discover-s2 --download` 已内置此模式。

## 不可下载源（已确认 paywall，2026-06-21）

新论文检测出来但确实下不到 PDF 的，元数据留在 Zotero 即可，不要反复重试：

| 出版商/源 | DOI 前缀 | 状态 | 原因 |
|-----------|---------|------|------|
| **SPIE** | `10.1117/12.*` | ⛔ 硬 paywall | BU 无订阅，CDP 过 Edge 仍 "Access denied / no subscription"。已硬编码进 `engine.py` 的 `_PUBLISHER_BLACKLIST`。**清 blacklist 重试也是 Access denied，别浪费时间** |
| **researching.cn**（中国期刊，如《Advanced Imaging》） | `10.3788/*` | ⛔ SPA + SSL | DOI 解析到 researching.cn，返回 405 + SPA 动态页，PDF 链接由 JS 渲染不暴露。SSL 证书验证也失败 |
