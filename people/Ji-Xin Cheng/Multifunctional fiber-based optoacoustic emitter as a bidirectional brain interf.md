# Multifunctional Fiber-Based Optoacoustic Emitter as a Bidirectional Brain Interface

Nan Zheng, Ying Jiang, Shan Jiang, Jongwoon Kim, Guo Chen, Yueming Li, Ji-Xin Cheng, Xiaoting Jia,\* and Chen Yang\*

A bidirectional brain interface with both “write” and “read” functions can be an important tool for fundamental studies and potential clinical treatments for neurological diseases. Herein, a miniaturized multifunctional fiber-based optoacoustic emitter (mFOE) is reported thatintegrates simultaneous optoacoustic stimulation for “write” and electrophysiology recording of neural circuits for “read”. Because of the intrinsic ability of neurons to respond to acoustic wave, there is no requirement of the viral transfection. The orthogonality between optoacoustic waves and electrical field provides a solution to avoid the interference between electrical stimulation and recording. The stimulation function of the mFOE is first validated in cultured ratcortical neurons using calcium imaging. In vivo application of mFOE for successful simultaneous optoacoustic stimulation and electrical recording of brain activities is confirmed in mouse hippocampus in both acute and chronical applications up to 1 month. Minor brain tissue damage is confirmed after these applications. The capability of simultaneous neural stimulation and recording enabled by mFOE opens up new possibilities for the investigation of neural circuits and brings new insights into the study of ultrasound neurostimulation.

## 1. Introduction

Bidirectional communication with dynamic local circuits inside the brain of individual behaving animals or humans has been an invaluable approach for fundamental studies of neural circuits and for effective clinical treatment of neurological diseases, like epilepsy, Parkinson’s disease, and depression.[1,2] Additionally, bidirectional neural interface paves the way for the closed-loop control, as it could enable more sophisticated, real-time control over neural dynamics[3] behaviors[4] and achieve effective therapeutic effect in neurological disease.[5,6] To achieve real time assessment of the stimulated outcome, neural interfaces with ability to simultaneously manipulate and directly monitor the neural activities are preferred. Among the technologies developed in past decades, electrical stimulation and electrophysiology recording have been widely used and form the basis of current implantable devices, which has been applied to clinical applications[7] For example, to restore both the motor and sensory modalities, electric stimulation of the cortical surface is often associated with electrophysiology recording[8,9] like electrocorticography

(ECoG). Also, the electrical stimulation and recording system has demonstrated promising treatment effect in neurological

N. Zheng

Division of Materials Science and Engineering

Boston University

Boston, MA 02215, USA

Y. Jiang, J.-X. Cheng

Department of Biomedical Engineering

Boston University

Boston, MA 02215, USA

![](images/6f787b784179f4ad47f3428b5ef73457b6be88a1d955bb2af01bf5e72ac63389.jpg)

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/adhm.202300430

© 2023 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.

DOI: 10.1002/adhm.202300430

S. Jiang, J. Kim, X. Jia

Bradley Department of Electrical and Computer Engineering

Virginia Tech

Blacksburg, VA 24061, USA

E-mail: xjia@vt.edu

G. Chen, J.-X. Cheng, C. Yang

Department of Electrical and Computer Engineering

Boston University

Boston, MA USA

E-mail: cheyang@bu.edu

Y. Li

Department of Mechanical Engineering

Boston University

Boston, MA 02215, USA

X. Jia

Department of Materials Science and Engineering

Virginia Tech

Blacksburg, VA 24061, USA

C. Yang

Department of Chemistry

Boston University

Boston, MA 02215, USA

diseases, such as epilepsy. The responsive neurostimulation (RNS) system, leveraging ECoG recording as the trigger to provide stimulation, showed a statistically significantly greater re duction in seizure frequency, and the benefits increased over time in a two-year study.[10,11] However, the current-controlled or voltage-controlled stimulation field may interfere with the electrical signals used for recording, leading to artifacts in electrophysiology recording.[2,12] Although researchers are improving its performance through technologies such as current steering,[13] novel electrode design,[14] and artifacts cancellation,[15] considering the intrinsic conductivity of brain tissue,[16] the artifact issues is hard to be fully eliminated. Therefore, electrical stimulation for the bidirectional communication of brain may not be the ideal candidate, especially when working with the electrophysiology recording.

Exploring alternative neuromodulation methods that are orthogonal with electrical recording and potentially improve the spatial resolution of modulation could offer a new bidirectional brain interface for fundamental studies and clinical applications. Optogenetics is a powerful method that utilizes light and transfected opsins to control and manipulate neurons in brain and other neural systems with cell specificity.[17] It targets and modulates only cells that express the photosensitive channels of interest, while leaving other cells unaffected.[18] This further boosts the stimulation selectivity within the spatial pattern of illumination. To take this advantage, early efforts developed so-called optoelectrodes by simply assembling the optical fibers for optogenetics stimulation with the electrodes, such as Utah arrays,[19–21] Michigan probes[22,23] and microwires.[24] Semiconductor fabrication techniques and multiple material processing methods have recently been applied to improve the integration of those bidirectional devices. New processing techniques not only make the device more compact but also strengthen its functionality and biocompatibility. For example, monolithically integrated microlight-emitting-diodes (μLEDs) were used to reduce the complexity of light-guide structures and significantly boosted the number of stimulation sites and stimulation resolution.[25,26] Alternatively, a high-throughput thermal drawing method has been used to integrate the function components, for example, elec trodes, microfluidic channels, and optical waveguides, to the flex ible multifunctional polymer fiber.[27,28] Through this approach, the flexible fiber probes showed low bending-stiffness and enabled multifunctionalities, including optical waveguide, electrical recording and drug delivery.[29–31] Optogenetics utilizing the expression of light-sensitive opsins in neurons through gene modification[28] enables cell specificity. However, it also impose challenges of low efficiency in viral transfection and safety when applying optogenetics to non-human primates and human,[32] limiting its further applications in fundamental studies in primates and clinical applications. Photothermal modulation also leverages the optical waveguide developed in a variety of interfaces to perturb neural activity.[33,34] For example, Meneghetti et al. developed a soft fiber-based device to deliver the infrared laser pulse in the 2 μm spectral region while recording electrophysiological signals,[35] but the infrared laser illumination on the seconds scale raises some safety concerns for thermal toxicity in clinical applications.[36] In addition, chemical modulator using the drug delivery capability of the multifunctional neural probe can also work with a pathologic electrophysiological recording,[37] but have a limited spatiotemporal resolution.

Recently, our team showed optoacoustic neural stimulation with a high spatial resolution up to single neuron level.[38,39] In an optoacoustic process, the pulsed light is illuminated on an absorber, causing transient heating and thermal expansion, and generating broadband acoustic pulses at ultrasonic frequencies.[40,41] As a light-mediated neural modulation method, optoacoustic is an ideal candidate to work with electrical recording for bidirectional neural communication. Compared with existing technologies, it exhibited the advantages as a lightmediated method, including a high spatial resolution and minimal crosstalk noise with electrical recording. Importantly, the optoacoustic neurostimulation alleviates the challenges and safety concern in optogenetics since no viral transfection is required.

Here, we developed a multifunctional fiber-based optoacoustic emitter (mFOE) as a miniaturized bidirectional brain interface performing simultaneously neural stimulation and electrical recording of the neural activities. Through a thermal drawing process,[27,42] fabrication of mFOE integrated an optical waveguide and multiple electrodes within a single fiber with a total diameter of 300 μm, comparable to the typical size of silica fibers used in optogenetic studies. An optoacoustic coating was selectively deposited to the tip of the core optical waveguide in the mFOE through a controlled micro-injection process. Upon nanosecond pulse laser delivered to the photoacoustic coating, the mFOE generates a peak-to-peak pressure greater than 1 MPa, confirmed by the hydrophone measurement, which is sufficient for successful neural stimulation in vitro and in vivo. By calcium imaging, the optoacoustic stimulation function of the mFOE was validated in Oregon green-loaded rat primary neurons. Importantly, we demonstrated the reliable functions of the chronic implanted mFOE for simultaneously stimulating and recording neurons in mouse hippocampus. Chronic recording also demonstrated that the embedded electrodes could monitor both the local field potential and spike activities in the mouse brain. The histological evaluation of the brain tissue response confirmed that our flexible mFOE established a stable and biocompatible multifunctional neural interface. mFOE is the first device integrated both optoacoustic stimulation with electrical recording for bidirectional neural communication. With the bidirectional capabilities and excellent biocompatibility, it offers a tool probing brain circuits, alternative to the optoelectrode devices, with improved feasibility in non-human primates and human. It also opens up potentials for closed-loop neural stimulation and brain machine interface.

## 2. Results

## 2.1. Design, Fabrication, and Characterization of mFOE

Toward bidirectional neural communication, we have designed the mFOE to utilize the optoacoustic stimulation as “writing” and electrophysiological recording as “reading” of the neural interface (Figure 1a). Previously, fiber-based optoacoustic emitters have been developed as a miniature invasive ultrasound transducer for the biomedical applications, such as intravascular imaging and interventional cardiology.[43,44] Recently, our work showed that fiber-based optoacoustic emitters can also be

![](images/f6a1626027f7006495bca35e1b6d76578193252414002cabb97deb08c18437fc.jpg)

<details>
<summary>text_image</summary>

a
Optoacoustic wave
Pulsed laser
Electrical signal
</details>

![](images/253ca1ec9e9f123cea1a5b7a1fd63f97c68743a1f590e5a418a7e31941d606ef.jpg)

<details>
<summary>text_image</summary>

b
Heat
Vdrawing speed
c
Wave guide
(PC/PVDF)
Sacrifice layer (PC)
Electrode (BiSn alloy)
d
Injector on 3D stage
Micro pipette
Fiber
Fiber holder
on 3D stage
</details>

![](images/b3ea52a38c47e0f8baa5edd898af6f64c50152b319624d7a4b3f86b138501712.jpg)

<details>
<summary>line chart</summary>

