# Legacy Architecture — 旧版入口参考

> 旧版入口（`main.py`, `zot.py`, `people.py` 等）已弃用但代码保留兼容。
> 新项目一律使用 `python -m lit <command>` 系列命令。
> 本文件供需要理解旧代码或做反向兼容调试时查阅。

## 旧版文件结构

| 文件 | 职责 |
|------|------|
| `main.py` | CLI 入口，单篇下载完整工作流编排 |
| `zot.py` | Zotero 完整工作流（去重 + 元数据 + 下载 + 添加 + 挂载） |
| `people.py` | 学者批量处理（抓取 Scholar Profile + 下载 + 消化报告） |
| `chromium_helper.py` | Chromium 启动/CDP 连接/暖场页面 |
| `click_engine.py` | 坐标转换 + pyautogui 人类式点击（备用） |
| `download_monitor.py` | `page.evaluate(fetch())` PDF 下载 + 目录监控 fallback |
| `rate_limiter.py` | 延迟控制（60-180s）、模拟阅读、session 限制 |
| `url_parser.py` | URL/DOI 解析、出版商自动识别 |
| `zotero_attach.py` | 旧版批量挂载 PDF 到 Zotero |
| `generate_qr.py` | 旧版 QR 码生成 |
| `ocr_citation.py` | 旧版图片 OCR 引用提取 |
| `pdf_parser.py` | 旧版 MinerU PDF 解析 |

## 旧版文件职责（完整）

| 文件 | 职责 |
|------|------|
| `main.py` | CLI 入口，完整工作流编排 |
| `chromium_helper.py` | Chromium 启动/CDP 连接/暖场页面 |
| `click_engine.py` | 坐标转换 + pyautogui 人类式点击（备用，当前未使用） |
| `download_monitor.py` | `page.evaluate(fetch())` PDF 下载（主方案） + 目录监控 fallback |
| `rate_limiter.py` | 延迟控制（60-180s）、模拟阅读、session 限制 |
| `url_parser.py` | URL/DOI 解析、出版商自动识别 |
| `publisher/base.py` | 适配器抽象基类 (PublisherAdapter) |
| `publisher/acs.py` | ACS Publications 适配器 |
| `publisher/optica.py` | Optica Publishing Group 适配器 |
| `publisher/aaas.py` | AAAS (Science) 适配器 |
| `publisher/npg.py` | Nature Publishing Group 适配器 |
| `publisher/springer.py` | Springer (link.springer.com) 适配器 |
| `publisher/aip.py` | AIP (Silverchair 平台) 适配器 |
| `publisher/elsevier.py` | Elsevier ScienceDirect 适配器 (Ctrl+P 打印下载) |
| `publisher/pnas.py` | PNAS 适配器 |
| `publisher/wiley.py` | Wiley Online Library 适配器 |
| `publisher/aps.py` | APS (Physical Review系列) 适配器 |
| `publisher/tandf.py` | Taylor & Francis 适配器 |
| `publisher/rsc.py` | RSC (Royal Society of Chemistry) 适配器 |
| `publisher/iop.py` | IOP (IOPscience) 适配器 |
| `publisher/annualreviews.py` | Annual Reviews 适配器 |
| `publisher/mdpi.py` | MDPI 适配器 |
| `publisher/frontiers.py` | Frontiers 适配器 |
| `publisher/elife.py` | eLife 适配器 |
| `publisher/royalsociety.py` | Royal Society 适配器 |
| `publisher/bmj.py` | BMJ 适配器 |
| `publisher/ieee.py` | IEEE Xplore 适配器 |
| `publisher/spie.py` | SPIE Digital Library 适配器 |
| `config.yaml` | 所有可调参数 |

## 旧版 main.py 下载流程

```
navigate_to_paper → check_access → get_paper_metadata → simulate_reading
  → find_download_url → [resolve_pdf_url 如果有] → navigate_back
  → [若 use_click_download: click + Ctrl+P 打印] → [否则: pre_click_delay → fetch() download]
  → save → rename → cleanup_tabs
```

**特殊路径：**
- `__click_download__`：Elsevier 返回此标记触发 click_download 流程（Ctrl+P 打印）

## 旧版构建/运行

```bat
:: 首次
setup.bat

:: 方式 A：手动启动 Chromium（推荐，有登录状态）
start_browser.bat         :: 启动 Chromium (端口 9222)
run.bat "DOI或URL"        :: 下载单篇（main.py 自动 CDP 连接）

:: 方式 B：让 main.py 自动启动（临时 profile，无登录状态）
run.bat --launch-browser "DOI或URL"

:: 批量下载
run.bat --input urls.txt
```

全部 global install，无 venv。

## 旧版入口命令

```bash
# 旧版入口仍可用，但会打印弃用警告
PYTHONIOENCODING=utf-8 python "main.py" "URL"           # 下载
PYTHONIOENCODING=utf-8 python "zot.py" "URL"            # Zotero
PYTHONIOENCODING=utf-8 python "people.py" "URL"         # 学者
PYTHONIOENCODING=utf-8 python "pdf_parser.py" "path"    # 解析
```

## 旧版 Key Gotchas

- `--config` argparse default 必须是 `None`（不是 `"config.yaml"`）。`load_config()` 用 `path or default_path` 做回退。
- Windows Hyper-V 可能保留端口 9222。本机 config.yaml 使用 `cdp_url: "http://127.0.0.1:19222"`。
- `launch_browser()` 中的调试端口从 config 的 `cdp_url` 解析。
- Optica 适配器有两种重定向链路，适配器两种都处理了。
- `zot.py` 的 `download_pdf()` 直接用 `SKILL_BASE / "main.py"`。
