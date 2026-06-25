# Functionalized NIR-II Semiconducting Polymer Nanoparticles for Single-cell to Whole-Organ Imaging of PSMA-Positive Prostate Cancer

Jiayingzi Wu, Hyeon Jeong Lee, Liyan You, Xuyi Luo, Tsukasa Hasegawa, Kai-Chih Huang, Peng Lin, Timothy Ratliff, Minoru Ashizawa, Jianguo Mei,\* and Ji-Xin Cheng\*

Development of molecular probes holds great promise for early diagnosis of aggressive prostate cancer. Here, 2-[3-(1,3-dicarboxypropyl) ureido] pentanedioic acid (DUPA)-conjugated ligand and bis-isoindigo-based polymer (BTII) are synthesized to formulate semiconducting polymer nanoparticles (BTII-DUPA SPN) as a prostate-specific membrane antigen (PSMA)-targeted probe for prostate cancer imaging in the NIR-II window. Insights into the interaction of the imaging probes with the biological targets from single cell to whole organ are obtained by transient absorption (TA) microscopy and photoacoustic (PA) tomography. At single-cell level, TA microscopy reveals the targeting efficiency, kinetics, and specificity of BTII-DUPA SPN to PSMA-positive prostate cancer. At organ level, PA tomographic imaging of BTII-DUPA SPN in the NIR-II window demonstrates superior imaging depth and contrast. By intravenous administration, BTII-DUPA SPN demonstrates selective accumulation and retention in the PSMA-positive tumor, allowing noninvasive PA detection of PSMA overexpressing prostate tumors in vivo. The distribution of nanoparticles inside the tumor tissue is further analyzed through TA microscopy. These results collectively demonstrate BTII-DUPA SPN as a promising probe for prostate cancer diagnosis by PA tomography.

## 1. Introduction

Prostate cancer is the most common male malignancy and remains the second leading cause of cancer deaths in men in the United States.[1] Serum prostatespecific antigen (PSA) test is a standard approach for prostate cancer screening.[2] However, common conditions, such as benign prostatic hyperplasia and prostatitis, are also accompanied by increased PSA levels, resulting in false-positive results and a large number of unnecessary prostate biopsies.[3,4] Besides, the current standard transrectal ultrasound– guided prostate biopsy is like a “lottery” to patients, because biopsy needles are placed blindly into the prostate owing to the inability to visualize prostate cancer.[5,6] As a result. indolent tumors with little clinical relevance are substantially overdiagnosed and overtreated, while some aggressive prostate cancer may be missed.[7,8] The recent introduction of magnetic resonance imaging (MRI)-guided prostate biopsy allows improved accuracy but adds significant cost and lacks real-time imaging capabilities.[6,9,10] Thus, there is an urgent need to develop cost-effective diagnostic

tools with high sensitivity and specificity for detection and staging of prostate cancer.

Photoacoustic (PA) tomography as a hybrid imaging modality with light excitation and acoustic detection is attractive

J. Wu, Dr. H. J. Lee, P. Lin, Prof. J.-X. Cheng Department of Electrical and Computer Engineering Boston University Boston, MA 02215, USA E-mail: jxcheng@bu.edu J. Wu, Dr. L. You, X. Luo, Prof. J. Mei Department of Chemistry Purdue University West Lafayette, IN 47907, USA E-mail: jgmei@purdue.edu T. Hasegawa, Prof. M. Ashizawa Department of Materials Science and Engineering Tokyo Institute of Technology Meguro-ku, Tokyo 152-8552, Japan

![](images/f95e576f735db58d82f4e7dcd8f95ba6d2b7e37865073cd4b38bdf5bd40326a1.jpg)

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/smll.202001215.

K.-C. Huang, Prof. J.-X. Cheng Department of Biomedical Engineering Boston University Boston, MA 02215, USA Prof. T. Ratliff Department of Comparative Pathobiology Purdue University West Lafayette, IN 47907, USA Prof. T. Ratliff Center for Cancer Research Purdue University West Lafayette, IN 47907, USA Prof. J.-X. Cheng Photonics Center Boston University Boston, MA 02215, USA

DOI: 10.1002/smll.202001215

for clinical applications. Compared to conventional imaging modalities, such as, MRI, computed tomography, and positron emission tomography, PA tomography provides advantages in molecular optical sensitivity, spatial and temporal resolutions, as well as non-ionizing radiation risk.[11–15] When compared to traditional optical imaging modalities, PA tomography has superior imaging depth as both ballistic photons and diffused photons will induce photoacoustic signals. Meanwhile, the acoustic scattering is three orders of magnitude less than the optical scattering.[16]

The most common application of PA tomography in prostate cancer diagnosis is for imaging angiogenesis based on the high PA signal of blood.[17–19] Unfortunately, angiogenesis in the prostate is not specific to prostate cancer.[20] One way to overcome this limitation is to develop active targeting probes that can selectively bind to the receptors or antigens overexpressed on the surface of cancerous cells, and thus highlighting the malignant tumor without labeling the normal tissues.[21–23] Several PA probes have been reported for prostate cancer detection via active targeting, including gold nanorods,[24] NIR dyes,[25,26] and polymer nanoparticles.[27,28] Nevertheless, the existing PA probes with absorption in the first near-infrared window (NIR-I: 800–1000 nm) suffer from limited penetration depth and imaging contrast. PA imaging in the second nearinfrared window (NIR-II: 1000–1700 nm) is attracting more and more attention owing to the reduced absorption of endogenous chromophores, lower light scattering, and higher maximum permissible exposure of light in this region, which leads to the enhanced photon penetration for in vivo deep-tissue imaging.[29–39] Significant breakthroughs have been made to develop organic semiconducting polymer nanoparticles (SPNs) for PA imaging in the NIR-II window, due to their good biocompatibility, excellent photostability, high mass extinction, and controllable dimensions.[39–43] The majority of current NIR-II SPNs rely on the accumulation in tumor through enhanced permeability and retention (EPR) effect. Although this passive targeting approach has been widely used in clinics and in research, it preserves several drawbacks including the lack of cellular specificity for assessing the aggressiveness of tumors and the difficulty in controlling due to the random nature of the approach.[44] Therefore, the development of active targeted SPN in the NIR-II window is desirable for sensitive and accurate prostate cancer diagnosis.

Herein, we report an active targeted SPN that contains NIR-II absorbing semiconducting polymer (bis-isoindigo-based polymer (BTII)) with surface functionalized by glutamate urea ligands (2-[3-(1,3-dicarboxypropyl)ureido]pentanedioic acid (DUPA)), termed as BTII-DUPA SPN, for targeted imaging of prostate cancer. DUPA is known to have high affinity to prostate-specific membrane antigen (PSMA) that is overexpressed in prostate cancer.[45–48] More importantly, the expression level of PSMA increases with the aggressiveness and the recurrence of prostate cancer.[45,47–49] The potentials of PSMA-based imaging for cancer diagnosis[26,50–54] and fluorescence-guided surgery[55,56] have been shown previously. In this study, based on the abovementioned advantages of NIR-II PA tomography over conventional imaging modalities, the BTII-DUPA SPN is expected to bring new opportunities for prostate cancer diagnosis and treatment. We investigated the effective targeting of BTII-DUPA SPN to PSMA-positive prostate cancer at the single-cell level in live cells by using a transient absorption (TA) microscope that provides sub-micrometer resolution and single-particle sensitivity. Then, the deep imaging depth and high imaging contrast in PA tomography were validated to reveal the potential of BTII-DUPA SPN for in vivo deep-tissue imaging. Next, the targeting specificity of BTII-DUPA SPN was demonstrated in living mice bearing both PSMA-positive and PSMA-negative tumors. Lastly, the nanoparticle distributions in tumor tissues after intravenous injection of BTII-DUPA SPN were studied in detail by TA microscopy.

## 2. Results

## 2.1. Synthesis and Characterization of BTII-DUPA SPN

The donor–acceptor–acceptor (D-A-A) type conjugated polymer, BTII, was synthesized according to our previous report (Figure 1a).[57] The highly planarized BTII has exhibited an extended effective conjugation length with a lowered LUMO level,[57] which attributes to its narrow bandgap with effective absorption in the NIR-II window, and thus is served as the NIR-II absorbing PA agent in this study. Meanwhile, the targeting ligand DUPA was conjugated to the amphiphilic surfactant F127 and formed DUPA-F127-DUPA (Figure 1a).[58]

To prepare a series of water-soluble BTII-DUPA SPNs (Figure 1b) with different functionalities of DUPA on the surface, DUPA-F127-DUPA was blended with F127 in different weight percentages (e.g., 50%, 70%, and 100% of DUPA-F127- DUPA) and then co-precipitated with BTII. Considering the purity of DUPA-F127-DUPA was calculated to be ≈70%, the actual feeding ratio, which means how many surfactants were initially added to the solution for nanoparticle synthesis, of DUPA-F127-DUPA was determined as 35%, 49%, and 70%, respectively. As a control group, the nontargeted BTII SPN was synthesized with BTII and F-127 only (0% DUPA-F127- DUPA). The DLS results show that the number-averaged hydrodynamic diameter of SPNs gradually increases from 41.4 to 91.3 nm as the feeding ratio of DUPA-F127-DUPA increases from 0% to 70% (Figure  1c). Since more DUPA could make the particle bulkier, this result indicates the fine-tuned func tionality of DUPA on the SPN surface. Transmission electron microscopy (TEM) images (inserted in Figure 1c) further revealed the spherical morphology of SPNs and confirmed the size difference between the nanoparticles without DUPA-F127- DUPA (average diameter ≈37.6 nm) and with 70% DUPA-F127- DUPA (average diameter ≈81.0 nm). The slightly smaller size estimated by TEM relative to DLS was probably due to the shrinkage of nanoparticles in the dry state during the preparation of TEM samples.[59]

