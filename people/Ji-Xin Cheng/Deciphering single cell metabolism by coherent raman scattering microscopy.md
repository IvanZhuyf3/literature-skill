# Deciphering single cell metabolism by coherent Raman scattering microscopy

Shuhua Yue1 and Ji-Xin Cheng

![](images/9e8d26e68c3488dd662a59139a36560c03347fe84ec1d3f7bb1b89cf5c63696b.jpg)

CrossMark

Metabolism is highly dynamic and intrinsically heterogeneous at the cellular level. Although fluorescence microscopy has been commonly used for single cell analysis, bulky fluorescent probes often perturb the biological activities of small biomolecules such as metabolites. Such challenge can be overcome by a vibrational imaging technique known as coherent Raman scattering microscopy, which is capable of chemically selective, highly sensitive, and high-speed imaging of biomolecules with submicron resolution. Such capability has enabled quantitative assessments of metabolic activities of biomolecules (e.g. lipids, proteins, nucleic acids) in single live cells in vitro and in vivo. These investigations provide new insights into the role of cell metabolism in maintenance of homeostasis and pathogenesis of diseases.

## Addresses

1 School of Biological Science and Medical Engineering, Beihang University, Beijing 100191, PR China  
2 Weldon School of Biomedical Engineering, Department of Chemistry, Purdue University Center for Cancer Research, Birck Nanotechnology Center, Purdue Institute of Inflammation, Immunology and Infectious Disease, Purdue University, West Lafayette, IN 47907, USA

Corresponding authors: Yue, Shuhua (yue\_shuhua@buaa.edu.cn) and Cheng, Ji-Xin (jcheng@purdue.edu)

Current Opinion in Chemical Biology 2016, 33:46–57

This review comes from a themed issue on Molecular imaging

Edited by Ji-Xin Cheng and Yasuteru Urano

http://dx.doi.org/10.1016/j.cbpa.2016.05.016

1367-5931/# 2016 Elsevier Ltd. All rights reserved.

## Introduction

Metabolism is a set of chemical transformations that are highly dynamic and tightly regulated for maintaining homeostasis within individual cells of living organisms. These life-sustaining chemical reactions are organized into metabolic pathways by which key biomolecules, such as nucleic acids, amino acids, and lipids, are built up or broken down. Dysregulation in cell metabolism leads to many prevalent human diseases [1,2]. Conventional bioanalysis, where biomolecules are extracted from isolated cells or tissue homogenates, and then analyzed by various types of assays, can tell the presence and concentrations of the biomolecules. Nevertheless, due to limited detection sensitivity, some important target molecules with small quantities are often buried in the large background of dominant species. It has also been increasingly recognized that metabolic processes are intrinsically heterogeneous at the cellular level. The traditional population measurement techniques that describe average cell behaviors cannot investigate variability among cells. More importantly, without information regarding spatial and temporal dynamics, it is impossible to elucidate how exactly the biomolecules are metabolized in single live cells.

For real time imaging of biomolecule dynamics in single cells, fluorescent labels, especially fluorescent proteins, have been widely used. Fluorescent probes are, however, too bulky compared to small biomolecules, so that they often destroy or significantly perturb the biological activities of the small biomolecules. By using endogenous sources of fluorescence contrast, optical microscopic imaging offers unique opportunities to assess metabolic state of cells and tissues in a noninvasive and dynamic manner. In particular, the autofluorescence of coenzymes nicotinamide adenine dinucleotide (NADH) and flavin adenine dinucleotide (FAD) has been widely characterized for the study of cell metabolism. For instance, the Georgakoudi group has studied key metabolic pathways such as glycolysis, the Krebs cycle, and oxidative phosphorylation in the context of cancer, brain function, and obesity by detecting the endogenous fluorescence from NADH and FAD [3]. The Skala group has quantitatively identified glycolytic levels, subtypes, and treatment response in various types of human cancers by probing the fluorescence intensities and lifetimes of reduced NADH and FAD [4,5].

As an alternative to fluorescence, signals from molecular vibration offer an attractive way for chemically selective spectroscopic imaging of cells and tissues. Molecules can be recognized by their distinctive signature, or produced by vibrations of chemical bonds. Fingerprint vibrational spectra of molecules can be recorded through measurements of linear infrared (IR) absorption or inelastic Raman scattering. The application of IR spectroscopy to live-cell imaging is largely hindered by strong water absorption of IR light and low spatial resolution due to long wavelength of IR light. Raman spectroscopy, which uses shorter-wavelength visible light for excitation, has been widely used for analysis of biomolecules in cells and tissues (reviewed in [6]). However, due to extremely small cross-section (-1030 cm2 per molecule as compared with the fluorescence cross-section ${ \sim } 1 0 ^ { - 1 6 }$ cm2 per molecule), spontaneous Raman scattering (shown in Figure 1a) requires a long integration time of at least tens of minutes per frame, which is unsuitable for imaging dynamic living systems.

In order to enhance the Raman scattering signal level, coherent Raman scattering (CRS) microscopy has been developed [7]. As shown in Figure 1b, in most CRS imaging experiments, two excitation fields are used, denoted as pump $( \omega _ { \mathrm { p } } )$ and Stokes $( \omega _ { \mathrm { s } } )$ . When the beating frequency $( \omega _ { \mathrm { p } } - \omega _ { \mathrm { s } } )$ is in resonant with a molecular vibration frequency, four major CRS processes occur simultaneously, namely coherent anti-Stokes Raman scattering (CARS) at $( \omega _ { \mathrm { p } } - \omega _ { \mathrm { s } } ) + \omega _ { \mathrm { p } } ,$ coherent Stokes Raman scattering at $\omega _ { \mathrm { s } } - ( \omega _ { \mathrm { p } } - \omega _ { \mathrm { s } } ) .$ , stimulated Raman gain (SRG) at $\omega _ { \mathrm { s } } ,$ and stimulated Raman loss (SRL) at $\omega _ { \mathrm { { p } } } .$ SRG and SRL belong to the process of stimulated Raman scattering (SRS), in which the Stokes beam intensity is increased and the pump beam intensity is decreased. CARS signal arises from any medium with nonzero third-order susceptibility, which consists of a nonresonant part independent of the beating frequency and a resonant part depending on the beating frequency. The advantages of SRS over CARS lie in the fact that the SRS signal is completely free of the non-resonant background, the spectral profile is identical to the spontaneous Raman spectrum, and the SRS intensity is linearly dependent on molecular concentration. These advantages render SRS microscopy a highly sensitive and quantitative method for biochemical imaging (reviewed in [8]). As a vibrationally enhanced four-wave mixing process, the CARS signal is generated at a new frequency apart from input beams and can be detected by a photo multiplier tube. The modulated SRS signal appears at the same wavelength of the incident beam and can be extracted by a lock-in amplifier [9–11] or a tuned amplifier [12].

Figure 1  
![](images/0423f02cbde3cd0f5b9b6c35c90d7f345019aef66b6d371194715174823404b0.jpg)

<details>
<summary>bar chart</summary>

| Category | Sub-category | Peak Label |
| -------- | ----------- | ---------- |
| (a) Spontaneous Raman scattering | ωp | |
| (a) Spontaneous Raman scattering | ωs | |
| (a) Spontaneous Raman scattering | ωp | |
| (a) Spontaneous Raman scattering | ωas | |
| (b) Coherent Raman scattering (single frequency) | Ω | |
| (b) Coherent Raman scattering (single frequency) | Ωs | |
| (b) Coherent Raman scattering (single frequency) | ωp | |
| (b) Coherent Raman scattering (single frequency) | ωas | |
| (c) Coherent Raman scattering (broadband) | ωs | |
| (c) Coherent Raman scattering (broadband) | ωp | |
| (c) Coherent Raman scattering (broadband) | ωs | |
| (c) Coherent Raman scattering (broadband) | ωp | |
| (c) Coherent Raman scattering (broadband) | ωas | |
| Current Opinion in Chemical Biology
</details>

