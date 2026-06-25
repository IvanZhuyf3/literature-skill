ARTICLE

Received 22 Aug 2016 | Accepted 2 Mar 2017 | Published 24 Apr 2017

DOI: 10.1038/ncomms15117

OPEN

# Volumetric chemical imaging by stimulated Raman projection microscopy and tomography

Xueli Chen1,2,\*, Chi Zhang2,\*, Peng Lin2, Kai-Chih Huang2, Jimin Liang1 , Jie Tian1,3 & Ji-Xin Cheng2,4

Volumetric imaging allows global understanding of three-dimensional (3D) complex systems. Light-sheet fluorescence microscopy and optical projection tomography have been reported to image 3D volumes with high resolutions and at high speeds. Such methods, however, usually rely on fluorescent labels for chemical targeting, which could perturb the biological functionality in living systems. We demonstrate Bessel-beam-based stimulated Raman projection (SRP) microscopy and tomography for label-free volumetric chemical imaging. Our SRP microscope enables fast quantitation of chemicals in a 3D volume through a two dimensional lateral scan. Furthermore, combining SRP and sample rotation, we demonstrate the SRP tomography that can reconstruct the 3D distribution of chemical compositions with optical spatial resolution at a higher speed than the Gaussian-beam-based stimulated Raman scattering sectioning imaging can. We explore the potential of our SRP technology by mapping polymer particles in 3D volumes and lipid droplets in adipose cells.

olumetric imaging enables quantitative and global measurements of a three-dimensional (3D) complex system. It allowed quantitation of molecules in the whole volume of a specimen, and has proven to be invaluable in the studies of cell metabolism, brain function, and developmental biology1–4. The simplest way to image a volume is through optical sectioning in the axial direction. In such a scheme, the laser scans in the lateral plane to collect a two-dimensional (2D) image, and then the laser focus moves along the axial direction to acquire an image stack for 3D reconstruction. Such a method requires tightly focused laser beams and good axial sectioning capability. Confocal or multiphoton fluorescence microscopy can section a volume with good axial resolution5,6. Coherent Raman scattering microscopy, having a similar sectioning ability, can map the chemical compositions in a volume based on molecular vibrations7,8. Such a sectioning approach, however, can be time-consuming for a volume hundreds of micrometres across9.

Light-sheet microscopy overcame this limitation by scanning an axially elongated laser beam to cover the completely 3D volume in a single 2D lateral scan. For example, the light-sheet fluorescence microscopy has achieved high-resolution and high-speed volumetric imaging of biological samples ranging from single cells to whole embryos10,11. Despite its wide applications12–15, the fluorescent labels used in light-sheet fluorescence microscopy might cause strong perturbation to biological functionalities in living systems, especially when labelling small metabolic molecules. Fluorescent labels can also induce other issues, such as non-specific targeting and photobleaching16. Light-sheet Raman microscopy has been reported to enable label-free volumetric imaging of chemicals in a volume17–21. However, the spontaneous Raman scattering suffers from low signal level and strong autofluorescence background, especially in living samples19. Furthermore, the image quality in the light-sheet microscopy often degenerates as the distance from the sample surface to the objective increases22.

Another approach for volumetric imaging is through tomo graphy, in which images were collected from many different angles around the sample. The 3D information can be then reconstructed using the angle-dependent images. Tomography can overcome the depth-induced deterioration on image quality in light-sheet techniques22. On the basis of the light transmission or emission, optical projection tomography (OPT) can produce isotropic, high-resolution image of a specimen in 3D (refs 2,9,23,24). Nonetheless, the transmission OPT does not have chemical contrast, whereas the fluorescence emission OPT subjects to the same issues in fluorescence microscopy for the quantification of metabolic molecules in living samples. Spontaneous Raman tomography was reported to image the chemical compositions of specimens in 3D (refs 25–27), yet it has low image acquisition speed due to the inherently low signal level of spontaneous Raman scattering. Furthermore, the spontaneous Raman tomography is based on the collection of diffused photons, leaving the technique with low spatial resolution, usually on the scale of millimetres. Such a low spatial resolution was caused by the physical nature of the diffuse light propagation in turbid medium28,29.

Here we demonstrate the first Bessel-beam-based stimulated Raman projection (SRP) microscopy and tomography for high-speed volumetric chemical imaging. Our SRP method is built upon the concept that the detected signal is an integration of Stimulated Raman Scattering (SRS) intensity along the Rayleigh length of the input Bessel beams, which remain their focuses along axial direction for a long distance. Compared to the Gaussian beam SRS microscopy, the Bessel beam SRP microscopy is able to quantify the total chemical compositions of a 3D volume in a 2D lateral scan. By rotating the sample, the 3D chemical distribution inside the sample volume can be reconstructed by the SRP tomography with isotropic spatial resolution. We first theoretically simulate the generation of SRP signal using Bessel pump and Stokes beams. The experimental characterization results of the system show good agreement with our simulation results. Using polymer particles and single adipose cells, we further exemplify the potential of our SRP technology for in vivo volumetric chemical imaging of live samples. Our results collectively prove that the SRP microscopy and tomography allow fast quantitation of chemical compositions in a 3D volume.

## Results

Volumetric imaging based on stimulated Raman scattering. Conventionally, the SRS imaging relies on 2D lateral scanning of tightly focused Gaussian laser beams. To image through a 3D volume, either the laser focus or the sample needs to be swept along the axial direction at one image per step. The image stack obtained from such a scheme can be used to reconstruct the 3D volume, as shown in Fig. 1a. To quantify the total chemical compositions in the volume, such a sectioning imaging scheme can be time-consuming, especially for a large volume that requires many image slices to reconstruct. Bessel beam can remain tightly focused for a long distance. Using Bessel beams for excitation, the SRS signal can be integrated along the axial direction of the sample. Scanning the Bessel excitation beams two-dimensionally on the lateral plane can therefore generate a projection image containing the total amount of chemical compositions in a volume. Such an imaging modality, termed SRP microscopy in this paper, is illustrated in Fig. 1b. Though SRP microscopy allows for high-speed quantitation of total chemical compositions in a volume, it loses axial resolution. To reconstruct the distribution of chemical compartments in a 3D volume, we further developed SRP tomography by collecting a series of SRP images while rotating the sample, and reconstructing the 3D structure through image reconstruction algorithms, as illustrated in Fig. 1c.

Theory of SRS signal generation by Bessel beams. Assuming collinearly overlapped pump and Stokes beams, the SRS intensity from a very thin slab centred at position z with a thickness Dz can be expressed as ref. 30

$$
I _ {\mathrm{SRS}} = C _ {0} \mathrm{Im} \left(\chi^ {(3)}\right) I _ {\mathrm{p}} (\mathbf {z}) I _ {\mathrm{S}} (\mathbf {z}) \Delta z, \tag {1}
$$

where $C _ { 0 }$ is a constant, Im $( \chi ^ { ( 3 ) } )$ is the imaginary part of the third-order nonlinear susceptibility $\chi ^ { ( 3 ) } { } _ { ; }$ , and $I _ { \mathrm { p } } ( \mathbf { z } )$ and $I _ { \mathrm { S } } ( \mathbf { z } )$ are the intensities of the pump and Stokes beams at z, respectively.

Several methods were reported to generate a Bessel beam31–33. Here we used two axicons and an objective lens to convert a Gaussian beam into a Bessel beam (Fig. 1d). In our implementation, a Gaussian beam was first converted to a ring-shaped beam by the axicon pair and then to a Bessel beam via the objective lens. The intensity distribution of the Bessel beam can be modelled as

$$
I _ {\mathrm{B}} (\mathbf {r}, \mathbf {z}) = I _ {0} \frac {w _ {0} ^ {2}}{w ^ {2} (\mathbf {z})} \mathrm{e} ^ {- \frac {2 r _ {\mathrm{c}} ^ {2}}{w ^ {2} (\mathbf {z})}} \left(\frac {2 \pi r _ {\mathrm{c}} \Delta d}{\lambda f}\right) ^ {2} J _ {0} ^ {2} \left(\frac {2 \pi r _ {\mathrm{c}}}{\lambda f} \mathbf {r}\right). \tag {2}
$$

