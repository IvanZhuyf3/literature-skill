# Mid-infrared photothermal relaxation intensity diffraction tomography for video-rate volumetric chemical imaging

DANCHEN JIA,1,† DASHAN DONG,1,† TONGYU LI,1 HAONAN ZONG,1 JIABEI ZHU,1 XINYAN TENG,2 LEI TIAN,1,2,3 AND JI-XIN CHENG1,2,4

1Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, USA  
2Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, USA  
3leitian@bu.edu  
4jxcheng@bu.edu  
†These authors contributed equally.

Abstract: Three-dimensional molecular imaging of living cells is essential for unraveling cellular metabolism and response to therapies. However, existing volumetric methods, including fluorescence microscopy and quantitative phase imaging, either require fluorescent labels or lack chemical specificity. Mid-infrared (mid-IR) photothermal microscopy provides label-free spectroscopic contrast with sub-micrometer resolution but is limited by slow acquisition rates, precluding 3D live-cell studies. Here, we present a photothermal relaxation intensity diffraction tomography (PRIDT) system that encodes mid-IR absorption-induced refractive index changes via a photothermal relaxation scheme and recovers it through intensity diffraction tomography. PRIDT achieves video-rate volumetric chemical imaging with up to 15 Hz per wavelength and offers lateral and axial resolutions of 264 nm and 1.12 µm, respectively, within a volumetric field of view of $5 0 \times 5 0 \times 1 0 ~ \mu \mathrm { m } ^ { 3 }$ . We showcase high-speed PRIDT imaging of protein and lipid metabolism in ovarian cancer cells and lipid-droplet dynamics in live cells. PRIDT opens new avenues for rapid, quantitative, three-dimensional molecular imaging in living systems.

© 2026 Optica Publishing Group under the terms of the Optica Open Access Publishing Agreement

## 1. Introduction

Three-dimensional (3D) visualization of biological structures and functions at the subcellular level is essential for better understanding of biological processes such as cancer metabolism, drug response, and disease progression. Bright-field and phase-contrast microscopy offers basic morphological insights but lacks molecular information. Fluorescence microscopy addresses this limitation and has been developed with a range of 3D modalities, including confocal [1,2], two-photon [3,4], light-sheet [5,6,7], light-field [8,9]. Despite their high specificity and resolution, fluorescence microscopy require labeling, which complicates sample preparation, limits throughput, and may perturb native molecular functions.

Stimulated Raman scattering (SRS) and coherent anti-Stokes Raman scattering (CARS) have been widely used for label-free chemical imaging with bond specificity [10–13]. To further accelerate 3D SRS imaging, Bessel beam-based stimulated Raman projection tomography [14] and remote-focusing SRS microscope [15] have been introduced, enabling quantification of the total chemical composition of 3D biological specimens. More recently, the integration of SRS microscopy with expansion microscopy has enabled nanoscale 3D chemical imaging [16]. Despite these advances, the imaging speed of coherent Raman techniques remains fundamentally constrained by the intrinsically weak spontaneous Raman scattering cross-section of 10−30 cm2 for most biomolecules [17].

Infrared (IR) microscopy offers higher signal levels than Raman scattering due to its intrinsically stronger linear absorption cross-section of $1 0 ^ { - 1 8 } ~ \mathrm { c m } ^ { 2 }$ . Mid-infrared photothermal (MIP) microscopy employs a visible probe beam to detect IR absorption–induced refractive index changes, thus achieving 3D chemical imaging with sub-micrometer spatial resolutions in a scanning configuration [18–22], and enabling functional analysis in life science and material science [23–27]. Wide-field MIP microscopy improves MIP imaging speed using a virtual lock-in camera approach [28–31]. Wide-field infrared-excited fluorescence-detected microscopy further enables cellular imaging beyond video rate [32]. Furthermore, double-shot volumetric chemical imaging has been demonstrated by integrating fluorescence-detected MIP [33,34] with Fourier light field microscopy [34], while the chemical contrast here still relies on fluorescent labeling.

In parallel to chemical microscopy, quantitative phase imaging (QPI) has been developed to measure subtle phase shifts in transparent biological samples without labeling [35]. Optical diffraction tomography (ODT) extends QPI to three dimensions using multi-angle illumination [36–39]. However, the laser coherence required for ODT introduces strong speckle noise. Intensity diffraction tomography (IDT) has been demonstrated, enabling 3D refractive index reconstruction from intensity-only measurements with partially coherent illumination without speckle articles [40–42]. QPI enables noninvasive, high-resolution, long-term imaging of organelle dynamics, but its contrast arises from refractive-index variations lacking molecular specificity. To address this limitation, QPI and MIP microscopy are integrated to encode the chemical information of subcellular organelles into phase contrasts [43]. To further explore label-free volumetric chemical imaging, the MIP effect is incorporated into ODT [44,45] and IDT [46] to map chemicals in cells and C. elegans. Thus far, these methods have only been demonstrated on fixed samples in deuterium oxide, with a 3D chemical imaging speed limited to approximately 20 seconds per volume. Real-time imaging of living cells remains a challenge.

We recognize that volumetric MIP imaging in a wide-field configuration is fundamentally limited by the slow thermal relaxation dynamics of aqueous environments [47–49]. To overcome this limitation, we introduce photothermal relaxation intensity diffraction tomography (PRIDT) that decouples photothermal relaxation time from image acquisition speed through transient-state sampling. Specifically, this approach leverages the slow thermal relaxation of bulk water by introducing two fine-tuned pump–probe delay times to capture transient phase changes associated with the IR absorption of subcellular structures. Moreover, by precisely modulating laser pulse timing and fluence, PRIDT maintains thermal equilibrium near physiological temperatures, ensuring compatibility with live-cell imaging. We applied PRIDT to perform 3D mid-infrared hyperspectral imaging of cancer cells in the fingerprint region to investigate cancer metabolism. Azide-tagged fatty acids were used to visualize fatty acid uptake at the subcellular level. Finally, video-rate PRIDT imaging of lipid droplet dynamics in live cancer cells was achieved at 15 Hz per volume.

## 2. Results

## 2.1. PRIDT system

The PRIDT system is a dual-delay, pump-probe, multi-angle imaging system capable of volumetric chemical imaging at video-rate speed. Optical layout is shown in Fig. 1(a). Nanosecond mid-IR pulses $( 9 0 0 { - } 2 3 0 0 { \mathrm { c m } } ^ { - 1 } )$ serve as the pump beam. A custom-built ring-shaped array of 450-nm fiber-collimated laser diodes modulated into nanosecond pulses provides wide-field oblique illumination at $N _ { \mathrm { i l l u m } } = 1 6$ angles. The transmitted probe light, modulated by the sample’s photothermal response, is collected by a 60× water-immersion objective with an adjustable aperture to match the illumination numerical aperture (NA) of 0.9 (see Methods). To sustain high signal-to-noise ratio (SNR) at the short exposures required for the high-speed imaging, we use a camera with 2-million-electron full-well capacity. A kHz-frame-rate camera $( f _ { \mathrm { c a m e r a } } \leq 1$ kHz) operation, yielding a volumetric imaging speed of $f _ { \mathrm { c a m e r a } } / 2 N _ { \mathrm { i l l u m } }$ .

