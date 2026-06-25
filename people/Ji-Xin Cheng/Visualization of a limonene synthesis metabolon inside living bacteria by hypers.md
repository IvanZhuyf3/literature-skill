# Visualization of a Limonene Synthesis Metabolon Inside Living Bacteria by Hyperspectral SRS Microscopy

Jing Zhang, Jonghyeon Shin, Nathan Tague, Haonan Lin, Meng Zhang, Xiaowei Ge, Wilson Wong, Mary J. Dunlop,\* and Ji-Xin Cheng\*

Monitoring biosynthesis activity at single-cell level is key to metabolic engineering but is still difficult to achieve in a label-free manner. Using hyperspectral stimulated Raman scattering imaging in the 670–900 cm−1 region, localized limonene synthesis are visualized inside engineered Escherichia coli. The colocalization of limonene and GFP-fused limonene synthase is confirmed by co-registered stimulated Raman scattering and two-photon fluorescence images. The finding suggests a limonene synthesis metabolon with a polar distribution inside the cells. This finding expands the knowledge of de novo limonene biosynthesis in engineered bacteria and highlights the potential of SRS chemical imaging in metabolic engineering research.

## 1. Introduction

A metabolon is a supramolecular complex of sequentia metabolic enzymes.[1,2] Metabolons provide multiple advantages for enhanced product flux, and protection from toxic metabolic intermediates.[3,4] Moreover, a few examples of metabolons such as a glucosome and purinosome have been reported.[5-7] Advanced imaging techniques such as gas cluster ion beam

J. Zhang, J. Shin, N. Tague, H. Lin, W. Wong, M. J. Dunlop, J.-X. Cheng

Department of Biomedical Engineering

Boston University

Boston, MA 02215, USA

E-mail: mjdunlop@bu.edu; jxcheng@bu.edu

J. Zhang, H. Lin, M. Zhang, X. Ge, J.-X. Cheng

Photonics Center

Boston University

Boston, MA 02215, USA

N. Tague, W. Wong, M. J. Dunlop

Biological Design Center

Boston University

Boston, MA 02215, USA

M. Zhang, X. Ge, J.-X. Cheng

Department of Electrical and Computer Engineering

Boston University

Boston, MA 02215, USA

![](images/d8cdbdb06affb7b15032d9ffc343c05f767dccd85f74788ead0e135d6b8dc365.jpg)

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/advs.202203887

© 2022 The Authors. Advanced Science published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

DOI: 10.1002/advs.202203887 secondary ion mass Spectrometry (GCIB-SIMS), super-resolution fluorescence microscopy, and fluorescence resonance energy transfer (FRET) microscopy have been employed to image metabolons, e.g. purinosomes in eukaryotic cells.[8-10] However, the investigation of metabolons in a single bacterial cell remains extremely challenging, especially when the metabolites involved are small molecules for which fluorescent reporters are not available.

Limonene is a type of cyclic monoterpenes that widely exist in plants. Both limonene and its derivatives have diverse applications in the food industry and pharmaceuticals.[11–13] Despite increasing demand, the supply of limonene, mainly

produced from food processing, is unstable.[14] Empowered by the latest advancements in genetic engineering and metabolic engineering, microbial fermentation facilitating the conversion of limonene from low-value materials like glucose has been a promising approach for the bulk and stable production of limonene.[15,16] However, cell-to-cell variation of biochemical synthesis hinders the maximum yield and the lack of detailed singlecell level characterization is one of the bottlenecks to solve the problem. Recently, spontaneous Raman has been applied to study metabolite production in engineered fungi or bacteria.[17,18] Due to the small Raman cross sections of biological samples, the speed of spontaneous Raman is limited, and it usually requires tens of milliseconds to seconds dwell time. This long acquisition time hinders the further utility of spontaneous Raman in biological applications.

Employing a two-laser system (a pump beam and a Stokes beam), stimulated Raman scattering (SRS) offers accelerated imaging speed compared to spontaneous Raman.[19–21] The rapid identification of Raman signals offered by SRS paves the way for single-cell imaging with live-cell compatibility, which is beyond the reach of mass spectrometry.[22–24] Compared to fluorescence imaging, SRS has the potential to detect molecules that do not have commercially available fluorescent probes. Here, we report direct visualization of localized limonene synthesis inside single engineered Escherichia coli (E. coli) by hyperspectral stimulated Raman scattering (hSRS). Compared to previous study of limonene biosynthesis detection by single-color SRS,[25,26] hSRS allows simultaneous quantification of multiple chemicals inside one specimen by recording a Raman spectrum at each pixel. Intracellular compositions of various biological specimens have been studied using hSRS, ranging from tissues,[27,28] to cancerous cells,[29,30] to bacteria.[31,32] Many of these applications employ the C–H stretching region (2800–3100 cm−1) for its strong SRS signal or the C–D stretching region (2070– $2 3 0 0 \mathrm { c m } ^ { - 1 } )$ for selective imaging of Raman tags. However, both C–H region and C–D band in the silent region lack specificity in detecting small-molecule synthesis because of Raman signal contributions from other intracellular biomacromolecules. In comparison, the fingerprint region $( 6 0 0 { - } 1 8 0 0 ~ \mathrm { c m ^ { - 1 } } )$ takes advantage of the rich spectral features of limonene,[33] making hSRS in the fingerprint region an ideal tool to study limonene biosynthesis at the single-cell level.

![](images/e464474569bd8d5ee4e7697c0bf8d2480c86cb4c5a101a6f71a3d570deac292f.jpg)

<details>
<summary>chemical</summary>

Chemical reaction pathway showing the synthesis of liponene from acetyl-CoA and leucine under various reagents including HMGS, HMGR, GPPS, and idi.
</details>

