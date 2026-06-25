## Multiplex Coherent Anti-Stokes Raman Scattering Microspectroscopy and Study of Lipid Vesicles

Ji-xin Cheng, Andreas Volkmer,† Lewis D. Book,‡ and X. Sunney Xie\*

Department of Chemistry and Chemical Biology, Har ard Uni ersity, Cambridge, Massachusetts 02138

Recei ed: March 15, 2002; In Final Form: July 19, 2002

We report a theoretical description and experimental implementation of multiplex coherent anti-Stokes Raman scattering (M-CARS) microspectroscopy using a picosecond pump beam and a femtosecond Stokes beam. The effect of the chirp in the Stokes pulse on a M-CARS spectrum is studied. Polarization-sensitive detection is utilized for suppression of the nonresonant background and for selective detection of spectrally overlapped Raman bands. M-CARS spectra of liposomes in the C H stretching vibration region were acquired. Polarization CARS imaging of lipids in live cells based on the M-CARS spectra is demonstrated.

## Introduction

Coherent anti-Stokes Raman scattering (CARS) is a nonlinear Raman process in which a pump beam at frequency $\omega _ { \mathrm { p } }$ and a Stokes beam at frequency ωs are mixed in a sample to generate a signal at the anti-Stokes frequency of $\omega _ { \mathrm { a s } } = 2 \omega _ { \mathrm { p } } - \omega _ { \mathrm { s } }$ . CARS ) -microscopy was put forward as a vibrational imaging tool in 1982.1 High-quality three-dimensional (3D) CARS imaging was achieved by using two tightly focused near-IR femtosecond laser beams with a collinear beam geometry.2 A series of recent advances have made CARS microscopy a powerful technique for biological imaging.3 10

It has been shown that excitation by two picosecond lasers3 gives a much higher ratio of the resonant signal to the nonresonant background in CARS microscopy than two femtosecond lasers.2 This is because the spectral width of a picosecond beam is comparable to the Raman line width and the excitation power can be fully utilized to generate the resonant CARS signal. High-speed imaging of live cells at an acquisition rate of several seconds per frame (512 512 pixels) has been achieved by laser-scanning CARS microscopy with two synchronized picosecond pulse trains.9 However, it is timeconsuming to record a CARS spectrum by tuning the Stokes beam frequency point by point,3,5,11 which makes it difficult to follow dynamical changes in a CARS spectrum.

In this paper, we report multiplex CARS (M-CARS) microspectroscopy using a picosecond pump beam and a femtosecond Stokes beam for fast acquisition of CARS spectra of a microscopic sample. The femtosecond Stokes pulse has a broad spectral width that allows simultaneous detection over a wide range of Raman shifts. The energy level diagram of CARS with a pico/femto excitation scheme is shown in Figure 1.

In previous work of M-CARS spectroscopy ,12 15 a narrowband picosecond dye laser and a broad-band picosecond laser using multiple dyes were employed as the pump and the Stokes beam, respectively. Our setup is distinguished from previous work in that we use a near-IR laser system consisting of a femtosecond Ti:sapphire laser synchronized with a picosecond Ti:sapphire laser. The spectral profile of Ti:sapphire lasers is much more stable than that of dye lasers. The use of near-IR excitation also reduces photodamage of biological samples. Moreover, instead of using a noncollinear beam geometry as in previous work,12 15 the pump and Stokes laser beams are collinearly overlapped2,16 and tightly focused into a sample using an objective lens of high numerical aperture (NA). Under the tight focusing condition, the phase-matching condition for forward CARS is fulfilled17 and insensitive to the laser wavelength in a collinear beam geometry, which allows spectral recording over a wide spectral range without changing the alignment. The tight focusing condition is particularly suitable for characterization of small objects such as intracellular organelles with high spatial resolution and high sensitivity.

![](images/31dcef329cf965af22f39ca6131d2bf90970cab56123d018ab77cb15d8e2d80e.jpg)

<details>
<summary>text_image</summary>

ωₚ
ωₛ
ω'ₚ
ωₐₛ
Vibrational
levels
</details>

Figure 1. Energy level diagram of CARS using a narrow-band picosecond pump/probe beam and a broad-band femtosecond Stokes beam.

A major shortcoming of CARS spectroscopy is the existence of a nonresonant background that limits the detection sensitivity. Polarization-sensitive detection18,19 was extensively applied in M-CARS to suppress the nonresonant background.20 It was also used to determine the depolarization ratios of Raman bands,21 and to resolve spectrally overlapped Raman bands.22 Recently, polarization CARS microscopy has been developed for imaging of intracellular protein distribution based on the vibrational contrast from the amide I band.5 In this paper, we make use of polarization-sensitive detection in our M-CARS microscope to suppress the nonresonant background and to reveal the polarization properties of Raman bands.

CARS microscopy provides a sensitive means of imaging lipid membranes2,9 by taking advantage of the high density of C H bonds in lipids. Although lipid membranes have been

\* Corresponding author. E-mail: Xie@chemistry.harvard.edu. † Present address: 3 Physikalisches Institut, Universita¨t Stuttgart, Pfaffenwaldring 57, 70550 Stuttgart, Germany. ‡ Present address: BlueLeaf Networks, Sunnyvale, CA 94085.

![](images/1a029fe28a760324da7412736d99c22ed9c5b0bc606124565a3177ed0353f914.jpg)

<details>
<summary>text_image</summary>

(A)
Analyzer
y
E_s
P_nr
φ
α
β
E_p
x
0
(B)
APD
Spectrometer
Flip mirror
ω_as
Filter
Polarizer
Objective
Sample
Objective
QW HW
ω_p (5 ps)
ω_s (90 fs)
Dichroic
</details>

