RESEARCH ARTICLE OPEN ACCESS

# High-Content SRS Imaging Unveils Altered Cholesterol Metabolism in Ovarian Cancers Under CAR-T Treatment

Chinmayee V. Prabhu Dessai1,2 Zhuoying Huang1,3 Haonan Lin1,2,4 Guangrui Ding2,4 Hongjian He2,4 Menna Siddiqui1,3 Meng Zhang2,4 Wilson Wong1,3 Ji-Xin Cheng1,2,4

1 Department of Biomedical Engineering, Boston University, Boston, Massachusetts, USA 2Photonics Center, Boston University, Boston, Massachusetts, USA 3Biological Design Center, Boston University, Boston, Massachusetts, USA 4Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts. USA

Correspondence: Wilson Wong (wilwong@bu.edu) Ji-Xin Cheng (jxcheng@bu.edu)

Received: 17 September 2025 Revised: 15 January 2026 Accepted: 6 February 2026

Keywords: cancer metabolism modulation | CAR-T therapy improvement | high-content SRS imaging | ovarian cancer

## ABSTRACT

Ovarian cancer is one of the most lethal gynecological cancers worldwide and has one of the highest recurrence rates. Recently developed Chimeric Antigen Receptor (CAR) -T cell therapy has shown potent clinical efficacy against hematological malignancies. However, solid tumors, including ovarian cancer, possess several mechanisms that hinder T cell activity, and metabolic alteration of cancer cells has been shown to contribute to resistance to immune cell attack against solid tumors. Here, we explore the metabolic response of ovarian cancer cells to CAR-T cell attack using label-free high-content hyperspectral stimulated Raman scattering (h2SRS) imaging. Utilizing visible h2SRS imaging with much improved spatial resolution, we find an altered cholesterol metabolism, featured by increased storage of cholesteryl ester in lipid droplets and free cholesterol, in ovarian cancer cells that survive the CAR-T treatment. Administration of Avasimibe, an inhibitor of cholesteryl esterification, further enhances CAR-T cytotoxicity. Our study shows the promise of implementing metabolic modulation to facilitate CAR-T cell treatment of solid tumors.

## 1 Introduction

Ovarian cancer poses a major clinical challenge and remains the leading cause of death among the gynecological malignancies in the world. Despite extensive research and treatment advances, it remains a persistent problem because of the high recurrence rates [1]. The current standard of care for ovarian cancer includes surgical removal followed by platinum-based chemotherapy [2]. Even though many patients show an initial positive response, the majority of them show a relapse within two years, most commonly due to platinum resistance development [2, 3]. Due to this short-lived success of the existing standard therapy, there is an urgent need for more effective clinical strategies. A particularly exciting form of immunotherapy is the Chimeric Antigen Receptor (CAR) -T cell therapy, which has demonstrated potent efficacy in the clinics against hematological malignancies [2]. CAR-T cel therapy involves genetically engineering the patient’s T cells to express the CAR that bind to a specific antigen expressed on the target cancer cells [4]. While CAR-T therapy has shown success in hematological malignancies [5], extending CAR-T therapy to solid tumors, such as ovarian cancer, has been challenging [6. 7]. One of the maior obstacles is the immunosuppressive tumor microenvironment, which limits the activity of CAR-T cells against solid tumors [7, 8]. Hence, there is a need to improve CAR-T cell-mediated killing of cancer cells.

Cell metabolism plays an important role in CAR-T cell cytotoxicity and is pivotal in understanding immunotherapy [9–12].

Similarly, modulation of cancer cell metabolism has also been linked to cancer survival under drug resistance and stress resistance [3, 13]. The inhibition of several metabolic pathways has been shown to reduce cancer cell aggression [3, 14, 15]. The metabolic dynamics of CAR-T cells attacking cancers will be an important piece of information for understanding the interaction between the engineered immune cells and tumors, and for discovering metabolic targets to improve the CAR-T cell-mediated killing efficacy. Current gold standard techniques to study cell metabolism include mass spectrometry and fluorescence imaging [16]. Although highly sensitive, mass spectrometrybased methods do not elucidate metabolic dynamics or capture cellular heterogeneity due to their bulk analysis and destructive nature. Imaging mass spectrometry can provide spatial metabolic information but often requires sample preparation and is affected by limited spatial resolution. In contrast, fluorescence imaging is high-resolution but requires prior knowledge of the metabolic pathways to target, capping its applications in exploratory studies. Additionally, fluorescent probes are usually bulky and may interfere with the metabolic processes being investigated, potentially introducing artifacts in the data [17, 18]. Label-free, non-destructive vibrational spectroscopic techniques have emerged as powerful alternatives to address these limitations [17, 19].

Molecular vibrations produce specific Raman spectra that can be used as a signature of molecules [20]. Label-free Raman spectroscopy has been extensively applied to study cancer cell metabolism and classification [20, 21]. However, spontaneous Raman spectroscopy has limitations in biological imaging applications due to very low signal levels and slow image acquisition speeds. Coherent Raman Scattering processes, which include Coherent Anti-Stokes Raman Scattering (CARS) and Stimulated Raman Scattering (SRS), overcome these limitations and allow high-speed vibrational imaging of living specimens [22, 23]. CARS imaging has been used in studying cancer cell metabolism, but it suffers from a non-resonant background [17, 24]. SRS imaging shows a better contrast as it does not have the problem of nonresonant background. SRS imaging has emerged as a proficient method for studying cell metabolism, including cancer cells, in the past decade. Applications of SRS imaging to cancer cell metabolism have revealed new cancer biomarkers [25, 26]. Being able to generate maps of multiple biomolecules, recently developed high-content hyperspectral SRS (h2SRS) imaging shows great potential in profiling cancer cell metabolism in live and fixed samples [27, 28].

While various Raman techniques have been used to study cancer cells, CAR-T cells or other immune cells [29, 30], using coherent Raman microscopy to study the result of CAR-T cell challenge on cancer cell metabolism is under-explored. In this work, we studied the alteration of ovarian cancer cell metabolism using a CAR-T cell and cancer cell coculture. Toward this goal. we harnessed both near-infrared (NIR) and Visible h2SRS imaging [27, 28, 31, 32] to study lipid metabolic changes, especially the changes in cholesterol metabolism, in ovarian cancer cells cocultured with CAR-T cells. Based on the observation of increased cholesteryl ester storage and free cholesterol levels, we further explored the impact of cholesterol metabolic modulation on the efficiency of CAR-T cell-mediated killing of ovarian cancer cells.

## 2 Results

## 2.1 NIR h2SRS Imaging Shows Altered Lipid Metabolism and Protrusions in Ovarian Cancer Cells Co-Cultured with CAR-T Cells

To confirm the specificity of our anti-HER2 CAR-T cells and to characterize HER2 expression on our ovarian cancer target cell lines, we first assessed CAR expression and target HER2 levels. Our CAR-T cells demonstrated sustained robust CAR expression even after co-incubation with cancer cells, confirming their continued functionality (Figure S1C). SKOV3 cells exhibited high HER2 surface expression, while OVCAR5 cells expressed HER2 at a significantly lower level (Figure S1D). Critically, surviving SKOV3 and OVCAR5 cancer cells largely maintained their respective HER2 expression after CAR-T challenge (Figure S1D). This sustained antigen presence strongly indicates that CAR-T mediated killing is antigen-specific and that cell survival is not primarily due to antigen loss, thereby motivating our investigation into alternative adaptive mechanisms, such as metabolic reprogramming, as drivers of CAR-T resistance. To investigate the metabolic changes in the ovarian cancer cells under attack from CAR-T cells, we employed NIR h2SRS imaging of a coculture of ovarian cancer and CAR-T cells. We cocultured an ovarian cancer cell line, SKOV3, with anti-HER2 CAR-T cells. We acquired NIR h2SRS imaging stacks of the coculture samples using a lab-built setup [31], shown in Figure 1A and described in the methods section. As shown in Figure 1B, we then performed spectral unmixing of these stacks using pixel-wise least absolute shrinkage and selection operator (LASSO) to decompose them into chemical maps of triacylglycerols/triglycerides (TAG), protein, total cholesterol, and nucleic acid based on the pure chemical spectra acquired of trioleate glycerol, bovine serum albumin (BSA), cholesterol, and purified ribonucleic acid (RNA) from cells, respectively [27, 31]. Figure 1C shows the metabolic maps of the SKOV3 cells with and without coculture with CAR-T cells at an Effector: Target (E:T) of 2:1. We observed an overall signal increase from the SKOV3 cells cocultured with CAR-T cells.

Furthermore, significant protrusions in the SKOV3 cells were observed in the coculture sample, indicating that the cells are under stress [33]. Cell membrane protrusions are associated with cancer cell migration and metastasis [34, 35] and are also promoted in response to immune activity [36]. Cancer cells under stress have been shown to increase the level of lipids and cholesterol species inside the cells as a survival mechanism [33, 37–41]. Consequently, we analyzed the TAG and total cholesterol (TC) maps shown in Figure 1C to obtain quantitative results as presented in Figure 1D. As expected, surviving SKOV3 cells cocultured with CAR-T cells exhibited an upregulation of triglycerides and total cholesterol (free cholesterol and cholesteryl ester), with increases of 3.5-fold and 2.3-fold, respectively, compared to SKOV3-only cells.

## 2.2 Visible h2SRS Imaging Unveils Upregulation of Free Cholesterol and Cholesteryl Ester in Ovarian Cancer Cells Cocultured with CAR-T Cells

We further dissected the total cholesterol (TC) content to quantify free cholesterol (FC) and cholesteryl ester (CE), as these species are markers of distinct functions and regulations within the cell [39]. Free cholesterol resides in membranes, while the core of lipid droplets (LDs) is mainly composed of TAG and sterol esters [42, 43]. High-resolution imaging to resolve single LDs and membranes would allow us to dissect the LDs content. Our recently developed Visible h2SRS system, shown in Figure 2A, offers a diffraction-limited resolution of 86 nm [28. 44]. Such Visible h2SRS imaging significantly improves organellar analysis compared to NIR h2SRS [28] since the size of lipid droplets can vary from less than 0.4 m to tens of m [44, 45]. As shown in Figure 2B. Visible h2SRS resolved individual lipid droplets smaller than 0.2 µm, whereas in NIR h2SRS, the small LDs appear as aggregates. Thus, with Visible h2SRS, FC, CE, and TAG can be spatially resolved.

