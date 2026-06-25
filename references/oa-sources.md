# OA 下载源 API 参考

> `lit quick` 的快速下载源实现细节。每个源是 `lit/download/` 下的一个独立模块，
> 注册到 `quick_download.py` 的 `_METHODS` 列表。

## 添加新源

1. 创建 `lit/download/<source_name>.py`，函数签名 `fn(doi, year=None) -> Path | None`
2. 在 `quick_download.py` 的 `_METHODS` 列表加 `(显示名, 函数)`
3. 不需要改其他文件

## 当前源

### Crossref TDM (`crossref_tdm.py`)
- **API**: `GET https://api.crossref.org/works/{doi}`
- **提取**: `message.link[]` 数组中 `content-type` 含 `pdf` 或 URL 以 `.pdf` 结尾的条目
- **排序**: `intended-application=vor`（version of record）优先
- **Key**: 不需要
- **Gotcha**: `link[].content-type` 常为 `"unspecified"` 而非 `"application/pdf"`，需同时检查 URL 后缀
- **Gotcha**: DOI 路径不 URL-encode 斜杠（`/works/10.1038/xxx` 不是 `%2F`）

### Preprint arXiv 直连 (`preprint.py`)
- **匹配**: DOI 前缀 `10.48550/arXiv.*`
- **URL**: `https://arxiv.org/pdf/{arxiv_id}.pdf`（无反爬，纯 HTTP 秒级下载）
- **仅限 arXiv**：bioRxiv/medRxiv（`10.1101/`）和 ChemRxiv（`10.26434/`）有 Cloudflare 保护或无可预测 URL，纯 HTTP 会 403，必须走 `lit attach` 的 CDP adapter
- **预印本 DOI 前缀速查**：

  | 前缀 | 服务器 | quick 能下？ | 原因 |
  |------|--------|:---:|------|
  | `10.48550/arXiv.*` | arXiv | ✅ | 无反爬 |
  | `10.1101/` | bioRxiv / medRxiv | ❌ | Cloudflare 403 → 走 attach CDP |
  | `10.26434/chemrxiv-*` | ChemRxiv | ❌ | 无可预测 URL → 走 attach |

### Sci-Hub CDP (`scihub_cdp.py`)
- **方案**: Edge CDP 打开 Sci-Hub 页面，DDoS-Guard 自然过，提取 PDF URL 后浏览器 fetch 下载
- **年份限制**: `config.yaml` 的 `scihub.max_year`（默认 2021）
- **镜像**: `sci-hub.ru`
- **详见**: memory 中的 Sci-Hub 条目

### Unpaywall (`unpaywall.py`)
- **API**: `GET https://api.unpaywall.org/v2/{doi}?email={email}`
- **提取**: `best_oa_location.url_for_pdf`，fallback 到 `oa_locations[].url_for_pdf`
- **Key**: 不需要，但建议填 email（`config.yaml` 的 `unpaywall.email`）走 polite pool
- **Gotcha**: 空 email 会 422，代码有 fallback placeholder
- **Gotcha**: DOI 路径不 URL-encode 斜杠
- **覆盖率**: OA 论文（bioRxiv、eLife、PLOS、MDPI、Frontiers 等全 OA 出版商效果好）

## 已评估但未采用的源

| 源 | 原因 |
|----|------|
| Elsevier/Springer/Wiley TDM API | 返回 XML 非 PDF，需 API Key 注册，与 PDF 下载目标不符 |
| CORE | API 覆盖率与 Unpaywall 重叠 |
| publisher BeautifulSoup 抓取 | 改版即碎，CDP adapter 更鲁棒 |

## _download_pdf 通用验证

所有源的 `_download_pdf()` 统一验证：
1. HTTP 200
2. Content ≥ 10KB
3. Header `%PDF`
4. 文件名: `{source}_{doi_safe}.pdf`
