# Mapping enzyme activity in living systems by real-time mid-infrared photothermal imaging of nitrile chameleons

Received: 15 February 2023

Accepted: 17 November 2023

Published online: 8 January 2024

![](images/3bceb9b8a5cbf4703e5f3cf4947dc7cdf2775b8c0705b00dbdb0653a463bb422.jpg)

Check for updates

Hongjian He1,2,7, Jiaze Yin1,2,7, Mingsheng Li1,2, Chinmayee Vallabh Prabhu Dessai  2,3, Meihui Yi4 , Xinyan Teng  2,5, Meng Zhang2,3, Yueming Li  2,6, Zhiyi Du2,5, Bing Xu  4 & Ji-Xin Cheng  1,2,3,5

Simultaneous spatial mapping of the activity of multiple enzymes in a living system can elucidate their functions in health and disease. However, methods based on monitoring fuorescent substrates are limited. Here, we report the development of nitrile (C≡N)-tagged enzyme activity reporters, named nitrile chameleons, for the peak shift between substrate and product. To image these reporters in real time, we developed a laser-scanning mid-infrared photothermal imaging system capable of imaging the enzymatic substrates and products at a resolution of 300 nm. We show that when combined, these tools can map the activity distribution of diferent enzymes and measure their relative catalytic efciency in living systems such as cancer cells, Caenorhabditis elegans, and brain tissues, and can be used to directly visualize caspase–phosphatase interactions during apoptosis. Our method is generally applicable to a broad category of enzymes and will enable new analyses of enzymes in their native context.

Enzymes, efficient and specific catalysts of a variety of biochemical reactions, play a critical role in all biological processes. Precise spatial and temporal regulation of enzyme activity is crucial to the successful operation of cellular machinery1 . Thus, the spatial mapping and quantification of the activity of enzymes, preferentially in living organisms, is vital to understand the functions and roles of enzymes in health and disease. Notably, many biological events and signaling pathways, such as apoptosis2 , are accomplished by the cooperation of multiple enzyme species. However, an attempt to map the activity of one kind of enzyme in one area of interest is insufficient to elucidate the cooperation between different enzymes in a complicated biological system. Hence, approaches that are capable of spatially profiling the activity of different enzymes in the same area of interest at the single-cell level and in vivo are needed to elucidate the links of multiple enzymes to life and pathophysiological processes.

Visualizing enzyme activity is largely performed using synthetic fluorogenic substrates3–5 . However, current fluorogenic probes fail to provide spatial information because the water-soluble fluorophores tend to diffuse away from the reaction sites6 . Recently, selfimmobilizing fluorogenic reporters have been developed to locate enzyme activities in dynamic environments7 . However, the covalent connection of bulky fluorophores to enzymes increases the risk of perturbing the function of the enzymes8,9 and, consequently, of disrupting the downstream signaling and cellular activity. Thus, the potential enzyme-silencing effects of the self-immobilizing strategy reduce its usefulness for mapping the activities of multiple enzymes in living systems.

Further developments in the field of enzyme activity imaging in living organisms derive from in situ enzymatic non-covalent synthesis (ENS)10 of small molecules into non-diffusive nanostructures to enable

1 Department of Electrical and Computer Engineering, Boston University, Boston, MA, USA. 2 Photonics Center, Boston University, Boston, MA, USA. 3 Department of Biomedical Engineering, Boston University, Boston, MA, USA. 4 Department of Chemistry, Brandeis University, Waltham, MA, USA. 5 Department of Chemistry, Boston University, Boston, MA, USA. 6 Department of Mechanical Engineering, Boston University, Boston, MA, USA. 7 These authors contributed equally: Hongjian He, Jiaze Yin.  e-mail: jxcheng@bu.edu

the retention of fluorescent modalities at reaction sites11,12. Notably, the characteristics of fluorophores are critical to the successful mapping of enzyme activity via ENS-based fluorescent probes13–15. These filter criteria largely reduce the choice of fluorophore candidates. Given the broad-band emission spectrum, current research using this strategy focuses mostly on the mapping of one kind of enzyme in one area of interest16, which is not sufficient to elucidate the cooperation between different enzymes in a biological process.

Beyond fluorescence, other technologies have been developed to map enzyme activity in cells and tissues17, including magnetic resonance imaging and mass spectrometry imaging18. However, poor spatial resolution or inapplicability to living organisms significantly restricts these approaches with regard to high-resolution mapping of the activity of multiple enzymes in living subjects.

Addressing this challenge requires innovations in imaging systems and in chemistry. Here, we present a method for visualizing enzyme activities via real-time mid-infrared photothermal (MIP) imaging of a category of nitrile-tagged enzyme activity probes. The recently developed MIP microscope enables chemical imaging with submicron spatial resolution by using a visible-light probe to sense the photothermal effect induced by mid-infrared absorption19,20. Importantly, such indirect measurement mitigates the huge water absorption issue and enables mid-infrared imaging in an aqueous environment with high contrast21. The reported sample-scan MIP microscope requires a pixel dwell time of 500 μs–10 ms19,20, making it difficult to resolve the movements of living systems. To address these difficulties we have developed a high-speed and high-sensitivity laser-scan MIP microscope. In this new system, high-speed imaging is achieved using a synchronized laser-scanning scheme, which produces a pixel dwell time as short as a few microseconds22. These efforts collectively enable real-time MIP imaging of living systems.

Although label-free MIP microscopy succeeds in visualizing the abundant cellular components19,20, direct observation of specific enzymatic reactions in cells and tissues remains difficult because the MIP signals from products are immersed in a strong background generated by the other biomolecules. To address this challenge, we synthesized a nitrile-tagged bio-orthogonal enzyme activity probe. The vibration frequency of the nitrile group (C≡N) differs from those of endogenous functional groups, thus exhibiting unique infrared absorbance in the cell-silent region23. The C≡N group has a relatively large infrared absorption cross-section and can serve as a sensitive photothermal reporter. Spectrally, the C≡N vibration is narrow-band and tunable through chemical and physical approaches, enabling super-multiplexed detection24. Thus, the adoption of C≡N as a photothermal reporter of biochemical reactions is promising for bio-orthogonal detection of multiple enzyme activities in living systems. Here, we synthesized a series of nitrile-tagged enzyme activity probes, named nitrile chameleons. The probes exhibit reaction-activatable MIP spectral shifts of C≡N, which signifies enzymatic reactions. These probes also undergo in situ ENS10 for mapping enzyme activity.

## Results

## Performance of a laser-scanning MIP microscope

Figure 1a illustrates the principle of mid-infrared photothermal imaging. A mid-infrared light excites the chemical bond through vibrational transition. The vibrational energy is transferred into the sample, which subsequently experiences a local temperature rise. The temperature escalation produces several photothermal effects such as thermal expansion and refractive index alteration. Those changes influence the scattering of a visible-light probe, which is adopted as the photothermal signal.

Previous MIP microscopes relied on sample scan with a pixel dwell time of 500 µs or longer21, which is insufficient to capture the dynamics of a living system. To increase the MIP imaging speed, we designed a laser-scan MIP microscope (Fig. 1b) that provides a much faster pixel resolution speed on the order of a few microseconds (Methods). This faster resolution speed enables visualization of fast dynamics in real time (20 Hz) at a small range with pixel counts under 25,000 (158 × 158). To provide high spatial resolution, counter-propagating geometry is used. Specifically, the visible beam is focused via a water immersion objective lens with a numerical aperture of 1.2, while the infrared beam is focused by a reflective objective with a numerical aperture of 0.5. The spatial resolution is characterized using poly(methyl methacrylate) (PMMA) particles with a known diameter of 200 nm (Fig. 1c). The resolution reached 300 nm, approaching the theoretical resolution of 276 nm estimated from the point spread function (Supplementary Information). The vertical resolution is determined to be 640 nm (Supplementary Fig. 1), resulting in a cubed voxel with lateral dimensions of 300 nm and axial dimensions of 640 nm. By synchronously scanning the infrared and visible beams with two pairs of galvanometer mirrors, a uniform field of view of more than 400 ×400 μm2 is reached (Fig. 1d).

For live cell imaging, we optimized the infrared excitation pulse width to maximize the signal-to-water background ratio. Regarding the photothermal dynamics, the water background is known to have a large decay constant (τB) due to the large heat capacity. The decay constant (τ ) for the signal from the organelles is usually smaller. We harness this difference to enhance the signal-to-background contrast by reducing the heating pulse duration τ (Supplementary Informa tion)25. Experimentally, we investigated the influence of heating pulse duration on the MIP contrast of a live cell in the protein channel (1,553 cm−1, amide II). A pulse duration of 50 ns provides the highest signal-to-background ratio with negligible photodamage (Fig. 1e and Supplementary Fig. 2). This enabled successful live cell MIP imaging in the protein channel (1,553 cm−1, Fig. 1f and Supplementary Video 1), and hence we retained these conditions for the following experiments unless otherwise specified.

## Nitrile-based enzymatic activity probes

We constructed two probes that selectively map the activity of phosphatase and caspase in living subjects because both phosphatase and caspase are critical to cell survival and cell death. Our phosphatase probe is generally applicable to different kinds of phosphatase such as alkaline phosphatase (ALP)11, protein tyrosine phosphatase26, acid phosphatase27 as well as other types of phosphatases. The enzyme activity probes consist of an enzymatic substrate, a nitrile group (C≡N) as the reporter of the enzymatic reaction and a self-assembly moiety (Fig. 2a,b). The nitrile-tagged probes for mapping the activity of cas pase and phosphatase are named Casp-CN(S) and Phos-CN(S), respec tively. The enzymatic products are named Casp-CN(P) and Phos-CN(P), respectively. The enzyme-catalyzed cleavage of the substrate alters the electronic donation from the para-position atoms (N or O), thus significantly changing the electron density as well as the vibrational frequency of C≡N. Consequently, in the MIP spectra the C≡N of the enzymatic product is spectrally separated from that before the enzymatic reaction. The MIP signal intensity of the C≡N of the enzymatic products positively correlates with the level of enzyme activity. This reaction-activatable peak shift of C≡N is not only an indicator of enzymatic reactions, but also enables detection of specific enzymatic products via bio-orthogonal chemical imaging in the cell-silent region28. Furthermore, we conjugated a self-assembly moiety to the probes (Fig. 2a,b) to enable in situ ENS for conserving the products at the reaction sites. ENS of the probes also amplifies the imaging contrast via aggregation-enhanced responsiveness29, a phenomenon likely to be caused by concentrating the target molecules inside the volume of imaging. The amphiphilicity of the probes enables a solubility exceeding 1 mM (Methods). We named this category of probes ‘nitrile chameleons’ because of the spectral shift of C≡N.

As shown in Fig. 2c, the MIP spectra of the C≡N bond of Casp-CN(S) and Casp-CN(P) (50 mM, in dimethylsulfoxide (DMSO)) have a sharp peak at 2,225 and at 2,205 cm−1, respectively, while Phos-CN(S) and

a  
![](images/249d0c27776faba30ada0602631b73eae1c7d911ad0b83e57412436260f006a5.jpg)

<details>
<summary>text_image</summary>

Pulsed IR pump
Non-radiative
relaxation
v = 1
v = 0
ΔT
Visible probe
Scattering intensity
</details>

b  
![](images/90e37187a8093d623a7f975efad94016f74a640431a161c5b9839f4f70d7d4c3.jpg)

<details>
<summary>text_image</summary>

QCL
PD2
GW2
CM1
CM2
Lock-in
PD1
RL
OL
CW 532 nm
BS
GV1
SL
TL
</details>

