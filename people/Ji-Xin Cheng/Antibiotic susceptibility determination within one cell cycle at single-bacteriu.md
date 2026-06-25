# Antibiotic Susceptibility Determination within One Cell Cycle at Single-Bacterium Level by Stimulated Raman Metabolic Imaging

Weili Hong,† Caroline W. Karanja,‡ Nader S. Abutaleb,§ Waleed Younis, § Xueyong Zhang, 7+ Mohamed N. Seleem,\*,§ and Ji-Xin Cheng\*,†,‡,⧫

† Weldon School of Biomedical Engineering, ‡ Department of Chemistry, and § Department of Comparative Pathobiology, Purdue University, West Lafayette, Indiana 47907, United States

⧫Department of Biomedical Engineering and Department of Electrical and Chemical Engineering, Boston University, Boston, Massachusetts 02215, United States

\*S Supporting Information

ABSTRACT: The widespread use of antibiotics has significantly increased the number of resistant bacteria, which has also increased the urgency of rapid bacterial detection and profiling their antibiotic response. Current clinical methods for antibiotic susceptibility testing (AST) rely on culture and require at least 16 to 24 h to conduct. Therefore, there is an urgent need for a rapid method that can test the susceptibility of bacteria in a culture-free manner. Here we demonstrate a rapid AST method by monitoring the glucose metabolic activity of live bacteria at the single-cell level with hyperspectral stimulated Raman scattering (SRS) imaging. Using vancomycinsusceptible and -resistant enterococci E. faecalis as models, we demonstrate that the metabolic uptake of deuterated glucose in a single living bacterium can be quantitatively monitored via hyper spectral SRS imaging. Remarkably, the metabolic activity of susceptible

bacteria responds differently to antibiotics from the resistant strain within only 0.5 h from the addition of antibiotics. Therefore, bacterial susceptibility and the minimum inhibitory concentration (MIC) of antibiotics can be determined within one cell cycle. Our metabolic imaging method is applicable to other bacteria species including E. coli, K. Pneumoniae, and S. aureus as well as different antibiotics, regardless of their mechanisms of inhibiting or killing bacteria.

![](images/837f03f5fdbb18d78a04e8d677a29a75d3ec1b4c2b1017f48ba7a730cb5fdc08.jpg)

<details>
<summary>line chart</summary>

| Antibiotic Condition | Raman Shift (cm⁻¹) | Intensity (a.u.) |
|----------------------|--------------------|------------------|
| No antibiotics        | ~2100              | ~1.2             |
| 20 µg/ml vancomycin | ~2150              | ~1.1             |
| No antibiotics        | ~2200              | ~0.8             |
| 20 µg/ml vancomycin | ~2250              | ~0.6             |
| No antibiotics        | ~2300              | ~0.4             |
| 20 µg/ml vancomycin | ~2350              | ~0.2             |
</details>

has become a growing global threat due to the misuse and overuse of antibiotics.1 In order to combat infections, it is essential to detect and characterize bacterial susceptibility to antibiotics in the early stages of infections to reduce the inappropriate use of antibiotics and the death rate.2,3 Conventional methods for antibiotic susceptibility testing (AST), such as agar plates and broth dilution assays, are based on culture and require at least 16 to 24 h to conduct.4,5 A few new techniques, including matrix-assisted laser desorption ionization time-of-flight mass spectrometry (MALDI-TOF MS),6,7 polymerase chain reaction (PCR),8 DNA microarray,8 and bacteria vibration measurement by cantilevers9,10 have been developed for rapid AST of bacteria. While these techniques are powerful AST tools that reduce the detection time to a few hours or less, they still have limitations. Some work for specific bacteria species only or require sample enrichment, which can be time-consuming and does not work for fastidious bacteria. Imaging-based approaches,11,12 including single-cell morphological analysis by monitoring bacterial morphological changes in response to antibiotic exposure11 and a microfluidic agarose channel system by tracking cell growth13 with microscopic imaging, work at the single-cell level and reduce the AST time to 1 to 3 h. However, these methods still rely on cell growth and do not work for nongrowing but metabolically active bacteria, which are responsible for recurrent infections.14

Raman spectroscopy, a label-free technique that measures molecular vibration, has been employed for rapid bacterial AST. Raman peaks in the fingerprint region15 or the uptake of heavy water D O16,17 have been used as spectroscopic markers to characterize the response of bacteria to antibiotic or antiseptic drug treatment. While these methods significantly reduced bacterial AST to a few hours, they still have significant drawbacks. Raman spectroscopy has low sensitivity due to the inefficiency of the Raman scattering process;1 thus, it requires large amount of samples or long integral time per cell to obtain the Raman signal. More importantly, it is very challenging for these methods to work on most clinical and environmental samples, in which bacteria are usually surrounded by different substrates that could interfere with the bacterial Raman signal. One way to enhance the Raman signal is with surface-enhanced Raman spectroscopy (SERS). Using metal colloids or rough

