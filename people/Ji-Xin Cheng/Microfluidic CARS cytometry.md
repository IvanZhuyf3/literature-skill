# Microfluidic CARS cytometry

Han-Wei Wang,1 Ning Bao,2 Thuc T. Le,1 Chang Lu,2 and Ji-Xin Cheng, 1,3,\*

1 Weldon School of Biomedical Engineering, Purdue University, West Lafayette, IN. 47907, USA 2 Department of Agricultural and Biological Engineering, Purdue University, West Lafayette, IN. 47907, USA 3 Department of Chemistry, Purdue University, West Lafayette, IN. 47907, USA \*Corresponding author: jcheng@purdue.edu

Abstract: Coherent anti-stokes Raman scattering (CARS) flow cytometry was demonstrated by combining a laser-scanning CARS microscope with a polydimethylsiloxane (PDMS) based microfluidic device. Line-scanning across the hydrodynamically focused core stream was performed for detection of flowing objects. Parameters were optimized by utilizing polystyrene beads as flowing particles. Population measurements of adipocytes isolated from mouse fat tissues demonstrated the viability of microfluidic CARS cytometry for quantitation of adipocyte size distribution. CARS cytometry could be a new modality for quantitative analysis with vibrational selectivity.

© 2008 Optical Society of America

OCIS codes: (190.4380) Nonlinear optics, four-wave mixing; (300.6230) Spectroscopy, coherent anti-Stokes Raman scattering; (170.1530) Cell analysis

## References and links

