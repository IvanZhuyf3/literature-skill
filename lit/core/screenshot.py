"""
lit/core/screenshot.py — 调试截图工具

在下载流程的失败点自动保存页面截图，供后续 Vision 分析。

使用方式:
    from lit.core.screenshot import save_screenshot
    filepath = save_screenshot(page, "navigate_failed", doi="10.1002/anie.1518521")

截图默认保存到 debug/screenshots/<timestamp>_<doi>_<stage>.png。
成功时静默，失败时 log warning。
"""

from __future__ import annotations

import logging
import os
import re
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

# 默认截图目录（相对于 skill base）
_DEFAULT_DIR = Path(__file__).resolve().parent.parent.parent / "debug" / "screenshots"


def save_screenshot(
    page,
    stage: str,
    doi: str = "",
    output_dir: str | Path | None = None,
) -> Path | None:
    """保存当前页面的调试截图。

    Parameters
    ----------
    page : playwright.async_api.Page
        要截图的 Playwright Page 对象。
    stage : str
        截图时的阶段标签，如 ``"navigate_failed"``, ``"access_denied"``。
    doi : str, optional
        论文 DOI，用于文件名标识。传入完整 DOI 会自动提取紧凑片段。
    output_dir : str | Path, optional
        截图输出目录。默认 ``<skill_base>/debug/screenshots/``。

    Returns
    -------
    Path | None
        截图文件的 Path，失败时返回 None。
    """
    if output_dir is None:
        output_dir = _DEFAULT_DIR
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # 构造文件名：timestamp_doi_stage.png
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    doi_slug = _slugify_doi(doi) if doi else "unknown"
    safe_stage = re.sub(r"[^\w\-]+", "_", stage).strip("_")
    filename = f"{ts}_{doi_slug}_{safe_stage}.png"
    filepath = output_dir / filename

    try:
        page.screenshot(path=str(filepath), full_page=False)
        logger.debug("Screenshot saved: %s", filepath)
        return filepath
    except Exception as exc:
        logger.warning("Screenshot failed at stage '%s': %s", stage, exc)
        return None


def _slugify_doi(doi: str) -> str:
    """从 DOI 中提取紧凑的文件名安全片段。

    Examples
    --------
    "10.1002/anie.1518521"  →  "10.1002_anie.1518521"
    "10.1038/s41586-024-..." →  "10.1038_s41586-024"
    """
    slug = doi.strip().replace("/", "_")
    # 截断过长 slug，保留前 60 字符
    if len(slug) > 60:
        slug = slug[:60]
    slug = re.sub(r"[^\w\.\-]", "_", slug)
    return slug
