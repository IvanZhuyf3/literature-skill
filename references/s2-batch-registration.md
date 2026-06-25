# S2 DOI → CrossRef 批量注册

当 `lit scholar` 标题匹配率低（<30%，常见于法语/老欧洲期刊学者），用 Semantic Scholar API 直接拉 DOI，再从 CrossRef 精确查元数据。

## 适用场景

- Scholar 抓取成功但 CrossRef 标题匹配率低（法语论文、截断标题、老期刊）
- 学者有大量会议论文（Scholar 过滤掉了）但期刊论文也没注册全
- 已有 S2 author ID（从 `lit track` 或手动查 S2 获取）

## 流程

```python
# 1. S2 API 拉全部 DOI（分页 100，~5 页）
import requests
all_dois = set()
offset = 0
while True:
    r = requests.get(
        f"https://api.semanticscholar.org/graph/v1/author/{S2_ID}/papers",
        params={"fields": "externalIds", "limit": 100, "offset": offset},
        timeout=30
    )
    if r.status_code == 429:
        time.sleep(30); continue  # rate limit
    papers = r.json().get("data", [])
    if not papers: break
    for p in papers:
        doi = (p.get("externalIds") or {}).get("DOI")
        if doi: all_dois.add(doi.lower())
    offset += 100
    time.sleep(1)  # polite

# 2. diff Zotero 已有 DOI（本地 SQLite，秒级）
#    用 pyzotero 或 lit.core.zotero.find_by_doi() 逐个查

# 3. 缺失 DOI 逐个调 CrossRef /works/{doi} 拿元数据
r = requests.get(f"https://api.crossref.org/works/{doi}", timeout=15)
m = r.json()["message"]
meta = {
    "DOI": doi,
    "title": m.get("title", [""])[0],
    "year": str(m.get("published", {}).get("date-parts", [[""]])[0][0] or ""),
    "journal": m.get("container-title", [""])[0] if m.get("container-title") else "",
    "authors": [f"{a.get('given','')} {a.get('family','')}".strip()
                for a in m.get("author", []) if a.get("family")],
}

# 4. 批量注册
from lit.batch.register import register_papers
register_papers(papers_list, collection_key)
```

## 关键点

- **check_duplicate 只走 DOI**（`check_duplicate(doi=doi, title="", url="")`）：避免 `find_by_url` 的 API 搜索返回非 dict 导致 `AttributeError`
- **subprocess 调 `lit import` 太慢**：每篇重新启动 Python + 加载模块，~5s/篇。单进程调 `register_papers()` 或直接 `zot.create_item()` 快 10 倍
- **CrossRef 元数据成功率 ~99%**（DOI 精确匹配），远高于标题搜索
- **figshare 等非论文 DOI**：CrossRef 返回 404，跳过即可

## 实测数据

Rigneault（Institut Fresnel）：Scholar 标题匹配 107 篇 → S2 DOI 补到 387 篇（+216 新建 +64 已有归入）。S2 总 480 篇，其中 341 篇有 DOI。
