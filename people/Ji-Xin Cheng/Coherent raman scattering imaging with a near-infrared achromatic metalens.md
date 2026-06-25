RESEARCH ARTICLE | SEPTEMBER 14 2021

# Coherent Raman scattering imaging with a near-infrared achromatic metalens

Peng Lin ; Wei Ting Chen ; Kerolos M. A. Yousef; Justin Marchioni; Alexander Zhu; Federico Capasso  ; Ji-Xin Cheng 

![](images/471675aaccf06017fbb91a4720bb54a1f3d7f6ef3936ae5069c74b51e7a8eb38.jpg)

Check for updates

APL Photonics 6, 096107 (2021)

https://doi.org/10.1063/5.0059874

![](images/a1e04e983fb9a981e621f79cccd3da6c664259d75bd7b048def9f571645d01d0.jpg)  
View Online

![](images/4c8da4130e8dd597f3ab21fdcc0af9a1b417c293133cdc25140484fb52a24cd2.jpg)  
Export Citation

## Articles You May Be Interested In

Broadband achromatic mid-infrared metalens with polarization-insensitivity

AIP Advances (February 2022)

High-efficiency broadband achromatic metalens in the visible

Appl. Phys. Lett. (March 2025)

Computational inverse design for ultra-compact single-piece metalenses free of chromatic and angular aberration

Appl. Phys. Lett. (January 2021)

## AIP Advances

## Why Publish With Us?

![](images/b7ddd3d9e35fc60b0d8a4a3b0d3c5b67d5725e7498f6a1d8534e556f4b9f80d5.jpg)  
21DAYS average time to 1 st decision

![](images/bcb6cef7a63adfe551c0c52bf0521dfa4c13499cba5495db3fdf1b56cacd305d.jpg)  
OVER 4 MILLION views in the last year

![](images/f58d8e1faa1d4c1f40bf88ac6116e43a04377a6b4f39f04a9388b658d139661d.jpg)  
INCLUSIVE scope

Learn More

![](images/a2bb67ed31761aaf9094d688de2fe39f949e7bddd73f2307e966efab3894e3e8.jpg)  
AIP ublishing

# Coherent Raman scattering imaging with a near-infrared achromatic metalens

Cite as: APL Photon. 6, 096107 (2021); doi: 10.1063/5.0059874 Submitted: 13 June 2021 • Accepted: 24 August 2021 • Published Online: 14 September 2021

![](images/2850a00f82017df81479153b05a2af7fd953a547c2e602f17723f93d925aee9b.jpg)

![](images/674250fcc3c6aba601c31a905e9045676139f3c3ff4895c6a4313018612a4dea.jpg)

![](images/10304469dc58e21ea0dff379b6547ee3f2e3507641f1d74d7ccb583de562a852.jpg)

Peng Lin,1 Wei Ting Chen,2 Kerolos M. A. Yousef,,2,3 Justin Marchioni,,2,4 Alexander Zhu,2 Federico Capasso,2,a) and Ji-Xin Cheng1,5,6,a)

## AFFILIATIONS

1 Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, USA  
2John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, Massachusetts 02138, USA  
3College of Biotechnology, Misr University for Science and Technology, Giza 12568, Egypt  
4Department of Physics and Astronomy, University of Waterloo, Waterloo, Ontario N2L 3G1, Canada  
5Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, USA  
6Photonics Center, Boston University, Boston, Massachusetts 02215, USA

a)Authors to whom correspondence should be addressed: capasso@seas.harvard.edu and jxcheng@bu.edu

## ABSTRACT

Miniature handheld imaging devices and endoscopes based on coherent Raman scattering are promising for label-free in vivo optical diagnosis. Toward the development of these small-scale systems, a challenge arises from the design and fabrication of achromatic and high-end miniature optical components for both pump and Stokes laser wavelengths. Here, we report a metasurface converting a low-cost plano–convex lens into a water-immersion, nearly diffraction-limited and achromatic lens. The metasurface comprising amorphous silicon nanopillars is designed in a way that all incident rays arrive at the focus with the same phase and group delay, leading to corrections of monochromatic and chromatic aberrations of the refractive lens, respectively. Compared to the case without the metasurface, the hybrid metasurface-refractive lens has higher Strehl ratios than the plano–convex lens and a tighter depth of focus. The hybrid metasurface-refractive lens is utilized in spectroscopic stimulated Raman scattering and coherent anti-Stokes Raman scattering imaging for the differentiation of two different polymer microbeads. Subsequently, the hybrid metalens is harnessed for volumetric coherent Raman scattering imaging of bead and tissue samples. Finally, we discuss possible approaches to integrate such hybrid metalens in a miniature scanning system for label-free coherent Raman scattering endoscopes.