| Time (μs) | Pressure (MPa) - 41.8 µJ | Pressure (MPa) - 27.3 µJ | Pressure (MPa) - 16.6 µJ | Magnitude (a.u.) - 41.8 µJ | Magnitude (a.u.) - 27.3 µJ | Magnitude (a.u.) - 16.6 µJ |
|-----------|--------------------------|--------------------------|--------------------------|----------------------------|----------------------------|----------------------------|
| 0.0       | 0.0                      | 0.0                      | 0.0                      | 0.0                        | 0.0                        | 0.0                        |
| 0.1       | 0.0                      | 0.0                      | 0.0                      | 0.0                        | 0.0                        | 0.0                        |
| 0.2       | 1.5                      | 1.0                      | 0.5                      | 0.3                        | 0.2                        | 0.1                        |
| 0.3       | 0.0                      | 0.0                      | 0.0                      | 0.0                        | 0.0                        | 0.0                        |
| 0.4       | 0.0                      | 0.0                      | 0.0                      | 0.0                        | 0.0                        | 0.0                        |
| Frequency (MHz) | Magnitude (a.u.) - 41.8 µJ | Magnitude (a.u.) - 27.3 µJ | Magnitude (a.u.) - 16.6 µJ | Frequency (MHz) - 41.8 µJ | Frequency (MHz) - 27.3 µJ | Frequency (MHz) - 16.6 µJ |
|---        | ---                      | ---                      | ---                      | ---                       | ---                       | ---                       |
| 0         | ~0.1                     | ~0.1                     | ~0.1                     | ~0.1                       | ~0.1                       | ~0.1                       |
| 10        | ~0.35                    | ~0.28                    | ~0.25                    | ~0.38                     | ~0.29                     | ~0.22                     |
| 20        | ~0.38                    | ~0.25                    | ~0.2                     | ~0.35                     | ~0.25                     | ~0.18                     |
| 30        | ~0.2                     | ~0.1                     | ~0.1                     | ~0.25                     | ~0.15                     | ~0.1                       |
| 40        | ~0.1                     | ~0.05                    | ~0.05                    | ~0.15                     | ~0.1                       | ~0.05                     |
| 50        | ~0.05                    | ~0.03                    | ~0.03                    | ~0.1                       | ~0.05                     | ~0.03                     |
| 60        | ~0.03                    | ~0.02                    | ~0.02                    | ~0.05                     | ~0.03                     | ~0.02                     |
| 70        | ~0.02                    | ~0.01                    | ~0.01                    | ~0.03                     | ~0.02                     | ~0.01                     |
| 80        | ~0.01                    | ~0.01                    | ~0.01                    | ~0.02                     | ~0.01                     | ~0.01                     |
| 90        | ~0.01                    | ~0.01                    | ~0.01                    | ~0.01                     | ~0.01                     | ~0.01                     |
| 100       | ~0.0                      | ~0.0                     | ~0.0                     | ~0.0                       | ~0.0                       | ~0.0                       |
</details>

Figure 1. Design, fabrication and characterization of mFOE. a) Schematic of mFOE for bidirectional communication with neurons. Input laser pulse (red) is used to generate optoacoustic waves (black mesh next to the emitter at the mFOE tip) by the emitter. Neural activities are recorded by embedded electrodes (brown) as the output electrical signal (blue). Neurons stimulated are highlight in the tan color, in contrast to the unstimulated neurons in the gray color. b) Illustration of the thermal drawing process. c) Components of the multifunctional fiber, including a PC/PVDF waveguide, BiSn alloy electrodes and PC sacrifice layer. d) The selective deposition process for integrating the optoacoustic converter to the core wave guide in the multifunctional fiber. A pressure-driven micro-injector is used to control the volume of CB/PDMS deposited. 3D translation stages and microscope are used to control the deposition location. Zoom-in: The micro pipette was aligned to the center of the fiber under the microscope. e) Top view microscope image of the mFOE. Scale bar: 100 μm. f) Representative acoustic waveforms under different laser pulse energies recorded by a needle hydrophone. g) Frequency spectrum of acoustic waveforms shown in (f).

applied to neural stimulation in vitro and in vivo, with single neuron resolution and dual site capability.[39,45] In these studies, typically commercial silica fibers were used, together with optoacoustic coating. However, the silica fiber, with Young’s mod ulus of approximately70 GPa, is mismatched with mechanical properties of native neural tissue (kilo- to mega pascals)[2] and not easy to integrate with miniaturized electrodes for recording. In this study, we took advantage of the fiber fabrication method developed by Fink and Anikeeva.[27,42] and utilized the polymer multifunctional fiber design as the base for the mFOE to delivering nanosecond laser to the optoacoustic coating and to record electrical signals. Specifically, a multifunctional fiber with a core optical waveguide and miniaturized electrodes was fabricated using the thermal drawing process (TDP) as previously reported[29] (Figure 1b). The waveguide is made of polycarbonate core (PC, refractive index $\mathtt { n _ { P C } } = 1 . 5 8 6$ , diameter = 150 μm) and polyvinylidene difluoride cladding (PVDF, refractive index $\mathrm { n } _ { \mathrm { P V D F } }$ = 1.426, thickness = 50 μm) as the core and the shell, respectively (Figure 1c). The notable difference in the refractive index of those two materials facilitates efficient light transmission at 1030 nm (loss = 0.38 dB/cm, Figure S1a, Supporting Information). Both polymer materials show a much lower young’s modulus than the commercial silica fiber (Table S1, Supporting Information) and significantly reduce the bending stiffness to 60 N $\mathrm { m } ^ { - 1 } .$ .[ 29 ] BiSn alloy is used in surrounding electrodes with diameters of 35 μm because of its conductivity and compatibility with TDP (Figure 1c). As an implant device, the biocompatibility is also a critical factor when choosing the electrode materials. Based on previous studies, bismuth and its alloy showed very low toxicity or even non-toxicity in the animal and cell experiments.[46–48] This multifunctional fiber showed broadband transmission across the visible range to near infrared region[29,49] and sub-megaohm impedance at 1k Hz (Figure S2, Supporting Information) when it has been prepared into a length about two centimetres.

To integrate the optoacoustic converter to the multifunctional fiber, the optoacoustic coating, composed of light absorbers and thermal expansion matrix, needs to be selectively coated on the core waveguide distal end while keeping the surrounding electrodes exposed and conductive. Compared to our prior FOE fabrication using the dip-coating method,[38,39] here we took several innovative steps. First, a pressure-driven pico-liter injector was used to precisely deposit the optoacoustic materials to the core waveguide distal end. The coating area was controlled through varying the injection volume (0.1–0.5 nL), which is controlled by the regulated pressure (2-4 psi) over a set period of time (1–2 s, Figure S3, Supporting Information) as described in Equation (1),

$$
V = C \cdot d _ {\text {inner}} ^ {3} \cdot p \cdot t \tag {1}
$$

where V is the injection volume, C is a constant attributed to the unit conversion factors, effects of liquid viscosity and the taper angle of micropipette, $d _ { \mathrm { i n n e r } }$ is the inner diameter of the pico-litter injector, p is the pressure, and t is the deposition time. Two 3D translational stages with stereo microscopes were used to precisely control the deposition localization. Second, instead of using carbon nanotubes (CNT), we used carbon black (CB) embedded polydimethylsiloxane (PDMS) as the composite optoacoustic material. CB exhibited similar wideband light absorption[50] (Figure S1b, Supporting Information), assuring the sufficient photoacoustic conversion for neural stimulation. Importantly, due to its relative low viscosity,[51,52] CB/PDMS composite shows much higher injectability compared with CNT/PDMS, therefore more comparable to the picoliter deposition process. Through these steps, we successfully coated 10–20 μm thick 10% w/w CB/PDMS composite onto the 150 μm diameter core waveguide distal end while electrodes were still exposed as shown in Figure 1e. Collectively mFOE with the photoacoustic emitter and multiple electrodes has been successfully fabricated.

To characterize the optoacoustic performance of mFOE, a Qswitched 1030 nm pulsed nanosecond laser with a repetition rate of 1.7 kHz was applied with pulse energies of 16.6, 27.3, and 41.8 μJ, respectively. Each pulse was 3 ns and this short pulse width enabled the thermal and mechanical stress confinement during laser excitation, which was critical to the highly efficient generation of optoacoustic waves. The generated acoustic waves were measured by a 40 μm needle hydrophone placed at about 100 μm away from the fiber tip. The acoustic pulse with a width of approximately0.08 μs was generated by a single laser pulse as shown in Figure 1f. Higher input laser pulse energy led to larger acoustic pressure. A peak-to-peak pressure of 1.0, 1.6, and 2.3 MPa were measured with the pulse energy of 16.6, 27.3, and

41.8 μJ, respectively. The frequency spectrum shows the broadband characteristic of typical optoacoustic waves,[41] and the peak frequencies are around 12.5 MHz (Figure 1g). Based on our previous work,[38,39] we expected that such pressure and frequency are capable to successfully stimulate neurons in vitro and in vivo. To quantify the attenuation of the optoacoustic signal generated by the mFOE, we measured the pressure generated P using the hydrophone and plotted it as a function of distance x from the optoacoustic emitter (Figure S4, Supporting Information). By analyzing the collected pressure data, we derived a fitting curve described by the equation $P = 0 . 9 2 \ ^ { * } e x p ( - x / 3 3 5 . 5 4 ) + \bar { 0 } . 1 8 \ ( \mathrm { R } ^ { 2 } =$ 0.976). According to the fitting curve, the pressure of acoustic wave drops to 1/e of $P _ { 0 }$ at the characteristic distance of 335 μm indicated by the attenuation constant. Considering the attenuation of acoustic wave in soft tissue such as brain is several folds larger than that in water due to the higher absorption and scattering effect,[53] the acoustic wave generated by mFOE is expected to attenuate much faster, with a characteristic length much smaller than 335 μm in the brain tissue than that measured in water. Notably, a small electrode with a similar diameter of 100 μm shows attenuation of the electrical field at a characteristic distance of 100 μm.[54] This suggests that photoacoustic stimulation could have a potential to provide at least a comparable spatial resolution. We also calculated the mechanical index (MI), a commonly used matrix, to evaluate the probability of mechanical damage due to ultrasound generated. The MI of acoustic waves generated by 2.3 MPa is 0.2 (calculation in the Supporting Information), lower than 1.9, the safety threshold suggested by the Food and Drug Administration (FDA) safety guidelines.[55]

## 2.2. mFOE Stimulation of Cultured Primary Neurons