![](images/f20f003f61a49fca42e394a8ae355c4429143775b9d69d134438da0136b35ae7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    subgraph Left_Phasule
  A["P1acUV5"] --> B["atoB"]
  B --> C["HMGSHMGR MK"]
  C --> D["PMK"]
  D --> E["PMD"]
  E --> F["idi"]
  F --> G["GPPS"]
  G --> H["LS"]
  H --> I["colE1"]
  I --> J["GPPS"]
  J --> K["LS"]
  K --> L["colE1"]
  L --> M["GPPS"]
  M --> N["LacI"]
  N --> O["CmR"]
  O --> P["p15A"]
  P --> Q["LacI"]
  Q --> R["AmpR"]
    end
    subgraph Right_Phasule
  S["P2A15A"] --> T["Pconstitutive"]
  T --> U["LacI"]
  U --> V["CmR"]
  V --> W["p15A"]
  W --> X["LacI"]
  X --> Y["AmpR"]
  Y --> Z["LacI"]
  Z --> AA["AmpR"]
    end
```
</details>

![](images/5b939bdc072fb3a34b95b34011770ca0ebd38e866600509c532e72ac55cc8e2b.jpg)

<details>
<summary>bar chart</summary>

| Condition       | Limonene (mg/L) |
| --------------- | --------------- |
| Wild-type       | 0               |
| IPTG 0.1 mM     | 6               |
| IPTG 0.5 mM     | 23              |
</details>

Figure 1. Limonene-producing E. coli strains and GC-MS measurements. a) Metabolic pathway from Acetyl-CoA to limonene in E. coli. Enzymes and some of the reaction intermediates necessary for the production of limonene are shown. AtoB: acetoacetyl-CoA synthase; HMGS: HMG-CoA synthase; HMGR: MG-CoA reductase; MK: Mevalonate Kinase; PMK: PhosphoMevalonate Kinase; PMD: PhosphoMevalonate Decarboxylase; IPP: isopenteny pyrophosphate; idi: isopentenyl diphosphate isomerase; DMAPP: dimenthylallyl pyrophosphate; GPPS: Geranyl PyroPhosphate Synthase; GPP: geranyl pyrophosphate; LS: limonene synthase. b) Genetic design of limonene pathway for strains with a two-plasmid system. c) GC-MS measurements of microbial production of limonene (BW25113 strain with a two-plasmid system). Error bar: std.

In this study, we harness polygon-scanner-based hSRS to map the de novo synthesized limonene distribution inside Escherichia coli cells. We first verify that limonene is synthesized from engineered E. coli using gas chromatography-mass spectrometry (GC-MS). To investigate subcellular limonene distribution, $\mathrm { L } _ { 1 } \cdot$ regularized least squares fitting was used for hSRS image stack in $6 7 0 { - } 9 0 0 \mathrm { c m } ^ { - 1 }$ region, enabling selective mapping of limonene and proteins inside individual E. coli cells. The chemical content and spatial distribution of the limonene-rich aggregates were then characterized by single-cell and single-aggregate segmentation. In addition, two-photon fluorescence (TPF) imaging of GFP-fused limonene synthase supports the colocalization of limonene with limonene synthase. Together, our data support the possible existence of metabolons in engineered E. coli. The result also highlights the potential of hSRS imaging in metabolic engineering through multiplexed biomolecular analysis at the sub-cellular level.

## 2. Results

## 2.1. Limonene-Producing E. Coli Strains and Mass Spectrometry Measurements

We harnessed the heterogeneous mevalonate pathway to produce limonene in E. coli (Figure 1a).[34] Isoprenoid precursors, isopentenyl pyrophosphate (IPP), and dimenthylallyl pyrophosphate (DMAPP), are products of the mevalonate pathway derived from acetyl-CoA, one of the key node molecules in E. coli central metabolism. A geranyl pyrophosphate synthase (GPPS) converts IPP and DMAPP to geranyl pyrophosphate (GPP) that is a universal precursor of terpenes and a limonene synthase (LS) specifically converts GPP to limonene. For easy genetic modification, we distributed necessary enzymes in two plasmids: one plasmid encodes the mevalonate pathway and the other encodes GPPS and LS that are translationally fused (denoted as a twoplasmid system, Figure 1b).[34] E. coli strain BW25113 was used as the host. Limonene production is induced by a small molecule isopropyl ??-d-1-thiogalactopyranoside (IPTG). IPTG is a molecular reagent that induces expression where the gene is under the control of the lac repressor. We then used gas chromatography– mass spectrometry to confirm the successful limonene synthesis in these engineered strains (Figure 1c).

## 2.2. Hyperspectral SRS Imaging Unveils Chemical Aggregates Inside Limonene-Producing E. Coli

To visualize limonene biosynthesis at the single-cell level, we utilized both Raman spectroscopy and SRS microscopy. Raman spectroscopy was used to determine the vibrational signatures of limonene and its precursors (Figure 2a,b). Pure limonene, glycerol trioleate (GT), and bovine serum albumin (BSA) were measured using a LabRAM HR800 confocal Raman microscopy. Spectra of geraniol, prenol, and isoprenol from[35] were used to present the spectra of geranyl diphosphate (GPP), dimethylallyl diphosphate (DMAPP), and isopentenyl diphosphate (IPP), which are the intermediates in the limonene synthesis pathway. Limonene exhibits strong Raman signals in the high wavenumber C–H stretching region (2800 to $3 1 0 0 ~ \mathrm { c m ^ { - 1 } } )$ ), but this region lacks limonene specificity as C–H bonds are the most abundant functional groups in the cell. In the fingerprint region (600 to 1800 cm−1), limonene shows several signature peaks. We chose the peak at $7 6 0 ~ \mathrm { c m ^ { - 1 } }$ considering the high intensity of limonene and the relatively low background contributed by other biomolecules in the $6 7 0$ to 900 $\mathrm { c m } ^ { - 1 }$ region. This unique limonene peak stems from a combination of ring and $\mathrm { C H } _ { 2 }$ vibra-

(a)  
![](images/98a2458091e1ed4101a5ebc52ee8e90a798b44702f376d81b68a6381ea0bae09.jpg)

<details>
<summary>line chart</summary>

| Compound   | Raman shift (cm⁻¹) |
| ---------- | ------------------ |
| Limonene   | ~750               |
| Geraniol   | ~750               |
| Prenol     | ~750               |
| Isoprenol  | ~750               |
| GT         | ~750               |
| BSA        | ~750               |
</details>

(b)  
![](images/dc400c399ddc9eb344e74e7221cca227f4cb3480cf77d018bbdd78fc24a56603.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Series 1 | Series 2 | Series 3 | Series 4 | Series 5 | Series 6 |
| ------------------ | -------- | -------- | -------- | -------- | -------- | -------- |
| 2800               | ~0.8     | ~0.7     | ~0.6     | ~0.5     | ~0.4     | ~0.3     |
| 2900               | ~1.0     | ~0.9     | ~0.8     | ~0.7     | ~0.6     | ~0.5     |
| 3000               | ~0.9     | ~0.8     | ~0.7     | ~0.6     | ~0.5     | ~0.4     |
</details>

(c)  
![](images/14645e7b5700c5f1bf86d56bccb292035d876dba471da7dd34feed2098adbda4.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of wild-type cells with scale bar indicating 5 μm (no text or symbols beyond labels)
</details>

IPTG 0.1 mM  
![](images/28922edc09fa671ccc43d4812c12609d380dcfef99e44f0394d1e8a383b067ad.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright spots on a dark background, with three white arrowheads highlighting specific regions (no text or symbols present)
</details>

(f)  
![](images/b9697591e070edd80dd883f661de3e5fcf0a9392d05c1233f3b49d401437fbd5.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing wild-type cells with blue nuclei and green cytoplasmic markers (no text or symbols)
</details>

IPTG 0.1 mM  
![](images/cb68949ab7edf504dae7a58145fab2e97f0ce508df5851544875ed51267bd4e9.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing scattered green and blue cellular structures with white arrow annotations (no text or symbols)
</details>

![](images/f9bf83229f700feb8ddea77fddf52a45581c97bac3bd5b517828f2ef10817ff2.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 700                | ~0.2             |
| 750                | ~0.8             |
| 800                | ~0.9             |
| 850                | ~0.6             |
| 900                | ~0.1             |
</details>

![](images/b38c854450a3d95005bc238f80365c8feff375b4e266a7cc8567325280bf113b.jpg)

<details>
<summary>scatterplot</summary>

| Group | Intensity (a.u.) |
|-------|------------------|
| Wild-type | ~0.4–1.0 |
| IPTG 0.1 mM rest of the cell | ~0.5–1.0 |
| IPTG 0.1 mM Aggregate | ~0.8–1.0 |
</details>

(g)  
![](images/cec37d7d292e31fc092343316814ea2b4c7b0760c50f576dd9db0843e1d7f22c.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 2900               | ~5E3             |
| 3000               | ~1E4             |
</details>

(h)  
![](images/b96851f62cfdb384beac25a21a2d7fb3d4407a43eb2f2d84e4f315c41eb4945f.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 2900               | 1.0              |
</details>

Wild-typeIPTG 0.1 mM: AggregateIPTG 0.1 mM: rest of the cell BSA

Figure 2. Hyperspectral SRS imaging unveils chemical aggregates inside limonene-producing E. coli. a) Spontaneous Raman spectra of limonene, geraniol, prenol, isoprenol, GT (glycerol trioleate), and BSA (bovine serum albumin) in the fingerprint window $( 6 0 0 - 1 8 0 0 ~ { \mathsf { c m } } ^ { - 1 } )$ . Spectra of geraniol, prenol, and isoprenol represent the spectra of precursors in limonene synthesis pathway (GPP, DMAPP, and IPP). b) Spontaneous Raman spectra of limonene, geraniol, prenol, isoprenol, GT, and BSA in the C–H window. The spectra of GT and BSA were included to show that neither protein nor fatty acids inside the cells have a significant contribution to the $7 6 0 \ c m ^ { - 1 }$ Raman peak. Red arrows denote peaks at Raman shift $7 6 0 c m ^ { - 1 }$ (limonene), $7 7 4 ~ \mathsf { c m } ^ { - 1 }$ (prenol), and $7 6 7 \mathsf { c m } ^ { - 1 }$ (isoprenol). c) Spectrally summed hSRS images of BW25113 strain (fingerprint window). Left: wild-type; Right: limonene-producing strain. White arrows denote the position of the intracellular aggregates. d) Average of the normalized spectra of the wild-type strain, aggregate of limoneneproducing strain, and non-aggregating part of limonene-producing strain. Red arrow marks $7 6 0 ~ \mathsf { c m } ^ { - 1 }$ Raman peak. Shaded error bar: std. e) Scatter plot of the Raman intensity at $7 6 0 ~ \mathsf { c m } ^ { - 1 }$ per region of the normalized spectra in (d). The solid green, blue, and red lines were averaged by 68 cells, 33 cells, 4 aggregates respectively. ${ \mathsf { N S } } ,$ nonsignificant, $P > 0 . 0 5 . * , 1 0 ^ { - 5 } < P < 0 . 0 \dot { 5 }$ (Wilcoxon rank sum test). f) Spectrally summed hSRS images of BW25113 strain (C–H window). Left: wild-type; Right: limonene-producing strain. g) Average of the raw spectra of the wild-type strain, aggregates of limonene-producing strain, and non-aggregating part of limonene-producing strain. Red arrow marks $2 9 3 0 \mathsf { c m } ^ { - 1 }$ Raman peak. h) Average of the normalized spectra of wild-type strain, aggregates of limonene-producing strain, and non-aggregating part of limonene-producing strain. Red arrow marks $2 9 3 0  c m ^ { - \dagger }$ Raman peak. Shaded error bar: std.

tion in limonene.[36] We also measured spectra of GT and BSA to confirm that neither protein nor fatty acids inside the cells dc not have a significant contribution to the $7 6 0 \mathrm { c m ^ { - 1 } }$ Raman peak.

Next, hSRS imaging was utilized to characterize the spatial distribution of limonene inside single engineered E. coli cells. We employed an ultrafast delay-tuning hSRS scheme[22] shown in Figure S1 (Supporting Information). Briefly, polygonscanner-based SRS collects image stacks in $\mathbf { a _ { \lambda } \ ^ { \textit { \textbf { u } } } } \lambda \mathbf { - X - y } ^ { \mathfrak { n } }$ manner and provides an acquisition speed of down to 20 μs per spectrum with a $1 0 ~ \mathrm { c m ^ { - 1 } }$ resolution in the fingerprint region.[22] In this study, each single spectrum in the SRS stack takes 120 μs, which improved the spectral fidelity and eliminated low-frequency noise compared to the conventional motorized-stage-based hSRS scheme. It thus provides great advantages for differentiating limonene from other biomolecules inside cells. Figure S2 (Supporting Information) shows the linearity and sensitivity of limonene detection at the $7 6 0 ~ \mathrm { c m ^ { - 1 } }$ Raman peak. The detection limit is found to be ≈21 mm at a speed of 0.89 sec per frame of 200 × 200 pixels. Compared to the conventional frame-by-frame scheme, the use of the polygon scanner increased the hSRS imaging speed by ≈5 times at the same signal-to-noise ratio (SNR) (Figure S3, Supporting Information).

By hSRS imaging, intracellular aggregates were observed in the $6 7 0 { - } 9 0 0 ~ \mathrm { c m } ^ { - 1 }$ region for the limonene-producing strains, as indicated by arrows in Figure 2c. In contrast, the control strains without the heterologous limonene synthesis pathway did not exhibit obvious intracellular aggregates. Figure 2d shows the fingerprint Raman spectra of the aggregates and the rest of the cell. Specifically, the Raman peak at $7 6 0 \mathrm { \bar { c } m ^ { - 1 } }$ confirms the presence of limonene inside these aggregates. The spectrum of the rest of the cell, lacking the $7 6 0 ~ \mathrm { c m ^ { - 1 } }$ Raman peak, is comparable to the spectrum of the wild-type strain (Wilcoxon rank sum test, Figure 2e). As a comparison, hSRS imaging in the C–H region was also performed. Intracellular aggregates were also observed in the limonene-producing strain but not in the control strain (Figure 2f). As opposed to the fingerprint region, the spectra in the C–H region do not distinguish the aggregate from the rest of the cell, as the C–H region does not have enough specificity for limonene detection (Figure 2g,h). Besides, in the C–H region, the spectra of aggregates resemble the spectrum of BSA but not limonene, indicating the coexistence of proteins with the locally aggregated limonene. Because of the low solubility of limonene and the intermediates in water, these proteins might offer protection to hydrophobic molecules against the hydrophilic environment of the cytoplasm. Further testing of the chemical composition and potential functions of these intracellular aggregates is shown in the following sections.

## 2.3. Pixel-Wise Spectral Unmixing Reveals the Chemical Composition of the Intracellular Aggregates

To extract the limonene distribution map from the hyperspectral stack, we applied the least absolute shrinkage and selection operator (LASSO).[37] The effectiveness of LASSO in unmixing hSRS images in the fingerprint region has been tested on various biological samples.[22] Compared to least squares fitting, LASSO introduces a pixel-wise sparsity constraint. It hypothesizes that each pixel of our hyperspectral image is dominated by sparsity components. This feature makes LASSO ideal for our study because limonene is localized in the intracellular aggregates and the rest of the cell (the non-aggregating part) has the same spectral profile as the control strain (Figure 2d). Therefore, using the reference spectra for pure limonene, wild-type strain, and background (of each hSRS image stack), chemical maps of three channels can be generated, denoted as limonene, cell body, and background.

By LASSO analysis of the fingerprint hSRS data (Figure 3a), we generated concentration maps of limonene (Figure 3b). Locally concentrated limonene was found in engineered strains but not in the wild-type. The cell body channel was similar across all samples (Figure 3c). By single-cell and single-aggregate segmentation (Figure S4 (Supporting Information), details in the Exper imental Section), segmentation maps of two types of cell regions were generated: aggregates and the rest of the cell. By averaging the limonene intensity of both regions, the limonene amount of each aggregate and the rest of the cell is plotted (Figure 3d). This result indicates the limonene intensity of aggregate depends on IPTG concentration, which is qualitatively correlated to GC-MS measurements (Figure 1c). Importantly, SRS imaging and LASSO analysis quantitatively show that the produced limonene is locally concentrated and not spread over the whole cell.

![](images/00d34c2016e76817a28ed9ad699b5f9a7345bfbad1137ca5f9ecf2c023daf1bc.jpg)  
Figure 3. Chemical composition analysis of limonene-producing E. coli strains, a) Spectrally summed hSRS images $( 6 7 0 - 9 0 0 ~ \mathrm { { \dot { c } m } ^ { - 1 } ) }$ Left: wild type; middle: Limonene-producing strain with 0.1 mm IPTG; right: Limonene-producing strain with 0.5 mM IPTG. b) Chemical map of limonene. Localized limonene distribution is observed in limoneneproducing strain. Cyan lines: contour of each single cell. White lines: contour of each single aggregate. c) Chemical map of cell body. d) Scatter plot of limonene intensity in aggregates and rest of the cell. Each dot represents the averaged limonene intensity in a single aggregate.

To verify that the SRS-mapped limonene indeed originates from de novo synthesis, we tested E. coli strains with incomplete synthesis pathways in addition to the wild-type strain and the strain with the complete limonene synthesis pathway. Specifically, we tested three incomplete pathways: ∆GPPS without GPPS but having all other enzymes, ∆LS without LS but having all other enzymes, and GPPS-LS only having GPPS and LS but none of the upstream genes in the mevalonate pathway. Based on hSRS images in the $6 7 0 { - } 9 0 0 ~ \mathrm { c m ^ { - 1 } }$ spectral region (Figure 4a), the concentration map of limonene was produced via LASSO analysis (Figure 4b). A high abundance of limonene was only ob served in the strain with a full limonene synthesis pathway, in the form of aggregates. By applying single-aggregate segmentation to SRS images (C–H region, Figure 4c) of the same specimens, limonene-channel intensities in aggregate and the rest of the cell are plotted in Figure 4d. Using a threshold sweeping method (Figure S5, Supporting Information), 1.1 was set as the limonene intensity threshold (red dashed line in Figure 4d) to distinguish the limonene-rich aggregates. Using this threshold, the percentage of cells with limonene-rich aggregates is 16.9% in the strain with a complete pathway. Further tests with a different construct design are shown in the following section.

![](images/b71fb7f61f839af08e4b546b917a7df76c8d595443f90c858e7dbe14ae1b3545.jpg)  
Figure 4. Characterization of limonene distribution in E. coli with complete or incomplete limonene synthesis pathways. The genetic design of each strain is shown in the top row. a) Spectrally summed hSRS images in the fingerprint region. Aggregates are observed in limonene-producing E. coli strains. b) Chemical maps of limonene. Localized limonene distribution is observed in limonene-producing strain. Cyan lines: contour of each single cell. White lines: contour of each single aggregate. c) Spectrally summed SRS images at C–H region. d) Scatter plot of limonene intensity in aggregates and rest of the cell. Red dashed line denoted the threshold of limonene-rich aggregates.

## 2.4. Localized Limonene Synthesis is Confirmed in One-Plasmid Limonene-Producing Strains

To confirm the evidence of localized limonene aggregate formation, engineered strains with a one-plasmid version of the limonene production pathway were tested as a different construct design (denoted as one-plasmid system, Figure 5a). As production is impacted by the strain background, we tested E. coli strain DH1 in addition to BW25113. These one-plasmid strains show higher limonene production in GC-MS measurements than the two-plasmid design in BW25113 (Figure S6a,b, Supporting Information). To further demonstrate the in situ live-cell imaging compatibility of our imaging system, we directly grew the cells on a thin layer of agarose gel pads after IPTG induction (method). With growth medium and air exchange provided by the agarose pad,[38] colonies composed of a single layer of cells form on top of the agarose pad. After culturing for 24 h, the cells growing on the agarose pad were directly imaged using SRS. Using this protocol, we tested the E. coli DH1 strain with one-plasmid, and we were also able to observe intracellular aggregates in both the C–H and the $6 7 0 { - } 9 0 0 ~ \mathrm { c m ^ { - 1 } }$ region (Figure 5b,c). Limonene concentration maps were produced using LASSO analysis (Figure 5d), showing that limonene is localized and enriched in these aggregates. By segmenting these bright spots from the rest of the cell, fingerprint spectra of the aggregates were extracted and exhibited a distinct Raman peak at 760 cm−1 unique to limonene (Figure 5e). Similar results were obtained with another host strain (Figure S6c–f, Supporting Information).

HSRS imaging further allowed us to study the intracellular lo cation of these aggregates as well as cell-to-cell variation. By extracting the central line along the major axis of each aggregatecontaining cell, the position of the aggregate was determined as the pixel with the maximal intensity along the central line (Figure 5f). The scatter plot of the relative location of the aggregate (defined as d/L) is shown in Figure 5g, and 48.5% of aggregates resided between 70% to 90% of the cell length for DH1 strains. We also found that only 18.9% of the cells contain aggregates (Figure 5h). Similar results were observed in the BW25113 strain (Figure S6g,h, Supporting Information). Cell-to-cell variation in limonene biosynthesis was also quantified using the average and total limonene content per aggregate (Figure S7, Supporting In formation). Interestingly, a larger aggregate tends to be accompanied by higher average limonene content (Figure S7a, Supporting Information). Moreover, the scatter plot of aggregate size versus average limonene intensity was bounded by a constant upper threshold and an asymptotic lower threshold. In addition, by comparing the spectra of these aggregates and limonene solution in dodecane, the local concentration of limonene was estimated to be around tens to one hundred mm (Figure S2, Supporting Information). Further evidence revealing the biosynthetic function of these proteins is shown in the next section.

(a)  
![](images/3715b1ee8928c8108279ac10743f6df70f40827ce8f028c1b9af2d23bc020ae9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["atoB"] --> B["HMGS"]
  B --> C["HMGR"]
  C --> D["MK"]
  D --> E["PMK"]
  E --> F["PMD"]
  F --> G["idi"]
  H["P_IacUV5"] --> I["P_trc"]
  J["P_constitutive"] --> K["LacI"]
  K --> L["P_constitutive"]
  L --> M["CmR"]
  M --> N["p15A"]
  N --> O["P_trc"]
  O --> P["GPPS"]
  P --> Q["LS"]
```
</details>

(b)  
![](images/50777b1cd28fc273cf2b4d8bef4c6389925f1f22d4494ea20c316342e1635063.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image of a cell with green and blue staining, scale bar 5 μm (no text or symbols)
</details>

(c)

![](images/aa70015809f519bce3987a03a0bd499cd0da0722df3d4215a083f6f5799b94cb.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological or material sample with green fluorescent spots, labeled '670-900 cm⁻¹' (no other text or symbols)
</details>

(d)

![](images/af110a3c67c434af6d4f83a7958cad12a4e634d41e5ca3ef5b8bd5699d0c0fc3.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of Limonene cells with green cytoskeleton and red punctate signals (no text or symbols)
</details>

(e)

![](images/b2edd4499ff81ff01af771e833d045d7bd0c231f2190da8cf221805f7bf0a6df.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Aggregate Intensity (a.u.) | Rest of the cell Intensity (a.u.) |
| ------------------ | -------------------------- | --------------------------------- |
| 700                | ~0.5                       | ~0.3                              |
| 800                | ~1.0                       | ~0.9                              |
| 900                | ~0.5                       | ~0.3                              |
</details>

(f)  
![](images/a9393484102d67f38f32dacfea6165938ba5fd6af72ec7fbb4310b5ee68a86f6.jpg)

<details>
<summary>text_image</summary>

d
L
Aggregate
Aggregate centroid
Major axis of the cell. Length L
Distance between o and
furthest cell pole
</details>

(g)  
![](images/b93b9008d74114343b1793a130623fa686f24ef94ba7bc2c8e1c735c0d35e348.jpg)

<details>
<summary>scatterplot</summary>

| DH1 | d/L |
| --- | --- |
| (Data points not extractable as discrete values; visual scatter around center) | 0.8, 0.6, 0.4, 0.2, 0.0 |
</details>

(h)  
![](images/6bd14a867808c22d209bd3275115432a164f4d358d5950a7a36ebc2d03a2c7df.jpg)

<details>
<summary>bar chart</summary>

| #aggr per cell | #cell |
|---|---|
| 0 | 1000 |
| 1 | 150 |
| 2 | 10 |
| 3 | 5 |
</details>

Figure 5. Characterization of limonene production in one-plasmid limonene-producing E. coli. a) Genetic design for strains with one-plasmid system. b,c) Spectrally summed hSRS images of DH1 one-plasmid strain. d) Chemical maps of limonene channel of the same field of view in (b). Cyan lines: contour of each single cell. White lines: contour of each single aggregate. e) Averaged spectra of aggregates and rest of the cell (670–900 cm−1). Shaded error bar: std. f) Diagram of a cell with an intracellular aggregate. g) Violin plot with values of d/L for DH1 one-plasmid strain. h) Histogram of aggregate counts per cell for DH1 one-plasmid strain.