Here (r, z) are, respectively, the coordinates in the lateral and longitudinal directions, $I _ { 0 }$ is the intensity at the centre of the incident Gaussian beam with a half width $w _ { 0 } ,$ $w ( \mathbf { z } ) = w _ { 0 } \sqrt { 1 + ( \mathbf { z } / z _ { \mathrm { B } } ) ^ { 2 } }$ , $z _ { \mathrm { B } }$ is the equivalent Rayleigh length of the Bessel beam, $r _ { \mathrm { c } }$ is the radius of the ring-shaped beam, Dd is the width of the ring, l is the wavelength and f is the focal length of the objective lens.

a  
![](images/064f9de7cbfd1cc5afd7458a163842f08d12fbd6018a116640429802f4682491.jpg)

<details>
<summary>text_image</summary>

Condenser
Objective
</details>

b  
![](images/270f31663f6f88038653e14097e5f19a0406e9c4e9db189b5ee7aa083dd71fca.jpg)

<details>
<summary>text_image</summary>

Condenser
Objective
</details>

c  
![](images/2bc57dea240d88fe4f111cb284ba6406bc5842bbefaa9bbdb94480705aa01b2c.jpg)

<details>
<summary>text_image</summary>

Condenser
180°
Objective
</details>

d  
![](images/df9c42d6da8c11bed39bfd3680698521e13203d01a49d13f2590105b231e3904.jpg)

<details>
<summary>text_image</summary>

Gaussian
beam
input
Axicon
Ring-shaped
beam
Axicon
Beam size
reduction
Objective
Bessel beam
</details>

Figure 1 | Volumetric imaging modalities based on stimulated Raman scattering. (a) Sectional imaging by the conventional Gaussian beam stimulated Raman scattering microscopy. (b) Stimulated Raman projection (SRP) microscopic imaging based on Bessel beams. (c) SRP tomographic imaging based on Bessel beams. (d) The generation of a Bessel beam using a pair of axicons and an objective lens

By expressing the pump and Stokes beams using the Bessel beam expression in equation (2), we obtain the distribution of SRS intensity

$$
I _ {\mathrm{bSRS}} (\mathbf {r}, \mathbf {z}) = C _ {\mathrm{B}} \operatorname{Im} \left(\chi^ {(3)}\right) \left(\frac {r _ {\mathrm{c}}}{f}\right) ^ {4} J _ {0} ^ {2} \left(\beta_ {\mathrm{P}} \mathbf {r}\right) J _ {0} ^ {2} \left(\beta_ {\mathrm{S}} \mathbf {r}\right) P _ {\mathrm{P}} (\mathbf {z}) P _ {\mathrm{S}} (\mathbf {z}) \Delta z, \tag {3}
$$

where $C _ { \mathrm { B } } , \ \beta _ { \mathrm { p } }$ and $\beta _ { \mathrm { { S } } }$ are constants, $P _ { \mathrm { p } } ( \mathbf { z } )$ and $P _ { \mathrm { S } } ( \mathbf { z } )$ are the powers of the pump and Stokes beams, respectively, $J _ { 0 } ( \bullet )$ is the zeroth-order Bessel function.

For a thick sample, the SRP signal intensity is defined as the integration of $I _ { \mathrm { b S R S } } ( \mathbf { r } , \mathbf { z } )$ over the sample thickness L

$$
I _ {\mathrm{bSRP}} (\mathbf {r}, L) = C _ {\mathrm{B}} \operatorname{Im} \left(\chi^ {(3)}\right) \left(\frac {r _ {\mathrm{c}}}{f}\right) ^ {4} J _ {0} ^ {2} \left(\beta_ {\mathrm{p}} \mathbf {r}\right) J _ {0} ^ {2} \left(\beta_ {\mathrm{S}} \mathbf {r}\right) \int_ {0} ^ {L} P _ {\mathrm{p}} (\mathbf {z}) P _ {\mathrm{S}} (\mathbf {z}) \mathrm{d} \mathbf {z}. \tag {4}
$$

The overall SRP signal is then

$$
P _ {\mathrm{bSRP}} (L) = Q \iint I _ {\mathrm{bSRP}} (\mathbf {r}, L) \mathrm{d} \mathbf {A}. \tag {5}
$$

Here A is the signal integration area and Q is the detection efficiency of the photodetector. The derivations of equations (1–5) are detailed in Supplementary Notes 1–3.

Simulation results of the SRP signal. On the basis of equations (2 and 3), we calculated the intensity distributions of the pump, Stokes and SRS fields. $\mathrm { ~  ~ { ~ A ~ } ~ } \times 1 0$ objective having a numerical aperture (NA) of 0.3 was used in all calculations. As shown in Fig. 2a–d, our approach can generate laterally diffraction-limited Bessel beams for both pump and Stokes fields, which exhibit a high-intensity central lobe with a series of low-intensity rings. Such a beam profile can maintain a long distance in the direction of laser beam propagation. For example, the central lobe of the Stokes beam (at the wavelength of 1,040 nm) has a latera diameter of 4.02 mm (Supplementary Fig. 1a), and can maintain over 8.89 mm propagation distance with a full width at half maximum (FWHM) of 3.79 mm (Supplementary Fig. 1b). Although the rings of the pump and Stokes beams can partially overlap (Supplementary Fig. 2a), the laser intensity is much lower in the rings than in the central lobe. Thus, the nonlinear SRP signal generated by the partially overlapped rings can be neglected (Supplementary Fig. 2b). It is reasonable to assume that the SRP signal is only arisen from the overlapped central lobes of the Bessel beams (Fig. 2e,f).

Figure 2g,h shows the SRP signal level as a function of the thickness of the sample placed in the centre of the focus, calculated using equation (5). We found a linear dependence of SRP signal on the sample thickness within 2.2 mm. If the sample thickness exceeds 2.2 mm, such linearity failed. This is because 2.2 mm is the longitudinal FWHM of the SRP signal. The power of the Bessel beam is equally distributed on the central lobe and the rings. Therefore, the energy density at the Bessel beam focus is often much lower than that of the Gaussian beam with the same overall input power. Consequently, the SRP signal generated by the Bessel beams can be much lower than the SRS signal generated by the Gaussian beams, especially when the sample is thin (Fig. 2g). For a thick sample, the signal from SRP can be comparable or even larger than the SRS signal generated by the Gaussian beams, due to the long signal integration length. If we assume that the power on the central lobe of the Bessel beam equals the power at the Gaussian focus, the SRP signal generated by the Bessel beams is always larger than the SRS signal from the Gaussian beams (Fig. 2h),

We further calculated the dependence of the SRP signal on the laser power, which showed a positive linear growth, as seen in the Supplementary Fig. 3. We also investigated the influence of the objective NA and magnification on the Rayleigh length of the Bessel beam, the size of the central lobe, the overall SRP signal and the longitudinal FWHM of the SRP signal. As shown in the

a  
![](images/860cbaf418097dc1d648171144d4662efc256f357f7661ad7527c1bcb8055fd6.jpg)

b  
![](images/a24e8aed339da2dbf7b22fa4f50d4895fcfe055444c73d46f744c5abcdc23f14.jpg)

<details>
<summary>line chart</summary>

| z (mm) | Intensity (W m⁻²) |
| ------ | ----------------- |
| 0      | 0                 |
| 2      | 0                 |
| 4      | 0                 |
| 6      | 0                 |
| 8      | 0                 |
| 10     | 0                 |
| 12     | 0                 |
| 14     | 0                 |
| 16     | 0                 |
| 18     | 0                 |
</details>

c  
![](images/b4b1dd2039cf34cca0a7dd8c2bf4b4518dcaedbc8adf3b08dda37b7974ef9f6f.jpg)

d  
![](images/2ee5461f02865215bc6919547b2fe2216782d0df1f3e70a48d47c2fd8a817897.jpg)

<details>
<summary>line chart</summary>

| z (mm) | x (μm)     |
| ------ | ---------- |
| 0      | 0          |
| 2      | 0          |
| 4      | 0          |
| 6      | 0          |
| 8      | 0          |
| 10     | 0          |
| 12     | 0          |
| 14     | 0          |
| 16     | 0          |
| 18     | 0          |
</details>

e  
![](images/4e64c2fa11bf49523c604bc6b639dbd21f75d08590d9c9a7eddfad8f07c910f6.jpg)

f  
![](images/8415824ed0fde341938d7637b184e29e7bf70e22c27fdfe0eec03945f51f61ab.jpg)

<details>
<summary>heatmap</summary>

