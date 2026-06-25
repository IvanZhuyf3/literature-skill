# Label-free spectroscopic detection of membrane potential using stimulated Raman scattering

Bin Liu,1 Hyeon Jeong Lee,2 Delong Zhang,3 Chien-Sheng Liao,4 Na Ji,5 Yuanqin Xia,1,a) and Ji-Xin Cheng3,4,a)

1 National Key Laboratory of Science and Technology on Tunable Laser, Harbin Institute of Technology, Harbin 150080, China

2 Interdisciplinary Life Science Program, Purdue University, West Lafayette, Indiana 47907, USA

3 Department of Chemistry, Purdue University, West Lafayette, Indiana 47907, USA

4 Weldon School of Biomedical Engineering, Purdue University, West Lafayette, Indiana 47907, USA

5 Janelia Research Campus, Howard Hughes Medical Institute, Ashburn, Virginia 20147, USA

(Received 23 December 2014; accepted 15 April 2015; published online 27 April 2015)

Hyperspectral stimulated Raman scattering microscopy is deployed to measure single-membrane vibrational spectrum as a function of membrane potential. Using erythrocyte ghost as a model, quantitative correlation between transmembrane potential and Raman spectral profile was found. Specifically, the ratio between the area under Raman band at -2930 cm1 and that at -2850 cm1 increased by -2.6 times when the potential across the erythrocyte ghost membrane varied from þ10 mV to 10 mV. Our results show the feasibility of employing stimulated Raman scattering microscopy to probe the membrane potential without labeling. VC 2015 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4919104]

The plasma membrane, which consists of a double layer of phospholipids with embedded proteins, is the outer boundary of a biological cell. The cell membrane functions as a physical barrier isolating the cytoplasm from the extracellular environment, thus protecting the cell from its surroundings. Since the cell membrane is selectively permeable, it regulates and organizes the cell by controlling the exchange of substances. In additional to these fundamental roles, the cell membrane also mediates the communication between different cells. Changes in the transmembrane potential can generate action potential and give cells the capability to convey messages and communicate with other partners. Therefore, methods of probing cell membrane properties are of extreme importance.

Fluorescence labeling is the most widely used method for cell membrane related study. Various florescent voltagesensitive indicators have been extensively used to sense the membrane potential.1 Immunofluorescence staining is a well-established method for the analysis of cell polarity.2 Cell membrane fluidity is frequently analyzed by monitoring the dynamics of fluorophores which tag either membrane proteins or lipids to mimic the behavior of cell membrane.3 For these fluorescence based approaches, perturbation of the membrane properties by chromophores is often a concern.

As a label-free analytical tool, Raman spectroscopy has been used to measure the responses of membranes to variations of temperature, pH, and transmembrane ion gradients.4,5 Because spontaneous Raman scattering is weak, extremely high laser power (400 mW at sample) was used in the previous study,5 which is close to the physical damage threshold. The weak signal also hinders the application of spontaneous Raman scattering as a dynamic imaging tool. To address this problem, coherent Raman scattering microscopy techniques6 were recently developed, which increased the acquisition speed by several orders of magnitude through coherent excitation of Raman bands in a spectral window of interest. With coherent anti-Stokes Raman scattering (CARS) microscopy,7 the orientation of lipid bilayers inside the erythrocyte ghost membrane was visualized by Potma and Xie.8 Compound Raman microscopy,9 which combines advantage of high-speed vibrational imaging offered by CARS and quantitative spectral analysis by spontaneous Raman scattering, offers an alternative way to study the membrane. Using a compound Raman microscope, Yue et al. demonstrated label-free analysis of apical polarity of live cell membranes in 3D culture. 10

In this work, we present the use of stimulated Raman scattering (SRS) microscopy 1 1 to detect the membrane potential in a label-free manner. SRS gives identical spectral profile as spontaneous Raman scattering and it provides several orders of magnitude stronger signal through stimulated scattering. By offering spectral information at each pixel, hyperspectral SRS microscopy has allowed for quantitative chemical imaging of cell,12,13 tissue,14,15 and Caenorhabditis elegans.16 Herein, we demonstrate the employment of hyperspectral SRS microscopy for probing the transmembrane voltage with erythrocyte ghost as a model system.