Received: August 20, 2017

Accepted: February 20, 2018

Published: February 20, 2018

metal surface, SERS has been used for rapid AST based on the Raman peak change with antibiotic treatment;19 however, SERS requires substrates, and the signals vary too much for practical applications.

Coherent Raman scattering microscopy, an emerging molecular imaging technique,20,21 including coherent anti-Stokes Raman scattering (CARS)22,23 and stimulated Raman scattering (SRS) microscopy,24−27 offers significant signal improvement over spontaneous Raman. In previous work, we demonstrated the detection of bacteria at the single-cell level in complex environments with hyperspectral CARS microscopy.28 SRS, unlike CARS, does not suffer from the nonresonant background, and has been used for metabolic imaging in cells,18,29,30 tissues,31 and model organisms.32 However, SRS is not completely background-free. Hyperspectral SRS,33 which records a spectrum at each pixel, has been developed to distinguish the SRS signal from the background induced by nonlinear absorption and cross-phase modulation.34

Here, we demonstrate a rapid AST method, by monitoring the glucose metabolic activity of live bacteria at the single-cell level with hyperspectral SRS imaging. We chose glucose, because it is the preferred carbon source for most bacteria growth.35 Using vancomycin-susceptible enterococci (VSE) and vancomycin-resistant enterococci (VRE) as models, we show that bacteria can be detected, and their metabolic activity can be quantitatively monitored at the single-cell level by SRS imaging. Bacterial susceptibility and minimum inhibitory concentration (MIC) can be determined within 0.5 h by monitoring their metabolic response to antibiotic treatment. In addition, we demonstrate that our metabolic imaging method works for other antibiotics, regardless of their mechanism of inhibiting or killing bacteria, and is applicable to various bacteria species including E. coli, K. pneumoniae, and S. aureus.

## EXPERIMENTAL SECTION

