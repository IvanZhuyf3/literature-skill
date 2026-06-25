# Title: Photothermally Detected Stimulated Raman Microscopy towards Ultrasensitive Chemical Imaging

Authors: Yifan Zhu1, †, Xiaowei Ge2, †, Hongli Ni2 , Jiaze Yin2 , Haonan Lin3 , Le Wang2 , Yuying Tan3 , Chinmayee V. Prabhu Dessai3 , Ji-Xin Cheng1,2,3,4, \*

## Affiliations:

1 Department of Chemistry, Boston University, Boston, MA, 02215, USA  
2 Department of Electrical and Computer Engineering, Boston University, Boston, MA, 02215, USA  
3 Department of Biomedical Engineering, Boston University, Boston, MA, 02215, USA  
4 Photonics Center, Boston University, Boston, MA, 02215, USA  
# Equal contribution  
\*Corresponding author: jxcheng@bu.edu

Abstract: Stimulated Raman scattering (SRS) microscopy has shown enormous potential in revealing molecular structures, dynamics and couplings in complex systems. However, the sensitivity of SRS is fundamentally limited to milli-molar level due to the shot noise and the small modulation depth. To overcome this barrier, we revisit SRS from the perspective of energy deposition. The SRS process pumps molecules to their vibrationally excited states. The thereafter relaxation heats up the surrounding and induces refractive index changes. By probing the refractive index changes with a laser beam, we introduce stimulated Raman photothermal (SRP) microscopy, where a >500-fold boost of modulation depth is achieved. Versatile applications of SRP microscopy on viral particles, cells, and tissues are demonstrated. SRP microscopy opens a new way to perform vibrational spectroscopic imaging with ultrahigh sensitivity.

One-Sentence Summary: We demonstrate a new spectroscopic imaging method that improves the signal intensity by >500-fold.

Main Text: Avoiding the non-resonant background encountered in coherent anti-Stokes Raman scattering (CARS) microscopy, stimulated Raman scattering (SRS) microscopy has become a powerful platform in the field of chemical imaging (1-3). In SRS (Fig. 1A), two spatialtemporally overlapped laser pulse trains, namely pump and Stokes, coherently interact with Raman-active molecules that resonates at the laser beating frequency, causing a stimulated Raman gain and loss in the Stokes and the pump field, respectively. While providing the same molecular vibrational features to conventional Raman spectroscopy, SRS offers up to 6 orders of speed improvement comparing to spontaneous Raman (3). Such speed improvement, together with development of vibrational probes (4), has enabled many applications, e.g. label-free stimulated Raman histology (5,6), nutrient mapping (7-9), unveiling altered metabolism in cancer (10-14), heterogeneity in microbiome (15), rapid detection of antimicrobial susceptibility (16). Despite these advances, the detection sensitivity of SRS is fundamentally challenged by the small modulation depth (0.1% for a pure liquid) and the shot noise in the pump or Stokes beam (17,18), where simply increasing the number of photons can easily exceed the power tolerance of the sample.

Pushing the fundamental limit of SRS sensitivity requires either a reduction of measurement noise, or a boost of SRS signal. On the reduction of SRS measurement noise, efforts focused on using squeezed light, termed “quantum-enhanced SRS”. Signal-to-noise-ratio (SNR) enhancements of 3.6 dB (19) with continuous wave squeezed light, or 2.89 dB (20) with pulsed squeezed light have been demonstrated with no additional perturbation on sample. While the future of this method is bright, it is currently limited by the low squeeze efficiency and decoherence in complex imaging systems. On the boost of SRS signal, different photophysical processes have been utilized to increase the cross-section, hence the signal intensity, including electronic pre-resonance SRS (21-23), plasmon enhanced SRS (24) and stimulated Raman excited fluorescence (25). Very high enhancement factor $( 1 0 ^ { 4 } \sim 1 0 ^ { 7 } )$ of SRS signal, and single molecule SRS measurement (24,25), have been achieved. However, the requirement of special target molecules or plasmonic nanostructures constrains the scope of applications.

To seek new approaches towards boosting the signal, we revisit the physics of SRS from the perspective of energy transfer from laser fields to the sample. As explored by Cheng and coworkers in 2007 from the perspective of photodamage in CARS imaging (26), \~0.08% of the laser power is absorbed by the sample through the simultaneously occurred stimulated Raman gain and loss processes. As illustrated in Fig. 1b, when pump and Stokes pulses with appropriate wavelengths interact with Raman-active molecules, the target molecules are pumped to their vibrationally excited states, with the transition energy equals to the beating frequency between the pump and Stokes lasers. Importantly, after SRS excitation, the vibrationally excited molecules relax their vibrational energy quickly through non-radiative decay, and consequently, heat up the surrounding environment, causing a stimulated Raman photothermal (SRP) effect.

Optically detected photothermal microscopy has been well developed (27) and has reached the sensitivity down to a single molecule (28). In photothermal spectroscopy, first reported in 1970s (29), an optical absorption raises the local temperature, creating local change of refractive index, which is measured with a probing beam. Early photothermal microscopy works focused on electronic absorption, targeting non-fluorescent dye molecules or metal nanostructures (27). Recently developed mid-infrared photothermal (MIP) microscopy provides universal infrared active vibrational spectroscopic features, offers a detection sensitivity at micro-molar level, and creates a spatial resolution at the visible diffraction limit (30,31) or even higher by probing the high harmonic signals (32). To the contrary, the thermal effects induced by a Raman process is commonly believed minimal due to the small cross sections of Raman scattering, and consequent Raman based photothermal imaging is usually considered impossible. However, with coherent Raman excitation that nonlinearly benefits from high laser peak power, we prove and quantify the thermal effect of SRS process, and demonstrate its potential in chemical imaging with ultrahigh sensitivity, complementary spectroscopic information to MIP, as well as negligible water absorption.

## Results and discussion

## Simulation of the SRP effect

For a stimulated Raman loss measurement, the relationship between pump beam modulation depth η, pump laser intensity $I _ { \mathrm { p } } ,$ and change of photon number per pulse, ΔN, can be written as:

$$
\eta = \frac {2 \cdot \Delta N \cdot h \omega_ {p} \cdot f _ {r e p}}{I _ {p}} \tag {1}
$$

where h is the Plank’s constant, $\omega _ { \mathrm { p } }$ is the pump wavenumber, and $f _ { \mathrm { r e p } }$ is the laser repetition rate. With this, one can estimate the energy deposition per pair of SRS pulses by $E = \Delta N \cdot h \omega _ { R }$ , where ωR is the target Raman shift. Literature (4) has shown that with 25 mW (modulated at 50% duty cycle) and 15 mW on-sample powers for 80 MHz Stokes and pump beams, respectively, the SRS modulation depth on the $2 9 1 3 ~ \mathrm { c m } ^ { - 1 }$ mode of dimethyl sulfoxide (DMSO) reaches 0.04%. By inserting these measured values into the equations, the energy deposition per pair of laser pulses is found to be 8.7 fJ, equivalent to $0 . 7 \mu \mathrm { W }$ .

A  
![](images/3bd049e54c7391f24dd5a5c2fa4748769756ed5d2d726be7f2ae14c75dc96045.jpg)

<details>
<summary>line chart</summary>

| Component | Value |
| --------- | ----- |
| Stokes    | High  |
| Pump      | High  |
</details>

![](images/4804cf6f1f1ef015e5bd2dd76e76b9d3a551ef6d2fea18ee571d7bf71632b7aa.jpg)

<details>
<summary>bar chart</summary>

| Component | Value |
| --------- | ----- |
| Stokes    | SRG   |
| Pump      | SRL   |
</details>

B

![](images/11f1d0f8fdef6c318414d117b3113d7ee41ea447bdf62388be2e46df304d9d35.jpg)

<details>
<summary>text_image</summary>

VS
ωp
ωs
GS
Ω
Nonradiative
decay
</details>