To investigate whether mFOE can directly trigger the neuronal activity, we examined the response of cultured primary neurons under mFOE stimulation. Because of the presence of calcium channels in neuronal membrane and their activation during the depolarization, calcium imaging has been widely used to monitor the neuronal activities.[56,57] Here, we cultured and loaded the rat cortical neurons (days in vitro 10–14) with a calcium indicator, Oregon Green 488 BAPTA-1 dextran (OGD-1)[58] and performed the calcium imaging with an inverted wide-field fluorescence microscope (Figure S5, Supporting Information). To perform the optoacoustic stimulation, mFOE was placed approximately50 μm above the in-focus target neurons (Figure 2a) by a micromanipulator under the microscope. 1030 nm 3 ns pulsed laser with a repetition rate of 1.7 kHz was delivered to the mFOE through an optical fiber. The energy of laser pulse was 41.8 μJ, corresponding to a peak-to-peak pressure of 2.3 MPa generated. Lower energy was tested but did not induce calcium transient. The stimulation duration determined by each laser burst was 100 ms, corresponding to 170 pulses (Figure S6, Supporting Information). By applying 5 bursts of laser pulses with interval of 1s, we investigated the reproducibility of the stimulation.

Using calcium imaging, we monitored the activities of neurons in the field of view and divided them into two groups: groups within the converter area (Figure 2b) and outside the converter area (Figure 2c). For neurons within the converter area, i.e., 100 μm from the center of the mFOE, Figure 2b shows that

![](images/6281d86616f1dffed6fa826238eecd1271ed24165713011ea5bbcbe1858f2bc3.jpg)

<details>
<summary>text_image</summary>

a
10
9
8
7
5
6
3
2
1
1
2
3
4
5
6
7
8
9
10
</details>

![](images/85d989003f311ff10ddf86a26fd43b70b5ef00b3ba6391e0dc9c29eb66fa5e89.jpg)

<details>
<summary>line chart</summary>

| Channel | Time (s) |
| ------- | -------- |
| 1       | 0        |
| 2       | 0        |
| 3       | 0        |
| 4       | 0        |
| 5       | 0        |
| 6       | 0        |
| 7       | 0        |
| 8       | 0        |
| 9       | 0        |
| 10      | 0        |
</details>

![](images/1ba30342d2712a00303692a95a7b55c522567a040ec2843258d54ac480b2c4ae.jpg)

<details>
<summary>line chart</summary>

| Channel | Value |
| ------- | ----- |
| 1       | 10    |
| 2       | 9     |
| 3       | 8     |
| 4       | 7     |
| 5       | 6     |
| 6       | 5     |
| 7       | 4     |
| 8       | 3     |
| 9       | 2     |
| 10      | 1     |
</details>

![](images/878f435db84a468da2359b4a58603e29998045312c55f20733f9093b0eac7daa.jpg)

<details>
<summary>line chart</summary>

| Time (s) | ΔF/F |
| -------- | ---- |
| 0        | 0.0  |
| 1        | 0.0  |
| 2        | 0.1  |
</details>

![](images/6876fbf149a13109f4e1f234ff611a0b06f39614997eb56731adad604cb95009.jpg)

<details>
<summary>line chart</summary>

| Time (s) | ΔF     |
| -------- | ------ |
| 0        | 0.0    |
| 1        | 0.0    |
| 2        | 0.1    |
| 3        | 0.0    |
</details>

![](images/00320bdcf2c178400d558c93e363b5c4f6c3dfbf9d5dfd3f9f765499a7308f00.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Value |
| -------- | ----- |
| 0        | ~0.01 |
| 1        | ~0.02 |
| 2        | ~0.04 |
| 3        | ~0.01 |
</details>

![](images/aa556ed6cb68544dc694a7b769637d393f532864fffb6a48d8b463ee2b608e65.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Value |
| -------- | ----- |
| 0        | 0.0   |
| 1        | 0.0   |
| 2        | 0.0   |
| 3        | 0.0   |
</details>

![](images/02c9e23b22aec36238a74caed4dd8c8232a0544c57f185e9b1be1b3b95fb4553.jpg)

<details>
<summary>box plot</summary>

| Time     | ΔF/F   |
| -------- | ------ |
| 200 ms   | 0.08   |
| 100 ms   | 0.09   |
| 50 ms    | 0.03   |
| 5 ms     | 0.01   |
</details>

Figure 2. Calcium transients induced by mFOE in cultured primary neurons. a) Calcium image of primary cultured neurons loaded with OGD-1. Twenty neurons within (orange) and outside (blue) the optoacoustic converter area are circled and labeled. Scale bar: 100 μm. Solid line circle: area outside the converter area; dashed line circle: area within the optoacoustic converter area. b,c) Calcium traces of neurons undergone repeated mFOE stimulations with a laser pulse train duration of 100 ms (red dots). Each pulse train was repeated 5 times. Colors and numbers of the traces are corresponding to the neurons labeled in (a). d–g) Average calcium traces of neurons triggered by mFOE stimulation with durations of 200 ms (d), 100 ms (e), 50 ms (f) and 5 ms (g), respectively. Shaded area: the standard deviation (SD). N = 15. h) Average maximum ΔF/F of neurons stimulated by mFOE. N = 15. (n.s.: non-significant, p > 0.05; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001, One-Way ANOVA and Tukey’s mean comparison test).

8 of 10 neurons showed successful and repeatable calcium tran sient $( \Delta \mathrm { F } / \mathrm { F } > 1 \% $ , the baseline standard deviation) corresponding to each stimulation. Calcium transients are also repeatable for each burst applied over the 1 s period, indicating the evoked neuronal activities and confirming the reliability of mFOE stimula tion. For neurons outside the converter area, only 2 of 10 neurons responded. This result also suggested the mFOE with the 150 μm center waveguide with photoacoustic coating provided a spatial precision of approximately200 μm for stimulation in vitro. This observation is consistent with that fiber-based optoacoustic converters generate confined ultrasound fields with sizes comparable with the radius of converter.[38]

Next, to investigate the threshold of mFOE stimulation, we varied the stimulation duration from 5, 50, 100, to 200 ms on neurons in different cultures (N = 15) under the same laser pulse energy of 41.8 ul and the same repetition rate of 1.7 kHz, mFOE stimulation with duration of 5 ms did not evoked any observable fluorescence change (n.s., $\mathsf { p } > 0 . 0 5 )$ (Figure 2g). Only when the duration was 50 ms or longer, the mFOE successfully produced neural activation $( \Delta \mathrm { F } / \mathrm { F } > 1 \% , \mathrm { p } < 0 . 0 1 )$ ) as shown in Figure 2d–f, and Figure 2h. Longer pulse durations lead to larger peak fluorescence changes, from $2 . 9 \pm 1 . 1 \% , 6 . 0 \pm 2 . 8 \%$ to $7 . 8 \pm 1 . 3 \%$ corresponding to 50, 100, and 200 ms, respectively. For the longest stimulation duration of 200 ms tested, no obvious change on morphology or elevation of baseline fluorescence intensity was detected in neurons after multiple stimulations (Figure S7, Supporting Information), indicating the safety of stimulation.

A laser only control experiment was also performed. Laser light with the same pulse energy of 41.8 μJ and duration (200, 100, and 50 ms) was delivered to OGD-1 loaded neurons through the multifunctional fiber but without optoacoustic coating. None of neuron cultures showed a detectable calcium response, distinct from the observed in mFOE-stimulated neurons (Figure S8, Supporting Information).

To evaluate the photothermal effect of the mFOE stimulation and its potential impact on neurons, we also characterized the thermal profile of the mFOE in PBS during the acoustic generation. Temperature was measured by an ultrafast thermal sensor with a sampling rate of 2000 Hz placed in contact with mFOE optoacoustic coating under the microscope. The laser conditions were consistent with neural stimulation test, i.e., the pulse energy was maintained at 41.8 μJ and the burst duration was varied from

a  
![](images/00243e0d55affa53d4b76a8ded36881505caf804d69ca92b7c33293e19ee39ed.jpg)

<details>
<summary>text_image</summary>

Optical
input
Electrical
readout
</details>