The absorption spectra of BTII SPN and BTII-DUPA SPN were then measured, showing identical absorption profiles in the NIR-II window (Figure 1d) with the same extinction coefficient of 22.5 cm−1  mg−1  mL at 1100 nm (normalized by the mass concentration of BTII), which means that the conjugation of DUPA did not alter the optical properties of SPNs. The NIR-II absorption contributed to the efficient generation of PA signa (Figure 1e) measured with a PA spectroscopy setup (Scheme S1,

(a  
![](images/a6e68aaf22da47022fbb19ebf0f78056d51d3292247d0403371e4b45eca9f542.jpg)

<details>
<summary>chemical</summary>

Chemical structure of BTII polymer with repeating units and side chains labeled C10H21, C8H17, C10H21, C8H17, C10H21
</details>

![](images/12115abaf376a81660eee5b6b9ea1d6c0663b07a75841261a57ac5be7fc7b5cb.jpg)

<details>
<summary>chemical</summary>

Chemical structure of DUPA-F127-DUPA with labeled functional groups and a wavy chain representation
</details>

(b)

![](images/f9e41b5ea7185d26f7a4080cbd975a09fef62dfe08125eca0e45f589e79150d4.jpg)

<details>
<summary>chemical</summary>

Diagram of BTII-DUPA SPN molecular structure showing electron flow around a central orange core
</details>

(c)  
![](images/962e3571b0e1a71761cb3bfeddb68e35c180bf2930e4a80c0af5d0346391fada.jpg)

<details>
<summary>line chart</summary>

| Diameter (nm) | Normalized value (a.u.) - 0% | Normalized value (a.u.) - 35% | Normalized value (a.u.) - 49% | Normalized value (a.u.) - 70% |
| ------------- | ---------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| ~10           | ~0.0                         | ~0.0                          | ~0.0                          | ~0.0                          |
| ~100          | ~1.0                         | ~1.0                          | ~1.0                          | ~1.0                          |
| ~1000         | ~0.0                         | ~0.0                          | ~0.0                          | ~0.0                          |
| ~10000        | ~0.0                         | ~0.0                          | ~0.0                          | ~0.0                          |
</details>

(d)  
![](images/b14f392dfe2c679bb08de4758d1be869c9250de1447af5905e80a6490a03ce38.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | BTII-DUPA SPN | BTII SPN | BTII in THF |
| --------------- | ------------- | -------- | ----------- |
| 500             | 0.1           | 0.0      | 0.1         |
| 700             | 0.2           | 0.1      | 0.2         |
| 900             | 0.8           | 0.7      | 0.8         |
| 1100            | 1.0           | 1.0      | 1.0         |
| 1300            | 0.2           | 0.2      | 0.2         |
</details>

(e)  
![](images/9b87cd33488ae8a644a4d04fe00e84de7f0aa8d5b38fe0a46b30810fc4134541.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | BTII-DUPA SPN | BTII SPN |
| --------------- | ------------- | -------- |
| 1100            | 3.5           | 3.5      |
| 1150            | 2.8           | 2.7      |
| 1200            | 2.0           | 1.9      |
| 1250            | 1.5           | 1.4      |
| 1300            | 1.0           | 1.2      |
</details>

Figure 1. Synthesis and chracterization of BTII-DUPA SPN. a) Chemical structures of BTII and DUPA-F127-DUPA. b) Schematic illustration of BTII DUPA SPN. c) DLS profiles of BTII SPN (0% DUPA-F127-DUPA) and BTII-DUPA SPN with 35%, 49%, and 70% DUPA-F127-DUPA feeding ratio. Inserts: representative TEM images. Scale bars: 100 nm. d) Absorption spectra of BTII in tetrahydrofuran (THF), as well as BTII SPN and BTII-DUPA SPN with 70% DUPA-F127-DUPA feeding ratio in water. e) PA spectra of BTII SPN and BTII-DUPA SPN with 70% DUPA-F127-DUPA feeding ratio.

Supporting Information), demonstrating that BTII-DUPA SPNs are effective NIR-II PA emitters.

## 2.2. Imaging SPNs by TA Microscopy

We explored the feasibility of using a TA microscope (Scheme S2, Supporting Information) for imaging the non-fluorescent BTII-DUPA SPN, which allows the further in-depth study of BTII-DUPA SPN at cellular level. Experimentally, BTII-DUPA SPN was pumped by fs-pulses at 1045 nm and probed by fs-pulses at 853 nm, and the corresponding frequency difference (2150 cm−1 ) lies in the “cell silent region” to ensure sensitive and specific detection in living systems.[60–62] To identify which mechanism contributes to the signal generation in the case of BTII-DUPA SPN detection under our TA microscopy system settings, we retrieved the intensity and phase information of both the in-phase channel and quadrature channel from a lockin amplifier, and the signals from BTII-DUPA SPN were found to correspond to an in-phase modulation of the probe beam (Figure S1, Supporting Information).[63] Although both stimulated emission and ground-state depletion processes can lead to an in-phase signal, the possibility of stimulated emission is excluded since the probe wavelength is shorter than the pump wavelength.[64] Therefore, the generation of TA signals from BTII-DUPA SPN can be depicted by ground-state depletion mechanism where the population in ground-state is decreased by the photoexcitation of the pump beam and thus the sequent probe beam is absorbed less, yielding the TA signal (Figure 2a). Next, the TA kinetics trace is shown in Figure 2b, of which the decay phase reflects the relaxion of excitons to the ground-state via nonradiative decay.[65] By fitting of the decay phase with a biexponential model, the nonradiative time constant is determined to be 2.79 ± 0.36 ps, which is one to two times shorter than the exciton lifetimes of most thiophene-based polymers.[66] The fast nonradiative decay implies the minimized fluorescence. On the other hand, the shorter nonradiative time constant contributes to the higher photothermal conversion efficiency and benefits the efficient generation of PA signal.[65]

The TA intensity of BTII-DUPA SPN solution displays a linear relationship with the concentration, which can be used for a quantitative analysis of intracellular BTII-DUPA SPN (Figure 2c). To further characterize the sensitivity and resolution of the TA microscopy system, individual BTII-DUPA SPNs were dispersed on a glass substrate by high-speed spin coating. Uniformly monodispersed nanoparticles were clearly visualized under a TA microscope (Figure 2d), demonstrating the single-particle sensitivity of the system. The intensity profile of an individual particle shows a full-width-half-maximum (FWHM) of 600–700 nm via Gaussian fitting (Figure  2e,f), which indicates that TA microscopy can reach sub-micrometer resolution. Taken together, we have demonstrated that TA microscopy, as a unique nonfluorescence-based imaging modality, provides high sensitivity and sub-micrometer resolution for imaging BTII-DUPA SPN.

## 2.3. Specific Targeting In Vitro

The specific targeting of BTII-DUPA SPN to PSMA-positive prostate cancer was examined in vitro. In order to investigate the biocompatibility of BTII-DUPA SPN, we first carried out cytotoxicity tests. No overt toxicity was found at concentrations up to 100 µg $\mathrm { m } \mathrm { L } ^ { - 1 }$ of BTII-DUPA SPNs with different DUPA functionalities (Figure 3a). We then determined the optimal DUPA functionality that confers maximal targeted cellular uptake. BTII-DUPA SPNs made with different feeding ratios of DUPA-F127-DUPA were incubated with LNCaP cells (PSMApositive prostate cancer cell line) for 48 h and then imaged with TA microscopy (Figure  3b). While nontargeted BTII SPN had negligible uptake by LNCaP cells, obvious cellular uptake was observed by BTII-DUPA SPN made with 35% DUPA-F127- DUPA. This indicates that DUPA plays an essential role in the cellular binding and uptake. Furthermore, there is a significant increase of $4 . 1 \pm \ : 2 . 5 { \cdot } \mathrm { f o l d }$ in intracellular TA intensity when the DUPA-F127-DUPA feeding ratio was increased from 35% to 70% (Figure 3b; Figure S2, Supporting Information). Based on these results. BTII-DUPA SPN with 70% DUPA-F127-DUPA feeding ratio was used for the following study to achieve the maximal cellular targeting unless otherwise mentioned.

(a)  
![](images/e649dbadead3c8d9303a7fd92886be4c26b01dd311cf46256d385d65727af902.jpg)

<details>
<summary>text_image</summary>

Pump
Probe
</details>

(b)  
![](images/69c8519cfdd9f1b581bf370cec91b7664d38c4806d179e0255cc949806d391f3.jpg)

<details>
<summary>line chart</summary>

| Pump-probe delay (ps) | TA intensity (a.u.) |
| --------------------- | ------------------- |
| -1.0                  | 0.0                 |
| -0.5                  | 0.0                 |
| 0.0                   | 11.0                |
| 0.5                   | 3.0                 |
| 1.0                   | 1.5                 |
| 1.5                   | 1.0                 |
| 2.0                   | 0.5                 |
</details>

(c)

![](images/677c3040330a98d7caa87cf670e70d0943a8654ad9c5f21bb03570511fb88d9f.jpg)

<details>
<summary>line chart</summary>

| Concentration (μg mL⁻¹) | TA intensity (a.u.) |
| ------------------------ | ------------------- |
| 0                        | 0                   |
| 10                       | 1                   |
| 20                       | 2                   |
| 40                       | 4                   |
| 60                       | 6                   |
| 80                       | 8                   |
| 100                      | 10                  |
</details>

(d)  
![](images/a435c1d7f01c6afbbed7edf181f6b6dac6f064ce55e05d3db02b174d8cc213c8.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing blue fluorescent spots on a black background with a 1 μm scale bar (no text or symbols beyond scale)
</details>

(e)  
![](images/c4ee28af6c14cd9481a1faa5d1a547b097d3a25ee1677f5c7a9547b9fae2a5c5.jpg)

<details>
<summary>scatterplot</summary>

| Displacement (nm) | TA intensity (a.u.) |
| ----------------- | ------------------- |
| 0                 | 0.2                 |
| 500               | 0.4                 |
| 1000              | 0.7                 |
| 1500              | 0.3                 |
| 2000              | 0.2                 |
</details>

(f)  
![](images/a21658109f7030b40e7bd7c7ec06e2fee7eb62d08f36f47448cf4579d53f3881.jpg)

<details>
<summary>scatterplot</summary>

| Displacement (nm) | TA intensity (a.u.) |
| ----------------- | ------------------- |
| 0                 | 0.0                 |
| 700               | 0.2                 |
| 1400              | 0.8                 |
| 2100              | 0.2                 |
| 2800              | 0.1                 |
</details>

Figure 2. TA microscopy allows high-sensitivity and high-resolution imaging of BTII-DUPA SPN. a) Schematic illustration of the ground-state deple tion mechanism. b) Pump-probe decay curve of BTII-DUPA SPN and the corresponding biexponential decay fitting curve $\begin{array} { r } { ( R ^ { 2 } > 0 . \dot { 9 } 9 ) . } \end{array}$ c) TA intensity as a function of BTII-DUPA SPN concentration and the corresponding linear fitting curve $\left( R ^ { 2 } > 0 . 9 9 \right)$ ). Insert: TA image of 2.5 µg $\mathsf { m L } ^ { - 1 }$ BTII-DUPA SPN solution. d) TA image of individual BTII-DUPA SPNs. e,f) Intensity profiles of individual nanoparticles extracted from (d) and the coreesponding Gus saian fitting curves. Inserts: TA images of the corresponding nanoparticles. Error bars represent standard deviations. For imaging of BTII-DUPA SPN solutions, laser power was 10 mW for pump beam at 1045 nm and 10 mW for probe beam at 853 nm, before microscope. For imaging of BTII-DUPA SPN thin films, laser power was 2 mW for pump beam at 1045 nm and 2 mW for probe beam at 853 nm, before microscope.

