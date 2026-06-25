## C H E M I C A L P H YS I C S

# Ultrasensitive infrared spectroscopy via vibrational modulation of plasmonic scattering from a nanocavity

Danchen Jia1 , Ran Cheng2 , James H. McNeely2 , Haonan Zong1 , Xinyan Teng2 , Xinxin Xu3 , Ji-Xin Cheng1,2,3,4,5 \*

Most molecules and dielectric materials have characteristic bond vibrations or phonon modes in the mid-infrared regime. However, infrared absorption spectroscopy lacks the sensitivity for detecting trace analytes due to the low quantum efficiency of infrared sensors. Here, we report mid-infrared photothermal plasmonic scattering (MIP-PS) spectroscopy to push the infrared detection limit toward nearly a hundred molecules in a plasmonic nanocavity. The plasmon scattering from a nanoparticle-on-film cavity has extremely high sensitivity to the spacing defined by the analyte molecules inside the nanogap. Meanwhile, a 1000-fold infrared light intensity enhancement at the bond vibration frequency further boosts the interaction between mid-IR photons and analyte molecules. MIP-PS spectroscopic detection of nitrile or nitro group in \~130 molecules was demonstrated. This method heralds potential in ultrasensitive bond-selective biosensing and bioimaging.

Copyright © 2024 The

Authors, some rights

reserved; exclusive

licensee American

Association for the

Advancement of

Science. No claim to

original U.S.

Government Works.

Distributed under a

Creative Commons

Attribution

NonCommercial

License 4.0 (CC BY-­NC ).

## INTRODUCTION

Mid-infrared (MIR) spectroscopy has emerged as a prominent tech nology for the exploration of chemical bond vibrations in biology, organic chemistry, and phonon vibrations in material science (1–3). Contemporary Fourier transform infrared (FTIR) detection methods, based on mercury cadmium telluride detectors, have enabled infrared (IR) spectroscopy at millimolar levels. Nevertheless, its detection sensitivity is inherently limited by several factors, including the weak interaction between IR photons and chemical bond vibrations, as well as the relatively low quantum efficiency of detectors in the MIR spectral region. Notably, the MIR absorption cross section of a single bond is on the order of 10−20 to 10−16 cm2 (4), limiting the accurate detection of analytes at low concentrations. Therefore, FTIR is primarily suitable for the analysis of substantial sample vol umes, with the detection speed limited to a few seconds to minutes per spectrum due to the scanning speed of the interferometer.

In the pursuit of high detection efficiency, a range of indirect sensing technologies has been developed. Mid-IR photothermal (MIP) microscopy, also called optical photothermal IR microscopy, harnesses a visible probe beam to exploit the thermal effect resulting from the IR absorption of analytes. This innovative approach refines spatial resolution to the visible diffraction limit (5–9), facilitating video-rate chemical imaging at subcellular scales (10). MIP imaging has unveiled insights into intracellular protein aggregation, lipid dynamics, and glucose metabolism (11–13). However, the MIP sensitivity remains constrained by the three-order size mismatch between the MIR focusing spot and the characteristic length of a chemical bond.

Atomic force microscopy–based IR (AFM-IR) spectroscopy uses a near-field scanning tip to probe the thermal expansion induced by IR absorption of analytes, which transcends the optical diffraction limit and much improves the detection sensitivity of MIR spectroscopy for molecular monolayers and single proteins (14–16). To achieve more precise and quantitative results without scratching the samples, researchers have developed a peak force IR imaging technique, which is compatible with tapping-mode AFM (17). With these advances, it is crucial to acknowledge that the imaging depth achievable with AFM-IR techniques is inherently confined within the near-field region defined by the AFM tips, which is limited to tens of nanometers from the surface of the material.

Besides innovating sensing methods with high figures of merit, amplifying the interaction between IR photons and chemical bonds represents an alternative avenue for improving detection limits. Surface-enhanced IR absorption (SEIRA) method exploits the strong electromagnetic field confinement enabled by the resonance between incident IR light and electron waves at the metal-dielectric interface. This method provides a substantial enhancement of the IR field, often on the order of 104 at localized hot spots (18). An electrically tunable nanoribbon array further augments the potential of SEIRA by manipulating the IR resonant frequencies to encompass a wider spectral window for comprehensive spectroscopic analysis (19). Starting from the sensing mechanism of SEIRA, the extension to metasurface with periodic noble metal nanoantenna with extreme near-field enhancements and engineered multi-resonant spectra have grown in versatile designs and broad potential as lab-on-chip sensors (20, 21). The versatility of SEIRA enabled by tailoring diverse nano-geometries has proven its wide potential in life science and chemical analysis (22).

Complementing the plasmonic enhancement route, the utilization of optical cavities is another approach to boost the IR absorption of analytes. This is accomplished by prolonging the interaction duration between light and matter within an optical cavity, such as whispering gallery mode (WGM) within microfibers or waveguides (23). WGM-based sensors have enabled label-free biosensing down to single molecules. Nevertheless, the bandwidth of these WGMbased sensors remains limited by the wavelength-scale dimensions of the cavity, resulting in a constrained spectral range for analysis.

Upconversion-based techniques further break the detection limit of MIR spectroscopy through converting MIR measurements into detection in the visible regime, operating in both the far-field and near-field manners. Facilitated by the strong pulse energy of ultrafast laser pulses, these methods achieve remarkable upconversion efficiency from MIR to fluorescence, and MIR spectroscopic information

1 Department of Electrical and Computer Engineering, Boston University, Boston, MA 02215, USA. 2 Department of Chemistry, Boston University, Boston, MA 02215, USA. 3 Department of Material Science and Engineering, Boston University, Boston, MA 02215, USA. 4 Photonics Center, Boston University, Boston, MA 02215, USA. 5 Department of Biomedical Engineering, Boston University, Boston, MA 02215, USA. \*Corresponding author. Email: jxcheng@bu.edu

becomes readily detectable by visible photon detectors (24–26). This method offers an unprecedented sensitivity for sensing and imaging of fluorescent dyes down to single-molecule level. Notably, the upconversion-based MIR detection extends beyond ultrafast lasers aided by plasmonic nanocavities. Plasmonic nanocavities harness the strong local field confinement to increase the energy density and thus the upconversion efficiency. By tailoring nanocavity with dual resonant frequencies to align with both visible and MIR region, the upconversion efficiency from IR to visible light through surfaceenhanced Raman scattering is magnified by $1 0 ^ { \dag 0 } .$ . This strategy enables MIR detection of few target molecules within the plasmonic nanogaps using continuous-wave (CW) pump lasers (27, 28). Subsequently, benefitting from the geometric design of plasmonic nanostructures, single-molecule IR spectroscopy has been achieved through upconversion from IR to fluorescence, even with CW pump sources (29). Notably, these techniques constrain the analytes to be IR-active fluorescent molecules or nonfluorescent molecules with both IR and Raman activity, limiting the IR detection to specific species. Consequently, the scope of detection remains confined to specific energy bands. Benefitting from the field enhancement of nanocavities, surface-enhanced Raman scattering signals perturbed by MIR absorption have enabled IR spectroscopy of phonons in substrates, which helps to the understanding of plasmonic nano-design for ultrasensitive IR analysis (30).

Here, we report MIP plasmonic scattering (MIP-PS) spectroscopy with ultrahigh sensitivity to detect a trace amount of small molecules, facilitated by the strong interaction between the plasmons in the nanocavity and the vibrations of the analytes inside the nanogap. The vibration of chemical bonds interacts with nanocavityenhanced IR field, leading to increased MIR absorption of detected molecules by thousand folds. Meanwhile, the visible plasmons interact with amplified molecular vibrations, and, thus, the scattering spectrum of the nanostructure is altered by the MIR absorption of the molecules in the nanogap. Benefitting from the extreme sensitivity of the plasmonic scattering spectra to the bond-regulated spacing of the nanogap, MIP-PS identifies chemical bond information through MIR-encoded plasmonic scattering of nanocavities. Detailed results are shown below.

## RESULTS

## MIP-PS principle

