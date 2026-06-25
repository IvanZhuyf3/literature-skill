# Electronic Preresonance Stimulated Raman Scattering Spectromicroscopy Using Multiple-Plate Continuum

Published as part of The Journal of Physical Chemistry virtual special issue “Hiro-o Hamaguchi Festschrift”.

Guan-Jie Huang, Cheng-Wei Li, Po-Yi Lee, Jia-Xuan Su, Kuo-Chuan Chao, Li-An Chu, Ann-Shyn Chiang, Ji-Xin Cheng, Bo-Han Chen, Chih-Hsuan Lu, Shi-Wei Chu,\* and Shang-Da Yang

![](images/527c0e891c5ef15307256672ee918d14e1148aff01a11c2070d27314828d6ad1.jpg)

Cite This: J. Phys. Chem. B 2023, 127, 6896−6902

![](images/75083e27827a6ab36ba4d5607a775b7ebc701f6facbdfd78fac898819ab5961d.jpg)

Read Online

## ACCESS

![](images/1bf17c60d1bb575a5e789b7a69919cd82d7f1d8bafb98c7504beca2d7be1bcf2.jpg)

Metrics & More

![](images/dd126f3aa7636f6e38d4480b0145b253c7cb060d312636cb5361289b9c523fd3.jpg)

Article Recommendations

ABSTRACT: Stimulated Raman scattering (SRS) spectromicroscopy is a powerful technique that enables label-free detection of chemical bonds with high specificity. However, the low Raman cross section due to typical far-electronic resonance excitation seriously restricts the sensitivity and undermines its application to bio-imaging. To address this bottleneck, the electronic preresonance (EPR) SRS technique has been developed to enhance the Raman signals by shifting the excitation frequency toward the molecular absorption. A fundamental weakness of the previous demonstration is the lack of dual-wavelength tunability, making EPR-SRS only applicable to a limited number of species in the proof-of-concept experiment. Here, we demonstrate the EPR-SRS

spectromicroscopy using a multiple-plate continuum (MPC) light source able to examine a single vibration mode with independently adjustable pump and Stokes wavelengths. In our experiments, the $\mathrm { C } { = } \mathrm { C }$ vibration mode of Alexa 635 is interrogated by continuously scanning the pump-to-absorption frequency detuning throughout the entire EPR region enabled by MPC. The results exhibit 150-fold SRS signal enhancement and good agreement with the Albrecht A-term preresonance model. Signal enhancement is also observed in EPR-SRS images of the whole Drosophila brain stained with Alexa 635. With the improved sensitivity and potential to implement hyperspectral measurement, we envision that MPC-EPR-SRS spectromicroscopy can bring the Raman techniques closer to a routine in bio-imaging.

![](images/780ddd9a71b10fc04cce8b33ba5da79f8500bac30e7af5ffaa16bd29e3f634e1.jpg)

<details>
<summary>line chart</summary>

| λ Range              | Absorption |
|----------------------|----------|
| Γ                    | Low      |
| Δv: Frequency detuning | High     |
| Ω: Raman shift       | Medium   |
| EPR region           | 2Γ < ω₀ - ωpump < 6Γ |
</details>

## 1. INTRODUCTION

Fluorescence microscopy has long been a popular modality in biomedical applications because of its high sensitivity and low background.1 However, the chemical specificity comes from labeling at the cost of phototoxicity and perturbation of the intrinsic behaviors, which are a great concern for functional imaging. Crosstalk between different fluorescence channels also limits the number of distinguishable molecules to 2−5.2,3 $2 \mathrm { - } 5 . ^ { 2 , 3 }$ Raman scattering, on the other hand, provides label-free chemical contrast. However, spontaneous Raman scattering is an inherently weak process, where the cross section is typically on the order of 10−29 $1 0 ^ { ^ { \bullet } - 2 9 } \ \mathrm { c m } ^ { - 2 } . ^ { 4 }$ The low-efficiency results in a long integration time, seriously restricting its usefulness in imaging applications. In addition, Raman signals can be overwhelmed by either much stronger fluorescence signals or detector overflow near the excitation wavelength due to insufficient filter extinction.

To overcome these problems, stimulated Raman scattering (SRS) microscopy using two mutually coherent pump and Stokes ultrashort pulses has been developed to amplify Raman signals by seven orders of magnitude5,6 and is free of fluorescence or overflow artifact.6−10 Nevertheless, typical SRS operated at a far-EPR condition (i.e., both pump frequency $\omega _ { \mathrm { p u m p } }$ and Stokes frequency $\omega _ { \mathrm { S t o k e s } }$ are far away from the molecular absorption $\omega _ { 0 } )$ is still much weaker than the fluorescence, making it still a secondary modality in bioimaging.

Simultaneous electronic and vibrational resonance is a well known strategy to boost the Raman signal by shifting ωpump $\omega _ { \mathrm { p u m p } }$ toward $\omega _ { 0 } . ^ { 1 1 - 1 4 }$ In reality, electronic resonance $( \omega _ { \mathrm { p u m p } } \approx \stackrel { \cdot } { \omega } _ { 0 } )$ will induce a large nonlinear background and smear out the vibrational Raman features of interest.3,15 This motivates the access to the electronic preresonance (EPR) region, which seeks the balance between SRS signal enhancement and

Received: April 20, 2023

Revised: July 2, 2023

Published: July 26, 2023

![](images/afd0b382aa10377d05d86e40ff4083e4fb90acd705dcaa8d98259b6767ccd2c0.jpg)

