# Overtone photothermal microscopy for high-resolution and high-sensitivity vibrational imaging

Received: 30 June 2023

Accepted: 11 June 2024

Published online: 25 June 2024

![](images/11a7a333eb4101ee47303f868849487f2716edb9717578757b7f592498a21147.jpg)

Check for updates

Le Wang1,4, Haonan Lin 1,4, Yifan Zhu2 , Xiaowei Ge 1 , Mingsheng Li1 , Jianing Liu1 , Fukai Chen3 , Meng Zhang1 & Ji-Xin Cheng 1,2,3

Photothermal microscopy is a highly sensitive pump-probe method for map ping nanostructures and molecules through the detection of local thermal gradients. While visible photothermal microscopy and mid-infrared photo thermal microscopy techniques have been developed, they possess inherent limitations. These techniques either lack chemical specificity or encounter significant light attenuation caused by water absorption. Here, we present an overtone photothermal (OPT) microscopy technique that offers high chemical specificity, detection sensitivity, and spatial resolution by employing a visible probe for local heat detection in the C-H overtone region. We demonstrate its capability for high-fidelity chemical imaging of polymer nanostructures, depth-resolved intracellular chemical mapping of cancer cells, and imaging of multicellular  organisms and highly scattering brain tissues. By bridging the gap between visible and mid-infrared photothermal microscopy, OPT establishes a new modality for high-resolution and high-sensitivity chemical imaging. This advancement complements large-scale shortwave infrared imaging approaches, facilitating multiscale structural and chemical investigations of materials and biological metabolism.

The shortwave infrared (SWIR) window, typically spanning from 900 nm to 2 µm in the electromagnetic spectrum, offers distinct advantages for bioimaging. Compared to the mid-infrared window, the SWIR window has an \~20–5000 times (wavelength-dependent) smaller water absorption coefficient1 . Furthermore, SWIR imaging allows for unprecedentedly large penetration depth attributed to much-reduced light scattering2,3 . This depth is wavelength-dependent and can extend to the millimeter level4,5 . With the rich chemical information based on overtone absorption, SWIR spectroscopy emerges as an appealing analytical tool6 . Several SWIR imaging methods have been developed, including hyperspectral reflectance/transmittance imaging7–9 , diffuse optical spectroscopic imaging (DOSI)10–12, and photoacoustic microscopy (PAM)13,14. SWIR hyperspectral imaging, which measures reflectance or transmittance, primarily serves in the qualitative spectral characterization of samples at the macroscale, focusing on properties related to absorption and scattering. To probe macroscopic sample areas for improved representative sampling, this technique generally sacrifices spatial resolution in favor of a larger field-of-view (FOV) due to the space-bandwidth product limit, thereby leading to resolutions on the order of ten micrometers. Diffraction-limited spectroscopic imaging can be attained by magnifying the FOV onto the camera or implementing a laser point-scanning design15,16. DOSI, adopting a widefield approach, measures the combined effects of broadband optical absorption and scattering. It has proven successful in the study of thick tissues, such as functional information of bone sarcomas and breast tumor hemodynamic responses. This method offers a sub-millimeter lateral resolution and a penetration depth of generally a few millimeters. PAM utilizes an objective lens as the focusing element and

1Department of Electrical and Computer Engineering, Boston University, Boston, MA o2215., USA., 2Department of Chemistry, Boston University, Boston, M4 02215, USA. 3 Department of Biology, Boston University, Boston, MA 02215, USA. 4 These authors contributed equally: Le Wang, Haonan Lin.

e-mail: jxcheng@bu.edu

collects acoustic waves with an ultrasonic transducer to achieve optical resolution. SWIR PAM was first developed for imaging lipids based on the 2nd overtone of the C-H bond14 and more recently imaging water at 1930 nm17, whereas the sensitivity is heavily reliant on the quality of the ultrasonic transducer employed18.

Here, we introduce a technique named overtone photothermal (OPT) microscopy, which excites the sample in the SWIR window and employs a visible probe to detect the thermal lensing effect caused by overtone vibrational absorption. Specifically, we utilized a femtosecond laser tunable in the C-H 2nd overtone window and a 520 nm probe beam through the second harmonic generation of a 1040 nm femtosecond laser. Both pulses were chirped to picosecond to minimize photodamage. Compared to existing SWIR imaging methods, OPT microscopy provides simultaneous high resolution and high sensitivity. Spectroscopic OPT imaging was successfully demonstrated on polymer nanostructures. In conjunction with spectral unmixing algorithms, depth-resolved OPT mapping of protein and fatty acids in cancer cells, , and brain C. eleganstissues was performed at intracellular and multicellular levels. These results underscore the potential of OPT microscopy as a valuable technique for investigating chemical structures at high resolution in biological systems and materials.

## Results

## OPT microscope setup and signal extraction

Figure 1a illustrates a lab-built OPT microscope. The specific optical components and signal extraction methods are detailed in the Methods Section. In brief, the OPT microscope utilizes a pulsed SWIR pump beam, tunable in the range of 1080 nm to 1280 nm, and a 520 nm probe beam generated from the second harmonic generation of the 1040 nm output. Both pump and probe beams are chirped to picosecond duration by glass rods. The beams are treated as pseudocontinuous waves with a repetition rate of 80 MHz, and the excitation beam is modulated at desirable frequency (hundreds of kHz to 1 MHz) and duty cycle (10% to 50%) based on the sample’s thermal decay properties. The two beams are delivered collinearly to a laser-scanning upright microscope and focused onto the sample plane using a water immersion objective with a numerical aperture (NA) of 1.2.

Upon the SWIR illumination, the sample’s selective absorption within the focal volume leads to a local temperature rise and a thermal gradient, inducing a subtle decrease in the local refractive index at the pump beam focus. To efficiently generate photothermal signals, an axial focus displacement between the two beams is implemented, as depicted in Fig. 1b19. In this scenario, the induced thermal lens modifies the propagation of the 520 nm probe beam, causing it to diverge or converge depending on its focal position relative to the pump focus. When there is no axial offset, the thermal lens forms precisely at the focal position of the probe beam. Therefore, the ray locus of the probe beam will not be modified, and the photothermal signal vanishes.

By incorporating an iris with an adjustable NA on the collection condenser, the intensity modulation of the probe beam, corresponding to the selective absorption, can be read out by a photodiode and demodulated using a lock-in amplifier. As shown in Fig. 1c, the green curve represents the transient probe beam intensity change as a function of periodic heating and cooling processes. The direction of the probe intensity change is determined by the direction of the vertical focus displacement of the excitation and probe beams. For the provided thermodynamic trace of dimethyl sulfoxide (DMSO) shown in Fig. 1c, the focus of the probe beam is positioned above that of the excitation beam, resulting in an equivalently divergent lens and a decreased probe intensity on the photodiode. The OPT signal at the modulation frequency is extracted by a lock-in amplifier (Fig. 1d). Spectroscopic OPT imaging is performed by tuning the SWIR wavelength and recording OPT images through laser scanning facilitated by 2D galvo mirrors.