1. H. M. Shapiro, Practical Flow Cytometry, 4th ed. (Wiley Liss, New York, 2003).  
2. C. D. Jennings and K. A. Foon, "Recent Advances in Flow Cytometry: Application to the Diagnosis of Hematologic Malignancy," Blood 90, 2863-2892 (1997).  
3. T. D. Chung and H. C. Kim, "Recent advances in miniaturized microfluidic flow cytometry for clinical use," Electrophoresis 28, 4511-4520 (2007).  
4. A. Gordon, A. Colman-Lerner, T. E. Chin, K. R. Benjamin, R. C. Yu, and R. Brent, "Single-cell quantification of molecules and rates using open-source microscope-based cytometry," Nat. Methods 4, 175- 181 (2007).  
5. S. P. Perfetto, P. K. Chattopadhyay, and M. Roederer, "Seventeen-colour flow cytometry: unravelling the immune system," Nat. Rev. Immun. 4, 648-655 (2004).  
6. J. X. Cheng, "Coherent anti-stokes Raman scattering microscopy," Appl. Spectrosc. 61, 197A-208A (2007).  
7. M. Muller and A. Zumbusch, "Coherent anti-Stokes Raman Scattering Microscopy," Chem. PhysChem. 8, 2156-2170 (2007).  
8. J. X. Cheng and X. S. Xie, "Coherent anti-Stokes Raman scattering microscopy: instrumentation, theory, and applications.," J. Phys. Chem. B 108, 827-840 (2004).  
9. H.-Y. Wang and C. Lu, "Microfluidic chemical cytometry based on modulation of local field strength," Chem. Commun. 3528-3530 (2006).  
10. H. Y. Wang and C. Lu, "Electroporation of Mammalian Cells in a Microfluidic Channel with Geometric Variation," Anal. Chem. 78, 5158-5164 (2006).  
11. D. C. Duffy, J. C. McDonald, O. J. A. Schueller, and G. M. Whitesides, "Rapid Prototyping of Microfluidic Systems in Poly(dimethylsiloxane)," Anal. Chem. 70, 4974-4984 (1998).  
12. J. X. Cheng, A. Volkmer, L. D. Book, and X. S. Xie, "An epi-detected coherent anti-stokes Raman scattering microscope with high spectral resolution and high sensitivity," J. Phys. Chem. B 105, 1277-1280 (2001).  
13. H. Wang, Y. Fu, P. Zickmund, R. Shi, and J. X. Cheng, "Coherent anti-stokes Raman scattering imaging of axonl myelin in live spinal tissues.," Biophys. J. 89, 581-591 (2005 ).  
14. A. Zumbusch, G. R. Holtom, and X. S. Xie, "Three-dimensional vibrational imaging by coherent anti-Stokes Raman scattering," Phys. Rev. Lett. 82, 4142-4145 (1999).  
15. K. Bahlmann, P. T. So, M. Kirber, R. Reich, B. Kosicki, W. McGonagle, and K. Bellve, "Multifocal multiphoton microscopy (MMM) at a frame rate beyond 600 Hz," Opt. Express 15, 10991-10998 (2  
16. K. H. Kim, C. Buehler, and P. T. C. So, "High-Speed, Two-Photon Scanning Microscope," Appl. Opt. 38, 6004-6009 (1999).  
17. D. Huh, W. Gu, Y. Kamotani, J. B. Grotberg, and S. Takayama, "Microfluidics for flow cytometric analysis of cells and particles," Physiol. Meas. 26, R73-R98 (2005).

18. T. T. Le, I. M. Langohr, M. J. Locker, M. Sturek, and J. X. Cheng, "Label-free molecular imaging of atherosclerotic lesions using multimodal nonlinear optical microscopy," J. Biomed. Opt. 12, 054007 (2007).

19. Y. Fu, H. Wang, R. Shi, and J. X. Cheng, "Second harmonic and sum frequency generation imaging of fibrous astroglial filaments in ex vivo spinal tissues," Biophys. J. 92, 3251-3259 (2007).

## 1. Introduction

With technological advances in the past decades, flow cytometry has been a powerful tool for quantitative analysis of cell populations and intracellular content [1, 2]. Signals in flow cytometry could arise from electrical impedance, forward or side light scattering, and fluorescence. Scattering and electrical impedance provide granularity and size information, but limited chemical specificity [2, 3]. Fluorescent labeling acts as a prime approach for cellular analysis, either in microscope-based cytometry or flow cytometry [4, 5].

As a nonlinear optical imaging technique with vibrational selectivity, coherent anti-Stokes Raman scattering (CARS) microscopy has been successfully applied to image cells, tissues, and live animals, with a particularly strong signal from CH2-abundant structures [6-8]. Quantitative analysis of cell populations is, however, limited by the relatively small field of view (< 1 mm2 ) in CARS microscopy. Therefore, it is intriguing to combine CARS with flow cytometry for chemically selective cell analysis in a quantitative manner.

In this study, the proof-of-principle of CARS cytometry was demonstrated by the incorporation of a microfluidic device into a laser-scanning CARS microscope. Flowing objects were detected by line-scan of laser beams across the stream defined by 2D hydrodynamic focusing. Polystyrene (PS) beads were used to optimize the scan and flow parameters. As a biological application, the microfluidic CARS device was used to measure the size distribution of adipocytes isolated from mice fat tissues. The current work heralds the potential of CARS flow cytometry in high throughput analysis of objects with chemical selectivity.

## 2. Materials and methods

## 2.1 Sample preparation

Polystyrene (PS) beads (Polybead® Polystyrene Microspheres, Polysciences, PA) of 2 μm (standard deviation, SD, \~0.098 μm), 10 μm (SD \~0.562 μm), and 5 μm (SD \~0.14 μm, PS06N/5544, Bangs Lab, IN) were diluted in milli-Q water. Isolated adipocytes were collected from mouse fat tissues around mammary glands by the following procedure: The fat tissues were minced into pieces and maintained in DMEM media with 10% fatal bovine serum (FBS) at $3 7 \ { } ^ { \circ } \mathrm { C } .$ . To separate the adipocytes from the extracellular matrix, 1 gram of fat tissues was incubated with 10 mg collagenase in 3 ml DMEM media for 1 hour at $3 7 ^ { \circ } \mathrm { C } .$ . By stirring dispersed tissue fragments, adipocytes were liberated in the medium. By removing °large tissue fragments and centrifuging cell suspension for 1 minute at 400 rcf, purified floating adipocytes were collected from the supernatant. The purified adipocytes were maintained in DMEM with 10% FBS at $3 7 ~ ^ { \circ } \mathrm { C }$ and used for experiments within 12 hours. Filtration with 60 μm pore size Nylon filter (CMN-0062, Small Parts, FL) was operated to °remove clumps in order to avoid clog in microfluidic channel.

## 2.2 Microfluidic chip fabrication

Microfluidic chips were fabricated with polydimethylsiloxane (PDMS) [9, 10] based on the soft lithography method [11]. The microfluidic chip consisted of two layers: a thin PDMS layer (channel layer, \~ 280 μm thick) where microfluidic channels resided and a thick PDMS layer (supporting layer, \~ 5 mm thick) which allowed the connection between polymeric tubing and the microfluidic channels (Fig. 1(a)). The thin PDMS “roof” (\~220 μm with a channel depth of \~ 60 μm) allowed sufficient transmission of forward CARS signal. The microscale patterns were designed using a computer-aided software (FreeHand MX, Macromedia, San Francisco, CA) and then printed out on transparency films which were used as photomasks for the fabrication of masters with a negative photoresist (SU-8 2025, MicroChem Corp., Newton, MA) as the relief on the silica wafers. The pattern of channels in the photomask was replicated in the photoresist after exposure and development. The depth of the channels replicated from the thickness of the photoresist was 60 μm (measured by a Sloan Dektak3 ST profilometer). The channel layer was fabricated by casting a layer of PDMS prepolymer mixture (General Electric Silicones RTV 615, MG chemicals, Toronto, Ontario, Canada) with a mass ratio of ${ \bf A } { : } { \bf B } = 1 0 { : } 1$ on the SU-8/Si master and spinning at 500 rpm for 35 sec. The channel layer was cured at $8 0 ~ ^ { \circ } \mathrm { C }$ for 1.5 hr in an oven. The supporting layer was fabricated by casting and curing PDMS layer (\~5 mm thick) with the same composition under °the same conditions. The supporting layer was bonded to the channel layer on the master by oxidizing both PDMS surfaces using a Tesla coil (Kimble/Kontes, Vineland, NJ) in air and bringing the layers into contact immediately after oxidation. The supporting layer covered only parts of the channel layer where the access holes would be punched for the inlets and outlet of the fluid. The PDMS chip (including both layers) was peeled off from the master. Glass slides were cleaned in a basic solution $\mathrm { ( H _ { 2 } O \colon N H _ { 4 } O H ~ ( 2 7 \% ) : H _ { 2 } O _ { 2 } ~ ( 3 0 \% ) = 5 { : } l { : } l }$ , volumetric ratio) at $7 5 ^ { \circ } \mathrm { ~ \overset { \circ } { C } ~ }$ for an hour and then rinsed with deionized water and blown dry. The PDMS chip and a clean glass slide were bonded by oxidation using the Telsa coil to form closed channels. The entire structure was baked in an oven at $8 0 ~ ^ { \circ } \mathrm { C }$ for 2 h to enhance adhesion at different interfaces. The width of the microfluidic channels was 150 μm and the depth was 60 μm.

## 2.3 Microfluidic CARS cytometry

Microfluidic CARS measurements were performed by coupling a picosecond laser source and a microfluidic device with a laser-scanning microscope, as shown in Fig. 1(a). The laser source comprised of two mode-locked 5-ps Ti:sapphire lasers (Tsunami, Spectra-Physics, Mountain View, CA) synchronized to each other through an electronic module controller (Lok-to-Clock, Spectra-Physics). Wavelengths of the master and slave lasers were tunable from 690 to 810 nm and from 690 to 1025 nm, respectively. The two parallel-polarized laser beams were collinearly combined and sent into a laser scanning confocal microscope (FV300/IX71, Olympus America, Center Valley, PA). A 20x air objective with a 0.75 numerical aperture (NA) was used to focus the laser beams into a sample for imaging or into a flowing chamber for cytometry. Its axial focal width was determined to be 7.5 μm in full width at half maximum. The focal width was measured as the first derivative of the axial CARS intensity profile at the water/glass interface.

Steady pressure-driven flows were created by a syringe pump (PHD infusion pump, Harvard Apparatus, MA) from inlet A and inlet B (Fig. 1(b)). The flow from inlet A fed beads or cells continuously into the downstream channel to form the core stream. The flows from inlet B provided sheath stream for tapering the core stream by the hydrodynamic focusing effect. A 100 μl syringe (Hamilton, NV) with 1.46 mm inner diameter (ID) was used for core flow introduction. Two 1 ml syringes with 4.65 mm ID were used to provide sheath flow. Flow rate of the core flow was in the range of 1−0.02 μl/min. The average flow speed was from \~39.42 mm/s to \~0.79 mm/s in the downstream channel of the microfluidic chip described above. The microfluidic device was mounted at the observation stage of the inverted microscope. Line-scan mode was operated for the detection of flowing objects. The scanning frequency across a line of the whole field of view (707 μm) was \~200 Hz and could be boosted by decreasing the scanning width in the line-scan mode. The line-scan window covered the flowing sample particles in the hydrodynamically focused core flow.

Backward CARS signal was detected by an external photomultiplier tube (PMT, H7422- 40, Hamamatsu, Japan) detector mounted at the back port of the microscope (Fig. 1(a)). The forward CARS signal was collected by using a 0.55 NA condenser and detected by a PMT (R3896, Hamamatsu, Japan). For detection of flowing particles and cells, the strong and directional CARS signal in the forward channel was used for preview, and the backward channel was used for data acquisition by taking advantage of the lower non-resonant background in epi-detected CARS [12].

![](images/1d6da386aa6d6e7b0fac05d78738f66e80b7b49063f878191cd3b0113f8c0362.jpg)

<details>
<summary>text_image</summary>

a
Tubings
Supporting layer
Channel layer
Glass
Fluidic Chip
Obj.
Z
Condenser
PMT 1
PMT 2
b
A
B
90 µm
ωp
ωs
Combiner
D.M.
Scanner
Tubing
Syringes
Syringe Pump
C
Normalized Int. (a.u.)
2000 2200 2400 2600 2800 Raman Shift (cm⁻¹)
90 µm
</details>

Fig. 1. Schematic diagram of CARS cytometry and imaging illustration of the hydrodynamic focusing effect. (a) Schematic of microfluidic CARS cytometry. The blowup inset shows layers of microfluidic chip providing function of hydrodynamic focusing for cytometry analysis. The schematic drawings are not to scale. D.M=dichroic mirror; Obj=objective. (b) Hydrodynamic focusing effect examined by forward CARS imaging of $\mathrm { D } _ { 2 } \mathrm { O }$ injected as the core flow (red) from inlet A, and backward TPEF imaging of fluorescent microspheres in the sheath flow (green) injected from inlet B. The bar over the core flow indicates the line-scan window. (c) CARS spectrum of D2O measured by tuning the frequency of the slave laser from 11300 to 12085 cm−1 . The peak is located around 2350 cm−1 . (d) Transmission image showing 2 μm beads in the core around the flow impinging area in a microfluidic chip. Arrows show the flow directions.

Signals were analyzed by the FlowView software (Olympus America, Center Valley, PA). Pixels of intensity lower than 10% of the highest signal were set to zero. Statistical analysis of particle size and intensity was carried out on a MATLAB 7.0 platform.

For CARS imaging and scanning of PS beads and adipocytes, the master laser beam was tuned $\mathrm { t o \sim 1 4 1 4 0 c m ^ { - 1 } \Gamma ( \mathfrak { \omega } _ { p } ) }$ and the slave laser beam was tuned $\mathrm { { t o \sim 1 1 3 0 0 c m } ^ { - 1 } ( \mathfrak { \omega } \mathfrak { o } _ { s } ) } .$ , generating a frequency difference of ${ \sim } 2 8 4 0 ~ \mathrm { c m } ^ { - 1 }$ that matches the symmetric $\mathrm { C H } _ { 2 }$ stretch vibration [8, 13]. The slave laser beam was tuned $\mathrm { { t o \sim 1 1 7 9 0 ~ c m ^ { - 1 } ~ ( { \mathfrak { \omega } } { \mathfrak { o } } _ { s } ) } }$ for imaging $\mathrm { D } _ { 2 } \mathrm { O }$ at vibrational resonance of ${ \sim } 2 3 5 0 ~ \mathrm { c m } ^ { - 1 }$ . Bandpass filters (600/65 nm, Ealing Catalog, Rocklin, CA) were used to transmit the CARS signal. The average powers of the master and slave laser beams were attenuated by using neutral-density filter wheels to 90 mW and 45 mW at the sample. There was no noticeable photo-damage to the samples. The PMT gain value was set identically for experiments.

For demonstration of hydrodynamic focusing, forward CARS from $\mathbf { D } _ { 2 } \mathbf { O }$ in the core stream and backward two photon excited fluorescence (TPEF) signal from 40-nm spheres (Polymer Microsphere G40, Duke Scientific, CA) were recorded simultaneously. The backward TPEF signal was filtered with two bandpass filters (hp520/40m-2p, Chroma) and probed by the PMT at the back port of the microscope.

## 3. Experimental results

We first examined the hydrodynamic focusing in the flow chamber by using D2O as the core flow and the solution of fluorescent nano-particles as the sheath flow (Fig. 1(b)). By forward CARS imaging of $\mathrm { D } _ { 2 } \mathrm { O }$ at the beating frequency of 2350 cm−1 (Fig. 1(c)) and backward TPEF imaging of fluorescent particles, the core and sheath streams were visualized simultaneously. As shown in Fig. 1(b), the core flow was focused into a single file along the center of the chamber. The hydro-focusing effect formed a stable (\~6 μm wide) stream that constrained the flow region of particles (Fig. 1(d)) and provided a well-defined observation area for the cytometry experiments.

A key difference of CARS from one-photon fluorescence lies in that efficient CARS signal generation necessitates tight focusing, particularly in the collinear beam geometry [14]. Thus, two key issues have to be addressed to make CARS flow cytometry a valid technique. First, is it possible to minimize the signal fluctuations induced by out-of-focusing of the flowing objects? Second, can the scan speed be sufficient for volumetric detection of each flowing object? In our experiment, PS beads with well-defined size distributions were used to address these issues.

![](images/f1dbf1ffe14415ff9731202e76aa9045e3c853019bfb63ffcbf379d8e728dd39.jpg)

<details>
<summary>line chart</summary>

| S/F Ratio | Mean Size (µm) |
| --------- | -------------- |
| 0.00      | 6.5            |
| 0.04      | 10.5           |
| 0.08      | 10.5           |
| 0.20      | 10.5           |
</details>

![](images/bd067ebcad0aab6be106eee1524efd4e9d2b0862b4a86b577fe94d35c69faffa.jpg)

<details>
<summary>line chart</summary>

| S/F Ratio | Mean Size (µm) |
| --------- | -------------- |
| 0.00      | 1.8            |
| 0.04      | 2.1            |
| 0.08      | 2.1            |
| 0.20      | 2.2            |
</details>

![](images/7d44efd953c87b86d958d168e86c6995f707dcfe5c03ce1fd12e10315b66ff60.jpg)

<details>
<summary>line chart</summary>

| S/F Ratio | Mean Intensity (a.u.) |
| --------- | --------------------- |
| 0.00      | 900                   |
| 0.02      | 1000                  |
| 0.04      | 1500                  |
| 0.08      | 1600                  |
| 0.20      | 1800                  |
</details>

![](images/a06119a0e9a212204771fc285dbcf31015f94d5a819348c46b81c1d0006b2fbe.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Intensity (a.u.) |
| -------- | ---------------- |
| 22.3     | ~1500            |
| 22.4     | ~1500            |
| 22.5     | ~1500            |
| 22.7     | ~1500            |
| 22.8     | ~1500            |
</details>

Fig. 2. Variations of bead size and signal intensity correlated to S/F ratio. (a) S/F ratio versus mean size of 10 μm PS beads. As increasing the S/F ratio, size variation was reduced and the mean size was closer to the true value. (b) S/F ratio versus mean size of 2 μm PS beads. The size variation mainly resulted from the unmatched channel depth. The insets tagged A, B, and C in (a) and (b) are the time-stack CARS images (\~160 ms) relative to the S/F ratio shown in the plots. Time-stack CARS images were obtained by signaling along the fixed 1-D scan window of \~34 μm. Arrows besides inset C indicate the direction of time flow. (c) S/F ratio versus mean signal intensity of 10 μm PS beads. (d) Signal history of 10 μm PS beads within 1 ms. The signal trace was obtained by setting the S/F ratio to be 0.203. All CARS signals were backward detected.

We have optimized several parameters to ensure that the flowing objects stay in the axial focal region. First, the chamber height was chosen to be 60 μm to maximally constrain the flow volume without clogging of beads. Second, a 20x air objective with an axial focal width of 7.5 μm was used. Third, the flow speed was kept below 40 mm/s to minimize the axial tumbling so that the objects were flowing at a certain height within the chamber. In our experiment, the focal depth was defined by maximizing the CARS signal from the beads. To ensure detection of all flowing objects laterally, line scanning across the core flow was employed.

To ensure volumetric detection, we have optimized an important parameter, scan speed to mean flow speed ratio (S/F) to produce the correct size information. The scanning speed (m/s) was the product of the line-scan frequency multiplied by the pixel dimension of the scanning line, and the mean flow speed (m/s) was the result of the total volume flow rate per second divided by the cross-section of the observation channel (150 μm x 60 μm). The S/F ratio represents the coverage of particles in the line-scanning process.

Figure 2 shows the measurements of PS beads using the CARS signals from CH vibration. For 10 μm PS beads, size variation decreased with increasing the S/F ratio (Fig. 2(a)), and the mean size of the beads approached to the value provided by the vendor (9.775 μm) when operating with an S/F ratio higher than 0.04. On the contrary, there was no prominent change in the size variation of 2 μm beads as the S/F ratio increased (Fig. 2(b)), possibly due to the axial tumbling of these smaller beads. At the scan speed of 0.16 mm/s and flow speed of 0.79 mm/s $( \mathrm { S } / \mathrm { F } = 0 . 2 0 )$ , the SD for 10 μm and 2 μm beads were 0.51 μm and 0.17 μm, respectively. Variation value of 10 μm beads was comparable to the SD of its diameter. The relatively larger variation value of 2 μm beads could be due to the axial tumbling as described above. The insets in Figs. 2(a) and 2(b) which are tagged correspondingly to the S/F ratios are XT images within a flow time of 160 ms. The PS beads gave the vibrational signal in time stack images. Furthermore, peak intensities of the signal from beads were retrieved on the MATLAB platform. The means and SDs of the peak intensity at different S/F ratios were shown in Fig. 2(c). It was found that higher S/F ratio provided lower intensity variation. A stable signal trace of PS beads was obtained when the SF ratio is set as 0.2 (Fig. 2(d)). These measurements provided the information about viable S/F ratios that allowed reliable measurement of particles at the order of 10 μm in diameter. Accordingly, the possible throughput for 10 um beads could be around 100 particles per second with the S/F ratio of 0.2.

a  
![](images/87a62847527091f5e8e9bc7d343c682254ef9731e181d5ce54d46f6021bcddbc.jpg)

<details>
<summary>natural_image</summary>

Black and white image showing vertical elongated patterns with a downward arrow in the top-left corner (no text or symbols)
</details>

b  
![](images/d12b94e5763c83e42e555576502ded832ee1fedeac436b1da349818a5ba6563a.jpg)

<details>
<summary>histogram</summary>

| Size (μm) | Counts |
| --------- | ------ |
| 4         | 8      |
| 5         | 45     |
| 6         | 90     |
| 7         | 25     |
| 8         | 2      |
| 9         | 8      |
| 10        | 15     |
| 11        | 10     |
| 12        | 12     |
</details>

Fig. 3. Population distribution of size mixed PS beads verified by microfluidic CARS cytometry. (a) A typical time-stack CARS image (\~600 ms) obtained by signaling along the 1- D scan window of \~34 μm for population analysis. The arrow indicates the direction of time flow. (b) Bead counts versus size of a solution mixed with 5 μm and 10 μm beads. The S/F ratio was set \~0.2.

Analysis of population distribution was demonstrated by using a mixture of 5 μm and 10 μm PS beads. Total sampling time was about 50 seconds with a 0.2 S/F ratio. A typical timestack image was shown in Fig. 3(a). Counts of the two populations were shown in Fig. 3(b). Two groups of beads were clearly identified by analyzing the time-stack images. The average diameters were and 5.05 μm and 10.47 μm, and SD were 0.38 and 0.81, respectively. The relatively large average value and the broader size distribution for the group of 10 μm beads could arise from the conjoining of PS beads that was also observed by imaging (data not shown).

As an application of CARS cytometry to quantitative cell analysis, adipocytes isolated from mouse fat tissues were injected into core flow. The S/F ratio was set \~0.2 in the experiment. The size distribution of adipocytes was resolved by CARS cytometry and analyzed by the program on MATLAB platform. The result is shown in Fig. 4(a). A broad size distribution was observed and the major cell size was in the bin of 15 to 25 μm. The size information was also retrieved by CARS imaging of adipocytes and analysis with the same criteria in background and size determination. The result shown in Fig. 4(b) affirmed the size distribution analyzed by CARS cytometry.

![](images/aadc7278b926a02469d7bb9537bf307497d987a7cda27880bc3c69638dafdf51.jpg)  
Fig. 4. Size population of adipocytes verified by microfluidic CARS cytometry. (a) Size distribution of isolated adipocytes retrieved from time stack images of CARS cytometry. The S/F ratio was set \~0.2. (b) Size distribution of isolated adipocytes obtained by analyzing 8 CARS images for microscopic-based cytometry. Size analyses were obtained by using a program developed on MATLAB platform. The inset in (b) shows a backward-detected CARS image of purified adipocytes from mouse fat tissues. Bar= 30 μm.

## 4. Discussion

The current study reports the development of CARS cytometry by integrating a laser-scanning CARS microscope with a microfluidic device. PS beads were utilized for proving the concept of CARS cytometry and determining adequate range of experimental parameters. With isolated adipocytes from mouse fat tissues, the population distributions elucidate the capability of CARS cytometry for cell counting and size measurement based on the CH2 vibrational signal. The CARS signal provides the capability of chemical selective scanning in a label-free manner that could avoid the cell-to-cell variation of fluorescent or signal agent labeling. The vibrational signal generated at the beating frequency of $\mathrm { C H } _ { 2 }$ rendered high signal-to-noise ratio as injecting PS beads or adipocytes into the core stream for flow cytometry analysis.

In our experiment, the CARS signal was generated in the focal volume of tightly focused laser beams and the observation window for cytometry was formed by line-scanning. The pixel-by-pixel line-scanning provided the potential of identifying 2-D morphology of each object, particularly when the scanning speed can be technically boosted up to beat the flow speed. Advanced scanning methods by using resonance mirror [15] or polygon mirror [16] could effectively increase the line-scanning speed and improve the object counting efficiency.

While soft lithography allows efficient and cost-effective way for testing and development, PDMS channel could generate strong nonresonance background in CARS signaling once excitation focal volume approaches wall layers. Channel depth of 60 μm was set to circumvent the adverse effect, but it compromised the signal stability when small particles were probed. With the constructions of 3-D hydrodynamic focusing [3], signal from small particles could be more reliable. Furthermore, by changing the material of microfluidic devices [17], nonresonance background would be relaxed.

Although we used line-scanning of tightly focused laser beams on a microscope platform, CARS flow cytometry is possible with static laser beams in a non-collinear beam geometry. In such case, the CARS signal would be detected in the phase-matching condition and spatially separated from the excitation beams. This strategy could allow the corporation of CARS into a commercial flow cytometer to realize high-throughput analysis.

Microfluidic CARS cytometry analysis of single cells could open a new modality in the technology of microfluidics. With the demonstration of multimodal NLO imaging on a CARS microscope [18, 19], it is foreseeable that multiparameter analysis for different components within the same cell could be achieved by taking the advantages of acquiring NLO signals, e.g. CARS and TPEF, on the same platform.

In conclusion, we demonstrated CARS cytometry by the combination of a microfluidic device with a CARS microscope. Soft-lithographic microfluidic devices that allowed the capacity for efficient design-fabrication cycle time provided the possibility of higher throughput than microscope-based cytometry. In addition to the proof-of-concept examination with polystyrene (PS) beads, CARS cytometry was demonstrated by using isolated adipocytes from mice fat tissues. The information shows the capacity of microfluidic CARS cytometry for the studies of adipogenesis and metabolic disorders of lipid, and heralds the potential of CARS application for high throughput cell population and property measurement in a labelfree manner with chemical selectivity.

## Acknowledgment

The authors cordially thank Alan P. Kennedy and Fen Wang for their participation in experiments, and Wei He for helps in programming. This work was supported by a NIH R01 grant #EB007243 to JXC and Wallace H. Coulter Foundation Early Career Award to CL.