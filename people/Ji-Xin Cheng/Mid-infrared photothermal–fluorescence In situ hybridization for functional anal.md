pubs.acs.org/ac

Article

# Mid-Infrared Photothermal−Fluorescence In Situ Hybridization for Functional Analysis and Genetic Identification of Single Cells

Yeran Bai,# Zhongyue Guo,# Fátima C. Pereira, Michael Wagner,\* and Ji-Xin Cheng\*

![](images/99443781e4b9a175ed7f7f8bae5215b0b892bc614f7d0ac18a1dbc35a3465570.jpg)

Cite This: Anal. Chem. 2023, 95, 2398−2405

![](images/9284f193070bba650ac7a6190f23f341c7d3af7e7699e55795903d928359c14d.jpg)

Read Online

ACCESS

![](images/7fab135e9275169b3bff703c2f0afecc324117412e7b654998b34f4a0a304bb7.jpg)

Metrics & More

![](images/2e85463e351e43a245c7c46e9f4bbbb5a9e7b0bec3fb94392d9210a883137002.jpg)

Article Recommendations

![](images/76506ba6107782d5936eaca240ac8e8c01f95857c3f6970bc88d70200703b40e.jpg)

Supporting Information

ABSTRACT: Simultaneous identification and metabolic analysis of microbes with single-cell resolution and high throughput are necessary to answer the question of “who eats what, when, and where” in complex microbial communities. Here, we present a mid-infrared photothermal−fluorescence in situ hybridization (MIP−FISH) platform that enables direct bridging of genotype and phenotype. Through multiple improvements of MIP imaging, the sensitive detection of isotopically labeled compounds incorporated into proteins of individual bacterial cells became possible, while simultaneous detection of FISH labeling with rRNA-targeted probes enabled the identification of the analyzed cells. In proof-of-concept experiments, we showed that the clear spectral red shift in the protein amide I region due to incorporation of 13C atoms originating from 13C-labeled glucose can be exploited by MIP−FISH to discriminate and identify 13C-labeled bacterial

cells within a complex human gut microbiome sample. The presented methods open new opportunities for single-cell structure− function analyses for microbiology.

