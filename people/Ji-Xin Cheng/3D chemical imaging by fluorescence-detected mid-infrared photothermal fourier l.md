pubs.acs.org/ChemBioImaging

Article

# 3D Chemical Imaging by Fluorescence-detected Mid-Infrared Photothermal Fourier Light Field Microscopy

Danchen Jia,‡ Yi Zhang,\*,‡ Qianwan Yang,‡ Yujia Xue, Yuying Tan, Zhongyue Guo, Meng Zhang, Lei Tian,\* and Ji-Xin Cheng\*

![](images/ae86db5b98c72acab2647525c703af0a525681e319f06b599f8c5b5eb3b3ba9a.jpg)

Cite This: Chem. Biomed. Imaging 2023, 1, 260−267

![](images/447577ecae46d6ca06ca1ef93ddb60bc2c1e81dc76179c188ec55b1885e23fc6.jpg)

Read Online

ACCESS

![](images/87d2c67331c18ccc7b80da7332c77aebb0b1e83f05890e1b8df973b9e03279ba.jpg)

Metrics & More

![](images/2249606005154edfdea858323bb6973777a934d22a2aec1ad2eede8a9191cbba.jpg)

Article Recommendations

![](images/c2bcff0c9502973368a61a3433170a992d0d08d20bfec9397daabdad84fe3d95.jpg)

Supporting Information

![](images/0b103813a4036be636c964c2ebec6f243f732d5da8baeabac3747b8a1a742133.jpg)

<details>
<summary>text_image</summary>

Probe
MIP signal
Pump
*
3D PSF
=
2D measurement
</details>

ABSTRACT: Three-dimensional molecular imaging of living organisms and cells plays a significant role in modern biology. Yet, current volumetric imaging modalities are largely fluorescence-based and thus lack chemical content information. Mid-infrared photothermal microscopy as a chemical imaging technology provides infrared spectroscopic information at submicrometer spatial resolution. Here, by harnessing thermosensitive fluorescent dyes to sense the mid-infrared photothermal effect, we demonstrate 3D fluorescence-detected mid-infrared photothermal Fourier light field (FMIP-FLF) microscopy at the speed of 8 volumes per second and submicron spatial resolution. Protein contents in bacteria and lipid droplets in living pancreatic cancer cells are visualized. Altered lipid metabolism in drug-resistant pancreatic cancer cells is observed with the FMIP-FLF microscope.

KEYWORDS: mid-infrared, volumetric imaging, photothermal, Fourier light field, lipid metabolism, chemical imaging

## 1. INTRODUCTION

Volumetric imaging plays a prominent role in life science due to its ability to visualize 3D architecture of biological systems ranging from whole-brain to subcellular level.1−3 Volumetric fluorescence imaging is routinely performed by optical sectioning and z-axis scanning with either confocal microscopy4 or two-photon laser scanning microscopy.5 However, these scanning-based approaches are time-consuming and require a precise mechanical 3D positioning device. In cases where photobleaching is a concern, repeated sectioning only exacerbates this problem by increasing exposure. Fast focus scanning methods using electrically tunable lens6 or spatial light modulator7 mitigate the issue by improving scanning speed, but hinder the imaging contrast due to a drawback of out-of-focus background. Light-sheet fluorescence microscopy physically eliminates the background by illuminating the sample only with a thin sheet of light from the side of the specimen for optical sectioning.8− -10 Also, the excitation is confined to the focal plane, thus boosting detection efficiency while reducing photobleaching and photodamage. Various scanning-based strategies discussed above promote the imaging speed of volumetric fluorescence imaging,11 but still cannot achieve video-rate due to the requirement of mechanical movement.

To further capture the fast-moving organelles or study dynamic activities in living cells, single-snapshot light field microscopy emerged as a scanning-free, scalable method that allows for high-speed, volumetric imaging.12 Specifically, a lenslet array is used to capture 3D structure of objects in a single snapshot. Recently developed Fourier light-field (FLF) microscopy achieved high-quality volumetric imaging by recording the light field in the Fourier domain, which allows jointly allocating the spatial and angular information on the incident light in a consistently non-overlapping manner, effectively avoiding any artifacts in conventional light field

Received: February 5, 2023

Revised: March 4, 2023

Accepted: March 8, 2023

Published: March 20. 2023

![](images/542f1089dc7bb8a0435f6c0a22b284f02261349b6fe4867493a7d534db8d95c1.jpg)

![](images/cafbedcdd9b0c0a85f5e2dea6dc4548d0e769acee775abfd75218b78683311f4.jpg)

<details>
<summary>text_image</summary>

(a)
(b)
MLA camera
TL
Iris
FL
Visible laser
DM
OL
sample
Chopper
Function Generator
Mid-IR laser
</details>

![](images/328134d059eafa2b07714f24d70abc5a907605faba8befeacdf6661fdb4382d2.jpg)

<details>
<summary>text_image</summary>

(c) i. Point-spread functions
z₁ z₂ z₃
ii. FMIP-FLF measurement
IR-off IR-on
</details>

![](images/92d2f711b146c0d5f7af8e49ec699cfe9074224a6f516d9baf4cc104607efdae.jpg)

<details>
<summary>text_image</summary>

iii. 3D Reconstruction
z₁
z₂
z₃
</details>

Figure 1. FMIP-FLF imaging system and procedures. (a) Principle of FMIP-FLF microscope. The modulated fluorescence emission carries IR information coded by mid-IR pulses. Each 2D snapshot contains 3D information introduced by a lenslet array placed at the Fourier plane. FL, Fourier lens. (b) Experimental setup. The pump beam is a nanosecond mid-IR laser, modulated by an optical chopper and weakly focused on the sample by a gold-coated parabolic mirror. The probe beam is a 520 nm nanosecond laser and sent through the lenslet array placed at the back focal plane of a FL. The tube lens and the FL formed a 4f system. OL, objective lens. DM, dichroic mirror. (c) Procedures of FMIP-FLF measurements. (i) Example measured PSFs of the system. (ii) Raw FMIP-FLF measurement contains a pair of IR-on and IR-off images. (iii) 3D FMIP-FLF reconstruction by deconvolution between 2D raw FMIP-FLF image and the measured PSFs. The samples were Rhodamine 6G stained Staphylococcus aureus (S. aureus) bacteria prepared on a tilted silicon substrate.

system s.13−16 These advances in both imaging capability and computation speed promise further development of FLF microscopy toward high-resolution, volumetric data acquisition, analysis, and observation at the video rate. However, these methods are fluorescence based, lacking the chemica content information about the subjects.