To study the cellular uptake process of BTII-DUPA SPN into LNCaP cells, time-dependent TA imaging was performed. As shown in Figure  3c, BTII-DUPA SPN was first bound to the LNCaP cell membrane, then gradually endocytosed and accumulated inside cells. Such observation can be explained by the endocytic function of cell surface receptors that PSMA undergoes internalization constitutively, resulting in the enhancement in internalization of ligand-conjugates.[47,67] On the contrary, no noticeable cellular uptake of the nontargeted BTII SPN was observed within 48 h (Figure 3d).

The targeting specificity of BTII-DUPA SPN to PSMA-positive cells were further validated by comparison among cell lines with different PSMA expression levels. As shown in Figure 3e, while significant cellular uptake was found in LNCaP cells, minimal amount of BTII-DUPA SPN was presented in PC-3 cells (PSMA-negative prostate cancer cell line) and in HFB cells (PSMA-negative normal human fibroblast cell line). Additionally, the uptake by LNCaP cells was blocked in the presence of excess PMPA (PSMA inhibitor; Figure  3e). The statistical analysis of intracellular TA signal intensities confirms that cellular uptake in the control groups are significantly lower compared with the PSMA-positive LNCaP cell line (Figure  3f). In summary, we have shown that BTII-DUPA SPN is a specific targeting agent for PSMA-positive prostate cancer and used TA microscopy to obtain insights into the cellular targeting process.

## 2.4. PA Imaging Contrast and Depth

In addition to the targeting functionality, the imaging contrast and depth in deep tissue are evaluated. To investigate the in vivo PA imaging contrast in the NIR-II window, multispectral

(a)  
![](images/eadee39f42f0edc9153710d3f11cf116bf68eb28c2e8d64c39aa4a15170a2eb2.jpg)

<details>
<summary>bar chart</summary>

| Concentration (μg mL⁻¹) | 0%   | 35%  | 70%  |
| ------------------------ | ---- | ---- | ---- |
| 20                       | 100  | 90   | 100  |
| 40                       | 98   | 88   | 102  |
| 60                       | 100  | 95   | 98   |
| 80                       | 100  | 98   | 98   |
| 100                      | 100  | 100  | 95   |
</details>

(b)  
![](images/4cc7cb3ad2c9599132d6f8af800f831c939515a5d5e5661d02330751439d7bde.jpg)

<details>
<summary>image displays two panels: the top panel</summary>

| Condition | TA 0 % | TA 35 % | TA 70 % | Overlay |
|-----------|--------|---------|---------|---------|
| DUPA-F127-DUPA Feeding Ratio | 0      | 35      | 70      | 50 µm   |
</details>

(c)  
![](images/8154be6a70a3611e3ea5891fc95a396e32616ad588091bc88de0da3d25674a9d.jpg)

<details>
<summary>text_image</summary>

BTII-DUPA SPN
TA
3 hour
24 hour
48 hour
Overlay
50 µm
</details>

(d)  
![](images/7df2af1d9e20d4e7dab8e9c94edca4808d7da590cf876468bf194b02ed676082.jpg)

<details>
<summary>text_image</summary>

a)
BTII SPN
TA
3 hour
24 hour
48 hour
Overlay
50 µm
</details>

(  
![](images/fcdca8816dfea9e40c4e2374490c6a4c99166afcc06291afcc58e8983bdf2e9b.jpg)

<details>
<summary>text_image</summary>

e) LNCaP PC-3 HFB LNCaP (+PMPA)
TA
Overlay
50 µm
</details>

(f)  
![](images/025faadccf0d459e062f37cf659bad7a45000ef45d3ce72c3039c7daff637207.jpg)

<details>
<summary>bar chart</summary>

| Group        | TA intensity (a.u.) |
| ------------ | ------------------- |
| LNCaP        | 7.0                 |
| PC-3         | 1.0                 |
| HFB          | 0.5                 |
| LNCaP (+PMPA) | 3.0                 |
</details>

Figure 3. TA microscopy reveals specific targeting of BTII-DUPA SPN to prostate cancer cells in vitro. a) Cell viability of LNCaP cells after treated with BTII SPN (with 0% DUPA-F127-DUPA) or BTII-DUPA SPNs (with 35% or 70% DUPA-F127-DUPA feeding ratio) in different concetrarions for 24 h. b) TA images of LNCaP cells after treated with 13.3 µg $\mathsf { m L } ^ { - 1 }$ BTII SPN (with 0% DUPA-F127-DUPA) or BTII-DUPA SPNs (with 35% or 70% DUPA-F127-DUPA feeding ratio) for 48 h. c,d) Time dependent TA imaging of LNCaP cells treated with 13.3 µg $\mathsf { m L } ^ { - 1 }$ of (c) BTII-DUPA SPN (with 70% DUPA-F127-DUPA feeding ratio) or (d) BTII SPN (with 0% DUPA-F127-DUPA). TA images were taken after $3 , 2 4 ,$ and 48 h treatment. e) TA images of LNCaP cells, PC-3 cells, HFB cells, and LNCaP cells with excess PMPA. Cells were treated with 13.3 µg mL−1 BTII-DUPA SPN (with 70% DUPA-F127-DUPA feeding ratio) for 48 h. LNCaP, PSMA-postive prostate cancer cell line; PC-3, PSMA-negative prostate cancer cell line; HFB, PSMA-negative normal human fibroblast cell line; PMPA, PSMA inhibitor, 100 $\mu \ g \mathsf { m } \mathsf { L } ^ { - 1 } . \mathsf { f } )$ Quantatitive ananlysis of TA intensities extrated from (e). All the TA images (cyan hot) were overlayed with transmission images (gray) to show the location of nanoparticles. Error bars represent standard deviations. $\tilde { \alpha } \tilde { \alpha } \tilde { \kappa } \tilde { \kappa } _ { P < }$ 0.0001 in t-test with equal variance. Laser power was 20 mW for pump beam at 1045 nm and 10 mW for probe beam at 853 nm, before microscope.

analysis was performed by using least absolute shrinkage and selection operator (LASSO) analysis to specify the source of PA signals in images. Three major components were considered in multispectral analysis, including blood, lipid, and BTII-DUPA SPN. The PA spectra of those pure components were recorded by PA spectroscopy and used as reference spectra for LASSO decompositions (Figure 4a). Then, Matrigel-containing solutions of BTII-DUPA SPN (50 µL, 20 µg $\mathrm { m L ^ { - 1 } } )$ were administrated into the dorsal area of mice and PA images of the region of interest (ROI) were recorded over the NIR-II wavelengths (1100–1300 nm) with 20 nm interval (Scheme S3a, Supporting Information). The results after multispectral analysis are shown in Figure 4b–e. Signals of lipid were mostly distributed in the skin and only small amount of blood signals were found in the tissue background, while strong BTII-DUPA SPN signals were found in the injection site underneath the skin. It is worth noting that the image acquired at a single wavelength of 1100 nm (Figure 4f) is identical to the concentration image of BTII-DUPA SPN from multispectral analysis (Figure 4d), which suggests that the PA signal at 1100 nm are dominated by BTII-DUPA SPN with minimal tissue background signals. In comparison, PA images of Matrigel-containing phosphate-buffered saline (PBS) solution after subcutaneous injection display negligible PA signal close to the background at 1100 nm (Figure S3, Supporting Information). Furthermore, there exhibits a linear relationship between the PA signal at 1100 nm and the concentration of BTII-DUPA SPN in vivo (Figure S3, Supporting Information). In view of the outstanding imaging contrast of BTII-DUPA SPN at around 1100 nm, the following experiments were carried out with a 1064 nm Nd:YAG laser unless otherwise mentioned, which is one of the most reliable and economical nanosecond lasers and will accelerates the clinical translation process.

![](images/3718de4a0c9695fe7d28bdaf35d689cc0ac0f3bcc9725ad6ef2db1b59d806376.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Blood | Lipid | BTII-DUPA SPN |
| --------------- | ----- | ----- | ------------- |
| 1100            | 0.3   | 0.1   | 0.9           |
| 1150            | 0.1   | 0.1   | 0.7           |
| 1200            | 0.1   | 0.6   | 0.4           |
| 1250            | 0.1   | 0.1   | 0.4           |
| 1300            | 0.1   | 0.1   | 0.2           |
</details>

![](images/a428ca825959f04e2f7f4e5b099de000c2befde8678c74d18d154e89800dc9d7.jpg)

<details>
<summary>line chart</summary>

| Depth (cm) | 80 µg mL⁻¹ | 200 µg mL⁻¹ |
| ---------- | ---------- | ----------- |
| 1.0        | 3000       | 50000       |
| 2.0        | 1000       | 3000        |
| 3.0        | 300        | 1000        |
| 4.0        | 100        | 300         |
</details>

![](images/fa1b003f39ebd1cdd69b603c2d9d2b8fa63c269e6f1f75fbb5ac7fe53993c03d.jpg)

![](images/3d268300805a34717b2e22536be259a4f89247da5539a28e149381f69d9d8e8c.jpg)

![](images/b911c7a25697c5d5322e3df0e45933e0bdf2ed2e6ff7a533508df1a374718c83.jpg)

![](images/eab2b6570629e50ad640ab8bcf63962d783a3c5d47748a98047e756f43b6b174.jpg)

![](images/99ae9c2e59e89cb339da5ae010f959aa12cf1d39d6ffc39fa667e0135138dc41.jpg)

![](images/5031e52b11eed5ad4be086a121dc08bbc8ea0cc6d281eb0979f1dbcc27671019.jpg)

<details>
<summary>text_image</summary>

(g) 1064 nm laser
4.2 cm
3.8 cm
0.84
0.75
</details>

Figure 4. PA tomographic imaging of BTII-DUPA SPN in the NIR-II window offers suprior imaging contrast and depth. a) PA spectra of lipid, blood, and BTII-DUPA SPN solution, which were used as reference spectra for LASSO analysis. b–d) LASSO retrieved concetration images of b) lipid (green), c) blood (red), and d) BTII-DUPA SPN (blue) in mouse skin with subcutaneous injection of Marigel containing BTII-DUPA SPN (50 µL, 20 µg mL−1 ). e) The overlayed image of (b–d). f) PA tomographic imaging (magenta) of the same ROI in mouse skin as beforementioned at 1100 nm. Laser energy density was tuned to 15 mJ cm−2 at each wavelength. g) PA/ultrasound co-registered image of the 80 µg mL−1 BTII-DUPA SPN in a transparent polyurethane tube placed at 4.2 cm depth in chicken breast tissue. PA image is in magenta and ultransound image is in gray. Laser energy density was tuned to 45 mJ cm−2 at 1064 nm. h) SNR of 80 or 200 µg mL−1 BTII-DUPA SPN solution as a function of depth from the illuminated tissue surface and the corresponding linear fitting curve $( R ^ { 2 } > 0 . 9 9 )$ ). Laser energy density was tuned to 45 mJ $\mathsf { c m } ^ { - 2 }$ at 1064 nm.

