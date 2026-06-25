Review article

# Bond-selective photoacoustic imaging by converting molecular vibration into acoustic waves

![](images/ca7bcd943f49d6e4f649c58aae69e03390e4151ac95bea4120b4a5444caa1595.jpg)

CrossMark

Jie Hui $^{a}$ , Rui Li $^{b}$ , Evan H. Phillips $^{b}$ , Craig J. Goergen $^{b}$ , Michael Sturek $^{b,c}$ , Ji-Xin Cheng $^{b,c,d,e,*}$

$^{a}$ Department of Physics and Astronomy, Purdue University, West Lafayette, IN 47907, USA  
$^{b}$ Weldon School of Biomedical Engineering, Purdue University, West Lafayette, IN 47907, USA  
$^{c}$ Department of Cellular and Integrative Physiology, Indiana University School of Medicine, Indianapolis, IN 46202, USA  
$^{d}$ Department of Chemistry, Purdue University, West Lafayette, IN 47907, USA  
$^{e}$ Purdue Institute of Inflammation, Immunology and Infectious Diseases, West Lafayette, IN 47907, USA

## ARTICLE INFO

Article history:

Received 18 November 2015

Accepted 11 January 2016

Available online 1 February 2016

Keywords:

Overtone absorption

Photoacoustic microscopy

Photoacoustic tomography

Intravascular photoacoustic

Lipid

Atherosclerosis

Tumor margin

## ABSTRACT

The quantized vibration of chemical bonds provides a way of detecting specific molecules in a complex tissue environment. Unlike pure optical methods, for which imaging depth is limited to a few hundred micrometers by significant optical scattering, photoacoustic detection of vibrational absorption breaks through the optical diffusion limit by taking advantage of diffused photons and weak acoustic scattering. Key features of this method include both high scalability of imaging depth from a few millimeters to a few centimeters and chemical bond selectivity as a novel contrast mechanism for photoacoustic imaging. Its biomedical applications spans detection of white matter loss and regeneration, assessment of breast tumor margins, and diagnosis of vulnerable atherosclerotic plaques. This review provides an overview of the recent advances made in vibration-based photoacoustic imaging and various biomedical applications enabled by this new technology.

© 2016 The Authors. Published by Elsevier GmbH. This is an open access article under the CC BY license

