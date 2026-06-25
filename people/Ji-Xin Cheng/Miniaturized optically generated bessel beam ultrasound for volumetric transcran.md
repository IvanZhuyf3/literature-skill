## A P P L I E D S C I E N C E S A N D E N G I N E E R I N G

# Miniaturized optically generated Bessel beam ultrasound for volumetric transcranial brain stimulation

Yueming Li1 , Guo Chen1 , Tiago R. Oliveira2,3 , Nick Todd2 , Yong-Zhi Zhang2 , Carolyn Marar4 , Nan Zheng5 , Lu Lan1 , Nathan McDannold2 , Ji-Xin Cheng1,4 \*, Chen Yang1,6 \*

Noninvasive stimulation of small, variably shaped brain subregions is crucial for advancing our understanding of brain functions. Current ultrasound neuromodulation faces two major trade-offs when targeting brain subregions: miniaturization versus volumetric control and spatial resolution versus transcranial capability. Here, we present an optically generated Bessel beam ultrasound (OBUS) device designed to overcome these limitations. This miniaturized device, measuring 2.33 millimeters in diameter, delivers a column-shaped field achieving a lateral resolution of 152 micrometers and an axial resolution of 1.93 millimeters, enabling targeting of brain subregions with an elongated volume of tissue activation. Immunofluorescence imaging of mouse brain slices confirms its ability to stimulate cells at depths up to 2.1 millimeters. In addition, OBUS outperforms conventional Gaussian ultrasound in transcranial transmission efficiency and beam shape preservation. Electrophysiological recordings and functional MRI captured rodent brain responses evoked by OBUS, demonstrating OBUS’s ability to noninvasively activate neural circuits in intact brains. This technology offers expanded possibilities for studying brain functions with precision and volumetric control.

Copyright © 2026 The

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

Precisely modulating brain subregions is critical for decoding brain function at the level of individual functional units, enabling research ers to explore complex neural mechanisms and developing more effective therapeutic interventions (1–3). An ideal approach to this task requires key features such as noninvasiveness, miniaturization, and advanced precision. Specifically, it should achieve spatial resolution on the order of a few hundred micrometers and be adaptable to the complex and heterogeneous morphologies of brain subregions (4, 5). For example, ocular dominance columns (ODCs) in humans exhibit an elongated structure spanning multiple cortical layers over 2 to 3 mm, with a mean width of only 863 μm (5). In macaque monkeys, ODCs are even narrower, with widths ranging from 400 to 700 μm, posing significant challenges for precise targeting (6, 7). In addition, the interleaved organization of ODCs corresponding to the left and right eyes introduces further complexity, as off-target stimulation could disrupt decoding of these functional subregions (6). These intricate anatomical and functional characteristics highlight the critical need for stimulation tools capable of precise volumetric control to accurately target specific brain subregions while minimizing the risk of activating adjacent structures.

Current neuromodulation tools have achieved precise control over the stimulation volume. Deep brain stimulation (DBS), the gold standard in neuromodulation for decades, is widely used in the clinical treatment of Parkinson’s disease and tremors (8–10). DBS uses current steering techniques with directional leads comprising radially segmented electrodes, offering superior targeting of nonspherical brain regions and precise control over the volume of tissue activation (VTA) to improve therapeutic outcomes (11, 12). To mitigate DBS vulnerability to heterogeneous tissue properties like impedance mismatch, computational models evaluate electrode configurations (13) and multiset steering effects (14). Despite these advancements, DBS remains invasive, and its VTA in human brains is still on the millimeterscale. Optogenetics has emerged as a powerful neuromodulation technology (15–17), enabling cell type–specific modulation of neural circuits, including the selective activation of individual ODCs in nonhuman primates (18). However, its broader application faces several limitations: (i) Accessibility is largely limited by the complexity of the animal model, viral vector design and handling, and high costs; (ii) effective implementation requires long incubation periods (\~3 months) following viral vector injection (19); (iii) limited light penetration into brain tissue results in \~99% absorption at a depth of 0.9 mm, generating heat and posing risks of thermal side effects (17, 19); and (iv) incomplete stimulation of elongated structures such as ODCs, which span 2 to 3 mm. Although depth-specific, multisite optical probes have been developed to target deeper brain regions (20), invasive fiber-based delivery of photons is needed.

Noninvasive neuromodulation techniques such as transcranial direct current stimulation (21) and transcranial magnetic stimulation (22) suffer from poor spatial resolution, ranging from several millimeters to centimeters. Transcranial focused ultrasound (tFUS), in contrast, offers superior resolution on the order of a few millimeters at frequencies below 1 MHz, enabling efficient transcranial penetration (23, 24). Its functional efficacy has been demonstrated on mice, monkeys, and humans (25–29). tFUS also allows control over the VTA through acoustic lenses (30) or two-dimensional (2D) arrays (31, 32). However, acoustic lenses introduce additional interfaces that compromise acoustic energy delivery, while 2D arrays require complex engineering for precise multichannel control over timing and amplitude to shape wavefronts. Moreover, the bulkiness and rigidity of current ultrasound arrays limit their portability, limiting their use as wearable devices for awake animal studies or clinical applications (33).

Optoacoustic neuromodulation is an emerging technique that offers a promising alternative for ultrasound neural stimulation, providing enhanced spatial resolution and greater flexibility in waveform

1 Department of Electrical and Computer Engineering, Boston University, Boston, MA 02215, USA. 2 Department of Radiology, Brigham and Women’s Hospital, Harvard Medical School, Boston, MA 02115, USA. 3 CEC S–Center for Engineering, Modeling and Applied Social Sciences, Federal University of ABC (UFABC), São Bernardo do Campo, SP 09606405, Brazil. 4 Department of Biomedical Engineering, Boston University, Boston, MA 02215, USA. 5 Division of Materials Science and Engineering, Boston University, Boston, MA 02215, USA. 6 Department of Chemistry, Boston University, Boston, MA 02215, USA. \*Corresponding author. Email: jxcheng@bu.edu (J.-X.C.); cheyang@bu.edu (C.Y.)

engineering (34). This technique leverages pulsed laser–induced ultrasound waves by using a combination of light-absorbing materials and a thermally expandable medium. When coated onto optical fibers, this composite forms a point ultrasound source capable of achieving subcellular resolution (35–37). Furthermore, the use of soft materials allows for the fabrication of high–numerical aperture curvatures, mitigating the cracking risk due to the mechanical rigidity of conventional piezoelectric transducers. This advantage surpasses the performance of traditional acoustic lenses by enabling spatial resolutions closer to the theoretical diffraction limit at a given frequency, without requiring higher frequencies that would compromise transcranial penetration (38).

Here, we introduce an optically generated Bessel beam ultrasound (OBUS) device—a miniaturized, noninvasive, and nongenetic neuromodulation tool. OBUS incorporates two key innovations: (i) The use of a Bessel beam ultrasound enables OBUS to achieve volumetric tar geting of column-shaped brain subregions, such as ODCs, and offers superior transcranial ability compared to conventional Gaussian beam. (ii) The use of optically generated ultrasound enables significant miniaturization, resulting in a compact device with a footprint of 2.33 mm in diameter and a weight of just 2.1 mg. The device is fabricated by embedding candle soot (CS) nanoparticles in polydimethylsiloxane (PDMS) at an 8:1 polymer-to-curing agent ratio, optimized for a high optoacoustic conversion efficiency. Upon nanosecond laser illumination, OBUS produces an elongated acoustic field with a lateral resolution of 152 μm and an axial resolution of 1.93 mm, enabling precise volumetric stimulation. Simulations using rat skull models demonstrate OBUS’s ability to maintain beam shape and intensity during transcranial propagation, outperforming conventional Gaussian beams. Immunofluorescence validates OBUS’s capability to stimulate cortical layers up to 2.1 mm depth in the mouse brain. Electrophysiological recording and functional magnetic resonance imaging (fMRI) recorded robust neural and hemodynamic responses elicited by OBUS in rodent brains, showcasing its capacity to modulate neural circuits in intact brains. Safety evaluations confirm compliance with mechanical and thermal thresholds in vivo. OBUS represents a substantial tool advancement for noninvasively studying brain function and neural circuits, offering opportunities to explore complex neural circuits and contribute to future neuromodulation research and clinical applications.

## RESULTS

## Design of OBUS

To effectively target elongated brain subregions such as ODCs, we adopted the Bessel beam concept to optically generate a Bessel beam ultrasound field using an optoacoustic device. This approach is designed to achieve both an elongated VTA and high transcranial efficiency simultaneously for noninvasive brain stimulation (Fig. 1A). The OBUS is illuminated by an optical fiber aligned through a 3Dprinted adapter ensuring uniform laser illumination. When positioned on the skull, OBUS generates an elongated ultrasound field that penetrates the skull and reaches the targeted brain region.

To generate the acoustic Bessel beam, a conical optoacoustic emit ter surface, analogous to an axicon lens, was used to generate a zerothorder Bessel beam propagating along the axial direction (Fig. 1B). Two critical parameters of an elongated acoustic focus used for brain stimulation are the depth of focus (DOF) and the peak pressure position, which corresponds to the VTA length and the region where the highest acoustic energy is delivered, respectively. The DOF can be precisely tuned by adjusting the radius (R) and angle (θ) of the conical optoacoustic surface, as defined by the governing equation

$$
\mathrm{DOF} = \frac {R}{\tan (\theta)} \tag {1}
$$

To determine the optimal R and θ values for positioning the peak pressure at the desired VTA depth, we conducted simulations based on four criteria for effective brain stimulation: (i) We decided to demonstrate OBUS in rodents due to resource accessibility, targeting a lateral resolution ≤0.35 mm to enable brain mapping in the mouse model (39); (ii) we ensured that the DOF was shorter than the depth of the mouse brain, which is \~6 mm; (iii) we aimed to position the maximum point of the field deeper than 1.5 mm beneath the skin to target the cortical layer of the brain; (iv) we miniaturized the OBUS to have a diameter of <4 mm (approximately half the width of a mouse brain) to facilitate ease of manipulation and enable potential multisite stimulation.

To satisfy the outlined criteria, we selected an R value of 1.165 mm. We then simulated the acoustic field generated by OBUS using a 1.165-mm radius with conical angles of 10°, 15°, 18°, 20°, and 30°. The simulations used a central frequency of 15-MHz central frequency with a 200% bandwidth based on previous work (38). Water was chosen as the propagation medium, with material-specific acoustic speed and density values applied accordingly. The simulation results are summarized in Table 1. Although the DOF and axial resolution are proportionally related, axial resolution more accurately represents the effective stimulation region, as the ultrasound intensity near the DOF edges is relatively low. Therefore, we used axial resolution instead of DOF in subsequent analyses. On the basis of the simulation, a conical angle of 15° and an overall device diameter of 2.33 mm satisfied the criteria for lateral resolution, axial resolution, and maximum pressure position. The optimal simulated acoustic field using these parameters is shown in Fig. 1C.

Our previous work on a soft optoacoustic pad has shown that miniaturization through reducing the diameter while maintaining the same laser density reduces ultrasound intensity at the focus, limiting its potential for further miniaturization (38). In contrast, through simulation, we confirmed that the diameter of OBUS primarily affects the axial resolution but not the maximum intensity along the zero-order beam. Simulations confirm that OBUS with diameters from 12.2 to 2.33 mm deliver consistent peak intensities, as shown in fig. S1. OBUS diameter designed according to desired axial resolution can output consistent maximum acoustic intensity, making OBUS well suited for miniaturized transcranial neuromodulation applications.