c  
![](images/ebdef055bab2db47cac5d6370e777f446abd7f578546cd552f9201798078dcc3.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing scattered pink dots on a black background with a scale bar and coordinate labels (x, y) and 1.729 cm⁻¹ annotation
</details>

![](images/5aa377f6f3c0f54c3ffe8e4c35c6b08ac315561b6009fd66a6ae93b7cfb3b11a.jpg)

<details>
<summary>line chart</summary>

| Distance (nm) | FWHM 311 nm Intensity (a.u.) | FWHM 306 nm Intensity (a.u.) |
| ------------- | ---------------------------- | ---------------------------- |
| 0             | 0.0                          | 0.0                          |
| 500           | 0.2                          | 0.1                          |
| 1000          | 1.2                          | 1.2                          |
| 1500          | 0.2                          | 0.1                          |
</details>

d  
![](images/2c8362d2b8ae77522c58a9851e88d04e31d59464675a84ab27c6700886973dbd.jpg)

<details>
<summary>line chart</summary>

| Distance (μm) | SNR     |
| ------------- | ------- |
| 0             | 10      |
| 50            | 100     |
| 100           | 100     |
| 150           | 100     |
| 200           | 100     |
| 250           | 100     |
| 300           | 100     |
| 350           | 100     |
| 400           | 10      |
| 450           | 1       |
| 500           | 1       |
</details>

f  
![](images/f739471fe03abccde025ae98345a4a66fc731a3d9c57e387d961bebb313e9069.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing blue fluorescent cellular structures with a white arrow pointing to a specific region (no text or symbols present)
</details>

![](images/8444a88b670129a54a1ddf0a6e6cfd393e315db9c531725f6f961dc8e6199ad2.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of cellular structures with blue fluorescence, labeled '15 s' and an arrow pointing to a specific cell (no text or symbols beyond labels)
</details>

![](images/2c24f6ae6466cd3f34207dfef454ae01d7518dcd71824aec347b01fffedf0264.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing blue fluorescent cellular structures with a 5-second time marker (no text or symbols beyond label)
</details>

![](images/ea28d774010a56139e707b1abb3bd22c783cf3f567eee4a47e1c7ed8fe703429.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing blue fluorescent cellular structures with a 20-second time marker (no text or symbols beyond label)
</details>

e  
![](images/a30b31236f15a59096ce285246689a1f7e3aca49c78319fe0e2d7ff9528324eb.jpg)

<details>
<summary>text_image</summary>

Water background
τIR = 50 ns, SBR: 6.5
τIR = 100 ns, SBR: 2.4
τIR = 200 ns, SBR: 1.9
τIR = 300 ns, SBR: 1.7
225
0
</details>

![](images/41629f28dc104c546845511ee0daccf0f4e9862ad3e1e2181a422e9ef715b32f.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing blue fluorescent cellular structures with a 10-second time marker (no text or symbols beyond label)
</details>

![](images/9add4fb2e69d30e9f92189a3eda4ca859f69a403723a3f05c1fe9fa22f274f84.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing cellular structures with a 30-second time label and an arrow pointing to a specific region (no text or symbols beyond labels)
</details>

Fig. 1 | Laser-scan MIP microscope for real-time bond-selective imaging of live cells at 300 nm spatial resolution. a, Principle of MIP detection. IR, infrared. b, Schematic illustration of a MIP microscope. BS, beam splitter; CM, concave mirror; CW, continuous-wave laser; DM, dichroic mirror; GV, galvanometer mirror; lock-in, lock-in amplifier; OL, objective lens; PD, photodiode; QCL, quantum cascade laser; RL, reflective objective lens; SL, scan lens; TL, tube lens. c, Spatial resolution characterized using 200-nm-diameter PMMA particles. FWHM, full  
width at half-maximum. d, Characterization of uniformity by MIP imaging of the signal-to-noise ratio (SNR) of 500-nm-diameter PMMA particles, showing that uniformity is >400 μm. e, MIP imaging (1,553 cm−1, amide II) of proteins in SJSA-1 cancer cells using different IR excitation pulse widths. SBR, signal-to-background ratio. f, Live cell MIP imaging of protein dynamics (1,553 cm−1, amide II) in OVCAR5 cancer cells. All experiments in c–f were repeated independently three times with similar results. Scale bars: c, 2 μm; d, 50 μm; e, 20 μm; f, 10 μm.

Phos-CN(P) (50 mM, in DMSO) have a narrow-band MIP spectrum of C≡N with a peak at 2,239 and at 2,221 cm−1, respectively (Fig. 2d). These distinctive peaks of C≡N guarantee multicolor MIP imaging of the nitrile probes and the corresponding enzymatic products. Moreover, the MIP signal intensity of the C≡N bond in the enzymatic products is linearly proportional to the concentration with a limit of detection of around 5 μM (Fig. 2e,f and Supplementary Fig. 3).

Next, we evaluated the enzymatic conversion efficiency of Casp-CN(S) by caspase-3 (active) and that of Phos-CN(S) by ALP (Fig. 2g,h). According to time-course analysis of product formation, the initial speed (v ) is 0.23 nmol−1 min−1 for Casp-CN(S) by caspase-3, and 0.29 nmol−1 min−1 for Phos-CN(S) by ALP. The $\scriptstyle { \boldsymbol { \nu } } _ { 0 }$ is slightly lower than that for standard substrates (Ac-DEVD-pNA, 0.33 nmol min−1, and P-nitrophenyl phosphate, 0.53 nmol min−1) in identical conditions (Supplementary Fig. 4). No reaction occurred in the mixture of Phos-CN(S) or Casp-CN(S) with phosphate-buffered saline (PBS), carboxylesterase-1 (CES-1), matrix metalloproteinase-2 (MMP-2) and proteinase K (Fig. 2i,j), confirming the enzyme specificity for the reporters. Transmission electron microscopy images of Casp-CN(S) and Phos-CN(S) (50 μM, in PBS) show sparsely distributed small nanoparticles formed by the self-assembly of the probes (Fig. 2k,l). Bulky nanofilaments formed by the self-assembly of products are observed after incubating the probes with the corresponding enzymes for 1 hour (Fig. 2k,l). Thioflavin T (ThT) was used to examine the kinetics of nanofibril formation by the enzymatic products30. As shown in Fig. 2m,n, ThT fluorescence surges within 10 seconds upon mixing with the enzymatic products (10 μM, PBS), suggesting a minimal nucleation phase and rapid nanoaggregate formation30. Thus, the enzymatic products settle near enzymes due to fast aggregation. Thermodynamically, the chemical potential of nanoaggregate formation is positively linked to monomer concentration31. Therefore, nanofibers predominantly develop near the enzymes because of the maximized product monomer concentration through local generation. However, according to Fick’s law of diffusion, the distant product molecules are much less likely to assemble into nanofibers due to reduced concentration. These kinetic and thermodynamic factors ensure that the nanoaggregates spatially associate with enzymes, thereby enabling the spatial mapping of enzyme activities.

## Real-time MIP imaging of enzyme activities in living cells

As shown in Fig. 3a, the probes enter the cells and react with the corresponding enzymes, generating products that produce MIP signal at new wayvenumbers. The MiP signal intensity from products is correlated with enzyme activity. The ENS of probes produces non-diffusive nanofilaments that uncover the reaction sites and enhance the imaging contrast by aggregation-enhanced responsiveness29. We first used this approach to map the activity of phosphatase in SJSA-1 cells, an osteosarcoma cell line with high phosphatase expression. A working concentration of

a  
![](images/ef0cd1cd0949380e70bed4aecd9d89db96d8c818dfe18fcc4764533f63aae958.jpg)

<details>
<summary>chemical</summary>

Chemical reaction scheme showing Caspase substrate modification with GDEVD and Casp-CN(S)/Casp-CN(P) reporter steps
</details>

c  
![](images/92e8318ee83e889177fc4865838b368f4bcd961fb156804af88ffa303308cdc5.jpg)

<details>
<summary>line chart</summary>

| Wavenumber (cm⁻¹) | Normalized MIP intensity (a.u.) |
| ----------------- | ------------------------------- |
| 2205              | 1.0                             |
| 2225              | 1.0                             |
</details>

e

![](images/4bb982492b99b7c57b130ed0b80474309bb3217b0e5ed07dfa851e4905c281cd.jpg)

<details>
<summary>line chart</summary>

| μM | MIP intensity (a.u.) |
| --- | --- |
| 0 | 3 |
| 10 | 7 |
| 20 | 14 |
| 40 | 28 |
| 60 | 38 |
</details>

g  
![](images/d0da161ff067b704819dc33f2667926615a8de533e6503fc454f6c537767bf48.jpg)

<details>
<summary>line chart</summary>

| Time (min) | ΔProduct/nmol |
| ---------- | ------------- |
| 0          | 0             |
| 10         | 1             |
| 20         | 2             |
| 30         | 3             |
| 40         | 4             |
| 50         | 4.5           |
| 60         | 5             |
</details>

b  
![](images/69590d85a17a1858a5267a4fb6031bf7ca3080832e3dfec91c8fce1fd22ed884.jpg)

<details>
<summary>chemical</summary>

Chemical reaction scheme showing phosphatase-substrate interaction with Phos-CN(S) and Phos-CN(P) under self-assembly moiety
</details>

d  
![](images/c27a01f161151307ba5d2365f92c1a64d0a8176738c479494d28563094dab547.jpg)

<details>
<summary>line chart</summary>

| m/z (cm⁻¹) | Phos-CN(P) | Phos-CN(S) |
| ---------- | ---------- | ---------- |
| 2,221      | 0.0        | 0.0        |
| 2,239      | 0.0        | 0.0        |
</details>

f

![](images/9489764ed310e67d4d1ce4d45e8b343442b04b94468084ddf2f363e0352d6a44.jpg)

<details>
<summary>line chart</summary>

| μM | MIP intensity (a.u.) |
| --- | --- |
| 10 | 5 |
| 20 | 12 |
| 30 | 20 |
| 60 | 38 |
</details>

h  
![](images/52bd1eae568a61afb12802b6be494819c8439a814a30d32375012d14a603025b.jpg)

<details>
<summary>line chart</summary>

| Time (min) | ΔProduct/nmol |
| ---------- | ------------- |
| 0          | 0             |
| 10         | 2             |
| 20         | 4             |
| 30         | 6             |
| 40         | 8             |
| 50         | 10            |
| 60         | 12            |
</details>

i  
![](images/3a03741532fc18b85aa16dad55e7202880a5753667ac2a85ea9b49e447299b3d.jpg)

<details>
<summary>bar chart</summary>

| Protein        | ΔAbsorbance (a.u.) |
| -------------- | ------------------ |
| ALP            | 0.001              |
| CES-1          | 0.001              |
| Caspase-3      | 0.032              |
| Proteinase K   | 0.001              |
| MMP-2          | 0.001              |
| PBS            | 0.001              |
</details>

![](images/1423037c3c6f6f9980313bd2bcbed0a610d53e8089ef52d85bc3e6b2de379d62.jpg)

<details>
<summary>text_image</summary>

k
Casp-CN(S)
Caspase-3 (1 h)
Nanofilaments
</details>

m  
![](images/09795865b585b87a2b93a3ca8dd3aa11fa7e097407984219a2d8fd15c7efc091.jpg)

<details>
<summary>line chart</summary>

| Time (s) | ΔThT intensity (a.u.) |
| -------- | --------------------- |
| 0        | 0.0                   |
| 5        | 0.1                   |
| 10       | 0.3                   |
| 15       | 0.4                   |
| 20       | 0.5                   |
| 25       | 0.6                   |
| 30       | 0.7                   |
| 35       | 0.8                   |
| 40       | 0.9                   |
| 45       | 1.0                   |
| 50       | 1.1                   |
| 55       | 1.2                   |
| 60       | 1.3                   |
</details>

j  
![](images/983d91c0b67ad64a92a1cd0a57d10dae19d8bf9857860b5eabe91b8719268398.jpg)

<details>
<summary>bar chart</summary>

| Compound     | ΔAbsorbance (a.u.) |
| ------------ | ------------------ |
| ALP          | 0.06               |
| CES-1        | 0.005              |
| Caspase-3    | 0.002              |
| Proteinase K | 0.001              |
| MMP-2        | 0.001              |
| PBS          | 0.001              |
</details>

![](images/8d5710efbed3859c5a8408dfa2dadcbcd15b28533843b135dad77786b1bec8d1.jpg)

<details>
<summary>text_image</summary>

Phos-CN(S)
ALP (1 h)
Nanofilaments
</details>

n  
![](images/50b1d3d2b32d5cb38c622a502b0d6fc575f3a8765dae9559c7c3bd308ff1ad92.jpg)

<details>
<summary>line chart</summary>

| Time (s) | ΔThT intensity (a.u.) |
| -------- | --------------------- |
| 0        | 0.0                   |
| 10       | 0.5                   |
| 20       | 1.0                   |
| 30       | 1.5                   |
| 40       | 1.7                   |
| 50       | 1.9                   |
| 60       | 2.0                   |
</details>

Fig. 2 | Development of nitrile chameleons for mapping specific enzyme activity. a, Molecular structures of Casp-CN(S) and the enzymatic product Casp-CN(P). b, Molecular structures of Phos-CN(S) and the enzymatic product Phos-CN(P). c, MIP spectra of Casp-CN(S) and the enzymatic product Casp-CN(P), 50 mM in DMSO. d, MIP spectra of Phos-CN(S) and the enzymatic product Phos-CN(P), 50 mM in DMSO. e,f, MIP signal intensity of Casp-CN(P) (e) and Phos-CN(P) (f) at different concentrations in DMSO. g, Time-dependent formation of Casp-CN(P) catalyzed by active caspase-3 (25 U ml−1). RT, room temperature. h, Time-dependent formation of Phos-CN(P) catalyzed by ALP (0.5 U ml−1). i,j, UV  
absorbance change in the mixtures of Casp-CN(S) (i) or Phos-CN(S) (j) with PBS, ALP, caspase-3 (active), carboxylesterase-1 (CES-1), matrix metalloproteinase-2 (MMP-2) and proteinase K. k, Transmission electron microscopy (TEM) images of the nano-assemblies formed by Casp-CN(S) before and after the addition of active caspase-3 (25 U ml−1, 1 h). TEM imaging was repeated independently three times with similar results. l, TEM images of the nano-assemblies formed by Phos-CN(S) before and after the addition of ALP (1 U ml−1 1 h). TEM imaging was repeated independently three times with similar results. m,n, Self-assembly kinetics of the enzymatic products Casp-CN(P) (m) and Phos-CN(P) (n). Scale bars: k,l, 100 nm.

50 μM was chosen based on cytotoxicity assay (Supplementary Fig. 5). All MIP images in the cell-silent window undergo a subtraction of water background as described in Methods unless otherwise indicated. After the treatment of Phos-CN(S) (1 h), a pinpointed MIP spectrum in the silent window inside a cell (see Methods for details on choosing the pinpointed area) exhibits a sharp peak at 2,174 cm−1 arising from the C≡N of the dephosphorylated products (Phos-CN(P)), and a smaller peak at 2,215 cm−1 originating from the C≡N of Phos-CN(S) (Fig. 3b).

This MIP spectrum identifies the optimal wavenumbers for imaging and validates the intracellular chemical components. The peaks of the C≡N inside cells shift compared with that in DMSO (Fig. 2d), probably due to the Stark effect32. Live cell MIP imaging at 1,745 cm−1 visualizes the profiles of lipid droplets in SJSA-1 cells (Fig. 3c). Subsequent MIP images of the same cells at 2,174 cm−1 show strong signal from Phos-CN(P), while the intracellular MIP signal from Phos-CN(S) at 2,215 cm−1 is weaker (Fig. 3c,d). These results suggest an efficient cellular uptake of the phosphatase activity probe, and that the phosphatases in SJSA-1 cells substantially convert Phos-CN(S) to Phos-CN(P), demonstrating robust intracellular phosphatase activity.

a  
![](images/4dc0f13fe94fabc5eebad84abed78dd7631cd934e3ce2a5691ee4758863142e1.jpg)

<details>
<summary>text_image</summary>

MIP spectrum
Probe-C≡N
+
Enzyme
Product-C≡N
ENS
Substrate
MIP spectrum
MIP intensity
Wavenumber
Shift
Wavenumber
</details>

b  
![](images/5b15d3c57e81630f4715df534674484f63324a91a17b97cb7a0cdc4c33987d2d.jpg)

<details>
<summary>line chart</summary>

| cm⁻¹    | MIP intensity (a.u.) |
| ------- | -------------------- |
| 2,174   | 1.0                  |
| 2,215   | 0.6                  |
</details>

c  
![](images/99e7d55262286255e02695c31762294518393f82af32a0f72ae9555f2cc90ee5.jpg)

<details>
<summary>text_image</summary>

Transmission
Lipids
0.43
Phos-CN(P)
2,174 cm⁻¹
0.1
Phos-CN(S)
2,215 cm⁻¹
0.50
Phos-CN(P)
2,174 cm⁻¹
</details>

d  
![](images/c11ad086159e8ce3bfb2def4b37a8a29e12e374b0181bf404730f38703ee627c.jpg)

<details>
<summary>scatterplot</summary>

| Category   | MIP intensity (a.u.) |
| ---------- | -------------------- |
| Product    | 12                   |
| Product    | 14                   |
| Product    | 16                   |
| Product    | 20                   |
| Substrate  | 6                    |
| Substrate  | 7                    |
| Substrate  | 8                    |
</details>

g  
![](images/0dfcaa01bd6f31a3d14432404744b761aa0a5cf82e0b64c8f792be36a1ca0845.jpg)

<details>
<summary>scatterplot</summary>

| Group     | MIP intensity (a.u.) |
| --------- | -------------------- |
| Control   | 3.5                  |
| Inhibitor | 1.5                  |
</details>

e  
![](images/9056d9495d207b4653d2122836c61498b8c16b765513315db32dbcd946bbf512.jpg)

<details>
<summary>text_image</summary>

Transmission
Lipids
0.43
Phos-CN(P)
1,745 cm⁻¹
2,174 cm⁻¹
Phos-CN(S)
2,215 cm⁻¹
0.50
Phos-CN(P)
2,174 cm⁻¹
</details>

f  
![](images/6d6f67cad600ce8543f97e3ffb1e4e052bc4f8fa1cfe4bb0f4b3080ab31c03f7.jpg)

<details>
<summary>scatterplot</summary>

| Group     | MIP intensity (a.u.) |
| --------- | -------------------- |
| Product   | 8                    |
| Product   | 10                   |
| Product   | 12                   |
| Product   | 6                    |
| Product   | 4                    |
| Substrate | 8                    |
| Substrate | 10                   |
| Substrate | 13                   |
| Substrate | 6                    |
| Substrate | 4                    |
</details>

h  
![](images/6e70098a5125ccbc85715991f8f6e78ce66dc8ae3583293a0f1ff8c8a3baa7ba.jpg)

j  
![](images/a626ad6477ea1a91cbaba2c373c07b7707d6054b2a5c9ec098bc545303cb3ace.jpg)

<details>
<summary>text_image</summary>

Transmission
10 min
15 min
25 min
35 min
50 min
AOI
</details>

i  
![](images/ca8fe8ce5389c4ff35e2cb78b7c185dd08202313ea19e2f272206ee2fa0f4544.jpg)

<details>
<summary>scatterplot</summary>

| Wavelength | SNR (Red Dots) | SNR (Green Dots) |
| ---------- | -------------- | ---------------- |
| 2.174 cm⁻¹ | ~30            | ~60              |
| 488 nm     | ~50            | ~70              |
</details>

k  
![](images/35ac163e7643811e71fea56d9cc60b5a6f4ccf5841ac7fa6ca24a0f8c806d677.jpg)

<details>
<summary>line chart</summary>

| cm⁻¹   | MIP intensity (a.u.) |
| ------ | -------------------- |
| 2,163  | 1.0                  |
| 2,225  | 0.9                  |
</details>

l  
![](images/8c07bb188cc1fc787691fe092a0a9df9fa24d8617779b335e98480c61ca62bcf.jpg)

<details>
<summary>text_image</summary>

DC channel
Lipids
1,745 cm⁻¹
0.9
0.1
Casp-CN(P)
2,163 cm⁻¹
Casp-CN(S)
2,225 cm⁻¹
0.45
0.02
Casp-CN(P)
Zoom in
2,163 cm⁻¹
</details>

m  
![](images/ddaa8a33e4a34ecbc81a8371c6d6ced6b3404f2b3d26a4b435432ffd73fdb456.jpg)

<details>
<summary>scatterplot</summary>

| Category   | MIP intensity (a.u.) |
| ---------- | -------------------- |
| Product    | 20                   |
| Product    | 30                   |
| Product    | 15                   |
| Product    | 10                   |
| Substrate  | 10                   |
| Substrate  | 15                   |
| Substrate  | 5                    |
</details>

Fig. 3 | Real-time MIP imaging of nitrile chameleons generates the activity maps of caspase-3/7 and phosphatase in living cells. a, Schematic diagram of the principle of enzyme activity mapping by real-time MIP imaging of nitrile chameleons. b, Pinpointed MIP spectrum, indicated by the arrow in c. c, MIP images of phosphatase activity profile in living SJSA-1 cells incubated with Phos CN(S). The zoom-in of the dashed box is given on the far right. d, Quantification of MIP signal intensity of Phos-CN(S) and Phos-CN(P) in cells (n = 10 cells). Data are given as mean ± s.d. e, MIP images of phosphatase activity profile in phosphatase inhibitor-pretreated SJSA-1 cells incubated with Phos-CN(S). The zoom-in of the dashed box is given on the far right. f, Quantification of MIP signal intensity of Phos-CN(S) and Phos-CN(P) in phosphatase inhibitor-pretreated SJSA-1 cells (n = 10 cells). Data given as mean ± s.d. g, Quantification of [P]/[S]  
in the cells from PIC-pretreated and PIC-free groups (n = 11 cells). Data given as mean ± s.d. h, Confocal fluorescence image of SJSA-1 cells incubated with NBD-labeled phosphatase activity reporter (NBD-Phos-CN(S), 50 μM, 1 h). i, Comparison of SNR between MIP imaging of C≡N (at 2,174 cm−1) and fluorescence imaging of NBD in cancer cells at 488 nm. Each dot represents a cell (n = 10 cells). Data given as mean ± s.d. j, Time-course MIP images of the phosphatase activity (at 2,174 cm−1) as Phos-CN(S) (50 μM in PBS, room temperature) was added to SJSA-1 cells. AOI, area of interest. k, Pinpoint MIP spectrum, indicated by the arrow in l. l, MIP images of caspase-3/7 activity profile in Dox-pretreated SJSA-1 cells incubated with Casp-CN(S). The zoom-in of the dashed box is given on the far right. m, Quantification of MIP intensity of Casp-CN(S) and Casp-CN(P) in Dox-pretreated cells (n = 10 cells). Data given as mean ± s.d. Scale bars, 30 μm.

Instead of a diffuse distribution, Phos-CN(P) highlights intricate subcellular structures as shown by the variations in MIP intensity in the mapping (Fig. 3c), indicating a heterogeneous biodistribution of phosphatase activity. To verify the non-diffuse property of nanofilaments in cells, we incubated cancer cells with Phos-CN(S) (1 hour) followed by fixation. We then sequentially captured two MIP images in the same field of view at a 1 hour interval. Little movement occurred during the 1 hour interval (Supplementary Fig. 6), suggesting that the nanofilaments are highly immobile inside cells. Although the Stokes–Einstein equation suggests high mobility for 100 nm particles in water, the nanofilaments formed by enzymatic products exhibited non-diffusive behaviors in the cells, probably due to the intertwining of nanofilaments, which creates rigid nano-networks that interact with cellular structures33, thus restricting the mobility in the cellular environment. Such immobility ensures the spatial accuracy of enzyme activity mapping. However, the dissolved portion of Phos-CN(S) is not visible due to the lack of aggregation-enhanced responsiveness. Integrated MIP and widefield fluorescence imaging indicate good colocalization (Pearson’s r = 0.7, Supplementary Fig. 7) between the MIP signal from Phos-CN(P) and the immunofluorescence from phosphatase antibodies (for example, anti-ALP), confirming the high spatial accuracy of mapping. As a control, MIP contrast was not seen at 2,174 cm−1 in the cells that did not have Phos-CN(S) treatment (Supplementary Fig. 8a). These results collectively confirm the successful mapping of phosphatase activity in living SJSA-1 cells by real-time MIP imaging of the nitrile chameleon.

Phosphatase inhibitor cocktail (PIC)-pretreated SJSA-1 cells incubated with Phos-CN(S) have a punctate distribution of Phos-CN(P) and Phos-CN(S) with much weaker MIP signals (Fig. 3e,f) than the cells from the inhibitor-free group (Fig. 3c,d), which agrees with the phosphatase activity inhibition. This confirms that Phos-CN(S) can delineate spatiotemporal phosphatase activity change in cells. Given that the phosphatase level (for example, ALP) in cells remains unchanged after PIC treatment (Supplementary Fig. 9), the relative enzyme catalytic efficiency $( \mathsf { k } _ { \mathrm { c a t } } / \mathsf { K } _ { \mathsf { M } } )$ of phosphatase between the cells from PIC-pretreated and inhibitor-free groups can be approximately determined using the product-to-substrate ratio in cells ([P]/[S], that is, the ratio of intracellular MIP intensity at $2 , 1 7 4 \thinspace { \mathrm { c m } } ^ { - 1 }$ to that at 2,215 cm−1) (Supplementary Information). The effect of PIC-induced inhibition on the $\sf k _ { \mathrm { c a t } } / \sf K _ { \mathrm { M } }$ of phosphatase in cells can be evaluated using this relative value. On statistical analysis, the average [P]/[S] in PIC-pretreated cells is 2.5-fold lower than that in the PIC-free group (Fig. 3g), indicating that the average ${ \sf k } _ { \mathrm { c a t } } / { \sf K } _ { \mathrm { M } } \mathbf { o f }$ the phosphatase in SJSA-1 cells decreases by 60% through PIC treatment.

Although the limit of detection of enzymatic products in DMSO is approximately 5 μM, the minimum detectable concentration of the same molecules in cells, upon nanofilament formation, is estimated to be around 600 nM (Supplementary Information). Due to the uneven distribution of nanoaggregates in water, we used hyperspectral MIP images of Phos-CN(P) suspensions at a concentration as low as 800 nM in PBS to substantiate this calculation. The peak of the nitrile group is discernible in the spectrum obtained from the hyperspectral images (Supplementary Fig. 10), confirming the sub-micromolar sensitivity of MIP in detecting the nano-assemblies of enzymatic products. To further validate the high sensitivity of MIP imaging, we compared the MIP images to the fluorescence images of cells incubated with NBD-Phos-CN(S), a nitrobenzofurazan (NBD)-tagged Phos-CN(S) (Supplementary Scheme 1). On statistical analysis, the MIP images of C≡N at 2,174 cm−1 (Supplementary Fig. 11) and fluorescence images of NBD (Fig. 3h) of the cancer cells incubated with NBD-Phos-CN(S) (50 μM, 1 h) had a similar signal-to-noise ratio (Fig. 3i). Here, signal-to-noise ratio is the mean signal intensity in cells divided by that of a blank area. Given that C≡N and NBD exist in the molecule in a 1:1 ratio, this indicates that the detection ability of C≡N by MIP is similar to that of NBD by fluorescence in cells. Furthermore, MIP imaging outperforms fluorescence imaging because it is photobleaching free (Supplementary Fig. 12), making it more suitable for observing continuous events in living systems.

Considering the high sensitivity and resistance to photobleaching, we conducted real-time monitoring of dephosphorylation reaction in cells using MIP imaging as Phos-CN(S) is introduced to the cells. As shown in Fig. 3j, within 10 minutes of Phos-CN(S) addition, distinct puncta of dephosphorylated products were observed, indicating an efficient endocytosis-dependent cell entry and early endosomal dephosphorylation. Between 15 and 50 minutes, the MIP signal of enzymatic products appeared in other cellular regions as a crooked-stripe pattern, indicating that Phos-CN(S) escaped from the endosomes and underwent dephosphorylation by the phosphatases in various cellular locations. The nanoparticles formed by the amphiphilic nitrile chameleons may escape from endosomes through endosomal membrane disruption or perforation34. The variation in phosphatase activity patterns at different time points is attributed to the dynamic movements of cellular structures inside live cells. As previously discussed, the nanofilaments intertwine with cellular structures, causing the nanofilaments to move along with these structures. Furthermore, we used NBD-Phos-CN(S) to study the cellular uptake mechanism of nitrile chameleons because NBD fluorescence cannot distinguish between substrate and product. As shown in Supplementary Fig. 13, NBD fluorescence inside the cells was significantly reduced by ATP synthetase inhibitor (oligomycin, 5 μM), suggesting that the internalization of the probes occurs through endocytosis.

Other than phosphatase, we profiled caspase-3/7 activity in live cancer cells. Doxorubicin (Dox) efficiently induces apoptosis in SJSA-1 cells for the purpose of activating caspase-3/7 (Supplementary Fig. 14). After incubation with Casp-CN(S) (50 μM, 1 h), a pinpointed MIP spectrum inside a cell exhibits a sharp peak at 2,163 cm−1 arising from the C≡N in Casp-CN(P), and a smaller peak originating from the C≡N in Casp-CN(S) at 2,225 cm−1 (Fig. 3k). This MIP spectrum provides the optimal wavenumbers for imaging and validates the intracellular chemical compositions. MIP imaging at 1,745 cm−1 generates a map of lipid droplets in the cells (Fig. 3l). MIP images of the Dox-pretreated SJSA-1 cells show an intense MIP signal from Casp-CN(P) at $2 , 1 6 3 \mathsf { c m } ^ { - 1 }$ and a weaker signal from Casp-CN(S) at 2,225 cm−1 with detailed spatial information (Fig. 3l,m). This indicates efficient internalization of the caspase activity probe by cells, and a high caspase-3/7 activity in the Dox-pretreated SJSA-1 cells. Colocalization between Phos-CN(S) and Phos-CN(P) (Fig. 3c), as well as between Casp-CN(S) and Casp-CN(P) (Fig. 3l), is observed, suggesting the co-assembly between probes and products into non-diffusive nanofilaments during ENS35–37. Tandem MIP and widefield fluorescence imaging confirmed a high spatial correlation between the MIP signal from Casp-CN(P) and the immunofluorescence from caspase-3 (active) antibody (Pearson’s r = 0.72, Supplementary Fig. 7). These results confirm the precise mapping of caspase-3/7 activity in apoptotic cells. The nitrile chameleons are non-cytotoxic (Supplementary Fig. 5), but incubation of the cancer cells with Casp-CN(S) pro duced a weak but non-zero MIP signal from Casp-CN(P) (Supplementary Fig. 15a). This signal disappeared upon pretreatment with caspase-3/7 inhibitors (Supplementary Fig. 15b). Together, these results indicate the presence of low levels of caspase-3/7 activity in non-apoptotic cells38–40

The hydrophobic enzymatic products show little interaction with the plasma membrane or the lipid droplets (Fig. 3c,l). Interestingly, the overall MIP intensity of C≡N increases along with the enzymatic cleavage in the cells (Fig. 3c–f,l and Supplementary Fig. 16), despite the same import efficiency of probe molecules into different cell populations. This phenomenon can be explained by the assembly of products and substrates into non-diffusive nanofilaments after enzymatic cleavage, leading to improved imaging detectability and cellular retention41 of C≡N. The increased detectability arises from a higher molecular density in the imaging volume, enabling the target signals to stand out from background noise (Supplementary Fig. 16a). Consequently, nanofibe formation corresponds to elevated C≡N accumulation and imaging detectability inside cells, leading to higher MIP signal intensity. Incubation of cancer cells with control probes (Supplementary Scheme 2)42,43 resistant to caspase-3/7 and phosphatase produced negligible MIP signal in cells at the wavenumber of the enzymatic products (Supplementary Fig. 8b,c), supporting the accuracy of enzyme activity detection by MIP imaging of nitrile chameleons.

a  
![](images/e8c0588cae68d683478539987e19fc303031bcab5c401e068b0af1e1db93454d.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing cellular or particulate structures labeled 'Transmission' (no other text or symbols visible)
</details>

![](images/c4ce0b0bce0e65278678d8a8797d43a4665c10f8da8817ecabbc867f0b4394ad.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of Amide II with purple fluorescence, scale bar 1,553 cm⁻¹ (no text or symbols beyond label)
</details>

![](images/c48a6945076380b5545c9f4de6a6f9db956da137afd82aa45dd31a7553a38ca9.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescently labeled lipids with a scale bar of 1,745 cm⁻¹ (no text or symbols beyond label)
</details>

![](images/4b6ecaeca71bea47f6e05964d3c3df60d111edcdb058ad5e76b20031beacdcc5.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing green-labeled phosphatase structures with a 2,174 cm⁻¹ scale bar (no text or symbols beyond labels)
</details>

![](images/906e1bf988f99676e7658951f8a84f3b34d84f1fb7b2aca305a646529965b6d6.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of Caspase-3/7 cells with red fluorescence, showing a 2,163 cm⁻¹ scale bar (no text or symbols beyond label)
</details>

![](images/d37d16aac1530ec6e1ef4763510f3a3eee58f52fb09f532b2fc5e7def5ea267d.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing merged red and green cellular signals (no text or symbols)
</details>

b  
![](images/7c06b05b989bd0d0f9b7cbcbf518e64ef4c21f159f2f3b90544583cccf1f27c5.jpg)

<details>
<summary>heatmap</summary>

| Value (cm⁻¹) |
| :--- |
| 2,174 |
| 2,163 |
</details>

Green: phosphatase Red: caspase-3/7 Yellow: overlap  
![](images/9d3140e8071a08989da3019ffe63d04f2444ef730332394b2c14f1ce9cf43655.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing green-labeled cells against a black background, with 'Zoom in' label above (no other text or symbols)
</details>

![](images/d8adbad403c050ecc6854cdaf115260b03e23ffa2fe57100b4b5aa5eede2b4a7.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing red fluorescent cellular structures against a black background, labeled 'Zoom in' at top (no other text or symbols)
</details>

![](images/f9208222f628b134c770e830d60f0f849f9e3f53173004f0feb8b7e15ab8ff18.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red and green cellular structures (no text or symbols)
</details>

c  
![](images/1228aca22234485a3c6bec0cc81d76d6f8147c6d529588be06552cf17e334928.jpg)

<details>
<summary>text_image</summary>

Transmission
i
ii
iii
</details>

![](images/934d8d5100f8bc6a23eeacf77bb5f1b08dc476f0626c403e16e034b60d3b7f22.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red and green cellular staining with AOI label (no text or symbols beyond label)
</details>

![](images/d3380d5602a9b30ef72f676060b4b86fdb1389a43270e3a88115a883080f11e7.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing red and green labeled cells against a black background, with an arrow pointing to a specific cell (no text or symbols present)
</details>

![](images/72a205fbad2e72c5e5f9ee67a0084ee34311d5eca40657d3e08dc80ce89c6853.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing red and green cellular structures with AOI label (iii) and scale bar, no readable text or symbols beyond labels
</details>

e  
![](images/977d011678d6205c98af9d6f3c6423a717dbc48ae6df00e5cb2af92ad1ba3d88.jpg)

<details>
<summary>scatterplot</summary>

| Phosphatase activity | Caspase activity |
| --------------------- | ---------------- |
| 40                    | 40               |
| 50                    | 50               |
| 60                    | 60               |
| 70                    | 70               |
| 80                    | 80               |
| 90                    | 90               |
| 100                   | 100              |
| 110                   | 110              |
| 120                   | 120              |
| 130                   | 130              |
| 140                   | 140              |
</details>

d  
![](images/5eeb8f13ee26df0ecf6a7603de051d4ce24215450158a95b42fa29f5668d3fa8.jpg)

<details>
<summary>line chart</summary>

| μm | MIP intensity (a.u.) |
| --- | --- |
| 0 | 16 |
| 2 | 8 |
| 4 | 26 |
| 6 | 40 |
| 8 | 36 |
| 10 | 28 |
| 12 | 24 |
| 14 | 22 |
| 16 | 20 |
| 18 | 14 |
| 20 | 4 |
| 22 | 5 |
| 24 | 3 |
</details>

![](images/ac69f3c6fd2473145185b1d42517eb583597103721e3b5f64c059c20e7f63628.jpg)

<details>
<summary>line chart</summary>

| μm | AOI: ii |
| --- | ------- |
| 0   | 6       |
| 1   | 32      |
| 2   | 40      |
| 3   | 42      |
| 4   | 18      |
| 5   | 30      |
</details>

![](images/52f30843e285ed0478085fa30a3f067dcddc5fb07f6a371d0010dec1799eeec4.jpg)

<details>
<summary>line chart</summary>

| μm | AOI: iii |
| --- | -------- |
| 0   | 10       |
| 1   | 35       |
| 2   | 55       |
| 3   | 40       |
| 4   | 35       |
| 5   | 30       |
| 6   | 5        |
| 7   | 0        |
</details>

![](images/03351724e3a43618e9e70bdcb25aa92f90c09ba8d8d784f35aa6301e8167b21f.jpg)

<details>
<summary>bar chart</summary>

| Dox (μM) | No inhibitor | 8,000:1 | 4,000:1 |
| -------- | ------------ | ------- | ------- |
| 1.5      | 20           | 42      | 48      |
| 0.5      | 30           | 58      | 65      |
</details>

Fig. 4 | Multicolor MIP imaging of nitrile chameleons in live cancer cells provides evidence of caspase–phosphatase cooperation in apoptosis. a, Simultaneous visualization of the phosphatase and caspase-3/7 activity profile in Dox-pretreated SJSA-1 cells incubated with Phos-CN(S) and Casp-CN(S). The experiment was repeated independently 12 times with similar results. b, Colocalization analysis of the mapping in a. Pearson’s r = 0.42, indicating low spatial correlation. c, Spatial interaction between phosphatase and caspase-3/7  
in Dox-pretreated SJSA-1 cells. Similar results were observed in 12 independent experiments. d, Intensity plot of Phos-CN(P) along the dashed arrows in c. e, Correlation scatterplot of caspase-3/7 and phosphatase activity in Dox-pretreated SJSA-1 cells. Pearson’s r = 0.59. f, Cell viability assay of SJSA-1 cells incubated with Dox in the presence and absence of PIC. The PIC was diluted by 4,000-fold and 8,000- fold, respectively, using culture medium (n = 3 independent experiments). Data given as mean ± s.d. Scale bars: a, 40 μm; c, 10 μm.

## MIP imaging visualizes caspase–phosphatase interactions

The MIP spectra of C≡N in Phos-CN(P) and Casp-CN(P) in cells appear as narrow bands at unique wavenumbers (Fig. 3b,k), enabling multispectral imaging of these two enzymatic products. Thus, we simultaneously determined the activity distribution of phosphatase and caspase-3/7 in apoptotic cancer cells by MIP imaging of Phos-CN(P) and Casp-CN(P), because the yield of enzymatic products aligns with the level and biodistribution of enzyme activities. As shown in Fig. 4a, MIP imaging at 1,553 cm−1 (amide II) and 1,745 cm−1 shows the location and morphology of proteins and lipid droplets, respectively, in the Dox-pretreated SJSA-1 cells. After incubating the apoptotic cells with Phos-CN(S) and Casp-CN(S), strong MIP signals from the C≡N of Phos-CN(P) and Casp-CN(P) with a fine texture are observed in cells (Fig. 4a), suggesting a high level of activity of phosphatase and caspase-3/7 in the cells.

The merge channel and colocalization analysis confirms a weak spatial correlation between the MIP signals from Phos-CN(P) and Casp-CN(P) (Pearson’s r = 0.42, Fig. 4b), confirming that MIP imaging of nitrile chameleons not only visualizes, but also spatially and spectrally distinguishes the activity distribution of different enzymes.

Interestingly, although the activity maps of phosphatase and caspase-3/7 are mostly independent, sporadic instances of coexistence were observed in the cells (Fig. 4c). The overlaps between the activity maps of phosphatase and caspase-3/7, although infrequent, suggest the coexistence and co-assembly of their enzymatic products in certain areas inside the cells. Given that the MIP signal of enzymatic products spatially corresponds to the biodistribution of enzyme activities, such overlapping indicates that the activity of caspase-3/7 and phosphatase are spatially close in some areas of the cells, suggesting potential phosphatase–caspase interactions in apoptosis. PTEN44 and the protein tyrosine phosphatase PEST (PTP-PEST)45 have been reported as potential substrates of caspase-3. Importantly, the caspase-3-catalyzed cleavage of PTP-PEST increases the catalytic activity of PTP-PEST45. Notably, in the activity map of phosphatase and caspase-3/7, areas with colocalization generally have a stronger MIP signal from Phos-CN(P) than the ambient regions, as shown by the intensity plots (Fig. 4d). This indicates a higher phosphatase activity in the sites that are coupled with caspase-3/7 activity. On statistical analysis, the activity level of phosphatase in the SJSA-1 cell population is positively associated with that of caspase-3/7 (Fig. 4e). This indicates potential caspase–phosphatase interactions during apoptosis, probably through enzymatic cleavage with some phosphatase as the substrates of caspase. Such interactions appear to influence the activity of phosphatases in cells. Nevertheless, it is important to note that the alterations in phosphatase activity during apoptosis may occur through many other biochemical processes in the apoptosis signaling pathway, rather than being solely attributed to the direct processing of phosphatases by caspase-3/7.

To further confirm the interaction between phosphatase and caspase-3/7 during apoptosis, we imaged the intracellular distribution of caspase-3 proteins (full-length and cleaved) and the activity map of phosphatase in Dox-pretreated cancer cells in the presence and absence of a caspase-3 inhibitor (Z-DEVD-FMK, 10 μM). In this experiment the caspase-3 protein in the cancer cells was visualized by immunofluorescence staining using a confocal fluorescence microscope. To locate the phosphatase activity alongside caspase-3 protein via confocal fluorescence microscopy, we incubated cancer cells with NBD-Phos-CN(S) and located phosphatase activity through NBD fluorescence. This approach, known as fluorescence ENS, has been widely used to identify the location of enzyme activity11,26,46. We found that cancer cells in the caspase inhibitor-treated group had significantly fewer spatial overlaps between the phosphatase activity map and the caspase-3 proteins than the cells in the inhibitor-free group (Supplementary Fig. 17). This supports our hypothesis that caspase-3 and some phosphatases interact in the colocalized regions through enzymatic cleavage, with some phosphatases acting as the substrate of caspase-3. Thus, the simultaneous mapping of phosphatase and caspase-3/7 activity probably localizes the caspase-mediated cleavage of phosphatase, probably PTP-PEST41, in the apoptotic SJSA-1 cells. In addition to SJSA-1, we observed a similar scenario in MIA PaCa-2 (Supplementary Fig. 18). Furthermore, a slight inhibition of phosphatase activity rescued cancer cells from Dox-induced cell death (Fig. 4f), strengthening the notion that phosphatase activity is crucial in apoptosis signaling47–50

## Multicolor MIP imaging of enzyme activities in Caenorhabditis elegans and tissues

We explored enzyme activity mapping in C. elegans and brain tissues via MIP imaging of the nitrile chameleons. After incubating C. elegans with Phos-CN(S), real-time MIP imaging at 1,745 and 2,174 cm−1 delineated the biodistribution of lipid droplets and Phos-CN(P), elucidating the phosphatase activity profile in C. elegans (Fig. 5a). Although C. elegans lack

ALP, the intense MIP signal from the C≡N of Phos-CN(P) at 2,174 cm−1 and a weaker one from Phos-CN(S) at 2,215 cm−1 confirm an efficient enzymatic conversion (Fig. 5a,b), suggesting a high activity of other phosphatase isoenzymes, such as PTP, in C. elegans51. In the controls, MIP contrast is almost non-observable in the C. elegans without nitrile chameleon treatment (Supplementary Fig. 19). PIC significantly reduces the phosphatase activity in C. elegans, as shown by the weaker MIP signal from Phos-CN(P) and Phos-CN(S) (Fig. 5c,d). To avoid cell death due to the cytotoxicity of PIC, the PIC concentration we used might not completely deplete phosphatase activity in cells and C. elegans, resulting in a remnant of some phosphatase activity. The average [P]/[S] of the PIC-treated C. elegans versus that of the inhibitor-free group suggests a 54% decrease in the catalytic efficiency (k $_ { \mathrm { { a f } } } / \mathsf { K } _ { \mathsf { M } } )$ of the phosphatase (Fig. 5e) in C. elegans via PIC treatment. Although the caspase (for example, CED 3) of C. elegans may differ from that in humans, DEVD works as the substrate52. We exposed C. elegans to ultraviolet (UV) radiation to induce apoptosis for caspase activation53. After incubating the UV-irradiated C. elegans with Casp-CN(S), real-time MIP imaging at 2,163 cm−1 visualized the activity profile of the caspase in C. elegans (Fig. 5f). The strong MIP signal from Casp-CN(P) and the lower signal from Casp-CN(S) at 2,223 cm−1 confirm a high caspase activity in the UV-treated C. elegans (Fig. 5f,g). Conversely, faint MIP signals from Casp-CN(P) and Casp-CN(S) were observed in the UV-free C. elegans (Supplementary Fig. 20), indicat ing the existence of a weak caspase activity background in C. elegans. Furthermore, we reconstructed the 3D activity profiles of phosphatase and caspase in the nematode (Fig. 5h,i and Supplementary Videos 2 and 3). As well as visualizing the enzyme activity individually, we concurrently mapped the activity of phosphatase and caspase in C. elegans by incubating the UV-irradiated C. elegans with nitrile chameleons followed by MIP imaging (Fig. 5j). The merge channel and colocalization analysis show a poor overlap between the MIP signals from Phos-CN(P) and Casp-CN(P) (Pearson’s r = 0.23, Fig. 5k), confirming the identification and differentiation of the activity profiles of diverse enzymes in C. elegans by MIP imaging of nitrile chameleons.

Furthermore, we concurrently mapped the activity of phosphatase and caspase-3/7 in sections of mouse brains. Caspase-3/7 in fresh mouse brains was activated through ex vivo incubation with Dox (1 μM, 24 h), simulating chemotherapy-induced neurotoxicity. After incubating the Dox-treated tissues with nitrile chameleons, MIP imaging produced clear activity maps of phosphatase and caspase-3/7 in the unfixed tissue sections of cerebral cortex (Fig. 5l,m). MIP images of the phosphatase activity map in the brain slices resemble the pattern of phosphatase histochemistry, showing the dense network of capillaries in the cortical mantle54. The merged channel and colocalization analysis showed a low spatial overlap between Phos-CN(P) and Casp-CN(P) (Pearson’s r = 0.34, Fig. 5m). This supports the capability to identify and differentiate the activity distribution of various enzymes in the cerebral cortex via MIP imaging of nitrile chameleons. In tissues that were not treated with nitrile chameleons and which served as controls, little MIP contrast of C≡N is seen (Supplementary Fig. 21).

## Discussion

Here, we report a broadly applicable approach to the imaging of functions of multiple enzymes in living biological systems. We envision that this will be useful for studying enzyme biology during normal cell function and in pathological contexts. In addition, we envision that the technique will be applied to the discovery of drugs targeting enzyme activity.

Our approach addresses the challenge of visualizing the activities of multiple types of enzymes simultaneously inside live cells. Prior fluorescence-based studies55–58 focused on the imaging of individual enzymes in separate fields of view, leading to insufficient understanding of the interactions between different types of enzymes in the same cell or organism. Here, the development of a laser-scan MIP microscope and the synthesis of nitrile probes outperforms traditional enzyme activity imaging approaches by mapping the activities of multiple enzymes in the same field of view inside a live cell. Our approach enables comparison of the catalytic efficiency of specific enzymes between different cell populations, surpassing conventional off–on probes3,59 for imaging enzyme activity. Moreover, our vibrational approach is free of photobleaching, therefore facilitating quantitative measurements over time. An intriguing finding is the visualization of caspase–phosphatase interaction during apoptosis inside cancer cells.

a  
![](images/b74c9bb00e5cf2cabe2d994afa4d423bc231647e670c040b707531fedc346754.jpg)

<details>
<summary>text_image</summary>

Lipids
1,745 cm⁻¹
Phos-CN(P)
2,174 cm⁻¹
Phos-CN(S)
2,215 cm⁻¹
Control
Zoom in
</details>

b  
![](images/f5b5fa47e461b9dd2045c0c920c28326bb47ea1bcb1ece0d1f35914f5f29c50e.jpg)

<details>
<summary>bar chart</summary>

| Sample | MIP intensity (a.u.) |
| ------ | -------------------- |
| 2,174 (P) | 20 |
| 2,215 (S) | 10 |
</details>

e  
![](images/f9335ff4afe5fcbd054acb8b94b5b4ba730c8070de24441e44de92f9031c9eb3.jpg)

<details>
<summary>bar chart</summary>

| Group     | [P]/[S] |
| --------- | ------- |
| PBS       | 2.0     |
| Inhibitor | 1.0     |
</details>

![](images/180c016d81e84b494828c8737495b8c2e469605cba73ef393bc95b034ec09949.jpg)

<details>
<summary>text_image</summary>

UV pretreated
Zoom in
Lipids
1,745 cm⁻¹
Casp-CN(P)
2,163 cm⁻¹
Phos-CN(P)
2,174 cm⁻¹
Merged
</details>

c  
![](images/b2da37dee93399ad58428d1c5e8a0d49f12207fbcf836562a9dd2d32db877a74.jpg)

<details>
<summary>text_image</summary>

Lipids
1,745 cm⁻¹
Phos-CN(P)
2,174 cm⁻¹
Phos-CN(S)
2,215 cm⁻¹
Inhibitor
Zoom in
</details>

d  
![](images/60360afa4153f7f05c0b9635fc34faae0fde5f364efde28d99ab09de34aa5154.jpg)

<details>
<summary>bar chart</summary>

| Condition | MIP intensity (a.u.) |
| --------- | -------------------- |
| 2,174 (P) | 2                    |
| 2,215 (S) | 2                    |
</details>

h  
![](images/ff2ceaddcb638d5308067c6965846189a72be69573052455aa1db9bf17b725bd.jpg)

<details>
<summary>text_image</summary>

2,174 cm⁻¹
225
0
</details>

k  
![](images/7f29dcac04fc134741e9a32df1d21f9ea2ba8d3cff6056b635158bbf1238f6a4.jpg)

<details>
<summary>heatmap</summary>

| Quadrant | Value     |
|----------|-----------|
| 1        | 2,174 cm⁻¹ |
| 2        | 2,163 cm⁻¹ |
| 3        | 2,174 cm⁻¹ |
| 4        | 2,174 cm⁻¹ |
</details>

f  
![](images/96c85ba6bb67f9d20c454f5b686abcfd4efaead2bf4df1068b652d18a1157518.jpg)

<details>
<summary>text_image</summary>

Lipids
1,745 cm⁻¹
UV treated
Casp-CN(P)
2,174 cm⁻¹
Casp-CN(S)
2,215 cm⁻¹
Zoom in
</details>

g  
![](images/adcc101bb25cb859b8b68bf03e5bd8e74f4c8f8094a0bf063292fbbbcfa61fc9.jpg)

<details>
<summary>bar chart</summary>

| Group | MIP intensity (a.u.) |
|-------|----------------------|
| 2,163 (P) | 17 |
| 2,225 (S) | 8 |
</details>

i  
![](images/dd1ad764dc3eb6cdf5ed439645aaef71e1593ddcfc83f14bc8bf19d6d2755e95.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological structure with color scale bar (0–225) and measurement annotation (2,163 cm⁻¹), enclosed in a dashed border (no readable text or symbols)
</details>

![](images/cca29499b6ae03f2f18f44f044facd4d9610f4f720649453fabefdc673b9474b.jpg)

<details>
<summary>text_image</summary>

Cerebral cortex
1. Dox
2. Probes
MIP imaging
</details>

m  
![](images/5274af6a7bec15b6b3b9278e90205132d6edb09fec160ecc79c1d6df84a217bf.jpg)

<details>
<summary>text_image</summary>

1,553 cm⁻¹
Amide II
</details>

![](images/aed201132968666bd066a6328b74b833b96e9067703e83006672622a180d34d2.jpg)

<details>
<summary>text_image</summary>

2,174 cm⁻¹
Phos-CN(P)
</details>

![](images/98691d088d0785bd43bae526ae34dd80edf8ed98c8e5a1c5fa31092fbfa10d4a.jpg)

<details>
<summary>text_image</summary>

2,163 cm⁻¹
Casp-CN(P)
</details>

![](images/7ef90d8867cbf22f9ac74ae7b57e8e3e9ee0f87784424cd9ea169265cee9f9ab.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing merged green and red cellular structures (no text or symbols)
</details>

Phosphatase Caspase Overlap  
Fig. 5 | Multicolor MIP imaging of nitrile chameleons generates activity maps of caspase and phosphatase inside C. elegans and brain tissues.  
a, MIP imaging of phosphatase profile in live C. elegans incubated with Phos CN(S). b, Quantification of the MIP signal intensity from Phos-CN(P) and Phos-CN(S) in inhibitor-free C. elegans $\displaystyle ( n = 6 C$ . elegans). Data given as mean ± s.d. c, MIP imaging of phosphatase activity profile in PIC-pretreated C. elegans incubated with Phos-CN(S). d, Quantification of the MIP signal intensity from Phos-CN-(P) and Phos-CN-(S) in PIC-pretreated C. elegans $\left( n = 6 C \right.$ . elegans). Data given as mean ± s.d. e, Statistical analysis of phosphatase [P]/[S] in inhibitorfree and PIC-pretreated C. elegans (n = 6 C. elegans). Data given as mean ± s.d. The paired t-test (two-tailed) was used without adjustments for multiple comparisons. \*\*P ≤ 0.01 (P = 0.0019). f, MIP imaging of caspase activity profile  
in UV-pretreated C. elegans incubated with Casp-CN(S). g, Quantification of the MIP signal intensity from Casp-CN(P) and Casp-CN(S) in UV-pretreated, inhibitor-free C. elegans (n = 6 C. elegans). Data given as mean ± s.d. h,i, 3D reconstruction of phosphatase activity (h) and caspase activity (i) in C. elegans. j, Simultaneous activity mapping of phosphatase and caspase in UV-pretreated C. elegans incubated with the nitrile chameleons. The experiment was repeated independently at least ten times with similar results. k, Colocalization analysis of the mapping in j. Pearson’ $; r = 0 . 2 3$ , indicating low spatial correlation. l,m, Simultaneous mapping of phosphatase and caspase activities in Dox pretreated (1 μM) mouse cerebral cortex sections after incubation with the nitrile chameleons (Pearson’ $\ ; r = 0 . 3 4 )$ . The experiment was repeated independently ten times with similar results. Scale bars: a,c,f,j, 20 μm; m, 100 μm.

Given that multiple enzymes may share the same substrate, the development of probes with higher enzyme specificity is crucial to understand the function of a particular enzyme in various biological processes and diseases. Developing a more precise mathematical model $\mathsf { f o r k } _ { \mathrm { c a t } } / \mathsf { K } _ { \mathrm { M } }$ quantification is another worthwhile future endeavor. With regard to hardware, here, we used quantum cascade lasers for laser-scanning MIP imaging. However, the development of mid-infrared lasers with a shorter pulse duration and higher pulse energy would enable high-speed widefield MIP imaging of enzymatic activities and other cellular processes.

Although we focus on caspase and phosphatase in this study, activity mapping of a broad category of enzyme species can be done by developing more spectrally resolvable enzymatic reaction reporters24,28,60 (Supplementary Scheme 3). Additionally, enzyme activity profiling in other tissues, such as a tumor, is worth exploration. Furthermore, the nitrile chameleon concept, namely the reaction-activatable spectral shift of C≡N, can be extended to detect numerous cellular activities, including pH, reactive oxygen species, membrane potential and post-translational modification.

## Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41592-023-02137-x.

## References

1. Baruch, A., Jefery, D. A. & Bogyo, M. Enzyme activity: it’s all about image. Trends Cell Biol. 14, 29–35 (2004).  
2. Patel, T., Gores, G. J. & Kaufmann, S. H. The role of proteases during apoptosis. FASEB J. 10, 587–597 (1996).  
3. Zhang, J. et al. Fluorogenic probes for disease-relevant enzymes. Chem. Soc. Rev. 48, 683–722 (2019).  
4. Chyan, W. & Raines, R. T. Enzyme-activated fluorogenic probes for live-cell and in vivo imaging. ACS Chem. Biol. 13, 1810–1823 (2018).  
5. Xing, B., Khanamiryan, A. & Rao, J. Cell-permeable near-infrared fluorogenic substrates for imaging β-lactamase activity. J. Am. Chem. Soc. 127, 4158–4159 (2005).  
6. Grimm, J. B., Heckman, L. M. & Lavis, L. D. The chemistry of small-molecule fluorogenic probes. Prog. Mol. Biol. Transl. Sci. 113, 1–34 (2013).  
7. Kwan, D. H. et al. Self-immobilizing fluorogenic imaging agents of enzyme activity. Angew. Chem. Int. Ed. Engl. 50, 300–303 (2011).  
8. Johnson, D. S., Weerapana, E. & Cravatt, B. F. Strategies for discovering and derisking covalent, irreversible enzyme inhibitors. Future Med. Chem. 2, 949–964 (2010).  
9. Noe, M. C. & Gilbert, A. M. Targeted covalent enzyme inhibitors. Annu. Rep. Med. Chem. 47, 413–439 (2012).  
10. He, H. et al. Enzymatic noncovalent synthesis. Chem. Rev. 120, 9994–10078 (2020).  
11. Zhou, J. et al. Enzyme-instructed self-assembly for spatiotemporal profiling of the activities of alkaline phosphatases on live cells. Chem 1, 246–263 (2016).  
12. Liu, H. W. et al. In situ localization of enzyme activity in live cells by a molecular probe releasing a precipitating fluorochrome. Angew. Chem. Int. Ed. Engl. 56, 11788–11792 (2017).  
13. Gao, Y. et al. Imaging self-assembly dependent spatial distribution of small molecules in a cellular environment. Langmuir 29, 15191–15200 (2013).  
14. Zanetti-Domingues, L. C., Tynan, C. J., Rolfe, D. J., Clarke, D. T. & Martin-Fernandez, M. Hydrophobic fluorescent probes introduce artifacts into single molecule tracking experiments due to non-specific binding. PLoS One 8, e74200 (2013).  
15. Bao, K. et al. Charge and hydrophobicity efects of NIR fluorophores on bone-specific imaging. Theranostics 5, 609–617 (2015).  
16. Kim, B. J. & Xu, B. Enzyme-instructed self-assembly for cancer therapy and imaging. Bioconjug. Chem. 31, 492–500 (2020).  
17. Razgulin, A., Ma, N. & Rao, J. Strategies for in vivo imaging of enzyme activity: an overview and recent advances. Chem. Soc. Rev. 40, 4186–4216 (2011).  
18. Hamilton, B. R. et al. Mapping enzyme activity on tissue by functional mass spectrometry imaging. Angew. Chem. Int. Ed. Engl. 59, 3855–3858 (2020).  
19. Xia, Q., Yin, J., Guo, Z. & Cheng, J.-X. Mid-infrared phototherma microscopy: principle, instrumentation, and applications. J. Phys. Chem. B 126, 8597–8613 (2022).  
20. Bai, Y., Yin, J. & Cheng, J.-X. Bond-selective imaging by optically sensing the mid-infrared photothermal efect. Sci. Adv. 7, eabg1559 (2021).  
21. Zhang, D. et al. Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2, e1600521 (2016).  
22. Yin, J. et al. Video-rate mid-infrared photothermal imaging by single-pulse photothermal detection per pixel. Sci. Adv. 9, eadg8814 (2023).  
23. Tai, F. et al. Detecting nitrile-containing small molecules by infrared photothermal microscopy. Analyst 146, 2307–2312 (2021).  
24. Wei, L. et al. Super-multiplex vibrational imaging. Nature 544, 465–470 (2017).  
25. Yin, J. et al. Nanosecond-resolution photothermal dynamic imaging via MHZ digitization and match filtering. Nat. Commun. 12, 7097 (2021).  
26. Gao, Y., Shi, J., Yuan, D. & Xu, B. Imaging enzyme-triggered self-assembly of small molecules inside live cells. Nat. Commun. 3, 1033 (2012).  
27. Yi, M. et al. Enzyme responsive rigid-rod aromatics target ‘undruggable’ phosphatases to kill cancer cells in a mimetic bone microenvironment. J. Am. Chem. Soc. 144, 13055–13059 (2022).  
28. Wei, L. et al. Live-cell imaging of alkyne-tagged small biomolecules by stimulated Raman scattering. Nat. Methods 11, 410–412 (2014).  
29. Wang, R. et al. Aggregation enhanced responsiveness of rationally designed probes to hydrogen sulfide for targeted cancer imaging. J. Am. Chem. Soc. 142, 15084–15090 (2020).  
30. Hanczyc, P. & Fita, P. Laser emission of thioflavin T uncovers protein aggregation in amyloid nucleation phase. ACS Photonics 8, 2598–2609 (2021).  
31. Zaguri, D. et al. Kinetic and thermodynamic driving factors in the assembly of phenylalanine-based modules. ACS Nano 15, 18305–18311 (2021).  
32. Fried, S. D. & Boxer, S. G. Measuring electric fields and noncovalent interactions using the vibrational Stark efect. Acc. Chem. Res. 48, 998–1006 (2015).  
33. Feng, Z. et al. Artificial intracellular filaments. Cell Rep. Phys. Sci. 1, 100085 (2020).  
34. Qiu, C. et al. Advanced strategies for overcoming endosomal/ lysosomal barrier in nanodrug delivery. Research 6, 0148 (2023).  
35. He, H., Wang, H., Zhou, N., Yang, D. & Xu, B. Branched peptides fo enzymatic supramolecular hydrogelation. Chem. Commun. 54, 86–89 (2018).  
36. Guo, J. et al. The ratio of hydrogelator to precursor controls the enzymatic hydrogelation of a branched peptide. Soft Matter 16, 10101–10105 (2020).  
37. He, H. et al. Dynamic continuum of nanoscale peptide assemblies facilitates endocytosis and endosomal escape. Nano Lett. 21, 4078–4085 (2021).  
38. Sztiller‐Sikorska, M., Jakubowska, J., Wozniak, M., Stasiak, M. & Czyz, M. A non apoptotic function of caspase-3 in pharmacologically-induced diferentiation of K562 cells. Br. J. Pharmacol. 157, 1451–1462 (2009).  
39. Wilhelm, S., Wagner, H. & Häcker, G. Activation of caspase-3-like enzymes in non-apoptotic T cells. Eur. J. Immunol. 28, 891–900 (1998).  
40. Carlile, G. W., Smith, D. H. & Wiedmann, M. Caspase-3 has a nonapoptotic function in erythroid maturation. Blood 103, 4310–4316 (2004).  
41. Zhou, J., Du, X., Li, J., Yamagata, N. & Xu, B. Taurine boosts cellular uptake of small D-peptides for enzyme-instructed intracellular molecular self-assembly. J. Am. Chem. Soc. 137, 10040–10043 (2015).  
42. Andrews, L. D., Zalatan, J. G. & Herschlag, D. Probing the origins of catalytic discrimination between phosphate and sulfate monoester hydrolysis: comparative analysis of alkaline phosphatase and protein tyrosine phosphatases. Biochemistry 53, 6811–6819 (2014).  
43. Li, X. et al. Introducing D-amino acid or simple glycoside into small peptides to enable supramolecular hydrogelators to resist proteolysis. Langmuir 28, 13512–13517 (2012).  
44. Torres, J. et al. Phosphorylation-regulated cleavage of the tumor suppressor PTEN by caspase-3: implications for the control of protein stability and PTEN–protein interactions. J. Biol. Chem. 278, 30652–30660 (2003).  
45. Hallé, M. et al. Caspase-3 regulates catalytic activity and scafolding functions of the protein tyrosine phosphatase PEST, a novel modulator of the apoptotic response. Mol. Cell. Biol. 27, 1172–1190 (2007).  
46. Cai, Y. et al. Environment-sensitive fluorescent supramolecular nanofibers for imaging applications. Anal. Chem. 86, 2193–2199 (2014).  
47. Yang, C., Chang, J., Gorospe, M. & Passaniti, A. Protein tyrosine phosphatase regulation of endothelial cell apoptosis and diferentiation. Cell Growth Difer. 7, 161–172 (1996).  
48. Halle, M., Tremblay, M. L. & Meng, T. C. Protein tyrosine phosphatases: emerging regulators of apoptosis. Cell Cycle 6, 2773–2781 (2007).  
49. Sangwan, V. et al. Protein-tyrosine phosphatase 1B deficiency protects against Fas-induced hepatic failure. J. Biol. Chem. 281, 221–228 (2006).  
50. Van Hoof, C. & Goris, J. Phosphatases in apoptosis: to be or not to be, PP2A is in the heart of the question. Biochim. Biophys. Acta 1640, 97–104 (2003).  
51. Chen, M. J., Dixon, J. E. & Manning, G. Genomics and evolution of protein phosphatases. Sci. Signal. 10, eaag1796 (2017).  
52. Brantley, S. J. et al. Discovery of small molecule inhibitors for the C. elegans caspase CED-3 by high-throughput screening. Biochem. Biophys. Res. Commun. 491, 773–779 (2017).  
53. Stergiou, L., Doukoumetzidis, K., Sendoel, A. & Hengartner, M. The nucleotide excision repair pathway is required for UV-C-induced apoptosis in Caenorhabditis elegans. Cell Death Difer. 14, 1129–1138 (2007).  
54. Fonta, C., Négyessy, L., Renaud, L. & Barone, P. Areal and subcellular localization of the ubiquitous alkaline phosphatase in the primate cerebral cortex: evidence for a role in neurotransmission. Cereb. Cortex 14, 595–609 (2004).  
55. Bardet, P.-L. et al. A fluorescent reporter of caspase activity for live imaging. Proc. Natl Acad. Sci. USA 105, 13901–13905 (2008).  
56. Ye, D. et al. Bioorthogonal cyclization-mediated in situ self-assembly of small-molecule probes for imaging caspase activity in vivo. Nat. Chem. 6, 519–526 (2014).  
57. Van de Bittner, G. C., Bertozzi, C. R. & Chang, C. J. Strategy fo dual-analyte luciferin imaging: in vivo bioluminescence detection of hydrogen peroxide and caspase activity in a murine model of acute inflammation. J. Am. Chem. Soc. 135, 1783–1795 (2013).  
58. Ntziachristos, V., Tung, C.-H., Bremer, C. & Weissleder, R. Fluorescence molecular tomography resolves protease activity in vivo. Nat. Med. 8, 757–760 (2002).  
59. Fujioka, H. et al. Multicolor activatable Raman probes for simultaneous detection of plural enzyme activities. J. Am. Chem. Soc. 142, 20701–20707 (2020).  
60. Shi, L. et al. Mid-infrared metabolic imaging with vibrationa probes. Nat. Methods 17, 844–851 (2020).

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature America, Inc. 2024

## Methods

## Materials

RPMI 1640 culture medium (Thermofisher Scientific) with the addition of 10% (vol/vol) FBS and 1% (vol/vol) penicillin–streptomycin was used for SJSA-1 (ATCC, CRL-2098) cell culturing. DMEM culture medium (Thermofisher Scientific) with the addition of 10% (vol/vol) FBS and 1% (vol/vol) penicillin–streptomycin was used for MIA PaCa-2 (ATCC, CRM-CRL-1420) cell culturing. Nematode Growth Medium (NGM) for preparing the C. elegans suspension was purchased from Fisher Scientific. Phosphatase Inhibitor Cocktail II (PIC) was purchased from Sigma Aldrich. The caspase-3/7 inhibitor Z-DEVD-FMK was purchased from Sigma Aldrich. All amino acid derivatives involved in the synthesis were purchased from Fisher Scientific. N,Nʹ-Diisopropylethylamine (DIEA) and O-(1H-benzotriazol-1-yl)-N,N,Nʹ,Nʹ-tetramethyluronium hexafluorophosphate (HBTU) were purchased from Fisher Scientific. Human recombinant active caspase-3 was purchased from Abcam (ab52101), and ALP was purchased from Sigma Aldrich (10713023001). Caspase-3 (cleaved and full-length) antibody was purchased from Cell Signaling (catalog number 9662). All reagents and solvents were used as received without further purification unless otherwise stated.

## Laser-scan MIP microscope

The laser-scan MIP microscope is built on an inverted microscope frame (IX73, Olympus). The visible-light probe is provided by a continuous-wave 532 nm laser (Samba, HUBNER photonics). The mid-infrared pump is provided by a pulsed quantum cascade laser (MIRcat 2400, Daylight Solutions) tunable from 900 cm−1 to 2,300 cm−1. The visible beam is scanned using a galvanometer mirror with a 3 mm aperture (Saturn 1B, ScannerMax) and focused with a water immersion objective lens (1.2 numerical aperture (NA), ×60, Olympus). The infrared beam is synchronously scanned with another pair of galvanometer mirrors (GVS001, Thorlabs) and focused on the same spot with a reflective objective (0.5 NA, ×40, Thorlabs). For infrared beam scanning, reflective conjugation with two concave mirrors is used to remove the chromatic aberration. Probe photonics are collected in both the forward and backward directions, and the intensity is sensed using a silicon photodiode (DET100A, Thorlabs) connected to a low-noise amplifier (SA230, NF Corporation). The amplifier signal is then sent to a lock-in amplifier (HF2LI, Zurich) for MIP signal demodulation. The microscope is controlled using LabView 2020 software.

## Synthesis of nitrile probes

The synthesis of the self-assembly moiety was based on solid-phase peptide synthesis. All probes were purified using a water Agilent 1100 HPLC system, equipped with an Xterra C18 RP column. Details of the probe synthesis are given in Supplementary Information.

## Transmission electron microscopy

The transmission electron microscopy (TEM) images were taken on a Morgagni 268 transmission electron microscope using negative staining. Samples were dropped onto copper grids and dried by vacuum. Uranyl acetate (1 wt%, pH 4.5) was used to stain the samples three times followed by washing with distilled water. The images were taken by trained laboratory members.

## Limit of detection

The limit of detection used in this study is defined as the concentration at which the MIP signal from the molecule is equal to threefold the standard deviation of the background noise. A drop of solution of Casp-CN(P) or of Phos-CN(P) dissolved in DMSO at different concentrations was put under the MIP microscope, sandwiched between a piece of silicate cover glass and CaF crystal substrate. We focused on the center of the drop. We obtained the MIP spectra of Casp-CN(P) and Phos-CN(P) dissolved in DMSO at different concentrations in the cell-silence window until the MIP signal intensity at the peaks from the molecules was equal to threefold the standard deviation of the background noise. The lock-in integration time used for measurement is set to 50 ms.

## In vitro time-course monitoring of product formation

The in vitro time-course formation of enzymatic products from standard substrates was done following the manufacturer’s protocol. In brief, colorimetric substrates Ac-DEVD-pNA (100 μM) and pNPP (200 μM) were mixed with active caspase-3 (25 U ml−1) and ALP (0.5 U ml−1), respectively, at room temperature in PBS buffer. The UV absorbance at 405 nm was monitored over time using a UV-Vis (UV–visible light) spectrometer. Standard curves of enzymatic products were constructed to determine the product concentrations according to UV absorbance (Supplementary Fig. 4).

The in vitro time-course formation of enzymatic products from nitrile chameleons was carried out in a similar way. In brief, Casp-CN(S) (100 μM) and Phos-CN(S) (200 μM) were mixed with active caspase-3 (25 U ml−1) and ALP (0.5 U ml−1), respectively, at room temperature in PBS buffer. The UV absorbance of Casp-CN(S) (100 μM) mixed with caspase-3 was monitored at 325 nm over time with a UV-Vis spectrometer. The UV absorbance of Phos-CN(S) (200 μM) mixed with ALP was monitored at 340 nm over time using a UV-Vis spectrometer. Standard curves of enzymatic products were constructed to determine the product concentrations according to UV absorbance (Supplementary Fig. 4).

For the experiments to determine off-targeting effects, probes were mixed with CES-1 (1 mg ml−1), MMP-2 (10 U ml−1), proteinase K (0.1 mg ml−1), ALP (0.5 U ml−1) and caspase-3 (25 U mlml−1), respectively, in PBS at room temperature. The UV absorbance of the mixtures was monitored over time using a UV-Vis spectrometer.

## Sample preparation

For MIP imaging of live cells, SJSA-1 and MIA PaCa-2 cells were first seeded on CaF crystal substrates with a density of 1 × 105  ml−1 with 2 ml culture medium overnight at 37 °C and 5% ${ \mathrm { C O } } _ { 2 } .$ After cell attachment, the cells underwent pretreatment with, for example, PBS (control), Dox (2 μM, 24 h) or PIC (0.25 μl in 1 ml medium, 24 h). After treatment, cells were incubated with Phos-CN(S) (50 μM, 1 h) for phosphatase activity mapping, or Casp-CN(S) (50 μM, 1 h) for caspase activity mapping. Cells were then washed with PBS three times, sandwiched under a piece of silicate cover glass and imaged using the MIP microscope. For concurrent mapping of the activity of two enzymes, solutions of Phos-CN(S) (100 μM) and Phos-CN(S) (100 μM) were mixed at a 1:1 ratio. Cells (2 μM Dox treatment) were incubated with the mixture of probes (1 h), washed with PBS three times, sandwiched under a piece of silicate cover glass and then imaged using the MIP microscope (infrared frequency, 1 MHz; infrared power, 5–18 mW; probe beam, 20 mW; infrared pulse width, 50 ns; pixel dwell time, 4 μs).

For the optimization of laser pulse width, SJSA-1 cells were first seeded on CaF crystal substrates with a density of 1 × 105  ml−1 with 2 ml culture medium overnight at 37 °C and 5% $\mathrm { C O } _ { 2 } .$ After cell attachment, cells were fixed with 4% formaldehyde to avoid shrinkage caused by heat damage from use of the long laser pulse width.

For MIP imaging of live C. elegans, C. elegans (daf-2 (e1370) mutant strain, Caenorhabditis Genetics Center) were grown at 20 °C on NGM agar seeded with Escherichia coli OP50 by PBS washing. The C. elegans and E. coli suspension was centrifuged at 400 ×g for 30 s to separate C. elegans from E. coli. The C. elegans were resuspended in NGM followed by treatment according to the conditions of interest, for example, PBS (control), UV exposure (254 nm, until the movement of most C. elegans slows down) using a UV Stratalinker 2400 and PIC II treatment (1 μl PIC in 1 ml). After treatment, the nitrile chameleons (50 μM) were mixed with C. elegans in NGM and incubated for 1 h. The C. elegans were then washed by centrifugation at 400 ×g in PBS three times and sandwiched between a CaF crystal substrate and a piece of silicate cover glass for MIP imaging.

For the 3D reconstruction of the enzyme activity map in C. elegans, wild-type C. elegans were grown at $2 0 ^ { \circ } \mathrm { C }$ on NGM agar seeded with Escherichia coli OP50 by PBS washing. The C. elegans and E. coli suspension was centrifuged at 400 ×g for 30 s to separate C. elegans from E. coli. The C. elegans were resuspended in NGM followed by treatment according to the conditions of interest. The C. elegans were then fixed by 4% formaldehyde to prevent movement during the 3D reconstruction.

For MIP imaging of the cerebral cortex, two nude mice (Jackson lab, catalog number JAX:00555, female, 4 weeks of age) were anesthe tized by isoflurane. For all animal experiments, mice were housed at 21–23 °C in 35% humidity with a 12–12 dark–light cycle. The mice were checked with a tail pinch and were quickly decapitated. The scalps and skulls were opened with scissors and the brains were carefully removed. The brains were placed in PBS at room temperature and washed with PBS. The brain tissues were then cultured in 49 ml Hibernate-E Medium, 0.25 ml Gentamicin, 1 ml B-27 Plus Supplement and 50 μl Amphotericin B at 37 °C. Dox was then added to the medium to a final concentration of 1 μM. The brains were further incubated for 24 h. The brains were then transferred to new culture medium containing Casp-CN(S) and Phos-CN(S) (50 μM) for 4 h at $3 7 ^ { \circ } \mathrm { C }$ . After treatment, the tissue was sliced in coronal sections with a thickness of 100 µm using an Oscillating Tissue Slicer (OST-4500, Electron Microscopy Sciences). Brain slices were gently transferred by a brush and sandwiched between a CaF substrate and a cover glass for MIP imaging. The protocol of animal experiments was approved by BU IACUC (PROTO201800534).

## Immunofluorescence imaging

All samples were fixed using 4% formalin in PBS, pH 7.4, for 10 min at room temperature. The samples were then washed with PBS three times, for 5 min each, to remove formalin residue. The samples were permeabilized for 10 min with PBS containing 0.25% Triton X-100, and then washed again in PBS three times for 5 min each. Samples were incubated with 1% BSA, 22.52 mg ml−1 glycine in PBST (PBS + 0.1% Tween 20) for 30 min to block unspecific binding of the antibodies. Then, samples were incubated in 1,000× diluted antibody (Anti-Alkaline Phosphatase antibody, Abcam, ab354; Anti-Cleaved Caspase-3 antibody, Abcam, ab2302; Anti-Caspase-3 antibody, full-length and cleaved, Cell Signaling, catalog number 9662) in 1% BSA in PBST in a humidified chamber overnight at 4 °C. After this, the cells were washed three times in PBS for 5 min each. The cells were then incubated with 500× diluted secondary antibody (Goat anti-rabbit IgG labeled with Alexa-532, Thermofisher Scientific, catalog number A-11009) in 1% BSA for 1 h at room temperature in the dark. After decanting the secondary antibody solution, the cells were washed again three times with PBS for 5 min each in the dark and were then ready for imaging.

## Acquisition of pinpointed MIP spectra

To determine the area in cells in which to pinpoint the MIP spectrum, MIP images of the cells were initially captured at the wavenumbers of C≡N of enzymatic products derived from their corresponding DMSO solutions (2,205 and 2,221 cm−1, respectively). The cell features could be seen in these images. The features were selected randomly, and the MIP spectra (2,000–2,300 cm−1) from these features were monitored to identify sharp peaks, indicating the detection of nitrile groups. The MIP spectra of the selected pixels were obtained by sweeping the quantum cascade laser from 2,000 to 2,300 cm−1 at a speed of 50 cm−1 per second, and the data points were recorded by a lock-in amplifier with a time constant of 20 ms. The spectra undergo smoothing with the Savitzky–Golay method using Origin. It was found that, for the same molecules, the wavenumbers of C≡N in the cells shift compared with those in DMSO (Fig. 2d), probably due to the Stark effect32. Thus, the cell morphologies shown at 2,205 and 2,221 cm−1 correspond to the infrared absorption of water in the cell-silence window. The infrared spectrum of the water absorbance background from 2,000 to 2,300 cm−1 was therefore collected by pinpointing a blank area in the field of view, and this was then subtracted from the pinpointed spectra of C≡N to give the final pinpointed MIP spectra of C≡N in cells. The data were plotted using GraphPad Prism 8 or Microsoft 365 Excel.

## MIP imaging in cell-silent window and water background subtraction

All samples were imaged under a counter-propagating MIP microscope under the following condition: infrared frequency, 1 MHz; infrared power, 5–18 mW (depending on wavenumber); probe beam, 20 mW; infrared pulse width, 50 ns; pixel dwell time, 4 μs. A weak and broad-band MIP signal from the water absorption in the cell-silence window (2,000–2,300 cm−1) was observed. To remove the water background, two consecutive frames at the peak of the C≡N of products and 2,080 cm−1 (water infrared absorbance) or at the peak of the C≡N of substrates and $2 { , } 0 4 0 \mathsf { c m } ^ { - 1 }$ (water infrared absorbance) were collected, respectively. The fast imaging speed (4 μs pixel−1 or 1 s frame−1 for 500 pixels × 500 pixels) of the MIP microscope enables minimal sample moves between two consecutive frames, as well as little subtraction artifact. This is supported by the observation that the cells in the blank control groups exhibit no signal after subtraction (Supplementary Fig. 8a). Thus, all MIP images collected at the peak of the C≡N of products underwent subtraction of the MIP images collected at 2,080 cm−1 to remove the water background and to generate the final images. Moreover, all MIP images collected at the peak of the C≡N of substrates underwent subtraction of the MIP images collected at 2,040 cm−1 to remove the water background and to generate the final images. The wavenumbers 2,080 cm−1 and 2,040 cm−1 were selected because the MIP signal intensity in the blank area of a field of view at these wavenumbers is equal to the MIP signal intensity at the wavenumbers of the C≡N of products and substrates in the same blank region, respectively.

## Determination of probe solubility

To assess probe solubility, Casp-CN(S) and Phos-CN(S) were mixed in PBS at a final concentration of 1 mM. After being vortexed for 10 min, the mixtures were filtered through a 0.22 μm syringe filter. By measuring the UV absorbance of the filtrate and subsequent comparison with a standard curve, the concentrations of both probes in filtrates were determined to be 1 mM, indicating that the maximum solubility of the probes exceeds 1 mM in PBS. This solubility is significantly higher than the working concentration $( 5 0 \mu \mathrm { M } )$ . These results confirm that although both Casp-CN(S) and Phos-CN(S) formed small nanoparticles in PBS at 50 μM, these nanoparticles, like micelles formed by surfactants, can be uniformly dispersed in an aqueous solution.

## Image processing

All images were opened and processed using ImageJ. Colocalization analysis was done with ImageJ using the colocalization threshold and the coloc 2 plugin. 3D reconstruction was done with ImageJ using the 3D viewer plugin. The whole cell was selected for quantification of MIP signal in a cell and for colocalization analysis. The data were plotted using GraphPad Prism 8 or Microsoft 365 Excel. All MIP images of nitrile chameleons were 32 bit. All fluorescence images are 8 bit. MIP images of nitrile chameleons were converted to 8 bit for comparison with fluorescence images.

## Reporting summary

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

## Data availability

All data related to the work are available in the article and supplementary information in this paper. The original data for the figures are available at https://doi.org/10.5281/zenodo.10085096.

## Acknowledgements

This work was supported by R35GM136223 and R33CA261726 to J.-X.C., R01CA142746 to B.X. and grant 2023-321163 from the Chan Zuckerberg Initiative Donor-Advised Fund at the Silicon Valley Community Foundation. Source data are provided with this paper.

## Author contributions

J.-X.C. and H.H. conceived the study. H.H. synthesized the probes, performed the experiments and drafted the paper. J.Y. developed the laser-scanning MIP microscope. J.Y. and M.L. helped with the MIP imaging. M.Y. and X.T. helped in the probe synthesis. M.Z. helped in the culturing and MIP imaging of C.elegans. C.V.P.D., Y.L. and Z.D. carried out the extraction of mice brains, tissue sectioning and tissue imaging. B.X. provided material support on synthesis and made intellectual contributions to experiment design.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41592-023-02137-x.

Correspondence and requests for materials should be addressed to Ji-Xin Cheng.

Peer review information Nature Methods thanks Lingyan Shi, Stephen Weber and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available. Primary Handling Editor: Rita Strack, in collaboration with the Nature Methods team.

Reprints and permissions information is available at www.nature.com/reprints.

## Reporting Summary

Nature Portfolio wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Portfolio policies, see our Editorial Policies and the Editorial Policy Checklist.

## Statistics

For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.

n/a Confirmed

The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement  
A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly  
X

A description of all covariates tested

A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons

A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) X AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)

For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted

For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings

For hierarchical and complex designs, identification of the appropriate level for tests and ful reporting of outcomes

Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated

Our web collection on statistics for biologists contains articles on many of the points above.

## Software and code

Policy information about availability of computer code

Data collection

LabView 2020

Data analysis

ImageJ, Microsoft 365 Excel, GraphPad Prism 8

For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Portfolio guidelines for submitting code & software for further information.

## Data

Policy information about availability of data

All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:

- Accession codes, unique identifiers, or web links for publicly available datasets  
- A description of any restrictions on data availability  
- For clinical datasets or third party data, please ensure that the statement adheres to our policy

All data related to the work is available in the article and supplementary information within this paper. The Original data of figures is available in doi:10.5281/ zenodo.10161552. Other data is available upon reasonable request to the corresponding author.

Policy information about studies involving human research participants and Sex and Gender in Research.

Reporting on sex and gender

Population characteristics N/A

Recruitment N/A

Ethics oversight N/A

Note that full information on the approval of the study protocol must also be provided in the manuscript

## Field-specific reporting

Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.

Life sciences

Behavioural & social sciences

Ecological, evolutionary & environmental sciences

For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf

## Life sciences study design

All studies must disclose on these points even when the disclosure is negative.

<table><tr><td>Sample size</td><td>Sample sizes were predetermined based on the basis of prior experience, published standards in the field and standard deviation. The sample size for individual experiment was determined based on sample availability and the balance between experiment time and data standard deviation. Sample sizes are reported for each experiment in the manuscript.</td></tr><tr><td>Data exclusions</td><td>No data exclusion</td></tr><tr><td>Replication</td><td>All samples were chosen randomly. All attempts to replication were successful. Sample size for each experiment are indicated in the figure legends.</td></tr><tr><td>Randomization</td><td>For all in vitro and in vivo samples, the samples were chosen randomly before the treatment of the condition of interests. The samples that were treated by the same conditions were allocated into the same experiment or control group. The field of vied of imaging were randomized.</td></tr><tr><td>Blinding</td><td>The imaging of mouse brain was blinded during data collection and analysis. In vitro study were keep blinded as possible but blinding for imaging experiment is not applicable due to cell&#x27;s morphology feature. However, data collection was randomized to avoid potential operator bias. For TEM imaging, the researchers were kept blind during data collection and analysis.</td></tr></table>

## Reporting for specific materials, systems and methods

We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.

Materials & experimental systems

<table><tr><td>n/a</td><td>Involved in the study</td></tr><tr><td></td><td>Antibodies</td></tr><tr><td></td><td>Eukaryotic cell lines</td></tr><tr><td></td><td>Palaeontology and archaeology</td></tr><tr><td></td><td>Animals and other organisms</td></tr><tr><td></td><td>Clinical data</td></tr><tr><td></td><td>Dual use research of concern</td></tr></table>

Methods

<table><tr><td>n/a</td><td>Involved in the study</td></tr><tr><td>☒</td><td>☐ ChIP-seq</td></tr><tr><td>☒</td><td>☐ Flow cytometry</td></tr><tr><td>☒</td><td>☐ MRI-based neuroimaging</td></tr></table>

Antibodies

<table><tr><td>Antibodies used</td><td>Anti-Alkaline Phosphatase antibody (Abcam, ab354); Anti-Cleaved Caspase-3 antibody (Abcam, ab2302); Anti-Caspase-3 antibody (full length and cleaved, cell signaling #9662), Goat anti-rabbit IgG labeled with Alexa-532 (Thermofisher Scientific, Catalog # A-11009).</td></tr><tr><td>Validation</td><td>The validation can be found on manufacture&#x27;s website. Anti-Alkaline Phosphatase antibody (Abcam, ab354), validated in WB, IP and ELISA: https://www.abcam.com/products/primary-antibodies/alkaline-phosphatase-antibody-ab354.html Anti-Cleaved Caspase-3 antibody (Abcam, ab2302), validated in WB: https://www.abcam.com/products/primary-antibodies/cleaved-caspase-3-antibody-ab2302.html Anti-Caspase-3 antibody (full length and cleaved, cell signaling #9662), validated in WB, IP and IHC: https://www.cellsignal.com/products/primary-antibodies/caspase-3-antibody/9662 Goat anti-rabbit IgG labeled with Alexa-532 (Thermofisher Scientific, Catalog # A-11009), validated in ICC/IF: https://www.thermofisher.com/antibody/product/Goat-anti-Rabbit-IgG-H-L-Cross-Adsorbed-Secondary-Antibody-Polyclonal/A-11009</td></tr></table>

Eukaryotic cell lines  
Policy information about cell lines and Sex and Gender in Research

<table><tr><td>Cell line source(s)</td><td>SJSA-1 cell line and MIA PaCa-2 cell line were purchased from ATCC</td></tr><tr><td>Authentication</td><td>Authentication of Mia Paca2 was performed by ATCC through STR profiling. The SJSA-1 cell line was purchased from the manufacture (ATCC) and used immediately after receipt. Thus, SJSA-1 cell line was not authenticated.</td></tr><tr><td>Mycoplasma contamination</td><td>All cell lines were tested to be mycoplasma negative.</td></tr><tr><td>Commonly misidentified lines (See ICLAC register)</td><td>There is no commonly misidentified cell lines in this study.</td></tr></table>

## Animals and other research organisms

Policy information about studies involving animals; ARRiVE guidelines recommended for reporting animal research, and Sex and Gender in Research

<table><tr><td>Laboratory animals</td><td>Nude mice (Jackson Labs Cat#JAX:00555), 4 weeks; C. elegans (caenorhabditis genetics center, daf-2 (e1370)), used upon reception</td></tr><tr><td>Wild animals</td><td>There is no wild animals involved in this study.</td></tr><tr><td>Reporting on sex</td><td>Sex was not considered in this study</td></tr><tr><td>Field-collected samples</td><td>There is no field-collected samples involved in this study.</td></tr><tr><td>Ethics oversight</td><td>Animal studies were approved by the Institutional Animal Care and Use Committee (IACUC) at Boston University .</td></tr></table>

Note that full information on the approval of the study protocol must also be provided in the manuscript.