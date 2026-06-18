"""
debug/debug-vision.py — 用 DeepSeek Vision 分析下载流程截图

用途:
    当 lit download 失败时，引擎会自动在 debug/screenshots/ 保存截图。
    此脚本读取这些截图，调用 DeepSeek Vision API 分析页面内容，
    帮助确定失败类型和修复方向。

使用方式:
    # 分析单张截图
    python debug/debug-vision.py debug/screenshots/20260617_091500_some_doi_navigate_failed.png

    # 批量分析整个目录
    python debug/debug-vision.py debug/screenshots/

    # 指定 Vision API 地址（默认 http://127.0.0.1:3000）
    python debug/debug-vision.py debug/screenshots/ --api-url http://localhost:3000

输出: 每张截图的分析表:
    文件名 | 页面类型 | PDF 可用性 | 错误信息 | 修复建议
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from pathlib import Path

import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# ── 默认配置 ──────────────────────────────────────────────────────
DEFAULT_API_URL = "http://127.0.0.1:3000"
DEFAULT_MODEL = "deepseek-vision"
DEFAULT_API_KEY = "sk-local"  # DeepSeek Web2API 本地代理


def encode_image(image_path: str) -> str:
    """读取图片并返回 base64 编码字符串。"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


DIAGNOSTIC_PROMPT = """You are debugging a failed academic paper download. Analyze this screenshot of the publisher's web page and answer:

1. 页面类型 (Page type): What kind of page is this? Choose one:
    - PAYWALL / SUBSCRIPTION REQUIRED — login or purchase prompt visible
    - PDF VIEWER — the PDF is already displayed in browser
    - ARTICLE PAGE — standard HTML article with abstract and references
    - ERROR PAGE — 404, 403, 500, or other error code
    - CAPTCHA / BOT DETECTION — unusual verification challenge
    - LOGIN PAGE — institutional or personal login form
    - INTERSTITIAL / REDIRECT — intermediate redirect or loading screen
    - EMPTY / BROKEN — white page, no content, or JavaScript error
    - OTHER (describe briefly)

2. PDF 可用性 (PDF availability): Is there a visible PDF download link or button? Look for:
    - "Download PDF", "View PDF", "PDF" links/buttons
    - citation_pdf_url meta tag (check page source if visible)
    - PDF viewer embed/iframe
    - Any link containing "/pdf/" or "?pdf" or "download=true"
    State: YES / NO / UNCLEAR

3. 错误信息 (Error message): Copy any visible error message verbatim. If none, say "None visible".

4. 修复建议 (Fix suggestion): Based on the page state, what should happen next?
    - If PAYWALL: need institutional login / proxy
    - If PDF VIEWER: need __click_download__ flow
    - If ARTICLE: find_download_url() selector needs update
    - If CAPTCHA: human intervention required
    - If ERROR: check URL / publisher access
    - If UNKNOWN: suggest CDP probe script for this page

Return your analysis as a JSON object with exactly these keys:
{"page_type": "...", "pdf_available": "...", "error_message": "...", "fix_suggestion": "..."}"""


def analyze_screenshot(
    image_path: str,
    api_url: str = DEFAULT_API_URL,
    api_key: str = DEFAULT_API_KEY,
    model: str = DEFAULT_MODEL,
) -> dict | None:
    """调用 DeepSeek Vision 分析一张截图，返回结构化诊断。

    Returns
    -------
    dict with keys: page_type, pdf_available, error_message, fix_suggestion
    None on failure.
    """
    endpoint = f"{api_url.rstrip('/')}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    base64_image = encode_image(image_path)
    data_url = f"data:image/png;base64,{base64_image}"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": DIAGNOSTIC_PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {"url": data_url},
                    },
                ],
            }
        ],
        "temperature": 0.1,
        "max_tokens": 512,
    }

    try:
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        raw = data["choices"][0]["message"]["content"]

        # 尝试解析 JSON 响应
        # 模型可能返回 ```json ... ``` 包围的代码块
        json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group(1))
        else:
            parsed = json.loads(raw)

        return {
            "page_type": parsed.get("page_type", "UNKNOWN"),
            "pdf_available": parsed.get("pdf_available", "UNKNOWN"),
            "error_message": parsed.get("error_message", "None visible"),
            "fix_suggestion": parsed.get("fix_suggestion", "N/A"),
        }
    except Exception as exc:
        console.print(f"[red]Vision analysis failed for {image_path}: {exc}[/red]")
        return None


