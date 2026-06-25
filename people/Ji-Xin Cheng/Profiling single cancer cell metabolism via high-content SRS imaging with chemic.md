## CA N C E R

# Profiling single cancer cell metabolism via high-content SRS imaging with chemical sparsity

Yuying Tan1 †, Haonan Lin1 †, Ji-Xin Cheng1,2,3\*

Metabolic reprogramming in a subpopulation of cancer cells is a hallmark of tumor chemoresistance. However, single-cell metabolic profiling is difficult because of the lack of a method that can simultaneously detect multiple metabolites at the single-cell level. In this study, through hyperspectral stimulated Raman scattering (hSRS) imaging in the carbon-hydrogen (C–H) window and sparsity-driven hyperspectral image decomposition, we demonstrate a high-content hSRS (h2 SRS) imaging approach that enables the simultaneous mapping of five major biomolecules, including proteins, carbohydrates, fatty acids, cholesterol, and nucleic acids at the single-cell level. h2 SRS imaging of brain and pancreatic cancer cells under chemotherapy revealed acute and adapted chemotherapy-induced metabolic reprogramming and the unique metabolic features of chemoresistance. Our approach is expected to facilitate the discovery of therapeutic targets to combat chemoresistance. This study illustrates a high-content, label-free chemical imaging approach that measures metabolic profiles at the single-cell level and warrants further research on cellular metabolism.

Copyright © 2023 The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original U.S. Governmen Works. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC)

## INTRODUCTION

Although chemotherapy remains a commonly used anticancer treatment for various cancers (1), the development of chemoresist ance has become a major challenge for current cancer therapies and contributes significantly to tumor relapses and deaths (2). Alterna tions in multiple metabolites have been found in several chemore sistant cancers that facilitate tumor cell survival under chemostress (3, 4). In tamoxifen-resistant breast cancer, a tremendous increase in neutral lipids in the form of droplets and the accumulation of free cholesterol in lysosomes has been observed (5), and cholesterol and lipid pathways are up-regulated by the oncoprotein MUC-1 (6). Hamadneh et al. identified glucose and glutamine metabolic dysfunction in the development of tamoxifen resistance in breast cancer (7). In lung cancer, membrane lipid composition has been reported to be associated with cisplatin resistance in lung adenocar cinoma (8), whereas cholesterol has been identified to contribute to the development of cisplatin resistance in lung adenocarcinoma through ABCG2 up-regulation (9). A notable increase in lipidrich protrusions and cholesteryl ester levels has been observed in gemcitabine-treated and gemcitabine-resistant pancreatic cancer (10, 11). Recently, a metabolic switch from glycolysis to fatty acid uptake and β-oxidation was identified as a hallmark of cisplatin-resistant ovarian cancer, supporting a therapeutic target and detec tion method for cisplatin-resistant ovarian cancer (12). These studies imply that the reprogramming of multiple metabolites i common in the development of cancer chemoresistance, facilitating tumor cell survival during chemotherapy.

Cell metabolic profiling is commonly performed through indi rect measurements of metabolite-related gene expression, enzyme protein levels, or functional assays, such as Seahorse (12–14). Alternatively, mass spectroscopy can provide direct metabolic measurements and has made prominent achievements in cancer metabolism studies (15, 16). However, these methods involve bulk measure ments of millions of cells, which potentially mask the metabolic var iations of subpopulations in highly heterogeneous cancer cel environments (17–19). Fluorescence-based flow cytometry and imaging can be used to study single-cell metabolism by providing information on fluorescently labeled organelles or metabolites within individual cells. However, labeling probes may eithe perturb or tag small metabolites such as carbohydrates (20). Fo the single-cell labeling of multiple metabolites, broad fluorescence emission spectra pose another challenge in resolving the species.

Coherent Raman scattering microscopy is a high-speed label free chemical imaging modality. It is capable of mapping metabo lites based on their intrinsic Raman spectroscopic signatures (21, 22). Coherent anti-Stokes Raman scattering (CARS) microscopy has been used to study lipid storage in aggressive cancers (23–26). Compared to CARS, stimulated Raman scattering (SRS) is free of the nonresonant background and scales linearly with molecula concentrations, providing better contrast and facilitating more quantitative analysis (27). The integration of single-color SRS imaging and spontaneous Raman spectroscopy revealed cholesterol ester as an aggressiveness marker for prostate cancer (28) and pan creatic cancer (29). To resolve multiple metabolites with overlap ping Raman features, hyperspectral SRS (hSRS) has been developed through pulse shaping (30, 31), spectral multiplexing (32, 33), or spectral focusing (34, 35). To date, hSRS has reached a subsecond imaging speed with spectral coverage of more than 200 cm−1 and spectral resolution of less than 10 $\mathrm { c m } ^ { - 1 }$ (36). Via downstream spectral analysis methods such as least squares (LS) fitting (37), principal components analysis (38), independent component analysis (30), multivariate curve resolution (MCR) (31), and phasor segmentation (39), hSRS can distinguish intracellular bio molecules including fatty acid, nucleic acid, and protein in the signal-rich carbon-hydrogen (C–H) vibration region (10, 22, 40). hSRS imaging in the high–wave number C–H window revealed in creased lipid unsaturation as a marker of cancer stem cells (41). However, other essential metabolites such as carbohydrates and cholesterol remain challenging to study because their SRS signals

1 Biomedical Engineering, Boston University, Boston, MA 02155, USA. 2 Electrical and Computer Engineering, Boston University, Boston, MA 02155, USA. 3 Photonics Center, Boston University, Boston, MA 02155, USA. \*Corresponding author. Email: jxcheng@bu.edu †These authors contributed equally to this work.

are either weak in the fingerprint region or concealed in the crowded C–H region by other dominant biomolecules such as pro teins or lipids (36, 42). To date, newly synthesized carbohydrates have been studied using deuterium labeling (43), whereas cholesterol mapping has been reported in the 1650 cm−1 fingerprint region (44). To gain a complete picture of single-cell metabolic profiles and study cell metabolic switches in response to treatment, high-content imaging of multiple metabolites is highly desired.

Although fingerprint bands are informative, their cross sections are small. This leads to noisy measurements, making it difficult to differentiate less abundant metabolites from the noise. While broadband CRS covering the entire fingerprint region provides the potential for high-content imaging, the long acquisition time for integrating weak signals over a broad spectral window make it challenging to perform high-content and high-throughput mapping of the abovementioned biomolecules in single cells (45– 49). The high–wave number C–H bands can alleviate the sensitivity issue owing to their much larger cross section than the fingerprint bands. All major metabolic species, including proteins, nucleic acids, lipids, and glucose, exhibited the most essential yet overlap ping Raman peaks. However, existing hyperspectral data analytics approaches (30, 31, 37–39) cannot fully appreciate the rich content of C–H vibrations owing to notable cross-talk between the output chemical maps. An analysis that incorporates additional constraints to suppress cross-talk is required to deliver high-content chemical images in the C–H region.

It was observed that at an optical resolution of approximately 300 nm, within each spatial pixel, only a few metabolic species made dominant contributions. This physical condition can be incorporated as a sparsity constraint that limits the number of nonzero com ponents in each pixel. The sparsity constraint can be used to effectively suppress the spectral cross-talk by driving the inconse quential components to zero. Using this idea, we added the L1 norm to the component concentration vector at each pixel and in troduced a hyperspectral image unmixing method, termed pixel wise least absolute shrinkage and selection operator (LASSO) un mixing, to decompose hSRS into chemical concentration maps (50). Previously, LASSO was used in Raman spectroscopy as a feature selection tool to identify the most significant peaks that differentiate substances (49). Here, we present different uses of the pixel-wise LASSO for sparsity-driven linear unmixing. Using reference spectra from the components of interest, pixel-wise LASSO unmixing can separate the components in a complex spectral profile. Because LASSO provides soft thresholding for sparsity, it can be adjusted to unmix biomolecular signals even if they overlap spatially (50).

On the basis of this rationale, we describe a high-content hSRS (h2 SRS) imaging approach using hSRS imaging, block-matching and 4D filtering (BM4D) denoising (51) and pixel-wise LASSO spectral unmixing. Pixel-wise LASSO unmixing has previously been used in the $1 6 5 0 \mathrm { c m } ^ { - 1 }$ fingerprint region to generate chemical maps of proteins, lipids, and cholesterol (36). However, its potential to overcome spectral cross-talk in the high–wave number C–H vibration window for high-content metabolic imaging (up to five species) was demonstrated in this study. Using h2 SRS, we mapped the major biomolecules, including proteins, carbohydrates, fatty acids, cholesterol, and nucleic acids, within a single cancer cell line. Next, we examined metabolic alterations in cancer cells in response to chemotherapy. Specifically, we found increased intracellular fatty acid and carbohydrate levels in brain cancer cells, U-87 MG (U87), after cisplatin treatment, and in pancreatic cancer cells, Mia Paca2, after gemcitabine treatment. In addition, metabolism measured through high-content SRS imaging showed that the gemcitabine-resistant pancreatic cancer cell line G3K has higher amounts of carbohydrates, fatty acids, and cholesterol than its parental sensitive cell line Mia Paca2. These findings provide valuable insights into potential strategies for sensitizing drug-resis tant cancer cells to chemotherapy by targeting the most dramatic metabolic alterations.

## RESULTS

## Chemical sparsity constraints enable h2 SRS imaging in the high–wave number C–H window

To study the metabolic profiles of the major biomolecules (proteins, carbohydrates, fatty acids, cholesterol, and nucleic acids), we used bovine serum albumin (BSA), glucose, triglycerides (TAG), cholesterol, and purified RNA from cells as pure chemical spectral references. Their Raman spectra had the most substantial peaks in the C–H region, suggesting that it provides optimal signal fidelity for the h2 SRS imaging of metabolic profiles in cancer cells (Fig. 1A). In the C–H region, our lab-built SRS system reached a lateral spatial resolution of 306 nm with a 1.2–numerical aperture (NA) water immersion objective (fig. S1, A and B). By extensively chirp ing the pump and Stokes beams using 75 and 90 cm SF57 glass rods, respectively, a spectral resolution of $\stackrel { \smile } { 1 } 3 . 0 9 \mathrm { c m } ^ { - 1 }$ was achieved in the C–H region (fig. S1, C and D) (36). The high spatial resolution lays the physical foundation for chemical sparsity at each pixel, and the spectral resolution was sufficient to discriminate the overlapped peaks in the highly congested C–H region. Sparsity-constrained hy perspectral image unmixing via pixel-wise LASSO unmixing leverages the aforementioned instrumentation advances to fundamentally improve chemical resolving power. To apply h2 SRS imaging, we first obtained reference spectra from pure biomolecular samples (Fig. 1B), followed by hSRS imaging of the cells. As illustrated in Fig. 1C, we first unfolded a hyperspectral cell image stack into a data matrix D, in which the ith row $( \bar { D } _ { i , : } )$ represents the raw spectrum from pixel i. Given the spectral reference input matrix from the pure component spectra $\overset { \cdot } { ( } S ^ { T } )$ , pixel-wise LASSO solves the regression problem of fitting the concentrations of all components at pixel $i \left( C _ { i , : } \right)$ (see Materials and Methods for more details). The L1-norm sparsity regularization on vector $C _ { i , : }$ promotes that only a few components make dominant contributions at a pixel, as highlighted by the dashed circles in each row of the data matrix. After refolding the concentration matrix, the resulting chemical maps provided information on the concentration and spatial distribution of reference biomolecules (Fig. 1C). Using this hSRS-LASSO method, we simultaneously separated five biomole cules in single cells, including proteins, carbohydrates, fatty acids, cholesterol, and nucleic acids (Fig. 1D). Compared with previous postprocessing methods, such as LS fitting and MCR, pixel-wise LASSO unmixing showed notably improved chemical mapping results for nucleic acids, cholesterol, and carbohydrates in brain tumor U87 cells (Fig. 1D). The carbohydrate, cholesterol, and nucleic acid mappings analyzed through LS fitting and MCR were cross-talked and had noisy backgrounds probably because of the disturbance of inconsequential components in the LS fitting and the loss of reference spectrum accuracy for biomolecules with weaker signals in MCR (fig. S1E). In contrast, pixel-wise LASSO unmixing can filter out most of the background signal and has less cross-talk between channels because it uses a sparsity constraint to prevent spectral cross-talk and retains the accuracy of the reference spectra.

![](images/3483a590491bf925e60a9746686274ad712043e55f59b90f4b37829680f6d05a.jpg)  
Fig. 1. Sparsity constraints accompanied by improved spectral and spatial resolution enable $\scriptstyle \mathbf { h } ^ { 2 } \mathbf { S } \mathbf { R } \mathbf { S }$ imaging. (A) Raman spectra of BSA, glucose, TAG, cholesterol, and purified RNA from cells. (B) Normalized SRS spectra of BSA, glucose, TAG, cholesterol, and purified RNA from cells. (C) Schematic illustration of pixel-wise LASSO spectral unmixing for chemical mapping generation. $N _ { x } , N _ { y } ,$ and $N _ { \lambda }$ represent dimensions of the hyperspectral image, and $D , C ,$ and S stand for the data matrix, concen tration matrix, and spectral reference matrix, respectively. The circled elements represent the dominant components in each row. (D) Representative hSRS image (sum of all channels), mapped protein, carbohydrate, fatty acid, cholesterol, and nucleic acid images, as well as the merged image of metabolites mapping for U87 cells through LASSO, LS fitting, or MCR separation processing. Each channel has the same contrast and shares a color bar. The ranges of color bars are 0 to 150, 0 to 8, 0 to 3, 0 to 5, 0 to 2, and 0 to 0.6. Scale bar, 20 μm.

