# Nanoparticle Targeting in Chemo-Resistant Ovarian Cancer Reveals Dual Axis of Therapeutic Vulnerability Involving Cholesterol Uptake and Cell Redox Balance

Yinu Wang, Andrea E. Calvert, Horacio Cardenas, Jonathon S. Rink, Dominik Nahotko, Wenan Qiang, C. Estelle Ndukwe, Fukai Chen, Russell Keathley, Yaqi Zhang, Ji-Xin Cheng, C. Shad Thaxton,\* and Daniela Matei\*

Platinum (Pt)-based chemotherapy is the main treatment for ovarian cancer (OC); however, most patients develop Pt resistance (Pt-R). This work shows that Pt-R OC cells increase intracellular cholesterol through uptake via the HDL receptor, scavenger receptor type B-1 (SR-B1). SR-B1 blockade using synthetic cholesterol-poor HDL-like nanoparticles (HDL NPs) diminished cholesterol uptake leading to cell death and inhibition of tumor growth. Reduced cholesterol accumulation in cancer cells induces lipid oxidative stress through the reduction of glutathione peroxidase 4 (GPx4) leading to ferroptosis. In turn, GPx4 depletion induces decreased cholesterol uptake through SR-B1 and re-sensitizes OC cells to Pt. Mechanistically, GPx4 knockdown causes lower expression of the histone acetyltransferase EP300, leading to reduced deposition of histone H3 lysine 27 acetylation (H3K27Ac) on the sterol regulatory element binding transcription factor 2 (SREBF2) promoter and suppressing expression of this key transcription factor involved in the regulation of cholesterol metabolism. SREBF2 downregulation leads to decreased SR-B1 expression and diminished cholesterol uptake. Thus, chemoresistance and cancer cell survival under high ROS burden obligates high GPx4 and SR-B1 expression through SREBF2. Targeting SR-B1 to modulate cholesterol uptake inhibits this axis and causes ferroptosis in vitro and in vivo in Pt-R OC.

## 1. Introduction

Emergence of platinum (Pt) resistance (Pt-R) predicts invariably fatal outcomes in high grade serous ovarian cancer (HGSOC) with an expected median survival of 12– 18 months.[1,2] Pt-R HGSOC remains an area of unmet need, where progress has remained slow and clinical outcomes are lagging.[3–6] Understanding key vulnerabilities of Pt-R OC could unlock new possibilities to target HGSOC and improve survival.

While previous studies on Pt-R have focused on DNA repair pathways or altered membrane transporters, new concepts support metabolic reprogramming as a key contributor to the cellular chemoresistant state. The first step in this transition is caused by a Pt-induced shift in central carbon metabolism leading to increased oxidative stress.[7] Our recent work showed that OC cells become Pt-R by increasing glutathione (GSH) anti-oxidative defenses to evade Pt-induced apoptosis.[8] Depletion of GSH-mediated anti-oxidant defense

Y. Wang, H. Cardenas, W. Qiang, C. E. Ndukwe, R. Keathley, Y. Zhang, D. Matei

Department of Obstetrics and Gynecology

Feinberg School of Medicine

Northwestern University

Chicago, IL 60611, USA

E-mail: daniela.matei@northwestern.edu

![](images/7503a0d171a33d1fa3912c28bf26411e936136f7b72719d7b8b5bb2c723430ac.jpg)

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/advs.202305212

© 2024 The Authors. Advanced Science published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

DOI: 10.1002/advs.202305212

A. E. Calvert, C. S. Thaxton

Simpson Querrey Institute for BioNanotechnology

Feinberg School of Medicine

Northwestern University

Chicago, IL 60611, USA

E-mail: cthaxton003@northwestern.edu

J. S. Rink, D. Nahotko

Division of Hematology/ Oncology

Department of Medicine

Feinberg School of Medicine

Northwestern University

Chicago, IL 60611, USA

W. Qiang

Center for Developmental Therapeutics,Feinberg School of Medicine

Northwestern University

Evanston, IL 60208, USA

W. Qiang, C. S. Thaxton, D. Matei

Robert H. Lurie Comprehensive Cancer Center

Northwestern University

Chicago, IL 60611, USA

mechanisms results in cell membrane phospholipid peroxidation and cell death through a mechanism consistent with ferroptosis, an iron-dependent form of cell death that results from oxidation of cell membrane polyunsaturated fatty acid (PUFA) tails of cell membrane phospholipids (PUFA-PL).[8] Using single-cell metabolic imaging based on Raman spectroscopy and isogenic cell lines sensitive or resistant to Pt, we also detected increased lipid uptake and oxidation in Pt-R cells and tumors.[9] Pt-R OC models were dependent upon fatty acids for energy generation and blockade of fatty acid beta-oxidation reversed resistance to Pt in vitro and in vivo. Others reported an increased reliance on lipids in HGSOC models.[10]

Cholesterol is a significant component of cell membranes that modulates fluidity and lipid raft microdomains implicated in oncogenic cellular signaling .[11,12] Emerging evidence supports the role of cholesterol in cancer progression and the development of drug resistance[13,14] leading to interest in manipulating cholesterol levels to induce anti-tumor activity. Cells can either synthesize cholesterol de novo in the endoplasmic reticulum (ER) or uptake cholesterol from circulating lipoprotein particles, like high- and low-density lipoproteins (HDL and LDL).[12] One strategy to attempt to reduce cell cholesterol is by inhibiting de novo cholesterol biosynthesis using “statins” which block the rate limiting enzyme 3-hydroxy-3-methylglutaryl-coenzyme A reductase (HMGCR) that converts 3-hydroxy-3-methylglutaryl-CoA (HMG-CoA) to mevalonate and, eventually, cholesterol. Interestingly, the use of statins was associated with a reduced risk of developing OC in a case control study[15] and with improved survival among women with newly diagnosed OC.[16] However, clinical studies reported that addition of statins to standard chemotherapy did not improve clinical outcomes.[17] These clinical results are consistent with preclinical findings demonstrating increased uptake, but suppressed de novo biosynthesis, of cholesterol in Pt-R OC cells,[14] supporting a potential strategy targeting OC cell cholesterol uptake.

Cellular cholesterol uptake is mediated by cholesterol-rich HDL and LDL[18] and both lipoproteins types have been implicated in cancer.[19] LDLs target the LDL receptor (LDLR) for holoparticle internalization via clathrin mediated endocytosis.[20] Cholesterol from the degraded LDL particle is ultimately reesterified and stored in cytoplasmic lipid droplets (LDs) or transferred to the cell or mitochondrial membranes via the ER. On the other hand, cholesterol rich HDLs (crHDL) target scavenger receptor type B-1 (SR-B1) localized to the cell membrane which transports cholesterol, phospholipids, and other small molecules between the cell membrane and the HDL particle[21] and selectively delivers cholesteryl esters to the cell without holoparticle internalization.[22] After delivering the core payload of cholesteryl ester, the remnant HDL particle dissociates from SR-B1. High expression of SR-B1 has been described as a mechanism of internalizing cholesterol in OC.[23,24]

Because increased lipid metabolism and cholesterol uptake through SR-B1 are associated with a Pt and oxidation resistant phenotype in OC, we studied a strategy using synthetic HDL nanoparticles (NP) that target SR-B1[25–27] and functionally support the efflux of free cholesterol while blocking the delivery of cholesteryl esters[28–30] to resistant OC cells and tumors. The functional properties of HDL NP are enabled by employing an inert nanoparticle “core” as a template to assemble phospholipids and protein (i.e., apolipoprotein A-I) in a manner that approximates the surface chemistry of native crHDLs that bind SR-B1. Different from native crHDL, HDL NPs are synthesized without cholesterol in the outer layer of phospholipids, which enables maximal free cholesterol efflux from the cell membrane and HDL NPs have no internal cholesteryl ester cargo to deliver to the target cell.[27,31–33] Compositional differences between the HDL NPs and crHDLs functionally differentiate the two materials. Here we report that Pt-R OC cells and tumors are rich in intracellular cholesterol and HDL NP targets SR-B1 to deplete cholesterol stores in Pt-R OC cells. We found that GPx4 expression, highly upregulated in Pt-R cells, is intimately linked with cell cholesterol stores and SR-B1 expression. Collectively, targeting SR-B1, cell cholesterol and GPx4 is a unique mechanism to induce cell death through ferroptosis and block Pt-R ovarian tumor growth.

## 2. Results

## 2.1. Pt-R OC Cells Demonstrate Increased Intracellular Cholesterol Accumulation

We developed Pt-R OC models through repeated exposure of OC cell lines to cytotoxic doses of Pt.[8,34] Compared to platinumsensitive (Pt-S) cells, the Pt-R cells demonstrated increased antioxidant capacity (upregulated GPx4), increased susceptibility to ferroptosis,[8] and increased fatty acid (FA) accumulation and import.[9] Given the reported dependence of other cancer cells to cholesterol,[13,35,36] we measured intracellular total cholesterol levels through an Amplex Red colorimetric assay in OC Pt-S and Pt-R cells. Total cholesterol abundance, including free cholesterol and cholesteryl esters, was higher in Pt-R compared to Pt-S OVCAR5 and OVCAR4 cells (Figure 1A,B). As cholesterol is a key component of lipid droplets (LDs), we also measured total LD content in OVCAR5 and OVCAR4 Pt-R and Pt-S cells by using Nile Red staining and quantification of mean fluorescence intensity (MFI) via flow cytometry. Increased LD content was demonstrated in Pt-R versus Pt-S OVCAR5 and OVCAR4 cells (Figure 1C-D). LDs contain tryglicerides (TAGs) along with cholesterol, therefore, we also measured TAGs content. TAGs were increased in both OVCAR5 and OVCAR4 Pt-R cells versus Pt-S cells (Figures S1A,B, Supporting Information). Spectroscopic stimulated Raman scattering (SRS) imaging maps cholesterol content by using its unique signature in the high wave number CH vibration window. SRS imaging of Pt-S and Pt-R cancer cell populations quantified cholesterol content and showed increased cholesterol rich cell populations in Pt-R versus Pt-S cells (Figure 1E–G). Thus, several quantitative methods demonstrated increased intracellular cholesterol and TAGs in Pt-R versus Pt-S OC cells.

A  
![](images/216f44220df65613f38ffd9366a0f202455b937e55b13bcd0d8e638d395ce5bc.jpg)

<details>
<summary>bar chart</summary>

| Group | Cholesterol (ng/ml/10⁵ cells) |
|-------|-------------------------------|
| Pt-S  | 30                            |
| Pt-R  | 60                            |
</details>

B  
![](images/dc0c68b9b8f389fcd81170a0e3cbe5c073b1378863ae8e564b0eac22cbad022a.jpg)

<details>
<summary>bar chart</summary>

| Group | Cholesterol (ng/ml/10⁵ cells) |
|-------|-------------------------------|
| Pt-S  | 25                            |
| Pt-R  | 75                            |
</details>

C  
![](images/dddaf44d258d694218f806e69a521a78a98c401bf16b11a34c443f01163998fd.jpg)

<details>
<summary>bar chart</summary>

| Group | Nile Red (Mean fluorescence intensity) |
|-------|----------------------------------------|
| Pt-S  | 3000                                   |
| Pt-R  | 6000                                   |
</details>

D  
![](images/52b680060623f5e05bc8890c5cbd2fb1efb15dde28c20bee1ab05531aed4b81e.jpg)

<details>
<summary>bar chart</summary>

| Condition | Nile Red (Mean fluorescence intensity) |
| --------- | ------------------------------------- |
| Pt-S      | 1700                                  |
| Pt-R      | 2600                                  |
</details>

E  
![](images/b6a972ec2b8d074007a2d90b53f4fa6594889ad06d93839c2216f28d3f2ecb1c.jpg)

<details>
<summary>text_image</summary>

Stack
Cholesterol
OVCAR5 Pt-S
OVCAR5 Pt-R
10µm
</details>

F

![](images/e85f41b44c4508003fc431a2cb2af2da4ed63f40b3708605f9798e5e9df95ac1.jpg)

<details>
<summary>violin chart</summary>

| Group | Relative cholesterol amount |
|-------|-----------------------------|
| Pt-S  | 1.0                         |
| Pt-R  | 1.5                         |
</details>

G

![](images/3e28b80de1abec2487453c6b540a713bd8649c6db13c03e919864de8ebc3349f.jpg)

<details>
<summary>line chart</summary>

| Relative cholesterol amount | Pt-S  | Pt-R  |
| --------------------------- | ----- | ----- |
| 0.0                         | 0.000 | 0.000 |
| 0.4                         | 0.100 | 0.050 |
| 0.8                         | 0.430 | 0.320 |
| 1.2                         | 0.330 | 0.400 |
| 1.6                         | 0.120 | 0.130 |
| 2.0                         | 0.020 | 0.080 |
| 2.4                         | 0.000 | 0.010 |
</details>

H  
![](images/9fa0cf046120ebac6eb0266085b6cd368a269368ab5d29918e4f713277e0d23c.jpg)

<details>
<summary>line chart</summary>

| Rank in Ordered Dataset | Enrichment score (RS) |
| ----------------------- | --------------------- |
| 0                       | 0.0                   |
| 2,000                   | -0.1                  |
| 4,000                   | -0.3                  |
| 6,000                   | -0.5                  |
| 8,000                   | -0.7                  |
| 10,000                  | -0.9                  |
| 12,000                  | -1.1                  |
| 14,000                  | -1.3                  |
</details>

![](images/217a9a39fe80bf0db43f3071ef463370030dd7c95a375997ef81a413ce5e4894.jpg)

<details>
<summary>line chart</summary>

| Shares in Ordered Dataset | Enrichment profile | Hits | Ranking metric scores |
| --- | --- | --- | --- |
| 0 | - | - | - |
| 2,000 | - | - | - |
| 4,000 | - | - | - |
| 6,000 | - | - | - |
| 8,000 | - | - | - |
| 10,000 | - | - | - |
| 12,000 | - | - | - |
| 14,000 | - | - | - |
| 16,000 | - | - | - |
| 18,000 | - | - | - |
| 20,000 | - | - | - |
| 22,000 | - | - | - |
| 24,000 | - | - | - |
| 26,000 | - | - | - |
| 28,000 | - | - | - |
| 30,000 | - | - | - |
| 32,000 | - | - | - |
| 34,000 | - | - | - |
| 36,000 | - | - | - |
| 38,000 | - | - | - |
| 40,000 | - | - | - |
| 42,000 | - | - | - |
| 44,000 | - | - | - |
| 46,000 | - | - | - |
| 48,000 | - | - | - |
| 50,000 | - | - | - |
| 52,000 | - | - | - |
| 54,000 | - | - | - |
| 56,000 | - | - | - |
| 58,000 | - | - | - |
| 60,000 | - | - | - |
| 62,000 | - | - | - |
| 64,000 | - | - | - |
| 66,000 | - | - | - |
| 68,000 | - | - | - |
| 70,000 | - | - | - |
| 72,000 | - | - | - |
| 74,000 | - | - | - |
| 76,000 | - | - | - |
| 78,000 | - | - | - |
| 80,000 | - | - | - |
| 82,000 | - | - | - |
| 84,000 | - | - | - |
| 86,000 | - | - | - |
| 88,000 | - | - | - |
| 90,000 | - | - | - |
| 92,000 | - | - | - |
| 94,000 | - | - | - |
| 96,000 | - | - | - |
| 98,000 | - | - | - |
| 100,000 | - | - | - |
| 12,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 14,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 16,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 18,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 20,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 22,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 24,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 26,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 28,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 32,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 34,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 36,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 38,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 42,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 44,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 46,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 48,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 52,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 54,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 62,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 72,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 74,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 76,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 78,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 82,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 84,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 86,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 88,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 92,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 94,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 96,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 98,555 | ~-1.5 | ~-1.5 | ~-1.5 |
| 99,999 | ~-1.2 | ~-1.2 | ~-1.2 |
| 9999 | ~-1.2 | ~-1.2 | ~-1.2 |
| 9999 | ~-1.2 | ~-1.2 | ~-1.2 |
| 9999 | ~-1.2 | ~-1.2 | ~-1.2 |
| 9999 | ~-1.2 | ~-1.2 | ~+3.4E-4 |
</details>

