A R T I C L E

O p e n A c c e s s

# Mid-infrared chemical imaging of intracellular tau fibrils using fluorescence-guided computational photothermal microscopy

Jian Zhao 1,2✉, Lulu Jiang3 , Alex Matlock 1,8, Yihong Xu4 , Jiabei Zhu1 , Hongbo Zhu 5 , Lei Tian 1,6 iD Benjamin Wolozin3 and Ji-Xin Cheng 1,4,6,7✉

## Abstract

Amyloid proteins are associated with a broad spectrum of neurodegenerative diseases. However, it remains a grand challenge to extract molecular structure information from intracellular amyloid proteins in their native cellular environment. To address this challenge, we developed a computational chemical microscope integrating 3D midinfrared photothermal imaging with fluorescence imaging, termed Fluorescence-guided Bond-Selective Intensity Diffraction Tomography (FBS-IDT). Based on a low-cost and simple optical design, FBS-IDT enables chemical-specific volumetric imaging and 3D site-specific mid-IR fingerprint spectroscopic analysis of tau fibrils, an important type of amyloid protein aggregates, in their intracellular environment. Label-free volumetric chemical imaging of human cells with/without seeded tau fibrils is demonstrated to show the potential correlation between lipid accumulation and tau aggregate formation. Depth-resolved mid-infrared fingerprint spectroscopy is performed to reveal the protein secondary structure of the intracellular tau fibrils. 3D visualization of the β-sheet for tau fibril structure is achieved.

## Introduction

Alzheimer’s Disease (AD) affects nearly fifty million people worldwide1 . Individuals with AD develop cognitive impairment including memory loss that eventually progresses to death. As an important type of amyloid protein aggregates, tau aggregates are a pathological hallmark of AD and related neurodegenerative disorders2,3 . The mechanism of tau aggregate formation and the pathways underlying tau-induced diseases are still not well understood. Characterizing the geometrical morphologies and chemical structures of tau aggregates in their cellular native states can provide valuable structural and functional information useful for uncovering the mechanisms of tauopathies and for developing therapeutics. To this end, there are several challenges to overcome. First, the tau protein aggregates are predominantly intracellular, and their formation is sensitive to molecular environments2,4,5 . It is, therefore, highly desired to perform noninvasive and intracellular characterizations, which require sub-cellular resolutions and compatibilities with intracellular fluid environments. Second, aggregates formed by different isoforms and conformers of tau exhibit remarkable structural diversity at the atomic level associated with distinct tauopathies5–7 . The same protein can also form distinct structures with respect to both morphologies and molecular arrangements5 . In addition, β sheets constitute the main secondary protein structures of tau aggregates and other types of amyloid protein aggregates 8,9 Therefore, it is preferable to develop methods that can resolve 3D morphological and chemical heterogeneities and are sensitive to β-sheet secondary structure. Third, the interplay between amyloid protein aggregates, including tau aggregates, and lipid droplets might play an essential role in the formation of tau aggregations but is not fully understood10–13, requiring a method that enables the characterizations of lipids and protein simultaneously.

To tackle these challenges, various techniques have been applied to characterize tau aggregates and other amyloid protein aggregates. Structural biology tools14,15, including X-ray crystallography, small-angle X-ray scattering, nuclear magnetic resonance spectroscopy, and Cryo-Electron Microscopy (Cryo-EM), have played pivotal roles in determining atomic-level structures of amyloid fibrils16–19, α-synuclein oligomers20 tau protein21,22, and tau filaments23,24. However, these methods require purified protein samples with complicated sample preparation s14,25–27, making it challenging to directly analyze intracellular tau aggregates in cells. In addition, the related instrumentations and usages are expensive28 (e.g. \~\$7 million for buying a Cryo-EM and \~\$10,000 operational cost per day), imposing additional restrictions. The spectroscopy method, Circular Dichroism (CD) spectroscopy, can provide rapid secondary protein structure quantifications for samples in dilute solutions20,29,30. Yet, CD spectroscopy lacks high predictive accuracy for β-sheet secondary structures29. More importantly, the spectroscopic method usually lacks site-specific information, leading to difficulties in attributing spectral features to the structural heterogeneity of protein aggregates. Imaging methods, such as Positron Emission Tomography (PET) and fluorescence imaging, have also been applied to investigate neurodegenerative diseases. PET enables the brain-wide amyloid-β contents imaging with radiotracer but has a low spatial resolution (\~2 mm)31–33. Fluorescence imaging is popular for high-resolution and high-fidelity intracellular imaging of tau aggregates but lacks the capabilities of quantifying secondary protein structures4,34,35. Overall, the abovementioned solutions are fundamentally limited by their inability to perform cost-effective, non-invasive 3D imaging and analysis of amyloid proteins’ morphology and chemical structure in the cellular fluid.

Vibrational spectroscopic imaging, including Raman and Infrared (IR)-based methods, can potentially circumvent the abovementioned technique barriers based on cost-effective solutions for imaging amyloid protein aggregates in their native states. For Raman-based solutions, stimulated Raman scattering microscopy and tipenhanced Raman spectroscopic imaging have been applied to investigate tau fibrils, amyloid plaques, and protein aggregates related to polyglutamine diseases36–41 However, Raman scattering is a weak process with an extremely small cross-section of $\mathrm { \sim } 1 0 ^ { - 3 0 } \mathrm { \dot { ~ } t o } \sim 1 0 ^ { - 2 8 } \mathrm { c m } ^ { 2 } .$ Due to this limitation, Raman imaging systems are based on point-scanning configurations with tightly focused high-power laser beams, resulting in low imaging speed, weak signals in the amide bands, and a high potential for photodamage42. In addition, Raman has difficulties in discriminating parallel β-sheet protein from anti-paralle β-sheet protein without ambiguities, while β-sheet protein constitutes the most important secondary structure of amyloid protein aggregates8,9 . In comparison, IR-based spectroscopic imaging solutions are more suitable for detecting amyloid protein aggregates, such as tau fibrils and oligomers. First, IR absorption offers a cross-section of \~10−18 cm2 that is ten orders of magnitude larger than Raman scattering43. An important advantage of IR lies in its exceptional sensitivity to changes in the chemical bond strength as well as variations in β-sheet protein secondary structure in amide bands since a change of 0.02% can be easily detected9,44. Therefore, IR-based spectroscopic imaging methods feature higher sensitivity, greater accuracy and are free from a requirement of tightly focused beam designs with a resulting reduction in the risk of photodamage while detecting intracellular tau protein aggregates. Conventional IR spectroscopy methods can provide sensitive and accurate protein secondary structure analysis but lack high spatial resolution and sitespecific information45,46. Atomic Force Microscopy IR (AFM-IR) spectroscopy overcomes issues arising from low spatial resolution but is limited to 2D and requires dry samples, which could alter the structure of the tau aggregates due to changes in the native intracellular fluid environment47,48.

The emerging Mid-IR Photothermal (MIP) microscopy49 also called Optical Photothermal IR (OPTIR) microscopy, opens a new avenue to detect amyloid protein aggregates. MIP microscopy inherits the advantages of IR spectroscopy while enabling hyperspectral 2D/3D chemical cell imaging with diffraction-limited resolution in the visible band, and being compatible with both point-scanning and widefield imaging configurations 50–58 Prior studies show that MIP microscopy enables 2D imaging and mid-IR fingerprint spectra extractions on polymorphic amyloid aggregates in neurons using point-scanning systems59. Despite this significant progress, demonstrated MIP-based characterizations of amyloid proteins still cannot uncover the 3D heterogeneity of amyloid protein aggregates using 2D imaging data and averaged spectra due to the system design. 3D MIP imaging of normal intracellular proteins is achieved by integrating infrared excitation with optical diffraction tomography55 and intensity diffraction tomography58 . Yet, 3D chemical imaging of intracellular amyloid protein aggregates has not been reported. Without additional guidance, these volumetric imaging and spectroscopic analysis methods of amyloid protein aggregates suffer because the weak amyloid protein signal tends to be overwhelmed by background signals from other proteins and the immersion medium.

In this work, we present a fluorescence-guided computational MIP microscope for 3D bond-selective imaging of intracellular amyloid protein aggregates (tau fibrils) as well as lipid content in the fluid environment of a cell. Our scheme can differentiate amyloid protein aggregate signatures from the background protein signals, extract 3D site-specific mid-IR fingerprints spectra, and provide high-resolution 3D visualizations of aggregate secondary structure. Our method, termed Fluorescence-guided Bond-Selective Intensity Diffraction Tomography (FBS-IDT), integrates a simple 2D fluorescence imaging modality within a chemical intensity diffraction tomography framework. FBS-IDT uses 2D fluorescence imaging as the guide star for differentiating the amyloid protein aggregates from other proteins within a large Field Of View (FOV). Then, FBS-IDT performs time-gated pump-probe hyperspectral detection to capture 3D Refractive Index (RI) variations per mid-IR wave number to generate both 3D chemical imaging results and site-specific depthresolved mid-IR spectra. Based on protein secondary structure analysis, 3D visualization of the secondary structure compositions can be realized. Notably, FBS-IDT is a cost-effective table-top microscope developed from commercially available components, which fit most laboratories’ routine usage. Compared to various state-ofthe-art techniques, FBS-IDT resolves the difficulties of 3D chemical imaging of amyloid protein aggregates and their secondary protein structure in their native intracellular fluid environment for the first time. In the following sections, we first illustrate FBS-IDT’s principle and system design. Then, we demonstrate high-fidelity 3D chemical imaging of intracellular tau fibrils and lipid contents and showcase their potential correlations at the single-cell level. Next, we show that depth-resolved mid-IR fingerprint spectra can be extracted from tau fibrils and reveal the chemical structure differences between tau fibrils and diffusive tau protein. Finally, we demonstrate depthresolved protein’s secondary structure analysis and 3D visualization of tau fibrils’ β sheets structure.

## Results

## FBS-IDT principle, workflow, and instrumentation

