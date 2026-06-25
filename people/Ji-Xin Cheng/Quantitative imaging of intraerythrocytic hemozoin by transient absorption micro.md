BiomedicalOptics.SPIEDigitalLibrary.org

# Quantitative imaging of intraerythrocytic hemozoin by transient absorption microscopy

Andy J. Chen Kai-Chih Huang Selina Bopp Robert Summers Puting Dong Yimin Huang Cheng Zong Dyann Wirth Ji-Xin Cheng

# Quantitative imaging of intraerythrocytic hemozoin by transient absorption microscopy

Andy J. Chen,a,† Kai-Chih Huang,b,c,† Selina Bopp, d,\* Robert Summers,d Puting Dong,b Yimin Huang,b Cheng Zong,b Dyann Wirth,d and Ji-Xin Chengb,c,e,f,\*

a Purdue University, Department of Biological Sciences, West Lafayette, Indiana, United States

b Boston University, Photonics Center, Boston, Massachusetts, United States

c Boston University, Department of Biomedical Engineering, Boston, Massachusetts, United States

d Harvard T.H. Chan School of Public Health, Boston, Massachusetts, United States e Boston University, Department of Electrical and Computer Engineering, Boston, Massachusetts, United States

f Boston University, Department of Chemistry, Boston, Massachusetts, United States

Abstract. Hemozoin, the heme detoxification end product in malaria parasites during their growth in the red blood cells (RBCs), serves as an important marker for diagnosis and treatment target of malaria disease. However, the current method for hemozoin-targeted drug screening mainly relies on in-vitro β-hematin inhibition assays, which may lead to false-positive events due to under-representation of the real hemozoin crystal. Quantitative in-situ imaging of hemozoin is highly desired for high-throughput screening of antimalarial drugs and for elucidating the mechanisms of antimalarial drugs. We present transient absorption (TA) imaging as a high-speed single-cell analysis platform with chemical selectivity to hemozoin. We first demonstrated that TA microscopy is able to identify β-hematin, the artificial form of hemozoin, from the RBCs. We further utilized time-resolved TA imaging to in situ discern hemozoin from malaria-infected RBCs with optimized imaging conditions. Finally, we quantitatively analyzed the hemozoin amount in RBCs at different infection stages by single-shot TA imaging. These results highlight the potential of TA imaging for efficient antimalarial drug screening and drug mechanism investigation. © The Authors. Published by SPIE under a Creative Commons Attribution 4.0 Unported License. Distribution or reproduction of this work in whole or in part requires full attribution of the original publication, including its DOI. [DOI: 10.1117/1.JBO.25.1.014507]

Keywords: malaria; hemozoin; transient absorption microscopy; label-free imaging; chemical imaging.

Paper 190341SSR received Sep. 25, 2019; accepted for publication Nov. 22, 2019; published online Dec. 17, 2019.

## 1 Introduction

Malaria, which is caused by the infection of Plasmodium species, infects over 200 million people and caused 430,000 deaths worldwide in 2017, according to the World Health Organization.1 Although there have been advances in prevention, fast diagnosis, and improved antimalarial treatment, artemisinin-resistant and multidrug-resistant Plasmodium falciparum strains pose a new threat to public health worldwide. Thus, methods for better understanding the drug mechanisms and efficient screening of innovative antimalarial compounds are highly desired.2,3

During the blood stage of malaria infection, the Plasmodium species utilizes hemoglobin as the main nutrient source.4 The breakdown of hemoglobin releases free heme, which is toxic to the malaria parasite.5 To detoxify free heme, the parasite catalyzes the polymerization of free heme and transforms it into insoluble hemozoin crystal.5 Hemozoin crystal, therefore, serves as the sink for minerals and heme.6 It was reported that small molecular drugs directly or indirectly inhibit the formation of hemozoin crystal and effectively kill malaria parasites.7 In addition, targeting hemozoin formation, which is specific to the parasite, reduces the concern of disrupting host pathways, such as nucleotide and protein synthesis machineries, by other drugs targeting purine and pyrimidine metabolic pathways of Plasmodium. 8 Therefore, screening for chemicals targeting hemozoin formation is important for antimalarial drug development.9,10

Hemozoin-formation-inhibiting antimalarial drug development requires target-based highthroughput screening (HTS) and target pathway validation.9 Currently, the most prominent hemozoin-based HTS is in-vitro β-hematin inhibition assays.9 The β-hematin inhibition assay utilizes β-hematin, a synthetic analog of hemozoin, as a simple, robust, and cost-effective assay to screen antimalarial compounds. There are two main methods for early β-hematin inhibition assays: one is based on the detection of radioactive C14-labeled hematin incorporated into the growing hemozoin crystal by using a scintillation counter.11 This method is sensitive but hazardous and expensive. The other method quantifies β-hematin via infrared light absorption.12 This method does not need radiolabeled hematin but is time consuming. It requires centrifugations and 48 h of sample drying before recording the infrared spectrum, which limits its application for HTS.12,13 After the initial round of in-vitro screening, positive hits are selected. However, not all the positive hits can inhibit hemozoin formation in situ. Therefore, highthroughput in-situ quantitative imaging of both hemozoin and intracellular heme is highly desired to confirm disruption of hemozoin formation as the drug target.