## $\boldsymbol { \mathsf { h } } ^ { 2 }$ SRS imaging accurately maps major intracellular biomolecules, including fatty acid, nucleic acid, protein, cholesterol, and carbohydrate

To further validate the accuracy of $\mathrm { h } ^ { 2 } \mathrm { S R S }$ imaging, we measured changes in the cell metabolic profile in response to environmenta nutrient variation. First, we cultured brain tumor cell U87 in a glucose-depleted medium. With pixel-wise LASSO unmixing, there was a clear decrease in the carbohydrate and lipid signals, whereas no obvious reduction was observed in the raw SRS images or output cholesterol and nucleic acid maps (Fig. 2A).

![](images/50a459150e50d15cf03fdeeeeb0f4d824f45631f44b6da4ef4bc9897c1b522d6.jpg)

<details>
<summary>text_image</summary>

A
SRS Protein Carbohydrate Fatty acid Cholesterol Nucleic acid Merged
Control
Glucose
depletion
</details>

![](images/22bfa330492162d20fbb9717736407d9fad989bd9525463831cfdfcfb40a3c13.jpg)

<details>
<summary>violin plot</summary>

| Protein / Carbohydrate / Fatty acid / Cholesterol | Control Mean Intensity (a.u.) | Glucose depletion Mean Intensity (a.u.) |
| -------------------------------------------------- | ----------------------------- | -------------------------------------- |
| Protein (Mean intensity)                            | ~0.8                          | ~0.6                                   |
| Carbohydrate (Mean intensity)                      | ~0.4                          | ~0.2                                   |
| Fatty acid (Mean intensity)                        | ~0.3                          | ~0.2                                   |
| Cholesterol (Mean intensity)                      | ~0.6                          | ~0.5                                   |
</details>

![](images/d47c60e811144e384319b63a70359ba505f23de47e626f3af81b46df866824b6.jpg)

<details>
<summary>text_image</summary>

C
SRS Protein Carbohydrate Fatty acid Cholesterol Nucleic acid Merged
Control
Glucose
depletion
</details>

![](images/e80c9ee68d853b85d6f8a0ad445d9cc020cc8dadd1e6a8e7d5896f0a05aa356f.jpg)

<details>
<summary>violin plot</summary>

| Protein / Carbohydrate / Fatty acid / Cholesterol | Control Mean Intensity (a.u.) | Glucose depletion Mean Intensity (a.u.) |
| -------------------------------------------------- | ----------------------------- | --------------------------------------- |
| Protein                                            | 0.8                           | 0.6                                     |
| Carbohydrate                                       | 0.12                          | 0.09                                    |
| Fatty acid                                         | 0.04                          | 0.03                                    |
| Cholesterol                                        | 0.3                           | 0.2                                     |
</details>

![](images/a70baacb8c09ba3d3fd90f38ad0790f7424275067c5b9aeb9321ace6bb04d829.jpg)

<details>
<summary>text_image</summary>

E
Carbohydrate
</details>