![](images/3862a8e3cc44044936ca08f721e087013ee8901f8facdabfdb9d182c4a14d99b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Light Sources"] --> B["1030 nm"]
  B --> C["1st stage MPC"]
  C --> D["CM"]
  D --> E["2nd stage MPC"]
  E --> F["NDBS"]
  F --> G["BPF"]
  G --> H["1030 nm"]
  H --> I["SPF1"]
  I --> J["TCF1"]
  J --> K["AOM"]
  K --> L["Stokes"]
  L --> M["DBS1"]
  M --> N["DBS2"]
  N --> O["Pump"]
  O --> P["DBS3"]
  P --> Q["Microscope"]
  Q --> R["10x"]
  R --> S["SPF2"]
  S --> T["or"]
  T --> U["SPF3"]
  U --> V["PD"]
  V --> W["EBF LNA"]
  W --> X["LIA"]
  X --> Y["1.02 mV 0.00 mV"]
  Y --> Z["Pump + (modulated) Stokes\nStokes + (modulated) 1030 nm"]
```
</details>

Figure 1. Apparatus of the MPC-EPR-SRS spectromicroscope. MPC: multiple-plate continuum; CM: chirp mirror; NDBS: notch dichroic beam splitter; BPF: bandpass filter; SPF#: short-pass filter; DBS#: dichroic beam splitter; TCF#: tunable color filter; AOM: acousto-optic modulator; PD: photodetector; EBF: electronic bandpass filter; LNA: low noise amplifier; LIA: lock-in amplifier.

nonlinear background penalty. Wei et al. have reported that EPR is most effective when $\omega _ { \mathrm { p u m p } }$ is detuned from $\omega _ { 0 }$ by $_ { 2 - 6 }$ times the absorption bandwidth Γ.16 A series of recent works have successfully demonstrated SRS signal enhancement by means of either selecting a specific chemical dye whose $\omega _ { 0 }$ happens to be close to the available $\omega _ { \mathrm { p u m p } } , \stackrel { 3 , 5 , 1 6 - 1 8 } { }$ or adjusting $\omega _ { \mathrm { p u m p } }$ via second harmonic generation 19 or supercontinuum generation20,21 in support of the target dyes. However, the ability to address different molecules, Raman signatures, and pump-to-absorption detuning $( \Delta \nu \ : = \ : \omega _ { 0 } \ : - \ : \omega _ { \mathrm { p u m p } } )$ at will, which is essential for real imaging applications, has not been achieved yet.

Here, we present EPR-SRS spectromicroscopy driven by a multiple-plate continuum (MPC) light source.2 2−24 A strategic advantage of such a light source is the ability to independently adjust $\omega _ { \mathrm { p u m p } }$ and $\omega _ { \mathrm { S t o k e s } }$ with high spectral energy density, which enables EPR-SRS interrogation over the entire Raman active region $( 0 { - } 4 0 0 0 ~ \mathrm { c m } ^ { - 1 } )$ with variable pump-toabsorption detuning as long as the absorption peak lies in the visible to NIR. In the proof-of-concept experiments, we interrogated the $\mathrm { C } { = } \mathrm { C }$ vibration mode of Alexa 635 by continuously scanning the pump-to-absorption frequency detuning Δν from 2.2 to $5 . 6 \Gamma$ , nearly covering the entire EPR region. Up to 150-fold SRS signal enhancement was observed when $\Delta \nu = 2 . 2 \Gamma$ , and the trend agreed well with the Albrecht A-term preresonance theoretical model. However, a trade-off between enhancement and fluctuation of the SRS signal was observed, and the optimal signal-to-noise ratio (SNR) occurred when $\Delta \nu \approx 4 \Gamma$ . Finally, SRS images of the whole Drosophila brain stained with Alexa 635 were acquired at $\Delta \nu = 2 . 2 , 3 . 9 _ { \cdot }$ , and 5.6Γ, consistent with the trends observed in the measurements of the Alexa 635 solution.

## 2. EXPERIMENTAL METHODS

2.1. MPC-EPR-SRS Spectromicroscope. Figure 1 illustrates the setup of the MPC-EPR-SRS spectromicroscope. A Yb:KGW laser system (Carbide, Light Conversion) with 1030 nm center wavelength, 190 fs duration, 20 W average power, and 200 kHz repetition rate served as the front-end light source for supercontinuum generation. The beam was focused by a concave mirror into the first MPC stage consisting of six strategically positioned 200 μm-thick quartz plates aligned at Brewster’s angle for spectral broadening based on the optical Kerr effect.22−24 The pulses were temporally compressed to ${ \sim } 5 5$ fs with chirped mirrors. The second MPC stage was used to further broaden the spectral bandwidth beyond one octave. Figure 2 shows the supercontinuum spectrum after the second

![](images/1df50adc10ff79624c8973c5529dafb121aaf99004abf5d4dc7fcb1a61e2ed1d.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Normalized Intensity (a.u.) |
| --------------- | --------------------------- |
| 600             | ~10⁻³                       |
| 700             | ~10⁻²                       |
| 800             | ~10⁻²                       |
| 900             | ~10⁻¹                       |
| 1000            | ~10⁰                        |
| 1100            | ~10⁻¹                       |
| 1200            | ~10⁻²                       |
| 1300            | ~10⁻³                       |
</details>

Figure 2. Supercontinuum spectrum generated by two MPC stages.

MPC stage measured by visible to near-infrared spectrometers (Flame, Ocean Optics, and BTC264P, B&W Tek). The supercontinuum first passed through a 1040 nm notch dichroic beam splitter NDBS (NFD01-1040, Semrock) to reflect the laser wavelength near 1040 nm. A super-narrow bandpass filter BPF (1030.7-3 OD5, Alluxa) was utilized to select a narrowband 1030 nm beam as the long-wavelength “Stokes” in the far-EPR SRS experiment. To prevent the optics from damage, a 945 nm short-pass filter SPF1 (FF01-945/SP-25, Semrock) was used to filter out the brightest spectral components around 1030 nm. The average power was approximately 8 W and the spectral energy density was calculated to be around 1 $\mathrm { { n J / c \hat { m } ^ { - 1 } } }$ , which is sufficient for Raman imaging. The MPC supercontinuum was then split into the pump and Stokes paths with an 800 or 830 nm dichroic beam splitter DBS1 (FF801-Di01-25 × 36 or Di02-R830-25 ×

36, Semrock). The Stokes and pump excitation wavelengths were adjusted by a linear variable bandpass filter TCF1 (LVFBP, Delta) and a pair of linear variable long- and shortpass filters TCF2 (3G LVLWP and LVSWP, Delta). The bandwidths of TCF1 (Stokes) and TCF2 (pump) are 13 (200 $\mathsf { c m } ^ { - 1 } )$ and 5 nm $( 1 0 0 ~ \mathrm { { c m } ^ { - 1 } ) }$ , respectively. The average powers of both beams after TCF1 and TCF2 are in the order of tens of mW. Thereby, we could interrogate any desired Raman shift with a continuously tunable pump-Stokes wavelength pair. An acousto-optic modulator (MT110-B50A1.5-IR-HK, AA Opto Electronic) was implemented to modulate the intensity of the Stokes or 1030 nm beamline at ∼100 kHz. In the case of far-EPR excitation, the 1030 nm and Stokes beams were combined with a 930 nm dichroic beam splitter DBS2 (FF930-SDi01-25 × 36, Semrock) while the pump beam was blocked. Otherwise, the pump and Stokes beams were collinearly combined with another identical 800 or 830 nm dichroic beam splitter DBS3 while the 1030 nm was blocked. The spatially and temporally overlapped dual-color beams (Stokes and 1030/pump) were directed into a commercial upright microscope (Axio Examiner.Z1, Zeiss). A 10× objective (Plan-Apochromat 10x/0.45 M27, Zeiss) was used for optical excitation on samples. The forward beams were collected in transmission with an identical 10× objective lens, where a 785 or 842 nm short-pass filter SPF2 (BSP01-785R-25 and FF01-842/SP-25, Semrock) was placed to reject the Stokes beam. In the case of far-EPR excitation, a 1030 nm beam was filtered out with a 945 nm short-pass filter SPF3 (FF01-945/SP-25, Semrock). The transmitted beam was measured with a silicon photodetector (DET100A2, Thorlabs). The output photocurrent of the photodetector was electronically prefiltered by a 100 kHz bandpass filter EBF (KR3317-SMA, KR Electronics) to suppress low-frequency noise and preamplified with a lownoise amplifier LNA (SA-230F5, NF Corporation) to improve the SNR. It was then sent into a lock-in amplifier (SR844, Stanford Research) phase-locked with the electric signal driving the acousto-optic modulator to demodulate the SRS signals. For all spectroscopic measurements, the lock-in time constant was set to 300 ms, and 200 data points were used for averaging. When capturing the SRS images, the lock-in time constant was set to 100 μs to coordinate with the longest pixel dwell time (∼180 μs) of the commercial microscope. The lateral resolution of the system characterized by scanning an SRS signal profile across the interface between the DMSO solution and the air is about 1 μm. The Drosophila brain image was obtained by averaging 40 frames to attain enough SNR.

2.2. Sample Preparation. A total of 1 mg of Alexa 635 (Streptavidin, Alexa Fluor 635 conjugate, Thermo Fisher Scientific) powder was dissolved in 1 mL of phosphatebuffered saline (PBS, Thermo Fisher Scientific). The solution was then sealed with coverslips with two 80 μm ring spacers in between before conducting the spectroscopic measurement. Dve labeling Drosophila was anesthetized on ice for 20 min and dissected in phosphate-buffered saline (PBS. pH 7.2). After the brain was dissected and all the surrounding trachea had been removed, the fly brain was transferred to a 24-well plate containing 4% paraformaldehyde in PBS for 30 min immediately, put in a vacuum for 10 min, and left in a vacuum for 3 min to expel air from the internal tracheal system; this process was repeated for 4 times. Fixed tissues were then permeabilized and blocked in PBS containing 2% Triton X-100 and 10% normal goat serum (NGS; Vector Laboratories, CA) at $4 ~ ^ { \circ } \mathrm { C }$ overnight. Dye labeling was carried out in PBS containing 1% Triton X-100, 0.25% NGS, and Alexa Fluor streptavidin 635 (1:500 dilution) (Invitrogen) for 1 day at room temperature.

## 3. RESULTS AND DISCUSSION

3.1. MPC-EPR-SRS Theoretical Consideration. To examine the EPR effects of a specific vibration mode in SRS measurement, both pump and Stokes frequencies need to be adjusted so that they fulfill the two conditions of EPR-SRS. First, the pump-to-Stokes frequency difference $( \omega _ { \mathrm { p u m p } } \ \mathrm { ~ - ~ }$ $\omega _ { \mathrm { S t o k e s } } )$ must match the desired Raman shift Ω. Second, the pump-to-absorption frequency detuning $( \Delta \nu = \omega _ { 0 } - \omega _ { \mathrm { p u m p } } )$ has to be $_ { 2 - 6 }$ times the absorption bandwidth Γ to achieve noticeable Raman signal enhancement by EPR and adequate signal-to-background ratio $\left( { \cal S } / { \tt B } > 5 \right) . ^ { 1 6 }$ The octave-spanning MPC spectrum is a promising light source to meet these requirements since it supports dual-wavelength tunability as depicted in Figure 3.

(a)  
![](images/11a1e6c0cbe3c0a45aee61e115e49f76dbd0108d004cdd7edc138cf5f5bf64b3.jpg)

<details>
<summary>text_image</summary>

virtual state
far-resonance SRS
Δν
μwrop
μwrokes
MPC-EPR-SRS
Ω
</details>

(b)  
![](images/b5c8608e6d8e4f7b41ccf4f8be962c3e29c9d877edc39d81a5283d8804d9c3bc.jpg)

<details>
<summary>line chart</summary>

| λ Range | Absorption (molecular absorption spectrum) | Absorption (MPC spectrum) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 2Γ < ω₀ - ωₚₘₚ < 6Γ | Δν (peak) | 0 |
| 2Γ < ω₀ - ωₚₘₚ < 6Γ | Ω (peak) | 0 |
| 2Γ < ω₀ - ωₚₘₚ < 6Γ | ... | 0 |
| 2Γ < ω₀ - ωₚₘₚ < 6Γ | ... | 0 |
| 2Γ < ω₀ - ωₚₘₚ < 6Γ | ... | 0 |
| 2Γ < ω₀ - ωₚₘₚ < 6Γ | ... | 0 |
| 2Γ > ω₀ | 0 | 0 |
| > 2Γ | 0 | 0 |
</details>

Figure 3. Schematic of dual-wavelength tunability of MPC-EPR-SRS spectroscopy. (a) Energy diagram of (left panel) far-EPR and (right panel) electronic preresonance stimulated Raman scattering probing via MPC. $\omega _ { \mathrm { p u m p } }$ and $\omega _ { \mathrm { S t o k e s } } \mathrm { : }$ the frequencies of pump and Stokes beams; Ω: Raman shift. (b) Dual-wavelength tunability of MPC enables flexible control of the frequency detuning Δν defined by the energy difference between the molecular absorption peak and the pump excitation. The EPR region lies during 2−6 times the absorption bandwidth Γ.

Figure 3a shows the energy diagram of the SRS process with different combinations of $\omega _ { \mathrm { p u m p } }$ and $\omega _ { \mathrm { S t o k e s } } .$ . An overwhelming majority of SRS experiments is performed by utilizing a fixed Stokes wavelength (e.g., 1030 nm) and tunable pump frequencies well below the molecular absorption peak (Δν $\gg \bar { \Gamma } _ { i }$ , refer to left panel, Figure 3a).3,9,19,25 These traditional light sources with single wavelength tunability can only operate in the less sensitive far-EPR mode. In contrast, the MPC light source covering from the visible to near-infrared enables independent adjustment of both $\omega _ { \mathrm { p u m p } }$ and $\omega _ { \mathrm { S t o k e s } }$ through tunable color filters and thus can flexibly manipulate the frequency detuning $\Delta \nu$ while interrogating a specific Raman shift Ω (right panel, Figure 3a; Figure 3b). By properly positioning the pump frequency $\omega _ { \mathrm { p u m p } }$ below the molecular absorption peak (purple curve in Figure 3b) by 2−6 times the absorption bandwidth Γ, highly sensitive EPR detection can be achieved.

(a)  
![](images/ca5211d884b25031a833d1a39b2ae8cf4cdfcff212bfb62aec281f1d13333e86.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Absorption (a.u.) |
| --------------- | ----------------- |
| 450             | ~0.0              |
| 500             | ~0.1              |
| 550             | ~0.3              |
| 600             | ~0.5              |
| 650             | 1.0               |
| 700             | ~0.1              |
| 750             | ~0.0              |
| 800             | ~0.0              |
</details>

(b)  
![](images/1514ba17187fce283995fe01ef617a460fdb5ee57941be21cce8583cd5bca975.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Measured Intensity (a.u.) | Fitted Curve | SNR |
| --------------- | ------------------------- | ------------ | --- |
| 900             | ~0                        | ~0           | ~40 |
| 984             | ~0                        | ~0           | ~150 |
| 917             | ~10                       | ~10          | ~100 |
| 852             | ~20                       | ~20          | ~30 |
| 788             | ~150                      | ~60          | ~10 |
</details>

Figure 4. MPC-EPR-SRS spectroscopy of Alexa 635. (a) Absorption spectrum of Alexa 635 obtained by experimental measurement (black solid) and pseudo-Voigt fitting (red dashed), from which the absorption bandwidth Γ is determined as 794 cm−1 . (b) SRS intensities (filled squares) of the $\bar { \mathrm { C } } { = } \mathrm { C }$ bond $( \Omega = 1 \dot { 6 } 0 0 \ c m ^ { - 1 } )$ relative to the far-EPR condition when the frequency detuning $\left( \Delta \nu = \omega _ { 0 } - \omega _ { \mathrm { p u m p } } \right)$ varies between 2.2 and $5 . 6 \Gamma .$ . The red dashed curve represents the Albert A-term preresonance fitting. SNR spectral response (open circles) is maximal when $\Delta \nu \approx 4 \Gamma .$ The spectral region denoted by a blue (green) background indicates the measurements where the cutoff wavelength of DBS1 was chosen as 800 nm $\left( { \bar { 8 } } 3 0 - \operatorname { n m } \right)$ . The far-EPR condition is denoted by a red background.

(a)  
5.6T : 884 nm (pump) + 1030 nm (Stokes)  
![](images/d3107c352deaf86c41bd582c5812c8683cf91814ee88be84a7006923cb1ddaa5.jpg)

<details>
<summary>scatterplot</summary>

| x    | y    |
| ---- | ---- |
| 100  | 250  |
| 200  | 350  |
| 300  | 450  |
| 400  | 300  |
| 500  | 200  |
</details>

(b)  
3.9T : 790 nm (pump) + 904 nm (Stokes)  
![](images/b0d39634fb446ebb555419189d7c3999b7af767cedc55065cf0d65d889c63a02.jpg)

<details>
<summary>scatterplot</summary>

| x    | y    |
| ---- | ---- |
| 100  | 50   |
| 200  | 100  |
| 300  | 150  |
| 400  | 200  |
| 500  | 250  |
</details>

(c)  
2.27 : 713 nm (pump) + 805 nm (Stokes)  
![](images/9dba062d8006d8cbe755f42fe609e8c8b1420930decefe69d95dd9e522b28f80.jpg)

<details>
<summary>heatmap</summary>

| X Range | Y Range | Value |
|---------|---------|-------|
| 100-500 | 50-500  | -10   |
| 100-500 | 100-150 | -8    |
| 100-150 | 150-200 | -6    |
| 100-200 | 200-250 | -4    |
| 100-250 | 250-300 | -2    |
| 100-300 | 300-350 | 0     |
| 100-350 | 350-400 | 2     |
| 100-400 | 400-450 | 4     |
| 100-450 | 450-500 | 6     |
| 100-500 | 500-550 | 8     |
</details>

Figure 5. MPC-EPR-SRS images of the Alexa-staining Drosophila brain measured at (a) far-EPR $( \Delta \nu = 5 . 6 \Gamma ) , ( \mathrm { b } )$ moderate EPR $\left( \Delta \nu = 3 . 9 \Gamma \right)$ , and deep-EPR $\left( \Delta \nu = 2 . 2 \Gamma \right)$ regions, respectively. The pump and Stokes powers at the sample are {0.68 mW, 0.83 mW}, {0.56 mW, 1.22 mW}, and {0.71 mW, 1.72 mW} in the three cases, respectively.

Theoretically, the Albrecht A-term expression describes the approximated frequency-dependent Raman cross section for 12,16,26,27

$$
\sigma_ {R} \left(\omega_ {\text {pump}}\right) = K \omega_ {\text {pump}} \left(\omega_ {\text {pump}} - \Omega\right) ^ {3} \left[ \frac {\omega_ {0} ^ {2} + \omega_ {\text {pump}} ^ {2}}{\left(\omega_ {0} ^ {2} - \omega_ {\text {pump}} ^ {2}\right) ^ {2}} \right] ^ {2} \tag {1}
$$

where K is the frequency-independent factor, Ω is the vibrational frequency (Raman shift), and $\omega _ { 0 }$ refers to the frequency of molecular absorption peak.

3.2. Experiment Demonstration of MPC-EPR-SRS Signal Enhancement. In the following, we present a proofof-concept demonstration of MPC-EPR-SRS spectroscopy, which was carried out in a continuous frequency detuning mode via MPC by interrogating the $\mathrm { C } { = } \mathrm { C }$ vibration mode $\left( \Omega = 1 6 0 0 ~ \mathrm { c m } ^ { - 1 } \right)$ on a commercial Alexa 635 fluorescent dye with continuously adjustable pump/Stokes wavelength combinations arising from an MPC light source. To determine the frequency detuning range, we first measured the absorption spectrum of Alexa 635 with a halogen lamp. Using pseudo-Voigt function fitting gives the peak absorption wavelength of $\lambda _ { \mathrm { p e a k } } { = } ~ 6 3 3$ nm $( \tilde { \omega _ { 0 } = } 1 5 , 7 9 8 ^ { \mathrm { { - } } } ~ \mathrm { c m ^ { - 1 } } )$ and the absorption bandwidth of $\Gamma { = 7 9 4 \ \mathrm { c m } ^ { - 1 } \ \mathrm { ( F i g u r e \ 4 a ) } . ^ { 2 8 } }$ Next, we performed MPC-EPR-SRS measurements with pump wavelength varying from 713 to 884 nm, while the Stokes wavelength was adjusted accordingly to match the 1600 $\mathrm { c m } ^ { - 1 }$ Raman shift of $\mathrm { C } { = } \mathrm { C }$ vibration mode. In these conditions, the pump-to-absorption detuning ranges from 2.2 to 5.6Γ, nearly covering the entire EPR region. Taking the long-wavelength excitation (884/1030 nm) as the far-EPR reference $( \Delta \nu = 5 . 6 \Gamma )$ ), more than 150-fold SRS signal enhancement (after normalization with respect to power, bandwidth, responsivity curve of the photodetector, and objective transmission of excitation pulses) is observed when operating in the deep-EPR region $\left( \Delta \nu \ : = \ : 2 . 2 \Gamma \right)$ . The measured data points (filled squares, Figure 4b) are well-fitted by $\mathrm { e q } \ 1 ,$ confirming the integrity of the EPR operation. However, the signal enhancement is accompanied by the increased fluctuation due to the energy transfer to the molecules. SNR. defined by the ratio of mean to standard deviation of 200 data points, is optimal in the moderate EPR region $( \Delta \nu \approx 4 \Gamma $ , open circles, Figure 4b).

3.3. MPC-EPR-SRS Bioimaging. To demonstrate the potential of MPC-EPR-SRS microscopy, we acquired images of Drosophila brain samples stained with Alexa 635 dye under far-EPR and EPR modes. Figure 5a displays the result when pump/Stokes wavelengths are 884/1030 nm, corresponding to $\mathrm { { \dot { \Omega } } = \mathrm { { 1 6 0 0 } ~ c m ^ { - 1 } ~ ( C = \mathrm { { \dot { C } } } } }$ vibration mode) and $\Delta \nu = 5 . 6 \Gamma$ (far EPR). By blue-shifting the excitation wavelengths to 790/904 $\left( \Delta \nu = 3 . 9 \Gamma \right)$ and 713/805 nm $\left( \Delta \nu = 2 . 2 \Gamma \right)$ , the Raman signal level in the brain region is enhanced by 4.2 and 7.3 times (after the same normalization conducted in the solution measurement) [Figure 5b,c]. The corresponding enhancement factors are substantially lower than those (14.2 and 151) obtained in the Alexa 635 solution measurements [filled squares, Figure 4b]. The reduced Raman signal enhancement in the biological samples mainly originates from the fact that both Alexa dyes and intrinsic biological molecules (e.g., DNA or proteins) in the Drosophila brain contribute to SRS signals but in different ways. In our experiment, only Alexa dyes exhibited EPR enhancement, while the near-infrared pump remained largely detuned from the ultraviolet absorption of the intrinsic biological molecules. The overall EPR enhancement in a biological sample could be significantly “diluted” as long as the concentration of Alexa dyes is relatively lower than that of the intrinsic biological molecules. In contrast, the brain images and Alexa 635 solution exhibited similar SNR values, which are {13,42,20} (brain images) and {19,42,8} (solution) at $\Delta \nu =$ {5.6Γ, 3.9Γ, 2.2Γ}, respectively.

Both results endorse that the trade-off between signal and noise is best achieved in the moderate EPR region (Δν ≈ 4Γ). Given that the SRS signal reduction is irrelevant to the biological sample (but some technical issues of the micro scope), EPR-SRS is promising in high-sensitivity bio-imaging.

## 4. DISCUSSION AND CONCLUSIONS

In addition to the ability to address the entire Raman active region reported in our previous literature,21 this study highlights another unique advantage of intense supercontinuum light source like MPC in implementing high-sensitivity EPR-SRS spectromicroscopy. By deploying tunable color filters in both pump and Stokes beam paths, the two excitation pulses can be independently selected from the octave-spanning spectrum (600−1300 nm) to meet the requirements of EPR detection $( \Omega = \omega _ { \mathrm { p u m p } } - \omega _ { \mathrm { S t o k e s } }$ and $\omega _ { 0 } - \omega _ { \mathrm { p u m p } } \in [ 2 \Gamma , 6 \Gamma ] )$ . In the spectroscopy experiment, we measured the SRS signal of $\mathrm { C } { = } \hat { \mathrm { C } } ~ ( \Omega = 1 \hat { 6 } 0 0 ~ \mathrm { c m } ^ { - 1 } )$ of a commercial fluorescent dye Alexa 635 by continuously changing the pump-to-absorption frequency detuning Δν from $\bar { 5 . 6 } \ : \mathrm { ~ ( 4 4 8 6 ~ c m ^ { - 1 } ) }$ to 2.2Γ (1773 $\mathsf { c m } ^ { \triangleq 1 } )$ , nearly covering the entire EPR range. The result shows not only the qualitative trend but also good agreement with the phenomenological model. There is a remarkable 150-fold signal enhancement compared with using a traditional light source whose Stokes wavelength is fixed at 1030 nm $( \Delta \dot { \nu } =$ 5.6Γ). To the best of our knowledge, this is the first quantitative verification of the EPR-SRS model. In the microscopy experiment, we demonstrated EPR-SRS bioimaging of a Drosophila brain stained with Alexa 635 dye. The SRS signal enhancement is larger than 7-fold when operated at deep-EPR region $( \Delta \nu = 2 . 2 \Gamma )$ ). These results suggest the potential of MPC-EPR-SRS microscopy in enhancing the sensitivity of biomedical imaging.

Several technical improvements could be made to enhance the performance of the MPC-EPR-SRS system. First, the spectral resolution in the current system is estimated to be 200 $\mathrm { c m } ^ { - 1 }$ , primarily limited by the bandwidths of tunable color filters. As demonstrated in our previous report, etalon can be utilized to narrow down the pass bandwidth to ∼35 cm−1 . 21 ${ \sim } 3 5 ~ \mathrm { c m } ^ { - 1 } . { } ^ { 2 1 }$ Other schemes, such as spectral focusing, could be employed to approach the typical Raman linewidths (∼10 cm−1 ).29−31 $( \sim 1 0 ~ \mathrm { c m ^ { - 1 } } ^ { \tt { 1 } } ) . ^ { 2 9 ^ { \prime } - 3 1 }$

Improved spectral resolution in collaboration with hyperspectral SRS measurement, linear decomposition algorithms, and deep-learning methods would facilitate the deconvolution of complex molecular images in the C-H stretching or fingerprint region.32−34 Next, the acquisition speed and sensitivity of the current apparatus are limited by the hundreds of kHz laser repetition rate. A promising remedy is to employ high-power thin-disk lasers35 with both a high repetition rate (∼10 MHz) and sufficient pulsed energy (∼10 μJ) for supercontinuum generation. Existing techniques, such as nonlinear background removal methods (stimulated Raman gain and loss detection,25,36 spectral modulation,37,38 dualvibrational excitation,39 and deep learning40 and noise cancellation methods (denoising algorithm,41 balance detection,42,43 and boxcar detection44,45) can further enhance the system sensitivity. In conclusion, intense supercontinuum light source like MPC has great potential in SRS spectromicroscopy. In particular, the high spectral energy density and enormous spectral diversity enable interrogation of multiple Raman signatures of low-concentration, versatile molecules via spectrally multiplexed EPR-SRS3 or stimulated Raman excited fluorescence techniques.46

## AUTHOR INFORMATION

## Corresponding Authors

Shi-Wei Chu − Department of Physics and Molecular Imaging Center, National Taiwan University, Taipei 10617, Taiwan; Brain Research Center, National Tsing Hua University, Hsinchu 300044, Taiwan; orcid.org/0000-0001-7728- 4329; Email: swchu@phys.ntu.edu.tw

Shang-Da Yang − Institute of Photonics Technologies, National Tsing Hua University, Hsinchu 300044, Taiwan; Brain Research Center, National Tsing Hua University, Hsinchu 300044, Taiwan; orcid.org/0000-0003-3151- 0700; Email: shangda@ee.nthu.edu.tw

## Authors

Guan-Jie Huang − Department of Physics, National Taiwan University, Taipei 10617, Taiwan  
Cheng-Wei Li − Institute of Photonics Technologies, National Tsing Hua University, Hsinchu 300044, Taiwan  
Po-Yi Lee − Institute of Photonics Technologies, National Tsing Hua University, Hsinchu 300044, Taiwan  
Jia-Xuan Su − Institute of Photonics Technologies, National Tsing Hua University, Hsinchu 300044, Taiwan  
Kuo-Chuan Chao − Brain Research Center, National Tsing Hua University, Hsinchu 300044, Taiwan  
Li-An Chu − Brain Research Center, National Tsing Hua University, Hsinchu 300044, Taiwan; Department of Biomedical Engineering & Environmental Sciences, National Tsing Hua University, Hsinchu 30044, Taiwan  
Ann-Shyn Chiang − Brain Research Center, National Tsing Hua University, Hsinchu 300044, Taiwan; Institute of Systems Neuroscience and Department of Life Science, National Tsing Hua University, Hsinchu 30044, Taiwan  
Ji-Xin Cheng − Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, United States; orcid.org/0000-0002-5607-6683

Bo-Han Chen − Institute of Photonics Technologies, National Tsing Hua University, Hsinchu 300044, Taiwan

Chih-Hsuan Lu − Institute of Photonics Technologies, National Tsing Hua University, Hsinchu 300044, Taiwan

Complete contact information is available at: https://pubs.acs.org/10.1021/acs.jpcb.3c02629

## Author Contributions

The manuscript was written through contributions of all authors. All authors have given approval to the final version of the manuscript.

## Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

This work was supported by the Brain Research Center under the Higher Education Sprout Project, co-funded by the National Science and Technology Council in Taiwan, under grant NSTC-111-2321-B-002-016 (SWC), NSTC-111-2119- M-002-013-MBK (SWC), NSTC-109-2112-M-002-026-MY3 (SWC), NSTC-108-2321-B-002-058-MY2 (SDY), and NSTC-110-2112-M-007-025 (SDY), as well as supported by The Featured Areas Research Center Program (NTHU) and NTU Higher Education Sprout Project (NTU-111 L8809) within the framework of the Higher Education Sprout Project co funded by the NSTC and the Ministry of Education (MOE), Taiwan. In addition, we would like to thank Mr. Chun-An Chen for his helpful assistance with the spontaneous Raman spectrum measurement.

## REEERENCES

(1) Vesely, P. Handbook of Biological Confocal Microscopy; John Wiley & Sons: 2007; p 172−173.  
(2) Dean, K. M.; Palmer, A. E. Advances in fluorescence labeling strategies for dynamic cellular imaging. Nat. Chem. Biol. 2014, 10, 512−523.  
(3) Wei, L.; Chen, Z.; Shi, L.; Long, R.; Anzalone, A. V.; Zhang, L.; Hu, F.; Yuste, R.; Cornish, V. W.; Min, W. Super-multiplex vibrational imaging. Nature 2017, 544, 465−470.  
(4) Aroca, R. Surface-enhanced vibrational spectroscopy; John Wiley & Sons: 2006; p 31.  
(5) McCamant, D. W.; Kukura, P.; Mathies, R. A. Femtosecond Broadband Stimulated Raman: A New Approach for High-Perform ance Vibrational Spectroscopy. Appl. Spectrosc. 2003, 57, 1317−1323.  
(6) Rigneault, H.; Berto, P. Tutorial: Coherent Raman light matter interaction processes. APL Photonics 2018. 3. No. 091101.  
(7) Min, W.; Freudiger, C. W.; Lu, S.; Xie, X. S. Coherent Nonlinear Optical Imaging: Beyond Fluorescence Microscopy. Annu. Rev. Phys. Chem. 2011, 62, 507−530.  
(8) Cheng, J.-X.; Xie, X. S. Coherent Raman Scattering Microscopy; CRC Press: 2012; p 102.  
(9) Freudiger, C. W.; Min, W.; Saar, B. G.; Lu, S.; Holtom, G. R.; He, C.; Tsai, J. C.; Kang, J. X.; Xie, X. S. Label-Free Biomedical Imaging with High Sensitivity by Stimulated Raman Scattering Microscopy. Science 2008, 322, 1857.  
(10) Saar, B. G.; Freudiger, C. W.; Reichman, J.; Stanley, C. M.; Holtom, G. R.; Xie, X. S. Video-Rate Molecular Imaging in Vivo with Stimulated Raman Scattering. Science 2010, 330, 1368.  
(11) Albrecht, A. C. On the Theory of Raman Intensities. J. Chem. Phys, 1961, 34, 14761484.  
(12) Asher, S. A. UV Resonance Raman Studies of Molecular Structure and Dynamics: Applications in Physical and Biophysical Chemistry. Annu. Rev. Phys. Chem. 1988, 39, 537−588.  
(13) Asher, S. A. UV resonance Raman spectroscopy for analytical, physical, and biophysical chemistry. Part 1. Anal. Chem. 1993, 65, 59A−66A.  
(14) Deng, S.; Xu, W.; Wang, J.; Ling, X.; Wu, J.; Xie, L.; Kong, J.; Dresselhaus, M. S.; Zhang, J. Direct measurement of the Raman enhancement factor of rhodamine 6G on graphene under resonan excitation. Nano Res. 2014, 7, 1271−1279.  
(15) Shi, L.; Xiong, H.; Shen, Y.; Long, R.; Wei, L.; Min, W. Electronic Resonant Stimulated Raman Scattering Micro-Spectrosco py. J. Phys. Chem. B 2018, 122, 9218−9224.  
(16) Wei, L.; Min, W. Electronic Preresonance Stimulated Raman Scattering Microscopy. J. Phys. Chem. Lett. 2018, 9, 4294−4301.  
(17) Fimpel, P.; Choorakuttil, A. J. X.; Pruccoli, A.; Ebner, L.; Tanaka, S.; Ozeki, Y.; Winterhalder, M. J.; Zumbusch, A. Double modulation SRS and SREF microscopy: signal contributions unde pre-resonance conditions. Phys. Chem. Chem. Phys. 2020, 22, 21421− 21427.  
(18) Lee, D.; Qian, C.; Wang, H.; Li, L.; Miao, K.; Du, J.; Shcherbakova, D. M.; Verkhusha, V. V.; Wang, L. V.; Wei, L. Toward photoswitchable electronic pre-resonance stimulated Raman probes. J. Chem. Phys. 2021, 154, 135102.  
(19) Zhuge, M.; Huang, K.-C.; Lee, H. J.; Jiang, Y.; Tan, Y.; Lin, H.; Dong, P.-T.; Zhao, G.; Matei, D.; Yang, Q.; Cheng, J.-X. Ultrasensitive Vibrational Imaging of Retinoids by Visible Preresonance Stimulated Raman Scattering Microscopy. Adv. Sci. 2021, 8, 2003136.  
(20) Zhu, L.; Liu, W.; Fang, C. A versatile femtosecond stimulated Raman spectroscopy setup with tunable pulses in the visible to near infrared. Appl. Phys. Lett. 2014, 105, No. 041106.  
(21) Huang, G.-J.; Lai, P.-C.; Shen, M.-W.; Su, J.-X.; Guo, J.-Y.; Chao, K.-C.; Lin, P.; Cheng, J.-X.; Chu, L.-A.; Chiang, A.-S.; et al. Towards stimulated Raman scattering spectro-microscopy across the entire Raman active region using a multiple-plate continuum. Opt. Express 2022, 30, 38975−38984.  
(22) Lu, C.-H.; Tsou, Y.-J.; Chen, H.-Y.; Chen, B.-H.; Cheng, Y.-C.; Yang, S.-D.; Chen, M.-C.; Hsu, C.-C.; Kung, A. H. Generation of intense supercontinuum in condensed media. Optica 2014, 1, 400− 406.  
(23) Lu, C.-H.; Wu, W.-H.; Kuo, S.-H.; Guo, J.-Y.; Chen, M.-C.; Yang, S.-D.; Kung, A. H. Greater than 50 times compression of 1030 nm Yb:KGW laser pulses to single-cycle duration. Opt. Express 2019, 27, 15638−15648.  
(24) Chen, B.-H.; Su, J.-X.; Guo, J.-Y.; Chen, K.; Chu, S.-W.; Lu, H.- H.; Lu, C.-H.; Yang, S.-D. Double-Pass Multiple-Plate Continuum fo High-Temporal-Contrast Nonlinear Pulse Compression. Front. Photonics 2022, 3, No. 937622.  
(25) Berto, P.; Andresen, E. R.; Rigneault, H. Background-Free Stimulated Raman Spectroscopy and Microscopy. Phys. Rev. Lett. 2014, 112, No. 053905.  
(26) Albrecht, A. C.; Hutley, M. C. On the Dependence of Vibrational Raman Intensity on the Wavelength of Incident Light. J. Chem. Phys. 1971, 55, 4438−4443.  
(27) Dudik, J. M.; Johnson, C. R.; Asher, S. A. Wavelength dependence of the preresonance Raman cross sections of CH3CN, SO42−, ClO4−, and NO3−. J. Chem. Phys. 1985, 82, 1732−1740.  
(28) Stancik, A. L.; Brauns, E. B. A simple asymmetric lineshape fo fitting infrared absorption spectra. Vib. Spectrosc. 2008, 47, 66−69.  
(29) Mohseni, M.; Polzer, C.; Hellerer, T. Resolution of spectral focusing in coherent Raman imaging. Opt. Express 2018, 26, 10230− 10241.  
(30) Koike, K.; Smith, N. I.; Fujita, K. Spectral focusing in picosecond pulsed stimulated Raman scattering microscopy. Biomed. Opt. Express 2022, 13, 995−1004.  
(31) Fu, D.; Holtom, G.; Freudiger, C.; Zhang, X.; Xie, X. S. Hyperspectral Imaging with Stimulated Raman Scattering by Chirped Femtosecond Lasers. J. Phys. Chem. B 2013, 117, 4634−4640.  
(32) Lu, F.-K.; Basu, S.; Igras, V.; Hoang, M. P.; Ji, M.; Fu, D.; Holtom, G. R.; Neel, V. A.; Freudiger, C. W.; Fisher, D. E.; et al. Label-free DNA imaging in vivo with stimulated Raman scattering microscopy. Proc. Natl. Acad. Sci. 2015, 112, 11624.  
(33) Zhang, L.; Shi, L.; Shen, Y.; Miao, Y.; Wei, M.; Qian, N.; Liu, Y.; Min, W. Spectral tracing of deuterium for imaging glucose metabolism. Nat. Biomed. Eng. 2019, 3, 402−413.  
(34) Zhang, J.; Zhao, J.; Lin, H.; Tan, Y.; Cheng, J.-X. High-Speed Chemical Imaging by Dense-Net Learning of Femtosecond Stimulated Raman Scattering. J. Phys. Chem. Lett. 2020, 11, 8573− 8578.  
(35) Tsai, C.-L.; Meyer, F.; Omar, A.; Wang, Y.; Liang, A.-Y.; Lu, C.- H.; Hoffmann, M.; Yang, S.-D.; Saraceno, C. J. Efficient nonlinear compression of a mode-locked thin-disk oscillator to 27 fs at 98 W average power. Opt. Lett. 2019, 44, 4115−4118.  
(36) Heuke, S.; Lombardini, A.; Büttner, E.; Rigneault, H. Simultaneous stimulated Raman gain and loss detection (SRGAL). Opt. Express 2020, 28, 29619−29630.  
(37) Zhang, D.; Slipchenko, M. N.; Leaird, D. E.; Weiner, A. M.; Cheng, J.-X. Spectrally modulated stimulated Raman scattering imaging with an angle-to-wavelength pulse shaper. Opt. Express 2013, 21, 13864−13874.  
(38) Xiong, H.; Qian, N.; Zhao, Z.; Shi, L.; Miao, Y.; Min, W. Background-free imaging of chemical bonds by a simple and robust frequency-modulated stimulated Raman scattering microscopy. Opt. Express 2020, 28, 15663−15677.  
(39) Heuke, S.; Rimke, I.; Sarri, B.; Gasecka, P.; Appay, R.; Legoff, L.; Volz, P.; Büttner, E.; Rigneault, H. Shot-noise limited tunable dual-vibrational frequency stimulated Raman scattering microscopy. Biomed. Opt. Express 2021, 12, 7780−7789.  
(40) Manifold, B.; Thomas, E.; Francis, A. T.; Hill, A. H.; Fu, D. Denoising of stimulated Raman scattering microscopy images via deep learning. Biomed. Opt. Express 2019, 10, 3860−3874.  
(41) Liao, C.-S.; Choi, J. H.; Zhang, D.; Chan, S. H.; Cheng, J.-X. Denoising Stimulated Raman Spectroscopic Images by Total Variation Minimization. J. Phys. Chem. C 2015, 119, 19397−19403.  
(42) Freudiger, C. W.; Yang, W.; Holtom, G. R.; Peyghambarian, N.; Xie, X. S.; Kieu, K. Q. Stimulated Raman scattering microscopy with a robust fibre laser source. Nat. Photonics 2014, 8, 153−159.  
(43) Crisafi, F.; Kumar, V.; Scopigno, T.; Marangoni, M.; Cerullo, G.; Polli, D. In-line balanced detection stimulated Raman scattering microscopy. Sci. Rep. 2017, 7, 10745.  
(44) Khatua, D. P.; Gurung, S.; Singh, A.; Khan, S.; Sharma, T. K.; Jayabalan, J. Filtering noise in time and frequency domain for ultrafast pump−probe performed using low repetition rate lasers. Rev. Sci. Instrum. 2020, 91, 103901.  
(45) Fimpel, P.; Riek, C.; Ebner, L.; Leitenstorfer, A.; Brida, D.; Zumbusch, A. Boxcar detection for high-frequency modulation in stimulated Raman scattering microscopy. Appl. Phys. Lett. 2018, 112, 161101.  
(46) Xiong, H.; Shi, L.; Wei, L.; Shen, Y.; Long, R.; Zhao, Z.; Min, W. Stimulated Raman excited fluorescence spectroscopy and imaging. Nat. Photonics 2019, 13, 412−417.

## NOTE ADDED AETER ISSUE PUBLICATION

The virtual issue designation was omitted in the version published on July 26, 2023 and was correctly restored on August 17, 2023.

![](images/3932a67c3b4ea054df859d120b8fe28e40fbe4a46d75d922a6752e22bb0c3760.jpg)

<details>
<summary>natural_image</summary>

3D molecular model of a virus-like structure with yellow filamentous body and green/red ribbons at base (no text or symbols)
</details>

CAS BIOFINDER DISCOVERY PLATFORMTM

## BRIDGE BIOLOGY AND CHEMISTRY FOR FASTER ANSWERS

Analyze target relationships, compound effects, and disease pathways

Explore the platform

![](images/4b61aaab8903e39ca9a430d8d8ec82ff74ffa1b3e0b9aa9e5da9888db892cc66.jpg)