## 2.5. Intracellular Limonene is Co-Localized with Limonene Synthase

To further validate our observation, simultaneous imaging of both limonene and LS, the final enzyme in the pathway that synthesizes it, was carried out. For this purpose, green fluorescence protein (GFP) was translationally fused to LS. Notably, limonene was observed in the strain with GFP-LS fusion (Figure 6a,b). Co-registered images of SRS and two-photon fluorescence of both BW25113 with two-plasmid system and DH1 with one-plasmid system are shown in Figure 6c,d and Figure 6f,g, respectively. Limonene maps generated from SRS images are overlaid with the contour of the aggregates in the fluorescence channel, exhibiting the colocalization of limonene with GFP-fused LS (Figure 6e,h). Co-occurrence between limonene and limonene synthase was quantified by Mander’s colocalization coefficient (MCC).[39] MCC is defined as the summed limonene intensity of the colocalized pixels over the summed limonene intensity of all pixels (detailed definition in the Experimental Section). Higher MCC values indicate a higher colocalization level. BW25113 with two-plasmid system (Figure 6e) has an MCC of 0.79. and DH1 with one-plasmid system (Figure 6h) has an MCC of 0.71. This quantification confirms that these aggregates encompass both enzyme and limonene, with the potential function of limonene synthesis and storage. Together, our observation of colocalization of limonene and its synthesis enzyme verifies the formation of limonene synthesis metabolon inside the engineered E. coli strains.