![](images/4b202104b795eb6177b7211974702f6ea02752b3bc6a0f764b48fc5b129fd680.jpg)

<details>
<summary>line chart</summary>

| Rank in Ordered Dataset | Enrichment score (85) |
| ----------------------- | --------------------- |
| 2,000                   | 0.0                   |
| 4,000                   | -0.2                  |
| 6,000                   | -0.4                  |
| 8,000                   | -0.6                  |
| 10,000                  | -0.8                  |
| 12,000                  | -1.0                  |
| 14,000                  | -1.2                  |
</details>

![](images/c2a3799519a5a132e882759dd5b7b0dc0a9dbb7012837cf69ea1f672d14765b0.jpg)

<details>
<summary>text_image</summary>

Pt-S Pt-R
HMGCS1 57 kDa
SQLE 60 kDa
GAPDH 37 kDa
</details>

![](images/c590a7f8424b91dc2dceedfae480840308c0d0fd5ef104261195dbae23977431.jpg)

<details>
<summary>bar chart</summary>

| Gene    | Pt-S  | Pt-R  |
|---------|-------|-------|
| HMGCS1  | 1.0   | 0.5   |
| SQLE    | 0.5   | 0.2   |
</details>

J  
![](images/dc7057dbca6a81180cfc72303b9bf64de82bd84662798ca64713883f6f15d86b.jpg)

<details>
<summary>bar chart</summary>

| Group | MFI TF Cholesterol |
|-------|---------------------|
| Pt-S  | 4500                |
| Pt-R  | 7000                |
</details>

K  
![](images/139e4bdeb09dd7782305cb121d5952e01eb3870abf0333f314f3168781891395.jpg)

<details>
<summary>bar chart</summary>

| Group | MFI TF Cholesterol |
|-------|---------------------|
| Pt-S  | 7000                |
| Pt-R  | 9000                |
</details>

L

![](images/1bb17b9d34d0743499ea06ffc43b0cb2e2bc4b51b64a706b09be58c3ac729d42.jpg)

<details>
<summary>text_image</summary>

FT190
NOEM
OVCAR4 Pt-S
OVCAR4 Pt-R
Peo1
Peo4
OVCAR5 Pt-S
OVCAR5 Pt-R
SR-B1 57 kDa
β-actin 42 kDa
</details>

M  
![](images/21107616d7bc2d1a187d387f4df559088872ab9e8915e9e6d1b39f89ed135348.jpg)

<details>
<summary>text_image</summary>

IOSE HFTEC FT190 Pt_1 Pt_2
SR-B1 57 kDa
β-actin 42 kDa
</details>

N  
![](images/0b0ea7e1f2e3f61a79176f53ab0712bcc4f5b03e9fe93e5fedef6320bd8b9d0d.jpg)

<details>
<summary>text_image</summary>

FT190
Pt_1 Pt_2 Pt_3 Pt_4 Pt_5 Pt_6
SR-B1 57 kDa
β-actin 42 kDa
</details>

Figure 1. Platinum resistant OC cells are more dependent on cholesterol import than on de novo synthesis for survival. A,B) Intracellular total cholesterol level $( \mathsf { m e a n } \pm \mathsf { S D } , \mathsf { n } = 3 )$ measured using an Amplex Red cholesterol assay kit in Pt-S and Pt-R variants of OVCAR5 (A) and OVCAR4 (B) OC cells. C,D) Total lipid levels in OVCAR5 (C) and OVCAR4 (D) Pt-S and Pt-R cells were measured by Nile Red staining and analyzed by flow cytometry. Values represent median fluorescent intensity (MFI; mean ± SD, n = 3). E) Representative stimulated Raman scattering (SRS) images (left panel) and unmixed cholesterol channel signal images (right panel) of OVCAR5 Pt-S and Pt-R OC cells. F) Quantification of the SRS cholesterol channel signal intensity from

Next, we investigated whether increased cholesterol content resulted from de novo biosynthesis or increased uptake. RNA sequencing comparing Pt-R and Pt-S OVCAR5 cells (GSE 148 003) demonstrated downregulation of genes related to cholesterol synthesis among differentially expressed genes (DEGs). Gene set enrichment analysis (GSEA) showed significant enrichment of gene sets related to “hallmark cholesterol homeostasis” (Figure S1C, Supporting Information), “reactome cholesterol biosynthesis” and “reactome regulation of cholesterol biosynthesis by SREBP/F” in OV-CAR5 Pt-S versus Pt-R cells (Figure 1H), suggesting downregulation of cholesterol synthesis gene sets in resistant cells. Genes implicated in these pathways are listed in Tables S1 and S2, Supporting Information. Two important enzymes implicated in de novo cholesterol biosynthesis, 3-hydroxy-3-methylglutaryl Coen zyme A synthase 1 (HMGCS1) and squalene monooxygenase (SQLE), were downregulated in Pt-R compared with Pt-S OC cells (Figure 1I). Given the observations supporting downregulation of cholesterol biosynthesis in Pt-R cells, we next examined cholesterol uptake. The TopFluor-labeled cholesterol uptake assay demonstrated increased cholesterol uptake in Pt-R OVCAR5 (Figure 1J) and OVCAR4 (Figure 1K) compared to Pt-S cells, suggesting that Pt-R cells are dependent on cholesterol uptake to maintain high intracellular cholesterol levels. Further, the expression levels of the scavenger receptor type B-1 (SR-B1), a highaffinity HDL receptor,[37] were increased in Pt-R OVCAR4 and OVCAR5 compared with Pt-S cells and in Peo4 (Pt-R) versus Peo1 (isogenic Pt-S) cell lines (Figure 1L). SR-B1 protein expression was higher in a majority of OC cell lines compared to normal en dometrial cells (NoEM),[38] and immortalized fallopian tube epithelial cells (FT-190) (Figure 1L). Upregulated SR-B1 protein ex pression was also validated in primary cells dissociated from HG-SOC tumors (n = 6, Table S3, Supporting Information) compared with immortalized ovarian surface epithelium (IOSE), primary human fallopian tube epithelial cells (HFTEC), and FT190 cells (Figure 1M,N). In addition, patients with high tumoral SR-B1 expression as profiled by publically available Gene Expression Omnibus (GEO) databases and The Cancer Genome Atlas (TCGA) databases had significantly reduced overall survival compared to patients with low SR-B1 expression (p = 0.029; Figure S1D, Sup porting Information).

## 2.2. HDL NP Inhibit Pt-R OC Growth

To investigate if SR-B1-dependent cholesterol uptake is necessary to sustain OC survival, we employed HDL-like nanoparticles (HDL NPs) to block SR-B1. HDL NPs are bioinspired materials that share physicochemical features with native HDLs including size, charge, and surface composition.[28,30,32,37,39] OVCAR5 and OVCAR4 Pt-S and Pt-R cells were treated with increasing doses of HDL NPs and cell viability was measured. Pt-R cells were more sensitive to HDL NP treatment compared with Pt-S cells, as evidenced by lower $\mathrm { I C } _ { 5 0 }$ values (Figure 2A,B, $2 3 . 4 9 \pm 1 . 9 6$ nm (Pt-S) versus 8.46 ± 2.40 nm (Pt-R) for OVCAR5 and $8 . 0 7 \pm 1 . 6 0 $ nm (Pt-S) versus $3 . 6 1 \pm 0 . 7 6$ nm (Pt-R) for OVCAR4 cells). We hypothesized that the difference in sensitivity was due to a reduction in SR-B1-mediated cholesterol uptake and increased dependence of Pt-R cells on cholesterol. To test this, we examined the uptake of a fluorescently labeledTopFluor (TF) cholesterol in OC cells treated with HDL NP. Treatment with HDL NP reduced cholesterol uptake in both Pt-S (Figure 2C,E) and Pt-R (Figure 2D,F) cells.

Treatment with HDL NP also reduced tumor burden in murine models of Pt-R OC. Pt-R OVCAR5 cells were orthotopically implanted in the peritoneal cavity of female nude mice. Treatment with PBS (control) or HDL NP was given five times a week (Mon.-Fri.) i.p. for 4 weeks. HDL NP treatment was well tolerated and did not induce significant changes in body weight (Figure S2A, Supporting Information). Mice treated with HDL NP had decreased tumor burden (Figure 2G), and significantly reduced total tumor weight (Figure 2H) and number of tumors (Figure 2I). Similar results were observed by using a Pt-R ovarian PDX model. Body weights were not affected by HDL NP treatment (Figure S2B, Supporting Information). PDX tumors disseminated intraperitoneally and displayed HGSOC histological characteristics (Figure S2C,D, Supporting Information). HDL NPs reduced total tumor weight (Figure 2J), number of metastases (Figure 2K), and tumor volume (Figure S2E, Supporting Information). Taken together, these results demonstrate that targeting SR-B1 by HDL NPs reduces cholesterol uptake and causes decreased cell viability in vitro and tumor growth in vivo.

## 2.3. HDL NPs Decrease the Viability of OC Cells by Inducing Ferroptosis

Cells dependent on cholesterol uptake have been shown to be especially sensitive to ferroptosis[30,35,40] and we have shown that Pt-R cells are resistant to pro-apoptotic signals, but can be killed through ferroptosis.[8] We therefore determined whether HDL NP treatment induced increased levels of oxidized lipids in OC cell membranes by using C11 BODIPY staining. HDL NP treatment resulted in a dose- and time-dependent increase in oxidized lipids in both Pt-S (Figure 3A and Figure S3A, Supporting Information) and Pt-R cells (Figure 3B and Figure S3B, Supporting Information); however, the magnitude of lipid

OVCAR5 Pt-S and Pt-R OC cells relative to total cholesterol levels and G) at cell fraction level. H) GSEA enrichment plots of gene sets involved in de novo cholesterol synthesis: “hallmark cholesterol homeostasis,” “reactome cholesterol biosynthesis,” and “reactome regulation of cholesterol biosynthesis by SREBP/F” in OVCAR5 Pt-S versus Pt-R cells measured by RNA-seq (n = 3). I) (Left) Western blot images of enzymes HMGCS1 and SQLE regulating de novo cholesterol biosynthesis in OVCAR5 Pt-S and Pt-R cells. Quantification of band intensity was performed by Image J and is shown in the right panel (n = 3). J,K) Cholesterol uptake in OVCAR5 (J) and OVCAR4 (K) Pt-S and Pt-R cells measured using TopFluor Cholesterol by flow cytometry. Values represent median fluorescent intensity (MFI; mean ± SD, n = 3). L) Western blot of SR-B1 protein in immortalized fallopian tube epithelial cells (FT-190), normal endometrial cells (NoEM), OVCAR5, and OVCAR4 Pt-S and Pt-R cells, and in the isogenic Pt-S Peo1 and Pt-R Peo4 OC cells $( n = 3 )$ . M) SR-B protein expression levels in immortalized ovarian surface epithelial cells (IOSE), normal human fallopian tube epithelial cells (HFTEC), FT190, and two primary cells derived from HGSOC tumors (n = 2). N) SR-B1 protein levels measured by western blot in OC tumors (n = 6) and in FT190 cells. For all panels, \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001, \*\*\*\*p < 0.0001.

![](images/c5816924b22d18eb5e26b0ec4962a409dc4441573a23b40b382e2048e6e952a3.jpg)

<details>
<summary>line chart</summary>

| [HDL NP] (nM) | Pt-S Relative cell viability | Pt-R Relative cell viability | Pt-S IC50 (nM) | Pt-R IC50 (nM) |
| ------------- | ---------------------------- | ---------------------------- | -------------- | -------------- |
| 0.01          | ~100                         | ~100                         | ~25            | ~25            |
| 0.1           | ~95                          | ~98                          | ~23            | ~23            |
| 1             | ~85                          | ~90                          | ~22            | ~22            |
| 10            | ~60                          | ~70                          | ~10            | ~10            |
| 100           | ~10                          | ~10                          | ~5             | ~5             |
| 1000          | ~0                           | ~0                           | ~0             | ~0             |
</details>

![](images/de9968c20f1f763013b46031b2de17b490e072756387d93ed867dc49c7c52437.jpg)

<details>
<summary>line chart</summary>

| [HDL NP] (nM) | Pt-S Relative cell viability | Pt-R Relative cell viability | IC50 (nM) |
| ------------- | ---------------------------- | ---------------------------- | --------- |
| 0.01          | 100                          | 100                          | 8         |
| 0.1           | 100                          | 95                           | 7         |
| 1             | 95                           | 85                           | 6         |
| 10            | 60                           | 40                           | 4         |
| 100           | 10                           | 5                            | 3         |
| 1000          | 0                            | 0                            | 2         |
</details>

![](images/b12177a60c887dcd353052756cb97559235db29a81b8173c3d25cfa5908d8ce0.jpg)

<details>
<summary>bar chart</summary>

| [HDL NP] (nM) | MFI TF Cholesterol |
| ------------- | ------------------ |
| 0             | 4500               |
| 10            | 3000               |
| 20            | 2500               |
| 40            | 2000               |
</details>

![](images/26d203117240ca9aae3a3b3a154762172d290383cfd04b9980d4efa16f162a77.jpg)

<details>
<summary>bar chart</summary>

| [HDL NP] (nM) | MFI TF Cholesterol |
| ------------- | ------------------ |
| 0             | 7000               |
| 10            | 4500               |
| 20            | 3800               |
| 40            | 2800               |
</details>

![](images/d2b1fa8a20e3f77fbc627cc192a089e23346b4a343f2691df5d171b2d915aaca.jpg)

<details>
<summary>bar chart</summary>

| [HDL NP] (nM) | MFI TF Cholesterol |
| ------------- | ------------------ |
| 0             | 25000              |
| 10            | 20000              |
| 20            | 15000              |
| 40            | 12000              |
</details>

![](images/45123e8a0e8b8ae8af695eeac5891354bf3e6ec6f810f916758c616148e7a341.jpg)

<details>
<summary>bar chart</summary>

| HDL NP (nM) | MFI TF Cholesterol |
|-------------|-------------------|
| 0           | 30000             |
| 10          | 25000             |
| 20          | 22000             |
| 40          | 18000             |
</details>

![](images/5b9293fbb84135ce3ee40949285fe50e489e74ef362b8136191bbf54a3811cfa.jpg)

<details>
<summary>natural_image</summary>

