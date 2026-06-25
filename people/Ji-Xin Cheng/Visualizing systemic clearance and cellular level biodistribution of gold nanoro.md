## Langmuir LLetter

pubs.acs.org/Langmuir

© 2009 American Chemical Society

# Visualizing Systemic Clearance and Cellular Level Biodistribution of Gold Nanorods by Intrinsic Two-Photon Luminescence

Ling Tong,† Wei He,† Yanshu Zhang,§ Wei Zheng,§ and Ji-Xin Cheng\*,†,‡

† Department of Chemistry and ‡ Weldon School of Biomedical Engineering and § School of Health Sciences, Purdue University, West Lafayette, Indiana 47907

Received August 11, 2009. Revised Manuscript Received September 20, 2009

Characterization of systemic performance of gold nanostructures is critical to the advancement of biomedical applications of these nanomaterials as imaging or therapeutic agents. The accuracy of current in vitro methods, however, is limited by interanimal variability. We present a novel method capable of monitoring the pharmacokinetics of PEGylated gold nanorods (GNRs) in the same animal by using intravital two-photon luminescence (TPL) imaging of GNRs flowing through a surface blood vessel. The TPL imaging with high speed and submicrometer resolution allowed for studying the clearance of GNRs as a function of surface coating. PEGylated-GNRs (PEG-NRs) were found to exhibit a biphasic clearance mode, with a significantly prolonged blood residence time for branched poly(ethylene glycol) (PEG) as compared to the linear PEG. With spectral detection to distinguish GNR TPL from tissue autofluorescence, we also mapped the cellular distribution of GNRs in the explanted organs, and found most GNRs resided in the macrophages in liver and spleen.

## Introduction

A wide range of “nanomedicines” including liposomes,1 polymeric micelles,2 quantum dots,3 carbon nanotubes,4 and gold nanostructures (nanospheres,5,6 nanoshells,7 nanocages,8 and nanorods)9,10 have shown exciting potential as drug- and genedelivery carriers, imaging probes, or therapeutic agents. On the basis of the extensive in vitro cellular study, new efforts are being made toward a better understanding of how composition, surface chemistry, and size affect their stability11 and clearance during blood circulation,12-14 interaction with the immunological system,15

\*Corresponding author. E-mail: jcheng@purdue.edu (Ji-Xin Cheng).  
(1) Immordino, M. L.; Dosio, F.; Cattel, L. Int. J. Nanomed. 2006, 1, 297–315. (2) Duncan, R.; Ringsdorf, H.; Satchi-Fainaro, R. Adv. Polym. Sci. 2006, 192, 1–8.  
(3) Alivisatos, A. P. Science 1996, 271, 933–937.  
(4) Kam, N. W. S.; , M.; Wisdom, J. A.; Dai, H. Proc. Natl. Acad. Sci. U.S.A. 2005, 102, 11600–11605.  
(5) Huang, X.; El-Sayed, I. H.; Qian, W.; El-Sayed, M. A. Nano Lett. 2007, 7, 1591–1597.  
(6) Qian, X.; Peng, X.-H.; Ansari, D. O.; Yin-Goen, Q.; Chen, G. Z.; Shin, D. M.; Yang, L.; Young, A. N.; Wang, M. D.; Nie, S. Nat. Biotechnol. 2008, 26, 83–90.  
(7) Hirsch, L. R.; Gobin, A. M.; Lowery, A. R.; Tam, F.; Drezek, R. A.; Halas, N J: West. J. L Ann Biomed. Eng 2006 34. 1522  
(8) Skrabalak, S. E.; Chen, J.; Sun, Y.; Lu, X.; Au, L.; Cobley, C. M.; Xia, Y. Acc. Chem. Res. 2008, in press.  
(9) Murphy, C. J.; Gole, A. M.; Hunyadi, S. E.; Stone, J. W.; Sisco, P. N.; Alkilany. Å : Kinard. B. E · Hankins. P. Chem Commun 2008 5. 544557  
(10) Ling, T.; Qingshan, W.; Alexander, W.; Ji-Xin, C. Photochem. Photobiol. 2009 85(1) 2132  
(11) Chen, H.; Kim, S.; He, W.; Wang, H.; Low, P. S.; Park, K.; Cheng, J.-X.Langmuir 2008, 24, 52135217  
(12) Cherukuri, P.; Gannon, C. J.; Leeuw, T. K.; Schmidt, H. K.; Smalley, R. E.; Curley. S A : Weisman R B Proc Natl Acad Sci, U S A. 2006 103 18882 18886.  
(13) Soo Choi, H.; Liu, W.; Misra, P.; Tanaka, E.; Zimmer, J. P.; Ipe, Itty; Bawendi, B.; Frangioni, M. G.; Renal, J. V. Nat. Biotechnol. 2007, 25, 1165–1170.  
(14) Liu, Z.; Davis, C.; Cai, W.; He, L.; Chen, X.; Dai, H. Proc. Natl. Acad. Sci. U S.4. 2008 105. 14101415  
(15) Dobrovolskaia, M. A.; McNeil, S. E. Nat. Nano 2007, 2(8), 469–478.  
(16) Niidome, T.; Yamagata, M.; Okamoto, Y.; Akiyama, Y.; Takahashi, H.; Kawano, T.; Katayama, Y.; Niidome, Y. J. Controlled Release 2006, 114, 343–347.  
(17) Singh, R.; Pantarotto, D.; Lacerda, L.; Pastorin, G.; Klumpp, C.; Prato, M.; Bianco, A.; Kostarelos, K. Proc. Natl. Acad. Sci. U.S.A. 2006, 103, 3357–3362.  
(18) Schipper, M. L.; Nakayama-Ratchford, N.; Davis, C. R.; Kam, N. W. S.; Chu, P.; Liu, Z.; Sun, X.; Dai, H.; Gambhir, S. S. Nat. Nano 2008, 3, 216–221.