![](images/0b5d1b76d7bc9f3eaada4262fac11cdb6d59993da836e75be41a4c8a8c75d2a0.jpg)  
Figure 6. SRS and two-photon fluorescence (TPF) imaging unveil co-localization of limonene and limonene synthase. a) GC-MS measurement of microbial production of limonene in BW25113 two-plasmid strain. Error bar: std. b) GC-MS measurement of microbial production of limonene in DH1 one-plasmid strain. Error bar: std. c) Spectrally summed hSRS images of BW25113 two-plasmid strain (670–900 cm−1 region). d) Two-photon fluorescence image of the same FOV in (a). e) Limonene map of the same FOV in (a,b). White lines: contour of each single cell. Green lines: contour of each single aggregate by two-photon fluorescence image. f–h) The same order as (a–c). DH1 one-plasmid strain.

## 3. Discussion

Limonene is a high-value chemical with various applications in the industry. A thorough understanding of the limonene biosyn thesis process in the host microorganism is desired to guide metabolic engineering and potentially enhance the limonene yield. Our study here revealed the formation of limonene-rich aggregates in engineered E. coli strains with a limonene synthesis pathway. Quantification of the chemical content of these aggregates was achieved by spectral unmixing of hSRS images of spectral region $6 7 0 { - } 9 0 0 ~ \mathrm { c m ^ { - 1 } }$ . Furthermore, taking advantage of simultaneous hSRS and TPF imaging, colocalization of limonene and limonene synthase was observed in the engineered E. coli. Two biological systems (one-plasmid DH1 strain and twoplasmid BW25113 strain) were tested and both exhibited aggregates in variants with a full limonene pathway. These data offer direct evidence of metabolite channeling and metabolon formation in these engineered strains.

