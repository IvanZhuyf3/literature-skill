## FULL ARTICLE

# Heterodyne detected nonlinear optical imaging in a lock-in free manner

Mikhail N. Slipchenko1 , Robert A. Oglesbee2, Delong Zhang2, Wei $W u ^ { 1 }$ , and Ji-Xin Cheng\*; 1; 2

1 Weldon School of Biomedical Engineering, Purdue University, West Lafayette, IN 47907 USA  
2 Department of Chemistry, Purdue University, West Lafayette, IN 47907 USA

Received 11 January 2012, revised 1 February 2012, accepted 2 February 2012

Published online 5 March 2012

Key words: tuned amplifier, coherent Raman scattering, stimulated Raman scattering, nonlinear microscopy, heterodyne detection

Supporting information for this article is available free of charge under http://dx.doi.org/10.1002/jbio.201200005

We report a compact, cost-effective tuned amplifier for frequency-selective amplification of the modulated signal in heterodyne detected nonlinear optical microscopy. Our method improved the signal to noise ratio by an order of magnitude compared to conventional lock-in detection, as demonstrated through stimulated Raman scattering imaging of live cells and tissues at the speed of 2 msec/pixel. Application of the tuned amplifier to transient absorption microscopy is also demonstrated. The increased signal to noise ratio allowed epi-detected in vivo imaging of myelin and blood in rat spinal cord with high spatial resolution.

![](images/752c133089547e0d0e3a3b83c697c90615250f794fa2a67a82a660c264beb8a1.jpg)  
Tuned amplifier (TAMP) allows SRS imaging with a much higher signal to noise ratio than lock-in amplifier.

## 1. Introduction

Several heterodyne detected optical imaging techniques based on interferometric CARS [1–3], stimulated Raman scattering (SRS) [4], transient absorption [5], and photothermal effect [6] have shown great potential for label-free imaging, e.g., SRS microscopy [7, 8–11] has been used for vibrational imaging of biomass [12], pharmaceutical samples [13, 14], and lipid bodies [10, 15]. All these techniques require the extraction of a small AC signal at the sub-microvolt level from a noisy environment. The lock-in amplifier (LIA), invented by Robert Dicke in 1961 and known as a phase-sensitive detector, has been an essential instrument for heterodyne detected nonlinear optical microscopy.

Although laser shot noise limit can be reached by MHz modulation in SRS microscopy [8–10, 16], the signal to noise ratio (SNR) at low laser power is actually limited by the electronic noise of the LIA’s input preamplifier. For an ideal voltage preamplifier the source of the electronic noise is the thermal Johnson–Nyquist noise of the input impedance,

$$
V _ {\text { noise }} = \sqrt {4 k _ {\mathrm{B}} T R \Delta f}
$$

where $k _ { \mathrm { B } }$ is a Boltzmann’s constant, T is temperature, R is the value of resistor, and $\Delta f$ is the bandwidth. For current sources like photodiodes the voltage on the input of amplifier is linearly dependent on the input impedance while the thermal noise has a square root dependence on impedance. Based on this consideration, the simplest approach to improve the SNR is to use larger impedance at the LIA input. However, due to the parasitic junction capacitance of the photodiode and input capacitance of the LIA, the input impedance has to be set low (usually 50 Ohm) for MHz-rate modulated signal to be effectively detected. For a 50 Ohm resistor at room temperature, $V _ { \mathrm { n o i s e } } = 0 . 9 \ : \mathrm { n V / H z ^ { 1 / 2 } }$ . This noise is equal to the level of photocurrent shot noise produced by an 800 nm laser of 6 mW power at the photodiode with 0.5 A/W sensitivity. For tissue samples less than 30% of the photons reach the forward detector and less than 10% of the photons reach the epi detector. Therefore, more than 18 and 60 mW laser power at the sample is needed to approach the laser shot noise limit in forward and epi detection, respectively (Figure S1). Such power is often above the level of damage threshold for biological samples [10].

In addition to the relatively large thermal noise, LIA-based detection sets the limit of imaging speed and also lacks the simplicity. The widely used SR844 digital LIA offered by Stanford Research Systems has a minimum time constant of 20 msec. At such time constant it takes tens of seconds to obtain an image of 512 - 512 pixels [8]. Faster digital LIA, such as the HF2LI model (Zurich Instruments) with the shortest time constant of 0.8 msec, has been used for stimulated Raman loss imaging [10]. A homebuilt analog LIA amplifier was recently employed for video rate SRS imaging [17]. Nevertheless, these radio frequency LIAs are sophisticated devices, which sets a bottleneck for wide use of SRS microscopy by non-experts.