Spontaneous versus coherent Raman scattering processes. (a) Spontaneous Raman scattering generated by a narrowband pump laser. (b) Single-frequency CRS generated by two narrowband lasers. (c) Broadband CRS induced by a narrowband pump laser and a broadband Stokes laser. Multiple Raman transitions were excited simultaneously. SRG, stimulated Raman gain; SRL, stimulated Raman loss; CARS, coherent anti-Stokes Raman scattering. $\omega _ { \mathsf { p } } , \omega _ { \mathsf { s } } ,$ and $\omega _ { a s }$ denote the frequencies of the pump, Stokes, and anti-Stokes beam, respectively.

CRS microscopy offers the following capabilities for live cell imaging applications. First, the CRS signal is significantly enhanced when the beating frequency is in resonance with a molecular vibration frequency, which offers chemical selectivity for CRS microscopy. Second, the large signal level in CRS microscopy enables high-speed imaging, which is -1000 times faster than a line-scan Raman microscope and -10 000 times faster than a pointscan Raman microscope. Third, signals of CRS microscopy are produced by near IR (NIR) excitation, rendering submicron spatial resolution and minimized photodamage. Fourth, the nonlinear optical processes of CRS microscopy offer inherent three-dimensional sectioning.

Single-frequency excitation has been shown to provide high spectral resolution and maximize the signal to background ratio for CARS by Cheng et al. in 2001 [13]. In early single-frequency CARS microscopy, the major laser sources are electronically synchronized twin picosecond laser systems, which suffer from temporal jitter between the two pulse trains. Laser pumped optical parametric oscillator (OPO) was then adopted for high-speed jitterfree CARS imaging [14–16]. The OPO laser system was used to demonstrate SRS by the Xie group [9], the Volkmer group [10], and the Ozeki group [11]. Although single-frequency CARS and SRS microscopes have reached a video-rate imaging speed [17,18], such speed comes with the price of losing spectral information.

In an effort to gain spectral information, it has been realized that single-frequency CRS microscopy and spontaneous Raman spectroscopy are complementary to each other [19]. While CRS permits high-speed vibrational imaging of a single Raman band, spontaneous Raman scattering allows full spectral analysis at a specified location. It has been demonstrated that integration of CRS microscopy and spontaneous Raman spectroscopy on a single platform permits quantitative compositional analysis of objects inside single live cells [20]. This method, however, can only provide compositional information of certain objects of interest, and not possible to analyze each pixel on the frame.

With narrowband pulses initially used for single frequency CRS imaging, hyperspectral CRS microscopy has been developed based on frame-by-frame wavelength scanning (Figure 1c). Such wavelength-scanning hyperspectral CRS imaging was achieved by several ways. The first was to directly scan the wavelength of one narrowband excitation beam to match different Raman transitions [21,22]. The second was to properly chirp the two broadband excitation beams and tune the time delay between them, which is called spectral focusing [23]. The third was to employ femtosecond pulse-shaping technology [24– 26], which can reach a spectral resolution better than $1 0 \mathrm { c m } ^ { - 1 }$ . In these methods, however, it still takes seconds to minutes to obtain an entire stack of images for reconstruction, and spectral scanning over a stack of frames leads to spectral and spatial distortions.

To avoid such spectral distortions, many research groups are devoted to developing multiplex CRS microscopy, where a CRS spectrum is instantaneously recorded at each pixel $[ 2 7 , 2 8 , 2 9 ^ { \bullet \bullet } ]$ . As early as 2002, Mu¨ ller et al. have developed multiplex CARS microscope to image the thermodynamic state of lipid membranes at the speed of 50–200 ms per pixel [30]. Until very recently, the Cicerone group has demonstrated high speed multiplex CARS with 3.5 ms dwell times per pixel $\left[ 2 9 ^ { \bullet \bullet } \right]$ . On the basis of a tuned amplifier array, the Cheng group demonstrated a multiplex SRS microscope, where SRS spectra covering a window of hundreds of wavenumbers can be recorded in microseconds per pixel $[ 3 1 ^ { \bullet \bullet } ]$ . It is important to note that multiplex detection can be performed not only in the spectral domain, but also in the time domain. In time-domain measurements, all photons are collected and the spectrum is recovered by Fourier transformation. This scheme is useful for in vivo imaging where photons from the specimens are highly scattered. Along this line, Liao et al. demonstrated an approach where coded photons are used for microsecond-scale SRS imaging in a spectrometer free manner [32 ]. Hashimoto et al. showed Fourier-transform CARS spectroscopy at the speed of 41 microseconds per spectrum [33 ]. Along with these instrumental advancements, there have been significant developments of quantitative methods to decompose the spectroscopic image into chemical maps [24,26,27,34].

With all these unique features, including label-free, highspeed, chemically selective, and submicron resolution, CRS microscopy provides a powerful platform for functional imaging of biomolecules and organelles in single living cells. Especially, CRS study of cell metabolism has been pursued in a label-free manner. In 2003, Nan et al. published the first CARS study of lipid droplet biology [35]. Four years later, Hellerer et al. for the first time reported CARS analysis of lipid metabolism in model organism [36]. In 2009, Le et al. used CARS microscopy to study the role of lipid accumulation in cancer metastasis [37]. In 2014, Yue et al. employed SRS microscopy coupled with Raman spectroscopy and revealed altered cholesterol metabolism in prostate cancer $\big [ 3 8 ^ { \bullet \bullet } \big ]$ . Very recently, Lu et al. has demonstrated label-free DNA imaging in vivo with SRS microscopy [39].

CRS study of cell metabolism has been further facilitated by Raman tags. Small-size Raman tags, which show distinct, strong Raman scattering peaks well separated from endogenous cellular background, offer a great opportunity to increase molecular selectivity and improve detection sensitivity of CRS microscopy, without perturbing biological activities of small biomolecules. As shown in Figure 1, a variety of Raman tags, including deuterium [40,41,42 , $4 3 ^ { \bullet \bullet } , 4 4 \dot { ] } , ^ { 1 3 } \mathrm { C } [ 4 5 ^ { \bullet \bullet } ] .$ , alkyne $[ 4 6 ^ { \bullet \bullet } , 4 7 ^ { \bullet \bullet } , 4 8 ^ { \bullet \bullet } , 4 9 ^ { \bullet \bullet } ]$ , and diyne $[ 5 0 ^ { \bullet \bullet } ]$ , have been developed for fast CRS imaging of metabolic activities of fatty acids $[ 2 4 , 4 2 ^ { \bullet } , 4 3 ^ { \bullet \bullet } ]$ , cholesterol $[ 5 0 ^ { \bullet \bullet } ] ,$ , amino acids $[ 4 1 , 4 5 ^ { \bullet \bullet } , 4 7 ^ { \bullet \bullet } , 4 8 ^ { \bullet \bullet } , 5 1 ]$ , nucleic acids $[ 4 6 ^ { \bullet \bullet } , 4 7 ^ { \bullet \bullet } , 4 8 ^ { \bullet \bullet } ]$ , glucose $[ 4 3 ^ { \bullet \bullet } , 4 9 ^ { \bullet \bullet } ] ,$ glycan $[ 4 7 ^ { \bullet \bullet } ] ,$ , and choline $[ 4 4 , 4 5 ^ { \bullet \bullet } , \bar { 4 } 6 ^ { \bullet \bullet } , 4 8 ^ { \bullet \bullet } ]$ , in single cells in vitro and in vivo, with detection sensitivity at a micromolar level.

We note that technical developments and biological applications of CRS microscopy have been extensively discussed in multiple reviews $[ \dot { 5 } 2 ^ { \bullet \bullet } , 5 3 ^ { \bullet \bullet } , 5 4 , 5 5 ^ { \bullet \bullet } , 5 6 ^ { \bullet \bullet } , 5 7 \dot { ] } .$ . Here, we focus on applications of CRS microscopy to understanding lipid, protein and nucleic acid metabolism in various biological systems.