c  
![](images/0e6e5464babcde72b9bb128ec72de9228c5e82625cd446c9ae24424396929014.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Voltage (mV) |
| -------- | ------------ |
| 2        | -0.5         |
| 4        | 0.0          |
| 6        | -0.5         |
| 8        | 0.0          |
| 10       | 0.0          |
</details>

d  
![](images/fb6ccb1423a6c8d305df76868d2a4f0cfe363497c263aa21611d1487f14ca98f.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Voltage (mV) |
| -------- | ------------ |
| 2        | 0.3          |
| 4        | 0.3          |
| 6        | 0.3          |
</details>

![](images/c571e8a9e7429e64ddfab7c6d8f1e30da6760b7d8d5c98533cb3539e505bd420.jpg)

<details>
<summary>natural_image</summary>

Black mouse resting on wood shavings in a container (no visible text or symbols)
</details>

e  
![](images/9d60cf1f73b153c70a095798acda5522053ae74744e1b415ebe9ee7a109187fd.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Voltage (mV) |
| -------- | ------------ |
| 2        | 0.0          |
| 4        | 0.0          |
| 6        | 0.0          |
</details>

4  
![](images/79c4ed9631cb5eda2deff81ac16841c596dd6acd60ba48d5a826d2370792d963.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Voltage (mV) |
| -------- | ------------ |
| 2        | 0.3          |
| 4        | 0.3          |
| 6        | 0.3          |
</details>

![](images/a1f34ce96082ca1840501cbede9a820536a4481a41c7015a1f109c34b537ecdf.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Voltage (µV) |
| -------- | ------------ |
| 0        | 20           |
| 1        | 20           |
| 2        | 20           |
| 3        | 20           |
| 4        | 20           |
| 5        | 20           |
| 6        | 20           |
| 7        | 20           |
| 8        | 20           |
| 9        | 20           |
| 10       | 20           |
| 11       | 20           |
| 12       | 20           |
| 13       | 20           |
| 14       | 20           |
| 15       | 20           |
| 16       | 20           |
| 17       | 20           |
| 18       | 20           |
| 19       | 20           |
| 20       | 20           |
| 21       | 20           |
| 22       | 20           |
| 23       | 20           |
| 24       | 20           |
| 25       | 20           |
| 26       | 20           |
| 27       | 20           |
| 28       | 20           |
| 29       | 20           |
| 30       | 20           |
| 31       | 20           |
| 32       | 20           |
| 33       | 20           |
| 34       | 20           |
| 35       | 20           |
| 36       | 20           |
| 37       | 20           |
| 38       | 20           |
| 39       | 20           |
| 40       | 20           |
| 41       | 20           |
| 42       | 20           |
| 43       | 20           |
| 44       | 20           |
| 45       | 20           |
| 46       | 20           |
| 47       | 20           |
| 48       | 20           |
| 49       | 20           |
| 50       | 20           |
| 51       | 20           |
| 52       | 20           |
| 53       | 20           |
| 54       | 20           |
| 55       | 20           |
| 56       | 20           |
| 57       | 20           |
| 58       | 20           |
| 59       | 20           |
| 60       | 20           |
| 61       | 20           |
| 62       | 20           |
| 63       | 20           |
| 64       | 20           |
| 65       | 20           |
| 66       | 20           |
| 67       | 20           |
| 68       | 20           |
| 69       | 20           |
| 70       | 20           |
| 71       | 20           |
| 72       | 20           |
| 73       | 20           |
| 74       | 20           |
| 75       | 20           |
| 76       | 20           |
| 77       | 20           |
| 78       | 20           |
| 79       | 20           |
| 80       | 20           |
| 81       | 20           |
| 82       | 20           |
| 83       | 20           |
| 84       | 20           |
| 85       | 20           |
| 86       | 20           |
| 87       | 20           |
| 88       | 20           |
| 89       | 20           |
| 90       | 20           |
| 91       | 20           |
| 92       | 20           |
| 93       | 20           |
| 94       | 20           |
| 95       | 20           |
| 96       | 20           |
| 97       | 20           |
| 98       | 20           |
| 99       | 20           |
| Note: The actual values may vary due to the random nature of the data generation.
</details>

h  
![](images/db219f7a7230ad1615c1c95fa450d6aeaa0d57a7d8d3804b1632435749ae2d92.jpg)

<details>
<summary>scatterplot</summary>

| PC1 | PC2 |
| --- | --- |
| -100 | 0 |
| 0 | 50 |
| 0 | 0 |
| -100 | -50 |
| 0 | -50 |
| 0 | 0 |
| 0 | 50 |
| 0 | 100 |
| 0 | 100 |
| 0 | 100 |
| 0 | 100 |
| 0 | 100 |
| 0 | 100 |
| 0 | 100 |
| 0 | 100 |
| 0 | 100 |
| 0 | 100 |
</details>

![](images/e9c6bbea7ee6e927473ccf17d4c0dbb058ce7bd698b6b12d59e9514b54daf8e0.jpg)

<details>
<summary>line chart</summary>

| Time (ms) | Voltage (μV) |
| --------- | ------------ |
| 0.0       | 0            |
| 0.5       | 10           |
| 1.0       | -50          |
| 1.5       | 10           |
| 2.0       | 0            |
</details>

![](images/a7606c45fda6bb96ecd613a1f981ef4677353600f13286dd36182b44e1d90117.jpg)

<details>
<summary>line chart</summary>

| Time (ms) | Voltage (μV) |
| --------- | ------------ |
| 0.0       | 0            |
| 0.5       | 0            |
| 1.0       | -40          |
| 1.5       | 0            |
| 2.0       | 0            |
</details>

![](images/4834e4d39e4336d96ba997c6a7c644d67c31d747c90c7656fc70f9fd305b187e.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Amplitude |
| -------- | --------- |
| 0.5      | 0         |
| 3        | 3         |
| 50       | 0         |
</details>

|  
![](images/9d705781604f306d6fd7532baac05e00c7061dc26c6896d6a1ac89aa332af056.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Frequency (Hz) |
| -------- | -------------- |
| 0        | 100            |
| 2        | 50             |
| 4        | 0              |
| 6        | -50            |
| 8        | -100           |
| 10       | -150           |
| 12       | -100           |
| 14       | 0              |
</details>

![](images/d76701ae5fc9fd9c74c707f17c1c8ca0f3190842415a90189f714caa88572bae.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Frequency (Hz) |
| -------- | -------------- |
| 2        | 0              |
| 4        | 0              |
| 6        | 0              |
| 8        | 0              |
| 10       | 0              |
| 12       | 0              |
| 14       | 0              |
</details>

![](images/bd4eda736687f0fd0cef3f37bc236c5a6b1a63a3d7fc1b19248b4e7fa6074913.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Power (dB) |
| -------- | ---------- |
| 2        | 0          |
| 4        | 0          |
| 6        | 0          |
| 8        | 0          |
| 10       | 0          |
| 12       | 0          |
| 14       | 0          |
</details>

Figure 3. Simultaneous optoacoustic stimulation and electrophysiological recording by implanted mFOE in mouse hippocampus. a) Illustration of the mFOE enabled bidirectional neural communication using laser signal as input and electrical signal as readout. b) mFOE was implanted into hippocampus of a wild type $\mathsf C 5 7 \mathsf B \mathsf L / 6 ]$ mouse. c–f) Simultaneous optoacoustic stimulation and electrophysiological recording performed at 3 days (c), 7 days (d), two weeks (e) and one month (f) after implantation. Blue dots, the laser pulse trains. For each laser train: 50 ms burst of pulses, pulse energy of 41.8 μJ, laser repetition rate of 1.7 kHz. g) Part of the filtered spontaneous activity containing two separable group of spikes recorded by mFOE electrode at one month after implantation. h) Principal-components analysis (PCA) of the two group of spikes. i,j) Waveform of two group of spikes in (h). k) Local field potential (LFP) recorded by mFOE one month after implantation with an alternating anesthesia level (0.5–3% v/v isoflurane). l–n) different LFP responses induced by varying the concentration of isoflurane: l corresponds to the initial stage (0.5% of isoflurane level); m corresponds to the burst/suppression transition stage (after increasing the isoflurane level to 3%); n corresponds to the suppression stage (the isoflurane level was maintained at 3% and took effect).

50, 100, to 200 ms. The temperature increase on the mFOE surface was found to be $1 . 2 3 \pm 0 . 0 9 ^ { \circ } \mathrm { C } , 1 . 0 7 \pm 0 . 0 8 ^ { \circ } \mathrm { C } , 0 . 9 6 \pm 0 . 0 8 ^ { \circ } \mathrm { C }$ for 200, 100, 50 ms laser durations, respectively (Figure S9, Sup porting Information). Such temperature increase is far below the previously reported threshold of thermal-induced neural stimulation $( \Delta \dot { \mathrm { T } } > \bar { 5 } ^ { \circ } \mathrm { C } ) . ^ { [ 3 4 , 5 9 ] }$ In addition, a recent study by Kim et al. shows that small temperature increases of $1 ~ ^ { \circ } \mathrm { C }$ caused transient suppression of neurons.[60] This also proves that the temperature effect is not the main contributor to the neuronal response induced by mFOE. Taken together, we conclude that activation of neurons was due to the mFOE optoacoustic stimulation.

## 2.3. In Vivo Simultaneous Optoacoustic Stimulation and Electrophysiological Recording

Since the animal experiment is a significant part of the study in neuroscience and neurological diseases, we further investigated the performance of mFOE in the wild type C57BL/6J mice. In vivo optoacoustic stimulation was performed by delivering pulsed laser to the implanted mFOE, and the optoacoustically stimulated neuronal activities were recorded through electrodes in the mFOE (Figure 3a). Experimentally, we implanted the mFOE into the hippocampus of mice $( \mathrm { N } = 5 )$ . The chronically implanted mFOE allows mice to move freely after surgery (Figure 3b). During stimulation and recording tests, the mFOE was coupled with the laser source and electrophysiological recording headstage through the standard ferrule and pin connector, respectively. The stimulation and recording were conducted in the mice under continuous anesthesia induced and maintained by isoflurane. Based on the threshold of optoacoustic stimulation obtained in in vitro studies. 50 ms bursts of laser pulses with a pulse energy of 41.8 μJ were delivered to the mFOE at 1Hz during the 5 second treatment period. The simultaneous electrophysiological recording by mFOE electrodes was bandpass filtered to examine the local field potential (LFP, 0.5-300 Hz).

Simultaneous optoacoustic stimulation and electrophysiological recording were performed at multiple time points, including 3 days, 7 days, 2 weeks and 1 month (Figure 3c–f). Three out of five mice tested showed successful simultaneous stimulation and recording functions for testing periods of 3 days to one month.

The evoked brain activities corresponding to the optoacoustic stimulation were confirmed by monitoring the LFP response. LFP response at two weeks after implantation was detected with latency of $7 . 1 9 \pm 2 . 2 9$ ms (N = 15, from three mice). The am plitude of LFP response varied at four time points. The largest and smallest responses occurred at 2 weeks and 1 month, respectively. The decreased response observed after 1 month can be attributed to multiple factors. For example, the formation of glial scar around the implanted electrodes can not only block the propagation of electrical signals but also push neurons away from the optoacoustic emitter of mFOE. Both reduce the intensity of the LFP response. Further optimization of the electrode surface coating could improve the reliability of the recording interface.[61,62] These results collectively demonstrate the reliability of the optoacoustic stimulation and recording functions of the implanted mFOE in the animals.

To eliminate the possibility that LFP response was induced by electrical noise or laser artifacts, we also conducted two sham control experiments. In the light only control group, we implanted a multifunctional fiber without optoacoustic coating to the mouse hippocampus and delivered the laser light with the same condition. The LFP recorded didn’t correlate to the laser pulse train, indicating the spontaneous brain activities were recorded and light only did not invoke the LFP response (Figure S10a, Supporting Information). In the dead brain control group, we tested the optoacoustic stimulation through mFOE implanted to the euthanized mouse and did not observe the corresponding LFP response (Figure S10b, Supporting Information). These results collectively confirm the signals we detected from mFOE stimulation were not artifacts.

We further evaluated the recording performance of implanted mFOE. To evaluate the ability of mFOE for recording spike activity, the electrophysiological signals recorded were first bandpass filtered (0.5–3 kHz, Figure 3g). Through a principal-component analysis (PCA) based spike sorting algorithm, two spike clusters can be isolated from an endogenous neural recording (Figure 3h). The cluster quality was assessed by two common measures,[63] $L _ { \mathrm { r a t i o } }$ and isolation distance. $L _ { \mathrm { r a t i o } }$ is 0.0017 and isolation distance has the value of 99.37. Both of them are comparable to the prior reported value of the spike recording with good cluster-separation quality.[27–29] The first averaged spike shape (Figure 3i) showed a narrower and larger depolarization than that of the second spike shape (Figure 3j). The different spike waveform and the cluster analysis suggested that the action potentials were recorded from at least two different groups of neurons.[64,65] Thus, the successfully clustered neural activities from CA3 confirmed the ability of mFOE electrodes for the spike recording.

