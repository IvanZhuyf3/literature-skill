Review

# Unveiling Cancer Metabolism through Spontaneous and Coherent Raman Spectroscopy and Stable Isotope Probing

Jiabao Xu 1,\* , Tong Yu 1, Christos E. Zois 2,3, Ji-Xin Cheng 4, Yuguo Tang 5, Adrian L. Harris 2,\* and Wei E. Huang 1,\*

1 Department of Engineering Science, University of Oxford, Oxford OX1 3PJ, UK; tong.yu@spc.ox.ac.uk  
2 Molecular Oncology Laboratories, Department of Oncology, Weatherall Institute of Molecular Medicine, John Radcliffe Hospital, Oxford University, Oxford OX3 9DS, UK; christos.zois@oncology.ox.ac.uk  
3 Department of Radiotherapy and Oncology, School of Health, Democritus University of Thrace, 68100 Alexandroupolis, Greece  
4 Department of Biomedical Engineering, Boston University, Boston, MS 02215, USA; jxcheng@bu.edu  
5 Suzhou Institute of Biomedical Engineering and Technology, Chinese Academy of Sciences, Suzhou 215163, China; tangyg@sibet.ac.cn  
\* Correspondence: jiabao.xu@eng.ox.ac.uk (J.X.); adrian.harris@oncology.ox.ac.uk (A.L.H.); wei.huang@eng.ox.ac.uk (W.E.H.)

Simple Summary: Raman spectroscopy and imaging are label-free, non-destructive techniques to study cellular metabolism with subcellular spatial resolution. This review focuses on applications of Raman-based methods in a combination of stable isotope probing on cancer metabolism and cancer imaging.

![](images/7f522ae01d9fc04ef96c16455177240cea83e6c5a4b943e5b5bc307c4b8880a4.jpg)

- -

Citation: Xu, J.; Yu, T.; Zois, C.E.; Cheng, J.-X.; Tang, Y.; Harris, A.L.; Huang, W.E. Unveiling Cancer Metabolism through Spontaneous and Coherent Raman Spectroscopy and Stable Isotope Probing. Cancers 2021, 13, 1718. https://doi.org/ 10.3390/cancers13071718

Academic Editor: Mark W Dewhirst

Received: 9 March 2021

Accepted: 28 March 2021

Published: 5 April 2021

Publisher’s Note: MDPI stays neutra with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/701734572a8c96160c6f51afa20168eff9474bc83dd504473cdb547e1e46b43a.jpg)

Copyright: © 2021 by the authors. Licensee MDPL. Basel. Switzerland This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

Abstract: Metabolic reprogramming is a common hallmark in cancer. The high complexity and heterogeneity in cancer render it challenging for scientists to study cancer metabolism. Despite the recent advances in single-cell metabolomics based on mass spectrometry, the analysis of metabolites is still a destructive process, thus limiting in vivo investigations. Being label-free and nonperturbative, Raman spectroscopy offers intrinsic information for elucidating active biochemical processes at subcellular level. This review summarizes recent applications of Raman-based techniques, including spontaneous Raman spectroscopy and imaging, coherent Raman imaging, and Raman-stable isotope probing, in contribution to the molecular understanding of the complex biological processes in the disease. In addition, this review discusses possible future directions of Raman-based technologies in cancer research.

Keywords: cancer metabolism; Raman spectroscopy; stimulated Raman scattering; coherent Raman anti-Stokes scattering; Raman imaging; lipid metabolism; stable isotope probing

## 1. Introduction

Reprogrammed metabolism is considered a hallmark of cancer [1]. Cancer metabolism is a question of great interest in a wide range of fields since the “Warburg Effect” indicated aerobic glycolysis, as a characteristic of cancer cells [2]. Cancer cells rely on the acquisition of nutrients from the environment to meet the demand for energy and biomass production. In the last few decades, features of tumor-associated metabolic alteration were widely observed. Key questions among the tumor metabolic reprogramming rapidly expanded our understanding of carcinogenesis. In particular, how cancer cells reprogram their metabolism and interact with other biological processes, which mechanisms and functions of nutrient acquisition in cancer cells are achieved, and what targeted pathways in metabolism can be engaged to selective development of inhibitors during therapeutic evaluation [3].

Cancer metabolism is highly complex and heterogeneous, subject to environmental cues. The metabolic phenotype is dependent on the tumor microenvironment. It is now clear that even though cancer cells are from the same tumor with the same genotypes, they can manifest distinct phenotypic states in different positions [4]. Challenges remain in investigating the vastly complex metabolism of cancer with regards to intra-tumoral heterogeneity, different tissues, and tumor types.

Metabolomics based on mass spectrometry is a gold standard for study of cellular metabolites. Although lagging behind other single-cell omics methods, it recently advances to the level where multiplex analysis from single cells could be achieved [5,6]. However, the disadvantages of mass spectrometry metabolomics remain due to its destructive nature, prohibiting live cell analysis. Moreover, it does not offer insights on the spatial information of metabolite distribution, which can be crucial in heterogeneous intra-tumor environments. Fluorescence-based methods offer high sensitivity and selectivity, and they can provide sub cellular resolution. However, the fluorophore labels are often much larger than the targeted molecules and thus can hinder the intrinsic metabolism [7]. The prerequisite of knowing the target molecules also hinders multiplex targeting and investigative probing. Consider ing the high complexity and heterogeneity in cancer, minimally invasive, non-destructive, and label-free tools with imaging ability providing subcellular spatial information, are in need to study cancer metabolism and fulfill the translational clinical need.

Raman spectroscopy technologies present several advantages for the cancer research community. In particular, Raman spectroscopy is a label-free spectroscopic method to provide comprehensive biochemical information, the so-called “biomolecular fingerprint”, regarding metabolic processes in cells and tissues. In addition, Raman imaging offers high spatial resolution at the sub-cellular level and is capable of real-time, noninvasive examination of living cells, tissues, and organisms, based on their metabolic profiles.

This review aims to present Raman-based technologies in the area of cancer research, to study the metabolism of single cells as well as physio-pathological tissues. First, we present applications of label-free Raman spectroscopy and imaging in cancer metabolism. Second, we discuss Raman-based technologies combined with stable isotope probing (SIP) for studying metabolic fates of specific metabolites. The primary focus of the methodology is on spontaneous Raman spectroscopy and coherent Raman scattering (CRS) microscopy. Readers interested in surface-enhanced Raman scattering and other Raman-based methodologies are referred to excellent reviews elsewhere [8–11].

## 2. Background of Raman Spectroscopy and Coherent Raman Scattering

## 2.1. Spontaneous Raman Spectroscopy and a Cell’s Fingerprint

Raman spectroscopy is an essential tool for chemists, physicists, biologists, and materials scientists. It was first experimentally observed by C. V. Raman in 1928, for which he was awarded the Nobel Prize in 1930 [12]. In Raman spectroscopy, a sample is illuminated with a monochromatic laser beam (Figure 1A). The incident laser beam with a frequency of $v _ { 0 }$ interacts with a molecule in the sample that has a vibrational frequency of $v _ { m }$ . This interaction originates scattered light. The vast majority of the scattered light is elastic scattering, the so-called Rayleigh scattering. However, due to energy exchange between the incident photons and molecular vibration, there is a small fraction of inelastic scattering, which has a different frequency from that of the incident light, collectively called Raman scattering. Raman scattering consists of both Stokes scattering, which has a lower frequency at $\begin{array} { r } { \boldsymbol { v } _ { 0 } - \boldsymbol { v } _ { m } , } \end{array}$ and anti-Stokes scattering, which has a higher frequency at $v _ { 0 } + v _ { m }$ (Figure 1B) The Stokes spectrum is often presented as the Raman spectrum, due to its higher intensity, as compared to the anti-Stokes lines.

![](images/33f727d85aaf0e9dae344b1271958cd38822ab55d567a7a0c13d914261cdcf97.jpg)  
Figure 1. (A) Electromagnetic radiation interacting with a vibrating molecule. (B) Schematic energy diagrams of spontaneous Raman scattering and coherent Raman scattering (CRS). The solid arrows indicate laser excitation or stimulated emission; the dashed arrows indicate spontaneous scattering process.

Raman spectroscopy is now increasingly popular among biologists. A Raman spectrum can be regarded as a phenotype of a biological system because it provides an overall molecular vibrational profile, containing Raman bands for major cellular building blocks, such as proteins, nucleic acids, lipids, and carbohydrates. Figure 2 illustrates a Raman spectrum of a single glioblastoma cell with Raman bands marked with assignments of major biological macromolecules. A biological Raman spectrum can be divided into three regions—the ‘fingerprint’ region that contains essential bio-information and can be seen as a fingerprint of a cell $( 4 0 0  – 1 8 0 0 \ c m ^ { - 1 } )$ ; the ‘silent’ region that usually does not involve vibrational modes contributed by biomolecules formed of naturally occurring isotopes and can involve bands contributed by stable isotopes or triple bonds $( 1 8 0 0 { - } 2 7 0 0 \ \mathrm { c m } ^ { - 1 } )$ ; the high-wavenumber region that is specifically contributed by the stretching vibrations of CH groups, predominantly from lipids and proteins $( 2 7 0 0 - 3 2 0 0 \mathrm { c m } ^ { - 1 } )$ .

The advantages of using Raman micro-spectroscopy in biological studies are high spatial resolution; ability to detect aqueous samples; intrinsic and label-free characterization; non-contacting and non-destructive analysis; and easy preparation and small sample volume.

By combining the power of optical magnification and direct visualization, Raman micro-spectroscopy can probe biological systems at a subcellular resolution. For large biological systems like tissues, it can collectively produce label-free Raman images with subcellular structural and chemical information. The ability to analyze aqueous samples separates Raman spectroscopy from other vibrational spectroscopies like infrared (IR) spectroscopy. A water molecule has low polarizability, thus, it minimally hinders sample signals in Raman spectroscopy and can be easily subtracted during preprocessing procedures. This is particularly advantageous in biological studies because it avoids laborious sample drying preparation, which might also alter the biochemistry of the samples.

![](images/2053b0be5090c7bbed6a250167339c6240e0115d3f9d0240057dcc2d3c9c218f.jpg)

<details>
<summary>line chart</summary>

| Raman shift cm⁻¹ | Raman Intensity a.u. |
| ---------------- | -------------------- |
| 500              | ~0                   |
| 1000             | ~0                   |
| 1500             | ~0                   |
| 2000             | ~0                   |
| 2500             | ~0                   |
| 3000             | ~1.0                 |
</details>

Figure 2. Raman spectrum—a cell’s fingerprint. Raman spectrum of a single cell of human primary glioblastoma U87 cell line, demonstrating various bands representative of cellular constituents.

Molecular labeling using genetically encoded reporters (e.g., green fluorescent protein) is used extensively for monitoring cellular events in biological systems [13]. The introduction of unnatural functional groups might risk interfering with the native biological processes. Raman spectroscopy, on the other hand, is label-free and able to probe bio logical samples in their natural setting. It also does not require any prior knowledge of the particular substrate for selective labeling. It unbiasedly probes all macromolecules and collectively displays their vibrational modes in one spectrum. Raman spectroscopy is also non-contacting and non-destructive, as opposed to other analytical tools such as gas chromatography and mass spectrometry that destroy the sample to achieve results. This non-invasive, label-free, and spatially resolved nature renders Raman spectroscopy suitable for in vitro and in vivo biological investigations, from investigating a single cancer cell, to producing biochemical maps of cancerous tissues.

## 2.2. Coherent Raman Scattering for High-Speed Imaging

Having discussed the advantages of Raman micro-spectroscopy, the challenge is intrinsically weak Raman scattering as approximately only 1 in $1 0 ^ { 7 }$ photons experiences inelastic scattering [14]. Another Raman-based approach is emerging in recent decades to obtain much stronger vibrational signals by coherent Raman scattering (CRS), which employs multiple light sources to produce coherent Raman signals.

Coherent anti-Stokes Raman scattering (CARS) and stimulated Raman scattering (SRS) are two CRS processes [15–18]. During spontaneous Raman scattering, the pump beam with a frequency of $\nu _ { 0 }$ is incident upon the sample generating a Stokes signal $\nu _ { S }$ and an anti-Stokes signal $\nu _ { a S } .$ . In SRS, two laser beams at frequencies $\nu _ { 0 }$ and $\nu _ { S }$ are directed onto the sample, such that the frequency difference $\nu _ { 0 } - \nu _ { S }$ matches the frequency of a molecular vibrational mode $\nu _ { m }$ (Figure 1B). This process causes stimulated excitation of a chemically specific signature and brings the advantage of suppressing non-resonant background. Experimentally, either stimulated-Raman gain (SRG) of the Stokes or stimulated-Raman loss (SRL) of the pump is measured, and optical modulation and demodulation are required to extract the proper SRS signal [19].

CARS involves a complex four-beam mixing process probing, as shown in Figure 1B. As in SRS, the resonance occurs when the difference between the pump and Stokes beam $\nu _ { 0 } \mp \nu _ { S }$ matches a molecular vibration in the sample. This resonance is then probed by the third field at $\nu _ { 0 }$ and generates an anti-Stokes signal at $2 \nu _ { 0 } \mp \nu _ { S }$ . With respect to SRS, no complex demodulation schemes are required in CARS. However, the presence of a strong non-resonant background due to the four-wave mixing that does not carry any chemical information can distort and overwhelm the resonant signal [20].

