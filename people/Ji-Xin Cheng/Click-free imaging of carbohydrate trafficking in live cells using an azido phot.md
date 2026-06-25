## P H YS I C S

# Click-free imaging of carbohydrate trafficking in live cells using an azido photothermal probe

Qing Xia1,2 , Harini A. Perera3 , Rylie Bolarinho4 , Zeke A. Piskulich4 , Zhongyue Guo5 , Jiaze Yin1 , Hongjian He1 , Mingsheng Li1 , Xiaowei Ge1 , Qiang Cui4 , Olof Ramström3,6 , Mingdi Yan3 \*, Ji-Xin Cheng1,2,4,5 \*

Real-time tracking of intracellular carbohydrates remains challenging. While click chemistry allows bio-orthogonal tagging with fluorescent probes, the reaction permanently alters the target molecule and only allows a single snapshot. Here, we demonstrate click-free mid-infrared photothermal (MIP) imaging of azide-tagged carbohydrates in live cells. Leveraging the micromolar detection sensitivity for 6-azido-trehalose (TreAz) and the 300-nm spatial resolution of MIP imaging, the trehalose recycling pathway in single mycobacteria, from cytoplasmic uptake to membrane localization, is directly visualized. A peak shift of azide in MIP spectrum further uncovers interactions between TreAz and intracellular protein. MIP mapping of unreacted azide after click reaction reveals click chemistry heterogeneity within a bacterium. Broader applications of azido photothermal probes to visualize the initial steps of the Leloir pathway in yeasts and the newly synthesized glycans in mammalian cells are demonstrated.

Copyright © 2024 The

Authors, some rights

reserved; exclusive

licensee American

Association for the

Advancement of

Science. No claim to

original U.S.

Government Works.

Distributed under a

Creative Commons

Attribution License 4.0

(CC BY).

## INTRODUCTION

Carbohydrates play important roles in various physiological processes. Most cell surfaces are coated with a layer of glycoproteins and glycolipid derived from posttranslational modification inside the cell (1, 2). Hence, monitoring intracellular trafficking of carbohydrates could elucidate the biological functions of carbohydrates in complex biological systems. Chromatography and mass spectrometry are used to quantify the amount of intracellular carbohydrates (3, 4). Yet, these in vitro methods lack spatial information and their destructive nature prohibits live-cell analysis. Fluorescence microscopy has been an invaluable tool for mapping intracellular carbohydrates with high selectivity. Accelerated efforts have been devoted to developing fluorescent analogs, based on fluorophores like boron-dipyrromethene and fluorescein, to track specific carbohydrates (5, 6), including glucose (7), maltose (8), and trehalose (9). However, these fluorophores typically have a size comparable to or larger than the target molecules (10), which often alters the intracellular local ization and uptake pathways of the target molecules. For example, a widely used fluorescent analog of glucose, 2-deoxy-2-[(7-nitro-2,1, 3-benzoxadiazol-4-yl)amino]-D-glucose (NBD-glucose), has been shown to enter cells independent of the glucose transporter (7).

To track molecules in their natural state, click chemistry has been developed for visualizing carbohydrates in live cells with minimal disruption to the surrounding cellular environment (11–13). This technique relies on tagging of carbohydrates with an azido group and subsequent mapping of glycans with the conjugation of azide to an alkyne-tagged fluorophore via click reaction (14, 15). The azide reporter, being small in size, has been shown not to interfere with cellular metabolism and has been used to study the function of carbohydrates in living systems, such as cell signaling (16), immunomodulation (17), and carbohydrate core formation (18). However, the fluorophores commonly used in click chemistry exhibit a relatively low cell permeability (19), thus requiring long incubation with biological samples ranging from 30 to 120 min and hindering real-time tracking of carbohydrates within living cells (14). Photobleaching and cytotoxicity present additional challenges. Moreover, the click reaction efficiency inside the cell remains uncertain, potentially leading to inaccurate imaging results.

Here, we present a click-free approach enabling real-time tracking of carbohydrates in live cells by using azide as a reporter under a mid-infrared photothermal (MIP) microscope (Fig. 1A). MIP is an emerging technique that detects the infrared (IR) absorption–induced photothermal effect with a visible beam (20). In this approach (21), a pulsed mid-IR laser excites the chemical bond vibration. Subsequent vibrational relaxation induces a temperature rise and consequent change of local refractive index. A visible beam then detects the modulated refractive index, providing spectroscopic information of the target molecule at 300-nm resolution. Thus, by dynamic MIP mapping of azide, the trafficking of target molecules can be tracked in real time. With a commercial optical photothermal infrared microscope, mIRage, Bai et al. (22) recently reported the detection of newly synthesized lipids in human-derived model systems incubated with azide-palmitic acid. However, limited by the relatively low numerical aperture (NA) objective in a co-propagation geometry, the measurements were restricted to dry samples, thus lacking dynamic information.

We find that a counter-propagation scheme is essential to detect nanoscale carbohydrates inside a single bacterium. Here, we developed an inverted laser-scan MIP microscope coupled with a lab-made CaF -bottom dish, based on previous MIP microscope (23), to enable high-speed longitudinal MIP imaging of azide in live cells. We selected 6-azido-trehalose (TreAz) and Mycobacterium smegmatis mc2 155 (M. smeg) as the test bed. Mycobacteria, including the pathogen Mycobacterium tuberculosis that is the single caustic agent to tuberculosis (TB), rely on trehalose as a crucial building block for essential cell wall glycolipids and various metabolites (11). It is proposed that TreAz undergoes a recycling pathway and is incorporated into glycoconjugates. Previously, Bertozzi and co-workers (3) orthogonally linked TreAz to an alkyne-functionalized fluorophore to investigate trehalose metabolic pathways in live M. smeg (Fig. 1B). However, the click reaction permanently changes the target molecule, thus only allowing a

1 Department of Electrical and Computer Engineering, Boston University, Boston, MA 02215, USA. 2 Photonics Center, Boston University, Boston, MA 02215, USA. 3 Department of Chemistry, University of Massachusetts, Lowell, MA 01854, USA. 4 Department of Chemistry, Boston University, Boston, MA 02215, USA. 5 Department of Biomedical Engineering, Boston University, Boston, MA 02215, USA. 6 Department of Chemistry and Biomedical Sciences, Linnaeus University, SE-39182 Kalmar, Sweden. \*Corresponding author. Email: jxcheng@bu.edu (J.-X.C.); mingdi\_yan@uml.edu (M.Y.)