Our hyperspectral SRS imaging system (Fig. 1) was built based on a previously reported spectral focusing scheme,13,17 where the Raman shift is controlled by the temporal delay of two chirped femtosecond pulses. An ultrafast laser system with dual output operating at 80 MHz (InSight DeepSee, Spectra-Physics) provided the excitation sources. The tunable output with a pulse duration of 120 fs was tuned to 800 nm, serving as pump beam. The other output centered at 1040 nm with a pulse duration of 220 fs was used as Stokes beam, modulated by an acousto-optic modulator (AOM, 1205-C, Isomet) at 2.3 MHz. An optical delay line was installed in the pump light path and a motorized translation stage (T-LS28E, Zaber) was employed to scan the delay between two beams. After combination by a dichroic mirror, both beams were chirped by two 12.7 cm long SF57 glass rods. In order to match the linear chirp parameter of two beams, the inbuilt prism compressor inside the laser system was used to adjust the dispersion of the pump beam. After glass rods, pulse durations of the pump and Stokes beams were stretched to -1.3 and -0.8 ps, respectively, measured with an autocorrelator (PulseScope, APE). The pump and Stokes beams were sent into a homebuilt laser-scanning microscope described elsewhere.15,18 Briefly, a 60 water immersion objective lens $( \mathrm { N A } = 1 . 2 $ , UPlanApo/IR, Olympus) was utilized to focus the light into the sample, and an oil condenser (NA ¼ 1.4, U-AAC, Olympus) was used to collect the signal. The stimulated Raman loss signal was detected by a Si photodiode (S3994–01, Hamamatsu) and extracted with a digital lock-in amplifier (HF2LI, Zurich Instrument).

