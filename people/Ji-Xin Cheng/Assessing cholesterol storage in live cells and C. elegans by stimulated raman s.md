## OPEN

SUBJECT AREAS:

MOLECULAR IMAGING

COMPUTATIONAL CHEMISTRY

RAMAN SPECTROSCOPY

STEROLS

Received

3 October 2014

Accepted

22 December 2014

Published

22 January 2015

Correspondence and requests for materials

should be addressed to

M.D. (mjdai@purdue.

edu) or J.-X.C.

(jcheng@purdue.edu)

\* These authors

contributed equally to

this work.

# Assessing Cholesterol Storage in Live Cells and C. elegans by Stimulated Raman Scattering Imaging of Phenyl-Diyne Cholesterol

Hyeon Jeong Lee1,2\*, Wandi Zhang3 \*, Delong Zhang3 , Yang Yang3 , Bin Liu4 , Eric L. Barker1,5, Kimberly K. Buhman1,6, Lyudmila V. Slipchenko3 , Mingji Dai1,3 & Ji-Xin Cheng1,3,7

1 Interdisciplinary Life Science Program, Purdue University, West Lafayette, IN, USA, 2 Department of Comparative Pathobiology, Purdue University, West Lafayette, IN, USA, 3 Department of Chemistry, Purdue University, West Lafayette, IN, USA, 4 National Key Laboratory of Science and Technology on Tunable Laser, Harbin Institute of Technology, Harbin 150080, China, 5 Medicinal Chemistry and Molecular Pharmacology, Purdue University, West Lafayette, IN, USA, 6 Department of Nutrition Science, Purdue University, West Lafayette, IN, USA, 7 Weldon School of Biomedical Engineering, Purdue University, West Lafayette, IN, USA.

We report a cholesterol imaging method using rationally synthesized phenyl-diyne cholesterol (PhDY-Chol) and stimulated Raman scattering (SRS) microscope. The phenyl-diyne group is biologically inert and provides a Raman scattering cross section that is 88 times larger than the endogenous C5O stretching mode. SRS microscopy offers an imaging speed that is faster than spontaneous Raman microscopy by three orders of magnitude, and a detection sensitivity of 31 mM PhDY-Chol (,1,800 molecules in the excitation volume). Inside living CHO cells, PhDY-Chol mimics the behavior of cholesterol, including membrane incorporation and esterification. In a cellular model of Niemann-Pick type C disease, PhDY-Chol reflects the lysosomal accumulation of cholesterol, and shows relocation to lipid droplets after HPbCD treatment. In live , PhDY-Chol mimics cholesterol uptake by intestinal cells and reflects cholesterol storage. Together, our work demonstrates an enabling platform for study of cholesterol storage and trafficking in living cells and vital organisms.

s an important component of cellular membrane, cholesterol controls physical properties of the membrane and contributes to specific membrane structures such as lipid rafts1,2. Inside cells, cholesterol plays an important role in various signaling pathways3,4 and serves as the precursor for signaling molecules, and modifies specific proteins, such as hedgehog, to control protein trafficking and activity5 . The distribution of cholesterol in a living cell is highly regulated6,7. Intracellular cholesterol is stored in lipid droplets (LDs) in the form of cholesteryl ester to avoid the toxicity caused by free cholesterol8,9. Dysregulation of cholesterol metabolism and/or trafficking has been linked to diseases, including atherosclerosis9,10, Niemann-Pick type C (NP-C) disease11, and various cancers12,13. So far, our understanding of cholesterol transport and metabolism is limited, partly due to lack of suitable tools for imaging cholesterol in a living system14.

Intracellular cholesterol transport and metabolism have been studied extensively using various reporter mole cules15, including cholesterol binding molecules and cholesterol analogs. Cholesterol binding molecules, such as cholesterol oxidase, filipin, and perfringolysin O derivatives, are commonly used to study steady-state distribution of cholesterol in fixed cells and tissues16–18. Fluorescent cholesterol, including intrinsic fluorescent sterols such as dehydroergosterol (DHE) and fluorophore-tagged analogs such as 7-nitrobenz-2-oxa-1,3-diazole (NBD)- cholesterol and boron dipyrromethene difluoride (BODIPY)-cholesterol are widely used in vitro and in vivo19–21. Radiolabeled cholesterol or its precursors are used in biochemical studies of metabolism and trafficking of cholesterol15. More recently, clickable cholesterol analogs were also developed for studying cholesterol-binding proteins and tracking cholesterol metabolism and distribution22,23.

These current cholesterol assays have limitations. Cholesterol oxidase is commonly used in fluorometric or colorimetric assays to quantify total cholesterol in homogenized cells. Radiolabeled cholesterol has to be used in combination with separation methods to determine intracellular cholesterol distribution indirectly. For imaging purpose, filipin is the most commonly used molecule for visualizing distribution of free cholesterol, but it is only applicable to fixed cells or tissues with moderate specificity because filipin also labels other lipids24. BODIPY-cholesterol is known to cause perturbations due to bulkiness of the fluorophores25. DHE has the closest structure as cholesterol, but its fluorescence undergoes rapid photo-bleaching15, which impedes real-time observation of cholesterol trafficking. Clickable cholesterol analog requires additional steps before fluorescence imaging.