To overcome the dimensional mismatch between the focusing area of the MIR beam and the size of the chemical bonds (Fig. 1A), a plasmonic nanocavity is introduced to bridge the gap. Here, the plasmonic nanocavity sensor is composed of a smooth Au nanofilm, an Au nanoparticle, and the analyte molecules formed by a selfassembled monolayer (SAM) inside the nanogap between them (Fig. 1A). The MIP-PS sensor takes advantage of the extremely sensitive dependence of the plasmonic scattering from a nanoparticle on-film (NPoF) cavity on the separation between the nanoparticle and the nanofilm. According to rotational-vibrational coupling theorem, bond length changes as molecule vibrates; at higher vibrational states, the rotational constant $\widetilde { B }$ of a molecule decreases, its momentum of inertia increases, and, thus, its bond length increases, according to $\begin{array} { r } { l = \sqrt { \frac { h } { 8 \pi ^ { 2 } c \widetilde { B } \mu } } } \end{array}$ (31). Here, $\mu$ is the reduced mass of the chemical bond, and l is the bond length. Meanwhile, IR absorption of molecules results in a photothermal expansion $( \Delta l = l _ { \mathrm { o } } \alpha _ { \mathrm { t h } } \bar { \Delta } T )$ , which also modulates the spacing distance of the nanogap. Here, $l _ { \mathrm { o } }$ is the initial molecule length, $\alpha _ { \mathrm { t h } }$ is the thermal expansion coefficient, and ΔT is the change of temperature. As the analyte molecules are thiol–self-assembled on the Au nanofilm and its functional groups contact with the Au nanoparticle, the spacing of the NPoF cavity, thus the plasmonic scattering, is regulated by the varied size of the molecules at certain vibrational mode (Fig. 1B).

A  
![](images/e972131e462d5af1979436e29c169995bf857f9af5508a574cc9ecd5e5cc1c56.jpg)

<details>
<summary>text_image</summary>

<1 nm
nm
50 nm
μm
>1 μm
</details>

B  
![](images/c07c378b1502095751eeef1948c7c22de0d1ee7898add0690339ca7015d82285.jpg)

<details>
<summary>line chart</summary>

| Bond displacement | Bond vibration energy |
| ----------------- | --------------------- |
| 0                 | High                  |
| Mid-IR transition | Low                   |
| Non-radiative decay | Low                   |
</details>

c  
![](images/563dc8985dbdb39db6d8482784f1448210df21d0e3cc843eafda99451258a3bd.jpg)

<details>
<summary>line chart</summary>

| Wavelength (um) | E²/E₀²     |
| --------------- | ---------- |
| 0.5             | ~10⁴       |
| 0.6             | ~10⁵       |
| 0.7             | ~10⁴       |
| 0.8             | ~10⁵       |
| 0.9             | ~10⁴       |
| 1.0             | ~10³       |
| 2.0             | ~10³       |
| 3.0             | ~10³       |
| 4.0             | ~10³       |
| 5.0             | ~10³       |
</details>

D  
![](images/66c2753a4b24e3a8f4d26a2a67219afee25a4b2e2b247c26b46279e263463c0f.jpg)

<details>
<summary>heatmap</summary>

| λ (nm) | E_z (×10 nm) Range | Color Scale |
|--------|---------------------|-------------|
| 638    | 0.0                 | ~0.8        |
| 638    | 1.5                 | ~0.8        |
</details>

Fig. 1. Principle of a MIP-PS sensor. (A) Size mismatch between molecules (<1 nm) and focal area of mid-­IR beam (>1 μm) leads to weak interaction of the bond vibration and the mid-­IR field. A plasmonic nanocavity with high effective index of refraction confines the IR field and molecules. The nanocavity has extreme sensitivity dependent on the spacing between the nanoparticle and the nanofilm. (B) Photothermal expansion induced by IR absorption of chemical bonds at vibrational excited states with respect to ground states modifies the far-field scattering distribution of the plasmonic nanocavity. (C) Simulated light intensity enhancement factor at the hot spot of the nanosphere-on-film (NSoF) cavity indicates an enhancement of $1 0 ^ { 3 }$ excited in mid-­IR regime. Inset: Near-field distribution of the nanocavity (diameter of the Au nanosphere, 50 nm; thickness of the Au nanofilm, 15 nm; spacer thickness, 1 nm) excited at the wavelength of 4.6 μm. (D) Simulated near-field of the NSoF cavity excited at the probe wavelength of 638 nm with the spacer thickness of 1.0 nm (left) and 1.5 nm (right).

The nanosphere-on-film (NSoF) cavities display two characteristic plasmonic bright modes in visible and near-IR regime as shown in the simulation results in Fig. 1C (32–34). These two plasmonic bright modes locate at around 580 and 810 nm dependent on the spacing distance, the size of the Au nanosphere, and the thickness of the Au nanofilm. Here, the NSoF cavity is composed of an Au nanosphere with the diameter of 50 nm and an Au nanoplate with the thickness of 24 nm separated by a thiol–self-assembled layer of small molecules. The 580-nm peak represents the transverse dipole mode of the Au nanosphere (fig. S1). The 810-nm peak represents the vertical antenna mode resulted from the coupling between the Au nanosphere and the surface plasmon polariton (SPP) modes of the Au nanoplate covering the visible and near-IR regime. Thus, the localized dipole mode of the nanosphere both radiates to far field and couples to the SPP modes of the nanofilm. When the Au nanosphere touches the Au mirror, its horizontal dipole modes vanish because of the opposite polarization of the nanosphere and the mirror mode. As the spacing distance between the nanoparticle and the nanofilm increases, the horizontal dipole modes recover and couple less to the SPP modes of the Au film. When the spacing distance increases, more photons radiate into far field and less coupled to SPP modes, which results in the blueshifting of the scattering peak of the transverse mode. Because the scattering spectra of the NPoF cavity is very sensitive to the spacing between the nanoparticle and nanofilm (35), molecular vibration in the nanogap can be detected through the scattering intensity change of NPoF cavities at certain visible prove wavelength.

Owing to the coupled resonance between the nanosphere and the nanoplate, the electric field is highly confined within the nanogap and thus results in an intensity enhancement of $1 0 ^ { 4 }$ to ${ 1 0 } ^ { 5 }$ in the visible regime (Fig. 1C). Meanwhile, in the mid-IR spectral window of interest, there is still an IR enhancement of $1 0 ^ { \hat { 3 } }$ even if the frequency is away from the plasmonic resonant frequency (Fig. 1C). This field enhancement provided by the nanocavity can boost the interaction of IR photons with the targeted chemical bond vibrations. With the chemical bonds pumped to vibrational excited states with mid-IR plasmons, the nanocavity is then characterized with another probe laser in the visible range. We select the probe wavelength as 638 nm for NSoF cavities where the first derivative of the scattering cross section reaches the local maximum. From the near field distribution of the nanocavity at 638 nm, the localized surface plasmon resonance (LSPR) of Au nanoparticle couples more into SPP modes of Au nanofilm and thus radiates less into far field with thinner spacing (Fig. 1D). Here, near-field mappings of NSoF with the spacing distance of 1.0 and 1.5 nm are illustrated to differentiate the cavity-mode change. In results, we can sense the IR absorption by detecting the scattering intensity change of the NPoF cavities.

## Experimental results

To experimentally demonstrate the high sensitivity of MIP-PS spectroscopy, we prepared SAMs of 4-mercaptomethylbenzonitrile (4- MBN) and 4-nitrobenzenethiol (4-NBT) molecules inside the Au NSoF cavities. The detailed sample preparation and characterization procedures are described in Materials and Methods. The analyte molecules were uniformly distributed on the Au surface in a monolayered manner where thiol group was chemically bound to Au atoms (Fig. 1A and fig. S2). The Au nanoparticles were drop-casted on the SAMs, and the spacing distance of the nanocavity is \~0.686 nm estimated from density functional theory (DFT) simulations below. The NSoF cavities were then characterized with dark-field scattering spectra (fig. S3 and Materials and Methods), where the scattering peak position at 590 nm. The number of analyte molecules inside a NSoF cavity was estimated from the effective area of the confined mid-IR field in the nanogap (fig. S4) and the surface density of molecular monolayers. For molecular surface density, we adopt an estimation of the topological polar surface area, computed as the surface sum over polar atoms in the molecule (36). Following the detailed calculation steps in the Supplementary Materials, the effective molecular number of individual cavities is 218 and 132 for 4-MBN and 4-NBT, respectively.

The MIP-PS system is a pump-probe system in counter-propagation mode (Fig. 2A). To efficiently excite all modes of the NPoF structure and collect the backscattered photons, we built a dark-field microscope in the reflection mode as the probe beam path with an illumination angle of 68°. The pump mid-IR pulses are generated from a quantum cascade laser (QCL) and synchronized with the probe pulses through a pulse generator. The MIP-PS signal was extracted from the subtraction of adjacent IR-on frames and IR-off frames (Fig. 2B), and the MIP-PS spectra were collected by scanning the wavelengths of the pump laser across the spectral window of interest. A detailed explanation of the setup can be found in Materials and Methods, and synchronization for time-resolved measurements was shown in Fig. 2C.