## Characterization and optimization of OBUS optoacoustic efficiency

To fabricate the OBUS with a 15° conical angle, a steel rod mold with an axicon tip was machined. After coating the metal cone with CS, the CS layer was transferred into PDMS and cured to form the OBUS device (fig. S2). However, initial designs with a sharp conical tip led to heat accumulation and thermal damage of OBUS under high laser energy. To address this issue, the mold tip was polished to a slightly rounded shape. All references to OBUS refer to this optimized rounded-tip design.

The OBUS prepared has a diameter of 2.33 mm (Fig. 1D, inset) and is ultralight, weighing only 2.1 mg. With the addition of the 3Dprinted adapter, the total weight is 167.6 mg. This lightweight design highlights the potential of OBUS as a wearable device, providing its potential advantage over conventional ultrasound transducers for use in freely moving animals.

A  
![](images/ccb0e10a2719cafa0a202e93e2ca181c50be425cdef49b4b7b3c805921b9f38a.jpg)

<details>
<summary>text_image</summary>

Laser pulse
Fiber
Adaptor
OBUS
Ultrasound
</details>

B  
![](images/f7f5106b83b3a33ff6b445b4a42e45e338303555beae025457f3fc90663b6fb0.jpg)

<details>
<summary>text_image</summary>

R
θ
Depth of focus (DOF)
</details>

C  
![](images/a1d011f2d9d2589a64402060c608d50b78f9ec7d61d213eb5bfc2b8ffc0f7547.jpg)

<details>
<summary>heatmap</summary>

| Z position (mm) | X position (mm) | Value |
| --------------- | --------------- | ----- |
| -1              | -1              | 0     |
| -1              | 0               | 0     |
| -1              | 1               | 0     |
| 0               | -1              | 0     |
| 0               | 0               | 8     |
| 0               | 1               | 8     |
| 0               | 2               | 6     |
| 0               | 3               | 4     |
| 0               | 4               | 2     |
| 1               | -1              | 0     |
| 1               | 0               | 0     |
| 1               | 1               | 0     |
| 1               | 2               | 0     |
| 1               | 3               | 0     |
| 1               | 4               | 0     |
| 2               | -1              | 0     |
| 2               | 0               | 0     |
| 2               | 1               | 0     |
| 2               | 2               | 0     |
| 2               | 3               | 0     |
| 2               | 4               | 0     |
| 3               | -1              | 0     |
| 3               | 0               | 0     |
| 3               | 1               | 0     |
| 3               | 2               | 0     |
| 3               | 3               | 0     |
| 3               | 4               | 0     |
| 4               | -1              | 0     |
| 4               | 0               | 0     |
| 4               | 1               | 0     |
| 4               | 2               | 0     |
| 4               | 3               | 0     |
| 4               | 4               | 0     |
</details>