Figure 2. (A) Polarization vectors of the pump $( E _ { \mathrm { p } } )$ and the Stokes $( E _ { \mathrm { s } } )$ fields, the resonant $( P _ { \mathrm { r } } )$ and nonresonant $( P _ { \mathrm { n r } } )$ parts of the induced third-order polarization, and the analyzer. (B) Schematic of the multiplex CARS microscope. Key: QW, quarter-wave plate; HW, half-wave plate; APD, avalanche photodiode.

extensively studied by spontaneous Raman spectroscopy $, ^ { 2 3 }$ little is known about their CARS spectra. In this paper, we apply M-CARS microspectroscopy to study the C H stretching -vibration in single lipid vesicles. The recorded M-CARS spectra are used for vibrational imaging of lipids in live cells with polarization-sensitive detection.

## Theoretical Description of M-CARS with Pico/Femto Excitation

In our implementation of M-CARS, a femtosecond Stokes pulse and a picosecond pump/probe pulse temporally overlapped with the Stokes pulse are used. In the frequency domain, the third-order polarization induced by parallel-polarized pump and Stokes beams can be written $\mathrm { a s } ^ { 3 , \bar { 2 } 4 }$

$$
\begin{array}{l} P ^ {(3)} (\omega_ {\mathrm{as}}) = \\ \int_ {- \infty} ^ {+ \infty} d \omega_ {p} \int_ {- \infty} ^ {+ \infty} d \omega_ {s} \int_ {- \infty} ^ {+ \infty} d \omega_ {p} ^ {\prime} \chi_ {1 1 1 1} ^ {(3)} (- \omega_ {a s}; \omega_ {p}, - \omega_ {s}, \omega_ {p} ^ {\prime}) \\ E _ {\mathrm{p}} \left(\omega_ {\mathrm{p}}\right) E _ {\mathrm{s}} \left(\omega_ {\mathrm{s}}\right) E _ {\mathrm{p}} \left(\omega_ {\mathrm{p}} ^ {\prime}\right) \delta \left(\omega_ {\mathrm{p}} - \omega_ {\mathrm{s}} + \omega_ {\mathrm{p}} ^ {\prime} - \omega_ {\mathrm{as}}\right) (1) \\ \end{array}
$$

where $E _ { \mathrm { p } } ( \omega _ { \mathrm { p } } ) , E _ { \mathrm { s } } ( \omega _ { \mathrm { s } } )$ , and $E _ { \mathrm { p } } ( \omega _ { \mathrm { p } } ^ { \prime } )$ are the pump, Stokes, and probe fields, respectively. $\chi _ { 1 1 1 1 } ^ { ( \bar { 3 } ) }$ is a component of the thirdorder susceptibility. Because the spectral profile of the Stokes beam is much broader than that of the pump beam, we first perform the integration over the Stokes field. Then eq 1 can be recast as

$$
\begin{array}{l} P ^ {(3)} \left(\omega_ {\mathrm{as}}\right) = \int_ {- \infty} ^ {+ \infty} \mathrm{d} \omega_ {\mathrm{p}} \int_ {- \infty} ^ {+ \infty} \mathrm{d} \omega_ {\mathrm{p}} ^ {\prime} \chi_ {1 1 1 1} ^ {(3)} \left(- \omega_ {\mathrm{as}}; \omega_ {\mathrm{p}}, - \omega_ {\mathrm{s}}, \omega_ {\mathrm{p}} ^ {\prime}\right) \\ E _ {\mathrm{p}} (\omega_ {\mathrm{p}}) E _ {\mathrm{s}} (\omega_ {\mathrm{s}}) E _ {\mathrm{p}} (\omega_ {\mathrm{p}} ^ {\prime}) (2) \\ \end{array}
$$

where $\omega _ { \mathrm { s } } = \omega _ { \mathrm { a s } } - \omega _ { \mathrm { p } } - \omega _ { \mathrm { p } } ^ { \prime } .$ The transform-limited Gaussian pump pulse is written as

$$
E _ {\mathrm{p}} (\omega) = E _ {\mathrm{p}} \exp \left[ - 2 \ln 2 \left(\frac {\omega - \omega_ {\mathrm{p0}}}{\Delta \omega_ {\mathrm{p}}}\right) ^ {2} \right] \tag {3}
$$

where $E _ { \mathrm { p } } , \ \omega _ { \mathrm { p 0 } }$ and $\Delta \omega _ { \mathrm { p } }$ refer to the peak amplitude, central frequency, and spectral full width at half-maximum (fwhm) of the pump field. For the femtosecond Stokes pulse, there usually exists a chirp due to group velocity dispersion. In practice, it might be preferred to introduce a chirp in the Stokes pulse to reduce the photodamage of a sample. The effect of such a chirp on a M-CARS spectrum should be evaluated and can be conveniently analyzed in the frequency domain using eq 2. A linearly chirped Stokes pulse with a constant spectral fwhm of $\Delta \omega _ { \mathrm { s } }$ can be described $\mathrm { a s } ^ { 2 5 }$

$$
\begin{array}{l} E _ {\mathrm{s}} (\omega) = \\ E _ {\mathrm{s}} \exp \left[ - \frac {1}{4} \left(\frac {a}{a ^ {2} + b ^ {2}}\right) \left(\omega - \omega_ {\mathrm{s0}}\right) ^ {2} - \frac {i}{4} \left(\frac {b}{a ^ {2} + b ^ {2}}\right) \left(\omega - \omega_ {\mathrm{s0}}\right) ^ {2} \right] \tag {4} \\ \end{array}
$$

where $E _ { \mathrm { s } }$ refers to the peak amplitude and $\omega _ { \mathrm { s 0 } }$ refers to the central frequency of the Stokes field. The parameter a is related to the temporal width (τ, fwhm) of the chirped pulse by $a = 2$ $\scriptstyle \ln 2 / \tau ^ { 2 }$ , and the parameter $b$ )is related to the ratio (R) of the temporal width of the chirped pulse to its transform-limited temporal width by $b = a \sqrt { R ^ { 2 } - 1 }$ . For a transform-limited ) -Stokes pulse, R equals 1.0 and τ equals $0 . 4 4 / \Delta \omega _ { \mathrm { s } }$ s.

