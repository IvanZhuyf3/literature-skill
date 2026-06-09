# Literature Skill

学术文献一站式工具：**下载论文 PDF** + **添加到 Zotero**。

合并自 [Paper-at-Home](https://github.com/IvanZhuyf3/Literature_downloader_skill)（PDF 下载）和 [Zot](https://github.com/IvanZhuyf3/Zot_add)（Zotero 工作流）。

## 功能

### /download — 下载论文 PDF

通过 Playwright CDP 连接本地 Chromium 浏览器，利用已有的机构登录状态下载论文全文。

- 支持 23 家出版商（Nature、Science、Springer、Wiley、ACS、Elsevier 等）
- 支持单篇 / 批量 / DOI 下载
- 模拟人类行为（阅读延迟、鼠标移动、真实点击）

### /zot — Zotero 完整工作流

一站式：去重检查 → 元数据提取（citation meta tags + CrossRef API） → PDF 下载 → 创建 Zotero 条目 → 挂载 PDF。

- 自动从页面提取 DOI，通过 CrossRef 补全完整元数据
- 自动去重（DOI / URL / 标题匹配）
- PDF 下载失败也会先保存元数据

## 前置要求

- Windows
- Chromium 内核浏览器（Chrome / Edge / Brave 等）
- Python 3.8+
- Elsevier 论文额外需要 Foxit Reader

## 安装

```powershell
# 安装依赖（全局安装）
pip install -r requirements.txt

# 安装 Playwright 浏览器
playwright install chromium

# 或直接运行 setup.bat（一键安装）
setup.bat

# 配置 Zotero（如果要用 /zot 功能）
cp config.yaml.example config.yaml
# 编辑 config.yaml，填入 Zotero API key 和 library ID
```

## 使用方法

### 下载论文 PDF

```powershell
# 单篇下载
set PYTHONIOENCODING=utf-8 && python main.py "https://www.nature.com/articles/s41586-024-07386-0"

# 通过 DOI
set PYTHONIOENCODING=utf-8 && python main.py "10.1038/s41586-024-07386-0"

# 批量下载
set PYTHONIOENCODING=utf-8 && python main.py --input urls.txt

# 调试模式
set PYTHONIOENCODING=utf-8 && python main.py "URL" --debug
```

### 添加到 Zotero

```powershell
set PYTHONIOENCODING=utf-8 && python zot.py "https://www.nature.com/articles/s41586-023-06139-9"
```

输出：
```
Step 1/4: Extracting metadata from page...
  Page metadata: title=Transfer learning..., DOI=10.1038/s41586-023-06139-9
  CrossRef enriched: Nature 2023 v618

Step 2/4: Downloading PDF...
✓ PDF downloaded: ...\Transfer learning enables predictions in network biology.pdf

Step 3/4: Creating Zotero item...
✓ Zotero item created: XXXXXXXX (type: journalArticle)

Step 4/4: Attaching PDF...
✓ PDF attached: YYYYYYYY

ZOT_RESULT: zot_key=XXXXXXXX|att_key=YYYYYYYY|local_pdf=...|title=Transfer learning...
```

## 支持的出版商（23 家）

AAAS (Science) · ACS · AIP · Annual Reviews · APS · BMJ · eLife · Elsevier · Frontiers · IEEE · IOP · MDPI · Nature · Optica · PNAS · Royal Society · RSC · SPIE · Springer · Taylor & Francis · Wiley

## 项目结构

```
├── SKILL.md              # Skill 定义（agent 入口）
├── AGENTS.md             # 开发参考
├── main.py               # PDF 下载入口
├── zot.py                # Zotero 工作流入口
├── chromium_helper.py    # CDP 连接与浏览器管理
├── click_engine.py       # 模拟人类鼠标/键盘操作
├── download_monitor.py   # 下载进度监控
├── rate_limiter.py       # 速率限制
├── url_parser.py         # URL/DOI 解析，出版商识别
├── config.yaml           # 配置文件（gitignored）
├── config.yaml.example   # 配置模板
├── publisher/            # 出版商适配器（20+）
├── debug/                # 调试探测脚本
├── references/           # 架构文档
├── requirements.txt      # Python 依赖
├── setup.bat             # 一键安装
├── run.bat               # 快速启动
└── start_browser.bat     # 启动带调试端口的浏览器
```

## 配置

编辑 `config.yaml`：

- **Chrome**：浏览器路径、CDP 端口、用户数据目录
- **下载**：临时目录、超时时间
- **速率**：论文间延迟、阅读模拟时间、session 上限
- **Zotero**：API key、library ID、本地 storage 路径
- **调试**：自动截图