Medical images showing abdominal organs under PBS and HDL NP conditions, with white arrows indicating specific anatomical features (no text or symbols present)
</details>

![](images/e1c283e9ac0d99aa6cb6d3df364915b62c83e8f4e144b8e0db9863df11ae61ec.jpg)

<details>
<summary>bar chart</summary>

| Group | Tumor weight (g) |
|-------|------------------|
| PBS   | 0.35             |
| HDL NP| 0.20             |
</details>

![](images/62c774c281dfeb12841c9a68fa21ed06719a220930d9aa35a137ca725bac8a0b.jpg)

<details>
<summary>bar chart</summary>

| Group  | Total number of tumors |
| ------ | ---------------------- |
| PBS    | 120                    |
| HDL NP | 80                     |
</details>

![](images/013f0c40fa5a5f0f7d379f33a5f9d4d08dcd2bce3383323c786e6b00b46d6e77.jpg)

<details>
<summary>scatterplot</summary>

| Group  | Tumor weight (g) |
| ------ | ---------------- |
| Ctrl   | 0.25             |
| HDL NP | 0.05             |
</details>

![](images/4908f01fa2e9c79d1164768042731755059e6cd2bc56f9419d753844a317388d.jpg)

<details>
<summary>scatterplot</summary>

| Group   | Total number of tumors |
| ------- | ---------------------- |
| Ctrl    | 7                      |
| HDL NP  | 2                      |
</details>

Figure 2. HDL NPs decrease viability of OC cells and inhibit growth of OC tumor xenografts. A,B) Effects of HDL NPs on viability and $1 C _ { 5 0 }$ estimates in Pt-S and Pt-R ${ \mathsf { O V C A R 5 \ ( A ) } }$ and OVCAR4 (B) cells treated for 72 (OVCAR4) or 96 h (OVCAR5) and determined using MTS assays. Average $1 \mathsf { C } _ { 5 0 }$ (mean $\pm \mathsf { S D } , n = 3$ replicate experiments) are shown on the right. C–F) Cholesterol uptake $( \mathsf { m e a n } \pm \mathsf { S D } , n = 3 )$ ) measured using TopFluor Cholesterol and flow cytometry in OVCAR5 Pt-S (C) and Pt-R (D) and OVCAR4 Pt-S (E) and Pt-R (F) OC cells treated with increasing concentrations of HDL NP. G) Representative images of mice injected intraperitoneally with OVCAR5 Pt-R OC cells and then treated with PBS or HDL NPs. The largest tumors are indicated by arrows. H,I) Total tumor weight (H) and number of tumors (I) in mice treated as described in $( \mathsf { C } ) ; n = 1 7$ per group. $\bar { \mathbf { \Lambda } } _ { | , \mathsf { K } ) }$ . Total tumor weights (J) and numbers of tumors (K) in mice bearing ovarian Pt-R PDX treated with HDL NPs compared to PBS $( n = 7$ per $\mathtt { g r o u p } )$ . Values are mean $\pm \mathsf { S D } , \mathsf { \pi } ^ { \mathrm { s } \mathrm { s } } p < 0 . 0 5 , \mathsf { \pi } ^ { \mathrm { s } \mathrm { s } } p < 0 . 0 1 , \mathsf { \pi } ^ { \mathrm { s } \mathrm { s } \mathrm { s } } p < 0 . 0 0 1 )$ .

A  
![](images/6f9e2cd38401c31cf12ee517da3cd2cee817d885782c4d09ddaf8b08082982eb.jpg)

<details>
<summary>bar chart</summary>

| Time (hours) | PBS   | 10 nM HDL NP | 20 nM HDL NP | 40 nM HDL NP |
| ------------ | ----- | ------------ | ------------ | ------------ |
| 24           | ~1    | ~1           | ~1           | ~1           |
| 48           | ~1    | ~6           | ~7           | ~8           |
| 72           | ~1    | ~10          | ~11          | ~17          |
</details>

B  
![](images/13e77c0a977c0aefb9a4068598baf7fe38addf1a72349233a9886b9673978cba.jpg)

<details>
<summary>bar chart</summary>

| Time (hours) | PBS | 10 nM HDL NP | 20 nM HDL NP | 40 nM HDL NP |
| ------------ | --- | ------------ | ------------ | ------------ |
| 24           | ~0  | ~0           | ~0           | ~0           |
| 48           | ~2  | ~16          | ~16          | ~20          |
| 72           | ~0  | ~10          | ~12          | ~24          |
</details>

C  
![](images/7e5f4e801255f08bfb04c8cafa7019e93df124c6a1c434e5b5588ce83ca6e52d.jpg)

<details>
<summary>bar chart</summary>

| [HDL NP] (nM) | Control | Ferrostatin-1 | DFO |
| ------------- | ------- | ------------- | --- |
| 0             | 100     | 100           | 100 |
| 6.25          | 100     | 140           | 130 |
| 12.5          | 100     | 130           | 120 |
| 25            | 70      | 140           | 100 |
</details>

D  
![](images/49e0f635073c22ece5ab0ebae9e5873d4142bab3a0423a6e2561d93225f40e93.jpg)

<details>
<summary>bar chart</summary>

| [HDL NP] (nM) | Control | Ferrostatin-1 | DFO |
| ------------- | ------- | ------------- | --- |
| 0             | ~95     | ~85           | ~90 |
| 6.25          | ~70     | ~100          | ~95 |
| 12.5          | ~50     | ~80           | ~75 |
| 25            | ~30     | ~70           | ~55 |
</details>

E  
![](images/7a8ae43ef9ff8bf9195dfac6a3831fc5080074c0c888c4fe598edece9add8c1c.jpg)

<details>
<summary>other</summary>

| Time | GPx4 22 kDa | β-actin 42 kDa |
|------|-------------|----------------|
| 24   | 1           | 0              |
| 48   | 0.33        | 10             |
| 72   | 0.30        | 20             |
|      | 0.38        | 40             |
|      | 1.24        | 0              |
|      | 0.18        | 10             |
|      | 0.12        | 20             |
|      | 0.10        | 40             |
|      | 1.29        | 0              |
|      | 0.18        | 10             |
|      | 0.05        | 20             |
|      | 0.03        | 40             |
HDL NP (nM) | 0         | 10             |
|      | 10          | 20             |
|      | 20          | 40             |
|      | 40          | 0              |
|      | 0           | 10             |
|      | 10          | 20             |
|      | 20          | 40             |
|      | 40          | 0              |
</details>

F

![](images/e4e1c439a6c396daacb3dbdd7705000d829fc67ece8e11c36d51067942b61af4.jpg)

<details>
<summary>other</summary>

| Time (hours) | GPx4 22 kDa | β-actin 42 kDa |
| --- | --- | --- |
| 24 | 10.32 | 10 |
| 48 | 0.33 | 20 |
| 72 | 0.29 | 40 |
| GPx4 | 2.73 | 0 |
| GPx4 | 0.18 | 10 |
| GPx4 | 0.10 | 20 |
| GPx4 | 0.07 | 40 |
| GPx4 | 3.19 | 0 |
| GPx4 | 0.08 | 10 |
| GPx4 | 0.05 | 20 |
| GPx4 | 0.06 | 40 |
| HDL NP (nM) | 0 | 10 |
| HDL NP (nM) | 10 | 20 |
| HDL NP (nM) | 20 | 40 |
| HDL NP (nM) | 0 | 0 |
| HDL NP (nM) | 10 | 10 |
| HDL NP (nM) | 20 | 20 |
| HDL NP (nM) | 40 | 40 |
| HDL NP (nM) | 0 | 10 |
| HDL NP (nM) | 10 | 20 |
| HDL NP (nM) | 20 | 40 |
| HDL NP (nM) | 0 | 10 |
| HDL NP (nM) | 10 | 20 |
| HDL NP (nM) | 20 | 40 |
| HDL NP (nM) | 0 | 10 |
| HDL NP (nM) | 10 | 20 |
| HDL NP (nM) | 10 | 40 |
| HDL NP (nM) | 0 | 10 |
| HDL NP (nM) | 10 | 20 |
| HDL NP (nM) | 10 | 40 |
| HDL NP (nM) | 0 | 10 |
| HDL NP (nM) | 10 | - |
| HDL NP (nM) | - | - |
| HDL NP (nM) | - | - |
| HDL NP (nM) | - | - |
| HDL NP (nM) | - | - |
| HDL NP (nM) | - | - |
| HDL NP (nM) | - | - |
| HDL NP (nM) | - | - |
</details>

![](images/ee95cadaed67eae811c258707380113f1e5c7625e4a7f3aad185dbced52d4fd4.jpg)

<details>
<summary>bar chart</summary>

| Group | % Oxidized/Reduced C11 BODIPY |
|-------|-------------------------------|
| PBS   | 3.0                           |
| HDL NP| 5.0                           |
</details>

H  
![](images/a86c0461de6aac8f1b3681750f265712f5df98803d8d2f35ad3afd4ce3efe015.jpg)

<details>
<summary>western blot chart</summary>

| Treatment | SR-B1 (kDa) | GPx4 (kDa) | α-tubulin (kDa) |
| --------- | ----------- | ---------- | --------------- |
| PBS       | 57          | 22         | 50              |
| HDL NP    | -           | -          | -               |
</details>

Figure 3. HDL NPs decrease viability of Ovarian Cancer cells by inducing ferroptosis. A,B) OVCAR5 Pt-S (A) and Pt-R (B) cells were treated with increasing concentrations of HDL NPs for 24, 48, or 72 h and the percentage of oxidized/reduced lipids was determined by C11 BODIPY staining (mean $\pm \mathsf { S D } _ { \mathrm { i } }$ , $n = 3 )$ . (C,D) MTS assays measure viability of OVCAR5 Pt-S (C) and Pt-R (D) cells treated with increasing concentrations of HDL ${ \mathsf { N P s } } ,$ , alone or in combination with ferrostatin-1 or DFO. Values are mean ± SD (n = 3). E,F) Measurements of GPx4 and ??-actin (loading control) protein levels by western blot in OVCAR5 Pt-S (E) and Pt-R (F) cells treated with HDL NPs for 24, 48, or 72 h. Band intensity was quantified using Image J and is indicated below each blot. G) Percentage of oxidized/reduced lipids measured by C11 BODIPY staining in cells isolated from tumor xenografts induced in mice by OVCAR5 Pt-R cells and treated with PBS or HDL NP (mean ± SD, n = 10–11). H) Western blot analysis shows SR-B1, GPx4, and ??-tubulin (loading control) protein levels in xenografts resected from mice injected i.p. with OVCAR5 Pt-R cells and treated $\mathsf { i . p . }$ with PBS or HDL NPs. Lanes represent tumors from different mice. For all panels, $^ { * } p < 0 . 0 5 , ^ { * * } p < 0 . 0 0 0 1 , ^ { * * * } p < 0 . 0 0 1$ .

oxidation was slightly increased in Pt-R cells. Ferroptosis can be rescued by delivering the membrane-targeted antioxidant, ferrostatin-1, or the iron chelator, deferoxamine (DFO). HDL NP-induced decreased cell viability was, indeed, rescued by ferroptosis inhibitors, ferrostatin-1 and DFO, (Figure 3C,D and Figure S3C,D, Supporting Information) confirming ferroptosis. Glutathione peroxidase 4 (GPx4) is a key antioxidant enzyme, which reduces oxidized cell membrane polyunsaturated lipids preventing ferroptosis. Western blotting demonstrated that treatment of Pt-R and Pt-S OC cells with HDL NPs potently reduced

GPx4 protein expression in a dose and time dependent manner (Figure 3E,F and Figure S3E,F, Supporting Information). Furthermore, higher oxidized lipid content was observed in Pt-R xenografts treated with HDL NP compared to PBS treated tumors (Figure 3G). In addition, Pt-R tumors from mice treated with HDL NPs had lower GPx4 protein expression than those treated with PBS (Figure 3H). Further. slightly decreased SR-B1 protein expression levels were noted in HDL NPs treated xenografts (Figure 3H). indicating potential correlation between GPx4 and SR-B1 expression levels. These data support that HDL

NPs induce ferroptosis in Pt-R OC cells and tumors in vitro and in vivo. Interestingly, the expression levels of HMGCS1, one of the key enzymes regulating de novo cholesterol synthesis, was in creased after HDL NPs treatment in OVCAR5 Pt-S cells (Figure S3G, Supporting Information), but only modestly affected in Pt-R cells (Figure S3H, Supporting Information), indicating that blocking cholesterol import may induce compensatory activation of cholesterol synthesis. Atorvastatin, a potent inhibitor of cholesterol synthesis, had additive effects on reducing cells viability of Pt-S OVCAR5 cells in combination with HDL NPs, but did not add cytotoxic effects to HDL NPs in Pt-R OVCAR5 cells (Figure S3I,J, Supporting Information).

## 2.4. GPx4 Inhibition Re-Sensitizes OC Cells to Chemotherapy by Targeting SR-B1 Mediated Cholesterol Import

Due to the observed correlation between GPx4 and SR-B1 expression in Pt-R cells, we investigated whether SR-B1-regulated cholesterol homeostasis in OC cells is linked to the antioxidant enzyme GPx4. We knocked-down (KD) GPX4 by stable shRNA transfection in Pt-R OC cells. Decreased GPx4 protein expression was confirmed by western blotting in Pt-S and Pt-R OV-CAR5 and OVCAR4 cells transduced with two shRNA sequences targeting GPx4 versus control shRNA (shCTRL; Figure 4A,B, Figure S4A,B,E,G, Supporting Information) and response to Pt was measured in cells in which the protein was downregulated. GPx4 KD decreased the $\mathrm { I C } _ { 5 0 }$ to Pt by approximately twofold in Pt-R OVCAR5 (Figure S4C, Supporting Information) and OV-CAR4 cells (Figure S4D, Supporting Information), and by ≈1.5- fold in Pt-S OVCAR5 (Figure S4F, Supporting Information) and OVCAR4 cells (Figure S4H, Supporting Information). Similarly, treatment with HDL NPs, which depletes cancer cells of GPx4, sensitized Pt-R cancer cells to carboplatin. Combination of HDL NPs and carboplatin synergistically killed OVCAR5 Pt-R cells compared with either treatment alone (combination index (CI), CI = 0.825 at $\mathrm { E D } _ { 5 0 } , \mathrm { C I } = 0 . 9 2 4$ at $\mathrm { E D } _ { 7 5 } .$ , Figure S4I,J, Supporting Information).

