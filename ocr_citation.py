#!/usr/bin/env python3
"""
ocr_citation.py — 从图片中提取学术引用，通过 CrossRef API 确认 DOI。

用法：
  python ocr_citation.py <image_path> [--json] [--all]

流程：
  1. 调 DeepSeek Vision API 识别图片中的引用信息
  2. 对每条引用用 CrossRef API 搜索确认，获取正确 DOI 和完整元数据
  3. 输出结构化结果

前置：
  - DeepSeekWeb2API 服务需在 http://127.0.0.1:3000 运行
"""

import base64
import json
import sys
import textwrap
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

# ── 配置 ──────────────────────────────────────────────
API_URL = "http://127.0.0.1:3000/v1/chat/completions"
API_KEY = "sk-local"
CROSSREF_URL = "https://api.crossref.org/works"
VISION_TIMEOUT = 300  # 5 minutes
CROSSREF_TIMEOUT = 15


# ── DeepSeek Vision 调用 ──────────────────────────────

def call_vision(image_path: str, prompt: str) -> str:
    """调用 DeepSeek Vision API，返回文本响应。"""
    img = Path(image_path)
    if not img.exists():
        print(f"ERROR: Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    ext = img.suffix.lower()
    mime_map = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
                ".gif": "image/gif", ".webp": "image/webp", ".bmp": "image/bmp"}
    mime = mime_map.get(ext, "image/jpeg")
    b64 = base64.b64encode(img.read_bytes()).decode()

    body = json.dumps({
        "model": "deepseek-vision",
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}}
        ]}]
    }).encode()

    req = urllib.request.Request(API_URL, data=body, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=VISION_TIMEOUT) as resp:
            result = json.loads(resp.read().decode())
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            if not content:
                print("ERROR: Empty response from DeepSeek Vision", file=sys.stderr)
                sys.exit(1)
            return content
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:500]
        print(f"ERROR: DeepSeek Vision API {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: DeepSeek Vision request failed: {e}", file=sys.stderr)
        sys.exit(1)


# ── CrossRef 搜索 ─────────────────────────────────────

def crossref_search(query: str, rows: int = 3) -> list[dict]:
    """搜索 CrossRef，返回匹配结果列表。"""
    params = urllib.parse.urlencode({"query": query, "rows": rows})
    url = f"{CROSSREF_URL}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "LiteratureSkill/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=CROSSREF_TIMEOUT) as resp:
            data = json.loads(resp.read().decode())
            return data.get("message", {}).get("items", [])
    except Exception as e:
        print(f"WARNING: CrossRef search failed for '{query[:50]}': {e}", file=sys.stderr)
        return []


def extract_doi_from_ocr(ocr_text: str) -> list[dict]:
    """从 OCR 文本中解析出结构化引用列表。"""
    prompt = textwrap.dedent(f"""\
        The following text was OCR'd from a photo of a presentation slide. Extract ALL academic references/citations from it.

        For EACH reference found, output EXACTLY this JSON format (one per line):
        {{"authors": "Author1, Author2", "title": "Paper title", "journal": "Journal name", "year": "YYYY", "volume": "V", "pages": "PP-PP", "doi": "10.xxxx/xxxxx"}}

        Rules:
        - If a field is not visible, use empty string ""
        - Output ONLY the JSON lines, no other text
        - Be precise with author names and title words

        OCR text:
        {ocr_text}""")

    # 这里我们不用再次调 vision，而是直接解析 OCR 输出
    # 但 OCR 输出可能不够结构化，所以用正则尝试提取
    refs = []
    for line in ocr_text.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("Note") or line.startswith("Based"):
            continue
        # 尝试解析 JSON 行
        if line.startswith("{"):
            try:
                ref = json.loads(line.rstrip(","))
                refs.append(ref)
            except json.JSONDecodeError:
                continue
    if not refs:
        # Fallback: 把整个 OCR 文本当做一个引用去 CrossRef 搜
        refs = [{"raw_ocr": ocr_raw, "authors": "", "title": "", "journal": "", "year": "", "doi": ""}]
    return refs


