# Millimetre-deep micrometre-resolution vibrational imaging by shortwave infrared photothermal microscopy

Received: 15 October 2023

Accepted: 16 May 2024

Published online: 25 June 2024

![](images/ab449616e627a08fcd025927dac7367a06ae3e1210896e7276838c42736ab731.jpg)

Check for updates

Hongli Ni  1,5, Yuhao Yuan  1,5, Mingsheng Li1 , Yifan Zhu  2 , Xiaowei Ge  1 , Jiaze Yin1 , Chinmayee Prabhu Dessai  3 , Le Wang1 & Ji-Xin Cheng  1,2,3,4

Deep tissue chemical imaging has a vital role in biological and medical applications. Current approaches sufer from water absorption and tissue scattering, which limits imaging depth to hundreds of micrometres. The shortwave infrared spectral window allows deep tissue imaging but typically features unsatisfactory spatial resolution or low detection sensitivity. Here we present a shortwave infrared photothermal (SWIP) microscope for millimetre-deep vibrational imaging with micrometre lateral resolution. By pumping the overtone transition of carbon–hydrogen bonds and probing the subsequent photothermal lens with shortwave infrared light, SWIP can obtain chemical contrast from 1 μm polymer particles located at 800 μm depth in a highly scattering phantom. The amplitude of the SWIP signal is shown to be 63 times larger than that of the optically probed photoacoustic signal. We further demonstrate that SWIP can resolve intracellular lipids across an intact tumour spheroid and the layered structure in thick liver, skin, brain and breast tissues. SWIP microscopy flls a gap in vibrational imaging with subcellular resolution and millimetre-level penetration, which heralds broad potential for life science and clinical applications.

Probing cellular activities and functions in intact tissue is crucial for biomedical applications such as cancer pathology and drug discovery1 . Vibrational microscopy is a powerful tool for studying cellular functions by providing chemical contrast from nutrients, metabolites and other biomolecules2 . However, the imaging depth of current vibrational microscopy is not sufficient to map the chemical content in intact organoids or tissue without altering the natural microenvironment. Specifically, infrared spectroscopy-based approaches suffer from a strong water absorption, which restricts the penetration depth to tens of micrometres3 . Spontaneous or coherent Raman microscopy with visible or near-infrared excitation has large tissue scattering, limiting their imaging depth to around 100 µm (refs. 4,5). With detection of diffusively backscattered photons, spatially offset Raman spectroscopy6,7 and spontaneous Raman tomography8–10 can acquire signals beyond millimetres deep in tissue. However, these methods have a millimetre-level spatial resolution that is not sufficient to monitor cellular-level activity.

The shortwave infrared (SWIR) region (from 1,000 nm to 2,000 nm)11 opens a new window for deep tissue imaging with reduced scattering compared with the visible region and lower water absorption compared with the mid-infrared region12,13 (Fig. 1a). Importantly, the overtone transitions, which are high-order harmonics of the fundamental modes of molecular vibrations (Fig. 1b), reside in this window14, allowing deep vibrational imaging. Among various SWIR modalities, diffuse optical tomography can image beyond millimetres deep in tissue, yet at a millimetre-level spatial resolution15. Photoacoustic (PA) imaging achieves a higher spatial resolution by detecting acoustic waves with low tissue scattering16,17. SWIR-photoacoustic microscopy

1 Department of Electrical and Computer Engineering, Boston University, Boston, MA, USA. 2 Department of Chemistry, Boston University, Boston, MA, USA. 3 Department of Biomedical Engineering, Boston University, Boston, MA, USA. 4 Photonics Center, Boston University, Boston, MA, USA. 5 These authors contributed equally: Hongli Ni, Yuhao Yuan.  e-mail: jxcheng@bu.edu