To understand whether modulation of GPx4 expression alters pathways related to cholesterol uptake or biosynthesis, an unbiased approach was pursued by using transcriptomic analyses. RNA sequencing of Pt-R OVCAR5 cells transfected with shGPx4 versus shCTRL revealed 3919 DEGs (FDR<0.05, see GSE234404). “Reactome analysis” of top molecular pathways associated with the downregulated DEGs in Pt-R OVCAR5 cells transfected shGPx4 versus shCTRL cells included, among the top altered gene sets, HDL-mediated lipid transport (Figure 4E). In addition, GPx4 KD in OVCAR5 Pt-S and Pt-R OC cells reduced SR-B1 expression (Figure 4A,B, Figure S4E,G, Supporting Information), indicating that GPx4 is linked to cholesterol accumulation in Pt-R OC cells by modulating SR-B1 and HDL-mediated cholesterol uptake. Therefore, we examined the impact of GPx4 KD on cholesterol accumulation on OVCAR5 Pt-S and Pt-R cells. An Amplex Red cholesterol assay indicated that total intracellular cholesterol levels were reduced in OVCAR5 Pt-S (Figure 4F) and Pt-R cells (Figure 4G) in which GPx4 was knocked down compared with shCTRL transfected cells. SRS imaging analysis also demonstrated decreased intracellular cholesterol signal intensity in OVCAR5 Pt-S (Figure 4H,I and Figure S4K, Supporting Information) and Pt-R (Figure 4J,K and Figure S4L, Supporting Information) cells in which GPx4 was KD compared with control cells. To determine whether the effects of GPx4 on cholesterol content were contributed by altered cholesterol uptake, we used the TopFluor cholesterol uptake assay. FACS analysis demonstrated that GPx4 KD reduced cholesterol uptake in OVCAR5 Pt-S (Figure 4L), and Pt-R cells compared with control cells (Figure 4M). Collectively these data support that GPx4 expression is linked to intracellular cholesterol homeostasis and cholesterol uptake, which contribute to chemoresistance in OC cells.

## 2.5. GPx4-Mediated Cholesterol Accumulation Maintains Cellular Redox Homeostasis in OC Cells

We previously reported that Pt-R OC cells harbor enhanced glutathione metabolism, including increased GPx4,[8] which protects cells from chemotherapy-induced oxidative stress and that reducing intracellular reactive oxygen species (ROS), especially lipid-orientated ROS (L-ROS), is critical to regulating chemotherapy resistance.[8,41] At the same time, these Pt-R cells are enriched in cholesterol and dependent upon cholesterol uptake. To determine whether cholesterol homeostasis plays a role in regulating cellular ROS levels, the effects of GPx4 and of cholesterol uptake blockade on ROS levels were quantified. First, intracellular ROS levels were measured through 2’,7’-dichlorofluorescin diacetate (DCFDA) staining and found to be decreased in Pt-R versus Pt-S OC cells (Figure 5A, Figure S5A, Supporting Information). Intracellular ROS levels increased if GPx4 was KD (Figure 5B) or inhibited by using the small molecule inhibitor RSL3 (Figure 5C,D). These data support that GPx4 reduces cellular ROS in Pt-R cells, consistent with its known functions.[41]

As GPx4 regulates lipid-dependent anti-oxidant responses, we next examined oxidized membrane lipid levels in OVCAR5 cells transfected with shRNA targeting GPx4 versus shCTRL. Staining with C11 BODIPY showed increased oxidized membrane lipid levels in GPx4 KD compared with control cells (Figure 5E), confirming its role in preventing ferroptosis. To determine whether intracellular cholesterol levels could rescue ferroptosis under conditions of GPx4 depletion, Pt-R OVCAR5 cells under basal conditions (1% FBS) were provided with free choles terol $( 5 0 \mu \mathrm { g } \ \mathrm { m L ^ { - 1 } } , 4 8 \ \mathrm { h } )$ ). Exogenous cholesterol reduced the increased oxidized lipids in GPx4 KD Pt-R OVCAR5 compared with control cells (Figure 5F). Additionally, Pt-R OC cells depleted of GPx4 were less viable under low serum conditions compared with control cells. Addition of exogenous cholesterol rescued GPx4 KD cells (Figure 5G), confirming the dependence of Pt-R cells on cholesterol and GPx4. Likewise, exogenous cholesterol rescued viability in OVCAR5 Pt-S (Figure 5H) and Pt-R cells (Figure 5I) treated with the GPx4 inhibitor, RSL-3, supporting that cholesterol uptake can buffer the toxic effects of increased intracellular ROS. In contrast, inhibition of cholesterol uptake through SR-B1 blockade by using HDL NP induced an increase in ROS levels (Figure 5J).

To further support the connection between SR-B1 and GPx4, we examined the effects of genetic KD of SR-B1 on GPx4 expression level. SR-B1 depletion by siRNA led to a decrease in GPx4 expression as determined by western blot (Figure 5K,L).

A  
![](images/692853b9a1af31b53e479f421fd77b555a4f7e66eedd2bccd27d67b4ef38b377.jpg)

<details>
<summary>text_image</summary>

OVCAR5 Pt-R OVCAR4 Pt-R
GPx4 22 kDa
SR-B1 57 kDa
β-actin 42 kDa
shCTRL shGPx4_1 shGPx4_2 shCTRL shGPx4_1 shGPx4_2
</details>

C  
![](images/7754d159fdf6da33049448e30acf97a483ed95fd0963b92faf9e9e7f85810e14.jpg)

<details>
<summary>line chart</summary>

| Log [Cisplatin] (µM) | shCTRL | shGPx4 |
| --------------------- | ------ | ------ |
| 0                     | 0      | 0      |
| 1                     | 90     | 80     |
| 2                     | 70     | 60     |
| 3                     | 50     | 40     |
| 4                     | 30     | 20     |
| 5                     | 10     | 5      |
| 6                     | 5      | 2      |
</details>

D  
![](images/dcb7894a89ad1801ec32217f601449fefd1d79eb7502411d31d413494ecbaebc.jpg)

<details>
<summary>line chart</summary>

| Log [Cisplatin] (µM) | shCTRL Relative viability | shGPx4 Relative viability |
| --------------------- | -------------------------- | -------------------------- |
| 10^0                  | 100                        | 100                        |
| 10^1                  | ~95                        | ~98                        |
| 10^2                  | ~70                        | ~90                        |
| 10^3                  | ~40                        | ~60                        |
| 10^4                  | ~10                        | ~20                        |
| 10^5                  | ~0                         | ~0                         |
</details>

E  
![](images/fa9a72679b9cc4b4027e6fe446ffe829598ba393a2f9119e71f75ce6aa522c4f.jpg)

<details>
<summary>bar chart</summary>

| Category | -log (P Value) |
| --- | --- |
| HDL-mediated lipid transport Homo sapiens R-'SA-194223 | 3 |
| Visual phototransduction Homo sapiens R-HSA-2187338 7 | 2.5 |
| Metabolism Homo sapiens R-HSA-1430728 | 3.5 |
| PERK regulates gene expression Homo sapiens R-HSA-381042 | 3.5 |
| Metabolism of vitamins and cofactors Homo sapiens R-HSA-196854 | 3.5 |
| ATF6-alpha activates chaperones Homo sapiens R-HSA-381033 | 4 |
| (Interferon Signaling Homo sapiens R-HSA-913531 | 4 |
| ATF6-alpha activates chaperone genes Homo sapiens R-HSA-381183 | 4.5 |
| Unfolded Protein Response (UPR) Homo sapiens R-HSA-381119 | 4.5 |
| Interferon alpha/beta signaling Homo sapiens R-HSA-909733 | 8 |
</details>

F  
![](images/944af0b124a2c59ab380a301597e4c906d9356e77c2924f8a3cfbda455faa536.jpg)

<details>
<summary>bar chart</summary>

| Group   | Cholesterol level (ng/ml/10⁵ cells) |
| ------- | ----------------------------------- |
| shCTRL  | 40                                  |
| shGPx4  | 25                                  |
</details>

G  
![](images/ccd006d51db431c68006b3f1ef4195cad49406bcbd784a35334bac7aed5b7ee7.jpg)

<details>
<summary>bar chart</summary>

| Group   | Cholesterol level (ng/ml/10⁵ cells) |
| ------- | ----------------------------------- |
| shCTRL  | 70                                  |
| shGPx4  | 35                                  |
</details>

H  
![](images/0346a348e3659d46a28feb695b38ff92fe6437f181983ccb56044e23a8ebd0a1.jpg)

<details>
<summary>text_image</summary>

OVCAR5 Pt-S
Stack	Cholesterol
shCTRL
shGPx4
10µm
</details>

![](images/746d52aec9903e96a77b8d7af8ae112986b0654e59f33b49683c7b752fceb4e3.jpg)

<details>
<summary>violin chart</summary>

| Group | Relative cholesterol amount |
|-------|-----------------------------|
| shCTRLshGPx4 | 1.0 |
| shCTRLshGPx4 | 1.5 |
</details>

![](images/77b860ab4c9afda66d691f2c61ff56c188d734c4184fb6b195d8753137d7fe64.jpg)

<details>
<summary>text_image</summary>

OVCAR5 Pt-R
Stack	Cholesterol
shCTRL
shGPx4
10µm
</details>

K  
![](images/64b20f225793c8544810a597f873a88605b7779f01cc54dfd13e9235f05f622e.jpg)

<details>
<summary>violin chart</summary>

| Group    | Relative cholesterol amount |
| -------- | --------------------------- |
| shCTRL   | 1.8                         |
| shGPx4   | 0.6                         |
</details>

L  
![](images/728a9b76520832733e8442ba0e8d8bdb6ded39a219528df3deffa34dcc5b9880.jpg)

<details>
<summary>bar chart</summary>

| Group       | MFI TF Cholesterol |
| ----------- | ------------------ |
| shCTRL      | 9000               |
| shGPx4_1    | 7000               |
| shGPx4_2    | 6500               |
</details>

M  
![](images/15d63c77c5abf2baae03e767af79cd85ead79eee5e4b059d64a799145223e11b.jpg)

<details>
<summary>bar chart</summary>

| Group       | MFI TF Cholesterol |
| ----------- | ------------------ |
| shCTRL     | 21000              |
| shGPx4_1   | 16500              |
| shGPx4_2   | 17000              |
</details>

Figure 4. GPx4 inhibition re-sensitizes OC cells to platinum chemotherapy through reduction of cholesterol uptake. A,B) Western blot shows GPx4, SR-B1, and ??-actin (loading control) protein levels in OVCAR5 Pt-R (left panel) and OVCAR4 Pt-R (right panel) cells transduced with shRNAs targeting GPx4 (shGPx4) or control shRNAs (shCTRL). shGPx4\_1 and $s { \mathsf { h C P } } \times 4 \_ 2$ represent different shRNA sequences. C,D) Cell viability assays measured surviving OVCAR5 (C, n = 5 replicates), OVCAR4 (D, n = 3 replicates) Pt-R cells after treatment with cisplatin (various concentrations). E) Reactome analysis of top molecular pathways associated with differentially downregulated genes measured by RNAseq $( \mathsf { F D R } < 0 . 0 5 , n = 3 )$ in OVCAR5 Pt-R cells transduced with

Combined, these results support that GPx4-mediated cellular redox homeostasis in OC cells is linked to SR-B1 expression levels and cholesterol accumulation, providing a rationale for targeting cholesterol uptake in Pt-R cancer cells to induce ferroptosis.

## 2.6. GPx4 Blockade Inhibits SREBF2 Mediated SR-B1 Expression in OC Cells

To further study the molecular mechanism by which increased GPx4 maintains high SR-B1 expression and cholesterol uptake in OC cells, we examined GPx4 related transcriptomic signatures in Pt-R OVCAR5 cells by comparing GPx4 KD versus control cells. Protein-Protein Interaction (PPI) analysis identified top transcriptional regulators enriched among the downregulated DEGs in GPx4 KD OC cells. The histone acetyltransferase EP300 was the most significantly suppressed transcriptional regulator in GPx4 KD cells (Figure 6A). We validated down-regulation of EP300 expression in OVCAR5 Pt-R cells in which GPx4 was KD through qRT-PCR (Figure 6B).

Among the key TFs involved in regulating SR-B1 expression and cholesterol metabolism are the sterol regulatory binding factors 1 and 2 (SREBFs, also referred to as SREBPs) encoded by the SREBF 1 and 2 genes.[42,43] We found a strong correlation between the SR-B1 and SREBF2 or 1 expression levels in HG-SOC tumors profiled by TCGA (Figure 6C, R = 0.34, p = 2.5 e-11; Figure S5B, Supporting Information, R = 0.26, p = 5e-07). While the two related TFs have somewhat overlapping functions, SREBF2 was linked with regulation of key genes in cholesterol metabolism, while SREBF1 was shown to regulate genes in the fatty acid synthesis pathway[44] and SREBF2 was found to be a more potent regulator of SR-B1 transcription as compared with SREBF1.[43] Therefore, in subsequent studies we focused on SREBF2. This TF was downregulated in OC cells in which GPx4 was KD (Figure 6D), suggesting a potential link between GPx4 and SREBF2.

To uncover the mechanism by which SREBF2 was downregulated in GPx4 KD cells, especially given the substantial inhibition of EP300 in these cells, we investigated potential epigenetic regulation of SREBF2 by EP300 in the GPx4 KD cells. Previous studies showed acetylation of H3K27 in the promoter region of the SREBF2 gene in OVCAR5 cells[45] and other cell lines analyzed in the ENCODE dataset (GM12878 and HEK293T)[46,47] (Figure 6E and Figure S5C, Supporting Information), suggesting conserved regulation of the SREBF2 gene by H3K27Ac. Cut&Tag sequencing using an H3K27Ac antibody detected a reduction of H3K27Ac enrichment at the SREBF2 promoter in OC cells in which GPx4 was KD (hg38\_dna range = chr22: 41 831600-41833300, Figure 6E). ChIP-qPCR using an antibody against H3K27Ac, with primers flanking the known H3K27Ac peak in the SREBF2 promoter (hg38\_dna range = chr22:41831994-41832707\_region 2; chr22:41832517- 41833087\_region 3; Figure 6E) confirmed H3K27ac enrichment in the SREBF2 promoter region compared with a control region (hg38\_dna range: chr22:41830626-41830921\_region 1; Figure 6F,G), as well as reduction of H3K27ac enrichment in cells in which GPx4 was KD. In contrast, GPx4 KD had little impact on H3 enrichment on the promoter region of SREBF1 (Figure S5C, Supporting Information). Thus, H3K27Ac deposition enriched in the promoter region of SREBF2, was significantly inhibited in cells in which GPx4 was KD. These data support that OC cells in which GPx4 is KD, harbor increased ROS levels, decreased EP300 expression resulting in reduced histone acetylation on the SREBF2 promoter and suppressed SR-B1 expression, as illustrated in Figure 6H.

## 3. Conclusion

The development of resistance to Pt-based chemotherapy is challenging because of the lack of effective treatments for resistant cancers. The Pt-R OC phenotype requires increased enzymatic detoxification of L-ROS, which involves changes in fatty acid and cholesterol metabolism. Our data reveal that Pt-R OC requires increased cholesterol uptake through SR-B1 and increased activity of the glutathione (GSH)-dependent GPx4 enzyme that reduces cell membrane L-ROS. Knocking down GPx4 caused changes in SREBF2 activity, a key regulator of SR-B1 expression. This regulatory axis was therapeutically targeted using a novel synthetic ligand of SR-B1. HDL NP. We show that HDL NPs binding SR-B1 in Pt-R OC models inhibit cell cholesterol uptake and drastically reduce GPx4 expression, increase L-ROS, and cause cell death through ferroptosis in vitro and in vivo. Therefore, targeting cell membrane anchored SR-B1 and cholesterol uptake is a powerful way to disrupt redox pathways required for the survival of Pt-R OC cells and tumors.