Next, the imaging depth at 1064 nm was assessed by using chicken-breast tissue as the scattering medium. BTII-DUPA SPN solution was sealed in a transparent polyurethane tube and the PA images at different depths were collected by changing the number of layers of chicken-breast tissues below and above the tube simultaneously (Scheme S3b, Supporting Information). The corresponding laser energy density was ≈45 mJ cm−2 and 100 images were acquired and averaged at the same position. The polyurethane tube containing 80 µg $\mathrm { m } \mathrm { L } ^ { - 1 }$ BTII-DUPA SPN solution can be visualized at an imaging depth of 4.2 cm with a signal-to-noise ratio (SNR) of 29.2 (Figure  4g). Notably, the achieved imaging depth with a low concentration of BTII DUPA SPN is readily larger than the normal size of a human prostate (3.5 cm), indicating a promising potential application in whole-prostate imaging. Furthermore, by increasing the BTII-DUPA SPN concentration to 200 µg mL−1 , the SNR was increased to 72.3 at 4.2 cm depth. The SNR of PA signal was plotted as a function of depth and was fitted into an exponential function based on Lambert–Beer's law (Figure  4h).[68] The imaging depth-limit where the SNR of BTII-DUPA SPN was equivalent to the SNR of tissue background $( \mathrm { S N R } = 2 0 )$ is calculated to be 4.5 cm and 5.7 cm with 80 and 200 µg mL−1 BTII-DUPA SPN, respectively.

## 2.5. In Vivo Imaging of PSMA-Positive Prostate Tumor

The tumor targeting capability of BTII-DUPA SPN to PSMApositive prostate cancer in vivo was investigated on living mice bearing LNCaP (PSMA-positive) and PC-3 (PSMA-negative) xenografts on opposite flanks (Figure 5a). To statistically evaluate the targeting of BTII-DUPA SPN to PSMA-positive tumors, the measurements were repeated with five nude mice and consistent results were obtained (Figure S4, Supporting Information). Before systemic administration of nanoparticles, tumors show negligible PA signals due to the minimal absorption of blood and lipid in the NIR-II region (Figure 5b), which is consistent with our previous results (Figure 4).[40] After intravenous injection of BTII-DUPA SPN into the mice, the

(a)  
![](images/3f11c849379eb31642f2df1508319c9a618fcfe58248b8aa01e8a6f931b10375.jpg)

(b)  
![](images/acd86349b15f6794e8a17c436000c099572d355d2315f3ae98ff76d92d840f90.jpg)

<details>
<summary>text_image</summary>

Pre
3 hour
6 hour
24 hour
72 hour
LNCaP
(PSMA+)
PC-3
(PSMA-)
Log (PA intensity)
14.5
8.2
2 mm
</details>

(c)  
![](images/202fc07e0d59314c35ec307ed8bb8c79e557609e072da9db77cc33d5c9ece2c2.jpg)

<details>
<summary>line chart</summary>

| Time (hour) | LNCaP | PC-3 |
|-------------|-------|------|
| 0           | 0.0   | 0.0  |
| 12          | 4.5   | 1.5  |
| 24          | 3.5   | 1.0  |
| 36          | 2.5   | 0.5  |
| 48          | 2.0   | 0.3  |
| 72          | 1.5   | 0.1  |
</details>

(d)  
![](images/dc9fc35efc4dadc3fd6558f4c08845cf32133eb039e5b09b6ab4c850dd21284d.jpg)

<details>
<summary>bar chart</summary>

| Group   | Distribution half-life (h) | Elimination half-time (h) | AUC (a.u.) |
|---------|-----------------------------|----------------------------|----------|
| PC-3    | 1.9                         | 18                         | 50       |
| LNCaP   | 1.6                         | 43                         | 180      |
</details>

(e)  
![](images/43c80fd6f93e219c69ad73ef3eb3c7bacd4bdb3ad0ce9420b0f5538a819a802c.jpg)

<details>
<summary>bar chart</summary>

| Tissue | BTII-DUPA SPN | PBS |
|--------|---------------|-----|
| PC-3   | 3             | 1   |
| LNCaP  | 6             | 1   |
| Heart  | 3             | 1   |
| Kidney | 2             | 1   |
| Liver  | 9             | 1   |
| Spleen | 11            | 1   |
| Prostate | 1             | 1   |
| Lung   | 4             | 6   |
</details>

(f)  
![](images/da3da2a6f1b38d27606a08bd706e3920dddbef627e91892884b82e21407fb400.jpg)

<details>
<summary>text_image</summary>

Liver
Kidney
Spleen
Lung
Heart
PBS
BTII-DUPA
200 µm
</details>

Figure 5. NIR-II PA tomographic imaging shows active targeting of BTII-DUPA SPN to PSMA-positive prostate tumor in living mice. a) Photograph of a nude mouse bearing LNCaP (PSMA-positive) and PC-3 (PSMA-negative) xenografts on opposite flanks. b) Representative PA/ultrasound coregistered images of LNCaP and PC-3 tumors before and after intravenous injection of BTII-DUPA SPN solution (200 µL, 800 µg $m ^ { i - 1 } )$ . Ultrasound images (gray) delineate the tumor boundaries, while the PA images (hot red) show the accumulation and distribution of BTII-DUPA SPN in tumor region $( n = 5 )$ . c) Quantification of PA intensity increase in LNCaP and PC-3 tumors as a function of time and the corresponding biexponential fitting curves. $R ^ { 2 } >$ 0.99 for both fitting curves $( n = 5 )$ ). ΔPA intensity was calculated as the PA signal intensity in the tumor region at different time points subtracted by the PA signal intensity in the tumor region at pre-injection. d) The calculated distribution half-lives, elimination half-lives and area under curve (AUC) of BTII-DUPA SPN in LNCaP and $\mathsf { P C } . 3$ tumors $( n = 5 )$ . e) Ex vivo PA quantification of PC-3 tumor, LNCaP tumor and major organs 72 h after intravenous injection of PBS (200 µL) or BTII-DUPA SPN solution (200 µL, 800 µg mL−1 ) (n = 3). f) Histological analysis of major organs 72 h after intravenous injection of PBS (200 µL) or BTII-DUPA SPN solution (200 µL, $8 0 0 \mu \mathrm { g } \mathsf { m } \mathsf { L } ^ { - 1 } )$ . Laser energy density was tuned to 20 mJ $\mathsf { c m } ^ { - 2 }$ at 1064 nm. $\because P < 0 . 7 , \ ^ { * * } P < \mathrm { \dot { 0 } } . 0 1$ , ns: no significant difference in paired t-test. Error bars represent standard error of mean.

PA signal increased significantly throughout the entire LNCaP tumors while much less accumulation of BTII-DUPA SPN was observed only near the surface of PC-3 tumors (Figure 5b). At 6 h post-injection time, the PA intensities reached maxima in both types of tumors, which were 3.9- and 2.0-fold higher than the tissue background in the LNCaP tumors and the PC-3 tumors, respectively (Figure  5b; Figure S4, Supporting Information). Importantly, most of the PA signals were eliminated in PC-3 tumors after 72 h post-injection, while the PA signal intensities in LNCaP tumors remained as high as 2.1- fold greater than the tissue background (Figure 5b; Figure S4,

Supporting Information). To understand the targeting of BTII-DUPA SPN in LNCaP and PC-3 tumors quantitatively, the PA intensity increase was plotted against the post-injection time and fitted by a bi-exponential model (Figure 5c):

$$
C (t) = - A \exp (- \alpha t) + B \exp (- \beta t) \tag {1}
$$

where A and B intercepts on C(t) for each exponential segment of the curve; α and $\beta$ represent rate constants in the distribution phase and elimination phase, respectively.[69–71] The distribution half-lives $( \tau _ { 1 / 2 \alpha } )$ and elimination half-lives $( \tau _ { 1 / 2 \beta } )$ were extracted from the fitting curves and summarized in Figure 5d. The results reveal that BTII-DUPA SPN distributed 1.5-fold faster in LNCaP tumors $( \tau _ { 1 / 2 \alpha } = 1 . 3 ~ \pm ~ 0 . 5 \mathrm { h } )$ ) than that in PC-3 tumors $( \tau _ { 1 / 2 \alpha } = 1 . 9 \pm 0 . 5 \ \mathrm { h } )$ , while the retention was nearly twofold longer in LNCaP tumors $( \tau _ { 1 / 2 \beta } = 4 1 . 6 \pm 8 . 7$ h) than that in PC-3 tumors $( \tau _ { 1 / 2 \beta } = 2 1 . 6 \pm 3 . 9 \ )$ h). Also, the area under curve (AUC) was calculated as a metric of nanoparticle accumulation in tumors,[72] which suggests 3.8-fold enhanced accumulation of nanoparticles in the LNCaP tumors as compared to that in the PC-3 tumors. The difference in distribution and elimination kinetics of BTII-DUPA SPN between LNCaP tumors and PC-3 tumors reflects the advantages of active targeting over the passive targeting through EPR effect that it can differentiate PSMA-positive prostate tumors from other tumors.

