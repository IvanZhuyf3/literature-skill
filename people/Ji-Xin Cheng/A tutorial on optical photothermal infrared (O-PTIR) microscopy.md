TUTORIAL | SEPTEMBER 13 2024

# A tutorial on optical photothermal infrared (O-PTIR) microscopy

Special Collection: Mid-IR Photonics

Craig B. Prater  ; Mustafa Kansiz; Ji-Xin Cheng

![](images/ebcbaa22df49db50a15c94ee9d5f91820e65786a079021c46c8a6cff51cbd6c6.jpg)

Check for updates

APL Photonics 9, 091101 (2024)

https://doi.org/10.1063/5.0219983

![](images/d2ce8a2f5d816904a8d34890bdb2d338cf9c870d22a74b7efb7b6577e0351c0a.jpg)  
View Online

![](images/c6fa52a373f0994aff110d87e41ff8dd3e08b5ca6c2c984216bcb7a3db73a0c1.jpg)  
Export Citation

## Articles You May Be Interested In

Application of optical photothermal infrared spectroscopy (O-PTIR) for future returned Mars samples

Rev. Sci. Instrum. (August 2025)

Theory of infrared nanospectroscopy by photothermal induced resonance

J. Appl. Phys. (June 2010)

Concurrent surface enhanced infrared and Raman spectroscopy with single molecule sensitivity

Rev. Sci. Instrum. (February 2023)

![](images/1d3031f5bf2d8f18e73cc61d40ce3cc24ace252c0418648eb38c5f0eceb7bd7e.jpg)

<details>
<summary>natural_image</summary>

Abstract digital artwork with flowing blue light streaks on black background, no text or symbols present
</details>

## AIP Advances

Why Publish With Us?

![](images/68d2494369a753b9ebbbc8975559fe81a71238d8317fd41c43e0cbf2dee72746.jpg)  
21DAYS average time to 1 st decision

![](images/ec6b0d8cf9be989a09fe82ab96a5f1c1029242a9699bd36a7a0d19ce81598666.jpg)  
OVER 4 MILLION views in the last year

![](images/1738ab599e48ce50df1c28a1dd98b4e47cb44b9e6fe6a7f4d2082073e075351b.jpg)  
INCLUSIVE scope

Learn More

![](images/fee7664c0cda7a733f9711b7b8bd281b1847f52e9c8f2cd1c08d9e910d0d79fc.jpg)  
AIP Publishing

# A tutorial on optical photothermal infrared (O-PTIR) microscopy

Cite as: APL Photon. 9, 091101 (2024); doi: 10.1063/5.0219983 Submitted: 21 May 2024 • Accepted: 1 August 2024 • Published Online: 13 September 2024

![](images/dd43a6c46442f42e840a173358be1d5895065fdd560360e898afa051555a08f0.jpg)

![](images/8d98389a8ff93be1c794dba02342caa3a8b06308fa664915842a5b3da8a873d4.jpg)

![](images/99310deb5595f63ae68f33d1e6dae0dd46172dde46b7237e53efe44eb45d6e33.jpg)

Craig B. Prater,1,a) Mustafa Kansiz,1 and Ji-Xin Cheng

## AFFILIATIONS

1 Photothermal Spectroscopy Corporation, Santa Barbara, California 93111, USA  
2Photonics Center, Boston University, Boston, Massachusetts 02215, USA  
Note: This paper is part of the APL Photonics Special Topic on Mid-IR Photonics.  
a)Author to whom correspondence should be addressed: craig@photothermal.com

## ABSTRACT

This tutorial reviews the rapidly growing field of optical photothermal infrared (O-PTIR) spectroscopy and chemical imaging. O-PTIR is an infrared super-resolution measurement technique where a shorter wavelength visible probe is used to measure and map infrared (IR) absorption with spatial resolution up to 30× better than conventional techniques such as Fourier transform infrared and direct IR laser imaging systems. This article reviews key limitations of conventional IR instruments, the O-PTIR technology breakthroughs, and their origins that have overcome the prior limitations. This article also discusses recent developments in expanding multi-modal O-PTIR approaches that enable complementary Raman spectroscopy and fluorescence microscopy imaging, including wide-field O-PTIR imaging with fluorescencebased detection of IR absorption. Various practical subjects are covered, including sample preparation techniques, optimal measurement configurations, use of IR tags/labels and techniques for data analysis, and visualization. Key O-PTIR applications are reviewed in many areas, including biological and biomedical sciences, environmental and microplastics research, (bio)pharmaceuticals, materials science, cultural heritage, forensics, photonics, and failure analysis.

© 2024 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/). https://doi.org/10.1063/5.0219983

## INTRODUCTION

Infrared spectroscopy is one of the most widely used tech niques for chemical analysis with many diverse applications. Midinfrared wavelengths have oscillation frequencies that correspond to numerous chemical bond vibrations within organic and inorganic molecules (Fig. 1) and thus serve as excellent probes of molecular composition based on chemical functional groups and molecular conformation within a sample. Infrared (IR) spectroscopy enables characterization and identification of materials based on infrared absorption spectra, which can serve as highly specific molecular fingerprints. The combination of infrared spectroscopy with optical microscopy in the 1980s enabled rich spatially resolved chemical analysis. Conventional IR micro-spectroscopy, however, suffers from several key limitations, namely, relatively coarse spatial resolution, complex sample preparation requirements, and issues with scattering/dispersive artifacts. Optical photothermal infrared (O-PTIR) spectroscopy and imaging was developed to address these limitations. This tutorial will review the origins of O-PTIR, the underlying technology, and review recent applications.

## Limitations of conventional infrared spectroscopy

The resolution of a conventional optical microscope, including infrared microscopes, is constrained by optical diffraction. The lateral spatial resolution dl according to the Rayleigh criterion is given by

$$
d _ {l} = \frac {0 . 6 1 \lambda}{\mathrm{NA}}, \tag {1}
$$

where λ is the wavelength, n is the index of refraction, and NA is the numerical aperture of the focusing and/or collection objective. For mid-IR wavelengths in the range of 2.5–25 μm, this corresponds to a spatial resolution range of around 3–30 μm for commonly used IR objectives. It is important to point out that for traditional infrared spectroscopy, the actual spatial resolution is very much wavelength (wavenumber) dependent, hence there is no singular value that can be used to characterize the spatial resolution performance of an infrared microscope, but rather, there is a range of values, which is typically in the order of 3–30 μm. This spatial resolution is significantly coarser than conventional optical microscopy performed at visible wavelengths. For example, a 0.8 NA air objective imaging at 532 nm can achieve a spatial resolution of around 400 nm, and water or oil objectives can achieve a resolution of ∼250 nm. This has left IR micro-spectroscopy at a significant deficit compared to visible light microscopy. The spatial resolution limit of mid-IR micro-spectroscopy has also constrained its application in critical high-value research areas. For example, in the case of life sciences, the mid-IR spatial resolution limits on the scale of 3–30 μm is similar to the length scale of entire biological cells, making most sub-cellular spectroscopic analysis impossible or extremely limited at mid-IR wavelengths. Somewhat higher spatial resolution can be achieved with attenuated total reflection (ATR), but this approach requires direct mechanical contact of a high index crystal with the sample, which can lead to sample damage, cross-contamination, and inconsistent imaging. Conventional infrared spectroscopy is often preferably performed in a transmission configuration, which requires thin sectioning of samples (to ∼5–10 μm thickness) to avoid excessive absorption by the sample and resulting nonlinearity and saturation effects. Finally, when samples have features on the length scale of mid-IR wavelengths, Mie scattering can cause size, shape, and wavelength-dependent scattering effects that can distort spectra, making spectral interpretation difficult. The O-PTIR approach, as detailed in the following, addresses all these key limitations, providing a non-contact measurement approach with spatial resolution commensurate with visible light optical microscopy, no requirement for thin-sectioning, and that is insensitive to size and shape scattering artifacts.

