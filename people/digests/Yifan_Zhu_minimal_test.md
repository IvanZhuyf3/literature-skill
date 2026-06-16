# 文献消化 — 最小量测试

> 测试日期: 2026-06-15
> 测试链路: Scholar 抓取 → DOI 匹配 → PDF 下载 → Zotero 归档 → 文献解读

---

## 测试论文

| 字段 | 内容 |
|------|------|
| 标题 | Contrasted photochromic and luminescent properties in dinuclear Pt(II) complexes linked through a central dithienylethene unit |
| 期刊 | Chemical Communications (2016) |
| DOI | 10.1039/c6cc03431d |
| 引用 | 25 |
| Zotero Key | HTK532AW |
| PDF 路径 | `C:\Users\Ivanz\Zotero\storage\VRBDQH87\...pdf` (1.7 MB) |

## 论文精读 (Block 4)

### 解决的问题
如何在一片分子中同时实现**可切换发光**和**可切换光致变色**两种功能，并探索 Pt(II)···Pt(II) 相互作用对这两种光物理性质的调控。

### 核心创新
- 设计合成了一类**双核 Pt(II)-二噻吩乙烯 (DTE)** 复合物，将光致变色单元 (DTE) 与发光单元 (Pt(II)配合物) 通过 π-共轭桥连接
- 发现 DTE 的开环/闭环光异构化可**可逆地调控 Pt(II)···Pt(II) 相互作用**，进而切换发光颜色（~520 nm → ~650 nm）
- 两个异构体的发光特性截然不同：开环态发射绿光（单体激发态），闭环态发射红光（金属-金属电荷转移，MMLCT）

### 方法细节
- 合成路线：Sonogashira 偶联构建双核 Pt(II) 配合物
- 表征：UV-Vis 吸收光谱、稳态/时间分辨发光光谱、X 射线单晶衍射
- 光致变色切换：254 nm UV → 闭环，>500 nm 可见光 → 开环

### 与 Yifan 其他论文的关联
- **光声/光热成像**（2020+）：本文研究的 Pt(II) 配合物的光物理性质（非辐射衰减通道）直接关联光声成像的机理理解
- **光致变色**方向（2018-2021）：Rhodol 类探针、Au(III)-indolizine 等系列工作共享"光调控发光"的设计思路
- **光动力学治疗**（2021, Matter）：本文 DTE 的可逆光开关能力 → 光控释放/光敏化概念延伸

### 影响
- 被引 25 次，为该学者第 8 高引论文
- 为后续金属-配体电荷转移 (MLCT) 相关的光声/光热成像研究提供了基础物理化学理解
- 首次展示了 Pt(II)-DTE 体系的光控发光切换

---

## 测试结论

| 测试项 | 结果 | 备注 |
|--------|------|------|
| Phase 1: Scholar 抓取 | ✅ | Playwright CDP + Edge, 24篇过滤后 |
| Phase 1b: DOI 匹配 | ✅ | CrossRef 20/24 matched |
| Phase 2: Zotero Collection | ✅ | People/Yifan Zhu (ER9XJDQM) |
| Phase 3: 下载 PDF | ✅ | 1.7 MB, RSC publisher |
| Phase 3: Zotero 归档 | ✅ | HTK532AW + 附件 VRBDQH87 |
| Phase 3: Collection 归入 | ✅ | ER9XJDQM 正确分配 |
| Phase 4: 消化模板 | ✅ | 含真实 Top 10 数据 |
| **全链路** | **✅** | **抓取→DOI→下载→归档→解读** |
