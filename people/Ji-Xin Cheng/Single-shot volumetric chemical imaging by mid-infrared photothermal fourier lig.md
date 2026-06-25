# Single-shot Volumetric Chemical Imaging by Mid-Infrared Photothermal Fourier Light Field Microscopy

Yi Zhanga,d,†, Danchen Jiab,d,†, Qianwan Yangb,d,†, Yujia Xueb,d, Yuying Tanc, Zhongyue Guoc, Meng Zhangc, Lei Tianb,c,d, Ji-Xin Chenga,b,c,d,\*

aDepartment of Physics, Boston University, MA, 02215, Boston

bDepartment of Electrical and Computer Engineering, Boston University, MA, 022153, Boston

cDepartment of Biomedical Engineering, Boston University, MA, 022154, Boston

dPhotonics Center, Boston University, MA, 02215, Boston

\*Corresponding author: jxcheng@bu.edu; †equal contributions

Abstract: Three-dimensional molecular imaging of living organisms and cells plays a significant role in modern biology. Yet, current volumetric imaging modalities are largely fluorescence-based and thus lack chemical content information. Mid-infrared photothermal microscopy as a new chemical imaging technology provides infrared spectroscopic information at sub-micrometer spatial resolution. Here, by harnessing thermosensitive fluorescent dyes to sense the mid-infrared photothermal effect, we demonstrate mid-infrared photothermal Fourier light field (MIP-FLF) microscopy for single-shot volumetric infrared spectroscopic imaging at the speed of 8 volumes per second and submicron spatial resolution. Protein contents in bacteria and lipid droplets in living pancreatic cancer cells are visualized. Altered lipid metabolism in drug-resistant pancreatic cancer cells is observed with the MIP-FLF microscope.

## 1. Introduction

Volumetric imaging plays a prominent role in life science due to its ability of visualizing 3D architecture of biological systems ranging from whole-brain to subcellular level1-3. Volumetric fluorescence imaging is routinely performed by optical sectioning and z-axis scanning with either confocal microscopy4 or two-photon laser scanning microscopy5. However, these scanning-based approaches are time-consuming and require a precise mechanical 3D positioning device. In cases where photobleaching is a concern, repeated sectioning only exacerbates this problem by increasing exposure. Fast focus scanning methods using electrically tunable lens6 or spatial light modulator7 mitigate the issue by improving scanning speed, but hinder the imaging contrast due to a drawback of out-of-focus background. Light-sheet fluorescence microscopy physically eliminates the background by illuminating the sample only with a thin sheet of light from the side of the specimen for optical sectioning8-10. Also, the excitation is confined to the focal plane, thus boosting detection efficiency while reducing photobleaching and photodamage. Various scanning-based strategies discussed above promote the imaging speed of volumetric fluorescence imaging11, but still cannot achieve video-rate due to the requirement of mechanical movement.

To further capture the fast-moving organelles or study dynamic activities in living cells, single-snapshot light field microscopy emerged as a scanning-free, scalable method that allows for high-speed, volumetric imaging12

Specifically, a microlens array is used to capture 3D structure of objects in a single snapshot. Recently developed Fourier light-field (FLF) microscopy achieved high-quality volumetric imaging by recording the light field in the Fourier domain, which allows jointly allocating the spatial and angular information of the incident light in a consistently non-overlapping manner, effectively avoiding any artifacts in conventional light field systems 13-16 . These advances in both imaging capability and computation speed promise further development of FLF microscopy toward high-resolution, volumetric data acquisition, analysis and observation at the video rate. However, these methods are fluorescence based, lacking the chemical content information about the subjects.

Vibrational spectroscopic imaging based on molecular fingerprints is able to offer chemical content and molecular structural information about an organism in a label-free manner17. Along this direction, coherent Raman scattering metastasis19, brain metabolic activity20, and so on. Bessel beam based Stimulated Raman projection tomography has been developed to quantify the total chemical composition of a 3D object21. More recently, volumetric chemica imaging on the nanoscale is enabled by the integration of stimulated Raman scattering microscopy and expansion microscop y22, 23. Yet, the detection sensitivity of Raman based vibrational microscopy is ultimately limited by its small cross section.

The infrared absorption offers a cross section that is eight orders of magnitude larger than Raman scattering. Yet, infrared microscopy lacks depth resolution, which prohibits accurate decomposition of cellular dry mass density into independent biomolecular components. Recently developed mid-infrared photothermal (MIP) microscopy exceeds the diffraction limit of infrared microscopy and allows three-dimensional chemical imaging in a confocal scanning manner24. To improve the 2D imaging speed and achieve large scale imaging, wide field MIP microscopy is demonstrated via a virtual lock-in camera approach25. By measuring the mid-infrared photothermal effect in a quantitative phase microscope, both 2D and 3D bond-selective phase imaging has been demonstrated26-29. Yet, the speed (\~50s per volume) is insufficient to capture chemical information in a highly dynamic living system.

