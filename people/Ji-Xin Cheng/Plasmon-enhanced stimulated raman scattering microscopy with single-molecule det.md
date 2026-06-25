ARTICLE

https://doi.org/10.1038/s41467-019-13230-1

OPEN

# Plasmon-enhanced stimulated Raman scattering microscopy with single-molecule detection sensitivity

Cheng Zong1,2, Ranjith Premasiri3,4, Haonan Lin1 , Yimin Huang3, Chi Zhang1 , Chen Yang3,4, Bin Ren Lawrence D. Ziegler3,4 & Ji-Xin Cheng1,3,4\*

Stimulated Raman scattering (SRS) microscopy allows for high-speed label-free chemical imaging of biomedical systems. The imaging sensitivity of SRS microscopy is limited to \~10 mM for endogenous biomolecules. Electronic pre-resonant SRS allows detection of submicromolar chromophores. However, label-free SRS detection of single biomolecules having extremely small Raman cross-sections $( \cdot 1 0 ^ { - 3 0 } \mathsf { c m } ^ { 2 } \mathsf { s r } ^ { - 1 } )$ remains unreachable. Here, we demonstrate plasmon-enhanced stimulated Raman scattering (PESRS) microscopy with single-molecule detection sensitivity. Incorporating pico-Joule laser excitation, background subtraction, and a denoising algorithm, we obtain robust single-pixel SRS spectra exhibiting single-molecule events, verified by using two isotopologues of adenine and further confirmed by digital blinking and bleaching in the temporal domain. To demonstrate the capability of PESRS for biological applications, we utilize PESRS to map adenine released from bacteria due to starvation stress. PESRS microscopy holds the promise for ultrasensitive detection and rapid mapping of molecular events in chemical and biomedical systems.

aman spectroscopy is a versatile analytical tool providing information about the native fingerprint vibrational states of a sample determined by its molecular structure and chemical environment. Non-electronically resonant spontaneous vibrational Raman scattering cross-sections are typically $1 0 ^ { - 3 0 } \mathsf { c m } ^ { 2 } \mathsf { s r } ^ { - 1 }$ and intrinsically small cross-sections on this order result in detection limits only as low as milli-molar (mM) levels. By placing a molecule close to a plasmonic nanostructure, plasmon-enhanced Raman spectroscopy pushes the detection sensitivity to the singlemolecule level1–9, yet the speed in spectral acquisition is still not sufficient for ultrasensitive chemical mapping of molecular events in a dynamic and complex system10

Owing to the development of advanced lasers and electro-optic instruments, nonlinear Raman microscopy has been shown to provide label-free chemical imaging, based on either coherent anti-Stokes Raman scattering (CARS) or stimulated Raman scattering (SRS), for a broad range of biomedical applications11. Early developments of CARS and SRS microscopy relied on picosecond pulses for detection of a single Raman $\mathrm { p e a k } ^ { 1 2 - 1 7 }$ . Intra-pulse broadband CARS, developed by Cicerone and coworkers, allowed recording of a whole Raman spectrum within $3 . 5 \mathrm { m s } ^ { 1 8 }$ Hyperspectral SRS microscopy has been achieved recently by many strategies, such as wavelength tuning19,20, spectral-focusing21,22, optical frequencies coding23, etc, which provide spectral profile at each image pixel and enable the discoveries of new biology24,25. Multiplex SRS microscopy developed by Cheng and coworkers26, is able to acquire a Raman spectrum covering a 200 wavenumber spectral window within 5 µs, which allowed high-throughput chemical analysis in a flow cytometry setting27. Yet, the imaging sensitivity of SRS microscopy is limited to \~10 mM for chemical bonds such as the C-H vibrations in cell membranes22,28. Min and coworkers recently reported electronic pre-resonance SRS achieving sub-micromolar-sensitivity detection for chromophores having a Raman cross-section $1 0 ^ { ^ { 3 } }$ or 104 times larger than endogenous biomolecules29,30.

To push coherent Raman detection sensitivity further, plasmonenhanced CARS has been reported31–37 and single-molecule sensitivity has been proved32,34,35. While, the CARS signal displays a nonlinear dependence on the concentration of analytes38. The SRS signal, on the other hand, shows a linear dependence on the concentration of analytes17. The Van Duyne group reported reproducible surface-enhanced femtosecond SRS spectra from molecules embedded in a gold nano-dumbbell $\mathrm { s o l } ^ { 3 9 , 4 0 }$ . Yet, plasmon-enhanced SRS at single-molecule detection sensitivity has not been reported. Major hurtles of achieving single-molecule SRS detection include the damage of plasmonic substrates by the ultrafast pulses41 and a large pump-probe background, arising from plasmon-induced photothermal and/or stimulated emission process.

Here, we report plasmon-enhanced SRS (PESRS) microscopy (Fig. 1a, instrument in Supplementary Fig. 1) and its application to ultrasensitive imaging of biomolecules released from cells. We reach single-molecule detection sensitivity by incorporating several innovations. First, we use chirped laser pulses at 80 MHz repetition rate for spectral-focusing hyperspectral SRS imaging. The pulse energy on the sample is on the level of pico-Joule. Such low pulse energy together with chirping to picosecond duration effectively avoided sample photodamage, while the high repetition rate allowed fast chemical mapping of molecules adsorbed on gold nanostructured surfaces. Second, we employ a penalized least squares (PLS) approach and successfully extract the sharp Raman peaks from a spectrally broad non-Raman background largely contributed by the photothermal effect42. Third, harnessing a block-matching and 4D filtering (BM4D) algorithm to denoise a hyperspectral stack, we are able to generate high-quality single-pixel SRS spectra for statistical analysis of single-molecule events. By a bianalyte method43–46, we use two isotopologues of adenine that offer unique vibrational signatures and verify PESRS detection of single molecules with Raman cross-section as low as $1 0 ^ { - 3 0 } \mathrm { c m } ^ { 2 }$ per molecule. Furthermore, we demonstrate PESRS imaging of adenine resulting from nucleotide degradation as a stress response of S. aureus cells to starvation.

## Results

Plasmon-enhanced stimulated Raman scattering spectroscopy. Adenine adsorbed on gold nanoparticles (Au NPs) aggregation substrates (see Methods) is selected as a proof-of-principle system for the demonstration of PESRS. Adenine is one of the four constituent bases of nucleic acids. The Raman band at $7 2 3 \mathrm { c m } ^ { - 1 }$ of adenine powder, which has a cross-section of $2 . 9 \times 1 0 ^ { - 3 0 } \mathrm { c m } ^ { 2 4 7 }$ , has been studied for single-molecule detection by surface-enhanced Raman spectroscopy (SERS)46,47 and surface-enhanced CARS34. As shown in Fig. 1a, a pump laser centered at 969 nm and a Stokes laser centered at 1040 nm are employed to induce a PESRS spectrum covering a window ranging from 550 to 850 cm−1. Then, 10 µL of a 5 mM aqueous adenine solution is added to ca. 2–4 µL of a concentrated Au colloid suspension, which induces the aggregation of Au NPs. A representative extinction spectrum of an adenine-induced Au NPs aggregation substrate is shown in Fig. 1b. The plasmonic band of the aggregated Au NPs is broad and peaked at 1040 nm, which allows PESRS for the pump and Stokes laser wavelength used here. The resulting PESRS spectrum (Fig. 1c, black) from the adenine-adsorbed Au NPs aggregates consists of a narrower feature at $7 3 3 c m ^ { - 1 }$ (highlighted by green) on top of a strong and broad non-resonant background. This sharp feature is close to the prominent adenine ring-breathing mode frequency observed in the normal SRS spectrum of adenine powder (Fig. 1c, blue) and identical to the corresponding $7 3 3 c m ^ { - 1 }$ peak observed in the SERS results on Au substrates (Supplementary Fig. $2 ) ^ { 4 8 }$ . The blank result (Fig. 1c, red) is independently measured from the Au NPs substrate without adenine adsorption. The background could arise from three different non-Raman processes: photothermal effect, cross-phase modulation, and transient absorption42, all due to laser interactions with the gold nanostructures. The spectral shif between the substrate with/without adenine may relate to the different extent of aggregation with/without adenine. These back grounds are spectrally overlapped with the SRS signal, but are largely independent of the Raman shift42. In contrast, the SRS signal originates from a vibrational resonance that has a sharp spectral feature. A PLS approach is used to fit the broad spectral background. The resulting fitting backgrounds of PESRS are shown in Fig. 1c as the dash lines for the corresponding observed PESRS spectra. Figure 1d shows the vibrationally resonant component of the PESRS spectra resulting from subtraction of the fitting backgrounds from the observed PESRS signals. The PESRS spectrum of adsorbed adenine shows a dominated peak at $7 3 3 c m ^ { \div 1 }$ . Only a noisy baseline is evident after background subtraction from the pure substrate spectrum. Compared with the SRS spectrum of adenine crystal (blue line in Fig. 1d), $\mathrm { { a \ 1 0 \mathrm { c m } ^ { - 1 } } }$ blue shift of the peak is observed in the PESRS spectrum. This blue shifted frequency (733 cm−1) is consistent with the strongest vibrational feature observed in SERS spectra of adenine (Supplementary Fig. $2 ) ^ { 4 9 } .$ These results collectively indicate that the observed vibrational PESRS signal component originates from the surface adsorbed adenine. Figure 1d (purple) presents the standard SRS spectrum of adenine powder at the same laser power condition as used for the detection of PESRS. The standard SRS setup could not generate any Raman signal from a pure adenine powder, while PESRS could detect a thin layer of adenine adsorbed on Au nanostructures. This result indicates that the large electromagnetic field boosted by the plasmon significantly amplified the stimulated Raman process.