A lock-in amplifier is essentially a phase-sensitive bandpass amplifier with variable central frequency and bandwidth. For imaging applications such as SRS microscopy, the laser modulation frequency is fixed, the signal phase is known (i.e. 0 for Raman gain and 180 degree for Raman loss), and the time constant needs to be as short as a few msec for real time imaging. A time constant of t ¼ 1.0 msec corresponds to a bandwidth (at 3 dB) of $\Delta \dot { f } = ( \tau \pi ) ^ { - 1 }$ ¼ 320 kHz. Similar bandwidth can be achieved in a much simpler way, through a RLC resonant circuit of high quality factor (Figure S2). For an ideal parallel RLC circuit the resonance frequency, w , quality factor, Q, and bandwidth, Dw, are given as

$$
\omega_ {0} = 1 / \sqrt {L C}, \quad Q = R \sqrt {C / L}, \quad \Delta \omega = \omega_ {0} / Q
$$

respectively. For high-speed imaging conditions this set of equations determine the value of the load resistor, R, to be in the range of tens of kOhm. Therefore, in cases where Johnson–Nyquist noise is dominant, the resonant circuit could enhance the SNR by one order of magnitude compared to a LIA with a 50 Ohm input impedance.

Based on the above concept, we have designed a tuned amplifier (TAMP) and tested its performance on a stimulated Raman loss (SRL) microscope where the pump beam serves as the local oscillator (LO) and the Stokes beam is modulated (Figure S3). The TAMP is designed to extract a small modulation of LO, usually with $\Delta I / I \le 1 0 ^ { - 4 }$ , riding on the top of a strong DC component.

## 2. Experimental

## 2.1 SRS microscopes

Two SRS imaging systems were used in this study. For femtosecond stimulated Raman loss (fs SRL) imaging and transient absorption imaging, a Ti : Sapphire laser (Chameleon Vision, Coherent) with up to 4 W (80 MHz, 140 fs pulse width) was used to pump an optical parametric oscillator (OPO, Chameleon Compact, Angewandte Physik & Elektronik GmbH), providing the Stokes beam tunable from 1.01.6 mm and the pump beam tunable from 680 to 1080 nm, respectively. The two pulse trains were collinearly overlapped and directed into a laser-scanning upright microscope (FV300/BX51, Olympus). For picosecond SRL microscopy the Stokes beam tunable from 810960 nm and the pump beam tunable from 690 to 790 nm were provided by two 5 ps lasers (Tsunami, Spectra-Physics, CA) electronically synchronized and collinearly combined into an inverted confocal microscope (FV300/IX71, Olympus America Inc, PA). In both setups the Stokes beam intensity was modulated by an acousto-optic modulator. The pump beam (local oscillator) was spectrally selected by a bandpass filter from Chroma and detected by a large area photodiode (S3071, Hamamatsu). A lock-in amplifier (HF2LI, Zurich Instruments) was used for phase sensitive detection.

## 2.2 Tissue preparation

All procedures were approved by the Purdue Animal Care and Use Committee. Small intestines were extracted from 3-month old male mouse (C57BL/6) as described previously [18]. For intact tissue imaging, ex vivo fresh tissue (5 mm long) from small intestine (S2, representing upper jejunum) was placed in 3 mL Dulbecco’s Modified Eagle’s Medium (Gibco, Carlsbad, CA) supplemented with 20 mM HEPES, 100 U/mL penicillin-streptomycin (Gibco), and 10% fetal bovine serum.

## 2.3 Cell culture

Chinese hamster ovary (CHO) cells and SCC7 cells were cultured in a coverslip bottomed dish at $3 7 ^ { \circ } \mathrm { C }$ in a humidified atmosphere containing 5% $\mathrm { C O } _ { 2 }$ and grown continuously in folate-deficient RPMI 1640 medium containing 10% FBS and 1% penicillinstreptomycin.

## 2.4 Preparation of all trans Retinoic Acid (atRA)-loaded PLGA microspheres

