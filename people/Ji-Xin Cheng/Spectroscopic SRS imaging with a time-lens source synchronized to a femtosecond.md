# Spectroscopic SRS imaging with a time-lens source synchronized to a femtosecond pulse shaper

Ke Wang,a Delong Zhang,b Kriti Charan,b Mikhail N. Slipchenko,b Ping Wang,b Ji-Xin Cheng \*b,c and Chris Xu#a

a School of Applied and Engineering Physics, Cornell University, Ithaca, NY, USA 14853 b Weldon School of Biomedical Engineering, Purdue University, West Lafayette, IN, 47907, USA c Department of Chemistry, Purdue University, West Lafayette, IN, 47907, USA

\* jcheng@purdue.edu, # chris.xu@cornell.edu

## ABSTRACT

Though single-color coherent Raman microscopy has been widely used for vibrational imaging of isolated Raman bands, it is still challenging to visualize molecules having overlapping Raman bands. We address this issue by developing a spectroscopic SRS microscope with a time-lens laser source synchronized to a femtosecond laser. The time-lens source provides 2-ps pulse at the wavelength of 1064 nm. A pulse shaper is installed for intra-pulse spectral scanning of the femtosecond laser output. By electronically modulating the time-lens source at MHz frequency, spectroscopic stimulated Raman loss (SRL) images were obtained on a laser-scanning microscope. Using this microscope, we have been able to detect 0.2% DMSO in aqueous solution. Spectroscopic SRL images of prostate cancer cells were obtained. Multivariate curve resolution analysis was further applied to decompose the SRL images into concentration maps of proteins and lipids. With high sensitivity and high spectral resolution, this method offers exciting potential in label-free imaging of live cells using fingerprint Raman bands.

Keywords: hyperspectral, stimulated Raman scattering, time-lens, multivariate curve resolution, nonlinear optical microscopy, pulse shaper

## 1. INTRODUCTION

Coherent Raman Scattering (CRS) microscopy1 , with contrast from coherent anti-Stokes Raman scattering (CARS)2,3 or stimulated Raman scattering (SRS)4 , allows label-free imaging of biological samples with endogenous image contrast based on vibrational spectroscopy. SRS has superseded CARS as a contrast mechanism for microscopy, because it has no image artifacts from non-resonant background and its linear concentration dependence. SRS microscopy has found wide applications in imaging various biological and chemical samples from cellular level to tissues and organs4-12. So far most SRS imaging are performed in a single-frequency configuration, which uses pump and stokes pulses at fixed wavelengths to probe a specific vibrational bond. As a result, it is difficult for single frequency SRS imaging to resolve molecular species that have overlapping Raman bands. Another drawback of single frequency SRS imaging is the lack of spectral in-formation. Two methods have been proposed to address these issues, including multiplex9 and hyperspectral SRS imaging13,14. Multiplex SRS simultaneously image a specimen at several distinct wavelengths. Hyper-spectral SRS continuously scans the frequency of the excitation pulse to get a stack of spectrally resolved images.

![](images/5c00c877b389ec7d86942aa9b6cab5daae658be21cb9a4e4234df1779d2005da.jpg)

<details>
<summary>text_image</summary>

a
Virtual states
CARS
ωp ωs ωm
S0 ↑Ω
Light-molecule interaction
SRS
b
Pump
ΔIp
t
Modulated Stokes
Is
</details>

Fig. 1. Energy diagram of CARS and SRS (a) and SRS detection mechanism (b).

