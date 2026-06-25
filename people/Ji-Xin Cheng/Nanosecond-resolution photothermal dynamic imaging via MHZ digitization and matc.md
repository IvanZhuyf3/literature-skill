ARTICLE

![](images/1323bb23cb79f1e0ec4a7768d7ba4ad5dd3eeb25a3d06af0dec0434484605742.jpg)

Check for updates

https://doi.org/10.1038/s41467-021-27362-w

OPEN

# Nanosecond-resolution photothermal dynamic imaging via MHZ digitization and match filtering

Jiaze Yin 1,2,5, Lu Lan1,2,5, Yi Zhang3, Hongli Ni1,2, Yuying Tan4, Meng Zhang1,2, Yeran Bai 1,2 & Ji-Xin Cheng 1,2,3,4✉

Photothermal microscopy has enabled highly sensitive label-free imaging of absorbers, from metallic nanoparticles to chemical bonds. Photothermal signals are conventionally detected via modulation of excitation beam and demodulation of probe beam using lock-in amplifier. While convenient, the wealth of thermal dynamics is not revealed. Here, we present a lock-in free, mid-infrared photothermal dynamic imaging (PDI) system by MHz digitization and match filtering at harmonics of modulation frequency. Thermal-dynamic information is acquired at nanosecond resolution within single pulse excitation. Our method not only increases the imaging speed by two orders of magnitude but also obtains four-fold enhancement of signal-to-noise ratio over lock-in counterpart, enabling high-throughput metabolism analysis at single-cell level. Moreover, by harnessing the thermal decay difference between water and biomolecules, water background is effectively separated in midinfrared PDI of living cells. This ability to nondestructively probe chemically specific photo thermal dynamics offers a valuable tool to characterize biological and material specimens.

Photothermal microscopy is a versatile analytical tool togauge optical absorption with extremely high sensitivity1. gauge optical absorption with extremely high sensitivity1. Unlike conventional spectroscopic methods that measure light attenuation, photothermal detection acquires absorption information by probing the thermal effect using a second light beam outside the absorption band. Its high sensitivity majorly benefits from the much-reduced background by employing a modulated heating beam and heterodyne detection of a frequency-shifted probe beam with a lock-in amplifier2,3. Using such a detection scheme, shot-noise limited imaging of single gold nanoparticles of 1.4 nm diameter has been demonstrated2, and the single-molecule detection limit has been reported4. Recently, by employing a mid-infrared (mid-IR) laser as the pump source and visible light as the probe, a label-free vibrational spectroscopic imaging modality termed mid-infrared photothermal (MIP) microscopy has been demonstrated5. It obtains the mid-IR absorption contrast from a transient thermal field that is tightly confined in the vicinity of the absorber. By probing such a field with focused visible light, a submicron spatial resolution as good as 300 nm is achieved6. This new imaging modality not only enriches the photothermal techniques with enormous molecular fingerprint information, but also overcomes the limitations in conventional mid-IR absorption microscopy and near-field IR approaches. MIP microscopy is emerging as a valuable tool for biological and material science7. It enables IR spectroscopic imaging at the submicron spatial resolution, empowering a broad spectrum of applications in both research and industry, including but not limited to non-contact material characterization8–10, biomolecular mapping11,12, protein dynamics and aggregation in neurons13,14, bacterial response to antibiotics15, single virus detection16 and imaging of metabolism in living cells and other organisms5,17,18. Since the first demonstration of highperformance MIP imaging in 20165, it has been quickly commercialized into a product19, and the field expands with innovations, including wide-field detection20, optical phase detection21–23, photoacoustic detection18,24, and synergistic integration with Raman spectroscopy11.

Yet, despite the success in the development and applications of photothermal microscopy1, the wealth and valuable information about an object’s thermal dynamics along with the transient photothermal process is rarely explored. In principle, lock-inbased photothermal heterodyne imaging (PHI) can reveal thermal diffusivity of the medium through phase detection in the lock-in amplifier. This method25,26 has enabled various applications, including observing superconducting transition 27 tissue differentiation26,28. and revealing membrane interfaces29. However, lock-in demodulation at the fundamental modulation frequency loses the temporal resolution and all the higher-order harmonics of the photothermal signal. Therefore, this method is only capable of quantitatively retrieving thermal information for a well-defined model under ideal impulse or sinusoidal excitation, and it has a limited dynamic range for depicting the decay difference30. Thus, it is hard to use PHI to interpret a complex mid-infrared photothermal signal that originates not only from the absorbers but also from the embedding medium with distinct decay lifetimes. In the temporal domain, time-gated approaches, including digital boxcar averager or optical gating with a short pulse laser, can resolve the dynamics by tuning the delay between the probe point and excitation laser pulse20,21,31. Nevertheless, acquiring a complete thermal-dynamic profile depicting the temperature rise and decay at nanosecond resolution requires tedious, repetitive measurements, making it slow and unsuitable for non-repetitive transient processes.

In this work, we demonstrate a mid-IR photothermal dynamic imaging (PDI) system with nanosecond-scale temporal resolution and covering a bandwidth larger than 25 MHz. By using a wideband voltage amplifier and a megahertz digitizer, the photothermal dynamic response to a single IR pulse excitation is recorded. Combined with digital signal processing to filter out the noise outside the fundamental IR modulation frequency and its harmonics, PDI achieves more than a four-fold improvement in signal-to-noise ratio (SNR) than lock-in-based PHI. With these improvements, mid-IR PDI allowed high throughput metabolism analysis at the single bacterium level with an imaging speed nearly two orders of magnitude faster than the lock-in counterpart. Moreover, mid-IR PDI retrieves the transient thermal field evolvement and gives out information on the target’s physical properties and micro-environment. Using PDI, we mapped the photothermal dynamics of various organelles inside a cancer cell. Distinct from the macroscopic observation on the homogeneous thermal response of tissue or cell as a whole26,31, we show a highly heterogeneous, chemical-dependent thermal environment inside a cell. Furthermore, by harnessing the thermal decay difference between water and biomolecules, cellular components that are buried by the water background in conventional PHI can be differentiated in PDI based on their time-resolved signatures. Collectively, PDI enables direct detection of the transient pho tothermal process with nanosecond-level temporal resolution. Together with mid-IR excitation, PDI as a new approach allows for nondestructive investigation of a sample’s intrinsic chemica and physical properties and is broadly applicable to biology and material science.

## Results

Modeling the transient mid-infrared photothermal effect. The photothermal phenomenon originates from the transformation of absorbed photon energy into heat through a nonradiative relaxation31. Under a pulsed laser excitation with a duration shorter than the thermal relaxation time, the absorbed energy forms a localized thermal field around the absorber. This thermal field induces concurrent thermoelastic deformation that modifies the local optical refractive index through local density change, which can be detected as a time-dependent photothermal signal through optical scattering. Compared with PHI detection of nanoparticles32, the MIP thermal dynamics are distinct in two aspects. First, the MIP absorbers, specifically in the living system, cannot be simply modeled as point heat sources in a medium. For instance, targets like lipid droplets, protein aggregation, cytoplasm are bulky. The thermal dynamics are affected by both the absorbers and local medium collectively. Second, given the water absorption in the mid-IR range, both the absorbers and the aqueous medium will experience temperature elevation, which affects the contrast.

In a thermo-conductive environment, the evolvement of an absorber’s local temperature (T) under a mid-IR pump is governed by the heat transfer equation33:

$$
m C _ {s} \frac {\mathrm{d} T}{\mathrm{d} t} = Q _ {\mathrm{abs}} - Q _ {\mathrm{diss}} \tag {1}
$$

where m and C represent the mass and specific heat capacity of the absorber; dT/dt is the temperature change over time; $( Q _ { \mathrm { a b s } } -$ $Q _ { \mathrm { d i s s } } )$ denotes the energy flux, representing the rate difference between the absorbed and dissipated energies. $Q _ { \mathrm { a b s } }$ can be approximated by $I _ { \mathrm { I R } } ( t ) \sigma _ { \mathrm { a b s } } .$ where $\dot { I } _ { \mathrm { I R } } ( t )$ represents the incident IR intensity over the IR pulse; $\sigma _ { \mathrm { a b s } }$ represents the IR absorption cross-section. The heat dissipation follows Newton’s law, i.e., $Q _ { \mathrm { d i s s } }$ is driven by the temperature gradient and given by $( h S [ T ( t ) - T _ { \mathrm { e n v } } ] )$ , where h and S represent the heat transfer coefficient and effective transfer surface area from specimen to environment, respectively. $( T ( t ) - T _ { \mathrm { e n v } } )$ is the time-dependent temperature difference between the absorber and ambient environment $T _ { \mathrm { e n v } } .$ We note that the heat transfer model here is valid when the time scale of the heat dissipation is longer than sub-nanosecond34, which matches with the pulse duration of most mid-IR excitations.

![](images/6b75fd94e15d779a41e1bcff96baa7adcf10ae08924755179ada68da9dbfed64.jpg)

<details>
<summary>line chart</summary>

| Metric         | Value |
| -------------- | ----- |
| Pulse width    | 900 ns |
| Period         | 10 µs |
| ΔT             | Heating |
| Cooling        |       |
| Lock-in recovered |       |
| FFT            | 1st   |
| FFT            | 2nd   |
| FFT            | 3rd   |
| FFT            | 4th   |
| FFT            | 5th   |
| FFT            | 10th  |
| FFT            | 15th  |
</details>

![](images/7d6876d4d20daadea13c31b77588e1f7dac4550d0b407114327365d45a0d6386.jpg)

<details>
<summary>text_image</summary>

b
Mid-IR
MCT
DM
RL
PD2
Scan stage
OL
BS
Probe
PD1
</details>

