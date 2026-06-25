# Fingerprinting a Living Cell by Raman Integrated Mid-Infrared Photothermal Microscopy

Xiaojie Li,†,‡,§,∥ Delong Zhang, §,∥ Yeran Bai,‡,§,∥ Weibiao Wang,† Jingqiu Liang, 4 and Ji-Xin Cheng\*,§,∥,⊥,# iD

† State Key Laboratory of Applied Optics, Changchun Institute of Optics, Fine Mechanics and Physics, Chinese Academy of Sciences, Changchun, Jilin 130033, China  
‡ University of Chinese Academy of Sciences, Beijing 100049, China  
§ Department of Electrical and Computer Engineering, ∥ Photonics Center, ⊥Department of Biomedical Engineering, and # Department of Chemistry, Boston University, Boston, Massachusetts 02215, United States

Supporting Information

ABSTRACT: Vibrational spectroscopic imaging techniques, based on infrared absorption or Raman scattering, allow for noninvasive chemically specific visualization of biological systems. The infrared and Raman modalities with different selection rules provide complementary information. Specifically, infrared microscopy provides strong signals in the fingerprint region, but suffers from low spatial resolution. Raman microscopy provides submicrometer resolution, but requires a long acquisition time. We developed a system that combines the strengths of both techniques by integrating confocal Raman microspectroscopy to the recently developed mid-infrared photothermal microscopy. This hybrid system is capable of fast infrared photothermal imaging of living cells with submicrometer resolution to identify points of interest, followed by a full-spectrum Raman analysis of the identified objects. In addition, a fingerprint photothermal spectrum can be acquired by scanning the wavelengths of the infrared laser. Comprehensive vibrational

fingerprint mapping of live cells, demonstrated in adipocytes and single bacteria, promises broad applications of this technology in biology and material science.

![](images/18bdf8590bda952e02af35462770ce71eac3f054241799679710611bfed007e0.jpg)

<details>
<summary>text_image</summary>

IR 1650 cm⁻¹
Counts
225
75
0
900 1200 1500 1800
Raman shift (cm⁻¹)
</details>

he changes of chemical composition in cells and tissues are indicative of functional abnormalities, for example, aberrant accumulation of cholesterol ester in aggressive prostate cancer.1 Optical spectroscopic imaging with molecular fingerprint information infers extensive possibilities for better identifying and understanding of diseases by characterizing chemical composition at a subcellular level. Among various techniques, the vibrational spectroscopy2 has become a unique tool in biology and medicine because of its capacity in visualizing the molecular composition of subcellular structures noninvasively. Infrared3,4 (IR) absorption spectroscopy and Raman5,6 scattering spectroscopy are two main modalities of the vibrational spectroscopy, both of which can yield reproducible spectral information from a specimen.

Based on infrared spectroscopy, the Fourier transform infrared (FTIR) microscope has been widely used for spatially resolved chemical analysis of biological systems.7,8 Despite its wide use, FTIR microspectroscopy offers poor spatial resolution in the range from 3 to 30 μm,9 depending on the wavelength of light and instrument deployed. Such low spatial resolution prohibits the application of FTIR in characterizing subcellular structures or single microorganisms. To overcome the spatial resolution challenge, indirect measurement by the combination of an atomic force microscope with an infrared laser source (AFM-IR) was developed. In an AFM-IR microscope, an AFM tip is used to sense and map IR-induced thermal expansion below the diffraction limit.10 As a result, the spatial resolution can be improved to 20 nm.11 However, FTIR and AFM-IR are mostly applicable to dried specimens, which hinders their use for functional analysis of living systems in an aqueous environment. Additionally, AFM-IR needs a long acquisition time, typically tens of minutes per frame.12

To overcome such limitations, optical probing of thermal effect as a noncontact approach to detect the IR absorption has been developed, namely, infrared photothermal imaging.13−16 The target molecules absorb the mid-IR light and convert the energy into a rise in temperature, resulting in the changes in local refractive index. Consequently, a variation in the propagation of the visible probe beam can be detected. The resolution is in accordance with the diffraction limit of the visible probe wavelength. Zhang et al.13 built a mid-infrared photothermal (MIP) microscope and demonstrated IR imaging of living cells and organisms for the first time with a spatial resolution of 0.6 μm. Li et al.14 demonstrated a backward detected MIP imaging of the active pharmaceutical

Received: May 16, 2019

Accepted: July 17, 2019

Published: July 17, 2019

ingredients in a drug tablet. Bai et al.15 demonstrated MIP imaging in the 2100 cm−1 region by implementing difference frequency generation from femtosecond lasers. By utilizing a counter-propagation system with a 532 nm laser and a water immersion objective, Li et al.16 achieved a spatial resolution of 0.3 μm and demonstrated photothermal imaging of a single E. coli cell in the high-wavenumber C−H region. Using a near-IR fiber laser probe, Totachawattana et al.17 achieved signal-tobaseline values of mid-IR photothermal spectroscopy exceeding 103 . Samolis et al.18 provided higher contrast and enhanced spatial resolution for imaging single weakly absorbing features by combining photothermal phase-sensitive lock-in detection with mid-IR vibrational signatures.

