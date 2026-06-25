## SCIENTIFIC REPRTS

OPEN

Received: 9 January 2017

Accepted: 31 March 2017

Published: xx xx xxxx

# Real-time intravascular photoacoustic-ultrasound imaging of lipid-laden plaque in human coronary artery at 16 frames per second

Jie Hui 1, Yingchun Cao2, Yi Zhang1, Ayeeshik Kole2,3, Pu Wang 2, Guangli Yu4, Gregory Eakins5, Michael Sturek2,3, Weibiao Chen4,6 & Ji-Xin Cheng2,7,8

Intravascular photoacoustic-ultrasound (IVPA-US) imaging is an emerging hybrid modality for the detection of lipid-laden plaques, as it provides simultaneous morphological and lipid-specific chemical information of an artery wall. Real-time imaging and display at video-rate speed are critical for clinical utility of the IVPA-US imaging technology. Here, we demonstrate a portable IVPA-US system capable of imaging at up to 25 frames per second in real-time display mode. This unprecedented imaging speed was achieved by concurrent innovations in excitation laser source, rotary joint assembly, 1 mm IVPA-US catheter size, differentiated A-line strategy, and real-time image processing and display algorithms. Spatial resolution, chemical specificity, and capability for imaging highly dynamic objects were evaluated by phantoms to characterize system performance. An imaging speed of 16 frames per second was determined to be adequate to suppress motion artifacts from cardiac pulsation for in vivo applications. The translational capability of this system for the detection of lipid-laden plaques was validated by ex vivo imaging of an atherosclerotic human coronary artery at 16 frames per second, which showed strong correlation to gold-standard histopathology. Thus, this high-speed IVPA-US imaging system presents significant advances in the translational intravascular and other endoscopic applications.

Coronary artery disease remains the leading cause of morbidity and mortality throughout the world. Atherosclerosis, a major form of coronary artery disease, occurs in many different forms and can be distin guished by morphologic classification into different plaque types1 . Among them, the thin-capped fibroatheroma has been understood to be the most “vulnerable” plaque type, as evidence shows it is the most prone to rupture and progress to thrombosis and acute coronary syndrome1–4 . Thin-capped fibroatheromas are grossly defined by hallmarks of a large lipid-rich necrotic core, a thin fibrous cap, and inflammatory infiltrate2, 4 . In addition, these plaques are often structurally non-obstructive to moderately obstructive, thus clinically unidentifiable by routine angiography and stress testing2, 5, 6 . Currently, there are no clinically available imaging tools to reliably and accurately detect vulnerable plaques7–9 . Angiographic techniques, including X-ray angiography, computed tomography angiography, and magnetic resonance angiography, are limited to visualizing areas of severe luminal narrowing. Intravascular ultrasound (IVUS) provides the overall morphology of artery wall for quantification

1Department of Physics and Astronomy, Purdue University, West Lafayette, IN, 47907, USA. 2Weldon School of Biomedical Engineering, Purdue University, West Lafayette, IN, 47907, USA. 3 Department of Cellular and Integrative Physiology, Indiana University School of Medicine, Indianapolis, IN, 46202, USA. 4Nanjing Institute of Advanced Laser Technology, Nanjing, 210038, China. 5 Jonathan Amy Facility for Chemical Instrumentation, Purdue University, West Lafayette, IN, 47907, USA. 6 Shanghai Institute of Optics and Fine Mechanics, Chinese Academy of Sciences, Shanghai, 201800, China. 7 Department of Chemistry, Purdue University, West Lafayette, IN, 47907, USA. 8 Purdue Institute for Inflammation, Immunology, and Infectious Disease, Purdue University, West Lafayette, IN, 47907, USA. Jie Hui, Yingchun Cao, Yi Zhang and Ayeeshik Kole contributed equally to this work. Correspondence and requests for materials should be addressed to J.-X.C. (email: jcheng@purdue.edu)

a  
![](images/8edf4407b0f71faeb36604278260ef4d96800378fcd65a8c7597ebeac64a820b.jpg)

<details>
<summary>text_image</summary>

Labeled photo of a laboratory setup with numbered equipment and a computer monitor displaying two screens
</details>