(http://creativecommons.org/licenses/by/4.0/).

## Contents

1. Introduction 12  
2. Vibrational absorption as a photoacoustic contrast mechanism 12

2.1. Photoacoustic signal generation based on molecular overtone absorption 12  
2.2. New optical windows for photoacoustic imaging 13

3. Applications through vibration-based photoacoustic microscopy 15

3.1. Mapping lipid bodies in Drosophila 3rd-instar larva 15  
3.2. Mapping intramuscular fat 15  
3.3. Mapping white matter loss and regeneration 16

4. Applications through vibration-based photoacoustic tomography 16

4.1. Imaging a model of carotid atherosclerosis 16  
4.2. Imaging peripheral nerves 16  
4.3. Assessing breast tumor margins 16

5. Intravascular photoacoustic imaging of lipid-laden plaques 17

5.1. Imaging lipid-laden atherosclerotic plaques 17  
5.2. High-speed laser sources 18

6. Discussion 18

Conflict of interest 19

Acknowledgements 19

References 19

## 1. Introduction

Molecular vibration is the basis of numerous microscopy approaches and enables the detection of specific molecules within cells and tissues. These approaches include Raman scattering, infrared absorption, and near-infrared (NIR) absorption, which have been widely used for chemical imaging in biomedicine $[1-3]$ . Similarly, nonlinear vibrational methods, such as coherent anti-Stokes Raman scattering $[4,5]$ and stimulated Raman scattering $[6]$ microscopies, have enabled new discoveries in biology $[7]$ on account of their high sensitivity and 3D spatial resolution. However, all these approaches have limited imaging depth on the order of a few hundred micrometers due to significant optical scattering in biological tissue. Thus, their potential applications at the organ level in vivo and in clinical settings are restricted.

A deep-tissue imaging modality able to maintain both high chemical selectivity and spatial resolution would certainly satisfy the functional requirements for many diagnostic applications in biomedicine. A promising approach is the development of photoacoustic (PA) imaging platforms, which combine optical excitation with acoustic detection. With this approach, the imaging depth is significantly improved, as acoustic scattering by biological tissue ( $\sim1.2\times10^{-3}$ mm $^{-1}$ in human skin at 5 MHz) [8] is more than three orders of magnitude weaker than optical scattering ( $\sim10$ mm $^{-1}$ in human skin at 700 nm) [9]. Unlike nonlinear optical microscopy that relies on tightly focused ballistic photons, the diffused photons contribute equally to the generation of PA signal and thus further enhance the penetration depth. Over the past decade, researchers have developed various PA imaging platforms, including photoacoustic microscopy (PAM) [10,11], photoacoustic tomography (PAT) [10,12,13], photoacoustic endoscopy (PAE) [14,15], and intravascular photoacoustic (IVPA) imaging [16]. Many excellent review articles provide comprehensive insight into different aspects of the imaging technology [17–19], applicable contrast agents [20–22], and a variety of biomedical applications [23–26]. In most of the aforementioned applications, the PA signal comes from the electronic absorption of endogenous tissue pigments, such as hemoglobin and melanin, or from exogenous contrast agents, such as nanoparticles and dyes.

Molecular vibrational transitions in biological tissue have recently been demonstrated as a novel contrast mechanism for PA imaging. It describes the periodic motion of atoms in a molecule with typical frequencies ranging from $10^{12}$ to $10^{14}$ Hz. The molecular population in the ith vibrationally excited state relative to the ground state follows the Boltzmann's distribution law as $N_{i}/N_{0} = \exp(-\Delta E/kT)$ , where $\Delta E$ is the energy gap, T is the temperature, and k is the Boltzmann constant. Thus, the Boltzmann distribution describes how the thermal energy is stored in molecules. When the incident photon energy matches the transition frequency between the ground state and a vibrationally excited state, the molecule absorbs the photon and jumps to the excited state. During subsequent relaxation of the excited molecule to the ground state, the thermal energy is converted into acoustic waves detectable by an ultrasound transducer.

The fundamental vibrational transitions in the mid-infrared wavelength region have been previously exploited for PA detection of glucose in tissues $[27]$ . Nevertheless, this approach is limited in detecting molecules only tens of micrometers under the skin, where strong water absorption in the mid-infrared region predominates. Vibrational absorption with minimal water absorption can occur in two ways. One is through the stimulated Raman process and the other is through overtone transition. In stimulated Raman scattering, the energy difference between the visible or NIR pump and Stokes fields is transferred to the molecule to induce a fundamental vibrational transition. The concept of stimulated Raman-based PA imaging has been previously demonstrated [28,29]. However, because stimulated Raman scattering is a nonlinear optical process relying on ballistic photons under a tight focusing condition, this approach is not suitable for deep-tissue imaging. The overtone transition is based on the anharmonicity of chemical bond vibrations. Taking the C—H bond as an example, the first, second, and third overtone transitions occur at around 1.7 $\mu$ m, 1.2 $\mu$ m, and 920 nm, respectively, where water absorption is locally minimized. Since C—H bonds are one of the most abundant chemical bonds in biological molecules including lipids and proteins, photoacoustic detection of C—H bond overtone absorption offers an elegant platform for mapping the chemical content of tissue with penetration depths up to a few centimeters.

In the following sections, we introduce the mechanism for vibration-based PA signal generation. Then, applications of vibration-based PA imaging in forms of microscopy, tomography, and intravascular catheter will be reviewed, followed by a discussion of the improvements needed to overcome technical challenges that limit translation of these imaging modalities to the clinic.

## 2. Vibrational absorption as a photoacoustic contrast mechanism

## 2.1. Photoacoustic signal generation based on molecular overtone absorption

Vibration-based PA signals arise from the molecular overtone transitions and combinational band absorptions, which are allowed by anharmonicity of chemical bond vibration. According to the anharmonicity theory, the transition frequency for an overtone band has the following relation with the fundamental frequency, $\Omega_{n}=\Omega_{0}n-\chi\Omega_{0}(n+n^{2})$ , where $\Omega_{0}$ is the transition frequency of fundamental vibration, $\chi$ is the anharmonicity constant, and $n=2,3\ldots$ representing the first, second, and subsequent overtones. When the frequency of an incident pulsed laser matches the transition frequency of an overtone, the energy of the incident photons is absorbed and then induces a local rise in temperature. When both thermal and stress confinements are satisfied [30], the accumulated heat is subsequently released through a thermal-elastic expansion in tissue, which generates acoustic waves detectable by an ultrasound transducer. Fig. 1 depicts this process for PA signal generation based on first and second overtone transitions. The generated signal contains depth-resolved information of absorbers on which the image reconstruction is grounded. Compared to diffuse optical tomography, the integration of NIR spectroscopy with ultrasound detection eliminates the scattering background.

![](images/257de1e9360a39d521b5c6af195f64a992bdf2c2ce695cf1e0a974020b4b4c10.jpg)

<details>
<summary>text_image</summary>

Pulsed
NIR
laser
Chemical
bond
Ultrasound
waves
v=3
v=2
v=1
v=0
Ω₁
Ω₂
Overtone
absorption
</details>

Fig. 1. Schematic of vibration-based PA signal generation and the 1st and 2nd overtone absorption of a molecule. $\nu$ denotes the vibrational energy level; NIR demotes near infrared.

Through conversion of molecular vibration into acoustic waves, vibration-based PA imaging enables the visualization of different molecules and chemical components in biological tissue. Thus far, $CH_{2}$ -rich lipids [31–36], $CH_{3}$ -rich collagen [33], O—H bond-rich water [37], nerve [38,39], intramuscular fat [34,40], and neural white matter [41] have all been investigated. Particularly, the detection of overtone absorption of C—H bonds has recently drawn attention [42–48], since C—H bonds are highly concentrated in certain types of biological components, such as lipid and collagen. The presence of these molecules or components is directly related to several clinically relevant diseases, including atherosclerosis and cancers.

## 2.2. New optical windows for photoacoustic imaging

Using vibrational absorption, researchers have conducted PA spectroscopic studies of various molecules in biological specimens $[31,34,35,49]$ . These efforts were aimed at identifying suitable spectral windows to visualize different biological components, as well as differentiate them based on their vibrational spectral signatures. As shown in Fig. 2a, two new optical windows have been identified for bond-selective photoacoustic imaging (highlighted in blue between 1100–1300 nm and 1650–1850 nm), where the absorption coefficient of C—H bond-rich specimens is maximized and water absorption is locally minimized. The electronic absorption of hemoglobin $[50]$ is dominant in the visible to NIR wavelength range (i.e., 400 nm to 1.1 $\mu$ m) and it overwhelms the third- and higher-order C—H overtone transitions in the same range. For longer wavelengths in the range of 1.1–2.0 $\mu$ m, the optical absorption from hemoglobin has been significantly reduced. In particular, in the first optical window, the hemoglobin absorption [50] is close to one order of magnitude smaller than lipid absorption. The whole blood in the second optical window (1650–1850 nm) exhibits almost the same spectrum as pure water [50], the major content of blood [51–53]. Although the absorption coefficient of lipid [54,55] is 1–2 time larger than that of water in both optical windows, the fat constituent in tissue provides much higher contrast than water in vibration-based PA imaging. This observed phenomenon in PA imaging experiments can be explained by the following theoretical prediction and quantitative analysis.

Table 1 Absorption coefficient and Gruneisen parameter of fat and water at 1.2 and 1.7 micron.

<table><tr><td>Tissue constituent</td><td>Tissue parameter</td><td>1210 nm</td><td>1730 nm</td><td>Ref.</td></tr><tr><td rowspan="2">Fat</td><td> $\mu_{\text{a}}$  (cm $^{-1}$ )</td><td>1.65</td><td>10.5</td><td>[54]</td></tr><tr><td> $\Gamma$ </td><td>0.7–0.9</td><td>0.7–0.9</td><td>[56]</td></tr><tr><td rowspan="2">Water</td><td> $\mu_{\text{a}}$  (cm $^{-1}$ )</td><td>1.00</td><td>5.63</td><td>[53]</td></tr><tr><td> $\Gamma$ </td><td>0.12</td><td>0.12</td><td>[9]</td></tr></table>

Theoretically, the initial PA signal amplitude is described by $p_{0} = \xi \Gamma \mu_{a} F$ , where $\xi$ is a constant related to the imaging system, $\Gamma$ is the Gruneisen parameter of tissue, $\mu_{a}$ is the absorption coefficient of tissue, and F is the local light fluence. The Gruneisen parameter can be further expressed as $\Gamma = \beta \nu_{s}^{2} / C_{p}$ , where $\beta$ is the isobaric volume expansion coefficient, $\nu_{s}$ is the acoustic speed, and $C_{p}$ is the specific heat. In the equation, only $\Gamma$ and $\mu_{a}$ are dependent on absorbers in tissue. Thus, the vibration-based PA contrast of fat versus water can be expressed as $p_{0\_fat} / p_{0\_water} = (\mu_{a} \Gamma)_{\text{fat}} / (\mu_{a} \Gamma)_{\text{water}}$ . Based on the Gruneisen parameter and absorption coefficient of fat and water listed in Table 1 [9,54,56], the PA contrast of fat versus water is 9.6–12.4 and 10.9–14.0 at 1210 and 1730 nm, respectively. These parameters make vibration-based PA imaging a valid platform for selective mapping of fat or lipids in a complex tissue environment. Based on the same parameters, the fat signal amplitude at 1730 nm is 6.4 time of that at 1210 nm, largely due to the stronger absorption of lipid at 1730 nm.

![](images/97b77a4bba73ce9d1f5a073ec76a8433750fcea446e6883a2bb4a200501c99db.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | HbO₂ Absorption coefficient (cm⁻¹) | Hb Absorption coefficient (cm⁻¹) | Water Absorption coefficient (cm⁻¹) | Lipid Absorption coefficient (cm⁻¹) |
| --------------- | ---------------------------------- | -------------------------------- | ---------------------------------- | ---------------------------------- |
| 400             | ~10³                               | ~10³                             | ~10⁻²                              | ~10⁻²                              |
| 600             | ~10²                               | ~10²                             | ~10⁻³                              | ~10⁻³                              |
| 800             | ~10¹                               | ~10¹                             | ~10⁻²                              | ~10⁻²                              |
| 1000            | ~10⁰                               | ~10⁰                             | ~10⁻¹                              | ~10⁻¹                              |
| 1200            | ~10⁻¹                              | ~10⁻¹                            | ~10⁰                               | ~10⁰                               |
| 1400            | ~10⁻²                              | ~10⁻²                            | ~10¹                               | ~10⁰                               |
| 1600            | ~10⁻³                              | ~10⁻³                            | ~10¹                               | ~10⁰                               |
| 1800            | ~10⁻⁴                              | ~10⁻⁴                            | ~10²                               | ~10⁰                               |
| 2000            | ~10⁻⁴                              | ~10⁻⁴                            | ~10²                               | ~10⁰                               |
</details>

![](images/a13a88800a7f3b35c8620590f22babfd9e1767103c694a007b66dd33c5694a45.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Water layer thickness: 1.2 mm | Water layer thickness: 1.6 mm | Water layer thickness: 1.9 mm | Water layer thickness: 2.6 mm | Water layer thickness: 2.9 mm |
| --------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| 1100            | ~0                            | ~0                            | ~0                            | ~0                            | ~0                            |
| 1150            | ~0                            | ~0                            | ~0                            | ~0                            | ~0                            |
| 1200            | ~2                            | ~2                            | ~2                            | ~2                            | ~2                            |
| 1250            | ~3                            | ~3                            | ~3                            | ~3                            | ~3                            |
| 1300            | ~4                            | ~4                            | ~4                            | ~4                            | ~4                            |
| 1350            | ~5                            | ~5                            | ~5                            | ~5                            | ~5                            |
| 1400            | ~6                            | ~6                            | ~6                            | ~6                            | ~6                            |
| 1450            | ~7                            | ~7                            | ~7                            | ~7                            | ~7                            |
| 1500            | ~8                            | ~8                            | ~8                            | ~8                            | ~8                            |
| 1550            | ~9                            | ~9                            | ~9                            | ~9                            | ~9                            |
| 1600            | ~10                           | ~10                           | ~10                           | ~10                           | ~10                           |
| 1650            | ~11                           | ~11                           | ~11                           | ~11                           | ~11                           |
| 1700            | ~12                           | ~12                           | ~12                           | ~12                           | ~12                           |
| 1750            | ~13                           | ~13                           | ~13                           | ~13                           | ~13                           |
| 1800            | ~14                           | ~14                           | ~14                           | ~14                           | ~14                           |
</details>

![](images/24b548716519e1bb9266a0ac3728355265bd7b73094f02f4e6d50ff11c4c3634.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Polyethylene film | Trimethylpentane | Water | Deuterium oxide |
|---|---|---|---|---|
| 1100 | ~0 | ~0 | ~0 | ~0 |
| 1200 | ~5 | ~5 | ~0 | ~0 |
| 1300 | ~0 | ~0 | ~0 | ~0 |
| 1400 | ~0 | ~0 | ~5 | ~0 |
| 1500 | ~0 | ~0 | ~5 | ~0 |
| 1600 | ~0 | ~0 | ~0 | ~0 |
| 1700 | ~35 | ~25 | ~0 | ~0 |
| 1800 | ~25 | ~20 | ~35 | ~2 |
| 1900 | ~10 | ~5 | ~45 | ~5 |
| 2000 | ~5 | ~5 | ~5 | ~5 |
</details>

Fig. 2. Two spectral windows for vibration-based PA imaging. (a) Optical absorption spectra of water (from Ref. [53]), lipid (from Refs. [54,55]), oxygenated $(\mathrm{HbO}_2)$ and deoxygenated (Hb) (from Ref. [50]) showing that the first optical window lies between 1.1 and $1.3\mu \mathrm{m}$ and the second window lies between 1.65 and $1.85\mu \mathrm{m}$ . (b) Vibration-based PA spectra of different chemical bonds or groups with absorption band assignments. $\nu_{\mathrm{s}}$ and $\nu_{\mathrm{a}}$ denote symmetric stretching and anti-symmetric stretching of chemical bond, respectively. (b) Vibration-based PA spectra of a C—H bond-rich sample (polyethylene film) with a varying water layer thickness. Adapted with permission from Ref. [34] (b, c).

Detailed analysis of the PA spectra of C—H, O—H, and O—D bonds further verified these two optical windows [57]. Fig. 2b shows the PA spectra of polyethylene film, trimethylpentane, water, and deuterium oxide. These spectra have contributions from the absorption profiles of methylene groups (CH₂), methyl groups (CH₃), O—H, and O—D bonds, respectively. According to the spectrum of polyethylene film, the peak at ∼1210 nm comes from the second overtone transition of the symmetric stretching of CH₂ [58]. The broad peak located from 1350 to 1500 nm is attributed to the combinational band of symmetric stretching and bending of CH₂. The two primary peaks at ∼1.7 μm are thought to be the first overtone of CH₂ [58], which are caused by the anti-symmetric stretching and symmetric stretching, respectively [58]. For trimethylpentane, the 1195 nm peak corresponds to the second overtone transition of CH₃ symmetric stretching [58]. The combinational band has a main peak at ∼1380 nm [58]. The primary peak at ∼1700 nm is thought to be the first overtone of anti-symmetric stretching of CH₃ [58]. Although O—H bonds have combinational bands at $\sim$ 1450 and $\sim$ 1950 nm, respectively, its absorption is locally minimal in the first and second overtone windows of C—H bonds. Due to the heavier mass of deuterium, the prominent overtone and combinational bands of $D_{2}O$ have their corresponding peaks at longer wavelengths. Thus, it has been widely used as an acoustic coupling medium for vibration-based PA imaging [34,57].

As shown in Fig. 2c, a PA spectroscopic study of polyethylene film with a varying water layer thickness suggests that the second overtone of C—H bonds is peaked at $\sim1.2\mu m$ , while the first overtone corresponds to the peak at $\sim1.7\mu m$ [34]. Compared with $1.2\mu m$ excitation, $1.7\mu m$ excitation produces a $\sim6.3$ times stronger PA signal in the absence of water [34], which is consistent with aforementioned theoretical calculation. The signal amplitude drops with the thickness of the water layer and has the same level as $1.2\mu m$ excitation when the water layer thickness reaches 3–4 mm. Thus, a $1.7\mu m$ wavelength is favorable for intravascular photoacoustic imaging considering the relatively large absorption coefficient of the first overtone and the diminished optical scattering caused by blood at longer wavelengths [36,47,52,57]. The second overtone however is suitable for a tomographic configuration that requires larger penetration depths due to smaller water absorption at $1.2\mu m$ [59]. These spectral signatures were utilized for different biomedical applications, as reviewed below.

![](images/fdeae6743dcf0108623d244d90315d88ae6a592d55980f60f727261ec51a93a9.jpg)  
Fig. 3. A PAM system and enabled representative applications enabled in the new optical windows. (a) Schematic of a typical PAM system. T, ultrasound transducer. (b) 3D image of lipid bodies in Drosophila 3-instar Larva at $\sim$ 1200 nm. (c) Image of intramuscular fat at 1197 nm performed with a Raman laser. (d) Image of white matter in a normal rat spinal cord at 1730 nm showing the contrast difference between white matter and gray matter. Red arrows indicate the dorsolateral surface of the cord above dorsal horn. Adapted with permission from Ref. [31] (a, b), Ref. [40] (c), and Ref. [41] (d).

## 3. Applications through vibration-based photoacoustic microscopy

Based on its high spatial resolution, deep penetration depth, and rich optical absorption contrast, PAM has been used extensively and enabled new discoveries in biology and medicine. Using vibrational absorption, new applications are explored through PAM in the relevant optical windows. In a typical PAM setup, an inverted microscope is employed to direct the excitation light (Fig. 3a) which can be generated by Nd:YAG pumped optical parametric oscillator (OPO) [31,38,60] or a Raman laser [40]. An achromatic doublet lens or objective is applied to focus the laser light into a sample. A focused ultrasonic transducer records the time-resolved PA signal from the acoustic focal zone. According to the time of flight, each laser pulse can be used to generate an A-line. By raster scanning the sample in the $X - Y$ direction, a three-dimensional image can be acquired.

## 3.1. Mapping lipid bodies in Drosophila 3rd-instar larva

One important application for PAM in the new optical windows is to map the lipid bodies in Drosophila 3rd-instar Larva.

Drosophila melanogaster is one of the genetically best-known and widely used model organisms for genetic, behavioral, metabolic, and autophagic studies $[61–63]$ . Since lipids have strong optical absorption due to the second overtone transition of the C—H bond, Wang et al. performed 3D imaging of lipid body of a whole 3rd-star larva in vivo (Fig. 3b). The imaging result shows that lipid storage is mainly distributed along the anterior-posterior and the ventral-dorsal axis. This demonstrated capability of label-free visualization of adipose tissues in Drosophila is important for the rapid determination of phenotype, which will decrease the time required to conduct genetic screens for targets of fat metabolism and autophagy in this model organism $[64,65]$ .

## 3.2. Mapping intramuscular fat

Intramuscular lipids are associated with insulin resistance, which is related to a range of metabolic disorders including type 2 diabetes, obesity, and cardiovascular diseases [66,67]. However, the assessment of intramuscular fat is difficult since current deep-tissue imaging modalities cannot provide chemical contrast. Li et al. reported the feasibility of performing intramuscular fat mapping with a $\mathrm{Ba(NO_3)_2}$ crystal-based Raman laser [40]. The

a  
![](images/6b8dcd51536a953cfb0d8c0c450a172fb26ffc017f4a33ae3e628b835380aacc.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Delay generator"] --> B["Trigger"]
  C["Function generator"] --> D["Trigger"]
  E["Ultrasound machine"] --> F["Signal"]
  G["Nd:YAG pumped OPO"] --> H["Fiber bundle"]
  H --> I["US transducer"]
  I --> J["Silver mirror"]
  J --> K["Trigger"]
    style A fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style E fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style D fill:#ccf,stroke:#333
    style F fill:#ccf,stroke:#333
    style H fill:#ccf,stroke:#333
    style I fill:#ccf,stroke:#333
    style J fill:#ccf,stroke:#333
    style K fill:#ccf,stroke:#333
```
</details>

b

![](images/998d447dfba8833b55c60722d6d7d8fb97fd3793b37442d22f1c9bc90f66bd99.jpg)

<details>
<summary>text_image</summary>

Blood
4 mm
Fat
z
x
</details>

C  
![](images/f575ae7cf40332773b4ed3456fa89cf1dce0ccb38c516126fe0cdd5bf8f6fd5d.jpg)

<details>
<summary>text_image</summary>

Nerve
2 mm
Blood
z
x
</details>

d  
![](images/49c6a1e62af9181ebba5a8cb8a11ec4e73b4a32c8683930c5dc1b64de68d9050.jpg)

<details>
<summary>text_image</summary>

Blood
4 mm
Fat
z
x
</details>

Fig. 4. A PAT system and enabled representative applications enabled in the new optical windows. (a) Schematic of a typical PAT system. OPO, optical parametrical oscillator; US, ultrasound. (b) Images of modeled atherosclerotic carotid artery with contrast from lipid and blood. (c) Images of mouse peripheral nerve with contrast from fat and blood. (d) Image of breast tumor margin with contrast from fat and blood. Red oval indicates a normal tissue area with fat and scattered fibrous tissue; yellow oval indicates angiogenesis and invasive tumor with scattered fat tissue; blue oval indicates tumor with dense fibrous tissue. Adapted with permission from Ref. [90] (a, d), Ref. [78] (b), and Ref. [39] (c).

Raman laser provided an output with wavelength of 1197 nm. The signal from fat at 1197 nm is strong and the contrast nearly disappeared at 1064 nm, which indicates a strong absorption at 1197 nm due to the second overtone transition of C—H bond. The muscle sample was also imaged in three dimensions with an imaging depth of 3 mm, where the fat structure was clearly reflected (Fig. 3c). This result shows the promise of using this technique for quantitative measurement of intramuscular fat accumulation in metabolic disorders.

## 3.3. Mapping white matter loss and regeneration

Each year, approximately 12,000 new cases of spinal cord injury are diagnosed in the U.S., causing tetraplegia or paraplegia. White matter loss is thought to be a critical event after spinal cord injury. Traditionally, such degeneration is measured by histological and histochemical approaches [68]. However, real-time imaging is not feasible and artifacts are often introduced during histological processing. Wu et al. used PAM with $1730\mathrm{nm}$ excitation to assess white matter loss after a contusive spinal cord injury in adult rats [41]. Owing to the abundance of $\mathrm{CH}_2$ groups in the myelin sheath, white matter in the spinal cord can be easily visualized (Fig. 3d). From the cross-sectional image, contrast from white matter is $\sim 2.5$ times higher compared with grey matter. The absorption difference can be used to examine the morphology of white matter and changes in injured spinal cords. This study suggests that PAM based on first overtone transition of C—H bond could be potentially used to assess white matter loss during spinal cord injury and repair.

## 4. Applications through vibration-based photoacoustic tomography

By taking advantage of signal generation from diffused photons, PAT penetrates deeper than PAM and expands the imaging scale from the cell and tissue to whole organ level $[13]$ . The high scalability of PAT is achieved through a trade-off in spatial resolution for improved imaging depth. Moreover, the imaging scale can vary with the specific needs of PAT applications. Current applications for PAT include lymphatic $[69]$ and sentinel lymph node $[70,71]$ mapping, superficial $[72]$ and deep $[73]$ vessel mapping, and tumor imaging $[74,75]$ . The key advantages of this technique are noninvasiveness, superior depth penetration, and chemical-selectivity without the need for exogenous agents. For superior penetration depth, the experimental set-up requires integration of a high power laser with a low-frequency ultrasound array. Fig. 4a shows a typical PAT system $[39]$ . Briefly, a customized OPO laser (NT352C, EKSPLA) generating a 10 Hz, 5 ns pulse train with wavelength tunable from 670 to 2300 nm was used as the light excitation source. An optical fiber bundle delivers the light to tissue through two rectangular distal terminals adjacent to an arrayed ultrasound transducer with center frequency of 21 MHz (MS250, FUJIFILM VisualSonics). The generated PA signal is then acquired and reconstructed as two-dimensional or three-dimensional tomographic images using the ultrasound system. Below we describe a range of applications using molecular overtone absorption for tomographic imaging of lipid-associated diseases.

## 4.1. Imaging a model of carotid atherosclerosis

Carotid artery atherosclerosis is a common underlying cause of ischemic stroke $[76,77]$ . Noninvasive imaging and quantification of the compositional changes within the arterial wall is essential for disease diagnosis. Current imaging modalities are limited by the lack of compositional contrast, inability to detect of non-flow-limiting lesions, and inadequate accessibility to patients (like magnetic resonance imaging). However, modified multispectral

PAT has great potential for serving as a point-of-care device for early diagnosis of carotid artery disease in the clinic. Hui et al. tested this system to image ex vivo atherosclerotic human femoral arteries and tissue-mimicking phantoms [78]. We placed a 45-degree polished fiber-optic probe and a 21 MHz linear array transducer with 256 elements on opposite sides of the sample with a thick piece of chicken breast in order to mimic the in vivo conditions of carotid artery imaging through transesophageal excitation and external acoustic detection. Chemical maps of the blood and lipid in the lipid-laden vessel and fatty chicken breast were generated as shown in Fig. 4b.

Furthermore, for the tissue-mimicking phantom experiment, a piece of chicken breast was added between the excitation source and a polyethylene tube in order to analyze the signal-to-noise ratio and imaging depth in this set-up. An imaging depth of about 2 cm was achievable in this scenario while retaining chemical selectivity around 1210 nm and spectral discrimination (<10 nm) between the intramuscular fat in the chicken breast and the polyethylene tube. These results collectively show that this prototype fiber-optic probe design enables deep-tissue multispectral imaging and has translational potential as a minimally invasive diagnostic tool.

## 4.2. Imaging peripheral nerves

In a surgical procedure, iatrogenic damage to peripheral nerves is a leading cause of morbidity $[79–81]$ . The resultant complications include temporary numbness, loss of sensation, and peripheral neuropathy $[80,82]$ . The accurate noninvasive visualization of nerve tissues relative to adjacent structures is of vital importance yet remains technically challenging. As myelin sheaths surrounding axons are abundant in lipids, there is an opportunity to apply PA imaging technique to discriminate nerves from adjacent tissues using lipid and blood as two different contrasts.

A preliminary feasibility study of nerve imaging was performed in a PAM configuration $[38]$ . Clinical translation of this technique however is impeded by millimeter-scale imaging depth and slow imaging speed. Li et al. recently demonstrated the label-free in vivo tomographic visualization of mouse nerves through PAT based on second overtone absorption of C—H bonds with an imaging depth of at least 2 mm $[39]$ . Spectroscopic imaging was performed in the optical window of 1100 to 1250 nm to discriminate lipid ( $\sim$ 1210 nm) from blood (<1150 nm). An algorithm called multivariate curve resolution alternating least squares (MCR-ALS) $[83]$ was then applied to the spectroscopic image stack to resolve chemical maps from lipid and blood. As shown in Fig. 4c, the femoral nerve fiber was clearly resolved and distinguished from the adjacent femoral artery. Although this application does not require a greater imaging depth, it demonstrates chemical selectivity (using only two excitation wavelengths) and sufficient spatial resolution to discriminate adjacent structures with a large imaging field of view. It has the potential for label-free imaging of peripheral nerves in patients undergoing surgery.

## 4.3. Assessing breast tumor margins

Breast-conserving surgery, or lumpectomy, is a common procedure for breast cancer treatment $[84,85]$ . To prevent local cancer recurrence after lumpectomy, histology is performed to check whether the excised tumor specimen is surrounded by a sufficient amount of normal tissue $[86,87]$ . A re-operation is needed if a positive margin is identified. Currently, the re-operation rate ranges from 20% to 70% $[88,89]$ . This high re-operation rate highlights a pressing need for the development of an intraoperative device that is rapid, sensitive, label-free, and able to scan the entire tissue surface for accurate breast cancer margin assessment.

Recently developed multispectral PAT combining lipid with blood contrast provides a compelling opportunity to meet this need $[90]$ . Specific to breast cancer, multispectral PAT, as shown in Fig. 4a, was applied for margin detection in the optical window from 1100 to 1250 nm. In this window, the distribution of fat and blood were visualized after acquisition of a multispectral image stack. The image stack was processed through the MCR-ALS algorithm, generating chemical maps for those two major components (Fig. 4d). Based on the imaging results and a comparison with histology results, the area with fat and lacking hemoglobin contrast was assigned to be normal tissue with fat and scattered fibrous tissue (red oval). The area with hemoglobin contrast and fat indicated angiogenesis and invasive tumor with scattered fat tissue (yellow oval). The area without fat contrast indicated tumor tissue with dense fibrous tissue (blue oval). These results collectively demonstrated the capacity of tumor margin assessment based on the contrast of hemoglobin and fat. This imaging configuration maintains an imaging depth of up to 3 mm, which is sufficient for determining breast tumor margins (typically 1–2 mm of tumor-free tissue are necessary for a margin to be negative). With 100% sensitivity, the system can successfully detect breast tumor margin and opens a new way for clinical intraoperative breast tumor margin assessment. A similar approach using blood and lipid as two complementary contrasts has recently been demonstrated to visualize the vasculature and external boundaries of healthy lymph nodes across their depth (<6 mm) $[91]$ . Future studies will be useful for “indirect detection” of cancerous nodes in which the structure and composition are expected to change.

## 5. Intravascular photoacoustic imaging of lipid-laden plaques

Beyond microscopic studies of lipid-laden plaques inside an atherosclerotic artery, IVPA has been intensively investigated over the past few years. As is widely known, cardiovascular disease is the number one cause of death in the United States. The majority of acute fatal incidents with cardiovascular disease are due to vulnerable plaques, which are at a high risk for rupture and thrombosis [92,93]. Pathophysiological findings suggest that these vulnerable lesions contain a large lipid core covered by a thin fibrous cap and are located in areas of high shear stress within the coronary arterial wall [94,95]. Current imaging modalities either lack compositional contrast or sufficient imaging depth for this application. Furthermore, no existing imaging tools can reliably and accurately diagnose vulnerable plaques in live patients [96]. However, IVPA maintains high resolution, chemical selectivity, and sufficient imaging depth to characterize vulnerable plaques. It has great potential to be developed as a life-saving device for diagnosis of vulnerable plaques.

## 5.1. Imaging lipid-laden atherosclerotic plaques

The current translational goal for IVPA imaging is to detect lipid-laden plaques with high accuracy and specificity. Thus, the selection of an optimal wavelength to excite lipids becomes the primary objective. PA imaging of lipid-rich plaques has been demonstrated using different wavelengths $[35,97,98]$ . However, the PA signal from lipids between 400 and 1100 nm is greatly overwhelmed by hemoglobin absorption, and is not suitable for in vivo applications. When the wavelength exceeds 1.1 $\mu$ m, hemoglobin absorption is minimal, but significant water absorption due to vibrational transition of O—H bonds attenuates light intensity inside the biological tissue. Nevertheless, two optical windows have been revealed for PA detection of overtone absorption of C—H bonds, where lipids can be imaged at $\sim$ 1.2 $\mu$ m and $\sim$ 1.7 $\mu$ m as discussed before $[31,36,44]$ .

Grounded on these two lipid-specific optical windows, a series of IVPA imaging developments has been reported. Jansen et al. demonstrated the first IVPA imaging result of human artery with 1210 nm excitation of the second overtone of C—H bond [32]. As seen in Fig. 5a, the histology shows a large eccentric lipid-rich lesion, as well as a calcified area and regions of peri-adventitial fat, which is confirmed by IVUS image. The IVPA image at 1210 nm exhibits a bright signal along the intimal border, and also from deeper tissue layers in the eccentric plaque and the peri-adventitial fat in the bottom right corner, compared with IVPA image at 1230 nm. Wang et al. tested the feasibility of IVPA imaging of atherosclerotic rabbit aorta at 1.7 $\mu$ m in the presence of luminal blood [36]. A preliminary study of in vivo IVPA imaging was also performed at 1720 nm in a rabbit model [43]. These results suggest that in vivo IVPA imaging is possible even without flushing luminal blood with saline, a necessary step for imaging coronary arteries with optical coherence tomography. Recently, with the availability of high-repetition-rate laser sources, a few research groups have developed high-speed IVPA imaging at $\sim$ 1.7 $\mu$ m [99–101]. Hui et al. demonstrated the high-speed IVPA imaging of human femoral artery ex vivo at 1 frame per sec as shown in Fig. 5b [99]. The IVPA and IVUS images of the atherosclerotic artery reveal complementary information in the artery wall. The lipid deposition in the arterial wall indicated by white arrows at 2 and 3 o'clock directions, which is not seen in the IVUS image, shows clear contrast in the IVPA image.

![](images/db5b878659ceffda97485068bfb39559d4fba46996c8b820a2958a4a07a3ef40.jpg)  
Fig. 5. IVPA/IVUS imaging of lipid-laden atherosclerotic plaque. (a) IVPA/IVUS imaging of an advanced human atherosclerotic plaque in 1.2 $\mu$ m optical window: histology with Oil Red O stain; IVUS image; IVPA image at 1210 nm (high lipid absorption); IVPA image at 1230 nm (low lipid absorption). \*, lipid-rich plaque; Ca, calcified area; arrowheads, a needle used for marking. (b) IVPA/IVUS imaging of an excised human femoral artery in 1.7 $\mu$ m optical window: IVPA image at 1724 nm with white arrows indicating large lipid deposition; IVUS image. Adapted with permission from Ref. [32] (a) and Ref. [99] (b).

## 5.2. High-speed laser sources

IVPA imaging has been widely considered a promising technique for the diagnosis of vulnerable plaque in the arterial wall of live patients. However, the translation of the imaging technology from bench to bedside has been stifled by its slow imaging speed, mainly due to lack of suitable laser sources to excite the molecular overtone transitions at a high repetition rate. Wang et al. recently demonstrated a 2-kHz master oscillator power amplifier (MOPA)-pumped barium nitrite $\left(\mathrm{Ba}(\mathrm{NO}_{3})_{2}\right)$ Raman laser, which enabled the high-speed IVPA imaging [47]. In the laser system, a 1064 nm pulsed laser at a repetition rate of 2 kHz generated by the MOPA laser was used to pump the $\mathrm{Ba}(\mathrm{NO}_{3})_{2}$ -based Raman shifter (Fig. 6a). Through a stimulated Raman scattering process, the 1064 nm pump laser is converted to an 1197 nm output, which matches the second overtone vibration of C—H bond and thus can be used to excite the lipid-rich plaques. The high-speed IVPA imaging with this laser was validated using the iliac artery from a pig model at a speed of 1 frame per sec, which is nearly two orders of magnitude faster than previously reported systems.

Since 1.7 $\mu$ m optical window is more optimal for in vivo IVPA imaging when compared with 1.2 $\mu$ m, the laser development having output at $\sim$ 1.7 $\mu$ m with high pulse energy and high repetition rate is of great importance toward the in vivo applications of IVPA imaging. More recently, several research groups have developed such laser sources based on different technologies with a repetition rate of kHz levels and applied them to high-speed IVPA imaging [99–101]. As one example, shown in Fig. 6b, a potassium titanyl phosphate (KTP)-based OPO laser has an output at 1724 nm with pulse energy up to 2 mJ and with pulse repetition rate of 500 Hz [99]. In order to obtain high pulse energy at high repetition rate, two KTP crystals were cut with a special angle and placed with adverse orientation in the OPO, which effectively minimized the walk-off effect. This laser enabled imaging of human artery at a speed of 1 frame per sec with a cross-sectional IVPA image composed of 500 A-lines. This speed greatly reduces the ambiguity caused by slow imaging speed and can be further used for preclinical in vivo imaging. However, in order to make IVPA competitive in the clinic, the repetition rate needs to be further improved to the order of 10 kHz [99].

## 6. Discussion

Harnessing its high depth scalability and endogenous contrast mechanism, vibration-based PA imaging has opened up a range of biomedical applications in forms of microscopy, tomography, and intravascular imaging, as well as technical challenges for their translation to the clinic. PAM with overtone absorption of C—H bonds as the contrast can achieve ultrasonic resolution in deep tissue regime. As lipids are rich in $CH_{2}$ -groups, PAM offers opportunities for lipid imaging, which is often related to disease severity, including type 2 diabetes and white matter loss and regeneration. Using an OPO as the light exciting source, multispectral PAM can be achieved with spectral signatures of molecules. Currently, with $\sim20$ MHz ultrasound transducer, the lateral resolution of vibration-based PAM is $\sim70\mu m$ [31]. However, it potentially can be increased by 10 times with optical-resolution PAM configuration through a $\sim75$ MHz transducer and objective lens [102]. Because of light focusing and sample scanning scheme, the speed of PAM is limited, which hinders its translation from bench to bedside. However, imaging speed may be improved by translating the transducer instead of the sample stage $[103]$ .

![](images/362f50849b769452d7469929e1ff26def39735b4299cd7506c86e5585bf50178.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Input: 1064 nm"] --> B["Amplifier"]
  B --> C["Amplifier 2"]
  C --> D["Amp 1"]
  D --> E["Amplifier 1"]
  E --> F["O1"]
  F --> G["Output: 1064 nm"]
    
    subgraph Input
  H["M2"] --> I["PBS"]
  J["M3"] --> K["HWP"]
  L["M6"] --> M["Isolator"]
  N["M7"] --> O["Ba(NO3)2"]
  P["M8"] --> Q["M9"]
  R["M10"] --> S["Beam trap"]
    end
    
    subgraph Output
  T["M4"] --> U["Telescope"]
  V["M5"] --> W["Beam trap"]
    end
    
  X["DL"] --> Y["FA"]
  Y --> Z["fiber"]
  Z --> AA["OI"]
  AA --> AB["Output: 1197 nm"]
```
</details>

![](images/90e12469f324828c7a3534f40971d1d856b4149bccfaf7764db45acaf86ffd35.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Laser Diode"] --> B["Coupling Lenses"]
  B --> C["Fold Mirror"]
  C --> D["O-X-PN"]
  D --> E["Polarizer"]
  E --> F["KD*P"]
  F --> G["E-O Q-switch"]
  G --> H["M2"]
  G --> I["M3"]
  H --> J["Dump"]
  I --> K["M4"]
  J --> L["M6"]
  K --> M["M5"]
  L --> N["M7"]
  M --> O["M8"]
  N --> P["Signal"]
  O --> P
  P --> Q["Laser Diode"]
```
</details>

Fig. 6. High-repetition-rate laser sources developed for IVPA imaging. (a) Schematics of 2 kHz MOPA-pumped Raman laser with an output of 1197 nm. Amp: amplifier; PH: pin hole; QR: quartz rotator; Ol: optical isolator; FA: fiber amplifier; DL: Directly modulated diode laser; M $_{1}$ -M $_{7}$ : 45-degree 1064 nm reflective mirror; PBS: polarizing beam splitter; HWP: half wave plate; M $_{8}$ : resonator end mirror; M $_{9}$ : output coupler; M $_{10}$ : silver mirror. (b) Schematics of 500 Hz KTP-based OPO laser with an output of 1724 nm. M $_{1}$ , M $_{2}$ , M $_{5}$ , M $_{6}$ , flat mirrors; M $_{3}$ , M $_{4}$ , M $_{8}$ , reflective mirrors; M $_{7}$ , dichroic mirror; KD\*P, potassium dideuterium phosphate Pockels cell; KTP, potassium titanyl phosphate. The inset shows the pictures of the actual laser system. Adapted with permission from Ref. [47] (a) and Ref. [99] (b).

PAT in the new optical windows offers new opportunities for its use in biomedicine, but also some particular engineering challenges. As demonstrated in the previous examples, the ability to perform either two-color imaging or multispectral tomography lends the technology to different applications. For instance, a two-color PAT system for ex vivo breast tumor margin assessment may be advantageous for a compact mobile system designed for a clinical setting, whereas multispectral tomography is helpful for analyzing spectral differences in more complex tissue samples. The most salient advantage and future direction for vibration-based PAT though is the enabling of molecular-specific deep-tissue imaging applications. Vessels, nerves, and organs that accumulate pathological levels of lipid are of primary interest in this regard. Currently, magnetic resonance imaging, X-ray computed tomography, and ultrasound are used in the clinic to aid in the diagnosis and treatment monitoring of lesions, such as those in atherosclerosis and fatty liver disease $[104,105]$ . While magnetic resonance imaging provides excellent soft tissue contrast and adequate resolution for these applications, its cost and availability make it an impractical option in many cases. Ultrasound and PA imaging are well suited to clinical applications requiring functional and chemical-selective characterization while providing greater imaging depth than purely optical tomographic techniques. Furthermore, different configurations involving excitation or detection outside or within the body expand the capabilities and potential applications of vibration-based PAT.

Challenges for tomographic imaging, including vibration-based PAT, are present and require refinements in the engineering of these systems. Two significant challenges for in vivo imaging are the presence of clutter, or unwanted superficial signal enhancement, and volumetric imaging without motion artifacts. The first is mainly contributed by the distance between the illumination source and the imaging surface (i.e., the irradiation distance) [104]. The geometry of the illumination source and detector may also help to alleviate this effect, which degrades the signal to background ratio. Volumetric imaging provides significantly more morphological and compositional information of large and complex regions. With handheld two-dimensional array transducers, it is important that it is stabilized in order to collect three-dimensional images. Furthermore, gating techniques (i.e., respiration and cardiac gating) can significantly reduce motion artifacts from breathing and vessel motion in small animals, which have high heart and respiration rates. The integration of gating into PAT will be critical for future experiments examining complex lesions and areas of the body where motion is significant.

IVPA imaging has become one of the hot topics in the field of biomedical imaging. So far, it has shown great potential for clinical applications and is undergoing rapid development. To translate the imaging tool from bench to bedside, several significant challenges need to be resolved. The first and most pressing challenge is to develop a high-pulse-energy (mJ level) laser with a lipid-specific wavelength at 1.7 $\mu$ m and with a pulse repetition rate at 10 kHz level. The high pulse energy would be large enough, but also under the ANSI safety limits [106], to ensure effective PA signal generation even through a thin layer of luminal blood. The high repetition rate would enable IVPA imaging at high speeds ( $\sim$ 30 frames/sec), comparable with the speed of many IVUS systems. The second one is to design a clinically relevant IVPA catheter. The catheter should be further miniaturized to $\sim$ 1 mm or less in diameter for clinical practice, as well as maintain excellent detection sensitivity. Better sensitivity could help reduce the laser pulse energy, thus further reducing the challenge for development of a high-pulse-energy laser. In addition, a clinically relevant large animal used as a model for human atherosclerosis is also essential for the validation of IVPA imaging technology. With this model, the in vivo IVPA imaging procedure, the detection of lipid-laden plaques, and the clinical requirements of catheters in pressurized vessels and blood can be all tested and validated. Ultimately, IVPA imaging of living patients could have a phenomenal impact on both diagnosis and treatment of vulnerable plaques. Moreover, it has the potential to guide coronary stenting during percutaneous coronary intervention, as well as to stimulate the development of new cholesterol-lowering and anti-inflammatory therapeutics for atherosclerosis. Indeed, it has the potential to be a life-saving technology when used in clinical settings.

## Conflict of interest

The authors declare that there are no conflicts of interest.

## Acknowledgements

This work was partly supported by the National Institutes of Health (R01HL125385) to J.X. Cheng and M. Sturek, an American Heart Association (AHA) National Innovation Award to J.X. Cheng, an AHA Scientist Development Grant (14SDG18220010) to C.J. Goergen, a Purdue University Center for Cancer Research Jim and Diann Robbers Cancer Research Grant for New Investigators Award to C.J. Goergen, and the Fortune-Fry Ultrasound Research Fund to M. Sturek.

## References

[1] D.C. Fernandez, et al., Infrared spectroscopic imaging for histopathologic recognition, Nat. Biotechnol. 23 (4) (2005) 469–474.  
[2] D. Michael, G.S.M. Morris, in: Y.O. Slobodan Šašić (Ed.), Biomedical Applications of Raman Imaging, in Raman, Infrared, and Near-Infrared Chemical Imaging, John Wiley & Sons, Inc., Hoboken, NJ, USA, 2010, pp. 109–131.  
[3] R. Anthony Shaw, V.V.K. Olga Jilkina, G. Michael Sowa, in: Y.O. Slobodan Šašić (Ed.), Near-Infrared In Vivo Spectroscopic Imaging: Biomedical Research and Clinical Applications, in Raman, Infrared, and Near-Infrared Chemical Imaging, John Wiley & Sons, Inc., Hoboken, NJ, USA, 2010, pp. 149–165.  
[4] M.D. Duncan, J. Reintjes, T.J. Manuccia, Scanning coherent anti-Stokes Raman microscope, Opt. Lett. 7 (8) (1982) 350–352.  
[5] G.R.H. Andreas Zumbusch, X. Sunney Xie, Three-dimensional vibrational imaging by coherent anti-Stokes Raman scattering, Phys. Rev. Lett. 82 (20) (1999) 4142.  
[6] C.W. Freudiger, et al., Label-free biomedical imaging with high sensitivity by stimulated Raman scattering microscopy, Science 322 (5909) (2008) 1857–1861.  
[7] S. Yue, et al., Cholesteryl ester accumulation induced by PTEN loss and PI3K/AKT activation underlies human prostate cancer aggressiveness, Cell. Metab. 19 (3) (2014) 393–406.  
[8] C.M. Sehgal, J.F. Greenleaf, Scattering of ultrasound by tissues, Ultrason. Imaging 6 (1) (1984) 60–80.  
[9] L.V. Wang, H.-i. Wu, Biomedical Optics: Principles and Imaging, John Wiley & Sons, 2012.  
[10] L.V. Wang, Multiscale photoacoustic microscopy and computed tomography, Nat. Photonics 3 (9) (2009) 503–509.  
[11] J. Yao, L.V. Wang, Photoacoustic microscopy, Laser Photonics Rev. 7 (5) (2013) 758–778.  
[12] J. Yao, L.V. Wang, Photoacoustic tomography: fundamentals, advances and prospects, Contrast Media Mol. Imaging 6 (5) (2011) 332–345.  
[13] L.V. Wang, S. Hu, Photoacoustic tomography: in vivo imaging from organelles to organs, Science 335 (6075) (2012) 1458–1462.  
[14] J.M. Yang, et al., Photoacoustic endoscopy, Opt. Lett. 34 (10) (2009) 1591–1593.  
[15] J.M. Yang, et al., Simultaneous functional photoacoustic and ultrasonic endoscopy of internal organs in vivo, Nat. Med. 18 (8) (2012) 1297–1302.  
[16] K. Jansen, G. van Soest, A.F. van der Steen, Intravascular photoacoustic imaging: a new tool for vulnerable plaque identification, Ultrasound Med. Biol. 40 (6) (2014) 1037–1048.  
[17] M. Xu, L.V. Wang, Photoacoustic imaging in biomedicine, Rev. Sci. Instrum. 77(4) (2006) 041101.  
[18] J. Yao, L.V. Wang, Sensitivity of photoacoustic microscopy, Photoacoustics 2 (2) (2014) 87–101.  
[19] B. Cox, et al., Quantitative spectroscopic photoacoustic imaging: a review, J. Biomed. Opt. 17 (6) (2012) 0612021–06120222.  
[20] A. de la Zerda, et al., Advanced contrast nanoagents for photoacoustic molecular imaging: cytometry, blood test and photothermal theranostics, Contrast Media Mol. Imaging 6 (5) (2011) 346–369.  
[21] D. Pan, et al., A brief account of nanoparticle contrast agents for photoacoustic imaging, Wiley Interdiscip. Rev. Nanomed. Nanobiotechnol. 5(6) (2013) 517–543.  
[22] D. Wu, et al., Contrast agents for photoacoustic and thermoacoustic imaging: a review, Int. J. Mol. Sci. 15 (12) (2014) 23616–23639.  
[23] C. Li, L.V. Wang, Photoacoustic tomography and sensing in biomedicine, Phys. Med. Biol. 54 (19) (2009) R59–R97.  
[24] V. Ntziachristos, Going deeper than microscopy: the optical imaging frontier in biology, Nat Methods 7 (8) (2010) 603–614.  
[25] S. Mallidi, G.P. Luke, S. Emelianov, Photoacoustic imaging in cancer detection: diagnosis, and treatment guidance, Trends Biotechnol. 29 (5) (2011) 213–221.  
[26] A. Taruttis, V. Ntziachristos, Advances in real-time multispectral optoacoustic imaging and its applications, Nat. Photonics 9 (4) (2015) 219–227.  
[27] M.A. Pleitez, et al., In vivo noninvasive monitoring of glucose concentration in human epidermis by mid-infrared pulsed photoacoustic spectroscopy, Anal. Chem. 85 (2) (2013) 1013–1020.  
[28] V.V. Yakovlev, et al., Stimulated Raman photoacoustic imaging, Proc. Natl. Acad. Sci. U. S. A. 107 (47) (2010) 20335–20339.  
[29] V.V. Yakovlev, et al., Monitoring stimulated Raman scattering with photoacoustic detection, Opt. Lett. 36 (7) (2011) 1233–1235.  
[30] S.L. Jacques, Role of tissue optics and pulse duration on tissue effects during high-power laser irradiation, Appl. Opt. 32 (13) (1993) 2447–2454.  
[31] H.W. Wang, et al., Label-free bond-selective imaging by listening to vibrationally excited molecules, Phys. Rev. Lett. 106 (23) (2011) 238106.  
[32] K. Jansen, et al., Intravascular photoacoustic imaging of human coronary atherosclerosis, Opt. Lett. 36 (5) (2011) 597–599.  
[33] P. Wang, et al., Mapping lipid and collagen by multispectral photoacoustic imaging of chemical bond vibration, J. Biomed. Opt. 17 (9) (2012) 96010–96011.  
[34] P. Wang, et al., Bond-selective imaging of deep tissue through the optical window between 1600 and 1850 nm, J. Biophotonics 5 (1) (2012) 25–32.  
[35] T.J. Allen, et al., Spectroscopic photoacoustic imaging of lipid-rich plaques in the human aorta in the 740 to 1400 nm wavelength range, J. Biomed. Opt. 17(6) (2012) 061209.  
[36] B. Wang, et al., Intravascular photoacoustic imaging of lipid in atherosclerotic plaques in the presence of luminal blood, Opt. Lett. 37 (7) (2012) 1244–1246.  
[37] Z. Xu, C. Li, L.V. Wang, Photoacoustic tomography of water in phantoms and tissue, J. Biomed. Opt. 15 (3) (2010) 036019.  
[38] T.P. Matthews, et al., Label-free photoacoustic microscopy of peripheral nerves, J. Biomed. Opt. 19 (1) (2014) 16004.  
[39] R. Li, et al., Label-free in vivo imaging of peripheral nerve by multispectral photoacoustic tomography, J. Biophotonics 9 (1–2) (2016) 124–128.  
[40] R. Li, et al., Compact high power barium nitrite crystal-based Raman laser at 1197 nm for photoacoustic imaging of fat, J. Biomed. Opt. 18 (4) (2013) 040502.  
[41] W. Wu, et al., Assessment of white matter loss using bond-selective photoacoustic imaging in a rat model of contusive spinal cord injury, J. Neurotrauma 31 (24) (2014) 1998–2002.  
[42] X. Li, et al., Intravascular photoacoustic imaging at 35 and 80 MHz, J. Biomed. Opt. 17 (10) (2012) 106005.  
[43] B. Wang, et al., In vivo intravascular ultrasound-guided photoacoustic imaging of lipid in plaques using an animal model of atherosclerosis, Ultrasound Med. Biol. 38 (12) (2012) 2098–2103.  
[44] K. Jansen, et al., Photoacoustic imaging of human coronary atherosclerosis in two spectral bands, Photoacoustics 2 (1) (2014) 12–20.  
[45] X. Bai, et al., Intravascular optical-resolution photoacoustic tomography with a 1.1 mm diameter catheter, PLoS One 9 (3) (2014) pe92463.  
[46] J. Zhang, et al., Characterization of lipid-rich aortic plaques by intravascular photoacoustic tomography: ex vivo and in vivo validation in a rabbit atherosclerosis model with histologic correlation, J. Am. Coll. Cardiol. 64 (4) (2014) 385–390.  
[47] P. Wang, et al., High-speed intravascular photoacoustic imaging of lipid-laden atherosclerotic plaque enabled by a 2-kHz barium nitrite Raman laser, Sci. Rep. 4 (2014) 6889.  
[48] J. Hui, J.-x. Cheng, Converting molecular vibration to mechanical wave for bond-selective imaging of deep tissue $^{\dagger}$ , Chinese J. Chem. Phys. 28 (4) (2015) 375–382.  
[49] B. Wang, et al., Detection of lipid in atherosclerotic vessels using ultrasound-guided spectroscopic intravascular photoacoustic imaging, Opt. Express 18(5) (2010) 4889–4897.  
[50] W.B. Gratzer, N.K.H. Suzuki, G.M. Hale, M.R. Querry, R.L.P. van Veen, H.J.C.M. Sterenborg, A. Pifferi, A. Torricelli, R. Cubeddu, Generic tissue optical properties. http://omlc.org/news/feb15/generic\_optics/index.html (retrieved 17.1.2016).  
[51] R. Nachabe, et al., Effect of bile absorption coefficients on the estimation of liver tissue optical properties and related implications in discriminating healthy and tumorous samples, Biomed. Opt. Express 2 (3) (2011) 600–614.  
[52] M. Friebel, et al, Influence of oxygen saturation on the optical scattering properties of human red blood cells in the spectral range 250 to 2000 nm, J. Biomed. Opt. 14 (3) (2009) 034001.  
[53] G.M. Hale, M.R. Querry, Optical constants of water in the 200-nm to 200-microm wavelength region, Appl. Opt. 12 (3) (1973) 555–563.  
[54] R.R. Anderson, et al., Selective photothermolysis of lipid-rich tissues: a free electron laser study, Lasers Surg. Med. 38 (10) (2006) 913–919.  
[55] R.L. van Veen, et al., Determination of visible near-IR absorption coefficients of mammalian fat using time- and spatially resolved diffuse reflectance and transmission spectroscopy, J. Biomed. Opt. 10 (5) (2005) 054004.  
[56] B.T. Cox, J.G. Laufer, P.C. Beard, The challenges for quantitative photoacoustic imaging, Proc. SPIE 7177 (2009) 717713.  
[57] P. Wang, J.R. Rajian, J.X. Cheng, Spectroscopic imaging of deep tissue through photoacoustic detection of molecular vibration, J. Phys. Chem. Lett. 4 (13) (2013) 2177–2185.  
[58] J. Workman Jr, L. Weyer, Practical Guide to Interpretive Near-infrared Spectroscopy, CRC Press, 2007.  
[59] J.R. Rajian, et al., Vibrational photoacoustic tomography: chemical imaging beyond the ballistic regime, J. Phys. Chem. Lett. 4 (19) (2013) 3211–3215.  
[60] P. Hai, et al., Near-infrared optical-resolution photoacoustic microscopy, Opt. Lett. 39 (17) (2014) 5192–5195.  
[61] T.R. Wright, The genetics of biogenic amine metabolism, sclerotization, and melanization in Drosophila melanogaster, Adv. Genet. 24 (1987) 127–222.  
[62] P.J. Shaw, et al., Correlates of sleep and waking in Drosophila melanogaster, Science 287 (5459) (2000) 1834–1837.  
[63] R.C. Scott, O. Schuldiner, T.P. Neufeld, Role and regulation of starvation-induced autophagy in the Drosophila fat body, Dev. Cell 7 (2) (2004) 167–178.  
[64] K.D. Baker, C.S. Thummel, Diabetic larvae and obese flies-emerging studies of metabolism in Drosophila, Cell. Metab. 6 (4) (2007) 257–266.  
[65] M. Slaidina, et al., A Drosophila insulin-like peptide promotes growth during nonfeeding states, Dev. Cell 17 (6) (2009) 874–884.  
[66] B.H. Goodpaster, et al., Intramuscular lipid content is increased in obesity and decreased by weight loss, Metabolism 49 (4) (2000) 467–472.  
[67] J. He, S. Watkins, D.E. Kelley, Skeletal muscle lipid content and oxidative enzyme activity in relation to muscle fiber type in type 2 diabetes and obesity, Diabetes 50 (4) (2001) 817–823.  
[68] N.K. Liu, et al., A novel role of phospholipase A2 in mediating spinal cord secondary injury, Ann. Neurol. 59 (4) (2006) 606–619.  
[69] C. Martel, et al., Photoacoustic lymphatic imaging with high spatial-temporal resolution, J. Biomed. Opt. 19 (11) (2014) 116009.  
[70] T.N. Erpelding, et al., Sentinel lymph nodes in the rat: noninvasive photoacoustic and US imaging with a clinical US system, Radiology 256 (1) (2010) 102–110.  
[71] W.J. Akers, et al., Noninvasive photoacoustic and fluorescence sentinel lymph node identification using dye-loaded perfluorocarbon nanoparticles, ACS Nano 5 (1) (2011) 173–182.  
[72] J. Gamelin, et al., A real-time photoacoustic tomography system for small animals, Opt. Express 17 (13) (2009) 10489–10498.  
[73] A. Taruttis, et al., Real-time imaging of cardiovascular dynamics and circulating gold nanorods with multispectral optoacoustic tomography, Opt. Express 18 (19) (2010) 19592–19602.  
[74] S.V. Hudson, et al., Targeted noninvasive imaging of EGFR-expressing orthotopic pancreatic cancer using multispectral optoacoustic tomography, Cancer Res. 74 (21) (2014) 6271–6279.  
[75] Y. Zhou, et al., Handheld photoacoustic probe to detect both melanoma depth and volume at high speed in vivo, J. Biophotonics 8 (11–12) (2015) 961–967.  
[76] S. Carr, et al., Atherosclerotic plaque rupture in symptomatic carotid artery stenosis, J. Vasc. Surg. 23 (5) (1996) 755–766.  
[77] N.A.S.C.E.T. Collaborators, Beneficial effect of carotid endarterectomy in symptomatic patients with high-grade carotid stenosis, N. Engl. J. Med. 325(7) (1991) 445.  
[78] Jie Hui, Rui Li, Pu Wang, Evan Phillips, Rebecca Bruning, Chien-Sheng Liao, Michael Sturek, Craig J. Goergen, Ji-Xin Cheng, Assessing carotid atherosclerosis by fiber-optic multispectral photoacoustic tomography, Proc. SPIE 9323 (2015) 93233S.  
[79] A.D. Sharma, et al., Peripheral nerve injuries during cardiac surgery: risk factors, diagnosis, prognosis, and prevention, Anesth. Analg. 91 (6) (2000) 1358–1369.  
[80] G. Antoniadis, et al., Iatrogenic nerve injuries: prevalence, diagnosis and treatment, Dtsch. Arztebl. Int. 111 (16) (2014) 273–279.  
[81] B.F. Jung, et al., Neuropathic pain following breast cancer surgery: proposed classification and research update, Pain 104 (1) (2003) 1–13.  
[82] A.J. Wilbourn, Iatrogenic nerve injuries, Neurol. Clin. 16 (1) (1998) 55–82.  
[83] J. Jaumot, et al., A graphical user-friendly interface for MCR-ALS: a new tool for multivariate curve resolution in MATLAB, Chemom. Intell. Lab. Syst. 76 (1) (2005) 101–110.  
[84] B. Fisher, et al., Twenty-year follow-up of a randomized trial comparing total mastectomy: lumpectomy, and lumpectomy plus irradiation for the treatment of invasive breast cancer, N. Engl. J. Med. 347 (16) (2002) 1233–1241.  
[85] U. Veronesi, et al., Twenty-year follow-up of a randomized study comparing breast-conserving surgery with radical mastectomy for early breast cancer, N. Engl. J. Med. 347 (16) (2002) 1227–1232.  
[86] D. Aziz, et al., The role of reexcision for positive margins in optimizing local disease control after breast-conserving surgery for cancer, Breast J. 12 (4) (2006) 331–337.  
[87] M.F. Dillon, et al., Factors affecting successful breast conservation for ductal carcinoma in situ, Ann. Surg. Oncol. 14 (5) (2007) 1618–1628.  
[88] F.J. Fleming, et al., Intraoperative margin assessment and re-excision rate in breast conserving surgery, Eur. J. Surg. Oncol. 30 (3) (2004) 233–237.  
[89] L. Jacobs, Positive margins: the challenge continues for breast surgeons, Ann. Surg. Oncol. 15 (5) (2008) 1271–1272.  
[90] R. Li, et al., Assessing breast tumor margin by multispectral photoacoustic tomography, Biomed. Opt. Express 6 (4) (2015) 1273–1281.  
[91] J.A. Guggenheim, et al., Photoacoustic imaging of human lymph nodes with endogenous lipid and hemoglobin contrast, J. Biomed. Opt. 20 (5) (2015) 50504.  
[92] P. Libby, Inflammation in atherosclerosis, Nature 420 (6917) (2002) 868–874.  
[93] M. Naghavi, et al., From vulnerable plaque to vulnerable patient: a call for new definitions and risk assessment strategies: part I, Circulation 108 (14) (2003) 1664–1672.  
[94] A. Fernandez-Ortiz, et al., Characterization of the relative thrombogenicity of atherosclerotic plaque components: implications for consequences of plaque rupture, J. Am. Coll. Cardiol. 23 (7) (1994) 1562–1569.  
[95] E. Falk, P.K. Shah, V. Fuster, Coronary plaque disruption, Circulation 92 (3) (1995) 657–671.  
[96] R. Puri, et al., Exploring coronary atherosclerosis with intravascular imaging, Int. J. Cardiol. 168 (2) (2013) 670–679.  
[97] P.C. Beard, T.N. Mills, Characterization of post mortem arterial tissue using time-resolved photoacoustic spectroscopy at 436, 461 and 532 nm, Phys. Med. Biol. 42 (1) (1997) 177–198.  
[98] S. Sethuraman, et al., Spectroscopic intravascular photoacoustic imaging to differentiate atherosclerotic plaques, Opt. Express 16 (5) (2008) 3362–3367.  
[99] J. Hui, et al., High-speed intravascular photoacoustic imaging at 1.7 $\mu$ m with a KTP-based OPO, Biomed. Opt. Express 6 (11) (2015) 4557–4566.  
[100] Y. Li, et al., High-speed intravascular spectroscopic photoacoustic imaging at 1000 A-lines per second with a 0.9-mm diameter catheter, J. Biomed. Opt. 20(6) (2015) p065006.  
[101] Z. Piao, et al., High speed intravascular photoacoustic imaging with fast optical parametric oscillator laser at 1.7 m, Appl. Phys. Lett. 107 (8) (2015) p083701.  
[102] K. Maslov, et al., Optical-resolution photoacoustic microscopy for in vivo imaging of single capillaries, Opt. Lett. 33 (9) (2008) 929–931.  
[103] S. Hu, K. Maslov, L.V. Wang, Second-generation optical-resolution photoacoustic microscopy with improved sensitivity and speed, Opt. Lett. 36(7) (2011) 1134–1136.  
[104] J.M. Cai, et al., Classification of human carotid atherosclerotic lesions with in vivo multicontrast magnetic resonance imaging, Circulation 106 (11) (2002) 1368–1373.  
[105] J.B. Schwimmer, et al., Magnetic resonance imaging and liver histology as biomarkers of hepatic steatosis in children with nonalcoholic fatty liver disease, Hepatology 61 (6) (2015) 1887–1895.  
[106] American National Standard for Safe Use of Lasers, ANSI Z136.1. 2014: Laser Institute of America.