To perform CRS imaging, two synchronized laser sources providing pump $\left( \omega _ { \mathsf { p } } \right)$ and Stokes fields $\left( \omega _ { \mathrm { s } } \right)$ are needed. The frequency difference between the pump and Stokes $\left( \mathrm { { \omega _ { p } } - \mathrm { { \omega _ { s } } } } \right)$ should be tuned to the resonant frequency (Ω) of molecular vibration (Fig. 1a). For CARS, a new frequency at anti-Stokes frequency $\mathfrak { \omega _ { \mathrm { a s } } } \left( \mathfrak { \omega _ { \mathrm { a s } } } \overline { { = } } 2 \mathfrak { o _ { \mathrm { p } } } \overline { { \circ } } \overline { { \mathfrak { o } _ { \mathrm { s } } } } \right)$ is generated and detected. For SRS imaging, the Stokes pulse train is modulated at high frequency (typically MHz) to suppress laser noise, and the modulation of the pump pulse train, in the form of stimulated Raman loss (SRL, $\Delta \mathrm { I } _ { \mathrm { p } } )$ is detected by a lock-in amplifier for imaging (Fig. 1b)4 . The pump pulse train can also be modulated and the modulation of the Stokes pulse train, in the form of stimulated Raman gain (SRG, ΔI ) can also be detected for SRS imaging. For hyperspectral SRS imaging, typically one is a femtosecond source with broad bandwidth to cover the vibrational bandwidth of the target, while the other is a picosecond source with narrow bandwidth to get spectral resolution. A tunable bandpass filter, such as a slit in a pulse shaper14 was used as a linear spectral filter which narrows the spectrum. Current solutions of the picosecond source is either from spectral filtering of a broadband source14, which is highly inefficient in the use of available laser power and leads to limited power and reduced sensitivity, or high-cost, bulky mode-locked Titanium:Sapphire (Ti:S) lasers or optical parametric oscillators13,14.

Recently, Wang et al. demonstrated a new scheme for two-color, synchronized picosecond light sources for CRS imaging, based on the time-lens concept and its superb capability of being synchronized to any mode-locked lasers15,16. A time-lens imposes a temporal quadratic phase modulation onto the incident light, analogous to a spatial lens imposing a spatial quadratic phase onto a wavefront in space. The phase modulation broadens the spectrum of the input light, and generates the necessary spectral bandwidth for a short pulse. In practice, the quadratic phase modulation is approximated by applying a sinusoidal drive voltage to an electro-optic (EO) phase modulator. With proper dispersion compensation, picosecond or even femtosecond pulses can be generated from a CW laser. While the repetition rate of a conventional mode-locked laser is constrained by the cavity length, the repetition rate of a time-lens source is entirely determined by the electrical drive signal. Thus, a time-lens source has the remarkable capability of synchronizing to any mode-locked laser. The time-lens also benefits from a robust all-fiber configuration and RF electronic tuning of the pulse delay for the temporal overlap between the two pulse trains. Critical to SRS imaging, the time-lens source is naturally compatible with intensity modulation. As a result, free-space modulators such as electro-optic or acousto-optic modulators are no longer needed. With time-lens source, CRS imaging up to video rate has been demonstrated15. However, current time-lens source suffers from low output power (160 mW after intensity modulation) due to the high insertion loss of the all-fiber compressor15, which limits its application to high-sensitivity CRS imaging. In addition, the use of fiber coupled intensity modulator for modulating the pulse train at several MHz for SRS imaging introduces additional insertion loss, system cost and complexity.

In this paper, we demonstrate high-sensitivity, hyper-spectral stimulated Raman scattering (SRS) imaging, using a time-lens source synchronized to a femtosecond mode-locked Ti:S laser. We directly modulate the cur-rent of the CW laser diode (LD) in the time-lens source with a square wave at several MHz for SRS imaging, which not only eliminates the intensity modulator but also vastly improves the extinction ratio (optical power ratio between the “on” and “off” state) because below threshold there is no lasing at all. A free-space transmission grating pair with high diffraction efficiency is used to compress the chirped pulse, which improves the modulated output power to 400 mW. The tunable picosecond pump pulse is generated by pulse shaping of a femtosecond Ti:S laser through intra-pulse spectral scanning. Our system improves the sensitivity of SRS imaging by five times compared to a spectrally filtered OPO output14, by measuring the concentration of dimethyl sulfoxide (DMSO) in aqueous solution down to 28 mM. We also performed hyperspectral SRS imaging of PC3 cells. Multivariate curve resolution (MCR) method14 is used to reconstruct a quantitative concentration image for each individual component, which clearly maps the lipid and protein content and distribution in these cells.