Vibrational spectroscopic imaging based on molecular fingerprints is able to offer chemical content and molecular structural information about an organism in a label-free manner.17 Along this direction, coherent Raman scattering microscopy has been developed and has found broad applications in revealing recording neural activities,18 cancer metastasis,19 brain metabolic activity,20 and so on. Bessel beam based Stimulated Raman projection tomography has been developed to quantify the total chemical composition of a 3D object.21 More recently, volumetric chemical imaging on the nanoscale is enabled by the integration of stimulated Raman scattering microscopy and expansion microscopy.22,23 Yet, the detection sensitivity of Raman based vibrational microscopy is ultimately limited by its small cross section.

The infrared absorption offers a cross section that is 8 orders of magnitude larger than Raman scattering. Yet, infrared microscopy lacks spatial resolution, which prohibits accurate decomposition of cellular dry mass density into independent biomolecular components. Recently developed mid-infrared photothermal (MIP) microscopy exceeds the diffraction limit of infrared microscopy and allows three-dimensional chemical imaging in a confocal scanning manner.24 To improve the 2D imaging speed and achieve large scale imaging, wide field MIP microscopy is demonstrated via a virtual lock-in camera approach.25 By measuring the mid-infrared photothermal effect in a quantitative phase microscope, both 2D and 3D bondselective phase imaging has been demonstrated.26−29 Yet, the speed (∼50 s per volume) is insufficient to capture chemical information in a highly dynamic living system.

Here, we present a fluorescence-detected mid-infrared photothermal Fourier light-field (FMIP-FLF) microscope that allows high-speed chemical imaging of living cells. We harness thermosensitive fluorescent dyes to sense the mid infrared photothermal effect.30,31 The fluorescence intensity can be modulated at the level of 1% per Kelvin by mid-IR absorption, which is 100 times larger than the thermal modulation of scattering intensity. Moreover, the fluorophores can target specific organelles or biomolecules, thus augmenting the specificity of photothermal imaging. Importantly, this method is fully compatible with the FLF fluorescence imaging. By recording photothermal modulation of fluorescence emission in an FLF microscope, we achieved a fluorescencedetected infrared spectroscopic imaging rate of 8 volumes per second. at a lateral resolution of 0.5 to 0.9 um and an axial resolution of 0.8 to 1.1 μm. This speed is faster than reported confocal MIP microscopy24 or MIP-based optical diffraction tomography28 by 2 orders of magnitude. With these advancements, we demonstrate high-speed volumetric bond-selective imaging in living cells, where the lipid content is used as a marker to determine the drug resistance of cancer cells.