Biochemical and transcriptomic profiling reveal that Pt-R OC cells harbor increased intracellular cholesterol and express higher levels of the transporter SR-B1, while downregulating pathways related to de novo cholesterol biosynthesis. High expression of SR-B1 in HGSOC was reported by others.[14,48] The data suggest increased reliance of Pt-R cells upon crHDL binding SR-B1 and support the concept that acquired changes in lipid metabolism are required cellular adaptations to reduce the toxicity induced by Pt and excess L-ROS. This phenomenon is detectable in other cancers. Some lymphomas are auxotrophic for cholesterol because of hypermethylation and silencing or mutation of de novo cholesterol biosynthesis genes.[40] Accumulation of cholesteryl esters has also been reported in PTEN-null prostate cancer being associated with increased aggressiveness,[13] and dependence on cholesterol uptake through SR-B1 was described in clear cell renal cell carcinoma.[35] The latter is notoriously resistant to chemotherapy and auxotrophic for cholesterol from

shRNAs targeting GPX4 (shGPx4) versus cells transduced with control shRNAs (shCTRL). F,G) Amplex Red cholesterol assay measured total intracellular cholesterol levels/105 cells (mean ± SD, n = 3) in shGPx4 versus shCTRL OVCAR5 Pt-S (F) and Pt-R (G) OC cells. H–K) Representative SRS images (left) and unmixed cholesterol channel signal images (right) of shCTRL and shGPx4 OVCAR5 Pt-S (H) and Pt-R (J) OC cells. Quantification of relative amounts of cholesterol channel signal intensity (mean ± SD, n = 3) in shCTRL and shGPx4 OVCAR5 Pt-S (I) and Pt-R (K) OC cells. L,M) Cholesterol uptake measured by TopFluor Cholesterol flow cytometry in shGPx4 and shCTRL OVCAR5 Pt-S (L) and Pt-R (M) cells (mean ± SD, n = 3). For all panels, $\ddot { \ast p } < 0 . 0 5 , \ddot { \ast \ast p } < 0 . \dot { 0 } 1 , \ddot { \ast \ast \ast p } < 0 . 0 0 1$ .

A  
![](images/bc9268596506785637222ccf536137b09fac936d57f1917c2206a831f8e6ab07.jpg)

<details>
<summary>bar chart</summary>

| Group | ROS-DCFDA MFI |
|-------|---------------|
| Pt-S  | 550           |
| Pt-R  | 520           |
</details>

B  
![](images/124042ee6557918d2715263050aa07417f3478aa8ffdc67669033c842af8eaf6.jpg)

<details>
<summary>line chart</summary>

| ROS-DCFDA (FITC) | shCTRL | shGPx4_1 | shGPx4_2 |
| ---------------- | ------ | -------- | -------- |
| Value            | 0      | 0        | 0        |
</details>

OVCAR5 Pt-R  
![](images/eae308ca77131b7b9a8d402ea076a24fdaea3795175de6eebfbb3a8e3fff0ace.jpg)

<details>
<summary>bar chart</summary>

| Group      | ROS-DCFDA MFI |
| ---------- | ------------- |
| shCTRL     | 3500          |
| shGPx4_1   | 5500          |
| shGPx4_2   | 8500          |
</details>

C  
OVCAR5 Pt-S  
![](images/66d2cb7ef5c5407d4afbe8effd572536e3babe16ecbaefdffa276110a99fe140.jpg)

<details>
<summary>text_image</summary>

DMSO RSL-3
GPX4 22 kDa
□tubulin 55 kDa
</details>

D  
OVCAR5 Pt-S  
![](images/e1abaac724d50e5befe1685a520179440804764b88100b4195f9fcb7fb519849.jpg)

<details>
<summary>bar chart</summary>

| Group | Relative ROS-DCFDA |
|-------|---------------------|
| DMSO  | 2.8                 |
| RSL-3 | 5.0                 |
</details>

E  
OVCAR5 Pt-S  
![](images/15257eb122de4f0163b631f8d2c2f703e4ec283a9ce06a45ba3d43ea39c62963.jpg)

<details>
<summary>line chart</summary>

| FITC | shCTRL | shGPx4_1 | shGPx4_2 |
|------|--------|----------|----------|
| Value | Peak   | Peak     | Peak     |
</details>

![](images/407cd9473e46f513f626d1c0e8499b41ce3df04667598d491791a0a735c9c5ae.jpg)

<details>
<summary>bar chart</summary>

| Group      | Fold change of oxidized lipid |
| ---------- | ----------------------------- |
| shCTRL     | 1.0                           |
| shGPx4_1   | 1.3                           |
| shGPx4_2   | 1.3                           |
</details>

F  
OVCAR5 Pt-R  
![](images/9e78068d18917dfceb183dfd535b53b866a9f3e084a803daf9174872cf97f4fa.jpg)

<details>
<summary>bar chart</summary>

| Group   | Oxidized/Reduced C11 BODIPY |
| ------- | --------------------------- |
| shCTRL  | 12                          |
| shGPx4  | 23                          |
</details>

G  
OVCAR5 Pt-R  
![](images/ec033705713cc79337060eb9ad1e13d948dc0f9587c41a8a7abf0324a45569ac.jpg)

<details>
<summary>bar chart</summary>

| Group   | DMSO  | Cholesterol |
|---------|-------|-------------|
| shCTRL  | 3.3   | 2.4         |
| shGPx4  | 3.3   | 1.7         |
</details>

H  
OVCAR5 Pt-S

![](images/5414e48b4b478ddd0dfd16d3766677328b96b2913b5ca149381c34919cb8232d.jpg)

<details>
<summary>bar chart</summary>

| Treatment Group | Viability (OD450) |
| --------------- | ------------------ |
| DMSO            | 100                |
| RSL-3           | 80                 |
| RSL-3 + Cholesterol | 95             |
</details>

OVCAR5 Pt-R  
![](images/32d7ba1d2c89edc9eb5c77b6a25e03be82a26976b7504b7c5efaa90ebf7b4067.jpg)

<details>
<summary>bar chart</summary>

| Treatment        | Viability (OD450) |
| ---------------- | ------------------ |
| DMSO             | 100                |
| RSL-3            | 85                 |
| RSL-3 + Cholesterol | 100                |
</details>

J  
OVCAR5 Pt-S  
![](images/5e7f4dfc6a3cf30764dd8c2280fcc8f4262d77b8a2d88e70e20c807460934201.jpg)

<details>
<summary>line chart</summary>

| ROS-DCFDA (FITC) | Count |
| ---------------- | ----- |
| -10^3            | 0     |
| 0                | 0     |
| 10^3             | Peak  |
| 10^4             | 0     |
| 10^5             | 0     |
</details>

K  
![](images/d986cd00128c4ee76b1b42525bbc6d9e5d52d2fc80bc9e5eeb288bd2c6381263.jpg)

<details>
<summary>bar chart</summary>

| Group | ROS-DCFDA MFI |
|-------|---------------|
| PBS   | 25            |
| HDL NP| 55            |
</details>

OVCAR5 Pt-S  
![](images/1f1fbdc69b34f84b04c002c831ca06eb9235bcd6c2c462b63b3c41fec1eab668.jpg)

<details>
<summary>other</summary>

| Treatment     | Value  |
| ------------- | ------ |
| Untreated     | 1      |
| Lipo.         | 1.48   |
| si-Control    | 2.55   |
| si-SR-B1      | 0.20   |
| Untreated     | 1      |
| Lipo.         | 1.17   |
| si-Control    | 1.96   |
| si-SR-B1      | 0.96   |
</details>

SR-B1 57 kDa  
GPx4 22 kDa  
β-actin 42 kDa

L  
OVCAR5 Pt-R  
![](images/c5ce17ebcfbb9de00759448160b04c1e9e2c1cb71db4e442b6eb3606c3d029af.jpg)

<details>
<summary>other</summary>

| Condition     | SR-B1 (kDa) | GPx4 (kDa) | β-actin (kDa) |
| ------------- | ----------- | ---------- | ------------- |
| Untreated     | 57          | 22         | 42            |
| Lipo.         | 1.68        | 1.49       | 0.80          |
| si-Control    | 0.86        | 0.35       | 0.35          |
| si-SR-B1      | 0.00        | 0.35       | 0.35          |
</details>

Figure 5. GPx4-mediated cholesterol accumulation maintains cellular redox homeostasis in OC cells. A) Quantification of intracellular ROS levels in OVCAR5 Pt-S and Pt-R OC cells. ROS levels are represented by mean DCFDA fluorescence intensity $( \pm \mathsf { S D } , n = 3 )$ as quantified with a fluorescence plate reader at $\mathsf { E x } / \mathsf { E m } = 4 8 5 / 5 3 5$ nm. B) Histograms (left) and quantification of intracellular ROS levels with DCFDA (right) in OVCAR5 Pt-R cells transduced with shRNAS directed at GPx4 (shGPx4\_1 and shGPx4\_2) or control shRNA (shCTRL). Results show mean $\pm \mathsf { S D } \left( n = 3 \right)$ of DCFDA fluorescence intensity quantified by flow cytometry. C) Western blot measures GPx4 and ??-tubulin (loading control) protein levels in OVCAR5 Pt-S cells treated with DMSO or

exogenous sources. In fact, renal cell carcinoma demonstrates a “clear cell” pathophysiology due to reduced de novo cholesterol biosynthesis, uptake of HDL cholesterol through SR-B1[49] and cholesterol stored in lipid droplets.

It has been proposed that intracellular cholesterol and cholesterol-pathway intermediates play critical roles in maintaining redox homeostasis and can protect cells from excess ROS,[50,51] but the mechanism is not clear. Cholesterol metabolism and accumulation of lipids have been shown to prevent cell death along with increasing the expression of GPx4, a potent antioxidant protein and inhibitor of ferroptosis.[52] On the other hand, GPx4 inhibition was shown to induce cell death through a process dependent upon oxidized phospholipids (ferroptosis) which uniquely target treatment-resistant cancer cells.[8,53] Examples of cholesterol uptake dependent cancers that are highly sensitive to targeted GPx4 inhibitors are clear cell renal carcinoma, lymphomas, and leukemias.[35] Under certain circumstances, GPx4 can be inhibited by disruption of de novo cholesterol synthesis (e.g., using statins) resulting in increased ferroptosis. This is thought to occur because GPx4 contains selenocysteine residues which are activated during protein synthesis by isopentenyl-5-pyrophosphate, an intermediate of the mevalonate pathway of cholesterol synthesis.[54]

Here we show that targeting cholesterol uptake in Pt-R OC models by using HDL NP decreased cancer cell viability and blocked tumor growth. A main mechanism of cytotoxicity in these OC models adapted to surviving under high ROS conditions was induction of ferroptosis. Flow cytometry experiments employing the membrane localizing C11-BODIPY fluorophore reagent whose fluorescence is modified upon oxidation demon strated that addition of HDL NPs results in a significant increase in cell membrane localized oxidation. Pt-R OC cell death could be rescued by addition of the lipophilic cell membrane localizing antioxidant ferrostatin-1 or the iron chelator deferoxamine which depletes iron rendering it unavailable as a co-factor for lipid oxidation. Levels of GPx4 were significantly reduced in Pt-R cells after treatment with HDL NP. Furthermore, by depleting GPx4, HDL NPs sensitized Pt-R cells to carboplatin. These observations are consistent with prior results from our group testing HDL NP [30,39,55]

There is a strong relationship between enhanced uptake of cholesterol by chemotherapy resistant cancer cells and the requisite high expression of GPx4 to prevent lipid peroxidation and cell death by ferroptosis. Interestingly, prior data suggest that cholesterol modulation of cell membrane fluidity and lipid raft formation was important for modulating the diffusion of membrane localized substrates for oxidation and cell sensitivity to GPx4-mediated ferroptosis.[36,56] These reports suggest the possibility that HDL NP induced ferroptosis is triggered by modulating membrane fluidity and lipid rafts to enhance cell membrane lipid peroxidation. Our past work supports that HDL NPs also enhance cholesterol efflux from the cell membrane after binding SR-B1 and that this disrupts membrane lipid rafts.[26] Thus, aside from restricting cholesterol uptake, HDL NPs could also reduce cell membrane cholesterol and modulate membrane fluidity and lipid rafts to facilitate ferroptosis. Here we show that replenishment of cholesterol stores in Pt-R OC cells rescues ferroptosis induced by GPx4 knockdown or inhibition, consistent with this mechanism.

Accumulation of cholesterol in chemoresistant cancer cells, highly enriched in antioxidant molecules such as GPx4,[8] remains unexplained. Here we show that GPx4 expression levels, which reduce intracellular ROS induced by exposure to chemotherapy, are directly correlated with cholesterol uptake and intracellular cholesterol stores. We propose epigenetic repression of SREBF2 as a potential mechanism by which GPx4 modulated redox balance in Pt-R OC cells alters cholesterol uptake. SREBF2 is a transcription factor that directly regulates the expression of the HDL transporter SR-B1 exerting more potent effects than the related factor SREBF1.[43] Under high ROS levels caused by GPx4 knockdown, expression of the EP300 histone acetyltransferase is downregulated, leading to decreased histone acetylation at the SREBF2 promoter and reducing its expression levels. Regulation of EP300 by GPx4 and ROS levels is consistent with previous observations supporting that oxidative stress could alter epigenetic mechanisms regulating transcription.[57–59] Our results establish a link between redox balance, histone acetylation, and cholesterol metabolism. We recognize that EP300 downregulation could have more global transcriptional effects.

Our data detail a pathway whereby Pt resistance is enabled by an increased cell membrane requirement for cholesterol through crHDL binding SR-B1 and increased expression of the antioxidant enzyme. GPx4. A synthetic ligand of SR-B1. HDL NP. that targets cell membrane cholesterol and the uptake of cholesteryl esters induces cell death by ferroptosis. Single-agent efficacy is possible due to reduced cholesterol and cholesteryl ester delivery to the cell and reduced expression of GPx4. An epigenetic mechanism links the antioxidant protein, GPx4 to key regulators of cholesterol metabolism. We anticipate that the dual mechanism through which HDL NPs induce ferroptosis will be therapeutically relevant to other human cancers that are highly resistant to chemotherapy and radiation.