PLGA (700 mg) was dissolved in dichloromethane (5 ml) and atRA (7, 35, or 70 mg) was added to the PLGA solution. Then, the mixture was dropped into 150 ml of aqueous solution (0.1 w/v% of PVA) using a glass syringe (10 ml) and a needle (needle gauge; 18 G) while stirring with a magnetic stirrer at 500 rpm. In order to remove the organic solvents, the suspension was heated for 1 h at $4 0 ^ { \circ } \mathrm { C }$ under gentle stirring at 500 rpm. For purification, drug-loaded PLGA microspheres were collected via centrifugation at 1200 rpm for 2 min, washed four times with distilled water, and then lyophilized.

Detailed information on the materials and methods is included in the Supporting Information.

## 3. Results and discussion

As shown in Figure 1a, the TAMP is composed of a LC resonant tank circuit, a low noise JFET-based preamplifier [19], a bandpass filter, a selectable gain amplifier, and a full wave precision rectifier, integrated into a single box (Figure S4). The LC circuit backed up by a voltage buffer preamplifier selectively amplifies the signal at the modulation frequency by 44 dB. Next, the bandpass filter eliminates the low and high frequency noise leaking through the resonant circuit. The following amplifier with selectable gain from 19 to 58 dB further enhances the signal level in order to reach the amplitude of a few volts. Finally, the signal is rectified with the precision rectifier and then sent to the analog-to-digital converter for digitization. Detailed description of the TAMP can be found in supporting information.

To validate the design we measured the bandwidth of the LC circuit for which the resonance frequency was tuned to the optical modulation frequency of f ¼ 6 MHz. As shown in Figure 1b, the measured bandwidth (full width at 0.707 maximum) of the LC circuit was 250 kHz, which is smaller than the measured bandwidth of 360 kHz of a digital LIA (HF2LI, Zurich Instruments) under the setting of 1 msec time constant. From the measured central frequency and bandwidth (Figure 1b) the quality factor of the LC circuit is estimated to be about 24.

![](images/8ddbeb17901d9ef6439c4bebc97d8d0f576c173d9fe64bdec9a6976d6add5bed.jpg)  
Figure 1 (online color at: www.biophotonics-journal.org) Principle of heterodyne detection with a tuned amplifier. (a) Schematic of a lock-in free stimulated Raman loss microscope and electronic components in a tuned amplifier (TAMP). The Stokes beam intensity is modulated by an optical modulator (OM) and the pump beam serves as the local oscillator (LO). The LO is detected by a photodiode (PD). The TAMP selectively amplifies the signal and sends it to the analog to digital converter (ADC). (b) Bandwidth comparison between the LIA and TAMP circuits. (c), (d) Non-rectified output from a tuned amplifier recorded on an oscilloscope (TDS5000B, Tektronics). The signal was produced through a line scan across the olive oil/air interface. Pump and Stokes beams were tuned to be resonant with C––H stretch vibration. (e) FFT analysis of the amplitude trace, showing that the tuned amplifier selectively transmits the signal at the modulation frequency of 6.0 MHz.

Compared to the steep cut off of LIA response, the LC circuit response showed two wings extending to lower and higher frequencies. These parasitic components in the signal were subsequently eliminated by the bandpass filter. To further clarify the working principle of the tuned amplifier, a line scan across an oil/air interface was performed and the SRL signal before the rectification stage was recorded with a fast oscilloscope. The recorded oscilloscope trace (Figure 1c) shows large amplitude corresponding to signal from olive oil. Zooming into the trace shows periodic oscillations (Figure 1d) at the optical modulation frequency, as confirmed by FFT analysis (Figure 1e).