To evaluate the biodistribution of BTII-DUPA SPN, ex vivo PA imaging of tumors and major organs was performed at 72 h post-injection time (Figure  5e; Figure S5, Supporting Information). BTII-DUPA SPN had noticeable accumulation in the major reticuloendothelial system (RES) organs such as liver and spleen, but minimal accumulation in other organs.[59] Nevertheless, by virtue of the targeting effect, BTII-DUPA SPN shows 2.3-fold higher accumulation in the LNCaP tumors as compared with the PC-3 tumors, which is consistent with the real-time PA measurements in vivo.

Moreover, negligible weight loss was observed in mice (Figure S6, Supporting Information) and no noticeable histopathological damage was observed in major organs after intravenous administrations of BTII-DUPA SPN (Figure 5f). These results verify the in vivo biocompatibility of BTII-DUPA SPN.

## 2.6. Mapping of BTII-DUPA SPN Inside Tumor Tissue

The large-area mapping of the whole-tissue slices was achieved by TA microscopy to study the distribution of BTU-DUPA SPN in different tumors at cellular level with high spatial resolution. The probe beam was switched between 853 and 802 nm, while the pump beam was fixed at 1045 nm (Scheme S2, Supporting Information). We hypothesized that with a probe beam at 853 nm, only BTII-DUPA SPN will contribute to TA signal, and with a probe beam at 802 nm, the detected signal mainly attributed to the stimulated Raman scattering (SRS) signal of C-H bonds dominating in cells.[73] Our hypothesis was first validated by imaging of LNCaP and PC-3 tumor tissue slices from the mice without nanoparticles administration, both of which showed negligible signals at 853 nm probe (Figure 6a). Then, tissue imaging was performed with LNCaP and PC-3 tumors harvested at 72 h after intravenous injection of BTII-DUPA SPN (Figure  6b). In the PC-3 tumor tissue slices, relatively intense TA signals only appeared around the blood vessels (BVs, indicated by yellow arrows in the images), meaning that some of the BTU-DUPA SPN escaped from the blood yessels and gradually diffused into the nearby tumor tissue through EPR effect, but most nanoparticles inside the tissue were washed away by blood circulation (Figure  6c). On the contrary, substantial amount of BTII-DUPA SPN was presented throughout the entire tissue slice of LNCaP tumor, indicating specific binding of nanoparticles to PSMA-positive cancer cells and the consecutive cellular endocytosis to retain the nanoparticles (Figure  6b,c). This also highlights the ability of BTII-DUPA SPN to specifically label the entire prostate tumor that has high PSMA expression level. Taking advantage of the subcellular resolution of TA microscopy system, the cellular binding and uptake by individual cells were clearly visualized in LNCaP tissue at the single-cell level (Figure 6d). On the other hand, only a few nanoparticles were randomly trapped in PC-3 tissue without any intracellular accumulation. Interestingly, an obvious separation of nanoparticle distribution between can cerous tissue (left-side of the image) and normal tissue (right side of the image) at the LNCaP tumor margin was observed, further confirming the binding specificity to PSMA-positive cells (Figure 6e). In summary, BTII-DUPA SPN shows a great potential for prostate cancer diagnosis with high targeting spec ificity, and the clear tumor margin delineated by BTII-DUPA SPN will allow precision tumor resection with intraoperative margin assessment.

## 3. Discussion

In order to rationally design the targeted PA probe and pushing toward bench-to-bedside translation, insights into the interaction of nano-sized probes with the biological systems at various levels (i.e., organ system, organ, tissue, and cell) are of paramount importance. The high heterogeneity nature of tumor tissues results in the inconsistency in the in vivo studies.[74] In addition, the targets are localized at sub-cellular compartments and are not uniformly distributed throughout a single tumor.[44] Accordingly, it is essential to study SPNs at cellular level by using advanced non-fluorescence microscopy. Although in vivo PA tomographic imaging of tumors with SPNs have been extensively studied[43] and more recently NIR-II photoacoustic microscopy imaging of living tissues with SPNs has also been reported,[75] investigation at cellular level has been deficient so far. On the other hand. PA agents usually show low or no fluorescence signals for conventional fluorescence imaging. As an efficient PA agent, the conversion of absorbed optical energy into thermal energy and later acoustic signal is through nonradiative decay, and the radiative decay (fluorescence emis sion) is inactivated, resulting in minimized fluorescence signa generation.[15]

In TA microscopy, the change of probe beam induced by the transient absorption of the pump beam is sensed. The advantages of TA microscopy include label free, high sensitivity, high temporal and spatial resolution, low photodamage, and inherent sectioning capability.[76–78] TA microscopy has been applied for imaging of metal nanoparticles,[64,79,80] carbon nanomaterials,[81,82] and nonfluorescent chromophores.[83–86] highlighting its potential as an enabling tool for label-free characterization of materials.

PA tomography and TA microscopy are two very different methods, and we harnessed the advantages of each technique to study the NIR-II SPN. PA tomography provided deep imaging depth for in vivo imaging and potential clinical applications, but its spatial resolution is usually limited. On the other hand, TA microscopy offered sub-micrometer resolution and ultra-high for imaging non-fluorescent agents, so it is suitable for in vitro characterization at single-cell level. In this work, TA microscopy helped us to determine the efficiency, kinetics, and specificity of BTII-DUPA SPN for targeting tumor cells and to map the distribution of SPN inside a tumor tissue at a much higher resolution, which not only confirmed our in vivo PA tomography findings but also provided a deep insight of the tumor targeting mechanisms.

(a)  
![](images/77bc4e366a5909a777294562e5c7f10c1b2316f669fd3db81288c3bd9f33638b.jpg)

<details>
<summary>text_image</summary>

LNCaP, control
</details>

![](images/5ae854367e587a260512649c694e7d54808679d61af3e8883da52313ee4c3355.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a red-stained biological sample labeled 'LNCaP, control' (no additional text or symbols visible)
</details>

![](images/741fc949b4c3f64c04e0a586059299c2a6f8c902c3b8a04737705eb48d71b61c.jpg)

<details>
<summary>text_image</summary>

PC-3, control
</details>

![](images/75c399c3b3b07421859aadbc38eb242eb232e9f22f16268f49d7502154ca7f6d.jpg)

<details>
<summary>text_image</summary>

PC-3, control
2 mm
</details>

![](images/6ead7d8418890728f7be7a8fa5e8729f492f0d09ed3d2f7d19000848f5c82fde.jpg)

(b)  
![](images/7c00dbca42e4a4b95b57f95172fca0fdeb317e871e6070a7c686175a79787725.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological sample with LNCaP label and highlighted regions (no text or symbols beyond label)
</details>

![](images/56ec40f7983e7cdb4062c8939a60de44e33a971bb785c89b342d2321a088f0fd.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing cellular structures with a highlighted region, labeled 'PC-3' in the top-left corner (no other text or symbols)
</details>

256

![](images/fd4dc7d9d45be6170b4cd35626435aa11f198599f0b4aee9e2c7d59f074fae30.jpg)

<details>
<summary>text_image</summary>

LNCaP
</details>

![](images/a9c6b0b354fd1ebd263eeff8fc12838b5e59ad7744e555798ee6a0e0825f3151.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a red-stained biological structure with scale bar indicating 2 mm (no text or symbols present)
</details>

(c)  
![](images/d9ad5045082aacd73b4557fe6786e7043be5693423a3250cd6a4ec4eda2650b3.jpg)

![](images/928ac126cfe77d80825684bb8528109ffc54d36a3da3c882f019c43b64a925ec.jpg)

![](images/c41cf8ab026d72774bdfd9d8b37d8cb5c8814976d387ec9c5369bd63fe582306.jpg)

![](images/9720b123c6d3717cb43234b9382bb444f19652561e35433c7df72782c36c901c.jpg)

![](images/c567d5c6fdb3bffe729c9aec98541b9e4ef6c4f34d173ff31b13881d2ec9fe06.jpg)

![](images/19c52004369aa977008ddee913216ab662b20e7352ee2f15343d33b4b3d8ade2.jpg)

![](images/8b62c3fef4bbb0f79456eb78fbd3548b567c5ef5221df356e75284d3f955faa7.jpg)

![](images/eb23113c8d6d1377285e9f932afae9dd3edce55e01274c81c503abf0c3336e0b.jpg)

(d)  
![](images/4ce701ee1d1e343303a392ea116935e0b18ca32359e95bde97484b4858d7c105.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing red and blue fluorescent staining with white arrow annotations and a scale bar (no text or symbols beyond labels)
</details>

![](images/c79336063f255ca27d2fb3e6a1a5ed4290ce386f68b6ffba509f6119c4435562.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of red-stained tissue with scale bar indicating 40 μm (no text or symbols present)
</details>

(e)  
![](images/6dda17cefae25be5229ccf58b85aae5873d4aa6d121f79f7b2552a2fc44886e9.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of red-stained tissue with blue fluorescent labeling, labeled 'LNCaP' in top right corner (no other text or symbols)
</details>

![](images/2cfbe3963012b6988803bad9e0b14a33e2912a66fbf7e08e4e26019067c788ef.jpg)

<details>
<summary>natural_image</summary>

Microscopic tissue section stained with LNCaP, showing pink and purple cellular structures with a 200 μm scale bar (no text or symbols beyond labels)
</details>

Figure 6. High-resolution mapping of BTII-DUPA SPN inside tumor tissue slices was achieved by TA microscopy. a) and b) SRS (red) and TA (cyan hot) images of LNCaP and PC-3 tumor tissues harvested 72 h after intravenous injection of a) PBS (200 µL) or b) BTII-DUPA SPN solution (200 µL, $8 0 0 \mu \mathrm { g } \mathsf { m } \mathsf { L } ^ { - 1 } )$ . c) Zoom-in images of the ROI indicated by white solid frames in (b), and their corresponding adjacent H&E staining images. The blood vessels (BVs) are indicated by yellow arrows. d) TA/SRS images of LNCaP and PC-3 tumor tissues at single-cell level. e) TA/SRS image of the LNCaP tumor margin indicated by white dotted frame in (b), and the adjacent H&E staining image. Laser power was 20 mW for pump beam at 1045 nm and 10 mW for probe beam at 853 nm or 20 mW for probe beam at 802 nm, before microscope.

To our best knowledge, it is the first report to utilize TA microscopy to investigate the interaction between nonfluorescent PA probes and the biological systems at single cell level, which circumvents the heterogeneity in tissues and provides robust evidence for the specific targeting to the subcellular compartments. The combined PA tomography and TA microscopy can serve as a new platform to study nonfluorescent PA agents at multiscales to gain complete understanding of their behaviors in biological systems and paves a way for the new development of functionalized PA agents.

## 4. Conclusion