Transient absorption (TA) microscopy is sensitive for mapping endogenous pigments or nonfluorescent molecules in a label-free manner.14 17 TA microscopy utilizes two synchronized pulsed beams, namely the pump and probe beams, to interrogate the excited state molecular dynamics. The pump beam first excites the electrons from ground state to an excited state, which can be detected by the following probe beam at different pump–probe temporal delays. TA microscopy uses time-zero TA intensity or time-resolved TA signal as an image contrast to differentiate chemical species and has been applied in various scientific fields, including material science, biology fields, and translational medicine studies.18 2 2 For biomedical applications, TA imaging is shown to be able to differentiate deoxyhemoglobin and oxyhemoglobin,2 discriminate melanomas,19 and quantify glycated hemoglobin for diabetes diagnosis.24 Moreover, as an absorption-based method, TA is more sensitive to small-sized particles, compared to the scattering-based methods.25 Therefore, we propose using TA microscopy as a quantitative and sensitive single-cell analysis platform to in-situ study intraerythrocytic hemozoin.

We first utilized our lab-built TA microscope to differentiate β-hematin from red blood cells (RBCs). In addition, we demonstrated that TA microscopy is able to in situ differentiate hemozoin crystal from hemoglobin within RBCs. Hemozoin crystal in infected RBCs can be detected as early as the ring stage. Finally, we quantitatively analyzed the size and number of hemozoin at various stages of malaria infection and observed an increase in both the crystal size and crystal number corresponding to the infected RBCs along with a decrease of TA signal from the RBCs. Our proof-of-concept study shows the potential of using a TA microscope for high-throughput in-vitro β-hematin inhibition assays and in-situ antimalarial drug target validation.

## 2 Materials and Methods

## 2.1 β-Hematin Synthesis

β-hematin was synthesized using an acid precipitation method documented previously.26 Specifically, nitrogen gas was constantly pumped into 0.1 M sodium hydroxide for 15 min to deoxygenize the solution. Then 50 mg hemin chloride (Sigma Aldrich 51280) was dissolved in 10 ml deoxygenized sodium hydroxide solution and was kept away from light. About 0.4 ml propionic acid was added drop by drop over a 20-min frame with the solution stirred at 200 rpm. The mixture was annealed for 18 h at 70°C. The amorphous aggregates were removed by washing with 0.1 M sodium bicarbonate alternating with water wash for three times. Then, the sample was washed with high performance liquid chromatography (HPLC) grade methanol (Sigma Aldrich 34860) alternating with water applied three more times. The solid products were dried over phosphorus pentoxide (Sigma Aldrich 431419) overnight to produce β-hematin crystal.

## 2.2 Scanning Electron Microscopy

Scanning electron microscopy (SEM) of β-hematin was performed on a Zeiss Supra 55 VP system. β-hematin crystal suspensions were dispersed in ethanol and later dried on a silicon wafer. The specimen was mounted on aluminum stubs and coated with platinum for SEM imaging at an electron beam voltage of 3 kV and a beam aperture of 30 μm.

## 2.3 Time-Resolved Transient Absorption Microscopy

The setup of a time-resolved TA microscope is shown in Fig. S1 in the Supplementary Material. Our lab-built TA imaging system used a femtosecond pulsed laser (Spectra-Physics Insight) operating at 80 MHz with two synchronized outputs. The pump beam was modulated at ∼2.5 MHz using an acoustic-optical modulator (Isomet 1205-C). The probe beam went through a delay-tuning stage and combined with the pump beam. The combined beams were directed to a 60×, 1.2 numerical aperture (NA) water immersing objective (Olympus UPlanApo/IR). After passing through the specimen, the transmitted probe beam was collected using a 1.4-NA oil condenser (Olympus U-AAC), filtered with a bandpass filter, and detected by a photodiode (Hamamatsu 3994). The modulated TA signal was first amplified by a lab-built resonant circuit and then demodulated by a lock-in amplifier (Zurich Instrument HF2LI) with a time constant set to $7 \ \mu \mathrm { s } .$ . To record the time-resolved TA signal, a delay-tuning stage was applied to tune the temporal delay between the pump pulse and the probe pulse with 66.7 fs per step. The pump probe delay is scanned in a frame-by-frame manner to generate a three-dimensional data cube ( −  − τ). A $. 2 0 0 \times 2 0 0 \times 1 2 0 ( x - y - \tau )$ data cube requires 48 s to acquire with a pixel dwell x y x ytime set to 10 μs. No photodamage was observed for RBC after data acquisition. Data were processed using IMAGEJ and analyzed using ORIGIN software.

## 2.4 Spontaneous Raman Spectroscopy

Spontaneous Raman spectroscopy of synthesized β-hematin was performed on a Horiba confocal Raman microscope (Horiba Scientific, Labram HR Evolution). A continuous wave laser at 785 nm was used for excitation. The laser was focused by a 40× air objective with a laser power of 35 mW on the sample. Each Raman spectral acquisition was accumulated for 10 s. The pinhole size was set to 50 μm to reject the out-of-focus background. A 600-grooves∕mm grating was utilized to disperse the light and generate a Raman spectrum. Crystals of β-hematin were screened through transmission imaging to determine the point of interest for Raman spectroscopy.

## 2.5 P. falciparum Culture and Sample Preparation

P. falciparum 3D7 strain was cultured by standard methods.27 The parasites were kept in cell culture flasks (Corning 430825) containing blood (New York blood center) and Roswell Park Memorial Institute (RPMI) 1640 medium (Thermo Fisher 11875093) supplemented with 28 mM ${ \mathrm { N a H C O } } _ { 3 } ,$ , 25 mM N-2-hydroxyethylpiperazine-N'-2-ethanesulfonic acid (HEPES) buffer solution, 25 μg∕mL gentamicin, and 0.5% AlbuMAX II (Life Technologies 11021-045). The culture flasks were kept in a cell culture incubator at 37°C. Culture medium was changed on a daily basis. P. falciparum 3D7 was diluted about twice per week to keep the parasitemia below 5%. During subculture, P. falciparum culture was synchronized using sorbitol.28 The culture was then maintained as described above. P. falciparum fixation is done by immersing in 100% methanol (Sigma Aldrich 322415) for 4 s.