The performance of the TAMP was evaluated against LIA with a 50 Ohm input impedance by measuring the dependence of the SRL signal from olive oil and the noise on the LO generated photocurrent at the detector. The measured linearity of the SRL signal on the photocurrent (Figure 2a) shows a dynamic range for linear response from 0.1 to 7 mA photocurrent, which corresponds to 0.2 to 14 mW of LO power at the detector. Such dynamic range is sufficient for most SRS imaging applications. In principle the linearity for high LO power can be extended by reducing the value of the current limiting resistor in the preamplifier, and the nonlinearity for LO power lower than 0.2 mW can be overcome by using higher amplifier gain before rectification. The noise dependence on the photocurrent is strikingly different for LIA and TAMP (Figure 2b). The LIA input noise remained constant from 0 to 2 mA photocurrent and then slowly increased with photocurrent. The plateau is due to the dominant electronic noise at low photocurrent. For 2 msec time constant used in these measurements, the bandwidth is equal to 160 kHz, which corresponds to Johnson– Nyquist noise of 0.37 mV for a 50 Ohm load. The measured electronic noise of LIA has slightly higher value of 0.5 mV due to extra noise of LIA’s input preamplifier. In contrast, the total noise arising from TAMP-based detection showed square root dependence (slope ¼ 0.5 in log scale) on the photocurrent from 0.1 to 7.0 mA, which indicates true laser shot noise limited detection. The dependences of SNR on the photocurrent for LIA and TAMP are compared in Figure 2c. At the LO power below 1 mW, the TAMP improved the SNR by up to 10 times compared to LIA based detection. Such improvement opens the opportunity for high-speed, high-quality SRS imaging with low power sources such as Er: fiber lasers [20], photonic crystal fiber [21, 22] or fiber optical parametric oscillator [23] recently developed as compact and cost-effective alternatives to solid state lasers.

![](images/430565703b94c029a36d28b06ae41d6ead851777c18365cf300be712a7238f0a.jpg)  
Figure 2 (online color at: www.biophotonics-journal.org) TAMP enhances the detection sensitivity of SRL microscopy. (a)–(c) Comparison of LIA and TAMP linearity, noise level, and signal to noise ratio, respectively. The SRL signal was generated by olive oil and the noise level was calculated as standard deviation of the pixel intensity with the Stokes beam blocked. The top scale indicates corresponding pump beam power at the photodiode. (d), (e) SRL images of 200 nm polystyrene particles acquired with LIA and TAMP, respectively. The TAMP detection improved the signal to noise ratio by 6 times. Scale bar is 5 mm. (f), (g) TAMP-based SRL images (XZ scan, 30 - 120 mm) of 50 mM deuterated palmitic acids dissolved in DMSO and pure DMSO solvent, respectively, at the Raman shift of 2100 cm1 . The Stokes beam power was 2 mW at the sample for a–c. The pump and Stokes beam powers at the sample were 4 and 12 mW for d, e and were 6 and 40 mW for f, g, respectively. The imaging speeds were 2 msec/pixel for a, c and f, g, and 8 msec/pixel for d, e.

The detection sensitivity of LIA-based and TAMP-based SRL microscopy was compared by mapping 200 nm polystyrene beads spin-coated on a coverslip. It was found that the TAMP improved the SNR by 6 times (Figure 2d, e). The improved sensitivity allowed chemical mapping of 50 mM d -palmitic fatty acid dissolved in DMSO at the speed of 2 msec per pixel (Figure 2f, g). For comparison, an integration time of 2 sec is required to obtain similar SNR of the C–D peak using spontaneous Raman technique (Figure S5). In an earlier study [8], LIAbased SRS detection of 5.0 mM methanol dissolved in water was reported using 1 sec integration time.

With improved SNR we demonstrate TAMPbased stimulated Raman loss (SRL) imaging of C––H band with femtosecond (fs) pulse excitation [10] and of fingerprint bands with picosecond (ps) pulse excitation. Figure 3a shows fs SRL image of triacylglycerol pools stored in enterocytes of mouse small intestine [18] based on the signal from C––H stretch vibration. By comparing the C––H off-resonance images and the time off images obtained by TAMP and LIA, it was found that TAMP-based detection produced the same signal level as LIA based detection but reduced the noise by 3 time (Figure S6). Without affecting the spatial resolution, the TAMP technique allowed high-speed 3-D mapping of the lipids in villi of a small intestine (Movie 1). As another application, Figure 3b shows TAMP-based fs SRL image of SCC7-cell with an intensive signal originating from small lipid droplets. Without photodamage to cells [10], trafficking of small LDs in live cells was monitored in real time (Movie 2).