def enrich_with_crossref(refs: list[dict]) -> list[dict]:
    """对每条引用用 CrossRef 确认并补充 DOI。"""
    enriched = []
    for ref in refs:
        # 构建搜索 query
        parts = []
        if ref.get("title"):
            parts.append(ref["title"])
        if ref.get("authors"):
            # 只取第一个作者的姓
            first_author = ref["authors"].split(",")[0].split(" ")[-1].strip()
            parts.append(first_author)
        if ref.get("journal"):
            parts.append(ref["journal"])
        if ref.get("year"):
            parts.append(ref["year"])

        query = " ".join(parts).strip()
        # Fallback: 如果结构化字段为空，用 raw_ocr 文本做 query
        if not query and ref.get("raw_ocr"):
            # 取 OCR 文本中看起来像引用的部分（第一段非空内容）
            raw = ref["raw_ocr"].strip()
            # 去掉常见前缀
            for prefix in ["Based on the slide image", "Here are", "The following"]:
                if raw.lower().startswith(prefix.lower()):
                    # 取第一行实际内容
                    lines = [l.strip() for l in raw.split("\n") if l.strip() and not l.strip().startswith(prefix)]
                    if lines:
                        raw = lines[0]
                    break
            # 截断到 CrossRef 能接受的长度（~200 字符）
            query = raw[:200]
        if not query.strip():
            enriched.append({**ref, "crossref_doi": "", "crossref_title": "", "crossref_score": 0})
            continue

        results = crossref_search(query)
        if results:
            best = results[0]
            cr_doi = best.get("DOI", "")
            cr_title = best.get("title", [""])[0]
            cr_authors = ", ".join(
                f"{a.get('family', '')} {a.get('given', '')}".strip()
                for a in best.get("author", [])[:3]
            )
            cr_journal = best.get("container-title", [""])[0]
            cr_year = str(best.get("published-print", best.get("published-online", {}))
                          .get("date-parts", [[0]])[0][0])
            enriched.append({
                **ref,
                "crossref_doi": cr_doi,
                "crossref_title": cr_title,
                "crossref_authors": cr_authors,
                "crossref_journal": cr_journal,
                "crossref_year": cr_year,
                "crossref_score": best.get("score", 0),
            })
        else:
            enriched.append({**ref, "crossref_doi": "", "crossref_score": 0})

    return enriched


# ── 主流程 ─────────────────────────────────────────────

OCR_PROMPT = textwrap.dedent("""\
    Read ALL academic references/citations visible in this image.
    For EACH reference, output exactly this JSON format on its own line:
    {"authors": "Author1, Author2", "title": "Full paper title", "journal": "Journal name", "year": "YYYY", "volume": "V", "pages": "PP-PP", "doi": "10.xxxx/xxxxx"}

    Rules:
    - If a field is not visible, use empty string ""
    - Output ONLY the JSON lines, nothing else
    - Be as precise as possible with every word
    - Include ALL references visible in the image, even partial ones""")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Extract citations from image via OCR + CrossRef")
    parser.add_argument("image", help="Path to image file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--all", action="store_true", help="Show all CrossRef matches (not just best)")
    args = parser.parse_args()

    # Step 1: OCR via DeepSeek Vision
    print("Step 1/2: Reading image with DeepSeek Vision...", file=sys.stderr)
    ocr_raw = call_vision(args.image, OCR_PROMPT)

    # Step 2: Parse + CrossRef verify
    refs = extract_doi_from_ocr(ocr_raw)

    if not refs:
        # OCR 没返回结构化 JSON，直接输出原文让调用方处理
        print("WARNING: Could not parse structured references from OCR output.", file=sys.stderr)
        print(f"OCR_RAW:{ocr_raw}", file=sys.stderr)
        if args.json:
            print(json.dumps({"ocr_raw": ocr_raw, "refs": []}, ensure_ascii=False))
        else:
            print("OCR output (unstructured):")
            print(ocr_raw)
        sys.exit(0)

    print(f"Step 2/2: Verifying {len(refs)} reference(s) via CrossRef...", file=sys.stderr)
    enriched = enrich_with_crossref(refs)

    # Output
    if args.json:
        print(json.dumps({"refs": enriched}, ensure_ascii=False, indent=2))
    else:
        for i, ref in enumerate(enriched, 1):
            print(f"\n--- Reference {i} ---")
            print(f"  Title:    {ref.get('crossref_title') or ref.get('title', '?')}")
            print(f"  Authors:  {ref.get('crossref_authors') or ref.get('authors', '?')}")
            print(f"  Journal:  {ref.get('crossref_journal') or ref.get('journal', '?')}")
            print(f"  Year:     {ref.get('crossref_year') or ref.get('year', '?')}")
            print(f"  DOI:      {ref.get('crossref_doi') or ref.get('doi', 'NOT FOUND')}")
            if ref.get("volume"):
                print(f"  Volume:   {ref['volume']}")
            if ref.get("pages"):
                print(f"  Pages:    {ref['pages']}")

    # 机器可读行（给 skill dispatcher 用）
    for ref in enriched:
        doi = ref.get("crossref_doi") or ""
        title = ref.get("crossref_title") or ref.get("title", "")
        print(f"CITATION: doi={doi}|title={title}", file=sys.stderr)


if __name__ == "__main__":
    main()