FBS-IDT integrates the 3D label-free chemical imaging modality with a simple 2D single-photon fluorescence imaging modality. The chemical imaging modality utilizes a pump-probe MIP tomography imaging scheme to provide 3D chemical imaging information with high temporal and spatial resolution as well as site-specific mid-IR fingerprint spectra. Within this framework, the mid-IR pump laser induces chemical-specific volumetric MIP effects, and the visible probe laser images the induced 3D RI variations. Meanwhile, the 2D fluorescence imaging modality can extract the target amyloid protein aggregates from background protein signals. This 2D image can work as the guide star for the chemical imaging modality to perform the site-specific mid-IR protein secondary structure analysis, which can determine the spectral locations and areas of secondary structures. Finally, 3D visualization of protein secondary structures for amyloid protein aggregates can be achieved using the spectral ratio map.

The principle of 3D label-free chemical quantitative phase imaging is illustrated in Fig. 1a–d. FBS-IDT relies on the MIP effects from the mid-IR fingerprint region, where each absorption peak corresponds to a unique molecular vibrational bond60, to generate the molecularspecific 3D RI maps. As shown in Fig. 1a, a pulsed and tunable mid-IR pump beam is incident on the sample and absorbed by the particular chemical compositions. This chemical-specific absorption changes the temperature and causes local sample expansions that modify the local RI distributions61. Meanwhile, each pulsed visible probe beam from the customized laser ring array is synchronized with the mid-IR laser pulse to image the MIPinduced RI variations. This pump-probe detection is a transient process in that the local heat can dissipate within a few microseconds to tens of microseconds61,62. Here, the 3D RI sample map is reconstructed using the IDT method (Methods). The IDT method implements a physical model that relates the sample’s properties to the scattering information recorded by the 2D intensity images based on the first-Born approximation63–65. Under this approximation, the scattered field from each point within the object space is independent and allows the 3D object to be treated as an axially discretized set of decoupled 2D slices. This discretization enables slice-wise 3D reconstruction of the object’s RI map using deconvolution. As shown in Fig. 1b, the 2D intensity image captured under each oblique probe illumination contains the linearized cross-interference information that can be mapped onto shells of an Ewald’s sphere in the 3D frequency domain. The object’s 3D RI map can be reconstructed by transforming the synthesized Ewald’s sphere to the spatial domain using the data from 16 different probe illuminations65. 3D RI map reconstructions are performed for both “Cold” and “Hot” states (Fig. 1c). The “Cold” and “Hot” states are created by the high-speed modulation of the pump mid-IR laser between the “Off” and the “On” states, where the chemical-specific MIPinduced RI variations are absent or present. The chemical-specific 3D RI variation map under a particular mid-IR wavenumber is recovered by the subtraction between “Hot” and “Cold” 3D RI maps. Repeating the chemical RI map extractions for the mid-IR fingerprint region can generate the 4D hyperspectral chemical images that contain 3D site-specific mid-IR spectra information (Fig. 1d).

Fluorescence-guided amyloid protein aggregate chemical information extractions are illustrated in Fig. 1e–g. First, the FBS-IDT is switched to fluorescence imaging

a  
![](images/3d92dbd65913fe0f3f292a8734c509a6dc293d6a4eea81c59bab444f79fa9970.jpg)

<details>
<summary>text_image</summary>

Mid-IR laser beam
Probe laser beam
Sample
</details>

b  
![](images/36b2444c3edfcc5e430265f5a4e9833fe20dcdf348543dd29425c2b90b8ff564.jpg)

<details>
<summary>text_image</summary>

Laser 1
Laser 6
16 Lasers
Spatial frequency
v_z
v_y
v_x
...
...
...
v_z
v_y
v_x
...
...
v_z
v_y
v_x
</details>

![](images/f12c991b9cdeb71429fd9ecc57ad2908ee97ff6ac653f380741da191dc898620.jpg)

<details>
<summary>text_image</summary>

C
Mid-IR laser off: "Cold"
Probe laser beam
Mid-IR laser on: "Hot"
Probe laser beam
Mid-IR wavenumber tuning
</details>

![](images/bcbf3a326ee5e28888a947c47ed73155ffdffd508446263d62c6a125367dbc43.jpg)

<details>
<summary>text_image</summary>

d
4D imaging data: 3D images varying with mid-IR wavenumbers
Wavenumber
</details>

![](images/432587fa009eaff6a11e4d1ae24e31d90128191e76a2f26861e3eb65a8020dca.jpg)

<details>
<summary>text_image</summary>

Excitation laser beam
Sample
2D image
Amyloid protein aggregates
</details>

![](images/eb73a081cebfd2b481dbff34481f18bdf1138b0b0100f19ae86937127962e91f.jpg)

<details>
<summary>line chart</summary>

| Wavenumber | Mid-IR fingerprint spectra | Secondary structure analysis |
| ---------- | -------------------------- | ---------------------------- |
| Depth      | Peak (approximate)         | Peak (approximate)           |
| Amide I band | Approximate peak (approximate) | Approximate peak (approximate) |
</details>