D  
![](images/42e015b55edc6546a2c4416ad2974518ece761fa0e6c63f0288d5f679b7901e6.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Acoustic pressure (MPa) | Normalized power (dB) |
| --------- | ------------------------ | --------------------- |
| 0.0       | -2.0                     | -30                   |
| 0.5       | 1.5                      | -10                   |
| 1.0       | -0.5                     | -20                   |
</details>

E  
![](images/3e615be4a55b0807554dc02d21fc8dfdd64d62f708c6ae89e048f9be3189f7cc.jpg)

<details>
<summary>line chart</summary>

| Lateral profile (r) | Amplitude (mV) |
| ------------------- | -------------- |
| -0.4                | 0              |
| -0.3                | 20             |
| -0.2                | 50             |
| -0.1                | 80             |
| 0.0                 | 120            |
| 0.1                 | 80             |
| 0.2                 | 50             |
| 0.3                 | 20             |
| 0.4                 | 0              |
</details>

F

![](images/8fd1e31dc9ca81789e2065d8ba07587a7b181e5eb22d5bb0426ad3918f866221.jpg)

<details>
<summary>line chart</summary>

| Axial profile (mm) | Amplitude (mV) |
| ------------------ | -------------- |
| 0                  | 30             |
| 1                  | 60             |
| 2                  | 105            |
| 3                  | 60             |
| 4                  | 30             |
</details>

G  
![](images/8b9a1d186ee108cc2cfb1b6a4c631766b98848c5f9026ddfc78983986a063bd5.jpg)

<details>
<summary>scatterplot</summary>

| Weight ratio of base to curing agent | Normalized amplitude (a.u.) |
| ----------------------------------- | ---------------------------- |
| 2:1                                 | 0.3                          |
| 4:1                                 | 0.8                          |
| 6:1                                 | 1.0                          |
| 8:1                                 | 0.7                          |
| 10:1                                | 0.9                          |
</details>

Fig. 1. Design of OBUS and characterization of the acoustic field generated. (A) Schematic illustration of the OBUS device for noninvasive brain stimulation in rodents. Created in BioRender. Li, Y. (2026) https://BioRender.com/sq958rf. (B) Schematic of OBUS device and the resulting acoustic field. Key parameters are highlighted. (C) Simulated acoustic field generated by OBUS with a conical angle of 15°. (D) Acoustic waveform and corresponding frequency spectrum recorded at the peak pressure location. Inset: Photo of the OBUS device. Scale bar, 2 mm. (E) Lateral profile of the acoustic field generated by OBUS. (F) Axial profile of the acoustic field generated by OBUS. (G) Optoacoustic signal intensity as a function of the PDMS base-to-curing agent weight ratio. a.u., arbitrary units.

Table 1. Comparison of acoustic field generated by OBUS with various conical angles. Lateral and axial resolutions are based on simulation and defined by the full width at half maximum of the pressure profile along x and z directions. DOF is calculated on the basis of Eq. 1.

<table><tr><td>Conical angle θ</td><td>Lateral resolution (mm)</td><td>Axial resolution (mm)</td><td>DOF (mm)</td><td>Maximum pressure position (mm)</td></tr><tr><td>10°</td><td>0.30</td><td>6.60</td><td>6.61</td><td>3.21</td></tr><tr><td>15°</td><td>0.33</td><td>4.49</td><td>4.35</td><td>2.06</td></tr><tr><td>18°</td><td>0.24</td><td>3.34</td><td>3.59</td><td>1.48</td></tr><tr><td>20°</td><td>0.21</td><td>3.06</td><td>3.20</td><td>1.14</td></tr><tr><td>30°</td><td>0.12</td><td>1.88</td><td>2.02</td><td>0.50</td></tr></table>

To characterize the optoacoustic properties, a laser with a wavelength of 1064 nm, a pulse width of 2.2 ns, and a fluence of 61 μJ/mm2 was delivered to OBUS, generating a peak-to-peak pressure of 4.1 MPa at a distance of 2 mm from the OBUS surface (Fig. 1D). The frequency spectrum of the waveform, calculated using fast Fourier transform (FFT), revealed a central frequency of 10.6 MHz and a −6-dB bandwidth of 250% (5 to 30 MHz). In Fig. 1 (E and F), spatial profiling of OBUS was conducted using a needle hydrophone, yielding lateral and axial resolutions of 152 μm and 1.93 mm at the focal point’s full width at half maximum (FWHM), confirming the creation of an elongated acoustic field.

To optimize optoacoustic conversion efficiency, we measured the peak-to-peak pressure generated by OBUS using various PDMS prepolymer to curing agent weight ratios. Previous studies have shown that the weight ratio of PDMS prepolymer to curing agent affects the Young’s modulus E of pure PDMS (40). According to optoacoustic principles, the initial pressure p0 generated in the material is directly proportional to the Gruneisen parameter Γ

$$
p _ {0} = \Gamma \cdot \mu_ {\mathrm{a}} \cdot F \tag {2}
$$

where $\mu _ { \mathrm { a } }$ is the absorption coefficient, and F is the optical fluence. The Gruneisen parameter Γ is proportional to the bulk modulus K in solid materials

$$
\Gamma = \frac {\beta}{\rho C _ {\mathrm{v}} \kappa} = \frac {\beta K}{\rho C _ {\mathrm{v}}} \tag {3}
$$

where β is the thermal coefficient of volume expansion, ρ is the mass density, $C _ { \mathrm { v } }$ is the principal heat capacity at a constant volume, and κ is the isothermal compressibility. The bulk modulus K is further proportional to Young’s modulus E

$$
K = \frac {E}{3 (1 - 2 \nu)} \tag {4}
$$

where ν representing the Poisson’s ratio. Since the CS-embedded PDMS in OBUS is a composite material, we experimentally evaluated the impact of varying the weight ratio on optoacoustic conversion efficiency. OBUS was fabricated at weight ratios of 2:1, 4:1, 6:1, 8:1, and 10:1 to assess their impact on peak-to-peak pressure under identical laser energy conditions. As shown in Fig. 1G, the 8:1 ratio produced the highest acoustic amplitude, indicating optimal optoacoustic efficiency. This 8:1 ratio was used for the final characterization (Fig. 1, D to F) and subsequent experiments.

## Transcranial efficiency and VTA maintenance of OBUS after skull aberration

To assess the transcranial capability of OBUS, we simulated and com pared its focus retention through a rat skull with that of a Gaussian beam. Simulations instead of experimental testing were used here for the comparison, as simulation enables a direct comparison, under the same ultrasound central frequency, identical bandwidth, and the same targeting focal depth while these are not available experimentally. In the simulation, a real profile of a rat skull was scanned by ultrasound and imported, along with the OBUS profiles. A curved surface was designed to generate the Gaussian beam. By varying the diameters of the devices, both OBUS and Gaussian beams were designed to focus at a 4.8-mm depth, corresponding to the rat thalamus. This brain region was chosen for two reasons: First, it aims to maximize differences in outcomes and demonstrate OBUS’s ability to target deeper brain regions while preserving the desired shape. Second, the thalamus is a well-established target in brain studies due to its influence on cortical functions (41).

We set both fields to a central frequency of 10 MHz with a 250% bandwidth, based on experimental data measured from OBUS. Water served as the propagation medium. Simulations of acoustic fields with and without the skull in place are shown in Fig. 2 for analysis. As shown in Fig. 2A, the presence of the skull induced aberrations in both OBUS and Gaussian beams. Figure 2B shows that both focal points shifted 0.5 mm closer to the skull due to its high acoustic impedance. For a more intuitive and direct interpretation of acoustic attenuation, Fig. 2 was also replotted using a unified scale across all four conditions, as shown in fig. S3. For reference, the simulation results of a standard acoustic Bessel beam are provided in fig. S4.

To further characterize the acoustic fields, we quantified the energy distribution of the OBUS field shown in Fig. 2A. We first calculated the total integrated acoustic intensity after transmission through the skull, followed by the integrated intensity within the focal region defined as the area where the intensity exceeded half of the maximum value. Under this criterion, the focal region of OBUS contained 11.35% of the total postskull acoustic energy. For comparison, the Gaussian beam yielded a focal region energy fraction of 5.93%, indicating that OBUS produces substantially less off-target energy deposition. We additionally examined the lateral profiles at the intended focal point and at positions up to 2.5 mm anterior to it, with 0.5-mm increments, as shown in Fig. 2C. In the transcranial profiles, OBUS maintained an elongated focus after penetrating the skull, with a side lobe appearing immediately postpenetration. In contrast, the Gaussian beam exhibited a broad profile extending between 4.25 and 5.25 mm along the z axis, with an intensity remaining above −6 dB relative to the peak. This suggests that in transcranial neuromodulation with the Gaussian beam, tissue along the propagation path may receive exposure levels comparable to those at the intended target, potentially leading to unintended effects and excessive heat deposition. Conversely, OBUS demonstrated a well-defined VTA, maintaining the designed focal region while minimizing exposure to surrounding areas. These results underscore OBUS’s capability for precise neuromodulation with reduced off-target effects in deep-brain transcranial applications.

To quantify VTA maintenance, we calculated the ratio between simulated peak intensity after and before skull penetration to assess transcranial efficiency. We also measured axial and lateral resolutions pre- and postskull penetration, defined as the FWHM values, and calculated the fold change for comparison. Table 2 summarizes these results: OBUS achieved a transcranial efficiency of 18.7%, surpassing the Gaussian beam by 70%. In addition, OBUS showed only a 1.76-fold axial change, whereas the Gaussian beam experienced a marked 5.67-fold change. Similarly, the fold change in lateral resolution for OBUS was 74% of that observed in the Gaussian beam. These findings underscore OBUS’s superior ability to preserve VTA, enabling precise neuromodulation while minimizing unintended exposure. This underscores its potential for targeted transcranial applications. The corresponding data for the standard acoustic Bessel beam are provided in table S1.

## Elongated stimulation volume delivery in vivo with OBUS

To evaluate OBUS’s ability to induce cellular responses with a targeted VTA in vivo, we used c-Fos immunofluorescence staining. c-Fos has been widely used as a marker of neural activation following repeated stimulation. We conducted in vivo stimulation in adult C57BL/6J mouse (N = 3 mice), exposing the skull and applying ultrasound gel for optimal acoustic coupling (Fig. 3A). Using stereotaxic coordinates [anteroposterior (AP): −0.5, mediolateral (ML): 1.5], we aligned the ultrasound focus with the motor cortex, maintaining a 0.5-mm gel gap between OBUS and the mouse head to prevent heat accumulation on the tissue. The OBUS used in vivo was fabricated with the same $1 5 ^ { \circ }$ conical angle as the device modeled in Fig. 2. For stimulation, OBUS was operated with a laser fluence of 68 μJ/mm2 , corresponding to a peak-to-peak pressure of 4.6 MPa at the focus, delivering 3000-pulse trains every 12 s for a duration of 30 min (Fig. 3B). Following stimulation, the mice rested for 1 hour to facilitate peak c-Fos expression. Subsequently, the brains were extracted, fixed, and sectioned horizontally for VTA measurement and immunofluorescence analysis. To aid stimulation site identification, extracted brains were punctured at Bregma and the contralateral untreated side (fig. S5).

A  
![](images/63c06f6e652f603004d044dad62956892ee6177532689697ee5cca03282c4b0e.jpg)

<details>
<summary>heatmap</summary>

| Panel | Description                     | Value |
|-------|---------------------------------|-------|
| A     | OBUS field                       | 25    |
| A     | OBUS penetrate skull            | 10    |
| A     | Gaussian field                   | 25    |
| A     | Gaussian penetrate skull         | 10    |
| B     | OBUS field                       | 25    |
| B     | OBUS penetrate skull            | 10    |
| B     | Gaussian field                   | 25    |
| B     | Gaussian penetrate skull         | 10    |
</details>

B  
![](images/b9816ed807809b4bbd495c7a370a4d88bd6555619f2f6903cb2d8935e3b464c2.jpg)

<details>
<summary>line chart</summary>

| Axial profile (mm) | Amplitude (a.u.) |
| ------------------ | ---------------- |
| 0                  | 0                |
| 1                  | 4                |
| 2                  | 3                |
| 3                  | 10               |
| 4                  | 15               |
| 5                  | 20               |
| 6                  | 25               |
| 7                  | 20               |
| 8                  | 15               |
| 9                  | 10               |
| 10                 | 8                |
| 11                 | 6                |
| 12                 | 4                |
| 13                 | 2                |
| 14                 | 1                |
| 15                 | 0                |
</details>

![](images/cc2de90dcd4648546c5cf135d07d561efa27242ad2ea63d8e9cbf747b6097692.jpg)

<details>
<summary>line chart</summary>

| Lateral profile (mm) | Z position (mm) | Amplitude (a.u.) |
| --------------------- | --------------- | ---------------- |
| -2                    | 6.25            | 0                |
| -1                    | 6.25            | 2                |
| 0                     | 6.25            | 4                |
| 1                     | 6.25            | 6                |
| 2                     | 6.25            | 8                |
| 4.25                  | 6.25            | 10               |
| 5.25                  | 6.25            | 12               |
| 6.25                  | 6.25            | 14               |
</details>

Fig. 2. Comparison of simulated acoustic fields between OBUS and Gaussian beam ultrasound. (A) Simulated acoustic fields of OBUS and Gaussian beam ultrasound without and with interacting with the rat skull. Black dashed lines, the surface of the emitters; pink regions, the rat skulls. (B) Axial profile of the maximum pressure along the propagation direction. Black dashed lines, the surface of the emitters; pink rectangular, the position of the rat skull. Blue, red, yellow, purple, green, and light blue dashed lines, the positions for the lateral profiles in (C). (C) Lateral profiles of the acoustic field at six positions: the intended focus and five preceding slices at 0.5-mm intervals.

Table 2. Summary of transcranial efficiency on peak intensity and changes in axial and lateral resolution before and after skull penetration for OBUS and Gaussian beam ultrasound. Lateral and axial resolutions are defined by the full width at half maximum of the pressure profile along x and z directions. Fold change is defined as the ratio of with skull data to without skull data.

<table><tr><td>Performance parameters</td><td>OBUS</td><td>Gaussian beam</td></tr><tr><td>Peak intensity transcranial efficiency</td><td>18.7%</td><td>11.0%</td></tr><tr><td>Axial resolution (mm)—without skull</td><td>6.48</td><td>1.05</td></tr><tr><td>Axial resolution (mm)—with skull</td><td>11.43</td><td>5.95</td></tr><tr><td>Fold change in axial resolution</td><td>1.76</td><td>5.67</td></tr><tr><td>Lateral resolution (mm)—without skull</td><td>0.20</td><td>0.10</td></tr><tr><td>Lateral resolution (mm)—with skull</td><td>0.93</td><td>0.63</td></tr><tr><td>Fold change in lateral resolution</td><td>4.63</td><td>6.25</td></tr></table>

To confirm cellular activation, we performed 4o,6-diamidino-2- phenylindole (DAPI) and c-Fos staining and conducted confocal imaging of both markers at various depths (figs. S6 to S8). Brain slices were analyzed with the brain surface as the reference point to determine the depth of the VTA. Brain slices shallower than 1.1 mm were excluded from analysis, as they either fell outside the OBUS field or contained the stimulation site near the edge, making data collection impractical. Some tissue damage was observed at the edges of the brain slices due to cuts during extraction. Representative images at 1.4 mm (Fig. 3C) and 1.7 mm (Fig. 3D) showed concentrated signals at the targeted region. The stimulated site exhibited strong c-Fos signals, while the contralateral control side showed minimal signal. Overlay images confirmed the colocalization of c-Fos (green) and DAPI (magenta) as white signals, indicating cellular activation specifically induced by OBUS stimulation.

A  
![](images/27417e4a48ab16970042d9ac8b83a63c87c2532fb21b8d4d7e85205898f7a05b.jpg)

<details>
<summary>text_image</summary>

OBUS
</details>

B

![](images/6dc7d39c7af5ced6e3daaa9ac1b84101c491aa84c890ecc28c54b9b41f3cc975.jpg)

<details>
<summary>text_image</summary>

Sonication duration, 30 min
Pulse train, 3 s
... Interval, 12 s
3000 pulses at 1-kHz PRF
</details>

E  
![](images/7b140fd312045d6f267d33b7ea7e185470a24ffba960dbcda3ace921cf82652d.jpg)

<details>
<summary>box plot</summary>

| Depth (mm) | Stimulated | Control |
| ---------- | ---------- | ------- |
| 1.3        | 0.3        | -0.1    |
| 1.4        | 0.3        | -0.1    |
| 1.5        | 0.3        | -0.1    |
| 1.6        | 0.3        | -0.1    |
| 1.7        | 0.3        | -0.1    |
| 1.8        | 0.2        | -0.1    |
| 1.9        | 0.2        | -0.1    |
| 2.0        | 0.2        | -0.1    |
| 2.1        | 0.1        | -0.1    |
| 2.2        | 0.1        | -0.1    |
</details>

C  
![](images/60060fab27d7f624244bea14e357dedd603be2838d42dc876d128bb0cfe263a1.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing two green-stained biological structures with scale bars (2 mm and @1.4 mm), no text or symbols present.
</details>

Control side  
![](images/e76909f835c7b9b8a4f91348f7b45f324ceb2dec9b9c255756edbf5861c416e6.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing green fluorescent particles with a 100 μm scale bar (no text or symbols beyond scale indicator)
</details>

Merged control  
![](images/25bb9a152b821177cbdad4576d1dae9c8c65b00a0e2b421a66ced656fe835a39.jpg)

<details>
<summary>text_image</summary>

DAPI
c-Fos
Overlap
</details>

Stimulated site  
![](images/5a12816bd64e581ef483d29f1e932f7b51950c08effff58b9a5a515630155a23.jpg)

<details>
<summary>natural_image</summary>

Green fluorescent microscopic image showing cellular or particulate structures (no text or symbols visible)
</details>

Merged stimulated  
![](images/dbc5a71e903fb0d6296ca09d9e9726bd9263805617eae028147fc6bfa9384fd2.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of green fluorescent cells with purple nuclei (no text or symbols)
</details>

D  
![](images/8abcb51c7f1b72ac80f6ac1f22db6fbf7fcbe3938d98039ded52ce429a05b373.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image of a brain with green staining, showing two highlighted regions (red and blue squares) and a scale marker at 1.7 mm (no text or symbols beyond measurement)
</details>

![](images/d6dc29c38cbbe013d215f24fac6e70934e2d507c1db3cd3dca3a51e0b5e51e39.jpg)

<details>
<summary>natural_image</summary>

Solid green textured background with no visible text, symbols, or distinct features
</details>

![](images/d12bcc72e4b4085ec4d713bd8def90eb32cea521d9fb05d9945b160426bdf2e8.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of purple and green cellular structures (no text or symbols)
</details>

![](images/a07e190f2f260ddd1602ea84a54ba72bf5bf085986c552759ee27fb9552044a3.jpg)

<details>
<summary>natural_image</summary>

Green textured surface with scattered bright spots, no visible text or symbols
</details>

![](images/432cc1da850c93bbe23f3f518906de352ceb6a01bcdb216baa914686f4a56597.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of purple and green fluorescent particles on a dark background (no text or symbols)
</details>

Fig. 3. Elongated stimulation volume delivery in vivo with OBUS. (A) Schematic of the experimental setup for OBUS stimulation. Created in BioRender. Li, Y. (2026) https://BioRender.com/wfs0r32. (B) Schematic representation of the pulse train delivered to induce c-Fos protein expression. PRF, pulse repetition frequency. (C and D) Representative images of the brain slice at 1.4 and 1.7 mm, respectively. (E) Comparison of Pearson’s coefficient between stimulated site and control sites at different depths (N = 3 mice, n = 9 sites). Position 0 mm is at the surface of OBUS. $^ { * * } P \leq 0 . 0 1 . ^ { * * * } P \leq 0 . 0 0 1$ .

For quantitative depth analysis of the VTA, ImageJ software was used to perform unbiased colocalization analysis for c-Fos and DAPI signals through automated image thresholding and calculation of the Pearson’s correlation coefficient, which ranges from −1 (negative correlation) to 1 (positive correlation). Slight misalignments in zoomed images and asymmetry between the stimulated and control groups likely resulted from manual adjustments of the confocal field. To address these issues, three smaller regions of interest (ROIs) were selected within the targeted region in both stimulated and control sites. The following criteria were applied to standardize the selection: (i) avoidance of vessels, which were identified by their larger size relative to nuclei to prevent overestimation of colocalization; (ii) ensuring overlap with the targeted site (white dashed circle in figs. S6 to S8); and (iii) maintaining symmetry between ROIs at stimulated and control sites, as indicated by yellow boxes in figs. S6 to S8. A Mann-Whitney U test was performed to compare Pearson’s coefficients at various depths, with results shown in Fig. 3E. Notably, sig nificant differences in Pearson’s coefficient between the stimulated and control groups were observed up to a depth of 2.1 mm.

When an additional 0.6 mm was added to accounted for the gap of ultrasound gel to the 2.1-mm depth, the decay pattern of the c-Fos signal closely matched the axial acoustic profile, with the Pearson’s coefficient for the c-Fos signal peaking at 2.2 mm and gradually decaying to 2.8 mm (fig. S9). The axial acoustic profile measured by the hydrophone (Fig. 1F) peaked around 2 mm and decayed to 40% at 3 mm. This alignment confirmed that the depth of the c-Fos signal corresponded to the OBUS VTA.

## Electrophysiological responses induced in vivo by OBUS

After confirming OBUS’s ability to target the VTA through c-Fos staining, we evaluated its potential to elicit localized electrophysiological responses in vivo in C57BL/6J mice. Craniotomy was performed on anesthetized mice, and OBUS was aligned with the somatosensory cortex at stereotaxic coordinates (AP: −1.5, ML: 2). A 3D-printed pointer indicated the VTA lateral center, ensuring precise alignment with the recording electrode (fig. S10). A 16-channel electrode (NeuroNexus) was then accurately inserted into the brain using a 3D stereotactic frame (Fig. 4A). To minimize heat accumulation, OBUS was placed \~0.5 mm away from the brain surface.

For neuromodulation experiments in mice, OBUS was applied at peak-to-peak pressures of 2.8, 3.7, and 4.1 MPa with a 1-kHz pulse repetition frequency. Each stimulation consisted of a 10-s pulse train followed by a 20-s rest period within a 1-min cycle. Electrophysiological recordings lasted 3 min, comprising 1-min baseline before stimulation, 1 min during OBUS stimulation, and 1 min after stimulation (Fig. 4B). Each pressure level was tested in four mice (N = 4). Raw signals were recorded using cortical electrodes, and local field potentials (LFPs; 0.5 to 100 Hz) were extracted for analysis.

A  
![](images/94e7bf45f2d96655ea26c348d862429e212f47e0023d98c4fab6f3d7eee44f21.jpg)

<details>
<summary>text_image</summary>

Electrode
OBUS
</details>

B  
![](images/226fce80f50bb3a6d69ce8394afcbc46e012d81a3095df5138a9749a3a5215a8.jpg)

<details>
<summary>text_image</summary>

Before, 1 min
OBUS modulation, 1 min
After, 1 min
Pulse train, 10 s
Interval, 20 s
</details>

10k pulses at 1-kHz PRF

C  
![](images/e06f48555d67106581b464745eb0e5629abd310a412fdf6b3ce185d843a3ba51.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Amplitude (mV) |
| -------- | -------------- |
| 0        | ~0.0           |
| 20       | ~0.0           |
| 40       | ~0.0           |
| 60       | ~0.3           |
| 80       | ~0.0           |
| 100      | ~0.3           |
| 120      | ~0.0           |
| 140      | ~0.0           |
| 160      | ~0.0           |
| 180      | ~0.0           |
</details>

![](images/b2a1da0ec46e63ba4a08e79ee25a75322f8038de5bbc56120e7411d138f85617.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Frequency (Hz) |
| -------- | -------------- |
| 0        | ~0             |
| 20       | ~50            |
| 40       | ~50            |
| 60       | ~50            |
| 80       | ~50            |
| 100      | ~50            |
| 120      | ~50            |
| 140      | ~50            |
| 160      | ~50            |
| 180      | ~50            |
</details>

D  
![](images/4c79f6aec9473e86f02fcdf7d12d27228c40d1cb54b48dc58e901bfa1aebd26e.jpg)

<details>
<summary>line chart</summary>

| Frequency (Hz) | Before | During | After |
| -------------- | ------ | ------ | ----- |
| 0              | -40    | -40    | -40   |
| 50             | -70    | -70    | -70   |
| 100            | -70    | -70    | -70   |
</details>

3.7 MPa  
![](images/9f21cc45c18b2d789dc88b36933a089ce10b9e7b406d0c78ae62f17ad94333b6.jpg)

<details>
<summary>line chart</summary>

| Frequency (Hz) | Before | During | After |
| -------------- | ------ | ------ | ----- |
| 0              | -35    | -35    | -35   |
| 50             | -65    | -65    | -65   |
| 100            | -70    | -70    | -70   |
</details>

4.1 MPa  
![](images/2f00f8499b3a59b12b154a92e330cc06452e77e884b3aa764cf0f0fd45e3b6a8.jpg)

<details>
<summary>line chart</summary>

| Frequency (Hz) | Before | During | After |
| -------------- | ------ | ------ | ----- |
| 0              | -35    | -35    | -35   |
| 50             | -70    | -70    | -70   |
| 100            | -70    | -70    | -70   |
</details>

E  
![](images/e4ce1035b5ffc29f1b237ef9b52bd9b12790f6b3fe914437a4c606a141c19d68.jpg)

<details>
<summary>line chart</summary>

| Frequency (Hz) | Normalized during (dB/Hz) | Normalized after (dB/Hz) |
| -------------- | ------------------------- | ------------------------ |
| 0              | ~0                        | ~0                       |
| 50             | ~0                        | ~0                       |
| 100            | ~0                        | ~0                       |
</details>

![](images/5dacb672bf77bdb413cf1a70e4f302343e2c680e346cc18a300fe58daa73851f.jpg)

<details>
<summary>line chart</summary>

| Frequency (Hz) | Normalized during (dB/Hz) | Normalized after (dB/Hz) |
| -------------- | ------------------------- | ------------------------ |
| 0              | ~0                        | ~0                       |
| 50             | ~3                        | ~2                       |
| 100            | ~0                        | ~0                       |
</details>

![](images/31f942b1fd87444a0454adcd8b319cfa41d9053fad065898cedecddfb1cabf3d.jpg)

<details>
<summary>line chart</summary>

| Frequency (Hz) | Normalized during (dB/Hz) | Normalized after (dB/Hz) |
| -------------- | ------------------------- | ------------------------ |
| 0              | ~0                        | ~0                       |
| 50             | ~2                        | ~2                       |
| 100            | ~0                        | ~0                       |
</details>

Fig. 4. LFP responses induced by OBUS modulation. (A) Schematic of the in vivo OBUS stimulation and recording setup. Created in BioRender. Li, Y. (2026) https://Bio-Render.com/wfs0r32. (B) Schematic representation of the pulse train delivered to stimulate LFP responses. (C) Representative LFP signals and corresponding frequency spectrogram during OBUS stimulation at 4.1 MPa, initiated at t = 60 and 90 s with a 10-s duration. Red bars indicate laser burst timing. (D) Power spectral density (PSD) plots for 2.8, 3.7, and 4.1 MPa (left to right), averaged over three repeats (N = 1 mouse, n = 3 recordings). (E) Normalized PSD plots for 2.8, 3.7, and 4.1 MPa (left to right). The “during” and after PSD values were normalized to “before” and then averaged across three animals (N = 4 mice, n = 11 recordings). Paired t tests were conducted to compare “before versus during” and “before versus after.”

A representative LFP trace and its corresponding spectrogram during 4.1-MPa OBUS stimulation are shown in Fig. 4C, demonstrating increased LFP frequency and amplitude both during and after stimulation. Data from additional trials are provided in figs. S11 to S13. Figure 4D shows the power spectral density (PSD) calculated at each pressure level in one representative mouse. Notably, PSD analysis revealed increased power in the 10- to 50-Hz range at all three pressure levels, corresponding to β and γ bands. Although 2.8 MPa produced the largest PSD increase, high variability was observed, likely due to the limited LFP signal recorded (fig. S11). Two factors contributed to the low recording quality: (i) The animal may not have fully recovered from isoflurane anesthesia at the time of recording, and (ii) the neuron-electrode interface was initially suboptimal following acute probe insertion. In contrast, PSD increases at 3.7 and

4.1 MPa were more consistent and reproducible, with smaller error bars, indicating improved reliability with increasing pressure and optimized recording condition.

Figure 4E shows the normalized PSD (during normalized to be fore and after normalized to before) across all mice (N = 4). A paired t test on raw data (before normalization) at 43.0 Hz revealed no significant difference at 2.8 MPa but significant increases at 3.7 and 4.1 MPa. Poststimulation PSD (“after”) also showed significant elevation compared to baseline at all pressure levels. These results indicate that OBUS effectively modulates neural activity. Higher pressure levels produced more significant increases in brain activity during stimulation; however, the sustained poststimulation effects were consistent across all pressures, suggesting that the persistence of neuromodulatory effects is pressure independent.

To verify that the observed LFP signals were specifically induced by OBUS, we conducted three control experiments. First, we set the laser output to 0 mW to eliminate potential electrical interference. No increase in LFP amplitude or frequency was observed in the sig nal trace (fig. S14A), and no change in the PSD was detected (fig. S14B). These results confirm that the neural responses observed in prior experiments were not artifacts of electrical interference. Second, we repositioned the OBUS transducer to the contralateral side of the S1 cortex and applied stimulation at 4.2 MPa to evaluate whether the responses were mediated by cochlear activation. No significant changes in LFP amplitude or frequency were detected (fig. S15A), and PSD remained unchanged (fig. S15B). Last, we delivered 4 mW of laser power—corresponding to \~1.5% laser leakage—without the OBUS device to confirm that residual light did not directly stimulate the brain. No significant changes in LFP amplitude or frequency were observed (fig. S16A), and the PSD remained unchanged (fig. S16B). These findings indicate that OBUS-induced modulation is spatially localized and results from direct interaction with brain tissue, rather than indirect activation via the auditory pathway.

## Blood oxygenation level–dependent responses elicited by OBUS modulation

To noninvasively confirm the induction of brain activity by OBUS, we monitored the percent change in blood oxygenation level–dependent (BOLD) signal in the somatosensory cortex of rats (N = 2) using fMRI. As shown in Fig. 5A, we conducted a positive control by applying electrical stimulation to the right hind paw for 15 s every minute for seven stimulation blocks, with the OBUS device positioned but inactive. For OBUS stimulation, the device was activated with a peakto-peak pressure of 4.9 MPa at a 1-kHz pulse repetition frequency for 15 s every minute, across seven modulation blocks. The representative time course of the BOLD signals for both conditions are shown in Fig. 5B, which indicates a clear correlation between the stimulus activation and the increase in signal response over time. The BOLD signal maps were obtained as a percent change from the unstimulated baseline and averaged over the stimulation blocks to provide an average signal over the 1-min on/off modulation block. The functional activation maps (Fig. 5C) reveal spatially distinct activation patterns: Electrical stimulation of the right hind paw evoked responses in the left somatosensory cortex, while OBUS stimulation consistently elicited activation directly beneath the device. Both robust positive and negative modulation was observed during OBUS modulation. The averaged data over the stimulation blocks for each rat (Fig. 5D) show that BOLD signals followed both stimulation paradigms, peaking at 15 s and returning to baseline poststimulation. The peak BOLD responses from OBUS were comparable to those from electrical stimulation, indicating that OBUS may serve as an effective alternative neuromodulation method.

## Safety evaluation of in vivo OBUS neural modulation

To ensure the safety of in vivo OBUS stimulation in mice, we evaluated both the mechanical index (MI) and temperature rise associated with the stimulation parameters. The MI quantifies the potential for tissue damage due to rarefactional pressure. For our experiments, we set a peak-to-peak pressure limit of 5 MPa for subsequent animal studies. On the basis of the negative-to-positive peak pressure ratio shown in Fig. 1D, we estimated the negative peak amplitude to be 3.05 MPa, resulting in an MI of 0.93—well below the Food and Drug Administration threshold of 1.9 (42), indicating safe operation at 5 MPa.

To assess thermal deposition, we measured temperature rise in ex vivo brain tissue with a thermocouple positioned at the cortical surface (fig. S17A). Using the highest duty-cycle stimulation pattern used in the in vivo experiments, the measured temperature increase was $2 . 7 6 \pm 0 . 3 5 \ : \mathrm { K }$ (n = 4 measurements) (fig. S17B). Although the temperature rise is substantial, it remains within physiological fluctuation ranges and is not expected to induce thermal damage (43). In summary, OBUS operates within safe limits for in vivo neural modulation, with a low MI and moderate temperature rise during stimulation.

## DISCUSSION

In this study, we designed and developed an OBUS device for noninvasive targeting of column-shaped brain regions. We characterized the spatial profile of the OBUS-generated ultrasound field and demonstrated its enhanced transcranial penetration capability compared to a conventional Gaussian beam–based photoacoustic emitter. This approach enables noninvasive neuromodulation with precise control over the shape of the VTA. Notably, OBUS outperformed conventional Gaussian beams in transcranial applications, as confirmed through simulations using rat skulls. This makes OBUS a more effective neuromodulation technique compared to conventional ultrasound neuromodulation. To validate OBUS’s targeting capability, we performed immunofluorescence imaging for c-Fos protein, revealing a VTA depth of 2.2 mm in mouse brains. In addition, we recorded successful electrophysiological and BOLD responses to OBUS stimulation in mice and rats. We confirmed the device’s safety through MI and temperature rise measurements with the stimulation pattern designed for in vivo experiments. This comprehensive evaluation demonstrates OBUS’s potential as a noninvasive neuromodulation tool with advanced spatial control and safety features.

It should be noted that the c-Fos data in Fig. 3 were acquired using a cranial window rather than a fully transcranial method. We have obtained c-Fos–positive data with an intact skull with another mouse; however, repeated experiments with the intact skull had a lower success rate. In the craniotomy experiments, the VTA identified by the c-Fos–positive region exhibited a lateral profile exceeding 400 μm (stimulated side at 1.1-mm depth; fig. S6), suggesting that stimulation was driven by the entire OBUS beam rather than only the focal area. Given that the lateral width of the OBUS focal area is \~150 μm wide—encompassing only a few neurons—it was difficult to spatially localize activated regions in whole-brain slices. To overcome this limitation, we increased the acoustic pressure to engage the full OBUS beam, allowing us to more reliably identify the stimulated area. As a result, while c-Fos expression serves as a reliable indicator of stimulation depth, it has limited utility for resolving lateral activation patterns. Thus, quantification of the beam profile indi cated a potential 150-μm lateral resolution, and the biological lateral resolution of the VTA requires further experimental validation.

A  
![](images/c8d3970e23d133dbc73efcbb782bc23ec3af855c5b427b64d8507103c0d3c5b7.jpg)

<details>
<summary>text_image</summary>

OBUS off
Electric on
L
R
</details>

![](images/f4a50d90983ff59a558f89759433693e446385a9d3739b8c9a829136820ca3e7.jpg)

<details>
<summary>text_image</summary>

OBUS on
R L
</details>

![](images/e4be769d64c7aaadff4216d7d4ecf1192d25eada34649ecfb295a7a822e89f1d.jpg)

<details>
<summary>natural_image</summary>

Illustration of a cylindrical industrial machine with a blue valve and control panel, no visible text or symbols
</details>

B  
![](images/9bc15cf28ed984831cdc7632f405dc8a1d7c5f74066c0984198a186f8e5cabef.jpg)

<details>
<summary>line chart</summary>

| Time (s) | MRI signal (a.u.) |
| -------- | ----------------- |
| 15       | 41                |
| 75       | 37                |
| 135      | 41                |
| 195      | 37                |
| 255      | 41                |
| 315      | 37                |
| 375      | 41                |
| 435      | 37                |
</details>

![](images/d04eeb42bd38e129c9a8704090d7a2d07fbbb48309bd9f724b9e305005deea03.jpg)

<details>
<summary>line chart</summary>

| Time (s) | MRI signal (a.u.) |
| -------- | ----------------- |
| 15       | 36.5              |
| 75       | 36.0              |
| 135      | 36.8              |
| 195      | 36.2              |
| 255      | 36.5              |
| 315      | 36.8              |
| 375      | 36.5              |
| 435      | 36.0              |
</details>

C  
![](images/37cfff33f5ce38be4f12d97be28164e58db206bf84b70076e5090d50df2363a3.jpg)

<details>
<summary>natural_image</summary>

Medical brain scan images with color-coded intensity scale (no text or symbols)
</details>

![](images/727e6c17a066f9f201c3f36924daf33e641289f81c1285969b60e6343f78963c.jpg)

<details>
<summary>natural_image</summary>

Medical brain scan images with color-coded intensity scale (no text or symbols)
</details>

D  
![](images/047c8a56908f6e939a3552949fb1b807c37d588f1b3eba701f8efdd90d32eba3.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Right - OBUS stimulation | Left - Hind paw stimulation |
| -------- | ------------------------ | --------------------------- |
| 0        | 0.0                      | 0.0                         |
| 5        | -1.2                     | -0.4                        |
| 10       | 0.3                      | 0.5                         |
| 15       | 0.7                      | 0.8                         |
| 20       | 0.6                      | 0.3                         |
| 25       | 0.4                      | 0.1                         |
| 30       | 0.2                      | -0.1                        |
| 35       | -0.1                     | -0.3                        |
| 40       | 0.1                      | 0.0                         |
| 45       | -0.2                     | -0.2                        |
| 50       | -0.3                     | -0.4                        |
| 55       | -0.5                     | -0.3                        |
| 60       | -0.4                     | -0.3                        |
</details>

![](images/1b68efec08c1da393191ce5f84a80a2510517057ef6348c38d05e9798968ceee.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Right - OBUS stimulation | Left - Hind paw stimulation |
| -------- | ------------------------ | --------------------------- |
| 0        | -0.5                     | -1.0                        |
| 5        | -0.8                     | -0.7                        |
| 10       | -1.2                     | -0.9                        |
| 15       | 0.0                      | 1.0                         |
| 20       | 0.5                      | 0.8                         |
| 25       | 1.7                      | 0.9                         |
| 30       | 1.4                      | 0.6                         |
| 35       | 1.0                      | 0.3                         |
| 40       | 0.8                      | 0.1                         |
| 45       | 0.5                      | -0.2                        |
| 50       | 0.3                      | -0.5                        |
| 55       | -0.5                     | -0.8                        |
| 60       | -1.0                     | -1.2                        |
</details>

Fig. 5. fMRI BOLD signal in response to OBUS modulation in the somatosensory cortex. (A) Experimental design showing electrical stimulation applied to the right hind paw (positive control) and OBUS modulation with the device positioned over the cortex. Created in BioRender. Li, Y. (2026) https://BioRender.com/uqyezfo. (B) Representative BOLD signal time courses for both conditions, aligned with the stimulation period. Top: electrical stimulation. Bottom: OBUS modulation. Red dashed lines indicate stimulation onset and duration. (C) Representative functional activation maps averaged across stimulation blocks, illustrating contralateral cortical activation from electrical hind paw stimulation (top) and localized modulation beneath the OBUS (bottom). R, right; L, left. (D) Averaged BOLD responses for individual subjects over stimulation blocks showing consistent temporal dynamics, with signal peaks at 15 s followed by a return to baseline after stimulation ends.

For the stimulation mechanism, in addition to the acoustic radia tion force generated by OBUS, the accompanying temperature increase of 2.76 K may also contribute to the observed neuromodulatory effects. This level of heating is below the threshold for destructive and irreversible damage and lies within the range of physiological temperature fluctuations reported in vivo (43–45). Studies have demonstrated that temperature changes of 1° to 3°C could alter neurophysiological properties and functions, including nerve conduction velocity, synaptic transmission, and memory encoding (46). Notably, several studies have reported inhibitory neural responses at similar levels of temperature elevation (47, 48). Thus, while the primary stimulation mechanism of OBUS is likely acoustic, we acknowledge a potential secondary contribution from mild thermal effects, and thermal and acoustic effects may compound in complex ways. Future investigations using genetically modified models knocking out mechanosensitive or thermosensitive channels will be essential to determine whether ultrasound-induced and thermally induced neuromodulation effects are synergistic or antagonistic.

Optoacoustic technology offers distinct advantages over conventional ultrasound techniques for generating specific acoustic fields, such as Bessel beams. Bessel beams are commonly produced using three methods in traditional ultrasound systems: acoustic lenses (49, 50) or spiral phase plates (51) on a planar ultrasound transducer, acoustic transducer arrays (31), and specialized transducers such as ring arrays (52). However, these methods face inherent limitations. Acoustic lenses, for instance, suffer from energy losses due to reflections at two interfaces, leading to reduced acoustic intensity. This issue is exacerbated when materials with high acoustic impedance mismatches are used. For example, with aluminum, only about 3% of the acoustic energy is transmitted (49, 53). Even lower impedance materials like epoxy still reflect \~20% of incident energy (50). Furthermore, while ultrasound arrays and specialized transducers enable more precise control of the wavefront, they are often complex and require advanced equipment and calibration, limiting their practicality. Optoacoustic modality overcomes many of these challenges by using a direct emitting surface to generate acoustic fields. This approach bypasses the need for intermediate components, such as lenses, reducing energy loss and improving acoustic transmission efficiency. Furthermore, compared to the complexity of transducer arrays and ring transducers, a single-element emitter in optoacoustic systems offers a simpler, more accessible, and cost-effective method for generating the desired VTA for brain research. Last, the photoacoustic approach offers substantial flexibility for wavefront engineering. Off-target neuronal activation could be further minimized through free-form wavefront optimization, in which the ideal photoacoustic emitter geometry is computationally determined for a given skull profile. Such customized emitter shapes can be readily fabricated using 3D printing and molding techniques. This simplicity, combined with its efficiency, makes the optoacoustic modality a practical and innovative solution for creating tailored acoustic fields for neuromodulation.

We selected the Bessel beam for shaping the VTA due to its ad vantageous properties for noninvasive brain stimulation. First, its greater penetration depth, compared to Gaussian beams from conventional curved acoustic surfaces, is ideal for targeting column structures in the brain. Second, the Bessel beam’s self-healing property enables it to recover its shape after encountering small obstacles, such as blood vessels, within the brain’s heterogeneous structure (31). This resilience, combined with OBUS’s superior shape-maintaining capabilities, ensures reliable performance in complex brain environments. Third, simulations showed that Bessel beams maintain focal intensity despite emitter size variations, supporting miniaturization for compact optoacoustic devices. The acoustic intensity of other optoacoustic devices, such as soft optoacoustic pad (SOAP), scales with its size due to the material’s fixed laser energy tolerance (38). In contrast, OBUS maintains consistent intensity despite variations in its DOF. Last, while standard Bessel beams have lower localized intensity than Gaussian beams (54), our polished round tip design combines the strengths of both, increasing peak intensity within the VTA by 51.6% (fig. S3) while extending the beam profile and reducing heat accumulation during skull penetration. These attributes make the Bessel beam, particularly in its modified form, a powerful and practical tool for noninvasive brain modulation.

In comparing OBUS to optogenetics, the latter represents a wellestablished technology with its unparalleled selectivity for stimulating specific brain subregions (18) but presents practical challenges for four reasons. First, optogenetics requires substantial expertise, as viral vector optimization for specific brain regions can be complex and time intensive. Multisite, low-pressure viral injections demand advanced skills and careful training (19). In addition, maintaining cranial windows or implanted lenses on animal skulls requires meticulous care to prevent infections. In contrast, OBUS, an optoacoustic neuromodulation device with a portable laser, is easy to distribute and implement across laboratories, as shown by the successful use of optoacoustic stimulation devices shared with collaborators. Optoacoustic neuromodulation also avoids the need for invasive surgeries and associated cranial maintenance, making it an accessible tool for fundamental research. Second, while optogenetics can require up to 3 months for viral transfection (19), leading to significant delays in animal studies, optoacoustic neuromodulation allows research to start immediately once animals are available, greatly accelerating research timelines and improving workflow efficiency. Third, while blue light in optogenetics retains only 1% of its energy at a depth of 0.9 mm (19), OBUS’s ultrasound-based stimulation reaches a depth of 2 mm, covering brain subregions like the ODC across the cortex’s full thickness (\~2 mm). Last, optogenetic stimulation often involves a \~50% duty cycle, raising thermal accumulation risks. In contrast, optoacoustic neuromodulation applies single ultrasound cycles within microseconds at kilohertz frequencies, yielding a much lower duty cycle and significantly reducing thermal risks. Overall, OBUS provides potential as a miniaturized and light-weighted platform for neural stimulation in freely moving animals with high penetration depth and controllable VTA.

Current OBUS neuromodulation experiments use a diode-pumped solid-state laser (1064 nm, Onda, Bright Solutions), which is compact and portable, making it suitable for future clinical translation. Although relatively high laser power is required to generate sufficient photoacoustic pressure for stimulation, the optical energy is predominantly absorbed by the OBUS device, with measured light leakage below 1.5%. The resulting leakage corresponds to an irradiance of 0.94 μJ/mm2 , which is well below the American National Standards Institute (ANSI) Maximum Permissible Exposure for skin exposure at 1064 nm. Looking ahead to using lower-class, safer laser sources, improving the photoacoustic conversion efficiency of the OBUS is essential. Recent studies have demonstrated that perovskite-based optoacoustic transducers can achieve approximately 6.7-fold higher photoacoustic conversion efficiency (55). We expect that adopting these higher efficient materials in the OBUS could thereby substantially reduce the required laser fluence.

## MATERIALS AND METHODS

## Fabrication of OBUS device

To fabricate the desired conical mold, a steel rod (McMaster-Carr, 8890K1) was machined, and its tip polished into a curved shape to prevent heat accumulation and potential thermal damage to the OBUS tip. The mold was then exposed to a paraffin wax candle flame for 10 to 15 s to achieve a uniform CS coating. Next, the coated mold was immersed in a degassed PDMS mixture with base-to-curing agent ratios of 2:1, 4:1, 6:1, 8:1, and 10:1 to optimize optoacoustic conversion efficiency. The immersion took place within a 2.33-mm-diameter metal mold to ensure precise shaping. Last, the coated mold was cured at 110°C for 15 min to solidify the structure and complete sample formation.

## Characterization of the ultrasound field generated by OBUS

A diode-pumped laser (Onda 1064 nm, Bright Solution) emitting 2.2-ns pulses at a 1064-nm wavelength was used to generate optoacoustic signals with the OBUS. The laser beam was modulated at a

1-kHz repetition rate via a function generator (33220A, Agilent) and a pulse generator (9214-TZ50, Quantum Composers). To minimize laser leakage, an optical chopper was integrated to ensure consistent 1-kHz pulse delivery. Laser coupling was achieved using a 400-μm multimode fiber (FT400EMT, Thorlabs), and the numerical aperture of the output beam was characterized using a complementary metaloxide semiconductor camera (MU1000, Amscope). A custom 3Dprinted adapter was designed to facilitate uniform illumination of the OBUS device.

For ultrasound pressure and waveform characterization, a measurement system comprising a needle hydrophone (NH0040, optimized for 5 to 40 MHz, Precision Acoustics), a submersible preamplifier, and a dc coupler was used. The signal was further amplified using an ultrasonic pulse-receiver (model 5073PR, Olympus) and recorded with a digital oscilloscope (DS4024, Rigol) after four-time averaging. The 40-μm needle hydrophone was used to acquire waveform and pressure data for OBUS samples fabricated with varying PDMS base-to-curing agent ratios. In addition, the hydrophone was mounted on a 3D manipulator to obtain spatial profiles of the OBUS-generated acoustic field.

## Simulation of the ultrasound field generated by OBUS

The ultrasound field generated by OBUS was simulated using the open-source k-Wave toolbox in MATLAB R2021a (MathWorks, MA). The simulation was performed in 2D, leveraging rotational symmetry, and focused solely on acoustic wave propagation, disregarding light absorption and photoacoustic conversion. Material-specific density and acoustic velocity values were assigned accordingly. In the 2D setup, a PDMS block with various surface profiles was positioned at the water-air interface, with water as the propagation medium and air as the backing material, to compute the resulting acoustic field.

To optimize the conical angle before OBUS fabrication, the acoustic wave’s central frequency was set to 15 MHz with a 200% bandwidth according to the previous study (38). To accurately model the acoustic field produced by the tip-polished OBUS, the emitter’s surface profile was extracted from a photograph and imported into the simulation. On the basis of experimental OBUS characterization, the acoustic wave’s central frequency was set to 10 MHz with a 200% bandwidth. To study skull-induced aberrations, a rat skull profile obtained via photoacoustic tomography was incorporated into the simulation.

## In vivo stimulation on mice via OBUS

All experimental procedures adhered to the relevant guidelines and ethical regulations for animal research, as approved by the Institutional Animal Care and Use Committee of Boston University (PROTO201800534). Adult C57BL/6J mice (14 to 16 weeks old) were anesthetized with 5% isoflurane in an oxygen chamber before being secured in a standard stereotaxic frame. Anesthesia was maintained at 1.5 to 2% isoflurane, with depth monitored via the tail pinch reflex. A heating pad was placed beneath the animal to maintain body temperature. The targeted brain region was prepared by removing the fur, and the OBUS device, mounted on a 3D-printed holder, was aligned with the mouse somatosensory cortex (AP: −1.5 mm, ML: 2 mm). To minimize thermal deposition, the OBUS was positioned \~0.5 mm above the tissue. The acoustic coupling was maintained by filling with ultrasound gel. The laser pulses at a 1-kHz repetition rate were delivered to the OBUS via an optical fiber.

To induce c-Fos protein expression, OBUS stimulation was applied in a pulse train with a 25% duty cycle (3-s laser on, 9-s laser off) for 30 min. To evoke LFPs, 10-s OBUS stimulations consisting of 10,000 optoacoustic wave cycles were delivered every 20 s. The animals for electrophysiological recordings were initially anesthetized with 5% isoflurane and then transitioned to ketamine to restore more spontaneous brain activities.

## Immunofluorescence staining and imaging of mouse brain

After the stimulation session, mice were allowed to rest for 1 hour to maximize c-Fos expression. Euthanasia and transcardial perfusion were then performed using 1× phosphate-buffered saline [PBS (pH 7.4); Thermo Fisher Scientific], followed by fixation with 10% formalin. To facilitate stimulation site identification, extracted brains were carefully punctured at Bregma and the contralateral untreated site using a 25G needle. The brains were postfixed in 10% formalin for 24 hours before being transferred to 1× PBS. Horizontal sections (100-μm thickness) were obtained using an oscillating tissue slicer (OST-4500, Electron Microscopy Sciences) to assess stimulation depth. Brain slices were then transferred back into 10% formalin for an additional 24-hour fixation.

For immunostaining, slices were blocked in 5% bovine serum albumin (Sigma-Aldrich) in PBS for 30 min at room temperature and permeabilized with 0.2% Triton X-100 (Bio-Rad) in PBS for 10 min. They were incubated overnight at 4°C with an anti–c-Fos rabbit antibody (2 μg/ml; Cell Signaling Technology), followed by incubation in the dark at 4°C for 2 hours with Alexa Fluor 488 goat anti-rabbit immunoglobulin G (1 μg/ml; Thermo Fisher Scientific) and DAPI (4 μg/ ml; Thermo Fisher Scientific) for nuclear staining. Between each step, slices were rinsed four times for 5 min each in 0.2% Tween 20 (Tokyo Chemical Industry) in PBS. Fluorescent images were acquired using an FV3000 Confocal Laser Scanning Microscope (Olympus) with separate excitations at 405 nm for DAPI and 488 nm for c-Fos to minimize spectral cross-talk.

## Electrophysiological recording and signal processing

A multichannel neural probe (A1x16-Poly2-8 mm-100s-177-A16, NeuroNexus) with \~1-MΩ impedance was surgically implanted to mouse brains to record electrophysiological signals at the stimulation site. Neural signals were acquired at a 20-kHz sampling rate using a 16-channel headstage (Intan Technologies, part #C3334) and digitized by a 512-channel controller (Intan Technologies, part #C3004).

To synchronize laser activation with neural recordings, a trigger signal from the function generator was connected to an analog port on the recording system. For probe implantation, the anesthetized mouse underwent craniotomy. Alignment between the probe tip and OBUS center was achieved using a 3D micromanipulator. The OBUS was positioned at the stimulation site with ultrasound gel coupling, and laser delivery was precisely controlled using a mechanical shutter (Thorlabs, SH1).

Data processing was performed in MATLAB using custom scripts. Raw extracellular recordings were bandpass-filtered between 0.5 and 100 Hz to extract LFP signals. Spectrograms of LFP activity were generated using a 512-point FFT with 50% overlap, providing a frequency resolution of 1.95 Hz. PSD before, during, and after OBUS stimulation was computed using the Welch’s method with a 512-point window and 50% overlap.

## fMRI acquisition and processing

All fMRI experiments and animal handling procedures were approved by the Brigham and Women’s Hospital Institutional Animal Care and Use Committee and conducted in compliance with the Office of Laboratory Animal Welfare and the Association for Assessment and Accreditation of Laboratory Care regulations. Healthy male Sprague-Dawley rats (\~400 g, Charles River Laboratories, n = 2) were used. Body temperature and breathing rate were continuously monitored throughout the experiments.

To enhance acoustic transmission, a 5-mm-diameter cranial win dow was surgically created by removing the skullcap (AP: −1.9 mm, ML: 2.2 mm) while preserving the dura matter. The exposed brain was hydrated with 0.9% NaCl saline and covered with a cotton swab. Rats were anesthetized via intraperitoneal injection of ketamine (80 mg/kg) and xylazine (10 mg/kg), and petroleum jelly (Vaseline, Unilever, NJ, USA) was applied to the eyes to prevent dehydration.

MRI scans were performed using a horizontal bore 7.0-T Bruker BioSpec USR scanner (Bruker Corporation, Billerica, MA) with a 20–mm–inner diameter multipurpose receive-only surface coil over the rat’s head. Rats were placed in the prone position with their heads immobilized in a nose cone for isoflurane and oxygen delivery. The OBUS was positioned at the center of the cranial window with ultrasound gel coupling. Anesthesia was maintained with a combination of medetomidine (Dexdomitor, 0.025 mg/kg) and light isoflurane flow (56).

The functional imaging paradigm consisted of alternating 15-s “on” stimuli and 45-s “off ” periods over 7 min and 30 s. Ultrasoundevoked neuronal activity was validated by observing bilateral activation of the hind limb region in the somatosensory cortex following electrical stimulation of the hind paws. Four experimental conditions were tested in the same animal: trial 1: bilateral electrical stimulation of the hind paws only without the OBUS device in place (15 s on, 45 s off); trial 2: OBUS stimulation only with the OBUS device in place (15 s on, 45 s off); trial 3: bilateral electrical stimulation of the hind paws with OBUS in place (15 s on, 45 s off); and trial 4: bilateral electrical stimulation of the hind paws and OBUS stimulation with OBUS in place (15 s on, 45 s off). Hind paw stimulation consisted of subthreshold electrical pulses (5 Hz) delivered during the on period to activate the primary somatosensory cortex (S1) over six stimulation blocks.

fMRI data were acquired using a 2D single-shot gradient-echo echo planar imaging (EPI) sequence [0.5 mm by 0.5 mm by 1.0 mm resolution, 64 by 64 matrix, 18 axial slices, 0.2-mm slice gap, repetition time (TR) = 1500 ms, echo time (TE) = 18 ms]. Before the functional image, a main field homogeneity was optimized using the Bruker Mapshim protocol, and an anatomical image was acquired with a T2- weighted Rapid Acquisition with Relaxation Enhancement (RARE) sequence (0.469 mm by 0.469 mm by 0.5 mm resolution, 64 by 64 matrix, 50 axial slices, no slice gap, TR = 5367.7 ms, TE = 37.5 ms) was used for anatomical imaging. For hind paw stimulation, pairs of 30-gauge needles were inserted into the second and fourth digit pads of each hind paw. Electrical pulses (300 ms, 6 Hz) were delivered via a transcutaneous electrical nerve stimulation (TENS) unit (TU 7000, Tensunits.com, Largo, FL), with voltages adjusted to 700 mV (\~2-mA current) per hind paw, confirmed via oscilloscope measurements.

Data preprocessing was performed using SPM (2014) software and custom MATLAB scripts. T2-weighted anatomical images were segmented in SPM12 using the template of Valdés-Hernández et al. (57). The EPI images were first preprocessed, including slice time corrected, realigned, coregistered to the anatomical image, normalized to the template space, and spatially smoothed with a Gaussian filter of 0.8 mm–by–0.8 mm–by–0.8 mm FWHM. BOLD signals were analyzed as percent change from nonstimulated baseline, averaged across stimulation blocks to provide an average signal over the

1-min on/off stimulation block. To mitigate motion-related artifacts, a temporal band-pass filter (0.006 to 0.25 Hz) was applied, and motion traces and the average time signal from a white matter mask were regressed out. Activation was quantified using two metrics: mean BOLD signal change: computed over a defined ellipsoidal cortical region of interest (ROI: 1.75 mm by 2.5 mm in the cortical plane, by 2.25 mm through the cortex). Voxel-based activation count: the number of voxels exceeding a 0.5% BOLD signal change within an expanded S1 ROI (3.5 mm by 4.5 mm by 3.25 mm). Data were averaged within subjects and presented as mean ± SE.

## Temperature measurement of OBUS under stimulation pattern

To quantify temperature changes induced by OBUS stimulation, we conducted measurements with ex vivo mouse brain tissue. A formalinfixed mouse brain was dissected to allow insertion of a thermocouple (Opsens Solutions, OTG-M220). The thermocouple tip was positioned at the cortical surface. During measurements, the brain was immersed in PBS to prevent dehydration; however, the cortical surface remained above the waterline to eliminate thermal convection artifacts. Ultrasound gel was applied between the brain surface and the OBUS device, consistent with the preparation used for in vivo experiments.

The OBUS device was driven using the same stimulation protocol used in the in vivo electrophysiology experiment. Specifically, the laser delivered a patterned sequence of 10 s on, 20 s off, for a total duration of 1 min, corresponding to a 33% duty cycle, the highest duty cycle among the three stimulation paradigms used in the study. Temperature was recorded continuously at 50 Hz with a 5-s baseline.

## Statistical analysis

Acoustic waveforms and electrophysiological traces were plotted using Origin 2020. Frequency spectrum analysis was performed using FFT in MATLAB R2021a. Data are presented as mean ± SEM. Immunofluorescence images were analyzed using ImageJ. Additional data analysis details are provided in the respective method sections.

## Supplementary Materials

This PDF file includes:

Figs. S1 to S17

Table S1

## REFERENCES

1. B. A. Vogt, Pain and emotion interactions in subregions of the cingulate gyrus. Nat. Rev. Neurosci. 6, 533–544 (2005).  
2. K. C. Berridge, Affective valence in the brain: Modules or modes? Nat. Rev. Neurosci. 20 225–234 (2019).  
3. R. Martínez-Fernández, L. Zrinzo, I. Aviles-Olmos, M. Hariz, I. Martinez-­Torres, E. Joyce, M. Jahanshahi, P. Limousin, T. Foltynie, Deep brain stimulation for Gilles de la Tourette syndrome: A case series targeting subregions of the globus pallidus internus. Mov. Disord. 26, 1922–1930 (2011).  
4. J. E. Hoover, P. L. Strick, Multiple output channels in the basal ganglia. Science 259, 819–821 (1993).  
5. D . L. Adams, L. C. Sincich, J. C. Horton, Complete pattern of ocular dominance columns in human primary visual cortex. J. Neurosci. 27, 10391–10403 (2007).  
6. S. LeVay, M. Connolly, J. Houde, D. V. Essen, The complete pattern of ocular dominance stripes in the striate cortex and visual field of the macaque monkey. J. Neurosci. 5, 486–501 (1985).  
7. J. C. Horton, D. R. Hocking, An adult-like pattern of ocular dominance columns in striate cortex of newborn monkeys prior to visual experience. J. Neurosci. 16, 1791–1807 (1996).  
8. S. Breit, J. B. Schulz, A.-L. Benabid, Deep brain stimulation. Cell Tissue Res. 318, 275–288 (2004).  
9. J. S. Perlmutter, J. W. Mink, Deep brain stimulation. Annu. Rev. Neurosci. 29, 229–257 (2006).  
10. A. M. Lozano, N. Lipsman, H. Bergman, P. Brown, S. Chabardes, J. W. Chang, K. Matthews, C. C. McIntyre, T. E. Schlaepfer, M. Schulder, Y. Temel, J. Volkmann, J. K. Krauss, Deep brain stimulation: Current challenges and future directions. Nat. Rev. Neurol. 15, 148–160 (2019).  
11. M. D. Johnson, S. Miocinovic, C. C. McIntyre, J. L. Vitek, Mechanisms and targets of deep brain stimulation in movement disorders. Neurotherapeutics 5, 294–308 (2008).  
12. W. M. M. Schüpbach, S. Chabardes, C. Matthies, C. Pollo, F. Steigerwald, L. Timmermann, V. V. Vandewalle, J. Volkmann, P. R. Schuurman, Directional leads for deep brain stimulation: Opportunities and challenges. Mov. Disord. 32, 1371–1375 (2017).  
13. S. Zhang, M. Tagliati, N. Pouratian, B. Cheeran, E. Ross, E. Pereira, Steering the volume of tissue activated with a directional deep brain stimulation lead in the globus pallidus pars interna: A modeling study with heterogeneous tissue properties. Front. Comput. Neurosci. 14, 561180 (2020).  
14. S. Zhang, P. Silburn, N. Pouratian, B. Cheeran, L. Venkatesan, A. Kent, A. Schnitzler, Comparing current steering technologies for directional deep brain stimulation using a computational model that incorporates heterogeneous tissue properties. Neuromodulation 23, 469–477 (2020).  
15. G. Nagel, D. Ollig, M. Fuhrmann, S. Kateriya, A. M. Musti, E. Bamberg, P. Hegemann, Channelrhodopsin-1: A light-gated proton channel in green algae. Science 296, 2395–2398 (2002).  
16. E . S. Boyden, F. Zhang, E. Bamberg, G. Nagel, K. Deisseroth, Millisecond-timescale, genetically targeted optical control of neural activity. Nat. Neurosci. 8, 1263–1268 (2005).  
17. J. Delbeke, L. Hoffman, K. Mols, D. Braeken, D. Prodanov, And then there was light: Perspectives of optogenetics for deep brain stimulation and neuromodulation. Front. Neurosci. 11, 663 (2017).  
18. M. M. Chernov, R. M. Friedman, G. Chen, G. R. Stoner, A. W. Roe, Functionally specific optogenetic modulation in primate visual cortex. Proc. Natl. Acad. Sci. U.S.A. 115, 10505–10510 (2018).  
19. O. Ruiz, B. R. Lustig, J. J. Nassi, A. Cetin, J. H. Reynolds, T. D. Albright, E. M. Callaway, G. R. Stoner, A. W. Roe, Optogenetics through windows on the brain in the nonhuman primate. J. Neurophysiol. 110, 1455–1467 (2013).  
20. R. Scharf, T. Tsunematsu, N. McAlinden, M. D. Dawson, S. Sakata, K. Mathieson, Depth-specific optogenetic control in vivo with a scalable, high-density μLED neura probe. Sci. Rep. 6, 28381 (2016).  
21. H . Thair, A. L. Holloway, R. Newport, A. D. Smith, Transcranial direct current stimulation (tDC S): A beginner’s guide for design and implementation. Front. Neurosci. 11, 641 (2017).  
22. N . Bolognini, T. Ro, Transcranial magnetic stimulation: Disrupting neural activity to alter and assess brain function. J. Neurosci. 30, 9647–9650 (2010).  
23. R. Beisteiner, M. Hallett, A. M. Lozano, Ultrasound neuromodulation as a new brain therapy. Adv. Sci. 10, 2205634 (2023).  
24. Y. Tufail, A. Yoshihiro, S. Pati, M. M. Li, W. J. Tyler, Ultrasonic neuromodulation by brain stimulation with transcranial ultrasound. Nat. Protoc. 6, 1453–1470 (2011).  
25. G. Li, W. Qiu, Z. Zhang, Q. Jiang, M. Su, R. Cai, Y. Li, F. Cai, Z. Deng, D. Xu, H. Zhang, H. Zheng, Noninvasive ultrasonic neuromodulation in freely moving mice. IEEE Trans. Biomed. Eng. 66, 217–224 (2019).  
26. Y. Yang, J. Yuan, R. L. Field, D. Ye, Z. Hu, K. Xu, L. Xu, Y. Gong, Y. Yue, A. V. Kravitz, M. R. Bruchas, J. Cui, J. R. Brestoff, H. Chen, Induction of a torpor-like hypothermic and hypometabolic state in rodents by ultrasound. Nat. Metab. 5, 789–803 (2023).  
27. Z. Lin, L. Meng, J. Zou, W. Zhou, X. Huang, S. Xue, T. Bian, T. Yuan, L. Niu, Y. Guo, H. Zheng, Non-invasive ultrasonic neuromodulation of neuronal excitability for treatment of epilepsy. Theranostics 10, 5514–5526 (2020).  
28. F. Munoz, A. Meaney, A. Gross, K. Liu, A. N. Pouliopoulos, D. Liu, E. E. Konofagou, V. P. Ferrera, Long term study of motivational and cognitive effects of low-intensity focused ultrasound neuromodulation in the dorsal striatum of nonhuman primates. Brain Stimul. 15, 360–372 (2022).  
29. R. Beisteiner, E. Matt, C. Fan, H. Baldysiak, M. Schönfeld, T. Philippi Novak, A. Amini, T. Aslan, R. Reinecke, J. Lehrner, A. Weber, U. Reime, C. Goldenstedt, E. Marlinghaus, M. Hallett, H. Lohse-Busch, Transcranial pulse stimulation with ultrasound in alzheimer’ disease—A new navigated focal brain therapy. Adv. Sci. 7, 1902583 (2020)  
30. S. Jiménez-Gambín, N. Jiménez, J. M. Benlloch, F. Camarena, Generating Bessel beams with broad depth-of-field by using phase-only acoustic holograms. Sci. Rep. 9, 20104 (2019).  
31. G. Antonacci, D. Caprini, G. Ruocco, Demonstration of self-healing and scattering resilience of acoustic Bessel beams. Appl. Phys. Lett. 114, 013502 (2019).  
32. X. Zhuang, J. He, J. Wu, X. Ji, Y. Chen, M. Yuan, L. Zeng, A spatial multitarget ultrasound neuromodulation system using high-powered 2-­D array transducer. IEEE Trans. Ultrason. Ferroelectr. Freq. Control 69, 998–1007 (2022).  
33. H . Chan, H.-Y. Chang, W.-L. Lin, G.-S. Chen, Large-volume focused-ultrasound mild hyperthermia for improving blood-brain tumor barrier permeability application. Pharmaceutics 14, 2012 (2022).  
34. Z. Du, G. Chen, Y. Li, N. Zheng, J.-X. Cheng, C. Yang, Photoacoustic: A versatile nongenetic method for high-precision neuromodulation. Acc. Chem. Res. 57, 1595–1607 (2024).  
35. Y. Jiang, H. J. Lee, L. Lan, H. Tseng, C. Yang, H.-Y. Man, X. Han, J.-X. Cheng, Optoacoustic brain stimulation at submillimeter spatial precision. Nat. Commun. 11, 881 (2020).  
36. L. Shi, Y. Jiang, Y. Zhang, L. Lan, Y. Huang, J.-X. Cheng, C. Yang, A fiber optoacoustic emitter with controlled ultrasound frequency for cell membrane sonoporation at submillimeter spatial resolution. Photoacoustics 20, 100208 (2020).  
37. L. Shi, Y. Jiang, F. R. Fernandez, G. Chen, L. Lan, H.-Y. Man, J. A. White, J.-X. Cheng, C. Yang, Non-genetic photoacoustic stimulation of single neurons by a tapered fiber optoacoustic emitter. Light Sci. Appl. 10, 143 (2021).  
38. Y. Li, Y. Jiang, L. Lan, X. Ge, R. Cheng, Y. Zhan, G. Chen, L. Shi, R. Wang, N. Zheng, C. Yang, J.-X. Cheng, Optically-generated focused ultrasound for noninvasive brain stimulation with ultrahigh precision. Light Sci. Appl. 11, 321 (2022).  
39. H . Estrada, J. Robin, A. Özbek, Z. Chen, A. Marowsky, Q. Zhou, D. Beck, B. le Roy, M. Arand, S. Shoham, D. Razansky, High-resolution fluorescence-guided transcranial ultrasound mapping in the live mouse brain. Sci. Adv. 7, eabi5464 (2021).  
40. H . Hocheng, C.-M. Chen, Y.-­C. Chou, C.-­H. Lin, Study of novel electrical routing and integrated packaging on bio-compatible flexible substrates. Microsyst. Technol. 16, 423–430 (2010).  
41. B. G. Sanganahalli, G. J. Thompson, M. Parent, J. V. Verhagen, H. Blumenfeld, P. Herman, F. Hyder, Thalamic activations in rat brain by fMRI during tactile (forepaw, whisker) and non-tactile (visual, olfactory) sensory stimulations. PLOS ONE 17, e0267916 (2022).  
42. F. A. Duck, Medical and non-medical protection standards for ultrasound and infrasound Prog. Biophys. Mol. Biol. 93, 176–191 (2007).  
43. E . A. Kiyatkin, Brain temperature and its role in physiology and pathophysiology: Lessons from 20 years of thermorecording. Temperature (Austin) 6, 271–333 (2019).  
44. E . A. Kiyatkin, Physiological and pathological brain hyperthermia. Prog. Brain Res. 162, pp. 219–243 (2007).  
45. E . J. Walter, M. Carraretto, The neurological and cognitive consequences of hyperthermia Crit. Care 20, 199 (2016).  
46. H . Wang, B. Wang, K. P. Normoyle, K. Jackson, K. Spitler, M. F. Sharrock, C. M. Miller, C. Best, D. Llano, R. Du, Brain temperature and its fundamental properties: A review for clinical neuroscientists. Front. Neurosci. 8, 307 (2014).  
47. M. N. Collins, W. Legon, K. A. Mesce, The inhibitory thermal effects of focused ultrasound on an identified, single motoneuron. eNeuro 8, ENE URO.0514-20.2021 (2021).  
48. S. Charbenny, Z. Huang, Brain thermal response to low intensity focused ultrasound at the action potential level and neuron response to various stimulus. Comput. Biol. Med. 197, 111094 (2025).  
49. Y. Choe, J. W. Kim, K. K. Shung, E. S. Kim, Microparticle trapping in an ultrasonic Besse beam. Appl. Phys. Lett. 99, 233704 (2011).  
50. Z. Xu, W. Xu, M. Qian, Q. Cheng, X. Liu, A flat acoustic lens to generate a Bessel-like beam. Ultrasonics 80, 66–71 (2017).  
51. N . Jiménez, R. Picó, V. Sánchez-Morcillo, V. Romero-García, L. M. García-Raffi, K. Staliunas, Formation of high-order acoustic Bessel beams by spiral diffraction gratings. Phys. Rev. E 94, 053004 (2016).  
52. J.-Y. Lu, J. F. Greenleaf, Ultrasonic nondiffracting transducer for medical imaging. IEEE Trans. Ultrason. Ferroelectr. Freq. Control 37, 438–447 (1990).  
53. W. Gao, W. Liu, Y. Hu, J. Wang, Study of ultrasonic near-field region in ultrasonic liquid-level monitoring system. Micromachines 11, 763 (2020).  
54. J. Durnin, J. J. Miceli, J. H. Eberly, Comparison of Bessel and Gaussian beams. Opt. Lett. 13, 79–80 (1988).  
55. X. Du, J. Li, G. Niu, J.-­H. Yuan, K.-­H. Xue, M. Xia, W. Pan, X. Yang, B. Zhu, J. Tang, Lead halide perovskite for efficient optoacoustic conversion and application toward high-resolution ultrasound imaging. Nat. Commun. 12, 3348 (2021).  
56. J. K. Brynildsen, L.-M. Hsu, T. J. Ross, E. A. Stein, Y. Yang, H. Lu, Physiologica characterization of a robust survival rodent fMRI method. Magn. Reson. Imaging 35, 54–60 (2017).  
57. P. A. Valdés-­Hernández, A. Sumiyoshi, H. Nonaka, R. Haga, E. Aubert Vasquez, T. Ogawa, Y. Iturria Medina, J. J. Riera, R. Kawashima, An in vivo MRI template set for morphometry, tissue segmentation, and fMRI localization in rats. Front. Neuroinform. 5, 26 (2011).

Acknowledgments: We acknowledge R. Wang and M. Marar for assistance in OBUS device fabrication and in vivo experiment setup. Immunofluorescence imaging reported in this publication was supported by the Boston University Micro and Nano Imaging Facility and the Office of the Director, National Institutes of Health of the National Institutes of Health under award number S10OD024993. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health. Funding: This work was supported by the Focused Ultrasound Foundation grant (C.Y.), NIH R21 EY035437-01 (C.Y.), and R01NS109794 (J.-X.C.). Author contributions: Conceptualization: Y.L. and L.L. Methodology: Y.L., T.R.O., and N.T. Investigation: Y.L., G.C., T.R.O., N.T., Y.-Z.Z., C.M., and N.Z. Data curation: Y.L., G.C., T.R.O., N.T., C.M., and N.Z. Validation: Y.L. and N.T. Visualization: Y.L. and T.R.O. Formal analysis: Y.L. and T.R.O. Software: Y.L. Supervision: C.Y., J.-X.C., and N.M. Project administration: Y.L. and C.Y. Writing—original draft: Y.L. and T.R.O. Writing—review and editing: Y.L., T.R.O., N.T., C.Y., and J.-X.C. Resources: Y.L., T.R.O., N.T., Y.-Z.Z., N.M., C.Y., and J.-X.C. Funding acquisition: C.Y. Competing interests: C.Y., J.-X.C., N.Z., Y.L., and L.L. have a patent on Methods and Devices for Optoacoustic Stimulation (US patent no. 11684404 B2) issued June 27, 2023 by Boston University. C.Y. and J.-X.C. serve as Scientific Advisor for Axorus SAS. C.Y. received a research grant from Axorus SAS, which did not support this work. Y.L. was partially supported by Axorus which does not support this work. All other authors declare that they have no competing interests. Data, code, and materials availability: All data and code needed to evaluate and reproduce the results in the paper are present in the paper and/or the

Supplementary Materials. This study did not generate new materials. The data for this study have been deposited in the database Dryad: https://doi.org/10.5061/dryad.zgmsbccr0.

Submitted 13 June 2025

Accepted 6 March 2026

Published 10 April 2026

10.1126/sciadv.adz7708

# ScienceAdvances

## Miniaturized optically generated Bessel beam ultrasound for volumetric transcranial brain stimulation

Yueming Li, Guo Chen, Tiago R. Oliveira, Nick Todd, Yong-Zhi Zhang, Carolyn Marar, Nan Zheng, Lu Lan, Nathan McDannold, Ji-Xin Cheng, and Chen Yang

Sci. Adv. 12 (15), eadz7708. DOI: 10.1126/sciadv.adz7708

View the article online

https://www.science.org/doi/10.1126/sciadv.adz7708

Permissions

https://www.science.org/help/reprints-and-permissions

Use of this article is subject to the Terms of service