To examine the sensitivity of LFP recording, at one month after implantation we altered the anesthesia level via adjusting the induced isoflurane concentration during the recording to see if the characteristic anesthesia dosage-dependent changes can be observed (Figure 3k). Initially, a low level of anesthesia was maintained at 0.5% v/v isoflurane, and recorded LFP showed that spontaneous brain activities occurred continuously (i in Figure 3k,l). Then a higher-level anesthesia (3% v/v isoflurane) was applied for 3 min. After the isoflurane level was increased, some spontaneous brain activities were suppressed and a hyperexcitable brain state was induced, where the voltage alternation (bursts) and isoelectric quiescence (suppression) appeared quasiperiodically[29,66] (ii in Figure 3k,m). With maintaining 3% v/v isoflurane, a deep anesthesia state was induced in the animal. At the same time, both respiration rate and responsiveness to toe pinch decreased due to the higher anesthetic level.

Less voltage alternation occurred and for the most of time the LFP signal was a flat line (suppression, iii in Figure 3h,n). Compared with initial stage, ?? band LFP activity in 30–100 Hz was decreased due to the higher concentration of isoflurane as shown in the power spectrum[67] (Figure 3n). Later, when the concentration of isoflurane was reduced to 0.5% v/v again, the LFP activity returned to a similar level as measured in the initial stage. Taken together, this isoflurane dosage-dependent characteristic confirmed the accuracy of LFP recording by mFOE.

## 2.4. Foreign Body Response Comparison between mFOE and Standard Optical Fiber using Immunohistochemistry

Foreign body response is a critical property of implantable neural interface to assure their usage in a safe and chronic way, since the physical insertion into brain tissue commonly initiates a progressive inflammatory tissue response.[61] To evaluate the biocompatibility of mFOE, we compared the foreign body response of mouse brain to mFOE with the similar size standard silica optical fibers (diameter = 300 μm), which is widely used in optogenetic technologies.[68,69] The immunohistochemistry analysis of surrounding brain tissue was performed from mice $( \mathrm { N } = 3 )$ implanted with the mFOE and a conventional silica fiber 3 days and 1 month after implantation (Figure 4a). The damage to surrounding neurons from implant was assessed through evaluating neuronal density using the neuronal nuclei (NeuN) markers (Figure 4b). Number of neurons was calculated by counting the NeuN-positive cells per field of view (650 × 650 μm). The presence of ionized calcium-binding adaptor molecule 1 (Iba1, Figure 4c) and glial fibrillary acidic protein (GFAP, Figure 4d) were used as the markers for activated microglia and astrocytic response, respectively.

Compared with the silica fiber, mFOE induced significantly less microglial response $( p < 0 . 0 1$ , Figure 4c,f) and astrocyte reactivity $( p < 0 . 0 0 1$ , Figure 4d,g), but no significant difference was observed on the neuronal density (Figure 4b,e) 3 days after implantation. A decrease in foreign body response, specifically, higher neuronal density and lower microglia and astrocytic response (Figure 4e–g), was observed from 3 days to 1 month after implantation of both mFOE and silica fiber and no significant difference was observed between mFOE and silica fiber 1 month after implantation. Taken together, the immunohistochemistry analysis confirmed that mFOE yielded less foreign body response in the short period, i.e., 3 days, after implantation and showed similar biocompatibility with silica fiber at longer implantation time, i.e., 1 month.

![](images/ff4ba73b2df786fb86cbf51d150cf9ee13f133ab269564254252138da5c1d061.jpg)  
Figure 4. Foreign body response comparison of mFOE and silica fiber using immunohistochemistry. $\mathsf { a } \mathrm { - } \mathsf { d } )$ Immunohistochemistry images of mouse brains implanted with mFOE and silica fiber one month after implantation $( \mathsf { N } = 3 )$ . Scale bar: 100 μm. Brain slices were labeled with the neuron-specific protein (NeuN, cyan), ionized calcium-binding adaptor molecule 1 (Iba1, red) and glial fibrillary acidic protein (GFAP, green). e) Number of neurons in the field of view, calculated by counting the NeuN-positive cells for mFOE and silica fiber at 3 days and 1 mon after implantation. f) Microglial reactivity, assessed by counting the Iba-1 labeled area, for mFOE and silica fiber at 3 days and 1 mon after implantation. g) Astrocyte reactivity, assessed by counting the GFAP labeled area, for mFOE and silica fiber at 3 days and 1 mon after implantation. For each experimental group, two to four brain slices were used from each mouse $( \mathsf { N } = 3 )$ . (n.s.: non-significant, $p > 0 . 0 5 ; \stackrel { \ast } { \ast } p < 0 . 0 5 ; \stackrel { \ast \ast } { \ast \ast } p < 0 . 0 1 ; \stackrel { \ast \ast \ast } { \ast \ast \ast } p < 0 . 0 0 1$ , One-Way ANOVA and Tukey’s mean comparison test).

## 3. Discussion

In this study, we designed and developed a miniaturized fiber based device, i.e., mFOE, for bidirectional neural communica tion. mFOE performs the “write” function, i.e., optoacoustic stimulation and the “read” function, i.e., simultaneous electrophysiological recording. The broadband acoustic wave generated by mFOE has a pulse width about 0.1 μs, center frequency at 12.5 MHz and peak pressure of 2.3 MPa. >85 such acoustic pulses generated by mFOE successfully stimulate neurons with a spatial resolution of approximately200 μm in primary rat cortical neuron culture. By implanting mFOE into mouse hippocampus, we demonstrated its ability for simultaneous optoacoustic stimulation and electrophysiological recording and superior biocompatibility as a chronic bidirectional neural interface, Reliable stimulation and LFP recording have been achieved up to one month post implantation. Recording quality has been demonstrated by the spike recording.

For the first time, combining this pico-liter deposition and thermal fiber pulling, we successfully integrated an optoacoustic converter to the polymer multifunctional fiber. Different from the conventional dip-coating method,[43,70] the selective deposition through micro-injection allows the easy fabrication of optoa coustic emitter in a volume and position-controlled way. Through the selective deposition, the dimension of optoacoustic emitter is no longer limited by the tip sizes of optical fibers. Our choice of CB/PDMS composite as the optoacoustic material is also essential as it is comparable with this deposition process with a fine volume control at pico liter level. Besides the application in neural interface, such design and fabrication method can also be applied to optical ultrasound probes used in imaging,[44,71] for example, in the tip engineering and the integration to photonics crystal fibers.

We introduced the optoacoustic stimulation as a new strategy for “writing” in the bidirectional neural interface. Compared with previous optoelectrode devices based on optogenetics[26,27,29] and photothermal,[72,73] the optoacoustic stimulation enabled by mFOE reduces the barrier of transgenic techniques for applica tions in primates and potentially human, and avoids the thermal toxicity. At the same time, it offers the spatial precision benefit from the confined ultrasound field. It is orthogonal to electrical recording, therefore minimizing crosstalk with electrical record ing. As an emerging neuromodulation method, the mechanism of optoacoustic stimulation is still not fully understood. In addition to the micropore formation and cavitations,[74,75] more recent studies also indicated that mechanosensitive ion channels are responsible for the activation of neurons.[76,77]

Bidirectional brain interfaces are important research tools to understand brain circuits, potential treatments for neurologi cal disease and bridges to brain computer interface for broad applications. In addition to electrical recording, there are other modalities for recording neural activity in the brain,[78] such as fiber photometry, calcium imaging with a Gradient-Index (GRIN) lens, and microdialysis providing orthogonal ways to record neural activity in the brain. However, due to their disadvantages in temporal resolution and ease of integration, these modalities have not yet replaced electrophysiology recording, the gold standard method “reading” from brain in bidirectional neural interfaces.

New features of mFOE compared to the previous fiberbased interface, such as no viral transfection required and nonelectrical stimulation, are critical to advance many applications. For example, closed-loop neuromodulation has been demonstrated to be superior to the conventional open-loop system, as it can achieve more responsive and real-time control over neural dynamics. In neurological diseases treatment, combining the detection and in situ intervention improves the treatment effectiveness and safety. Because of its bidirectional capabilities, mFOE has the potential to be used as a new brain interface with closedloop capability. Using epilepsy as an example, the implantation of mFOE into seizure foci enables continuous local field potential (LFP) recording. This recording can serve as a guide for localized optoacoustic stimulation, allowing for timely intervention at the early stage before the initial seizure activity progresses into a sever seizure. Such capabilities are also desirable in the application of closed-loop stimulation. For conventional electrical stimulation system, various tools were developed to remove the stimulation artifacts from the recording signal in real time.[79,80] However, they are still limited by the issues on the temporal delay,[81] complex design,[82] and higher hardware resource needed for the computationally intensiveness. The unique orthogonal nonelectrical optoacoustic stimulation and electrical recording avoids electrical artifacts from stimulation appearing in the recording signals, potentially offering a simpler design for the closed-loop strategy.

In comparison of the optoelectrodes fabricated through the semiconductor fabrication process, the recording and stimulation sites of the current mFOE design is fixed at the core waveguide and the number of channels is limited because of the nature of multifunctional fiber. Some post processing methods have been proposed to tackle this challenge, like the laser micromachining technique.[29] It is possible to further engineer the fiber to offer multiple and selective stimulation sites.[83] Additionally, while utilization of soft polymer material[84,85] is effective in reducing the bending stiffness compared to silica fiber, implementation of novel design strategies, such as incorporating a hydrogel matrix,[31] can further enhance flexibility, softness, and biocompatibility, making it more suitable for long-term applications. With further development of the multifunctional fiber strategy, we believe the bandwidth of mFOE would be improved and open more opportunities in the research of neuroscience and neurological diseases.

## 4. Experimental Section

Multifunctional Fiber Fabrication and Optoacoustic Emitter Integration: Multifunctional fibers were fabricated from a preform fiber and then drawn into thin fibers through TDP in a customized furnace. For the preform fiber, PVDF film (0.003" Thick, 8675K21, Mcmaster) and PC film (100 μm thick, LEXAN FR83, laminated plastics) were rolled onto a PC rod (1/2" Diameter, 8 Feet Long, 8571k14, Mcmaster) and followed by a consolidation process in vacuum at 200 °C. Next, four rectangular grooves (2 mm × 2 mm) were machined on the solid PC layer and inserted with the BiSn (RIBBONBO-123407, Indium Corporate) electrodes. Then, another PVDF layer was rolled over the rod to form an insulation layer for the electrodes and followed by an additional PC as the sacrifice layer for the convenience of TDP. The detailed fabrication process was discussed in the previous paper.[29]