biodistribution,16,17 and toxicity.18 Radiotracers17 or fluorescence labels19 have been used to track nanomedicines in blood and organs. However, these extrinsic conjugates might gradually dissociate or lose activity with time, and possibly change the traits of nanomedicines. More recently, intrinsic near-infrared (NIR) fluorescence12 and Raman spectroscopy14 have been used to investigate the circulation of carbon nanotubes in animals. Inductively coupled plasma mass spectrometry (ICP-MS)16 and atomic absorption spectroscopy (AAS)20 are widely used to measure the biodistribution of gold nanostructures. In these studies, however, blood has to be extracted at each postinjection (p.i.) time point for in vitro measurements, which is cumbersome and incapable of in vivo monitoring the clearance in the same animal. Moreover, these methods lack the spatial resolution to locate individual particles in the blood and organs. Information about the interaction between nanomedicines and specific blood components may be lost during blood extraction and processing. Therefore, new methods that are able to directly track nanostructures in the live animals with high spatial resolution are in dire need to elucidate the real-time systemic behavior of nanomedicines.21

Herein, we demonstrate an intravital imaging method to visualize the clearance of gold nanostructures by their intrinsic multiphoton luminescence.22-24 Compared to dark field and confocal reflectance imaging, multiphoton luminescence is particularly advantageous for imaging gold nanostructures in live animals. First, multiphoton luminescence can be distinguished

(19) Yin, Y.; Chen, D.; Qiao, M.; Wei, X.; Hu, H. J. Controlled Release 2007, 123, 27–38.  
(20) Hainfeld, J. F.; Slatkin, D. N.; Focella, T. M.; Smilowitz, H. M. Br. J. Radiol, 2006, 79(939). 248253  
(21) Sanhai, W. R.; Sakamoto, J. H.; Canady, R.; Ferrari, M. Nat. Nano 2008, 3, 242244.  
(22) Farrer, R. A.; Butterfield, F. L.; Chen, V. W.; Fourkas, J. T. Nano Lett. 2005, 5, 1139–1142.  
(23) Wang, H.; Huff, T. B.; Zweifel, D. A.; He, W.; Low, P. S.; Wei, A.; Cheng, J.-X. Proc. Natl. Acad. Sci. U.S.A. 2005, 102, 15752–15756.  
(24) Park, J.; Estrada, A.; Sharp, K.; Sang, K.; Schwartz, J. A.; Smith, D. K.; Coleman, C.; Payne, J. D.; Korgel, B. A.; Dunn, A. K.; Tunnell, J. W. Opt. Express 2008, 16, 1590–1599.

from tissue autofluorescence based on the specific spectral patterns, thus providing chemical selectivity. Second, multiphoton luminescence can be resolved in the axial direction to provide 3D spatial resolution. Third, the excitation is within the NIR region, a spectral window which permits photons to penetrate biological tissues with relatively high transmittivity. Using PEGylated gold nanorods (GNRs) as an example, we show a biphasic clearance, a depletion kinetics that was not observed in the previous study of carbon nanotubes.12 Compared with linear poly(ethylene glycol) (PEG), branched PEG provides a better protection for GNRs, exhibiting a prolonged blood circulation. By multiphoton luminescence imaging of explanted organs, we further demonstrate that most GNRs depleted from circulation are accumulated in macrophages in the liver and spleen.

## Experimental Section

GNR Preparation and Surface Modification. GNRs were synthesized using AgNO3-assisted seeded growth method in cetyl trimethyltrimethylammonium bromide (CTAB) solution.25,26 The growth was initiated 10-15 min after seed injection, carefully monitored by an UV-vis spectrophotometer (DU-530, Beckman) for the next 5-30 min, and stopped at the desired wavelength with the treatment of Na2S26 $\mathrm { N a } _ { 2 } \mathrm { S } ^ { 2 6 }$ and centrifugation at 10 500 rpm for 10 min. The precipitates were resuspended in milli-Q water, with longitudinal plasmon resonance peak around 770 nm. PEGylation with linear methyl PEG (mPEG) and branched PEG were performed as follows. GNRs were first centrifuged at 11 000 rpm for 6 min to remove the unassociated CTAB and dispersed in milli-Q water. 3 mL GNR solution (0.54 nM) was mixed with 0.5 mL m $\mathrm { \Phi _ { 1 } P E G } _ { 5 \mathrm { k } } – \mathrm { S H }$ (Sigma) or $\mathrm { \Phi _ { 1 } P E G _ { 2 k } } – \mathrm { S H }$ (Rapp Polymere GmbH) aqueous solution (3 μmol, $\mathrm { p H } \sim 9 )$ , kept at room temperature overnight with gentle shaking, and dialyzed (MWCO 6000-8000, Fisher Scientific) for 12 h against milli-Q water. For coating with branched PEG,14 3 mL GNR solution (0.54 nM) was first conjugated with 3 μmol $\mathrm { S H \mathrm { - } P E G _ { 5 k } \mathrm { - } N H _ { 2 } \cdot H C l }$ (Rapp Polymere GmbH) in 0.5 mL aqueous solution (pH 9) with similar procedures to m $\mathrm { P E G } _ { \mathrm { 5 k } ^ { - } } \mathrm { N } \mathrm { \bar { R } s }$ . After dialysis, 1.5 equiv of (Methyl-$\mathrm { \dot { P } E O _ { 1 2 } ) _ { 3 } - P E O _ { 4 } - N H S }$ Ester (Pierce) was added to the above solution in the presence of triethylamine (Sigma) and incubated for 3 h with gentle shaking. Then, acetic anhydride (Sigma) was added to block unreacted $\bar { \mathrm { N H } } _ { 2 }$ groups. Finally, the solution was dialyzed for 12 h to remove the excess reagents. These procedures yielded a stable dispersion of PEGylated GNRs (PEG-NRs). For in vivo study, PEG-NR solution was concentrated by centrifugation at 11 000 rpm for 6 min and redispersed in phosphate buffered saline (PBS). The hydrodynamic diameter and surface charge of PEG-NRs were measured by dynamic light scattering (DLS) and zeta potential, respectively, using ZetaPALS (Brookhaven Instruments Corp.).

