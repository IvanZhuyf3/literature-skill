# Paper Digest 工作流（单篇精读）

> 单篇论文深度精读笔记。与 scholar digest（全量、广度）互补，paper digest 专注深度。

## 前置流程

### 步骤 0（可选）：创建 People collection 并归入论文

`lit import` 不支持 `--collection` 参数，论文默认创建在根目录。如果要归入 `People/<作者名>` 文件夹：

```python
from lit.core.zotero import _client   # 注意是 _client()，不是 get_zotero_client
z = _client()

# 创建子 collection（People parent key = WI2ZXCM3）
resp = z.create_collections([{"name": "Author Name", "parentCollection": "WI2ZXCM3"}])
col_key = resp["successful"]["0"]["data"]["key"]

# import 后把条目移入
item = z.item("ITEMKEY")          # import 返回的 key
item["data"]["collections"] = [col_key]
z.update_item(item)
```

### 步骤 1：注册 + 下载 + 解析

```
lit import <DOI>                          # 确保 Zotero 有条目（返回 item key）
lit quick <DOI> → lit attach <DOI>        # 确保 PDF 已下载
lit parse <pdf> --item-key <key>          # PDF → 全文 Markdown
```

⚠ **`lit parse` 不输出 .md 路径到 stdout**。解析后需在 `cache/mineru/` 搜索输出文件——按 DOI 片段内容匹配：
```bash
grep -l "10.xxx/xxx" cache/mineru/*.md
```

### 步骤 2：深读全文 → 产出 paper digest

如果没有 PDF（下载失败），基于 abstract + CrossRef 元数据也能做，但 Block 3/4/5 会大打折扣，需在头部标注"⚠ 无全文，基于摘要"。

## 输出

路径：`<Obsidian vault>/research_digest/<last author>/`
文件名：`<first author> - <journal> - <year> - <完整标题>.md`

Last author = 大通讯作者（通常也是 PI）。

## Paper Digest 结构（6 个 Block）

### Block 1：文献信息卡

固定字段，从 Zotero/CrossRef 拉：

```markdown
- **标题**:
- **作者**: 全名（走 CrossRef，不用缩写，不脑补）
- **期刊**: 
- **年份**: 
- **DOI**: [10.xxx/xxx](https://doi.org/10.xxx/xxx)
- **文章类型**: research / review / letter / preprint
- **引用数**: (CrossRef)
- **PDF**: [本地文件](file:///C:/Users/Ivanz/Zotero/storage/XXXXXX/filename.pdf)
- **网页**: [出版商页面](https://doi.org/10.xxx/xxx)
```

本地 PDF 路径通过 `lit pdf <DOI>` 获取（返回 Zotero storage 里的实际文件路径）。转成 `file:///` 链接格式，Obsidian 可直接点击打开。

### Block 2：问题与动机

从 Introduction 提取，不是 abstract 转述：

- **具体问题**：这篇论文要解决什么？（一句话，具体到参数层面）
- **现有方法为什么不够**：指出 gap（分辨率？速度？特异性？灵敏度？）
- **核心贡献**：一句话

### Block 3：方法深拆

⚠ 最严格的 Block。所有细节必须从 Methods / Results / Figure captions 提取，不从 abstract 编。每条标注出处。

- **实验装置**：光源（波长、功率、脉冲宽度）、显微镜物镜（NA、放大率）、检测器（类型、积分时间）、扫描方式——能找到的硬件参数都要
- **核心原理**：数学公式（原文公式，不是文字转述）。如果是物理方法，写出关键物理方程
- **数据处理流程**：原始信号 → 最终图像/谱图的每一步变换
- **样品**：细胞系 / 组织类型 / 动物模型
- **创新点定位**：跟已有方法比，新在哪个具体环节

### Block 4：关键结果

挑 2-4 个核心 Figure（不是罗列所有图）：

- 每个 Figure：展示了什么 → 定量结论（具体数字：分辨率 XX nm，速度 XX fps，SNR 提升 XX 倍）
- 与 Block 2 对应：解决了当初提出的问题吗？