![](images/a119c813c940cad111f190819a8231f54729a6af4b0ef6d74d48d2fd2e2cb75e.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of cellular structures with PAS label, showing stained regions and a scale bar (no text or symbols beyond label)
</details>

![](images/3465b281ae956bfc514e94a67d36d1a413aab24bd0db5b9a844a3eb70f5d60e6.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing cellular structures labeled with 'Carbohydrate' and 'PAS', no text or symbols present.
</details>

Fig. 2. h2 SRS imaging can precisely map intracellular carbohydrates in cancer cells. (A) Representative hSRS image, h2 SRS mapped protein, carbohydrate, fatty acid, cholesterol, and nucleic acid images, as well as the merged image of metabolites mapping for U87 cultured in a control or glucose depletion medium. The ranges of color bars are 0 to 400, 0 to 2, 0 to 1.2, 0 to 2, 0 to 2.4, and 0 to 0.5. Scale bar, 20 μm. (B) Quantitative analysis of $\mathsf { h } ^ { 2 } \mathsf { S R S } .$ -mapped signal of protein, carbohydrate, fatty acid, or cholesterol for U87 cultured in a control or glucose depletion medium. $n = 1 3 \mathrm { t o } 3 5 .$ . (C) Representative hSRS image (sum of all channels), $\mathsf { h } ^ { 2 } \mathsf { S } \mathsf { R } \mathsf { S }$ mapped protein, car bohydrate, fatty acid, cholesterol, and nucleic acid images, as well as the merged image of metabolites mapping for Mia Paca2 cultured in a control or glucose depletion medium. The ranges of color bars are 0 to 300, 0 to 3, 0 to 0.4, 0 to 0.5, 0 to 1, and 0 to 0.1. Scale bar, 20 μm. (D) Quantitative analysis of h2 SRS-mapped signal of protein, carbohydrate, fatty acid, or cholesterol for Mia Paca2 cultured in a control or glucose depletion medium. n = 36 to 43. The box in the violin plot indicates means ± SD. \*\*P < 0.01 and $^ { * * * } P < 0 . 0 0 1$ . (E and F) Representative h2 SRS-mapped carbohydrate and periodic acid–Schiff (PAS) staining images of U87 (E) and SKOV3 (F). Carbohydrate-rich droplets are highlighted in (E) with yellow arrows in original images and zoomed-in regions [(E), second column]. Each compared channel (A and C) has the same contrast and shares a color bar. Scale bars, 20 μm.

Consistent with the representative images, the quantified mean in tensity from the carbohydrate maps significantly decreased due to glucose depletion in the cell culture environment (Fig. 2B). Fatty acid and protein levels also decreased, probably because fatty acids are used as an alternative fuel for glucose (12) and protein synthesis is suppressed by a lack of energy sources and precursors for glucose metabolism (52), whereas cholesterol levels did not show obvious changes, as expected (Fig. 2B). A similar metabolic profile change in response to glucose depletion was also observed in pancreatic cells Mia Paca2 (Fig. 2, C and D).

In addition to evaluating intracellular carbohydrate alterations in response to environmental carbohydrate source variations, periodi acid–Schiff (PAS) staining, a widely used polysaccharide labeling method, was used to validate the carbohydrate maps of h2 SRS imaging. As shown in Fig. 2, E and F, the $\mathrm { { h } } ^ { \mathrm { { 2 } } } \mathrm { { S R S } }$ mapped carbohy drate was highly consistent with PAS polysaccharides in multiple cell lines, including the pancreatic cancer cell Mia Paca2 (Fig. 2E) and the ovarian cancer cell line SKOV3 (Fig. 2F). In addition to the overall carbohydrate distribution overlapping with PAS staining, suspected carbohydrate-related subcellular structures, such as glycogen, were observed in the h2 SRS carbohydrate map, as highlighted with yellow arrows in Fig. 2E. The h2 SRS mappings for other components, including proteins, fatty acids, cholesterol, and nucleic acids, were quite different from those of PAS staining, suggesting that there was no obvious cross-talk between the carbohydrate separation and other biomolecules (fig. S2A). The h2 SRS mapped TAG signal was very low in these PAS-stained cells, probably because the PAS staining solution contained charcoal, which is widely used to remove nonpolar materials such as fatty acids. The fatty acid concentrations in both Mia Paca2 and SKOV3 cells de creased markedly after PAS staining (fig. S2, B and C), suggesting that h2 SRS can accurately detect intracellular fatty acid levels.

In addition to monitoring the fatty acid removal by charcoal, the metabolic profiles of cells cultured at various lipid concentrations were measured to further validate the h2 SRS map of fatty acids. Cells were cultured in delipidated (charcoal-striped) serum, in which most of the hydrophobic lipid species were removed. A rescue experiment using a 1% lipid mixture was also performed. The h2 SRS signal for fatty acids in U87 cells decreased in a lipid-depleted culture environment and was rescued by a 1% lipid mixture (Fig. 3, A and B). Quantification analysis showed that the rescue group had the highest cholesterol level, and there was no significant difference between the other two groups (Fig. 3B) because the lipid mixture containing cholesterol and cholesterol in this delipidated serum was removed. Similar validation measurements were performed in Mia Paca2 cells, and similar results were obtained (fig. S3, A and B). These results indicate that fatty acid and cholesterol levels measured by h2 SRS are positively related to the source concentration in the culture environment, suggesting the accuracy of h2 SRS in mapping these lipid species.

To validate the ability of h2 SRS to distinguish cholesterol from other biomolecules, h2 SRS imaging was performed on U87 cells cul tured in a cholesterol-rich medium in both the C–H and $1 6 0 0 \mathrm { c m } ^ { - 1 }$ regions (Fig. 3C). Because TAG and cholesterol have clearly distin guishable C═C trans and cis peaks at 1655 and $1 6 7 2 ~ \mathrm { { c m } ^ { - 1 } , }$ , respectively, they can be used to cross-validate corresponding h2 SRS output maps in the C–H region (44). Our SRS system in the 1600 $\mathrm { c m } ^ { \frac { \bf \lambda _ { 1 } } { \bf \lambda _ { 1 } } }$ region has a comparable spectral resolution $( 1 2 . 6 6 ~ \mathrm { c m } ^ { - 1 } )$ as the C–H region (fig. S3, C and D) and could thus detect the peak shifts of TAG and cholesterol (Fig. 3C). Through h2 SRS imaging in the C–H region, protein-rich, fatty acid–rich, and cholesterol-rich droplets were found in their respective mappings (Fig. 3C). The SRS spectra of these single-component–rich droplets in the C–H region are difficult to distinguish without further data processing but have cognizable spectral differences in the $1 6 0 0 ~ \mathrm { { c m } ^ { - 1 } }$ region that agree with their reference chemicals (Fig. 3, D and E). In this cholesterol-rich culture environment, both U87 (Fig. 4, A and B) and Mia Paca2 cells (fig. S4, A and B) exhibited a marked increase in the mapped cholesterol signals, whereas the signals from other channels remained at similar levels. These results indicate that h2 SRS imaging in the C–H region can map cholesterol levels with minimal cross-talk with other biomolecules.

Except for detecting intracellular cholesterol level rise in a cho lesterol-rich culture environment, we also validated cholesterol con centration maps by evaluating the intracellular cholesterol level variation in response to a cholesterol-removing agent methyl-β-cy clodextrin (MβCD). After MβCD treatment, U87 cells had visibly weaker h2 SRS signal of cholesterol while the signals for other channels remained unchanged (Fig. 4C), consistent with the quantification analysis (Fig. 4D). Metabolic profile changes in Mia Paca2 in response to MβCD showed a similar phenomenon (fig. S4, C and D). These data support the idea that h2 SRS imaging can accurately measure intracellular carbohydrates, fatty acids, cholesterol, and protein levels without observable cross-talk between different biomolecules.

## h2 SRS imaging discloses metabolic profile reprogramming in cisplatin treated brain cancer cells

By simultaneously mapping multiple metabolites through h2 SRS, we can uncover alterations in the cancer metabolic network during chemotherapy. We first measured the U87 cell’s metabolic profile change in response to cisplatin treatment, a common chemotherapeutic agent for brain cancer. U87 cells treated with cisplatin exhibited a considerable increase in carbohydrate and fatty acid content and similar protein and cholesterol levels (Fig. 5, A and B), implying that carbohydrate and fatty acid metabolic alterations may play an important role in brain cancer survival under cisplatin induced stress. On the basis of the shape of the violin plot, which illustrates the probability density of the data, subpopulations can be observed within each group, particularly in terms of fatty acid content (Fig. 5B). This suggests that certain cells exhibit a more pro nounced metabolic response to chemotherapy and may be more re silient to chemotherapeutic stress, ultimately leading to the development of chemoresistance.

To study the mechanism underlying cisplatin-induced metabolic profile reprogramming in U87 cells, we first investigated the sources of metabolites using hSRS imaging in the C–D bond region (2050 to $2 3 5 0 ~ \mathrm { c m } ^ { - 1 } )$ for cells cultured with nutrients and stable isotope probes. We examined glucose uptake and derived me tabolism by feeding U87 cells deuterated $\mathrm {  { g l u c o s e - D _ { 7 } . } }$ . SRS images showed a stronger C–D signal in the cisplatin-treated U87 cells (Fig. 5C), which was confirmed by a significant increase in the in tegral C–D signal per cell in quantitative analysis (Fig. 5D). Thi result implies that the increase in carbohydrate content in cisplat in-treated U87 cells may be due to glucose uptake. To test this hy pothesis, we measured the mRNA expression level in U87 cells using the glucose transporter GLUT1 (53). The results indicated that cisplatin treatment enhanced GLUT1 expression in U87 cells, which was positively correlated with the cisplatin concentration (Fig. 5E). This increased C–D signal from $\mathrm { g l u c o s e - D _ { 7 } }$ and glucose transporter up-regulation indicated that glucose uptake contributed to cisplatin-induced carbohydrate content enrichment in U87 cells, which could be a therapeutic target for sensitizing breast cancer cells to cisplatin treatment. Thus, we performed a viability test on U87 cells treated with cisplatin in a glucose-depleted medium. The result shows that glucose depletion rendered U87 cells more vulnerable to cisplatin (Fig. 5F). To identify the therapeutic target at the molecular level, we used the GLUT1 inhibitor BAY-876 (BAY) to inhibit glucose uptake, with the aim of sensitizing U87 cells to cis platin treatment, because BAY is not toxic to U87 cells at high concentrations (fig. S5A). The combination treatment of cisplatin and BAY on U87 cells had a crucial synergistic effect in suppressing cell growth, reducing the half-maximal inhibitory concentration $( \bar { \mathrm { I C } } _ { 5 0 } )$ values by 51% (Fig. 5G). These data suggest that targeting the altered metabolism following cisplatin treatment can sensitize brain cancer U87 cells to cisplatin.

Subsequently, we studied another metabolite, fatty acid, an in creased level of which was detected by h2 SRS (Fig. 5, A and B).

![](images/a51d78c383889106d631481813c8e4f1a70ae4740c7ecea9161e3553135e4372.jpg)

<details>
<summary>text_image</summary>

A
SRS Protein Carbohydrate Fatty acid Cholesterol Nucleic acid Merged
Control
Delipid
Delipid +
1% lipid
</details>

![](images/e6c6399ad7dbdceb994b02d44091d50c58a8fb603b66043fc40e63befc6aa195.jpg)

<details>
<summary>violin plot</summary>

| Protein / Carbohydrate / Fatty acid / Cholesterol | Control | Delipid | Delipid + 1% lipid |
| --- | --- | --- | --- |
| Mean intensity (a.u.) | 0.6 | 0.8 | 1.2 |
| Mean intensity (a.u.) | 0.15 | 0.15 | 0.20 |
| Mean intensity (a.u.) | 0.05 | 0.05 | 0.10 |
| Mean intensity (a.u.) | 0.25 | 0.25 | 0.30 |
| Mean intensity (a.u.) | 0.15 | 0.15 | 0.20 |
| Mean intensity (a.u.) | 0.05 | 0.05 | 0.10 |
| Mean intensity (a.u.) | 0.4 | 0.4 | 0.45 |
| Mean intensity (a.u.) | 0.25 | 0.25 | 0.30 |
| Mean intensity (a.u.) | 0.15 | 0.15 | 0.20 |
| Mean intensity (a.u.) | 0.05 | 0.05 | 0.10 |
| Mean intensity (a.u.) | 0.45 | 0.45 | 0.50 |
** indicates statistical significance for Delipid vs. Delipid + 1% lipid.
</details>

![](images/c922f39e807ca4f9fdcf3bfb39ceeb7289680214a0b5b1499740482df79d033c.jpg)

<details>
<summary>text_image</summary>

C
SRS
Protein
Carbohydrate
Fatty acid
Cholesterol
Merged
Cholesterol
Fatty acid
Protein rich
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
</details>

![](images/aa609fc013dde818f2a43eb9e72e70bc179cead7222931a5a32c8b0c39ae8fe5.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | BSA | TAG | Cholesterol |
| ------------------ | --- | --- | ----------- |
| 1600               | 0.0 | 1.0 | 2.0         |
| 1700               | 1.0 | 2.0 | 3.0         |
| 2900               | 1.0 | 2.0 | 3.0         |
| 3000               | 0.0 | 1.0 | 2.0         |
</details>

![](images/1903bcf14e58860fa0c3b25de173b67d61014e20d572b443be7af7f59f7805a2.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Protein-rich | Fatty acid-rich | Cholesterol-rich |
| ------------------ | ------------ | --------------- | ---------------- |
| 1600               | 0.3          | 1.2             | 2.4              |
| 1700               | 1.0          | 2.0             | 3.3              |
| 2900               | 1.0          | 2.0             | 3.2              |
| 3000               | 0.0          | 1.0             | 2.2              |
</details>

Fig. 3. h2 SRS imaging can precisely separate fatty acids from other biomolecules in cancer cells. (A) Representative hSRS image, $\mathsf { h } ^ { 2 } \mathsf { S R S }$ mapped protein, carbo hydrate, fatty acid, cholesterol, and nucleic acid images, as well as the merged image of metabolites mapping for U87 cultured in a control (with fetal bovine serum), lipid depletion (with delipid serum), or lipid depletion medium supplementary with 1% lipid mixture. Each channel has the same contrast and shares a color bar. The ranges of color bars are 0 to 250, 0 to 3, 0 to 0.9, 0 to 0.8, 0 to 1.2, and 0 to 0.1. (B) Quantitative analysis of $\mathsf { h } ^ { 2 } \mathsf { S R S } .$ -mapped signal of protein, carbohydrate, fatty acid, or cholesterol fo U87 cultured in control, lipid depletion medium, or lipid depletion medium supplementary with 1% lipid mixture. $n = 1 0 \mathrm { t o } 1 5 . ^ { \ast } P < 0 . 0 5 , ^ { \ast \ast } P < 0 . 0 1$ , and $^ { * * * p } { } < 0 . 0 0 1 . ( \mathbf { c } )$ Representative hSRS image, $\mathsf { h } ^ { 2 } \mathsf { S R S }$ mapped protein, carbohydrate, fatty acid, cholesterol, and nucleic acid images, as well as the merged image of metabolites mapping for U87 cultured in medium with excess cholesterol with protein, fatty acid, and cholesterol-rich droplets highlighted. The ranges of color bars are 0 to 300, 0 to 1.1, 0 to 0.4, 0 to 1.8, and 0 to 2. (D) SRS spectra of BSA, TAG, and cholesterol in $1 6 0 0 { \mathsf { c m } } ^ { - 1 }$ and C–H regions. (E) SRS spectra of protein, fatty acid, and cholesterol-rich droplets are highlighted in (C) in 1600 $\mathsf { c m } ^ { - 1 }$ and C–H regions. The cholesterol peak at 1674 cm−1 and the TAG peak $\mathfrak { t } 1 6 5 5 \mathsf { c m } ^ { - 1 }$ are highlighted with green and red dash lines in (D) and (E), respectively. Scale bars, 20 μm.

We first measured fatty acid uptake by hSRS imaging in the C–D region of U87 cells separately fed with the deuterium-labeled saturated fatty acid palmitic acid- $\mathrm { \cdot D } _ { 3 1 } \left( \mathrm { P A } \mathrm { - D } _ { 3 1 } \right)$ or the unsaturated fatty acid oleic $\mathrm { a c i d \mathrm { - } D _ { 3 4 } \left( O A { - } D _ { 3 4 } \right) }$ (Fig. 5, H and I, and fig. S6, A and B). Representative SRS images and quantitative analysis revealed a re duction in the C–D signal in $\mathrm { P A } { \mathrm { - } } \mathrm { D } _ { 3 1 } { \mathrm { - t r e a t e d } }$ U87 cells (fig. S6, A and B). However, the C–D signal in U87 cells from $\mathrm { O A } { - } \mathrm { D } _ { 3 4 }$ mark edly increased after cisplatin treatment (Fig. 5, H and I), suggesting that U87 cells preferentially took up unsaturated fatty acids instead of saturated fatty acids under cisplatin treatment stress. In agreement with the metabolic profile measurements obtained through $\mathrm { h } ^ { 2 } \mathrm { S R S } .$ , it is evident from the representative image and violin plot that certain treated cells exhibited substantially higher levels of fatty acid uptake than the remaining population, suggesting the presence of a subpopulation within cisplatin-treated brain cancer cells (Fig. 5, H and I). To further confirm that the increased fatty acid content in cisplatin-treated U87 cells was due to exogenous fatty acid uptake, the mRNA expression level of the common fatty acid transporter CD36 was evaluated and showed a positive rela tionship with cisplatin treatment (Fig. 5J). These results imply that modulating fatty acid availability may boost U87 sensitivity to cisplatin, and the decreased $\mathrm { I C } _ { 5 0 }$ value of U87 cells in a fatty acid–deficient environment supports this hypothesis (Fig. 5K). In addition, reducing fatty acid availability by blocking fatty acid uptake through the fatty acid transporter CD36 inhibitor sulfosuccinimidyl oleate (SSO) significantly sensitized U87 cells to cisplatin with an approximate reduction of 45% in the value of $\mathrm { I C } _ { 5 0 } \left( \mathrm { F i g } . 5 \mathrm { L } \right)$ , whereas SSO treatment alone was not lethal to U87 cells unless the concentration was extremely high (fig. S6C). Therefore, SSO is a po tential candidate for combination therapy with cisplatin to achieve better anticancer outcomes. Furthermore, we assessed the uptake of cholesterol by measuring the C≡C signal in cells fed with

![](images/d0ac52206835277d40adfcf70dc9629cd2391a2e48335fbcec822b1e3ad24a56.jpg)

<details>
<summary>text_image</summary>

A
SRS Protein Carbohydrate Fatty acid Cholesterol Nucleic acid Merged
Control
Cholesterol
</details>

B  
![](images/bf805db6496eebd44ff25898bc95f2210ce0cc586decbb479259eb681fd4da0f.jpg)

<details>
<summary>violin plot</summary>

| Protein / Carbohydrate / Fatty acid / Cholesterol | Group | Mean Intensity (a.u.) |
| --- | --- | --- |
| Protein | Control | ~0.7 |
| Protein | Exogenous cholesterol | ~0.85 |
| Carbohydrate | Control | ~0.04 |
| Carbohydrate | Exogenous cholesterol | ~0.08 |
| Fatty acid | Control | ~0.03 |
| Fatty acid | Exogenous cholesterol | ~0.06 |
| Cholesterol | Control | ~0.01 |
| Cholesterol | Exogenous cholesterol | ~0.25 (***), ~0.35 (***), ~0.15 (***) |
</details>

![](images/75c7d52e1e784fd07d69023230ee10ac87d73bb1432209bccc55aa06b00eaabc.jpg)

<details>
<summary>text_image</summary>

c
SRS Protein Carbohydrate Fatty acid Cholesterol Nucleic acid Merged
Control
MβCD
</details>

D  
![](images/620ab99aae68c8f914c7020436fe2700c2446da118dcdab97b6f4bf38590ef64.jpg)

<details>
<summary>violin plot</summary>

| Protein / Carbohydrate / Fatty acid / Cholesterol | Group | Mean Intensity (a.u.) |
| --- | --- | --- |
| Protein | Control | 0.8 |
| Protein | MβCD | 0.6 |
| Carbohydrate | Control | 0.15 |
| Carbohydrate | MβCD | 0.12 |
| Fatty acid | Control | 0.45 |
| Fatty acid | MβCD | 0.35 |
| Cholesterol | Control | 0.18 |
| Cholesterol | MβCD | 0.15 |
</details>

Fig. 4. h2 SRS imaging reveals cholesterol content change in response to culture environment alternation and drug treatment in brain cancer cells. (A) Repre sentative hSRS image, h2 SRS mapped protein, carbohydrate, fatty acid, cholesterol, and nucleic acid images, as well as the merged image of metabolites mapping for U8 cultured in a control medium or medium with excess cholesterol. The ranges of color bars are 0 to 400, 0 to 2, 0 to 0.4, 0 to 0.6, 0 to 2, and 0 to 0.7. (B) Quantitative analysis of h2 SRS mapped signal of protein, carbohydrate, fatty acid, or cholesterol for U87 cultured in a control medium or medium with excess cholesterol. n = 14 to 19. (C) Representative hSRS image, h2 SRS mapped protein, carbohydrate, fatty acid, cholesterol, and nucleic acid images, as well as the merged image of metabolites mapping for U87 with or without cholesterol remover methyl-β-cyclodextrin (MβCD) treatment. The ranges of color bars are 0 to 300, 0 to 2, 0 to 0.8, 0 to 1.5, 0 to 1, and 0 to 0.4. (D) Quantitative analysis of h2 SRS mapped signal of protein, carbohydrate, fatty acid, or cholesterol for U87 treated with or without MβCD. n = 14 to 20. Each channel has the same contrast and shares a color bar. Scale bars, 20 μm. The box in the violin plot indicates means ± SD. \*P < 0.05 and $^ { * * * } P < 0 . 0 0 1$ .

Fig. 5. h2 SRS imaging discloses metabolic profile reprogramming in brain cancer cells after cisplatin treatment. (A) Representative images of hSRS, h2 SRS mapped protein, carbohydrate, fatty acid, cholesterol, and nucleic acid, as well as merged mapping for U87 cells treated with or without cisplatin. Each channel has the same contrast and shares a color bar. The ranges of color bars are 0 to 150, 0 to 1.5, 0 to 0.3, 0 to 0.5, 0 to 0.5, and 0 to 0.05. (B) Quantitative analysis for (A). The box indicates means ± SD. n = 59 to 62. (C and D) Representative SRS images and quantitative C–D signal of U87 cells cultured with 25 mM glucose- $\cdot \mathsf { D } _ { 7 } ,$ with or without 3.3 μM cisplatin treatment for 72 hours. n $= 1 1 2$ to 139. (E) Relative mRNA expression of GLUT1 in U87 cells treated with cisplatin for 48 hours. (F and G) Dose-response curve to cisplatin for U87 cultured with control or no glucose medium and with or without supplemental 1 μM BAY-876. (H and I) Representative SRS images and quantitative C–D signal of U87 cells cultured with 20 μM $\tt O A ^ { - } D _ { 3 4 }$ with or without $1 . 6 5 \mu \mathsf { M }$ cisplatin treatment for 48 hours. $n = 1 1 1$ to 146. (J) Relative mRNA expression of CD36 in U87 cells treated with cisplatin for 48 hours. (K and L) Dose-response curve to cisplatin for U87 cultured in medium with control or delipid serum and with or without supplemental 200 μM sulfosuccinimidyl oleate (SSO). $n = 3$ to 7 for $( { \mathsf { F } } ) , ( { \mathsf { G } } ) , ( { \mathsf { K } } ) ,$ , and (L). Scale bars, 20 μm (A) and 50 μm (C and H). In (D) and (I), the box indicates means $\pm \mathsf { S E } ;$ the whisker represents 5 to 95% of the data. Data in (E) and (J) are shown as means $+ 5 \mathsf { D } . \mathsf { \Pi } ^ { * } P < 0 . 0 5 .$ DMSO, dimethyl sulfoxide.  
![](images/d2b66def70d653da9c3b54cf11d8982ca5ac14a4c0eaf71ba8faf8819ef52e9c.jpg)

<details>
<summary>text_image</summary>

A
SRS Protein Carbohydrate Fatty acid Cholesterol Nucleic acid Merged
Control
Cisplatin
</details>

![](images/0a876f805fc36895b216800985ad68ad1ce3741dafab669542e4d1758bff771c.jpg)

<details>
<summary>violin plot</summary>

| Protein / Carbohydrate / Fatty acid / Cholesterol | Control Mean Intensity (a.u.) | Cisplatin Mean Intensity (a.u.) |
| -------------------------------------------------- | ----------------------------- | ------------------------------- |
| Protein (Mean intensity)                            | ~0.4                          | ~0.3                            |
| Carbohydrate (Mean intensity)                        | ~0.04                         | ~0.03                           |
| Fatty acid (Mean intensity)                        | ~0.15                         | ~0.12                           |
| Cholesterol (Mean intensity)                      | ~0.08                         | ~0.07                           |
</details>

![](images/18830876316ca2a79a1d9f8d48e3f956fffb318c6a7ce7d2f497f2fc166b599c.jpg)

<details>
<summary>text_image</summary>

C
CH SRS
CD SRS
DMSO
Cisplatin
</details>

![](images/bd2baf217e47fcf03ec161b8b59ba51f7d9f7aeea9e4176636548f5142b98e2e.jpg)

<details>
<summary>violin chart</summary>

| Group        | Integral CD signal per cell (a.u.) |
| ------------ | ---------------------------------- |
| U87_DMSO     | 0                                  |
| U87_Cisplatin| 40                                 |
</details>

![](images/b490c40da08030b18823bb9f3c6b458a46f2731e0a028e0891bf1a329b417053.jpg)

<details>
<summary>bar chart</summary>

| Group       | Relative mRNA expression level |
| ----------- | ------------------------------ |
| Control     | 1.0                            |
| 3.3 µM Cis  | 2.0                            |
| 6.6 µM Cis  | 3.0                            |
</details>

![](images/e14b5e22dc0fb4839c54a8e6763ad6bcce019c38a6b30bb7555050d42fd744fa.jpg)

<details>
<summary>line chart</summary>

| Cisplatin concentration (µM) | Control Viability (% of control) | No glucose Viability (% of control) |
| ---------------------------- | -------------------------------- | ---------------------------------- |
| 0.00                         | 100                              | 100                                |
| 1                            | 95                               | 90                                 |
| 10                           | 40                               | 20                                 |
| 100                          | 10                               | 5                                  |
</details>

![](images/8fe014262f16e2b3693a28d649f31c4b48fc1a3779683eef873d7dab5ddc7125.jpg)

<details>
<summary>line chart</summary>

| Cisplatin concentration (µM) | Control | BAY-876 |
| ---------------------------- | ------- | ------- |
| 0.00                         | 100     | 100     |
| 1                            | 95      | 90      |
| 10                           | 40      | 20      |
| 100                          | 10      | 5       |
</details>

![](images/62efcecc8c5c77c0f1899e06abb7b14f28040ec555c878c2ff381fd833f8e894.jpg)

<details>
<summary>text_image</summary>

H
C-H SRS
C-D SRS
DMSO
Cisplatin
</details>

![](images/6c47f4c589fdc79280eead14bfe3cb79b26f7f90ee51c053a3eb77e749702ea5.jpg)

<details>
<summary>bar chart</summary>

| Group        | Integral CD signal per cell (a.u.) |
| ------------ | ---------------------------------- |
| U87_DMSO     | 2000                               |
| U87_Cisplatin| 12000                              |
</details>

![](images/38722f1f86b74c81bba0b74ac5e771c1c8776e2112583f32963c6f8d6377e284.jpg)

<details>
<summary>bar chart</summary>

| Group | Relative mRNA expression level |
|-------|-------------------------------|
| Control | 1.0 |
| 3.3 µM Cis | 1.5 |
| 6.6 µM Cis | 2.0 |
</details>

![](images/b994038d5d5306c499d972a776045cb762064c048d19c7e300d85e11244e1b31.jpg)

<details>
<summary>line chart</summary>

| Cisplatin concentration (µM) | Control | Delipid |
| ---------------------------- | ------- | ------- |
| 0.00                         | 100     | 100     |
| 1                            | 95      | 90      |
| 10                           | 40      | 20      |
| 100                          | 10      | 5       |
</details>

![](images/585262d83388c9c98511dbb3301e244a5b9e1ef9eed7826aa775bd597488c567.jpg)

<details>
<summary>line chart</summary>

| Cisplatin concentration (µM) | Control Viability (% of control) | SSO Viability (% of control) |
| ---------------------------- | -------------------------------- | ---------------------------- |
| 0.00                         | 100                              | 100                          |
| 1                            | 95                               | 85                           |
| 10                           | 60                               | 40                           |
| 100                          | 20                               | 5                            |
</details>

cholesterol labeled with an alkyne tag, phenyl-diyne cholesterol (PhDY-Chol) (fig. S7). The observed reduction in cholesterol uptake suggests that other metabolic activities related to cholesterol, such as cholesterol synthesis and utilization, were also altered, re sulting in similar intracellular cholesterol content in treated U87 cells (Fig. 5, A and B). Our findings indicate that changes in the me tabolite content induced by cisplatin treatment in U87 cells can be detected using isotope hSRS imaging. Targeting these chemothera py-induced metabolic alterations can potentially enhance current therapeutic outcomes in the treatment of brain cancer (Fig. 5, G and L).

## h2 SRS imaging unveils metabolic profile reprogramming in gemcitabine-treated and -resistant pancreatic cancer cells

To demonstrate the general applicability of h2SRS, we further monitored the metabolic profile changes in pancreatic cancer cells that responded to gemcitabine, the most commonly used chemotherapy for pancreatic cancer. In addition to understanding the acute metabolic profile changes under chemotherapy, we studied the adapted metabolic profile reprogramming in drug-resistant cells to help identify a therapeutic target to fight gemcitabine resistance, a major challenge in current pancreatic cancer treatment (54–57). Accordingly, both the gemcitabine-resistant cell line G3K and its parental sensitive cell line Mia Paca2 were used to study gemcitabineinduced acute and adapted metabolic profile reprogramming in pancreatic cancer. h2 SRS imaging revealed that acute gemcitabine treatment resulted in distinct increases in carbohydrate and fatty acid concentrations in Mia Paca2 cells; however, no changes were observed for these two channels in G3K. Compared with sensitive Mia Paca2 cells, resistant G3K cells showed stronger signals in carbohydrate and fatty acid mapping (Fig. 6A). Notably, h2 SRS imaging enabled the visualization of elongated cell morphology in both gemcitabine-treated and gemcitabine-resistant cells, as well as the spatial distribution of each metabolite. For instance, fatty acid– dominant droplets are predominantly located at the periphery of the cells, as indicated by the arrows in the fatty acid channel. Furthermore, cholesterol-rich components near the nucleus were observed in G3K cells, as indicated by the arrows in the cholesterol maps (Fig. 6A). Quantitative analysis corresponded with the observation from the h2 SRS images and revealed an increase in cholesterol intensity in both gemcitabine-treated Mia Paca2 and resistant G3K cells compared to untreated Mia Paca2 cells (Fig. 6B). These results suggest that gemcitabine causes acute and adaptive enhancement of intracellular fatty acids, carbohydrates, and cholesterol levels in pancreatic cancer cells. The violin plot of fatty acids shows a distinct subpopulation of cells with a high fatty acid content, which is consistent with the representative images presented in Fig. 6A. These metabolic profile changes may be part of the self-defense strategies of pancreatic cancer cells to facilitate survival under gemcitabine stress.

To further study the mechanism underlying the observed meta bolic alterations, we first examined the source of enhanced carbo hydrate signals in these pancreatic cells by hSRS imaging in the C–D region of pancreatic cells fed with glucose-D7. The hSRS images in dicated that the C–D signals from glucose-D in gemcitabine treated Mia Paca2 cells and resistant G3K cells were significantly higher than those in wild-type Mia Paca2 cells, which is in agreement with the quantitative analysis (fig. S8, A and B). This boosted glucose-D –derived signal implies that gemcitabine drives pancreatic cancer cells to uptake more glucose instantly and perma nently, resulting in increased intracellular carbohydrate content in gemcitabine-treated and gemcitabine-resistant pancreatic cancer cells. This hypothesis was validated by the up-regulation of GLUT1 mRNA expression in the up-regulation in gemcitabinetreated and gemcitabine-resistant PC cells (Fig. 6, C to E). On the basis of the increased demand for glucose in gemcitabine-treated pancreatic cancer cells, Mia Paca2 and G3K cells were found to be more vulnerable to gemcitabine in glucose-depleted environments, as expected (fig. S8, C and D). To specifically interfere with glucose uptake, BAY, an inhibitor of the glucose transporter GLUT1, was used, which is not toxic at low concentrations (fig. S8E). The toxicity of high concentrations of BAY implies that its target trans porter, GLUT1, is a major glucose transporter in the pancreas and essential for its survival. The viability assay of BAY also indicated that the resistant G3K was more sensitive to BAY than the sensitive Mia Paca2 cell, in compliance with the increased carbohydrate level in G3K. Combined with low concentrations of BAY, gemcitabine toxicity obviously increased in G3K cells but did not improve sig nificantly in Mia Paca2 cells probably because this cell line is already extremely sensitive to gemcitabine (Fig. 6, F and G). These data sug gested that GLUT1-mediated glucose uptake was critical for the survival of G3K cells under gemcitabine stress.

In addition to carbohydrate metabolism, we studied fatty acid metabolism according to gemcitabine-induced metabolic profile re programming in pancreatic cells using h2 SRS imaging. hSRS imaging in the C–D region showed enhanced C–D signal intensity in gemcitabine-treated Mia Paca2 and resistant G3K cells with PA-$\mathrm { D } _ { 3 1 } ,$ , indicating that PA is one of the major sources of the acute and adapted fatty acid increase in pancreatic cancer cells under gemcitabine stress (fig. S9, A and B). In contrast, the C–D signal from OA $\mathrm { D } _ { 3 4 }$ increased in Mia Paca2 cells treated with gemcitabine but de creased in resistant G3K cells, implying that OA uptake contributes to the acute but not adapted gemcitabine-induced fatty acid increase in pancreatic cells (fig. S9, C and D). This increase in fatty acid uptake was supported by the up-regulation of mRNA expression of the fatty acid transporter CD36 in gemcitabine-treated and gemcitabine-resistant pancreatic cancer cells (Fig. 6, H to J). According to this growing demand for fatty acid sources, interference with fatty acid availability by removing fatty acid sources in the culture medium makes Mia Paca2 and G3K cells more vulnerable to gemcitabine treatment, as expected (fig. S9, E and F). To narrow down the therapeutic target to the molecular level, SSO, an inhibitor of the fatty acid transporter CD36, was used to improve the therapeutic outcome of gemcitabine. Solely, SSO was not toxic to pancreatic cancer cells (fig. S9G), but it could sensitize pancreatic cancer cells to gemcitabine treatment, especially G3K, with an $\mathrm { I C } _ { 5 0 }$ value reduction of approximately 41% (Fig. 6, K and L). These results imply that CD36-mediated fatty acid uptake contributes to the gemcitabine-induced fatty acid content increase in pancreatic cancer cells and that the CD36 inhibitor SSO combined with gemcitabine yields a synergetic effect on suppressing pancreatic cancer cell growth.

Via h2 SRS, we also observed an increase in cholesterol levels in gemcitabine-resistant G3K cells compared to Mia paca2 cells (Fig. 6B). To monitor cholesterol uptake, we performed hSRS imaging of cells treated with the cholesterol analog PhDY-Chol. Images and quantitative analysis showed a significant increase in cholesterol uptake in resistant G3K cells and a modest increase in treated Mia Paca2 cells compared to untreated Mia Paca2 cell (fig. S10, A and B). This enhanced cholesterol uptake in G3K cell agrees with the metabolic profile measurement of intracellular cho lesterol levels, suggesting that exogenous uptake is the primary source of cholesterol in G3K cells. The limited increase in cholester ol uptake observed in the treated Mia Paca2 cells implies that cho lesterol synthesis may also contribute to the acute elevation of cholesterol levels following gemcitabine treatment. Using a similar strategy, the cholesterol removal agent 2-hydroxypropyl-β cyclodextrin (HPβCD) was used to sensitize pancreatic cancer cell to gemcitabine because HPβCD is not toxic to Mia Paca2 and G3K cells (fig. S10C). However, the synergistic effect of this combination treatment was inconspicuous in both Mia Paca2 and G3K cells (fig. S10, D and E). The various synergistic outcomes of combinational treatments targeting different metabolites demonstrate the signifi cance of high-content metabolic imaging and subsequent analysis of the same cells.

![](images/45943cd056bcc5cbd22a08721e388475bc5b81f93a2f3eb55fe90dea58a2d98b.jpg)

<details>
<summary>text_image</summary>

A
SRS Protein Carbohydrate Fatty acid Cholesterol Nucleic acid Merged
Mia Paca2
Mia Paca2
+ Gem
G3K
(resistant)
G3K
+ Gem
</details>

![](images/c9eb4b58ac77e32a7de35ace68ab379d8f0d4a458914ef4d709b763356650e87.jpg)

<details>
<summary>violin chart</summary>

| Category       | Subgroup        | Mean Intensity (a.u.) |
| -------------- | --------------- | --------------------- |
| Protein        | Mia Paca2 + Gem | 0.8                   |
| Protein        | G3K             | 0.6                   |
| Protein        | G3K + Gem       | 0.7                   |
| Carbohydrate   | Mia Paca2 + Gem | 0.1                   |
| Carbohydrate   | G3K             | 0.2                   |
| Carbohydrate   | G3K + Gem       | 0.3                   |
| Fatty acid     | Mia Paca2 + Gem | 0.1                   |
| Fatty acid     | G3K             | 0.1                   |
| Fatty acid     | G3K + Gem       | 0.2                   |
| Cholesterol    | Mia Paca2 + Gem | 1.5                   |
| Cholesterol    | G3K             | 1.4                   |
| Cholesterol    | G3K + Gem       | 1.6                   |
</details>

![](images/c2d1e6069657fd07734c67e302034fb36de241d8513189c008e6303acf67fcd9.jpg)

<details>
<summary>bar chart</summary>

| Gene | Condition | Relative mRNA expression level |
|------|-----------|-------------------------------|
| GLUT1 | Mia Paca2 | 1.0 |
| GLUT1 | G3K | 2.0 |
| Mia Paca2 | Control | 1.0 |
| Mia Paca2 | 10 µM Gem | 2.0 |
| Mia Paca2 | 20 µM Gem | 2.5 |
| Mia Paca2 | Control | 1.0 |
| Mia Paca2 | 20 µM Gem | 1.5 |
| Mia Paca2 | 40 µM Gem | 1.5 |
| G3K | Control | 100 |
| G3K | BAY-876 | 100 |
| Viability (% of control) - Mia Paca2 | Control | 100 |
| Viability (% of control) - Mia Paca2 | BAY-876 | 100 |
| Viability (% of control) - G3K | Control | 100 |
| Viability (% of control) - G3K | BAY-876 | 100 |
</details>

![](images/212cee866ddb44d946e7f91d02e62a24e1bf7943d1cf6e5de4f3ed20cf894dad.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Cell Line | Treatment | Relative mRNA expression level | Gene Concentration (μM) | Significance |
| --- | --- | --- | --- | --- |
| H | Mia Paca2 | ~1.0 | ~10 | ** |
| H | G3K | ~1.8 | ~10 | * |
| I | Mia Paca2 | ~1.0 | ~10 | — |
| I | 10 µM Gem | ~5.0 | ~10 | — |
| I | 20 µM Gem | ~5.0 | ~10 | — |
| I | Control | ~1.0 | ~10 | — |
| K | Mia Paca2 | ~1.0 | ~10 | ** |
| K | 10 µM Gem | ~5.0 | ~10 | — |
| K | 20 µM Gem | ~5.0 | ~10 | — |
| K | 40 µM Gem | ~5.0 | ~10 | — |
| J | Mia Paca2 | ~95 | ~0.00001E-4 | — |
| J | Control | ~95 | ~0.001 | — |
| J | SSO | ~95 | ~0.01 | — |
| L | Mia Paca2 | ~95 | ~0.1 | — |
| L | Control | ~95 | ~1 | — |
| L | SSO | ~95 | ~10 | — |
| G3K | Mia Paca2 | ~95 | ~1 | — |
| G3K | Control | ~95 | ~1 | — |
| G3K | SSO | ~95 | ~1 | — |
</details>

Fig. 6. h2 SRS imaging unveils metabolic profile reprogramming in gemcitabine-treated or -resistant pancreatic cancer cells. (A) Representative hSRS image, h2 SR mapped protein, carbohydrate, fatty acid, cholesterol, and nucleic acid images, as well as the merged image of metabolites mapping for gemcitabine-sensitive Mia Paca and resistant G3K cells treated with or without gemcitabine. Scale bar, 20 μm. Each channel has the same contrast and shares a color bar. The ranges of color bars are 0 to 250, 0 to 1.8, 0 to 0.4, 0 to 1.2, 0 to 6, and 0 to 0.05. (B) Quantitative analysis of h2 SRS mapped signal of protein, carbohydrate, fatty acid, or cholesterol for Mia Paca2 and G3K with or without gemcitabine treatment. n = 83 to 105. The box in the violin plot indicates means ± SD. (C to E) Relative mRNA expression level of GLUT1 in Mia Paca and G3K cells treated with (D and E) or without (C) gemcitabine for 72 hours. (F and G) Dose-response curve to gemcitabine with or without supplemental 50 nM BAY-876 treatment for Mia Paca2 (F) and G3K (G) cells. (H to J) Relative mRNA expression level of GLUT1 in Mia Paca2 and G3K cells treated with (I and J) or without (H) gemcitabin for 72 hours. Data in all the bar charts (C to E and H to J) are shown as means + SD. (K and L) Dose-response curve to gemcitabine with or without supplemental 200 μM SSO treatment for Mia Paca2 (K) and G3K (L) cells. n = 3 for dose-response viability assay (F, G, K, and L). $^ { * } P < 0 . 0 5 , ^ { * * } P < 0 . 0 1$ , and $^ { * * * } P < 0 . 0 0 1$ cl

## DISCUSSION

## h2 SRS imaging provides insights into cancer metabolic response to chemotherapy

Several studies have indicated that chemotherapy can trigger the re programming of multiple metabolites simultaneously (5–7, 12), similar to our observations in this study. However, simultaneous mapping of multiple chemical species inside a single cell using ex isting analytical approaches is challenging. Although mass spec trometry approaches, including cytometry by time of flight, matrix-assisted laser desorption/ionization, desorption electrospray ionization, and SpaceM, can provide a wealth of molecular information, they have insufficient resolution for intracellular measure ments and/or require the introduction of labels that may interfere with cell metabolism (58, 59). Some mass spectrometry imaging techniques, such as nano–secondary ion mass spectrometry (nano-SIMS), have high resolution. However, nano-SIMS has low throughput, making it impractical for studying heterogeneous samples (60). Raman spectroscopy allows label-free, high-resolu tion, and high-throughput imaging but can only distinguish a few metabolites inside a cell (12) because the major metabolites have limited spectral features in certain vibration regions and signifi cantly overlap spatially, leading to signal cross-talk. To address these difficulties, we improved the spatial and spectral resolutions of our SRS setup to collect more spectral information from biolog ical samples (36). To extract the desired information from the hSRS images with packed spectral information, we introduced a sparsity constraint to restrain cross-talk from inconsequential components at each pixel. The integration of these instrumental advantages and data processing by pixel-wise LASSO enables the mapping of major biomolecules, specifically proteins, carbohydrates, fatty acids, cho lesterol, and nucleic acids, thereby revealing the metabolic profiles of cancer cells.

Taking advantage of this metabolic profile measurement at the single-cell level using h2 SRS imaging, we clustered three important metabolites, carbohydrates, fatty acids, and cholesterol, in a single cell–based three-dimensional (3D) scatterplot for a more compre hensive understanding of metabolic reprogramming in cancer cells. After clustering these three important metabolites, the difference between gemcitabine-sensitive Mia Paca2 and resistant G3K cell in the 3D scatterplot was much more evident than the measurement of a single metabolite because G3K cells tend to have higher con tents of all three metabolites simultaneously (Fig. 7A). In addition, acute metabolic profile reprogramming induced by gemcitabine in Mia Paca2 cells clearly showed that gemcitabine-treated Mia Paca2 cells with higher carbohydrate signals tended to have higher fatty acid and cholesterol contents (Fig. 7B). Similarly, the difference in metabolic profile between cisplatin-treated and untreated U87 cells was more obvious in the 3D scatterplot than in the single metabolite measurements (Fig. 7C). This metabolic profile measurement provides an approach for studying any potential positive or negative correlation between metabolites that have been observed in previou cancer studies (5, 6, 12). In addition to measuring the metabolite content within a cell, h2 SRS imaging revealed subpopulations in heterogeneous cell samples, as illustrated in Figs. 5B and 6B, as well as the spatial distribution of certain metabolites, such as lipid droplets at the cell periphery and cholesterol accumulation near the nucleus in pancreatic cancer cells (Fig. 6A). Moreover, our previou study established a relationship between the spatial distribution of lipid droplets and alterations in the morphology of pancreatic cancer cells subjected to stress (10). Expanding upon this study, the inclusion of h2 SRS would enable the exploration of additional metabolites and the investigation of more intricate correlations between cell morphology and metabolic profiles.

## h2 SRS mapping of metabolic profile facilitates discovery of most effective therapeutic targets

In this study, h2 SRS was used to map multiple metabolites at the single-cell level. To quantitatively compare their significance in im proving the outcome of chemotherapy, we characterized the metabolic profile in terms of the intensity of $\mathrm { h } ^ { 2 } \mathrm { S R S }$ mapped carbohydrate, fatty acids, and cholesterol at the single-cell level and performed discriminant analysis to classify different cell lines or cells with various treatments. Using the intensity of these three metabolites, the discriminant analysis yielded a relatively high original (62.6%) and cross-validated (61.6%) accuracy in distinguishing gemcitabine-sensitive Mia Paca2 and resistant G3K cells. Furthermore, the standardized canonical discriminant function coefficient from the discriminant analysis was positively related to the synergetic effect of the combined treatment targeting the respective metabolites (table S1A). The synergetic effect of the combinational treatment was evaluated by the $\bar { \Gamma } \bar { \mathbf { C } } _ { 5 0 }$ fold-change between the combinational treatment and the original chemotherapy. BAY, SSO, and HPβCD have been used to perform combinational treatment target ing carbohydrate, fatty acid, and cholesterol-derived metabolism, respectively. The standardized canonical discriminant function coefficient represents the correlation of specific variables to distin guish the two groups in the discernment analysis. Ranking the discriminant function coefficients in table S1A, fatty acids contributed most to the adapted metabolic profile reprogramming in gemcitabine-resistant G3K cells, followed by carbohydrates and cholesterol. Accordingly, the combination treatment targeting fatty acid uptake resulted in the greatest reduction in the $\mathrm { I C } _ { 5 0 }$ value for gemcitabine treatment in G3K cells, followed by carbohy drate and cholesterol. These discriminant function coefficients and the synergetic effect of the combination treatment were also positively related to the fold change in $\mathrm { h } ^ { 2 } \mathrm { S R S }$ mapped intensity for the respective metabolites (table S1A). These results imply that h2 SRS imaging metabolic profile measurement can not only identify potential metabolic targets for better anti-cancer outcomes but also predict the most effective target metabolites to improve cancer therapy.

In addition to adapting metabolic profile reprogramming in drug-resistant cells, we applied the abovementioned analytical method to study metabolic profile reprogramming by comparing gemcitabine-treated and untreated Mia Paca2 cells. The discriminant analysis had high original (80.1%) and cross-validated (77.3%) accuracy when classifying Mia Paca2 cells with and without gemcitabine treatment. On the basis of discriminant anal ysis, fatty acids had the highest discriminant function coefficient, accompanied by the greatest growth of h2 SRS mapped intensity and the best synergetic effect in suppressing Mia Paca2 cell growth, followed by carbohydrates (table S1B). Cholesterol with a small increase in $\mathrm { \dot { h } } ^ { 2 } \mathrm { S R S }$ mapped intensity was least positively related to the differentiation between gemcitabine-treated versus untreated Mia Paca2 cells and thus could barely improve gemcitabine therapeutic outcome on Mia Paca2 as expected.

A  
![](images/76f5316a6c9e2c6e6a983a1e35d1a7850a1a2e709d43d4ec3ed9f21b9605a924.jpg)

<details>
<summary>scatterplot</summary>

| Fatty acid | Cholesterol | Group     |
| ---------- | ----------- | --------- |
| 0.0        | 0.0         | Mia Paca2 |
| 0.0        | 0.0         | G3K       |
| 0.2        | 0.3         | Mia Paca2 |
| 0.2        | 0.4         | G3K       |
| 0.4        | 0.6         | Mia Paca2 |
| 0.4        | 0.7         | G3K       |
| 0.6        | 0.9         | Mia Paca2 |
| 0.6        | 1.0         | G3K       |
| 0.8        | 1.2         | Mia Paca2 |
| 0.8        | 1.3         | G3K       |
| 1.0        | 1.4         | Mia Paca2 |
| 1.0        | 1.5         | G3K       |
</details>

B  
![](images/b6af5265e46de6bd9a62d8d0820c470cad18f1a9eb9836f5a67fe2f500a0407e.jpg)

<details>
<summary>scatter plot</summary>

| Fatty acid | Cholesterol | Group        |
| ---------- | ----------- | ------------ |
| 0.05       | 0.0         | Control      |
| 0.08       | 0.3         | Control      |
| 0.1        | 0.6         | Control      |
| 0.15       | 0.9         | Control      |
| 0.2        | 1.2         | Control      |
| 0.25       | 1.5         | Control      |
| 0.3        | 1.4         | Control      |
| 0.35       | 1.3         | Control      |
| 0.4        | 1.2         | Control      |
| 0.45       | 1.1         | Control      |
| 0.5        | 1.0         | Control      |
| 0.05       | 0.0         | Gemcitabine  |
| 0.08       | 0.3         | Gemcitabine  |
| 0.1        | 0.6         | Gemcitabine  |
| 0.15       | 0.9         | Gemcitabine  |
| 0.2        | 1.2         | Gemcitabine  |
| 0.25       | 1.5         | Gemcitabine  |
| 0.3        | 1.4         | Gemcitabine  |
| 0.35       | 1.3         | Gemcitabine  |
| 0.4        | 1.2         | Gemcitabine  |
| 0.45       | 1.1         | Gemcitabine  |
| 0.5        | 1.0         | Gemcitabine  |
</details>

C  
![](images/dd32311417052076d739e69c3b2288bcb83342781e8904af64847fec0b25bc83.jpg)

<details>
<summary>scatter plot</summary>

| Fatty acid | Cholesterol | Group     |
| ---------- | ----------- | --------- |
| 0.01       | 0.00        | Control   |
| 0.02       | 0.02        | Cisplatin |
| 0.03       | 0.04        | Cisplatin |
| 0.04       | 0.06        | Cisplatin |
| 0.05       | 0.08        | Cisplatin |
| 0.06       | 0.10        | Cisplatin |
</details>

Fig. 7. Single-cell–based 3D scatterplot reveals cancer cell metabolic profile reprogramming induced by chemotherapy. (A) Three-dimensional scatterplots of h2 SRS mapped carbohydrate, fatty acid, and cholesterol intensity for Mia Paca2 and G3K cell based on single-cell analysis. n = 94 to 106. (B) Three-dimensional scatterplots of h2 SRS mapped carbohydrate, fatty acid, and cholesterol intensity for Mia Paca2 with or without gemcitabine treatment. n = 84 to 94. (C) Three-dimensional scatterplots of h2 SRS mapped carbohydrate, fatty acid, and cholesterol intensity for U87 treated with or without cisplatin. n = 59 to 62. Each point represents a single cell, and the ellipsoids represent 80% of data coverage.

A similar phenomenon was observed in the brain cancer U87 cells. The accuracy of the discriminant analysis distinguishing U87 cells with and without cisplatin treatment was relatively high for both the original (62.8%) and cross-validated (60.3%) analyses. Comparing the metabolites with a significant change in $\mathrm { h } ^ { 2 } \mathrm { S R S }$ mapped intensity in cisplatin-treated U87 cells, fatty acids had a higher discriminant function coefficient and h2 SRS mapped intensity fold change than carbohydrates did, and thus the synergetic effect of combinational treatment blocking fatty acid uptake was greater than that blocking glucose uptake, as expected (table S1C). All these data support that h2 SRS-measured metabolic profile reprogramming can successfully predict which metabolites could be the most effective targets for improving the current therapy.

## h2 SRS enables label-fee imaging of carbohydrate inside cells

Currently, technologies for detecting intracellular carbohydrates are limited. Widely used methods include glucose uptake measurement by detecting fluorescent or isotopic labeling of glucose analogs, such as 2-[N-(7-Nitrobenz-2-oxa-1,3-diazol-4-yl)Amino]-2-Deoxyglu cose (2-NBDG)and [3 H]-2-deoxyglucose, and indirect measurement of glucose-related proteins, such as the glucose transporter GLUT1 (20, 61). However, these approaches cannot directly measure the endogenous glucose content of a cell, which is critical for studying carbohydrate metabolism, one of the most common fuels in mammalian cells. A recent study also showed that a glucose analog with a bulky fluorescent label enters the cell via a transporter-independent mechanism and thus lacks accuracy in studies of glucose transporters (20). This result is convincing when considering the comparable sizes of the fluorescent group and glucose, suggesting that only small labeling tags and labelfree methods are suitable for carbohydrate measurement.

Accordingly, SRS imaging is a powerful approach for carbohydrate metabolism studies that measures glucose uptake in the CD region via glucose-D (12, 62) and evaluates endogenous carbohydrate content in the C–H region through h2 SRS. This is the first reported imaging approach to evaluating relative endogenous carbohydrate content at the single-cell level in a label-free manner. This approach can greatly benefit not only research on overall intracellular carbo hydrate levels but also studies of carbohydrate-rich cellular compo nents, such as glycogen and the cell wall. Combined with a recently developed method established by Oh et al. (63), h2 SRS can measure the absolute concentration of carbohydrates as well as other metab olites in a cell, enabling metabolic profiling with absolute concen tration measurements. This combination further enhances the benefits of h2 SRS imaging for studying cell metabolism.

## Broader applications of h2 SRS imaging

Compared to metabolic profile measurements in fixed cells, as dem onstrated in this study, living cell imaging is more attractive for cell metabolic studies, although fixation has shown no effect on spectra unmixing in a previous study (36). Living cell imaging can facilitate a more comprehensive metabolic study by tracking metabolic profile dynamics and interactions between metabolites but requires a higher imaging acquisition speed. In this study, we used 100 frames of SRS images to cover the spectral region of interest with an even step size to obtain sufficient spectral information. However, the number of frames can be considerably reduced to less than 10 by subsampling, which can significantly shorten the imaging acquisition time but retain the spectral signature of the molecule of interest by capturing images only at the Raman shift with essential spectral features of the molecule of interest (47, 49). Improvement of imaging acquisition speed not only allows the implementation of metabolic profile monitoring in a living cell bu also benefits time-consuming tissue imaging, which is also impor tant for various biomedical fields. Leveraging the high depth reso lution and penetration depth of SRS imaging (64), h2 SRS can also be used for the more intricate task of volumetric imaging of tissues and 3D cultures.

In this study, we distinguished five major components covering the most abundant Raman signals within a cell. Several improvements can be made to scale separable channels beyond current channels. On the instrumentation side, we can further optimize the pulse chirping condition of the SRS system to reach sub–10 $\mathrm { c m } ^ { - \mathrm { i } }$ spectral resolution, making subtle peaks more differentiable. From an algorithm perspective, spectral unmixing is highly dependent on the signal fidelity of the data, and we can deploy more advanced deep learning–based denoisers to enhance the robustness of weaker channels versus noise. Last, because the unmixing algorithm is a supervised approach that requires prior knowledge of the chemical composition, more detailed prior information (metabolite com position and abundance) obtained through mass spectroscopy can effectively guide the selection and scaling of input references beyond the current five components.

In addition to investigating metabolic features related to chemo resistance, this approach could also be applied to study cancer progression, differentiation, and metastasis, which have been reported to involve cellular metabolic preprogramming (65–68). In addition to cancer studies, this method has broader applications in other disease models that are closely correlated with cellular metabolic re programming, such as obesity, diabetes, and metabolic disorders (69–72). Fundamental biological studies correlating metabolic re programming, such as immunological reactions, may benefit from this approach (73). In conclusion, our approach opens the door to a plethora of cancer cell metabolic features and reprogramming studies but is not limited to cancer cell research.

## MATERIALS AND METHODS

## Cell lines

Mia Paca2 (catalog no. CRL-1420), U-87 MG (catalog no. HTB-14), and SKOV3 (catalog no. HTB-77) cells were purchased from the American Type Culture Collection. Gemcitabine-resistant G3K cells were generated from parental Mia Paca2 cells by repeated gem citabine treatments (11). All cell lines were authenticated and tested negative for mycoplasma. SKOV3, Mia Paca2, and G3K cells were cultured in high-glucose Dulbecco’s modified Eagle’s medium (DMEM) supplemented with 10% fetal bovine serum (FBS) and penicillin/streptomycin (P/S; 100 U/ml). U-87 MG cells were cultured in Eagle’s minimum essential medium supplemented with 10% FBS and P/S (100 U/ml). All cells were maintained in a humidified incubator with a 5% $\mathrm { C O } _ { 2 }$ supply at $3 7 ^ { \circ } \mathrm { C } .$ Cells were seeded in 35 mm glass-bottom dishes for imaging experiments.

## Materials

Glucose- $\mathrm { D } _ { 7 } , \mathrm { P A } { \cdot } \mathrm { D } _ { 3 1 } ,$ and $\mathrm { O A } { - } \mathrm { D } _ { 3 4 }$ were purchased from Cambridge Isotope Laboratory. BAY, SSO, cisplatin, and gemcitabine were purchased from Cayman Chemical Co. Delipidated serum (charcoal stripped FBS) and glucose-free DMEM were obtained from Thermo Fisher Scientific.

## hSRS imaging

A lab-built SRS system developed according to a previously pub lished method was used to perform hSRS imaging (36). The system had a femtosecond laser source (InSight DeepSee+, Spectra-Physics) operating at 80 MHz with two synchronized output beams, a tunable pump beam ranging from 680 to 1300 nm, and a fixed Stokes beam at 1040 nm. The pump beam is tuned to 799 nm for imaging at the C–H vibration region (2800 to 3050 $\mathrm { c m } ^ { - 1 } )$ ), to 852 nm for imaging at the C–D vibration region (2100 to $2 3 0 0 ~ \mathrm { c m } ^ { - 1 } )$ , and to 890 nm for imaging at the fin gerprint vibration region (1530 to $1 7 8 0 \mathrm { c m } ^ { - 1 } )$ ). The Stokes beam was modulated at 2.3 MHz by an acousto-optic modulator (1205-C, Isomet) and chirped by a 15 cm glass rod (SF57, Schott) before being combined with the pump beam. The combined beam was subsequently chirped by five 15 cm glass rods before being sent to a laser-scanning microscope. The combined beam was focused on the sample using a 60× water immersion objective $( \mathrm { N A } = 1 . 2 , \mathrm { U P } .$ lanApo/IR, Olympus), and the signal from the sample was collected using an oil condenser (NA = 1.4, U-AAC, Olympus). The powers of the pump and Stokes beam before the microscope were 30 and 200 mW, respectively. To obtain hSRS images, a motorized linear stage was used to tune the optical path length of the Stokes beam, generating a pump-Stokes temporal delay that corresponds to different Raman bands under the spectral focusing scheme. The pixel dwell time was set to 10 μs. The size of each image was set to 400 × 400 pixels. A 100-frame image stack was acquired at differen pump-Stokes temporal delays for hSRS imaging.

Large-area mapping was achieved by moving the samples fixed on a motorized stage (PH117, Prior Scientific) controlled by a lab written LabView program. The program directs the stage to move to an adjacent location with partial overlap for stitching after hSRS imaging stack acquisition. A 3 × 3 montage image was acquired for each area of interest. At least three montage images were ob tained from different areas of interest in each sample. Montage images were stitched using ImageJ.

## Pixel-wise LASSO for hyperspectral image unmixing

After processing by the BM4D denoising method following a pre viously published method (36, 51), the acquired hSRS images were decomposed into pure chemical maps by pixel-wise LASSO unmix ing, as described below.

Given a 3D hyperspectral image stack with spatial dimensions of $N _ { x } , N _ { y }$ , and spectral dimension of $N _ { \lambda } ,$ , we first unfold the image into a 2D data matrix $D \in R ^ { N _ { x } N _ { y } \times N _ { \lambda } }$ in raster order. Assuming a total of k components, we subsequently construct a spectral reference matrix $S \in \overset { * } { R } ^ { N _ { \lambda } \times k }$ in which each column represents a spectrum from a pure component. Assuming a concentration matrix $\mathbf { \bar { \mathit { C } } } \in R ^ { N _ { x } N _ { y } \times k }$ , a linear mixing forward model equation can be formulated as follows

$$
D = C S ^ {T} + E \tag {1}
$$

where $S ^ { T }$ is the transpose of ${ \mathrm { ~  ~ \cal ~ S ~ } } ,$ and $E \in { \cal R } ^ { N _ { x } N _ { y } \times N _ { \lambda } }$ represents the error introduced by noise or fitting. The goal of hyperspectral image un mixing is to solve for C as the inverse of Eq. 1. To leverage chemica sparsity as a priori model, we introduced L1-norm regularization to each row of the concentration matrix and solved the original inverse problem in a row-by-row (i.e., pixel-by-pixel) manner through LASSO regression

$$
\hat {C} _ {i,:} = \arg \min _ {C _ {i,:} \geq 0} \left\{\frac {1}{2} \| D _ {i,:} - C _ {i,:} S ^ {T} \| _ {2} ^ {2} + \lambda \| C _ {i,:} \| _ {1} \right\} \tag {2}
$$

where $C _ { i , : }$ : is a k-element nonnegative vector representing the ith row of the concentration matrix $C , \hat { C } _ { i , : }$ : is the LASSO regression output, $D _ { i , : }$ : is the ith row in the data matrix D, and λ is the hyperparamete that tunes the level of sparsity.

For label-free high-content hSRS imaging, to form matrix $S ,$ spectra of pure biomolecule samples, including glucose, Bovine serum albumin (BSA), glyceryl trioleate, cholesterol, and cell ex tracted RNA, were obtained from individual experiments. For iso topic labeling imaging, reference spectral profiles were acquired from isotopic analog stock solutions. Measurements of the cell samples and references were performed on the same day to eliminate system variation. We fixed all imaging conditions and unmix ing parameters (S and λ) when measuring different cell samples; therefore, the output concentrations of a certain metabolite channel could be compared across different groups to study metabolic profile changes.

To quantify the metabolic profile and isotopic signal at the single-cell level, single-cell unmixing and mapping were performed using Ilastik pixel classification software (74). Representative areas of the nuclei, cytoplasm, and background were selected for Ilastik training and initial pixel unmixing generation. The final single cell map was generated via morphological fine-tuning using MATLAB software (MathWorks).

## Isotope labeling and SRS imaging

After seeding the cells in a 35 mm glass-bottom dish overnight, the original medium was replaced with media containing isotope labeling (glucose- $\mathrm { D } _ { 7 } , \mathrm { P A } \mathrm { - } \mathrm { D } _ { 3 1 } , \mathrm { O A } \mathrm { - } \mathrm { D } _ { 3 4 } ,$ or PhDY-Chol). For glucose-D labeling, glucose-free DMEM medium supplemented with 10% FBS, P/S (100 U/ml), and 25 mM glucose-D was used to culture cells for 72 hours. For fatty acid and cholesterol analogs labeling, cells were incubated within a medium containing analogs at a final concentration of 20 μM for 48 hours. Cells were then fixed with 10% neutral buffered formalin for 30 min and washed with phosphate-buffered saline (PBS) three times, before hSRS imaging at Raman spectral region from 2100 to 2300 cm−1

## Spontaneous Raman spectroscopy

The spontaneous Raman spectra of the pure chemical samples were acquired using Raman spectroscopy (inVia Raman microscope, Re nishaw) with a 532 nm laser source and a 20× air objective. The grating was set to 2600 cm−1 and acquisition time was between 2 and 60 s.

## PAS staining

Cells seeding in 35 mm glass-bottom dishes were fixed with 10% neutral-buffered formalin for 15 min, followed by three washe with PBS. The cells were then incubated in 1% periodic acid (Sigma-Aldrich, 3951) for 30 min at 20°C and washed three times with deionized water. The cells were incubated with Schiff’s reagent (Sigma-Aldrich, 3952016) for 30 min. After washing three times with deionized water, the cells were imaged under a microscope (BX 51, Olympus) equipped with a color complementary metaloxide semiconductor camera (Thorlabs, CS165CU).

## Cell viability assay

The MTS assay (Abcam, #ab197010) was used to measure cell viability. After overnight seeding of cells in 96-well plates at a density of 1500 to 2000 cells per well, chemotherapy was added to the cell culture at the indicated concentrations for 72 hours. After incubat ing with MTS reagent for 1 hour, cell viability was evaluated by measuring the absorbance at 490 nm using a plate reader.

## RNA extraction and reverse transcription PCR

Total RNA was extracted from cells using the RNeasy Mini Kit (Qiagen Inc.). RNA was reverse-transcribed using the iScript cDNA Synthesis Kit (Bio-Rad). Reverse transcription polymerase chain reaction (RT-PCR) was performed using StepOne Plus RT PCR (Applied Biosystems) with Power SYBR Green Master Mix (Thermo Fisher Scientific) following the manufacturer’s protocol. The melting curve and cycle threshold (Ct) of the gene of interest and the housekeeping gene (RPLP0) were recorded. The relative mRNA expression level (ΔCt) was calculated by subtracting the housekeeping gene Ct value from the target gene Ct value. Results are presented as means ± SD. The primer sequences are listed in table S2.

## Quantification and statistical analysis

All the data are presented as means ± SD unless otherwise specified. Two-tailed Student’s t test and Mann-Whitney U test were used to analyze statistical significance. N represents the sample size used in each experiment. P < 0.05 was considered statistically significant. Sample size, n, and statistical parameters are shown in the figure legends. The discrimination accuracy and standardized canonica discriminant function coefficients were calculated using the Statis tical Package for the Social Sciences (SPSS)linear discriminant func tion analysis. ImageJ, MATLAB, Ilastik, and Microsoft Excel were used for data processing and analysis. Figures were generated and organized using Origin and Microsoft PowerPoint software.

## Supplementary Materials

This PDF file includes:

Figs. S1 to S10

Tables S1 and S2

## REFERENCES AND NOTES

1. K. D. Miller, L. Nogueira, A. B. Mariotto, J. H. Rowland, K. R. Yabroff, C. M. Alfano, A. Jemal, J. L. Kramer, R. L. Siegel, Cancer treatment and survivorship statistics, 2019. CA Cancer J. Clin. 69, 363–385 (2019)  
2. X. Wang, H. Zhang, X. Chen, Drug resistance and combating drug resistance in cancer. Cancer Drug Resist. 2, 141–160 (2019).  
3. X. Chen, S. Chen, D. Yu, Metabolic reprogramming of chemoresistant cancer cells and the potential significance of metabolic regulation in the reversal of cancer chemoresistance. Metabolites 10, 289 (2020).  
4. J. Kopecka, P. Trouillas, A. C. Gasparovic, E. Gazzano, Y. G. Assaraf, C. Riganti, Phospholipid and cholesterol: Inducers of cancer multidrug resistance and therapeutic targets. Drug Resist. Updat. 49, 100670 (2020).  
5. S. Hultsch, M. Kankainen, L. Paavolainen, R. M. Kovanen, E. Ikonen, S. Kangaspeska V. Pietiainen, O. Kallioniemi, Association of tamoxifen resistance and lipid reprogrammin in breast cancer. BMC Cancer 18, 850 (2018).  
6. M. Poirot, S. Silvente-Poirot, R. R. Weichselbaum, Cholesterol metabolism and resistance t tamoxifen. Curr. Opin. Pharmacol. 12, 683–689 (2012)  
7. L. Hamadneh, R. Abuarqoub, A. Alhusban, M. Bahader, Upregulation of PI3K/AKT/PTEN pathway is correlated with glucose and glutamine metabolic dysfunction during tamoxi fen resistance development in MCF-7 cells. Sci. Rep. 10, 21933 (2020).  
8. X. Liang, Y. Huang, Physical state changes of membrane lipids in human lung adenocar cinoma A(549) cells and their resistance to cisplatin. Int. J. Biochem. Cell Biol. 34, 1248–1255 (2002).  
9. Y. Wu, R. Si, H. Tang, Z. He, H. Zhu, L. Wang, Y. Fan, S. Xia, Z. He, Q. Wang, Cholestero reduces the sensitivity to platinum-based chemotherapy via upregulating ABCG2 in lung adenocarcinoma. Biochem. Biophys. Res. Commun. 457, 614–620 (2015)  
10. K. C. Huang, J. Li, C. Zhang, Y. Tan, J. X. Cheng, Multiplex stimulated Raman scattering imaging cytometry reveals lipid-rich protrusions in cancer cells under stress condition. iScience 23, 100953 (2020)  
11. J. Li, X. Qu, J. Tian, J. T. Zhang, J. X. Cheng, Cholesterol esterification inhibition and gem citabine synergistically suppress pancreatic ductal adenocarcinoma proliferation. PLOS ONE 13, e0193318 (2018).  
12. Y. Tan, J. Li, G. Zhao, K. C. Huang, H. Cardenas, Y. Wang, D. Matei, J. X. Cheng, Metaboli reprogramming from glycolysis to fatty acid uptake and beta-oxidation in platinum-resistant cancer cells. Nat. Commun. 13, 4554 (2022)  
13. S. Pan, M. Fan, Z. Liu, X. Li, H. Wang, Serine, glycine and one-carbon metabolism in cancer (Review). Int. J. Oncol. 58, 158–170 (2021).  
14. D. Jia, M. Lu, K. H. Jung, J. H. Park, L. Yu, J. N. Onuchic, B. A. Kaipparettu, H. Levine, Eluci dating cancer metabolic plasticity by coupling gene regulation with metabolic pathways. Proc. Natl. Acad. Sci. U.S.A. 116, 3909–3918 (2019)  
15. D. R. Schmidt, R. Patel, D. G. Kirsch, C. A. Lewis, M. G. Vander Heiden, J. W. Locasale, Me tabolomics in cancer research and emerging applications in clinical oncology. CA Cancer J. Clin. 71, 333–358 (2021).  
16. D. B. Liesenfeld, N. Habermann, R. W. Owen, A. Scalbert, C. M. Ulrich, Review of mass spectrometry-based metabolomics in cancer research. Cancer Epidemiol. Biomarkers Prev. 22, 2182–2201 (2013).  
17. C. E. Meacham, S. J. Morrison, Tumour heterogeneity and cancer cell plasticity. Nature 501, 328–337 (2013).  
18. F. Luond, S. Tiede, G. Christofori, Breast cancer as an example of tumour heterogeneity and tumour cell plasticity during malignant progression. Br. J. Cancer 125, 164–175 (2021).  
19. C. Shembrey, N. D. Huntington, F. Hollande, Impact of tumor and immunological heterogeneity on the anti-cancer immune response. Cancers (Basel) 11, 1217 (2019).  
20. K. E. Hamilton, M. F. Bouwer, L. L. Louters, B. D. Looyenga, Cellular binding and uptake of fluorescent glucose analogs 2-NBDG and 6-NBDG occurs independent of membrane glucose transporters. Biochimie 190, 1–11 (2021).  
21. C. Zhang, D. Zhang, J. X. Cheng, Coherent Raman scattering microscopy in biology and medicine. Annu. Rev. Biomed. Eng. 17, 415–445 (2015).  
22. S. Yue, J. X. Cheng, Deciphering single cell metabolism by coherent Raman scattering microscopy. Curr. Opin. Chem. Biol. 33, 46–57 (2016).  
23. T. T. Le, T. B. Huff, J. X. Cheng, Coherent anti-Stokes Raman scattering imaging of lipids in cancer metastasis. BMC Cancer 9, 42 (2009).  
24. I. Pope, F. Masia, K. Ewan, A. Jimenez-Pascual, T. C. Dale, F. A. Siebzehnrubl, P. Borri, W. Langbein, Identifying subpopulations in multicellular systems by quantitative chemical imaging using label-free hyperspectral CARS microscopy. Analyst 146, 2277–2291 (2021).  
25. M. C. Potcoava, G. L. Futia, J. Aughenbaugh, I. R. Schlaepfer, E. A. Gibson, Raman and coherent anti-Stokes Raman scattering microscopy studies of changes in lipid content and composition in hormone-treated breast and prostate cancer cells. J. Biomed. Opt. 19, 111605 (2014).  
26. T. Guerenne-Del Ben, V. Couderc, L. Duponchel, V. Sol, P. Leproux, J. M. Petit, Multiplex coherent anti-Stokes Raman scattering microspectroscopy detection of lipid droplets in cancer cells expressing TrkB. Sci. Rep. 10, 16749 (2020).  
27. J. X. Cheng, X. S. Xie, Vibrational spectroscopic imaging of living systems: An emerging platform for biology and medicine. Science 350, aaa8870 (2015).  
28. S. Yue, J. Li, S. Y. Lee, H. J. Lee, T. Shao, B. Song, L. Cheng, T. A. Masterson, X. Liu, T. L. Ratliff, J. X. Cheng, Cholesteryl ester accumulation induced by PTEN loss and PI3K/AKT activation underlies human prostate cancer aggressiveness. Cell Metab. 19, 393–406 (2014).  
29. J. Li, D. Gu, S. S. Lee, B. Song, S. Bandyopadhyay, S. Chen, S. F. Konieczny, T. L. Ratliff, X. Liu, J. Xie, J. X. Cheng, Abrogating cholesterol esterification suppresses growth and metastasis of pancreatic cancer. Oncogene 35, 6378–6388 (2016)  
30. Y. Ozeki, W. Umemura, Y. Otsuka, S. Satoh, H. Hashimoto, K. Sumimura, N. Nishizawa, K. Fukui, K. Itoh, High-speed molecular spectral imaging of tissue with stimulated Rama scattering. Nat. Photonics 6, 845–851 (2012)  
31. D. L. Zhang, P. Wang, M. N. Slipchenko, D. Ben-Amotz, A. M. Weiner, J.-X. Cheng, Quantitative vibrational imaging by hyperspectral stimulated Raman scattering microscopy and multivariate curve resolution analysis. Anal. Chem. 85, 98–106 (2013).  
32. C.-S. Liao, M. N. Slipchenko, P. Wang, J. Li, S.-Y. Lee, R. A. Oglesbee, J.-X. Cheng, Microsecond scale vibrational spectroscopic imaging by multiplex stimulated Raman scattering microscopy. Light Sci. Appl. 4, e265 (2015).  
33. D. Fu, F. K. Lu, X. Zhang, C. Freudiger, D. R. Pernik, G. Holtom, X. S. Xie, Quantitative chemical imaging with multiplex stimulated Raman scattering microscopy. J. Am. Chem Soc. 134, 3623–3626 (2012).  
34. D. Fu, G. Holtom, C. Freudiger, X. Zhang, X. S. Xie, Hyperspectral imaging with stimulated Raman scattering by chirped femtosecond lasers. J. Phys. Chem. B 117, 4634–4640 (2013).  
35. C. S. Liao, K.-C. Huang, W. L. Hong, A. J. Chen, C. Karanja, P. Wang, G. Eakins, J.-X. Cheng, Stimulated Raman spectroscopic imaging by microsecond delay-line tuning. Optica 3, 1377–1380 (2016).  
36. H. Lin, H. J. Lee, N. Tague, J. B. Lugagne, C. Zong, F. Deng, J. Shin, L. Tian, W. Wong M. J. Dunlop, J. X. Cheng, Microsecond fingerprint stimulated Raman spectroscopic imaging by ultrafast tuning and spatial-spectral learning. Nat. Commun. 12, 3052 (2021)  
37. F.-K. Lu, S. Basu, V. Igras, M. P. Hoang, M. B. Ji, D. Fu, G. R. Holtom, V. A. Neel, C. W. Freudiger, D. E. Fisher, X. S. Xie, Label-free DNA imaging in vivo with stimulated Raman scattering microscopy. Proc. Natl. Acad. Sci. U.S.A. 112, 11624–11629 (2015)  
38. C. Zhang, K.-C. Huang, B. Rajwa, J. Li, S. Yang, H. Lin, C.-s. Liao, G. Eakins, S. Kuang V. Patsekin, Stimulated Raman scattering flow cytometry for label-free single-particle analysis. Optica 4, 103–109 (2017).  
39. D. Fu, X. S. Xie, Reliable cell segmentation based on spectral phasor analysis of hyper spectral stimulated Raman scattering imaging data. Anal. Chem. 86, 4115–4119 (2014).  
40. P. Wang, B. Liu, D. Zhang, M. Y. Belew, H. A. Tissenbaum, J.-X. Cheng, Imaging lipid me tabolism in live Caenorhabditis elegans using fingerprint vibrations. Angew. Chem. Int. Ed Engl. 53, 11787–11792 (2014).  
41. J. Li, S. Condello, J. Thomes-Pepin, X. Ma, Y. Xia, T. D. Hurley, D. Matei, J. X. Cheng, Lipid desaturation is a metabolic marker and therapeutic target of ovarian cancer stem cells. Cel Stem Cell 20, 303–314.e5 (2017).  
42. J. Du, Y. Su, C. Qian, D. Yuan, K. Miao, D. Lee, A. H. C. Ng, R. S. Wijker, A. Ribas, R. D. Levine J. R. Heath, L. Wei, Raman-guided subcellular pharmaco-metabolomics for metastatic melanoma cells. Nat. Commun. 11, 4830 (2020)  
43. L. Y. Zhang, L. Y. Shi, Y. H. Shen, Y. P. Miao, M. Wei, N. X. Qian, Y. N. Liu, W. Min, Spectra tracing of deuterium for imaging glucose metabolism. Nat. Biomed. Eng. 3, 402–413 (2019).  
44. P. Wang, J. Li, P. Wang, C. R. Hu, D. Zhang, M. Sturek, J. X. Cheng, Label-free quantitative imaging of cholesterol in intact tissues by hyperspectral stimulated Raman scattering microscopy. Angew. Chem. Int. Ed. Engl. 52, 13042–13046 (2013)  
45. C. H. Camp Jr., Y. J. Lee, J. M. Heddleston, C. M. Hartshorn, A. R. Hight Walker, J. N. Rich J. D. Lathia, M. T. Cicerone, High-speed coherent Raman fingerprint imaging of biologica tissues. Nat. Photonics 8, 627–634 (2014)  
46. W. W. Chen, G. A. Lemieux, C. H. Camp Jr., T. C. Chang, K. Ashrafi, M. T. Cicerone, Spec troscopic coherent Raman imaging of Caenorhabditis elegans reveals lipid particle diver sity. Nat. Chem. Biol. 16, 1087–1095 (2020).  
47. A. De la Cadena, F. Vernuccio, A. Ragni, G. Sciortino, R. Vanna, C. Ferrante, N. Pediconi C. Valensise, L. Genchi, S. P. Laptenok, A. Doni, M. Erreni, T. Scopigno, C. Liberale, G. Ferrari M. Sampietro, G. Cerullo, D. Polli, Broadband stimulated Raman imaging based on multi channel lock-in detection for spectral histopathology. APL Photonics 7, 076104 (2022)  
48. H. Ni, P. Lin, Y. Zhu, M. Zhang, Y. Tan, Y. Zhan, Z. Wang, J. X. Cheng, Multiwindow SRS imaging using a rapid widely tunable fiber laser. Anal. Chem. 93, 15703–15711 (2021)  
49. I. J. Pence, B. A. Kuzma, M. Brinkmann, T. Hellwig, C. L. Evans, Multi-window sparse spectra sampling stimulated Raman scattering microscopy. Biomed. Opt. Express 12, 6095–6114 (2021).  
50. R. Tibshirani, Regression shrinkage and selection via the lasso. J. R. Stat. Soc. Ser. B Meth odol. 58, 267–288 (1996)  
51. M. Maggioni, V. Katkovnik, K. Egiazarian, A. Foi, Nonlocal transform-domain filter for vol umetric data denoising and reconstruction. IEEE Trans. Image Process. 22, 119–133 (2013).  
52. P. S. Ward, C. B. Thompson, Metabolic reprogramming: A cancer hallmark even warburg did not anticipate. Cancer Cell 21, 297–308 (2012).  
53. J. Chen, C. Zhang, Y. Mi, F. Chen, D. Du, CREB1 regulates glucose transport of glioma cel line U87 by targeting GLUT1. Mol. Cell. Biochem. 436, 79–86 (2017).  
54. C. Holohan, S. Van Schaeybroeck, D. B. Longley, P. G. Johnston, Cancer drug resistance: A evolving paradigm. Nat. Rev. Cancer 13, 714–726 (2013)  
55. Y. Jia, J. Xie, Promising molecular mechanisms responsible for gemcitabine resistance in cancer. Genes Dis. 2, 299–306 (2015).  
56. M. Amrutkar, I. P. Gladhaug, Pancreatic cancer chemoresistance to gemcitabine. Cancer (Basel) 9, 157 (2017).  
57. R. Andersson, U. Aho, B. I. Nilsson, G. J. Peters, M. Pastor-Anglada, W. Rasch, M. L. Sandvold Gemcitabine chemoresistance in pancreatic cancer: Molecular mechanisms and potentia solutions. Scand. J. Gastroenterol. 44, 782–786 (2009).  
58. C. Giesen, H. A. O. Wang, D. Schapiro, N. Zivanovic, A. Jacobs, B. Hattendorf, P. J. Schuffler D. Grolimund, J. M. Buhmann, S. Brandt, Z. Varga, P. J. Wild, D. Günther, B. Bodenmiller, Highly multiplexed imaging of tumor tissues with subcellular resolution by mass cytom etry. Nat. Methods 11, 417–422 (2014)  
59. G. Yagnik, Z. Liu, K. J. Rothschild, M. J. Lim, Highly multiplexed immunohistochemica MALDI-MS imaging of biomarkers in tissues. J. Am. Soc. Mass Spectrom. 32, 977–988 (2021).  
60. M. A. Brunet, M. L. Kraft, Toward understanding the subcellular distributions of cholestero and sphingolipids using high-resolution NanoSIMS imaging. Acc. Chem. Res. 56, 752–762 (2023).  
61. N. Yamamoto, M. Ueda, T. Sato, K. Kawasaki, K. Sawada, K. Kawabata, H. Ashida, Mea surement of glucose uptake in cultured cells. Curr. Protoc. Pharmacol. 71, 12.14.1–12.14.26 (2011).  
62. R. Long, L. Zhang, L. Shi, Y. Shen, F. Hu, C. Zeng, W. Min, Two-color vibrational imaging of glucose metabolism using stimulated Raman scattering. Chem. Commun. (Camb.) 54, 152–155 (2018).  
63. S. Oh, C. Lee, W. Yang, A. Li, A. Mukherjee, M. Basan, C. Ran, W. Yin, C. J. Tabin, D. Fu, X. S. Xie, M. W. Kirschner, Protein and lipid mass concentration measurement in tissues by stimu lated Raman scattering microscopy. Proc. Natl. Acad. Sci. U.S.A. 119, e2117938119 (2022)  
64. J. Li, P. Lin, Y. Tan, J. X. Cheng, Volumetric stimulated Raman scattering imaging of cleare tissues towards three-dimensional chemical histopathology. Biomed. Opt. Express 10, 4329–4339 (2019).  
65. Y. Zhao, E. B. Butler, M. Tan, Targeting cellular metabolism to improve cancer therapeutics. Cell Death Dis. 4, e532 (2013).  
66. G. Bergers, S. M. Fendt, The metabolism of cancer cells during metastasis. Nat. Rev. Cancer 21, 162–180 (2021).  
67. B. Faubert, A. Solmonson, R. J. DeBerardinis, Metabolic reprogramming and cancer pro gression. Science 368, eaaw5473 (2020).  
68. A. M. Intlekofer, L. W. S. Finley, Metabolic signatures of cancer cells and stem cells. Nat Metab. 1, 177–188 (2019).  
69. J. J. Heindel, B. Blumberg, M. Cave, R. Machtinger, A. Mantovani, M. A. Mendez, A. Nadal, P. Palanza, G. Panzica, R. Sargis, L. N. Vandenberg, F. Vom Saal, Metabolism disrupting chemicals and metabolic disorders. Reprod. Toxicol. 68, 3–33 (2017).  
70. B. H. Goodpaster, L. M. Sparks, Metabolic flexibility in health and disease. Cell Metab. 25, 1027–1036 (2017).  
71. D. J. Drucker, Diabetes, obesity, metabolism, and SARS-CoV-2 infection: The end of the beginning. Cell Metab. 33, 479–498 (2021).  
72. R. J. DeBerardinis, C. B. Thompson, Cellular metabolism and disease: What do metabolic outliers teach us? Cell 148, 1132–1144 (2012)  
73. R. Wang, D. R. Green, Metabolic reprogramming and metabolic dependency in T cells Immunol. Rev. 249, 14–26 (2012).  
74. S. Berg, D. Kutra, T. Kroeger, C. N. Straehle, B. X. Kausler, C. Haubold, M. Schiegg, J. Ales T. Beier, M. Rudy, K. Eren, J. I. Cervantes, B. Xu, F. Beuttenmueller, A. Wolny, C. Zhang U. Koethe, F. A. Hamprecht, A. Kreshuk, ilastik: Interactive machine learning for (bio)image analysis. Nat. Methods 16, 1226–1232 (2019).

## Acknowledgments

Funding: This work was supported by NIH grant R33CA223581 (to J.-X.C.), NIH gran R01CA224275 (to J.-X.C.), NIH grant R35GM136223 (to J.-X.C.). Author contributions: Y.T., H.L. and J.-X.C. designed the experiments. Y.T. and H.L. performed the experiments, analyzed the data, and cowrote the manuscript. All authors have read and edited the manuscript

Competing interests: The authors declare that they have no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present i the paper and/or the Supplementary Materials. The raw data and codes are available in Zenodo (DOI:10.5281/zenodo.7826365)

Submitted 9 January 2023

Accepted 14 July 2023

Published 16 August 202

10.1126/sciadv.adg6061

# ScienceAdvances

## Profiling single cancer cell metabolism via high-content SRS imaging with chemical sparsity

Yuying Tan, Haonan Lin, and Ji-Xin Cheng

Sci. Adv. 9 (33), eadg6061. DOI: 10.1126/sciadv.adg6061

View the article online

https://www.science.org/doi/10.1126/sciadv.adg6061

Permissions

https://www.science.org/help/reprints-and-permissions

Use of this article is subject to the Terms of service