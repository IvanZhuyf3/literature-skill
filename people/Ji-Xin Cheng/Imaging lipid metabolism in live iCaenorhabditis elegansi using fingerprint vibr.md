# Imaging Lipid Metabolism in Live Caenorhabditis elegans Using Fingerprint Vibrations\*\*

Ping Wang, Bin Liu, Delong Zhang, Micah Y. Belew, Heidi A. Tissenbaum,\* and Ji-Xin Cheng\*

Abstract: Quantitation of lipid storage, unsaturation, and oxidation in live C. elegans has been a long-standing obstacle. The combination of hyperspectral stimulated Raman scattering imaging and multivariate analysis in the fingerprint vibration region represents a platform that allows the quantitative mapping of fat distribution, degree of fat unsaturation, lipid oxidation, and cholesterol storage in vivo in the whole worm. Our results reveal for the first time that lysosome-related organelles in intestinal cells are sites for storage of cholesterol in C. elegans.

extensively used for studying the impact of lipid metabolism on aging and disease.[1] Yet, tools for the identification and quantitation of chemical composition of stored lipids in living animals remain to be developed. The “vital” dyes Nile red[2] and BODIPY[3] were historically adopted for fat staining through feeding live worms. Recent studies found that both Nile red and BODIPY largely stain the lysosome-related organelles (LROs) rather than the fat stored in the intestinal cells, gonad, germ line, and hypodermis.[4] Thus, the lipid storages and phenotypes revealed by Nile red and BODIPY fluorescence do not correlate with the fat level measured by fixative staining, such as Sudan black and Oil red O, nor with biochemical analysis.[3, 5] Attempts to identify the ubiquitous fat storage in C. elegans were made by using nonlinear vibrational imaging technologies[6] based on coherent anti-Stokes Raman scattering $( \mathrm { C A R S } ) ^ { [ 7 ] }$ or stimulated Raman scattering (SRS).[8] Single-frequency CARS[9] and SRS[10] allowed visualization of lipid droplets in live C. elegans by exploiting signals from the intrinsic carbon-hydrogen (C-H) stretching vibration. Despite this chemical bond specificity for lipids, the mapped fat distribution in the body of C. elegans did not fully co-localize with the pattern produced by vital or fixative dyes.[9b, 10, 11] In fact, as nearly all biomolecules, including protein, cholesterol, and triglyceride, contribute to the C-H vibrational signals in the highly congested spectral window from 2800 to $3 1 0 0 \mathrm { c m } ^ { - 1 } .$ , it is not possible to distinguish protein-rich organelles or gut granules[12] from fat droplets in the body of C. elegans using single-frequency CARS or SRS. In addition, the CARS/SRS contrast based on C-H stretch vibrations is dominated by the signal from lipid droplets, making it difficult to detect other cellular compartments inside the worm.

Herein, we overcame the above-mentioned limitations by integration of hyperspectral SRS imaging[13] (Supporting Information, Figure S1), k-means clustering, and multivariate curve resolution (MCR) analysis[14] (Supporting Information, Figure S2) to identify and quantitate the chemical contents of intracellular organelles in live C. elegans, which is out of reach for either fluorescence or single-frequency SRS microscopy. Using hyperspectral SRS images that cover a fingerprint vibration window and spectral groups identified by k-means clustering as MCR inputs, we show the quantitative mapping of fat distribution, the degree of fat unsaturation, lipid oxidation, and cholesterol storage in vivo in a whole worm. Our results reveal that lysosome-related organelles are sites for storage of cholesterol.

