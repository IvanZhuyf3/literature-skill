![](images/77d7599eb24ddf2a9f49fe8db08c5a9ea851f17ac82c89abf43e7f7555d96321.jpg)

Check for updates

## OPEN ACCESS

EDITED BY

Zhihai Qiu,

Guangdong Institute of Intelligence

Science and Technology, China

REVIEWED BY

Zhongtao Hu,

Washington University in St. Louis,

United States

Rui Min,

Beijing Normal University, China

Zongyue Cheng,

Purdue University, United States

\*CORRESPONDENCE

Ji-Xin Cheng

jxcheng@bu.edu

Chen Yang

cheyang@bu.edu

†These authors have contributed equally to this work and share first authorship

SPECIALTY SECTION

This article was submitted to

Neural Technology,

a section of the journal

Frontiers in Neuroscience

28 July 2022

10 October 2022

PUBLISHED 03 November 2022

Chen G, Shi L, Lan L, Wang R, Li Y,

Du Z, Hyman M, Cheng J-X and

Yang C (2022) High-precision neural

stimulation by a highly efficient

candle soot fiber optoacoustic

emitter

Front. Neurosci. 16:1005810.

doi: 10.3389/fnins.2022.1005810

© 2022 Chen, Shi, Lan, Wang, Li, Du, Hyman, Cheng and Yang. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

# High-precision neural stimulation by a highly efficient candle soot fiber optoacoustic emitter

Guo Chen1,2†, Linli Shi2,3†, Lu Lan1, Runyu Wang1, Yueming Li2,4, Zhiyi Du2,3, Mackenzie Hyman2,5, Ji-Xin Cheng1,5\* and Chen Yang1,3\*

1Department of Electrical and Computer Engineering, Boston University, Boston, MA, United States, 2Photonics Center, Boston University, Boston, MA, United States, 3Department of Chemistry, Boston University, Boston, MA, United States, 4Department of Mechanical Engineering, Boston University, Boston, MA, United States, 5Department of Biomedical Engineering, Boston University, Boston, MA, United States

Highly precise neuromodulation with a high efficacy poses great importance in neuroscience. Here we developed a candle soot fiber optoacoustic emitter (CSFOE), capable of generating a high pressure of over 10 MPa with a central frequency of 12.8 MHz, enabling highly efficient neuromodulation in vitro. The design of the fiber optoacoustic emitter, including the choice of the material and the thickness of the layered structure, was optimized in both simulations and experiments. The optoacoustic conversion efficiency of the optimized CSFOE was found to be 10 times higher than the other carbonbased fiber optoacoustic emitters. Driven by a single laser, the CSFOE can perform dual-site optoacoustic activation of neurons, confirmed by calcium (Ca2+) imaging. Our work opens potential avenues for more complex and programmed control in neural circuits using a simple design for multisite neuromodulation in vivo.

KEYWORDS

neural modulation, neural stimulation, optoacoustic stimulation, optoacoustic, photoacoustic, fiber, optoacoustic conversion efficiency

## Introduction

Highly precise neural modulation is of great importance in neuroscience, as firing of specific neuronal populations in the brain could alter the behavior of animals and serve as a novel tool for studying neural pathways in disease and health. Sophisticated control of neuronal circuits and brain functions requires stimulating multiple functional regions at high spatial resolution. For example, a previous study by Li et al. (2019) used two ultrasound transducers to stimulate primary somatosensory cortex barrel field (S1BF) of a free moving mouse and successfully controlled the head turning direction of the mouse by applying stimuli at different positions. Among the current neuromodulation platforms, electrical neural stimulation has been proven to be efficient and allows for deep brain stimulation, while it provides a limited spatial resolution of millimeters in vivo, due to electric current spread (Boon et al., 2007). Optogenetics neural stimulation with single neuron resolution has been shown as a powerful tool in fundamental studies, but the requirement of viral infection makes it challenging to apply to human brains (Boyden et al., 2005). Transcranial magnetic stimulation (TMS) and transcranial direct current stimulation (tDCS) are capable of non-invasive transcranial neuromodulation, while suffering from the resolution at the centimeter level (Rosa and Lisanby, 2012; Davidson et al., 2020). Infrared neuron stimulation (INS) takes advantage of the near-infrared absorption of water to generate heat for neural stimulation. However, the thermal toxicity and potential tissue damage is a concern in real clinical scenarios (Cayce et al., 2014; Zhu et al., 2022). Low frequency focused ultrasound is an emerging non-invasive modality with centimeter-scale penetration depth in tissue (Beisteiner et al., 2020; Bobola et al., 2020; Brinker et al., 2020). It has a spatial resolution limited by the diffraction of acoustic wave, therefore it is challenging for low-frequency (< 1 MHz) ultrasound to reach submillimeter spatial resolution. New technologies and methods are still being sought for precise and non-genetic neural stimulation.

Recently, our team developed a miniaturized fiberoptoacoustic converter (FOC) converting pulsed laser into ultrasound (Jiang et al., 2020). FOC succeeded in spatially confined neural stimulation of mouse brain and modulation of motor activities in vivo. It was found that, for successful FOC based optoacoustic neural stimulation, a pressure of around 0.5 MPa is needed (Jiang et al., 2020). Typical FOC generate a pressure of 0.48 MPa upon laser pulse energy of 14.5 µJ, with an estimated photoacoustic conversion efficiency of 1,374 Pa m2/J. Considering the typical energy and repetition rate of nanosecond lasers, the low conversion efficiency of FOC limits its application in multi-site stimulation. Thus, new fiber optoacoustic emitters with a higher conversion efficiency are needed to enable multisite optoacoustic neuromodulation.

According to a simplified model of optoacoustic generation, the output optoacoustic pressure is related to the laser fluence (F), the absorption coefficient (α) and the thermal expansion coefficient (β) (Xu and Wang, 2006). The pressure generated can be calculated following the equation below:

$$
\mathbf {P} = \Gamma (\beta) \alpha \mathbf {F}
$$

where the Grüneisen parameter (0) is a function of the thermal expansion coefficient β. To improve the optoacoustic conversion efficiency, materials with greater light absorption and larger thermal expansion coefficients are preferred. Previously, many materials have been studied for efficient optoacoustic conversion, including metal, carbon material, etc. Metals, in the form of gold nanoparticles (Wu et al., 2011, 2012, 2013; Tian et al., 2013; Zou et al., 2014) and Cr and Ti films (Lee and Guo, 2017) were used due to their high absorption coefficient. However, the high light reflection by metal films and scattering of metal nanoparticles limit the energy conversion efficiency. Different carbon materials have also been studied, including carbon nanoparticle (CNP) (Biagi et al., 2001), carbon nanotube (CNT) (Won Baac et al., 2010; Colchester et al., 2014; Baac et al., 2015; Alles et al., 2016; Noimark et al., 2016; Moon et al., 2017; Poduval et al., 2017; Shi et al., 2020; Thompson et al., 2022), graphite (Jiang et al., 2020) and candle soot films (CS) (Chang et al., 2015, 2018; Huang et al., 2016). Among these, candle soot stands out for its high light absorption coefficient, low interfacial thermal resistance, and easy fabrication process. Direct comparison of optoacoustic conversion efficiency among CS, CNT, and CNP showed CS can generate a pressure six times higher than that generated by the other two materials (Chang et al., 2018). The CS layer deposited onto polydimethylsiloxane (PDMS), a material with high thermal expansion coefficient (Wolf et al., 2018), forms a diffused mixture—an excellent choice for highly efficient optoacoustic generation.

In this work, we developed a candle soot-based fiber optoacoustic emitter (CSFOE) for the first time. COMSOL simulation was used to simulate the optoacoustic generation process of a CSFOE. We optimized the design of the CSFOE by identifying the optimal thickness of the CS layer through simulation. A CSFOE with a CS layer of an optimal ∼10 µm thickness was found to achieve the highest peak to-peak pressure. Experimentally, we fabricated CSFOEs with controlled thicknesses of candle soot layers in the range of 1 µm to 60 µm. By comparing their optoacoustic performance, we confirmed that the optimal thickness of the CS layer is 10 µm, consistent with the simulation prediction. The maximum optoacoustic pressure reached ∼10 MPa, which is 9.6 times larger compared with that generated by FOC (Jiang et al., 2020; Shi et al., 2021). The application of CSFOE to non-genetic optoacoustic neural stimulation was demonstrated in GCaMP6f labeled neuron culture. Successful high precision activation of neurons confined in an area of 200 µm was verified by calcium imaging. Significantly, we demonstrated dual-site optoacoustic neural stimulation driven by a single laser utilizing the high optoacoustic conversion efficiency of CSFOE. The highly localized ultrasound field generated by each CSFOE allows the two stimulated sites to be sub-millimeter apart. Our work opens up potentials for complex and programmed control in neural circuits using a simple design for multisite neuromodulation.

A  
![](images/348736a68300b0827230828ddd10fffc1839fb0724ad5006a8e9321d377ede07.jpg)

<details>
<summary>text_image</summary>

Ultrasound
PDMS
Candle soot nanoparticle / PDMS mixture
Multi mode fiber
Pulsed laser
3 ns
1.7 kHz
</details>

B  
![](images/a4bd2efc4a833f4470f8849d481342c96ec8f9ab7a691b79b2ee74611fbc301d.jpg)

<details>
<summary>text_image</summary>

Symmetric axis
Water
Pressure
probe
CS/PDMS
PDMS
Fiber
</details>

c  
![](images/7e8280468d7118fed881b0f88d4d5f4934e1ea059bf1b4af74598a2b5012fdd8.jpg)

<details>
<summary>heatmap</summary>

| Value Range | Color Scale |
|-------------|-------------|
| 1           | Red         |
| 0.5         | Blue        |
| 0           | Green       |
| -0.5        | Light Blue  |
| -1          | Dark Blue   |
</details>

D  
![](images/24b83c359f7a04eca8578507daee2cd5b1178276d606f98af2064b1a5aad8c6b.jpg)

<details>
<summary>line chart</summary>

| Thickness | Current (a.u.) |
| --------- | -------------- |
| 1 µm      | ~1.0           |
| 3 µm      | ~0.8           |
| 5 µm      | ~0.6           |
| 10 µm     | ~0.4           |
| 40 µm     | ~0.2           |
</details>