Intracellular organization achieved through compartmentalization is key to cell metabolism. Consisting of sequential enzymes and metabolites, metabolon offers intracellular spatial organization in both eukaryotic[40,41] and prokaryotic cells,[42] bringing multiple advantages in terms of biosynthesis efficiency, cell growth, and survival.[1,43,44] Both natural and engineered systems could take advantage of cellular localization.[45,46] Benefiting from the multimodal capabilities of our imaging system, this study suggests that these intracellular aggregates are limonene synthesis metabolons. First, limonene was shown enriched inside aggregates (Figures 2–5). In the DH1 one-plasmid strain, limonene concentration of aggregates is around tens to one hundred mm, which is one to two order magnitude higher than the limonene concentration measured by GC-MS (Figure 5e; Figure S2a, Supporting Information). Moreover, larger aggregates were accompanied by higher limonene intensities, indicating the continuous limonene deposition in these regions (Figure S7a, Supporting Information). Second, proteins were found existing inside the limonene-rich aggregates by comparing the C–H stretching spectra of aggregates with a standard protein sample BSA (Figure 2g,h). Considering the hydrophobicity of limonene and its precursors, these proteins may offer protection of these metabolites from the hydrophilic environment.[5] Another advantage of these coexisting proteins is preventing the diffusion of reactive or potentially toxic intermediates, which potentially increases the reaction efficiency and reduces the metabolic cross talk.[47] Last, the enrichment of GFP-fused limonene synthase inside these aggregates suggests active limonene synthesis at these spots (Figure 6). This provides substantial evidence of the synthetic function of the proteins coexisting with limonene. Collectively, these data confirmed both the chemical composition and synthetic function of these intracellular aggregates, documenting a new case of metabolon formation in limonene-producing E. coli.