![](images/271031fdfd7a9bc95e98313b1d3468aecfddabb32d3550d8b500d2154b1be79b.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing scattered pink and blue fluorescent spots against a black background, labeled (a)
</details>

![](images/025164c106c2798a1e795eda0dc0a2ee1d034461ad86b74e83cd03522fda5a6f.jpg)

<details>
<summary>scatterplot</summary>

| x    | y    | z    | Intensity |
|------|------|------|---------|
| (various) | (various) | (various) | (various) |
</details>

![](images/52470d1472f238d1c603aa5de278ff71946eaaef13291a2b87e03d21b3d5e67b.jpg)

<details>
<summary>natural_image</summary>

Vertical column of scattered purple and pink dots on black background with x, y, z axis indicators (no text or symbols)
</details>

![](images/d9579d4668be0879fb6ec1548cc5a3dcffa5398fdd5452845581633e99951ca8.jpg)

<details>
<summary>natural_image</summary>

Five labeled panels (i–v) showing colored dots on black background, no text or symbols present
</details>

![](images/4111c9a47992941d1bdc523fce38f49a14094facc668d9d40e53d90fd264db97.jpg)

<details>
<summary>text_image</summary>

z
x
</details>

![](images/54276eb786d3c0cd5bcf46ab8372a541aa0a267fa41cf36d1b20ce728632f93c.jpg)

<details>
<summary>scatterplot</summary>

| x (μm) | y (μm) |
| ------ | ------ |
| 0      | -2.8   |
| 2.8    | 0      |
| 2.8    | 2.8    |
</details>

![](images/a6917739f903ec4d438b1ebfdabf988b7270abb3b08ad743dfc4a02187d6bbd4.jpg)

<details>
<summary>natural_image</summary>

Two-panel scientific image showing scattered purple dots on black background, with scale bar labeled (d) and distance annotation z = 1.24 μm
</details>

![](images/1b9dbdc2d339fbf3fe8dc2c2b4334160e4ce4ac5ddcebcc8b56f32ff5e2ed801.jpg)

<details>
<summary>natural_image</summary>

Two-panel scientific image showing scattered bright spots against a black background, with scale bar labeled z = -0.31 μm (top panel)
</details>

![](images/3061a375450018dae8753c866b797445e5af6716d1fc34bc475aa27f32196303.jpg)

<details>
<summary>natural_image</summary>

Two-panel scientific image showing scattered bright spots on black background, with scale bar and red annotation (no readable text or symbols)
</details>

![](images/06d369ea2b24ce70257c474506a0f335aede4c7ce78f7256010ff603e71b8147.jpg)

<details>
<summary>scatterplot</summary>

| x (μm) | y (μm) |
| ------ | ------ |
| -2.8   | 0      |
| 0      | 0      |
| 2.8    | 0      |
</details>

![](images/609674e442d715f080d2b7d68cf46ca564a2d5f759efb230a9c326b6d6ca06a3.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing purple dots and a red dot on black background with scale bar (no text or symbols)
</details>

![](images/51b7e4fa51b842f51de30c505f4c578cbb6f105301ebe90ff10193609ed5e0b1.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered purple and red dots on a black background, with a scale bar at the bottom (no text or symbols)
</details>

![](images/5eead107cb747505c4ae4f2a247bf2194e13c2b58fbad9b8bf8acc9312e3eece.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered purple and red dots on a black background, with a scale bar and z-value label (2.34 μm) in the top right corner.
</details>

Figure 2. Characterization of FLF system with 175 nm fluorescent beads and FMIP-FLF system with S. aureus. (a) Raw FLF measurement, and (b) 3D reconstructed image of 175 nm fluorescent beads distributed in 3D agarose gel, and its x−z and y−z projection. The inset images (i−v) are zoomed-in images of (b) at $z = - 1 . 8$ to 1.0 μm, with fwhm of 0.5 to 0.9 μm and 0.8 to 1.1 μm in the lateral and axial direction, respectively (see Figure S1). (c) 3D reconstructed fluorescent beads and (d) zoomed-in reconstructed slices at varying depths and corresponding widefield images with the same FOV. (e) 3D reconstructed FLF image and (f) reconstructed FMIP images of varying depth at 1650 $\mathrm { c m } ^ { - 1 }$ of R6G stained S. aureus prepared on a tilted Si substrate. Scale bar, 20 μm; scale bar of (b) insets, 1 μm.

## 2. EXPERIMENTAL SECTION

## FMIP-FLF Microscope

The FMIP-FLF microscope is a pump and probe imaging system (Figure 1a). A pulsed visible probe beam passes through a FLF microscope to capture fluorescently labeled sample, while the IR absorption information is coded by a nanosecond pulsed mid-IR laser. The raw FMIP-FLF images are acquired by synchronizing the IR pump pulses, the visible probe pulses, and the camera exposure (Figure 1b). After acquiring each pair of “IR-on” and “IR-off” images, a 3D deconvolution is performed that incorporates the point spread function (PSF) to generate the final 3D chemical image (Figure 1c).

The schematic of the FMIP-FLF microscope is shown in Figure 1b. The infrared pulses are generated by a tunable optical parametric oscillator laser (Firefly-LW, M Squared Lasers), ranging from 1175 to 1800 cm−1 , operating at 20 kHz repetition rate 30 mW output power and 50 ns pulse duration. An optical chopper (MC2000B, Thorlabs) modulates the IR pulses to accommodate the acquisition speed of the camera. A gold-coated off-axis parabolic mirror with a focal length of 25.4 mm weakly focuses the pump beam at the sample with the power of 20 mW across the $6 0 \times 6 0$ μ 2

On the FLF microscope, a 2 × 2 lenslet array is used to image the 3D fluorescence as 2 × 2 projection views on the camera plane. Since $\begin{array} { r } { R _ { x y } = \frac { \lambda N } { 2 \mathrm { N A } } , } \end{array}$ 2NA , small occupancy ratio N of the lenslet array and large numerical aperture NA of the objective are desired. The FLF imaging is implemented on an epifluorescence microscope using a 100×, 0.95NA objective lens (PLFLN100X; PLAN FLUOR 100X DRY OBJ, NA 0.95, WD 0.2). The samples are excited with a 520 nm nanosecond laser (NPL52C, Thorlabs) at 20 kHz repetition rate. The visible laser is focused on the back pupil plane of the objective and illuminates the sample with the average power of 5 mW across 100 × 100 $\mu \mathrm { m } ^ { 2 } .$ . The generated fluorescence emission is collected with a dichroic mirror (DMLP550T, Thorlabs), a 550 nm long-pass filter (FEL0550, Thorlabs) and a tube lens (TTL180-A, Thorlabs). The field of view (FOV) is adjusted by an iris placed at the native image plane to avoid overlapping light field signals on the camera plane. A Fourier lens (FL, $f _ { \mathrm { F L } } = 1 5 0$ mm, Thorlabs) performs optical Fourier transform of the image at the native image plane, forming a 4f system with the tube lens (TL). A lenslet array (APO-Q-P3000-R23.5, advanced micro optic systems GmbH) is placed at the back focal plane of the FL, thus conjugated to the back pupil of the objective. The lenslet array then segments the light field with different spatial frequency onto different area of the camera. The raw FLF images are recorded on a CMOS camera (CS235MU, Thorlabs) at the back focal plane of the lenslet array.

Before recording FMIP-FLF images, a one-time calibration of the system 3D PSF is required. To perform the calibration, we first prepared a point source phantom with resolution limited fluorescence beads (P7220, 175 nm diameter, excitation/emission 540/560 nm, PS-Speck). We adjusted the concentration of the beads to ensure only one bead is in the imaging area. The PSFs were recorded by scanning the point source along the axial direction with a 100 nm step size (Figure 1c-i).

To record the FMIP-FLF images, a pulse generator (Emerald 9254, Quantum Composers) triggers the optical chopper, the 520 nm nanosecond laser, and the CMOS camera with a master clock signal of 20 kHz from the mid-IR laser. The camera sequentially measured the “IR-on” and “IR-off” FLF images (Figure 1c-ii). FMIP-FLF signals were extracted by subtracting the two images. The 3D objects were then reconstructed through a deconvolution algorithm using the 2D FMIP-FLF measurement and the calibrated PSFs. 3D chemical information was attained by scanning the wavenumber of mid-IR laser during FMIP-FLF measurements or concentrating on the vibrationa frequencies of certain chemical bonds.

## FLF Reconstruction Algorithm

The forward model of the FLF system can be written as the following form 13

$$
y = \mathbf {H} x \tag {1}
$$

where y denotes the 2D sensor measurement, x is the 3D object, and H is the forward convolution matrix determined by the experimentally calibrated 3D PSF. The 2D measurement is treated as the axial sum of the 2D convolution between the object “slice” at each depth and the corresponding depth-dependent PSF.

The reconstruction algorithm solves a regularized least-squares optimization

$$
\hat {x} = \underset {x \geq 0} {\operatorname{argmin}} \frac {1}{2} \| \mathbf {H} x - y \| _ {2} ^ {2} + R (x) \tag {2}
$$

Here, R refers to regularization terms that includes 11-norm and 3D total variation to promote sparsity of the 3D solution. We solve the optimization by adopting the algorithm based on the alternating direction method of multipliers (ADMM). 16

## Bacteria, Cancer Cell Culture, and Lipid Droplets Staining

S. aureus was stained with $1 0 ^ { - 4 }$ mol/L Rhodamine 6G (R6G) for 20 min and then dried on a tilted silicon substrate. Pancreatic cancer MIA Paca-2 cells were purchased from the American Type Culture Collection. The cells were cultured in Dulbecco’s Modified Eagle Medium (DMEM) medium supplemented with 10% Fetal Bovine Serum and 1% Penicillin−Streptomycin. All cells were maintained at $3 7 ~ ^ { \circ } \mathrm { C }$ in a humidified incubator with 5% CO supply. For lipid droplets staining, cells were cultured within 3 μmol/L lipi-red (Dojindo Lipi-Series) dissolved in serum-free medium at $3 7 ^ { \circ } \mathrm { C }$ for 30 min, following three times of phosphate-buffered saline (PBS) wash. After staining, cells were washed with deuterated PBS solution and sandwiched between glass coverslip and silicon substrate for FMIP-FLF imaging. In the experiments of $^ { 1 3 } \mathrm { C }$ fatty acid treatment, MIA Paca-2 cells were cultured with $2 5 \mathrm { g } / \mathrm { L } ^ { 1 3 } \mathrm { C }$ isotopic labeled fatty acids mixture for 24 h.

## 3. RESULTS

## System Characterization

To characterize the spatial resolution of the FMIP-FLF system, we prepared an agarose film filled with fluorescent beads of 175 nm diameter. The fluorescence beads were distributed in 1% agarose gel through sonication. The gel then formed a thin film on a silicon substrate. The raw FLF image contains four (2 × 2) elemental images (Figure 2a), which are the perspective views containing different spatial and angular information captured by the lenslet array. Based on the forward model, the 3D object (Figure 2b) was reconstructed through our deconvolution algorithm (Figure S2, Methods). The full width at half-maximum (FWHM) of the reconstructed beads at varying depths was measured using Gaussian fitting (see Figure S1), resulting in a lateral resolution of 0.5−0.9 μm and an axial resolution of 0.8−1.1 μm. The measured image volume was $\sim 6 0 \ \mu \mathrm { m } \times 6 0 \ \mu \mathrm { m } \times 5 . 6$ μm due to the trade-off between spatial resolution and FOV in FLF microscopy. The axial resolution was determined by the lateral translation of the objects from varying depths on the camera plane, which was demonstrated in the depth-resolved PSFs of the system. The detailed calculations of the spatial resolution, FOV and DOF of the system are discussed in the Supporting Information. By comparing the FMIP-FLF reconstruction results with widefield epifluorescence images at varying depths (Figure 2d), we confirmed the imaging fidelity of high-speed 3D FMIP-FLF microscopy, which is capable of imaging with submicron spatial resolution. Furthermore, the FLF imaging provided significant improvement in the axial sectioning capability compared with widefield fluorescence (Figure 2d). Here, the spatial resolution of the system is characterized by the FLF images without IR modulation, because the dye of the fluorescence beads is not thermosensitive. In this FMIP-FLF microscopy, the MIR pulse width is 50 ns resulting in the thermal diffusion length at ∼165 nm $( \mu _ { { t } } = 2 \sqrt { \alpha t } )$ which will not affect the spatial resolution.

We further demonstrated FMIP-FLF imaging of biological samples using S. aureus to confirm the spectral fidelity of the system. In the MIP measurement, fluorescence intensity was modulated by mid-IR pump beam due to the photothermal effect (Figure 1c-ii). MIP signals were thus extracted through subtraction of sequentially acquired IR-on and IR-off frames of the FLF image stack. The FMIP-FLF reconstructed 3D image stack showed the mid-IR absorption mapping of S. aureus at the Amide-I band $( 1 6 5 0 ~ \mathrm { c m ^ { - 1 } } )$ in Figure 2e. Notably, the volumetric FMIP-FLF image stack was reconstructed from two 2D FLF snapshots, including one IR-on and one IR-off frame. Consequently, the FMIP-FLF system is capable of video-rate 3D chemical imaging. As a result, FMIP-FLF microscopy is able to capture fast-moving components and study activities in dynamic living cells with chemical specificity, high throughput, as well as high spatial resolution.

## 3D Chemical Imaging of Lipid Droplets in Cancer Cells

To demonstrate the capability of FLF-MIP system for live cell imaging, we imaged MIA-Paca2 cells stained with lipi-red (see

![](images/fd0193474b015a144aa9cba88ebab98710e4404bc2b59cfc95f5c31e33366e1c.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing cellular structures with color scale (196–2505) and panel label (i), no readable text or symbols beyond labels.
</details>

![](images/ff570ef9e07eb89950d55a31f5ea880dac4289e93a4d92e83ee88a33e30daf27.jpg)

<details>
<summary>text_image</summary>

(b)
1.9 µm
0 µm
-1.9 µm
y
x
z
y
z
x
z
</details>

![](images/209c68060dea35232b2d0a045888beaa1d98a63ba6be444d1b39b5938252d2ea.jpg)

<details>
<summary>text_image</summary>

(c) z = -1.61 µm
i
z = -0.86 µm
ii
z = 0.10 µm
iii
</details>

Figure 3. FMIP-FLF imaging of lipid droplets in a MIA Paca-2 cell. The IR beam was tuned to 1744 $\mathrm { c m } ^ { - 1 }$ for the excitation of $\scriptstyle \mathrm { C = O }$ bonds. (a) Raw FLF elemental images at $\mathrm { ( i ) }$ IR-on and (ii) IR-off state. (b) 3D reconstructed FMIP image and its $_ { x - z }$ and $y - z$ projections. (c) 3D reconstructed FMIP images at varying depth. Scale bar of $( \mathsf { a } , \mathsf { b } ) _ { i }$ , 20 μm; scale bar of (c), 10 μm.

(a)  
![](images/12992da5e216018513912415f9e62adc8b4e422f4f2b3d49c254cba3823d56a5.jpg)

<details>
<summary>text_image</summary>

¹³C
1744 cm⁻¹ 0 1
1704 cm⁻¹ 0 1
</details>

![](images/50fe3e12c4823f2d1ca91413b6e02b218f97489389e6159b7ea61a373295e226.jpg)

<details>
<summary>text_image</summary>

¹²C
1744 cm⁻¹ 0 1
1704 cm⁻¹ 0 1
</details>

(c)  
![](images/b47d08dc4cb1668840e403d5783ad5fd6835da04f7b9c745c48cc8565eea2520.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | FMIP signal (25g/L ¹³C fatty acid treated) | FMIP signal (12.5g/L ¹³C fatty acid treated) | FMIP signal (control group) |
| ----------------- | ------------------------------------------ | ------------------------------------------- | ---------------------------- |
| 1690              | 0.04                                       | 0.03                                        | 0.02                         |
| 1700              | 0.08                                       | 0.03                                        | 0.02                         |
| 1710              | 0.06                                       | 0.03                                        | 0.02                         |
| 1720              | 0.03                                       | 0.03                                        | 0.02                         |
| 1730              | 0.03                                       | 0.03                                        | 0.02                         |
| 1740              | 0.04                                       | 0.03                                        | 0.03                         |
| 1750              | 0.04                                       | 0.03                                        | 0.03                         |
</details>

![](images/119bb708a09d709b6d6fd8a56f89373e9b28fcc6bc96d1701f24cabe9eac2761.jpg)

<details>
<summary>text_image</summary>

(d) z = -1.67 µm
MIA Paca-2
1744 cm⁻¹ 0 1
1704 cm⁻¹ 0 1
G3K
1744 cm⁻¹ 0 1
1704 cm⁻¹ 0 1
</details>

![](images/ced75cc9266852c59bca8bd6785b9fde77b56f7409cdc34977aeddf7167acc18.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing cellular structures at z = -1.04 μm (no text or symbols present)
</details>

![](images/73cae0d61bfbdf4d49fb605fc6c0e0caf89ae68797fbc2b8e2d7d2cb7a0f9024.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing cellular structures at z = -0.57 μm (no text or symbols present)
</details>

![](images/84df449ea8fcb49102156b48a7966249aa552c36b03e5504a859a87926351edb.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing cellular structures at z = 1.00 μm (no text or symbols present)
</details>

![](images/0c074029eb52ac6bfc608833b622e73c885b44d587e2855de9a1d8516475449b.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing cellular structures at z = 2.25 μm, with scale bars (no text or symbols beyond labels)
</details>

(e)

![](images/540ed4299d0c2a04af13548399c7b11edead158c8db33d3ddd01e76e81f63f1f.jpg)

<details>
<summary>box plot</summary>

| Group      | FMIP ratio @1704 cm⁻¹/1704 cm⁻¹ |
| ---------- | ------------------------------- |
| MIA Paca-2 | 1.40                            |
| G3K        | 1.88                            |
</details>

Figure 4. FMIP-FLF imaging of lipid droplets in MIA Paca-2 and G3K cells treated with $^ { 1 3 } \mathrm { C }$ fatty acids. $^ { ( \mathrm { a } , \mathrm { b } ) }$ FMIP intensity from 3D FMIP-FLF reconstructed stack $\mathrm { o f } ^ { 1 3 } \dot { \mathrm { C } }$ fatty acid treated MIA Paca-2 cells (a) and the control group (b) without fatty acid treatment imaged at 1704 $\mathrm { c m } ^ { - 1 } \left( \mathrm { r e d } \right)$ overlaid with that from 1744 $\mathrm { c m } ^ { - 1 } \ \mathrm { ( g r e e n ) }$ . (c) FMIP spectra of MIA Paca-2 cells treated with $( \mathrm { r e d } , 2 5 \mathrm { g / L }$ , light red, ${ \bar { 1 } } 2 . 5 ~ \mathrm { g / L } )$ and without $\left( { \mathrm { g r e e n } } \right) { } ^ { 1 3 } { \mathrm { C } }$ fatty acid. Each data point represents the mean value of the FMIP signal $\left( N = 3 \right)$ and its error bar calculates the standard deviation. The solid curves are Lorentzian fitted FMIP spectra. (d) FMIP intensity colormap of $^ { 1 3 } \mathrm { C }$ fatty acid treated MIA Paca-2 cells (top) and G3K cells (bottom) (green, 1744 $\mathrm { c m } ^ { - 1 } ,$ red, $1 7 0 4 \mathrm { c m } ^ { - 1 } )$ at varying depths. $\left( \mathrm { e } \right)$ The ratio of FMIP intensity between ${ } ^ { 1 3 } \mathrm { C } { = } \mathrm { O }$ peak at 1704 cm−1 and $^ { 1 2 } { \mathrm { C } } { = } { \mathrm { O } }$ peak at 1744 $\mathrm { c m } ^ { - 1 }$ labeled with the mean value $( N \overset { \cdot } { = } 5 \overset { \cdot } { ) }$ . The bound of outer box, inner box, lines, whiskers represent $2 5 \%$ to $7 5 \%$ of data, mean, medium, maxima, and minima, respectively. The labels represent the mean values. Scale bar, 20 μm.

Experimental Section). The bright spots in Figure 3b represent lipid droplets in a single MIA-Paca2 cell. By using a $1 7 4 4 ~ \mathrm { { c m } ^ { - 1 } }$ mid-IR pump beam to excite the ${ \mathrm { C } } { = } { \mathrm { O } }$ bonds in esterified lipids, MIP modulation of lipid droplet fluorescence was demonstrated by the comparison between IR-on and IR-off frames (Figure 3a, i and ${ \ddot { \mathbf { u } } } ,$ respectively). After reconstruction, 3D distribution of lipid droplets in a single cell was mapped in Figure 3b with bond-selectivity, covering a volume of ∼60 μm $\times 6 0 \ : \mu \mathrm { m } \times 4 \ : \mu \mathrm { m }$ . The artifacts at the edge of the cells in Figure 3b are from the FMIP contrast out of the reconstruction depth range constrained by two times of the axial FWHM of the PSF. A few reconstructed depth slices are shown in Figure 3c. Here, the depth-resolved FMIP-FLF images of lipi-red stained MIA-Paca2 showed rich lipid contents in cancer cells, except for the nuclei area. The 3D reconstructed FMIP-FLF images with submicron level axial resolution and video acquisition rate show greater potential in quantitative chemical analysis than previous MIP microscopy in 2D manner. Furthermore, using this ultrafast 3D imaging method in living cells with chemical specificity, we are capable of studying lipid metabolism in cancer cells, such as fatty acid uptake that is beyond the reach of FLF microscopy.

## MLP-FLF Imaging of Lipid Metabolism in Drug-Resistant Cancer Cells

Lipids are essential building blocks synthesized by complex molecular pathways, from glucose or fatty acid uptake, and are stored as lipid droplets in cells. Fluorescence labeling of lipid will dramatically alter its properties in metabolism, 32 while isotopic labeling hardly changes the chemical properties of lipid in metabolism. Consequently, the isotopically labeled FMIP-FLF imaging method is more reliable in analyzing lipid pathways of cancer cells. Currently, $^ { 1 3 } \mathrm { C }$ metabolic flux analysis is the preferred tool for quantitative characterization of metabolic phenotypes in mammalian cells.33,34 Cells can take up long chain free fatty acids (FFA) in vivo from the nonprotein bound ligand pool in extracellular fluid.35 To study fatty acid uptake in cancer cells, we treated MIA Paca-2 cells with $^ { 1 3 } \mathrm { C }$ isotopically labeled fatty acids. As seen in Figure $^ { \mathrm { ~ S 3 , ~ } }$ Fourier-transform infrared spectroscopy (FTIR) $\mathrm { o f } ^ { 1 3 } \mathrm { { \dot { C } } }$ labeled fatty acid mixture showed $\overline { { { \mathrm { ~ a ~ } } } } \sim 3 0 \mathrm { ~ c m } ^ { - 1 }$ peak shift to lower wavenumber compared with $^ { 1 2 } \mathrm { C }$ palmitic acid (major contents in the $^ { 1 3 } \mathrm { C }$ fatty acid mixture). Incubating MIA Paca-2 cells with $^ { 1 3 } \mathrm { C }$ isotopic labeled free fatty acid results in the formation of intracellular neutral lipid. Consequently, the FMIP peak of lipid droplets formed from $^ { 1 3 } \mathrm { C }$ fatty acid treatment is expected to display $\mathsf { a } \sim 3 0 \ \mathrm { c m } ^ { - 1 }$ peak shift from that for endogenous, de novo synthesized lipids $\left( 1 7 4 4 \ \mathrm { c m } ^ { - 1 } \right)$ . As seen in Figure $^ { 4 \mathrm { c } , }$ the FMIP spectra (solid curves in Figure 4c) were generated by Lorentzian fitting from FMIP signals of MIA Paca-2 cells $( N =$ 3) heated by mid-IR pulses ranging from 1690 to $1 7 4 5 ~ \mathrm { { c m } ^ { - 1 } }$ . The FMIP signals here were calculated by the ratio of the fluorescence intensity change between $^ { \omega } \mathrm { I R } ^ { \prime } \mathrm { o n } ^ { \prime \prime }$ and $\ " \mathrm { { I R - o f f } }$ states and the fluorescence intensity at “IR-off” states. Since the sampling rate in frequency domain of FMIP-FLF imaging was limited by the photobleaching effect of the fluorescent dye, FMIP-FLF images were collected only at six mid-IR wavenumbers for each cell. The baseline of the FMIP spectra in Figure 4c is from the water absorption inside the cells. Lipid droplets in $^ { 1 3 } \mathrm { C }$ fatty acid treated cells (red) showed FMIP peaks shift to shorter vibrational frequency, while those without $^ { 1 3 } \mathrm { C }$ fatty acid treatment (green) remained at 1744 $\mathrm { c m } ^ { - 1 }$ . Besides, cells treated with $^ { \circ } { } ^ { 1 3 } \mathrm { C }$ fatty acid of high concentration (red) displayed higher FMIP signals at $^ { 1 3 } { \mathrm { C } } { = } { \mathrm { O } }$ peak than those of low concentration (light red). This indicates that our isotopically labeled FMIP-FLF imaging method is potential for lipid pathway tracing. By overlaying the 3D reconstructed $\mathrm { F M I P } ^ { \mathrm { \overline { { 1 } } N M I P } ^ { \mathrm { \overline { { 1 } } } } }$ images at 1704 and $1 7 4 4 ~ \mathrm { c m } ^ { - 1 } ,$ , the lipid chemical components of MIA Paca-2 were demonstrated in Figure 4a,b, where the red colormap represented lipid droplets formed from fatty acid uptake and the green color mapped endogenous lipid. Here, the colormap of MIA Paca-2 and restored FMIP spectra confirmed rich lipid contents in cancer cells from fatty acid pathway. The isotopic labeling of fatty acids in FMIP-FLF measurement does not introduce significant modification of molecular structures, which provide the possibility of quantitative analysis. To accurately correlate the FMIP signal with molecular concentration, further calibration with quantitative chemical imaging golden standard, such as coherent Raman microscopy, is required.

Next, we used the FMIP-FLF image to study altered fatty acid metabolism in drug-resistant pancreatic cancer cells by comparing the gemcitabine-sensitive MIA PaCa-2 cells and gemcitabine-resistant G3K cells (see Experimental Section). Based on the lipid pathway tracing method discussed above, we can distinguish between exogenous and endogenous lipid of living cells. Here, both G3K group and MIA Paca-2 group were treated with $^ { 1 3 } \mathrm { C }$ fatty acids with the same concentration and culture time. In the depth-resolved FMIP-FLF reconstructed image stacks (Figure 4d), the drug-resistant G3K group shows higher FMIP intensity at $1 7 0 4 ~ \mathrm { { c m } ^ { - 1 } }$ (red) than the MIA Paca 2 cell. As compared in the FMIP signal ratio between $^ { 1 3 } { \mathrm { C } } { = } { \mathrm { O } }$ peak and $^ { 1 2 } { \mathrm { C } } { \dot { = } } { \mathrm { O } }$ peak of the lipid droplets in MIA Paca-2 (N $= 5 )$ and G3K (N = 5) cells (Figures 4e, S4), G3K group displayed exceedingly more $^ { 1 3 } { \mathrm { C } } { = } \breve { \mathrm { O } }$ than MIA Paca-2 group. As a result, we concluded that gemcitabine-resistant G3K cells more rely on exogenous fatty acids than gemcitabine-sensitive MIA PaCa-2 cells. Meanwhile, the G3K cells showed distinctly longer protrusions than MIA $\mathrm { P a c a } { - 2 , }$ and the protrusions were rich in lipid droplets. These observations can also serve as markers to determine drug resistance of cancer cells.

## 4. DISCUSSION

We developed FMIP-FLF microscopy that allows high-speed volumetric chemical imaging with infrared spectroscopic information at an 8 Hz volume rate. The image volume was $6 0 \ \mu \mathrm { m } \times 6 0 \ \mu \mathrm { m } \times 5 . 6$ μm with a lateral resolution of 0.5−0.9 μm and an axial resolution of 0.8−1.1 μm. FLF microscopy provides an unprecedented 3D imaging speed that cannot be achieved with the confocal microscope, which takes a few seconds to scan the sample voxel by voxel. The FMIP sets additional requirement for the confocal scanning when detecting the fluorescence intensity modulation induced by the mid-IR pulse. The pump mid-IR laser can only operate at a limited repetition rate, which is determined by not only the laser pulse repetition rate but also the thermal decay time to avoid heat accumulation. In addition, to get enough SNR, long pixel dwell time is used experimentally and thus further decreases the scanning speed and makes confocal measurement not an optimal method for high-speed volumetric chemical imaging. The light sheet microscopy has several benefits over the confocal laser scanning microscopy. The plane-scanning speed is faster than point-scanning speed and also diminishes the photobleaching issue. However, all these scanning-based methods are not capable of imaging 3D volume in a single snapshot.

The FMIP-FLF system is compact and simple, since it does not require any mechanical movements. Meanwhile, the snapshot volumetric system is more stable than scanningbased methods, which play a significant role in MIP detection. During the MIP measurements, mechanical fluctuation induced by scanning or rotation will introduce strong artifacts after the subtraction of images at IR-on and IR-off states, and thus is detrimental to the restoration of spectroscopic information. Furthermore, the ultrahigh speed of FMIP-FLF imaging also mitigates the laser fluctuation issue during MIP detection.

In this work, we aim to achieve high spatial resolution for subcellular imaging, while the FOV and DOF are limited by high magnification and high NA of the objective and high occupancy ratio of the lenslet array. In order to accommodate broader application, such as multicellular systems,36 extended imaging volume of 400 × 400 × 20 μm3 with lateral resolution of 1 μm and axial resolution of 2.8 μm can be achieved with proper optical design following the rationale in the Supporting Information.

In the reported FMIP-FLF microscope, high-speed chemical 3D volumes are captured containing volumetric chemical information in half of the camera frame rate. To attain FMIP images with high SNR, we need to balance the exposure time with the imaging speed. In this work, we set the camera frame rate as 16 fps, and the exposure time can be tuned to 60 ms for high SNR. In the future, the imaging speed can potentially be improved toward the laser repetition rate with an ultrafast camera with sufficient light sensitivity. However, real-time volumetric spectroscopic imaging is still challenging due to the long reconstruction time. Recently, deep learning framework has emerged as the state-of-the-art to perform fast and reliable reconstruction for various volumetric fluorescence microscopes.37−39 We anticipate that our system could achieve video-rate reconstruction speed by replacing the current iterative method with deep learning framework, which is especially beneficial for biomedical application.

## 5. CONCLUSION

In summary, via the development of FMIP-FLF microscopy, we demonstrated high-speed volumetric chemical imaging of lipid contents in living cells and further studied the lipid metabolism in drug-resistant cancer cells with infrared spectroscopic selectivity. Specifically, we distinguished lipids from exogeneous fatty acids versus those from de novo synthesis, which cannot be fulfilled with fluorescence imaging alone. Meanwhile, in our FMIP-FLF design, we relied on fluorescence intensity modulations to sense the MIP effect. Fluorescence labeling improves the specificity of MIP imaging by targeting specific organelles or biomolecules. However, photobleaching issue is sometimes not negligible. To mitigate these issues and broaden the potential applications, label-free high-speed volumetric chemical imaging will be pursued in our future work.

## ASSOCIATED CONTENT

## \*sı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/cbmi.3c00022.

FLF optical design rationale, the theoretical calculations of its spatial resolution, FOV and DOF, and detailed optimization potentials of the optical design; FMIP-FLF system calibration, the measured PSF of the FMIP-FLF system; Fourier-transform infrared spectra of the isotopically labeled fatty acids; FMIP colormap of lipid contents in Mia Paca-2 and G3K cells (PDF)

## AUTHOR INFORMATION

## Corresponding Authors

Yi Zhang − Department of Physics, Boston University, Boston, Massachusetts 02215, United States; Email: zhangyi@ bu.edu  
Lei Tian − Department of Electrical and Computer Engineering and Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, United States; Email: leitian@bu.edu  
Ji-Xin Cheng − Department of Electrical and Computer Engineering and Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, United States; orcid.org/0000-0002-5607-6683; Email: jxcheng@bu.edu

## Authors

Danchen Jia − Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, United States

Qianwan Yang − Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, United States

Yujia Xue − Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, United States

Yuying Tan − Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, United States

Zhongyue Guo − Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, United States

Meng Zhang − Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, United States

Complete contact information is available at: https://pubs.acs.org/10.1021/cbmi.3c00022

## Author Contributions

‡ D.J., Y.Z., and Q.Y. contributed equally to this work. Y.Z. initialized the idea of volumetric FMIP imaging with FLF for this work. Y.Z. and D.J. developed the FMIP-FLF setup. D.J. and Y.Z. designed and carried out the experiments. Q.Y. and Y.X. carried out the image reconstruction. D.J. analyzed the experimental results. Y.T. cultured and stained the cells. M.Z. and D.J. cultured and stained the bacteria. Z.G. contributed tc build the widefield MIP setup. L.T. and J.X.C. supervised the research and the development of the manuscript. D.J. and Y.Z. wrote the manuscript with input from all authors. All authors took part in the revision and approved the final version of the manuscript.

## Notes

The authors declare the following competing financial interest(s): J.X.C. declares a financial interest with Photo thermal Spectroscopy Corp.

## ACKNOWLEDGMENTS

This work is supported by R01EB032391 to J.X.C. and L.T., R35GM136223, R01AI141439, R33CA261726 to J.X.C.

## REFERENCES

(1) Dodt, H. U.; Leischner, U.; Schierloh, A.; Jahrling, N.; Mauch, C. P.; Deininger, K.; Deussing, J. M.; Eder, M.; Zieglgansberger, W.; Becker, K. Ultramicroscopy: three-dimensional visualization of neuronal networks in the whole mouse brain. Nat. Methods 2007, 4 (4), 331−336.  
(2) Planchon, T. A.; Gao, L.; Milkie, D. E.; Davidson, M. W.; Galbraith, J. A.; Galbraith, C. G.; Betzig, E. Rapid three-dimensional isotropic imaging of living cells using Bessel beam plane illumination. Nat. Methods 2011, 8 (5), 417−423.  
(3) Boden, A.; Pennacchietti, F.; Coceano, G.; Damenti, M.; Ratz, M.; Testa, I. Volumetric live cell imaging with three-dimensional parallelized RESOLFT microscopy. Nat. Biotechnol. 2021, 39 (5), 609−618.  
(4) Gu, M. Principles of three dimensional imaging in confocal microscopes; World Scientific, 1996.  
(5) Denk, W.; Strickler, J. H.; Webb, W. W. Two-photon laser scanning fluorescence microscopy. Science 1990, 248 (4951), 73−76.  
(6) Oku, H.; Hashimoto, K.; Ishikawa, M. Variable-focus lens with 1- kHz bandwidth. Opt Express 2004, 12 (10), 2138−2149.  
(7) Dal Maschio, M.; De Stasi, A. M.; Benfenati, F.; Fellin, T. Threedimensional in vivo scanning microscopy with inertia-free focus control. Opt. Lett. 2011, 36 (17), 3503−3505.  
(8) Keller, P. J.; Schmidt, A. D.; Wittbrodt, J.; Stelzer, E. H. Reconstruction of zebrafish early embryonic development by scanned light sheet microscopy. Science 2008, 322 (5904), 1065−1069.  
(9) Huisken, J.; Swoger, J.; Del Bene, F.; Wittbrodt, J.; Stelzer, E. H. Optical sectioning deep inside live embryos by selective plane illumination microscopy. Science 2004, 305 (5686), 1007−1009.  
(10) Bouchard, M. B.; Voleti, V.; Mendes, C. S.; Lacefield, C.; Grueber, W. B.; Mann, R. S.; Bruno, R. M.; Hillman, E. M. Swept confocally-aligned planar excitation (SCAPE) microscopy for high speed volumetric imaging of behaving organisms. Nat. Photonics 2015, 9 (2), 113−119.  
(11) Mertz, J. Strategies for volumetric imaging with a fluorescence microscope. Optica 2019, 6 (10), 1261−1268.  
(12) Levoy, M.; Ng, R.; Adams, A.; Footer, M.; Horowitz, M. Light field microscopy. ACM Trans. Graph. 2006, 25, 924.  
(13) Guo, C.; Liu, W.; Hua, X.; Li, H.; Jia, S. Fourier light-field microscopy. Opt Express 2019. 27 (18). 2557325594.  
(14) Liu, W.; Jia, S. wFLFM: enhancing the resolution of Fourier light-field microscopy using a hybrid wide-field image. Appl. Phys. Express 2021, 14 (1), 012007.  
(15) Hua, X.; Liu, W.; Jia, S. High-resolution Fourier light-field microscopy for volumetric multi-color live-cell imaging. Optica 2021, 8 (5), 614−620.  
(16) Xue, Y.; Davison, I. G.; Boas, D. A.; Tian, L. Single-shot 3D wide-field fluorescence imaging with a Computational Miniature Mesoscope. Sci. Adv. 2020, 6 (43), 7508 DOI: 10.1126/sciadv.abb7508.  
(17) Cheng, J. X.; Xie, X. S. Vibrational spectroscopic imaging of living systems: An emerging platform for biology and medicine. Science 2015, 350 (6264), aaa8870.  
(18) Lee, H. J.; Jiang, Y.; Cheng, J. X. Label-free Optical Imaging of Membrane Potential. Curr. Opin Biomed Eng. 2019, 12, 118−125.  
(19) Huang, K. C.; Li, J.; Zhang, C.; Tan, Y.; Cheng, J. X. Multiplex Stimulated Raman Scattering Imaging Cytometry Reveals Lipid-Rich Protrusions in Cancer Cells under Stress Condition. iScience 2020, 23 (3), 100953.  
(20) Hu, F.; Lamprecht, M. R.; Wei, L.; Morrison, B.; Min, W. Bioorthogonal chemical imaging of metabolic activities in live mammalian hippocampal tissues with stimulated Raman scattering. Sci. Rep 2016, 6, 39660.  
(21) Chen, X.; Zhang, C.; Lin, P.; Huang, K. C.; Liang, J.; Tian, J.; Cheng, J. X. Volumetric chemical imaging by stimulated Raman projection microscopy and tomography. Nat. Commun. 2017, 8, 15117.  
(22) Hu, F.; Shi, L.; Min, W. Biological imaging of chemical bonds by stimulated Raman scattering microscopy. Nat. Methods 2019, 16 (9), 830−842.  
(23) Qian, C.; Miao, K.; Lin, L. E.; Chen, X.; Du, J.; Wei, L. Super resolution label-free volumetric vibrational imaging. Nat. Commun. 2021, 12 (1), 3648.  
(24) Zhang, D.; Li, C.; Zhang, C.; Slipchenko, M. N.; Eakins, G.; Cheng, J. X. Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2016, 2 (9), e1600521.  
(25) Bai, Y.; Zhang, D.; Lan, L.; Huang, Y.; Maize, K.; Shakouri, A.; Cheng, J. X. Ultrafast chemical imaging by widefield photothermal sensing of infrared absorption. Sci. Adv. 2019, 5 (7), eaav7127.  
(26) Tamamitsu, M.; Toda, K.; Horisaki, R.; Ideguchi, T. Quantitative phase imaging with molecular vibrational sensitivity. Opt. Lett. 2019, 44 (15), 3729−3732.  
(27) Zhang, D.; Lan, L.; Bai, Y.; Majeed, H.; Kandel, M. E.; Popescu, G.; Cheng, J. X. Bond-selective transient phase imaging via sensing of the infrared photothermal effect. Light Sci. Appl. 2019, 8, 116.  
(28) Tamamitsu, M.; Toda, K.; Shimada, H.; Honda, T.; Takarada, M.; Okabe, K.; Nagashima, Y.; Horisaki, R.; Ideguchi, T. Label-free biochemical quantitative phase imaging with mid-infrared photo thermal effect. Optica 2020, 7 (4), 359−366.  
(29) Zhao, J.; Matlock, A.; Zhu, H.; Song, Z.; Zhu, J.; Wang, B.; Chen, F.; Zhan, Y.; Chen, Z.; Xu, Y. Bond-Selective Intensity Diffraction Tomography. Nat. Commun. 2022, 13, 8.  
(30) Li, M.; Razumtcev, A.; Yang, R.; Liu, Y.; Rong, J.; Geiger, A. C.; Blanchard, R.; Pfluegl, C.; Taylor, L. S.; Simpson, G. J. Fluorescence Detected Mid-Infrared Photothermal Microscopy. J. Am. Chem. Soc. 2021, 143 (29), 10809−10815.  
(31) Zhang, Y.; Zong, H.; Zong, C.; Tan, Y.; Zhang, M.; Zhan, Y.; Cheng, J. X. Fluorescence-Detected Mid-Infrared Photothermal Microscopy. J. Am. Chem. Soc. 2021, 143 (30), 11490−11499.  
(32) Rumin, J.; Bonnefond, H.; Saint-Jean, B.; Rouxel, C.; Sciandra, A.; Bernard, O.; Cadoret, J.-P.; Bougaran, G. The use of fluorescent Nile red and BODIPY for lipid measurement in microalgae. Biotechnology for Biofuels 2015, 8 (1), 42.  
(33) Dong, W.; Keibler, M. A.; Stephanopoulos, G. Review of metabolic pathways activated in cancer cells as determined through isotopic labeling and network analysis. Metab Eng. 2017, 43, 113− 124.  
(34) Badur, M. G.; Metallo, C. M. Reverse engineering the cancer metabolic network using flux analysis to understand drivers of human disease. Metab Eng. 2018, 45, 95−108.  
(35) Berk, P. D.; Stump, D. D. Mechanisms of cellular uptake of long chain free fatty acids. Mol. Cell. Biochem. 1999, 192 (1−2), 17−31.  
(36) Liu, W.; Kim, G. R.; Takayama, S.; Jia, S. Fourier light-field imaging of human organoids with a hybrid point-spread function. Biosens Bioelectron 2022, 208, 114201.  
(37) Wang, Z.; Zhu, L.; Zhang, H.; Li, G.; Yi, C.; Li, Y.; Yang, Y.; Ding, Y.; Zhen, M.; Gao, S.; et al. Real-time volumetric reconstruction of biological dynamics with light-field microscopy and deep learning. Nat. Methods 2021, 18 (5), 551−556.  
(38) Wagner, N.; Beuttenmueller, F.; Norlin, N.; Gierten, J.; Boffi, J. C.; Wittbrodt, J.; Weigert, M.; Hufnagel, L.; Prevedel, R.; Kreshuk, A. Deep learning-enhanced light-field imaging with continuous validation. Nat. Methods 2021, 18 (5), 557−563.  
(39) Xue, Y.; Yang, Q.; Hu, G.; Guo, K.; Tian, L. Deep-learningaugmented computational miniature mesoscope. Optica 2022, 9, 1009.