$\chi _ { 1 1 1 1 } ^ { ( 3 ) }$ in eqs 1 and 2 is the sum of a nonresonant part $( \mathbb { \chi } _ { 1 1 1 1 } ^ { \mathrm { n r } } )$ arising from the electronic contributions and a vibrationally resonant part $( \mathbb { \chi } _ { 1 1 1 1 } ^ { \mathrm { r } } )$ . Away from any one-photon electronic resonance, $\chi _ { 1 1 1 1 } ^ { \mathrm { n r } }$ is a real constant and $\chi _ { 1 1 1 1 } ^ { \mathrm { r } }$ assumes the following form,

$$
\chi_ {1 1 1 1} ^ {\mathrm{r}} (\omega_ {\mathrm{p}} - \omega_ {\mathrm{s}}) = \sum_ {j} \frac {A _ {j}}{\Omega_ {j} - (\omega_ {\mathrm{p}} - \omega_ {\mathrm{s}}) - i \Gamma_ {j}} \tag {5}
$$

Here, $\Omega _ { j }$ and $\Gamma _ { j }$ denote the vibrational frequency and the Raman line half-width, respectively. $A _ { j }$ is a constant related to the spontaneous Raman scattering cross-section. The M-CARS spectrum is calculated from

$$
I _ {\mathrm{CARS}} (\omega_ {\mathrm{as}}) = | P ^ {(3)} (\omega_ {\mathrm{as}}) | ^ {2} \tag {6}
$$

For polarization-sensitive detection, the polarization direction of the Stokes beam is rotated by an angle of $\phi$ with respect to the pump beam (Figure 2A). Away from any one-photon electronic resonance, the nonresonant CARS signal is linearly polarized along the angle  determined by tan ${ \bf { a } } = \rho ^ { \mathrm { { n r } } }$ tan φ. $\rho ^ { \mathrm { n r } } = \chi _ { 1 2 2 1 } ^ { \mathrm { n r } } / \chi _ { 1 1 1 1 } ^ { \mathrm { n r } }$ R R ) Fis the depolarization ratio of the nonresonant F )CARS field and is equal to 1/3 following the rule of Kleimann’s symmetry.26 The nonresonant part of $P ^ { ( 3 ) }$ passing through an analyzer polarizer along the angle $\varphi$ can be written as

$$
\begin{array}{l} P _ {\mathrm{nr}} ^ {(3)} (\omega_ {\mathrm{as}}, \varphi) = (\cos \phi \cos \varphi + \\ \begin{array}{r} \rho^ {\mathrm{nr}} \sin \phi \sin \varphi) \int_ {- \infty} ^ {+ \infty} \mathrm{d} \omega_ {\mathrm{p}} \int_ {- \infty} ^ {+ \infty} \mathrm{d} \omega_ {\mathrm{p}} ^ {\prime} \chi_ {1 1 1 1} ^ {\mathrm{nr}} E _ {\mathrm{p}} (\omega_ {\mathrm{p}}) \\ E _ {\mathrm{s}} (\omega_ {\mathrm{s}}) E _ {\mathrm{p}} (\omega_ {\mathrm{p}} ^ {\prime}) (7) \end{array} \\ \end{array}
$$

It has been shown that the highest signal-to-background ratio is obtained when the angle φ is $7 1 . 6 ^ { \circ }$ and is $4 5 ^ { \circ } . ^ { \overline { { 1 8 } } }$ The angle $\varphi$ is set to be $1 3 5 ^ { \circ }$ Rfor suppression of the nonresonant background.

The polarization of the vibrationally resonant CARS signal is related to the spontaneous Raman depolarization ratio, which is 0.75 for an asymmetric band and is between 0 and 0.75 for a totally symmetric band. For the jth Raman line, $P _ { r , j } ^ { ( 3 ) }$ is polarized along an angle of $\beta _ { j }$ (Figure 2A) that is determined by tan $\beta _ { j } = \rho _ { j } ^ { \mathrm r }$ tan φ. $\rho _ { j } ^ { \mathrm r } = \chi _ { 1 2 2 1 } ^ { \mathrm r , j } / \chi _ { 1 1 1 1 } ^ { \mathrm r , j }$ is the depolarization ratio of the $\mathrm { C A R S }$ F ) band and is equal to that of the corresponding spontaneous Raman band.19 The resonant third-order polarization passing through the polarization analyzer can be written as

$$
P _ {\mathrm{r}, j} ^ {(3)} (\omega_ {\mathrm{as}}, \varphi) = (\cos \phi \cos \varphi +
$$

$$
\rho_ {j} ^ {\mathrm{r}} \sin \phi \sin \varphi) \int_ {- \infty} ^ {+ \infty} \mathrm{d} \omega_ {\mathrm{p}} \int_ {- \infty} ^ {+ \infty} \mathrm{d} \omega_ {\mathrm{p}} ^ {\prime} \chi_ {1 1 1 1} ^ {\mathrm{r}, j} E _ {\mathrm{p}} (\omega_ {\mathrm{p}}) E _ {\mathrm{s}} (\omega_ {\mathrm{s}}) E _ {\mathrm{p}} (\omega_ {\mathrm{p}} ^ {\prime}) \tag {8}
$$

The polarization M-CARS spectrum is calculated from

$$
I _ {\mathrm{P-CARS}} (\omega_ {\mathrm{as}}, \varphi) = | P _ {\mathrm{nr}} ^ {(3)} (\omega_ {\mathrm{as}}, \varphi) + \sum_ {j} P _ {\mathrm{r}, j} ^ {(3)} (\omega_ {\mathrm{as}}, \varphi) | ^ {2} \tag {9}
$$

## Experiments