the GPx4 inhibitor RSL-3 (200 nm, 48 h, n = 3). D) Intracellular ROS levels in OVCAR5 Pt-S OC cells treated with RSL-3 (1 um, 4 h) versus DMSO, detected by DCFDA fluorescence and quantified with a fluorescence plate reader. E) Assessment of intracellular lipid peroxidation using BODIPY 581/591-C11. Histograms of fluorescence intensities (left) and fold-change of fluorescence intensities (mean ± SD, n = 3) (right) in shGPx4 versus shCTRL OVCAR5 Pt-S OC cells. F) Effects of cholesterol (50 μg mL−1 for 48 h) on percentage of oxidized/reduced lipids measured by flow cytometry of C11 BODIPY in shCTRL and shGPx4 OVCAR5 Pt-R cells cultured in low serum conditions (1% FBS) (mean ± SD, n = 3). G) Viability of OVCAR5 Pt-R cells, cultured in full serum (10% FBS), basal conditions (1% FBS), and 1% FBS + cholesterol (50 μg mL−1). Cell viability was measured with the CCK8 assay at 48 h (mean ± SD, n = 3–5 replicates). H,I) Viability of OVCAR5 Pt-S (H) and Pt-R (I) OVCAR5 OC cells, cultured in low serum conditions (1% FBS), and treated with DMSO, GPx4 inhibitor RSL-3 (200 nm) or RSL-3 plus cholesterol (50 μg mL−1) combination. Cell viability was measured with the CCK8 assay at 96 h (Pt-S) or 48 h (Pt-R) (mean $\mathsf { i } \pm \mathsf { S D } , \mathsf { n } = 3 { - } 5 \mathsf { ) } . \mathsf { j } )$ ) Histograms (left) and quantification of intracellular ROS levels (right) by DCFDA fluorescence intensity determined by flow cytometry (mean ± SD, n = 3) in OVCAR5 Pt-S OC cells treated with PBS or HDL NPs (40 nm, 24 h). K,L) Western blot analysis of SR-B1, GPx4, and ??-actin (loading control) in OVCAR5 Pt-S (K) and Pt-R (L) cells transfected with siRNA against SR-B1. Band intensity was measured with Image J and is indicated below each blot. For all panels, $^ { * } p < 0 . 0 5 , ^ { * * } p < 0 . 0 1 , ^ { * * * } p < 0 . 0 0 1$ .

A  
![](images/35d8b9f02efcb3b628e21df231f7725cb8e92d7dd36539cb7bf09e9cb79a8735.jpg)

<details>
<summary>bar chart</summary>

| Transcription Factor | PPIs |
| --- | --- |
| EP300 | 2.7 |
| BATF | 2.5 |
| JUNB | 2.2 |
| HNF4A | 2.1 |
| SIRT3 | 1.1 |
| JUND | 1.1 |
| NFKB1 | 1.1 |
| ATF3 | 1.1 |
| ASTAT1 | 1.0 |
| USF2 | 1.0 |
</details>

B  
![](images/d0a6f341666183d88837fca02064c01ccff2a82e00bb4c7c3a761fed1ebc6b36.jpg)

<details>
<summary>scatterplot</summary>

| Group      | Log2 fold change |
| ---------- | ---------------- |
| shCTRL     | -0.2             |
| shGPx4_1   | -0.8             |
| shGPx4_2   | -0.6             |
</details>

C  
![](images/68e95cd8c45591efb19cc30eb91f344ea684a2fa8abce029fb183bab93fe8432.jpg)

<details>
<summary>scatterplot</summary>

| Log₂ (SR-B1 TPM) | Log₂ (SREBF2 TPM) |
| ---------------- | ----------------- |
| 2                | 3                 |
| 4                | 5                 |
| 6                | 6                 |
</details>

D  
![](images/4ec3ea6057a0af25ba309f44b643dacba051865d5ab8a7546ecffd9be2486587.jpg)

<details>
<summary>scatterplot</summary>

| Gene   | shCTRL | shGPx4 |
|--------|--------|--------|
| GPx4   | 1.3    | 0.1    |
| SREBF2 | 1.2    | 0.3    |
</details>

E  
![](images/890276daa7fc8e1d235e839326b73f2eb643f07e93a66e4514c4102628e85129.jpg)

<details>
<summary>other</summary>

| Region | Gene Sequence | Significance |
|--------|---------------|--------------|
| Control | chr22:41830626-41830921 | High |
| Region 1 | chr22:41830626-41830921 | High |
| Region 1 | chr22:41831994-41832707 | High |
| Region 1 | H3K27Ac_Peak | High |
| Region 1 | chr22:41832517-41833087 | High |
| Region 1 | H3K27Ac_Peak | High |
</details>

F  
![](images/3edfce054f1c992563c93bb52d280889220563e6502dcd6e900d404285edf979.jpg)

<details>
<summary>bar chart</summary>

| Group           | % of input |
| --------------- | ---------- |
| shCTRL control  | ~50        |
| shCTRL peak     | ~800       |
| shGPx4 control  | ~50        |
| shGPx4 peak     | ~150       |
</details>

G  
![](images/442527a8c2b1cc7c3becdf331018dd41cacb33ca74f54f29e44fccf114cfc4bb.jpg)

<details>
<summary>bar chart</summary>

| Group           | % of input |
| --------------- | ---------- |
| shCTRL control  | ~100       |
| shCTRL peak     | ~500       |
| shGPx4 control  | ~100       |
| shGPx4 peak     | ~150       |
</details>