## Single cell metabolism of lipids Lipid-droplet biology

Lipid droplets (LDs) are complex proteolipid organelles that store excessive neutral lipids, like triglycerides (TAGs) and cholesterol esters (CEs) in mammalian cells. LDs have been long underappreciated as inert fat storage by cell biologists, partially due to a lack of readily accessible tools. Until recently, LDs have been found to play essential roles in various aspects of lipid metabolism, and their accumulation is associated with some of the most widespread human diseases, such as obesity, diabetes type II, and atherosclerosis [58]. With the capability of label-free visualization of LDs that generate strong signals from C–H stretching vibrations, CRS microscopy has shed new light on the study of LD biology.

Since the first report of CARS imaging of adipogenesis in live 3T3-L1 cells by the Xie group in 2003 [35], many studies have been undertaken to understand LD formation and degradation. Le et al. unraveled that insulin accounted for the phenotypic variability in LDs accumulation among clonal cells [59]. Yamaguchi et al. found that CGI-58 protein facilitated lipolysis of LDs in cooperation with perilipin [60]. Paar et al. revealed that LDs grow by highly regulated transfer of lipids from one organelle to another, leading to the heterogeneous LD size distribution within and between individual cells [61] (Figure 2a). Since the first CARS study by Zhu et al. to reveal a dynamic, cytoplasmic TAG pool in enterocytes [62], Buhman and Cheng have extensively assessed the physiological functions of cytoplasmic LDs in enterocytes during dietary fat absorption (reviewed in [63]). The Walther and Farese groups unraveled that TAG synthesis enzymes mediated LD growth by relocalizing from the endoplasmic reticulum (ER) to LD [64].

Not only the content but also the composition of LDs may vary with cell type, growth conditions, differentiation status, and other factors. Unsaturation level and packing density of lipids in LDs can be determined by CARS microscopy alone or coupled with confocal Raman spectroscopy [20,65,66]. By SRS imaging of deuterated fatty acids, Zhang et al. found that oleic acids facilitated the conversion of palmitic acids into neutral lipids stored in LDs [40] (Figure 2b). Wang et al. and Fu et al. used hyperspectral SRS microscopy to quantitatively analyze the two classes of neutral lipid, TAGs and CEs, in LDs [42 ,67]. Fu et al. further revealed an increased number and size of LDs and enhanced deposition of unsaturated lipid molecules into LDs in the adrenal gland of obese mice [42 ]. ER stress was found to induce rapid deposition of TAG into hepatic LDs. By using isotope labeling, it was found that unsaturated fatty acid had preferential uptake into lipid storage while saturated fatty acid exhibits toxicity in hepatic cells [42 ].

Moreover, studies have demonstrated that LD is an organelle with directional intracellular trafficking and active transport. The Xie group revealed both subdiffusion and active transport of LDs along microtubules in adrenal cortical cells, and found possible involvement of LD active transport in steroidogenesis [68]. Pezacki and coworkers showed hepatitis C virus (HCV) core protein induced rapid increase in LD size and directed movement of LD on microtubules [69]. They further showed that core-mediated LD localization involved core slowing down the rate of movement of LDs until localization at the perinuclear region where LD movement ceased [70].

In addition, CRS microscopy is a favored approach for the characterization of LD associated genes and proteins. Lee et al. uncovered that adipophilin-coated LDs located in the enterocytes of chronic high-fat fed mice, whereas TIP47- coated LDs located in the enterocytes of acute high-fat fed mice, suggesting the distinct functions of these two proteins [71]. Given that fluorescent protein-tagged LDs associated proteins have been made available, simultaneous CRS and fluorescence imaging would be able to provide new insights into the LD formation and function in living cells. Furthermore, it is foreseeable that the application of high-speed multiplex SRS microscopy and Raman tagbased metabolic labeling will significantly improve our understanding of LD biology.

## Lipid metabolism in model organism

Although nematode Caenorhabditis elegans is distant from mammals, the pathways of lipid metabolism in human are highly conserved in C. elegans. Highly tractable genetics that are critical in lipid metabolism make C. elegans an attractive model for the integrative studies of lipid metabolism regulation and related metabolic diseases [72]. Traditional methods cannot be used to accurately measure dynamic changes of lipid composition in live C. elegans. Since 2007 when Enejder and coworkers reported the first study on CARS imaging of fat storage in live C. elegans [36], several pilot studies have showcased the capability of CARS microscopy for elucidating lipid metabolism in C. elegans. The Cheng and Tissenbaum groups revealed two distinctive lipid species in C. elegans: a neutral lipid species in both the intestine and hypodermis and an autofluorescent particle species only found in the intestine [73,74]. By coupling CARS microscopy with confocal Raman spectroscopy, it was found that genetic mutations on peroxidation and desaturation altered both the amount and composition of neutral lipids [73]. Yi et al. reported that nondroplet-like structure is primarily due to the accumulation of yolk lipoproteins [75]. With the development of SRS microscopy, more in-depth studies have been conducted by several research groups. Xie and coworkers demonstrated RNA interference screening based on SRS microscopy and yielded eight new genetic regulators of lipid storage [76]. The Xie and Wang groups further traced deuterium-labeled saturated and unsaturated fatty acids simultaneously in live C. elegans, and revealed that there was a lack of interaction between the two [42 ]. The Cheng and Tissenbaum groups demonstrated a new platform that allowed the quantitative mapping of fat distribution, unsaturation level, lipid oxidation, and cholesterol-rich lysosomes in living wild-type and mutant C. elegans by hyperspectral SRS imaging in the fingerprint vibration $[ 7 7 ^ { \bullet \bullet } ]$ (Figure 2c). The Cheng group further performed high-speed mapping of biomolecules and discriminated LDs from protein-rich organelles in live worms by the microsecond scale multiplex SRS microscopy [31].

Other than C. elegans, some other model organisms are also gaining popularity in research of lipid metabolism. Brackmann et al. and Chien et al. employed CARS microscopy to investigate the impact of genetic modification on lipid storage in yeast cells [78] and Drosophila [79], respectively. Dou et al. used SRS microscopy to monitor LD dynamics during the development of early Drosophila embryos [80]. Taking advantage of highly manageable genetics of model organisms and lifelong imaging capability of microfluidic chamber, it is foreseeable that CRS microscopy presents an unprecedented opportunity to study dynamic lipid regulation and the underlying metabolic pathways, which will ultimately promote the understanding of human metabolic diseases.

Figure 2  
![](images/076a45eaa4cd7a3d14b793517af8173249632d824c8e949b33487220344cef14.jpg)  
Deciphering single cell metabolism of lipids by CRS microscopy, (a) Time-lapse CARS imaging, of I D depletion in 3T3-L 1, adipocytes upon forskolin-stimulated lipolysis. Reprinted with permission from Ref [61]. Copyright 2012 The American Society for Biochemistry and Molecular Biology, Inc. (b) SRL imaging of deuterated palmitic acid-d in live CHO cells at C–H and C–D stretching vibration, respectively. Reprinted with permission from Ref [40]. Copyright 2011 American Chemical Society. (c) Quantitative mapping of neutral fat droplets, lysosome-related organelles

## Lipid metabolism in cancer