E  
![](images/6d67e48e3d07113eb9a0195c3ddc57b75298c53d18b5a34492983b4d7653d94c.jpg)

<details>
<summary>line chart</summary>

| CS layer thickness (μm) | Peak pressure (a.u.) |
| ----------------------- | -------------------- |
| 0                       | 0.0                  |
| 5                       | 1.0                  |
| 10                      | 1.0                  |
| 20                      | 0.8                  |
| 40                      | 0.3                  |
| 60                      | 0.0                  |
</details>

FIGURE 1 COMSOL simulation of CSFOE performance. (A) Schematic of CSFOE. (B) Illustration of the CSFOE model used in simulation. Not to scale (C) Representative ultrasound waveform, simulated at t = 400 ns under an input of a 3 ns pulsed laser. (D) Acoustic waveforms simulated at different thicknesses of the CS layer. (E) Peak-to-peak acoustic pressure plotted as a function of candle soot layer thickness.

## Materials and methods

## Simulation of the ultrasound field generated from candle soot-based fiber optoacoustic emitters

The ultrasound field generated by CSFOE was simulated by COMSOL Multiphysics 5.4. The CSFOE was modeled by a 2D axisymmetric model with a double-layer structure, including an absorber layer of CS and PDMS mixture and a pure PDMS layer. The backing material was set to be a fiber $\left( \mathrm { S i O } _ { 2 } \right)$ . Radiative Beam in Absorbing Media module was used to simulate the absorption of the CSNP-PDMS mixture layer when being applied a nanosecond pulsed laser. The Heat Transfer and Solid Mechanics modules were used to model the thermal expansion caused by the photothermal effect. The Transient Pressure Acoustic module converted the thermal expansion of the absorber into the acoustic signal and simulated the propagation of ultrasound in the water medium. The absorption coefficient of the absorber layer used in the simulation was a measured value by our experiment, and all the other material parameters were set according to COMSOL’s material library database. The time step of the simulation was set to be 0.001 ns at the beginning to fully simulate the nanosecond laser pulse, and then to simply the calculation, the time step was increased to 5,000 ns after the first 10 ns of simulation. The mesh grid size was set to be a physics-controlled mesh in COMSOL and it can adjust its size automatically to a suitable value according to the simulation model.

## Fabrication of candle soot-based fiber optoacoustic emitters

A schematic of the CSFOE is shown in Figure 1A. A flame from a paraffin wax candle served as the source of the candle soot. To fabricate the CSFOE, the tip of a polished multimode optical fiber with a 200 µm diameter (200EMT, Thorlabs) was placed into the center of the flame for 3– 5 s. This step was repeated until the optical fiber was fully coated with flame synthesized candle soot. To prepare the PDMS, the silicone elastomer (Sylgard 184, Dow Corning Corporation, USA) was carefully dispensed into a container to minimize air entrapment. Then, the curing agent was added for a weight ratio of ten to one (silicone elastomer to curing agent). A nanoinjector deposited the PDMS onto the tip of the candle-soot coated fiber. The position of the fiber and the nanoinjector were both controlled by 3D manipulators for precise alignment, and the PDMS coating process was monitored under a lab-made microscope in real time. The coated fiber was stored overnight in a temperature-controlled environment $( 2 0 ^ { \circ } \mathrm { C } )$ for 12 h, to allow the PDMS to cure and fully diffuse into the porous structure of the candle soot.

## Characterization of absorption ability of CS

The absorption of CS with different deposition thicknesses was measured with a photodiode (DET10A2, Thorlabs, USA, covering the detection range from 200 nm to 1,100 nm). Different thicknesses of CS were controlled by the deposition durations. The fiber was connected to a Q-switched 1,030-nm nanosecond laser (Bright Solution, Inc. Calgary Alberta, CA), and the transmission power was detected by the photodiode.

## Characterization of optoacoustic signals

The amplitude of the CSFOE-generated acoustic wave was measured using a needle hydrophone with a 40 µm core sensor (Precision Acoustics, UK). A digital oscilloscope (DSO6014A, Agilent Technologies, CA, USA) recorded the electrical signal from the hydrophone. A four-axis micromanipulator (MC1000e controller with MX7600R motorized manipulator, Siskiyou Corporation, OR, USA), with a resolution of 0.2 µm, controlled the distance between the CSFOE tip and the hydrophone. For the measurement of optoacoustic signals (Figure 2F), CSFOE was aligned with the hydrophone using the micromanipulator until the signal amplitude reached its maximum. The distance between the hydrophone and the CSFOE was kept to be within the sub-millimeter range. The same alignment has been performed to all the CSFOE for Figure 2F.

For distance-dependent characterization of optoacoustic signal intensity in Figure 2I, the distance was precisely controlled using a widefield microscope with a 10 × objective, which was incremented from 0 to 400 µm (as shown in Supplementary Figure 1). The CSFOE tip and the hydrophone tip were both immersed in a drop of degassed water placed on a glass microscope slide. The CSFOE was connected to a Q-switched 1,030-nm nanosecond laser (Bright Solution, Inc. Calgary Alberta, CA) with a laser pulse energy of 24, 46, 56, and 65 µJ, respectively. The setup of the measurement is shown in Figure 2D. The acoustic pressure values were calculated based on the calibration curve obtained from the hydrophone manufacturer. The frequency data were obtained through the Fast Fourier Transform (FFT) using MATLAB R2020a. For visualizing the acoustic wavefront, a Q-switch Nd: YAG laser (Quantel Laser CFR ICE450) was used to deliver 8 ns pulses to the CSFOE. The generated acoustic signal was capture by a 1 × 128 linear transducer array (L22-14, Verasonics Inc.)

and processed by an ultrasound imaging system (Vantage128, Verasonics).

## Embryonic neuron culture

Primary cortical neuron cultures were derived from Sprague-Dawley rats. Cortices were dissected from embryonic day 18 (E18) rats of either sex and then digested in papain (0.5 mg/mL in Earle’s balanced salt solution) (Thermo Fisher Scientific Inc., MA). Dissociated cells were washed with and triturated in 10% heat-inactivated fetal bovine serum (FBS, Atlanta Biologicals, GA, USA), 5% heat-inactivated horse serum (HS, Atlanta Biologicals, GA, USA), 2 mM Glutamine-Dulbecco’s Modified Eagle Medium (DMEM, Thermo Fisher Scientific Inc., MA, USA), and cultured in cell culture dishes (100 mm diameter) for 30 min at $3 7 ^ { \circ } \mathrm { C }$ to eliminate glial cells and fibroblasts. The supernatant containing neurons was collected and seeded on poly-D- lysine coated cover glass and incubated in a humidified atmosphere containing 5% $\mathrm { C O } _ { 2 }$ at $3 7 ^ { \circ } \mathrm { C }$ with 10% FBS + 5% HS + 2 mM glutamine DMEM. After 16 h, the medium was replaced with Neurobasal medium (Thermo Fisher Scientific Inc., MA, USA) containing 2% B27 (Thermo Fisher Scientific Inc., MA, USA), 1% N2 (Thermo Fisher Scientific Inc., MA, USA), and 2 mM glutamine (Thermo Fisher Scientific Inc., MA, USA). On day five, cultures were treated with 5 µM FDU (5-fluoro-2’-deox- yuridine, Sigma-Aldrich, MO, USA) to further reduce the number of glial cells. Additionally on day five, the pAAV.Syn.GCaMP6f.WPRE.SV40 virus (Addgene, MA, USA) was added to the cultures at a final concentration of 1 µL/mL for GCaMP6f expression and has cre-independent expression already with no Cre virus involved in the process. Half of the medium was replaced with fresh culture medium every 3–4 days. Cells cultured in vitro for 10–13 days were used for CSFOE stimulation experiment.

## In vitro neurostimulation

In vitro neurostimulation experiments were performed using a Q-switched 1,030-nm nanosecond laser (Bright Solution, Inc. Calgary Alberta, CA). A 3-D micromanipulator (Thorlabs, Inc., NJ, USA) was used to position the CSFOE in the cell culture dish. Calcium fluorescence imaging was performed on a lab-built wide-field fluorescence microscope based on an Olympus IX71 microscope frame with a 20 × air objective (UPLSAPO20X, 0.75NA, Olympus, MA, USA), illuminated by a 470 nm LED (M470L2, Thorlabs, Inc., NJ, USA) and a dichroic mirror (DMLP505R, Thorlabs, Inc., NJ, USA). Image sequences were acquired with a scientific CMOS camera (Zyla 5.5, Andor) at 20 frames per second. Neurons expressing GCaMP6f at DIV (day in vitro) 10–13 were used for the stimulation experiment. For the tetrodotoxin (TTX) control group, tetrodotoxin citrate (ab120055, Abcam, MA, USA) was added to the culture to reach 3 µM final concentration 10 min before Calcium imaging. The fluorescence intensities, data analysis, and exponential curve fitting were analyzed using ImageJ (Fiji) and MATLAB R2020a.

## Data analysis

Calcium images were analyzed using ImageJ. The fluorescence intensity was measured by selecting the soma. Calcium traces, acoustic waveform and temperature traces were analyzed using MATLAB R2020a and Prism 9. All statistical analysis was done using MATLAB R2020a. All statistical analysis was done using two-sample t-test otherwise specified. Data shown are mean ± standard deviation.

## Results

## Simulation of acoustic waveforms generated from candle soot-based fiber optoacoustic emitters