### Block 5：Agent Critique

⚠ 从第一性原理出发，分析方法的实际物理/化学本质，寻找论文没有自白的缺陷。

**不是**样本量不够、缺对照、统计检验缺位这些"大路货"参数——除非严重到影响结论成立。

**是**：
- 宣称的"新方法"在物理上是否真的新？（例：一个图像处理方法实质上是包装精美的锐化）
- 宣称的原理是否能带来声称的效果？（例：宣称超分辨但物理原理上无法突破衍射极限）
- 效果的提升归因是否正确？（例：SNR 提升是来自新原理还是单纯加大了功率/积分时间）
- 控制实验是否真正验证了核心 claim？（不是泛泛说"缺对照"，而是指出具体哪个对照缺失导致哪个 claim 无法成立）

如果论文方法扎实、没有发现根本性问题，明确写"未发现根本性方法缺陷"，不要硬编问题。

### Block 6：强关联引用

扫 Introduction（有时延伸到 Methods 开头），找被花额外篇幅讨论的引文——说明技术高度相关。

对每条强关联引用：
- **引文**：作者 + 年份 + [DOI 链接](https://doi.org/xxx)
- **关联**：这篇论文跟它的关系是什么？（在前人基础上改了什么 / 反驳了什么 / 组合了什么）

只放真正被详细讨论的（通常 2-5 条），不是 References 全量。

## 格式规范

### 标题层级（Obsidian 可读性）

Obsidian 中 h1/h2 渲染字体很大，长文里会显得突兀。Paper digest 标题层级：

| 层级 | `#` 数量 | 用途 | 示例 |
|------|----------|------|------|
| h1 | `#` | 论文标题，全文仅一次 | `# Super-resolution imaging...` |
| h2 | `##` | Block 标题（6个Block） | `## Block 3：方法深拆` |
| h3 | `###` | Block 内主要分段 | `### 实验装置` |
| h4 | `####` | 分段内子节 | `#### E-PEARL（电子吸收模式）` |
| h5 | `#####` | 最细粒度（偶尔用） | `##### 功率依赖测试` |

**规则**：文内所有小标题用 `###`～`#####`（h3-h5），不要用 `#` 或 `##`。Block 标题用 `##`。只有论文标题用 `#`。

### DOI 链接（禁止幻觉）

**所有 DOI 必须通过 CrossRef API 验证，禁止 LLM 生成或猜测 DOI。**

流程（Block 1 自身 DOI 和 Block 6 引用 DOI 都适用）：
1. 从论文全文/参考文献列表提取引文的**标题 + 第一作者 + 年份 + 期刊**
2. 用 CrossRef API 搜索：`https://api.crossref.org/works?query.bibliographic=<title>&rows=3`
3. 比对返回结果的标题、期刊、年份，确认匹配
4. 使用 CrossRef 返回的 DOI 构造链接
5. 如果 CrossRef 搜不到匹配项，标注 `[DOI 待查]`，**不要编一个看着像的**

**教训（2026-06-19）**：PEARL 论文 digest 的 Block 6 中，2/4 条引用的 DOI 是幻觉（`-27117-x` 应为 `-27362-w`，`nl504641n` 应为 `nl504640e`）。DOI 格式看起来合理但数字错误，只有查 CrossRef 才能发现。

## 质量约束

1. **方法细节只从全文提取**，不从 abstract 编。标注出处（"Methods §2.3" / "Fig. 2 caption"）
2. **定量数字必须来自原文**
3. **Critique 必须基于第一性原理**，不是套路化的"建议补充对照实验"
4. **作者全名走 CrossRef**，不用缩写，不脑补展开（曾将 Keith Man-Chung Wong 错写成 Kenneth）
5. **DOI 走 CrossRef 验证**，不猜测（详见上方"DOI 链接"规范）
6. **标题层级**：文内小标题用 `###`～`#####`，不用 `#`/`##`（详见上方"标题层级"规范）
7. **无全文时标注**：没有 PDF 的论文基于 abstract 做，Block 3/4/5 会受限，头部标"⚠ 无全文"