With the oblique plane-wave incidence at the wavelength of 638 nm, the hexagonal nanoplate with the thickness of 20 nm showed up in the dark-field scattering images (Fig. 3A). The Au nanofilms were prepared by controlled growth of high–aspect ratio single-crystalline gold platelets (Materials and Methods), where ultrasmooth Au surface was maintained within the hexagonal shape in Fig. 3A. The dark-field scattering distribution of the NSoF structure showed “Donut” shape, because the opposite polarization of the transverse dipole mode of the nanosphere and its mirror mode leads to destructive interactions in the far field. When mid-IR pulses with the wave number of $2 2 0 0 ~ \mathrm { { c m } ^ { - 1 } }$ , which matches the resonant frequency of the nitrile stretching mode of 4-MBN molecules, were pumped from the bottom of the plasmonic nanocavity, the bond vibration was excited with the localized mid-IR field enhanced by the nanocavity and resulted in the modification of the plasmonic scattering photon distribution of the NSoF structure. As a result, by taking subtraction of the dark-field scattering images at IR-on states and IR-off states (Fig. 3B), the modulated scattering intensity induced by the mid-IR absorption of certain chemical bonds can be quantified. As compared in Fig. 3B, the MIP-PS image of 4-MBN at 2200 cm−1 (on-resonance state) showed modified scattering intensity of the nanostructure, while the one at $2 2 4 0 \mathrm { c m } ^ { - 1 }$ (off-resonance state) had no contrast. Subsequently, we can analyze the MIP-PS spectra by tuning the wavelength of the mid-IR pump beam and integrating the corresponding modification of scattering intensity of the NSoF cavities. The MIP-PS spectra of 4-MBN molecules showed a peak at $2 2 0 0 \mathrm { c m } ^ { - 1 }$ in Fig. 3C and figs. S5 and S6. The spectra were collected from 10 nanocavities. As a reference, the FTIR peak of 4-MBN molecules locates at 2230 cm−1 measured with attenuated total reflec tance (ATR; fig. S7). This effect arises from the interaction between the gold surface and the molecular dipole that can modify the vibrational frequencies of chemical bonds, especially in molecules with polar functional groups (37). Here, the nitrile group, with its strong dipole moment, is particularly sensitive to metal surface effects in MIP-PS spectroscopy.

![](images/2b607eb6463c9f49533ba6a58104892a9b8e111cfea11de0e7d4fce27943f369.jpg)

<details>
<summary>text_image</summary>

A
Probe
Modulation of scattered photons
IR-on IR-off
Camera
Mid-IR pump
Pump
B
IR-on
IR-off
Near-field
Δt
Far-field
ΔI
c
Time-resolved measurement
140 fs 80 MHz
Time delay
52 ns
</details>

Fig. 2. MIP-PS system. (A) The MIP-PS measurement is performed on an IR-pump visible-probe dark-field microscope. The probe beam from a 638-nm laser is expanded by a 4-f system and passes through a central aperture to form ring-shaped illumination. The probe beam excites the NPoF cavity through a dark-field objective on top. The mid-­IR pulses loosely focused by a parabolic mirror at bottom pump the analyte molecules inside the nanocavity. The modified visible backscattered photons are collected by the dark-field objective to a camera. Inset: Synchronization of the mid-­IR pump and visible probe pulses. (B) Schematic of near-field (top) and far-field (bottom) distribution of the modified NPoF cavity by the mid-­IR absorption of the SAM of molecules. (C) Synchronization of the time-resolved MIP-PS measurements. The probe laser is a femtosecond laser chopped by an acoustic-optical modulator to 52-ns pulses. The time decay constant of the MIP-PS measurements of molecules is determined by tuning the delay time between synchronized pump and probe pulses.

To further confirm the spectral fidelity, we analyzed the MIP-PS spectra of 4-NBT from 10 nanocavities, as shown in Fig. 3D and fig. S5. The 4-NBT molecules were self-assembled on the Au nanoplate via thiol groups and the nitro groups contact the Au nanosphere on top. The MIP-PS peak of 4-NBT located at 1330 cm−1 , corresponding to the asymmetric stretching mode of nitro group. The MIP-PS signals exhibited a positive linear relationship with IR pulse width (fig. S7), consistent with the increased photothermal effect resulting from higher IR pulse energy. The peak position is also in agreement with the FTIR spectra in fig. S8. The variations of the MIP-PS signal from different nanocavities were attributed to the variations of the geometric parameters of the Au nanoparticles (i.e., the diameters, facets, and surface roughness of the nanospheres) and the surface quality of the nanoplate.

To further study the mechanism of the MIP-PS signals, we performed time-resolved MIP-PS measurements by manipulating the time delay between the visible probe pulses and the mid-IR pump pulses. To ensure high temporal resolution, we substituted the nanosecond probe laser with a femtosecond laser (Coherent Chameleon Ultra, Ti:Sapphire, pulse with of 140 fs, 80 MHz). The femtosecond probe pulses were chopped to 52 ns as pulse duration at a repetition rate of 100 kHz by acoustic-optical modulator (Fig. 2C). The averaged probe power was measured to be 1.0 mW, which resulted in a power density of 10 $\mu \mathrm { W } / \mu \mathrm { m } ^ { 2 } .$ . To match the excitation wavelength of 800 nm, we selected nanorod-on-film (NRoF) structure, where Au nanorod with the average length of 103 nm and the average diameter of 24 nm were dispersed on Au film for time-resolved measurements, which corresponds to the vertical antenna mode. When scanning the time delay between the pump pulses and the delay pulses controlled by a pulse generator, the decay curve of the relaxation of the IR absorption–induced plasmon scattering change was plotted in Fig. 3E. By fitting the time decay curve with a convolution function detailed in Materials and Methods, the decay constant of the MIP-PS signals was determined to be 65 ns, while the instrumental response time was fitted at 51 ns. The coefficient of determination (R2 ) value for this fit is 0.92. This nanosecond-scale signal relaxation time agrees with the photothermal contrast mechanism, because the vibrational decay time based on bond-length theory is no more than 100 ps. Therefore, this measurement suggests that photothermal effect plays a major role in the MIP-PS signals.

