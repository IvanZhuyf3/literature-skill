# Spectroscopic Imaging of Deep Tissue through Photoacoustic Detection of Molecular Vibration

Pu Wang,† Justin R. Rajian,† and Ji-Xin Cheng\*,†,‡

† Weldon School of Biomedical Engineering and ‡ Department of Chemistry, Purdue University, West Lafayette, Indiana 47907, United States

ABSTRACT: The quantized vibration of chemical bonds provides a way of imaging target molecules in a complex tissue environment. Photoacoustic detection of harmonic vibrational transitions provides an approach to visualize tissue content beyond the ballistic photon regime. This method involves pulsed laser excitation of overtone transitions in target molecules inside of tissue. Fast relaxation of the vibrational energy into heat results in a local temperature rise on the order of milliKelvins and a subsequent generation of acoustic waves detectable with an ultrasonic transducer. In this Perspective, we review recent advances that demonstrate the advantages of vibration-based photoacoustic imaging and illustrate its potential in diagnosing cardiovascular plaques. An outlook into future development of vibrational photoacoustic endoscopy and tomography is provided.

![](images/4d2f52b620d00eb4292b8ec22e6406c9c7bd360272d0437d0116427784eff682.jpg)

<details>
<summary>text_image</summary>

Lipid core
3.15 mm
z
y
x
Lumen
</details>

ibrational spectroscopy and imaging based on infrared absorption, near-infrared absorption, and spontaneous Raman scattering have been applied intensively to biomedicine.1−3 With high sensitivity and three-dimensional sectioning capability, nonlinear vibrational microscopies based on and stimulated Raman scattering6,7 have shed new light on biomedical research.8 While coherent Raman scattering microscopy offers submicrometer resolution for mapping subcellular structures, it employs ballistic photons under the tight focusing condition and thus has a limited tissue penetration depth of ∼100 μm, which prevents its potential use for imaging deep tissue in clinical settings. With a superior imaging depth, diffused optical tomography based on near-infrared absorption and Raman scattering has been successfully developed for biomedical study, even in clinical settings.9,10 This modality interrogates the subjects with photons and detects the output signal with a photon detector. When a biological tissue of millimeter to centimeter thickness is investigated, the output photons undergo multiple scattering within the sample and hence carry only the spatially averaged information from a bulk volume. As a result, the spatial resolution is significantly compromised. Moreover, sophisticated excitation schemes and/ or image processing algorithms are needed to separate molecular absorption from scattering. Therefore, new imaging platforms are needed in order to reach deep tissue while maintaining high chemical selectivity and spatial resolution in order to satisfy biomedical diagnostic needs.

An elegant way toward such a goal is to the coupling of photons and sound. When a photon is absorbed by a molecule, part of the absorbed energy is converted into heat. If the absorption takes place in a short time (e.g., induced by a nanosecond laser pulse), the local heating leads to thermal expansion and contraction followed by creation of pressure transients, which then propagate as acoustic waves detectable by an ultrasonic transducer. This creation of acoustic waves by pulsed absorption of light is called the photoacoustic effect, documented by Alexander Graham Bell as early in 1880.11 Photoacoustic waves can be excited by microwave pulses or by laser pulses. The principle of laser-based photoacoustic tomography is depicted in Figure 1. A pulsed laser beam is

![](images/a935ca3779dc9a36501b563d79eb17347a1664cde9e8006fa14735bd4b8d032d.jpg)

<details>
<summary>text_image</summary>

Pulsed laser
Diffuser
Optical
absorber
Sample
Acoustic
waves
Transducer
ΔT ~ 10⁻³ K
Output waveform
</details>

Figure 1. The principle of laser-based photoacoustic tomography.

expanded by an optical diffuser, which then irradiates a specimen containing optical absorbers with significant absorption at the laser wavelength. Part of the absorbed energy heats the surrounding region of the absorbers, resulting in a temperature rise on the order of milliKelvins and a subsequent generation of acoustic waves. The measured waveform as the

Received: March 11, 2013

Accepted: June 13, 2013

Published: June 13, 2013

output of a transducer is bipolar, a positive peak followed by a negative peak. The amplitude of the photoacoustic waveform is proportional to the absorption coefficient and the light fluence

$$
P \propto E \beta \alpha n \left(\frac {\kappa}{\rho C _ {\mathrm{p}}}\right) \tag {1}
$$

where E is the radiation fluence. $\beta$ is the thermal coefficient of volume expansion, α is the absorption coefficient, n is the concentration of absorbers, κ is the Bulk modulus, $\rho$ is the mass density, and $C _ { \mathfrak { p } }$ is the specific heat capacity at constant pressure.

Importantly, the time-of-flight of the PA signal carries information about the location of the absorber. Hence, the distribution of the optical absorbers responsible for the PA generation can be determined by using an image reconstruction algorithm. Because the speed of sound is about 1.5 mm/μs inside of a soft tissue, a spatial resolution on the order of 0.1 mm can be achieved with a transducer of 10 MHz bandwidth. The PA imaging technique offers several unique advantages over its pure optical counterparts. First is higher resolution in deep tissue owing to the detection of acoustic waves, scattering of which is about 3 orders of magnitude less than optical scattering. Second, because the PA signal originates from absorption of photons, it eliminates the background caused by scattering and offers a molecular contrast based on optical absorption. Third, the PA signal generation does not solely depend on ballistic photons. The diffused photons equally contribute to the signal, which leads to a centimeter-scale imaging depth in a tomography configuration.

The field of PA imaging has grown rapidly during the past decade, resulting in numerous biomedical applications.12−14 Most of those applications were based on the electronic absorption of hemoglobin,15−17 while others employed exogenous contrast agents such as dyes and nanomaterials.18−25

In this Perspective, we review recent advances in label-free spectroscopic PA imaging using vibrational absorption as a novel contrast mechanism. We start with an introduction of two vibrational absorption processes that have been used for PA imaging, with a focus on overtone transitions. Specific applications to lipid and connective tissue imaging will be given to illustrate the potential impact of the technology on biomedicine. Translational potential of vibrational PA imaging in the diagnosis of atherosclerosis and other human disorders will be discussed.

## Molecular vibrational transition offers a novel mechanism for generation of photoacoustic waves inside of a tissue.

Recent studies revealed new possibilities of implementing PA imaging by using vibrational absorption as the contrast mechanism. One is based on a molecular overtone (Figure 2A) as well as combinational transitions that are allowed by anharmonicity of chemical bond vibration.26 The transition frequency of an overtone band is described by

$$
\Omega = \Omega_ {0} n - \chi \Omega_ {0} (n + n ^ {2}) \tag {2}
$$

