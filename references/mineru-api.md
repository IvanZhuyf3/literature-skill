# MinerU Online API Quick Reference

> Source: https://mineru.net/apiManage/docs (extracted 2026-06-16)
> Used by: `pdf_parser.py` — PDF → Markdown structural extraction

## Authentication

- **Token**: Create at https://mineru.net/apiManage (API Management page)
- **Header**: `Authorization: Bearer <token>`
- **Validity**: 90 days

## Two API Modes

| Dimension | 🎯 Precision Extract | ⚡ Agent Lightweight |
|-----------|---------------------|---------------------|
| Token | ✅ Required | ❌ No (IP rate-limited) |
| Endpoint | `/api/v4/file-urls/batch` or `/api/v4/extract/task` | `/api/v1/agent/parse/url` |
| Model | pipeline / **vlm** (recommended) / MinerU-HTML | Fixed lightweight |
| File size | ≤ 200MB | ≤ 10MB |
| Pages | ≤ 200 | ≤ 20 |
| Batch | ✅ (≤ 200 files) | ❌ Single only |
| Output | ZIP (Markdown + JSON) | Markdown (CDN link) |

**We use Precision Extract** (vlm model) for paper-grade accuracy.

## Local File Upload Flow (batch endpoint)

Our `pdf_parser.py` uses this path — local PDF files don't have public URLs.

### Step 1: Request upload URL

```
POST https://mineru.net/api/v4/file-urls/batch
Authorization: Bearer <token>
Content-Type: application/json

{
  "files": [{"name": "paper.pdf"}],
  "model_version": "vlm",
  "enable_formula": true,
  "enable_table": true,
  "language": "en"
}
```

**Response**:
```json
{"code": 0, "data": {"batch_id": "xxx", "file_urls": ["https://...signed-url..."]}}
```

### Step 2: Upload file (PUT, no Content-Type)

```python
with open("paper.pdf", "rb") as f:
    requests.put(upload_url, data=f)  # NO Content-Type header!
```

System auto-submits extract task after upload. No separate submit call needed.

### Step 3: Poll for result

```
GET https://mineru.net/api/v4/extract-results/batch/{batch_id}
Authorization: Bearer <token>
```

**States**: `pending` → `running` (shows `extracted_pages/total_pages`) → `done` | `failed`

**Done response**:
```json
{"data": {"extract_result": [{"state": "done", "full_zip_url": "https://...zip"}]}}
```

### Step 4: Download ZIP, extract `full.md`

ZIP contains: `full.md` (main markdown), `layout.json`, `model.json`, `content_list.json`, images.

## URL-Based Flow (alternative)

For files with public URLs (not used by pdf_parser.py — papers are local):

```
POST https://mineru.net/api/v4/extract/task
{"url": "https://...", "model_version": "vlm"}
```
Returns `task_id`. Query: `GET /api/v4/extract/task/{task_id}`.

⚠️ **Overseas URLs (GitHub, AWS) may time out** — MinerU servers are in China.

## Key Parameters

| Parameter | Default | Notes |
|-----------|---------|-------|
| `model_version` | `pipeline` | `vlm` recommended (highest accuracy) |
| `enable_formula` | `true` | Formula recognition |
| `enable_table` | `true` | Table structure recognition |
| `language` | `ch` | Use `en` for English papers |
| `page_ranges` | all | e.g. `"1-10"`, `"2,4-6"` |
| `is_ocr` | `false` | Enable for scanned PDFs |
| `extra_formats` | none | `["docx","html","latex"]` optional exports |

## Rate Limits

- **Free**: 5000 pages/day, ≤200 pages/file
- **High priority**: 1000 pages/day (pages beyond 1000 get lower priority)
- Token validity: 90 days

## Auto-Splitting for Large PDFs (2026-06-20)

MinerU API limits: single file ≤200MB, ≤200 pages. `parse_pdf()` now auto-handles this:

1. **`_needs_splitting(filepath)`** checks file size (>200MB) and page count (>200, via PyMuPDF `fitz`)
2. **`_split_pdf(filepath)`** uses PyMuPDF to split into ≤200-page chunks, saves to temp files
3. Each chunk is uploaded/parsed independently with its own SHA256 cache key
4. Results merged with `"\n\n---\n\n"` separator (markdown horizontal rule)
5. Merged result cached under the original file's SHA256
6. Temp chunk files cleaned up in `finally` block

**Dependency**: `pymupdf` (`fitz`) installed in Hermes venv — used for page counting and PDF splitting.

**Partial failure handling**: if some chunks fail, remaining successful chunks are still merged (partial results > no results).

## Common Pitfalls

1. **No Content-Type on upload**: The PUT upload request must NOT include `Content-Type` header. Including it causes auth/signature failures.
2. **Overseas URL timeout**: URLs from GitHub/AWS may time out. Upload local files instead.
3. **Batch vs single**: Batch endpoint (`/file-urls/batch`) is for local file upload. URL endpoint (`/extract/task`) is for remote URLs. Don't mix them.
4. **Poll interval**: 5s is optimal. MinerU processes ~1-2 pages/sec with vlm model.
5. **ZIP structure**: `full.md` is the main result. Other JSON files are intermediate layout data.

## Validated Test (2026-06-17)

- **File**: Nature Microbiology paper, 7.4MB PDF
- **Model**: vlm
- **Result**: 186,055 chars Markdown in ~15s total (upload + parse + download)
- **Quality**: Title hierarchy, author list, abstract, body paragraphs, figure references (`![](images/...)`), and even flowcharts extracted as mermaid code blocks. Author names correctly identified.
- **Cache**: SHA256 hash → `cache/mineru/501e4b02be678986.md`