Owing to smaller volumes compared to fluorophores, Raman tags provide a promising way of imaging biomolecules like DNA and cytochrome c inside cells on a Raman microscope26,27. These Raman tags utilize the vibrational signatures of the carbon-deuterium (C–D) bond, the cyano bond $( { \mathrm { C } } { \bar { = } } \mathrm { N } )$ or the alkyne bond $( { \mathrm { C } } { \equiv } { \mathrm { C } } )$ that are spectrally isolated from the endogenous Raman bands28. Spontaneous Raman imaging has allowed cellular trafficking of different C–D labeled lipid species in fixed cells29, and direct visualization of alkyne-tagged DNA synthesis and cytochrome c release from mitochondria in living $\mathrm { c e l l s } ^ { 2 \mathrm { \ ' { 6 , 2 7 } } }$ with an image acquisition speed of 50 min per frame of $\bar { 1 2 7 } \times 1 2 7$ pixels. To enhance the signal level, nonlinear vibrational microscopy based on the coherent Raman process has been developed30 and deployed for imaging C–D labeled fatty $\mathrm { a c i d } s ^ { 3 1 , 3 2 }$ , amino acids33, and $\dot { \mathrm { d r u g s } } ^ { 3 4 }$ in living cells with a speed that is ,1,000 times faster than with spontaneous Raman microscopy. More recently, stimulated Raman scattering (SRS) imaging of alkyne-tagged molecules has been reported, with a detection limit at the level of hundreds of micromolar35,36. SRS is a third order nonlinear optical process that involves two laser fields, namely, a pump field at $\omega _ { \mathrm { { p } } }$ and a Stokes field at $\omega _ { \mathrm { { S } } } .$ When the beating frequency $( \omega _ { \mathrm { p } } -$ $\mathfrak { o } _ { \mathrm { s } } )$ is tuned to excite a molecular vibration, the energy difference between ${ \mathfrak { O } } _ { \mathfrak { p } }$ and $\omega _ { S }$ pumps the molecule from a ground state to a vibrationally excited state. In correspondence, the laser fields experience a weak decrease in pump beam intensity, called stimulated Raman loss (SRL), and a corresponding increase in Stokes beam intensity, called stimulated Raman gain (SRG). In the case of SRL, the Stokes beam intensity $I _ { \mathrm { S } }$ is modulated and the pump beam intensity $I _ { \mathrm { p } }$ is recorded by a photodiode. The induced modulation is often extracted by a lock-in amplifier. Theoretically, the modulation depth induced by $\mathrm { S R L } , I _ { \mathrm { S R L } } / I _ { \mathrm { p } } ,$ is linearly proportional to the Raman cross section, $\sigma ,$ molar concentration of the target molecule, $N ,$ and the Stokes beam intensity, i.e., $I _ { \mathrm { S R L } } / I _ { \mathrm { p } } \propto \sigma \ : N \ : \bar { I } _ { \mathrm { S } } .$ . SRS microscopy offers much faster imaging speed compared to spontaneous Raman microscopy37.

Here, we report the synthesis of a Raman probe, phenyl-diyne cholesterol (PhDY-Chol), and its use for imaging cholesterol esterification, storage and trafficking inside living cells and vital organisms. By rational design and chemical synthesis, we prepared a probe molecule, PhDY-Chol, which gives a 2,254 cm21 Raman peak that is 88 times stronger than the endogenous $\mathrm { C } { = } \mathrm { O }$ stretching band. Compared to alkyne-tagged cholesterol of which the $\mathrm { \bar { I C } } _ { 5 0 }$ is 16 mM, the phenyl-diyne group is biologically inert and did not cause cytotoxicity after 16 h incubation at 50 mM. In live Chinese hamster ovary (CHO) cells, SRS imaging showed incorporation into plasma membrane, esterification of PhDY-Chol by acyl-CoA: cholesterol acyltransferase 1 (ACAT-1), and storage in LDs. In a cellular model of NP-C disease, PhDY-Chol is selectively accumulated in lysosomes and is esterified and relocated to LDs after treatment with a choles terol-mobilization drug. In live C. elegans, SRS imaging of PhDY-Chol reflected cholesterol uptake through ChUP-1 regulated manner, and storage in the intestinal cells. These studies herald the potential of our method for unveiling intracellular cholesterol trafficking mechanisms and highly efficient screening of drugs that target cho lesterol metabolism.

## Results

Rational design and synthesis of tagged cholesterol with an extremely large Raman scattering cross section. In order to design a probe mole cule that not only maintains physiological functions of cholesterol, but also has a large Raman scattering cross section, we chose to replace the aliphatic side chain of cholesterol with a cyano or an alkynyl group (Fig. 1). These groups have small size, which could minimize structural perturbation of the molecule of interest, in this case, cholesterol. Meanwhile, these groups produce strong Raman scattering peaks in a cellular silent region $\mathrm { \dot { ( 1 , 8 0 0 - 2 , 8 0 0 ~ c m ^ { - 1 } ) ^ { 2 6 , 2 8 } } }$ and therefore, can potentially be used for Raman imaging in a low-concentration condition. It has been reported that as the chain length increases, the hyperpolarizability increases in polyynes38. Also, aromatic ring capped alkyne was shown to give stronger Raman signals than terminal alkyne27. To design tagged cholesterol with very strong Raman intensity, we calculated the Raman cross section of potential tags, namely alkyne, phenyl-alkyne, diyne, and phenyl-diyne, using the Q-Chem and GAMESS electronic structure packages to provide insight of the relation between molecular structure and Raman intensity. Our results show that the localized polarizabilities on each $\mathrm { C } \equiv \mathrm { C }$ moiety increase with the number of conjugated triple bonds, as well as with addition of a phenyl ring (Supplementary Figure 1a and Supplementary Table 1). Thus, the total polarizability of the molecule increases as a result of the additive effect as well as non-linear boost in the polarizability of conjugated bonds. The phenyl ring serves as both a donor and an acceptor of pelectrons from the neighboring triple bonds, further escalating polarizabilities of neighboring conjugated bonds. Taking into account that the Raman intensity is proportional to squares of polarizability derivatives, the additional three-fold enhancement of the total polarizability due to conjugation results in a ,10-fold boost in Raman intensity. Together, compared to the alkyne group, the Raman intensity increases by 9 times by adding a phenyl group to the terminal alkyne, and 52 times by conjugating a phenyl group and another alkyne (Supplementary Fig. 1b).

Based on the above considerations, we have synthesized a series of tagged cholesterols – alkyne cholesterol (A-Chol, 5), phenylalkyne cholesterol (PhA-Chol, 6), phenyl-diyne cholesterol (PhDY-Chol, 7), and cyano cholesterol (CN-Chol, 8), as shown in Figure 1. Our synthesis commenced with commercially available cholenic acid 3. Using a sequence of THP-protection, LiAlH reduction, Dess-Martin oxidation and Seyferth-Gilbert-Bestmann homologation, cholenic acid 3 was converted to compound 4 with a terminal alkyne group in excellent yield. Removal of the THPprotecting group gave probe 5. We further prepared PhA-Chol 6 and PhDY-Chol 7 from compound 4 via a palladium-catalyzed Sonogashira reaction and a copper-catalyzed Cadiot-Chodkiewicz reaction, respectively, followed by acidic removal of THP group. Additionally, CN-Chol 8 was prepared from cholenic acid 3 via standard transformations.

Raman spectral analysis and SRS imaging of tagged cholesterol. To determine the Raman shift of the $\scriptstyle \mathrm { C } \equiv \mathrm { C }$ stretching vibrational mode and to compare the level of Raman signals from the tagged cholesterols, we prepared 50 mM of each compound in cyclohexanone and performed confocal Raman spectral analysis (Fig. 2). The signal from CN-Chol was too weak to be detected. A-Chol showed its peak for C;C vibrational mode at 2,122 cm21 ; PhA-Chol at 2,239 cm21 ; PhDY-Chol at 2,254 cm21 (Fig. 2a). To evaluate the amplitude of the Raman scattering cross section, we fitted each Raman band with a Lorentzian profile and calculated the area under the fitted profile. Compared to the Raman peak of each tag to the 1,714 cm $\stackrel { \cdot } { - 1 } _ { \mathbf { \lambda } }  { \mathbf { \zeta } } _ { } \mathbf { C } = \mathbf { \zeta } \mathbf { O }$ Raman peak from the solvent (9.7 M for pure cyclohexanone), the alkyne, PhA, and PhDY groups were found to be 6, 15, and 88 times stronger in Raman cross section, respectively (Fig. 2b). This result showed that the PhDY tag produces a spectrallyisolated peak, which is stronger than the C5O vibrational mode by two orders of magnitude.

To determine the SRS imaging sensitivity for PhDY-Chol, we used a femtosecond SRL microscope reported elsewhere32. Cyclohexanone

Raman Probe Design:  
![](images/25e2d04bcaacfea84f3ab813649dc1b74955cf57a5ca6e3060dfedfd086fef29.jpg)

<details>
<summary>chemical</summary>

Chemical structure of Cholesterol (1), a steroid derivative with hydroxyl and methyl substituents
</details>

![](images/fd62fddb4009e611be155eb2860abbbbfff8f9c29bc9f8cf27c80a39f0bb470f.jpg)

<details>
<summary>chemical</summary>

Molecular structure of Tagged-cholesterol (2) with Raman Tag label and stereochemistry indicators
</details>

Raman Probe Synthesis:  
![](images/74e18c25e827dbd666c2d0f12716d8c622ae5fc7f9769b1af1445012b03e3c7e.jpg)

<details>
<summary>chemical</summary>

Chemical reaction scheme showing synthesis of compounds 4, A-Chol, PhA-Chol, and PhDY-Chol from cholenic acid (3) using various reagents and conditions.
</details>

![](images/83e1ec58ab3e2fec90ea1ca0731775ecad791b36a54435a05028fc5fcc717beb.jpg)

<details>
<summary>chemical</summary>

Chemical reaction scheme converting cholenic acid (3) to CN-Chol (8) using DHP, LiAlH4, and MsCl under specified conditions
</details>

Figure 1 | Design and synthesis of tagged cholesterol probes. Reagents and conditions: (a) DHP (5.0 equiv), p-TsOH (0.2 equiv), THF, RT, 91%; (b) LiAlH (3.0 equiv), THF, 0uC to RT, 98%; (c) DMP (3.0 equiv), NaHCO (3.0 equiv), $\mathrm { C H } _ { 2 } \mathrm { C l } _ { 2 } , 0 ^ { \circ } \mathrm { C } ,$ 86%; (d) dimethyl (1-diazo-2- oxopropyl)phosphonate (Bestmann reagent, 2.4 equiv), $\mathrm { K } _ { 2 } \mathrm { C O } _ { 3 } \ : ( 4 . 0$ equiv), THF/MeOH, RT, 99%; (e) p-TsOH (1.0 equiv), THF/MeOH, RT, 84%; (f) Iodobenzene (1.02 equiv), PdCl (PPh ) (0.05 equiv), CuI (0.05 equiv), TEA, RT; then p-TsOH (1.0 equiv), THF/MeOH, RT, 77%; (g) CuI (0.1 equiv), $\mathrm { K } _ { 2 } \mathrm { C O } _ { 3 }$ (2.0 equiv), P(o-Tol) (0.2 equiv), phenyl bromoacetylene (1.3 equiv), EtOH, 100uC, 51%; (h) p-TsOH (1.0 equiv), THF/MeOH, RT, 95%; (i) MsCl (3.0 equiv), TEA (3.0 equiv), $\mathrm { C H } _ { 2 } \mathrm { C l } _ { 2 } , 0 ^ { \circ } \mathrm { C }$ to RT, 75%; (j) KCN (2.0 equiv), DMSO, 90uC, 76%; (k) p-TsOH (1.0 equiv), THF/MeOH, RT, 74%. DHP 5 3,4-Dihydro-2H-pyran, DMP 5 Dess-Martin Periodinane, p-TsOH 5 p-Toluenesulfonic acid, TEA 5 triethylamine, P(o-Tol) 5 tri(o tolyl)phosphine, MsCl 5 methanesulfonyl chloride. CN: cyano; A: alkyne; PhA: phenyl-alkyne; PhDY: phenyl-diyne; Chol: cholesterol.

solutions of PhDY-Chol were prepared by serial dilution, and SRS images of PhDY-Chol were recorded with the laser beating frequency tuned to be resonant with C;C vibration at 2,254 cm21 . In solutions without PhDY-Chol, a residual background was detected, caused by cross phase modulation. The SRS contrast, defined as $( \mathsf { S } \mathrm { ~ - ~ } \mathsf { B } ) / \mathsf { B } ,$ where S and B denote SRS signal and background, was calculated as a function of PhDY-Chol molar concentration. At the speed of 200 ms per pixel, a linear relationship was observed (Fig. 2c) and 13% and 4% contrasts were reached at 313 mM and 156 mM, respectively. To increase the detection sensitivity, we chirped the femtosecond lasers to 0.8 picoseconds with a SF-10 glass rod. This spectral focusing approach39 maintained 85% of the SRS signal while reduced the cross phase modulation background level by 3 times, to a level of $6 . 3 \times 1 0 ^ { - 7 }$ in terms of modulation depth. As a result, the SRS contrast became 14% at 31 mM, corres ponding to ,1,800 molecules in the excitation volume (Fig. 2d). We also depicted the modulation depth (DI/I) as a function of molar concentration (Supplementary Fig. 2), which is used for estimating the molar concentration of PhDY-Chol inside cells in following studies.

Cytotoxicity caused by terminal alkyne is avoided by phenyl group. To evaluate the cytotoxicity of tagged cholesterols, we performed MTT cell-viability assays after treating CHO cells with tagged cholesterol. Various concentrations of tagged cholesterol were added to the culture media and the cells were incubated for

a  
![](images/6c4e1fe0632ab55af5eb4f79b3c2230e796deb4f9c823ddf688945cdc83ed774.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | PhDY-Chol (#7) | PhA-Chol (#6) | A-Chol (#5) | CN-Chol (#8) | Chol (#1) | Cyclohexanone |
| ------------------ | -------------- | ------------- | ----------- | ------------ | --------- | ------------- |
| 1600               | ~0.2           | ~0.3          | ~0.4        | ~0.5         | ~0.6      | ~0.7          |
| 1700               | ~0.8           | ~0.9          | ~0.95       | ~0.9         | ~0.95     | ~1.0          |
| 1800               | ~0.1           | ~0.1          | ~0.1        | ~0.1         | ~0.1      | ~0.1          |
| 2000               | ~0.3           | ~0.3          | ~0.3        | ~0.3         | ~0.3      | ~0.3          |
| 2200               | ~0.6           | ~0.6          | ~0.6        | ~0.6         | ~0.6      | ~0.6          |
| 2400               | ~0.2           | ~0.2          | ~0.2        | ~0.2         | ~0.2      | ~0.2          |
</details>

b  
![](images/63a1de5fc86abbcc189a82bd8ebb59a6c98902a72707f1b0c067dbc06ae63e6a.jpg)

<details>
<summary>scatterplot</summary>

| Label         | Raman shift (cm⁻¹) | I_Raman tag / I_C=O |
| ------------- | ------------------ | ------------------- |
| A-Chol (#5)   | 2120               | 5                   |
| PhA-Chol (#6) | 2240               | 15                  |
| CN-Chol (#8)  | 2240               | 0.5                 |
| PhDY-Chol (#7)| 2240               | 100                 |
</details>

c  
![](images/c337bc5e7281a10d4d3aef548ee5e6fce7d095603b9fd2094134a19799957b70.jpg)

<details>
<summary>line chart</summary>

| Concentration (mM) | SRS Contrast (%) |
| ------------------ | ---------------- |
| 0                  | 0                |
| 1                  | 30               |
| 2                  | 45               |
| 5                  | 115              |
| 10                 | 245              |
</details>

d  
![](images/e8b2c5a1b52b57adaa2c03d07e0de935b57033c88a8dea94d28942e9d9039b39.jpg)

<details>
<summary>scatterplot</summary>

| Concentration (mM) | SRS Contrast (%) |
| ------------------ | ---------------- |
| 0.0                | 0                |
| 0.1                | 40               |
| 0.2                | 50               |
| 0.5                | 100              |
</details>

Figure 2 | Raman spectral analysis of tagged cholesterol and SRS detection of PhDY-Chol. (a) Raman spectra of 50 mM tagged cholesterols in cyclohexanone (solvent). Spectral intensity was normalized by C5O vibration band at 1,714 cm21 . Spectral acquisition time: 10 s. (b) Plot of relative intensity of Raman tags versus solvent and Raman shifts of tagged cholesterols. Based on the molar concentration of the molecules (50 mM) and the solvent (9.7 M), the Raman cross section of C;C from A-Chol, PhA-Chol, and PhDY-Chol are 6 times, 15 times, and 88 times larger than the C5O band from the solvent, respectively. CN: cyano; A: alkyne; PhA: phenyl-alkyne; PhDY: phenyl-diyne; Chol: cholesterol. (c) SRS contrast versus concentration plot of PhDY-Chol solutions. 13% contrast was reached at 313 mM and 4% contrast was reached at 156 mM. Image acquisition speed: 200 ms per pixel. Data represents the mean 6 SEM in 3 measurements. $\ R ^ { 2 } = 0 . 9 9 6 .$ (d) SRS contrast versus concentration plot of PhDY-Chol solutions using chirped femtosecond lasers with spectral focusing approach. 14% contrast was reached at 31 mM. Image acquisition speed: 200 ms per pixel. Data represents the mean 6 SEM in 3 measurements. $\mathrm { R } ^ { 2 } = 0 . 9 8 0 .$ . Contrast was defined as $( \mathsf { S } - \mathsf { B } ) / \mathsf { B } .$ . S: SRS signal; B: background.

48 h before the assays were conducted. A-Chol was found to be toxic to the cells with $\mathrm { I C } _ { 5 0 }$ of 16 mM. Importantly, adding a phenyl group effectively reduced the cytotoxicity (Supplementary Fig. 3a). To directly visualize the toxic effect, we stained the cells with propidium iodide for late apoptosis and necrosis. Cells incubated with A-Chol showed reduced density and extensive apoptosis, whereas both PhA-Chol and PhDY-Chol caused minimum cell death (Supplementary Fig. 3b). This result presents another important role of the phenyl group, which is to reduce the toxicity caused by terminal alkyne. Based on the signal level and the severity of toxicity, we conclude that PhDY-Chol is the most suitable cholesterol analog for live cell imaging, and we used PhDY-Chol in subsequent experiments.

Membrane incorporation and esterification of PhDY-Chol in live cells. We chose CHO cells which are commonly used for cholesterol trafficking and metabolism studies40. To enhance cellular uptake of PhDY-Chol, the cells were pre-incubated in medium supplemented with lipoprotein-deficient serum to deplete medium cholesterol, after which the cells were incubated with 50 mM PhDY-Chol for 16 h. By tuning the laser beating frequency to be resonant with C;C vibration (2,254 cm21 ), SRL signals arose from PhDY-Chol. We also tuned the laser to be resonant with C-H vibration (2,885 cm21 ) and obtained signals from C–H-rich lipid structures, such as LDs.

To show the incorporation of PhDY-Chol into the plasma membrane, we performed spectral focusing SRS imaging of live CHO cells after treating with PhDY-Chol for 1 h with 6 ms per pixel speed. PhDY-Chol in the membrane was detected in the on-resonance image, and the contrast disappeared in the off-resonance image (Supplementary Fig. 4a). The membrane incorporation was confirmed by filipin staining of free cholesterol and Raman spectral analysis (Supplementary Fig. 4b and 4c). By focusing at the filipinstained membrane, we have obtained the Raman spectrum showing the C5C band from filipin (Supplementary Fig. 4d), the amide I band from protein, and the C;C band from the PhDY (Supplementary Fig. 4c). Inside live CHO cells, PhDY-Chol was colocalized with LDs found in the C–H vibrational region (Fig. 3a). This colocalization was confirmed by two-photon-excited fluorescence (TPEF) imaging and Raman spectral analysis of BODIPYstained LDs in fixed CHO cells. (Supplementary Fig. 5a and 5b). The Raman spectra of the BODIPY-labeled LDs showed 702 cm21 peak from cholesterol ring and the $\mathrm { C } { \equiv } { \mathrm { C } }$ band from the PhDY (Supplementary Fig. 5b), which further supports the localization of PhDY-Chol in LDs. Importantly, high imaging speed offered by SRS microscopy allowed real-time imaging of the trafficking of PhDY-Chol containing LDs within living cells (Supplementary Movie 1).

It is important to note that PhDY-Chol-rich structures inside the CHO cells could not be stained by filipin (Supplementary Fig. 4b), implicating that it is not in the free form. We hypothesize that PhDY-

![](images/76c72e49eff1271068455f2f3cbf8d00387fcd3c91829eda03b37dcc7d08bbd1.jpg)

b  
![](images/da669d655a6a5faad9fd6767ada563b35328490d5aaeee9cd83696cfcbd77bcc.jpg)

<details>
<summary>chemical</summary>

Chemical reaction diagram showing PhDY-Chol reacting with Acyl-CoA to form PhDY-cholesterol ester, with ACAT-1 as the inhibitor.
</details>

d  
![](images/8fb87e94b73d9c4e18a4623a8f2f2857005a03c7428c27f9ced683db66924c4d.jpg)

<details>
<summary>bar chart</summary>

| Group | BODIPY-Chol (Relative to control) | PhDY-Chol (Relative to control) |
|---|---|---|
| Control | 1.0 | 1.0 |
| + Avasimibe | 0.9 | 0.25* |
</details>

![](images/d1d27c5c1c277dd855919678ad5cee2d3eea94058c857f307c3249e70f033917.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing BODIPY-Chol expression in Control and +Avasimibe groups (no text or symbols present)
</details>

![](images/9faa15062a970573e5ddfe161befc8ee8f1b92fa0d78abe6bcda0a13e2ba46f5.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing red-stained cellular structures with two circular annotations (no text or symbols present)
</details>

![](images/f5cad31ce1a2fbc88673622cdbe2d2f6c459be7e5e67c1ac495d20a3fe3b01c8.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing merged red and yellow cellular structures with circular annotations (no text or symbols)
</details>

Figure 3 | SRS images of PhDY-Chol in live CHO cells and blockage of PhDY-Chol storage into LDs via ACAT-1 inhibition. (a) SRS images of live CHO cells treated with PhDY-Chol (50 mM) for 16 h. C;C vibrational mode at 2,254 $\mathrm { c m } ^ { - 1 }$ was used for PhDY-Chol, and C–H vibrational mode at 2,885 $\mathrm { c m } ^ { - 1 }$ was used for C–H-rich lipid structures. Lasers were also tuned away to 2,099 cm21 to show specificity of PhDY-Chol signal inside the cells. PhDY-Chol was found to accumulate in LDs (arrows). Image acquisition speed: 10 ms per pixel for $5 1 2 \times 5 1 2$ pixels. Scalar bar: 10 mm. (b) Schematic graph showing the hypothesis of PhDY-Chol metabolism inside the cells. ACAT-1: Acyl-CoA:cholesterol acyltransferase. (c) SRS images of PhDY-Chol in CHO cells and ACAT-1 inhibited CHO cells by avasimibe treatment. As shown in circles, PhDY-Chol was stored in LDs in CHO cells, but not in avasimibe treated CHO cells. Image acquisition speed: 100 ms per pixel for 400 3 400 pixels. Scalar bar: 10 mm. Intensity bars in (a) and (c) show the DI/I of the SRS image. (d) Quantification of PhDY-rich and BODIPY-rich LDs in CHO cells before and after ACAT-1 inhibition. The number of the LDs was normalized by the control group $( \mathbf { n } = 7 )$ . Error bars represent standard deviation. $\ast _ { : \mathrm { { p } } } < 0 . 0 5 .$ . (e) TPEF images of BODIPY-cholesterol and SRS images C–H-rich structures in CHO cells and ACAT-1 inhibited CHO cells. As shown in circles, BODIPY-cholesterol showed no difference between the two groups. Scalar bar: 10 mm.

Chol is converted into PhDY-cholesteryl ester, by ACAT-1, the enzyme responsible for cholesterol esterification8 (Fig. 3b). To confirm the esterification of PhDY-Chol, we inhibited ACAT with avasimibe for 24 h before addition of PhDY-Chol. After blocking cholesterol esterification, the amount of PhDY-Chol storage found in CHO cells significantly decreased (Fig. 3c). Although LDs were still visible, the amount of PhDY-Chol signal found inside LDs reduced by 4 times (Fig. 3d). ACAT-1 knockdown by shRNA was also conducted to specifically inhibit the enzyme. Similarly, we found decreased amount of PhDY-Chol in ACAT-1 knocked down CHO cells, and the amount of PhDY-Chol in LDs reduced significantly (Supplementary Fig. 6a). To determine where PhDY-Chol accumulates after ACAT-1 inhibition, we stained the cells with LysoTracker for lysosomes. Our result indicated that after ACAT-1 inhibition, PhDY-Chol partially located in lysosomes (Supplementary Fig. 6b). Collectively, these results show that PhDY-Chol can be transported into cells, converted into PhDY-cholesteryl ester by ACAT-1, and stored in LDs following the normal metabolic pathway of cho lesterol. To emphasize the physiological compatibility of our PhDY tag, we treated CHO cells with BODIPY-cholesterol. The amount of BODIPY-cholesterol incorporated into LDs did not change after ACAT-1 inhibition (Fig. 3d and 3e), indicating that BODIPY-cholesterol directly labels the LDs without metabolic conversion into cholesteryl ester. It is known that excess cholesterol inside cells is stored into LDs through cholesterol esterification by ACAT proteins8 . Therefore, PhDY-Chol reflects the intracellular cholesterol metabolism more faithfully compared to BODIPY-cholesterol.

Lysosomal accumulation and relocation to LDs in NP-C disease model. Next, we explored the potential of PhDY-Chol for studying cholesterol transport in NP-C disease, a disorder featured by abnormal cholesterol accumulation in late endosome/lysosome caused by mutation in NPC1 or 2 gene41. M12 cells, mutant CHO cells that contain a deletion of the NPC1 locus, were established as a cellular model of the NP-C disease42. By combining SRL imaging of

PhDY with TPEF imaging of filipin, we observed that, unlike wildtype CHO cells, the PhDY-Chol-rich structures were stained by filipin, indicating that these PhDY-Chol molecules were located in lysosomes. (Fig. 4a, Supplementary Fig. 7a and 7b). Moreover, we observed some filipin labeled structures that do not contain PhDY-Chol. This result is reasonable given that filipin has been shown to label other lipid molecules, such as glycosphingolipids24. As additional evidence, we incubated M12 cells with PhDY-Chol and stained the cells with LysoTracker. It was found that all PhDY-Cholrich areas were localized in LysoTracker-stained organelles (Supplementary Fig. 7c). Collectively, these results showed that PhDY-Chol selectively represents the lysosomal storage of cholesterol in the NP-C disease model.

We then treated the PhDY-Chol-labeled M12 cells with a cholesterol-mobilizing drug, hydroxypropyl b-cyclodextrin (HPbCD)43. This drug is known to mediate lysosomal escape of cholesterol, and promote storage of excess cholesterol into LDs44. After treating with HPbCD, the amount of PhDY-Chol in M12 cells decreased by half (Fig. 4b and c). Interestingly, we observed that some PhDY-Chol-rich areas were not labeled by filipin after HPbCD treatment (arrow heads in Fig. 4b). These areas likely represent PhDY-cholesteryl ester stored in LDs. To confirm this possibility, we stained the cells with BODIPY for localization of LDs. The result clearly showed that PhDY-Chol has moved into LDs after HPbCD treatment, and the number of PhDY-rich LDs increased significantly (Fig. 4d and 4e). Together, these data indicate that PhDY-Chol can be used as a reliable cholesterol analog to study cholesterol mobilization inside living cells.

Cholesterol uptake and storage in intestinal cells in C. elegans visualized by PhDY-Chol. Finally, to demonstrate the capability of monitoring cholesterol uptake and distribution in vivo, we used C. elegans as an animal model to study cholesterol uptake and storage. We fed N2 wildtype C. elegans with PhDY-Chol-labeled E. coli and imaged PhDY-Chol storage in the worms using our SRL microscope at speed of 40 ms per pixel. PhDY-Chol was found most abundantly in the intestinal cells inside the wildtype worms (upper panels in Fig. 5a). To confirm the uptake of PhDY-Chol by intestinal cells, we fed ChUP-1 mutant C. elegans, in which dietary cholesterol uptake is inhibited by ChUP-1 deletion45, with PhDY-Chol. We did not observe PhDY-Chol inside this strain (lower panels in Fig. 5a), which indicates that the PhDY tag did not affect the cholesterol uptake process. Then, we tuned the laser to be resonant with C–H vibration for lipid-rich LDs. Unlike CHO cells, the PhDY-Chol-rich compartments were found to be distinguished from LDs in wildtype worms (upper panels in Fig. 5a). To explore the nature of PhDY-

![](images/556d6a264fd87bde427e2f513832a06bfb48b1aaedbc561b710d94c01e29085b.jpg)

<details>
<summary>text_image</summary>

C≡C
M12
Filipin
Merge
Control
</details>

b  
![](images/a1facfec4ee516f3420387ad4e619b36ddb84546c5f9483eb8015822623ea023.jpg)

<details>
<summary>text_image</summary>

M12
+ HPβCD
0	2.6 x 10⁻⁶
0	99
</details>

c  
![](images/de38f3a83e28f5dc3c6165c8ca1cdf250e46d37fde39c57eaa046eab412ea971.jpg)

<details>
<summary>bar chart</summary>

| Group | PhDY-rich area fraction/cell (Relative to control) |
|---|---|
| Control | 1.0 |
| + HPβCD | 0.56 |
*
</details>

![](images/449e8b8d94662240f7deb49127f0c33cb087eb294664546055be1ca02b2ee245.jpg)

<details>
<summary>text_image</summary>

C≡C
BODIPY
Merge
M12
Control
+ HPβCD
0 2.6 x 10⁻⁶
0 99
</details>

e  
![](images/4cfbe0f1fbec3ecd3417ba18d98cca07951ab79f832df7dfd821741f04c83632.jpg)

<details>
<summary>bar chart</summary>

| Group | PhDY-rich LDs/cell |
|---|---|
| Control | 1.5 |
| + HPβCD | 7.0 |
**
</details>

Figure 4 Restored cholesterol transport in M12 cells treated with HPbCD. TPEF images of filipin and SRS images PhDY-Chol in (a) PhDY-Cholloaded M12 cells, and (b) the same cells treated with HPbCD (500 mM) for 30 h. Arrows indicate PhDY-rich area labeled by filipin before treatment (non-esterified PhDY-Chol), and arrow heads indicate PhDY-rich area not labeled by filipin after treatment (esterified PhDY-Chol). Green intensity bar shows the DI/I value of the SRS image; red intensity bar represents the relative intensity of fluorescence. Image acquisition speed: 100 ms per pixel for 400 3 400 pixels. Scalar bar: 10 mm. (c) Quantification of PhDY-rich area in the cells before and after HPbCD treatment (n 5 7). Error bars represent standard deviation. $\mathfrak { * } _ { : \mathrm { p } } < 0 . 0 5 . ( \mathrm { d } )$ TPEF images of BODIPY and SRS images of PhDY-Chol in M12 cells treated with or without HPbCD (500 mM) for 30 h. Arrow heads indicate LDs without PhDY-Chol before treatment, and arrows indicate LDs with PhDY-Chol after treatment. Green intensity bar shows the DI/I value of the SRS image; red intensity bar represents the relative intensity of fluorescence. Image acquisition speed: 100 ms per pixel for 400 3 400 pixels. Scalar bar: 10 mm. (e) Quantification of PhDY-rich LDs in the cells before and after HPbCD treatment (n 5 7). Error bars represent standard deviation. ${ } ^ { * * } \colon \mathfrak { p } < 0 . 0 0 5$ .

Chol-rich compartments found in our study, we used hjIs9 worms that contain GFP targeted to lysosome-related organelles (LROs) in intestinal cells46. Dual-modality SRS and TPEF imaging showed that PhDY-Chol is stored in the LROs (Fig. 5b). We further confirmed the cholesterol storage in intestinal LROs by combining TPEF imaging of GFP targeted LROs and Raman spectral analysis of hjIs9 worms fed with normal cholesterol (Supplementary Fig. 8). Raman spectrum of LROs showed peaks for sterol C5C bond at 1,667 cm21 and Fermi resonance between asymmetrical $\mathrm { C H } _ { 2 }$ vibrational modes at 2,875 cm21 , indicating the presence of cholesterol in this organelle. Collectively, these results suggest that dietary PhDY-Chol uptake is through a ChUP-1 mediated process, and unlike mammalian CHO cells, C. elegans stores cholesterol in LROs, but not in LDs in the intestine.

![](images/21d8b1f2e2701f5a82aa14da3cfe496263cf531cb1c8bd64e735d0241e460dd6.jpg)

<details>
<summary>text_image</summary>

a
C≡C
C-H
Merge
WT
ChUP-1 deleted
b
C≡C
C-H
Glo1-GFP
Glo1-GFP
C≡C
hjs9
</details>

Figure 5 | SRS imaging of PhDY-Chol visualizes compartments of cholesterol storage in live . (a) SRS images of live wildtype and ChUP-1 deleted C. elegans fed with PhDY-Chol (500 mM) for 3 days. Arrows indicate PhDY-rich particles in the intestine. Image acquisition speed: 40 ms per pixel for 400 3 400 pixels. Scalar bar: 10 mm. (b) TPEF and SRS images of live hjIs9 [ges-1p::glo-1::GFP 1 unc-119(1)] worm fed with PhDY-Chol (500 mM) for 3 days. Arrows indicate the PhDY-rich particles in LROs. Image acquisition speed: 40 ms per pixel for 400 3 400 pixels. Scalar bar: 10 mm.

## Discussion

In this study, we have developed a series of tagged cholesterols based on quantum chemistry calculations and chemical synthesis. By using PhDY to replace the aliphatic chain in cholesterol, we produced a cholesterol analog, PhDY-Chol, with a Raman signal that is two orders of magnitude stronger than the C5O group. By SRS imaging of live CHO cells, PhDY-Chol was found to be incorporated into the membrane, and converted to PhDY-cholesteryl ester for storage in LDs. With this cholesterol analog, we experimentally validated that after ACAT-1 inhibition, cholesterol partly accumulates in lysosomes. In live NPC1-deleted CHO cells, PhDY-Chol selectively represented lysosomal accumulation of cholesterol in untreated cells, and esterification and relocation to LDs after HPbCD treatment. Lastly, SRS imaging of PhDY-Chol in live C. elegans showed choles terol uptake by intestinal cells, and indicated LROs, but not LDs, as the cholesterol storage compartments in the intestine.

Essential parameters of a valid Raman tag include its amplitude of Raman scattering cross section, cytotoxicity, and biocompatibility. Although the C–D bond can be used to replace C–H bonds without changing the structures of the molecules, it gives relatively weak Raman intensities. Raman signal from alkyne bond is stronger than that from C–D bond by one order of magnitude27, and detection at hundreds of micromolar of alkyne-containing molecules by SRS microscopy was reported35,36. It should be noted that terminal alkyne is known to react with the cysteine residues in proteins47, which might induce cytotoxicity at micromolar concentrations. In our study, through rational design and synthesis of a PhDY tag, we increased the Raman scattering cross section by 15 times compared to the alkyne group, and 88 times compared to the endogenous C5O group. This enhancement is a result of conjugation of p-electrons among the two C;C bonds and the phenyl group. As a result, we have been able to detect ,30 mM of PhDY-Chol molecules (,1,800 molecules at excitation volume), and demonstrated SRS imaging of PhDY-Chol in single membrane at speed of 6 ms per pixel, and a realtime movie of PhDY-Chol containing LDs. Importantly, this design also shielded the activity of terminal alkyne and significantly reduced cytotoxicity. Moreover, PhDY-Chol structurally mimics cholesterol, using the same physiological process for cholesterol transport and metabolism inside cells. Cell membrane morphology did not alter when PhDY-Chol was supplemented at high concentrations when compared to the cells supplemented with the same concentrations of cholesterol (Supplementary Fig. 3). Moreover, the fluorescent property of pyrenedecanoic acid, a membrane fluidity indicator48, did not change after CHO cells were treated with 50 mM of PhDY-Chol or 50 mM of cholesterol for 16 h. These evaluations suggest that the membrane property of the cells was not significantly affected by addition of PhDY-Chol or cholesterol under our experimental conditions. We note that using the same strategy, other Raman tag molecules can be designed for sensitive and biocompatible probing of biomolecules in live cells.

The potential value of a Raman tag is also related to the detection sensitivity of SRS microscopy. One limitation comes from the cross phase modulation, which produces a background that reduces the contrast for the tag molecules. Although broadband femtosecond lasers provide high peak intensity to enhance the SRS signal32, they also increase the amplitude of the cross phase modulation. As shown in our study, this background can be reduced by 3 times using spectral focusing39. The spectral focusing approach also increases the spectral selectivity, reduces the photodamage, and provides opportunities to conduct hyperspectral SRS imaging49.

In this study, we compared BODIPY-cholesterol21 and PhDY-Chol. Our results show that PhDY-Chol is stored in LDs via esterification which can be blocked by ACAT-1 inhibition. In contrast, BODIPY-cholesterol labels LDs even after ACAT-1 inhibition. This result may be due to the strong hydrophobic interaction of BODIPY with LDs, and is consistent with previous studies showing that BODIPY-cholesterol is hardly esterified by ACAT-1 inside the cells21. These results demonstrate that PhDY-Chol, but not BODIPY-cholesterol, reflects the intracellular behavior of free cholesterol. We also showed that PhDY-Chol reflects the location of the cholesterol in real-time, unlike filipin staining, which requires fixation. Lastly, SRS microscopy utilizes chemical-bond vibrational signals for visualization. Thus, unlike fluorophores, the PhDY tag does not undergo bleaching (Supplementary Fig. 9), in contrast to BODIPY-cholesterol and DHE15 which is known to have a rapid photo-bleaching rate. Combining these unique properties, PhDY-Chol allows quantitative imaging of intracellular cholesterol, and repetitive observation of the same sample before and after treatment.

Our work opens new opportunities for mechanistic study of the NP-C disease, a fatal neurodegenerative disease that shows extensive lysosomal accumulation of cholesterol. Early detection methods and treatment strategies of this disease are still under development11. The involvement of lysosomal cholesterol accumulation to the neurodegeneration is still unclear50. Our in vitro study shows the cholesterol trafficking and metabolism in a cellular model. This can be extended to in vivo studies using suitable mouse models to understand the progression of the disease and impact of potential therapeutic strategies, especially in central nervous system.

C. elegans is an important model for genetic and chemical screening in many diseases51. It has been proposed that the intracellular sterol trafficking pathway might be conserved in nematodes52, making it a good model for exploring the genetics of fat storage and lipid metabolism53. However, lipid storage in C. elegans has been a debate because of limitations and controversies of the visualization tool for lipids54,55, especially cholesterol. Filipin labeling causes sterol extraction and some tissues were not accessible with staining20,56. Imaging fluorescent cholesterol in C. elegans is a challenge due to strong and spectrally overlapping autofluorescence from the worm57. Using label-free coherent anti-Stokes Raman scattering (CARS) microscopy, fat storage compartments in C. elegans were studied58,59. However, single color CARS microscopy based on the signal from C–H stretching vibrations cannot tell the compositions of the LDs, and so far it is not clear where the cholesterol is stored inside the worms. By combination of chemical synthesis of PhDY-Chol and real-time SRS imaging, we found evidences suggesting the choles terol storage in LROs. Label-free Raman spectral analysis was performed to validate the finding. Sterol uptake and transport in worms are still poorly understood45, and SRS imaging of PhDY-Chol opens an avenue to directly assess cholesterol uptake and transport for genome-wide RNA interference screening of cholesterol transport and storage genes in this animal model. Finally, our work also opens new opportunities to study cholesterol trafficking and metabolism in other animal models such as zebrafish and mice.

## Methods

Calculation of Raman intensity. All calculations were performed at the HF/6- 311G\* level of theory. Geometry optimizations, vibrational frequencies and Raman intensities are obtained in Q-Chem electronic structure package60. Localized polarizabilities are calculated in the GAMESS quantum chemistry software61.

Chemicals. 3b-hydroxy-D5 -cholenic acid was purchased from VWR. Lipoprotein deficient serum was purchased from Biomedical Technologies Inc. Cholesterol, avasimibe, and filipin complex were purchased from Sigma-Aldrich. BODIPY cholesterol was purchased from Avanti Polar Lipids, Inc. Propidium iodide, BODIPY, and LysoTracker were purchased from Life technologies.

Synthesis of Raman-tagged cholesterol. Detailed synthesis procedures and characterization of compounds are shown in Supplementary Information.

Solubilization of tagged cholesterol. To solubilize the tagged cholesterol molecules, the following procedure was used to prepare a stock solution of 10 mM cholesterol probe molecules. The appropriate amount of cholesterol probe powder was dissolved in 100% ethanol to make a 20 mM solution. The tube was vortexed and then sonicated in bath sonicator for 2 min. The same volume of DMSO was added into the tube, vortexed, and then sonicated in bath sonicator for 2 min. BODIPY-cholesterol was prepared with the same procedure. For SRS imaging and Raman spectral analysis of tagged cholesterol solutions, cholesterol probe molecules were prepared in cyclohexanone at 50 mM. The tube was vortexed and then sonicated in bath sonicator for 2 min. 1 mL of the solution was taken to prepare cover glass sample immediately before use.

Cell culture and PhDY-Chol treatment. CHO-K1 cells and M12 cells (mutant CHO K1 cells that contain a deletion of the NPC1 locus42) were kindly provided by Dr. Daniel Ory, and were grown in a monolayer at 37uC in 5% CO in DMEM/F-12 medium supplemented with 10% (vol/vol) FBS. To incubate cells with PhDY-Chol, cells were pre-incubated in DMEM/F-12 medium supplemented with 4.4% lipoprotein-deficient serum to deplete medium cholesterol for 16 h. The cells were then incubated with PhDY-Chol containing medium (DMEM/F-12 1 4.4% lipoprotein-deficient serum 150 mM PhDY-Chol) for 16 h to 24 h. Cells were rinsed with 13 PBS buffer three times before the next procedure.

Raman spectromicroscopy. The background of Raman spectrum was removed as described62. Each Raman spectrum of tagged cholesterol solution was acquired in 10 seconds, and each Raman spectrum of fluorescence stained cells was acquired in 30 seconds. On the same microscope, TPEF imaging was performed with 707 nm laser with 100 mW power. Backward-detected two-photon fluorescence signal was collected through a 425/40 nm or 522/40 nm band-pass filter for imaging filipin or BODIPY fluorescence, respectively.

SRS microscopy. SRS imaging was performed on a femtosecond SRL microscope, with the laser beating frequency tuned to the C;C vibration band at 2,254 cm21 , or to the C–H vibration band at 2,885 cm21 , as described previously32. The laser power at the specimen was maintained at 75 mW, and no cell or tissue damage was observed. For off-resonance, 2,099 cm21 was used. On the same microscope, TPEF imaging was performed with 843 nm laser with 30 mW power. Forward-detected two-photon fluorescence signal was collected through an appropriate band-pass filter for imaging filipin, BODIPY, or LysoTracker.

ACAT-1 inhibition. ACAT-1 inhibition was used to block cholesterol esterification either by adding a potent ACAT inhibitor, avasimibe, or by RNA interference with ACAT-1 shRNA plasmid. Avasimibe: Cells were pre-treated with avasimibe at a final concentration of 10 mM for 24 h. Then PhDY-Chol containing medium with 10 mM avasimibe was added into the cells and incubated for 24 h. RNA interference: RNA interference was employed to specifically inhibit endogenous ACAT-1. The ACAT-1 shRNA plasmid was purchased from Santa Cruz (sc-29624-SH). shRNA plasmid was transfected with LipofectamineH2000 (Invitrogen 11668030) as described in the manufacturer’s protocols.

HPbCD treatment. HPbCD was used as a drug treatment of NP-C disease. M12 cells were incubated with PhDY-Chol for 16 h as described above. Then cells were treated with 500 uM HPBCD for 30 h.

Cell-viability assay. CHO cells were grown in 96-well plates with density of 4000 cells per well. The next day, the cells were treated with each cholesterol probe at the indicated concentrations for 48 h. Cell-viability was measured with the MTT colorimetric assay (Sigma).

Propidium iodide staining. Propidium iodide was used to stain late apoptotic or necrotic cells. CHO cells were incubated with 30 mM of tagged cholesterol molecules for 24 h. The propidium iodide staining was performed following protocols provided by the manufacturer (Life Technologies).

Fluorescent staining of free cholesterol, LDs, and lysosomes. Filipin was used to stain free cholesterol. Cells were fixed with 10% formalin solution (Sigma) for 1 h at room temperature. 1.5 mg/mL glycine in PBS was used to quench the formalin by incubating the fixed cells for 10 minutes at room temperature. To stain the cells with filipin, working solution of 0.05 mg/mL of filipin in PBS/10% FBS was used to incubate cells for 2 h at room temperature. BODIPY was used to label LDs. Cells were incubated with 10 mg/mL of BODIPY for 30 minutes at room temperature. LysoTracker Yellow-HCK-123 was used to stain lysosomes following protocols provided by the manufacturer (Life Technologies). Cells were rinsed with PBS three times before TPEF imaging.

C. elegans strains. The N2 Bristol was used as wild-type strain. VC452 strain with chup-1(gk245) X genotype was used to study PhDY-Chol uptake. VS17 strain with hjIs9 [ges-1p::glo-1::GFP 1 unc-119(1)] genotype was used to study cholesterol storage in LROs.

PhDY-Chol uptake into C. elegans. PhDY-Chol uptake procedure was modified from a previously reported procedure20. Briefly, 500 mM of PhDY-Chol in DMSO was spread on the NGM plates seeded with an E. coli OP50 lawn and allowed to grow overnight at room temperature. C. elegans was then transferred to PhDY-Chol containing plates and grown for 3 days before SRS imaging.

Statistical analysis. To quantify PhDY-rich area, we first selected one cell and used ‘‘Threshold’’ function to select PhDY-rich cellular regions using ImageJ. Then, by using ‘‘Analyze Particles’’ function, the area fraction (%) of PhDY-rich region was obtained. To quantify PhDY-rich LDs, ‘‘Image Calculator’’ function in ImageJ was used to multiply SRS image of PhDY-Chol by TPEF image of BODIPY. Then, after using ‘‘Threshold’’ function to select PhDY-rich LDs, the number of PhDY-rich LDs was counted by ‘‘Analyze Particles’’ function. For each group, 7 cells were analyzed, and results were shown as mean 6 standard deviation (SD). Student’s t test was used for all the comparisons. p , 0.05 was considered statistically significant.

1. Yeagle, P. L. Cholesterol and the cell membrane. Biochim. Biophys. Acta 822, 267287 (1985).  
2. Lingwood, D. & Simons, K. Lipid rafts as a membrane-organizing principle. Science 327, 46–50 (2010).  
3. Wang, P. Y., Weng, J. & Anderson, R. G. OSBP is a cholesterol-regulated scaffolding protein in control of ERK 1/2 activation. Science 307, 1472–1476 (2005).  
4. Sheng, R. et al. Cholesterol modulates cell signaling and protein networking by specifically interacting with PDZ domain-containing scaffold proteins. Nat. Commun, 3, 1249 (2012)  
5. Mann, R. K. & Beachy, P. A. Cholesterol modification of proteins. Biochim. Biophys. Acta 1529, 188–202 (2000).  
6. Goldstein, J. L., DeBose-Boyd, R. A. & Brown, M. S. Protein sensors for membrane sterols. Cell 124, 35–46 (2006).  
7. Ikonen, E. Cellular cholesterol trafficking and compartmentalization. Nat. Rev. Mol. Cell Biol. 9, 125–138 (2008).  
8. Chang, T. Y., Chang, C. C. & Cheng, D. Acyl-coenzyme A: cholesterol acyltransferase. Annu. Rev. Biochem. 66, 613–638 (1997).  
9. Farese, R. V., Jr. & Walther, T. C. Lipid droplets finally get a little R-E-S-P-E-C-T. Cell 139, 855–860 (2009).  
10. Tabas, I. Consequences of cellular cholesterol accumulation: basic concepts and physiological implications. J. Clin. Invest. 110, 905911 (2002).  
11. Patterson, M. C. A riddle wrapped in a mystery: understanding Niemann-Pick disease, type C. Neurologist 9, 301–310 (2003).  
12. Nelson, E. R. et al. 27-Hydroxycholesterol links hypercholesterolemia and breast cancer pathophysiology. Science 342, 1094–1098 (2013).  
13. Yue, S. et al. Cholesteryl ester accumulation induced by PTEN loss and PI3K/AKT activation underlies human prostate cancer aggressiveness. Cell Metab. 19, 393406 (2014).  
14. Chang, T. Y., Chang, C. C., Ohgami, N. & Yamauchi, Y. Cholesterol sensing, trafficking, and esterification. Annu. Rev. Cell Dev. Biol. 22, 129–157 (2006).  
15. Gimpl, G. & Gehrig-Burger, K. Cholesterol reporter molecules. Biosci. Rep. 27, 335–358 (2007).  
16. Butler, J. D. et al. Progesterone blocks cholesterol translocation from lysosomes. J. Biol. Chem. 267, 23797–23805 (1992).  
17. MacLachlan, J., Wotherspoon, A. T., Ansell, R. O. & Brooks, C. J. Cholesterol oxidase: sources, physical properties and analytical applications. J. Steroid Biochem. Mol. Biol. 72, 169–195 (2000).  
18. Reid, P. C. et al. A novel cholesterol stain reveals early neuronal cholesterol accumulation in the Niemann-Pick type C1 mouse brain. J. Lipid Res. 45, 582–59 (2004).  
19. Mukherjee, S., Zha, X., Tabas, I. & Maxfield, F. R. Cholesterol distribution in living cells: fluorescence imaging using dehydroergosterol as a fluorescent cholesterol analog. Biophys. J. 75, 19151925 (1998)  
20. Matyash, V. et al. Distribution and transport of cholesterol in Caenorhabditis elegans. Mol. Biol. Cell 12, 1725–1736 (2001).  
21. Holtta-Vuori, M. et al. BODIPY-cholesterol: a new tool to visualize stero trafficking in living cells and organisms. Traffic 9, 1839–1849 (2008).  
22. Hulce, J. J. et al. Proteome-wide mapping of cholesterol-interacting proteins in mammalian cells. Nat. Methods 10, 259–264 (2013).  
23. Hofmann, K. et al. A novel alkyne cholesterol to trace cellular cholesterol metabolism and localization. J. Lipid Res. 55, 583591 (2014).  
24. Arthur, J. R., Heinecke, K. A. & Seyfried, T. N. Filipin recognizes both GM1 and cholesterol in GM1 gangliosidosis mouse brain. J. Lipid Res. 52, 1345–1351 (2011).  
25. Solanko, L. M. et al. Membrane orientation and lateral diffusion of BODIPYcholesterol as a function of probe structure. Biophys. J. 105, 20822092 (2013)  
26. Yamakoshi, H. et al. Imaging of EdU, an alkyne-tagged cell proliferation probe, by Raman microscopy. J. Am. Chem. Soc. 133, 6102–6105 (2011).  
27. Yamakoshi, H. et al. Alkyne-tag Raman imaging for visualization of mobile small molecules in live cells. J. Am. Chem. Soc. 134, 20681–20689 (2012).  
28. Pezacki, J. P. et al. Chemical contrast for imaging living systems: molecular vibrations drive CARS microscopy. Nat. Chem. Biol. 7, 137–145 (2011).  
29. Matthaus, C. et al. Noninvasive imaging of intracellular lipid metabolism in macrophages by Raman microscopy in combination with stable isotopic labeling. Anal. Chem. 84, 8549–8556 (2012).  
30. Cheng, J.-X. & Xie, X. S. Coherent Raman scattering microscopy (CRC Press, 2013).  
31. Xie, X. S., Yu, J. & Yang, W. Y. Living cells as test tubes. Science 312, 228–230 (2006).  
32. Zhang, D., Slipchenko, M. N. & Cheng, J. X. Highly sensitive vibrational imaging by femtosecond pulse stimulated Raman loss. J. Phys. Chem. Lett. 2, 1248–1253 (2011).  
33. Wei, L. et al. Vibrational imaging of newly synthesized proteins in live cells by stimulated Raman scattering microscopy. Proc. Natl. Acad. Sci. U. S. A. 110, 11226–11231 (2013).  
34. Bergner, G. et al. Quantitative detection of C-deuterated drugs by CARS microscopy and Raman microspectroscopy. Analyst 136, 3686–3693 (2011).  
35. Wei, L. et al. Live-cell imaging of alkyne-tagged small biomolecules by stimulated Raman scattering. Nat. Methods 4, 410–412 (2014).  
36. Hong, S. et al. Live-cell stimulated Raman scattering imaging of alkyne-tagged biomolecules. Angew. Chem. Int. Ed. Engl. 53, 5827–5831 (2014).  
37. Zhang, D., Wang, P., Slipchenko, M. N. & Cheng, J. X. Fast vibrational imaging of single cells and tissues by stimulated Raman scattering microscopy. Acc. Chem. Res. 47, 2282–2290 (2014).  
38. Lee, J. Y., Suh, S. B. & Kim, K. S. Polyenes vs polyynes: Efficient p-frame for nonlinear optical pathways. J. Chem. Phys. 112, 344–348 (2000).  
39. Hellerer, T., Enejder, A. M. K. & Zumbusch, A. Spectral focusing: High spectra resolution spectroscopy with broad-bandwidth laser pulses. Appl. Phys. Lett. 85, 25–27 (2004).  
40. Cadigan, K. M., Chang, C. C. & Chang, T. Y. Isolation of Chinese hamster ovary cell lines expressing human acyl-coenzyme A/cholesterol acyltransferase activity. J. Cell Biol. 108, 2201–2210 (1989).  
41. Carstea, E. D. et al. Niemann-Pick C1 disease gene: homology to mediators of cholesterol homeostasis. Science 277, 228–231 (1997).  
42. Millard, E. E. et al. Niemann-pick type C1 (NPC1) overexpression alters cellular cholesterol homeostasis. J. Biol. Chem. 275, 38445–38451 (2000).  
43. Liu, B. et al. Reversal of defective lysosomal transport in NPC disease ameliorates liver dysfunction and neurodegeneration in the npc1-/- mouse. Proc. Natl. Acad. Sci. U. S. A. 106, 2377–2382 (2009).  
44. Abi-Mosleh, L. et al. Cyclodextrin overcomes deficient lysosome-to-endoplasmic reticulum transport of cholesterol in Niemann-Pick type C cells. Proc. Natl. Acad. Sci. U. S. A. 106, 19316–19321 (2009).  
45. Valdes, V. J. et al. CUP-1 is a novel protein involved in dietary cholesterol uptake in Caenorhabditis elegans. PLoS One 7, e33962 (2012).  
46. Zhang, S. O. et al. Genetic and dietary regulation of lipid droplet expansion in Caenorhabditis elegans. Proc. Natl. Acad. Sci. U. S. A. 107, 4640–4645 (2010).  
47. Ekkebus, R. et al. On terminal alkynes that can react with active-site cysteine nucleophiles in proteases. J. Am. Chem. Soc. 135, 2867–2870 (2013).  
48. Dix, J. A. & Verkman, A. S. Pyrene eximer mapping in cultured fibroblasts by ratio imaging and time-resolved microscopy. Biochemistry 29, 1949–1953 (1990).  
49. Fu, D. et al. Hyperspectral imaging with stimulated Raman scattering by chirped femtosecond lasers. J. Phys. Chem. B 117, 4634–4640 (2013).  
50. Pfrieger, F. W. Cholesterol homeostasis and function in neurons of the centra neryous system. Cell. Mol. Life Sci. 60, 11581171 (2003),  
51. Kaletta, T. & Hengartner, M. O. Finding function in novel targets: C. elegans as a model organism. Nat. Rev. Drug Discov. 5, 387–398 (2006).  
52. Li, J. et al. NCR-1 and NCR-2, the C. elegans homologs of the human Niemann Pick type C1 disease protein, function upstream of DAF-9 in the dauer formation pathways. Development 131, 5741–5752 (2004).  
53. Ashrafi, K. et al. Genome-wide RNAi analysis of Caenorhabditis elegans fat regulatory genes. Nature 421, 268272 (2003).  
54. O’Rourke, E. J., Soukas, A. A., Carr, C. E. & Ruvkun, G. C. elegans Major Fats Are Stored in Vesicles Distinct from Lysosome-Related Organelles. Cell Metab. 10, 430–435 (2009).  
55. Mak, H. Y. Lipid droplets as fat storage organelles in Caenorhabditis elegans: Thematic Review Series: Lipid Droplet Synthesis and Metabolism: from Yeast to Man. J. Lipid Res. 53, 28–33 (2012).  
56. Merris. M. et al. Sterol effects and sites of sterol accumulation in Caenorhabditis elegans: developmental requirement for 4alpha-methyl sterols. J. Lipid Res. 44, 172–181 (2003).  
57. Wustner, D. et al. Selective visualization of fluorescent sterols in Caenorhabditis elegans by bleach-rate-based image segmentation. Traffic 11, 440–454 (2010).  
58. Le, T. T. et al. Label-free quantitative analysis of lipid metabolism in living Caenorhabditis elegans[S]. J. Lipid Res. 51, 672–677 (2010).  
59. Yen, K. et al. A comparative study of fat storage quantitation in nematode Caenorhabditis elegans using label and label-free methods. PLoS One 5, e12810 (2010).  
60. Shao, Y. et al. Advances in methods and algorithms in a modern quantum chemistry program package. Phys. Chem. Chem. Phys. 8, 3172–3191 (2006).  
61. Gordon, M. S. & Schmidt, M. W. in Theory and Applications of Computational Chemistry (eds Clifford E. Dykstra, Gernot Frenking, Kwang S. Kim, & Gustavo E. Scuseria) 1167–1189 (Elsevier, 2005).  
62. Slipchenko, M. N., Le, T. T., Chen, H. & Cheng, J. X. High-speed vibrational imaging and spectral analysis of lipid bodies by compound Raman microscopy. J. Phys. Chem. B 113, 7681–7686 (2009).

## Acknowledgments

We thank Dr. Daniel Ory at Washington University in St. Louis for providing CHO and M12 cell lines. We thank Chunrui Hu for the help with the experiments. VC452 strain was provided by the C. elegans Reverse Genetics Core Facility at UBC, which is part of the International C. elegans Gene Knockout Consortium, made from Moerman D, C. elegans Reverse Genetics Core, Vancouver, BC, Canada. Other C. elegans strains were provided by the CGC, which is funded by NIH Office of Research Infrastructure Programs (P40 OD010440). This research was supported by R21 CA182608 to J.X.C., and the Ara Parseghian Medical Research Foundation/Smith Family BReaK-Thru Fund to E.L.B. M.D thanks Purdue University for Startup support and NIH P30CA023168 for supporting shared NMR resources through Purdue Center for Cancer Research.

## Author contributions

M.D. and J.X.C. designed the research. D.Z. and L.V.S. performed and analyzed the quantum chemistry calculation. W.Z. and Y.Y. synthesized and analyzed the compounds. H.J.L. and D.Z. performed and analyzed the SRS experiments. B.L. developed dual-modality imaging. E.L.B. and K.K.B. provided the NP-C disease model and discussed the data. H.J.L. performed and analyzed in vitro and in vivo experiments. H.J.L., W.Z., M.D. and J.X.C. wrote the manuscript.

## Additional information

Supplementary information accompanies this paper at http://www.nature.com/ scientificreports

Competing financial interests: The authors declare no competing financial interests.

How to cite this article: Lee, H.J. et al. Assessing Cholesterol Storage in Live Cells and C. elegans by Stimulated Raman Scattering Imaging of Phenyl-Diyne Cholesterol. Sci. Rep. 5, 7930; DOI:10.1038/srep07930 (2015).

![](images/7f5adc1659c16a3438c96aa5c1f7ac157e0d7dac68d4184cb75190b37b5add68.jpg)

This work is licensed under a Creative Commons Attribution 4.0 Internationa License, The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder in order to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0