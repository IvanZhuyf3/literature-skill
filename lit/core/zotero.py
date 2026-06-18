"""
lit/core/zotero.py — Zotero API 薄封装

所有 Zotero 操作收拢到此处。不包含下载逻辑。
无 cfg 参数传来传去——配置从 ``lit.core.config`` 单例读取。
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from pyzotero import zotero as zotero_mod
from rich.console import Console

from lit.core.config import zotero as get_zotero_cfg, storage_path as get_storage_path

console = Console()


# ── Client factory ──

def _client() -> zotero_mod.Zotero:
    """创建 pyzotero 客户端。"""
    zcfg = get_zotero_cfg()
    return zotero_mod.Zotero(
        zcfg["library_id"],
        zcfg.get("library_type", "user"),
        zcfg["api_key"],
    )


def _api_base() -> str:
    """Zotero API base URL for REST calls (attachment JSON POST)."""
    zcfg = get_zotero_cfg()
    return f"https://api.zotero.org/{zcfg.get('library_type', 'user')}s/{zcfg['library_id']}"


def _api_headers() -> dict[str, str]:
    return {
        "Zotero-API-Key": get_zotero_cfg()["api_key"],
        "Content-Type": "application/json",
    }


# ── DOI index (local cache) ──

import json as _json
import os as _os
import time as _time

from lit.core.config import skill_base as _skill_base

_INDEX_PATH = _skill_base() / "cache" / "doi_index.json"
_INDEX_MAX_AGE = 7 * 24 * 3600  # 7 days


def build_doi_index(force: bool = False) -> dict[str, str]:
    """Scan all Zotero items and build {doi_lower: item_key} index.

    Cached to cache/doi_index.json. Rebuilds if missing or stale (>7 days)
    unless force=True.

    Returns the doi→key dict.
    """
    if not force and _INDEX_PATH.exists():
        age = _time.time() - _INDEX_PATH.stat().st_mtime
        if age < _INDEX_MAX_AGE:
            with open(_INDEX_PATH, "r", encoding="utf-8") as f:
                data = _json.load(f)
            return data.get("dois", {})

    console.print("[dim]Building DOI index (one-time, ~60s for large libraries)...[/dim]")
    zot = _client()
    doi_map: dict[str, str] = {}
    start = 0
    batch_size = 100
    total = 0
    while True:
        items = zot.items(itemType="-attachment", limit=batch_size, start=start)
        if not items:
            break
        for item in items:
            d = item.get("data", {})
            doi = d.get("DOI", "").strip().lower()
            if doi:
                doi_map[doi] = item["key"]
        total += len(items)
        start += batch_size
        if len(items) < batch_size:
            break
        _time.sleep(0.3)

    _INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(_INDEX_PATH, "w", encoding="utf-8") as f:
        _json.dump({"dois": doi_map, "count": len(doi_map), "built_at": _time.time()}, f)
    console.print(f"[green]✓ DOI index:[/green] {len(doi_map)} entries from {total} items")
    return doi_map


def _load_doi_index() -> dict[str, str]:
    """Load DOI index from cache. Does NOT auto-rebuild if missing."""
    if _INDEX_PATH.exists():
        with open(_INDEX_PATH, "r", encoding="utf-8") as f:
            data = _json.load(f)
        return data.get("dois", {})
    return {}


# ── Collection operations ──

def find_or_create_collection(name: str, parent_name: str = "People") -> str:
    """Find or create a named collection under parent. Returns key."""
    zot = _client()
    all_cols = zot.collections()

    # Find parent
    parent_key = None
    for col in all_cols:
        if col["data"]["name"] == parent_name and not col["data"].get("parentCollection", False):
            parent_key = col["key"]
            break
    if not parent_key:
        resp = zot.create_collections([{"name": parent_name, "parentCollection": False}])
        parent_key = resp["successful"]["0"]["key"]

    # Find or create leaf
    for col in all_cols:
        if col["data"]["name"] == name and col["data"].get("parentCollection") == parent_key:
            return col["key"]

    resp = zot.create_collections([{"name": name, "parentCollection": parent_key}])
    key = resp["successful"]["0"]["key"]
    console.print(f"  Created collection: [bold]{parent_name}/{name}[/bold] ({key})")
    return key


def find_collection(name: str, parent_name: str = "People") -> str | None:
    """Find an existing collection. Returns key or None if not found."""
    zot = _client()
    all_cols = zot.collections()

    parent_key = None
    for col in all_cols:
        if col["data"]["name"] == parent_name and not col["data"].get("parentCollection", False):
            parent_key = col["key"]
            break
    if not parent_key:
        return None

    for col in all_cols:
        if col["data"]["name"] == name and col["data"].get("parentCollection") == parent_key:
            return col["key"]
    return None


def list_collections() -> list[dict]:
    """List all collections with name + key + parent."""
    zot = _client()
    return [
        {"key": c["key"], "name": c["data"]["name"], "parent": c["data"].get("parentCollection", "")}
        for c in zot.collections()
    ]


# ── Item operations ──

def find_by_doi(doi: str) -> str | None:
    """Search by DOI, return item key or None. Skips attachments and notes.

    Uses local DOI index (cache/doi_index.json). Falls back to API q-search
    if index is missing (less reliable — Zotero API q does not index DOI field).
    """
    if not doi:
        return None
    doi = doi.lower().strip()

    # Try local index first (fast, reliable)
    index = _load_doi_index()
    if index:
        return index.get(doi)

    # Fallback: API q-search (unreliable for DOI, but better than nothing)
    zot = _client()
    try:
        results = zot.items(q=doi, limit=10)
    except Exception:
        return None
    for item in results:
        d = item.get("data", {})
        if d.get("itemType") in ("attachment", "note"):
            continue
        if d.get("DOI", "").lower().strip() == doi:
            return item["key"]
    return None


def find_by_url(url: str) -> str | None:
    """Search by URL."""
    if not url:
        return None
    zot = _client()
    try:
        results = zot.items(q=url.split("?")[0][-60:], limit=10)
    except Exception:
        return None
    for item in results:
        d = item.get("data", {})
        if d.get("itemType") in ("attachment", "note"):
            continue
        if d.get("url", "").strip() == url.strip():
            return item["key"]
    return None


def check_duplicate(doi: str = "", title: str = "", url: str = "") -> tuple[str | None, str | None]:
    """Comprehensive dedup check by DOI, URL, or title.

    Returns (item_key, match_reason) if found, (None, None) otherwise.
    """
    zot = _client()

    queries = []
    if title:
        queries.append(("title", title[:60]))
    if doi:
        queries.append(("DOI", doi))
    if url:
        queries.append(("URL", url.split("?")[0][-60:]))

    for label, query in queries:
        try:
            results = zot.items(q=query, limit=25)
        except Exception:
            continue
        for item in results:
            d = item.get("data", {})
            itype = d.get("itemType", "")
            item_doi = d.get("DOI", "").lower().strip()
            item_title = d.get("title", "").strip()
            item_url = d.get("url", "").strip()

            if doi and item_doi == doi and itype not in ("attachment", "note"):
                return d["key"], "DOI"
            if url and item_url == url and itype not in ("attachment", "note"):
                return d["key"], "URL"
            if title and item_title and item_title.lower() == title.lower() and itype not in ("attachment", "note"):
                return d["key"], "title"
            if itype == "attachment" and title and item_title:
                if item_title.lower() == title.lower():
                    parent = d.get("parentItem", "")
                    if parent:
                        return parent, "title"
    return None, None


def create_item(meta: dict) -> str:
    """Create a Zotero journal article item from metadata dict.

    Args:
        meta: dict with keys: DOI, title, url, journal (publicationTitle),
              year (date), volume, issue, pages, ISSN, abstract, publisher, authors (list[str])

    Returns:
        Item key.
    """
    zot = _client()
    doi = meta.get("DOI", "")
    has_full_meta = bool(meta.get("title") and meta.get("journal"))
    item_type = "journalArticle"

    template = zot.item_template(item_type)
    template["title"] = meta.get("title", meta.get("url", ""))
    template["url"] = meta.get("url", "")

    if doi:
        template["DOI"] = doi
    if meta.get("journal"):
        template["publicationTitle"] = meta["journal"]
    if meta.get("year"):
        template["date"] = meta["year"]
    if meta.get("volume"):
        template["volume"] = meta["volume"]
    if meta.get("issue"):
        template["issue"] = meta["issue"]
    if meta.get("pages"):
        template["pages"] = meta["pages"]
    if meta.get("ISSN"):
        template["ISSN"] = meta["ISSN"]
    if meta.get("abstract"):
        template["abstractNote"] = meta["abstract"]
    if meta.get("publisher"):
        template["publisher"] = meta["publisher"]

    # Authors → creators
    authors = meta.get("authors", [])
    if authors:
        template["creators"] = []
        for name in authors:
            name = name.strip()
            if not name or name == "...":
                continue
            parts = name.rsplit(" ", 1)
            creator = {"creatorType": "author"}
            if len(parts) == 2:
                creator["firstName"] = parts[0]
                creator["lastName"] = parts[1]
            else:
                creator["lastName"] = name
            template["creators"].append(creator)

    resp = zot.create_items([template])
    return _parse_create_response(resp)


def _parse_create_response(resp: dict) -> str:
    """Extract item key from pyzotero create_items response."""
    if resp.get("successful") and "0" in resp["successful"]:
        return str(resp["successful"]["0"]["key"])
    failed = resp.get("failed", {})
    if failed:
        msg = failed.get("0", {}).get("message", "Unknown API error")
        console.print(f"[red]Zotero API error:[/red] {msg}")
    raise RuntimeError(f"Unexpected Zotero API response: {resp}")


def get_children(item_key: str) -> list[dict]:
    """Get all child items (attachments, notes) for an item."""
    zot = _client()
    try:
        return zot.children(item_key)
    except Exception:
        return []


def has_pdf_attachment(item_key: str) -> bool:
    """Check if item already has a PDF attachment."""
    children = get_children(item_key)
    return any(
        c.get("data", {}).get("contentType") == "application/pdf"
        for c in children
    )


def resolve_local_pdf(doi: str) -> str | None:
    """按 DOI 精确查找本地 Zotero 存储的 PDF 文件路径。

    流程: find_by_doi → get_children → 拼 storage/{att_key}/ → 验证文件存在。
    不信任 Zotero 附件记录，必须 os.path.isfile 验证磁盘上真有 PDF。
    首次使用自动构建 DOI 索引（~60s），后续读缓存（秒级）。

    Returns:
        PDF 绝对路径 if found, None otherwise.
    """
    import os

    doi = doi.lower().strip()
    item_key = find_by_doi(doi)

    # If no hit and no index cache, build it then retry
    if not item_key and not _INDEX_PATH.exists():
        build_doi_index()
        item_key = find_by_doi(doi)

    if not item_key:
        return None

    children = get_children(item_key)
    storage = get_storage_path()
    if not storage:
        return None

    for child in children:
        cd = child.get("data", {})
        if cd.get("contentType") != "application/pdf":
            continue
        att_key = child["key"]
        dir_path = os.path.join(storage, att_key)
        if not os.path.isdir(dir_path):
            continue
        pdfs = [f for f in os.listdir(dir_path) if f.lower().endswith(".pdf")]
        if pdfs:
            return os.path.join(dir_path, pdfs[0])

    return None


def assign_to_collection(item_key: str, collection_key: str):
    """Assign item to a collection. Idempotent — skips if already assigned."""
    zot = _client()
    item = zot.item(item_key)
    collections = item["data"].get("collections", [])
    if collection_key not in collections:
        collections.append(collection_key)
        item["data"]["collections"] = collections
        zot.update_item(item)


def collection_items(collection_key: str) -> list[dict]:
    """Get ALL items in a collection (incl. children), with pagination.

    Returns list of pyzotero item dicts (both parent items and their children).
    """
    zot = _client()
    all_items: list[dict] = []
    start = 0
    while True:
        batch = zot.collection_items(collection_key, limit=100, start=start)
        if not batch:
            break
        all_items.extend(batch)
        start += 100
        if len(batch) < 100:
            break
    return all_items


def collection_items_top(collection_key: str) -> list[dict]:
    """Get top-level items only (no children), with pagination."""
    zot = _client()
    all_items: list[dict] = []
    start = 0
    while True:
        batch = zot.collection_items_top(collection_key, limit=100, start=start)
        if not batch:
            break
        all_items.extend(batch)
        start += 100
        if len(batch) < 100:
            break
    return all_items


def fetch_item(item_key: str) -> dict | None:
    """Fetch a single Zotero item by key.

    Returns the full item dict (including ``data`` sub-dict with title,
    DOI, creators, date, etc.), or ``None`` if not found.
    """
    zot = _client()
    try:
        item = zot.item(item_key)
        return item
    except Exception:
        logger.warning("fetch_item: item %s not found", item_key)
        return None


def item_to_meta(item: dict) -> dict:
    """Extract a CrossRef-style metadata dict from a Zotero item dict.

    Fields: DOI, title, authors (list), journal, year, volume, issue,
            pages, ISSN, publisher, url.
    """
    data = item.get("data", item)
    meta: dict = {}

    meta["DOI"] = data.get("DOI", "")

    title = data.get("title", "")
    # Zotero sometimes stores shortTitle separately
    if not title:
        title = data.get("shortTitle", "")
    meta["title"] = title

    # Journal name: depends on item type
    itype = data.get("itemType", "")
    if itype == "conferencePaper":
        meta["journal"] = data.get("proceedingsTitle", data.get("conferenceName", ""))
    elif itype == "thesis":
        meta["journal"] = data.get("university", data.get("publisher", ""))
    else:
        meta["journal"] = data.get("publicationTitle", "") or data.get("publisher", "")

    meta["publisher"] = data.get("publisher", "")

    # Creators → authors
    creators = data.get("creators", [])
    authors: list[str] = []
    for c in creators:
        first = (c.get("firstName") or c.get("name", "")).strip()
        last = (c.get("lastName") or "").strip()
        if last and first:
            authors.append(f"{first} {last}")
        elif last:
            authors.append(last)
        elif first:
            authors.append(first)
    meta["authors"] = authors

    # Date → year
    date_str = data.get("date", "")
    if date_str:
        import re as _re
        m = _re.search(r"(\d{4})", date_str)
        if m:
            meta["year"] = m.group(1)

    meta["volume"] = data.get("volume", "")
    meta["issue"] = data.get("issue", "")
    meta["pages"] = data.get("pages", "")
    meta["ISSN"] = data.get("ISSN", "")
    meta["url"] = data.get("url", "")

    return meta


def delete_item(item_key: str):
    """Delete an item by key. Fetches the item first to get version info."""
    zot = _client()
    item = zot.item(item_key)
    zot.delete_item(item)


# ── Attachment operations ──

def attach_pdf(item_key: str, pdf_path: Path) -> str:
    """Attach PDF to a Zotero item.

    Sync method from config:
      - ``webdav`` (default/recommended): JSON API creates attachment entry,
        PDF copied to local storage dir. WebDAV sync handles the upload.
      - ``cloud``: Multipart upload via pyzotero (consumes Zotero storage quota).
      - Falls back cloud→webdav on 413 quota error.

    Args:
        item_key: Parent item key.
        pdf_path: Path to the PDF file.

    Returns:
        Attachment item key.
    """
    from lit.core.config import load as get_config
    cfg = get_config()
    sync = cfg.get("zotero", {}).get("sync_method", "webdav")

    if sync == "webdav":
        return _attach_webdav(item_key, pdf_path)
    else:
        try:
            return _attach_cloud(item_key, pdf_path)
        except Exception as e:
            err = str(e)
            if "413" in err or "quota" in err.lower():
                console.print(f"  [yellow]⚠ Cloud upload failed (quota). Falling back to WebDAV...[/yellow]")
                return _attach_webdav(item_key, pdf_path)
            raise


def _attach_webdav(item_key: str, pdf_path: Path) -> str:
    """WebDAV mode: JSON API creates attachment entry, copy PDF to local storage.

    No file upload to Zotero cloud. File goes to ``{storage_path}/{att_key}/{filename}``.
    """
    import shutil
    import requests as req

    import hashlib
    from datetime import datetime, timezone

    filename = pdf_path.name
    # Compute md5 and mtime for Zotero to locate the file
    md5_hash = hashlib.md5()
    with open(pdf_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            md5_hash.update(chunk)
    mtime_ts = int(pdf_path.stat().st_mtime * 1000)  # Zotero expects milliseconds

    payload = [{
        "itemType": "attachment",
        "linkMode": "imported_file",
        "contentType": "application/pdf",
        "title": filename,
        "filename": filename,
        "md5": md5_hash.hexdigest(),
        "mtime": mtime_ts,
        "parentItem": item_key,
    }]

    resp = req.post(f"{_api_base()}/items", headers=_api_headers(), json=payload)
    if resp.status_code != 200:
        raise RuntimeError(f"Attachment creation failed: HTTP {resp.status_code} - {resp.text[:200]}")

    result = resp.json()
    if result.get("failed"):
        first_key = next(iter(result["failed"]))
        msg = result["failed"][first_key].get("message", "Unknown")
        raise RuntimeError(f"Attachment creation failed: {msg}")

    first_success = next(iter(result["successful"]))
    att_key = result["successful"][first_success]["data"]["key"]

    # Copy PDF to local Zotero storage
    storage = get_storage_path()
    if storage:
        dest_dir = Path(storage) / att_key
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(pdf_path), str(dest_dir / filename))
        console.print(f"  [green]✓ PDF attached (WebDAV):[/green] {att_key} (local: {dest_dir / filename})")
    else:
        console.print(f"  [yellow]⚠ No zotero.storage_path set, file at: {pdf_path}[/yellow]")

    return att_key


def _attach_cloud(item_key: str, pdf_path: Path) -> str:
    """Cloud mode: upload via pyzotero multipart (consumes storage quota)."""
    zot = _client()
    resp = zot.attachment_simple([str(pdf_path)], parentid=item_key)

    if resp.get("success"):
        att_key = str(resp["success"][0]["key"])
    elif resp.get("unchanged"):
        att_key = str(resp["unchanged"][0]["key"])
    elif resp.get("failure"):
        msg = resp["failure"][0].get("message", "Upload failed")
        raise RuntimeError(f"Attachment upload failed: {msg}")
    else:
        raise RuntimeError(f"Unexpected attachment response: {resp}")

    # Also copy to local storage as fallback
    import shutil
    storage = get_storage_path()
    if storage:
        dest_dir = Path(storage) / att_key
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(pdf_path), str(dest_dir / pdf_path.name))
        console.print(f"  [green]✓ PDF attached:[/green] {att_key} (local: {dest_dir / pdf_path.name})")
    else:
        console.print(f"  [green]✓ PDF uploaded:[/green] {att_key}")

    return att_key