a  
![](images/1726b431fe0cd39ca580d9ab1cd92cec003510684b5fd78e35c4853416b34c6c.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Absorption | Scattering | Combined |
| --------------- | ---------- | ---------- | -------- |
| 1000            | 0          | 0          | 0        |
| 1500            | 2000       | 500        | 300      |
| 2000            | 500        | 1000       | 400      |
| 2500            | 0          | 1500       | 200      |
</details>

d  
![](images/b55b533929917826160d5ef8f432c3daeb08c3e6434e57a3fcd70a5f43ac7101.jpg)

<details>
<summary>text_image</summary>

Dichroic mirror
Objective
Sample
Condenser
Filter
Detector
Amplifier
Probe
Excitation
Computer
Digitizer
</details>

b  
![](images/a78ebd8bb8eadcd39af3387f50ee3d6d38de0d5bebbab44b861bb49f2483f080.jpg)

<details>
<summary>text_image</summary>

Overtone
v = 3
v = 2
v = 1
v = 0
Fundamental
</details>

c  
![](images/d5ab72f43b074c3310b44ab8d6cd025e65cdf25ef7937946d6102fa925fbb974.jpg)

<details>
<summary>text_image</summary>

Excitation off
Absorber
Aperture Detector
Excitation on
Absorber
Aperture Detector
T↑
n↓
I↑
</details>

Fig. 1 | SWIP microscope principle and schematic. a, Wavelength-dependent attenuation length in brain tissue calculated with water absorption and brain tissue scattering coefficients12. b, Overtone absorption energy diagram. ν denotes the vibration energy levels. c, PT contrast mechanism. T, temperature; n, refractive index; I, light intensity. d, SWIP microscope schematic.

(SWIR-PAM) has allowed vibrational mapping of lipids in arterial tissues and Drosophila embryo13. In SWIR-PAM, the transducer is placed at a considerable distance away from the absorption site. Acoustic signal loss takes place during the propagation, which degrades the detection sensitivity and constrains the detected target sizes to tens of micrometres. In addition, acoustic coupling complicates the optical path design and is not applicable to samples that are sensitive to mechanical contact such as a patient wound18. Optically probed PAM has been developed for remote-sensing purposes18,19 and has been extended to the SWIR window20,21. However, the sensitivity of PA remote sensing is not sufficient for subcellular chemical imaging.

In this Article, we present a shortwave infrared photothermal (SWIP) microscope for subcellular-resolution and millimetre-deep tissue imaging. By optically sensing the refractive index change directly from the absorption site (Fig. 1c), SWIP prevents signal loss during propagation and eliminates the necessity of sample contact. Through a pump–probe scheme, SWIP achieves subcellular spatial resolution and millimetre-level imaging depth in highly scattering mediums, which allows imaging of single 1 µm polystyrene (PS) beads through an 800-µm-thick scattering phantom. Furthermore, the photothermal (PT) dynamics enables the detection of small objects over the surrounding medium background. With these advances, we demonstrate volumetric SWIP imaging of intracellular lipids in an intact tumour spheroid, thick animal tissue slices and human breast biopsy.

## Results

## An SWIP microscope

To fulfil the SWIP concept, we built a pump–probe microscope, as shown in Fig. 1d. A 1,725 nm pulsed laser serves as the excitation to target the first overtone absorption of carbon–hydrogen (C–H) vibration. A 1,310 nm continuous-wave laser is used as the probe. The excitation and probe beams are combined and focused into the sample to obtain the SWIP signal originating from the absorption-induced thermo-optic effect. The thermal-modulated refractive index forms a microlens and consequently alters the propagation of the probe laser, which modulates the light intensity collected through a small aperture inside the condenser (Fig. 1d).

## Optically detected PT versus PA signal

Under pulsed excitation, PT and PA conversions occur simultaneously. Studying the relative amplitudes between the coupled PT and PA signals is valuable in designing the detection scheme. We first performed a theoretical analysis of PT and PA contributions to the optically probed signal. Since both PT and PA signals can be written as a function of temperature rise, an amplitude ratio between optically probed PT and PA signal intensities could be calculated as (details in Supplementary Section 2)

$$
\frac {I _ {\mathrm{PT}}}{I _ {\mathrm{PA}}} = \left| \frac {\delta n _ {\mathrm{PT}}}{\delta n _ {\mathrm{PA}}} \right| = \frac {2 | \alpha | v _ {\mathrm{a}} ^ {3} \tau_ {\text { pulse }}}{\eta n _ {0} ^ {3} \Gamma C _ {V} r _ {\text { focus }}} \tag {1}
$$

Here α is the thermo-optic coefficient, $\nu _ { \mathrm { a } }$ is the speed of sound, $\tau _ { \mathrm { p u l s e } }$ is the pulse duration, η is the elasto-optic coefficient, $n _ { 0 }$ is the initial refractive index of the sample, Γ is the Grüneisen parameter, $C _ { V }$ is the constant volume heat capacity and $r _ { \mathrm { { f o c u s } } }$ is the radius of the probe focus. For olive oil, we find that $\frac { \bar { I _ { \mathrm { P T } } } } { I _ { \mathrm { P A } } } \approx 4 7$ (details in Supplementary Section 2).

The calculation indicates that the PT contribution is more than one order larger than that of PA. To validate this result, we measured PA and PT signals simultaneously using the SWIP microscope. Through fast digitization, PT and PA contributions can be differentiated by their temporal profiles (Fig. 2). Because the estimated acoustic relaxation time is shorter than the pulse duration, PA initial pressure rise should have the same duration as the excitation pulse, which is 10 ns. By con trast, the PT signal shows a long exponential decay as indicated by Newton’s law of cooling. When the two foci were tight and in good lateral overlapping (Fig. 2a), the PT signal overwhelmed the PA signal (Fig. 2b). A bipolar PA oscillation was observed with an amplitude 63 times smaller than that of PT (Fig. 2c).

To confirm whether the initial oscillation signal was from PA, we acquired three other signal traces under different focusing conditions. We recognize that PT is locally confined and PA propagates according to their diffusion speeds. Therefore, enlarging the probe focus size (Fig. 2d) or introducing lateral displacement between the two foci (Fig. 2g,j) should selectively probe the PA signal22.

a  
![](images/773eea5b45199c4014119189a651e6146d1665601956cebe1596e75082916928.jpg)

<details>
<summary>text_image</summary>

Probe
Excitation
</details>

d  
![](images/7c8e076979cb2887e12cd8057a9f73519127a5eea16995c35df9566ab6f00ac9.jpg)

<details>
<summary>text_image</summary>

Probe
Excitation
</details>

g

![](images/989352947456a3667107fd8f104c573b6b6a08748df581ce272e6d4a37eeccca.jpg)

<details>
<summary>text_image</summary>

Probe
Excitation
</details>

j

![](images/5ffa5a9b4abeb6d7385cca0bede813d4e9a16158d411d6b123345995f5c51d10.jpg)

<details>
<summary>text_image</summary>

Probe
Excitation
</details>

b  
![](images/4c4f813d58545bb65fef1f1445edeadd13474e04225c1a4fd4519bb29a3e51ee.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Signal (V) |
| --------- | ---------- |
| 0         | 1.7        |
| 2         | 1.5        |
| 4         | 1.2        |
| 6         | 0.9        |
| 8         | 0.7        |
| 10        | 0.6        |
</details>

e  
![](images/bbaa1d67991122bd6fc8b4d284d68955451022f147b1fa88e5803e764977fb63.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Signal (V) |
| --------- | ---------- |
| 0         | 0.0        |
| 1         | 0.20       |
| 2         | 0.20       |
| 4         | 0.18       |
| 6         | 0.17       |
| 8         | 0.16       |
| 10        | 0.15       |
</details>

h  
![](images/513de5889991cf319a6ae43d497f6b1bee276154e8e9cd4826b15fad6c1a796c.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Signal (V) |
| --------- | ---------- |
| 0         | 0.0        |
| 1         | 0.11       |
| 2         | 0.10       |
| 4         | 0.08       |
| 6         | 0.07       |
| 8         | 0.06       |
| 10        | 0.05       |
</details>

k  
![](images/75d840c409863bb785289008ebb23a1d493948fd9bab80f9f462f24242e35088.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Signal (V) |
| --------- | ---------- |
| 0         | 0          |
| 2         | ~0         |
| 4         | ~-0.01     |
| 6         | ~-0.02     |
| 8         | ~-0.03     |
| 10        | ~-0.04     |
</details>

c  
![](images/e95b0362d023200e557e5f27f3306d6f7c656643809e6ba8c04836695ec4d557.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Signal (V) |
| --------- | ---------- |
| 0.5       | 1.70       |
| 0.6       | 1.72       |
| 0.8       | 1.68       |
| 1.0       | 1.64       |
| 1.2       | 1.62       |
</details>

f  
![](images/4b73eb9404939fc2e8db8075b142bf55c5853daa1c48925f4db59d18f8c89c44.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Signal (V) |
| --------- | ---------- |
| 0.5       | 0.20       |
| 1.0       | 0.195      |
| 1.5       | 0.192      |
</details>

i  
![](images/0ec180cffa44f219d440c14f1c28f64966b6b317609a321bf46b94b7d4366a6b.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Signal (V) |
| --------- | ---------- |
| 0.5       | 0.11       |
| 1.5       | 0.09       |
</details>

l  
![](images/f4b40ce14e0dc11192a27afa8497a9bc8737b31b7d52248377dc0431590eb6d2.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Signal (V) |
| --------- | ---------- |
| 0.5       | 0.01       |
| 1.5       | ~0.00      |
</details>

Fig. 2 | Comparison of optically detected PT and PA signals. a, Normal SWIP focusing configuration where probe and excitation foci have a similar size and good lateral overlapping. b, Signal trace under the configuration in a. c, Zoom-in of b. d, Focusing configuration where the probe focus is enlarged by reducing the probe beam diameter before the objective, which leads to a reduced effective NA. e, Signal trace under the configuration in d. f, Zoom-in  
of e. g, Focusing configuration where the probe focus has a small lateral shift relative to the excitation focus. h, Signal trace under the configuration in g. i, Zoom-in of h. j, Focusing configuration where the probe focus has a large lateral shift to the excitation focus. k, Signal trace under the configuration in j. l, Zoom-in of k. Sample, olive oil. SWIR excitation power on the sample, 4.2 mW.

As expected, under the modified schemes, the relative amplitude of PA became larger in the detected signal (Fig. 2e,h,k), which could be clearly observed in the zoom-in views (Fig. 2f,i,l). In an extreme case, when the two foci had little overlap (Fig. 2j), the PT contribution in the probed signal became negligible and a typical acoustic bipolar oscillation was observed (Fig. 2k,l). The width of the strongest PA pulse in Fig. 2f,i,l is around 10 ns, consistent with the initial pressure rise theory. In Fig. 2c,f, the oscillations following the strongest PA pulse represent the low-frequency PA components, whereas the rip ples in Fig. 2i,l are a result of detector noise (details in Supplementary Section 3). Together, these results confirm that the bipolar signal detected in Fig. 2c is from PA. A ball-lens model that interprets the SWIP contrast under various focusing conditions can be found in Supplementary Section 1.

We noticed a slight mismatch between the theoretical calculation and the experimental result, possibly owing to the deviation of the elasto-optic coefficient used in our calculation from the real value in our experimental system, or the limited bandwidth of our photodetector (70 MHz). Such a mismatch does not influence the conclusion that the PT signal has more than one order larger amplitude than the PA signal in the well-overlapped tight-focusing condition.

To compare the detection sensitivity, we measured SWIP and optically detected PA signal dependence on dimethyl sulfoxide (DMSO) concentration in D O (Supplementary Fig. 3). The limits of detection (LODs) (see Methods for definition) were 112 mM for SWIP and 7.78 M for optically detected PA. Thus, the LOD for SWIP is 69 times better than that for optically detected PA, consistent with the measured amplitude difference on the pure oil sample. Together, the SWIP amplitude is more than one order larger than the optically probed PA in our configuration theoretically and experimentally.

## SWIP imaging characteristics

Next, we characterized the performance of our SWIP microscope using standard samples. Figure 3a,b shows the XY and YZ sections of volumetric SWIP images of 500 nm PS beads. The signal-to-noise ratio (SNR) of the XY image of a single bead was 25, suggesting the high sensitivity of SWIP. Figure 3c,d shows the lateral and axial profiles of a single 500 nm PS bead, where the lateral and axial full width at half maximum values were 0.92 µm and 3.5 µm, respectively. After deconvolution with the bead’s profile, the calculated system’s lateral and axial resolutions were 0.77 µm and 3.5 µm, respectively. Such a resolution is sufficient to resolve the subcellular features.

To confirm the chemical selectivity of SWIP, we acquired the SWI spectra of standard samples (Fig. 3e). The SWIP spectra match well with the SWIR absorption spectra reported in the literature11,23. The peak registration is illustrated in Supplementary Section 5. Figure 3f,g shows a linear dependence of the SWIP signal on both excitation power and molecular concentration, consistent with the ball-lens model of the SWIP contrast (Supplementary Section 1). On the basis of the concentration curve (Fig. 3g), the LOD of DMSO for SWIP was measured to be 112 mM. Under the same average power, the LOD of DMSO using a hyperspectral stimulated Raman scattering (SRS) microscope in our lab was 152 mM (Supplementary Fig. 6). Collectively, these data show good sensitivity and linearity of SWIP microscopy.

The deep-penetration, high-resolution imaging capability of SWIP was characterized with scattering phantoms. A tissue-mimicking

a  
![](images/e2b86fb4c70104fe024221680ebb45c5ce87103ccfc39cf3d59b0a5514fcbb46.jpg)

b  
![](images/94deff1717690c1fbe8fab0d810df24c5caf85249409bbd1370494232d2c78ad.jpg)

<details>
<summary>natural_image</summary>

Grayscale abstract image with a red dashed line and a white corner marker (no text or symbols)
</details>

c  
![](images/e018ff4405f039570a393108bd773a9d2b9b3f8f0674d27d3ba4dd442475ce73.jpg)

<details>
<summary>line chart</summary>

| X (μm) | Signal (×10⁻³ V) |
| ------ | ---------------- |
| -2     | 0                |
| -1     | 0.5              |
| 0      | 4.5              |
| 1      | 0.5              |
| 2      | 0                |
</details>

d  
![](images/1224ec926d04d3c3a0e6fbcc5312cc76daa42f80c2282d7c4ed4ff4cd8685ed0.jpg)

<details>
<summary>line chart</summary>

| Z (μm) | Signal (×10⁻³) (V) |
| ------ | ------------------ |
| -5.0   | 0.0                |
| -2.5   | 1.5                |
| 0.0    | 4.0                |
| 2.5    | 1.5                |
| 5.0    | 0.0                |
</details>

e  
![](images/a7d1aababc5d443c77e8c5a8fcf760cb0ac6b81c0d34a9624c8f42f688680a89.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | DMSO Signal (V) | Protein Signal (V) |
| --------------- | --------------- | ------------------ |
| 1600            | ~0.1            | ~0.13              |
| 1650            | ~0.2            | ~0.12              |
| 1700            | ~1.0            | ~0.18              |
| 1750            | ~0.8            | ~0.16              |
| 1800            | ~0.3            | ~0.10              |
| 1850            | ~0.1            | ~0.05              |
</details>

![](images/bd30c8ce751b01705f0dc008a7fca7641318de16e73d75ac468e1ee062f2334a.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Lipid Signal (V) | DNA Signal (V) |
| --------------- | ---------------- | -------------- |
| 1600            | ~0.0             | ~0.06          |
| 1650            | ~0.2             | ~0.07          |
| 1700            | ~1.8             | ~0.08          |
| 1750            | ~1.0             | ~0.07          |
| 1800            | ~0.4             | ~0.05          |
| 1850            | ~0.1             | ~0.04          |
</details>

f  
![](images/8c28c353dead288de00b245364cc2ad098afa88849b5523783b4a9a709a5b01c.jpg)

<details>
<summary>scatterplot</summary>

| Excitation power (mW) | Signal (V) |
| --------------------- | ---------- |
| 0                     | 0          |
| 1                     | 0.3        |
| 2                     | 0.7        |
| 3                     | 1.1        |
| 4                     | 1.5        |
| 5                     | 1.8        |
</details>

g  
![](images/551d88c7919ba3cd87ce5ad018d3310332799ce09382296a022677893a44bf04.jpg)

<details>
<summary>line chart</summary>

| DMSO concentration (mol l⁻¹) | Signal (V) |
| ---------------------------- | ---------- |
| 0.0                          | 0.005      |
| 0.3                          | 0.010      |
| 0.9                          | 0.020      |
| 1.8                          | 0.035      |
</details>

![](images/def83eb9cb8b06c611399ab6bec6dae62cf2f5232a38e2131e2b3a86759021b0.jpg)

<details>
<summary>text_image</summary>

OBJ
TMP
CLP
Beads
COND
Filter
PD
800 µm
</details>

i  
![](images/756f90ecd6f37d3369076175c609e00f870c876847487aa0be17d4ec3c82b8bf.jpg)

<details>
<summary>text_image</summary>

Water
SWIP
0	0.12
SNR = 297
</details>

![](images/96ecc34fd45447665a770f762869aa91c856ada4ff31c78459e8241757be2c87.jpg)

<details>
<summary>text_image</summary>

1% intralipid
0	0.06
SNR = 259
</details>

![](images/d7fe3e987823af8b445715a30983f71f82637281841060d68700a425c726d5b1.jpg)

<details>
<summary>text_image</summary>

5% intralipid
0	0.008
SNR = 95
</details>

![](images/bf1280f21a7357cc336a35de6cb93e4a1fd159090cf945b7edaacc44a8032281.jpg)

<details>
<summary>text_image</summary>

10% intralipid
0	0.001
SNR = 6
</details>

k

![](images/3a625dc12a2aed94ce77df47e8ac3eebb3ca1a75800d2765afdcb70d770a44ee.jpg)

<details>
<summary>line chart</summary>

| X (μm) | Water | 1% intralipid | 5% intralipid | 10% intralipid |
| ------ | ----- | ------------- | ------------- | -------------- |
| -3     | 0.0   | 0.0           | 0.0           | 0.2            |
| -2     | 0.0   | 0.0           | 0.0           | 0.2            |
| -1     | 0.0   | 0.0           | 0.0           | 0.4            |
| 0      | 1.0   | 1.0           | 1.0           | 1.0            |
| 1      | 0.0   | 0.0           | 0.0           | 0.4            |
| 2      | 0.0   | 0.0           | 0.0           | 0.2            |
</details>

j  
![](images/816eca27bbe095d9aaedac7d0df15a1ccf35e5cec8af173583fd1fd2aaab30be.jpg)

<details>
<summary>text_image</summary>

Water
SRS
</details>

![](images/c973298bce2b0b7e24832e2604e42d4db4ff20a099592b6a467957fec3db5d40.jpg)

<details>
<summary>text_image</summary>

1% intralipid
</details>

![](images/982dbc3088802cc23f6481a137555c5d45d61f17f4e64f8fb30f566a3c7aa67f.jpg)

<details>
<summary>text_image</summary>

5% intralipid
</details>

![](images/563e9698b24a63b8852338e5ff13223ef4b1e3e270b9101ee7520e47bbd61c97.jpg)

<details>
<summary>text_image</summary>

10% intralipid
</details>

l

![](images/19294d0b0446bb99a0b1af3fcfe25f2fd397f85c82fc8701ea62ab994f618d68.jpg)

<details>
<summary>line chart</summary>

| X (μm) | Water | 1% intralipid |
| ------ | ----- | ------------- |
| -3     | 0.0   | 0.4           |
| -2     | 0.0   | 0.3           |
| -1     | 0.1   | 0.2           |
| 0      | 1.0   | 1.0           |
| 1      | 0.1   | 0.3           |
| 2      | 0.0   | 0.3           |
</details>

Fig. 3 | SWIP microscope performance. a,b, XY (a) and YZ (b) sections of the volumetric SWIP image of single 500 nm PS beads. Excitation power on the sample, 20 mW. Scale bars, 1 μm. c,d, Single 500 nm PS bead’s lateral (c) and axial (d) profiles corresponding to dashed lines in a and b. e, SWIP spectra of DMSO, lipid, protein and DNA. f, SWIP signal dependence on excitation power. Sample, pure DMSO. g, SWIP signal dependence on the concentration of DMSO in D O. h, Scattering phantom imaging schematic. OBJ, objective lens; TMP, tissue-mimicking phantom; CLP, coverslip; COND, condenser; PD, photodiode.  
i, SWIP imaging results of 1.0 μm PS beads through water or scattering medium. Greyscale bars represent SWIP signal intensity in voltage. Laser power on the sample, 1,725 nm, 20 mW; 1,310 nm, 10.3 mW. Scale bar, 10 μm. j, SRS imaging results of 1.0 μm PS beads through water or scattering medium. Laser power on the sample, 798 nm, 10 mW; 1,040 nm, 60 mW (water group); 798 nm, 50 mW; 1,040 nm, 100 mW (intralipid groups). Scale bar, 10 μm. k, Lateral profile of a single 1.0 μm PS bead in i as indicated by the red dashed lines. l, Lateral profile of a single 1.0 μm PS bead in j as indicated by the red dashed lines.

intralipid aqueous solution was placed between the objective and 1.0 μm PS beads (Fig. 3h). Note that 1% intralipid has a similar scattering coefficient to the human skin epidermis24. Figure 3i shows the SWIP imaging results through water and 1%, 5% and 10% intralipids. SWIP successfully resolved single 1.0 μm PS beads even under 10% intralipids. In comparison, near-infrared SRS imaging was performed under the same conditions (Fig. 3j). In pure water conditions, SRS showed a higher resolution than SWIP owing to shorter excitation wavelengths. However, the image quality of SRS quickly degraded as the intralipid concentration increased. No beads could be seen by SRS under 5% and 10% intralipid solutions. To investigate the resolution degradation of SWIP and SRS through a scattering medium, we plotted the lateral profiles of a single bead and observed no notable broadening through a scattering phantom for SWIP (Fig. 3k) but a slight broadening for SRS (Fig. 3l), indicating that SWIP can maintain good spatial resolution through a highly scattering medium, which is beyond reach of a typical near-infrared SRS microscope.

## SWIP imaging of lipids in an intact tumour spheroid

A tumour-derived spheroid is an in vitro cancer model that better recapitulates tumour physiology than two-dimensional cell culture25. As cancer development is closely related to the altered lipid metabolism26, imaging intracellular lipids helps understand cancer progression and test drug effectiveness. However, imaging cellular components inside spheroids is challenging as the densely packed cells strongly scatter light. Sectioning27 and tissue clearing28,29 have been applied to circumvent the strong scattering. Yet, these methods alter the metabolic state of spheroids and cannot be used for a live sample study.

a  
![](images/3b8ef9f8ca4e0772885263a7fb0e1ff1adfc282f6fd58492a0347d3ffda8f80f.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing cellular structures with red and blue arrows indicating specific regions (no text or symbols present)
</details>

b  
![](images/8f673a92bb725244a2e8a089efa56e60fee8ac7d02b8261800c756aa975f06ff.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Raw data | Fit result | Exp comp 1 | Exp comp 2 |
| --------- | -------- | ---------- | ---------- | ---------- |
| 0         | 0.10     | 0.10       | 0.08       | 0.04       |
| 1         | 0.07     | 0.07       | 0.06       | 0.02       |
| 2         | 0.05     | 0.05       | 0.05       | 0.01       |
| 3         | 0.04     | 0.04       | 0.04       | 0.01       |
| 4         | 0.03     | 0.03       | 0.03       | 0.01       |
| 5         | 0.02     | 0.02       | 0.02       | 0.01       |
</details>

c  
![](images/54331d4ca1a71312f5a522a89eaa880d8555ba84eafff994af63930074af60b1.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Raw data | Fit result | Exp comp 1 | Exp comp 2 |
| --------- | -------- | ---------- | ---------- | ---------- |
| 0         | 0.04     | 0.04       | 0.02       | 0.02       |
| 2         | 0.03     | 0.03       | 0.02       | 0.01       |
| 4         | 0.02     | 0.02       | 0.02       | 0.01       |
| 6         | 0.02     | 0.02       | 0.02       | 0.01       |
</details>

d  
![](images/f65190fa11d0bf7f8378c96b402a358eaf5ea70c08fc6725cda691d079ae27e9.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing scattered red and blue fluorescent spots against a black background, with a scale bar in the corner (no text or symbols)
</details>

![](images/ee9612fdbefcb28b436589a80ffc1de7b6de34864df9c6abe24a76152b7b5d75.jpg)

<details>
<summary>text_image</summary>

Z = 20 µm
Z = 90 µm
Z = 180 µm
Raw
Background removed
f
0 µm
200 µm
200 µm
200 µm
</details>

Fig. 4 | SWIP imaging of cancer cells and spheroids. a, Raw SWIP image of monolayer OVCAR-5-cisR cells. Red arrow, lipid droplets; blue arrow, water area. b, Single-pixel SWIP signal trace at the red arrow-pointed lipid area. The fitting $\mathrm { r e s u l t i s } f ( t ) = 0 . 0 7 1 \mathrm { e } ^ { - 0 . 1 2 \mathrm { t } } + 0 . 0 3 1 \mathrm { e } ^ { - 1 . 9 6 ( \mathrm { e } ^ { - 1 . 9 6 ( \mathrm { e } ^ { - 1 . 7 6 ( \mathrm { e } ^ { - 1 . 7 6 ( \mathrm { e } ^ { - 1 . 7 6 ) } } ) } ) } - 0 . 0 7 1 \mathrm { e } ^ { - 1 . 9 6 ( \mathrm { e } ^ { - 1 . 7 6 ( \mathrm { e } ^ { - 1 . 7 6 ) } } ) } ) }$ t. Exp comp, fitted exponential component; t, time. c, Single-pixel SWIP signal trace at the blue arrow-pointed background area. The fitting result i $\mathrm { 3 } f ( t ) = 0 . 0 2 4 \mathrm { e } ^ { - 0 . 0 4 5 \mathrm { t } } + 0 . 0 2 0 \mathrm { e } ^ { - 0 . 5 0 \mathrm { t } }$ . d, Background rejection  
result of a using the decay characteristic. Red arrow, lipid droplets; blue arrow, water area. e, SWIP imaging of an OVCAR-5-cisR spheroid. The blue arrows point to individual cells. The white arrow points to a hollow structure in the spheroid. f, Three-dimensional rendering of volumetric SWIP imaging of the OVCAR-5- cisR spheroid after background rejection. Laser power on the sample for all subpanels, 1,725 nm, 20 mW; 1,310 nm, 8.5 mW. All scale bars, 20 μm.

Deep-penetrating multiphoton or light-sheet fluorescence microscopy can image live spheroids30,31. However, fluorescent labelling is perturbative, especially for small lipid molecules32.

SWIP provides an opportunity to overcome the above-mentioned challenges. We first validated the SWIP contrast on single-layer cells. SWIP well mapped intracellular lipids and revealed good cell morphology (Fig. 4a). Utilizing the different thermal decay coefficients of lipids (Fig. 4b) and bulk water (Fig. 4c), the water background in Fig. 4a was removed (blue arrow, Fig. 4d) and the intracellular lipid contrast was enhanced (red arrow, Fig. 4d). The logic and workflow of the background suppression are described in Methods.

Figure 4e shows the SWIP images of an intact tumour spheroid with a diameter of around 200 µm. In raw SWIP images, the intracellular lipids were successfully identified at the top, equatorial and bottom planes. After background suppression, the intracellular lipids showed up cleanly. Individual cells can be identified by circles of intracellular lipids (blue arrow in Fig. 4e). Hollow structures in the centre of the spheroid can be observed (white arrow in Fig. 4e). Figure 4f shows a background-removed three-dimensional volumetric SWIP image of the spheroid where an enriched accumulation and a relatively uniform distribution of lipid were seen.

## SWIP imaging of lipids in biological tissues

Lipids have an important role in biological tissues, including energy storage, signalling and transport of fat-soluble nutrients33. Imaging lipid content and its distribution inside a tissue enables a broad range of applications34. Because fluorescent labelling is perturbative for lipid molecules, vibrational imaging is widely adopted for lipid studies . As mentioned, current vibrational imaging modalities do not allow high-resolution lipid imaging in deep tissue. Tissue sectioning is generally applied for high-resolution layer-by-layer imaging, but the sectioning process usually introduces morphological artefacts and causes lipid loss35.

Here we explored SWIP imaging of lipids in various types of tissue. Figure 5a shows SWIP images of a fresh swine liver slice. The lipid and liver morphology revealed by SWIP was consistent with previously reported SRS results36. Lipid droplets as small as 1.0 μm in diameter can be distinguished even at 300 µm deep inside the fresh liver with rich blood content, which cannot be achieved via existing modalities. Figure 5b shows SWIP images of a mouse ear. Characteristic layered structures were observed, including hair at Z = 0 µm, sebaceous gland at Z = 52 µm and subcutaneous fat layer or cartilage at Z = 156 µm. SWIP can also image through a 1.0-mm-thick brain slice and well capture the myelin fibrous structures (Fig. 5c), confirmed by benchmarking with SRS on the same mouse brain slice (Supplementary Fig. 10). Images in Fig. 5b,c have a slightly lower resolution because of the use of a different objective with a longer working distance and a lower effective numerical aperture (NA) (Methods and Supplementary Fig. 11). Figure 5d shows SWIP images of fat cells at different layers across a 600-µm-thick healthy breast biopsy.

Finally, towards in vivo deep tissue imaging, we demonstrated an epi-detected SWIP system (Supplementary Fig. 12). We harnessed an amplified photodiode with higher sensitivity to detect the weak backscattered probe laser. Figure 5e shows the epi-detected SWIP images of a mouse ear with sebaceous gland at Z = 60 μm and subcutaneous fat layer or cartilage at Z = 120 µm, well matched with the forward results (Fig. 5b). Figure 5f shows the epi-detected SWIP images of an intact mouse brain. The SWIP signal became stronger at Z = 500 μm compared with Z = 300 μm as the imaging plane moving from the cell-rich grey matter to the myelin-rich white matter. Together, these results show that in vivo SWIP imaging could be potentially achieved.

![](images/2b9e3c86dd812ff89bf37ccfddd47e5d2553d35a8bc9a9f010e159c69658ad01.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing red fluorescence with scattered yellow fluorescent spots, scale bar indicates 50 μm (no text or symbols present)
</details>

Z = 300 µm  
![](images/3802694bf2b54907c9c4dfc0ad17dd2a1dc97b31128c06c9b9feb3ebad2567f0.jpg)

<details>
<summary>natural_image</summary>

Abstract red textured pattern with no visible text or symbols
</details>

![](images/0523caf3ca624f45cf4b4a1248816176c9eebc87b67f8acde092a366c1bd655b.jpg)

<details>
<summary>natural_image</summary>

3D rendered cube with red speckled texture and a 500 μm scale indicator (no text or symbols on the cube itself)
</details>

![](images/e7ffe071ddfd019d85c2f5b1338fa0957d2f28f3e9fcd25a1db3d0877e0e3a0e.jpg)

![](images/8235991d526bd7146d54a45f65c3e171b8adfa4ec7fb80e364992c1900d1c902.jpg)

![](images/101d1aaf0ab68e89b7b664987ba269bf94d30b81f1af5e329588faead88590cc.jpg)

![](images/1a768d38c3c08047cfca3c71e9fc137e533a63e6137b19b115e539ef5a6c969e.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular or microbial structures under 0 μm scale (no text or symbols)
</details>

Z = 500 µm

e  
![](images/56129835665ecdb34f14bad27a9f26d2f83ff3d3ea316e6067248899a87288b1.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescently labeled cellular structures at 60 μm scale (no text or symbols present)
</details>

![](images/4877f836767fece65ba1150a901d06778a19f44264c3d62e0e37608539cc4006.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a textured surface with red-orange fluorescence, labeled 'Z = 120 μm' on the left (no other text or symbols)
</details>

c  
![](images/4881d8c6985dce59d77b1f533dc19c198b8cbc5da30489100a9475872b4a2e19.jpg)

<details>
<summary>natural_image</summary>

3D microscopic image of a layered material structure with green fluorescent regions, labeled with scale bar (1,040 μm) and orientation marker (0), no readable text or symbols beyond measurement annotations.
</details>

Z = 160 µm  
![](images/f8f1a0007b20a3540394fcdee51e2aa3c3bf431cac558149d25d69b43e4b6e70.jpg)

<details>
<summary>natural_image</summary>

Abstract pattern with green and blue diagonal bands, no text or symbols present
</details>

Z = 1,040 µm  
![](images/ada2a7cf36605bec5e622963063e5975b187d83861f3a1082513ba7f301e9a23.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing green fluorescent structures against a blue background, with a scale bar in the corner (no text or symbols)
</details>

![](images/aba104c993bc35ce1070eb60091e0eded4bd2d5e99b69187b8505d3afd34a2ac.jpg)

<details>
<summary>natural_image</summary>

Close-up of a textured yellow surface with a circular dark region (no text or symbols)
</details>

![](images/d662f7f1c5fda760687f0639e60c45328bce82bcb38f8875970fb6a298765ae5.jpg)

<details>
<summary>natural_image</summary>

3D rendered cube with textured surface and scale bar (600 μm), no readable text or symbols
</details>

![](images/b4ceb929d521e9fce0a78921ff241b7d00a710f88699302601280387b3aa7a6d.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a textured blue-green pattern with a scale bar labeled 'Z = 300 μm' (no other text or symbols)
</details>

![](images/69b36cf253519fa4d398c179d68663bcd9d28b8bf0376b273352e6ee1bf85e8e.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing green fluorescent particles on a blue background, with scale bar indicating 500 μm (no text or symbols present)
</details>

Fig. 5 | SWIP imaging of lipids in biological tissues. a, SWIP imaging of a fresh swine liver slice. b, SWIP imaging of a mouse ear. c, SWIP imaging of a mouse brain slice. d, SWIP imaging of a breast biopsy from a healthy human. e, Epi-SWIP imaging of a mouse ear at 60 µm and 120 µm depth. f, Epi-SWIP imaging of a  
mouse brain at 300 µm and 500 µm depth. Laser power on the sample, 1,725 nm, 20 mW; 1,310 nm, 50 mW (a–d); 1,725 nm, 20 mW; 1,310 nm, 70 mW (e,f). All scale bars, 20 μm.

## Discussion

A comparison of SWIP with existing vibrational imaging modalities in the depth-resolution space is illustrated in Fig. 6. These techniques can be clustered into three groups. The first group (bottom left) has subcellular resolution and sensitivity but limited imaging depth up to 100 μm. The second group (top right) has deep penetration depth but relatively poor spatial resolution at best hundreds of micrometres. Although SWIR-PAM can achieve a higher spatial resolution with a tighter optical focus, the large signal loss leads to a low detection sensitivity (Supplementary Fig. 5) and prevents it from probing small intracellular components. Clearly, there exists a gap between two groups for deep tissue vibrational imaging at subcellular resolution. As demonstrated in this work, SWIP successfully fills this gap. The millimetre-deep, micrometre-resolution, high-sensitivity vibrational imaging capability provided by SWIP opens exciting opportunities for many applications, including a live organoid study, slice-free tissue pathology, dynamic embryo imaging and so on.

As nonlinear optical microscopy, both SWIP and SRS signals are largely contributed by ballistic photons. To interpret the distinct imaging performance of SWIP and SRS shown in Fig. 3, we calculated the amounts of ballistic photons transmitted through a scattering medium. As shown in Supplementary Table 1, through 800 μm of 10% intralipid, 1.9% and 0.11% photons at 1,725 nm and 1,310 nm remain ballistic, whereas the amounts of ballistic photons at 798 nm and 1,040 nm are negligible. Thus, the deep imaging capability of SWIP largely benefits from the longer wavelengths.

It is noteworthy that the SWIP signal intensity is sensitive to the focusing condition. As in Fig. 2, the best configuration for PT detection is when the two foci have a similar size and in good lateral overlapping. The PA signal can be selectively detected if the probe volume is larger than the excitation volume, consistent with the PA remote-sensing study18. Compared with PT, PA imaging has its own merits. The PA signal is closely related to the mechanical property that is valuable for many applications37. Furthermore, the high-frequency PA can circumvent low-frequency noises. Our data and theory relating the signal level to the focusing condition can serve as a guide for better utilizing the strengths of PT and PA.

![](images/74974b61e940f1aa3514edb05ac640dfb22cd4886f52dd6f60d842eeac3bcc8c.jpg)

<details>
<summary>scatterplot</summary>

| Material   | Resolution (μm) | Penetration depth (μm) |
| ---------- | --------------- | ---------------------- |
| SWIR-PAM   | ~100            | ~5000                  |
| SORS       | ~200            | ~3000                  |
| SWIR DOI    | ~5000           | ~10000                 |
| SWIP       | ~1              | ~1000                  |
| CRS        | ~1              | ~100                   |
| CRM        | ~1              | ~100                   |
| MIP        | ~1              | ~50                    |
| FTIR       | ~1              | ~50                    |
</details>

Fig. 6 | Penetration depth versus spatial resolution of vibrational imaging modalities. The penetration-depth and spatial-resolution data are from 3,4,6,15,16,39. Group 1 (bottom left): CRS, coherent Raman scattering; MIP, mid-infrared photothermal; CRM, confocal Raman microscopy; FTIR, Fourier transform infrared spectroscopy. Group 2 (top right): SWIR-PAM; SWIR DOI, shortwave infrared diffusive optical imaging; SORS, spatial-offset Raman spectroscopy. Group 3: SWIP.

The reported SWIP microscope can be improved in several aspects. By far, our single-colour SWIP imaging using the first overtone absorption at 1,725 nm mainly targets the C–H bond that is enriched in lipid content. With a wavelength-tunable excitation laser, hyperspectral SWIP imaging and subsequent decomposition can differentiate multiple molecular species such as proteins, fatty acids, cholesterol and carbohydrates11,14. We noticed that the SWIP LOD of 112 mM DMSO is relatively large compared with the molecular concentration inside a cell. Fortunately, many biomolecules such as lipids are locally concentrated, which ensures their detectability with SWIP. Furthermore, some biomolecules have multiple targeted bonds. As shown in Supplementary Table 2, the C–H bond concentrations of cellular protein and lipid are much higher than the SWIP LOD for the C–H bond. Thus, SWIP can be applied to study a variety of locally enriched biomolecules, including lipid, cellular protein and collagen.

Second, the acquisition time of the current SWIP microscope is around 3 minutes per frame, limited by the 2 kHz excitation laser repetition rate. Combining a higher-repetition-rate excitation laser with galvo scanning, the imaging speed of SWIP can be improved (details in Supplementary Section 6). Third, SWIP has shown good performance in imaging through a homogeneous scattering phantom but encounters image degradation at hundreds-of-micrometres depth in the tissue. We attribute such degradation to tissue-induced aberration that inevitably distorts the laser focus. By implementing adaptive optics for aberration correction38, SWIP can reach even deeper. Lastly, we envision that SWIP microscopy can be upgraded into SWIP-optical coherence tomography (SWIP-OCT) for high-speed volumetric vibrational imaging of organoids and tissues.

## Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41566-024-01463-6.

## References

1. Kim, J., Koo, B. K. & Knoblich, J. A. Human organoids: model systems for human biology and medicine. Nat. Rev. Mol. Cell Biol. 21, 571–584 (2020).  
2. Cheng, J. X. & Xie, X. S. Vibrational spectroscopic imaging of living systems: an emerging platform for biology and medicine. Science 350, aaa8870 (2015).  
3. Zhang, D. et al. Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2, e1600521 (2016).  
4. Hill, A. H., Manifold, B. & Fu, D. Tissue imaging depth limit of stimulated Raman scattering microscopy. Biomed. Opt. Express 11, 762–774 (2020).  
5. Esposito, R. et al. Depth profiles in confocal optical microscopy: a simulation approach based on the second Rayleigh– Sommerfeld difraction integral. Opt. Express 24, 12565–12576 (2016).  
6. Mosca, S. et al. Spatially ofset Raman spectroscopy—how deep? Anal. Chem. 93, 6755–6762 (2021).  
7. Mosca, S., Conti, C., Stone, N. & Matousek, P. Spatially ofset Raman spectroscopy. Nat. Rev. Methods Primers 1, 21 (2021).  
8. Schulmerich, M. V. et al. Noninvasive Raman tomographic imaging of canine bone tissue. J. Biomed. Opt. 13, 020506 (2008).  
9. Demers, J.-L. H., Davis, S. C., Pogue, B. W. & Morris, M. D. Multichannel difuse optical Raman tomography for bone characterization in vivo: a phantom study. Biomed. Opt. Express 3, 2299–2305 (2012).  
10. Demers, J. L., Esmonde-White, F. W., Esmonde-White, K. A., Morris, M. D. & Pogue, B. W. Next-generation Raman tomography instrument for non-invasive in vivo bone imaging. Biomed. Opt. Express 6, 793–806 (2015).  
11. Wilson, R. H., Nadeau, K. P., Jaworski, F. B., Tromberg, B. J. & Durkin, A. J. Review of short-wave infrared spectroscopy and imaging methods for biological tissue characterization. J. Biomed. Opt. 20, 030901 (2015).  
12. Horton, N. G. et al. In vivo three-photon microscopy of subcortical structures within an intact mouse brain. Nat. Photon. 7, 205–209 (2013).  
13. Wang, H. W. et al. Label-free bond-selective imaging by listening to vibrationally excited molecules. Phys. Rev. Lett. 106, 238106 (2011).  
14. Wang, P., Rajian, J. R. & Cheng, J. X. Spectroscopic imaging of deep tissue through photoacoustic detection of molecular vibration. J. Phys. Chem. Lett. 4, 2177–2185 (2013).  
15. Zhao, Y. et al. Shortwave-infrared meso-patterned imaging enables label-free mapping of tissue water and lipid content. Nat. Commun. 11, 5355 (2020).  
16. Wang, L. V. & Yao, J. A practical guide to photoacoustic tomography in the life sciences. Nat. Methods 13, 627–638 (2016).  
17. Wang, L. V. Photoacoustic Imaging and Spectroscopy (CRC Press, 2017).  
18. Hajireza, P., Shi, W., Bell, K., Paproski, R. J. & Zemp, R. J. Noninterferometric photoacoustic remote sensing microscopy. Light Sci. Appl. 6, e16278 (2017).  
19. Reza, P. H., Bell, K., Shi, W., Shapiro, J. & Zemp, R. J. Deep noncontact photoacoustic initial pressure imaging. Optica 5, 814–820 (2018).  
20. Bell, K., Mukhangaliyeva, L., Khalili, L. & Haji Reza, P. Hyperspectral absorption microscopy using photoacoustic remote sensing. Opt. Express 29, 24338–24348 (2021).  
21. Hu, G. et al. Noncontact photoacoustic lipid imaging by remote sensing on first overtone of the C–H bond. Adv. Photon. Nexus 2, 026011 (2023).  
22. Rose, A., Salamo, G. J. & Gupta, R. Photoacoustic deflection spectroscopy: a new specie-specific method for combustion diagnostics. Appl. Opt. 23, 781–784 (1984).  
23. Shin, J. Y., Shaloski, M. A., Crim, F. F. & Case, A. S. First evidence of vibrationally driven bimolecular reactions in solution: reactions of Br atoms with dimethylsulfoxide and methanol. J. Phys. Chem. B 121, 2486–2494 (2017).  
24. Vardaki, M. Z. & Kourkoumelis, N. Tissue phantoms for biomedical applications in Raman spectroscopy: a review. Biomed. Eng. Comput. Biol. 11, 1179597220948100 (2020).  
25. Ishiguro, T. et al. Tumor-derived spheroids: relevance to cancer stem cells and clinical applications. Cancer Sci. 108, 283–289 (2017).  
26. Bian, X. et al. Lipid metabolism and cancer. J. Exp. Med. 218, e20201606 (2021).  
27. Kuriu, S., Kadonosono, T., Kizaka-Kondoh, S. & Ishida, T. Slicing spheroids in microfluidic devices for morphological and immunohistochemical analysis. Micromachines 11, 480 (2020).  
28. Wei, M. et al. Volumetric chemical imaging by clearing-enhanced stimulated Raman scattering microscopy. Proc. Natl Acad. Sci. USA 116, 6608–6617 (2019).  
29. Edwards, S. J. et al. High-resolution imaging of tumor spheroids and organoids enabled by expansion microscopy. Front. Mol. Biosci. 7, 208 (2020).  
30. Pampaloni, F., Ansari, N. & Stelzer, E. H. High-resolution deep imaging of live cellular spheroids with light-sheet-based fluorescence microscopy. Cell Tissue Res. 352, 161–177 (2013).  
31. Konig, K., Uchugonova, A. & Gorjup, E. Multiphoton fluorescence lifetime imaging of 3D-stem cell spheroids during diferentiation. Microsc. Res. Tech. 74, 9–17 (2011).  
32. Yu, Y., Ramachandran, P. V. & Wang, M. C. Shedding new light on lipid functions with CARS and SRS microscopy. Biochim. Biophys. Acta 1841, 1120–1129 (2014).  
33. Pradas, I. et al. Lipidomics reveals a tissue-specific fingerprint. Front. Physiol. 9, 1165 (2018).  
34. Shi, L., Fung, A. A. & Zhou, A. Advances in stimulated Raman scattering imaging for tissues and animals. Quant. Imaging Med. Surg. 11, 1078–1101 (2021).  
35. Taqi, S. A., Sami, S. A., Sami, L. B. & Zaki, S. A. A review of artifacts in histopathology. J. Oral Maxillofac. Pathol. 22, 279 (2018).  
36. Urasaki, Y., Zhang, C., Cheng, J. X. & Le, T. T. Quantitative assessment of liver steatosis and afected pathways with molecular imaging and proteomic profiling. Sci. Rep. 8, 3606 (2018).  
37. Singh, M. S. & Thomas, A. Photoacoustic elastography imaging: a review. J. Biomed. Opt. 24, 1–15 (2019).  
38. Streich, L. et al. High-resolution structural and functional deep brain imaging using adaptive optics three-photon microscopy. Nat. Methods 18, 1253–1258 (2021).  
39. Hu, S. & Wang, L. V. Optical-resolution photoacoustic microscopy: auscultation of biological systems at the cellular level. Biophys. J. 105, 841–847 (2013).

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2024

## Methods

## Chemicals

The oil and DMSO solution samples were prepared by sandwiching 2 µl liquid with two no. 1 coverslips. Eighty micrometre double-sided tape was placed between the two coverslips as a spacer. To prepare the sample of PS beads, an aqueous solution of PS beads was first prepared and mixed well with an ultrasound homogenizer to avoid large aggregates. Then the bead solution was dried on a no. 1 coverslip. When performing SWIP imaging, the coverslip side was on the top to isolate the beads from the immersion medium or the scattering phantom. The protein and DNA samples for the SWIP spectrum acquisition were prepared by sandwiching bovine serum albumin crystal (A2153, Sigma-Aldrich) and DNA powder (D3159, Sigma-Aldrich) between two no. 1 coverslips with 80 µm double-sided tape as the spacer.

## Cancer cells and spheroids

Cisplatin-resistant ovarian cancer cells (OVCAR-5-cisR)40 were generously provided by the Daniela Matei Lab at Northwestern University. The cells were cultured in RPMI 1640 with 10% fetal bovine serum, 100 units per ml penicillin and 100 µg ml−1 streptomycin. Cells were seeded on a coverslip for 24 hours for monolayer cell imaging. To form ovarian cancer spheroids, 200 µl per well of OVCAR-5-cisR cell suspension was added to an ultralow attachment 96-well plate with a cell density of 0.5 × 104 cells per ml. The spheroids were cultured for 7 days. Cells were then kept in 1× PBS and sealed in between two coverslips with spacers.

## Biological tissues

The fresh swine liver was purchased from the supermarket. Before imaging, the liver was hand-sliced into around 3 mm and sandwiched between two no. 1 coverslips. The mouse ear sample was isolated from a 6-month-old mouse and fixed with 10% formalin solution. Before imaging, the ear was rinsed with 1× PBS and then attached to a coverslip. The mouse brain was from a 6-month-old mouse and fixed with 10% formalin solution. The brain was sliced to be 1 mm thick with a vibratome. Before imaging, the brain was rinsed with 1× PBS and then attached to a coverslip. The de-identified healthy human breast biopsy sample was obtained from the Susan G. Komen Tissue Bank at the IU Simon Cancer Center. The breast biopsy sample was freshly frozen and had a thickness of \~0.6 mm. Before imaging, the breast biopsy sample was defrosted and then sandwiched between two coverslips.

## SWIP microscope

Both pump and probe beams are in the SWIR window to ensure deep tissue penetration. The pulsed pump beam is generated by an optical parametric oscillator (DX-1725-OPO, Photonics Industries), with a repetition rate of 2 kHz, wavelength centred at 1,725 nm and a pulse duration of 10 ns. The 1,310 nm probe beam is provided by a continuous-wave diode laser (TURN-KEY CCS-LN/1310LD-4-0-0/ OC, Research Lab Source). The 1,725 nm excitation laser is chosen to excite the first overtone of C–H stretching vibrations. Although the first C–H overtone absorption cross section is around two orders of magnitude smaller than the fundamental absorption41,42, detecting at the first overtone region can circumvent the strong water absorption in the mid-infrared region where water absorption is more than three orders stronger than that in the SWIR region43. Moreover, compared with the second overtone, the first overtone of C–H gives a seven times larger signal from lipids44.

The beam sizes of the 2 lasers were adjusted to be around 6 mm with telescopes. The telescopes were also used for optimizing the axial offset of the two laser foci on the sample to obtain the maximum SWIP signal45. After beam expansion, the two lasers were collinearly combined with a dichroic mirror and then focused into a sample through an objective lens. Two objective lenses were used for the experiments. A 1.0 NA water-immersion objective with an 800 µm working distance (UPLSAPO30XSIR, Olympus) was used to image the polymer beads, cancer cells, spheroids, swine liver and human breast biopsy. A 2 mm working distance objective with an effective NA of \~0.4 was applied for mouse ear and brain imaging. The transmitted light from the sample was collected by an air condenser (D-CUO, Nikon) with an adjustable aperture. After the condenser, the remaining excitation laser was filtered out by a 1,310 nm band-pass filter (FBH1310-12, Thorlabs). The signal-carrying probe beam is detected by a biased InGaAs photodiode. When recording both PA and PT signals, we used a small-area high-speed photodiode (70 MHz bandwidth, 0.8 mm2 , DET10N2, Thorlabs). When targeting only the PT signal, we used a slower photodiode with a larger active area (11.7 MHz bandwidth, 3.14 mm2 , DET20C2, Thorlabs). The photocurrent from the photodiode is converted to a voltage signal with a 50 Ω impedance and then amplified by an a.c.-coupled low-noise voltage amplifier (100 MHz bandwidth, SA230F5, NF Corporation) and digitized by a high-speed data acquisition card at 180 MSa s−1 (ATS9462, Alazar Tech). Every excitation laser pulse corresponds to a single pixel in the image. The image was formed by sample scanning achieved with a stage (Nano-Bio 2200, Mad City Labs). The volumetric image was acquired with a motorized z-knob to allow axial scanning.

## SWIP image formation

Every pixel in the SWIP image corresponds to one excitation laser pulse, for which a temporal trace of the probe laser intensity will be recorded. A gating method is applied to turn the signal temporal trace to pixel intensity. Two averaging windows are used: the first window is set before the excitation pulse arriving to estimate the probe intensity baseline; the second window starts at intensity extremum right after the excitation to obtain the changed probe intensity. The pixel intensity is assigned to be the difference between the two window averages. This gating method takes advantage of the long decay of the PT signal for a better SNR. Multiple window sizes have been tested and the size of 80 sampling points (\~450 ns) is chosen to output the best SNR.

## SWIP spectroscopy

The SWIP spectra were acquired by replacing the single-colour excitation laser with a tunable excitation laser (Opolette HE 355 LD, OPOTEK), which has a tuning range from 410 nm to 2,400 nm, a pulse duration of 5 ns and a repetition rate of 20 Hz. Other parts in the SWIP microscope remained unchanged. The spectral scanning was achieved by manuall tuning the laser wavelength with a step size of 10 nm.

## Time-domain extraction of the SWIP signal from the water background

The thermal property is closely related to the object size, shape and chemical constitution. The thermal decay coefficient of the SWIP signal can therefore provide extra information for differentiating small objects within the bulk medium. When the particle size is smaller than the SWIP heating volume (usually satisfied for intracellular features as the axial resolution of SWIP is 3.5 µm), the heat dissipation of the small object is faster than that of the bulk surrounding medium. The single-pixel SWIP traces shown in Fig. 4b,c support this hypothesis. To reject the background from the bulk medium with the thermal decay difference, the decay part of every SWIP signal trace is fitted with a two-component exponential function. A two-component exponential function is selected, considering that the detected SWIP signal consists of the in-focus target and out-of-focus water background contribution. A weight w(x, y) is calculated by thresholding the decay coefficient d(x, y) of the faster decay component. The water background is estimated by a(x, y) + c(x, y) × w(x, y), where a(x, y) and c(x, y) are the amplitudes of the two fitted exponential components. Assuming that the water background is spatially slow varying, we applied a Gaussian blurring filter on the estimated water background to avoid a sharp spatial inten sity change. The final image is generated by subtracting the water background from the raw image. The background rejection workflow is shown in Supplementary Fig. 8.

Considering that the fitting fidelity is related to the SNR, we tested the robustness of our fitting-based background rejection algorithm. As presented in Supplementary Fig. 9, weak signals with an SNR of around 8 can be extracted with high fidelity.

## LOD measurement

The LOD is the molar concentration with a signal intensity as three times of background standard deviation over the background46. If the signal has a linear dependence on the concentration, the LOD can be calculated by LOD = 3σ/S (ref. 46), where σ is the standard deviation of the background intensity and S is the fitted slope of the signal versus concentration.

## SRS microscope

Two synchronized femtosecond laser pulse trains with an 80 MHz repetition rate were used for SRS imaging. The wavelengths of the lasers are at 800 nm and 1,040 nm to target the C–H stretch vibration. The 1,040 nm laser is modulated by an acousto-optic modulator at 2.27 MHz to separate the SRS signal from the laser repetition rate frequency. The SRS is conveyed by the modulation transfer from 1,040 nm to 800 nm laser at 2.27 MHz. The two lasers are chirped to a few picoseconds with SF57 glass rods for spectral focusing. A dichroic mirror spatially combines the two lasers. The combined beams pass a pair of galvo mirrors for laser scanning and then are focused on the sample by the same objective (1.0 NA, UPLSAPO30XSIR, Olympus) used for SWIP. The transmitted light is collected by a 1.4 NA oil-immersion condenser and filtered by a 980 nm short-pass filter. The residue 800 nm laser is detected by a biased photodiode. The SRS signal is obtained by demodulating the signal received by a photodiode with a lock-in amplifier.

## Data availability

Source data are available via figshare at https://doi.org/10.6084/m9. figshare.25687185 (ref. 47).

## Code availability

Code is available via figshare at https://doi.org/10.6084/m9. figshare.25687185 (ref. 47).

## References

40. Tan, Y. et al. Metabolic reprogramming from glycolysis to fatty acid uptake and beta-oxidation in platinum-resistant cancer cells. Nat. Commun. 13, 4554 (2022).  
41. Cias, P., Wang, C. & Dibble, T. S. Absorption cross-sections of the C–H overtone of volatile organic compounds: 2 methyl-1,3-butadiene (isoprene), 1,3-butadiene, and 2,3-dimethyl-1,3-butadiene. Appl. Spectrosc. 61, 230–236 (2007).  
42. Bai, J. et al. Sensitivity analysis of 1,3-butadiene monitoring based on space-based detection in the infrared band. Remote Sens. 14, 4788 (2022).  
43. Bertie, J. E. & Lan, Z. Infrared intensities of liquids XX: the intensity of the OH stretching band of liquid water revisited, and the best current values of the optical constants of H O(l) at 25 °C between 15,000 and 1 cm−1. Appl. Spectrosc. 50, 1047–1057 (1996).  
44. Wang, P., Wang, H. W., Sturek, M. & Cheng, J. X. Bond-selective imaging of deep tissue through the optical window between 1600 and 1850 nm. J. Biophoton. 5, 25–32 (2012).  
45. Selmke, M., Braun, M. & Cichos, F. Photothermal single-particle microscopy: detection of a nanolens. ACS Nano 6, 2741–2749 (2012).  
46. MacDougall, D. et al. Guidelines for data acquisition and data quality evaluation in environmental chemistry. Anal. Chem. 52, 2242–2249 (1980).  
47. Ni, H. et al. Millimeter-deep micron-resolution vibrational imaging by shortwave infrared photothermal microscopy. figshare https://doi.org/10.6084/m9.figshare.25687185 (2024).

## Acknowledgements

Human breast samples from the Susan G. Komen Tissue Bank at the IU Simon Cancer Center were used in this study. This work is supported by NIH R35GM136223, R33CA261726, R01 HL125385, R01 EB032391 and R01CA224275 to J.-X.C. We thank L. Lu for advice on the photothermal detection scheme and G. Chen for help in understanding photoacoustic signal propagation. We acknowledge M. Cherepashensky for proofreading of the paper.

## Author contributions

H.N. developed the SWIP system, designed the experiments, processed the data, built the theoretical models and drafted the paper. Y.Y. helped in the experiments and paper writing, performed the theoretical analysis, and prepared cancer cell and spheroid samples. M.L. provided the mouse tissue and helped in data analysis. Y.Z. contributed to the project formulation and building of theoretical models. X.G. contributed to the project formulation and data analysis. J.Y. helped in optimizing the photothermal detection scheme. C.P.D. prepared the human breast biopsy sample. L.W. helped in the SRS experiment. J.-X.C. initialized the project, revised the paper and provided scientific guidance.

## Competing interests

J.-X.C. declares financial interest with Photothermal Spectroscopy Corp, which did not support this work. The other authors declare no competing interests.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41566-024-01463-6.

Correspondence and requests for materials should be addressed to Ji-Xin Cheng.

Peer review information Nature Photonics thanks Keisuke Goda and Lu Wei for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.