A composite of 10% carbon black (diameter < 500 nm, Sigma–Aldrich) and 90% polydimethylsiloxane (PDMS, Sylgard 184, Dow Corning Corporation, USA) were used as the optoacoustic material. The mixture was sonicated for 1 h followed by degassing in vacuum for 30 min. The mixture was then filled in the glass micropipette (Inner diameter = 30 μm, TIP30TW1, World Precision Instruments, USA) and connected to the pico-liter injector (PLI-100A, Warner Instruments, USA). Before the injection of optoacoustic material, the deposition surface of the fiber was polished by optical polishing papers to reduce roughness from 30 to 1 μm. Under the microscope, the glass micropipette was aligned with the core waveguide of multifunctional fiber and the mixture was deposited to the surface of the core waveguide by controlling the injection pressure and time. The deposited fiber was then cured vertically at room temperature for 2 days. Then the cured optoacoustic emitter was inspected under an upright optical microscope to confirm its position and thickness through top view and side view, respectively.

Before use, mFOE was further prepared for the optical coupling and electrodes connection. For the optical coupling, a ceramic ferrule (Thorlabs, USA) was added and affixed to the end of the fiber by the 5-min epoxy (Devcon, ITW Performance Polymers, USA). Then the end surface was polished by optical polishing papers to reduce roughness from 30 to 1 μm. For the connection to electrodes embedded in the multifunctional fiber, the electrodes were exposed manually along the side wall of the fiber by using a blade and silver paint (SPI Supplies, USA). Then copper wires were wrapped around the fiber at each exposure locations along the fiber and the silver paint were applied for the fixation and lower resistance. The copper wires connected to fiber electrodes were soldered to the pin connector while a stainless-steel wire was also soldered as the ground wire for later extracellular recording. In addition, the 5-min epoxy (Devcon, ITW Performance Polymers, USA) was applied to the connection interface for strengthening affixation and better electrical insulation.

Impedance Measurement: First, multifunctional fiber probes were prepared into two centimeters long and the embedded electrodes were electrically connected to the copper wire (connecting details in the above fabrication and integration section). The impedance Spectrum results were acquired via a potentiostat (Interface 1010E, Gamry Instruments). During the measurements, two-electrode experiments were performed with fiber probes as a working electrode, Pt wire (Basi) as 1 × phosphate-buffered saline (PBS, Thermo Fisher) as electrolyte by an AC voltage of 10 mV (10 Hz–100 kHz).

Optoacoustic Wave Characterization: To generate the optoacoustic signal, a compact Q-switched diode-pumped solid-state laser (1030 nm, 3 ns. 100 ul, repetition rate of 1.7 kHz. RPMC Lasers Inc., USA) was used as the excitation laser source. The laser was first connected to an optical fiber through a 200 μm fiber coupling module and then connected to the mFOE with a SubMiniature version A (SMA) connector. The pulse energy was adjusted through a fiber optic attenuator (varied gap SMA Connector, Thorlabs, Inc., USA). The acoustic signal was measured through a homebuilt system including a needle hydrophone (ID. 40 μm; OD, 300 μm) with a frequency range of 1–30 MHz (NH0040, Precision Acoustics Inc., Dorchester, UK), an amplifier and an oscilloscope. The mFOE tip and hydrophone tip were both immersed in degassed water. The pressure values were calculated based on the calibration factor provided by the hydrophone manufacturer. The frequency data was obtained through a fast Fourier transform (FFT) calculation using the OriginPro 2019.

Embryonic Neuron Culture: All experimental procedures complied with all relevant guidelines and ethical regulations for animal testing and research established and approved by Institutional Animal Care and Use Committee (IACUC) of Boston University (PROTO201800534). Primary cortical neurons were isolated from embryonic day 15 (E15) Sprague−Dawley rat embryos of either sex (Charles River Laboratories, MA, USA). Cortices were isolated and digested in TrypLE Express (ThermoFisher Scientific, USA). Then the neurons were plated on poly-D-lysine (50 μg mL−1, ThermoFisher Scientific, USA)-coated glass bottom dish (P35G-1.5-14-C, MatTek Corporation, USA). Neurons were first cultured with a seeding medium composed of 90% Dulbecco’s modified Eagle medium (ThermoFisher Scientific, USA) and 10% fetal bovine serum (ThermoFisher Scientific, USA) and 1% GlutaMAX (ThermoFisher Scientific, USA), which was then replaced 24 h later by a growth medium composed of Neurobasal Media (ThermoFisher Scientific, USA) supplemented with 1 × B27 (ThermoFisher Scientific, USA), 1 × N2 (ThermoFisher Scientific, USA), and 1 × GlutaMAX (ThermoFisher Scientific, USA). Half of the medium was replaced with fresh growth medium every 3 or 4 days. Cells cultured in vitro for 10−14 days were used for Oregon Green labeling and PA stimulation experiments.

In Vitro Neurostimulation and Calcium Imaging: Oregon Green 488 BAPTA-1 dextran (OGD-1) (ThermoFisher Scientific, USA) was dissolved in 20% Pluronic F-127 in dimethyl sulfoxide (DMSO) at a concentration of 1 mm as stock solution. Before imaging, neurons were incubated with 2 μm OGD-1 for 30 min, followed by incubation with normal medium for 30 min. Q-switched 1030 nm nanosecond laser was used to generate light and delivered to mFOE. The pulse energy was adjusted through a fiber optic attenuator (varied gap SMA Connector, Thorlabs, Inc., USA). Notably, 1030 nm is far from the excitation peak of Oregon Green (494 nm) and pass band of emission filter (500–540 nm), therefore assuring no effect from direct excitation of OGD by any light leak from the fiber. A 3D translational stage was used to position the mFOE approaching the target neurons.

Calcium fluorescence imaging was performed on a lab-built wide-field fluorescence microscope based on an Olympus IX71 microscope frame with a 20 × air objective (UPLSAPO20X, 0.75NA, Olympus, USA), illuminated by a 470 nm LED (M470L2, Thorlabs, USA), an emission filter (FBH520-40, Thorlabs, USA), an excitation filter (MF469-35, Thorlabs) and a dichroic mirror (DMLP505R, Thorlabs, USA). The converter area is visible and identifiable through the inverted microscope when the mFOE was placed close enough to the imaging plate. Image sequences were acquired with a scientific CMOS camera (Zyla 5.5, Andor, Oxfords Instruments, UK) at 20 frames per second. The fluorescence intensities, data analysis, and exponential curve fitting were analyzed using ImageJ (Fiji) and MATLAB 2022.

Implantation Surgery Procedure: All surgery procedures complied with all relevant guidelines and ethical regulations for animal testing and research established and approved by Institutional Animal Care and Use Committee (IACUC) of Boston University (PROTO201800534). Eight to ten weeks old male wildtype C57BL/6-E mice (Charles River Laboratories, US) were received and allowed to acclimate for at least 3 days before enrolling them in experiments. All mice in experiments had access to food and water ad libitum and were kept in the BU animal facility maintained for 12-h light/dark cycle. During the implantation surgery, mice were anesthetized by isoflurane (5% for induction, 1–3.5% during the procedure) and positioned on a stereotaxic apparatus (51500D, Stoelting Co., USA). After hair removal, a small incision was made by sterile surgery scalpel at the target region and then a small craniotomy was made by using a dental drill. Assembled mFOE was inserted into mouse hippocampus (−2.0 mm AP, 1.5 mm ML, 2 mm DV) using a manipulator with respect to the Mouse Brain Atlas. The ground stainless steel wire was soldered to a miniaturized screw (J.I. Morris) on the skull. Finally, the whole exposed skull area was fully covered by a layer of Metabond (C&B METABOND, Parkell, USA) and dental cement (51458, Stoelting Co., USA). Buprenorphine SR was used to provide long effective analgesia after the surgery.

In Vivo Electrophysiology Recording and Optoacoustic Stimulation: Extracellular recording was performed through an electrophysiology system (Molecular Devices, LLC, USA). mFOE electrodes were connected to the amplifier (Multiclamp 700B, Molecular Devices, LLC, USA) through the pin connector and headstages after the animals recovered from surgeries. The amplified analog signal was then converted and recorded by the digitizer (Digidata 1550, Molecular Devices, LLC, USA).

Q-switched 1030 nm nanosecond laser was used to generate light and delivered to mFOE. During the extracellular electrophysiological recording, the preset trigger signal was generated by the digitizer and used to trigger the Q-switch laser for optoacoustic stimulation. The pulse energy was adjusted through a fiber optic attenuator (varied gap SMA Connector, Thorlabs, Inc., USA).

Data analysis was performed with Matlab and OriginPro and custom scripts were used to analyze the local field potential and spike sorting. The raw extracellular recordings were first band filtered for local field potential results (LFP, 0.5–300 Hz) and spike results (300–5000 Hz). A custom Matlab script was used to create spectrograms to visually support the analysis of the LFPs in both the time domain and the frequency domain. The spike sorting algorithm was implemented through several steps: first, individual spike signals with length of 3 ms were picked up from the full recording through a standard amplitude threshold method. The threshold amplitude was set as −15 μV. Then the dimensionality of each spike signal was reduced via the principal component analysis (PCA) and unsupervised learning algorithms (K-means clustering) was used to separate out the clusters.