Raman spectroscopy is especially suitable for biological applications because of the weak Raman signal of water. 19 Spontaneous Raman microscopy allows visualization of the molecular composition of a single cell, but it requires long acquisition time on the order of seconds per pixel.20 To overcome the speed limitation, coherent Raman scattering microscopy, including coherent anti-Stokes Raman scatterin g21−23 and stimulated Raman scattering24−26 microscopy, has been developed and employed to visualize subcellular structures at the speed of a few microseconds per pixel or 1.0 s per frame on a laser-scanning microscope platform. Yet, wide use of coherent Raman scattering microscopy relies on the development of compact and low-cost ultrafast laser sources.

IR spectroscopy and Raman spectroscopy are often used together for comprehensive characterization of materials. These two techniques arise from different processes and follow different selection rules. IR spectroscopy arises from vibrational absorption of light by vibrating molecules, while Raman spectroscopy is due to the inelastic scattering of light by vibrating molecules.27 In general, IR spectral information is dominated by molecular vibrations involving a net change in the dipole moment. By contrast, Raman vibrational signal accompanies with the change of polarizability of the molecule.28 Appreciating the complementary nature of IR and Raman spectroscopy, Nallala et al.29 characterized colon tissues. Depciuch et al.30 compared breast tumor cancer tissue and healthy tissue with a history of chemotherapy. Perez-Guaita et al.31 investigated red blood cells infected with the Plasmodium falciparum parasite and Micrasterias. Kochan et al.32 used Raman and AFM-IR imaging to determine the effectiveness of metabolic pathway engineering approaches for enhanced lipid content in yeast cells. Notably, those studies were performed on two separate instruments, where samples were usually fixed and moved from an IR microscope to a Raman microscope or made into two forms to suit for each technique. Moreover, due to the spatial resolution mismatch between Raman and IR modalities, coregistration of signals is ffi

Here, we report the integration of infrared photothermal microscopy and Raman spectroscopy, termed as IRaman, where the visible beam is used for both probing the photothermal effect and generating a Raman spectrum at the same spatial resolution. Our system can generate infrared photothermal images at specific IR wavelengths and perform both IR photothermal and Raman scattering spectroscopy at the point of interest for the same sample, especially in the fingerprint region. Because Raman and IR are sensitive to different vibrational modes, this integrated system enables to provide complementary chemical information to a complex biological specimen. In the following sections, we present the development of such a platform and its applications to living cells, using adipocytes and single bacteria as testing beds.

## EXPERIMENTAL SECTION