![](images/99062c17be670453d96603e5d47c1f347b186fb18907050de614eb08fd3fde4c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["¹³C-glucose incubation"] --> B["Phenotype – metabolism"]
  B --> C["Genotype – identification"]
  C --> D["Fluorescence in situ hybridization"]
  D --> E["Mid-infrared photothermal microscopy"]
  E --> F["Fluorescence microscopy"]
```
</details>

## INTRODUCTION

In eukaryotic cell biology, measuring single-cell behaviors and cell-to-cell heterogeneity in a complex environment is key to understanding cellular interactions in different physiological conditions.1 For microorganisms, the heterogeneity in genotypic and phenotypic traits has a direct impact on human health and the functioning of environmental microbiomes.8−11 Consequently, the rapidly developing single-cell technologies have revolutionized microbiology.1 -16 Among omics-based analyses, single-cell metabolomics provides the most immediate and dynamic picture of the functionality of a cell, but it is arguably the most difficult to measure.17,18 Due to the small amount of metabolites present in single cells and the inability for amplification, detection sensitivity challenges are posed on metabolomics technology, especially when analyzing the comparably small bacterial and archaeal cells. Additionally, as the function of a cell in a given set of physiochemical conditions is a variable and dynamic property that cannot be reliably predicted from either metabolic reconstructions or genomics data alone,12 genotyping integrated with metabolic analysis provides a better way to understand how microorganisms interact with their biotic and abiotic environment. Therefore, technologies that help bridge genotype and phenotype of microbes at the single-cell level are in high demand.19−22

Vibrational spectroscopy with stable isotope probing has recently emerged as a novel platform for single-cell metabolism profiling.23−30 Compared to mass spectrometry, vibrational spectroscopy is nondestructive and promises the compatibility with genotypic analysis.17 For stable isotope probing, cells are either incubated with specific substrates carrying isotopically labeled atoms (most commonly 13C, 15N, 18O, and 2 H) or with compounds such as heavy water $\left( ^ { 2 } \mathrm { H } _ { 2 } \mathrm { O } / \mathrm { D } _ { 2 } \mathrm { O } \right)$ that are incorporated by all metabolic active cells and thus serve as general activity markers.28 The newly anabolized biomolecules including lipids, proteins, and nucleic acids that contain the substrate-derived isotopes can be detected with single-cell resolution by investigating the red-shifted vibrational peaks due to the isotopic effect. Raman spectroscopy has been successfully applied to study bacterial metabolic activities by tracking incorporation of 2 H (deuterium) from D O or 13C from 13C-labeled substrates into single bacterial cell biomass.21,31 In these studies, the isotope-labeled cells were simultaneously identified using fluorescence in situ hybridization (FISH) with rRNA-targeted oligonucleotide probes. However, a spontaneous Raman spectrum from a single bacterium takes about 20 s to acquire, resulting in limited throughput that prevents large-scale analysis. Additionally, Raman spectroscopy is sometimes challenging to integrate with fluorescence-based genotyping methods because Raman

Received: October 11, 2022

Accepted: January 9, 2023

Published: January 18, 2023

![](images/ef2fa982b58c93a1d3ad751aee9e843c71886cea66e83b165485dcb884317876.jpg)

scattering and fluorescence emission can result in spectral overlap, which then complicates spectral interpretation.31 Recently, we reported on the combination of stimulated Raman scattering and FISH (SRS−FISH) that greatly boosted the Raman spectral acquisition speed and enabled an increase in throughput of analyzed microbial cells by 2−3 orders of magnitude.20 In this study, the activities of selected human gut microbiome members after incubation with different mucosal sugars in the presence of heavy water were investigated at high throughput. However, the direct visualization of sugar metabolism by tracking the incorporation of the 13C-labeled substrates by microbiome members has not yet been achieved with SRS−FISH. Additionally, SRS imaging required that the analyzed bacteria were immersed in liquid, while the two photon fluorescence imaging used for detection of FISHlabeled cells turned out to be more efficient in dry samples to avoid photobleaching, which complicated the experimental procedures.20 In contrast, infrared (IR) absorption can be applied to study cell metabolism32 while not suffering from fluorescence background. It should also not require different sample conditions for optimal IR and fluorescence measurements. However, the spatial resolution of conventional IR microscopy is limited to several micrometers,33,34 which hinders imaging of individual bacteria and co-recording of IR spectra and genotypic-informative FISH images.

The recently developed mid-IR photothermal (MIP) imaging addresses these limitations.35−41 In MIP, two lasers in the mid-IR and the visible regions are used. When the modulated mid-IR light is absorbed by the sample, it leads to sample heating and expansion (photothermal effect). The visible beam passing through the sample redirects its propagation direction due to the photothermal effect. A farfield photosensor detects the periodically modulated probe photons, and an image is created through pixel-by-pixel scanning or in a widefield manner. MIP has been successfully applied to image a range of organisms from a whole nematode Caenorhabditis elegans to a single virus at sub-micrometer spatial resolution. 38,39,42 47 The spectra from single bacteria have been recorded with MIP with high spectral fidelity and 290 nm spatial resolution.48,49 Additionally, the MIP signal could be detected from fluorescence intensity fluctuation for fluorophore-loaded samples.50,51 However, so far, there is no demonstration of MIP for simultaneous bacterial FISHgenotyping and metabolic imaging via isotope probing.

Here, we present a MIP−FISH platform that enables highthroughput metabolic imaging and identification of bacteria with single-cell resolution. By using oligonucleotide probes tagged with fluorophores to target signature regions in ribosomal RNA (rRNA) genes, FISH has become an indispensable tool for rapid and direct single-cell identification of microbes.52 In this work, we greatly improved the performance of a widefield MIP microscope through multiple optimizations such as the utilization of a nanosecond laser as the probe source. We then incorporated a fluorescence module on the widefield MIP to enable a coregistered MIP and fluorescence imaging from the same cells. To demonstrate the high-throughput metabolic imaging capability of MIP−FISH, we imaged the newly synthesized protein in hundreds of Escherichia coli cells from 13C-labeled glucose in seconds, with single-cell resolution. Simultaneous identification of bacterial taxa and metabolism profiling was demonstrated by imaging bacterial mixtures including a spiked gut microbiome sample. Collectively, our results demonstrate the capability of highthroughput microbial phenotyping of metabolism and genotyping with single-cell resolution through MIP−FISH.

## EXPERIMENTAL SECTION

MIP−FISH Microscope. Figure 1A shows a schematic illustration of the MIP−FISH microscope. For MIP imaging,

A  
![](images/6d6b03126f882cf66a1c4dbe132c6b4f91f0ed4d2308f117cbeebb3fde97b2db.jpg)

<details>
<summary>text_image</summary>

Camera
LPF
M
DM
Visible
Chopper
OAPM
IR
Sample
Obj.
</details>

B  
![](images/6d86f68daf53d5bda93c32e64ba2c83e9e87102c3b4af8ded7e48f51617639c1.jpg)

<details>
<summary>text_image</summary>

Metabolism
MIP
Identity
FISH
</details>

Figure 1. Schematic of MIP−FISH for in situ bacteria identification and phenotypical metabolic imaging. (A) The setup was based on a widefield MIP with the incorporation of a fluorescence module. OAPM, off-axis parabolic mirror. DM, dichroic mirror. LPF, long pass filter. M, mirror. (B) The subtraction image of MIP signals at two IR wavenumbers provides information on cellular metabolism. Positive values (in yellow) indicate active incorporation of $^ { 1 3 } \mathrm { C }$ from labeled substrates (here 13C-glucose) into protein, while negative values (in blue) indicate no $^ { 1 3 } \mathrm { \dot { C } }$ incorporation. (C) The fluorescence image detects a signal from FISH with rRNA-targeted probes, enabling the identification of bacterial taxa (Escherichia coli in red and Bacteroides thetaiotaomicron in green). Scale bars: 5 μm.

the mid-IR pump source is an optical parametric oscillator (OPO) laser (Firefly-LW, M Squared Lasers) with 20 ns pulse duration and 20 kHz repetition rate. The visible probe is a nanosecond laser (NPL52C, Thorlabs) with a center wavelength of 520 nm and a pulse width of 129 ns. The mid-IR beam was modulated using an optical chopper (MC2000B, Thorlabs) with a duty cycle of 50%. The mid-IR was optically chopped into pulse trains with a modulation frequency of 635 Hz, and around 16 bursts of IR pulses are in the period of one camera exposure time. The microscopy objective (MPLFLN Olympus, 100X, NA 0.9) was used to focus the visible light onto the sample as well as to collect the reflected light. To record the sample scattered light for MIP imaging, a high fullwell-capacity camera (Q-2HFW, Adimec) was used. For FISH imaging, a fluorescence module composed of a fluorescence camera (CS235MU, Thorlabs), a dichroic beam splitter, and filter sets were installed on the MIP microscope. An additional continuous wave 638 nm laser (0638-06-01, cobalt) was aligned with a 520 nm laser for additional fluorophore excitation. For MIP imaging, the IR power before the microscope was 32.9 and 34.8 mW at 1612 and 1656 cm−1 , respectively. All presented images were normalized with IR powers at corresponding wavelengths. The visible power was less than 1 mW before the microscope. Unless otherwise noted, the MIP images at one IR wavenumber were acquired at the speed of 2.4 s per image. For fluorescence imaging, the exposure time of the fluorescence camera was 1 s with a gain of 20 dB.

E. coli 13C-Glucose Isotope Labeling and Sample Preparation. For data presented in Figures 2 and 3, E. coli

![](images/5cebf2e89b98d95d6bcae69d5f75ae4cc225ba4ad61138648a6f29b456db38f5.jpg)  
Figure 2. Single-cell metabolic imaging of $^ { 1 3 } \mathrm { C } .$ -glucose incorporation by widefield MIP. Reflection and MIP images at two key protein amide I wavenumbers (1612 and 1656 cm−1 ) for E. coli cells incubated with 12C-glucose (A−C) or 13C-glucose (D−F). Scale bars 10 μm.

![](images/ba6017d89eb9680c10ce36251dc6b63123d2caeb9952738d2fe67b750f4162a1.jpg)

<details>
<summary>scatterplot</summary>

| percentage of ¹³C-glucose (%) | ¹³C-protein replacement ratio |
| ------------------------------ | ------------------------------- |
| 0                              | 0.0                             |
| 25                             | 0.3                             |
| 50                             | 0.5                             |
| 75                             | 0.7                             |
| 100                            | 1.0                             |
</details>

Figure 3. High detection sensitivity for $^ { 1 3 } \mathrm { C } .$ -incorporation. $^ { 1 3 } \mathrm { C } \mathrm { - }$ protein replacement ratio of E. coli cells grown for 24 h in minimal medium supplemented with 0.2% (w/v) of glucose at varying percentages of the total glucose in the form of ${ } ^ { 1 3 } \overline { { \mathrm { C } } } .$ -glucose (0, 5, 10, 30, 50, 70, 90, and 100%). More than 155 cells in each group were measured to produce the mean and standard deviation. A significant difference was observed between the 0 and the 5% $^ { 1 3 } \mathrm { C } .$ -glucoseincubated cells (pairwise t-test, $p = 3 . 8 6 \times 1 0 ^ { - 2 2 } )$ . A linear regression between the percentage of $^ { 1 3 } \mathrm { C }$ -glucose and $^ { 1 3 } \mathrm { C }$ -protein replacement ratio is shown as a dashed line $\left. R ^ { 2 } = 0 . 9 9 8 2 \right.$ )

BW25113 was inoculated from a single colony and precultured in a nutrient-rich medium (either tryptic soy broth or Mueller Hinton broth) for 3 h to reach the log phase. The optical density at 600 nm was measured to estimate the concentration of cells per milliliter. Then, the cultures were diluted to a concentration around $\begin{array} { l l } { \zeta } \ \times  & { 1 0 ^ { 5 } } \end{array}$ cfu/mL in a M9 minimal medium. The M9 minimal medium was supplemented with 12C-glucose or $^ { 1 3 } \mathrm { C - g l u c o s e } ,$ or a varying volume mixture of both, at a final concentration of 0.2% (w/v). The $^ { 1 3 } \mathrm { C } .$ -glucose used (D-glucose ${ \mathrm { U } } - \mathrm { \mathrm { } } ^ { 1 3 } { \mathrm { C } } _ { 6 } ,$ 99%, Cambridge Isotope Laboratories) was universally labeled�so that all carbon atoms were replaced with $^ { 1 3 } \mathrm { C }$ atoms. Cells were harvested by centrifugation at $1 1 { , } 0 0 0$ rpm and $4 ~ ^ { \circ } \mathrm { C }$ for 3 min after 24 h of aerobic incubation at $3 7 ^ { \circ } \mathrm { C }$ with glucose. The bacterial cells were then fixed with 10% formalin at.4 $\textsf { F } ^ { \circ } \mathbf { C }$ overnight. Multiple rounds of centrifugation and washes with deionized water were performed to remove the remaining fixative. A 2 μL drop of the concentrated cell solution in water was deposited on a poly- -lysine-coated IR-transparent silicon coverslip (silicon 2018, University Wafers) and dried in air.

Multispecies Sample and Fluorescence In Situ Hybridization. For data presented in Figures 4−6, E. coli K-12 (DSM 498) was grown aerobically at $3 7 ~ ^ { \circ } \mathrm { C }$ in a M9 minimal medium containing 0.4% (w/v) of either $^ { 1 2 } { \mathrm { C } } \cdot$ -glucose (unlabeled D-glucose, 99.5%, Sigma-Aldrich) or $^ { 1 3 } \mathrm { C }$ -glucose

![](images/1d2a596a15ddebf35a8e0af6eeaff5f9bffbca92c85aa090bfbae3f73c6ca518.jpg)

<details>
<summary>scatterplot</summary>

| Condition | Cell Type | 13C-Glucose No FISH | 13C-Glucose No FISH | 13C-Glucose FISH |
| --- | --- | --- | --- | --- |
| MIP 1612 cm⁻¹ | A | ~0.8 | ~0.7 | ~0.6 |
| MIP 1612 cm⁻¹ | B | ~0.9 | ~0.8 | ~0.7 |
| MIP 1612 cm⁻¹ | C | ~0.7 | ~0.6 | ~0.5 |
| MIP 1656 cm⁻¹ | D | ~0.6 | ~0.5 | ~0.4 |
| MIP 1656 cm⁻¹ | E | ~0.7 | ~0.6 | ~0.5 |
| MIP 1656 cm⁻¹ | F | ~0.8 | ~0.7 | ~0.6 |
| MIP 1656 cm⁻¹ | G | ~0.9 | ~0.8 | ~0.7 |
| MIP 1656 cm⁻¹ | H | ~0.7 | ~0.6 | ~0.5 |
| MIP 1656 cm⁻¹ | I | ~0.8 | ~0.7 | ~0.6 |
| FISH Gam42a -Cy5 | J | ~0.9 | ~0.8 | ~0.7 |
| FISH Gam42a -Cy5 | J | ~0.8 | ~0.7 | ~0.6 |
| FISH Gam42a -Cy5 | J | ~0.9 | ~0.8 | ~0.7 |
| FISH Gam42a -Cy5 | J | ~0.7 | ~0.6 | ~0.5 |
| FISH Gam42a -Cy5 | J | ~0.8 | ~0.7 | ~0.6 |
| FISH Gam42a -Cy5 | J | ~0.9 | ~0.8 | ~0.7 |
| FISH Gam42a -Cy5 | J | ~0.7 | ~0.6 | ~0.5 |
| FISH Gam42a -Cy5 | J | ~1.0 | ~0.9 | ~0.8 |
| FISH Gam42a -Cy5 | J | ~0.8 | ~0.7 | ~0.6 |
| FISH Gam42a -Cy5 | J | ~0.9 | ~0.8 | ~0.7 |
| FISH Gam42a -Cy5 | J | ~0.7 | ~0.6 | ~0.5 |
| FISH Gam42a -Cy5 | J | ~2.0 | ~1.9 | ~1.8 |
| FISH Gam42a -Cy5 | J | ~1.1 | ~1.0 | ~0.9 |
| FISH Gam42a -Cy5 | J | ~1.2 | ~1.1 | ~1.0 |
| FISH Gam42a -Cy5 | J | ~1.3 | ~1.2 | ~1.1 |
| FISH Gam42a -Cy5 | J | ~1.4 | ~1.3 | ~1.2 |
| FISH Gam42a -Cy5 | J | ~1.5 | ~1.4 | ~1.3 |
| FISH Gam42a -Cy5 | J | ~1.6 | ~1.5 | ~1.4 |
| FISH Gam42a -Cy5 | J | ~1.7 | ~1.6 | ~1.5 |
| FISH Gam42a -Cy5 | J | ~1.8 | ~1.7 | ~1.6 |
| FISH Gam42a -Cy5 | J | ~1.9 | ~1.8 | ~1.7 |
| FISH Gam42a -Cy5 | J | ~2.0 | ~1.9 | ~1.8 |
| FISH Gam42a -Cy5 | J | ~2.1 | ~2.0 | ~1.9 |
| FISH Gam42a -Cy5 | J | ~2.2 | ~2.1 | ~2.0 |
| FISH Gam42a -Cy5 | J | ~2.3 | ~2.2 | ~2.1 |
| FISH Gam42a -Cy5 | J | ~2.4 | ~2.3 | ~2.2 |
| FISH Gam42a -Cy5 | J | ~2.5 | ~2.4 | ~2.3 |
| FISH Gam42a -Cy5 | J | ~2.6 | ~2.5 | ~2.4 |
| FISH Gam42a -Cy5 | J | ~2.7 | ~2.6 | ~2.5 |
| FISH Gam42a -Cy5 | J | ~2.8 | ~2.7 | ~2.6 |
| FISH Gam42a -Cy5 | J | ~2.9 | ~2.8 | ~2.7 |
| FISH Gam42a -Cy5 | J | ~3.0 | ~2.9 | ~2.8 |
| FISH Gam42a -Cy5 | J | ~3.1 | ~3.0 | ~2.9 |
| FISH Gam42a -Cy5 | J | ~3.2 | ~3.1 | ~3.0 |
| FISH Gam42a -Cy5 | J | ~3.3 | ~3.2 | ~3.1 |
| FISH Gam42a -Cy5 | J | ~3.4 | ~3.3 | ~3.2 |
| FISH Gam42a -Cy5 | J | ~3.5 | ~3.4 | ~3.3 |
| FISH Gam42a -Cy5 | J | ~3.6 | ~3.5 | ~3.4 |
| FISH Gam42a -Cy5 | J | ~3.7 | ~3.6 | ~3.5 |
| FISH Gam42a -Cy5 | J | ~3.8 | ~3.7 | ~3.6 |
| FISH Gam42a -Cy5 | J | ~3.9 | ~3.8 | ~3.7 |
| FISH Gam42a -Cy5 | J | ~4.0 | ~3.9 | ~3.8 |
| FISH Gam42a -Cy5 | J | ~4.1 | ~4.0 | ~3.9 |
| FISH Gam42a -Cy5 | J | ~4.2 | ~4.1 | ~4.0 |
| FISH Gam42a -Cy5 | J | ~4.3 | ~4.2 | ~4.1 |
| FISH Gam42a -Cy5 | J | ~4.4 | ~4.3 | ~4.2 |
| FISH Gam42a -Cy5 | J | ~4.5 | ~4.4 | ~4.3 |
| FISH Gam42a -Cy5 | J | ~4.6 | ~4.5 | ~4.4 |
| FISH Gam42a -Cy5 | J | ~4.7 | ~4.6 | ~4.5 |
| FISH Gam42a -Cy5 | J | ~4.8 | ~4.7 | ~4.6 |
| FISH Gam42a -Cy5 | J | ~4.9 | ~4.8 | ~4.7 |
| FISH Gam42a -Cy5 | J | ~5.0 | ~4.9 | ~4.8 |
| FISH Gam42a -Cy5 | J | ~5.1 | ~5.0 | ~4.9 |
| FISH Gam42a -Cy5 | J | ~5.2 | ~5.1 | ~5.0 |
| FISH Gam42a -Cy5 | J | ~5.3 | ~5.2 | ~5.1 |
| FISH Gam42a -Cy5 | J | ~5.4 | ~5.3 | ~5.2 |
| FISH Gam42a -Cy5 | J | ~5.5 | ~5.4 | ~5.3 |
| FISH Gam42a -Cy5 | J | ~5.6 | ~5.5 | ~5.4 |
| FISH Gam42a -Cy5 | J | ~5.7 | ~5.6 | ~5.5 |
| FISH Gam42a -Cy5 | J | ~5.8 | ~5.7 | ~5.6 |
| FISH Gam42a -Cy5 | J | ~5.9 | ~5.8 | ~5.7 |
| FISH Gam42a -Cy5 | J | ~6.0 | ~5.9 | ~5.8 |
| FISH Gam42a -Cy5 | J | ~6.1 | ~6.0 | ~5.9 |
| FISH Gam42a -Cy5 | J | ~6.2 | ~6.1 | ~6.0 |
| FISH Gam42a -Cy5 | J | ~6.3 | ~6.2 | ~6.1 |
| FISH Gam42a -Cy5 | J | ~6.4 | ~6.3 | ~6.2 |
| FISH Gam42a -Cy5 | J | ~6.5 | ~6.4 | ~6.3 |
</details>

Figure 4. FISH is compatible with MIP metabolic imaging. E. coli cells grown in $\mathrm { ~ \mathsf ~ { ~ a ~ } ~ } ^ { 1 2 } \mathrm { C } { \cdot } \bar { \mathrm { g l } }$ ucose-containing medium with no FISH labeling were imaged at the two amide I peak wavenumbers as well as by recording fluorescence in the Cy5 channel $\left( \mathrm { A , D , G } \right)$ . $^ { 1 3 } \mathrm { C } \mathrm { - }$ glucose incubated E. coli with and without FISH labeling was imaged at the same channels (B,E,H and $^ { \mathrm { C , F , I ) } }$ using identical settings. (J) The $^ { 1 3 } \mathrm { C } \mathrm { - }$ protein replacement ratio was calculated for each incubation group. A slight reduction (7.5%) was observed for the $^ { 1 3 } \mathrm { C }$ -protein replacemen ratio between groups with and without FISH labeling. Scale bars 10 $\mu \mathrm { m . }$

A  
![](images/c09d84298fd608dba3a3bf9d82c316d6731186347a70e6740113e12a4fd3b250.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red and green labeled cells (Cy3 and Cy5), with a scale bar in the corner (no text or symbols beyond labels)
</details>

B  
![](images/060e0eceeda2977d655a276375da87710fec01486af5fa3a52b1180ffd855604.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing cellular structures with color scale bar (no text or symbols)
</details>

c  
![](images/86ba033a114c0a5cbdaf3509380f5f1943b1d79af47d415d7f6a8a09ba19be00.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of rod-shaped bacterial cells under labeled 'Reflection' (no additional text or symbols)
</details>

D  
![](images/a4dc35d8b56cb03d558630e33ae718e952d4bc15e203ad2d00c3f1c62daa5cdc.jpg)

<details>
<summary>scatterplot</summary>

| Group   | ¹³C-protein replacement ratio |
|---------|--------------------------------|
| E. coli | ~1.0                           |
| B. theta| ~0.0                           |
</details>

Figure 5. MIP−FISH imaging of bacterial mixtures. E. coli cells were incubated with 0.4% $\overline { { ( \mathbf { w } / \mathbf { v } ) } }$ 13C-glucose and hybridized with a $\mathrm { G a m } 4 2 \mathrm { a - C y } 5$ oligonucleotide probe, while B. theta cells grown in the presence of $^ { 1 2 } \mathrm { C - g l u c o s e }$ were hybridized with a $\mathrm { B a c } 3 0 3 \mathrm { - C y } 3$ oligonucleotide probe. (A) Fluorescence imaging for identification of E. coli (red) and B. theta (green). Scale bars 10 $\mu \mathrm { m } .$ . (B) Subtraction of two MIP images (intensity at 1612 $\mathrm { c m } ^ { - 1 }$ minus intensity at 1656 $\mathrm { c m } ^ { - 1 } )$ showed that a portion of the cells have incorporated $^ { 1 3 } \mathrm { C }$ into the protein (in yellow), while other cells showed no $^ { \circ } \mathrm { { } ^ { 1 3 } C }$ labeling (in blue). (C) Reflection image shows the cell morphology of the bacterial mixture. (D) Quantification of the $^ { 1 3 } \mathrm { C } \mathrm { - } 1$ protein replacement ratio. (Pairwise t-test: $p = 9 . 7 4 \times 1 0 ^ { - 3 3 } . )$ )

$\mathrm { \left( D { \cdot } g l u c o s e { - } ^ { 1 3 } C _ { 6 } , \right. }$ 99%, Sigma-Aldrich). Cells were grown overnight in a M9 medium containing unlabeled glucose and diluted 1:100 in $5$ mL of fresh medium containing either $^ { 1 2 } { \mathrm { C } } { \cdot }$ - $\mathrm { o r } ^ { \ 1 3 } \mathrm { C }$ -glucose. Bacteroides thetaiotaomicron (DSM 2079) (Bacteroides theta) cells were grown anaerobically (in a Coy Labs anaerobic chamber containing an atmosphere of 85% $\mathrm { N } _ { 2 } ,$ 10% $\mathrm { C O } _ { 2 } ,$ and 5% $\operatorname { H } _ { 2 } )$ in Bacteroides defined minimal medium (BMM) containing 0.5% (w/v) of either $^ { 1 2 } \mathrm { C }$ -glucose (unlabeled D-glucose, 99.5%, Sigma-Aldrich) or 13C-glucose $\dot { \left( \mathrm { D - g l u c o s e - } ^ { 1 3 } \mathrm { C } _ { 6 } , \right. }$ 99%, Sigma-Aldrich) $\cdot ^ { 5 3 }$ Cells were grown overnight in BMM containing unlabeled glucose and diluted 1:100 in 5 mL of fresh medium containing either ${ } ^ { 1 2 } \mathrm { C } \mathrm { - ~ } 0 \mathrm { r } \ { } ^ { 1 3 } \mathrm { C } \mathrm { . }$ - glucose. E. coli and B. theta cells were harvested by centrifugation at the late exponential phase (9 h of growth for E. coli and 12 h of growth for B. theta) and immediately fixed in 4% formaldehyde in phosphate-buffered saline (PBS) for 2 h at $4 ~ ^ { \circ } \mathrm { C }$ . Cells were subsequently washed once with PBS, resuspended in 1 mL of a 50% $\scriptstyle ( \mathbf { v } / \mathbf { v } )$ mixture of PBS and 96% ethanol, and finally stored $\mathrm { a t } - 2 0 \ ^ { \circ } \mathrm { C }$ until further use. E. coli cells were subsequently hybridized with the Gam42a probe tagged with the $\mathrm { C y } 5$ fluorophore, and B. theta cells were hybridized with the Bac303 probe tagged with the $\mathrm { C y } 3$ fluorophore following a standard FISH protocol (Supporting Information Methods and Table S1). Hybridized E. coli and B. theta cells were mixed, and $2 \mu \mathrm { L }$ of this mixture was spotted on the poly-L-lysine-coated silicon coverslips and allowed to dry in air protected from light. In addition, a cultured human gut microbiome sample stored in PBS (Supporting Information Methods) and prehybridized E. coli cells that have been stored in PBS/ethanol were gently mixed in an Eppendorf tube and subsequently spotted on poly-L-lysine-coated silicon coverslips. Excess salt was removed by adding 2 $\mu \mathrm { L }$ of Milli- $\mathbf { \nabla } \cdot \mathbf { Q }$ water onto the dried spot. Subsequently, the water was gently blown away, and the spot was dried again at room temperature protected from light.

A  
![](images/5a9c93949ee263212f60ddffd250c6963a9b5ba96ae71519874e05dadd8e4b1e.jpg)

<details>
<summary>natural_image</summary>

Microscopy image showing red fluorescent spots labeled 'Cy5' against a black background, with a scale bar at bottom (no text or symbols beyond label)
</details>

B

![](images/ada639c158c476e35cfbc41cb537915b4a8c80af9461d27f3450ccb6f1cd0c88.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing cellular structures with color scale bar (no text or symbols)
</details>

C  
![](images/50e11a82fb14e8f177d6b686c0c559b632f365344f1e1902f7ea4867c85e6cb8.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of rod-shaped bacterial cells under reflection (no text or symbols)
</details>

D  
![](images/33b1c01bdc9e70420f880fd44ad2955153bbf0901e678775a62b73f642701864.jpg)

<details>
<summary>scatterplot</summary>

| Group          | 13C-protein replacement ratio |
| -------------- | ------------------------------ |
| E. coli        | 0.8                            |
| gut microbiome | 0.4                            |
</details>

Figure 6. MIP−FISH imaging of a gut microbiome sample with spiked $^ { 1 3 } \mathrm { C }$ -labeled E. coli cells. $^ { 1 3 } \mathrm { C }$ -glucose fully labeled $E .$ coli cells that were FISH labeled with Cy5 were mixed with an isotopically unlabeled human gut microbiome sample. (A) Fluorescence imaging enabled localization of the added E. coli cells in the complex sample. Scale bars 10 μm. (B) MIP subtraction image indicated $^ { \mathbf { \lambda } _ { 1 3 } } \mathrm { C }$ -labeling for E. coli (in yellow). (C) Reflection image of the sample mixture. (D) Quantification of the ${ } ^ { \mathrm { i } 3 } \mathrm { C }$ -protein replacement ratio. (Pairwise ttest: $p = 7 . 6 9 \times 1 0 ^ { - 2 4 } . \AA )$ )

13C-Protein Replacement Ratio Quantification. For high-throughput, single-cell analysis, the regions of interests were determined based on the reflection images. To quantify metabolic activity, we defined the $^ { 1 3 } { \mathrm { C } } .$ -protein replacement ratio as the relative contribution of the $^ { 1 3 } \mathrm { C }$ -protein to the whole protein (Figure S1). The contribution was calculated based on four coefficients obtained from two reference samples at the original amide I $\left( 1 6 5 6 ~ \mathrm { c m } ^ { - 1 } \right)$ and the shifted amide I $( 1 6 1 2 c m ^ { - 1 } )$ bands. Since different culture and treatment conditions were used, we obtained different coefficients for ingroup comparison. The details of coefficients and statistics for reported experiments are listed in Table S2. We also recorded the coefficients for the same reference sample on different days and observed less than 6% variation (Table S3).

![](images/faeb30f18cf7908093bb99bb2bfc1fa018b15de51e27d709c3e61ef15f7214fa.jpg)

## RESULTS AND DISCUSSION

MIP−FISH Platform. We improved the performance of the previously reported first-generation widefield MIP micro-$\stackrel { \star } { \mathbf { s c o p e } ^ { 4 1 } }$ and achieved an over 2 orders of magnitude increase of the imaging speed by making the following modifications: (1) a LED was used as the probe source in the first-generation MIP setup with a minimal pulse width of 900 ns, which was ideal for micron-sized polymer beads since the decay constant is around several microseconds.41,54 However, the signal produced from a single bacterium is much weaker than that of a polymer bead, and the decay constant is much shorter, reaching to 280 $\mathrm { n } \mathrm { s . } ^ { 3 5 }$ Therefore, we coupled a nanosecond laser with a pulse width of 129 ns to match the decay constant to improve the detection sensitivity for bacteria. (2) MIP is a shot noise-limited technique, and the signal-to-noise ratio (SNR) is proportional to the total probe photon received.41 Therefore, we incorporated a high full-well-capacity $\left( 2 ~ \mathrm { M e } ^ { - } \right)$ camera to the current setup. (3) To accommodate the high full-well-capacity camera with a pixel size of 12 μm, we used a high-magnification and high numerical aperture objective. Other improvements including shortening of the IR pathlength, galvo scanner adjusting the pointing of the IR beam when tuning wavenumbers, and adding a laser speckle reduction module synergistically worked together to push the MIP imaging speed. As a comparison, we previously achieved 2 frames/s for 1 μm polymethyl methacrylate (PMMA) beads imaging with a field of view of around 20 μm and a SNR of $2 4 . ^ { 5 4 }$ By implementing the optimizations, we achieved 635 frames/s for 500 nm PMMA beads imaging with a field of view of around 60 μm and a SNR of 31 (Figure S3). Collectively, these optimizations were essential to adapt the technique for high-throughput bacterial metabolic phenotyping.

The MIP−FISH microscope is schematically shown in Figure 1A. Briefly, a fluorescence module was integrated into the MIP microscope sharing the visible illumination. The mid-IR pulses are modulated with an optical chopper to a burst of pules matching the camera frame rate. In this work, we focused on imaging of the fluorophores $\mathrm { C y } 3$ and $\mathrm { C y } 5 ,$ , which are widely used for FISH-based detection of microbes. The 520 nm nanosecond probe source also served as the $\mathrm { C y } 3$ fluorophore excitation source. The $\mathrm { C y } 5$ fluorophore was excited with a second visible beam with a center wavelength of 638 nm aligned with the 520 nm laser. Due to the different requirement of MIP and FISH imaging for cameras, we separated the two detection paths and used two cameras for recording the sample scattered light and the fluorophoreemitted light. For the bacteria taxa-specific fluorescence detection from FISH, we chose a camera with high quantum efficiency and low readout noise for the low photon-budget condition. The metabolic activity of the cells was characterized by two IR wavenumber MIP imaging (Figure 1B), while the identity of the cells was provided by two-color fluorescence imaging (Figure 1C).

High-Throughput, High-Sensitivity Metabolic Imaging of Protein Synthesis in Bacteria by Widefield MIP. The incorporation of isotopes into cellular biomass leads to shifts in the IR absorption peaks to a lower wavenumber and has been observed for various isotopes and organisms.32,55 The effect of $^ { 1 3 } \mathrm { C }$ incorporation by cells was previously demonstrated in a point-scan MIP system.35,56,57 Here, we use E. coli cells to demonstrate the capability of widefield MIP to image the metabolism of $^ { 1 3 } \mathrm { C }$ from isotopically labeled compounds by bacteria. Glucose is a widely used energy source of bacteria, and various amino acids can be synthesized from glucose. Therefore, we selected 13C-labeled glucose as a model substrate for this study.

We imaged the cells under the MIP−FISH microscope (Figure 2). The rod shape of the individual E. coli was clearly shown in both the reflection and MIP images. We acquired multispectral widefield MIP images covering the protein amide I and amide II regions (1512 to $1 7 6 8 ~ \mathrm { { c m } ^ { - 1 } ) }$ for the unlabeled glucose $\left( ^ { 1 2 } \mathrm { C - g l u c o s e } \right)$ and $^ { 1 3 } \mathrm { C }$ -labeled glucose $\left( ^ { 1 3 } { \bf C } { \cdot } { \bf g l u c o s e } \right)$ - incubated cells (Figure S2). The $^ { \mathrm { f } _ { 2 } } \mathrm { C } .$ -glucose-incubated bacteria showed a protein amide I peak at around 1656 $\mathrm { c m } ^ { - 1 } ,$ , while the protein amide I peak for $^ { 1 3 } { \mathrm { C } } .$ -glucose-incubated bacteria was around $1 6 1 2 ~ \mathrm { { c m } ^ { - 1 } . }$ . The amide II peak also showed the isotopic effect with a smaller shift from 1548 to $1 5 3 2 ~ \mathrm { c m } ^ { - 1 }$ . The spectra from the cell-free background region showed no contrast, suggesting negligible effect from poly-Llysine coating. We selected two key wavenumbers representing the $^ { 1 2 } { \mathrm { C } } \cdot$ -protein $( 1 6 5 6 ~ \mathrm { c m ^ { - 1 } }$ , original amide I band) and $^ { 1 3 } \mathrm { C } \cdot$ protein $\bar { ( } 1 6 1 2 ~ \mathrm { c m } ^ { - 1 }$ , shifted amide I band) and recorded MIP images (Figure $^ { 2 \mathrm { B } , \mathrm { C } , \mathrm { E } , \mathrm { F } ) }$ . For the cells incubated with $^ { 1 2 } \mathrm { C } \mathrm { - }$ glucose, a higher intensity was observed at $1 6 5 6 ~ \mathrm { { c m } ^ { - 1 } }$ . For the cells incubated with $^ { 1 3 } \mathrm { C }$ -glucose, a higher intensity was observed at $1 6 1 2 ~ \mathrm { { c m } ^ { - 1 } }$ for the shifted amide I band, indicating the incorporation of the heavier carbon atoms into the protein. Due to the high throughput of widefield MIP, we were able to acquire high-SNR MIP images of up to hundreds of bacteria within $2 . 4 { \mathrm { ~ s } } .$ .

To quantify the percentage of the $^ { 1 3 } \mathrm { C }$ -protein in the whole protein pool, we defined a $^ { 1 3 } \mathrm { C } .$ -protein replacement ratio (Experimental Section and Figure S1). The estimated $^ { 1 3 } \mathrm { C } \mathrm { - }$ protein replacement ratio reaches 0.956 after 24 h based on the residual peak at $1 6 5 6 ~ \mathrm { { c m } ^ { - 1 } }$ (Figure S2), which could be considered as near-full substitution.

We further demonstrate the high detection limit of isotope incorporation for MIP. We incubated E. coli cells for 24 h with varying percentages of 13C-glucose contributing to the total pool of available carbon. The $^ { 1 3 } \mathrm { C } .$ -protein replacement ratio was calculated for each group and plotted as the function of percentage of $^ { 1 3 } \mathrm { C } .$ -glucose in the medium (Figure 3). The $^ { 1 3 } \mathrm { C } \mathrm { . }$ - protein replacement ratio increased as the percentage of $^ { 1 3 } \mathrm { C } \mathrm { - }$ glucose increased, and there was a clear linear correlation $\left( R ^ { 2 } = \right.$ 0.9982) between the concentration of $^ { 1 3 } \mathrm { C }$ -glucose and the incorporation of $^ { 1 3 } \mathrm { C }$ into the cellular protein. Notably, a significant difference was observed for 0 and 5% 13C-glucose incubation (pairwise t-test, $p = 3 . 8 6 \times 1 0 ^ { - 2 2 } )$ . In comparison, with spontaneous Raman spectroscopy, a detection limit of 8% has been described for recording deuterium incorporation in microbial biomass.21 It should be noted that a relative low percentage of heavy water in Raman-based measurement is used to avoid potential inhibitory effects.21 Here, we observed no differences in growth or cell morphology that could reflect toxicity, even when all carbon source available was in the form of 13C-glucose (100% 13C-glucose). This is in agreement with literature reporting that incorporation of 13C-glucose shows negligible influence on cell metabolism and physiology. 58

Heterogeneity in $^ { 1 3 } \mathrm { C }$ incorporation was observed for the 13C-protein replacement ratio within each individual incubation group, despite the fact that cells were derived from an isogenic microbial population. To understand the origin of this heterogeneity, we performed multispectral MIP imaging on standard samples including polymer beads (PMMA beads 500 nm in diameter) and on a bovine serum albumin (BSA) film and calculated the mock ratio by applying a similar analysis as for the $^ { 1 3 } \mathrm { C }$ -protein replacement ratio (Figure S4 and Table S4). The standard deviation for these mock ratios from the PMMA beads and BSA film is 5 times smaller than that of the $E .$ coli samples, indicating that the $^ { 1 3 } \mathrm { C } .$ -protein replacement ratio fluctuation originated indeed mostly from phenotypic heterogeneity. This is not unexpected in batch incubations with the resulting physicochemical differences.

Microbial Identification and Metabolism Analysis with MIP−FISH. To evaluate the capacity of MIP−FISH to simultaneously retrieve information on cellular metabolism and identity of the analyzed bacterial cells, we initially imaged E.

coli cells that were stained by FISH with the oligonucleotide probe $\mathrm { G a m } 4 2 \mathrm { a - C y } 5$ (Figure 4 and Table S1). We acquired the FISH and MIP images sequentially with FISH imaging first to avoid photo bleaching. Hybridized cells showed a clear signal on the fluorescence $\mathrm { C y } 5$ channel that overlaps well with the MIP images. As expected, in control experiments, no fluorescence signal could be detected in cells that were not hybridized. We observed for hybridized as well as nonhybridized cells higher IR intensities at $1 6 1 2 ~ \mathrm { { c m } ^ { - 1 } }$ for cells grown in a $^ { 1 3 } \mathrm { C }$ -glucose-containing medium (Figure 4). By calculating the 13C-protein replacement ratio, a difference in cells grown with unlabeled glucose and $^ { \mathrm { i } _ { 3 } } \mathrm { C } .$ -glucose was observed, as expected. However, the FISH process slightly reduced the $^ { 1 3 } \mathrm { C } ^ { \bullet }$ protein replacement ratio (7.5% on average; Figure 4J). We also observed a higher than the 0 13C-protein replacement ratio for $^ { 1 2 } \mathrm { C }$ -glucose-incubated cells with FISH labeling (Figure S5). One potential reason can be that the selective loss of the cellular protein during the hybridization and washing steps of the FISH protocol leads to an overall amide I intensity decrease, changing the quantification coefficients. An effect of the FISH protocol on quantification of isotope incorporation within microbial cells has been previously reported for other vibrational spectroscopy-based methods.20,21 Therefore, we acquired coefficients for different cultures and treatment conditions to obtain a more accurate result (Table S2). Additionally, we observed no statistically significant difference between FISH probe Gam42a (specifically bind to E. coli rRNA) and FISH probe non-EUB (negative control, no binding), suggesting that the binding of rRNA-targeted probes will not influence our protein quantification.

We further tested the capacity of MIP−FISH to identify bacterial taxa and their metabolic status on multi-species samples. We started by using an artificial mixture of two common human gut microbiome members: E. coli and B. thetaiotaomicron (B. theta). E. coli cells grown in the presence $\mathrm { o f } ~ ^ { 1 3 } \mathrm { C }$ -glucose were hybridized with the Gam42a−Cy5 probe, while B. theta cells were grown with 12C-glucose and hybridized with the $\mathrm { B a c } 3 \bar { 0 } 3 \mathrm { - } \mathrm { C y } 3$ probe $\tilde { ( \mathrm { T a b l e } \Delta } 1 )$ . Subtraction of MIP images at 1612 and 1656 $\mathrm { c m } ^ { - 1 }$ revealed that a fraction of the cells on this two-species sample displayed positive subtraction values (Figure 5B, yellow color), indicative of $^ { 1 3 } \mathrm { C } .$ -glucose incorporation, while the majority of the remaining cells displayed negative values (Figure 5B, blue color). From the subtraction results and the growth conditions, we inferred that cells with a positive contrast were E. coli and the cells with a negative contrast were B. theta. However, since both E. coli and B. theta are rod-shaped bacteria of similar size, we were not able to differentiate them based on morphology (Figure 5C). Benefiting from the fluorescence imaging capability of MIP−FISH and the ability of rRNA-targeted FISH to discriminate bacterial taxa, we could confirm that cells with a positive contrast were E. coli as these displayed a $\mathrm { C y } 5$ fluorescence signal resulting from hybridization with the $\mathrm { G a m } 4 2 \mathrm { a - C y } 5$ probe (Figure ${ \mathsf { S A } } ,$ red color). In contrast, B. theta cells displaying $\texttt { a } \thinspace \mathrm { C y } 3$ signal that originated from hybridization with the Bacteroidales probe $\mathrm { B a c } 3 0 3 \mathrm { - C y } 3$ (Figure ${ \mathsf { S A } } ,$ green color) exhibited negative subtraction values. Finally, the $^ { 1 3 } \mathrm { C }$ -protein replacement ratio was calculated (Figure 5D) and showed a significant difference between the two species (pairwise t-test, $\begin{array} { r } { p = 9 . 7 4 \times 1 0 ^ { - 3 3 } ) } \end{array}$ . A similar differentiation was observed for the opposite combination (E. coli incubated in $^ { 1 2 } { \mathrm { C } } { \mathrm { . } }$ -glucose and FISH-labeled with $\mathrm { C y } 5 ,$ B.

theta incubated in $^ { 1 3 } \mathrm { C } .$ -glucose and FISH-labeled with $\mathrm { C y } 3 ,$ Figure S6). Our results demonstrated that MIP−FISH is suitable to efficiently distinguish cells with $^ { 1 3 } \mathrm { C } .$ -induced protein peak shifts in mixed samples.

To test the performance of MIP−FISH beyond simple mixtures of bacteria and to demonstrate that it can be applied to identify microbes and retrieve metabolic information in a complex microbiome sample, we imaged a mixture of $^ { 1 3 } \mathrm { C } .$ cYanmaGntaYelowb labeled E. coli and a human gut microbiome sample. The human large intestine is inhabited by trillions of gut microbes that perform a range of metabolic functions important for host health. We have therefore tested the suitability of MIP−FISH to investigate the microbial metabolism of isotopically labeled compounds in such a complex setting. MIP−FISH successfully enabled us to identify E. coli cells grown with $^ { 1 3 } \mathrm { C }$ -glucose and hybridized with a Gam42a−Cy5 probe in a gut microbiome sample that had been incubated with $^ { 1 2 } { \mathrm { C } } { \cdot } { \mathrm { g l } }$ ucose. The 1612 and $1 6 5 6 ~ \mathrm { ~ c m ^ { - 1 } }$ subtraction results (Figure 6B) and quantitative calculation of the $^ { 1 3 } \mathrm { C } .$ -protein replacement ratio (Figure 6D) together with fluorescence imaging showed the assimilation of 13C-glucose into protein for E. coli but not for other gut microbiome members (Figure 6A). As the gut microbiome contains many different microbial taxa, we measured a large number of cells $\left( n \ = \ 5 9 3 \right)$ to cover a majority of the species. From the replacement ratio analysis (Figure 6D), we observed a larger standard deviation when compared to pure bacteria sample; however, different gut microbiome member constitutions have no strong effect on differentiation between fully labeled and unlabeled cells. Together, these data show the applicability of MIP−FISH to a complex microbiome sample.

## CONCLUSIONS

In this study, we developed a MIP−FISH platform for in situ bacteria identification and metabolic imaging in a high throughput manner with single-cell resolution. Benefiting from the high compatibility of MIP, we coupled a fluorescence module to a widefield MIP setup for fluorescence imaging of bacterial species hybridized with fluorescently labeled oligonucleotide probes. We demonstrated the potential for applying MIP−FISH on multi-species communities and complex samples and observed good correlations between MIP metabolic imaging and FISH imaging. As a proof of concept, we successfully applied MIP−FISH to image the microbial assimilation of $^ { 1 3 } \dot { C }$ from labeled glucose. In pure culture experiments, high sensitivity was achieved with a detection limit of 5% of $^ { \circ } { } ^ { 1 3 } \mathrm { C }$ in total carbon. In the complex microbiome sample containing many different unlabeled microbial taxa with different chemical cellular compositions, the background signal in the selected regions for the MIPbased detection $\mathrm { o f } ^ { \mathrm { 1 3 } } \mathrm { C }$ -incorporation into proteins was higher, but unambiguous detection of spiked fully labeled E. coli cells was nevertheless possible. Microbial taxa with different physiologies and in distinct environments may display variable $^ { \mathbf { i } _ { 3 } } \dot { \mathrm { C } }$ incorporation levels and may never achieve full $^ { 1 3 } \mathrm { C } \mathrm { - }$ labeling. Under these circumstances, it would be important to first evaluate if MIP−FISH is able to unambiguously discriminate $^ { 1 3 } \mathrm { C }$ -labeled and $^ { 1 2 } \mathrm { C }$ -labeled cells of a taxa of interest in the context of a complex community.

Keeping in mind that the protein amide II band involves nitrogen, in future studies, MIP−FISH might also be suitable to study the assimilation of nitrogen-containing compounds using $\mathrm { i } 5 _ { \mathrm { N } }$ -labeled substrates. More generally, this newly developed platform should now be ready to interrogate assimilation of many key substrates by human gut microbiome members including sweeteners, prebiotics, or even human targeted drugs.

It is worth to compare MIP−FISH with other single-cell vibrational spectroscopy or IR-based metabolic characterization platforms for single-cell isotope probing of microbes. Single-cell spontaneous Raman spectroscopy offers a fullspectral coverage, but strong fluorescence background could complicate the spectral analysis .21,31,59,60 The throughput of Raman measurement is drastically improved by SRS at the cost of more expensive and complicated instrumentation, as well as limited spectral coverage.20 Additionally, it is harder to resolve 13C and 15N assimilation than 2 H as the isotopic effect of 13C and 15N is relatively small and often buried in the Raman fingerprint region.59 On the other hand, IR offers a higher signal in the fingerprint region,61 which makes MIP a more suitable tool for high-throughput characterization of 13C and 15N assimilation in microbial cells. Additionally, widefield MIP provides a similar imaging speed to SRS, along with compactness, cost-effectiveness, and high compatibility with fluorescence merits.

We envision that the MIP−FISH platform will amend the toolbox of microbial ecologists and microbiome researchers that aim to simultaneously investigate the identity and function of individual microbial cells. Furthermore, this technique might also be useful for rapidly determining the antibiotic resistance of microbial cells in complex samples62−67 Finally, as a non destructive single-cell analytic tool, it should be feasible in the future to integrate MIP imaging with other genotyping methods beyond FISH, such as cell-sorting and whole-genome sequencing.68

## ASSOCIATED CONTENT

## \*sı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.analchem.2c04474.

Data processing pipeline for metabolism quantification, multispectral widefield MIP imaging of unlabeled and 13C-labeled glucose-incubated E. coli cells, ultrafast MIP imaging 500 nm PMMA beads, multispectral imaging of the standard sample, influence of the FISH protocol on quantification, FISH probes used for single-cell analysis, reference coefficients for quantification, reference coefficients variation between measurements, mock ratio of standard samples, FISH procedure, and gut microbiome incubation (PDF)

## AUTHOR INFORMATION

## Corresponding Authors

Michael Wagner − Centre for Microbiology and Environmental Systems Science, Department of Microbiology and Ecosystem Science, University of Vienna, Vienna 1030, Austria; Department of Chemistry and Bioscience, Aalborg University, Aalborg 9220, Denmark; Email: michael.wagner@univie.ac.at

Ji-Xin Cheng − Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, United States; Department of Biomedical Engineering and Photonics Center, Boston University, Boston, Massachusetts 02215, United States; orcid.org/0000-0002-5607-6683; Email: jxcheng@bu.edu

## Authors

Yeran Bai − Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, United States; Photonics Center, Boston University, Boston, Massachusetts 02215, United States; Present Address: Neuroscience Research Institute, University of California, Santa Barbara, CA 93106, USA

Zhongyue Guo − Department of Biomedical Engineering and Photonics Center, Boston University, Boston, Massachusetts 02215, United States

Fátima C. Pereira − Centre for Microbiology and Environmental Systems Science, Department of Microbiology and Ecosystem Science, University of Vienna, Vienna 1030, Austria; Present Address: Molecular and Cellular Biosciences, University of Southampton, Southampton, SO17 1BJ, United Kingdom.

Complete contact information is available at: https://pubs.acs.org/10.1021/acs.analchem.2c04474

## Author Contributions

\# Y.B. and Z.G. contributed equally to the work.

## Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

This work was supported by the National Institutes of Health (NIH) R35GM136223, R01AI141439 to J.X.C. Funding for the presented research was also provided via Young Independent Research Group Grant ZK-57 to F.C.P. M.W. was supported by the Wittgenstein award of the Austrian Science Fund FWF (Z-383B).

## REFERENCES

(1) Lim, B.; Lin, Y.; Navin, N. Cancer Cell 2020, 37, 456−470.  
(2) Morris, S. A. Development 2019, 146, 169748.  
(3) Efremova, M.; Vento-Tormo, R.; Park, J.-E.; Teichmann, S. A.; James, K. R. Annu. Rev. Immunol. 2020, 38, 727−757.  
(4) Saadatpour, A.; Lai, S.; Guo, G.; Yuan, G. C. Trends Genet. 2015, 31, 576−586.  
(5) Heath, J. R.; Ribas, A.; Mischel, P. S. Nat. Rev. Drug Discovery 2016, 15, 204216.  
(6) Taheri-Araghi, S.; Brown, S. D.; Sauls, J. T.; McIntosh, D. B.; Jun, S. Annu. Rev. Biophys. 2015, 44, 123−142.  
(7) Ye, Z.; Sarkar, C. A. Trends Cell Biol. 2018, 28, 1030−1048.  
(8) Ackermann, M. Nat. Rev. Microbiol. 2015, 13, 497−508.  
(9) Sampaio, N. M. V.; Dunlop, M. J. Curr. Opin. Microbiol. 2020, 57, 87−94.  
(10) Lidstrom, M. E.; Konopka, M. C. Nat. Chem. Biol. 2010, 6, 705−712.  
(11) Hare, P. J.; LaGree, T. J.; Byrd, B. A.; DeMarco, A. M.; Mok, W. W. K. Microorganisms 2021, 9, 2277.  
(12) Hatzenpichler, R.; Krukenberg, V.; Spietz, R. L.; Jay, Z. J. Nat. Rev. Microbiol. 2020, 18, 241−256.  
(13) Hu, Y.; An, Q.; Sheu, K.; Trejo, B.; Fan, S.; Guo, Y. Front. Cell Dev. Biol. 2018, 6, 28.  
(14) Kalisky, T.; Quake, S. R. Nat. Methods 2011, 8, 311−314.  
(15) Kashima, Y.; Sakamoto, Y.; Kaneko, K.; Seki, M.; Suzuki, Y.; Suzuki. A. ExpMol. Med. 2020. 52, 14191427.  
(16) Wagner, M. Annu. Rev. Microbiol. 2009, 63, 411−429.  
(17) Zenobi, R. Science 2013, 342, 1243259.  
(18) Evers, T. M. J.; Hochane, M.; Tans, S. J.; Heeren, R. M. A.; Semrau, S.; Nemes, P.; Mashaghi, A. Anal. Chem. 2019, 91, 13314− 13323.  
(19) Lee, K. S.; Pereira, F. C.; Palatinszky, M.; Behrendt, L.; Alcolombri, U.; Berry, D.; Wagner, M.; Stocker, R. Nat. Protoc. 2021, 16, 634−676.  
(20) Ge, X.; Pereira, F. C.; Mitteregger, M.; Berry, D.; Zhang, M.; Hausmann, B.; Zhang, J.; Schintlmeister, A.; Wagner, M.; Cheng, J. X. Proc. Natl. Acad. Sci. U. S. A. 2022, 119, No. e2203519119.  
(21) Berry, D.; Mader, E.; Lee, T. K.; Woebken, D.; Wang, Y.; Zhu, D.; Palatinszky, M.; Schintlmeister, A.; Schmid, M. C.; Hanson, B. T.; Shterzer, N.; Mizrahi, I.; Rauch, I.; Decker, T.; Bocklitz, T.; Popp, J.; Gibson, C. M.; Fowler, P. W.; Huang, W. E.; Wagner, M. Proc. Natl. Acad. Sci. U. S. A. 2015, 112, E194−E203.  
(22) Lee, K. S.; Palatinszky, M.; Pereira, F. C.; Nguyen, J.; Fernandez, V. I.; Mueller, A. J.; Menolascina, F.; Daims, H.; Berry, D.; Wagner, M.; Stocker, R. Nat. Microbiol. 2019, 4, 1035−1048.  
(23) Muhamadali, H.; Chisanga, M.; Subaihi, A.; Goodacre, R. Anal. Chem. 2015, 87, 4578−4586.  
(24) Tao, Y.; Wang, Y.; Huang, S.; Zhu, P.; Huang, W. E.; Ling, J.; Xu, J. Anal. Chem. 2017, 89, 4108−4115.  
(25) Hong, W.; Karanja, C. W.; Abutaleb, N. S.; Younis, W.; Zhang, X.; Seleem, M. N.; Cheng, J. X. Anal. Chem. 2018, 90, 3737−3743.  
(26) Yang, K.; Li, H. Z.; Zhu, X.; Su, J. Q.; Ren, B.; Zhu, Y. G.; Cui, L. Anal. Chem. 2019, 91, 6296−6303.  
(27) Zhang, M.; Hong, W.; Abutaleb, N. S.; Li, J.; Dong, P. T.; Zong, C.; Wang, P.; Seleem, M. N.; Cheng, J. X. Adv. Sci. (Weinheim, Ger.) 2020, 7, 2001452.  
(28) Lima, C.; Muhamadali, H.; Xu, Y.; Kansiz, M.; Goodacre, R. Anal. Chem. 2021. 93. 30823088.  
(29) Yi, X.; Song, Y.; Xu, X.; Peng, D.; Wang, J.; Qie, X.; Lin, K.; Yu, M.; Ge, M.; Wang, Y.; Zhang, D.; Yang, Q.; Wang, M.; Huang, W. E. Anal. Chem. 2021, 93, 5098−5106.  
(30) Lee, K. S.; Landry, Z.; Pereira, F. C.; Wagner, M.; Berry, D.; Huang, W. E.; Taylor, G. T.; Kneipp, J.; Popp, J.; Zhang, M. Nat. Rev. Methods Primers 2021, 1, 80.  
(31) Huang, W. E.; Stoecker, K.; Griffiths, R.; Newbold, L.; Daims, H.; Whiteley, A. S.; Wagner, M. Environ. Microbiol. 2007, 9, 1878− 1889.  
(32) Muhamadali, H.; Chisanga, M.; Subaihi, A.; Goodacre, R. Anal. Chem. 2015, 87, 4578−4586.  
(33) Dazzi, A.; Prater, C. B.; Hu, Q.; Chase, D. B.; Rabolt, J. F.; Marcott, C. Appl. Spectrosc. 2012, 66, 1365−1384.  
(34) Baker, M. J.; Trevisan, J.; Bassan, P.; Bhargava, R.; Butler, H. J.; Dorling, K. M.; Fielden, P. R.; Fogarty, S. W.; Fullwood, N. J.; Heys, K. A.; Hughes, C.; Lasch, P.; Martin-Hirsch, P. L.; Obinaju, B.; Sockalingum, G. D.; Sulé-Suso, J.; Strong, R. J.; Walsh, M. J.; Wood, B. R.; Gardner, P.; Martin, F. L. Nat. Protoc. 2014, 9, 1771−1791.  
(35) Bai, Y.; Yin, J.; Cheng, J.-X. Sci. Adv. 2021, 7, No. eabg1559. (36) Li, Z.; Aleshire, K.; Kuno, M.; Hartland, G. V. J. Phys. Chem. B 2017. 121, 88388846  
(37) Li, C.; Zhang, D.; Slipchenko, M. N.; Cheng, J.-X. Anal. Chem. 2017, 89, 48634867.  
(38) Bai, Y.; Zhang, D.; Li, C.; Liu, C.; Cheng, J. X. J. Phys. Chem. B 2017, 121, 10249−10255.  
(39) Zhang, D.; Li, C.; Zhang, C.; Slipchenko, M. N.; Eakins, G.; Cheng, J.-X. Sci. Adv. 2016, 2, No. e1600521.  
(40) Pavlovetc, I. M.; Podshivaylov, E. A.; Chatterjee, R.; Hartland, G. V.; Frantsuzov, P. A.; Kuno, M. J. Appl. Phys. 2020, 127, 165101.  
(41) Bai, Y.; Zhang, D.; Lan, L.; Huang, Y.; Maize, K.; Shakouri, A.; Cheng, J.-X. Sci. Adv. 2019, 5. No. eaav7127.  
(42) Yin, J.; Lan, L.; Zhang, Y.; Ni, H.; Tan, Y.; Zhang, M.; Bai, Y.; Cheng. J. X. Nat. Commun. 2021. 12. 7097.  
(43) Lim, J. M.; Park, C.; Park, J. S.; Kim, C.; Chon, B.; Cho, M. J. Phys. Chem. Lett. 2019, 10, 2857−2861.  
(44) Klementieva, O.; Sandt, C.; Martinsson, I.; Kansiz, M.; Gouras, G. K.; Borondics, F. Adv. Sci. (Weinheim, Ger.) 2020, 7, 1903004.  
(45) Schnell, M.; Mittal, S.; Falahkheirkhah, K.; Mittal, A.; Yeh, K.; Kenkel, S.; Kajdacsy-Balla, A.; Carney, P. S.; Bhargava, R. Proc. Natl. Acad. Sci. U. S. A. 2020, 117, 3388−3396.  
(46) Mankar, R.; Gajjela, C. C.; Bueso-Ramos, C. E.; Yin, C. C.; Mayerich, D.; Reddy, R. K. Appl. Spectrosc. 2022, 76, 508−518.  
(47) Zhang, Y.; Yurdakul, C.; Devaux, A. J.; Wang, L.; Xu, X. G.; Connor, J. H.; Ünlü, M. S.; Cheng, J.-X. Anal. Chem. 2021, 93, 4100− 4107.  
(48) Xu, J.; Li, X.; Guo, Z.; Huang, W. E.; Cheng, J.-X. Anal. Chem.2020, 92, 14459−14465.  
(49) Li, X.; Zhang, D.; Bai, Y.; Wang, W.; Liang, J.; Cheng, J.-X. Anal. Chem. 2019, 91, 10750−10756.  
(50) Zhang, Y.; Zong, H.; Zong, C.; Tan, Y.; Zhang, M.; Zhan, Y.; Cheng, J.-X. J. Am. Chem. Soc. 2021, 143, 11490−11499.  
(51) Li, M.; Razumtcev, A.; Yang, R.; Liu, Y.; Rong, J.; Geiger, A. C.; Blanchard, R.; Pfluegl, C.; Taylor, L. S.; Simpson, G. J. J. Am. Chem. Soc. 2021, 143, 10809−10815.  
(52) Wagner, M.; Haider, S. Curr. Opin. Biotechnol. 2012, 23, 96− 102.  
(53) Bacic, M. K.; Smith, C. J. Curr. Protoc. Microbiol. 2008, 9, 13C 1.  
(54) Zong, H.; Yurdakul, C.; Bai, Y.; Zhang, M.; Ü nlü, M. S.; Cheng, J.-X. ACS Photonics 2021, 8, 3323−3336.  
(55) Shi, L.; Liu, X.; Shi, L.; Stinson, H. T.; Rowlette, J.; Kahl, L. J.; Evans, C. R.; Zheng, C.; Dietrich, L. E.; Min, W. Nat. Methods 2020, 17, 844−851.  
(56) Lima, C.; Muhamadali, H.; Xu, Y.; Kansiz, M.; Goodacre, R. Anal. Chem. 2021, 93, 3082−3088.  
(57) Lima, C.; Muhamadali, H.; Goodacre, R. Sensors 2022, 22, 3928.  
(58) Sandberg, T. E.; Long, C. P.; Gonzalez, J. E.; Feist, A. M.; Antoniewicz, M. R.; Palsson, B. O. PLoS One 2016, 11, No. e0151130.  
(59) Wang, Y.; Huang, W. E.; Cui, L.; Wagner, M. Curr. Opin. Biotechnol. 2016, 41, 34−42.  
(60) Huang, W. E.; Ferguson, A.; Singer, A. C.; Lawson, K.; Thompson, I. P.; Kalin, R. M.; Larkin, M. J.; Bailey, M. J.; Whiteley, A. S. Appl. Environ. Microbiol. 2009, 75, 234−241.  
(61) Ma, J.; Pazos, I. M.; Zhang, W.; Culik, R. M.; Gai, F. Annu. Rev. Phys. Chem. 2015, 66, 357.  
(62) Arnoldini, M.; Vizcarra, I. A.; Peña-Miller, R.; Stocker, N.; Diard, M.; Vogel, V.; Beardmore, R. E.; Hardt, W. D.; Ackermann, M. PLoS Biol. 2014, 12, No. e1001928.  
(63) Balaban, N. Q.; Merrin, J.; Chait, R.; Kowalik, L.; Leibler, S. Science 2004, 305, 1622−1625.  
(64) Chua, S. L.; Yam, J. K.; Hao, P.; Adav, S. S.; Salido, M. M.; Liu, Y.; Givskov, M.; Sze, S. K.; Tolker-Nielsen, T.; Yang, L. Nat. Commun. 2016, 7, 10750.  
(65) Wakamoto, Y.; Dhar, N.; Chait, R.; Schneider, K.; Signorino Gelo, F.; Leibler, S.; McKinney, J. D. Science 2013, 339, 91−95.  
(66) Lee, J. J.; Lee, S. K.; Song, N.; Nathan, T. O.; Swarts, B. M.; Eum, S. Y.; Ehrt, S.; Cho, S. N.; Eoh, H. Nat. Commun. 2019, 10, 2928.  
(67) Levy, S. F.; Ziv, N.; Siegal, M. L. PLoS Biol. 2012, 10, No. e1001325.  
(68) Hatzenpichler, R.; Connon, S. A.; Goudeau, D.; Malmstrom, R. R.; Woyke, T.; Orphan, V. J. Proc. Natl. Acad. Sci. U. S. A. 2016, 113, E4069−E4078.