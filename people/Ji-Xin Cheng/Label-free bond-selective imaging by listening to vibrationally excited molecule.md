# Label-Free Bond-Selective Imaging by Listening to Vibrationally Excited Molecules

Han-Wei Wang,1 Ning Chai,2 Pu Wang,1 Song Hu,3 Wei Dou,4 David Umulis,1,4 Lihong V. Wang,3 Michael Sturek,1,5 Robert Lucht,2 and Ji-Xin Cheng1,6,\*

1 Weldon School of Biomedical Engineering, Purdue University, West Lafayette, Indiana 47907, USA

2 School of Mechanical Engineering, Purdue University, West Lafayette, Indiana 47907, USA

3 Department of Biomedical Engineering, Washington University in St. Louis, St. Louis, Missouri 63130, USA

4 Department of Agricultural and Biological Engineering, Purdue University, West Lafayette, Indiana 47907, USA

5 Department of Cellular and Integrative Physiology, Indiana University School of Medicine, Indianapolis, Indiana 46202

6 Department of Chemistry, Purdue University, West Lafayette, Indiana 47907, USA

(Received 12 November 2010; revised manuscript received 7 May 2011; published 10 June 2011; publisher error corrected 15 June 2011)

We report the realization of vibrational photoacoustic (VPA) microscopy using optical excitation of molecular overtone vibration and acoustic detection of the resultant pressure transients. Our approach eliminates the tissue scattering problem encountered in near-infrared spectroscopy and enables depthresolved signal collection. The 2nd overtone of the CH bond stretch around $8 3 0 0 ~ \mathrm { c m } ^ { - 1 }$ , where blood interference is minimal, is excited. We demonstrate 3D VPA imaging of lipid-rich atherosclerotic plaques by excitation from the artery lumen, and lipid storage in live Drosophila larvae, with millimeter-scale penetration depth.

DOI: 10.1103/PhysRevLett.106.238106

PACS numbers: 87.85.Pq, 34.50.Ez, 42.62.Be, 78.20.Pa

Signals from inherent molecular vibrations provide a key approach to detecting specific molecules in cells, tissues, and materials. Vibrational microscopes based on spontaneous Raman scattering and infrared absorption have been widely used for chemical imaging of unstained samples. With a large signal level and 3D spatial resolution, nonlinear vibrational microscopy based on coherent anti-Stokes Raman scattering (CARS) [1] and stimulated Raman scattering [2] has shed new light on lipid biology via label-free imaging of myelin in neuronal tissues, fat storage in C. elegans, and lipid bodies inside cells. While coherent Raman microscopy offers submicron resolution for monitoring subcellular structures, it employs ballistic photons and thus has a tissue penetration depth of ca 100 m, which limits its potential for deep tissue imaging in clinical settings. For instance, we had to employ crosssectional slices of arteries to visualize the lipid-laden plaques in atherosclerosis by CARS [3]. Extensive efforts have been made to increase the penetration depth optically by use of adaptive optics [4] and invasively by use of a miniature microprobe objective [5]. In addition, the concept of CARS endoscopy has been reported [6]. However, none of these strategies have overcome the difficulties of a small field of view and limited penetration depth inherent to nonlinear vibrational imaging.

We report a new method termed vibrational photoacoustic (VPA) microscopy that permits 3D vibrational imaging of tissues with a field of view and a penetration depth both in the millimeter scale. Our method is based on excitation of molecular overtone vibration and acoustic detection of the resultant pressure waves in the tissue. Overtone and combinational band absorptions are essential principles of near-infrared spectroscopy that measures bulk absorbance or reflectance of samples. According to the anharmonicity theory, the frequency of an overtone band is described by $\bar { \nu } = \bar { \nu } _ { 1 } n - \chi \bar { \nu } _ { 1 } ( n + n ^ { 2 } )$ , where $\bar { \nu } _ { 1 }$ is the frequency of the fundamental vibration, $\chi$ is the anharmonicity, and $n = 2 , 3 , \ldots$ . represent the first, second, and so on, overtones [Fig. 1(a)]. Using the near-infrared spectroscopic approach, molecular spectra in chemical and biological samples can be unraveled according to radiation signals representing the overall overtone absorption and the elastic scattering in a sample [7]. Remarkably, the spectral information can also be retrieved to perform a molecular scan or chemogram of biological tissues, e.g., atherosclerotic arteries [8,9]. The bulk measurement of absorbance or reflectance, however, obscures depth information. The elastic scattering further compromises the imaging potential of near-infrared spectroscopy. Notably, most of the 2nd overtone frequencies of molecules are located in the nearinfrared region from 800 to 2500 nm. In particular, the 2nd overtones of CH and NH stretching modes lie between 1000 and 1300 nm, where the background tissue is minimally absorbing. Within this spectral region, overtone vibrational absorption provides opportunities to generate a chemically selective photoacoustic (PA) transient in a biological structure.