A App-based MIP imaging  
![](images/c00cd528713408d57d18591b32b0acaaaafc82f536d8f363b441cdb30cbd2b9c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["App N₃"] --> B["Vibrational relaxation"]
  B --> C["Mid-IR absorption"]
  C --> D["Scattering ΔS (ΔT, Δn)"]
  D --> E["MIP intensity (arb. units)"]
  E --> F["Azide peak"]
```
</details>

B TreAz-based click chemistry strategy  
![](images/423b8a705d707d976b7433a359cb6ddf194964851aa111e3b3a14f789206aba0.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["(i) M. smeg"] --> B["(ii) TreAz incubation"]
  B --> C["(iii) Metabolic incorporation"]
  C --> D["(iv) Strain-promoted click reaction"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
```
</details>

![](images/d7d2a82a0468ff99ed7c42c8f8b0316f301da82b4ef3c3bd4ed57f37dfaa4bb9.jpg)

<details>
<summary>text_image</summary>

Click-based fluorescent probe
(i)
(ii)
(iii)
(iv) After click
Time
Multiple steps + single-shot imaging
</details>

D Click-free azido photothermal probe N3  
![](images/0f46e8dad87ff056a0e5e3ca392f27fc8d4fb048af79175b52951284c3431f3c.jpg)

<details>
<summary>text_image</summary>

(i)
Time
(ii)
(iii)
One step + dynamic imaging + spectroscopy
</details>

Fig. 1. Mapping trehalose trafficking in live mycobacteria via an App. (A) Principle of azido photothermal probe (App)–based mid-infrared photothermal (MIP) imaging. (B) 6-Azido-trehalose (TreAz)–based click chemistry strategy for trehalose tracking in live Mycobacterium smegmatis mc2 155 (M. smeg). (C) Schematic illustration of fluorescence imaging of TreAz detection in single M. smeg via click chemistry. (D) Schematic illustration of click-free imaging of trehalose trafficking in live M. smeg via App.

single snapshot of the molecule at the final state (Fig. 1C). To study specific pathways, in vitro tools were used to analyze the cell extracts (3), but they are time-consuming.

In this work, we use TreAz as an azido photothermal probe (App) to monitor the trafficking of trehalose in mycobacteria in situ (Fig. 1D). Through App-based MIP imaging, we directly visualized the trehalose recycling pathway in single mycobacteria, from cytoplasmic uptake to membrane localization. By monitoring the IR peak shift of azide in MIP spectra, we show that App can be used to sense interactions between TreAz and intracellular Ag85 proteins. Intriguingly, we detected a substantial amount of unreacted azide molecules after the click reaction, indicating heterogeneity of the click chemistry within a single mycobacterium and highlighting the reliability of App in tracing intracellular carbohydrates. To demonstrate the broad applicability of our approach, we further used commercially sourced Apps to explore galactose metabolism in yeasts and glycoconjugate biosynthesis in mammalian cells.

These results collectively showcase the versatility of App in unraveling complex biological processes.

## RESULTS

## MIP spectroscopy of TreAz

To demonstrate the use of azide as a photothermal probe of carbohydrate, we performed a density functional theory calculation to quantitate the IR absorption cross section of various chemical groups conjugated to trehalose. The IR absorption cross section of azide is \~17 times larger than that of nitrile and \~118 times larger than that of alkyne (table S1). Next, we synthesized TreAz (Fig. 2A) as a trehalose analog due to its known metabolic pathway and its ability to replace natural trehalose (3). Synthetic procedures of TreAz (24) are described in Supplementary Text 1. By Fourier transform infrared (FTIR) spectroscopy characterization of pure TreAz powder, the azide group in TreAz shows a strong IR peak at 2105 $\mathrm { c m } ^ { - 1 }$ with a band width of 34 $\mathrm { c m } ^ { - 1 }$ (Fig. 2B) in the spectrally silent window (Fig. 2C).

In addition, the IR absorbance of azide is known to be sensitive to local environment (25, 26). Under a co-propagating MIP microscope (fig. S1), the MIP spectrum of TreAz shows a distinct peak at $2 1 0 5 \mathrm { c m } ^ { - 1 }$ in dimethyl sulfoxide (DMSO) (Fig. 2D, green curve), consistent with the FTIR spectrum. Meanwhile, a blueshift of 13 cm−1 is observed upon changing the solvent to phosphate-buffered saline (PBS), likely due to a hydrogen-bond interaction between TreAz and water molecules (Fig. 2D, blue curve) (26, 27). Notably, the Ag85 protein, an intracellular trehalose-binding protein in mycobacteria, shows strong binding with trehalose (9). To mimic the intracellular environment, we mixed 10 mM TreAz with 1 mM Ag85 protein complex in PBS solution. The mixture of TreAz and Ag85 shows a blueshifted peak at $2 1 7 6 \mathrm { c m } ^ { - 1 }$ , while the mixture of 10 mM TreAz and 1 mM bovine serum albumin (BSA) protein shows the same peak position as the TreAz in PBS at 2118 $\dot { \mathrm { c m } } ^ { - 1 }$ (Fig. 2D, red and gray curves). Thus, the large azide peak shift unveils a strong interaction between TreAz and Ag85 proteins. Such a large blueshift of the azide peak indicating the interactions between azide and proteins has also been observed by nonlinear optical spectroscopy (28, 29). Together, the vibrational peak shift of azide highlights the potential of using App-based MIP imaging to sense intracellular molecular interactions. All MIP spectra in the silent window underwent a subtraction of solvent background as described in Supplementary Text 2 unless specially mentioned.

The MIP signal intensity of the azide is found to be linearly proportional to the TreAz concentrations with a limit of detection (LOD) around 1.3 μM in DMSO (Fig. 2E and fig. S2) and 23.6 μM in PBS (fig. S2). Such high detection sensitivity builds the foundation for Appbased MIP imaging of carbohydrate trafficking inside live cells.

## Live-cell MIP imaging of TreAz

With the high detection sensitivity, we explored counter-propagating MIP imaging of TreAz in live M. smeg. In this system (fig. S3), with a 532-nm probe beam and a high NA water immersion objective, we achieved a spatial resolution of 300 nm (fig. S4).

After a 26-hour incubation of 50 μM TreAz until reaching the logarithmic phase (fig. S5), a pinpointed MIP spectrum in the silent window (2000 to 2300 cm−1 ) acquired inside a live bacterium shows a peak of azido groups at 2180 cm−1 (Fig. 2F). This peak position is consistent with in vitro experiment and confirms the cellular uptake of TreAz.

For MIP imaging of intracellular azide, we chose 2180 $\mathrm { c m } ^ { - 1 }$ as the on-resonance wave number and obtained the azide signal via subtraction of the off-resonance water background at $2 1 0 0 \mathrm { c m } ^ { \underline { { { \bf v } } } _ { 1 } }$ (fig. S6, details in Supplementary Text 3). For TreAz-treated M. smeg, the azide signal is predominantly localized to the cell surface, indicating the incorporation of TreAz into the mycobacteria membrane (Fig. 2G). Depthresolved MIP imaging further demonstrates TreAz localization to the membrane (fig. S7). For the bacteria without TreAz treatment (control group), while individual bacteria exhibit high contrast at the amide II band of 1553 cm−1 , indicating the distribution of proteins, no contrast at the azide channel is observed.

To test the specificity of TreAz, Pseudomonas aeruginosa and Staphylococcus aureus were chosen as the Gram-negative and Grampositive controls, respectively. The results show that the control, which is M. smeg without treating with TreAz, and the other bacterial strains treated with TreAz exhibit minimal azide signal when compared with TreAz-treated M. smeg (Fig. 2H and fig. S8), revealing that the uptake of TreAz is specific for M. smeg.

Furthermore, to demonstrate the application of App in a complex environment, we cultured the TreAz-treated M. smeg on A549 lung cells. As shown in Fig. 2I (control group shown in fig. S9), a clear MIP contrast for single M. smeg on top of A549 cells was observed. The azide signal is located to the mycobacteria membrane, which is clearly distinguishable from the surrounding cell background and distinct from the protein channel (Fig. 2, J and K). These results highlight that App-based MIP is capable of imaging mycobacteria in a complex environment.

Previously, Goodacre and co-workers imaged isotopically labeled single bacteria using mIRage, a commercial MIP microscope (30). Fujita and co-workers imaged nitrile-containing molecules in single cell with a lab-built MIP microscope (31). In both works, the singlecell imaging was performed in a co-propagation manner, where the probe beam is weakly focused by a reflective objective.

We performed a head-to-head comparison between co-propagating (fig. S1) and counter-propagating MIP imaging (fig. S3) of TreAz-treated M. smeg. The MIP signal of single bacteria in the counter-propagating geometry shows an enhanced signal-to-noise ratio (SNR) by 11.3 times and increased resolution by 2.5 times compared to those in the copropagating microscope, which allows us to resolve the membrane structure of the bacteria (fig. S10). Theoretically, when the focus volume for the visible beam is comparable to the thermal lens size, photothermal imaging gives the best sensitivity (32). Thus, while co-propagating MIP is good for measuring the LOD from liquid specimens, counterpropagating MIP is the choice for high-sensitivity detection of nanoscale features in live cells.

## Visualization of trehalose recycling pathway in single mycobacteria

A recycling metabolic pathway was proposed for TreAz utilization in mycobacteria (3, 33), as shown in Fig. 3A. The LpqY-SugABC transporters deliver trehalose into the cytoplasm, where trehalose is converted to trehalose monomycolate (TMM). The TMM is then transported to the periplasmic space and used by the protein Ag85 to synthesize trehalose dimycolate to build the cell wall. By fluorescence microscopy, Backus et al. (9) demonstrated the uptake of fluorescein isothiocyanate–conjugated trehalose analog (FITC-Tre) by mycobacteria. However, due to the large size of FITC, FITC-Tre did not enter the cytoplasm. Genetic and biochemical methods are informative but unsuitable for live-cell experiments (34). Thus, direct visualization of the trehalose metabolic pathway remains a challenge.

To apply the App to monitor the TreAz trafficking in mycobacteria, we performed time-course MIP imaging of logarithmic-phase M. smeg incubated with TreAz for different time periods (Fig. 3B). The transmission and MIP image of proteins were recorded as references. Initially (0 hour), while the protein channel showed high contrast on the cell body, no azide signal was observed. After 1 hour of incubation, the azide signal appeared inside the cell body. By the 2-hour mark, the azide signal showed up to the cell surface. After 4 hours, the azide was predominantly localized at the poles. Such a pattern is consistent with the polar growth model of M. smeg, indicating active growth and division in the presence of TreAz.

Given the involvement of Ag85 and LpqY proteins in the TreAz uptake pathway (3), we further investigated the uptake of TreAz by LpqY and Ag85C deletion mutants. The results revealed a complete abolishment of azide signals in both ∆LpqY (Fig. 3C) and ∆Ag85C mutants (Fig. 3D), confirming that TreAz requires LpqY and Ag85C for entering the cytoplasm and recycling to the membrane, supported by statistical results (Fig. 3E). Together, App-based MIP enabled visualization of the complete TreAz recycling pathway, from uptake, membrane recycling, to pole localization.

![](images/be6d7e268269197af53cc25a904b268fd9ed898be59a6cb2dddfccf8370309ac.jpg)

<details>
<summary>chemical</summary>

Chemical structure of a glycoside analog with hydroxyl and amine functional groups, labeled as App: TreAz
</details>

B  
![](images/26d176f17653e338c6f3cd37cc1e33fb5f36f78d797e007daaa1dd1e9e5e8f02.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Normalized absorbance |
| ------------------ | --------------------- |
| 2105               | Peak                  |
</details>

C  
![](images/90ccdee6c871812344fb7895d6e56be94eb13632ad4603ea325cbb02104a3fb0.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Absorbance |
| ------------------ | ---------- |
| 1000               | 0.0        |
| 1500               | 0.2        |
| 2000               | 0.0        |
| 2500               | 0.0        |
| 3000               | 0.1        |
| 3500               | 0.2        |
| 4000               | 0.0        |
</details>

D  
![](images/ef8a37ae2c290652e23084cccb133ac4d3ee601ed10ccba0cc1260c2e92dc6a1.jpg)

<details>
<summary>line chart</summary>

| Condition       | Peak W/ Ag85 (cm⁻¹) | Peak W/ BSA (cm⁻¹) | Peak DMSO (cm⁻¹) |
| --------------- | ------------------- | ------------------ | ---------------- |
| In PBS          | 2176                | -                  | -                |
| In PBS          | 2118                | -                  | -                |
| In DMSO         | 2105                | -                  | -                |
</details>

E  
![](images/a29889617eb5f11874691075f9b07c3dc8959d7fcf5f699897d3d2af22137488.jpg)

<details>
<summary>line chart</summary>

| Concentration (mM) | MIP intensity (arb. units) |
| ------------------ | -------------------------- |
| 0                  | 0                          |
| 1                  | 0.3                        |
| 2                  | 0.7                        |
| 10                 | 2.8                        |
</details>

F  
![](images/ad8da083aff0b04edf47485cd331f8be52a120cd227b52324d54aa14005e0454.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Normalized MIP intensity |
| ------------------ | ------------------------ |
| 2180               | Peak                     |
</details>

H

![](images/fa2f8210a5d043b25251350abebbebf4fc40ea8cb9be645ab20f0b89334be0ba.jpg)

<details>
<summary>bar chart</summary>

| Group        | MIP intensity (arb. units) |
| ------------ | -------------------------- |
| M. smeg      | 1.8 × 10⁻²                 |
| Control      | 0.2 × 10⁻²                 |
| P. aeruginosa| 0.1 × 10⁻²                 |
| S. aureus    | 0.05 × 10⁻²                |
</details>

TreAz-treated M. smeg on A549 cell

G  
![](images/1983b6cb7e4464a8d2cbca4f55efab025611d5cfccbaf77655432fd74128cda9.jpg)

<details>
<summary>text_image</summary>

Transmission
Amide II 1553 cm⁻¹
Azide 2180 cm⁻¹
Merge
M. smeg, w/ TreAz
Control
-0.04 0.04 0 0.3 0 0.02 10 µm
</details>

![](images/34f24c386b17f6a296b74211345f6c40bdd46e7f3b8a38d707423f1a810a768e.jpg)

<details>
<summary>text_image</summary>

Transmission
Merge
Amide II, 1553 cm⁻¹
Azide, 2180 cm⁻¹
20 µm
</details>

J  
![](images/87a0006751e773cc83430216cd163123910d19bf768df43ec488de62a238a557.jpg)

<details>
<summary>text_image</summary>

Protein
Azide
Transmission + azide
Zoom-in
2 µm
</details>

K  
![](images/f4969f72813f53f886abdbf9750d63b3d9ecacb1555602c17a7f8713c395d207.jpg)

<details>
<summary>line chart</summary>

| X Distance (µm) | Protein | Azide |
| --------------- | ------- | ----- |
| 0               | 0.2     | 0.1   |
| 1               | 0.8     | 0.1   |
| 2               | 0.1     | 0.05  |
| 3               | 0.2     | 0.1   |
| 4               | 1.0     | 0.9   |
| 5               | 0.8     | 1.0   |
| 6               | 0.8     | 0.1   |
| 7               | 0.2     | 0.1   |
| 8               | 0.1     | 0.1   |
| 9               | 0.05    | 0.1   |
</details>

Fig. 2. In vitro detection and live-cell MIP imaging of TreAz. (A) Molecular structure of TreAz. Orange characters indicate the azide group. (B) Fourier transform infrared (FTI R) spectrum of pure TreAz powder. (C) FTI R spectrum of M. smeg. Red region indicates the spectrally silent window, free from endogenous biomolecule peaks. (D) MIP spectra of 10 mM TreAz in dimethyl sulfoxide (DMSO; green curve), 10 mM TreAz in phosphate-buffered saline (PBS; blue curve), 10 mM TreAz mixed with 1 mM Ag85 protein complex in PBS (red curve), and 10 mM TreAz mixed with 1 mM bovine serum albumin (BSA) in PBS (gray curve). (E) MIP signal intensity as a function of TreAz concentration in DMSO. (F) Pinpointed MIP spectrum of intracellular TreAz, with the pinpoint indicated by cross in (G). (G) MIP image of TreAz in single live M. smeg. Scale bar, 10 μm. (H) Specificity analysis of TreAz uptake by M. smeg. MIP signal intensity of TreAz-treated M. smeg until logarithmic phase $( n = 9 5 )$ was compared to the signa of the control $( n = 9 2 , * * * * P = 8 . 6 7 \times 1 0 ^ { - 2 6 7 } ) ,$ P. aeruginosa $( n = 8 4 , * * * * P = 1 . 0 8 \times 1 0 ^ { - 2 7 0 } )$ , and S. aureus $( n = 1 0 7 , ^ { * * * * } P = 4 . 3 2 \times 1 0 ^ { - 2 8 3 } ) .$ . Data are given as means ± SD. (I) Transmission and MIP image in the protein Amide II and azide channels of TreAz-treated M. smeg on A549 cells. Scale bar, 20 μm. (J) Zoomed-in views [white dotted boxes labeled in (I)] of single M. smeg on A549 cells. Scale bars, 2 μm. (K) MIP intensity profiles in both protein and azide channels of single M. smeg on A549 cells [white dotted lines labeled in (J)].

A  
![](images/5cfda789c89b184483bdd84399f343f80e7adcf06d04f7a40d0218a3d84914bd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Trehalose"] --> B["Ag85"]
  C["TDM"] --> B
  B --> D["Trehalose monomycolate"]
  B --> E["Trehalose dimycolate"]
  B --> F["Mycomembrane"]
  B --> G["PG: Peptidoglycan"]
  B --> H["Plasma membrane"]
  I["TMM"] --> J["SugABC -LpqY"]
  J --> K["TMM"]
    style A fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style I fill:#f9f,stroke:#333
    style J fill:#ccf,stroke:#333
    style K fill:#ccf,stroke:#333
```
</details>

B

M. smeg, w/ TreAz treated to different growth points  
![](images/0e1d2b18de9f1a4e37773806d2c44fe7786fd3e33621ce8d3bc05db4fb39db6a.jpg)

<details>
<summary>text_image</summary>

0 hours
1 hours
2 hours
4 hours
Transmission
Amide II 1553 cm⁻¹
Azide 2180 cm⁻¹
-0.04 0.04 0 0.1 0 0.03 10 µm
</details>

![](images/193608a0e4287cd6a4531b3a55838b10eb4974395c8b27618d71ca4efc69e102.jpg)

<details>
<summary>text_image</summary>

C
ΔLpqY, w/ TreAz
Transmission
10 µm
Azide 2180 cm⁻¹
-0.15 0.15 0 0.02
</details>

![](images/e11400fd6a283fc87a8aa09ec5571d71e9264ab7ae0ba5dc24a50888bd3234b6.jpg)

<details>
<summary>text_image</summary>

D
ΔAg85C, w/ TreAz
Transmission
Azide 2180 cm⁻¹
10 µm
-0.15 0.15 0 0.02
</details>

E  
![](images/bb2ab61fa567603082f7c1a080bce274d8774ee8fe1fa7847e61ac39c92ff449.jpg)

<details>
<summary>bar chart</summary>

| Treatment | MIP intensity (arb. units) ×10⁻² |
| --------- | ------------------------------- |
| M. smeg   | 1.1                             |
| ΔAg85C    | 0.3                             |
| ΔLpqY     | 0.2                             |
</details>

Fig. 3. Visualization of TreAz metabolic recycling pathway in live M. smeg via App-based MIP imaging. (A) Schematics of trehalose metabolic recycling pathway in M. smeg. (B) Time-course MIP imaging of live M. smeg treated with 50 μM TreAz in transmission mode, MIP Amide II , and Azide window. Scale bar, 10 μm. (C) MIP imaging of live ∆LpqY mutant treated with 50 μM TreAz. Scale bar, 10 μm. (D) MIP imaging of live ∆Ag85C mutant treated with 50 μM TreAz. Scale bar, 10 μm. (E) Quantitative azide signal of TreAz-treated M. smeg and the mutants. MIP signal intensity of TreAz-treated M. smeg for 1 hour $( n = 8 9 )$ was compared with the signal of the mutant ∆Ag85C $( n = 8 3 , * * * * P = 8 . 1 4 \times 1 0 ^ { - 5 2 } )$ and $\Delta L p q Y ( n = 7 7 ,$ $* * * * P = 8 . 7 4 \times 1 0 ^ { - 6 0 } )$ . Data are given as means ± SD.

## App-based MIP imaging allows dynamic tracking of TreAz in a single bacterium

To validate TreAz uptake, we used click reaction–based fluorescence imaging using a commercial fluorescent probe, AF 488 DBCO (Supplementary Text 4). This probe contains an alkyne group for the click reaction with the azido group in TreAz. M. smeg was treated with TreAz for 26 hours until reaching the logarithmic phase. The mycobacteria mem brane was then imaged by both MIP imaging of azide before the click reaction and confocal fluorescence imaging of AF 488 DBCO after the click reaction (Fig. 4A). From the intensity plot profile of single M. smeg, clear membrane patterns were resolved by both MIP and fluorescence imaging at similar SNR (Fig.  4B) affirming the visualization of azide-tagged glycoconjugates on the mycobacteria membrane by App-based MIP.

Notably, while fluorescence undergoes fast photobleaching, the MIP signal is resistant to photobleaching, which is essential for dynamic analysis (Fig. 4C). To further demonstrate the dynamic imaging capabilities of App, we made a CaF -bottom culture dish suitable for longitudinal counter-propagating MIP imaging of live cells (Fig. 4D). Longitudinal MIP imaging of TreAz uptake into cytoplasm and recycling to membrane over 1 hour period is shown in Fig. 4E, where the transmission images serve as a reference. Together, these results validate the trehalose recycling pathway and showcase the advantages of App-based MIP imaging.

## App-based MIP imaging reveals uneven efficiency of click chemistry in a cellular environment

As illustrated in Fig. 5A, the azide is converted into triazole after the strain-promoted click reaction. Thus, by MIP imaging of the remaining azide after click chemistry, one could evaluate the efficiency of the click reaction within a cell. To validate this, we added a scanning fluorescence imaging modality (fig. S11) to our MIP microscope, enabling multimodal fluorescence and MIP imaging of the same bacteria. Upon completion of the click reaction, the MIP signals of azido groups that undergo click reactions would disappear. Meanwhile, unabolished MIP signals indicate the unreacted azide after the click reaction.

P  
![](images/67846d2ad79f3807a8ba1a05f5a8f822656d03b98f0e98895db146160d09e207.jpg)

<details>
<summary>text_image</summary>

A
Azide 2180 cm⁻¹
MIP imaging
before click
reaction
Fluorescence
imaging after click
reaction
5 µm
</details>

B  
![](images/7f65652a675fac5900d3188fb2a2cbbffe750e45907d39599e5ae6db5a69a9fe.jpg)

<details>
<summary>line chart</summary>

| Distance (μm) | MIP  | Fluorescence |
| ------------- | ---- | ------------ |
| 0             | 0.0  | 0.0          |
| 1             | 1.0  | 1.0          |
| 2             | 0.0  | 0.0          |
</details>

C  
![](images/b6efc5813c18aab4080579000ed5bc8ddab70ab11fcf74a80804211e583f0591.jpg)

<details>
<summary>line chart</summary>

| Time (s) | Norm. MIP intensity | Norm. fluorescence intensity |
| -------- | ------------------- | --------------------------- |
| 0        | 1.0                 | 1.0                         |
| 5        | 0.9                 | 0.9                         |
| 10       | 0.8                 | 0.8                         |
| 15       | 0.9                 | 0.7                         |
| 20       | 0.8                 | 0.6                         |
| 25       | 0.9                 | 0.5                         |
| 30       | 0.8                 | 0.4                         |
| 35       | 0.9                 | 0.3                         |
| 40       | 0.8                 | 0.2                         |
</details>

D  
![](images/3be54ef816c92d9326e19be81e920c3906d0e9649a8240a60658ac001caad488.jpg)

<details>
<summary>text_image</summary>

Dynamic MIP imaging
Water immersion objective
Cover
slide
Medium
Dish
CaF₂
Reflective objective
</details>

E  
![](images/04ddac8dfcd6905cc41fa5cbe011208cacb82a810d91e8b91c34c499cc830d08.jpg)

<details>
<summary>heatmap</summary>

| Condition | Time (min) | Transmission (cm⁻¹) |
|-----------|------------|---------------------|
| W/ 50 µM TreAz | 1          | 2180                |
| W/ 50 µM TreAz | 10         | 2180                |
| W/ 50 µM TreAz | 20         | 2180                |
| W/ 50 µM TreAz | 35         | 2180                |
| W/ 50 µM TreAz | 45         | 2180                |
| W/ 50 µM TreAz | 60         | 2180                |
</details>

Fig. 4. App-based MIP imaging allows dynamic tracking of TreAz in a single bacterium. (A) MIP imaging of 50 μM TreAz-treated M. smeg before the click reaction and confocal fluorescence imaging of TreAz-treated M. smeg after the click reaction. Scale bar, 5 μm. (B) Line profiles across the bacteria indicated in MIP and fluorescence imaging of M. smeg in (A). (C) MIP and fluorescence signal intensities versus scanning time. (D) The MIP imaging mode with a lab-made CaF2-bottom culture dish for longitudinal imaging of live M. smeg. (E) Real-time MIP imaging of TreAz trafficking in M. smeg. Scale bar is 5 μm in TreAz-treated group and 10 μm in Tre-treated group, respectively.

We incubated M. smeg with TreAz until the logarithmic phase and followed a standard protocol of click chemistry (3). Notably, we observed a substantial amount of MIP signal from azide after the click reaction in different fields of view (Fig. 5B) and two independent repeats (fig. S12).

Statistically, a significantly negative correlation between fluorescence signals and MIP signals of azide was observed on individual bacteria [Fig. 5C, Pearson’s correlation coefficient $( r ) = - 0 . 7 2 ]$ . To explore whether the unreacted azido groups truly come from the heterogeneity of click reaction, a series of validation experiments were conducted. First, we repeated the same experiment with a commercial confocal fluorescence microscope. A similar pattern of uneven fluorescence distribution was found (Fig. 5D). Next, depth-resolved confocal fluorescence imaging of M. smeg after click reaction was performed. In three-dimensional (3D) confocal fluorescence, a portion of the cells dis played uneven fluorescence signals along the cell body (Fig. 5E), elimi nating the influence of nonuniformity caused by different focal planes. Last, to evaluate the impact from the diffusion of fluorescent probes, M. smeg was incubated only with the fluorescent probe and imaged without washing. Uniform fluorescence intensity was observed along individual bacteria, indicating good permeability and uniform diffusion of the fluorescent probe inside the bacteria (Fig. 5F). Collectively, these data reveal the heterogeneity of strain-promoted click chemistry in the mycobacteria membrane environment.

![](images/05b86f90e4b54f5cf3c46763431941e48dd3442d857cd5fa3d651bf0fd401f2c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Click reaction"] --> B["Imaging"]
  B --> C["Fluorescence: Reacted azide"]
  B --> D["MIP: Unreacted azide"]
```
</details>

![](images/26f10eecaae132e7e9e2b179186faa6d4ca41fcd0f78991da7d0abc62bc9e249.jpg)

<details>
<summary>scatter plot</summary>

| Fluorophore area (%) | Azide area (%) |
| --------------------- | -------------- |
| 0                     | 70             |
| 10                    | 65             |
| 20                    | 60             |
| 30                    | 55             |
| 40                    | 50             |
| 50                    | 45             |
| 60                    | 40             |
| 70                    | 35             |
| 80                    | 30             |
| 90                    | 25             |
</details>

![](images/46435cd8be072985129f1a076ceab7a0948383717f9ae01e5aef1a97684c27a9.jpg)

<details>
<summary>text_image</summary>

B
M. smeg w/ TreAz treated, imaging after click reaction
Transmission	Fluorescence	Azide 2180 cm⁻¹	Merge
FOV 1
FOV 2
FOV 3
-0.1	0.1	0	0.3	0	0.03	10 µm
</details>

![](images/b0eb0e774603a11404e976c47299e1924ec774518ed1d2fb783ad56e85df90bf.jpg)

<details>
<summary>natural_image</summary>

Transmission and 2D fluorescence microscopy images showing rod-shaped bacterial cells with yellow outline, alongside fluorescent green structures (no text or symbols)
</details>

![](images/c8c848bcba6cd7140fe80d052c4b1eb1b33f7ce3faeeb6c63cc9ec73f99e5a9f.jpg)

<details>
<summary>text_image</summary>

E
3D fluorescence
F
M. smeg only w/ fluorescent probe, no washing
Transmission
Fluorescence
5 µm
0
50
0
0
</details>

Fig. 5. App-based MIP imaging reveals heterogeneity of click reaction inside single M. smeg. (A) Schematic illustration of complimentary MIP and fluorescence imaging contrast of TreAz-treated single M. smeg after click reaction. (B) Colocalized MIP and fluorescence imaging of single M. smeg that treated with 50 μM TreAz and after click reaction. FOV, field of view. Scale bar, 10 μm. (C) Statistical analysis of azide and fluorophore area distribution on single M. smeg $( n = 5 7 )$ . Pearson’s $r = - 0 . 7 2 ,$ , indicating statistically significant negative correlation. (D) Uneven fluorescence distribution was observed in a commercial confocal fluorescence imaging of single M. smeg treated with TreAz and underwent click reaction. Yellow dashed lines indicate single bacteria. Scale bars, 5 μm. (E) Depth-resolved confocal fluorescence imaging of TreAztreated M. smeg after click reaction in (D). Yellow dashed lines indicate single bacteria. Each grid represents a size of $: \mu \mathsf { m }$ . (F) Confocal fluorescence imaging of M. smeg only with fluorescent probe incubation. Scale bars, 5 μm.

The observed heterogeneity in the click reaction within mycobacteria could potentially be attributed to the relatively large size of dibenzocycloctynes in the clickable dye AF 488 DBCO. It has been reported that the dibenzocycloctynes could not be site-specifically incorporated into proteins (35), and the sterically encumbered nature of the molecule may limit the effectiveness of the click reaction in bioconjugation applications (36). To further explore the origin of the heterogeneity, logarithmic-phase M. smeg was incubated with TreAz until different growth points and then analyzed either via MIP imaging of the azide or by fluorescence imaging of the fluorescent probe after click reaction (fig. S13). After 0-, 1-, 2-, and 4-hour incubation of TreAz, MIP imaging demonstrated a high resolution to differentiate the locations of the azide reporter at different time points. In comparison, the fluorescence images displayed a weak but uniform contrast at 1 hour and uneven intensity along individual bacteria at 2 and 4 hours. These results indicate that click reaction is more favorable in the cytoplasm and on the poles.

## App-based MIP imaging of carbohydrates in various biological systems

Benefiting from the rapid development of click chemistry, a variety of azide-tagged carbohydrate products are commercially available or with well-defined synthetic procedures (37, 38). To demonstrate the versatil ity of Apps in other biological systems, we explored galactose metabo lism in yeast Saccharomyces cerevisiae and glycoconjugate biosynthesis in mammalian HeLa cells by harnessing commercially sourced azido carbohydrates.

Galactose serves as a vital carbon source for energy production in yeast cells, primarily metabolized through the Leloir pathway (39). The pathway initiates with the conversion of β-d-galactose into α-d-galactose (α-d-Gal) catalyzed by a mutarotase enzyme, followed by phosphorylation of α-d-Gal. The enzymatic phosphorylation of galactose into galactose-1-phosphate exhibits a preference for the α-form of the galactose (40), where α and β anomers of galactose differ in the stereochemistry of the C-1 carbon atom (Fig. 6A).

To visualize the Leloir pathway in live cells, we used two azide-tagged galactoses: 6-azido-6-deoxy-d-galactose (6-GalAz) and 1-deoxy-β-dgalactopyranosyl azide (1-GalAz), with the azide at C-6 and C-1, respectively (Fig. 6B). Yeast cells cultured in medium with 6-GalAz showed a sharp azide peak at $2 1 5 6 ~ \mathrm { c m } ^ { - 1 }$ , while the cells cultured with 1-GalAz presented a clear azide peak at $2 1 3 0 { \mathrm { c m } } ^ { - 1 }$ (fig. S14). Live-cell MIP imaging revealed a concentrated distribution of 6-GalAz and a diffuse distribution of 1-GalAz (Fig. 6B). Control cells cultured with d-galactose (Gal) without azide conjugation showed no peaks in the silent region. Fluorescence imaging of the yeast cells after click reactions further substantiated the MIP results, confirming the uptake of 6-GalAz and 1-GalAz (fig. S15).

Moving beyond imaging, we explored protein-galactose interactions in the Leloir pathway through azide peak shifts (Fig. 6C). An obvi ous azide peak shift of 6-GalAz from $2 1 1 \dot { 7 } \mathrm { c m } ^ { - 1 }$ in PBS to 2156 $\mathrm { c m } ^ { - 1 }$ in the yeast cell is observed, indicative of carbohydrate-enzyme binding (41). In contrast, 1-GalAz showed no azide peak shift between solution and live-cell MIP spectrum, indicating that the azide group occupying the C-1 position hinders its further metabolism in the Leloir pathway. Consequently, 1-GalAz exhibited a diffuse pattern inside the cell. These findings provide visual evidence of the interactions between carbohydrates and proteins during the Leloir pathway. Together, MIP detection of peak shift in the azide vibration offers a way to study intracellular carbohydrate-enzyme interaction, which is beyond the reach of click reaction–based fluorescence imaging.

We further extended App-based MIP imaging to monitor glycan synthesis in mammalian cells. For glycan visualization, tetraacylated N-azidoacetylmannosamine $( \mathrm { A c _ { 4 } M a n N A z } )$ has been widely used for metabolic labeling of glycoconjugates in cells and mice through click reaction (15, 42, 43). To demonstrate the applicability of App to mammalian cells, we performed MIP imaging of $\mathrm { A c _ { 4 } M a n N A z }$ to map glycosylation in HeLa cells (Fig.  6D). N-acetyl-d-mannosamine (ManNAc) was used as a control. HeLa cells treated with 50 μM Ac ManNAz presented a strong azide peak at $2 1 4 0 ~ \mathrm { c m } ^ { - 1 }$ in the MIP spectrum, whereas the control cells showed no peak in the silent region (fig. S16). In Ac ManNAz-treated cells, the azide signals were predominantly localized to the cell surface and inside the cells, especially in the endoplasmic reticulum (ER) regions, as confirmed by their positions in the transmitted images and colocalized fluorescence imaging of ER-Tracker (Fig. 6D and figs. S17 and S18). No azide contrast shows up in the control group. The MIP images at 1553 cm−1 provide a reference map of protein distribution inside cells. Our result reveals $\mathrm { A c _ { 4 } M a n N A z }$ incorporation into the newly synthesized azido-glycoconjugates inside HeLa cells and on the cell surface, consistent with the glycoconjugate biosynthesis process (44). Click reaction–based fluorescence imaging validated the MIP results (fig. S19).

The high spatial resolution and high sensitivity of App-based MIP imaging allowed observation of two distinct peaks of azide-tagged carbohydrates across a single protein-rich component (Fig. 6E). As the MIP intensity of proteins increased in the selected areas labeled as the position from 1 to 3 (Fig. 6E), the azide peak at $2 1 1 0 \mathrm { c m } ^ { - 1 }$ attenuates, and a shifted azide peak at 2140 $\mathrm { c m } ^ { - \mathrm { i } }$ shows up (Fig. 6F). As a reference, the MIP spectrum of 10 mM $\mathrm { A c _ { 4 } M a n N A z }$ in ethanol exhibited a peak at $2 1 1 \bar { 0 } \mathrm { c m } ^ { - 1 }$ . Together, this spectroscopic data suggests a transition from free states to protein-bound states of the azidocarbohydrate molecules.

## DISCUSSION

Click chemistry–based fluorescent imaging has become a powerful method for studying carbohydrate metabolisms. In this work, we introduce App-based MIP imaging that enables dynamic mapping of cellular entry, intracellular trafficking, and metabolism of carbohydrates without the need for click chemistry. App-based MIP imaging of intracellular carbohydrates in various biological systems, from single bacteria, yeasts, to mammalian cells, is demonstrated. Trehalose recycling in single mycobacteria, from cytoplasmic uptake, membrane recycling, to pole localization, was directly visualized. Notably, we observed a substantial amount of unreacted azide after following a standard protocol of click reaction, indicating click chemistry heterogeneity and incompleteness within a single mycobacterium. Moreover, through monitoring the shift of the azide vibrational peak in the silent window, we show that App can be used to sense intracellular carbohydrate-protein interactions, which is beyond the reach of fluorescence imaging.

We note that click-free vibrational imaging was first demonstrated via Raman imaging of 5-ethynyl-2′-deoxyuridine (EdU), where Yamakoshi et al. (45) used the alkyne-tagged cell proliferation probe to detect newly synthesized DNA in HeLa cells. Yet, a long acquisition time of 49 min for one image (\~50 μm by 50 μm) was needed. The importance of Raman tags was underscored in subsequent studies, which confirmed that alkyne tags offer relatively strong Raman intensity (46). Stimulated Raman scattering (SRS) microscopy further improved the imaging speed and offered a LOD of 200 μM for alkyne-tagged molecules (47). This advancement enabled bio-orthogonal chemical imaging of a variety of biomolecules tagged with vibrational probes (48–50). Moreover, super-resolution vibrational imaging using photoswitchable Raman probes achieved exceptional chemical specificity and spatial resolution beyond the optical diffraction limit (51, 52). Collectively, the established use of Raman tags in imaging small molecules has notably advanced the field of vibrational imaging. Compared to Raman scattering, IR absorption benefits from a much larger cross section (53). Min and co-workers reported direct IR imaging of azides in single cells, yet with low spatial resolution of around 3 μm (54, 55). MIP microscopy offers both high resolution and high sensitivity through the use of a tightly focused visible probe beam.

To compare MIP and SRS imaging in the silent window, we performed SRS spectroscopic detection of pure TreAz powder, which exhibited a Raman peak of the azide group at 2105 cm−1 . However, for 2.5 mM TreAz dissolved in DMSO, no SRS peak of azide vibration was distinguished from the DMSO background (fig. S20). We further performed SRS imaging of M. smeg treated with 50 μM TreAz for 26 hours. Although SRS showed a high contrast at the C-H channel, the azide signals in single bacterium were not detectable by SRS microscopy (fig. S20). Because azide is known to be a weak Raman scatterer, we further selected EdU as a model compound with a large Raman cross section to facilitate a fair comparison between MIP and SRS imaging. As shown in fig. S20, EdU exhibits a Raman peak for the alkyne group at approximately 2123 cm−1 , with an estimated LOD of 276 μM. This result is consistent with the result reported by Min and co-workers (47) and is much lower than the SRS LOD for azide (>2.5 mM). We also note that the SRS LOD for EdU is above the MIP LOD for azide (1.3 μM in DMSO) by two orders of magnitude. This difference is largely due to the different cross sections for SRS and IR, i.e., the IR cross section for azide (4.46 × 10−18 cm2 per molecule) is larger than the apparent SRS cross section (56) for alkyne $( \sim 4 . 5 \times 1 0 ^ { - 2 0 } \ : \mathrm { c m } ^ { 2 }$ per molecule under 150-mW Stokes power). It is also important to note that the vibrational tags, experimental parameters, and conditions differ notably between MIP and SRS imaging. Our results offer an insight of the sensitivity achievable by MIP and SRS imaging in the silent window. Users should select appropriate vibrational tags and imaging modalities when mapping lowconcentration biomolecules in the silent window.

![](images/81560cadf44404435750869349eee31ddee486921337962077df3708a9104f76.jpg)

<details>
<summary>chemical</summary>

Leloir pathway diagram showing β-D-Gal, α-D-Gal, and Gal-1-P enzyme interactions with enzyme 1 and enzyme 2
</details>

C  
![](images/612d33b63d8a3217afdd2accd2ccdf9af3e8189ed34989a63ef0fa607159cf6a.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Normalized MIP intensity |
| ------------------ | ------------------------ |
| 2117               | Peak                     |
| 2156               | Peak                     |
</details>

![](images/65248e2b186fbdc1566de1f28f3940cb4821ce6301e60a301c659e4b950e4bdb.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Normalized MIP intensity |
| ------------------ | ------------------------ |
| 2130               | Peak                     |
</details>

B  
![](images/6d7fbd3bf276433dd8f4d97dac00759d84687a0b0a3152744755d380d08b0464.jpg)

<details>
<summary>scatterplot</summary>

| Sample     | Ion        | Transmission | Azide   | Merge   |
| ---------- | ---------- | ------------ | ------- | ------- |
| 6-GalAz    | N₃         | ~0.9         | 2156 cm⁻¹ | -       |
| 6-GalAz    | N₃         | ~0.8         | 2130 cm⁻¹ | -       |
| 1-GalAz    | -          | ~0.7         | 2156 cm⁻¹ | -       |
| Control: Gal | -      | ~0.6         | 2156 cm⁻¹ | -       |
</details>

D  
Treated carbohydrates  
![](images/a2818851ec7ae3cb1d408a0907caf685f0a17899a75224f0d0ce65ab7e17b200.jpg)  
AcManNAz

![](images/76c5d2c1c4c163f6b82833dd188f17ac1fd62f2d4bbdca8bd200ac709a01f04c.jpg)  
Control: ManNAc

Transmission  
![](images/37e57e4d6a8a0012443b076026b86f40b9db9970824f86d0ae0e2032ba8a5571.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of cellular or material structure with 20 μm scale bar (no text or symbols beyond scale indicator)
</details>

![](images/b7fdcf70b67577a793c833ebcbf26e6c1e47335e7f777012344a97cd714a30ec.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular or tissue structure with scattered dark spots and a dashed outline (no text or symbols)
</details>

-0.1

Azide  
![](images/c70509a2b6fe0974acec968f50061794f4503ec5a0617aa1a99b3417cfb0fe0c.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescently labeled cellular structures with a 2140 cm⁻¹ scale marker (no text or symbols beyond scale indicator)
</details>

![](images/fd6cecfad0f5ddb7d702438653097536570f19e3a3280ab1ae180e673ed0087c.jpg)

<details>
<summary>text_image</summary>

2140 cm⁻¹
</details>

0.1 0

Protein  
![](images/c89ae5017ed8f2d54b8293e22825ab8b95d587faf13b31045ad6636e00d5fb97.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing cellular structures with a 1553 cm⁻¹ scale marker (no text or symbols beyond scale indicator)
</details>

![](images/7e14c9dce85a4b244124f38e436ccd6584e794256154955674ec048594d8627a.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing cellular structures with blue fluorescence, labeled '4553 cm⁻¹' (no other text or symbols)
</details>

0.020

Merge  
![](images/7067b19e9cfd8bea879a113cb408a064c442466817c226658fb163b8abd3c999.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular structures with red and yellow staining (no text or symbols visible)
</details>

![](images/eb39dfd63df069b74a6d4f2ad6e42acbe6d87bdc4ef05cab5c221c81b8c0da9a.jpg)

<details>
<summary>natural_image</summary>

Microscopic tissue image showing cellular structures with scattered dark spots and a color scale bar (no text or symbols)
</details>

0.2

![](images/80b2817302fa137d81fa7b2e85b55cc36832e7a4ca22ea4805ade5f4bc02fc1c.jpg)

<details>
<summary>text_image</summary>

E
Protein
1553 cm⁻¹
Zoom-in
□ 3
□ 2
□ 1
2 µm
0	0.2
</details>

Azide  
![](images/e4bff406a3dba01bd873b821c10e0f4b6cedfdc99890fa2174af48d3f37c74f5.jpg)

<details>
<summary>text_image</summary>

2140 cm⁻¹
□ 3
□ 2
□ 1
</details>

2 0

![](images/29f9a7ff3e5ef48a4b70b56207350586be4820e7b2976a4282dfcc86aff37f9e.jpg)

<details>
<summary>text_image</summary>

Azide
2110 cm⁻¹
□ 3
□ 2
□ 1
</details>

0.02 0

Azide Merge  
![](images/8b6a5702e1a2a70ab8fda86e1931992c305f7542a379316680c9d3c9f3d56806.jpg)

<details>
<summary>text_image</summary>

1
2
3
1
</details>

0.01

F  
![](images/6738b1e00664d0d4c97c29a2fb9e132c1f03d15ed239bc67541192e7431ce04a.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Normalized MIP intensity |
| ------------------ | ------------------------ |
| 2140               | ~0.3                     |
| 2110               | ~0.13                    |
</details>

Fig. 6. App-based MIP detection of carbohydrate metabolism and interaction with proteins in various biological systems. (A) Initial steps of Leloir pathway for galactose metabolism in yeast. β-d-galactose (β-d-Gal) is reversibly converted into α-d-galactose (α-d-Gal) via mutarotase (Enzyme 1), where the α and β anomers of galactose differ in the stereochemistry of the C-1 carbon atom, labeled with purple circles. α-d-Gal is then phosphorylated to galactose-1-phosphate (Gal-1-P) via galactokinase (Enzyme 2), which can subsequently be converted into a derivative of glucose to generate energy. (B) MIP imaging of live yeast cells cultured with 2% 6-GalAz, 1-GalAz, and Gal for 24 hours. Scale bar, 5 μm. The experiment was repeated independently three times with similar results. (C) Validation of interactions between proteins and galactose in Leloir pathway via azide peak shift. Solid curves are MIP spectra acquired from GalAz-cultured yeast cells. Dash-dotted curves are MIP spectra of 50 mM GalAz in PBS solution. (D) MIP imaging of 50 μM Ac4ManNAz- and ManNAc-treated HeLa cells in azide and protein channels. Scale bar, 20 μm. White dotted lines in transmitted images indicate the outline of the cells. The experiment was repeated independently three times with similar results. (E) Multicolor MIP imaging of Ac4ManNAz-treated HeLa cell in protein, azide, and merge channels. The imaging areas are zoomed-in views of white dotted boxes labeled in (D). (F) Spectroscopic correlation between azide peak shift and protein abundance in Ac4ManNAz-treated HeLa cell. The MIP spectra and protein profile were acquired from the white boxes labeled area in (E). Gray dotted line indicates the MIP spectrum of 10 mM Ac4ManNAz in ethanol.

One limitation of App-based MIP imaging lies in the water photo thermal background in the silent window. The water molecules ex hibit a weak absorption centered around 2100 cm−1 , contributed by the water bend-libration combination band (57). In this work, we used the difference between on- and off-resonance images to map the azide in biological cells. This method requires the acquisition of two MIP images upon tuning the quantum cascade laser. A more elegant way of distinguishing MIP signals from the water photothermal background is to use thermal dynamics (58). Compared to nanoscale objects, water exhibits a much larger thermal decay constant. Thus, by signal digitization (58) or two-window boxcar detection (59), time-resolved measurement of thermal dynamics can be pursued to extract the signal from water background upon excitation with a single IR pulse per pixel.

For future work, as TreAz works well for MIP imaging of trehalose uptake by mycobacteria with a high specificity, it can be potentially used for detecting individual mycobacteria in clinical samples, aiding in rapid diagnosis of TB infection. Another important direction will be real-time MIP imaging of glycan synthesis in vivo upon treatment of live tissues or animals with azido-carbohydrates. The concept of App can be extended to other molecules other than carbohydrates. For instance, azido–amino acids can be used to facilitate the study of protein synthesis and function in live cells. We envision that Appbased MIP imaging will pave a way for investigation of the localization, trafficking, and metabolism of biomolecules in life and diseases.

## MATERIALS AND METHODS

## Cell lines and materials

M. smeg mc2 155 and the mutants were obtained from the Biodefense and Emerging Infections Research Resources Repository (BEI Resources). P. aeruginosa 1133, S. aureus ATCC6538, A549 cell line, and HeLa cell line were obtained from American Type Culture Collection. S. cerevisiae strain (W303) was obtained from a published strain (60). Ag85 complex (NR-14855) was obtained from the BEI Resources. BSA (A7030), DMSO (472301), d-(+)-trehalose dihydrate (Tre; 90210), Luria-Bertani broth (LB; 1102850500), and yeast nitrogen base (YNB; 51483) were purchased from Sigma-Aldrich. Ethanol (A962-4) was purchased from Thermo Fisher Scientific. Complete supplement mixture (CSM; 1001-010) was obtained from Sunrise Science Products. Middlebrook 7H9 (271310) and ADC enrichment (212352) were purchased from BD Biosciences. Glycerol (AC158922500) was purchased from Acros Organics. AF 488 DBCO (218F0) was purchased from Lumiprobe

Corporation. 6-GalAz (AF432) and 1-GalAz (GL631) were purchased from Synthose Inc. Gal (48260-100G-F), Ac ManNAz (900917-50MG), and ManNAc (A8176-250MG) were purchased from Sigma-Aldrich. TreAz was synthesized and purified according to a previous procedure (24, 61). CaF2 substrates (ø 25 mm and 1-mm thick, CAFP25-1) were purchased from Crystran. EdU (20518) was purchased from Cayman Chemical. ER-Tracker Red dye (E34250) was purchased from Thermo Fisher Scientific Inc.

## MIP microscopy

For LOD measurement, an upright co-propagating MIP microscope was used (fig. S1). The system was constructed on an inverted microscope frame (IX73, Olympus), integrating a continuous-wave 532-nm laser (Samba, HUBNER photonics) for the visible probe and a pulsed quantum cascade laser (MIRcat 2400, Daylight Solutions) tunable from 900 to 2300 cm−1 as the mid-IR pump. The visible probe was co-aligned with the mid-IR pump laser and focused into a sample by a reflective objective lens (40×, 0.5 NA, LMM440x-P01, Thorlabs). The probe photons were collected in forward direction. Two photodiodes (PDs; DET100A2, Thorlabs) were used to acquire the transmission and MIP images, respectively. For MIP detection, the current from the photodiode was converted to voltage through a 50-ohm resistor (T4119, Thorlabs), filtered by a high-pass filter (0.12 to 1000 MHz, ZFHP-0R12-S+, Mini-Circuits), and then amplified by two low-noise amplifiers (gain, 40 dB; 1 kHz to 500 MHz; SA-251F6, NF Corporation). Last, the signal was filtered by a low-pass filter (BLP-1.9+, DC-1.9 MHz, 50 ohms, Mini Circuits) and then delivered to a lock-in amplifier (HF2LI, Zurich) to demodulate the MIP signals.

For intracellular imaging, a counter-propagating beam geometry on the same upright MIP microscope was used (fig. S3). The IR beam was focused on the sample with a reflective objective lens (40×, 0.5 NA, LMM440x-P01, Thorlabs) and the visible beam was focused by a water immersion objective lens (60×, 1.2 NA, UPlanSApo, Olympus). A galvanometer mirror (Saturn 1B, ScannerMax) was used to scan the visible beam. Simultaneously, the IR beam was synchronously scanned by another pair of galvanometer mirrors (GVS001, Thorlabs). The probe photons were collected in the forward direction using a visible/IR dichroic mirror (GEBBAR-3-5-25, Andover Corporation), and the intensity was sensed by a PD (DET100A2, Thorlabs). For longitudinal MIP imaging of App within the same cells, an inverted counterpropagating MIP microscope was used. In this setup, a lab-built frame was used. The IR beam was directed from the bottom, while the visible light was focused from the top. The accessories were the same as those used in the upright counter-propagating MIP microscope.

For LOD measurement, the IR laser was set with a repetition rate of 100 kHz and pulse width of 100 ns to reduce heat accumulation during long-time spectral scanning. The mid-IR laser continuously swept wave numbers from 2000 to 2300 cm−1 at a speed of 50 cm−1 per s. The raw MIP spectra were obtained from a lock-in amplifier with a time constant of 20 ms. For MIP imaging of bacteria, the IR laser was set with a repetition rate of 1 MHz, a pulse width of 80 ns, and an average power after the objective ranging from 8 to 20 mW, depending on the wave number. An average power of the probe laser was \~50 mW after the objective. The MIP images were acquired with a pixel dwell time of 10 μs and a step size of 150 nm. For hyperspectral MIP imaging of yeast and HeLa cells, the IR laser was set with a repetition rate of 290 kHz and pulse width of 100 ns to reduce heat accumulation during longtime scanning. The hyperspectral scanning range was from 2060 to 2220 cm−1 with a step size of 2 cm−1 per frame. The MIP images were acquired with a pixel dwell time of 25 μs and a step size of 200 nm (yeast) and 300 nm (HeLa cell), respectively.

## Limit of detection

The LOD determines the minimum analyte concentration at which the MIP signal can be reliably distinguished from the background noise and is defined as

$$
\mathrm{LOD} = \frac {3 \times S T D}{S l o p e} \tag {1}
$$

where STD is the standard deviation of the MIP intensity in the blank solvent solution and Slope is the slope of the calibration curve relating concentration to MIP signal. To get the calibration curve, MIP spectra of TreAz were obtained at various concentrations in PBS and DMSO solutions, respectively. A 2-μl solution was sandwiched between two CaF2 substrates, and the MIP spectra were acquired via a co-propagating MIP system. This geometry ensured that the focus volume of the probe beam was comparable to the thermal lens of the solution medium, providing an ideal MIP signal for LOD detection (32). After background subtraction of the solvent spectra and baseline correction, the MIP intensity at azide peak was used to establish the calibration curve between concentration and MIP signal. The slope values were determined as $0 . 0 1 6 8 ~ \mathrm { m M } ^ { - 1 }$ for PBS and 0.277 $\mathrm { m } \dot { \mathrm { M } } ^ { - 1 }$ for DMSO measurements. The STD was measured from the MIP intensity of the solvent at the corresponding azide peak $( 2 1 1 8 ~ \mathrm { c m } ^ { - 1 }$ for PBS and $2 0 1 5 \mathrm { c m } ^ { - 1 }$ for DMSO). Specifically, $3 \times \overset { \cdot } { S } T D _ { \mathrm { P B S } } = 3 . 9 7 \times 1 0 ^ { - 4 }$ and $3 \times S T D _ { \mathrm { D M S O } } = 3 . 7 4 \times 1 0 ^ { - 4 }$ . According to Eq. 1, the LOD of TreAz is determined to be 1.3 μM in DMSO and 23.6 μM in PBS.

## FTIR measurement

The FTIR spectra of all samples were measured on an attenuated total reflection FTIR spectrometer (Nicolet Nexus 670, Thermo Fisher Scientific). The spectra resolution is $2 ~ { \mathrm { c m } } ^ { - 1 }$ , and each spectrum was measured with 128 scans. All spectra were automatically normalized by the baseline correction on the system. In addition, for samples in solvent, the background spectra of the corresponding solvent were subtracted.

## Fluorescence imaging

The fluorescence imaging was pursued by a laser-scanning fluo rescence modality integrated into the MIP microscope. An additional 488-nm laser (06-MLD, Cobolt) was co-aligned with the 532-nm laser to serve as the excitation source, with the laser power output set at 12 mW. The power of the excitation laser on sample was around 0.1 mW. A 60× water immersion objective with NA of 1.2 was used (UPlanApo, Olympus) as MIP imaging. The fluorescence emission was collected in an epi-direction with a filter set (excitation filter: FES0500, Thorlabs; dichroic beam splitter: Di03-R405/488/532/635-t1-25×36, Sermock; emission filter: FF01-525/30-25, Sermock). For fluorescence imaging of ER-Tracker, the 532-nm laser served as the excitation source, with the laser power output set at 1 mW. The fluorescence emission was collected in an epi-direction with an emission filter (ET609/34m, Chroma). The emitted photons were collected by a photomultiplier tube (H10721-110, Hamamatsu). The transmitted images were collected using the MIP imaging mode. The confocal fluorescence images were acquired on a Zeiss LSM 880 laser scanning microscope equipped with an oil immersion objective (63×, 1.4 NA), and ZEN software was used to collect the data.

## Data processing

All images were analyzed and displayed with ImageJ. The data were plotted using Origin. Pseudocolor was added to the MIP and fluorescent images with ImageJ. Individual bacterium was marked for the quantification of single-cell MIP signals, except for the measurement presented in Fig. 5B, where the MIP and fluorescence intensities on the cell surface were measured. The transmitted images were normalized by the subtraction of the background. 3D reconstruction was done with ImageJ using the 3D viewer plugin. The detailed MIP spectra and images processing workflow are shown in Supplementary Texts 2 and 3, respectively.

## Bacteria preparation

Middlebrook 7H9 broth supplemented with ADC enrichment was prepared using Middlebrook 7H9 (4.7 g), glycerol (2.0 ml), and distilled water (900 ml). The mixture was then autoclaved (Tuttnauer EZ 10, Hauppauge, NY) for sterilization before use. Following autoclaving, ADC enrichment (100 ml) was added to the sterilized Middlebrook 7H9 broth once its temperature reached 45°C. M. smeg was cultured in 7H9 liquid medium in incubation tubes at 37°C with shaking until the optical densities measured at wavelength of 600 nm $\mathrm { ( O D _ { 6 0 0 } ) }$ reached 0.5, typical within 22 to 26 hours (fig. S5). A stock solution of 2.5 mM TreAz in PBS buffer was prepared. To 1.96 ml of M. smeg in an incubation tube, 40 μl of TreAz stock solution was added, which gave the TreAz concentration of 50 μM. Subsequently, M. smeg was incubated at $3 7 ^ { \circ } \mathrm { C }$ for different incubation time of 0, 1, 2, and 4 hours while shaking at 250 rpm. For the control group, M. smeg was treated with Tre with the same procedure.

To culture M. smeg on A549 lung cells, A549 cells were seeded on $\mathrm { C a F } _ { 2 }$ substrates in a culture dish with a density of $1 \times 1 0 ^ { 5 }$ colonyforming units ml−1 with 2 ml of culture medium overnight at $3 7 ^ { \circ } \mathrm { C }$ and 5% CO . After cell attachment, cells were washed with PBS three times and then fixed with 4% formaldehyde. The cells were lastly washed two times with PBS. M. smeg cells was added into the dish with 7H9 liquid medium and 50 μM TreAz and incubated with the A549 cells for 2 hours at $3 7 ^ { \circ } \mathrm { C } .$ For the control group, no TreAz was added to the culture dish. Last, the samples were sandwiched between a $\mathrm { C a F } _ { 2 }$ substrate and a cover glass for imaging.

P. aeruginosa and S. aureus were cultured in LB medium at $3 7 ^ { \circ } \mathrm { C }$ with shaking until $\mathrm { O D } _ { 6 0 0 }$ reached 0.5. To 1.96 ml of P. aeruginosa and S. aureus in incubation tube, 40 μl of TreAz stock solution was added, which gave the TreAz concentration of $5 0 \mu \mathrm { M }$ . The bacterial cells were then incubated at 37°C for 1 hour while shaking at 250 rpm.

After collection, the bacteria were centrifuged (3500 rpm, 3 min) and washed three times with PBS. About 1 to 2 μl of concentrated bacteria were sandwiched between a $\mathrm { C a F } _ { 2 }$ substrate and a cover glass ready for imaging. For dynamic MIP imaging, about 10 μl of concentrated bacteria were added to a lab-made CaF -bottom culture dish containing 200 μl of PBS with 50 μM TreAz or Tre. To prevent bacterial movement, a glass cover slide was added to the center of the dish.

## Yeast cell preparation

The synthetic defined (SD) medium was prepared by mixing 79 mg of CSM, 746 mg of YNB, and 100 ml of distilled water and was sterilized by autoclaving before use. Yeast cells were grown 3 days in SD medium with 2% (w/v) ethanol at 30°C with shaking without other carbohydrates. After collection, the cells were centrifuged (3000 rpm, 5 min) and washed twice with sterilized distilled water. Then, the cells were incubated in SD medium with 2% (w/v) Gal or GalAz as the sole carbon source for 1 day at 30°C with shaking. After collection, the cells were centrifuged (3000 rpm, 5 min) and washed three times with sterilized distilled water. About 1 to 2 μl of concentrated yeast cells were sandwiched between the special $\mathrm { C a F } _ { 2 }$ substrates and the cover glass for imaging.

## HeLa cell preparation

HeLa cells were seeded on $\mathrm { C a F } _ { 2 }$ substrates with a density of 1 $\times 1 0 ^ { 5 } \mathrm { m l } ^ { - 1 }$ with 2 ml of minimum essential medium overnight at $3 7 ^ { \circ } \mathrm { C }$ and 5% $\mathrm { C O } _ { 2 } .$ After cell attachment, the cells were treated with Ac ManNAz or ManNAc by adding 1.25 μl (for a final concentration of 50 $\mu \mathrm { M }$ Ac ManNAz or ManNAc) of 10 mM Ac ManNAz or ManNAc in ethanol stock solution to each dish. Cells were incubated with Ac ManNAz or ManNAc for 40 hours at $3 7 ^ { \circ } \mathrm { C }$ . Cells were then washed with PBS three times and then fixed with 4% formaldehyde. The cells were lastly washed two times with PBS and sandwiched under a piece of cover glass for imaging.

## Click chemistry

The click reaction was performed following an established protocol (3). Bacterial cells or yeast cells $( 2 0 0 ~ \mu \mathrm { l } )$ were transferred to a 0.5-ml sterile centrifuge tube, followed by centrifugation (3500 rpm, 3 min, 4°C) and triple washing with PBS with 0.5% BSA (PBSB). Subsequently, the cells were incubated with 50 μM AF 488 DBCO (Lumiprobe, catalog no. 218F0) (diluted from a 10 mM DMSO stock solution into PBSB) for 1 hour at room temperature in the dark. After centrifugation (3500 rpm, 3 min, $4 ^ { \circ } \mathrm { C } )$ and washing three times with PBSB, the cells were fixed with 200 μl of 4% paraformaldehyde in PBS in the dark for 10 min. Final washing two times with PBS readied the cells for analysis by fluorescence or MIP microscopy.

For click reaction in HeLa cells, after treatment of Ac4ManNAz or ManNAc, the cells were rinsed two times with live-cell imaging solution (A14291DJ, Invitrogen). Each dish was filled with 50 μM AF 488 DBCO (diluted from a 10 mM DMSO stock solution) in solution and incubated for 1 hour at $3 7 ^ { \circ } \mathrm { C }$ in the dark. The cells were washed three times with PBS and were fixed with 4% formaldehyde for 15 min at room temperature in the dark. The cells were lastly washed two times with PBS and sandwiched under a piece of cover glass ready for imaging.

## ER-tracker labeling

For colocalized experiments with ER-Tracker, HeLa cells were incubated with 50 μM Ac ManNAz for 40 hours at $3 7 ^ { \circ } \mathrm { C }$ , followed by labeling with ER-Tracker Red dye with instructions provided by the manufacturer.

## Statistics and reproducibility

All experiments were independently repeated at least three times with similar results. The sample sizes for all statistical experiments exceeded 7 per group. All data collected during the experiments were included. No data were excluded from the analyses. Statistical analysis was performed using Origin version 2018. All groups were expressed as means $\pm \ \mathrm { S D } _ { \cdot }$ . Column means were compared using one-way analysis of variance (ANOVA). When ANOVA showed a significant difference, pair wise comparisons between group means were examined by Bonferroni comparison test. Significance was defined when $P < 0 . 0 5$ .

## Supplementary Materials

This PDF file includes:

Supplementary Texts 1 to 4

Figs. S1 to S25

Table S1

References

## REFERENCES AND NOTES

1. C . Reily, T. J. Stewart, M. B. Renfrow, J. Novak, Glycosylation in health and disease. Nat. Rev. Nephrol. 15, 346–366 (2019).  
2. E . Cabib, J. Arroyo, How carbohydrates sculpt cells: Chemical control of morphogenesis in the yeast cell wall. Nat. Rev. Microbiol. 11, 648–655 (2013).  
3. B. M. Swarts, C. M. Holsclaw, J. C. Jewett, M. Alber, D. M. Fox, M. S. Siegrist, J. A. Leary, R. Kalscheuer, C. R. Bertozzi, Probing the mycobacterial trehalome with bioorthogonal chemistry. J. Am. Chem. Soc. 134, 16123–16126 (2012).  
4. J. Hofmann, H. S. Hahm, P. H. Seeberger, K. Pagel, Identification of carbohydrate anomers using ion mobility–mass spectrometry. Nature 526, 241–244 (2015).  
5. A. Barattucci, C. M. A. Gangemi, A. Santoro, S. Campagna, F. Puntoriero, P. Bonaccorsi, Bodipy-carbohydrate systems: Synthesis and bio-applications. Org. Biomol. Chem. 20, 2742–2763 (2022).  
6. B. Thomas, K. C. Yan, X. L. Hu, M. Donnier-Marechal, G. R. Chen, X. P. He, S. Vidal, Fluorescent glycoconjugates and their applications. Chem. Soc. Rev. 49, 593–641 (2020).  
7. K. E. Hamilton, M. F. Bouwer, L. L. Louters, B. D. Looyenga, Cellular binding and uptake of fluorescent glucose analogs 2-­NBDG and 6-­NBDG occurs independent of membrane glucose transporters. Biochimie 190, 1–11 (2021).  
8. A. Zlitni, G. Gowrishankar, I. Steinberg, T. Haywood, S. Sam Gambhir, Maltotriose-based probes for fluorescence and photoacoustic imaging of bacterial infections. Nat. Commun. 11, 1250 (2020).  
9. K. M. Backus, H. I. Boshoff, C. S. Barry, O. Boutureira, M. K. Patel, F. D’Hooge, S. S. Lee, L. E. Via, K. Tahlan, C. E. Barry, B. G. Davis, Uptake of unnatural trehalose analogs as a reporter for Mycobacterium tuberculosis. Nat. Chem. Biol. 7, 228–235 (2011).  
10. Y. Shen, F. Hu, W. Min, Raman imaging of small biomolecules. Annu. Rev. Biophys. 48, 347–369 (2019).  
11. N . Banahene, H. W. Kavunja, B. M. Swarts, Chemical reporters for bacterial glycans: Development and applications. Chem. Rev. 122, 3336–3413 (2022).  
12. J. A. Prescher, C. R. Bertozzi, Chemistry in living systems. Nat. Chem. Biol. 1, 13–21 (2005).  
13. B. Kenry, Bio-orthogonal click chemistry for In vivo bioimaging. Trends Chem. 1, 763–778 (2019).  
14. M. J. Hangauer, C. R. Bertozzi, A FRET -based fluorogenic phosphine for live-cell imaging with the staudinger ligation. Angew. Chem. Int. Ed. Engl. 47, 2394–2397 (2008).  
15. J. M. Baskin, J. A. Prescher, S. T. Laughlin, N. J. Agard, P. V. Chang, I. A. Miller, A. Lo, J. A. Codelli, C. R. Bertozzi, Copper-free click chemistry for dynamicin vivoimaging. Proc. Natl. Acad. Sci. U.S.A. 104, 16793–16797 (2007).  
16. M. Boyce, I. S. Carrico, A. S. Ganguli, S. H. Yu, M. J. Hangauer, S. C. Hubbard, J. J. Kohler, C. R. Bertozzi, Metabolic cross-talk allows labeling of O-linked β-N-acetylglucosamine modified proteins via the N-acetylgalactosamine salvage pathway. Proc. Natl. Acad. Sci. U.S.A. 108, 3141–3146 (2011).  
17. N . Geva-Zatorsky, D. Alvarez, J. E. Hudak, N. C. Reading, D. Erturk-­Hasdemir, S. Dasgupta, U. H. von Andrian, D. L. Kasper, In vivo imaging and tracking of host–microbiota interactions via metabolic labeling of gut anaerobic bacteria. Nat. Med. 21, 1091–1100 (2015).  
18. H . Liang, K. E. DeMeester, C. W. Hou, M. A. Parent, J. L. Caplan, C. L. Grimes, Metabolic labelling of the carbohydrate core in bacterial peptidoglycan and its applications. Nat. Commun. 8, 15015 (2017).  
19. L . Wang, M. Tran, E. D’Este, J. Roberti, B. Koch, L. Xue, K. Johnsson, A general strategy to develop cell permeable and fluorogenic probes for multicolour nanoscopy. Nat. Chem. 12, 165–172 (2020).  
20. D . Zhang, C. Li, C. Zhang, M. N. Slipchenko, G. Eakins, J. X. Cheng, Depth-resolved mid-infrared photothermal imaging of living cells and organisms with submicrometer spatial resolution. Sci. Adv. 2, e1600521 (2016).  
21. Q. Xia, J. Yin, Z. Guo, J. X. Cheng, Mid-­Infrared photothermal microscopy: Principle, instrumentation, and applications. J. Phys. Chem. B 126, 8597–8613 (2022).  
22. Y. Bai, C. M. Camargo, S. M. K. Glasauer, R. Gifford, X. Tian, A. P. Longhini, K. S. Kosik, Single-cell mapping of lipid metabolites using an infrared probe in human-derived model systems. Nat. Commun. 15, 350 (2024)  
23. J. Yin, M. Zhang, Y. Tan, Z. Guo, H. He, L. Lan, J. X. Cheng, Video-rate mid-infrared photothermal imaging by single-pulse photothermal detection per pixel. Sci. Adv. 9, eadg8814 (2023).  
24. S. A. Wijesundera, S. H. Liyanage, P. Biswas, J. F. Reuther, M. Yan, Trehalose-grafted glycopolymer: Synthesis via the staudinger reaction and capture of Mycobacteria. Biomacromolecules 24, 238–245 (2023).  
25. X. S. Gai, B. A. Coutifaris, S. H. Brewer, E. E. Fenlon, A direct comparison of azide and nitrile vibrational probes. Phys. Chem. Chem. Phys. 13, 5926–5930 (2011)  
26. K. I. Oh, J. H. Lee, C. Joo, H. Han, M. Cho, β-Azidoalanine as an IR probe: Application to amyloid Aβ(16-22) aggregation. J. Phys. Chem. B 112, 10352–10357 (2008).  
27. S. M. Salehi, D. Koner, M. Meuwly, Vibrational spectroscopy of N3– in the gas and condensed phase. J. Phys. Chem. B 123, 3282–3290 (2019).  
28. M. Lim, P. Hamm, R. M. Hochstrasser, Protein fluctuations are sensed by stimulated infrared echoes of the vibrations of carbon monoxide and azide probes. Proc. Natl. Acad. Sci. U.S.A. 95, 15315–15320 (1998).  
29. M. Garcia-­Viloca, K. Nam, C. Alhambra, J. L. Gao, Solvent and protein effects on the vibrational frequency shift and energy relaxation of the azide ligand in carbonic anhydrase. J. Phys. Chem. B 108, 13501–13512 (2004).  
30. C . Lima, H. Muhamadali, Y. Xu, M. Kansiz, R. Goodacre, Imaging isotopically labeled bacteria at the single-cell level using high-resolution optical infrared photothermal spectroscopy. Anal. Chem. 93, 3082–3088 (2021).  
31. F. Tai, K. Koike, H. Kawagoe, J. Ando, Y. Kumamoto, N. I. Smith, M. Sodeoka, K. Fujita, Detecting nitrile-containing small molecules by infrared photothermal microscopy. Analyst 146, 2307–2312 (2021).  
32. H . Ni, Y. Yuan, M. Li, Y. Zhu, X. Ge, C. V. P. Dessai, L. Wang, J. X. Cheng, Millimeter-deep micron-resolution vibrational imaging by shortwave infrared photothermal microscopy. arXiv:2310.05798 (2023).  
33. M. Jackson, C. M. Stevens, L. Zhang, H. I. Zgurskaya, M. Niederweis, Transporters involved in the biogenesis and functionalization of the mycobacterial cell envelope. Chem. Rev. 121, 5124–5157 (2021).  
34. R. L. Nieto, C. Mehaffy, M. N. Islam, B. Fitzgerald, J. Belisle, J. Prenni, K. Dobos, Biochemical characterization of isoniazid-resistant Mycobacterium tuberculosis: Can the analysis of clonal strains reveal novel targetable pathways? Mol. Cell. Proteomics 17, 1685–1701 (2018).  
35. T . Plass, S. Milles, C. Koehler, C. Schultz, E. A. Lemke, Genetically encoded copper-free clic chemistry. Angew. Chem. Int. Ed. Engl. 50, 3878–3881 (2011).  
36. C . S. McKay, M. G., Click chemistry in complex mixtures: Bioorthogonal bioconjugation. Chem. Biol. 21, 1075–1101 (2014).  
37. Z. J. Witczak, in Carbohydrate Chemistry, A. Pilar Rauter, T. Lindhorst, Eds. (The Royal Society of Chemistry, 2010), vol. 36, pp. 176–193.  
38. S. Cecioni, D. Goyard, J.-P. Praly, S. Vidal, in Carbohydrate Microarrays: Methods and Protocols, Y. Chevolot, Ed. (Humana Press, 2012), pp. 57–68.  
39. R. Caputto, L. F. Leloir, R. E. Trucco, C. E. Cardini, A. C. Paladini, The enzymatic transformation of galactose into glucose derivatives. J. Biol. Chem. 179, 497–498 (1949).  
40. C . A. Sellick, R. N. Campbell, R. J. Reece, in International Review of Cell and Molecular Biology (Academic Press, 2008), vol. 269, pp. 111–150.  
41. J. B. Thoden, H. M. Holden, The molecular architecture of galactose mutarotase/ UDP-galactose 4-epimerase from Saccharomyces cerevisiae. J. Biol. Chem. 280, 21900–21907 (2005).  
42. M. Kufleitner, L. M. Haiber, V. Wittmann, Metabolic glycoengineering-exploring glycosylation with bioorthogonal chemistry. Chem. Soc. Rev. 52, 510–535 (2023).  
43. P. V. Chang, J. A. Prescher, E. M. Sletten, J. M. Baskin, I. A. Miller, N. J. Agard, A. Lo, C. R. Bertozzi, Copper-free click chemistry in living animals. Proc. Natl. Acad. Sci. U.S.A. 107, 1821–1826 (2010).  
44. C . R. Bertozzi, L. L. Kiessling, Chemical glycobiology. Science 291, 2357–2364 (2001).  
45. H . Yamakoshi, K. Dodo, M. Okada, J. Ando, A. Palonpon, K. Fujita, S. Kawata, M. Sodeoka, Imaging of EdU, an alkyne-tagged cell proliferation probe, by Raman microscopy. J. Am. Chem. Soc. 133, 6102–6105 (2011).  
46. H . Yamakoshi, K. Dodo, A. Palonpon, J. Ando, K. Fujita, S. Kawata, M. Sodeoka, Alkyne-tag Raman imaging for visualization of mobile small molecules in live cells. J. Am. Chem. Soc. 134, 20681–20689 (2012).  
47. L . Wei, F. Hu, Y. Shen, Z. Chen, Y. Yu, C. C. Lin, M. C. Wang, W. Min, Live-cell imaging of alkyne-tagged small biomolecules by stimulated Raman scattering. Nat. Methods 11, 410–412 (2014).  
48. S. Hong, T. Chen, Y. Zhu, A. Li, Y. Huang, X. Chen, Live-cell stimulated Raman scattering imaging of alkyne-tagged biomolecules. Angew. Chem. Int. Ed. 53, 5827–5831 (2014).  
49. F. Hu, L. Shi, W. Min, Biological imaging of chemical bonds by stimulated Raman scattering microscopy. Nat. Methods 16, 830–842 (2019).  
50. H . Fujioka, J. Shou, R. Kojima, Y. Urano, Y. Ozeki, M. Kamiya, Multicolor activatable Raman probes for simultaneous detection of plural enzyme activities. J. Am. Chem. Soc. 142, 20701–20707 (2020).  
51. J. Ao, X. Fang, X. Miao, J. Ling, H. Kang, S. Park, C. Wu, M. Ji, Switchable stimulated Raman scattering microscopy with photochromic vibrational probes. Nat. Commun. 12, 3089 (2021).  
52. J. Shou, A. Komazawa, Y. Wachi, M. Kawatani, H. Fujioka, S. J. Spratt, T. Mizuguchi, K. Oguchi, H. Akaboshi, F. Obata, R. Tachibana, S. Yasunaga, Y. Mita, Y. Misawa, R. Kojima, Y. Urano, M. Kamiya, Y. Ozeki, Super-resolution vibrational imaging based on photoswitchable Raman probe. Sci. Adv. 9, eade9118 (2023).  
53. J. Ma, I. M. Pazos, W. Zhang, R. M. Culik, F. Gai, Site-specific infrared probes of proteins. Annu. Rev. Phys. Chem. 66, 357–377 (2015).  
54. L . Shi, X. Liu, L. Shi, H. T. Stinson, J. Rowlette, L. J. Kahl, C. R. Evans, C. Zheng, L. E. P. Dietrich, W. Min, Mid-infrared metabolic imaging with vibrational probes. Nat. Methods 17, 844–851 (2020).  
55. X. Liu, L. Shi, Z. Zhao, J. Shu, W. Min, VI BRANT : Spectral profiling for single-cell drug responses. Nat. Methods 21, 501–511 (2024).  
56. X. Gao, X. Li, W. Min, Absolute stimulated Raman cross sections of molecules. J. Phys. Chem. Lett. 14, 5701–5708 (2023).  
57. S. Ramos, J. C. Lee, Water bend-libration as a cellular Raman imaging probe of hydration. Proc. Natl. Acad. Sci. U.S.A. 120, e2313133120 (2023).  
58. J. Yin, L. Lan, Y. Zhang, H. Ni, Y. Tan, M. Zhang, Y. Bai, J. X. Cheng, Nanosecond-resolution photothermal dynamic imaging via MHZ digitization and match filtering. Nat. Commun. 12, 7097 (2021).  
59. P. D. Samolis, X. Zhu, M. Y. Sander, Time-resolved mid-infrared photothermal microscopy for imaging water-embedded axon bundles. Anal. Chem. 95, 16514–16521 (2023).  
60. L . Z. Osherovich, B. S. Cox, M. F. Tuite, J. S. Weissman, Dissection and design of yeast prions. PLOS Biol. 2, E86 (2004).  
61. S. H. Liyanage, N. G. H. Raviranga, J. G. Ryan, S. S. Shell, O. Ramstrom, R. Kalscheuer, M. Yan, Azide-masked fluorescence turn-on probe for imaging mycobacteria. JACS Au 3, 1017–1028 (2023).  
62. H . He, J. Yin, M. Li, C. V. P. Dessai, M. Yi, X. Teng, M. Zhang, Y. Li, Z. Du, B. Xu, J. X. Cheng, Mapping enzyme activity in living systems by real-time mid-infrared photothermal imaging of nitrile chameleons. Nat. Methods 21, 342–352 (2024).  
63. K. Dabov, A. Foi, V. Katkovnik, K. Egiazarian, Image denoising by sparse 3-­D transformdomain collaborative filtering. IEEE Trans. Image Process. 16, 2080–2095 (2007).  
64. M. Maggioni, G. Boracchi, A. Foi, K. Egiazarian, Video denoising, deblocking, and enhancement through separable 4-­D nonlocal spatiotemporal transforms. IEEE Trans. Image Process. 21, 3952–3966 (2012).  
65. E . Kim, H. Koo, Biomedical applications of copper-free click chemistry: In vitro, in vivo, and ex vivo. Chem. Sci. 10, 7835–7851 (2019).  
66. D . Fu, G. Holtom, C. Freudiger, X. Zhang, X. S. Xie, Hyperspectral imaging with stimulated Raman scattering by chirped femtosecond lasers. J. Phys. Chem. B 117, 4634–4640 (2013).  
67. A. D. Becke, Density-functional thermochemistry. III . The role of exact exchange. J. Chem. Phys. 98, 5648–5652 (1993).  
68. C . Lee, W. Yang, R. G. Parr, Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density. Phys. Rev. B Condens Matter 37, 785–789 (1988).  
69. R. Krishnan, J. S. Binkley, R. Seeger, J. A. Pople, Self-consistent molecular orbital methods. XX. A basis set for correlated wave functions. J. Chem. Phys. 72, 650–654 (1980).  
70. M. D. Hanwell, D. E. Curtis, D. C. Lonie, T. Vandermeersch, E. Zurek, G. R. Hutchison, Avogadro: An advanced semantic chemical editor, visualization, and analysis platform. J. Cheminform. 4, 17 (2012).

Acknowledgments: We thank G. Chiesa for providing the yeast strain. We thank M. Zhang for helpful discussions on the bacteria culture and J. Ao for helpful discussions on the manuscript and SRS imaging. Funding: This research was supported by NIH grants R35GM136223, R01AI141439, and R33CA261726 to J.-X.C. Author contributions: Q.X., M.Y., and J.-X.C. conceived the concept and designed the experiments. Q.X. performed the experiments and analyzed the data. R.B. cultured the HeLa cell and performed the cell treatment. H.A.P. synthesized TreAz and helped with M. smeg culture. J.Y. developed the counter-propagating scanning MIP system. Z.G. helped with the scanning fluorescence imaging system. M.L. helped with the co-propagating scanning MIP system. Z.G., J.Y., and X.G. coded the program for data acquisition. H.H. helped with the confocal fluorescence imaging. Z.A.P. and Q.C. did the calculation of IR cross section. X.G. performed the SRS imaging. O.R. intellectually contributed to the experiment design. Q.X. and J.-X.C. cowrote the manuscript. All authors have read and approved the manuscript. Competing interests: J.-X.C. declares interests with Photothermal Spectroscopy Corp., which did not support this study. The other authors declare that they have no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Raw data are available in Zenodo (DOI: 10.5281/zenodo.12638627).

Submitted 23 April 2024

Accepted 16 July 2024

Published 21 August 2024

10.1126/sciadv.adq0294

# ScienceAdvances

## Click-free imaging of carbohydrate trafficking in live cells using an azido photothermal probe

Qing Xia, Harini A. Perera, Rylie Bolarinho, Zeke A. Piskulich, Zhongyue Guo, Jiaze Yin, Hongjian He, Mingsheng Li, Xiaowei Ge, Qiang Cui, Olof Ramström, Mingdi Yan, and Ji-Xin Cheng

Sci. Adv. 10 (34), eadq0294. DOI: 10.1126/sciadv.adq0294

View the article online

https://www.science.org/doi/10.1126/sciadv.adq0294

Permissions

https://www.science.org/help/reprints-and-permissions

Use of this article is subject to the Terms of service