Hyperspectral SRS Setup. Our hyperspectral SRS imaging setup is illustrated in Supplementary Figure S1. A dual output femtosecond pulse laser (InSight DeepSee, Spectra-Physics) with a repetition rate of 80 MHz was employed for hyperspectral SRS imaging. To image at the C−D vibration region, the 120 fs tunable laser (yellow line in Figure S1) was tuned to 847 nm and served as the pump beam. The 220 fs laser (red line in Figure S1) centered at 1040 nm served as the Stokes beam and was modulated by an acousto-optical modulator (AOM, 1205-C, Isomet) at 2.35 MHz. A motorized translational stage (T-LS28E, Zaber) was installed in the pump path to tune the delay between the pump and Stokes beams. After the combiner, both beams were chirped with two 15 cm long SF57 glass rods. After chirping, the pump and Stokes pulse durations were 1.9 and 1.3 ps, respectively. The pump and Stokes beams were directed into a custom-built laser scanning microscope. A 60× water objective (NA = 1.2, UPlanApo/IR, Olympus) was used to focus the lasers on the sample, and an oil condenser (NA = 1.4, U-AAC, Olympus) was used to collect the laser from the sample. Two filters (HQ825/150m, Chroma) were used to filter out the Stokes beam, the pump beam was detected by a photodiode ((S3994−01, Hamamatsu), and the pump beam loss signal was extracted by a lock-in amplifier (HF2LI, Zurich Instrument).

Sample Preparation. E. faecalis 31970, E. faecalis 31972, S. aureus, E. coli 35150, or K. pneumoniae 2146 were cultivated in LB (LB broth, Sigma-Aldrich) or TSB (tryptic soy broth, Sigma-Aldrich) for 2 h to reach to log phase, and then, the bacteria were diluted in a 1:100 ratio to 2 mL of M9 medium supplemented with 2% glucose or glucose-d . After 0.5, 1, or 3 h of incubation, 500 μL of each sample was centrifuged, washed twice with purified water, and deposited to an agarose gel pad. To prepare the agarose gel pad, 1% in weight agarose powder was added to 2 mL of purified water in a plastic tube, and then, the tube was heated in a microwave for about 20 s until the agarose powder was completely melted. About 10 μL of heated agarose gel solution was added to a cover glass by a pipet, and another cover glass was immediately put on the top of the agarose gel solution to make it flat. After about 2 min, one cover glass could be removed from the agarose gel by sliding the two cover glasses.

MIC Determination from Culture-Based Method. MICs of antibiotics, tested against isolates of E. faecalis, S. aureus, E. coli, and K. pneumoniae, were determined using the broth microdilution assay in accordance with the Clinical and Laboratory Standards Institute guidelines. Bacteria were cultured in LB or TSB in a 96-well plate. Antibiotics, using triplicate samples, were added to the plate and serially diluted. Plates were incubated at 37 °C for at least 20 h prior to determine the MIC. Plates were visually inspected, and the MIC was categorized as the concentration at which no visible growth of bacteria was observed.

MCR Analysis. We used the same MCR analysis procedure that was described in a previous paper.28 In brief, MCR is a bilinear model that decomposes the experimental data matrix that contains a spectrum at each pixel into concentration maps and spectra of principle components. With an initial estimated spectrum of each component as the input, MCR is calculated and optimized iteratively using an alternating least-squares algorithm until convergence is reached. The output of MCR contains the concentration map and a spectrum of each component.

## RESULTS AND DISCUSSION

Although the detection of a single bacterium was previously demonstrated with CARS microscopy in the C−H vibrational region,28 imaging the metabolic activity of a single bacterium remains highly challenging. The bacterium (∼1 μm in diameter) is much smaller than that of a mammalian cell (∼10 μm) and close to the spatial resolution of CARS or SRS microscopy. Moreover, the C−D Raman signal is much weaker than the C−H signal.29 To overcome these challenges, we developed a new sample preparation strategy, improved the bacterial culture medium, and optimized our hyperspectral SRS setup (Figure S1) to maximize the signal-to-noise ratio (SNR). Specifically, we first prepared samples for SRS imaging by drying the bacteria on glass, as is done in Raman measurement,16,36 but found a strong background (Figure S2a), possibly due to the cross-phase modulation.34,37 We then developed an agarose gel pad (details can be found in the Experimental Section) and deposited bacteria in solution on the gel pad for live bacteria imaging. We found this sample preparation significantly reduced the background in SRS imaging (Figure S2b). To maximize the C−D signal level, we replaced the LB medium, which contains normal glucose, with custom-made M9 medium, in which glucose-d is the only carbon source. We also increased the glucose-d concentration to 2%. To ensure signal and spectral resolution, we adopted a two-rod setup (Figure S1), using two 15 cm SF57 glass rods to chirp the pump and Stokes beams for the hyperspectral SRS imaging, and achieved an SNR of 5 for a single bacterium at the C−D vibrational region, with a spectral resolution of ${ \sim } 2 0 ~ \mathrm { c m ^ { - 1 } }$ .

Toxicity Test. Glucose-d has been used for the visualization of de novo lipogenesis in mammalian cells and showed no toxicity to mammalian cells.29 To test the toxicity of glucose-d to bacteria, E. faecalis 31970 (VSE) and E. faecalis 31972 (VRE) were cultivated in custom-made M9 medium, one with normal glucose for control and the other with glucose-$d _ { 7 } .$ The bacterial growth was monitored with optical density (OD) measurement at 600 nm for 22 h (Figure S3). Similar growth curves were observed for both E. faecalis 31970 and E. faecalis 31972 cultivated in control and glucose-d medium (Figure S3), indicating no toxicity of glucose-d to bacterial growth.

Glucose-d Incorporation. To test the feasibility of assessing bacterial metabolic activity via SRS imaging, we cultivated E. faecalis in the normal glucose and glucose-d medium overnight, and then washed them in PBS to remove traces of the culture and deposited them on agarose gel pads for SRS imaging. Hyperspectral SRS imaging of 1 M glucose- $\cdot d _ { 7 }$ solution (Figure S4a) shows a peak around 2130 cm−1 from the C−D vibration modes. This peak lies in the cell silent region of the Raman spectrum, providing an excellent contrast for imaging the metabolic incorporation of the deuterium labeled metabolite. SRS imaging of bacteria cultivated in the glucose- $\cdot d _ { 7 }$ medium show a strong signal in the C−D vibrational region (Figure S 4d), indicating successful incorporation of glucose-d . Glucose-d incorporated into bacteria may be present in the free form or used for biomass synthesis. The C−D signal we detected includes both the free form glucose-d and the biomass that has the C−D bond. No signal was observed for bacteria cultivated in the normal glucose medium (Figure S4c). We further confirmed these results with spontaneous Raman measurement (Figure S5), where a peak in the C−D region was observed for bacteria cultivated in the glucose- $\cdot d _ { 7 }$ medium only. These data collectively demonstrated that the metabolic activity of glucose-d incorporation into bacteria can be monitored by hyperspectral SRS imaging at the single-cell level.

Antibiotic Susceptibility Determination within One Cell Cycle. Next, we examined the influence of antibiotics on the metabolic incorporation of glucose-d by bacteria. VSE and VRE were first grown to log phase by cultivation in the LB medium for 2 h, and then, VSE and VRE were further cultivated in the M9 medium with 2% glucose-d as the sole carbon source, with and without the addition of vancomycin to a final concentration of 20 μg/mL (Figure 1a).

This concentration was chosen because it is between the MICs of vancomycin to VSE (MIC is 1 μg/mL) and VRE (MIC is >128 μg/mL). To test whether VSE can be killed by vancomycin at this concentration, a time-kill assay was performed for VSE without and with the treatment of 20 μg/ mL vancomycin (Figure S10). Bacteria counts with the treatment did not decrease significantly for up to 6 h, indicating 20 μg/mL vancomycin did not kill VSE within 6 h. For the control, VSE and VRE were cultivated in glucose- $\cdot d _ { 7 }$ medium without the addition of vancomycin (Figure 1a). After 0.5 to 3 h of cultivation, each sample was centrifuged, washed twice in PBS, and then deposited on an agarose gel pad for SRS imaging. Figure 1b shows the SRS imaging at the C−D vibrational region $( { \sim } 2 1 7 8 \ \mathrm { c m } ^ { - 1 } )$ for VSE and VRE cultivated in the glucose-d medium for 0.5 h, with and without the addition of vancomycin. In the control group, both VSE and VRE have C−D signal, indicating glucose-d incorporation into the bacteria. Moreover, individual bacterium can be clearly observed. In the vancomycin treated group, a reduction of the C−D intensity was observed for VSE. To quantify the change of C−D intensity for bacteria with antibiotic treatment, Student’s t-test was used to compare the average C−D intensity for bacterial cells in the control and treated group. The average C−D intensity for the treated VSE has been reduced to about 1/2 of the average C−D intensity for VSE in the control group (Figure 1e); this reduction is significant statistically (p-value < 0.001). Since the SRS signal intensity of glucose-d is proportional to its concentration,29 the reduced signal intensity indicates less glucose-d incorporation. On the contrary, the average C−D intensity for VRE is similar to that of the control group (p-value = 0.15) (Figure 1e). Figure 1c,d shows the corresponding normalized SRS spectra of VSE and VRE shown in Figure 1b. These results indicate that the glucose-d incorporation of VSE and VRE responds differently to vancomycin treatment, and the susceptibility of VSE and VRE can be determined within 0.5 h, close to one cell cycle for enterococci (doubling time of 26 min38). Similar effects were observed for 1 h (Figure S6) and 3 h (Figure S7) of vancomycin treatment. Accordingly, the AST of E. faecalis with our metabolic imaging method is not time sensitive.

![](images/963e29f4e62933e319e1115018c1b83a28fb2d536276d18df5e32029f3e4fa2c.jpg)  
Figure 1. Determination of antibiotic susceptibility within 0.5 h by hyperspectral SRS imaging. (a) Experimental procedure for AST by SRS imaging of glucose metabolism in bacteria. (b) SRS images at $\mathrm { C } -$ D vibrational region (2178 cm−1 ) for VSE and VRE with and without 20 μg/mL vancomycin treatment. (c,d) Corresponding SRS spectra for susceptible and resistant bacteria in the field of view. (e) Statistical analysis of average C−D intensity for VSE and VRE with and without 20 μg/mL vancomycin treatment. Data are shown as mean + standard deviation (SD; number of cells > 50). \*\*\* p-value < 0.001.

To quantify the C−D content of the E. faecalis cells, we applied multivariate curve resolution (MCR) analysis39 to retrieve the C−D component from the hyperspectral SRS imaging data (Figure S8). The spectra of glucose- $\cdot d _ { 7 } ,$ representing the C−D component, and gel, representing the background, were used as the input components. After MCR analysis, the C−D component can be clearly separated from the background (Figure S8).

![](images/fac9d0a0511f5f21f776194bb30a6e8508c8b2a001205f1aa421132b609ac069.jpg)

<details>
<summary>text_image</summary>

a
VSE
0.5 h	1 h	3 h
No antibiotics
20 µg/ml
vancomycin
</details>

![](images/f7e501fcc0208c9299894221236b3a9c1c867f3fcfcddebbb70b8d9ceeba3e13.jpg)

<details>
<summary>line chart</summary>

| Time (h) | No antibiotics | 20 µg/ml vancomycin |
| -------- | -------------- | ------------------- |
| 0        | 0.00           | 0.00                |
| 1        | 0.03           | 0.01                |
| 3        | 0.05           | 0.02                |
</details>

![](images/1f57b93afbfa5e6a9e63014f215918e4b194cef39a823f201678d2b6be236426.jpg)

<details>
<summary>text_image</summary>

b
VRE
0.5 h	1 h	3 h
10 µm
</details>

![](images/029161d83c49992280e1f72927aa8a7cc8557aabb133e7d48e85a3da7dc1ad1c.jpg)

<details>
<summary>line chart</summary>

| Time (h) | No antibiotics | 20 µg/ml vancomycin |
| -------- | ------------- | ------------------- |
| 0        | 0.00          | 0.00                |
| 1        | 0.04          | 0.035               |
| 3        | 0.035         | 0.04                |
</details>

Figure 2. Time lapse of C−D component concentration map in bacteria cultivated in glucose-d medium. (a, b) C−D component concentration map in VSE (a) and VRE (b), in the presence and absence of 20 μg/mL vancomycin. (c, d) Quantitation of C−D component intensity change with time for VSE (c) and VRE (d) cultivated in the presence and absence of vancomycin. Error bars indicate standard deviation (SD, number of cells > 30).

Temporal Profile of Glucose Incorporation. Figure 2a,b shows the temporal dynamics of the C−D component after MCR analysis for VSE and VRE, respectively. The average intensity of the C−D component in individual bacterium was quantified and plotted (Figure 2c,d for VSE and VRE, respectively). For VSE in the control without vancomycin treatment, the bacteria cultivated in the glucose-d medium for 0.5 and 1 h has a similar C−D component intensity. The C−D component intensity for 3 h is higher (Figure 2c), indicating a slightly increased glucose-d incorporation over time. For VRE in the control. the C—D component in individual bacterium has a similar intensity from 0.5 to 3 h (Figure 2d). Vancomycin treatment significantly reduced the intensity of the C−D component for VSE. On the contrary, vancomycin treatment did not significantly reduce the intensity of the C−D component in VRE. Interestingly, 3 h of vancomycin treatment of VRE has a higher C−D component intensity than the control group (p-value $= 5 \times 1 0 ^ { - 4 } )$ . This is probably due to the metabolic response of VRE to the treatment of vancomycin, whereby the cells increase their glucose incorporation to combat the antibiotic stress. Our results demonstrate that vancomycin treatment significantly reduced the incorporation of glucose-d in VSE, but did not reduce the incorporation of glucose-d in VRE. Therefore, the susceptibility of VSE and VRE can be rapidly determined.

MIC Determination. We then tested whether MIC, defined as the lowest antibiotic concentration able to inhibit the visible growth of bacteria in vitro, can be determined by our metabolic imaging method. VSE was cultivated in glucose-d M9 medium, with the addition of different concentrated vancomycin. After 1 h of cultivation, each sample was centrifuged, washed twice in PBS, and deposited on an agarose gel pad for SRS imaging. Figure 3a shows the C−D component of each sample after

![](images/061555618b43f88478c5c80a14ba947008d29155bd14dfe082ec844a1ffbecfc.jpg)

<details>
<summary>text_image</summary>

a
0 µg/ml
1 µg/ml
2 µg/ml
3 µg/ml
5 µg/ml
20 µg/ml
10 µm
</details>

![](images/0f81d56744504e257020664b63f512790cce47c2400ef2b29b5a3bb1130dfb69.jpg)

<details>
<summary>bar chart</summary>

| Concentration (μg/ml) | Intensity (a.u.) |
| --------------------- | ---------------- |
| 0                     | 0.07             |
| 1                     | 0.08             |
| 2                     | 0.04             |
| 3                     | 0.04             |
| 5                     | 0.04             |
| 20                    | 0.03             |
</details>

<table><tr><td>Method</td><td>MIC (μg/ml)</td></tr><tr><td>Culture-based</td><td>1</td></tr><tr><td>Metabolic imaging</td><td>2</td></tr></table>

Figure 3. MIC determination by SRS metabolic imaging. (a) C−D component concentration map for bacteria cultivated in glucose-d medium for 1 h at different vancomycin concentrations. (b) Relative C−D component intensity of bacteria in (a). Data are shown as mean + standard deviation (SD; number of cells > 10). \*\*\* p-value < 0.001. (c) Comparison of the MICs determined by the conventional culture based method and the metabolic imaging method.

MCR analysis. To quantitatively compare the change of glucose-d incorporation after vancomycin treatment, the intensity of the C−D component for individual bacterium in the field of view was statistically analyzed using Student’s t-test (Figure 3b). Compared to the control without vancomycin treatment, 2 μg/mL or higher concentrations of vancomycin treatment significantly reduced the intensity of the C−D component. On the contrary, 1 μg/mL vancomycin treatment did not reduce this intensity significantly. Therefore, the MIC for VSE determined by our metabolic imaging method is 2 μg/ mL, which is 2 times the MIC determined by the conventional cultured-based method (Figure 3c). This discrepancy is within the precision range,5 and could be due to the short incubation time (0.5 h) prior to metabolic imaging. In our method, the antibiotics and glucose were added at the same time, whereas it might take some time for the antibiotics to be fully effective. To improve the experimental protocol, it would be better to add the antibiotics first, cultivate for some time, and then add glucose.

Metabolic-Imaging Method for Different Antibiotics. To test whether our metabolic-imaging-based AST method works for other antibiotics, we cultivated clinical isolate E. faecalis 31970 in glucose-d M9 medium with five different antibiotics, vancomycin, linezolid, daptomycin, gentamicin, and erythromycin. These antibiotics are commonly prescribed in clinics for treatment of enterococci infection and have different mechanisms of action. Figure 4a−f shows the SRS images of E.

![](images/4796c134ecb0a11746e54bc816c66fb8dd7b0194a23ceb162eba45742aab3b1d.jpg)  
Figure 4. SRS metabolic imaging to test antibiotic susceptibility of E. faecalis 31970 exposed to different antibiotics. (a−f) SRS images at C− D vibrational region for bacteria cultivated in glucose-d M9 medium for 1 h without the treatment of antibiotic (a) and with the treatment of 20 μg/mL vancomycin (b), linezolid (c), daptomycin (d), gentamicin (e), or erythromycin (f), respectively. (g) Quantitation of C−D bond SRS intensity of bacteria in (a−f). Data are shown as mean + standard deviation (SD; number of cells > 30). \*\*\* p-value < 0.001.

faecalis 31970 after 1 h of cultivation in glucose-d medium without and with the addition of each antibiotic at a final concentration of 20 μg/mL. Student’s t test was used to compare the C−D signal change, and a significant reduction (pvalue < 0.001) was observed for bacteria treated with vancomycin and linezolid only (Figure 4g). Therefore, we conclude that this clinical isolate (E. faecalis 31970) is susceptible to vancomycin and linezolid, but resistant to daptomycin, gentamicin, and erythromycin based on our metabolic imaging method. To confirm this, MICs of these antibiotics to E. faecalis 31970 were determined using the conventional culture-based method (Table S1). The suscept ibility of VSE to these antibiotics is consistent with the results determined by our metabolic imaging method.

Metabolic-Imaging Method for Different Bacteria Species. To verify that the metabolic-imaging-based method works for other bacteria species, we performed the experiment on E. coli, K. pneumoniae, and S. aureus. Figure 5 shows the C− D bond SRS images of E. coli and K. pneumoniae cultured in glucose-d medium for 0.5 h, without and with the treatment of gentamicin, cefotaxime, and amikacin at a final concentration of 20 μg/mL. Remarkably, E. coli with antibiotics treatment shows no C−D signal (Figure 5a), indicating almost no glucose-d incorporation. Bright field transmission images were taken at the same areas to confirm the presence of bacterial cells (Figure 5a,c). Statistical analysis of the SRS imaging shows a significant reduction of E. coli C−D intensity and no significant reduction of K. pneumoniae C−D intensity with the treatment of all antibiotics tested. Therefore, E. coli was determined to be susceptible, and K. pneumoniae was determined to be resistant to gentamicin, cefotaxime, and amikacin using our metabolic imaging method. These results agree with the culture-based method as indicated by the MICs determined by broth microdilution (Tables S2 and S3). For S. aureus, one oxacillin susceptible (MIC: 0.06 μg/mL) and one oxacillin-resistant strain were tested. The incorporation of glucose-d was observed in single bacterium cultivated in glucose-d medium for 0.5 h by SRS imaging (Figure S9b). When bacteria were treated with 1.3 μg/mL oxacillin for 0.5 h, a reduction in the C−D peak was observed for the susceptible strain (Figure S9c), and no significant change was observed in the resistant strain (Figure S9d). Therefore, the susceptibility of S. aureus can be determined. These results collectively show that our metabolic imaging method can determine the antibiotic susceptibility of E. coli, K. pneumoniae, and S. aureus in 0.5 h.

We noticed that some susceptible bacteria, including E. faecalis and S. aureus, still have C−D signal after antibiotic treatment. The reasons could be that (1) antibiotics take longer than 0.5 h to fully inhibit the growth of bacteria, and (2) even when antibiotics inhibit the growth of bacteria, they may not fully inhibit the metabolic activity of bacteria. As long as the reduction is significant, the residual C−D signal should not affect the susceptibility results determined with the metabolic imaging method.

## CONCLUSION

We demonstrated a metabolic imaging method that can determine the susceptibility of live bacteria and the MICs of antibiotics within one cell cycle by monitoring the glucose metabolic activity at the single-cell level. Our method reduces the AST time from at least 16 to 24 h required for the conventional culture-based method to only 0.5 h. The AST at single-bacterium level based on metabolic imaging is especially useful for nonculturable or fastidious bacteria.40,41 Moreover, the metabolic imaging method is applicable to a wide range of bacteria species, including vancomycin-susceptible and -resistant enterococci, E. coli, K. pneumoniae, and S. aureus as well as different antibiotics.

![](images/9086bb749d66b8b01404332754e8615c490aec96f758dfbc4dc35199f8b0280b.jpg)

<details>
<summary>text_image</summary>

a
No antibiotics Gentamicin Cefotaxime Amikacin
2178 cm⁻¹
Transmission
</details>

b

![](images/978a9432e1a92389054c5e1840087cab9c11d038dac498745e184012880bdbc2.jpg)

<details>
<summary>bar chart</summary>

| Group   | Intensity (a.u.) |
| ------- | ---------------- |
| No Ab   | 0.45             |
| Gen     | 0.0              |
| Cef     | 0.0              |
| Ami     | 0.0              |
</details>

![](images/638e6d0f5c6b3a3a69674b1dddaace535b38bed846e2979c47cbecb6a382a984.jpg)

<details>
<summary>natural_image</summary>

Microscopy images showing rod-shaped bacterial cells under different conditions, with scale bar indicating 10 μm (no text or symbols present)
</details>

d  
![](images/7dcf1a65da2545f825d6d50d4b29f1553436eefdfd31fd030595d2f459a2c2a4.jpg)

<details>
<summary>bar chart</summary>

| Group | Intensity (a.u.) |
|-------|------------------|
| No Ab | 0.5              |
| Gen   | 0.5              |
| Cef   | 0.5              |
| Ami   | 0.5              |
</details>

Figure 5. Determination of antibiotic susceptibility for E. coli and K. pneumoniae in 0.5 h by SRS imaging. (a) C−D bond SRS images at 2178 cm−1 (top column) and corresponding transmission images (bottom column) of E. coli cultivated without or with 20 μg/mL gentamicin, cefotaxime, and amikacin for 0.5 h. (b) Quantitation of C−D bond SRS intensity of bacteria in (a). Data are shown as mean + standard deviation (SD; number of cells > 14). \*\*\* p-value < 0.001. (c) C−D bond SRS images at 2178 $\mathrm { c m } ^ { - 1 }$ (top column) and corresponding transmission images (bottom column) of K. pneumoniae cultivated without or with 20 μg/mL gentamicin, cefotaxime, and amikacin for 0.5 h. (d) Quantitation of C−D bond SRS intensity of bacteria in (c). Data are shown as mean + standard deviation (SD; number of cells > 50).

## ASSOCIATED CONTENT

## \*S Supporting Information

The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.analchem.7b03382.

Additional tables and figures as described in the text (PDF)

## AUTHOR INFORMATION

## Corresponding Authors

\*E-mail: jcheng@purdue.edu (J.-X.C.)

\*E-mail: mseleem@purdue.edu (M.N.S.)

## ORCID

Waleed Younis:

Mohamed N. Seleem:

Ji-Xin Cheng: 0000-0002-5607-6683

## Author Contributions

J.X.C., M.N.S., and W.H. conceived the idea. W.H. designed the experiment. W.H., C.W.K., N.S.A., W.Y., and X.Z. conducted the experiment. W.H. analyzed the data. W.H. and J.X.C. cowrote the manuscript. All authors have given approval to the final version of the manuscript.

## Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

This work was supported by a Keck Foundation Science & Engineering Grant and R01GM118471 to J.X.C.

## REFERENCES

(1) O’Neill, J. Tackling Drug-Resistant Infections Globally: Final Report and Reccommendations; Review on Antimicrobial Resistance; 2016.  
(2) Kumar, A.; Roberts, D.; Wood, K. E.; Light, B.; Parrillo, J. E.; Sharma, S.; Suppes, R.; Feinstein, D.; Zanotti, S.; Taiberg, L. Crit. Care Med. 2006, 34, 1589−1596.  
(3) Kollef, M. H. Clin. Infect. Dis. 2008, 47, S3−S13.  
(4) Wiegand, I.; Hilpert, K.; Hancock, R. E. Nat. Protoc. 2008, 3, 163175.  
(5) Barth Reller, L.; Weinstein, M.; Jorgensen, J. H.; Ferraro, M. J. Clin. Infect. Dis. 2009, 49, 1749−1755.  
(6) Hrabak, J.; Chudá ć kovǎ , E.; Walková , R.́ Clin. Microbiol. Rev. 2013, 26, 103−114.  
(7) Sparbier, K.; Schubert, S.; Weller, U.; Boogen, C.; Kostrzewa, M. Journal of clinical microbiology 2012, 50, 927−937.  
(8) Pulido, M. R.; García-Quintanilla, M.; Martín-Peña, R.; Cisneros, J. M.; McConnell, M. J. J. Antimicrob. Chemother. 2013, 68, 2710− 2717.  
(9) Etayash, H.; Khan, M.; Kaur, K.; Thundat, T. Nat. Commun. 2016, 7, 12947.  
(10) Longo, G.; Alonso-Sarduy, L.; Rio, L. M.; Bizzini, A.; Trampuz, A.; Notz, J.; Dietler, G.; Kasas, S. Nat. Nanotechnol. 2013, 8, 522−526.  
(11) Choi, J.; Yoo, J.; Lee, M.; Kim, E.-G.; Lee, J. S.; Lee, S.; Joo, S.; Song, S. H.; Kim, E.-C.; Lee, J. C. Sci. Transl. Med. 2014, 6, 267ra174− 267ra174.  
(12) Choi, J.; Jeong, H. Y.; Lee, G. Y.; Han, S.; Han, S.; Jin, B.; Lim, T.; Kim, S.; Kim, D. Y.; Kim, H. C. Sci. Rep. 2017, 7, 1148.  
(13) Choi, J.; Jung, Y.-G.; Kim, J.; Kim, S.; Jung, Y.; Na, H.; Kwon, S. Lab Chip 2013, 13, 280−287.  
(14) Manina, G.; Dhar, N.; McKinney, J. D. Cell Host Microbe 2015, 17, 32−46.  
(15) Schröder, U.-C.; Beleites, C.; Assmann, C.; Glaser, U.; Hübner, U.; Pfister, W.; Fritzsche, W.; Popp, J.; Neugebauer, U. Sci. Rep. 2015, 5, 8217.  
(16) Tao, Y.; Wang, Y.; Huang, S.; Zhu, P.; Huang, W. E.; Ling, J.; Xu, J. Anal. Chem. 2017, 89, 4108−4115.  
(17) Berry, D.; Mader, E.; Lee, T. K.; Woebken, D.; Wang, Y.; Zhu, D.; Palatinszky, M.; Schintlmeister, A.; Schmid, M. C.; Hanson, B. T. Proc. Natl. Acad. Sci. U. S. A. 2015, 112, E194−E203.  
(18) Fu, D.; Yu, Y.; Folick, A.; Currie, E.; Farese, R. V., Jr; Tsai, T.- H.; Xie, X. S.; Wang, M. C. J. Am. Chem. Soc. 2014, 136, 8820−8828.  
(19) Liu, C.-Y.; Han, Y.-Y.; Shih, P.-H.; Lian, W.-N.; Wang, H.-H.; Lin, C.-H.; Hsueh, P.-R.; Wang, J.-K.; Wang, Y.-L. Sci. Rep. 2016, 6, 23375.  
(20) Cheng, J.-X.; Xie, X. S. Science 2015, 350, aaa8870.  
(21) Min, W.; Freudiger, C. W.; Lu, S.; Xie, X. S. Annu. Rev. Phys. Chem. 2011, 62, 507−530.  
(22) Cheng, J.-X.; Xie, X. S. J. Phys. Chem. B 2004, 108, 827−840.  
(23) Evans, C. L.; Xie, X. S. Annu. Rev. Anal. Chem. 2008, 1, 883− 909.  
(24) Freudiger, C. W.; Min, W.; Saar, B. G.; Lu, S.; Holtom, G. R.; He, C.; Tsai, J. C.; Kang, J. X.; Xie, X. S. Science 2008, 322, 1857− 1861.  
(25) Nandakumar, P.; Kovalev, A.; Volkmer, A. New J. Phys. 2009, 11, 033026.  
(26) Ploetz, E.; Laimgruber, S.; Berner, S.; Zinth, W.; Gilch, P. Appl. Phys. B: Lasers Opt. 2007, 87, 389−393.  
(27) Ozeki, Y.; Kitagawa, Y.; Sumimura, K.; Nishizawa, N.; Umemura, W.; Kajiyama, S. i.; Fukui, K.; Itoh, K. Opt. Express 2010, 18, 13708−13719.  
(28) Hong, W.; Liao, C. S.; Zhao, H.; Younis, W.; Zhang, Y.; Seleem, M. N.; Cheng, J. X. ChemistrySelect 2016, 1, 513−517.  
(29) Li, J.; Cheng, J.-X. Sci. Rep. 2015, 4, 6807.  
(30) Wakisaka, Y.; Suzuki, Y.; Iwata, O.; Nakashima, A.; Ito, T.; Hirose, M.; Domon, R.; Sugawara, M.; Tsumura, N.; Watarai, H. Nature Microbiology 2016, 1, 16124.  
(31) Hu, F.; Chen, Z.; Zhang, L.; Shen, Y.; Wei, L.; Min, W. Angew. Chem. 2015, 127, 9959−9963.  
(32) Wang, P.; Liu, B.; Zhang, D.; Belew, M. Y.; Tissenbaum, H. A.; Cheng, J. X. Angew. Chem., Int. Ed. 2014, 53, 11787−11792.  
(33) Fu, D.; Holtom, G.; Freudiger, C.; Zhang, X.; Xie, X. S. J. Phys. Chem. B 2013, 117, 4634−4640.  
(34) Zhang, D.; Wang, P.; Slipchenko, M. N.; Cheng, J.-X. Acc. Chem. Res. 2014, 47, 2282.  
(35) Görke, B.; Stülke, J. Nat. Rev. Microbiol. 2008, 6, 613−624.  
(36) Stöckel, S.; Meisel, S.; Lorenz, B.; Kloß, S.; Henk, S.; Dees, S.; Richter, E.; Andres, S.; Merker, M.; Labugger, I. Journal of Biophotonics 2017, 10, 727−734.  
(37) Fu, D.; Yang, W.; Xie, X. S. J. Am. Chem. Soc. 2017, 139, 583− 586.  
(38) Siegal-Gaskins, D.; Crosson, S. Biophys. J. 2008, 95, 2063−2072.  
(39) Zhang, D.; Wang, P.; Slipchenko, M. N.; Ben-Amotz, D.; Weiner, A. M.; Cheng, J.-X. Anal. Chem. 2013, 85, 98.  
(40) Didelot, X.; Bowden, R.; Wilson, D. J.; Peto, T. E.; Crook, D. W. Nat. Rev. Genet. 2012, 13, 601−612.  
(41) Masselot, F.; Boulos, A.; Maurin, M.; Rolain, J.; Raoult, D. Antimicrob. Agents Chemother. 2003, 47, 1658−1664.