b  
![](images/c6d41373b9d37fd9f97e63d470e59c41cb90a3f5beb243c43959e79a364ace70.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["1.7 µm MOPA-pumped OPO"] --> B["Multimode fiber"]
  B --> C["Pullback stage assembly"]
  C --> D["Catheter"]
  D --> E["Ultrasound pulser/receiver"]
  E --> F["PA US US"]
  F --> G["Stage control"]
  G --> H["DAQ & PC"]
  H --> I["Trigger"]
  I --> J["Delay & multiplexing unit"]
```
</details>

Figure 1. High-speed real-time IVPA-US imaging system. (a) Image of the portable IVPA-US imaging system. Major components: 1, oscilloscope; 2, fiber-optic rotary joint assembly; 3, IVPA-US catheter; 4, delay generator; 5, ultrasound pulser/receiver; 6, MOPA-pumped OPO; 7, laser controller; 8, mobile cart; 9, laser chiller; 10, PC and DAQ card; 11, image display monitor. (b) Schematic of IVPA-US imaging system layout. Dashed black line: trigger signal; solid black line: stage control cable; solid green line: radiofrequency signal.

of the plaque burden and monitoring disease progression, but lacks chemical selectivity to identify plaque composition. Virtual-histology IVUS, based on radiofrequency (RF) analysis of the ultrasound signal, provides valuable information of the plaque composition10, 11, but still has not been thoroughly validated12, 13. Intravascular near-infrared spectroscopy (NIRS) has been shown to reliably detect lipid-rich plaques in the artery wall14, 15, but lacks imperative depth resolution to quantify the size and location of the lipid deposition. Intravascular optical coherence tomography can accurately detect fibrous cap thickness with micron-scale resolution16, but lacks sufficient imaging depth and chemical selectivity to wholly determine plaque composition. These gaps, along with the increasing prevalence of coronary artery disease, highlight an unmet clinical need for a chemically-selective imaging modality with spatial resolution to advance the detection, understanding, and treatment of lipid-laden vulnerable plaques.

Dual-mode intravascular photoacoustic-ultrasound (IVPA-US) imaging is a promising approach to bridge the aforementioned gaps. In this hybrid modality, IVPA channel maps the lipid-specific chemical composition over the entire artery wall with ultrasonic spatial resolution. Based on conversion of optical absorption into ultrasound signal, photoacoustic (PA) imaging provides chemical selectivity and deep penetration depth17–20. Specifically, the lipid-specific contrast is generated endogenously from the first overtone absorption of C-H bonds at 1.7 µm wavelength21, 22 and the PA signal is one order of magnitude greater than that of water and connective tissues22. Furthermore, IVPA imaging works concurrently with IVUS imaging, which can provide simultaneous morphological information. Therefore, a co-registered IVPA-US image provides complementary information necessary for advanced and quantitative assessment of lipid-laden vulnerable plaques.

The IVPA-US imaging technology is currently under active investigation for the identification of various tissue components21, 23, 24, contrast mechanism21, 22, optical excitation sources25–27, IVPA-US catheter designs27–31, and ex vivo and preclinical validations32–34. However, these works are limited by the use of slow imaging speeds (up to 5 frames per second (fps)27) as well as lack of real-time image display, which are necessary components for future in vivo applications where imaging must be at a sufficient speed to avoid motion artifacts from cardiac pulsation. Motion artifacts can lead to inaccurate spatial mapping and quantification of lipid deposition, and subsequent misinterpretation of plaque type. Furthermore, a lack of real-time processing and display capability would prevent user feedback necessary to adjust imaging parameters and location.

In this work, we overcame these limitations by presenting a portable IVPA-US system capable of imaging in real-time, up to 25 fps. In this system, a master oscillator power amplifier (MOPA)-pumped optical parametric oscillator (OPO) with a wavelength of 1.7 µm and a repetition rate of 2 kHz was used as the optical excitation source. A compact fiber-optic rotary joint provided efficient and stable optical coupling with a scanning speed up to 30 revolutions per second. A 1 mm diameter collinear IVPA-US catheter was built for high-sensitivity imaging. A differentiated A-line strategy, where the triggering frequency for US was doubled to that of PA, was applied to maximize IVPA-US imaging functionality. Lastly, LabView-based algorithms were developed to process and display IVPA-US images in real-time. These developments enabled the 25 fps imaging speed, a 5 times improve ment over any previously reported IVPA-US imaging speed and comparable to the imaging speeds of current commercial IVUS and NIRS-IVUS systems35.

## Results

High-speed real-time IVPA-US imaging system. We designed and developed the compact and porta ble IVPA-US imaging system as shown in Fig. 1(a). The detailed connections and controls of these components were shown in Fig. 1(b). Briefly, in the system, a 1.7 µm, 2 kHz MOPA-pumped OPO was used for high-speed optical excitation. Its output pulses were coupled to a multimode fiber through a coupling mount, then a fiber-optic rotary joint, and lastly the IVPA-US catheter tip. Initial ultrasound pulses generated from an ultrasound pulser were sent to the catheter tip through a slip ring. The delays between the ultrasound and optical pulses were precisely controlled by a delay generator. The B-scan and linear pullback of the catheter was conducted with the fiber-optic rotary joint assembly and rotation and pullback rate controlled by a computer. The sequentially generated PA and US signals were detected by the IVPA-US catheter, transmitted by the slip ring, amplified by the ultrasound receiver, digitized and recorded by a data acquisition (DAQ) card, and further processed and dis played in real-time. This IVPA-US system was capable of imaging in real-time at speed up to 25 fps. The imaging speed was achieved by innovations in several key components, which are presented as below.

a  
![](images/2025fc09dd5b7eb8d4992eeae251736f2798473eb964a8c1fecdac90e96dcf7b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph I
  LD --> CL
  CL --> M1
  M1 --> NdYAG
  NdYAG --> P
  P --> n4["λ/4"]
  n4 --> BBO
  BBO --> M2
  M2 --> OC
  OC --> M4
    end
    subgraph II
  LD --> CL
  CL --> M5
  M5 --> NdYAG
  NdYAG --> L
  L --> M6
  M6 --> Isolator
  Isolator --> M7
  M7 --> M8
  M8 --> Dump
  Dump --> M9
  M9 --> III
  III --> KTP
  KTP --> KTP
  KTP --> M10
  M10 --> M11
  M11 --> M12
  M12 --> W
    end
```
</details>

b  
![](images/db0bf6aef06114f43aaa8b4d1b75f209df74f8672d7983da000b3020c82a83c9.jpg)

<details>
<summary>line chart</summary>

| Wavelength (nm) | Laser output spectrum | PA spectrum of lipid |
| --- | --- | --- |
| 1700 | 0.0 | 0.0 |
| 1710 | 0.0 | 0.2 |
| 1720 | 0.8 | 0.4 |
| 1730 | 0.0 | 0.6 |
| 1740 | 0.0 | 0.8 |
| 1750 | 0.0 | 1.0 |
| 1760 | 0.0 | 1.2 |
| 1770 | 0.0 | 1.4 |
| 1780 | 0.0 | 1.6 |
| 1790 | 0.0 | 1.8 |
| 1800 | 0.0 | 2.0 |
| 1810 | 0.0 | 2.2 |
| 1820 | 0.0 | 2.4 |
| 1830 | 0.0 | 2.6 |
| 1840 | 0.0 | 2.8 |
| 1850 | 0.0 | 3.0 |
| 1860 | 0.0 | 3.2 |
| 1870 | 0.0 | 3.4 |
| 1880 | 0.0 | 3.6 |
| 1890 | 0.0 | 3.8 |
| 1900 | 0.0 | 4.0 |
| 1910 | 0.0 | 4.2 |
| 1920 | 0.0 | 4.4 |
| 1930 | 0.0 | 4.6 |
| 1940 | 0.0 | 4.8 |
| 1950 | 0.0 | 5.0 |
| 1960 | 0.0 | 5.2 |
| 1970 | 0.0 | 5.4 |
| 1980 | 0.0 | 5.6 |
| 1990 | 0.0 | 5.8 |
| 2000 | 0.0 | 6.0 |
| 2010 | 0.0 | 6.2 |
| 2020 | 0.0 | 6.4 |
| 2030 | 0.0 | 6.6 |
| 2040 | 0.0 | 6.8 |
| 2050 | 0.0 | 7.0 |
| 2060 | 0.0 | 7.2 |
| 2070 | 0.0 | 7.4 |
| 2080 | 0.0 | 7.6 |
| 2090 | 0.0 | 7.8 |
| 2100 | 0.0 | 8.0 |
| 2110 | 0.0 | 8.2 |
| 2120 | 0.0 | 8.4 |
| 2130 | 0.0 | 8.6 |
| 2140 | 0.0 | 8.8 |
| 2150 | 0.0 | 9.0 |
| 2160 | 0.0 | 9.2 |
| 2170 | 0.0 | 9.4 |
| 2180 | 0.0 | 9.6 |
| 2190 | 0.0 | 9.8 |
| 2200 | 0.0 | 1.2 |
| Peak (labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (nabeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (nabeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser output spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of lipid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of liquid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of liquid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of liquid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of liquid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of liquid |
| Peak (n labeled) | Laser input spectrum | PA spectrum of liquid |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of lipid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarized) | Laser input spectrum | PA spectrum of liquid (labeled) |
| Peak (polarizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (polarizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser Input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA spectrum of lipid |
| Peak (poralizonal) | Laser input spectrum | PA Spectrum |
| Peak (poralizonal) | Laser input spectrum | PA Spectrum |
| Peak (poralizonal) | Laser input spectrum | PA Spectrum |
| Peak (poralizonal) | Laser input spectrum | PA Spectrum |
| Peak (poralizonal) | Laser input spectrum | PA Spectrum |
| Peak (poralizonal) | Laser input spectrum | PA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LAA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LAA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LAA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LAA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LAA Spectrum |
| Peak (poralizonal) | Laser input spectrum | LAA Spectrum |
| Peak (poralizonal) | LAA Spectrum | LAA Spectrum |
</details>

C

![](images/2bd22343c4804ccdf316917f4e216edea49bf5d708a1854396c51c190d00dca0.jpg)

<details>
<summary>line chart</summary>

| Control current (A) | Output power (W) |
| ------------------- | ---------------- |
| 3.5                 | 0.0              |
| 4.0                 | 0.5              |
| 4.5                 | 1.0              |
| 5.0                 | 1.5              |
| 5.5                 | 1.8              |
| 6.0                 | 2.0              |
| 6.5                 | 2.2              |
</details>

Figure 2. 1.7 µm 2 kHz MOPA-pumped OPO for high-speed optical excitation. (a) Schematic of MOPApumped OPO. Dashed boxes labeled by I, II, and III highlight the master oscillator, optical power amplifier, and OPO, respectively. LD, laser diode; CL, coupling lens; M1 and M5, fold mirror; M2, M10, and M11, flat mirror; M3, M4, M6, M7, M8, M12, and M13, reflective mirror; M9, dichroic mirror; P, polarizer; BBO, beta barium borate Pockels cell; OC, output coupler; L, lens; KTP, potassium titanyl phosphate; W, output window. (b) Output wavelength of the laser (black curve), 1725 nm, matching the maximum peak in photoacoustic spectrum of lipids (blue curve). (c) Output power with control current. Other performance parameters can be found in Supplementary Fig. S1.

The determining factor for imaging speed is the laser pulse repetition rate, as each laser pulse corresponds to a depth-resolved A-line signal. In this system, a custom-built MOPA-pumped OPO was used for 2 kHz optical excitation, with the optical layout detailed in Fig. 2(a). The master oscillator provided 2.5 mJ and 15 ns laser pulses at 1064 nm with a 2 kHz repetition rate. The output was amplified to 6.0 mJ by a laser diode side-pumped optical power amplifier. Its wavelength was further shifted to 1.7 µm by a potassium titanyl phosphate (KTP)-based OPO. The performance of the laser output was further characterized. The final output wavelength was measured to be 1725 nm, which coincides with the first overtone transition frequency of C-H bonds (Fig. 2(b)). Thus, laser pulses at this wavelength were effectively absorbed by C-H bond-rich lipids, which generated strong PA signals. The output power was tunable in a range of 2.1 W, sufficient for lipid excitation (Fig. 2(c)). Other laser performance characterizations were shown in Supplementary Fig. S1. Collectively, this laser source was optimal for high-speed IVPA imaging of lipids.

The catheter used in the system had a collinear IVPA-US design with a diameter of 1mm. Fig. 3(a) showed the actual image of a fully assembled collinear IVPA-US catheter, with the detailed schematic of the catheter imaging window shown in Fig. 3(b). In this design (further details found elsewhere28), the incident optical wave and its generated ultrasound wave were collinearly aligned, providing efficient overlap between the optical and acoustic paths over an imaging depth of >6 mm. In this work, we further miniaturized the catheter diameter to 1 mm, a clinically-compatible size adopted by most commercial IVUS systems. The reduction in diameter was achieved by aligning a miniaturized single element transducer $( 0 . 5 \times 0 . 6 \dot { \times } 0 . 2 \mathrm { m m } ^ { 3 } )$ , a multimode fiber with core diameter of 365 µm, and a reflection rod mirror with diameter of 365 µm in a 3-D printed housing. The beam path and beam characteristics were shown in Supplementary Fig. S2. The inset in Fig. 3(b) showed the actual image of an assembled IVPA-US catheter tip. This catheter provided high-sensitivity IVPA-US imaging capability and its size made access into human coronary artery samples feasible.

The fiber-optic rotary joint assembly is another key element that enabled the high-speed imaging. The assem bly simultaneously provided optical coupling, RF signal transmission, fast rotary scan, and linear pullback. The compact and portable assembly was shown in Fig. 3(c). The rotary motor and the linear stage were used to provide rotary scan and linear pullback of catheter for 3-D imaging. The fiber-optic rotary joint was used to provide sufficient and stable optical coupling at high rotational speeds. The design of fiber-optic rotary joint was shown in Fig. 3(d). In this design, the use of two adjacent collimators and a mating sleeve enabled an overall coupling efficiency of 60% from the initial optical input to the final output at the catheter tip. Furthermore, the design sig nificantly minimized the coupling efficiency variation usually caused by the mechanical rotation to 5.4%. Thus, the artery wall was uniformly excited in laser pulse energy at every angular position. The fiber-optic rotary joint was further driven by the motor with rotational speed up to 30 revolutions per second.

To maximize IVPA-US imaging functionality at high imaging speeds, a differentiated A-line strategy was designed. Fig. 4(a) showed the timing diagram for the A-line strategy. The transistor-transistor logic (TTL) sig nal from the laser was used to trigger DAQ card. The same trigger was delayed and frequency-doubled through multiplexing by a delay generator to trigger initial ultrasound pulses. As a result, the digitized signal in one acquisition cycle contained one PA signal segment and two US signal segments. Thus, the number of A-lines in a cross-sectional IVUS image was two times of that in IVPA image. Specifically, at 16 fps, 125 A-lines were used to reconstruct a cross-sectional IVPA image; 250 A-lines were used to reconstruct a cross-sectional IVUS image, comparable to current commercial systems. In order to verify the use of 125 A-lines in IVPA image, we characterized IVPA lateral resolution by imaging of a single 30 µm diameter carbon fiber submerged in heavy water. The cross-sectional IVPA image at 16 fps was shown in Fig. 4(b) and its lateral resolution of 305 µm was estimated by the full-width-at-half-maximum (FWHM) of the Gaussian fitted curve of the raw data points in the lateral direc tion at an axial position of 2.38 mm (Fig. 4(c)). At this axial position, there were 2.5 A-lines sampled in the lateral resolution of 305 µm, which indicates that signals in IVPA image were adequately sampled in the lateral direction based on the Nyquist sampling theorem (2.5 was calculated by L/(2 \* pi \* R/N), where L is the lateral resolution, N is the number of A-lines per cross-sectional image, and R is the axial position). Using the same methodology, there were constantly \~2.5 A-lines sampled in the lateral resolution at every axial position for 16 fps IVPA imaging (calculated based on the data in Fig. 4(d)). Thus, the use of 125 A-lines should provide adequate image quality for IVPA imaging. Meanwhile, we characterized the lateral resolutions at different axial positions at other imaging speeds (Fig. 4(d)). Notably, when the axial position was increased, the lateral resolution decreased, varying from 150 to 600 µm. However, there was no significant difference in lateral resolution at each axial position at different imaging speeds.

a  
![](images/6fca7df58008c046477b27825918182a9cc3110f231642d2b383a604f5e95a44.jpg)

<details>
<summary>text_image</summary>

FC/PC connector
Flexible torque coil
Electrical connector
IVPA/US catheter tip
</details>

b  
![](images/ed12a7d528ce6d59d923a4c9539d63b1d1c93b76248fe73d0cef1b3f534322fe.jpg)

<details>
<summary>text_image</summary>

IVPA/US catheter tip
Lipid-laden plaque
Torque coil Fiber Electrical wire Housing Transducer Rod mirror
1 mm
</details>

c  
![](images/9da14eac241bb27a9051197b8a1f679a879fb12beede06d99ddc206b52d92831.jpg)

<details>
<summary>text_image</summary>

Linear pullback stage
IVPA/US catheter
Drive belt
Rotary motor
Fiber-optic rotary joint
& slip ring assembly
</details>

d  
![](images/525728f02e480c60e93ba528716763f8adf8f78ff61e25af5c0422182f504f00.jpg)

<details>
<summary>text_image</summary>

Laser coupling
Stator
Bearing
SMA connector
Multimode fiber
SMA connector
Rotor
FC/PC connector
The proximal of
IVPA/US catheter
Electrical wire
SMA connector
SMA collimator
Rotator
Slip ring
Electrical connector
SMA to SMA mating sleeve
</details>

Figure 3. 1-mm high-sensitivity catheter and fiber-optic rotary joint assembly for high-speed IVPA-US imaging. (a) Gross picture of flexible IVPA-US catheter with a 1 cent coin. Proximal end of the catheter was assembled with a FC/PC connector. (b) Schematic of 1-mm collinear IVPA-US catheter design. The red ellipses and black curves highlight the collinear paths of optical pulses and acoustic waves, respectively. Inset shows the actual picture of assembled catheter tip. Ruler scale: 1 mm. (c) Picture of overall fiber-optics rotary joint assembly. (d) Schematic of fiber-optic rotary joint for high-pulse-energy high-repetition-rate laser delivery.

To achieve real-time display of IVPA-US images, we developed fast processing and display algorithms. The processing flow was shown in Supplementary Fig. S3 and the details were in Methods. Briefly, the digitized data containing non-meaningful signals was discarded in a preprocessing loop. The remaining PA and US segments were processed, reconstructed, and displayed in parallel IVPA and IVUS loops. A polar projection module was applied to convert IVPA and IVUS signals into polar images simultaneously. Through this program, we were able to image and display in real-time. (More details about the high-speed real-time IVPA-US imaging system can be found in Methods).

IVPA-US imaging of pulsatile motion at different speeds. To find the optimal speed to image arteries with cardiac motion in in vivo settings, a phantom with pulsatile motion mimicking a human heartbeat was imaged at different speeds: 1, 5, 10, 16, 20, and 25 fps. Heat shrink tubes have a high absorption and can generate strong PA signal in a broad optical spectrum including 1.7 µm. Thus, we used a short heat shrink tube segment with a \~6 mm diameter in a heavy water environment as the phantom. At the time of imaging, the pulsatile motion was generated by mechanically pinching the tube at 1.2 Hz with forceps. The demonstration of real-time IVPA-US imaging of heat shrink tube at 16 fps and 25 fps can be found in Supplementary Video S1 and Supplementary Video S2, respectively. Supplementary Video S3 showed the merged IVPA-US images at speeds of 1, 5, 10, 16, 20, and 25 fps, respectively. In this video, IVPA and IVUS signals from the circumference of the phantom were detected at all imaging speeds. The imaging speed did not affect detection sensitivity and IVPA-US co-registration. However, IVPA-US imaging at speeds of 1 and 5 fps was not able to accurately capture 1.2 Hz pul satile motion. The speed of 10 fps was acceptable, but its slow refresh rate was noticeable. However, there was no observable difference among the speeds of 16, 20, 25 fps in capturing the 1.2 Hz pulsatile motion. Thus, IVPA-US images at low imaging speeds were subject to distortion from motion artifacts. As contrasting examples, four consecutive IVPA-US images at 1 fps (Fig. 5(a)), 5 fps (Fig. 5(b)), 10 fps (Fig. 5(c)), and 16 fps (Fig. 5(d)) were used to demonstrate the distortion. At lower imaging speeds, there was obvious A-line signal mismatch at 6 o’clock, where the first and final A-lines in a cross-sectional image were located (e.g. Frames #2 and #4 in Fig. 5(a), Frames #2 and #3 in Fig. 5(b), Frame #4 in Fig. 5(c)). However, at 16 fps, the mismatch became negligible (Fig. 5(d)). Furthermore, the overall shape of shrink tube at lower speeds was distorted, especially for images at speeds of 1 and 5 fps (e.g. Frames #1—4 in Fig. 5(a), Frames #2 and #3 in Fig. 5(b)); while the distortion was successfully suppressed at 16 fps and its images reflected the real tube cross-sections (Fig. 5(d)). Lastly, at 16 fps, the dynamic change on tube shape from Frame #1 to #4 in Fig. 5(d) was continuous; but, at 1 fps, such continuity was not shown (Fig. 5(a)). Thus, a 16 fps imaging speed should be sufficient to avoid motion artifacts induced by cardiac pulsation for in vivo IVPA-US imaging.

a  
![](images/4004a063a2362a89e5df8af64d0a3946892d28645764a136e2628ddb620ca5a7.jpg)

<details>
<summary>line chart</summary>

| Signal Type   | Time (τ) |
| ------------- | -------- |
| Pulse train   | 0        |
| TTL trigger   | τ₁       |
| US trigger    | τ₂       |
| PA signal     | τ₃       |
| US signal     | τ₀       |
</details>

b  
![](images/071770c8555b1904820d7f30028a3fdb334835075ac4595b0d82114a88c1d535.jpg)

<details>
<summary>text_image</summary>

IVPA
Lateral
x
z → y
</details>

C  
![](images/55300531294474c26be402bf6b0479e23331625505f2e53838d0576178119522.jpg)

<details>
<summary>line chart</summary>

| Lateral position (mm) | Normalized PA amplitude (a.u.) |
| --------------------- | ------------------------------ |
| 0.0                   | 0.0                            |
| 0.2                   | 0.0                            |
| 0.4                   | 0.0                            |
| 0.6                   | 0.3                            |
| 0.8                   | 1.0                            |
| 1.0                   | 0.6                            |
| 1.2                   | 0.1                            |
| 1.4                   | 0.0                            |
| 1.6                   | 0.0                            |
| 1.8                   | 0.0                            |
</details>

d  
![](images/49dad48b693b2dce5db9f6379e604cf690ac04e68df4e7aeb7ba87522a6ac00f.jpg)

<details>
<summary>scatterplot</summary>

| Axial position (mm) | 1 fps | 5 fps | 10 fps | 16 fps |
| ------------------- | ----- | ----- | ------ | ------ |
| 1                   | 120   | 130   | 110    | 170    |
| 2                   | 250   | 230   | 220    | 280    |
| 3                   | 320   | 280   | 370    | 440    |
| 4                   | 450   | 420   | 520    | 600    |
</details>

Figure 4. Differentiated A-line strategy and A-line number verification for IVPA-US imaging at 16 fps. (a) Timing diagram of IVPA-US imaging. τ , 0 µs; τ, 0.126 µs; τ , 8.126 µs; $\tau _ { 3 } ,$ 258.126 µs. TTL trigger refers to the trigger signal from laser. (b) Cross-sectional IVPA image of a single carbon fiber with diameter of 30 µm for spatial resolution characterization. The image shown was reconstructed by raw imaging data without A-line interpolation. Inset shows the zoom-in IVPA image. Scale bar: 1 mm. (c) Lateral plot of the carbon fiber in IVPA image at an axial position of 2.38 mm. The lateral resolution of 305 µm is estimated by the full with at half maximum (FWHM) of Gaussian fitted curve. (d) IVPA lateral resolution at different axial position at imaging speeds of 1, 5, 10, and 16 fps.

IVPA-US imaging of tissue phantom at 16 fps. To test the chemical specificity of our imaging system, we imaged different tissue components, including intramuscular fat, tendon, and muscle tissue, at 16 fps. Intramuscular fat is rich in CH groups and has similar optical absorption at 1.7 µm as intravascular lipids, thus was used to mimic a lipid-laden plaque. Tendons and muscle tissue were used to mimic the medial layer of an artery, which is composed of vascular smooth muscle cells and collagen-rich extracellular matrix. These tissue components were harvested from a swine and dissected into small segments to be embedded into 2.5% agar gel as shown in Fig. 6(a). A central lumen was created in the phantom to insert the imaging catheter and the phantom was submerged in heavy water during the experiment. A 10 mm pullback of the phantom was captured at 16 fps with a pulse energy of 60 µJ (30.69 mJ/cm2 for laser fluence, calculation found in Supplementary Fig. S2) on the sample and a pullback speed of 0.5 mm/s. In the pullback, 320 frames of IVPA and IVUS data were acquired and reconstructed. Supplementary Video S4 showed the entire pullback. Fig. 6(b–d) showed the IVPA, IVUS, and merged images at one selected position, respectively. The image frames were 3-D rendered along the pull back direction (3-D rendering method was shown in Fig. 6(e)), showing the overall spatial distribution of each imaged tissue component (Fig. 6(f–h) and Supplementary Video S5). In the IVPA channel, only intramuscular fat generated signal, with a signal-to-noise ratio of 46.8 (Fig. 6(f)). However, in the IVUS channel, all three tissue components generated similar levels of signal. Thus, these results validated the chemical selectivity of our imaging system, indicating that lipid deposition in an artery can be specifically mapped.

a  
![](images/00e0a113b4f6155d8ad5b0e0f9d419a37c6c75cb57856aad356c214b607ca22e.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing merged IVPA/US signal at 1 fps, with green and red emission patterns on a dark background (no text or symbols)
</details>

![](images/a90e57356b8b29bb6170825634bee886a1d11f1a0c853116cd5af624ed883657.jpg)

<details>
<summary>natural_image</summary>

Circular fluorescent pattern with green and red hues on black background, labeled 'Frame #2' in top-right corner (no other text or symbols)
</details>

![](images/1c59822be14c7e5d129dab9c73ab0953f55e2fa99abe37e515c50c04f0b5b82c.jpg)

<details>
<summary>natural_image</summary>

Circular fluorescent pattern with green center and red outer ring against black background, labeled 'Frame #3' in top-right corner (no other text or symbols)
</details>

![](images/46ba034ba9e2a2becebc4573b02f3380914e3656dc5a81522775f38c7c286923.jpg)

<details>
<summary>natural_image</summary>

Fluorescently labeled circular pattern with green and red hues against black background, no text or symbols present
</details>

b  
![](images/f53bfea15d6a41b6dae95c803647677644117a64c8f69f4031a6232fb8066a9d.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing merged IVPA/US signal at 5 fps, frame #1, with x, y, z axes and concentric rings (no text or symbols)
</details>

![](images/a0b31c52e0c3fe62e662fee4cf42263365843b69e8db0262f076ddee51c972a3.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing spiral-shaped structures with green and red emission, labeled 'Frame #2' in top right corner (no other text or symbols)
</details>

![](images/4a4a6b645db858b4ebf00e6adb0696272d6b0b75805a27fb4db24f3d2f26ca4e.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing a spiral structure with green and red emission, labeled 'Frame #3' in top-right corner (no other text or symbols)
</details>

![](images/01475d9ac7ace2109472cfeaf9ccfb90e74749f74d8c43bcc4e3f700b9c41ef2.jpg)

<details>
<summary>natural_image</summary>

Circular glowing pattern with green and red hues on black background, labeled 'Frame #4' in top-right corner (no other text or symbols)
</details>

c  
![](images/93fbf1274b50f62f3d92bbb9cde13fa02fb9bf6b497627d64b773bb7a1076ca7.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing merged IVPA/US signal at 10 fps, frame #1, with x, y, z axes and green/red emission patterns (no text or symbols)
</details>

![](images/ac21009cf1d9818d952f1186edfdef145336dab69658837ba47362266a5a0830.jpg)

<details>
<summary>natural_image</summary>

Circular glowing pattern with green and red hues on black background, labeled 'Frame #2' in top-right corner (no other text or symbols)
</details>

![](images/6e2ac100fd34e58e1e4e771c1a1952565612366199843e68222d68c4a4de49e1.jpg)

<details>
<summary>natural_image</summary>

Circular pattern with concentric rings and two glowing red-green spots, labeled 'Frame #3' in top-right corner (no other text or symbols)
</details>

![](images/65beec4a3bca946a013ec0d8804945d30dbf9f2516cefe3bcd07abf9cb22d57c.jpg)

<details>
<summary>natural_image</summary>

Circular glowing pattern with concentric rings and a central green core, labeled 'Frame #4' in top-right corner (no other text or symbols)
</details>

d  
![](images/a81e26c7a752b44c8cba28b0e018c065819a40a80be0c9122c062b43579290e1.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing merged IVPA/US signal at 16 fps, with green and red emission patterns on a dark background (no text or symbols)
</details>

![](images/0c3d9c242f99fbd2997b045a16beea6d08616cdfb4def0bfe9db950834eed8a1.jpg)

<details>
<summary>natural_image</summary>

Circular fluorescent pattern with green and red rings on black background, labeled 'Frame #2' in top-right corner (no other text or symbols)
</details>

![](images/1ef62e19108a4df370e1cc0acb4ae09ddf9324b958b06a7ff1d2300516bd5250.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing concentric ring patterns with red and green emission, labeled 'Frame #3' in top-right corner (no other text or symbols)
</details>

![](images/b4c97e49df74101ef140024da84bf8828d5e7084da0704c37a1747ed41fd5346.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing concentric rings with green and red emission, labeled 'Frame #4' in top-right corner (no other text or symbols)
</details>

Figure 5. IVPA-US imaging of pulsatile motion at different speeds. Four consecutive IVPA-US frames selected at speed of (a) 1 fps, (b) 5 fps, (c) 10 fps, and (d) 16 fps highlighting the imaging distortion induced by pulsatile motion at lower imaging speed, while demonstrating the capability to suppress the motion artifacts at 16 fps. Complete comparison of IVPA-US imaging results at different imaging speed (1, 5, 10, 16, 20, and 25 fps) can be found in Supplementary Video S3. The depth field of view is 5.09 mm. Scale bar: 1 mm.

IVPA-US imaging of human coronary atherosclerosis and comparison to histopathology. To further validate the imaging system for the detection of lipid-laden plaques, a diseased human coronary artery was imaged ex vivo. The right coronary artery was dissected from a human heart, collected from a 44-year old male who died of atherosclerotic hypertensive cardiovascular disease (gross image was shown in Fig. 7(a)). The artery sample was pressure-fixed in 10% w/v formalin and immobilized in a Sylgard tray with metal pins and submerged in heavy water as shown in Fig. 7(b). A protective polyimide sheath was used to enclose the IVPA-US catheter except for the imaging window at the catheter tip. The catheter and sheath were inserted to the artery lumen for IVPA-US imaging at 16 fps and with a pulse energy of 80 µJ (40.93 mJ/cm2 for laser fluence) on the sample, which is below the 1.0 J/cm2 ANSI safety standard for skin exposed in 1.7 µm laser36. A positive region of interest was identified based on IVPA, IVUS, and merged images in Fig. 7(c–e), which was further marked with a metal pin as shown in Fig. 7(b). There were two sites of lipid deposition at the 2 and 8 o’clock positions, as recognized by strong signals in the IVPA channel (Fig. 7(c)). There was a noticeable lipid-rich core at the 2 o’clock posi tion, which correlated with luminal encroachment observed in the IVUS channel (Fig. 6(d)). The co-registered IVPA-US image (Fig. 7(e)) suggested that this lipid-rich core was beneath a fibrous cap of the plaque surface shown by signal in the IVUS channel. To validate our imaging results, we performed gold-standard histopathology at the region of interest. Fig. 7(f) provided an overall image of histology. The lumen and artery structure in the histological section correlated with artery morphology as shown in the IVUS channel. Furthermore, the areas between 5 and 9 o’clock was rich in fibrous tissue, correlating with the strong echogenicity observed in the IVUS channel at the same location. Also apparent were two lipid-rich necrotic cores (Fig. 7(g,h)), as identified by the loss of matrix, cholesterol clefts, and macrophage infiltration into the lipid pool with an overlying fibrous cap (200 µm thickness). Based on these histological hallmarks, we identified this plaque as an advanced fibroather oma, which showed strong correlation with our imaging results.

a  
![](images/c600ce57d411fd31dfa02cb792f7cfa5603f8a83974e36073f2845c62a770736.jpg)

<details>
<summary>text_image</summary>

Tissue phantom
F
T
Pullback
M
x
y
z
</details>

b  
![](images/e8f9b37890915916c93a9477b4d89a7bcc43a5096dc59ac2e0265c7daffe0f9d.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-stained cellular structures labeled IVPA and F, with x, y, z axes indicated (no text or symbols beyond labels)
</details>

c  
![](images/06fd1c13d158c769226c15188c8564fe2e153315a27156290ee01ab4daeb4dd1.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing green-labeled cellular structures labeled F, M, and T (no text or symbols beyond labels)
</details>

d  
![](images/24017dc2d75904f5326a885a23c279099eb9c8a47d2ac4bfd07de515711b3b6c.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing merged red and green cellular structures labeled F, M, and T (no text or symbols beyond labels)
</details>

e  
![](images/550b970850b956c7ce2ef6e90381b05d65128a24a13ceb514ae181c33f75cf75.jpg)

<details>
<summary>text_image</summary>

3D rendering
Pullback
Cross-sectional image
z
x
y
</details>

f  
![](images/9b6aa1c21061239faed6898aec0310cb6b4cce42a8df97e822f459df2723c47c.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing a red-stained vascular structure with 3D rendered IVPA label (no text or symbols beyond labels)
</details>

g  
![](images/a31b4475370a3d4438a406daabe8e1b2be70c6a90b37ca9fd7da4c40fbd7cd33.jpg)

<details>
<summary>text_image</summary>

3D rendered IVUS
M
F
T
</details>

h  
![](images/611d6d731f45fbfdf01f581266e334f5a14aa7af436bb4e68675f8c5fcd4b950.jpg)

<details>
<summary>text_image</summary>

3D rendered merged
M
F
T
</details>

Figure 6. IVPA-US imaging of tissue phantom at 16 fps. (a) Picture of tissue phantom. F, intramuscular fat; T, tendon; M, muscle. Cross-sectional (b) IVPA, (c) IVUS, and (d) merged images of the tissue phantom. The scale bar and the coordinates in (b) is also applied to (c,d). (e) 3-D rendering method. 3-D rendered (f) IVPA, (g) IVUS, and (h) merged images of the tissue phantom with a pullback length of 10 mm. The coordinates in (f) is also applied to (g,h). Scale bar: 1 mm.

## Discussion

In summary, we have demonstrated a real-time IVPA-US imaging system for the detection of lipid-laden plaque in a human coronary artery at 16 fps. In this system, we presented several key innovations, including excitation laser source, fiber-optic rotary joint assembly, 1 mm diameter IVPA-US catheter, and real-time image processing and display algorithms. By imaging pulsatile motion at different imaging speeds, 16 fps was determined to be adequate to suppress motion artifacts from cardiac pulsation for future in vivo applications. Using this system, we further imaged and identified a lipid-laden plaque ex vivo in a human coronary artery, which was confirmed by gold-standard histopathology. Collectively, this work offered significant advances towards the clinical translation of IVPA-US imaging technology.

Imaging speed has been a remaining challenge in development of IVPA/US imaging technology, primarily limited by laser pulse repetition rate. In this work, we overcame this obstacle by using a MOPA-pumped OPO with a 2 kHz optical excitation and achieved up to 25 fps imaging speed, making the IVPA-US system comparable to the commercial IVUS and NIRS-IVUS systems. Although a video-rate speed at 30 fps is preferred for in vivo applications, achieving so would potentially be cost-prohibitive during laser sourcing and development. Moreover, our imaging results concluded that 16 fps imaging speed does not suffer from motion artifacts induced by cardiac pulsation. Meanwhile, this speed was achieved without significantly compromising image quality with the reciprocal reduction of number of A-lines per image frame. To further improve the IVPA imaging quality at 16 fps, we can use a number of strategies including slightly increasing the laser repetition rate (but number of A-lines does not necessarily to be the same as that in IVUS channel) or using less A-lines per image frame paired with advanced reconstruction algorithms that exploit speckle differences in PA and US imaging37.

a  
![](images/f9134965be428984429fef37296c5b2352e66c052e0860f5df70d87562ff3c63.jpg)

<details>
<summary>natural_image</summary>

Anatomical specimen of the human heart with visible blood vessels and a ruler for scale (no text or symbols on the specimen itself)
</details>

b  
![](images/acbefc17cdaae813636600cd48f9f18eb79d039ec89a713c1c141aa67f0bd273.jpg)

<details>
<summary>text_image</summary>

IVPA/US catheter in a transparent sheath
Imaged position marked by metal pin
</details>

c  
![](images/ac45dffc498736eeb99b51040dd78e3b341411e59d855bad98a83c693388f7f7.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-stained cellular structures with x, y, z axes labeled (no text or symbols beyond labels)
</details>

d  
![](images/e0062eb89f92489f9c980926f85069efd1b64150a415dde7785f57e153b8f7d4.jpg)

<details>
<summary>natural_image</summary>

Circular green fluorescent pattern on black background, resembling a brain or neural structure (no text or symbols)
</details>

e  
![](images/4577f35bfd867ae943ec012ebde06e7c1047963f9f7da57ddf97db078d810078.jpg)

<details>
<summary>natural_image</summary>

Circular fluorescent pattern with green and red spots on black background, labeled 'Merged' in top-left corner (no other text or symbols)
</details>

![](images/8428b7a1757c9e1b207f6e857bc57f7a2110cc59d7597aaec09e97861522cddc.jpg)

<details>
<summary>text_image</summary>

Movat pentachrome stain
</details>

g  
![](images/67fab2c2ef8a75514f3b3a37d63d4813e4d3b98bd32dcdcacc3a6503c551f485.jpg)

<details>
<summary>text_image</summary>

Lipid-rich
necrotic core
Cholesterol clefts
Fibrous cap with macrophage infiltration
100 µm
</details>

h  
![](images/ec098e63578454992836b94f819f4fdfe6efb10958e5cadceda0423ebc0abecb.jpg)

<details>
<summary>text_image</summary>

Lipid-rich
necrotic core
</details>

Figure 7. IVPA-US imaging of human coronary atherosclerosis at 16 fps with comparison to histopathology. (a) Picture of collected human heart. (b) Scenario picture of ex vivo IVPA-US imaging of dissected human coronary artery. The region of interest was marked by metal pin. The catheter and sheath were inserted into the artery lumen. Cross-sectional (c) IVPA, (d) IVUS, and (e) merged images of human coronary artery at the region of interest. (f) Gold-standard histopathology stained with Movat’s pentachrome at the region of interest. (g,h) Magnified images of lipid deposition sites corresponding to the dashed boxes in (f). \*Indicates the accumulation of cholesterol clefts.

Real-time imaging capability is also a critical feature for clinical translation of the IVPA-US technology. It can provide operator the necessary and timely feedback to adjust imaging parameters based on their operational requirements. These include the laser pulse energy, the amplification of signals, the pullback speeds, and the image processing parameters. Moreover, the real-time imaging allows to accurately locate the catheter tip at the time of imaging and instantly revisit an identified region of interest. The high-speed real-time imaging capability, along with the superior chemical selectivity and high scalability of PA imaging, makes the imaging system versatile for other intravascular and endoscopy applications. By using a different excitation wavelength or multiple wavelengths, our system could be used to detect other plaque components, e.g. intraplaque hemorrhage or loss of collagen in the fibrous cap. Furthermore, exogenous contrast agents could be employed to target other markers of plaque vulnerability such as macrophage infiltration or matrix metalloproteinases38–40. Our system may also resolve the current limitations (slow imaging speed, 4 Hz; partial field of view) encountered in PA endoscopy of gastrointestinal tracts41.

Our system is currently limited by the lack of an optically and acoustically transparent sheath fully enclosing the IVPA-US imaging catheter. A sheath is a necessary component in a clinical setting to protect the catheter components and the artery endothelium. In addition, the sheath must be flexible and have a clinically compatible size. Lastly, a clinically relevant animal model of atherosclerosis will be critical in refining the catheter and the sheath designs and preclinical validation of the technology in vivo.

## Methods

MOPA-pumped OPO. The detailed optical layout of the laser was shown in Fig. 2(a). In the MOPA configu ration, a Nd:YAG laser side-pumped by a laser diode was used as the master oscillator, generating 2.5 mJ and 15 ns laser pulses at a frequency of 2 kHz and a wavelength of 1064 nm. The output of the laser diode was collimated onto the Nd:YAG crystal through a pair of coupling lenses. A BBO Pockels cell was used as the electro-optical Q-switch along with a polarizer and a quarter-wave plate. A Nd:YAG rod side-pumped by a collimated laser diode was applied as the power amplifier. After the amplification, the pulse energy reached 6.0 mJ at a wavelength of 1064 nm and a pulse duration of 15 ns. The wavelength of the laser pulses was shifted to 1.7 µm as the final output by a KTP-based OPO. In the OPO cavity, two KTP crystals were specially cut to realize the type II phase matching and placed with opposite orientation to effectively reduce the walk-off effect. The temperature of the laser rods and the KTP crystals were kept at 295 K for effective heat dissipation. All optical components were installed and enclosed in a compatible aluminum alloy box with dimensions of $1 0 7 \times 2 6 \mathrm { { \bar { 0 } } \times 4 3 0 \mathrm { { m i \bar { m } } ^ { 3 } } }$ . The performance of the laser output was further characterized as shown in Fig. 2(b,c) and Supplementary Fig. S1.

IVPA-US catheter. We designed and assembled a new 1 mm catheter for simultaneous IVPA and IVUS imaging. The detailed design was shown in Fig. 3(a,b). In the catheter, a multimode fiber (FG365LEC, Thorlabs) was used to guide the optical beam. The proximal end of the fiber was polished to 90° and assembled with a FC/ PC connector for light coupling. The distal end was polished to 47° to realize the collinear overlap between the optical and acoustic paths (Supplementary Fig. S2), considering the small difference in refraction index between the fiber core (1.44) and water or heavy water (1.33). A single element ultrasound transducer (center frequency, 40 MHz; bandwidth, 52%; size, 0.5 × 0.6 × 0.2 mm3 ; Blatek Inc.) was used to receive generated PA and US signals sequentially. A 45° rod mirror (made from the same fiber, polished to 45° and coated with gold, with an optical reflection of 99% and a damage threshold of 1 J/cm2 ) was used to reflect both optical and acoustic waves. The catheter housing (Proto Labs Inc.) was 3-D printed with micro-resolution stereolithography process to enclose and align the relative positions of fiber distal end, rod mirror, and ultrasound transducer. The fabrication was completed on a workstation capable of aligning these components precisely and monitoring the PA and US signals in real-time under aqueous environment.

Data acquisition, image processing and display algorithm. In order to process and display IVPA-US images in real-time, we developed LabView-based algorithms and an intuitive graphical user-friendly interface. First, we used a differentiated A-line strategy for IVPA and IVUS imaging by doubling the US triggering frequency (Fig. 4(a)). Specifically, the TTL signal from the laser was used to trigger data acquisition. The same signal was also used to generate two delayed TTL signals (one channel was delayed for 8 µs and the other for 258 µs) through a delay generator (9512+, Quantum Composer). The two channels were further multiplexed for triggering ultrasound pulser/receiver. Thus, the signal recorded in each acquisition cycle contained one PA signal segment, two US signal segments, and the remaining non-meaningful signal. The signal was then processed by developed image processing and display algorithms (the processing flow shown in Supplementary Fig. S3). Finally, the IVPA and IVUS images were displayed separately on screen in real-time. Using the same methodology as that in 16 fps imaging, we achieved 10, 20, and 25 fps real-time image processing and display. In 10 fps IVPA-US imaging, 200 and 400 raw A-lines were used to reconstruct cross-sectional IVPA and IVUS images, respectively. Similarly, for 20 fps, 100 and 200 raw A-lines for IVPA and IVUS images; for 25 fps, 80 and 160 raw A-lines for IVPA and IVUS images. For 1 and 5 fps, the US triggering frequency was the same as PA, thus IVPA and IVUS images had the same number of A-lines. For 1 fps, IVPA and IVUS images both had 2000 raw A-lines. For 5 fps, both images had 400 raw A-lines. For off-line image reconstruction, an additional median filter was used to reduce noise in both IVPA and IVUS images. An A-line interpolation method was further implemented into the reconstruction algorithm smoothing both IVPA and IVUS images. This was a method that applied inter polation for raw data points along the lateral direction, through which the discontinuity between raw A-lines can be smoothed.

IVPA-US imaging system. The portable IVPA-US imaging system was shown in Fig. 1(a,b). In the system, the laser output was coupled to a multimode fiber (FG365LEC, Thorlabs) through a fiber coupling mount (Supplementary Fig. S4). A designed fiber-optic rotary joint (Fig. 3(c,d)) delivered the laser beam to the IVPA-US catheter tip sequentially through the following optical parts: SMA collimator (F220SMA-C, Thorlabs) for beam collimation, a second SMA collimator (F220SMA-C, Thorlabs) used for coupling the beam into a terminated fiber end, a SMA-to-SMA mating sleeve (ADASMA, Thorlabs) used to properly align the cores of the each terminated fiber end and minimize back reflection. Each terminated fiber end was assembled with a SMA connector. The second collimator, the short fiber segment, and the mating sleeve were fixed in place and enclosed by a metal rotor. Three bearings were assembled onto the proximal end of the rotor and then installed into a stator; while the first collimator was fixed in place into the other end of the stator. The rotator drove the rotor and the optical components in the rotor at a set speed. A step motor (X-NMS17C-E01, Zaber) was used to drive the rotator through a belt for cross-sectional scanning; a linear stage (X-LRM100A, Zaber) was integrated for pullback. The speeds of rotational scanning and linear pullback were controlled by a computer. The optical pulses and initial ultrasound pulses were sequentially sent to the IVPA-US catheter through the multimode fiber and the electric wire of the ultrasound transducer, respectively, to generate IVPA and IVUS signals. The detected signal was transmitted through a slip ring. Electronic noise induced by the assembly was suppressed by electrical grounding and shielding. The signal was received and amplified (39 dB) by an ultrasound receiver (5073PR, Olympus, Inc.), digitized and acquired by a DAQ card (ATS9350 PCI express digitizer, AlazarTech) with waveform digitization of 12-bit, sampling rate of 500 MS/s, and data throughput of 1600 MB/s. The digitized data was processed and displayed in real-time by the computer. The laser chiller used was a non-compressor based chiller. This robust, compact, and portable design is essential for future work in catheterization labs for preclinical and clinical studies.

Human artery samples and histology. Human specimens were obtained within 24 hours of death from deceased patients bequeathed to Indiana University School of Medicine, as approved by Institutional Review Board exemption. The studied donor sample was from a 44-year old Caucasian male with a body mass index of 32.4, past medical history of a previous myocardial infarction, smoking and alcohol use, and hypertension, and died from atherosclerotic hypertensive cardiovascular disease. The right coronary artery was excised from sur rounding bulk myocardium. Small side branches were ligated with ligation clips to allow for pressure-perfusion and the proximal portion of the artery was cannulated using a modified 6 F hemostatic introducer sheath. To maintain the vessel morphology, we pressure-fixed the artery using 10% w/v formalin with a large barrel syringe (140 mL Monoject, Covidien) for 20 minutes at 225 mL/min, which approximately translated to a physiologic pressure. The artery was left in formalin overnight to ensure fixation. We imaged the vessel by first submerging and perfusing it with room temperature 1X PBS, pH 7.4 to remove all air. Next, we inserted the IVPA/US catheter, partially enclosed with a polyimide sheath, through the hemostatic introducer sheath and advanced it distally to a point of resistance (from tortuous anatomy). We completed a pullback of the entire artery length at a pullback rate of 0.2 mm/s and 1 fps imaging speed. After we identified a positive region of interest (an area with strong signal from the IVPA channel), we repeated imaging at 16 fps. We identified and marked the catheter tip location in the vessel at our imaged region of interest by using a metal pin that was strongly echogenic on IVUS. This region was grossly segmented into a \~2.5 mm section and further sectioned at multiple 250 µm levels and stained with Russell-Movat’s pentachrome.

Ethics statement. All the experiment protocols in this study were approved by the Institutional Biosafety Committee of Purdue University, and in accordance with the approval guidelines. The experiments involving human artery samples were approved by Human Research Protection Program of Purdue University, and the informed consent was obtained from all subjects.

## References

1. Yahagi, K. et al. Pathophysiology of native coronary, vein graft, and in-stent atherosclerosis. Nat Rev Cardiol 13, 79–98, doi:10.1038/ nrcardio.2015.164 (2016).  
2. Narula, J. et al. Histopathologic characteristics of atherosclerotic coronary disease and implications of the findings for the invasive and noninvasive detection of vulnerable plaques. J Am Coll Cardiol 61, 1041–1051, doi:10.1016/j.jacc.2012.10.054 (2013).  
3. Virmani, R., Kolodgie, F. D., Burke, A. P., Farb, A. & Schwartz, S. M. Lessons from sudden coronary death: a comprehensive morphological classification scheme for atherosclerotic lesions. Arterioscler Thromb Vasc Biol 20, 12621275, doi:10.1161/01 ATV.20.5,1262 (2000).  
4. Finn, A. V., Nakano, M., Narula, J., Kolodgie, F. D. & Virmani, R. Concept of vulnerable/unstable plaque. Arterioscler Thromb Vasc Biol 30, 1282–1292, doi:10.1161/ATVBAHA.108.179739 (2010).  
5. Schoenhagen, P., Ziada, K. M., Vince, D. G., Nissen, S. E. & Tuzcu, E. M. Arterial remodeling and coronary artery disease: the concept of “dilated” versus “obstructive” coronary atherosclerosis. J Am Coll Cardiol 38, 297–306, doi:10.1016/S0735-1097(01)01374- 2 (2001).  
6. Takano, M. et al. Mechanical and structural characteristics of vulnerable plaques: analysis by coronary angioscopy and intravascular ultrasound. J Am Coll Cardiol 38, 99–104, doi:10.1016/S0735-1097(01)01315-8 (2001).  
7. Puri, R., Tuzcu, E. M., Nissen, S. E. & Nicholls, S. J. Exploring coronary atherosclerosis with intravascular imaging. Int J Cardiol 168, 670–679, doi:10.1016/j.ijcard.2013.03.024 (2013).  
8. Mintz, G. S. Clinical utility of intravascular imaging and physiology in coronary artery disease. J Am Coll Cardiol 64, 207–222, doi:10.1016/ijacc.2014.01.015 (2014)  
9. Sanidas, E. & Dangas, G. Evolution of intravascular assessment of coronary anatomy and physiology: from ultrasound imaging to optical and flow assessment. Eur J Clin Invest 43, 996–1008, doi:10.1111/eci.2013.43.issue-9 (2013).  
10. Kubo, T. et al. The dynamic nature of coronary artery lesion morphology assessed by serial virtual histology intravascular ultrasound tissue characterization. J Am Coll Cardiol 55, 1590–1597, doi:10.1016/j.jacc.2009.07.078 (2010).  
11. Stone, G. W. et al. A prospective natural-history study of coronary atherosclerosis. N Engl I Med 364, 226-235, doi:10.1056 NEJMoa1002358 (2011).  
12. Tuzcu, E. M. & Weissman, N. J. Imaging coronary artery histology: a virtual pursuit? Circ Cardiovasc Imaging 3, 348–350, doi:10.1161/CIRCIMAGING.110.957894(2010)  
13. Thim, T. et al. Unreliable assessment of necrotic core by virtual histology intravascular ultrasound in porcine coronary artery disease. Circ Cardiovasc Imaging 3, 384–391, doi:10.1161/CIRCIMAGING.109.919357 (2010).  
14. Brugaletta, S. et al. NIRS and IVUS for characterization of atherosclerosis in patients undergoing coronary angiography. JACC Cardiovasc Imaging 4, 647–655, doi:10.1016/j.jcmg.2011.03.013 (2011).  
15. Caplan, J. D., Waxman, S., Nesto, R. W. & Muller, J. E. Near-infrared spectroscopy for the detection of vulnerable coronary artery plaques. J Am Coll Cardiol 47, C92–96, doi:10.1016/j.jacc.2005.12.045 (2006).  
16. Jang, I. K. et al. In vivo characterization of coronary atherosclerotic plaque by use of optical coherence tomography. Circulation 111, 1551–1555, doi:10.1161/01.CIR.0000159354.43778.69 (2005).  
17. Wang, L. V. & Hu, S. Photoacoustic tomography: in vivo imaging from organelles to organs. Science 335, 1458–1462, doi:10.1126/ science.1216210 (2012).  
18. Wang, L. V. & Yao, J. A practical guide to photoacoustic tomography in the life sciences. Nat Methods 13, 627–638, doi:10.1038/ nmeth.3925 (2016).  
19. Ntziachristos, V. Going deeper than microscopy: the optical imaging frontier in biology. Nature Methods 7, 603–614, doi:10.1038/ nmeth.1483 (2010).  
20. Beard, P. Biomedical photoacoustic imaging. Interface Focus 1, 602–631, doi:10.1098/rsfs.2011.0028 (2011).  
21. Wang, H. W. et al. Label-free bond-selective imaging by listening to vibrationally excited molecules. Phys Rev Lett 106, 238106, doi:10.1103/PhysRevLett.106.238106 (2011).  
22. Hui, J. et al. Bond-selective photoacoustic imaging by converting molecular vibration into acoustic waves. Photoacoustics 4, 11–21, doi:10.1016/j.pacs.2016.01.002 (2016).  
23. Allen, T. J., Hall, A., Dhillon, A. P., Owen, J. S. & Beard, P. C. Spectroscopic photoacoustic imaging of lipid-rich plaques in the human aorta in the 740 to 1400 nm wavelength range. J Biomed Opt 17, 061209, doi:10.1117/1.JBO.17.6.061209 (2012).  
24. Wang, B. et al. Detection of lipid in atherosclerotic vessels using ultrasound-guided spectroscopic intravascular photoacoustic imaging. Opt Express 18, 4889–4897, doi:10.1364/OE.18.004889 (2010).  
25. Hui, J. et al. High-speed intravascular photoacoustic imaging at 1.7 mum with a KTP-based OPO. Biomed Opt Express 6, 4557–4566, doi:10.1364/BOE.6.004557 (2015).  
26. Wang, P. et al. High-speed intravascular photoacoustic imaging of lipid-laden atherosclerotic plaque enabled by a 2-kHz barium nitrite raman laser. Sci Rep 4, 6889, doi:10.1038/srep06889 (2014).  
27. Li, Y. et al. High-speed intravascular spectroscopic photoacoustic imaging at 1000 A-lines per second with a 0.9-mm diameter catheter. J Biomed Opt 20, 065006, doi:10.1117/1.JBO.20.6.065006 (2015).  
28. Cao, Y. et al. High-sensitivity intravascular photoacoustic imaging of lipid-laden plaque with a collinear catheter design. Sci Rep 6, 25236, doi:10.1038/srep25236 (2016).  
29. Karpiouk, A. B., Wang, B. & Emelianov, S. Y. Development of a catheter for combined intravascular ultrasound and photoacoustic imaging. Rev Sci Instrum 81, 014901, doi:10.1063/1.3274197 (2010).  
30. Bai, X. et al. Intravascular optical-resolution photoacoustic tomography with a 1.1 mm diameter catheter. PLoS One 9, e92463, doi:10.1371/journal.pone.0092463 (2014).  
31. Ji, X., Xiong, K., Yang, S. & Xing, D. Intravascular confocal photoacoustic endoscope with dual-element ultrasonic transducer. Opt Express 23, 9130–9136, doi:10.1364/OE.23.009130 (2015).  
32. Jansen, K., van der Steen, A. F., van Beusekom, H. M., Oosterhuis, J. W. & van Soest, G. Intravascular photoacoustic imaging of human coronary atherosclerosis. Opt Lett 36, 597–599, doi:10.1364/OL.36.000597 (2011).  
33. Wang, B. et al. In vivo intravascular ultrasound-guided photoacoustic imaging of lipid in plaques using an animal model of atherosclerosis. Ultrasound Med Biol 38, 2098–2103, doi:10.1016/j.ultrasmedbio.2012.08.006 (2012).  
34. Zhang, J., Yang, S., Ji, X., Zhou, Q. & Xing, D. Characterization of lipid-rich aortic plaques by intravascular photoacoustic tomography: ex vivo and in vivo validation in a rabbit atherosclerosis model with histologic correlation. J Am Coll Cardiol 64, 385–390, doi:10.1016/j.jacc.2014.04.053 (2014).  
35. Danek, B. A. et al. Experience with the Multimodality Near-Infrared Spectroscopy/Intravascular Ultrasound Coronary Imaging System: Principles, Clinical Experience, and Ongoing Studies. Curr Cardiovasc Imag 9 (2016).  
36. American National Standard for Safe Use of Lasers, ANSI Z136.1 (Laser Institute of America, 2014).  
37. Guo, Z., Li, L. & Wang, L. V. On the speckle-free nature of photoacoustic tomography. Med Phys 36, 4084–4088, doi:10.1118/1.3187231 (2009).  
38. Keswani, R. K. et al. Repositioning Clofazimine as a Macrophage-Targeting Photoacoustic Contrast Agent. Sci Rep 6, 23528, doi:10.1038/srep23528 (2016).  
39. Wang, B. et al. Plasmonic intravascular photoacoustic imaging for detection of macrophages in atherosclerotic plaques. Nano Lett 9, 2212–2217, doi:10.1021/nl801852e (2009).  
40. Qin, H. et al. Inflammation-targeted gold nanorods for intravascular photoacoustic imaging detection of matrix metalloproteinase-2 (MMP2) in atherosclerotic plaques. Nanomedicine: Nanotechnology, Biology, and Medicine 12, 1765–1774, doi:10.1016/j. nano.2016.02.016 (2016).  
41. Yang, J. M. et al. Simultaneous functional photoacoustic and ultrasonic endoscopy of internal organs in vivo. Nat Med 18, 12971302 doi:10.1038/nm.2823 (2012).

## Acknowledgements

The authors thank Randy Replogle at Jonathan Amy Facility for part machining, Dr. Delong Zhang of Purdue University for helpful discussion, and Pu-Ting Dong of Purdue University for phantom preparation. Y.C. acknowledges AHA Postdoctoral Fellowship for financial support. A.K. acknowledges IUPUI Graduate Student Imaging Research Fellowship for financial support. This work was supported by R01HL125385 to J.-X. Cheng and M. Sturek.

## Author Contributions

J.H., Y.C., Y.Z., A.K. contributed equally to this work. J.H. designed and built the high-speed IVPA-US system. J.H., Y.Z. performed the experiment and analyzed the data. Y.C. assembled the catheter. Y.Z., J.H. developed the image processing and display program. Y.C., J.H. built the rotary joint. A.K. provided the artery sample and performed the histology. P.W. provided suggestions and discussion. G.E. helped on the program development. W.C., G.Y. contributed to the construction of the laser. A.K., M.S. provided the comments on the physiology. J.-X.C., M.S. provided overall guidance of the project. J.H. wrote the manuscript. All authors contributed to the editing and approval of the manuscript.

## Additional Information

Supplementary information accompanies this paper at doi:10.1038/s41598-017-01649-9

Competing Interests: J.-X.C. and P.W. have a financial interest in Vibronix Inc., which does not support this work.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/a714d443b83c49fbe3d16548067b931f3099acf1678fd8b92552dbf9402a316f.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or

format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Cre ative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2017