where $\Omega _ { 0 }$ is the frequency of a fundamental vibration, $\chi$ is the anharmonicity, and $n = 2 , 3 ,$ ... represents the first, second, and so on overtone. The molecules directly absorb the photons when an incident laser frequency resonates with an overtone transition. Stimulated Raman scattering is another process that has been used to produce PA signals.27 A stimulated Raman scattering process involves a pump beam at frequency $\omega _ { \mathsf { p } }$ and a Stokes beam at frequency $\omega _ { s } .$ When $( \omega _ { \mathrm { p } } - \omega _ { \mathrm { s } } )$ is tuned to the frequency of a fundamental vibration (Figure 2B), a gain in the Stokes field intensity and a loss in the pump field intensity occur via light−molecule interactions. The energy difference, $\hbar ( \omega _ { \mathrm { p } } - \omega _ { \mathrm { s } } ) ^ { - } = \hbar \Omega _ { 0 } ,$ is absorbed by the interacting molecules.28 In both overtone transition and SRS processes, fast relaxation of the vibrational energy into heat offers a mechanism for generation of acoustic waves. SRS-based PA microscopy was reported by Yakovlev and co-workers.29,30 Compared to the overtone transitions, SRS has a much lower efficiency in light− matter energy transfer.31 Consequently, PA-SRS has relatively low detection sensitivity, and it suffers from a background induced by absorption of individual pump and Stokes beams. In this Perspective, we focus on deep tissue imaging enabled by photoacoustic detection of molecular overtone absorption.

![](images/bf3943e49015c3b4de3b9e0b0ed91b85369d6939804d1956375a16505ba0b85b.jpg)

<details>
<summary>text_image</summary>

A Overtone absorption
v = 3
v = 2
v = 1
v = 0
Ω₁ Ω₂
</details>

![](images/42689320cafedfbf98da02131b07c7c9bb22e5a593181783f12bac14e8ad08f4.jpg)

<details>
<summary>text_image</summary>

B
Stimulated Raman scattering
ωp ωs
v = 3
v = 2
v = 1
v = 0
Ω0
</details>

Figure 2. Principles of overtone absorption (A) and stimulated Raman scattering process (B); ν denotes the vibration energy levels.

We note that photoacoustic overtone spectroscopy was reported more than 30 years ago by Tam and Patel.32−35 At that time, applications were focused on spectroscopic study of pure liquids of $\mathrm { H } _ { 2 } \mathrm { O } , \mathrm { D } _ { 2 } \mathrm { O } ,$ , and benzene. The applicability of overtone absorption to photoacoustic imaging of biological tissues has not been explored until very recently.31,36−38 Han-Wei Wang et al. reported an important study that demonstrated the feasibility of vibrational photoacoustic microscopy.31 At first glance, the absorption cross section of hemoglobin $\dot { ( 9 . 1 \times 1 0 ^ { - 1 7 } }$ cm2 /molecule at 550 nm) is about 6 orders of magnitude larger than that of the second overtone transition of the CH bond $( 2 . 7 \times 1 0 ^ { - 2 2 }$ at 1200 nm).39 Nevertheless, the molar density of hemoglobin in whole blood $\left( \sim 1 \times 1 0 ^ { - 2 } \mathrm { M } \right)$ is much lower than that of CH bonds in olive oil $( 5 \times 1 0 ^ { 1 } \mathrm { ~ M ~ } )$ . Experimentally, Wang et al. compared microscopic PA imaging of whole blood by 5 ns pulsed excitation at 555 nm and PA imaging of olive oil by 5 ns pulsed excitation at 1200 nm. Both samples were embedded in a glass tube. The same level of signals was produced by using 22 $\mu \mathrm { J }$ for the PA imaging of olive oil and $2 . 5 9 \mu ]$ for the PA imaging of whole blood. These data suggest that the PA imaging of chemical bonds is possible when the target subject has high chemical bond density. Given the fact that OH and CH are the most abundant chemical bonds in biological tissues, it is promising to develop bond-selective PA imaging modalities for visualization of water with abundant OH bonds, lipid bodies with abundant $\mathrm { C H } _ { 2 }$ groups, and protein aggregates with abundant $\mathrm { C H } _ { 3 }$ groups.

Lihong Wang and co-workers reported that water in phantoms and in tissues can be visualized by excitation at $9 7 0 ~ \mathrm { ~ n m } , ^ { 4 0 }$ where the high-order combination bands of symmetric and asymmetric stretching modes of the OH bond reside.41 However, the absorption coefficient of pure water at this wavelength is an order of magnitude smaller than that of whole blood, which limits in vivo applications. Moreover, water molecules are abundant everywhere in most biological samples. If water is excited at its lower-order overtone or combination bands, the abundant water absorption will strongly attenuate the light fluence into the deep tissue. Given that the absorption coefficient of water $\mathrm { i s } \sim 3 0 \ c m ^ { - 1 }$ for the first combination bands at 1450 nm, the absorption mean free path is only ∼300 μm. Therefore, water is not an ideal target for vibration-based PA imaging. On the other hand, the CH bonds are only abundant in certain types of biological structures, such as $\mathrm { C H } _ { 2 }$ -rich lipid bodies and CH -rich collagens. It means that the contrast depth dilemma does not present in PA imaging of CH bonds.

A few studies were conducted to determine the suitable wavelengths for PA imaging of CH bonds.31,42 As shown in Figure 3A, electronic absorption of hemoglobin is dominant in a window ranging from the visible to the near-infrared region $( \mathrm { i . e . , }$ 400 nm to 1.0 μm). The hemoglobin absorption overwhelmed the third- and higher-order CH overtone transitions located in the same region. For wavelengths longer than 1.0 μm, significant water absorption due to overtone transitions of OH bonds reduces the photon fluence inside of the biological samples. Nevertheless, two valleys exist in the water vibrational absorption spectrum, 1000−1300 and 1600− 1850 nm (highlighted in light blue). Importantly, the second and first overtone transitions of CH bonds are located at the windows of 1000−1300 and 1600−1850 nm, respectively. These spectral features produce two optical windows for CH bond-selective imaging.