IRaman Microscope. Figure 1 shows the schematic. A pulsed mid-IR pump beam, generated by a tunable (from 1000

![](images/9b923adc573dc964b3250fd2e681cfa1ab8450e9cf853d477d5138a405b4983f.jpg)

<details>
<summary>text_image</summary>

Mid-IR
MCT
PD
BS
532 nm
CaF₂
Reflective Obj.
Sample
Obj.
LPF
DM
Spectrometer
IR
CaF₂
Sample
Quartz
532 nm
</details>

Figure 1. Schematic of the IRaman microscope. A pulsed mid-IR pump beam and a continuous visible probe beam are focused at the sample with a reflective objective and a water-immersion objective, respectively. The reflected probe beam is collected by a 50:50 beam splitter (BS) and sent to a silicon photodiode (PD). The visible beam also serves as the excitation source for Raman scattering. The Raman scattering signal is reflected by a dichroic mirror (DM) and directed to the spectrometer. The dashed line box shows the sample cell design for living cell investigation. The cell samples are grown on the IR transparent CaF substrate. LPF, long pass filter.

to 1886 cm−1 ) quantum cascade laser (QCL, Daylight Solutions, MIRcat-2400) operating at 100 kHz repetition rate, passes through a calcium fluoride (CaF ) lens and then is focused onto the sample by a reflective objective lens (52×; NA, 0.65; Edmund Optics, #66589) with gold coating. The residual reflection of the infrared beam from the CaF lens is measured by a mercury cadmium telluride (MCT) detector. A continuous-wave probe laser (Cobolt, Samba 532 nm) beam is focused by a high NA refractive objective (60×; NA, 1.2; water immersion; Olympus, UPlanSApo) into the same spot on the sample. The probe beam is aligned to be collinear to the mid-IR pump beam to ensure the overlap of the two focal spots. A scanning piezo stage (Mad City Labs, Nano-Bio 2200) with a maximum scanning speed of 200 μs/pixel is used to scan the samples. The continuous-wave laser is also used as the excitation source for spontaneous Raman scattering. The back-reflected/scattered beam is split by a dichroic mirror (Edmund Optics, #69215) into two beams: one beam containing photothermal information is collected by a 50:50 beam splitter and sent to a silicon photodiode (Hamamatsu, S3994−01); another beam generated by Raman scattering is filtered by a long-pass filter and focused into a spectrometer (Andor Technology, Shemrock SR-303i-A) through an achromatic lens of 100 mm focal length.

![](images/44b351db287fa820715b63404b22dd177b213ea93a84aac8203e7ed4f710be20.jpg)

<details>
<summary>text_image</summary>

A
1730 cm⁻¹
y
x
0.7
0
</details>

![](images/9186a9b952c5149010593c7f6070b1e1238fecc47417ce67b7690c8d500c76be.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | MIP int. (a.u.) |
| ----------------- | --------------- |
| 1400              | ~1.8            |
| 1450              | ~3.5            |
| 1500              | ~2.5            |
| 1600              | ~0.2            |
| 1700              | ~0.3            |
| 1750              | ~6.0            |
| 1800              | ~0.5            |
</details>

![](images/360f0ba902e6cab4eeab194355b1f51ee80dceb54c28807883e332f0106b49c5.jpg)

<details>
<summary>line chart</summary>

| Distance (μm) | FWHM: 0.59 µm | FWHM: 0.57 µm |
| ------------- | ------------- | ------------- |
| 0.0           | 0.1           | 0.1           |
| 0.5           | 0.2           | 0.2           |
| 1.0           | 0.6           | 0.6           |
| 1.5           | 0.4           | 0.4           |
| 2.0           | 0.1           | 0.1           |
</details>

![](images/13a56f1910b7d8f3f6f00c6153851e99b8056b5aa774d399bc43ebd9c8c91e80.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Counts |
| ------------------ | ------ |
| ~850               | ~200   |
| ~950               | ~400   |
| ~1100              | ~300   |
| ~1400              | ~600   |
| ~1600              | ~200   |
| ~2950              | ~1900  |
</details>

Figure 2. Performance of the IRaman microscope. (A) Spatial resolution. MIP image of 500 nm PMMA beads is shown at the top. The horizontal (red) and vertical (blue) intensity profiles are plotted at the bottom. The measured fwhms are 0.59 and 0.57 μm, respectively. Scale bar: 1 μm; Pixel dwell time: 3 ms; Image acquisition time: 14 s; Probe power on the sample: 40 mW; Pump power on the sample: 5 mW at 1730 cm−1 . (B) MIP spectrum obtained from a single PMMA bead in panel A. Acquisition time: 30 ms per wavenumber; int.: intensity; a.u.: arbitrary units. (C) Raman spectrum obtained from the same PMMA bead in panel A. Acquisition time: 4 s.

A laboratory-built resonant circuit (resonant frequency at 103.8 kHz, gain 100) is used to amplify the photocurrent from the photodiode and send it to a lock-in amplifier (Zurich Instruments. HF2LI) for phase-sensitive detection of the MIP signal modulated at the repetition rate of the QCL. The power spectrum of the mid-IR beam collected by the MCT detector is sent to another lock-in input channel, which is used to normalize the MIP signal to obtain the absorption spectrum of samples. Based on the MIP image, a spectrometer equipped with a charge-coupled device (CCD; Andor Technology, Newton DU920N-BR-DD) is used to acquire a Raman spectrum from points of interest, covering the window from 700 to $3 1 0 0 ~ \mathrm { c m } ^ { - 1 }$ . A computer is used to synchronize the QCL wavelength selection, stage scanning, and data acquisition.

Preparation of Adipocytes. Mouse 3T3-L1 preadipocytes (ATCC) were cultured in a basal medium containing high-glucose Dulbecco’s modified eagle medium (Thermo-Fisher) supplemented with 10% fetal bovine serum (Thermo-Fisher) and 1% glutamine−penicillin−streptomycin (GPS). To differentiate 3T3-L1 cells into adipocytes, at 2 days’ postconfluence, the basal medium was changed to a differentiation medium composed of a basal medium supplemented with 0.25 μM dexamethasone, 2 μM rosiglitazone, 10 μg/mL insulin, 0.5 mM 3-isobutyl-1-methylxanthine, and 0.2 mM ascorbic acid 2-phosphate (all from Sigma-Aldrich). After another 2 days, the differentiation medium was replaced with a maintenance medium composed of a basal medium supple mented with 10 $\mu \mathrm { g / m L }$ insulin only for 6 days prior to the imaging.

The dashed line box in Figure 1 shows the sample cell design for living adipocytes. Raman grade CaF coverslips (Crystran Ltd., CAFP13−0.2R) and quartz coverslips (Ted Pella, #26014) instead of standard borosilicate glass coverslips were used to minimize the substrate fluorescence background in Raman spectra. Moreover, the Raman grade CaF provides high transmission of mid-IR light. Living cells were cultured on the Raman grade $\mathrm { C a F } _ { 2 }$ coverslip in a dish in a humidified atmosphere of 5% $\mathrm { C O } _ { 2 }$ at $3 7 ~ ^ { \circ } C .$ . After overnight incubation, the medium was replaced by 1× PBS to avoid background signal provided by the medium. A slide of quartz coverslip was selected to be the substrate and a drop of 1× PBS was placed on the center of the quartz coverslip. Then, the Raman grade $\mathrm { C a F } _ { 2 }$ coverslip with living cells was flipped and placed on the top of the 1× PBS to ensure the activity of cells and avoid 1× PBS absorbing mid-IR light. The quartz and Raman grade $\mathrm { C a F } _ { 2 }$ coverslips were sealed with a double side tape serving as a spacer.

Preparation of Bacterial Sample. Staphylococcus aureus ( S. aureus) 6538 (ATCC) was cultivated in TSB (tryptic soy broth, Sigma-Aldrich) to reach the log phase. After 2 h, 1 mL of bacteria solution was centrifuged and washed twice with sterile water. Then, 4 μL of bacteria solution was deposited to a $\mathrm { C a F } _ { 2 }$ coverslip and kept at room temperature for 5 min for the bacteria to attach to the coverslip.

## RESULTS AND DISCUSSION

Spatial Resolution and Spectral Sensitivity. We first evaluated the performance of our setup using single poly-(methyl methacrylate) (PMMA) beads of 500 nm diameters spreading on a quartz coverslip to minimize the fluorescence background. We first imaged the PMMA beads at the 1730 $\mathrm { c m } ^ { - 1 }$ peak assigned to $\scriptstyle { \dot { \mathrm { C } } } = 0$ stretching (Figure 2A). The measured full width at half-maximum (fwhm) was 0.57 μm in the x direction and 0.59 μm in the y direction. After deconvolution with particle size, a spatial resolution of 0.29 μm was obtained, consistent with the spatial resolution reported by $\mathrm { L i ~ e t ~ a l . ^ { 1 4 } }$ The fwhm along the axial direction was measured to be 1.6 um (Figure S1). After deconyolution with particle size, the depth resolution of our setup was found to be 1.52 μm, which is close to the theoretical value of 1.0 μm. The signal-to-noise ratio for the MIP image of 500 nm PMMA beads at $1 7 3 0 ~ \mathrm { { c m } ^ { - 1 } }$ was 200. The visible beam diffraction limited resolution and the high signal-to-noise ratio offer the opportunity for using the IRaman microscope to study subcellular structures in mammalian cells or microorganism samples.

A  
![](images/f82a52ba9279e5c61c566ac8682a18373d4bbfc0714326230086e50d932addee.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular or particulate structures with circular features and a grayscale intensity scale bar (no text or symbols)
</details>

B  
![](images/1e4dd9639efea9a1cdd2cea0be4eebfac4500ac34df4a828ba22bb2a06c23f62.jpg)

<details>
<summary>natural_image</summary>

Thermal or fluorescence imaging of a molecular structure at 1750 cm⁻¹, showing circular hotspots with a color scale from 0 to 0.15 (no text or symbols beyond scale and label)
</details>

C  
![](images/9c8ec2c6c4bc1834e719f0414cf0ef608ecfe76c7201251479ac4afc5a0a42ff.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | MIP int. (a.u.) |
| ----------------- | --------------- |
| 1400              | ~0.1            |
| 1500              | ~0.2            |
| 1600              | ~0.1            |
| 1700              | ~0.3            |
| 1800              | ~0.8            |
| 1900              | ~0.0            |
</details>

D  
![](images/95a0b1fccc9d48e46f3dbeb475fc9eac86d17f99b74765f1c3d77471f4742793.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Counts |
| ------------------ | ------ |
| ~1100              | ~500   |
| ~1250              | ~1500  |
| ~1450              | ~2500  |
| ~1650              | ~1800  |
| ~2850              | ~7000  |
</details>

Figure 3. Characterization of individual LDs inside an adipocyte cell. (A) Reflection image of a 3T3-L1 cell. (B) MIP image of LDs in a 3T3-L1 cell. Scale bar: 5 μm. Pixel dwell time: 2 ms. Probe power on the sample: 40 mW. Pump power on the sample: 1.5 mW at $1 7 5 0 ~ \mathrm { c m } ^ { - 1 }$ . (C) MIP spectrum of a selected LD in panel B (labeled by white arrow). Acquisition time: 30 ms per wavenumber. (D) Raman spectrum of the same LD in panel B. Acquisition time: 4 s.

Then, we pinpointed the lasers to the center of one PMMA bead marked with blue and red lines in Figure 2A and acquired the MIP spectrum and Raman spectrum. The Raman spectrum was calibrated by peaks of dimethyl sulfoxide (DMSO)33 $( \mathrm { D } \mathbf { \dot { M } S O } ) ^ { 3 3 }$ sandwiched between two glass coverslips (ThermoFisher, Cat. 12440S). For the $\scriptstyle \mathrm { C = O }$ bond in PMMA, the peak intensity is much stronger in the MIP spectrum than in the Raman spectrum. Accordingly, the signal-to-noise ratio at $1 7 3 0 ~ \mathrm { c m } ^ { - 1 }$ in the MIP spectrum $\left( { \mathrm { F i g u r e ~ } } \mathbf { \bar { 2 } B } \right)$ was 500, while the signal-to noise ratio at $1 7 5 0 ~ \mathrm { c m } ^ { - 1 }$ in the Raman spectrum (Figure 2C) was 16.5. Additionally, while the MIP spectrum provides fingerprint information, the Raman spectrum provides fullwindow spectral analysis, featured by a very strong peak of $\mathrm { C H } _ { 3 }$ vibration at $2 9 5 0 ~ \mathrm { { c m } ^ { - 1 } }$ in the high-wavenumber region. Collectively, these data demonstrate the ability of an IRaman microscope to perform high-sensitivity MIP imaging and to provide comprehensive coregistered vibrational spectral analysis of the same object at the same submicrometer spatial resolution.

Characterization of Lipid Droplets (LDs) in Adipocytes. Next, we deployed the IRaman microscope to visualize and analyze individual LDs in a differentiated 3T3-L1 cell. Information about the molecular composition of LDs within their cellular context is crucial to understanding the develop ment of metabolic disorders such as obesity, type II diabetes, and atherosclerosis.34,35 In order to visualize the LDs by an IRaman microscope, the infrared laser was tuned to the 1750 $\mathrm { c m } ^ { - 1 }$ vibration of the $\scriptstyle \mathrm { C = O }$ bond, which is abundant in esterified lipids in LDs. Compared to the reflection image of the 3T3-L1 cell (Figure 3A), the MIP image (Figure 3B) is able to differentiate LDs from other subcellular structures such as the nucleus in the 3T3-L1 cell.

We then pinpointed the laser to the center of a LD (pointed by a white arrow) and acquired its MIP and Raman spectra. From the MIP spectrum $( { \dot { \mathrm { F i g u r e } } } 3 \mathbf { C } )$ , the lipid contents were identified by peaks related to the $\scriptstyle \mathrm { C = O }$ stretching in esters $( 1 7 5 0 ~ \mathrm { c m ^ { - 1 } } )$ and the $\mathrm { C H } _ { 2 }$ bending in the methylene chains $\big ( 1 4 5 5 \mathrm { c m } ^ { - 1 } \big ) . ^ { 3 6 }$ The Raman spectrum $( \mathrm { F i g u r e } \quad 3 \mathrm { D } )$ is prominent in the high wavenumber region, with the peaks at 2852 and $2 8 9 0 ~ \mathrm { { c m } ^ { - 1 } }$ contributed by the $\mathrm { C H } _ { 2 }$ symmetric and antisymmetric vibrations, respectively. In the fingerprint window, besides the ${ \mathrm { C } } { = } 0$ stretching band and the $\mathrm { C H } _ { 2 }$ bending band, peaks contributed by the $\mathrm { C } { - } \mathrm { C }$ stretching at 1092 $\mathrm { c m } ^ { - 1 } , \ \mathrm { t h e \ = c H }$ bending at $1 2 6 0 ~ \mathrm { c m } ^ { - 1 } ,$ , the $\mathrm { C } { = } \mathrm { C }$ stretching at $1 6 6 2 ~ \mathrm { c m } ^ { - 1 }$ , and the $\mathrm { C H } _ { 2 }$ bending vibrations are clearly seen. An important parameter that the Raman spectrum can provide for lipids is the average number of double $\mathrm { C } { = } \mathrm { C }$ bonds at $1 6 6 2 ~ \mathrm { c m } ^ { - 1 }$ within an acyl chain in fatty acids, featured by the intensity ratio between the $\mathrm { C } { = } \mathrm { C }$ stretching peak to the $\mathrm { C H } _ { 2 }$ bending peak. As the three fatty acid species were tested in a previous work,37 the peak of the $\mathrm { C } { = } \mathrm { C }$ stretching is absent in saturated palmitic acid (C16:0) $\left( I ( \mathrm { C = C } ) / I ( \mathrm { C H } _ { 2 } ) = 0 \right)$ , present at low intensity for monounsaturated oleic acid (C18:1) $( I ( \mathrm { C = C } ) / I ( \mathrm { C H } _ { 2 } ) ~ = ~ 0 . 5 8 )$ , and present at high intensity for the polyunsaturated linoleic acid (C18:2) $( I ( { \mathrm { C } } { = } $ $\mathrm { C } ) / I \big ( \mathrm { C H } _ { 2 } \big ) = 1 . 2 7 \big )$ . In our case, the ratio of $I ( \mathrm { C } { = } \mathrm { C } ) / I ( \mathrm { C H } _ { 2 } )$ is measured to be $0 . 7 5 ,$ indicating a relatively high level of unsaturation of lipids in the studied adipocyte. Collectively, these results demonstrate the capability of the IRaman microscope for high-resolution MIP imaging of intracellular lipids and comprehensive coregistered fingerprint spectral analysis of single LDs.

![](images/7406de5ef113f8f9764074d9bdb8b2347e66446b271b406f289f5ecb7bc2c271.jpg)  
Figure 4. Fingerprinting the contents of single bacteria. (A) MIP image of S. aureus cells at the $1 6 5 0 ~ \mathrm { { c m } ^ { - 1 } }$ Amide I band. (B) MIP image of S. aureus cells at the $1 7 8 0 \mathrm { \ c m ^ { - 1 } }$ (off resonance). Scale bar: 2 μm; Pixel dwell time: 0.5 ms; Probe power on the sample: 7 mW; Pump power on the sample: 6 mW at $1 6 5 0 ~ \mathrm { { c m } ^ { - 1 } }$ . (C) MIP spectrum of a S. aureus cell selected from panel A (labeled by white arrow). Probe power on the sample: 2 mW; Acquisition time: 30 ms per wavenumber. (D) FTIR spectrum from a bacterial film of the same S. aureus strain. (E) Raman spectrum of the same S. aureus cell in panel A. Excitation power on the sample: 2 mW; Acquisition time: $3 0 ~ s$ .

Fingerprinting a Single Bacterium. On the basis of the submicrometer resolution of the IRaman microscope, we explored its potential for characterization of single bacteria in the fingerprint region using S. aureus as a testing model. When the IR wavelength was tuned to the $1 6 5 0 ~ \mathrm { { c m } ^ { - 1 } }$ assigned to the protein Amide I band, the bacteria show bright contrast in the MIP image (Figure 4A). When the IR laser was tuned to 1780 $\mathrm { c m } ^ { - 1 }$ off resonance, the contrast completely disappeared (Figure 4B). These results show the potential of mapping proteins inside a microorganism by IR photothermal microscopy.

To obtain the fingerprints of a single bacterium in both IR and Raman modes, we pinpointed the lasers to a single bacterium in the MIP image and acquired both IR photo thermal and Raman scattering spectra, as shown in Figure 4C. The IR photothermal spectrum shows strong peaks at 1650 $\mathrm { c m } ^ { - 1 }$ for the Amide I band, at $1 5 4 5 ~ \mathrm { { c m } ^ { - 1 } }$ for the Amide II, at

1245 $\mathrm { c m } ^ { - 1 }$ for Amide III, and at $1 0 8 5 ~ \mathrm { ~ c m ^ { - 1 } }$ for the phosphodioxy group $\mathrm { P O } _ { 2 } { } ^ { - }$ . These data indicate high concentrations of proteins and nucleic acids inside the S. aureus cell. The IR photothermal spectrum is validated by the FTIR spectrum (Figure 4D) from a bacterial film made of the same S. aureus strain. Notably, though FTIR has been used to study bacteria for decade s,38−40 this is the first time that infrared vibrational fingerprints of a single bacterium are recorded. A weak feature at $1 7 4 0 ~ \mathrm { c m } ^ { - 1 }$ is also exhibited, which is assigned to the ester functional groups from membrane lipids.41,42

The Raman spectrum from the same bacterium (Figure 4E) shows a strong signal in the C−H stretching vibration region and weaker bands in the fingerprint region. The strongest band peaked at $2 9 3 5 ~ \mathrm { { c m } ^ { - 1 } }$ is contributed by a superposition of the $\mathrm { C H } _ { 2 }$ symmetric and $\mathrm { C H } _ { 3 }$ antisymmetric vibrations from lipids, proteins, and carbohydrates.43 More detailed chemical compositions of nucleic acids and proteins are revealed in the fingerprint region. Nucleic acids are identified by Raman peaks at $\stackrel { \star } { 8 } 1 0 ~ \mathrm { c m } ^ { \simeq 1 }$ (for thymine, cytosine, and uracil), 1110 $\cdot \mathrm { c m } ^ { - 1 }$ (for phosphodioxy group $\mathrm { P O } _ { 2 } ^ { - } )$ , and $1 5 7 0 ~ \mathrm { { c m } ^ { - 1 } }$ (for guanine and adenine). Proteins are indicated by peaks corresponding to the Amide $\mathrm { ~ I ~ } \left( 1 6 5 6 \ \mathrm { c m } ^ { - 1 } \right)$ and Amide III (1254 cm−1 ) vibrations. In addition, there are additional Raman peaks corresponding mainly to amino acids containing phenyl groups, including phenylalanine (1021 and 1060 cm $^ { - 1 } ) . ^ { 4 4 , 4 5 }$ The $\mathrm { C H } _ { 2 }$ bending vibration at $1 4 4 9 ~ \mathrm { { c m } ^ { - 1 } }$ is contributed by both proteins and lipids. These measurements demonstrate that our IRaman microscope can provide rich chemical content information by fingerprinting a single bacterium in both IR and Raman modes.

We note that optical photothermal imaging and spectroscopy is now commercially available. With this said, what is presented here is different from the commercially available mIRage instrument. The mIRage machine uses a low-NA reflective Cassegrain objective to focus both the IR pump and the visible probe beams into a sample. While in our setup, the IR beam is focused to the sample by a Cassegrain objective and a counterpropagating visible probe beam is focused at the same spot by a water-immersion refractive objective (NA = 1.2). The spatial resolution of mid-infrared photothermal imaging is determined by the visible probe beam and the NA of the focusing objective. Consequently, the lateral spatial resolution of our setup has reached 290 nm, which is significantly higher than the mIRage setup (500 nm). Moreover, for Raman spetroscopy, the high-NA refractive objective can collect more photons compared to the Cassegrain objective. These advantages allowed us to acquire photothermal IR and Raman fingerprint spectra from a single bacterium within a few seconds. This analytical capability has not been reported elsewhere.

## CONCLUSION

We presented a novel microscope that is capable of mid infrared photothermal imaging, IR-specific fingerprint analysis, and full-window Raman spectral analysis. We further applied this instrument to chemical mapping and spectral analysis of single LDs in adipocytes and single bacteria. Important information in adipocytes, including lipid body abundance and size and degree of carbon chain unsaturation, is obtained. The contents of nucleic acids, proteins, and lipids in a single bacterium are identified by characteristic vibrational peaks. With the capacity of rapid IR photothermal imaging and IR/

Raman spectral analysis of a biological specimen on the same platform, the current work opens exciting opportunities of comprehensive vibrational spectroscopic analysis at submicrometer resolution for monitoring disease progression, testing antimicrobial susceptibility, and many other applications.

## ASSOCIATED CONTENT

## \*S Supporting Information

The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.analchem.9b02286.

Depth-resolved MIP imaging of 500 nm PMMA beads (PDF)

Depth-resolved MIP imaging of 500 nm PMMA beads at 1730 $\mathrm { c m } ^ { - 1 } \ \mathrm { ( A V I ) }$

## AUTHOR INFORMATION

## Corresponding Author

\*E-mail: jxcheng@bu.edu.

## ORCID

Ji-Xin Cheng: 0000-0002-5607-6683

## Author Contributions

J.X.C. conceived the idea. X.L. performed the experiments. X.L., D.Z., Y.B., and J.X.C. analyzed the data. The manuscript was written through contributions of all authors. All authors have given approval to the final version of the manuscript.

## Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

This work is supported by R43 EB027018 to J.X.C. X.L. acknowledges the financial support from the China Scholarship Council (No. 201704910707). J.L. and W.W. acknowledge the National Natural Science Foundation of China (61627819, 61575193). The authors thank Dr. Junjie Li and Pu-Ting Dong from the same group for the help of preparing the samples.

## REFERENCES

(1) Yue, S.; Li, J.; Lee, S.-Y.; Lee, H. J.; Shao, T.; Song, B.; Cheng, L.; Masterson, T. A.; Liu, X.; Ratliff, T. L.; Cheng, J.-X. Cell Metab. 2014, 19 (3), 393−406.  
(2) Jamieson, L. E.; Byrne, H. J. Vib. Spectrosc. 2017, 91 (7), 16−30.  
(3) Nallala, J.; Lloyd, G. R.; Shepherd, N.; Stone, N. Analyst 2016, 141, 630639.  
(4) Kumar, S.; Srinivasan, A.; Nikolajeff, F. Curr. Med. Chem. 2018, 25 (9), 1055−1072.  
(5) Cui, S.; Zhang, S.; Yue, S. J. Healthc Eng. 2018, 2018, 8619342.  
(6) Kong, K.; Kendall, C.; Stone, N.; Notingher, I. Adv. Drug Delivery Rev. 2015, 89, 121−134.  
(7) Baker, M. J.; Trevisan, J.; Bassan, P.; Bhargava, R.; Butler, H. J.; Dorling, K. M.; Fielden, P. R.; Fogarty, S. W.; Fullwood, N. J.; Heys, K. A.; Hughes, C.; Lasch, P.; Martin-Hirsch, P. L.; Obinaju, B.; Sockalingum, G. D.; Sule-Suso, J.; Strong, R. J.; Walsh, M. J.; Wood,́ B. R.; Gardner, P.; Martin, F. J. Nat. Protoc. 2014, 9, 1771−1791.  
(8) Levin, I.; Bhargava, R. Annu. Rev. Phys. Chem. 2005, 56, 429−74.  
(9) Dazzi, A.; Prater, C. B.; Hu, Q.; Chase, D. B.; Rabolt, J. F.; Marcott, C. Appl. Spectrosc. 2012, 66 (12), 1365−1384.  
(10) Dazzi, A.; Prater, C. B. Chem. Rev. 2017, 117 (7), 5146−5173. (11) Huth, F.; Govyadinov, A.; Amarie, S.; Nuansing, W.; Keilmann, F.; Hillenbrand, R. Nano Lett. 2012, 12, 3973−3978.  
(12) Perez-Guaita, D.; Kochan, K.; Batty, M.; Doerig, C.; Garcia Bustos, J.; Espinoza, S.; McNaughton, D.; Heraud, P.; Wood, B. R. Anal. Chem. 2018, 90, 3140−3148.  
(13) Zhang, D.; Li, C.; Zhang, C.; Slipchenko, M. N.; Eakins, G.; Cheng, J.-X. Sci. Adv. 2016, 2 (9), e1600521.  
(14) Li, C.; Zhang, D.; Slipchenko, M. N.; Cheng, J.-X. Anal. Chem. 2017, 89, 4863−4867.  
(15) Bai, Y.; Zhang, D.; Li, C.; Liu, C.; Cheng, J.-X. J. Phys. Chem. B 2017, 121, 10249−10255.  
(16) Li, Z.; Aleshire, K.; Kuno, M.; Hartland, G. V. J. Phys. Chem. B 2017, 121, 8838−8846.  
(17) Totachawattana, A.; Liu, H.; Mertiri, A.; Hong, M. K.; Erramilli, S.; Sander, M. Y. Opt. Lett. 2016, 41, 179−182.  
(18) Samolis, P.; Sander, M. Y. Opt. Express 2019, 27 (3), 2643− 2655.  
(19) Petry, R.; Schmitt, M.; Popp, J. ChemPhysChem 2003, 4, 14− 30.  
(20) van Manen, H.-J.; Kraan, Y. M.; Roos, D.; Otto, C. Proc. Natl. Acad. Sci. U. S. A. 2005, 102 (29), 10159−10164.  
(21) Evans, C. L.; Xie, X. S. Annu. Rev. Anal. Chem. 2008, 1, 883− 909.  
(22) Hong, W.; Liao, C.-S.; Zhao, H.; Younis, W.; Zhang, Y.; Seleem, M. N.; Cheng, J.-X. ChemistrySelect 2016, 1, 513−517.  
(23) Cheng, J.-X.; Xie, X. S. Science 2015, 350, 1054.  
(24) Prince, R. C.; Frontiera, R. R.; Potma, E. O. Chem. Rev. 2017, 117 (7), 5070−5094.  
(25) Wang, P.; Li, J.; Wang, P.; Hu, C.-R.; Zhang, D.; Sturek, M.; Cheng, J.-X. Angew. Chem., Int. Ed. 2013, 52, 13042−13046.  
(26) Lee, H. J.; Cheng, J.-X. Methods 2017, 128, 119−128.  
(27) Bunaciu, A. A.; Aboul-Enein, H. Y.; Fleschin, Ş. Appl. Spectrosc. Rev. 2015, 50, 176−191.  
(28) Harz, M.; Rösch, P.; Popp, J. Cytometry, Part A 2009 , 75A , 104−113.  
(29) Nallala, J.; Piot, O.; Diebold, M.-D.; Gobinet, C.; Bouche, O.; Manfait, M.; Sockalingum, G. D. Appl. Spectrosc. 2014, 68, 57−68.  
(30) Depciuch, J.; Kaznowska, E.; Zawlik, I.; Wojnarowska, R.; Cholewa, M.; Heraud, P.; Cebulski, J. Appl. Spectrosc. 2016, 70, 251− 263.  
(31) Perez-Guaita, D.; Kochan, K.; Martin, M.; Andrew, D. W.; Heraud, P.; Richards, J. S.; Wood, B. R. Vib. Spectrosc. 2017, 91, 46− 58.  
(32) Kochan, K.; Peng, H.; Wood, B. R.; Haritos, V. S. Biotechnol. Biofuels 2018, 11, 106.  
(33) Selvarajan, A. Proc. - Indian Acad. Sci., Sect. A 1966, 64 (1), 44− 55.  
(34) Rinia, H. A.; Burger, K. N. J.; Bonn, M.; Müller, M. Biophys. J. 2008, 95 (10), 4908−4914.  
(35) Heid, H.; Rickelt, S.; Zimbelmann, R.; Winter, S.; Schumacher, H.; Dörflinger, Y.; Kuhn, C.; Franke, W. W. PLoS One 2014, 9 (2), e90386.  
(36) Jamme, F.; Vindigni, J.-D.; Mechin, V.; Cherifi, T.; Chardot, T.;́ Froissard, M. PLoS One 2013, 8 (9), e74421.  
(37) Slipchenko, M. N.; Le, T. T.; Chen, H.; Cheng, J.-X. J. Phys. Chem. B 2009, 113, 7681−7686.  
(38) Naumann, D.; Helm, D.; Labischinski, H. Nature 1991, 351, 81−82.  
(39) Helm, D.; Labischinski, H.; Schallehn, G.; Naumann, D. J. J. Gen. Microbiol. 1991, 137, 69−79.  
(40) Quintelas, C.; Ferreira, E. C.; Lopes, J. A.; Sousa, C. Biotechnol. J. 2018, 13, 1700449.  
(41) Ojeda, J. J.; Dittrich, M. Methods Mol. Biol. 2012, 881, 187− 211.  
(42) Davis, R.; Mauer, L. J. Curr. Res. Technol. Educ Topics Appl. Microbiol Biotechnol. 2010, 2, 1582−94.  
(43) Neugebauer, U.; Schmid, U.; Baumann, K.; Ziebuhr, W.; Kozitskaya, S.; Deckert, V.; Schmitt, M.; Popp, J. ChemPhysChem 2007, 8, 124−137.  
(44) Notingher, I.; Verrier, S.; Romanska, H.; Bishop, A. E.; Polak, J. M.; Hench, L. L. Spectroscopy 2002, 16, 43−51.  
(45) Notingher, I. Sensors 2007, 7, 1343−1358.