The picosecond pump and the femtosecond Stokes beams were from two Ti:sapphire lasers (Spectra-Physics, Tsunami) that were pumped by a 532 nm continuous-wave (cw) laser (Spectral-Physics, 10 W Millennia) and synchronized to an 80 MHz external clock (Spectra-Physics, Lok-to-Clock). The timing jitter between the two pulse trains was around 0.5 ps. The time delay between the two pulse trains was electronically adjustable by the Lok-to-Clock system. To reduce the average excitation power but keep a high peak power at the sample, the pulse repetition rate was reduced to 400 kHz using a Pockel’s cell (Conoptics, Model 350-160) in each beam. The picosecond pump beam was tuned to 713 nm with a spectral fwhm of 2.9 $\mathrm { { \bar { c } m ^ { - 1 } } }$ , corresponding to a transform-limited temporal fwhm of 5.0 ps. The femtosecond Stokes beam was tuned to 900 nm with a spectral fwhm of $1 6 0 \mathrm { c m } ^ { - 1 }$ , corresponding to a transformlimited temporal fwhm of 91 fs. The frequency difference $( \omega _ { \mathsf { p } }$ $- \it \Delta \phi _ { \mathrm { s } } )$ covered the spectral region of the aliphatic C H - -stretching vibration from 2750 to 3050 cm 1. The laser for the Stokes beam can be easily converted from femtosecond to picosecond configuration for CARS imaging with a high spectral resolution.3

The two laser beams were collinearly combined and sent into an inverted microscope (Nikon, TE300). A schematic of our multiplex CARS microscope is depicted in Figure 2B. A water objective (Olympus, UPIANAPO, 60X, $\mathrm { N A } = 1 . 2 )$ was used )to focus the beams into a sample mounted on a 3D scanning stage (Mad-city, Nano-Bio3200). The CARS signal was parfocally collected in the forward direction with an oil objective lens (Nikon, PLANAPO, 60X, NA 1.4) and spectrally isolated )from the excitation beams by use of three band-pass filters (Coherent, 35-5081, 40 nm bandwidth). An avalanche photodiode (EG&G, Model SPCM-AQR-14) was used for recording a CARS image. A spectrograph (Acton Research Corp., Spectrapro-150) equipped with a 1800 groves/mm grating and a liquid nitrogen cooled CCD detector (Princeton Instruments), was used for recording the CARS spectrum of a specific position in the sample. All the CARS spectra of samples were normalized by the nonresonant CARS spectra of the coverglass recorded with the same laser beams.

For polarization-sensitive detection, the Stokes beam was kept p-polarized to the dichroic combiner and the polarization of the pump beam was rotated from that of the Stokes beam by $7 1 . 6 ^ { \circ }$ with a half-wave plate (Figure 2B). A quarter-wave plate was used in the pump beam before the half-wave plate to compensate the birefringence mainly induced by the dichroic mirrors. A rotatable polarizer analyzer was used before the detectors either to suppress the nonresonant CARS background with an extinction ratio of 600:15 or to detect a particular vibrational band based on its depolarization ratio.

![](images/b9d11f05f849ffa781b43fbe8814e8e564e15de63e250ae96d6cfc0a42338d7e.jpg)

<details>
<summary>line chart</summary>

| ω_p−ω_s / cm⁻¹ | No chirp (R=1.0) | Chirped (R=50) |
| -------------- | ---------------- | -------------- |
| 2700           | 0                | 0              |
| 2800           | ~5               | ~4             |
| 2900           | ~22              | ~21            |
| 3000           | ~10              | ~8             |
| 3100           | 0                | 0              |
</details>

![](images/fcd16cacecb1086208c68f33ceb9a908f82b6435d793cae4a5b78c1fb577ed2c.jpg)

<details>
<summary>line chart</summary>

| ω_p - ω_s / cm⁻¹ | No chirp (R=1.0) | Chirped (R=50) |
| ---------------- | ---------------- | -------------- |
| 2700             | 0                | 0              |
| 2800             | ~5               | ~5             |
| 2900             | ~28              | ~28            |
| 3000             | ~10              | ~10            |
| 3100             | 0                | 0              |
</details>

![](images/df8f3550a9b099b17926e5827c8306980912de98f490c3050cb499b86d5b2bea.jpg)

<details>
<summary>line chart</summary>

| ω_p - ω_s / cm⁻¹ | Normalized CARS Int. |
| ---------------- | -------------------- |
| 2700             | 1.0                  |
| 2800             | 1.4                  |
| 2900             | 1.3                  |
| 3000             | 1.2                  |
| 3100             | 1.0                  |
</details>

Figure 3. (A) Calculated CARS spectra of a model sample with only nonresonant contribution. (B) Calculated CARS spectra of a model sample containing three Raman bands. (C) The spectra shown in (B) normalized with the nonresonant CARS spectra shown in (A) under the same chirp condition. A transform-limited 5-ps pump pulse centered at $1 4 0 2 5 ~ \mathrm { c m } ^ { - 1 }$ and a Stokes pulse centered at $\mathrm { { \dot { 1 } } 1 \dot { 1 } 1 1 \dot { 1 } c m ^ { - 1 } }$ are used. The solid lines represent the results with a transform-limited Stokes pulse (90 fs), and the open circles represent the results with the Stokes pulse chirped to 4.5 ps. R is the ratio of the temporal width of the chirped Stokes pulse to that of the nonchirped Stokes pulse. The parameters (see eq 5) for the three Raman bands are $\chi _ { 1 1 1 1 } ^ { \mathrm { n r } } = 0 . 5 \mathrm { a u } , A _ { i }$ $\dot { ( \ i = 1 , 2 , 3 ) } = 1 . \dot { 0 }$ au, $\Gamma _ { i } ( i = 1 , 2 , 3 ) = 7 . 5$ cm 1 , $\Omega _ { \mathrm { 1 } } = 2 8 0 0$ cm 1 , $\Omega _ { 2 } = 2 9 0 0$ )cm 1 , $\Omega _ { 3 } = 3 0 0 0 ~ \mathrm { c m } ^ { - 1 }$ .