![](images/a7d047ccd77904e6f962374310f524de2fd96ebcc88018da5e8d9e26912aec12.jpg)  
Fig. 1. PRIDT system design, timing diagram and data pipeline. (a) Schematic of the PRIDT setup, consisting of a nanosecond mid-IR quantum cascade laser (QCL) pump laser, a multi-angle laser diode ring array for tomographic visible probe illumination, and a kHz-frame-rate camera. (b) Thermal dynamics of PRIDT: left, thermo-equilibrium at an elevated environmental temperature T0; right, absorber (red) and medium (gray) responses within a single pump–probe cycle. (c) Timing diagram of mid-IR pump, visible probe and camera exposure synchronized to capture two thermal relaxation states at delays $\mathrm { t } _ { 1 }$ and $\mathbf { t } _ { 2 } .$ The time difference of the pump-probe delay between the two delay windows $\left( \ t _ { 1 } - \ t _ { 2 } \right)$ is 8 µs when the probe repetition rate is 50 kHz. (d) Image acquisition and reconstruction pipeline: 16-angle illumination images recorded at two delays, IDT volumes reconstructed at each state, and PRIDT volume retrieved by subtracting the two IDT reconstructions.

Considering that the thermal relaxation time of bulk water is on the millisecond time-scale, a slow laser repetition rate ( 1 kHz) would favor virtual lock-in detection of purely transient <photothermal signals (see Supplement 1, Fig. S1a) [45]. In our practice, however, filling the camera’s full-well without excessive per-pulse energy necessitates a high probe repetition rate; we therefore operated probe at 50 kHz with 500-ns pulses, which also mitigates pulse-to-pulse fluctuations. Under these conditions, cumulative water heating dominates the bond-specific transients (see Supplement 1, Fig. S1b). To recover chemically selective contrast, we implement a photothermal relaxation scheme [Fig. 1(b)]. After previous millisecond-scale heating the sample reaches a quasi-steady baseline temperature $T _ { 0 }$ , further absorption from the mid-IR pump pulses induce same transient local temperature rises of the molecular absorbers and water, followed by heat dissipation into the surrounding medium. This relaxation leads to distinct temporal signatures between absorbers (red) and the background medium (gray), due to the differences in the thermal conductivity and heat capacity of the materials. Thus, mid-IR absorption of the target absorbers $( I _ { \mathrm { a b s } } )$ can be extracted by subtraction of the photothermal signals at two temporal states $( I _ { t 1 }$ , red window; $I _ { t 2 } .$ , gray window), where the temperature of the background medium remains the same.

$$
I _ {\text { abs }} \propto \Delta T _ {\text { abs }} - \Delta T _ {\text { medium }} = S _ {1} - S _ {2} = I _ {t _ {1}} - I _ {t _ {2}} \tag {1}
$$

Here, $\Delta T _ { a b s }$ is the temperature rise from mid-IR absorption by the absorbers, and $\Delta T _ { \mathrm { m e d i u m } }$ is the temperature rise of the surrounding medium induced due to mid-IR absorption of water and thermal diffusion in the surrounding medium.

To achieve video-rate volumetric imaging with this scheme, we use time-multiplexed acquisition [Fig. 1(c)]. The 16 probe angles illuminate sequentially while the pump alternates between chemical resonant states (t1) and reference states (t2). One volume is acquired in 32 frames, 16 for each state, enabling 15 volumes per second (see details in Methods). The data pipeline of PRIDT is outlined in Fig. 1(d). Raw probe images are collected from 16 incident angles and two delay states. Each 16-angle IDT dataset is used to perform tomographic reconstruction of refractive index (RI) distributions via the transfer function-based IDT reconstruction41. Incorporating photothermal relaxation dynamics at each angle further provides chemically selective volumetric reconstructions with PRIDT.

## 2.2. Thermal dynamics and spectroscopic imaging of polymer beads

To demonstrate the volumetric chemical imaging capability with PRIDT, we first characterized the transient photothermal response of polymer microspheres embedded in water. Figure 2(a) shows the temporal evolution of the refractive index change (∆n) following mid-IR excitation, measured by scanning the dual pump–probe delay windows between resonant states and reference states $t _ { 1 } \textrm { - } t _ { 2 }$ [illustrated in Fig. 1(b) and 1(c)]. To accommodate the camera frame rate (1 kHz) with nanosecond-scale photothermal relaxation, a multiplexed pulse generator was utilized to trigger the mid-IR laser and camera from the probe laser array driver’s 100 kHz master clock. PMMA microspheres with a diameter of 2 µm exhibited a rapid thermal rise and subsequent relaxation with a time constant of 2.5 µs, whereas the water background showed a slower thermal response, demonstrating the capability of suppressing water background with the dual-delay method. The extracted spectral response [Fig. 2(b); see Data File 1] revealed a strong absorption peak at $1 7 2 8 \mathrm { c m } ^ { - 1 }$ , consistent with the C = O stretching mode of PMMA, confirming chemical specificity of the PRIDT signal.

We further evaluated 3D chemical imaging performance in Fig. 2(c) and 2(d). IDT images at multiple axial planes (z = 0 to 1.2 µm) captured the structural distribution of the PMMA microspheres but lacked chemical selectivity. PRIDT reconstructions at corresponding depths revealed clear localization of PMMA beads with strong photothermal contrast, enabling chemical distinction from the surrounding medium [Fig. 2(d)]. The reconstructed images suffer from missing-cone artifacts (Fig. S2a). To assess resolution and sensitivity, we imaged PMMA nanospheres with a diameter of 200 nm (Fig. S2b). We further quantified the spatial resolution of IDT [Fig. 2(e)] and PRIDT [Fig. 2(f)]. Line profiles across isolated particles demonstrated lateral and axial full-width half-maximums (FWHM) of 264 nm and 1.12 µm, respectively, governed by optical diffraction limit and photothermal diffusion length (see details in Supplement 1). These results establish PRIDT as a label-free platform for volumetric, chemically specific imaging with sub-micrometer spatial resolution.

## 2.3. Fingerprint-region spectroscopic imaging of cancer cells

We applied PRIDT to map the chemically resolved subcellular composition of fixed OVCAR- 5 ovarian cancer cells. 3D IDT reconstructions across multiple depths [ Fig. 3(a)] revealed the subcellular morphology but lacked molecular specificity. By contrast, PRIDT reconstructions at protein and lipid vibrational bands [Fig. 3(b) and 3(c)] provided chemically selective volumetric maps. Hyperspectral image data processing was performed by a least-squares fitting algorithm detailed in Methods section. Protein signals were observed throughout the cytoplasmic region, whereas lipid contrast were localized to lipid droplets.

![](images/9795ffbd295147521b1d4899827267c274caf759c557227f564bec9ce2e588a4.jpg)

<details>
<summary>line chart</summary>

| x    | PMMA       | Water      |
| ---- | ---------- | ---------- |
| 0    | 0.0        | 0.0        |
| 1000 | 3.0e-4     | 1.2e-4     |
| 2000 | 2.5e-4     | 1.1e-4     |
| 3000 | 1.8e-4     | 1.0e-4     |
| 4000 | 1.2e-4     | 0.8e-4     |
| 5000 | 8.0e-5     | 0.6e-4     |
| 6000 | 4.0e-5     | 0.4e-4     |
</details>