We first performed hyperspectral SRS imaging in the Raman region from 1620 to 1800 cm-1 of wild-type N2 worms and daf-2 (e1370) mutants, which bear a mutation of insulinlike growth factor 1 (IGF-1) receptor in C. elegans.[15] Figure 1a,b presents the MCR results of a single wild-type worm and a daf-2 mutant both at the L2 stage, in which the development of intestinal cells dominates the worm growth. In all worms examined, three types of subcellular compartments are found in most intestinal cells, as shown by the higher magnification images of the daf-2 mutant (Figure 1c–f and Supporting Information, Movie S1). The concentration maps produced by the MCR algorithm clearly reveal the distributions of neutral fat droplets, protein-rich organelles, and oxidized lipids in distinct sites of intestinal cells. The content in the lipid droplets is primarily in the form of triglyceride (Figure 1e), confirmed by Raman peaks of the acyl C=C bond at 1655 cm-1 and the ester C=O bond at $1 7 4 5 \mathrm { c m } ^ { - 1 }$ (Figure 1 h). The proteins are distributed more uniformly in the entire worm body, including the hypodermis, intestinal lumen, and intestinal cells (Figure 1 g), characterized by the broad amide I band with a maximum at 1650 cm-1 [\*] Dr. P. Wang, B. Liu, Prof. J.-X. Cheng Weldon School of Biomedical Engineering, Purdue University West Lafayette, IN 47907 (USA) E-mail: jcheng@purdue.edu D. Zhang, Prof. J.-X. Cheng Department of Chemistry, Purdue University West Lafayette, IN 47906 (USA) M. Y. Belew, Prof. H. A. Tissenbaum Program in Gene Function and Expression University of Massachusetts Medical Schoo Worcester, MA 01605 (USA) E-mail: Heidi.Tissenbaum@umassmed.edu

[\*\*] Some of the strains used in this study were kindly provided by the Caenorhabditis Genetics Center funded by the NIH Office of Research Infrastructure Programs (P40 OD010440). This work was supported by National Institutes of Health grant GM104681 to J.X.C. and grant AG031237 to H.A.T., and an endowment from the William Randolph Hearst Foundation to H.A.T.

Supporting information for this article (including details about the experimental setup, specimen preparation, and MCR algorithm) is available on the WWW under http://dx.doi.org/10.1002/anie. 201406029.

![](images/16a273a58548802c3836007801210b2b81737b8d3815924e0b594ab4444a9733.jpg)  
Figure 1. Compositional analysis of intracellular compartments in whole C. elegans worms by hyperspectral SRS imaging, k-means clustering, and MCR analysis. a,b) MCR-retrieved concentration maps of neutral fat droplets, lysosome-related organelles (LROs), oxidized lipids, and protein in the body of whole wild type worms and daf-2 mutants. Scale bar: 50 mm. c) Zoom-in of intestine cells indicated in (b). d–g) MCR-reconstructed concentration images of LROs, fat droplets, oxidized lipids, and protein, respectively. h) MCR-retrieved Raman spectra of corresponding compartments. The dotted line represents the pump–probe signal. Scale bar: 5 mm. i) Quantitation of amounts of LROs, fat droplets, and oxidized lipids in wild-type N2 and daf-2 mutants (n  5) based on SRS spectral images of intestinal cells.

(Figure 1h). In addition to the fat stores, we discovered one type of protein-rich organelles in large amounts filling the intestinal cells (Figure 1 d). Importantly, these spherica organelles are spectrally distinct from either lipid droplets or pure protein, based on the MCR-retrieved Raman spectra. Compared to the amide I band of protein, the spectral peak of those organelles is shifted to higher wave numbers, implying that they contain a significant amount of cholesterol, which possesses the sterol C=C stretching band at $1 6 6 9 \mathrm { c m } ^ { - 1 }$ (Figure 1 h, green curve).[13f] These cholesterol-containing compartments are assigned to be lysosome-related organelles based on detailed evidence shown below.

A third type of compartment found in the intestinal cells (Figure 1 f) contains oxidized lipids, for which the SRS Raman spectrum showed a shoulder peak at 1680 cm-1 , indicating the presence of an aldehyde.[16] We note that a pump–probe signal, which is independent of the Raman shift, was observed in the raw Raman spectrum, thus implying that these compartments contain chromophores. The MCR algorithm is able to separate the SRS signal from the pump– probe background and retrieve background-free Raman spectra of detected chemicals (Figure 1 h). To further explore the nature of the oxidized lipids, hyperspectral SRS imaging was performed in the region from 1520 to $1 7 0 0 \mathrm { c m } ^ { - 1 }$ (Supporting Information, Figure S3). A specific Raman peak at $1 5 5 5 \mathrm { c m } ^ { - 1 }$ was identified and assigned to the retinal C=C stretching band.[17] Together, these characteristic Raman peaks and the pump–probe signal suggest that we detected and located retinaldehyde, a known aging-related pigment stored in lipofuscin.[17]