We have developed NIR-II absorbing BTII-DUPA SPNs with PSMA-targeting function for prostate cancer detection through TA microscopy and PA tomography. The unique NIR-II absorption profile of BTII-DUPA provides high SNR in tissue and an imaging depth (>4.2 cm) greater than the size of a entire human prostate. The targeting specificity is investigated at multi-scales from single-cell to whole-organ level by TA microscopy and PA tomography. TA microscopy provides sub-micrometer resolution and ultra-high sensitivity for studying SPN properties at single-cell level. By using TA microscopy, optimal parameters for targeting tumor cells are determined in vitro and multiple evidences are revealed to support the specific targeting of BTII-DUPA SPN to prostate cancer cells. The PA tomography study further validates the specific targeting of BTII-DUPA SPN to PSMA-positive prostate tumor in vivo. Lastly, the distribution of BTII-DUPA SPN inside a tumor tissue is mapped by TA microscopy to confirm the PA results and to differentiate the active targeting from the EPR effect. Based on the established correlation between prostate cancer progression and PSMA expression[45–50,54] , we expect that BTII-DUPA SPNs can be used not only for tumor detection but also for evaluation of aggressiveness and recurrence of prostate cancer with superior imaging contrast and depth in NIR-II PA tomography.

## 5. Experimental Section

Synthesis of DUPA-F127-DUPA: All reagents were purchased and used without further purification unless otherwise noted. This compound was synthesized according to the literature.[58] Triphosgene (883 mg, 3 mmol) was added in DCM (20 mL) and stirred at ${ \mathsf { 0 } } \ { \mathsf { o } } { \mathsf { C } } .$ A mixture solution of DIPEA (3.4  g, 26.6 mmol) and HCl.Cbz-Lys-Ot-Bu (3 g, 8.1  mmol) in dichloromethane (DCM; 20 mL) was added dropwise to the triphosgene solution over 1 h. A solution of l-glutamic acid di-tert-butyl ester hydrochloride (2.4 g, 8.1 mmol) and DIPEA (2.3 g, 17.9 mmol) in DCM (20 mL) was then added into the mixture and stirred for 2 h. The mixture was washed with 2 m NaHSO (2× 100 mL) and brine (50 mL) and dried over sodium sulfate to yield a yellow oil. Purification by column chromatography (SiO ) afforded the desired product as clear oil (3.0 g, 4.8 mmol, 60%). 1 H NMR (300 MHz, CDCl ) δ (ppm): 7.38–7.28 (m, 5H), 5.16–5.01 (m, 5H), 4.37–4.29 (m, 2H), 3.21–3.14 (m, 2H), 2.33–1.22 (m, 37H). Ammonium formate (1 g, 16.1 mmol) and 10% Pd/C (0.1  g) was added to a solution of (S)-2-[3-(5-benzyloxycarbonylamino-1-tert-butoxycarbonylpentyl)ureido]-pentanedioic acid di-tert-butyl ester (1 g, 1.61 mmol) in ethanol (20  mL). The solution was stirred at room temperature for 20 h. Then it was filtered to remove the solid and dried in a rotavapor to remove the solvent, yielding the product as a clear oil (750 mg, 95%). 1 H NMR (300 MHz, CDCl ) δ (ppm): 5.20–5.17 (m, 2H), 4.36–4.29 (m, 2H), 2.71–2.59 (m, 2H), 2.40–2.21 (m, 2H), and 2.10–1.08 (m, 35H). To a 20mL DCM solution of F127 (4 g, 0.32 mmol), CDI (154 mg, 0.96 mmol) was added. The solution was stirred at room temperature for 20 h. Then, after adding DCM (40 mL) into the solution that was washed by HCl (20 mL, 0.1M) and brine (20 mL) and dried with sodium sulfate. After removing the solvent, the white solid was dissolved into DCM (20  mL) and (S)-2-[3-(5-amino-1- tert-butoxycarbonylpentyl) ureido]pentanedioic acid di-tert-butyl ester (375 mg, 0.77mmol) was added into the solution that was stirred at 35 oC for 20 h. Then the solution was washed by HCl (20  mL, 0.1  m) twice and then by brine (20 mL), and dried with sodium sulfate. After removing solvent, white solid was obtained (3.5 g, Y = 80%). 1 H NMR (300 MHz, CDCl ) δ (ppm): 3.62–3.37 (m, 26.6H), 2.08–2.01 (m, 0.62H), 1.42 (H on Boc group, m, 1H), 1.23 (m,1.5H), and 1.12 (m,4.26H). To a

DCM (20 mL) solution of tBuDUPA-F127-DUPAtBu (3.3 g, 0.26 mmol), TFA (4mL) was added. The solution was stirred at room temperature for 20 h. Then, DCM (20 mL) was added into the solution that was washed by DI water (20 mL) and brine (20 mL), and dried with sodium sulfate. After removing the solvent, white solid was obtained (3.1  g, Y  =  93%). 1 H NMR (300 MHz, CDCl ) δ (ppm): 3.62–3.37 (m, 1H), 2.08–2.01 (m, 0.02H), 1.23 (m, 0.06H), and 1.12 (m, 0.16H). According to the 1 H NMR of the tBuDUPA-F127-DUPAtBu, we calculated 68.4% of surfactant polymer was added with DUPA.

Synthesis of BTII-DUPA SPN: A standard protocol has been developed to prepare SPNs through the nanoprecipitation method. Briefly, a 1 mL THF mixture of BTII (0.5 mg mL−1 ) and surfactant F127/DUPA-F127-DUPA (20 mg mL−1 ) was rapidly injected into deionized water (9 mL) under continuous sonication with a micro tip-equipped probe sonicator (Branson, W-150) at a power output of 4 watts RMS for 30 s. After sonication for additional 1 min, THF was removed by nitrogen bubbling. The aqueous solution was filtered through a polyethersulfone syringe driven filter (0.22 µm) and centrifuged three times using a 30 K centrifugal filter unit at 3500 rpm for 30 min. The nanoparticle solution was finally concentrated to 1.0 mg mL−1 (based on the mass of BTII) by ultrafiltration and stored in dark at $4 ^ { \circ } \mathbb { C } .$

Characterization: 1 H and $^ { 1 3 } { \mathsf { C } }$ NMR spectra were recorded on a Brucker ARX 400 at 293 K with deuterated chloroform as the solvent. DLS was performed using a Malvern Nano-zetasizer. UV–vis–NIR spectra were recorded with Cary-5000. TEM imaging: For negative staining, 4–6 µL sample was applied to a continuous-carbon or Formvar-carbon coated grid, washed with water, and then stained using 1% uranyl acetate. Grids were imaged in a Philips CM12 transmission electron microscope equipped with a LaB6 electron source, operated at 120 kV. Images were recorded at a magnification of 13 000× on a TVIPS CCD camera with a pixel size of 24 um.

PA Spectroscopy: Schematic illustration of the PA spectroscopy setup is shown in Scheme S1, Supporting Information. The OPO Laser (EKSPLA NT320) with pulse width 5 ns, repetition rate 10 Hz was applied as excitation laser resource. Nikon Eclipse TE2000-U inverted microscope with 10× objective was used to focus the light to the sample. The laser energy after an ND filter was 40–120 µJ. Single element transducer (v317-sm, 20 MHz) was used to acquire acoustic and photoacoustic signals. A preamplifier (Olympus 5682, voltage gain 30 dB) and a pulser/receiver (Olympus 5073 pr, ultrasonic bandwidth 75 MHz, voltage gain 39 dB) were used to improve the system sensitivity. All the samples were in the solution state and were sealed in 1 mm diameter glass tube. $\mathsf { D } _ { 2 } \mathsf { O }$ was applied as the sound coupling agent to avoid water absorption.

PA Tomography: Schematic illustration of the PA tomography setup is shown in Scheme S3, Supporting Information. The ultrasound and photoacoustic signals were processed by a high-frequency ultrasound imaging system (Vantage128, Verasonics Inc.). An EKSPLA OPO Laser with pulse width 5 ns, repetition rate 10 Hz was applied as excitation laser for multispectral PA tomography. A Q-switched Nd:YAG laser (CFR ICE450, Quantel Laer) with 8 ns pulse with a 10 Hz repetition rate was applied as the excitation laser for other experiments. For the imaging depth study in chicken breast, a transmission-mode detection modality was adopted in imaging depth study in chicken breast. The laser light was guided to the tissue surface by a fiber bundle and the photoacoustic signals were detected from the other size of the tissue by a low-frequency transducer array (L7-4, PHILIPS/ATL). For other experiments, a refectionmode detection was applied with using a customized collinear probe, which has a customized high-frequency ultrasound array with 128 elements and 50% bandwidth (L22-14v, Verasonics Inc.).

TA Microscopy: Schematic illustration of a multimodal TA/SRS microscope is shown in Scheme S2, Supporting Information. An 80 MHz repetition rate femtosecond pulsed laser (Spectra Physics, InSight X3) provided two synchronized outputs: a fixed 1045 nm beam with ≈200 fs pulse width and a tunable beam ranging from 680 to 1300 nm with ≈120 fs pulse width. In the TA microscopy system, the fixed 1045 nm beam served as pump source and the other beam served as probe beam was tuned to 853 nm. The resulted laser beating frequency (2154 cm−1 ) is far away from the C-H region between 2800 and 3000 cm−1 , avoiding any signals from the biological systems. The pump beam was modulated at 2.3 MHz by an acousto-optic modulator (Isomet, 1205-C). Temporal delay between the pump and probe pulses was controlled by a motorized translation stage (Zaber, TLS28E), and collinearly combined and directed into a homebuilt laser-scanning microscope. Then, the pump and probe beams were focused on the sample by a 60× water immersion objective (NA = 1.2, UPlanApo/IR, Olympus), and the forward signals were collected by an oil condenser (NA = 1.4, U-AAC, Olympus). After passing an 850 ± 120 nm filter, the 853 nm light was blocked and the TA signals (gain in the 1045 nm probe beam) were detected by a photodiode (Hamamatsu, S3994) incorporated with a home-built resonant circuit, which were demodulated by a phase-sensitive lock-in amplifier (Zurich Instruments). All images were acquired with 10 µs pixel−1 dwell time. The probe (853 nm) and pump (1045 nm) powers before the microscope were maintained at 10 and 20 mW, respectively. More details can be found in the Supporting Information.

