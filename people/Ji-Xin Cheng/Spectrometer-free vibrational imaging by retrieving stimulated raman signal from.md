## O P T I C A L M I C R O S C O P Y

# Spectrometer-free vibrational imaging by retrieving stimulated Raman signal from highly scattered photons

2015 © The Authors, some rights reserved; exclusive licensee American Association fo the Advancement of Science. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC). 10.1126/sciadv.1500738

Chien-Sheng Liao,1 \* Pu Wang,1 \* Ping Wang,1 Junjie Li,2 Hyeon Jeong Lee,2 Gregory Eakins,3 Ji-Xin Cheng1,3,4,5,6†

In vivo vibrational spectroscopic imaging is inhibited by relatively slow spectral acquisition on the second scale and low photon collection efficiency for a highly scattering system. Recently developed multiplex coherent anti-Stokes Raman scattering and stimulated Raman scattering techniques have improved the spectral acquisition time down to microsecond scale. These methods using a spectrometer setting are not suitable for turbid systems in which nearly all photons are scattered. We demonstrate vibrational imaging by spatial frequency multiplexing of incident photons and single photodiode detection of a stimulated Raman spectrum within 60 ms. Compared to the spectrometer setting, our method improved the photon collection efficiency by two orders of magnitude for highly scattering specimens. We demonstrated in vivo imaging of vitamin E distribution on mouse skin and in situ imaging of human breast cancerous tissues. The reported work opens new opportunities for spectroscopic imaging in a surgical room and for development of deep-tissue Raman spectroscopy toward molecular level diagnosis.

## INTRODUCTION

In vivo vibrational spectroscopic imaging is opening a new window on cellular machinery by visualizing the spatiotemporal dynamics of target molecules or intracellular organelles. However, in vivo spectroscopic imaging is not a simple combination of spectroscopy and microscopy. Two grand challenges need to be overcome to realize spectroscopic imaging of a living system. One is decreasing the spectral acquisition time to microsecond scale per pixel to allow real-time imaging of a highly dynamic living system. The other is extracting the spectral information from highly scattered photons, for which the conventional dispersion approach is no longer efficient.

To increase the imaging speed, single- or multicolor coherent anti-Stokes Raman scattering (CARS) and stimulated Raman scattering (SRS) have been used to map known species (1–4), which have reached video rate speed (5, 6). To resolve overlapping Raman bands, various frame-by-frame hyperspectral imaging platforms by Raman shift sweeping (7–12) have been reported. In these methods, the CARS or SRS spectra are derived from the whole image stack acquired on millisecond to second scale, which is insufficient for imaging living systems. Broadband CARS (13–15) and multiplex SRS (16–18) have been developed to allow spectral acquisition at each pixel. Using a tuned amplifier array, microsecond-scale multiplex SRS imaging has been demonstrated (19). Yet, these methods using a spectrometer setting are not suitable for turbid systems in which nearly all photons are scattered.

The spectrometer, conceptually demonstrated by Newton in 1672 and first built by Fraunhofer in 1814, uses a prism or grating to disperse the collimated signal light on a detector array, which requires a slit to reject scattered photons to achieve the desired spectral resolution. For highly scattered photons, this scheme becomes inefficient because most of the photons are rejected by the slit. An elegant way to overcome this difficulty is to code the excitation photons, collect the photons with a single detector, and then decode the spectral signal. To this end, spectrally tailored SRS using pulse shaping technology has been developed to map desired chemicals (20). Three-color SRS by modulation-multiplexing at kilohertz rate has been demonstrated with an acousto-optical tunable filter (21). Coherent control (22) and frequency comb (23) techniques allowed acquisition of a CARS spectrum at each pixel. These two techniques required tens of milliseconds or longer for each spectrum, which is not sufficient for in vivo imaging purposes.

Here, we demonstrate a spectrometer-free, microsecond-scale spectroscopic imaging scheme by using a single large-area photodiode to collect highly scattered photons within tens of microseconds for each pixel. We first modulate the intensity $( I _ { \mathrm { p } } )$ o f a spectrally dispersed broadband pump beam with distinct megahertz frequencies (Fig. 1A). The broadband laser is then combined with a narrow-band Stokes beam (I ) and focused onto a sample. Through the stimulated Raman gain (SRG) process, $\Delta I = \sigma I _ { \mathrm { p } } I _ { \mathrm { S } } ,$ where s is the Raman scattering cross section, a Raman spectrum is coded into the intensity of the Stokes beam, with each Raman shift corresponding to a distinct modulation frequency. Then, a large-area detector collects the Stokes beam intensity in the time domain, and a Fourier transformation is performed to retrieve the SRG spectrum.

## RESULTS

## Quantification of photon collection efficiency by ray tracing simulation

We quantitatively evaluated the photon collection efficiency by ray tracing simulations in nonsequential mode using Zemax. In brief, $1 0 ^ { ^ { \circ } }$ rays were focused by a lens $( f = 2$ mm) into a 25-mm spot on the surface of a scattering medium. A Henyey-Greenstein scattering phase function was used to approximate the angular scattering dependence (24). The reflected rays were collected by the same lens and passed through a pinhole of 50-mm diameter on the focal plane (fig. S1A). The percentage

1 Weldon School of Biomedical Engineering, Purdue University, West Lafayette, IN 47907, USA. 2 Department of Biological Sciences, Purdue University, West Lafayette, IN 47907, USA. 3 Department of Chemistry, Purdue University, West Lafayette, IN 47907, USA. 4 Purdue University Center for Cancer Research, Purdue University, West Lafayette, IN 47907, USA. 5 Birck Nanotechnology Center, Purdue University, West Lafayette, IN 47907, USA. 6 School of Electrical and Computer Engineering, Purdue University, West Lafayette, IN 47907, USA. \*These authors contributed equally to this work. †Corresponding author. E-mail: jcheng@purdue.edu

A  
![](images/faeec82a50fec766db50f414a50c2673bfc43a5cc1885aa0eb0be7182eef8ba3.jpg)

<details>
<summary>line chart</summary>

| Modulation frequency (MHz) | Wavelength (μs) | Label             |
| -------------------------- | --------------- | ----------------- |
| 0                          | ~0              | ΔI_s(SRG)         |
| 1.5                        | ~0.8            | ΔI_p(SRL)         |
| 3                          | ~1.2            | ω_s               |
| Time trace                 | ~0.1            | Time trace        |
| FFT                        | ~0.6            | SRG spectrum      |
| Raman shift                | ~0.9            |                   |
</details>

B  
![](images/961d99a552bb2c8590a930fbf7c5f24b0e366b6ae8f67b14a4dec157ef076691.jpg)

<details>
<summary>text_image</summary>

2.25 MHz
ωp
Scan
PS
G Q P
Pump
Stokes
M SL
G Q P
D
SU
PD
P OBJ
Sample
ωs
</details>