![](images/fbc5dd055ca960d98b25ed4006083416649dfa914cc7c00fa6497dc9ff83a470.jpg)

<details>
<summary>natural_image</summary>

Microscopic images of IDT particles at four different z positions (0 μm, 0.4 μm, 0.8 μm, 1.2 μm), with color scale indicating n values (1.31–1.38)
</details>

![](images/f2130f0a4296960672ca7e334deed66172f6f44eea6093e526a678c785c00053.jpg)

<details>
<summary>line chart</summary>

(b) Delay time (ns)
| Wavenumber (cm⁻¹) | ROI 1 (×10⁻⁴) | ROI 2 (×10⁻⁴) | ROI 3 (×10⁻⁴) |
|---|---|---|---|
| 1700 | ~1.0 | ~1.2 | ~1.0 |
| 1720 | ~3.5 | ~3.0 | ~2.0 |
| 1740 | ~2.8 | ~2.5 | ~1.8 |
| 1760 | ~0.8 | ~0.6 | ~0.4 |
| 1780 | ~0.2 | ~0.1 | ~0.1 |
| 1800 | ~0.1 | ~0.1 | ~0.1 |
</details>

![](images/bcef7a0f8a2446619fefe68c45b15b706811705df317c6e1c11183d029ef8a3d.jpg)

<details>
<summary>text_image</summary>

(d)
z = 0 µm
z = 0.4 µm
z = 0.8 µm
z = 1.2 µm
PRIDT
0
8×10⁻⁴
Δn
2×10⁻⁴
</details>

![](images/00702f0b3bc19be5c58db53c04d664dab8fd08a808b3cba2943460858e14aef1.jpg)

<details>
<summary>line chart</summary>

| x (μm) | η     |
| ------ | ------- |
| -0.5   | 1.33    |
| 0      | 1.336   |
| 0.5    | 1.33    |
</details>

![](images/20f31c0191c1adc43c609a66f91a17979763022f6c9b180b685be04905264ce1.jpg)

<details>
<summary>line chart</summary>

| z (μm) | Value   |
| ------ | ------- |
| -0.8   | 1.333   |
| -0.6   | 1.335   |
| -0.4   | 1.337   |
| -0.2   | 1.337   |
| 0.0    | 1.337   |
| 0.2    | 1.335   |
| 0.4    | 1.333   |
| 0.6    | 1.332   |
| 0.8    | 1.331   |
</details>

![](images/c25e5a65882a63c8418c20c31e97da5c2e618dc09779f814045ebb4d7da36dbe.jpg)

<details>
<summary>line chart</summary>

| x (μm) | Δn (×10⁻⁶) |
|---|---|
| -0.5 | 0 |
| -0.25 | 1 |
| 0 | 9 |
| 0.25 | 2 |
| 0.5 | 0 |
The inset image shows a blue-and-white photo of a particle at 5×10⁻⁵ nm scale. The left chart displays Δn versus x (μm), while the right chart shows Δn versus z (μm). Both charts share the same x-axis label '264 nm' but differ in y-axis scale and position.
</details>

Fig. 2. Thermal dynamics, spectral response and image reconstruction of PMMA beads in water. (a) Thermal dynamics of 2 µm-diameter PMMA beads in water (red, PMMA; gray, water; curves fitted by the convolution of the Gaussian instrumental response function and the exponential decay function of the sample). (b) Spectra of PMMA beads (peak at $1 7 2 8 \mathrm { c m } ^ { - 1 } )$ indicated by white arrows in the PRIDT image of (d). (c, d) Depth-resolved IDT (c) and PRIDT (d) reconstructions of µm-diameter PMMA beads in water. Scale bar, 5 µm. (e, f) Line profiles of IDT (e) and PRIDT (f) of 200 nm-diameter PMMA beads (highlighted by yellow arrows), with the full width at half maximum (FWHM) marked. Scale bar, 1 µm.

To further validate spectral fidelity, we extracted hyperspectral PRIDT responses from different regions of interest (ROIs). Spectra obtained from protein-rich regions [Fig. 3(d); see Data File 2] exhibited two peaks around $1 5 5 2 \mathrm { c m } ^ { - 1 }$ and $1 6 5 6 \mathrm { c m } ^ { - 1 }$ , corresponding to the amide II and amide I vibrational band, characteristic of cellular protein with -helix secondary structures. In contrast, spectra from lipid-rich regions [Fig. 3(e); Data File 3] showed a pronounced absorption peak at $1 7 4 4 \mathrm { c m } ^ { - 1 }$ , consistent with the C = O stretching mode of lipid esters. These spectral features match established biochemical fingerprints, confirming the molecular contrast provided by PRIDT. Together, these results demonstrate that PRIDT enables volumetric label-free chemical imaging of cancer cells with subcellular spatial resolution, highlighting its potential for biochemical mapping of cellular architecture in 3D and to study protein and lipid metabolisms in a label-free manner.

## 2.4. Imaging fatty acid uptake with PRIDT

So far, we have shown that PRIDT is capable of distinguishing intrinsic molecules inside cells. Here, we further investigated lipid synthesis in cancer cells using a biorthogonal chemical reporter introduced through metabolic incorporation of azide-tagged fatty acids [50,51]. These bio-orthogonal tags are widely used to probe dynamic metabolic processes without perturbing native cellular functions. Bai et al. demonstrated MIP imaging of azide-tagged fatty acids in primary neurons [52]. Here, PRIDT reconstructions [ Fig. 4(a) and 4(b)] revealed cellular morphology and 3D distribution of lipids at C = O vibrational band, which concentrated within lipid droplets. Concurrently, PRIDT also resolved signals at the azide vibrational band [Fig. 4(c)] of $2 0 9 6 \mathrm { c m } ^ { - 1 }$ , with spectral fidelity confirmed in Fig. 4(d) and 4(e). These signals co-localized with lipid droplet regions, confirming the intake of exogenous fatty acids into intracellular lipid pools. The azide contrast further demonstrates the ability of PRIDT to detect non-native vibrational signatures with high sensitivity.

![](images/2f4c27c0a51476405ead9d69394652d2d3799a131ebbff059cf9151d0ab5f226.jpg)

<details>
<summary>text_image</summary>

(a)
IDT
(b)
Protein
(c)
Lipid
z = 0 µm
z = 0.4 µm
z = 0.8 µm
1.31 n 1.38 1×10⁻⁴ Δn 8×10⁻⁴ 1×10⁻⁴ Δn 8×10⁻⁴
</details>