Here, we present a mid-infrared photothermal Fourier light-field (MIP-FLF) microscope that allows single-shot chemical imaging of living cells. We harness thermosensitive fluorescent dyes to sense the mid-infrared photothermal effect30, 31. The fluorescence intensity can be modulated at the level of 1% per Kelvin by mid-IR absorption, which is 100 times larger than the thermal modulation of scattering intensity. Moreover, the fluorophores can target specific organelles or biomolecules, thus augmenting the specificity of photothermal imaging. Importantly, this method is fully compatible with the FLF fluorescence imaging. By recording photothermal modulation of fluorescence emission in an FLF microscope, we achieved an infrared spectroscopic imaging rate of 8 volumes per second, at a lateral resolution of 0.5 to 0.9 m and an axial resolution of 0.8 to 1.1 m. This speed is faster than reported confocal MIP microscopy24 or MIP-based optical diffraction tomography28 by two orders of magnitude. With these advancements, we demonstrate single-shot volumetric bond-selective imaging in living cells, where the lipid content is used as a marker to determine the drug resistance of cancer cells.

## 2. Methods

## 2.1. MIP-FLF Microscope

The MIP-FLF microscope is a pump and probe imaging system (Fig. 1a). A pulsed visible probe beam passes through a FLF microscope to capture fluorescently labeled sample, while the IR absorption information is coded by a nanosecond pulsed mid-IR laser. The raw MIP-FLF images are acquired by synchronizing the IR pump pulses, the visible probe pulses, and the camera exposure (Fig. 1b). After acquiring each pair of $^ { \mathrm { s } } \mathrm { I R - o n } ^ { \mathrm { 3 } }$ and $^ { 6 6 } \mathrm { I R - o f f } ^ { 3 }$ images, a 3D deconvolution is performed that incorporates the point spread function (PSF) to generate the final 3D chemical image (Fig. 1c).

The schematic of the MIP-FLF microscope is shown in Fig. 1b. The infrared pulses are generated by a tunable optical parametric oscillator laser (Firefly-LW, M Squared Lasers), ranging from 1175 to 1800 cm-1, operating at 20 kHz repetition rate and 50 ns pulse duration. An optical chopper (MC2000B, Thorlabs) modulates the IR pulses to accommodate the acquisition speed of the camera. A gold-coated off-axis parabolic mirror with a focal length of 25.4 mm weakly focuses the pump beam at the sample.

On the FLF microscope, a 2x2 microlens array is used to image the 3D fluorescence as 2x2 projection views on the camera plane. The FLF imaging is implemented on an epifluorescence microscope using a 100×, 0.95NA objective lens (PLFLN100X; PLAN FLUOR 100X DRY OBJ, NA 0.95, WD 0.2). The samples are excited with a 520-nm nanosecond laser (NPL52C, Thorlabs) at 20 kHz repetition rate. The generated fluorescence emission is collected with a dichroic mirror (DMLP550T, Thorlabs), a 550-nm long-pass filter (FEL0550, Thorlabs) and a tube lens (TTL180- A, Thorlabs). The field of view (FOV) is adjusted by an iris placed at the native image plane to avoid overlapping light field signals on the camera plane. A Fourier lens (FL, $f _ { F L } = 1 5 0 ~ \mathrm { m m }$ , Thorlabs) performs optical Fourier transform of the image at the native image plane, forming a 4f system with the tube lens (TL). A microlens array (MLA, APO-Q-P3000-R23.5, advanced microoptic systems GmbH) is placed at the back focal plane of the FL, thus conjugated to the back pupil of the objective. The raw FLF images are recorded on a CMOS camera (CS235MU, Thorlabs) at the back focal plane of the MLA.

Before recording MIP-FLF images, a one-time calibration of the system 3D PSF is required. To perform the calibration, we first prepared a point source phantom with resolution limited fluorescence beads (P7220, 175 nm diameter, excitation/emission 540/560 nm, PS-SpeckTM). We adjusted the concentration of the beads to ensure only one bead is in the imaging area. The PSFs were recorded by scanning the point source along the axial direction with a 100 nm step size (Fig. 1c-i).

To record the MIP-FLF images, a pulse generator (Emerald 9254, Quantum Composers) triggers the optical chopper, the 520 nm nanosecond laser and the CMOS camera with a master clock signal of 20 kHz from the mid-IR laser. The camera sequentially measured the “IR-on” and “IR-off” FLF images (Fig. 1c-ii). MIP-FLF signals were extracted by subtracting the two images. The 3D objects were then reconstructed through a deconvolution algorithm using the 2D MIP-FLF measurement and the calibrated PSFs. 3D chemical information was attained by scanning the wavenumber of mid-IR laser during MIP-FLF measurements or concentrating on the vibrational frequencies of certain chemical bonds.

![](images/8287ed12f61ce70eb480ec5fb727fb56e83a47014c040970b8df7a90f8af4376.jpg)

<details>
<summary>text_image</summary>

(a)
Mid-IR pulses
Visible pulses
sample
FL
MLA
Modulated fluorescence
</details>

![](images/25814c6256267738b71fac58a2ae9b6cf63a233a0ab6af78fe3578fc867c2679.jpg)

<details>
<summary>text_image</summary>

(c) i. Point-spread functions
z₁ z₂ z₃
e ii. MIP-FLF measurement
IR-off IR-on
</details>