## 2. EXPERIMENTAL SETUP AND SAMPLE PREPARATION

In our experiment, a mode-locked Ti:S laser (Chameleon APE, Coherent) delivers tunable pump pulse with a duration of 140 fs at 80 MHz. The modulated Stokes pulses are generated from a 1064-nm time-lens source, which is described in detail in Ref. [15]. Two major improvements have been made in this setup: First, the CW LD is directly modulated by a 2.29 MHz square wave generated from a function generator, which replaces the second intensity modulator in the original setup; second, a free-space transmission grating pair is used to compress the output from the power amplifier, which improves the modulated power to 400 mW.

For hyperspectral SRS imaging, we set up a pulse shaper for the Ti:S laser output with a tunable slit in the Fourier plane, described in detail in Ref. [14]. The pump and the Stokes beams are spatially combined with a dichroic, and sent into a laser scanning microscope. A water immersion objective lens (UPlanSApo, Olympus) with numerical aperture (NA) of 1.2 was used to focus the light into the sample. A second objective lens (LUMFI, Olympus) of NA 1.10 was used to collect the signal. Two 850/90 nm bandpass filters and a 900 nm short pass filter were used to remove the 1064 nm Stokes beam. The SRL signal was detected by a silicon photodiode (S3994-01, Hamamatsu) and extracted by a digital lock-in amplifier (HF2LI, Zurich Instrument) with a center frequency at 2.29 MHz17. The dwell time for each pixel is 2 µs for DMSO solutions and 4 µs for cells.

The hyperspectral SRS stacks were imported to Matlab (MathWorks, Natick) using ImageJ (National Institutes of Health) as spectra arrays of all the pixels for MCR analysis. The concentration matrix and spectra of each component were then retrieved by a Matlab tool box, MCR-ALS toolbox. Non-negative concentration and spectrum were set as constraints, and 0.01% is set as the convergence. The corresponding images were then re-constructed with Matlab and ImageJ.

## 3. SYSTEM CHARACTERIZATION AND HYPERSPECTRAL SRS IMAGING

First we characterize the time-lens output. Figure 2a shows the 2.29 MHz modulated pulse train from the time-lens output, demonstrating its capability of direct current modulation for SRS imaging. Tunable modulation up to 10 MHz (limited by the bandwidth of the function generator) can be easily achieved. To directly characterize the temporal profile of the pulses from the time-lens source, we measure the cross correlation between the time-lens output and the 140 fs pulses from the Ti:S laser (Figure 2b), using noncollinear sum frequency generation from a beta barium borate crystal (β- BBO)15,16. Optical delay scanning is easily achieved by an electronically RF delay line, eliminating the need for freespace optical delay lines (e.g., translation stages) which could change optical alignment. The full-width-at-halfmaximum (FWHM) pulse width of the time-lens source is 1.6 ps. To evaluate synchronization performance, we measured intensity fluctuation of the sum frequency signal at half maximum (red line, inset in Figure 2b), from which timing jitter can be derived15,16. The measured root-mean-square (RMS) timing jitter is 55 fs, only a small fraction of the pulse width and suitable for CRS imaging.