![](images/955c73f74728a810c15abbbd80b5c6ff55d41173fcde68d1a679b6dc091485de.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | ROI 1     | ROI 2     | ROI 3     |
| ----------------- | --------- | --------- | --------- |
| 1500              | ~0.4      | ~0.2      | ~0.1      |
| 1550              | ~0.7      | ~0.6      | ~0.5      |
| 1600              | ~0.5      | ~0.8      | ~0.4      |
| 1650              | ~1.3      | ~1.5      | ~1.6      |
| 1700              | ~0.1      | ~0.3      | ~0.2      |
| 1750              | ~0.0      | ~0.5      | ~0.4      |
| 1800              | ~0.0      | ~0.0      | ~0.0      |
</details>

![](images/89fd4512119a7eff6a7edc683174eb8e4adabef5a50e6ff7683ec897ad1564a4.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | ROI 1     | ROI 2     | ROI 3     |
| ----------------- | --------- | --------- | --------- |
| 1500              | ~0        | ~0        | ~0        |
| 1550              | ~0        | ~0        | ~0        |
| 1600              | ~0        | ~0        | ~0        |
| 1650              | ~0.2      | ~0.1      | ~0.1      |
| 1700              | ~0.4      | ~0.3      | ~0.2      |
| 1750              | ~2.5      | ~3.5      | ~3.3      |
| 1800              | ~0        | ~0        | ~0        |
</details>

Fig. 3. Hyperspectral imaging of fixed cancer cells. (a–c) IDT and PRIDT reconstructions showing 3D chemical maps of proteins (blue) and lipids (hot) in fixed OVCAR-5 cells. Scale bar, 5 µm. (d, e) Representative spectra from ROIs enriched in protein (peaks at $1 6 5 6 \mathrm { c m } ^ { - 1 }$ and $1 5 5 2 \mathrm { c m } ^ { - 1 }$ , corresponding to Amide I and Amide II) and lipid ester (peak at $1 7 4 4 \mathrm { c m } ^ { - 1 } )$

As a control, cells without azido-fatty acid treatment exhibited lipid droplet signals but no detectable azide signal [Fig. 4(f–h)], confirming the capability of chemical tracking of PRIDT. Statistical analysis of fatty acid uptake was shown in Fig. 4(i), where the mean intensities of lipid and azide signals were compared to quantify the lipid synthesis from exogenous treatment and endogenous pathways. These results demonstrate that PRIDT enables volumetric monitoring of lipid metabolism in cancer cells, providing an approach for tracing diverse biochemical pathways with three-dimensional subcellular spatial resolution. Moreover, many pharmacological agents contain azide functional groups, such as antiviral azidothymidine as an HIV reverse transcriptase inhibitor [53,54]. Thus, PRIDT could be further extended to track drug uptake and intracellular distribution at the subcellular level, offering insights for drug discovery and development.

## 2.5. Temperature rise in PRIDT

In PRIDT imaging of living cells, elevated temperatures by water heating raise concerns about potential cytotoxicity. To assess this, we first conducted numerical simulations of heat accumulation in bulky water using a simplified 3D finite element model in COMSOL (see Supplementary Information). The model included a 500-nm PMMA particle located at the

![](images/1d079683796d5328a9dc34dbaab3318a014ccc08ba0503937451313df9edf138.jpg)  
Fig. 4. Fatty acid uptake in fixed cancer cells treated with azide-tagged fatty acids. (a–c) IDT (a) and PRIDT images at the lipid (b) and azide (c) channels, shown at different depths of OVCAR-5 cells treated with azide-tagged fatty acids. (d, e) Representative spectra of lipid (peak at $1 7 4 4 \mathrm { c m } ^ { - 1 } )$ and azide (peak at $2 0 9 6 \mathrm { c m } ^ { - 1 } )$ signals. (f–h) IDT (f) and PRIDT images at the lipid (g) and azide (h) channels for cells without azide treatment (control group). (i) Statistical analysis of the mean lipid (left) and azide (right) signal intensities comparing the experimental and control groups. Error bars, standard deviations of the normalized signal intensities. Scale bar, 5 µm.

CaF2–water interface. As shown in Fig. 5(a), increasing the IR laser repetition rate from 20 kHz to 50 kHz resulted in a rise in equilibrium water temperature from $2 5 ^ { \circ } \mathrm { C } \mathrm { t o } 3 2 ^ { \circ } \mathrm { C }$ .

To experimentally validate the temperature changes in aqueous cellular environment during PRIDT imaging, we employed FITC-based fluorescence thermometry under the same mid-IR heating conditions (see Methods) [55]. The temperature sensitivity of FITC fluorescence was calibrated to be 1.8% per °C using a heating plate and a precision thermometer (see Supplement 1, Fig. S3). The cellular temperature was then inferred from the decrease in fluorescence intensity [Fig. 5(b)]. The temperature distribution followed the spatial profile of the mid-IR heating beam, with measured temperatures in bulk water reaching ${ \sim } 2 6 ~ ^ { \circ } \mathrm { C }$ under 20 kHz heating pulses and ${ \sim } 3 3 ~ ^ { \circ } \mathrm { C }$ under 50 kHz, at the water absorption peak $( 1 6 4 0 \mathrm { c m } ^ { - 1 } )$ . We further extended the measurements across the fingerprint spectral region (see Supplement 1, Fig. S3). These in situ thermometry results confirm that PRIDT imaging elevates the medium temperature to a range close to physiological conditions, which is essential for preserving cellular function and viability.

## 2.6. 3D imaging of lipid dynamics in live cells

To demonstrate video-rate volumetric chemical imaging in living systems, we applied PRIDT to monitor lipid droplet dynamics in cultured cancer cells at a speed of 15 volumes per second.

(a)  
![](images/269708934ab80ba54b003a08140771b4fcc8fc8fc9044496a699a0ae6868b59a.jpg)

![](images/eeaebe7ce5186d4febaca766c00b4328ca29584a22228d8073e053d4c048288b.jpg)

(b)  
![](images/e8ce75f4680a9aaf955a41fae1b6387ea8592a2fbf5781f4ed7c00fb7ebf6573.jpg)

![](images/6e040b264bf63a2757768d08dbdbcde1c77d2170009234e668abd2c5e5644058.jpg)

![](images/e115c453703cce1d66c7365d2e6e55b583773e2ffe3dff150635cc7015a61bfc.jpg)

![](images/24b64b89e90d73cf15d86e860ba1f47f3d0b6be607fec830b6d55d88ad30bd2f.jpg)

(c)  
![](images/25e5f96c373f0c5c519ec74e73efde662d7601a7513969a9f56551cd8e5e56b7.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a textured surface with a highlighted region and scale bar (no text or symbols)
</details>

![](images/0ede80e4a58c3283c948252971fc0b3f68a8912639cdb1f7e688bed4d4493e57.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing scattered red fluorescent spots on a black background, with a yellow arrow pointing to a specific region (no text or symbols present)
</details>

![](images/88f54a8b870fca58dd75f189243e1a995912ba869b6790e5302e613117e9aad4.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescently labeled cellular structures with a color scale bar (ranging from -1.2 μm to 1.6 μm) and z-axis label (no text or symbols beyond color indicators)
</details>

(d)  
![](images/cdd0facd4419743849ddc059c7967be69c3f07eaa4079736deeb95099df51723.jpg)

![](images/81a86df80a636e541630f87bfdf02131f3d77e3ba7defdcb5d51428c6a5113ff.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing cellular changes at 2 min and 3 min (no text or symbols present)
</details>

![](images/fd62bc6a089037bcaf7f693c53a1b1f61dd301ef5adf697400f451cda731723d.jpg)

(e)  
![](images/49efb4d3c65d05474e703f738dd999a9d41702a896867d4468f83ec4caf13ca1.jpg)

<details>
<summary>natural_image</summary>

Microscopic grayscale image showing granular texture with a blue dashed square highlighting a region, scale bar indicates 1.31–1.38 (no text or symbols beyond measurement markers)
</details>

![](images/42a0d7fe7b7002635889aedfb21eb875346764c093deb33e5c312b7c6f59b884.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-labeled cellular structures with a color scale bar indicating Δn (no text or symbols present)
</details>

![](images/ffc435cddacdf1a49b9ad8fb40c767c1aafc949e2a802b1c4183a67a33442669.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular structures with two yellow arrows pointing to specific regions (no text or symbols present)
</details>

(f)  
![](images/732b82c3b5c76c12c1436148a1e4bef83a53cc5d9cb325b0d8874949b8901b8f.jpg)

![](images/93cdc10f722aa568323b82221f6e77788860cde6497dbf6229284093492a39a6.jpg)

<details>
<summary>natural_image</summary>

Four-panel scientific image showing cellular or molecular structures at 10 s and 20 s (no text or symbols present)
</details>

![](images/3c803e05716f4e212fc29e6e5fe4bb1ddce55c2d6cdaddefb025320f07acf80f.jpg)  
Fig. 5. Temperature calibration and PRIDT video of living cells. (a) Simulated temperature maps of photothermal heating of a 500 nm-diameter PMMA bead in water at 20 kHz and 50 kHz. (b) Experimental temperature measurements of cancer cells under photothermal heating at 20 kHz (left) and 50 kHz (right) using thermo-sensitive fluorescence. Green: fluorescence maps; red: corresponding temperature maps. (c) Representative slices from IDT (left), PRIDT (middle), and the PRIDT z-stack color map of living OVCAR-5 cells. (d) Zoomed-in views of ROI from (c), highlighting lipid droplet dynamics on minute-scale. (e) Representative slices from IDT (left), PRIDT (middle), and their overlay of living OVCAR-5 cells. (f) Zoomed-in views of ROI from (e), showing lipid droplets dynamics on second-scale. Scale bar in (b, c, e), 5 µm; scale bar in (d, f), 1 µm.

BM4D denoising was applied to the reconstructed volumes, substantially improving the SNR to 25 dB while preserving structural features. SNR analysis of PRIDT images before and after denoising was compared in Fig. S4 with the method described in Supplement 1. Lipid droplets were clearly identified in the denoised IDT and PRIDT videos [Fig. 5(c), Visualization 1, Visualization 2, Visualization 3, Visualization 4]. In Fig. 5(d), we highlighted subcellular areas with evident droplet activity. To demonstrate the long-term cellular viability, we have shown the time-lapsed PRIDT of living OVCAR-5 cells for half an hour (see Supplement 1, Fig. S5). Notably, in the overlaid image [Fig. 5(e)], several high-refractive-index features did not correspond to lipid signals, likely attributed to lysosomes or other organelles highlighted with yellow arrows. This observation emphasized the chemical specificity of PRIDT over IDT, enabling differentiation between lipid droplets and other refractive subcellular structures.

Time-lapse imaging over 30 s revealed continuous droplet growth and trafficking. In the region highlighted in cyan, newly formed lipid droplets emerged and gradually increased in contrast, while adjacent droplets migrated along cytoplasmic tracks [Fig. 5(f), top]. Corresponding photothermal signals confirmed the chemical specificity of lipid components [Fig. 5(f), bottom, cyan arrows]. Additionally, shown in Supplement 1, Fig. S6 (green arrows), Visualization 5 and Visualization 6, droplet clusters displayed fusion events and dynamic redistribution within the cytoplasm. These observations illustrate the ability of PRIDT to resolve lipid droplet dynamics in 3D, with sufficient temporal resolution to capture subcellular trafficking in real time.

## 3. Conclusion and discussion

PRIDT pushed the volumetric imaging speed of label-free 3D vibrational microscopy to a video rate, achieving 15 Hz per volume, with a lateral resolution of 264 nm and an axial resolution of $1 . 1 2 \mu \mathrm { m } ,$ , and across a $5 0 \times 5 0 \times 1 0 \mu \mathrm { m } ^ { 3 }$ field of view defined by the mid-IR illumination profile. PRIDT add chemical selectivity to quantitative phase imaging, enabling chemically specific volumetric reconstruction. The photothermal relaxation detection method not only enhanced the 3D chemical imaging speed by 300 × compared with previously reported BS-IDT [46], but also preserved physiologically compatible temperatures within the sample environment, which is beneficial for live-cell studies. With these advances, we demonstrated label-free monitoring of cancer cell metabolism, including protein secondary structure and lipid droplet dynamics. Furthermore, PRIDT enabled visualization of fatty acid uptake using azide-tagged fatty acids, extending its ability of specific metabolic studies and drug screening in living cells.

Mechanistically, PRIDT leverages differences in photothermal relaxation between targets and their medium to suppress water background and isolate chemical contrast from target absorbers. Importantly, the photothermal relaxation readout enables high-repetition-rate ( 1 kHz) detection with sub-microsecond probe pulses, decoupling signal formation from single pulse energy and thus permitting the use of simpler, lower-cost laser diodes rather than high-energy pulsed sources. Operating at high repetition rates also averages laser intensity fluctuations to reduce laser noise, which improves sensitivity at video rates.

Several limitations and opportunities remain. Firstly, PRIDT relies on the distinct photothermal relaxation characteristics between target structures and their surrounding medium. Therefore, contrast is strongest for dense or high-absorption samples (e.g., lipid droplets, protein aggregates), whereas diffused molecules show weaker signals. Specifically, for spatially resolved objects such as polymer beads and subcellular structures, PRIDT provides quantitative chemical imaging, whereas for unresolved structures thermal diffusion may introduce nonlinearity (see details in Supplement 1). Secondly, the current transmission implementation constrains illumination NA by free space geometry. A reflection-mode PRIDT using water- or oil-immersion objectives could increase NA and improve spatial resolutions. Thirdly, extending the pump and probe wavelengths into short-wave infrared regime could increase the penetration depths for thicker specimens, enabling label-free tissue imaging in vivo.

## 4. Materials and methods

## 4.1. PRIDT instrumentation and synchronization

The PRIDT system integrates a mid-IR tunable quantum cascade laser (QCL) as the pump source, a custom-built 16-angle visible laser diode array as the probe illumination module, and a high-speed camera for synchronized image acquisition. The mid-IR pump beam was generated by a nanosecond QCL (Daylight Solutions, MIRcat), operating in the mid-IR regime. The output was directed through an off-axis parabolic mirror (Thorlabs, MPD019-P01, reflected focal length 25.4 mm) to loosely focus the beam onto the sample in a transmission geometry. The resulting mid-IR illumination area is approximately $5 0 \times 5 0 \mu \mathrm { m }$ . The QCL was operated at a repetition rate of 50 kHz with a pulse width of 500 ns, parameters optimized by thermal calibration to maximize photothermal signal contrast.

The probe illumination module is a 16-channel 450-nm laser diode array arranged in a ring-shaped 3D-printed frame, which enables evenly distributed oblique illumination from 16 azimuthal angles $( \mathrm { N A } = 0 . 9 )$ . Each laser diode was coupled into a multimode optical fiber $( \mathrm { N A } = 0 . 2 2$ , 105 µm core diameter) equipped with a fiber collimator (Thorlabs, F950FC-A) to deliver collimated probe light with sufficient power density. The transmitted light was collected by a water dipping objective (Olympus, LUMPLANFLN 60X) and a tube lens (TTL200-A, focal length 200 mm). To match the illumination NA, the back pupil plane was relayed using a 4-f system consisting of lenses with focal lengths of 180 mm and 300 mm. An adjustable aperture was placed at the relayed pupil plane to restrict the effective collection NA to 0.9. The 4-f system also provided the magnification required by spatial sampling rate determined by the camera pixel size of 12 µm.

The transmitted probe signals were recorded by a CMOS camera (Adimec Q-2HFW-CXP, full-well capacity 2 million electrons), operated at kilohertz frame rates to capture images across 16 illumination angles and two pump–probe delay states. The timing of all devices was synchronized by a custom-designed MATLAB automation program. A master clock generated by an Atmel microcontroller distributed sequential trigger pulses to the 16 probe lasers using a multiplexer. A pulse generator synchronized the pump and probe lasers with the camera, alternating between on-resonance-delay and off-resonance-delay states to encode photothermal modulation. The probe pulse width was set to 500 ns to match the thermal excitation and relaxation time scale. For the thermal dynamics measurements in Fig. 2, the experiments were conducted under a laser repetition rate of 100 kHz, where the time difference in the pump-probe delay between the two delay windows $\left( t _ { 1 } - t _ { 2 } \right)$ was 4 µs. To ensure cellular viability, as discussed in Section 2.5, cell imaging was performed at a laser repetition rate of 50 kHz, with a pump-probe delay time difference $\left( t _ { 1 } - t _ { 2 } \right)$ of 8 µs. Each camera frame accumulated 100 probe pulses to accommodate the camera well depth, which resulted in a camera frame rate of 500 Hz and a volumetric imaging speed of 15 Hz.

## 4.2. Image reconstruction

Under the first-Born approximation, the refractive index change ∆n of the scatters induced by photothermal heating modulated the transmitted probe light intensity [56]. For an oblique illumination at angle $\theta ,$ the transmitted intensity modulation captured by the camera is given by θconvolution of the 3D IDT transfer functions $H _ { \theta }$ and $\Delta n$ .

$$
\widetilde {\delta I _ {\theta}} (k _ {x}, k _ {y}) = \int H _ {\theta} (k _ {x}, k _ {y}, k _ {z}) \cdot \widetilde {\Delta n} (k _ {x}, k _ {y}, k _ {z}) d k _ {z} \tag {2}
$$

The IDT transfer function is

$$
H _ {\theta} (\mathbf {k}) = P \left(\mathbf {k} - \mathbf {k} _ {\mathbf {i n}}\right) \delta \left(| \mathbf {k} | - k _ {0}\right) \tag {3}
$$

Here, $\begin{array} { r } { \mathrm { P } ( \mathbf { k } ) = \csc \left( \frac { \sqrt { k _ { x } ^ { 2 } + k _ { y } ^ { 2 } } } { k _ { 0 } \mathrm { N A } } \right) } \end{array}$ is the pupil function under the incident wavevector of $\mathbf { k } _ { \mathbf { i n } }$ , and $k _ { 0 } = 2 \pi n _ { 0 } / \lambda$ is the wavenumber of the medium.

π λWith the measurements of 16 illumination angles at two delay states $( I _ { \theta } ^ { ( t ) } ( k _ { x } , k _ { y } ) )$ ), we performed θIDT reconstruction at each delay state. The 2D measurements were mapped into 3D k-space based on $k _ { z } = \ \sqrt { k _ { 0 } ^ { 2 } - ( k _ { x } \ + k _ { x , \theta } ) ^ { 2 } - ( k _ { y } \ + k _ { y , \theta } ) ^ { 2 } }$ . The 3D refractive index was then reconstructed using Tikhonov regularization [40,57].

$$
\widetilde {n ^ {(t)}} \left(k _ {x}, k _ {y}, k _ {z}\right) = \frac {\sum_ {\theta} H _ {\theta} ^ {*} \left(k _ {x} , k _ {y} , k _ {z}\right) \cdot \widetilde {I _ {\theta} ^ {(t)}} \left(k _ {x} , k _ {y}\right)}{\sum_ {\theta} \left| H _ {\theta} \left(k _ {x} , k _ {y} , k _ {z}\right) \right| ^ {2} + \lambda} \tag {4}
$$

Here,  is the Tikhonov regularization term to suppress noise. Finally, the PRIDT volume was obtained by subtracting the reconstructions at two delay states.

$$
\Delta n _ {P R I D T} (x, y, z) = n ^ {\left(t _ {1}\right)} (x, y, z) - n ^ {\left(t _ {2}\right)} (x, y, z) \tag {5}
$$

For hyperspectral imaging, this process was repeated at each QCL wavelength to generate volumetric chemical maps.

## 4.3. Cellular sample preparation

OVCAR5 cells were cultured in RPMI-1640 medium supplemented with 10% (v/v) fetal bovine serum (FBS) and 1% (v/v) penicillin-streptomycin (P/S) at $3 7 ~ ^ { \circ } \mathrm { C }$ in a humidified incubator containing 5% CO . For live-cell imaging, cells were seeded onto CaF slides and incubated overnight, followed by three washes with phosphate-buffered saline (PBS). A live-cell imaging buffer was used to maintain cellular activity during imaging. For azide-labeled samples, cells were first seeded on $\mathrm { C a F } _ { 2 }$ slides and incubated overnight in standard culture medium, then treated with azido-palmitic acid (final concentration: $5 0 \mu \mathrm { M } )$ in RPMI-1640 medium containing 1% (v/v) FBS and 1% (v/v) P/S for 24 h. After treatment, cells were washed three times with PBS and fixed with 4% formalin.

## 4.4. Temperature measurements

Temperature measurements were performed by a custom-built pump-probe imaging system incorporating thermo-sensitive fluorescence modulation as the probe. The setup used a counterpropagating geometry, with the pump laser pulses operating at the same repetition rate (50 kHz) and pulse width (500 ns) as in the PRIDT imaging configuration. The probe system was implemented by a wide-field fluorescence microscope with a 488-nm laser (Cobolt, 06-MLD), modulated to a pulse width of 500 ns as the excitation source, and the reflected probe fluorescence was recorded by a sCMOS camera (Andor, ZYLA-5.5-USB3- S). FITC dye was selected as the thermo-sensitive probe.

To calibrate the fluorescence thermo-sensitivity, FITC–water solutions were placed on a temperature-controlled plate. Fluorescence intensity was recorded while tuning the temperature, thus providing a calibration curve of the temperature-dependent fluorescence response. For in situ measurements of background heating induced by accumulated QCL excitation, the pump and probe were synchronized so that pump pulse trains alternated between “Hot” and “Cold” states. In the Hot states, the pump-probe delay was tuned to 18 µs to capture the residual thermal relaxation. The photothermal signals were then extracted by subtracting the Hot and Cold frames. Each camera frame integrated 1000 probe pulses, and 5 frames were averaged to improve the SNR. The fluorescence modulation was calibrated to account for photobleaching effects. Finally, the measured photothermal signals were converted into temperature rise using the pre-calibrated FITC thermo-sensitivity curve.

## 4.5. Hyperspectral data acquisition and processing

Hyperspectral data were collected by tuning the QCL wavelength to targeted molecular resonances. To synchronize wavelength tuning with multi-angle image acquisition, TTL signals were used as wavelength triggers to initiate each imaging cycle at a given wavenumber. At each QCL wavelength, 5 cycles of 32 camera frames were recorded and averaged to reconstruct the corresponding PRIDT volume. The wavelength scan introduced a dead time of approximately 200 ms between adjacent wavenumbers. The raw spectra (Data File 1, Data File 2 and Data File 3) were collected from 3 × 3-pixel ROIs indicated by the arrows in the corresponding PRIDT images. For applications requiring faster spectral acquisition, a continuous wavelength sweep mode without dead time can be used. During long image acquisition processes, there were motioninduced artifacts in the surrounding medium. To mitigate these artifacts in the hyperspectral image stacks and attain quantitative chemical abundance maps, we applied a least-square unmixing method.

$$
\mathbf {I} (x, y, z) = \sum_ {i} a _ {i} (x, y, z) \mathbf {e} _ {i} + \varepsilon \tag {6}
$$

Here, $\mathbf { I } _ { x , y , z }$ is the pixel-wise spectrum, ei represents the normalized spectral basis vectors within the wavelengths of interest, ai is the quantitative chemical abundance map to be retrieved, and  accounts for residual signals from noise or other chemical contents. Then, abundance maps were recovered by solving a least-square problem.

$$
a _ {i} (x, y, z) = \arg \min _ {a} \left| \left| \mathbf {I} (x, y, z) - \mathbf {E} \cdot a \right| \right| ^ {2} \tag {7}
$$

Here, E is a matrix that contains all normalized spectral basis vectors of interest. The hyperspectral depth-resolved image stacks were reconstructed as the calculated abundance distributions.

## 4.6. Video data acquisition and processing

PRIDT video of living cells was recorded at single mid-IR excitation wavelength $( 1 7 4 4 \mathrm { c m } ^ { - 1 } )$ to match the C = O vibrations of lipid droplets. To achieve video-rate volumetric chemical imaging, each chemical volume was reconstructed directly from 32 camera frames without frame averaging. To suppress noise in the time-resolved volumetric data I (x, y, z, t), we applied the block-matching 4D (BM4D) filtering algorithm. For long time-lapse imaging, cells were recorded every 1 min for 1 h, with each acquisition consisting of 10 cycles (32 frames × 2 delay states).

Funding. Chan Zuckerberg Initiative (United States) (2023-321163).

Acknowledgment. The authors thank Dr. Qing Xia from Electrical and Computer Engineering Department at Boston University for providing the thermal sensitivity calibration of fluorescence, and Guo Chen from Electrical and Computer Engineering Department at Boston University for help with 3D printing of the probe laser holder.

Disclosures. The authors declare no conflicts of interest.

Author Contributions. J.-X.C. and L.T. conceived and supervised the project. D.J. and D.D. designed and built the PRIDT system. D.J. and T.L. developed and performed the image processing pipeline. H.Z. designed the illumination module. J.Z. contributed to the IDT reconstruction algorithm. X.T. provided the biological samples. D.J. wrote the manuscript with input from all authors.

Data availability. All data are available in the main text or the supplementary documents.

Supplemental document. See Supplement 1 for supporting content.

## References

1. J. W. Lichtman and J.-A. Conchello, “Fluorescence microscopy,” Nat. Methods 2(12), 910–919 (2005).  
2. R. H. Webb, “Confocal optical microscopy,” Rep. Prog. Phys. 59(3), 427–471 (1996).  
3. W. Denk, J. H. Strickler, and W. W. Webb, “Two-photon laser scanning fluorescence microscopy,” Science 248(4951), 73–76 (1990).  
4. F. Helmchen and W. Denk, “Deep tissue two-photon microscopy,” Nat. Methods 2(12), 932–940 (2005).  
5. J. Huisken, J. Swoger, F. Del Bene, et al., “Optical sectioning deep inside live embryos by selective plane illumination microscopy,” Science 305(5686), 1007–1009 (2004).  
6. P. J. Keller, A. D. Schmidt, J. Wittbrodt, et al., “Reconstruction of zebrafish early embryonic development by scanned light sheet microscopy,” Science 322(5904), 1065–1069 (2008).  
7. M. Tokunaga, N. Imamoto, and K. Sakata-Sogawa, “Highly inclined thin illumination enables clear single-molecule imaging in cells,” Nat. Methods 5(2), 159–161 (2008).  
8. M. Levoy, R. Ng, A. Adams, et al., “Light field microscopy,” ACM Trans. Graph. 25(3), 924–934 (2006).  
9. X. Hua, W. Liu, and S. Jia, “High-resolution Fourier light-field microscopy for volumetric multi-color live-cell imaging,” Optica 8(5), 614–620 (2021).  
10. J.-X. Cheng and X. S. Xie, “Vibrational spectroscopic imaging of living systems: An emerging platform for biology and medicine,” Science 350(6264), aaa8870 (2015).  
11. J.-X. Cheng and X. S. Xie, “Coherent anti-stokes raman scattering microscopy: instrumentation, theory, and applications,” J. Phys. Chem. B 108(3), 827–840 (2004).  
12. C. W. Freudiger, W. Min, B. G. Saar, et al., “Label-free biomedical imaging with high sensitivity by stimulated raman scattering microscopy,” Science 322(5909), 1857–1861 (2008).  
13. F. Hu, L. Shi, and W. Min, “Biological imaging of chemical bonds by stimulated Raman scattering microscopy,” Nat. Methods 16(9), 830–842 (2019).  
14. X. Chen, C. Zhang, P. Lin, et al., “Volumetric chemical imaging by stimulated Raman projection microscopy and tomography,” Nat. Commun. 8(1), 15117 (2017).  
15. P. Lin, H. Ni, H. Li, et al., “Volumetric chemical imaging in vivo by a remote-focusing stimulated Raman scattering microscope,” Opt. Express 28(20), 30210–30221 (2020).  
16. C. Qian, K. Miao, L.-E. Lin, et al., “Super-resolution label-free volumetric vibrational imaging,” Nat. Commun. 12(1), 3648 (2021).  
17. X. Gao, X. Li, and W. Min, “Absolute stimulated raman cross sections of molecules,” J. Phys. Chem. Lett. 14(24), 5701–5708 (2023).  
18. D. Zhang, C. Li, C. Zhang, et al., “Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution,” Sci. Adv. 2(9), e1600521 (2016).  
19. Z. Li, K. Aleshire, M. Kuno, et al., “Super-resolution far-field infrared imaging by photothermal heterodyne imaging,” J. Phys. Chem. B 121(37), 8838–8846 (2017).  
20. D. Zhang, L. Lan, Y. Bai, et al., “Bond-selective transient phase imaging via sensing of the infrared photothermal effect,” Light:Sci. Appl. 8(1), 116 (2019).  
21. P. D. Samolis and M. Y. Sander, “Phase-sensitive lock-in detection for high-contrast mid-infrared photothermal imaging with sub-diffraction limited resolution,” Opt. Express 27(3), 2643–2655 (2019).  
22. J. Yin, M. Zhang, Y. Tan, et al., “Video-rate mid-infrared photothermal imaging by single-pulse photothermal detection per pixel,” Sci. Adv. 9(24), eadg8814 (2023).  
23. Y. Bai, J. Yin, and J.-X. Cheng, “Bond-selective imaging by optically sensing the mid-infrared photothermal effect,” Sci. Adv. 7(20), eabg1559 (2021).  
24. Q. Xia, J. Yin, Z. Guo, et al., “Mid-infrared photothermal microscopy: principle, instru- mentation, and applications,” J. Phys. Chem. B 126(43), 8597–8613 (2022).  
25. X. Teng, M. Li, H. He, et al., “Mid-infrared photothermal imaging: instrument and life science applications,” Anal. Chem. 96(20), 7895–7906 (2024).  
26. R. Furstenberg, C. A. Kendziora, M. R. Papantonakis, et al., “Chemical imaging using infrared photothermal microspectroscopy,” Proc. SPIE 8374, 837411 (2012).  
27. K. Aleshire, I. M. Pavlovetc, R. Collette, et al., “Far-field midinfrared superresolution imaging and spectroscopy of single high aspect ratio gold nanowires,” Proc. Natl. Acad. Sci. U.S.A. 117(5), 2288–2293 (2020).  
28. Y. Bai, D. Zhang, L. Lan, et al., “Ultrafast chemical imaging by widefield photothermal sensing of infrared absorption,” Sci. Adv 5(7), eaav7127 (2019).  
29. H. Zong, C. Yurdakul, Y. Bai, et al., “Background-suppressed high-throughput mid-infrared photothermal microscopy via pupil engineering,” ACS Photonics 8(11), 3323–3336 (2021).  
30. M. Schnell, S. Mittal, K. Falahkheirkhah, et al., “All-digital histopathology by infrared-optical hybrid microscopy,” Proc. Natl. Acad. Sci. U.S.A. 117(7), 3388–3396 (2020).  
31. P. Fu, B. Chen, Y. Zhang, et al., “Breaking the diffraction limit in molecular imaging by structured illumination mid-infrared photothermal microscopy,” Adv. Photonics 7(03), 036003 (2025).  
32. D. Lee, H. Wang, P. A. Kocheril, et al., “Wide-field bond-selective fluorescence imaging: from single-molecule to cellular imaging beyond video rate,” Optica 12(2), 148–157 (2025).  
33. Y. Zhang, H. Zong, C. Zong, et al., “Fluorescence-detected mid-infrared photothermal microscopy,” J. Am. Chem. Soc. 143(30), 11490–11499 (2021).  
34. D. Jia, Y. Zhang, Q. Yang, et al., “3D chemical imaging by fluorescence-detected mid-infrared photothermal Fourier light field microscopy,” Chem. Biomed. Imaging 1(3), 260–267 (2023).  
35. G. Popescu, Quantitative Phase Imaging of Cells and Tissues (McGraw-Hill Education, 2011), 1st edition edn.  
36. W. Choi, C. Fang-Yen, K. Badizadegan, et al., “Tomographic phase microscopy,” Nat. Methods 4(9), 717–719 (2007).  
37. Y. Sung, W. Choi, C. Fang-Yen, et al., “Optical diffraction tomography for high resolution live cell imaging,” Opt. Express 17(1), 266–277 (2009).  
38. Y. Cotte, F. Toy, P. Jourdain, et al., “Marker-free phase nanoscopy,” Nat. Photonics 7(2), 113–117 (2013).  
39. D. Dong, X. Huang, L. Li, et al., “Super-resolution fluorescence-assisted diffraction computational tomography reveals the three-dimensional landscape of the cellular organelle interactome,” Light:Sci. Appl. 9(1), 11 (2020).  
40. R. Ling, W. Tahir, H.-Y. Lin, et al., “High-throughput intensity diffraction tomography with a computational microscope,” Biomed. Opt. Express 9(5), 2130–2141 (2018).  
41. J. Li, A. C. Matlock, Y. Li, et al., “High-speed in vitro intensity diffraction tomography,” Adv. Photonics 1(06), 066004 (2019).  
42. J. Li, N. Zhou, J. Sun, et al., “Transport of intensity diffraction tomography with non-interferometric synthetic aper ture for three-dimensional label-free microscopy,” Light:Sci. Appl. 11(1), 154 (2022).  
43. M. Tamamitsu, K. Toda, R. Horisaki, et al., “Quantitative phase imaging with molecular vibrational sensitivity,” Opt. Lett 44(15), 3729–3732 (2019).  
44. M. Tamamitsu, K. Toda, H. Shimada, et al., “Label-free biochemical quantitative phase imaging with mid-infrared photother- mal effect,” Optica 7(4), 359–366 (2020).  
45. M. Tamamitsu, K. Toda, M. Fukushima, et al., “Mid-infrared wide-field nanoscopy,” Nat. Photonics 18(7), 738–743 (2024).  
46. J. Zhao, A. Matlock, H. Zhu, et al., “Bond-selective intensity diffraction tomography,” Nat. Commun. 13(1), 7767 (2022).  
47. J. Yin, L. Lan, Y. Zhang, et al., “Nanosecond-resolution photothermal dynamic imaging via MHz digitization and match filtering,” Nat. Commun. 12(1), 7097 (2021).  
48. P. D. Samolis, X. Zhu, and M. Y. Sander, “Time-resolved mid-infrared photothermal microscopy for imaging water-embedded axon bundles,” Anal. Chem. 95(45), 16514–16521 (2023).  
49. R. Bolarinho, J. Yin, H. Ni, et al., “Background-free mid-infrared photothermal microscopy via single-shot measurement of thermal decay,” Anal. Chem. 97(8), 4299–4307 (2025).

## Optics EXPRESS

50. E. M. Sletten and C. R. Bertozzi, “Bioorthogonal chemistry: fishing for selectivity in a sea of functionality,” Angew. Chem., Int. Ed. 48(38), 6974–6998 (2009).  
51. H. C. Hang, E.-J. Geutjes, G. Grotenbreg, et al., “Chemical probes for the rapid detection of fatty-acylated proteins in mammalian cells,” J. Am. Chem. Soc. 129(10), 2744–2745 (2007).  
52. Y. Bai, C. M. Camargo, S. M. K. Glasauer, et al., “Single-cell mapping of lipid metabolites using an infrared probe in human-derived model systems,” Nat. Commun. 15(1), 350 (2024).  
53. E. De Clercq, “HIV resistance to reverse transcriptase inhibitors,” Biochem. Pharmacol. (Amsterdam, Neth.) 47(2), 155–169 (1994).  
54. E. De Clercq and G. Li, “Approved antiviral drugs over the past 50 Years,” Clin. Microbiol. Rev 29(3), 695–747 (2016).  
55. X. D. Wang, O. S. Wolfbeis, and R. J. Meier, “Luminescent probes and sensors for temperature,” Chem. Soc. Rev. 42(19), 7834–7869 (2013).  
56. E. Wolf, “Three-dimensional structure determination of semi-transparent objects from holographic data,” Opt. Commun. 1(4), 153–156 (1969).  
57. L. Tian and L. Waller, “3D intensity and phase imaging from light field measurements in an LED array microscope,” Optica 2(2), 104–111 (2015).