C  
![](images/3b928e458d989cad01c58669795daa793e5d1bde4477508328668b2922cb07b3.jpg)

<details>
<summary>line chart</summary>

| Modulation frequency (Hz) | Int. (a.u.) |
| ------------------------- | ----------- |
| 1.5M                      | 1           |
| 1.6M                      | 2           |
| 1.7M                      | 3           |
| 1.8M                      | 4           |
| 1.9M                      | 5           |
| 2.0M                      | 6           |
| 2.1M                      | 7           |
| 2.2M                      | 8           |
| 2.3M                      | 9           |
| 2.4M                      | 10          |
| 2.5M                      | 11          |
| 2.6M                      | 12          |
| 2.7M                      | 13          |
| 2.8M                      | 14          |
| 2.9M                      | 15          |
| 3.0M                      | 16          |
</details>

D  
![](images/987e7afb70486f6c302d2ea93f8bc2c41a7e97dc2a2be09a4c22c560425b8eba.jpg)

<details>
<summary>line chart</summary>

| Modulation frequency (Hz) | Wavelength (nm) |
| ------------------------- | --------------- |
| 1.5M                      | 791             |
| 2.0M                      | 793             |
| 2.5M                      | 796             |
| 3.0M                      | 800             |
</details>

E  
![](images/bd26de785703d244185c371988c81889686ea1d42f4a40d723a92a38911bcc30.jpg)

<details>
<summary>line chart</summary>

| Modulation frequency (Hz) | Vrms/Hz^1/2 |
| ------------------------- | ----------- |
| 1.5M                      | 1           |
| 1.6M                      | 2           |
| 1.7M                      | 3           |
| 1.8M                      | 4           |
| 1.9M                      | 5           |
| 2.0M                      | 6           |
| 2.1M                      | 7           |
| 2.2M                      | 8           |
| 2.3M                      | 9           |
| 2.4M                      | 10          |
| 2.5M                      | 11          |
| 2.6M                      | 12          |
| 2.7M                      | 13          |
| 2.8M                      | 14          |
| 2.9M                      | 15          |
| 3.0M                      | 16          |
</details>