With the advantages of dramatically enhanced Raman signal and little autofluorescence interference, CARS and SRS microscopy are emerging techniques for real-time analysis and video-rate imaging of cells and tissues in a living system, with high speed and 3D spatial resolution [21]. Nonetheless, both techniques are limited to the complex set-up of two synchronized trains of laser pulses. CARS and SRS are also limited by the small spectral range due to the narrow bandwidths between lasers. Therefore, so far in most cases, these were demonstrated for chemical signatures with high concentrations and strong Raman signals, for example, the $\mathrm { C H } _ { 2 }$ stretching vibrations that are typically found in lipids in cells [22]. In addition, CARS suffers from the complicated interpretation of Raman bands due to changed band frequencies [20]. SRS, on the other hand, shows a comparable spectrum like spontaneous Raman. Its signal also shows an intensity that is linearly proportional to the concentration of the targeted molecules and is free of nonresonant background. With the intensity of the signal proportional to the concentration of the metabolites of interest, semi-quantitative molecular profiling of single cells and tissues is possible [23–27]. SRS would be a complementary tool to spontaneous Raman scattering and simultaneously using the two can be beneficial (Table 1) [28]. The investigation of a biological system can begin with spontaneous Raman scattering (acquisition time from seconds to minutes) covering the entire spectral window of molecular vibrations and looking for a defined marker of interest. It could then be followed with SRS focusing on a prede fined spectral window and offering high-speed benefit (acquisition time microseconds) for imaging and collection of a huge amount of spectral data.

Table 1. Comparison of spontaneous Raman spectroscopy and spectroscopic SRS microscopy, which are complementary to each other and can be used simultaneously.

<table><tr><td></td><td colspan="2">Spontaneous Raman</td><td>Spectroscopic SRS</td></tr><tr><td>Advantages</td><td colspan="2">Relatively cost-effective and easy operationWhole spectral range with high spectral resolution</td><td>Enhanced signalFree from fluorescence and non-resonant backgroundComparable spectrum with spontaneous Raman</td></tr><tr><td>Disadvantages</td><td colspan="2">Intrinsically weak signalFluorescence interference</td><td>Complex and expensive set-upNarrow spectral range with low spectral resolution</td></tr><tr><td>Suitability</td><td colspan="2">Investigative spectral study</td><td>Targeted high-speed imaging</td></tr><tr><td>Speed per spectra</td><td colspan="2">100 millisecond</td><td>20 microsecond</td></tr><tr><td>Time required for a 200×200 image</td><td colspan="2">~1 hour</td><td>~1 second</td></tr><tr><td>Spectral width</td><td colspan="2">Whole spectral range up to 4000 cm-1</td><td>200 cm-1</td></tr><tr><td>Target</td><td colspan="2">Whole spectrum</td><td>Mostly CH stretching [15,16], recently also fingerprint [17]</td></tr><tr><td>Spectral resolution</td><td colspan="2">~1 cm-1</td><td>10 cm-1</td></tr></table>

## 3. Raman Spectroscopy as a Label-Free Tool for Cancer Metabolism Investigation

Metabolic reprogramming is now a widely accepted hallmark of cancer [3]. Monitoring metabolites and understanding the reprogramming pathways are crucial to fully understand cellular metabolism in cancer development and to provide new therapeutic targets. Raman spectroscopy and Raman imaging benefit cancer research and understanding of metabolic regulation in cancers, because it offers single-cell resolution or spatial informa tion about biochemical composition of nucleic acids, proteins, lipids, and other metabolites. The defined subcellular locations cannot be provided by conventional analytical methods that rely on bulk or fractionated analyses of extracted components, e.g., mass spectrometry, nuclear magnetic resonance spectroscopy, and high-performance liquid chromatography. As a label-free technique, Raman spectroscopy also outperforms many fluorescence-based approaches that involve exogenous probes and can interfere with intrinsic biological processes.

## 3.1. Investigation of Lipid Metabolism in Cancer Cells

Lipid reprogramming is one of the key features of cancer’s metabolic adaptation [29]. Alterations in lipid metabolism were observed in many different cancer types [30–33], and have important therapeutic inferences, as they affect the survival, dynamics, and response of cancer cells. Raman microscopy is one of the most powerful techniques for analyzing the properties of lipids in cancer cells, offering lipid compositional information as well as spatial information within cellular compartments. As the lipidic CH stretching vibrations are the strongest among all Raman vibrations generated in the high-frequency region of 2800–3200 cm-1, lipid metabolism is possibly the most investigated subject by Raman spectroscopy.

To satisfy proliferation demand, cancer cells exhibit a higher content of cellular lipid content than normal cells. Lipids are particularly in demand as nutrient sources for energy supply, building blocks for membrane biogenesis, and as lipid-derived signaling molecules [34]. A number of studies found an altered lipid metabolism related to the pro gression of cancer by Raman spectroscopy [23,35–38]. Abramczyk et al. found an increasing content of lipid droplets in mildly malignant (MCF7) and malignant (MDA-MB-231) breast cancer cells, as compared to the non-malignant (MCF10A) cells [36]. They also demon strated altered lipid metabolism in adipocytes of the breast tissue from breast epithelial cells. Nieva et al. used Raman micro-spectroscopy to characterize lipid metabolism of breast cancer cells with different degrees of malignancy [39]. By analyzing characteristic Raman bands related to lipid content at 3014, 2935, 2890, and 2845 $\mathrm { c m } ^ { - 1 }$ , they hypothesized that the lipid content of breast cancer cells might be a useful indirect measure of a variety of functions coupled to breast cancer progression. A study by Tirinato et al. demonstrated the capability of functional characterization of lipid droplets in cancer stem cells (CSCs) by Raman spectroscopy, and confirmed lipid droplets as a distinctive mark of CSCs in colorectal cancer [40]. Similarly, lipid upregulation and reprogramming was observed by Raman spectroscopy in cells of prostate cancer [23], lung cancer [41], and melanoma [42,43].

Subcellular composition and distribution of lipids were the center of the subject by both CARS and SRS microscopy, due to strong contrast in the CH vibrations. The high speed capacity of CRS realizes rapid biochemical–optical lipid imaging, which is comparable to the traditional optical methods. In 2003, Nan et al. first used CARS microscopy to image neutral lipid droplets (LDs) in live fibroblast cells [44]. In 2008, Freudiger et al. used SRS microscopy to visualize lipid distribution with depth information [45]. They monitored lipids along varying depths of mouse skin, as well as DMSO penetrating into the skin. Since then, CRS microscopy was used extensively in lipid imaging with structural diversity tightly associated with their biological functions [43,46–55].

Hyperspectral CRS microscopy was applied to study changes in lipid composition (e.g., saturated vs. unsaturated) of cancer cells and tissues, which plays an important role in cancer metabolism and development. For example, increased saturation in phospholipids markedly alters signal transduction, protects cancer cells from oxidative damage, and po tentially inhibits chemotherapeutic drug uptake [56]. Wang et al. visualized a substantial amount of saturated lipids accumulated in liver cancer tissues, compared with the adjacent noncancerous tissues [49]. Li et al. reported significantly increased levels of unsaturated lipids in ovarian ${ \mathrm { C S C s } } ,$ as compared to non-CSCs (Figure 3) [48]. Subsequent experiments showed that inhibition of lipid desaturases effectively eliminated ${ \mathrm { C S C s } } ,$ suppressed sphere formation, and blocked tumor initiation capacity in vivo. With spontaneous Raman spec troscopy, followed by SRS microscopy and transcriptomics analysis, Du et al. investigated and imaged lipids droplets in patient-derived melanoma cells during differentiation [43]. They identified fatty acid synthesis pathway as a druggable susceptibility and a lipid mono-unsaturation within de-differentiated mesenchymal cells, with innate resistance to BRAF inhibition.

![](images/ce567eb59537dde651cdbef7046eb5f8114fc368ad46fd14eca9d03e571c718c.jpg)

<details>
<summary>text_image</summary>

A
2900 cm⁻¹
3002 cm⁻¹
Ratio I₃₀₀₂/I₂₉₀₀
ALDH-/CD133-
ALDH+/CD133+
0.5
0.4
0.3
0.2
0.1
0.5
0.4
0.3
0.2
0.1
</details>