In our setup, the chirp of the 5-ps pump pulse was negligible, whereas the femtosecond Stokes pulse was significantly chirped because it passed through several dispersive optics, such as the Faraday isolator and the Pockel’s cell. The temporal width was measured to be 600 fs for the Stokes pulse before going into the microscope. We estimate that the chirp induced by the objective lens was negligible compared to that by the dispersive optics mentioned above.

DSPC (1,2-distearoyl-sn-glycero-3-phosphocholine) and DOPC (1,2-dioleoyl-sn-glycero-3-phosphocholine) powders were purchased from Avanti Polar Lipids Inc. and used without further purification. The phase transition temperatures for DSPC and DOPC are 55 and $- 2 0 ^ { \circ } \mathrm { C } ,$ , respectively. Multilamellar vesicles were prepared following a recipe provided by Avanti Polar Lipids Inc. Briefly, the powder was hydrated with distilled water. The lipid suspension was then stirred for 30 min on a vortex. For DSPC, the lipid suspension temperature was maintained above the phase transition temperature during the hydration period by using a water bath. The formation of multilamellar vesicles with a large size distribution (from less than 1 µm to more than 10 µm) was verified with a phase-contrast microscope. The vesicle suspension was sandwiched between two #1.5 coverslips separated by a 150-µm spacer. Spontaneous Raman spectra of vesicles were recorded on a Raman microspectrograph (Jobin Yvon/Spec, LabRam) with a 1800 groves/mm grating and a 15 mW HeNe laser at 632.8 nm.

![](images/a214a12b2877cd165ccb421f7f86de393e73e7154de6e01c0953f8499c2ee8ad.jpg)

<details>
<summary>line chart</summary>

| Raman shift / cm⁻¹ | Intensity (a.u.) |
| ------------------ | ---------------- |
| 2800               | 0.0              |
| 2850               | 0.8              |
| 2900               | 0.6              |
| 2950               | 0.4              |
| 3000               | 0.2              |
</details>

![](images/f9f70cc62416726fb582f8a2259c81863f22c5119ae2817d9fa4bf17531a9219.jpg)

<details>
<summary>line chart</summary>

| ωp−ωs / cm⁻¹ | Normalized CARS Int. |
| ------------ | -------------------- |
| 2700         | 0.8                  |
| 2800         | 1.2                  |
| 2850         | 2.5                  |
| 2900         | 1.0                  |
| 3000         | 0.5                  |
</details>

Figure 4. (A) Spontaneous Raman spectrum (dots) of a DSPC vesicle in the C H stretching vibration region and its decomposition into 7 -Lorentzian lines (solid). See Table 1 for the parameters. (B) Normalized CARS spectrum (dots) of the DSPC vesicle indicated in the inset by an arrow. The acquisition time was 1.0 s. The average powers of the parallel-polarized pump and Stokes beams were 0.6 and 0.3 mW, respectively. The solid curve is the fit with eq 11. The inset is a CARS image $( 4 8 ~ \times ~ 2 4$ µm2 ) that locates the lipid vesicles. This image consisting of $5 1 2 \times 2 5 6$ pixels was acquired with the same laser pulses at a scanning rate of 0.5 ms/pixel.

NIH3T3 cells (ATCC, CRL-1658, Manassas, VA) were cultured in the Dullbecco’s modified Eagle’s medium (ATCC, 30-2002) supplemented with 10% bovine calf serum. The cells grown on a chambered coverglass (Lab-Tek, #155360, Rochester, NY) were used for CARS imaging without staining. All experiments were carried out at a room temperature of 21 $^ { \circ } \mathrm { C } .$

## Results and Discussion

Effect of Pulse Chirping. Using eqs $2 ^ { - } { } ^ { 6 } ,$ we can investigate -theoretically the effects of the chirp in the Stokes pulse on a M-CARS spectrum. We assume that the pump field is a transform-limited 5-ps pulse, as used in our experiment. Nonresonant CARS spectra with a transform-limited Stokes pulse (90 fs) and a chirped Stokes pulse (4.5 ps, R 50) are )displayed in Figure 3A. The fwhm of the CARS spectral profile is reduced from 164 to $1 3 8 ~ \mathrm { { c m ^ { - 1 } } }$ upon pulse chirping that introduces a quadratic phase profile in the Stokes pulse (see eq 4). In the time domain, this chirp effect can be explained as a reduction of temporal overlap with the pump pulse for the frequency components away from the central Stokes frequency. Our calculation indicates that the fwhm of the CARS spectral profile decreases linearly with increasing R (not shown). Next, we consider a model sample containing three Raman bands located in the center and at the two edges of the CARS spectra profile. Changes in the CARS spectral profile because of the Stokes pulse chirping can be seen from Figure 3B. However, Figure 3C shows that the CARS spectra of the same sample normalized by the nonresonant CARS spectra under the same chirp condition display little difference. The above analysis implies that one should normalize CARS spectra of a sample by a nonresonant CARS spectrum recorded under the same excitation condition, as we did in our experiment.

TABLE 1: Raman and CARS Parameters for the C H -Stretching Vibrational Bands of DSPC Recorded at Room Temperaturea

