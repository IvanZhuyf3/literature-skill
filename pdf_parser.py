"""
MinerU Online API PDF Parser.

Uploads PDF to MinerU (mineru.net) for high-accuracy structural extraction.
Returns clean Markdown with preserved tables, formulas, and reading order.

Usage (CLI):
    set PYTHONIOENCODING=utf-8 && python pdf_parser.py <pdf_path> [--output <md_path>]

Usage (module):
    from pdf_parser import parse_pdf
    markdown_text = parse_pdf("path/to/paper.pdf")
    # → returns full markdown string, or None on failure

Requires: token in config.yaml under "mineru" → "token".
Get token from https://mineru.net/apiManage (API Management page).
"""

import os
import sys
import time
import json
import zipfile
import hashlib
import logging
import requests
import yaml

logger = logging.getLogger(__name__)

BASE_URL = "https://mineru.net"
DEFAULT_MODEL = "vlm"       # recommended, highest accuracy
DEFAULT_LANGUAGE = "en"     # English papers (change to "ch" for Chinese)
POLL_INTERVAL = 5           # seconds between polling
POLL_TIMEOUT = 300          # 5 min max wait for single paper
MAX_FILE_SIZE = 200 * 1024 * 1024  # 200MB API limit
MAX_PAGE_COUNT = 200                 # API limit


def load_config(config_path=None):
    """Load config.yaml from skill base directory."""
    if config_path is None:
        # Resolve relative to this file (skill base)
        skill_base = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(skill_base, "config.yaml")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        logger.error(f"config.yaml not found at {config_path}")
        return {}


def _get_token(config=None):
    """Extract MinerU token from config."""
    if config is None:
        config = load_config()
    token = config.get("mineru", {}).get("token", "")
    if not token:
        raise ValueError(
            "MinerU token not found. Add to config.yaml:\n"
            "  mineru:\n"
            "    token: \"your-token-here\"\n"
            "Get token from https://mineru.net/apiManage"
        )
    return token


def _get_cache_dir(config=None):
    """Get cache directory for parsed markdown."""
    if config is None:
        config = load_config()
    cache_dir = config.get("mineru", {}).get("cache_dir", "")
    if not cache_dir:
        skill_base = os.path.dirname(os.path.abspath(__file__))
        cache_dir = os.path.join(skill_base, "cache", "mineru")
    os.makedirs(cache_dir, exist_ok=True)
    return cache_dir