## 2.6 Spectral Phasor Analysis

Time-resolved TA signals at each pixel were mapped into a two-dimensional (2-D) phasor space with the coordinates and , which are the real and imaginary parts of the time-resolved TA g ssignal after Fourier transformation, respectively.24,29 The coordinates and can be expressed as $\begin{array} { r } { \mathrm { g } ( \omega ) = \int I ( t ) \times \cos ( \omega t ) \mathrm { d } t / \int | I ( t ) | \mathrm { d } t } \end{array}$ , and $\begin{array} { r } { \mathrm { s } ( \omega ) = \int I ( t ) \times \sin ( \omega t ) \mathrm { d } t / \int | I ( t ) | \mathrm { d } t . } \end{array}$ , where is the I t t t I t t I t t t I t t I ttime-resolved TA signal and ω is the given frequency, which is set to 1.0 here. Clusters of hemozoin and RBCs in the phasor plot were separated manually, as shown in Fig. 3(c). Spectral phasor analysis was performed using an IMAGEJ plugin software.30 To quantitatively analyze the TA decay rates of each cluster, the retrieved TA decay curves were approximated by fitting with a biexponential decay function as shown below: $y = \mathrm { A } 1 \times \exp ( - t / \tau _ { 1 } ) + \mathrm { A } 2 \times \exp ( - t / \tau _ { 2 } ) + y 0 .$ , where is the pump–probe delay, A1 is the amplitude, and $\tau _ { i }$ are the decay time constants. The fast decay time constant $\tau _ { 1 }$ iwas fixed at 0.38 ps as the system response time determined by the laser pulse duration. The TA decay rate was retrieved by fitting the slow decay time constant τ . $\tau _ { 2 } .$

## 3 Results

## 3.1 Time-Resolved Transient Absorption Imaging to Differentiate β-Hematin and Heme in Red Blood Cells

TA microscopy is shown to be able to map heme and heme-related products, such as imaging of heme dynamics in Caenorhabditis elegans22 and detection of glycated hemoglobin (HbA1c) in single $\mathrm { R B C s . } ^ { 2 4 }$ Since hemozoin is synthesized from the polymerization of heme dimer,31 we tested whether a time-resolved TA signal can be used to differentiate the artificial hemozoin, β-hematin, from the heme in RBC.

## 3.1.1 Characterization of β-hematin

We synthesized β-hematin from hemin chloride using an acid precipitation protocol.26 SEM confirmed the synthesized β-hematin with the desired flake shape and with a size ranging from 0.5 to $2 . 0 \ \mu \mathrm { m } ,$ , similar to natural hemozoin [Fig. 1(a)].32 Spontaneous Raman scattering spectroscopy was performed to confirm the chemical composition. As shown in Fig. 1(b), the characteristic peak at $7 5 0 ~ \mathrm { c m ^ { - 1 } }$ , which is assigned to the full pyrrole ring breathing modes $\nu _ { 1 5 }$ , indicates the β-hematin structure in the synthesized crystals.33,34 Notably, the peak pattern from 1300 to 1600 $\mathrm { c m } ^ { - 1 }$ resembles the Raman spectrum of hemin [Fig. 1(b)],33 indicating the remnant of hemin. However, the hemin remnant, which is likely in a powder format, did not confuse the experimental result later because individual $\beta \mathrm { \cdot }$ -hematin crystals were mixed with RBCs instead of hemin.

## 3.1.2 Transient absorption signal of β-hematin and its dependence on excitation laser wavelength

Having acquired β-hematin with high quality, we next performed time-resolved TA imaging on the mixture of β-hematin and RBCs. First, we performed a pump and probe wavelength dependence experiment to optimize the TA signal of β-hematin with either a 520∕680 nm or a 680∕520 nm pump/probe combination. From the images at zero pump–probe temporal delay, we observed that β-hematin has substantially higher TA intensity than RBCs in both imaging conditions [Fig. 1(c), top panel]. This observation was consistent with the decay curve generated from the image stacks, in which the intensities of β-hematin were about twice that of the RBCs [Fig. 1(c), bottom panel]. We also noted that β-hematin and RBCs produced very different pump–probe decay curves, which can be used as a spectroscopic contrast. Therefore, we applied spectral phasor analysis to project the TA decay curve from each pixel onto a 2-D phasor domain.29 We observed distinctive distribution patterns of RBCs and β-hematin from the background on the phasor plots (see Fig. S2 in the Supplementary Material). Notably, the β-hematin crystals, originally with weak TA intensities acquired under the 680∕520 nm pump/probe combination, were apparent in the phasor map. We further normalized the retrieved decay curves and compared the decay curve as shown in the bottom panel of Fig. 1(d). We observed that when the pump beam was set to 520 nm, the β-hematin showed distinctively slower decay dynamics, with a decay time constant of $2 . 4 7 \pm 0 . 1 6 \ \mathrm { p s } .$ , than RBCs, with a decay time constant of $0 . 5 2 \pm 0 . 0 1$ ps [Fig. 1(d), bottom left panel). When the pump beam was set to 680 nm, the pump probe decay curve of β-hematin suggests that the signal is mainly contributed from the thermal effect due to the signal insensitivity to the pump–probe decay position, whereas RBCs retained an identical asymmetry TA decay curve [Fig. 1(d), bottom right panel]. In either case, the pump–probe decay patterns could serve as a spectroscopic signature to differentiate β-hematin from RBCs.