def _extract_doi(filename: str) -> str:
    """从截图文件名中提取 DOI 片段。文件名格式: <ts>_<doi>_<stage>.png"""
    parts = filename.split("_", 2)
    if len(parts) >= 2:
        return parts[1]
    return "unknown"


def _extract_stage(filename: str) -> str:
    """从截图文件名中提取失败阶段。"""
    base = filename.replace(".png", "")
    parts = base.split("_")
    if len(parts) >= 3:
        return parts[-1]  # 最后一段是 stage
    return "unknown"


def main():
    parser = argparse.ArgumentParser(
        description="用 DeepSeek Vision 分析下载失败截图",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python debug/debug-vision.py debug/screenshots/20260617_091500_navigate_failed.png
  python debug/debug-vision.py debug/screenshots/ --api-url http://localhost:3000
        """,
    )
    parser.add_argument("target", help="截图文件路径 或 截图目录路径")
    parser.add_argument(
        "--api-url",
        default=DEFAULT_API_URL,
        help=f"Vision API 地址 (默认: {DEFAULT_API_URL})",
    )
    parser.add_argument(
        "--api-key",
        default=DEFAULT_API_KEY,
        help="API Key (默认: 从 config 读取)",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Vision 模型 (默认: {DEFAULT_MODEL})",
    )
    args = parser.parse_args()

    target = Path(args.target)
    if target.is_file():
        screenshots = [target]
    elif target.is_dir():
        screenshots = sorted(
            [f for f in target.glob("*.png") if f.is_file()],
            key=lambda p: p.name,
        )
        if not screenshots:
            console.print(f"[yellow]目录下没有 PNG 截图: {target}[/yellow]")
            return
    else:
        console.print(f"[red]路径不存在: {target}[/red]")
        sys.exit(1)

    console.print(
        Panel(
            f"分析 {len(screenshots)} 张截图...\n"
            f"API: {args.api_url}  模型: {args.model}",
            title="🔍 Debug Vision Analysis",
        )
    )

    # 建结果表
    table = Table(title="截图分析结果")
    table.add_column("File", style="dim", no_wrap=True)
    table.add_column("Page Type", style="cyan")
    table.add_column("PDF Available", style="green")
    table.add_column("Error", style="red", max_width=50)
    table.add_column("Fix", style="yellow", max_width=40)

    for shot in screenshots:
        console.print(f"[dim]Analyzing: {shot.name}...[/dim]")
        result = analyze_screenshot(
            str(shot),
            api_url=args.api_url,
            api_key=args.api_key,
            model=args.model,
        )
        if result:
            table.add_row(
                shot.name,
                result["page_type"],
                result["pdf_available"],
                result["error_message"][:50],
                result["fix_suggestion"][:40],
            )
        else:
            table.add_row(shot.name, "ERROR", "-", "Analysis failed", "-")

    console.print()
    console.print(table)

    # 汇总建议
    fix_types: dict[str, int] = {}
    for shot in screenshots:
        result = analyze_screenshot(
            str(shot),
            api_url=args.api_url,
            api_key=args.api_key,
            model=args.model,
        )
        if result:
            fix = result["fix_suggestion"]
            # 取第一行作为分类
            category = fix.split(".")[0].strip() if fix else "Unknown"
            fix_types[category] = fix_types.get(category, 0) + 1

    if fix_types:
        console.print()
        console.print("[bold]问题分布:[/bold]")
        for cat, count in sorted(fix_types.items(), key=lambda x: -x[1]):
            console.print(f"  {cat}: {count} 张截图")


if __name__ == "__main__":
    main()