To identify the optimal condition toward maximized optoacoustic conversion efficiency, we used COMSOL Multiphysics 5.4 to simulate the generation and propagation of the optoacoustic signals. Taking advantage of COMSOL’s ability of multiple physics field simulations, we simulated the different steps of optoacoustic generation: laser absorption, thermal expansion, and acoustic wave propagation. Since the candle soot has a very porous structure, the PDMS diffuses into the candle soot layer, forming a uniformly mixed candle soot/PDMS mixture layer (Chang et al., 2015). Therefore, we included a candle soot/PDMS mixture layer and a pure PDMS layer in the 2D axisymmetric CSFOE model built in COMSOL Multiphysics 5.4 for simulation (Figure 1B). A single 3 ns laser pulse was delivered through a multimode fiber (with a 200 µm core diameter) to the double layer coating on the fiber tip. Figure 1C shows a representative wave front of the generated ultrasound 400 ns after the onset of the laser, indicating a bipolar pressure signal generated by CSFOE (Figure 1C, red: positive pressure; blue: negative pressure). Figure 1D plots the time domain waveforms when the thickness of the CS/PDMS layer varied from 1 µm to 40 µm. In Figure 1E, the normalized peak-to-peak amplitude of the generated PA signal is plotted as a function of the thickness of the CS/PDMS mixture layer. The optimal thickness of the CS/PDMS layer, which generates the largest amplitude PA signal, was found to be ∼10 µm. This result is consistent with the previous work, where an optimal thickness generating the maximum pressure was also found (Chang et al., 2018).

## Fabrication and characterization of candle soot-based fiber optoacoustic emitters

To fabricate the optimal CSFOE, as guided by the simulations, we developed a two-step fabrication procedure to precisely control the CS layer thickness (Figure 2A). A polished multimode fiber with a 200 µm core diameter (Thorlabs) was inserted into a fiber ferrule. The fiber tip was positioned so that it was flush with the distal end of the ferrule. Then, the distal tips of both the ferrule and fiber were placed into the flame core of a paraffin wax candle, where they were fully coated with flame synthesized candle soot (Figure 2A, left). The key parameter to control the thickness of the CS was the coating time, which ranged between 1 and 20 s. Then, a nanoinjector was used to deposit a controlled amount of PDMS (∼0.01 µm3) onto the tip of the fiber coated with candle soot (Figure 2A, middle). The transmission images of the CS-coated fiber before and after PDMS coating are also shown in Figure 2A (right). When varying the CS coating time, the thickness of the CS coating was measured from the transmission images of samples before PDMS coating. Figure 2B plots the thickness of the CS layer measured as a function of deposition time. The CS layer thickness was linearly proportional to the deposition time, with an estimated deposition rate of 3.04 µm/s, similar to previous reports (Chang et al., 2018). Such a linear relation enables us to precisely control the thickness of the CS layer to study the PA conversion as a function of the layer thickness. Transmission of CS layers with different thicknesses were also measured (Figure 2C). The normalized transmission of the coating exponentially decreased as a function of the thickness. An absorption depth, the thickness when the transmission decreased to 1/e of initial transmission at the zero thickness was obtained as 6.6 µm. This measured ultrathin absorption depth indicated strong absorption of CS in NIR, enabling efficient ultrasound generation.

The characterization of the CSFOE with various CS/PDMS layer thicknesses was performed with a 40 µm needle hydrophone. A 1,030 nm nanosecond pulsed laser, with a 46 µJ pulse energy was delivered to the CSFOE to generate optoacoustic signals. The acoustic signals were measured for CSFOEs where the thickness of the CS-PDMS mixture layer ranged from 1 µm to 57 µm (Figure 2D,E). The peakto-peak pressure is plotted as a function of the CS layer thickness in Figure 2F. An optimal thickness of ∼10 µm was found to generate the highest peak-to-peak pressure of 9 MPa. Notably, the experimentally measured optimal thickness and the trend between the thickness and the peakto-peak pressure are consistent with the simulation results. Importantly, the 10 µm optimal thickness was also found to be close to the 6.6 µm absorption depth of CS-PDMS layer obtained from the absorption shown in Figure 2C. The greatest optoacoustic conversion efficiency occurred when the

A  
![](images/93221ace33af828d6454ec57435f259f526face6d942166822b4bdf0af8cce17.jpg)

<details>
<summary>text_image</summary>

Fiber
Ferrule
Candle
soot
Candle
200 µm
-PDMS +PDMS
</details>

B  
![](images/447da67102109296633ad70f1b2b2bc0574787faf967945851f36617e32b1e1f.jpg)

<details>
<summary>line chart</summary>

| Duration (s) | Thickness (µm) |
| ------------ | -------------- |
| 0            | 0              |
| 5            | 10             |
| 10           | 25             |
| 15           | 45             |
| 20           | 60             |
</details>

c

![](images/0558016c8b697c7fc2768f7d7ebf8c0f94274be0d6929c2beda0a16939991574.jpg)

<details>
<summary>line chart</summary>

| Initial CS layer thickness (μm) | Laser transmission (%) |
| ------------------------------- | ---------------------- |
| 0                               | 100                    |
| 10                              | 20                     |
| 20                              | 5                      |
| 40                              | 1                      |
| 60                              | 0                      |
</details>

D  
![](images/339f694c29f9b2a441e996b8d9d12984d5369b9e7fec73f16ec63d5391de610b.jpg)

<details>
<summary>text_image</summary>

CSFOE
Water drop
Needle hydrophone
Glass Slide
objective
Setup Schematic
</details>

E  
![](images/5bffc4b7a045ea277e8aad409dbdc6c6b3cb75d400fb463bb169f7b44765a818.jpg)

<details>
<summary>line chart</summary>

| Thickness | Pressure (MPa) at 50 ns |
| --------- | ------------------------ |
| 1 µm      | ~10                      |
| 3 µm      | ~10                      |
| 12 µm     | ~10                      |
| 42 µm     | ~10                      |
| 57 µm     | ~10                      |
</details>

F  
![](images/8bbc761f878e2809b414bb37881e1c147e83f79044ddb8ee3a5e5254e6a1735f.jpg)

<details>
<summary>scatterplot</summary>

| Thickness (μm) | Peak to Peak Pressure (MPa) |
| -------------- | --------------------------- |
| 0              | 8                           |
| 10             | 8                           |
| 40             | 5                           |
| 60             | 2                           |
</details>

G  
![](images/edb0270ed75a8d40fb0d7388d957f4836679b00451ada10801386fd8fa98dc8f.jpg)

<details>
<summary>line chart</summary>

| Time (ns) | Pressure (MPa) | Magnitude |
| --------- | -------------- | --------- |
| 0         | 0              | 0         |
| 50        | 10             | 0.5       |
| 100       | 9              | 0.5       |
| 150       | -5             | 0         |
| 200       | 0              | 0         |
| 250       | 0              | 0         |
</details>

H  
![](images/6d354f72298f61db9fbbf9b5c10862752a613326ee21321f9dd2c34aefa93856.jpg)

<details>
<summary>line chart</summary>

| Particle Size | Pressure (MPa) |
| ------------- | -------------- |
| 42.4 µm       | ~0.8           |
| 105 µm        | ~0.6           |
| 174 µm        | ~0.5           |
| 240 µm        | ~0.4           |
| 300 µm        | ~0.3           |
</details>

![](images/d0a841a76a74bf278396739ca1db2904dc537ca6c9df7afa4b4039bb83eb8181.jpg)

<details>
<summary>scatterplot</summary>

| Distance away from CSFOE (μm) | Peak to Peak Pressure (MPa) |
| :--- | :--- |
| 50 | 14.5 |
| 75 | 14.3 |
| 100 | 14.2 |
| 125 | 12.8 |
| 150 | 12.5 |
| 175 | 9.5 |
| 200 | 8.5 |
| 225 | 7.8 |
| 250 | 6.8 |
| 300 | 5.2 |
| 350 | 4.8 |
| 400 | 3.8 |
</details>