In Vitro Two-Photon Luminescence (TPL) Imaging and Microspectroscopy. TPL from GNRs was excited by an femtosecond (fs) Ti:sapphire laser (Maitai HP, Spectra-Physics) with a width of 130 fs and a repetition rate of 80 MHz. The wavelength was tunable from 690 to 1020 nm. The laser beam was directed into a scanning confocal microscope (FV1000/IX81, Olympus America Inc.) and focused onto the sample by a 60 waterimmersion objective (NA = 1.2). The back reflected TPL from GNRs was detected by the internal spectral detector within 500-600 nm. Microspectroscopy was performed by λ scan (spectral scan) using the internal spectral detector with a dichroic mirror (675 dcspxr) in the confocal scanning box and a silver mirror below the objective. In the λ scan, a series of individual images within 400-700 nm was recorded. Each image was detected at a specific emission wavelength. FlowView sorftware (Olympus America Inc.) analyzed the series of images and plotted an emission spectrum from the imaged area.

GNR Injection and Intravital TPL Imaging. Female BALB/c mice aged 6-8 week at the time of experimentation were used for in vivo study. After anesthesia by intraperitoneal injection of ketamine (50 mg/kg) and xylazine (5 mg/kg), an aliquot (100 μL) of concentrated PEG-NR solution (5.2 nM in PBS) was administrated via tail vein. The mouse was immediately placed on a Petri dish with one ear attached to the coverslip. A 40 water-immersion objective $( \mathrm { N A } = 0 . 8 )$ with a working distance of 3.3 mm was used to focus the femtosecond laser beam onto the earlobe. The laser power measured after objective was 42 mW. No photodamage to blood vessels was observed. The TPL signal was detected by the internal spectral detector within 500-600 nm. At least three movies (60 frames, 256 256 pixels/frame) were taken at each p.i. time with a scanning rate of $2 \mu \mathrm { s } / \mathrm { p i x e l } .$ . The same blood vessel or vessels with similar size, depth, and flow rate were monitored. The 60 frames in each movie were stacked in one image for quantitative analysis. The TPL intensity in the blood vesse $\left( I _ { \mathrm { T P L } } \right)$ ) or the perivascular tissue $( I _ { \mathrm { t i s s u e } } )$ was calculated by dividing the total intensity in a vessel or perivascular tissue by the area of the vessel or perivascular tissue, respectively. Mice injected with 100 μL saline solution were used as controls. In the control mice, the autofluorescence from blood $( I _ { \mathrm { b l o o d } } )$ showed the same intensity level as that from perivascular tissues $( I _ { \mathrm { b l o o d } } / I _ { \mathrm { t i s s u e } } = 1 . 0 )$ for all the vessels examined. Therefore, we define the TPL contrast from the GNRs as

$$
I _ {\mathrm{NR}} / I _ {\text { blood }} = \left(I _ {\mathrm{TPL}} - I _ {\text { blood }}\right) / I _ {\text { blood }} = I _ {\mathrm{TPL}} / I _ {\text { tissue }} - 1
$$

where $I _ { \mathrm { T P L } }$ and $I _ { \mathrm { t i s s u e } }$ could be measured simultaneously in the same animal. The TPL contrast, $I _ { \mathrm { N R } } / I _ { \mathrm { b l o o d } } ,$ was used to indicate the blood concentration of GNRs for quantitative pharmacoki netics analysis.

ICP-MS Analysis. 100 μL of m $\mathbf { \Delta } _ { \mathrm { l P E G } _ { 5 \mathrm { k } } - \mathrm { N R } }$ solution (5.2 nM in PBS) was administrated to each BALB/c mouse through tail vein injection. After anesthesia, several hundred microliters of blood was collected from inferior vena cava at 0.5 h, 1 h, 2 h, 4 h, 8 h, 12 h, and 24 h p.i. and mixed well with heparin. All the blood samples were lysed with aqua regia and digested in a closed vessel system using pressure- and temperature-controlled microwave heating. The digested solution was further diluted into 2% aqua regia solution and the gold content in the final solutions was quantitatively analyzed by Element2 ICP mass spectrometer (ThermoFisher) equipped with an Aridus desolvating introduction system (Cetac Technologies). Data were calculated as ppb of gold in 1 mL of blood and normalized by the gold concentration at 0.5 h p.i. Three mice were analyzed for each p.i. time.