A  
![](images/ddf70a2e806606e78b8bbd0696d7a8c7dd0729db10df67a2db24b1940368e916.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a cellular or molecular structure with highlighted regions and a yellow circular marker (no text or symbols)
</details>

B

![](images/c67657ca99d16bd890cf93c7631d81e4e5ba9871b780ea25ded4a2589285dd40.jpg)

<details>
<summary>text_image</summary>

2200 cm⁻¹
2240 cm⁻¹
2200 cm⁻¹
2240 cm⁻¹
</details>

C  
![](images/00e2d5ab3a4117238ddda25b22e3583fc3f62dd9f4daa1d4a5caa401d6eebd10.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | MIP-PS signal |
| ------------------ | ------------- |
| 2100               | 0.005         |
| 2150               | 0.005         |
| 2200               | 0.01          |
| 2250               | 0.005         |
</details>

D  
![](images/5d6221e5e5da8dba5a76ebcfe0baa13bcba3802b395165839b0b84a679fc7b75.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Value  |
| ------------------ | ------ |
| 1200               | 0.003  |
| 1250               | 0.004  |
| 1300               | 0.006  |
| 1350               | 0.012  |
</details>

E  
![](images/3270ca673396975b7e38e2c72d835ba40a6c041562e5069b88ad512bab2af53c.jpg)

<details>
<summary>line chart</summary>

| Time (ns) | Value  |
| --------- | ------ |
| -100      | 0.002  |
| 0         | 0.015  |
| 100       | 0.008  |
| 200       | 0.003  |
| 300       | 0.001  |
</details>

Fig. 3. MIP-PS spectroscopy of 4-MBN and 4-NBT. (A) Measured dark-field scattering image of NSoF cavity. Scale bars, 10 μm. (B) Left: Zoomed-in view of dark-field scattering image from (A); top, blue solid box; bottom, blue dashed box. Right: MIP-PS image subtracted by IR-on and IR-off dark-field images at 2200 cm−1 (on-resonance) and $2 2 4 0 ~ \mathsf { c m } ^ { - 1 }$ (off-resonance). Scale bars, 1 μm. (C) Measured MIP-PS spectra of 4-MBN molecules from 10 NSoF cavities (red, Lorentzian fitted curve of mean MIP-PS spectra; gray, measured MIP-PS signals from individual cavities; error bars, SD of MIP-PS signals). Each MIP-PS signal is the integration of the subtracted scatting intensity of a whole nanocavity. (D) Measured MIP-PS spectra of 4-­NBT molecules from 10 NSoF cavities. (E) Measured time decay curve of the MIP-PS signal of 4-MBN molecules inside the NRoF cavity (black, exponential fitted curve of mean time decay signals; errorbars, measured MIP-PS signals from individual nanorod-on-film (NRoF) cavities). The procedure of the time-resolved measurements is described in Fig. 2C.

## Simulation results

To quantify the scattering intensity variation corresponding to the modulation of the spacing of nanocavity induced by IR absorption of molecules, we performed finite element method (FEM) simulation with COMSOL. For the Au NSoF structure, the diameter of the nanosphere is 50 nm, the thickness of the Au nanoplate is 20 nm, and the substrate is a silicon wafer with the thickness of 500 nm. There are two characteristic bright modes as shown in the scattering spectra of NSoF cavity in Fig. 1C. To quantify the spacing of the nanocavities, the ground-state molecular structure was optimized with DFT using the r2 SCAN-3c composite method under metalmolecule configuration (38). The optimized geometries of Au/4- MBN and 4-MBN anion are shown in fig. S9, where the molecular size is optimized to be 0.686 nm at equilibrium. The calculated nano-geometry of 4-MBN at its equilibrium state is detailed in table S1. Here, we focused on the transverse mode located at the wavelength of about 600 nm (Fig. 4A). The plasmonic coupling effect leads to a higher field confinement in the nanocavity and narrower linewidth of the far-field scattering peaks. The narrow linewidth of $\sim 7 0 ~ \mathrm { c m ^ { - 1 } }$ is beneficial to the plasmon sensing due to higher figure of merit and stronger enhancement factor improving the interaction between IR photons and analyte molecules inside the nanocavity. As in the fundamental states without IR heating, the spacing thickness is 0.686 nm defined by the calculated molecular size, and the corresponding scattering peaks located at 590 and 820 nm. While increasing the gap spacing, the scattering peak position shifted to a shorter wavelength and the peak width is slightly narrower. The reason of the blueshift with increasing gap spacing is that the coupling strength between LSPR of the nanoparticle and SPP modes of the nanofilm is reduced with larger separation. Thus, the NSoF radiates more into far-field which leads to blue-shifting of peak position (Fig. 4A). At the wavelength of 638 nm when the first derivative of the scattering spectra reaches the local maximum, the scattering cross section of the NSoF structure dropped from 1.84 to 1.83 nm2 as gap spacing expands from 0.686 to 0.687 nm. The modification of \~0.6% in far-field scattering of NSoF is experimentally detectable to probe the molecular deformation induced by IR absorption.

A  
![](images/080b94a1775d1d95d7d8fe2de1227ab8c3b79730b3734410b4c21fe076ad9b83.jpg)

<details>
<summary>heatmap</summary>

| Gap spacing (nm) | Value |
| ---------------- | ----- |
| 0.764            |       |
| 0.744            |       |
| 0.724            |       |
| 0.704            |       |
| 0.684            |       |
</details>

Wavelength(nm)

nm{2  
![](images/89e61d2d91976800613d3a04a6c39e514f3eeb39dbb585cd18cf207502159942.jpg)

<details>
<summary>line chart</summary>

| Gap spacing (nm) | Scattering Cross section (nm²) |
| ---------------- | ------------------------------- |
| 0.68             | 2.5                             |
| 0.70             | 2.4                             |
| 0.72             | 2.2                             |
| 0.74             | 2.0                             |
| 0.76             | 1.8                             |
</details>

B  
![](images/45558298604b943b41b65d5ecab55eef6cc6e8d0f84ad33cd82f599f6d29c80e.jpg)

<details>
<summary>scatterplot</summary>

| Wavelength(nm) | Gap spacing(nm) |
| -------------- | --------------- |
| 740            | 0.744           |
</details>

nm^{  
![](images/85341c43935097b4f607c31fd81fa4eee5933963b187e500a571cb09b2c356cb.jpg)

<details>
<summary>line chart</summary>

| Gap spacing (nm) | Resonant wavelength (nm) |
| ---------------- | ------------------------ |
| 0.68             | 1.5                      |
| 0.70             | 1.2                      |
| 0.72             | 0.9                      |
| 0.74             | 0.6                      |
| 0.76             | 0.4                      |
</details>

E  
![](images/6bf1a9dd8ccc22e2f681495fcde4ff4112c3c6d164176de693f2ca6f3fe4b186.jpg)

<details>
<summary>chemical</summary>

Molecular structure diagram of 4-MBN-Au20, showing atomic bonds and spatial arrangement
</details>

F  
![](images/ecabffa239908ed7e42dcfb2ad2de4258bfc59129aa30458fc20dd75ac229842.jpg)

<details>
<summary>heatmap</summary>

| Time (ns) | X axis (nm) | Y axis (nm) | ΔT (K) |
|-----------|-------------|-------------|--------|
| 20        | -10         | 0           | 0      |
| 20        | -5          | 0           | 0      |
| 20        | 0           | 0           | 0      |
| 20        | 5           | 0           | 0      |
| 20        | 10          | 0           | 0      |
| 40        | -10         | 0           | 0      |
| 40        | -5          | 0           | 0      |
| 40        | 0           | 0           | 0      |
| 40        | 5           | 0           | 0      |
| 40        | 10          | 0           | 0      |
| 60        | -10         | 0           | 0      |
| 60        | -5          | 0           | 0      |
| 60        | 0           | 0           | 0      |
| 60        | 5           | 0           | 0      |
| 60        | 10          | 0           | 0      |
| 80        | -10         | 0           | 0      |
| 80        | -5          | 0           | 0      |
| 80        | 0           | 0           | 0      |
| 80        | 5           | 0           | 0      |
| 80        | 10          | 0           | 0      |
</details>

Fig. 4. Simulation of dependence of far-field scattering from a NPoF cavity on the gap spacing and the thermal dynamics of MIP-PS. (A) Simulated color map of scattering cross section of NSoF cavity with varied gap spacing. Increased gap spacing leads to the blueshift of the far-field scattering peak position of the NSoF cavity. Color bar, scattering cross section. Dashed line, probe wavelength. Inset: Incident angle of the wave vector (68°). The diameter of the NS is 50 nm. The thickness of the nanofilm is 20 nm. (B) Simulated color map of scattering cross section of NRoF cavity with varied gap spacing. The length of the NR is 103 nm, and the diameter of the NR is 24 nm. The thickness of the nanofilm is 20 nm. (C) The far-field scattering cross section of NSoF cavity (blue) and NRoF cavity (red) at probe wavelength (638 and 800 nm, respectively) dependent on the gap spacing. (D) Dependence of the plasmonic resonant wavelength (λ) of NSoF cavity on the gap spacing (s). (E) Simulated molecular structure of Au/4-MBN system at ground state. Unit, angstrom. (F) Simulated temperature increase of the monolayer 4-MBN molecules during and after an IR heating pulse of 50 ns.

To optimize the geometric design of the plasmonic nanocavity, we compared the sensitivity of the NRoF with that of the NSoF structure. As for NRoF cavities, there are three characteristic peaks in the spectral range from 590 to 840 nm (Fig. 4, B and C) resulted from the hybridization of the film-coupled vertical mode of the nanorod and SPP modes along the nanofilm. We selected the scattering peak at around 780 nm matching with the probe wavelength of 800 nm discussed in the “Experimental results” section. The corresponding scattering intensity of NRoF decreased by 0.1% when the gap spacing increases from 0.686 to 0.687 nm, which was 83% smaller than that of NSoF. As shown in Fig. 4D, the sensitivity is dependent on the contacting area of the NPoF cavities. When the contacting area decreases, the optical properties are more sensitive to the variation of the thickness and the refractive index of the spacer. Meanwhile, the scattering cross section is positively related to the size of the nanoparticle, so we selected the Au nanosphere with the diameter of 50 nm as the plasmonic scatter. On the other hand, the coupling strength between the nanoparticle and nanofilm is positively related to the thickness of the nanofilm. However, the transmittance of the mid-IR beam is in negative correlation with the thickness of the nanofilm. Thus, we selected the Au nanoplate with the thickness of 20 nm to form the plasmonic nanocavity, where \~30% of the incident mid-IR power is transmitted to the nanogap. Last, the optimized NSoF cavity to detect the vibrationally excited molecules shows a sensitivity of 75 times the plasmonic resonance wavelength dependent on the gap spacing of the nanocavity (Fig. 4D).

Next, we considered two mechanisms of gap spacing modulation. One is via direct IR excitation of chemical bond, and the other is via the MIP effect.

To theoretically estimate the molecular deformation induced by IR excitation, we further simulated the molecular structures of 4-mercaptobenzonitrile (4-MBN) at vibrational-corrected mode. To calculate the bond displacement at vibrational-excited states, the Becke, 3-parameter, Lee-Yang-Parr (B3LYP) hybrid density functional in combination with the balanced polarized triple-zeta (def2- TZVP) basis set was used. The anharmonic analysis and vibrational correction were performed by second-order vibrational perturbation theory (VPT2) module in Orca 5.0.4 (39, 40). The molecular geometry was simplified to 4-MBN anion in the VPT2 calculation. As shown in fig. S9, the nitrile bond length of 4-MBN anion increased by 0.1 Å at the ─CN stretching mode compared with its fundamental state (Fig. 4E). The optimized geometry of 4-MBN anion with and without vibrational correction is compared in tables S2 and S3. Therefore, there is a \~1.3% modification of the gap spacing of the plasmonic nanocavity when 4-MBN analyte molecules are pumped from the ground state to the ─CN stretching mode.

To quantify the IR absorbance of target molecule in MIP-PS measurements, we calculated the total IR energy absorbed by nitrile groups in the hot area of a nanocavity as $E _ { \mathrm { t o t } } = \mathrm { \bar { \it N } } | E _ { \mathrm { f } } | ^ { 2 } \mathrm { \frac { \it P } { \it A } } \sigma .$ . Here, $E _ { \mathrm { t o t } }$ is the total energy absorbed by absorbers, N is the molecule number in the hot area of the nanocavity, $E _ { \mathrm { f } }$ is the averaged field enhancement factor of the hot area, P is the power of input IR beam, A is the IR illumination area, τ is the pulse duration of IR incidence, and σ is the absorption cross section of the absorbers. The input pulse energy is 0.026 nJ with a loosely focused beam diameter of 50 μm and a pulse width of 50 ns. The molecule number is estimated to be 218 (the Supplementary Materials). The IR intensity enhancement factor provided by the nanogap is around ${ { 1 0 } ^ { 3 } }$ . Considering the IR absorption cross section of nitrile group to be $6 \times 1 0 ^ { - 1 8 } \ \mathrm { c m } ^ { 2 } .$ , the IR photon number $( N _ { \mathrm { a b s } } = E _ { \mathrm { t o t } } / E _ { \mathrm { p h o t o n } } )$ absorbed by the molecules inside the nanogap is calculated to be about $4 \times 1 \dot { 0 } ^ { 4 }$ . Considering the vibrational lifetime on the level of 10 $\mathrm { p } \mathsf { s } ,$ the population of molecules at vibrational excited states are 4% during an IR heating pulse. As a result, under the current experimental condition, the IR pulse energy is not sufficient to pump all the monolayer molecules.

Alternatively, the spacing distance of the nanogap can be regulated by the thermal expansion of the monolayer molecules $( \Delta l = l _ { \mathrm { o } } \alpha _ { \mathrm { t h } } \Delta T$ ). Here, $l _ { \mathrm { o } }$ is the initial molecule length, $\alpha _ { \mathrm { t h } }$ is the thermal expansion coefficient, and $\Delta T$ is the change of temperature. The thermal expansion coefficient $\alpha _ { \mathrm { t h } }$ is assumed to be the same as those of bulk polymer materials $( 1 0 ^ { - 4 } ~ \mathrm { K } ^ { - 1 } )$ . Assuming the nanogap expanded from 0.686 to 0.687 nm derived from the FEM simulation results, the corresponding temperature rise is about 14 K. We simulated the temperature increase during and after an IR heating pulse of a NSoF cavity as shown in Fig. 4F. The general parameters of the simulation were detailed in the Supplementary Materials. Thus, the integrated temperature rise of the monolayer molecules within the hot area of the nanocavity is calculated to be 16 K, which is consistent with the modulation depth in MIP-PS measurements. The heat generated during the IR pulse with a pulse width of 50 ns diffuses away after 80 ns, which matches well with the experimental results of time relaxation.

## DISCUSSION

The reported MIP-PS spectroscopy pushes the IR detection limit toward few molecules in a plasmonic nanocavity. IR spectroscopy of nitrile and nitro groups from \~130 molecules has been experimentally resolved with MIP-PS system. The plasmonic scattering modification of the NPoF cavities from IR absorption of analyte molecules inside the nanogap was initially attributed to the bond displacement at different vibrational states. The bond-regulated MIP-PS sensing mechanism is explained with DFT simulation of molecular structures and FEM simulation of optical characterization of the plasmonic nanocavities. The theoretical calculation of the modification of the scattering intensity shows a change by 0.6% for NSoF, which is on the same level with the experimental results of 1 to 1.5%. The deviation in the experimental MIP-PS signal compared to our simulation results is mainly resulted from the nanoparticle-to-nanoparticle variation from the chemical synthesis process and the surface quality of the nanoparticles and nanoplates. However, considering the short vibrational lifetime of \~10 ps, only less than 10% of the molecules are vibrationally excited during an IR pulse of tens of nanosecond. Thus, there are some other potential mechanisms that synergistically affect the phenomena that we observed. Calculated by the bulk thermal expansion coefficient of the small organic molecules, the predicted temperature increase of \~15 K is in agreement with our MIP-PS signal contrast of a SAM. From the energy perspective, the photothermal expansion induced by IR absorption of the molecules is sufficient to expand the nanogap against the van der Waals attraction between the nanoparticle and the nanofilm (see the Supplementary Materials). Meanwhile, the thermal relaxation time is small due to the high thermal conductivity of gold. Tip-enhanced AFM-IR (15) has also resolved IR spectra of monolayer molecules with the plasmonic enhancement introduced by the nanogap between the AFM tip and the Au film. The predicted expansion of the gap spacing distance is \~10 pm, which is also in agreement with our MIP-PS signal contrast.

The plasmonic scattering modification of the NPoF cavities from IR absorption of analyte molecules inside the nanogap is attributed to the photothermal expansion during the relaxation from different vibrational states. There are some other factors that simultaneously contribute to MIP-PS contrasts, such as temperature-dependent refractive index change of the spacer. As for the thermo-optical effect, metasurface-enhanced reflection IR spectroscopy (41) has achieved the IR detection of monolayer protein based on its temperaturedependent refractive index, while the temperature-dependent refractive index change of a SAM of small molecules only contributes less than 1/10 modification of the plasmonic scattering change compared to the spacing effect (fig. S10). Another possible explanation on this modulation is the altered water shell thickness of the residue water in the crevice (30). However, because the scattering intensity of the nanocavity structure is more sensitive to the spacing distance change of the nanogap (determined by the monolayer molecules) compared with the thick water shell in the surroundings, the modulation depth induced by water shell expansion is one order of magnitude below the MIP-PS signal on the level of 1% in our experiments (see the Supplementary Materials).

To fingerprint individual molecules through recognition of characteristic bond vibrations, surface-enhanced Raman spectroscopy has reached single-molecule level with plasmonic enhancement inside metallic nanojunctions (42, 43). Furthermore, plasmon-enhanced coherent anti-Stokes Raman scattering (44), stimulated Raman scattering (45), and stimulated Raman excited fluorescence (46) have sped up the spectral acquisition time and thus enabled singlemolecule Raman imaging. Mid-IR spectroscopic information of individual small molecules without fluorescence and Raman activity has yet remained unreachable. MIP-PS spectroscopy has enabled IR chemical analysis of few molecules via plasmonic nanocavity with its extreme sensitivity of plasmonic scattering spectra to the spacing defined by the bond displacement of analyte molecules inside the nanogap. MIP-PS spectroscopy suggests potential in ultrasensitive bond-selective biosensing and bioimaging. Taking advantages of the extreme sensitivity of plasmonic scattering spectra dependent on the spacing of the nanocavity and the high scattering cross section of the metallic nanoparticles, nanodimer structure functionalized with IR-active groups can serve as ultrasensitive IR reporters. By treating cells with MIP-PS reporters through endocytosis, we can potentially study conformational change or binding event of biomolecules in vivo.

## MATERIALS AND METHODS

## Materials

All chemicals were obtained from commercial suppliers and used without further purification. Cetyltrimethylammonium bromide $( \mathrm { C T A B } ; > 9 9 \% ) .$ , l-ascorbic acid $( \mathrm { A A } ; > 9 9 \% )$ , sodium borohydride $\left( \mathrm { N a B H _ { 4 } } ; { > } 9 8 \% \right)$ , silver nitrate $( \mathrm { A g N O } _ { 3 } ; > 9 9 \% ) .$ , gold (III) chloride trihydrate $\mathrm { ( H A u C l _ { 4 } { \cdot } 3 H _ { 2 } O ; > 9 9 . 9 \% ) }$ , hydrochloric acid (HCl; 37 wt % in water), sulfuric acid $( \mathrm { H } _ { 2 } \mathrm { S O } _ { 4 } ; ~ 9 5 $ to 98%), ethylene glycol (>99.8%), and 4-MBN were purchased from Sigma-Aldrich. 4-NBT (>95%) and sodium oleate $\left( \mathrm { N a O L } ; { > } 9 7 \% \right)$ were purchased from TCI America. Deionized (DI) water (18.2 megohms) was provided by a Synergy UV water purification system. All reactions were carried out in glassware cleaned by aqua regia and piranha solution.

## Synthesis of gold nanospheres

Au nanospheres with an average diameter of 56 nm were synthesized by following a multistep seeded growth synthetic protocol developed by Bastús et al. (47) with modifications. In brief, first, the seed solution was synthesized as follows: 141.5 ml of DI water was heated to $1 0 0 ^ { \circ } \mathrm { C }$ in a 250-ml flask. A condenser was used to prevent the evaporation of the solvent. $\mathrm { H A u C l _ { 4 } }$ solution (25 mM; 1 ml) was added to the flask under vigorous stirring. Once the boiling had commenced again, 8.5 ml of sodium citrate solution (1 wt %) was quickly injected. The color of the solution changed from light yellow to pink within 5 min. The mixture was kept under boiling for 30 min to form the seeds with an average diameter of around 20 nm. Second, the seeded growth of gold nanoparticles was conducted at $9 0 ^ { \circ } \mathrm { C }$ . The seed solution was first cooled down to $9 0 ^ { \circ } \mathrm { C } ,$ , and, then, 50 ml of seed solution was extracted to maintain a volume of 100 ml in the flask. Then, 0.67 ml of $\mathrm { H A u C l _ { 4 } }$ solution (25 mM) was quickly added, and the mixture was kept at $9 0 ^ { \circ } \mathrm { C }$ under constant vigorous stirring. After 30 min, another $0 . 6 7$ ml of HAuCl solution (25 mM) was injected again, and the mixture was kept at $9 0 ^ { \circ } \mathrm { C }$ under constant vigorous stirring for another 30 min. The average size of gold nanoparticles in the flask was about 31 nm after these two steps. Then, the solution was diluted by extracting 50 ml of nanoparticle solution and then adding 50 ml of DI water and 3 ml of sodium citrate solution (1 wt %). The system was then stabilized for 15 min to allow the temperature to recover to $9 0 ^ { \circ } \mathrm { C }$ Then, 1 ml of $\mathrm { H A u C l _ { 4 } }$ solution (25 mM) was quickly added, and the mixture was kept at $9 0 ^ { \circ } \mathrm { C }$ under constant vigorous stirring for 30 min. This procedure was then repeated for another two times, resulting in the formation of 56-nm gold nanoparticles used for MIP-PS detection.

## Synthesis of gold nanorods

Au nanorods with an average diameter of 24 nm and an average length of 103 nm were synthesized by following a modified protocol developed by Ye et al. (48), with the detailed synthetic protocol and characterizations described in our previous study (49). In brief, the seed solution was synthesized as follows: 5 ml of $\mathrm { H A u C l _ { 4 } }$ solution (0.54 mM) was mixed with 5 ml of CTAB solution $( 0 . 2 \mathbf { M } )$ in a 20-ml glass vial. Fresh $\mathrm { N a B H _ { 4 } }$ solution (6 mM; 1 ml) was added to the above mixture solution under vigorous stirring (2000 rpm). The color of the solution changed from yellow to brownish yellow, and the stirring was stopped after 2 min. The seed solution was aged at room temperature for 45 min before use. The growth solution was prepared by dissolving 1.8 g of CTAB and 246.8 mg of NaOL in 50 ml of warm water $( { \sim } 5 0 ^ { \circ } \mathrm { { C } ) }$ in a 250-ml flask. The solution was cooled down to $3 0 ^ { \circ } \mathrm { C } ,$ and 4.8 ml of $\mathrm { A g N O } _ { 3 }$ solution (4 mM) was added.

The mixture was kept undisturbed at $3 0 ^ { \circ } \mathrm { C }$ for 15 min after which 50 ml of $\mathrm { H A u C l _ { 4 } }$ solution (1.08 mM) was added. The solution became colorless after 90 min of stirring (700 rpm), and 0.72  ml of HCl solution (37 wt % in water) was added to adjust the pH value. After another 15 min of slow stirring at 400 rpm, 0.25 ml of ascorbic acid (AA, 0.064 M) was added, and the solution was vigorously stirred at 1500 rpm for 30 s. Last, 0.02 ml of seed solution was added to the growth solution. The mixture was stirred at 1500 rpm for another 30 s and left undisturbed at $3 0 ^ { \circ } \mathrm { C }$ for 12 hours for Au nanorods growth.

## Synthesis of gold nanoplates

Au nanoplate was synthesized in situ through the reduction of $\mathrm { H A u C l _ { 4 } }$ solution with ethylene glycol on silicon wafer by following a modified protocol developed by Krauss et al. (50, 51). ${ \mathrm { H A u C l } } _ { 4 } s 0 -$ lution (100 mM; 180 μl) was added to 5 ml of ethylene glycol. Then, 225 μl of DI water was added to the mixture solution to speed up the reaction to form thin nanoplate. The mixture solution was slowly stirred for 30 s and, then, the pre-cleaned silicon wafer was put into the solution. The mixture was then left undisturbed at $9 5 ^ { \circ } \mathrm { C }$ for 4.5 hours for growth. After synthesis, the chip with Au nanoplate was washed with ultrasonic for 1 min in ethanol alcohol before functionalization. The chemically synthesized ultrasmooth surface of the single-crystal Au nanoplate promised the high quality of the plasmonic nanocavity.

## Preparation of NPoF cavities

To prepare the nanocavity structure, the Au nanoplate was functionalized with a SAM of analyte molecules. The chip with Au nanoplate was immersed into 500 μM 4-MBN or 4-NBT solution and kept still for 12 hours. The functionalized chip was cleaned by sonication for 1 min in ethanol alcohol and dried with nitrogen gas. The presynthesized nanoparticle solution was then drop-casted on the nanoplate and dried with nitrogen gas.

## MIP-PS experimental setup

The MIP-PS system is a pump-probe microscope with counterpropagating mid-IR excitation beam and a visible probe beam $( \mathrm { F i g . }$ 2A). A 638-nm laser (Cobolt 08-NLD, 638-nm-wavelength) was triggered to 100 kHz with the pulse width of 500 ns by a pulse generator (Emerald Pulse Generator, 9254-TZ50-US, Quantum composers). The probe laser beam was expanded by a 4-f system and then formed the ring-shape illumination through a three-dimensionally (3D) printed annular aperture with the diameter of 26 mm to accommodate the waist of the dark-field objective [Olympus 100×, numerical aperture $( \mathrm { N A } ) = 0 . 9 ]$ . The illumination angle was $6 8 ^ { \circ } .$ . The backscattered photons were recorded by a complementary metal-oxide semiconductor camera (FS-U3-17S7, FLIR, dynamic range of 72.46 dB, dark noise of $2 2 . 9 9 e ^ { - } )$ synchronized to 100 Hz by the pulse generator. The pump beam was nanosecond mid-IR pulses from QCL (Daylight MIRcat) laser external triggered to 100 kHz. The mid-IR beam was loosely focused on the sample with an area of 50 μm by 50 μm by a parabolic mirror [Thorlabs, focal length of 1 inch (2.54 cm)]. The mid-IR pulses was then chopped to hot states (1000 pulses on) and cold states (1000 pulses off) sequentially by the pulse generator. The MIP-PS images were then generated by subtraction of adjacent hot frames and cold frames. To eliminate the power fluctuations of the probe laser, we defined a reference area at the camera plane by placing a tilted mirror at the spare path of the beam splitter to simultaneously collect the probe laser power during experiments. The probe laser fluctuation was then compensated by normalization of the subtracted MIP-PS signal with the measured probe laser power at hot and cold states, respectively. By scanning the wavelength of the IR excitation beam, we obtained a hyperspectral stack. By integrating the scattered photons from a single nanocavity unit, we plotted and analyzed the MIP-PS spectra.

## Molecular simulations

All molecular calculations were performed with ORCA 5.0.4. The metal-molecule system was optimized using r2 SCAN-3c composite method. All vibration corrections were calculated with VPT2 module in ORCA using the B3LYP hybrid density functional in combination with the def2-TZVP basis set. All VPT2 corrections were performed on anion state of molecules without Au binding structures to compensate the computation complexity to reach extreme convergence for anharmonic analysis. Anharmonic constant of analytes was attained from VPT2 calculation, and, thus, the bond displacement at vibrational excited states was quantified through analytical relations between vibrational mean structure and anharmonicity (52) or displaced Hessian matrix based on quantum mechanics calculation (see the Supplementary Materials).

## Dark-field scattering spectra measurements

The dark-field scattering spectra of NSoF structures were measured with an imaging spectrometer (Shamrock 303i, Andor Technology) equipped with an electron multiplying CCD (NewtonEM). The samples were illuminated with an unpolarized white light through a dark-field air condenser. Scattered photons from the nanostructures were then collected with a 60× oil immersion objective (NA = 1.4) in transmission mode. The recorded scattering spectra were subtracted by the background scattering signals and then normalized with the power spectrum of the illumination source.

## FTIR measurements

The standard IR spectra of analyte molecules were collected with Nicolet Nexus 670 FT-IR (ATR mode). The samples (4-MBN pow der and 4-NBT powder) were prepared as powders covering the op tical window of a ZnSe substrate. The ATR spectra were collected at a spectral resolution of 2 cm−1 with an averaging time of 128.

## Fitting of time-resolved curve

The time-resolved MIP-PS curve is fitted by the convolution of the instrumental response function R(t) and the exponential decay from the sample S(t)

$$
I (t) = \int R \left(t - t ^ {\prime}\right) S \left(t ^ {\prime}\right) d t ^ {\prime} \tag {1}
$$

Here, R(t) is modeled by a Gaussian function with a full width at half maximum σ as the instrumental response time

$$
R (t) = A _ {1} e ^ {- \frac {t ^ {2}}{2 * \sigma^ {2}}} \tag {2}
$$

Meanwhile, the pump-probe decay is modeled by an exponential function with a decay constant τ

$$
S (t) = A _ {2} e ^ {- \frac {t}{\tau}} \tag {3}
$$

Thus, the time-dependent MIP-PS signal can be derived as the following function

$$
I (t) = A * e ^ {\frac {\sigma^ {2} - 2 * t * \tau}{2 * \tau^ {2}}} * \left[ 1 - \operatorname{erf} \left(\frac {\sigma^ {2} - t * \tau}{\sqrt {2} * \sigma * \tau}\right) \right] \tag {4}
$$

The time decay curve shown in Fig. 3E is then fitted using the convolution function described above.

## Supplementary Materials

This PDF file includes:

Supplementary Text

Figs. S1 to S10

Tables S1 to S3

References

## REFERENCES AND NOTES

1. M. J. Baker, J. Trevisan, P. Bassan, R. Bhargava, H. J. Butler, K. M. Dorling, P. R. Fielden, S. W. Fogarty, N. J. Fullwood, K. A. Heys, C. Hughes, P. Lasch, P. L. Martin-­Hirsch, B. Obinaju, G. D. Sockalingum, J. Sulé-Suso, R. J. Strong, M. J. Walsh, B. R. Wood, F. L. Martin, Using Fourier transform IR spectroscopy to analyze biological materials. Nat. Protoc. 9, 1771–1791 (2014).  
2. R. Bhargava, Infrared spectroscopic imaging: The next generation. Appl. Spectrosc. 66, 1091–1120 (2012).  
3. N . Jamin, P. Dumas, J. Moncuit, W.-­H. Fridman, J.-­L. Teillaud, G. L. Carr, G. P. Williams, Highly resolved chemical imaging of living cells by using synchrotron infrared microspectrometry. Proc. Natl. Acad. Sci. U.S.A. 95, 4837–4840 (1998).  
4. X. Gao, X. Li, W. Min, Absolute stimulated raman cross sections of molecules. J. Phys. Chem. Lett. 14, 5701–5708 (2023).  
5. D. Zhang, C. Li, C. Zhang, M. N. Slipchenko, G. Eakins, J.-X. Cheng, Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2, e1600521 (2016).  
6. Y. Bai, D. Zhang, L. Lan, Y. Huang, K. Maize, A. Shakouri, J.-X. Cheng, Ultrafast chemical imaging by widefield photothermal sensing of infrared absorption. Sci. Adv. 5, eaav7127 (2019).  
7. Q. Xia, J. Yin, Z. Guo, J.-X. Cheng, Mid-infrared photothermal microscopy: Principle, instrumentation, and applications. J. Phys. Chem. B. 126, 8597–8613 (2022).  
8. Y. Bai, J. Yin, J.-X. Cheng, Bond-selective imaging by optically sensing the mid-infrared photothermal effect. Sci. Adv. 7, eabg1559 (2021).  
9. H . Zong, C. Yurdakul, Y. Bai, M. Zhang, M. S. Unlu, J.-X. Cheng, Background-suppressed high-throughput mid-infrared photothermal microscopy via pupil engineering. ACS Photonics 8, 3323–3336 (2021).  
10. J. Yin, M. Zhang, Y. Tan, Z. Guo, H. He, L. Lan, J.-X. Cheng, Video-rate mid-infrared photothermal imaging by single-pulse photothermal detection per pixel. Sci. Adv. 9, eadg8814 (2023).  
11. O. Klementieva, C. Sandt, I. Martinsson, M. Kansiz, G. K. Gouras, F. Borondics, Superresolution infrared imaging of polymorphic amyloid aggregates directly in neurons. Adv. Sci. 7, 1903004 (2020).  
12. J. M. Lim, C. Park, J.-S. Park, C. Kim, B. Chon, M. Cho, Cytoplasmic protein imaging with mid-infrared photothermal microscopy: Cellular dynamics of live neurons and oligodendrocytes. J. Phys. Chem. Lett. 10, 2857–2861 (2019).  
13. D. Khanal, J. Zhang, W.-R. Ke, M. M. B. Holl, H.-K. Chan, Bulk to nanometer-scale infrared spectroscopy of pharmaceutical dry powder aerosols. Anal. Chem. 92, 8323–8332 (2020).  
14. A. Dazzi, C. B. Prater, AFM-­IR: Technology and applications in nanoscale infrared spectroscopy and chemical imaging. Chem. Rev. 117, 5146–5173 (2017).  
15. F. Lu, M. Jin, M. A. Belkin, Tip-enhanced infrared nanospectroscopy via molecular expansion force detection. Nat. Photonics 8, 307–312 (2014).  
16. F. S. Ruggeri, B. Mannini, R. Schmid, M. Vendruscolo, T. P. J. Knowles, Single molecule secondary structure determination of proteins through infrared absorption nanospectroscopy. Nat. Commun. 11, 2945 (2020).  
17. L . Wang, H. Wang, M. Wagner, Y. Yan, D. S. Jakob, X. G. Xu, Nanoscale simultaneous chemical and mechanical imaging via peak force infrared microscopy. Sci. Adv. 3, e1700255 (2017).  
18. L . Dong, X. Yang, C. Zhang, B. Cerjan, L. Zhou, M. L. Tseng, Y. Zhang, A. Alabastri, P. Nordlander, N. J. Halas, Nanogapped Au antennas for ultrasensitive surface-enhanced infrared absorption spectroscopy. Nano Lett. 17, 5768–5774 (2017).  
19. H . Hu, X. Yang, X. Guo, K. Khaliji, S. R. Biswas, F. J. García De Abajo, T. Low, Z. Sun, Q. Dai, Gas identification with graphene plasmons. Nat. Commun. 10, 1131 (2019).  
20. A. John-­Herpin, A. Tittl, L. Kuhner, F. Richter, S. H. Huang, G. Shvets, S. H. Oh, H. Altug, Metasurface-enhanced infrared spectroscopy: An abundance of materials and functionalities. Adv. Mater. 35, 2110163 (2023).  
21. A. Leitis, M. L. Tseng, A. John-­Herpin, Y. S. Kivshar, H. Altug, Wafer-scale functional metasurfaces for mid-infrared photonics and biosensing. Adv. Mater. 33, 2102232 (2021).  
22. T . Tanaka, T.-A. Yano, R. Kato, Nanostructure-enhanced infrared spectroscopy. Nanophotonics 11, 2541–2561 (2022).  
23. F. Vollmer, S. Arnold, Whispering-gallery-mode biosensing: Label-free detection down to single molecules. Nat. Methods 5, 591–596 (2008).  
24. L . Whaley-Mayda, A. Guha, S. B. Penwell, A. Tokmakoff, Fluorescence-encoded infrared vibrational spectroscopy with single-molecule sensitivity. J. Am. Chem. Soc. 143, 3060–3064 (2021).  
25. H . Wang, D. Lee, Y. Cao, X. Bi, J. Du, K. Miao, L. Wei, Bond-selective fluorescence imaging with single-molecule sensitivity. Nat. Photonics 17, 846–855 (2023).  
26. C . Yan, C. Wang, J. C. Wagner, J. Ren, C. Lee, Y. Wan, S. E. Wang, W. Xiong, Multidimensional widefield infrared-encoded spontaneous emission microscopy: Distinguishing chromophores by ultrashort infrared pulses. J. Am. Chem. Soc. 146, 1874–1886 (2024).  
27. A. Xomalis, X. Zheng, R. Chikkaraddy, Z. Koczor-Benda, E. Miele, E. Rosta, G. A. E. Vandenbosch, A. Martinez, J. J. Baumberg, Detecting mid-infrared light by molecular frequency upconversion in dual-wavelength nanoantennas. Science 374, 1268–1271 (2021).  
28. W. Chen, P. Roelli, H. Hu, S. Verlekar, S. P. Amirtharaj, A. I. Barreda, T. J. Kippenberg, M. Kovylina, E. Verhagen, A. Martinez, C. Galland, Continuous-wave frequency upconversion with a molecular optomechanical nanocavity. Science 374, 1264–1267 (2021).  
29. R. Chikkaraddy, R. Arul, L. A. Jakob, J. J. Baumberg, Single-molecule mid-infrared spectroscopy and detection through vibrationally assisted luminescence. Nat. Photonics 17, 865–871 (2023).  
30. R. Chikkaraddy, A. Xomalis, L. A. Jakob, J. J. Baumberg, Mid-infrared-perturbed molecular vibrational signatures in plasmonic nanocavities. Light Sci. Appl. 11, 19 (2022).  
31. D. A. McQuarrie, Quantum Chemistry (University Science Books, 2007).  
32. J. J. Mock, R. T. Hill, A. Degiron, S. Zauscher, A. Chilkoti, D. R. Smith, Distance-dependent plasmon resonant coupling between a gold nanoparticle and gold film. Nano Lett. 8, 2245–2252 (2008).  
33. R. Chikkaraddy, J. J. Baumberg, Accessing plasmonic hotspots using nanoparticle-on-foi constructs. ACS Photonics 8, 2811–2817 (2021).  
34. X. Qi, T. W. Lo, D. Liu, L. Feng, Y. Chen, Y. Wu, H. Ren, G.-­C. Guo, D. Lei, X. Ren, Effects of gap thickness and emitter location on the photoluminescence enhancement of monolayer MoS2 in a plasmonic nanoparticle-film coupled system. Nanophotonics 9, 2097–2105 (2020).  
35. C . Sönnichsen, B. M. Reinhard, J. Liphardt, A. P. Alivisatos, A molecular ruler based on plasmon coupling of single gold and silver nanoparticles. Nat. Biotechnol. 23, 741–745 (2005).  
36. P. Ertl, B. Rohde, P. Selzer, Fast calculation of molecular polar surface area as a sum of fragment-based contributions and its application to the prediction of drug transport properties. J. Med. Chem. 43, 3714–3717 (2000).  
37. K. I. Hadjiivanov, D. A. Panayotov, M. Y. Mihaylov, E. Z. Ivanova, K. K. Chakarova, S. M. Andonova, N. L. Drenchev, Power of infrared and raman spectroscopies to characterize metal-organic frameworks and investigate their interaction with guest molecules. Chem. Rev. 121, 1286–1424 (2021).  
38. S. Grimme, A. Hansen, S. Ehlert, J.-M. Mewes, r2SCAN-3c: A “Swiss army knife” composite electronic-structure method. J. Chem. Phys. 154, 064103 (2021).  
39. F. Neese, The ORCA program system. WIREs Comput. Mol. Sci. 2, 73–78 (2012).  
40. F. Neese, Software update: The ORCA program system—Version 5.0. WIREs Comput. Mol. Sci. 12, e1606 (2022).  
41. C . Wu, A. B. Khanikaev, R. Adato, N. Arju, A. A. Yanik, H. Altug, G. Shvets, Fano-resonant asymmetric metamaterials for ultrasensitive spectroscopy and identification of molecular monolayers. Nat. Mater. 11, 69–75 (2012).  
42. S. Nie, S. R. Emory, Probing single molecules and single nanoparticles by surfaceenhanced raman scattering. Science 275, 1102–1106 (1997).  
43. R. Zhang, Y. Zhang, Z. C. Dong, S. Jiang, C. Zhang, L. G. Chen, L. Zhang, Y. Liao, J. Aizpurua, Y. Luo, J. L. Yang, J. G. Hou, Chemical mapping of a single molecule by plasmon-enhanced Raman scattering. Nature 498, 82–86 (2013).  
44. S. Yampolsky, D. A. Fishman, S. Dey, E. Hulkko, M. Banik, E. O. Potma, V. A. Apkarian, Seeing a single molecule vibrate through time-resolved coherent anti-Stokes Raman scattering. Nat. Photonics 8, 650–656 (2014).  
45. C . Zong, R. Premasiri, H. Lin, Y. Huang, C. Zhang, C. Yang, B. Ren, L. D. Ziegler, J.-X. Cheng, Plasmon-enhanced stimulated Raman scattering microscopy with single-molecule detection sensitivity. Nat. Commun. 10, 5318 (2019).  
46. H . Xiong, L. Shi, L. Wei, Y. Shen, R. Long, Z. Zhao, W. Min, Stimulated Raman excited fluorescence spectroscopy and imaging. Nat. Photonics 13, 412–417 (2019).  
47. N . G. Bastús, J. Comenge, V. Puntes, Kinetically controlled seeded growth synthesis of citrate-stabilized gold nanoparticles of up to 200 nm: Size focusing versus Ostwald ripening. Langmuir 27, 11098–11105 (2011).  
48. X. Ye, C. Zheng, J. Chen, Y. Gao, C. B. Murray, Using binary surfactant mixtures to simultaneously improve the dimensional tunability and monodispersity in the seeded growth of gold nanorods. Nano Lett. 13, 765–771 (2013).  
49. R. Cheng, D. Jia, Z. Du, J.-X. Cheng, C. Yang, Gap-enhanced gold nanodumbbells with single-particle surface-enhanced Raman scattering sensitivity. RSC Adv. 13, 27321–27332 (2023).  
50. E . Krauss, R. Kullock, X. Wu, P. Geisler, N. Lundt, M. Kamp, B. Hecht, Controlled growth of high-aspect-ratio single-crystalline gold platelets. Cryst. Growth Des. 18, 1297–1302 (2018).  
51. L . Liu, A. V. Krasavin, J. Zheng, Y. Tong, P. Wang, X. Wu, B. Hecht, C. Pan, J. Li, L. Li, X. Guo, A. V. Zayats, L. Tong, Atomically smooth single-crystalline platform for low-loss plasmonic nanocavities. Nano Lett. 22, 1786–1794 (2022)  
52. T . Yamada, M. Aida, Structures of molecules in ground and excited vibrational states from quasiclassical direct ab initio molecular dynamics. J. Phys. Chem. A 114, 6273–6283 (2010).  
53. R. L. Olmon, B. Slovick, T. W. Johnson, D. Shelton, S.-­H. Oh, G. D. Boreman, M. B. Raschke, Optical dielectric function of gold. Phys. Rev. B 86, 235147 (2012).  
54. E . Shkondin, O. Takayama, M. E. A. Panah, P. Liu, P. V. Larsen, M. D. Mar, F. Jensen, A. V. Lavrinenko, Large-scale high aspect ratio Al-doped ZnO nanopillars arrays as anisotropic metamaterials. Opt. Mater. Express 7, 1606–1627 (2017).  
55. N ational Center for Biotechnology Information, PubChem Compound Summary for CI D 585058, 4-Mercaptobenzonitrile, PubChem (2024).  
56. N ational Center for Biotechnology Information, PubChem Compound Summary for CI D 15809, 4-­Nitrothiophenol, PubChem (2024).  
57. M. Bass, C. DeCusatis, J. Enoch, V. Lakshminarayanan, G. Li, C. Macdonald, V. Mahajan, E. Van Stryland, Handbook of optics, Volume II: Design, Fabrication and Testing, Sources and Detectors, Radiometry and Photometry (McGraw-­Hill Inc., 2009).  
58. J. Autschbach, T. Ziegler, Double perturbation theory: A powerful tool in computational coordination chemistry. Coord. Chem. Rev. 238–239, 83–126 (2003).

Acknowledgments: We thank G. Chen from Electrical and Computer Engineering Department at Boston University for assisting with 3D printing of the annular aperture for the MIP-PS experimental setup. We thank T. Ouyang from Chemistry Department at Boston University for help on dark-field scattering spectroscopy for the characterization of nanostructures.

Funding: This work is supported by R35GM136223 from National Institutes of Health and R33CA261726 from National Institute of General Medical Sciences to J.-X.C. Author contributions: D.J and J.-X.C. initialized the idea of MIP-PS spectroscopy; D.J. and H.Z. designed and built the MIP-PS experimental setup; R.C., D.J., and X.X. synthesized the nanostructures; D.J. and R.C. carried out the experiments. D.J. analyzed the experimenta results. D.J. performed the simulation. J.H.M., X.T., and D.J. performed the DFT simulation. R.C. and D.J. characterized the nanostructures. J.-X.C. supervised the research and the development of the manuscript. D.J. wrote the manuscript with input from all authors.

Competing interests: The authors declare that they have no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials.

Submitted 4 January 2024

Accepted 15 November 2024

Published 20 December 2024

10.1126/sciadv.adn8255

# ScienceAdvances

## Ultrasensitive infrared spectroscopy via vibrational modulation of plasmonic scattering from a nanocavity

Danchen Jia, Ran Cheng, James H. McNeely, Haonan Zong, Xinyan Teng, Xinxin Xu, and Ji-Xin Cheng

Sci. Adv. 10 (51), eadn8255. DOI: 10.1126/sciadv.adn8255

View the article online

https://www.science.org/doi/10.1126/sciadv.adn8255

Permissions

https://www.science.org/help/reprints-and-permissions

Use of this article is subject to the Terms of service