Foreign Body Response Assessment via Immunohistochemistry: To compare the tissue response, animals were implanted with a silica optical fiber (diameter = 300 μm, FT300EMT, Thorlabs, Inc, USA) and mFOE for 3 days or 4 weeks. Then at target timepoints, animals were euthanized and transcardially perfused with phosphate-buffered saline (PBS, ThermoFisher Scientific, USA) followed by 4% paraformaldehyde (PFA, ThermoFisher Scientific, USA) in PBS. The fiber probes were carefully extracted before the extraction and then the brains were kept in 4% PFA solution for one day at 4 °C. Brains were sectioned in the horizontal plane at 75 μm on an oscillating tissue slicer (OST-4500, Electron Microscopy Sciences). Free-floating brain slices were washed in PBS and blocked for 1 h at room temperature in a blocking solution consisting of 0.3% Triton X-100 (vol/vol) and 2.5% goat serum (vol/vol) in PBS. After blocking, brain slices were incubated with the primary antibodies in the PBS solution with 2.5% goat serum (vol/vol) for 24 h at 4 °C. Primary antibodies used included rat anti-GFAP (Abcam Cat. # ab279291, 1:500), chicken anti-NeuN (Millipore Cat. # ABN91, 1:500), and rabbit anti-Iba1 (Abcam Cat. # ab178846, 1:500). Following primary incubation, slices were washed three times with PBS for 10 min at room temperature. The brain slices were then incubated with secondary antibodies in the PBS solution with 2.5% goat serum (vol/vol) for 2 h at room temperature. Secondary antibodies used included goat anti-rat Alexa Fluor 488 (Abcam Cat. # ab150157, 1:1000), goat anti-rabbit Alexa Fluor 568 (Abcam Cat. # ab175471, 1:1000) and goat anti-chicken Alexa Fluor 647 (Abcam Cat. # ab15017], 1:1000). Slices were then washed three times with PBS for 10 min at room temperature. Before imaging, slices were stained with DAPI solution (1 μg/ml, Millipore, USA) for 15 min at room temperature. Perfusion, staining and mounting procedures were identical to all samples regardless of the implants.

All brain slices were prepared by using an oscillating tissue slicer (OST-4500, Electron Microscopy Sciences) with the same thickness of 75 μm controlled by the machine. Before imaging, stained brain slices were gently transferred on the cover glass by a brush without any folding. Perfusion, staining and mounting procedures were identical to all samples regardless of the implants.

All fluorescent images were acquired with a laser scanning confocal microscope (Olympus FV3000) with an air 20 × objective and a numerical aperture NA = 0.75 unless otherwise noted. Regions centered on the wound induced by implants, i.e., mFOE or silica fibers, with the dimension of 650 μm × 650 μm were selected for later quantitative analysis (Figure 4). Neuron density was then calculated within the selected areas by counting NeuN-labeled cell bodies using the cell counter plugin (ImageJ). Sample with obvious uneven neuron distribution (Figure S11, Supporting Information) was excluded for comparison. Area analysis of Iba1 and GFAP labeled cells was performed by creating binary layers of the fluorescence images using the threshold function and quantified using the measurement tool (ImageJ Fiji). The IsoData algorithm[86] in ImageJ Fiji was used to unbiasedly determine the threshold value to distinguish the signal area from the background.

Statistical Information: Data shown are mean ± standard deviation. For the comparison on peak fluorescence change of in vitro optoacoustic stimulation, one-way ANOVA and Tukey’s mean comparison test were conducted by using OriginLab. 15 stimulation events were compared for each condition. For the comparison of foreign body response between silica fiber and mFOE, N > 8 brain slices from 3 animals were analyzed using one-way ANOVA and Tukey’s mean comparison test. The p values were determined as n.s.: nonsignificant, $p > 0 . 0 5 ; \ast p <$ $0 . 0 5 ; \mathrm { ~ } \vec { \cdots } p < 0 . 0 1 ; \mathrm { ~ } \vec { \cdots } \vec { \times } \vec { \times } p < 0 . 0 0 1$ . Statistic analysis were conducted using OriginPro.

## Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements

J-X.C. and C.Y. acknowledge funding support from US National Institute of Health Brain Initiative R01 NS109794. X.J. gratefully acknowledges funding support from US National Science Foundation (ECCS-1847436) and US National Institutes of Health (R01 NS123069 and R21 EY033080- 01). C.Y. acknowledge the support from the Boston University Micro and Nano Imaging Facility and the Office of the Director, National Institutes of Health under the award number S10OD024993.

## Conflict of Interest

The authors declare no conflict of interest.

## Author Contributions

C.Y. conceived the project. N.Z. and S.J. performed fabrication and characterization of materials, N.Z, and Y.I. performed the stimulation and record ing experiments in vitro and in vivo. N.Z. and Y.L. performed the in vivo biocompatibility evaluations. G.C. and N.Z. performed photoacoustic characterization. X.J. provided guidance on the multifunctional fiber system. J.-X.C. provided guidance on the design of fiber optoacoustic emitter. J.K. provided guidance on optimization of recording and data analysis. The manuscript was written through contributions of all authors. All authors have given approval to the final version of the manuscript.

## Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Keywords

bidirectional neural interfaces, multifunctional fibers, neuromodulation, optoacoustic

Received: February 9, 2023

Revised: July 11, 2023

Published online: July 31, 2023

[1] L. Wilbrecht, Front Hum Neurosci 2010, 3, 81.  
[2] R. Chen, A. Canales. P. Anikeeva, Nat. Rev. Mater. 2017, 2. 16093.  
[3] V. S. Sohal, F. Zhang, O. Yizhar, K. Deisseroth, Nature 2009, 459, 698.  
[4] A. C. Paulk, L. Kirszenblat, Y. Zhou, B. Van Swinderen, J. Neurosci. 2015, 35, 10304.  
[5] B. Rosin, M. Slovik, R. Mitelman, M. Rivlin-Etzion, S. N. Haber, Z. Israel, E. Vaadia, H. Bergman, Neuron 2011, 72, 370.  
[6] J. T. Paz, T. J. Davidson, E. S. Frechette, B. Delord, I. Parada, K. Peng, K. Deisseroth, J. R. Huguenard, Nat. Neurosci. 2013, 16, 64.  
[7] I. E. Harmsen, G. J. B. Elias, M. E. Beyn, A. Boutet, A. Pancholi, J. Germann, A. Mansouri, C. S. Lozano, A. M. Lozano, Brain Stimul. 2020, 13, 378.  
[8] C. Hughes, A. Herrera, R. Gaunt, J. Collinger, Handb Clin Neurol 2020, 168, 163.  
[9] A. Zhou, B. C. Johnson, R. Muller, Curr. Opin. Neurobiol. 2018, 50, 119.  
[10] C. N. Heck, D. King-Stephens, A. D. Massey, D. R. Nair, B. C. Jobst, G. L. Barkley, V. Salanova, A. J. Cole, M. C. Smith, R. P. Gwinn, C. Skidmore, P. C. Van Ness, G. K. Bergey, Y. D. Park, I. Miller, E. Geller, P. A. Rutecki, R. Zimmerman, D. C. Spencer, A. Goldman, J. C. Edwards, J. W. Leiphart, R. E. Wharen, J. Fessler, N. B. Fountain, G. A. Worrell, R. E. Gross, S. Eisenschenk, R. B. Duckrow, L. J. Hirsch, et al., Epilepsia 2014, 55, 432.  
[11] F. T. Sun, M. J. Morrell, Expert Rev. Med. Devices 2014, 11, 563.  
[12] S. Miocinovic, S. F. Lempka, G. S. Russo, C. B. Maks, C. R. Butson, K. E. Sakaie, J. L. Vitek, C. C. Mcintyre, Exp Neurol 2009, 216, 166.  
[13] M. Paff, A. Loh, C. Sarica, A. M. Lozano, A. Fasano, J Mov Disord 2020, 13, 185.  
[14] J. Buhlmann, L. Hofmann, P. A. Tass, C. Hauptmann, Front. Neuroeng. 2011, 4, 15.  
[15] X. Qian, Y. Chen, Y. Feng, B. Ma, H. Hao, L. Li, IEEE Trans. Neural Syst. Rehabil. Eng. 2017, 25, 2217.  
[16] L. Koessler, S. Colnat-Coulbois, T. Cecchin, J. Hofmanis, J. P. Dmochowski, A. M. Norcia, L. G. Maillard, Hum Brain Mapp 2017, 38, 974.  
[17] K. Deisseroth, Nat. Methods 2011, 8, 26.  
[18] J. A. Cardin, M. Carlén, K. Meletis, U. Knoblich, F. Zhang, K. Deisseroth, L.i-H. Tsai, C. I. Moore, Nat. Protoc. 2010, 5, 247.  
[19] J. Zhang, F. Laiwalla, J. A. Kim, H. Urabe, R. Van Wagenen, Y.-K. Song, B. W. Connors, F. Zhang, K. Deisseroth, A. V. Nurmikko, J. Neural Eng. 2009, 6, 055007.  
[20] T. V. F. Abaya, S. Blair, P. Tathireddy, L. Rieth, F. Solzbacher, Biomed. Opt. Express 2012, 3, 3087.  
[21] J. Wang, F. Wagner, D. A. Borton, J. Zhang, I. Ozden, R. D. Burwell, A. V. Nurmikko, R. Van Wagenen, I. Diester, K. Deisseroth, J. Neural Eng. 2012, 9, 016001.  
[22] S. Royer, B. V. Zemelman, M. Barbic, A. Losonczy, G. Buzsáki, J. C. Magee, Eur J Neurosci 2010, 31, 2279.  
[23] H. Zhang, W. Pei, X. Yang, X. Guo, X. Xing, R. Liu, Y. Liu, Q. Gui, H. Chen presented at Annual Int. Conf. of IEEE Engineering in Medicine and Biology Society, Orlando, FL, USA, August 2016.  
[24] A. V. Kravitz, S. F. Owen, A. C. Kreitzer, Brain Res. 2013, 1511, 21.  
[25] F. Wu, E. Stark, P.-C. Ku, K. D. Wise, G. Buzsáki, E. Yoon, Neuron 2015, 88, 1136.  
[26] M. Vöröslakos, K. Kim, N. Slager, E. Ko, S. Oh, S. S. Parizi, B. Hendrix, J. P. Seymour, K. D. Wise, G. Buzsáki, A. Fernández-Ruiz, E. Yoon, Adv. Sci. 2022, 9, 2105414.  
[27] A. Canales, X. Jia, U. P. Froriep, R. A. Koppes, C. M. Tringides, J. Selvidge, C. Lu, C. Hou, L. Wei, Y. Fink, P. Anikeeva, Nat. Biotechnol. 2015  
[28] S. Park, Y. Guo, X. Jia, H. K. Choe, B. Grena, J. Kang, J. Park, C. Lu, A. Canales, R. Chen, Y. S. Yim, G. B. Choi, Y. Fink, P. Anikeeva, Nat. Neurosci. 2017, 20, 612.  
[29] S. Jiang, D. C. Patel, J. Kim, S. Yang, W. A. Mills, Y. Zhang, K. Wang, Z. Feng, S. Vijayan, W. Cai, A. Wang, Y. Guo, I. F. Kimbrough, H. Sontheimer, X. Jia, Nat. Commun. 2020, 11, 6115.  
[30] M.-J. Antonini, A. Sahasrabudhe, A. Tabet, M. Schwalm, D. Rosenfeld, I. Garwood, J. Park, G. Loke, T. Khudiyev, M. Kanik, N. Corbin, A. Canales, A. Jasanoff, Y. Fink, P. Anikeeva, Adv. Funct. Mater. 2021, 2104857, 31.  
[31] S. Park, H. Yuk, R. Zhao, Y. S. Yim, E. W. Woldeghebriel, J. Kang, A. Canales, Y. Fink, G. B. Choi, X. Zhao, P. Anikeeva, Nat. Commun. 2021, 12, 3435.  
[32] A. Bansal, S. Shikha, Y. Zhang, Nat. Biomed. Eng. 2022, 7, 349.  
[33] Y. An, Y. Nam, J. Neural Eng. 2021, 18, 066002.  
[34] Y. Lyu, C. Xie, S. A. Chechetka, E. Miyako, K. Pu, J. Am. Chem. Soc. 2016, 138, 9049.  
[35] M. Meneghetti, J. Kaur, K. Sui, J. F. Sørensen, R. W. Berg, C. Markos, Light Sci Appl 2023, 12, 127.  
[36] J. M. Cayce, R. M. Friedman, G. Chen, E. D. Jansen, A. Mahadevan-Jansen, A. W. Roe, NeuroImage 2014, 84, 181.  
[37] A. Jonsson, S. Inal, I. Uguz, A. J. Williamson, L. Kergoat, J. Rivnay, D. Khodagholy, M. Berggren, C. Bernard, G. G. Malliaras, D. T. Simon, Proc. Natl. Acad. Sci. USA 2016, 113, 9440.  
[38] Y. Jiang, F. Wang, Q. Wei, H. Li, Y. Shang, W. Zhou, C. Wang, P. Cheng, Q. Chen, L. Chen, Z. Ning, Nat. Commun. 2020, 11, 1245.  
[39] L. Shi, Y. Jiang, F. R. Fernandez, G. Chen, L.u Lan, H.-Y.e Man, J. A. White, J.i-X. Cheng, C. Yang, Light Sci Appl 2021, 10, 143.  
[40] L. V. Wang, S. Hu, Science 2012, 335, 1458  
[41] T. Lee, H. W. Baac, Q. Li, L. J. Guo, Adv. Opt. Mater. 1800491, 2018, 6.  
[42] A. F. Abouraddy, M. Bayindir, G. Benoit, S. D. Hart, K. Kuriki, N. Orf, O. Shapira, F. Sorin, B. Temelkuran, Y. Fink, Nat. Mater. 2007, 6, 336.  
[43] R. J. Colchester, C. A. Mosse, D. S. Bhachu, J. C. Bear, C. J. Carmalt, I. P. Parkin, B. E. Treeby, I. Papakonstantinou, A. E. Desjardins, Appl. Phys. Lett. 2014, 104.  
[44] S. Noimark, R. J. Colchester, B. J. Blackburn, E. Z. Zhang, E. J. Alles, S. Ourselin, P. C. Beard, I. Papakonstantinou, I. P. Parkin, A. E. Desjardins, Adv. Funct. Mater. 2016, 26, 8390.  
[45] G. Chen, L. Shi, L.u Lan, R. Wang, Y. Li, Z. Du, M. Hyman, J.i-X. Cheng, C. Yang, Front Neurosci 2022, 16, 1005810.  
[46] L. Yi, C. Jin, L. Wang, J. Liu, Biomaterials 2014, 35, 9789.  
[47] Y. He, Y.u Zhao, L. Fan, X. Wang, M. Duan, H. Wang, X. Zhu, J. Liu, Adv. Sci. 2021, 8, 2100719.  
[48] S. Chen, R. Zhao, X. Sun, H. Wang, L. Li, J. Liu, Adv. Healthcare Mater. 2023, 12, 2201924.  
[49] Y. Guo, C. F. Werner, A. Canales, L.i Yu, X. Jia, P. Anikeeva, T. Yoshinobu, PLoS One 2020, 15, 0228076.  
[50] D. Han, Z. Meng, D. Wu, C. Zhang, H. Zhu, Nanoscale Res. Lett. 2011, 6, 457.  
[51] K. Hilarius, D. Lellinger, I. Alig, T. Villmow, S. Pegel, P. Pötschke, Poly mer 2013, 54, 5865.  
[52] P. J. Brigandi, J. M. Cogen, J. R. Reffner, C. A. Wolf, R. A. Pearson, Polym. Eng. Sci. 2017, 57, 1329.  
[53] P. N. T. Wells, Ultrasound Med Biol 1975, 1, 369.  
[54] Z. Zhao, R. Gong, H. Huang, J. Wang, Sensors 2016, 16, 880.  
[55] T. Sen, O. Tufekcioglu, Y. Koza, Anatol J Cardiol 2015, 15, 334.  
[56] D. Smetters, A. Majewska, R. Yuste, Methods 1999, 18, 215.  
[57] W. Yang, R. Yuste, Nat. Methods 2017. 14. 349  
[58] S. Nagayama, S. Zeng, W. Xiong, M. L. Fletcher, A. V. Masurkar, D. J. Davis, V. A. Pieribone, W. R. Chen, Neuron 2007, 53, 789.  
[59] M. G. Shapiro, K. Homma, S. Villarreal, C.-P. Richter, F. Bezanilla, Nat. Commun. 2012, 3, 736.  
[60] T. Kim, H. Kadji, A. J. Whalen, A. Ashourvan, E. Freeman, S. I. Fried, S. Tadigadapa, S. J. Schiff, J. Neural Eng. 2022, 19, 056029.  
[61] T. D. Y. Kozai, A. S. Jaquins-Gerstl, A. L. Vazquez, A. C. Michael, X. T. Cui. ACS Chem. Neurosci, 2015. 6. 48  
[62] J. R. Eles, A. L. Vazquez, N. R. Snyder, C. Lagenaur, M. C. Murphy, T. D. Y. Kozai, X. T. Cui, Biomaterials 2017, 113, 279.  
[63] N. Schmitzer-Torbert, J. Jackson, D. Henze, K. Harris, A. D. Redish, Neuroscience 2005, 131, 1.  
[64] M. M. Heinricher, Microelectrode Recording in Movement Disorder Surgery, Thieme, Teningen, Germany, 2004, 8.  
[65] D. A. Henze, Z. Borhegyi, J. Csicsvari, A. Mamiya, K. D. Harris, G. Buzsáki, J Neurophysiol 2000, 84, 390.  
[66] S. Ching, P. L. Purdon, S. Vijayan, N. J. Kopell, E. N. Brown, Proc. Natl. Acad. Sci. USA 2012. 109, 3095.  
[67] A. G. Hudetz, J. A. Vizuete, S. Pillay, Anesthesiology 2011, 114, 588.  
[68] A. M. Aravanis, L.i-P. Wang, F. Zhang, L. A. Meltzer, M. Z. Mogri, M. B. Schneider, K. Deisseroth, J. Neural Eng. 2007, 4, S143.  
[69] K. Ung, B. R. Arenkiel, J. Vis. Exp. 2012, 29, 50004.  
[70] R. K. Poduval, S. Noimark, R. J. Colchester, T. J. Macdonald, I. P. Parkin, A. E. Desjardins, I. Papakonstantinou, Appl. Phys. Lett. 2017, 110, 223701.  
[71] M. C. Finlay, C. A. Mosse, R. J. Colchester, S. Noimark, E. Z. Zhang, S. Ourselin, P. C. Beard, R. J. Schilling, I. P. Parkin, I. Papakonstantinou, A. E. Desjardins, Light Sci Appl 2017, 6, 17103.  
[72] M. Yoo, H.o Koo, M. Kim, H.-I. Kim, S. Kim, J. Biomed. Opt. 2013, 18, 128005.  
[73] T. V. F. Abaya, M. Diwekar, S. Blair, P. Tathireddy, L. Rieth, G. A. Clark, F. Solzbacher, Biomed. Opt. Express 2012, 3, 2200.  
[74] M. Plaksin, S. Shoham, E. Kimmel, Phys. Rev. X 2014, 4, 011044.  
[75] B. Krasovitski, V. Frenkel, S. Shoham, E. Kimmel, Proc. Natl. Acad. Sci. USA 2011, 108, 3258.  
[76] S. Yoo, D. R. Mittelstein, R. C. Hurt, J. Lacroix, M. G. Shapiro, Nat. Commun, 2022, 13, 493.  
[77] L. Shi, Y. Jiang, N. Zheng, J.i-X. Cheng, C. Yang, Neurophotonics 2022, 9, 032207.  
[78] A. Vázquez-Guardado, Y. Yang, A. J. Bandodkar, J. A. Rogers, Nat. Neurosci, 2020, 23, 1522.  
[79] Y. Nie, X. Guo, X. Li, X. Geng, Y. Li, Z. Quan, G. Zhu, Z. Yin, J. Zhang, S. Wang, J. Neural Eng. 2021, 18, 066031.  
[80] E. M. Dastin-van Rijn, et al., Cell Rep Methods 2021, 1, 100010.  
[81] A. M. Oyama, C. Itiki, Annu Int Conf IEEE Eng Med Biol Soc 2010, 2010, 6091.  
[82] S. Stanslaski, P. Afshar, P. Cong, J. Giftakis, P. Stypulkowski, D. Carlson, D. Linde, D. Ullestad, A.l-T. Avestruz, T. Denison, IEEE Trans. Neural Syst. Rehabil. Eng. 2012, 20, 410.  
[83] F. Pisanello, L. Sileo, I. A. Oldenburg, M. Pisanello, L. Martiradonna, J. A. Assad, B. L. Sabatini, M. De Vittorio, Neuron 2014, 82, 1245.  
[84] K. Sui, M. Meneghetti, J. Kaur, R. J. F. Sørensen, R. W. Berg, C. Markos, J. Neural Eng. 2022, 19, 016035.  
[85] S. I.l Park, D. S. Brenner, G. Shin, C. D. Morgan, B. A. Copits, H.a U.k Chung, M. Y. Pullen, K. N. Noh, S. Davidson, S. J.u Oh, J. Yoon, K.- I.n Jang, V. K. Samineni, M. Norman, J. G. Grajales-Reyes, S. K. Vogt, S. S. Sundaram, K. M. Wilson, J. S. Ha, R. Xu, T. Pan, T.-I.l Kim, Y. Huang, M. C. Montana, J. P. Golden, M. R. Bruchas, R. W. Gereau, J. A. Rogers, Nat. Biotechnol. 2015, 33, 1280.  
[86] T. W. Ridler, S. Calvard, IEEE Trans Syst Man Cybern 1978, 8, 630.