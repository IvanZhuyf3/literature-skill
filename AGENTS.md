# Literature Skill — 开发环境入口

> 本文件供 OpenCode / Claude Code 开发时使用。打包为 skill 后，agent 读 `SKILL.md` 入口。

## 文档导航

| 文件 | 什么时候看 |
|------|-----------|
| `SKILL.md` | 用法、两个功能入口、故障排查 |
| `references/maintain.md` | 添加/修复 publisher 时的流程模板 |
| `references/architecture.md` | 代码架构、核心机制、适配器详解 |

## 两个功能入口

| 入口 | 功能 | 调用方式 |
|------|------|---------|
| `main.py` | 下载论文 PDF | `python main.py "URL"` |
| `zot.py` | Zotero 完整工作流（去重 + 元数据 + 下载 + 添加 + 挂载） | `python zot.py "URL"` |

`zot.py` 内部调用 `main.py`（同目录）下载 PDF，然后通过 Zotero API 添加条目和挂载附件。

## 快速命令

```bash
# 下载论文
set PYTHONIOENCODING=utf-8 && python main.py "URL" --no-warmup --debug

# 批量下载
set PYTHONIOENCODING=utf-8 && python main.py --input urls.txt --debug

# Zotero 工作流
set PYTHONIOENCODING=utf-8 && python zot.py "URL"
```

## 开发约定

- 新建 publisher 适配器后，更新 `references/architecture.md` 和 `SKILL.md`
- 所有 Python 脚本前缀 `PYTHONIOENCODING=utf-8`（Windows GBK）
- 全局安装依赖，不建 venv
- config.yaml 同时包含 Chrome/Zotero/下载/速率/调试配置

## Key Gotchas

- `--config` argparse default 必须是 `None`（不是 `"config.yaml"`）。`load_config()` 用 `path or default_path` 做回退。
- Windows Hyper-V 可能保留端口 9222。本机 config.yaml 使用 `cdp_url: "http://127.0.0.1:19222"`。
- `launch_browser()` 中的调试端口从 config 的 `cdp_url` 解析。
- Optica 适配器有两种重定向链路，适配器两种都处理了。
- `zot.py` 的 `download_pdf()` 现在直接用 `SKILL_BASE / "main.py"`，不再依赖外部 paper_at_home 路径。