<table><tr><td>peak position $\Omega_{i}$  (cm $^{-1}$ )</td><td>FWHM2 $\Gamma_{i}$  (cm $^{-1}$ )</td><td>strength $a_{i}$  (a.u.)</td><td> $A_{j}/\chi^{nr}_{\text{sampl}}$  (cm)</td></tr><tr><td>2846.52 (09)</td><td>10.9 (03)</td><td>0.271 (13)</td><td>4.40 (15)</td></tr><tr><td>2860.41 (28)</td><td>19.3 (12)</td><td>0.287 (22)</td><td>5.14 (18)</td></tr><tr><td>2882.18 (11)</td><td>15.0 (05)</td><td>0.368 (18)</td><td>5.30 (27)</td></tr><tr><td>2904.03 (49)</td><td>29.6 (27)</td><td>0.298 (34)</td><td>6.02 (53)</td></tr><tr><td>2934.75 (46)</td><td>28.5 (24)</td><td>0.262 (28)</td><td>4.67 (67)</td></tr><tr><td>2964.8 (18)</td><td>20.1 (84)</td><td>0.040 (21)</td><td>0.20 (88)</td></tr><tr><td>2983.1 (13)</td><td>18.7 (37)</td><td>0.050 (14)</td><td>1.31 (77)</td></tr></table>

a Note: The numbers in parentheses are standard deviations of the last two digits.

Raman and M-CARS Spectra of Liposomes. The Raman spectrum of a mutilamellar DSPC vesicle in the C H stretching vibration region is shown in Figure $4 \mathrm { A } ,$ -. It has been established that the two bands at 2847 and 2882 $\mathrm { c m } ^ { - 1 }$ correspond to the symmetric and asymmetric $\mathrm { C H } _ { 2 }$ stretching vibrations, whereas the two bands at 2935 and $2 9 6 5 ~ \mathrm { c m ^ { - 1 } }$ correspond to the symmetric and asymmetric CH3 stretching vibrations, respectively.23 The two shoulders at 2860 and 2904 $\mathrm { c m } ^ { - 1 }$ arise from the Fermi resonance between the asymmetric CH stretching mode and the first overtones of the asymmetric CH2 and $\mathrm { C H } _ { 3 }$ deformation modes at 1437.4 and 1451.4 $\mathrm { c m } ^ { - 1 }$ (not shown). The spectrum in the 2750 3050 cm 1 region is well fitted as -a sum of seven Lorentzian bands

$$
I _ {\text { Raman }} (\omega) = y _ {0} + \sum_ {j} \frac {a _ {j} \Gamma_ {j} / \pi}{(\omega - \Omega_ {j}) ^ {2} + \Gamma_ {j} ^ {2}} \tag {10}
$$

The obtained peak positions, strengths, and line widths are listed in Table 1.

Figure 4B shows the CARS spectrum of an individual DSPC vesicle indicated in the inset image. The CARS spectrum is different from the Raman spectrum in that the asymmetric $\mathrm { C H } _ { 2 }$ stretching band exhibits a much lower intensity than the symmetric $\mathrm { C H } _ { 2 }$ stretching band. This can be explained as a consequence of the interference between the spectrally adjacent and overlapped CARS bands.27 In addition, all the peaks are slightly shifted toward lower wavenumbers because of their interference with the nonresonant CARS signal. Figure 4B indicates that the CARS band at $2 8 4 3 ~ \mathrm { c m ^ { - 1 } }$ corresponding to the symmetric CH vibration gives the highest contrast in CARS imaging of lipids.

We performed a least-squares fitting of the CARS spectrum of DSPC. The integration over the spectral profile of the pump beam in eq $^ 2$ was neglected in the fitting. This simplification is reasonable because the spectral fwhm $( 2 . 9 \ \mathrm { c m } ^ { - 1 } )$ of the pump pulse is much smaller than the typical Raman line width ( 15 $\mathrm { c m } ^ { - 1 } )$ . The normalized CARS signal is calculated as