Tissue Imaging. Mice were euthanatized 24 h after tail vein injection of GNRs. Organs including liver, kidney, and spleen were explanted and fixed in 4% formalin solution to preserve the tissue architecture. Before imaging, organs were cut into smal pieces by a razor blade and placed in a Petri dish with PBS. The femtosecond laser beam was focused onto the sample by a 60 water objective, with a laser power of 10 mW at sample. The back reflected signals were detected by internal spectral detectors. The microspectroscopy was preformed and analyzed by λ scan (spectral scan) as described above. The images of autofluorescence from liver and TPL from GNRs were simultaneously acquired by one detector within 460-560 nm range and the other detector within 650-700 nm range, separated by a dichroic mirror (SD560). Images were analyzed by FlowView software.

F4/80 Antibody Labeling of Kupffer Cells in Liver. Mice were euthanatized 24 h after tail vein injection of GNRs. Liver was explanted and cut into small pieces, then incubated in Tricolor F4/80 antibody solution (Invitrogen, 1:100) at $4 ~ { } ^ { \circ } \mathrm { C }$ for 4 h and washed with PBS. The fresh liver sample was sequentially imaged by confocal and TPL microscopy to visualize F4/80 antibody and GNRs, respectively. Tricolor-F4/80 antibody was excited by an $\mathrm { A r } ^ { + }$ 488 nm laser and detected by an internal spectral detector within 620-720 nm. Then, the same area was imaged by TPL as described in the Tissue Imaging section.

![](images/a68f5abcfd216c350d8ec7c4a88bd57544b9ea5a1b2caf6d111ca651cd9573e0.jpg)  
Figure 1. Surface modification of GNRs and characterization of TPL from GNRs. (a) Structure of PEG-NRs (linear PEG: 2k and 5k; branched PEG: 7k). (b) TPL emission spectra from CTAB-NR and PEG-NR solution. (c) TPL emission spectra from PEG-NRs in water, PBS, and serum. For b and c, 6 μL of each solution was dropped into a small chamber on a coverslip. TPL was excited at the wavelength of the longitudinal plasmon peak of each sample with the same laser power and photomultiplier tube voltage, and spectra were recorded from the solution with the laser focused at 20 μm above the coverslip. (d) TPL intensity vs PEG-NR concentration in aqueous solution. A linear dependence was observed from 4.7 nM to 0.11 nM.

## Results and Discussion

The surface CTAB on GNRs prepared with a seeded growth method25 was replaced with both linear (MW 2k and 5k) and branched PEG (MW 7k) as shown in Figure 1a. After dialysis, the PEG-NRs were well-dispersed in water, with slight shift of the longitudinal plasmon resonance peaks due to the change of dielectric constant. For example, the longitudinal plasmon resonance peak of $\mathrm { m P E G } _ { 5 \mathrm { k } ^ { - } } \mathrm { N R }$ shifted from 765 to 774 nm after modification (Supporting Information Figure S1). The result was consistent with the theoretical calculation of 9 nm red shift for GNRs with aspect ratio of 3.8 and the effective refractive index of single layer CTAB and PEG as 1.414 and 1.438,27 respectively, based on the spheroid model and electromagnetic theory. Surface charge and hydrodynamic diameter were characterized by zeta potential and DLS, respectively. The results were summarized in Supporting Information Table S1. All the PEG-NRs showed neutral surfaces. Measured by DLS (Supporting Information Figure S2), the hydrodynamic diameter of $\mathrm { m P E G } _ { 2 \mathrm { k } ^ { - } } \mathrm { N R s } ,$ $\operatorname { m P E G } _ { 5 \mathrm { k } ^ { - } } { \mathrm { N R s } } .$ , and branched $\mathrm { P E G } _ { \mathrm { 7 k } } – \mathrm { N R s }$ was 58.0, 70.8, and 86.9 nm, respectively.

Before applying the TPL signal to monitor circulating PEG-NRs, we first examined with microspectroscopy whether surface modification or solvent would affect the TPL property. The solution samples were prepared by suspending CTAB-NRs or PEG-NRs in water, PBS, or serum, adjusted to the same optical density (O.D.). As shown in Figure 1b,c, the TPL spectra from CTAB-NRs and PEG-NRs in water or from PEG-NRs in water,

PBS, and serum had similar intensity and profiles, with a broad emission from 400 nm to near 700 nm. We also examined the TPL intensity as a function of PEG-NR concentration. TPL images of GNR solutions ranging from 4.7 nM to 0.11 nM (estimated from O.D. and $\varepsilon ) ^ { 2 8 }$ were acquired, and the average TPL intensities were plotted against GNR concentration. The linear dependence as shown in Figure 1d allows quantification of GNR density by TPL intensity measurement. Taken together, these results suggest that TPL can be used as a reliable tool for quantitatively imaging of GNRs.