To quantify the amount of fat, LROs, and oxidized lipids in worms, we performed SRS imaging of intestinal cells in multiple wild-type worms (Supporting Information, Fig ure S4, $n = 5 )$ and $d a f { - } 2$ mutants (Supporting Information, Figure $\mathrm { S } 5 , n = 6 )$ . Areas in the intestinal cells occupied by fat, LROs, and oxidized lipids were normalized by the total imaged area of the worm (Supporting Information, Figure S6). In wild-type worms, 18 % of the area of the intestinal cells is filled by cholesterol-rich LROs and 4 % by neutral fat. Oxidized lipids appear much less in the whole body and the occupied area is less than 0.3 % (Figure 1 i). Compared to the wild type, the daf-2 insulin/IGF-1 receptor mutants show a 1.2- and 3.6-fold increase in LROs and neutral fat storages, respectively. In addition, the amount of oxidized lipids is 6- fold greater than in the wild type, suggesting that the insulin/ IGF-1 signaling pathway regulates not only the neutral fat storage but also lipid oxidation. The measured difference of neutral fat between wild type and daf-2 mutants is in agreement with earlier results obtained by single-frequency SRS and thin-layer chromatography/gas chromatography.[10]

To investigate whether the observed cholesterol-containing organelles are LROs, we performed hyperspectral SRS imaging on adult wild-type worms fed with LysoTracker, a marker for LROs (Supporting Information, Movie S2). The MCR concentration map in Figure 2a clearly shows that the neutral lipid droplets are distributed in both intestinal cells and undifferentiated germ cells in the gonad arm located above the intestine. The content of these lipid droplets is primarily in the form of triglyceride, confirmed by the presence of acyl C=C and C=O stretching band (Figure 2 f).