HSRS imaging also offers an interesting insight into the cell to-cell variation of these limonene-producing cells. For all the strains with the full limonene synthesis pathway in this study, heterogeneity in terms of intracellular localization and limonene content were observed. Most of the cells contain zero or one aggregate, suggesting the sparsity of the high-producers in the whole population (Figures 5h; Figure S6h, Supporting Information). The histogram of average limonene content per aggregate showed about ten times variation (Figure S7b, Supporting Information) within an isogenic population for both BW25113 and DH1 one-plasmid strains. We are also able to observe the spatial bias where aggregates were formed. Asymmetric cell partitioning might be one possible reason for the observed single cell heterogeneity and the pole-biased accumulation in these limonene-producing E. coli (Figure 5f,g; Figure S6g, Supporting Information).[48,49]

We would also note a few limitations of our method in characterizing the proposed limonene synthesis metabolon. First, we assumed that at each single pixel, the chemical composition is sparse. By using three standard reference spectra: pure limonene, the wild-type strain, and the background (of each hSRS image stack), the potential Raman signal contribution from the precursors was forced to go to the cell body channel. To discriminate limonene and three precursors (IPP, DMAPP, and GPP), a broadband coherent Raman imaging system could be applied.[50,51] By collecting a wider Raman spectral window, more metabolites could be quantified simultaneously, providing direct evidence of metabolite channeling.[52] Second, limited by the limonene detection sensitivity (≈21 mm) of our hSRS imaging system, limonene distribution in the non-aggregating area of the cell was not ruled out. Although most limonene is expected to exist in an aggregate form because of its low solubility in a hydrophilic environment, limonene efflux[53] is still of special interest and could be achieved by surface-enhanced Raman scattering.[54] Third, time-lapse imaging of the limonene-producing E. coli was not achieved in this study due to laser toxicity.[55] Machine learningbased methods offer a potential way to mitigate laser toxicity by overcoming tradeoffs between imaging speed, sensitivity, and specificity.[56,57]

## 4. Conclusion

In summary, our study provides direct visualization of the chemical composition and synthetic function of the limonene-rich aggregates inside engineered E. coli. This evidence of channeled limonene and its colocalization with limonene synthase is an important addition to our knowledge of the spatial control of limonene biosynthesis in engineered E. coli, and can offer conceivable guidance on metabolic engineering designs. Further investigations of localized limonene biosynthesis may include broadband coherent Raman imaging and time-lapse SRS imaging of live E. coli cells. With the live-cell imaging capacity, integration of our imaging platform with downstream cell sorting[58,59] is expected.

## 5. Experimental Section

Sample Preparation: The E. coli strains in this study were derived from the BW25113 and DH1 strains. These wild-type strains were transformed with plasmids expressing the heterologous pathways for limonene production. For the two-plasmid system, the limonene synthesis pathway was split among two plasmids. First, the mevalonate pathway was expressed using plasmid pJBEI-3085 from Taek Soon Lee (Addgene #87950). Second, GPPS was expressed from a plasmid derived from pJBEI-3933,[60] but where pinene synthase with limonene synthase using golden gate cloning was replaced. pJBEI-3933 was a gift from Jay D. Keasling. For the oneplasmid system, the transformed plasmid was pJBEI-6409 from Taek Soon Lee (Addgene #47 048) or variants of this plasmid.

Cell cultures were inoculated in Luria Bertani (LB) medium with appropriate antibiotics for plasmid maintenance. For two-plasmid system, chloramphenicol (25 μg mL−1) and carbenicillin (100 μg mL−1) were applied. For one-plasmid system, chloramphenicol (25 μg mL−1) was applied. On the following day, the cell culture was refreshed in M9 media (3 mL). M9 salts are composed of MgSO (2 mm), CaCl (100 μm), casaminos acids (0.2%), thiamine (340 mg L−1), and was supplemented with glucose $( 2 0 \ g \ L ^ { - 1 } )$ and appropriate antibiotics. Limonene was induced by isopropyl ??-d-1-thiogalactopyranoside (IPTG) when OD600 (optical density at 600 nm) reached ≈0.8. The induction level was 100 μm for two-plasmid strains and 50 μm for one-plasmid strains if not otherwise specified. SRS images were taken after ≈72 h for two-plasmid strains and 24 h for oneplasmid strains (except for the one-plasmid BW25113 strain in Figure 2, which was imaged after 24 h). For SRS imaging of cells grown in M9 culture medium, 2–4 μL of cell culture was placed on a poly-l-lysine coated coverslip and sandwiched with another coverslip on the top. For SRS imaging of cells grown on M9 media agarose pads, 3 μL of cell culture was placed on an agarose pad (3%) and sandwiched with another coverslip.

Gas-Chromatography Mass-Spectrometry (GC-MS): Limonene samples were analyzed with an Agilent GC-MS 6890N equipped with an MS detector for up to 800 m/z. Helium was used as a carrier gas at a constant flow rate of 1 ml min−1 in an Agilent 222–5532LTM column. The inlet temperature was set to 300 °C. The oven temperature was held at $5 0 ~ ^ { \circ } \mathsf { C }$ for

30 sec, ramped up to $1 5 0 ~ ^ { \circ } \mathsf C$ at a rate of $2 5 ~ ^ { \circ } C ~ \mathsf { m i n } ^ { - 1 }$ , and then further ramped to 250 °C at a rate of 40 $^ { \circ } \mathsf { C } \mathsf { m i n } ^ { - 1 }$ . The results were analyzed using the MSD Productivity ChemStation (E.02.02.1431). An internal standard of ??-pinene was used as a reference to calculate limonene concentrations.

Ultrafast-Tuning Spectroscopic SRS Microscope: SRS images were acquired using a lab-built SRS microscope (Figure S1, Supporting Information) previously reported.[22] A polygon scanner (Lincoln SA24, Cambridge Technology) scanned the Stokes beam onto a blazed grating (GR50- 0310, Thorlabs). As a reflective wedge, the grating introduces a continuous temporal delay between the pump and the retroreflected Stokes beam. Both the pump and Stokes beams were chirped with high-dispersion glass (SF57, 90 cm in length for the Stokes beam and 75 cm in length for the pump beam). For all experiments, the power on the sample was 20 mW for 966 nm, 14 mW for 800 nm, and 75 mW for 1040 nm, if not otherwise noted. The microscope was equipped with a 60x water immersion objective $( \mathsf { N A } = 1 . 2$ , UPlan-Apo/IR, Olympus). The SRS signal was then captured by a photodiode with a custom-built resonant circuit and extracted by a lock-in amplifier (UHFLI, Zurich Instrument). The same setup was used for two-photon fluorescence imaging with 20 mW for 966 nm. After filtering the excitation beam following the interaction with the sample, a photomultiplier tube (H7422-40, Hamamatsu) was used to measure the two-photon fluorescence signal.

Linear Unmixing of Hyperspectral SRS Signals: For each hyperspectral SRS image stack captured, a pixel-wise spectral unmixing was performed by the built-in MATLAB function LASSO (Least absolute shrinkage and selection operator). For every single pixel, LASSO decomposes its spectrum into the combination of several pure chemicals: $\begin{array} { r } { D = C S + E , D } \end{array}$ is the detected signal $( D \in \mathcal { R } ^ { 1 \times N _ { \lambda } } )$ ). C is the decomposed concentration $( C \in$ $\mathcal { R } ^ { 1 \times k } )$ . S is the measured spectral profiles of pure chemicals $( S \in \mathcal { R } ^ { k \times N _ { \lambda } } )$ . E is the residual term. $N _ { \lambda }$ and k are the number of frames and the number of pure components, respectively. To get the optimal solution for this leastsquare fitting problem, $\mathsf { L } _ { \mathsf { T } }$ -norm regularization was applied and the optimization problem is formulated as: $\begin{array} { r } { \hat { C } = \mathsf { a r g m i n } ( \frac { 1 } { \gamma } \| D - C S \| _ { 2 } ^ { 2 } + \lambda \| C \| _ { 1 } ) } \end{array}$ . ?? is a positive real number that denotes the regularizer penalty level. The same ?? was chosen for a set of data recorded in the same imaging and digitizing conditions. Three spectral profiles were chosen as S including pure limonene, wild-type strain, and background (of each SRS image stack). The averaged Raman spectrum from wild-type was used as a cell background signal as it does neither show limonene content in GC-MS measurement nor Raman peak unique to limonene in SRS spectra. Averaged spectrum of the non-cell area of each SRS image stack was used as a reference to eliminate the background contribution from measurement.