SRS imaging of C-H bonds is implemented on the same TA microscope. For SRS imaging, the 1045 nm laser served as the Stokes beam while the tunable laser was adjusted to 802 nm as the pump beam. The resulted laser beating frequency (2899 cm−1 ) is within the C-H region between 2800 and 3000 cm−1 . The SRS signals (signal loss in the 1045 nm Stokes beam) was detected by the photodiode, which were demodulated with the digital lock-in amplifier (Zurich Instrument). Al images were acquired with 10 µs pixel–1 dwell time. The pump (802 nm) and Stokes (1045 nm) powers before the microscope were maintained at 20 and 20 mW, respectively.

In Vitro TA Imaging of BTII-DUPA SPN: For cellular imaging, cells were treated with 13.3 µg mL−1 and incubated at 37 oC for different periods of time. Before the imaging, the cells were washed three times by fresh cell culture medium to remove extracellular and unbound nanoparticles.

Ex Vivo TA Imaging of BTII-DUPA SPN: Mice were euthanatized 72 h after intravenous injection of BTII-DUPA SPNs. Tumor tissues were immediately frozen in liquid nitrogen to preserve the tissue architecture. The frozen tissues were cut in pairs, that one slice in 100 µm for tissue imaging and the neighboring slice in 8–10 µm for H&E staining. The signals outside the region of interest in the large-area TA imaging of tissue slice were cropped.

Cell Culture: All the cell lines were purchased from American Type Culture Collection (ATCC). LNCaP cells were cultured in RPMI-1640 supplemented 10% fetal bovine serum (FBS). PC-3 cells were cultured in F-12K supplemented 10% FBS. HFB cells were cultured in DMEM supplemented 10% FBS. The cells were maintained in a humid environment containing 5% CO and 95% air at 37 oC.

Cytotoxicity Test: LNCaP Cells were first seeded in 96-well plates (3000–5000 cells per well) for, and the culture medium was replaced with fresh medium containing polymer SPN at different concentrations (0–100 µg mL−1 ) and incubated for 24 h. The cell viability was then measured by MTS Assay Kit (Abcam plc.).

Tumor Mouse Model: Four to 6 weeks old male nude mice obtained from Charles River Laboratories were inoculated subcutaneously with 3  ×  106 PC-3 cells in the rear left flanks and 5  ×  106 LNCaP cells in the rear right flanks. Mice were used in imaging studies when either PC-3 or LNCaP tumors reached 8−10 mm in diameter. All protocols were approved by the Boston University Animal Care and Use Committee.

In Vivo PA Tomography Imaging of Tumor: Tumors bearing mice were anesthetized using 2% isoflurane in oxygen delivered through a nose cone and their body temperature was maintained by a heat pad during the PA imaging period. PA images of PC-3 and LNCaP tumors on the same mouse before (pre) and 3, 6, 12, 24, 36, 48, and 72 h after intravenous injection of 200 µL BTII-DUPA SPN (800 µg mL−1 ) were collected, respectively. All animal experiments were performed in compliance with the Guidelines for the Care and Use of Research Animals established by the Boston University Animal Studies Committee.

Imaging Nanoparticle Solution in Matrigel In Vivo: Nanoparticles were suspended in 50% v/v Matrigel (BD Biosciences) to different concentrations. A total of 50 µL PBS or nanoparticle Matrigel mixture was subcutaneously injected into the dorsal space of male nude mice (Charles River Laboratories), and PA imaging of the inclusions was performed with our PA tomography system at wavelengths from 1100 to 1300 nm in 20 nm interval. Then, concentration images of lipid, blood, and BTII-DUPA SPN were generated from the multispectral images via LASSO analysis in Matlab.

LASSO Analysis: To perform chemical analysis, the hyperspectral image D (consisting of spectra from every pixel) should be decomposed into the linear combination of two smaller matrices C and S, corresponding to concentration maps of each component and the spectral profiles for each component. Once S is determined by measuring spectra from pure samples, C can be obtained through a least square fitting In our study, to further improve the robustness against noise and suppress crosstalks between different channels, a sparsity constraint, termed LASSO (least absolute shrinkage and selection operator), was introduced to the original least square fitting problem, resulting in the following:

$$
\hat {C} = \arg \min _ {C} \left\{\frac {1}{2} (D - C S) ^ {2} + \lambda | C | \right\} \tag {2}
$$

Solving the above equation yielded the concentration maps for all channels.

## Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements

This work is supported by a Keck Foundation grant to J. Cheng, the Showalter Trust Research Award and Startup grant by Purdue University to J.M., and JSPS KAKENHI Grants No. 17K05830 to M.A. The authors thank Lu Lan (Boston University) for his help in photoacoustic imaging experiments; Haonan Lin (Boston University) for providing Matlab code for LASSO analysis. Prof. Esther Bullitt (Boston University School of Medicine) for her assistance in transmission electron microscopy.

## Conflict of Interest

The authors declare no conflict of interest.

## Keywords

nanoparticles, photoacoustic tomography, prostate cancer, prostate specific membrane antigen (PSMA), semiconducting polymers, transient absorption microscopy

Received: February 25, 2020

Revised: March 22, 2020

Published online: April 20, 2020