![](images/1fc37f72216d8665cec79233d0329ed911e14d4f5d36ce71080773b5db773dce.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-labeled Lipids against a black background (no text or symbols)
</details>

![](images/fc20fbc68eff242ef68ccd6508e351fd58df6b02095765516196e140931ef36a.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing protein expression levels with green and blue staining (no text or symbols)
</details>

![](images/8440af036e72ea499b42c7dd64196acb9483eca6d01bcd7924250069ea7c476e.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing green-labeled cellular structures against a black background, labeled 'Cholesterol' in top left corner (no other text or symbols)
</details>

![](images/d59a6daa9ed31ffa7f99f6d52eab291b6bcd75ccc6db4b7e06845c2e44923b3a.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing red and green cellular structures with blue arrow annotations (no text or symbols)
</details>

![](images/78e15f853528c6bfc97db094fa57edd23cd453e81143bc3826ec3b7ae16faa82.jpg)

<details>
<summary>natural_image</summary>

Microscopy image showing fluorescently labeled cells under TPEF (LysoTracker) condition, no text or symbols present
</details>

![](images/e54e73f29e2186baa4dcd57622c608d3e18d98bfae79ba7a5cb4d914b5d0d526.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing red and green labeled cells against a dark background, with 'Glo-1::GFP' label in top right (no other text or symbols)
</details>

![](images/85f7fc25901de446fa461692b4cc9695e05be714c9de3086ee1a9a8acc90d9e5.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological structure labeled 'TPEF' (no additional text or symbols visible)
</details>

![](images/4a3cf36890d100717ea63cfb507f7fefa9825aca371d8b713eeb04d03eb4af8e.jpg)

<details>
<summary>text_image</summary>

chup-1 mutant
</details>

f SRS Raman spectra at pixels  
![](images/585b195a6dc0b3d2d40fa40e4c736d39aa2152fb1340af5aa1cd764514d60982.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Lipids | LROs | Protein |
| ------------------ | ------ | ---- | ------- |
| 1620               | 0.1    | 0.3  | 0.2     |
| 1650               | 1.6    | 1.4  | 0.5     |
| 1680               | 0.1    | 0.1  | 0.1     |
| 1710               | 0.0    | 0.0  | 0.0     |
| 1740               | 0.2    | 0.1  | 0.1     |
| 1770               | 0.1    | 0.1  | 0.1     |
| 1800               | 0.0    | 0.0  | 0.0     |
</details>

g MCR retrieved spectra

![](images/49c1ff4433b55968d81c8deee3176f98586eb79f766335c0d45f83df86f11629.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Lipids | Cholesterol | Protein |
| ------------------ | ------ | ----------- | ------- |
| 1620               | 0.0    | 0.0         | 0.0     |
| 1650               | 1.6    | 0.0         | 0.9     |
| 1670               | 1.6    | 1.6         | 0.9     |
| 1700               | 0.0    | 0.0         | 0.0     |
| 1740               | 0.2    | 0.0         | 0.2     |
| 1770               | 0.1    | 0.0         | 0.1     |
| 1800               | 0.0    | 0.0         | 0.0     |
</details>

![](images/43e8830e8110a8cde350dff3401118555978646b3b9ef219fab3a29db3d2c2e6.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | chup-1 Lipids | chup-1 LROs | N2 LROs |
| ------------------ | ------------- | ----------- | ------- |
| 1620               | ~0.2          | ~0.3        | ~0.4    |
| 1650               | ~1.6          | ~0.8        | ~1.4    |
| 1680               | ~0.2          | ~0.1        | ~0.1    |
| 1710               | ~0.0          | ~0.0        | ~0.0    |
| 1740               | ~0.3          | ~0.1        | ~0.1    |
| 1770               | ~0.1          | ~0.0        | ~0.0    |
| 1800               | ~0.0          | ~0.0        | ~0.0    |
</details>

Figure 2. Hyperspectral SRS imaging and multivariate data analysis identify cholesterol storage compartments. a–c) MCR-reconstructed concentration maps of neutral lipid droplets, protein, and cholesterol in LROs. d) Color-overlay image of (a–c). e) TPEF image of the same area stained with vital LysoTracker. f) SRS spectra at pixels indicated by arrows in (d). g) MCR-retrieved Raman spectra of lipids, cholesterol and protein. h,i) MCR-concentration maps and TPEF image of LRO-specific GLO-1:GFP worm. j) MCR image of chup-1 mutant. k) SRS spectra at indicated compartments in (j). Dashed spectrum of LROs in the wild type is provided for comparison. Scale bar: 10 mm.

The retrieved protein map (Figure 2b) not only shows the protein distribution in regions of intestinal cells and lumen, but also reveals many compartments with a similar size of lipid droplets. These protein-rich organelles do not overlap with lipid droplets, but co-localized with the MCR-retrieved third component shown in Figure 2 c. The corresponding Raman spectrum derived from the MCR (Figure 2g, green curve) indicates a characteristic Raman peak of cholesterol at 1670 cm-1 , and therefore suggests that these protein-rich organelles store a significant amount of cholesterol.[13 f]

Raman spectrum acquired at the position of LROs (Supporting Information, Figure S7) confirmed this finding. We further performed two-photon-excited fluorescence (TPEF) imaging of LysoTracker in the same area of the worm (Figure 2 e). Comparing the MCR color overlay image (Figure 2d) and the TPEF image of LysoTracker highlights the colocalization of LROs with the cholesterol-containing compartments other than the lipid droplets. Figure 2 f presents the raw SRS spectra of lipid droplets, LROs, and background protein at pixels indicated by arrows in Figure 2 d. Figure 2 g presents the MCR-decomposed SRS spectra for neutral lipids, cholesterol, and protein. These data collectively suggest that LROs store both the protein represented by the amide I band and cholesterol represented by the sterol C= C band. To provide additional evidence that these cholesterol-rich compartments are indeed LROs, wild-type worms that bear a transgenic marker for $\mathrm { L R O s } ^ { \mathrm { [ 4 c ] } }$ (hjIs9 [glo-1:gfp]) were imaged by hyperspectral SRS (Figure 2 h) and TPEF signals (Figure 2 i). As expected, all spherical LROs structures recognized by MCR were encircled by GLO-1:GFP fluorescence.

![](images/16e01aa4c5e7483976e3d22baa892c7ca6875b5ff6d0deafd3319ff59af77871.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing cellular structures with purple and yellow staining (no text or symbols)
</details>

![](images/60f5afd579e1f56c3427af50a2ecafbd69f86a41377a5c826efb52d4b35d594b.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | LDs in lumen | LDs in oocytes | LDs in hypodermis |
| ------------------ | ------------ | -------------- | ----------------- |
| 1620               | ~0           | ~0             | ~0                |
| 1650               | ~0.8         | ~1.2           | ~1.8              |
| 1680               | ~0.3         | ~0.5           | ~0.7              |
| 1710               | ~0.1         | ~0.2           | ~0.3              |
| 1740               | ~0.2         | ~0.3           | ~0.4              |
| 1770               | ~0.1         | ~0.1           | ~0.2              |
| 1800               | ~0           | ~0             | ~0                |
</details>

![](images/bfd3218898fb1b49d3dbed5cb334ce2841b4b1419a23a4ba4cbefd3f4e034ddb.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Acyl C=C | EsterC=O |
| ------------------ | -------- | -------- |
| 1620               | ~0       | ~0       |
| 1650               | ~1.0     | ~0       |
| 1680               | ~0       | ~0       |
| 1710               | ~0       | ~0       |
| 1740               | ~0       | ~0.5     |
| 1770               | ~0       | ~0       |
| 1800               | ~0       | ~0       |
</details>

![](images/a2d4006d77a7aebbc6fc06f6b1b9fdbb7b7658bce1daa8f86ada1d4b8daa6566.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescently labeled cellular structures with no visible text or symbols
</details>

![](images/3086f402c44d39b0c12fd56bffeb0797a1d2b6b92581e9eca5b8bc63a808e1cd.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing green-labeled Ester group C=O structure against black background (no text or symbols)
</details>

![](images/d5a6acdfaa32adc4582837c632c62c36d6ee609b22d62c3c1fd44b3b17e276c0.jpg)

<details>
<summary>heatmap</summary>

| Acyl C=C/C=O | Value |
| ------------ | ----- |
| (various positions) | 0–3 (color-coded) |
</details>

![](images/3f340f80f0f9bdc618cd11c75cd628562fe9209994bfef166873dc61d5b4f20b.jpg)

<details>
<summary>bar chart</summary>

| Category              | Degree of unsaturation |
| --------------------- | ----------------------- |
| Fat in hypodermis      | 2.1                     |
| Oocytes               | 1.1                     |
| Intestinal lumen      | 0.5                     |
| Germ cells            | 1.0                     |
| Intestinal cells      | 1.0                     |
| Hypodermis of fat-6; fat-5 mutant | 1.3                   |
</details>

![](images/fc69a0a8ea399ef0749fc2ab1dfe060f128f203e0ba8b07abdfb9d8cd59ddbfe.jpg)

<details>
<summary>text_image</summary>

Lipids in intestinal
cell
h
</details>

![](images/1dc6ecbdc0dc02036bd4d141bdd633a8484ddad4bfadbc651ef9955562858ffc.jpg)

<details>
<summary>text_image</summary>

Lipids in hypodermis
of fat-6; fat-5 mutant
</details>

Figure 3. Mapping the degree of unsaturation of fat distributed in different segments of C. elegans. a) Color overlay image of neutral fat, proteins, and oxidized lipids in gonad arms of adult daf-2 worm. b) SRS spectra of three types of neutral fat at indicated position of worm in (a). c) MCR reference spectra of acyl C=C bond and ester group C=O bond. d,e) MCR-decomposed concentration maps corresponding to acyl C=C and ester C=O bonds. f) Degree of unsaturation map based on the ratio of (d) and (e). g) Statistical comparison of unsaturation of fat stored in the oocytes, lumen, germ cells, intestinal cells, and hypodermis tissue of a fat-6;fat-5 double mutant. h) Unsaturation degree map of fat in intestinal cells of Figure 1 c. i) Unsaturation degree map of fat in hypodermis tissue in a fat-6;fat-5 double mutant. Scale bar: 10 mm.