![](images/fcde624414d15091677c08db315ab17bf97e26fcb5dd47b198be8519123e720c.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Normalized intensity |
| --------- | -------------------- |
| 0.0       | ~0.9                 |
| 0.5       | ~0.9                 |
| 1.0       | ~0.9                 |
| 1.5       | ~0.9                 |
| 2.0       | ~0.9                 |
| Delay (ps) | Normalized intensity |
| -15       | ~0.0                 |
| -10       | ~0.0                 |
| -5        | ~0.0                 |
| 0         | ~1.0                 |
| 5         | ~0.5                 |
| 10        | ~0.5                 |
| 15        | ~0.5                 |
</details>

Fig. 2. Characterization of the time-lens output and its synchronization performance. a. Temporal trace of the time-lens output modulated by a 2.29 MHz square wave. b. Cross-correlation trace (blue) between the time-lens source and the 140 fs pulse from the mode-locked Ti:S laser. Inset: measured sum-frequency signal at the half maximum of the crosscorrelation trace over a time span of 240 seconds at a sampling rate of 1 kHz (red).

To demonstrate the capability of the time-lens source for high-sensitivity hyperspectral SRS imaging, we perform SRS imaging of DMSO in aqueous solutions at various concentrations (Figure 3). To map the Raman spectrum of DMSO, we took hyperspectral SRL images at the interface of pure DMSO droplet and air, and measured the SRL signal of a single pixel inside the DMSO droplet (Figure 3a). The single pixel DMSO spectrum (red dots, figure 3b) is in good agreement with the spontaneous Raman spectrum (solid line, figure 3b). The MCR analysis resolved the concentration of DMSO at each pixel based on the Raman spectrum of pure DMSO (Figure 3b), with a linear response of MCR results to real DMSO concentration (Figure 3c). MCR resulting images of DMSO at various concentrations are shown in Figure 3d. It can be seen that even at a concentration down to 28 mM, there is clear SRL signal from DMSO. The total equivalent acquisition time is 100 µs per pixel, which is 100,000 times faster than spontaneous Raman. Com-pared with our previous result obtained with an OPO source, the measurable minimum concentration is improved by 5 times, corresponding to 5 times increase in sensitivity with the time-lens source. These results demonstrated the capability of the time-lens source for high-sensitivity hyperspectral SRS imaging.

![](images/3b5110054561f636f84d4c7444e54cff7ebc4c6bc334a6c93832ee472e897d0e.jpg)

<details>
<summary>line chart</summary>

| Distance (μm) | Int. (a.u.) |
| ------------- | ----------- |
| 0             | 0           |
| 20            | 0           |
| 40            | 0           |
| 60            | 0           |
| 80            | 600         |
| 100           | 600         |
| 120           | 600         |
| 140           | 500         |
| 160           | 450         |
| 180           | 400         |
| 200           | 350         |
| 220           | 300         |
| 240           | 250         |
| 260           | 200         |
| 280           | 150         |
| 300           | 100         |
| 320           | 50          |
| 340           | 25          |
| 360           | 10          |
| 380           | 5           |
| 400           | 2           |
| 420           | 1           |
| 440           | 0.5         |
| 460           | 0.2         |
| 480           | 0.1         |
| 500           | 0.05        |
| 520           | 0.02        |
| 540           | 0.01        |
| 560           | 0.005       |
| 580           | 0.002       |
| 600           | 0.001       |
| 620           | 0.0005      |
| 640           | 0.0002      |
| 660           | 0.0001      |
| 680           | 0.00005     |
| 700           | 0.00002     |
| 720           | 0.00001     |
| 740           | 0.000005    |
| 760           | 0.000002    |
| 780           | 0.000001    |
| 800           | 25          |
| 820           | 25          |
| 840           | 25          |
| 860           | 25          |
| 880           | 25          |
| 900           | 25          |
| 920           | 25          |
| 940           | 25          |
| 960           | 25          |
| 980           | 25          |
| 1000          | 25          |
| 1020          | 25          |
| 1040          | 25          |
| 1060          | 25          |
| 1080          | 25          |
| 1100          | 25          |
| 1120          | 25          |
| 1140          | 25          |
| 1160          | 25          |
| 1180          | 25          |
| 1200          | 25          |
| 1220          | 25          |
| 1240          | 25          |
| 1260          | 25          |
| 1280          | 25          |
| 1300          | 25          |
| 1320          | 25          |
| 1340          | 25          |
| 1360          | 25          |
| 1380          | 25          |
| 1400          | 25          |
</details>

![](images/b1c6b5fe67530a473318b640dc1b144c3368733027c5e8d8f4be9e9a516a9852.jpg)

<details>
<summary>text_image</summary>

d
14 M	-10X
1.4 M	-4X
140 M
28 mM
</details>

![](images/09b89da73a4d14d02cce53da865fd2399f667e4e638bde4d47e94023c265297e.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Int. (a.u.) |
| ------------------ | ----------- |
| 2850               | 100         |
| 2900               | 1200        |
| 2950               | 100         |
| 3000               | 400         |
</details>

![](images/eb413f692d8fd653e899082d393a737ba3b371134b9287251ffdc5d26b6b91be.jpg)

<details>
<summary>line chart</summary>

| Concentration (M) | Int. (a.u.) |
| ----------------- | ----------- |
| 0.01              | 0.3         |
| 0.1               | 2.0         |
| 1                 | 20.0        |
| 10                | 150.0       |
</details>

Fig. 3 Hyperspectral SRS imaging of DMSO aqueous solution. The imaging was performed at the interface of a droplet of solution sandwiched in between coverslips. (a) SRS images of pure DMSO at selected Raman shift. Curves below the images show the profiles along the dashed line (yellow). (b) Spectral profile (square, red) of SRS imaging at the single pixel indicated with a red cross in (a). Solid line shows the spontaneous Raman profile. (c) Concentration dependence of the SRS signal. (d) SRS images of DMSO solution at various concentrations indicated in the figure at a Raman shift of 2911 cm-1.

It is worth mentioning that the spectral window of our spectral SRS microscope is not limited by the bandwidth of the femtosecond laser, but by the tuning range of the femtosecond laser. By tuning the wavelength of the Ti:S laser, we can easily extend the spectral window. For example, when we tuned the laser wavelength to 858 nm, we could easily get Raman spectrum of acetonitrile at CN stretching frequency around $2 2 5 0 ~ \mathrm { c m } ^ { - 1 }$ , which is also in very good agreement spontaneous Raman spectrum (Fig. 4). If the Ti:S wavelength is tuned beyond the spectral response window (>890 nm) of the GaAs detector, we can simply switch to another fast detector (such as InGaAs) as we have demonstrated previously. As a result, by tuning the wavelength of the Ti:S laser (tunable between 700 nm and 1100 nm), we should be able to scan from $0 ~ \mathrm { c m } ^ { \overline { { - 1 } } }$ up to $4 8 8 0 ~ \mathrm { c m ^ { - 1 } }$ , covering the entire fingerprint region. Alternatively, using an ultrashort femtosecond laser delivering broad bandwidth, it is even possible to cover the entire fingerprint region without the need of laser wavelength tuning.

![](images/c97d1237ca80f487b67b8af80acef4518dc4d475048f53e5fcfb1ccbd1f9a362.jpg)

<details>
<summary>line chart</summary>

| Distance (μm) | Int. (a.u.) |
| ------------- | ----------- |
| 0             | 0           |
| 50            | 0           |
| 100           | 0           |
| 150           | 0           |
| 200           | 0           |
| 2216          | 0           |
| 2252          | 0           |
| 2276          | 0           |
</details>

![](images/cb0ed24b18b7cdddfcd9ee931dcd5bb3c4bdd83057263a83f7d302b5dbea11d1.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Int. (a.u.) |
| ------------------ | ----------- |
| 2200               | 0           |
| 2250               | 700         |
| 2300               | 100         |
| 2350               | 0           |
</details>

lFig. 4 Hyperspectral SRS imaging of acetonitrile. The imaging was performed at the interface of a droplet of acetonitrile sandwiched in between coverslips. (a) SRS images of pure acetonitrile at selected Raman shift. Curves below the images show the profiles along the dashed line (yellow). (b) Spectral profile (square, red) of SRS imaging and spontaneous Raman spectrum (solid line, black).

To demonstrate hyperspectral SRS imaging of biological samples, we perform SRL imaging of PC3 human prostate cancer cells, shown in figure 5. Using MCR analysis, we decompose image contents of lipid (Figure 5a) and protein/nucleotide (Figure 5b), with the corresponding spectra given in figure 5d. Figure 5 shows that, by combining high-sensitivity hyperspectral SRS imaging enabled by the time-lens source and content decomposition enabled by MCR analysis, we can easily identify various compositions of biological tissues, as well as their spatial distribution. Thus, high-sensitivity hyperspectral SRS imaging and MCR analysis provide a unique capability to resolve the chemical and spatial heterogeneity inherent to a biological environment.

![](images/c3a73a561660901f7cb70263026bc3efe464d035f62c9a9c4ba9fd76b8fcf5c8.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing green-labeled cellular structures (no text or symbols visible)
</details>

![](images/4210290cc9838e08ca7e28fac36fbb5fa7dd076cb82a137da376aa9303e17d48.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological cell with red fluorescent markers (no text or symbols visible)
</details>

![](images/d287c32056aa7de9c6f6a316de3882a4850da317b94a0c4aa0d1d47e7bdcf049.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image of a cell with red and green stained nuclei (no text or symbols)
</details>

![](images/edf7d43f421efa293e092850523ab177ef3ed4e2a11f7cb1d2b35d77363933bd.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Lipid Int. (a.u.) | Protein/neucleotide Int. (a.u.) |
| ------------------ | ----------------- | -------------------------------- |
| 2800               | 0.1               | 0.0                              |
| 2850               | 0.4               | 0.1                              |
| 2900               | 0.6               | 0.1                              |
| 2950               | 0.3               | 0.2                              |
| 2975               | 0.1               | 0.1                              |
</details>

Fig. 5 Decomposition results of hyperspectral SRS imaging of PC3 cells. MCR analysis was performed to decompose the raw data to (a) lipid content and (b) protein/nucleotide content. The merged color image is shown in (c). Respective spectra are shown in (d), where green square indicates lipid and red dots protein/nucleotide. Scale bars: 10 µm.

## 4. CONCLUSION

We have experimentally demonstrated high-sensitivity hyperspectral SRS imaging. The Stokes pulse is generated through time-lens spectral broadening of a CW laser, and the pump is generated by spectral filtering and intra-pulse spectral scanning. Picosecond pulse width, hundreds of milliwatts of optical power at a wavelength of 1064 nm makes the time-lens source ideal for high-sensitivity CRS imaging. Hyperspectral SRS imaging combined with MCR analysis maps the chemical contents and their spatial distribution in complex biological environments such as cells. By fully exploiting the intrinsic advantages of SRS imaging, we expect this imaging modality will find wide applications in various fields such as biology, biomedical analysis and diagnosis, and chemical identification.

## REFERENCES

[1] J. X. Cheng, X. S. Xie (eds), Coherent Raman Scattering Microscopy, CRC Press, 2012.  
[2] A. Zumbusch, G. R. Holtom, and X. S. Xie, “Three-dimensional vibrational imaging by coherent anti-stokes Raman scattering”, Phys. Rev. Lett. 82, 4142-4145 (1999).  
[3] J.-X. Cheng and X. S. Xie, “Coherent anti-Stokes Raman scattering microscopy: instrumentation, theory, and applications”, J. Phys. Chem. B 108, 827-840 (2004).  
[4] C. W. Freudiger, W. Min, B. G. Saar, S. Lu, G. R. Holtom, C. He, J. C. Tsai, J. X. Kang, and X. S. Xie, “Labelfree biomedical imaging with high sensitivity by stimulated Raman scattering microscopy”, Science 322, 1857– 1861 (2008).  
[5] B. G. Saar, C. W. Freudiger, J. Reichman, C. M. Stanley, G. R. Holtom, and X. S. Xie, “Video-rate molecular imaging in vivo with stimulated Raman scattering” Science 330, 1368–1370 (2010).  
[6] D. Zhang, M. N. Slipchenko, and J.-X. Cheng, “Highly sensitive vibrational imaging by fs pulse stimulated Raman loss” J. Phys. Chem. Lett. 2, 1248–1253 (2011).  
[7] X. Zhang, M. B. Roeffaers, S. Basu, J. R. Daniele, D. Fu, C. W. Freudiger, G. R. Holtom, and X. S. Xie, “Label-free live-cell imaging of nucleic acids using stimulated Raman scattering microscopy”, ChemPhysChem 13, 1054–1059 (2012).  
[8] C. W. Freudiger, R. Pfannl, D. A. Orringer, B. G. Saar1, M. Ji, Q. Zeng, L. Ottoboni, W. Ying, C. Waeber, J. R. Sims, P. L. De Jager, O. Sagher, M. A. Philbert, X. Xu, S. Kesari, X. S. Xie, and G. S. Young, “Multicolored stain-free histopathology with coherent Raman imaging,” Lab. Invest. 92, 1492–1502 (2012).  
[9] D. Fu, F. K. Lu, X. Zhang, C. Freudiger, D. R. Pernik, G. Holtom, and X. S. Xie, “Quantitative chemical imaging with multiplex stimulated Raman scattering microscopy,” J. Am. Chem. Soc.134(8), 3623–3626 (2012).  
[10] K. Nose, Y. Ozeki, T. Kishi, K. Sumimura, N. Nishizawa, K. Fukui, Y. Kanematsu, and K. Itoh, “ Sensitivity enhancement of fiber-laser-based stimulated Raman scattering microscopy by collinear balanced detection technique,” Opt. Express 20, 13958-13965 (2012).  
[11] Y. Ozeki, W. Umemura, Y. Otsuka, S. Satoh, H. Hashi-moto, K. Sumimura, N. Nishizawa, K. Fukui, and K. Itoh, “ High-speed molecular spectral imaging of tissue with stimulated Raman scattering,” Nat. Photonics, 6, 845-851 (2012).  
[12] J. Moger, N. L. Garrett, D. Begley, L. Mihoreanu, A. La-latsa, M. V. Lozano, M. Mazza, A. Schatzlein, and I. Uchegbu, “Imaging cortical vasculature with stimulated Raman scattering and two-photon photothermal lensing microscopy,” J. Raman Spectrosc. 43, 668–674 (2012).  
[13] Y. Ozeki, W. Umemura, K. Sumimura, N. Nishizawa, K. Fukui, K. Itoh, “ Stimulated Raman hyperspectral imaging based on spectral filtering of broadband fiber,” Opt. Lett. 37, 431-433, 2012.  
[14] D. Zhang, P. Wang, M. N. Slipchenko, D. Ben Armotz, A. M. Weiner, and J.-X. Cheng, “Quantitative Vibrational Imaging by Pulse Shaping based Hyperspectral Stimulated Raman Scattering Microscopy and Multivariate Curve Resolution Analysis,” Anal. Chem. 85, 98-106 (2013)  
[15] K. Wang, C. W. Freudiger, J. H. Lee, B. G. Saar, X. S. Xie, and C. Xu, “Synchronized time-lens source for coherent Raman scattering microscopy,” Opt. Express 18, 24019 (2010).  
[16] K. Wang and C. Xu, “Fiber-delivered picosecond source for coherent Raman scattering imaging,” Opt. Lett. 36, 4233 (2011).  
[17] M. N. Slipchenko, R. A. Oglesbee, D. Zhang, W. Wu, and J.-X. Cheng. “Heterodyne detected nonlinear optical imaging in a lock-in free manner,” J. Biophoton. 5, 801-807 (2012).