![](images/9682de23c4d008d72be10bc0e7e8013455b10c1dbe89f66fc9eeca265fea5c16.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Intensity |
| ----------------- | --------- |
| ~3500             | ~0        |
| ~2900             | ~0.6      |
| ~2400             | ~0        |
| ~2000             | ~0        |
| ~1500             | ~0.75     |
| ~1000             | ~0        |
</details>

FIG. 1. Key functional groups accessible in mid-infrared spectroscopy. The “cell silent” region refers to a region without significant IR absorption by biological materials and is used for stable isotope labeling for metabolic studies.

## The origins of O-PTIR

Photothermal infrared spectroscopy has been exploited for decades, primarily through the application of photo-acoustic Fourier transform infrared (PA-FTIR), often also simply referred to as photo-acoustic spectroscopy (PAS). PA-FTIR was based on the absorption of IR light into a solid sample, with the signal detected by the subtle acoustic waves generated by sample expansion, typically in a nitrogen atmosphere with an ultra-sensitive microphone.1 While being a very useful sampling accessory to FTIR, especially for the more bulk, intractable samples, it lacked any spatial resolving capabilities. Photothermal imaging has a history dating back at least to the 1980s, including the work of Fournier et al.2 (Fig. 2) who used the “mirage effect” to detect absorption of laser radiation by a sample. Despite a rich application space for photothermal imaging and spectroscopy that emerged since this work, almost thirty years passed before it was realized that photothermal detection approaches could be used to overcome infrared diffraction limits that constrain mid-IR spectroscopy.

The first approaches for overcoming the mid-IR diffraction limit originated in the field of atomic force microscopy where the probe of an atomic force microscope was used to detect thermal expansion resulting from absorption of IR light.3–6 The AFM-IR technique has become widely used, but its applications have been constrained by the level of technical skill required to operate the AFM, as well as limits on measurement speed and samples that can be readily measured by AFM. In 2012, researchers at the U.S. Naval Research Laboratory7 reported the use of an optical probe beam operating at visible wavelengths to detect IR absorption at a spatial resolution smaller than the diffraction limit for mid-IR light. Researchers at Boston University reported a similar work by using a quantum cascade laser (QCL) as the excitation source.8,9 Yet, these preliminary research described in conference proceedings did not demonstrate super-resolution over IR microscopy, nor the potential of imaging a living system by an infrared pump and a visible probe.

![](images/f9239c7790032bd3afcbec0b0818f640331dc9bc7e82eaa43b09d58293aeb194.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["LASER"] --> B["CHOPPER"]
  B --> C["CYLINDRICAL LENS"]
  C --> D["SAMPLE"]
  D --> E["SAMPLE"]
  E --> F["PROBE BEAM"]
  F --> G["SAMPLE"]
  G --> H["POS. SENSOR"]
  H --> I["1"]
  H --> J["2"]
  I --> K["Beam EXPANDER"]
  J --> K
```
</details>

FIG. 2. Photothermal imaging apparatus of Fournier et al. reproduced with permission from Fournier et al., J. Phys. Colloq. 44(C6), C6-479 (1983). Copyright 1983 EDP Sciences.

In 2011, Cheng, a co-inventor of coherent Raman scattering microscopy,10 independently started to explore infrared photothermal microscopy at Purdue University to overcome the sensitivity issue in Raman microscopy due to the very low cross section of Raman scattering. After five years of persistent effort in 2016, the Cheng group reported use of dark-field beam geometry and a resonant circuit to pick up the photothermal signal, to enable a high-performance mid-infrared photothermal (MIP) microscope that allowed for the first time 3D imaging of chemical bonds inside a living cell at 600 nm resolution and 10 μM limit of detection.11 The pioneering studies at Purdue11–13 and independent work at Notre Dame14–16 quickly inspired new developments by various groups (for reviews17,18) and caught industrial attention. The first commercial MIP instrument “mIRage” was announced in October 2017 by Anasys Instruments who had previously commercialized AFM-based photothermal infrared spectroscopy. The acronym O-PTIR (optical photothermal infrared) was coined to differentiate the technology from the AFM-based photothermal infrared approach. For avoidance of confusion, O-PTIR and MIP refer to the same super-resolution IR spectroscopy and chemical imaging approach. The acronym O-PTIR will be used for the remainder of this review. Photothermal Spectroscopy Corp. (a spinoff of Anasys)

was founded in 2018 to develop and commercialize this emerging technology with full momentum, in collaboration with the Cheng group, which moved to Boston University in 2017. Two prior review articles 17,18 provide an excellent summary of academic research in the field of super-resolution infrared photothermal microscopy. In this tutorial, we introduce the working principle, instrumentation, and applications of OPTIR microscopy in lay language.

## How O-PTIR works

The O-PTIR approach (Fig. 3) works by illuminating a sample with pulses of IR radiation, typically from a tunable IR laser source, such as a quantum cascade laser (QCL) and detecting localized heating of IR absorbing regions with a shorter wavelength visible probe beam. In particular, when IR light excites molecular bonds within a sample, a portion of the energy absorbed and dissipated in the sample, resulting in localized heating. The resulting temperature increase causes thermal expansion in the sample that, in turn, causes a reduction of the index of refraction of the IR-heated regions. The optical probe beam can detect these IR-induced temperature changes because the thermal expansion and associated reduction in the index of refraction alter the intensity and angular distribution of probe light reflected, scattered, and/or transmitted by the sample.

![](images/4b22635d2f1c2b22f337f7bcbf09592825e13de19851c03fe5992a847c00f76c.jpg)

<details>
<summary>text_image</summary>

Infrared pulse
IR diffraction limit
~10μm
</details>

![](images/9a15429a52249ffeaa84d84f57ea34025208ecc68ca942ef06bb00d470301a7a.jpg)

<details>
<summary>text_image</summary>

Visible light
Visible diffraction limit
~0.4 µm
</details>

![](images/008a69f7dd4fdae3d37b01b2c5053e7f63adb38418e663054389abc15fa82d60.jpg)

<details>
<summary>text_image</summary>

dn/dT
Thermal expansion
</details>

FIG. 3. O-PTIR uses a visible probe beam to detect infrared absorption with sub-500 nm spatial resolution via photothermal detection sensitive to thermal expansion and index of refraction changes in IR absorbing regions of a sample.

## Achieving super-resolution photothermal infrared

The O-PTIR approach achieves spatial resolution commensurate with the visible light optical microscope and Raman microscope because the spatial resolution is set by the optical diffraction limit of the shorter wavelength probe beam, not the longer wavelength IR beam. Because the probe beam wavelength is chosen to be roughly an order of magnitude shorter than mid-IR wavelengths, the achievable resolution achievable by O-PTIR [as indicated by Eq. (1)] is roughly an order of magnitude better than conventional IR instrument. Figure 4(a) shows a comparison of the theoretical lateral spatial resolution of typical conventional IR microscopes (both FT-IR and QCL based). For example, at $1 0 0 0 ~ \mathrm { { c m } ^ { - 1 } }$ (10 μm IR wavelength), a typical FT-IR based microscope with a 15×, 0.4 NA objective would achieve a lateral spatial resolution of around 15 μm, whereas an O-PTIR instrument operating with a 532 nm probe wavelength and a 0.78 NA objective would achieve a theoretical spatial resolution of 416 nm, an improvement of ∼36×. The O-PTIR approach thus enables “super-resolution” infrared microscopy/spectroscopy by exceeding the optical diffraction limit for infrared wavelengths. For the avoidance of confusion, the term “super-resolution” in this context does not refer to approaches used in optical microscopy to exceed the ∼250 nm diffraction limit of visible light microscopy, but rather exceeding the corresponding diffraction limits for infrared wavelengths. O-PTIR also achieves significant improvements in axial resolution, as shown in Fig. 4(b). Axial resolution da, as given by Eq. (2) depends on the square of the NA, causing lower NA objectives commonly used in FT-IR microscopy to suffer very coarse axial spatial resolution e.g., around 76 μm at 1000 $\mathrm { c m } ^ { - 1 }$ with a 0.4 NA objective, whereas a typical O-PTIR microscope can achieve an axial spatial resolution around 1 μm at the same wavelength,

$$
d _ {a} = \frac {2 \lambda}{N A ^ {2}}. \tag {2}
$$

Even higher lateral and axial resolutions can be achieved in O PTIR using higher NA refractive objectives, which are unsuitable for FTIR/QCL microscopy and using immersion objectives and/or confocal microscopy approaches, as will be discussed later.

## O-PTIR instrumentation

An example schematic of O-PTIR instrumentation is shown in Fig. 5. In this arrangement, infrared light from a tunable IR laser is combined coaxially with light from a visible probe laser using a dichroic mirror DM1, and both IR and probe beams are focused onto the sample using a reflective objective (RO) of a Schwarzschild design (also called Cassegrain objective). A reflective objective is necessary due to the ultra-wide range of wavelengths being employed, from visible wavelength (400–700 nm) to IR wavelengths up to about 12 μm. In addition, typical glass objectives used in optical or Raman microscopy are not transmissive to mid-IR wavelengths. Absorption of IR light by the sample creates a modulated local temperature increase that causes both thermal expansion of the sample and a resulting decrease in the local index of refraction due to the decrease in sample density. The changes in size, shape, and index of refraction alter the intensity and angular distribution of light reflected, scattered, and/or transmitted by the sample. The typical magnitude of fractional change in the index of refraction is around $1 0 ^ { \stackrel { \smile } { - } 4 } / { } ^ { \circ } \mathrm { C } .$ The IR source is typically pulsed at frequencies in the range of 100 kHz to produce periodic modulations in the intensity/distribution of the probe beam. In the configuration shown, modulated probe light is collected by the same reflective objective and sent to a photodetector. In other configurations discussed later, the modulated probe beam can also be collected in the transmission directions. The detector signal is generally demodulated with a lockin amplifier11 at the pulse repetition frequency of the IR laser or a harmonic thereof.19–21 Demodulation in the time domain has also been demonstrated,22,23 which can provide time-resolved analysis of the samples’ photothermal response. Modulation of the probe beam is then measured as a function of IR wavelength (wavenumber) to create IR absorption spectra or as a function of the sample position to create IR absorption images at desired IR absorption bands.

![](images/a11bd62cfb382c0a91b3cd8dc7c8fffb54076686911d5eb6ac69140994bfccb0.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | FTIR IR Microscope (0.4 NA) | QCL IR Microscope (0.7 NA) | O-PTIR Microscope (0.78 NA) |
| ----------------- | --------------------------- | -------------------------- | --------------------------- |
| 3800              | 4                           | 2                          | 0                           |
| 2800              | 6                           | 3                          | 0                           |
| 1800              | 10                          | 5                          | 0                           |
| 800               | 19                          | 11                         | 0                           |
</details>

![](images/1df74dbc097d67295779225be4ef310792d170149e992e5913a24435823e66a1.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Theoretical Spatial Resolution (µm) |
| ----------------- | ----------------------------------- |
| 3800              | 20                                  |
| 2800              | 30                                  |
| 1800              | 45                                  |
| 800               | 95                                  |
</details>

FIG. 4. Comparison of theoretical lateral (a) and axial (b) spatial resolution of conventional IR microscopes (FTIR and QCL based) with the O-PTIR approach. Unlike conventional IR microscopes, O-PTIR’s spatial resolution is set by the probe wavelength and thus is constant over all IR wavelengths.

![](images/9deaa1246375a9f923356838381a6176dbd9d8bc3be6d0269dd67917fffbf615.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Computer"] --> B["Lock-in"]
  B --> C["Visible detector"]
  C --> D["Visible laser"]
  D --> E["IR laser"]
  E --> F["Camera"]
  F --> G["DM1"]
  G --> H["BS"]
  H --> I["DM2"]
  I --> J["XY stage"]
  J --> K["Sub-μm IR spectra and chemical images"]
```
</details>

FIG. 5. Simplified schematic diagram of an O-PTIR instrument. Reprinted with permission from Kansiz et al.,24 Microsc. Today 28(3), 26 (2020). Copyright 2020 Microscopy Society of America.

![](images/57a8d5f6f6f37ba4eea04446cb04523dec63cdbdd056884221dc1fdd111e2e16.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | O-PTIR (mV) |
| ----------------- | ----------- |
| 2995              | ~0.5        |
| 2800              | ~4.3        |
| 2600              | ~0.0        |
| 2400              | ~0.0        |
| 2200              | ~0.0        |
| 2000              | ~0.0        |
| 1800              | ~1.0        |
| 1600              | ~8.0        |
| 1400              | ~2.5        |
| 1200              | ~4.8        |
| 1000              | ~1.2        |
| 771               | ~0.3        |
</details>

FIG. 6. Example QCL power curve for a four chip QCL covering the CH region (QCL chip 1) and fingerprint region (QCL chips 2–4). QCLs are also available with emission in the “silent region” for metabolic studies, as discussed later.

Current generation QCLs are typically composed of four “chip” slots, which are user-configurable with an example power spectrum, as shown in Fig. 6, of a common, so-called “C–H/Fingerprint” QCL. More recently, interest in silent region IR tags (discussed further below) has increased; one could configure a four chip, as a so-called tri-range QCL covering the C–H region, silent region, and fingerprint region out to the high 900 $\dot { \mathrm { c m } } ^ { - 1 }$ . Collected IR spectra are normalized for the variable, wavelength dependent power output that is typical of QCL as well as optical path and atmospheric (e.g., water vapor) absorbances (e.g., the downward spikes in the QCL chip 2 power curve in the following).

## KEY O-PTIR CAPABILITIES

Among the key advantages of O-PTIR are the ability to achieve sub-500 nm spatial resolution at mid-IR wavelengths, the ability to acquire spectra with excellent correlation to conventional FT-IR transmission spectra, and high sensitivity/signal-to-noise ratio. Each of these are discussed briefly in the following.

## Sub-500 nm super-resolution IR imaging

Figure 7 in the following shows an example IR absorption image demonstrating sub-500 nm spatial resolution. For this test, a 10 μm diameter PMMA bead was embedded in epoxy and sectioned to 500 nm thick and then imaged in counter-propagating mode (described in a following section) at 1730 cm−1, which is strongly absorbed by the carbonyl band in PMMA. A cross section of the IR absorption shown in Fig. 7(b) reveals a spatial resolution of around 350 nm. A similar resolution has been reported in the literature on 100 nm polystyrene beads,16 lipid droplets in cells,25 and other samples. Even higher spatial resolution has been demonstrated using higher-harmonic detection approaches.20

## Rapid high-quality spectra

IR absorption spectra are acquired by using O-PTIR by measuring the modulation of the collected visible probe beam while sweeping the wavelength of the tunable IR source. The acquisition speed is determined by the sweep speed of the tunable IR laser source and the desired signal to noise ratio (SNR). The most commonly used IR laser sources are quantum cascade lasers $( \mathrm { Q C L s } ) ,$ which can be tuned at rates of $1 0 0 \dot { 0 } ~ \mathrm { c m } ^ { - 1 } / s$ and higher. IR spectra are typically acquired in 1–5 s depending on the spectral resolution and SNR requirements for the measurement. For higher SNR, multiple spectra can be acquired and co-averaged. In typical operation, a user will acquire some exemplar spectra at various locations on the sample to determine the IR absorption bands present in the sample. Examination of the collected spectra can reveal which IR bands show the most variation between different constituents in the sample. With this knowledge, it is possible to acquire IR absorption images at multiple IR absorption bands to reveal the spatial heterogeneity within the sample. It is also possible to collect hyperspectral arrays of O-PTIR spectra over an array of locations on a sample, or using emerging wide-field approaches acquire an array of IR absorption images at different IR wavelengths. These hyperspectral arrays can provide a rich analysis of the spatial and spectral variations in complex samples.

## Strong correlation to FTIR spectra

One of the strengths of the O-PTIR approach is the ability to acquire super-resolution infrared spectra with very strong correlation to transmission-mode FT-IR spectra. Figure 8 shows an example O-PTIR spectra measured on a variety of polymeric films in comparison with conventional transmission-mode FT-IR spectra from a material reference database. The reason for the strong correlation is that the signal detected in O-PTIR, a modulation in the collected probe beam, is directly proportional to the spectral absorbance that is measured in FT-IR instruments. This has enabled researchers to leverage large spectral databases with hundreds of thousands of IR spectra for the identification of unknowns. This correlation has proven very useful, for example, in the analysis/identifications of organic contaminants,24 nanocomposites,26 and microplastic particles.

![](images/23789d9c05fb98e9a0ac92fd95c043c9fa1800ca20856803aa7500a7704cf5ab.jpg)

<details>
<summary>heatmap</summary>

| Longitude (μm) | Latitude (μm) | Value (mV) |
| -------------- | ------------- | ---------- |
| -6541.8        | 371.24        | ~0         |
| -6539.23       | 374.07        | ~0         |
| -6536.67       | 376.9         | ~0         |
| -6534.1        | 379.73        | ~0         |
| -6531.53       | 382.56        | ~0         |
| -6528.97       | 379.73        | ~0         |
| -6526.4        | 376.9         | ~0         |
</details>

![](images/636a945192b0b069ad1a14c28df79cf669aed154f6563019d1aa49e508d5f51f.jpg)

<details>
<summary>line chart</summary>

| µm | mV |
| --- | --- |
| 0 | 0.0 |
| 1 | 0.0 |
| 2 | 3.0 |
| 3 | 4.2 |
| 4 | 4.0 |
| 5 | 3.9 |
| 6 | 3.9 |
| 7 | 3.9 |
| 8 | 4.0 |
| 9 | 4.0 |
| 10 | 3.9 |
| 11 | 3.9 |
| 12 | 3.9 |
| 13 | 0.5 |
| 14 | 0.0 |
| 15 | 0.0 |
| 16 | 0.0 |
</details>

FIG. 7. Super-resolution infrared chemical imaging with O-PTIR. The sample is an (a) IR chemical image of PMMA bead at 1730 cm−1 with 50 nm pixel size. (b) Cross section of IR absorption across the line indicated in panel (a) showing spatial resolution at the PMMA/epoxy boundary of around 350 nm.

![](images/c170d045514a509b39d1a1364a54d68a1baf556f671a0c1368b443b79f9de94c.jpg)

<details>
<summary>line chart</summary>

| cm⁻¹ | Polypropylene, PP (FTIR reference) | Polypropylene, PP (O-PTIR) |
|------|-----------------------------------|---------------------------|
| 3000 | ~8.5                              | ~8.5                      |
| 2800 | ~4.5                              | ~4.5                      |
| 1400 | ~5.5                              | ~5.5                      |
| 1200 | ~1.0                              | ~1.0                      |
| 1000 | ~1.5                              | ~1.5                      |
| 800  | ~0.5                              | ~0.5                      |
</details>

![](images/a53a63ecbe33397d185ef74209ea9476bd445dc8dda1e401d3d8246585fa137b.jpg)

<details>
<summary>line chart</summary>

| cm⁻¹ | Value |
|------|-------|
| ~3000 | ~1.0 |
| ~2800 | ~0.8 |
| ~1400 | ~0.1 |
</details>

![](images/c08e211dd590eb2fe31beb768506560b5b758a51394feeb38cbaed26f59d10d8.jpg)

<details>
<summary>line chart</summary>

| cm⁻¹ | Polyamide, Nylon FTIR (reference) | Polyamide, Nylon (O-PTIR) |
|------|-----------------------------------|---------------------------|
| 3400 | ~0.8                              | ~0.5                      |
| 3200 | ~0.1                              | ~0.3                      |
| 3000 | ~0.5                              | ~0.2                      |
| 2800 | ~0.1                              | ~0.1                      |
| 2600 | ~0.0                              | ~0.0                      |
| 2400 | ~0.0                              | ~0.0                      |
| 2200 | ~0.0                              | ~0.0                      |
| 2000 | ~0.0                              | ~0.0                      |
| 1800 | ~0.0                              | ~0.0                      |
| 1600 | ~1.0                              | ~0.6                      |
| 1400 | ~0.1                              | ~0.1                      |
| 1200 | ~0.1                              | ~0.1                      |
| 1000 | ~0.0                              | ~0.0                      |
| 800  | ~0.0                              | ~0.0                      |
</details>

FIG. 8. Comparison of O-PTIR spectra with FT-IR reference spectra. (Reference spectra source: Wiley Know-It-All).

The reason for this correlation is that in most cases: (1) the temperature increase in the sample varies linearly with the sample IR absorption coefficient and (2) O-PTIR signal is generally linear with the increase in sample temperature. This is summarized in the following in a simplified analysis of relevant photothermal physics, following an analogous analysis for AFM-IR by Dazzi and Prater (see supplementary material of Ref. 6). First, as shown in Eq. (3), the IR spectral absorbance A(ν) as a function of wavenumber ν is proportional to the wavenumber and the sample’s imaginary index of refraction κ(ν),

$$
A (\nu) = \log \left(\frac {1}{T}\right) = \frac {4 \pi}{\ln (1 0)} \nu \kappa (\nu). \tag {3}
$$

The amount of heat absorbed by the sample is similarly proportional to the input power $I _ { 0 } ,$ the spectral absorbance $A ( \nu )$ , the sample volume V, and various constants subsumed in $\alpha _ { o p t }$ ,

$$
P _ {a b s} (\nu) = I _ {0} \alpha_ {o p t} V A (\nu). \tag {4}
$$

The maximum sample temperature increase is, in turn, proportional to the absorbed IR power, the IR pulse duration $t _ { P } ,$ and inversely related sample’s density and heat capacity ρcp, $\rho c _ { p } .$

$$
\Delta T _ {\max} = \frac {P _ {a b s} (\nu) t _ {p}}{V \rho c _ {p}} = \frac {I _ {0} \alpha_ {o p t} t _ {p}}{\rho c _ {p}} A (\nu). \tag {5}
$$

The increase in sample temperature results in a change in the index of refraction of the sample that, in turn, alters the intensity and distribution of the probe light collected by the detector. The math associated with the intensity change is beyond the scope of this manuscript and dependent on the specific collection geometry, but various models28–33 exist within the photothermal physics community. However, the literature and experiments show that, in general, the collected probe intensity will have a linear dependence on sample temperature change in the limit of fractionally small modulation, i.e., $\frac { \mathop { \Delta I _ { P T } } } { I _ { d c } } \ll 1 .$ ΔIPT ≪ 1, where ΔIPT is the fluctuation of the collected probe $\varDelta I _ { P T }$ beam in response to IR absorption and $I _ { d c }$ is the dc intensity at the detector. The collected probe beam intensity modulation can have a complex nonlinear dependence on the sample thermal expansion and temperature induced index of refraction shift, but this depen dence can generally be linearized due to the small fractional changes involved. Both the thermal expansion coefficient and the temperature dependence of the index of refraction have a typical fractional sensitivity on the order of $1 0 ^ { - 4 } / { } ^ { \circ } \mathrm { C }$ for most biological and polymeric materials. This leads to a case where the sample thermal expansion $\frac { \delta h } { h } \ll 1$ h ≪ 1 and the index change δn ≪ 1, providing an essentially linear $\begin{array} { r } { \frac { \delta n } { n } \ll 1 , } \end{array}$ −n dependence of collected probe light modulation with temperature. In practical experiments, $\frac { \varDelta I _ { P T } } { I _ { d c } }$ typically has a maximum value of order $1 0 ^ { - 3 }$ with peak temperature increases on the scale of $1 { - } 1 0 ^ { \circ } \mathrm { C } .$ Considering just the index of refraction effects for simplicity, the detected change in the collected probe beam intensity $\varDelta I _ { P T }$ is linearly related to the spectral absorbance $A ( \nu )$ , as shown in Eq. (6). Similar arguments apply to photothermal contrast associated with shape change/surface motion associated with thermal expansion,

$$
\Delta I _ {P T} \propto \frac {\delta n}{d T} \Delta T _ {\max} = \left(\frac {I _ {0} \alpha_ {o p t} t _ {p}}{\rho c _ {p}}\right) \frac {\delta n}{d T} A (\nu). \tag {6}
$$

For this reason, it is important in O-PTIR to apply ratiometric approaches to normalize for these other signal contributions.

## O-PTIR + Raman

O-PTIR also supports simultaneous infrared and Raman spectroscopy, leveraging the probe beam for two complementary spectroscopic measurements (Fig. 9). Raman and infrared spectroscopy, while both being vibrational spectroscopic techniques and thus probing molecular vibrations, have very different selection rules (conditions that result in a vibrational signal). For infrared spectroscopy, IR active bands require an inter-atomic vibration that results in a net change in the bond dipole moment. Thus, IR spectroscopy, in general, is more sensitive to bonds involving more polar atoms. On the other hand, Raman spectroscopy selection rules stipulate that for a vibration to be Raman active, the vibration in question must have a change in polarizability during the vibration. Thus, and in contrast to IR spectroscopy, Raman spectroscopy is generally more sensitive to non-polar vibrations. Hence, the two techniques are often considered “complementary” to one another, with molecules with strong IR absorbance, typically having a weaker Raman response and molecules with a strong Raman response, typically having weakening IR absorbances. While the beneficial nature of combining these two complementary techniques for a more thorough spectroscopic characterization is clear, the very different instrument operation, measurement sample presentations required, have meant that true complementary measurements have not been possible, since two very different instrument platforms, with very different achievable spatial resolutions have existed so far.

![](images/d9738c1f3b8d12cd513cf5378a2e718ca824685d6f9c244048a0011d7cfcb79a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Raman spectrum"] --> B["3086"]
  B --> C["1618"]
  C --> D["Reflective objective"]
  D --> E["Sample stage"]
  F["Illuminator"] --> G["Camera"]
  G --> H["PBS"]
  H --> I["Visible detector"]
  I --> J["Visible laser"]
  J --> K["Edge filter"]
  K --> L["CCD"]
  L --> M["DM"]
  M --> N["IR laser"]
  N --> O["IR Spectrum"]
    style A fill:#cce5ff,stroke:#333
    style F fill:#cce5ff,stroke:#333
    style G fill:#cce5ff,stroke:#333
    style H fill:#cce5ff,stroke:#333
    style I fill:#cce5ff,stroke:#333
    style J fill:#cce5ff,stroke:#333
    style K fill:#cce5ff,stroke:#333
    style L fill:#cce5ff,stroke:#333
    style M fill:#cce5ff,stroke:#333
    style N fill:#cce5ff,stroke:#333
    style O fill:#cce5ff,stroke:#333
```
</details>

FIG. 9. Schematic diagram of instrumentation for combined O-PTIR + Raman spectroscopy.

Therefore, one of the biggest vibrational spectroscopic value propositions of O-PTIR has been that, for the first time, IR and Raman spectroscopy can be collected from the same spot, at the same time, and at the same spatial resolution, thus finally achieving full complementarity of these two techniques.21,24,34–38 This can be achieved by using a visible probe beam used to detect IR absorption that is also a low noise narrow bandwidth laser and can thus act and double as a Raman excitation laser. For example, commercial O-PTIR instruments are currently available with 532 and 785 nm laser lines. After interacting the probe beam with the sample, any Raman scattered light is separated by a dichroic mirror (a Raman edge filter)

and the light at the original excitation wavelength is sent to a visible room temperature detector for demodulation of the IR absorption signal, whereas wavelength shifted light is sent to a Raman spectrometer for the generation of Raman spectra. As such, the IR and Raman measurements are obtained at the same time, same location, and same spatial resolution, with essentially no compromise on either IR or Raman spectral quality. In this approach, the full complementarity and confirmatory nature of these two techniques is realized, without the need to move the sample, the objective, or any other optic, hence also providing for exact registration between these two channels.

An example of a simultaneous, submicron IR + Raman measurement is shown in the following in Fig. 10 of a single E. coli bacterium. This measurement is also a good demonstration of the spectroscopic complementarity between IR and Raman. Figure 10 shows very strong Raman C–H bands, which are a characteristic of Raman, while fingerprint spectral features are weaker in Raman. This is generally and conversely true in the IR, as clearly demonstrated in this example with very strong protein (amide I and amide II) bands together with an overall significantly better SNR for the IR (O-PTIR) measurement, despite measurement time being identical at a few seconds of averaging.

## O-PTIR + fluorescence

Fluorescence microscopy has also been combined with O PTIR to provide labeled targeting of infrared analysis and enhanced measurement sensitivity.

![](images/86095d49f872777d6cfbec66c532dcac3665b3a1ecc636ec10c01ce8f35bf168.jpg)

<details>
<summary>line chart</summary>

| Wavenumber/Raman Shift (cm⁻¹) | Raman (532nm) | O-PTIR (with Dual Range (C-H/FP) QCL) |
| ----------------------------- | ------------- | ------------------------------------- |
| 4000                          | ~0.05         | ~0.0                                  |
| 3800                          | ~0.05         | ~0.0                                  |
| 3600                          | ~0.05         | ~0.0                                  |
| 3400                          | ~0.05         | ~0.0                                  |
| 3200                          | ~0.05         | ~0.0                                  |
| 3000                          | ~0.95         | ~0.3                                  |
| 2800                          | ~0.2          | ~0.1                                  |
| 2600                          | ~0.0          | ~0.0                                  |
| 2400                          | ~0.0          | ~0.0                                  |
| 2200                          | ~0.0          | ~0.0                                  |
| 2000                          | ~0.0          | ~0.0                                  |
| 1800                          | ~0.0          | ~0.0                                  |
| 1600                          | ~1.0          | ~1.0                                  |
| 1400                          | ~0.3          | ~0.2                                  |
| 1200                          | ~0.2          | ~0.15                                 |
| 1000                          | ~0.25         | ~0.25                                 |
| 800                           | ~0.1          | ~0.1                                  |
| 600                           | ~0.0          | ~0.0                                  |
</details>

FIG. 10. Example of simultaneous and co-located infrared (O-PTIR) and Raman spectra acquired on a single E. coli bacterium. The sample is courtesy of Goodacre. Figure courtesy of Photothermal Spectroscopy Corp., reprinted with permission.

## Fluorescence-guided O-PTIR

Fluorescence labeling, e.g., by immunofluorescence staining or fluorescent proteins, is ubiquitous in the life sciences and is frequently used to label specific substructures within cells and tissue. Fluorescence imaging while providing excellent chemical specificity by virtue of targeted tabs/labels lacks any broad chemical characterization capabilities. These fluorescent labels can then be used as landmarks to guide targeted chemical analysis via O-PTIR.39,40 Although fluorescence labeling has very high specificity, immunofluorescence labeling adheres fluorescent dyes to specific epitopes, but the fluorescence labeling and imaging does not provide information about the specific chemical molecular structure/conformation of the labeled molecules. O-PTIR provides highly complementary analysis capabilities by probing the molecular structure and conformation, which can provide key insights into, for example, the local protein folding state. The group of Prater et al. in collaboration with researchers at Photothermal Spectroscopy Corp. demonstrated the ability to use immunofluorescent labeling of amyloid plaques in brain tissue to locate the whereabouts of these amyloid plaques, thus allowing a direct targeting of the O-PTIR analysis of labeled amyloid plaques and adjacent normal tissue to provide for a broad chemical analysis, including protein secondary structure analysis, both of which would be impossible with fluorescence imaging alone.39 This analysis demonstrated clear spatially resolved differences in the presence of beta sheet structures associated with protein misfolding, as shown in Fig. 11.

## Wide field fluorescence detected O-PTIR (FL-PTIR)

Fluorescence emission can also provide an enhanced method of detecting IR absorption. As mentioned previously, conventional O-PTIR detects IR absorption by measuring a modulation in the collected probe beam due to thermal expansion and index of refraction changes with a typical intrinsic photothermal sensitivity of most materials of around 10 $^ { - 4 } / ^ { \circ } \mathrm { C } \ ( \mathrm { i } . \mathrm { e } . ,$ , the change in the index of refraction of a sample with temperature). The efficiency of fluorescence emission (quantum yield), however, is highly temperature dependent with a typical temperature coefficient of around $1 \% / { } ^ { \circ } \mathrm { C } .$ Researchers at Photothermal Spectroscopy Corp.,41 Boston University, and Purdue University 43,44 realized that the high temperature of fluorescence emission could provide a new mechanism of detecting local IR absorption with roughly 100× better sensi tivity than conventional O-PTIR. The group of Cheng at Boston University demonstrated high sensitivity chemical imaging of fluorescently labeled bacteria and live cancer cells, as well as the ability to

![](images/4bdd50b8062cb0a27ead6690dc1673d188843fc719415b8441d3fd2685cdd701.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological specimen with grid overlay and 1 mm scale bar (no text or symbols)
</details>

![](images/03c7db3067eb83ac8f2502fd50699913ea952ccd854e1277ff88bf3ac1d3d6d1.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a red fluorescent spot labeled 'Amytracker' with a 25 μm scale bar (no other text or symbols)
</details>

![](images/353c2969dc7d6ac087d53832aa59a7bd2e9bc99b8f3d47cc2ac80afa47406684.jpg)

<details>
<summary>natural_image</summary>

Microscopic surface topography image with color gradient and 25 μm scale bar (no text or symbols beyond scale indicator)
</details>

![](images/a8ea7b6cbcbfd3f6e2d50517714cb2836be73cbfc90660adb125e50f8cc1a0fb.jpg)

<details>
<summary>line chart</summary>

| Wavenumber, cm⁻¹ | Outside | Core | Corona |
| ---------------- | ------- | ---- | ------ |
| 1630             | ~1.0    | ~0.95| ~0.9   |
</details>

FIG. 11. Fluorescence-guided O-PTIR of amyloid plaques in brain tissue. (a) Multi-image fluorescence microscope mosaic of mouse brain tissue with amyloid plaques labeled with Amytracker 520. (b) Zoomed image of an amyloid plaque stained with Amytracker. (c) A map demonstrating the distribution of β-sheet structures as a ratio of the bands at 1630–1656 cm−1 for the plaque shown in panel (b). (d) Averaged and normalized O-PTIR spectra were recorded from the outside, core, and plaque corona; the spectra locations were indicated by the markers of the corresponding color on the inset. Reprinted with permission from Prater et al., J. Med. Chem. 66(4), 2542 (2023). Copyright 2023 Author(s), licensed under a Creative Commons Attribution 4.0 License.

perform high-speed wide-field O-PTIR taking advantage of the ∼100× sensitivity enhancement provided by fluorescence detec tion.42 The group of Garth Simpson demonstrated sensitive characterization of the chemical composition within phase-separated domains of amorphous solid dispersions, highlighting its utility in pharmaceutical material analysis43 and the ability to use two-photon autofluorescence to enabled fluorescence detected O-PTIR on unlabeled samples.44 Another significant benefit to fluorescence detected photothermal infrared (FL-PTIR) is that the fluorescence detector typically employed a high sensitivity wide-field fluorescence camera, and thus operated analogously to infrared focal plane arrays commonly used in FT-IR imaging, i.e., permitting simultaneous measurements of IR absorption at hundreds of thousands of pixels simultaneously. Such operation provides for true wide-field snapshot O-PTIR where all pixels in the array (typically 512 × 512), even up to 5 frames/s with a typical projected pixel size of 130 nm, thus covering a field of view (FOV) of 66 × 66 μm2 per tile. This rapid, multi-channel collection process has also provided a massive increase in hyperspectral measurements, with typical full spectral range hyperspectral measurements taking only tens of minutes and with full FOV single frequency images taking seconds (or less). Since the IR source is generally defocused for wide-field measurements, the field of view is generally limited by the power density of the IR source (a QCL in this case). As more powerful IR sources become available, addressable fields of view will also increase. In the meantime, large fields of view are achievable by tiling multiple adjacent measurements in a mosaic.

Recently, a collaboration between Photothermal Spectroscopy Corp. and the group of Kathleen Gough at the University of Manitoba demonstrated high-speed wide-field O-PTIR of biological samples using intrinsic autofluorescent emission instead of fluorescent labeling.45 Autofluorescent emission is very common among biological materials, for example, associated with aromatic amino acids, cross-linking, and photosynthetic molecules. Furthermore,

Co-propagating mode  
![](images/b84fdc10183dce12d61ad0ac36694431159bcf5bd5264b95f6cf1cdb3bec0712.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Camera"] --> B["Illuminator"]
  B --> C["Cassegrain"]
  C --> D["Sample"]
  D --> E["Condenser lens"]
  E --> F["Detector (trans)"]
  G["Probe beam"] --> H["IR beam"]
  I["Detector (ref)"] --> J["Detector (ref)"]
```
</details>

Resolution: 400-800 nm  
Arbitrary sample thickness

Counter-Propagating Mode  
![](images/022c4e357f71fcd8a4ff43180092566f194a18f5d5d4a13643a1455e2be27353.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Camera"] --> B["Illuminator"]
  B --> C["Vis objective"]
  C --> D["Sample"]
  D --> E["IR Cassegrain"]
  E --> F["IR beam"]
  F --> G["Detector (trans)"]
  G --> H["Detector (ref)"]
  H --> I["Probe beam"]
  I --> J["Monitor"]
```
</details>

Resolution: 250-400 nm  
√ Samples <10 µm thick

FIG. 12. Comparison of co-propagating and counter-propagating O-PTIR measurement modes. Co-propagating mode can be used for any sample thickness with slightly coarser spatial resolution. Counter-propagating mode can achieve higher spatial resolution but requires thinner samples (≲10 μm thick).

autofluorescence is a well-known and much maligned interferent in Raman spectroscopy but can also be an interferent in fluorescence imaging too. In fact, the more autofluorescent a sample, the more sensitive the FL-PTIR measurement will be. The recent work with Kathleen Gough demonstrated the ability to acquire IR hyperspectral arrays on biological materials with high spectral resolution $( 4 \thinspace { \mathrm { c m } } ^ { - 1 } )$ and sub-500 nm spatial resolution within minutes, including measurements on diatoms, plant tissue, and even dynamic measurement on live microalgae.45

## O-PTIR CONFIGURATIONS/MEASUREMENT MODALITIES

O-PTIR is usually operated in one of two optical configurations, co-propagating and counter-propagating (Fig. 12). In copropagating mode, the IR and visible probe beams are arranged to be collinear and illuminate the sample from the same side, top-down. In counter-propagating mode (first demonstrated by the Hartland and Kuno groups at Notre Dame;14–16 Fig. 13), the IR beam and probe beam are de-coupled and delivered by separate objectives on opposite sides of the sample. In counter-propagating mode, the IR beam is typically delivered via a reflective objective (from beneath), whereas the probe beam is delivered by a high-quality, high-NA refractive objective (from the top). The counter-propagating approach can achieve higher spatial resolution because refractive objectives can generally attain higher numerical aperture and achieve better optical performance than reflective (Cassegrain) objectives. Furthermore, refractive objectives not only deliver better optical throughput due to their higher collection efficiencies, especially in high NA objectives, but also benefit from the absence of a central obscuration. Central obscuration is an unavoidable drawback in reflective objectives and typically blocks 25%-50% of the incident light. For example, a typical maximum NA for a reflective IR objective is around 0.78, whereas optical objectives are readily available at 0.95 NA for operation in air or up to around 1.2 for water immersion objectives, which deliver >50% improvement in spatial resolution relative to co-propagation operation with reflective Cassegrain objectives. (Oil immersion objectives with NA up to 1.4 can provide even better spatial resolution.) Thus counter-propagating mode can achieve a best case spatial resolution of around 200–250 nm, whereas copropagating mode achieves spatial resolution in the 400–800 nm range depending on the specific objective NA and probe wavelength. However, counter-propagation mode typically requires the use of thin IR transparent substrates (often 350 μm thick CaF2 windows) and requires thin samples, i.e., not thicker than ∼5–10 μm to avoid excessive self-absorption and/or scatter of the incident IR light. The use of counter-propagating mode on thicker samples or highly scattering samples can lead to distortions in the spectra resulting from attenuation/scattering of the infrared beam before it interacts with the surface where the probe beam is focused. A key advantage of copropagating mode is that it can measure samples of arbitrary thickness and on opaque substrates, at the expense of somewhat worse spatial resolution. Thus, it is often beneficial to have access to both modes of operation with switching between these modes typically achieved through instrument software selection. Examples of possible counter-propagating objectives, sample presentation (upright vs upside-down), and substrate choice configurations combinations are shown in Fig. 14.

![](images/d6842d378f5d876237650606925678fed06460688bf5d538f0c34b2bed3b540a.jpg)  
FIG. 13. Counter-propagating geometry developed by the researchers at Notre Dame achieving spatial resolution of around 300 nm. (a) Schematic diagram of the apparatus showing the mid-IR pump and 532 nm probe beams focused on the sample with separate objectives. The change in reflectivity of the probe is monitored by an APD with a lock-in amplifier. RC = reflective Cassegrain, FO = focusing objective, B/S = beam splitter, and TL = tube lens. (b) O-PTIR image of a 0.1 μm diameter polystyrene bead recorded with a step size of 0.05 μm. (c) Line profile extracted from the image in panel (b) showing a full width at half maximum (FWHM) of 0.3 μm. Reprinted with permission from Li et al., J. Phys. Chem. B 121(37), 8838 (2017). Copyright 2017 Author(s), licensed under ACS Open Access License.

An example of an oil immersion counterpropagating measurement is shown in the bottom center of Fig. 15. The enhanced spatial resolution is evident with features of 285 nm being easily resolved in the single-frequency IR lipid image at 1740 cm−1. In this configuration, the sample must be a thin sample (≲10 μm) and placed on a standard glass cover-slip (typically 170 μm thick) as such oil immersion objectives are designed to be used only with glass coverslips. In addition, the sample is presented upside down, such that the IR excitation, being delivered from beneath in this counter-propagating mode, will strike the sample first without having to be transmitted through a substrate, with associated wavelength transmission and focal dispersion considerations.

![](images/3e6328b1e89a4cd5084c2ab07994deed53779d2c121bed1a25f8f2ac075d8d0e.jpg)  
FIG. 14. Various objective/sample configurations for measurement in counter-propagating mode.

Lipid image (1740 cm-1)  
![](images/0d707fb738b9201b7287dec73ae7be43a019c8e75385f32c6dc4e706db2915a4.jpg)  
FIG. 15. Sub-300 nm spatial resolution O-PTIR image acquired in counter-propagating mode with a 1.3 NA oil objective on a dried biological cell at the 1740 cm−1 absorption peak indicated with the blue arrow on the spectrum at the bottom right. The sample is courtesy of Gough, measurement by Photothermal Spectroscopy Corp., used with permission.

One important consideration when using glass substrates, be it in counter-propagating mode or co-propagating mode, is that with thinner samples ≲7–10 μm, as in the case of a single dried cell as shown in Fig. 15, that since the IR beam is passing through the sample and interacting with glass substrate, some broad silicate absorbances, with superimposed IR absorbances from the sample, are evident in the spectral range of ∼1300–800 cm− . For any single frequency imaging, this will need to be factored into appropriate selection of ratio image combinations, but for instances of where the biomolecular spectral features lie outside of this glass region, such as protein and lipid absorbances, such glass substrates are ideal and very practical as they align well with existing typical biological sample preparation workflows.

Similarly, in Fig. 16 we show the applicability of regular 1 mm thick glass slides as substrates for O-PTIR. Here, a regular histological tissue section has been placed on a standard 1 mm glass slide and measured in counter-propagating mode, but this time with a low magnification, low NA glass objective as only low NA glass objectives provide good, distortion-free imaging when measuring through a relatively thick optical element, such a 1 mm glass slide in this case. The use of a low NA probe objective also provides benefits in terms of a larger measurement spot size (∼1 μm), which is useful when need to image larger FOVs but also in terms of a deeper depth of field, which can be advantageous for tissue sections with higher topological variability. It is worth noting that, in this case, compared to Fig. 15 above, no broad glass silicate features are observed, as in this case, the sample was relatively thick at least 7–10 μm. This means that little to no IR energy is transmitted to the underlying glass substrate, thus no glass features are observed.

## O-PTIR sample thickness/size impacts and sensitivity limits

Unlike conventional transmission infrared measurements, O-PTIR can measure arbitrarily thick samples when operated in copropagating mode, whereas transmission IR requires a sample thin enough for IR radiation to transmit through it to a detector. On the other end of the size scale, O-PTIR has also been used to measure very small objects below the detection sensitivity of conventional IR, including polymeric microspheres to 100 nm diameter,16 individual bacteria,16,46–48 and sub-micron lipid droplets. 22,49 The measured signal level in O-PTIR typically has a somewhat complex dependence on the size of the object measured in part because the measured signal depends on not only the peak temperature but also the thermal decay dynamics, which impacts the time duration of the photothermal distortion sampled by the probe beam. Smaller objects lose heat more rapidly, and hence, the demodulated photothermal signal can have nonlinear dependence on an object’s size. Li et al. have modeled these effects16 and example measurements of the thermal decay dynamics of different cellular components are shown in Fig. 17, adapted from the work of Yin et $a l . ^ { 2 2 }$ Interferometric effects can also enhance or reduce the detection sensitivity based on coherent interference of the probe beam interactions with the sample of interest and with an underlying substrate.16,50 The sample thermal diffusivity (which depends on thermal conductivity, heat capacity, and density) also impact the thermal decay dynamics and hence the detected signal level.

![](images/a48d500369e675ded147c4234e26eb468c5f846a32a443c4e8ad9ce09ecb6551.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | O-PTIR (nV) |
| ----------------- | ----------- |
| 1242              | 4.6354      |
</details>

IR image @ 1240 cm-1  
![](images/10106270346c9d0ea690eea478c1fac55104f7c912613cc951f0653e52c613da.jpg)

<details>
<summary>heatmap</summary>

| Longitude (μm) | Latitude (μm) | Value (mV) |
| -------------- | ------------- | ---------- |
| 0              | 0             | 0.002      |
| 15             | 16.67         | 2.502      |
| 30             | 33.33         | 5.001      |
| 45             | 50            | 7.501      |
| 60             | 50            | 1          |
</details>

![](images/4dbe8151dc7c23641cc4d059b355b13027f6925d4ab6339e24f1547694a0effa.jpg)

<details>
<summary>text_image</summary>

10x, 0.3NA
Probe
Low mag, long
WD objective
std glass slide
(1mm thick)
Reflective
Objective
(Cassegrain)
IR
</details>

FIG. 16. Use of low NA probe beam objective for large area O-PTIR mapping.  
![](images/08f7a1b460befca8e17137360ee6148ca125b6355ffc72748167d0e7d7586b9d.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Lipid droplet 1750cm⁻¹ | Nucleus 1655cm⁻¹ | Cytoplasm 1655cm⁻¹ |
|-----------|------------------------|------------------|--------------------|
| 0         | 0                      | 0                | 0                  |
| 1         | 20                     | 55               | 12                 |
| 2         | 5                      | 30               | 8                  |
| 3         | 2                      | 15               | 4                  |
| 4         | 1                      | 8                | 2                  |
| 5         | 0.5                    | 4                | 1                  |
| 6         | 0.3                    | 2                | 0.5                |
| 7         | 0.2                    | 1                | 0.3                |
| 8         | 0.1                    | 0.5              | 0.2                |
| 9         | 0                      | 0                | 0                  |
</details>

FIG. 17. Example peak signal levels and thermal decay times for different cellular components. Colored traces show the time-dependent photothermal response of the cellular components. (Thin black traces show auxiliary measurements of the IR source pulses.) Adapted and reprinted with permission from Yin et al., Nat. Commun. 12(1), 7097 (2021). Copyright 2021 Author(s), licensed under a Creative Commons Attribution 4.0 License.

## Quantitation

A common question about O-PTIR is whether it can be used for quantitative extraction of component concentrations similar to the use of the Beer–Lambert law in conventional FTIR. The signal in O-PTIR does have a linear dependence on the concentration and molecular absorptivity but has a more complex dependence on the object size due to the effects mentioned above. The O-PTIR signal also depends on several other material properties not included in Beer–Lambert, including the sample density, heat capacity, and thermal conductivity. As such, the O-PTIR signal amplitude itself is generally not used for direct quantitation, but semi-quantitative measurements can be made using ratiometric approaches, e.g., the ratio of spectral band intensities or ratios of O-PTIR absorption images at different wavelengths. For example, one can use the ratio of absorption of a carbonyl ester band to an amide band to obtain a relative measurement of lipid to protein concentration variations. These approaches are discussed in more detail later in this article. Pavlovetc et al. have performed systematic tests of the photothermal signal intensity vs radius for polystyrene microspheres and observed a linear dependence on temperature rise and quadratic dependence on radius.51

## Detector choice for photosensitive samples

Traditional IR systems (both FTIR and direct QCL based) employ infrared detectors and also often require cryogenically cooled IR detectors (e.g., with liquid nitrogen). Advantageously, O-PTIR is typically performed with one of two different visible, room-temperature photodetectors. For routine work at mW probe power levels, silicon PIN photodiodes are used, which provide excellent SNR and dynamic range. For samples that are highly sensitive to potential photodamage from the visible probe beam, more sensitive detectors such as avalanche photodiodes (APD) or photomultiplier tubes (PMT) can be used. The use of APDs enables O-PTIR measurements at microwatt level probe power levels, which has proven essential, for example, is common for the measurement of dark, colored, or otherwise easily damaged samples, including samples that are difficult or impossible to measure with Raman spectroscopy due to generally higher required excitation power. The use of microwatt level probe power with APD detectors has enabled vibrational spectroscopic measurements with sub-micron spatial resolution on samples that could potentially be damaged by higher excitation, including pigmented plastics,52 hair,53 polymeric spherulites,54 biological cells,32 and fresh hydrated tissue.38 If when measuring a sample with O-PTIR one observes signal instability and/or morphological or spectral changes in the sample at higher probe powers, the use of lower probe power and APD detection is advised.

## Avoiding sample damage

For most samples, it is possible to find operating conditions to avoid sample damage. Commercial O-PTIR instruments have variable attenuators to permit adjustment of the IR and/or probe power on the sample. In general, the SNR increases with increasing probe and IR power as long as the intensities do not exceed the damage threshold of the sample. When adjusting settings to determine optimal operating conditions, it is useful to perform the following steps.

(1) Acquire optical images before and after O-PTIR spectral measurements to verify that the sample is not visibly altered by the IR and/or probe beams.  
(2) Observe the O-PTIR signal intensity at a strongly absorbing band over time and ensure that it is stable. If the O-PTIR

signal rises or falls quickly, it is usually an indication that the sample’s damage threshold is exceeded.

(3) Acquire multiple successive spectra from the same location to ensure the spectra are reproducible or observe the co averaged spectral acquisition, keeping an eye out for any drastic spectral changes from scan to scan, which would indicate likely sample damage. Each scan in a set of co-averaged spectra should help increase spectral SNR only and not result in spectral changes.

If damage/instability is observed, the IR and/or probe power should be reduced until stability and reproducibility are achieved. Dark or colored samples tend to be more easily damaged by the visible probe beam and can be more optimally measured at lower optical power and using APD detectors as described above. In general, organic and polymeric samples may need to be measured at lower IR/probe power, whereas inorganic samples can usually tolerate higher IR/probe powers. Examples of diagnostics for detecting damage and methods to avoid are described by Sandt and Borondics.53

## Molecular orientation

O-PTIR has proven to be a powerful tool for examining molecular orientation in both polymeric54,55 and biological56,57 applications. Taking advantage of the inherent high polarization of mid-IR laser sources used in O-PTIR, researchers have studied the polarization sensitivity of IR absorption bands to infer details about the molecular orientation of the absorbing bonds. In particular, the efficiency of excitation of a molecular bond is dependent on the relative alignment of the bond axis and the electric field of the incident IR radiation. Measurements of O-PTIR spectra and/or images are usually performed at multiple relative polarization orientations. Early work was done by rotating the sample on the measurement stage, but more recently, polarization rotation capabilities have been integrated into O-PTIR instruments (Fig. 18) to adjust the incident orientation of the electric field of the incident IR radiation on the sample at prescribed intervals. To avoid ambiguity in the extracted orientations, measurements are generally performed at three or more polarization orientations to extract molecular orientation angles.54,56

![](images/09c22bf146ca3b2031af9adcef1a96e8befbe88a5e4715aa5194ac98c312b3bf.jpg)

<details>
<summary>text_image</summary>

Incoming polarization
IR light
Eo
Rotatable polarizer
Rotated polarization
θ
Er
</details>

FIG. 18. Schematic for polarization sensitive infrared spectroscopy with O-PTIR. The amount of IR absorption is dependent on the relative angle between the electric field of the IR radiation and the molecular bonds in the irradiated molecule, which controls the efficiency of excitation of molecular bond vibrations. Measuring O-PTIR images and spectra at different polarization rotations provides insight into molecular orientation within a sample.

![](images/1304706d1bf78bb1dbe2af025b9b3f5912e8a3239d2b21164709c86458ad7083.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Parallel Absorbance | Perpendicular Absorbance |
| ----------------- | ------------------- | ------------------------ |
| 1700              | ~0.8                | ~0.2                     |
| 1650              | ~1.2                | ~0.8                     |
| 1600              | ~0.9                | ~0.3                     |
| 1550              | ~1.5                | ~0.1                     |
| 1500              | ~0.7                | ~0.2                     |
| 1450              | ~0.6                | ~0.1                     |
</details>

FIG. 19. Example of molecular orientation effects observed in O-PTIR spectra measured on a collagen fibril. Reprinted with permission from Bakir et al., Molecules 25(18), 4295 (2020). Copyright 2020 Author(s), licensed under a Creative Commons Attribution 4.0 License.

Figure 19 shows an example of polarization sensitive O-PTIR measurements performed on a collagen fibril showing a reversal in the relative amplitudes of the amide I and amide II proteinassociated bands.57 Figure 20 shows the measurements extracting the quantitative molecular orientations of collagen in a biological tissue section, and Fig. 21 shows the 3D mapping of molecular orientation in a polymer spherulite.54

![](images/245d3394f9f7d30081d2219d5d25720c5c2fc3f5c7ef1f80625c456c33c76f44.jpg)

<details>
<summary>text_image</summary>

(a)
O-PTIR v_as(C-O-C)
25 µm
5 µm
5 µm
(b) In-plane angle relative to radial axes ψ_r
25 µm
R1
R3
R2
90°
60°
30°
0°
</details>

FIG. 21. 3D mapping of polymer chain orientation in a spherulite. Reprinted with permission from Koziol et al., J. Am. Chem. Soc. 144(31), 14278 (2022). Copyright 2022 Author(s), licensed under a Creative Commons Attribution 4.0 License.

![](images/83735d5978720c22c8514e68b522b0b822b3b023917af5ac63de90eca1a537cb.jpg)

<details>
<summary>text_image</summary>

(a)
150µm
(b)
1.0
0
(c)
(d)
90
90
90
(f)
-90
-90
-40
0.6
0.5
0.4
0.3
0.2
0.1
0.0
-40
-30
-20
-10
0
-25
-35
-40
</details>

FIG. 20. Collagen and its orientation from polarization-sensitive O-PTIR imaging at two wavenumbers (1536 and 1660 cm−1); visible image (a) and O-PTIR image (b) at 1660 cm−1 shows a region of interest from bone marrow biopsy that includes trabecular bone (yellow arrows), blood vessel (red arrows), and diffused collagen (green arrow). The image in panel (c) shows the polarization sensitivity of each pixel computed from polarization-sensitive O-PTIR images; collagen orientation represented with amide ratios from three polarization as red-green-blue color channels of the image in panel (d) with red: R0○, green: R45○, and blue: R-45○. The image in panel (e) shows principal orientation (angle in degrees) of fibers in this image as indicated by the color bar. The image in panel (f) shows the projection of the tensor onto an angular distribution. Reprinted with permission from Mankar et al., Appl. Spectrosc. 76(4), 508 (2022). Copyright 2022 SAGE Publications.

<table><tr><td>Sample type</td><td>Preferred substrate(s)</td><td>Substrate thickness</td><td>Sample prep</td><td>Example reference</td><td>Co-prop</td><td>Counter-prop</td><td>Detection path</td><td>Sample orientation</td><td>Objective style</td><td>Objective mag.</td><td>Objective NA</td><td>Achievable spatial resolution (nm)</td></tr><tr><td rowspan="3">Thin film/tissue sections(&lt;5-10μm thick)Thick tissue sections(&gt;10μm) or blocks or live hydrated tissues</td><td>Glass slides</td><td>1-2 mm</td><td rowspan="2">Embed, microtome, and dewax</td><td>Mankar et al.56</td><td>X</td><td></td><td>Epi</td><td>Upright</td><td>Cassegrain</td><td>40×</td><td>0.75</td><td>500-800</td></tr><tr><td>CaF2</td><td>350 μm</td><td>Prater et al.39</td><td></td><td>X</td><td>Epi</td><td>Upright</td><td>Refractive</td><td>50×</td><td>0.8</td><td>300-500</td></tr><tr><td>Glass slide</td><td>Any</td><td></td><td>Gvazava et al.69</td><td>X</td><td></td><td>Epi</td><td>Upright</td><td>Cassegrain</td><td>40×</td><td>0.78</td><td>500-800</td></tr><tr><td>Dried cells</td><td>CaF2</td><td>350 μm</td><td>Culture and fix or drop cast</td><td>Spadea et al.35 Bai et al.25</td><td></td><td>X</td><td>Epi</td><td>Upright</td><td>Refractive</td><td>50×</td><td>0.8</td><td>300-500</td></tr><tr><td rowspan="3">Live/hydrated cells</td><td>Glass slidea</td><td>1 mm</td><td></td><td>Kansiz et al.71</td><td>X</td><td></td><td>Epi</td><td>Upright</td><td>Cassegrain</td><td>40×</td><td>0.78</td><td>500-800</td></tr><tr><td>Glass coverslip, ~5 μm spacer, CaF2 window</td><td>170 μm glass coverslip on top, 350 μm CaF2 on bottom</td><td></td><td></td><td></td><td>X</td><td>Trans</td><td>Upright</td><td>Coverslip compensated refractive</td><td>40×</td><td>0.95</td><td>300-500</td></tr><tr><td>CaF2 window/5 μm spacer, glass slide or coverslip</td><td>350 μm CaF2 on top, thin or thick glass (up to 1 mm) on bottom</td><td></td><td>Shuster et al.49</td><td>X</td><td></td><td>Trans</td><td>Cells on inverted CaF2 window, glass coverslip beneath</td><td>Cassegrain</td><td>40×</td><td>0.8</td><td>500-800</td></tr><tr><td rowspan="4">Bacteria/spores and other small(&lt;5-10μm thick)particulatesMicroplastic particlesAtmospheric particles,drug aerosols</td><td>Glassa</td><td>Any</td><td rowspan="2">Culture and incubate or drop cast</td><td rowspan="2">Xu et al.37 Lima et al.47-49</td><td rowspan="2">X</td><td></td><td>Epi</td><td>Upright</td><td>Cassegrain</td><td>40×</td><td>0.78</td><td>500-800</td></tr><tr><td>CaF2</td><td>350 μm</td><td>X</td><td>Epi</td><td>Upright</td><td>Refractive</td><td>50×</td><td>0.8</td><td>300-500</td></tr><tr><td>Gold coated polycarbonate filter, Simpore filter</td><td>Any</td><td>Vacuum filtration</td><td>Tarafdar et al.89</td><td></td><td></td><td>Epi</td><td>Upright</td><td>Cassegrain</td><td>40×</td><td>0.78</td><td>500-800</td></tr><tr><td>CaF2 or glass for &gt;5 μm particles</td><td>Any</td><td>Atmospheric sampling/fractionation</td><td>Khanal et al.88Olson et al.90</td><td>X</td><td></td><td>Epi</td><td>Upright</td><td>Cassegrain</td><td>40×</td><td>0.78</td><td>500-800</td></tr><tr><td>Thick (&gt;10μm) and/or opaque samples, bulk samples</td><td>Any</td><td>Any</td><td>None if smooth, cut/polish if needed</td><td>Jubb et al.124</td><td>X</td><td></td><td>Epi</td><td>Upright</td><td>Cassegrain</td><td>40×</td><td>0.78</td><td>500-800</td></tr><tr><td>Polymer multilayers, cultural heritage</td><td>CaF2 for sections &lt;10 μm, any for &gt;10 μm</td><td>Any</td><td>Embed in epoxy and cross-section</td><td>Marcott et al.116Beltran et al.106</td><td>X</td><td></td><td>Epi</td><td>Upright</td><td>Cassegrain</td><td>40×</td><td>0.78</td><td>500-800</td></tr></table>

aUse of glass slides can provide interference with a glass silicate band (∼1300–800 cm−1), particularly for samples ≪10 μm thickness, with some biological bands (such as nucleic acids and carbohydrates), but suitable for studies of proteins with a clear access to amide I (for protein secondary structure) and amide II, lipids. For samples >10 μm thickness, glass absorption interference is often negligible across the entire IR spectral region.

## SAMPLE PREPARATION TECHNIQUES

Sample preparation for O-PTIR measurements depends on the sample type and can range from immediate measurement with no sample preparation to more complex techniques including labeling, fixing, sectioning, digestion, filtration, and other approaches depending on the sample and analysis requirements. Common sample preparation techniques are described in the following and presented in Table I, along with recommended measurement configurations for each sample type.

## No sample preparation

Many samples require no special sample preparation. If the features of interest occur on the top surface of a sample, many samples can be loaded into the microscope and measured directly. O-PTIR microscopes typically have mounting features for glass slides and other similar sized sample holders and available sample areas of around $1 0 0 \times 1 0 0 ~ \mathrm { m m } ^ { 2 }$ . In the case of larger samples, it may be necessary to simply cut a portion that will fit on the sample stage. Examples of such samples include thin films/coatings on substrates, polymeric materials, and similar bulk materials.

## Drop casting/spin coating

For many polymeric materials and biological materials such as cell suspensions, drop casting is a simple approach for sample preparation. In this method, the sample suspended or dissolved in a solvent is typically pipetted onto a sample substrate and the solvent is permitted to evaporate. Serial dilutions are often used, e.g., stock solution, 10× dilution, 100× dilution, 1000× dilution to find a concentration that provides adequate coverage without excessive pileup of sample material. To achieve uniform coating thicknesses for polymer films, spin-coating approaches26 may be used where the solution is pipetted onto a spinning sample at a given rotation speed to achieve the desired thickness.

## Sectioning/polishing

Sectioning and/or polishing are often used for tissue (sectioning) and geological samples (sectioning/polishing). For tissue samples, sectioning is generally used to extract a slice of tissue from a tumor biopsy or from a specific location in an organ. Such slices are usually created via microtomy and may involve embedding tissue prior to sectioning. It should be noted that most embedding materials (e.g., paraffin, epoxy resins, and nitrocellulose) have strong IR absorption peaks of their own, so it may be desirable to remove the embedding medium prior to chemical analysis by O-PTIR. The use of cryomicrotomy (i.e., freezing the tissue before sectioning) can eliminate the need to add and then later remove embedding material. Cross sectioning can also be useful when studying layered materials, e.g., a polymer laminate film, cultural heritage items such as paintings, and the examination of sub-surface defects. For fine sectioning, microtomy is still preferred, but in some cases, sectioning by a razor blade may produce sufficient results.

## Fixed cells, including fluorescent labeling

For biological cells, sample preparation techniques already commonly used for conventional light microscopy, including fluorescence microscopy, are often directly applicable to O-PTIR measurements. For example, conventional approaches for cell culturing, fixing, and immunofluorescence labeling are all compatible with O-PTIR measurements. Unlike Raman microscopy, O-PTIR measurements are immune to fluorescence interference and in fact fluorescence labeling can be a very powerful technique to help guide O-PTIR measurements to specific regions of interest.39,58 Antifade media should generally be avoided in fluorescent labeling of biological samples since common antifade media while optically transparent, often contain strong IR absorption bands that can overlap/interfere with the measurement of biologically relevant IR bands.

For co-propagating measurements, cells can be deposited/ incubated on conventional glass slides and cover slips. Plastic bottomed petri dishes are generally not recommended because they have strong IR absorption bands that can overlap with some biologi cally relevant absorption bands. Zhang et al. have used conventional plastic petri dishes with the bottoms replaced with CaF windows for some measurements of biological samples in aqueous solutions.11 For the counter-propagating O-PTIR configuration, cells should be incubated or deposited on IR transparent windows to permit IR excitation light to reach the sample. The most commonly used IR transparent windows that are thin CaF disks, for example, 10 mm diameter, 0.35 mm thick, e.g., available from Crystran. These CaF2 disks can be directly mounted into an appropriate sample holder for either measurements in air or aqueous environments.

In the case of bacteria, aqueous suspensions are often drop cast directly onto an appropriate sample support, e.g., glass slides, coverslips, or CaF disks and air dried without fixation. For mammalian cells where it is important to preserve the structure of the cell, conventional cell fixation techniques can be appropriate, although with certain caveats. Chemical fixation using cross-linking fixatives, such as formaldehyde or glutaraldehyde, form additional chemical bonds in the sample, which while preserving the cell morphology can introduce conformational changes that can impact the IR spectra. For O-PTIR measurements, where the focus is on detecting specific chemical bonds and maintaining the native chemical state of the sample, alcohol-based fixation (e.g., methanol or ethanol) may be preferred. These fixatives are less likely to introduce new chem ical groups and generally cause fewer changes in chemical bond structures compared to aldehydes.

## Sample preparation for live cell measurements

O-PTIR measurements on live cells are generally performed by first culturing cells on a glass or IR transparent cover slip and then mounting the cover slip in a sealed sandwich configuration or in a flow-through fluid cell. Sealed fluid sandwiches can be readily made by cutting a small piece of thin double-sided tape (e.g., 3M 8260059), punching a hole in the center and adhering the tape to a glass cover slip to create a small well. A small drop of buffer containing suspended cells can be pipetted into the well and then covered and sealed with an IR transparent window. Depending on the cell type, the cells can remain alive and hydrated for tens of minutes to a few days. For better control of temperature, $\mathrm { C O } _ { 2 } ,$ nutrients, and/or for the introduction of drugs or other bioactive agents, flow-through fluid cells can be used. It is often desirable to limit the thickness of the water layer within the fluid cell to prevent excessive IR absorption by water. In some cases, it can be desirable to use D2O (heavy water), which shifts the H–O–H bending absorption band in water away from the amide I band associated with biological proteins.22 As will be discussed later, $\mathrm { D } _ { 2 } \mathrm { O }$ has also been used for isotopic labeling of cells, for example, for metabolic studies.

## Measurement and data processing approaches

A key aspect of obtaining informative data is the approach to data acquisition and analysis. For O-PTIR imaging, it is important to understand that the brightness at any pixel is not just dependent on the IR absorptivity, but can also depend on the sample’s thickness, distance from the focal plane, and other thermophysical properties such as heat capacity, density, thermal conductivity, and size, all of which can contribute to the sample’s maximum temperature and how quickly it cools after each IR pulse. As such, the contrast in an O-PTIR image at a single wavenumber may not be representative of the IR absorption only. To overcome this issue, two different approaches are recommended: (1) multi-wavenumber ratiometric images and (2) multi-color overlay images.

## Ratiometric images

Consider an O-PTIR image with a signal intensity $S ( x , y , \nu )$ , where (x, y) are the locations on the sample and ν is the IR wavenumber used to collect the O-PTIR image. This signal can be broken down into two separate functions,

$$
S (x, y, \nu) = A (x, y, \nu) B (x, y). \tag {7}
$$

(1) $A ( x , y , \nu )$ which represents the IR absorption as a function of $( x , y )$ position and wavenumber ν  
(2) $B ( x , y )$ which represents the other sources of variation in the O-PTIR signal, for example, reflectivity, sample thickness, and thermal/mechanical properties.

Calculating the ratio of the signal S at two different wavenumbers ν1 and ν2 gives

$$
\frac {S (x , y , v 1)}{S (x , y , v 2)} = \frac {A (x , y , v 1) B (x , y)}{A (x , y , v 2) B (x , y)} = \frac {A (x , y , v 1)}{A (x , y , v 2)}. \tag {8}
$$

In this case, the reflectivity, sample thickness, and thermal/mechanical properties are constant at each point in the sample; thus, the $B ( x , y )$ term in the numerator and denominator are the same and cancel out in the ratio. The ratio image thus reveals the variation in IR absorption while eliminating effects from other sample properties. Thus, it is strongly recommended to display ratio images and optionally any single wavenumber images. Example ratiometric images from a widefield fluorescence-detected O-PTIR measurement are shown in Fig. 22.

For single point measurements, ratiometric images should preferably be acquired in an interleaved mode where O-PTIR images are acquired at different wavelengths by alternating between wave lengths at each scan line in the image to avoid any image drift between successive images. Similarly, for widefield O-PTIR measurements it is advisable to acquire images at wavenumbers of interest over a short period of time or otherwise correct for drift to ensure registration between the images in the ratio calculation. When performing a ratio calculation, it can be desirable to employ a minimum denominator threshold to coerce the ratio calculation to zero for regions of the denominator images where there is no appreciable signal. (This avoids the issue of dividing by a number near zero, which could otherwise obscure real features in the image ratio.)

## Multi-color overlay images

Multi-color overlay images can also be a useful way to high light differences in absorption at different IR absorption bands. Although this approach does not eliminate contrast from nonabsorptive variables, it does visually highlight where the absorption is different between different regions in a sample. Multi-color overlays are performed analogously to their common use in fluorescence microscopy, except instead of assigning a different color to each fluorophore band, a different color is assigned to each IR absorption band. Current O-PTIR instruments permit automated collection of a sequence of O-PTIR images at different IR bands, which can then be quickly assembled into an RGB overlay image.

![](images/a5605ff8a53fd5ee81f2a4f4feb5973cf7e93043935b1eb6a1e0c92519a32503.jpg)

<details>
<summary>heatmap</summary>

| Panel | IR absorption ratio (cm⁻¹/1072 cm⁻¹) |
|-------|-------------------------------------|
| (a)   | 1200                                |
| (b)   | 1648                                |
</details>

FIG. 22. Examples of ratiometric images of a diatom displaying the ratio of IR absorption at different IR bands. (a) Ratio image of two different silica bands; (b) ratio image of protein to silica bands. In both images, the ratio has been set to zero when the absorption signal was below a given threshold (i.e., regions with minimal signal away from the diatom). Wide-field fluorescence-detected O-PTIR images are shown. Reprinted with permission from Prater et al.,45 Appl. Spectrosc. (published online) (2024). Copyright 2024 The Authors.

## Hyperspectral data analysis

O-PTIR researchers are increasingly collecting larger hyperspectral datasets, which involve either the measurements of spectra at many locations on a sample or alternately the collection of O-PTIR images at many IR wavenumbers. In the cases of large hyperspectral datasets, multivariate analyses and machine learning approaches can be very helpful. Commercial programs, such as CytoSpec60 Eigenvector Research61 products, and the open source analysis package Quasar,62 all offer extensive capabilities for hyperspectral data analysis, including techniques such as principal component analysis; various clustering approaches, including k-means and hierarchical cluster analysis; and spectral decomposition such as multivariate curve resolution. Such approaches can be useful for analyzing large datasets to generate maps of the distribution of different chemical species and extracting representative spectra. Supervised machine learning approaches can also be used to train models to classify sample regions based on subtle spectral variations, for example, for tissue classification.63 Multivariate analysis/machine learning approaches can also be used to determine which absorption bands most significantly discriminate different chemical species/spectral variations within a sample and can be used to dramatically reduce the number of IR bands measured and signif icantly reduced required measurement time. For example, Gajjela et al. demonstrated that O-PTIR imaging at only five wavenumbers combined with deep learning was sufficient to outperform state-ofthe-art diffraction-limited conventional IR imaging with up to 235 wavenumbers.63 Machine learning approaches have also been used for microplastics identification.64

## O-PTIR APPLICATIONS

## Biological and biomedical applications of O-PTIR

Mid-infrared spectroscopy and chemical imaging have proven to be vital tools in the life sciences, offering non-destructive, label-free, and chemically specific insights into biological samples. Infrared spectroscopy enables the identification and characterization of key biomolecular categories, including proteins, lipids, nucleic acids, and carbohydrates. With its improved spatial resolution, O-PTIR significantly enhanced the power of IR spectroscopy by providing detailed spatial distribution and concentration data of these molecules with sub-micron spatial resolution. O-PTIR research in the life sciences facilitates a deeper understanding of cellular processes, disease mechanisms, and the composition of complex bio logical systems. The following sections summarize recent O-PTIR research in biological and biomedical sciences.

## IR tags

Label-free imaging of the main bio macromolecules, such as proteins, lipids, carbohydrates, and nucleic acids, with infrared spectroscopy have been much touted and demonstrated. However, since IR spectroscopy is a “total” analysis technique, i.e., one where all IR active molecules within the measurement volume will contribute to the spectrum, when specific and lower concentration components, such as metabolites are required to be chemically imaged, interferences from the surrounding higher concentrations biomolecules can make this very challenging.

One approach to increase the specificity of IR spectroscopy is to employ IR tags (also referred to as probes and labels). IR tags can be broadly categorized into two classes: (1) Stable Isotopic labeling and (2) so-called “silent region tags.”

Stable isotope IR labels most commonly include ${ } ^ { 2 } \mathrm { H ( D ) } , { } ^ { 1 3 } \mathrm { C } ,$ and $^ { 1 5 } \mathrm { N } ,$ , although, in principle, other stable isotopes will also work. Stable isotopes for increased IR spectroscopic specificity work by generating additional spectral contrast taking advantage of molecular vibrations involving heavier atoms (isotopes) that result in a significant spectral redshift (lower wavenumber) in absorbance of the relevant band. In the case of the C–H vs C–D stretching vibration, as the relative atomic weight difference between H and D is so large, this causes a very large spectral redshift on the order of ∼700 cm with C–H stretching vibrations typically at $3 0 0 0 { - } 2 8 0 0 ~ \mathrm { c m } ^ { - 1 }$ and C–D stretching vibrations typically at $2 3 \mathrm { { \dot { 0 } 0 - 2 1 0 0 ~ c m ^ { - 1 } } }$ , which turn up in the spectral silent region (more on that is provided in the following). With the relative atomic weight differences of $^ { \cdot 1 3 } \mathrm { C }$ and $^ { 1 2 } \mathrm { C }$ being much smaller, for protein amide bands, this redshift is on the order of ∼40 cm−1, shifting $^ { 1 2 } \mathrm { C }$ labeled amide bands from ∼1655 to ∼1615 cm $^ { - 1 } \mathrm { f o r } ^ { 1 3 } \mathrm { C }$ labeled amide bands,46 as shown in Fig. 23.

Silent region IR tags deliver specificity and spectral contrast by virtue of their unique spectral features in the so-called infrared “silent region,” typically between $2 6 0 0 { - } 1 8 0 0 ~ \mathrm { c m ^ { - 1 } } ~ ( \mathrm { s e e ~ F i g . ~ 1 } )$ .

Common functional groups with IR active absorbances in this IR silent region include alkynes, nitriles, and azides. While their unique spectral absorbances in the otherwise absorbance-free “silent window” of the spectrum provide the unique spectral contrast, the ability to modify chemicals to incorporate such moieties provides the key element of designer chemical specificity. This chemical specificity is analogous to that of fluorescent labeling where excellent specificity is typically attained, but unlike fluorescent labeling, these IR probes typically have an ultra-low molecular weight, in stark contrast to the often-bulky labels, such as green fluorescent protein (GFP), which has become so commonplace in fluorescence imaging but runs the risk of perturbing normal metabolic functions.

![](images/c22c244bdd975f46d79e5ffbcc864434228e86fa91f9b8f6a8285a15e8f38ebf.jpg)

<details>
<summary>line chart</summary>

| 2000 | 1.8 |  |  |  |
| --- | --- | --- | --- | --- |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 2000 |  |  |  |  |
| 1887 |  |  |  |  |
| 1887 |  |  |  |  |
| 1887 |  |  |  |  |
| 1887 |  |  |  |  |
| 1887 |  |  |  |  |
| 1887 |  |  |  |  |
</details>

FIG. 23. O-PTIR measurements with stable isotope labeling showing amide I and II regions $( 1 4 0 0 - 1 8 0 0 \mathsf { c m } ^ { - 1 } )$ on single E. coli cells incubated with $\bar { 1 2 } \bar { ( ) ^ { 1 4 } } \bar { 1 }$ (blue line), $^ { 1 3 } { \mathsf { C } } ^ { 1 4 } { \mathsf { N } }$ (red line), $^ { 1 2 } { \mathsf C } ^ { 1 5 } { \mathsf N } ^ { ' }$ (yellow line), and $^ { 1 3 } { \mathsf C } ^ { 1 5 } { \mathsf N }$ (green line). Data reprinted with permission from Lima et al., Anal. Chem. 93(6), 3082 (2021). Copyright 2021 American Chemical Society.

Recent examples of the use of stable isotope labeling from Shams et $a l . ^ { 6 5 }$ have been applied to bacterial antimicrobial susceptibility testing (AST), where individual bacterial cells were spectrally measured and chemically imaged with O-PTIR. In this example, various E. coli strains were grown in dilute concentrations of $\mathrm { D } _ { 2 } \mathrm { O }$ in the presence of antimicrobial agents with the incorporation of deuterium, detected as C–D vibrations, as a marker for metabolism. The benefit of such a single-cell measurement approach is that far less biomass is required, thus greatly speeding up culturing times and thus time-to-answer, which is critical when rapid AST is required. Other examples from Lima et al.46 demonstrate the applicability of $^ { 1 3 } \mathrm { C }$ and $^ { 1 5 } \mathrm { N }$ labeling via $^ { 1 3 } \mathrm { C }$ labeled glucose and 15N labeled ammonium chloride to explore metabolic activity of individual bacterial cells and their interactions within microbial communities.

Examples of the usage of IR tags for submicron O-PTIR anal ysis of single and intra-cellular analysis of mammalian (adipocyte) cells have been conducted by Shuster et $a l . ^ { 4 9 }$ The researchers initially grew cells in regular $^ { 1 2 } \mathrm { \dot { C } }$ glucose, followed by a switch to $^ { 1 3 } \mathrm { C }$ labeled glucose. This labeled glucose was metabolized and incorporated into the triglycerides in cell lipid droplets, with the $^ { 1 3 } \mathrm { C }$ lipid band appearing at $\stackrel { \cdot } { 1 7 } 0 3 \mathrm { c m } ^ { - 1 }$ compared to 1747 $\mathrm { c m } ^ { - 1 }$ for $^ { 1 2 } \mathrm { C }$ lipid, providing for a clear peak separation [see Fig. 24(d) below]. The ratio of these two bands, which is correlated to the rate of metabolism, was measured over 72 h. This ratio was also measured using rapid, high spatial resolution single frequency O-PTIR images, providing, both inter- and intra-cellular spatial information on rate of metabolism [see Fig. 24(c) below]. In also a first for the O-PTIR measurements, this experiment was conducted with live, metabolizing cells in water.

a  
![](images/53e908001c01274605c626fc7b34b55414ba3599fc88a28095f006408589871b.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular structures labeled 'Brightfield' (no text or symbols within the image content)
</details>

b  
![](images/6e8a59d634c15e499b1da16bde3f2a9fe0eaf4575d49b0ec93b15c97b630eae9.jpg)

<details>
<summary>text_image</summary>

OPTIR Intensity (mV)
250
1747 cm⁻¹
</details>

c  
![](images/9c93e9bf00b4cd8ae8b71225378a6971e9082e906aab9ffa230c7d5e91bf7bd5.jpg)

<details>
<summary>text_image</summary>

Ratio
13C/12C lipid corrected
0
</details>

scale bar = 20 μm

d  
![](images/66bb582c1d8455a054d7e87b63d1107594f61416a58349acc6535902ee92e709.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | live | fixed |
| ----------------- | ---- | ----- |
| 1800              | 0.0  | 0.0   |
| 1600              | 0.8  | 0.7   |
| 1400              | 0.5  | 0.4   |
| 1200              | 0.5  | 0.6   |
| 1000              | 0.2  | 0.3   |
| 800               | 0.0  | 0.0   |
</details>

FIG. 24. O-PTIR measurements of lipogenesis in live adipocytes 72 h after feeding with 13C glucose. (a) Brightfield image. (b) Single wavenumber image collected at 1747 cm−1 corresponding with 12C lipid ester carbonyl band. (c) Ratio image showing 13C lipid ester carbonyl (1703 cm−1)/12C lipid ester carbonyl (1747 cm−1) after correction for amide-I, and water bending band highlighting varying rates of DNL across the cell. Data collected in PBS. (d) Representative spectra from live and fixed cells. Spectra from live (blue) and fixed (orange) differentiated 3T3-L1 adipocytes 72 h after feeding with 13C glucose. Reprinted with permission from Shuster et al., J. Phys. Chem. B 127(13), 2918 (2023). Copyright 2023 American Chemical Society.

A recent example of a silent region tagging with azides yields from Bai et $a l . , ^ { 2 5 }$ where azide-labeled palmitate was used to investigate the lipid metabolism of single cells from human derived 2D and 3D culture systems. The use of azide labeled palmitic acid provided enhanced sensitivity to lipid detection (including spatial location) of newly synthesized lipids, while the co-located fluorescence imaging modality of O-PTIR proved useful for cell-type identification in complex tissue systems.

Stable isotope labeling has also recently been used for “extraterrestrial” research. Using a reversed $^ { 1 3 } \mathrm { C } \cdot$ -stable isotope labeling experiment, Waajen et $a l . ^ { 6 6 }$ demonstrated the direct metabolic transfer of carbon from an (extraterrestrial) meteorite into microbes, suggesting that organics from meteorites could have been used as a carbon source on early Earth and other habitable planets.

## Neurodegenerative applications of O-PTIR

A very promising application field for O-PTIR has been shown in neurodegenerative disease research. Neurodegenerative diseases can be broadly categorized as diseases where neuronal cells lose function and die over time. Some common examples of neurode generative diseases include Alzheimer’s disease (AD), Parkinson’s disease, and Huntington’s disease. While the mechanisms of these various neurodegenerative diseases are complex and different, they often share a common feature— protein misfolding and aggregation. In addition, herein lies the unique fit that O-PTIR possesses for their study, with O-PTIR delivering both the chemical specificity for determination of the protein secondary structure (and misfolding), and uniquely, by virtue of its submicron spatial resolution, it can also locate and resolve these very small aggregates at physiologically relative spatial scales. The protein secondary structure has long been studied with infrared spectroscopy, and it is well known as a powerful tool for absolute or relative protein secondary structure determination with key protein bands having characteristic peak positions and shapes that are directly related to the proteins secondary structure(s).67

Initial work in this field by Klementieva et $a l . ^ { 6 8 }$ focused on the application of O-PTIR on the study of AD-related amyloid protein aggregation directly in neurons of transgenic mouse models at sub-micron, sub-cellular resolution. In a measurement, first, amyloid protein aggregates were detected in neuronal dendritic spines and neurites, leading to a conclusion that amyloid structures exist in different polymorphic forms, with implications in the possibility of different AD progression mechanisms (Fig. 25).

![](images/a2b61906dc847371789c04ccdafa0aeff92e9b7e96bd8577cdf296dd43e9db04.jpg)

<details>
<summary>line chart</summary>

| Wavenumber, cm⁻¹ | FTIR Absorbance (β) |
| ---------------- | ------------------- |
| 1700             | 0.0                 |
| 1675             | 0.5                 |
| 1650             | 1.0                 |
| 1625             | 0.5                 |
</details>

![](images/b9f18e0a1e883418d1d300833ec3b9e8ca5e7985c3b9a6c7bfee995d549fa732.jpg)

<details>
<summary>line chart</summary>

| Wavenumber, cm⁻¹ | dA²/d²(v) |
| ---------------- | --------- |
| 1693             | -0.5      |
| 1682             | -0.4      |
| 1638             | -0.7      |
| 1628             | -0.3      |
</details>

![](images/7c15c2c25015ae74fdacb9a01ff75f4f03870fec69ce743eae6e3b7a7a290892.jpg)

<details>
<summary>bar chart</summary>

| Group    | β/α   |
| -------- | ----- |
| APP/PS1  | 0.15  |
| WT       | 0.05  |
| APP-KO   | 0.01  |
</details>

![](images/177df9cad3b53401ab373460a62e68c815e0d403b922b0502ff886708158605c.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of a biological or material structure with highlighted regions (no text or symbols)
</details>

![](images/04c335dd6ad3359e7078466459ba37110b48f87879820952341a3c26f926267d.jpg)

<details>
<summary>line chart</summary>

| Wavenumber, cm⁻¹ | Photothermal Amplitude, au |
| ---------------- | -------------------------- |
| 1740             | ~0.2                       |
| 1600             | ~1.0                       |
| 1500             | ~0.6                       |
| 1400             | ~0.3                       |
</details>

![](images/09a0e28fc17334a4921812a408e8aa7300d41902386b9ffd3329190136fcddd4.jpg)

<details>
<summary>line chart</summary>

| Wavenumber, cm⁻¹ | dA²/d²(v) |
| ---------------- | --------- |
| 1693             | -0.5      |
| 1682             | -0.7      |
| 1642             | -0.9      |
| 1635             | -0.6      |
</details>

![](images/7eab9ecd74ccbe41adbb21598485eceab740c48565d6e250ac126f3e32f7734e.jpg)

<details>
<summary>text_image</summary>

g
min max
</details>

![](images/350a454a97773831bdd748901947d9c1482de044ff3b9f9aea6727582155a80e.jpg)

<details>
<summary>line chart</summary>

| Wavenumber, cm⁻¹ | Photothermal Amplitude, au |
| ---------------- | -------------------------- |
| 1740             | ~0.2                       |
| 1640             | ~1.0                       |
</details>

![](images/188d009924e57c15f2b6c787d9ae329e96eca3e27e980752353dd6778a25109c.jpg)

<details>
<summary>bar chart</summary>

| Category           | APP/PS1 | WT   |
| ------------------ | ------- | ---- |
| Unordered structures | 1.0     | 0.8  |
| Lipid oxidation    | 0.3     | 0.2  |
| β-sheet structures | 0.2     | 0.1  |
</details>

FIG. 25. O-PTIR imaging of Aβ aggregates in AD transgenic neurons highlights distinct β-sheet enriched structures, illustrating the technique’s capability to reveal subcellular localization and structural polymorphism of amyloid aggregates in neuronal disease progression. Reprinted with permission from Klementieva et al., Adv. Sci. 7(6), 1903004 (2020). Copyright 2020 Author(s), licensed under a Creative Commons Attribution 4.0 DEED License.

In recent work, Gvazava et $a l . ^ { 6 9 }$ have taken the study of neurodegenerative diseases related protein aggregates into more biologically relevant conditions with the first ever reports of ex vivo and in vivo measurements of living, hydrated tissues with infrared microspectroscopy (Fig. 26). Freshly extracted tissues, unprocessed and fully hydrated tissues from various organs, such as living brain and lung tissues, and in vivo measurement of living salamander embryos were conducted with submicron O-PTIR spatial resolution. The formation of newly formed amyloid aggregates over time in functioning brain tissues was observed for the first time.

![](images/7cbba33113c6c02b2b663366b55e1872d543aaf9cb8f7c0f5df67757f5bd9fec.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Mouse with Brain, Lung, Kidney, Salivary gland, Heart, Liver"] --> B["Tissue biopsy"]
  B --> C["Spatially resolved structural analysis"]
  C --> D["Downstream analysis"]
  D --> E["2000–1000"]
```
</details>

![](images/12c1b1c2666c8b4ee39ae2608fb072cae6c9fb602eb03c2ae15cb05e6bbf0a0f.jpg)

<details>
<summary>line chart</summary>

| Wavenumbers, cm⁻¹ | Normalized intensity |
| ----------------- | -------------------- |
| 1700              | ~1.0                 |
| 1600              | ~0.5                 |
| 1500              | ~0.8                 |
| 1400              | ~0.6                 |
| 1300              | ~0.7                 |
</details>

![](images/d5b0fcda275819ee244306b1d0fade4796478b0645417b9ff09befca5213d673.jpg)

<details>
<summary>line chart</summary>

| Wavenumbers, cm⁻¹ | Normalized intensity (Red Line) | Normalized intensity (Black Line) |
| ----------------- | ------------------------------- | --------------------------------- |
| 1700              | ~0.8                            | ~0.2                              |
| 1600              | ~0.9                            | ~0.3                              |
| 1500              | ~0.6                            | ~0.4                              |
| 1400              | ~0.7                            | ~0.2                              |
| 1300              | ~0.7                            | ~0.2                              |
</details>

![](images/4f1129a9d1088b6efb8b716863f40e09fb19172ac7a470133021657dd9ab6d5d.jpg)

<details>
<summary>line chart</summary>

| Wavenumbers, cm⁻¹ | Normalized intensity (Red Line) | Normalized intensity (Black Line) |
| ----------------- | ------------------------------- | --------------------------------- |
| 1700              | ~0.8                            | ~0.2                              |
| 1600              | ~0.9                            | ~1.0                              |
| 1500              | ~0.7                            | ~0.6                              |
| 1400              | ~0.8                            | ~0.3                              |
| 1300              | ~0.7                            | ~0.2                              |
</details>

![](images/97dcedaa36f2fc2d3036d8ad612a3578bbf29c3f5cf489e860136f74bb562929.jpg)

<details>
<summary>line chart</summary>

| Wavenumbers, cm⁻¹ | Normalized intensity (Red) | Normalized intensity (Blue) |
| ----------------- | -------------------------- | --------------------------- |
| 1700              | ~0.8                       | ~0.4                        |
| 1600              | ~0.9                       | ~0.9                        |
| 1500              | ~0.6                       | ~0.3                        |
| 1400              | ~0.8                       | ~0.2                        |
| 1300              | ~0.7                       | ~0.2                        |
</details>

![](images/f8ea8fed128f0f7f423971bfe27dc0b0041846a14b7db04d39171e1da807ff0a.jpg)

<details>
<summary>line chart</summary>

| Wavenumbers, cm⁻¹ | Normalized intensity (Red Line) | Normalized intensity (Black Line) |
| ----------------- | ------------------------------- | --------------------------------- |
| 1700              | ~0.8                            | ~0.2                              |
| 1600              | ~0.9                            | ~0.9                              |
| 1500              | ~0.7                            | ~0.6                              |
| 1400              | ~0.5                            | ~0.3                              |
| 1300              | ~0.6                            | ~0.2                              |
</details>

![](images/0441df6a18860e99fc277bcc3280f3d1f56a0b98d770d76eb0879f2d6d383f73.jpg)

<details>
<summary>line chart</summary>

| Wavenumbers, cm⁻¹ | Normalized intensity (Red Line) | Normalized intensity (Black Line) |
| ----------------- | ------------------------------- | --------------------------------- |
| 1700              | ~0.8                            | ~0.2                              |
| 1600              | ~0.9                            | ~0.8                              |
| 1500              | ~0.6                            | ~0.3                              |
| 1400              | ~0.7                            | ~0.2                              |
| 1300              | ~0.7                            | ~0.2                              |
</details>

FIG. 26. O-PTIR imaging of diverse fresh, hydrated tissue biopsies with submicron spatial resolution capabilities reveal distinct biochemical compositions within unprocessed living tissues. Reprinted with permissions from Gvazava et al., J. Am. Chem. Soc. 145(45), 24796 (2023). Copyright 2023 Author(s), licensed under a Creative Commons Attribution 4.0 License.

Here, it is remarkable that despite conventional wisdom that protein measurements and in particular protein secondary structure determination in the presence of water is impossible, due to overwhelming water absorbances, O-PTIR has demonstrated a unique and valuable property—that of minimal water interferences. Such a capability is invaluable in the measurement of biological systems as it now promises the ability to measure biochemistry under far more physiologically relevant, hydrated, living conditions. Traditional infrared spectroscopy systems, such as FTIR and direct QCL based systems, will suffer significantly from the strong absorbances of water, which almost perfectly overlaps with the key secondary structurally specific amide I band of proteins.

The unique property of O-PTIR of limited water interferences can be essentially attributed to the fact that the mechanism of IR signal detection is very different between traditional IR spectroscopy systems and O-PTIR. In O-PTIR, since it is differential heating from wavelength specific IR absorbance that is being detected, and not the absorbance of IR light directly, like in traditional IR, the fact that water has a relatively high heat capacity compared to biological tissues, such as muscle,70 means that O-PTIR is in effect less sensitive to the presence of water relative to other biological materials.

## Measurement of biological samples on histopathology glass slides

Kansiz et al.71 demonstrated a potential key enabler of O-PTIR toward a more clinical translation by using regular 1 mm thick glass slides as substrates for the measurement and differentiation of different cancerous cell lines. Since O-PTIR operates in reflection mode, as the most commonly employed mode, transmission of IR light through the substrate is not a consideration like it is with traditional IR instrumentation. Furthermore, as O-PTIR reflection mode operation generates regular, FTIR transmission/ATR-like spectral quality, devoid of any dispersive (Mie) scattering artifacts, collected spectra are highly reproducible, which is a critical prerequisite for the detection of the sorts of subtle spectral differences that are found in different cell lines. In contrast, traditional FTIR/QCL based systems almost never operate in direct reflection mode due to poor IR reflection off tissues and cells and the previously mentioned scattering artifacts. FTIR and QCL microscopes are often operating in a “transflection” mode by depositing samples on an IR reflective substrate made from low-e glass. In practice, this approach is a double-pass transmission measurement that can still suffer from IR standing wave effects and Mie scattering artifacts. While some algo rithms exist for addressing these artifacts, the O-PTIR approach does not require such spectral corrections.

The high-quality, reproducible reflection mode O-PTIR operation thus means that glass slides are now compatible substrates, effectively meaning that standard clinical workflows and practices can be employed, further enhancing the techniques clinical translatability. In contrast again, a traditional FTIR/QCL system would operate often in transmission mode, requiring IR transparent substrates, such as $\mathrm { C a F } _ { 2 } ,$ which are relatively expensive and fragile. Kansiz et al. compared various spectral pre-processing techniques (second derivatives vs no derivatives), modeling techniques (K nearest neighbor vs random forests), and spectral ranges (fingerprint vs C–H region). Classification accuracy of up to 99% was achieved across three different cancerous cell lines using a combination of second derivation spectral pre-processing, random forest modeling with a combined C–H spectral region and fingerprint region.

## Cell measurements in water

A growing body of publications is emerging, utilizing a key differentiating aspect of O-PTIR over traditional IR techniques—the ability to measure cells in water, even live, metabolizing cells. As discussed above, under within the stable isotope labeling section, Shuster et al.49 demonstrated a first, by measuring the metabolic update of glucose in living, metabolizing cells. In this case, as detailed above, the example from Gvazava et al.,69 lipid droplets were measured in living salamander embryos with little to no water interferences despite the cells being present in water. This is because the heat capacity of lipids is even lower than that of muscles compared to water; thus, the effective thermal chemical selectivity toward lipids over water is greater. A key instrument mode and configuration consideration for hydrated cell measurements with O-PTIR is that unlike most samples, which have appreciable probe beam reflectivity, the reflectivity of the probe beam (commonly a 532 nm laser) is extremely low due to the existence of very little refractive index differences between the cell and water. In this case, the preferred mode of detection is not reflection, but transmission detection. It is important to reiterate here that unlike traditional IR techniques, discussions of reflection vs transmission detection are with respect to the probe beam, not the IR pump beam. With co-propagating transmission detection, both the IR pump beam and the probe beam are delivered from above, thus necessitating an IR transparent upper cell window. Thin CaF2 windows here are ideal, with thicknesses of 350 μm delivering excellent IR transmission with a sufficient visible imaging performance. The transmitted probe beam passes through the lower window (which only now must be transparent to the visible probe beam, thus being compatible with regular glass) before being detected by a dedicated transmission detector. In this configuration, to minimize water absorbances and attenuation, the biological cell is ideally placed on the under-side of the upper CaF2 window in a so-called “upside-down sandwich” configuration. As shown in the diagram in Fig. 27, Shuster $e t a l . ^ { 4 9 }$ used ∼5 μm double-sided tape as both a seal and spacer.

![](images/11465ea8a3fb28a2f0125e91d987443642e82b906ce7e7d77cf637e5e85b2b2d.jpg)

<details>
<summary>text_image</summary>

Objective
Infrared
Probe
CaF₂ cover slip
Cells in H₂O drop
Glass
Transmission Probe Beam Detection
</details>

FIG. 27. O-PTIR measurement in transmission mode on a glass slide.

Other examples of the measurement of cells in water can be found in the work of Spadea et $a l . ^ { 3 5 }$ where simultaneous (concomitant) IR (O-PTIR) and Raman spectra were measured in an upside-down sandwich cell configuration to explore and demonstrate subcellular structures such as protein secondary structures and lipid inclusions could be chemical (spectrally) characterized and chemical imaged in water. Shaik et $\cdot a l . ^ { 7 2 }$ published results using fixed cells in water (upside-down sandwich configuration) to demonstrate that various cancerous cell lines could be trained and differentiated while fully hydrated with up to 95% classification accuracy.

## Biomineralization studies

O-PTIR has been used successfully in the study of calcified tissue, including studying bone composition,73 growth,74,75 and regeneration.76,77 Kim et $\bar { a } l . ^ { 7 4 }$ used O-PTIR imaging to analyze microcavities within developing synovial joints of mouse embryos, mapping carbohydrate and protein contents at the micron scale within these microstructures. The high-resolution imaging of O-PTIR was crucial for examining the biochemical environment in developing joints, showing its potential to reveal early joint cavitation processes. Ahn et $a l . ^ { 7 5 }$ used O-PTIR to assess agedependent changes in the matrix/mineral ratio within mouse femur bone tissue, revealing variations in mineralization patterns as bone tissue matures. Chen et al. have used O-PTIR to study the bone healing processes in a rat model involving critical-size calvarial bone defects.76 O-PTIR enabled detailed visualization and quantification of the bone’s organic and inorganic content, revealing the spatial distribution and relative amounts of key components such as collagen and mineral phases, providing insights related to understanding the effectiveness of different biomaterials in promoting bone regeneration and integration with the host tissue.

a  
![](images/9ea57ce0f593a33aed2f2f2dba766dcdb206bb19f34c9ff4067dc99b655dcddf.jpg)

<details>
<summary>natural_image</summary>

Microscopic tissue section image showing cellular structures with a highlighted region (no text or symbols present)
</details>

b  
![](images/1422767d522ceb2e23954b0c24b93c57c80099dbdc8ea120d3cf5d56fd10ecc0.jpg)

<details>
<summary>heatmap</summary>

| Longitude | Latitude | Value |
| --------- | -------- | ----- |
| 0         | 35.9     | 1.000 |
| 26.79     | 35.9     | 1.000 |
| 53.37     | 35.9     | 1.000 |
| 81.26     | 35.9     | 1.000 |
| 107.24    | 35.9     | 1.000 |
| 133.93    | 35.9     | 1.000 |
| 160.71    | 35.9     | 1.000 |
| 180.78    | 35.9     | 1.000 |
| 200.6    | 35.9     | 1.000 |
| 226.5    | 35.9     | 1.000 |
| 252.4    | 35.9     | 1.000 |
| 288.3    | 35.9     | 1.000 |
| 324.2    | 35.9     | 1.000 |
| 360.1    | 35.9     | 1.000 |
| 396.0    | 35.9     | 1.000 |
| 431.9    | 35.9     | 1.000 |
| 468.8    | 35.9     | 1.000 |
| 505.7    | 35.9     | 1.000 |
| 542.6    | 35.9     | 1.000 |
| 579.5    | 35.9     | 1.000 |
| 616.4    | 35.9     | 1.000 |
| 653.3    | 35.9     | 1.000 |
| 690.2    | 35.9     | 1.000 |
| 727.1    | 35.9     | 1.000 |
| 764.0    | 35.9     | 1.000 |
| 800.9    | 35.9     | 1.000 |
| 837.8    | 35.9     | 1.000 |
| 874.7    | 35.9     | 1.000 |
| 911.6    | 35.9     | 1.000 |
| 948.5    | 35.9     | 1.000 |
| 985.4    | 35.9     | 1.000 |
| 1022.3   | 35.9     | 1.000 |
| 1069.2   | 35.9     | 1.000 |
| 1116.1   | 35.9     | 1.000 |
| 1153.0   | 35.9     | 1.000 |
| 1199.9   | 35.9     | 1.000 |
| 1246.8   | 35.9     | 1.000 |
| 1293.7   | 35.9     | 1.000 |
| 1339.6   | 35.9     | 1.000 |
| 1386.5   | 35.9     | 1.000 |
| 1433.4   | 35.9     | 1.000 |
| 1479.3   | 35.9     | 1.000 |
| 1526.2   | 35.9     | 1.000 |
| 1572.1   | 35.9     | 1.000 |
| 1628.0   | 35.9     | 1.000 |
| 1674.9   | 35.9     | 1.000 |
| 1721.8   | 35.9     | 1.000 |
| 1768.7   | 35.9     | 1.000 |
| 1815.6   | 35.9     | 1.000 |
| 1862.5   | 35.9     | 1.000 |
| 1909    | 35.9     | 1.000 |
| 1956    | 35.9     | 1.000 |
| 2012    | 35.9     | 1.000 |
| 2068    | 35.9     | 1.000 |
| 2124    | 35.9     | 1.000 |
| 2179    | 35.9     | 1.000 |
| 2234    | 35.9     | 1.000 |
| 2289    | 35.9     | 1.000 |
| 2344    | 35.9     | 1.000 |
| 2488    | 35.9     | 1.000 |
| 2644    | 35.9     | 1.000 |
| Note: The values in the heatmap are estimated based on the provided code and not explicitly provided in the original data source image.
</details>

c  
![](images/1d6765b531282be941f1e2328b0625aec0a2d33b5dfb80502bcb1142e4ae3449.jpg)

<details>
<summary>heatmap</summary>

| x    | y     | Value |
| ---- | ----- | ----- |
| 0    | 26.79 | 1.00  |
| 53.37| 81.36 | 2.00  |
| 107.14| 131.90| 3.00  |
| 131.90| 169.75| 4.00  |
| 167.8 | 25.9  | 5.00  |
</details>

d  
![](images/358eff8c065378116259021f70d91747b5a422b681917b29576e949e83736b25.jpg)

<details>
<summary>heatmap</summary>

| Longitude | Latitude | Value |
| --------- | -------- | ----- |
| 26.79     | 35.0     | 1.6   |
| 53.37     | 54.8     | 1.2   |
| 91.26     | 77.2     | 1.0   |
| 107.14    | 100.6    | 0.8   |
| 123.93    | 100.71   | 0.6   |
| 138.9     | 100.71   | 0.4   |
</details>

e  
![](images/97c73566e40f305ce37b869a15d6f294393dbbb9e8377b9c27abc0c9bbbed07d.jpg)

<details>
<summary>heatmap</summary>

| X (deg) | Y (deg) | Value |
| ------- | ------- | ----- |
| 26.79   | 35.0    | 120   |
| 53.57   | 55.8    | 120   |
| 00.36   | 77.2    | 120   |
| 107.14  | 107.8   | 120   |
| 133.93  | 133.93  | 120   |
| 160.71  | 160.71  | 120   |
| 181.8   | 181.8   | 120   |
</details>

f

![](images/29f522b3f33e02b21255636c1ad55dd80516a8198423041a2e7b02a634d287f9.jpg)

<details>
<summary>heatmap</summary>

| Longitude (μm) | Latitude (μm) | Value |
| -------------- | ------------- | ----- |
| 37.5           | 43.27         | 1     |
| 150            | 5             | 15    |
</details>

g  
![](images/ba662598c40d8e95beb4f58a44cdffde97617c3e26856c968bcd4321427bb647.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | minage Amp (mV) |
| ----------------- | --------------- |
| 1660              | 5               |
| 1544              | 3               |
| 1450              | 2               |
| 1399              | 1               |
| 1237              | 1               |
| 1082              | 1               |
</details>

h

![](images/04d1da7b9f87743e93bcffd8fa3a555955f584be502a4434b5628ff99fabc19e.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | mI-Rage Amp (mV) |
| ----------------- | ---------------- |
| 1656              | ~2.7             |
| 1529              | ~1.5             |
| 1450              | ~1.0             |
| 1044              | ~2.7             |
| 962               | ~0.5             |
| 874               | ~0.3             |
</details>

FIG. 28. O-PTIR measurements of a breast tissue section, including microcalcifications. (a) White light image (×10 objective) showing a microcalcification in dark (red box). Single IR frequencies collected at (b) protein-associated amide I band (1656 cm−1), at (c) phosphate band $( 1 0 4 4 ~ \mathsf { c m } ^ { - 1 } ) ,$ and (d) carbonate band $( 8 7 2 c m ^ { - 1 } )$ . Panels (e) and (f) show ratiometric images comparing intensity ratios for different bands: (e) phosphate to amide I ratio (1044: 1656 cm $\dot { - } 1 \dot { } \dot { } \big <$ and (f) carbonate to amide I ratio (872: $1 6 5 6 ( c m ^ { - 1 } ) .$ (g) Example of O-PTIR spectra collected from the tissue (orange dot, orange arrow) and (h) within the microcalcification (black dot, black arrow). Reprinted with permission from Bouzy et al., Anal. Methods 15(13), 1620 (2023). Copyright 2023 Author(s), licensed under a Creative Commons Attribution 3.0 DEED Unported License.

O-PTIR has also been used to study biomarkers associated with bone disease. Clarke et $a l . ^ { 7 8 }$ used O-PTIR to discriminate osteoarthritic extracellular vesicles (EVs) from those of healthy controls in equine plasma with a classification accuracy of 93.4%, demonstrating a potential use as a diagnostic tool. O-PTIR has also been very successful studying biogenic crystalline disorders, i.e., conditions causing abnormal crystal formations in biological tissue, including breast tissue calcification,79,80 arterial calcification,81 kidney stones,80 and cystinuria. 82 Figure 28 shows example O-PTIR measurements from Bouzy et al.79 on breast tissue, where ratiometric images reveal the spatial distribution of carbonates and phosphates, and localized spectra reveal the differences between normal and calcified tissue.

![](images/a3fa3e256f9f0002117889118c2af91b8e42183aadb02f0ade46ba8ef93440a4.jpg)

<details>
<summary>line chart</summary>

| Wavenumber cm⁻¹ | Mirage Amp (mV) |
| --------------- | --------------- |
| 1746            | ~4000           |
| 1702            | ~4500           |
| 1662            | ~6000           |
| 1612            | ~5500           |
| 1556            | ~8500           |
| 1468            | ~4000           |
| 1612            | ~3500           |
| 1432            | ~3000           |
| 1424            | ~2500           |
| 1360            | ~2000           |
| 1310            | ~1500           |
| 1310            | ~1000           |
| 1074            | ~2500           |
| 996             | ~2000           |
| 886             | ~1000           |
</details>

![](images/9e3394395b1f46b8b37689cbd447f450b7ddccaac1829a494d3aa87e4f105ecd.jpg)

<details>
<summary>line chart</summary>

| Wavenumber cm⁻¹ | Mirage Amp (mV) |
| --------------- | --------------- |
| 1748            | ~600            |
| 1702            | ~1000           |
| 1661            | ~900            |
| 1614            | ~300            |
| 1585            | ~200            |
| 1410            | ~800            |
| 1320            | ~600            |
| 1156            | ~800            |
| 1072            | ~1800           |
| 3.82            | ~1000           |
| 5             | ~200            |
</details>

FIG. 29. O-PTIR spectroscopic measurements of drug particles from a dry powder aerosol. Reprinted with permission from Khanal et al., Anal. Chem. 92(12), 8323 (2020). Copyright 2020 American Chemical Society.

## Biomaterial coatings

O-PTIR has also been used to provide insights into the enhancement of coatings for biomaterials, particularly targeting improved resistance to biofouling and corrosion.83,84 Zhao et al.83 used O-PTIR to assess the effectiveness of bionic engineered protein coatings in preventing biofouling in complex biological fluids with applications related to biomedical devices. O-PTIR measurements enabled the high-resolution visualization and quantification of biofoulant distributions on treated surfaces, demonstrating that the coatings significantly reduce biofouling by repelling biological contaminants. The same research group also used to characterize the dual-protection coatings on magnesium-based biomaterials inspired by tooth enamel biomineralization.84 The measurements facilitated the understanding of how these coatings enhance anticorrosion and antifouling properties by providing detailed insights into the molecular interactions at the coating interfaces related to anticorrosion and antifouling functionalities. O-PTIR has also been used to study biomaterials coatings on surgical sutures with the goal of reducing post-surgery infection. Puthia et al.85 used O-PTIR spectroscopy to analyze the interaction between TCP-25 peptides and polyglactin suture fibers. The O-PTIR measurements revealed that the peptide was successfully integrated into the suture fibers, as evidenced by spectral analysis, which detected specific infrared signatures characteristic of TCP-25 on the suture material. This integration is significant because it enables the sutures to function both as an antimicrobial and an anti-inflammatory agent, enhancing their utility in preventing surgical site infections and reducing inflammation directly at the wound site.

## Pharmaceutical applications

O-PTIR has also been used in pharmaceutical research, including mapping of active pharmaceuticals in a drug tablet,12 investigating polymer/drug phase separation in amorphous solid dispersions,86 and studying pharmaceutical dry powder aerosol formulations,87,88 e.g., for asthma inhalers. Yang et al.86 employed O-PTIR to examine the impact of surfactants on amorphous–amorphous phase separation in drug–polymer mixtures. O-PTIR provided detailed images and chemical composition analyses of phase-separated films, identifying how different surfactants alter the microstructure, which is relevant for understanding drug release and stability in pharmaceutical formulations. As shown in Fig. 29, Khanal et al.88 demonstrated that O-PTIR can be used to effectively characterize the chemical composition and distribution of drugs and excipients in size-segregated particles of pharmaceutical dry powder inhalation formulations, providing a new analytical capability for evaluating and enhancing drug delivery systems. O-PTIR allowed for the assessment of the spatial distribution of drugs and excipients, suggesting that this technique can provide detailed insights into the colocalization of these components within the aerosol particles. Razumtcev et al. employed autofluorescence-detected photothermal infrared to determine the spatial distribution and chemical composition of active pharmaceutical ingredients (APIs) within pharmaceutical mixtures, allowing for detailed characterization of drug formulations, including high-resolution, selective imaging of APIs, with the potential to enable measurements of content uniformity and quality in pharmaceutical products. Recently, studies have also been undertaken to evaluate the ability of O-PTIR to characterize and identify “subvisible” particles, i.e., particles in the range of 2–100 μm. Regulatory guidelines, such as those by the United States Pharmacopeia (USP) and the European Medicines Agency (EMA), require monitoring and controlling subvisible particles, especially in injectable drug products. While existing methods such as light obscuration/flow imaging microscopy can detect subvisible particles and characterize size and shape, the existing analytical methods do not provide information regarding the chemical composition of the particles. O-PTIR has demonstrated the ability to characterize and uniquely identify the composition of subvisible particles,89 providing critical data to help ascertain particle sources with the potential for reducing or eliminating the sources of contamination.

![](images/e09dcc03041a03f0b1a284f8d7184be052d6487490baad9edbbf56b747a4f7cc.jpg)  
FIG. 30. O-PTIR measurement of pharmaceutical inhaler drug formulation dispensed directly onto a glass slide. IR absorption images at IR bands unique to the different APIs reveal the spatial distribution and size of the API particles, with the ability to detect and characterize particles as small as ∼600 nm.

(a)  
![](images/21b9e5599f5a71afab8c8d99a90c6467d802e44683aa32eb2581141407eb7a4a.jpg)

<details>
<summary>scatterplot</summary>

| x (μm) | y (Value) |
| ------ | --------- |
| 0      | +         |
| 100    | +         |
| 200    | +         |
| 300    | +         |
</details>

(b)  
![](images/705eca4e19e5b176c2a401437f5929aa2e3dd8a1dabd6e3dd4b3eabed9ad6b0a.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Blue Line Intensity | Orange Line Intensity |
| ----------------- | ------------------- | --------------------- |
| 1800              | ~0                  | ~0                    |
| 1700              | ~1.0                | ~0.8                  |
| 1600              | ~0                  | ~0.2                  |
| 1500              | ~0.3                | ~0.4                  |
| 1400              | ~0.1                | ~0.2                  |
| 1300              | ~0.5                | ~0.6                  |
| 1200              | ~0.8                | ~1.0                  |
| 1100              | ~0.3                | ~0.5                  |
| 1000              | ~0                  | ~0.2                  |
</details>

(c)

<table><tr><td>Name</td><td>Id</td><td>Color</td><td>X (μm)</td><td>Y (μm)</td><td>Size (μm)</td><td>Area (μm2)</td><td>Highest HQI</td><td>Chemical ID</td></tr><tr><td>IR Spectrum 68</td><td>68</td><td></td><td>33.35</td><td>-1702.15</td><td>2.61</td><td>5.348</td><td>0.894</td><td>PMMA</td></tr><tr><td>IR Spectrum 69</td><td>69</td><td></td><td>-51.15</td><td>-1703</td><td>18.349</td><td>264.43</td><td>0.806</td><td>PS</td></tr><tr><td>IR Spectrum 70</td><td>70</td><td></td><td>50.45</td><td>-1695.35</td><td>11.678</td><td>107.106</td><td>0.846</td><td>PMMA</td></tr><tr><td>IR Spectrum 71</td><td>71</td><td></td><td>112.4</td><td>-1692.5</td><td>10.136</td><td>80.695</td><td>0.687</td><td>PMMA</td></tr><tr><td>IR Spectrum 72</td><td>72</td><td></td><td>-35.9</td><td>-1681.15</td><td>7.105</td><td>39.646</td><td>0.721</td><td>PMMA</td></tr><tr><td>IR Spectrum 73</td><td>73</td><td></td><td>6.2</td><td>-1679.4</td><td>8.532</td><td>57.175</td><td>0.615</td><td>protein</td></tr><tr><td>IR Spectrum 74</td><td>74</td><td></td><td>-2.9</td><td>-1677.45</td><td>6.184</td><td>30.034</td><td>0.981</td><td>PMMA</td></tr><tr><td>IR Spectrum 75</td><td>75</td><td></td><td>127.2</td><td>-1674.4</td><td>3.243</td><td>8.262</td><td>0.823</td><td>PMMA</td></tr><tr><td>IR Spectrum 76</td><td>76</td><td></td><td>-68.6</td><td>-1677.95</td><td>16.622</td><td>217.001</td><td>0.904</td><td>PMMA</td></tr></table>

(d)  
![](images/584283508fe83aab05c5f34918d995fd428f9cb48551a11c6de6ca68df7ccd2b.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | 3μm, PMMA | 20μm, PMMA | 18μm, PS | 30μm, PP | 13μm, PE | 14μm, Nylon | 4μm, PI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1800 |  |  |  |  |  |  |  |
| 1700 |  |  |  |  |  |  |  |
| 1600 |  |  |  |  |  |  |  |
| 1500 |  |  |  |  |  |  |  |
| 1400 |  |  |  |  |  |  |  |
| 1300 |  |  |  |  |  |  |  |
| 1200 |  |  |  |  |  |  |  |
| 1100 |  |  |  |  |  |  |  |
| 1000 |  |  |  |  |  |  |  |
</details>

FIG. 31. Automation detection of microplastic particles via O-PTIR. (a) Blob analysis showing particle locations, (b) example particle and reference spectra, (c) measured particle summary and chemical identification, and (d) example spectra and chemical identifications of microplastic particles in the 3–30 μm range filtered from water.

Figure 30 shows O-PTIR spectroscopy and chemical mapping of a binary API inhaled drug formulation sprayed directly onto a glass slide. The resulting O-PTIR spectra clearly demonstrate the high-quality, FTIR transmission/ATR-like spectra, despite being collected in reflection mode off a glass substrate. The spectra show no dispersive scatter artifacts, which in turn translates to highquality, single IR frequency chemical images on the same sample. By identifying key spectral markers for the compounds of interest, in this case, the two active pharmaceutical ingredients (APIs), rapid, high resolution chemical images can be collected in minutes, depicting an accurate chemical distribution of APIs or other target compounds.

## Environmental applications/microparticle analysis

O-PTIR has been very successful in the field of environmental analysis, especially as associated with detection and characterization of microparticulates, for example, airborne particles resulting from pollution,90 sea spray,91 and environmental microplastic particles. Similar analysis has been performed on aerosol drug particles, as described above in the pharmaceutical applications section.

## Microparticle sample preparation

For microplastics and airborne particle sampling, filtration and/or segmentation is often used to prepare samples for O-PTIR. For particles originally suspended in water or other aqueous solutions (e.g., environmental waterway samples and beverages), particles are usually filtered via a vacuum flask using serial filtration, e.g., a first filtration step with 20 μm pores to collect 20+ μm particles and then a second filtration step with 2 μm pores to collect 2–20 μm particles. Metal-coated filters are often preferable over uncoated polymeric filters because polymeric filters will have strong IR absorption bands that can provide an excessive background spectrum when trying to characterize small particles. Gold-coated polycarbonate filters are often a good choice as the thin gold coating blocks IR absorption from the underlying polycarbonate. Inorganic filters such as those etched from silicon materials (e.g., SiMPore filters) can also be an appropriate choice. For certain particle samples such as extraction of microplastic particles from soil or aquatic animal tissue require additional separation/digestion to remove unwanted non-polymeric materials (e.g., inorganics particles and organic tissue) prior to aqueous filtration.

Filtration of airborne particles (e.g., pollution, sea spray, and aerosol drug particles) can be filtered using aerosol particle samplers, which often include size fractionation capabilities based on particle aerodynamic properties. Microanalysis particle samplers have been used to sample airborne pollutants 9 0 and sea spray particles. 9 Cascade impactors, for example, the Next Generation Impactor92 have been used to capture and fractionate samples for O-PTIR.87,88

## Microplastics

Microplastics have been a rich application area for O-PTIR for several reasons. First, O-PTIR provides better spatial resolution and sensitivity than conventional IR micro-spectroscopy, includ ing FT-IR and QCL microscope approaches. A recent publication demonstrated that O-PTIR achieves a much lower limit of detection than QCL-IR and detected 18 times more microplastic particles than QCL-IR93 and enabled detection of much smaller particles. Second, O-PTIR avoids the dispersive size/shape/wavelength dependent scattering artifacts. O-PTIR also has advantages over Ramanbased approaches as it generally has better sensitivity and is immune to fluorescence interference, which is common in plastic materials. In addition, since O-PTIR can be combined with simultaneous Raman analysis, it can provide additional discriminatory or confirmatory analysis27,52 when the particle autofluorescence is not excessive. For these reasons O-PTIR has seen very strong publication growth in microplastics analysis, including detection and analysis of microplastic particles in beverages,94,95 food,96 baby bottle nipples,97 intravenous fluid delivery systems,89 bakeware,93 aquatic life,98 sediment,99 and human tissue.100 O-PTIR has also been used to analyze chemical changes in microplastic particles associated with photodegradation101 and tire wear.95,102

While early O-PTIR microplastics measurements were performed manually,103 automated analysis of microplastics has recently become available, as shown in Fig. 31. In these approaches, so-called “blob analysis” is first performed on optical microscope images to characterize particle sizes and locations within a field of view. Next, particles may be selected for automated analysis based on size/shape parameters to create a location list for O-PTIR spectral measurements. After automated acquisition of O-PTIR spectra at target locations, O-PTIR spectra are compared against a reference database to provide a chemical assignment for the measured particles.

## Cultural heritage

Chemical analysis of cultural heritage items via vibrational spectroscopy has a rich history.104,105 O-PTIR has been able to extend these analysis capabilities and has been used to analyze historical paintings106–109 and decorative objects.110 For example, researchers at the University of Antwerp, the Kröller–Müler Museum and SOLEIL Synchrotron used O-PTIR to perform complete stratigraphic analysis of a tiny fragment of a Van Gogh painting106 to detect and identify specific pigment particles used in the painting, enabling successful analysis where other techniques had failed. O-PTIR has also been used in the analysis of degradation products in historic painting107,108 and glass-metal decorative objects110 as well as used as part of a suite of tools to aid in authentication testing of historic paintings.109 Marchetti in

(a) car paint fragments  
![](images/1cb68fe95fed2413c5ba4ee06ccffd445100693df5bae4d8e2f90f883854c3f0.jpg)

<details>
<summary>scatterplot</summary>

| X | Y (μm) | Color |
|---|---|---|
| 55.38 | 71.31 | Red |
| 92.3 | 80.14 | Green |
| 110.76 | 106.97 | Blue |
</details>

![](images/0f4d3d8a0f8258a284310c1053a9be1f0740d61159455066f88d73a5d8454aa8.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Mirage Amp (mV) |
| ----------------- | --------------- |
| 1734              | 1.0             |
| 1608              | 0.4             |
| 1553              | 0.6             |
| 1512              | 0.9             |
| 1483              | 0.5             |
| 1477              | 0.4             |
| 1381              | 0.3             |
| 1254              | 0.2             |
| 1244              | 0.7             |
| 1187              | 0.5             |
| 110               | 0.8             |
| 1088              | 0.6             |
| 1036              | 0.5             |
| 1012              | 0.4             |
| 918               | 0.2             |
</details>

b) high explosives  
![](images/0dd9c9b3b2d31a936654a0f04cd0a6ea688eb4f989576023d3d4feec2da5c824.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of fluorescently labeled cellular structures with a 50 μm scale bar (no text or symbols beyond scale indicator)
</details>

![](images/42322d58c6b3d512c1f809c38fe80e8dc3ed680f3f128e1a0f0fe2c6ba7d4fd7.jpg)

<details>
<summary>line chart</summary>

| Wavenumber [cm⁻¹] | 1     | 2     | 3     | 4     | 5     | PETN  |
| ----------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| 1800              | -0.2  | -0.2  | -0.2  | -0.2  | -0.2  | -0.2  |
| 1600              | 1.5   | 1.5   | 1.5   | 1.5   | 1.5   | 1.5   |
| 1400              | 0.8   | 0.8   | 0.8   | 0.8   | 0.8   | 0.8   |
| 1200              | 1.7   | 1.7   | 1.7   | 1.7   | 1.7   | 1.7   |
| 1000              | 1.4   | 1.4   | 1.4   | 1.4   | 1.4   | 1.4   |
| 800               | 0.6   | 0.6   | 0.6   | 0.6   | 0.6   | 0.6   |
</details>

)polymer fiber additives  
![](images/8c144c1bda337f6947a720d10e39327d9d8d50c42523c5c3e85946a36a89365a.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Normalized O-PTIR intensity (AU) |
| ----------------- | -------------------------------- |
| 1900              | ~0                               |
| 1500              | ~0                               |
| 1000              | ~0                               |
| 700               | ~0                               |
</details>

d) fiber identification  
![](images/754ccea8f2a68b7044e12184291a9d75f9c9ae1389daca97b05e4234613721a1.jpg)

<details>
<summary>natural_image</summary>

Close-up of a textured surface with horizontal stripes and beige bands (no text or symbols visible)
</details>

![](images/ebfbaf9091ab129702afc38ff3570dbb1ca41cc4cbbe15130436480e49ee8afd.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Worst wool | Viscose | Spun silk | Acrylic | Polyester | Polymide type 66 | Bleached cotton | Acetate filament |
| ----------------- | ----------- | ------- | --------- | ------- | -------- | ---------------- | --------------- | ---------------- |
| 1900              | ~0.8        | ~0.3    | ~0.2      | ~0.1    | ~0.1     | ~0.1             | ~0.1            | ~0.1             |
| 1600              | ~0.7        | ~0.4    | ~0.3      | ~0.2    | ~0.2     | ~0.2             | ~0.2            | ~0.2             |
| 1400              | ~0.6        | ~0.5    | ~0.4      | ~0.3    | ~0.3     | ~0.3             | ~0.3            | ~0.3             |
| 1200              | ~0.5        | ~0.6    | ~0.5      | ~0.4    | ~0.4     | ~0.4             | ~0.4            | ~0.4             |
| 1000              | ~0.4        | ~0.7    | ~0.6      | ~0.5    | ~0.5     | ~0.5             | ~0.5            | ~0.5             |
| 800               | ~0.3        | ~0.8    | ~0.7      | ~0.6    | ~0.6     | ~0.6             | ~0.6            | ~0.6             |
</details>

FIG. 32. Forensic applications of O-PTIR analysis. (a) Spectroscopic identification of paint/coating layers from automotive paint fragment. (b) O-PTIR characterization of individual explosives particles. (c) Detecting/mapping of polymer fiber additives. (d) Discrimination of different polymer and natural fibers in a forensics fiber reference sample. (a), (c), and (d) courtesy of Photothermal Spectroscopy Corp.; (b) reprinted with permission from Banas et al., Anal. Chem. 92(14), 9649 (2020). Copyright 2020 American Chemical Society.

Ref. 109 noted, “The high spatial resolution (≈450 nm), lack of sample preparation, and comparability of the spectral results to traditional Fourier transform infrared spectroscopy make it a promising candidate for the analysis of cultural heritage,” and “The results clearly demonstrate how O-PTIR can be easily implemented in a noninvasive multi-analytical strategy for the study of heritage materials, making it a fundamental tool for cultural heritage analyses.”

## Forensics

O-PTIR also shows promise for applications in forensic sciences. O-PTIR has been used for proof-of-concept demonstrations regarding the identification of paint layers in automobile paint fragments,111 characterization of explosives particles,112 and successful identification and discrimination of different polymer and natural fibers, including the ability to identify and localized fiber additives (Fig. 32).

## Materials science

O-PTIR has been used extensively in materials science research, including 2D materials, polymers and composites, battery research, catalysis, and other areas. Example applications are summarized in the following sections.

![](images/7d09c8c8842e78a2080a57b8f608911e92f9ad84e144d54e63c57f42ccbdb001.jpg)

<details>
<summary>heatmap</summary>

| Region         | Value       |
| -------------- | ----------- |
| PHA crystalline | 1725 cm⁻¹   |
| PLA              | 1760 cm⁻¹   |
</details>

![](images/81c9fc1c53eaf0c918ce2bfbf19400c9fa0aa60bdbcfc8da313ac41ab64f0b32.jpg)

<details>
<summary>line chart</summary>

| Position | Profile Value |
| -------- | ------------- |
| 4        | 327           |
| 10       | 17            |
| 16       | 1.7           |
| 20       | 1.7           |
</details>

FIG. 33. O-PTIR analysis of a polymer multilayer film comprised of degradable bioplastics. Reprinted with permission from Marcott et al., J. Mol. Struct. 1210, 128045 (2020). Copyright 2020 Elsevier.

## 2D materials

He et al. have used O-PTIR microscopy to characterize the chemical distributions within self-assembled microdomains containing amine-functionalized graphene nanoplatelets in a commercial epoxy blend.113 Yoo et $a \check { l } . ^ { 1 1 \check { 4 } }$ used O-PTIR alongside UV–Vis absorption spectroscopy to analyze functional group inhomogeneity in graphene oxide (GO). By correlating these techniques, the research team was able to identify and map the distribution of different functional groups, particularly C–H and C–O rich regions and examine their electronic behaviors. This dual-spectroscopy approach allowed for a more detailed understanding of how these

![](images/7ba03ef6d5a0d240f2928a006a20b55a501a9cafaf187b85b20b848a179198ea.jpg)

<details>
<summary>heatmap</summary>

| X (μm) | Y (μm) | Value (mV) |
|---|---|---|
| 0 | 0 | 0 |
| 100 | 0 | 0 |
| 0 | 20 | 0.0008 |
| 100 | 20 | 0.0016 |
| 0 | 40 | 0.0024 |
| 100 | 40 | 0.0032 |
| 0 | 60 | 0.004 |
| 100 | 60 | 0.0058 |
| 0 | 80 | 0.0076 |
| 100 | 80 | 0.01 |
| 0 | 100 | 0.0124 |
| 100 | 100 | 0.0152 |
| 20 | 0 | 0.0168 |
| 30 | 20 | 0.02 |
| 40 | 40 | 0.024 |
| 50 | 60 | 0.03 |
| 60 | 80 | 0.036 |
| 70 | 100 | 0.042 |
| 80 | 80 | 0.048 |
| 90 | 60 | 0.054 |
| 100 | 40 | 0.06 |
| 110 | 20 | 0.066 |
| 120 | 40 | 0.072 |
| 130 | 60 | 0.078 |
| 140 | 80 | 0.084 |
| 150 | 100 | 0.1 |
| 160 | 80 | 0.116 |
| 170 | 60 | 0.132 |
| 180 | 40 | 0.148 |
| 190 | 20 | 0.164 |
| 200 | 40 | 0.18 |
| 210 | 60 | 0.2 |
| 220 | 80 | 0.226 |
| 230 | 100 | 0.252 |
| 240 | 80 | 0.278 |
| 250 | 60 | 0.3 |
| 260 | 40 | 0.336 |
| 270 | 20 | 0.362 |
| 280 | 40 | 0.388 |
| 290 | 60 | 0.414 |
| 300 | 80 | 0.44 |
| 310 | 100 | 0.466 |
| 320 | 80 | 0.5 |
| 330 | 60 | 0.536 |
| 340 | 40 | 0.562 |
| 350 | 20 | 0.588 |
| 360 | 40 | 0.614 |
| 370 | 60 | 0.64 |
| 380 | 80 | 0.666 |
| 390 | 100 | 0.7 |
| 400 | 80 | 0.736 |
| 410 | 60 | 0.762 |
| 420 | 40 | 0.788 |
| 430 | 20 | 0.814 |
| 440 | 40 | 0.84 |
| 450 | 60 | 0.866 |
| 460 | 80 | 1 |
| 470 | 100 | - |
The image displays a color-coded heatmap with a red box highlighting the region around the top-left corner of the heatmap area.
</details>

![](images/c35c40ad8abe0adc788eca6d841c0b945740056dbf528050c637e254caba56ad.jpg)

<details>
<summary>heatmap</summary>

| Region | Value |
|--------|-------|
| 1      | 24    |
| 2      | 23    |
| 3      | 24    |
| 4      | 25    |
</details>

![](images/1a31094aabb8c235846edbd8fabce844bcf31a716edc0b07a9c81b8bde15e2fe.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | IR Amplitude (arb. units) |
| --- | --- |
| 972 | 996 |
| 972 | 996 |
| 972 | 996 |
| 972 | 996 |
| 972 | 996 |
| 1212 | 1155 |
| 1212 | 1155 |
| 1212 | 1155 |
| 1212 | 1155 |
| 1212 | 1155 |
| 1376 | 1456 |
| 1376 | 1456 |
| 1376 | 1456 |
| 1376 | 1456 |
| 1376 | 1456 |
| 1456 | 1456 |
| 1456 | 1456 |
| 1456 | 1456 |
| 1456 | 1456 |
| 1456 | 1456 |
| 1730 | 1730 |
| center of PTFE | — |
</details>

![](images/e3ccdbc57660eaa7c02abb027f755a2d96b16f1da9c055418c1a21c8585d7a5f.jpg)

<details>
<summary>heatmap</summary>

| (μm) | 0    | 16   | 32   | 48   | 64   | 80   |
|------|------|------|------|------|------|------|
| 0    | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 16   | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 32   | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 48   | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 64   | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.12 |
| 80   | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.12 |
</details>

![](images/47ccaaa9e2876792d1d330b24cea32f988ea6077c1907c6a5d6a9f1b27c32254.jpg)

<details>
<summary>heatmap</summary>

| Label | Value |
|---|---|
| PTFE | 5678 |
| PP matrix | (labeled point) |
</details>

![](images/847276f53bfdf1819a1bf03ad426ca3cb7467079a3d52cc2d01b3c3b91cdbb2f.jpg)

<details>
<summary>line chart</summary>

| wavenumber (cm⁻¹) | IR Amplitude (arb. units) |
| --- | --- |
| 990 | 990 |
| 972 | 972 |
| 996 | 996 |
| 1210 | 1210 |
| 1153 | 1153 |
| 1376 | 1376 |
| 1456 | 1456 |
| 1376 | 1376 |
| 1456 | 1456 |
| 972 | 972 |
| 996 | 996 |
| 1210 | 1210 |
| 1153 | 1153 |
| 1376 | 1376 |
| 1456 | 1456 |
| 972 | 972 |
| 996 | 996 |
| 1210 | 1210 |
| 1153 | 1153 |
| 1376 | 13.76 |
| 1456 | 1456 |
| 972 | 972 |
| 996 | 996 |
| 1210 | 12.10 |
| 1153 | 11.53 |
| 1376 | 13.76 |
| 1456 | 14.56 |
| 972 | 972 |
| 996 | 996 |
| 1210 | 12.10 |
| 1153 | 11.53 |
| 1376 | 13.76 |
| 1456 | 14.56 |
| 972 | 8 |
| 996 | 8 |
| 1210 | 8 |
| 1153 | 8 |
| 1376 | 8 |
| 1456 | 8 |
| 972 | 8 |
| 996 | 8 |
| 1210 | 8 |
| 1153 | 8 |
| 1376 | 8 |
| 1456 | 8 |
| 972 | 8 |
| 996 | 8 |
| 1210 (peak) | - |
| 1153 (peak) | - |
| 1376 (peak) | - |
| 1456 (peak) | - |
| 972 | - |
| 996 | - |
| 1210 (peak) | - |
| 1153 (peak) | - |
| 1376 (peak) | - |
| 1456 (peak) | - |
| 972 | - |
| 996 | - |
| 1210 (peak) | - |
| 1153 (line) | - |
| 1376 (peak) | - |
| 1456 (peak) | - |
| 972 | - |
| 996 | - |
| 1210 (peak) | - |
| 1153 (peak) | - |
| 1376 (peak) | - |
| 1455 (peak) | - |
| 972 | - |
| 996 | - |
| 1210 (peak) | - |
| 1153 (peak) | - |
| 1376 (peak) | - |
| 1455 (peak) | - |
| 972 | - |
| 996 (line) | - |
| 1210 (peak) | - |
| 1153 (peak) | - |
| 1376 (peak) | - |
| 1455 (peak) | - |
| 972 | - |
| 996 | - |
| 1210 (peak) | - |
| 1154 (peak) | - |
| 1376 (peak) | - |
| 1455 (peak) | - |
| 972 | - |
| 996 | - |
| 1210 (peak) | - |
| 1154 (peak) | - |
| 1376 (peak) | - |
</details>

FIG. 34. O-PTIIR chemical imaging and spectroscopy of PP/PTFE polymer composite. Panels (a) and (b) and (d) and (e) show IR absorption images on different polymer composite formulations at 1210 cm−1 corresponding to an absorption band of PTFE. Panels (c) and (f) show spectra at locations indicated in panels (b) and (e). Reprinted with permission from Zhang et al., Mater. Des. 211, 110157 (2021). Copyright 2021 Author(s), licensed under a Creative Commons Attribution 4.0 License.

![](images/4081d47f3dab840de472a12b2e2d136af4d98da8546d69cc7b31e1cec2d14b7f.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | 40°C | 160°C |
| ----------------- | ---- | ----- |
| 1800              | -0.2 | -2.5  |
| 1700              | 0.8  | -1.5  |
| 1600              | -0.1 | -2.3  |
| 1500              | -0.3 | -2.4  |
| 1400              | -0.2 | -2.2  |
| 1300              | 0.3  | -2.1  |
| 1200              | -0.1 | -2.0  |
| 1100              | -0.2 | -2.3  |
| 1000              | -0.1 | -2.4  |
| 951               | -0.2 | -2.5  |
</details>

![](images/159cd7e6ed734526a24654688f00da524ef2bbe240a13f5e4766c6a05b06012e.jpg)

<details>
<summary>line chart</summary>

| Raman Shift (cm⁻¹) | Raman Intensity |
| ------------------ | --------------- |
| 2007.4             | ~0              |
| 1800               | ~-150           |
| 1600               | ~-50            |
| 1400               | ~-100           |
| 1200               | ~-50            |
| 1000               | ~-100           |
| 800                | ~-50            |
| 600                | ~-100           |
| 414.17             | ~-50            |
</details>

![](images/a983cdbcb8e116868f2d2e24ce6489eec200db9edf97952938e23073e2e3e9e0.jpg)

<details>
<summary>natural_image</summary>

Close-up of a mechanical device with a central circular component and surrounding components (no visible text or symbols)
</details>

FIG. 35. Submicron O-PTIR and simultaneous Raman spectra a biodegradable polymer under temperature ramp with an environmental stage (right). The spectra were acquired in reflection mode from 40 to $1 6 0 ^ { \circ } \complement$ at $1 0 ^ { \circ } \mathsf { C }$ increments. The sample is courtesy of Isao Noda and data are courtesy of Photothermal Spectroscopy Corp.; reprinted with permission.

![](images/37aa792eeb90cde475e174654a5c57bea0bbb1761f56dbac05767807ceded5a6.jpg)

<details>
<summary>line chart</summary>

| wavenumber (cm⁻¹) | uncycled | BE    | BE + FEC | BE + VC |
| ----------------- | -------- | ----- | -------- | ------- |
| 800               | ~0.5     | ~0.3  | ~0.4     | ~0.6    |
| 1000              | ~0.7     | ~0.6  | ~0.7     | ~0.8    |
| 1200              | ~0.6     | ~0.5  | ~0.6     | ~0.7    |
| 1400              | ~0.4     | ~0.8  | ~0.5     | ~0.6    |
| 1600              | ~0.3     | ~0.4  | ~0.3     | ~0.4    |
| 1800              | ~0.2     | ~0.2  | ~0.2     | ~0.2    |
| 2000              | ~0.1     | ~0.1  | ~0.1     | ~0.1    |
</details>

FIG. 36. Comparison of ATR spectra (top) and O-PTIR spectra (bottom) on silicon nanowire electrodes, before and after electrochemical cycling with a benchmark electrolyte (BE) and the same electrolyte with two different additives vinylene carbonate (VC) and fluoroethylene carbonate (FEC). O-PTIR spectra revealed the production of carbonates and LiPF6 decomposition residues. The spectra are normalized at Si–C stretching vibration band (990 cm−1). Reprinted with permission from Sarra et al., Batteries 9(3), 148 (2023). Copyright 2023 Author(s), licensed under a Creative Commons Attribution 4.0 License.

functional groups affect the electronic and optical properties of GO, informative for optimizing its use in various applications, such as energy storage and biosensors.

## Polymers and composites

O-PTIR can be a very productive tool for studying polymeric systems because most polymers have both strong IR absorption bands and distinct IR spectral fingerprints that provide robust characterization and identification. O-PTIR has been used to study multi-layer polymer laminates,115 including biopolymers116 and 26,113,117,118 polymer composites.

Figure 33 shows an example of analysis by Marcott et al.116 over the interface between two degradable polymers based on imaging at IR bands unique to the constituents. Figure 34 shows the use of O-PTIR for mapping polymer constituents in a polytetrafluoroethylene/polypropylene (PTFE/PP) reinforced polymer composite.

## Environmentally controlled (heating/cooling/gases) measurements

The measurement of samples under environmental perturba tion(s), such as temperature (heating/cooling) or exposure to gases is a common and important experimental approach often applied to the study of polymers and catalysts. As is commonly employed in FTIR and Raman, environmental cells, capable of heating or cooling the sample and capable of introduction gases are also applicable directly with O-PTIR, with the added benefit of multi-modality with Raman and fluorescence imaging. The submicron simultaneous measurement of IR and Raman spectra while a polymer is heated to melting is shown in Fig. 35. This demonstrates the utility of employing complementary spectroscopic techniques such as IR and Raman to probe the structural changes a sample undergoes during such perturbations.

## Battery research

O-PTIR has also been used in battery research, for example, studying spectroscopic changes in silicon nanowire electrodes under electrochemical cycling.119 Battery research represents a challenge for traditional infrared spectroscopy because many battery electrode materials are opaque to infrared radiation and thus cannot be studied in transmission. As such, techniques such as reflection or attenuated total reflection (ATR) must be used, which can lead to dispersive/scattering artifacts and/or lower SNR. Figure 36 shows a comparison of spectra acquired by conventional ATR infrared and O-PTIR on nanowire electrodes before and after cycling in the presence of different electrolyte additives. This first application of O-PTIR on lithium battery research demonstrated both better SNR and the ability to probe deeper into electrode materials compared to ATR measurements on the same sample. The improved SNR and improved depth sensitivity together enabled more complete analysis of reaction products than possible with conventional infrared approaches, demonstrating substantial benefits even when achieving higher spatial resolution is not the key focus.

a  
![](images/c6f66b687d910916393674f9e663062e530333e7ca29d1c810a4355994a970d8.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of brightfield material with green and blue cellular structures (no text or symbols)
</details>

b  
![](images/9529d30d3e4e4d561439a908b1f96b1627f7389f56485c9c645262f00a9816cc.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological sample showing textured surface with scale bar (no text or symbols)
</details>

c  
![](images/4509597c631296306d6238c441c7107a8b471e1d2a7ad8e32e45bf30fb8b170c.jpg)

<details>
<summary>text_image</summary>

1595 cm⁻¹
0.0 10.5
</details>

d  
![](images/452b9221ca3394f584f126a831a9ad20bc70ecefaf42d6b9454fd7f46e2bbb66.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological sample with red fluorescent staining, labeled 'Overlaid' in top-left corner (no other text or symbols)
</details>

FIG. 37. O-PTIR super-resolution IR imaging characterization of a copper–cobalt (CuCo) alloy electrocatalyst. (a) Brightfield image. (b) Reflectance image of the area indicated by the white box in panel (a) with 532 nm laser illumination. (c) Super-resolution IR imaging of the same area by O-PTIR imaging at 1595 cm−1 associated with the CuCo catalyst band. (d) Overlay of reflectance and IR image. Scale bars: 50 μm. Reprinted with permission from Wu et al., ACS Sustain. Chem. Eng. 10(44), 14539 (2022). Copyright 2022 American Chemical Society.

## Catalysis

O-PTIR measurements have also been used to study catalysts for waste water treatment for nitrate to ammonia conversion120 and dye degradation associated with printing and dyeing industries.121 Wu et al. used O-PTIR as part of a suite of analytical techniques, including x-ray diffraction, atomic force microscopy, electron microscopy, and conventional infrared spectroscopy, to evaluate copper–cobalt alloy electrocatalysts. O-PTIR was particularly used for morphological and compositional analysis of the catalyst material. Figure 37 shows O-PTIR chemical imaging of a copper–cobalt alloy electrocatalyst for ammonia conversion revealing the spatial localization of the active catalyst regions.

## Photonics/plasmonics

## Perovksite/solar cells

O-PTIR has also been used to study perovskite materials, for example, to investigate the structures at the edges of a type of solar cell material known as 2D Ruddlesden–Popper perovskites122 (Fig. 38). This research discovered that at perovskite crystal edges, the material spontaneously transforms from a two-dimensional to a three-dimensional form. When combined with O-PTIR, it helped identify the loss of organic components (specifically butylammonium) and the presence of methylammonium in the 3D structures at the edges of perovskite crystals. This transformation is significant because it enhances the material’s ability to emit light and improves its electrical properties, which are crucial for increasing the efficiency of solar cells and other electronic devices. While the measurements shown in the following were performed on separate instruments, the current generation O-PTIR instruments optionally include flu orescence microscopy capabilities, which, with appropriate filter sets, can also perform photoluminescence imaging, thus enabling photoluminescence-guided infrared spectroscopy with sub-micron spatial resolution.

## Surface enhanced O-PTIR

Anderson recently demonstrated simultaneous and complementary surface-enhanced infrared absorption (SEIRA) and surface-enhanced Raman spectroscopy (SERS) using a Ramanenabled O-PTIR instrument in combination with plasmonically active substrates to achieve single molecule detection sensitivity. 123 To demonstrate single molecule sensitivity, Anderson coated silver nanospheres with two target analytes [C60 and 1,2-bis(4-pyridyl) ethylene, BPE] and then measured them at sub-monolayer dilution to provide a high likelihood that observed hotspots contained only a single analyte molecule. As further evidence of single molecule sensitivity, Anderson also analyzed binary mixtures of C60 and BPE at low dilution, obtaining spectra that showed the spectral signatures of either C60 or BPE without contributions for the other analyte. Figures 39(a) and 39(b) show an example of concurrent single molecule SEIRA and SERS measurements on BPE. While single molecule SERS spectroscopy is well-established, to our knowledge, this is the first demonstration of single molecule detection by SEIRA and the first demonstration of single molecule spectroscopy by both Raman and infrared techniques. Since IR and Raman are highly complementary approaches, as described earlier, this demonstration is an extremely promising milestone. Anderson also showed how gold-coated atomic force microscopy probes could be used as both an analyte nano-sampler and as a plasmonic enhancer [Figs. 39(c)–39(f)] for O-PTIR based SEIRA and SERS measurements, albeit with reduced plasmonic enhancement compared to the silver nanospheres.

## Geochemical and paleontological applications

O-PTIR has also been used to enable the molecular characterization of sedimentary organic matter and organic fossils.

![](images/a62009a0b1267d482b6f8d4a206d985658b70782e5e2562ae88bd8e3820179ee.jpg)

<details>
<summary>text_image</summary>

(a)
3
6
4
5
1
2
10 µm
</details>

![](images/4a57fb38b6f9230d748459cc94f897cf3fd850a11ae77df990abbbfce13b9684.jpg)

<details>
<summary>line chart</summary>

| IR Wavenumber (cm⁻¹) | Intensity (Red) | Intensity (Green) | Intensity (Yellow) | Intensity (Orange) | Intensity (Blue) |
|----------------------|-----------------|-------------------|--------------------|--------------------|------------------|
| 1400                 | ~0.5            | ~0.3              | ~0.2               | ~0.1               | ~0.1             |
| 1500                 | ~2.0            | ~3.0              | ~2.5               | ~2.0               | ~2.5             |
| 1600                 | ~5.0            | ~4.0              | ~3.5               | ~3.0               | ~4.5             |
| 1700                 | ~3.0            | ~3.5              | ~3.0               | ~2.5               | ~3.5             |
</details>

FIG. 38. O-PTIR analysis of perovskite crystals for solar cell applications. O-PTIR spectra (b) were measured at locations identified in photoluminescence imaging (a). Reprinted with permission from Qin et al., Chem. Mater. 32(12), 5009 (2020). Copyright 2020 American Chemical Society.

![](images/ceedffdf3c0ae547ef538925c042295342f8c1127c67f428fe061af679bcdf7b.jpg)

<details>
<summary>line chart</summary>

| Wavenumbers (cm-1) | Raman Intensity (a) | OPT Infrared Signal (b) |
| ------------------ | ------------------- | ----------------------- |
| 1800               | ~0.1                | ~0.05                   |
| 1700               | ~0.3                | ~0.1                    |
| 1600               | ~1.0                | ~1.0                    |
| 1500               | ~0.8                | ~0.3                    |
| 1400               | ~0.9                | ~0.6                    |
| 1300               | ~0.7                | ~0.4                    |
| 1200               | ~1.2                | ~0.3                    |
| 1100               | ~0.5                | ~0.4                    |
| 1000               | ~0.3                | ~0.5                    |
</details>

(c)  
![](images/f2a20fc801508cf1b2d2dd1edacec64ea3e982c350566ad41ab44c655409a490.jpg)

(d)  
![](images/290961b74b921af6c5dea0eccb83a80e2f882e5edf3de3b900c062a80c56b989.jpg)

![](images/49a3bd62a298d2bc7dba15cef79e2d148b551f9a0ead21804956981a03a3f49c.jpg)

<details>
<summary>line chart</summary>

| Wavenumbers (cm-1) | Raman Intensity (Raman SERS) | OPT Infrared Signal (Infrared SEIRA) |
| ------------------ | ---------------------------- | ------------------------------------ |
| 1800               | ~0                           | ~0                                   |
| 1700               | ~0                           | ~0                                   |
| 1600               | ~1.5                         | ~1.5                                 |
| 1500               | ~0.5                         | ~0.5                                 |
| 1400               | ~0.8                         | ~0.8                                 |
| 1300               | ~0.3                         | ~0.3                                 |
| 1200               | ~0.9                         | ~0.9                                 |
| 1100               | ~0.2                         | ~0.2                                 |
| 1000               | ~0.6                         | ~0.6                                 |
| 900                | ~0.1                         | ~0.1                                 |
| 800                | ~0                           | ~0                                   |
| 700                | ~0                           | ~0                                   |
| 600                | ~0                           | ~0                                   |
| 500                | ~0.4                         | ~0                                   |
| 400                | ~0                           | ~0                                   |
</details>

FIG. 39. O-PTIR with plasmonic enhancement demonstrating single molecule sensitivity. Single molecular SERS (a) and SEIRA (b) spectra simultaneously acquired on 1,2-bis(4-pyridyl) ethylene (BPE) cast onto silver nanospheres. (c) AFM-based analyte nano-sampling and (d) plasmonic enhancement. SERS (e) and SEIRA (f) spectra on AFM nano-sampled/enhanced BP+C60 analytes. Reprinted with permission from Anderson, Rev. Sci. Instrum. 94(2), 025103 (2023). Copyright (2023) Author(s), licensed under a Creative Commons Attribution 4.0 License.

![](images/245cbc0f8e0979137d7781910bbbd67f5f250b337ac5de8d0c13df022ff76990.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Series 1 | Series 2 | Series 3 | Series 4 |
| ----------------- | -------- | -------- | -------- | -------- |
| 1000              | ~0.8     | ~0.6     | ~0.4     | ~0.2     |
| 1400              | ~0.7     | ~0.5     | ~0.3     | ~0.1     |
| 1800              | ~0.9     | ~0.7     | ~0.5     | ~0.3     |
| 2600              | ~0.6     | ~0.4     | ~0.2     | ~0.1     |
| 3000              | ~0.8     | ~0.6     | ~0.4     | ~0.2     |
</details>

![](images/32db455f2a70563a47c168b47930fc6ace6da5a1ce6533803d685dacbd4b69b6.jpg)

<details>
<summary>text_image</summary>

B) 1100 cm⁻² (SiO str.)
0
50
100
150
200
250
300 µm
0
mV
200µm
</details>

![](images/70eed15abe573b6b82bc2a10885fa12a7ffb9a80eb2dcf7c0a11ff38cbe6a100.jpg)

<details>
<summary>text_image</summary>

(c) 1459 cm⁻¹ (CH₂ scissor)
0	50	100	150	200	250	300 µm
0	50	100	150	200	250	300 µm
mV	1000
</details>

![](images/0d023a7dee014a7dbac9da033ea432be56d6a7ba3692dab5f21b2456fc2e2057.jpg)

<details>
<summary>text_image</summary>

D) 1605 cm⁻¹ (C=C str.)
0	50	100	150	200	250	300 µm
0	50	100	150	200	250	300 µm
mV	1000
</details>

![](images/ddfdad6677ca19d624095fe80fb387fe45a1f837f500d795644db56dc89ccd43.jpg)

<details>
<summary>text_image</summary>

E) 1713 cm⁻¹ (C=O str.)
0	50	100	150	200	250	300 µm
0	50	100	150	200	250	300 µm
mV	2000
</details>

![](images/6295c733bb1b0362645c97cf09d4006c62fff317cbf28d627f9c37de93f19fa1.jpg)

<details>
<summary>text_image</summary>

F) 2923 cm⁻¹ (CH₃ asy. str.)
0
50
100
150
200
250
300 µm
0
50
100
150
200
250
300 µm
0
50
100
150
200
250
300 µm
0
50
100
150
200
250
300 µm
0
50
100
150
200
200
250
300 µm
0
50
100
150
200
250
300 µm
</details>

![](images/eea0c2da0ac0026da6c9e8e843f0ff2551bbbf218aac41dcd16c603483a27f71.jpg)

<details>
<summary>text_image</summary>

G) 2961 cm⁻¹ (CH₃ asy. str.)
0	50	100	150	200	250	300 µm
0	50	100	150	200	250	300 µm
mV	1000
</details>

![](images/6f5f67d03d74e6421f92e1de7036b0c1c780ff79b3d71b8fbdaa6b8517f3617e.jpg)

<details>
<summary>text_image</summary>

H) A-factor (H/C proxy)
0	50	100	150	200	250	300 µm
	45	10.65
</details>

![](images/de1b8759d02869f8c48fe87a99e412565a38b033295d215d04bc4443d2119991.jpg)

<details>
<summary>text_image</summary>

I) C-factor (O/C proxy)
0
50
100
150
200
250
300 µm
</details>

![](images/e0b725a8ccde29d0093d6a4c085210c37e758694a5f8235a890358a72adf3dd4.jpg)

<details>
<summary>text_image</summary>

J) Branching ratio (CH₂/CH₃)
0 50 100 150 200 250 300 µm
0.5 0.9
</details>

FIG. 40. O-PTIR chemical characterization and visualization of organics in sediments associated with algal microfossils. (a) O-PTIR spectra on Tasmanites microfossil (spectra 1-2) and adjacent sediment regions (spectra 3-4). (b)–(j) O-PTIR absorption images and image ratios for relevant organic and inorganic absorption bands. Reprinted with permission from Jubb et al., Org. Geochem. 177, 104569 (2023). Copyright 2023 Author(s), licensed under a Creative Commons Attribution 4.0 License.  
![](images/139eb52389fcdfcf5bc490a9b8a8756cab826979103f3ce82715f29af6c3f637.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Value |
| ----------------- | ----- |
| 5.14              | 5.14  |
</details>

FIG. 41. O-PTIR analysis of organic contaminant for data storage applications. (a) Optical image showing a ∼5 μm defect on the surface of a disk drive recording head. (b) O-PTIR spectrum (bottom) and reference spectrum from KnowItAll spectral database, revealing an identification of polyetherimide. Reprinted with permission from Kansiz et al., Microsc. Today 28(3), 26 (2020). Copyright 2020 Microscopy Society of America.

![](images/2c6203b634df6f23abc24ac9bc0288ead2f341e66a02484c2ce4f9acfaafcf91.jpg)  
FIG. 42. O-PTIR spectra and images associated with characterizing a defective weld in an electronic component. Optical images (center) show a good weld and a defective weld in an electronic component. O-PTIR spectra were collected at the color-coded locations in the image in and around the weld defect (left). The IR absorbance image (right) was collected at $1 7 2 4 ~ { \mathsf { c m } } ^ { - 1 }$ , where a properly formed weld has a strong absorption band. The spectra and images provide insights into the bond failure mechanism. Reprinted with permission from Kansiz et al., Microsc. Today 28(3), 26 (2020). Copyright 2020 Microscopy Society of America.

![](images/8a799765db160a0328badc7acda76e7b83d2b5ee81948e6b6dd2851d77617f0f.jpg)  
epoxy  
carboxylate BSM  
IR image ratio 1598 cm1/1460 cm1  
IR image ratio - 1510 cm1/1460 cm

FIG. 43. O-PTIR analysis of a cross-sectioned semiconductor device. (a) and (b) Optical image of the analyzed region of the cross sectioned device sample with locations noted for spectra in panel (g). (c), (e), and (f) O-PTIR ratiometric images at the wavenumbers indicated. (d) RGB overlay of ratio images in panels (c), (e), and (f) reprinted with permission from Zulkifli et al., in 2022 IEEE International Symposium on the Physical and Failure Analysis of Integrated Circuits (IPFA) (IEEE, 2022), p. 1. Copyright 2022 IEEE.

Jubb et al.124 have used O-PTIR to map the distribution of functional groups in sedimentary organic matter (SOM) within the Upper Devonian Ohio Shale (Fig. 40), revealing that O-PTIR can discriminate between different types of organic materials and mineral matrices at sub-micron scales providing relevant insights into petroleum generation processes and sedimentary environments. In particular, the research mapped infrared functional groups associated algal microfossils and discriminated organic matter from adjacent solid bitumen with 500 nm spatial resolution.

## Failure analysis/defect identification

O-PTIR is being rapidly adopted in industrial research, includ ing by Fortune 500 companies, often for process development, optimization, failure analysis, and defect identification.125–129 Applications include semiconductor,129 data storage,24 display, electronic, and pharmaceutical industries. A very common application is the identification of organic contaminants that are below the detection limit of conventional infrared spectroscopy. While electron microscopes configured with energy dispersive x-ray capabilities can routinely provide elemental analysis, there has been a gap in the ability to characterize and identify organic contaminants below the detection limit of conventional IR and Raman spectroscopy. O-PTIR is demonstrating significant success in this arena with its ability to characterize even sub-micron contaminants. Figure 41 shows an example of O-PTIR identification of a defect found on a disk drive recording head. Another common application is failure analysis associated with the degradation and/or migration of species within a device, and/or manufacturing related defects. Figure 42 shows an example of O-PTIR spectroscopy and chemical imaging associated with a defective weld in an electronic device. Figure 43 shows O-PTIR imaging and spectroscopic analysis of a packaged semiconductor device that has undergone underfill creep.

## ADVANCED MODALITIES AND OUTLOOK

O-PTIR researchers are continuing to push the state of the art and have demonstrated a variety of advanced modalities, including interferometric and phase-based detection and wide-field detection approaches50,130–138 as well as depth-resolved O-PTIR tomography.58,139,140 Looking ahead, we anticipate a panel of exciting directions of this technology. First, advanced infrared lasers and modalities are to be developed to further improve the sensitivity, speed, and enlarge the field of view of the technique. By sync-scan of IR pump and visible probe beam, video rate imaging speed has been achieved recently.141 With high-energy IR pulses, we expect OPTIR to reach millimeter-scale field of view for highthroughput tissue analysis. We expect infrared absorbing tags and substrates to be extensively developed for O-PTIR imaging of specific molecules and/or cellular processes without the need of click chemistry. We also expect the development of highly sensitive temperature reporters to boost the sensitivity of O-PTIR imaging toward a single molecule level. We expect the integration of OPTIR with microfluidics for high-throughput single cell or single particle analysis. Finally, we predict clinical translation as the next frontier through miniaturization of the O-PTIR microscope toward molecular-based diagnosis in the clinic settings.

## ACKNOWLEDGMENTS

This work was partly supported by NIH Grant No. R35GM136223 to J.-X.C.

## AUTHOR DECLARATIONS

## Conflict of Interest

C.B.P. and M.K. are employees and/or shareholders of Pho tothermal Spectroscopy Corp. (PSC), a company that manufactures and sells O-PTIR instruments. J.-X.C. is a consultant for PSC and has other financial benefits related to sale of O-PTIR instruments via equity and license agreements.

## Author Contributions

C.B.P., M.K., and J.-X.C. each contributed to the manuscript writing and editing.

Craig. B. Prater: Writing – original draft (lead); Writing – review & editing (equal). Mustafa Kansiz: Writing – original draft (supporting); Writing – review & editing (equal). Ji-Xin Cheng: Writing – original draft (supporting); Writing – review & editing (equal).

## DATA AVAILABILITY

As this is a tutorial/review article, requests for source data should be directed to authors of cited publications.

## REFERENCES

1R. Kizil and J. Irudayaraj, in Encyclopedia of Biophysics, edited by G. C. K. Roberts (Springer, Berlin, Heidelberg, 2013), p. 840.  
2D. Fournier, F. Lepoutre, and A. Boccara, “Tomographic approach for photothermal imaging using the mirage effect,” J. Phys. Colloq. 44(C6), C6-479 (1983).  
3M. S. Anderson, “Infrared spectroscopy with an atomic force microscope,” Appl. Spectrosc. 54(3), 349 (2000).  
4A. Dazzi, R. Prazeres, F. Glotin, and J. M. Ortega, “Local infrared microspectroscopy with subwavelength spatial resolution with an atomic force microscope tip used as a photothermal sensor,” Opt. Lett. 30(18), 2388 (2005).  
5A. Hammiche, H. M. Pollock, M. Reading, M. Claybourn, P. H. Turner, and K. Jewkes, “Photothermal FT-IR spectroscopy: A step towards FT-IR microscopy at a resolution better than the diffraction limit,” Appl. Spectrosc. 53(7), 810 (1999).  
6A. Dazzi and C. B. Prater, “AFM-IR: Technology and applications in nanoscale infrared spectroscopy and chemical imaging,” Chem. Rev. 117(7), 5146 (2017).  
7R. Furstenberg, C. Kendziora, M. Papantonakis, V. Nguyen, and R. A. McGill, “Chemical imaging using infrared photothermal microspectroscopy,” Proc. SPIE 8374, 837411 (2012).  
8A. Mërtiri, A. Totachawattana, H. Liu, M. K. Hong, T. Gardner, M. Y. Sander, and S. Erramilli, “Label free mid-IR photothermal imaging of bird brain with quantum cascade laser,” in CLEO: Applications and Technology (Optical Society of America, 2014), p. AF1B.4.  
9M. Y. Sander, “Mid-infrared photothermal imaging,” in Frontiers in Optics 2015 (Optica Publishing Group, 2015), p. LM1I.2.10.1364/LS.2015.LM1I.2.  
10J.-X. Cheng and X. S. Xie, “Vibrational spectroscopic imaging of living systems: An emerging platform for biology and medicine,” Science 350(6264), aaa8870 (2015).  
11D. Zhang, C. Li, C. Zhang, M. N. Slipchenko, G. Eakins, and J.-X. Cheng, “Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution,” Sci. Adv. 2(9), e1600521 (2016).  
12C. Li, D. Zhang, M. N. Slipchenko, and J.-X. Cheng, “Mid-infrared photothermal imaging of active pharmaceutical ingredients at submicrometer spatial resolution,” Anal. Chem. 89(9), 4863 (2017).  
13Y. Bai, D. Zhang, C. Li, C. Liu, and J.-X. Cheng, “Bond-selective imaging of cells by mid-infrared photothermal microscopy in high wavenumber region,” J. Phys. Chem. B 121(44), 10249 (2017).  
14Z. Li, M. Kuno, and G. Hartland, “Super-resolution imaging with mid-IR photothermal microscopy on the single particle level,” Proc. SPIE 9549, 954912 (2015).  
15Z. Li, M. Kuno, and G. Hartland, “Super-resolution mid-infrared imaging using photothermal microscopy,” in Conference on Lasers and Electro-Optics (Optical Society of America, 2016), p. ATu3J.7.  
16Z. Li, K. Aleshire, M. Kuno, and G. V. Hartland, “Super-resolution far-field infrared imaging by photothermal heterodyne imaging,” J. Phys. Chem. B 121(37), 8838 (2017).  
17Y. Bai, J. Yin, and J.-X. Cheng, “Bond-selective imaging by optically sensing the mid-infrared photothermal effect,” Sci. Adv. 7(20), eabg1559 (2021).  
18Q. Xia, J. Yin, Z. Guo, and J.-X. Cheng, “Mid-infrared photothermal microscopy: Principle, instrumentation, and applications,” J. Phys. Chem. B 126, 8597 (2022).  
19P. D. Samolis and M. Y. Sander, “Phase-sensitive lock-in detection for high-contrast mid-infrared photothermal imaging with sub-diffraction limited resolution,” Opt. Express 27(3), 2643 (2019).  
20P. Fu, W. Cao, T. Chen, X. Huang, T. Le, S. Zhu, D.-W. Wang, H. J. Lee, and D. Zhang, “Super-resolution imaging of non-fluorescent molecules by photothermal relaxation localization microscopy,” Nat. Photonics 17(4), 330 (2023).  
21P. Craig, K. Kjoller, and R. Shetty, U.S. patent application 16/155,089 (10 September 2019).  
22J. Yin, L. Lan, Y. Zhang, H. Ni, Y. Tan, M. Zhang, Y. Bai, and J.-X. Cheng, “Nanosecond-resolution photothermal dynamic imaging via MHz digitization and match filtering,” Nat. Commun. 12(1), 7097 (2021).  
23P. D. Samolis and M. Y. Sander, “Increasing contrast in water-embedded particles via time-gated mid-infrared photothermal microscopy,” Opt. Lett. 49(6), 1457 (2024).  
24M. Kansiz, C. Prater, E. Dillon, M. Lo, J. Anderson, C. Marcott, A. Demissie, Y. Chen, and G. Kunkel, “Optical photothermal infrared microspectroscopy with simultaneous Raman: A new non-contact failure analysis technique for identification of <10 μm organic contamination in the hard drive and other electronics industries,” Microsc. Today 28(3), 26 (2020).  
25Y. Bai, C. M. Camargo, S. M. K. Glasauer, R. Gifford, X. Tian, A. P. Longhini, and K. S. Kosik, “Single-cell mapping of lipid metabolites using an infrared probe in human-derived model systems,” Nat. Commun. 15(1), 350 (2024).  
26A. J. Wang, E. P. Dillon, S. Maharjan, K.-S. Liao, B. P. McElhenny, T. Tong, S. Chen, J. Bao, and S. A. Curran, “Resolving nanocomposite interfaces via simultaneous submicrometer optical-photothermal infrared-Raman microspectroscopy,” Adv. Mater. Interfaces 8(5), 2001720 (2021).  
27J. S. Böke, J. Popp, and C. Krafft, “Optical photothermal infrared spectroscopy with simultaneously acquired Raman spectroscopy for two-dimensional microplastic identification,” Sci. Rep. 12(1), 18785 (2022).  
28D. P. Almond and P. Patel, Photothermal Science and Techniques (Springer Science & Business Media, 1996).  
29J. Sell, Photothermal Investigations of Solids and Fluids (Elsevier, 2012).  
30R. D. Snook and R. D. Lowe, “Thermal lens spectrometry. A review,” Analyst 120(8), 2051 (1995).  
31M. Franko and C. D. Tran, “Analytical thermal lens instrumentation,” Rev. Sci. Instrum. 67(1), 1 (1996).  
32S. J. Sheldon, L. V. Knight, and J. M. Thorne, “Laser-induced thermal lens effect: A new theoretical model,” Appl. Opt. 21(9), 1663 (1982).  
33A. Rahman, K. Rahim, I. Ashraf, and H. Cabrera, “A modified modemismatched thermal lens spectrometry Z-scan model: An exact general approach,” Optik 265, 169399 (2022).  
34X. Li, D. Zhang, Y. Bai, W. Wang, J. Liang, and J.-X. Cheng, “Fingerprinting a living cell by Raman integrated mid-infrared photothermal microscopy,” Anal. Chem. 91, 10750 (2019).  
35A. Spadea, J. Denbigh, M. J. Lawrence, M. Kansiz, and P. Gardner, “Analysis of fixed and live single cells using optical photothermal infrared with concomitant Raman spectroscopy,” Anal. Chem. 93(8), 3938 (2021).  
36M. Kansiz and C. Prater, “Super resolution correlative far-field submicron simultaneous IR and Raman microscopy: A new paradigm in vibrational spectroscopy,” Proc. SPIE 11252, 112520E (2020).  
37J. Xu, X. Li, Z. Guo, W. E. Huang, and J.-X. Cheng, “Fingerprinting bacterial metabolic response to erythromycin by Raman-integrated mid-infrared photothermal microscopy,” Anal. Chem. 92(21), 14459 (2020).  
38X. Li, J. Xu, and J.-X. Cheng, in Molecular and Laser Spectroscopy, edited by V. P. Gupta (Elsevier, 2022), p. 281.  
39C. Prater, Y. Bai, S. C. Konings, I. Martinsson, V. S. Swaminathan, P. Nordenfelt, G. Gouras, F. Borondics, and O. Klementieva, “Fluorescently guided optical photothermal infrared microspectroscopy for protein-specific bioimaging at subcellular level,” J. Med. Chem. 66(4), 2542 (2023).  
40A. Paulus, S. Yogarasa, M. Kansiz, I. Martinsson, G. K. Gouras, T. Deierborg, A. Engdahl, F. Borondics, and O. Klementieva, “Correlative imaging to resolve molecular structures in individual cells: Substrate validation study for superresolution infrared microspectroscopy,” Nanomed. Nanotechnol. Biol. Med. 43, 102563 (2022).  
41C. Prater, U.S. provisional patent 63/054,167 (20 July 2020); U.S. patent 11,519,861 (6 December 2022); US patent 11,885,745 (30 January 2024).  
42Y. Zhang, H. Zong, C. Zong, Y. Tan, M. Zhang, Y. Zhan, and J.-X. Cheng, “Fluorescence-detected mid-infrared photothermal microscopy,” J. Am. Chem. Soc. 143(30), 11490 (2021).  
43M. Li, A. Razumtcev, R. Yang, Y. Liu, J. Rong, A. C. Geiger, R. Blanchard, C. Pfluegl, L. S. Taylor, and G. J. Simpson, “Fluorescence-detected mid-infrared photothermal microscopy,” J. Am. Chem. Soc. 143(29), 10809 (2021).  
44A. Razumtcev, M. Li, J. Rong, C. C. Teng, C. Pfluegl, L. S. Taylor, and G. J. Simpson, “Label-free autofluorescence-detected mid-infrared photothermal microscopy of pharmaceutical materials,” Anal. Chem. 94(17), 6512 (2022).  
45C. B. Prater, K. J. Kjoller, A. P. D. Stuart, D. A. Grigg, R. Limurn, and K. M. Gough, “Widefield super-resolution infrared spectroscopy and imaging of autofluorescent biological materials and photosynthetic microorganisms using fluorescence detected photothermal infrared (FL-PTIR),” Appl. Spectrosc. (published online).  
46C. Lima, H. Muhamadali, Y. Xu, M. Kansiz, and R. Goodacre, “Imaging isotopically labeled bacteria at the single-cell level using high-resolution optical infrared photothermal spectroscopy,” Anal. Chem. 93(6), 3082 (2021).  
47C. Lima, H. Muhamadali, and R. Goodacre, “Simultaneous Raman and infrared spectroscopy of stable isotope labelled Escherichia coli,” Sensors 22(10), 3928 (2022).  
48C. Lima, S. Ahmed, Y. Xu, H. Muhamadali, C. Parry, R. J. McGalliard, E. D. Carrol, and R. Goodacre, “Simultaneous Raman and infrared spectroscopy: A novel combination for studying bacterial infections at the single cell level,” Chem. Sci. 13(27), 8171 (2022).  
49S. O. Shuster, M. J. Burke, and C. M. Davis, “Spatiotemporal heterogeneity of de novo lipogenesis in fixed and living single cells,” J. Phys. Chem. B 127(13), 2918 (2023).  
50Y. Bai, D. Zhang, L. Lan, Y. Huang, K. Maize, A. Shakouri, and J.-X. Cheng, “Ultrafast chemical imaging by wide-field photothermal sensing of infrared absorption,” Sci. Adv. 5(7), eaav7127 (2019).  
51I. M. Pavlovetc, E. A. Podshivaylov, P. A. Frantsuzov, G. V. Hartland, and M. Kuno, “Quantitative infrared photothermal microscopy,” Proc. SPIE 11246, 1124613 (2020).  
52C. Krafft, Molecular and Laser Spectroscopy (Elsevier, 2022), p. 305.  
53C. Sandt and F. Borondics, “Super-resolution infrared microspectroscopy reveals heterogeneous distribution of photosensitive lipids in human hair medulla,” Talanta 254, 124152 (2023).  
54P. Koziol, K. Kosowska, D. Liberda, F. Borondics, and T. P. Wrobel, “Superresolved 3D mapping of molecular orientation using vibrational techniques,” J. Am. Chem. Soc. 144(31), 14278 (2022).  
55N. Baden, H. Kobayashi, and N. Urayama, “Submicron-resolution polymer orientation mapping by optical photothermal infrared spectroscopy,” Int. J. Polym. Anal. Charact. 25(1), 1 (2020).  
56R. Mankar, C. C. Gajjela, C. E. Bueso-Ramos, C. C. Yin, D. Mayerich, and R. K. Reddy, “Polarization sensitive photothermal mid-infrared spectroscopic imaging of human bone marrow tissue,” Appl. Spectrosc. 76(4), 508 (2022).  
57G. Bakir, B. E. Girouard, R. Wiens, S. Mastel, E. Dillon, M. Kansiz, and K. M. Gough, “Orientation matters: Polarization dependent IR spectroscopy of collagen from intact tendon down to the single fibril level,” Molecules 25(18), 4295 (2020).  
58J. Zhao, L. Jiang, A. Matlock, Y. Xu, J. Zhu, H. Zhu, L. Tian, B. Wolozin, and J.-X. Cheng, “Mid-infrared chemical imaging of intracellular tau fibrils using fluorescence-guided computational photothermal microscopy,” Light: Sci. Appl. 12(1), 147 (2023).  
59 3M 82600 is 5 μm thick double sided tape from 3M comprising a PET film carrier and a high performance acrylic adhesive on both sides. Available from Digikey and other suppliers.  
60See https://www.cytospec.com/ for hypespectral image analysis and chemometrics software from Cytospec.  
61See https://eigenvector.com/ for chemometrics software and training from Eigenvector Research, Inc.  
62M. Toplak, S. T. Read, C. Sandt, and F. Borondics, “Quasar: Easy machine learning for biospectroscopy,” Cells 10(9), 2300 (2021).  
63C. C. Gajjela, M. Brun, R. Mankar, S. Corvigno, N. Kennedy, Y. Zhong, J. Liu, A. K. Sood, D. Mayerich, S. Berisha, and R. Reddy, “Leveraging mid-infrared spectroscopic imaging and deep learning for tissue subtype classification in ovarian cancer,” Analyst 148(12), 2699 (2023).  
64C. Yang, J. Xie, A. Gowen, and J.-L. Xu, “Machine learning driven methodology for enhanced nylon microplastic detection and characterization,” Sci. Rep. 14(1), 3464 (2024).  
65S. Shams, C. Lima, Y. Xu, S. Ahmed, R. Goodacre, and H. Muhamadali, “Optical photothermal infrared spectroscopy: A novel solution for rapid identification of antimicrobial resistance at the single-cell level via deuterium isotope labeling,” Front. Microbiol. 14, 1077106 (2023).  
66A. C. Waajen, C. Lima, R. Goodacre, and C. S. Cockell, “Life on Earth can grow on extraterrestrial organic carbon,” Sci. Rep. 14(1), 3691 (2024).  
67A. Barth, “Infrared spectroscopy of proteins,” Biochim. Biophys. Acta, Bioenerg. 1767(9), 1073 (2007).  
68O. Klementieva, C. Sandt, I. Martinsson, M. Kansiz, G. K. Gouras, and F. Borondics, “Super-resolution infrared imaging of polymorphic amyloid aggregates directly in neurons,” Adv. Sci. 7(6), 1903004 (2020).  
69N. Gvazava, S. C. Konings, E. Cepeda-Prado, V. Skoryk, C. H. Umeano, J. Dong, I. A. N. Silva, D. R. Ottosson, N. D. Leigh, D. E. Wagner, and O. Klementieva, “Label-free high-resolution photothermal optical infrared spectroscopy for spatiotemporal chemical analysis in fresh, hydrated living tissues and embryos,” J. Am. Chem. Soc. 145(45), 24796 (2023).  
70See https : // itis . swiss / virtual - population / tissue - properties / database / heat - capacity/ for a table of heat capacities for different biological tissues and fluids.  
71M. Kansiz, L. M. Dowling, I. Yousef, O. Guaitella, F. Borondics, and J. Sulé-Suso, “Optical photothermal infrared microspectroscopy discriminates for the first time different types of lung cells on histopathology glass slides,” Anal. Chem. 93(32), 11081 (2021).  
72T. A. Shaik, A. Ramoji, N. Milis, J. Popp, and C. Krafft, “Optical photothermal infrared spectroscopy and discrete wavenumber imaging for high content screening of single cells,” Analyst 148(22), 5627 (2023).  
73E. Reiner, F. Weston, N. Pleshko, and W. Querido, “Application of optical photothermal infrared (O-PTIR) spectroscopy for assessment of bone composition at the submicron scale,” Appl. Spectrosc. 77(11), 1311 (2023).  
74M. Kim, E. Koyama, C. M. Saunders, W. Querido, N. Pleshko, and M. Pacifici, “Synovial joint cavitation initiates with microcavities in interzone and is coupled to skeletal flexion and elongation in developing mouse embryo limbs,” Biol. Open 11(6), bio059381 (2022).  
75T. Ahn, M. Jueckstock, G. S. Mandair, J. Henderson, B. P. Sinder, K. M. Kozloff, and M. M. Banaszak Holl, “Matrix/mineral ratio and domain size variation with bone tissue age: A photothermal infrared study,” J. Struct. Biol. 214(3), 107878 (2022).  
76S. Chen, H. Wang, D. Liu, J. Bai, H. J. Haugen, B. Li, and H. Yan, “Early osteoimmunomodulation by mucin hydrogels augments the healing and revascularization of rat critical-size calvarial bone defects,” Bioact. Mater. 25, 176 (2023).  
77M. Rahmati, S. Stötzel, T. El Khassawna, C. Mao, A. Ali, J. C. Vaughan, K. Iskhahova, D. C. Florian Wieland, A. G. Cantalapiedra, G. Perale, F. Betge, E. P. Dillon, S. P. Lyngstadaas, and H. J. Haugen, “Intrinsically disordered peptides enhance regenerative capacities of bone composite xenografts,” Mater. Today 52, 63 (2022).  
78E. J. Clarke, C. Lima, J. R. Anderson, C. Castanheira, J. Hyett, R. Goodacre, and M. J. Peffers, “Novel spectroscopy techniques used to interrogate equine osteoarthritic extracellular vesicles,” Osteoarthritis Cartilage 30, S95 (2022).  
79P. Bouzy, I. D. Lyburn, S. E. Pinder, R. Scott, J. Mansfield, J. Moger, C. Greenwood, I. Bouybayoune, E. Cornford, K. Rogers, and N. Stone, “Exploration of utility of combined optical photothermal infrared and Raman imaging for investigating the chemical composition of microcalcifications in breast cancer,” Anal. Methods 15(13), 1620 (2023).  
80D. Bazin, E. Bouderlique, E. Tang, M. Daudon, J.-P. Haymann, V. Frochot, E. Letavernier, E. Van de Perre, J. C. Williams, J. E. Lingeman, and F. Borondics, “Using mid infrared to perform investigations beyond the diffraction limits of microcristalline pathologies: Advantages and limitation of Optical PhotoThermal IR spectroscopy,” C. R. Chim. 25(S1), 105 (2022).  
81E. Bouderlique, E. Tang, J. Zaworski, A. Coudert, D. Bazin, F. Borondics, J.-P. Haymann, G. Leftheriotis, L. Martin, M. Daudon, and E. Letavernier, “Vitamin D and calcium supplementation accelerate vascular calcification in a model of pseudoxanthoma elasticum,” Int. J. Mol. Sci. 23(4), 2302 (2022).  
82D. Bazin, M. Rabant, J. Mathurin, M. Petay, A. Deniset-Besseau, A. Dazzi, Y. Su, E. P. Hessou, F. Tielens, F. Borondics et al., “Cystinuria and cystinosis are usually related to L-cystine: Is this really the case for cystinosis? A physicochemical investigation at micrometre and nanometre scale,” C. R. Chim. 25(S1), 489 (2022).  
83Z. Zhao, W. Yu, W. Yang, G. Zhang, C. Huang, J. Han, R. Narain, and H. Zeng, “Dual-protection inorganic-protein coating on Mg-based biomaterials through tooth-enamel-inspired biomineralization,” Adv. Mater. 36, 2313211 (2024).  
84Z. Zhao, M. Pan, C. Qiao, L. Xiang, X. Liu, W. Yang, X.-Z. Chen, and H. Zeng, “Bionic engineered protein coating boosting anti-biofouling in complex biological fluids,” Adv. Mater. 35(6), 2208824 (2023).  
85M. Puthia, J. Petrlova, G. Petruk, M. Butrym, F. Samsudin, M. Å. Andersson, A.-C. Strömdahl, S. Wasserstrom, E. Hartman, S. Kjellström, L. Caselli, O. Klementieva, P. J. Bond, M. Malmsten, D. B. Raina, and A. Schmidtchen, “Bioactive suture with added innate defense functionality for the reduction of bacterial infection and inflammation,” Adv. Healthcare Mater. 12(31), 2300987 (2023).  
86R. Yang, G. G. Z. Zhang, K. Kjoller, E. Dillon, H. S. Purohit, and L. S. Taylor, “Phase separation in surfactant-containing amorphous solid dispersions: Orthogonal analytical methods to probe the effects of surfactants on morphology and phase composition,” Int. J. Pharm. 619, 121708 (2022).  
87D. Khanal, J. Zhang, W.-R. Ke, M. M. Banaszak Holl, and H.-K. Chan, “Bulk to nanometer-scale infrared spectroscopy of pharmaceutical dry powder aerosols,” Anal. Chem. 92(12), 8323 (2020).  
88D. Khanal, J. Kim, J. Zhang, W.-R. Ke, M. M. B. Holl, and H. K. Chan, “Optical photothermal infrared spectroscopy for nanochemical analysis of pharmaceutical dry powder aerosols,” Int. J. Pharm. 632, 122563 (2023).  
89A. Tarafdar, J. Xie, A. Gowen, A. C. O’Higgins, and J.-L. Xu, “Advanced optical photothermal infrared spectroscopy for comprehensive characterization of microplastics from intravenous fluid delivery systems,” Sci. Total Environ. 929, 172648 (2024).  
90N. E. Olson, Y. Xiao, Z. Lei, and A. P. Ault, “Simultaneous optical photothermal infrared (O-PTIR) and Raman spectroscopy of submicrometer atmospheric particles,” Anal. Chem. 92(14), 9932 (2020).  
91J. A. Mirrielees, R. M. Kirpes, S. M. Haas, C. D. Rauschenberg, P. A. Matrai, A. Remenapp, V. L. Boschi, A. M. Grannas, K. A. Pratt, and A. P. Ault, “Probing individual particles generated at the freshwater–seawater interface through combined Raman, photothermal infrared, and X-ray spectroscopic characterization,” ACS Meas. Sci. Au 2(6), 605 (2022).  
92V. A. Marple, D. L. Roberts, F. J. Romay, N. C. Miller, K. G. Truman, M. Van Oort, B. Olsson, M. J. Holroyd, J. P. Mitchell, and D. Hochrainer, “Next generation pharmaceutical impactor (a new impactor for pharmaceutical inhaler testing). Part I: Design,” J. Aerosol Med. 16(3), 283 (2003).  
93X. Lin, A. A. Gowen, S. Chen, and J.-L. Xu, “Baking releases microplastics from polyethylene terephthalate bakeware as detected by optical photothermal infrared and quantum cascade laser infrared,” Sci. Total Environ. 924, 171408 (2024).  
94P. Zhao, Y. Zhao, L. Cui, Y. Tian, Z. Zhang, Q. Zhu, and W. Zhao, “Multiple antibiotics distribution in drinking water and their co-adsorption behaviors by different size fractions of natural particles,” Sci. Total Environ. 775, 145846 (2021).  
95K. Kniazev, I. M. Pavlovetc, S. Zhang, J. Kim, R. L. Stevenson, K. Doudrick, and M. Kuno, “Using infrared photothermal heterodyne imaging to characterize micro- and nanoplastics in complex environmental matrices,” Environ. Sci. Technol. 55(23), 15891 (2021).  
96Y. Shi, L. Yi, G. Du, X. Hu, and Y. Huang, “Visual characterization of microplastics in corn flour by near field molecular spectral imaging and data mining,” Sci. Total Environ. 862, 160714 (2023).  
97Y. Su, X. Hu, H. Tang, K. Lu, H. Li, S. Liu, B. Xing, and R. Ji, “Steam disinfection releases micro(nano)plastics from silicone-rubber baby teats as examined by optical photothermal infrared microspectroscopy,” Nat. Nanotechnol. 17, 76 (2022).  
98F. Yan, X. Wang, H. Sun, Z. Zhu, W. Sun, X. Shi, J. Zhang, L. Zhang, X. Wang, and M. Liu, “Development of a binary digestion system for extraction microplastics in fish and detection method by optical photothermal infrared (O-PTIR),” Front. Mar. Sci. 9, 845062 (2022).  
99J. Barrett, Z. Chase, J. Zhang, M. M. B. Holl, K. Willis, A. Williams, B. D. Hardesty, and C. Wilcox, “Microplastic pollution in deep-sea sediments from the great Australian bight,” Front. Mar. Sci. 7(808), 576170 (2020).  
100J. M. Masterson, A. HassanMazandarani, W. Querido, A. Steplewski, Y. Zhang, C. Huynh, A. Fertala, N. Pleshko, and M. M. Garcia, “PD53-01 are microplastics present in human testicle tissue? Analysis using infrared spectroscopy,” J. Urol. 211(5S), e1138 (2024).  
101O. Nwachukwu, K. Kniazev, A. Abarca Perez, M. Kuno, and K. Doudrick, “Single-particle analysis of the photodegradation of submicron polystyrene particles using infrared photothermal heterodyne imaging,” Environ. Sci. Technol. 58(2), 1312 (2024).  
102W. Huang, J. Deng, J. Liang, and X. Xia, “Comparison of lead adsorption on the aged conventional microplastics, biodegradable microplastics and environmentally-relevant tire wear particles,” Chem. Eng. J. 460, 141838 (2023).  
103M. Dong, Z. She, X. Xiong, G. Ouyang, and Z. Luo, “Automated analysis of microplastics based on vibrational spectroscopy: Are we measuring the same metrics?,” Anal. Bioanal. Chem. 414(11), 3359 (2022).  
104G. Bitossi, R. Giorgi, M. Mauro, B. Salvadori, and L. Dei, “Spectroscopic techniques in cultural heritage conservation: A survey,” Appl. Spectrosc. Rev. 40(3), 187 (2005).  
105G.-L. Liu and S. G. Kazarian, “Recent advances and applications to cultural heritage using ATR-FTIR spectroscopy and ATR-FTIR spectroscopic imaging,” Analyst 147(9), 1777 (2022).  
106V. Beltran, A. Marchetti, G. Nuyts, M. Leeuwestein, C. Sandt, F. Borondics, and K. De Wael, “Nanoscale analysis of historical paintings by means of O-PTIR spectroscopy: The identification of the organic particles in L’Arlésienne (portrait of Madame Ginoux) by van Gogh,” Angew. Chem., Int. Ed. 60(42), 22753 (2021).  
107L. Chua, A. Banas, and K. Banas, “Comparison of ATR–FTIR and O-PTIR imaging techniques for the characterisation of zinc-type degradation products in a paint cross-section,” Molecules 27(19), 6301 (2022).  
108X. Ma, G. Pavlidis, E. Dillon, V. Beltran, J. J. Schwartz, M. Thoury, F. Borondics, C. Sandt, K. Kjoller, B. H. Berrie, and A. Centrone, “Micro to nano: Multiscale IR analyses reveal zinc soap heterogeneity in a 19th-century painting by Corot,” Anal. Chem. 94(7), 3103 (2022).  
109T. Calligaro, A. Banas, K. Banas, I. B. Radovic, M. Brajkovi ´ c, M. Chiari, A.- ´ M. Forss, I. Hajdas, M. Krmpotic, A. Mazzinghi, E. Menart, K. Mizohata, M.´ Oinonen, L. Pichon, J. Raisanen, Z. Siketic,´ Z. Šmit, and A. Simon, “Emergingˇ nuclear methods for historical painting authentication: AMS-14C dating, MeV-SIMS and O-PTIR imaging, global IBA, differential-PIXE and full-field PIXE mapping,” Forensic Sci. Int. 336, 111327 (2022).  
110A. Marchetti, V. Beltran, G. Nuyts, F. Borondics, S. De Meyer, M. Van Bos, J. Jaroszewicz, E. Otten, M. Debulpaep, and K. De Wael, “Novel optical pho tothermal infrared (O-PTIR) spectroscopy for the noninvasive characterization of heritage glass-metal objects,” Sci. Adv. 8(9), eabl6769 (2022).  
111W. B. Kammrath and M. Kansis, “Forensic paint analysis with simultaneous sub-micron O-PTIR and Raman microspectroscopy,” https://www.photothermal. com/forensic-paint-analysis-with-simultaneous-submicron-o-ptir-and-ramanmicrospectroscopy/.  
112A. Banas, K. Banas, M. K. F. Lo, M. Kansiz, S. M. P. Kalaiselvi, S. K. Lim, J. Loke, and M. B. H. Breese, “Detection of high-explosive materials within fingerprints by means of optical-photothermal infrared spectromicroscopy,” Anal. Chem. 92(14), 9649 (2020).  
113S. He, P. Bouzy, N. Stone, C. Ward, and I. Hamerton, “Analysis of the chemical distribution of self-assembled microdomains with the selective localization of amine-functionalized graphene nanoplatelets by optical photothermal infrared microspectroscopy,” Anal. Chem. 94(34), 11848 (2022).  
114J. Yoo, S. M. Lee, K. Lee, S. C. Lim, M. S. Jeong, J. Kim, and T. G. Lee, “Functional group inhomogeneity in graphene oxide using correlative absorption spectroscopy,” Appl. Surf. Sci. 613, 155885 (2023).  
115J. Reffner, “Advances in infrared microspectroscopy and mapping molecular chemical composition at submicrometer spatial resolution,” Spectroscopy 33(9), 12 (2018).  
116C. Marcott, M. Kansiz, E. Dillon, D. Cook, M. N. Mang, and I. Noda, “Two-dimensional correlation analysis of highly spatially resolved simultaneous IR and Raman spectral imaging of bioplastics composite using optical photothermal infrared and Raman spectroscopy,” J. Mol. Struct. 1210, 128045 (2020).  
117A. Zhang, Z. Wang, Y. Guan, J. Zhao, G. Zhao, and G. Wang, “Strong PP/PTFE microfibril reinforced composites achieved by enhanced crystallization under CO2 environment,” Polym. Test. 112, 107630 (2022).  
118A. Zhang, J. Chai, C. Yang, J. Zhao, G. Zhao, and G. Wang, “Fibrosis mechanism, crystallization behavior and mechanical properties of in-situ fibrillary PTFE reinforced PP composites,” Mater. Des. 211, 110157 (2021).  
119A. Sarra, S. Brutti, O. Palumbo, F. Capitani, F. Borondics, G. B. Appetecchi, N. Carboni, S. A. Ahad, H. Geaney, K. Ryan, and A. Paolone, “Solid–electrolyte interface formation on Si nanowires in Li-ion batteries: The impact of electrolyte additives,” Batteries 9(3), 148 (2023).  
120A. Wu, Y. Zhou, J. Lv, D. Zhang, Y. Peng, Q. Ye, P. Fu, W. Wang, X. Lin, S. Liu, M. Xu, Z. Qi, S. Zhu, W. Zhu, J. Yan, X. Tu, and X. Li, “Boosting electrocatalytic nitrate-to-ammonia conversion via plasma enhanced CuCo alloy–substrate interaction,” ACS Sustain. Chem. Eng. 10(44), 14539 (2022).  
121P. Zhao, Y. Zhao, Y. Guo, R. Guo, Y. Tian, and W. Zhao, “Preparation of CuO/γAl2O3 catalyst for degradation of azo dyes (reactive brilliant red X–3B): An optimization study,” J. Cleaner Prod. 328, 129624 (2021).  
122Z. Qin, S. Dai, C. C. Gajjela, C. Wang, V. G. Hadjiev, G. Yang, J. Li, X. Zhong, Z. Tang, Y. Yao, A. M. Guloy, R. Reddy, D. Mayerich, L. Deng, Q. Yu, G. Feng, H. A. Calderon, F. C. Robles Hernandez, Z. M. Wang, and J. Bao, “Spontaneous formation of 2D/3D heterostructures on the edges of 2D Ruddlesden–Popper hybrid perovskite crystals,” Chem. Mater. 32(12), 5009 (2020).  
123M. S. Anderson, “Concurrent surface enhanced infrared and Raman spectroscopy with single molecule sensitivity,” Rev. Sci. Instrum. 94, 025103 (2023).  
124A. M. Jubb, M. Rebecca Stokes, R. J. McAleer, P. C. Hackley, E. Dillon, and J. Qu, “Mapping ancient sedimentary organic matter molecular structure at nanoscales using optical photothermal infrared spectroscopy,” Org. Geochem. 177, 104569 (2023).  
125J. Anderson, M. Kansiz, M. Lo, and C. Marcott, “Submicron simultaneous IR and Raman spectroscopy (IR + Raman): Breakthrough developments in optical photothermal IR (O-PTIR) combined for enhanced failure analysis,” in ISTFA 2019 (ASM International, 2019), p. 292.  
126M. Lo, C. Marcott, M. Kansiz, E. Dillon, and C. Prater, “Sub-micron, noncontact, super-resolution infrared microspectroscopy for microelectronics contamination and failure analyses,” in 2020 IEEE International Symposium on the Physical and Failure Analysis of Integrated Circuits (IPFA), 1 (IEEE, 2020).  
127D. J. Anderson, M. Kansiz, M. Lo, E. Dillon, and C. Marcott, “Enhanced failure analysis (FA) of organic contamination using submicron simultaneous IR and Raman spectroscopy: Breakthrough developments of optical photothermal IR (O-PTIR),” in ISTFA 2020 (ASM International, 2020), Vol. 75.  
128M. K. F. Lo, J. Anderson, E. P. Dillon, M. Kansiz, and C. A. Marcott, “Submicron noncontact simultaneous infrared and Raman spectroscopy for challenging failure analysis,” in ISTFA 2021: Conference Proceedings from the 47th International Symposium for Testing and Failure Analysis (ASM International, 2021), p. 196.  
129S. Zulkifli, B. Zee, and M. K. F. Lo, “Novel submicron spatial resolution infrared microspectroscopy for failure analysis of semiconductor components,” in 2022 IEEE International Symposium on the Physical and Failure Analysis of Integrated Circuits (IPFA) (IEEE, 2022), p. 1.  
130M. Tamamitsu, K. Toda, R. Horisaki, and T. Ideguchi, “Quantitative phase imaging with molecular vibrational sensitivity,” Opt. Lett. 44(15), 3729 (2019).  
131K. Toda, M. Tamamitsu, Y. Nagashima, R. Horisaki, and T. Ideguchi, “Molecular contrast on phase-contrast microscope,” Sci. Rep. 9(1), 9957 (2019).  
132K. Hashimoto, V. R. Badarla, A. Kawai, and T. Ideguchi, “Complementary vibrational spectroscopy,” Nat. Commun. 10(1), 4411 (2019).  
133K. Toda, M. Tamamitsu, and T. Ideguchi, “Adaptive dynamic range shift (ADRIFT) quantitative phase imaging,” Light: Sci. Appl. 10(1), 1 (2021).  
134T. Yuan, M. A. Pleitez, F. Gasparin, and V. Ntziachristos, “Wide-field midinfrared hyperspectral imaging by snapshot phase contrast measurement of optothermal excitation,” Anal. Chem. 93(46), 15323 (2021).  
135T. Yuan, L. Riobo, F. Gasparin, V. Ntziachristos, and M. A. Pleitez, “Phaseshifting optothermal microscopy enables live-cell mid-infrared hyperspectral  
imaging of large cell populations at high confluency,” Sci. Adv. 10(8), eadj7944 (2024).  
136D. Zhang, L. Lan, Y. Bai, H. Majeed, M. E. Kandel, G. Popescu, and J.-X. Cheng, “Bond-selective transient phase imaging via sensing of the infrared photothermal effect,” Light: Sci. Appl. 8(1), 116 (2019).  
137K. Kniazev, E. Zaitsev, S. Zhang, Y. Ding, L. Ngo, Z. Zhang, G. V. Hartland, and M. Kuno, “Hyperspectral and nanosecond temporal resolution widefield infrared photothermal heterodyne imaging,” ACS Photonics 10(8), 2854 (2023).  
138Q. Xia, Z. Guo, H. Zong, S. Seitz, C. Yurdakul, M. S. Ünlü, L. Wang, J. H. Connor, and J.-X. Cheng, “Single virus fingerprinting by widefield interferometric defocus-enhanced mid-infrared photothermal microscopy,” Nat. Commun. 14(1), 6655 (2023).  
139J. Zhao, A. Matlock, H. Zhu, Z. Song, J. Zhu, B. Wang, F. Chen, Y. Zhan, Z. Chen, Y. Xu et al., “Bond-selective intensity diffraction tomography,” Nat. Commun. 13(1), 7767 (2022).  
140H. Zong, C. Yurdakul, J. Zhao, Z. Wang, F. Chen, M. S. Ünlü, and J.-X. Cheng, “Bond-selective full-field optical coherence tomography,” Opt. Express 31(25), 41202 (2023).  
141J. Yin, M. Zhang, Y. Tan, Z. Guo, H. He, L. Lan, and J.-X. Cheng, “Video-rate mid-infrared photothermal imaging by single-pulse photothermal detection per pixel,” Sci. Adv. 9(24), eadg8814 (2023).