The capability of our lock-in free method for fingerprint SRL imaging was tested by mapping drug distribution in poly(lactic-co-glycolic acid) (PLGA) microspheres. As a biodegradable and biocompatible polymer, PLGA has been frequently used in microencapsulation of bioactive molecules such as alltrans retinoic acid (atRA). Based on their distinctive Raman bands shown in Figure S7, PLGA and atRA in the microspheres were mapped by SRL generated by a 5 ps laser source. Figure 3c, d shows the SRL images of PLGA microspheres without atRA and loaded with 5% atRA, respectively, obtained with the speed of 2 msec/pixel. In the absence of atRA the PLGA showed spherical shape. At 5% atRA loading, the drug did not blend with PLGA and was found mostly on the surface of irregular microparticle. These data show the potential of our platform for pharmaceutical applications. Our TAMP device is generally applicable to other types of heterodyne detected nonlinear optical microscopy. As an example, TAMP-based transient absorption imaging of heme proteins in red blood cells (RBCs) is shown in Figure S8.

![](images/145b26b5a04ab1c08a66dcb944bdcb067c1893d43bacfd86942fbb0e4217916d.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of intestinal cells with orange fluorescent labeling (no text or symbols)
</details>

![](images/b5f0b0a2150bd54bd8da6882fc1db8cc0e6f790fb1623b78e3ac76b0e783f5ff.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image of a SCC7 cell with green emission, showing cellular structure and color scale (no text or symbols)
</details>

![](images/9cdccc2fdfaaca9ae62910bbe0a94343a1628d196d848dd2e66c580fcf0c42f1.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing green-labeled PLGA-stained cells against a black background (no text or symbols)
</details>

![](images/dacab61be636ed5fe25a8ba07d0eeabff53c079657c8bfbb052e5a014bebaef8.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red and green labeled cells (no text or symbols)
</details>

Figure 3 (online color at: www.biophotonics-journal.org) Applications of TAMP-based stimulated Raman microscopy. (a) SRL image of lipid droplet in a fresh tissue of small intestine extracted from a mouse. (b) SRL image of C––H distribution in a live SCC7 cell. (c), (d) SRL images of poly(lactic-co-glycolic acid) (PLGA) microspheres without drug loading and loaded with 5% all-trans retinoic acid (atRA), respectively. The PLGA and atRA are visualized at the Raman shift of 2930 and 1580 cm1 , respectively, at the speed of 2 msec/pixel. The pump and Stokes beam powers at the sample were 8 and 20 mW for a and b, and 10 and 20 mW for c and d. Scale bars are 100 mm for a, c and d, and 20 mm for b.

The epi (backward) detection is critical for in vivo imaging applications. In epi-detection the signal is produced by the back-scattered photon reaching the detector [17, 24]. In such a case the photocurrent is much smaller than that in forward detection, and our TAMP detection method shows significant improvement of image quality over the standard LIA detection (Figure 4). Based on the intensity profiles along the dashed lines, the epi-detected fs SRL image of axonal myelin obtained with TAMP gave a SNR of 50 (Figure 4a). In comparison, imaging the same sample with LIA shows a much lower SNR (Figure 4b) due to the electronic noise contribution (Figures S9 and S10). Thus, the TAMP detection improved the SNR by 8.3 times, which permitted ex vivo 3D mapping of axonal myelin with high quality (Movie 3). In vivo application of TAMP was demonstrated by imaging spinal cord in a live rat (Figure S11). Notably, Xie and coworkers recently used a special photodiode directly attached to the objective to increase the efficiency of collecting the backscattered photons [17]. Although their method increased the epi-detected signal level and allowed video rate imaging, it can only be applied to objectives of low numerical aperture. In comparison, the order of magnitude enhancement of SNR offered by TAMP greatly benefits epi-detected SRS imaging without sacrifice of the spatial resolution.

![](images/9356d1fb52ce3bced6c3ad3e7a4b218afbc79a4015eeff3e2dae82a043cec233.jpg)

<details>
<summary>text_image</summary>

a
TAMP
2000
S/N = 50
1000
0
</details>

![](images/cf8ab70a328466ce9b2e281f8709e7b8f65a2d6da6828c2b8d10f62270154f55.jpg)

<details>
<summary>text_image</summary>

b LIA
20 µm
S/N = 6
2000
1000
0
</details>

Figure 4 (online color at: www.biophotonics-journal.org) TAMP significantly improves the signal to noise ratio in epi-detected SRL imaging of spinal cord white matter. (a) Ex vivo epi-SRL image of axonal myelin by TAMP detection. (b) Epi-SRL image of the same sample by LIA detection. Below the images are the intensity profiles along the dashed lines. Imaging speed: 2 msec/pixel. Pump and Stokes wavelengths were set to 830 and 1090 nm, respectively. Images were taken with a 60- IR water immersion objective and average pump and Stokes powers of 25 mW each at the sample position.

It is important to note that although TAMP can replace LIA for hetrodyne optical detection, the phase information is not preserved by TAMP. This is not a problem for SRS microscopy where the phase of the signal is known. If phase sensitive detection is needed, one can direct the resonantly amplified AC signal, produced after the LC circuit and preamplifier (see Figure 1a) to a LIA.

## 4. Conclusions

We have shown a lock-in free detection scheme for highly sensitive heterodyne detected nonlinear optical imaging with a focus on SRS microscopy. Our method allows high-speed SRS imaging of cell culture, tissue, and pharmaceutical samples with increased SNR of up to one order of magnitude compared to LIA based detection. Using the tuned amplifier we demonstrated high-speed epi-SRS imaging of spinal cord ex vivo and in vivo with high spatial resolution, which opens new applications of SRS microscopy. In contrast to the sophisticated LIA, the simple electronic design of the tuned amplifier permitted us to integrate all components into a single box with a small footprint and at a fraction of the cost of LIA. In addition the TAMP does not require phase-locking with the optical modulator and its performance can be optimized by adjusting one parameter, namely the amplifier gain. We anticipate that such simplicity would greatly promote the commercialization of heterodyne-detected microscopy, which in turn will expedite the acceptance of SRS and pump-probe imaging among the biologists.

![](images/975e3e0b622514a93b7dea7f067b7c698e067229781f7a3e56057ceb9e6a9e48.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man with curly hair and beard wearing a checkered shirt (no text or symbols visible)
</details>

Mikhail N. Slipchenko is cur rently a Research Scientis at Department of Biome dical Engineering, Purdue University (West Lafayette, IN). He obtained his Ph.D. in Chemistry from University of Southern California. His research expertise includes nonlinear and linear spectroscopy and optical mi croscopy. He focuses on the

development of linear and non-linear optical tools for chemical imaging.

![](images/94d878e7ac4ae96f3258e68e0eec77021081b49b5cb230028575e07e79a12aea.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling man in a checkered shirt, standing in front of bookshelves (no visible text or symbols)
</details>

Robert A. Oglesbee received his B.S. degree in Electrica Engineering from Purdue University in 1999, and his M.S. degree in Electrical Engineering from the Uni versity of Kentucky in 2008. He is currently a Senior In strumentation Specialist in the Jonathan Amy Facility for Chemical Instrumentation. The Amy Facility is

dedicated to the fusion of scientific knowledge with en gineering expertise to further research efforts at Pur due University.

![](images/58f69a9ea1b4ee9aa8b89879dff9df94ff943bc59a7983bcf49bb0e77fd957bb.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a young man in a striped shirt against a wooden background (no text or symbols visible)
</details>

Delong Zhang received his B.S. degree in Department of Chemical Physics from University of Science and Technology of China, Hefei, China, in 2009. Zhang is currently working as research assistant toward his Ph.D. degree in analytical chemistry at Purdue University, West Lafayette, IN. His research focuses on multimo-

dal nonlinear optical imaging and spectroscopy.

![](images/58f7d86aaba140c10a018c627656e3593dcb22c435289691ce1b3b62bf544a76.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling man in a maroon shirt against a blurred green background (no text or symbols visible)
</details>

Wei Wu received the B.S degree in clinic medicine in Medical Collagen of Nan-Chang University, JiangXi, China, in 2005. He is currently a Ph.D. candidate in ShangHai JiaoTong University and working in bio-medical engineering at Purdue University as a visiting scholar. His research interest include treating spinal cord

injury by nanotechnology, understanding the pathology and therapy effect after spinal cord injury by non-linear microscopy and photoacoustic imaging.

![](images/ecae58b90750bd5e798154d8a6e0b29b4f8cb27ee48628abcede32d0be2535b8.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling man in a collared shirt, hand resting on chin (no text or symbols visible)
</details>

Ji-Xin Cheng received B.S degree and Ph.D. degree in Department of Chemical Physics from University of Science and Technology of China, Hefei, China, in 1994 and 1998, respectively. He is currently an Associate Professor at Weldon School of Biomedical Engineering at Purdue University, West Lafayette, IN. His research lab develops label-free optical

imaging tools and nanotechnologies for challenging applications in biomedicine such as early detection of tumor spread and early nerve repair after traumatic spinal cord injury.

## References

[1] D. L. Marks and S. A. Boppart, Phys. Rev. Lett. 92, 123905 (2004).  
[2] E. O. Potma, C. L. Evans, and X. S. Xie, Opt. Lett. 31, 241–243 (2006).  
[3] M. Jurna, J. P. Korterik, C. Otto, J. L. Herek, and H. L. Offerhaus, Opt. Express 16, 15863–15869 (2008).  
[4] W. Min, C. W. Freudiger, S. Lu, and X. S. Xie, Annu. Rev. Phys. Chem. 62, 507–530 (2011).  
[5] T. Ye, D. Fu, and W. S. Warren, Photochem. Photobiol. 85, 631–645 (2009).  
[6] A. Gaiduk, M. Yorulmaz, P. V. Ruijgrok, and M. Orrit, Science 330, 353–356 (2010).  
[7] E. Ploetz, S. Laimgruber, S. Berner, W. Zinth, and P. Gilch, Appl. Phys. B 87, 389–393 (2007).  
[8] C. W. Freudiger, W. Min, B. G. Saar, S. Lu, G. R. Holtom, C. He, J. C. Tsai, J. X. Kang, and X. S. Xie, Science 322, 1857–1861 (2008).  
[9] P. Nandakumar, A. Kovalev, and A. Volkmer, New J. Phys. 11, 033026 (2009).  
[10] D. Zhang, M. N. Slipchenko, and J.-X. Cheng, J. Phys. Chem. Lett. 2, 1248–1253 (2011).  
[11] Y. Ozeki, F. Dake, S. i. Kajiyama, K. Fukui, and K. Itoh, Opt. Express 17, 3651–3658 (2009).  
[12] B. G. Saar, Y. N. Zeng, C. W. Freudiger, Y. S. Liu, M. E. Himmel, X. S. Xie, and S. Y. Ding, Angew. Chem. Int. Ed. 49, 5476–5479 (2010).  
[13] M. N. Slipchenko, H. Chen, D. R. Ely, Y. Jung, M. T. Carvajal, and J. X. Cheng, Analyst. 135, 2613–2619 (2010).  
[14] B. G. Saar, L. R. Contreras-Rojas, X. S. Xie, and R. H. Guy, Mol. Pharm. 8, 969–975 (2011).  
[15] M. C. Wang, W. Min, C. W. Freudiger, G. Ruvkun, and X. S. Xie, Nat. Meth. 8, 135–138 (2011).  
[16] Y. Ozeki, Y. Kitagawa, K. Sumimura, N. Nishizawa, W. Umemura, S. i. Kajiyama, K. Fukui, and K. Itoh, Opt. Express 18, 13708–13719 (2010).  
[17] B. G. Saar, C. W. Freudiger, J. Reichman, C. M. Stanley, G. R. Holtom, and X. S. Xie, Science 330, 1368– 1370 (2010).  
[18] J. Zhu, B. Lee, K. K. Buhman, and J. X. Cheng, J. Lipid Res. 50, 1080–1089 (2009).  
[19] S. Savikhin, Rev. Sci. Inst. 66, 4470–4474 (1995).  
[20] G. Krauss, T. Hanke, A. Sell, D. Trautlein, A. Leitenstorfer, R. Selm, M. Winterhalder, and A. Zumbusch, Opt. Lett. 34, 2847–2849 (2009).  
[21] H. N. Paulsen, K. M. Hilligse, J. Thøgersen, S. R. Keiding, and J. J. Larsen, Opt. Lett. 28, 1123–1125 (2003).  
[22] A. F. Pegoraro, A. Ridsdale, D. J. Moffatt, Y. W. Jia, J. P. Pezacki, and A. Stolow, Opt. Express 17, 2984– 2996 (2009).  
[23] Y. H. Zhai, C. Goulart, J. E. Sharping, H. Wei, S. Chen, W. Tong, M. N. Slipchenko, D. Zhang, and J. X. Cheng, Appl. Phys. Lett. 98, 191106 (2011).  
[24] P. Wang, M. N. Slipchenko, B. Zhou, R. Pinal, and J. X. Cheng, IEEE J. Sel. Top. Quant. 18, 384–388 (2012).