![](images/c80dee20c777004edd6ea4deb510f487d936da8e75b540f234559da95f3f30c2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Secondary protein structure"] -->|v₁/v₂| B["Structure 1"]
  A -->|v₁/v₂| C["Structure 2"]
  B --> D["Structure 3"]
  C --> D
  D --> E["Amide I band"]
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#bbf,stroke:#333
    style D fill:#dfd,stroke:#333
    style E fill:#dfd,stroke:#333
```
</details>

Fig. 1 FBS-IDT principle and workflow. a Pump-probe 3D chemical imaging scheme. Each oblique pulsed probe beam (\~450 nm) from a ring lase array illuminates the sample sequentially. A loosely focused pulsed mid-IR laser pump beam heats the sample periodically. b 3D RI map reconstruction scheme. Intensity imaging data from each probe beam illumination are mapped into the frequency domain. 3D RI map can be reconstructed by the inverse Fourier transform of the synthesized frequency domain information from all 16 probe beam detections. c “Cold” state: imaging without mid-IR pump beam illumination; “Hot” state: imaging with mid-IR pump beam illumination. d 4D hyperspectral chemical imaging. 3D chemical maps under different mid-IR wavenumbers are obtained in two steps: (1) subtracting “Hot” 3D RI maps from the “Cold” 3D RI maps under a particular wavenumber; (2) tuning the wavenumber to obtain 3D maps for different chemical compounds of interest. e Single-photon 2D fluorescence intensity imaging. To obtain the 2D guide star, both probe and pump beams are turned off while an excitation laser beam illuminates the sample. The 2D fluorescence images highlight the boundary of the amyloid protein aggregates. f Depth-resolved mid-IR fingerprint spectra generation and related protein secondary structure spectroscopic analysis. The depth-resolved mid-IR spectra are extracted from the 4D hyperspectral chemical imaging data under the guidance of the 2D image in (e). Secondary structures are analyzed by the deconvolution of the mid IR amide I band. g 3D visualization of protein secondary structure for the amyloid protein aggregates. Based on the spectroscopic analysis results in (f), spectral positions for specific secondary protein structures are selected. 3D visualization of the secondary protein structures is obtained by extracting the mid-IR spectral ratio map between two 3D chemical images. Cell and protein aggregate icons in (b–e) and (g) are created and adapted from ref. 89

mode by activating the 488 nm excitation laser beam and adding spectral filters (Fig. 1e). The excitation laser beam illuminates the sample labeled by Green Fluorescent Protein (GFP). A 2D single-photon fluorescence emission intensity image is recorded on the same camera. This 2D intensity image serves as a guide star to differentiate the boundary between the normal protein and the amyloid protein aggregates. Under the guidance of the 2D fluorescence image, we can extract the site-specific mid-IR fingerprint spectra from the target areas in the 4D hyperspectral chemical images (Fig. 1f). A peak deconvolution of amide I bands in those spectra enables the protein’s secondary structure analysis46,60 (“Methods” section), which resolves and quantifies the positions and areas of different protein bands, such as α-helical structures and β-sheet structures (Fig. 1f). Based on the analysis in Fig. 1f, we can generate the mid-IR spectral ratio map using two 3D chemical images corresponding to selected secondary structure positions (Fig. 1g). In this work, we mainly use this ratio map method59,66,67 to visualize 3D β-sheet structure distribution. Overall, FBS-IDT enables the characterization of intracellular chemical compositions in cellular fluid environments, including the 4D hyperspectral chemical imaging information, the 3D site-specific mid-IR fingerprint spectroscopy, and the 3D visualization of protein secondary structure. The abovementioned information fully characterizes the intracellular amyloid protein aggregates and provides 3D chemical information for other important organelles, such as lipid droplets, correlated to protein aggregates formation.

The FBS-IDT’s system design is demonstrated in Fig. 2. More details about the hardware can be found in Methods. FBS-IDT is based on a simple brightfield transmission microscope constructed using a microscope objective, a tube lens, and a CMOS camera (Fig. 2a, b). The unique add-on elements are the customized 450 nm laser ring array containing 16 low-cost diode lasers, the tunable mid-IR Quantum-Cascade Laser (QCL), and the 488 nm excitation laser. The mid-IR laser beam and the 488 nm excitation laser beam share the same beamline. The 450 nm laser, the mid-IR laser, and the excitation laser work as the probe beam, the pump beam, and the fluorescence excitation beam, respectively. The illumination angle per probe laser beam matches the objective’s Numerical Aperture (NA), maximizing the imaging system’s spatial frequency coverage63 This spatial frequency enhancement expands the accessible bandwidth following the synthetic aperture principles68 and enables the diffraction-limited resolution (\~350 nm laterally, \~1.1 µm axially) equivalent to incoherent imaging systems58 For the MIP-induced RI variations, we use an off-axis gold parabolic mirror to loosely focus the mid-IR pump beam on the sample with a beam spot size of 63 µm Full width at half maximum (FWHM). This beam spot size is sufficiently large for widefield single-cell imaging. During data acquisition, FBS-IDT is first operated under the fluorescence mode using the 488 nm excitation laser beam to guide MIP-based imaging (Fig. 2a). After obtaining the 2D guide-star image, the FBS-IDT turns on the pump-probe detection beams and performs 3D chemical quantitative phase imaging (Fig. 2b). Since the 3D chemical quantitative phase imaging detects the transient RI fluctuation within the microsecond time scale, time synchronization is essential to capture high Signal-to-Noise Ratio (SNR) images. To this end, both the probe laser and the mid-IR laser are modulated under pulse modes (\~10 kHz repetition rate and \~1 µs pulse duration) for transient pump-probe photothermal detection (Fig. 2c). An additional 50 Hz modulation is applied to the mid-IR laser to create “Hot” and “Cold” states since the CMOS camera is running at 100 Hz. Based on this design, the 3D chemical quantitative phase imaging speed can reach up to ${ \sim } 6 \mathrm { H z } ^ { 5 8 }$ . Overall, FBS-IDT features a simple and costeffective system design and enables intracellular volumetric high-resolution, high-speed chemical imaging and site-specific spectroscopic analysis of amyloid protein aggregates in intracellular fluid environments.

## 3D bond-selective imaging of intracellular lipids and proteins

Lipid homeostasis plays a vital role in maintaining normal neuronal functions. Dysregulation of lipid metabolism has been observed to correlate with neurodegenerative diseases10,13. Previous imaging research confirmed the co-localization of lipid compositions with amyloid protein deposits in tissues69–71. Despite this progress, the role of lipids in neurodegenerative diseases is still not clear. It requires imaging tools to investigate the interplay between lipids and amyloid protein aggregates. To this end, 3D chemical imaging is highly desired for visualizing different intracellular chemical compositions in a fluid environment. In Fig. 3, we demonstrate label-free hyperspectral 3D chemical imaging on fixed human epithelial cells (Tau RD P301S FRET Biosensor cells). The cells in the experimental group were cultured with seeded tau fibril fractions, while the cells in the control group were cultured without tau fibril seeding (“Methods” section). All the cell samples were fixed, washed, and immersed in $\mathrm { D } _ { 2 } \mathrm { O }$ Phosphate-Buffered Saline (PBS) between two pieces of 0.2-mm-thick Raman-grade $\mathrm { C a F } _ { 2 }$ glasses. $\mathrm { D } _ { 2 } \mathrm { O } .$ -based PBS demonstrates a relatively flat spectral response and minimizes the overlap between the amide I protein band and the O–H bending vibration from water72. Cells in both the experimental and control groups were imaged under the same mid-IR laser illuminations. Figure 3a–d (see Fig. S1 in the Supplementary Information for more data) demonstrate depth-resolved reconstructions of the cell with tau fibrils under four different conditions: (a) RI map without mid-IR laser illumination; (b) protein absorption map in the amide I band; (c) lipid absorption map; (d) RI variation map at the cell-silent window (1800–2700 cm−1 ) where minimal RI changes are expected. Based on the above imaging results, the variation of cellular features along different axis positions can be clearly observed. The chemical-specific cellular features only appear under the corresponding mid-IR fingerprint wavenumbers, resulting in the distinct morphology between the protein and the lipid maps. The chemical images from the cell-silent window confirm that the imaging contrast originates from MIP-induced absorption. Halo patterns and missing-cone artifacts are wellknown and commonly observed in quantitative phase imaging 73–75 . Our FBS-IDT method inevitably suffers from these artifacts. Nevertheless, these artifacts in our reconstructions are insignificant. Our FBS-IDT method successfully reconstructs the true features of the objects with high fidelity. We further illustrate our system’s high reconstruction fidelity on an artificial polymethyl methacrylate bead phantom (Supplementary Information: 3D bond-selective imaging of an artificial phantom).

![](images/53eb7a326ae9e833efaca2a00c92552b56502a9a26030ce88d3cbabae19c39ac.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Probe laser ring"] --> B["Excitation filter"]
  B --> C["Focusing mirror"]
  C --> D["Excitation laser beam"]
  D --> E["Sample"]
  E --> F["Objective 40X"]
  F --> G["Emission filter"]
  G --> H["Pupil"]
  H --> I["Tube lens"]
  I --> J["Camera"]
```
</details>

![](images/c87ed8adafad8cc6a9ef0750b11604e38d44088188f12dff78b3c4abed2d2f03.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["3D Chemical Imaging"] --> B["Mid-IR pump laser beam"]
  B --> C["Probe laser beam"]
  C --> D["Sample"]
  D --> E["stem switch"]
```
</details>

![](images/0bdb9a5589679ea74b8d88c751df3b8e07dd3fdf0ee8ea05612c9332cbe2c012.jpg)

<details>
<summary>text_image</summary>

Timing scheme
Mid-IR laser
ON
10kHz
OFF
Single probe laser
10kHz
Camera
Hot frame
100 Hz
Cold frame
</details>

Fig. 2 FBS-IDT instrumentation. FBS-IDT is based on a widefield transmission microscope consisting of a ×40 microscope objective, a tube lens, a CMOS camera, and add-on modalities that include a probe laser ring, a mid-IR pump laser, and an excitation laser. a 2D single-photon fluorescence intensity imaging mode. Under this mode, both the excitation filter and the emission filter are turned on. The 488 nm excitation laser beam is loosely focused on the sample using an off-axis parabolic mirror. b 3D chemical imaging mode. The oblique illumination of each probe beam matches the objective’s NA. The pump beam shares the same beam path with the 488-nm excitation laser beam. Under this mode, both pump and probe lasers are turned on and illuminating the sample while the excitation laser is switched off. c Time synchronization scheme for 3D chemical imaging. Both probe laser and mid-IR laser are running at 10 kHz with a pulse duration of \~1 µs. Each probe pulse is synchronized with a mid-IR laser pulse with a time delay of \~0.5 µs. An additional 50 Hz on/off duty-cycle modulation is imposed on the mid-IR laser to generate “Hot” and “Cold” frames on the camera. The camera is running with a frame rate of 100 Hz. Additional details on the timing scheme can be found in the Supplementary Information: Timing scheme

Here, the experimental group’s protein-based signal (Fig. 3b) is distributed throughout the cell, making it hard to locate the tau fibrils. Besides the protein map, the lipid map (Fig. 3c) of the experimental group demonstrates high concentrations of lipid compositions, which might correlate to the tau fibrils formation in the cell13,71. For the control group without tau fibrils, chemical images (Fig. 3i–l) are acquired under the same conditions as the cell in the experimental group. We can clearly observe the chemical-specific depth-resolved cellular structures based on the control group’s chemical imaging results. Compared to the experimental group, the significant difference is mainly manifested in the lipid map, where the control group has a low concentration of lipid contents. This stark difference in lipid concentrations between the control and 69–71 experimental groups matches previous observations , which might correlate to the tau fibrils formation. Besides the depth-resolved 2D demonstrations, we further perform 3D rendering of the chemical imaging results for the experimental group (Fig. 3e–h and Supplementary Movie 1) and the control group (Fig. 3m–p and Supplementary Movie 2). These 3D chemical images and movies clearly illustrate the volumetric distribution of the chemicalspecific cellular structures. The overlay 3D images simultaneously show the protein and lipid volumetric distribution, providing rich chemical and spatial correlation information. Although proteins with different secondary structure compositions are supposed to show varying MIP absorption, it is still difficult to directly extract this small variation. This gap can be filled when the 2D fluorescence guidance comes into play, as shown below.

![](images/3e8e2e9a1e94424d5c573fe00dad326a2aa66e20b7a793053f29b95256d27d29.jpg)

<details>
<summary>text_image</summary>

Cold IDT Protein: 1628 cm⁻¹ Lipid: 1745 cm⁻¹ 1900 cm⁻¹
-1.065 µm b c d
Experimental group 10 µm
0 µm
1.065 µm
Control group i j k l m n
0 µm
1.065 µm
Cold IDT Protein: 1628 cm⁻¹
Overlay Lipid: 1745 cm⁻¹
Cold IDT Protein: 1628 cm⁻¹
Overlay Lipid: 1745 cm⁻¹
1.31 1.40 0 2.2 ×10⁻³ 0 2.2 ×10⁻³
</details>

Fig. 3 FBS-IDT chemical imaging on human epithelial cells (Tau RD P301S FRET Biosensor cells). a–h 3D chemical imaging of the experimental group with fibrillar tau aggregates. i–p 3D chemical imaging of the control group without fibrillar tau aggregates. The fixed cells for both groups are immersed in $\mathsf { D } _ { 2 } \mathsf { O }$ PBS. The scale bar in (d) is applicable to (a–d) and (i–l). a, i Depth-resolved cold imaging results. b, j Protein imaging results with 1628 cm−1 mid-IR wavenumber. c, k Lipid imaging results with 1745 cm−1 mid-IR wavenumber. The wavenumber at 1745 cm−1 corresponds to the peak of the lipid ester $\mathsf { C } = \mathsf { O } ^ { 5 8 , 9 0 , 9 1 }$ 1. d, l Off-resonance imaging results with $1 9 0 0 { \mathsf { c m } } ^ { - 1 }$ mid-IR wavenumber. Most biochemical compounds have significantly weak or no absorptions at this cell-silent wavenumber. e, f, h 3D rendering of the cells in the experimental group shown in (a–c). g Overlay chemical imaging results of (f) and (h). m, n, p 3D rendering of the cells in the control group shown in (i–k). o Overlay chemical imaging results of (n) and (p). Extended data can be found in Fig. S1 in the Supplementary Information

## Depth-resolved mid-IR fingerprint spectra of tau fibrils

Amyloid protein aggregates exhibit highly heterogeneous chemical structures and morphologies5,7,76. The chemical and morphological variations show different levels of neurotoxicity and are associated with different stages of AD76–78. $\mathrm { A D } ^ { 7 6 - 7 8 }$ This heterogeneity is site-specific and sensitive to the cellular environment since the formation of the aggregate structure is subject to post-translational modifications and cofactors5,7 . The chemical, morphological and functional heterogeneity in AD is poorly understood, especially for the prefibrillar and early-stage aggregates. FBS-IDT enables 3D chemical imaging and 3D site-specific mid-IR spectra extraction for intracellular protein aggregates in the cellular fluid environment. Here, we demonstrate FBS-IDT’s capabilities of depth-resolved mid-IR fingerprint spectra extractions (Fig. 4).

We first performed single-photon 2D intensity fluorescence imaging on cells with/without tau fibrils (Fig. 4b, e). As expected, the experimental group shows strong GFPemission signals from labeled fibrillar tau aggregates, while no tau aggregates are observed in the control group. Fluorescence imaging results confirm the existence of tau fibrils in the experimental group and provide a guide star for extracting mid-IR spectra for tau fibrils. To extract depth-resolved mid-IR spectra, we first obtain hyperspectral 3D chemical images (4D data) of the cell samples for both experimental and control groups, covering the mid-IR fingerprint region. It is well known that the major absorption peak of the β-sheet structure is ${ \sim } 1 6 3 0 \mathrm { c m } ^ { - 1 }$ in the amide I band8,44. We thereby selected the areas of interest with high SNR for extracting mid-IR spectra from the tau fibrils using a protein map at 1628 cm−1 under fluorescence guidance (Fig. 4c). We further generated the depth-resolved mid-IR fingerprint spectra from the selected areas by averaging voxels within each axial plane. The depth-resolved mid-IR fingerprint spectra for tau fibrils are shown in Fig. 4g, i, k. As a comparison, we performed similar operations for the cell sample in the control group. The spectra plots for the control group are demonstrated in Fig. 4h, j, l. For both the experimental group and the control group spectra, the signature amide-I absorption peak (\~1650 cm−1 ) and two amide-II bands (\~1450 cm−1 and \~1550 cm−1 ) can be observed. Here, amide I vibration depends on the secondary structure of the polypeptide backbone and is hardly affected by the sidechain44. It is highly sensitive to secondary structure variations and is commonly applied to protein secondary structure analysis44. Therefore, we focus on the amide I band for analyzing the cell samples. As illustrated in Fig. 4g, i, k (see Fig. S2 in the Supplementary Information for more data), the amide I bands’ shapes significantly vary with the axial depths for the experimental group, which shows the heterogeneity of the tau fibrils. In contrast, the amide I bands of the control group in Fig. 4h, j, l (see Fig. S2 in the Supplementary Information for more data) demonstrate slight variations, consistent with the relatively uniform distribution of the diffusive protein.

## Protein secondary structure analysis and 3D visualization of β-sheet structure

Based on the depth-resolved mid-IR fingerprint spectra shown in Fig. 4, we further performed the protein secondary structure analysis for the experimental and the control groups. As shown in Fig. 5a (see Fig. S3 in the Supplementary Information for more data), we performed the Fourier self-deconvolution46,60 on amide-I band spectra to quantify the main protein secondary structure compositions, such as β sheet, α helix, and random coil (Methods). The protein secondary structure analysis of the experimental group confirms that the β sheet is the main secondary structure of the tau fibrils, which is consistent with previous observations by Cryo-EM before23,24. The variations of the experimental group’s secondary structure compositions further show the tau fibrils’ chemical structure heterogeneity. In comparison, the analyses of the control group that consists of diffusive proteins demonstrate much lower percentages of β sheet, indicating relatively homogeneous chemical structures. Overall, the depth-resolved mid-IR spectra and related protein secondary structure analyses validate the existence, the chemical compositions, and the heterogeneity of the intracellular tau fibrils, which are consistent with our fluorescence imaging and known facts.

To visualize 3D protein secondary structure, we further selected two 3D protein maps from the experimental group’s 4D hyperspectral data (Fig. 5b). We obtain the mid-IR spectral ratio map by dividing the 1628 cm−1 map by the 1644 cm−1 ma p59,66,67. After denoising processing, 3D visualization of β-sheet structure in tau fibrils was achieved (“Methods” section). 3D rendering of the β-sheet structure is shown in Fig. 5c and Supplementary Movie 3. We further demonstrate 2D cross-sections along different axial depth positions within the β-sheet 3D reconstruction in Fig. 5d–h. Although Cryo-EM enables high-resolution 3D characterization of tau aggregates, it is limited to purified protein extracted from cells with complicated sample preparations. Here, our FBS-IDT neither requires purified protein nor imposes any additional requirements on the protein aggregate sample preparations. It can directly perform 3D chemical non-invasive imaging of the intracellular protein aggregates and their secondary structure in the cell fluid with an optical approach. The validity of our protein secondary structure imaging approach relies on the extracted mid-IR spectra, the fidelity of which has been investigated and proven to be comparable to those obtained using the golden-standard Fourier-Transform Infrared (FTIR) Spectroscopy54,58.

## Discussion

Based on simple and cost-effective instrumentation, FBS-IDT enables chemical imaging on lipid droplets and protein, protein aggregates characterizations inside the cellular fluid, and 3D site-specific mid-IR spectroscopic analysis, which are not demonstrated by other state-of-the-art methods. Specifically, FBS-IDT realizes label-free hyperspectral 3D quantitative chemical imaging of intracellular tau fibrils and lipid droplets in the cellular fluid with a high speed and a high resolution. Based on the hyperspectral imaging capabilities, FBS-IDT further achieves 3D sitespecific mid-IR spectroscopy analysis on the tau fibrils and fluorescence-guided 3D visualization of this aggregate’s protein secondary structure for the first time.

![](images/33b686658761e433e333b5e95e89535b28cbb1147d3951885348b9d49403dc69.jpg)  
Fig. 4 Fluorescence-guided depth-resolved mid-IR fingerprint spectra of tau fibrils. a Cold IDT image at −1.065 µm depth for the cell with tau fibrils. b 2D single-photon fluorescence intensity image of the cell shown in (a). c Select areas within the tau fibrils from the 3D chemical protein map at 1628 cm−1 . The selection is guided by the 2D image in (b) and highlighted in red. d Cold IDT image at −1.065 µm depth for the cell without tau fibrils. e 2D single-photon fluorescence intensity image of the cell shown in (d). f Select areas that show protein signals from the 3D chemical protein map at 1628 cm−1 . The selection is highlighted in red. g–k Depth-resolved mid-IR spectra extracted from the areas shown in (c). h–l Depth-resolved mid-IR spectra extracted from the areas shown in (f). The axial depth value of each spectrum is shown in the top left of each plot for (g) to (l). Extended data can be found in Fig. S2 in the Supplementary Information

![](images/2544143470c9a05cc02602f015d24c9d9c9771989d00bfbed3e0e946a67a1a13.jpg)  
Fig. 5 Protein secondary structure analysis and 3D visualization of β-sheet structure. a Protein secondary structure analysis based on amide I bands for cells in the experimental and the control groups. The amide I band spectra are extracted from the mid-IR fingerprint spectra shown in Fig. 4. Three main protein secondary structures, the α helix, β sheet, and random coil, are quantified using the deconvolution method. The percentage and the peak positions for each secondary structure are indicated in each plot. b 3D protein maps of the cell with tau fibrils in the amide I band. These two images are selected according to the spectral positions of the β sheet and random coil. c 3D visualization of β sheet structure based on mid-IR spectral ratio map of two 3D images in (b). d–h Depth-resolved demonstration of the 3D rendering image in (c). The axial depth value is indicated in each image. The scale bar in (h) is applicable from (d) to (h). Extended data can be found in Fig. S3 in the Supplementary Information

FBS-IDT’s superior performance is rooted in the innovative instrumentation design by integrating fluorescence and MIP imaging into the computational imaging framework. First, FBS-IDT’s pump-probe pulsed IDT imaging design can directly correlate each voxel in the 3D object to its unique mid-IR spectra with a high resolution.

With this design, FBS-IDT efficiently recovers the 3D RI information from the intensity images and generates a stack of 3D chemical images using biological objects’ RI variations. Since each 3D image correlates with the unique MIP effect under a particular mid-IR wavenumber, extracting the voxel’s value from the same spatial position of all the 3D images can recover a site-specific mid-IR fingerprint spectrum. Unlike FBS-IDT, most conventional spectroscopy approaches, such as Raman spectroscopy, CD spectroscopy, and FTIR spectroscopy, merely provide spectra averaged over the sample volumes without 3D spectroscopic analysis capabilities. Recently emerging AFM-IR spectroscopy can extract IR spectra from specific sites but is limited to 2D plane47,48. In addition to the above advantages, FBS-IDT can convert the 3D site-specific mid-IR spectra into high-resolution images, circumventing the low-resolution restrictions of conventional IR-based spectroscopic imaging methods, such as FTIR micro-spectroscopy79. This is achieved by separating the detection process from the IR absorption process. The 450 nm short wavelength detection guarantees high spatial resolution. Meanwhile, the oblique illu mination further enhances the resolution up to the incoherent resolution limit. Second, FBS-IDT applies a tunable, broadband QCL laser for mid-IR fingerprint spectroscopic imaging, laying the foundation for highsensitivity bond-selective imaging and protein secondary structure analysis for amyloid protein aggregates. As is sensitive to a small fraction (\~0.02%) of chemical bond strength change and can reach spectroscopy resolution up to \~0.2 Angstrom, which guarantees FBS-IDT’s chemical sensitivity. Furthermore, due to its reliable quantification capability, the mid-IR amide I band has been commonly applied to perform protein secondary structure analy secondary structure in amyloid protein aggregates and can efficiently track protein aggregation kinetics9,44. Compared with mid-IR-based FBS-IDT, Raman spectroscopy requires a much higher concentration of analytes to obtain reasonable SNR, making it not commonly applied in protein secondary structure analysis9 . Another important spectroscopy method, CD spectroscopy, is less accurate in analyzing β-sheet structure than other secondary structures29, limiting its applications in amyloid protein. Besides the advantages of imaging and analyzing amyloid protein aggregates, FBS-IDT’s mid-IR fingerprint spectroscopic imaging significantly simplifies the requirements for fluorescence tag. Unlike fluorescenceonly imaging methods, FBS-IDT merely needs a single fluorescent tag for a certain type of protein since FBS-IDT can easily distinguish different biomolecules, such as lipids, DNA, and RNA, from proteins relying on label-free MIP effects. This can avoid spectral overlap issues from multiplexed fluorescence tags. Third, different from electron microscopy, FBS-IDT works in the visible and IR optical bands with a widefield configuration, compatible with fixed/living biological objects in the native cellular fluids and free from protein purification requirements. Here, both visible and mid-IR illuminations are non-toxic and harmless to most living biological entities. Also, the widefield illumination beams are either fast-diverging or loosely focused, resulting in low light intensity on the sample. Hence, the FBS-IDT’s optical imaging scheme guarantees non-invasive, safe, and low photodamage biological imaging in objects’ native states. Compared to FBS-IDT, Cryo-EM mainly applies to purified protein samples23,24 with complicated sample preparations27, hindering the investigations of the intracellular amyloid protein aggregates. Another emerging technique, AFM-IR spectroscopy imaging, does not require a purified protein sample but is limited to dry samples47,48. The dehydration process can alter the pathological protein aggregate since they are sensitive to the environment5 . Fourth, the FBS-IDT is a universal and scalable imaging platform with an affordable cost and negligible daily operational expenses. FBS-IDT does not require specialized optics and can be realized by adding CW diode lasers and a mid-IR laser to a standard brightfield microscope. The cost of FBS-IDT is affordable to most laboratories compared to Cryo-EM machine’s several million dollars cost and \~10 k dollars daily operational fee28

FBS-IDT’s system performance still has room for improvement. First, the fluorescence tag inevitably perturbs cellular functions and tends to bring in photobleaching issues in the current design. To realize fully label-free imaging, a deep neural network could be trained to extract the weak contrast of the target protein aggregates from the background protein signal and effectively denoise the extracted image. Second, the linear IDT reconstruction method degrades with high NA and strong scattering biological samples. The recently developed non-paraxial multiple-scattering model80 can be deployed within the FBS-IDT framework to significantly improve FBS-IDT’s resolution and high-fidelity imaging capabilities on strong scattering biological samples. Third, deep learning could be integrated with the FBS-IDT method to alleviate the reconstruction artifacts81,82. Fourth, the high-energy nanosecond mid-IR optical parametric oscillator could replace the current low-energy QCL laser, improving the SNR and expanding the FOV.

FBS-IDT’s application potential can be further explored to support tauopathy research by performing systematic imaging investigations in the future. There are many fundamental questions to be answered in tauopathy, such as the mechanism of tau aggregate generation/propagation and the role of tau oligomers in neuron toxicity2 . Additional questions include how FBS-IDT signals differ depending on the type of amyloid (e.g., tau vs. β-amyloid) or even the type of tau conformer83 To answer these questions, tau aggregation must be investigated at both single-cell and tissue levels to elucidate how tau aggregates vary in spatial distribution, chemical/morphological heterogeneity, conformation, relationship with environments, and interaction with organelles. Related biological samples can be from cultured cells/tissues or model animals. Future studies will need to focus on in vivo imaging to monitor the dynamics of tau and its aggregation. FBS-IDT is particularly suitable for the aforementioned application scenarios. It enables high volumetric imaging speed, non-invasive 3D spectroscopic imaging and analytic capabilities, and compatibility with biological analytes in cellular fluids. FBS-IDT will enable the comprehensive characterization of tau aggregates under numerous conditions.

In summary, using a cost-effective optical imaging system, FBS-IDT realizes 3D chemical imaging and spectroscopic analysis of intracellular lipid droplets, tau aggregate, and the secondary structure of tau aggregates in the cellular fluid. FBS-IDT enables 3D spatiallyresolved mid-IR fingerprint spectra extraction and quantitative chemical imaging with sub-micrometer spatial resolution and Hz-level speed. The above spectroscopic chemical imaging does not impose additional restrictions on the biological samples, opening a new avenue for in vivo imaging of intracellular protein aggregates. Notably, FBS-IDT is based on a modular design developed from low-cost standard optics components, which can be easily adapted to meet different imaging needs. We envision that the FBS-IDT can significantly contribute to neurodegeneration research and a broad range of biomedical applications.

## Materials and methods

## Instrumentation

The transmission brightfield microscope for FBS-IDT is a simple 4f imaging system built using the Thorlabs offthe-shelf components, including a microscope objective (RMS40x, 0.65 NA, 40x magnification), a tube lens (TTL180A, f = 180 mm), a silver plane mirror, and standard 60 mm cage assembling system. The camera is an Andor CMOS camera (ZYLA-5.5-USB3-S). The 488 nm excitation laser beam for the 2D single-photon intensity fluorescence imaging is generated from a tunable femtosecond laser (Coherent, Chameleon Ultra) by frequency doubling its 976 nm wavelength. The excitation laser beam power is \~30 mW. The fluorescence imaging in FBS-IDT can also use the 488 nm beam from a regular CW diode laser. We installed switchable excitation filters (ET485/20 from Chroma) and emission filters (FF01-525/ 45 from Semrock and FELH0500 from Thorlabs) in the FBS-IDT beamline to switch between the fluorescence imaging mode and the chemical imaging mode. For the label-free chemical imaging, we added a ring-shaped probe laser system and a mid-IR laser to the brightfield microscope. The probe laser beam is from a customized ring laser illumination system that consists of 16 individual fiber-coupled (multimode optical fiber: 0.22 NA and 105 µm core diameter) diode lasers (wavelength: \~450 nm, average power under CW mode: \~3 W, repetition rate: up to 10 kHz, pulse duration: \~0.6 µs to \~10 µs). Under pulsed mode, the probe laser output power is \~30 mW based on a \~ 0.01 duty cycle. Each probe beam’s illumination angle is adjusted to match the microscope objective’s NA. Two operation modes of the ring laser illumination system are available: 8 probe lasers and 16 probe lasers (Supplementary Information: Timing scheme). The pump laser beam is from a tunable mid-IR QCL laser (Daylight solution MIRcat-2400). A gold parabolic mirror (Thorlabs, MPD01M9-M03) redirects the excitation laser beam or the mid-IR pump beam into the sample. For pump-probe chemical imaging, the pulse duration and the repetition rate are set to \~1 µs and 10 kHz for both probe and pump beam, while the Andor camera runs at a 100 Hz frame rate. The energy fluence of the probe beam on the sample area is \~0.2 pJ/µm2 . The mid-IR energy fluence on the sample is \~50 pJ/µm2 , depending on the wavenumber. Additional duty cycle control is applied to the mid-IR pump laser so that the 10 kHz pulse train is turned on and off at 50 Hz. During data acquisition, the probe laser, the pump laser, and the camera are synchronized using a pulse generator (Quantum Composers 9214). The FBS-IDT system control and data acquisitions are based on customized MATLAB codes. The spatial resolution of FBS-IDT is diffractionlimited and is mainly determined by the coherent properties of the light source, the wavelength, and the NA of the microscope objective. The FOV of FBS-IDT can safely cover a 3D volume of \~100 µm × 100 µm × 50 µm (width × length × depth). For larger thin samples, the lateral FOV can be extended further using a scanning and stitching method58.

## Imaging method

For 2D single-photon intensity fluorescence imaging, FBS-IDT acquires the intensity image using the CMOS camera. For the area of interest smaller than the excitation beam size, the intensity image can be directly used as the guide star. For areas larger than the excitation beam size, FBS-IDT can scan the excitation beam to extend its FOV. The scanned images are stitched using the standard deviation projection (Fiji ImageJ, Version:1.53 c).

For label-free chemical imaging, FBS-IDT is using a similar approach developed by Zhao and Matlock et al. 58 The 3D RI map reconstruction follows the conventional IDT model published by Ling et al. 64 and the annular IDT work by Li and Matlock et al. $^ { 6 3 } .$ For FBS-IDT, the biological object is modeled as a 3D scattering potential within a given volume Ω as $V ( \mathbf { r } , z ) = k ^ { 2 } ( 4 \pi ) ^ { - 1 } \Delta \epsilon ( \mathbf { r } ) ,$ , where r denotes the spatial coordinates $\langle x , y , z \rangle _ { \mathrm { { \rangle } } }$ , k is the probe beam’s wavenumber, and $\Delta \epsilon ( \mathbf { r } )$ is the permittivity contrast between the biological object and its immersion medium. Each oblique probe beam is treated as a plane wave $u _ { i } ( \boldsymbol { r } | \nu _ { i } )$ incident on the sample with a illumination angle defined by the lateral spatial frequency vector $\nu _ { i } .$ Based on the first-Born approximation, the total scattering field from the biological object generated by the probe beam can be evaluated as a summation

$$
u _ {t o t} (\mathbf {r} | \boldsymbol {v} _ {\mathbf {i}}) = u _ {i} (\mathbf {r} | \boldsymbol {v} _ {\mathbf {i}}) + \iiint_ {\Omega} u _ {i} (\mathbf {r} ^ {\prime} | \boldsymbol {v} _ {\mathbf {i}}) V (\mathbf {r} ^ {\prime}) G (\mathbf {r} - \mathbf {r} ^ {\prime}) d ^ {3} \mathbf {r} ^ {\prime} \tag {1}
$$

of the incident and first-order scattered field defined by a 3D convolution with the Green’s function $G ( \pmb { r } )$ . Our model assumes that the total scattered field results from a stacked set of 2D slices through the object since the scattering events from each point in the object are mutually independent. This assumption implies that the 3D RI map can be recovered from a single 2D plane if the additional propagation is included in the inverse model for recovering each axial slice. FBS-IDT relates the object’s 3D scattering potential with the measured intensity images using the cross interference between the incident and the scattered field from the probe laser. The cross interference linearly encodes the scattering potential into intensity. Based on oblique probe beam illumination, the cross-interference term and its conjugate are spatially separated in the Fourier plane allowing for linear inverse scattering models under the first-Born approximation. With this separation and the complex permittivity contrast assumption $( \Delta \epsilon ( \mathbf { r } , z ) = \Delta \epsilon _ { r e } ( \mathbf { r } , z ) +$ $j \Delta \epsilon _ { i m } ( \mathbf { r } , z ) )$ , a forward model can be developed

$$
\begin{array}{l} \hat {I} (x, y \mid \boldsymbol {v} _ {\mathbf {i}}) = \sum_ {m} H _ {r e} (\boldsymbol {v}, m \mid \boldsymbol {v} _ {\mathbf {i}}) \Delta \hat {\epsilon} _ {r e} (\boldsymbol {v}, m) \tag {2} \\ + H _ {i m} (\pmb {\nu}, m | \pmb {\nu_ {i}}) \Delta \hat {\epsilon} _ {i m} (\pmb {\nu}, m) \\ \end{array}
$$

where ^ denotes the Fourier transform of a variable, m denotes the axial slice index, and $H _ { r e }$ and $H _ { i m }$ are the transfer functions (TFs) containing the physical model. These transfer functions have the form

$$
H _ {r e} (\boldsymbol {\nu}, m \mid \boldsymbol {\nu} _ {\mathrm{i}}) = \frac {j k ^ {2} \Delta z}{2} A (\boldsymbol {\nu} _ {\mathrm{i}}) P (\boldsymbol {\nu} _ {\mathrm{i}}) [ \quad - j [ n (\boldsymbol {\nu} - \boldsymbol {\nu} _ {\mathrm{i}}) - n (\boldsymbol {\nu} _ {\mathrm{i}}) ] m \Delta z \tag {3a}
$$

$$
\left[ P (\pmb {\nu} - \pmb {\nu_ {i}}) \frac {e ^ {- j [ \eta (\pmb {\nu} - \pmb {\nu_ {i}}) - \eta (\pmb {\nu_ {i}}) ] m \Delta z}}{\eta (\pmb {\nu} - \pmb {\nu_ {i}})} - P (\pmb {\nu} + \pmb {\nu_ {i}}) \frac {e ^ {j [ \eta (\pmb {\nu} + \pmb {\nu_ {i}}) - \eta (\pmb {\nu_ {i}}) ] m \Delta z}}{\eta (\pmb {\nu} + \pmb {\nu_ {i}})} \right]
$$

$$
\begin{array}{l} H _ {i m} (\boldsymbol {\nu}, m | \boldsymbol {\nu_ {i}}) = - \frac {k ^ {2} \Delta z}{2} A (\boldsymbol {\nu_ {i}}) \\ P \left(\boldsymbol {v} _ {\mathbf {i}}\right) \left[ P \left(\boldsymbol {v} - \boldsymbol {v} _ {\mathbf {i}}\right) \frac {e ^ {- j \left[ \eta \left(\boldsymbol {v} - \boldsymbol {v} _ {\mathbf {i}}\right) - \eta \left(\boldsymbol {v} _ {\mathbf {i}}\right) \right] m \Delta z}}{\eta \left(\boldsymbol {v} - \boldsymbol {v} _ {\mathbf {i}}\right)} + P \left(\boldsymbol {v} + \boldsymbol {v} _ {\mathbf {i}}\right) \frac {e ^ {j \left[ \eta \left(\boldsymbol {v} + \boldsymbol {v} _ {\mathbf {i}}\right) - \eta \left(\boldsymbol {v} _ {\mathbf {i}}\right) \right] m \Delta z}}{\eta \left(\boldsymbol {v} + \boldsymbol {v} _ {\mathbf {i}}\right)} \right] \tag {3b} \\ \end{array}
$$

where $A ( \nu _ { \mathrm { i } } )$ is an illumination light amplitude, $P ( \nu )$ is the pupil function, Δz is the discretized slice thickness based on the microscope’s depth of field, $\eta ( \pmb { \nu } ) = \sqrt { \lambda ^ { - 2 } - | \pmb { \nu } | ^ { 2 } }$ is the axial spatial frequency, and λ is the imaging wavelength. Given this linear forward model, the model inversion can be performed by slice-wise deconvolution with Tikhonov regularization. The image reconstruction is based on customized MATLAB codes.

Based on the above method, FBS-IDT can reconstruct the 3D RI maps for the object under “Cold” and $\mathrm { \Delta } ^ { \omega } \mathrm { H o t } ^ { \dprime }$ states. The 3D chemical image is obtained by subtraction between the $\mathrm { \Delta } ^ { \omega } \mathrm { H o t } ^ { \dprime }$ from the “Cold”. For 3D visualization of the protein secondary structure, two 3D chemical images of interest are selected and normalized by their corresponding mid-IR laser power. Then, the division between the two 3D chemical images is performed to generate a 3D ratio map that shows the 3D contrast of the secondary structure. Then, the 3D ratio map is further denoised using thresholding and median filtering (MATLAB function: medfilt2). The 2D fluorescence image can also delineate the boundary of tau fibrils to help reduce extra noise.

## FBS-IDT mid-IR spectroscopy

We first perform hyperspectral imaging over the mid-IR fingerprint region, generating a stack of 3D chemical images for each mid-IR wavenumber. Extracting the value of a certain voxel in the 3D object from all the 3D chemical images in the mid-IR fingerprint region and repeating this procedure over all voxels can generate the raw 3D site-specific mid-IR spectrum. Then, the raw spectrum is normalized by the measured mid-IR laser intensity spectrum and further denoised using a Savitzky-Golay $\dot { \mathrm { G l t e r } } ^ { 8 4 }$ . We repeat the above procedures for the voxels of interest selected per depth. To increase the SNR, we average the obtained spectra within the same depth to generate the depth-resolved mid-IR spectra. We further performed baseline correction processing on the mid-IR spectra60 For protein secondary structure analysis, we selected the amide I band region $( 1 6 0 0 { - } 1 7 0 0 \mathrm { c m } ^ { - 1 } )$ to perform the deconvolution on the spectra assuming Lorentzian lineshap e46,60. The abovementioned baseline correction processing and deconvolution-based secondary structure analysis were all performed by a peak analysis application module (Peak Deconvolution, Version 1.90) embedded in the commercial software OriginPro 2021(Version 9.8.0.200).

## Biological samples

Tau RD P301S FRET Biosensor (TRPFB) cells were used for the designated experiment to examine the seeding activity of fibril fractions extracted from aged (9 month) PS19 P301S mouse brain. The TRPFB cells (CAT#CRL-3275) were obtained from the American Type Culture Collection (ATCC). This cell line has been engineered to report tau seeding activity. Tau seeds introduced into the culture media (CRL-3275) can nucleate the aggregation of the endogenous tau reporter proteins85. The TRPFB cells were derived by transducing HEK293T cells with two separate lentivirus constructs encoding tau RD P301S-CFP and tau RD P301S-YFP. Dual-positive cells were identified by fluorescence-activated cell sorting and were cloned and isolated using cloning cylinders85

The tau fibril fraction extraction is described as follows. We followed similar protocols in the works by Jiang et al. 35,86 The frozen hippocampus and cortex tissues were weighed (100 mg - 250 mg) and put in a thick-wall polycarbonate tube (Beckman Coulter Life Sciences, cat # 362305). Then it was homogenized with TBS buffer (50 mM Tris, pH 8.0, 274 mM NaCl, 5 mM KCl) supplemented with protease and phosphatase inhibitor cocktails (Roche, cat#05892791001 and cat#04906837001)34. The homogenate was first centrifuged for 20 minutes (28k rpm, 4 °C). Then the pellet was homogenized with buffer B (10 mM Tris, pH 7.4, 800 mM NaCl, 10% sucrose, 1 mM EGTA, 1 mM PMSF). The homogenate was centrifuged again for 20 minutes (22k rpm, 4 °C). Then, the supernatant was aliquot to a new thick-wall polycarbonate tube and incubated with 1% Sarkosyl, rotating in a thermomixer at 37 °C for 1 hour. After the incubation, the fraction was further mixed by the ultracentrifuge for 1 h (55,000 rpm, 4 °C). Then the sarkosyl-insoluble pellet was resuspended with 50 µl TE buffer (10 mM Tris, 1 mM EDTA, pH 8.0), which is the final tau fibril fraction used for the experiment.

After the tau fibril fraction extraction, the seeding process is described as follows. The TRPFB cells were used to detect tau aggregates capable of propagating patholog y85,87,88. Fractions from 9 month PS19 P301S tau mouse brain (tau fibril fraction, containing 100 ng of tau fibrils) were used as the seeds to induce tau aggregation. The vehicle control was applied with the corresponding TE buffer. The cells are fixed after 24 h. After fixation, the cells were washed five times with D O-based PBS. Finally, the fixed cells were immersed in D O PBS solutions and sandwiched by two Raman-grade 0.2-mm-thick CaF2 glass pieces.

## Software

Data were acquired by customized MATLAB code. Data were processed by customized MATLAB code, OriginPro 2021 (Version 9.8.0.200), and Fiji ImageJ (Version:1.53 c).

## Acknowledgements

This work is supported by the National Institute of General Medical Sciences (R35GM136223), a grant from Daylight Solutions, and a grant (2023-321163) from the Chan Zuckerberg Initiative Donor-Advised Fund at the Silicon Valley Community Foundation. The authors thank Dr. Hongjian He for helpfu discussions in protein secondary structure analysis.

## Author details

1 Department of Electrical and Computer Engineering, Boston University, Boston, MA 02215, USA. 2 The Picower Institute for Learning and Memory, Massachusetts Institute of Technology, Cambridge, MA 02142, USA. 3 Department of Pharmacology and Experimental Therapeutics, Boston University School of Medicine, Boston, MA 02118, USA. 4 Department of Physics, Boston University, Boston, MA 02215, USA. 5 State Key Laboratory of Luminescence and Applications, Changchun Institute of Optics, Fine Mechanics and Physics, Chinese Academy of Sciences, 130033 Changchun, China. 6 Department of Biomedical Engineering, Boston University, Boston, MA 02215, USA. 7 Photonics Center, Boston University, Boston, MA 02215, USA. 8 Present address: Department of Mechanical Engineering, Massachusetts Institute of Technology, Cambridge, MA 02142, USA

## Author contributions

J.Z. and J.X.C. proposed FBS-IDT. J.Z. developed the FBS-IDT system, performed the experiments, processed the data, and wrote the draft. L.J. and B.W. prepared the biological samples and supported the experiments. A.M. developed the IDT-based reconstruction method and assisted with data processing. Y.H.X. assisted with system development, data acquisition, and data processing. J.B.Z. assisted with data processing. H.B.Z. assisted with the manufacture of the probe-laser array system. L.T. supported the IDT-based imaging reconstruction and data processing. J.X.C., B.W., and L.T. supervised the research and revised the manuscript. All authors contributed to the fina creation of the manuscript.

## Data availability

All the data are available upon reasonable request to the corresponding authors (jxcheng@bu.edu (J.X.C.) and jianzhao@knights.ucf.edu (J.Z.)).

## Code availability

The image reconstruction codes are available upon reasonable request to the corresponding authors (jxcheng@bu.edu (J.X.C.) and jianzhao@knights.ucf.edu (J.Z.)).

## Conflict of interest

The authors declare no competing interests.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41377-023-01191-6.

Received: 22 February 2023 Revised: 18 May 2023 Accepted: 21 May 2023 Published online: 15 June 2023

## References

1. GBD 2016 Dementia Collaborators. Global, regional, and national burden of Alzheimer’s disease and other dementias, 1990-2016: a systematic analysis for the global burden of disease study 2016. Lancet Neurol. 18, 88–106, https:// doi.org/10.1016/S1474-4422(18)30403-4 (2019).  
2. Wang, Y. P. & Mandelkow, E. Tau in physiology and pathology. Nat. Rev. Neurosci. 17, 22–35, https://doi.org/10.1038/nrn.2015.1 (2016).  
3. Giovannini, J. et al. Tau protein aggregation: key features to improve drug discovery screening. Drug Discovery Today 27, 1284–1297, https://doi.org 10.1016/j.drudis.2022.01.009 (2022).  
4. Lu, M., Kaminski, C. F. & Schierle, G. S. K. Advanced fluorescence imaging of in situ protein aggregation. Phys. Biol. 17, 021001, https://doi.org/10.1088/ 1478-3975/ab694e (2020).  
5. Li, D. & Liu, C. Hierarchical chemical determination of amyloid polymorphs in neurodegenerative disease. Nat. Chem. Biol. 17, 237–245, https://doi.org/ 10.1038/s41589-020-00708-z (2021).  
6 Buée. I et al. Tau protein isoforms, phosphorylation and, role, in neurode. generative disorders. Brain Res. Rev. 33, 95–130, https://doi.org/10.1016/s0165- 0173(00)00019-9 (2000)  
7. Chung, D. E. C. et al. Cellular and pathological heterogeneity of primary tauopathies. Mol. Neurodegener. 16, 57, https://doi.org/10.1186/s13024-021- 00476-x (2021).  
8. Ruysschaert, J. M. & Raussens, V. ATR-FTIR analysis of amyloid proteins. in Peptide Self-Assembly: Methods and Protocols (eds Nilsson, B. L. & Doran, T. M.) p. 69–81 (Springer, 2018).  
9. Martial, B., Lefèvre, T. & Auger, M. Understanding amyloid fibril formation using protein fragments: structural investigations via vibrational spectroscopy and solid-state NMR. Biophys. Rev. 10, 1133–1149, https://doi.org/10.1007/s12551- 018-0427-2 (2018).  
10. Farmer, B. C. et al. Lipid droplets in neurodegenerative disorders. Front. Neurosci. 14, 742, https://doi.org/10.3389/fnins.2020.00742 (2020).  
11. Girard, V. et al. Abnormal accumulation of lipid droplets in neurons induces the conversion of alpha-synuclein to proteolytic resistant forms in a Drosophila model of Parkinson’s disease. PLoS Genet. 17, e1009921, https://doi.org 10.1371/journal.pgen.1009921 (2021).  
12. Xu, Y. et al. Autophagy deficiency modulates microglial lipid homeostasis and aggravates tau pathology and spreading. Proc. Natl Acad. Sci. USA 118, e2023418118, https://doi.org/10.1073/pnas.2023418118 (2021).  
13. van der Kant, R. et al. Cholesterol metabolism is a druggable axis that independently regulates tau and amyloid-β in iPSC-derived Alzheimer’s disease neurons. Cell Stem Cell 24, 363–375.e9, https://doi.org/10.1016/ j.stem.2018.12.013 (2019).  
14. Pathuri, P. et al. Cancer Drug Design and Discovery. 2nd edn (ed Neidle, S.) p. 121–141 (Elsevier, 2014).  
15. Fernandez-Leiro, R. & Scheres, S. H. W. Unravelling biological macromolecules with cryo-electron microscopy. Nature 537, 339–346, https://doi.org/10.1038/ nature19948 (2016).  
16. Sunde, M. et al. Common core structure of amyloid fibrils by synchrotron X-ray diffraction. J. Mol. Biol. 273, 729–739, https://doi.org/10.1006/jmbi.1997.1348 (1997).  
17. Ortore, M. G. et al. Time-resolved small-angle X-ray scattering study of the early stage of amyloid formation of an apomyoglobin mutant. Phys. Rev. E 84, 061904, https://doi.org/10.1103/PhysRevE.84.061904 (2011).  
18. Tycko, R. Solid-state NMR studies of amyloid fibril structure. Annu. Rev. Phys. Chem. 62, 279–299, https://doi.org/10.1146/annurev-physchem-032210- 103539 (2011).  
19. Stroud, J. C. et al. Toxic fibrillar oligomers of amyloid-β have cross-β structure. Proc. Natl Acad. Sci. USA 109, 7717–7722, https://doi.org/10.1073/ pnas.1203193109 (2012).  
20. Hong, D. P., Fink, A. L. & Uversky, V. N. Structural characteristics of α-synuclein oligomers stabilized by the flavonoid baicalein. J. Mol. Biol. 383, 214–223, https://doi.org/10.1016/j.jmb.2008.08.039 (2008).  
21. Mylonas, E. et al. Domain conformation of tau protein studied by solution small-angle X-ray scattering. Biochemistry 47, 10345–10353, https://doi.org/ 10.1021/bi800900d (2008).  
22. Mukrasch, M. D. et al. Structural polymorphism of 441-residue tau at single residue resolution. PLoS Biol. 7, e1000034, https://doi.org/10.1371/ journal.pbio.1000034 (2009).  
23. Fitzpatrick, A. W. P. et al. Cryo-EM structures of tau filaments from Alzheimer’s disease. Nature 547, 185–190, https://doi.org/10.1038/nature23002 (2017).  
24. Scheres, S. H. W. et al. Cryo-EM structures of tau filaments. Curr. Opin. Struct. Biol. 64, 17–25, https://doi.org/10.1016/j.sbi.2020.05.011 (2020).  
25. Acton, T. B. et al. Preparation of protein samples for NMR structure, function, and small-molecule screening studies. Methods Enzymol. 493, 21–60, https:// doi.org/10.1016/b978-0-12-381274-2.00002-9 (2011).  
26. Grishaev, A. Sample preparation, data collection, and preliminary data analysis in biomolecular solution X-ray scattering. Curr. Protoc. Protein Sci. 70, 17.14.1- 17.14.18, https://doi.org/10.1002/0471140864.ps1714s70 (2012).  
27. Passmore, L. A. & Russo, C. J. Specimen preparation for high-resolution cryo-EM. Methods Enzymol. 579, 51–86, https://doi.org/10.1016/bs.mie.2016.04.011 (2016).  
28. Hand, E. Cheap shots. Science 367, 354–358, https://doi.org/10.1126 science.367.6476.354 (2020).  
29. Pelton, J. T. & McLean, L. R. Spectroscopic methods for analysis of protein secondary structure. Anal. Biochem. 277, 167–176, https://doi.org/10.1006/ abio.1999.4320 (2000).  
0 Whitmore I. & Wallace. B. A. Protein secondary structure analyses from circular dichroism spectroscopy: methods and reference databases. Biopolymers 89, 392–400, https://doi.org/10.1002/bip.20853 (2008).  
31. Craig, S. L. & Edward, J. H. Calculation of positron range and its effect on the fundamental limit of positron emission tomography system spatial resolution. Phys. Med. Biol. 44, 781–799, https://doi.org/10.1088/0031-9155/44/3/019 (1999).  
32. Klunk, W. E. et al. Imaging brain amyloid in Alzheimer’s disease with pittsburgh compound-B. Ann. Neurol. 55, 306–319, https://doi.org/10.1002/ana.20009 (2004).  
33. Hansson, O. Biomarkers for neurodegenerative diseases. Nat. Med. 27, 954–963, https://doi.org/10.1038/s41591-021-01382-x (2021).  
34. Apicco, D. J. et al. Reducing the RNA binding protein TIA1 protects against tau-mediated neurodegeneration in vivo. Nat. Neurosci. 21, 72–80, https:// doi.org/10.1038/s41593-017-0022-z (2018).  
35. Jiang, L. L. et al. Tau oligomers and fibrils exhibit differential patterns of seeding and association with RNA binding proteins. Front. Neurol. 11, 579434, https://doi.org/10.3389/fneur.2020.579434 (2020).  
36. Kurouski, D., Van Duyne, R. P. & Lednev, I. K. Exploring the structure and formation mechanism of amyloid fibrils by Raman spectroscopy: a review. Analyst 140, 4967–4980, https://doi.org/10.1039/c5an00342c (2015).  
37. Devitt, G. et al. Raman spectroscopy: an emerging tool in neurodegenerative disease research and diagnosis. ACS Chem. Neurosci. 9, 404–420, https:// doi.org/10.1021/acschemneuro.7b00413 (2018).  
38. Ji, M. et al. Label-free imaging of amyloid plaques in Alzheimer’s disease with stimulated Raman scattering microscopy. Sci. Adv. 4, eaat7715, https://doi.org 10.1126/sciadv.aat7715 (2018).  
39. Miao, K. & Wei, L. Live-cell imaging and quantification of PolyQ aggregates by stimulated Raman scattering of selective deuterium labeling. ACS Cent. Sci. 6, 478–486, https://doi.org/10.1021/acscentsci.9b01196 (2020).  
40. Ettema, L. et al. Label-free Raman and fluorescence imaging of amyloid plaques in human Alzheimer’s disease brain tissue reveal carotenoid accumulations. J. Opt. 24, 054005, https://doi.org/10.1088/2040-8986 ac5b51 (2022).  
41. Talaga, D. et al. Total internal reflection tip-enhanced Raman spectroscopy of tau fibrils. J. Phys. Chem. B 126, 5024–5032, https://doi.org/10.1021/ acs.jpcb.2c02786 (2022).  
42. Fu, Y. et al. Characterization of photodamage in coherent anti-Stokes Raman scattering microscopy. Opt. Express 14, 3942–3951, https://doi.org/10.1364/ OE.14.003942 (2006).  
43. Shi, L. X. et al. Mid-infrared metabolic imaging with vibrational probes Nat. Methods 17, 844–851, https://doi.org/10.1038/s41592-020-0883-z (2020).  
44. Barth, A. & Zscherp, C. What vibrations tell about proteins. Quart. Rev. Biophys 35, 369–430, https://doi.org/10.1017/S0033583502003815 (2002).  
45. Miyazawa, T. & Blout, E. R. The infrared spectra of polypeptides in various conformations: amide I and II bands1 . J. Am. Chem. Soc. 83, 712–719, https:// doi.org/10.1021/ja01464a042 (1961).  
46. Yang, H. Y. et al. Obtaining information about protein secondary structures in aqueous solution using Fourier transform IR spectroscopy. Nat. Protoc. 10, 382–396, https://doi.org/10.1038/nprot.2015.024 (2015).  
47. Zhou, L. & Kurouski, D. Structural characterization of individual α-synuclein oligomers formed at different stages of protein aggregation by atomic force microscopy-infrared spectroscopy. Anal. Chem. 92, 6806–6810, https://doi.org 10.1021/acs.analchem.0c00593 (2020).  
48. Banerjee, S. & Ghosh, A. Structurally distinct polymorphs of tau aggregates revealed by nanoscale infrared spectroscopy. J. Phys. Chem. Lett. 12, 11035–11041, https://doi.org/10.1021/acs.jpclett.1c02660 (2021).  
49. Bai, Y. R., Yin, J. Z. & Cheng, J. X. Bond-selective imaging by optically sensing the mid-infrared photothermal effect. Sci. Adv. 7, eabg1559, https://doi.org 10.1126/sciadv.abg1559 (2021).  
50. Zhang, D. et al. Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2, e1600521, https://doi.org/10.1126/sciadv.1600521 (2016).  
51. Li, Z. M. et al. Super-resolution far-field infrared imaging by photothermal heterodyne imaging. J. Phys. Chem. B 121, 8838–8846, https://doi.org/10.1021/ acs.jpcb.7b06065 (2017).  
52. Samolis, P. D. & Sander, M. Y. Phase-sensitive lock-in detection for highcontrast mid-infrared photothermal imaging with sub-diffraction limited resolution. Opt. Express 27, 2643–2655, https://doi.org/10.1364/OE.27.002643 (2019).  
53. Bai, Y. et al. Ultrafast chemical imaging by widefield photothermal sensing of infrared absorption. Sci. Adv. 5, eaav7127, https://doi.org/10.1126 sciadv.aav7127 (2019).  
54. Zhang, D. L. et al. Bond-selective transient phase imaging via sensing of the infrared photothermal effect. Light Sci. Appl. 8, 116, https://doi.org/10.1038/ s41377-019-0224-0 (2019).  
55. Tamamitsu, M. et al. Label-free biochemical quantitative phase imaging with mid-infrared photothermal effect. Optica 7, 359–366, https://doi.org/10.1364/ OPTICA.390186 (2020).  
56. Yin, J. Z. et al. Nanosecond-resolution photothermal dynamic imaging via MHZ digitization and match filtering. Nat. Commun. 12, 7097, https://doi.org/ 10.1038/s41467-021-27362-w (2021).  
57. Paiva, E. M. & Schmidt, F. M. Ultrafast widefield mid-infrared photothermal heterodyne imaging. Anal. Chem. 94, 14242–14250, https://doi.org/10.1021/ acs.analchem.2c02548 (2022).  
58. Zhao, J. et al. Bond-selective intensity diffraction tomography. Nat. Commun. 13, 7767, https://doi.org/10.1038/s41467-022-35329-8 (2022).  
59. Klementieva, O. et al. Super-resolution infrared imaging of polymorphic amyloid aggregates directly in neurons. Adv. Sci. 7, 1903004, https://doi.org/ 10.1002/advs.201903004 (2020).  
60. Stuart, B. H. Infrared Spectroscopy: Fundamentals and Applications (John Wiley & Sons, 2004).  
61. Sell, J. A. Photothermal Investigations of Solids and Fluids (Elsevier, 1989).  
62. Salazar, A. N. On thermal diffusivity. Eur. J. Phys. 24, 351–358, https://doi.org 10.1088/0143-0807/24/4/353 (2003).  
63. Li, J. J. et al. High-speed in vitro intensity diffraction tomography. Adv. Photon. 1, 066004 (2019).  
64. Ling, R. L. et al. High-throughput intensity diffraction tomography with a computational microscope. Biomed. Opt. Express 9, 2130–2141, https://doi.org/ 10.1364/BOE.9.002130 (2018).  
65. Wolf, E. Three-dimensional structure determination of semi-transparent objects from holographic data. Opt. Commun. 1, 153–156, https://doi.org/ 10.1016/0030-4018(69)90052-2 (1969).  
66. Rak, M. et al. Dense-core and diffuse Aβ plaques in TgCRND8 mice studied with synchrotron FTIR microspectroscopy. Biopolymers 87, 207–217, https:// doi.org/10.1002/bip.20820 (2007).  
67. Confer, M. P. et al. Label-free infrared spectroscopic imaging reveals heterogeneity of β-sheet aggregates in Alzheimer’s disease. J. Phys. Chem. Lett. 12, 9662–9671, https://doi.org/10.1021/acs.jpclett.1c02306 (2021).  
68. Micó, V. et al. Resolution enhancement in quantitative phase microscopy. Adv. Opt. Photon. 11, 135–214, https://doi.org/10.1364/AOP.11.000135 (2019).  
69. Sun, X. et al. Lipid droplets are present in amyloid deposits in familial amyloidotic polyneuropathy and dialysis related amyloidosis. Amyloid 13, 20–23, https://doi.org/10.1080/13506120500537137 (2006).  
70. Liao, C. R. et al. SynchrotronFTIR reveals lipid around and within amyloid plaques in transgenic mice and Alzheimer’s disease brain. Analyst 138, 3991–3997, https://doi.org/10.1039/c3an00295k (2013).  
71. Benseny-Cases, N. et al. Microspectroscopy (μFTIR) reveals co-localization of lipid oxidation and amyloid plaques in human Alzheimer disease brains. Anal. Chem. 86, 12047–12054, https://doi.org/10.1021/ac502667b (2014).  
72. Liu, H. C., Wang, Y. M. & Bowman, J. M. Quantum local monomer ir spectrum of liquid D O at 300 K from 0 to 4000 cm-1 Is in near-quantitative agreement with experiment. J. Phys. Chem. B 120, 2824–2828, https://doi.org/10.1021/ acs.jpcb.6b01722 (2016).  
73. Popescu, G. Quantitative Phase Imaging of Cells and Tissues (McGraw-Hill Education, 2011).  
74. Macias-Garza, F., Diller, K. R. & Bovik, A. C. Missing cone of frequencies and lowpass distortion in three-dimensional microscopic images. Opt. Eng. 27, 276461, https://doi.org/10.1117/12.7976703 (1988).  
75. Lim, J. et al. Comparative study of iterative reconstruction algorithms for missing cone problems in optical diffraction tomography. Opt. Express 23, 16933–16948, https://doi.org/10.1364/OE.23.016933 (2015).  
76. Tycko, R. Amyloid polymorphism: structural basis and neurobiological rele vance. Neuron 86, 632–645, https://doi.org/10.1016/j.neuron.2015.03.017 (2015).  
77. Petkova, A. T. et al. Self-propagating, molecular-level polymorphism in Alzheimer’s ß-amyloid fibrils. Science 307, 262–265, https://doi.org/10.1126/ science.1105850 (2005).  
78. Qiang, W. et al. Structural variation in amyloid-β fibrils from Alzheimer’s disease clinical subtypes. Nature 541, 217–221, https://doi.org/10.1038/nature20814 (2017).  
79. Baker, M. J. et al. Using Fourier transform IR spectroscopy to analyze biological materials. Nat. Protoc. 9, 1771–1791, https://doi.org/10.1038/nprot.2014.110 (2014).  
80. Zhu, J. B., Wang, H. & Tian, L. High-fidelity intensity diffraction tomography with a non-paraxial multiple-scattering model. Opt. Express 30, 32808–32821, https://doi.org/10.1364/OE.469503 (2022).  
81. Chung, H. et al. Missing cone artifact removal in ODT using unsupervised deep learning in the projection domain. IEEE Trans. Comput. Imaging 7, 747–758, https://doi.org/10.1109/TCI.2021.3098937 (2021).  
82. Matlock, A., Zhu, J. B. & Tian, L. Multiple-scattering simulator-trained neural network for intensity diffraction tomography. Opt. Express 31, 4094–4107, https://doi.org/10.1364/OE.477396 (2023).  
83. Shi, Y. et al. Structure-based classification of tauopathies. Nature 598, 359–363, https://doi.org/10.1038/s41586-021-03911-7 (2021).  
84. Rinnan, Å., van den Berg, F. & Engelsen, S. B. Review of the most common preprocessing techniques for near-infrared spectra. TrAC Trends Anal. Chem. 28, 1201–1222, https://doi.org/10.1016/j.trac.2009.07.007 (2009).  
85. Holmes, B. B. et al. Proteopathic tau seeding predicts tauopathy in vivo. Proc Natl Acad. Sci. USA 111, E4376–E4385, https://doi.org/10.1073 pnas.1411649111 (2014).  
86. Jiang, L. et al. TIA1 regulates the generation and response to toxic tau oligomers. Acta Neuropathol. 137, 259–277, https://doi.org/10.1007/s00401-018- 1937-5 (2019).  
87. Sanders, D. W. et al. Distinct tau prion strains propagate in cells and mice and define different tauopathies. Neuron 82, 1271–1288, https://doi.org/10.1016/ j.neuron.2014.04.047 (2014).  
88. Jiang, L. L. et al. Interaction of tau with HNRNPA2B1 and N6 -methyladenosine RNA mediates the progression of tauopathy. Mol. Cell 81, 4209–4227.e12, https://doi.org/10.1016/j.molcel.2021.07.038 (2021).  
89. BioRender.com. https://app.biorender.com/biorender-templates (2022).  
90. Gazi, E. et al. Direct evidence of lipid translocation between adipocytes and prostate cancer cells with imaging FTIR microspectroscopy. J. Lipid Res. 48, 1846–1856, https://doi.org/10.1194/jlr.M700131-JLR200 (2007).  
91. Forfang, K. et al. FTIR spectroscopy for evaluation and monitoring of lipid extraction efficiency for oleaginous fungi. PLoS ONE 12, e0170611, https:// doi.org/10.1371/journal.pone.0170611 (2017).