J  
![](images/8fca3b62f91ce75245903d211a7a4f27923903de8717f1bc0801a0dac4b73fe9.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing red fluorescent patterns with a 5 mm scale bar (no text or symbols)
</details>

K  
![](images/33f758040500373c21d6ab170758b683da54a05ed2d0880b8dded3a00da997b0.jpg)

<details>
<summary>line chart</summary>

| Current Density | Time (ns) | Current (MPa) |
| --------------- | --------- | ------------- |
| 65 µJ           | 50        | ~100          |
| 56 µJ           | 50        | ~80           |
| 46 µJ           | 50        | ~70           |
| 24 µJ           | 50        | ~60           |
</details>

L  
![](images/6817ebd478e55b66ec499a710c660d9c8f2cb81e159c080f6e52c7c688cd0925.jpg)

<details>
<summary>scatterplot</summary>

| Input Energy (μJ) | Peak to Peak Pressure (MPa) |
| ----------------- | --------------------------- |
| 20                | 5                           |
| 40                | 8                           |
| 60                | 12                          |
| 65                | 15                          |
</details>

FIGURE 2 Fabrication and characterization of CSFOE. (A) Key steps of CSFOE fabrication. (Left) Candle soot deposition on an optical fiber tip. (Middle) PDMS coating on the surface of the CS layer using a nanoinjector. (Right) Images of samples after CS deposition and PDMS coating, respectively. Scale bars: 200 µm. (B) Thickness of the CS layer obtained as a function of deposition duration. Inset: representative image of a fiber coated with candle soot. (C) Transmission ratio plotted as a function of the thickness of CS layer. (D) Schematic of experimenta configuration of photoacoustic signal measurement using a 40 µm needle hydrophone. Created with BioRender.com. (E) Acoustic signal of CSFOE as a function of the candle soot layer thickness detected by the hydrophone. Laser condition: 1,030 nm, 1.7 kHz repetition rate, 46 µJ per pulse. (F) Peak to peak pressure plotted as a function of the thickness of CS under the same laser condition as (E). (G) Representative photoacoustic waveform (Black) detected by the hydrophone and its FFT frequency spectrum (Red). laser condition: 1,030 nm, 56 µJ pulse energy. (H,I) Acoustic signal and peak-to-peak pressure generated by CSFOE detected at different distances from the CSFOE tip. Each data point was an average of three trials. laser condition: 1,030 nm, 56 µJ pulse energy, distance between hydrophone and CSFOE: 70 µm (J) Photoacoustic signal propagation in the medium detected by a linear transducer array. Fiber tip (Yellow), PA waveform (red). (K,L) Photoacoustic waveforms and peak-to-peak pressures measured at different laser pulse input. Each data point was an average of three trials, distance between hydrophone and CSFOE: 70 µm.

absorption layer thickness equaled the material absorption depth. In the thickness range < 10 µm, when increasing the absorption layer thickness, the thickness at the absorption depth allowed complete optical absorption. Further increasing the thickness beyond the absorption depth (> 10 µm) led to acoustic attenuation, as demonstrated in previous works (Chang et al., 2018).

Frequency characterization of the generated optoacoustic signal is shown in Figure 2G. The frequency spectrum of the measured acoustic waveforms after Fast Fourier Transform (FFT) exhibited a peak acoustic frequency of 12.8 MHz. This frequency was similar to previous studies on candle-sootbased optoacoustic films (Chang et al., 2018), in which a central frequency of ∼10 MHz was detected for ∼2 µm CS coating thickness. Based on the frequency analysis of ultrasound signal generated, CSFOE emitted broadband high-frequency ultrasound centered at 12.8 MHz. Previous studies have reported that, for laser-induced ultrasound, the generated ultrasound waveform is mainly determined by the absorption of the material and the laser duration (Lee et al., 2018). For CSFOE, in principle, the central frequency can be controlled by the absorption ability of candle soot through changing the candle soot thickness when the physical thickness is smaller than the absorption depth, which is approximately 6.6 µm. Specifically, thinner thicknesses lead to a higher frequency. It is evident that CSFOE with 1 µm CS produces a central frequency of 27.3 MHz while CSFOE with 12 µm CS has a central frequency of 10.6 MHz (Supplementary Figure 2).

To map the propagation of the optoacoustic wave generated by the CSFOE, the pressure was measured at different distances away from the CSFOE using a 40 µm needle hydrophone as shown in Figure 2H (N = 3 for each distance). The peak-to-peak pressure of the generated ultrasound is plotted as a function of distance in Figure 2I. The measurements were repeated for three times and the average values were plotted. The confinement of the generated acoustic field, defined by the distance where the pressure decreases to 1/e of the initial pressure at 0 µm, was found to be ∼300 µm, approximately equal to the size of the fiber core. Such decay of optoacoustic pressure over the distance away from the CSFOE tip enables a sub-millimeter localized neuron stimulation. In addition, Figure 2I shows that the dependence on distance is different from the previous $1 / \mathrm { r } ^ { 2 }$ relation obtained in FOC. The difference is due to the fact that the ultrasound field emitted by CSFOE is at a higher frequency, therefore propagates more directionally, compared with more omnidirectional propagation of the lower frequency FOCs (Jiang et al., 2020).

The propagation of generated ultrasound can be directly visualized using an optoacoustic tomography system (Figure 2J). The acoustic signal was detected by ${ \texttt { a 1 } } \times \ 1 2 8$ linear transducer array (L22-14, Verasonics Inc.) and processed by an ultrasound imaging system (Vantage128, Verasonics). The emitted ultrasound waveform (red) obtained with a time interval of 0.5 µs and the image of the tip of the CSFOE (yellow) are overlaid in Figure 2J. Through the photoacoustic waveform shown in Figure 2J, the emission angle of CSFOE was measured to be 25.3 degrees. For FOC reported previously (Jiang et al., 2020), the emission angle was measured to be 55.1 degrees which is around twice as large. This observation also supports the more directional propagation for the CSFOE generated ultrasound field (Jiang et al., 2020).

Different laser energy inputs also resulted in varied output pressures. Using different fiber attenuators to control the laser energy input, the waveform of generated acoustic signal was measured by the needle hydrophone (Figure 2K) (N = 3 for each energy condition), and the peak-to-peak pressure is plotted as a function of input energy in Figure 2L, showing a fitting curve of $P = 0 . 2 2 6 ^ { \ast } E ( R ^ { 2 } = 0 . 9 3$ , fitting coefficient of determination) confirming the linear dependence of the pressure on the input laser energy. We observed potential coating damage when the laser energy was greater than 65 µJ under the pulse train composed of five laser pulses, which limits the maximum pressure the device can produce. We conclude the 15 MPa is the CSFOE pressure up limit under a 1.7 kHz repetition rate, 3 ms pulse train duration (5 pulses) and pulse energy of 56 µJ. It is expected to produce higher pressure driven by energy larger than 56 µJ and a shorter pulse train than five pulses. Through controlling the distance away from the CSFOE tip and laser energy, we can have a complete control of the generated pressure in a large range under 15 MPa for various applications. By rationale fabrication of the layered structure of CSFOE and control of PA pressure generated, CSFOE can serve as a robust device for repeatable neuromodulation and allows us to study neuron responses under different conditions.

## Candle soot-based fiber optoacoustic emitter stimulation of neurons in vitro

To confirm the stimulation function of the CSFOE, GCaMP6f-labeled primary neurons (DIV 10-13) were cultured on a glass bottom dish, and calcium imaging was performed to monitor neuronal activities. A 3 ns pulsed laser at 1030 nm with a repetition rate of 1.7 kHz was delivered to the CSFOE. The laser pulse train, with a duration of 3 ms (corresponding to 5 pulses) and pulse energy of 65 µJ, was used for CSFOE optoacoustic in vitro neural stimulation. The CSFOE was precisely controlled by a 4D micromanipulator to approach the target neurons. The distance between the neurons and the CSFOE tip was monitored to make sure neurons were within the sub-millimeter confinement area.

Representative fluorescence images of the neuron before and after stimulation are shown in Figures 3A,B. Maximum change of the fluorescence intensity is highlighted in Figure 3C. The dashed circles indicate the location of the CSFOE. Increase in fluorescence intensity $\Delta F / F _ { 0 } > 1 0 \%$ upon stimulation confirms the successful activation. This map of fluorescence changes in Figure 3C also indicates that neurons within the stimulation area were successfully activated. The activation outside the stimulation area is due to networking effect (more details discussed later). To further investigate whether the CSFOE can activate neurons reliably and repeatedly, we stimulated the same area of neuron three times in 4 min (Figure 3D). Repeatable stimulations were successfully observed after the laser onset at t = 5 s, 90 s and 180 s, and all show $\Delta F / F _ { 0 } > 1 0 \%$ . This result clearly shows that there is no damage caused by CSFOE after stimulation and demonstrates the repeatability and safety of CSFOE stimulation.

A  
![](images/2ab09d9383debd82c44173a609ea4510d67cf87ff6e037082813bb53d9396232.jpg)

<details>
<summary>natural_image</summary>

Dark circular object with dashed outline on blue background, labeled 'Before' in top-left corner (no other text or symbols)
</details>

B  
![](images/0f6002f5e245e1c74bd467ff91fabd158153eb1e1e28784568960c1a3d2ca709.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescently labeled cells with a dashed circular region, labeled 'After' (no text or symbols within the image itself)
</details>

![](images/d156e55337cad3d348724c4cc5cd7430dcb1ca2014bd6de87935b40286cc188c.jpg)

<details>
<summary>text_image</summary>

Max ΔF/F₀
ΔF/F₀
</details>

D

![](images/4a69886c7adf7f6a1cfc56b0ac411e0c5f39f510687e0bf71c005c74a90e0131.jpg)

<details>
<summary>line chart</summary>

| Time (s) | ΔF/F₀ |
| -------- | ----- |
| 0        | 0.14  |
| 50       | 0.03  |
| 100      | 0.13  |
| 150      | 0.03  |
| 200      | 0.14  |
| 250      | 0.03  |
</details>

E  
![](images/4fe3cb7aeb0806cfdbdcd2ea03d4839ce2dff6f50f95567aafaecc2b268d5e39.jpg)

<details>
<summary>heatmap</summary>

| Neuron ID | Time (s) | ΔF/F₀ |
| --------- | -------- | ----- |
| 5         | 0        | ~0    |
| 5         | 5        | ~0    |
| 5         | 10       | ~0    |
| 5         | 15       | ~0    |
| 5         | 20       | ~0    |
| 10        | 0        | ~0    |
| 10        | 5        | ~0    |
| 10        | 10       | ~0    |
| 10        | 15       | ~0    |
| 10        | 20       | ~0    |
| 15        | 0        | ~0    |
| 15        | 5        | ~0    |
| 15        | 10       | ~0    |
| 15        | 15       | ~0    |
| 15        | 20       | ~0    |
| 20        | 0        | ~0    |
| 20        | 5        | ~0    |
| 20        | 10       | ~0    |
| 20        | 15       | ~0    |
| 20        | 20       | ~0    |
</details>

![](images/f26e7deee6f7f40f6d6e51b41dc87c31b1780458a864974b46fefa9dac364207.jpg)

<details>
<summary>heatmap</summary>

| Neuron ID | Time (s) | ΔF/F₀ |
| --- | --- | --- |
| 1 | 0 | 0.0 |
| 1 | 5 | 0.2 |
| 1 | 10 | 0.4 |
| 1 | 15 | 0.6 |
| 1 | 20 | 0.8 |
| 1 | 25 | 1.0 |
| 2 | 0 | 0.0 |
| 2 | 5 | 0.2 |
| 2 | 10 | 0.4 |
| 2 | 15 | 0.6 |
| 2 | 20 | 0.8 |
| 2 | 25 | 1.0 |
| 3 | 0 | 0.0 |
| 3 | 5 | 0.2 |
| 3 | 10 | 0.4 |
| 3 | 15 | 0.6 |
| 3 | 20 | 0.8 |
| 3 | 25 | 1.0 |
| 4 | 0 | 0.0 |
| 4 | 5 | 0.2 |
| 4 | 10 | 0.4 |
| 4 | 15 | 0.6 |
| 4 | 20 | 0.8 |
| 4 | 25 | 1.0 |
| 5 | 0 | 0.0 |
| 5 | 5 | 0.2 |
| 5 | 10 | 0.4 |
| 5 | 15 | 0.6 |
| 5 | 20 | 0.8 |
| 5 | 25 | 1.0 |
| 6 | 0 | 0.0 |
| 6 | 5 | 0.2 |
| 6 | 10 | 0.4 |
| 6 | 15 | 0.6 |
| 6 | 20 | 0.8 |
| 6 | 25 | 1.0 |
| 7 | 0 | 0.0 |
| 7 | 5 | 0.2 |
| 7 | 10 | 0.4 |
| 7 | 15 | 0.6 |
| 7 | 20 | 0.8 |
| 7 | 25 | 1.0 |
| 8 | 0 | 0.0 |
| 8 | 5 | 0.2 |
| 8 | 10 | 0.4 |
| 8 | 15 | 0.6 |
| 8 | 20 | 0.8 |
| 8 | 25 | 1.0 |
| 9 | 0 | 0.0 |
| 9 | 5 | 0.2 |
| 9 | 10 | 0.4 |
| 9 | 15 | 0.6 |
| 9 | 20 | 0.8 |
| 9 | 25 | 1.0 |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | .0 |
| ... | ... | .2 |
| ... | ... | .4 |
| ... | ... | .6 |
| ... | ... | .8 |
| ... | ... | .10 |
| ... | ... | .3 |
| ... | ... | .5 |
| ... | ... | .7 |
| ... | ... | .9 |
| ... | ... | .11 |
| ... | ... | .33 |
| ... | ... | .55 |
| ... | ... | .77 |
| ... | ... | .99 |
| ... | ... | .136 |
| ... | ... | .366 |
| ... | ... | .596 |
| ... | ... | .836 |
| ... | ... | .996 |
| ... | ... | .1666 |
| ... | ... | .3966 |
| ... | ... | .6366 |
| ... | ... | .8866 |
| ... | ... | .1176 |
| ... | ... | .3396 |
| ... | ... | .5796 |
| ... | ... | .8296 |
| ... | ... | .1396 |
| ... | ... | .3796 |
| ... | ... | .6296 |
| ... | ... | .8896 |
| ... | ... | .1396 |
| ... | ... | .3896 |
| ... | ... | .6396 |
| ... | ... | .8896 |
| ... | ... | .1396 |
| ... | ... | .3896 |
| ... | ... | .6396 |
| ... | ... | .8896 |
| ... | ... | .1396 |
</details>

![](images/e98c71d391100dcd097570dcf597665ea69192d9539e3f993adf2b59adc135b4.jpg)

<details>
<summary>heatmap</summary>

| Neuron ID | Time (s) | ΔF/F₀ |
| --------- | -------- | ----- |
| 2         | 0        | 0     |
| 2         | 5        | 0     |
| 2         | 10       | 0     |
| 4         | 0        | 0     |
| 4         | 5        | 0     |
| 4         | 10       | 0     |
| 6         | 0        | 0     |
| 6         | 5        | 0     |
| 6         | 10       | 0     |
| 8         | 0        | 0     |
| 8         | 5        | 0     |
| 8         | 10       | 0     |
| 10        | 0        | 0     |
| 10        | 5        | 0     |
| 10        | 10       | 0     |
</details>

![](images/f9cacead6e36c357023ae0c0aea6c70d1581c95b508f49b4e267b85bf0c2e6b9.jpg)

<details>
<summary>line chart</summary>

| Time (s) | 65 µJ | 56 µJ | 46 µJ |
| -------- | ----- | ----- | ----- |
| 0        | 0.0   | 0.0   | 0.0   |
| 5        | 0.0   | 0.0   | 0.0   |
| 10       | 1.0   | 0.8   | 0.4   |
| 15       | 1.1   | 0.7   | 0.3   |
| 20       | 1.0   | 0.5   | 0.2   |
| 25       | 0.9   | 0.3   | 0.1   |
</details>

![](images/64f8872bf56a9be65d0aa1411b1bbd5c9d2180efe08dab9c40267c014eaeccf6.jpg)

<details>
<summary>bar chart</summary>

| Pulse Energy | Max ΔF/F₀ |
| ------------ | --------- |
| 65 μJ        | 1.0       |
| 56 μJ        | 0.5       |
| 46 μJ        | 0.0       |
</details>

![](images/d0d4c017979d77f09847d0ca0e29480a84f06012b142c8f2af1bb2dec023bb9c.jpg)

<details>
<summary>line chart</summary>

| Time (s) | CS-FOE | Laser Only | CS-FOE+TTX |
| -------- | ------ | ---------- | ---------- |
| 0        | 0.0    | 0.0        | 0.0        |
| 5        | 0.0    | 0.0        | 0.0        |
| 10       | 0.8    | 0.0        | 0.0        |
| 15       | 0.4    | 0.0        | 0.0        |
| 20       | 0.2    | 0.0        | 0.0        |
| 25       | 0.1    | 0.0        | 0.0        |
</details>

K  
![](images/37f840720e67032902e5ce925ad3391bc3e7c0e2a8384bd87cf01fa33d8f702a.jpg)

<details>
<summary>heatmap</summary>

| Time (s) | Value |
| -------- | ----- |
| 0        | 0     |
| 5        | 0     |
| 10       | 0     |
| 15       | 0     |
</details>

![](images/6dcedb11d4446430a46609d4f7a63c0680cf355403c3128fc611f99ce01794b1.jpg)

<details>
<summary>line chart</summary>

| Time (s) | w/o S.B. | w/ S.B. |
| -------- | -------- | ------- |
| 0        | 0.0      | 0.0     |
| 5        | 0.0      | 0.0     |
| 10       | 1.2      | 1.0     |
| 15       | 1.0      | 0.8     |
| 20       | 0.8      | 0.6     |
| 25       | 0.6      | 0.4     |
</details>

![](images/1732a5ba70a7c6f7b1c466a9c62ca09e177bf21c3b65b7ac15e64b2cdb308224.jpg)

<details>
<summary>bar chart</summary>

| Group | Time constant (s) |
|-------|-------------------|
| w/o S.B. | 30 |
| w S.B. | 10 |
</details>

![](images/28b16c213ce435844e38f4e5b524312326e7618f4fae082fd08b5a1c97dd2c91.jpg)

<details>
<summary>natural_image</summary>

Thermal or emission imaging view showing a bright central region with concentric color scale (0.1 to 1.4) and a dashed circle highlighting a feature, no text or symbols present.
</details>

![](images/0ebcbec939c9be97ae4a3d610831f09928fc8b85d85cbb19e423103bce22e54b.jpg)

<details>
<summary>bar chart</summary>

| Distance away from CSFOE (µm) | Max ΔF/F₀ |
| ----------------------------- | --------- |
| 0-50                          | 0.9       |
| 50-100                        | 0.6       |
| 100-150                       | 0.1       |
| >150                          | 0.0       |
</details>

FIGURE 3 Activation of GCaMP6f-expressing cortical neurons by CSFOE stimulation. (A,B) Representative fluorescence of neurons from three batches stimulated by CSFOE before stimulation (A) and after stimulation (B). (C) Map of the maximum fluorescence change $\Delta F / F _ { 0 }$ induced by the CSFOE stimulation. Laser condition: 3 ms duration, pulse energy $6 5 ~ \mu \ J$ . Scale bar: 200 µm. (D) Calcium trace shows repeatable activation of the same neuron. Laser condition: 3 ms duration, pulse energy 56 µJ. (E–G) Colormaps of fluorescence change in neurons stimulated by CSFOE with a laser pulse energy of 65 µJ (E) (N = 20), 56 µJ (F) $( N = 1 0 )$ , and 46 µJ (G) (N = 10). (H) Average calcium traces of neurons obtained from (E,F,G) with the pulse energy of 65 µJ (Red) $( N = 2 0 )$ , 56 µJ (Blue) (N = 10) and 46 µJ (black) $( N = 1 0 )$ , respectively. The shaded region corresponds to one standard deviation. Laser turns on at t = 5 s (red dashed lines). The duration of each stimulation was fixed at 3 ms (I) Average of maximum fluorescence intensity changes shown in (E–G). Error bars represent standard deviation. \*\*\*p < 0.001, one way AVOVA test. (J) Average calcium traces of neurons of CSFOE stimulation, Laser only control and TTX control. Each group was repeated three times on three different dishes of neurons $( N = 1 0$ for each condition). (K) Colormaps of fluorescence change in neurons of a laser only control group. (L) Average calcium traces with (Red) $( N = 3 0 )$ and without (Blue) synaptic blocker $( N = 3 0 )$ . Laser is on at $t = 5 :$ s. laser condition: 1,030 nm, 1.7 kHz repetition rate, 65 µJ pulse energy (M) Time constant of the decay of the fluorescence trace with and without synaptic blockers $^ { \star \star \star } p < 0 . 0 0 1$ , two sample t-test. (N) Spatial distribution of maximum neuronal calcium response induced by CSFOE stimulation. Scale bar: 200 µm. Dashed circle: indication of the CSFOE position. (O) Maximum $\Delta F / F _ { 0 }$ changes over the distance away from the CSFOE (N = 6 for 0–50 µm group, N = 4 for 50–100 µm group, N = 5 for 100–150 µm group, N = 7 for > 150 µm group).

Next, we investigated the effect of laser pulse energy on CSFOE stimulation. Each pulse train was fixed to be 3 ms long. Three laser pulse energies, 65, 56, and 46 µJ, were applied to the CSFOE to modulate neural activities. Responses from neurons at each pulse energy are plotted as heatmaps in Figures 3E– G. Representative calcium traces are plotted in Figure 3H. The averages of maximum fluorescence change obtained from these three groups are compared in Figure 3I. With the laser pulse energy of 65 and 56 µJ, neurons showed an average maximum fluorescence change $\left( \Delta F / F _ { 0 } \right)$ of 99.8 ± 23.3% and $4 7 . 4 \pm 3 3 . 9 \%$ , while with laser energy of 46 µJ, the induced fluorescence change is negligible $( 1 . 2 \pm 1 . 0 \% )$ . These results indicate that at the laser pulse train with the repetition rate of 1.7 kHz and 3 ms duration, the activation threshold is between 46 and $5 6 \mu \mathrm { J } ,$ corresponding to a pressure of ∼8 MPa. To better statistically analyze the data from different groups, one-way ANOVA was used to determine the significant difference. The P-value is $5 . 4 7 \times 1 0 ^ { - 7 }$ between the 65 and 56 µJ groups, 9.56 $\times \ 1 0 ^ { - 1 0 }$ between the 65 and 46 µJ groups, and $1 . 2 9 \times 1 0 ^ { - 5 }$ between the 56 and 46 µJ $( N = 2 0$ for 65 µJ group, $N = 1 0$ for 56 µJ group and $N = 1 0$ for 46 µJ group), and all groups show significant difference to each other.

To confirm that the observed activation was due to optoacoustic stimulation, we performed a laser-only control and compared it to the calcium traces of CSFOE-stimulated neurons. The laser-only control group used the same optical fiber without any coatings on the tip, and with the same repetition rate of 1.7 kHz, 3 ms duration and laser pulse energy of 56 µJ. No significant fluorescence response was observed in the laser only group (Figures 3J,K). Optical excitation alone triggered negligible activities. Additionally, to investigate whether the activations observed were caused by action potential, we performed a control experiment with addition of 3 mM tetrodotoxin (TTX), a blocker of voltagegated sodium channels. No significant fluorescence response was observed in the TTX group (Figure 3J), indicating that the observed calcium transients under CSFOE stimulation were induced by the firing of action potentials $( N = 1 0$ for each condition). These results are also consistent with previous studies of optoacoustic stimulation (Jiang et al., 2021).

To investigate how synaptic inputs affects the stimulation outcomes, we applied a cocktail of synaptic blockers (10 µM NBQX, 10 µM gabazine, and 50 µM DL-AP5). Averaged traces of stimulated neurons with and without synaptic blockers in both conditions are plotted in Figure 3L. Two types of neuron responses were observed: a transient response under synaptic blocking (blue) and a prolonged response without synaptic blocking (orange). The decay portion of the response curves was fitted exponentially. A time constant for the decay was obtained from the time when the fluorescence intensity decreased by a factor of 1/e from the peak fluorescence intensity. The time constant decreased significantly from $3 2 . 3 2 \pm 2 6 . 1 5$ s without synaptic blocking to $1 0 . 1 5 \pm 8 . 7 0$ s with synaptic blocking. The two group shows significant difference through t-test $( p = 2 . 7 5 e \cdot$ 04). These results demonstrate that transient stimulation is likely to be the result of direct CSFOE optoacoustic stimulation, while the network effect through synaptic transmission results in prolonged stimulations (Jiang et al., 2021).

To demonstrate the stimulation resolution of CsFOE in vitro, we divided all the neurons in the FOV into four parts according to their distance away from the center of the stimulation: 0–50 µm, 50–100 µm, 100–150 µm, 150 µm and above. The averaged maximum $\Delta F / F _ { 0 }$ with standard deviation for neurons in different parts are plotted in Figures 3N,O as follows $( N = 6 \mathrm { f o r } 0  – 5 0$ µm group, N = 4 for 50–100 µm group, $N = 5$ for 100–150 µm group, N = 7 for > 150 µm group). As is shown here, the fluorescence changes of neurons decreased a lot when the distance increased, and no obvious stimulation was observed when the distance is larger than $1 0 0 \mu \mathrm { m }$ . It shows that our CSFOE’s effective stimulation range is highly localized and the effective range is in a circle of a diameter of 200 µm.

## Comparison between candle soot-based fiber optoacoustic emitters and fiber-optoacoustic converters

To evaluate the performance improvement of CSFOE from the previous FOC fabricated using graphite and epoxy, we first compared the design of CSFOE and FOC. As shown in Figure 4A, both CSFOE and FOC have two-layer structures. Compared with FOC, several improvements were made on the CSFOE regarding the choice of material and structure design. Instead of using a graphite-epoxy system, a CS/PDMS mixture was used in CSFOE as the optoacoustic material. Compared to the previous design, CS has stronger absorption while PDMS is well known for its huge expansion coefficient of $3 1 0 ~ { \mu \mathrm { m } } ~ \mathrm { m } ^ { - 1 }$ $^ \circ C ^ { - 1 }$ . The thickness of the CS layer in the CSFOE was optimized to obtain the largest pressure.

To directly compare the performance, we compared the pressure generated by CSFOE and FOC under the same laser condition. A transducer with greater sensitivity compared with the hydrophone was used to measure the generated pressure. As shown in Figure 4B, under the same laser condition of 1,030 nm, 3 ns, 1.7 kHz, 48 mW, CSFOE generated a 9.6 times higher signal than that generated by FOC. In addition, the temperature rise associated with the optoacoustic conversion was measured for both fiber emitters using a thermal coupler (DATAQ DI-245, USA) placed on the surface the fiber tips. According to Figure 4C, the average temperature increases were $0 . 7 9 ^ { \circ } \mathrm { C }$ for the CSFOE and $0 . 7 7 ^ { \circ } \mathrm { C }$ for the FOC. Similar temperature increases suggest that while the CSFOE significantly increased the output pressure, the thermal effect remained minimal. To further study the temperature rise under the condition of in vitro experiments, we used the same laser condition and placed CSFOE ∼10 µm away from the thermal probe. As is shown in Figures 4E,F, the near field thermal effect (∼10 µm away from the tip of the CSFOE) was measured by a thermal coupler. The laser condition was kept to be the same, specifically the pulse energies were 46, 56, and 65 µJ (with a 1.7 kHz repetition rate and 3 ms burst duration), respectively. The temperature was measured at approximately 10 µm away from the CSFOE in the cell medium by placing the thermal probe under a microscope. The measured temperature traces were shown in Figure 4E and the maximum temperature increase was shown in Figure 4F. The maximum temperature increases under 46, 56, and 65 µJ were found to be $0 . 6 9 \pm 0 . 0 4 , 1 . 0 3 \pm 0 . 0 3$ , and $1 . 1 5 \pm 0 . 0 7 ^ { \circ } \mathrm { C }$ respectively, all of which are less than $1 . 5 ^ { \circ } \mathrm { C }$ and far below the threshold for photothermal neuron stimulation in which temperature rise exceeded $1 5 ^ { \circ } \mathrm { C }$ (Zhu et al., 2022). Such a small temperature increase also minimizes the risk of thermal damage for the neural system.

A  
![](images/2498ab42189ddf1fabafbcca145906b3c4482ec8599e188b07f6a97dd39b68ae.jpg)

<details>
<summary>text_image</summary>

CSFOE
PDMS layer
Candle soot /
PDMS mixture
</details>

Graphite / epoxy  
![](images/db1ae06b2a8d6a776aaf495bc95ae9c4473475affb591d444e653a506d939662.jpg)

<details>
<summary>text_image</summary>

FOC
mixture
ZnO / epoxy
mixture
</details>

B  
![](images/6a01c6c56f930e6166432685ef82b1494c37d5cbdfd7f5d7db04a224a4bc8eae.jpg)

<details>
<summary>line chart</summary>

| Condition | CSFOE (V) | FOC (V) |
| --------- | --------- | ------- |
| 0.1 V     | ~0.1      | ~0.1    |
| 2 °C      | ~0.1      | ~0.1    |
</details>

C

![](images/024df5e7c23810e2fa84cd6ff2013fa59af49870c81f96d73455ddf3ab5402a7.jpg)

<details>
<summary>line chart</summary>

| Time (s) | CSFOE | FOC |
| -------- | ----- | --- |
| 0        | ~0    | ~0  |
| 2        | ~0    | ~0  |
</details>

D  
![](images/dbf6b75061bf5317bbf5c278e3f1bab1a1796c2aba2a152180b622fb6bbd2989.jpg)

<details>
<summary>line chart</summary>

| Time (s) | CSFOE | FOC |
| -------- | ----- | --- |
| 0        | 0.0   | 0.0 |
| 5        | 0.4   | 0.0 |
| 10       | 0.1   | 0.0 |
| 15       | 0.05  | 0.0 |
| 20       | 0.02  | 0.0 |
| 25       | 0.01  | 0.0 |
</details>

E  
![](images/af36672324772eda10dc635c312751b291f0e79bc288ae8f181e8e328fb3ce2a.jpg)

<details>
<summary>line chart</summary>

| Current Density | Peak Intensity |
| --------------- | -------------- |
| 65 µJ           | High           |
| 56 µJ           | Medium         |
| 46 µJ           | Low            |
</details>

F  
![](images/0b175b58d9c878538086b759f9e42b28bab00b864ee6dbc9b595f76ab0f00652.jpg)

<details>
<summary>bar chart</summary>

| Pulse Energy | T (°C) |
| ------------ | ------ |
| 65 µJ        | 1.2    |
| 56 µJ        | 1.0    |
| 46 µJ        | 0.7    |
</details>

FIGURE 4 Comparison of CSFOE and FOC. (A) Schematics of the CSFOE and FOC. (B) Photoacoustic signal of CSFOE and FOC, measured by a 5 MHz transducer under the same laser condition: 1,030 nm, 3 ns, 1.7 kHz, 48 mW. (C) Temperature rise measured by a thermal probe placed at the FOC (Red) under the same laser energy input of 56 µJ. (E) Temperature rise measured by the thermal probe placed at ∼10 µm away from CSFOE under the laser energy used in neuromodulation experiments. Red vertical bars indicate the laser on. Laser condition: 1,030 nm, 1.7 kHz repetition rate, 3 ms duration for each burst. Laser pulse energy is shown in the figure. (F) Measured maximum temperature increases a corresponding pulse energy inputs $( N = 5$ for each energy)

To compare their performance in neuron modulation, CSFOE and FOC were tested in GCaMP6f labeled neuron culture. Under the laser condition of 3 ms pulse train, 56 µJ pulse energy, 1,030 nm, 1.7 kHz repetition rate, successful activation was observed when CSFOE was applied to neurons. The average maximum $\Delta F / F _ { 0 }$ reached over 20%. When FOC was applied under the same laser condition, no obvious activation occurred (Figure 4D). Notably, previous work showed $\mathrm { C a } ^ { 2 + }$ imaging signals indicating successful activation by FOC has been confirmed in Oregon Green labeled neuron culture. GCaMP6f and Oregon Green, as calcium sensors, have different sensitivity upon stimulation. It has been reported that for a single action potential, Oregon Green can generate ∼50% fluorescence change, while GCaMP6f can only generate ∼10% (Palmer et al., 2014; Dana et al., 2019).

To evaluate the average ultrasound intensity during the stimulation, the $\mathrm { I } _ { S P T A }$ and $\operatorname { I } _ { S P P A }$ of the typical CSFOE stimulation of GCaMP6f labeled neurons and FOC stimulation of Oregon Green labeled neurons were calculated according to the equations below.

$$
I _ {S P T A} = \frac {E _ {a}}{A \times T} = \frac {A \times \frac {1}{\rho c} \int P (t) ^ {2} d t}{A \times T} = \frac {\int P (t) ^ {2} d t}{T \rho c}
$$

$$
I _ {S P P A} = \frac {I _ {S P T A}}{D C}
$$

Here $E _ { a }$ is the acoustic energy, A is the cross section area, T is the time for one period (inverse of the repetition rate), ρ is the density of the medium $( 1 , 0 0 0 ~ \mathrm { k g } / \mathrm { m } ^ { 3 }$ used for water), c is the propagation speed of sound (1,480 m/s in water) and DC is the duty cycle of the signal. The repetition rate used in the calculation is 1.7 kHz. Peak-to-peak pressure used for FOC is 0.48 MPa and is 12.4 MPa for CSFOE. CSFOE stimulation has an $\mathrm { I } _ { S P T A }$ of $0 . 1 3 ~ \mathrm { W / c m ^ { 2 } }$ , approximately fifty times larger than the $\mathrm { I } _ { S P T A }$ of $2 . 4 6 \times 1 0 ^ { - 3 } \ \mathrm { W / c m } ^ { 2 }$ for FOC stimulation. Besides, CSFOE has an $\operatorname { I } _ { S P P A }$ of $3 8 8 . 8 \ \mathrm { W } / \mathrm { c m } ^ { 2 }$ , and for FOC, its ISPPA of 0.725 ${ \mathrm { W / c m } } ^ { 2 } .$ . Through the calculation above, both CSFOE and FOC are within the safety limit of ultrasound therapy $( \mathrm { I } _ { \mathit { S P T A } } < 7 2 0 \mathrm { \ m W } / \mathrm { c m } ^ { 2 } )$ (Pasquinelli et al., 2019), which means there will be no significant tissue damage during the stimulation.

A  
![](images/d2aab596edfa807b5802646b88a5a90dba10a103bd69a9672b6d244f18b66fe3.jpg)

<details>
<summary>text_image</summary>

1 X 2 fiber splitter
Site 1
Site 2
Laser
</details>

B  
![](images/1a942cba18f901b8b5da7f4f7c1ba804dee3d6914cf680a7b778f96a17b835aa.jpg)

<details>
<summary>text_image</summary>

Max ΔF/F₀
Site 1
Site 2
200 µm
</details>

c  
![](images/16dd31be15e765c81dde6a337f2eb2bbfdee3c0159eb145e050ea1a813d63f3b.jpg)

<details>
<summary>heatmap</summary>

| Neuron ID | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 |
|---|---|---|---|---|---|---|---|---|
| site1 | 0.00 | 0.00 | 0.00 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 |
| site2 | 0.00 | 0.00 | 0.00 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 |
</details>

D  
![](images/47682b06e66a1b872caae9def5fa602d1d6cff5b6cce547c103a6767169243b9.jpg)

<details>
<summary>line chart</summary>

| Time (s) | site1 | site2 |
| -------- | ----- | ----- |
| 0        | -0.02 | 0.00  |
| 2        | 0.08  | 0.08  |
| 4        | 0.06  | 0.07  |
| 6        | 0.04  | 0.06  |
| 8        | 0.03  | 0.05  |
| 10       | 0.02  | 0.04  |
</details>

FIGURE 5 Dual site neuron stimulation by CSFOE. (A) Schematic of dual site stimulation using two CSFOEs with a fiber splitter. Created with BioRender.com. (B) Map of the max $\triangle F / F _ { 0 }$ image of two sites of neurons stimulated by two CSFOE. (C) Colormaps of fluorescence changes in (Black).

We attribute the difference in the I to the difference in the device frequencies and recording conditions upon stimulation. Specifically, as previously reported the central frequency of FOC is in low-frequency range (∼ 1.5 MHz), while CSFOE generates high frequency ultrasound (12.8 MHz central frequency). The significant difference in ultrasound frequency could lead to different ultrasound intensity required to activate neurons. In addition, in FOC stimulation, Oregon GreenTM 488 BAPTA-1 dextran was used as the calcium sensors, while in CSFOE stimulation we used GCaMP6f. Oregon Green is more sensitive than GCaMP6f in reporting the activation. This difference in sensitivity could lead to different stimulation intensities required for optoacoustic neural stimulation. In short, the different intensity used for stimulation observed in the FOC work and this work could be contributed to different calcium sensors used and the different frequencies of the emitters, collectively.

TABLE 1 Optoacoustic conversion efficiency comparison of different fiber based optoacoustic emitters for neuromodulation.

<table><tr><td></td><td>CSFOE (this work)</td><td>TFOE (Shi et al., 2021)</td><td>FOC (Jiang et al., 2020)</td></tr><tr><td>Energy conversion efficiency (%)</td><td>1.5E-3</td><td>2.28E-6</td><td>3.14E-5</td></tr><tr><td>Optoacoustic conversion efficiency in pressure ( $Pa\ m^{2}/J$ )</td><td>15,600</td><td>130</td><td>1,374</td></tr></table>

Collectively, our result clearly shows that CSFOE has a significantly higher stimulation efficacy and can be more widely used for recording based on different kinds of calcium sensors.

## Dual-site neuron stimulation by candle soot-based fiber optoacoustic emitter

To illustrate the advantage of the high optoacoustic conversion efficiency of CSFOE, we used CSFOE for dualsite neuron stimulation in vitro. A $. \ 1 \ \times \ 2$ fiber splitter was used for splitting the laser energy into two identical paths. The laser pulse energy of each path was measured to be 53 µJ (90 mW for each site, 1.7 kHz repetition rate) (Figure 5A). As shown in Figure 5B, the map of maximum fluorescence changes Max $\Delta F / F _ { 0 }$ clearly shows two groups of neurons, with each centered around a CSFOE, being successfully activated by two CSFOEs with fluorescence increase of around 10% at each site. Each group is confined within an area of ∼200 µm associated with the corresponding CSFOE. The highly localized feature of CSFOE stimulation makes it possible to distinguish different sites of stimulation under the same field of view.

Ca2+ traces from two groups at these two sites are plotted in a heatmap shown in Figure 5C. Representative traces of 14 cells from different sites are plotted in Figure 5D. Neurons in both sites showed significant change in fluorescence after the laser onset. The fluorescence changes at each site all reached over 10%, which shows that both sites are successfully stimulated (Figure 5C). The high optoacoustic conversion efficiency and the highly localized stimulation area open up potentials for multi-site neuron stimulation.

## Conclusion

In this study, we developed a new fiber optoacoustic emitter based on CS for the first time with high optoacoustic conversion efficiency and demonstrated CSFOE neuromodulation with an improved efficacy compared to FOC. Based on these improvements, we demonstrated dual-site neuromodulation through two CSFOE driven by a single laser source.

To obtain the highest optoacoustic pressure, we chose candle soot as the material of the absorber, which is considered as one of the best materials for optoacoustic generation owing to its high optical absorption. In addition, we optimized the layered design of the CSFOE through both simulation and experiment. The optimized CSFOE was able to generate over 15 MPa peak-to-peak pressure. A more detailed comparison of photoacoustic conversion efficiency between CSFOE and other two fiber optoacoustic emitters used in neuromodulation is shown in Table 1.

Through the direct comparison, CSFOE is ∼ 100 times more efficient than TFOE. Besides, CSFOE shows ∼10 times higher conversion efficiency compared with FOC, which is also evident in the results shown in Figure 4B.

Detailed optoacoustic characterization for CSFOE has also been performed, including power-pressure dependence and distance-pressure dependence. The output optoacoustic peak to peak pressure is linearly proportional to the input pulse energy as P = 0.226 ∗ E. The distance-pressure dependence confirmed a highly localized ultrasound field of around 200 µm. Based on the results of optoacoustic characterization, we can precisely control the ultrasound intensity to be delivered to neurons by controlling the energy of the laser as well as the distance between CSFOE and neurons.

Successful CSFOE neuron activation has been demonstrated using Calcium imaging. It was found that under the pulse energy of 56 and 65 µJ, at the repetition rate of 1.7 kHz, over a 3 ms duration, the maximum fluorescence change of the stimulated neurons were 47.4 ± 33.9% to 99.8 ± 23.3%, respectively. These laser conditions correspond to optoacoustic pressure of 8.8 MPa and 12.4 MPa at the peak of frequency of 12.8 MHz for CSFOE.

Taking advantage of its high energy conversion efficiency, we performed the dual-site neuron stimulation using two CSFOEs driven by a single laser, which is not feasible by previous fiber based optoacoustic emitters. Dual-site stimulation has lots of potential applications in animal behavior studies, since complex animal behavior is normally controlled by multiple functiona area in the brain. CSFOE, offering a superior sub-millimeter spatial resolution and high-pressure conversion efficiency, has the potential to modulate more complex animal behavior by controlling multiple target sites in the circuitry.

In summary, this robust and highly efficient optoacoustic converter, with an easy and repeatable fabrication process, offers a new tool for effective neuron stimulation. With an improved efficiency and the ability to perform multi-site stimulation, CSFOE opens up a great potential for complex animal behaviors that needs multiple stimuli at different locations in a programmable manner.

## Data availability statement

The raw data supporting the conclusions of this article will be made available by the authors, upon requests.

## Ethics statement

This animal study was reviewed and approved by the Institutional Animal Care and Use Committee of Boston University.

## Author contributions

GC, LS, J-XC, and CY: drafting and refining the manuscript. GC: conducting of the simulation. GC and LS: conducting of the experiments. LL, J-XC, and CY: critical guidance of the project. RW, YL, ZD, and MH: help with experiments. LL, YL, and MH: critical reading of the manuscript. All authors have read and approved the manuscript.

## Funding

This work was supported by the Brain Initiative R01 NS109794 to J-XC and CY by National Institute of Health, United States.

## Acknowledgments

We thank Y. Tian for help with the neuronal cultures.

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated

## References

Alles, E. J., Noimark, S., Zhang, E., Beard, P. C., and Desjardins, A. E. (2016). Pencil beam all-optical ultrasound imaging. Biomed. Opt. Express 7, 3696–3704. doi: 10.1364/BOE.7.003696  
Baac. H W . Ok. I. G. Lee. T. and Guo. L. I. (2015) Nano-structural characteristics of carbon nanotube-polymer composite films for high-amplitude optoacoustic generation. Nanoscale 7, 14460–14468. doi: 10.1039/c5nr03769g  
Beisteiner, R., Matt, E., Fan, C., Baldysiak, H., Schonfeld, M., Philippi Novak, T . et al (2020) Transcranial pulse stimulation with ultrasound in Alzheimer's disease-a new navigated focal brain therapy. Adv. Sci (Weinh). 7:1902583. doi: 10.1002/advs 201902583  
Biagi, E., Margheri, F., and Menichelli, D. (2001). Efficient laser-ultrasound generation by using heavily absorbing films as targets. IEEE Trans. Ultrason. Ferroelectr. Freq. Control 48, 1669–1680. doi: 10.1109/58.971720  
Bobola, M. S., Chen, L., Ezeokeke, C. K., Olmstead, T. A., Nguyen, C., Sahota, A., et al. (2020). Transcranial focused ultrasound, pulsed at 40 Hz, activates microglia acutely and reduces Abeta load chronically, as demonstrated in vivo. Brain Stimul. 13, 1014–1023. doi: 10.1016/j.brs.2020.03.016  
Boon, P., Vonck, K., De Herdt, V., Van Dycke, A., Goethals, M., Goossens, L., et al. (2007). Deep brain stimulation in patients with refractory temporal lobe epilepsy. Epilepsia 48, 1551–1560.  
Boyden, E. S., Zhang, F., Bamberg, E., Nagel, G., and Deisseroth, K. (2005). Millisecond-timescale, genetically targeted optical control of neural activity. Nat. Neurosci. 8, 1263–1268.  
Brinker, S. T., Preiswerk, F., White, P. J., Mariano, T. Y., Mcdannold, N. J., and Bubrick, E. J. (2020). Focused ultrasound platform for investigating therapeutic neuromodulation across the human hippocampus. Ultrasound Med. Biol. 46, 1270–1274. doi: 10.1016/j.ultrasmedbio.2020.01.007  
Cayce, J. M., Friedman, R. M., Chen, G., Jansen, E. D., Mahadevan-Jansen, A., and Roe, A. W. (2014). Infrared neural stimulation of primary visual cortex in non-human primates. Neuroimage 84, 181–190. doi: 10.1016/j.neuroimage.2013. 08.040  
Chang, W. Y., Huang, W. B., Kim, J., Li, S. B., and Jiang, X. N. (2015). Candle soot nanoparticles-polydimethylsiloxane composites for laser ultrasound transducers. Appl. Phys. Lett. 107:161903. doi: 10.3390/mi11070631  
Chang, W. Y., Zhang, X. A., Kim, J., Huang, W. B., Bagal, A., Chang, C. H., et al. (2018). Evaluation of photoacoustic transduction efficiency of candle soot nanocomposite transmitters. IEEE Trans. Nanotechnol. 17, 985–993.  
Colchester, R. J., Mosse, C. A., Bhachu, D. S., Bear, J. C., Carmalt, C. J., Parkin, I. P., et al. (2014). Laser-generated ultrasound with optical fibres using functionalised carbon nanotube composite coatings. Appl. Phys. Lett. 104:173502  
Dana, H., Sun, Y., Mohar, B., Hulse, B. K., Kerlin, A. M., Hasseman, J. P., et al. (2019). High-performance calcium sensors for imaging activity in neuronal populations and microcompartments. Nat. Methods 16, 649–657. doi: 10.1038/ s41592-019-0435-6  
Davidson, B., Hamani, C., Huang, Y., Jones, R. M., Meng, Y., Giacobbe, P., et al. (2020). Magnetic resonance-guided focused ultrasound capsulotomy for treatment-resistant psychiatric disorders. Oper. Neurosurg (Hagerstown). 19, 741– 749. doi: 10.1093/ons/opaa240

organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389 fnins.2022.1005810/full#supplementary-materia

Huang, W., Chang, W.-Y., Kim, J., Li, S., Huang, S., and Jiang, X. (2016). A novel laser ultrasound transducer using candle soot carbon nanoparticles. IEEE Trans. Nanotechnol. 15, 395–401.

Jiang, Y., Huang, Y. M., Luo, X. Y., Wu, J. Y. Z., Zong, H. N., Shi, L. L., et al. (2021). Neural stimulation in Vitro and In Vivo by photoacoustic nanotransducers. Matter 4, 654–674.

Jiang, Y., Lee, H. J., Lan, L., Tseng, H. A., Yang, C., Man, H. Y., et al. (2020). Optoacoustic brain stimulation at submillimeter spatial precision. Nat. Commun. 11:881. doi: 10.1038/s41467-020-14706-1

Lee, T., and Guo, L. J. (2017). Highly efficient photoacoustic conversion by facilitated heat transfer in ultrathin metal film sandwiched by polymer layers. Adv. Opt. Mater. 5:1600421.

Lee, T., Baac, H. W., Li, Q., and Guo, L. J. (2018). Efficient photoacoustic conversion in optical nanomaterials and composites. Adv. Opt. Mater. 6:1800491.

Li, G., Qiu, W., Zhang, Z., Jiang, Q., Su, M., Cai, R., et al. (2019). Noninvasive ultrasonic neuromodulation in freely moving mice. IEEE Trans. Biomed. Eng. 66, 217–224.

Moon, C., Fan, X., Ha, K., and Kim, D. (2017). Generation of planar blast waves using carbon nanotubes-poly-dimethylsiloxane optoacoustic transducer. Aip Adv. 7:015107.

Noimark, S., Colchester, R. J., Blackburn, B. J., Zhang, E. Z., Alles, E. J., Ourselin, S., et al. (2016). Carbon-Nanotube-PDMS composite coatings on optical fibers fo all-optical ultrasound imaging. Adv. Funct. Mater. 26, 8390–8396.

Palmer, L. M., Shai, A. S., Reeve, J. E., Anderson, H. L., Paulsen, O., and Larkum, M. E. (2014). NMDA spikes enhance action potential generation during sensory input. Nat. Neurosci. 17, 383–390.

Pasquinelli. C. Hanson, L. G. Siebner. H. R . Lee. H. J. and Thielscher. A (2019). Safety of transcranial focused ultrasound stimulation: A systematic review of the state of knowledge from both human and animal studies. Brain Stimul. 12, 1367–1380. doi: 10.1016/j.brs.2019.07.024

Poduval, R. K., Noimark, S., Colchester, R. J., Macdonald, T. J., Parkin, I. P. Desiardins. A E . et al (2017) Optical fiber ultrasound transmitter with electrospun carbon nanotube-polymer composite. Appl. Phys. Lett. 110:223701. doi: 10.1063/1.4984838

Rosa, M. A., and Lisanby, S. H. (2012). Somatic treatments for mood disorders. Neuropsychopharmacology 37, 102116

Shi, L. L., Jiang, Y., Zhang, Y., Lan, L., Huang, Y. M., Cheng, J. X., et al. (2020). A fiber optoacoustic emitter with controlled ultrasound frequency for cell membrane sonoporation at submillimeter spatial resolution. Photoacoustics 20:100208. doi 10.1016/j.pacs.2020.100208

Shi, L., Jiang, Y., Fernandez, F. R., Chen, G., Lan, L., Man, H. Y., et al. optoacoustic emitter. Light Sci. Appl. 10:143. doi: 10.1038/s41377-021-00580-z

Thompson, D., Nagel, J. R., Gasteau, D. B., and Manohar, S. (2022). Laser-induced ultrasound transmitters for large-volume ultrasound tomography. Photoacoustics 25:100312. doi: 10.1016/j.pacs.2021.100312

Tian, Y., Wu, N., Zou, X. T., Felemban, H., Cao, C. Y., and Wang, X. W. (2013). Fiber-optic ultrasound generator using periodic gold nanopores fabricated by a focused ion beam. Opt. Eng. 52:065005.

Wolf, M. P., Salieb-Beugelaar, G. B., and Hunziker, P. (2018). PDMS with designer functionalities-Properties, modifications strategies, and applications. Prog. Polym. Sci. 83, 97–134. doi: 10.1016/j.progpolymsci.2018.0 6.001  
Won Baac, H., Ok, J. G., Park, H. J., Ling, T., Chen, S. L., Hart, A. J., et al. (2010). Carbon nanotube composite optoacoustic transmitters for strong and high frequency ultrasound generation. Appl. Phys. Lett. 97:234104. doi: 10.1063/ 1.3522833  
Wu, N., Sun, K., and Wang, X. W. (2011). Fiber optics photoacoustic generation using gold nanoparticles as target. Sens. Smart Struct. Technol. Civil Mech. Aerosp. Syst. 2011:7981.  
Wu, N., Tian, Y., Zou, X. T., and Wang, X. W. (2013). “Fiber optic photoacoustic ultrasound generator based on gold nanocomposite”,

Nondestructive Characterization for composite materials, aerospace engineering civil infrastructure, and homeland security (San Diego, CA: SPIE), 8694.

Wu, N., Tian, Y., Zou, X. T., Silva, V., Chery, A., and Wang, X. W. (2012). High-efficiency optical ultrasound generation using one-pot synthesized polydimethylsiloxane-gold nanoparticle nanocomposite. J. Opt. Soc. Am. B Opt. Phys. 29, 2016–2020.

Xu, M., and Wang, L. V. (2006). Photoacoustic imaging in biomedicine. Rev. Sci Instrum. 77:041101.

Zhu, X., Lin, J. W., Turnali, A., and Sander, M. Y. (2022). Single infrared ligh pulses induce excitatory and inhibitory neuromodulation. Biomed. Opt. Express 13, 374–388. doi: 10.1364/BOE.444577

Zou, X., Wu, N., Tian, Y., and Wang, X. (2014). Broadband miniature fiber opti ultrasound generator. Opt. Express 22, 18119–18127. doi: 10.1364/OE.22.018119