F  
![](images/ff9c2a5c61eb9580031cc8378d6cd85a410809b15e90753d293056f752444709.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | DMSO SRG | DMSO Raman |
| ------------------ | -------- | ---------- |
| 3050               | ~0       | ~0         |
| 3100               | ~0       | ~0         |
| 3200               | ~0       | ~0         |
| 3300               | ~0       | ~0         |
| 3400               | ~0       | ~0         |
| 3500               | ~0       | ~0         |
| 3600               | ~0       | ~0         |
| 3700               | ~0       | ~0         |
| 3800               | ~0       | ~0         |
| 3900               | ~0       | ~0         |
| 4000               | ~0       | ~0         |
| 4100               | ~0       | ~0         |
| 4200               | ~0       | ~0         |
| 4300               | ~0       | ~0         |
| 4400               | ~0       | ~0         |
| 4500               | ~0       | ~0         |
| 4600               | ~0       | ~0         |
| 4700               | ~0       | ~0         |
| 4800               | ~0       | ~0         |
| 4900               | ~0       | ~0         |
| 5000               | ~0       | ~0         |
| 5100               | ~0       | ~0         |
| 5200               | ~0       | ~0         |
| 5300               | ~0       | ~0         |
| 5400               | ~0       | ~0         |
| 5500               | ~0       | ~0         |
| 5600               | ~0       | ~0         |
| 5700               | ~0       | ~0         |
| 5800               | ~0       | ~0         |
| 5900               | ~0       | ~0         |
| 6000               | ~2e-6    | ~2e-6      |
| 6100               | ~2e-6    | ~2e-6      |
| 6200               | ~2e-6    | ~2e-6      |
| 6300               | ~2e-6    | ~2e-6      |
| 6400               | ~2e-6    | ~2e-6      |
| 6500               | ~2e-6    | ~2e-6      |
| 6600               | ~2e-6    | ~2e-6      |
| 6700               | ~2e-6    | ~2e-6      |
| 6800               | ~2e-6    | ~2e-6      |
| 6900               | ~2e-6    | ~2e-6      |
| 7000               | ~2e-6    | ~2e-6      |
| 7100               | ~2e-6    | ~2e-6      |
| 7200               | ~2e-6    | ~2e-6      |
| 7300               | ~2e-6    | ~2e-6      |
| 7400               | ~2e-6    | ~2e-6      |
| 7500               | ~2e-6    | ~2e-6      |
| 7600               | ~2e-6    | ~2e-6      |
| 7700               | ~2e-6    | ~2e-6      |
| 7800               | ~2e-6    | ~2e-6      |
| 7900               | ~2e-6    | ~2e-6      |
| 8000               | ~2e-6    | ~2e-6      |
| 8100               | ~2e-6    | ~2e-6      |
| 8200               | ~2e-6    | ~2e-6      |
| 8300               | ~2e-6    | ~2e-6      |
| 8400               | ~2e-6    | ~2e-6      |
| 8500               | ~2e-6    | ~2e-6      |
| 8600               | ~2e-6    | ~2e-6      |
| 8700               | ~2e-6    | ~2e-6      |
| 8800               | ~2e-6    | ~2e-6      |
| 8900               | ~2e-6    | ~2e-6      |
| 9000               | ~2e-6    | ~2e-6      |
| 9100               | ~2e-6    | ~2e-6      |
| 9200               | ~2e-6    | ~2e-6      |
| 9300               | ~2e-6    | ~2e-6      |
| 9400               | ~2e-6    | ~2e-6      |
| 9500               | ~2e-6    | ~2e-6      |
| 9600               | ~2e-6    | ~2e-6      |
| 9700               | ~2e-6    | ~2e-6      |
| 9800               | ~2e-6    | ~2e-6      |
| 9900               | ~2e-6    | ~2e-6      |
| 10000              | ~2e-6    | ~2e-6      |
</details>

Fig. 1. Stimulated Raman spectroscopic imaging by spatial frequency multiplexing and single photodiode detection. (A) Principle. Every color of the pump laser was modulated at a specific megahertz frequency. Through the SRG process, the modulation frequency transferred to the Stokes beam. A time trace was recorded, from which fast Fourier transform was performed to retrieve an SRG spectrum. (B) A lab-built multiplexmodulation SRS microscope. D, dichroic mirror; G, grating; SU, scanning unit; M, mirror; OBJ, objective; P, polarizing beam splitter; PD, photodiode; PS, polygon scanner; Q, quarter waveplate; SL, slit. (C) Modulated pump laser intensity as a function of modulation frequency. (D) Linear relation between wavelength and modulation frequency. (E) SRG intensity as a function of modulation frequency. (F) Retrieved SRG spectrum (circles) and spontaneous Raman spectrum (solid line).

of rays entering the spectrometer was 0.01% for a 2.0-mm-thick dermis tissue with scattering parameters measured by Tuchin et al. (25). In comparison, a detector $( 1 0 \times 1 0 ~ \mathrm { m m } ^ { 2 } )$ placed right after the lens collected many more reflected rays (fig. S1B). On the basis of our simulation result, the detection efficiency can be improved 200 times with a single detector to directly collect modulated photons and retrieve the spectral information through demodulation.

## Single-photodiode detection of SRS spectra by spatial frequency multiplexing

We used femtosecond pulse shaping technology to implement spatial frequency multiplexing at megahertz level. A pulse shaper narrowed down the spectral width of the Stokes beam to 15 cm−1 . The pump beam was dispersed vertically and then scanned horizontally by a polygon scanner onto a vertically aligned reflective pattern with 16 different densities, so that the spectrally dispersed laser source was modulated at 16 frequencies ranging from 1.5 to 3.0 MHz. After combining and focusing the pump and Stokes beams onto the sample, the Stokes beam, as the local oscillator, was collected by a large-area photodiode and amplified by a resonant circuit with a 2.25-MHz central frequency and a 1.5-MHz bandwidth. A data acquisition board recorded a 60-ms time trace of the SRG signal, and fast Fourier transformation demodulated the 16 frequency components to 16 Raman shifts. A schematic of our experimental setup is shown in Fig. 1B (detailed in Materials and Methods). Figure 1C shows the 16 distinct frequency components of the broadband pump beam, each with a 70-kHz bandwidth. The frequency difference between two adjacent components was 100 kHz, which prevented crosstalk between adjacent channels. Moreover, a frequency range of 1.5 to 3.0 MHz prevented crosstalk caused by harmonic frequencies. The pump laser intensity profile (Fig. 1C) was used for normalization of the SRG signal on each spectral channel. By relating the wavelengths of the pump laser to the modulation frequencies, a linear relationship was found between Raman shifts and modulation frequencies (Fig. 1D). We further acquired the SRG spectrum of 100% dimethyl sulfoxide (DMSO) solution. Figure 1E shows SRG intensity as a function of modulation frequency. After laser intensity normalization and Raman shift calibration, an SRG spectrum was retrieved, which reproduced the spontaneous Raman spectrum (Fig. 1F).

A  
![](images/6c735cf22f55414d0dfe0fed843bf3d353b18ecf8f2107ca023ad808755e8e81.jpg)

<details>
<summary>text_image</summary>

UPIa
10x
∞ / - P
Sample
Filter
Chicken
breast
VBIAS
OUT
Photodiode
</details>

B  
![](images/36609c87a26082b19b07393fdc8d6d0cb29f5bf0fa349657a61905f2529aa33b.jpg)

<details>
<summary>line chart</summary>

| Modulation frequency (Hz) | 1.6 cm chicken breast | 3.2 cm |
| ------------------------- | --------------------- | ------ |
| 1.5M                      | ~0                    | ~0     |
| 2.0M                      | ~0                    | ~0     |
| 2.5M                      | ~4×10⁻⁸               | ~0     |
| 3.0M                      | ~0                    | ~0     |
</details>

C

![](images/53b37ad349b7c6247ed80a98fda79682bdfa176e9260b7a4f236bb21051e8788.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | No chicken breast | 1.6 cm | 3.2 cm |
| ------------------ | ----------------- | ------ | ------ |
| 3050               | ~0                | ~0     | ~0     |
| 3000               | ~0.5×10⁻⁶         | ~0.2×10⁻⁶ | ~0.1×10⁻⁶ |
| 2950               | ~0                | ~0     | ~0     |
| 2900               | ~2×10⁻⁶           | ~1.5×10⁻⁶ | ~0.5×10⁻⁶ |
</details>

D  
![](images/dd79acea4683a0176e415ba2019f295f3f9e9e9670c35a3f6e0bd797c111465f.jpg)

<details>
<summary>line chart</summary>

| Modulation frequency (Hz) | Vrms/Hz^1/2 |
| ------------------------- | ----------- |
| 1.5M                      | ~0          |
| 2.0M                      | ~0          |
| 2.5M                      | ~7×10^-9    |
| 3.0M                      | ~0          |
</details>

E

![](images/5d24e25b9d8995b10062fd78bd2c42910f5344b8aae90678978684f8f9047f16.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Vrms/Hz¹/² |
| ------------------ | ---------- |
| 1550               | ~0         |
| 1500               | ~0         |
| 1450               | ~3×10⁻⁹    |
| 1400               | ~0         |
</details>

Fig. 2. Microsecond-scale acquisition of SRG spectra from completely diffused photons. (A) Experiment configuration. (B) SRG intensity of DMSO as a function of modulation frequency with 1.6- or 3.2-cm chicken breast tissues before photodiode. (C) Calibrated SRG spectra of DMSO. (D) SRG intensity of olive oil as a function of modulation frequency with 1.0-cm chicken breast tissues before photodiode. (E) Calibrated SRG spectra of olive oil. The integration time was 60 ms.

We note that collecting all dispersed photons by a single detector increases the level of shot noise shared among all spectral channels (26). To evaluate the noise level, we measured the SDs of 16 spectroscopic images as a function of laser power on the photodiode (fig. S2A). After normalizing the gain of each spectral channel (fig. S2B), we compared the noise levels with electronic noise and theoretical shot noise (fig. S2C). Under a laser power of 10 mW on the photodiode, the theoretical shot noise and the measured noise were $1 . 5 \dot { \times } 1 0 ^ { - 8 }$ and 1.9 × $\mathrm { 1 0 ^ { - 8 } \ V r m s / H z ^ { 1 / 2 } }$ , respectively, which exceeded the level of electronic noise $\left( 2 . 0 \times 1 0 ^ { - 9 } \mathrm { \ V r m s / H z } ^ { 1 / \dot { 2 } } \right)$ . We further determined our detection sensitivity by recording the $2 9 1 2 ~ \mathrm { { c m } ^ { - 1 } }$ Raman peak of diluted DMSO solutions. The SRG spectrum of 1.0% DMSO produced a signal level of $2 . 5 \times 1 0 ^ { - 8 } \mathrm { V r m s } / \mathrm { H z } ^ { 1 } / 2 ( \mathrm { f i g . } \mathrm { S 2 D } )$ , corresponding to a detection sensitivity of $3 . 2 \times 1 0 ^ { - 6 }$ dI/I modulation depth at 60-ms time constant.

## Acquisition of stimulated Raman spectra from diffuse photons

To show that our technique is capable of extracting a Raman spectrum from highly diffuse photons, we focused the pump and Stokes light with a 10× objective into a cuvette filled with a specimen (Fig. 2A). After passing through the filter, the Stokes laser beam propagated through a chicken breast tissue and was received by a photodiode with 60-ms integration time. We first recorded the SRG spectra of DMSO in the spectral window of C-H stretching vibration 2800 to $3 0 0 0 ~ \mathrm { { c m } ^ { - 1 } ) }$ . The raw modulation spectra of DMSO reached a signal-to-noise ratio (SNR) of \~60 and \~6 for 1.6- and 3.2-cm chicken breast tissues, respectively (Fig. 2B). The calibrated spectra are shown in Fig. 2C. We then recorded the SRG spectra of olive oil in the C-H bending vibration $( \sim 1 4 5 0 \ c m ^ { - 1 } )$ . With 1.0-cm chicken breast tissues before the photodiode, the raw modulation spectrum showed an SNR of \~3 (Fig. 2D), and the calibrated SRG spectrum matched the spontaneous Raman spectrum (Fig. 2E). These results collectively demonstrated microsecond-scale spectrum extraction from diffuse photons in both C-H stretching and fingerprint vibration regions.

## Following drug diffusion through mouse skin tissue in vivo

Our technique allowed in vivo monitoring of drug delivery into a mouse skin. Topical drug delivery is traditionally analyzed by tape-stripping or microdialysis techniques. Single-color CARS and SRS microscopy have been used to map deuterated drug in the skin using the isolated C-D stretching vibration (27, 28). Here, we demonstrate in vivo mapping of vitamin E, in the form of a-tocopherol, on the skin of a live mouse (Fig. 3A). Vitamin E is a fat-soluble antioxidant widely used for the maintenance of healthy skin. This molecule exhibits a spectral profile overlapping with the skin tissue in the C-H stretching vibration (Fig. 3B). To distinguish vitamin E from the skin tissue, we acquired an SRG spectrum at each pixel and performed multivariate curve resolution (MCR) analysis of 40,000 SRG spectra. The SRG image was decomposed into vitamin E (in pink), lipid (in yellow), and protein (in green) as shown in Fig. 3C. Their concentration distributions in the epidermis layer (\~20 mm below the surface) and around the sebaceous gland (\~50 mm below the surface) are shown in Fig. 3D. Before the treatment, only lipid and protein components were found. After 5 min of treatment, vitamin E molecules were found (in pink) in the epidermis layer and enriched in the sebaceous gland (Fig. 3D). In contrast, selec tive imaging of vitamin E molecules was impossible with single-color SRS microscopy (Fig. 3E). Together, these data showed that our technique is capable of mapping a specific chemical in a spectrally overlapped tissue in vivo.

A  
![](images/0e389ad77828bf0e62006d5ca0d2e7973e565805b711743aab810b9c8ecddf05.jpg)

<details>
<summary>text_image</summary>

CQ=0.17
t=1.2
00
00
Isoflurane
←
</details>

B  
![](images/f1fff4c63c828402abe0666911b740f190f09d5117dc7c541a95b64441f06584.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Int. (a.u.) - α-Tocopherol (vitamin E) | Int. (a.u.) - Olive oil (CH₂) | Int. (a.u.) - BSA (CH₃) |
| ------------------ | -------------------------------------- | ------------------------------ | ------------------------ |
| 2800               | ~0.1                                   | ~0.1                           | ~0.1                     |
| 2850               | ~0.6                                   | ~1.0                           | ~0.2                     |
| 2900               | ~0.9                                   | ~0.8                           | ~0.4                     |
| 2950               | ~1.0                                   | ~0.8                           | ~0.5                     |
| 3000               | ~0.1                                   | ~0.1                           | ~0.1                     |
</details>

C  
![](images/ba777cdb96adc10a39c49e5ad520c4b39a5e838cf53a0b67470a9dda7bdc3229.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | α-Tocopherol (vitamin E) | Lipid | Protein |
| ------------------ | ------------------------ | ----- | ------- |
| 2800               | 0.0                      | 0.0   | 0.0     |
| 2850               | 0.4                      | 0.6   | 0.1     |
| 2900               | 0.5                      | 0.4   | 0.3     |
| 2950               | 0.3                      | 0.3   | 0.2     |
| 3000               | 0.0                      | 0.0   | 0.0     |
</details>

D  
Multiplex-modulation (2800-3000 cm-1)  
![](images/070397ad3e4f0f411f099349b67eb39592e2e7988c965672257f363f32be8abc.jpg)

<details>
<summary>text_image</summary>

Z = 20 µm
50 µm
Before treatment
100 µm
After treatment
Z = 20 µm
50 µm
</details>

![](images/7ced40ba1b4b21327b66a7f11ccda8d552f69d4759c06a4cd141450a30448a92.jpg)

<details>
<summary>text_image</summary>

Single color (2911 cm⁻¹)
Z = 20 µm
50 µm
Before treatment
Z = 20 µm
50 µm
After treatment
</details>

Fig. 3. In vivo monitoring of vitamin E distribution on mouse skin. (A) Experiment configuration. The nude mouse was anesthetized with isoflurane. (B) Spontaneous Raman spectra of vitamin E, olive oil (rich in CH2), and bovine serum albumin (rich in CH3). (C) MCR output spectra of three components assigned to lipid, protein, and vitamin E. (D) MCR concentration maps of lipid (in yellow) and protein (in green) before and after the treatment. (E) SRG images at $2 9 1 1 ~ \mathsf { c m } ^ { - 1 }$ . The pixel dwell time was $6 0 \mu \mathsf { s } .$ Scale bar, $1 0 0 \mu \mathrm { m } .$ .

## Spectroscopic imaging of human breast cancerous tissue in situ

We further demonstrated the capability of our scheme for imaging human breast cancer and stroma in situ. Current medical diagnosis of malignancies relies on in vitro hematoxylin and eosin (H&E) staining and histological examination of biopsies. Two-color SRS allowed selective imaging of lipids and proteins in brain tissue on the basis of $\mathrm { C H } _ { 2 }$ vibration $( 2 8 4 5 \mathrm { c m } ^ { - 1 } )$ and $\mathrm { C H } _ { 3 }$ vibration $( 2 9 3 0 { \mathrm { c m } } ^ { - 1 } )$ (29). Broadband CARS (15) and wavelength-sweeping SRS microscopy (9) were used to map the chemical composition of thin tissue sections. Here, we demonstrate epidetected stimulated Raman spectroscopic imaging of intact human breast cancerous tissues (Fig. 4A). SRG images at $2 9 0 8 ~ \mathrm { { c m } ^ { - 1 } }$ showed the morphology of the cancerous tissue at three different locations (Fig. 4B). MCR analysis decomposed the SRG spectra into three components (Fig. 4C). The spectral profile with a peak around $2 8 5 0 ~ \mathrm { c m } ^ { - 1 }$ was assigned to the adipose breast tissue. The peak at $2 9 4 0 \mathrm { c m } ^ { - 1 }$ was assigned to fibrosis, and the 2960 cm−1 peak was assigned to cell nuclei. The corresponding MCR concentration maps (Fig. 4D) closely matched the histological examination of sliced tissues of the same area (Fig. 4E).

A  
![](images/765bb5a37cd6135fcf9dffc88c99b6d5ef3fe2260970d80cd5655941de126f31.jpg)

<details>
<summary>natural_image</summary>

Close-up of a robotic arm pressing a small, textured object on a metal surface, labeled A, B, C (no text or symbols on the object itself)
</details>

B  
![](images/c89223a6b6c04febdf94a56967e58ed77262993f2f4580229cb435927a27cce8.jpg)

<details>
<summary>text_image</summary>

Location A
2908 cm⁻¹
</details>

Location B  
![](images/1a87352c2bd840a68f3a3fffa121a7c861c45a2ee7efc03610cc821e7fdf156f.jpg)

<details>
<summary>natural_image</summary>

Abstract grayscale texture with diagonal striations and soft gradients (no text or symbols)
</details>

Location C  
![](images/86d9fe2ce69e2d86c3f691e907be18410e0dd61fc2e455bfd6a983c3683647b8.jpg)

<details>
<summary>natural_image</summary>

Grayscale abstract texture with no discernible text, symbols, or structured elements
</details>

C  
![](images/3b478d0fdbaff59c0ec13510d22c0313111bf4798b26094435cd655986874c6f.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Fat    | Fibrosis | Nuclei |
| ------------------ | ------ | -------- | ------ |
| 2800               | 0.0    | 0.0      | 0.0    |
| 2850               | 0.4    | 0.1      | 0.05   |
| 2900               | 0.55   | 0.2      | 0.1    |
| 2950               | 0.5    | 0.3      | 0.15   |
| 3000               | 0.1    | 0.1      | 0.1    |
</details>

D  
![](images/e0dcc40aa7a9663e9d6498bf3f414d48cad3c4784dc79e1376dce301dfb6f116.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of yellow fluorescent cells labeled MCR (no text or symbols within the image content)
</details>

![](images/48097408c36e00c1a5a92471fd39d0b87623a9ec339ab0f4eee27bbbb678996e.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing green and magenta cellular structures with a yellow fluorescent region (no text or symbols)
</details>

![](images/90048db59eb5de6e66a9afdd2da38490434a5cf04e8c12509faae76b9465ed85.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing green fluorescent structures with scattered pink specks (no text or symbols)
</details>

E  
![](images/27ff733afc3caf4a52757bf57f54aabc398fffccc897c9bc707d4defd923278e.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular structures with hexagonal patterns, scale bar indicating 100 μm (no text or symbols within the image content)
</details>

![](images/1ad3ac2746d7c49b13a42c2d16d9a3aceca99a42cfccae0de719bb8d4861328a.jpg)

<details>
<summary>natural_image</summary>

Microscopic tissue section showing fibrous and cellular structures (no text or labels visible)
</details>

![](images/f6c8431fac44cc8e889ed279cacbe44eb5ad17800861463651593767867329ef.jpg)

<details>
<summary>natural_image</summary>

Microscopic tissue sample showing pink-stained cellular structures with purple nuclei (no text or labels visible)
</details>

Fig. 4. In situ mapping of human patient breast cancer and stroma. (A) Digital picture of a 5-mm-thick human breast cancerous tissue. (B) SRG images of locations indicated in (A) at 2908 $\mathsf { c m } ^ { - 1 } .$ (C) MCR output spectra of three components assigned to fat, fibrosis, and cell nuclei. (D) MCR concentration maps of fat (in yellow), fibrosis (in green), and cell nuclei (in pink). (E) Histological analysis (H&E staining) of the same tissue. The pixel dwell time was 600 ms. Scale bar, 100 mm.

## DISCUSSION

The current work demonstrated a platform for acquisition of a Raman spectrum from highly scattered photons at 60-ms integration time. Our method is conceptually different from Fourier-transform Raman spectroscopy, which sends the collimated signal light to a Michelson interferometer and retrieves the spectrum encoded in the Fourier domain (30). A greater potential of our technology can be realized by placing a ring-shaped detector between the focusing lens and the specimen (6). In this way, up to 40% of diffuse photons can be collected to generate a vibrational spectrum in a spectrometer-free manner. In another direction toward minimally invasive molecular level diagnosis, the combination of our spatial frequency multiplexing scheme with techniques that enable focusing of light through a turbid tissue, such as time reversal of ultrasound-encoded light (31) or digital phase conjugation with dynamic wavefront shaping (32), promises a new avenue to implement deep-tissue vibrational spectroscopy for minimally invasive in vivo diagnosis.

It is interesting to compare the detection sensitivity between our approach and single-color excitation SRS. For single-color SRS microscopy, the detection sensitivity of a 50 mM retinol or 5 mM methanol solution was reported by Freudiger et al. (33) with 1-min integration time. The 5 mM concentration limit for cholesterol reported by Freudiger et al. was achieved at 1-s integration time. Here, we achieved a 141 mM DMSO solution sensitivity at 60-ms integration time (fig. S2D). At 1-s integration time, our SNR would be improved 129 times in theory, which corresponds to a detection sensitivity of 1.1 mM. Thus, the detection sensitivity of our setup is on the same level as single-color SRS. This sensitivity is partly attributed to shot-noise limited detection and partly to spectral analysis of the whole data set.

It is important to note that acquiring a spectrum at each pixel allows for separation of the SRS signal from the unwanted cross-phase modulation. Because cross-phase modulation is largely wavelengthindependent, by using spectral analysis such as MCR, we can separate the Raman signal from this nonresonant background.

Our imaging platform can be applied to monitor the spatiotemporal dynamics of target molecules in nontransparent living tissues from which the signal photons are completely scattered. In these systems, spectral acquisition by the conventional dispersion approach would lead to low photon collection efficiency. Because the animal motion and molecular diffusion are on the second scale, a microsecond-scale spectral acquisition speed is required to collect a spectroscopic image within seconds. Our technique meets this requirement by recording a 60-ms signal time trace from highly scattered photons and retrieving a spectrum that is encoded in the modulation frequency domain. We expect broad applications including in vivo assessment of local drug bioavailability in human skin. Although we focused on epi-detection, our technique is also applicable to forward detection of scattering samples. We performed spectroscopic imaging of live Caenorhabditis elegans and showed its capability to distinguish lipid- and protein-rich compartments (fig. S3).

Our technology opens an avenue toward in vivo intraoperative histological imaging. Current intraoperative tools for cancerous tissue assessment, including cytological examination, frozen section analysis, ultrasound, and radio-frequency spectroscopy (34–38), either are timeconsuming or lack sufficient tumor specificity. Recently reported Raman spectroscopy technology for intraoperative tumor residual detection has shown the ability to differentiate cancer cells from normal brain tissue with a sensitivity of 93% and a specificity of 91% by point spectral measurement within 1 s (39). Our technique reported here improved the acquisition speed of a vibrational spectrum to microsecond scale, thus allowing real-time spectroscopic imaging. With the aid of the MCR analysis, we further generated chemical images of bulk human cancerous tissue, which reproduced the H&E staining and histological examination results. Future development of a mobile intraoperative vibrational spectroscopic imaging tool would enable generation of histological data from intact tissues in vivo to assess residual diseases in a surgical room.

The spectral coverage of our technology can be improved. The num ber of spectral channels (N) is determined as $N = ( f _ { \operatorname* { m a x } } - f _ { \operatorname* { m i n } } ) / \Delta f ,$ where $f _ { \mathrm { m a x } }$ is the maximum modulation frequency, f is the minimum modulation frequency, and Df is the bandwidth of each spectral channel. The spectrum acquisition time (T) is determined by T = 2/Df. Thematically, by modulating an ultrafast pulse from 20 to 40 MHz with 70-kHz bandwidth, we will be able to generate 285 spectral channels within 29 ms. Moreover, with a 10-fs pulse, we will be able to cover the entire fingerprint region with a spectral window of 1470 cm−1 .

In summary, our technique improved the Raman spectral acquisition speed to microsecond scale and at the same time allowed the retrieval of a vibrational spectrum from highly scattered photons. Using this approach, we demonstrated in situ imaging of cancerous human breast tissue and showed results that reproduced H&E staining and histological examination. Collectively, our technique has the potential of pushing Raman spectroscopy from a single point measurement tool toward in vivo clinical imaging applications.

## MATERIALS AND METHODS

## Spatial frequency multiplexing on an SRS microscope

A tunable 80-MHz pulsed laser (InSight, Spectra Physics) provided two synchronized outputs. The tunable pump beam provided up to 1.0-W power, 120-fs pulse duration, and a tuning range from 680 to 1300 nm. The fixed 1040-nm beam with 0.5-W power and \~200-fs pulse width served as the Stokes beam. The Stokes beam was sent to a diffraction grating (1200 grooves/mm), and a slit on the Fourier plane narrowed the bandwidth. The full width at half maximum was measured to be 3 ps by an autocorrelator, and the power was 100 mW. A broadband pump beam covering 180 cm−1 at 800 nm was dispersed by a diffraction grating (1200 grooves/mm) in the x direction and scanned by a 17-kHz polygon scanner (Lincoln Laser) in the y direction on a photolithography mask, which modulated the reflected intensities of each wavelength at 16 different frequencies ranging from 1.5 to 3.0 MHz. The photolithography mask was designed with 16 one-dimensional arrays of points in the x direction. Within each array, there were 88 to 176 periods in the y direction. These features were written by blue chrome, which exhibits an optical density of 3 and low reflectivity (less than 5%) at 800 nm, on a 4 inch × 4 inch × 0.060 inch piece of soda lime. We placed a mirror (E03, Thorlabs) after the photomask to reflect the modulated 800-nm laser beam. Therefore, the modulation depth was close to 95%. A similar scheme was used to modulate the beam in the kilohertz range in a previous study (26). For imaging applications, the modulated pump and Stokes beams were sent to a lab-built microscope. A 25× objective (XLPlan N 25×, Olympus) was used to focus the light on the sample. The pump and Stokes laser powers on the sample were 30 and 50 mW, respectively. The SRG signal was then collected by the same objective, and a polarizing beam splitter was used to reflect the polarization-scrambled SRG signal to a photodiode (s3994-01, Hamamatsu). This epi-detection scheme collected 3% of photons from the sample. For the forward-detected imaging scheme, the Stokes beam was collected by an oil condenser and sent to the photodiode. The induced photocurrent was amplified through a resonant amplifier circuit, which used the parasitic capacitance of the photodiode to create a central resonance frequency of 2.25 MHz and a bandwidth of 1.5 MHz. The amplified signal was sent to a high-speed data acquisition board with up to 140 MHz sampling rate (ATS 460, AlazarTech). The data acquisition was synchronized with the galvo mirrors in the lab-built microscope and the polygon scanner in the pulse shaper by LabVIEW. A 60-ms time trace of SRG signal with a sampling rate of 10 MHz was recorded for each pixel. Fast Fourier transformation was performed in LabVIEW to retrieve the SRG spectra in the modulation frequency domain. For each spectral channel, we integrated over the 70-kHz bandwidth. After the laser power normalization and Raman shift calibration, an SRG spectrum was retrieved. For an image with 200 × 200 pixels, it took 2.4 s to record a total of 40,000 time traces. The data transfer from the data acquisition board to the computer required \~3 s. The following Fourier transformation at each pixel and image reconstruction by LabVIEW required 1 min.

## MCR analysis

MCR and alternative least squares fitting were used to decompose the SRG spectral images into chemical maps of major components in a specimen (11). MCR is a bilinear model (40) capable of decomposing a measured spectral data set D into concentration profiles and spectra of chemical components, represented by matrices C and $\mathbf { S ^ { T } } , \mathbf { D } = \mathbf { \dot { C } } { \cdot } \mathbf { S ^ { T } } + \mathbf { E } .$ Here, T is the transpose of matrix of S. E is the residual matrix or experimental error. The inputs to MCR are the data set D and the reference spectra of each component. S contains the output spectra of all fitted components. The output concentration of a chemical component at each pixel is expressed as a percentage relative to the intensity of the MCR-optimized spectrum. Given an initial estimate of pure spectra from either principal components analysis or prior knowledge, an alternating least squares algorithm calculates C and S iteratively until the results optimally fit the data matrix D. Nonnegativity on both concentration maps and spectral profiles is applied as a constraint during the alternating least squares iteration. To reduce ambiguity associated with MCR decomposition, a data augmentation matrix composed of repeating reference spectra can be added to the spectral data set D if needed. The enhanced weight on pure reference spectra ensures that the MCR algorithm selectively recovers concentration profiles for corresponding Raman bands from experimental data set D.

## Mouse tissue preparation

The protocol for this animal study (no. 1111000114) was approved by the Purdue Animal Care and Use Committee. A male athymic nude mouse (6 weeks old) under inhalation anesthesia with isoflurane was used for in vivo imaging.

## Human tissue materials and examination

The breast tumor samples were excised from a patient diagnosed with invasive ductal carcinoma and then fixed in 10% buffered formalin. The SRS imaging experiments followed an Institutional Review Board protocol (no. 0905008097) approved by Purdue University. After SRS imaging, the tissues were sectioned and stained with H&E for histological examination in the Purdue Histology and Phenotyping Laboratory.

## SUPPLEMENTARY MATERIALS

Supplementary material for this article is available at http://advances.sciencemag.org/cgi/ content/full/1/9/e1500738/DC1  
Vibrational spectroscopic imaging of live C. elegans  
Fig. S1. Comparison of photon collection efficiency by a spectrometer to that by a single detector.  
Fig. S2. Detection sensitivity of spatial frequency multiplexing SRS microscopy.  
Fig. S3. Spectroscopic imaging of a live wild-type C. elegans.  
References (41–44)

## REFERENCES AND NOTES

1. L. Wei, F. Hu, Y. Shen, Z. Chen, Y. Yu, C.-C. Lin, M. C. Wang, W. Min, Live-cell imaging of alkyne tagged small biomolecules by stimulated Raman scattering. Nat. Methods 11, 410–412 (2014).

2. H. J. Lee, W. D. Zhang, D. L. Zhang, Y. Yang, B. Liu, E. L. Barker, K. K. Buhman, L. V. Slipchenko, M. Dai, J.-X. Cheng, Assessing cholesterol storage in live cells and C. elegans by stimulated Raman scattering imaging of phenyl-diyne cholesterol. Sci. Rep. 5, 7930 (2015).

3. S. Hong, T. Chen, Y. Zhu, A. Li, Y. Huang, X. Chen, Live-cell stimulated Raman scattering imaging of alkyne-tagged biomolecules. Angew. Chem. Int. Ed. 53, 5827–5831 (2014).

4. L. Kong, M. Ji, G. R. Holtom, D. Fu, C. W. Freudiger, X. S. Xie, Multicolor stimulated Raman scattering microscopy with a rapidly tunable optical parametric oscillator. Opt. Lett. 38, 145–147 (2013).

5. C. L. Evans, E. O. Potma, M. Puoris’haag, D. Côté, C. P. Lin, X. S. Xie, Chemical imaging of tissue in vivo with video-rate coherent anti-Stokes Raman scattering microscopy. Proc. Natl. Acad. Sci. U.S.A. 102, 16807–16812 (2005).

6. B. G. Saar, C. W. Freudiger, J. Reichman, C. M. Stanley, G. R. Holtom, X. S. Xie, Video-rate molecular imaging in vivo with stimulated Raman scattering. Science 330, 1368–1370 (2010).

7. C.-Y. Lin, J. L. Suhalim, C. L. Nien, M. D. Miljković, M. Diem, J. V. Jester, E. O. Potma, Picosecond spectral coherent anti-Stokes Raman scattering imaging with principal component analysis of meibomian glands. J. Biomed. Opt. 16, 021104 (2011).

8. E. T. Garbacik, J. L. Herek, C. Otto, H. L. Offerhaus, Rapid identification of heterogeneous mixture components with hyperspectral coherent anti-Stokes Raman scattering imaging. J. Raman Spectrosc. 43, 651–655 (2012).

9. Y. Ozeki, W. Umemura, Y. Otsuka, S. Satoh, H. Hashimoto, K. Sumimura, N. Nishizawa, K. Fukui, K. Itoh, High-speed molecular spectral imaging of tissue with stimulated Raman scattering. Nat. Photonics 6, 844–851 (2012).

10. D. Fu, G. Holtom, C. Freudiger, X. Zhang, X. S. Xie, Hyperspectral imaging with stimulated Raman scattering by chirped femtosecond lasers. J. Phys. Chem. B 117, 4634–4640 (2012).

11. D. Zhang, P. Wang, M. N. Slipchenko, D. Ben-Amotz, A. M. Weiner, J.-X. Cheng, Quantitative vibrational imaging by hyperspectral stimulated Raman scattering microscopy and multivariate curve resolution analysis. Anal. Chem. 85, 98–106 (2013).

12. F. Masia, A. Glen, P. Stephens, P. Borri, W. Langbein, Quantitative chemical imaging and unsupervised analysis using hyperspectral coherent anti-Stokes Raman scattering microscopy. Anal. Chem. 85, 10820–10828 (2013).

13. M. Müller, J. M. Schins, Imaging the thermodynamic state of lipid membranes with multiplex CARS microscopy. J. Phys. Chem. B 106, 3715–3723 (2002).  
14. T. W. Kee, M. T. Cicerone, Simple approach to one-laser, broadband coherent anti-Stokes Raman scattering microscopy. Opt. Lett. 29, 2701–2703 (2004).  
15. C. H. Camp Jr., Y. J. Lee, J. M. Heddleston, C. M. Hartshorn, A. R. H. Walker, J. N. Rich, J. D. Lathia, M. T. Cicerone, High-speed coherent Raman fingerprint imaging of biological tissues. Nat. Photonics 8, 627–634 (2014).  
16. W. Rock, M. Bonn, S. H. Parekh, Near shot-noise limited hyperspectral stimulated Raman scattering spectroscopy using low energy lasers and a fast CMOS array. Opt. Express 21, 15113–15120 (2013).  
17. K. Seto, Y. Okuda, E. Tokunaga, T. Kobayashi, Development of a multiplex stimulated Ra man microscope for spectral imaging through multi-channel lock-in detection. Rev. Sci. Instrum. 84, 083705 (2013).  
18. B. Marx, L. Czerwinski, R. Light, M. Somekh, P. Gilch, Multichannel detectors for femtosecond stimulated Raman microscopy—Ideal and real ones. J. Raman Spectrosc. 45, 521–527 (2014).  
19. C.-S. Liao, M. N. Slipchenko, P. Wang, J. Li, S.-Y. Lee, R. A. Oglesbee, J.-X. Cheng, Micro second scale vibrational spectroscopic imaging by multiplex stimulated Raman scattering microscopy. Light Sci. Appl. 4, e265 (2015).  
20. C. W. Freudiger, W. Min, G. R. Holtom, B. W. Xu, M. Dantus, X. S. Xie, Highly specific label free molecular imaging with spectrally tailored excitation-stimulated Raman scattering (STE-SRS) microscopy. Nat. Photonics 5, 103–109 (2011).  
21. D. Fu, F.-K. Lu, X. Zhang, C. Freudiger, D. R. Pernik, G. Holtom, X. S. Xie, Quantitative chem ical imaging with multiplex stimulated Raman scattering microscopy. J. Am. Chem. Soc. 134, 3623–3626 (2012).  
22. N. Dudovich, D. Oron, Y. Silberberg, Single-pulse coherently controlled nonlinear Raman spectroscopy and microscopy. Nature 418, 512–514 (2002).  
23. T. Ideguchi, S. Holzner, B. Bernhardt, G. Guelachvili, N. Picqué, T. W. Hänsch, Coherent Ra man spectro-imaging with laser frequency combs. Nature 502, 355–358 (2013).  
24. W.-F. Cheong, S. A. Prahl, A. J. Welch, A review of the optical-properties of biological tis sues. IEEE J. Quantum Elect. 26, 2166–2185 (1990).  
25. V. V. Tuchin, S. R. Utz, I. V. Yaroslavsky, Tissue optics, light-distribution, and spectroscopy. Opt. Eng. 33, 3178–3188 (1994).  
26. S. S. Howard, A. Straub, N. G. Horton, D. Kobat, C. Xu, Frequency-multiplexed in vivo mul tiphoton phosphorescence lifetime microscopy. Nat. Photonics 7, 33–37 (2013).  
27. B. G. Saar, L. R. Contreras-Rojas, X. S. Xie, R. H. Guy, Imaging drug delivery to skin with stimulated Raman scattering microscopy. Mol. Pharm. 8, 969–975 (2011).  
28. X. Chen, S. Grégoire, F. Formanek, J.-B. Galey, H. Rigneault, Quantitative 3D molecular cuta neous absorption in human skin using label free nonlinear microscopy. J. Control. Release 200, 78–86 (2015).  
29. M. Ji, D. A. Orringer, C. W. Freudiger, S. Ramkissoon, X. Liu, D. Lau, A. J. Golby, I. Norton, M. Hayashi, N. Y. R. Agar, G. S. Young, C. Spino, S. Santagata, S. Camelo-Piragua, K. L. Ligon, O. Sagher, X. S. Xie, Rapid, label-free detection of brain tumors with stimulated Raman scattering microscopy. Sci. Transl. Med. 5, 201ra119 (2013).  
30. T. Hirschfeld, B. Chase, FT-Raman spectroscopy: Development and justification. Appl. Spec trosc. 40, 133–137 (1986).  
31. X. Xu, H. Liu, L. V. Wang, Time-reversed ultrasonically encoded optical focusing into scattering media. Nat. Photonics 5, 154–157 (2011).  
32. Y. M. Wang, B. Judkewitz, C. A. DiMarzio, C. Yang, Deep-tissue focal fluorescence imaging with digitally time-reversed ultrasound-encoded light. Nat. Commun. 3, 928 (2012).  
33. C. W. Freudiger, W. Min, B. G. Saar, S. Lu, G. R. Holtom, C. He, J. C. Tsai, J. X. Kang, X. S. Xie, Label-free biomedical imaging with high sensitivity by stimulated Raman scattering microscopy. Science 322, 1857–1861 (2008).  
34. V. S. Klimberg, K. C. Westbrook, S. Korourian, Use of touch preps for diagnosis and evalua tions of surgical margins in breast cancer. Ann. Surg. Oncol. 5, 220–226 (1998).  
35. E. K. Valdes, S. K. Boolbol, I. Ali, S. M. Feldman, J.-M. Cohen, Intraoperative touch prepara tion cytology for margin assessment in breast-conservation surgery: Does it work for lob ular carcinoma? Ann. Surg. Oncol. 14, 2940–2945 (2007).  
36. T. P. Olson, J. Harter, A. Muñoz, D. M. Mahvi, T. M. Breslin, Frozen section analysis for in traoperative margin assessment during breast-conserving surgery results in low rates of re-excision and local recurrence. Ann. Surg. Oncol. 14, 2953–2960 (2007).  
37. T. Karni, I. Pappo, J. Sandbank, O. Lavon, V. Kent, R. Spector, S. Morgenstern, S. Lelcuk, A device for real-time, intraoperative margin assessment in breast-conservation surgery. Am. J. Surg. 194, 467–473 (2007).  
38. T. E. Doyle, R. E. Factor, C. L. Ellefson, K. M. Sorensen, B. J. Ambrose, J. B. Goodrich, V. P. Hart, S. C. Jensen, H. Patel, L. A. Neumayer, High-frequency ultrasound for intraoperative margin assessments in breast conservation surgery: A feasibility study. BMC Cancer 11, 444 (2011).  
39. M. Jermyn, K. Mok, J. Mercier, J. Desroches, J. Pichette, K. Saint-Arnaud, L. Bernstein, M.-C. Guiot, K. Petrecca, F. Leblond, Intraoperative brain cancer detection with Raman spectroscopy in humans. Sci. Transl. Med. 7, 274ra19 (2015).  
40. A. de Juan, R. Tauler, Multivariate curve resolution (MCR) from 2000: Progress in concepts and applications. Crit. Rev. Anal. Chem. 36, 163–176 (2006).  
41. T. Hellerer, C. Axäng, C. Brackmann, P. Hillertz, M. Pilon, A. Enejder, Monitoring of lipid storage in Caenorhabditis elegans using coherent anti-Stokes Raman scattering (CARS) microscopy. Proc. Natl. Acad. Sci. U.S.A. 104, 14658–14663 (2007).  
42. M. C. Wang, W. Min, C. W. Freudiger, G. Ruvkun, X. S. Xie, RNAi screening for fat regulatory genes with SRS microscopy. Nat. Methods 8, 135–138 (2011).  
43. P. Wang, B. Liu, D. Zhang, M. Y. Belew, H. A. Tissenbaum, J.-X. Cheng, Imaging lipid metabolism in live Caenorhabditis elegans using fingerprint vibrations. Angew. Chem. Int. Ed. 53, 11787–11792 (2014).  
44. E. J. O’Rourke, A. A. Soukas, C. E. Carr, G. Ruvkun, C. elegans major fats are stored in vesicles distinct from lysosome-related organelles. Cell Metab. 10, 430–435 (2009).

Acknowledgments: We thank A. Weiner for helpful discussions. Funding: This work was supported by the Keck Foundation and NIH grant GM104681 to J.-X.C. Author contributions: C.-S.L. and Pu W.

designed the experiment. G.E. designed the electronic circuits. C.-S.L., Pu W., Ping W., J.L., and H.J.L. performed the experiments. C.-S.L. carried out the data analysis. J.-X.C. conceived the study and provided overall guidance. All authors discussed the results and contributed to the writing of the manuscript. Competing interests: J.-X.C. has a financial interest in Vibonix Inc. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and Supplementary Materials and will be made available by the authors upon request.

Submitted 7 June 2015 Accepted 28 July 2015 Published 30 October 2015 10.1126/sciadv.1500738

Citation: C.-S. Liao, P. Wang, P. Wang, J. Li, H. J. Lee, G. Eakins, J.-X. Cheng, Spectrometer-free vibrational imaging by retrieving stimulated Raman signal from highly scattered photons. Sci. Adv. 1, e1500738 (2015).

This article is publisher under a Creative Commons license. The specific license under which this article is published is noted on the first page.

For articles published under CC BY licenses, you may freely distribute, adapt, or reuse the article, including for commercial purposes, provided you give proper attribution.

For articles published under CC BY-NC licenses, you may distribute, adapt, or reuse the article for non-commerical purposes. Commercial use requires prior permission from the American Association for the Advancement of Science (AAAS). You may request permission by clicking here.

The following resources related to this article are available online at http://advances.sciencemag.org. (This information is current as of November 2, 2015):

Updated information and services, including high-resolution figures, can be found in the online version of this article at: http://advances.sciencemag.org/content/1/9/e1500738.full.html

Supporting Online Material can be found at: http://advances.sciencemag.org/content/suppl/2015/10/27/1.9.e1500738.DC1.html

This article cites 44 articles,6 of which you can be accessed free: http://advances.sciencemag.org/content/1/9/e1500738#BIBL