![](images/9b896646b5e0689abe8a9e967a47395b9a3e29aeba51dc78661b0c445bfaf29f.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 2700               | 0.0              |
| 2800               | 0.0              |
| 2850               | 0.75             |
| 2900               | 0.6              |
| 2950               | 0.5              |
| 3000               | 0.1              |
</details>

![](images/b5334e2f5d5e20979a37b2b51712e8e38785862e90aa0c1a1aca4c3df1e42070.jpg)

<details>
<summary>line chart</summary>

| ωp−ωs / cm⁻¹ | Normalized CARS Int. |
| ------------ | -------------------- |
| 2700         | 0.3                  |
| 2800         | 0.4                  |
| 2850         | 0.9                  |
| 2900         | 0.4                  |
| 2950         | 0.1                  |
| 3000         | 0.0                  |
</details>

Figure 5. (A) Spontaneous Raman and (B) normalized CARS spectra of an individual DOPC vesicle in the C H stretching vibration region. -The CARS spectrum was acquired in 1.0 s with the parallel-polarized pump and Stokes beams at the same powers as in Figure 4.

$$
\begin{array}{l} I _ {\mathrm{CARS}} (\omega_ {\mathrm{p}} - \omega_ {\mathrm{s}}) = \\ \left(\frac {\chi_ {\text { sampl }} ^ {\mathrm{nr}}}{\chi_ {\text { glass }} ^ {\mathrm{nr}}}\right) ^ {2} \left| 1 + \sum_ {j} \frac {(A _ {j} / \chi_ {\text { sampl }} ^ {\mathrm{nr}})}{\Omega_ {j} - (\omega_ {\mathrm{p}} - \omega_ {\mathrm{s}}) - \mathrm{i} \Gamma_ {j}} \right| ^ {2} \tag {11} \\ \end{array}
$$

Here, $\chi _ { \mathrm { s a m p l } } ^ { \mathrm { n r } }$ and $\chi _ { \mathrm { g l a s s } } ^ { \mathrm { n r } }$ denote the nonresonant third-order susceptibility of the sample and of the coverglass, respectively. $\Omega _ { j }$ and $\Gamma _ { j }$ were fixed as the values in Table 1. The fit with eq 11 reproduces the main features of the CARS spectrum, as $\chi _ { \mathrm { s a m p l } } ^ { \mathrm { n r } } / \chi _ { \mathrm { g l a s s } } ^ { \mathrm { n r } }$ ( 0.003) and those for $A _ { j } / \chi _ { \mathrm { s a m p l } } ^ { \mathrm { n r } }$ are listed in the last column of (Table 1.

Unlike DSPC, which is in the gel state, DOPC is in the liquid crystalline state at room temperature. Spontaneous Raman and CARS spectra of an individual DOPC vesicle are shown in Figure 5. We found it difficult to perform a least-squares fitting of the CARS spectrum of DOPC because of the line broadening. Significant differences between the CARS spectrum of DSPC (Figure 4B) and that of DOPC (Figure 5B) can be seen. In the CARS spectrum of DOPC, the symmetric $\mathrm { C H } _ { 2 }$ stretching band displays a larger width and a broad shoulder is present on the right side. The differences between the two CARS spectra provides a way of distinguishing lipids of gel phase from lipids of liquid crystal phase by CARS imaging. For example, by tuning $\omega _ { \mathrm { p } } - \omega _ { \mathrm { s } }$ s from $2 9 1 5 \mathrm { t o } 2 9 7 5 \mathrm { c m } ^ { - 1 }$ , the CARS signal from -DSPC in the gel phase remains unchanged whereas the signal from DOPC in the liquid crystalline phase is reduced by 1 order of magnitude.

Polarization CARS Spectra and Imaging of Lipids. Figure 6 shows a series of polarization M-CARS spectra of the same DSPC vesicle (see the inset of Figure 4B) at different polarization directions of the analyzer. With the analyzer polarization along the y axis $( \varphi = 9 0 ^ { \circ } )$ , the $2 8 8 2 ~ \mathrm { c m ^ { - 1 } }$ band becomes prominent and the symmetric CH stretching band at $2 8 4 7 \mathrm { c m } ^ { - 1 }$ disappears (Figure 6D). With the analyzer polarization along the x axis $( \varphi = 0 ^ { \circ } )$ , the $2 8 4 7 ~ \mathrm { c m ^ { - 1 } }$ band is clearly detected (Figure 6B). A least-squares fitting of the spectrum recorded at $\varphi = 4 5 ^ { \circ }$ (Figure 6C) using eqs 7 9 and the parameters from ) -Table 1 gives depolarization ratios of 0.21 and 0.70 for the 2847 and $2 8 8 \bar { 2 } ~ \mathrm { c m } ^ { - 1 }$ bands, respectively. The above results imply that varying the orientation of the analyzer allows selective detection of these spectrally overlapped vibrational modes based on their different depolarization ratios.22

![](images/9303c33931ea772304f72de1e3e5a557b1a6d858ec56b60aeb2f024935804f1e.jpg)

<details>
<summary>line chart</summary>

| Condition | Peak Wavelength (Å) | Normalized CARS Int. |
| --------- | ------------------- | -------------------- |
| (A) φ = 135° | ~2850 | ~0.07 |
| (B) φ = 0° | ~2850 | ~0.28 |
</details>

![](images/9fa7cb713201950fa88d178d816522c6849f56d62b29ae15b2ee7a3187c06dcf.jpg)

<details>
<summary>line chart</summary>

| ωp−ωs / cm⁻¹ | Normalized CARS Int. (φ = 45°) | Normalized CARS Int. (φ = 90°) |
| ------------ | ------------------------------ | ------------------------------ |
| 2800         | ~0.2                           | ~0.1                           |
| 2850         | ~0.55                          | ~0.25                          |
| 2900         | ~0.1                           | ~0.05                          |
| 3000         | ~0.05                          | ~0.05                          |
</details>

Figure 6. Polarization-resolved multiplex CARS spectra of a DSPC vesicle at different angles of the polarization analyzer (æ). The average powers of the pump and the Stokes beam were 1.2 and 0.6 mW, respectively. The integration time for each spectrum was $2 . 0 \ s .$ The dashed curve in (C) is the fit with eqs 7 9 and the parameters in Table 1.

When the analyzer polarization is perpendicular to that of the nonresonant field $( \varphi = 1 3 5 ^ { \circ } )$ , the nonresonant background )is effectively suppressed (Figure 6A). The asymmetric $\mathrm { C H } _ { 2 }$ stretching band at $2 8 8 2 ~ \mathrm { c m } ^ { - 1 }$ does not show up because its polarization is close to that of the nonresonant CARS signal. However, the symmetric CH2 vibration band shows a high signal-to-background ratio. This indicates that polarization CARS permits vibrational imaging of lipids with a high contrast.

Polarization CARS imaging of lipids in a live NIH3T3 cell is demonstrated in Figure 7. We tuned $\omega _ { \mathrm { p } } - \omega _ { \mathrm { s } }$ to symmetric $\mathrm { C H } _ { 2 }$ vibration at $2 8 4 7 ~ \mathrm { c m ^ { - 1 } }$ -, the maximum position in the polarization M-CARS spectrum shown in Figure 6A. The nonresonant background from water and cellular organelles such as the nucleus was effectively suppressed. The lipid-rich features in the cytoplasm exhibit a high vibrational contrast, as can be seen from the intensity profile below the image.

![](images/d3a7d8085b9f01ce977c8b9febac730e9ec01456cb00a9a10f3a2aecc151a907.jpg)

<details>
<summary>line chart</summary>

| Distance (μm) | Counts |
| ------------- | ------ |
| 0             | 0      |
| 5             | 480    |
| 10            | 100    |
| 20            | 0      |
| 30            | 90     |
| 40            | 0      |
</details>

Figure 7. Polarization CARS $( \varphi = 1 3 5 ^ { \circ } )$ image of a live NIH3T3 )cell by use of 5-ps pump and Stokes beams at average powers of 1.3 and 0.9 mW, respectively. $\omega _ { \mathrm { p } } - \omega _ { \mathrm { s } }$ was tuned to 2847 cm-1 with the pump frequency at 14 048 $\mathrm { c } \dot { \mathrm { m } } ^ { - 1 }$ . The image consisting of 256 256 pixels was acquired at a scanning rate of 1.0 ms/pixel. The intensity profile along the line in the image is shown below the image.