![](images/e5b7b17780bd531ecf8e016e98321ecdb6b538ded4b25371da9036537218e657.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | ALDH-/CD133- | ALDH+/CD133+ |
| ------------------ | ------------ | ------------ |
| 2850               | ~22          | ~21          |
| 2900               | ~24          | ~23          |
| 2950               | ~18          | ~17          |
| 3000               | ~6           | ~8           |
| 3050               | ~0           | ~0           |
</details>

Figure 3. Increased lipid unsaturation level in ovarian cancer cells represented by intensity ratio between $2 9 0 0 \mathrm { a n d } 3 0 0 2 \mathrm { c m } ^ { - 1 }$ . (A) Representative hyperspectral SRS images of flow-sorted $\mathrm { A L D H ^ { - } / C D 1 3 3 ^ { - } }$ and $\mathrm { A L D H ^ { + } / C D 1 3 3 ^ { + } }$ COV362 cells. Images at 2900 and $3 0 0 2 \mathrm { c m } ^ { - 1 }$ , and the intensity ratio image between 3002 and $2 9 0 0 \mathrm { c m } ^ { - 1 }$ are shown. Scale bars: 10 µm. (B) Average SRS spectra from the lipid droplets in $\mathrm { A L D H } ^ { - } / \mathrm { C D } 1 3 3 ^ { - } \left( n = 3 \right)$ and $\mathrm { A L D H ^ { + } / C D 1 3 3 ^ { + } }$ cells $( n = 8 )$ . Shaded area indicates the standard deviation of SRS spectral measurement from different cells. Reprinted and adapted with permission from reference [48].

## 3.2. Investigation of Cellular Metabolism beyond Lipids

The applicability of Raman-based techniques is not limited to lipid in the high frequency CH region. The fingerprint region between 300 and $1 8 0 0 \mathrm { c m ^ { - 1 } }$ contains a collec tion of biological information of a cell. Investigative research focusing on the fingerprint region can either aim for a particular biomarker or use the whole region with chemometric techniques, to deconstruct Raman bands into biological information. Figure 4 shows an example of spontaneous Raman imaging of a HeLa cell, using the fingerprint region as well as the high-wavenumber region of Raman spectra.

The study of proteins can be conducted by investigating Raman bands of Amide vibrational modes, including Amide I that ranges from $1 6 0 0 { - } 1 6 7 0 \ \mathrm { c m } ^ { - 1 }$ , Amide II that ranges from $1 4 8 0 { - } 1 5 8 0 \mathrm { c m } ^ { - 1 }$ , and Amide III that ranges from $1 2 3 0 { - } 1 3 0 0 \mathrm { c m } ^ { - 1 }$ . A study of two breast cancer and one normal breast cell lines (MDA-MB-436, MCF-7, and MCF-10A) illustrated decreased protein content in cancerous cell line [57]. A linear discriminant analysis (LDA) model on the entire spectral range predicted the three cell lines with 100% sensitivity and 91% specificity. Abramczyk et al. demonstrated a Raman biomarker of protein phosphory lation using the ratio between two Raman peaks at 1586 and $8 2 9 \mathrm { c m } ^ { - 1 }$ , representing tyrosine phosphorylation [58]. They subsequently found overexpressed phosphorylation in the human breast, small intestine, and brain tissues, and in the glioblastoma U-87 MG cell line using this Raman biomarker. Using a multivariate curve resolution (MCR) to deconstruct the whole Raman spectra, Marro et al. demonstrated different intensities of proteins, lipids, and mitochondria Raman bands in primary breast cancer cell lines and their metastatic variants in bone [59]. Kopec et al. imaged and located glycogen, glycosaminoglycan, chondroitin sulfate, heparan sulfate proteoglycan, and distinguished each chemical species in normal and cancer tissues [60]. As a result, the study concluded that the metabolism of proteins, lipids, and glycans was markedly deregulated in breast (adenocarcinoma) and brain (medulloblastoma) tumors. Using a principal component–linear discriminant analysis (PC–LDA) to deconstruct the Raman spectra of primary normal breast cells, and immortalized, transformed, non-invasive, and invasive breast cancer cells, Chaturvedi et al. identified distinct clustering of cell types with a high degree of sensitivity [61]. A study by Lemoine included 547 in situ Raman spectra from 65 patients undergoing glioma resection and systematic literature analysis of Raman study of glioma [62]. They subsequently used band fitting for extraction of Raman features and identified oncogenic processes involved with increased nucleic acid content, overexpression of type IV collagen, and a shift in the primary metabolic engine.

![](images/54f38654835eb4ff6c697e86fe663913d6bf611eb1e9cbef6b8d567a2593398f.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of a cell with visible nucleus and cytoplasm, scale bar indicates 7 μm (no text or symbols on the image itself)
</details>

![](images/9a69600f0548e23c1b19858f67157f1d009d3f597f11747eb2feea7735ab1323.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image of a nucleic acid sample at 781 cm⁻¹, showing red emission against black background with scale bar (7 μm)
</details>

![](images/43cf21248542ae2f3c129b0b3c464befcdab129af0a733bb5504141e0c044a4d.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing green-labeled lipid structures with a 2845 cm⁻¹ scale bar and 7 μm scale bar (no textual annotations beyond labels)
</details>

![](images/3e2bb979938d400c1d99c36236bd15982c69d12d07d73ebb9315c54e64ec4160.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image of a cell under 855 cm⁻¹ tyrosine treatment, showing purple-stained nucleus and cytoplasmic structures (scale bar: 7 μm)
</details>

![](images/19282336c742e2584bcdc8caf9cc581dbf77c6af0a23d8d9e8cb9f4d9c8842a0.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing a blue-stained cellular structure with 1665 cm⁻¹ protein label and 7 μm scale bar (no additional text or symbols)
</details>

Figure 4. Raman images of a HeLa cell based on fingerprint Raman spectra, reconstructed from intensities at 781 (nucleic acids), 855 (tyrosine), 1665 (protein), and $2 8 4 5 \mathrm { c m } ^ { - 1 } \left( \mathrm { l i p i d s } \right)$ . The Raman images show the distributions of these biomolecules with various intensities at the subcellular level.

Coherent Raman imaging of proteins besides lipids is also a common practice in both SRS and CARS microscopy. Imaging the CH moiety at the high-frequency region provides information of both proteins and lipids, as it is rich in both proteins and lipids. Therefore, protein images can be obtained indirectly by subtracting the lipid moiety contribution from CH-derived images [52,55,63–65]. In addition, protein molecules can be imaged at $1 6 5 5 \mathrm { c m } ^ { - 1 }$ at the Amide I peak [64]. The Xie group demonstrated that DNA distribution could also be retrieved from the strong background of proteins and lipids at the CH region through linear decomposition of the SRS images [65].

Molecular vibrations in the fingerprint region other than the Amide I group show markedly reduced intensities, compared to the high-frequency CH stretching region, which is less studied in CRS microscopy [55]. At the fingerprint region, Sunney Xie’s group demonstrated the first SRS imaging of DNA at the fingerprint region in living cells [64], by using Raman bands at 785 and $1 0 9 0 \mathrm { c m ^ { - 1 } }$ . Recently, advancement in instrumentation and data science enabled SRS metabolic imaging of cancer cells in the fingerprint region with enhanced sensitivity. Cheng’s group reported SRS imaging of retinoids with significantly boosted molecular sensitivity to 34 micromolar, via visible preresonance SRS (VP–SRS)

microscopy [66]. By shifting the excitation laser wavelength to visible range, approaching the absorption of intrinsic chromophores, the study demonstrated heterogeneous distribu tion of retinoid storage inside various cancer cells and chemoresistant ovarian cancer cells. Combining advanced instrumentation using a polygon-based ultrafast delay scanner and advanced data science approach of a spatial–spectral residual learning network, the group further demonstrated 100 times improvement of signals in fingerprint SRS imaging. They illustrated distribution of proteins, cholesterols, and lipids, in live pancreatic cancer cells, as well as in a whole mouse brain [17].

## 3.3. Cellular Responses to Anti-Cancer Drugs and Radiotherapy

The uptake, metabolism, and distribution of a drug candidate in targeted cancer cells or tissues are pivotal during drug discovery and development. Raman spectroscopy and CRS microscopy were used to exploit metabolic transformation in cancer cells as a drug target. Jamieson et al. investigated responses of PC3 prostate cancer cells to a series of lipid targeting drugs [67]. Compared to the non-cancerous cells, the beta-blocker propranolol selectively chose the cancer cells in their Raman lipid profiles, showing an unexpected anti-cancer potential. The cellular lipid content in response to the drug was also studied by CARS microscopy [68]. By imaging the subcellular lipid distribution in hormone-treated breast and prostate cancer cells, the researchers found an increased number and size of intracellular lipid droplets and a higher degree of saturation in treated T47D and LNCaP cells than untreated cells.

In addition to lipids, comprehensive metabolic adaptations of cancer cells in re sponse to anti-cancer drugs could be investigated by studying the entire Raman spectral region [69–74]. El-Mashtoly et al. applied Raman spectral imaging to study the effect of the epidermal growth factor receptor (EGFR) inhibitor panitumumab on cell lines expressing wild-type Kirsten-Ras (K-Ras) and oncogenic K-Ras mutations [70]. Larion et al. inves tigated the drug response of FK866, an inhibitor of NAD+ salvage pathway, with both a fibrosarcoma cell line and mouse models [71]. The anti-cancer drug doxorubicin was studied by Farhane et al. [72] and Zhang et al. [73] to characterize its interaction with cancer cells. Note that Raman-based techniques could be used in combination with other techniques to be capable of conducting rapid drug screening and discovery. Wen et al. combined results from Raman spectroscopy with mass spectrometry, which is the gold standard in metabolomics, and characterized breast cancer responders and nonresponders to small molecule inhibitors [69].

Intracellular drug distribution and metabolism are traditionally visualized by fluorescent-labeled drug molecules. Despite the molecular specificity, fluorescent labels are often much larger than the drug molecules themselves and could largely alter the drug pharmacokinetic activities. Raman imaging offers new possibilities for label-free drug imaging with subcellular spatial resolution. Aljakouch et al. reported the intracellular spatial distribution and metabolism of neratinib, a tyrosine kinase inhibitor with antitumor property, in different cancer cells, using label-free Raman imaging [75]. Using the intrinsic CN bond in neratinib, which generates a Raman band at 2208 cm-1 in the silent region, the authors generated label-free images of neratinib distribution in cancer cells (Figure 5). A study by El-Mashtoly et al. used Raman microscopy to show the spatial distribution of the molecular-targeted drug erlotinib within the cell and that erlotinib was metabolized within cells to its demethylated derivative [76]. Recently, the advance of SRS microscopy enabled ultra-rapid images of cells and subcellular distribution of drugs. Fu et al. reported SRS visualization and quantification of two tyrosine kinase inhibitor drugs (imatinib and nilotinib), as well as the process of drug uptake into lysosomes [77]. Visualization of other drugs including ponatinib and retinol was also reported by SRS microscopy [15,78].

![](images/83e3cbc99cf435b197f514570a9e07f400bfa0e4559967faacecb426f87983b1.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a blue-stained biological sample with 6 μm scale bar, labeled 'A' in top-left corner (no other text or symbols)
</details>

![](images/3b59f42449476c6b0027a3ca7883e8beed0169fd8dad03d3751da794940d3ded.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-stained cellular structures against a black background (no text or symbols)
</details>

![](images/b874aa012a5cdd71f2fe62d13be09b3f28e60fd838e20f64f1d13d73efa7b1c5.jpg)

<details>
<summary>natural_image</summary>

Fluorescently stained biological cell structure with blue and pink regions (no text or symbols)
</details>

![](images/de009566858deb75c517c20ee894e08df4da7fe88b4436c2989ff5fb1e45a12a.jpg)

<details>
<summary>natural_image</summary>

Color-coded abstract shape with no visible text or symbols
</details>

![](images/58b5b2f55d1d5a98e223aa2861416e93cd701f52d0e8fe183d9e7908060d326d.jpg)

![](images/30979eff137df13bd3f19cf4711e0a55ed29a02eb2d748ea28ec6409f53eac31.jpg)

![](images/c07eabee177a50e994f19fd06208cdaacfbb7a63350ae589ab7424a0efaace89.jpg)

![](images/57d92107943f17601d0ef0b641930a4bf49dbb705c55bd40a90de93f9be535d4.jpg)  
Figure 5. Raman imaging of SK-BR-3 cells treated with 5 µM neratinib for 8 h. Raman images reconstructed from the CH deformation (A) and CN stretching (B) intensities. (C) Overlay of Panels A and B. (E–G) Cross-section of Raman images of the same cell measured along the x–z axis. Scanning positions are indicated by the white line in Panel A. (D,H) HCA results based on the Raman data shown in Panels A and E. Reprinted with permission from reference [75].

Besides chemotherapy, radiotherapy is the mainstay of the treatment for a range of types of cancer. Monitoring radiation-induced cellular response of cancer at both cell and tissue levels was studied by Raman spectroscopy [79–83]. Roman et al. reported a change in the lipid composition and concentration in prostate cancer cells after X-ray radiation [80]. Similarly, metabolic alterations of cancer cells after radiation were also seen in nasopharyngeal cancer [79], non-small lung cancer [83], and glioblastoma [82]. A study by Milligan et al. found different biochemical responses between radio-resistant and radio-sensitive cell types in lung (H460), breast (MCF7), and prostate (LNCaP) cells [81]. The main differences were found in glycogen, phosphatidylcholine, glucose, arginine, and asparagine based on restricted non-negative matrix factorization approach.

## 3.4. Potential Applications in Clinical Cancer Diagnosis

Noninvasive or minimally invasive in vivo tools that can provide rapid tissue assessment have potential application in clinical diagnosis of cancer. With many advantageous features of Raman spectroscopic methods (non-destructive, capable of deep penetration and high resolution, and chemical specificity), here, we discuss their potential in tissue imaging and potential clinical diagnosis. We also direct readers to a few more reviews on applications of Raman spectroscopy in cancer diagnosis [84–86].

A recent work by Contorno et al. compiled data from 41 papers aiming at characteriz ing breast cancer by using various modalities of Raman spectroscopy [87]. They identified aromatic amino acids as the most prominent biomarker for identifying cancerous breast tissues from their healthy counterparts. Cancer cells and tissues exhibited markedly higher expression of aromatic amino acids, specifically tryptophan, phenylalanine, and tyrosine. A study by Haka et al. acquired Raman spectra from ex vivo samples of human breast tissue (normal, fibrocystic change, fibroadenoma, and infiltrating carcinoma) from 58 patients [88]. The study reported an increase in collagen in all abnormal breast tissues and less fat content in the samples diagnosed as fibroadenoma than those diagnosed as infiltrating carcinoma. By using the different fit coefficients for fat and collagen, the authors demonstrated a Raman diagnostic algorithm illustrating 94% sensitivity, 96% specificity, and 86% overall accuracy for detecting infiltrating carcinoma. A range of other studies also demonstrated the potential of Raman spectroscopy in diagnosing breast cancer in human and mouse breast tissues [89–96]. By exploiting the fingerprint region of the Raman spectrum and various machine learning techniques, Raman spectroscopy showed diagnostic potential for distinguishing cancerous tissues from normal tissues in brain cancer [56,97–100], skin cancer [42,101–105], gastrointestinal cancer [106–109], and lung cancer [110,111].

The ability of CRS for generating rapid chemical images makes it ideal for tissue and whole organ imaging and subsequently localizing the tumor margins. Ji et al. reported the use of SRS imaging for differentiating healthy human and mouse brain tissues from tumor infiltrated brain tissues [53]. They demonstrated that these label-free histopathological images provided very similar results to those obtained by conventional hematoxylin & eosin (H&E) staining, providing intrinsic chemical information without the need of routine tissue processing. The authors further applied SRS microscopy to obtain in vivo mouse brain images during tumor resection surgery, to reveal tumor margins that were undetectable under standard operative conditions. Through SRS microscopy, Freudiger et al. generated multi-color images of lipids, proteins, and hemoglobin in fresh-frozen tissue sections from mice models of invasive glioma, breast cancer metastases, stroke, and demyelination A good correlation between SRS and H&E microscopy was also shown. These findings suggest that SRS microscopy can generate high-quality histological images for clinical diagnosis without the need for tissue fixation, sectioning, or staining. Noteworthy, with the recent advances of CARS and SRS endoscopy [112–114], further improvements to these Raman-based systems would open up exciting possibilities for in vivo, label-free, and non-invasive histopathological imaging and clinical diagnostics in the near future.

## 4. You Are What You Eat—Stable Isotope Probing (SIP)

The introduction of stable isotope probing to Raman spectroscopy was first demonstrated in bacteria [115], which was later referred as Raman–SIP technology [116]. Huang et al. showed that the incorporation of ‘heavy’ $^ { 1 3 } \mathrm { C }$ stable isotope into cells causes significant shifts of some Raman bands in single cell Raman spectra (SCRS) [115]. Later it was found that other stable isotopes D (2H) and $^ { 1 5 } \mathrm { N }$ also generated Raman shifts in SCRS at different positions [117]. Following those discoveries, Raman–SIP are found applicable to many biological models including cancer cells, revealing the metabolic activity of cancer.

Stable isotope labeling by amino acids in cell culture (SILAC) has become increasingly popular for accurate protein quantitation, by using isotopically labeled amino acids that are later metabolically incorporated into cells [118]. In cancer research, SILAC was also recognized as an important tool for metabolic profiling of cancer cells, with respect to their environments [119,120]. Techniques like SILAC are stable isotope probing (SIP) methods that involve exposing cells to isotopically labeled substrates that are consequently assimilated into cells that are actively involved in specific metabolic processes. Molecular analysis of the labeled biomarkers thereby reveals functional information about the cell responsible for the metabolism of a particular substrate.

SIP to study cell metabolism, in general, shows great advantages over other specific probes that have larger molecular weights, and can disturb the intrinsic metabolic activity of cells. Using isotopes that mimic their naturally abundant counterparts does not alter the natural substrate pool. Among all SIP techniques, Raman spectroscopy has its unique strengths. While modalities like isotope ratio mass spectrometry and NMR spectroscopy require at least 300,000 cells, Raman spectroscopy or secondary ion mass spectrometry (SIMS) coupled with SIP enables an analysis of cell functions at a single-cell level [121] However, SIMS is limited by its destructive nature and expensive equipment. Raman spectroscopy exceeds other techniques in its non-destructive, sensitive, and relatively cheap nature. While a Raman spectrum already conveys intrinsic and phenotypic information, more insight into cell functions can be obtained by combining Raman micro-spectroscopy with SIP, using D $( ^ { 2 } \mathrm { H } ) , ^ { 1 3 } \mathrm { C } ,$ and $^ { 1 5 } \mathrm { N }$ -containing substrates to replace their primordial isotopes $( ^ { 1 2 } { \cal C } , ^ { \mathrm { 1 4 } } \mathrm { N } ,$ and 1H) [116]. Among those stable isotopes, D (2H) and $^ { 1 3 } \mathrm { C }$ are mostly commonly used due to the stronger C–H bond strength. Heteroatomic X–H bonds such as O–H, N–H, and S–H can be exchanged from nonenzymatic reactions, while C–H bond formation depends solely on enzyme-catalyzed chemical reactions that occurred within the metabolic pathways [122]. This provides unique advantages of D (2H) and $^ { 1 3 } \mathrm { C }$ for probing the biological metabolism. Providing a wide variety of possible isotopic substrates, Raman–SIP probe the metabolism of most biomolecular constituents of a cell, including proteins, lipids, carbohydrates, and nucleic acids, revealing both molecule-specific and general metabolisms, as well as drug–cancer interactions (Figure 6).

${ } ^ { 2 } \mathsf { H } / { } ^ { 1 3 } \mathsf { C } / { } ^ { 1 5 } \mathsf { N } / { } ^ { 1 8 } \mathsf { O }$ Stable Isotope Probes Raman Labelling Applications for Cell Metabolism  
![](images/a722c5fa46142724ff5d1153f29d92e3a7dec4a23d4f2cedd9cff2bc945a4ee6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["D2O"] --> B["Oxidation"]
  B --> C["NADPH + H+"]
  C --> D["Reduction"]
  D --> E["H-C-C-D"]
  E --> F["D2O ⇌ D+ + OD-"]
  G["Drugs"] --> H["Metformin"]
  G --> I["Phenformin"]
  J["Protein Metabolism"] --> K["Tyrosine"]
  J --> L["Serine"]
  J --> M["Glutamine"]
  J --> N["Phenylalanine"]
  O["Nucleus Area(DNA/RNA)"] --> P["Cytidine"]
  O --> Q["Thymidine"]
  O --> R["Uridine"]
  S["Lipid Metabolism"] --> T["Cholesterol"]
  S --> U["Desmosterol"]
  S --> V["Arachidonic acid"]
  S --> W["Phosphatidylinositol"]
  X["Energy Metabolism"] --> Y["Glucose"]
  X --> Z["Glycogen"]
  AA["Mitochondria Mapping"] --> AB["Cytochrome C"]
```
</details>

Figure 6. Raman–SIP strategies to study cellular metabolism. Heavy water $( \mathrm { D } _ { 2 } \mathrm { O } )$ is involved in NADPH regeneration, which is able to indicate the general anabolism activity in cells. Stable isotope labeled sugars, amino acids, nucleic acids, lipid precursors, and drugs can be used to probe the dynamics of metabolic flux and interactions of drugs and cancer cells.

Although Raman–SIP is now a mature tool to study cell ecology and biology, its application in cancer research is new. Most applications demonstrate the capability of the technique rather than answer specific questions. One of this review’s purposes is to introduce Raman–SIP to a broader community and share our perspectives on its potential for studying cancer metabolism.

## 4.1. Principles of Raman–SIP

As Raman spectroscopy considers changes in vibrational modes of molecules, a me chanical model can be used to consider a molecular vibration as a spring model. A classical ‘two-balls-on-a-spring’ approach provides an equivalence of a diatomic molecule with two atoms with masses m and m connected by a chemical bond. The vibrational frequency υ of such a molecule is described as:

$$
v = \frac {1}{2 \pi c} \sqrt {\frac {k}{\mu}}
$$

where c is the speed of light, k is the force constant of the spring (diatomic bond), and $\mu$ is the reduced mass given by:

$$
\mu = \frac {m _ {1} m _ {2}}{m _ {1} + m _ {2}}
$$

. Therefore, the vibrational frequency υ is inversely proportional to the square root of the reduced mass $\mu .$ When an atom is replaced by its heavier isotope, µ increases, therefore, υ decreases. Taking C–D replacement of C–H as an example, if the 1H atom is replaced by the $^ 2 \mathrm { D }$ atom, $\mu$ almost doubles and the ratio of the new υ to the old υ is 1.36. Therefore, C–D vibrations usually appear in the silent zone of a Raman spectrum at around 2100–2200 cm $^ { - 1 } ,$ red-shifted from the C–H vibrations at 2800–3000 cm−1. Thus, a strategy to quantify D incorporation is to calculate the percentage of the integrated C–D band area to the sum of the areas of the C–D and C–H bands:

$$
D _ {\text {incorp}} = \frac {\text {Area} _ {C - D}}{\text {Area} _ {C - D} + \text {Area} _ {C - H}}
$$

. Redshifts of Raman bands can also be observed when replacing ${ } ^ { 1 2 } \mathrm { C } , { } ^ { 1 4 } \mathrm { N } , { } ^ { 1 8 } \mathrm { O } , \mathrm { o r } { } ^ { 3 2 } \mathrm { S }$ with their heavier analogs. Compared with the C–D shifts, the extent of the redshift is considerably less dramatic in the $^ { 1 3 } C$ and $^ { 1 5 } \mathrm { N }$ substitutions, due to the comparably low changes in µ. By feeding cells with isotope-labeled substrates, the active cells metabolize these substrates and the isotopic-dependent shifts in Raman spectra can be used as indicators of isotopic incorporation, thereby ‘you are what you eat’.

## 4.2. Raman–SIP Monitors Intracellular Metabolic Activities

Raman spectroscopy combined with isotopically labeled molecules is used to study the specific metabolic features of cell constituents such as lipids, proteins, and nucleic acids (Figure 6). Table 2 summarizes a collection of studies using Raman–SIP approaches to study cell metabolism and behaviors, together with their choices of probes, targeted molecules, and platform of research.

Table 2. Studies using Raman–SIP to probe metabolism in mammalian cells. “Spont.” refers to spontaneous Raman.

<table><tr><td>Case Studies</td><td>Spont.</td><td>CRS</td><td>Isotope</td><td>Substrate</td><td>Target</td><td>Platform</td></tr><tr><td>Matthäus, C. et al. (2012) [123]</td><td>√</td><td></td><td>D</td><td>d31-palmitic acid d33-oleic acid</td><td>Lipids</td><td>THP-1 monocytes</td></tr><tr><td>Stiebing, C. et al. (2014) [124]</td><td>√</td><td></td><td>D</td><td>d8-arachidonic acid 31-palmitic acid 6-cholesterol-2,2,3,4,4,6</td><td>Lipids</td><td>Human macrophages</td></tr><tr><td>Stiebing, C. et al. (2017) [125]</td><td>√</td><td>√</td><td>D</td><td>d31-palmitic acid</td><td>Lipids</td><td>Human macrophages</td></tr><tr><td>Majzner, K. et al. (2018) [126]</td><td>√</td><td></td><td>D</td><td>d8-arachidonic acid</td><td>Lipids</td><td>Endothelial cell line (HMEC-1)</td></tr><tr><td>Li, J. &amp; Cheng, J.-X. (2015) [127]</td><td>√</td><td>√</td><td>D</td><td>d7-glucosed 5-glutamin 31-palmitic acid-d31</td><td>Lipids</td><td>PANC1, A549, MIA PaCa2, MCF7, LNCaP, PC3, HPDE6 and RWPE1 cell lines</td></tr><tr><td>García, A. et al. (2015) [128]</td><td>√</td><td>√</td><td>D</td><td>d38-cholesterol</td><td>Lipids</td><td>Y1 cell line</td></tr><tr><td>Weeks, T. J. et al. (2011) [129]</td><td></td><td>√</td><td>D</td><td>d2-oleic Acid-9,10</td><td>Lipids</td><td>Human monocytes</td></tr><tr><td>Du, J. et al. (2020) [43]</td><td>√</td><td>√</td><td>D</td><td>d7-glucose 31-palmitic acid 35-stearic acid d33-oleic acid&gt;</td><td>Lipids</td><td>Patient-derived melanoma cell lines</td></tr><tr><td>Dodo, K. et al. (2021) [130]</td><td>√</td><td></td><td>D</td><td>d-γ-Linolenic acid</td><td>γ-Linolenic acid metabolism and cytotoxicity</td><td>WI-38 cell line and VA-13 tumor cell line</td></tr><tr><td>Matthäus, C. et al. (2008) [131]</td><td>√</td><td></td><td>D</td><td>1,2-Distearoyl-d70-sn-glycero3-phosphocholine (DSPC-d70)</td><td>Liposomal Drug Carrier Systems</td><td>MCF-7 cell line</td></tr><tr><td>Van Manen, H.-J. et al. (2008) [132]</td><td>√</td><td></td><td>D</td><td>d5-phenylalanine d4-tyrosine d3-methoine</td><td>Proteins</td><td>HeLa cell line</td></tr><tr><td>Wei, L. et al. (2013) [133]</td><td>√</td><td>√</td><td>D</td><td>d10-leucine</td><td>Newly synthesized proteins</td><td>Live HeLa cell line Human embryonic kidney HEK293T cell line Neuron-like neuroblastoma mouse N2A cell line</td></tr><tr><td>Wei, L. et al. (2015) [134]</td><td>√</td><td>√</td><td>D</td><td>deuterated amino acids</td><td>Proteins</td><td>HeLa cell line</td></tr><tr><td>Shen, Y. et al. (2014) [135]</td><td>√</td><td>√</td><td> $^{13}C$ </td><td> $^{13}C$ -phenylalanine</td><td>Protein degradation</td><td>HeLa, HEK293T and PC12 cell lines</td></tr></table>

Table 2. Cont.

<table><tr><td>Case Studies</td><td>Spont.</td><td>CRS</td><td>Isotope</td><td>Substrate</td><td>Target</td><td>Platform</td></tr><tr><td>Miao, K. &amp; Wei, L. (2020) [136]</td><td></td><td>√</td><td>D</td><td>d5-glutamine</td><td>Proteins</td><td>HeLa cell line</td></tr><tr><td>Zhang, L. et al. (2019) [137]</td><td>√</td><td>√</td><td>D</td><td>d12-glucose</td><td>Glucose metabolism</td><td>PC3, HeLa, MCF7, RWPE-1 and U87MG cell linesMouse model</td></tr><tr><td>Lee, D. et al. (2020) [138]</td><td>√</td><td>√</td><td>D</td><td>d7-glucose</td><td>Glucose metabolism; glycogen synthesis</td><td>U87 and HeLa cell lines</td></tr><tr><td>Hu, F. et al. (2015) [139]</td><td>√</td><td>√</td><td>D</td><td>3-O-propargyl-D-glucose</td><td>Glucose metabolism</td><td>HeLa cell line U-87 MG tumor xenograft tissue</td></tr><tr><td>Long, R. et al. (2018) [140]</td><td>√</td><td>√</td><td> $D/^{13}C$ </td><td> $^{13}C$ -3-O-propargyl-D-glucose</td><td>Glucose metabolism</td><td>U87 MG, PC-3, COS-7 and RWPE-1 cell lines</td></tr><tr><td>Chen, Z. et al. (2014) [141]</td><td>√</td><td>√</td><td> $^{13}C$ </td><td> $^{13}C$  isotopologues of EdU</td><td>DNA</td><td>HeLa cell lines</td></tr><tr><td>Zhang, L. &amp; Min, W. (2017) [142]</td><td>√</td><td>√</td><td>D</td><td>d-amino acidsd31-palmitate acidd7-glucose</td><td>Lipids and proteins</td><td>MCF-7 cell lines</td></tr><tr><td>Shi, L. et al. (2018) [143]</td><td>√</td><td>√</td><td>D</td><td> $D_2O$ </td><td>Lipids, proteins and DNA</td><td>HeLa, COS-7, and U-87 MG cell lines Zebrafish embryos Mouse model</td></tr><tr><td>Hekmatara, M. et al. (2021) [144]</td><td>√</td><td></td><td>D</td><td> $D_2O$ </td><td>Lipids, proteins and DNA</td><td>MCF-7 cell line</td></tr></table>

There is increasing evidence of upregulated demand for fatty acids in cancer cells, compared to their non-malignant counterparts [30]. Lipid uptake, distribution, and metabolism was extensively studied using Raman–SIP approach with labeled fatty acids in various types of cells [123–129]. D-labeled free fatty acids such as d -palmitic acid, d - oleic acid, and d -palmitic acid were used to image lipid metabolism in human macrophages [123–125]. Intracellular cholesterol storage can also be observed in cells by using d -cholesterol [128]. Heterogeneous distributions of neutral lipid species were found, where some lipid droplets accumulated preferentially unesterified cholesterol, whereas others stored cholesteryl esters.

De novo lipogenesis in cells can also be studied using deuterated carbon sources such as deuterated glucose or glutamine. Li and Cheng were the first to visualize the direct de novo lipid synthesis that originated from deuterated glucose through SRS imaging [127] (Figure 7A and 7B). They observed that glucose was largely utilized for lipid synthesis in pancreatic cancer cells, which occurred at a much lower rate in immortalized normal pancreatic epithelial cells. Similarly, de novo synthesis of fatty acids was also studied in undifferentiated and differentiated melanoma cell lines using deuterated glucose with spontaneous Raman spectroscopy and SRS [43]. In combination with transcriptomics analysis, the authors identified the fatty acid synthesis pathway as a druggable susceptibility for differentiated melanocytic cells.

Tumor-selective cytotoxicity of particular fatty acids was also studied. Dodo et al. synthesized several deuterated γ-linolenic acids and evaluated their metabolism and cytotoxicity towards normal human fibroblast WI-38 cells and VA-13 tumor cells [130]. Through Raman imaging of intracellular lipid droplets, they suggested the tumor-selective cytotoxicity of γ-linolenic acids from itself, as opposed to its oxidized metabolites.

![](images/6aeb94e7e00ec921f219de15ebe27333825c1cdd216d621dd2ff79217b6bb9d7.jpg)  
Figure 7. SRS imaging of cancer cells from deuterated glucose (A,B). Glucose-d -incubated pancreatic cancer PANC1 cells were treated without or with 10% FBS for 3 days. SRS imaging at C–D and C–H vibration were taken and the ratio of C–D/C–H was used to analyze the level of de novo lipogenesis and increased lipogenesis. Reprinted and adapted with permission from reference [127]. (C) SRS images of a glucose-d7-labelled mitotic HeLa cell before and after unmixing, showing distribution of DNA, lipids, and proteins. Reprinted and adapted with permission from Reference [137].

Cancer cells exhibit significant metabolic alterations with respect to their primary energy sources, including glucose. Deuterated glucose in Raman–SIP are shown to be valuable for the evaluation and exploration of glucose metabolism in cancer cells. Zhang et al. generated a comprehensive study to visualize the metabolic dynamics of macromolecules, such as DNA, protein, lipids, and glycogen, from glucose, in various cancer cell lines, and a mouse model with glioblastoma xenograft [137] (Figure 7C). The pathway from glucose to glycogen, which is important glucose storage in cancer cells, was also investigated by subcellular visualization of deuterated glycogen from deuterated glucose [138]. Hu et al. developed a protocol for synthesizing deuterated glucose with an alkyne tag, 3-O-propargyl-D-glucose [139]. By using this tag that shows a distinctive Raman band at 2129 cm-1, they quantified the glucose uptake and found different metabolic activities in different cancer cell types. Long et al. further developed this approach to add a second 13C labeling to synthesize 13C-3-O-propargyl-D-glucose [140]. Thus, they demon strated two-color imaging of glucose uptake and incorporation activity in U-87 MG human glioblastoma cells, PC-3 human prostate cancer cells, COS-7 monkey kidney cells, and RWPE-1 human prostate normal cells, as well as in ex vivo mouse brain tissues.

Just as in SILAC, protein synthesis could be observed in Raman–SIP through the incorporation of isotopically labeled amino acids. Back in 2008, van Manen et al. demonstrated the incorporation of deuterated phenylalanine, tyrosine, and methionine into proteins in single HeLa cells, also observed by the C–D vibrations in the 2100–2300 cm-1 spectral region [132]. It was shown that Raman images could be generated by illustrating newly synthesized proteins from deuterated amino acids, in a range of live mammalian cells with high spatial–temporal resolution [133]. Using this approach, subcellular compartments could be identified, revealing fast protein turnover in HeLa and HEK293T cells, and newly grown neurites in differentiating neuron-like N2A cells. Metabolic changes of proteins and lipids were also studied in cancer cells during epithelial–mesenchymal transition [142] Compared with approaches like SILAC or fluorescence, this approach with Raman–SIP could examine the proteome of a cell in a spatially resolved, non-destructive manner on living single cells with only minor modifications [145]. This approach could also be used to study protein degradation using $^ { 1 3 } \mathrm { C }$ labelled amino acids [134,135].

Compared with lipid and protein metabolism, there are fewer studies utilizing Raman– SIP approach to study DNA synthesis. Apart from newly synthesized DNA observed from deuterated glucose metabolism, EdU as an analog of thymidine was exclusively used as a DNA metabolic tag, which was incorporated into cellular biomass during cell division [146]. Chen et al. synthesized various designs of $^ { 1 3 } \mathrm { C }$ isotopologues of EdU and demonstrated three-color chemical imaging of nascent DNA, RNA, and newly synthesized fatty-acid in live HeLa cells.

## 4.3. Raman–SIP with $D _ { 2 } O$ Measures General Metabolic Activity

Apart from specifically labeled precursors of cellular constituents, heavy water $( \mathrm { D } _ { 2 } \mathrm { O } )$ is suggested to be a unique and universal tool to monitor the synthesis of biomolecules on a global scale. As an isotopologue of water, $\mathrm { D } _ { 2 } \mathrm { O }$ can rapidly and freely equilibrate with the total body water inside a cell, and D atoms can exchange with the H atoms to form a variety of X–D bonds. Different from the often non-enzymatic reactions to form heteroatomic X–D bonds, such as O–D, N–D, and S–D, the C–D bond formation depends solely on enzyme-catalyzed chemical reactions, due to the stronger C–H bond strength [122]. In C– H/C–D exchanges, D atoms from $\mathrm { D } _ { 2 } \mathrm { O }$ are rapidly incorporated into metabolic precursors of different classes of biomolecules such as deoxyribose, acetyl-CoA/NADPH, amino acids, and phosphoenolpyruvate (PEP) (Figure 8). These precursors with D labeling are then slowly incorporated into their final products, which are nucleic acids, lipids, proteins, and carbohydrates. Therefore, $_ { \mathrm { D _ { 2 } O } }$ serves as an ideal agent to probe general metabolic activities through the emergence of a variety of D-labelled macromolecules.

![](images/11cfcd83f206c3cfbc7a10b5601dffd7409841f7c1782fe19f3518ab5400dbd0.jpg)

<details>
<summary>chemical</summary>

Chemical reaction pathway for D₂O degradation using fast enzyme enzymes and polymerization, showing intermediates and products like D-DNA/D-RNA and D-Lipids.
</details>

Figure 8. $_ { \mathrm { D _ { 2 } O } }$ as a unique and universal tracer for different biomolecules. ‘rds’ stands for rate determining step.

Raman–SIP using $\mathrm { D } _ { 2 } \mathrm { O }$ was demonstrated to measure the general metabolic activities of single microbial cells, first reported by Berry et al. [117]. By incubating microbes with $\mathrm { D } _ { 2 } \mathrm { O } _ { \ l }$ , physiologically active cells could be rapidly and sensitively identified with Raman, by measuring the C–D peak at 2170–2300 cm−1. The metabolic activity could then be semi-quantified and compared by measuring the degree of D incorporation. This approach was extensively applied to study microbial activity and ecology [116,121,147–154]. Recently, it also generated an impact in the area of metabolic studies of animal cells.

Shi et al. demonstrated SRS imaging based on $_ { \mathrm { D _ { 2 } O } }$ in various animal models, achieving dynamic visualization of proteins, lipids, and DNA [143]. Based on the fact that tumor cells show inherently higher metabolic activities than normal cells, the study was able to visualize the boundaries between tumors and the surrounding normal tissues. The distribu tion of intratumor heterogeneity was also observed, which is considered a driver of tumor aggressiveness. In this study, the authors also suggested that $\mathrm { D } _ { 2 } \mathrm { O }$ is a better probe than deuterium-labeled carbon substrates. For visualizing lipogenic activities, $_ { \mathrm { D _ { 2 } O } }$ is better than deuterated fatty acids, as well as deuterated glucose, which at high concentrations, could potentially create hyperglycemia and might be less efficient in labeling newly synthesized lipids. In addition, $_ { \mathrm { D _ { 2 } O } }$ is cost-effective, as compared to other Raman–SIP probes and is uni versal in probing a range of metabolic activities simultaneously. Most recently, Hekmatara et al. applied Raman–SIP with $_ { \mathrm { D } _ { 2 } \mathrm { O } }$ to study anticancer drug response of MCF-7 cells [144]. They discovered high subcellular activities of cancer cells after high-dosage rapamycin exposure at the single-cell level, which was masked in a population-wise cytotoxicity test.

Although Raman–SIP application in cancer research using heavy water is just coming of age, recent studies exhibit its great potential in metabolic studies, as it is non-invasive, cost-effective, easily accessible, and universally applicable. It can be adapted to a broad range of model systems and cancer research areas to study cancer development, tissue homeostasis, tumor heterogeneity, cancer drug response, and pharmacokinetics. It would be of particular value in diagnosis at surgery, categorizing cancers by their metabolic status, evaluating new drugs, their uptake and metabolism, their antitumor effects, resistance mechanisms, and responses. Characterizing the changes in stroma at the local and distant sites and in premalignant disease, is likely to provide new insights into cancer development.

## 5. Conclusions and Outlook

Raman spectroscopy technologies, from comprehensive spectroscopy to advanced imaging, offer exciting new possibilities in cancer research. In this review, we summarize a wide range of applications using Raman and Raman–SIP techniques to investigate metabolism in cancer cells and tissues. Offering intrinsic biochemical information and subcellular spatial resolution, the Raman profile of a cancer cell or tissue is an excellent metabolic indicator and an indicator of phenotypic heterogeneity. It can help uncover the molecular basis of the disease and provide comprehensive, objective, and quantifiable molecular information for diagnosis and treatment evaluation.

Looking into the future, the potential of Raman spectroscopy and imaging in cancer research could be further exploited. Critical improvements and advances are still under development. Raman databases of more metabolites, potentially comparable to a mass spectrometry database, can cover identification of more metabolites. Advanced chemo metric algorithms and machine-learning methods can improve and accelerate current spectral processing and data interpretation, especially in a large, high-dimensional clinical dataset. Instrumentation engineering of advanced fiber optics, detectors, and handheld spectrometer would render Raman tools accessible for clinical translation.

Author Contributions: W.E.H., A.L.H. and $\operatorname { J . - X . C . }$ conceived and designed the study. J.X. and T.Y. performed the systematic review of the literature and wrote the manuscript. C.E.Z. and Y.T. conducted critical review of the study. All authors contributed to interpreting the data, revised the work, and approved the final version of the manuscript.

Funding: W.E.H. acknowledges finance and instrumentation support from EPSRC (EP/M002403/1, EP/M02833X/1) and NERC (NE/M002934/1).

Institutional Review Board Statement: Not applicable.

Acknowledgments: We thank Shanghai D-band Medical Instrument Co, Shanghai China for providing spontaneous Raman images and constructive discussion. J.X. and W.E.H. thank the Suzhou Institute of Biomedical Engineering and Technology, Chinese Academy of Sciences for financial support. A.L.H. and C.Z. thank the Breast Cancer Research Foundation for support.

Conflicts of Interest: The authors declare no conflict of interest.

## References

1. Pavlova, N.N.; Thompson, C.B. The Emerging Hallmarks of Cancer Metabolism. Cell Metab. 2016, 23, 27–47. [CrossRef] [PubMed]  
2. Heiden, M.G.V.; Cantley, L.C.; Thompson, C.B. Understanding the Warburg effect: The metabolic requirements of cell proliferation. Science 2009, 324, 1029–1033. [CrossRef] [PubMed]  
3. DeBerardinis, R.J.; Chandel, N.S. Fundamentals of cancer metabolism. Sci. Adv. 2016, 2, e1600200. [CrossRef]  
4. Gerlinger, M.; Rowan, A.J.; Horswell, S.; Larkin, J.; Endesfelder, D.; Gronroos, E.; Martinez, P.; Matthews, N.; Stewart, A.; Tarpey, P.; et al. Intratumor Heterogeneity and Branched Evolution Revealed by Multiregion Sequencing. N. Engl. J. Med. 2012, 366, 883–892. [CrossRef]  
5. Thiele, C.; Wunderling, K.; Leyendecker, P. Multiplexed and single cell tracing of lipid metabolism. Nat. Methods 2019, 16, 1123–1130. [CrossRef]  
6. Duncan, K.D.; Fyrestam, J.; Lanekoff, I. Advances in mass spectrometry based single-cell metabolomics. Analyst 2019, 144, 782–793. [CrossRef] [PubMed]  
7. Zenobi, R. Single-Cell Metabolomics: Analytical and Biological Perspectives. Science 2013, 342, 1243259. [CrossRef]  
8. Chakraborty, A.; Ghosh, A.; Barui, A. Advances in surface-enhanced Raman spectroscopy for cancer diagnosis and staging. J. Raman Spectrosc. 2020, 51, 7–36. [CrossRef]  
9. Cialla-May, D.; Zheng, X.-S.; Weber, K.; Popp, J. Recent progress in surface-enhanced Raman spectroscopy for biological and biomedical applications: From cells to clinics. Chem. Soc. Rev. 2017, 46, 3945–3961. [CrossRef]  
10. Guerrini, L.; Alvarez-Puebla, R.A. Surface-Enhanced Raman Spectroscopy in Cancer Diagnosis, Prognosis and Monitoring. Cancers 2019, 11, 748. [CrossRef] [PubMed]  
11. Krafft, C.; Schie, I.W.; Meyer, T.; Schmitt, M.; Popp, J. Developments in spontaneous and coherent Raman scattering microscopic imaging for biomedical applications. Chem. Soc. Rev. 2015, 45, 1819–1849. [CrossRef] [PubMed]  
12. Raman, C.V.; Krishnan, K.S. A New Type of Secondary Radiation. Nat. Cell Biol. 1928, 121, 501–502. [CrossRef]  
13. Thorn, K. Genetically encoded fluorescent tags. Mol. Biol. Cell 2017, 28, 848–857. [CrossRef] [PubMed]  
14. Zhang, Y.; Hong, H.; Cai, W. Imaging with Raman Spectroscopy. Curr. Pharm. Biotechnol. 2010, 11, 654–661. [CrossRef]  
15. Liao, C.-S.; Slipchenko, M.N.; Wang, P.; Li, J.; Lee, S.-Y.; Oglesbee, R.A.; Cheng, J.-X. Microsecond scale vibrational spectroscopic imaging by multiplex stimulated Raman scattering microscopy. Light. Sci. Appl. 2015, 4, e265. [CrossRef] [PubMed]  
16. Liao, C.-S.; Huang, K.-C.; Hong, W.; Chen, A.J.; Karanja, C.; Wang, P.; Eakins, G.; Cheng, J.-X. Stimulated Raman spectroscopic imaging by microsecond delay-line tuning. Optica 2016, 3, 1377–1380. [CrossRef]  
17. Lin, H.; Lee, H.J.; Tague, N.; Lugagne, J.-B.; Zong, C.; Deng, F.; Shin, J.; Tian, L.; Wong, W.; Dunlop, M.J.; et al. Microsec ond Fingerprint Stimulated Raman Spectroscopic Imaging by Ultrafast Tuning and Spatial-Spectral Learning. arXiv 2020, arXiv:2003.02224.  
18. Cheng, J.X.; Xie, X.S. (Eds.) Coherent Raman Scattering Microscopy; CRC Press, Taylor & Francis Group: Boca Raton, FL, USA, 2013.  
19. Liao, C.-S.; Cheng, J.-X. In Situ and In Vivo Molecular Analysis by Coherent Raman Scattering Microscopy. Annu. Rev. Anal. Chem. 2016, 9, 69–93. [CrossRef]  
20. Marangoni, M.; Gambetta, A.; Manzoni, C.; Kumar, V.; Ramponi, R.; Cerullo, G. Fiber-format CARS spectroscopy by spectral compression of femtosecond pulses from a single laser oscillator. Opt. Lett. 2009, 34, 3262–3264. [CrossRef]  
21. Zhang, C.; Zhang, D.; Cheng, J.-X. Coherent Raman Scattering Microscopy in Biology and Medicine. Annu. Rev. Biomed. Eng. 2015, 17, 415–445. [CrossRef]  
22. Palonpon, A.F.; Ando, J.; Yamakoshi, H.; Dodo, K.; Sodeoka, M.; Kawata, S.; Fujita, K. Raman and SERS microscopy for molecular imaging of live cells. Nat. Protoc. 2013, 8, 677–692. [CrossRef] [PubMed]  
23. O’Malley, J.; Kumar, R.; Kuzmin, A.N.; Pliss, A.; Yadav, N.; Balachandar, S.; Wang, J.; Attwood, K.; Prasad, P.N.; Chandra, D. Lipid quantification by Raman microspectroscopy as a potential biomarker in prostate cancer. Cancer Lett. 2017, 397, 52–60. [CrossRef] [PubMed]  
24. Lita, A.; Kuzmin, A.N.; Pliss, A.; Baev, A.; Rzhevskii, A.; Gilbert, M.R.; Larion, M.; Prasad, P.N. Toward Single-Organelle Lipidomics in Live Cells. Anal. Chem. 2019, 91, 11380–11387. [CrossRef] [PubMed]  
25. Kuzmin, A.N.; Levchenko, S.M.; Pliss, A.; Qu, J.; Prasad, P.N. Molecular profiling of single organelles for quantitative analysis of cellular heterogeneity. Sci. Rep. 2017, 7, 1–9. [CrossRef] [PubMed]  
26. Kuzmin, A.N.; Pliss, A.; Rzhevskii, A.; Lita, A.; Larion, M. BCAbox Algorithm Expands Capabilities of Raman Microscope for Single Organelles Assessment. Biosensors 2018, 8, 106. [CrossRef]  
27. Lita, A.; Pliss, A.; Kuzmin, A.; Yamasaki, T.; Zhang, L.; Dowdy, T.; Burks, C.; de Val, N.; Celiku, O.; Ruiz-Rodado, V.; et al. IDH1 mutations induce organelle defects via dysregulated phospholipids. Nat. Commun. 2021, 12, 1–16. [CrossRef]  
28. Zhang, D.; Wang, P.; Slipchenko, M.N.; Cheng, J.-X. Fast Vibrational Imaging of Single Cells and Tissues by Stimulated Raman Scattering Microscopy. Accounts Chem. Res. 2014, 47, 2282–2290. [CrossRef]  
29. Munir, R.; Lisec, J.; Swinnen, J.V.; Zaidi, N. Lipid metabolism in cancer cells under metabolic stress. Br. J. Cancer 2019, 120, 1090–1098. [CrossRef]  
30. Ackerman, D.; Simon, M.C. Hypoxia, lipids, and cancer: Surviving the harsh tumor microenvironment. Trends Cell Biol. 2014, 24, 472–478. [CrossRef]  
31. Zaidi, N.; Lupien, L.; Kuemmerle, N.B.; Kinlaw, W.B.; Swinnen, J.V.; Smans, K. Lipogenesis and lipolysis: The pathways exploited by the cancer cells to acquire fatty acids. Prog. Lipid Res. 2013, 52, 585–589. [CrossRef]  
32. Kuemmerle, N.B.; Rysman, E.; Lombardo, P.S.; Flanagan, A.J.; Lipe, B.C.; Wells, W.A.; Pettus, J.R.; Froehlich, H.M.; Memoli, V.A.; Morganelli, P.M.; et al. Lipoprotein Lipase Links Dietary Fat to Solid Tumor Cell Proliferation. Mol. Cancer Ther. 2011, 10, 427–436. [CrossRef] [PubMed]  
33. Menendez, J.A.; Lupu, R. Fatty acid synthase and the lipogenic phenotype in cancer pathogenesis. Nat. Rev. Cancer 2007, 7, 763–777. [CrossRef] [PubMed]  
34. Cha, J.-Y.; Lee, H.-J. Targeting Lipid Metabolic Reprogramming as Anticancer Therapeutics. J. Cancer Prev. 2016, 21, 209–215. [CrossRef]  
35. Abramczyk, H.; Brozek-Pluska, B. New look inside human breast ducts with Raman imaging. Raman candidates as diagnostic markers for breast cancer prognosis: Mammaglobin, palmitic acid and sphingomyelin. Anal. Chim. Acta 2016, 909, 91–100. [CrossRef]  
36. Abramczyk, H.; Surmacki, J.; Kope´c, M.; Olejnik, A.K.; Lubecka-Pietruszewska, K.; Fabianowska-Majewska, K. The role of lipid droplets and adipocytes in cancer. Raman imaging of cell cultures: MCF10A, MCF7, and MDA-MB-231 compared to adipocytes in cancerous human breast tissue. Analyst 2015, 140, 2224–2235. [CrossRef] [PubMed]  
37. Surmacki, J.; Brozek-Pluska, B.; Kordek, R.; Abramczyk, H. The lipid-reactive oxygen species phenotype of breast cancer. Raman spectroscopy and mapping, PCA and PLSDA for invasive ductal carcinoma and invasive lobular carcinoma. Molecular tumorigenic mechanisms beyond Warburg effect. Analyst 2015, 140, 2121–2133. [CrossRef] [PubMed]  
38. You, S.; Tu, H.; Zhao, Y.; Liu, Y.; Chaney, E.J.; Marjanovic, M.; Boppart, S.A. Raman Spectroscopic Analysis Reveals Abnormal Fatty Acid Composition in Tumor Micro- and Macroenvironments in Human Breast and Rat Mammary Cancer. Sci. Rep. 2016, 6, 32922. [CrossRef] [PubMed]  
39. Nieva, C.; Marro, M.; Santana-Codina, N.; Rao, S.; Petrov, D.; Sierra, A. The Lipid Phenotype of Breast Cancer Cells Characterized by Raman Microspectroscopy: Towards a Stratification of Malignancy. PLoS ONE 2012, 7, e46456. [CrossRef] [PubMed]  
40. Tirinato, L.; Liberale, C.; Di Franco, S.; Candeloro, P.; Benfante, A.; La Rocca, R.; Potze, L.; Marotta, R.; Ruffilli, R.; Rajamanickam, V.P.; et al. Lipid Droplets: A New Player in Colorectal Cancer Stem Cells Unveiled by Spectroscopic Imaging. Stem Cells 2015, 33, 35–44. [CrossRef] [PubMed]  
41. Le, T.T.; Huff, T.B.; Cheng, J.-X. Coherent anti-Stokes Raman scattering imaging of lipids in cancer metastasis. BMC Cancer 2009, 9, 42. [CrossRef]  
42. Gniadecka, M.; Philipsen, P.A.; Wessel, S.; Gniadecki, R.; Wulf, H.C.; Sigurdsson, S.; Nielsen, O.F.; Christensen, D.H.; Hercogova, J.; Rossen, K.; et al. Melanoma Diagnosis by Raman Spectroscopy and Neural Networks: Structure Alterations in Proteins and Lipids in Intact Cancer Tissue. J. Investig. Dermatol. 2004, 122, 443–449. [CrossRef] [PubMed]  
43. Du, J.; Su, Y.; Qian, C.; Yuan, D.; Miao, K.; Lee, D.; Ng, A.H.C.; Wijker, R.S.; Ribas, A.; Levine, R.D.; et al. Raman-guided subcellular pharmaco-metabolomics for metastatic melanoma cells. Nat. Commun. 2020, 11, 1–16. [CrossRef]  
44. Nan, X.; Cheng, J.-X.; Xie, X.S. Vibrational imaging of lipid droplets in live fibroblast cells with coherent anti-Stokes Raman scattering microscopy. J. Lipid Res. 2003, 44, 2202–2208. [CrossRef] [PubMed]  
45. Freudiger, C.W.; Min, W.; Saar, B.G.; Lu, S.; Holtom, G.R.; He, C.; Tsai, J.C.; Kang, J.X.; Xie, X.S. Label-Free Biomedical Imaging with High Sensitivity by Stimulated Raman Scattering Microscopy. Science 2008, 322, 1857–1861. [CrossRef] [PubMed]  
46. Slipchenko, M.N.; Le, T.T.; Chen, H.; Cheng, J.-X. High-Speed Vibrational Imaging and Spectral Analysis of Lipid Bodies by Compound Raman Microscopy. J. Phys. Chem. B 2009, 113, 7681–7686. [CrossRef]  
47. Mitra, R.; Chao, O.; Urasaki, Y.; Goodman, O.B.; Le, T.T. Detection of Lipid-Rich Prostate Circulating Tumour Cells with Coherent Anti-Stokes Raman Scattering Microscopy. BMC Cancer 2012, 12, 540. [CrossRef]  
48. Li, J.; Condello, S.; Thomes-Pepin, J.; Ma, X.; Xia, Y.; Hurley, T.D.; Matei, D.; Cheng, J.-X. Lipid Desaturation Is a Metabolic Marker and Therapeutic Target of Ovarian Cancer Stem Cells. Cell Stem Cell 2017, 20, 303–314. [CrossRef]  
Yan, S.; Cui, S.; Ke, K.; Zhao, B.; Liu, X.; Yue, S.; Wang, P. Hyperspectral Stimulated Raman Scattering Microscopy Unravels Aberrant Accumulation of Saturated Fat in Human Liver Cancer. Anal. Chem. 2018, 90, 6362–6366. [CrossRef] [PubMed]  
50. Zhang, C.; Li, J.; Lan, L.; Cheng, J.-X. Quantification of Lipid Metabolism in Living Cells through the Dynamics of Lipid Droplets Measured by Stimulated Raman Scattering Imaging. Anal. Chem. 2017, 89, 4502–4507. [CrossRef]  
51. Huang, K.-C.; Li, J.; Zhang, C.; Tan, Y.; Cheng, J.-X. Multiplex Stimulated Raman Scattering Imaging Cytometry Reveals Lipid-Rich Protrusions in Cancer Cells under Stress Condition. Science 2020, 23, 100953. [CrossRef]  
52. Fu, D.; Holtom, G.; Freudiger, C.; Zhang, X.; Xie, X.S. Hyperspectral Imaging with Stimulated Raman Scattering by Chirped Femtosecond Lasers. J. Phys. Chem. B 2013, 117, 4634–4640. [CrossRef] [PubMed]  
53. Ji, M.; Orringer, D.A.; Freudiger, C.W.; Ramkissoon, S.; Liu, X.; Lau, D.; Golby, A.J.; Norton, I.; Hayashi, M.; Agar, N.Y.R.; et al. Rapid, Label-Free Detection of Brain Tumors with Stimulated Raman Scattering Microscopy. Sci. Transl. Med. 2013, 5, 201ra119. [CrossRef] [PubMed]  
54. Folick, A.; Min, W.; Wang, M.C. Label-free imaging of lipid dynamics using Coherent Anti-stokes Raman Scattering (CARS) and Stimulated Raman Scattering (SRS) microscopy. Curr. Opin. Genet. Dev. 2011, 21, 585–590. [CrossRef] [PubMed]  
55. Yu, Y.; Ramachandran, P.V.; Wang, M.C. Shedding new light on lipid functions with CARS and SRS microscopy. Biochim. Biophys. Acta BBA Mol. Cell Biol. Lipids 2014, 1841, 1120–1129. [CrossRef]  
56. Abramczyk, H.; Imiela, A.; Sliwi ´nska, A. Novel strategies of Raman imaging for exploring cancer lipid reprogramming. ´ J. Mol. Liq. 2019, 274, 52–59. [CrossRef]  
57. Talari, A.C.S.; Evans, C.A.; Holen, I.; Coleman, R.E.; Rehman, I.U. Raman spectroscopic analysis differentiates between breast cancer cell lines. J. Raman Spectrosc. 2015, 46, 421–427. [CrossRef]  
58. Abramczyk, H.; Imiela, A.; Brozek-Płuska, B.; Kope´c, M.; Surmacki, J.;˙ Sliwi ´nska, A. Aberrant Protein Phosphorylation in Cancer´ by Using Raman Biomarkers. Cancers 2019, 11, 2017. [CrossRef]  
59. Marro, M.; Nieva, C.; De Juan, A.; Sierra, A. Unravelling the Metabolic Progression of Breast Cancer Cells to Bone Metastasis by Coupling Raman Spectroscopy and a Novel Use of Mcr-Als Algorithm. Anal. Chem. 2018, 90, 5594–5602. [CrossRef]  
60. Kopec, M.; Imiela, A.; Abramczyk, H. Monitoring glycosylation metabolism in brain and breast cancer by Raman imaging. Sci. Rep. 2019, 9, 1–13. [CrossRef]  
61. Chaturvedi, D.; Balaji, S.A.; Bn, V.K.; Ariese, F.; Umapathy, S.; Rangarajan, A. Different Phases of Breast Cancer Cells: Raman Study of Immortalized, Transformed, and Invasive Cells. Biosensors 2016, 6, 57. [CrossRef]  
62. Lemoine, É.; Dallaire, F.; Yadav, R.; Agarwal, R.; Kadoury, S.; Trudel, D.; Guiot, M.-C.; Petrecca, K.; Leblond, F. Feature engineering applied to intraoperativein vivoRaman spectroscopy sheds light on molecular processes in brain cancer: A retrospective study of 65 patients. Analyst 2019, 144, 6517–6532. [CrossRef]  
63. Lu, F.-K.; Ji, M.; Fu, D.; Ni, X.; Freudiger, C.W.; Holtom, G.; Xie, X.S. Multicolor stimulated Raman scattering microscopy. Mol. Phys. 2012, 110, 1927–1932. [CrossRef]  
64. Zhang, X.; Roeffaers, M.B.J.; Basu, S.; Daniele, J.R.; Fu, D.; Freudiger, C.W.; Holtom, G.R.; Xie, X.S. Label-Free Live-Cell Imaging of Nucleic Acids Using Stimulated Raman Scattering Microscopy. ChemPhysChem 2012, 13, 1054–1059. [CrossRef]  
65. Lu, F.-K.; Basu, S.; Igras, V.; Hoang, M.P.; Ji, M.; Fu, D.; Holtom, G.R.; Neel, V.A.; Freudiger, C.W.; Fisher, D.E.; et al. Label-free DNA imaging in vivo with stimulated Raman scattering microscopy. Proc. Natl. Acad. Sci. USA 2015, 112, 11624–11629. [CrossRef]  
66. Zhuge, M.; Huang, K.; Lee, H.J.; Jiang, Y.; Tan, Y.; Lin, H.; Dong, P.; Zhao, G.; Matei, D.; Yang, Q.; et al. Ultrasensitive Vibrational Imaging of Retinoids by Visible Preresonance Stimulated Raman Scattering Microscopy. Adv. Sci. 2021, 2003136. [CrossRef]  
67. Jamieson, L.E.; Wetherill, C.; Faulds, K.; Graham, D. Ratiometric Raman imaging reveals the new anti-cancer potential of lipid targeting drugs. Chem. Sci. 2018, 9, 6935–6943. [CrossRef]  
68. Potcoava, M.C.; Futia, G.L.; Aughenbaugh, J.; Schlaepfer, I.R.; Gibson, E.A. Raman and coherent anti-Stokes Raman scattering microscopy studies of changes in lipid content and composition in hormone-treated breast and prostate cancer cells. J. Biomed. Opt. 2014, 19, 111605. [CrossRef]  
69. Wen, X.; Ou, Y.-C.; Bogatcheva, G.; Thomas, G.; Mahadevan-Jansen, A.; Singh, B.; Lin, E.C.; Bardhan, R. Probing metabolic alterations in breast cancer in response to molecular inhibitors with Raman spectroscopy and validated with mass spectrometry. Chem. Sci. 2020, 11, 9863–9874. [CrossRef]  
70. El-Mashtoly, S.F.; Yosef, H.K.; Petersen, D.; Mavarani, L.; Maghnouj, A.; Hahn, S.; Kötting, C.; Gerwert, K. Label-Free Raman Spectroscopic Imaging Monitors the Integral Physiologically Relevant Drug Responses in Cancer Cells. Anal. Chem. 2015, 87, 7297–7304. [CrossRef] [PubMed]  
71. Larion, M.; Dowdy, T.; Ruiz-Rodado, V.; Meyer, M.W.; Song, H.; Zhang, W.; Davis, D.; Gilbert, M.R.; Lita, A. Detection of Metabolic Changes Induced via Drug Treatments in Live Cancer Cells and Tissue Using Raman Imaging Microscopy. Biosensors 2018, 9, 5. [CrossRef] [PubMed]  
72. Farhane, Z.; Bonnier, F.; Casey, A.; Byrne, H.J. Raman micro spectroscopy for in vitro drug screening: Subcellular localisation and interactions of doxorubicin. Analyst 2015, 140, 4212–4223. [CrossRef]  
73. Zhang, H.; Xiao, L.; Li, Q.; Qi, X.; Zhou, A. Microfluidic chip for non-invasive analysis of tumor cells interaction with anti-cancer drug doxorubicin by AFM and Raman spectroscopy. Biomicrofluidics 2018, 12, 024119. [CrossRef] [PubMed]  
74. Zhang, Y.; Xu, J.; Yu, Y.; Shang, W.; Ye, A. Anti-Cancer Drug Sensitivity Assay with Quantitative Heterogeneity Testing Using Single-Cell Raman Spectroscopy. Molecules 2018, 23, 2903. [CrossRef]  
75. Aljakouch, K.; Lechtonen, T.; Yosef, H.K.; Hammoud, M.K.; Alsaidi, W.; Kötting, C.; Mügge, C.; Kourist, R.; El-Mashtoly, S.F.; Gerwert, K. Raman Microspectroscopic Evidence for the Metabolism of a Tyrosine Kinase Inhibitor, Neratinib, in Cancer Cells. Angew. Chem. Int. Ed. 2018. 57. 72507254. [CrossRefl [PubMed]  
76. El-Mashtoly, S.F.; Petersen, D.; Yosef, H.K.; Mosig, A.; Reinacher-Schick, A.; Kötting, C.; Gerwert, K. Label-free imaging of drug distribution and metabolism in colon cancer cells by Raman microscopy. Analyst 2014, 139, 1155–1161. [CrossRef] [PubMed]  
77. Fu, D.; Zhou, J.; Zhu, W.S.; Manley, P.W.; Wang, Y.K.; Hood, T.; Wylie, A.; Xie, X.S. Imaging the intracellular distribution of tyrosine kinase inhibitors in living cells with quantitative hyperspectral stimulated Raman scattering. Nat. Chem. 2014, 6, 614–622. [CrossRef] [PubMed]  
78. Sepp, K.; Lee, M.; Bluntzer, M.T.J.; Helgason, G.V.; Hulme, A.N.; Brunton, V.G. Utilizing Stimulated Raman Scattering Microscopy To Study Intracellular Distribution of Label-Free Ponatinib in Live Cells. J. Med. Chem. 2019, 63, 2028–2034. [CrossRef] [PubMed]  
79. Qiu, S.; Weng, Y.; Li, Y.; Chen, Y.; Pan, Y.; Liu, J.; Lin, W.; Chen, X.; Li, M.; Lin, T.; et al. Raman profile alterations of irradiated human nasopharyngeal cancer cells detected with laser tweezer Raman spectroscopy. RSC Adv. 2020, 10, 14368–14373. [CrossRef]  
80. Roman, M.; Wrobel, T.P.; Panek, A.; Paluszkiewicz, C.; Kwiatek, W.M. Lipid droplets in prostate cancer cells and effect of irradiation studied by Raman microspectroscopy. Biochim. Biophys. Acta BBA Mol. Cell Biol. Lipids 2020, 1865, 158753. [CrossRef]  
81. Milligan, K.; Deng, X.; Shreeves, P.; Ali-Adeeb, R.; Matthews, Q.; Brolo, A.; Lum, J.J.; Andrews, J.L.; Jirasek, A. Raman spectroscopy and group and basis-restricted non negative matrix factorisation identifies radiation induced metabolic changes in human cancer cells. Sci. Rep. 2021, 11, 1–11. [CrossRef] [PubMed]  
82. Kumar, S.; Visvanathan, A.; Arivazhagan, A.; Santhosh, V.; Somasundaram, K.; Umapathy, S. Assessment of Radiation Resistance and Therapeutic Targeting of Cancer Stem Cells: A Raman Spectroscopic Study of Glioblastoma. Anal. Chem. 2018, 90, 12067–12074. [CrossRef] [PubMed]  
83. Van Nest, S.J.; Nicholson, L.M.; Pavey, N.; Hindi, M.N.; Brolo, A.G.; Jirasek, A.; Lum, J.J. Raman spectroscopy detects metabolic signatures of radiation response and hypoxic fluctuations in non-small cell lung cancer. BMC Cancer 2019, 19, 474. [CrossRef] [PubMed]  
84. Auner, G.W.; Koya, S.K.; Huang, C.; Broadbent, B.; Trexler, M.; Auner, Z.; Elias, A.; Mehne, K.C.; Brusatori, M.A. Applications of Raman spectroscopy in cancer diagnosis. Cancer Metastasis Rev. 2018, 37, 691–717. [CrossRef] [PubMed]  
85. Cui, S.; Zhang, S.; Yue, S. Raman Spectroscopy and Imaging for Cancer Diagnosis. J. Health Eng. 2018, 2018, 1–11. [CrossRef] [PubMed]  
86. Austin, L.A.; Osseiran, S.; Evans, C.L. Raman technologies in cancer diagnostics. Analyst 2015, 141, 476–503. [CrossRef] [PubMed]  
87. Contorno, S.; Darienzo, R.E.; Tannenbaum, R. Evaluation of aromatic amino acids as potential biomarkers in breast cancer by Raman spectroscopy analysis. Sci. Rep. 2021, 11, 1–9. [CrossRef]  
88. Haka, A.S.; Shafer-Peltier, K.E.; Fitzmaurice, M.; Crowe, J.; Dasari, R.R.; Feld, M.S. Diagnosing breast cancer by using Raman spectroscopy. Proc. Natl. Acad. Sci. USA 2005, 102, 12371–12376. [CrossRef] [PubMed]  
89. Hu, C.; Wang, J.; Zheng, C.; Xu, S.; Zhang, H.; Liang, Y.; Bi, L.; Fan, Z.; Han, B.; Xu, W. Raman spectra exploring breast tissues: Comparison of principal component analysis and support vector machine-recursive feature elimination. Med. Phys. 2013, 40, 063501. [CrossRef]  
90. Abramczyk, H.; Brozek-Pluska, B.; Surmacki, J.; Jablonska-Gajewicz, J.; Kordek, R. Raman ‘optical biopsy’ of human breast cancer. Prog. Biophys. Mol. Biol. 2012, 108, 74–81. [CrossRef]  
91. Brozek-Pluska, B.; Musial, J.; Kordek, R.; Bailo, E.; Dieing, T.; Abramczyk, H. Raman spectroscopy and imaging: Applications in human breast cancer diagnosis. Analyst 2012, 137, 3773–3780. [CrossRef]  
92. Abramczyk, H.; Brozek-Pluska, B.; Surmacki, J.; Jablo ´nska, J.; Kordek, R. The label-free Raman imaging of human breast cancer. J. Mol. Liq. 2011, 164, 123–131. [CrossRef]  
93. Bendau, E.; Smith, J.; Zhang, L.; Ackerstaff, E.; Kruchevsky, N.; Wu, B.; Koutcher, J.A.; Alfano, R.; Shi, L. Distinguishing metastatic triple-negative breast cancer from nonmetastatic breast cancer using second harmonic generation imaging and resonance Raman spectroscopy. J. Biophotonics 2020, 13, e202000005. [CrossRef] [PubMed]  
94. Kope´c, M.; Abramczyk, H. Angiogenesis—A crucial step in breast cancer growth, progression and dissemination by Raman imaging. Spectrochim. Acta Part A Mol. Biomol. Spectrosc. 2018, 198, 338–345. [CrossRef] [PubMed]  
95. Brozek-Pluska, B.; Kope´c, M.; Abramczyk, H. Development of a new diagnostic Raman method for monitoring epigenetic modifications in the cancer cells of human breast tissue. Anal. Methods 2016, 8, 8542–8553. [CrossRef]  
96. Chrabaszcz, K.; Kochan, K.; Fedorowicz, A.; Jasztal, A.; Buczek, E.; Leslie, L.S.; Bhargava, R.; Malek, K.; Chlopicki, S.; Marzec, K.M. FT-IR- and Raman-based biochemical profiling of the early stage of pulmonary metastasis of breast cancer in mice. Analyst 2018, 143, 2042–2050. [CrossRef] [PubMed]  
97. Koljenovi´c, S.; Choo-Smith, L.-P.; Schut, T.C.B.; Kros, J.M.; Berge, H.J.V.D.; Puppels, G.J. Discriminating Vital Tumor from Necrotic Tissue in Human Glioblastoma Tissue Samples by Raman Spectroscopy. Lab. Investig. 2002, 82, 1265–1277. [CrossRef]  
98. Koljenovic, S.; Schut, T.C.B.; Wolthuis, R.; Vincent, A.J.P.E.; Hendriks-Hagevi, G.; Santos, L.; Kros, J.M.; Puppels, G.J. Raman Spectroscopic Characterization of Porcine Brain Tissue Using a Single Fiber-Optic Probe. Anal. Chem. 2007, 79, 557–564. [CrossRef]  
99. Krafft, C.; Belay, B.; Bergner, N.; Romeike, B.F.M.; Reichart, R.; Kalff, R.; Popp, J. Advances in optical biopsy—Correlation of malignancy and cell density of primary brain tumors using Raman microspectroscopic imaging. Analyst 2012, 137, 5533–5537. [CrossRef]  
100. Jermyn, M.; Mok, K.; Mercier, J.; Desroches, J.; Pichette, J.; Saint-Arnaud, K.; Bernstein, L.; Guiot, M.-C.; Petrecca, K.; Leblond, F. Intraoperative brain cancer detection with Raman spectroscopy in humans. Sci. Transl. Med. 2015, 7, 274ra19. [CrossRef]  
101. Bratchenko, I.A.; Artemyev, D.N.; Myakinin, O.O.; Khristoforova, Y.A.; Moryatov, A.A.; Kozlov, S.V.; Zakharov, V.P. Combined Raman and autofluorescence ex vivo diagnostics of skin cancer in near-infrared and visible regions. J. Biomed. Opt. 2017, 22, 027005. [CrossRef] [PubMed]  
102. Schut, T.C.B.; Caspers, P.J.; Puppels, G.J.; Nijssen, A.; Heule, F.; Neumann, M.H.; Hayes, D.P. Discriminating Basal Cell Carcinoma from its Surrounding Tissue by Raman Spectroscopy. J. Investig. Dermatol. 2002, 119, 64–69. [CrossRef] [PubMed]  
103. Bodanese, B.; Silveira, L.; Albertini, R.; Zângaro, R.A.; Pacheco, M.T.T. Differentiating Normal and Basal Cell Carcinoma Human Skin Tissues In Vitro Using Dispersive Raman Spectroscopy: A Comparison Between Principal Components Analysis and Simplified Biochemical Models. Photomed. Laser Surg. 2010, 28, S119–S127. [CrossRef] [PubMed]  
104. Bodanese, B.; Silveira, F.L.; Zângaro, R.A.; Pacheco, M.T.T.; Pasqualucci, C.A.; Silveira, L. Discrimination of Basal Cell Carci noma and Melanoma from Normal Skin Biopsies in Vitro Through Raman Spectroscopy and Principal Component Analysis. Photomed. Laser Surg. 2012, 30, 381–387. [CrossRef]  
105. Nijssen, A.; Maquelin, K.; Santos, L.F.; Caspers, P.J.; Schut, T.C.B.; Hollander, J.C.D.; Neumann, M.H.A.; Puppels, G.J. Discriminat ing basal cell carcinoma from perilesional skin using high wave-number Raman spectroscopy. J. Biomed. Opt. 2007, 12, 034004. [CrossRef] [PubMed]  
106. Ishigaki, M.; Maeda, Y.; Taketani, A.; Andriana, B.B.; Ishihara, R.; Wongravee, K.; Ozaki, Y.; Sato, H. Diagnosis of early-stage esophageal cancer by Raman spectroscopy and chemometric techniques. Analyst 2016, 141, 1027–1033. [CrossRef]  
107. Almond, L.M.; Hutchings, J.; Lloyd, G.; Barr, H.; Shepherd, N.; Day, J.; Stevens, O.; Sanders, S.; Wadley, M.; Stone, N.; et al. Endoscopic Raman spectroscopy enables objective diagnosis of dysplasia in Barrett’s esophagus. Gastrointest. Endosc. 2014, 79, 37–45. [CrossRef]  
108. Hsu, C.-W.; Huang, C.-C.; Sheu, J.-H.; Lin, C.-W.; Lin, L.-F.; Jin, J.-S.; Chen, W. Differentiating gastrointestinal stromal tumors from gastric adenocarcinomas and normal mucosae using confocal Raman microspectroscopy. J. Biomed. Opt. 2016, 21, 75006. [CrossRef]  
109. Petersen, D.; Naveed, P.; Ragheb, A.; Niedieker, D.; El-Mashtoly, S.; Brechmann, T.; Kötting, C.; Schmiegel, W.; Freier, E.; Pox, C.; et al. Raman fiber-optical method for colon cancer detection: Cross-validation and outlier identification approach. Spectrochim. Acta Part A Mol. Biomol. Spectrosc. 2017, 181, 270–275. [CrossRef]  
110. Huang, Z.; McWilliams, A.; Lui, H.; McLean, D.I.; Lam, S.; Zeng, H. Near-infrared Raman spectroscopy for optical diagnosis of lung cancer. Int. J. Cancer 2003, 107, 1047–1052. [CrossRef]  
111. Magee, N.D.; Villaumie, J.S.; Marple, E.T.; Ennis, M.; Elborn, J.S.; McGarvey, J.J. ExVivo Diagnosis of Lung Cancer Using a Raman Miniprobe. J. Phys. Chem. B 2009, 113, 8137–8141. [CrossRef]  
112. Légaré, F.; Evans, C.L.; Ganikhanov, F.; Xie, X.S. Towards CARS Endoscopy. Opt. Express 2006, 14, 4427–4432. [CrossRef] [PubMed]  
113. Saar, B.G.; Johnston, R.S.; Freudiger, C.W.; Xie, X.S.; Seibel, E.J. Coherent Raman scanning fiber endoscopy. Opt. Lett. 2011, 36, 2396–2398. [CrossRef] [PubMed]  
114. Orringer, D.A.; Pandian, B.; Niknafs, Y.S.; Hollon, T.C.; Boyle, J.; Lewis, S.; Garrard, M.; Hervey-Jumper, S.L.; Garton, H.J.L.; Maher, C.O.; et al. Rapid intraoperative histology of unprocessed surgical specimens via fibre-laser-based stimulated Raman scattering microscopy. Nat. Biomed. Eng. 2017, 1, 1–13. [CrossRef] [PubMed]  
115. Huang, W.E.; Griffiths, R.I.; Thompson, I.P.; Bailey, M.J.; Whiteley, A.S. Raman Microscopic Analysis of Single Microbial Cells. Anal. Chem. 2004, 76, 4452–4458. [CrossRef] [PubMed]  
116. Wang, Y.; E Huang, W.; Cui, L.; Wagner, M. Single cell stable isotope probing in microbiology using Raman microspectroscopy. Curr. Opin. Biotechnol. 2016, 41, 34–42. [CrossRef]  
117. Berry, D.; Mader, E.; Lee, T.K.; Woebken, D.; Wang, Y.; Zhu, D.; Palatinszky, M.; Schintlmeister, A.; Schmid, M.C.; Hanson, B.T.; et al. Tracking heavy water (D2O) incorporation for identifying and sorting active microbial cells. Proc. Natl. Acad. Sci. USA 2015, 112, E194–E203. [CrossRef]  
118. Hoedt, E.; Zhang, G.; Neubert, T.A. Stable Isotope Labeling by Amino Acids in Cell Culture (SILAC) for Quantitative Proteomics. Adv. Exp. Med. Biol. 2014, 806, 93–106. [CrossRef]  
119. Everley, P.A.; Krijgsveld, J.; Zetter, B.R.; Gygi, S.P. Quantitative Cancer Proteomics: Stable Isotope Labeling with Amino Acids in Cell Culture (SILAC) as a Tool for Prostate Cancer Research. Mol. Cell. Proteom. 2004, 3, 729–735. [CrossRef]  
120. Wang, X.; He, Y.; Ye, Y.; Zhao, X.; Deng, S.; He, G.; Zhu, H.; Xu, N.; Liang, S. SILAC–based quantitative MS approach for real-time recording protein-mediated cell-cell interactions. Sci. Rep. 2018, 8, 1–9. [CrossRef]  
121. Abraham, W.-R. Applications and impacts of stable isotope probing for analysis of microbial interactions. Appl. Microbiol. Biotechnol. 2014, 98, 4817–4828. [CrossRef]  
122. Miyagi, M.; Kasumov, T. Monitoring the synthesis of biomolecules using mass spectrometry. Philos. Trans. R. Soc. A Math. Phys. Eng. Sci. 2016, 374, 20150378. [CrossRef] [PubMed]  
123. Matthäus, C.; Krafft, C.; Dietzek, B.; Brehm, B.R.; Lorkowski, S.; Popp, J. Noninvasive Imaging of Intracellular Lipid Metabolism in Macrophages by Raman Microscopy in Combination with Stable Isotopic Labeling. Anal. Chem. 2012, 84, 8549–8556. [CrossRef]  
124. Stiebing, C.; Matthäus, C.; Krafft, C.; Keller, A.-A.; Weber, K.; Lorkowski, S.; Popp, J. Complexity of fatty acid distribution inside human macrophages on single cell level using Raman micro-spectroscopy. Anal. Bioanal. Chem. 2014, 406, 7037–7046. [CrossRef]  
125. Stiebing, C.; Meyer, T.; Rimke, I.; Matthäus, C.; Schmitt, M.; Lorkowski, S.; Popp, J. Real-time Raman and SRS imaging of living human macrophages reveals cell-to-cell heterogeneity and dynamics of lipid uptake. J. Biophotonics 2017, 10, 1217–1226. [CrossRef]  
126. Majzner, K.; Tott, S.; Roussille, L.; Deckert, V.; Chlopicki, S.; Baranska, M. Uptake of fatty acids by a single endothelial cell investigated by Raman spectroscopy supported by AFM. Analyst 2018, 143, 970–980. [CrossRef] [PubMed]  
127. Li, J.; Cheng, J.-X. Direct Visualization of De novo Lipogenesis in Single Living Cells. Sci. Rep. 2014, 4, 6807. [CrossRef] [PubMed]  
128. Alfonso-Garcia, A.; Pfisterer, S.G.; Riezman, H.; Ikonen, E.; Potma, E.O. D38-cholesterol as a Raman active probe for imaging intracellular cholesterol storage. J. Biomed. Opt. 2015, 21, 061003. [CrossRef]  
129. Weeks, T.; Schie, I.; Hartigh, L.J.D.; Rutledge, J.C.; Huser, T. Lipid-cell interactions in human monocytes investigated by doubly-resonant coherent anti-Stokes Raman scattering microscopy. J. Biomed. Opt. 2011, 16, 021117. [CrossRef] [PubMed]  
130. Dodo, K.; Sato, A.; Tamura, Y.; Egoshi, S.; Fujiwara, K.; Oonuma, K.; Nakao, S.; Terayama, N.; Sodeoka, M. Synthesis of deuterated γ-linolenic acid and application for biological studies: Metabolic tuning and Raman imaging. Chem. Commun. 2021, 57, 2180–2183. [CrossRef]  
131. Matthäus, C.; Kale, A.; Chernenko, T.; Torchilin, V.; Diem, M. New Ways of Imaging Uptake and Intracellular Fate of Liposomal Drug Carrier Systems inside Individual Cells, Based on Raman Microscopy. Mol. Pharm. 2008, 5, 287–293. [CrossRef]  
132. Van Manen, H.-J.; Lenferink, A.T.; Otto, C. Noninvasive Imaging of Protein Metabolic Labeling in Single Human Cells Using Stable Isotopes and Raman Microscopy. Anal. Chem. 2008, 80, 9576–9582. [CrossRef]  
133. Wei, L.; Yu, Y.; Shen, Y.; Wang, M.C.; Min, W. Vibrational imaging of newly synthesized proteins in live cells by stimulated Raman scattering microscopy. Proc. Natl. Acad. Sci. USA 2013, 110, 11226–11231. [CrossRef] [PubMed]  
134. Wei, L.; Shen, Y.; Xu, F.; Hu, F.; Harrington, J.K.; Targoff, K.L.; Min, W. Imaging Complex Protein Metabolism in Live Organisms by Stimulated Raman Scattering Microscopy with Isotope Labeling. ACS Chem. Biol. 2015, 10, 901–908. [CrossRef] [PubMed]  
135. Shen, Y.; Xu, F.; Wei, L.; Hu, F.; Min, W. Live-cell quantitative imaging of proteome degradation by stimulated Raman scattering. Angew. Chem. Int. Ed. 2014, 53, 5596–5599. [CrossRef]  
136. Miao, K.; Wei, L. Live-Cell Imaging and Quantification of PolyQ Aggregates by Stimulated Raman Scattering of Selective Deuterium Labeling. ACS Central Sci. 2020, 6, 478–486. [CrossRef]  
137. Zhang, L.; Shi, L.; Shen, Y.; Miao, Y.; Wei, M.; Qian, N.; Liu, Y.; Min, W. Spectral tracing of deuterium for imaging glucose metabolism. Nat. Biomed. Eng. 2019, 3, 402–413. [CrossRef] [PubMed]  
138. Lee, D.; Du, J.; Yu, R.; Su, Y.; Heath, J.R.; Wei, L. Visualizing Subcellular Enrichment of Glycogen in Live Cancer Cells by Stimulated Raman Scattering. Anal. Chem. 2020, 92, 13182–13191. [CrossRef]  
139. Hu, F.; Chen, Z.; Zhang, L.; Shen, Y.; Wei, L.; Min, W. Vibrational Imaging of Glucose Uptake Activity in Live Cells and Tissues by Stimulated Raman Scattering. Angew. Chem. Int. Ed. 2015, 54, 9821–9825. [CrossRef] [PubMed]  
140. Long, R.; Zhang, L.; Shi, L.; Shen, Y.; Hu, F.; Zeng, C.; Min, W. Two-color vibrational imaging of glucose metabolism using stimulated Raman scattering. Chem. Commun. 2018, 54, 152–155. [CrossRef]  
141. Chen, Z.; Paley, D.W.; Wei, L.; Weisman, A.L.; Friesner, R.A.; Nuckolls, C.; Min, W. Multicolor Live-Cell Chemical Imaging by Isotopically Edited Alkyne Vibrational Palette. J. Am. Chem. Soc. 2014, 136, 8027–8033. [CrossRef]  
142. Zhang, L.; Min, W. Bioorthogonal chemical imaging of metabolic changes during epithelial–mesenchymal transition of cancer cells by stimulated Raman scattering microscopy. J. Biomed. Opt. 2017, 22, 1–7. [CrossRef] [PubMed]  
143. Shi, L.; Zheng, C.; Shen, Y.; Chen, Z.; Silveira, E.S.; Zhang, L.; Wei, M.; Liu, C.; De Sena-Tomas, C.; Targoff, K.; et al. Optical imaging of metabolic dynamics in animals. Nat. Commun. 2018, 9, 1–17. [CrossRef] [PubMed]  
144. Hekmatara, M.; Baladehi, M.H.; Ji, Y.; Xu, J. D2O-Probed Raman Microspectroscopy Distinguishes the Metabolic Dynamics of Macromolecules in Organellar Anticancer Drug Response. Anal. Chem. 2021, 93, 2125–2134. [CrossRef] [PubMed]  
145. Matanfack, G.A.; Rüger, J.; Stiebing, C.; Schmitt, M.; Popp, J. Imaging the invisible—Bioorthogonal Raman probes for imaging of cells and tissues. J. Biophotonics 2020, 13, e202000129. [CrossRef]  
146. Yamakoshi, H.; Dodo, K.; Okada, M.; Ando, J.; Palonpon, A.; Fujita, K.; Kawata, S.; Sodeoka, M. Imaging of EdU, an Alkyne-Tagged Cell Proliferation Probe, by Raman Microscopy. J. Am. Chem. Soc. 2011, 133, 6102–6105. [CrossRef]  
147. Huang, W.E.; Stoecker, K.; Griffiths, R.; Newbold, L.; Daims, H.; Whiteley, A.S.; Wagner, M. Raman-FISH: Combining stable-isotope Raman spectroscopy and fluorescence in situ hybridization for the single cell analysis of identity and func tion. Environ. Microbiol. 2007, 9, 1878–1889. [CrossRef] [PubMed]  
148. Song, Y.; Cui, L.; López, J.; Ángel, S.; Xu, J.; Zhu, Y.-G.; Thompson, I.P.; Huang, W.E. Raman-Deuterium Isotope Probing for in-situ identification of antimicrobial resistant bacteria in Thames River. Sci. Rep. 2017, 7, 1–10. [CrossRef]  
149. Hong, W.; Karanja, C.W.; Abutaleb, N.S.; Younis, W.; Zhang, X.; Seleem, M.N.; Cheng, J.-X. Antibiotic Susceptibility Determination within One Cell Cycle at Single-Bacterium Level by Stimulated Raman Metabolic Imaging. Anal. Chem. 2018, 90, 3737–3743. [CrossRef]  
150. Xu, J.; Zhu, D.; Ibrahim, A.D.; Allen, C.C.R.; Gibson, C.M.; Fowler, P.W.; Song, Y.; Huang, W.E. Raman Deuterium Isotope Probing Reveals Microbial Metabolism at the Single-Cell Level. Anal. Chem. 2017, 89, 13305–13312. [CrossRef]  
151. Wang, Y.; Xu, J.; Kong, L.; Liu, T.; Yi, L.; Wang, H.; Huang, W.E.; Zheng, C. Raman-Deuterium isotope probing to study metabolic activities of single bacterial cells in human intestinal microbiota. Microb. Biotechnol. 2019, 13, 572–583. [CrossRef]  
152. Xu, J.; Preciado-Llanes, L.; Aulicino, A.; Decker, C.M.; Depke, M.; Salazar, M.G.; Schmidt, F.; Simmons, A.; Huang, W.E. Single-Cell and Time-Resolved Profiling of Intracellular Salmonella Metabolism in Primary Human Cells. Anal. Chem. 2019, 91, 7729–7737. [CrossRef] [PubMed]  
153. Li, H.-Z.; Zhang, D.; Yang, K.; An, X.-L.; Pu, Q.; Lin, S.-M.; Su, J.-Q.; Cui, L. Phenotypic Tracking of Antibiotic Resistance Spread via Transformation from Environment to Clinic by Reverse D2O Single-Cell Raman Probing. Anal. Chem. 2020, 92, 15472–15479. [CrossRef] [PubMed]  
154. Wang, Y.; Xu, J.; Kong, L.; Li, B.; Li, H.; Huang, W.E.; Zheng, C. Raman-activated sorting of antibiotic-resistant bacteria in human gut microbiota. Environ. Microbiol. 2020, 22, 2613–2624. [CrossRef] [PubMed]