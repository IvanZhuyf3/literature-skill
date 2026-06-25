# DeepSeek Vision Integration

literature-skill 的图片引用提取（Step 5）依赖 DeepSeek Vision API 服务。

## 服务架构

```
图片 → ocr_citation.py → DeepSeek Vision API (localhost:3000) → CrossRef API → DOI
```

## DeepSeekWeb2API 服务

- **位置**: `deepseek_vision` skill 目录下的 `DeepSeekWeb2API/` 子目录
- **API 端点**: `http://127.0.0.1:3000/v1/chat/completions`
- **API Key**: `sk-local`
- **浏览器**: Edge (`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`)
- **配置文件**: `DeepSeekWeb2API/config.json`（浏览器路径、端口等）

### 启动检查

```bash
curl.exe -s http://127.0.0.1:3000/health
# 期望返回: {"ok":true,"queue":0}
```

### 如果服务未运行

加载 `deepseek_vision` skill，按其 SKILL.md 的启动流程操作。核心步骤：

```bash
cd <deepseek_vision_skill_base>/DeepSeekWeb2API
node src/index.js   # 后台启动
```

等日志输出 `DeepSeekWeb2API started` 后可用。首次请求可能需要 30-60 秒（浏览器启动 + 页面加载）。

### 如果启动失败

- **端口占用** (EADDRINUSE): 找到占用 3000 端口的进程并杀掉
- **浏览器路径错误**: 检查 config.json 的 `browser.executablePath` 是否指向 Edge
- **Cookie 过期**: 需要前台启动 `node src/index.js --login`，在弹出的 Edge 中登录 DeepSeek，登录完关掉后重新后台启动

## ocr_citation.py 要点

1. 调 DeepSeek Vision 时要求输出 JSON 格式的引用列表
2. 如果 OCR 没返回结构化 JSON（常见），fallback 用原始 OCR 文本去 CrossRef 搜索
3. CrossRef 匹配精度：当 OCR 提供的 title 为空时，可能匹配到错误论文。遇到可疑结果时用 OCR 原文中的作者名+关键词重新搜索
4. 输出 `CITATION:` 行（stderr）供 agent 解析，`--json` 标志控制 stdout 格式

## 已知局限

- DeepSeek Vision OCR 读取的 DOI 不可信，必须 CrossRef 二次确认
- PPT 照片如果模糊或角度歪斜，OCR 质量会下降
- DeepSeekWeb2API 不是 headless 的——需要 Edge GUI，用户操作其他窗口时可能抢不到 focus 导致发送失败
- 首次调用冷启动较慢（~60s），后续调用较快（~15-30s）