| z (mm) | x (μm) | Intensity (x10⁶ W m⁻²) |
| ------ | ------ | ---------------------- |
| 0      | -20    | 0                      |
| 2      | 0      | 8                      |
| 4      | 0      | 6                      |
| 6      | 0      | 4                      |
| 8      | 0      | 2                      |
| 10     | 0      | 2                      |
| 12     | 0      | 2                      |
| 14     | 0      | 2                      |
| 16     | 0      | 2                      |
| 18     | 0      | 2                      |
</details>

g  
![](images/1387bb6f78ff1f2e361a3aa49c0a1ad8c0481cba29a3d2e437f300e78d8751f8.jpg)

<details>
<summary>line chart</summary>

| Interaction length (mm) | Bessel     | Gaussian   |
| ----------------------- | ---------- | ---------- |
| 1e-4                    | 1e-11      | 1e-9       |
| 1e-3                    | 1e-10      | 1e-8       |
| 1e-2                    | 1e-9       | 1e-7       |
| 1e-1                    | 1e-8       | 1e-7       |
| 1e0                     | 1e-7       | 1e-7       |
| 1e1                     | 1e-6       | 1e-7       |
</details>

h  
![](images/b3c18de4d0da82995f6465fb887b58b918a3d3677dc81a28ec27e626a5e0f5c4.jpg)

<details>
<summary>line chart</summary>

| Interaction length (mm) | Bessel     | Gaussian   |
| ----------------------- | ---------- | ---------- |
| 1e-4                    | 1e-8       | 1e-9       |
| 1e-3                    | 1e-7       | 1e-8       |
| 1e-2                    | 1e-6       | 1e-7       |
| 1e-1                    | 1e-5       | 1e-7       |
| 1e0                     | 1e-4       | 1e-7       |
| 1e1                     | 1e-4       | 1e-7       |
</details>

Figure 2 | Numerical simulations of the Bessel beam intensity distributions and the stimulated Raman projection signal level. (a) The cross-sectiona and (b) the longitudinal distributions of the pump beam intensity at the wavelength of 800 nm. The colour bar is the same for a,b. (c) The cross-sectional and (d) the longitudinal distributions of the Stokes beam intensity at the wavelength of 1,040 nm. The colour bar is the same for c,d. (e) The cross-sectional and (f) the longitudinal distributions of the stimulated Raman scattering (SRS) signal intensity generated around $2 , 8 8 5 \mathsf { c m } ^ { - 1 }$ . The colour bar is the same for e,f. (g) The stimulated Raman projection (SRP) and the SRS signal level as a function of the sample thickness, assuming the same input laser powers for the Bessel and the Gaussian beams. (h) The SRP and the SRS signal level as a function of the sample thickness, assuming the same laser power at the Bessel beam central lobe and the total power of Gaussian beam. The red solid curves indicate the SRP signal generated by the Bessel pump and Stokes beams, and the blue dashed curves indicate the SRS signal generated by the Gaussian pump and Stokes beams.

Supplementary Fig. 4, a larger SRP signal can be achieved by using objectives with lower magnification and higher NA. Furthermore, for a specific NA, the SRP signal decreased with higher magnification. However, for a specific magnification, there was an optimal NA value to generate the maximum SRP signal for each sample thickness. In addition, we found that both the Rayleigh length of the Bessel beam (Supplementary Fig. 5a) and the longitudinal FWHM of the SRP signal (Supplementary Fig. 5b) decreased with a higher magnification (fix the NA value) or NA (fix the magnification value). For the Bessel beam SRP microscopy, the size of the central lobe determines the system resolution, which was independent on the magnification value (Supplementary Fig. 6a) but inversely dependent on the NA value (Supplementary Fig. 6b). Our simulation results can help select an optimal objective for specific SRP imaging applications.

The SRP microscope. A schematic of our SRP microscope is depicted in Fig. 3. Two synchronized beams were generated from a pulsed laser (InSight DeepSee, Spectral Physics) at 80 MHz repetition rate. One beam had a fixed wavelength at 1,040 nm and was used as the Stokes beam. The other beam had a tunable wavelength from 680 to 1,300 nm and was used as the pump beam. The Stokes beam was modulated at 2.5 MHz by an acousto-optic modulator (1205-C, Isomet). The pump beam was first delayed by a translational stage, and was then spatially and temporally combined with the Stokes beam by a dichroic mirror. Two axicons (AX2520-B, Thorlabs) were used to convert the overlapped Gaussian beams into ring-shaped beams. After reducing the beam size by a 4-f lens system, the ring-shaped beams were directed to a 2D galvo system (GVS012, Thorlabs) for laser scanning. After reflecting by the 2D galvo system and expanding by another 4-f lens system, the scanned ring-shaped beams were guided to an objective lens to generate Bessel beams.

The 4-f lens system was set up to create a conjugate plane of the galvo system at the entrance of the objective and to expand the ring-shaped beams to match the entrance pupil of the objective lens. After the sample, we used a  60 water immersion objective (UPlanSApo  60, NA ¼ 1.2, Olympus) to collect the transmitted Bessel beams. Such a high NA objective ensured a high signal collection efficiency to prevent image background from cross-phase modulation. The transmitted beams were first filtered by a pair of shortpass filters (ET980SP-2P, Chroma) to remove the Stokes beam composition and then directed to a large area silicon photodiode (S3994-01, Hamamatsu). The photocurrent generated in the photodiode was first amplified by a lab-built resonant amplifier, and was then sent to a lock-in amplifier (SRS844, Stanford Research Systems, or MFLI, Zurich Instruments) for further amplification and signal extraction.

