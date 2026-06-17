"""
lit/core/config.py — 配置加载（单例模式）

所有模块从此处加载配置，不再各自写 load_config()。
路径自动从 lit/ 包位置向上解析到 skill base 目录。
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml
from rich.console import Console

console = Console()

_cache: dict | None = None
_SKILL_BASE: Path | None = None


def _find_skill_base() -> Path:
    """Resolve the skill base directory: lit/ 的父目录."""
    return Path(__file__).resolve().parent.parent.parent


def skill_base() -> Path:
    """返回 skill base 目录（config.yaml 所在目录）。"""
    global _SKILL_BASE
    if _SKILL_BASE is None:
        _SKILL_BASE = _find_skill_base()
    return _SKILL_BASE


def load() -> dict:
    """加载 config.yaml。缓存，重复调用不重新读盘。缺文件则报错退出。"""
    global _cache
    if _cache is not None:
        return _cache

    config_path = skill_base() / "config.yaml"
    if not config_path.exists():
        console.print(f"[red]config.yaml not found at {config_path}[/red]")
        console.print(f"  Copy config.yaml.example → config.yaml and fill in credentials.")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        _cache = yaml.safe_load(f) or {}

    return _cache


def zotero() -> dict:
    """获取 zotero 配置段，含必填字段校验。

    Returns:
        已校验的 zotero 配置 dict（含 library_id, api_key, library_type 等）
    """
    cfg = load()
    z = cfg.get("zotero", {})
    for key in ("library_id", "api_key"):
        val = z.get(key, "")
        if not val or val.startswith("YOUR_"):
            console.print(f"[red]zotero.{key} not configured in config.yaml[/red]")
            sys.exit(1)
    return z


def people() -> dict:
    """获取 people 配置段（旧版），带默认值。

    向后兼容：新代码优先读 ``lit`` 段，回退到 ``people`` 段。
    """
    cfg = load()
    p = cfg.get("lit", {}) or cfg.get("people", {})
    defaults = {
        "parent_collection": "People",
        "exclude_types": ["Patent"],
        "scholar": {"page_delay": 3000, "max_show_more": 50, "min_delay": 5, "max_delay": 15},
        "digest_dir": str(skill_base() / "people" / "digests"),
    }
    for key, val in defaults.items():
        if key not in p:
            p[key] = val
    if "scholar" not in p:
        p["scholar"] = {}
    for key, val in defaults["scholar"].items():
        if key not in p["scholar"]:
            p["scholar"][key] = val
    return p


def storage_path() -> str:
    """获取 Zotero storage 路径。"""
    z = zotero()
    return z.get("storage_path", "")