© 2021 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license. (http://creativecommons.org/licenses/by/4.0/). https://doi.org/10.1063/5.0059874

## I. INTRODUCTION

Coherent Raman scattering (CRS) microscopy based on coherent anti-Stokes Raman scattering (CARS) or stimulated Raman scat tering (SRS) is a label-free, high spatial resolution, and chemicalspecific imaging technology.1–4 In the past two decades, benchtop CRS microscopes have been demonstrated as powerful laboratory tools for various applications, such as cancer diagnosis,5,6 stain-free histopathology,7,8 metabolic imaging,9 brain imaging,10,11 and drug discovery.12 Toward translating CRS imaging to the clinic, Hollon et al. recently reported a pilot study of brain tumor detection in human tissue slices with a mobile SRS microscope in a surgical suite, showing great potential for stainfree intraoperative histopathology.13 However, current benchtop CRS microscopes are bulky and hinder the capacity to image the lesions in human patients and internal organs. To overcome these issues, it is vital to miniaturize the CRS imaging systems, such as developing handheld SRS microscopes1 and CARS endoscopes,15,16 which directly apply to the human body.

To develop a handheld CRS imaging system, it is essential to design and fabricate high-performance miniature objective lenses that allow high-quality focusing. Because CARS and SRS rely on utilizing two synchronized pulsed laser beams of different wavelengths, namely, pump and Stokes beams, to match a Raman transition, the lenses need to tightly focus the laser beams to the same spot to obtain optimal signals and 3D sectioning resolution. Although commercial achromatic objectives have been widely used in benchtop CRS microscopes, they typically comprise multiple bulky lenses to correct aberrations.17,18 For endoscopy, it is challenging to precisely fabricate and align miniature lenses due to their curved configuration and small diameter. As a result, typical endoscope lenses suffer from inferior optical quality and severe monochromatic and chromatic aberrations.19

Resulting from their compact footprint and versatile opti cal properties, metasurface-based optical components, consisting of subwavelength-spaced nanostructures, have found broad applications in miniaturized optical systems,20–22 depth sensing,23–25 pulse shaping,26 and polarization control.27 These applications are enabled by the fact that a metasurface is able to simultaneously control transmitted light’s wavefront, dispersion, and polarization. These advantages originate from the constituent nanostructures: each nanostructure has many geometric parameters that are tunable to provide the required phase, polarization, and dispersion properties. Conventional diffractive elements control phase delays by heights, which results in shadow effect lowing transmittance,28 while metasurface components have more degrees of freedom29 in varying nanostructure shape, leading to high angular efficiency.30 For instance, by applying topology optimization and inverse design, the diffraction efficiency of metasurfaces has been increased up to about 95% for high diffraction angles.31 By controlling the phase, group delay, and group delay dispersion, achromatic metalenses have been demonstrated in the visible wavelength region.32–34 A hybrid metalens that integrates a metasurface with a low-cost singlet refractive lens has shown the ability to eliminate chromaticity as well as other optical aberrations.35 Moreover, the development of a diffractionlimited immersion metalens suggested the potential of using a metalens to directly image biological tissues.36,37 The aforementioned advances of achromatic metalenses have shown great potential to serve as a high-end miniature objective lens in endoscopic systems.

Here, we report a hybrid water-immersion achromatic metalens that is particularly designed for pump and Stokes wavelengths at the near-infrared region [Fig. 1(a)]. The hybrid metalens consists of a 2-mm-diameter plano–convex refractive lens attached to a 1.5-mm-diameter metasurface. The refractive lens and the metasurface were assembled under a laboratory-built microscope. The hybrid metalens was demonstrated to achromatically focus wavelengths of 800 and 1040 nm with near diffractionlimited performance and used for SRS and CARS imaging at the C–H Raman transition region (i.e., 2800–3100 cm−1). By imaging 1-μm polystyrene (PS) beads at $2 9 5 5 ~ \mathrm { c m } ^ { - 1 }$ , the hybrid metalens shows a 1.3- and 3.8-times improvement in lateral and axial resolution, respectively, compared with the case of only using the refractive lens. Employing a spectral focusing approach, the hybrid metalens enables spectroscopic forward SRS and backward (epi-) CARS imaging to map and differentiate PMMA and PS beads. Finally, we demonstrate the new capability of the metalens in volumetric CRS imaging of PMMA beads, mouse ear, and ovarian cancer tissue samples. These studies collectively demonstrate a way to develop metalens-based CRS endoscopic imaging systems.

![](images/cd5132c87e7e6a208c4b8b6f0d85250e8d94b334149d862a03a2f72cadf3aaca.jpg)

<details>
<summary>text_image</summary>

(a)
ωp - ωs = Ωvib
metasurface
Pump (ωp)
Stokes (ωs)
refractive lens
tape substrate
water
molecule
Anti-Stokes (ωas=2ωp- ωs)
ICARS
I_p
I_s
I_ΔI_p
Pump (ωp)
I_ΔI_S
Stokes (ωs)
</details>

![](images/6e354e67fa5556eaae7942c47bf4c27b5f137839469578e6f86665940c8e3b1e.jpg)

<details>
<summary>heatmap</summary>

| Δf=0μm | 5μm | 10μm | 15μm |
| ------ | --- | ---- | ---- |
| z      |     |      |      |
| Norm.   |     |      |      |
| SRS inf|     |      |      |
</details>

![](images/4b1fb83e5a15df918e8ef056ca23dc0a05e6d2315e2f0604d4f8d334bda6bf0b.jpg)

<details>
<summary>line chart</summary>

| Focal length difference (Δf) (μm) | Norm. SRS int. (a.u.) | SRS axial resolution (μm) |
| -------------------------------- | --------------------- | ------------------------- |
| 0                                | 1.0                   | 10                        |
| 3                                | 0.8                   | 12                        |
| 6                                | 0.6                   | 14                        |
| 9                                | 0.4                   | 16                        |
| 12                               | 0.2                   | 18                        |
| 15                               | 0.0                   | 20                        |
</details>

FIG. 1. Schematic diagram of a hybrid water-immersion achromatic metalens for CRS imaging and theoretical analysis on the effect of chromatic aberration. (a) Illustration of a hybrid metalens to achromatically focus the pump and Stokes beams. The hybrid metalens consists of a plano–convex glass lens attached to a metasurface comprising α-silicon nanopillars. $\omega _ { \mathsf { p } }$ and $\omega _ { \mathsf { S } }$ label the frequencies of the pump and Stokes beams. $\Omega _ { \mathrm { v i b } }$ is the targeted Raman transition, which is equal to the energy difference between the pump and Stokes beam (i.e., $\Omega _ { \mathrm { v i b } }$ $= \omega _ { \mathsf { p } } - \omega _ { \mathsf { s } } )$ . $\Omega _ { \sf a s }$ is the frequency of newly generated coherent anti-Stokes light (i.e., $\Omega _ { \sf a s } = 2 \omega _ { \sf p } - \omega _ { \sf s } ) .$ . $\Delta I _ { \mathsf { p } }$ and $\Delta \mathfrak { h }$ represent the energy loss (i.e., stimulated Raman loss) at the pump beam and the energy gain (i.e., stimulated Raman gain) at Stokes beam before (solid curve) and after (dashed curve) interaction with the molecules, respectively. (b) Simulated SRS intensity when there is a focal length difference (Δf) between the pump beam of $\lambda _ { p } = 8 0 \dot { 0 }$ nm and the Stokes beam of $\lambda _ { S } = 1 0 4 0$ nm. The numerical aperture (NA) of the focusing lens is assumed to be 0.4. (c) Effects of Δf on SRS intensity (red curve) and axial resolution (blue curve). The axial resolution is defined as the full width at half maximum (FWHM) of the longitudinal SRS intensity profile in the focal region.

## II. EFFECT OF CHROMATIC ABERRATION ON SRS IMAGING

Using selected wavelengths of the ultrafast pump and Stokes pulses to match a Raman transition, CRS takes advantage of coherent processes to yield a significantly stronger signal than sponta neous Raman scattering spectroscopy.1 The pixel dwell time of CRS imaging could be as short as sub-microseconds to enable videorate chemical imaging.38 The pump and Stokes wavelength are defined by $\begin{array} { r } { \frac { 1 } { \lambda _ { p } } - \frac { 1 } { \lambda _ { S } } = \check { \Omega } _ { \nu i b } } \end{array}$ , where $\lambda _ { P }$ and λS are the wavelength of the pump and Stokes, respectively, and $\Omega _ { \nu i b }$ is the Raman transition of interest for a given specimen. Figure 1(a) illustrates that when the two laser pulses are focused on Raman-active molecules, three CRS processes occur. CARS light with a new redshifted frequency $\left( \omega _ { a s } \right)$ is generated and typically detected by a photomultiplier tube detector with a short-pass optical filter blocking the excitation beams.39 In addition, SRS involves the energy transfer from the laser to the molecules, leading to an intensity gain in the Stokes beam and to an intensity loss in the pump. The SRS signal can be extracted via a heterodyne detection approach that detects the subtle energy change in each beam.40 The energy loss at the pump beam and gain at Stokes beam are named stimulated Raman loss and stimulated Raman gain, respectively. Both SRS and CARS imaging provide chemical selectivity, whereas CARS has non-resonant backgrounds and spectral distortions that can be removed through multiple approaches, such as phase retrieval algorithms41,42 or frequency modulation.43

To effectively induce CRS processes, the pump and Stokes pulses need to be focused and overlap well temporally and spatially. Therefore, we designed a hybrid water-immersion achromatic metalens consisting of an α-silicon metasurface and an offthe-shelf miniature refractive lens (No. 43-397, Edmund Optics). Before we introduce the design of the hybrid metalens, we first illustrate how chromatic aberration affects the resolution and signal level in SRS imaging. We considered the pump and Stokes wavelengths of 800 and 1040 nm targeting at 2884 cm−1, respectively. These near-infrared wavelengths give less photodamage and deeper penetration depth in biological samples.2 To calculate SRS signal generation, we assumed that the pump and Stokes are Gaussian beams focused by a lens of $\mathrm { N A } = 0 . 4$ into a homogeneous dimethyl sulfoxide (DMSO) solution. The SRS signals originate from the overlapped region of the two foci. The SRS intensity along the lateral, r, and longitudinal, z, directions can be modeled as2

$$
I _ {S R S} (\boldsymbol {r}, \boldsymbol {z}) = C _ {0} \mathrm{Im} \Bigl (\chi^ {(3)} \Bigr) I _ {p} (\boldsymbol {r}, \boldsymbol {z}) I _ {S} (\boldsymbol {r}, \boldsymbol {z}),
$$

where $I _ { P } ( \mathbf { r } , \mathbf { z } )$ and $I _ { s } ( \mathbf { r } , \pmb { z } )$ are the intensities of the pump and Stokes beams, respectively; C0 is a constant; and Im $( \chi ^ { ( 3 ) } )$ is the imaginary part of the third-order nonlinear susceptibility $\chi ^ { ( 3 ) }$ of the sample. Figure 1(b) shows the cross section of the SRS intensity profiles when the focal length difference between the two beams is 0, 5, 10, and 15 μm. When the two foci are axially separated, the SRS intensity drops significantly. Fitting the SRS intensity profile along the longi tudinal direction with a Gaussian function, the blue curve in Fig. 1(c) shows that the SRS axial resolution degrades when the focal length difference increases. Next, we simulated a 1-μm polystyrene (PS) bead placed at the center of the SRS signal and investigated how its SRS intensity is affected by focal length differences. The total SRS signal from the bead is an integral of ISRS(r,z) over the bead volume. The simulated result given by the red curve in Fig. 1(c) shows that the SRS signal deteriorates dramatically due to chromatic aberration.

## III. PRINCIPLE AND DESIGN OF THE HYBRID WATER-IMMERSION ACHROMATIC METALENS

The key element of the hybrid water-immersion achromatic metalens (NA = 0.4, 1.5-mm diameter) is the metasurface possessing a phase profile illustrated in Fig. 2(a). Figure S1 shows the parameters of the metasurface and the refractive lens. We used raytracing software (ZEMAX OpticStudio, USA) to calculate phases and group delays of all incident rays and adjusted the phase pro file of the metasurface and the focal length of the hybrid metalens in such a way that all incident rays arrive at the focus with nearly the same phase and group delay.35 These calculations were performed at a wavelength of 904 nm corresponding to the midpoint of the pump and Stokes frequencies. The compensation of group delay leads to a parabolic focal length shift with incident wavelengths [see the red curve of Fig. 2(b)]. Without the metasurface, the plano–convex refractive lens has a focal length monoton ically increasing with wavelength [the blue curve of Fig. 2(b)]. In Fig. 2(c), the $\mathrm { W A F _ { R M S } }$ defined as the optical path difference between the wavefront and an ideal aberration-free wavefront (i.e., a reference spherical surface) with 0○, 1○, and $2 ^ { \circ }$ angles of incidence are shown for the cases with and without the metasurface. Not only is the chromatic focal length shift corrected for, but also other aberrations (spherical, coma, and astigmatism) are well-corrected within a field of view of $4 ^ { \circ } .$ A WAF smaller than 0.072λ is considered as a criterion for diffraction-limited performance.44 Considering that the effective focal length of the hybrid water-immersion metalens is 1.86 mm, the field of view covers an area of about $1 3 0 \times 1 3 0 \ \mu \mathrm { m } ^ { 2 }$ with diffraction-limited resolution.

![](images/388b8d8de407b419815cf9f10dc57f951d8a0b8395f8830c726648060d13fade.jpg)

<details>
<summary>line chart</summary>

| x-axis (mm) | Phase (rad) |
| ----------- | ----------- |
| -0.6        | 0.0π        |
| -0.4        | 2.0π        |
| -0.2        | 0.0π        |
| 0.0         | 2.0π        |
| 0.2         | 0.0π        |
| 0.4         | 2.0π        |
| 0.6         | 0.0π        |
</details>

![](images/52015f648624cae49f6c06c05cc98cff807698d90d90ce0a47c8fa0f32749a93.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | With metasurface | Without metasurface |
| --------------- | ---------------- | ------------------- |
| 750             | -2               | -28                 |
| 800             | 0                | -20                 |
| 850             | 2                | -15                 |
| 900             | 3                | -10                 |
| 950             | 3                | -5                  |
| 1000            | 2                | 0                   |
| 1050            | 1                | 2                   |
| 1100            | -1               | 3                   |
</details>

![](images/89ecb6e6d68a23c8406969a3440320e862ac3783e7457d18bd0f346953732eb4.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | With metasurface (0° incidence) | With metasurface (1° incidence) | With metasurface (2° incidence) | Without metasurface |
| --------------- | ------------------------------- | ------------------------------- | ------------------------------- | -------------------- |
| 750             | 0.09                            | 0.09                            | 0.12                            | 0.37                 |
| 800             | 0.04                            | 0.04                            | 0.06                            | 0.34                 |
| 850             | 0.04                            | 0.04                            | 0.04                            | 0.34                 |
| 900             | 0.04                            | 0.04                            | 0.04                            | 0.36                 |
| 950             | 0.04                            | 0.04                            | 0.04                            | 0.38                 |
| 1000            | 0.04                            | 0.04                            | 0.04                            | 0.41                 |
| 1050            | 0.05                            | 0.05                            | 0.06                            | 0.43                 |
| 1100            | 0.06                            | 0.06                            | 0.08                            | 0.44                 |
</details>

![](images/1d63eefeb60ea80248aa8d23d3b27f641c3620d0061546cb29c859b764e5c769.jpg)

<details>
<summary>scatterplot</summary>

| Point | Phase at 800 nm (rad) | Phase at 1040 nm (rad) |
|-------|------------------------|-------------------------|
| #1    | ~0.25                  | ~0.25                   |
| #2    | ~0.5                   | ~0.6                    |
| #3    | ~0.7                   | ~0.7                    |
| #4    | ~1.0                   | ~1.1                    |
| #5    | ~1.3                   | ~1.3                    |
| #6    | ~1.5                   | ~1.5                    |
| #7    | ~1.8                   | ~1.8                    |
| #8    | ~2.0                   | ~2.0                    |
</details>

![](images/c5609ebd9bc1eaefe8932a7d81a2b94edb6280fdac7a592cd03e29feec86b749.jpg)

<details>
<summary>natural_image</summary>

Microscopic surface texture with hexagonal patterns and a magnified inset showing nanoscale structures (no text or symbols)
</details>

![](images/cbd30253a1dc199dacc517408f065b58e7558fd767a4bc7005a109e0dc48fe25.jpg)

<details>
<summary>text_image</summary>

(f)
Vacuum
chuck
Refractive
lens'
Tape
Metasurfac
</details>

FIG. 2. Principle and design of a hybrid water-immersion achromatic metalens. (a) Calculated phase profile of the metasurface along the x-axis passing through the lens center. (b) Simulated focal shift and (c) root-mean-square of wavefront aberration function $( W A F _ { R M S } )$ with and without the metasurface. The red and brown curves show the $W A F _ { R M S }$ at $0 ^ { \circ } , 1 ^ { \circ } ,$ and $2 ^ { \circ }$ angle of incidence. (d) Designed nanostructures and their phase shifts for $\lambda _ { p } = 8 0 0$ nm and $\lambda _ { s } = 1 0 4 0$ nm and their transmission at $\lambda = 8 0 0$ nm (shown by colors). The inset illustrates the shape of eight α-silicon nanopillars. (e) Scanning electron microscopy (SEM) images from a region of the metasurface. Scale bar: 1 μm. The inset shows an oblique view (scale bar: 200 nm). (f) An image taken while aligning the metasurface to the refractive lens. Scale bar: 2 mm.

To implement the metasurface, we built an α-silicon nanostructure library consisting of different dimensions of square and cross-shaped nanopillars with 1-μm height. The simulations were carried out by a finite-difference time domain (FDTD) solver (Lumerical, USA) with a periodic boundary (unit cell is 350 $\times ~ 3 5 0 ~ \mathrm { n m } ^ { 2 } )$ . It is worth mentioning that the chosen eight nanopillars are along the $4 5 ^ { \circ }$ line in Fig. 2(d) so that the phase profile shown in Fig. 2(a) can be accurately implemented at both λ = 800 and 1040 nm to maintain high diffraction efficiency. The dimensions of the eight nanopillars are listed in Fig. S2. The metasurface was fabricated by e-beam lithography and dry etching following the same recipe reported in Ref. 45. The SEM images from a region of the fabricated metasurface are shown in Fig. 2(e). We assembled the metasurface and the refractive lens under an optical setup (see its schematic in Fig. S3). The refractive lens was held by a vacuum pickup system and moved to the center of the metasurface [Fig. 2(f)]. During this lateral alignment process, we first marked the center of the metasurface on a camera and then illuminated the refractive lens with a normally incident laser beam such that its focal spot could be seen on the camera. Subsequently, we slightly adjusted the refractive lens’ position until its focal spot on the camera overlapped with the previously marked center of the metasurface. Following this step, we vertically moved the refractive lens to about 20 μm above the metasurface and released the refractive lens. The refractive lens fell on a U-shaped 30-μm-thick double-sided tape (OCA8146-2, Thorlabs). The vacuum pick-up nozzle was used to slightly press the top of the refractive lens to ensure that the refractive lens stuck well to the tape.

## IV. CHARACTERIZATION OF THE HYBRID METALENS

After assembling the hybrid metalens, we built a vertical microscope for characterizing the point spread function (PSF) of the metalens [Fig. 3(a)]. We used a tunable supercontinuum laser (EXTREME from NKT Photonics, LLTF from Photon, etc.) with

5 nm linewidth. The incident beam was collimated by a reflec tive fiber collimator (RC02F2-P01, Thorlabs) and then focused by the hybrid metalens. The focus was imaged and magnified by a 40× water-immersion objective (LUMPLFLN 40XW, Olympus) and a tube lens (180 mm focal length) onto a camera (DCC1545M, Thorlabs). To obtain a three-dimensional (3D) point spread function (PSF), we sequentially image the focus by moving the hybrid metalens with a translational stage (MT1-Z8, Thorlabs) from z = −40 μm to z = +40 μm at 1 μm intervals and change the incident wavelength from 750 to 1100 nm at 10 nm intervals. Figure 3(b) shows the crosssectional views of the PSFs at the selected wavelengths for the hybrid metalens and the refractive lens only. The complete PSF images of the hybrid metalens at different wavelengths are shown in Fig. S4. The refractive lens shows spherical aberration and a focal length shift of 30 μm between 800 and 1040 nm, as seen by its long depth of focus and the movement of the peak intensity for each wavelength (Fig. S5), respectively. With the metasurface, the depth of focus becomes shallower and the focal length shift is significantly reduced to 1 μm. We further characterized and compared the FWHMs and Strehl ratios of the hybrid metalens as shown in Figs. 3(c) and 3(d), respectively. The FWHMs of the hybrid metalens are significantly reduced and close to the theoretical values [see the black solid line in Fig. 3(c)]. The Strehl ratios are improved over the whole wavelength range. We noticed that there is an ∼20-μm lateral misalignment (estimated by comparing the measured focal spot profile with simulation, see Fig. S6) between the metasurface and the refractive lens. This translates to an asymmetric focal spot profile leading to larger standard deviation in FWHM and Strehl ratios. Finally, the focusing efficiency was determined by taking the ratio of the focal spot power of the hybrid metalens to that of the refractive lens. The former was measured using the setup shown in Fig. 3(a) by placing a power meter and an iris in front of the camera. The iris had a diameter of about twice the diameter of the central Airy disk to filter out any background light. When measuring the transmitted power of the refractive lens, the iris was removed. The focusing efficiency of the hybrid metalens, as shown in Fig. 3(e), is wavelength-dependent due to the dispersive nature of the nanopillars.

## V. METALENS SRS MICROSCOPE AND ITS PERFORMANCE

We developed a metalens-based SRS microscope and characterized its focusing performance. The experimental setup is illustrated in Fig. 4(a). The laser source is a dual-output ultrafast laser (InSight DeepSee, Spectral-Physics) with a tunable pump beam from 680 to 1100 nm of ∼120 fs duration and a fixed Stokes beam of 1040 nm and ∼220 fs duration, both at 80 MHz repetition rate. The diameters of the output laser beams are about 1.1 mm. To detect the stimulated Raman loss signal, an acousto-optic modulator (AOM, M1250, Isomet) set at 3 MHz modulation frequency is installed at the focal plane of lenses L1 and L2 (both focal lengths are 100 mm) in the Stokes beam path. The pump beam passes through a motorized delay line stage used for adjusting the temporal overlap of pump and Stokes pulses. A short-pass dichroic mirror (ZT1064rdcsp, Chroma) is used to combine the two beams. The formation of SRS images is based on raster scanning of the laser focus steered by a pair of galvanometric mirrors (GVS202, Thorlabs). A pair of 200 mm lenses (L3 and L4) is used to conjugate the galvanometric mirrors and the hybrid metalens held by a 3D motorized stage. A sample is placed at the focal plane of the hybrid metalens. A 40× objective lens (LUMPLFLN 40XW, Olympus, Japan) with 0.8 NA is used to collect the light after the sample. A short-pass filter (No. 64-336, Edmund Optics) is employed to block the Stokes beam. A 30-mm lens is used to focus the pump light to a home-built photodiode (PD).46 The PD signal is sent to a lock-in amplifier (MFLI, Zurich Instruments, Switzerland) to demodulate the stimulated Raman loss signals at the pump beam. Before conducting SRS imaging, we used a resolution target to find the focal plane of the hybrid metalens and obtained clear scanning images over an area of 200 × 200 μm2 (Fig. S7). Tuning the pump to 798 mm, we used a pure

(a)  
![](images/527a359112d193569f10fb02f3f9043ee74187cf1903e5f539ed83f05308c5db.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  Laser --> Fiber
  Fiber --> Collimator
  Collimator --> Mirror
  Camera --> TubeLens["Tube Lens"]
  TubeLens --> Objective
  Objective --> n3DStage["3D stage"]
  n3DStage --> Metalens
  Metalens --> Z
  Metalens --> Y
  Metalens --> X
    style Laser fill:#f9f,stroke:#333
    style Colimator fill:#ccf,stroke:#333
    style Mirror fill:#cfc,stroke:#333
    style 3D stage fill:#ffc,stroke:#333
    style Tube Lens fill:#cfc,stroke:#333
    style Objective fill:#ffc,stroke:#333
    style Watercolor fill:#fcc,stroke:#333
```
</details>

(b)

![](images/460744ef624f5600449dad8b9bf10cd45e58c23f6b00ad52bb7252782a13f1b7.jpg)

<details>
<summary>heatmap</summary>

| Wavelength (nm) | Z (μm) Range | Value |
| --------------- | ------------ | ----- |
| 750             | -10 to 40    | ~0.8  |
| 800             | -10 to 40    | ~0.8  |
| 850             | -10 to 40    | ~0.8  |
| 900             | -10 to 40    | ~0.8  |
| 1040            | -10 to 40    | ~0.8  |
| 1100            | -10 to 40    | ~0.8  |
</details>

![](images/00e2ed0f8d3074e0b584aa6372c87fbed22c422e7bea7780379fd1eead6ad312.jpg)

<details>
<summary>heatmap</summary>

| Z (μm) | Value |
| ------ | ----- |
| -10    | Low   |
| 0      | Medium|
| 20     | High  |
| 30     | Medium|
| 40     | High  |
</details>

(c)  
![](images/aa0c71471da897742865572f5efb52def5c2f23511e55bdb294ca96b30cae773.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | W/ metasurface | W/o metasurface | Theory |
| --------------- | -------------- | --------------- | ------ |
| 750             | 1.0            | 1.9             | 1.0    |
| 800             | 1.2            | 1.7             | 1.1    |
| 850             | 1.3            | 1.8             | 1.2    |
| 900             | 1.4            | 1.9             | 1.3    |
| 950             | 1.4            | 2.0             | 1.4    |
| 1000            | 1.5            | 2.1             | 1.5    |
| 1050            | 1.5            | 2.2             | 1.6    |
| 1100            | 1.6            | 2.3             | 1.7    |
</details>

(d)  
![](images/2adb365feacb160fd7c5f2fa495e233ca3503afb5a9bf5bb8314da98d9fa0858.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | W/ metasurface | W/o metasurface |
| --------------- | -------------- | --------------- |
| 750             | 0.6            | 0.15            |
| 800             | 0.7            | 0.3             |
| 850             | 0.6            | 0.5             |
| 900             | 0.7            | 0.4             |
| 950             | 0.8            | 0.45            |
| 1000            | 0.85           | 0.4             |
| 1050            | 0.9            | 0.45            |
| 1100            | 0.7            | 0.35            |
</details>

(e)

![](images/e157c4c8f4e641b4a8f343bf9aae1d50742bde3328e92e35ef8d5829c3cc8e4b.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Focusing efficiency (%) |
| --------------- | ---------------------- |
| 750             | 36                     |
| 775             | 44                     |
| 800             | 41                     |
| 825             | 42                     |
| 850             | 45                     |
| 875             | 48                     |
| 900             | 50                     |
| 925             | 48                     |
| 950             | 46                     |
| 975             | 44                     |
| 1000            | 42                     |
| 1025            | 38                     |
| 1050            | 34                     |
| 1075            | 30                     |
| 1100            | 28                     |
</details>

FIG. 3. Characterization of the hybrid metalens. (a) Point spread function (PSF) measurement setup, (b) PSFs of the refractive lens with and without the metasurface, (c) FWHM of focus, (d) Strehl ratio of focus, and (e) focusing efficiency of the hybrid metalens, measured from λ = 750 to 1100 nm with 10 nm interval. The red and blue curves represent the measurements of the hybrid metalens with and without the metasurface, respectively. For each wavelength in (c) and (d), intensity profiles of the focal spot along horizontal, vertical, and diagonal directions were measured. An Airy disk function was then used to fit the measured intensity profiles to determine FWHMs and Strehl ratios. The average value of these quantities at each wavelength is shown in (c) and (d) as data points, with the standard deviation plotted as error bars. The black line in (c) is the theoretical FWHM of the focal spot calculated when NA = 0.4.

DMSO solution sample to optimize the SRS signal at C–H transition through adjusting the delay between two beams to ensure an optimal temporal match.

We compare the performance of the refractive lens with and without the metasurface by imaging a 1-μm PS bead (No.112, Phosphores Inc.) at a $3 0 6 0 ~ \mathrm { { c m } ^ { - 1 } }$ Raman shift. The bead sample was sandwiched between two cover glasses and placed at the focal plane of the lens. We imaged the bead by sequentially moving the lens from −45 to +45 μm along the z-axis to form a 3D imaging stack of the bead. The pixel dwell time was 10 μs. The power of the pump and Stokes beams measured before the hybrid metalens was 45 and 130 mW, respectively. Figures 4(b)–4(e) show the

![](images/babfe25de4f6cb8e13b1f2c9f73cd1981c8bb09b8ac208ea431565529bef37ed.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Pulsed laser"] --> B["Pump"]
  B --> C["DM"]
  C --> D["Galvo mirrors"]
  D --> E["PD"]
  D --> F["Filter"]
  D --> G["L5"]
  D --> H["OBJ"]
  D --> I["Metalens"]
  I --> J["L4"]
  J --> K["L1"]
  K --> L["AOM"]
  L --> M["L2"]
  M --> N["Stokes"]
  N --> O["Pulse stage"]
```
</details>

![](images/9ed60cb68b04fdf7d769e0953a96348596447195167638064c7af9a4bb52beb1.jpg)

<details>
<summary>line chart</summary>

| X (μm) | SRS norm. int. (a.u.) |
| ------ | --------------------- |
| -4     | ~0.1                  |
| -2     | ~0.3                  |
| 0      | 1.0                   |
| 2      | ~0.3                  |
| 4      | ~0.1                  |
</details>

![](images/9aaabd2703a4313618cf55be4a376b3d85b6952069a23bb017b1264653f3cf88.jpg)

<details>
<summary>line chart</summary>

| X (μm) | SRS norm. int. (a.u.) |
| ------ | --------------------- |
| -4.0   | 0.0                   |
| -3.0   | 0.1                   |
| -2.0   | 0.3                   |
| -1.0   | 0.6                   |
| 0.0    | 0.9                   |
| 1.0    | 0.7                   |
| 2.0    | 0.4                   |
| 3.0    | 0.1                   |
| 4.0    | 0.0                   |
</details>

![](images/12f844fd34c54bf03a6419774a8f5ee7adfffdaca2492a19f432aafc8a5e9ad4.jpg)

<details>
<summary>line chart</summary>

| Z (μm) | SRS norm. int. (a.u.) |
| ------ | --------------------- |
| -20    | 0.1                   |
| -10    | 0.3                   |
| 0      | 1.0                   |
| 10     | 0.3                   |
| 20     | 0.1                   |
</details>

![](images/dbf0547a28a8f6099ef10d2fafa8cacf509faec22a1ad8dd7ead61947158aef6.jpg)

<details>
<summary>line chart</summary>

| Z (μm) | SRS norm. int. (a.u.) |
| ------ | --------------------- |
| -40    | 0.1                   |
| -20    | 0.5                   |
| 0      | 1.0                   |
| 20     | 0.5                   |
| 40     | 0.1                   |
</details>

FIG. 4. A metalens SRS microscope and its imaging performance. (a) Schematic. AOM: acousto-optic modulator; L: lens; OBJ: objective lens; PD: photodiode; DM: dichroic mirror; M: mirror. (b)–(e) Performance comparison between the hybrid metalens and refractive lens (i.e., without the metasurface) by imaging a 1-μm polystyrene bead at 3060 $\mathsf { c m } ^ { - 1 }$ Raman shift. (b) and (c) are the intensity profiles along the x-direction, and their inset images are the x–y cross section view of the bead. (d) and (e) are the intensity profiles along the z-direction, and their inset images are the x–z cross section view of the bead. All solid curves are fitted with a Gaussian function. δx and δz are the FWHM of the fitted curves and defined as the lateral and axial resolutions, respectively. All scale bars in the inset images are 5 μm.

x–y and x–z cross section views of the bead and its lateral and axial intensity profiles, respectively. For the refractive lens assembled with the metasurface, the FWHMs along the x- and z-directions [Figs. 4(b) and 4(d)] are 2.2 and 12.0 μm, respectively. In contrary, in the case of the refractive lens alone (i.e., without the metasurface), the FWHMs along the x- and z-directions [Figs. 4(c) and 4(e)] are 2.8 and 45.6 μm, respectively. The results indicate that both lateral and axial resolutions are significantly improved by the metasurface that corrects both chromatic and spherical aberrations.

## VI. METALENS CRS IMAGING OF THE MIXED POLYMER BEADS

Spectroscopic CRS imaging is able to map and differentiate different chemicals on a sample with high imaging speed. Here, we demonstrate that the hybrid metalens enables spectroscopic SRS and CARS imaging. Employing a spectral focusing approach,47 we equally linearly chirped the femtosecond pump and Stokes pulses by placing a 30-cm SF 57 glass rod in the combined path and an additional 15-cm one in the Stokes path (see Fig. S8 for the modified schematic setup). By sweeping the time delay between the two chirped pulses (the pump and Stokes wavelengths were set at 798 and 1040 nm, respectively) with a motorized translational stage, the system can scan the Raman shifts from 2850 to 3100 cm 1 to form a spectroscopic imaging stack.47 Applying a spectral unmixing algorithm,48 Fig. 5(a) illustrates that the two kinds of beads are differentiated based on their characteristic Raman peaks (i.e., PMMA: $2 9 5 5 ~ \mathrm { c m } ^ { - 1 }$ and PS: $3 0 6 0 ~ \mathrm { c m } ^ { - 1 } )$ as indicated in $\mathrm { F i g . } ~ 5 ( \mathrm { b } )$ . Subsequently, we demonstrated the hybrid metalens for backward (epi-)CARS imaging by modifying the setup (see Fig. S8), where a dichroic mirror (Chroma) is installed before the hybrid metalens to reflect the newly generated anti-Stokes light to a photomultiplier tube detector (Hamamatsu). For CRS endoscopes that collect the backscatter photons with a double-clad fiber15 or multicore fiber,16 CARS imaging may be preferable as the anti-Stokes light with a shorter wavelength $( \mathrm { i . e . , } \lambda _ { a s } = 6 4 7$ nm at 2884 $\mathrm { c m } ^ { - 1 } )$ enables more multi-scattering events to bounce back photons from the tissues. Figures 5(c) and $5 ( \mathrm { d } )$ show the epi-CARS images of PS and PMMA beads and their spectra, respectively. The distortion of the spectra is due to the non-resonant background in CARS imaging and can be corrected using phase retrieval algorithms.37,38

![](images/918db84f8e2d5dd5c6c3545c519adad749abae071b4641f4e6beb5032eb4a2a4.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red and green labeled cells, scale bar 5 μm (no text or symbols beyond label)
</details>

![](images/fc316fe0e990fe25e0255a8b18bc99a9721de2059fee11ce3920636211843603.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | PS     | PMMA   |
| ----------------- | ------ | ------ |
| 2850              | 0.0    | 0.0    |
| 2900              | 0.4    | 0.1    |
| 2950              | 0.3    | 1.0    |
| 3000              | 0.4    | 0.3    |
| 3050              | 1.0    | 0.1    |
| 3100              | 0.0    | 0.0    |
</details>

![](images/3c41f55c8188dd6503488f10ecc24d3327ba0f580cc38924d6e0de252800f91f.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing Epi-CARS-labeled cells with red and green signals (no text or symbols)
</details>

![](images/132f24bf75f9fad2bece4db128d389b7952ba5c886b09c275f43e33840b5935c.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | PS    | PMMA  |
| ----------------- | ----- | ----- |
| 2850              | 0.1   | 0.05  |
| 2900              | 0.8   | 0.4   |
| 2950              | 0.7   | 0.9   |
| 3000              | 1.0   | 0.6   |
| 3050              | 0.3   | 0.1   |
| 3100              | 0.0   | 0.0   |
</details>

FIG. 5. Metalens SRS and CARS imaging of mixed 3-μm polymethyl methacrylate (PMMA) and 2-μm polystyrene (PS) beads. (a) SRS images and (b) spectra of PMMA (green) and PS beads (red) at the forward detection mode. (c) CARS images and (d) spectra of PMMA (green) and PS beads (red) in the backward (epi-)detection mode. Scale bars are $5 \mu \mathsf { m }$

## VII. METALENS CRS IMAGING OF LIPID CONTENT IN AN EX VIVO MOUSE EAR

Next, we demonstrate that the hybrid metalens enables depth resolved chemical imaging of mouse ear tissue in both the forward SRS and epi-CARS modes. In the C–H vibrational region (2800–3100 cm−1), chemicals such as lipids, proteins, and deoxyribonucleic (DNA) are distinguished based on their Raman spectra.2,7 Mapping of lipids and the ratio of lipid-to-protein in lesions by CRS imaging is a rapid and label-free diagnostic approach for atheromatous disease2 and brain cancer.13 The mouse ear tissue was har vested from a euthanized 8-week-old nude mouse (Boston University Charles River Laboratory) and flattened with a drop of pure water on a coverslip, which was placed on the focal plane of the hybrid metalens. As shown in Fig. 6, the brighter signal in the images represents the lipid-rich region in the cells. The grooves between cells where less lipid concentrated show lower C–H Raman signals. In the supplementary material, videos 1 and 2 show the volumetric SRS and CARS images taken by moving the hybrid metalens from $\mathrm { Z } = - 3 0 \mathrm { t o } + 3 0 \mu \mathrm { m } .$ .

## VIII. VOLUMETRIC SRS IMAGING THROUGH THE METALENS

Finally, we investigated the performance of the hybrid metal ens in volumetric PMMA bead and ovarian cancer tissue samples. We compared the z-resolution for cases with and without the metasurface. The PMMA bead sample was prepared by 10 μm PMMA beads (Phosphores Inc.) dispersed in 1% agarose gel. A droplet from the gel was sandwiched by two cover glasses with a spacer of doublesided tape (Cat.3136, 3M). The hybrid metalens sequentially imaged the bead sample at different depths at $2 9 5 5 ~ \mathrm { c m } ^ { - 1 }$ Raman shift. The pixel dwell time was 10 μs. Figure 7(a) shows that the hybrid metalens clearly differentiates the beads located at different depths. In comparison, Fig. 7(b) shows that the refractive lens (i.e., without metasurface) barely resolves the beads located at different depths because of its elongated depth of focus. In the supplementary material, videos 3 and 4 show their complete volumetric images from $\mathrm { ~ Z ~ = ~ - 4 0 ~ t o ~ } { + 4 0 }$ μm with 2 μm interval. Note that Figs. 7(a) and 7(b) were obtained from the same sample but at different positions because a realignment is required after changing the hybrid metalens and the refractive lens. We then used the hybrid metalens to image the ovarian cancer tissue at $2 9 0 0 { \mathrm { c m } } ^ { - 1 }$ Raman shift. Such cancer tissue has a complex, three-dimensional lipid structure for showcasing the axial resolution. The tissue sample with 80 μm thickness was sliced from a patient-derived xenograft.49 The power of pump and Stokes beams before the hybrid metalens was 45 and 250 mW. The pixel dwell time was 50 μs. In Fig. 7(c), one can see that lipid droplets (bright spots in the images) at different depths can be resolved while moving the hybrid metalens by 10 μm steps. In contrary, in Fig. 7(d), images obtained from different depths are similar and the boundary of lipid droplet is vague (see the area outlined by the white dashed line). The ability to resolve accumulated lipid droplets in cancer tissue holds potential for cancer diagnosis.5,6

![](images/8787a62762985d0a25d06e74ce1535f04b5579bdc6ecb2e00aa65be826dd4dcc.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-stained cellular structures under forward-SRS imaging (no text or symbols)
</details>

![](images/578e595644b9e2b477c116062f3e43b7069c0de222774f1e71c21099e358d5b5.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of Epi-CARS imaging showing cellular structures (no text or symbols)
</details>

FIG. 6. Metalens-based CRS imaging of lipid content in an ex vivo mouse ear. (a) Forward SRS image and (b) epi-detected CARS image at 2884 cm−1. Scale bar: 50 μm.

![](images/82cf23c50d5b80d70c374e4e1c1e6a72a886f1558caa5f54d483695c8b50e193.jpg)  
FIG. 7. Performance of the hybrid metalens in volumetric SRS imaging PMMA bead and ovarian cancer tissue samples. (a) and (b) are images from the sample of 10 μm PMMA beads imaged (2955 cm−1 Raman shift) by the hybrid metalens and refractive lens, respectively. Different depths are labeled. (c) and (d) Ovarian cancer tissue imaged at 2900 cm−1 Raman shift by the hybrid metalens and refractive lens, respectively. The bright spots are lipid droplets. Scale bars are 40 μm.

## IX. DISCUSSION

We have designed and fabricated a hybrid achromatic waterimmersion metalens for CRS imaging. The hybrid metalens comprises a low-cost 2-mm-diameter plano–convex lens and a 1.5-mm-diameter metasurface consisting of 1-μm-height α-silicon nanopillars. The metasurface was designed and characterized to have nearly diffraction-limited focal spots from λ = 800 to 1040 nm, matching typical Raman transitions with a Strehl ratio of >0.7. After verifying the hybrid metalens’ improved focal spot size and depth of focus by the point spread function measurement, we demonstrated the capability of the hybrid metalens in spectroscopic and volumetric CRS imaging of bead and tissue samples, showcasing its promising potential for miniature endoscopic CRS imaging.

Further desired improvements include increasing the focusing efficiency of the hybrid lens. The fabricated hybrid metalens in this manuscript has about 50% peak measured focusing efficiency, which is lower than about the 92% from simulations (Fig. S9). The rest of the transmitted light either goes toward the secondary foci or back ground light. We attribute the difference between experiment and simulation to the tapered sidewall of the α-silicon nanopillar due to deep dry etching, as seen in the inset of Fig. 2(e). Our previous study suggests that a 4○ tapering introduces a significant phase error of ∼150○ when a nanopillar’s diameter is 220 nm.50 This tapering effect may be reduced by fine tuning the ratio of etching gases to the substrate temperature.

An emerging design of miniature CRS imaging probe is based on fiber scanning.15 In these setups, the facet of a fiber is held and steered by a piezoelectric tube in a circular or Lissajous scanning pattern. Since the light from the fiber tip is divergent, an endoscopic imaging system usually requires a collimating lens and a miniature objective to form a finite-conjugated system that relays the laser focus from the fiber tip to the sample. The current hybrid metalens was designed as an infinite-conjugate lens, i.e., focusing a collimated beam to a spot. It is possible to design a finite conjugate metalens that focuses light from a fiber to a sample with a single element.51 This can further reduce the footprint of a hybrid metalens compared to the systems using only refractive elements.

## SUPPLEMENTARY MATERIAL

See the supplementary material for details of the design parameters of the hybrid metalens and nanostructures, optical setup for assembling the metasurface and refractive lens, measured focal length shift, measured and simulated focal spot profiles to estimate lateral alignment error, scanning transmitted images with the hybrid metalens, detailed schematic setup for the spectroscopic SRS and epi-CARS microscope, simulation of a metasurface optimized for λ = 800 and 1040 nm, volumetric SRS and CARS images of mouse ear tissues in supplementary videos 1 and 2 , and volumetric imaging of PMMA beads and ovarian cancer tissues in supplementary video 3 and 4.

## AUTHORS’ CONTRIBUTIONS

P.L. and W.T.C. contributed equally to this work.

## ACKNOWLEDGMENTS

We thank Dr. Jiayingzi Wu for preparing the mouse ear sample, Yuying Tan for preparing the cancer tissue samples, Joon-Suh Park for taking SEM images of the metasurface, and Dr. Cheng Zong for helpful discussion on CARS imaging.

This work was supported by NSF Grant Nos. CHE1807106 and NIH R35GM136223 (J.-X.C.) and DARPA Grant No. HR00111810001 (F.C.). This work was performed, in part, at the Center for Nanoscale Systems (CNS), a member of the National Nanotechnology Coordinated Infrastructure (NNCI), which is supported by the National Science Foundation under NSF Award No. 1541959. CNS is a part of Harvard University.

The authors declare no conflicts of interest.

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding authors upon reasonable request.

## REFERENCES

1J.-X. Cheng and X. S. Xie, “Vibrational spectroscopic imaging of living systems: An emerging platform for biology and medicine,” Science 350(6264), aaa8870 (2015).  
2C. Zhang, D. Zhang, and J.-X. Cheng, “Coherent Raman scattering microscopy in biology and medicine,” Annu. Rev. Biomed. Eng. 17, 415–445 (2015).  
3M. T. Cicerone and C. H. Camp, “Histological coherent Raman imaging: A prognostic review,” Analyst 143(1), 33–59 (2018).  
4F. Hu, L. Shi, and W. Min, “Biological imaging of chemical bonds by stimulated Raman scattering microscopy,” Nat. Methods 16(9), 830–842 (2019).  
5S. Yue, J. Li, S.-Y. Lee, H. J. Lee, T. Shao, B. Song, L. Cheng, T. A. Masterson, X. Liu, T. L. Ratliff, and J.-X. Cheng, “Cholesteryl ester accumulation induced by PTEN loss and PI3K/AKT activation underlies human prostate cancer aggressiveness,” Cell Metab. 19(3), 393–406 (2014).  
6F.-K. Lu, D. Calligaris, O. I. Olubiyi, I. Norton, W. Yang, S. Santagata, X. S. Xie, A. J. Golby, and N. Y. R. Agar, “Label-free neurosurgical pathology with stimulated Raman imaging,” Cancer Res. 76(12), 3451–3462 (2016).  
7M. Lee, C. S. Herrington, M. Ravindra, K. Sepp, A. Davies, A. N. Hulme, and V. G. Brunton, “Recent advances in the use of stimulated Raman scattering in histopathology,” Analyst 146(3), 789–802 (2021).  
8Y. Ozeki, W. Umemura, Y. Otsuka, S. Satoh, H. Hashimoto, K. Sumimura, N. Nishizawa, K. Fukui, and K. Itoh, “High-speed molecular spectral imaging of tissue with stimulated Raman scattering,” Nat. Photonics 6(12), 845–851 (2012).  
9L. Shi, C. Zheng, Y. Shen, Z. Chen, E. S. Silveira, L. Zhang, M. Wei, C. Liu, C. de Sena-Tomas, K. Targoff, and W. Min, “Optical imaging of metabolic dynamics in animals,” Nat. Commun. 9(1), 2995 (2018).  
10J. Li, P. Lin, Y. Tan, and J.-X. Cheng, “Volumetric stimulated Raman scattering imaging of cleared tissues towards three-dimensional chemical histopathology,” Biomed. Opt. Express 10(8), 4329–4339 (2019).  
11M. Ji, D. A. Orringer, C. W. Freudiger, S. Ramkissoon, X. Liu, D. Lau, A. J. Golby, I. Norton, M. Hayashi, N. Y. R. Agar, G. S. Young, C. Spino, S. Santagata, S.  
Camelo-Piragua, K. L. Ligon, O. Sagher, and X. S. Xie, “Rapid, label-free detection of brain tumors with stimulated Raman scattering microscopy,” Sci. Transl. Med. 5(201), 201ra119 (2013).  
12W. J. Tipping, M. Lee, A. Serrels, V. G. Brunton, and A. N. Hulme, “Stimulated Raman scattering microscopy: An emerging tool for drug discovery,” Chem. Soc. Rev. 45(8), 2075–2089 (2016).  
13T. C. Hollon, B. Pandian, A. R. Adapa, E. Urias, A. V. Save, S. S. S. Khalsa, D. G. Eichberg, R. S. D’Amico, Z. U. Farooq, S. Lewis, P. D. Petridis, T. Marie, A. H. Shah, H. J. L. Garton, C. O. Maher, J. A. Heth, E. L. McKean, S. E. Sullivan, S. L. Hervey-Jumper, P. G. Patil, B. G. Thompson, O. Sagher, G. M. McKhann II, R. J. Komotar, M. E. Ivan, M. Snuderl, M. L. Otten, T. D. Johnson, M. B. Sisti, J. N. Bruce, K. M. Muraszko, J. Trautman, C. W. Freudiger, P. Canoll, H. Lee, S. Camelo-Piragua, and D. A. Orringer, “Near real-time intraoperative brain tumor diagnosis using stimulated Raman histology and deep neural networks,” Nat. Med. 26(1), 52–58 (2020).  
14C.-S. Liao, P. Wang, C. Y. Huang, P. Lin, G. Eakins, R. T. Bentley, R. Liang, and J.-X. Cheng, “In vivo and in situ spectroscopic imaging by a handheld stimulated Raman scattering microscope,” ACS Photonics 2017, 5 (3), 947–954.  
15A. Lombardini, V. Mytskaniuk, S. Sivankutty, E. R. Andresen, X. Chen, J. Wenger, M. Fabert, N. Joly, F. Louradour, A. Kudlinski, and H. Rigneault, “Highresolution multimodal flexible coherent Raman endoscope,” Light: Sci. Appl. 7, 10 (2018).  
16A. Lukic, S. Dochow, H. Bae, G. Matz, I. Latka, B. Messerschmidt, M. Schmitt, and J. Popp, “Endoscopic fiber probe for nonlinear spectroscopic imaging,” Optica 4(5), 496 (2017).  
17R. Mittal, M. Balu, P. Wilder-Smith, and E. O. Potma, “Achromatic miniature lens system for coherent Raman scattering microscopy,” Biomed. Opt. Express 4(10), 2196–2206 (2013).  
18M. Abramowitz, K. R. Spring, H. E. Keller, and M. W. Davidson, “Basic principles of microscope objectives,” BioTechniques 33(4), 772–781 (2002).  
19W. M. Lee and S. H. Yun, “Adaptive aberration correction of GRIN lenses for confocal endomicroscopy,” Opt. Lett. 36(23), 4608–4610 (2011).  
20H. Pahlevaninezhad, M. Khorasaninejad, Y.-W. Huang, Z. Shi, L. P. Hariri, D. C. Adams, V. Ding, A. Zhu, C.-W. Qiu, F. Capasso, and M. J. Suter, “Nanooptic endoscope for high-resolution optical coherence tomography in vivo,” Nat. Photonics 12(9), 540–547 (2018).  
21M. Khorasaninejad, W. T. Chen, R. C. Devlin, J. Oh, A. Y. Zhu, and F. Capasso, “Metalenses at visible wavelengths: Diffraction-limited focusing and subwavelength resolution imaging,” Science 352(6290), 1190–1194 (2016).  
22E. Arbabi, J. Li, R. J. Hutchins, S. M. Kamali, A. Arbabi, Y. Horie, P. Van Dorpe, V. Gradinaru, D. A. Wagenaar, and A. Faraon, “Two-photon microscopy with a double-wavelength metasurface objective lens,” Nano Lett. 18(8), 4943–4948 (2018).  
23Q. Guo, Z. Shi, Y.-W. Huang, E. Alexander, C.-W. Qiu, F. Capasso, and T. Zickler, “Compact single-shot metalens depth sensors inspired by eyes of jumping spiders,” Proc. Natl. Acad. Sci. U. S. A. 116(46), 22959–22965 (2019).  
24A. L. Holsteen, D. Lin, I. Kauvar, G. Wetzstein, and M. L. Brongersma, “A lightfield metasurface for high-resolution single-particle tracking,” Nano Lett. 19(4), 2267–2271 (2019).  
25R. J. Lin, V.-C. Su, S. Wang, M. K. Chen, T. L. Chung, Y. H. Chen, H. Y. Kuo, J.-W. Chen, J. Chen, Y.-T. Huang, J.-H. Wang, C. H. Chu, P. C. Wu, T. Li, Z. Wang, S. Zhu, and D. P. Tsai, “Achromatic metalens array for full-colour lightfield imaging,” Nat. Nanotechnol. 14(3), 227–231 (2019).  
26S. Divitt, W. Zhu, C. Zhang, H. J. Lezec, and A. Agrawal, “Ultrafast optical pulse shaping using dielectric metasurfaces,” Science 364(6443), 890–894 (2019).  
27N. A. Rubin, G. D’Aversa, P. Chevalier, Z. Shi, W. T. Chen, and F. Capasso, “Matrix Fourier optics enables a compact full-Stokes polarization camera,” Science 365(6448), eaax1839 (2019).  
28P. Lalanne, S. Astilean, P. Chavel, E. Cambril, and H. Launois, “Design and fabrication of blazed binary diffractive elements with sampling periods smaller than the structural cutoff,” J. Opt. Soc. Am. A 16(5), 1143–1156 (1999).  
29W. T. Chen, A. Y. Zhu, and F. Capasso, “Flat optics with dispersion-engineered metasurfaces,” Nat. Rev. Mater. 5(8), 604–620 (2020).  
30M. Decker, W. T. Chen, T. Nobis, A. Y. Zhu, M. Khorasaninejad, Z. Bharwani, F. Capasso, and J. Petschulat, “Imaging performance of polarization-insensitive metalenses,” ACS Photonics 6(6), 1493–1499 (2019).  
31T. Phan, D. Sell, E. W. Wang, S. Doshay, K. Edee, J. Yang, and J. A. Fan, “Highefficiency, large-area, topology-optimized metasurfaces,” Light: Sci. Appl. 8(1), 48 (2019).  
32W. T. Chen, A. Y. Zhu, V. Sanjeev, M. Khorasaninejad, Z. Shi, E. Lee, and F. Capasso, “A broadband achromatic metalens for focusing and imaging in the visible,” Nat. Nanotechnol. 13(3), 220–226 (2018).  
33S. Wang, P. C. Wu, V.-C. Su, Y.-C. Lai, M.-K. Chen, H. Y. Kuo, B. H. Chen, Y. H. Chen, T.-T. Huang, J.-H. Wang, R.-M. Lin, C.-H. Kuan, T. Li, Z. Wang, S. Zhu, and D. P. Tsai, “A broadband achromatic metalens in the visible,” Nat. Nanotechnol. 13(3), 227–232 (2018).  
34E. Arbabi, A. Arbabi, S. M. Kamali, Y. Horie, and A. Faraon, “Controlling the sign of chromatic dispersion in diffractive optics with dielectric metasurfaces,” Optica 4(6), 625–632 (2017).  
35W. T. Chen, A. Y. Zhu, J. Sisler, Y.-W. Huang, K. M. A. Yousef, E. Lee, C.-W. Qiu, and F. Capasso, “Broadband achromatic metasurface-refractive optics,” Nano Lett. 18(12), 7801–7808 (2018).  
36W. T. Chen, A. Y. Zhu, M. Khorasaninejad, Z. Shi, V. Sanjeev, and F. Capasso, “Immersion meta-lenses at visible wavelengths for nanoscale imaging,” Nano Lett. 17(5), 3188–3194 (2017).  
37H. Liang, Q. Lin, X. Xie, Q. Sun, Y. Wang, L. Zhou, L. Liu, X. Yu, J. Zhou, T. F. Krauss, and J. Li, “Ultrahigh numerical aperture metalens at visible wavelengths,” Nano Lett. 18(7), 4460–4466 (2018).  
38B. G. Saar, C. W. Freudiger, J. Reichman, C. M. Stanley, G. R. Holtom, and X. S. Xie, “Video-rate molecular imaging in vivo with stimulated Raman scattering,” Science 330(6009), 1368–1370 (2010).  
39J.-X. Cheng and X. S. Xie, “Coherent anti-Stokes Raman scattering microscopy: Instrumentation, theory, and applications,” J. Phys. Chem. B 108(3), 827–840 (2004).  
40C. W. Freudiger, W. Min, B. G. Saar, S. Lu, G. R. Holtom, C. He, J. C. Tsai, J. X. Kang, and X. S. Xie, “Label-free biomedical imaging with high sensitivity by stimulated Raman scattering microscopy,” Science 322(5909), 1857–1861 (2008).  
41C. H. Camp, Jr., Y. J. Lee, and M. T. Cicerone, “Quantitative, comparable coherent anti-Stokes Raman scattering (CARS) spectroscopy: Correcting errors in phase retrieval,” J. Raman Spectrosc. 47(4), 408–415 (2016).  
42R. Houhou, P. Barman, M. Schmitt, T. Meyer, J. Popp, and T. Bocklitz, “Deep learning as phase retrieval tool for CARS spectra,” Opt. Express 28(14), 21002–21024 (2020).  
43F. Ganikhanov, C. L. Evans, B. G. Saar, and X. S. Xie, “High-sensitivity vibrational imaging with frequency modulation coherent anti-Stokes Raman scattering (FM CARS) microscopy,” Opt. Lett. 31(12), 1872–1874 (2006).  
44A. Maréchal, “Mechanical integrator for studying the distribution of light in the optical image,” J. Opt. Soc. Am. 37(5), 403\_1–404 (1947).  
45M. Khorasaninejad, W. T. Chen, J. Oh, and F. Capasso, “Super-dispersive offaxis meta-lenses for compact high resolution spectroscopy,” Nano Lett. 16(6), 3732–3737 (2016).  
46M. N. Slipchenko, R. A. Oglesbee, D. Zhang, W. Wu, and J.-X. Cheng, “Heterodyne detected nonlinear optical imaging in a lock-in free manner,” J. Biophotonics 5(10), 801–807 (2012).  
47D. Fu, G. Holtom, C. Freudiger, X. Zhang, and X. S. Xie, “Hyperspectral imaging with stimulated Raman scattering by chirped femtosecond lasers,” J. Phys. Chem. B 117(16), 4634–4640 (2013).  
48L. Zhang, L. Shi, Y. Shen, Y. Miao, M. Wei, N. Qian, Y. Liu, and W. Min, “Spectral tracing of deuterium for imaging glucose metabolism,” Nat. Biomed. Eng. 3(5), 402–413 (2019).  
49J. Li, Y. Tan, G. Zhao, K.-C. Huang, H. Cardenas, D. Matei, and J.- X. Cheng, “Metabolic reprogramming from glycolysis to fatty acid uptake and beta-oxidation in platinum-resistant cancer cells,” bioRxiv:444564v1 (2021).  
50M. Khorasaninejad, A. Y. Zhu, C. Roques-Carmes, W. T. Chen, J. Oh, I. Mishra, R. C. Devlin, and F. Capasso, “Polarization-insensitive metalenses at visible wavelengths,” Nano Lett. 16(11), 7229–7234 (2016).  
51A. Arbabi, Y. Horie, A. J. Ball, M. Bagheri, and A. Faraon, “Subwavelength-thick lenses with high numerical apertures and large efficiency based on high-contrast transmitarrays,” Nat. Commun. 6(1), 7069 (2015).