![](images/69fe020b4dd452ee9368d6b5240697119b6334d95029360b177e10cde38c7bc2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Pump"] --> B["Stokes"]
  B --> C["L1"]
  C --> D["AOM"]
  D --> E["L2"]
  E --> F["M1"]
  F --> G["M2"]
  G --> H["M3"]
  H --> I["DM"]
  I --> J["Gaussian beam"]
  J --> K["Bessel beam"]
  K --> L["M5"]
  L --> M["A1"]
  M --> N["A2"]
  N --> O["L3"]
  O --> P["L4"]
  P --> Q["M8"]
  Q --> R["2D scanning mirror"]
  R --> S["L5"]
  S --> T["L6"]
  T --> U["M4"]
  U --> V["Objective"]
  V --> W["Sample"]
  W --> X["Condenser"]
  X --> Y["Filter"]
  Y --> Z["Pulsed laser"]
  Z --> AA["PBS HWP"]
  AA --> AB["PBS HWP"]
  AB --> AC["Pulse output"]
    style Z fill:#ffcccc,stroke:#333
```
</details>

Figure 3 | The experimental set-up of the stimulated Raman projection microscopic and tomographic imaging. A tunable pulsed laser provides two synchronized femtosecond pulse trains as pump and Stokes beams. The Stokes beam is modulated by an AOM. The pump beam is first delayed by a translational stage, and is then spatially and temporally combined with the Stokes beam by a DM. The collinearly overlapped beams are sent to a pair of axicons for generating ring-shaped beams. By adjusting the beam size, the ring-shaped beams are first directed to a 2D galvo system for laser scanning, and then guided to an objective for Bessel beams generation. After the sample, the transmitted Bessel beams are collected by a condenser, and then directed to the PD. A pair of shortpass filters are fixed in front of PD to remove the Stokes beam composition. The photocurrent generated in the PD is amplified by a lab-built resonant amplifier, and then sent to a lock-in amplifier for signal extraction. A, axicon; AOM, acousto-optic modulator; DM, dichroic mirror; HWP, half wave-plate; L, lens; M, mirror; PBS, polarizing beam splitter; PD, photodiode.

To facilitate the comparison between the Gaussian beam SRS microscope and the Bessel beam SRP microscope, we built an additional optical arm to allow the laser beams to bypass the axicons, as shown by the dashed lines in Fig. 3. By using flip mirrors, the system can quickly switch between the Bessel SRP and the Gaussian SRS schemes.

Performance of the SRP microscope. We first verified the simulation results of Bessel beams using $\textbf { a } \times 1 0$ objective with $\mathrm { N A } = 0 . 3$ . For the Stokes beam at the wavelength of 1,040 nm, the diameter of the central lobe and the axial FWHM of the longitudinal propagation were measured to be 4.13 mm and 3.34 mm, respectively (Supplementary Fig. 7). These values closely matched the calculations.

Next, we characterized the performance of the SRP microscope. To investigate the dependence of SRP signal on the sample thickness and the input laser powers, we prepared polydimethylsiloxane (PDMS) films with different thicknesses.

Figure 4a shows that the SRP signal increased linearly as the sample thickness increases within millimetre range $( R ^ { 2 } = { 0 . 9 9 7 7 } )$ . Furthermore, the SRP signal was linearly dependent on the powers of both the pump $( R ^ { 2 } = 0 . 9 9 9 8 )$ and the Stokes $\overset { \bullet } { ( } R ^ { 2 } = 0 . 9 9 8 0 )$ beams (Fig. 4b,c). The noise, on the other hand, was proportional to the square root of the pump power (Fig. 4d), indicating a laser shot-noise-limited signal detection.

We then evaluated the sensitivity of the SRP microscope by measuring the CH symmetric stretching at $2 , 9 1 5 \mathrm { c m } ^ { - 1 }$ from dimethyl sulfoxide (DMSO) diluted in deuterium oxide (D O). The sample thickness was 2 mm, smaller than the longitudinal FWHM of the Bessel beams generated by the  10 objective. The pump and Stokes powers on the central lobe of the Bessel beams were 0.7 and 30 mW, respectively. Figure 4e shows the measured signal-to-noise ratio as a function of DMSO concentration. These results indicated an estimated detection limit of 21.84 mM DMSO from single frequency SRP measurement. From the spectrum measurement, which can further improve the sensitivity of the system, we can clearly resolve the peak from 21.84 mM DMSO (Fig. 4f) and reach a detection limit of 1.8 mM DMSO. We also measured the C ¼ C Raman transition at $1 { , } 5 8 3 \thinspace \mathrm { c m } ^ { - 1 }$ from retinoic acid, which gave the detection limit as low as 100 mM (Supplementary Fig. 8). This result proved a micro-molar sensitivity of our SRP microscope in the Raman fingerprint region.

SRP microscopic imaging. To prove the capability of our SRP microscope in fast quantification of chemicals in a volume, we imaged polystyrene beads dispersed in a 3D matrix of agarose gel and compared the SRP images with SRS sectioning images obtained from the Gaussian scheme. From the Gaussian beam SRS images, only a portion of the beads can be seen in each sectional plane (Fig. 5a). To image all the beads in the 3D volume, a series of sectional images (50 images, 2 mm per step, as shown in Supplementary Movie 1) were acquired within 20 s. A superposition of the sectional images from selected depths is shown in Fig. 5b. In the SRP image acquired at the same location, all beads in the volume can be resolved by a single 2D lateral scan, finished in 2 s (Fig. 5c,d), an order of magnitude faster than the sectional imaging. Such a speed advantage would be magnified for imaging an even larger volume. We also imaged a mixture of polystyrene beads having 10 and 100 mm diameters (Supplementary Fig. 9).

![](images/f54400700566bab39a97f5e6a354c6b28a42d0613fd5e8a9312b52ea55d405ab.jpg)

<details>
<summary>line chart</summary>

| Sample thickness (mm) | SRP signal (a.u.) |
| --------------------- | ----------------- |
| 0.00                  | 12                |
| 0.26                  | 28                |
| 0.52                  | 44                |
| 0.78                  | 60                |
| 1.04                  | 76                |
</details>

![](images/233ef4cad5fed41a2569410c2cd24f106cc61e0070ade3151a1dcd2145fff4f8.jpg)

<details>
<summary>line chart</summary>

| Stokes power (mW) | SRP signal (a.u.) |
| ----------------- | ----------------- |
| 0                 | 50                |
| 20                | 100               |
| 40                | 150               |
| 60                | 200               |
| 80                | 250               |
| 100               | 300               |
| 120               | 350               |
| 140               | 400               |
| 160               | 450               |
| 180               | 500               |
| 200               | 550               |
| 220               | 600               |
| 240               | 650               |
| 260               | 700               |
| 280               | 750               |
| 300               | 800               |
| 320               | 850               |
| 340               | 900               |
| 360               | 950               |
| 380               | 1000              |
| 400               | 1050              |
| 420               | 1100              |
| 440               | 1150              |
| 460               | 1200              |
| 480               | 1250              |
| 500               | 1300              |
| 520               | 1350              |
| 540               | 1400              |
| 560               | 1450              |
| 580               | 1500              |
| 600               | 1550              |
| 620               | 1600              |
| 640               | 1650              |
| 660               | 1700              |
| 680               | 1750              |
| 700               | 1800              |
| 720               | 1850              |
| 740               | 1900              |
| 760               | 1950              |
| 780               | 2000              |
| 800               | 2050              |
| 820               | 2100              |
| 840               | 2150              |
| 860               | 2200              |
| 880               | 2250              |
| 900               | 2300              |
| 920               | 2350              |
| 940               | 2400              |
| 960               | 2450              |
| 980               | 2500              |
| 1000              | 2550              |
</details>

![](images/6fcd0d7fbec72bb6dec0d095d4639878d3f213a58e41447fbc23d15644ce6c98.jpg)

<details>
<summary>line chart</summary>

| Pump power (mW) | SRP signal (a.u.) |
| --------------- | ----------------- |
| 0.0             | 0                 |
| 1.5             | 25                |
| 3.0             | 50                |
| 4.5             | 75                |
| 6.0             | 100               |
| 7.5             | 125               |
| 9.0             | 150               |
</details>

![](images/dfe7d4803c89b0f7426fdcac90d53e40c86f29cbaa8ff3c650f08563cdc156ec.jpg)

<details>
<summary>line chart</summary>

| Pump power (mW) | Noise (a.u.) |
| --------------- | ------------ |
| 0.5             | 0.16         |
| 1.0             | 0.25         |
| 1.5             | 0.34         |
| 2.0             | 0.40         |
| 2.5             | 0.42         |
| 3.0             | 0.46         |
</details>

![](images/f9e0fe217a49010f185ab95d14064474378e047f08f8c9591d68a8a9e2ceeae1.jpg)

<details>
<summary>line chart</summary>

| Concentration of DMSO (mM) | SNR     |
| -------------------------- | ------- |
| 10                         | 0.5     |
| 20                         | 1.0     |
| 50                         | 3.0     |
| 100                        | 6.0     |
| 200                        | 12.0    |
| 500                        | 32.0    |
| 1000                       | 100.0   |
</details>

![](images/82e620c26b6c5afe151fe038d922a66b2d9232d71eb8d311805e1cc55417fd03.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity of DMSO (a.u.) |
| ------------------ | ------------------------ |
| 2,750              | 0.00                     |
| 2,800              | 0.005                    |
| 2,850              | 0.01                     |
| 2,900              | 0.05                     |
| 2,950              | 0.015                    |
| 3,000              | 0.01                     |
| 3,050              | 0.005                    |
| 3,100              | 0.005                    |
</details>

Figure 4 | Characterization of the stimulated Raman projection microscope. (a) The measured stimulated Raman projection (SRP) signal from PDMS films as a function of the sample thickness. The red line is the linear fitting curve for the measured data points $( R ^ { 2 } = 0 . 9 9 7 7 )$ . (b,c) The SRP signal of PDMS as a function of the Stokes power (b) and the pump power (c). The red lines are the linear fitting curves for the measured data points $( R ^ { 2 } = 0 . 9 9 8 0$ for the Stokes power and $R ^ { 2 } = 0 . 9 9 9 8$ for the pump power). (d) The SRP noise as a function of the pump power. The red curve is the fitting result of the measured data points $( R ^ { 2 } = 0 . 9 9 3 1 )$ ). (e) The signal-to-noise-ratio (SNR) of the SRP microscopy as a function of sample concentration. The red line is the linear fitting curve of the measured data points $( R ^ { 2 } = 0 . 9 9 9 4 )$ . (f) The SRP spectrum of DMSO in $\mathsf { D } _ { 2 } \mathsf { O }$ at a concentration of 21.84 mM.

The SRP signal intensity from the 100 mm bead was found to be roughly 10 times as that of the $1 0 \mu \mathrm { m }$ beads (both measured at the centre part of the beads). This result further confirmed the validity of our SRP microscope in chemical quantification.

As an example to quantify biomolecules, we imaged lipid droplets (LDs) in differentiated 3T3-L1 cells. We tuned the Raman transition to CH symmetric vibration at $2 { , } 8 5 0 \mathrm { c m } ^ { - 1 }$ to image the LDs. The cells have near-spherical shapes with diameters up to tens of micrometres. We first acquired 50 sectional images of a cell by the Gaussian beam SRS microscope at 1 mm per depth step. The total image acquisition time was 45 s. Figure 6a shows the sectional images at depths of $z = 2 0 , 3 0$ and

a  
![](images/d49b3e9160dde53d2370cb37f3d76016f3fa0690504530737810d314559a57e8.jpg)

<details>
<summary>text_image</summary>

z=8 µm
z=32 µm
z=56 µm
z=74 µm
z=94 µm
</details>

b  
![](images/2e23fdad54450fb9c5c74c4748d58608032549ab7d45a3ad7556ff89c4ab4e68.jpg)

<details>
<summary>natural_image</summary>

Black background with scattered colorful dots (no text or symbols)
</details>

c  
![](images/f3b6818ebdce665aac3392c4d39b11fd06a475cb0008762286f969d3c49e6992.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescent spots on a dark red background, labeled 'On' in top-left corner (no other text or symbols)
</details>

d  
![](images/5c25ddf4938a12879799568dfd71faef46dbcb269bc3459e38b35672e32af287.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a red-stained surface with a white label 'Off' in the top-left corner and a scale bar at bottom right (no other text or symbols)
</details>

Figure 5 | Volumetric imaging of polystyrene beads. (a) Sectional images acquired by the Gaussian beam stimulated Raman scattering (SRS) microscope at different depths of the sample volume. (b) Superposition of the sectional images in a. The false-colours were used to represent beads located at different depths. Stimulated Raman projection (SRP) images of the same beads acquired when the Raman resonance was on (c) and off (d). The pixel dwell times were 10 ms for the SRS imaging and 50 ms for the SRP imaging. Scale bars, 30 mm

a  
![](images/d3f4813aac9f033feab12a88bebbea8326b6781ffc962d646ab83af734154c99.jpg)

<details>
<summary>heatmap</summary>

| z-value | Intensity (a.u.) |
|---------|------------------|
| 20 µm   | ~0.5             |
| 30 µm   | ~0.8             |
| 40 µm   | ~0.6             |
</details>

b  
![](images/b60e0edd041dd0e94b8ccdd0ffd7d47d64526e45985703f2590721d6b662c52b.jpg)

<details>
<summary>text_image</summary>

1
Intensity (a.u.)
0
c On
d Off
</details>

Figure 6 | Volumetric imaging of a single adipose cell. (a) Sectional images acquired by the Gaussian beam stimulated Raman scattering (SRS) microscope at different depths of the sample. (b) Superposition of the 50 sectional images. Stimulated Raman projection (SRP) images of the same cel acquired when the Raman resonance was on (c) and off (d). The pixel dwell time was 10 ms for both the SRS and SRP imaging. The signal profiles along the dashed lines were display at the bottom-right of the images. Scale bars, 30 mm.

40 mm, displaying very different intracellular morphologies about LDs. Figure 6b gives a superposition of the 50 sectional images, representing the overall lipid content in the cell. The SRP image of the same cell, on the other hand, directly revealed such global information of lipids through a single 2D lateral scan taken only 0.9 s (Fig. 6c,d), giving the morphology and intensity profile similar to those of the superposition image (Fig. 6b). This example further highlighted the advantage of speed in using the SRP microscopy to quantify global information of biomolecules in a volume.

SRP tomographic imaging. Although the SRP microscopy can quantify chemicals or biomolecules in a volume at a high speed, it loses axial resolution. To solve this limitation, we developed an SRP-based tomographic method to reconstruct the 3D distribution of biomolecules in a volume with optical resolution. In this tomographic method, projection images were collected while rotating the sample at 1- per step for 180 steps. The 180 projection images were then assembled to reconstruct the 3D information within the imaging volume. We first wrote the reconstruction code and then validated the code using simulation. The simulation model contained four objects that generated signals, as shown in Supplementary Fig. 10. The SRP image stack was formed by rotating the sample around the principle axis of the cylindrical volume (along z direction) while projecting the objects to a plane along the axis. The location and distribution of the objects were then reconstructed from the SRP image stack with the filtered back-projection (FBP) algorithm34. The reconstructed 3D volume and the relevant cross-sectional images from the transverse, coronal and sagittal views are shown in Supplementary Movie 2 and Supplementary Fig. 11, showing good agreement with the original objects (Supplementary Fig. 10).

Experimentally, we imaged 3D distribution of poly(methyl methacrylate) (PMMA) beads (10 mm) in agarose gel. The laser was tuned to excite Raman transition at $2 , 9 5 0 \mathrm { c m } ^ { \simeq 1 }$ from $\mathrm { C H } _ { 3 }$ vibration. The sample was loaded into a cylindrical capillary tube (50 mm in diameter) that was fixed onto a rotation stage. The sample was consecutively rotated 180- at 1- per step. The SRP images from the beads were then collected at each step. The reconstructed volume had a dimension around $6 0 \times 6 0 \times { \bar { 6 0 } } { \mu \mathrm { m } } ^ { 3 }$ . In the reconstructed tomographic image, the dimension and location of the beads were well resolved (Supplementary Movie 3). Furthermore, the validity of the tomographic reconstruction was verified by the reconstructed volume from sectional images obtained by the Gaussian beam SRS sectioning imaging on the same beads. The reconstructed 3D volume of the PMMA beads by the sectioning imaging is shown in Supplementary Movie 4. For a direct comparison, we selected the corresponding sections (in coronal and sagittal views) of the beads imaged using both methods, as shown in Fig. 7. Though slightly decreased in spatial resolution, the SRP tomographic results agreed well with the SRS sectioning imaging results in terms of the morphology and localization. The spherical shape of the beads can be well reconstructed with little distortion, which was proved by comparing the bead profiles along three axial directions, as shown in the Supplementary Fig. 12.

The SRP tomography has a greater advantage in imaging speed when a larger volume is measured. As an example, we imaged a 100 mm polystyrene bead in a volume of $\sim 3 2 0 \stackrel { \cdot } { \times } 3 2 0 \times 3 2 0 \stackrel { \cdot } { \mu } \mathrm { m } ^ { 3 } .$ . The reconstructed 3D volume by the SRP tomography is shown in Supplementary Movie 5. The reconstruction fidelity of the SRP tomography was again confirmed by comparing one of the 3D sectional images with the corresponding one acquired by the Gaussian beam SRS sectioning imaging (Supplementary Fig. 13). Using the SRP tomography, 47 s was needed to collect the SRP image stack of 180 projections. However, using the Gaussian beam SRS sectioning imaging method, it takes 723 sections, equals to 188 s, to complete 3D imaging of such a large volume. In this case, our SRP tomography is four times faster than the sectioning imaging method. For imaging an even larger volume, when more sectional images are needed to reconstruct the volume structure, the advantage of SRP tomography in imaging speed would be further manifested. We note that the imaging speed calculated here is for a single Raman shift. By tuning the wavelength of the pump beam, different Raman shifts can be imaged. The laser tuning can be achieved in tens of milliseconds within the 200 cm - 1 range or in seconds over a larger range in $4 , 0 0 0 { \mathrm { c m } } ^ { - 1 } \ ( { \mathrm { r e f . } } \ 3 5 )$ .

![](images/b802b7acd6d59958388d1247bfb8b95fe4c911bef0b88e6896b39622999045e7.jpg)  
Figure 7 | Comparing volumetric imaging results from stimulated Raman projection tomographic and stimulated Raman scattering sectional imaging. (a,b) Selected image slices of PMMA beads at different positions in the sagittal view (yz plane). (c,d) Selected image slices from the same beads in the coronal view (xz plane). (a,c) Images reconstructed by the stimulated Raman projection (SRP) tomography. (b,d) Sectional images collected by the Gaussian beam stimulated Raman scattering (SRS) microscope. The imaged volume was $\sim 6 0 \times 6 0 \times 5 0 \mu \mathrm { m } ^ { 3 }$ for SRS sectioning imaging and $6 0 \times 6 0 \times 6 0 \mu \mathrm { m } ^ { 3 }$ for SRP tomographic imaging. The pixel dwell time was 10 ms for the SRS sectional imaging and 24 ms for the SRP tomographic imaging Scale bars, 10 mm.

Next, we performed SRP tomography on single differentiated 3T3-L1 cells to explore the potential of this technique for 3D in vivo imaging of biomolecules. The laser was tuned to excite CH vibration at 2,850 cm - 1. Figure 8a shows the reconstructed 3D distribution of lipids in the cell, while the complete 3D view is displayed in Supplementary Movie 6. The selected slices in the sagittal and the transverse views displayed different lipid distributions and were shown in Fig. 8b,c, respectively. Such lipid distributions were also revealed in the SRS sectional images in the transverse view (Supplementary Fig. 14), showing good agreement with the tomographic results besides little differences in fine structures, possibly caused by differences in system resolutions, discrepancies in image depths and disagreements in sample orientation. The spatial resolution of the SRP tomographic images was slightly lower than that of the SRS sectional images, caused by the lower effective NA in the SRP measurement (B0.88 in Bessel SRP and B1.07 in Gaussian SRS). These results confirmed the applicability of the SRP tomography for in vivo imaging of biomolecules in a 3D volume.

## Discussion

We reported a proof of concept demonstration of the Besselbeam-based SRP microscopy and tomography for label-free volumetric imaging. Our SRP microscope is capable of quantifying chemical compositions in a living system with a single 2D lateral scan. With the help of the tomographic strategy, we resolved 3D distribution of chemicals in a volume with isotropic spatial resolution. We demonstrated the potential of this new technology by volumetric imaging of polymer particles in a volume and 3D distribution of lipids in single adipose cells.

It is important to discuss pros and cons of our Bessel-beambased SRP technology in the context of Gaussian-beam-based SRS microscopy. In SRP, the diffraction-free Bessel beam enables volumetric examination of millimetre-scale specimens. Because we use two Bessel beams for the pump and Stokes fields at two different wavelengths, the signal only arises from the central lobe (Fig. 2e,f; Supplementary Fig. 2), which ensures the diffractionlimited spatial resolution. More importantly, because of the energy exchange between the rings and the central lobe during propagation, Bessel beams are able to maintain the focus through a highly scattered medium33. Thus, one can potentially apply our SRP technology to examine subjects buried inside a millimetre layer highly scattered medium. These capabilities are beyond the reach by the Gaussian beam SRS microscopy. On the other hand, we note that only a small portion of the total energy resides in the central lobe, our technology is not sensitive to sub-micrometre features, for which SRS microscopy will offer better performance. Meanwhile, we note that there is plenty of room for further improvement of our SRP microscopy and tomography, as discussed below.

First, we can further increase the detection sensitivity of the system. In this work, the input power of the pump beam was limited by the photo-saturation of the detector. This was because the detector collected all the photons distributed on the centra lobe and side rings; however, only the central lobe photons contributed for generating SRP signal. A detector with higher saturation power can further improve the sensitivity of the SRP system. Moreover, the input power of the Stokes beam was limited by the current laser system. A more powerful laser with higher output power for the Stokes beam would allow an increase in the generation of SRP signal, in turn a higher detection sensitivity.

Second, we can further increase the spatial resolution of our SRP technology. In this work, we used a dual-axis scanning galvo system with two large area scanning mirrors. The distance between the two mirrors was so large that they cannot be simultaneously conjugated to the entrance pupil of the objective lens. Consequently, to avoid beam clipping during laser scanning, we shrunk the beam smaller than the objective entrance pupil did. Therefore, the effective NA of our system is usually smaller than the actual NA of the objective. For example, using a  40, 0.8 NA objective, which ideally allowed a 0.38 mm spatial resolution, the SRP microscopy utilized an effective NA of only B0.51, which theoretically gave a 0.73 mm spatial resolution (an experimentally measured resolution was B0.83 mm, as shown in Supplementary Fig. 15). In the future, an optimized system allowing a galvo system with shorter distance between the mirrors would further increase the effective NA in the SRP scheme, in turn improving the spatial resolution.

Third, we can further improve the imaging quality and speed of SRP tomography. In current experiments, we used a cylindrical glass tube to mount samples. The refractive index mismatch between the glass tube and the sample would deteriorate the quality of the SRP images, in turn reducing the quality and the resolution of the SRP tomographic images. A better samplemounting scheme, such as using tubes made of fluorinated ethylene propylene that has a refractive index close to that of the sample, can improve the image quality36. The imaging speed of SRP tomography can be improved by applying algorithms that are more efficient. The FBP algorithm used in this work required

![](images/13623b75e39da21efb9e8ca09cd32218887bde07b8dbaf8540a76341eac241bb.jpg)

<details>
<summary>natural_image</summary>

3D visualization of a cube with colored regions and x, y, z axes labeled (no text or symbols beyond axis labels)
</details>

![](images/c436c67ff242c82d1d04bb2819b0717b49ad99d28489b6f7fa58a9b6b3021f99.jpg)

<details>
<summary>text_image</summary>

b
z
y
z
y
z
x
c
y
x
y
x
y
x
z
Intensity (a.u.)
255
0
</details>

Figure 8 | Volumetric imaging of a single adipose cell by stimulated Raman projection tomography. (a) Reconstructed 3D structure of a 3T3-L1 cell. (b) Selected image slices of the 3T3-L1 cell at different positions in the sagittal view (yz plane). (c) Images from the same cell in the transverse view (xy plane). The imaged volume was $\sim 1 5 0 \times 1 5 0 \times 1 5 0 \mu \mathrm { m } ^ { 3 }$ . The pixel dwell time was 10 ms. Scale bars, 20 mm.

180 projections for reconstructing a reasonable 3D image34. By combining iteration algorithm and the sparse reconstruction strategy37, image reconstruction can be performed with much less projection images, which would improve the imaging speed of our SRP tomography.

Fourth, we assumed a constant central lobe intensity for the Bessel beams throughout the sample in the current SRP microscopy and tomography. In fact, the central lobe of the Bessel beam has non-constant intensity distribution along its maximum propagation distance (Supplementary Figs 1b and 7b). By placing the sample at the centre of focus and ensuring the sample thickness smaller than the FWHM of SRP signal, the assumption of a constant value of central lobe intensity is acceptable (Figs 2g,h and 4a). Furthermore, by adding a weighting factor, which is determined by the longitudinal distribution of the central lobe intensity of Bessel beam, to the back-projection intensity during the tomographic reconstruction, the accuracy and the quality of the reconstructed image can be further improved. Alternatively, a logarithmic axicon would generate a Bessel beam with a more constant central lobe intensity for

Finally, we note that the reported SRP imaging system is based on a bulky and relatively expensive femtosecond laser, which limits its potential for broad use and clinical translation. Nevertheless, we anticipate that this limitation can be circumvented through innovations in fibre laser, fibre technology and demodulation strategies. Freudiger et al.39 and Orringer et al.40 demonstrated high-quality SRS imaging of clinical samples using a fibre laser and a balanced detector. Such approach can be adopted to reduce the cost and size of our technology. We also note that Bessel beam can be produced using fibres41, which could simplify the system and enable endoscopic applications. Finally, the lock-in amplifier can be replaced by a low-cost tuned amplifier35,42. Collectively, these strategies could potentially reduce the cost, size and complexity of the SRP set-up towards broader applications and clinical use.

## Methods

Selection of the objective lenses. For different purposes, we generated Bessel beams using different objectives lenses, including a  10 0.3 NA air objective (RMS10X-PF, Thorlabs), a  40 0.8 NA water immersion objective (LUMPlanFLN  40, Olympus), a  60 1.1 NA water immersion objective (LUMFI  60, Olympus) and a  25 1.05 NA water immersion objective (XLPL25XWMP, Olympus). The  10 objective was employed to verify the simulation results, since the Bessel beam generated by this objective had a larger profile for easy measurement and characterization (Supplementary Fig. 1). The  40 objective was used for the SRP microscopic imaging of polymer particles and biological samples, since it allowed for a tighter focusing and hence generating the stronger SRP signal (Supplementary Fig. 16). The  60 objective, which allowed even higher signal to be generated (Supplementary Fig. 16), was used in the SRP tomographic imaging of polymer particles and biological samples. The  25 objective was used for imaging a larger volume (Supplementary Fig. 13). The detailed comparisons of the Bessel beams generated by the four objectives are listed in Supplementary Table 1.

Sample holder for the SRP tomography. A lab-built sample holder was used to hold and rotate samples22. For the SRP microscopic imaging, the sample holder was comprised of a microscope slide holder and a 3D translational stage. The slide holder (MAX3SLH, Thorlabs) was used to hold the sample fixed between two slides or in a cuvette. The 3D translational stage was used to fine tune the sample position at the focus of the Bessel beams. In the SRP tomographic imaging, three more components were added, including a fibre holder, a rotational stage and an additional 3D translational stage. A cylindrical capillary tube, with one end attached to the fibre holder, while the other inserted into a square capillary tube, was used to store samples. The square capillary tube was attached to the slide holder to confine the sample during rotation. The cylindrical capillary tube was rotated while being confined in the square tube. The projection imaging was performed within the boundary of the square capillary tube. The fibre holder (FPH-S, Newport) was attached to the rotational stage installed on a 3D translational stage for position adjustment. The sample rotation was performed by electronically controlling the rotational stage to rotate at 1- per step for 180-. An SRP image was acquired at each rotational step.

Characterization of the SRP microscope. To measure the dependence of the SRP signal and the noise on sample thickness and laser power, we used PDMS films with different thicknesses. The sample was prepared by sandwiching PDMS between two glass slides. The PDMS film thickness ranged from 130 to 1,040 mm, with a 130 mm increment. The SRP signal from 2,915 cm - 1 CH bond vibration was measured (Supplementary Fig. 17a).

The thickness dependence measurements in Fig. 4a were acquired at a 200 ms pixel dwell time. The central lobe powers of the pump and Stokes beams were 0.9 and 6.3 mW, respectively. Signal from the sample was calculated by the average voltage difference between the presence and the absence of the sample.

The laser power dependence measurements in Fig. 4b–d were measured using a 1 mm-thick PDMS, at a 200 ms pixel dwell time. To investigate the dependence of the SRP signal on the Stokes power, the central lobe power of the pump beam was fixed to 0.6 mW and the central lobe power of the Stokes beam was changed from 0.5 to 7.35 mW, with a 0.5 mW increment. For the measurement of signal dependence on the pump power, the central lobe power of the Stokes beam was fixed to 4.2 mW and the central lobe powers of the pump beam were set to 0.02, 0.06, 0.13, 0.18, 0.26, 0.37, 0.44, 0.52 and 0.60 mW. In the noise analysis, the pump powers at the photodiode were set to 0.3, 0.9, 1.2, 1.7, 2.4 and 3 mW.

Different concentrations of DMSO in D O (10.92, 21.84, 43.75, 87.50, 175, 350, 700 and 1,400 mM) were used for the measurement of system sensitivity. The sample, stored in a quartz cuvette, has a thickness of 2 mm. The wavelength of pump beam was set to 798 nm to excite the DMSO Raman shift at 2,915 cm - 1 $2 , 9 1 5 \mathrm { c m } ^ { - 1 }$ (Supplementary Fig. 17b). The pixel dwell time was 1 ms for all the measurements. The central lobe powers of the pump and Stokes beams were 0.7 and 30 mW, respectively. For the SRS spectral measurement at 21.84 mM DMSO, the central lobe powers of the chirped pump and Stokes beams were B1.1 and B27 mW, respectively. Using the same method, we measured SRP signal from different concentrations of retinoic acid in D2O (0.05, 0.1. 0.25, 0.5, 1. 5 and 25 mM) The pump beam wavelength was tuned to 893 nm to excite the Raman shift at B1,583 cm - 1 (Supplementary Fig. 17c). The pump and Stokes powers at the central lobe of the Bessel beams were 0.9 and 23 mW, respectively. The spectra of DMSO and retinoic acid were measured using spectral focusing method43.

SRP microscopic imaging. For the SRP microscopic imaging of polystyrene beads, the wavelength of the pump beam was tuned to 789 nm to excite the Raman shift at B3,058 cm - 1. The beads were suspended in a 1.5 wt% cured agarose gel to prevent particle movement during image acquisition. The sample mixture was sandwiched between two glass slides with B130 mm spacing. For the Gaussian beam modality, 50 sectional images were acquired at 2 mm per step in depth. The powers of the pump and Stokes beams at sample were B10 and B24 mW, respectively. The pixel dwell time was 10 ms and the image size was 200  200 pixels. The total acquisition time of an image stack was B20 s, excluding the time for data transfer and storage, and the sample stage moving along the depth direction. In the Bessel beam SRP modality, all the beads were resolved in one projection image obtained from a 2D lateral scan. The central lobe powers of the pump and Stokes beams were B1 and B30 mW, respectively. The pixel dwell time was 50 ms and the image size was 200  200 pixels. The total image acquisition time was ∼ 2 s.

3T3-L1 cells were also embedded in the cured agarose gel and sandwiched between two glass slides for imaging. The wavelength of the pump beam was tuned to 802 nm, exciting the 2,850 cm - 1 Raman shift from lipids. We first acquired 50 sectional images at 1 mm per step in depth using the Gaussian beam SRS modality. The powers of the pump and Stokes beams at sample were B10 and B24 mW, respectively. The pixel dwell time was 10 ms and the image size was 300  300 pixels. The total acquisition time of the image stack was B45 s, excluding the time used for data transfer and storage, and the sample stage movement along the depth direction. The SRP projection image of the whole cell was acquired with the central lobe powers of pump and Stokes beams being 1 and 34 mW, respectively. The pixel dwell time was 10 ms and the image size was 300  300 pixels. The total image acquisition time was B0.9 s.

SRP tomographic imaging. For the SRP tomographic imaging of PMMA beads (10 mm), the wavelength of pump beam was tuned to 796 nm. The beads were first mixed with 1.5 wt% agarose gel, and then the sample mixture was cured in a cylindrical capillary tube (inner diameter: 50 mm; outer diameter: 80 mm). One end of the tube was attached to the fibre holder and the other end of the tube was inserted into a square capillary tube (inner width: 100 mm, wall thickness: 50 mm). The square capillary tube was then fixed on the slide holder to prevent sample movement during rotation. By rotating the capillary tube 1- per step, 180 projection images were collected with 24 ms pixel dwell time. Each image was 150  150 pixels. The whole imaged volume was B60  60  60 mm3. The central lobe powers of the pump and Stokes beams were B1.2 and B35 mW, respectively. For image comparison, the sectional image stack collected using the Gaussian modality contains 50 images, which were acquired at 1 mm per step. The total volume acquired in imaging was $\sim 6 0 \times 6 0 \times 5 0 \mathrm { { \mu m } } ^ { 3 } .$ . The pixel dwell time was 10 ms. The powers of the pump and Stokes beams at sample were B13 and B25 mW, respectively.

Similarly, we imaged a 100 um PS bead in a volume of \~ 320 × 320 × 320 um (Supplementary Fig. 13). The total acquisition time for the SRP image stack was

47 s. The powers of the pump and Stokes beams at the central lobe were B3 and B35 mW, respectively.

For the SRP tomographic imaging of the 3T3-L1 cells, the sample was prepared using a similar way as the beads. A total of 180 projection images were collected at 1- angle increment with 10 ms pixel dwell time. Each image was 300  300 pixels. The whole imaged volume was B150  150  150 mm3. The central lobe powers of pump and Stokes beams were B1 and B30 mW, respectively. The total acquisition time for the tomographic image stack was B162 s. The sectional image stack collected using the Gaussian modality contains 90 images, which were acquired at 1 mm per step. The total volume acquired in imaging was B150  150  90 mm3. The pixel dwell time and the image size were the same as those used in the SRP tomography. The powers of the pump and Stokes beams at sample were B13 and 25 mW, respectively. The Gaussian beam has an axial resolution of 0.65 mm. To image a volume with 150 mm depth, it requires 4230 sectional images.

Image processing and reconstruction. Data acquisition and storage were performed on a lab-written software based on LabVIEW (National Instruments Corporation). The 2D images were processed and analysed using ImageJ. Parallel-beam-based FBP algorithm written in MATLAB (The MathWorks, Inc.) was used to reconstruct the 3D volume from the SRP images34. The total reconstruction time for a volume of 150  150  150 pixels was B50 s by using a personal computer (Inter Core i7-4702HQ CPU at 2.2 GHz, 8 GB RAM). The visualization and analysis of the SRP tomographic volume and the volume created from the sectioning images were accomplished using Amide.

The detailed theory for Bessel beam SRP signal calculation, the materials used in this work and other experimental procedures can be found in Supplementary Notes 1–3 and Supplementary Methods.

Data availability. The data and codes that support the findings of this study are available from the corresponding author on reasonable request.

## References

1. Christof, J. et al. Single-molecule imaging of transcription factor binding to DNA in live mammalian cells. Nat. Methods 10, 421–426 (2013).  
2. Sharpe, J. et al. Optical projection tomography as a tool for 3D microscopy and gene expression studies. Science 26, 541–545 (2002).  
3. Ahrens, M. et al. Whole-brain functional imaging at cellular resolution using light-sheet microscopy. Nat. Methods 10, 413–420 (2013).  
4. Fu, Q. et al. Imaging multicellular specimens with real-time optimized tiling light-sheet selective plane illumination microscopy. Nat. Commun. 7, 11088 (2016).  
5. Katona, G. et al. Fast two-photon in vivo imaging with three-dimensional random-access scanning in large tissue volumes. Nat. Methods 9, 201–208 (2012).  
6. Dana, H. et al. Hybrid multiphoton volumetric functional imaging of large-scale bioengineered neuronal networks. Nat. Commun. 5, 3997 (2014).  
7. Camp, Jr C. & Cicerone, M. Chemically sensitive bioimaging with coherent Raman scattering. Nat. Photon. 9, 295–305 (2015).  
8. Krafft, C. et al. Developments in spontaneous and coherent Raman scattering microscopic imaging for biomedical applications. Chem. Soc. Rev. 45, 1819–1849 (2016).  
9. Sharpe, J. et al. Optical projection tomography as a new tool for studying embrvo anatomy. J. Anat. 202, 175181 (2003).  
10. Eisenstei, M. et al. Pump up the volume. Nat. Methods 12, 19–22 (2015).  
11. Bouchard, M. et al. Swept confocally-aligned planar excitation (SCAPE) microscopy for high-speed volumetric imaging of behaving organisms. Nat. Photon. 9, 113–119 (2015).  
12. Wu, Y. et al. Inverted selective plane illumination microscopy (iSPIM) enables coupled cell identity lineaging and neurodevelopmental imaging in Caenorhabditis elegans. Proc. Natl Acad. Sci. USA 108, 17708–17713 (2011).  
13. Tomer, R. et al. Quantitative high-speed imaging of entire developing embryos with simultaneous multiview light-sheet microscopy. Nat. Methods 9, 755–763 (2012).  
14. Stelzer, E. Light-sheet fluorescence microscopy for quantitative biology. Nat. Photon. 12, 23–26 (2015).  
15. Keller, P., Ahrens, M. & Freeman, J. Light-sheet imaging for systems neuroscience. Nat. Photon. 12, 2729 (2015).  
16. Cheng, J. & Xie, X. Vibrational spectroscopic imaging of living systems: an emerging platform for biology and medicine. Science 350, aaa8870 (2015).  
17. Oshima, Y., Furihata, C. & Sato, H. Light sheet direct Raman imaging technique for observation of mixing of solvents. Appl. Spectrosc. 63, 1115–1120 (2009).  
18. Barman, I., Tan, K. & Singh, G. Optical sectioning using single-plane illumination Raman imaging. J. Raman Spectrosc. 41, 10991101 (2010)  
19. Oshima, Y. et al. Light sheet-excited spontaneous Raman imaging of a living fish by optical sectioning in a wide field Raman microscope. Opt. Express 20, 16195–16204 (2012).  
20. Rocha-Mendoza, I. et al. Rapid spontaneous Raman light sheet microscopy using cw-lasers and tunable filters. Biomed. Opt. Express 6, 3449–3461 (2015)  
21. Mu¨ller, W. et al. Light sheet Raman micro-spectroscopy. Optica 3, 452–457 (2016).  
22. Bruns, T., Schickinger, S. & Schneckenburger, H. Sample holder for axia rotation of specimens in 3D microscopy. J. Microsc. 260, 30–36 (2015).  
23. Boot, M. et al. In vitro whole-organ imaging: 4D quantification of growing mouse limb buds. Nat. Methods 5, 609–612 (2008).  
24. Pardo-Martin, C. et al. High-throughput hyperdimensional vertebrat phenotyping. Nat. Commun. 4, 1467 (2013).  
25. Schulmerich, M. et al. Noninvasive Raman tomographic imaging of canine bone tissue. J. Biomed. Opt. 13, 020506 (2008).  
26. Demers, J. et al. Multichannel diffuse optical Raman tomography for bone characterization in vivo: a phantom study. Biomed. Opt. Express 3, 2299–2305 (2012).  
27. Demers, J. et al. Next-generation Raman tomography instrument for non-invasive in vivo bone imaging. Biomed. Opt. Express 3, 793–806 (2015).  
28. Stuker, F. et al. Fluorescence molecular tomography: principles and potential for pharmaceutical research. Pharmaceutics 3, 229274 (2011)  
29. Konovalov, A. B. & Vlasov, V. V. Theoretical limit of spatial resolution in diffuse optical tomography using a perturbation model. Quant. Electron. 44, 239–246 (2014).  
30. Zhang, C., Zhang, D. & Cheng, J. Coherent Raman scattering microscopy in biology and medicine. Annu. Rev. Biomed. Eng. 17, 415–445 (2015).  
31. Planchon, T. et al. Rapid three-dimensional isotropic imaging of living cells using Bessel beam plane illumination. Nat. Methods 8, 417–423 (2011).  
32. Heuke1, S. et al. Bessel beam CARS of axially structured samples. Sci. Rep. 5, 10991 (2015).  
33. Fahrbach, F., Simon, P. & Rohrbach, A. Microscopy with self-reconstructing beams. Nat. Photon. 4, 780–785 (2010).  
34. Zeng, G. Medical Image Reconstruction: A Conceptual Tutorial (High Education Press and Springer, 2010).  
35. Liao, C. S. et al. Microsecond scale vibrational spectroscopic imaging by multiplex stimulated Raman scattering microscopy. Light Sci. Appl. 4, e265 (2015).  
36. Kaufmann, A. et al. Multilayer mounting enables long-term imaging of zebrafish development in a light sheet microscope. Development 139, 3242–3247 (2012).  
37. Correia, T. et al. Accelerated optical projection tomography applied to in vivo imaging of zebrafish. PLoS ONE 10, e0136213 (2015).  
38. Golub, I. et al. Characterization of a refractive logarithmic axicon. Opt. Lett. 35, 2828–2830 (2010).  
39. Freudiger, C. W. et al. Stimulated Raman scattering microscopy with a robust fibre laser source. Nat. Photon. 8, 153–159 (2014).  
40. Orringer, A. D. et al. Rapid intraoperative histology of unprocessed surgical specimens via fibre-laser-based stimulated Raman scattering microscopy. Nat. Biomed. Eng. 1, 0027 (2017).  
41. Steinvurzel, P. et al. Fiber-based Bessel beams with controllable diffraction-resistant distance, Opt. Lett, 36, 46714673 (2011).  
42. Slipchenko, M. N. et al. Heterodyne detected nonlinear optical imaging in a lock-in free manner. J. Biophoton. 5, 801–807 (2012).  
43. Liu, B. et al. Label-free spectroscopic detection of membrane potential using stimulated Raman scattering. Appl. Phys. Lett. 106, 173704 (2015).

## Acknowledgements

This work was partly supported by a Keck Foundation grant and a National Institutes of Health (NIH) R01 grant GM118471 to J.-X.C. X.C. acknowledges the National Natura Science Foundation of China (nos 81627807, 81227901 and 81571725) and the China Scholarship Council for a financial support (no. 201406965025). P.L. acknowledges the support from senior thesis research funding program offered by Tianjin University. We appreciate Dr Shouping Zhu of Xidian University for the help in the implementation of reconstruction algorithm, Dr Yanfeng Li of Tianjin University, Dr Delong Zhang and Chien-Sheng Liao of Purdue University for helpful discussions.

## Author contributions

X.C., C.Z. and J.-X.C. designed the experiments; X.C., C.Z. and P.L. built the SRP imaging system; X.C., C.Z., P.L. and K.-C.H. performed the experiments; X.C., C.Z. and P.L. analysed the data; X.C. and J.L. wrote the codes for 3D reconstruction; C.Z prepared 3T3-L1 cells for imaging. X.C., C.Z. and J.-X.C. wrote the manuscript; J.T. and J.-X.C. provided overall guidance of the project. All authors read and approved the manuscript.

## Additional information

Supplementary Information accompanies this paper at http://www.nature.com/ naturecommunications

Competing interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/ reprintsandpermissions/

How to cite this article: Chen, X. et al. Volumetric chemical imaging by stimulated Raman projection microscopy and tomography. Nat. Commun. 8, 15117 doi: 10.1038/ncomms15117 (2017).

Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/a165218a365355ba2fa68e3ce0c0cf3ef2470dbcea83bfef7dc1c4f69a364c07.jpg)

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this

article are included in the article’s Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/

r The Author(s) 2017