Altered lipid metabolism is increasingly recognized as a signature of cancer cells [2]. Although excess intracellular lipids have been observed in various kinds of cancer, lipid accumulation has not, to date, been used as a prognostic factor or therapeutic target of cancer. In particular, the exact role of lipid accumulation in cancer progression remains elusive. By coupling CARS with other nonlinear optical modalities, Le et al. revealed that excess free fatty acids not only induced intracellular lipid accumulation in cancer cells, but also perturbed cancer cell membranes and increased cancer aggressiveness [37]. Recently, by integrating SRS microscopy with confocal Raman spectroscopy, Yue et al. performed quantitative analysis of lipogenesis at single-cell level in human patient cancerous tissues [38]. The imaging data revealed an unexpected, aberrant accumulation of esterified cholesterol in LDs of high-grade prostate cancer and metastases (Figure 2d–h). Such CE accumulation was shown to be a consequence of loss of tumor suppressor PTEN and subsequent activation of PI3K/AKT pathway in prostate cancer cells [38]. Depletion of CE storage significantly reduced cancer proliferation, impaired cancer invasion capability, and suppressed tumor growth in mouse xenograft models with negligible toxicity [38]. This work opens opportunities for diagnosing and treating prostate cancer by targeting the altered cholesterol metabolism. By coupling SRS microscopy with isotope labeled glucose, Li et al. presented the direct observation of de novo lipogenesis in pancreatic cancer cells, and found glucose was utilized for lipid synthesis in much higher rate in cancer cells compared to normal cells [43] (Figure 2i). By using high-speed multiplex SRS microscopy, Liao et al. quantitatively analyzed LD compositions and dynamics in single cancer cells (Figure 2j–m), and observed the conversion of retinol into retinoic acids [31]. Future studies that take advantages of multiplex SRS microscopy and Raman tag-based metabolic labeling to map lipid dynamics in single live cancer cells will not only provide a better understanding of the roles of lipids in cancer development, but also promote the discovery of new diagnostic biomarkers and therapeutic targets.

## Cholesterol metabolism

Inside cells, cholesterol is an essential molecule that plays important roles in the maintenance of membrane structure, signal transduction, and provision of precursor to hormone synthesis [81]. Dysregulation of cholesterol metabolism has been linked to various diseases [82]. By coupling SRS microscopy with Raman spectroscopy, Yue et al. revealed altered cholesterol metabolism in human prostate cancer. By using synthesized phenyldiyne cholesterol, Lee et al. monitored lysosomal accumulation of cholesterol in cellular model of Niemann– Pick type C disease, and relocation of cholesterol to LDs after HPbCD treatment [50]. They further unraveled that cholesterol uptake was mediated by ChUP-1, and confirmed that cholesterol was stored in lysosome-related organelles, but not in LDs in the intestine in C. elegans [50].

## Single cell metabolism of proteins

The proteome of a cell is highly dynamic and tightly regulated via both protein synthesis and degradation to actively maintain homeostasis. Despite extensive efforts devoted to probing proteins via fluorescence staining, autoradiography, and mass spectrometry, selective visualization of protein synthesis and degradation in living systems with subcellular resolution remains challenging. By coupling SRS microscopy with deuterium-labeled amino acids, Min and coworkers demonstrated direct visualization and quantification of newly synthesized proteins in live cancer cells, embryonic kidney cells, and newly grown neuritis [41] (Figure 3a). They further used 13C-labeled phenylalanine to quantitatively monitor the process of protein degradation in live cells under oxidative stress, cell differentiation, and huntingtin protein aggregation [45]. On the basis of these work, they generalized the

(Figure 2 Legend Continued) (LROs), oxidized lipids, and protein in the whole C. elegans worm with daf-2 mutant, by hyperspectral SRS imaging, k-means clustering, and multivariate curve resolution analysis. Reprinted with permission from Ref [77]. Copyright 2014 Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim. (d)–(h) Aberrant CE accumulation in human prostate cancer tissues. (d)–(g) SRL and two-photon fluorescence images of normal prostate, low-grade, high-grade, and metastatic prostate cancers, respectively. Autofluorescent granules and LDs are indicated by red arrows (gray, SRL; green, two-photon fluorescence). (h) Raman spectra of autofluorescent granules in normal prostate, LDs in prostate cancers, and pure cholesteryl oleate. Spectral intensity was normalized by CH bending band at 1442 cm1 . Black arrows indicate the bands of cholesterol rings at 702 cm1 . Reprinted with permission from Ref [38]. Copyright 2014 Elsevier Inc. (i) SRS imaging of normal immortalized pancreatic epithelial HPDE6 cells and pancreatic cancer PANC1 cells at C–D and C–H vibrations. Cells were treated with 25 mM glucose-d in glucose-free DMEM media supplemented with 10% FBS for three days. The ratio of C–D/C–H was used to analyze the level of de-novo lipogenesis. Reprinted with permission from Ref [43]. Copyright 2014 Macmillan Publishers Limited. (j)–(m) Quantitative mapping and trafficking of lipids in LDs in single live PC3 cells by multiplex SRS microscopy. Reprinted with permission from Ref [31]. Copyright 2015 Macmillan Publishers Limited. (j) CE concentration map. (k) SRL image at 2874 cm1 . Enlarged image shows the movement of LDs (as indicated by the arrow). (l)–(m) Time-lapsed SRL spectra of LDs 1 and 2 shown in (k).

Figure 3  
![](images/e12e77324c1ff0aaf1b162153d11c6db378073e8a2d9d7a17373d53a1d09ec58.jpg)

Deciphering single cell metabolism of proteins by CRS microscopy. (a) SRS imaging of time-dependent de novo protein synthesis in live HeLa cells incubated in a deuterium-labeled all-amino acid medium. SRS image targeting the central 2133 cm1 vibrational peak of C–D displays a time-dependent signal increase of the newly synthesized proteins, with nucleoli being gradually highlighted. As a control, the amide I (1655 cm1 ) signal remains at a steady state over time. Ratio images between the SRS image at 2133 cm1 (newly synthesized proteins) and the SRS image at 1655 cm1 (the amide I band from total proteins), representing the relative new protein fraction with subcellular resolution at each time point. The color bar ranging from black to red represents the ratio ranging from low to high. Reprinted with permission from Ref [41]. Copyright 2013 National Academy of Sciences. (b) SRS imaging of live HeLa cells incubated with 2 mM Hpg alone at $2 1 2 5 \mathsf { c m } ^ { - 1 }$ (alkyne on), 2000 cm1 (alkyne off), and 1655 cm1 (amide I), respectively. Reprinted with permission from Ref [46]. Copyright 2014 Nature America, Inc.

platform for time-lapse imaging of complex protein metabolism in individual live cells in vitro and in vivo [51]. In order to further boost the detection sensitivity, the Min and Huang groups developed alkyne-based Raman tags $[ 4 6 ^ { \bullet \bullet } , 4 7 ^ { \bullet \bullet } , 4 8 ^ { \bullet \bullet } ]$ . In their works, homopropargylglycine, an alkyne-tagged analog of methionine, was imaged to visualize newly synthesized proteomes. As shown in Figure 3b, newly synthesized proteins enrich in the nucleoi, which experience rapid protein exchange. Taken together, integration of CRS microscopy with a variety of Raman tags enables sensitive and specific visualization of amino acids, which will promote the understanding of protein metabolism in single live cells.

## Single cell metabolism of nucleic acids

Nucleic acids metabolism, including synthesis and degradation of nucleic acids (DNA and RNA), is essential for maintaining tissue homeostasis. Dysregulated metabolism of nucleic acids leads to many prevalent human diseases such as cancer. Therefore, live imaging of nucleic acid dynamics in single cells will greatly contribute to the fundamentals of cell biology as well as to applied biomedicine. Multiple studies have shown the capability of CARS microscopy to map 3D distribution of chromosomes in individual live cells [83–86]. By using SRS microscopy in the fingerprint region, Xie and coworkers observed DNA condensation associated with cell division in single salivary gland cells of Drosophila larvae

Figure 4  
![](images/c71d3aa9e9b41c880e27692c32494d504eb90c400a978157cbb747cb5c018cc5.jpg)