c  
![](images/7058e9d9f7220185e83f9deb5e75d7c8dce301feff73e928d063a415cb377ede.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | ΔT / K (r = 0) | ΔT / K (r = 1 μm) | ΔT / K (r = 2 μm) |
|-----------|----------------|-------------------|-------------------|
| 0         | 0              | 0                 | 0                 |
| 2         | ~1.5           | ~0.2              | ~0.1              |
| 4         | ~2.0           | ~0.3              | ~0.2              |
| 6         | ~2.2           | ~0.4              | ~0.3              |
| 8         | ~2.3           | ~0.5              | ~0.4              |
| 10        | ~2.4           | ~0.6              | ~0.5              |
| 12        | ~2.5           | ~0.7              | ~0.6              |
| 14        | ~2.4           | ~0.6              | ~0.5              |
| 16        | ~2.2           | ~0.5              | ~0.4              |
| 18        | ~2.0           | ~0.4              | ~0.3              |
| 20        | ~1.8           | ~0.3              | ~0.2              |
| 22        | ~1.6           | ~0.2              | ~0.1              |
| 24        | ~1.4           | ~0.1              | ~0.05             |
</details>

D  
![](images/701eff54753d4deb934c4bf50ed056c6423f0a977b90d2563877d3ac991cd71b.jpg)

<details>
<summary>heatmap</summary>

| r / μm | n(r) |
| ------ | ---- |
| 0      | 0    |
| 5      | ~0.3 |
| 10     | ~0.6 |
| 15     | ~0.8 |
| 20     | ~1.0 |
</details>

E  
![](images/3aaef67af18e0ed736b402eb9bf1d0de5d603366f3bc867d3399c4411bab275d.jpg)

<details>
<summary>chemical</summary>

Molecular orbital diagram showing SRS off and SRS on states with T and F labels
</details>

F  
![](images/23240a1cb92ee01a4af302d87999c53dd93ef6416a88dc2cc34591dfcccc4875.jpg)

<details>
<summary>line chart</summary>

| Time / µs | Off resonance (background) | On resonance | On resonance (background removed) | Simulation |
| --------- | -------------------------- | ------------ | --------------------------------- | ---------- |
| 0         | 1.00                       | 1.00         | 1.00                              | 1.00       |
| 2         | 1.00                       | 0.99         | 0.98                              | 0.99       |
| 4         | 1.00                       | 0.98         | 0.97                              | 0.98       |
| 6         | 1.00                       | 0.97         | 0.97                              | 0.97       |
| 8         | 1.00                       | 0.97         | 0.97                              | 0.97       |
| 10        | 1.00                       | 0.97         | 0.97                              | 0.97       |
| 12        | 1.00                       | 0.97         | 0.97                              | 0.97       |
</details>

Fig. 1 Theoretical simulation and experimental observation of the SRP effect. (A) Schematic of stimulated Raman gain and loss. (B) Schematic of stimulated Raman photothermal (SRP) effect. (C) Simulation of temperature rise induced by SRP in temporal (top) and spatial (bottom) domains. Spatial scale bar: 1 μm. (D) Simulated profile of thermal lens induced by SRP in pure DMSO. (E) Illustration of fluorescence thermometer measurement of SRP-mediated temperature rise. (F) Measured fluorescence of rhodamine B in DMSO during an SRS process. The beating frequency $( \omega _ { \mathrm { { p } } } \mathrm { { - } } \omega _ { \mathrm { { s } } } )$ is tuned to $2 9 1 3 \mathrm { c m } ^ { - 1 }$ for on-resonance and $2 8 5 0 ~ \mathrm { c m } ^ { - 1 }$ for offresonance.

With this energy deposition estimation, we applied Fourier’s law and built a finite unit model (Fig. S1) to quantitatively simulate the stimulated Raman induced temperature rise in pure DMSO. Simulation results (Fig. 1C) show that, when using an objective with 0.8 N.A. (numerical aperture), and routinely used laser power (25 mW and 50 mW for pump and Stokes, 80 MHz repetition rate, 50% duty cycle), the temperature rise at the center of the laser focus can reach as high as 2.4 K after 12 µs of stimulated Raman excitation, corresponding to 960 pairs of pump/Stokes pulses. The temperature rises at r = 1 μm and 2 μm away from the focal center are 0.54 K and 0.12 K, respectively, at t = 12 μs. The temperature map at different time points is also shown in Fig. 1C. The full width at half maximum (FWHM) of the temperature rising field at t = 12 μs is calculated to be 1.1 μm, suggesting a very localized thermal field.

The temperature elevation subsequently changes the local refractive index through the thermaloptic effect. For pure DMSO with a refractive index of 1.497 and a thermo-optic coefficient of $- \dot { 4 } . 9 3 { \times } 1 0 ^ { - 4 } \mathrm { K } ^ { - 1 }$ (∂n/∂T) (33), at t = 12 μs, the stimulated Raman induced heating causes a refractive index change by −0.07% at the focal center. As shown in Fig. 1D, such an index change nonlinearly extends to the surroundings through heat propagation, thus creating a thermal lens. Formation of such a thermal lens builds the foundation for SRP microscopy.

## Experimental confirmation of the SRP effect

We experimentally confirmed the simulation results with a fluorescence thermometer. It has been well documented that the emission intensities of some fluorophores is temperature dependent (34). For instance, the fluorescence intensity of Rhodamine B decreases by \~2% per Kelvin at room temperature (35). This property has been utilized in fluorescence-detected midinfrared photothermal spectroscopy (36,37). Here, we adopt this method to measure the temperature rise at the SRS focus, using Rhodamine B as a fluorescence thermometer. When chirped pump and Stokes lasers are focused into a DMSO solution of Rhodamine B, the Rhodamine B molecules at the SRS focus are electronically excited to emit fluorescence through multiphoton absorption. Meanwhile, when the beating frequency between pump and Stokes is tuned to resonate with the C-H vibration in DMSO, the SRP effect occurs to raise the temperature and accordingly decrease the two-photon fluorescence intensity of Rhodamine B molecules (Fig. 1E).

With this design and identical parameters as in the simulation, we find that the fluorescence intensity drops \~2.3% after 12 μs of on-resonance SRS, corresponding to \~1.2 K of temperature rise (Fig. 1F), close to the simulation result of 2.4 K. After weighting each unit in the temperature field with corresponding two-photon excitation intensity of Gaussian beams, the fluorescence change curve can be well fitted as shown in Fig. 1F.

## A chemical microscope sensing the SRP effect

By sensing the local refractive index modulation using a third continuous wave beam, we have built an SRP microscope as illustrated in Fig. 2A. Briefly, the synchronized pump and Stokes pulse trains are intensity-modulated by two AOMs, combined, and chirped to excite the molecules. A probe beam is then collinearly aligned with the SRS beams. A pair of lenses adjusts the collimation of the probe beam to make the probe laser focus axially off the SRS focus, to maximize the photothermal signal (27). An iris at the back focal plane of the condenser lens is set to N.A. = 0.4 to convert the probe beam refraction modulation to an intensity modulation. The SRP effect creates a divergent lens, which reduces the effective N.A. of the probe laser focus, thus increases the transmission of the probe beam through the iris. A fast photodiode detects the probe beam intensity, followed by a highpass filter and a broadband amplifier. The

SRP modulation induced by synchronized pump and Stokes pulses is digitized in real time by a high-speed digitization card. Details can be found in Methods and Fig. S2.

Unlike SRS, both pump and Stokes beam are intensity-modulated in the SRP microscope. Since the SRS intensity is proportional to the product of pump and Stokes peak power, with conserved average laser power, reduction of laser duty cycle leads to higher laser peak power, hence more SRS energy deposition. Our experiment (Fig. 2B) confirmed this idea and showed much higher SRP signal intensity with lower duty cycle. In SRP imaging applications, the duty cycle was set to 5\~10 % as a compromise between signal intensity and laser power. Another key parameter is the modulation frequency. Lower frequency shows higher signal intensity (Fig. 2C) due to longer heat accumulation time, but suffers more from the 1/f laser intensity noise (38) and meanwhile reduces the imaging speed. 125 kHz was chosen to balance these factors.

![](images/d4a44b6c33bf0ca21780f9dd461aeb2fd37a8bab873565702ed72cee725accc8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  DL["LD"] --> AOM["AOM"]
  AOM --> PBS["PBS"]
  PBS --> HWP["HWP"]
  HWP --> Pump["Pump"]
  Pump --> Stokes["Skokes"]
  DM1["DM1"] --> Probe["Probe"]
  Probe --> Rods["Rods"]
  Rods --> Telescope["Telescope"]
  Telescope --> DM2["DM2"]
  DM2 --> SM["SM"]
  SM --> OBJ["OBJ"]
  OBJ --> Sample["Sample"]
  Sample --> COND["COND"]
  COND --> Iris["Iris"]
  Iris --> SP["SP"]
  SP --> PD["PD"]
  PD --> HP["HP"]
  HP --> AMP["AMP"]
    style DM1 fill:#f9f,stroke:#333
    style DM2 fill:#ccf,stroke:#333
    style PM fill:#fff,stroke:#333
    style PBS fill:#fff,stroke:#333
    style HWP fill:#fff,stroke:#333
    style STK fill:#fff,stroke:#333
    style SEM fill:#fff,stroke:#333
    style DISP fill:#fff,stroke:#333
    style OJ fill:#fff,stroke:#333
    style COND fill:#fff,stroke:#333
    style IR fill:#fff,stroke:#333
    style DSP fill:#fff,stroke:#333
    style SP fill:#fff,stroke:#333
    style IR fill:#fff,stroke:#333
    style DSP fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill#000,stroke:#000,color:#fff
    style ORJ fill:#000,stroke:#000,color:#fff
    style ORJ fill:#000,stroke:#000,color:#fff
    style ORJ fill:#000,stroke:#000,color:#fff
    style ORJ fill:#000,stroke:#000,color:#fff
    style ORJ fill:#000,stroke:#000,color:#fff
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
    style ORJ fill:#fff,stroke:#333
```
```
</details>

![](images/892a6742fd4189943c874f8b0685734b640605e1f3ffa390759c5c9a06972143.jpg)

<details>
<summary>line chart</summary>

| Duty cycle | Intensity (V) |
| ---------- | ------------- |
| 6.05%      | 0.15          |
| 12.1%      | 0.12          |
| 25%        | 0.08          |
| 50%        | 0.04          |
</details>

![](images/91bdb8a9d8201ea88e4cf534572a9bc97963dce58599fd2c0f0e5cfc917ca4f5.jpg)

<details>
<summary>line chart</summary>

| Time / µs | Off resonance | On resonance |
| --------- | ------------- | ------------ |
| 0         | 56.5          | 56.5         |
| 8         | 56.5          | 56.5         |
| 16        | 56.5          | 56.5         |
| 24        | 56.5          | 56.5         |
| 32        | 56.5          | 56.5         |
</details>

![](images/d0fbc108ff6ed0de8ea9390cd572e2040730603a147b82ce694000281e636010.jpg)

<details>
<summary>line chart</summary>

| Modulation frequency (kHz) | Intensity (V) |
| -------------------------- | ------------- |
| 18.3                       | 0.12          |
| 55                         | 0.08          |
| 110                        | 0.06          |
| 225                        | 0.04          |
| 450                        | 0.02          |
</details>

Fig. 2 SRP microscope design and characterization of SRP modulation depth as a function of duty cycle and modulation frequency. (A) Experimental setup. DM: dichroic mirror; DL: delay line; AOM: acousto-optic modulator; PBS: polarizing beam splitter; HWP: halfwave plate; SM: scanning mirror; OBJ: objective; COND: condenser; SP: spectral filter; PD: photodiode; HP: highpass filter; AMP: amplifier. (B) Measured SRP signal as a function of modulation duty cycle. (C) Measured SRP signal as a function of modulation frequency. (D) SRP generates a large (22.3%) modulation depth with DMSO as the sample. The on-resonance and off-resonance traces were obtained with the Raman shift at 2913 cm−1 and 2850 cm−1, respectively.

For pure liquid, under 5% duty cycle and 125 kHz modulation frequency, the induced modulation on the probe beam was so strong that we could directly measure the SRP signal in the direct current channel without any amplification, as shown in Fig. 2D. With reasonable laser powers on sample to excite the C-H symmetric stretching mode (2913 cm−1 ) of DMSO, the modulation depth reached 22.3%, which is 500-fold higher than the SRS modulation depth (0.04%) with identical average power. The tremendously higher modulation depth builds the foundation for a better detection sensitivity.

In addition to duty cycle and modulation frequency, medium is another crucial factor that affects the photothermal signal intensity (39). It has been well-formulated that the photothermal signal intensity (ΣPT), thermo-optic coefficient (∂n/∂T) and heat capacity (Cp) hold the relationship of $\scriptstyle { \sum \mathrm { p r } = n ( { \hat { o } n } / { \hat { o } T } ) / C _ { \mathfrak { p } } }$ . Yet, the most common medium in biological samples, i.e. water, has a relatively low thermo-optic coefficient $( - 1 . 1 3 { \times } 1 0 ^ { - 4 } \mathrm { K } ^ { - }$ 1 ) (40) and relatively high heat capacity $( 4 1 8 1 \ \mathrm { J \cdot { k g } ^ { - 1 } { \cdot } K ^ { - 1 } } )$ . To avoid the signal loss caused by water medium, we investigated a few common liquid media, as shown in table. S1. It is found that glycerol maintains the signal intensity very well. Meanwhile, glycerol shows high bio-compatibility, and is widely used as a mounting medium or clearing agent in bio-imaging. Our simulation of the thermal lens comparison, shown in Fig. S4, also agrees with the previous theory that the peak refractive index change in glycerol medium is \~2.5-fold as high as in water, with identical heat source (100 nm PMMA nanoparticle under on-resonance SRP heating). Therefore, glycerol was chosen as the medium in following SRP experiments except for the liquid samples. Also, considering the Raman-active vibrational features of glycerol itself, deuterated glycerol (glycerol-d8) was applied for SRP measurement at the C-H and fingerprint regions.

## Limit of detection and spatial resolution

We characterized the performance of our SRP microscope with well-defined samples. We first measured the limit of detection (LOD) for DMSO, focusing on the 2913 cm−1 mode. To keep the thermal and optical properties constant throughout the measurement, deuterated DMSO (DMSOd6) was used as the solvent to dilute DMSO. As shown in Fig. 3A (and Fig. S5 for complete measurement), the SRP spectrum was clean and smooth with high concentration DMSO, and the signal was observable with concentration as low as 15.4 mM. We calculated the LOD with the equation of $\mathrm { L O D } = 3 \sigma / k .$ where σ is the standard deviation of the baseline, and k is the slope of the intensity-concentration linear calibration curve. Calculation yielded a sub-millimolar level LOD value of 0.93 mM. In comparison, the LOD by SRS under identical average laser powers was found to be 39 mM. Thus, SRP measurement offers a \~40-fold improvement in LOD. The LODs for C≡C and C-D bonds were measured by using 1,7-Octadiyne in DMSO medium (Fig. S6) and DMSO-d6 in DMSO medium (Fig. S7). In both cases, SRP showed superior sensitivity than SRS with conserved average power.

Such sensitivity improvement allows high-quality imaging of nanoparticles. With the SRP microscope, we successfully acquired hyperspectral image of 100 nm Poly(methyl methacrylate) (PMMA) beads as shown in Fig. 3C. The acquired SRP spectrum showed Raman peak of PMMA at 2950 cm−1 which was well-distinguished from the background spectrum as shown in Fig. S8, with an SNR \~7.0 after BM4D denoising (41). In comparison, the SRS measurement showed no contrast of 100 nm beads on the same sample with identical average laser power. Collectively, SRP showed significantly improved sensitivity comparing to SRS, both for liquid samples and for nanoparticles. Importantly, the introduction of a third probe beam at a shorter wavelength helped improve the spatial resolution (Fig. 3D). We plotted the intensity profile

across a pair of 100 nm PMMA beads, with the Gaussian fitted FWHM found to be \~218 nm. Deconvolution with the beads size generated a FWHM of \~ 194 nm, which was below the theoretical resolution limit of SRS under the same condition (\~217 nm, FWHM of Airy disk). The FWHM was a little larger than the theoretical resolution limit yielded from the product of pump, Stokes and probe point spread functions (\~167 nm), probably due to the imperfect overlap between the probe and the SRS focus along the axial axis.

A  
![](images/21554bb32d8a5bcd2f934b96cacd839523013b1443f1477d22c8231d300f30b0.jpg)

<details>
<summary>line chart</summary>

| Concentration (mM) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 0                  | ~0               |
| 46.7               | ~50              |
| 15.6               | ~100             |
| 140                | ~280             |
</details>

B  
![](images/10fef05c5c529fe7928bb767cd9ada00d9a14df8227684b2c5cc0d117d0e88fa.jpg)

<details>
<summary>line chart</summary>

| Concentration / mM | Intensity / a.u. |
| --- | --- |
| 0 | ~0 |
| 500 | ~5 |
| 1000 | ~10 |
| 1500 | ~15 |
| 2000 | ~2 |
| 2500 | ~3 |
| 3000 | ~1 |
| 3500 | ~0.5 |
| 4000 | ~0.8 |
| 4500 | ~1 |
| 5000 | ~1.5 |
| 5500 | ~2 |
| 6000 | ~3 |
| 6500 | ~4 |
| 7000 | ~5 |
| 7500 | ~6 |
| 8000 | ~5 |
| 8500 | ~4 |
| 9000 | ~3 |
| 9500 | ~2 |
| 10000 | ~1 |
| 10500 | ~0.5 |
| 11000 | ~0.8 |
| 11500 | ~1 |
| 12000 | ~1.5 |
| 12500 | ~2 |
| 13000 | ~3 |
| 13500 | ~4 |
| 14000 | ~5 |
| 14500 | ~6 |
| 15000 | ~7 |
| 15500 | ~8 |
| 16000 | ~9 |
| 16500 | ~1 |
| 17000 | ~1.5 |
| 17500 | ~2 |
| 18000 | ~3 |
| 18500 | ~4 |
| 19000 | ~5 |
| 19500 | ~6 |
| 20000 | ~7 |
| 20500 | ~8 |
| 21000 | ~9 |
| 21500 | ~1 |
| 22000 | ~1.5 |
| 22500 | ~2 |
| 23000 | ~3 |
| 23500 | ~4 |
| 24000 | ~5 |
| 24500 | ~6 |
| 25000 | ~7 |
| 25500 | ~8 |
| 26000 | ~9 |
| 26500 | ~1 |
| 27000 | ~1.5 |
| 27500 | ~2 |
| 28000 | ~3 |
| 28500 | ~4 |
| 29000 | ~5 |
| 29500 | ~6 |
| 30000 | ~7 |
| 30500 | ~8 |
| 31000 | ~9 |
| 31500 | ~1 |
| 32000 | ~1.5 |
| 32500 | ~2 |
| 33000 | ~3 |
| 33500 | ~4 |
| 34000 | ~5 |
| 34500 | ~6 |
| 35000 | ~7 |
| 35500 | ~8 |
| 36000 | ~9 |
| 36500 | ~1 |
| 37000 | ~1.5 |
| 37500 | ~2 |
| 38000 | ~3 |
| 38500 | ~4 |
| 39000 | ~5 |
| 39500 | ~6 |
| 40000 | ~7 |
| 40500 | ~8 |
| 41000 | ~9 |
| 41500 | ~1 |
| 42000 | ~1.5 |
| 42500 | ~2 |
| 43000 | ~3 |
| 43500 | ~4 |
| 44000 | ~5 |
| 44500 | ~6 |
| 45000 | ~7 |
| 45500 | ~8 |
| 46000 | ~9 |
| 46500 | ~1 |
| 47000 | ~1.5 |
| 47500 | ~2 |
| 48000 | ~3 |
| 48500 | ~4 |
| 49000 | ~5 |
| 49500 | ~6 |
| 50000 | ~7 |
</details>

C  
![](images/9173c5ec96b319696d8161bdd24f92dd4f530302618805bd43096d5b1e26e923.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing SRP-labeled cells with red-orange fluorescence and white arrows indicating specific features (no text or symbols present)
</details>

SRS  
![](images/c52e434771b7e1ff0f806c5da1511ad890d8a236e50fecb5aa27c4d4f7dcbe7d.jpg)

<details>
<summary>natural_image</summary>

Abstract red textured pattern with no visible text or symbols
</details>

D  
![](images/f5757a9fab301e6aac4b1193a9cabf99730d4ed0dc8df80d4d3202b07b58b371.jpg)

<details>
<summary>line chart</summary>

| Displacement / nm | Intensity / a.u. |
| ----------------- | ---------------- |
| 0                 | 0.93             |
| 200               | 0.95             |
| 400               | 1.02             |
| 600               | 0.95             |
| 800               | 1.02             |
| 1000              | 0.95             |
| 1200              | 0.93             |
</details>

Fig.3 SRP spectroscopy and imaging performance characterization. (A-B) SRP (A) or SRS (B) signal with gradient concentration of DMSO dissolved in DMSO-d6. Concentration unit: mM. Insert shows the signal intensity as a function of concentration (complete data in Fig. S6). (C) SRP and SRS image of 100 nm PMMA beads at 2930 cm−1 with the same average power, at the same field of view. Scale bar: 500 nm. (D) The Gaussian fitting measured size of the bead is 218 nm (FWHM).

## Biological applications

The outstanding performance encouraged us to explore the potential of SRP in bio-imaging. Inspired by the sensitive imaging on 100-nm nanoparticles, we first tested the capability of imaging viral particles. As shown on Fig. 4A1, single varicella-zoster virus (diameter ≈ 180 nm)42 could be clearly resolved from the background with an SNR \~20. The SRP spectrum of a single virus (Fig. 4A2) peaked at 2950 cm-1, indicating strong contribution from the nucleotide at the core of the virus.

We then applied SRP microscopy to the spectrally silent region. Bacteroides cultured in heavy water were imaged as shown in Fig. 4B1. Decent contrast was obtained from the C-D vibration, while the off-resonance image (Fig. 4B2) showed little signal at the same field of view,

confirming the Raman origin of the signals. Such results indicate the potential of SRP in metabolic imaging of single bacteria.

Pancreatic cancer cell MIA Paca-2 was selected as the testbed for mammalian cell imaging (Fig. 4C1). Glycerol-d8 was applied to replace the PBS buffer and immerse the cells to enhance the SRP contrast. SRP provided nice contrast at the C-H region. Phasor analysis was applied to segment the cellular compartments (Fig. S9), where up to 6 different components could be well identified (Fig. 4C2). Notably, the nuclear membrane outstood from the cytoplasm and the nuclear matrix, giving rise to the potential of applying SRP to study fine structure in a membrane. The high contrast is probably due to the high thermo-optic coefficients and low heat capacities of membranes.

The high sensitivity of SRP also provides access to weak Raman bands in the fingerprint region. Fig. 4D1 showed the SRP image of a 10 μm thick OVCAR-5 cancer tissue at 1650 cm-1, targeting the Amide I band in proteins and the C=C vibration in lipids. High-quality spectra were resolved from the hyperspectral image stack. Lipid (region of interests 1 (ROI1)) and protein (ROI2) species are clearly differentiated, as shown in Fig. 4D2. Collectively, versatile bioimaging applications are demonstrated, scaling from single virus to cancerous tissues.

A1  
![](images/2a68c3e6507082faa7bec252e9360363545132db3bd39fce295f5c33985b40e9.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescent spots on a dark blue background, with white arrows and a scale bar (no text or symbols)
</details>

A2  
![](images/f882f23bdaab4fbb849d5830fbf6efcbaab995b1b95af8ec660b0fe07f7919a0.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Virus | Background |
| ------------------ | ----- | ---------- |
| 2850               | 0.1   | 0.05       |
| 2900               | 0.5   | 0.2        |
| 2950               | 1.6   | 0.4        |
| 3000               | 0.3   | 0.1        |
| 3050               | 0.1   | 0.05       |
</details>

B1  
![](images/e425c91ff7a710ba6beb8edd2886d37aaa27e1b6614a873914c0035a7801d437.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing green and blue cellular structures against a black background, with a 2170 cm⁻¹ scale bar (no text or symbols beyond scale indicator)
</details>

B2  
![](images/2dfe22d32a231c3549e84a80818384599a3b42e9b3cb894fba02a3b1116003ae.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a dark field with scattered bright spots and a scale bar labeled 2361 cm⁻¹ (no other text or symbols)
</details>

C1  
![](images/4aadad3f5de767787c31d6ccd8ceaeba566ee5f59dcbad802bf1fd0cc79988a7.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image of a cell with green fluorescent staining, showing nucleus and cytoplasm (no text or symbols)
</details>

C2  
![](images/1a55d2c3aa8b6ece2f3a2ff0a0f2303a386e83e4ecebd6e0dc200a5a3ffc1f63.jpg)

<details>
<summary>text_image</summary>

Nuclear matrix Cytoplasm
Cell membrane Lipid & ER
Nucleolus Nuclear membrane
</details>

D1  
![](images/812433999b008c3a2f39cad06c4d405cd4cb9dec8481df0b9ae74335e7cd3405.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing cellular structures with green and red fluorescent markers, labeled ROI1 and ROI2 (no text or symbols beyond labels)
</details>

D2  
![](images/480c005230905f21b5866fc4f5a82b8c20c2ecae471966c24fc4894f99c2bb7a.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | ROI1 | ROI2 |
| ------------------ | ---- | ---- |
| 1550               | 0.1  | 0.3  |
| 1600               | 0.2  | 0.4  |
| 1650               | 0.8  | 1.0  |
| 1700               | 0.3  | 0.5  |
| 1750               | 0.1  | 0.2  |
</details>

Fig.4 Bio-application of SRP spectroscopic imaging. (A1) SRP imaging of a single varicellazoster virus, $2 9 5 0 ^ { - 1 }$ cm. Scale bar: 2 μm. (A2) Single virus Raman spectrum at C-H region, acquired from a single virus in (A1). (B1) C-D imaging of heavy water cultured Bacteroides at $2 1 \bar { 7 } 0 ^ { - 1 }$ cm ((B1) On-resonance) or $2 3 6 1 ^ { - 1 }$ cm ((B2) Off-resonance). Scale bar: 3 μm. (C1) SRP imaging of fixed Mia-Paca2 cell immersed in glycerol-d8, at $2 9 5 0 ^ { - 1 }$ cm. Scale bar: 5 μm. (C2) Color coded chemical map through manual phasor segmentation of (C1). (D1) SRP spectroscopic imaging of OVCAR-5 tissue, cleared with glycerol-d8, at $1 6 5 0 ^ { - 1 }$ cm. (D2) Single pixel spectrum at the circled region of interests (ROI).

## References and Notes

1. C. W. Freudiger, W. Min, B. G. Saar, S. Lu, G. R. Holtom, C. He, J. C. Tsai, J. X. Kang, X. S. Xie, Label-free biomedical imaging with high sensitivity by stimulated Raman scattering microscopy. Science. 322, 1857–1861 (2008).  
W. Min, C. W. Freudiger, S. Lu, X. S. Xie, Coherent nonlinear optical imaging: beyond fluorescence microscopy. Annu. Rev. Phys. Chem. 62, 507–530 (2011).  
3. J.-X. Cheng, X. S. Xie, Vibrational spectroscopic imaging of living systems: An emerging platform for biology and medicine. Science. 350 (2015), doi:10.1126/science.aaa8870.  
4. Z. Zhao, Y. Shen, F. Hu, W. Min, Applications of vibrational tags in biological imaging by Raman microscopy. The Analyst. 142, 4018–4029 (2017).  
5. M. Ji, D. A. Orringer, C. W. Freudiger, S. Ramkissoon, X. Liu, D. Lau, A. J. Golby, I. Norton, M. Hayashi, N. Y. R. Agar, G. S. Young, C. Spino, S. Santagata, S. Camelo-Piragua, K. L. Ligon, O. Sagher, X. S. Xie, Rapid, Label-Free Detection of Brain Tumors with Stimulated Raman Scattering Microscopy. Sci. Transl. Med. 5, 201ra119-201ra119 (2013).  
6. D. A. Orringer, B. Pandian, Y. S. Niknafs, T. C. Hollon, J. Boyle, S. Lewis, M. Garrard, S. L. Hervey-Jumper, H. J. L. Garton, C. O. Maher, J. A. Heth, O. Sagher, D. A. Wilkinson, M. Snuderl, S. Venneti, S. H. Ramkissoon, K. A. McFadden, A. Fisher-Hubbard, A. P. Lieberman, T. D. Johnson, X. S. Xie, J. K. Trautman, C. W. Freudiger, S. Camelo-Piragua, Rapid intraoperative histology of unprocessed surgical specimens via fibre-laser-based stimulated Raman scattering microscopy. Nat. Biomed. Eng. 1, 0027 (2017).  
7. F. Hu, Z. Chen, L. Zhang, Y. Shen, L. Wei, W. Min, Vibrational Imaging of Glucose Uptake Activity in Live Cells and Tissues by Stimulated Raman Scattering. Angew. Chem. Int. Ed. 54, 9821–9825 (2015).  
8. L. Shi, C. Zheng, Y. Shen, Z. Chen, E. S. Silveira, L. Zhang, M. Wei, C. Liu, C. de Sena-Tomas, K. Targoff, W. Min, Optical imaging of metabolic dynamics in animals. Nat. Commun. 9, 2995 (2018).  
9. J. Li, J.-X. Cheng, Direct visualization of de novo lipogenesis in single living cells. Sci. Rep. 4, 6807 (2014).  
10. S. Yue, J. Li, S.-Y. Lee, H. J. Lee, T. Shao, B. Song, L. Cheng, T. A. Masterson, X. Liu, T. L. Ratliff, J.-X. Cheng, Cholesteryl Ester Accumulation Induced by PTEN Loss and PI3K/AKT Activation Underlies Human Prostate Cancer Aggressiveness. Cell Metab. 19, 393–406 (2014).  
11. J. Du, Y. Su, C. Qian, D. Yuan, K. Miao, D. Lee, A. H. C. Ng, R. S. Wijker, A. Ribas, R. D. Levine, J. R. Heath, L. Wei, Raman-guided subcellular pharmaco-metabolomics for metastatic melanoma cells. Nat. Commun. 11, 4830 (2020).  
12. H. J. Lee, Z. Chen, M. Collard, F. Chen, J. G. Chen, M. Wu, R. M. Alani, J.-X. Cheng, Multimodal Metabolic Imaging Reveals Pigment Reduction and Lipid Accumulation in Metastatic Melanoma. BME Front. 2021, 1–17 (2021).  
13. C. Chen, Z. Zhao, N. Qian, S. Wei, F. Hu, W. Min, Multiplexed live-cell profiling with Raman probes. Nat. Commun. 12, 3405 (2021).  
14. Y. Tan, J. Li, G. Zhao, K.-C. Huang, H. Cardenas, Y. Wang, D. Matei, J.-X. Cheng, Metabolic reprogramming from glycolysis to fatty acid uptake and beta-oxidation in platinum-resistant cancer cells. Nat. Commun. 13, 4554 (2022).  
15. X. Ge, F. C. Pereira, M. Mitteregger, D. Berry, M. Zhang, B. Hausmann, J. Zhang, A. Schintlmeister, M. Wagner, J.-X. Cheng, SRS-FISH: A high-throughput platform linking microbiome metabolism to identity at the single-cell level. Proc. Natl. Acad. Sci. U. S. A. 119, e2203519119 (2022).  
16. M. Zhang, W. Hong, N. S. Abutaleb, J. Li, P.-T. Dong, C. Zong, P. Wang, M. N. Seleem, J.-X. Cheng, Rapid Determination of Antimicrobial Susceptibility by Stimulated Raman Scattering Imaging of D2O Metabolic Incorporation in a Single Bacterium. Adv. Sci. Weinh. Baden-Wurtt. Ger. 7, 2001452 (2020).  
17. W. Rock, M. Bonn, S. H. Parekh, Near shot-noise limited hyperspectral stimulated Raman scattering spectroscopy using low energy lasers and a fast CMOS array. Opt. Express. 21, 15113–15120 (2013).  
18. C.-S. Liao, M. N. Slipchenko, P. Wang, J. Li, S.-Y. Lee, R. A. Oglesbee, J.-X. Cheng, Microsecond scale vibrational spectroscopic imaging by multiplex stimulated Raman scattering microscopy. Light Sci. Appl. 4, e265–e265 (2015).  
19. R. B. de Andrade, H. Kerdoncuff, K. Berg-Sørensen, T. Gehring, M. Lassen, U. L. Andersen, Quantum-enhanced continuous-wave stimulated Raman scattering spectroscopy. Optica. 7, 470–475 (2020).  
20. Z. Xu, K. Oguchi, Y. Taguchi, S. Takahashi, Y. Sano, T. Mizuguchi, K. Katoh, Y. Ozeki, Quantumenhanced stimulated Raman scattering microscopy in a high-power regime. Opt. Lett. 47, 5829–5832 (2022).  
21. L. Wei, Z. Chen, L. Shi, R. Long, A. V. Anzalone, L. Zhang, F. Hu, R. Yuste, V. W. Cornish, W. Min, Super-multiplex vibrational imaging. Nature. 544, 465–470 (2017).  
22. L. Wei, W. Min, Electronic Preresonance Stimulated Raman Scattering Microscopy. J. Phys. Chem. Lett. 9, 4294–4301 (2018).  
23. M. Zhuge, K.-C. Huang, H. J. Lee, Y. Jiang, Y. Tan, H. Lin, P.-T. Dong, G. Zhao, D. Matei, Q. Yang, J.-X. Cheng, Ultrasensitive Vibrational Imaging of Retinoids by Visible Preresonance Stimulated Raman Scattering Microscopy. Adv. Sci. Weinh. Baden-Wurtt. Ger. 8, 2003136 (2021).  
24. C. Zong, R. Premasiri, H. Lin, Y. Huang, C. Zhang, C. Yang, B. Ren, L. D. Ziegler, J.-X. Cheng, Plasmon-enhanced stimulated Raman scattering microscopy with single-molecule detection sensitivity. Nat. Commun. 10, 5318 (2019).  
25. H. Xiong, L. Shi, L. Wei, Y. Shen, R. Long, Z. Zhao, W. Min, Stimulated Raman excited fluorescence spectroscopy and imaging. Nat. Photonics. 13, 412–417 (2019).  
26. H. Wang, Y. Fu, J.-X. Cheng, Experimental observation and theoretical analysis of Raman resonanceenhanced photodamage in coherent anti-Stokes Raman scattering microscopy. J. Opt. Soc. Am. B. 24, 544 (2007).  
27. S. Adhikari, P. Spaeth, A. Kar, M. D. Baaske, S. Khatua, M. Orrit, Photothermal Microscopy: Imaging the Optical Absorption of Single Nanoparticles and Single Molecules. ACS Nano. 14, 16414–16445 (2020).  
28. A. Gaiduk, M. Yorulmaz, P. V. Ruijgrok, M. Orrit, Room-Temperature Detection of a Single Molecule’s Absorption by Photothermal Contrast. Science. 330, 353–356 (2010).  
29. M. E. Long, R. L. Swofford, A. C. Albrecht, Thermal Lens Technique: A New Method of Absorption Spectroscopy. Science. 191, 183–185 (1976).  
30. D. Zhang, C. Li, C. Zhang, M. N. Slipchenko, G. Eakins, J.-X. Cheng, Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2, e1600521 (2016).  
31. Z. Li, K. Aleshire, M. Kuno, G. V. Hartland, Super-Resolution Far-Field Infrared Imaging by Photothermal Heterodyne Imaging. J. Phys. Chem. B. 121, 8838–8846 (2017).  
32. P. Fu, W. Cao, T. Chen, X. Huang, T. Le, S. Zhu, D.-W. Wang, H. J. Lee, D. Zhang, Super-resolution imaging of non-fluorescent molecules by photothermal relaxation localization microscopy. Nat. Photonics, 1–8 (2023).  
33. H. El-Kashef, The necessary requirements imposed on polar dielectric laser dye solvents—II. Phys. B Condens. Matter. 311, 376–379 (2002).  
34. E. J. Bowen, J. Sahu, The Effect of Temperature on Fluorescence of Solutions. J. Phys. Chem. 63, 4– 7 (1959).  
35. A. Soleilhac, M. Girod, P. Dugourd, B. Burdin, J. Parvole, P.-Y. Dugas, F. Bayard, E. Lacôte, E. Bourgeat-Lami, R. Antoine, Temperature Response of Rhodamine B-Doped Latex Particles. From Solution to Single Particles. Langmuir. 32, 4052–4058 (2016).  
36. M. Li, A. Razumtcev, R. Yang, Y. Liu, J. Rong, A. C. Geiger, R. Blanchard, C. Pfluegl, L. S. Taylor, G. J. Simpson, Fluorescence-Detected Mid-Infrared Photothermal Microscopy. J. Am. Chem. Soc. 143, 10809–10815 (2021).  
37. Y. Zhang, H. Zong, C. Zong, Y. Tan, M. Zhang, Y. Zhan, J.-X. Cheng, Fluorescence-Detected Mid-Infrared Photothermal Microscopy. J. Am. Chem. Soc. 143, 11490–11499 (2021).  
38. C. W. Freudiger, W. Yang, G. R. Holtom, N. Peyghambarian, X. S. Xie, K. Q. Kieu, Stimulated Raman scattering microscopy with a robust fibre laser source. Nat. Photonics. 8, 153–159 (2014).  
39. A. Gaiduk, P. V. Ruijgrok, M. Yorulmaz, M. Orrit, Detection limits in photothermal microscopy. Chem. Sci. 1, 343–350 (2010).  
40. S. Novais, M. S. Ferreira, J. L. Pinto, Determination of thermo-optic coefficient of ethanol-water mixtures with optical fiber tip sensor. Opt. Fiber Technol. 45, 276–279 (2018).  
41. M. Maggioni, V. Katkovnik, K. Egiazarian, A. Foi, Nonlocal transform-domain filter for volumetric data denoising and reconstruction. IEEE Trans. Image Process. Publ. IEEE Signal Process. Soc. 22, 119–133 (2013).  
42. A. Sauerbrei, Diagnosis, antiviral therapy, and prophylaxis of varicella-zoster virus infections. Eur. J. Clin. Microbiol. Infect. Dis. Off. Publ. Eur. Soc. Clin. Microbiol. 35, 723–734 (2016).  
43. P. H. C. Eilers, A perfect smoother. Anal. Chem. 75, 3631–3636 (2003).  
44. J. Yin, L. Lan, Y. Zhang, H. Ni, Y. Tan, M. Zhang, Y. Bai, J.-X. Cheng, Nanosecond-resolution photothermal dynamic imaging via MHZ digitization and match filtering. Nat. Commun. 12, 7097 (2021).  
45. Bialkowski, S. E., “Photothermal spectroscopy methods for chemical analysis”, Vol. 134 of Chemical Analysis: A Series of Monographs on Analytical Chemistry and Its Applications, J. D. Winefordner, ed., (John Wiley & Sons, Inc., 1996), pp. 290.  
46. Z. Cao, L. Jiang, S. Wang, M. Wang, D. Liu, P. Wang, F. Zhang, Y. Lu, All-glass extrinsic Fabry-Perot interferometer thermo-optic coefficient sensor based on a capillary bridged two fiber ends. Appl. Opt. 54, 2371–2375 (2015).

Acknowledgments: We thank Fátima C. Pereira from Centre for Microbiology and Environmental Systems Science University of Vienna for assisting with preparation of bacterial cells.

Funding: National Institutes of Health grant R35GM136223 (JXC)

Author contributions: J.X.C. conceived the concept of photothermal detection and supervised the research team; Y.Z. built the simulation model, designed and built the SRP imaging system; X.G. implemented the data analysis algorithm; Y.Z. and X.G. performed the imaging experiments and data analysis; J.Y. designed and implemented the matched filtering algorithm; H.N. designed and implemented the broadband detector; H.L. conceived the idea of introducing SHG probe laser; L.W. implemented the SHG probe laser; Y.T. prepared the Mia-Paca 2 cell sample; C.P.D prepared the OVCAR-5 tissue sample. Y.Z., X.G. and J.X.C. wrote the manuscript with input from all authors.

Competing interests: J.X.C. declares financial interests in Vibronix Inc. and Photothermal Spectroscopy Corp., which did not fund the study.

Data and materials availability: All data and image reconstruction codes are available upon reasonable request to the corresponding author (jxcheng@bu.edu (J.X.C.)).

## Science

NAAAS

## Supplementary Materials for

# Photothermally Detected Stimulated Raman Microscopy towards Ultrasensitive Chemical Imaging

Yifan Zhu, Xiaowei Ge, Hongli Ni, Jiaze Yin, Haonan Lin, Le Wang, Yuying Tan, Chinmayee V. Prabhu Dessai, Ji-Xin Cheng\*

\* Correspondence to: jxcheng@bu.edu

## This PDF file includes:

Materials and Methods

Figs. S1 to S9

Tables S1

References (15, 43-46)

## Materials

## Cell culture and sample preparation

SKOV3 (Cat#: HTB-77) and Mia Paca2 (Cat#: CRL-1420) cells were from the American Type Culture Collection (ATCC). Cells were cultured in high-glucose DMEM medium (Gibco) supplemented with 10% FBS and 100 units/mL penicillin/streptomycin and maintained in a humidified incubator with 5% CO2 supply at 37°C. After overnight seeding in a sterile 35 mm glass-bottom dish (Cellvis) or #1 cover glass (VWR), cells were fixed with 10% neutral buffered formalin for 30 min followed by 3 times PBS wash. Then the cells were covered with glycerol-d8 before sealing and imaging.

## Tissue sample preparation

A fresh ovarian tumor section was extracted from NU/J mouse (4 weeks old female homozygous for Foxn1nu) purchased from the Jackson Laboratory. The mouse was inoculated with OVCAR5-cisR cells. The sections were immediately fixed in a 10% formalin solution. The extracted tissue section was then washed using PBS solution and cryopreserved by incubation in 15% sucrose solution for 12 hours, followed by incubation in 30% sucrose solution overnight at room temperature. The tissue section was frozen at −80°C by embedding in OCT (Optimal Cutting Temperature) compound in a tissue mold. The tissue section was then sliced using a Microm HM525 cryostat at the Bio-Interface and Technologies Facility, Boston University, into 10 µm thick layers, each placed on separate glass slides and frozen at −80°C until the experiment. To prepare the samples for imaging, the tissue slides were washed using PBS solution to wash off the OCT. The tissue slides were then covered with glycerol-d8 before placing a coverslip to seal the glycerol-d8 covered tissue layer.

## Glycerol-agar (glycerol-d8-agar) medium preparation

1% (w/w) agar (Sigma Aldrich) was mixed with glycerol (or glycerol-d8, Sigma Aldrich), then microwaved for 2min to fully dissolve the agar.

## Nanoparticle, bacteria, and virus preparation

For 100 nm PMMA nanoparticles, 10 μL solution was mixed with warm glycerol-d8-agar medium, then sandwiched between two No.1 coverslips before imaging. For D2O cultured bacteroid (15), 10 μL solution of fixed bacteria was mixed with warm glycerol-agar medium, then sandwiched between two No.1 coverslips before imaging. Varicella zoster virus solution (Fisher Scientific) was dropped onto a No.1 coverslip and dried on top. The sample was covered with glycerol-d8, then sandwiched between two coverslips and sealed with nail polish before imaging.

## Methods

## Modeling the temperature change induced by SRS

To quantitatively evaluate the SRP effect, we built a model to simulate the heat deposition spatially and temporally. The SRS induced temperature change is dependent on the pulse width, pulse energy, laser repetition rate, and thermal properties (thermal conductivity, heat capacity, etc.) of the sample and the surrounding medium. First, the deposited energy by SRS is estimated by the modulation depth on the pump or Stokes beam along with the pulse energy. Then, to simulate the thermal conduction, the time domain and spatial domain are divided into finite elements for the calculation according to Fourier’s law: ???? ൌ െ???? ሺ???? ????ሻ ⁄ , where ???? is the conducted heat energy in the time window, ?? is the thermal conductivity, ?? is the surface area, ???? is the temperature difference between distance ????. The SRS on-off process induces a heating and cooling process at the focus. Heat transfer happens during both heating and cooling. During the heating process, the SRS pulses deposit heat to the sample instantaneously with a Gaussian distribution as the vibrational excited state relaxation time is much faster compared to the simulation time grid. Finally, with the heating estimated by the modulation depth and the thermal conduction calculated according to Fourier’s Law, the temperature spatial distribution at each time point is calculated. To simplify the model, an isotropic Gaussian SRS heating area is assumed. The simulation area is set to be a 48- layer model with increasing step size from the center to the edge (Fig. S1). The time step is set to be 200 ps, which is much smaller than the heat propagation time to ensure a converged result. DMSO has a heat conductivity of 0.2 W/(mꞏK). The laser parameters are set to 50% duty cycle, 80 MHz repetition rate, according to the commonly used SRS setting.

To predict the fluorescence change upon temperature rise, the excitation profile of two photon fluorescence was modeled as the normalized Gaussian point spread function of the objective. Weights based on the assumed

excitation profile were put onto the temperature rise of each layer, then multiplied by the −2%/K rate (34), to yield the fluorescence change.

## Measurement of temperature at the SRS focus

A fluorescence thermometer, Rhodamine B (−2%/K) (34), is introduced to measure the temperature rise at the SRS focus. 80 μM Rhodamine B dissolved in DMSO is sandwiched between two thin coverslips (No.1; Thermo Fisher) for the measurement. A dual-output synchronized laser source (InSight X3; Spectra-Physics) provides pump and Stokes beams, respectively. The Stokes beam is modulated by an acousto-optic modulator (1205c; Isomet Corporation) at 40 kHz with the first order beam to provide a 100% modulation depth. Then the pump and Stokes beams are chirped by 75 and 90 cm glass rods (SF57; Scott AG), respectively, to implement hyperspectral SRS under a spectral focusing scheme. The path length of the Stokes beams could be adjusted by a motorized delay line (X-LRM025A-KX13A, Zaber Technologies). The two beams are combined by a dichroic mirror (950 nm; Chroma) and then collinearly guided into a laser scanning microscope. To vibrationally excite the C-H bond in DMSO, the pump laser was set to 800 nm with the Stokes beam wavelength fixed at 1045 nm. These two beams could also simultaneously excite the two-photon fluorescence signal of Rhodamine B. A 40 water objective (numerical aperture (N.A.) = 0.8; Olympus) focused the two beams onto the sample, with power of 25 mW for pump and 50 mW for Stokes. The output light is collected in the forward direction by an oil condenser (N.A. = 1.4, Aplanat Achromat 1.4; Olympus) and a 75 mm A-coating focal lens (Thorlabs). A silicon photomultiplier (C14455-3050GA; Hamamatsu) module with a bandpass optical filter (RT570/20x; Chroma) and two short-pass filters (1000SP, 775SP; Thorlabs) is used to detect the fluorescence signal. The output of the silicon photomultiplier is recorded by a spectrometer (Moku:Lab, Liquid Instruments) for the analysis in Fig. 1F.

## SRP microscope

The SRP microscope is based on the SRS setup described in the previous section. Both pump and Stokes beams are modulated by two synchronized acousto-optic modulators outputting the first order beams, various duty cycles, and modulation frequency at 125 kHz. Besides, a 765 nm continuous probe laser (TLB6712-D; Spectral Physics) is added after the combining dichroic mirror by a polarized beam splitter to form a three beam copropagating colinear system (Fig. 2B). The three beams are guided to a two-dimensional galvo scanning unit (GVS002; Thorlabs), which is conjugated by a four-focal system to the back aperture of a 100× oil objective (N.A. = 1.49, UAPON100XOTIRF; Olympus). The N.A. of the condenser is adjusted to 0.4 to enable the detection of the thermal lensing signal. The detector is a broadband silicon photodiode (Hamamatsu) with 50-ohm resistance, a 22 kHz highpass radio frequency filer (Mini-circuits) and a 46 dB low noise amplifier (SA230-F5; Wayne). A tilted bandpass optical filter (FL780-10; Thorlabs) is mounted before on the detector to block the SRS beams and allow sole detection of the probe beam. The output signal is digitized by a fast data acquisition card (Alazar card, ATS9462; Alazar Technologies). In imaging the virus on a coverslip, the 1045-nm femtosecond laser output is sent to an LBO crystal to generate 522.5 nm SHG laser beam as the SRP probe. This femtosecond probe with reduced coherence length minimizes the interference from the medium/coverglass interface. When performing SRS imaging on the same setup, the probe laser is turned off. A 1.4 N.A. condenser is used to minimize the cross phase modulation background. The modulation on the pump is set to always on and the Stokes was modulated at around 2.25 MHz. After the condenser, two short-pass optical filters (980SP, Thorlabs) pass the pump beam to the photodiode. A laboratory-built resonant amplifier after the photodiode picks up the stimulated Raman loss signal. The photodiode output is sent to the lock-in amplifier (MFLI; Zurich) and the stimulated Raman loss signal is recorded with a data acquisition card (NI DAQ card, PCI-6363; National Instruments). The SRP system is electronically synchronized by a NI DAQ card. The NI DAQ card controls the galvo scanning unit and generates the transistor-transistor logic trigger to control the sampling of the Alazar card and the pixel trigger to control the function generator. The function generator generates rectangular waves with various duty cycles at 125 kHz in burst mode to control the two acousto-optic modulators to modulate the pump and Stokes pulse trains (Fig. S2). The amplified signal from the detector set is digitized by the Alazar card at a sampling frequency of 20 MHz and then sent to the host computer for further analysis.

## SRP signal digitization and processing

After recording the signal from each pixel, a Whittaker smoother removes the fluctuated baseline caused by variation in the transmission (43). Matched filtering is then applied to improve the SNR (44). Fourier transform on the baseline removed signal is applied to generate the signal spectrum. To reduce the out-of-frequency noise, a match multi-bandpass filter at up to seven harmonic frequencies of the modulation frequency is applied to the signal spectrum (Fig. S3). The width of the single bandpass filter is set to 13.89 kHz when the pixel dwell time is 72 μs.

The match-filtered spectrum is then inversely Fourier transformed back to the time domain. The SPR signal intensity of each pixel is calculated from the average peak-dip contrast of the processed time domain data.

## SRP imaging parameters

5 The modulation depth is measured with 5% duty cycle modulation, 50 mW and 20 mW for Stokes and pump, respectively. The virus image is acquired with 5% duty cycle modulation, 40 mW and 20 mW for Stokes and pump, respectively. The bacteria image is acquired with 10% duty cycle modulation, 30 mW and 20 MW for Stokes and pump, respectively. The cell image is acquired with 10% duty cycle modulation, 30 mW and 15 mW for Stokes and pump,  
10 respectively. The tissue image is acquired with 5% duty cycle modulation, 30 mW and 10 mW for Stokes and pump, respectively. All powers are measured before the microscope.

## Phasor analysis

Phasor analysis was performed with the standardized phasor analysis plug-in in ImageJ (1.49v). 15 The phasor domain segmentation was performed manually to maximize the separation of different components as well as the integrity of each component.

A  
![](images/fde2949dd39d95fb32691bf5f7fd1fea17908d7f2973afc844c2b2609707f497.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["SRS on"] --> B["Vibrational transition"]
  B --> C["Excited state relaxation"]
  C --> D["Heat diffusion"]
```
</details>

B  
![](images/86fe07e0563b363a9004b2e8a9f2d59b0ed6ff986834c47f2ca4a4f63ebe4a71.jpg)

<details>
<summary>natural_image</summary>

3D diagram showing concentric wave patterns and a conical surface with a red arrow pointing to a small red dot (no text or symbols)
</details>

$$
d Q = - k A \frac {d T}{d r} = - k (4 \pi r ^ {2}) \frac {d T}{d r}
$$

Fig. S1. SRP simulation model. The system is gridded into concentric spherical shells. The red arrow indicates the thermal propagation direction.

![](images/062a4ba6ec4d1822efc6cfe18d5d3d30c7eeec680f48b596e489eeb47c967fa8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  Light --> AOM
  AOM -->|1st order| Galvo_Unit
  Galvo_Unit --> Sample
  Sample --> Photodiode
  Photodiode --> Alazar_DAQcard
  Alazar_DAQcard --> DataTransfer["Data transfer"]
  DataTransfer --> Host_PC["Host PC"]
  Control --> NI_DAQ
  NI_DAQ -->|2D Scanning| Galvo_Unit
  FunctionGenerator --> AOM
  ModulationBurst --> AOM
  DataTransfer --> Alazar_DAQcard
  TriggerControl --> Alazar_DAQcard
```
</details>

Pixel Trigger  
Fig. S2. Electronic control and data acquisition flow in the SRP microscope.

![](images/bfded9a6b4640b73a9459fd008c4f5df044c37b8f5a3cad789cea0b95f132b98.jpg)  
Fig. S3. A thermal dynamic trace from SRP measurement and under different stages of data processing. The signal is acquired from a single 100 nm PMMA nanoparticle at 2950 cm-1 immersed in glycerol-d8. FFT: fast Fourier transform; iFFT: inverse fast Fourier transform.

Temperature gradient  
![](images/8a077164e58db2a95130e1f7e3ff8549a5439f9ccb01a8c46bbb4ae5a903890e.jpg)

<details>
<summary>line chart</summary>

| x / μm | Glycerol | Water |
| ------ | -------- | ----- |
| -3.0   | 0.00     | 0.00  |
| -2.0   | 0.00     | 0.00  |
| -1.0   | 0.00     | 0.00  |
| 0.0    | 0.16     | 0.08  |
| 1.0    | 0.00     | 0.00  |
| 2.0    | 0.00     | 0.00  |
| 3.0    | 0.00     | 0.00  |
</details>

Shape of thermal lens  
![](images/291ffb32a3e74a9019428971a701c905cd9d3130d46851d9b986aebb564048d3.jpg)

<details>
<summary>line chart</summary>

| x / µm | Glycerol       | Water         |
| ------ | -------------- | ------------- |
| -3     | 0.0            | 0.0           |
| -2     | ~0.0           | ~0.0          |
| -1     | ~-0.5          | ~-0.5         |
| 0      | ~-2.8e-5       | ~-1.0e-5      |
| 1      | ~-0.5          | ~-0.5         |
| 2      | ~0.0           | ~0.0          |
| 3      | 0.0            | 0.0           |
</details>

Fig. S4. Simulation results for the shape of temperature gradient and thermal lens induced by a 100 nm PMMA particle in glycerol or water.

![](images/dc855058bed58c1460ddcc2ebeba719a79fcc1996b72e0f254a141a79ed39710.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / V |
| ------------------ | ------------- |
| 2800               | ~0.0          |
| 2900               | ~0.9          |
| 3000               | ~0.1          |
| 3100               | ~0.0          |
</details>

![](images/9d46e1dcd4182b2ae760081d6bcf5e8ea8c009ee4724e8ce2910b8af15f0ad88.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / a.u. |
| ------------------ | ---------------- |
| 2800               | 0                |
| 2900               | 280              |
| 3000               | 50               |
| 3100               | 0                |
</details>

Fig. S5. Complete data set of LOD measurement of DMSO dissolved in DMSO-d6 with SRP (A) and SRS (B). Unit of concentration: mM.

![](images/b51e35209be4222da735ee2e4f734dc634a3bfdf6aa0f4ae6bd7f0349399833a.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / a.u. (2) | Intensity / a.u. (0.66) | Intensity / a.u. (0.22) | Intensity / a.u. (0) |
| ------------------ | -------------------- | ----------------------- | ----------------------- | ------------------- |
| 2050               | ~0.05                | ~0.04                   | ~0.03                   | ~0.03               |
| 2100               | ~0.15                | ~0.12                   | ~0.10                   | ~0.08               |
| 2150               | ~0.22                | ~0.18                   | ~0.15                   | ~0.12               |
| 2200               | ~0.10                | ~0.08                   | ~0.07                   | ~0.06               |
| 2250               | ~0.08                | ~0.06                   | ~0.05                   | ~0.04               |
| 2300               | ~0.05                | ~0.04                   | ~0.03                   | ~0.03               |
</details>

![](images/103818a483d6d6562fcd30d6155ad58d8dc2e222832051eb0c1176d947520add.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / a.u. (27) | Intensity / a.u. (9) | Intensity / a.u. (3) |
| ------------------ | --------------------- | -------------------- | -------------------- |
| 2050               | ~0.0                  | ~0.0                 | ~0.0                 |
| 2100               | ~0.2                  | ~0.2                 | ~0.2                 |
| 2150               | ~0.3                  | ~0.3                 | ~0.3                 |
| 2200               | ~0.2                  | ~0.2                 | ~0.2                 |
| 2250               | ~0.1                  | ~0.1                 | ~0.1                 |
| 2300               | ~0.0                  | ~0.0                 | ~0.0                 |
</details>

![](images/35c8a984379a618d92e61d1d584bc2826448689fe51fd970e96c96bb17bc08ad.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / a.u. (162) | Intensity / a.u. (54) | Intensity / a.u. (18) | Intensity / a.u. (6) | Intensity / a.u. (2) | Intensity / a.u. (0.66) | Intensity / a.u. (0.22) |
| ------------------ | ---------------------- | --------------------- | --------------------- | -------------------- | -------------------- | ----------------------- | ----------------------- |
| 2050               | ~0.0                   | ~0.0                  | ~0.0                  | ~0.0                 | ~0.0                 | ~0.0                    | ~0.0                    |
| 2100               | ~0.1                   | ~0.05                 | ~0.05                 | ~0.05                | ~0.05                | ~0.05                   | ~0.05                   |
| 2150               | ~2.4                   | ~0.9                  | ~0.3                  | ~0.1                 | ~0.1                 | ~0.1                    | ~0.1                    |
| 2200               | ~0.1                   | ~0.05                 | ~0.05                 | ~0.05                | ~0.05                | ~0.05                   | ~0.05                   |
| 2250               | ~0.0                   | ~0.0                  | ~0.0                  | ~0.0                 | ~0.0                 | ~0.0                    | ~0.0                    |
| 2300               | ~0.0                   | ~0.0                  | ~0.0                  | ~0.0                 | ~0.0                 | ~0.0                    | ~0.0                    |
</details>

![](images/d011d4383df2b8e46cbcb5e4baf32e4211755773539b1ebcb8fc2ae97bd51464.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | 1M    | 243mM | 81mM | 27mM | 9mM  | 3mM  |
| ------------------ | ----- | ----- | ---- | ---- | ---- | ---- |
| 2050               | ~0.0  | ~0.0  | ~0.0 | ~0.0 | ~0.0 | ~0.0 |
| 2100               | ~6.0  | ~1.5  | ~1.5 | ~0.5 | ~0.5 | ~0.5 |
| 2150               | ~0.5  | ~0.5  | ~0.5 | ~0.5 | ~0.5 | ~0.5 |
| 2200               | ~0.0  | ~0.0  | ~0.0 | ~0.0 | ~0.0 | ~0.0 |
| 2250               | ~0.0  | ~0.0  | ~0.0 | ~0.0 | ~0.0 | ~0.0 |
| 2300               | ~0.0  | ~0.0  | ~0.0 | ~0.0 | ~0.0 | ~0.0 |
</details>

Fig. S6. LOD of 1,7-Octadiyne in SRP and SRS measurement. (A-B). SRP (A) or SRS (B) signal with a gradient concentration of 1,7-Octadiyne dissolved in DMSO. Concentration unit: mM. Insert shows the signal intensity as a function of concentration. (C-D). The complete data set of LOD measurement with SRP (C) and SRS (D). Unit of concentration: mM.

![](images/e2586bdb6830696cf922698bd765026e94042de5033357b1722bd9dc91ba44b5.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / a.u. (140) | Intensity / a.u. (46.7) | Intensity / a.u. (15.6) | Intensity / a.u. (0) |
| ------------------ | ---------------------- | ----------------------- | ----------------------- | -------------------- |
| 2050               | ~0                     | ~0                      | ~0                      | ~0                   |
| 2100               | ~10                    | ~5                      | ~5                      | ~0                   |
| 2150               | ~35                    | ~15                     | ~10                     | ~0                   |
| 2200               | ~5                     | ~10                     | ~5                      | ~0                   |
| 2250               | ~0                     | ~5                      | ~0                      | ~0                   |
| 2300               | ~0                     | ~0                      | ~0                      | ~0                   |
</details>

LOD = 15.5 mM

![](images/8a5d7656cbfb70d8652dbbba526f676eeba740bd86889f4ed6475d1de28b6195.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / a.u. (140) | Intensity / a.u. (46.7) | Intensity / a.u. (15.6) | Intensity / a.u. (0) |
| ------------------ | ---------------------- | ----------------------- | ----------------------- | -------------------- |
| 2050               | ~0.1                   | ~0.1                    | ~0.1                    | ~0.1                 |
| 2100               | ~0.3                   | ~0.2                    | ~0.2                    | ~0.2                 |
| 2150               | ~0.2                   | ~0.2                    | ~0.2                    | ~0.2                 |
| 2200               | ~0.2                   | ~0.2                    | ~0.2                    | ~0.2                 |
| 2250               | ~0.1                   | ~0.1                    | ~0.1                    | ~0.1                 |
| 2300               | ~0.1                   | ~0.1                    | ~0.1                    | ~0.1                 |
</details>

LOD = 32.3 mM

![](images/a6d3881652c7f35cba6a6128db28109c9a370215998d65680c05ae052e3c4898.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / a.u. (14000) | Intensity / a.u. (3780) | Intensity / a.u. (1260) | Intensity / a.u. (420) | Intensity / a.u. (140) | Intensity / a.u. (46.7) | Intensity / a.u. (15.6) | Intensity / a.u. (0) |
| ------------------ | ------------------------ | ----------------------- | ----------------------- | ---------------------- | --------------------- | ---------------------- | ---------------------- | ------------------- |
| 2050               | ~0                       | ~0                      | ~0                      | ~0                     | ~0                    | ~0                     | ~0                     | ~0                  |
| 2100               | ~500                     | ~100                    | ~200                    | ~100                   | ~50                   | ~50                    | ~50                    | ~50                 |
| 2150               | ~5500                    | ~1200                   | ~1000                   | ~50                    | ~50                   | ~50                    | ~50                    | ~50                 |
| 2200               | ~0                       | ~0                      | ~0                      | ~0                     | ~0                    | ~0                     | ~0                     | ~0                  |
| 2250               | ~1200                    | ~150                    | ~50                     | ~50                    | ~50                   | ~50                    | ~50                    | ~50                 |
| 2300               | ~0                       | ~0                      | ~0                      | ~0                     | ~0                    | ~0                     | ~0                     | ~0                  |
</details>

![](images/afa1c0ffcbcfa3f36521f6bad3505153df8740700ee206e9504d4bae53242d70.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity / a.u. |
| ------------------ | ---------------- |
| 2100               | ~0               |
| 2150               | ~17              |
| 2250               | ~2               |
| 2300               | ~0               |
</details>

Fig.S7 LOD of DMSO-d6 in SRP and SRS measurement. (A-B). SRP (A) or SRS (B) signal with a gradient concentration of DMSO-d6 dissolved in DMSO. Concentration unit: mM. Insert shows the signal intensity as a function of concentration. (C-D). The complete data set of LOD measurement with SRP (C) and SRS (D).

![](images/d1bcbf413c820244c88cbc436f8cf0488bdb4019a65d0a4cd0d34846190e729a.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Background | PMMA |
| ------------------ | ---------- | ---- |
| 2850               | 0.65       | 0.63 |
| 2900               | 0.85       | 1.00 |
| 2950               | 0.90       | 1.45 |
| 3000               | 0.75       | 0.70 |
| 3050               | 0.65       | 0.63 |
</details>

Fig. S8. SRP spectrum of a single 100 nm PMMA nanoparticle at the C-H region.

A  
![](images/6603e4e57ad2e407aa3d45094f737d6d754b65500a397e9504576f6da9f88d20.jpg)

<details>
<summary>text_image</summary>

Nucleolus
Nuclear matrix
Nuclear membrane
Background
Cell membrane
Lipid and ER
Cytoplasm
</details>

B  
![](images/3c8acfa7e0337371fdd287dcecb91f0256f66a34f24e6dfed115faac63ac7165.jpg)

<details>
<summary>text_image</summary>

Lipid and ER
Nuclear matrix
Cytoplasm
Cell membrane
Nucleolus
Nuclear membrane
</details>

C  
![](images/0d1128207f21599a9d158031f3a7f67b13fa08b6353a88dda059ee8c5d61ef0d.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Lipid and ER | Nuclear matrix | Nucleolus | Cytoplasm | Cell membrane | Nuclear membrane |
| ------------------ | ------------ | -------------- | --------- | --------- | ------------- | ---------------- |
| 2850               | 0.0          | 0.0            | 0.0       | 0.0       | 0.0           | 0.0              |
| 2900               | 0.6          | 0.4            | 0.5       | 0.4       | 0.3           | 0.2              |
| 2950               | 1.0          | 1.0            | 1.0       | 1.0       | 1.0           | 1.0              |
| 3000               | 0.4          | 0.4            | 0.4       | 0.4       | 0.4           | 0.4              |
| 3050               | 0.0          | 0.0            | 0.0       | 0.0       | 0.0           | 0.0              |
</details>

Fig. S9. Phasor analysis for the SRP image of glycerol-d8 immersed Mia PACA-2 cells. (A). Segmentation of the SRP image in the phasor domain. (B). Mapping of each component from phasor analysis. (C). The SRP spectrum at C-H region for each component.

<table><tr><td>Thermal property</td><td>Unit</td><td>DMSO</td><td>hexane</td><td>glycerol</td><td>water</td></tr><tr><td>Heat Capacity</td><td>J/(kg·K)</td><td>1966</td><td>2251</td><td>2400</td><td>4184</td></tr><tr><td>Thermal conductivity</td><td>W/(m·K)</td><td>0.200</td><td>0.124</td><td>0.283</td><td>0.598</td></tr><tr><td>Thermo-optic coefficient dn/dT (10-4)</td><td>K-1</td><td>-4.93 (33)</td><td>-5.20 (43)</td><td>-2.30 (44)</td><td>-1.13 (40)</td></tr><tr><td>Refractive index</td><td></td><td>1.479</td><td>1.375</td><td>1.473</td><td>1.333</td></tr><tr><td>Relative signal intensity</td><td>a.u.</td><td>10.3</td><td>8.83</td><td>4.27</td><td>1</td></tr></table>

Table S1. Thermal and thermo-optic properties and estimated relative signal intensity of the mediums related to the study.