As a bright TPL emitter, GNRs flowing in blood could be observed by intravital imaging of earlobe vessels (see Supporting Information supplemental video). The blood vessel was visualized by transmission illumination (blue). In a single frame acquired in 0.4 s, GNRs (yellow) inside the blood vessel could be detected with a signal-to-noise ratio of 4:1 (Figure 2a). To test whether GNRs would be melted under this condition, we performed continuous laser scanning of GNRs mixed with gel and locally injected into the mouse earlobe. The laser power density and scanning speed were the same as the condition used in the intravital imaging. Both clustered and individual GNRs exhibited the same level of TPL intensity in sequential frames (Supporting Information Figure S3), which supported that photothermal degradation of GNRs was negligible under the flowing conditions. To accurately count the GNRs, we acquired 60-frame movies at different p.i. time over a 24 h period and stacked the 60 frames together for quantitative analysis (Figure 2b-g). An obvious clearance of GNRs was observed. At 10 min after injection, the whole blood vessel was luminescent with highly concentrated GNRs in blood. The TPL intensity decreased with the clearance of GNRs over time, with a fast decay in the first 2 h and a slow change during the following time. At 24 h after injection, almost no GNRs could be detected anymore.

![](images/8f584f98cf0822d03bd8dc0a145da7d39bed55735bbdcca0b6fe6cf70f1d44aa.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright spots on a dark blue textured background, with two red-circled markers and a scale bar (no text or symbols)
</details>

![](images/a7b2232579987c3c7a5d4e42de63ae26a1a65946f7b1ca502f2bd3b6409d9402.jpg)

<details>
<summary>line chart</summary>

| position (μm) | TPL intensity (a.u.) |
| ------------- | -------------------- |
| 2             | 1500                 |
| 3             | 400                  |
| 4             | 600                  |
| 5             | 500                  |
| 6             | 400                  |
| 7             | 500                  |
| 8             | 600                  |
| 9             | 1300                 |
| 10            | 300                  |
</details>

![](images/9eb7c93ac848a50eaad61bda1d5b2ddb813f894628e401401d8c22c81944392e.jpg)

<details>
<summary>text_image</summary>

b
10 min
4099
a.u.
</details>

![](images/5b7eaddf548769186450ee41217343a965331ecff95f12e3b86627b5cf9135bd.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright spots on a dark background with two yellow dashed lines and a 4 h time label (no text or symbols beyond labels)
</details>

![](images/a4960b9d871ce89ab7fd3e418db9d5bdff7f2f73856963061d3ba316611ae168.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing cellular structures with blue nuclei and a yellow dashed boundary, labeled 'c' and '1 h' (no text or symbols beyond labels)
</details>

![](images/2deb5daeaf12312ecdcb679643cd1f970070e316c1de8ad1c7e68a1a1169bb59.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered bright spots on a dark background with two yellow dashed lines labeled '8 h' and a scale bar (no text or symbols beyond labels)
</details>

![](images/089d5b6733d451d37b9f9cb53d8c5db2e112d0c521198e8b40f309c280b18552.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a diagonal band of fluorescent particles with yellow dashed lines indicating time points (no text or symbols present)
</details>

![](images/257d84a2b30ccaa1f9cf32b68a4e80b0eadfc496f8b2ae0b93d5888bf47cb145.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing two yellow dashed lines labeled 'g' and '24 h' against a dark background with scattered bright spots (no text or symbols beyond labels)
</details>

Figure 2. Intravital TPL imaging of PEG-NRs circulating in peripheral blood vessels. (a) A single-frame TPL image of individual flowing GNRs (yellow) marked by red circles. The excitation wavelength was 774 nm. TPL intensity profile from the two GNRs was shown under the figure, with a signal-to-noise ratio of 4:1. The background ( 400 au) was due to the autofluorescence from the blood vessel. $( \mathsf { b { \mathrm { - g } } ) T P I }$ L images of PEG-NRs flowing in blood vessels of the same mouse at p.i. time of (b) 10 min, (c) 1 h, (d) 2 h, (e) 4 h, (f) 8 h, and (g) 24 h. Each image was compiled as a stack of 60 frames collected continuously at a rate of 0.4 s per frame. The excitation wavelength was 774 nm. Scale ba ${ \mathrm { r } } = \widetilde { 2 } 0 \mu { \mathrm { m } }$ .

To carry out a quantitative analysis of GNR clearance from blood, we injected 100 μL saline solution of $\mathrm { m P E G } _ { 2 \mathrm { k } ^ { - } } \mathrm { N R s }$ or $\mathrm { m P E G _ { 5 k } - N R s } \left( \mathrm { \sim } 5 . 2 \mathrm { n M } \right)$ through the tail vein. GNRs flowing in the blood vessels in an earlobe were monitored by TPL imaging at different p.i. time. Control experiment was performed at the same condition using a mouse injected with 100 μL saline solution. We defined the TPL contrast from GNRs, $I _ { \mathrm { N R } } / I _ { \mathrm { b l o o d } }$ (details see Experimental Section) to represent the blood concentration of GNRs. The blood kinetics of $\mathrm { m P E G } _ { 2 \mathrm { k } } – \mathrm { N R s }$ and m $\mathrm { P E G } _ { 5 \mathrm { k } ^ { - } } \mathrm { N F }$ Rs were plotted by $I _ { \mathrm { N R } } / I _ { \mathrm { b l o o d } } \mathrm { v s p . i }$ . time in Figure 3a, b and fitted with two exponential kinetic models. Compared with the one-compartment kinetic model, the two-compartment model generated a much better fitting. The blood clearance of both $\mathrm { m P E G } _ { 2 \mathrm { k } ^ { - } } \mathrm { N R s }$ and $\mathrm { \ m P E G _ { 5 k } - N R s }$ were biphasic, with a rapid initial phase characterized by a $t _ { 1 / 2 }$ of 0.58 h for $\mathrm { n P E G } _ { 2 \mathrm { k } ^ { - } } \mathrm { N R s }$ , and 0.76 h for mP $\mathrm { \bf E G } _ { 5 \mathrm { k } ^ { - } } \mathrm { \bf N R s }$ , and a slower elimination phase with a $t _ { 1 / 2 }$ of 5.00 h for $\mathrm { n P E G } _ { 2 \mathrm { k } } – \mathrm { N R s }$ and 5.42 h for $\mathrm { m P E G } _ { 5 \mathrm { k } ^ { - } } \mathrm { N R s }$ . The population in the slower elimination phase was less than 40% for both m $\mathbf { I P E G } _ { 2 \mathbf { k } } – \mathbf { N R s }$ and $\mathrm { m P E G } _ { 5 \mathrm { k } ^ { - } } \mathrm { N R s }$ . The improvement on blood residence time with longer (5k) PEG was limited compared with the earlier studies of other nanoparticles.14,29 Notably, it was suggested that changing the density of shorter PEG might help to prevent nonspecific binding and rapid clearance.29 In our experiments, the dense PEGylation provided both m $\mathrm { P E G } _ { 2 \mathrm { k } ^ { - } } \mathrm { N R }$ and $\mathrm { n P E G } _ { 5 \mathrm { k } ^ { - } } \mathrm { N R }$ neural surface, explaining their comparability in clearance kinetics.

A recent study by Dai and co-workers demonstrated that branched PEG could significantly prolong the blood circulation of carbon nanotubes than the linear PEG.14,30 We measured the blood residence time of branched $\mathrm { P E G } _ { \mathrm { 7 k } } .$ -coated GNRs by intravital TPL imaging. With the same administered dose, branched $\mathrm { P E G } _ { 7 \mathrm { k } ^ { - 1 } } \mathrm { N R s }$ also showed biphasic kinetics (Figure 3c), with enhanced circula tion half times as 1.01 and 6.99 h for initial and elimination phases and a higher population $( 6 1 \% )$ in the elimination phase, indica tive of better surface protection compared with straight PEG.

![](images/46a3602e561766345114ab3c18f95e4f425401fe19793507e27e91876feb2b88.jpg)

<details>
<summary>line chart</summary>

| post-injection time (h) | mPEG₂ₖ-NR | one-compartment | two-compartment |
| ----------------------- | --------- | -------------- | -------------- |
| 0                       | 1.0       | 1.0            | 1.0            |
| 4                       | 0.6       | 0.4            | 0.5            |
| 8                       | 0.2       | 0.1            | 0.2            |
| 12                      | 0.1       | 0.05           | 0.1            |
| 24                      | 0.0       | 0.0            | 0.0            |
</details>

![](images/ef3dd5d3ec3f4fa41012b1b795d89f27ceea0b432181d73ded7bf222b01222a9.jpg)

<details>
<summary>line chart</summary>

| post-injection time (h) | mPEG₅ₖ-NR | one-compartment | two-compartment |
| ----------------------- | --------- | -------------- | -------------- |
| 0                       | 1.0       | 1.0            | 1.0            |
| 4                       | 0.3       | 0.2            | 0.2            |
| 8                       | 0.1       | 0.1            | 0.1            |
| 12                      | 0.05      | 0.05           | 0.05           |
| 24                      | 0.0       | 0.0            | 0.0            |
</details>

![](images/2faa7894aa7d0fb474aa52f37cb84600c64ea5be36160e15cc249faa98d5a5a3.jpg)

<details>
<summary>line chart</summary>

| post-injection time (h) | branched PEG₇ₖ-NR | one-compartment | two-compartment |
| ----------------------- | ----------------- | -------------- | -------------- |
| 0                       | 1.0               | 1.0            | 1.0            |
| 4                       | 0.6               | 0.5            | 0.4            |
| 8                       | 0.3               | 0.2            | 0.2            |
| 12                      | 0.2               | 0.1            | 0.1            |
| 24                      | 0.0               | 0.0            | 0.0            |
</details>

![](images/0f733d398fd5153612d88f0170fbaf1665a66a710f6211c26d3fdeaf87232b1f.jpg)

<details>
<summary>line chart</summary>

| post-injection time (h) | normalized Au con. |
| ----------------------- | ------------------ |
| 0                       | 1.0                |
| 4                       | 0.6                |
| 8                       | 0.2                |
| 12                      | 0.0                |
| 24                      | 0.0                |
</details>

Figure 3. Quantitative analysis of clearance of $\mathbf { \partial P E G - N R s }$ . Blood circulation kinetics of m $\mathrm { \mathbf { I P E G } } _ { 2 \mathrm { k } } \mathrm { - } \mathrm { N } \mathrm { R s }$ (a), $\mathrm { n P E G _ { 5 k } \mathrm { - N R s \ ( b ) } }$ , and branched $\mathrm { P E G } _ { 7 \mathrm { k } ^ { - } } \mathrm { N R s } \left( \mathrm { c } \right)$ ) probed by intravital TPL imaging meth od. The blood concentration of GNRs was represented by TPL contrast, $I _ { \mathrm { N R } } / I _ { \mathrm { b l o o d } } .$ Each data point was an average from 3 mice $( n \ = \ 3 ) .$ . The data were fitted with one-compartment model (red, $\stackrel { . } { \gamma } ~ = ~ \stackrel { . } { A } e ^ { - ( x { \mathrm { ~ \tiny ~ - ~ \frac ~ { ~ } { ~ } \alpha ~ } } x { } ) / t } ~ + ~ y _ { 0 } )$ ) and two-compartment model (green, $A _ { 1 } e ^ { - ( x \mathrm { ~ - ~ } x _ { 0 } ) / t _ { 1 } } + A _ { 2 } e ^ { - ( \check { x } \mathrm { ~ - ~ } x _ { 0 } ) / t _ { 2 } } + y _ { 0 } ) ~ ($ (d) ICP-MS analysis of gold concentration in blood at different p.i. times, normalized by the gold concentration at 0.5 h after injection. $n = 3 .$ .

![](images/4483e0abab2d7aa1f86cd2bb3123a289dcf867758b32f11706c47a377b942cdd.jpg)  
Figure 4. Serum binding test. $\mathrm { m P E G } _ { 2 \mathrm { k } ^ { - } } \mathrm { N R s }$ (a, 0.52 nM), $\mathrm { n P E G } _ { 5 \mathrm { k } ^ { - } } \mathrm { N R s }$ (b, 0.52 nM), and branched $\mathrm { P E G _ { 7 k } { \mathrm { - N R s } } \ ( c , 0 . 5 2 \ n M ) }$ were incubated in mouse serum, and the extinction spectra were monitored for 24 h. The spectrum was first measured in PBS and then in serum after incubation for 5 min, 10 min, 30 min, 1 h, 2 h, 4 h, 8 h, 12 h, and 24 h. A gradual widening of the longitudinal plasmon resonance band was observed for $\mathrm { m P E G } _ { 2 \mathrm { k } ^ { - } } \mathrm { N R s }$ and $\mathrm { m P E G } _ { 5 \bf k ^ { - } } \mathrm { N R s } .$ , but not for branched $\mathrm { P E G } _ { 7 \mathrm { k } ^ { - } } \mathrm { N R s }$ .

![](images/c30ef13d7757ac6fd4e692e60e62621e4d1a49a5b8d3ed259628ec5631c103b6.jpg)

<details>
<summary>line chart</summary>

| wavelength (nm) | liver | GNRs |
| --------------- | ----- | ---- |
| 400             | 0     | 0    |
| 450             | 30    | 35   |
| 500             | 60    | 70   |
| 550             | 50    | 80   |
| 600             | 20    | 60   |
| 650             | 10    | 30   |
</details>

![](images/299df0145b7be92c0c073370ad38f3a0cb1ab56aa9a82ed1d391f4d7dd3e6fa5.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing red fluorescent structures against a black background, labeled '460-560 nm' in top right corner (no other text or symbols)
</details>

![](images/ff8a34f394b8e87aa64d9289588a6cb1a1bda602b9f0849b51239b4bab27e9c5.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescently labeled structures against a dark background, with scale bar indicating 650-700 nm (no text or symbols beyond label)
</details>

![](images/2b66b88eb709e8929d5e0432aa5c985b76d4fd98ec7e3765ff856de1b8f88e6f.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a bright fluorescent cell cluster with surrounding dark circular structures, highlighted by a green oval (no text or symbols)
</details>

![](images/1f8c7e8ac29c1f18dc4f93c0c4d1bf3ae77f334fc42ade546451bdd2fcdeb045.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of spleen tissue with fluorescent labeling (no text or symbols)
</details>

![](images/a1fa7cb2e3d809a2e6e86b8879d43aa64ad4a52e25e1eb984b6eb1c78b8f6b47.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of kidney tissue with red fluorescence, showing cellular structures (no text or symbols)
</details>

Figure 5. TPL imaging of PEG-NRs in explanted organs. (a) Emission spectra from liver autofluorescence (black) and TPL from PEG-NRs in liver (red), excited by an fs laser at 774 nm. (b) Autofluoresecence from liver and TPL from PEG-NRs excited by 774 nm laser and detected with spectral detector within 460-560 nm. PEG-NRs (bright dots) were observed between adjacent hepatocytes. (c) Image acquired with spectral detector within 650-700 nm in the same area with (b). Only TPL from PEG-NRs was detected, while no autofluorescence was observed in this range. (d) Enlarged image of PEG-NRs in liver, detected within 460-560 nm. GNRs were accumulated in the intercellular space between hepatocytes, which were assigned as Kupffer cells. (e) PEG-NRs observed in spleen. The green circle indicated the uptake of GNRs by a macrophage. (f) No TPL signal from GNRs was detected in kidney. Scale bar $= ~ 1 0 \mu \mathrm { m }$ .

To confirm the in vivo measurement, we performed standard ICP-MS analysis of gold in the blood samples collected at each p.i. time. The ICP-MS measurement (Figure 3d) of $\mathrm { m P E G } _ { 5 \mathrm { k } ^ { - } } \mathrm { N R s }$ showed similar clearance kinetics of GNRs in blood circulation as intravital TPL imaging data; however, the standard deviation of the ICP-MS results was quite big. Because the blood samples were taken from different animals at each p.i. time, the animal-to animal variation and sample preparation including blood extraction and digestion would contribute to the big fluctuations.

The biphasic kinetics we observed was different from the results of carbon nanotubes, which displayed a first-order decay.1

The difference may be attributed to the different compositions and surface properties between nanotubes and PEG-NRs. The biphasic kinetics has been observed for PEGylated liposomes and polymeric nanoparticles, with a rapid clearance of a fraction of administered dose within the first hour of injection.31 Doxil, a PEGylated liposome encapsulated with doxorubicin, is an example with a biphasic circulation $t _ { 1 / 2 }$ of 84 min and 46 h, respectively.32

One possible reason for the biphasic decay might be the surface heterogeneity among PEGylated nanoparticles, with a population bearing insufficient protection. The poor steric shielding allows opsonic binding, which is subsequently prone to phagocytosis by the reticuloendothelial system (RES).31 To assay for opsonic binding, we incubated the $\begin{array} { r l } {  { \operatorname* { m P E G } _ { 2 \mathrm { k } } \mathbf { - N } } } \end{array}$ Rs and m $\mathrm { P E G } _ { 5 \mathrm { k } } – \mathrm { N R }$ s with serum isolated from mouse blood and observed a gradual widen ing of the longitudinal plasmon resonance band (Figure 4a,b), indicative of heterogeneous binding of GNRs by the serum components. For the GNRs coated with branched PEG, no such obvious widening of the longitudinal plasmon resonance band was observed after 24 h incubation in mouse serum (Figure 4c), corresponding to the prolonged blood circulation.

Following the depletion of circulating GNRs, we further mapped their cellular distribution in explanted organs by TPL imaging. Representative images of liver, spleen, and kidney explanted at 24 h p.i. of $\mathrm { m P E G } _ { 5 \mathrm { k } } – \mathrm { N R s }$ were shown in Figure 5. Our microspectroscopy measurement showed that the liver autofluorescence within 400-600 nm as reported before33 was spectrally displaced from the TPL signal. As shown in Figure 5a, GNRs had a broad TPL emission from 400 to 700 nm, whereas autofluorescence from liver quickly dropped near 600 nm. This feature enabled us to distinguish hepatocytes from GNRs by using two spectral channels, 460-560 nm for visualization of hepatocytes (Figure 5b) and 650-700 nm for GNRs (Figure 5c). Using two-photon excited autofluorescence, the hepatocytes were clearly visualized with nuclei appearing as dark circles. Numerous bright dots were observed between adjacent hepatocytes. These dots also appeared in the 650-700 nm channel as shown in Figure 5c and were assigned as GNRs deposited in the liver. As a control, no autofluorescence signal was observed within 650- 700 nm in liver explanted from a mouse injected with saline (Supporting Information Figure S4). It is conceivable that GNRs were captured by Kupffer cells when circulating through liver sinusoids. Accordingly, we observed in an enlarged image (Figure 5d) that no GNRs were inside of hepatocytes, but aggregated in the Kupffer cells confirmed by labeling with F4/80 antibody (Supporting Information Figure S5). Spleen and kidney were also imaged using the same method. GNRs were observed accumulated in spleen macrophages but little in kidney (Figure 5e, f). Similar results were obtained for other PEG-NRs. These observations provided visual evidence that most circulating PEG-NRs were trapped by RES. Although the accumulation of

(33) Croce, A. C.; Ferrigno, A.; Vairetti, M.; Bertone, R.; Freitas, I.; Bottiroli, G. Photochem. Photobiol. Sci. 2004, 3(10), 920–926.

nanoparticles in liver or spleen could be detected by histology or TEM, no sample preparation is required for TPL imaging, making it a quick method to map nanoparticles in the tissues.

## Conclusions

We have demonstrated intravital TPL imaging of GNRs flowing through blood vessels in mice with a high signal-to-noise ratio. The intrinsic TPL from GNRs was not affected by either surface coating or solution environment, and allowed us to visualize the clearance of PEG-NRs after tail vein injection. Quantitative analysis of the TPL signals suggested a biphasic elimination of GNRs from blood circulation and helped us to study how surface coating affected the clearance rate. Compared with ICP-MS method, intravital TPL imaging provides a quick and reliable screening of behaviors of nanoparticles in the same animal. Moreover, spectrally resolved detection of TPL and tissue autofluoresence enabled cellular-level localization of GNRs in explanted organs. Considering that gold surfaces can be modified under mild conditions and that various other gold nanostructures such as nanospheres22 and nanoshells24 also emit a strong multiphoton luminescence, our method can be used as a general approach to study the impacts of size, shape, and surface chemistry on pharmacokinetics of nanostructures in a label-free manner. Combined with other imaging modalities, this method can also be applied to investigate the interactions between nanomedicines with blood components, immune cells, and endo thelium at the tumor vasculature.

Acknowledgment. This work is supported in part by an AHA predoctoral fellowship for Ling Tong and NSF grant CBET0828832 for Dr. Ji-Xin Cheng and Dr. Wei Zheng. The authors cordially thank Yookyung Jung for calculating the plasmon peak shift after PEGylation, and Jaehyun Hur for help in zeta potential and DLS measurement.

Supporting Information Available: Video of intravital TPL imaging of PEG-NRs flowing in a blood vessel, extinction spectra before and after PEGylation of GNRs, size distribution and zeta potential of PEG-NRs, in vitro test of laserinduced GNR melting, TPL images of explanted liver from mouse without GNR injection, TPL and confocal images of liver with GNR accumulation and F4/80 antibody labeling. This material is available free of charge via the Internet at http://pubs.acs.org.