def _file_hash(filepath):
    """SHA256 hash of file for cache key."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:16]  # 16 chars is enough for dedup


def _get_page_count(filepath):
    """Get PDF page count using PyMuPDF."""
    import fitz
    doc = fitz.open(filepath)
    count = doc.page_count
    doc.close()
    return count


def _needs_splitting(filepath):
    """Check if PDF exceeds MinerU limits (200MB or 200 pages)."""
    file_size = os.path.getsize(filepath)
    if file_size > MAX_FILE_SIZE:
        return True
    try:
        pages = _get_page_count(filepath)
        if pages > MAX_PAGE_COUNT:
            return True
    except Exception as e:
        logger.warning(f"Could not read page count: {e}")
    return False


def _split_pdf(filepath, max_pages=MAX_PAGE_COUNT, cache_dir=None):
    """Split a large PDF into chunks of ≤max_pages.

    Returns: list of (temp_file_path, page_range_str) tuples.
    Caller is responsible for cleaning up temp files.
    """
    import fitz
    import tempfile

    doc = fitz.open(filepath)
    total_pages = doc.page_count

    chunks = []
    chunk_idx = 0
    start_page = 0
    while start_page < total_pages:
        end_page = min(start_page + max_pages, total_pages)

        # Create chunk PDF
        chunk_doc = fitz.open()
        chunk_doc.insert_pdf(doc, from_page=start_page, to_page=end_page - 1)

        # Save to temp file
        prefix = os.path.splitext(os.path.basename(filepath))[0]
        tmp_fd, tmp_path = tempfile.mkstemp(
            suffix=f"_p{start_page+1}-{end_page}.pdf",
            prefix=f"{prefix}_chunk{chunk_idx}_",
            dir=cache_dir,
        )
        os.close(tmp_fd)
        chunk_doc.save(tmp_path)
        chunk_doc.close()

        page_range = f"{start_page + 1}-{end_page}"
        chunks.append((tmp_path, page_range))
        logger.info(f"  Chunk {chunk_idx}: pages {page_range} "
                     f"({os.path.getsize(tmp_path) / 1024 / 1024:.1f}MB)")

        start_page = end_page
        chunk_idx += 1

    doc.close()
    return chunks


def _upload_and_parse(filepath, token, config, model_version=None,
                      enable_formula=True, enable_table=True,
                      language=None, page_ranges=None):
    """
    Upload local PDF to MinerU and return batch_id.
    
    Uses the batch file-urls endpoint: request signed upload URL,
    PUT the file, system auto-submits extract task.
    
    Returns: batch_id string, or None on failure.
    """
    filename = os.path.basename(filepath)
    model_version = model_version or config.get("mineru", {}).get("model_version", DEFAULT_MODEL)
    language = language or config.get("mineru", {}).get("language", DEFAULT_LANGUAGE)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    
    # Request signed upload URL
    payload = {
        "files": [{"name": filename}],
        "model_version": model_version,
        "enable_formula": enable_formula,
        "enable_table": enable_table,
        "language": language,
    }
    if page_ranges:
        payload["files"][0]["page_ranges"] = page_ranges
    
    logger.info(f"Requesting upload URL for {filename}...")
    resp = requests.post(f"{BASE_URL}/api/v4/file-urls/batch",
                         headers=headers, json=payload, timeout=30)
    if resp.status_code != 200:
        logger.error(f"Upload URL request failed: HTTP {resp.status_code}")
        logger.error(f"Response: {resp.text[:500]}")
        return None
    
    data = resp.json()
    if data.get("code") != 0:
        logger.error(f"API error: {data.get('msg', 'unknown')}")
        return None
    
    batch_id = data["data"]["batch_id"]
    upload_url = data["data"]["file_urls"][0]
    
    # Upload file (PUT, no Content-Type header)
    logger.info(f"Uploading {filename} ({os.path.getsize(filepath) / 1024 / 1024:.1f}MB)...")
    with open(filepath, "rb") as f:
        upload_resp = requests.put(upload_url, data=f, timeout=120)
    
    if upload_resp.status_code != 200:
        logger.error(f"File upload failed: HTTP {upload_resp.status_code}")
        return None
    
    logger.info(f"Upload complete. batch_id={batch_id}")
    return batch_id


def _poll_batch_result(batch_id, token, timeout=None):
    """
    Poll batch extract result until done or timeout.
    
    Returns: dict with 'full_zip_url' on success, None on failure/timeout.
    """
    timeout = timeout or POLL_TIMEOUT
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URL}/api/v4/extract-results/batch/{batch_id}"
    
    start = time.time()
    while time.time() - start < timeout:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code != 200:
            logger.warning(f"Poll HTTP {resp.status_code}, retrying...")
            time.sleep(POLL_INTERVAL)
            continue
        
        data = resp.json().get("data", {})
        results = data.get("extract_result", [])
        
        if not results:
            time.sleep(POLL_INTERVAL)
            continue
        
        result = results[0]  # single file
        state = result.get("state", "unknown")
        
        if state == "done":
            zip_url = result.get("full_zip_url", "")
            logger.info(f"Parse complete. ZIP: {zip_url[:80]}...")
            return result
        elif state == "failed":
            err = result.get("err_msg", "unknown error")
            logger.error(f"Parse failed: {err}")
            return None
        else:
            # pending / running / converting
            progress = result.get("extract_progress", {})
            extracted = progress.get("extracted_pages", 0)
            total = progress.get("total_pages", 0)
            if total > 0:
                logger.info(f"State: {state} ({extracted}/{total} pages)")
            else:
                logger.info(f"State: {state}")
            time.sleep(POLL_INTERVAL)
    
    logger.error(f"Timeout after {timeout}s waiting for batch {batch_id}")
    return None


def _download_and_extract_zip(zip_url, cache_dir):
    """
    Download result ZIP and extract markdown.
    
    Returns: (markdown_text, zip_local_path) or (None, None)
    """
    logger.info("Downloading result ZIP...")
    resp = requests.get(zip_url, timeout=120)
    if resp.status_code != 200:
        logger.error(f"ZIP download failed: HTTP {resp.status_code}")
        return None, None
    
    # Save ZIP
    zip_path = os.path.join(cache_dir, "result.zip")
    with open(zip_path, "wb") as f:
        f.write(resp.content)
    
    # Extract markdown
    markdown_text = None
    with zipfile.ZipFile(zip_path, "r") as zf:
        for name in zf.namelist():
            if name.endswith("full.md") or name.endswith(".md"):
                markdown_text = zf.read(name).decode("utf-8")
                logger.info(f"Extracted markdown from: {name} ({len(markdown_text)} chars)")
                break
    
    if markdown_text is None:
        logger.error("No markdown file found in ZIP")
        logger.debug(f"ZIP contents: {zipfile.ZipFile(zip_path).namelist()}")
    
    return markdown_text, zip_path


def parse_pdf(filepath, config=None, use_cache=True, **kwargs):
    """
    Parse a PDF file via MinerU online API.
    
    Automatically splits PDFs exceeding 200 pages or 200MB into chunks,
    parses each separately, and merges the markdown results.

    Args:
        filepath: Path to PDF file
        config: Config dict (auto-loaded if None)
        use_cache: If True, skip re-parsing if cached result exists
        **kwargs: Override model_version, enable_formula, enable_table,
                  language, page_ranges

    Returns:
        Markdown string on success, None on failure.
    
    Cache:
        Results cached by file SHA256 hash in cache/mineru/.
        Repeated calls with same PDF return cached result instantly.
    """
    if not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        return None
    
    file_size = os.path.getsize(filepath)
    if file_size > MAX_FILE_SIZE and not _needs_splitting(filepath):
        logger.error(f"File too large: {file_size / 1024 / 1024:.1f}MB (limit {MAX_FILE_SIZE / 1024 / 1024:.0f}MB)")
        return None
    
    if config is None:
        config = load_config()
    
    token = _get_token(config)
    cache_dir = _get_cache_dir(config)
    
    # Cache check
    file_hash = _file_hash(filepath)
    cache_file = os.path.join(cache_dir, f"{file_hash}.md")
    if use_cache and os.path.exists(cache_file):
        logger.info(f"Cache hit: {cache_file}")
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()
    
    # ── Split large PDFs into chunks ──
    if _needs_splitting(filepath):
        pages = _get_page_count(filepath)
        n_chunks = (pages + MAX_PAGE_COUNT - 1) // MAX_PAGE_COUNT
        logger.info(f"PDF has {pages} pages — splitting into {n_chunks} chunks of ≤{MAX_PAGE_COUNT} pages")
        
        chunks = _split_pdf(filepath, max_pages=MAX_PAGE_COUNT, cache_dir=cache_dir)
        markdown_parts = []
        temp_files = [cp for cp, _ in chunks]
        
        try:
            for i, (chunk_path, page_range) in enumerate(chunks):
                logger.info(f"Parsing chunk {i+1}/{len(chunks)} (pages {page_range})...")
                
                # Check chunk cache
                chunk_hash = _file_hash(chunk_path)
                chunk_cache = os.path.join(cache_dir, f"{chunk_hash}.md")
                if use_cache and os.path.exists(chunk_cache):
                    with open(chunk_cache, "r", encoding="utf-8") as f:
                        md = f.read()
                    logger.info(f"  Chunk {i+1} cache hit")
                else:
                    # Upload + poll this chunk
                    batch_id = _upload_and_parse(chunk_path, token, config, **kwargs)
                    if batch_id is None:
                        logger.error(f"  Chunk {i+1} upload failed")
                        continue
                    result = _poll_batch_result(batch_id, token,
                                                timeout=kwargs.get("timeout", POLL_TIMEOUT))
                    if result is None:
                        logger.error(f"  Chunk {i+1} parse failed/timeout")
                        continue
                    zip_url = result.get("full_zip_url", "")
                    md, _ = _download_and_extract_zip(zip_url, cache_dir)
                    if md is None:
                        logger.error(f"  Chunk {i+1} download failed")
                        continue
                    # Cache chunk
                    with open(chunk_cache, "w", encoding="utf-8") as f:
                        f.write(md)
                
                markdown_parts.append(md)
        finally:
            # Clean up temp chunk files
            for tf in temp_files:
                try:
                    os.unlink(tf)
                except Exception:
                    pass
        
        if not markdown_parts:
            logger.error("All chunks failed")
            return None
        
        # Merge: join with page separator
        merged = "\n\n---\n\n".join(markdown_parts)
        logger.info(f"Merged {len(markdown_parts)}/{len(chunks)} chunks "
                     f"({len(merged)} chars total)")
        
        # Cache merged result
        with open(cache_file, "w", encoding="utf-8") as f:
            f.write(merged)
        logger.info(f"Cached to: {cache_file}")
        
        return merged
    
    # ── Normal path: single upload ──
    # Step 1: Upload + submit
    batch_id = _upload_and_parse(filepath, token, config, **kwargs)
    if batch_id is None:
        return None
    
    # Step 2: Poll for result
    result = _poll_batch_result(batch_id, token,
                                timeout=kwargs.get("timeout", POLL_TIMEOUT))
    if result is None:
        return None
    
    zip_url = result.get("full_zip_url", "")
    if not zip_url:
        logger.error("No full_zip_url in result")
        return None
    
    # Step 3: Download ZIP + extract markdown
    markdown_text, _ = _download_and_extract_zip(zip_url, cache_dir)
    if markdown_text is None:
        return None
    
    # Step 4: Cache result
    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(markdown_text)
    logger.info(f"Cached to: {cache_file}")
    
    return markdown_text


def parse_pdf_batch(filepaths, config=None, use_cache=True, **kwargs):
    """
    Parse multiple PDFs via MinerU batch API.
    
    Uploads all files in one batch request (max 50), polls once.
    More efficient than individual parse_pdf() calls for bulk digest.
    
    Args:
        filepaths: List of PDF paths
        config: Config dict
        use_cache: Skip cached files
    
    Returns:
        Dict mapping filepath → markdown string (None for failures)
    """
    if config is None:
        config = load_config()
    
    token = _get_token(config)
    cache_dir = _get_cache_dir(config)
    
    # Separate cached vs uncached
    results = {}
    to_parse = []
    file_hashes = {}
    
    for fp in filepaths:
        if not os.path.exists(fp):
            logger.warning(f"File not found, skipping: {fp}")
            results[fp] = None
            continue
        
        fh = _file_hash(fp)
        file_hashes[fp] = fh
        cache_file = os.path.join(cache_dir, f"{fh}.md")
        
        if use_cache and os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                results[fp] = f.read()
            logger.info(f"Cache hit: {os.path.basename(fp)}")
        else:
            to_parse.append(fp)
    
    if not to_parse:
        logger.info("All files cached, no upload needed")
        return results
    
    # Request batch upload URLs (max 50)
    upload_files = [{"name": os.path.basename(fp)} for fp in to_parse[:50]]
    model_version = kwargs.get("model_version", DEFAULT_MODEL)
    language = kwargs.get("language", DEFAULT_LANGUAGE)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    payload = {
        "files": upload_files,
        "model_version": model_version,
        "enable_formula": kwargs.get("enable_formula", True),
        "enable_table": kwargs.get("enable_table", True),
        "language": language,
    }
    
    logger.info(f"Requesting batch upload for {len(upload_files)} files...")
    resp = requests.post(f"{BASE_URL}/api/v4/file-urls/batch",
                         headers=headers, json=payload, timeout=30)
    if resp.status_code != 200 or resp.json().get("code") != 0:
        logger.error(f"Batch upload URL request failed: {resp.text[:300]}")
        for fp in to_parse:
            results[fp] = None
        return results
    
    batch_id = resp.json()["data"]["batch_id"]
    upload_urls = resp.json()["data"]["file_urls"]
    
    # Upload all files
    for fp, url in zip(to_parse[:50], upload_urls):
        logger.info(f"Uploading {os.path.basename(fp)}...")
        with open(fp, "rb") as f:
            requests.put(url, data=f, timeout=120)
    
    # Poll for all results
    timeout = kwargs.get("timeout", POLL_TIMEOUT * len(to_parse))
    result = _poll_batch_result(batch_id, token, timeout=timeout)
    if result is None:
        for fp in to_parse:
            results[fp] = None
        return results
    
    # Download and cache each result
    extract_results = _poll_batch_result_all(batch_id, token, timeout=timeout)
    if extract_results is None:
        # Fallback: single result
        extract_results = [result]
    
    for fp, res in zip(to_parse, extract_results):
        if res is None or res.get("state") != "done":
            results[fp] = None
            continue
        zip_url = res.get("full_zip_url", "")
        md, _ = _download_and_extract_zip(zip_url, cache_dir)
        if md:
            fh = file_hashes.get(fp, _file_hash(fp))
            cache_file = os.path.join(cache_dir, f"{fh}.md")
            with open(cache_file, "w", encoding="utf-8") as f:
                f.write(md)
            results[fp] = md
    
    return results


def _poll_batch_result_all(batch_id, token, timeout=None):
    """Poll batch result, return list of all extract_result items."""
    timeout = timeout or POLL_TIMEOUT
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URL}/api/v4/extract-results/batch/{batch_id}"
    
    start = time.time()
    while time.time() - start < timeout:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code != 200:
            time.sleep(POLL_INTERVAL)
            continue
        
        data = resp.json().get("data", {})
        results = data.get("extract_result", [])
        if not results:
            time.sleep(POLL_INTERVAL)
            continue
        
        all_done = all(r.get("state") in ("done", "failed") for r in results)
        if all_done:
            return results
        
        states = [r.get("state", "?") for r in results]
        done_count = sum(1 for s in states if s == "done")
        logger.info(f"Batch progress: {done_count}/{len(states)} done")
        time.sleep(POLL_INTERVAL)
    
    return None


# ─── CLI ────────────────────────────────────────────────────────────

def main():
    """[DEPRECATED] Use ``lit parse`` instead. See ``lit --help``."""
    import warnings
    warnings.warn(
        "pdf_parser.py is deprecated. Use 'lit parse <pdf_path>' instead. See 'lit --help'.",
        DeprecationWarning, stacklevel=2
    )
    import argparse
    parser = argparse.ArgumentParser(description="Parse PDF via MinerU online API")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--output", "-o", help="Output markdown file path")
    parser.add_argument("--model", default="vlm", choices=["pipeline", "vlm"],
                        help="MinerU model version (default: vlm)")
    parser.add_argument("--language", default="en",
                        help="Document language (default: en)")
    parser.add_argument("--no-cache", action="store_true",
                        help="Bypass cache, force re-parse")
    parser.add_argument("--page-ranges", help="Page range, e.g. '1-10'")
    parser.add_argument("--config", help="Path to config.yaml")
    parser.add_argument("--debug", action="store_true")
    
    args = parser.parse_args()
    
    # Logging
    level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=level, format="[%(levelname)s] %(message)s")
    
    config = load_config(args.config)
    
    kwargs = {
        "model_version": args.model,
        "language": args.language,
    }
    if args.page_ranges:
        kwargs["page_ranges"] = args.page_ranges
    
    markdown = parse_pdf(
        args.pdf_path,
        config=config,
        use_cache=not args.no_cache,
        **kwargs,
    )
    
    if markdown is None:
        print("FAILED: PDF parsing failed", file=sys.stderr)
        sys.exit(1)
    
    # Output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"OK: {len(markdown)} chars → {args.output}")
    else:
        # Print to stdout (for piping)
        print(markdown)


if __name__ == "__main__":
    main()