a  
![](images/4b03902b57582b26141e7baa2d1714a45e3e02f22b1077f03178de31f4288e34.jpg)

<details>
<summary>chemical</summary>

Diagram illustrating pump and stoke energy levels in a molecular system with labeled components
</details>

b  
![](images/e1b5f4a1ef74ddffac83eb691b4bfc9ae0932958ed93f79258d3c4cacecad698.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Extinction (arb. units) |
| --------------- | ------------------------ |
| 400             | 0.25                     |
| 600             | 0.27                     |
| 800             | 0.30                     |
| 1000            | 0.35                     |
| 1200            | 0.32                     |
| 1400            | 0.25                     |
</details>

c  
![](images/acc0472ddccd164704a5cdfedbdb552df9979b243606e18135af85e22b83c0e0.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | PESRS | Substrate | SRS |
| ------------------ | ----- | --------- | --- |
| 550                | 0.75  | 0.80      | 0.02 |
| 600                | 0.85  | 0.90      | 0.03 |
| 650                | 0.95  | 0.98      | 0.04 |
| 700                | 1.00  | 1.00      | 0.95 |
| 750                | 0.90  | 0.85      | 0.10 |
| 800                | 0.70  | 0.60      | 0.02 |
| 850                | 0.50  | 0.35      | 0.01 |
</details>

d  
![](images/593b632f217aefda9b72e9f39f08224e4a8eb881f2228e900ab587b5d1b5b293.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | PESRS | Substrate | SRS |
| ------------------ | ----- | --------- | --- |
| 600                | ~0.01 | ~0.01     | ~0.0 |
| 650                | ~0.01 | ~0.01     | ~0.0 |
| 700                | ~0.01 | ~0.01     | ~0.0 |
| 750                | ~0.05 | ~0.02     | ~0.0 |
| 800                | ~0.01 | ~0.01     | ~0.0 |
| 850                | ~0.01 | ~0.01     | ~0.0 |
</details>

e  
![](images/c28d6959da5bdf19e724e6277731cfc66b8ede5e52b5906a3743c5527250bc77.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | 969 nm | 972 nm | 942 nm |
| ------------------ | ------ | ------ | ------ |
| 600                | 0.75   | 0.78   | 0.76   |
| 650                | 0.95   | 0.98   | 0.97   |
| 700                | 1.00   | 1.00   | 1.00   |
| 750                | 0.85   | 0.88   | 0.87   |
| 800                | 0.65   | 0.68   | 0.67   |
| 850                | 0.50   | 0.52   | 0.51   |
| 900                | 0.45   | 0.47   | 0.46   |
| 950                | 0.48   | 0.50   | 0.49   |
| 1000               | 0.52   | 0.55   | 0.54   |
| 1050               | 0.58   | 0.62   | 0.61   |
| 1100               | 0.65   | 0.72   | 0.71   |
</details>

f  
![](images/cbb56797bad1431f2fd337c12c94d6312b38ee7f5787bdac1bfed33f3e6fd0ee.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | 969 nm- BG | 972 nm- BG | 942 nm- BG |
| ------------------ | ---------- | ---------- | ---------- |
| 600                | ~0.00      | ~0.01      | ~0.00      |
| 700                | ~0.04      | ~0.03      | ~0.00      |
| 800                | ~0.01      | ~0.02      | ~0.01      |
| 900                | ~0.00      | ~0.01      | ~0.01      |
| 1000               | ~0.00      | ~0.01      | ~0.01      |
| 1100               | ~0.00      | ~0.01      | ~0.01      |
</details>

Fig. 1 PESRS spectroscopy. a A schematic of PESRS. b A representative extinction spectrum of adenine-induced Au NPs aggregation substrate. c The PESRS spectrum (solid) with a green highlighted portion and fitted background (dash) obtained from the substrate with adenine adsorption. The blank spectrum (solid) and fitted background (dash) obtained from the substrate without adenine. The total power of pump and Stokes was 0.4 mW. The SRS spectrum of adenine powder (blue) was obtained with a pump power at 10 mW and a Stoke power at 50 mW. d The background-subtracted PESRS spectrum of adsorbed adenine versus the SRS spectrum of adenine powder (same as blue line in c) and the spectrum of blank substrate. Inset: The SRS spectrum of adenine powder obtained as the same laser power condition as the PESRS. e PESRS spectra (solid) and fitted background (dash) of adenine at Raman resonance (969 nm and 972 nm) and off-resonance (942 nm). f Background-subtracted PESRS spectra of adenine at Raman resonance and off-resonance BG: background.

To verify that the SRS signal is due to the adenine vibrational resonance, we vary the pump wavelength while keeping the Stokes wavelength fixed. The pump laser centered at 972 nm, as well as the previous 969 nm wavelength encompass the adenine Raman resonance for a 1040 nm Stokes pulse, and both generated SRS spectra showing a pronounced peak at the expected wavenumber (Fig. 1e, black and red). In contrast, the 942 nm is off-resonance for the $7 3 3 \mathrm { c m } ^ { - 1 }$ band. Accordingly, the measured spectrum does not exhibit such a peak as shown in Fig. 1e (blue). After subtraction of the background in Fig. 1e (corresponding fitted backgrounds were shown as dash lines), the PESRS spectra of adenine excited by both Raman resonance wavelengths show a Raman peak at 733 cm−1 (black and red, Fig. 1f), whereas the offresonance spectrum only shows a noisy featureless baseline (blue, Fig. 1f). Moreover, as shown in Supplementary Fig. 3, the intensity of the 733 cm−1 peak linearly depends on the pump power and the Stokes power before it reaches saturation. To evaluate the degree of photodamage, we continually measured a 1-mM adenine PESRS sample at the same location (Supplementary Fig. 4 and Supplementary Movie 1). About 20% of the signal is lost after 1.5 h continuous exposure. The reproducible spectra recorded at the same location demonstrate that the laser power in our experiment minimally damaged the substrate or induced molecular photodegradation during SRS imaging (\~1.0 min per hyperspectral stack). These results collectively confirm the SRS origin of the vibrationally resonant component of the observed spectrum and the plasmonic enhancement of this signal. To ensure that our method is not specific to adenine, we tested other molecules. Supplementary Fig. 5 shows the PESRS spectra of Rhodamine 800 (85 μM in solution) and 4-mercaptopyridine (5.7 mM in solution) adsorbed on the Au NPs aggregated substrate.

![](images/fd13c5739892bc9c4699ab61a63f9802ac9f75a5d15bd2cf7feb26e3c891f252.jpg)

<details>
<summary>text_image</summary>

Raw image
2
1
5 um
</details>

b  
![](images/0835fe40a9affdd1344ab7453bdb611b6cf1158c2d0df7d288d2360e6be855f8.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (arb. units) - 1 | Intensity (arb. units) - 2 |
| ------------------ | --------------------------- | --------------------------- |
| 550                | ~0.04                       | ~0.005                      |
| 600                | ~0.05                       | ~0.008                      |
| 650                | ~0.06                       | ~0.007                      |
| 700                | ~0.06                       | ~0.009                      |
| 750                | ~0.05                       | ~0.008                      |
| 800                | ~0.03                       | ~0.01                       |
| 850                | ~0.02                       | ~0.01                       |
</details>

c  
![](images/968b331b71ceb80e136d4966eaeadc0134d699a59c10ec7d2f264c9258ff49a3.jpg)

<details>
<summary>text_image</summary>

Background corrected
2
1
5 um
</details>

d  
![](images/4ec1d891ce84862c2250835d6ccdf1879efd2ba6219aba28f0bbf788d5955e4f.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (arb. units) - 1 | Intensity (arb. units) - 2 |
| ------------------ | --------------------------- | --------------------------- |
| 550                | ~0.008                      | ~0.006                      |
| 600                | ~0.012                      | ~0.007                      |
| 650                | ~0.004                      | ~0.003                      |
| 700                | ~0.014                      | ~0.005                      |
| 750                | ~0.018                      | ~0.006                      |
| 800                | ~0.008                      | ~0.004                      |
| 850                | ~0.006                      | ~0.007                      |
</details>

e  
![](images/3c7ecd139de4e0fc1337c574ebff4eac66b085fb0945f2159170a9d03872dfd3.jpg)

<details>
<summary>text_image</summary>

BM4D denoising
Int
0.06
0.05
0.04
0.03
0.02
0.01
2
1
5 um
</details>

f  
![](images/0fb0f9dfda67189e1d671123b63497ef8d16d74a3b876822f2f12c9b0f7e32d7.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (arb. units) - 1 | Intensity (arb. units) - 2 |
| ------------------ | --------------------------- | --------------------------- |
| 550                | ~0.001                      | ~0.000                      |
| 600                | ~0.004                      | ~0.000                      |
| 650                | ~0.003                      | ~0.000                      |
| 700                | ~0.008                      | ~0.000                      |
| 750                | ~0.010                      | ~0.000                      |
| 800                | ~0.001                      | ~0.000                      |
| 850                | ~0.001                      | ~0.000                      |
</details>

Fig. 2 Single-pixel PESRS. a The raw PESRS image of aggregated Au NPs substrate with adsorbed adenine. The color of each pixel represents the average total spectral channels intensity from each PESRS spectrum. b The raw single pixel spectra obtained from spot 1 and 2, which are indicated in a. c The PESRS image of adsorbed adenine on aggregated Au NPs substrate. The color of each pixel represents the peak area at $7 3 3 \mathsf { c m } ^ { - 1 }$ after background subtraction. d The background-removed single-pixel spectra obtained from spot 1 and 2 which are indicated in c. e The BM4D-denoised PESRS image of adsorbed adenine on aggregated Au NPs substrate. The color of each pixel represents the peak area at $7 3 3 \mathsf { c m } ^ { - 1 }$ after BM4D denoising and background subtraction. f The BM4D-denoised single-pixel spectra obtained from spot 1 and 2 which are indicated in e. Image area: 30 μm × 30 μm.

PESRS at single-pixel level. To demonstrate the imaging capability of PESRS, we scan the adenine containing aggregated Au

NPs substrate with a pixel dwell time of 10 μs. It takes ca. 1 min to obtain a hyperspectral cube (200 × 200 pixel, 80 Raman shifts) consisting of 40,000 spectra. In Fig. 2a, the averaged total 80 spectral channels of an original PESRS hyperspectral data cube are plotted to show the spatial distribution of aggregated NPs. Figure 2b shows two single-pixel spectra from regions with and without NP aggregates, indicated as spot 1 and spot 2, respectively. The single-pixel spectrum from spot 1 shows a broad background and a weak Raman peak around $7 3 3 c m ^ { - 1 }$ . After pixel by pixel subtraction of the fitting background, the area of the resulting vibrational band at $7 3 3 \mathrm { c m } ^ { - \widetilde { 1 } }$ at each pixel is shown in Fig. 2c revealing a clear spatial contrast between regions of adsorbed adenine and blank areas. The single-pixel background-removed spectra from spot 1 and 2 are displayed in Fig. 2d. It remains challenging to obtain high-quality single-pixel spectra due to the noisy non-Raman background. To address this challenge, we employ a BM4D algorithm which was widely used for 3D data denoising50,51. The reconstructed peak area image and the single-pixel spectra after BM4D denoising and background removal are shown in Fig. 2e, f, respectively. By employing BM4D, we achieve a signal-to-noise ratio of 33 for the single-pixel spectra at spot $1 , \sim 4$ times better than that without denoising. Good Raman reproducibility in terms of peak frequency in different locations of the imaging area is found (see Supplementary Fig. 6) even given an expected inhomogeneous intensity distribution due to the Au NPs randomly aggregated hot spots.

a  
![](images/64c966f1fcbdae2a607ccef7433b084f6c8a9bddb4ceee2ba7b4aac4d0e3be26.jpg)

<details>
<summary>text_image</summary>

PD
Filter
PBS
QWP
</details>

b  
![](images/18234d135882fc72a13971807fde822dbb900d4d7fd5cc993e8d30cb4732678e.jpg)

<details>
<summary>text_image</summary>

2
1
5 um
Int
0.14
0.12
0.1
0.08
0.06
0.04
0.02
</details>

c  
![](images/b852ac0516c4be85f5bc6988b83f9d4c77dd0f67a8db974a86f4c17c37824f39.jpg)

<details>
<summary>heatmap</summary>

| Region | Value |
|--------|-------|
| 1      | 0.1   |
| 2      | 0.1   |
</details>

d  
![](images/3d9e5c13625fb71df8c2d7f347c7a97e2e158f2973f35d4762a4d0b0a3a929a7.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | RAW-1 | BM4D-1 | RAW-2 | BM4D-2 |
| ------------------ | ----- | ------ | ----- | ------ |
| 550                | ~0.8  | ~0.6   | ~0.3  | ~0.2   |
| 600                | ~0.9  | ~0.7   | ~0.3  | ~0.2   |
| 650                | ~0.8  | ~0.6   | ~0.3  | ~0.2   |
| 700                | ~1.0  | ~0.8   | ~0.3  | ~0.2   |
| 750                | ~1.2  | ~1.0   | ~0.3  | ~0.2   |
| 800                | ~0.8  | ~0.6   | ~0.3  | ~0.2   |
| 850                | ~0.7  | ~0.5   | ~0.3  | ~0.2   |
</details>

Fig. 3 Epi-detected PESRS. a A schematic of epi-detected PESRS. A polarizing beam splitter (PBS) and a quarter wave plate (QWP) changes the polarization of incoming and backscattered lasers by 90°. In this way, the stimulated Raman loss signal passes the filter and is detected by a photodiode (PD). b Raw PESRS image of adenine adsorbed on $\mathsf { A u N P s  – S i O } _ { 2 }$ substrate. The color of each pixel represents the average intensity of each PESRS spectrum. c Denoised PESRS image of adenine adsorbed on $\mathsf { A u } \mathsf { N P s } { \mathsf { - S i O } } _ { 2 }$ substrate. The color of each pixel represents the intensity of the $7 3 3 \mathsf { c m } ^ { - 1 }$ peak in each denoised and background-corrected PESRS spectrum. The image area is $3 0 \mu \mathrm { m } \times 3 0$ μm. d Single-pixel spectra of adenine on the Au NPs-covered $\mathsf { S i O } _ { 2 }$ substrate obtained from spot 1 and 2 indicated in c.

PESRS is also demonstrated for epi-detection of molecules on a non-transparent plasmonic substrate that is often used in plasmon-enhanced spectroscopy applications. The experimental setup is shown in Fig. 3a. We use a sol-gel-derived $\mathrm { S i O } _ { 2 } ^ { - }$ substrate covered by immobilized aggregates of monodisperse-sized Au NPs (AuNPs–SiO substrate)52. Ten microliter of a 100 μM adenine solution are dropped on this plasmonic substrate and dried in air. The spectrally integrated image (Fig. 3b) reveals the distribution of NP clusters on the SiO chip. After BM4D denoising and background subtraction, the distribution of hot spots is evident in Fig. 3c. Single-pixel spectra extracted from spots 1 and 2 are indicated in Fig. 3d. After denoising, a signal-tonoise ratio of 48 is achieved for these single-pixel spectra. These data collectively show the high sensitivity of epi-detected PESRS.

To estimate the relative enhancement factor of a local hot spot, we assume a monolayer surface coverage of adenine and a monolayer NP cluster under the laser focus. Based on the measured local PESRS intensity (spot 1) and the average SRS intensity of 5 mM adenine solution, the power-averaged and concentration-averaged local enhancement factor of PESRS relative to normal SRS is estimated to be ${ \sim } 7 \times 1 0 ^ { 7 }$ (see details in Supplementary Note 1). Consistent with this result, enhancement factors of $\mathrm { i } 0 ^ { 4 } – 1 0 ^ { 6 }$ and $1 0 ^ { 5 } – 1 0 ^ { 8 }$ were reported for surfaceenhanced femtosecond $\mathrm { S R S } ^ { 3 9 }$ and surface-enhanced CARS spectroscopy33,34,36, respectively.

Single-molecule sensitivity in PESRS. To quantitate the detection sensitivity of PESRS, we use a well-accepted bianalyte approach developed by the Le $\mathrm { R u } ^ { 4 3 , 4 4 }$ and Van Duyne45 groups. The bianalyte approach was developed as a statistically robust method for verification of single molecule detection, as shown in recent single molecule studies in $\mathsf { S E R S ^ { 4 3 - 4 7 } }$ , and ${ \mathrm { S E C A R S } } ^ { 3 4 }$ . The bianalyte approach relies on the observation of two different analytes adsorbed on a nanostructured surface. At the single molecule level, components of the observed spectra can be attributed exclusively to one or the other of the two analytes by virtue of its distinguishable Raman spectrum. The most straightforward bianalyte approach uses a pair of isotopologues that are chemically identical but spectrally distinct. Here, we use a pair of isotopic molecules of adenine $( ^ { \mathrm { 1 4 } } \mathrm { N A } )$ and adenine-1, 3- $\mathrm { \bar { 1 5 } N _ { 2 } } ( ^ { 1 5 } \mathrm { N A } )$ . PESRS spectra of ensemble averaged pure $^ { 1 4 } \mathrm { N A }$ and pure $^ { 1 5 } \mathrm { N A }$ (both 1 mM in solution) show clearly distinguishable Raman bands centered at $7 3 3 \mathrm { c m } ^ { - 1 }$ and 726 cm−1, respectively (Fig. 4a). The PESRS spectrum of an equimolar solution $\mathrm { \dot { o f } ^ { 1 4 } N \dot { A } }$ and $^ { 1 5 } \mathrm { N A }$ displays two Raman band at $7 3 3 \mathrm { c m } ^ { - 1 }$ and $7 2 6 \mathrm { c m } ^ { - 1 }$ The frequency of isotope peaks match well with the SERS measurement (Supplementary Fig. 8) and previous papers46,47. These frequency features allow for identification of individual molecules and their mixture in PESRS spectra. Notably, to clearly distinguish the small Raman shift between $^ { 1 4 } \mathrm { N A }$ and $^ { 1 5 } \mathrm { N A }$ and resolve the concentration ratio of $^ { 1 4 } \mathrm { N A }$ and $^ { 1 5 } \mathrm { N A } .$ , we create more chirping of the pump and Stokes pulses with two additional rods, which improve the spectral resolution to ca. $7 \mathrm { c m ^ { - 1 } }$ (Supplementary Fig. 9) for the single-molecule PESRS study.

a  
![](images/9941dd5a3912d4f389e3f68f07303af2a0bb470fb1d5bfc66b6c1c42ed85883f.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | ¹⁵NA | Mix | ¹⁴NA |
| ------------------ | ---- | --- | ---- |
| 600                | ~0.8 | ~0.6 | ~0.1 |
| 650                | ~0.9 | ~0.7 | ~0.1 |
| 700                | ~0.8 | ~0.6 | ~0.1 |
| 730                | ~1.0 | ~0.8 | ~0.3 |
| 750                | ~0.8 | ~0.6 | ~0.1 |
| 800                | ~0.9 | ~0.7 | ~0.1 |
</details>

b

![](images/b149b82a8d2d25fdb98d3ac42ee8e6d8db10b9c18a5afdde8ae0b6ed56691d5f.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Normalized intensity (1) | Normalized intensity (2) | Normalized intensity (3) |
| ------------------ | ------------------------ | ------------------------ | ------------------------ |
| 600                | ~0.8                     | ~0.6                     | ~0.1                     |
| 650                | ~0.8                     | ~0.6                     | ~0.1                     |
| 700                | ~0.8                     | ~0.6                     | ~0.1                     |
| 730                | ~1.0 (peak)              | ~0.8                     | ~0.1                     |
| 750                | ~0.8                     | ~0.6                     | ~0.1                     |
| 800                | ~0.8                     | ~0.6                     | ~0.1                     |
</details>

c  
![](images/47221e7a891659caf3c9ee3a8f49fccf764ee3596f141bea985f52f1fbbbf156.jpg)

<details>
<summary>scatterplot</summary>

| Concentration of ¹⁴NA | Concentration of ¹⁵NA |
| --------------------- | --------------------- |
| 0.00                  | 0.15                  |
| 0.05                  | 0.05                  |
| 0.10                  | 0.00                  |
| 0.15                  | 0.00                  |
| 0.20                  | 0.00                  |
</details>

d  
![](images/5933344e15bc7d8bc7d4887cf1de6b49712e868a027b2155ba8b18419cb93008.jpg)

<details>
<summary>histogram</summary>

| Relative contribution of 14NA | Relative frequency (%) |
| :--- | :--- |
| 0.0 | 20.8 |
| 0.1 | 3.4 |
| 0.2 | 3.2 |
| 0.3 | 3.4 |
| 0.4 | 4.4 |
| 0.5 | 3.4 |
| 0.6 | 4.7 |
| 0.7 | 3.9 |
| 0.8 | 2.6 |
| 0.9 | 1.8 |
| 1.0 | 17.7 |
The chart displays the relative frequency (%) of the relative contribution of 14NA at 50 nM, with each bar representing a single data point. The x-axis is labeled as 'Relative contribution of 14NA', and the y-axis is labeled as 'Relative frequency (%)'.
</details>

e  
![](images/1b11cb7abe7f94ea277960dc418a5d09a07e92c94012e5d962587580d50f2b95.jpg)

<details>
<summary>line chart</summary>

| Time (min) | Intensity (arb. units) - (70,43) | Intensity (arb. units) - (24,92) |
| ---------- | -------------------------------- | -------------------------------- |
| 0          | ~0.01                            | ~0.01                            |
| 20         | ~0.05                            | ~0.01                            |
| 40         | ~0.02                            | ~0.01                            |
| 60         | ~0.02                            | ~0.01                            |
| 80         | ~0.02                            | ~0.03                            |
| 100        | ~0.02                            | ~0.02                            |
</details>

f  
![](images/22b6c93d30c907802833df361a0f25ca0aa9329df176df2f09aa9da310cafd2d.jpg)

<details>
<summary>line chart</summary>

| Time (min) | Intensity (arb. units) |
| ---------- | ---------------------- |
| 0          | 0.09                   |
| 20         | 0.02                   |
| 40         | 0.02                   |
| 60         | 0.02                   |
| 80         | 0.02                   |
| 100        | 0.02                   |
</details>

Fig. 4 Single-molecule sensitivity in PESRS. a The ensemble PESRS measurements of pure $^ { 1 4 } \mathsf { N A } ,$ pure $^ { 1 5 } { \mathsf { N A } }$ and their equimolar mixture. b Three representative single-pixel PESRS spectra showing a pure $^ { 1 5 } { \mathsf { N A } }$ SM event (1), a mix event (2), and a pure $^ { 1 4 } \mathsf { N A }$ SM event (3), obtained from the 50 nM mixture sample. The vertical dash lines indicate the position of $7 3 0 \mathsf { c m } ^ { - }$ −1 . c Concentration matrix coefficients obtained from MCR analysis of the hyperspectral imaging result sample (including 40000 single-pixel spectra) of the mixture. d Histogram of relative contribution of $^ { 1 4 } \mathsf { N A }$ from the hyperspectral imaging result of the mixture sample. Selected 796 single-pixel spectra with a desired Raman peak and above an intensity threshold were used. SM: single molecule. e–f Representative time traces of PESRS intensity collected of 50 nM adenine sample showing digital intensity fluctuation (e) and single-step photodamage (or photobleach) processes (f). The inside labels in e and f show the $X - Y$ pixel coordinate where the spectra were recorded in Supplementary Movie 2.

To evaluate the sensitivity of PESRS, we prepare a mixture solution of $^ { 1 4 } \mathrm { N A }$ and $^ { 1 5 } \mathrm { N A }$ at 50 nM concentration each with Au NPs and dry the colloid on a cover glass under vacuum. A hyperspectral PESRS image of this mixture sample, consisting of

40,000 spectra, is acquired for statistical analysis. Figure 4b shows typical single-pixel spectra after denoising and background subtraction (Original corresponding single-pixel spectra can be found in Supplementary Fig. 10). Spectrum 1 has a single peak at $7 2 4 \mathrm { c m } ^ { - 1 }$ , matching the spectrum taken from the reference sample of isotopically pure $^ { 1 5 } \mathrm { N A }$ . Spectrum 3 has a single band at $7 3 3 \mathrm { \bar { c m } ^ { - 1 } }$ , corresponding to the PESRS spectrum of $^ { 1 4 } \mathrm { N A } .$ . Spectrum 2 exhibits a double band, The left band at 724 cm−1 can be attributed to $^ { 1 5 } \mathrm { N A } ,$ , and the right band at $7 3 3 \mathrm { c m } ^ { - 1 }$ can be attributed to 14NA. Notably, spectra with single peaks around 726 and 733 cm−1 were observed at multiple pixels (see Supplementary Fig. 11). These data allow the statistical analysis described below.

A multivariate curve resolution (MCR) method is used for statistical analysis of the PESRS spectra. The hyperspectral data (containing 40000 single-pixel spectra) is unmixed by MCR into concentration contributions of pure $\mathrm { ^ { 1 4 } N A \ ( C _ { 1 4 } ) }$ and pure $^ { 1 5 } \mathrm { N A }$ $\left( \mathsf { C } _ { 1 5 } \right)$ spectra (Fig. 4c) and a relative concentration ratio of $^ { 1 4 } \mathrm { N A }$ $\begin{array} { r } { \left( \frac { \mathrm { C } _ { 1 4 } } { \mathrm { C } _ { 1 4 } + \mathrm { C } _ { 1 5 } } \right) } \end{array}$ C defined as the fraction of the average number of $^ { 1 4 } \mathrm { N A }$ molecules contributing to the total signal, is thus determined. We select 796 of the total spectra acquired that display the desired Raman bands and have an intensity above a threshold value (maximum values > 0.03) for this statistical analysis. The threshold requirement helps to reduce inclusion of noise events and avoid the counting of artificial molecular events44. The histogram of relative contributions to the total signal produced by $^ { 1 4 } \mathrm { \check { N } A }$ is obtained by counting the selected events. As shown in Fig. 4d, the histogram of intensity ratios has the dominant contribution from the single-molecule events at the ratio ≈0 and ≈1. Based on the Le Ru’s statistical methodology44 and our simulation result (Supplementary Note 2), for histograms with distributions like that shown in Fig. 4d, the edges of the histogram (events for the ratio ≈0 $\mathrm { ~ \ o r ~ } \ \approx 1 )$ represent single-molecule events. The obtained statistical results match well the expected statistics prediction of single-molecule PESRS model data (Supplementary Fig. 12c). As a control experiment, we measure PESRS from 50 nM pure $^ { 1 4 } \mathrm { N A }$ and pure $^ { 1 5 } \mathrm { \dot { N } A }$ samples. The histograms of relative contributions of ${ } ^ { 1 4 } \mathrm { N A }$ of isotopic pure 14NA and pure $^ { 1 5 } \mathrm { N A }$ sample are dominated by events at ratio ≈1 (Supplementary Fig. 13b) and events at ratio ≈0 (Supplementary Fig. 13a), respectively. As a second control, we prepare a high-concentration ${ } ^ { 1 4 } \mathrm { N A }$ and $^ { 1 5 } \mathrm { N A }$ mixture (500 μM each). For this concentrated solution of the two isotopic molecules, mixed events dominated the histogram (Supplementary Fig. 14a). In the pure 15NA sample (Supplementary Fig. 14b), a significant portion of signals is assigned to pure $^ { 1 5 } \mathrm { N A }$ (ratio ≈0) and little to $^ { 1 4 } \mathrm { N A }$ . The same result is obtained for the pure $^ { 1 4 } \mathrm { N A }$ sample (Supplementary Fig. 14c). We further use the Fano-line shape function to fit the single pixel spectra of the 50 nM adenine sample. Our results (Supplementary Fig. 15) show that the dispersive line shapes of PESRS spectra slightly affect the Raman peak frequency. However, this slight frequency shift has no obvious impact on the molecular assignment between $^ { 1 4 } \mathrm { N A }$ and 15NA.

In addition to spectral segregation, we analyze the bandwidths of single molecule events (the ratio ≈0 or ≈1) versus the mix events (the ratio between 0.3 and 0.7) by fitting the $6 8 0 { - } 7 8 0 \mathrm { c m } ^ { - 1 }$ portion of each spectrum to a Fano-line shape fuction53. Supplementary Fig. 16 shows the bandwidth distributions of SM $^ { 1 4 } \mathrm { { N A } }$ events and SM $^ { 1 5 } \mathrm { N A }$ events are centered at ca. $1 0 \mathrm { c m } ^ { - 1 }$ , whereas the bandwidth distribution of mix events is centered at $1 4 \mathrm { c m } ^ { - 1 }$ . This bandwidth measurement further distinguishes the single-molecule events from the mixed molecules events.

To further evaluate the single-molecule sensitivity of PESRS, we study the PESRS signal in the temporal domain. Specifically, we record time-lapsed PESRS images from the same area of a $5 0 { \cdot } \mathrm { n M }$ adenine sample (Supplementary Movie 2). Figure 4e shows digital intensity fluctuations of adenine during the PESRS measurement at the same location. This blinking phenomenon is not observed at 1 mM of adenine (Supplementary Fig. 17). As another evidence, we observe single-step photobleaching at some pixels (Fig. 4f). On the contrary, stable intensity traces are collected from the 1 mM adenine sample (Supplementary Fig. 17).

The spectral blinking and single-step photodamage phenomena are considered as a characteristic behaviors of single or a few molecules1,2,34,35,54,55. Collectively these measurements in the spectral and temporal domains support that PESRS allows detection of single-molecule events for biomolecules having a cross-section as low as $1 0 ^ { - 3 0 } \mathrm { c m } ^ { 2 }$ .

PESRS mapping of adenine generated from bacteria. The investigation of dynamic living samples requires imaging at a high speed. Compared to SERS, the dramatically improved imaging speed of PESRS microscopy makes it a potentially useful tool for imaging the chemical dynamics of a complex living specimen. To demonstrate such capacity, we study the metabolic response of S. aureus to starvation, as shown in Fig. 5a. Following enrichment in a nutrient-rich environment, the S. aureus sample is washed and centrifuged in pure water. After 1 h, 1 μL of a bacterial suspension is placed on the Au NPs- ${ \mathrm { . } } \mathrm { S i O } _ { 2 }$ plasmonic substrate and once the water evaporated (\~5 min) the PESRS signal is acquired. A control sample is similarly prepared but in contrast a PESRS spectrum is obtained without a 1-h delay. PESRS spectra of S. aureus under starvation conditions for 1 h are displayed in Fig. 5b, and the observed spectra closely resemble the Raman spectrum of adenine. In contrast, the spectra of S. aureus obtained immediately (no waiting period) (Fig. 5b) do not exhibit an adenine-like Raman band. These results are consistent with the SERS data (Supplementary Fig. $1 8 ) ^ { 4 8 }$ . These data imply that adenine, a purine degradation product, is secreted from S. aureus as a response to the no-nutrient, water-only environment48. As shown previously48, these molecular species are secreted from the bacterial cells under starvation conditions and appear most heavily concentrated in the pericellular region near the outer cell wall. Figure 5c shows the PESRS image of starved S. aureus on the plasmonic substrate, which presents the distribution of the secreted adenine. The two representative single-pixel PESRS spectra of S. aureus are presented in Fig. 5d. These results collectively demonstrate that PESRS has the potential for the study of the bacterial exogenous metabolome.

We have noted that SERS is a powerful and easy-to-use method to obtain the single-spot chemical information with high sensitivity. However, point-by-point scanning SERS imaging remains a time-consuming measurement. In previous SERS experiment48, it took ca. 10 s to obtain a SERS spectrum of bacteria. Thus, for imaging a 30 μm × 30 μm area with 60 × 60 spectra, the total measurement time would be over 600 min, which is much longer than the time scale of metabolic change within the bacteria. Compared with SERS, our PESRS method provides a much faster chemical image. This capacity opens new opportunities for real-time imaging dynamic biological processes, as well as rapid scanning of large areas of tissue labeled by plasmonic Raman tags. Moreover, PESRS imaging can sample millions of pixels in a specimen within a short time, which avoids pixel-dependent fluctuations of signal intensity encountered in SERS spectroscopy and consequently allows quantitative chemical analysis.

## Discussion

Through plasmonic enhancement and hyperspectral recording, the detection sensitivity of SRS microscopy reaches the single molecule level. The Au plasmonic nanostructures provide an extraordinary SRS intensity enhancement relative to normal SRS of about $1 0 ^ { \acute { 7 } } .$ Such large enhancements allow the detection of single molecule with a Raman cross-section as low as $1 0 ^ { - 3 0 } \mathrm { c m } ^ { 2 } .$ Single-molecule PESRS detection of adenine molecules is verified by an isotope-edited bianalyte method and time-lapsed PESRS measurements. A potential biomedical application of PESRS is demonstrated through mapping of adenine released from stressed bacterial cells.

a  
![](images/af53fb21cbde8eb268cc4f05c501bde358bb00480850bdd2631a81cd3b917e7a.jpg)

<details>
<summary>text_image</summary>

ω_pump
ω_stokes
S.aureus
Au NPs
</details>

b  
![](images/ad936fdbce66384cf7ab3c0d250ac97a4d1bf44c39f5a7421ed97197e18fbc9a.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | 1 h-1 (0 h-1) | 1 h-2 (0 h-1) | 1 h-3 (0 h-1) | 1 h-1 (0 h-2) | 1 h-2 (0 h-2) | 1 h-3 (0 h-2) | 1 h-1 (0 h-3) | 1 h-2 (0 h-3) | 1 h-3 (0 h-3) |
| ------------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 600                | ~0.0000       | ~0.0000       | ~0.0000       | ~0.0000       | ~0.0000       | ~0.0000       | ~0.0000       | ~0.0000       | ~0.0000       |
| 700                | ~0.0002       | ~0.0002       | ~0.0002       | ~0.0002       | ~0.0002       | ~0.0002       | ~0.0002       | ~0.0002       | ~0.0002       |
| 800                | ~0.0001       | ~0.0001       | ~0.0001       | ~0.0001       | ~0.0001       | ~0.0001       | ~0.0001       | ~0.0001       | ~0.0001       |
</details>

c  
![](images/6848979c12042f631feeab803b1bbc20781780be397c99b3465fa11a44d0ae7e.jpg)

<details>
<summary>text_image</summary>

2
1
5 um
</details>

d  
![](images/ee0a535169ae059fc5d8fc6bf0f3cd3529957006fb841ed36cc44d7790e0b95e.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (arb. units) - 1 | Intensity (arb. units) - 2 |
| ------------------ | --------------------------- | --------------------------- |
| 550                | ~0.000                      | ~0.000                      |
| 600                | ~0.001                      | ~0.001                      |
| 650                | ~0.003                      | ~0.001                      |
| 700                | ~0.000                      | ~0.001                      |
| 750                | ~0.006                      | ~0.001                      |
| 800                | ~0.000                      | ~0.001                      |
| 850                | ~0.001                      | ~0.001                      |
</details>

Fig. 5 PESRS mapping of adenine generated from stressed bacteria. a A schematic of PESRS mapping of adenine generated from stressed bacteria. b The PESRS spectra of S. aureus washed and kept in water for 1 h. The PESRS spectra of S. aureus obtained immediately (0 h) after washing. Numbers 1, 2, 3 represent measurements at three locations on surface. No denoising applied. c Denoised PESRS image of starved S. aureus placed on the plasmonic substrate. The image area is 30 μm × 30 μm. d Single-pixel PESRS spectra of S. aureus on plasmonic substrate obtained from spot 1 and 2 indicated in panel c.

In this work, single-molecule detection sensitivity in PESRS is achieved through a combination of several strategies. First, we create and employ a nanostructured Au substrate with a plasmon resonance peak overlapping with our pump and Stokes laser wavelengths. Second, we use chirped pico-Joule laser pulses at 80 MHz repetition rate. Such pulse energy, which is 2 to 3 orders of magnitude lower than that in previous surface-enhanced femtosecond SRS works39,40, significantly decreased potential photodamage. The high repetition rate also allows high-speed data acquisition. Third, a PLS method is used to distinguish the Raman peak from the broad non-Raman background in the hyperspectral dataset. Finally, a BM4D approach denoises a hyperspectral cube and allows high-quality single-pixel spectra to be obtained for statistical analysis of single molecules events.

A portion of our recorded PESRS spectra shows a dispersive vibrational line shape (Fig. 1f, Supplementary Figs 6 and 11). Such line shape was reported in previous surface-enhanced femtosecond SRS works39,40,53. Three possible explanations have been proposed: Fano-resonance of the molecule-nanostructure system53, interference between the PESRS signal and the plasmon enhanced aggregated NP emission56, and the effects of the complex character of the plamonic field amplitude57. It is important to note that various dispersive line shapes in single pixel spectra (e.g., Supplementary Figs. 6 and 11) are observed. As previous surface-enhanced femtosecond SRS studies have shown, dispersive line shapes show a strong dependence on the relative position of excitation field with respect to the plasmon resonance58 and enhancement factor56. Our PESRS-active aggregations are composed of randomly clustered nanoparticles. Various line shapes in single pixel spectra illustrate the heterogeneity of localized surface plasmon resonance and local enhancement factor in different PESRS active sites. The distribution and character of PESRS line shapes will be further studied.

PESRS microscopy opens a new window for fast vibrational spectroscopic imaging of low-concentration molecules with high sensitivity. It should be noted that PESRS intensity is strongly dependent on the distance between the molecule and the surface. To achieve the highest sensitivity in PESRS measurements, it is necessary to keep target analytes on the surface with the highest enhancement. In this way, PESRS could sensitively detect the chemical components on a cell membrane or cell wall that is closely attached to the surface. Second, PESRS can detect metabolites secreted from a live cell in the pericellular region and investigate metabolic changes linked to the development of microbial populations or to exposure to antibiotics or other environmental changes. Third, combined with bio-conjugated target-specific plasmonic Raman nanoprobes, hyperspectral

PESRS imaging can be employed for rapid localization of multibiomarkers in large areas of tissues. In addition, PESRS imaging method can be extended to study the dynamic processes in surface chemistry, such as the mapping of the solid electrolyte interface membrane in a lithium cell or imaging the heterogeneity of catalyst.

Additional improvements may be envisioned for this technology. For example, the imaging speed can be further improved by using a multiplex SRS method26,27, advanced delay tuning approach22, or a wide-field SRS system. Secondly, harnessing the rational-designed reproducible plasmonic nanostructure fabricated by lithographic methods, our method can pave the way for reproducible and quantitative molecular imaging platform. Such improvements will invoke the integration of coherent Raman imaging techniques and novel nanostructure designs to open new avenues towards ultrasensitivity, ultra-fast, and label-free chemical imaging.

## Methods

## Hyperspectral plasmon-enhanced stimulated Raman scattering microscope.

Supplementary Fig. 1 presents the scheme of a hyperspectral SRS microscope. Briefly, an 80 MHz tunable femtosecond laser (InSight DS+, Spectra-Physics) provided the pump (680–1300 nm) and Stokes (1040 nm) stimulated fields. The Stokes beam is modulated by an acousto-optic modulator at 2.3 MHz. The pump and Stokes beams are spatially aligned and sent to an upright microscope with 2D galvo system for laser scanning. The spectral-focusing approach is used to obtain spectral domain information. In spectral focusing, the pump and Stokes pulses are equally stretched in time by 4 glass rods to achieve a constant instantaneous frequency difference that drives a single Raman coherence. By delaying the pump pulses, a series of Raman shifts (80 data points) are generated. At a certain delay, all the laser energy is spectrally focused to excite a narrow Raman band. The laser powers (pump \~0.15 mW and Stokes \~0.15 mW at the sample) are sufficiently low so that good stability of the molecule and nanostructure was maintained during the experiments. A ×60 water immersion objective (Olympus, NA = 1.2) or a ×40 water immersion objective (Olympus, NA = 0.8) is used to focus pump and Stokes laser on a sample. An oil condenser (Nikon, NA = 1.4) is used to collect the laser light in the forward direction. A 1000 nm shortpass filter (Thorlabs) blocks the Stokes laser before a photodiode with a lab-built resonant amplifier. A lock-in amplifier demodulates the stimulated Raman loss signal from the pump beam detected by the photodiode. Using an XY scanner with a 150 nm step to scan the sample, a PESRS hyperspectral data cube (200 × 200 pixels, 80 Raman channels) is recorded with a 10 μs dwell time per pixel. To obtain the PESRS spectrum of adenine, we scan the spectral range from ca. $5 5 0 \mathrm { c m ^ { - 1 } \mathrm { t } }$ o 850 cm−1 with 13.7 cm−1 spectral resolution. To clearly distinguish the small Raman shift between 14NA, 15NA and their mixture, two more rods were added in the combined light path to increase the chirp of pump and Stokes. In this way, about 7 cm−1 spectral resolution is achieved (as shown in Supplementary Fig. 9) with 120 spectral data points from 565 cm−1 to 850 cm−1. The PESRS imaging speed is ca. 1 to 2 min per data cube. The image size (30 × 30 µm) and pixel dwell time were the same in all experiments.

An epi-detected SRS microscope is built for PESRS detection on non transparent plasmon-enhanced substrates. Before the microscope, a quarter wave plate is placed after a polarizing beam splitter to change the polarization of excitation and back-reflected laser light by 90°. In this way, the polarizing beam splitter allows forward light to pass through and the stimulated Raman loss signals are reflected into a photodiode to achieve epi-PESRS imaging (Fig. 3a).

Background reduction in PESRS. A raw PESRS spectrum contains a large back ground signal from the photothermal effect, cross-phase modulation, and transient absorption. Cross-phase modulation originates from the optical Kerr effect, and the transient absorption and photothermal effect are due to the plasmonic resonance of the Au NPs. We minimized the background arising from non-Raman processes by using a larger numerical aperture (NA = 1.4) lens for signal collection to reduce cross-phase modulation and photothermal effect. Moreover, a megahertzfrequency modulation was used to further diminish the photothermal effect. With those approaches, we successfully observe a PESRS signal in the presence of a strong background.

Background subtraction in a PESRS spectrum. An adaptive iteratively reweighted penalized least squares (airPLS) algorithm (https://github.com zmzhang/airPLS), developed by Zhang et al.59, is employed to subtract the baseline from the raw PESRS spectrum.

Denoising of a PESRS hyperspectral data. Firstly, we use a BM4D V3.2 (http:// www.cs.tut.fi/\~foi/GCF-BM3D/index.html#ref\_software) denoising algorithm, developed by Maggioni and Foi50,51, to process the raw PESRS hyperspectral data cube. The BM4D algorithm relies on the so-called grouping and collaborative

filtering paradigm. A 3D imaging block (x–y–λ) is stacked into a 4D data array, which is then filtered. Thus, BM4D leverages the spatial and spectral correlation of a hyperspectral data cube both at the nonlocal and local level. Then, we use the airPLS algorithm to subtract the background of a hyperspectral data cube pixel by pixel. In addition, the image is plotted by the peak area of the desired Raman band.

Statistical analysis of single-molecule events. Before the statistical analysis of single-molecule events, the PESRS hyperspectral data is denoised and corrected baseline as described. A multivariate curve resolution (MCR) algorithm, developed by Tauler and Juan et al.60,61, is used to extract the concentration maps of the two isotopically related molecules in the mixed hyperspectral dataset. Because 14NA and 15NA have the same Raman cross-section, we use the normalized spectra separately obtained from pure 14NA and 15NA samples as the initial estimation of the pure spectra. The constraints implemented during the optimization step are non-negativity for the concentration and spectrum. The outputs of the MCR treatment are the pure concentration maps $( \mathbf { C } _ { 1 4 } , \mathbf { C } _ { 1 5 } )$ of $\mathrm { \cdot 1 4 } _ { \mathrm { N A } } ^ { \mathrm { \cdot } }$ and $^ { 1 5 } \mathrm { N A } .$ respectively. Then, the 796 spectra whose maximum values appeared at the desired wavenumber range are selected and an intensity threshold (maximum values >0.03) is defined for removal of noise events. The histogram of the relative con tribution of $\begin{array} { r } { ^ { 1 4 } \mathrm { N A } \left( \frac { \mathrm { C } _ { 1 4 } } { \mathrm { C } _ { 1 4 } + \mathrm { C } _ { 1 5 } } \right) } \end{array}$ is plotted and the edges of the histogram, the ratio ≈0 or ≈1, are considered as the single molecule events. Hyperspectral data unmixing was done by MCR GUI 2.0 (https://mcrals.wordpress.com/download/). All data were processed by MATLAB.

Substrate preparation. The Au NPs colloid is prepared according to the classical citrate reduction method62, resulting in particles with a diameter of \~50 to 60 nm, as shown in Supplementary Fig. 19. The 0.5 mL of 0.01% (g/mL) colloidal suspension is concentrated to 2–4 µL by centrifuging, which is then added to the 10 μL adenine solution. The adenine solution induces the aggregation of Au NPs. The aggregated Au NPs are dropped on a cover glass, followed by vacuum drying to obtain a substrate for PESRS detection.

Au NPs-SiO plasmonic substrates are prepared as described previously52. Immobilized clustered aggregates of 80 nm Au NPs are grown on a SiO chip. A 1 μL adenine solution was dropped on the Au NPs-SiO plasmonic substrates and samples are ready for PESRS measurement after adenine solution dried under air ambient (\~5 mins). High-purity water (Milli-Q, 18.2 MΩ·cm) is used throughout the study.

Bacteria sample preparation. Bacteria are harvested during the log phase. Culture growth media is removed from the bacterial samples by centrifugation, and washing four times with 2 mL of deionized Millipore water. The bacterial pellet is suspended in 0.25 mL of water, and 1 μL of the resulting bacterial suspension is dropped and dried onto the Au NPs-SiO plasmonic substrate. Samples are dried onto the Au substrate either immediately or after 1 h in order to demonstrate the effect of the starvation stress response.

Additional experimental results and data analysis are available in the supplementary information.

Reporting summary. Further information on research design is available in the Nature Research Reporting Summary linked to this article.

## Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.

Received: 18 February 2019; Accepted: 22 October 2019; Published online: 21 November 2019

## References

1. Nie, S. & Emory, S. R. Probing single molecules and single nanoparticles by surface-enhanced Raman scattering. Science 275, 1102–1106 (1997).  
2. Kneipp, K. et al. Single molecule detection using surface-enhanced Raman scattering (SERS). Phys. Rev. Lett. 78, 1667–1670 (1997).  
3. Zhang, W., Yeo, B. S., Schmid, T. & Zenobi, R. Single molecule tip-enhanced Raman spectroscopy with silver tips. J. Phys. Chem. C. 111, 1733–1738 (2007).  
4. Steidtner, J. & Pettinger, B. Tip-enhanced Raman spectroscopy and microscopy on single dye molecules with 15 nm resolution. Phys. Rev. Lett. 100, 236101 (2008).  
5. Zhang, R. et al. Chemical mapping of a single molecule by plasmon-enhanced Raman scattering. Nature 498, 8286 (2013).  
6. Le, Ru,E. C. & Etchegoin, P. G. Single-molecule surface-enhanced Raman spectroscopy. Annu. Rev. Phys. Chem. 63, 65–87 (2012).  
7. Zrimsek, A. B. et al. Single-molecule chemistry with surface-and tip-enhanced Raman spectroscopy. Chem. Rev. 117, 7583–7613 (2016).  
8. Ding, S.-Y. et al. Nanostructure-based plasmon-enhanced Raman spectroscopy for surface analysis of materials. Nat. Rev. Mater. 1, 16021 (2016).  
9. Willets, K. A. & Van Duyne, R. P. Localized surface plasmon resonance spectroscopy and sensing. Annu. Rev. Phys. Chem. 58, 267–297 (2007).  
10. Zong, C. et al. Surface-enhanced Raman spectroscopy for bioanalysis: reliability and challenges. Chem. Rev. 118, 4946–4980 (2018).  
11. Cheng, J.-X. & Xie, X. S. Vibrational spectroscopic imaging of living systems: an emerging platform for biology and medicine. Science 350, aaa8870 (2015).  
12. Cheng, J.-X. & Xie, X. S. Coherent anti-stokes Raman scattering microscopy: instrumentation, theory, and applications. J. Phys. Chem. B 108, 827–840 (2004).  
13. Evans, C. L. et al. Chemical imaging of tissue in vivo with video-rate coherent anti-Stokes Raman scattering microscopy. Proc. Natl Acad. Sci. USA 102, 16807–16812 (2005).  
14. Freudiger, C. W. et al. Label-free biomedical imaging with high sensitivity by stimulated Raman scattering microscopy. Science 322, 1857–1861 (2008).  
15. Saar, B. G. et al. Video-rate molecular imaging in vivo with stimulated Raman scattering. Science 330, 1368–1370 (2010).  
16. Evans, C. L. & Xie, X. S. Coherent anti-Stokes Raman scattering microscopy: chemical imaging for biology and medicine. Annu. Rev. Anal. Chem. 1, 883–909 (2008).  
17. Prince, R. C., Frontiera, R. R. & Potma, E. O. Stimulated Raman scattering: from bulk to nano. Chem. Rev. 117, 5070–5094 (2016).  
18. Camp, C. H. Jr et al. High-speed coherent Raman fingerprint imaging of biological tissues. Nat. Photonics 8, 627–634 (2014).  
19. Ozeki, Y. et al. High-speed molecular spectral imaging of tissue with stimulated Raman scattering. Nat. Photonics 6, 845–851 (2012).  
20. Wang, P. et al. Label-free quantitative imaging of cholesterol in intact tissues by hyperspectral stimulated raman scattering microscopy. Angew. Chem. Int. Ed. 52, 13042–13046 (2013).  
21. Fu, D., Holtom, G., Freudiger, C., Zhang, X. & Xie, X. S. Hyperspectral imaging with stimulated Raman scattering by chirped femtosecond lasers. J. Phys. Chem. B 117, 4634–4640 (2013).  
22. Liao, C.-S. et al. Stimulated Raman spectroscopic imaging by microsecond delay-line tuning. Optica 3, 1377–1380 (2016).  
23. Liao, C.-S. et al. Spectrometer-free vibrational imaging by retrieving stimulated Raman signal from highly scattered photons. Sci. Adv. 1, e1500738 (2015).  
24. Li, J. et al. Lipid desaturation is a metabolic marker and therapeutic target of ovarian cancer stem cells. Cell. Stem. Cell. 20, 303–314. e305 (2017).  
25. Fu, D. et al. Imaging the intracellular distribution of tyrosine kinase inhibitors in living cells with quantitative hyperspectral stimulated Raman scattering. Nat. Chem. 6, 614–622 (2014).  
26. Liao, C.-S. et al. Microsecond scale vibrational spectroscopic imaging by multiplex stimulated Raman scattering microscopy. Light Sci. Appl. 4, e265 (2015).  
27. Zhang, C. et al. Stimulated Raman scattering flow cytometry for label-free single-particle analysis. Optica 4, 103–109 (2017).  
28. Zhang, C. & Cheng, J.-X. Perspective: coherent Raman scattering microscopy, the future is bright. APL Photonics 3, 090901 (2018).  
29. Wei, L. et al. Super-multiplex vibrational imaging. Nature 544, 465 (2017)  
30. Wei, L. & Min, W. Electronic preresonance stimulated raman scattering microscopy. J. Phys. Chem. Lett. 9, 4294–4301 (2018).  
31. Liang, E., Weippert, A., Funk, J.-M., Materny, A. & Kiefer, W. Experimenta observation of surface-enhanced coherent anti-Stokes Raman scattering. Chem. Phys. Lett. 227, 115–120 (1994).  
32. Koo, T.-W., Chan, S. & Berlin, A. A. Single-molecule detection of biomolecules by surface-enhanced coherent anti-Stokes Raman scattering. Opt. Lett. 30, 1024–1026 (2005).  
33. Steuwe, C., Kaminski, C. F., Baumberg, J. J. & Mahajan, S. Surface enhanced coherent anti-Stokes Raman scattering on nanostructured gold surfaces. Nano. Lett. 11, 5339–5343 (2011).  
34. Zhang, Y. et al. Coherent anti-Stokes Raman scattering with single-molecule sensitivity using a plasmonic Fano resonance. Nat. Commun. 5, 4424 (2014).  
35. Yampolsky, S. et al. Seeing a single molecule vibrate through time-resolved coherent anti-Stokes Raman scattering. Nat. Photonics 8, 650–656 (2014).  
36. Voronine, D. V. et al. Time-resolved surface-enhanced coherent sensing of nanoscale molecular complexes. Sci. Rep. 2, 891 (2012).  
37. Ichimura, T., Hayazawa, N., Hashimoto, M., Inouye, Y. & Kawata, S. Tip enhanced coherent anti-Stokes Raman scattering for vibrational nanoimaging. Phys. Rev. Lett. 92, 220801 (2004).  
38. Cheng, J.-X. & Xie, X.S. Coherent Raman Scattering Microscopy (CRC press, Boca Raton. 2016).  
39. Frontiera, R. R., Henry, A.-I., Gruenke, N. L. & Van Duyne, R. P. Surfaceenhanced femtosecond stimulated Raman spectroscopy. J. Phys. Chem. Lett. 2, 1199–1203 (2011).  
40. Buchanan, L. E. et al. Surface-enhanced femtosecond stimulated raman spectroscopy at 1 mhz repetition rates. J. Phys. Chem. Lett. 7, 4629–4634 (2016).  
41. Gruenke, N. L. et al. Ultrafast and nonlinear surface-enhanced Raman spectroscopy. Chem. Soc. Rev. 45, 2263–2290 (2016).  
42. Zhang, D., Slipchenko, M. N., Leaird, D. E., Weiner, A. M. & Cheng, J.-X. Spectrally modulated stimulated Raman scattering imaging with an angle-to wavelength pulse shaper. Opt. Express 21, 13864–13874 (2013).  
43. Le, Ru,E. C., Meyer, M. & Etchegoin, P. G. Proof of single-molecule sensitivity in surface enhanced Raman scattering (SERS) by means of a two-analyte technique. J. Phys. Chem. B 110, 1944–1948 (2006).  
44. Etchegoin, P. G., Meyer, M., Blackie, E. & Le, Ru,E. C. Statistics of singlemolecule surface enhanced Raman scattering signals: Fluctuation analysis with multiple analyte techniques. Anal. Chem. 79, 8411–8415 (2007).  
45. Dieringer, J. A., Lettan, R. B., Scheidt, K. A. & Van Duyne, R. P. A frequency domain existence proof of single-molecule surface-enhanced Raman spectroscopy. J. Am. Chem. Soc. 129, 16249–16256 (2007).  
46. Chen, C. et al. High spatial resolution nanoslit SERS for single-molecule nucleobase sensing. Nat. Commun. 9, 1733 (2018).  
47. Blackie, E. J., Le, Ru,E. C. & Etchegoin, P. G. Single-molecule surfaceenhanced Raman spectroscopy of nonresonant molecules. J. Am. Chem. Soc 131, 14466–14472 (2009).  
48. Premasiri, W. R. et al. The biochemical origins of the surface-enhanced Raman spectra of bacteria: a metabolomics profiling by SERS. Anal. Bioanal. Chem. 408, 4631–4647 (2016).  
49. Chen, Y., Premasiri, W. & Ziegler, L. Surface enhanced Raman spectroscopy of Chlamydia trachomatis and Neisseria gonorrhoeae for diagnostics, and extracellular metabolomics and biochemical monitoring. Sci. Rep. 8, 5163 (2018).  
50. Dabov, K., Foi, A., Katkovnik, V. & Egiazarian, K. Image denoising by sparse 3-D transform-domain collaborative filtering. IEEE Trans. Image Process. 16, 2080–2095 (2007).  
51. Maggioni, M., Boracchi, G., Foi, A. & Egiazarian, K. Video denoising, deblocking, and enhancement through separable 4-D nonlocal spatiotemporal transforms. IEEE Trans. Image Process. 21, 3952–3966 (2012).  
52. Premasiri, W. et al. Characterization of the surface enhanced Raman scattering (SERS) of bacteria. J. Phys. Chem. B 109, 312–320 (2005).  
53. Frontiera, R. R., Gruenke, N. L. & Van Duyne, R. P. Fano-like resonances arising from long-lived molecule-plasmon interactions in colloidal nanoantennas. Nano. Lett. 12, 5989–5994 (2012).  
54. Lim, D.-K., Jeon, K.-S., Kim, H. M., Nam, J.-M. & Suh, Y. D. Nanogapengineerable Raman-active nanodumbbells for single-molecule detection. Nat. Mater. 9, 60–67 (2010).  
55. Lombardi, J. R., Birke, R. L. & Haran, G. Single molecule SERS spectral blinking and vibronic coupling. J. Phys. Chem. C. 115, 4540–4545 (2011).  
56. Mandal, A., Erramilli, S. & Ziegler, L. Origin of dispersive line shapes in plasmonically enhanced femtosecond stimulated Raman spectra. J. Phys. Chem. C. 120, 20998–21006 (2016).  
57. McAnally, M. O., McMahon, J. M., Van Duyne, R. P. & Schatz, G. C. Coupled wave equations theory of surface-enhanced femtosecond stimulated Raman scattering. J. Chem. Phys. 145, 094106 (2016).  
58. Buchanan, L. E., McAnally, M. O., Gruenke, N. L., Schatz, G. C. & Van Duyne, R. P. Studying stimulated raman activity in surface-enhanced femtosecond stimulated raman spectroscopy by varying the excitation wavelength. J. Phys. Chem. Lett. 8, 3328–3333 (2017).  
59. Zhang, Z.-M., Chen, S. & Liang, Y.-Z. Baseline correction using adaptive iteratively reweighted penalized least squares. Analyst 135, 1138–1146 (2010).  
60. Jaumot, J., de Juan, A. & Tauler, R. MCR-ALS GUI 2.0: new features and applications. Chemom. Intell. Lab. Syst. 140, 1–12 (2015).  
61. Felten, J. et al. Vibrational spectroscopic image analysis of biological material using multivariate curve resolution–alternating least squares (MCR-ALS). Nat. Protoc. 10, 217–240 (2015).  
62. Frens, G. Controlled nucleation for the regulation of the particle size in monodisperse gold suspensions. Nat. Phys. Sci. 241, 20–22 (1973).

## Acknowledgements

This work was supported by NIH grants GM1 18471, AI141439, and a Keck Foundation grant to J.X.C., Xiamen University postdoctoral fellowship to C.Zo. supported by NSFC (2163000117, 21621091, and 21790354), and MOST (2016YFA0200601) grants to B.R. L.D.Z. acknowledges the support of NSF (CHE-1609952). We thank Jiayingzi Wu for assistance with UV-Vis detection, and Kai-Chih Huang, Fengyuan Deng, and Peng Lin for their valuable suggestion that greatly improved the experimental performance.

## Author contributions

Experiments were designed by J.X.C, C.Zo., and L.D.Z. The PESRS experiments were con ducted by C.Zo. Data analysis was executed by C.Zo. with the help of H.N.L. P.R. prepared the Au NPs-SiO2 substrate and the bacteria sample. Y.M.H. performed the SEM study and UV. Vis detection. H.N.L., C.Zh., and C.Zo. developed the hyperspectral SRS instruments. C.Zo. wrote the paper, revised by J.X.C., C.Y., B.R., and L.D.Z. All authors commented on the paper.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41467- 019-13230-1.

Correspondence and requests for materials should be addressed to J.-X.C.

Peer review information Nature Communications thanks the anonymous reviewer(s) for their contribution to the peer review of this work, Peer reviewer reports are available

Reprints and permission information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/813cae11eb7c0185e51ebca9a64692de53f10c7b19986719b2ba337022edde7d.jpg)

Open Access This article is licensed under a Creative Commons Attri bution 4.0 International License, which permits use, sharing, adaptation,

distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s)2019