![](images/1aa925c8dd8e44ae10a0d4dcfc3a65e25d3ad3c0cc45a2fe164f264fbe026025.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Absorption Coefficient μα (cm⁻¹) |
| --------------- | ------------------------------- |
| 500             | ~10²                            |
| 700             | ~10⁰                            |
| 1000            | ~10¹                            |
| 2000            | ~10²                            |
| 3333            | ~10⁴                            |
| 5000            | ~10²                            |
</details>

![](images/400d971d3bbd5dce52a402210ecf409928928d7100774da860dcc7c979f8dbf2.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Polyethylene PA amplitude (a.u.) | Trimethylpentane PA amplitude (a.u.) |
| ----------------- | -------------------------------- | ----------------------------------- |
| 1210              | ~5                               | -                                   |
| 1730              | ~30                              | -                                   |
| 1760              | ~25                              | -                                   |
| 1195              | -                                | ~5                                  |
| 1700              | -                                | ~20                                 |
</details>

![](images/6b352daef5303bd5d719661450974b248ae8c830c4e6a673587f0713aaf8e347.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Water PA amplitude (a.u.) | Deuterium oxide PA amplitude (a.u.) |
| --------------- | ------------------------- | ----------------------------------- |
| 1450            | ~8                        | -                                   |
| 1940            | ~38                       | -                                   |
</details>

Figure 3. PA spectra of various chemical bond vibrations. (A) Absorption spectra of whole blood and pure water. (B) PA spectra of polyethylene and trimethylpentane. (C) PA spectra of water and deuterium oxide. Adapted from ref 42. Copyright 2012, Wiley−VCH.

Pu Wang et al. performed a detailed analysis of photoacoustic vibrational spectra of CH, OH, and OD bonds.42 As shown in Figure 3B, polyethylene provides the absorption profile of the methylene group $( \mathrm { \dot { C } H _ { 2 } } ) _ { \mathrm { : } }$ , for which the first overtone $\left( 2 \nu \thinspace \mathrm { C H } _ { 2 } \right)$ shows two primary peaks at around 1730 $( 5 8 0 0 ~ \mathrm { c m } ^ { - 1 } )$ and 1760 nm $( \dot { 5 } 6 8 0 ~ \mathrm { { \dot { c } m } ^ { - 1 } ) }$ . The stronger peak at 1730 nm is generally thought to be a combination band of asymmetric and symmetric stretching $\left( \nu _ { \mathrm { a } } + \nu _ { \mathrm { s } } \right) . ^ { 4 1 }$ The 1760 nm peak is assigned to the first overtone of $\mathrm { C H } _ { 2 }$ stretching.41 The second combination band of $\mathrm { C H } _ { 2 } ,$ located between 1350 and 1500 nm, is attributed to the combination of harmonic stretching and a nonstretching mode, such as bending, twisting, and rocking $( 2 \nu + \delta ) . ^ { 4 1 }$ The second overtone of CH stretching is peaked at around 1210 nm. It was shown that the PA amplitude at 1730 nm is around 6.3 times that at $1 2 1 0 \ \mathrm { n m } . ^ { 4 2 }$ The spectrum of trimethylpentane is mainly contributed to by the absorption profile of methyl groups $\left( \mathrm { C H } _ { 3 } \right)$ . The primary peak at around 1700 nm $( 5 8 8 0 ~ \mathrm { c m } ^ { - 1 } )$ is assigned to the first overtone of $\mathrm { C H } _ { 3 }$ stretching. It is clear that the $\mathrm { C H } _ { 2 }$ and $\mathrm { C H } _ { 3 }$ groups have distinguishable profiles at the first overtone region, which allowed multispectral PA imaging of fat and collagen.43 The second combination band of $\mathrm { C H } _ { 3 }$ starts from 1350 to 1500 nm, with the main peak at around 1380 nm, which is generally thought to be $2 \dot { \nu } + \delta . ^ { 4 1 }$ The second overtone of $\mathrm { C H } _ { 3 }$ stretching shows the primary peak at around 1195 nm. Figure 3C shows the PA spectra of $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ and $\mathrm { D } _ { 2 } \mathrm { O }$ liquid in the 1.0−2.0 μm window. The $\nu _ { 2 } ~ + ~ \nu _ { 3 }$ combinational band and the $\nu _ { 1 } ~ + ~ \nu _ { 3 }$ combinational band appear at 1940 and 1450 nm, respectively. Here $\nu _ { 1 } , \ \nu _ { 2 } ,$ and $\nu _ { 3 }$ denote the symmetric, bending, and asymmetric vibrations of the water molecule, respectively. Due to the heavier mass of deuterium, the prominent overtone and combinational bands of $\mathrm { D } _ { 2 } \mathrm { O }$ are located at longer wavelengths. Thus, $\mathrm { D } _ { 2 } \mathrm { O }$ can be used as an acoustic coupling agent during vibration-based PA imaging.

## Overtone-absorption-based PA imaging offers an avenue of mapping lipids in biological samples.

As there are two optical windows for PA imaging of CH bonds, it raises a question of which window should be used for specific applications. On one hand, excitation of the first overtone of CH bond gives 6−7 times higher signal than excitation of the second overtone. On the other hand, as water is a dominant absorber in tissue and water absorption is enhanced at longer wavelengths, the photon fluence in deep tissue is more effectively reduced when excitation happens at the first overtone region. Figure 4A shows the PA overtone spectra of polyethylene acquired through a water layer of different thickness. The figure inset shows the schematic of the experiment setup. Increasing the water layer thickness resulted in a faster decrease of the PA signal at 1730 nm. Nevertheless, the PA signal produced by the first overtone remains larger than that of the second overtone when a water layer of 2.9 mm was added to the beam path. To validate the data, we theoretically computed the local light flux using the Beer− Lambert law for water absorption and calculated the ratio of the PA signal by first overtone excitation to that by second overtone excitation. The result is shown in Figure 4B. The calculated values agree well with the experimental data, showing that 1730 nm excitation is beneficial even through 3 mm water absorption.42 These results suggest that excitation at the first overtone of the CH bond is favorable in the applications where a millimeter-scale penetration depth is needed, such as PA microscopy of harvested tissues and intravascular PA imaging of an atherosclerotic artery. When dealing with applications that require a penetration depth larger than a few millimeters, excitation of the second overtone of CH becomes a better choice.

![](images/b0ba8080c518acc88b279d96671718f9641fd5e2b277e1cd1dceda403200e6d6.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | 1.2mm | 1.6mm | 1.9mm | 2.6mm | 2.9mm |
| --------------- | ----- | ----- | ----- | ----- | ----- |
| 1100            | ~0    | ~0    | ~0    | ~0    | ~0    |
| 1150            | ~0    | ~0    | ~0    | ~0    | ~0    |
| 1200            | ~3    | ~2    | ~1    | ~1    | ~1    |
| 1250            | ~4    | ~3    | ~2    | ~2    | ~2    |
| 1700            | ~15   | ~10   | ~8    | ~6    | ~4    |
| 1750            | ~5    | ~3    | ~2    | ~1    | ~1    |
| 1800            | ~0    | ~0    | ~0    | ~0    | ~0    |
</details>

![](images/7abff1ceea9e6a2804e46cb1ea1cc5699397a8f0fb981eca7a8c4ca8f7c01fba.jpg)

<details>
<summary>line chart</summary>

| Water layer thickness (mm) | Theoretical calculation | Experiment results |
| -------------------------- | ------------------------ | ------------------ |
| 0                          | 6.5                      | 6.5                |
| 0.5                        | 5.5                      | 5.5                |
| 1.0                        | 4.0                      | 3.8                |
| 1.5                        | 3.0                      | 2.8                |
| 2.0                        | 2.5                      | 2.3                |
| 2.5                        | 2.0                      | 1.8                |
| 3.0                        | 1.5                      | 1.3                |
| 3.5                        | 1.0                      | 0.8                |
| 4.0                        | 0.7                      | -                  |
| 4.5                        | 0.5                      | -                  |
| 5.0                        | 0.3                      | -                  |
</details>

Figure 4. Phantom study that evaluates the effect of water on PA imaging in the near-infrared region. (A) PA spectra of PE at different water layer thicknesses. The inset figure shows the schematic of the constructed phantom. PE: polyethylene. (B) PA amplitude ratio between the first and second overtone excitations as a function of water layer thickness. Adapted from ref 42. Copyright 2012, Wiley− VCH.

Lipid accumulation usually gives about 1 order of magnitude higher signal compared to the surrounding connective tissues in PA imaging with 1730 or 1210 nm excitation, owing to the dense packing of the $\mathrm { C H } _ { 2 }$ group in the lipid. Therefore, it is highly favorable to use a single resonant wavelength to map the distribution of the lipid in biological samples. Several applications were demonstrated by PA imaging of $\mathrm { C H } _ { 2 }$ groups. Wang et al. examined the intramuscular fat in a fresh muscle tissue (Figure 5A). Intramuscular lipids are involved in metabolic disorders, but their assessment in fresh tissues is difficult.44 In this study, intramuscular fat was inspected using PA microscopy, which is based on overtone absorption of CH bonds with a penetration depth of over 1 mm. The result shows the exciting potential of using this technique for quantitative measurement of intramuscular fat accumulation in metabolic disorders. Owing to the abundant $\mathrm { C H } _ { 2 }$ groups accumulated in a myelin sheath, the white matter in the spinal cord can also be visualized using PA microscopy based on CH overtone absorption (Figure 5B). From the cross-sectional image, a contrast of ${ \sim } 2 . 5$ times between the white matter and gray matter was obtained. This suggests that vibration-based PA microscopy could be potentially applied to the assessment of white matter loss during spinal cord injury and its repairing process. Figure 5C shows 3-D imaging of fat bodies of whole third-instar larvae in vivo. The projection and sectional images elucidate the distribution of lipid storage along the anterior− posterior and the ventral−dorsal axes. Depth-resolved spectroscopy at certain points was also performed for confirmation purposes. The demonstrated capability of label-free visualization of adipose tissues in Drosophila is important for the rapid determination of phenotype, which will decrease the time required to conduct genetic screens for targets of fat metabolism and autophagy in this model organism.45,46

## The intravascular vibrational PA catheter is a potential game changer in diagnosing vulnerable plaques in atherosclerosis.

Beyond the lipid studies in microscopy settings, applications that are more clinically relevant are emerging. One example is the intravascular photoacoustic (IVPA) catheter for diagnosis of plaques in atherosclerosis. Cardiovascular disease (CVD) is the number 1 cause of death in the United States. More than 2200 people die of CVD every day.47 The majority of the fatal acute syndromes are due to vulnerable plaques, referred to as plaques having a high risk to rupture and cause thrombosis. Of all physiological features, a lipid-rich core, a thin fibrous cap, and infiltration of inflammatory cells are considered major factors accounting for the high risk of acute cardiovascular syndrome.48 Current imaging modalities such as magnetic resonance imaging (MRI), X-ray angiography, intravascular ultrasound (IVUS), optical coherence tomography (OCT), and multislice spiral computed tomography (MSCT) provide valuable information of plaque from different respects.49−51 However, these modalities lack the compositional contrast. An emerging technology provides the compositional information of the lipid by a combination of NIR spectroscopy and $\mathrm { I V U S } , ^ { 5 2 }$ but it has limited capability in characterizing the size of the lipid core, which is critical for characterization of plaque vulnerability. For the purpose of diagnosis, prognosis, and therapeutic treatment assessment, an imaging tool that can provide reliable information about the atherosclerotic plaques in a clinical setting is critically needed.

An IVPA catheter utilizing vibrational absorption as the contrast mechanism is potentially a game changer. As shown in Figure ${ \bf 6 A , B , }$ the lipid-rich core presents a distinguishable contrast in the presence of luminal blood upon excitation of the first overtone of the CH bond.42 Compared to the second overtone excitation, the first overtone excitation holds advantages of lower scattering and larger signal (Figure 6C,D). Therefore, it is considered as the optimal wavelength for IVPA imaging of an atherosclerotic plaque. The concept of IVPA imaging of the atherosclerotic arterial wall has been demonstrated by several groups.31,36,53,54 Jansen et al. demonstrated in vitro intravascular imaging using a PA probe with 1200 nm excitation of the second overtone of CH bond.36 B. Wang et al. applied the first overtone of CH at 1730 nm as the excitation source to perform the intravascular imaging.37 In their study, the plaque inside of the arterial wall was visualized in the presence of luminal blood, suggesting no requirement for a saline flush in an IVPA imaging procedure. This feature is critical because it makes IVPA naturally compatible with the IVUS modality that is widely used in clinics. Figure 7 presents the first result of using second overtone absorption of CH as a contrast to visualize the atherosclerotic plaque in an endoscopic setting. As seen in the figure, the lipid distribution is clearly mapped under 1210 nm excitation.36 Although the development of the IVPA catheter is still at its early stage, its bright future is clearly foreseen.

![](images/f910be93e8a9539bafc5dc04a47f4bd94e6b4afc05f7ee313a807080d8cd5c55.jpg)  
Figure 5. Microscopic PA imaging of biological systems using the overtone transition as a contrast. (A) 3-D PA microscopy of intramuscular fat. The right bottom is the photograph of the same region. (B) PA microscopy of a spinal cord cross section. (C) In vivo 3-D PA microscopy of lipid accumulation in Drosophila larva. The right bottom shows the spectra of selected locations. (C) is adapted from ref 31. Copyright 2011 by the American Physical Society.

A key value of vibration-based PA imaging is the spectral information embedded in a vibrational overtone spectrum. By

## Multispectral vibrational PA imaging differentiates multiple components in a biological specimen.

making use of the distinctive spectral profiles of CH and CH groups in the first CH overtone bands, Pu Wang et al. demonstrated selective imaging of CH -rich fat and CH -rich collage through multispectral PA imaging in the window from 1650 to 1850 nm.43 This area of study is important because lipid deposition and collagen remodeling occur in many kinds of human diseases, including atherosclerosis and fatty liver diseases.55,56

For quantitative analysis of the multispectral PA images, Wang et al. exploited the multivariate curve resolution alternating least squares (MCR-ALS) method57 to recover the concentration maps and spectral profiles of fat and collagen.43 Compared to the linear inversion method, which determines the concentration maps by least-squares fitting of

![](images/fab443d519064a92a4eca3feeaca6be8b904b1cc443f4f9c2d8e4dd2826bbad4.jpg)  
Figure 6. PA imaging and spectroscopy of arterial plaque in the presence of blood. (A) Schematic for PA imaging of an artery through whole blood. (B) 3-D imaging of arterial plaque by 1730 nm excitation. Lumen and blood are indicated with red arrows. To precisely control the thickness at 0.5 mm, the blood was sandwiched between two cover glasses. As the result, the ultrasound signal from the blood layer was reflected by the glasses multiple times, which generated an interference pattern of the signal from blood. (C) PA image at a selected $_ { x - z }$ plane under 1730 nm excitation. (D) PA image at a selected x−z plane under 1210 nm excitation. (E) PA spectrum taken at the lipid deposition pointed out by the red arrow in (C). Scale bar: 1 mm. Adapted from ref 42. Copyright 2012, Wiley− VCH.

![](images/7e22f8c58bd953ff0033a53101b96774ca8451b7f0e3bacd3ed94cfe31c4997a.jpg)

<details>
<summary>text_image</summary>

A
*
Ca
Pf
Lu
Pf
</details>

![](images/d3c49bfca38a2ac88df67c1c3ddb6f0dccbb23dfa938be8e1694c9bf64a199bd.jpg)

<details>
<summary>natural_image</summary>

Circular grayscale medical scan image showing concentric rings with a central dark core and an arrow pointing to a feature, labeled 'B' in top-left corner (no other text or symbols)
</details>

![](images/4a054ae8dc2cfa6ca4e9ed833ce6c31ba50346fbdc3a0102c35b553946ca234a.jpg)

<details>
<summary>natural_image</summary>

Circular scientific visualization with concentric rings and a central bright spot, no text or symbols present
</details>

![](images/185fb0affcb212805663240a4075335b4123c6f25b69d582412d1a7fcdeb6d5d.jpg)

<details>
<summary>natural_image</summary>

Circular scientific image showing concentric rings with a central core and directional arrows, scale bar indicates 1 mm (no text or symbols present)
</details>

Figure 7. IVPA/IVUS imaging of an advanced human atherosclerotic plaque. (A) Histology: an oil red O stain shows the presence of a lipidrich plaque (∗) as well as a calcified area (Ca). Lu, lumen; Pf, periadventitial fat. (B) IVUS image. IVPA images at (C) 1210 (high lipid absorption) and (D) 1230 nm (low lipid absorption). Arrow heads indicate the needle used for marking. Adapted from ref 36. Copyright 2011, The Optical Society.

the multispectral images using known spectral profiles of pure components, MCR analysis has two advantages. First, by applying principal component analysis and MCR, one can determine the major components of a specimen and map the concentrations of each component without a priori knowledge of the chemical compositions and their spectroscopic information. Therefore, this method can be potentially used for real tissue analysis where the spectral profiles of major components are unknown. Second, when dealing with deep tissue spectral analysis, a simple linear inversion method fails because complex light scattering and absorption in deep tissue alter the spectral profiles. On the other hand, the MCR-ALS method uses the spectral profiles from the pure components as initial input for the iterative optimization. Once the selfoptimization process reaches a convergence, the finally resolved spectral profiles match the real spectral profiles of the components in deep tissue. In MCR-ALS analysis, the constructed multispectral image as a 3-D matrix $( x \times z \times \lambda )$ is unfolded into a 2-D matrix D with the size of $( ( x \times z ) \times \lambda )$ , in which the rows are spectra of different pixels. This data set is fit by a bilinear model to produce two matrices, C and $\mathbf { S } ^ { \mathrm { T } } ,$ , plus an error matrix, $\mathbf { E } ,$ expressed as

$$
\mathbf {D} = \mathbf {C S} ^ {\mathrm{T}} + \mathbf {E} \tag {3}
$$

Each row in $\mathbf { S } ^ { \mathrm { T } } ,$ which has the size $( q \times \lambda ) .$ , represents the spectrum of one of the q chemical components. Each column in $\mathbf { C } ,$ which is sized $( ( x \times z ) \times q )$ , represents the distribution of one of the q components. The matrix C is then refolded to q images, representing a distribution map of $q$ chemical components. An ALS algorithm58 is exploited to solve the MCR bilinear model. This algorithm iteratively optimizes the spectral matrix $\mathbf { S } ^ { \mathbf { T } }$ and the distribution matrix $\mathbf { C } ,$ with the aid of various constraints (e.g., non-negativity, unimodality, closure) according to the chemical properties and origin of mathematics to reduce the ambiguity.59,60

To demonstrate the value of multispectral PA imaging of chemical bond vibration, Wang et al. conducted a study that differentiated collagen and fat in a phantom composed of rat tail tendon (rich in collagen) and adipose tissue (rich in lipids).43 Multispectral photoacoustic imaging and MCR-ALS analysis of an atherosclerotic artery is demonstrated in Figure 8. A total of 21 wavelengths from 1700 to 1830 nm, which covers the first overtone region of the C−H bond, were scanned to construct a multispectral image stack. The images at selected wavelengths are shown in Figure 8A. In order to obtain the contrast between the lipid and connective tissue, MCR-ALS analysis was applied to obtain the chemical maps (Figure 8B). Component 1 is assigned as a deposited lipid because its profile resembles that of $\mathrm { C H } _ { 2 }$ groups enriched in lipid. Component 2 is attributed to the connective tissue because its spectral profile resembles that of $\mathrm { C H } _ { 3 }$ groups enriched in proteins. Comparison of spectra obtained from the MCR-ALS analysis and typical overtone spectra of $\mathrm { C H } _ { 2 }$ and $\mathrm { C H } _ { 3 }$ groups further validated the assignments (Figure 8C). The spectrum of component 1 shows two peaks at 1725 and 1760 nm, which are the first overtone of the stretching mode of the CH group. The spectrum of component 2 shows a peak at ∼1700 nm, where the peak of first overtone of the $\mathrm { C H } _ { 3 }$ group is located. As $\mathrm { C H } _ { 3 }$ groups are highly abundant in protein, we assign the spectrum of component 2 to collagen-containing connective tissue or smooth muscle tissue. The histology image of the investigated sample with standard Masson’s trichrome staining is shown in Figure 8D. The white color in the histology image indicates the deposition of the lipid, whereas collagen was stained in blue, and smooth muscle tissue was stained in red. The photo acoustic compositional mapping agreed well with standard histology. We note that quantification of the concentration of chemical components in deep tissue is challenging due to the fact that spectral profiles of the major components are corrupted by the wavelength dependence of the fluence distribution. The traditional linear inversion method fails because complex light scattering and absorption in deep tissue alter the spectra profiles. The MCR-ALS method uses the spectral profiles from the pure components as initial input for the iterative optimization. Once the self-optimization process reaches a convergence, the finally resolved spectral profiles match the real spectral profiles of the components in deep tissue. However, the MCR analysis is also based on a linear model. Therefore, the nonlinear behavior of the spectral profile in different depths of a tissue cannot be fully addressed by MCR-ALS. Advanced analytical methods need to be developed in order to quantify the chemical components in deep tissue.

![](images/236b14dac0f0bb7e7a38822f250fc1f2f2dc82b36e9db90aa600c35bdd16f4b1.jpg)  
Figure 8. Multispectral PA imaging of a plaque artery and MCR-ALS analysis. (A) Selected images from a 21 wavelength multispectral PA image. (B) Composition maps of the two components derived from the MCR-ALS analysis. (C) Spectral profiles recovered from augmented MCR-ALS analysis. (D) Histology image of the same artery tissue at a selected cross section.

## An imaging depth at the centimeter scale is possible with vibration-based PA tomography.

As the output signal in response to the input photons is acoustic waves in PA tomography (PAT), this imaging modality is not prone to scattering and therefore is capable of imaging a biological sample of several centimeters in size.13 Although scattering deteriorates the depth resolution in pure optical imaging, PAT makes use of it for uniform illumination. On the basis of electronic absorption in the visible or near-infrared regions, PAT imaging of various organs sized in the centimeter scale has been demonstrated.13,15,24,61−63 Vibration-based PAT is promising based on the following considerations. First, in PAT, the imaging depth mainly depends on the light fluence at the target. Because the output signal amplitude scales with the laser fluence and the whole volume of the sample is illuminated, a laser source with high energy per pulse is required. Such a source is possible through a Raman laser pumped by a Nd:YAG laser.64 Second, the presence of background absorbers in the sample affects the imaging depth as it prevents light penetration into the deep due to attenuation. This concern can be circumvented by selecting a wavelength where the background absorbers have medium absorption. The two windows, 1150− 1250 and 1700−1760 nm, are preferred as water, the dominant absorber at these wavelengths, is less absorbing as compared to the absorption due to the overtone vibrational transition of the CH bond. Third, on the basis of the ANSI safety limit,65 the maximum permissible exposure (MPE) is ${ \sim } 2 0 ~ \mathrm { m J / c m } ^ { 2 }$ at awavelength of 800 nm, 100 mJ/cm2 at a wavelength of 1200 nm, and $\breve { 1 } \mathrm { J } / \mathrm { c m } ^ { 2 }$ at a wavelength of 1700 nm. Therefore, for PA imaging at the two aforementioned windows, the input light fluence can be increased by about 5−50 times compared to that in the 800 nm region. This will increase the output acoustic signal as it scales with the input light fluence, so that a good signal-to-noise ratio at the desired imaging depth can be obtained. These advantages render it promising to transform molecular spectroscopy, a hard core of physical chemistry, into a biomedical device that sees the unseen inside of the human body. Such a platform holds great potential in noninvasive diagnosis of prostate cancer, breast cancer, fatty liver, cardiovascular plaques, and other disorders.

## AUTHOR INFORMATION

## Corresponding Author

\*E-mail: jcheng@purdue.edu.

## Notes

The authors declare no competing financial interest.

## Biographies

Pu Wang received a B.S. degree in physics from Fudan University, China, and M.S. degree in medical biophysics from Indiana University School of Medicine. He is currently working toward his Ph.D. degree in biomedical engineering at Purdue University. His research interests include nonlinear optical microscopy and photoacoustic imaging and spectroscopy.

Justin R. Rajian received his Ph.D. in Physics from Indian Institute of Technology Madras, Chennai, India. His research interests include photoacoustic tomography, ultrafast laser spectroscopy, and glass transition dynamics.

Ji-Xin Cheng received a B.S. degree and Ph.D. degree in the Department of Chemical Physics from the University of Science and Technology of China. He is currently a Professor at the Weldon School of Biomedical Engineering at Purdue University. His research lab develops label-free spectroscopic imaging tools and nanotechnologies for challenging applications in biomedicine. Website link: http://www.chem.purdue.edu/jcheng/

## ACKNOWLEDGMENTS

This work is supported by a NIH R21 Grant EB015901 to J.X.C. and an AHA fellowship to P.W.

## REFERENCES

(1) Morris, M. D.; Mandair, G. S. Biomedical Applications of Raman Imaging. Raman, Infrared, and Near-Infrared Chemical Imaging; John Wiley & Sons, Inc.: New York, 2010; pp 109−131.  
(2) Shaw, R. A.; Kupriyanov, V. V.; Jilkina, O.; Sowa, M. G. Near-Infrared In Vivo Spectroscopic Imaging: Biomedical Research and Clinical Applications. In Raman, Infrared, and Near-Infrared Chemical Imaging; John Wiley & Sons, Inc.: New York, 2010; pp 149−165.  
(3) Fernandez, D. C.; Bhargava, R.; Hewitt, S. M.; Levin, I. W. Infrared Spectroscopic Imaging for Histopathologic Recognition. Nat. Biotechnol. 2005, 23, 469−474.  
(4) Duncan, M. D.; Reintjes, J.; Manuccia, T. J. Scanning Coherent Anti-Stokes Raman Microscope. Opt. Lett. 1982, 7, 350−352.  
(5) Zumbusch, A.; Holtom, G. R.; Xie, X. S. Three-Dimensional Vibrational Imaging by Coherent Anti-Stokes Raman Scattering. Phys. Rev. Lett. 1999, 82, 4142−4145.  
(6) Ploetz, E.; Laimgruber, S.; Berner, S.; Zinth, W.; Gilch, P. Femtosecond Stimulated Raman Microscopy. Appl. Phys. B: Laser Opt. 2007, 87, 389−393.  
(7) Freudiger, C. W.; Min, W.; Saar, B. G.; Lu, S.; Holtom, G. R.; He, C.; Tsai, J. C.; Kang, J. X.; Xie, X. S. Label-Free Biomedical Imaging with High Sensitivity by Stimulated Raman Scattering Microscopy. Science 2008, 322, 1857−1861.  
(8) Cheng, J.-X.; Xie, X. S. Coherent Raman Scattering Microscopy; CRC Press: Boca Raton, FL, 2012.  
(9) Colak, S. B.; van der Mark, M. B.; t Hooft, G. W.; Hoogenraad, J. H.; van der Linden, E. S.; Kuijpers, F. A. Clinical Optical Tomography and NIR Spectroscopy for Breast Cancer Detection. IEEE J. Sel. Top. Quantum Electron. 1999, 5, 1143−1158.  
(10) Schulmerich, M. V.; Cole, J. H.; Dooley, K. A.; Morris, M. D.; Kreider, J. M.; Goldstein, S. A.; Srinivasan, S.; Pogue, B. W. Noninvasive Raman Tomographic Imaging of Canine Bone Tissue. J. Biomed. Opt. 2008, 13, 020506−020506.  
(11) Bell, A. G. On the Production and Reproduction of Sound by Light. Am. J. Sci. 1880, 20, 305−324.  
(12) Wang, L. V. Photoacoustic Imaging and Spectroscopy; CRC Press: Boca Raton, FL, 2009.  
(13) Wang, L. V.; Hu, S. Photoacoustic Tomography: In Vivo Imaging from Organelles to Organs. Science 2012, 335, 1458−1462.  
(14) Ntziachristos, V. Going Deeper Than Microscopy: The Optical Imaging Frontier in Biology. Nat. Methods 2010, 7, 603−614.  
(15) Wang, X.; Pang, Y.; Ku, G.; Xie, X.; Stoica, G.; Wang, L. V. Noninvasive Laser-Induced Photoacoustic Tomography for Structural and Functional in Vivo Imaging of the Brain. Nat. Biotechnol. 2003, 21, 803806.  
(16) Zhang, H. F.; Maslov, K.; Stoica, G.; Wang, L. V. Functional Photoacoustic Microscopy for High-Resolution and Noninvasive In Vivo Imaging. Nat. Biotechnol. 2006, 24, 848−851.  
(17) Zhang, E. Z.; Laufer, J. G.; Pedley, R. B.; Beard, P. C. In Vivo High-Resolution 3d Photoacoustic Imaging of Superficial Vascular Anatomy. Phys. Med. Biol. 2009, 54, 1035.  
(18) Akers, W. J.; Kim, C.; Berezin, M.; Guo, K.; Fuhrhop, R.; Lanza, G. M.; Fischer, G. M.; Daltrozzo, E.; Zumbusch, A.; Cai, X.; et al. Noninvasive Photoacoustic and Fluorescence Sentinel Lymph Node Identification Using Dve-Loaded Perfluorocarbon Nanoparticles. ACS Nano 2010, 5, 173−182.  
(19) Kim, C.; Song, H.-M.; Cai, X.; Yao, J.; Wei, A.; Wang, L. V. In Vivo Photoacoustic Mapping of Lymphatic Systems with Plasmon Resonant Nanostars. J. Mater. Chem. 2011, 21, 2841−2844.  
(20) Moon, G. D.; Choi, S.-W.; Cai, X.; Li, W.; Cho, E. C.; Jeong, U.; Wang, L. V.; Xia, Y.; New Theranostic, A. System Based on Gold Nanocages and Phase-Change Materials with Unique Features for Photoacoustic Imaging and Controlled Release. J. Am. Chem. Soc. 2011, 133, 4762−4765.  
(21) Galanzha, E. I.; Shashkov, E. V.; Kelly, T.; Kim, J.-W.; Yang, L.; Zharov, V. P. In Vivo Magnetic Enrichment and Multiplex Photoacoustic Detection of Circulating Tumour Cells. Nat. Nano technol. 2009, 4, 855−860.  
(22) Kim, J.-W.; Galanzha, E. I.; Shashkov, E. V.; Moon, H.-M.; Zharov, V. P. Golden Carbon Nanotubes as Multimodal Photoacoustic and Photothermal High-Contrast Molecular Agents. Nat. Nanotechnol. 2009, 4, 688−694.  
(23) Zharov, V. P. Ultrasharp Nonlinear Photothermal and Photoacoustic Resonances and Holes Beyond the Spectral Limit. Nat. Photonics 2011, 5, 110−116.  
(24) Razansky, D.; Distel, M.; Vinegoni, C.; Ma, R.; Perrimon, N.; Koster, R. W.; Ntziachristos, V. Multispectral Opto-Acoustic Tomography of Deep-Seated Fluorescent Proteins In Vivo. Nat. Photonics 2009, 3, 412417.  
(25) Wilson, K.; Homan, K.; Emelianov, S. Biomedical Photo acoustics Beyond Thermal Expansion Using Triggered Nanodrople Vaporization for Contrast-Enhanced Imaging. Nat. Commun. 2012, 3, 618.  
(26) Siesler, H. W.; Ozaki, Y.; Kawata, S.; Heise, H. M. Near-Infrared Spectroscopy: Principles, Instruments, Applications; Wiley-VCH: Weinheim, Germany, 2002.  
(27) Barrett, J. J.; Berry, M. J. Photoacoustic Raman Spectroscopy (PARS) Using CW Laser Sources. Appl. Phys. Lett. 1979, 34, 144−146.  
(28) Wang, H.; Fu, Y.; Cheng, J.-X. Experimental Observation and Theoretical Analysis of Raman Resonance-Enhanced Photodamage in Coherent Anti-Stokes Raman Scattering Microscopy. J. Opt. Soc. Am. B 2007, 24, 544−552.  
(29) Yakovlev, V. V.; Noojin, G. D.; Denton, M. L.; Rockwell, B. A.; Thomas, R. J. Monitoring Stimulated Raman Scattering with Photoacoustic Detection. Opt. Lett. 2011, 36, 1233−1235.  
(30) Yakovlev, V. V.; Zhang, H. F.; Noojin, G. D.; Denton, M. L.; Thomas, R. J.; Scully, M. O. Stimulated Raman Photoacoustic Imaging. Proc. Natl. Acad. Sci. U.S.A. 2010, 107, 20335−20339.  
(31) Wang, H.-W.; Chai, N.; Wang, P.; Hu, S.; Dou, W.; Umulis, D.; Wang, L. V.; Sturek, M.; Lucht, R.; Cheng, J.-X. Label-Free Bond-Selective Imaging by Listening to Vibrationally Excited Molecules. Phys. Rev. Lett. 2011. 106, 238106.  
(32) Patel, C. K. N.; Tam, A. C. Optoacoustic Spectroscopy of Liquids. Appl. Phys. Lett. 1979, 34, 467−470.  
(33) Patel, C. K. N.; Tam, A. C. Optical Absorption Coefficients of Water. Nature 1979. 280. 302304.  
(34) Patel, C. K. N.; Tam, A. C.; Kerl, R. J. High Overtones of C−H Stretch in Liquid Benzene Measured by Laser Optoacoustic Spectroscopy. J. Chem. Phys. 1979, 71, 1470−1474.  
(35) Tam, A. C.; Patel, C. K. N. Optical Absorptions of Light and Heavy Water by Laser Optoacoustic Spectroscopy. Appl. Opt. 1979, 18, 3348−3358.  
(36) Jansen, K.; van der Steen, A. F. W.; van Beusekom, H. M. M.; Oosterhuis, J. W.; van Soest, G. Intravascular Photoacoustic Imaging of Human Coronary Atherosclerosis. Opt. Lett. 2011, 36, 597−599.  
(37) Wang, B.; Karpiouk, A.; Yeager, D.; Amirian, J.; Litovsky, S.; Smalling, R.; Emelianov, S. Intravascular Photoacoustic Imaging of Lipid in Atherosclerotic Plaques in the Presence of Luminal Blood. Opt. Lett. 2012, 37, 1244−1246.  
(38) Allen, T. J.; Hall, A.; Dhillon, A. P.; Owen, J. S.; Beard, P. C. Spectroscopic Photoacoustic Imaging of Lipid-Rich Plaques in the Human Aorta in the 740 to 1400 nm Wavelength Range. J. Biomed. Opt. 2012, 17, 061209−1.  
(39) Cias, P.; Wang, C.; Dibble, T. S. Absorption Cross-Sections of the CH Overtone of Volatile Organic Compounds: 2 Methyl-1,3- butadiene (Isoprene), 1,3-Butadiene, and 2,3-Dimethyl-1,3-butadiene. Appl. Spectrosc. 2007, 61, 230−236.  
(40) Xu, Z.; Li, C.; Wang, L. V. Photoacoustic Tomography of Water in Phantoms and Tissue. J. Biomed. Opt. 2010, 15, 036019−036019.  
(41) Jerry Workman, L. W. Practical Guide to Interpretive near-Infrared Spectroscopy; CRC Press: Boca Raton, FL, 2007.  
(42) Wang, P.; Wang, H.-W.; Sturek, M.; Cheng, J.-X. Bond-Selective Imaging of Deep Tissue through the Optical Window between 1600 and 1850 Nm. J. Biophotonics 2012, 5, 25−32.  
(43) Wang, P.; Wang, P.; Wang, H.-W.; Cheng, J.-X. Mapping Lipid and Collagen by Multispectral Photoacoustic Imaging of Chemical Bond Vibration. J. Biomed. Opt. 2012, 17, 096010/1−.  
(44) Schick, F.; Machann, J.; Brechtel, K.; Strempfer, A.; Klumpp, B.; Stein, D. T.; Jacob, S. MRI of Muscular Fat. Magn. Reson. Med. 2002, 47, 720−727.  
(45) Baker, K. D.; Thummel, C. S. Diabetic Larvae and Obese Flies Emerging Studies of Metabolism in Drosophila. Cell Metab. 2007, 6, 257−266.  
(46) Slaidina, M.; Delanoue, R.; Gronke, S.; Partridg, L.; Leopold, P.́ A Drosophila Insulin-Like Peptide Promotes Growth During Nonfeeding States. Dev. Cell 2009, 17, 874−884.  
(47) Members, W. G.; Roger, V. L.; Go, A. S.; Lloyd-Jones, D. M.; Benjamin, E. J.; Berry, J. D.; Borden, W. B.; Bravata, D. M.; Dai, S.; Ford, E. S.; et al. Heart Disease and Stroke Statistics2012 Update. Circulation 2012, 125, e2−e220.  
(48) Naghavi, M.; Libby, P.; Falk, E.; Casscells, S. W.; Litovsky, S.; Rumberger, J.; Badimon, J. J.; Stefanadis, C.; Moreno, P.; Pasterkamp,  
G.; et al. From Vulnerable Plaque to Vulnerable Patient. Circulation 2003, 108, 1664−1672.  
(49) Choudhury, R. P.; Fuster, V.; Fayad, Z. A. Molecular, Cellular and Functional Imaging of Atherothrombosis. Nat. Rev. Drug Discovery 2004, 3, 913−925.  
(50) Fayad, Z. A.; Fuster, V. Clinical Imaging of the High-Risk or Vulnerable Atherosclerotic Plaque. Circ. Res. 2001, 89, 305−316.  
(51) Sanz, J.; Fayad, Z. A. Imaging of Atherosclerotic Cardiovascular Disease. Nature 2008, 451, 953−957.  
(52) Madder, R. D.; Steinberg, D. H.; Anderson, R. D. Multimodality Direct Coronary Imaging with Combined Near-Infrared Spectroscopy and Intravascular Ultrasound: Initial US Experience. Catheter Cardiovasc. Interv. 2013, 81, 551−557.  
(53) Allen, T. J.; Beard, P. C. Photoacoustic Characterisation of Vascular Tissue at NIR Wavelengths. Proc. SPIE 2009, 71770A.  
(54) Wang, B.; Su, J. L.; Karpiouk, A. B.; Sokolov, K. V.; Smalling, R. W.; Emelianov, S. Y. Intravascular Photoacoustic Imaging. IEEE J. Sel. Top. Quantum Electron. 2010, 16, 588−599.  
(55) Lusis, A. J. Atherosclerosis. Nature 2000, 407, 233−241.  
(56) Cohen, J. C.; Horton, J. D.; Hobbs, H. H. Human Fatty Liver Disease: Old Questions and New Insights. Science 2011, 332, 1519− 1523.  
(57) de Juan, A.; Tauler, R. Multivariate Curve Resolution (MCR) from 2000: Progress in Concepts and Applications. Crit. Rev. Anal. Chem. 2006, 36, 163−176.  
(58) Jaumot, J.; Gargallo, R.; de Juan, A.; Tauler, R. A Graphical User-Friendly Interface for MCR-ALS: A New Tool for Multivariate Curve Resolution in Matlab. Chemom. Intell. Lab. 2005, 76, 101−110.  
(59) Bro, R.; De Jong, S. A Fast Non-Negativity-Constrained Leas Squares Algorithm. J. Chemometrics 1997, 11, 393−401.  
(60) Bro, R.; Sidiropoulos, N. D. Least Squares Algorithms under Unimodality and Non-Negativity Constraints. J. Chemometrics 1998, 12, 223−247.  
(61) Wang, X.; Chamberland, D. L.; Jamadar, D. A. Noninvasive Photoacoustic Tomography of Human Peripheral Joints toward Diagnosis of Inflammatory Arthritis. Opt. Lett. 2007, 32, 3002−3004.  
(62) Kruger, R. A.; Lam, R. B.; Reinecke, D. R.; Del Rio, S. P.; Doyle, R. P. Photoacoustic Angiography of the Breast. Med. Phys. 2010, 37, 6096−6100.  
(63) Gamelin, J.; Maurudis, A.; Aguirre, A.; Huang, F.; Guo, P.; Wang, L. V.; Zhu, Q.; Real-Time Photoacoustic, A. Tomography System for Small Animals. Opt. Express 2009, 17, 10489−10498.  
(64) Li, R.; Slipchenko, M. N.; Wang, P.; Cheng, J.-X. Compact High Power Barium Nitrite Crystal-Based Raman Laser at 1197 nm for Photoacoustic Imaging of Fat. J. Biomed. Opt. 2013, 18, 040502.  
(65) ANSI.2012: American National Standard for Safe Use of Lasers in Research, Development, or Testing. ANSI Z136.8-2012; American National Standards Institute: Washington, DC, 2012.