![](images/3afa2907842f88479ee9632118c0b6c1952d1807147e2bd7c4cf09f2a640e65b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["InSight DeepSee"] --> B["Pump"]
  B --> C["N/2 PBS"]
  C --> D["AOM"]
  D --> E["DM"]
  E --> F["SF57"]
  F --> G["Obj"]
  G --> H["Con"]
  H --> I["Lens"]
  I --> J["Filter"]
  J --> K["PD"]
  K --> L["Ref LIA"]
  L --> M["Out"]
  M --> N["Stokes"]
  N --> O["N/2 PBS"]
  O --> P["AOM"]
  P --> Q["DF"]
  Q --> R["Scan unit"]
```
</details>

FIG. 1. Schematic of the hyperspectral SRS microscope. k/2, half wave plate; PBS, polarizing beam splitter; AOM, acousto-optic modulator; DM, dichroic mirror; SF57, SF57 glass; Obj, objective; Con, condenser; PD, photodiode; LIA, lock-in amplifier.

We first calibrated the Raman shift with respect to the pump-Stokes temporal delay using the Raman peaks of known chemicals. Fig. 2(a) shows the spontaneous Raman spectra of dimethyl sulfoxide, methanol, acetic acid and cyclohexanone in the CH stretching region from 2800 to $3 0 5 0 \mathrm { c m } ^ { - 1 }$ , measured with a commercial spectrograph (Shamrock SR-303i-A, Andor Technology). Corresponding SRS spectra recorded by scanning the pump-Stokes pulse delay are shown in Fig. 2(b). The SRS intensity was normalized with the two-photon absorption signal of Rhodamine 6G which approximately reflects the cross-correlation between the pump and Stokes pulses. Using these distinguished Raman peaks shown in Fig. 2(a), the translation stage positions were then correlated to the Raman shifts by linear fitting, resulting in the calibration curve shown in $\mathrm { F i g . }$ . 2(c). The correlation is almost linear $( \mathsf { R } ^ { 2 } = 0 . 9 9 5 )$ , which indicates that the laser pulses were nearly linearly chirped. The spectral resolution of our system is -25 cm1 , estimated from the SRS spectra of dimethyl sulfoxide and methanol.

Using the hyperspectral SRS imaging system, we recorded Raman spectrum from single erythrocyte membrane which is an established model system for membrane biochemistry.4,5,19 Fig. 3(a) shows a representative stack of hyperspectral SRS images of an erythrocyte ghost. Preparation of erythrocyte ghosts can be found in detail in supplementary material. $\cdot ^ { 2 0 } \mathrm { ~ A ~ }$ total of 50 frames were recorded from $2 7 8 4 . 8 2 \mathrm { c m } ^ { - 1 }$ to $3 0 4 1 . 8 3 \mathrm { c m } ^ { - 1 }$ with a step increment of ${ \sim } 5 . 2 5 \mathrm { c m } ^ { - 1 }$ . Each frame was composed of $4 0 \times 4 0$ pixels with a pixel dwell time of $2 0 0 \mu \mathrm { s } .$ Acquisition of the entire stack took -28 s. A representative SRS spectrum from single natural membrane, obtained through averaging the hyperspectral data from the pixels indicated by the rectangular box in Fig. 3(a), is shown in Fig. 3(b). Lorentzian fitting was performed to decompose the spectrum into 7 bands according to previous studies.10,21 The spectrum analysis and fitting parameters can be found in

![](images/bf3ecd1fdf061b47520eda4a4efea2e37268848c0c8ced0a66f8c9c42d58109f.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | DMSO | MeOH | AcOH | CYC |
| --- | --- | --- | --- | --- |
| 2800 | 0.0 | 0.1 | 0.0 | 0.0 |
| 2850 | 0.0 | 1.0 | 0.0 | 0.2 |
| 2900 | 0.0 | 0.5 | 0.5 | 0.8 |
| 2950 | 1.0 | 0.8 | 1.0 | 1.0 |
| 3000 | 0.3 | 0.2 | 0.2 | 0.1 |
| 3050 | 0.1 | 0.1 | 0.1 | 0.0 |
| 3100 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3150 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3200 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3250 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3300 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3350 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3400 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3450 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3500 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3550 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3600 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3650 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3700 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3750 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3800 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3850 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3900 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3950 | 0.0 | 0.0 | 0.0 | 0.0 |
| 4000 | 0.0 | 0.0 | 0.0 | 0.0 |
| 4050 | 0.0 | 0.0 | 0.0 | 0.0 |
| 4100 | 0.0 | 0.0 | 0.0 | 0.0 |
| 4150 | 0.0 | 0.0 | 0.0 | 0.0 |
| 4200 | 0.0 | 0.0 | 0.0 | 0.0 |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... = ... | ... | ... | ... | ... |
</details>

![](images/22b476bbf233854c097cef1cb906d1ce0d3b795b863b80251a8b65f931396897.jpg)

<details>
<summary>line chart</summary>

| Delay (μm) | DMSO | MeOH | AcOH | CYC |
|------------|------|------|------|-----|
| 0          | 0.0  | 0.0  | 0.0  | 0.0 |
| 150        | 0.2  | 1.0  | 0.1  | 0.8 |
| 300        | 1.0  | 1.0  | 1.0  | 1.0 |
| 450        | 0.1  | 0.1  | 0.1  | 0.1 |
</details>

![](images/919d17c6af3f199e664872b7a9e01c29b5fef8756bc3a2d5c84c161194183c05.jpg)

<details>
<summary>line chart</summary>

| Delay (μm) | Raman shift (cm⁻¹) |
| ---------- | ------------------ |
| 90         | 2840               |
| 140        | 2870               |
| 190        | 2900               |
| 240        | 2920               |
| 290        | 2950               |
| 340        | 2970               |
| 390        | 3000               |
</details>

FIG. 2. Calibration of Raman shifts in the spectral focusing system. (a) Normalized spontaneous Raman spectra of dimethyl sulfoxide (DMSO), methanol (MeOH), acetic acid (AcOH), and cyclohexanone (CYC). (b) Corresponding SRS spectra measured by scanning pump-Stokes delay. (c) Correlation of the Raman shift with respect to the pump-Stokes delay.

![](images/95c81bbf533fea9c59e8f9badae82ff5910e96e4815713cc3ffeba4c761253fa.jpg)

<details>
<summary>heatmap</summary>

| Row | Column | Value |
| --- | --- | --- |
| 1 | 1 | 7 |
| 1 | 2 | 8 |
| 1 | 3 | 9 |
| 1 | 4 | 10 |
| 1 | 5 | 11 |
| 1 | 6 | 12 |
| 2 | 7 | 13 |
| 2 | 8 | 14 |
| 2 | 9 | 15 |
| 2 | 10 | 16 |
| 2 | 11 | 17 |
| 2 | 12 | 18 |
| 3 | 13 | 19 |
| 3 | 14 | 20 |
| 3 | 15 | 21 |
| 3 | 16 | 22 |
| 3 | 17 | 23 |
| 3 | 18 | 24 |
| 4 | 19 | 25 |
| 4 | 20 | 26 |
| 4 | 21 | 27 |
| 4 | 22 | 28 |
| 4 | 23 | 29 |
| 4 | 24 | 30 |
| 5 | 25 | 31 |
| 5 | 26 | 32 |
| 5 | 27 | 33 |
| 5 | 28 | 34 |
| 5 | 29 | 35 |
| 5 | 30 | 36 |
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
</details>

![](images/c5059b785afd7ea47deebbf93b2208b918e662e3894347934f64ca768e104535.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 2800               | 0.2              |
| 2850               | 1.5              |
| 2900               | 1.8              |
| 2950               | 1.7              |
| 3000               | 0.3              |
</details>

FIG. 3. Hyperspectral SRS images of an erythrocyte ghost. (a) A total of 50 SRS images were recorded from $2 7 8 4 . 8 2 \mathrm { c m } ^ { - 1 }$ to 3041 $. 8 3 \mathrm { c m } ^ { - 1 }$ with a step increment of ${ \sim } 5 . 2 5 \mathrm { c m } ^ { - 1 }$ . Acquisition of the entire stack took ${ \sim } 2 8 \mathrm { s } .$ Inset: intensity averaged image of selected 27 frames from 2837.27 to 2973.64 $\mathrm { c m } ^ { - 1 }$ . (b) SRS spectrum of the region of interest (ROI) indicated by purple rectangle in (a). The spectrum was fitted as a sum of 7 Lorentzian bands (olive), where the Raman bands around 2850 and $2 9 3 0 \mathrm { c m } ^ { - 1 }$ were highlighted with filling. The cumulative fitted curve is shown in red. Scale bar: 1.0 lm. Pixel dwell time: 200 ls. Image averaged 5 times.

supplementary material. $\cdot ^ { 2 0 }$ The Raman band around 2850 cm1 is largely contributed by the CH groups in lipid bilayers. The band at ${ \sim } 2 9 3 0 \mathrm { c m } ^ { - 1 }$ is largely contributed by the $\mathrm { C H } _ { 3 }$ groups in membrane proteins. As the pump and Stokes beams were parallel-polarized, the SRS signal intensity [inset of Fig. 3(a)] showed a clear dependence on the orientation of lipid bilayers with respect to laser polarization.

To prove the concept of probing transmembrane potential via SRS microscopy, we changed the potential across the erythrocyte ghost membrane from þ10 to 10 mV by changing the intravesicular and extravesicular ionic compositions (see supplementary material $\begin{array} { r l } { \mathrm { f o r } } & { { } \mathrm { d e t a i l s } ^ { \bar { 2 } 0 } ) } \end{array}$ . Representative SRS spectra of erythrocyte ghost membrane recorded at 3 different transmembrane potentials are shown in Fig. 4(a). For the purpose of comparison, all spectra were normalized by the intensity at $2 8 5 0 \mathrm { c m } ^ { - 1 } \left( I _ { 2 8 5 0 } \right)$ which is not sensitive to the changes of environment.4,5 The SRS spectral profiles of erythrocyte ghosts showed a clear dependence on the membrane potentials. Specifically, the SRS signal intensity at ${ \sim } 2 9 3 0 \mathrm { c m } ^ { - 1 }$ decreased when a positive membrane potential was imposed. Fig. 4(b) shows the calculated ratio between the areas under Raman bands at -2930 cm1 ${ \sim } 2 9 3 0 \mathrm { c m } ^ { - 1 }$ and at ${ \sim } 2 8 5 0 \ c m ^ { - 1 } \ ( A _ { 2 9 3 0 } / A _ { 2 8 5 0 } )$ for 3 membrane potentials presented in Fig. 4(a). The ratio $( A _ { 2 9 3 0 } / A _ { 2 8 5 0 } )$ increased dramatically from $2 . 9 1 \pm 0 . 2 7$ to $7 . 5 9 \pm 0$ .84 with the membrane potential changing from þ10 mV to 10 mV.

![](images/5dd15f09140d72bbd6e09f9fda6c835c9781df18371d9eef62d117b955f7e7b7.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | +10 mV (n = 6) | +1 mV (n = 8) | -10 mV (n = 6) |
| ------------------ | -------------- | ------------- | -------------- |
| 2800               | ~0.0           | ~0.0          | ~0.0           |
| 2850               | ~1.0           | ~1.2          | ~1.4           |
| 2900               | ~1.2           | ~1.4          | ~1.7           |
| 2950               | ~1.0           | ~1.3          | ~1.8           |
| 3000               | ~0.0           | ~0.5          | ~0.5           |
</details>

![](images/dd0c1f9520ced9f8700ba4d9bebe3b9252d1bf7efbce0a9f53b49adea8f3309d.jpg)

<details>
<summary>scatterplot</summary>

| Potential (mV) | A2930/A2850 |
| -------------- | ----------- |
| 10             | 2.8         |
| 0              | 4.5         |
| -10            | 7.5         |
</details>

FIG. 4. SRS spectral profile as a function of transmembrane potential. (a) The average SRS spectra of erythrocyte ghost membrane with different transmembrane potentials (Intensity normalized with $I _ { 2 8 5 0 } ) .$ . For particular potential value, n indicates the number of independent measurements performed on different erythrocyte ghosts $( n = 6 , \ - 1 0$ mV; $n = 8 .$ , þ1 mV; $n { = } 6 , + 1 0 \mathrm { m V } )$ . The spectra were obtained from pixels at top and/or bottom parts of erythrocyte ghosts. Shading stands for the standard deviation of n separate measurements. (b) $A _ { 2 9 3 0 } / A _ { 2 8 5 0 }$ as a function of transmembrane potential. Results were first analyzed using one-way analysis of variance (ANOVA, $p < 0 . 0 0 0 1 )$ . Further pairwise comparisons were performed with Student’s t-test $( ^ { \ast } p = 0 . 0 0 0 3$ , $^ { * * } p = 0 . 0 0 2 3$ , $^ { * * * } p < 0 . 0 0 0 1$ , n  6). $p < 0 . 0 5$ was considered statistically significant.

Previous studies have shown that transmembrane ion gradients,4 temperature, and $\mathrm { p H } ^ { 5 }$ influence Raman spectrum of the erythrocyte membrane in the $\mathrm { C H } _ { 3 }$ stretching region. Mikkelsen et al.4 suggested that intensification of the ${ \sim } 2 9 3 0 \mathrm { c m } ^ { - 1 }$ band reflected transfer of protein $\mathrm { C H } _ { 3 }$ groups from the apolar to more polar environments. Besides, external environments like temperature and pH may involve a rearrangement of protein residue orientation, which can be reflected by the $I _ { 2 9 3 0 } / I _ { 2 8 5 0 }$ ratio as well.5 SRS is a nonlinear enhancement process of spontaneous Raman scattering, and it exhibits identical spectrum as spontaneous Raman. Consistently, the observed spectral profile change herein could be assigned to the transmembrane potential induced conformation changes of the membrane proteins.

In summary, with erythrocyte ghost as a model system, we showed the feasibility of using hyperspectral SRS microscopy to probe membrane potential in a label-free manner. By further improving the temporal resolution, SRS microscopy can be potentially used to measure the membrane potential and even record the action potential propagation in living cells. This imaging technique can also be extended to detect mitochondrial membrane potential and study the apoptosis process.

The authors warmly thank Seung-Young Lee and Evan Philipps for providing the blood sample, Ping Wang for technical support, and Chun-Rui Hu for helpful discussion. B.L. acknowledges the financial support from the China Scholarship Council (No. 201306120093). N.J. thanks Spectra-Physics (Newport Corporation) for the loan of an InSight DeepSee laser. This work was partly supported by the Howard Hughes Medical Institute’s Visiting Scientist Program (J.-X.C.).

1 A. Grinvald and R. Hildesheim, Nat. Rev. Neurosci. 5(11), 874 (2004); J. A. N. Fisher. J. R. Barchi. C. G. Welle. G. H. Kim. P. Kosterin. A. L Obaid, A. G. Yodh, D. Contreras, and B. M. Salzberg, J. Neurophysiol. 99(3), 1545 (2008); H. Tsutsui, S. Karasawa, Y. Okamura, and A. Miyawaki, Nat. Methods 5(8), 683 (2008); J. M. Kralj, A. D. Douglass, D. R. Hochbaum, D. Maclaurin, and A. E. Cohen, ibid. 9(1), 90 (2012); E. W. Miller, J. Y. Lin, E. P. Frady, P. A. Steinbach, W. B. Kristan, and R. Y. Tsien, Proc. Natl. Acad. Sci. U.S.A. 109(6), 2114 (2012); D. S. Peterka, H. Takahashi, and R. Yuste, Neuron 69(1), 9 (2011).  
2 T. Hanafusa, R. Pujol-Borrell, L. Chiovato, D. Doniach, and G. F. Bottazzo, Clin. Exp. Immunol. 57(3), 639 (1984); C. Plachot and S. A. Lelie\`vre, Exp. Cell Res. 298(1), 122 (2004); C. Plachot, L. S. Chaboub, H. A. Adissu, L. Wang, A. Urazaev, J. Sturgis, E. K. Asem, and S. A. Lelie\`vre, BMC Biol. 7(1), 77 (2009); G. Chandramouly, P. C. Abad, D. W. Knowles, and S. A. Lelie\`vre, J. Cell Sci. 120(9), 1596 (2007).  
3 B. R. Lentz, Chem. Phys. Lipids 50(3), 171 (1989); K. Fushimi, J. A. Dix, and A. Verkman, Biophys. J. 57(2), 241 (1990); C. Sousa, C. Nunes, M. L-ucio, H. Ferreira, J. L. Lima, J. Tavares, A. Cordeiro-da-Silva, and S. Reis, J. Pharm. Sci. 97(8), 3195 (2008).  
4 R. B. Mikkelsen, S. P. Verma, and D. F. H. Wallach, Proc. Natl. Acad. Sci. U.S.A. 75(11), 5478 (1978).  
5 S. P. Verma and D. Wallach, Proc. Natl. Acad. Sci. U.S.A. 73(10), 3558 (1976).  
6 J.-X. Cheng and X. S. Xie, Coherent Raman Scattering Microscopy (CRC Press, 2012).  
7 J.-X. Cheng and X. S. Xie, J. Phys. Chem. B 108(3), 827 (2004); C. L. Evans and X. S. Xie, Annu. Rev. Anal. Chem. 1, 883 (2008).  
8 E. O. Potma and X. S. Xie, J. Raman Spectrosc. 34(9), 642 (2003).  
9 M. N. Slipchenko, T. T. Le, H. Chen, and J.-X. Cheng, J. Phys. Chem. B 113(21), 7681 (2009).  
10S. Yue, J. M. C-ardenas-Mora, L. S. Chaboub, S. A. Lelie\`vre, and J.-X. Cheng, Biophys. J. 102(5), 1215 (2012).  
11W. Min, C. W. Freudiger, S. Lu, and X. S. Xie, Annu. Rev. Phys. Chem. 62, 507 (2011); D. Zhang, P. Wang, M. N. Slipchenko, and J.-X. Cheng, Acc. Chem. Res. 47(8), 2282 (2014).  
12D. Zhang, P. Wang, M. N. Slipchenko, D. Ben-Amotz, A. M. Weiner, and J.-X. Cheng, Anal. Chem. 85(1), 98 (2013).  
13D. Fu, G. Holtom, C. Freudiger, X. Zhang, and X. S. Xie, J. Phys. Chem. B 117(16), 4634 (2013).  
14Y. Ozeki, W. Umemura, Y. Otsuka, S. Satoh, H. Hashimoto, K. Sumimura, N. Nishizawa, K. Fukui, and K. Itoh, Nat. Photonics 6(12), 845 (2012).  
15P. Wang, J. Li, P. Wang, C. R. Hu, D. Zhang, M. Sturek, and J. X. Cheng, Angew. Chem., Int. Ed. 52(49), 13042 (2013).  
16P. Wang, B. Liu, D. Zhang, M. Y. Belew, H. A. Tissenbaum, and J. X. Cheng, Angew. Chem., Int. Ed. 53(44), 11787 (2014).  
17T. Hellerer, A. M. Enejder, and A. Zumbusch, Appl. Phys. Lett. 85(1), 25 (2004).  
18C.-R. Hu, M. N. Slipchenko, P. Wang, P. Wang, J. D. Lin, G. Simpson, B. Hu, and J.-X. Cheng, Opt. Lett. 38(9), 1479 (2013).  
19G. Fairbanks, T. L. Steck, and D. Wallach, Biochemistry 10(13), 2606 (1971).  
20See supplementary material at http://dx.doi.org/10.1063/1.4919104 for details of the preparation of erythrocyte ghosts, intravesicular and extravesicular ionic compositions, and SRS spectrum analysis.  
21J.-x. Cheng, A. Volkmer, L. D. Book, and X. S. Xie, J. Phys. Chem. B 106(34), 8493 (2002).

Applied Physics Letters is copyrighted by AIP Publishing LLC (AIP) . Reuse of AIP content is subj ect to the terms at: http ://scitation. aip . org/termsconditions . For more information see http ://publishing . aip . org/authors/rights- and-permis sions .