![](images/aa8fef8166b8d11d1a71dc1b7a56cbbbdbf4300e0889a8e659eb4d9c02cb06f1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Laser"] --> B["HWP"]
  B --> C["PBS"]
  C --> D["AOM"]
  D --> E["Rods"]
  E --> F["DBS"]
  F --> G["Galvo"]
  G --> H["Sample plane"]
  H --> I["Condenser"]
  I --> J["OBJ"]
  J --> K["PD Filter"]
  K --> L["Bond length"]
  L --> M["Second overtone"]
  L --> N["First overtone"]
  L --> O["Fundamental"]
  P["LBO"] --> Q["Rods"]
  Q --> R["Lens"]
  R --> S["AOM"]
  S --> T["Rods"]
  T --> U["DGB"]
  U --> V["Galvo"]
```
</details>

(b)  
![](images/4a91c3d8327b5abd57de9af1694ccd2ab900993297b5378f9820f6debbcadbbb.jpg)

<details>
<summary>text_image</summary>

(b)
ΔZf
(c)
</details>

(c)

![](images/ed6b085dca0bf525bd3a92c679b054e2d5aee7442e8aa1bd2fa371ee12a88664.jpg)

<details>
<summary>line chart</summary>

| Time | Intensity change of probe beam |
|------|-------------------------------|
| 0    | 1                             |
| 1    | 0                             |
| 2    | 1                             |
| 3    | 0                             |
| 4    | 1                             |
| 5    | 0                             |
| 6    | 1                             |
| 7    | 0                             |
| 8    | 1                             |
| 9    | 0                             |
| 10   | 1                             |
| 11   | 0                             |
| 12   | 1                             |
| 13   | 0                             |
| 14   | 1                             |
| 15   | 0                             |
| 16   | 1                             |
| 17   | 0                             |
| 18   | 1                             |
| 19   | 0                             |
| 20   | 1                             |
| 21   | 0                             |
| 22   | 1                             |
| 23   | 0                             |
| 24   | 1                             |
| 25   | 0                             |
| 26   | 1                             |
| 27   | 0                             |
| 28   | 1                             |
| 29   | 0                             |
| 30   | 1                             |
| 31   | 0                             |
| 32   | 1                             |
| 33   | 0                             |
| 34   | 1                             |
| 35   | 0                             |
| 36   | 1                             |
| 37   | 0                             |
| 38   | 1                             |
| 39   | 0                             |
| 40   | 1                             |
| 41   | 0                             |
| 42   | 1                             |
| 43   | 0                             |
| 44   | 1                             |
| 45   | 0                             |
| 46   | 1                             |
| 47   | 0                             |
| 48   | 1                             |
| 49   | 0                             |
| 50   | 1                             |
| 51   | 0                             |
| 52   | 1                             |
| 53   | 0                             |
| 54   | 1                             |
| 55   | 0                             |
| 56   | 1                             |
| 57   | 0                             |
| 58   | 1                             |
| 59   | 0                             |
| 60   | 1                             |
| 61   | 0                             |
| 62   | 1                             |
| 63   | 0                             |
| 64   | 1                             |
| 65   | 0                             |
| 66   | 1                             |
| 67   | 0                             |
| 68   | 1                             |
| 69   | 0                             |
| 70   | 1                             |
| 71   | 0                             |
| 72   | 1                             |
| 73   | 0                             |
| 74   | 1                             |
| 75   | 0                             |
| 76   | 1                             |
| 77   | 0                             |
| 78   | 1                             |
| 79   | 0                             |
| 80   | 1                             |
| 81   | 0                             |
| 82   | 1                             |
| 83   | 0                             |
| 84   | 1                             |
| 85   | 0                             |
| 86   | 1                             |
| 87   | 0                             |
| 88   | 1                             |
| 89   | 0                             |
| 90   | 1                             |
| 91   | 0                             |
| 92   | 1                             |
| 93   | 0                             |
| 94   | 1                             |
| 95   | 0                             |
| 96   | 1                             |
| 97   | 0                             |
| 98   | 1                             |
| 99   | 0                             |
| >99.5 | <1                            |
</details>

(d)  
![](images/e3579da8767771005530f869990da13d2f47b8a1a8548809d58f2c1ebaca6d0e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["High- and low-pass filters"] --> B["Voltage amplifier"]
  C["Photodiode"] --> B
  D["Probe beam"] --> E["..."]
  B --> F["Lock-in amplifier"]
```
</details>

Fig. 1 | Operational scheme of overtone photothermal (OPT) microscopy.  
a Schematics and optical components of the setup. HWP half-wave plate, PBS polarization beam splitter, AOM acousto-optic modulator, LBO lithium triborate crystal, DBS dichroic beam splitter, OBJ objective, PD photodiode. The inset is a vibrational potential energy diagram. b Beam propagation in OPT microscopy. The pulsed swIR excitation beam and the continuous 520 nm probe beam are collinearly propagated and tightly focused onto the sample plane. The axial foci of the two beams have an offset of $\varDelta Z _ { f }$ . c The waveforms of probe intensity as a function  
of periodic heating and cooling processes. The sign of the probe intensity change is determined by the sign of the axial offset between the excitation and probe foci. The shown thermodynamic trace was measured on DMSO. d Signal extraction in OPT microscopy. The probe intensity change was captured by a photodiode and converted into an electronic voltage signal. After passing through electronic filters and amplifiers, the periodic signal was demodulated by a lock-in amplifier and then registered as OPT signals per imaging pixel.

![](images/b4f750900bc92c1b86d88cf86defc3ae8564a51c59e84b9d677d2ca25dda6744.jpg)

<details>
<summary>line chart</summary>

| Wavelength / nm | Absorbance / % (NIR abs.) | Absorbance / % (OPT) | OPT signal / V |
| --------------- | ------------------------- | -------------------- | -------------- |
| 1100            | ~0.5                      | ~0.5                 | ~0.1           |
| 1150            | ~15                       | ~15                  | ~0.4           |
| 1200            | ~6                        | ~6                   | ~0.2           |
| 1250            | ~1                        | ~1                   | ~0.05          |
</details>

![](images/289a035c3ad208bd4f696ab449a48c8d55f09116da3ae3c6d8f62fa08ac89276.jpg)

<details>
<summary>heatmap</summary>

| Value |
|-------|
| 0.14  |
</details>

![](images/0727b0c6ffd9e088998716f775a590bbde38f6f429a0638467f5264dccef5eab.jpg)

<details>
<summary>scatterplot</summary>

| Distance / µm | Intensity / arb. units |
| ------------- | ---------------------- |
| 0.0           | 0.24                   |
| 0.5           | 0.24                   |
| 1.0           | 0.265                  |
| 1.5           | 0.24                   |
| 2.0           | 0.24                   |
</details>

![](images/cae854f43083c77e08585d877bac4539579b0deb202075e5a54cc0e5400c2062.jpg)

<details>
<summary>line chart</summary>

| Wavelength / nm | Absorbance / % | OPT signal / V |
| --------------- | -------------- | -------------- |
| 1100            | 0              | 0.1            |
| 1150            | 20             | 0.3            |
| 1200            | 60             | 0.4            |
| 1250            | 40             | 0.3            |
</details>

![](images/6aa353423ca15f8874c870c3db2ead82306391cc20870a74cd63583ef73065ba.jpg)

<details>
<summary>line chart</summary>

| SWIR power / mW | Intensity / arb. units (e) | Probe power / mW | Intensity / arb. units (f) |
| --------------- | -------------------------- | ---------------- | -------------------------- |
| 5               | 4.0                        | 3                | 2.0                        |
| 10              | 6.0                        | 7                | 4.0                        |
| 15              | 8.0                        | 10               | 6.0                        |
| 20              | 10.0                       | 13               | 8.0                        |
| 25              | 12.0                       | 16               | 10.0                       |
| 26              | 13.0                       | 18               | 11.0                       |
| 27              | 14.0                       | 20               | 12.0                       |
</details>

![](images/38ad6178dfeaae4982c836ed64d8d2c86b3acdeede02f654209f35e9acadcc96.jpg)

<details>
<summary>line chart</summary>

| Wavelength / nm | 3.4% DMSO | 2% DMSO | 1% DMSO | glycerol-d8 |
| --------------- | --------- | ------- | ------- | ----------- |
| 1100            | 0.4       | 0.4     | 0.4     | 0.4         |
| 1125            | 0.6       | 0.5     | 0.4     | 0.4         |
| 1150            | 1.0       | 0.9     | 0.5     | 0.4         |
| 1175            | 1.8       | 1.3     | 0.8     | 0.6         |
| 1200            | 1.2       | 1.2     | 1.0     | 0.9         |
| 1225            | 1.3       | 1.2     | 1.1     | 1.0         |
| 1250            | 1.0       | 0.9     | 0.8     | 0.7         |
| 1275            | 0.7       | 0.6     | 0.6     | 0.6         |
</details>

![](images/029aafd7033bcc0a8908229c8d740d9a930537c26071a2dc718006db41ae24fc.jpg)

<details>
<summary>line chart</summary>

| Z / μm | Intensity / arb. units |
| ------ | ---------------------- |
| -6     | 0.0                    |
| -4     | 0.0                    |
| -2     | 0.05                   |
| 0      | 0.25                   |
| 2      | 0.0                    |
| 4      | 0.0                    |
| 6      | 0.0                    |
</details>

Fig. 2 | System characteristics. a Spectral fidelity demonstrated on 10-µm polystyrene beads. The NIR spectrum of PS solution collected from a UV-Vis-NIR spectrophotometer was plotted as a reference. b Spectral fidelity demonstrated on pure solvent ethylene glycol. c OPT image at 1170 nm of 200-nm PMMA beads dispersed in glycerol-d8. Individual beads and bead aggregates are observed in the image. d Cross-section profile along the marked dashed line in c to estimate the lateral resolution in OPT microscopy. e Power dependence of OPT signals as a function of SWIR excitation power. f Power dependence of OPT signals as a  
function of the 520 nm probe power. g OPT spectra measured from multiple concentrations of DMSO@glycerol-d8 solution. The OPT signal at 1170 nm of 1% DMSO can be clearly distinguished out of the background of glycerol-d8.  
h Longitudinal view of a 3D OPT imaging of a 1-µm PMMA bead at 1170 nm. i Axial OPT point spread function profile measured from h. The inset shows an image of this bead at $Z = 0 \mu \mathrm { m } .$ . The axial position of the particle was precisely controlled Zthrough a piezo stage.

## System characteristics

To evaluate the performance of OPT microscopy, we first conducted a study examining its spectral fidelity. OPT spectra of 10-µm polystyrene (PS) beads and pure ethylene glycol were collected and compared with standard near-infrared absorption spectra from a UV-Vis-NIR spectrophotometer. Our results, as presented in Fig. 2a, b, demonstrate a good consistency between the two types of spectra. The PS spectra exhibited two prominent peaks at 1144 nm and 1205 nm, corresponding to the aromatic and aliphatic C-H 2nd overtone absorption, respectively4 . The OPT spectra of ethylene glycol showed a broad peak at around 1205 nm, attributed to the peak shape alternation of aliphatic C-H bonds connected with hydroxyl groups.

Additionally, we assessed the lateral resolution and detection sensitivity via OPT imaging of 200-nm PMMA beads. The OPT image was acquired at 1170 nm, corresponding to the 2nd overtone resonance of PMMA. The heating beam had a modulation frequency of 800 kHz and a duty cycle of 50%, resulting in a pulse duration of 625 ns. The average power of the 1170 nm beam was set at 40 mW on the sample. It is important to note that the selection of experimental parameters plays a crucial role in optimizing imaging performance. To guide the parameter selection, we performed a theoretical simulation using COMSOL to analyze the transient temperature changes during the periodic heat accumulation and dissipation processes20–22. A detailed description of the thermodynamic simulation can be found in Supplementary Note S1, and thermodynamic traces of 200-nm PMMA beads in glycerol-d8 and ${ \bf D } _ { 2 } { \bf O }$ were compared. The simulation revealed that the maximum temperature rise in glycerol-d8 as the medium was \~3.6 K, which is higher than that in $\mathsf { D } _ { 2 } \mathbf { O }$ (Supplementary Fig. S1). The thermal decay constant was found to be 35 ns in glycerol-d8 and 28 ns in ${ \bf D } _ { 2 } { \bf O }$ . We found that a repetition rate as high as 1 MHz can be used to enhance the imaging speed, with the prerequisite of ensuring sufficient heat dissipation.

To determine the lateral resolution, we imaged individual PMMA beads and bead clusters at 1170 nm (Fig. 2c). A BM3D denoising algorithm was applied to enhance the signal-to-noise ratio $( \mathsf { S N R } ) ^ { 2 3 }$ , and a SNR of 4 was observed on a single bead. The cross-section line profile marked by the dashed line shows a full-width-at-half-maximum (FWHM) of 432 nm (Fig. 2d) and indicates a lateral resolution of 405 nm after deconvolution with the particle size. The theoretical diffraction limit calculated based on two axially overlapped Gaussian beams is given by

$$
\text { Resolution } = \frac {0 . 6 1}{N A} \times \left(\sqrt {1 / \left(\frac {1}{\lambda_ {\text { pump }} ^ {2}} + \frac {1}{\lambda_ {\text { probe }} ^ {2}}\right)}\right) = \frac {0 . 6 1}{1 . 2} \times \left(1 / \sqrt {\frac {1}{1 1 7 0 ^ {2}} + \frac {1}{5 2 0 ^ {2}}}\right) = 2 4 2 n m.
$$

This discrepancy between theory and experiment is likely due to the practical axial displacement $ { \Delta Z _ { f } }$ between the two beams, and $\Delta Z _ { f }$ Zf Zfcan have both positive and negative values, typically on the order of several hundreds of nanometers to several microns19,24.

The power dependence of OPT signal intensity on the pump and probe power is depicted in Fig. 2e, f. The OPT intensity exhibited a linear relationship with both excitation and probe powers, consistent with observations made in visible photothermal and mid-infrared photothermal (MIP) microscopies25,26. To determine the limit of detection, we conducted measurements on serial-dilution samples of DMSO dissolved in glycerol-d8. A peak at 1170 nm, corresponding to the absorption of methyl groups in DMSO, was observed (Fig. 2g).

The OPT spectrum of DMSO was shown in Supplementary Fig. S2a. It should be noted that the solvent glycerol-d8 is not entirely transparent in this spectral window and exhibits a broad peak at approximately 1220 nm, resulting from the resonance of C-D bonds affected by O-D groups. Despite the solvent background, we were able to detect 1% DMSO at a SNR of 8. The theoretical detection limit of DMSO-inglycerol-d8 solutions, calculated from the statistical 3-Sigma (three times of the measurement noise after background subtraction) at 1170 nm, is found to be 0.3% DMSO (Supplementary Fig. S2b, c). The 200-nm PMMA beads presented in Fig. 2c also highlight the high sensitivity of OPT for imaging of nanoparticles.

To demonstrate the 3D imaging capability of OPT microscopy, we performed depth-resolved imaging of a single 1-µm PMMA bead at 1170 nm, as shown in Fig. 2h. Each image in the stack was collected with a 200 nm increment in the vertical direction. An intensity profile along the axial direction (Fig. 2i) indicates an axial resolution of $2 \mu \mathrm { m }$ . The dispersive axial profile of OPT signals arises from the interference between scattered and incident laser fields and is closely linked to the axial displacement $ { \Delta Z _ { f } }$ between excitation and probe lasers27.

OPT imaging and spectroscopy of fabricated polymer structures The high spatial resolution and sensitivity of OPT microscopy allow for the identification of fabricated polymer structures. Phase separation patterns of spin-coated PS-PMMA polymer blends (Fig. 3a) and fabricated PMMA striped structures were used to evaluate its performance. Controlled phase separation morphology in polymers is essential for designing thin film devices with desired mechanical, thermal, and electronic properties28,29. The resulting morphology can be finely tuned by manipulating factors such as temperature, molar ratio of polymer components, polymer solubility, and film thicknesses30.

Figure 3b displays OPT spectra of the two polymer components, and Fig. 3c–f presents two-color imaging results of the phase separation patterns. PS domains at 1140 nm and PMMA domains at 1170 nm were individually identified, demonstrating complementary patterns. These images are single frames without any averaging or denoising. Figure 3e shows an overlaid channel of PS and PMMA, clearly illustrating the distribution of each domain. Additionally, an AFM topography image in Supplementary Fig. S3 demonstrates the representative morphology of the phase-separated sample. PS domains appear as irregular-shaped holes with smaller heights, while the higher areas correspond to the PMMA matrix. The height difference between PS and PMMA domains is less than 80 nm, indicating the superior sensitivity of OPT in distinguishing neighboring polymer domains with distinct spectral features. Cross-section line profiles in Fig. 3f further confirm the complementary distribution of the two domains, with PMMA domains smaller than 500 nm in diameter detected within the surrounding PS domains.

OPT microscopy was also utilized to image fabricated nanostructures of homopolymers. As illustrated in Fig. 3g, h, PMMA striped patterns, prepared via electron beam lithography, were imaged at 1170 nm. Each stripe measures 500 nm in width and 650 nm in height, with a distance of $1 . 5 \mu \mathrm { m }$ between the centers of neighboring stripes, as confirmed by the AFM topography image. Cross-section profiles of OPT signals and height information along the dashed line were co-plotted in Fig. 3i. A Gaussian-like shape of the OPT signal on each stripe is observed, resulting from the convolution of the illumination laser’s point spread function (Gaussian) and the cuboid-shaped sample. Both the PS-PMMA phase separation and PMMA striped structures were examined in ambient air, demonstrating the potential of OPT microscopy for applications in materials science, particularly in the design of thin film devices with tailored properties.

![](images/7a35f1076a1b92eef958f311fa9ac671ff7af6a7697f3fff0c1a41c2a59c8e65.jpg)  
Fig. 3 | Overtone photothermal (OPT) spectroscopy and imaging of phase separation patterns of PS & PMMA blends and stripe-structured PMMA.

a Schematics of spin-coating procedures used for the preparation of microphase separation patterns of PS and PMMA blends. b OPT spectra of pure PMMA and PS as a guide for wavelength selection for PS and PMMA imaging. c, d OPT single-frame images at 1140 nm and 1170 nm, corresponding to the absorption of PS and PMMA, respectively. These images present complementary patterns of the distribution of PS and PMMA domains. e Overlaid channel of c, d, showing the combined

distribution of PS and PMMA domains. f Plot of cross-section profiles along the dashed line marked in e. g OPT image of the striped PMMA nanostructures at 1170 nm. h Corresponding AFM topography image of the same field-of-view, providing additional structural information. i Co-plot of the OPT signal cross-section and the height information of PMMA stripe nanostructures. a was created with BioRender.com released under a Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International license.

(a)  
![](images/b7dafd9df25c43636a81e736b0a2fa09558ded39589b4567525ddf94a054bd67.jpg)

<details>
<summary>text_image</summary>

Water immersion
objective NA = 1.2
Glass bottom dish
</details>

(b)  
![](images/364db3e7df4a93743aebee140bc645b22ae8e8962bb9a5c2ab754b7887586a30.jpg)

<details>
<summary>heatmap</summary>

| Z (μm) | Intensity (e.g., μs) |
|--------|----------------------|
| 0      | 0.9                  |
| 2.5    | 1                    |
| 6     | 0.9                  |
| 7     | 0.9                  |
| 8.5    | 0.9                  |
| 10    | 0.45                 |
</details>

(c)  
![](images/cc4ea6ba17aedd0ab439b8643a9f05147813e621fbcd33f79ec2714bb4c833f0.jpg)

<details>
<summary>line chart</summary>

| Wavelength / nm | BSA   | TAG   | Water |
| --------------- | ----- | ----- | ----- |
| 1100            | 0.0   | 0.0   | 0.0   |
| 1150            | 0.5   | 0.3   | 0.8   |
| 1200            | 1.0   | 1.0   | 1.0   |
| 1250            | 0.5   | 0.5   | 0.5   |
</details>

![](images/8181980cab694e546ea9930448496d1c9ae69a1464f4b2ac29cb7d2008f5e203.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a cellular or particulate structure with scale bar indicating 8 μm and height annotation Z = 3 μm (no text beyond labels)
</details>

0.55 |0.1  
![](images/2aadec6a6ab2e0d8c4f21ad772ca64484d32121bdec58446595db4d4a48183b4.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a cell with fluorescent staining, labeled 'Protein' in top-left corner (no other text or symbols)
</details>

0.24 0.02  
![](images/7b6f51a2cd0faa08d7f4dca1deb796f35c15e8dbe3d3d0d4b20ffa61d5658675.jpg)

<details>
<summary>text_image</summary>

Fatty acid
</details>

0.24 0.03

![](images/39e8f8e4aa96b5374b0c5fef737d5dd9bd06e17e8111ede5472ad7d6a9291559.jpg)

<details>
<summary>heatmap</summary>

| Intensity (arb. units) |
| ---------------------- |
| 0.75                   |
</details>

![](images/406c72e98bc6618282439b95e1c2c0320a1bfca7d936be557ce40dbad6065cf5.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of a biological cell or particle with scattered bright spots, labeled (e) and z = 9 μm (no text or symbols on the main subject)
</details>

0.49 0.21  
![](images/cf2837a1431dd3f2edb41029ab936fb1b08366d5651556073710f52eb9f2f6df.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of a biological sample with fluorescent staining (no visible text or symbols)
</details>

0.17 0.01  
![](images/83f1c6464dc6ede0120e33687b585d294361a5596c14a4ea5b5c0a31dfe1bbe6.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of scattered pink and white particles against a dark background (no text or symbols)
</details>

0.19

![](images/1e33456761fc019e72edd29f5ea312f476b8600ddc53efcd647c836f8d0b3553.jpg)

<details>
<summary>heatmap</summary>

| Intensity (arb. units) |
| ---------------------- |
| 0.45                   |
</details>

Fig. 4 | Depth-resolved overtone photothermal (OPT) imaging and spectral unmixing to reveal the spatial distribution of protein and fatty acids in OVCAR-5 single cells. a Schematics of using a water immersion objective for cell imaging in OPT microscopy. b Single-frame OPT image at 1190 nm at multiple Z positions. 1190 nm falls within the range of overlapped absorption of protein and fatty acids. c OPT spectra of pure BSA, TAG, and water, serving as spectral  
references in LASSO spectral unmixing. d Raw average OPT image at $Z = 3 \mu \mathrm { m }$ and resulting protein, fatty acid, and water maps. The water background was removed from protein and fatty acid channels through the unmixing of the water compo nent. e Raw average OPT image at $Z = 9$ µm and resulting protein, fatty acid, and water maps. a was created with BioRender.com released under a Creative Commons Attribution NonCommercial-NoDerivs 4.0 International license.

## Depth-resolved OPT imaging of metabolites inside ovarian cancer cells

The biological aqueous environment is an essential prerequisite for live cell imaging since it allows for the samples to be examined in their native environment to provide crucial insights into cellular processes and interactions. To evaluate the performance of OPT microscopy in aqueous environment, we used PS beads as a model system. As shown in Supplementary Fig. S4a, we observed a water background in the OPT image of 1-µm PS bead clusters, and the directly extracted PS spectrum was obscured due to the contribution of water. However, by subtracting the water background from the raw PS spectrum, we were able to retrieve a correct PS spectrum (Supplementary Fig. S4b). This highlights the necessity of spectro scopic analysis to resolve chemical compositions in biological studies conducted under aqueous conditions.

Moving forward, we delved into mapping the intracellular metabolites of OVCAR-5 ovarian cancer cells, with a specific focus on the protein and fatty acid content and distribution, as lipogenesis is a biomarker for cancer cells31,32. Given the heterogeneity observed in different layers of a single cell, we recognized the need for depthsectioning spectroscopic imaging to accurately acquire metabolic distributions. Therefore, we performed depth-resolved hyperspectral OPT imaging of cancer cells at incremental axial slices. Prior to measurement, the cells were fixed in formalin and washed three times in phosphate-buffered saline (PBS) buffer. Figure 4b displays the OPT images at 1190 nm of multiple focal planes of a single cell, and various cell features were observed at different sectioned layers. As the sample stage moved closer to the objective, the imaging plane moved towards the bottom of the dish, allowing us to observe the nucleus and nucleolus more clearly when the axial focus was at the top part of the cell, while lipid droplets were found more distributed at the bottom of the cell. It’s important to recognize that the detected OPT signal intensity is influenced by both the scattered light intensity and the modulation depth resulting from photothermal absorption. This characteristic indicates the potential for bias in the determination of absolute chemical concentrations due to optical scattering. In Supplementary Fig. S5, we present transmission images (DC signals) without SWIR beam excitation, alongside OPT images (AC signals) of single cancer cells. This comparison allows for a comprehensive assessment of the potential bias. Consequently, the subsequent chemical decomposition via OPT microscopy is carried out in relative concentration (semi quantitative) measurements, rather than precise absolute quantitative values.

![](images/1e8d50386d239e341e599a1c2e1d2d33196135ee23447b8a702f3681df4f56df.jpg)  
Fig. 5 | Depth-resolved overtone photothermal (OPT) imaging and spectral unmixing of OVCAR-5 single cells in $\mathbf { D _ { 2 } O P B S } .$ . a Single-frame OPT images at 1190 nm at multiple focal planes showing different cellular regions. b Reference  
OPT spectra of BSA and TAG for LASSO hyperspectral unmixing. c–e Raw OP images and corresponding protein and fatty acid maps at = 6 µm, 8 µm, and 10.5 µm, respectively.

To accurately generate chemical concentration maps of protein and fatty acid, we leveraged the least absolute shrinkage and selection operator (LASSO) algorithm33,34 for a pixel-wise unmixing based on their spectral profiles. Detailed LASSO algorithms and procedures are described in the Methods Section. Our high spectral resolution allowed us to distinguish between the overlapped peaks of C-H absorption. By employing sparsity-constrained hyperspectral image unmixing via the pixel-wise LASSO algorithm, we were able to further enhance the chemical resolving power of our instrumentation. We collected OPT spectra of bovine serum albumin (BSA) and triglyceride (TAG) and used them as reference chemicals for con centration unmixing of protein and fatty acid components $( \mathsf { F i g . 4 c } ) ^ { 3 5 }$ . To exclude the water absorption background and address the overlapped spectral shapes, we performed three-component spectral unmixing for protein, fatty acid, and water. Raw average OPT images and the generated chemical maps of protein, fatty acids, and water at two depths are demonstrated in Fig. 4d, e. Our analysis revealed that protein constitutes a significant component of the cell body, and its OPT signal generally becomes weaker when focusing on the bottom layer of the cell. Conversely, the concentration and distribution of fatty acids, which mainly manifest as lipid droplets, vary significantly at each depth. Besides, lipid droplets contain a heterogeneous protein abundancy due to the presence of proteins or enzymes on the surface that regulate lipid metabolism. Some of the droplets observed in Fig. 4d, e are protein-rich, while a few others are purely dominated by the lipid cores. The inclusion of water as a component in the spectral unmixing process was advan tageous for both removing background and enhancing image accuracy. By assigning all water signals to a separate image, the uneven background and artifacts were effectively removed from protein and lipid channels, and the resulting chemical maps were clearly distinguished and significantly improved with high signal-tobackground ratios.

An alternative way to deal with the water backgroud is replacing the medium with heavy water PBS (D O PBS). The absorption cross section of ${ \bf D } _ { 2 } { \bf O }$ within the 2nd overtone range is \~1/50 of $\mathbf { w a t e r } ^ { 3 6 }$ , resulting in a negligible signal that is easily removable by background subtraction. Consequently, biomass can be directly visualized and two-component LASSO analysis is sufficient to generate lipid and protein maps. Figure 5 illustrates the depth-resolved ima ging of single OVCAR-5 cells in $\mathsf { D } _ { 2 } \mathbf { O }$ PBS, where the chemical concentration maps of protein and fatty acids were generated at three focal planes targeting different cellular regions. $\mathbf { A } \mathbf { t } Z { = } 6 \mu \mathrm { m }$ , an oval Zprotruding nucleus with nucleoli is observed, surrounded by lipid droplets and aggregates. The main cell body at $Z = 8 \mu \mathrm { m }$ exhibits a Zprotein-rich cell network with embedded lipid droplets. The bottom layer of the cell primarily consists of lipids with minimal protein concentration due to the thin vertical integral volume.

Leveraging the LASSO-based spectral unmixing algorithm, we have achieved depth-resolved intracellular structural and chemical fingerprints within the C-H 2nd overtone absorption window of single cancer cells, as demonstrated in Figs. 4 and 5. High flexibility and applicability of OPT microscopy in biological mapping was demonstrated, regardless of the imaging media employed. This versatility allows for imaging living-cell dynamics in their natural conditions using regular PBS or performing fixed-cell imaging in $\mathsf { D } _ { 2 } \mathbf { O }$

![](images/4cd239e74787a99bc992e1e88873cdc293b013c5d72ed62437723edbd701bbb3.jpg)

<details>
<summary>natural_image</summary>

Diagram of layered materials with wavy top layer and wavy bottom layer, no text or symbols present
</details>

(b)  
![](images/c80a660dc6f14f462eda9d2613f2610b4d6652eb9449ce3c42840ac721ec446f.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a U-shaped biological structure with a 20 μm scale bar, showing no text or symbols.
</details>

(c)  
![](images/91b426f8ba0a891da426e31834a30d8ad57bbaf23060a6116c577520c6e858b8.jpg)

<details>
<summary>text_image</summary>

Z = 0 µm
20 µm
0.1
0.04
0.1
Z = 12 µm
2
0.1
(f)
Z = 18.8 µm
2
0.1
0.28
Intensity / arb. units
0.05
</details>

(d)  
![](images/8a88db2f0d4d3103be612b9cea91eeafa7cbceb60fccc9e589c3334df2bb6d6d.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a U-shaped biological structure with scale bar indicating 20 μm and depth labeled as Z = 12.8 μm (no other text or symbols)
</details>

(e)  
![](images/4831c22638c0725612f0c1b61a3c8919a8fa7b9106fba7d880be36687dcdf854.jpg)

<details>
<summary>text_image</summary>

Z = 19.2 µm
</details>

f)  
![](images/114351b895c2653e328684e7c04a476f41656ea4bcff9f99e48aa8881ae64858.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a U-shaped biological structure with scale bar (0–1.5 arb. units) and Z-value annotation (22 μm), no readable text or symbols beyond measurement markers.
</details>

![](images/cca64b1a39d64735a63ebe38e0e6bd4d9822fe840835d87a7eeecf253b7dd2a4.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological structure with green fluorescent staining, labeled 'Protein' (no other text or symbols)
</details>

![](images/737633a61eb047a0a6b31700d9fd1e82d54fc25fb125f7d7560d9cf54347f43e.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of a biological structure with fluorescent staining (no text or symbols visible)
</details>

![](images/53ef5a8e13c8fc631aa288d9273aee21a797291699e4f3523fca5139b2a972ea.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological structure with fluorescent intensity scale (0 to 0.55 arb. units), no readable text or symbols present.
</details>

![](images/7c41ff38698801422ab6e88d059cbc77064c25c0fe8268036d56c23cbcec9266.jpg)

<details>
<summary>text_image</summary>

Fatty acid
</details>

![](images/abdde3bd94e38bc621674be6299286d9bc2097d7389ef68cf57a62780e6bcdbd.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a curved biological structure with fluorescent staining (no text or symbols)
</details>

![](images/bc051371daff69235b08ca9a7e47742e80fd9ad7177ec52d25ac61617ebe1887.jpg)

<details>
<summary>heatmap</summary>

| Intensity / arb. units |
| ---------------------- |
| 0.1                    |
| 0.36                   |
</details>

![](images/08da17b0fa2625b29c929da15cb6d30a4f418bc413656b746094186eefb32ac6.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of a U-shaped biological structure with green fluorescence, labeled 'Water' in top left (no other text or symbols)
</details>

![](images/8ecd77269b6707480b71b5e77d5d76b9c8f630a7e8448ad785993c959318b7ad.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of a biological structure with green fluorescent staining (no text or symbols)
</details>

![](images/2a9bbbbc088a8ca7bb3d3788d6d6e22280ee53ca6ba12447bf7ac83da5ae3d8c.jpg)

<details>
<summary>natural_image</summary>

Thermal or intensity map of a biological structure with color scale (0 to 1.52 arb. units), no readable text or symbols beyond the color legend.
</details>

Fig. 6 | Depth-resolved overtone photothermal (OPT) imaging and spectral unmixing on . worms in aqueous PBS. a The worms were immersed in PBS and gently sandwiched by two coverslips for imaging. b A full field-of-view OPT image at 1190 nm capturing an entire worm, with a zoomed-in area of the body marked for detailed analysis. c Single-frame OPT image at 1190 nm of the zoomed-  
in section of a ${ \cal Z } = 0 \mu \mathrm { m }$ , 12 µm, 18.8 µm, and 25 µm. d–f Raw average OPT images and their corresponding protein, fatty acid, and water concentration maps a $: Z = 1 2 . 8 \mu \mathrm { m } _ { . }$ , 19.2 µm, and 22 µm, respectively. a was created with BioRender.com released under a Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International license.

PBS, thereby offering nearly background-free imaging and analysis capabilities.

## Depth-resolved OPT metabolic mapping of

C. elegansWith 3D spatial resolution, OPT microscopy has prospect in studying larger and more complex biological systems. To explore this potential, we performed in vivo OPT mapping of the multicellular organism , a model system in biological studies due to its C. eleganssimple anatomy and well-characterized nervous system. The chemical specificity within provides insights into the C. elegansmechanisms underlying its behaviors and potential applications in therapeutic medical studies37.

Figure 6 presents OPT images of multiple layers of a zoomed-in worm body in an aqueous PBS environment. The worm observed was at an early developmental stage, with a diameter of \~20 µm and a length of 200–300 µm. To generate chemical maps, we performed a three-component (protein, fatty acid, water) LASSO unmixing. Despite moderate water absorption in the raw OPT images of aqueous PBS medium, the spectral unmixing successfully removed the water background and generated protein and fatty acid concentration maps. Additionally, we performed OPT hyperspectral imaging in ${ \bf D } _ { 2 } { \bf O }$ PBS on a different worm, as depicted in Supplementary Fig. S6. The two datasets exhibited similar chemical spatial specificity, with protein distributed uniformly throughout the entire worm body while fatty acids predominantly localized near intestinal cells and skin-like hypodermis, which serves as the organism’s fat storage sites38. We also visualized a large number of native lipid droplets with various sizes and morphology in hypodermal adipocytes. Our sectioning chemical maps revealed the varying 3D distributions of not only protein and lipid granules but also major tissues such as the intestine, muscle, and hypodermis. These findings demonstrate the promising potential of OPT microscopy to provide quantitative insight into chemical information in large and complex multicellular biological systems, with a flexibility of choosing ${ \sf H } _ { 2 } { \sf O }$ PBS or $\mathsf { D } _ { 2 } \mathbf { O }$ PBS as the media.

## OPT mapping of lipids and proteins in a highly scattering mouse brain tissue

The brain is a complex system composed of diverse cell types and specialized functional regions. In-depth exploration of local cerebral functions and the determination of in situ chemical compositions are essential for a comprehensive understanding of brain tissue dynamics. Among these functional regions, the corpus callosum holds a pivota role, serving as the primary white matter tract in the brain by connecting the cortices of the two cerebral hemispheres and facilitating interhemispheric communication39. To investigate the applicability of OPT microscopy in this context, we conducted depth-resolved imaging of heterogeneous structures within a mouse brain slice, with a particular focus on the corpus callosum regions. Furthermore, we utilized the LASSO spectral unmixing algorithm to effectively delineate individual protein and fatty acid distributions across two distinct structural layers.

Mouse brain slices, 200 µm in thickness, were prepared and immersed in PBS for subsequent OPT imaging. In Fig, 7a, b, a schematic illustration of the mouse basal forebrain section is presented, along with a transmission image capturing a specific region of the corpus callosum. The image stack, acquired at 1190 nm for varying depths ranging from 0 to 100 µm, substantiates enhanced penetration capabilities compared to MIP measurements, which achieve an approximate depth of 40 µm on brain slices (Supplementary Fig. S7). These depth-resolved images provide a comprehensive view of structural and chemical variations from the surface to deeper layers. Notably, we observed pronounced structural heterogeneity, including sparsely distributed nerve fibers and thick nerve fiber bundles, indicating a complex microarchitecture. To account for potential optical scattering effects, DC (transmission) images at

![](images/a54097bdecdb398baa075ec88d9104c79bfa6c6a3cf3ff15c1200aedd5a66017.jpg)  
0.37

Fig. 7 | Overtone photothermal (OPT) imaging and spectral unmixing of mouse brain slices. a Schematic illustration of mouse basal forebrain coronal sections. The green-shaded area highlights the striatum region, where a key component is corpus callosum, marked by a star. A zoomed-in view shows a transmission image captured by an eyepiece camera, focusing on the area of interest within the corpus callosum. The dashed square outlines the region of OPT imaging. b Single-frame depth-resolved OPT images at 1190 nm within a depth range of 0–110 µm.

Structural heterogeneity was identified and a penetration depth of \~100 µm can be achieved with OPT microscopy for imaging in turbid media. c A raw average OPT image at $Z = 1 0$ µm and corresponding protein, fatty acid, and water maps. d A raw ZOPT image at $Z = 3 0$ µm and corresponding protein, fatty acid, and water maps. a was created with BioRender.com released under a Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International license.

depths of $1 0 \ - 1 0 0 \mu \mathrm { m }$ are included in Supplementary Fig. S8 for reference.

It’s worth noting that, in the current configuration of OPT microscopy, the penetration depth is primarily determined by the visible probe beam rather than the SWIR beam. The 520 nm beam encounters more pronounced wavefront distortion and focus broadening than the SWIR beam while transmitting through a turbid medium, due to considerable multiple scattering effects. As demonstrated in Supplementary Fig. S9, the SWIR beam exhibits the capability to penetrate through the entire working distance (0.28 mm) of our water objective without substantial beam focus distortion.

Consistent with prior literature, white matter is known to be lipidrich, and the corpus callosum, in particular, is characterized by a high myelin content, resulting in a substantial lipid presence40,41. Our analysis of protein and lipid distribution maps, as illustrated in Fig. 7c, d, supports this observation. Proteins are primarily associated with structural elements, whereas lipids prevail, especially within the relatively sparse nerve fibers. Owing to the high resolution of OPT microscopy, individual fibers in the white matter can be observed. The water content maps are provided simultaneously.

## Discussion

SWIR imaging has great potential for the visualization of biological structures and metabolites deep inside opaque tissues. A panel of SWIR spectroscopy and imaging technologies, such as hyperspectral transmittance and reflectance8 , photoacoustic14, and OCT (optical coherence tomography)-based imaging42, have been widely adopted for their curial roles in biomedical functional and chemical analysis. To accommodate a larger FOV and deeper penetration, current SWIR imaging approaches often sacrifice lateral resolution and detection sensitivity. In this work, we introduced OPT microscopy, utilizing SWIR excitation of overtone bands coupled with a visible beam to probe thermal effects. OPT microscopy achieves both high resolution and high sensitivity, benefiting from its pump-probe detection scheme, the utilization of a visible probe, and a high numerical aperture (NA) objective. As demonstrated in the results of polymer nanoparticles, OPT microscopy offers a lateral resolution of 405 nm and can clearly detect individual 200-nm PMMA beads. This is the first time to achieve simultaneous high spatial resolution and high sensitivity imaging within the SWIR region. We should acknowledge that such advantages come with a compromised imaging depth of \~100 µm. Nevertheless, the enhanced imaging resolution and sensitivity broadens the applicability of SWIR spectroscopy, enabling the visualization of subcellular features, characterization of materials such as nano-plastics or nanoscale organic contaminants in semiconductors, and identification of small drug particles in pharmaceutical products.

Photothermal microscopy is a pump-probe technique that optically detects local thermal gradients with high sensitivity. In photothermal microscopy, molecules or nanoparticles in a sample selectively absorb the pump excitation beam and undergo local temperature increase. The temperature change induces a local variation of the refractive index of the medium, thus altering the transmission or scattering of the probe beam. To date, two main categories of photothermal microscopy have been developed based on the choice of excitation frequency in the visible or mid-infrared. Visible photothermal microscopy leverages the field enhancement of gold nanostructures and targets single light-absorbing nanoparticles, such as single nonfluorescent dye molecules43 and semiconductor nanocrystals44. To enable bond-selective photothermal imaging, MIP microscopy offering abundant chemical information in the fingerprint region has been developed21,26,45,46. MIP has been successfully applied to material and life science. Examples include mapping of Fabry–Pérot modes of single metal nanowires47 and local cation heterogeneities of perovskites48, probing bacterial metabolic responses at a single-cell level49–51, structural mapping of proteins in cells and tissues52,53, and mapping of enzymatic activities through MIP reporters in the silent window54. Despite these achievements, MIP microscopy faces a strong absorption of water, resulting in substantial optical losses in thick tissues and a considerable background for measurements in aqueous environments.

In comparison, OPT microscopy provides chemical specificity while circumventing the substantial optical attenuation caused by water absorption in the mid-IR range. This enables versatile imaging applications, from observing living cells in their native environment to achieving deeper penetration into biological tissues. Including hyperspectral unmixing analysis further enhances the chemical resolving power in the SWIR window, where multiple functional groups exhibit overlapping absorption peaks. Supplementary Table 1 summarizes the attributes of current SWIR imaging methods, MIP microscopy, and OPT microscopy.

A key advantage of OPT over MIP microscopy lies in its compatibility with high NA objectives. Existing mid-infrared imaging platforms often employ parabolic mirrors or reflective objectives with an effective NA of up to 0.8. In contrast, the SWIR range is not limited by such optical constraints and can fully exploit high NA objectives, including water-immersion and oil-immersion objectives. This feature significantly increases the focused power density, and boosts signal intensities. Moreover, the optical configuration of co-propagationbased laser scanning of SWIR and probe beams simplifies instrumentation complexity and streamlines alignment procedures. This simplicity stands in contrast to mid-IR photothermal microscopy, which compromises lateral resolution through co-propagation via a low-NA objective. To maintain high lateral resolution in mid-IR approaches, a counter-propagation configuration of the mid-IR beam and probe beam is typically required, resulting in more challenging alignment and laser scanning implementation.

One limitation of OPT microscopy lies in the strong overlap of overtone bands in the SWIR spectroscopic window, which results in crosstalks between chemical species. In this work, we sought to improve the specificity through synergistic innovations in instru mentation and data science. Compared with traditional SWIR technologies, OPT can perform hyperspectral imaging at a subcellular resolution of 405 nm. We reason that under such resolutions, for a spatially heterogeneous biological system, only a few species have dominant contributions within each laser scanning spot. This physical prior knowledge, which we refer to as “local chemical sparsity”, is mathematically translated as an L1-norm regularizer on the concentration vector at each pixel (i.e., pixel-wise LASSO), thereby suppressing signal crosstalks effectively. Nevertheless, several challenges remain in advancing the quantitative multiplexing capability of OPT spectroscopic imaging. First, photothermal lensing detection is known to scale with both absorption and local optical scattering, the latter of which can result in biased concentrations after unmixing. This issue could be potentially addressed by either leveraging the water unmixing channel as a local calibration metric to compensate for scattering bias, or through quantitative phase detection, which scales solely with refractive index. Second, the broad spectral peaks in the SWIR region still pose a high demand for the SNR of the data. Heuristically, the necessary SNR can be determined by inspecting the quality of the output concentration maps. With sufficient SNR, maps of different chemical species should reflect the distinct morphological structures of subcellular organelles that differ from the water background channel, such as lipid droplets in the fatty acid channel. Lastly, to capture all the possible spectral differences amidst broad spectral peaks, we measured the entire second overtone window permitted by the laser tuning range. This approach is not optimized, as the number of separable species is much fewer than the spectral frames and theoretically requires fewer spectral frames. In the future, we aim to perform recursive feature elimination to selectively measure important spectral bands that contribute most to the differentiation of species.

Biological tissues, including brain slices, are inherently turbid media, complicating 3D volumetric rendering via one-photon multiple scattering55,56. Given that the pump-probe scheme inherently constitutes a “two-photon” imaging process, OPT microscopy demonstrates superior sectioning capability with insensitivity to the scattering loss of either the pump or probe beam, which does not contribute to the actual OPT signal. This unique characteristic effectively mitigates background from one-photon scattering and underscores the promising potential of OPT microscopy for bond-selective imaging through inhomogeneous turbid matrices. Taking a step further, leveraging a probe beam with longer wavelengths will enhance the performance for deeper penetration in turbid species, while maintaining excellent sectioning capability.

The OPT microscope, based on an ultrafast near-infrared laser, can be easily adapted into a multimodal imaging platform. Various imaging techniques, such as two-photon fluorescence, transient absorption, and coherent Raman scattering, can all be readily implemented on this platform with a simple exchange of photodetectors and electronics for signal extraction. This creates a highly versatile integrated multifunctional imaging station suitable for material and biological research in a wide span. Another notable feature of OPT is its utilization of a frequency-doubled 520 nm as probe beam, allowing for improved sensitivity and spatial resolution in detecting temperature change. Additionally, the probe beam exhibits a low noise level (near shot-noise-limited) which is attributed to the quiet ultrafast beam outputs of our laser. By employing a second beam as the phototherma detector, the OPT microscope benefits from the fact that the detection noise is largely determined by the noise floor of the probe beam, thereby relaxing the criteria for the noise level of the excitation beams. Consequently, this characteristic opens up possibilities for incorporating different laser sources, even those with noisier outputs, into the OPT microscope, which may potentially facilitate multiple promising technical advancements such as cost reduction, expanding the spectral coverage range, and enhancing wavelength tuning speed.

Building upon the less stringent requirements for excitation lasers, various enhancements to the capabilities of OPT microscopy can be explored. Firstly, our proof-of-principle implementation of OPT microscopy focused on C-H bonds within a limited portion of SWIR range. Expanding the wavelength coverage by employing a broadband laser, such as a supercontinuum white light laser, would extend OPT into the $1 ^ { \mathsf { s t } }$ overtone region. This expansion would enable investigations targeting various functional groups and meanwhile offer a costeffective approach for OPT measurements. Such advancements would be particularly beneficial for pharmaceutical investigations. Addressing the imaging speed aspect, the current acquisition time for a 400 pixel × 400 pixel OPT image is \~3 s, while manual wavelength tuning takes around 5 s, significantly compromising the speed of hyperspectral imaging. Incorporating an automatic and fast wavelength tuning module would enhance the overall imaging speed, thus creating opportunities for dynamics studies of living cells.

Another prospective implementation for broadening the scope of OPT microscopy is the incorporation of epi detection. This will be particularly useful when dealing with the measurement of small nanoparticles with intense backscattering, as well as opaque samples like pharmaceutical tablets. Our future work aims to augment the existing transmission mode by introducing an add-on epi detection mode, thereby enabling a wider range of applications.

In summary, we have developed overtone photothermal (OPT) microscopy, a label-free bond-selective imaging approach that significantly improves the sensitivity and lateral resolution of current SWIR image modalities. OPT fills the gap between visible and midinfrared photothermal microscopy by enabling highly chemicalspecific mapping in aqueous environment. We demonstrated successful applications of OPT microscopy in mapping polymer nanostructures and performing depth-resolved spectroscopic imaging and metabolic profiling of intercellular and multicellular organisms at single-cell and tissue levels. OPT microscopy allows for the unambiguous identification of spatially dependent protein and lipid distributions. We anticipate that the integration of OPT microscopy with existing large-scale SWIR imaging techniques will facilitate the exploration of structural and chemical features across various imaging scales, providing valuable insights into both material science and the underlying mechanisms of complex biological systems.

## Methods

## OPT microscope

OPT microscopy employed an InSight DeepSee femtosecond laser (Spectra-Physics), which emits a tunable beam from 680 nm to 1300 nm and a fixed-wavelength beam of 1040 nm with a repetition rate of 80 MHz. The OPT experiments were conducted within the 1080 nm to 1280 nm range, corresponding to the 2nd overtone resonances of C-H stretching vibrations. The power of two laser outputs was adjusted using a combination of a half-wave plate and a polarization beam splitter. An acousto-optic modulator (AOM, M1205-P80L-0.5, Isomet) was utilized to modulate the excitation beam at desired repetition rates (100 kHz–1 MHz) and duty cycles (usually 50% for biological measurements). The SWIR beam then passed through five 15-cm SF57 glass rods for chirping purposes, with a chirped pulse duration of approximately 2 ps to minimize nonlinear damage. The 1040 nm output from the laser source was frequency-doubled using a lithium triborate (LBO) crystal (LBO-604H, Eksma Optics) to 520 nm and served as the probe beam. Similarly, the femtosecond 520 nm probe beam was chirped after passing through four 15-cm glass rods to reduce non-linear thermal damage.

To optimize the OPT signal, one lens pair on the probe beam path was used to adjust the beam convergence and divergence, controlling the axial displacement between the excitation beam and probe beam foci. The SWIR beam and 520 nm probe beam were combined using a 900 nm long-pass dichroic beam splitter (DMLP900, Thorlabs) and directed to 2D scanning Galvo mirrors. The samples were mounted on an upright microscope (BX51WI, Olympus), and the images were acquired through laser raster scanning.

During the OPT imaging, the average on-sample SWIR power remained below 50 mW, and the average on-sample power of 520 nm was below 20 mW. For tight focusing of the SWIR and probe beams, a 60X water immersion objective with a NA = 1.2 (UPlanApo/IR, Olympus) was utilized. The collection NA of the oil condenser was adjustable to optimize the OPT signal intensity. After passing through the condenser, the probe beam went through a lens and optical filters before being detected by a biased Si photodiode (DET100A2, Thorlabs). The electronic signal from the photodiode was transmitted through highand low-pass electrical filters, amplified by a 46 dB low-noise preamplifier (SA-230F5, NF Corporation), and then processed by a lock-in amplifier (HF2LI, Zurich Instruments). The demodulated signals from the lock-in amplifier were registered as OPT signals and synchronized with each laser scanning step to generate OPT images. Spectroscopic information was extracted from hyperspectral image stacks acquired by manually tuning SWIR wavelengths and recording OPT images.

## Spectral unmixing with chemical sparsity constraint via pixel-wise LASSO

The task of spectral unmixing is to decompose the high-dimensiona hyperspectral image into the multiplication of two lower-dimensional matrices, namely reference spectra of pure chemicals and concentrations, to facilitate comprehension of the chemical information buried within the raw images. Mathematically, we define the spatial dimensions and the spectral dimension as $N _ { x } , N _ { y }$ and $N _ { \lambda }$ , and define the number of pure chemicals as $\kappa ,$ x ythe spectral unmixing problem can be formulated as follows:

$$
D = C S + E, \tag {1}
$$

where $\pmb { D } \in \mathbb { R } ^ { N _ { x } N _ { y } \times N _ { \lambda } }$ is a raster-ordered raw data matrix, $S \in \mathbb { R } ^ { K \times N _ { \lambda } }$ λ D Scontains the reference spectra of all pure chemicals, R × $\dot { \boldsymbol { C } } \in \mathbb { R } ^ { N _ { x } N _ { y } \times K }$ includes the concentrations for all the components and $\boldsymbol { E } \in \mathbb { R } ^ { N _ { x } N _ { y } \times N _ { \lambda } }$ Eis the residual term containing the fitting error and measurement noise. Given reference spectra of pure chemicals, the task of spectra unmixing is simplified to finding the concentrations at each spatial position. We introduce a L1-norm local chemical sparsity constraint to the concentration vector at each pixel, to encourage that at each position, only few components have dominant contributions. The solution is found by solving for the following LASSO problem in a pixelwise manner:

$$
\hat {C} _ {i} = \arg \min _ {C _ {i}} \left\{\frac {1}{2} \| D (i,:) - C _ {i} S \| ^ {2} + \beta \| C _ {i} \| _ {1} \right\}, \tag {2}
$$

where represents the pixel number, $\hat { \boldsymbol C } _ { i } \in \mathbb { R } ^ { K }$ is the concentration i Civector for all components at pixel , and β controls the level of sparsity iat each pixel to ensure suppression of channel cross talks while avoiding over-suppression that leads to all zeros. The value of β is fixed across all images to ensure output values can be quantitatively compared.

In the demonstrated spectral unmixing of biological specimens in water environment, OPT spectra of bovine serum albumin (BSA, purity ≥96%, Sigma-Aldrich), triglyceride (TAG, purity ≥97%, Sigma-Aldrich), and deionized water were collected, serving as the pure spectral references for protein, fatty acids, and water, respectively.

## Collection of NIR absorption spectra via UV-Vis-NIR spectrophotometer

Standard NIR absorption spectra for both polystyrene and ethylene glycol were acquired utilizing the Cary 5000 UV-Vis-NIR Spectrophotometer (Agilent) following established protocols. Polystyrene $( \mathbf { M } _ { \mathbf { w } } = 3 5 , 0 0 0 ,$ , Sigma-Aldrich) was dissolved in toluene, and 3 mL of the resulting solution was transferred into a quartz cuvette for insertion into the spectrophotometer. An absorption spectrum of toluene was acquired and subsequently utilized for baseline correction. Similarly, 3 mL ethylene glycol (purity 99.8%, Sigma-Aldrich) was introduced into a separate quartz cuvette, with ambient air as the reference baseline. The measurement parameters include a spectral bandwidth of 2 nm, an integration time of 0.1 s, and a wavelength interval of 1 nm.

## Preparation of phase separation patterns of PS and PMMA blends

To prepare the polymer stock solution, 51.4 mg PS $( M _ { \mathrm { w } } = 3 5 , 0 0 0 ,$ Sigma-Aldrich) and 15.4 mg PMMA $( M _ { \mathrm { w } } = 3 5 , 0 0 0$ M, Sigma-Aldrich) were Mdissolved in 2 mL toluene and allowed to settle. To observe the phase separation pattern of PS-PMMA blends, a coverslip substrate with a thickness of $1 3 0 \mu \mathrm { m }$ was cleaned with acetone and isopropanol, followed by drying using nitrogen gas. A 40 µL mixture solution was spincoated onto the coverslip substrate using a spinner (Headway Research, CB-15 & PWM32) at 500 revolutions per minute (rpm) for 10 seconds, followed by 1000 rpm for 50 seconds.

## Fabrication of PMMA striped structures

The fabrication of PMMA stripes was achieved using electron-beam lithography (EBL) on a 130 µm thick coverslip substrate. Prior to fab rication, the substrate underwent a thorough cleaning process involving acetone and isopropanol, nitrogen drying, and baking at $1 1 0 ^ { \circ } \mathrm { C } .$ . A 950-PMMA 6% in anisole solution was spin-coated onto the substrate to achieve a PMMA thickness of 600 nm as per the recipe used. The sample was subjected to a hard bake at $1 8 0 ^ { \circ } \mathrm { C }$ before a conduction layer of Au nanoparticles was sputtered onto the top surface. EBL was performed at 30 keV after a dose test to pattern the sample. The fabrication process was completed by soaking the PMMA in a solution of methyl isobutyl ketone/isopropanol (MIBK/IPA) 1:3 for 70 s, followed by rinsing with IPA and a wet etch to remove the sputtered Au.

## OVCAR-5 cancer cells

The OVCAR-5 cells used in this experiment were a generous gift from Dr. Daniela Matei of Northwestern University. The cells were cultured in RPMI 1640 media (Gibco) supplemented with 10% fetal bovine serum (Gibco), 2 mM L-Glutamine, and 1% penicillin-streptomycin. The cell line was incubated at 37 °C with 5% ${ \mathrm { C O } } _ { 2 } .$ For imaging purposes, the cells were seeded at a density of 0.2 million per dish on glass-bottom dishes and fixed in 10% neutral buffered formalin (Sigma-Aldrich) after 24 h of culturing. Prior to imaging, the cells were washed three times with either $\mathsf { H } _ { 2 } \mathbf { O }$ PBS or $\mathsf { D } _ { 2 } \mathbf { O }$ PBS. OPT images were obtained by directly immersing the objective into the medium in the glass-bottom dish.

## preparation

C. elegans N2 wild-type isolates were purchased from the Cae-C. elegansnorhabditis Genetics Center (CGC). The worms were maintained in a $2 0 ^ { \circ } \mathrm { C }$ incubator and propagated on Nematode Growth Medium (NGM) agar plates supplemented with the auxotrophic mutant Escherichia colistrain OP50. To immobilize worms for imaging, worms were harvested and washed using phosphate-buffered saline (PBS) solution (Gibco) and then fixed by 10% neutral buffered formalin solution (Sigma-

Aldrich). The worms were washed using $\mathsf { D } _ { 2 } \mathbf { O }$ PBS or ${ \sf H } _ { 2 } { \sf O }$ PBS C. elegansthree times and then carefully sandwiched between two cover glasses for imaging. Throughout the measurement process, PBS media was gently added along the edge of the top coverslip to maintain hydration.

## Mouse brain tissue preparation

The brain tissue utilized in this work was from an adult C57BL/6 J mouse. The mouse was sacrificed and subsequently perfused with PBS solution (1X, Thermo Fisher Scientific). The brain was carefully extracted and immersed in 10% formalin solution for a fixation period of 48 hours. Following fixation, an oscillating tissue slicer (OTS-4500, Electron Microscopy Sciences) was employed to section the brain into 200-µm-thick coronal slices. The brain slices were washed three times with PBS solution before measurement. For OPT imaging, the brain tissue was submerged in PBS and sandwiched between two cover glasses, while for mid-IR imaging, it was positioned between a coverslip and a ${ \mathrm { C a f } } _ { 2 }$ substate.

## MIP imaging of brain slices

A tunable quantum-cascade laser (QCL, MIRcat-2400, Daylight Solutions) was utilized to effectively excite the vibrational modes within the sample. Simultaneously, a continuous-wave laser of 532 nm (Samba 532 nm, Cobolt) was used to probe the local thermal changes. The mid-IR beam operated at a repetition rate of 200 kHz, with a pulse width of 500 ns. The average mid-IR power applied to the sample was approximately 3 mW, while the probe power was set at 45 mW. The two beams were collinearly focused onto the sample plane through a reflective objective, and an objective Z-piezo stage controlled the axial position to acquire multi-depth images. The forward propagating probe photons were detected by a biased photodiode (DET100A2, Thorlabs). The photocurrent generated by the photodiode underwent amplification through a low-noise amplifier (SA-251F6, NF Corporation) and was subsequently directed to a lock-in amplifier (HF2LI, Zurich Instruments) for signal demodulation. A multichannel data acquisition card registers the data for real-time signal processing.

## Data availability

All data supporting the findings of this study are available within the main article and the Supplementary Information file. The raw data are available from the corresponding author upon request.

## Code availability

MATLAB code for LASSO spectral unmixing is available on the fol lowing website: https://github.com/buchenglab.

## References

1. Hale, G. M. & Querry, M. R. Optical constants of water in the 200-nm to 200-μm wavelength region. Appl. Opt. 12, 555–563 (1973).  
2. Shi, L., Sordillo, L. A., Rodríguez‐Contreras, A. & Alfano, R. Transmission in near‐infrared optical windows for deep brain imaging. J. Biophotonics 9, 38–43 (2016).  
3. Horton, N. G. et al. In vivo three-photon microscopy of subcortical structures within an intact mouse brain. Nat. Photonics 7, 205–209 (2013).  
4. Padalkar, M. & Pleshko, N. Wavelength-dependent penetration depth of near infrared radiation into cartilage. Analyst 140, 2093–2100 (2015).  
5. Lammertyn, J., Peirs, A., De Baerdemaeker, J. & Nicolaı, B. Light penetration properties of NIR radiation in fruit with respect to nondestructive quality assessment. Postharvest Biol. Technol. 18, 121–132 (2000).  
6. Wilson, R. H., Nadeau, K. P., Jaworski, F. B., Tromberg, B. J. & Durkin, A. J. Review of short-wave infrared spectroscopy and imaging  
methods for biological tissue characterization. J. Biomed. Opt. 20, 030901–030901 (2015).  
7. Goetz, A. F., Vane, G., Solomon, J. E. & Rock, B. N. Imaging spectrometry for earth remote sensing. Science 228, 1147–1153 (1985).  
8. Manley, M. Near-infrared spectroscopy and hyperspectral imaging: non-destructive analysis of biological materials. Chem. Soc. Rev. 43, 8200–8214 (2014).  
9. Boldrini, B., Kessler, W., Rebner, K. & Kessler, R. W. Hyperspectral imaging: a review of best practice, performance and pitfalls for inline and on-line applications. J. Infrared Spectrosc. 20, 483–508 (2012).  
10. Peterson, H. M. et al. In vivo, noninvasive functional measurements of bone sarcoma using diffuse optical spectroscopic imaging. J. Biomed. Opt. 22, 121612–121612 (2017).  
11. Tank, A. et al. Diffuse optical spectroscopic imaging reveals distinct early breast tumor hemodynamic responses to metronomic and maximum tolerated dose regimens. Breast Cancer Res. 22, 1–10 (2020).  
12. Zhao, Y. et al. Shortwave-infrared meso-patterned imaging enables label-free mapping of tissue water and lipid content. Nat. Commun. 11, 5355 (2020).  
13. Zhang, H. F., Maslov, K., Stoica, G. & Wang, L. V. Functional photoacoustic microscopy for high-resolution and noninvasive in vivo imaging. Nat. Biotechnol. 24, 848–851 (2006).  
14. Wang, H.-W. et al. Label-free bond-selective imaging by listening to vibrationally excited molecules. Phys. Rev. Lett. 106, 238106 (2011).  
15. Yeh, K. et al. Infrared spectroscopic laser scanning confocal microscopy for whole-slide chemical imaging. Nat. Commun. 14, 5215 (2023).  
16. Mittal, S. et al. Simultaneous cancer and tumor microenvironment subtyping using confocal infrared microscopy for all-digital molecular histopathology. Proc. Natl. Acad. Sci. 115, E5651–E5660 (2018).  
17. Shi, J. et al. Hybrid optical parametrically-oscillating emitter at 1930 nm for volumetric photoacoustic imaging of water content. eLight 2, 6 (2022).  
18. Yao, J. & Wang, L. V. Photoacoustic microscopy. Laser Photonics Rev. , 758–778 (2013).  
19. Uchiyama, K., Hibara, A., Kimura, H., Sawada, T. & Kitamori, T. Thermal lens microscope. Jpn. J. Appl. Phys. 39, 5316 (2000).  
20. Zong, H. et al. Background-suppressed high-throughput midinfrared photothermal microscopy via pupil engineering. ACS Photonics 8, 3323–3336 (2021).  
21. Li, Z., Aleshire, K., Kuno, M. & Hartland, G. V. Super-resolution farfield infrared imaging by photothermal heterodyne imaging. J. Phys. Chem. B 121, 8838–8846 (2017).  
22. Pavlovetc, I. M. et al. Infrared photothermal heterodyne imaging: contrast mechanism and detection limits. J. Appl. Phys. 127, 165101 (2020).  
23. Dabov, K., Foi, A., Katkovnik, V. & Egiazarian, K. Image denoising by sparse 3-D transform-domain collaborative filtering. IEEE Trans. Image Process. 16, 2080–2095 (2007).  
24. Harris, J. & Dovichi, N. Thermal lens calorimetry. Anal. Chem. 52, 695A–706A (1980).  
25. Adhikari, S. et al. Photothermal microscopy: imaging the optical absorption of single nanoparticles and single molecules. ACS Nano 14, 16414–16445 (2020).  
26. Zhang, D. et al. Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2, e1600521 (2016).  
27. Selmke, M., Braun, M. & Cichos, F. Photothermal single-particle microscopy: detection of a nanolens. Acs Nano 6, 2741–2749 (2012).  
28. Yim, K.-H. et al. Phase-separated thin film structures for efficient polymer blend light-emitting diodes. Nano Lett. 10, 385–392 (2010).  
29. Chiu, M. Y., Jeng, U. S., Su, C. H., Liang, K. S. & Wei, K. H. Simultaneous use of small‐and wide‐angle X‐ray techniques to analyze  
nanometerscale phase separation in polymer heterojunction solar cells. Adv. Mater. 20, 2573–2578 (2008).  
30. Mrđenović, D. A. et al. Visualizing surface phase separation in PS PMMA polymer blends at the nanoscale. ACS Appl. Mater. Interfaces 14, 24938–24945 (2022).  
31. Menendez, J. A. & Lupu, R. Fatty acid synthase and the lipogenic phenotype in cancer pathogenesis. Nat. Rev. Cancer 7, 763–777 (2007).  
32. Wu, X., Daniels, G., Lee, P. & Monaco, M. E. Lipid metabolism in prostate cancer. Am. J. Clin. Exp. Urol. 2, 111 (2014).  
33. Tibshirani, R. Tibshirani, R. Regression shrinkage and selection via the lasso. J. R. Statist. Soc. B 58, 267–288 (1996).  
34. Lin, H. et al. Microsecond fingerprint stimulated Raman spectroscopic imaging by ultrafast tuning and spatial-spectral learning. Nat. Commun. 12, 3052 (2021).  
35. Cao, Q., Zhegalova, N. G., Wang, S. T., Akers, W. J. & Berezin, M. Y. Multispectral imaging in the extended near-infrared window based on endogenous chromophores. J. Biomed. Opt. 18, 101318–101318 (2013).  
36. Wang, Y. et al. Measurement of absorption spectrum of deuterium oxide (D2O) and its application to signal enhancement in multiphoton microscopy at the 1700-nm window. Appl. Phys. Lett. 108, 021112 (2016).  
37. Chen, X., Barclay, J. W., Burgoyne, R. D., Morgan, A. & Using, C. elegans to discover therapeutic compounds for ageing-associated neurodegenerative diseases. Chem. Cent. J. 9, 1–20 (2015).  
38. Mullaney, B. C. & Ashrafi, K. C. elegans fat storage and metabolic regulation. Biochim. Biophys. Acta-Mol. Cell Biol. Lipids 1791, 474–478 (2009).  
39. Richards, L. J., Plachez, C. & Ren, T. Mechanisms regulating the development of the corpus callosum and its agenesis in mouse and human. Clin. Genet. 66, 276–289 (2004).  
40. Ji, M. et al. Rapid, label-free detection of brain tumors with stimulated Raman scattering microscopy. Sci. Transl. Med. 5, 201ra119–201ra119 (2013).  
41. Le, S. Q. et al. Myelin and lipid composition of the corpus callosum in mucopolysaccharidosis type I mice. Lipids 55, 627–637 (2020).  
42. Fleming, C. P., Eckert, J., Halpern, E. F., Gardecki, J. A. & Tearney, G. J. Depth resolved detection of lipid using spectroscopic optical coherence tomography. Biomed. Opt. Express 4, 1269–1284 (2013).  
43. Gaiduk, A., Yorulmaz, M., Ruijgrok, P. & Orrit, M. Room-temperature detection of a single molecule’s absorption by photothermal contrast. Science 330, 353–356 (2010).  
44. Berciaud, S., Cognet, L., Blab, G. A. & Lounis, B. Photothermal heterodyne imaging of individual nonfluorescent nanoclusters and nanocrystals. Phys. Rev. Lett. 93, 257402 (2004).  
45. Bai, Y., Yin, J. & Cheng, J.-X. Bond-selective imaging by optically sensing the mid-infrared photothermal effect. Sci. Adv. 7, eabg1559 (2021).  
46. Xia, Q., Yin, J., Guo, Z. & Cheng, J.-X. Mid-infrared photothermal microscopy: principle, instrumentation, and applications. J. Phys. Chem. B 126, 8597–8613 (2022).  
47. Aleshire, K. et al. Far-field midinfrared superresolution imaging and spectroscopy of single high aspect ratio gold nanowires. Proc. Natl Acad. Sci. 117, 2288–2293 (2020).  
48. Chatterjee, R., Pavlovetc, I. M., Aleshire, K., Hartland, G. V. & Kuno, M. Subdiffraction infrared imaging of mixed cation perovskites: Probing local cation heterogeneities. ACS Energy Lett. 3, 469–475 (2018).  
49. Xu, J., Li, X., Guo, Z., Huang, W. E. & Cheng, J.-X. Fingerprinting bacterial metabolic response to erythromycin by Raman-integrated mid-infrared photothermal microscopy. Anal. Chem. 92, 14459–14465 (2020).  
50. Lima, C., Muhamadali, H., Xu, Y., Kansiz, M. & Goodacre, R. Imaging isotopically labeled bacteria at the single-cell level using high-  
resolution optical infrared photothermal spectroscopy. Anal. Chem. 93, 3082–3088 (2021).  
51. Guo, Z., Bai, Y., Zhang, M., Lan, L. & Cheng, J.-X. High-throughput antimicrobial susceptibility testing of Escherichia coli by wide-field mid-infrared photothermal imaging of protein synthesis. Anal. Chem. 95, 2238–2244 (2023).  
52. Lim, J. M. et al. Cytoplasmic protein imaging with mid-infrared photothermal microscopy: cellular dynamics of live neurons and oligodendrocytes. J. Phys. Chem. Lett. 10, 2857–2861 (2019).  
53. Klementieva, O. et al. Super‐resolution infrared imaging of polymorphic amyloid aggregates directly in neurons. Adv. Sci. 7, 1903004 (2020).  
54. He, H. et al. Mapping enzyme activity in living systems by real-time mid-infrared photothermal imaging of nitrile chameleons. Nat. Methods 21, 342–352 (2024).  
55. Katz, O., Small, E. & Silberberg, Y. Looking around corners and through thin turbid layers in real time with scattered incoherent light. Nat. Photonics 6, 549–553 (2012).  
56. Schmitt, J., Knüttel, A. & Yadlowsky, M. Confocal microscopy in turbid media. JOSA A 11, 2226–2235 (1994).

## Acknowledgements

This work was supported by NIH grants R35GM136223, R33CA261726, R01EB032391, and R01EB035429 to J.X.C.

## Author contributions

J.X.C. generated the idea and guided the overall research; L.W. built the imaging flatform, performed OPT data collection, and analyzed all data; H.L. conceived the idea of introducing SHG probe beam and developed pixel-wise LASSO spectral unmixing algorithm; Y.Z. and X.G. conducted the initial explorations of 3rd overtone absorption; M.L. prepared brain slices and collected mid-infrared photothermal images; J.L. fabricated the PMMA striped nanostructures; F.C. provided the OVCAR-5 cancer cells; M.Z. provided the C. elegans worms. L.W. prepared the manuscript with input from the authors.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-024-49691-2.

Correspondence and requests for materials should be addressed to Ji-Xin Cheng.

Peer review information Nature Communications thanks Mikhail Berezin, Garth Simpson and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at

http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jur isdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org licenses/by/4.0/.

© The Author(s) 2024