(a)  
![](images/764a135848cc70c139864314387b484cceab4053e38dc528b42665ed457c7a96.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of fibrous material with 2 μm scale bar (no text or symbols)
</details>

(b)  
![](images/386cff2aaf0bb9016e606ce28dda8b5d82334da2fe52e1efeef58b6e98087c32.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 0                  | 0                |
| 500                | 50               |
| 1000               | 100              |
| 1500               | 450              |
| 2000               | 580              |
</details>

(c)  
![](images/009cfecc0561803ab30a3ba254288d4c388f704a8934f6e767ed9468a73a85f0.jpg)

<details>
<summary>text_image</summary>

Pump/Probe (nm)
520/680
680/520
</details>

(d)  
![](images/accc5604ffa6aa5ecc0b2104a8cec34a9c2155ce7caf65c5891abf6265f96b1e.jpg)

<details>
<summary>scatterplot</summary>

| Pump/Probe (nm) | Value  |
| --------------- | ------ |
| 520/680         | 520    |
| 680/520         | 680    |
</details>

![](images/85b3b59b246f55cd8c70fa4461fdf5ee9a69196c95200cefc83b2676bb5bdc27.jpg)

<details>
<summary>line chart</summary>

| Delay time (ps) | RBC TA Intensity (a.u.) | β-hematin TA Intensity (a.u.) |
| --------------- | ------------------------ | ----------------------------- |
| 0               | ~0.8                     | ~1.9                          |
| 2               | ~0.3                     | ~0.7                          |
| 4               | ~0.2                     | ~0.5                          |
| 6               | ~0.1                     | ~0.4                          |
</details>

![](images/59036062d1c3d32330e307a0b7189293c5d0776123eb10280d4d7938fc855932.jpg)

<details>
<summary>line chart</summary>

| Delay time (ps) | RBC       | β-hematin |
| --------------- | --------- | --------- |
| 0               | 1.0       | 1.0       |
| 1               | 0.2       | 0.4       |
| 2               | 0.1       | 0.2       |
| 3               | 0.05      | 0.1       |
| 4               | 0.02      | 0.05      |
| 5               | 0.01      | 0.02      |
| 6               | 0.0       | 0.0       |
</details>

![](images/cd7e8a5627154c0ca0743e38ba931c645d09f602451c424b10ba9e73fa775a1a.jpg)

<details>
<summary>line chart</summary>

| Delay time (ps) | RBC       | β-hematin |
| --------------- | --------- | --------- |
| 0               | 1.0       | 0.5       |
| 2               | 0.2       | 0.5       |
| 4               | 0.1       | 0.55      |
| 6               | 0.05      | 0.55      |
</details>

Fig. 1 TA microscopy spectroscopically differentiates β-hematin from hemoglobin in RBCs. (a) SEM image of synthesized β-hematin. (b) Raman spectrum of β-hematin: laser wavelength: 785 nm; laser power: 35 mW on the sample; dwell time: 10 s; objective: 40× air; pinhole size: 50 μm, grating: 600 l∕mm. (c) Time-resolved pump–probe images of β-hematin and RBC mixture. Left panel: pump∕probe  520∕680 nm; right panel: pump∕probe  680∕520 nm; all images are at zero-time delay, dynamic range: 0.25 to 0.73; graphs are the decay curves of the β-hematin and RBCs indicated by the arrows (green and red, respectively); laser power: 10 mW for each beam; pixel dwell time: 10 μs; 60× water objective. (d) Phasor analysis outputs of the images in (c). (c)–(d) Left panel: $\mathsf { p u m p / p r o b e } = 5 2 0 / 6 8 0 \ \mathsf { n m } ;$ right panel: $\mathsf { p u m p / p r o b e } = 6 8 0 / 5 2 0 \mathsf { n r }$ m. (c)–(d) Top panel: retrieved images from phasor analysis (β-hematin is artificially colored green and RBCs in red); bottom panel: graphs are retrieved pump–probe spectra from phasor analysis.

## 3.2 Time-Resolved Transient Absorption Imaging of Hemozoin within Infected Red Blood Cells

## 3.2.1 Transient absorption signal of hemozoin and its dependence on excitation laser wavelength

Having proved that TA signals could separate β-hematin from RBCs, we next tested whether TA imaging could identify natural hemozoin within infected RBCs. We first optimized the hemozoin imaging condition with different pump–probe laser wavelength combinations. The optimization was performed under the constraint of our laser with one tunable beam ranging from 680 to 1300 nm and the other beam fixed at 1040 nm or 520 nm through frequency doubling. Since the absorbance difference of hemozoin and hemoglobin is largest at 680 nm,35 we hypothesize that hemozoin gives a stronger TA signal when pumped at 680 nm compared with that at 520 or

![](images/06cbdfdb16effd47570cd0126d2b21eb2210f52e12403164f9e7e16a5422ed0a.jpg)

<details>
<summary>text_image</summary>

(a)
Pump/probe (nm)
680/1040
680/520
Infected RBC
</details>

![](images/efb83d612a66972eb88542c6bc0123c1d86424ae1da4d6dab0ae005f9509027b.jpg)

<details>
<summary>line chart</summary>

| Pump wavelength (nm) | SNR (a.u.) |
| -------------------- | ---------- |
| 680                  | 310        |
| 700                  | 155        |
| 710                  | 230        |
| 720                  | 225        |
| 730                  | 225        |
| 740                  | 145        |
| 750                  | 135        |
| 760                  | 130        |
| 770                  | 125        |
| 780                  | 130        |
| 790                  | 120        |
| 800                  | 110        |
</details>

Fig. 2 Hemozoin TA signal dependence on excitation laser wavelength. (a) TA images of hemozoin using 680/1040 and 680∕520 nm as the pump/probe wavelengths, respectively. Sample: RBCs infected with P. falciparum 3D7 strain; laser power: 10 mW for each beam; scale bar: $2 5 \mu \mathsf { m } ;$ pixel dwell time: $1 0 \ \mu \mathsf s$ . Left panel: pump $/ \mathsf { p r o b e } = 6 8 0 / 1 0 4 0$ nm; dynamic range: 0.1 to $^ { 1 . 8 ; }$ right panel: pump∕probe  680∕520 nm; dynamic range: 0.1 to 0.7. (b) SNR of TA signal using different pump wavelengths. Sample was a single hemozoin crystal from RBCs infected with P. falciparum 3D7. Probe beam wavelength: 1040 nm; laser power: 10 mW for each beam, pixel dwell time: 10 $\mu \mathbf { S } ;$ SNR was calculated by first determining the intensity difference of a fixed area of hemozoin and an equal area of the RBC, then dividing the intensity difference by the standard deviation of the RBC.

1040 $\mathrm { n m } . ^ { 3 6 }$ Indeed, we found that the 680∕520 nm pump/probe combination obtained a higher signal-to-noise ratio (SNR) than the reversed combination (see Fig. S3 in the Supplementary Material). Later, we optimized the probe wavelength with the pump beam set to 680 nm. From the representative images, 1040-nm probing resulted in higher hemozoin signal normalized with the signals from the RBC [Fig. 2(a)], indicating that 1040 nm is a better probe wavelength. Finally, to confirm that 680 nm was the optimal pump wavelength, we carried out a pump wavelength dependency study. We fixed the probe beam at 1040 nm and compared SNRs generated from pump wavelengths ranging from 680 to 800 nm, with 10 nm increments [Fig. 2(b)]. The result shows that a pump wavelength of 680 nm optimizes the SNR. We conclude that the $6 8 0 / 1 0 4 0$ nm pump/probe combination is the optimal condition for in-situ TA imaging of hemozoin.

## 3.2.2 Time-resolved transient absorption imaging to identify natural hemozoin in 48-h infected red blood cells

With the optimized imaging condition, we then tested whether time-resolved TA imaging is able to differentiate hemozoin from hemoglobin in RBCs infected with late-stage P. falciparum. From the TA images at zero-time pump probe delay, intracellular hemozoin crystal is clearly identified with a higher TA intensity [Fig. 3(a), left panel]. By plotting the pump–probe decay curves from the hemoglobin region of RBCs and hemozoin, which is indicated by the arrow in the left panel of Fig. 3(a), we found both showing TA decay patterns, but hemozoin differed substantially from RBC with around nine times larger TA intensity [Fig. 3(a), right panel]. We further applied phasor analysis to generate maps of hemozoin and RBC based on their TA decay rates [Fig. 3(b), left panel]. In the phasor plot from the uninfected RBCs dataset, we observed only one RBC main group, as shown in the red rectangle of Fig. 3(c). In the phasor plot from infected RBCs, the hemozoin group located lower than the main RBCs group was marked with a green rectangle [Fig. 3(c)]. The retrieved spectra revealed that the hemozoin crystal decayed faster than hemoglobin, with the TA decay time constants of $1 . 2 2 \pm 0 . 1 2$ and $1 . 7 0 \pm 0 . 1 1$ ps, respectively [Fig. 3(b), right panel]. We observed that the hemozoin mapping result is consistent with the higher TA intensity region in the zero-time pump–probe delay TA image [Fig. 3(b), left panel]. Collectively, these data demonstrated that even single-shot TA at zero temporal delay is able to in situ identify hemozoin from RBCs in late stages of malarial infection. In the next section, we used this simplified and faster approach for large area mapping of intracellular hemozoin in different infection stages.

(a)  
![](images/db05d06d77953ba692bd8f93bbb9ba107d8937dee6a1bf47a8f85afee598d0b3.jpg)

<details>
<summary>text_image</summary>

RBC ctrl
Infected RBC
</details>

![](images/f8b4e1a64e9ad4069b590c36002d5797932dfe8c9821d69a1fdccfd479aa4ea0.jpg)

<details>
<summary>line chart</summary>

| Delay time (ps) | Hemozoin | RBC |
| --------------- | -------- | --- |
| -1              | 0.0      | 0.0 |
| 0               | 3.8      | 0.2 |
| 1               | 1.5      | 0.1 |
| 2               | 0.8      | 0.05 |
| 3               | 0.6      | 0.03 |
| 4               | 0.5      | 0.02 |
| 5               | 0.4      | 0.01 |
</details>

(b)  
![](images/d47db038c779cb31dac87af6bedd5d1a12957f385b360f09b5223695fd6e019b.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images comparing RBC ctrl and Infected RBC conditions, showing red-stained cell nuclei with a green fluorescent marker (no text or symbols present)
</details>

![](images/e29660028a322763f29ded603f7219f0188fee21ba4c65cb427499aa886be275.jpg)

<details>
<summary>line chart</summary>

| Delay time (ps) | Hemozoin | RBC |
| --------------- | -------- | --- |
| -1              | 0.0      | 0.0 |
| 0               | 1.0      | 1.0 |
| 1               | 0.4      | 0.6 |
| 2               | 0.2      | 0.3 |
| 3               | 0.1      | 0.15 |
| 4               | 0.05     | 0.08 |
| 5               | 0.02     | 0.05 |
</details>

(c)  
![](images/c0872225583d7f3d5a39ba7dea30ba5219004f84eae4d7a395309a855f49a625.jpg)

<details>
<summary>text_image</summary>

RBC ctrl
Infected RBC
</details>

Fig. 3 Time-resolved TA imaging and phasor analysis differentiates hemozoin from hemoglobin in RBCs. (a) Raw TA images and decay curves of malaria-infected RBCs. Sample: RBCs infected with P. falciparum; pump∕probe  680∕1040 nm; laser power: 10 mW for each beam. Left panel: images at zero-time delay; scale bar: 25 μm; image display range: 0.02 to 0.5; RBC and hemozoin selected for generating decay curves were indicated with arrows. Right panel: raw TA decay curves of RBC and hemozoin; an area of about 100 pixels from both indicated objects were selected to plot the decay curves. The curves were smoothed by averaging among five nearby data points. (b) Mapping result retrieved from phasor analysis of data in (a). Left panel: retrieved images; red: RBC; green: hemozoin; scale bar: 25 μm. Right panel: retrieved decay curves of hemozoin and RBCs; intensity was normalized to 1.0. (c) Phasor plot retrieved from phasor analysis of data in (a). Dots within red box: RBCs; dots within green box: hemozoin.

## 3.3 In Situ Quantitation of Hemozoin within Different Infection Stages of Red Blood Cells

Having demonstrated the capability of a TA microscopy to in situ differentiate hemozoin from hemoglobin, we further explored how early in the malarial infection stage TA imaging could detect hemozoin. To this end, we tightly synchronized parasites (6-h window) and made fixed smears at 0, 12, 24, 36, and 48 h postinfection. We found that in the 0 h of infection, no intracellular hemozoin was detected. Instead, only small individual hemozoin crystals dispersing in the medium were observed [Fig. 4(a), 0 to 6 h]. These extracellular crystals were likely the remnants from the synchronization process.28 We observed intracellular hemozoin crystal for cells after 12 h infection [Fig. 4(a), 2 to 18 h]. As infection proceeded, both crystal size and number increased [Fig. 4(a)]. Notably, contrary to the hemozoin, for which the TA signal increased with infection time, the hemoglobin signal continuously decreased as the infection progressed [Fig. 4(a)]. This observation demonstrates the power of TA imaging to visualize both hemoglobin degradation and hemozoin accumulation over the 48-h lifecycle of P. falciparum.

(a)  
![](images/d49cdf9162d14e29a1be1f28cdbcac360514d74861df29dccccb7b5215246613.jpg)

<details>
<summary>text_image</summary>

0 to 6 h
12 to 18h
24 to 30h
36 to 42h
48 to 54h
</details>

(b)  
![](images/5e2e4196dbc277e9821ee8531bcdb93b4ffec47823da41fdc616ab5f1bfae229.jpg)

<details>
<summary>text_image</summary>

0 to 6 h
12 to 18 h
24 to 30 h
36 to 42 h
48 to 54 h
</details>

(c)  
![](images/40def987e6bfcec7eb4f82960e8561771756a4d27381d4b3c7c4523f8511c628.jpg)

<details>
<summary>bar chart</summary>

| Hour post infection (h) | # of hemozoin per 1000 cells |
| ----------------------- | ---------------------------- |
| 0-6                     | 0                            |
| 12-18                   | 15                           |
| 24-30                   | 17                           |
| 36-42                   | 18                           |
| 48-54                   | 25                           |
</details>

(d)  
![](images/a519791dd299fea6a7f31b1b16f4eedaf87b962aea956d37d2a2184523a9fbd7.jpg)

<details>
<summary>bar chart</summary>

| Hour post infection (h) | Average hemozoin size (µm²) |
| ----------------------- | --------------------------- |
| 0-6                     | 0                           |
| 12-18                   | 2                           |
| 24-30                   | 5                           |
| 36-42                   | 10                          |
| 48-54                   | 10                          |
</details>

Fig. 4 Quantitative analysis of hemozoin in RBCs at different stages of malarial infection. (a) Representative single-shot TA images of infected RBCs. Sample: RBCs infected with P. falciparum 3D7 0, 12, 24, 36, and 48 h after invasion; since individual P. falciparum differs during synchronization and infection process, there is a range of 6 h at the beginning of synchronization, which expands to 12 h starting from 48 h after synchronization. Consequently, the time points were denoted as 0 to 6, 12 to 18, 24 to 30, 36 to 42 and 48 to 54 h; image was taken at zero-time delay; pump/probe: 680∕1040 nm; laser power: 30 mW for each beam; scale bar: 20 μm; pixel dwell time: $1 0 \ \mu \mathsf { s } ;$ (b) $7 \times 7$ large area mapping of samples in (a). Images were artificially colored red; representative hemozoin crystals were indicated by arrows; scale bar: 100 μm; displaying ranges were adjusted to standardize the RBCs: 0 to $6 \mathsf { h } = 0 . 0 3$ to 0.23, 12 to $1 8 \mathsf { h } = 0 . 0 2$ to 0.2, 24 to 30 h = 0.01 to 0.34, 36 to $4 2 ~ \mathsf { h } = 0 . 0 3$ to 0.48, 48 to $5 4 ~ \mathrm { h } = 0 . 0 3$ to 0.23. (c) The graph of the number of hemozoin crystals at different time points after infection; crystal number was normalized to 1000 RBCs. (d) The graph of the size of hemozoin crystal at different time points after infection. Hemozoin crystal size was determined by applying a threshold to filter out RBC background and then the total number of pixels of the hemozoin is converted into square micrometers.

We further performed large area mapping of thousands of RBCs in order to quantitatively analyze the growth of hemozoin in the rarely infected RBCs. With the estimated seeding parasitemia as 0.1%, and at least one hemozoin crystal produced by each parasite, we decided to sample at least 1000 cells to capture the rare event of hemozoin crystal formation in each image. Given that each single frame covers about 25 cells on average, $\mathrm { ~ a ~ } 7 \times 7$ large area mapping covers more than 1000 cells. The 0- to 6-h sample contains fewer than 1000 cells due to low cell density, but this does not affect the quantification result because there was no intracellular hemozoin observed [Fig. 4(b)]. However, 12 h after infection, hemozoin could be detected and quantified [Fig. 4(b)]. Since the number of infected RBCs did change over the next 48 h, the number of hemozoin crystals only increased slightly over the course of infection [Fig. 4(c)]. In contrast, the crystal size increased substantially over time, reflecting the growth of hemozoin in each infected cell during mid-infection and late infection stages [Fig. 4(d)]. After 36 h, the average crystal size reached a plateau. Meanwhile, the number of hemozoin crystals started to increase again at 48 h, indicating the maturation and rupture of the first-generation P. falciparum and the invasion of new RBCs by the second generation [Fig. 4(c)]. These data collectively show the potential of using TA microscopy to quantitate intracellular hemozoin growth in size and number over a full lifecycle of P. falciparum infection.

## 4 Discussion

Because of the emergence and fast evolution of multidrug-resistant malaria strains, efficient and HTS for alternative antimalarial drugs is highly desired.2 Validation of the positive hits and a thorough understanding of drug mechanisms are essential to achieve this goal.9 Here, we demonstrate TA microscopy as a sensitive, label-free, and chemical-selective method that enables in-situ quantitative detection of heme components in the forms of hemozoin crystals and hemoglobin in RBCs. We first synthesized β-hematin crystal and showed that TA imaging is sensitive to detect β-hematin crystal by either TA intensity or time-resolved TA signal. We determined the optimal pump–probe wavelength combination as 680∕1040 nm. In-situ quantitative study of hemozoin and RBCs in different infection stages was demonstrated. TA imaging is found to be able to detect hemozoin as early as after 12 h post infection. The TA signal of hemozoin increased while the signal of hemoglobin decreased as the infection progressed. Thousands of RBCs were screened to quantitatively monitor the change in the size and number of hemozoin in situ over a complete lifecycle of P. falciparum. These proof-of-concept data show the potential of using TA imaging for high-throughput antimalarial drug screening by monitoring hemozoin formation in situ. Our method overcomes the limitation of in-vitro β-hematin inhibition assay in its under-representation of the real hemozoin crystal, which leads to a large number of false positives while missing potential valuable hits.9 Our current system can be further upgraded to an imaging flow cytometry setting by conjugating with a hydrodynamic focusing system to further improve the throughput.

TA microscopy, as a sensitive tool for hemozoin, can be combined with coherent Raman scattering microscopy to monitor drug dynamics in infected RBCs. Visualization of the interaction between drugs and hemozoin will provide valuable insights to elucidate drug mechanisms. For example, it is known that quinoline suppresses P. falciparum by inhibiting hemozoin synthesis. However, the drug mechanism is still in debate as to whether it is through direct sequestration of heme36 or through binding to the growing face of hemozoin.37 Such mysteries can be unveiled by the combination of TA microscopy with coherent Raman scattering microscopy, which is a label-free chemical imaging tool with the capability of imaging small molecules.38,39 Such a multimodal imaging platform is expected to provide critical insights into the working mechanisms of antimalarial drugs.

## Disclosures

The authors declare no conflicts of interest.

## Acknowledgments

This work was supported by R01GM118471 to J. X. C. Author contributions: A. J. C., K. C. H., P. T. D., and J. X. C. designed the project; A. J. C. and K. C. H. performed the experiments; A. J. C. performed the data analysis; A. J. C. and K. C. H. wrote the manuscript; P. T. D. synthesized the β-hematin; Y. M. H. took the SEM images of the β-hematin; C. Z. collected the Raman spectrum of the β-hematin; S. E. B. and R. S. cultured and prepared P. falciparum samples; and D. F. W. provided training on malaria handling to A. J. C. All authors read and approved the manuscript.

## References

1. D. D. Laishram et al., “The complexities of malaria disease manifestations with a focus on asymptomatic malaria,” Malar. J. 11(1), 29 (2012).  
2. C. Wongsrichanalai et al., “Epidemiology of drug-resistant malaria,” Lancet Infect. Dis. 2(4), 209–218 (2002).  
3. R. E. Martin et al., “Chloroquine transport via the malaria parasite’s chloroquine resistance transporter,” Science 325(5948), 1680 1682 (2009).  
4. D. E. Goldberg et al., “Hemoglobin degradation in the malaria parasite : an ordered process in a unique organelle,” PNAS 87(8), 2931–2935 (1990).  
5. T. J. Egan, “Haemozoin formation,” Mol. Biochem. Parasitol. 157(2), 127–136 (2008).  
6. T. J. Egan et al., “Haemozoin (β-haematin) biomineralization occurs by self-assembly near the lipid/water interface,” FEBS Lett. 580(21), 5105–5110 (2006).  
7. A. F. G. Slater and A. Cerami, “Inhibition by chloroquine of a novel haem polymerase enzyme activity in malaria trophozoites,” Nature 355(6356), 167–169 (1992).  
8. M. Belen Cassera et al., “Purine and pyrimidine pathways as targets in ,” Curr. Top. Med. Chem. 11(16), 2103–2115 (2011).  
9. K. Y. Fong and D. W. Wright, “Hemozoin and antimalarial drug discovery,” Future Med. Chem. 5(12), 1437–1450 (2013).  
10. B. L. Tekwani and L. A. Walker, “Targeting the hemozoin synthesis pathway for new anti malarial drug discovery: technologies for in vitro β-hematin formation assay,” Comb. Chem. High Throughput Screen 8(1), 63–79 (2005).  
11. Y. Kurosawa et al., “Hematin polymerization assay as a high-throughput screen for identification of new antimalarial pharmacophores,” Antimicrob. Agents Chemother. 44(10), 2638–2644 (2000).  
12. N. Basilico et al., “A microtitre-based method for measuring the haem polymerization inhibitory activity (HPIA) of antimalarial drugs,” J. Antimicrob. Chemother. 42(1), 55–60 (1998).  
13. T. J. Egan, D. C. Ross, and P. A. Adams, “Quinoline anti-malarial drugs inhibit spontaneous formation of β-haematin (malaria pigment),” FEBS Lett. 352(1), 54–57 (1994).  
14. M. C. Fischer et al., “Invited review article: pump-probe microscopy,” Rev. Sci. Instrum. 87(3), 031101 (2016).  
15. D. Davydova et al., “Transient absorption microscopy: advances in chemical imaging of photoinduced dynamics,” Laser Photonics Rev. 10(1), 62–81 (2016).  
16. L. Wei and W. Min, “Pump-probe optical microscopy for imaging nonfluorescent chromophores,” Anal. Bioanal. Chem. 403(8), 2197–2202 (2012).  
17. P.-T. Dong and J.-X. Cheng, “Pump–probe microscopy: theory, instrumentation, and applications,” http://www.spectroscopyonline.com/pump-probe-microscopy-theory-instrumentationand-applications (accessed September 15, 2019).  
18. D. Fu et al., “Two-color, two-photon, and excited-state absorption microscopy,” J. Biomed. Opt. 12(5), 054004 (2007).  
19. T. E. Matthews et al., “Pump-probe imaging differentiates melanoma from melanocytic nevi,” Sci. Transl. Med. 3(71), 71ra15 (2011).  
20. W. Min et al., “Imaging chromophores with undetectable fluorescence by stimulated emission microscopy,” Nature 461(7267), 1105–1109 (2009).  
21. S. R. Domingue et al., “Transient absorption imaging of hemes with 2-color, independently tunable visible-wavelength ultrafast source,” Biomed. Opt. Express 8(6), 2807–2821 (2017).  
22. A. J. Chen et al., “Label-free imaging of heme dynamics in living organisms by transient absorption microscopy,” Anal. Chem. 90(5), 3395–3401 (2018).  
23. D. Fu et al., “Label-free   optical imaging of microvasculature and oxygenation level,” J. Biomed. Opt. 13(4), 040503 (2008).  
24. P.-T. Dong et al., “Label-free quantitation of glycated hemoglobin in single red blood cells by transient absorption microscopy and phasor analysis,” Sci. Adv. 5(5), eaav0561 (2019).  
25. M. A. van Dijk et al., “Absorption and scattering microscopy of single metal nanoparticles,” Phys. Chem. Chem. Phys. 8(30), 3486–3495 (2006).  
26. U. Tripathy et al., “Optimization of malaria detection based on third harmonic generation imaging of hemozoin,” Anal. Bioanal. Chem. 405(16), 5431–5440 (2013).  
27. W. Trager and J. B. Jensen, “Human malaria parasites in continuous culture,” Science 193(4254), 673–675 (1976).  
28. C. Lambros and J. P. Vanderberg, “Synchronization of   erythrocytic stages in culture,” J. Parasitol. 65(3), 418–420 (1979).  
29. F. E. Robles et al., “Phasor analysis for nonlinear pump-probe microscopy,” Opt. Express 20(15), 17082 17092 (2012).  
30. F. Fereidouni, “Spectral phasor,” version 1.4, http://www.spechron.com/Spectral%20Phasor-Introduction.aspx.  
31. C. D. Fitch and P. Kanjananggulpan, “The state of ferriprotoporphyrin IX in malaria pigment,” J. Biol. Chem. 262(32), 15552–15555 (1987).  
32. N. T. Huy et al., “Alcohols induce beta-hematin formation via the dissociation of aggregated heme and reduction in interfacial tension of the solution,” Acta Trop. 101(2), 130–138 (2007).  
33. C. Tempera et al., “Characterization and optimization of the haemozoin-like crystal (HLC) assay to determine Hz inhibiting effects of anti-malarial compounds,” Malar. J. 14(1), 403 (2015).  
34. G. T. Webster et al., “Resonance Raman spectroscopy can detect structural changes in haemozoin (malaria pigment) following incubation with chloroquine in infected erythrocytes,” FEBS Lett. 582(7), 1087–1092 (2008).  
35. I. Silva et al., “Hemozoin and hemoglobin characterization by optical absorption towards a miniaturized spectrophotometric malaria diagnostic system,” in IEEE 5th Portuguese Meeting Bioeng. (ENBENG), pp. 1–4 (2017).  
36. I. Solomonov et al., “Crystal nucleation, growth, and morphology of the synthetic malaria pigment β-hematin and the effect thereon by quinoline additives: the malaria pigment as a target of various antimalarial drugs,” J. Am. Chem. Soc. 129(17), 5779–5779 (2007).  
37. R. Buller et al., “Quinoline binding site on malaria pigment crystal: a rational pathway for antimalaria drug design,” Cryst. Growth Des. 2(6), 553–562 (2002).  
38. L. Wei et al., “Live-cell imaging of alkyne-tagged small biomolecules by stimulated Raman scattering,” Nat. Methods 11(4), 410–412 (2014).  
39. M. M. Gaschler et al., “Determination of the subcellular localization and mechanism of action of ferrostatins in suppressing ferroptosis,” ACS Chem. Biol. 13(4), 1013–1020 (2018).

Biographies of the authors are not available.