![](images/b5ec2255766cea06af58da75a5c083ac51ddeb5f5a3382627a7a13f9c0999a45.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Pump 800 nm"] --> B["Lens"]
  C["Stokes 1040 nm"] --> D["AOM"]
  E["Lock-in amplifier"] --> F["Objective"]
  G["PD with filter"] --> H["Condenser"]
  I["Motorized delay"] --> J["Mirror"]
  K["Glass Rods"] --> L["DM"]
  M["GM"] --> N["Output"]
```
</details>

B

![](images/4b811d4a80fcab878d6d99e535179a27b9badbfc9c746ea355285b559e9c9b95.jpg)

<details>
<summary>text_image</summary>

Ny
Nx
Nλ
Raster Unfold
</details>

![](images/b981de06739ee936e734939382e766548853952bb1b5cb4d71200ae75e065d9b.jpg)

![](images/b16c7974fadd80d250cf7ec3bd2ff87815faedb3126f7cb772f26e9a0978f930.jpg)

<details>
<summary>text_image</summary>

C
X
=
...
Dominant
Contribution
C_i
...
Refold
</details>

![](images/9d200de94bfa27209d555e2332188ebc1d19f9a2b619f34a220110b1a985c4b5.jpg)

<details>
<summary>line chart</summary>

| Intercoupler concentration (cm⁻¹) | Control | Treatment A | Treatment B |
| ------------------------------- | ------- | ----------- | ----------- |
| 2000                            | ~0.1    | ~0.1        | ~0.1        |
| 2500                            | ~0.9    | ~0.8        | ~0.7        |
| 3000                            | ~0.1    | ~0.1        | ~0.1        |
</details>

![](images/7b100c1fdf70e013c37826781785280644307141b7924ca92f2496abcc23b4e2.jpg)

<details>
<summary>text_image</summary>

C
NIR h2SRS sum Protein Triacylglycerol (TAG) Total Cholesterol (TC) Nucleic Acids
SKOV3 only
SKOV3 + CAR-T
</details>

D

![](images/b79124b67c47b198681ad7233eeba2cb3f1897883bd5ddac29cd967490fbb87c.jpg)

<details>
<summary>bar chart</summary>

| Group     | Condition | Area Fraction |
| --------- | --------- | ------------- |
| No CAR-T   | TAG       | 0.05          |
| No CAR-T   | TC        | 0.10          |
| w/ CAR-T   | TAG       | 0.18          |
| w/ CAR-T   | TC        | 0.25          |
</details>

FIGURE 1 Altered lipid metabolism and protrusion in SKOV3 cells cocultured with CAR-T cells. (A) NIR SRS imaging setup. DM: Dichroic Mirror, GM: Galvo Mirror, AOM: Acousto-Optic Modulator, PD: Photodiode. (B) Schematic of spectral unmixing of hyperspectral images of dimensions, $\mathrm { N _ { x } , N _ { y } , }$ and $\Nu _ { \lambda }$ using pixel-wise least absolute shrinkage and selection operator (LASSO) into biochemical maps, D stands for data matrix, C for Concentration matrix and S for pure chemical spectra reference matrix. (C) NIR h2SRS imaging of the SKOV3 cells with and without CAR-T coculture, E:T = 2:1, scale bars: 10 µm. (D) Quantification of cellular Total Cholesterol (TC) and Triglycerides/Triacylglycerols (TAG) in SKOV3 cells with and without CAR-T coculture, n>30 per group, data presented as means +/± stdev, \*\*\* p<0.001.

We acquired Visible h2SRS images of the SKOV3 cells only, and SKOV3 and CAR-T cells cocultured at an E:T ratio of 2:1. Metabolic maps are shown in Figure 2C. We also acquired the reference spectra of triacylglycerol, protein, total cholesterol, carbohydrates, and nucleic acid using trioleate glycerol, BSA, cholesterol, glucose, and purified RNA from cells, respectively for spectral unmixing. The symmetric $\mathrm { C H } _ { 3 }$ stretching in both CE and cholesterol contributes to the Raman spectrum peak at 2870 $\mathrm { c m ^ { - 1 } }$ [46, 47]. This peak contributes to the spectral unmixing in the same way, and it results in both CE and cholesterol being assigned to the same chemical map of total cholesterol. As previously mentioned and shown in Figure 2D, TAG and sterol esters make up most of the LDs. The cholesterol signal in the LD area should be from CE [42, 43], which is the excess cellular cholesterol esterized for storage in LDs [37, 48]. As shown in Figure 2E, we can separate the CE map from the TC map by creating a droplet mask out of the TAG map and overlapping it with the TC map. The FC content was then calculated as the difference between TC and CE. We further analyzed the FC and CE area fractions in each cell of the two groups (SKOV3 only and SKOV3+CAR-T), as shown in Figure 2F. We observed that all the lipid species were upregulated in the SKOy3 cells cocultured with CAR-T cells compared to the SKOV3-only cells, with specific increases of 2.3-fold in TAG, 4.5-fold in FC, and 1.7-fold in CE, respectively. We observed a similar trend in the OVCAR5 cell line, where CAR-T challenge induced an increase in lipid species, including FC (1.4-fold), TAG (1.38-fold), and CE

A  
![](images/e9b7fc2ddac0a2c34c29015f9e82adb29c790d0470c814e5d0f30e4d231acbd7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Pump 453 nm"] --> B["Lens"]
  C["Stokes 523 nm"] --> D["OM"]
  B --> E["Dichroic Mirror"]
  D --> E
  E --> F["Glass Rods"]
  F --> G["Scanning Unit"]
  H["Lock-in amplifier"] --> I["PD with filter"]
  I --> J["Condenser"]
  J --> K["Objective"]
  K --> E
```
</details>

B  
![](images/dcb44075b5d30c39452342a383c16c9cd5f0812a9b0279064040b34b52a2880c.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Lipid Droplet Signal Peak Width (µm) | Count (NIR SRS) | Count (VSRS) |
| ------------------------------------ | --------------- | ------------- |
| 0.0                                  | 1               | 3             |
| 0.4                                  | 4               | 8             |
| 0.8                                  | 3               | 5             |
| 1.2                                  | 2               | 3             |
| 1.6                                  | 1               | 2             |
| 2.0                                  | 1               | 1             |
| 2.4                                  | 1               | 1             |
| 2.8                                  | 0               | 0             |
| 3.2                                  | 0               | 0             |
| 3.6                                  | 1               | 0             |
</details>

C  
![](images/67515cdfcd23d5ff70f898466f45bef6240d6a7b9ea27c9e921929c1e509d792.jpg)

<details>
<summary>text_image</summary>

Visible h²SRS sum
SKOV3 only
Protein
TAG
Total Cholesterol
Nucleic Acids
Carbohydrate
SKOV3 + CAR-T
</details>

D  
![](images/b22c72432d6b68be9859d6e39d2a33e7958e96b9a00a556a1e6a099f8fbf7073.jpg)

<details>
<summary>text_image</summary>

Sterol Esters
Triacylglycerols/
Triglycerides
Free Cholesterol
Ovarian cancer cell
Lipid Droplet
</details>

E

![](images/17a36d07a34981b4783476ceae51c847340f4499388a0a61baf2c14732477ae6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["TAG Map"] --> B["1 LDs Thresholding"]
  C["TC Map"] --> D["2 LDs Mask"]
  E["TC Map"] --> F["3 Overlap"]
  G["FC Map"] --> H["4 Subtract"]
  B --> I["CE Map"]
  D --> I
  F --> I
  H --> I
```
</details>

F  
![](images/a867bdba78aefa13728fe4dc3c634875eee4a7f6384a1c283800b188e6dabbb8.jpg)

<details>
<summary>bar chart</summary>

| Group | CAR-T Condition | Area Fraction |
|-------|-----------------|---------------|
| TAG   | no CAR-T        | 0.04          |
| TAG   | with CAR-T      | 0.09          |
| FC    | no CAR-T        | 0.02          |
| FC    | with CAR-T      | 0.09          |
| CE    | no CAR-T        | 0.03          |
| CE    | with CAR-T      | 0.04          |
</details>

FIGURE 2 Visible SRS imaging uncovers altered cholesterol metabolism of SKOV3 cells. (A) Visible SRS imaging Setup, OM: Optical Modulator, PD: Photodiode. (B) Histogram of LDs spatial resolution comparison of NIR SRS and Visible SRS. (C) Visible h2SRS imaging of the SKOV3 cells with and without CAR-T coculture, E:T = 2:1, scale bars: 10 µm. (D) Composition of Lipid Droplets. (E) Schematic of CE and FC map generation from TAG and TC maps. (F) Quantification of TAG, FC and CE in SKOV3 cells with and without coculture with CAR-T cells., n>30 per group, data presented as means +/± stdev, \*\*\* p<0.001, \* p<0.05, TC: Total Cholesterol, FC: Free Cholesterol, CE: Cholesteryl Ester, TAG: Triacylglycerols/Triglycerides.

(2.27-fold) as compared to OVCAR5 cells without CAR-T (Figure S8A,B). Previous studies have shown that cholesterol plays a significant role in cancer and immune interactions [11. 14. 38. 49–51]. The cholesterol level in the tumor microenvironment is usually elevated, contributing to cancer progression and affecting immune cell response [14, 49, 52, 53]. Studies have shown that altering cholesterol levels in cancer cells can enhance T-cell function [50, 52]. Both CE and FC increase in cancer cells have been linked to cancer cell aggressiveness, immune response blockade, survivability, and proliferation [50, 54, 55]. Through chemical imaging of the surviving ovarian cancer cells in the ovarian cancer cell + CAR-T coculture, we revealed an upregulation of intracellular CE and TC levels in response to CAR-T challenge.

## 2.3 Inhibition of Cholesterol Synthesis or Esterification Suppresses SKOV3 Mobility

To investigate the effects of lowering cellular levels of either CE or TC in SKOV3 cells, we employed Avasimibe and Simvastatin to intervene in cholesterol metabolism [56, 57]. A previously published study showed that an increased level of FC in cancer cells softens cell membranes, facilitating cell migration [50] indicating that cholesterol metabolic intervention may reduce metastatic potential. As such, Simvastatin has been shown to decrease the cellular cholesterol level by inhibiting 3-hydroxy-3-methylglutaryl coenzyme A (HMG-CoA) reductase and, in turn, reducing ovarian cancer cell metastatic properties [15, 58]. Simvastatin has also been studied for T cell response enhancement in solid cancers like lung, breast, and gastric cancer [59–61]. Concurrently, CE accumulation is associated with the upregulation of the Phosphatidylinositol 3-Kinase/ Protein Kinase B (PI3K/AKT) pathway connected to increased cancer aggressiveness and metastasis [54]. The enzyme Acyl-CoA cholesterol acyltransferase 1 (ACAT-1) is responsible for cholesterol esterification of any excess cellular cholesterol [48, 54]. Hence, inhibition of ACAT-1 by Avasimibe decreases cancer aggressiveness [48, 54] by inducing endoplasmic reticulum stress. Researchers have also demonstrated the role of ACAT-1 inhibition in T cells in enhancing T cell response against liquid [62, 63] and solid cancers [14].

As summarized in Figure 3A, FC and CE are elevated in SKOV3 cells in the presence of CAR-T cells. While Simvastatin lowers the cellular FC, Avasimibe lowers the cellular CE. Hence, we examined the use of these drugs in decreasing the survival of SKOV3 cells cocultured with CAR-T cells. Figure 3B shows the TAG and TC maps of the Visible h2SRS imaging of SKOV3 cells with and without treatment with Avasimibe and Simvastatin. The quantification of the images is presented in Figure 3C. The SKOV3-only data presented in Figure 3C are the same as in Figure 2F, as these experiments were conducted in parallel. With Avasimibe treatment, the cellular CE level decreased to about 0.5-fold of the untreated group, while the FC and TAG levels stayed relatively the same. We also observed that with Simvastatin treatment, the cellular FC level decreased to about 0.25-fold of the untreated group, and the TAG levels increased 1.35-fold compared to the untreated group. However, as expected, cellular CE levels decreased mildly (to 0.69-fold of the untreated group) following Simvastatin treatment, although the change was not statistically significant [54]. With this validation, we conducted a migration assay with and without drug treatment of SKOV3 cells, presented in Figure 3D–G to assess their effect on migratory tendencies as an indicator of aggression. The concentrations used for the Avasimibe and Simvastatin treatments were at 30 m and were selected based on the cell viability of greater than 80% using the dose response assay presented in Figure S2C. We acquired confocal fluorescence images of the migrated cells in trans-well membranes. We can observe that the migration of the SKOV3 cells was significantly reduced following both Avasimibe and Simvastatin treatment by 95.5% and 47.4% compared to the untreated group. Importantly, Avasimibe treatment resulted in a much more significant reduction in migration, over twice that in the Simvastatin-treated group.

To comprehensively evaluate the impact of cholesterol metabolism interference, we assessed the effects of Avasimibe and Simvastatin on SKOV3 cell proliferation (Figure S9). Both drugs inhibited proliferation in a dose-dependent manner. Interestingly, Simvastatin proved more potent in reducing proliferation, achieving approximately a 50% reduction as compared to control by Day 7 at 0.39 µm, whereas Avasimibe required 6.25 µm for a similar effect. This contrasts with our findings in the migration assay (Figure 3D–G), where Avasimibe showed greater efficacy in reducing cell migration compared to Simvastatin (at comparable concentrations for viability >80%). This divergence suggests that the distinct pathways targeted of cholesterol esterification versus overall cholesterol synthesis, may differentially influence specific aspects of cancer cell biology, such as proliferation and migration, potentially reflecting their varied contributions to therapy evasion and tumor aggression.

## 2.4 Avasimibe Treatment Enhances CAR-T Induced Cancer Cell Killing in 2D Cancer Cell Models

To evaluate the impact of combining metabolic treatment with CAR-T cell killing on ovarian cancer cells, we conducted cell killing assays on SKOV3 cells. We performed this assay on 96- well plates and read out measurements using a plate reader (Figure S4). For the two groups, we had untreated SKOV3 and treated SKOV3 cells. In the treated group, we incubated SKOV3 cells with 30 µm Simvastatin for 24 h. Then, both groups were followed by coculture with anti-HER2 CAR-T cells for 24 h at an E:T ratio of 1:2. The simvastatin treatment did not provide significant improvement in the CAR-T induced cytotoxicity in SKOV3 cells (Figure 4A). Next, we carried out a cytotoxicity assay with Avasimibe, as presented in Figure 4B. Based on prior evidence that Avasimibe can enhance T cell function [14, 62, 63], we included all combinations of Avasimibe treatment in this assay, treating either the cancer cells, the CAR-T cells, or both. The Avasimibe concentration used for SKOV3 treatment was 30µm for cell viability greater than 80%. For CAR-T cell treatment, the Avasimibe concentration was at 1 m [62]. After 24 h of Avasimibe treatment of SKOV3, the ovarian cancer cells were cocultured with untreated or Avasimibe-treated anti-HER2 CAR-T cells for another 24 h at an E:T ratio of 1:4. The results showed that Avasimibe-treated SKOV3 cells, when cocultured with untreated CAR-T cells, exhibited higher cytotoxicity (54.6%) than the coculture group with untreated SKOV3 and untreated CAR-T cells (43.5%). Notably, treating only the SKOV3 cells led to greater cell death than treating both SKOV3 and CAR-T cells (51.6%) or only the CAR-T cells (46.8%). These results suggest that pretreatment of the ovarian cancer cells is sufficient to improve the CAR-T cell killing. Further validating our findings, the OVCAR5 cell line exhibited a similar synergistic cytotoxicity pattern with Avasimibe treatment (Figure S8C). Specifically, Avasimibe-treated OVCAR5 cells cocultured with untreated CAR-T cells demonstrated the highest cytotoxicity (57.12%). This represents a significant enhancement compared to the untreated OVCAR5 + untreated CAR-T group (33.36%) and was also superior to conditions where only CAR-T cells were treated with Avasimibe (34.5%) or both Ovcar5 and CAR-T cells were treated (39.38%), consistent with the enhanced killing observed in SKOV3 cells under the same conditions.

![](images/507bc81d95b95e5cf440356830a3422ae4b89f632a18ca1095c535cfd31f770e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Immune response"] --> B["Brain with green hexagons"]
  C["Aggression Survival ↑"] --> B
  D["Downstream"] --> B
  E["ACAT-1 T Avasimibe"] --> B
```
</details>

![](images/161f8b341b25cf2f23cecfd5ad21bcdde5b474fdb4ab02a2142320839d26bacd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Mevalonate pathway"] --> B["HMG CoA"]
  B --> C["Acetyl CoA"]
  D["Simvastatin"] --> B
```
</details>

![](images/3fe5a9775ec745737afc1ce7db153a9354e6ae43db0fe7dee1a9b018e62c1042.jpg)

<details>
<summary>text_image</summary>

Protrusion
Ovarian
Cancer Cell
CAR-T cell
Sterol Esters
Triacylglycerols
Free cholesterol
</details>

![](images/bc5696a771ee50f29c0f9aa507b3e1223330c4178691a8946bf2162bee386d66.jpg)

<details>
<summary>text_image</summary>

B
Untreated
SKOV3 +
Avasimibe
SKOV3 +
Simvastatin
Visible h2SRS sum
TAG
Total Cholesterol
</details>

![](images/d73f4a1781b7e29e8262ab14638a2e004a0498d0b9d6e52b00636c4981be952c.jpg)

<details>
<summary>bar chart</summary>

| Group     | Condition | Area Fraction |
| --------- | --------- | ------------- |
| Untreated | TAG       | 0.04          |
| Untreated | FC        | 0.02          |
| Untreated | CE        | 0.02          |
| Ava       | TAG       | 0.04          |
| Ava       | FC        | 0.02          |
| Ava       | CE        | 0.01          |
| Sim       | TAG       | 0.05          |
| Sim       | FC        | 0.01          |
| Sim       | CE        | 0.01          |
</details>

![](images/b641d5e8fe695d6dc663a13c7e4362f5ebe30012921d469509ec831b834fc331.jpg)

<details>
<summary>text_image</summary>

D Fluorescence – Migrated Cells
Untreated Avasimibe Treated
100 µm 100 µm
</details>

![](images/a7d993456238d6d334a5761452c8fcd3e71b5ab07285c2b6bf234f1405195861.jpg)

<details>
<summary>bar chart</summary>

| Treatment       | Migrated Cells (% of Untreated) |
| --------------- | ------------------------------ |
| Untreated       | 100                            |
| 30μM Avasimibe   | 5                              |
</details>

![](images/54fc78ad5c8b10832b11c02558a03f7dc84ab57aa3a457306c025ae6163473ac.jpg)

<details>
<summary>text_image</summary>

F
Fluorescence – Migrated Cells
Untreated	Simvastatin Treated
</details>

![](images/4292180292c8e21ad12561f582ff1f11ac930832d00865d4c4fbda5f7f4e30c5.jpg)

<details>
<summary>bar chart</summary>

| Treatment Group | Migrated Cells (% of Untreated) |
| --------------- | ------------------------------ |
| Untreated       | 100                            |
| 30 µM Simvastatin | 50                             |
</details>

FIGURE 3 Drug intervention of cholesterol metabolism to reduce ovarian cancer aggression. (A) Summary of metabolism changes in ovarian cancer cells as a reaction to immune response and cholesterol metabolism intervention with Avasimibe and Simvastatin. (B) Visible h2SRS imaging TAG and TC maps of untreated, Avasimibe treated, Simvastatin treated SKOV3 cells. Avasimibe concentration: 30 µm, Simvastatin concentration: 10 µm, scale bars: 10 µm. (C) Quantification of cellular TAG, FC, and CE in untreated, Avasimibe treated, Simvastatin treated SKOV3 cells, n>30 per group. (D) Confocal fluorescence imaging of migrated SKOV3 cells with Avasimibe and without Avasimibe. Avasimibe concentration: 30 µm, scale bars: 100µm. (E) Quantification of the migration with and without Avasimibe treatment, n = 3 per group. (F) Confocal fluorescence imaging of migrated SKOV3 cells with Simvastatin and without Simvastatin, Simvastatin concentration: 30 m, scale bars: 100 m. (G) Quantification of the cell migration with and without Simvastatin treatment, n = 3 per group. Data presented as means +/+ std. \*\*\* p<0.001, \*\* p<0.01, TC: Total Cholesterol, FC: Free Cholesterol. CE: Cholesteryl Ester, TAG: Triacylglycerols/Triglycerides.

Intriguingly, our cytotoxicity assays consistently revealed that pretreating only the ovarian cancer cells (SKOV3 or OVCAR5) with Avasimibe, followed by co-culture with untreated CAR-T cells, resulted in the highest cytotoxic efficacy. This suggests an optimal strategy focused on metabolically sensitizing the tumor. Avasimibe-mediated inhibition of ACAT-1 in cancer cells leads to free cholesterol accumulation, inducing cellular stress and enhancing their vulnerability to CAR-T attack. Conversely, while ACAT-1 inhibition can generally boost T cell function, our data suggest that direct pretreatment of CAR-T cells with Avasimibe, under our experimental conditions, may lead to subtle metabolic imbalances or temporary dysregulation that slightly compromises their maximal killing potential. Therefore, the superior outcome appears to stem from combining metabolically compromised cancer cells with fully potent, untreated CAR-T cells, allowing for robust immune effector function against a highly susceptible target. This highlights the importance of precise drug targeting to the tumor to maximize synergistic therapeutic benefits.

![](images/d9a2e434612a4692c1bb385a79bc1084684cd47b829304c51660251f1614d450.jpg)

<details>
<summary>bar chart</summary>

| Group              | CAR-T Cell Induced Cytotoxicity (%) |
| ------------------ | ----------------------------------- |
| Untreated SKOV3    | 56                                  |
| Simvastatin SKOV3  | 53                                  |
</details>

![](images/3ebc0d658e86e61de86d8bd4070a353bad73e61a9076e98f2325df2d22763d53.jpg)

<details>
<summary>bar chart</summary>

| Treatment Group       | Untreated SKOV3 | Avasimibe SKOV3 |
| --------------------- | --------------- | --------------- |
| Untreated CAR-T      | 43              | 54              |
| Avasimibe CAR-T       | 47              | 51              |
</details>

![](images/4dc328cc1845f242694ea275991316fd8cb3ceb4e7228d7121c86b9fabe23931.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing green-labeled cells under three conditions: SKOV3 only, SKOV3 + CAR-T, and SKOV3 + Avasimibe + CAR-T (no text or symbols present)
</details>

![](images/d7b86f366a001391493e3416da94fbab21511ff800cb17314ff2168da3bf3f8c.jpg)

<details>
<summary>bar chart</summary>

| Treatment Group | CAR-T cell induced Cytotoxicity in SKOV3 (%) |
| --- | --- |
| SKOV3 only | ~0 |
| SKOV3 w/ CAR-T | ~55 |
| Avasimibe treated SKOV3 w/ CAR-T | ~75 |
</details>

FIGURE 4 Drug intervention to enhance CAR-T cell induced cytotoxicity in ovarian cancer cells. (A) Cytotoxicity assay of untreated and Simvastatin treated SKOV3 cells with CAR-T cells and simvastatin treatment, n = 15 per group, Simvastatin concentration: 30 µm. (B) Cell killing assay of untreated and Avasimibe treated SKOV3 cells with untreated and Avasimibe treated CAR-T cells, n = 9 per group, Avasimibe concentration: 30 µm for SKOV3 cells and 1 µm for CAR-T cells. (C) Widefield fluorescence imaging of CAR-T-cell mediated cytotoxicity of the SKOV3 cells, scale bars: 100 µm. (D) Quantification of fluorescence imaging for the secondary cytotoxicity assay in C, n = 3 per group. Data presented as means +/± stdev, \*\*\*p<0.001, \*\* p<0.01, \* p<0.05, n.s. non-significant, p>0.05.

We further corroborated these results by adapting these ovarian cancer pre-treatment conditions to 35 mm glass bottom dishes and imaging using a lab-built widefield fluorescence setup described in the methods section. We incubated SKOy3 cells either with treatment of 30 m Avasimibe or no treatment for 24 h. We then added untreated anti-HER2 CA R-T cells at an E:T ratio of 2:1 for a 24-h coculture. As shown in fluorescence images (Figure 4C) and the corresponding quantification presented in Figure 4D, the Avasimibe-treated SKOV3 group showed the highest CAR-T cell induced cytotoxicity (76.4%) than the untreated SKOV3 group (54.6%), each cocultured with untreated CAR-T cells.

![](images/8ca3e7c071018a6f690037baea54ca42288429eeac7f97a5dda9018bb2c62ae5.jpg)

<details>
<summary>3d surface plot</summary>

| Cell Type | Value (µm) |
|-----------|------------|
| SKOV3 only | 636.4      |
| SKOV3 only | 636.4      |
| SKOV3 only | 286.3      |
</details>

![](images/7c006ad76d526b533f7e7c4bb9f3f12149ffb4624367b8348b5e4e54019f9d3e.jpg)

<details>
<summary>text_image</summary>

B Untreated SKOV3 + 1:1 CAR-T
636.4 µm x 636.4 µm x 185.7 µm
</details>

![](images/a8ce63a7b7fac0125fa7ab12e1b2a7eaf97bb553907250e360c58911b326f1b3.jpg)

<details>
<summary>heatmap</summary>

| Value Range | Color  |
|-------------|--------|
| 50          | Red    |
| 100         | Green  |
</details>

![](images/55c2b0870164a45d0c78b36aa84f833aa4e47ec9b959fee0b9197e50a9129d36.jpg)

<details>
<summary>bar chart</summary>

| Treatment Group | Untreated SKOV3 | Ava SKOV3 |
| --------------- | --------------- | --------- |
| No CAR-T        | 0.04            | -         |
| 1:1 CAR-T       | 0.19            | -         |
| 5:1 CAR-T       | 0.42            | 0.62      |
</details>

![](images/d4c0b7166df2a68f104cb1d1bfb569e415352f02626f2104bfcb5601169aebda.jpg)

<details>
<summary>text_image</summary>

E Untreated SKOV3 + 5:1 CAR-T
636.4 µm x 636.4 µm x 129.8 µm
</details>

![](images/6f523fa8552caedcd3f5fadb496671845f1c80bf1fc6db1789e05a33fcd6982f.jpg)

<details>
<summary>3d scatter plot</summary>

| Value Range | Count |
| ----------- | ----- |
| 636.4 µm x 636.4 µm x 158.4 µm | 636.4 µm |
</details>

Avasimibe amplifies CAR-T induced cytotoxicity in 3D SKOV3 spheroids. (A–E) Confocal fluorescence imaging of GFP-SKOV3 cells spheroids incubated in various treatment conditions (A) Untreated, (B) Untreated spheroids incubated with CAR-T cells in E:T = 1:1, (C) Avasimibe treated spheroids incubated with CAR-T cells in E:T = 1:1, (D) Avasimibe treated spheroids incubated with CAR-T cells in E:T = 5:1, (E) Untreated spheroids incubated with CAR-T cells in E:T = 5:1. (F) Quantification of the spheroids cytotoxicity assay using plate reader, n = 3 per group. Data presented as means $+ / \pm$ stdev, \*\*\*p<0.001, \*\* p<0.01, \* p<0.05.

## 2.5 Avasimibe Treatment Enhances CAR-T Induced Cell Killing in 3D Tumor Spheroids

We further extended the CAR-T cell induced cell killing assay to a 3D spheroids model. As has already been established in earlier studies, 3D spheroid models resemble the tumor microenvironment more closely than 2D cell cultures [64, 65]. We used GFP-SKOV3 cells to formulate 3D spheroids in ultra-low attachment 96-well plates. We incubated the GFP-SKOV3 cells in these plates for 48 h until the spheroids formed and then cultured them with or without Avasimibe for the next 24 h. We then added untreated anti-HER2 CAR-T cells in either a 1:1 E:T ratio as a reference condition or a 5:1 E:T ratio to assess enhanced cytotoxicity. We used the cytotoxicity index, the ratio of dead cells to the total dead and live cells in the spheroids, to analyze the effect on cell killing efficacy. The confocal fluorescence images of the spheroids shown in Figure 5A–E clearly indicate a positive impact of Avasimibe treatment on CAR-T induced cytotoxicity. Furthermore, as quantified using a plate reader and shown in Figure 5F, the cytotoxicity enhancement is the highest at 0.62 in the Avasimibe-treated spheroids cocultured with CAR-T cells in a 5:1 E:T ratio. The comparable cytotoxicity indices in the 1:1 E: T reference groups, 0.21 for Avasimibetreated and 0.19 for untreated spheroids (with not a statistically significant difference), indicate that Avasimibe does not induce cytotoxicity in SKOV3 spheroids in the absence of robust CAR-T cell activity, at the same time, its potentiating effect is evident at higher E: T ratios. To confirm that Avasimibe alone does not exert cytotoxic effects on SKOV3 spheroids, we assessed spheroid viability following Avasimibe treatment without CAR-T cells. As shown in Figure S10, the cytotoxicity index for SKOV3 spheroids treated with Avasimibe was 0.019, identical to that of untreated SKOV3 spheroids (0.019), thereby excluding any direct cytotoxic effects of Avasimibe alone in this 3D model. Taken together, these results indicate that Avasimibe pre-treatment of ovarian cancer cells improves the cytotoxicity induced by CAR-T cells.

## 2.6 Cytokines Impact Lipid and Cholesterol Metabolism in Cancer Cells

The immune response by CAR-T cells involves a release of pro inflammatory cytokines including Interleukin-2 (IL-2), Tumor

Necrosis Factor-alpha (TNF-α), and Interferon-gamma (IFNγ) [66]. These cytokines have essential anti-tumor functions, including enhancing cytotoxic T-cell activity and inducing tumor apoptosis. On the other hand, it is also known that cytokines have myriads of functions that impact cancer cell growth and metabolism depending on the tumor microenvironment and immune state [67]. To examine the molecular mechanism of cholesterol and triglycerides upregulation in ovarian cancer cells in the presence of CAR-T cells, we studied the impact of inflammatory cytokines on cancer cell metabolisms. As shown in Figure 6A, we acquired NIR h2SRS images of SKOV3 cells incubated with complete culture medium with and without the supplementation of the inflammatory cytokines and focused on TAG and TC maps. We analyzed the TAG and TC maps (Figure 6B), which revealed that both the fractions were upregulated in the SKOV3 cells treated with the cytokines, 2.3-fold and 2.94-fold with IL-2, 3.15-fold and 4-fold with TNF-α, 2.27-fold and 3.19-fold with IFN-γ, respectively. Notably, incubation with TNFα showed the most impact among all the other cytokines. TNF-α has been shown to help in cancer progression and metastasis, which correlates with cholesterol upregulation in cancer cells [36, 68]. With this knowledge and migration as an indicator of metastatic potential and aggression, we conducted migration assays of SKOV3 cells cultured in culture medium with and with out supplementation of the cytokines as shown in Figure 6C,D. As expected, the TNF-α incubated cells showed the highest migration increase by nearly 100% compared to the untreated group. IFN-γ and IL-2 have complex roles in tumor progression and metastasis [66–68]. In our results, IFN-γ treatment led to only a mild increase in migration (13.6%), while IL-2 treatment resulted in a more substantial increase (71.2%) relative to the untreated group. While pro-inflammatory cytokines such as TNF-α, IFNγ, and IL-2 are known to have essential anti-tumor functions and are critical for immune activation, our results highlight that, under certain conditions, these same cytokines may paradoxically enhance cancer cell aggressiveness.

To directly establish a causal link between CAR-T–secreted cytokines and metabolic reprogramming in SKOV3 cells, we performed coculture experiments with anti-HER2 T cells in the presence of neutralizing antibodies against TNF-??, IFNγ, and IL-2, followed by quantitative analysis of TAG and TC levels using SRS imaging (Figure S7). These functional blocking experiments revealed direct, cytokine-specific, and lipid-classdependent regulation of SKOV3 lipid metabolism. Blocking IFN-γ or IL-2 activity largely restored TC levels to those of untreated SKOV3 cells, indicating that these cytokines are key mediators of CAR-T–induced cholesterol accumulation. In contrast, TNF-?? neutralization only partially attenuated TC elevation, suggesting a contributory but non-exclusive role in TC regulation. Strikingly, TAG levels exhibited a distinct response pattern: IFN-γ blockade restored TAG to baseline, whereas TNF- neutralization reduced TAG levels to approximately 0.5-fold of untreated controls, indicating a particularly nuanced role for TNF-?? in regulating lipid storage pathways. IL-2 blocking had a minimal impact on TAG levels, suggesting that IL-2 does not play a dominant role in TAG accumulation in this context. Collectively, these results demonstrate that CAR-T-secreted cytokines directly and differentially regulate cholesterol and triglyceride metabolism in SKOV3 cells through overlapping but distinct mechanisms.

## 3 Discussion

CAR-T cell therapy is promising for liquid tumors, and its application in solid tumors, such as highly lethal ovarian cancer, is vital [1, 2]. Numerous research studies have demonstrated distinct metabolic regulations within a tumor microenvironment [3, 10]. Several studies have also shown that metabolic reprogramming is a crucial factor in cancer survivability and evasion of immune response [9, 12, 49]. Despite these studies, there is a paucity of research on the direct metabolic impact of T-cell response on cancer cells. In this work, we employed NIR and visible h2SRS microscopy to investigate the metabolism modulation in ovarian cancer cells that survived the CAR-T cell attack. We noticed TC and TAG augmentation and protrusion development in the surviving ovarian cancer cells in the presence of CAR-T cells. These observable effects have been associated with increased cancer aggression and migration [15, 38, 48, 58], which might help cancer cells evade CAR-T cell response. Further, the dissection of LDs using Visible h2SRS also showed an upregulation of the CE and FC within the cancer cells, suggesting a metabolic modulation as a survival mechanism [33, 37–41]. This observation allowed us to choose drugs for metabolic intervention, helping enhance CAR-T cell anti-tumor response. Furthermore, the reproducibility of our key findings about CAR-T induced lipid metabolic reprogramming and the synergistic effect of Avasimibe in the SKOV3 and the OVCAR5 cell lines provides critical support for the generalizability of this adaptive resistance mechanism beyond single cell line. While ovarian cancer is highly heterogeneous, these results suggest that targeting ACAT-1 may offer a broadly applicable strategy to enhance CAR-T cell efficacy. Through various approaches, including a 3D spheroid culture model, we concluded that cholesteryl esterification inhibition using Avasimibe helps improve the CAR-T cell-induced cell killing in ovarian cancer. Future studies will involve expanding this analysis to a wider panel of ovarian cancer subtypes and in vivo models to further validate these findings.

Our findings also reveal a multifaceted role for cholesterol metabolism in ovarian cancer aggression, demonstrating that Simvastatin is more potent at inhibiting proliferation while Avasimibe is more effective at suppressing migration. This distinction is biologically significant: free cholesterol is indispensable for cell membrane synthesis and rapid cell division, explaining Simvastatin’s robust antiproliferative effect. In contrast, cholesteryl esters, stored in lipid droplets, are increasingly implicated in supporting cancer cell invasiveness and adaptability, aligning with stronger impact of Avasimibe on migration [54]. This differential impact on distinct aggressive phenotypes underscores the complexity of targeting lipid metabolism. Remarkably, the superior cytotoxicity observed with CAR-T cells in combination with Avasimibe pretreatment, compared to Simvastatin, directly correlates with greater efficacy of Avasimibe in suppressing cell migration. This could suggest that modulating phenotypes related to cancer cell invasiveness, such as migration, which can contribute to immune evasion by facilitating escape from immune surveillance or growth of a more therapy resistant tumor, plays a more critical role than solely reducing proliferation in enhancing CAR-T sensitivity in our model. Thus, our focus on cholesterol esterification as a key adaptive mechanism influencing CAR-T sensitivity is strongly supported by these distinct functional outcomes. Importantly, our findings further highlight that the timing and cellular target of metabolic intervention are critical determinants of therapeutic synergy, in addition to the metabolic pathway targeted, as selective sensitization of tumor cells while preserving CAR-T cells in a fully functional state may represent a more effective strategy than indiscriminate modulation of both cellular compartments.

A  
![](images/fc71e5c2ef46b9fd24beed6d3f66bb5d0d911527aa2c8e13e60f3314d3d00769.jpg)

<details>
<summary>text_image</summary>

SKOV3 only
SKOV3 + 100 IU/mL IL-2
SKOV3 + 10ng/mL TNF-α
SKOV3 + 5ng/mL IFN-γ
TAG
TC
</details>

B  
![](images/b821289276ba1babb2e3f24d79fec5e52efa21cc1d3fadb8a8e6b3940f3eddcc.jpg)

<details>
<summary>bar chart</summary>

| Group     | TAG   | TC    |
| --------- | ----- | ----- |
| Untreated | 0.06  | 0.05  |
| IL-2      | 0.13  | 0.12  |
| TNF-α     | 0.18  | 0.17  |
| IFN-γ     | 0.14  | 0.13  |
</details>

C

![](images/008253914586121678e33f39fb93d107ea89c0f6f5e6f26a770320f03205bcbf.jpg)

<details>
<summary>bar chart</summary>

| Treatment    | Migrated cells (%) |
| ------------ | ------------------ |
| Untreated    | 100                |
| IL-2         | 170                |
| TNF-α        | 200                |
| IFN-γ        | 110                |
</details>

FIGURE 6 | Impact of cytokines on metabolism and aggressiveness of SKOV3 cells. (A) TAG and TC NIR h2SRS imaging maps of SKOV3 cells with and without cytokines: IL-2, TNF-??, IFN-?? supplemented media for SKOV3 cells, IL-2 Concentration: 100 IU/mL, TNF-?? Concentration: 10 ng/mL, IFN- Concentration: 5ng/mL, scale bars: 10 m. (B) Quantification of cellular TC and TAG in SKOV3 cells incubated with medium with and without cytokines supplementation, n>31 per group. (C) Confocal fluorescence imaging of migrated SKOV3 cells with and without cytokines, scale bars: 100 µm. (D) Quantification of the cell migration with and without Cytokines treatment, n = 3, \*\*\* p<0.001, \*\* p<0.01, data presented as means +/± stdev, TC: total cholesterol. TAG: triglycerides/triacylglycerols.

CAR-T cells release pro-inflammatory cytokines, particularly IL-2, TNF-α, and IFN-γ, which can directly and indirectly affec tumor cells. These cytokines are critical for mediating anti tumor immunity: IL-2 promotes the proliferation and persistence of cytotoxic T cells, IFN-γ enhances antigen presentation, and TNF-α can induce tumor cell apoptosis [66–69]. However, these same cytokines can also contribute to tumor progression by promoting cancer cell survival, metabolic reprogramming, and migration, particularly in an inflammatory tumor microenvironment. Thus, we examined and validated that the lipid metabolic changes observed in surviving SKOV3 cells may result, at least partially, from cytokines among other reasons [33, 38–40]. We further observed that cytokine supplementation increased ovarian cancer cell migration capacity. TNF-α led to the highest TC and TAG increase and a significant increase in ovarian cancer cell migration. This result is reasonable given that TNF-α, in addition to anti-tumor activity, is also known to have some pro-tumorigenic effects like cancer progression and migration by promoting epithelial to mesenchymal transition [36, 68], and the cancer migration is also linked to cholesterol upregulation in cancer cells [38]. The cytokines IL-2 and IFN-γ also show pro-tumorigenic effects like immune exhaustion and cancer migration promotion [67, 69], although not as significant as TNF-α. Furthermore, our functional cytokine-blocking experiments demonstrate that CAR-T secreted cytokines play a central and functionally important role in the lipid metabolic reprogramming observed in SKOV3 cells. The cytokine-specific and divergent regulation of TC and TAG, particularly the distinct and multifaceted role of TNF-α, highlights that different lipid classes are governed by partially separable inflammatory signaling pathways. These findings provide important mechanistic insight into how the immune microenvironment actively reshapes tumor cell metabolism in response to CAR-T attack. Importantly, they support a model in which adaptive changes in cholesterol and triglyceride metabolism that contribute to CAR-T resistance arise as a consequence of cytokine-driven immune pressure, thereby reinforcing the therapeutic rationale for targeting tumor lipid metabolism to enhance immunotherapy efficacy

We observed that inhibiting cholesterol esterification in the cancer cells significantly improved the CAR-T cell-induced cytotoxicity against cancer cells compared to inhibition of cholesterol synthesis. CE accumulation is a sign of metabolic reprogramming in cancer, where excess cellular cholesterol and fatty acids are known to be stored in LDs as CE through cholesterol esterification catalyzed by ACAT-1 [37, 48] to avoid lipotoxicity and help with cancer cell survival under stress. Recent findings show that, more than the cholesterol component alone, fatty acids play a crucial role in cancer progression, membrane synthesis, and resistance to ferroptosis or oxidative stress [37, 48, 54, 70, 71]. Cholesteryl esters often comprise arachidonic acid (AA), a polyunsaturated fatty acid, which is a key element in inflammation and is metabolized into compounds that have been shown to promote tumor progression, immune suppression, and resistance to therapy [54, 72]. The LDs rich in CE, serving as lipid reservoirs, have shown to increase the metastasis and proliferation of the cancer cells. Diminishing the CE-rich lipid droplets by ACAT-1 inhibition using Avasimibe helps increase the cancer cell sensitivity through altered membrane dynamics and increased endoplasmic reticulum stress and reduces the cancer cell aggressiveness [48]. Inhibiting the mevalonate pathway using statins has been shown to have a compensatory augmentation of SREBP activation and other ways of cholesterol upregulation [73]. Thus, targeting cholesterol esterification may be more advantageous than targeting the cholesterol pathway directly.

Our findings provide strong pharmacological evidence that targeting ACAT-1–mediated cholesterol esterification with Avasimibe enhances CAR-T cell cytotoxicity. While this strategy demonstrates significant translational potential, we acknowledge that the definitive establishment of ACAT-1 as a necessary factor conferring CAR-T resistance would require genetic validation, such as ACAT-1 knockdown or knockout approaches. In addition, direct assessment of ACAT-1 expression and regulation following CAR-T cell challenge would further clarify its mechanistic role. These experiments represent important priorities for future studies aimed at moving beyond pharmacological association to establish causality.

Visible h2SRS uses visible lasers with extensive pulse chirping and noise suppression for imaging, which leads to a higher resolution than NIR h2SRS [28]. This improvement in resolution allowed us to examine the lipid droplets. It was pivotal in analyzing lipid droplets, revealing changes in CE and FC levels in ovarian cancer cells, and offering insight into metabolic changes that support them. Thus, Visible h2SRS, with its high resolution and labelfree chemical imaging inside the cells, holds much promise in studying diseases with metabolic dysregulations, especially in lipid droplets and cholesteryl esters. For example, in addition to other solid cancers, neurodegenerative diseases like Alzheimer’s, Parkinson’s, and Huntington’s diseases show altered lipid droplet dynamics and cholesterol metabolism [74]. Exploring cellular metabolism in these diseases using Visible h2SRS would be beneficial to understand these dynamics, label-free, and for therapeutic discovery.

Although Visible h2SRS provides high spatial resolution, it has its limitations. We only studied the cell metabolism in the high-wave-number (C–H) region. The C–H region compromises chemical specificity because of the presence and overlap of many signature peaks of chemicals in this region [31]. High-content SRS imaging in the fingerprint region would provide a comprehensive observation of the metabolism changes in the pathways, not limited to only lipids [31, 45]. Furthermore, Visible SRS imaging suffers from photodamage and limited penetration depth, which is unsuitable for biological tissue imaging. Imaging modalities, like NIR h2SRS in the fingerprint region, provide more benefit in tissue imaging and facilitate access to more detailed metabolic information, like amino acids, fumarate. Alternative methods using infra-red (IR) laser like, mid-infrared photothermal (MIP) microscopy also can be used to achieve submicron spatial resolu tion imaging and in the fingerprint region by detecting thermal expansion induced by IR using a visible probe [75], which has also been used to map the drug distribution successfully and might help in investigating how drug intervention helps enhance CAR-T cell induced cytotoxicity. These imaging modalities are promising tools that can be used to investigate metabolism modulation in various diseases, including but not limited to cancer.

## 4 Materials and Methods

## 4.1 Cell Culture Preparation

SKOV3 cells (purchased from American Type Culture Collection) for 2D culture and GFP-SKOV3 (generous gift from Dr. Matei Lab, Northwestern University) for 3D spheroids were cultured in the DMGM Basal Medium (Cell applications, MCBD 105 Medium and Corning, Medium 199 1X combined 1:1) supplemented with 10% fetal bovine serum (FBS) and 1 X penicillin/streptomycin (P/S; 100 U/ml). OVCAR5 cells (generous gift from Dr Marcus Peter, Northwestern University) were cultured in the RPMI 1640 Medium (Thermo Fisher Scientific, 22400089) supplemented with 10% FBS and 1X P/S. For the Anti HER2 CAR-T cells, normal whole peripheral blood from deidentified donors was obtained from Boston Children’s Hospital. Primary human CD3+ T cells were isolated from anonymous healthy donor blood by negative selection (STEMCELL, 15621). T cells were cultured in human T cell medium consisting of X-Vivo 15 medium (Lonza, 04418Q), 5% Human AB serum (Valley Biomedical, HP1022), 10 mm N-acetyl L-Cysteine (Sigma–Aldrich, A9165), 55 µm 2-mercaptoethanol (Thermo Fisher Scientific, 31350010) supplemented with 50 units/mL IL-2 (NCI BRB Preclinical Repository). T cells were cryopreserved in 90% heat-inactivated FBS and 10% DMSO. All the cells were cultured and maintained in an incubator with 5% $\mathrm { C O } _ { 2 }$ and 80%–90% humidity at $3 7 ^ { \circ } \mathrm { C } .$ . We prepared coculture samples in an E:T ratio of 1:2 in 35 mm glass bottom dishes and fixed them with 10% formalin for h2SRS imaging. The coculture cell samples were prepared following the protocol shown in Figure S1A. For the cytokines treated imaging, we cultured SKOV3 cells with complete culture medium supplemented with 100 IU/mL IL-2 (NCI BRB Pre clinical Repository), 10 ng/mL TNF-?? (Thermo Fisher Scientific, PHC3011), 5 ng/mL IFN-?? (Thermo Fisher Scientific, PHC4033) respectively for 24 h. The cells were then fixed with a 10% formalin solution before imaging. For the cytokines blocking experiment, we co-cultured SKOV3 cells with anti-HER2 T cells in their own complete medium supplemented with 5 µg/mL human IL-2 antibody (R&D systems, MAB202), 5 µg/mL human IFN-?? antibody (R&D systems, MAB285), 5 µg/mL human TNF-?? antibody (R&D systems, MAB610) or all 3 antibodies and untreated SKOV3 only for control. The cells were then fixed with a 10% formalin solution before imaging.

## 4.2 Lentiviral Transduction of Human T Cells

Second-generation lentivirus was packaged via transfection of lentixHEK 293 cells (Takara) with a pHR transgene expression vector and the viral packaging plasmids: pMD2.G encoding for VSV-G pseudotyping coat protein (Addgene, 12259), pDelta 8.74 (Addgene, 22036), and pAdv (Promega). One day after transfection, viral supernatant was harvested every 24 h for 3 days and replenished with pre-warmed FreeStyle 293 expression media (Gibco) with 2 mm L-glutamine, 100 U/ml penicillin, 100 ug/mL streptomycin, 1 mm sodium pyruvate, and 5mm sodium butyrate. Then, 4X PEG8000 lentivirus concentrator was added to the harvested virus, and the mixture was incubated overnight before spinning at 1600xG for 50 min. Primary T cells were thawed 2 days before virus purification and cultured in the T cell medium described above. One day before virus centrifugation, T cells were stimulated with Human T-activator CD3/CD28 Dynabeads (Thermo Scientific #11132D) at a 1:1 cellto-bead ratio and cultured for 24 h. After viral supernatant purification, rectronectin (Clontech #T100B) was used to mediate T-cell transduction. Briefly, non-TC-treated 6-well plates were coated with rectronectin following the supplier’s protocol. Then, concentrated viral supernatant was added to each well and spun for 90 min at 1200xG. After centrifugation, the viral supernatant was removed, and 4 mL of human T cells at 250k/ml in T cell growth media supplemented with 100U/ml of IL-2 was added to the well. Cells were spun at 1200xG for 60 min and moved to an incubator at $3 7 ^ { \circ } \mathrm { C } .$ To confirm successful transduction and CAR expression, flow cytometry was performed on our CAR-T cells post-transduction and expansion, prior to their use in co-culture experiments and a consistent high positive rate was achieved as in Figure S1B (92.5%).

## 4.3 Cell Viability and Proliferation Assay

The cell viability assay was conducted using the MTS reagent (Abcam, ab197010) in 96 well plates. SKOV3 cells were seeded in 96 well plates at the density of 5000–15 000 cells per well and incubated for 24 h, followed by the addition of the drug at the mentioned concentrations and incubated for another 24 h. Then. the MTS reagent was added to the plate so that the culture medium to MTS reagent ratio was 5:1, and the mixture was incubated for 1h. The absorbance was then read at 490 nm [76] using a plate reader (i3X SpectraMax Molecular Devices). The step-by-step protocol is shown in Figure S2A. The treatment concentrations were selected so that they were sublethal (>80% viability) to study cell responses without causing immediate cell death, as shown in Figure S2B,C. This criterion also applies to cytokines, as they did not show significant toxicity to the SKOV3 cells, as shown in Figure S2B. The cell proliferation assay was conducted using the MTS reagent in 96 well plates as well. SKOV3 cells were seeded in 4 separate 96 well plates at a density of 600 cells per well. The MTS read was then acquired on Days 1, 3, 5, and 7 replenishing the culture medium and treatment doses every remaining plate. The step-by-step protocol is shown in Figure S9A.

## 4.4 Migration Assay and Confocal Fluorescence Imaging

Migration assays were conducted using trans-well membranes (Corning, CLS3401). SKOV3 cells were seeded onto 35 mm cell culture dishes till 70% confluence. Then, the drugs at the mentioned concentration were added to respective dishes. and the cells were incubated for 24 h. A culture medium supplemented with 20% FBS was added to the wells in 24 well plates, and the drugs at the mentioned concentrations. The cells were then detached from the dishes and seeded onto the upper chamber of the trans-well membranes with culture medium only and no FBS. The drugs at respective concentrations were added to the top chamber. The cells were then incubated for 24 h, followed by fixation with 10% formalin. The upper chambers of trans-well membranes were then cleaned with cotton swabs to remove nonmigrated cells. The migrated cells were then dyed with propidium iodide for 30 min at a concentration of 50µgmL−1 . We acquired confocal fluorescence images (excitation 561 nm, emission 570– 620 nm) using a laser scanning confocal microscope (Olympus FV3000, Micro/Nano Imaging Facility, Boston University) and quantified them using ImageJ. Drugs used were Avasimibe, purchased from Selleck Chemicals, and Simvastatin, purchased from Thermo Fisher Scientific. A step-by-step protocol is shown in Figure S3.

## 4.5 CAR-T Cell Cytotoxicity Assays

48 h before assay, SKOV3 cells were seeded in 96-well plates at a density of 15 000–20 000 cells per well and incubated for 24 h. Then, drugs were added at the mentioned concentrations, and the cells were incubated with dosed media for another 24 h. 24 h before assay, anti-HER2 CAR-T cells in their respective culture media were treated with drugs at the mentioned concentrations, if any. On the day of assay, SKOV3 cells were incubated with the green cell proliferation fluorescent agent (Abcam, ab176735) following the manufacturer’s protocol before coming into contact with CAR-T cells. Anti-HER2 CAR-T cells in various drug treatment conditions were added to SKOV3 cells at an appropriate E:T ratio. The coculture was incubated overnight before fluorescence read (excitation 488 nm, emission 511–525 nm), using a plate reader to assess target cell viability. A step-by-step protocol is shown in Figure S4. A minimum of 9 wells per group were analyzed. For the secondary imaging validation, SKOV3 cells were seeded in the glass-bottom dishes at a density of 25 000 to 50 000 cells per dish for 24 h. Then, the cells were incubated with Avasimibe at the specified concentration in the culture medium for 24 h. Before the assay, the cells were incubated with the green proliferation dye following the manufacturer’s protocol. Anti-HER2 CAR-T cells in their respective culture medium were added at the E:T ratio of 2:1 and incubated for 24 h. At the end of the coculture assay, the cells were fixed with 10% formalin before acquiring 6 fluorescence images per dish with our lab-built microscope using an Olympus IX71 microscope frame and 20x air objective (excitation 470 nm, emission 500–540 nm) [77]. The images were analyzed using ImageJ.

For the 3D spheroids cytotoxicity assay, Green Fluorescence Protein (GFP) -SKOV3 cells were seeded in ultra-low attachment round-bottom 96-well plates at a density of 8000 cells per well and incubated for 48 h till the spheroids formed. The drugs were then added at the mentioned concentrations, and spheroids were incubated with dosed media for another 24 h. Anti-HER2 CAR-T cells in their respective culture media were then added to the CAR-T treatment spheroids group in the appropriate ratios and cultured for 24 h. The dead cells in the spheroids were then dyed with propidium iodide for 1 h at a concentration of 5 gmL−1 . We acquired confocal fluorescence images (excitation 561 nm, emission 570620 nm for PI: excitation 488 nm. emission 500-

540 nm for GFP) using a laser scanning confocal microscope (Olympus FV3000, Micro/Nano Imaging Facility, Boston University) and acquired fluorescence reads (excitation 535 nm, emission 617 nm for PI; excitation 488 nm, emission 510 nm for GFP) using a plate reader (i3X SpectraMax Molecular Devices) for the quantification. A step-by-step protocol is shown in Figure S5.

## 4.6 High-Content Stimulated Raman Scattering Imaging

High Content SRS (h2SRS) imaging is a method involving hyperspectral Stimulated Raman Scattering (hSRS) imaging followed by denoising and spectral unmixing of the hyperspectral data using pixel-wise least absolute shrinkage and selection operator (LASSO) into biochemical maps [27, 28, 31, 32]. In this project, we used NIR hSRS and Visible hSRS.

## 4.7 NIR hSRS Imaging Setup

Our lab-built NIR hSRS system [31] is based on a dual-output laser (Insight DeepSee+, Spectral Physics), as shown in Figure 1A Hyperspectral imaging was achieved using the spectral focusing method by the temporal delay between pump and stokes beams, where both the femtosecond beams were chirped using glass rods to generate picosecond pulses and take hyperspectral stack image [31, 78]. We acquired an hSRS image stack for the cells in the C-H wavenumber region in the range from 2820 to 3050 cm−1 with Stokes beam (wavelength, 1040 nm) at 150mW and Pump beam (wavelength, 800 nm) at 30 mW measured before the galvo mirror.

## 4.8 Visible hSRS Imaging Setup

Our lab-built visible hSRS system [28] is based on two broadband femtosecond visible lasers, as shown in Figure 2A. The setup utilized a dual-output laser (Insight X3, Spectra Physics) where the output wavelengths of 906 and 1045 nm were used to obtain 453 and 523 nm through second harmonic generation. Hyperspectral imaging was achieved using the spectral focusing method, as mentioned previously in the NIR hSRS setup and detailed in [28]. We acquired the hyperspectral imaging data for the cells in the C-H wavenumber region as described above with Stokes beam (wavelength, 523 nm) at 30 mW and Pump beam (wavelength, 453 nm) at 20 mW measured before the galvo mirror.

## 4.9 Self-Supervised Elimination of Non-Independent Noise (SPEND) Denoising

We applied Self-Supervised Elimination of Non-Independent Noise (SPEND) denoising to the Visible SRS hyperspectral data to improve the resolution further. SPEND is a self-supervised deep learning denoising framework for removing non-independent noises in hyperspectral images. Details can be found in [79]. In this study, the SPEND model was trained on an NVIDIA RTX 4090 GPU with 24 GB of memory, requiring approximately 1 h for competition. The input dataset contains 24 fields of view. Each field of view contains 400 × 400 × 100 pixels. Data augmentation was performed using flipping and rotation, resulting in a fourfold increase in the effective dataset size. During interference, the model processes each field of view in 2.4 s.

## 4.10 LASSO Spectral Unmixing and Map Analysis

Then, we used the pixel-wise LASSO method for the spectral unmixing of the hyperspectral stack into chemical maps of lipid, protein, cholesterol, and nucleic acid [31]. It is a least square fitting problem with L1-norm regularization with the parameter λ used to control each chemical component’s sparsity level. The regularization is based on the observation that at each pixel, only a few chemical components contribute dominantly [31]. The unmixing is implemented using acquired hSRS spectra for pure solutions of protein (Bovine Serum Albumin, BSA), lipid (Trioleate Glycerol, TAG), cholesterol, and nucleic acid (RNA solution) and carbohydrates (Glucose) as reference inputs for the operator wherever specified (Spectra shown in Figure S6). The LASSO parameter, λ, was as follows for NIR h2SRS: $\lambda _ { T A G }$ $= 0 . 0 5 , ~ \lambda _ { p r o t e i n } = ~ 0 . 0 5 , ~ \lambda _ { c h o l e s t e r o l } = ~ 0 . 0 9 , ~ \lambda _ { R N A } = ~ 0 . 0 9 .$ . The LASSO parameter, λ, was as follows for Visible h2SRS: $\lambda _ { T A G } =$ $0 . 0 2 , \lambda _ { p r o t e i n } = 0 . 0 3 , \lambda _ { c h o l e s t e r o l } = 0 . 0 4 7 5 , \lambda _ { R N A } = 0 . 0 1 , \lambda _ { G l u c o s e }$ = 0.02 or a single λ = 0.01 for all biochemical maps. For the TC and TAG map analysis generated using both NIR and Visible h2SRS, we used Fiji (ImageJ). We quantified the TC and TAG in NIR h2SRS maps using ImageJ by applying a threshold based on intensity and calculating the area fraction for each out of the total cell area [37]. We used the same method for the cholesteryl ester (CE), free cholesterol (FC) and TAG quantification using Visible h2SRS maps. To generate cholesteryl ester maps, we first generated a mask using TAG maps by applying a threshold to pick up only the LDs. Then, we calculated the overlap between the TAG masks and TC maps to get a cholesteryl ester map. Then, we calculated the FC fraction as a difference between TC and CE. We analyzed a minimum of 30 cells per group for statistical analysis.

## 4.11 Statistical Analysis

The statistical graphs were shown as means +/± stdev unless specified otherwise. The statistical analysis was done using unpaired t-test between treated and untreated groups and using OriginPro. Statistical significance was denoted as \* for p<0.05, \*\* for p<0.01, \*\*\* for p<0.001, and n.s. for p>0.05, indicating a non-significant statistical difference.

## Acknowledgements

Research reported in this publication was supported by the Boston University Micro and Nano Imaging Facility and the Office of the Director, National Institutes of Health of the National Institutes of Health under Award Number S10OD024993. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institute of Health. We thank Dr. Daniela Matei. Dr. Ana Maria Isaac, and Dr. Hao Huang from the Department of Obstetrics and Gynecology, Feinberg School of Medicine, Northwestern University (Chicago, IL 60611), for generously providing the GFP-SKOV3 cells. Their support was inyaluable to this study.

## Funding

This work was funded by NIH grants R35GM136223 and R01CA224275 to J.X.C.

## Conflicts of Interest

The authors declare no conflicts of interest.

## Data Availability Statement

All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Correspondence and requests for materials should be addressed to J.X.C.

## References

1. L. A. Torre, B. Trabert, C. E. DeSantis, et al., “Ovarian Cancer Statistics,” CA: A Cancer Journal for Clinicians 68 (2018): 284–296.  
2. X. Zhu, H. Cai, L. Zhao, L. Ning, and J. Lang, “CAR-T Cell Therapy in Ovarian Cancer: From the Bench to the Bedside,” Oncotarget 8 (2017): 64607–64621.  
3. Y. Tan, J. Li, G. Zhao, et al., “Metabolic Reprogramming From Glycolysis to Fatty Acid Uptake and Beta-Oxidation in Platinum-Resistant Cancer Cells,” Nature Communications 13, no. 1 (2022): 4554.  
4. U. Blache, G. Popp, A. Dünkel, U. Koehl, and S. Fricke, “Potential Solutions for Manufacture of CAR T Cells in Cancer Immunotherapy,” Nature Communications 13 (2022): 5225.  
5. G. Guzman, M. R. Reed, K. Bielamowicz, B. Koss, and A. Rodriguez, “CAR-T Therapies in Solid Tumors: Opportunities and Challenges,” Current Oncology Reports 25 (2023): 479–489.  
6. J. L. Tanyi, C. Stashwick, G. Plesa, et al., “Possible Compartmental Cytokine Release Syndrome in a Patient With Recurrent Ovarian Cancer After Treatment With Mesothelin-targeted CAR-T Cells,” Journal of Immunotherapy 40 (2017): 104–107.  
7. R. C. Sterner and R. M. Sterner, “CAR-T Cell Therapy: Current Limitations and Potential Strategies,” Blood Cancer Journal 11 (2021): 69.  
8. F. Korell, T. R. Berger, and M. V. Maus, “Understanding CAR T cell Tumor Interactions: Paving the Way for Successful Clinical Outcomes,” Med 3 (2022): 538–564.  
9. J. Traba, M. N. Sack, T. A. Waldmann, and O. M. Anton, “Immunometabolism at the Nexus of Cancer Therapeutic Efficacy and Resistance,” Frontiers in Immunology 12 (2021): 657293.  
10. A. Hirayama, K. Kami, M. Sugimoto, et al., “Quantitative Metabolome Profiling of Colon and Stomach Cancer Microenvironment by Capillary Electrophoresis Time-of-Flight Mass Spectrometry," Cancer Research 69 (2009): 4918–4925.  
11. C. Yan, L. Zheng, S. Jiang, et al., “Exhaustion-Associated Cholesterol Deficiency Dampens the Cytotoxic Arm of Antitumor Immunity,” Cancer Cell 41 (2023): 1276–1293.  
12. C. Mateiou, L. Lokhande, L. H. Diep, et al., “Spatial Tumor Immune Microenvironment Phenotypes in Ovarian Cancer,” NPJ Precision Oncology 8 (2024): 148.  
13. X. Chen and J. R. Cubillos-Ruiz, “Endoplasmic Reticulum Stress Signals in the Tumour and its Microenvironment,” Nature Reviews Cancer 21 (2021); 7188.  
14. W. Yang, Y. Bai, Y. Xiong, et al., “Potentiating the Antitumour Response of CD8+ T Cells by Modulating Cholesterol Metabolism,” Nature 531 (2016): 651–655.  
15. J. E. Stine, H. Guo, X. Sheng, et al., “The HMG-CoA Reductase Inhibitor, Simvastatin, Exhibits Anti-Metastatic and Anti-Tumorigenic Effects in Ovarian Cancer." Oncotarget 7 (2016): 946960.  
16. R. Zenobi, “Single-Cell Metabolomics: Analytical and Biological Perspectives,” Science 342 (2013): 1201–1210.  
17. S. Yue and J. X. Cheng, “Deciphering Single Cell Metabolism by Coherent Raman Scattering Microscopy,” Current Opinion in Chemical Biology 33 (2016): 46–57.  
18. H. Na, P. Zhang, Y. Chen, et al., “Identification of Lipid Droplet Structure-Like/Resident Proteins in Caenorhabditis Elegans,” Biochimica et Biophysica Acta (BBA) - Molecular Cell Research 1853 (2015): 2481–2491.  
19. J. Xu, T. Yu, C. E. Zois, et al., “Unveiling Cancer Metabolism Through Spontaneous and Coherent Raman Spectroscopy and Stable Isotope Probing,” Cancers 13 (2021): 1718.  
20. S. Cui, S. Zhang, and S. Yue, “Raman Spectroscopy and Imaging for Cancer Diagnosis,” Journal of Healthcare Engineering 2018 (2018): 8619342.  
21. G. Pezzotti, “Raman Spectroscopy in Cell Biology and Microbiology,” Journal of Raman Spectroscopy 52 (2021): 2348–2443.  
22. J. X. Cheng and X. S. Xie, “Vibrational Spectroscopic Imaging of Living Systems: An Emerging Platform for Biology and Medicine,” Science 350 (2015): aaa8870.  
23. D. Polli, V. Kumar, C. M. Valensise, M. Marangoni, and G. Cerullo, “Broadband Coherent Raman Scattering Microscopy,” Laser & Photonics Reviews 12 (2018): 1800020.  
24. C. V. P. Dessai, A. Pliss, A. N. Kuzmin, E. P. Furlani, and P. N. Prasad “Coherent Raman Spectroscopic Imaging to Characterize Microglia Activation Pathway,” Journal of Biophotonics 12 (2019): 201800133.  
25. D. Zhang, P. Wang, M. N. Slipchenko, and J. X. Cheng, “Fast Vibrational Imaging of Single Cells and Tissues by Stimulated Raman Scattering Microscopy,” Accounts of Chemical Research 47 (2014): 2282– 2290.  
26. F. Hu, L. Shi, and W. Min, “Biological Imaging of Chemical Bonds by Stimulated Raman Scattering Microscopy,” Nature Methods 16 (2019): 830–842.  
27. Y. Tan, H. Lin, and J. X. Cheng, “Profiling Single Cancer Cell Metabolism via High-Content SRS Imaging With Chemical Sparsity,” Science Advances 9 (2023): adg6061.  
28. H. Lin, S. Seitz, Y. Tan, et al., “Label-Free Nanoscopy of Cell Metabolism by Ultrasensitive Reweighted Visible Stimulated Raman Scattering,” Nature Methods 22 (2025): 1040–1050.  
29. H. Liang, R. Shi, H. Wang, and Y. Zhou, “Advances in the Application of Raman Spectroscopy in Haematological Tumours,” Frontiers in Bioengineering and Biotechnology 10 (2023): 1103785.  
30. L. Xiao, S. Shelake, M. Ozerova, K. M. Balss, K. Amin, and A. Tsai, “Spectral Markers for T Cell Death and Apoptosis—A Pilot Study on Cell Therapy Drug Product Characterization Using Raman Spectroscopy,” Journal of Pharmaceutical Sciences 110 (2021): 3786–3793.  
31. H. Lin, H. J. Lee, N. Tague, et al., “Microsecond Fingerprint Stimulated Raman Spectroscopic Imaging by Ultrafast Tuning and Spatial-Spectral Learning,” Nature Communications 12 (2021): 3052.  
32. H. Ni, C. P. Dessai, H. Lin, et al., “High-Content Stimulated Raman Histology of Human Breast Cancer,” Theranostics 14 (2024): 1361–1370.  
33. K. C. Huang, J. Li, C. Zhang, Y. Tan, and J. X. Cheng, “Multiplex Stimulated Raman Scattering Imaging Cytometry Reveals Lipid-Rich Protrusions in Cancer Cells under Stress Condition,” iScience 23 (2020): 100953.  
34. M. Yoshihara, Y. Yamakita, H. Kajiyama, et al., “Filopodia Play an Important Role in the Trans-Mesothelial Migration of Ovarian Cancer Cells,” Experimental Cell Research 392 (2020): 112011.  
35. G. Jacquemet, H. Hamidi, and J. Ivaska, “Filopodia in Cell Adhesion, 3D Migration and Cancer Cell Invasion,” Current Opinion in Cell Biology 36 (2015): 23–31.  
36. H. Wang, H. S. Wang, B. H. Zhou, et al., “Epithelial–Mesenchymal Transition (EMT) Induced by TNF-α Requires AKT/GSK-3β-Mediated Stabilization of Snail in Colorectal Cancer,” PLoS ONE 8 (2013): 56664.  
37. J. Li, X. Qu, J. Tian, J. T. Zhang, and J. X. Cheng, “Cholesterol Esterification Inhibition and Gemcitabine Synergistically Suppress Pancreatic Ductal Adenocarcinoma Proliferation,” PLoS ONE 13 (2018): 0193318.  
38. B. Huang, B. liang Song, and C. Xu, “Cholesterol Metabolism in Cancer: Mechanisms and Therapeutic Opportunities,” Nature Metabolism 2 (2020): 132–141.  
39. C. H. Jakobsen, G. L. Størvold, H. Bremseth, et al., “DHA Induces ER Stress and Growth Arrest in Human Colon Cancer Cells: Associations With Cholesterol and Calcium Homeostasis,” Journal of Lipid Research 49 (2008): 2089–2100.  
40. S. Koizume and Y. Miyagi, “Lipid Droplets: A Key Cellular Organelle Associated With Cancer Cell Survival Under Normoxia and Hypoxia,” International Journal of Molecular Sciences 17 (2016): 1430.  
41. T. C. Walther and R. V. Farese, “Lipid Droplets and Cellular Lipid Metabolism,” Annual Review of Biochemistry 81 (2012): 687–714.  
42. R. V. Farese and T. C. Walther, “Lipid Droplets Finally Get a Little R-E-S-P-E-C-T,” Cell 139 (2009): 855–860.  
43. T. Y. Chang, B. L. Li, C. C. Y. Chang, and Y. Urano, “Acyl-Coenzyme A:Cholesterol Acyltransferases,” American Journal of Physiology-Endocrinology and Metabolism 297 (2009): E1–E9.  
44. A. K. Stobart, S. Stymne, and S. Höglund, “Safflower Microsomes Catalyse Oil Accumulation In Vitro: A Model System,” Planta 169 (1986): 33–37.  
45. H. Yang, A. Galea, V. Sytnyk, and M. Crossley, “Controlling the Size of Lipid Droplets: Lipid and Protein Factors,” Current Opinion in Cell Biology 24 (2012): 509–516.  
46. A. H. Chau, J. T. Motz, J. A. Gardecki, S. Waxman, B. E. Bouma, and G. J. Tearney, “Fingerprint and High-Wavenumber Raman Spectroscopy in a Human-Swine Coronary Xenograft In Vivo,” Journal of Biomedical Optics 13 (2008): 040501.  
47. X. Chen, S. Cui, S. Yan, et al., “Hyperspectral stimulated Raman Scattering Microscopy Facilitates Differentiation of Low-Grade and High Grade Human Prostate Cancer,” Journal of Physics D: Applied Physics 54 (2021): 484001.  
48. J. Li, D. Gu, S. S. Y. Lee, et al., “Abrogating Cholesterol Esterification Suppresses Growth and Metastasis of Pancreatic Cancer,” Oncogene 35 (2016): 6378–6388.  
49. X. Ma, E. Bi, Y. Lu, et al., “Cholesterol Induces CD8+ T Cell Exhaustion in the Tumor Microenvironment." Cell Metabolism 30 (2019): 143- 156.  
50. K. Lei, A. Kurum, M. Kaynak, et al., “Cancer-Cell Stiffening via Cholesterol Depletion Enhances Adoptive T-Cell Immunotherapy,” Nature Biomedical Engineering 5 (2021): 1411–1425.  
51. Y. Kidani and S. J. Bensinger, “Modulating Cholesterol Homeostasis to Build a Better T Cell,” Cell Metabolism 23 (2016): 963–964.  
52. P. Goossens, J. Rodriguez-Vita, A. Etzerodt, et al., “Membrane Cholesterol Efflux Drives Tumor-Associated Macrophage Reprogramming and Tumor Progression,” Cell Metabolism 29 (2019): 1376–1389.  
53. A. B. Chaves-Filho and A. Schulze, "Cholesterol Atlas of Tumor Microenvironment Provides Route to Improved CAR-T Therapy,” Cancer Cell 41 (2023): 1204–1206.  
54. S. Yue, J. Li, S. Y. Lee, et al., “Cholesteryl Ester Accumulation Induced by PTEN Loss and PI3K/AKT Activation Underlies Human Prostate Cancer Aggressiveness,” Cell Metabolism 19 (2014): 393–406.  
55. T. Tatsuguchi, T. Uruno, Y. Sugiura, et al., “Cancer-Derived Cholesterol Sulfate is a Key Mediator to Prevent Tumor Infiltration by Effector T Cells,” International Immunology 34 (2022): 277–289.  
56. G. Llaverías, J. C. Laguna, and M. Alegret, “Pharmacology of the AC AT Inhibitor Avasimibe (CI-1011),” Cardiovascular Drug Reviews 21 (2003): 33–50.  
57. W. W. L. Wong, J. Dimitroulakos, M. D. Minden, and L. Z. Penn, “HMG-CoA Reductase Inhibitors and the Malignant Cell: The Statin  
Family of Drugs as Triggers of Tumor-Specific Apoptosis,” Leukemia 16 (2002): 508–519.  
58. S. Kato, M. F. Liberona, J. Cerda-Infante, et al., “Simvastatin Interferes With Cancer ‘Stem-Cell’ Plasticity Reducing Metastasis in Ovarian Cancer,” Endocrine-Related Cancer 25 (2018): 821–836.  
59. W. Yuan, X. Ren, J. Zhu, et al., “Single-Intraosseous Simvastatin Injection Suppresses Cancers via Activating CD8+ T Cells,” Biomedicine & Pharmacotherapy 155 (2022): 113665.  
60. D. Sun, X. Cui, W. Yang, et al., “Simvastatin Inhibits PD-L1 via ILF3 to Induce Ferroptosis in Gastric Cancer Cells,” Cell death & disease 16 (2025): 208.  
61. K. J. Lee, J. Y. Moon, H. K. Choi, et al., “Immune Regulatory Effects of Simvastatin on Regulatory T Cell-Mediated Tumour Immune Tolerance,” Clinical and Experimental Immunology 161 (2010): 298–305.  
62. L. Zhao, J. Li, Y. Liu, et al., “Cholesterol Esterification Enzyme Inhibition Enhances Antitumor Effects of Human Chimeric Antigen Receptors Modified T Cells,” Journal of Immunotherapy 41 (2018): 45–52.  
63. Q. Su, J. Yao, M. A. Farooq, et al., “Modulating Cholesterol Metabolism via ACAT1 Knockdown Enhances Anti-B-Cell Lymphoma Activities of CD19-Specific Chimeric Antigen Receptor T Cells by Improving the Cell Activation and Proliferation,” Cells 13 (2024): 555.  
64. S. Luanpitpong, M. Janan, J. Poohadsuan, et al., “A High-Throughput, Three-Dimensional Multiple Myeloma Model Recapitulating Tumor-Stroma Interactions for CAR-Immune Cell-Mediated Cytotoxicity Assay,” ImmunoTargets and Therapy 14 (2025): 321–338.  
65. T. E. Schnalzger, M. H. de Groot, C. Zhang, et al., “3D Model for CAR -Mediated Cytotoxicity Using Patient-Derived Colorectal Cancer Organoids,” The EMBO Journal 38 (2019): 100928.  
66. A. Alnefaie, S. Albogami, Y. Asiri, et al., “Chimeric Antigen Receptor T-Cells: An Overview of Concepts, Applications, Limitations, and Proposed Solutions,” Frontiers in Bioengineering and Biotechnology 10 (2022): 797440.  
67. M. Yi, T. Li, M. Niu, et al., “Targeting Cytokine and Chemokine Signaling Pathways for Cancer Therapy,” Signal Transduction and Targeted Therapy 9 (2024): 176.  
68. M. Wang, C. Zhang, Y. Song, et al., “Mechanism of Immune Evasion in Breast Cancer,” OncoTargets and Therapy 10 (2017): 1561–1573.  
69. G. C. Sim and L. Radvanyi, “The IL-2 Cytokine Family in Cancer Immunotherapy,” Cytokine & Growth Factor Reviews 25 (2014): 377–390.  
70. G. Zhao, Y. Tan, H. Cardenas, et al., “Ovarian Cancer Cell Fate Regulation by the Dynamics Between Saturated and Unsaturated Fatty Acids,” Proceedings of the National Academy of Sciences 119 (2022): e2203480119.  
71. Z. Chen, Y. Gong, F. Chen, et al., “Orchestrated Desaturation Reprogramming From Stearoyl-CoA Desaturase to Fatty Acid Desaturase 2 in Cancer Epithelial-Mesenchymal Transition and Metastasis,” Cancer Communications 45 (2024): 245–280.  
72. D. Wang and R. N. Dubois, “Eicosanoids and Cancer,” Nature Reviews Cancer 10 (2010): 181–193.  
73. W. Jiang, W. L. Jin, and A. M. Xu, “Cholesterol Metabolism in Tumor Microenvironment: Cancer Hallmarks and Therapeutic Opportunities,” International Journal of Biological Sciences 20 (2024): 2044–2071.  
74. B. C. Farmer, A. E. Walsh, J. C. Kluemper, and L. A. Johnson, “Lipid Droplets in Neurodegenerative Disorders,” Frontiers in Neuroscience 14 (2020): 742.  
75. Q. Xia, J. Yin, Z. Guo, and J. X. Cheng, “Mid-Infrared Photothermal Microscopy: Principle, Instrumentation, and Applications,” The Journal of Physical Chemistry B 126 (2022): 8597–8613.  
76. M. W. Sutherland and B. A. Learmonth. "The Tetrazolium Dyes MTS and XTT Provide New Quantitative Assays for Superoxide and Superoxide Dismutase,” Free Radical Research 27 (1997): 283–289.  
77. C. Marar, Y. Jiang, Y. Li, et al., “Wireless Neuromodulation at Submillimeter Precision via a Microwave Split-Ring Resonator,” Science Advances 10 (2024): ado5560.  
78. R. Tibshirani, “Regression Shrinkage and Selection Via the Lasso,” Journal of the Royal Statistical Society Series B: Statistical Methodology 58 (1996): 267–288.  
79. G. Ding, C. Liu, J. Yin, et al., “Self-Supervised Elimination of Non-Independent Noise in Hyperspectral Imaging,” Newton 1 (2024): 100195.

## Supporting Information

Additional supporting information can be found online in the Supporting Information section.

Supporting file: advs74403-sup-0001-SuppMat.docx.