It is known that worms cannot synthesize sterols de $\mathbf { n o v o } ^ { [ 1 8 ] }$ and rely on exogenous sources of cholesterol. We next asked whether mutations in genes implicated in trafficking of cholesterol to lysosomes would alter the cholesterol storage in LROs. To do this, we performed hyperspectral SRS imaging of chup-1(gk245) mutants, which lack the cholesterol uptake protein CUP-1.[19] MCR-reconstructed image (Figure 2j) and spectra (Figure 2 k) showed the disappearance of the cholesterol peak at 1669 cm-1 . Though LROs in worms were considered as fat storage compartments for a long time, it is shown here by SRS spectral imaging that LROs are actually the sites for cholesterol storage regulated by the CUP-1 protein. Consistently, it is worth noting that all fat stores are comprised of triglyceride and none contains esterified cholesterol based on the MCR spectra.

Hyperspectral SRS imaging in the fingerprint vibration region further allowed in situ analysis of lipids unsaturation. Quantitative chemical maps based on the intensity ratio of acyl C=C and ester C=O Raman bands, generated by MCR analysis, were used to determine the degree of unsaturation of the fat in different compartments. Figure 3a shows a MCR reconstructed image of the gonad arm in a daf-2 mutant. The nucleus and cytoplasm, indicated in cyan, represent the area in the cell that is protein enriched. Four oocytes with a dense population of small-size lipid droplets are visualized and highlighted in yellow. Below the oocytes, a few hypoderma lipid droplets were spotted. In the intestinal lumen, we found a large amount of lipid droplets (yellow) together with oxidized lipids (magenta). We also observed the gonadal sheath overlying the undifferentiated germ cells above the intestinal lumen (Supporting Information, Movie S3). SRS spectra at indicated pixels shown in Figure 3 a, are given in Figure 3b to highlight the difference in the intensity of the C= C band normalized to the C=O band. These two bands were then used to quantify the degree of lipid unsaturation as follows: First, the hyperspectral SRS image stack was decomposed into two concentration maps (Figure 3 d,e), based on the internal reference spectra of acyl C=C and ester C=O bands acquired from glyceryl trioleate (Figure 3c).[13f] Then, the image of unsaturation (Figure 3 f) was generated by the intensity ratio between the acyl C=C and ester C=O bands at each pixel and interpreted as average number of C=C bonds per fatty acid chain in a triglyceride molecule. Figure 3 f illustrates the apparent difference in degree of unsaturation among hypodermal fat, oocyte fat, and gut deposits in the lumen of the intestine. Statistically, the hypodermal fat exhibits the highest degree of unsaturation (  2.0) and appears to be in the less-ordered liquid phase (Figure 3 g). In contrast, the fat stored in oocytes is analogous to glyceryl trioleate which bears on average one $\mathrm { C } { = } \mathrm { C }$ bond per fatty acid chain. The fat stored in the lumen resembles gellike saturated lipids with the average degree of unsaturation being around 0.54. In separate experiments, we also checked the degree of unsaturation of lipids in the intestinal cells (Figure 3h) and the germ cells, and found their degree of unsaturation was close to 1.0, similar to lipids stored in oocytes. To explore the enabling applications of the in vivo unsaturation measurement, we evaluated the hypodermal fat in $f a t { - } 6 { : } f a t { - } 5$ double mutants of C. elegans. Here, fat-6 is a stearoyl- $\mathrm { \cdot { C o A } \mathrm { - } \Delta ^ { 9 } \mathrm { . } }$ -desaturase that converts stearic to oleic acid, while fat-5 is a palmitoyl-CoA-D9 -desaturase that converts palmitic to palmitoleic acid. From the unsaturation image shown in Figure 3i, the $f a t { - } 6 { ; } f a t { - } 5$ double mutants bear a lower degree of unsaturation in hypodermal fat compared to either wild type or daf-2 mutants. Statistical measurements show their degree of unsaturation to be about 1.3 (Figure 3 g). Collectively these data show that SRS imaging of acyl C=C and ester C=O bands is capable of in vivo lipid unsaturation analysis with submicron spatial resolution.