![](images/c1bac3ca70ec4d15c987cbaddec0a0a98738def6b413ce7ee649e491f0cd4f2f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Lipid-O"] --> B["Periophus"]
  B --> C["ROS"]
  C --> D["EP300"]
  D --> E["H3K27Ac"]
  E --> F["SREBF2"]
  F --> G["SCARB1"]
  G --> H["HDL NPs"]
  I["Lipid-OH"] --> J["RSL3"]
  J --> K["IGPX4"]
  K --> L["GSH"]
  L --> M["GSSR"]
  M --> N["Lipid-OOH"]
  N --> O["cholesterol"]
  O --> P["oral tissue"]
  P --> Q["SCARB1"]
  Q --> R["HDL NPs"]
  R --> S["cholesterol"]
```
</details>

Figure 6. GPx4 knock down inhibits SR-B1 expression through decreased H3K27Ac on SREBF2 promoter. A) Protein-protein interactions (PPIs) analysi of top TFs binding targets in the downregulated DEGs of OVCAR5 Pt-R cells transfected with shRNAs targeting GPx4 (shGPx4) versus shCTRL cells. Gene expression was measured by RNA-seq (n = 3). B) Measurements by qRT-PCR of EP300 mRNA in shGPx4 versus shCTRL OVCAR5 Pt-R cells (mean $\pm \mathsf { S D } , n = 3 )$ . Results include two shGPx4 sublines. C) A scatter plot shows the correlation between expression levels of SCARB1 and SREBF2 in HGSOC specimens from TCGA The Pearson’s correlation coefficient (r) and p-value are indicated $( n = 3 7 0 )$ . D) GPx4 and SREBF2 mRNA expression in shGPx4 versus shCTRL OVCAR5 Pt-R cells measured by qRT-PCR (means ± SD, n = 3). E) UCSC Genome Brower on Human GRCh38/hg38 tracks of the H3K27Ac binding peak in the SREBF2 gene in OVCAR5 cells[45] and other cell lines previously recorded in the ENCODE dataset (GM12878, and HEK293T).[46,47 The H3K27Ac binding motif indicated along with the position of primer sequences (Primer\_2,3) used for q-PCR are shown. Amplification of a sequence 1 kb downstream was used as a control (Primer\_1). F,G) ChIP-PCR shows H3K27Ac enrichment in the SREBF2 gene (primer\_2 (F) and primer\_3 (G)) in shCTRL versus shGPx4 OVCAR5 Pt-S cells. Enrichment of H3K27Ac on a sequence 1 kb downstream was used as a control (Primer\_1) (mean ± SD, n = 3). H) Model shows mechanism interconnecting cholesterol and anti-redox pathway. For all panels, $^ { * } p < 0 . 0 5 ; ^ { * * } p < 0 . 0 1 ; ^ { * * * } p < 0 . \dot { 0 } \dot { 0 } \rceil )$ ).

## 4. Experimental Section

Human Specimens: Deidentified high grade serous ovarian tumors (HGSOC) were collected and processed fresh from consenting patients (Northwestern University IRB#: STU00202468). Human tumor tissues and OC xenografts were enzymatically disassociated into single cell suspensions and cultured as previously described $( n = 6 ;$ see Supporting [ 8,60 ]

Cell Culture: OVCAR5 cells were a generous gift from Dr. Marcus Pe ter, Northwestern University; OVCAR4 cells were from Dr. Mazhar Adli, Northwestern University; immortalized human fallopian tube epithelial cells (FT190) were from Dr. R. Drapkin of University of Pennsylvania;[61] normal endometrial cells (NoEM)[38] were from Dr. Serdar Bulun, Northwestern University, and IOSE cells were from Dr. N. Auersperg,[62] University of British Columbia. Peo1 and Peo4 cells were purchased from Sigma Aldrich. Cells were maintained in a $3 7 ^ { \circ } \mathsf { C }$ incubator with 5% ${ \mathsf { C O } } _ { 2 } .$ Low passage cells were used, and all cell lines were tested to be pathogen and Mycoplasma negative (Charles River Research Animal Diagnostic Services). Peo1 and Peo4 cells were cultured in RPMI-1640 with L-glutamine (Corning, Cat#10-040-CV) plus 10% FBS, 1% GlutaMAX (Gibco, Cat# 35050– 061), 2 mM Sodium Pyruvate (Gibco, Cat# 11360-070), and 1% penicillinstreptomycin. OVCAR5 and OVCAR4 Pt-S and Pt-R cells were maintained in RPMI-1640 with L-glutamine (Corning, Cat# 10-040-CV) plus 10% FBS, 1% GlutaMAX, and 1% penicillin-streptomycin. Primary patient tumor derived cells were maintained in DMEM with L-glutamine, $4 . 5 \ \mathrm { g } \ \lfloor - \rceil$ glucose, without sodium pyruvate (Corning, Cat#10-017-CV) plus 10% FBS, 1% GlutaMAX, and 1% penicillin-streptomycin. Primary human fallopian tube epithelial cells (HFTEC) were purchased from Lifeline Cell Technology (Frederich, MD) and cultured in the complete ReproLife Reproductive Medium (Lifeline Cell Technology, Cat# LL-0068). Pt-R sublines of OV-CAR4 and OVCAR5 OC cells were developed through repeated exposure to 3 or 4 equal or increasing doses of cisplatin or carboplatin for 24 h, as described previously (see Supporting Information).[8]

Chemicals and Reagents: RSL3 was purchased from Fisher Scientific (Cat# 611 810). Atorvastatin was from Selleck Chem (Cat# S5715). Cisplatin (Cat# 1 134 357), carboplatin (Cat# C2538), and cholesterol (Cat# C3045) were from Sigma-Aldrich.

HDL NP Synthesis: HDL NPs were synthesized and quantified as described previous $| \mathsf { y . } ^ { [ 2 7 , 3 7 ] }$ An aqueous solution of 5 nm diameter citrate stabilized gold nanoparticles (AuNP) (75 nm, Nanocomposix) was surface-functionalized with purified human apolipoprotein A-I (apoA-I) (1.3 mg $\mathsf { m L } ^ { - 1 }$ MyBiosource, MBS135961, fivefold molar excess). The AuNP/ apoA-I mixture was incubated on a flat bottom shaker at 60 rpm for 1 h at room temperature (RT). Next, 100% ethanol was added to AuNP/ apoA-I mixture to bring the concentration of ethanol to 20%. Then two different phospholipids, 1,2-dipalmitoyl-snglycero-3-phosphoethanolamine-N-[3-(2-pyridyldithio) propionate] (PDP PE) (Avanti Polar Lipids #870205P) and 1,2-dipalmitoyl-sn-glycero-3- phosphocholine (DPPC) (Avanti Polar Lipids #850355P), both dissolved in ethanol (1 mM), were added to the solution at a final concentration that is 250-fold molar excess to AuNP. PDP PE was added first in order to facilitate binding to the AuNP through the thiolate bond, and the DPPC solution was added second. These HDL NPs were incubated on a flat bottom shaker at 60 rpm overnight at RT followed by purification by tangential flow filtration (TFF: KrosFlo Research KRi2 TFF System, Repligen, model 900–1613). HDL NPs were stored ${ \sf a t } 4 ~ ^ { \circ } \mathsf C$ until use. UV–vis spectroscopy (Agilent 9453) and Beer’s Law were used to measure the concentration of HDL NPs where 5 nm AuNPs have a characteristic absorption at $\lambda _ { \operatorname* { m a x } } =$ 520 nm and extinction coefficient of $9 . 6 9 6 \times 1 0 ^ { 6 } ~ \mathsf { M } ^ { - 1 } ~ \mathsf { c m } ^ { - 1 }$

Cell Viability Assay: Cell viability was evaluated using the Cell Counting Kit 8 assay (CCK8, Dojindo Molecular Technologies, Cat# CK04, Rockville, MD, USA) following the manufacturer’s recommendations. Absorbances (450 nm) were measured with a microplate reader (BioTek ELX800, BioTeK, Winooski, VT). For experiments using HDL NPs, cell viability was measured with MTS assays (CellTiter, Promega, Madison, WI) as previously described.[63] Cells were plated at 500 cells $\mathsf { w e } | | \mathsf { - } |$ in 96-well plates and treated with PBS or HDL NP for 72 or 96 h depending on cell line. For ferroptosis experiments, cells were additionally treated with a final concentration of 1 μm of ferrostatin-1 or deferoxamine (DFO) (Sigma). For statin experiments, cells were treated with 2.5 or 5 μm atorvastatin (Cayman Chem). For synergy of carboplatin and HDL NPs, OVCAR5 Pt-R cells were treated with 3.125, 6.25, 12.5, 25, 50, or 100 nm HDL NP and/or 3.125, 6.25, 12.5, 25, 50, or 100 μm carboplatin. $1 \mathsf { C } _ { 5 0 }$ values were calculated using GraphPad Prism and the combination index was calculated using the method of Chou-Talalay.[64]

Cisplatin Half Maximal Inhibitory Concentration $( I C _ { 5 0 } ) { : }$ : Five thousand cells per well were seeded in 96-well plates and treated with different concentrations of cisplatin: 0, 0.5, 1, 2.5, 5, 10, 25, 50, 75, 100, 250, and 500 μM for 24 h. Cell viability was measured at 72 h post-cisplatin treatment by a CCK8 assay. $1 \mathsf { C } _ { 5 0 }$ values were calculated using GraphPad Prism software as described previously.[8]

In Vivo Experiments: Animal studies were conducted according to protocol # IS00017063 approved by the Institutional Animal Care and Use Committee of Northwestern University. Two million Pt-R OVCAR5 cells were injected intraperitoneally (i.p.) into female, 6–8 weeks old, nude mice (Foxn1nu, Envigo). 3 days after cell injection, mice were randomized and administered daily (Monday through Friday, 2 days off) i.p. treatments of 200 μL PBS (control) or HDL NP (1 μm) for 4 weeks. Mice were weighed biweekly and euthanized the day after the last treatment. Tumors were counted, measured and weighed. Tumors were enzymatically digested to obtain single cell suspension for lipid peroxidation analysis using C-11 BODIPY staining. For the PDX model, fresh tumor tissue resected from subcutaneously engrafted ovarian PDX growing in NSG $\mathsf { m i c e } ^ { [ 6 5 ] }$ was sliced, minced, and quickly digested with 1.5 mg mL−1 collagenase IV (Millipore Sigma cat#C7657-500MG), 50 μg $\mathrm { m } \lfloor { - } \rceil$ dispase (Thermo Fisher Scientific cat#17 105 041), 50 μg $\mathsf { m L } ^ { - 1 }$ liberase (Millipore Sigma cat#5 401 119 001), and 0.1 mg mL−1 DNase I (Thermo Fisher Scientific cat#EN0521) in Hanks Balanced Salt Solution (Thermo Fisher Scientific cat#88 284) in a shaker (Thermo Scientific MaxQ 8000 Incubated Stackable Shakers) at 250 rpm and $3 7 ^ { \circ } \mathsf { C }$ for 2 h. The digested tissue was passed through a 100 μm cell strainer (Corning Fisher Scientific cat#431 752) and the cell suspension was centrifuged, washed twice with Dulbecco’s PBS and reconstituted for cell counting. The cell suspension was mixed with 20% matrigel. $2 \times 1 0 ^ { 6 }$ cells in 100 μL solution were injected i.p. using a 25 G needle. After 2 weeks, the 14 mice were randomly divided into two groups: control (PBS) and HDL NP $( 7$ mice per group) and treated with either HDL NP (1 μm) or 1xPBS daily from Monday to Friday for 10 weeks. Body weights were monitored twice a week. All mice survived to the experimental end point (10 weeks). At necropsy, tumors were counted, measured, and weighed. All primary tumor tissue and organs were processed (fixed in 10% formalin, embedded in paraffin) and sectioned for histologic examination. Tumor histology was examined as previously described.[66]

Large-Area Hyperspectral SRS Imaging: Multiplex Stimulated Raman Scattering (SRS) was performed by a femtosecond laser with two synchronized outputs beams (Insight DeepSee, Spectra-Physics, Santa Clara, CA, USA) and images was taken and analyzed using ImageJ as described previously (see Supporting Information).[67,68]

RNA Extraction and Quantitative RT-PCR Analysis: Total RNA was isolated with Trizol (Invitrogen, Carlsbad, CA) following the manufacturer’s instructions and quantitative RT-PCR used the iTaq Universal SYBR Green Supermix (Bio-Rad, Berkeley, California) and a 7900HT real-time PCR instrument (Applied Biosystems, Foster City, CA) as previously described11 (see Supporting Information). Primer sequences (Integrated DNA Technologies, USA) are in Table S4, Supporting Information.

ChIP-PCR: ChIP was performed with anti-H3 (Active Motif, Cat# 39 763), and anti-H3K27Ac (Abcam, Cat# 4729) antibodies. Briefly, extracted chromatin was crosslinked with 1% paraformaldehyde and sonicated to an average size of ≈300–500 bp. 3 μgs of chromatin were incubated with 3 μg of either anti-H3 or anti-H3K27Ac overnight at $4 ~ ^ { \circ } \mathsf C$ . The concentration of immunoprecipitated DNA was measured with a Qubit ds-DNA HS Assay Kit (Thermo Fisher Scientific). Immunoprecipitated DNA was amplified by qPCR with gene-specific primers using SYBR Green Master Mix (Bio-Rad, iTaq Universal SYBR Green Supermix). A target sequence located 1 kb upstream from the binding site served as negative control. Normalization used input DNA. Primer sequences are listed in Table S5, Supporting Information.

Western Blotting: Cells were lysed in radio immunoprecipitation as- say (RIPA) buffer or mammalian protein extraction reagent (mPER, ThermoFisher, Waltham, MA). Protein concentrations were quantified with the Bradford assay (Biorad Protein Assay Reagent, BioRad, Berkeley, CA) or BCA assay (Pierce BCA Protein Assay Kit, ThermoFisher, Waltham, MA). Proteins (10–20 μg) were resolved by SDS-PAGE, and electroblotted onto PVDF membranes, as described previously.[8] The antibodies against GPx4 (rabbit monoclonal, Cat# ab125066, used at 1:1000), and scavenging receptor SR-B1 (rabbit monoclonal, Cat# 52 629, used at 1:1000) were purchased from Abcam (Cambridge, MA). HMGCS1 (rabbit monoclonal, Cat# 36 877, 1:1000), SQLE (rabbit monoclonal, Cat# 40 659, 1:1000), and ??-actin (rabbit monoclonal, Cat# 4970) were from Cell Signaling Technology (Danvers, MA). Mouse monoclonal GAPDH antibody was from Meridian Life Science (Memphis, Tennessee, Cat# H86504M, used at 1:10000). Mouse monoclonal alpha tubulin (Rosemont, IL, Cat# 66031- 1, used at 1:100000) was from Proteintech. HRP-conjugated donkey-antirabbit polyclonal antibody (Cat#NA9340, used at 1:2000) was purchased from GE Healthcare (Pittsburgh, PA), HRP-conjugated goat-anti-mouse antibody (Cat#haf007, used at 1:2000) was from R&D System (Minneapolis, MN), and Horseradish Peroxidase (HRP)-conjugated goat-anti-rabbit (Cat#1 706 515, used at 1:2000) was from BioRad (Berkely, CA). After blocking, membranes were incubated with primary antibody at 4 °C overnight and with HRP-conjugated secondary antibody for 1 h at room temperature. Signal was generated using SuperSignal West Pico PLUS Chemiluminescent Substrate (Thermo Scientific, Cat# 34 577), SuperSignal West Femto Maximum Sensitivity Substrate (Thermo Scientific, Cat# 34 095) enhanced chemiluminescent HRP system, or Clarity Western ECL Substrate (BioRad, Berkely, CA). Images were captured by a luminescent image analyzer with a CCD camera (LAS 3000, Fuji Film) or on an Azure300 system (Azure Biosystems, Dublin, CA).

Cell Transduction And Transfection: OC cells were transduced with lentiviral particles containing shRNA in the presence of polybrene (8 μg mL−1) for 48 h. Lentiviral transduction particles containing three shRNAs targeting GPx4 were used (shGPx4-1, Cat#TRCN0000046249; shGPx4-2, Cat#TRCN0000046251, and shGPx4-3, Cat#00 00046252). Cells transduced with scrambled shRNA (Mission Lentiviral Transduction Particles, Sigma-Aldrich, St Louis, MO, USA) served as controls. Transduced cells were selected with puromycin (2 μg mL−1). For transient siRNA transfection, cells were transfected with 25 nm siRNAs against SR-B1 (Cat# AM16708, Invitrogen) or control siRNAs (Cat# AM4611, Invitrogen) using RNAiMax (Thermo Fisher). Cells mock transfected with lipofectamine alone were used as a control. Cells were evaluated 72 h after transfection.

Intracellular Reactive Oxygen Species: Mean ROS levels were measured by using the DCFDA/H2DCFDA-Cellular ROS Detection Assay Kit (Abcam, Cambridge, MA, USA). For RSL3 treatment, 25, 000 cells per well were seeded in a dark, clear bottom 96-well microplate, were treated with RSL3 or control and ROS levels were measured by fluoro-spectrophotometer at Ex/Em wavelengths of 480 and 535 nm, respectively. Cells transduced with shRNAs (shCTRL or shGPx4) were cultured in full serum (10% FBS) for 24 h. A million cells were treated with 20 μm DCFDA for 30 min at 37 °C prior to FACS analysis.

BODIPY Staining for Lipid Peroxidation: Intracellular lipid peroxidation was determined with BODIPY 581/591 C11 (Thermo Fisher Scientific, Cat# D3861), a lipid peroxidation sensor as previously described[11] (see Supporting Information). Data were analyzed using FlowJo software.

Intracellular Cholesterol Quantification Assay: Total intracellular cholesterol, including free cholesterol and cholesteryl ester, was measured using an Amplex red cholesterol assay kit (Cat# A12216, Thermal Fisher Science, USA), as described previously.[37] Briefly, cells cultured in full serum conditions were detached using trypsin, counted, and lysed in RIPA buffer or directly in 1X Reaction Buffer. For quantification, 50 μL of standards or samples and 50 μL of the Amplex Red reagent/HRP/cholesterol oxidase/ cholesterol esterase working solution (300 μm Amplex Red reagent containing 2 U mL−1 HRP, 2 U mL−1 cholesterol oxidase, and 0.2 U mL−1 cholesterol esterase) were added to a 96-well black plate and incubated for 30 min at $3 7 ^ { \circ } \mathsf { C }$ in the dark. Fluorescence intensities were measured in a microplate reader using Ex/Em of 560/590 nm. Cholesterol content was normalized to cell number (per 105 cells mL−1).

Intracellular Lipid Quantification: Intracellular lipids were quantified using Nile Red reagent (Sigma Aldrich). Cells were plated at 150, 000 cells per well in 6-well plates. The following day, cells were incubated with Nile Red (300 nm) for 15 min at 37 °C, 5% CO , washed twice with 1X PBS, and resuspended in 1X PBS Fluorescence was quantified using a BD LSR II Fortessa flow cytometer and data were analyzed using FlowJo software.

Triglyceride Assay: Cellular triglyceride levels were detected with the Triglyceride-Glo Assay (Promega, Madison, WI) according to the manufacturer’s protocol. Cells were plated at 20, 000 cells well−1 in 96-well plates and allowed to attach to the plate overnight. Cells were washed twice with PBS, 50 uL lysis buffer with lipase was added to each well, and the plate was incubated at 37 °C for 30 min. 45 μL of sample, lysis buffer, or a 40 μm standard were added to a white 96-well plate. 45 μL of detection reagent was added to each well and incubated at room temperature for 1 h. Luminescence was read on a Synergy 2 plate reader (BioTek).

Cholesterol Uptake: Cells were plated at 100, 000 cell per well in 6-wel plates. The following day, media was changed to 1% FBS containing media and cells were incubated for 24 h. TopFlour (TF) cholesterol (1 μm, Avanti Polar Lipids) with or without HDL NPs (10, 20 or 40 nm) were added to cells and incubated for 4 h at 37 °C, 5% CO . Cells were then washed twice with 1X PBS, resuspended in 1X PBS, and TF cholesterol fluorescence was quantified using a BD LSR II Fortessa flow cytometer in the FITC channel. Data were analyzed using FlowJo software.

RNA Sequencing: Total RNA was extracted with TRI Reagent (Sigma, Cat# T9424), processed as previously described and sequenced on an Illumina NextSeq500 system with single-end, 75-bp read length settings (See Supporting Information). Data are deposited in the NCBI GEO database (GSE234404).

Data Analysis: Normalized read counts from RNA sequencing of Pt-S and Pt-R OVCAR5 cells (GSE 148 003)[8] were used for GSEA[69] by using Hallmark and C2 curated gene sets. Heatmap for Hallmark\_Cholesterol\_Homeostasis gene set was generated by using the heatmap R package. BioJupies https://www.cell.com/cell-systems/ fulltext/S2405-4712(18)30432-0 was used to analyze pathways enriched among differentially expressed genes (DEGs) in cells depleted of GPx4 versus control cells. Transcription factor PPI pathway enrichment used Enrichr https://maayanlab.cloud/Enrichr/. RNA sequencing data obtained from HGSOC tumors were downloaded from The Cancer Genome Atlas (TCGA-OV). Linear correlation analysis was performed using n = 370 samples to test the relationship between genes of interest. Pearson’s correlation coefficient was calculated based on normalized counts. For Kaplan-Meier survival analysis, an online tool was used (https://kmplot.com/ analysis/) and a database including gene expression data and overall survival information of patients with HGSOC.[70] A total of 523 samples from GEO were analyzed, including GSE14764, GSE15622, GSE18520, GSE19829, GSE23554, GSE26193, GSE26712, GSE27651, GSE30161, GSE3149, GSE51373, GES63885, GSE65986, GSE9891 and TCGA. The log rank test determined the statistical significance of survival differences between high versus low SCARB1 groups.

Statistical Analysis: Data were analyzed by Student’s t-test, one-way ANOVAs with Tukey’s multiple comparisons test, or two-way ANOVAs with Sidak’s multiple comparisons test. p-values from ANOVAs are multiplicity adjusted p-values. All experiments were done in at least biologica triplicates. All statistical analyses were done using GraphPad Prism software. For all experiments, p values less than 0.05 were considered significant. Outliers were selected by using Outlier Calculator (GraphPad) and a significance level of 0.05.

## Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements

This work was supported by the Office of the Assistant Secretary of Defense for Health Affairs, through the Ovarian Cancer Ressearch Program under Award Nos. W81XWH-21-1-0378. Opinions, interpretations, conclusions and recommendations are those of the author and are not necessarily endorsed by the Department of Defense. The authors thank Dr. Mazhar Adli for providing the OVCAR4 Pt-S and Pt-R cells, and Dr. Guangyuan Zhao for GSEA bioinformatic analysis. Flow cytometry analyses were performed in the Northwestern University Flow Cytometry Core Facility supported by the Cancer Center Support Grant NCI CA060553. PDX experiments were performed in the Center for Developmental Therapeutics (CDT) partly supported by Cancer Center Support Grant NCI CA060553.

## Conflict of Interest

CST and AEC have a relationship with Zylem Biosciences, Inc., which is a start-up biotechnology company with license to the HDL NP technology from Northwestern University.

## Data Availability Statement

The data that support the findings of this study are available in the supplementary material of this article.

## Keywords

cholesterol uptake, ferroptosis, platinum resistant ovarian cancer, redox targeting

Received: July 28, 2023

Revised: November 18, 2023

Published online: January 23, 2024

[1] E. Pujade-Lauraine, F. Hilpert, B. Weber, A. Reuss, A. Poveda, G. Kristensen, R. Sorio, I. Vergote, P. Witteveen, A. Bamias, D. Pereira, P. Wimberger, A. Oaknin, M. R. Mirza, P. Follana, D. Bollag, I. Ray-Coquard, J. Clin. Oncol. 2014, 32, 1302.  
[2] A. N. Gordon, J. T. Fleagle, D. Guthrie, D. E. Parkin, M. E. Gore, A. J. Lacave, J. Clin. Oncol. 2001, 19, 3312.  
[3] M. L. Disis, M. H. Taylor, K. Kelly, J. T. Beck, M. Gordon, K. M. Moore, M. R. Patel, J. Chaves, H. Park, A. C. Mita, E. P. Hamilton, C. M. Annunziata, H. J. Grote, A. Von Heydebreck, J. Grewal, V. Chand, J. L. Gulley, JAMA Oncol 2019, 5, 393.  
[4] K. Bell-McGuinn, J. Konner, W. Tew, D. R. Spriggs, Ann. Oncol. 2011, 22, viii77.  
[5] C. Aghajanian, D. S. Dizon, P. Sabbatini, J. J. Raizer, J. Dupont, D. R. Spriggs, J. Clin. Oncol. 2005, 23, 5943.  
[6] K. N. Moore, A. A. Secord, M. A. Geller, D. S. Miller, N. Cloven, G. F. Fleming, A. E. Wahner Hendrickson, M. Azodi, P. Disilvestro, A. M. Oza, M. Cristea, J. S. Berek, J. K. Chan, B. J. Rimel, D. E. Matei, Y. Li, K. Sun, K. Luptakova, U. A. Matulonis, B. J. Monk, Lancet Oncol. 2019, 20, 636.  
[7] W. Yu, Y. Chen, J. Dubrulle, F. Stossi, V. Putluri, A. Sreekumar, N. Putluri, D. Baluya, S. Y. Lai, V. C. Sandulache, Sci. Rep. 2018, 8, 4306.  
[8] Y. Wang, G. Zhao, S. Condello, H. Huang, H. Cardenas, E. J. Tanner, J. Wei, Y. Ji, J. Li, Y. Tan, R. V. Davuluri, M. E. Peter, J.-X. Cheng, D. Matei, Cancer Res. 2021, 81, 384.  
[9] Y. Tan, J. Li, G. Zhao, K. C. Huang, H. Cardenas, Y. Wang, D. Matei, J. X. Cheng, Nat. Commun. 2022, 13, 4554.  
[10] D. O. Bauerschlag, N. Maass, P. Leonhardt, F. A. Verburg, U. Pecks, F. Zeppernick, A. Morgenroth, F. M. Mottaghy, R. Tolba, I. Meinhold-Heerlein, K. Bräutigam, J. Transl. Med. 2015, 13, 146.  
[11] R. Vona, E. Iessi, P. Matarrese, Front. Cell Dev. Biol. 2021, 9, 622908.  
[12] Q. Shi, J. Chen, X. Zou, X. Tang, Front. Cell Dev. Biol. 2022, 10, 819281.  
[13] S. Yue, J. Li, S.-Y. Lee, H.-J. Lee, T. Shao, B. Song, L. Cheng, T.-A. Masterson, X. Liu, T.-L. Ratliff, J.-X. Cheng, Cell Metab. 2014, 19, 393.  
[14] D. Criscuolo, R. Avolio, G. Calice, C. Laezza, S. Paladino, G. Navarra, F. Maddalena, F. Crispo, C. Pagano, M. Bifulco, M. Landriscina, D. S. Matassa, F. Esposito, Cells 2020, 9, 828.  
[15] B. Akinwunmi, A. F. Vitonis, L. Titus, K. L. Terry, D. W. Cramer, Int. J. Cancer 2019, 144, 991.  
[16] J.-L. Feng, S. C. Dixon-Suen, S. J. Jordan, P. M. Webb, Br. J. Cancer 2021, 125, 766.  
[17] H. Y. Chen, Q. Wang, Q. H. Xu, L. Yan, X. F. Gao, Y. H. Lu, L. Wang, Biomed Res. Int. 2016, 2016, 9125238.  
[18] L. Gu, S. T. Saha, J. Thomas, M. Kaur, FEBS J. 2019, 286, 4192.  
[19] R. Riscal, N. Skuli, M. C. Simon, Mol. Cell 2019, 76, 220.  
[20] J. Lyu, E. J. Yang, J. S. Shim, Cells 2019, 8, 389.  
[21] B. Plochberger, M. Axmann, C. Röhrl, J. Weghuber, M. Brameshuber, B. K. Rossboth, S. Mayr, R. Ros, R. Bittman, H. Stangl, G. J. Schütz, Atherosclerosis 2018, 277, 53.  
[22] W.-J. Shen, S. Asthana, F. B. Kraemer, S. Azhar, J. Lipid Res. 2018, 59, 1114.  
[23] L. K. Mooberry, M. Nair, S. Paranjape, W. J. Mcconathy, A. G. Lacko, J. Drug Targeting 2010, 18, 53.  
[24] L. K. Mooberry, N. A. Sabnis, M. Panchoo, B. Nagarajan, A. G. Lacko, Front, Pharmacol, 2016, 7, 466.  
[25] M. P. Plebanek, D. Bhaumik, P. J. Bryce, C. S. Thaxton, Mol. Cancer Ther. 2018, 17, 686.  
[26] M. P. Plebanek, R. K. Mutharasan, O. Volpert, A. Matov, J. C. Gatlin, C. S. Thaxton, Sci. Rep. 2015, 5, 15724.  
[27] A. J. Luthi, N. N. Lyssenko, D. Quach, K. M. Mcmahon, J. S. Millar, K. C. Vickers, D. J. Rader, M. C. Phillips, C. A. Mirkin, C. S. Thaxton, J. Lipid Res. 2015, 56, 972.  
[28] S. Yang, M. G. Damiano, H. Zhang, S. Tripathy, A. J. Luthi, J. S. Rink, A. V. Ugolkov, A. T. K. Singh, S. S. Dave, L. I. Gordon, C. S. Thaxton, Proc. Natl. Acad. Sci. USA 2013, 110, 2511.  
[29] K. M. Mcmahon, C. Scielzo, N. L. Angeloni, E. Deiss-Yehiely, L. Scarfo, P. Ranghetti, S. Ma, J. Kaplan, F. Barbaglio, L. I. Gordon, F. J. Giles, C. S. Thaxton, P. Ghia, OncoTargets Ther. 2017, 8, 11219.  
[30] J. S. Rink, A. Y. Lin, K. M. Mcmahon, A. E. Calvert, S. Yang, T. Taxter, J. Moreira, A. Chadburn, A. Behdad, R. Karmali, C. S. Thaxton, L. I. Gordon, J. Biol. Chem. 2021, 296, 100100.  
[31] A. J. Luthi, H. Zhang, D. Kim, D. A. Giljohann, C. A. Mirkin, C. S. Thaxton, ACS Nano 2012, 6. 276,  
[32] C. S. Thaxton, W. L. Daniel, D. A. Giljohann, A. D. Thomas, C. A. Mirkin, J. Am. Chem. Soc. 2009, 131, 1384.  
[33] M.-C. Daniel, D. Astruc, Chem. Rev. 2004, 104, 293.  
[34] S. Shang, J. Yang, A. A. Jazaeri, A. J. Duval, T. Tufan, N. Lopes Fischer, M. Benamar, F. Guessous, I. Lee, R. M. Campbell, P. J. Ebert, T. Abbas, C. N. Landen, A. Difeo, P. C. Scacheri, M. Adli, Cancer Res. 2019, 79, 4599.  
[35] R. Riscal, C. J. Bull, C. Mesaros, J. M. Finan, M. Carens, E. S. Ho, J. P. Xu, J. Godfrey, P. Brennan, M. Johansson, M. P. Purdue, S. J. Chanock, D. Mariosa, N. J. Timpson, E. E. Vincent, B. Keith, I. A. Blair, N. Skuli, M. C. Simon, Cancer Discov. 2021, 11, 3106.  
[36] X. Zhao, X. Lian, J. Xie, G. Liu, Redox Biol. 2023, 62, 102678.  
[37] M. P. Plebanek, R. K. Mutharasan, O. Volpert, A. Matov, J. C. Gatlin, C. S. Thaxton, Sci. Rep. 2015, 5, 15724.  
[38] D. Monsivais, M. T. Dyson, P. Yin, A. Navarro, J. S. T. Coon, M. E. Pavone, S. E. Bulun, Fertil Steril. 2016, 105, 1266.  
[39] J. S. Rink, S. Yang, O. Cen, T. Taxter, K. M. Mcmahon, S. Misener, A. Behdad, R. Longnecker, L. I. Gordon, C. S. Thaxton, Mol. Pharm. 2017, 14, 4042.  
[40] J. Garcia-Bermudez, L. Baudrier, E. C. Bayraktar, Y. Shen, K. La, R. Guarecuco, B. Yucel, D. Fiore, B. Tavora, E. Freinkman, S. H. Chan, C. Lewis, W. Min, G. Inghirami, D. M. Sabatini, K. Birsoy, Nature 2019, 567, 118.  
[41] M. J. Hangauer, V. S. Viswanathan, M. J. Ryan, D. Bole, J. K. Eaton, A. Matov, J. Galeas, H. D. Dhruv, M. E. Berens, S. L. Schreiber, F. Mccormick, M. T. Mcmanus, Nature 2017, 551, 247.  
[42] D. Lopez, M. P. Mclean, Endocrinology 1999, 140, 5669.  
[43] M. Tre?Guier, C. Doucet, M. Moreau, C. Dachet, J. ?. L. Thillet, M. J. Chapman, T. Huby, Arterioscler. Thromb. Vasc. Biol. 2004, 24, 2358.  
[44] J. D. Horton, J. L. Goldstein, M. S. Brown, J. Clin. Invest. 2002, 109, 1125.  
[45] L. K. Gopi, B. L. Kidder, Nat. Commun. 2021, 12, 1419.  
[46] I. Dunham, A. Kundaje, S. F. Aldred, P. J. Collins, C. A. Davis, F. Doyle, C. B. Epstein, S. Frietze, J. Harrow, R. Kaul, J. Khatun, B. R. Lajoie, S. G. Landt, B.-K. Lee, F. Pauli, K. R. Rosenbloom, P. Sabo, A. Safi, A. Sanyal, N. Shoresh, J. M. Simon, L. Song, N. D. Trinklein, R. C. Altshuler, E. Birney, J. B. Brown, C. Cheng, S. Djebali, X. Dong, I. Dunham, et al., Nature 2012, 489, 57.  
[47] C. A. Davis, B. C. Hitz, C. A. Sloan, E. T. Chan, J. M. Davidson, I. Gabdank, J. A. Hilton, K. Jain, U. K. Baymuradov, A. K. Narayanan, K. C. Onate, K. Graham, S. R. Miyasato, T. R. Dreszer, J. S. Strattan, O. Jolanki, F. Y. Tanaka, J. M. Cherry, Nucleic Acids Res. 2018, 46, D794.  
[48] M. M. K. Shahzad, L. S. Mangala, H. D. Han, C. Lu, J. Bottsford-Miller, M. Nishimura, E. M. Mora, J.-W. Lee, R. L. Stone, C. V. Pecot, D. Thanapprapasr, J.-W. Roh, P. Gaur, M. P. Nair, Y.-Y. Park, N. Sabnis, M. T. Deavers, J.-S. Lee, L. M. Ellis, G. Lopez-Berestein, W. J. Mcconathy, L. Prokai, A. G. Lacko, A. K. Sood, Neoplasia 2011, 13, 309.  
[49] J. Kim, B. Thompson, S. Han, Y. Lotan, J. G. Mcdonald, J. Ye, Biochim. Biophys. Acta, Mol. Cell Biol. Lipids 2019, 1864, 158525.  
[50] J. Garcia-Bermudez, L. Baudrier, E. C. Bayraktar, Y. Shen, K. La, R. Guarecuco, B. Yucel, D. Fiore, B. Tavora, E. Freinkman, S. H. Chan, C. Lewis, W. Min, G. Inghirami, D. M. Sabatini, K. Birsoy, Nature 2019, 567, 118.  
[51] R. Riscal, C. J. Bull, C. Mesaros, J. M. Finan, M. Carens, E. S. Ho, J. P. Xu, J. Godfrey, P. Brennan, M. Johansson, M. P. Purdue, S. J. Chanock, D. Mariosa, N. J. Timpson, E. E. Vincent, B. Keith, I. A. Blair, N. Skuli, M. C. Simon, Cancer Dis. 2021, 11, 3106.  
[52] W. Liu, B. Chakraborty, R. Safi, D. Kazmin, C.-Y. Chang, D. P. Mcdonnell, Nat. Commun, 2021, 12, 5103.  
[53] M. J. Hangauer, V. S. Viswanathan, M. J. Ryan, D. Bole, J. K. Eaton, A. Matov, J. Galeas, H. D. Dhruv, M. E. Berens, S. L. Schreiber, F. Mccormick, M. T. Mcmanus, Nature 2017, 551, 247.  
[54] V. S. Viswanathan, M. J. Ryan, H. D. Dhruv, S. Gill, O. M. Eichhoff, B. Seashore-Ludlow, S. D. Kaffenberger, J. K. Eaton, K. Shimada, A. J.  
Aguirre, S. R. Viswanathan, S. Chattopadhyay, P. Tamayo, W. S. Yang, M. G. Rees, S. Chen, Z. V. Boskovic, S. Javaid, C. Huang, X. Wu, Y.-Y. Tseng, E. M. Roider, D. Gao, J. M. Cleary, B. M. Wolpin, J. P. Mesirov, D. A. Haber, J. A. Engelman, J. S. Boehm, J. D. Kotz, et al., Nature 2017, 547, 453.  
[55] S. Yang, M. G. Damiano, H. Zhang, S. Tripathy, A. J. Luthi, J. S. Rink, A. V. Ugolkov, A. T. K. Singh, S. S. Dave, L. I. Gordon, C. S. Thaxton, Proc. Natl. Acad. Sci. USA 2013, 110, 2511.  
[56] H. Ouled-Haddou, K. Messaoudi, Y. Demont, R. Lopes Dos Santos, C. Carola, A. Caulier, P. Vong, N. Jankovsky, D. Lebon, A. Willaume, J. Demagny, T. Boyer, J.-P. Marolleau, J. Rochette, L. Garçon, Blood Adv. 2020, 4, 5666.  
[57] D. R. Coelho, F. R. Palma, V. Paviani, C. He, J. M. Danes, Y. Huang, J. C. P. Calado, P. C. Hart, C. M. Furdui, L. B. Poole, M. J. Schipma, M. G. Bonini, Proc. Natl. Acad. Sci. USA 2022, 119, e2110348119.  
[58] N. Jänsch, C. Meyners, M. Muth, A. Kopranovic, O. Witt, I. Oehme, F.-I. Meyer-Almes, Redox Biol. 2019, 20, 60.  
[59] E. Polanská, S. Pospisilova, M. Stros, PLoS One 2014, 9, e89070.  
[60] Y. Zhang, Y. Wang, G. Zhao, E. J. Tanner, M. Adli, D. Matei, J. Clin. Invest. 2022, 132, e151591.  
[61] R. Perets, G.-A. Wyant, K.-W. Muto, J.-G. Bijron, B.-B. Poole, K.-T. Chin, J.-Y.-H. Chen, A.-W. Ohman, C.-D. Stepule, S. Kwak, A.-M. Karst, M.-S. Hirsch, S.-R. Setlur, C.-P. Crum, D.-M. Dinulescu, R. Drapkin, Cancer Cell 2013, 24, 751.  
[62] N. Auersperg, S. L. Maines-Bandiera, H. G. Dyck, P. A. Kruk, Lab Invest. 1994, 71, 510.  
[63] J. S. Rink, A. Lin, K. M. McMahon, A. E. Calvert, S. Yang, T. Taxter, J. Moreira, A. Chadburn, A. Behdad, R. Karmali, C. S. Thaxton, L. I. Gordon, J. Biol. Chem. 2020, 296, 100100.  
[64] T.-C. Chou, Cancer Res. 2010, 70, 440.  
[65] R. Dong, W. Qiang, H. Guo, X. Xu, J. J. Kim, A. Mazar, B. Kong, J.-J. Wei, J. Hematol. Oncol. 2016, 9, 92.  
[66] X. Xu, B. Ayub, Z. Liu, V. A. Serna, W. Qiang, Y. Liu, E. Hernando, S. Zabludoff, T. Kurita, B. Kong, J.-J. Wei, Mol. Cancer Ther. 2014, 13, 1729.  
[67] G. Zhao, Y. Tan, H. Cardenas, D. Vayngart, Y. Wang, H. Huang, R. Keathley, J.-J. Wei, C. R. Ferreira, S. Orsulic, J.-X. Cheng, D. Matei, Proc. Natl. Acad. Sci. USA 2022, 119, e2203480119.  
[68] J. Li, S. Condello, J. Thomes-Pepin, X. Ma, Y. Xia, T. D. Hurley, D. Matei, I.-X. Cheng, Cell Stem Cell 2017, 20, 303  
[69] A. Subramanian, P. Tamayo, V. K. Mootha, S. Mukherjee, B. L. Ebert, M. A. Gillette, A. Paulovich, S. L. Pomeroy, T. R. Golub, E. S. Lander, J. P. Mesirov, Proc. Natl. Acad. Sci. USA 2005, 102, 15545.  
[70] B. Gyorffy, A. Lánczky, Z. Szállási, Endocr. Relat. Cancer 2012, 19, 197.