The PA effect takes place when laser radiation is absorbed by a sample. The absorbed energy is converted to heat which then causes local volume expansion through the thermal elastic process. The thermal expansion thereafter generates a pressure transient that propagates as an acoustic wave and can be detected by one or more transducers. The pressure transients encode the spatial information of absorbers on which the image reconstruction is grounded. The PA signal has been used for mapping vessel plexuses [10,11] owing to the strong contrast from electronic absorption of hemoglobin in the visible region. Oxygenated and deoxygenated blood can be distinguished with such contrast [10,11]. Other than hemoglobin, labels such as dyes [12,13] and nanoparticles [14,15] were used as contrast agents for probing specific targets.

![](images/c535cacd34f6b94b1b36b6905f317c062ff6b645207bfba69121f35de75ed0e6.jpg)

<details>
<summary>text_image</summary>

a
n = 3
n = 2
n = 1
n = 0
b
Preamp
Scanning Stage
ns laser beam
Receiver/Amplifier
DAQ & PC
Oscilloscope
</details>

![](images/127bdf10deae552c22c2accf18b6a82b412f869d7d84341de9c91335cb6c3a0c.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Olive oil | Perivascular fat | Whole Blood | Water | Collagen matrix |
| ------------------ | --------- | ---------------- | ----------- | ----- | --------------- |
| 6000               | 0.0       | 0.0              | 0.0         | 0.0   | 0.0             |
| 7000               | 0.0       | 0.0              | 0.0         | 0.5   | 0.0             |
| 8000               | 4.5       | 2.0              | 0.5         | 0.0   | 0.5             |
| 9000               | 0.5       | 0.5              | 1.5         | 0.0   | 0.5             |
| 10000              | 0.5       | 0.5              | 2.5         | 0.0   | 0.5             |
| 11000              | 1.0       | 1.0              | 3.0         | 0.0   | 1.0             |
</details>

FIG. 1 (color online). Photoacoustic detection of molecules based on overtone absorption. (a) Schematic diagram of the 1st and 2nd overtone absorption of a molecule. (b) VPA imaging on an inverted microscope. T, ultrasound transducer; gray (red) beam, ns laser. (c) VPA spectra of biological molecules and tissue components. The VPA signal amplitude is normalized to the laser energy at each wavelength. The VPA peak around 1200 nm contains the contribution from 2nd overtone of symmetric and asymmetric stretching modes of $\mathrm { C H } _ { 2 } .$ . The 3rd overtone band of the CH stretching can be observed around 920–935 nm.

Because molecular overtone transitions are much weaker than electronic transitions, we have carefully performed technical design and experiments to explore VPA imaging based on overtone absorption of molecules as the contrast mechanism. The amplitude of a PA pressure transient is described by $P \propto E \beta \alpha n ( \kappa / \rho C _ { p } )$ (E, radiation fluence; $\beta ,$ thermal coefficient of volume expansion; $\alpha ,$ absorption cross section; n, concentration of absorbing species; , bulk modulus; $\rho ,$ mass density; $C _ { p } .$ , specific heat capacity at constant pressure). The absorption cross section of hemoglobin $( 9 . 1 \times 1 0 ^ { - 1 7 } \ \mathrm { c m ^ { 2 } / m o l e c u l e } )$ is about 6 orders of magnitude larger than that of the second overtone of CH stretching modes [16]. However, the molar density of hemoglobin in whole male blood $( \sim 1 . 0 2 \times$ $1 0 ^ { - 2 } \ \mathrm { \dot { M } ) }$ is much lower than that of CH stretching bonds in olive oil $( 5 \times 1 0 ^ { 1 } ~ \mathrm { M } )$ . Considering the higher thermal coefficient of expansion and lower specific heat capacity of olive oil, it is anticipated that a 10 times higher energy density is needed to generate a VPA signal of the second overtone of CH from olive oil at a level similar to the PA signal of whole blood generated at 555 nm. In general, about 20 $\mathrm { m J } / \mathrm { c m } ^ { 2 }$ is used for PA imaging of blood. Therefore, a pulsed radiation of 200 mJ $/ \mathrm { c m } ^ { 2 }$ or higher at the corresponding overtone frequency is needed for VPA imaging.

Based on these calculations, we have designed optics with proper focusing to provide sufficient energy density up to $5 \ \mathrm { { \bar { J } } } / \mathrm { { c m } } ^ { 2 }$ for demonstration of VPA imaging. The radiation is generated by a 5-ns, Nd:YAG pumped optical parametric oscillator laser system (Fig. S1 in supplementary material [17]). We employ a doublet lens $( f =$ 30 mm) to weakly focus the beam that provides enough spatial resolution and meanwhile renders sufficient energy density to VPA generation. Ultrasound transients are collected via a focused-type transducer and through a preamplifier and a signal receiver [Fig. 1(b)]. We have customized an ultrasound coupler by using a water-glass interface to redirect signal to the transducer. Such a configuration separates the transducer from the radiation and keeps the piezoelectric material of the transducer from the heating effect of the radiation to allow reliable detection of acoustic signals. The envelope of each signal amplitude of the PA transient [Fig. S2(a) in [17]] is retrieved for further signal analysis and image reconstruction.

To generate the PA signal from overtone excitation of CH bond, butanal, a CH-rich liquid, was loaded in a glass tube in which the sample volume and location were controlled. The VPA spectrum of butanal around its 2nd overtone absorption of CH stretching vibrations is shown in Fig. S2(b) of [17]. The peak is around $8 4 0 0 ~ \mathrm { c m } ^ { - 1 }$ , corresponding to 1190 nm. The VPA signal is found to be proportional to the energy of radiation pulses [Fig. S2(c) in [17]]. To test the detection sensitivity, we have measured the VPA signal of cholesterol in chloroform solution and were able to obtain a clean VPA spectrum from 25 mM cholesterol (Fig. S3 in [17]). Applying the VPA spectroscopy to biologically significant samples, our spectroscopic results [Fig. 1(c)] show that CH-rich samples produce a strong VPA signal around 1200 nm due to the 2nd overtone absorption of CH stretching vibrations. Specifically, at 1215 nm the VPA signal from adipose tissues is over 7 times higher than that from blood and over 5 times higher than that from collagen, and the acoustic signal is reduced about 40 times when the olive oil was replaced with water. We have also compared PA imaging of whole blood by 5-ns pulsed excitation at 555 nm and VPA imaging of olive oil by 5-ns pulsed excitation at 1200 nm. Both samples were embedded in a glass tube. The same level of signals was produced by using 22 $\mu \mathrm { J }$ for VPA imaging of olive oil and $2 . 5 9 ~ \mu \mathrm { J }$ for PA imaging of whole blood. These data confirm our calculations and demonstrate the feasibility of VPA microscopy. Besides the CH stretching modes, the VPA signal arising from the first overtone and the combination band of OH stretching modes is detectable around 1400 nm $( 6 5 0 0 { - } 7 2 5 0 ~ \mathrm { c m } ^ { - 1 } )$ , and the signal from the 2nd overtone absorption of NH is detectable around 1000 nm. To test the possible penetration depth in biological samples, a phantom made of semiopaque collagen matrices of different thicknesses was applied. The result shows that the penetration depth at $e ^ { - 1 }$ signal level is about 7 mm (Fig. S4 in [17]).

To perform 3D VPA imaging, we incorporated an XY translational stage into the system for sample scanning. The amplitude information in the time of flight of a pressure transient represents the locations of absorbers in the depth direction [Fig. S5(a) in [17]]. Therefore, by recording the pressure waveform of each pixel in an XY plane, 3D VPA images can be reconstructed. The VPA signal at each pixel was produced by a single pulse. We first used a sample phantom comprising an oil bubble in a polydimethylsiloxane (PDMS) slab [Fig. S5(b) in [17]] to demonstrate the 3D VPA imaging capability [Fig. S5(c) in [17]]. Planar images, reconstructed according to signal amplitudes at different times of flight, show the sectional views of the oil bubble at different depths [Figs. S5(d) and S6 in [17]]. The images elucidate the volume and a concave surface of the oil bubble formed in the PDMS slab. The spatial resolution was measured using an oil-filled microfluidic channel (Fig. S7 in [17]). The axial resolution is ca 130 m and can be improved using a transducer at a higher frequency. The lateral resolution produced by the doublet lens is ca 70 m, and can be improved to 7 m when a 10- objective lens is used (Fig. S8 in [17]).

For biomedical applications, we have performed 3D VPA imaging of lipid-rich atherosclerotic plaques optically excited from the lumen side. Lipid deposition is a major hallmark in atherosclerosis that predominates the lesion progression and plaque vulnerability to rupture [18]. Accurate monitoring of the lipid content in an arterial wall would provide a phenomenal improvement of vascular intervention in diagnosis and treatment of atherosclerosis [18]. To demonstrate label-free VPA imaging of atherosclerotic lipid depositions, carotid arteries were harvested from Ossabaw pigs having metabolic syndrome and profound atherosclerosis. Spectroscopic analysis and 3D imaging were conducted from the luminal side of the artery [Fig. 2(a)]. VPA spectroscopy at different sites of atheromatous arterial walls demonstrated clearly the capability of sensing different levels of lipid accumulation [Fig. 2(b)]. Cross-sectional views of the lesions at the three VPA imaged locations were verified by histology (Fig. S9 in [17]). Locations I–III in Fig. 2(b) correspond to a thickened intima, an intermediate plaque without a necrotic core or fibrotic lesion, and a relatively advanced lesion with the formation of a lipid core, respectively. According to the VPA spectra of the lipid depositions in atheromatous arterial walls, we used the radiation at 1195 nm for 3D VPA imaging of atherosclerotic lipid deposition with optimal vibrational contrast from the lipid depositions. Our images elucidate different milieus of lipid accumulation in the arterial wall [Figs. 2(c)–2(e) and online Videos 1–3 in [17]], such as a confluent lipid core in an atheromatous artery [Fig. 2(c)], a scattered lipid deposition in an arterial wall [Fig. 2(d)], and the formation of mild fatty streaks in early atheroma [Fig. 2(e)]. We were able to detect a strong VPA signal from lipids located at 1.5 mm below the lumen. Furthermore, by exploiting the VPA spectral difference between fat and collagen [Fig. 1(c)], selective imaging of fat by 1200 nm excitation and collagen by 1350 nm excitation could be achieved (Fig. S10 in [17]). The VPA method that enables 3D imaging represents a significant improvement over the existing near-infrared method [8,9,18]. We note that previous studies attempted to distinguish healthy and diseased artery tissues by PA detection of the same tissue at multiple wavelengths [19–21]. However, the contrast mechanism was not investigated and 3D images of plaques were not shown in those studies.

![](images/cf75b816dcb1e657ce8b124965eaede3b09f49d5a4c3392cd504e1ecd0da7310.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Location I Signal Amplitude (V) | Location II Signal Amplitude (V) | Location III Signal Amplitude (V) |
| ------------------ | ------------------------------ | ------------------------------- | -------------------------------- |
| 7000               | ~0.0                           | ~0.0                            | ~0.0                             |
| 8000               | ~0.2                           | ~0.6                            | ~1.4                             |
| 9000               | ~0.1                           | ~0.3                            | ~0.8                             |
| 10000              | ~0.0                           | ~0.1                            | ~0.2                             |
| 11000              | ~0.0                           | ~0.0                            | ~0.1                             |
</details>

FIG. 2 (color online). Lipid depositions in atheromatous arteries mapped by VPA microscopy. (a) Schematic drawing of luminal inspection of an atheromatous artery by VPA microscopy. (b) VPA spectra elucidate progressively greater levels of lipid deposition inside an arterial wall at positions I, II, and III compared to a normal artery with no lipid deposition. (c)–(e) 3D reconstructed VPA images of a confluent lipid core in an atheromatous artery (c), a scattered lipid deposition in an arterial wall (d), and mild fatty streaks (e). 3D animations are available as supplementary videos; see [17].

We have further applied the VPA microscope to map fat bodies in the entire larvae of living Drosophila melanogaster embedded in a thin layer of agar gel. Drosophila melanogaster is one of the genetically best-known and widely used model organisms for genetic, behavioral, metabolic, and autophagic studies. Utilizing the VPA signal of overtone absorption of CH bond stretch, we conducted 3D imaging of fat bodies of whole 3rd-instar larvae in vivo [Fig. 3(a) and online Video 4 in [17]]. The projection and sectional images elucidate the distribution of lipid storage along the anterior-posterior and the ventral-dorsal axis [Figs. 3(b) and 3(c)]. We have also performed depthresolved spectra, along the z axis, at certain points. Figure 3(d) exemplifies the spectral analysis and shows compositional information that is promising for use in depth-resolved compositional analysis. The demonstrated capability of label-free visualization of adipose tissues in Drosophila is important for the rapid determination of phenotype, which will decrease the time required to conduct genetic screens for targets of fat metabolism and autophagy in this model organism [22,23]. We note that because electronic absorption is minimal at 1:2 m, no tissue damage (e.g., plasma formation) was observed at the pulse energy of less than $3 5 ~ \mu \mathrm { J } \ : ( < 5 ~ \mathrm { J } / \mathrm { c m } ^ { 2 }$ at the focus) used for all the VPA imaging experiments.

![](images/90614824d81ac0e08ca8b2adbdd0511d2381e83371ebd1f12c446bf34f69738c.jpg)

<details>
<summary>text_image</summary>

a
Dorsal 1 mm
1 mm²
0.6 mm
0.4 mm
0.3 mm
c
1 mm²
1 mm
Anterior 1 mm
Posterior
y z x
b
X = 0.5 mm
X = 3.5 mm
Y
Signal Amplitude (V)
7000 8000 9000 10000 11000
Wave number (cm⁻¹)
d
1.0 mm²
0.8
0.7
0.5
0.4
0.1
0
Signal Amplitude (V)
0.5
0.4
0.3
0.2
0.1
0.05
0.03
0.02
</details>

FIG. 3 (color online). In vivo 3D VPA imaging of fat bodies in a 3rd-instar larva of Drosophila melanogaster. (a) 3D reconstruction and maximum amplitude projections in XZ and XY planes, (b) transverse images, and (c) longitudinal (planar) images of the lipid storages in a Drosophila larva. (d) Depthresolved VPA spectra at a location indicated by the light gray (yellow) arrow in (b). 3D animation is available as a supplementary video; see [17].

Previously, PA Raman spectroscopy was demonstrated as a way to perform chemical analysis relying on molecular vibration. This method, based on the energy deposition via the stimulated Raman scattering processes, was previously used for analysis of samples in gas phase [24]. Relatively weak PA Raman signals from adipocytes were reported [25]. Recently, PA Raman imaging of chloroform in a capillary tube has been demonstrated [26]. Theoretically, the energy deposition efficiency of the stimulated Raman process is on the order of $1 { \dot { 0 } } ^ { - 7 } – 1 0 ^ { - 8 }$ [24], which is over 1000 times lower than the possible energy deposition rate through overtone absorption of a specific composition in a biological tissue, such as lipid in an artery [8,27]. Moreover, the Raman-related PA signal can be embedded in a large background due to electronic absorption of each radiation beam. We have performed Raman-induced PA spectroscopy on the same setup. With similar pulse energy we used for VPA imaging and at CH vibration resonance of $2 8 5 0 ~ \mathrm { c m } ^ { - 1 }$ , we could not detect Raman-induced PA signal from olive oil.

With a penetration depth of millimeters and chemical information to identify the composition in biological samples without the need for labeling, our method opens up exciting opportunities for noninvasive, high resolution, intravital imaging of lipid-related disorders. Our method is also applicable to other molecules based on the NH and

OH vibrations. Though the imaging speed is limited by the low repetition rate laser used in our work, the speed can be significantly improved using a laser at kilohertz repetition rate for excitation. With such improvements, we envision a new avenue toward intravital diagnosis of, but not limited to, lipid-related disorders.

We acknowledge a grant from the American Heart Association to H. W. W.; support from R01 EB7243 to J. X. C.; HL062552 and the Fortune-Fry Ultrasound Research Fund to M. S.; and R01 EB000712, U54 CA136398, and 5P60 DK02057933 to L. V. W.

\*To whom correspondence should be addressed. jcheng@purdue.edu

[1] A. Zumbusch, G. R. Holtom, and X. S. Xie, Phys. Rev. Lett. 82, 4142 (1999).  
[2] C. W. Freudiger et al., Science 322, 1857 (2008).  
[3] H.-W. Wang et al., Arterioscler. Thromb. Vasc. Biol. 29, 1342 (2009).  
[4] A. J. Wright et al., Opt. Express 15, 18 209 (2007).  
[5] H. Wang et al., Opt. Lett. 32, 2212 (2007).  
[6] F. Le´gare´ et al., Opt. Express 14, 4427 (2006).  
[7] D. A. Burns and E. W. Ciurczak, Handbook of Near-Infrared Analysis (CRC Press, Boca Raton, 2008).  
[8] P. R. Moreno et al., Circulation 105, 923 (2002).  
[9] S. Waxman et al., J. Am. Coll. Cardiol. Img. 2, 858 (2009).  
[10] X. Wang et al., Nat. Biotechnol. 21, 803 (2003).  
[11] H. F. Zhang et al., Nat. Biotechnol. 24, 848 (2006).  
[12] X. Wang et al., Opt. Lett. 29, 730 (2004).  
[13] K. H. Song et al., J Biomed. Opt. 13, 054033 (2008).  
[14] L.-S. Bouchard et al., Proc. Natl. Acad. Sci. U.S.A. 106, 4085 (2009).  
[15] J.-W. Kim et al., Nature Nanotech. 4, 688 (2009).  
[16] P. Cias, C. Wang, and T. Dibble, Appl. Spectrosc. 61, 230 (2007).  
[17] See supplemental material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.106.238106 for methods and supplemental figures and videos.  
[18] S. Waxman, F. Ishibashi, and J. E. Muller, Circulation 114, 2390 (2006).  
[19] B. Wang et al., Opt. Express 18, 4889 (2010).  
[20] T. J. Allen and P. C. Beard, Proc. SPIE Int. Soc. Opt. Eng. 7177, 71770A (2009).  
[21] T. J. Allen et al., Proc. SPIE Int. Soc. Opt. Eng. 7564, 75640C (2010).  
[22] K. D. Baker and C. S. Thummel, Cell Metabol. 6, 257 (2007).  
[23] M. Slaidina et al., Dev. Cell 17, 874 (2009).  
[24] D. R. Siebert, G. A. West, and J. J. Barrett, Appl. Opt. 19, 53 (1980).  
[25] E. V. Shashkov, E. I. Galanzha, and V. P. Zharov, Opt. Express 18, 6929 (2010).  
[26] V. V. Yakovlev et al., Proc. Natl. Acad. Sci. U.S.A. 107, 20 335 (2010).  
[27] L. A. Cassis and R. A. Lodder, Anal. Chem. 65, 1247 (1993).