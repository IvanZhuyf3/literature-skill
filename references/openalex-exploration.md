# OpenAlex vs S2 API Comparison (2026-06-25 Exploration)

探索 OpenAlex 作为 S2 的补充/替代数据源。**状态：PoC 阶段，尚未集成到 tracker。**

## 为什么探索 OpenAlex

S2 的致命短板：**author.affiliations 永远为空 `[]`**。身份验证只能靠 CrossRef（覆盖率 ~40%）。OpenAlex 是 Microsoft Academic Graph 的继承者，免费 API，且**每篇论文的每个作者都带结构化 institution 数据**。

## API 对比

| 维度 | OpenAlex | S2 | CrossRef |
|------|----------|-----|----------|
| API | `api.openalex.org` 免费，无需 key | `api.semanticscholar.org` 免费（100req/5min） | `api.crossref.org` 免费 |
| 收录量 | ~2.5 亿 works | ~2 亿 | ~1.6 亿 DOI |
| 作者消歧 | 有（基于合作者+机构+主题） | 有（authorId） | **无** |
| **作者级 affiliation** | ✅ **每篇论文每个作者都带** | ❌ **永远空** | 有，但覆盖率低（~40%） |
| affiliation 格式 | 结构化 ROR-linked（`{display_name, id, country_code, type}`） | 空 | 纯文本字符串（需要 `_extract_institution()` 归一化） |
| Rate limit | 宽松（10 req/s，邮件=polite pool） | 100 req/5min 无 key | 宽松 |

## PoC 实测（Ping Wang 为例）

### DOI 反查（与 S2 同模式）

```python
import requests
resp = requests.get(
    f"https://api.openalex.org/works/doi:{doi}",
    headers={"User-Agent": "lit-skill/1.0 (mailto:research@example.com)"},
)
work = resp.json()
for au in work.get("authorships", []):
    author = au.get("author", {})
    name = author.get("display_name", "")
    aid = author.get("id", "").split("/")[-1]  # e.g. "A5011310852"
    insts = au.get("institutions", [])
    inst_names = [i.get("display_name", "") for i in insts]
```

### 结果（4 篇测试 DOI）

| DOI | OpenAlex author ID | institutions |
|-----|-------------------|-------------|
| 10.1021/acs.analchem.5b02434 (2015) | A5100338743 | **Purdue University West Lafayette** |
| 10.1117/12.2246098 (2016) | A5011310852 | **Huazhong University of Science and Technology** |
| 10.1021/acs.analchem.2c03981 (2022) | A5011310852 | **Wuhan National Laboratory for Optoelectronics**, HUST |
| 10.1038/s41467-025-59030-8 (2025) | A5011310852 | HUST + Changping + others |

**关键发现**：
- 同一人（A5011310852）的 affiliation 从 HUST 逐步演化到 Changping Lab，**无需手动查 CrossRef 猜**
- 早期 Purdue 论文用了不同 ID（A5100338743），说明 OpenAlex 的消歧也不完美——有重复 profile 问题
- 但 OpenAlex 的优势是：即使 profile 分裂，每个 profile 的论文都带正确的 institution

### 与 S2 对比

OpenAlex 搜 "Ping Wang" 返回 2610 个 profile。DOI 反查发现至少 2 个真 profile（A5100338743 + A5011310852），比 S2 的 5 个候选更容易区分——因为 OpenAlex **每个 profile 都带 topics 列表**，可以快速排除不相关领域（催化/电池/免疫学 vs 光谱成像）。

## OpenAlex 能解决的问题

1. **替代 CrossRef 做 affiliation 验证**：不需要 `_extract_institution()` regex 归一化，OpenAlex 直接给 ROR-linked 结构化机构名
2. **S2 profile 候选筛选**：用 institution 匹配（Purdue→HUST 的轨迹）确认同一人
3. **搬家问题**：OpenAlex 按论文记录 institution，自然支持同年多单位

## 尚未解决的问题

- OpenAlex 也有重复 profile（Purdue-era Ping Wang ≠ HUST-era Ping Wang ID）
- OpenAlex 消歧论文可能不如 S2 精确（arXiv:2502.11610 报告 Chinese authors 消歧精度不高）
- 需要实测覆盖率：OpenAlex 对 SPIE/Optica 论文的作者 institution 覆盖率是否比 CrossRef 好

## 集成路径（如果决定接入）

1. 加 `_openalex_reverse_lookup(dois, family_name, given_initial)` 到 tracker.py
2. 用 OpenAlex institution 数据补充/替代 CrossRef `_check_crossref_affiliation()`
3. 在 `build-affiliations` 中用 OpenAlex 替代 CrossRef（直接结构化数据，不需要 regex 归一化）
4. 用 OpenAlex topics 字段辅助 S2 profile 筛选（光谱成像 vs 催化的 Ping Wang）

**API 代码**：`debug/test_openalex.py`（PoC 脚本）