Statistical Analysis: For the hyperspectral SRS images, cell and aggregate segmentation was performed using the pixel classification + object classification workflow in ilastik.[61] For cells grown into the clustered colony, an additional step of manual correction from Schnitzcells was applied in MATLAB to ensure high segmentation accuracy.[62] Using these single-cell segmentation maps, quantification of single-cell features was performed by home-built MATLAB (MathWorks) scripts. Five categories of cell features were quantified: cell feature (area, major axis length), aggregate feature (area, major axis length), intracellular location of aggregate (distance from the aggregate centroid to the furthest cell pole), SRS image feature (SRS intensity at limonene peak $7 6 0 \ c m ^ { - 1 }$ , spectrally summed SRS intensity at C–H and fingerprint window), chemical profile (limonene channel, cell body channel). Spectra of cells/aggregates were represented as mean with shaded error bar (std). Wilcoxon rank sum test was applied to compare the statistical significance between different cell/aggregate population. For quantification of colocalization of limonene and limonene synthase, Mander’s colocalization coefficient was defined as $\sum { L i m _ { i , c o l o c a l } } / \sum { L i m _ { i } }$ , where Lim $_ { i , c o l o c a l } = L i m _ { _ { i } }$ i if LimSyn ≥ threshold, and $L i m _ { i , c o l o c a l } = 0 \ i f L i m S y n < t h r e s h o l d .$

## Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements

This work was supported by DOE Grant BER DE-SC0019387 to MJD, JXC, WW, and R35GM136223 and R01EB032391 to JXC. The authors thank Jean-Baptiste Lugagne and Eric South for helpful discussion on this project. The authors thank Boston University Chemical Instrumentation Center for their assistance with GC-MS experiments.

## Conflict of Interest

The authors declare no conflict of interest.

## Data Availability Statement

The data that support the findings of this study are available in the supplementary material of this article.

## Keywords

escherichia coli, limonene, metabolic engineering, stimulated Raman scattering

Received: July 6, 2022

Revised: August 21, 2022

Published online: September 28, 2022