![](images/545f93aa4e8bd4c97f33345eeccdc53d6237419dacd1e1df1b532b68f94cdbdc.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  DAQ --> CH1
  DAQ --> CH2
  DAQ --> CH3
  PC --> CH1
  PC --> CH2
  PC --> CH3
  MCT --> CH1
  LowPass["Low pass"] --> CH2
  AMP --> CH3
  ScanStage["Scan Stage"] --> CH3
  QCL --> CH3
  PD --> AMP
```
</details>

![](images/717a50fa7f699737d34c39fc11febee5e2747251dacb8dd4f02f50201b1faac1.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Amplitude (mV) |
| --------- | -------------- |
| 0         | 0              |
| 5         | -40            |
| 10        | 0              |
| 15        | -40            |
| 20        | 0              |
| 25        | -40            |
| 30        | 0              |
| 35        | -40            |
| 40        | 0              |
</details>

![](images/563bba4c78bd157557b77f0ee87c88d9e0295a4c3fe08e05ac63062fe2787ec8.jpg)

<details>
<summary>bar chart</summary>

| Frequency (MHz) | Amplitude (mV) |
| --------------- | -------------- |
| 0.0             | 8.5            |
| 0.1             | 6.5            |
| 0.2             | 4.5            |
| 0.3             | 3.5            |
| 0.4             | 2.5            |
| 0.5             | 2.0            |
| 0.6             | 1.5            |
| 0.7             | 1.0            |
| 0.8             | 0.8            |
| 0.9             | 0.6            |
| 1.0             | 0.5            |
| 1.1             | 0.4            |
| 1.2             | 0.3            |
| 1.3             | 0.2            |
| 1.4             | 0.1            |
| 1.5             | 0.1            |
| 1.6             | 0.1            |
| 1.7             | 0.1            |
| 1.8             | 0.1            |
| 1.9             | 0.1            |
| 2.0             | 0.1            |
| 2.1             | 0.1            |
| 2.2             | 0.1            |
| 2.3             | 0.1            |
| 2.4             | 0.1            |
| 2.5             | 0.1            |
| 2.6             | 0.1            |
| 2.7             | 0.1            |
| 2.8             | 0.1            |
| 2.9             | 0.1            |
| 3.0             | 0.1            |
</details>

![](images/4687bd47e0e21f423258de3fcf01ffa8748251ac8cfa0b40a94ebefd92663e10.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Amplitude (mV) |
| --------- | -------------- |
| 0         | 0              |
| 1         | 0              |
| 2         | -40            |
| 3         | -10            |
| 4         | 0              |
| 5         | 0              |
| 6         | 0              |
| 7         | 0              |
| 8         | 0              |
| 9         | 0              |
| 10        | 0              |
</details>

Fig. 1 Principle and schematic of photothermal dynamic imaging. a The simulated photothermal dynamics of a particle absorber under a pulsed IR pump. The absorber has a decay constant of 400 ns; the IR source has a repetition rate of 100 kHz and a pulse duration of 900 ns. b PDI setup schematics. A pulsed mid-IR beam is provided by a QCL and focused on the sample with a reflective objective lens (RL). The counter-propagated probe beam provided by a continuous-wave visible laser is focused by a water immersion objective lens (OL). Backscattered probe photons are collected with a 50/50 beam splitter (BS), forward scattered probe photons are collected by the reflective objective and separated by a dichroic mirror (DM). Both forward and backward probes are collected and sent to silicon photodiodes (PD) connected with a wideband voltage amplifier. A mercury cadmium telluride (MCT) detector is placed to monito the IR pulse. c Electronics diagram. A high-speed data acquisition (DAQ) card is used to collect photodiode signal after voltage amplifier (AMP), MCT signa and sample position synchronously. A computer (PC) is used to control and synchronize different instruments. d Digital signal processing procedure. The sample was a PMMA particle with 500-nm diameter under 1729 cm−1 excitation. Left panel, raw signal trace; middle panel, frequency domain distribution acquired via fast Fourier transform (FFT) and passband windows; right panel, filtered signal via inverse Fourier transform (IFFT). Match filtering is performed on the segment with 200 µs. Probe power on sample: 30 mW; IR average power measured before the objective lens: 5 mW.

During the heating process, $T ( t )$ can be derived by solving Eq. (1) with the initial condition $T ( 0 ) = T _ { \mathrm { e n v } }$ and assuming constant IR irradiation $I _ { \mathrm { I R } }$ and ambient tempearture $T _ { \mathrm { e n v } } { \mathrm { : } }$ ..

$$
T (t) = T _ {\text { env }} + \frac {I _ {\mathrm{IR}} \sigma_ {\mathrm{abs}}}{h S} (1 - \mathrm{e} ^ {- \frac {h S}{m C _ {s}} t}) \tag {2}
$$

When the IR pulse is finished, $Q _ { \mathrm { a b s } }$ becomes zero. The temperature change is only driven by $Q _ { \mathrm { d i s s } } .$ T t is then solved as

$$
T (t) = T _ {\text { env }} + \left(T _ {\max} - T _ {\text { env }}\right) \mathrm{e} ^ {- \frac {h S}{m C _ {s}} t} \tag {3}
$$

Here, $T _ { \mathrm { m a x } }$ is the maximal temperature of the absorber after heating ends. From this model, both the heating and cooling process can be described as exponential processes. As an analogy to a resistor–capacitor (RC) circuit, $m C _ { s }$ can be considered as the thermal capacitor and $1 / h S$ as the thermal resistor33. The interplay of these two items results in a time constant $\tau =$ $m C _ { s } \mathrm { ~ } \mathrm { ~ / ~ } h \dot { S } . \mathrm { ~ A ~ }$ simulation of this transient process is illustrated in Fig. 1a middle row, assuming τ = 400 ns. For absorbers with large heat capacity, such as bulky water and large particles, their time constants are expected to be large. Meanwhile, hS is mostly related to the heat transfer capability of the embedding medium and the geometry of absorbers. Therefore, the thermal response is tightly connected to the physical properties of both the absorber and the environment, which can vary greatly in a heterogeneous system like a biological cell. Note that a single exponential decay model is employed for illustration. For complex sample configurations, where heat conduction inside absorber or micro-environment needs to be considered, the assumption that constant ambient temperature $T _ { \mathrm { e n v } }$ no longer holds. For those cases, the transient photothermal dynamics has a superimposed decay with multiple lifetimes, and models that study complex decays in other fields, such as fluorescent lifetime imaging, can be applied35.

In the frequency domain, the photothermal signal produced by IR pulses at a repetition rate of $f _ { \mathrm { I R } }$ can be treated as a Fourier synthesis of Eqs. (2) and (3) and contains harmonics of $f _ { \mathrm { I R } } ,$ as shown in the simulation of absorbers with τ of 400 ns (Fig. 1a, bottom row). Harmonics are spread out widely in the frequency domain, whose amplitude and phase delay can be described with the frequency response function $H ( f )$ by analogy with a RC circuit. The relative amplitude of harmonic at the frequency f with given decay constant τ is calculated by:

$$
| H (f) | = \left| \frac {1}{1 + j 2 \pi \tau f} \right| \tag {4}
$$

Large τ results in weak harmonics at high frequency, whereas fast decay signals exhibit strong harmonic components. The conventional lock-in only recovers the amplitude of the first harmonic at low frequency and misses all higher harmonics, which not only sacrifices the sensitivity36 for low duty signal detection, but also causes contrast distortion in a heterogeneous sample with different thermal responses. Latterly we show that in the mid-infrared PHI of living cells using lock-in, the water background maximizes at the first harmonic, and it overwhelms the weak signal from the small organelles. To address these difficulties, we have developed a PDI system that is able to detect both fundamental and harmonic components in the frequency domain.

PDI instrumentation and data processing. A schematic of our PDI system is shown in Fig. 1b. A pulsed mid-IR pump beam is provided by a quantum cascade laser (QCL) and focused on the sample with a reflective objective lens (RL). A counter-propagated probe beam from a continuous-wave 532 nm laser is focused by a water immersion objective lens (OL). Backscattered probe photons are collected with the same OL and separated with a 50/50 beam splitter; forward scattered probe photons are collected by the reflective objective and separated by a dichroic mirror. Both forward and backward probe photons are collected and sent to silicon photodiodes (PD) connected with a wideband voltage amplifier worked in AC coupling (10 Hz–100 MHz). In the following experiments, the photothermal signal was detected on backward scattering for nanoparticle and bacteria samples; on forward scattering for cell samples. The voltage signal is filtered with a low pass filter with a cut-off frequency of 25 MHz and sent to a high-speed digitizer (DAQ) with a sampling rate of 50 million samples per second. Meanwhile, a mercury cadmium telluride (MCT) detector is placed to monitor the IR pulse, and the signal is digitized by the same DAQ synchronously. The electronics diagram is shown in Fig. 1c.

In PDI, we process the acquired data following the procedure shown in Fig. 1d. The PDI raw signal (left panel) was acquired from the center of the polymethyl methacrylate (PMMA) particle with a diameter of 500 nm under the IR pump at its absorption peak of 1729 cm−1. Benefited from the broadband detection scheme, a single pulse photothermal signal can be clearly resolved with an SNR over 43 without averaging. During the imaging process, the signal acquired per pixel is a segment with multiple pulses. We further performed match filtering on each segment with a comb-like passband in the frequency domain. In the comb passband, each small window has its center position colocalized at the harmonic frequencies to reject most of the non-modulated noise (middle panel). After filtering and inverse Fourier transform, the photothermal dynamic signal was obtained in the temporal domain with a much-improved SNR of 570 (right panel). By scanning the sample, an X-Y-t stack with each spatial pixel extended in the temporal domain is obtained. The single pulse resolved capability in PDI enables an unprecedented imaging speed with pixel dwell time as short as 50 μs, practically limited by the stage scanning speed.

## Mid-infrared photothermal dynamic imaging of nanoparticles.

To characterize PDI’s performance and evaluate its capability of scrutinizing transient thermal dynamics with chemical specificity, we performed PDI on PMMA particles with a nominal diameter of 300 nm. The QCL is set with a repetition rate of 100 kHz and a pulse duration of 600 ns. By tuning the QCL to $1 7 2 9 \ c m ^ { - 1 } ,$ , corresponding to the absorption peak of the C=O bond in PMMA, we acquired the photothermal dynamics signal (Supplementary Movie 1). The IR pump starts at $t _ { 1 } { = } 0 \ \mathrm { n s } .$ . As in Fig. 2a, most of the single particles with absorption reached their highest temperature at $t _ { 2 } { = } 4 4 0 \mathrm { n s . }$ The photothermal contrast disappears under an off-resonance IR pump at $1 6 0 0 ~ \mathrm { { c m } ^ { - 1 } }$ (Fig. 2b). To compare PDI with PHI, we acquired the intensity image under $1 7 2 9 \ \mathrm { c m } ^ { - 1 }$ at the same field of view by demodulating at 100 kHz using the lock-in (Fig. 2c). The line profiles across the indicated particle in Fig. 2a, c are shown in Fig. 2d. For PDI, an SNR of 230 was achieved with a pixel dwell time of 200 µs, while it was 52 using PHI, corresponding to more than four-fold improvement in detection sensitivity. The SNR improvement majorly comes from two aspects. Firstly, the laser noise level at high frequency is largely reduced as shown in Supplementary Fig. 1, and the transient photothermal signal has significant components at high frequency. Secondly, the harmonics of signal constructively add up, while the uncorrelated ran dom noise does not. A quantitative analysis of SNR improvement is given in Supplementary Note 1. For the above experimental condition, a theoretical SNR gain of 5.4 is expected. Experimentally, our result shows an improvement of 4.3 times, which is close to theory. The small discrepancy is attributed to the nonideal impulse shape of the actual IR excitation.

Apart from the sensitivity improvement, PDI concurrently revealed dynamics that enable accurate thermal property characterization. The photothermal dynamics of the nanoparticle indicated in Fig. 2a under $1 7 2 9 \ \mathrm { c m ^ { - \dot { 1 } } }$ excitation is presented as the red curve in Fig. 2e. The photothermal induced scattering modulation is known to be linear dependent on temperature6,37. The raw signal has a negative sign, indicating diminished backscattering as temperature rising. Here, an inversed waveform is used for better illustration. The temporal resolution in our system is ultimately limited by the photodiode response time, which is a few nanoseconds. With that high temporal resolution, the time-resolved energy flux function $[ \dot { Q _ { \mathrm { a b s } } } ( t ) \dot { - } Q _ { \mathrm { d i s s } } ( t ) ]$ in Eq. (1) could be directly evaluated by taking the derivative of PDI signal to time, shown as the blue curve in Fig. 2e. The thermaldynamic process is composed of three stages. At the beginning of heating (from $t _ { 1 }$ to $t _ { 2 } ) _ { : }$ , the heat dissipation was negligible. $\bar { Q _ { \mathrm { a b s } } ( t ) }$ related to energy absorption was dominant, and it resulted in a waveform similar to the IR pulse shape $I _ { \mathrm { I R } } ( t )$ shown as the black curve in Fig. 2e. The temperature kept rising until the heat dissipation term equaled to heat influx; at this point, the net energy flux became zero, and the absorber entered a thermal equilibrium state. From $\mathbf { t } _ { 2 }$ to t , with the IR intensity reduced gradually, the dissipated energy became dominant, and the energy flux function became negative, showing that the absorber entered the cooling stage. After the IR pulse $( { \bar { > } } t _ { 3 } )$ , the heat flux function only had the heat dissipation term $Q _ { \mathrm { d i s s } } ( t )$ , shown as an exponential decay.

Subsequently, we measured the thermal decay constant of the pure dissipation process after $t _ { 3 } .$ Here we extracted the exponential decay constant with the least square fitting method. Note that advanced methods, including maximum likelihood estimation38 and maximum entropy methods39,40, can be exploited to obtain the decay information. The fitted exponential decay function is shown as the green dashed line in Fig. 2e, which has a decay constant of 300 ns. From Eq. (3), this time constant is given by m $C _ { s } / h S .$ . With the material’s density $\rho$ and $C _ { s }$ from refe $\mathrm { \cdot e n c e ^ { 4 1 } }$ we can determine the heat transfer parameter hS. For this 300 nm PMMA particle on a $\mathrm { C a F } _ { 2 }$ substrate in air, the heat transfer parameter is derived to be 7.78E−8 W/K. To verify the experimental result, this parameter is independently calculated to be 7.65E–8 W/K using the finite-element method (FEM) (Supplementary Fig. 3), which closely matches the experimental measurement. The thermal decay constants of PMMA particles with various sizes were statistically studied by PDI (Supplementary Note 2), as shown in Supplementary Movie 2 and Supplementary Fig. 4. The particles with diameters of 300 nm and 500 nm showed distinct thermal decay constants of 280 ns and 495 ns, respectively. In addition, by acquiring complete photothermal dynamics together with scattering intensity, PDI enables transient temperature rise measurement according to the modulation depth as presented in Supplementary Note 3. For D = 500 nm PMMA particle at its absorbing peak 1729 cm−1, the highest transient temperature rising is estimated to be 7.6 K. Such temperature rise less than 10 Kelvin and with a duration less than hundreds of nanosecond is biologically safe. Next, we tuned the IR wavelength and recorded the photothermal spectrum of the indicated particle, as shown in Fig. 2f. When comparing it with the spectrum of PMMA film acquired with FT-IR, good consistency, such as the peak ratio, was observed in the entire fingerprint region. Collectively, with the capability of characterizing thermal decay properties with submicron spatial resolution and spectral fidelity, PDI offers a new dimension for molecular analysis.

![](images/c42f8f277820cc17def173bbd106eb8629e9200bd39701943ef1dbc612ee6420.jpg)  
Fig. 2 Mid-infrared photothermal dynamic imaging and spectroscopy of PMMA nanoparticles. a, b PDI-acquired photothermal intensity image of 300-nm diameter PMMA particles at the absorption peak at 1729 cm−1 and off-resonant wavelength at 1600 cm−1 , respectively. c MIP intensity image at 1729 cm−1 acquired with the lock-in amplifier in the same field of view. d Line profiles across the particle indicated in (a) and (c). Pixel dwell time: 200 μs; Step size: 100 nm; Probe power on sample: 30 mW; IR power on sample: 5 mW at 1729 cm−1 , 16 mW at $1 6 0 0 ~ { \mathsf { c m } } ^ { - 1 } ;$ IR repetition rate: 100 kHz; IR pulse duration: 600 ns at 1729 cm−1 , 900 ns at 1600 cm−1 . Scale bars: 5 μm. e Photothermal dynamics of the particle indicated in (a). The red curve is the transient PDI intensity. The green dash line is the fitted exponential decay function, with a decay constant τ of 300 ns. The blue curve is the derivative of PDI intensity over time. The dash-dot line indicates a thermal equilibrium state. The black curve is the synchronously acquired IR pulse. f Spectrum fidelity. FTIR spectrum of a standard PMMA film (top) and normalized MIP spectrum profile measured at the indicated 300-nm diameter PMMA particle (bottom). Acquisition speed: $5 0 \mathrm { c m } ^ { - 1 }$ per second. g Large area PDI of 500-nm diameter PMMA particles at $1 7 2 9 \ c m ^ { - 1 }$ . Pixel dwell time: 100 μs; Step size: 150 nm; Probe power on sample: 25 mW; IR average power measured before objective lens: 11 mW; IR repetition rate: 500 kHz; IR pulse duration: 400 ns. Scale bar: 20 μm.

Importantly, the retrieved decay constant of absorbers can be used for optimizing the IR modulation frequency and increasing the imaging speed accordingly. For 500 nm PMMA particles with a decay constant of 495 ns, more than 95% heat drain out at the initial 1500 ns of the cooling process. Thus, modulation frequency higher than 100 kHz used in the previous work5 can be employed without influencing the photothermal signal amplitude. Figure 2g shows PDI on PMMA particles with a diameter of 500 nm at an IR repetition rate of 500 kHz and pulse duration of 400 ns. The pixel dwell time of PDI was reduced to 100 μs, and average singleparticle SNR over 261 was achieved. This imaging speed is 30 times faster than the previous report work11 while achieving similar SNR. With such improvement, we further explored high speed PDI of biological specimens, as shown below.

PDI enables high-speed metabolic analysis at a single bacter ium level. Given the cell-to-cell heterogeneity, high-speed ima ging is essential to understand cell functions and pathways42. For example, sensitive single bacterium metabolism analysis plays an important role in synthetic biology where rare species of interest need to be differentiated from a large population43, or determination of antimicrobial susceptibility from few cells44, such as cells from a small volume of cerebrospinal fluid. Here, we explored PDI imaging of carbohydrate conversion into biomass at a single bacterium level using E. coli as a testbed.

We first implemented the PDI of E. coli at 100 kHz IR modulation frequency, and 200 µs pixel dwell time. The thermal response of a single E. coli is shown in Fig. 3a. The decay constant is found to be 280 ns, where 95% heat drains out within 800 ns. Such thermal property allows IR modulation at up to 1 MHz without overheating. At 1 MHz frequency and with a pixel dwell time of 50 us, we performed PDI of E. coli under $\dot { 1 } 6 5 8 ~ \mathrm { c m ^ { - 1 } }$ excitation, corresponding to the Amide I band, as shown in Fig. 3b. An SNR over 140 is achieved for a single cell (Fig. 3c). This speed is 600 times faster than the previous lock-in-based MIP imaging of single E. coli6. The PDI image covering more than 350 individual cells was acquired within 70 s, showing its high throughput.

![](images/b0a21b33c0f4aac6d271f416baa2534cdae2c133bb71c5eea29e77e7f43496b7.jpg)

<details>
<summary>line chart</summary>

| Time (ns) | PDI of single E.coli (mV) | Decay fit, τ=280ns (mV) |
| --------- | -------------------------- | ------------------------ |
| 0         | 0                          | 0                        |
| 500       | ~9                         | ~9                       |
| 1000      | ~8                         | ~7                       |
| 1500      | ~4                         | ~3                       |
| 2000      | ~1                         | ~1                       |
| 2500      | ~0.5                       | ~0.5                     |
| 3000      | ~0                         | ~0                       |
</details>

![](images/1963779ad01c413a30c88e507392e0e531584ab19bd391c3fa8370132eacb714.jpg)

<details>
<summary>scatterplot</summary>

| PDI Intensity [mV] |
| ------------------ |
| 9                  |
</details>

![](images/810ba379edb98beb118fc6e1801823f9dbd7fc1b0df4594be183b590912a0ac3.jpg)

<details>
<summary>line chart</summary>

| Distance (μm) | PDI (mV) |
| ------------- | -------- |
| 3.5           | 7.0      |
| 10.0          | 6.5      |
</details>

![](images/0cb35928e5862d1a6d03bc8ce66b8412e692bbe198bcd740c49e79eebf4b5ad0.jpg)

<details>
<summary>text_image</summary>

d
12C E.coli
Scattering
PDI 1658 cm⁻¹
PDI 1630 cm⁻¹
PDI 1615 cm⁻¹
Norm. Intensity
1
0
0
</details>

![](images/ca590d000ccfb42db6ba16987f674f425fa00d480780f13caf2cdd7ff2d26fa1.jpg)

<details>
<summary>text_image</summary>

e
Scattering
13C E.coli
PDI 1658 cm⁻¹
PDI 1630 cm⁻¹
PDI 1615 cm⁻¹
Norm. Intensity
1
0
0
</details>

![](images/fa0042682c8eebc3fb69d3598231dca54679912b3d27d00142d7c7199424a448.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | ¹²C E.coli | ¹³C E.coli |
| ----------------- | ---------- | ---------- |
| 1533              |            |            |
| 1546              |            |            |
| 1615              |            |            |
| 1658              |            |            |
</details>

Fig. 3 PDI enables high-throughput metabolic imaging at a single bacterium level. a Photothermal dynamics of single E. coli under 1658 $\mathsf { c m } ^ { - 1 }$ excitation. Measured decay constant τ of single bacteria is 280 ns. b High-speed PDI of E.coli at the protein Amide I band. Pixel dwell time: 50 µs; Scale bars: $2 0 \mu \mathrm { m }$ Probe power on sample: 10 mW; IR average power measured before the objective lens: 35 mW at 1658 cm−1 ; IR repetition rate: 1.0 MHz; IR pulse duration: 300 ns. c Line profile of indicated line in (b). d PDI of ${ } ^ { 1 2 } \mathsf { C }$ glucose-treated E. coli at Amide I band. (e) PDI $\mathsf { o f } ~ ^ { 1 3 } \mathsf C$ glucose-treated E. coli at Amide I band. Amide I peak is shifted from 1658 $\mathsf { c m } ^ { - 1 }$ to 1615 $\mathsf { c m } ^ { - 1 }$ due to the isotope substitution. Scale bars: 5 µm. (f) MIP spectra acquired from ${ } ^ { 1 2 } \mathsf { C }$ and $^ { 1 3 } \mathsf { C }$ glucose treated E. coli (Error bands represent standard deviation of the mean)

Next, we implemented the PDI of E. coli treated with normal and isotope-labeled glucose. Under the 12C-glucose carbon source, the Amide I absorption peak is localized at $1 6 5 8 ~ \mathrm { c m } ^ { - 1 } .$ , as shown in Fig. 3d. By substituting the carbon source with $^ { 1 3 } \mathrm { C } \mathrm { . }$ -glucose in the growth medium, the Amide I band is shifted to $1 6 1 5 \mathrm { c m } ^ { - 1 }$ , as shown in Fig. 3e. The PDI spectral profiles of these two different groups of E. coli are shown in Fig. 3f. It is clear that the Amide I peak is shifted from $1 6 5 8 ~ \mathrm { c m } ^ { - 1 } ~ \mathrm { t o } ~ 1 6 1 5 ~ \mathrm { c m } ^ { - 1 }$ , and the Amide II peak is shifted from $1 5 4 6 \mathrm { c m } ^ { - 1 }$ to $1 5 3 3 \mathrm { c m } ^ { - 1 }$ . Collectively, these data demonstrate that PDI has high through put and high sensitivity for single-cell metabolism imaging.

PDI separates biomolecular signal from water background in infrared photothermal imaging of living cells. Due to water absorption in the entire fingerprint region, the culture medium experiences temperature modulation when performing MIP imaging of living cells. Bulky water is known to have a large heat capacity, which helps increase the MIP contrast between biosamples and background5,21 to some extent. However, in the conventional lock-in-based MIP system, using signal amplitude alone is not sufficient for separating weak biomolecular signals from water background. By capturing the photothermal dynamics, PDI can be used to separate the water contribution from the organelles’ signal based on their distinct thermal responses.

To investigate the transient thermal responses of various organelles inside cells, we performed PDI of U87 brain cancer cells in $\mathrm { D } _ { 2 } \mathrm { O }$ PBS. The $\mathrm { D } _ { 2 } \mathrm { O }$ PBS was used to maintain cell morphology and reduce the water absorption of mid-IR around $1 6 5 0 ~ \mathrm { c m ^ { - 1 } } .$ . By tuning the IR to $1 6 5 5 ~ \mathrm { { c m } ^ { - 1 } }$ corresponding to the Amide I band, protein-rich contents inside the cell give strong contrast in the photothermal intensity map shown as Fig. 4a. Due to the residual water absorption at this wavenumber, the background was observed, but it was relatively weak compared to the cells’ signal5,20. In this protein map, uniformly distributed protein contents in the cytoplasm and a strong signal from the nucleolus are observed. By tuning the $\mathrm { I R } { \mathrm { ~ t o ~ } } 1 7 5 0 \ \mathrm { ~ c m } ^ { - 1 }$ corresponding to the C=O band from lipids, individual lipid droplets show a strong signal in Fig. 4b. To verify the chemical contents, we performed photothermal spectroscopy in the fingerprint region at lipid droplet, nucleus, cytoplasm, and medium, respectively, shown in Fig.4c. The spectra at the nucleus and cytoplasm show a strong peak in the Amide I band at $1 6 5 5 ~ \mathrm { { c m } ^ { - 1 } }$ and a shifted Amide II band at $1 4 5 0 \mathrm { c m } ^ { - 1 }$ due to the deuterium substitution of N-H bond45. The spectrum for lipid droplets shows a strong peak at $1 7 5 0 \ \mathrm { c m ^ { - 1 } }$ contributed by the $\mathrm { C = } \mathrm { \bar { O } }$ bond in esterified lipids. Interestingly, a broad peak centered at $1 6 5 0 ~ \mathrm { { c m } ^ { - 1 } }$ showed up in the spectra of lipid as well. It matched the result of the intensity map at $1 6 5 5 ~ \mathrm { { c m } ^ { - 1 } }$ (Fig. 4a), where lipid droplets are visible as well. This abnormal contrast at the protein band was found in previously reported scattering-based photothermal imaging but without in-depth explanation22,46.

![](images/2d060558c1f3a088c6c504df5bf33867e3acc9d15371a0997f5040c64c734934.jpg)

<details>
<summary>text_image</summary>

t = 1120 ns
PDI 1655 cm⁻¹
Background
Nucleus
Cytoplasm
55
PDI intensity [mV]
2
</details>

![](images/bcabd91dc051eb5e3d5fa31b4231b33ef5446b52e5f05b8a7906e3d089f7910f.jpg)

<details>
<summary>text_image</summary>

t = 260 ns
PDI 1750 cm⁻¹
Lipid droplet
42
PDI intensity [mV]
0
</details>

![](images/92a6cd55c814686c9e8f50d0644db9e87377ef24b36943cc0609aa9c2f1ade0e.jpg)

<details>
<summary>text_image</summary>

Decay constant 1655 cm⁻¹
LD2
LD3
LD1
0.15
Decay constant [µs]
</details>

![](images/87f87432c8d793d2296ddf540188353c82dd27222327e0556c544a64cf31672d.jpg)

<details>
<summary>scatterplot</summary>

| Label | Value |
|-------|-------|
| LD1   | 0.1   |
| LD2   | 1.3   |
| LD3   | 0.1   |
</details>

![](images/284020dce49faffe3457707073bf30cee6a995860e895e33aa1d63d103060713.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | LD 1 1655 cm⁻¹ | LD 2 1655 cm⁻¹ | LD 3 1655 cm⁻¹ | BG 1655 cm⁻¹ |
| --------- | -------------- | -------------- | -------------- | ------------ |
| 0         | 0              | 0              | 0              | 0            |
| 1         | ~50            | ~50            | ~25            | ~5           |
| 2         | ~40            | ~40            | ~20            | ~5           |
| 3         | ~30            | ~30            | ~15            | ~5           |
| 4         | ~20            | ~20            | ~10            | ~5           |
| 5         | ~15            | ~15            | ~8             | ~5           |
| 6         | ~10            | ~10            | ~6             | ~5           |
| 7         | ~8             | ~8             | ~5             | ~5           |
| 8         | ~5             | ~5             | ~4             | ~5           |
| 9         | ~3             | ~3             | ~3             | ~5           |
</details>

![](images/d49426b865f77e6f7386ea4fb4cd81508fb15a8372650029975a097f2ee2b924.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | LD 1 1750 cm⁻¹ | LD 2 1750 cm⁻¹ | LD 3 1750 cm⁻¹ |
| --------- | -------------- | -------------- | -------------- |
| 0         | 30             | 20             | 40             |
| 1         | 10             | 5              | 15             |
| 2         | 5              | 2              | 8              |
| 3         | 2              | 1              | 4              |
| 4         | 1              | 0.5            | 2              |
| 5         | 0.5            | 0.2            | 1              |
| 6         | 0.2            | 0.1            | 0.5            |
| 7         | 0.1            | 0.05           | 0.2            |
| 8         | 0.05           | 0.02           | 0.1            |
| 9         | 0.02           | 0.01           | 0.05           |
</details>

![](images/f101a5c8e1064abac79c35e5e669e4c346b9405e1188348d07f2e8856432b54e.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Lipid droplet | Nucleus | Cytoplasm | Background |
| ----------------- | ------------- | ------- | --------- | ---------- |
| 1000              | ~0.5          | ~0.5    | ~0.0      | ~0.0       |
| 1200              | ~0.5          | ~0.5    | ~0.0      | ~0.0       |
| 1400              | ~1.5          | ~4.5    | ~0.7      | ~0.2       |
| 1600              | ~2.5          | ~5.5    | ~1.0      | ~0.2       |
| 1800              | ~6.5          | ~1.5    | ~0.0      | ~0.1       |
</details>

![](images/cad8571d6f1b822ff0f5b6d10d7f28d353ff7aaf62a1e2e26cd550b57668bb96.jpg)

<details>
<summary>text_image</summary>

1750 cm⁻¹ + BG type signal 1655 cm⁻¹
</details>

![](images/b01d688a952a02582eb8daa1b6bab5e0572890489bac78b1389c9ffe0d99e00a.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Lipid droplet 1750cm⁻¹ | Nucleus 1655cm⁻¹ | Cytoplasm 1655cm⁻¹ | Background 1655cm⁻¹ |
|-----------|------------------------|------------------|--------------------|---------------------|
| 0         | ~20                    | ~0               | ~0                 | ~0                  |
| 1         | ~10                    | ~50              | ~10                | ~4                  |
| 2         | ~5                     | ~30              | ~5                 | ~5                  |
| 3         | ~2                     | ~20              | ~2                 | ~3                  |
| 4         | ~1                     | ~15              | ~1                 | ~2                  |
| 5         | ~0.5                   | ~10              | ~0.5               | ~1                  |
| 6         | ~0.2                   | ~5               | ~0.2               | ~0.5                |
| 7         | ~0.1                   | ~2               | ~0.1               | ~0.2                |
| 8         | ~0.05                  | ~1               | ~0.05              | ~0.1                |
| 9         | ~0.02                  | ~0.5             | ~0.02              | ~0.05               |
</details>

![](images/7725176f949f07c2eacd3f8077b695e6b0a25010684e0cfbdbf4e8a3ad09f7a0.jpg)

<details>
<summary>text_image</summary>

1750 cm⁻¹ + BG type removed 1655 cm⁻¹
</details>

Fig. 4 Mid-infrared photothermal dynamic imaging of U87 brain cancer cells. a PDI of U87 brain cancer cells at 1655 cm−1 Amide I band. b PDI of U8 brain cancer cell at 1750 cm−1 lipid C=O band. c MIP spectra of locations indicated in (a, b). All spectrum intensities are normalized according to the peak of cytoplasm at $1 6 5 5 \mathsf { c m } ^ { - 1 }$ . Acquisition speed: $5 0 \mathrm { c m } ^ { - 1 }$ per second. d Thermal dynamics at the positions indicated in (a, b). Black curves are synchronously acquired IR pulse. Green dash lines indicate fitted exponential decay functions and corresponding time constant τ. e Decay constant map at 1655 cm−1 . f Decay constant map at $1 7 5 0 ~ \mathsf { c m } ^ { - 1 } .$ g Thermal dynamics of background (BG) and positions indicated in (e) under 1655 $\mathsf { c m } ^ { - 1 }$ excitation. h Therma dynamics of lipid droplets (LD) indicated in (f) under $1 7 5 0 ~ \mathsf { c m } ^ { - 1 }$ excitation. i Merged intensity image at 1750 $\mathsf { c m } ^ { - 1 }$ (red) with background type signal at 1655 cm−1 (green). The yellow color shows a highly overlapped spatial distribution. j Merged lipid contents at 1750 cm−1 with protein contents at 1655 cm −1 after removing the background type signal. Pixel dwell time: 200 µs; probe power on sample: 20 mW; IR average power measured before objective lens: 22 mW at $1 6 5 5 ~ \mathsf { c m } ^ { - 1 }$ , 2 mW at $1 7 5 0 ~ { \mathsf { c m } } ^ { - 1 } ;$ Scale bars: 10 µm.

Here, enabled by PDI, we investigated the origin of this abnormal signal by studying the transient photothermal dynamics of various subcellular components indicated in Fig. 4a, b. The results in Fig. 4d show distinct thermal responses among organelles. The lipid droplets inside cells show a relatively fast decaved signal with a time constant of 300 ns. Nucleolus and cytoplasm with rich protein contents show slower thermal dynamics on the level of 2.5 µs. The water background at $1 6 5 5 ~ \mathrm { { c m } ^ { - 1 } }$ has the longest decay with a decay constant larger than 5 µs, largely because of the large water heat capacity. For a more intuitive illustration, we generated the decay constant map of $1 6 5 5 ~ \mathrm { { c m } ^ { - 1 } }$ (Fig. 4e) and $1 7 5 0 \ \mathrm { c m } ^ { - 1 } \ ( \mathrm { F i g . \ 4 f } )$ . From the decay map, the background and cellular structures are clearly differentiated for their distinct thermal response. The cytoplasm and nucleus have decay constant on the level of 2.5 µs with $1 6 5 5 ~ \mathrm { ~ c m ^ { - 1 } }$ excitation (Fig. 4e). Lipid droplets have decay constants ranging from 150 ns to 500 ns under $1 7 5 0 ~ \mathrm { ~ c m ^ { - 1 } }$ excitation (Fig. 4f).

Importantly, those “lipids” seen in the intensity image at 1655 $\mathsf { \bar { c } m } ^ { - 1 }$ (Fig. 4a) did not show fast dynamics (Fig. 4e). Instead, they exhibit a decay constant similar to that of the background. Since the detected signal originates from the modulation of the scattering field, the signal intensity is proportional to $( n _ { s } - n _ { m } ) .$ , where $n _ { s }$ and $n _ { m }$ are the refractive index of organelle and medium, respectively. In the presence of water absorption, $n _ { m } ( t )$ becomes time-dependent, and such change results in a pseudo-MIP signal without organelle's absorption. To better understand the origin of “lipids” seen under $1 6 5 5 \mathrm { { c m } ^ { - 1 } }$ excitation, underlying thermal dynamics at indicated positions in Fig. 4e and Fig. 4f are plotted in Fig. 4g and Fig. 4h, respectively. At 1750 cm−1, lipids’ signal has a fast response and decays in a few hundred nanoseconds. However, the signal at 1655 $\mathrm { c m } ^ { - 1 }$ from the same regions of interest shows a relatively slow process with a decay constant higher than 5 µs, similar to that of the water background, as shown in the dash lines in Fig. 4g. In summary, by analysis of photothermal dynamics, we conclude that the

a  
![](images/69424ea5b113909013e054e593aaf3d86cddc7dc37de4626355e86ee252f2406.jpg)

<details>
<summary>text_image</summary>

t = 260 ns
PDI 1750 cm⁻¹
BG
LD
Int. in In scale [mV]
54.6
20.0
7.4
2.7
1
</details>

b  
![](images/48d5b60872c4431a9454aa653dbc040410b438c7c1e19b2868cf981dab3073e6.jpg)

<details>
<summary>text_image</summary>

PHI 100kHz 1750 cm⁻¹
7.4
2.7
Int. in In scale [mV]
1
</details>

e  
![](images/6abe08107fe8eaaa9aee48ab619df5bccaa3691e9d386c3564cbbc52c8eeb2e9.jpg)

<details>
<summary>text_image</summary>

21th harmonic
PDI 1750 cm⁻¹
Line plot
FFT Amplitude [mV]
0
2.2
</details>

c  
![](images/e9be393f7ad809e22bc1fd2088c7f1d3c275f59b98e75b5f1a5e1ab82ddbc54e.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | BG 1750 cm⁻¹ | 1st harmonic | IR pulse |
| --------- | ------------ | ------------ | -------- |
| 0         | 0.4          | 0.1          | 0.0      |
| 1         | 0.3          | 0.25         | 0.0      |
| 2         | 0.25         | 0.2          | 0.0      |
| 3         | 0.2          | 0.15         | 0.0      |
| 4         | 0.15         | 0.1          | 0.0      |
| 5         | 0.1          | 0.05         | 0.0      |
| 6         | 0.05         | 0.0          | 0.0      |
| 7         | 0.0          | 0.0          | 0.0      |
| 8         | 0.0          | 0.0          | 0.0      |
| 9         | 0.0          | 0.1          | 0.0      |
</details>

d  
![](images/fb79e5b616df570dd032985d628c5139a60e26b19d61f5633cea0f29e63484ae.jpg)

<details>
<summary>line chart</summary>

| Frequency (MHz) | BG 1750 cm⁻¹ (mV) | LD 1750 cm⁻¹ (mV) | LD/BG (mV) |
| --------------- | ----------------- | ----------------- | ---------- |
| 0.0             | 0.12              | 3.5               | 30         |
| 0.5             | 0.04              | 1.5               | 60         |
| 1.0             | 0.02              | 0.8               | 80         |
| 1.5             | 0.01              | 0.5               | 100        |
| 2.0             | 0.005             | 0.3               | 120        |
| 2.5             | 0.002             | 0.2               | 90         |
</details>

f  
![](images/986733f692f9b6563955dd6dc4064e47daf352fd85384284309b6e15fc4f2512.jpg)

<details>
<summary>line chart</summary>

| Frequency | FWHM |
| --------- | ---- |
| 0.1 MHz   | 0.33 |
| 0.7 MHz   | 0.27 |
| 1.3 MHz   | 0.28 |
| 2.1 MHz   | 0.28 |
</details>

Fig. 5 PDI detection of weak lipid signal from water background. a PDI of U87 cancer cell at $1 7 5 0 \mathsf { c m } ^ { - 1 } ,$ , displayed with natural logarithm scale color bar. b MIP image of the same field of view at $1 7 5 0 \ c m ^ { - 1 }$ acquired by the lock-in method, displayed with natural logarithm scale color bar. Arrows indicated lipid droplets in (a) are hardly seen. c Photothermal dynamics of background (BG) and lipid droplet (LD) at the position indicated in (a). Black curves are synchronously acquired IR pulse. d Frequency domain representation of signals in (c) acquired by Fast Fourier transform (FFT) and corresponding signal to background ratio (SBR). e The 21st harmonic amplitude image was acquired by taking the Fourier transform of the PDI stack. f Intensity profiles of the line indicated in (e) at different frequencies. PDI pixel dwell time, 200 µs; PHI pixel dwell time 500 µs; Probe power on sample: 20 mW; IR average power measured before objective lens: 2 mW. Scale bars: 10 µm.

1655 $\mathrm { c m ^ { - 1 } }$ peak in lipid (Fig. 4c) comes from the water background rather than the organelles.

Next, by utilizing the distinct thermal properties between water medium and lipid droplets, we successfully extracted those waterinduced signals at lipid droplet positions with the acquired thermal dynamics via a simple algorithm that evaluates their photothermal intensity and decay constants, as shown in Fig. 4i. Those strong signals with background type thermal dynamics at $1 6 5 5 ~ \mathrm { { c m } ^ { - 1 } }$ are displayed in green color, and lipid droplets image acquired under $1 7 5 0 \ \mathrm { { \dot { c } m } ^ { - 1 } }$ excitation is shown in red color. The yellow contrast indicates highly matched colocalization in the merged image. After removing those water-induced pseudo signals at 1655 $\mathrm { c m } ^ { - 1 }$ from the intensity image, a corrected content map between lipids and proteins is produced, as shown in Fig. 4j.

PDI allows extraction of extremely weak signal from water background. The above photothermal dynamic results show that lipid droplets exhibit a fast decay on the order of a few hundreds of nanoseconds, while the water background is much slower, on the order of a few microseconds. By capturing the high-order harmonic signals, PDI further enabled us to visualize the small lipids (Fig. 5a). These small lipids were completely buried in the water background when lock-in detection was used (Fig. 5b). To better understand this capability, we performed a Fourier analysis of the photothermal dynamic signals.

The transient photothermal signals of background and lipid droplets at indicated positions in Fig.5a are shown in Fig.5c. Their fundamental components (100 kHz) are acquired by Fourier transform and plotted as orange curves. Those signals of small particles have fast responses and load high-order harmonic components. On the contrary, the water background is majorly localized at the fundamental modulation frequency. Thus, lock-in demodulation at the fundamental frequency minimizes the contrast between lipid droplets and the background.

The frequency responses of signals in Fig. 5c are shown in Fig. 5d. The slow background (blue square) majorly has components in the first and second harmonics. As a comparison, the fast lipid signal (red square) is widely spread out in the frequency domain, with the first harmonic only containing less than one-fifth of the total energy. Consequently, the lipid to background ratio (purple square) increases till the 21st harmonic. At the first harmonic that lock-in demodulates, the contrast is the lowest (Fig. 5d). Instead, the photothermal image (Fig. 5e) with the 21st harmonic (2.1 MHz) shows clear contrast for small lipids with minimal background. The intensity profiles of the line indicated in Fig. 5e at different frequencies are plotted in Fig. 5f. At the first harmonic (100 kHz), which is equivalent to lock-in extraction, the lipid signal is hardly resolved from the background signal, while a good signal to background ratio is shown in higher-order harmonics (0.7–2.1 MHz).

## Discussion

We have demonstrated a photothermal dynamic imaging microscope that can sense the transient photothermal modulation with nanosecond temporal resolution. This advanced technology enables concurrent detection of chemically specific IR absorption and physically specific thermal dynamics at submicron spatial resolution. We retrieved the thermal response of various organelles inside a cell for the first time. Our data shows that cytoplasm, nucleus, and lipid droplets exhibit distinct timeresolved signatures. Based on the time-resolved signatures, PDI enabled the differentiation of small signals from water medium contribution.

Compared with conventional PHI via lock-in amplifier, PDI increases the sensitivity by more than four-fold for low duty cycle photothermal signals. This improvement leverages the broad detection bandwidth by capturing all the harmonics components induced by the short-pulsed IR pump in the highfrequency region where laser noise is reduced. Those signal harmonics are correlated and can add up, while the noise is uncorrelated and can be suppressed. For this reason, PDI can largely benefit the mid-IR photothermal microscope with a powerful optical parametric oscillator (OPO) source20,47, which has a pulse duration of few nanoseconds and a fixed low repetition rate of tens kilohertz. Such a short-pulsed and high peak power excitation source is highly preferred for generating large modulation depth of small objects on a thermo-conductive substrate or in an aqueous environment, where heat dissipation is relatively rapid7. In such a case, the photothermal signal has a duty cycle of less than 1% and the lock-in amplifier can only capture a tiny portion of modulation or balanced detection for reducing the large laser noise is required at such low modulation frequency47. By capturing all the harmonics, PDI can improve the SNR over one order of magnitude as illustrated in Supplementary Note 1. Our results show that careful choice of detection method has to be made for optimal sensing of the photothermal signal induced by a short pulse excitation. While the same level of SNR improvement may be achieved by using other advanced demodulation techniques that are capable of capturing those high-frequency photothermal signals, such as signal synthesis using lock-in multi-channel demodulation48,49 or boxcar averaging50, those advanced demodulation methods are not yet widely available. In contrast, the broadband detector and digitizer or MHz are readily available and highly cost-effective. A comparison of those methods with PDI regarding the SNR performance, dynamics detecting capability is summarized in Supplementary Table 1. Importantly, our PDI method is able to capture all the harmonics and produce accurate thermal decay constant, which is beyond the reach of the multi-channel lock-in or the boxcar averaging approach.

When imaging specimens with background absorption, lock-in detection at the fundamental modulation frequency diminishes the contrast of fast decay signals. This is the case for detecting the small lipid droplets inside cells. These small organelles’ signals are buried in the water background in the lock-in method, but are detectable with PDI and give higher contrast in higher-order harmonics. We note that this issue can be mitigated in a lock-inbased MIP microscope with tunable modulation frequency IR sources. If knowing the thermal dynamics of a particular type of absorber of interest, one can change the modulation frequency according to their transfer function for optimal detection. For those lipid droplets in water, which quickly decay in few hundreds of nanoseconds, modulation frequency at 500 kHz or higher is more suitable. Yet, the strategy of tuning modulation frequency is no longer valid if absorbers of different decay constants need to be imaged simultaneously.

By retrieving the thermal-physical properties, such as thermal diffusion in a specimen, IR camera-based nondestructive thermal imaging has enabled advanced applications for characterizing materials51 including detection of hidden defects like 52,53 points of failure in composites, solar cells, semiconductors, and electronics54. However, as the time scale comes to sub-microsecond and spatial resolution goes down to the nanoscale, such traditional temperature mapping methods have encountered difficulty due to largely reduced heat radiation and diffraction limit. Various novel techniques have been developed55–60 to achieve transient heat detection in nanoscale. Our method intrinsically senses heat and is capable of measuring the exact temperature rise during the nanosecond photothermal process as demonstrated in Supplementary Note 3. This capability promotes PDI as a new scheme that directly probes those thermal processes at the far-field with nanometer-scale resolution and nanosecond temporal resolution.

Beyond the mid-IR photothermal process, PDI can fertilize research related to imaging of short lifetime events or complex photothermal decay process in general photothermal imaging field that includes but not limited to visible, near-infrared, and other transient physical perturbations61,62. Lock-in free PDI offers nanoseconds temporal resolution that is ultimately limited by the photon detector response. For example, it can be used to study the nonlinear photothermal phenomenon, including the nanobubble generation within a life span of hundreds of nanoseconds63,64, higher-order thermal wave modulation on heat capacity and conductivity65,66; revealing resistive heating profile of nanostructure8 and detecting photothermal induced pressure wave. Those photothermal processes have a relatively short lifetime due to the rapidly dissipated heat. On the other hand, PDI retrieves complete photothermal dynamics that reveal interesting heat dissipation processes of the sample for the first time. As shown in Supplementary Note 4, the lipid droplets inside a cell have a complex thermal decay composed of multiple distinct lifetimes. Such decay feature is related to the microenvironment of such small organelles conveying rich structure information to be scrutinized. This new imaging scheme can be applied to scrutinize intracellular organelles’ thermal response together with chemical composition, or monitor transient cell response to fast perturbation61, providing an entirely new perspective to understand the cell machinery. Collectively, the reported PDI system provides a novel far-field label-free imaging tool to scrutinize a sample’s chemical composition and physical dynamics simultaneously.

## Methods

Experimental setup. The mid-IR PDI system (Fig. 1b) was built on an inverted microscope frame (IX71, Olympus). A pulsed mid-IR beam, generated by a tunable (from 900 cm−1 to 1790 cm−1) quantum cascade laser (MIRcat-2400, Daylight Solutions) is used as the pump source. The mid-IR beam passes through a Ger manium dichroic mirror and then is focused onto the sample through a goldcoating reflective objective lens (52×; NA, 0.65; #66589, Edmund Optics). The residual mid-IR reflected by dichroic mirror is monitored with an MCT detector (PVM-10.6, VIGO System). The pulse repletion rate is tuned from 100 kHz to 1 MHz depending on the decay property of sample; the output pulse duration ranges from 300 to 1000 ns. Counter-propagated probe beam provided by a continuous-wave 532 nm laser (Samba 532 nm, Cobolt) is focused by a water immersion objective lens (×60; NA, 1.2; water immersion; UPlanSApo, Olympus). The probe beam is aligned to be collinear to the mid-IR pump beam to ensure the overlap of the two foci to maintain a good signal level. A scanning piezo stage (Nano-Bio 2200, Mad City Labs) with a minimum pixel dwell time of 50 µs and moving range of 200 µm is used to scan the sample. Backscattered probe photons are collected with a 50/50 beam splitter (BS013, Thorlabs), forward scattered probe photons are collected by the reflective objective and separated by the dichroic mirror. Both forward and backward probes are collected and sent to silicon photodiodes (S3994-01, Hamamatsu). The photocurrent is separated into AC and DC components with a bias Tee (ZFBT-4R2GW+, Minicircuit). The DC is a direct intensity readout. The AC channel is connected with a wideband voltage amplifier with 40 dB gain (DHPVA-101, FEMTO). The voltage signal is AC coupled and filtered with a low pass filter with a cut-off frequency of 25 MHz (BLP-25+, Minicircuit). Amplified signal is sent to a four-channel digitizer (Oscar 14, Gage Applied) installed on a computer, which has a sampling rate of 50 million samples per second and 14-bit A/D resolution. Acquired data is directly streamed to the computer memory for signal processing. During the imaging, the position feedback from scanning stage, mid-IR pulse shape from MCT are acquired synchronously by the same digitizer for image reconstruction and photothermal dynamics analysis. The same signal output from amplifier is also send to a lock-in amplifier (HF2LI Zurich Instruments) for conventional MIP detection at the fundamental modula tion frequency as comparison experiment and system calibration.

Data acquisition and processing. Acquired raw PDI raw data from the digitizer is directly streaming to the host computer memory via the PCIe Data Streaming Firmware (Gage Applied) and processed in the CPU. Segments containing repe titive measurements according to pixel dwell time are match filtered. Processed temporal dynamics with reduced data amount per pixel are then transferred to disk for image reconstruction.

During the match filtering processing, each segment is filtered in the frequency domain with a comb-like passband with each passing window at the harmonic of pump laser repetition rate (For laser running at 100 kHz, the pass windows are choosing at 100 kHz, 200 kHz, …, 2 MHz, 2.1 MHz). The window size is defined by the spectrum resolution according to pixel dwell time. The number of passing harmonics decides the thermal-dynamic bandwidth and influences the SNR. In this work, we used 16 order harmonics (1.6 MHz) for depicting absorption contrast which gives the highest image SNR. On the other hand, for depicting a complete photothermal dynamic profile, we used the bandwidth of 25 MHz. For best SNR performance, the included harmonics order can be selected based on the calculation model given in Supplementary Note 1S. for quantitative estimation

With acquired temporal dynamic behind each pixel, the X-Y-t hyper image is then reconstructed according to the pixel position acquired from the scanning stage. For preserving positioning precision, we perform the reconstruction in an enlarged mesh with four times of acquired pixels by linear interpolation using ImageJ.

Spectra acquisition. The MIP spectra are acquired from PDI signal at different wavelengths and normalized according to the effective pulse energy. To minimize the heat dissipation influence and IR pulse duration variance, the absorption cross section is evaluated at the initial 300 ns of the photothermal dynamic. The photothermal intensities at t = 300 ns at each wavelength are firstly evaluated noted as $S _ { \mathrm { r a w } } ( \lambda ) .$ . Subsequently, the effective heating energy at each wavelength is evaluated by integrating the IR pulse shape from 0 ns to 300 ns, which is noted as $Q _ { \mathrm { I R } } ( \lambda ) .$ With considering the IR focal spot size change along with wavelength, the final spectrum is then derived from normalizing $( S _ { \mathrm { r a w } } ( \lambda ) * \lambda ^ { 2 } ) / Q _ { \mathrm { I R } } ( \lambda )$ .

Thermal decay fitting. The thermal decay constant is acquired by fitting exponential function on the free decay process (IR pulse is finished) with a customcoded Matlab program. The nonlinear regression model is used to retrieve the function with the formula: $y = y _ { 0 } + A _ { 1 } \mathrm { e } ^ { - x / t }$ .

The display decay constant map is acquired firstly by fitting the decay constant at every pixel in the PDI stack and then smoothed with a median filter.

PMMA particles. The PMMA particles with a nominate diameter of 300 nm (MMA300, Phosphorex) or with diameter of 500 nm (MMA500, Phosphorex) in solution form were first diluted with deionized water. Around 2 µL of the solution was then dropped on the surface of a calcium fluoride (CaF ) substrate with 0.2 mm thickness for imaging. The photothermal signal was detected from backward scattering.

The 500-nm diameter PMMA particles (MMA500, Phosphorex) and 300-nm diameter PMMA particles (MMA500, Phosphorex) mixture sample was prepared by firstly mixing their solution together with 1:1 ratio, and then spreading one droplet of the solution on the surface of a CaF substrate with 0.2 mm thickness for imaging. The photothermal signal is detected from backward scattering.

E. coli. Bacteria were harvested during the log phase. 12C or 13C-glucose was used as the only carbon source in the growth media. The growth media was remoyed from the bacterial samples by centrifugation and washing four times with 2 mL of deionized water. The bacterial pellet was then suspended in 0.25 mL of water, and 1 uL of the resulting bacterial suspension was dropped on CaF2 with 0.2 mm thickness for imaging. The photothermal signal was detected from backward scattering.

U87 cancer cells. The U87 brain cancer cells were cultured on CaF substrate for 24 h and fixed with formalin. The medium was washed three times by phosphate buffered saline and replaced by 0.9% NaCl/D2O solution. It was later sandwiched with another thin calcium fluoride window with 0.2 mm thickness for imaging. The photothermal signal was detected from forward scattering.

Reporting summary. Further information on research design is available in the Nature Research Reporting Summary linked to this article.

## Data availability

All the data related to the work is available upon reasonable request to the corresponding author.

## Code availability

Data processing code related to the work is available upon reasonable request to the corresponding author.

Received: 5 May 2021; Accepted: 8 November 2021;

Published online: 07 December 2021

## References

1. Adhikari, S. et al. Photothermal microscopy: imaging the optical absorption of single nanoparticles and single molecules. ACS nano 14, 1641416445 (2020)  
2. Berciaud, S., Cognet, L., Blab, G. A. & Lounis, B. Photothermal heterodyne imaging of individual nonfluorescent nanoclusters and nanocrystals. Phys. Rev. Lett. 93, 257402 (2004).  
3. Berciaud, S., Cognet, L., Tamarat, P. & Lounis, B. Observation of intrinsic size effects in the optical response of individual gold nanoparticles. Nano Lett. 5, 515–518 (2005).  
4. Gaiduk, A., Yorulmaz, M., Ruijgrok, P. & Orrit, M. Room-temperature detection of a single molecule’s absorption by photothermal contrast. Science 330, 353–356 (2010).  
5. Zhang, D. et al. Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2, e1600521 (2016).  
6. Li, Z., Aleshire, K., Kuno, M. & Hartland, G. V. Super-resolution far-field infrared imaging by photothermal heterodyne imaging. J. Phys. Chem. B 121, 8838–8846 (2017).  
7. Bai, Y., Yin, J. & Cheng, J.-X. Bond-selective imaging by optically sensing the mid-infrared photothermal effect. Sci. Adv. 7, eabg1559 (2021).  
8. Aleshire, K. et al. Far-field midinfrared superresolution imaging and spectroscopy of single high aspect ratio gold nanowires. Proc. Natl Acad. Sci. 117, 2288–2293 (2020).  
9. Chatterjee, R., Pavlovetc, I. M., Aleshire, K., Hartland, G. V. & Kuno, M. Subdiffraction infrared imaging of mixed cation perovskites: Probing local cation heterogeneities. ACS Energy Lett. 3, 469–475 (2018).  
10. Pavlovetc, I. M. et al. Suppressing cation migration in triple-cation lead halide perovskites. ACS Energy Lett. 5, 2802–2810 (2020).  
11. Li, X. et al. Fingerprinting a living cell by Raman integrated mid-infrared photothermal microscopy. Anal. Chem. 91, 10750–10756 (2019).  
12. Lima, C., Muhamadali, H., Xu, Y., Kansiz, M. & Goodacre, R. Imaging isotopically labeled bacteria at the single-cell level using high-resolution optical infrared photothermal spectroscopy. Anal. Chem. 93, 3082–3088 (2021).  
13. Lim, J. M. et al. Cytoplasmic protein imaging with mid-infrared photothermal microscopy: cellular dynamics of live neurons and oligodendrocytes. J. Phys Chem. Lett. 10, 2857–2861 (2019).  
14. Klementieva, O. et al. Super‐resolution infrared imaging of polymorphic amyloid aggregates directly in neurons. Adv. Sci. 7, 1903004 (2020).  
15. Xu, J., Li, X., Guo, Z., Huang, W. E. & Cheng, J.-X. Fingerprinting bacterial metabolic response to erythromycin by Raman-integrated mid-infrared photothermal microscopy. Anal. Chem. 92, 14459–14465 (2020).  
16. Zhang, Y. et al. Vibrational spectroscopic detection of a single virus by mid infrared photothermal microscopy. Anal. Chem. 93, 4100–4107 (2021).  
17. Bai, Y., Zhang, D., Li, C., Liu, C. & Cheng, J.-X. Bond-selective imaging of cells by mid-infrared photothermal microscopy in high wavenumber region. J. Phys. Chem. B 121, 10249–10255 (2017).  
18. Pleitez, M. A. et al. Label-free metabolic imaging by mid-infrared optoacoustic microscopy in living cells. Nat. Biotechnol. 38, 293296 (2020).  
19. Kansiz, M. et al. Optical photothermal infrared microspectroscopy with simultaneous Raman—a new non-contact failure analysis technique fo identification of <10 um organic contamination in the hard drive and other electronics industries. Microsc. Today 28, 26–36 (2020).  
20. Bai, Y. et al. Ultrafast chemical imaging by widefield photothermal sensing of infrared absorption. Sci. Adv. 5, eaav7127 (2019).  
21. Zhang, D. et al. Bond-selective transient phase imaging via sensing of the infrared photothermal effect. Light.: Sci. Appl. 8, 1–12 (2019).  
22. Tamamitsu, M. et al. Label-free biochemical quantitative phase imaging with mid-infrared photothermal effect. Optica 7, 359–366 (2020).  
23. Schnell, M. et al. All-digital histopathology by infrared-optical hybrid microscopy. Proc. Natl Acad. Sci. 117, 3388–3396 (2020).  
24. Shi, J. et al. High-resolution, high-contrast mid-infrared imaging of fresh biological samples with ultraviolet-localized photoacoustic microscopy. Nat. photonics 13, 609–615 (2019).  
25. Selmke, M., Heber, A., Braun, M. & Cichos, F. Photothermal single particle microscopy using a single laser beam. Appl. Phys. Lett. 105, 013511 (2014).  
26. Dada, O. O., Feist, P. E. & Dovichi, N. J. Thermal diffusivity imaging with the thermal lens microscope. Appl. Opt. 50, 6336–6342 (2011).  
27. McLaren, R. & Dovichi, N. J. Spatially resolved differential resistance of bulk superconductors by laser-induced heating. J. Appl. Phys. 68, 48824884 (1990).  
28. Burgi, D. S. & Dovichi, N. J. Submicrometer resolution images of absorbance and thermal diffusivity with the photothermal microscope. Appl. Opt. 26, 4665–4669 (1987).  
29. Samolis, P. D. et al. Label-free imaging of fibroblast membrane interfaces and protein signatures with vibrational infrared photothermal and phase signals. Biomed. Opt. express 12, 303–319 (2021).  
30. Stringari, C. et al. Phasor approach to fluorescence lifetime microscopy distinguishes different metabolic states of germ cells in a live tissue. Proc. Natl Acad. Sci. 108, 13582–13587 (2011).  
31. Zharov, V. P. & Lapotko, D. O. Photothermal imaging of nanoparticles and cells. IEEE J. Sel. Top. Quantum Electron. 11, 733–751 (2005).  
32. Selmke, M., Braun, M. & Cichos, F. Photothermal single-particle microscopy: detection of a nanolens. Acs Nano 6, 2741–2749 (2012).  
33. Bergman, T. L., Incropera, F. P., DeWitt, D. P. & Lavine, A. S. Fundamentals of Heat and Mass Transfer (John Wiley & Sons, 2011).  
34. Chen, X., Chen, Y., Yan, M. & Qiu, M. Nanosecond photothermal effects in plasmonic nanostructures. ACS nano 6, 2550–2557 (2012).  
35. Datta, R., Heaster, T. M., Sharick, J. T., Gillette, A. A. & Skala, M. C. Fluorescence lifetime imaging microscopy: fundamentals and advances in instrumentation, analysis, and applications. J. Biomed. Opt. 25, 071203 (2020).  
36. Muir, R. D., Sullivan, S. Z., Oglesbee, R. A. & Simpson, G. J. Synchronous digitization for high dynamic range lock-in amplification in beam-scanning microscopy. Rev. Sci. Instrum. 85, 033703 (2014).  
37. Sullenberger, R., Redmond, S., Crompton, D., Stolyarov, A. & Herzog, W. Spatially-resolved individual particle spectroscopy using photothermal modulation of Mie scattering. Opt. Lett. 42, 203–206 (2017).  
38. Maus, M. et al. An experimental comparison of the maximum likelihood estimation and nonlinear least-squares fluorescence lifetime analysis of single molecules. Anal. Chem. 73, 20782086 (2001).  
39. Brochon, J.-C. [13] Maximum entropy method of data analysis in time resolved spectroscopy. Methods Enzymol. 240, 262–311 (1994).  
40. Swaminathan, R. & Periasamy, N. Analysis of fluorescence decay by the maximum entropy method: Influence of noise and analysis parameters on the width of the distribution of lifetimes. Proc. Indian Acad. Sci.—Chem. Sci. 108, 39 (1996).  
41. Ali, U., Karim, K. J. B. A. & Buang, N. A. A review of the properties and applications of poly (methyl methacrylate)(PMMA). Polym. Rev. 55, 678–705 (2015).  
42. Wang, Y. et al. Raman–deuterium isotope probing to study metabolic activities of single bacterial cells in human intestinal microbiota. Microb. Biotechnol. 13, 572583 (2020).  
43. Rodionova, M. V. et al. Biofuel production: challenges and opportunities. Int. J. Hydrog. Energy 42, 8450–8461 (2017).  
44. Wiegand, I., Hilpert, K. & Hancock, R. E. Agar and broth dilution methods to determine the minimal inhibitory concentration (MIC) of antimicrobial substances. Nat. Protoc. 3. 163 (2008).  
45. Lad, M. D., Birembaut, F., Matthew, J. M., Frazier, R. A. & Green, R. J. The adsorbed conformation of globular proteins at the air/water interface. Phys. Chem. Chem. Phys. 8, 2179–2186 (2006).  
46. Spadea, A., Denbigh, J., Lawrence, M. J., Kansiz, M. & Gardner, P. Analysis of fixed and live single cells using optical photothermal infrared with concomitant Raman spectroscopy. Anal. Chem. 93, 3938–3950 (2021).  
47. Pavlovetc, I. M. et al. Infrared photothermal heterodyne imaging: contrast mechanism and detection limits. J. Appl. Phys. 127, 165101 (2020).  
48. Wang, L. & Xu, X. G. Scattering-type scanning near-field optical microscopy with reconstruction of vertical interaction. Nat. Commun. 6, 1–9 (2015).  
49. Kim, B., Jahng, J., Sifat, A., Lee, E. S. & Potma, E. O. Monitoring fast thermal dynamics at the nanoscale through frequency domain photoinduced force microscopy. J. Phys. Chem. C 125, 7276–7286 (2021).  
50. Fimpel, P. et al. Boxcar detection for high-frequency modulation in stimulated Raman scattering microscopy. Appl. Phys. Lett. 112, 161101 (2018).  
51. Vavilov, V. P. & Burleigh, D. D. Review of pulsed thermal NDT: physical principles, theory and data processing. Ndt E Int. 73, 28–52 (2015).  
52. Poudel, A., Shrestha, S. S., Sandhu, J. S., Chu, T. P. & Pergantis, C. G. Comparison and analysis of acoustography with other NDE techniques for foreign object inclusion detection in graphite epoxy composites. Compos. B: Eng. 78, 86–94 (2015).  
53. Toivanen, J. et al. 3D thermal tomography with experimental measurement data. Int. J. Heat. Mass Transf. 78, 11261134 (2014).  
54. Christofferson, J. et al. Microscale and nanoscale thermal characterization techniques. I. Electron. Packaging 130.041101 (2008)  
55. Kucsko, G. et al. Nanometre-scale thermometry in a living cell. Nature 500, 5458 (2013).  
56. Mecklenburg, M. et al. Nanoscale temperature mapping in operating microelectronic devices. Science 347, 629–632 (2015).  
57. Chen, Z. et al. Imaging local heating and thermal diffusion of nanomaterials with plasmonic thermal microscopy. ACS Nano 9, 11574–11581 (2015).  
58. Chae, J. et al. Nanophotonic atomic force microscope transducers enable chemical composition and thermal conductivity measurements at the nanoscale. Nano Lett. 17, 5587–5594 (2017).  
59. Katzenmeyer, A. M. et al. Mid-infrared spectroscopy beyond the diffraction limit via direct measurement of the photothermal effect. Nanoscale 7, 17637–17641 (2015).  
60. Bouzin, M. et al. Photo-activated raster scanning thermal imaging at subdiffraction resolution. Nat. Commun. 10, 1–9 (2019).  
61. Jiang, Y. et al. Optoacoustic brain stimulation at submillimeter spatial precision. Nat. Commun. 11, 1–9 (2020).  
62. Ling, T. et al. High-speed interferometric imaging reveals dynamics of neuronal deformation during the action potential. Proc. Natl Acad. Sci. 117, 1027810285 (2020).  
63. Nedosekin, D. A., Galanzha, E. I., Dervishi, E., Biris, A. S. & Zharov, V. P. Super‐resolution nonlinear photothermal microscopy. Small 10, 135–142 (2014).  
64. Zharov, V. P. Ultrasharp nonlinear photothermal and photoacoustic resonances and holes beyond the spectral limit. Nat. Photonics 5, 110–116 (2011).  
65. Rajakarunanayake, Y. & Wickramasinghe, H. Nonlinear photothermal imaging. Appl. Phys. Lett. 48, 218–220 (1986).  
66. He, J., Miyazaki, J., Wang, N., Tsurui, H. & Kobayashi, T. Label-free imaging of melanoma with nonlinear photothermal microscopy. Opt. Lett. 40, 1141–1144 (2015).

## Acknowledgements

The work is supported by R35GM136223, R01AI141439, and R01CA224275 to J.X.C.

## Author contributions

L. L., J.Y., and J.X.C. conceived the idea. J.Y. and L.L. carried out modeling, PDI experiments, and analyzed the data. J.Y. and Y.Z. performed the PHI experiments. H.N. contributed to theoretical analysis. Y.T. prepared the cancer cells, M.Z. prepared the E. coli samples, Y.B. provided an initial demonstration of metabolism imaging in E. coli. J.Y. drafted the manuscript and all authors contributed to the manuscript writing. Th authors thank Celalettin Yurdakul for the helpful discussion.

## Competing interests

J.X.C. declares a financial interest with Photothermal Spectroscopy Corp and Vibronix Inc. The rest of the authors declare no competing interest.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-021-27362-w.

Correspondence and requests for materials should be addressed to Ji-Xin Cheng.

Peer review information Nature Communications thanks Matz Liebel and the other anonymous reviewers for their contribution to the peer review of this work. Peer reviewer reports are available.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/07542d07abb1b54167dd79fa2a4c8c9814673505400e754d3e54eff688a5a499.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unles indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org licenses/by/4.0/.

© The Author)202