## Conclusions

We have demonstrated multiplex CARS microspectroscopy using a femtosecond Ti:sapphire laser synchronized with a picosecond Ti:sapphire laser. We have shown that the chirp in the femtosecond Stokes pulse reduces the width of the nonresonant M-CARS spectral profile but induces little distortion to a M-CARS spectrum of a sample normalized with the nonresonant CARS spectrum recorded with the same pulses. Our setup allows high-speed spectral characterization of microscopic samples with high spectral resolution. We recorded the CARS spectra of DSPC vesicles in the gel phase and DOPC vesicles in the liquid crystalline phase, which provide valuable information (e.g., line profile and peak position) for CARS imaging of lipids. We have shown that polarization-sensitive detection can be used in the M-CARS microscope for effective suppression of the nonresonant background and for selective detection of the spectrally overlapped Raman bands. Guided by the recorded M-CARS spectra, we demonstrated highsensitivity polarization CARS imaging of lipids in live cells.

Note Added in Proof. After submission of this work, Mu¨ller et al. reported multiplex CARS microscopy using a similar laser system in J. Phys. Chem. B. 2002, 106, 3715. However, polarization-sensitive detection was not used to suppress the overwhelming nonresonant background.

Acknowledgment. This work was supported by a NIH grant (GM62536-01) and in part by Materials Research Science and Engineering Center at Harvard University. A.V. acknowledges support from the Deutsche Forschungsgemeinschaft.

## References and Notes

(1) Duncan, M. D.; Reintjes, J.; Manuccia, T. J. Opt. Lett. 1982, 7, 350 352.  
-(2) Zumbusch, A.; Holtom, G. R.; Xie, X. S. Phys. Re . Lett. 1999, 82, 4142 4145.  
-(3) Cheng, J. X.; Volkmer, A.; Book, L. D.; Xie, X. S. J. Phys. Chem. B 2001, 105, 1277 1280.  
-(4) Volkmer, A.; Cheng, J. X.; Xie, X. S. Phys. Re . Lett. 2001, 87, 0239011 0239014.  
-(5) Cheng, J. X.; Book, L. D.; Xie, X. S. Opt. Lett. 2001, 26, 1341 1343.  
(6) Potma, E. O.; Boeij, W. P. D.; Haastert, P. J. M. v.; Wiersma, D. A. Proc. Natl. Acad. Sci. U.S.A. 2001, 98, 1577 1582.  
-(7) Volkmer, A.; Book, L. D.; Xie, X. S. Appl. Phys. Lett. 2002, 80, 1505 1507.  
-(8) Cheng, J. X.; Volkmer, A.; Xie, X. S. J. Opt. Soc. Am. B 2002, 19, 1363 1375.  
-(9) Cheng, J. X.; Jia, Y. K.; Zheng, G.; Xie, X. S. Biophys. J. 2002, 83, 502 509.  
-(10) Potma, E. O.; Jones, D. J.; Cheng, J. X.; Xie, X. S.; Ye, J. Opt. Lett. 2002, 27, 1168 1170.  
-(11) Hashimoto, M.; Araki, T.; Kawata, S. Opt. Lett. 2000, 25, 1768 1770.  
(12) Shen, Y. R. The Principles of Nonlinear Optics; John Wiley and Sons Inc.: New York, 1984.  
(13) Levenson, M. D.; Kano, S. S. Introduction to Nonlinear Laser Spectroscopy; Academic Press: San Diego, 1988.  
(14) Ujj, L.; Volodin, B. L.; Popp, A.; Delaney, J. K.; Atkinson, G. H. Chem. Phys. 1994, 182, 291 311.  
-(15) Voroshilov, A.; Otto, C.; Greve, J. J. Chem. Phys. 1997, 106, 2589 2598.  
(16) Otto, C.; Voroshilov, A.; Kruglik, S. G.; Greve, J. J. Raman. Spectrosc. 2001, 32, 495 501.  
-(17) Bjorklund, G. C. IEEE J. Quantum Electron. 1975, QE-11, 287 296.  
(18) Oudar, J.-L.; Smith, R. W.; Shen, Y. R. Appl. Phys. Lett. 1979, 34, 758 760.  
-(19) Brakel, R.; Schneider, F. W. In Ad ances in Nonlinear Spectros-Vcopy; Clark, R. J. H., Hester, R. E., Eds.; John Wiley & Sons Ltd: New York, 1988; p 149.  
(20) Chikishev, A. Y.; Lucassen, G. W.; Koroteev, N. I.; Otto, C.; Greve, J. Biophys. J. 1992, 63, 976 985.  
-(21) Toleutaev, B. N.; Tahara, T.; Hamaguchi, H. Appl. Phys. B 1994, 59, 369 375.  
-(22) Igarashi, R.; Iida, F.; Hirose, C.; Fujiyama, T. Bull. Chem. Soc. Jpn. 1981, 54, 3691 3695.  
-(23) Levin, I. W. In Ad ances in Infrared and Raman Spectroscopy; VClark, R. J. H., Hester, R. E., Eds.; Wiley Heyden: New York, 1984; Vol. 11, pp 1 48.  
-(24) Gomez, J. S. In Modern Techniques in Raman Spectroscopy; Laserna, J. J., Ed.; John Wiley & Sons: New York, 1996; pp 309 342.  
-(25) Siegman, A. E. Lasers; University Science Books: Mill Valley, CA, 1986.  
(26) Kleinman, D. A. Phys. Re . 1962, 126, 1977 1979.  
V -(27) Maeda, S.; Kamisuki, T.; Adachi, Y. In Ad ances in Nonlinear VSpectroscopy; Clark, R. J. H., Hester, R. E., Eds.; John Wiley and Sons Ltd.: New York, 1988; p 253.