[1] P. A. Srere, Trends Biochem. Sci. 1985, 10, 109.  
[2] T. F. Moraes, R. A. F. Reithmeier, Biochim. Biophys. Acta BBA – Biomembr. 2012, 1818, 2687.  
[3] J. Ovádi, J. Theor. Biol. 1991, 152, 135.  
[4] L. J. Sweetlove, A. R. Fernie, Nat. Commun. 2018, 9, 2136.  
[5] M. Hajj Chehade, L. Pelosi, C. D. Fyfe, L. Loiseau, B. Rascalou, S. Brugière, K. Kazemzadeh, C.-D.-T. Vo, L. Ciccone, L. Aussel, Y. Couté, M. Fontecave, F. Barras, M. Lombard, F. Pierrel, Cell Chem. Biol. 2019, 26, 482.  
[6] S. An, M. Jeon, E. L. Kennedy, M. Kyoung, in Methods in Enzymology (Eds: N. L. Allbritton, M. L. Kovarik), Academic Press, Cambridge, MA 2019, p. 1.  
[7] A. M. Pedley, S. J. Benkovic, Trends Biochem. Sci. 2017, 42, 141.  
[8] J. B. French, S. A. Jones, H. Deng, A. M. Pedley, D. Kim, C. Y. Chan, H. Hu, R. J. Pugh, H. Zhao, Y. Zhang, T. J. Huang, Y. Fang, X. Zhuang, S. J. Benkovic, Science 2016, 351, 733.  
[9] T. Laursen, J. Borch, C. Knudsen, K. Bavishi, F. Torta, H. J. Martens, D. Silvestro, N. S. Hatzakis, M. R. Wenk, T. R. Dafforn, C. E. Olsen, M. S. Motawia, B. Hamberger, B. L. Møller, J.-E. Bassard, Science 2016, 354, 890.  
[10] V. Pareek, H. Tian, N. Winograd, S. J. Benkovic, Science 2020, 368, 283.  
[11] R. Ciriminna, M. Lomeli-Rodriguez, P. D. Carà, J. A. Lopez-Sanchez, M. Pagliaro, Chem. Commun. 2014, 50, 15288.  
[12] K. A. Wojtunik-Kulesza, K. Kasprzak, T. Oniszczuk, A. Oniszczuk, Chem. Biodivers. 2019, 16, e1900434.  
[13] Y. M. Mukhtar, M. Adu-Frimpong, X. Xu, J. Yu, Biosci. Rep. 2018, 38, BSR20181253.  
[14] C. Sun, C. Theodoropoulos, N. S. Scrutton, Bioresour. Technol. 2020, 300, 122666.  
[15] E. Jongedijk, K. Cankar, M. Buchhaupt, J. Schrader, H. Bouwmeester, J. Beekwilder, Appl. Microbiol. Biotechnol. 2016, 100, 2927.  
[16] Y. Ren, S. Liu, G. Jin, X. Yang, Y. J. Zhou, Biotechnol. Adv. 2020, 44, 107628.  
[17] K. Kochan, H. Peng, E. S. H. Gwee, E. Izgorodina, V. Haritos, B. R. Wood, Analyst 2019, 144, 901.  
[18] M. Kogawa, R. Miyaoka, F. Hemmerling, M. Ando, K. Yura, K. Ide, Y. Nishikawa, M. Hosokawa, Y. Ise, J. K. B. Cahn, K. Takada, S. Matsunaga, T. Mori, J. Piel, H. Takeyama, PNAS Nexus 2022, 1, pgab007.  
[19] J.-X. Cheng, X. S. Xie, Science 2015, 350, aaa8870.  
[20] F. Hu, L. Shi, W. Min, Nat. Methods 2019, 16, 830.  
[21] Stimulated Raman Scattering Microscopy, 1st ed. (Eds: J.-X. Cheng, W. Min, Y. Ozeki, D. Polli), Elsevier, New York 2021.  
[22] H. Lin, H. J. Lee, N. Tague, J.-B. Lugagne, C. Zong, F. Deng, J. Shin, L. Tian, W. Wong, M. J. Dunlop, J.-X. Cheng, Nat. Commun. 2021, 12, 3052.  
[23] M. Zhuge, K.-C. Huang, H. J. Lee, Y. Jiang, Y. Tan, H. Lin, P.-T. Dong, G. Zhao, D. Matei, Q. Yang, J.-X. Cheng, Adv. Sci. 2021, 8, 2003136.  
[24] R. Oda, J. Shou, W. Zhong, Y. Ozeki, M. Yasui, M. Nuriya, iScience 2022, 25, 103936.  
[25] C. Zhao, Y. Kim, Y. Zeng, M. Li, X. Wang, C. Hu, C. Gorman, S. Y. Dai, S.-Y. Ding, I. S. Yuan, ACS Synth. Biol. 2018. 7. 774.  
[26] B. Long, B. Fischer, Y. Zeng, Z. Amerigian, Q. Li, H. Bryant, M. Li, S. Y. Dai, J. S. Yuan, Nat. Commun. 2022, 13, 541.  
[27] K. Bae, W. Zheng, K. Lin, S. W. Lim, Y. K. Chong, C. Tang, N. K. King, C. B. Ti Ang, Z. Huang, Anal. Chem. 2018, 90, 10249.  
[28] Y. Yang, Y. Yang, Z. Liu, L. Guo, S. Li, X. Sun, Z. Shao, M. Ji, Anal. Chem. 2021, 93, 6223.  
[29] J. Du, Y. Su, C. Qian, D. Yuan, K. Miao, D. Lee, A. H. C. Ng, R. S. Wijker, A. Ribas, R. D. Levine, J. R. Heath, L. Wei, Nat. Commun. 2020, 11, 4830.  
[30] X. Lang, K. Welsher, J. Chem. Phys. 2020, 152, 174201.  
[31] P.-T. Dong, C. Zong, Z. Dagher, J. Hui, J. Li, Y. Zhan, M. Zhang, M. K. Mansour, J.-X. Cheng, Sci. Adv. 2021, 7, eabd5230.  
[32] H. Xiong, L. Shi, L. Wei, Y. Shen, R. Long, Z. Zhao, W. Min, Nat. Photonics 2019, 13, 412.  
[33] W. R. Angus, Proc. Indian Acad. Sci. – Sect. A 1938, 8, 529.  
[34] J. Alonso-Gutierrez, R. Chan, T. S. Batth, P. D. Adams, J. D. Keasling, C. J. Petzold, T. S. Lee, Metab. Eng. 2013, 19, 33.  
[35] John Wiley & Sons, Inc., “SpectraBase,” to be found under https:// spectrabase.com/  
[36] P. An, C.-Q. Yuan, X.-H. Liu, D.-B. Xiao, Z.-X. Luo, Chin. Chem. Lett. 2016, 27, 527.  
[37] R. Tibshirani, J. R. Stat. Soc. Ser. B Methodol. 1996, 58, 267.  
[38] J. W. Young, J. C. W. Locke, A. Altinok, N. Rosenfeld, T. Bacarian, P. S. Swain, E. Mjolsness, M. B. Elowitz, Nat. Protoc. 2012, 7, 80.  
[39] K. W. Dunn, M. M. Kamocka, J. H. McDonald, Am. J. Physiol.-Cell Physiol. 2011, 300, C723.  
[40] T. Tian, J. Fan, S. E. Elf, Cancer Commun 2021, 41, 439.  
[41] V. Pareek, Z. Sha, J. He, N. S. Wingreen, S. J. Benkovic, Mol. Cell 2021, 81, 3775.  
[42] F. M. Meyer, J. Gerwig, E. Hammer, C. Herzberg, F. M. Commichau, U. Völker, J. Stülke, Metab. Eng. 2011, 13, 18.  
[43] K. Jørgensen, A. V. Rasmussen, M. Morant, A. H. Nielsen, N. Bjarnholt, M. Zagrobelny, S. Bak, B. L. Møller, Curr. Opin. Plant Biol. 2005, 8, 280.  
[44] Y.-H. P. Zhang, Biotechnol. Adv. 2011, 29, 715.  
[45] A. H. Chen, P. A. Silver, Trends Cell Biol. 2012, 22, 662.  
[46] I. Wheeldon, S. D. Minteer, S. Banta, S. C. Barton, P. Atanassov, M. Sigman, Nat. Chem. 2016, 8, 299.  
[47] C. Singleton, T. P. Howard, N. Smirnoff, J. Exp. Bot. 2014, 65, 1947.  
[48] A. B. Lindner, R. Madden, A. Demarez, E. J. Stewart, F. Taddei, Proc. Natl. Acad. Sci 2008. 105. 3076.  
[49] D. T. Kysela, P. J. B. Brown, K. C. Huang, Y. V. Brun, Annu. Rev. Microbiol. 2013, 67, 417.  
[50] D. Polli, V. Kumar, C. M. Valensise, M. Marangoni, G. Cerullo, Laser Photonics Rev. 2018, 12. 1800020.  
[51] H. Ni, P. Lin, Y. Zhu, M. Zhang, Y. Tan, Y. Zhan, Z. Wang, J.-X. Cheng, Anal, Chem, 2021, 93, 15703.  
[52] Y. Zhang, A. R. Fernie, EMBO Rep. 2020, 21, e50774.  
[53] M. J. Dunlop, Z. Y. Dossani, H. L. Szmidt, H. C. Chu, T. S. Lee, J. D. Keasling, M. Z. Hadi, A. Mukhopadhyay, Mol. Syst. Biol. 2011, 7, 487.  
[54] F. Lussier, D. Missirlis, J. P. Spatz, J.-F. Masson, ACS Nano 2019, 13, 1403.  
[55] X. Yuan, Y. Song, Y. Song, J. Xu, Y. Wu, A. Glidle, M. Cusack, U. Z. Ijaz, J. M. Cooper, W. E. Huang, H. Yin, Appl. Environ. Microbiol. 2018, 84, 8.  
[56] J. Zhang, J. Zhao, H. Lin, Y. Tan, J.-X. Cheng, J. Phys. Chem. Lett. 2020, 11, 8573.  
[57] B. Manifold, S. Men, R. Hu, D. Fu, Nat. Mach. Intell. 2021, 3, 306.  
[58] K. S. Lee, M. Palatinszky, F. C. Pereira, J. Nguyen, V. I. Fernandez, A. J. Mueller, F. Menolascina, H. Daims, D. Berry, M. Wagner, R. Stocker, Nat. Microbiol. 2019, 4, 1035.  
[59] P. Liang, B. Liu, Y. Wang, K. Liu, Y. Zhao, W. E. Huang, B. Li, Appl. Environ. Microbiol. 2021, 88, 3.  
[60] S. Sarria, B. Wong, H. G. Martín, J. D. Keasling, P. Peralta-Yahya, A. C. S. Synth. Biol. 2014. 3. 466.  
[61] S. Berg, D. Kutra, T. Kroeger, C. N. Straehle, B. X. Kausler, C. Haubold, M. Schiegg, J. Ales, T. Beier, M. Rudy, K. Eren, J. I. Cervantes, B. Xu, F. Beuttenmueller, A. Wolny, C. Zhang, U. Koethe, F. A. Hamprecht, A. Kreshuk. Nat. Methods 2019, 16. 1226.  
[62] J. Young, M. Elowitz, Schnitzcells: Software for Quantitative Analysis of Time-Lapse Movies, CaltechDATA, 2021, http://doi.org/10.22002/ D1.1895.