![](images/2e56265c520d5bb929f8eb6baa76a7515ad91ad8ac358f308a7b8d538c9f5f23.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Mid-IR laser"] --> B["Chopper"]
  B --> C["OL"]
  C --> D["DM"]
  D --> E["sample"]
  E --> F["Visible laser"]
  F --> G["TL"]
  G --> H["Iris"]
  H --> I["FL"]
  I --> J["MLA camera"]
  J --> K["Function Generator"]
```
</details>

![](images/245d2f49d2f67a767555dc44a748159b46fb95ee7ef0d0f81dd09638c4fc6c5e.jpg)

<details>
<summary>text_image</summary>

iii. 3D Reconstruction
z₁
z₂
z₃
</details>

Figure 1. MIP-FLF imaging system and procedures. (a) Principle of MIP-FLF microscope. The modulated fluorescence emission carries IR information coded by mid-IR pulses. Each single snapshot image contains 3D information introduced by a microlens array (MLA) placed at the Fourier plane. FL, Fourier lens. (b) Experimental setup. The pump beam is a nanosecond mid-IR laser, modulated by an optical chopper and weakly focused on the sample by a gold-coated parabolic mirror. The probe beam is a 520 nm nanosecond laser and sent through the MLA placed at the back focal plane of a FL. The tube lens and the FL formed a 4f system. OL, objective lens. DM, dichroic mirror. (c) Procedures of MIP-FLF measurements. (i) Example measured PSFs of the system. (ii) Raw MIP-FLF measurement contains a pair of IR-on and IR-off images. (iii) 3D MIP-FLF reconstruction by deconvolution between 2D raw MIP-FLF image and the measured PSFs. The samples were Rhodamine 6G stained Staphylococcus Aureus (S. aureus) bacteria prepared on a tilted silicon substrate.

## 2.2. FLF reconstruction algorithm

The forward model of the FLF system can be written as the following form13

$$
y = \mathbf {H} x \tag {1}
$$

where y denotes the 2D sensor measurement, x is the 3D object, H is the forward convolution matrix determined by the experimentally calibrated 3D PSF. The 2D measurement is treated as the axial sum of the 2D convolution between the object “slice” at each depth and the corresponding depth-dependent PSF.

The reconstruction algorithm solves a regularized least squares optimization

$$
\hat {x} = \underset {x \geq 0} {\operatorname{argmin}} \frac {1}{2} \| \mathbf {H} x - y \| _ {2} ^ {2} + R (x) \tag {2}
$$

Here, R refers to regularization terms that includes l1-norm and 3D total variation to promote sparsity of the 3D solution. We solve the optimization by adopting the algorithm based on the alternating direction method of multipliers (ADMM)16.

## 2.3. Bacteria, cancer cell culture, and lipid droplets staining

S. aureus was stained with $1 0 ^ { - 4 }$ mol/L Rhodamine 6G (R6G) for 20 minutes and then dried on a tilted silicon substrate. Pancreatic cancer MIA Paca-2 cells were purchased from the American Type Culture Collection. The cells were cultured in Dulbecco's Modified Eagle Medium (DMEM) medium supplemented with 10% Fetal Bovine Serum and 1% Penicillin-Streptomycin. All cells were maintained at $3 7 ~ ^ { \circ } \mathrm { C }$ in a humidified incubator with 5 % $\mathrm { C O } _ { 2 }$ supply. For lipid droplets staining, cells were cultured within 3 μmol/L lipi-red (Dojindo Lipi-Series) dissolved in serum-free medium at $3 7 ~ ^ { \circ } \mathrm { C }$ for 30 minutes, following three times of Phosphate-Buffered Saline (PBS) wash. After staining, cells were washed with deuterated PBS solution and sandwiched the cells between glass coverslip and silicon substrate for

MIP-FLF imaging. In the experiments of $^ { 1 3 } \mathrm { C }$ fatty acid treatment, MIA Paca-2 cells were cultured with 25 $\mathrm { g / L \Omega ^ { 1 3 } C }$ isotopic labeled fatty acids mixture for 24 hours.

## 3. Results

## 3.1. System characterization

To characterize the spatial resolution of the MIP-FLF system, we prepared an agarose film filled with fluorescent beads of 175 nm diameter. The fluorescence beads were distributed in 1% agarose gel through sonication. The ge then formed a thin film on a silicon substrate. The raw FLF image contains four (2x2) elemental images (Fig. 2a), which are the perspective views containing different spatial and angular information captured by the MLA. Based on the forward model, the 3D object (Fig. 2b) was reconstructed through our deconvolution algorithm (Fig. S1, Methods). The full width at half-maximum (FWHM) of the reconstructed beads at varying depths was measured using Gaussian fitting (see Fig. S2), resulting in a lateral resolution of 0.5-0.9 μm and an axial resolution of 0.8-1.1 μm. The measured image volume was ${ \sim } 6 0 ~ { \mu \mathrm { m } } \times 6 0 ~ { \mu \mathrm { m } } \times 4$ μm due to the trade-off between spatial resolution and FOV in FLF microscopy. The axial resolution was determined by the lateral translation of the objects from varying depths on the camera plane, which was demonstrated in the depth-resolved PSFs of the system. By comparing the MIP-FLF reconstruction results with widefield epifluorescence images at varying depths (Fig. 2d), we confirmed the imaging fidelity of single-shot 3D MIP-FLF microscopy, which is capable of imaging with submicron spatial resolution. Furthermore, the MIP-FLF microscope provided significant improvement in the axial sectioning capability compared with widefield fluorescence (Fig. 2d).

We further demonstrated MIP-FLF imaging of biological samples using S. aureus to confirm the spectral fidelity of the system. In the MIP measurement, fluorescence intensity was modulated by mid-IR pump beam due to the photothermal effect (Fig. 1c-ii). MIP signals were thus extracted through subtraction of sequentially acquired IR-on and IR-off frames of the FLF image stack. The MIP-FLF reconstructed 3D image stack showed the mid-IR absorption mapping of S. aureus at the Amide-I band (1650 cm-1) in Fig. 2e. Notably, the volumetric MIP-FLF image stack was reconstructed from a single-shot FLF image, including one IR-on and one IR-off frame. Consequently, the MIP-FLF system is capable of video-rate 3D chemical imaging. As a result, MIP-FLF microscopy is able to capture fast-moving components and study activities in dynamic living cells with chemical specificity, high throughput, as well as high spatial resolution.

![](images/649a7e86524b8c03865bd19e8d91e25fef1e4ef4d5c263804408893082d13be3.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright purple dots against a black background, labeled (a) in top-left corner
</details>

![](images/1141a53d83112a4e3df9e5dab72417a51f914a6c8b9dbdf8b556e93ed96e0666.jpg)

<details>
<summary>text_image</summary>

(b)
-3.24 µm
0 µm
3.24 µm
y
x
z
x
</details>

![](images/3be2a2de0bb45718d493b070b1d0ed17983303cec38c9ba2322ed7f3386bee50.jpg)

<details>
<summary>text_image</summary>

i
ii
iii
iv
v
y
z
</details>

![](images/c729019412ac85c842128e2e44b6278e052a39bff409934cac2970469c8fd1b6.jpg)

<details>
<summary>scatterplot</summary>

| x (μm) | y (μm) |
| ------ | ------ |
| 0      | -3.86  |
| 3.86   | 3.86   |
</details>

![](images/3ad5a8cc37b7be5e78128bf238efc3001a5263fca8e2127b4fda3fde0e0dbe78.jpg)

<details>
<summary>natural_image</summary>

Two-panel scientific image showing purple fluorescent spots on black background, labeled (d) with z = 1.24 μm (top panel)
</details>

![](images/9e3ac2ca163c48303a1dd8d070e49e66e39432f16b49ee110aaffdbbc6112c60.jpg)

<details>
<summary>natural_image</summary>

Two-panel scientific image showing scattered bright spots against a dark background, labeled with z = -0.31 μm (top panel) and an unlabeled bottom panel.
</details>

![](images/0a86e8a3c0ca9b40c40e4862b4825d4bd03d32ba3b69a9a702696ed1d48fc9ea.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright spots on a dark background, with scale bar and red annotation indicating z = -1.85 μm (no text or symbols beyond labels)
</details>

![](images/2adc79128d94bdb52acbef1097faa53e3163497ecfd7dbf99af4bd19e657c9f0.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright spots on a black background with a color scale bar indicating depth (no text or symbols present)
</details>

![](images/dcfd2f58178a9ff2b663bcdaf58ad13da89036b9f447e31901b921a329a1e57a.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered purple and red fluorescent spots on a black background, with a scale bar and label (f) and z = -0.94 μm
</details>

![](images/9a6a7c0df45b02eab0168c046ca446bb549a516190de4ff14ed719ed6171b104.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered pink fluorescent dots on a black background, with a scale bar and text label 'z = 0 μm' (no other symbols or text)
</details>

![](images/61371a410b8ad1f83f2ff6766c8bbf80aa7ba20a150f2dbcb2907a60c10ef3b4.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered pink fluorescent dots against a black background, with a scale bar and z-value label (2.34 μm) in the top right corner.
</details>

Figure 2. Characterization of MIP-FLF system with 175 nm fluorescent beads and S. aureus. (a) Raw FLF measurement, and (b) 3D reconstructed image of 175 nm fluorescent beads distributed in 3D agarose gel, and its x-z and y-z projection. The inset images (i-v) are zoomed-in images of (b) at $z = - 1 . 8$ to $1 . 0 \ \mu \mathrm { m } .$ , with FWHM of 0.5 to 0.9 m and 0.8 to 1.1 m in the lateral and axial direction, respectively (see Fig. S2). (c) 3D reconstructed fluorescent beads and (d) zoomed-in reconstructed slices at varying depths and corresponding widefield images with the same FOV. (e) 3D reconstructed FLF image and (f) reconstructed MIP images of varying depth at 1650 cm-1 of R6G stained S. aureus prepared on a tilted Si substrate. Scale bar, 20 m; scale bar of (b) insets, 1 m.

## 3.2. 3D chemical imaging of lipid droplets in cancer cells

To demonstrate the capability of FLF-MIP system for live cell imaging, we imaged MIA-Paca2 cells stained with lipi-red (see Methods). The bright spots in Fig. 3b represent lipid droplets in a single MIA-Paca2 cell. By using a 1744-cm-1 mid-IR pump beam to excite the C=O bonds in esterified lipids, MIP modulation of lipid droplet fluorescence was demonstrated by the comparison between IR-on and IR-off frames (Fig. 3a, i and ii, respectively). After reconstruction, 3D distribution of lipid droplets in a single cell was mapped in Fig. 3b with bond-selectivity, covering a volume of \~60 μm×60 μm×4 μm. A few reconstructed depth slices are shown in Fig. 3c. Here, the depthresolved MIP-FLF images of lipi-red stained MIA-Paca2 showed rich lipid contents in cancer cells, except for the nuclei area. The 3D reconstructed MIP-FLF images with submicron level axial resolution and video acquisition rate show greater potential in quantitative chemical analysis than previous MIP microscopy in 2D manner. Furthermore, using this ultrafast 3D imaging method in living cells with chemical specificity, we are capable of studying lipid metabolism in cancer cells, such as fatty acid uptake that is beyond the reach of FLF microscopy.

![](images/7874442064da43bf181c5cf9498daac133cb4aae4c782830991942f244bf8d5d.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing cellular structures with a color scale bar (2505–196) and label (a), no readable text or symbols beyond the scale.
</details>

![](images/57d1d847729acc41a571ee3c0b508a5ef54da3e9199ef7c3051d78bfac56cb42.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing purple-stained cellular structures with a color scale bar (2505–196) and label 'ii' (no text or symbols beyond labels)
</details>

![](images/26f615c600e30bee22c3a8e7b6b9286c829922a8c8d1edcb63ebe16c46c0e1d2.jpg)

<details>
<summary>text_image</summary>

(b)
1.9 µm
0 µm
-1.9 µm
y
x
y
z
</details>

![](images/44478b2aed028894059ac7048d2c4acbd6883e70c396d6c02293cf4bb58e0873.jpg)

<details>
<summary>natural_image</summary>

3D coordinate system with X and Z axes, showing a red-orange particle cluster against black background (no text or symbols)
</details>

![](images/7aa89bb631bfdff86a5738c6c126a469ebf9b59202f9e0dee9c0c245d322c254.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright spots on a dark background, labeled (c) with z = -1.61 μm and i axis indicator (no text or symbols within the image content)
</details>

![](images/b8216a288d652efd39a0d809ecf54752969d88db44fc017f4f11497db8f862de.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright spots on a dark background, labeled with z = -0.86 μm and ii (no other text or symbols)
</details>

![](images/b6dc5b019bf108352361b6b262a1923f2292fd6a39dd70a89381606806a03fd8.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing scattered bright spots against a dark background, labeled with z = 0.10 μm and iii marker (no text or symbols beyond labels)
</details>

Figure 3. MIP-FLF imaging of lipid droplets in a MIA Paca-2 cell. The IR beam was tuned to 1744 cm-1 for the excitation of C=O bonds. (a) Raw FLF elemental images at (i) IR-on and (ii) IR-off state. (b) 3D reconstructed MIP image and its x-z and y-z projections. (c) 3D reconstructed MIP images at varying depth. Scale bar of (a, b), 20 m; scale bar of (c), 10 m.

## 3.3. MLP-FLF imaging of lipid metabolism in drug-resistant cancer cells

Lipids are essential building blocks synthesized by complex molecular pathways, from glucose or fatty acid uptake, and are stored as lipid droplets in cells. Currently, 13C metabolic flux analysis is the preferred tool for quantitative characterization of metabolic phenotypes in mammalian cells32, 33. Cells can take up long chain free fatty acids (FFA) in vivo from the non-protein bound ligand pool in extracellular fluid34. To quantitatively study fatty acid uptake in cancer cells, we treated MIA Paca-2 cells with 13C isotopically labeled fatty acids. As seen in Fig. S3,

Fourier-transform infrared spectroscopy (FTIR) of $^ { 1 3 } \mathrm { C }$ labeled fatty acid mixture showed $\mathrm { a } \sim 3 0 \ \mathrm { c m ^ { - 1 } }$ peak shift to lower wavenumber compared with $^ { 1 2 } \mathrm { C }$ palmitic acid (major contents in the $^ { 1 3 } \mathrm { C }$ fatty acid mixture). Incubating MIA Paca-2 cells with $^ { 1 3 } \mathrm { C }$ isotopic labeled free fatty acid results in the formation of intracellular neutral lipid. Consequently, the MIP peak of lipid droplets formed from $^ { 1 3 } \mathrm { C }$ fatty acid treatment is expected to display $\mathbf { a } \sim 3 0 \mathrm { c m } ^ { - 1 }$ peak shift from that for endogenous, de novo synthesized lipids $( 1 7 4 4 \mathrm { c m } ^ { - 1 } )$ ). As seen in Fig. 4c, the MIP spectra (solid curves in $\mathbf { F i g } .$ 4c) were generated by Lorentzian fitting from MIP signals of MIA Paca-2 cells (N=3) heated by mid-IR pulses ranging from 1690 to $1 7 4 5 ~ \mathrm { c m ^ { - 1 } }$ . Since the sampling rate in frequency domain of MIP-FLF imaging were limited by the photobleaching effect of the fluorescent dye, MIP-FLF images were collected only at six mid-IR wavenumbers for each cell. Lipid droplets in $^ { 1 3 } \mathrm { C }$ fatty acid treated cells (red) showed MIP peaks shift to shorter vibrational frequency, while those without $^ { 1 3 } \mathrm { C }$ fatty acid treatment (green) remained at $1 7 4 4 \mathrm { c m } ^ { - 1 }$ . Besides, cells treated with $^ { 1 3 } \mathrm { C }$ fatty acid of high concentration (red) displayed higher MIP signals at $^ { 1 3 } \mathrm { C } \mathrm { = } \mathrm { O }$ peak than those of low concentration (light red). This indicates that our isotopically labeled MIP-FLF imaging method is capable of quantitative study of lipid metabolism. Taking the ratio of the MIP intensity between $1 7 0 4 \mathrm { c m } ^ { - 1 }$ and $1 7 4 4 \mathrm { c m } ^ { - 1 }$ , the lipid chemical components of MIA-Paca2 were demonstrated in Fig. 4a, b, where the red colormap represented lipid droplets formed from fatty acid uptake and the green color mapped endogenous lipid. Here, the ratio colormap of MIA Paca-2 confirmed rich lipid contents in cancer cells from fatty acid pathway, while the restored MIP spectra demonstrated the fatty acid uptake quantitatively.

Next, we used the MIP-FLF ratio image to study altered fatty acid metabolism in drug-resistant pancreatic cancer cells by comparing the gemcitabine-sensitive MIA PaCa-2 cells and gemcitabine-resistant G3K cells (See Methods). Based on the lipid pathway tracing method discussed above, we can distinguish between exogenous and endogenous lipid of living cells. Here, both G3K group and MIA Paca-2 group were treated with $^ { 1 3 } \mathrm { C }$ fatty acids with the same concentration and culture time. In the depth-resolved MIP-FLF reconstructed image stacks (Fig. 4d), drug-resistant G3K group shows higher MIP intensity at $1 7 0 4 \ \mathrm { c m ^ { - 1 } }$ (red) than the MIA Paca-2 cell. As compared in the statistical analysis of the lipid droplets in MIA Paca-2 (N=3) and G3K (N=3) cells (Fig. 4e, S4), G3K group displayed exceedingly more $^ { 1 3 } \mathrm { C = O }$ than MIA Paca-2 group. As a result, we concluded that gemcitabine-resistant G3K cells more rely on exogenous fatty acids than gemcitabine-sensitive MIA PaCa-2 cells. Meanwhile, the G3K cells showed distinctly longer protrusions than MIA Paca- $^ { - 2 , }$ , and the protrusions were rich in lipid droplets. These observations can also serve as markers to determine drug resistance of cancer cells.

![](images/00e09c2edc8e19a1c050e0ecca4a248d6cbc25011350e98ffe2f57f1591ca974.jpg)  
Figure 4. MIP-FLF imaging of lipid droplets in MIA Paca-2 and G3k cells treated with 13C fatty acids. (a-b) MIP intensity from 3D MIP-FLF reconstructed stack of 13C fatty acid treated MIA-Paca-2 cells (a) and the control group (b) without fatty acid treatment imaged at 1704 cm-1 (red) overlayed with that from 1744 cm-1 (green). (c) MIP spectra of MIA Paca-2 cells treated with (red, 25g/L, light red, 12.5g/L) and without (green) 13C fatty acid. The solid curves are Lorentzian fitted MIP spectra (N=3). (d) MIP intensity colormap of 13C fatty acid treated MIA-Paca-2 cells (top) and G3K cells (bottom) (green, 1744 cm-1, red, 1704 cm-1) at varying depths. (e) The ratio of MIP intensity between 13C=O at 1704 cm-1 and 12C=O at 1744 cm-1 (top). Statistical analysis of lipid content in 13C fatty acid treated MIA Paca-2 cells (N=3) and G3K cells (N=3). Scale bar 20 m.

## 4. Discussion

We developed MIP-FLF microscopy that allows single-shot volumetric chemical imaging with infrared spectroscopic information at an 8-Hz volume rate. The image volume was 60 μm×60 μm×4 μm with a lateral resolution of 0.5-0.9 m and an axial resolution of 0.8-1.1 m. FLF microscopy provides an unprecedented 3D imaging speed that cannot be achieved with the confocal microscope, which takes a few seconds to scan the sample voxel by voxel. The MIP sets additional requirement for the confocal scanning when detecting the fluorescence intensity modulation induced by the mid-IR pulse. The pump mid-IR laser can only operate at a limited repetition rate, which is determined by not only the laser pulse repetition rate, but also the thermal decay time to avoid heat accumulation. In addition, to get enough SNR, long pixel dwell time is used experimentally and thus further decreases the scanning speed and makes confocal measurement not an optimal method for high-speed volumetric chemical imaging. The light sheet microscopy has several benefits over the confocal laser scanning microscopy. The plane-scanning speed is faster than point-scanning speed and also diminish the photobleaching issue. However, all these scanning-based methods are no capable of imaging 3D volume in a single snapshot.

The MIP-FLF system is compact and simple, since it does not require any mechanical movements. Meanwhile, the single-shot volumetric system is more stable than scanning-based methods, which plays a significant role in MIP detections. During the MIP measurements, mechanical fluctuation induced by scanning or rotation will introduce strong artifacts after the subtraction of images at IR-on and IR-off states, thus is detrimental to the restoration of spectroscopic information. Furthermore, the ultrahigh speed of MIP-FLF imaging also mitigate the laser fluctuation issue during MIP detections.

In the reported MIP-FLF microscope, single-shot chemical 3D volumes captured in half of the camera frame rate contains volumetric chemical information in video rate. However, real-time volumetric spectroscopic imaging is still challenging due to the long reconstruction time. Recently, deep learning framework has emerged as the state-of-theart to perform fast and reliable reconstruction for various volumetric fluorescence microscopes35-37. We anticipate that our system could achieve video-rate reconstruction speed by replacing the current iterative method with deep learning framework, which is especially beneficial for biomedical application.

In summary, via the development of MIP-FLF microscopy, we demonstrated single-shot volumetric chemical imaging of lipid contents in living cells and further studied the lipid metabolism in drug-resistant cancer cells with infrared spectroscopic selectivity. Specifically, we distinguished lipids from exogeneous fatty acids versus those from de novo synthesis, which cannot be fulfilled with fluorescence imaging alone. Meanwhile, in our MIP-FLF design, we relied on fluorescence intensity modulations to sense the MIP effect. As a result, we can only get MIP contrast from the molecules stained with certain fluorescent dyes, and photobleaching issue is sometimes not negligible. To mitigate these issues and broaden the potential applications, label-free single-shot volumetric chemical imaging will be pursued in our future work.

## Acknowledgments

This work is supported by R01EB032391 to J.X.C. and L.T., R35GM136223, R01AI141439, R33CA261726 to J.X.C.

## Disclosures

J.X.C. declares a financial interest with Photothermal Spectroscopy Corp.

## References

1. H. U. Dodt, U. Leischner, A. Schierloh, N. Jährling, C. P. Mauch, K. Deininger, J. M. Deussing, M. Eder, W. Zieglgänsberger, and K. Becker, "Ultramicroscopy: three-dimensional visualization of neuronal networks in the whole mouse brain," Nat Methods 4, 331-336 (2007).  
2. T. A. Planchon, L. Gao, D. E. Milkie, M. W. Davidson, J. A. Galbraith, C. G. Galbraith, and E. Betzig, "Rapid three-dimensional isotropic imaging of living cells using Bessel beam plane illumination," Nat Methods 8, 417-423 (2011).  
3. A. Bodén, F. Pennacchietti, G. Coceano, M. Damenti, M. Ratz, and I. Testa, "Volumetric live cell imaging with three-dimensional parallelized RESOLFT microscopy," Nat Biotechnol 39, 609-618 (2021).  
4. M. Gu, "Principles of three dimensional imaging in confocal microscopes," World Scientific (1996).  
5. W. Denk, J. H. Strickler, and W. W. Webb, "Two-photon laser scanning fluorescence microscopy." Science 248, 73-76 (1990).  
6. H. Oku, K. Hashimoto, and M. Ishikawa, “Variable-focus lens with 1-kHz bandwidth,” Opt. Express 12, 2138–2149 (2004).  
7. M. D. Maschio, A. M. D. Stasi, F. Benfenati, and T. Fellin, “Three- dimensional in vivo scanning microscopy with inertia-free focus control,” Opt. Lett. 36, 3503–3505 (2011).  
8. P. J. Keller, A. D. Schmidt, J. Wittbrodt, and E. H. Stelzer, "Reconstruction of zebrafish early embryonic development by scanned light sheet microscopy," Science 322, 1065-1069 (2008).  
9. J. Huisken, J. Swoger, F. Del Bene, J. Wittbrodt, and E. H. Stelzer, "Optical sectioning deep inside live embryos by selective plane illumination microscopy," Science 305, 1007-1009 (2004).  
10. M. B. Bouchard, V. Voleti, C. S. Mendes, C. Lacefield, W. B. Grueber, R. S. Mann, R. M. Bruno, and E. M. Hillman, "Swept confocally-aligned planar excitation (SCAPE) microscopy for high speed volumetric imaging of behaving organisms," Nat Photonics 9, 113-119 (2015).  
11. J. Mertz, " Strategies for volumetric imaging with a fluorescence microscope," Optica 6, 2334-2536 (2019).  
12. M. Levoy, R. Ng, A. Adams, M. Footer, M. Horowitz, "Light field microscopy," ACM SIGGRAPH, 924-934 (2006).  
13. C. Guo, W. Liu, X. Hua, H. Li, and S. Jia, "Fourier light-field microscopy," Opt Express 27, 25573-25594 (2019).  
14. W. Liu, and S. Jia, "wFLFM: enhancing the resolution of Fourier light-field microscopy using a hybrid wide-field image," Appl Phys Express 14 (2021).  
15. X. Hua, W. Liu, and S. Jia, "High-resolution Fourier light-field microscopy for volumetric multi-color live-cell imaging," Optica 8, 614- 620 (2021).  
16. Y. Xue, I. G. Davison, D. A. Boas, and L. Tian, "Single-shot 3D wide-field fluorescence imaging with a Computational Miniature Mesoscope," Sci Adv 6 (2020).  
17. J. X. Cheng and X. S. Xie, "Vibrational spectroscopic imaging of living systems: An emerging platform for biology and medicine," Science 350, 6264 (2015).  
18. H. J. Lee, Y. Jiang, and J. X. Cheng, "Label-free Optical Imaging of Membrane Potential," Curr Opin Biomed Eng 12, 118-125 (2019).  
19. K. C. Huang, J. Li, C. Zhang, Y. Tan, and J. X. Cheng, "Multiplex Stimulated Raman Scattering Imaging Cytometry Reveals Lipid-Rich Protrusions in Cancer Cells under Stress Condition," iScience 23, 100953 (2020)  
20. F. Hu, M. R. Lamprecht, L. Wei, B. Morrison, and W. Min, "Bioorthogonal chemical imaging of metabolic activities in live mammalian hippocampal tissues with stimulated Raman scattering," Sci Rep 6, 39660 (2016).  
21. X. Chen, C. Zhang, P. Lin, K. C. Huang, J. Liang, J. Tian, and J. X. Cheng, "Volumetric chemical imaging by stimulated Raman projection microscopy and tomography," Nat Commun 8, 15117 (2017).  
22. F. Hu, L. Shi, and W. Min, "Biological imaging of chemical bonds by stimulated Raman scattering microscopy," Nat Methods 16, 830- 842 (2019).  
23. C. Qian, K. Miao, L. E. Lin, X. Chen, J. Du, and L. Wei, "Super-resolution label-free volumetric vibrational imaging," Nat Commun 12, 3648 (2021).  
24. D. Zhang, C. Li, C. Zhang, M. N. Slipchenko, G. Eakins, and J. X. Cheng, "Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution," Sci Adv 2, e1600521 (2016).  
25. Y. Bai, D. Zhang, L. Lan, Y. Huang, K. Maize, A. Shakouri, and J. X. Cheng, "Ultrafast chemical imaging by widefield photothermal sensing of infrared absorption," Sci Adv 5, eaav7127 (2019).  
26. M. Tamamitsu, K. Toda, R. Horisaki, and T. Ideguchi, "Quantitative phase imaging with molecular vibrational sensitivity," Opt Lett 44, 3729-3732 (2019).  
27. D. Zhang, L. Lan, Y. Bai, H. Majeed, M. E. Kandel, G. Popescu, and J. X. Cheng, "Bond-selective transient phase imaging via sensing of the infrared photothermal effect," Light Sci Appl 8, 116 (2019).  
28. M. Tamamitsu, K. Toda, H. Shimada, T. Honda, M. Takarada, K. Okabe, Y. Nagashima, R. Horisaki, and T. Ideguchi, "Label-free biochemical quantitative phase imaging with mid-infrared photothermal effect," Optica 7, 359-366 (2020).  
29. J. Zhao, A. Matlock, H. Zhu, Z. Song, J. Zhu, B. Wang, F. Chen, Y. Zhan, Z. Chen, Y. Xu, X. Lin, L. Tian, Ji. X. Cheng et al. "Bondselective intensity diffraction tomography." arXiv preprint arXiv:2203.13630 (2022).  
30. Y. Zhang, H. Zong, C. Zong, Y. Tan, M. Zhang, Y. Zhan, and J. X. Cheng, "Fluorescence-Detected Mid-Infrared Photothermal Microscopy," J Am Chem Soc 143, 11490-11499 (2021).  
31. M. Li, A. Razumtcev, R. Yang, Y. Liu, J. Rong, A. C. Geiger, R. Blanchard, C. Pfluegl, L. S. Taylor, and G. J. Simpson, "Fluorescence-Detected Mid-Infrared Photothermal Microscopy," J Am Chem Soc 143, 10809-10815 (2021).  
32. W. Dong, M. A. Keibler, and G. Stephanopoulos, "Review of metabolic pathways activated in cancer cells as determined through isotopic labeling and network analysis," Metab Eng 43, 113-124 (2017).  
33. M. G. Badur, and C. M. Metallo, "Reverse engineering the cancer metabolic network using flux analysis to understand drivers of human disease," Metab Eng 45, 95-108 (2018).  
34. P. D. Berk, and D. D. Stump, "Mechanisms of cellular uptake of long chain free fatty acids," Mol Cell Biochem 192, 17-31 (1999).  
35. Z. Wang, L. Zhu, H. Zhang, G. Li, C. Yi, Y. Li, Y. Yang, Y. Ding, M. Zhen, S. Gao, T. K. Hsiai, P. Fei, "Real-time volumetric reconstruction of biological dynamics with light-field microscopy and deep learning," Nat Methods 18, 551–556 (2021).  
36. N. Wagner, F. Beuttenmueller, N. Norlin, J. Gierten, J. C. Boffi, J. Wittbrodt, M. Weigert, L. Hufnagel, R. Prevedel, A. Kreshuk, "Deep learning-enhanced light-field imaging with continuous validation," Nat Methods 18, 557–563 (2021).  
37. Y. Xue, Q. Yang, G. Hu, K. Guo, L. Tian, et al. "Computational Miniature Mesoscope V2: A deep learning-augmented miniaturized microscope for single-shot 3D high-resolution fluorescence imaging." arXiv preprint arXiv:2205.00123 (2022).