(b)  
![](images/8a3bc043e037a8575b336cd1aad0425b1fd996e8bee38110c3111bdf92f677b6.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | DNA    | Cellular Protein | Cellular Lipids |
| ------------------ | ------ | ---------------- | --------------- |
| 2800               | 0.0    | 0.0              | 0.0             |
| 2850               | 0.0    | 0.0              | 1.0             |
| 2900               | 0.3    | 0.4              | 0.9             |
| 2950               | 1.0    | 1.0              | 0.8             |
| 3000               | 0.3    | 0.4              | 0.1             |
| 3050               | 0.1    | 0.2              | 0.0             |
</details>

(c)  
![](images/5a2dd8363c39db7ac61200389be841bb46ef52335db0d278265dd50e2d949688.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image of a cell with green cytoplasm and magenta nuclear staining, labeled '0 min' (no other text or symbols)
</details>

![](images/e4da94f84690c2008a81dcc66e6949b3897aa1c91275ee06740be447d49f46f8.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image of a cell with magenta and green staining, labeled '10 min' (no other text or symbols)
</details>

![](images/b76579534224afd5e0bdcaf783b84c56dfab25064dd9fe3f439d2cc5105420c1.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a fluorescently labeled cellular structure at 20 minutes, with scale bar indicating 20 μm (no text or symbols beyond labels)
</details>

![](images/0a8f0f6b84635f93e7bb719c15bfb751a64795c4b387b5fa2725428cbe190ea0.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing cellular structures with magenta and green staining (no text or symbols)
</details>

(d)  
![](images/98c75330592a073499338984154a8e8bf5b23636273fa82960ea735aeda5f128.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing merged blue and magenta cellular structures with 10 μm scale bar (no text or symbols beyond labels)
</details>

(e)  
![](images/5e5e7568dd3ba90a96235e4995ca33b4c878d07d3567a93692af574f7fd9ba69.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing DNA-labeled cells with 2120 cm⁻¹ scale bar (no text or symbols beyond labels)
</details>

![](images/12045b98a2a82a327d8a31127e23c095310f4d23e8f3f05730c8f949dbd4fe81.jpg)

<details>
<summary>text_image</summary>

2180 cm⁻¹ Off
</details>

![](images/b31a31ef1bdc632f6d65fe24b4696965caf06f1e324fa937a16cfd4c08dab3ce.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-labeled lipid cells at 2850 cm⁻¹ (no text or symbols beyond labels)
</details>

![](images/4b229fbdc83d5c7223214a0ff1ae96978b19e3d83f3f404122af094ef3108115.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing merged red and blue cellular structures (no text or symbols)
</details>

![](images/750b06bfd955d4dffedbf6cb6688cdcac79045c3020ad956499e7feae1ca62b4.jpg)

(f)  
![](images/f6ae719c971f48047206dd311505c3fae3e245c966ef9e6ff27f1789b27956d4.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing RNA-labeled cells at 0 h and 10 μm scale (no text or symbols beyond labels)
</details>

![](images/fedff96551b0b5879781e09889bd0156adbe24802b1fa7e2d9af21074034b00f.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-stained cell nuclei at 1 hour (no text or symbols)
</details>

![](images/b19aaad62bd64927ac8ca977fbf72195e09d9bb55f90660924607a40664290bf.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red-labeled cellular structures against a black background, labeled '2 h' in the corner (no other text or symbols)
</details>

![](images/73b13a39eaacd02634b05ccead775d03e6aadfb06d09d3f96455c6157008c6d2.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing red fluorescent spots against a black background, labeled '4 h' in the corner (no other text or symbols)
</details>

![](images/4d7fdc69e95246c60006b87fe1fdcb32a4403847dcced7d69d66eb91c08dd2bc.jpg)

<details>
<summary>natural_image</summary>

Dark field image showing scattered red fluorescent spots against a black background, labeled '7 h' in the corner (no other text or symbols)
</details>

![](images/f19a416b17adc4427663ef10fcc0b7bff5410c4c740cf8ff07eafe8bed6cc6cc.jpg)  
Current Opinion in Chemical Biology

Deciphering single cell metabolism of nucleic acids by CRS microscopy. (a) SRS images of a live cell in mitotic phase (prophase) at 2967, 2926, and 2850 cm1 , respectively, and the decomposed distribution of DNA (magenta), protein (blue), lipids (green), and the overlay. SRS images at three selected Raman shifts in the C–H stretching vibrational band were acquired. Linear decomposition was performed with a premeasured calibration matrix to retrieve the distribution of DNA, protein, and lipids. (b) Raman spectra of DNA, cellular protein, and cellular lipids extracted from HeLa cells. (c) Time-lapse images of a HeLa cell undergoing cell division. (d) SRS images of a live cell in interphase (the decomposed distribution of DNA and the overlay). (a)–(d) Reprinted with permission from Ref [39]. Copyright 2015 National Academy of Sciences. (e) SRS images of HeLa cells treated with 200 mm EdU for 18 hours. Images shown from left to right are the alkyne on-resonance (2120 cm1 ), alkyne offresonance (2180 cm1 ), total lipids (2850 cm1 ) and merged images of EdU and total lipids. Reprinted with permission from Ref $[ 4 7 ^ { \bullet \bullet } ] .$ . Copyright 2014 Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim. (f) Pulse-chase imaging of RNA turnover in HeLa cells incubated with 2 mMEU (alkyne on, $2 1 2 0 \mathsf { c m } ^ { - \dagger } )$ for 12 hours followed by EU-free medium. Reprinted with permission from Ref [46]. Copyright 2014 Nature America, Inc.

and single mammalian cells [87]. Recently, they further increased imaging sensitivity by retrieving distinct Raman spectral features of C–H bonds in DNA, and showed the capability to track chromosome dynamics of skin cells in live mice $[ 3 9 ^ { \bullet \bullet } ]$ (Figure 4a–d).

The Min and Huang groups opened a new avenue to monitor nucleic acids dynamics in single live cells by metabolic incorporation of alkyne-based Raman tags [46,47,48] (Figure 4e–f). Specifically, 5-ethynyl-20 - deoxyuridine (EdU), an alkyne-bearing thymidine analog is metabolically incorporated into replicating DNA by partly substituting thymidine. Metabolic uptake of EdU was imaged during de novo DNA synthesis. On the basis of EdU labeling, dividing cells were tracked every 5 min during mitosis. By metabolic incorporation of the alkynetagged uridine analog 5-ethynyl uridine (EU), the RNA transcription and turnover were monitored and a short nuclear RNA lifetime (-3 hours) was found in live HeLa cells. Taken together, by coupling with Raman tags, SRS microscopy offers an effective way to study nucleic acid metabolism in single live cells.

## Single cell metabolism of glucose

Glucose is the primary energy source for most living organisms. Glucose uptake has been extensively studied by various methods, such as positron emission tomography and magnetic resonance imaging. Because glucose uptake in many crucial physiological and pathological processes is intrinsically heterogeneous at the cellular level, Hu et al. developed a new platform to visualize glucose uptake activity in single live cells by SRS imaging of alkyne-labeled glucose [49]. They found heterogeneous glucose uptake patterns in tumor xenograft tissues, neuronal culture, and mouse brain tissues [49]. In order to study the dynamic processes of glucose metabolism, Li et al. employed SRS microscopy to image deuterium-labeled glucose in individual living cells [43]. Deuterium substitution does not vary the structure of glucose, nor its physiological functions. As the first direct visualization, Li et al. observed that deuteriumlabeled glucose was largely utilized for de novo lipogenesis in cancer cells [43]. This method of imaging single cell metabolism of glucose could be a valuable tool for elucidating the reprogrammed metabolic network in human diseases.

## Concluding remarks and future perspectives

With the capability of label-free, highly sensitive, and high-speed mapping of biomolecules dynamics in individual live cells, CRS microscopy offers a novel platform to study single cell metabolism and has shed new light on the role of lipid and DNA metabolism in homeostasis maintenance and disease pathogenesis, in a label-free manner. The integration of CRS microscopy and Raman tagging is becoming a fruitful source of innovation for the toolbox of cell metabolism research

Looking into the future, we would predict two promising directions. One is the study of metabolic conversion via multiplex CRS microscopy, using spectral profile as a signature. As an example, Liao et al. has shown the conversion of retinol into retinoid acids by using multiplex SRS microscopy $[ 3 1 ^ { \bullet \bullet } ]$ . The other direction is the study of less concentrated metabolites via further improvement of sensitivity, for instance, NAD/NADH, ATP, glycogen/glucose, metabolism of specific protein, RNA or DNA modification. These are still difficult but will be enabled by further technology development. Eventually our dream is to understand how ‘Waldo’ functions based on intrinsic signature of molecules.

## Acknowledgements

This work is supported by the National Natural Science Foundation of China 81501516 (SY), the ‘Excellent Hundred Talents’ Program start-up fund from Beihang University (SY), and NIH grant CA182608 and a Keck Foundation grant (J-XC).

## References and recommended reading

Papers of particular interest, published within the period of review, have been highlighted as:

 of special interest  
 of outstanding interest

1 Wymann MP, Schneiter R: Lipid signalling in disease. Nat Re Mol Cell Biol 2008, 9:162-176  
2. Schulze A, Harris AL: How cancer metabolism is tuned for proliferation and vulnerable to disruption. Nature 2012, 491:364-373.  
3. Georgakoudi I, Quinn KP: Optical imaging using endogenous contrast to assess metabolic state. Annu Rev Biomed Eng 2012, 14:351-367.  
4. Shah AT, Demory Beckler M, Walsh AJ, Jones WP, Pohlmann PR, Skala MC: Optical metabolic imaging of treatment response in human head and neck squamous cell carcinoma. PLoS ONE 2014, 9:e90746.  
5. Walsh AJ, Cook RS, Sanders ME, Aurisicchio L, Ciliberto G, Arteaga CL, Skala MC: Quantitative optical imaging of primary tumor organoid metabolism predicts drug response in breast cancer, Cancer Res 2014. 74:5184-5194.  
6. Movasaghi Z, Rehman S, Rehman IU: Raman spectroscopy of biological tissues. Appl Spectrosc Rev 2007, 42:493-541.  
7. Cheng J-X, Xie XS: Coherent Raman Scattering Microscopy. Boca Raton. FL: CRC Press: 2012.  
8. Zhang D, Wang P, Slipchenko MN, Cheng JX: Fast vibrational imaging of single cells and tissues by stimulated Raman scattering microscopy. Acc Chem Res 2014, 47:2282-2290.  
9. Freudiger CW, Min W, Saar BG, Lu S, Holtom GR, He C, Tsai JC, Label-free biomedical imaging with high sensitivity by stimulated Raman scattering microscopy. Science 2008, 322:1857-1861.  
10. Nandakumar P, Kovalev A, Volkmer A: Vibrational imaging based on stimulated Raman scattering microscopy. New J Phys 2009, 11:033026.  
11. Ozeki Y, Dake F, Kajiyama S, Fukui K, Itoh K: Analysis and experimental assessment of the sensitivity of stimulated Raman scattering microscopy. Opt Express 2009, 17: 3651-3658.  
12. Slipchenko M, Oglesbee RA, Zhang D, Wu W, Cheng J-X: Heterodyne detected nonlinear optical microscopy in a lock-in free manner. J Biophoton 2012, 5:801-807.  
13. Cheng JX, Volkmer A, Book LD, Xie XS: An epi-detected coherent anti-Stokes Raman scattering (E-CARS) microscope with high spectral resolution and high sensitivity. J Phys Chem B 2001, 105:1277-1280.  
14. Jurna M, Korterik JP, Offerhaus HL, Otto C: Noncritical phasematched lithium triborate optical parametric oscillator for high resolution coherent anti-Stokes Raman scattering spectroscopy and microscopy. Appl Phys Lett 2006:89.  
15. Saar BG, Holtom GR, Freudiger CW, Ackermann C, Hill W, Xie XS: Intracavity wavelength modulation of an optical parametric oscillator for coherent Raman microscopy. Opt Express 2009, 17:12532-12539.  
16. Ganikhanov F, Carrasco S, Xie XS, Katz M, Seitz W, Kopf D: Broadly tunable dual-wavelength light source for coherent anti-Stokes Raman scattering microscopy. Opt Lett 2006, 31:1292-1294.  
17. Evans CL, Potma EO, Mehron Ph, Cote D, Lin CP, Xie XS: Chemical imaging of tissue in vivo with video-rate coherent anti-Stokes Raman scattering microscopy. Proc Natl Acad Sci U S A 2005, 102:16807-16812.  
18. Saar BG, Freudiger CW, Reichman J, Stanley CM, Holtom GR, Xie XS: Video-rate molecular imaging in vivo with stimulated Raman scattering. Science 2010, 330:1368-1370.  
19. Cui M, Bachler BR, Ogilvie JP: Comparing coherent and spontaneous Raman scattering under biological imaging conditions. Opt Lett 2009, 34:773-775.  
20. Slipchenko MN, Le TT, Chen H, Cheng JX: High-speed vibrational imaging and spectral analysis of lipid bodies by compound Raman microscopy. J Phys Chem B 2009, 113:7681-7686  
21. Suhalim JL, Chung CY, Lilledahl MB, Lim RS, Levi M, Tromberg BJ, Potma EO: Characterization of cholesterol crystals in atherosclerotic plaques using stimulated Raman scattering and second-harmonic generation microscopy. Biophys J 2012, 102:1988-1995  
22. Mansfield JC. Littleiohn GR. Seymour MP. Lind RJ. Perfect S Moger J: Label-free chemically specific imaging in planta with stimulated Raman scattering microscopy. Anal Chem 2013, 85:5055-5063.  
Hyperspectral imaging with stimulated Raman scattering by chirped femtosecond lasers. J Phys Chem B 2013, 117:4634-4640.  
24. Zhang D, Wang P, Slipchenko MN, Ben-Amotz D, Weiner AM, Cheng J-X: Quantitative vibrational imaging by hyperspectral stimulated Raman scattering microscopy and multivariate curve resolution analysis. Anal Chem 2013, 85:98-106.  
25. Ozeki Y, Umemura W, Sumimura K, Nishizawa N, Fukui K, Itoh K: Stimulated Raman hyperspectral imaging based on spectral filtering of broadband fiber laser pulses. Opt Lett 2012, 37:431-433.  
26. Ozeki Y, Umemura W, Otsuka Y, Satoh S, Hashimoto H, Sumimura K, Nishizawa N, Fukui K, Itoh K: High-speed molecular spectral imaging of tissue with stimulated Raman scattering. Nat Photon 2012, 6:845-851.  
27. Fu D, Lu FK, Zhang X, Freudiger C, Pernik DR, Holtom G, Xie XS: Quantitative chemical imaging with multiplex stimulated Raman scattering microscopy. J Am Chem Soc 2012, 134:3623-3626.  
28. Seto K, Okuda Y, Tokunaga E, Kobayashi T: Development of a multiplex stimulated Raman microscope for spectral imaging through multi-channel lock-in detection. Rev Sci Instrum 2013, 84:083705.  
29. Camp CH Jr, Lee YJ, Heddleston JM, Hartshorn CM, Hight • Walker AR, Rich JN, Lathia JD, Cicerone MT: High-speed coherent Raman fingerprint imaging of biological tissues. Nat Photonics 2014, 8:627-634.  
This study has demonstrated high speed multiplex CARS with 3.5 ms dwell times per pixel and a broad spectral window of over 3000 cm1 .  
30. Mu¨ ller M, Schins JM: Imaging the thermodynamic state of lipid membranes with multiplex CARS microscopy. J Phys Chem B 2002, 106:3715-3723  
31. Liao CS, Slipchenko MN, Wang P, Li J, Lee SY, Oglesbee RA,  
• Cheng JX: Microsecond scale vibrational spectroscopic imaging by multiplex stimulated raman scattering microscopy. Light Sci Appl 2015:4.  
This study has demonstrated a multiplex SRS microscope with the speed of microseconds per pixel and a spectral window of hundreds of wavenumbers.  
32. Liao CS, Wang P, Li J, Lee HJ, Eakins G, Cheng JX:  
Spectrometer-free vibrational imaging by retrieving stimulated Raman signal from highly scattered photons. Sci Adv 2015, 1:e1500738.  
This study has demonstrated microsecond-scale SRS imaging in a spectrometer free manner, where all photons are collected and the spectrum is recovered by Fourier transformation. This scheme is useful for in vivo imaging where photons from the specimens are highly scattered.  
33. Hashimoto K, Takahashi M, Ideguchi T, Goda K: Broadband  
coherent Raman spectroscopy running at 24,000 spectra per second. Sci Rep 2016, 6:21036.  
This study has demonstrated Fourier-transform CARS spectroscopy at the speed of 41 ms per spectrum.  
34. Suhalim JL, Chung CY, Lilledahl MB, Lim RS, Levi M, Tromberg BJ, Potma FO: Characterization of cholesterol crystals in atherosclerotic plaques using stimulated raman scattering and second-harmonic generation microscopy. Biophys J 2012, 102:1988-1995.  
35. Nan X, Cheng JX, Xie XS: Vibrational imaging of lipid droplets in live fibroblast cells with coherent anti-Stokes Raman scattering microscopy 44  
36. Hellerer T, Axa¨ ng C, Brackmann C, Hillertz P, Pilon M, Enejder A: Monitoring of lipid storage in Caenorhabditis elegans using coherent anti-Stokes Raman scattering (CARS) microscopy. Proc Natl Acad Sci U. S A 2007. 104:14658-14663  
37. Le TT, Huff TB, Cheng JX: Coherent anti-Stokes Raman scattering imaging of lipids in cancer metastasis. BMC Cancer 2009, 9:42.  
38. Yue S, Li J, Lee S-Y, Lee HJ, Shao T, Song B, Cheng L,  
Masterson TA, Liu X, Ratliff TL et al.: Cholesteryl ester accumulation induced by PTEN loss and PI3K/AKT activation underlies human prostate cancer aggressiveness, Cell Metabol 2014, 19:393-406.  
The authors revealed an unexpected, aberrant accumulation of esterified cholesterol in human prostate cancer by coupling SRS microscopy with Raman spectroscopy. Such accumulation is driven by PTEN loss and PI3K/AKT activation, and underlies prostate cancer aggressiveness. These findings open new opportunites for diagnosis and treatment of prostate cancer.  
39. Lu FK, Basu S, Igras V, Hoang MP, Ji M, Fu D, Holtom GR, Neel VA,  
Label-free DNA imaging in vivo with stimulated Raman scattering microscopy. Proc Natl Acad Sci U S A 2015. 112:11624-11629  
The authors showed the capability of SRS microscopy to track chromosome dynamics of skin cells in live mice by retrieving distinct Raman spectral features of C–H bonds in DNA. This method can be applied to both in vivo DNA dynamic studies and instant label-free human skin cancer diagnosis.  
40. Zhang D, Slipchenko MN, Cheng J-X: Highly sensitive vibrational imaging by femtosecond pulse stimulated Raman loss. J Phys Chem Lett 2011, 2:1248-1253.  
41. Wei L, Yu Y, Shen Y, Wang MC, Min W: Vibrational imaging of newly synthesized proteins in live cells by stimulated Raman scattering microscopy. Proc Natl Acad Sci U S A 2013, 110:11226-11231.  
42. Fu D, Yu Y, Folick A, Currie E, Farese RV Jr, Tsai TH, Xie XS,  
Wang MC: In vivo metabolic fingerprinting of neutral lipids with hyperspectral stimulated Raman scattering microscopy. J Am Chem Soc 2014, 136:8820-8828.  
The authors used hyperspectral SRS microscopy to quantitatively analyze different species of neutral lipids in lipid droplets. This study provides new approaches for metabolic tracing of neutral lipids and their precursors in living cells and organisms.

43. Li J, Cheng JX: Direct visualization of de novo lipogenesis in  single living cells. Sci Rep 2014, 4:6807. The authors presented the direct observation of increased de novo lipogenesis in individual pancreatic cancer cells by SRS imaging of deuterated glucose. This method of imaging single cell metabolism of glucose could be a valuable tool for elucidating the reprogrammed metabolic network in human diseases.

44. Hu F, Wei L, Zheng C, Shen Y, Min W: Live-cell vibrational imaging of choline metabolites by stimulated Raman scattering coupled with isotope-based metabolic labeling. Analyst 2014, 139:2312-2317.

45. Shen Y, Xu F, Wei L, Hu F, Min W: Live-cell quantitative imaging  of proteome degradation by stimulated Raman scattering. Angew Chem Int Ed Engl 2014, 53:5596-5599.

The authors coupled SRS microscopy with 13C-Phe labeling to quantitatively monitor the process of protein degradation in live cells under oxidative stress, cell differentiation, and huntingtin protein aggregation. This proteomic approach reveals the global proteolysis activity and may be applied to drug screening.

46. Wei L, Hu F, Shen Y, Chen Z, Yu Y, Lin CC, Wang MC, Min W: Live-• cell imaging of alkyne-tagged small biomolecules by stimulated Raman scattering. Nat Methods 2014, 11:410- 412.

This reference and Refs [47,48], three research articles, published at about the same time and report SRS imaging of alkyne tags as a general strategy for sensitive and specific visualization of a broad spectrum of small biomolecules in live cells and animals. SRS imaging of alkynes may do for small biomolecules what fluorescence imaging of fluorophores has done for larger species.

47. Hong S, Chen T, Zhu Y, Li A, Huang Y, Chen X: Live-cell  stimulated Raman scattering imaging of alkyne-tagged biomolecules. Angew Chem Int Ed Engl 2014. 53:5827-5831.

See annotation to Ref [46].

48. Chen Z, Paley DW, Wei L, Weisman AL, Friesner RA, Nuckolls C, • Min W: Multicolor live-cell chemical imaging by isotopically edited alkyne vibrational palette. J Am Chem Soc 2014, 136:8027-8033.

See annotation to Ref [46].

49. Hu F, Chen Z, Zhang L, Shen Y, Wei L, Min W: Vibrational imaging • of glucose uptake activity in live cells and tissues by stimulated Raman scattering. Angew Chem Int Ed Engl 2015, 54:9821-9825.

The authors developed a new platform to visualize glucose uptake in single live cells by SRS imaging of alkyne-labeled glucose. This method offers an opportunity to study heterogeneous glucose uptake patterns in crucial physiological and pathological processes.

50. Lee HJ, Zhang W, Zhang D, Yang Y, Liu B, Barker EL, Buhman KK, Slipchenko LV, Dai M, Cheng JX: Assessing cholesterol storage in live cells and C. elegans by stimulated Raman scattering imaging of phenyl-diyne cholesterol. Sci Rep 2015. 5:7930.

The authors developed a new method to monitor metabolic activities of cholesterol in single live cells by SRS imaging of phenyl-diyne cholesterol. This approach offers new opportunities for mechanistic study of diseases, such as Niemann–Pick type C disease, and highly efficient screening of drugs that target cholesterol metabolism in C. elegans.

51. Wei L, Shen Y, Xu F, Hu F, Harrington JK, Targoff KL, Min W: Imaging complex protein metabolism in live organisms by stimulated Raman scattering microscopy with isotope labeling 10

52. Schie IW, Krafft C, Popp J: Applications of coherent Raman scattering microscopies to clinical and biological studies. Analyst 2015, 140:3897-3909.

This reference and Refs [53,55,56], four recent reviews, overview the development and applications of CRS microscopy in biology and medicine.

53. Cheng J-X, Xie XS: Vibrational spectroscopic imaging of living • systems: an emerging platform for biology and medicine. Science 2015, 350:aaa8870.

See annotation to Ref [52].

54. Min W, Freudiger CW, Lu S, Xie XS: Coherent nonlinear optical imaging: beyond fluorescence microscopy. Annu Rev Phys Chem 2011,62:507-530

55. Streets AM, Li A, Chen T, Huang Y: Imaging without  fluorescence: nonlinear optical microscopy for quantitative cellular imaging. Anal Chem 2014, 86:8506-8513. See annotation to Ref [52].

56. Camp CH, Cicerone MT: Chemically sensitive bioimaging with  coherent Raman scattering. Nat Photon 2015, 9:295-305. See annotation to Ref [52].

57. Pezacki JP, Blake JA, Danielson DC, Kennedy DC, Lyn RK, Singaravelu R: Chemical contrast for imaging living systems: molecular vibrations drive CARS microscopy. Nat Chem Biol 2011, 7:137-145.

58. Walther TC, Farese RV Jr: Lipid droplets and cellular lipid metabolism. Annu Rev Biochem 2012, 81:687-714.

59. Le TT, Cheng JX: Single-cell profiling reveals the origin of phenotypic variability in adipogenesis. PLoS ONE 2009, 4:e5189.

60. Yamaguchi T, Omatsu N, Morimoto E, Nakashima H, Ueno K, Tanaka T, Satouchi K, Hirose F, Osumi T: CGI-58 facilitates lipolysis on lipid droplets but is not involved in the vesiculation of lipid droplets caused by hormonal stimulation. J Lipid Res 2007, 48:1078-1089.

61. Paar M, Jungst C, Steiner NA, Magnes C, Sinner F, Kolb D, Lass A, Zimmermann R, Zumbusch A, Kohlwein SD et al.: Remodeling of lipid droplets during lipolysis and growth in adipocytes. J Biol Chem 2012, 287:11164-11173.

62. Zhu J, Lee B, Buhman KK, Cheng JX: A dynamic, cytoplasmic triacylglycerol pool in enterocytes revealed by ex vivo and in vivo coherent anti-Stokes Raman scattering imaging. J Lipid Res 2009, 50:1080-1089.

63. Uchida A, Lee HJ, Cheng JX, Buhman KK: Imaging cytoplasmic lipid droplets in enterocytes and assessing dietary fat absorption. Methods Cell Biol 2013, 116:151-166.

64. Wilfling F, Wang H, Haas JT, Krahmer N, Gould TJ, Uchida A, Cheng JX, Graham M, Christiano R, Frohlich F et al.: Triacylglycerol synthesis enzymes mediate lipid droplet growth by relocalizing from the ER to lipid droplets. Dev Cell 2013, 24:384-399.

65. Heinrich C, Hofer A, Ritsch A, Ciardi C, Bernet S, Ritsch-Marte M: Selective imaging of saturated and unsaturated lipids by widefield CARS-microscopy. Opt Express 2008, 16:2699-2708.

66. Rinia HA, Burger KNJ, Bonn M, Mu¨ ller M: Quantitative label-free imaging of lipid composition and packing of individual cellular lipid droplets using multiplex CARS microscopy. Biophys J 2008, 95:4908-4914

67. Wang P, Li J, Hu CR, Zhang D, Sturek M, Cheng JX: Label-free quantitative imaging of cholesterol in intact tissues by hyperspectral stimulated Raman scattering microscopy. Angew Chem Int Ed Engl 2013. 52:13042-13046.

68. Nan X, Potma EO, Xie XS: Nonperturbative chemical imaging of organelle transport in living cells with coherent anti-Stokes Raman scattering microscopy. Biophys J 2006, 91:728-735.

69. Lyn RK, Kennedy DC, Stolow A, Ridsdale A, Pezacki JP: Dynamics of lipid droplets induced by the hepatitis C virus core protein. Biochem Biophys Res Commun 2010, 399:518-524.

70. Lyn RK, Hope G, Sherratt AR, McLauchlan J, Pezacki JP: Bidirectional lipid droplet velocities are controlled by differential binding strengths of HCV core DII protein. PLoS ONE 2013, 8:e78065.

71. Lee B, Zhu JB, Wolins NE, Cheng JX, Buhman KK: Differential association of adipophilin and TIP47 proteins with cytoplasmic lipid droplets in mouse enterocytes during dietary fat absorption. Biochim Biophys Acta 2009, 1791:1173- 1180.

72. Ashrafi K, Chang FY, Watts JL, Fraser AG, Kamath RS, Ahringer J, Ruvkun G: Genome-wide RNAi analysis of Caenorhabditis elegans fat regulatory genes. Nature 2003, 421:268-272.

73. Le TT, Duren HM, Slipchenko MN, Hu C-D, Cheng J-X: Label-free quantitative analysis of lipid metabolism in living Caenorhabditis elegans. J Lipid Res 2010, 51:672-677.

74. Yen K, Le TT, Bansal A, Narasimhan SD, Cheng J-X, Tissenbaum H: A comparative study of fat storage quantitation in nematode Caenorhabditis elegans using label and labelfree methods. PLoS ONE 2010.  
75. Yi YH, Chien CH, Chen WW, Ma TH, Liu KY, Chang YS, Chang TC, Lo SJ: Lipid droplet pattern and nondroplet-like structure in two fat mutants of Caenorhabditis elegans revealed by coherent anti-Stokes Raman scattering microscopy. J Biomed Opt 2014, 19:7.  
76. Wang MC, Min W, Freudiger CW, Ruvkun G, Xie XS: RNAi screening for fat regulatory genes with SRS microscopy. Nat Methods 2011, 8:135-138.  
77. Wang P, Liu B, Zhang D, Belew MY, Tissenbaum HA, Cheng JX: • Imaging lipid metabolism in live Caenorhabditis elegans using fingerprint vibrations. Angew Chem Int Ed Engl 2014, 53:11787-11792.  
The authors demonstrated a new platform that allowed the quantitative mapping of fat distribution, unsaturation level, lipid oxidation, and cholesterol-rich lysosomes in living wild-type and mutant C. elegans by hyperspectral SRS imaging in the fingerprint vibration. This method may be used to study the impact of diet and the insulin/IGF-1 signaling pathway on obesity, diabetes, and longevity.  
78. Brackmann C, Norbeck J, A˚ keson M, Bosch D, Larsson C, Gustafsson L, Enejder A: CARS microscopy of lipid stores in yeast: the impact of nutritional state and genetic background J Raman Spectrosc 2009, 40:748-756.  
79. Chien CH, Chen WW, Wu JT, Chang TC: Investigation of lipid homeostasis in living Drosophila by coherent anti-Stokes Raman scattering microscopy. J Biomed Opt 2012, 17:7.  
80. Dou W, Zhang D, Jung Y, Cheng J-X, Umulis DM: Label-free imaging of lipid-droplet intracellular motion in early Drosophila embryos using femtosecond-stimulated Raman loss microscopy. Biophys J 2012, 102:1666-1675.  
81. Ikonen E: Cellular cholesterol trafficking and compartmentalization. Nat Rev Mol Cell Biol 2008, 9: 125-138.  
82. Maxfield FR, Tabas I: Role of cholesterol and lipid organization in disease. Nature 2005, 438:612-621.  
83. Cheng J-X, Jia YK, Zheng G, Xie XS: Laser-scanning coherent anti-stokes Raman scattering microscopy and applications to cell biology. Biophys J 2002, 83:502-509.  
84. Kano H: Molecular vibrational imaging of a human cell by multiplex coherent anti-Stokes Raman scattering microspectroscopy using a supercontinuum light source. J Raman Spectrosc 2008, 39:1649-1652.  
85. Parekh SH, Lee YJ, Aamer KA, Cicerone MT: Label-free cellular imaging by broadband coherent anti-Stokes Raman scattering microscopy. Biophys J 2010, 99: 2695-2704.  
86. Pliss A, Kuzmin AN, Kachynski AV, Prasad PN: Biophotonic probing of macromolecular transformations during apoptosis. Proc Natl Acad Sci U S A 2010, 107:12771-12776.  
87. Zhang X, Roeffaers MB, Basu S, Daniele JR, Fu D, Freudiger CW, Holtom GR, Xie XS: Label-free live-cell imaging of nucleic acids using stimulated Raman scattering microscopy. Chemphyschem 2012, 13:1054-1059.