In summary, hyperspectral SRS imaging in the fingerprint vibration region, followed by k-means clustering and MCR analysis, allowed the in situ identification and quantitation of three distinct lipid compartments in live worms. In particular, we found that LROs are sites for storage of cholesterol in C. elegans. With the capability of mapping the degree of unsaturation, lipid oxidation, and cholesterol storage in vivo with subcellular spatial resolution, further studies using our platform promise to give new insight into the impact of diet and the insulin/IGF-1 signaling pathway on obesity, diabetes, and longevity from C. elegans to mammals.

Received: June 8, 2014

Published online: September 3, 2014

.Keywords: C. elegans · cell metabolism · lipids · stimulated Raman scattering · vibrational spectroscopy

[1] a) T. Kaletta, M. O. Hengartner, Nat. Rev. Drug Discovery 2006, 5, 387; b) K. T. Jones, K. Ashrafi, Dis. Models Mech. 2009, 2, 224; c) J. L. Watts, Trends Endocrinol. Metab. 2009, 20, 58.  
[2] P. Greenspan, S. D. Fowler, J. Lipid Res. 1985, 26, 781.  
[3] H. Y. Mak, L. S. Nelson, M. Basson, C. D. Johnson, G. Ruvkun, Nat. Genet. 38  
[4] a) K. Ashrafi, F. Y. Chang, J. L. Watts, A. G. Fraser, R. S. Kamath. J. Ahringer. G. Ruykun. Nature 2003. 421. 268 b) E. J. O-Rourke, A. A. Soukas, C. E. Carr, G. Ruvkun, Cell Metab. 2009, 10, 430; c) S. B. O. Zhang, R. Trimble, F. L. Guo, BMC Cell Biol. 11  
[5] a) M. C. Wang, E. J. O-Rourke, G. Ruvkun, Science 2008, 322, 957; b) K. K. Brooks, B. Liang, J. L. Watts, PLoS One 2009, 4, e7545.  
[6] J. X. Cheng, X. S. Xie, Coherent Raman Scattering Microscopy, Taylor & Francis Group. New York. 2012.  
[7] C. L. Evans, X. S. Xie, Annu. Rev. Anal. Chem. 2008, 1, 883.  
[8] a) E. Ploetz, S. Laimgruber, S. Berner, W. Zinth, P. Gilch, Appl. Phys. B 2007, 87, 389; b) W. Min, C. W. Freudiger, S. Lu, X. S. Xie, Annu. Rev. Phys. Chem. 2011, 62, 507; c) D. Zhang, P. Wang, M. N. Slipchenko, J. X. Cheng, Acc. Chem. Res. 2014, 47, 2282.  
[9] a) T. Hellerer, C. Axang, C. Brackmann, P. Hillertz, M. Pilon, A. Enejder, Proc. Natl. Acad. Sci. USA 2007, 104, 14658; b) K. Yen, T. T. Le, A. Bansal, D. Narasimhan, J. X. Cheng, H. A. Tissenbaum, PLoS One 2010, 5, e12810; c) T. T. Le, H. M. Duren, M. N. Slipchenko, C. D. Hu, J. X. Cheng, J. Lipid Res. 2010, 51, 672.  
[10] M. C. Wang, W. Min, C. W. Freudiger, G. Ruvkun, X. S. Xie, Nat. Methods 2011, 8, 135.  
[11] M. Klapper, M. Ehmke, D. Palgunow, M. Bohme, C. Matthaus, G. Bergner, B. Dietzek, J. Popp, F. Doring, J. Lipid Res. 2011, 52, 1281.  
[12] J. S. Laufer, P. Bazzicalupo, W. B. Wood, Cell 1980, 19, 569.  
[13] a) Y. Ozeki, W. Umemura, Y. Otsuka, S. Satoh, H. Hashimoto, K. Sumimura, N. Nishizawa, K. Fukui, K. Itoh, Nat. Photonics 2012, 6, 845; b) J. L. Suhalim, C. Y. Chung, M. B. Lilledahl, R. S. Lim, M. Levi, B. J. Tromberg, E. O. Potma, Biophys. J. 2012, 102, 1988; c) D. Fu, G. Holtom, C. Freudiger, X. Zhang, X. S. Xie, J.  
Phys. Chem. B 2013, 117, 4634; d) D. Zhang, P. Wang, M. N. Slipchenko, D. Ben-Amotz, A. M. Weiner, J. X. Cheng, Anal. Chem. 2013, 85, 98; e) J. Mansfield, J. Moger, E. Green, C. Moger, C. P. Winlove, J. Biophotonics 2013, 6, 803; f) P. Wang, J. Li, P. Wang, C. R. Hu, D. Zhang, M. Sturek, J. X. Cheng, Angew. Chem. Int. Ed. 2013, 52, 13042 – 13046; Angew. Chem. 2013, 125, 13280 – 13284.  
[14] J. Jaumot, R. Gargallo, A. de Juan, R. Tauler, Chemom. Intell. Lab. Syst. 2005, 76, 101.  
[15] K. D. Kimura, H. A. Tissenbaum, Y. X. Liu, G. Ruvkun, Science 1997, 277, 942.  
[16] Y. Mukai, Y. Koyama, M. Ito, K. Tsukida, J. Raman Spectrosc. 1986, 17, 387.  
[17] G. E. Eldred, M. R. Lasky, Nature 1993, 361, 724.  
[18] W. F. Hieb, M. Rothstein, Science 1968, 160, 778.  
[19] V. J. Valdes, A. Athie, L. S. Salinas, R. E. Navarro, L. Vaca, PLoS One 2012, 7, e33962.