[1] R. L. Siegel, K. D. Miller, A. Jemal, Ca-Cancer J. Clin. 2019, 69, 7.  
[2] W. R. Farwell, J. A. Linder, A. K. Jha, Arch. Intern. Med. 2007, 167, 2497.  
[3] K. Lin, R. Lipsitz, T. Miller, S. Janakiraman, Ann. Intern. Med. 2008, 149, 192.  
[4] F. Algaba, in Atlas of Multiparametric Prostate MRI, Springer, Basel, Switzerland 2018. p. 47  
[5] G. L. Andriole, Nat. Rev. Urol. 2009, 6, 188.  
[6] I. G.  Schoots, M. J.  Roobol, D.  Nieboer, C. H.  Bangma, E. W. Steyerberg, M. M. Hunink, Eur. Urol. 2015, 68, 438.  
[7] V.  Scattoni, A.  Zlotta, R.  Montironi, C.  Schulman, P.  Rigatti, F. Montorsi, Eur. Urol. 2007, 52, 1309.  
[8] S. C.  Berngard, K. O.  Rove, J.  Rassweiler, O.  Kalthoff, M.  Hruz, E. D.  Crawford, in Imaging and Focal Therapy of Early Prostate Cancer, Springer, Berlin/Heidelberg, Germany 2013, p. 103.  
[9] D.  Fehr, H.  Veeraraghavan, A.  Wibmer, T.  Gondo, K.  Matsumoto, H. A.  Vargas, E.  Sala, H.  Hricak, J. O.  Deasy, Proc. Natl. Acad. Sci. USA 2015, 112, E6265.  
[10] M. Kongnyuy, A. K. George, A. R. Rastinehad, P. A. Pinto, Curr. Urol. Rep. 2016, 17, 32.  
[11] M. Xu, L. V. Wang, Rev. Sci. Instrum. 2006, 77, 041101.  
[12] C. Li, L. V. Wang, Phys. Med. Biol. 2009, 54, R59.  
[13] S. Mallidi, G. P. Luke, S. Emelianov, Trends Biotechnol. 2011, 29, 213.  
[14] L. V. Wang, L. Gao, Annu. Rev. Biomed. Eng. 2014, 16, 155.  
[15] L. V. Wang, J. Yao, Nat. Methods 2016, 13, 627.  
[16] L. V. Wang, S. Hu, Science 2012, 335, 1458.  
[17] X.  Wang, W. W.  Roberts, P. L.  Carson, D. P.  Wood, J. B.  Fowlkes, Biomed. Opt. Express 2010, 1, 1117.  
[18] K. S. Valluru, J. K. Willmann, Ultrasonography 2016, 35, 267.  
[19] A.  Horiguchi, M.  Shinchi, A.  Nakamura, T.  Wada, K.  Ito, T.  Asano, H. Shinmoto, H. Tsuda, M. Ishihara, Urology 2017, 108, 212.  
[20] G. Russo, M. Mischi, W. Scheepens, J. J. De la Rosette, H. Wijkstra, BJU Int. 2012, 110, E794.  
[21] L. Fass, Mol. Oncol. 2008, 2, 115.  
[22] S. Lee, J. Xie, X. Chen, Biochemistry 2010, 49, 1364.  
[23] K. Strebhardt, A. Ullrich, Nat. Rev. Cancer 2008, 8, 473.  
[24] A.  Agarwal, S. W.  Huang, M.  O’Donnell, K. C.  Day, M.  Day, N. Kotov, S. Ashkenazi, J. Appl. Phys. 2007, 102, 064701.  
[25] V.  Dogra, B.  Chinni, S.  Singh, H.  Schmitthenner, N.  Rao, J. J. Krolewski, K. L. Nastiuk, J. Biomed. Opt. 2016, 21, 66019.  
[26] H. K.  Zhang, Y.  Chen, J.  Kang, A.  Lisok, I.  Minn, M. G.  Pomper, E. M. Boctor, J. Biophoton. 2018, 11, e201800021.  
[27] J.  Li, S. J.  Yoon, B. Y.  Hsieh, W.  Tai, M.  O’Donnell, X.  Gao, Nano Lett. 2015, 15, 8217.  
[28] G. Xu, M. Qin, A. Mukundan, J. Siddiqui, M. Takada, P. Vilar-Saavedra, S. A. Tomlins, R. Kopelman, X. Wang, Proc. SPIE 2016, 9708  
[29] A. M. Smith, M. C. Mancini, S. Nie, Nat. Nanotechnol. 2009, 4, 710.  
[30] M.  Pramanik, M.  Swierczewska, D.  Green, B.  Sitharaman, L. V. Wang, J. Biomed. Opt. 2009, 14, 034018.  
[31] G. Ku, M. Zhou, S. Song, Q. Huang, J. Hazle, C. Li, ACS Nano 2012, 6, 7489.  
[32] G.  Hong, S.  Diao, J.  Chang, A. L.  Antaris, C.  Chen, B.  Zhang, S.  Zhao, D. N.  Atochin, P. L.  Huang, K. I.  Andreasson, Nat. Pho tonics 2014, 8, 723.  
[33] Y. Sheng, L. D. Liao, N. Thakor, M. C. Tan, Sci. Rep. 2014, 4, 6562.  
[34] Y.  Zhou, D.  Wang, Y.  Zhang, U.  Chitgupi, J.  Geng, Y.  Wang, Y. Zhang, T. R. Cook, J. Xia, J. F. Lovell, Theranostics 2016, 6, 688.  
[35] F.  Wang, H.  Wan, Z.  Ma, Y.  Zhong, Q.  Sun, Y.  Tian, L.  Qu, H.  Du, M.  Zhang, L.  Li, H.  Ma, J.  Luo, Y.  Liang, W. J.  Li, G.  Hong, L.  Liu, H. Dai, Nat. Methods 2019, 16, 545.  
[36] H. Liu, G. Hong, Z. Luo, J. Chen, J. Chang, M. Gong, H. He, J. Yang, X.  Yuan, L.  Li, X.  Mu, J.  Wang, W.  Mi, J.  Luo, J.  Xie, X. D.  Zhang, Adv. Mater. 2019, 31, e1901015.  
[37] Y. S.  Chen, Y.  Zhao, S. J.  Yoon, S. S.  Gambhir, S.  Emelianov, Nat Nanotechnol, 2019, 14, 465.  
[38] K.  Welsher, Z.  Liu, S. P.  Sherlock, J. T.  Robinson, Z.  Chen, D. Daranciang, H. Dai, Nat. Nanotechnol. 2009, 4, 773.  
[39] P. K. Upputuri, M. Pramanik, J. Biomed. Opt. 2019, 24, 1.  
[40] J.  Wu, L.  You, L.  Lan, H. J.  Lee, S. T.  Chaudhry, R.  Li, J. X.  Cheng, J. Mei, Adv. Mater. 2017, 29.  
[41] Y.  Jiang, P. K.  Upputuri, C.  Xie, Y.  Lyu, L.  Zhang, Q.  Xiong, M. Pramanik, K. Pu, Nano Lett. 2017, 17, 4964.  
[42] B.  Guo, Z.  Sheng, K.  Kenry, D.  Hu, X.  Lin, S.  Xu, C.  Liu, H.  Zheng, B. Liu, Mater. Horiz. 2017, 4, 1151.  
[43] Q. Miao, K. Pu, Adv. Mater. 2018, 30, e1801778.  
[44] D.  Peer, J. M.  Karp, S.  Hong, O. C.  Farokhzad, R.  Margalit, R. Langer, Nat. Nanotechnol. 2007, 2, 751.  
[45] G. L.  Wright Jr., C.  Haley, M. L.  Beckett, P. F.  Schellhammer, Urol. Oncol. 1995, 1, 18.  
[46] D. A. Silver, I. Pellicer, W. R. Fair, W. Heston, C. Cordon-Cardo, Clin. Cancer Res. 1997, 3, 81.  
[47] A. Ghosh, W. D. Heston, J. Cell. Biochem. 2004, 91, 528.  
[48] A. Barve, W. Jin, K. Cheng, J. Controlled Release 2014, 187, 118.  
[49] D. G. Bostwick, A. Pacelli, M. Blute, P. Roche, G. P. Murphy, Cancer 1998, 82, 2256.  
[50] S. A. Kularatne, K. Wang, H. K. Santhapuram, P. S. Low, Mol. Phar maceutics 2009, 6, 780.  
[51] Y.  Chen, S.  Dhara, S. R.  Banerjee, Y.  Byun, M.  Pullambhatla, R. C. Mease, M. G. Pomper, Biochem. Biophys. Res. Commun. 2009, 390, 624.  
[52] T.  Liu, L. Y.  Wu, M. R.  Hopkins, J. K.  Choi, C. E.  Berkman, Bioorg. Med. Chem. Lett. 2010, 20, 7124.  
[53] Y.  Chen, M.  Pullambhatla, S. R.  Banerjee, Y.  Byun, M.  Stathis, C.  Rojas, B. S.  Slusher, R. C.  Mease, M. G.  Pomper, Bioconjugate Chem. 2012, 23, 2377.  
[54] A.  Afshar-Oromieh, E.  Avtzi, F. L.  Giesel, T.  Holland-Letz, H. G.  Linhart, M.  Eder, M.  Eisenhut, S.  Boxler, B. A.  Hadaschik, C. Kratochwil, W. Weichert, K. Kopka, J. Debus, U. Haberkorn, Eur. J. Nucl. Med. Mol. Imaging 2015, 42, 197.  
[55] L. E.  Kelderhouse, V.  Chelvam, C.  Wayua, S.  Mahalingam, S.  Poh, S. A. Kularatne, P. S. Low, Bioconjugate Chem. 2013, 24, 1075.  
[56] S. A.  Kularatne, M.  Thomas, C. H.  Myers, P.  Gagare, A. K.  Kanduluru, C. J.  Crian, B. N.  Cichocki, Clin. Cancer Res. 2019, 25, 177.  
[57] X.  Luo, D. T.  Tran, H.  Sun, T.  Mi, N. M.  Kadlubowski, Y.  Zhao, K. Zhao, J. Mei, Asian J. Org. Chem. 2018, 7, 2248.  
[58] K. P.  Maresca, S. M.  Hillier, F. J.  Femia, D.  Keith, C.  Barone, J. L.  Joyal, C. N.  Zimmerman, A. P.  Kozikowski, J. A.  Barrett, W. C. Eckelman, J. W. Babich, J. Med. Chem. 2009, 52, 347.  
[59] C.  Xie, P. K.  Upputuri, X.  Zhen, M.  Pramanik, K.  Pu, Biomaterials 2017, 119, 1.  
[60] H. Yamakoshi, K. Dodo, M. Okada, J. Ando, A. Palonpon, K. Fujita, S. Kawata, M. Sodeoka, J. Am. Chem. Soc. 2011, 133, 6102.  
[61] H. J.  Lee, W.  Zhang, D.  Zhang, Y.  Yang, B.  Liu, E. L.  Barker, K. K. Buhman, L. V. Slipchenko, M. Dai, J. X. Cheng, Sci. Rep. 2015, 5, 7930.  
[62] L. Wei, F. Hu, Y. Shen, Z. Chen, Y. Yu, C. C. Lin, M. C. Wang, W. Min, Nat. Methods 2014, 11, 410.  
[63] Y. Jung, M. N. Slipchenko, C. H. Liu, A. E. Ribbe, Z. Zhong, C. Yang, J. X. Cheng, Phys. Rev. Lett. 2010, 105, 217401.  
[64] S. Chong, W. Min, X. S. Xie, J. Phys. Chem. Lett. 2010, 1, 3316.  
[65] Y.  Cao, J.-H.  Dou, N.-J.  Zhao, S.  Zhang, Y.-Q.  Zheng, J.-P.  Zhang, J.-Y. Wang, J. Pei, Y. Wang, Chem. Mater. 2016, 29, 718.  
[66] S. D. Dimitrov, B. C. Schroeder, C. B. Nielsen, H. Bronstein, Z. Fei, I. McCulloch, M. Heeney, J. R. Durrant, Polymers 2016, 8.  
[67] H.  Liu, A. K.  Rajasekaran, P.  Moy, Y.  Xia, S.  Kim, V.  Navarro, R. Rahmati, N. H. Bander, Cancer Res. 1998, 58, 4055.  
[68] L.  Wang, S. L.  Jacques, L.  Zheng, Comput. Methods Prog. Biomed. 1995, 47, 131.  
[69] R. Urso, P. Blardi, G. Giorgi, Eur. Rev. Med. Pharmacol. Sci. 2002, 6, 33.  
[70] J. Liu, M. Yu, C. Zhou, S. Yang, X. Ning, J. Zheng, J. Am. Chem. Soc. 2013, 135, 4978.  
[71] Y.  Zhang, L.  Zhang, G.  Yin, W.  Ma, J.  Li, Z.  Zhou, F.  Gao, Mol. Imaging Biol. 2019, 21, 1044.  
[72] E. A.  Sykes, Q.  Dai, C. D.  Sarsons, J.  Chen, J. V.  Rocheleau, D. M.  Hwang, G.  Zheng, D. T.  Cramb, K. D.  Rinker, W. C.  Chan, Proc. Natl. Acad. Sci. USA 2016, 113, E1142.  
[73] C. W.  Freudiger, W.  Min, B. G.  Saar, S.  Lu, G. R.  Holtom, C.  He, J. C. Tsai, J. X. Kang, X. S. Xie, Science 2008, 322, 1857.  
[74] I. Dagogo-Jack, A. T. Shaw, Nat. Rev. Clin. Oncol. 2018, 15, 81.  
[75] B.  Guo, J.  Chen, N.  Chen, E.  Middha, S.  Xu, Y.  Pan, M.  Wu, K.  Li, C. Liu, B. Liu, Adv. Mater. 2019, 31, e1808355.  
[76] W. R. Zipfel, R. M. Williams, W. W. Webb, Nat. Biotechnol. 2003, 21, 1369.  
[77] D.  Fu, T.  Ye, T. E.  Matthews, G.  Yurtsever, W. S.  Warren, J. Biomed. Opt. 2007, 12, 054004.  
[78] D.  Davydova, A.  de  la Cadena, D.  Akimov, B.  Dietzek, Laser Photonics Rev. 2016, 10, 62.  
[79] O. L. Muskens, N. Del Fatti, F. Vallee, Nano Lett. 2006, 6, 552.  
[80] G. V. Hartland, Chem. Sci. 2010, 1, 303.  
[81] L.  Tong, Y.  Liu, B. D.  Dolash, Y.  Jung, M. N.  Slipchenko, D. E. Bergstrom, J. X. Cheng, Nat. Nanotechnol. 2011, 7, 56.  
[82] J.  Li, W.  Zhang, T. F.  Chung, M. N.  Slipchenko, Y. P.  Chen, J. X. Cheng, C. Yang, Sci. Rep. 2015, 5, 12394.  
[83] T. Ye, D. Fu, W. S. Warren, Photochem. Photobiol. 2009, 85, 631.  
[84] T. E.  Matthews, I. R.  Piletic, M. A.  Selim, M. J.  Simpson, W. S. Warren, Sci. Transl. Med. 2011, 3, 71ra15.  
[85] W.  Min, S.  Lu, S.  Chong, R.  Roy, G. R.  Holtom, X. S.  Xie, Nature 2009, 461, 1105.  
[86] P. T.  Dong, H.  Lin, K. C.  Huang, J. X.  Cheng, Sci. Adv. 2019, 5, eaav0561.  
[87] T. Hasegawa, M. Ashizawa, J. Hiyoshi, S. Kawauchi, J. Mei, Z. Bao, H. Matsumoto, Polym. Chem. 2016, 7, 1181.  
[88] G. W. P.  Van Pruissen, F.  Gholamrezaie, M. M.  Wienk, R. A. J. Janssen, J. Mater. Chem. 2012, 22, 20387.