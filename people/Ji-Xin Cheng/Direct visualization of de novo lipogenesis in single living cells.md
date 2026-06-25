## OPEN

SUBJECT AREAS: IMAGING AND SENSING MOLECULAR IMAGING CANCER METABOLISM

Received 25 July 2014 Accepted 8 October 2014 Published 29 October 2014

Correspondence and requests for materials should be addressed to J.-X.C. (jcheng@ purdue.edu)

# Direct Visualization of De novo Lipogenesis in Single Living Cells

Junjie Li1,2 & Ji-Xin Cheng1,3

1 Weldon School of Biomedical Engineering, Purdue University, West Lafayette, IN 47907, 2 Department of Biological Sciences, Purdue University, West Lafayette, IN 47907, 3 Center for Cancer Research, Purdue University, West Lafayette, IN 47907.

Increased lipogenesis is being increasingly recognized as a hallmark of cancer. Despite recent advances in fluorescence microscopy, autoradiography and mass spectrometry, direct observation of lipogenesis in living systems remains to be challenging. Here, by coupling stimulated Raman scattering (SRS) microscopy with isotope labeled glucose, we were able to trace the dynamic metabolism of glucose in single living cells with high spatial-temporal resolution. As the first direct visualization, we observed that glucose was largely utilized for lipid synthesis in pancreatic cancer cells, which occurs at a much lower rate in immortalized normal pancreatic epithelial cells. By inhibition of glycolysis and fatty acid synthase (FAS), the key enzyme for fatty acid synthesis, we confirmed the deuterium labeled lipids in cancer cells were from lipid synthesis. Interestingly, we also found that prostate cancer cells exhibit relatively lower level of lipogenesis, but higher fatty acid uptake compared to pancreatic cancer cells. Together, our results demonstrate a valuable tool to study dynamic lipid metabolism in cancer and other disorders.

R eprogramming of metabolism in cancers has been known since 1920s1 . Given Otto Warburg’s observation,aerobic glycolysis once was considered as the most prominent change of cancer metabolism. Based on aerobic glycolysis once was considered as the most prominent change of cancer metabolism. Based on advances in cancer metabolism research in the past decades, current concept of cancer metabolism holds that in addition to aerobic glycolysis, cancer cells also reprogram their mitochondria to satisfy the need for macromolecular synthesis, instead of maximizing the efficiency of ATP production2 . One evidence of the repro grammed mitochondrial metabolism is the increased lipogenesis that has been observed in many cancers.

In mammalian cells, glucose is utilized as the most important energy source and provides precursors for de novo synthesis of other macromolecules, like lipids. After glycolysis, pyruvate is produced from glucose and then enters mitochondria. Through the tricarboxylic acid cycle (TCA), pyruvate is converted to acetyl-CoA and exported to cytosol. Acetyl-CoA in the cytosol is used as precursors for lipid synthesis via the de novo lipogenesis pathway. Newly synthesized fatty acids are further esterified and stored in lipid droplets (LDs). On the other hand, fatty acids from lysed triglyceride or directly uptake can also be stored in lipids droplets (Fig. 1a)3,4. Compared to fatty acid uptake, de novo lipogenesis seems to play a more important role in many cancers. Overexpression of lipogenic enzymes, including ATP citrate lyase (ACL)5 , fatty acid synthase (FAS)6 and stearoyl-CoA desaturase (SCD)7 has been widely reported in many types of cancers. More recent studies showed that under hypoxia condition or in cells with defected mitochondria, glutamine, instead of glucose, mediated lipogenesis becomes more important for tumor growth8,9. These findings provides valuable insights to the complexity of cancer metabolism. However, it also raised a need to study metabolism in a temporal and spatial resolved manner, especially considering the varieties of microenvironments in vivo.

To monitor glucose metabolism, several glucose analogs have been synthesized to mimic the behavior of glucose, e.g., 3-O-methylglucose (3MG), 2-deoxy-D-glucose (2-DG) and fluoro-deoxyglucose (FDG)10. Fluorescent labeled glucose analog, 2-[N-(7-nitrobenz-2-oxa-1,3-diazol-4-yl)amino]-2-deoxy-D-glucose (2- NBDG), has been used to study the glucose uptake11,12. Isotope labeled glucose analog, 18F-deoxyglucose (FDG), has been successfully used in clinic to image to tumors in vivo by positron emission tomography (PET)13,14. However, these analogs are nonmetabolizable and can only be used to study the glucose uptake. Recently, mass spectrometry has been used combined with isotope labeling to study the dynamic process8,9,15,16 Although mass spectrometry has high species resolution, it doesn’t offer the temporal-spatial resolution to monitor glucose metabolism in single live cells.

Here, we report direct imaging of de novo lipid synthesis in single living cells using stimulated Raman scattering (SRS) microscopy that allows real-time vibrational imaging of live cells17–19. Earlier, SRS imaging of C–D vibration has been demonstrated to be successful in imaging the incorporation of isotope labeled amino acid into proteins20, map drug delivery into skin21,22 and intracellular fate of fatty acids23. More recent advances in coupling small vibration alkyne tags with SRS microscopy opens new opportunities for biological imaging with superb sensitivity24,25. In this work, we employed SRS microscopy to visualize metabolic reprograming of deuterium-labeled glucose in individual living cells with deuteriumlabeled glucose. Unlike the fluorescent analogs or FDG, deuterium substitution does not vary the structure of glucose, nor its physiological functions. With high spatial-temporal resolution of SRS microscopy, we monitored the dynamic metabolism of glucose in single living cancer cells. As the first direct visualization, we observed that deuterium labeled glucose was largely utilized for lipid synthesis in cancer cells, which occurs at a much lower rate in normal immor talized epithelial cells. This method of imaging dynamic metabolism in single living cells could be a valuable tool for elucidating the complexity of the metabolic network and exploring new therapeutic targets for cancer.

a  
![](images/5520a896d5173e596f00fd6c90cc2df4c9b8c8d4020ad85a763502b89218525e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Glucose-d7"] --> B["Glyceraldehyde-3-P"]
  B --> C["Pyruvate"]
  C --> D["Acetyl-CoA"]
  D --> E["TCA cycle"]
  E --> F["Citrate"]
  F --> G["Acetyl-CoA"]
  G --> H["Cholesterol"]
  I["Lipid droplets"] --> J["Triacylglyceride"]
  J --> K["Fatty acids"]
  K --> L["Phospholipids"]
  M["Dietary lipids"] --> N["Essential fatty acids"]
  N --> O["Triacylglyceride"]
  P["FASN"] --> Q["Malonyl-CoA"]
  Q --> R["Acetyl-CoA"]
  R --> S["Cholesterol"]
  T["Lactate"] --> C
```
</details>

b  
![](images/f09562113e8693e8ce6f95c3b9ad4f3013884ce1947ab964fbef52350870b511.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 500                | ~1000            |
| 1000               | ~1400            |
| 1500               | ~100             |
| 2000               | ~2000            |
| 2500               | ~100             |
| 3000               | ~100             |
</details>

c  
![](images/198dfe807bde312cea6828b0197b1ef0e49f936259214ca7428c23e753d65aa1.jpg)

<details>
<summary>scatterplot</summary>

| Concentration (M) | ΔI/I (×10⁵) |
| ----------------- | ----------- |
| 0.0               | 0.0         |
| 0.5               | 1.0         |
| 1.0               | 2.0         |
| 2.0               | 4.5         |
</details>

Figure 1 Isotope labeled glucose-d is a tracer for de-novo lipogenesis. (a). Scheme of glucose-derived de-novo lipid synthesis in mammalian cells. (b). Raman spectrum of 1.0 M glucose-d aqueous solution. A broad and unique peak around 2120 cm21 from C–D bond vibration was observed. Inset: chemical structure of glucose-d . (c). Linear dependence of SRS signal on glucose-d concentration. The detection limit of our SRS imaging is around 50 mM. Inset: SRS image of 1.0 M glucose-d solution at the interface of solution and air.

## Results

Imaging de novo lipogenesis in living cells. In order to visualize lipogenesis in living cells, we use a deuterium labeled glucose-d where the hydrogen atoms are replaced with deuterium atoms (Fig. 1b inset). Raman spectrum taken from a 1.0 M glucose-d aqueous solution showed a peak centered at ${ \sim } 2 1 2 0 ~ \mathrm { c m } ^ { - 1 }$ from the

C–D bond vibration modes (Fig. 1b). This peak resides in the silent region of the Raman spectrum of endogenous molecules, which provides excellent opportunities for SRS imaging of target molecules. By tuning the wavenumber difference between the pump and Stokes beams $( \omega _ { \mathrm { p } } \mathrm { ~ - ~ } \omega _ { \mathrm { S } } )$ to match the C–D vibration at 2120 cm21 , SRS imaging of glucose- $\mathbf { \cdot d } _ { 7 }$ solution shows a linear dependence of SRS signal on glucose-d concentration (Fig. 1c), with a detection sensitivity of 50 mM in water.

To study glucose metabolism inside living cells, we replaced glu cose in the normal cell culture medium to deuterium labeled glucose by adding glucose-d to glucose-free DMEM medium to same concentration (25 mM). PANC1 cells, a pancreatic cancer cell line, were incubated in the medium for 3 days and imaged by SRS microscopy. By matching ${ \mathfrak { o } } _ { \mathrm { p } } - { \mathfrak { o } } _ { \mathrm { s } }$ to the C–D bond vibration at 2120 cm21 , a strong SRS signal was observed in LDs (Fig. 2a, left), which are confirmed by SRS image of lipids at 2850 cm21 (Fig. 2a, right). A video of the de novo synthesized lipids showed intracellular trafficking of the LDs (supplementary movie). By tuning $( { \mathfrak { O } } _ { \mathsf { p } } \ - \ { \mathfrak { o } } _ { \mathsf { S } } )$ to $2 6 0 0 ~ \mathrm { { c m } ^ { - 1 } }$ , the off-resonant images showed some weak background (Fig. 2a, middle), which is known to result from cross-phase modulation26. As a control, no C–D labeled droplets were detected in the cells cultured with regular high-glucose DMEM medium (Fig. 2b).

![](images/40c715f24e32e761616b85c9d6e1b3bdbb664f6e0b457fb87cd1a9147c3bf9db.jpg)

C  
![](images/2d51e57829929e5f89a6f0cb2b467696777f777c177e986d4bd7debf986fde79.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | LD in control cell | LD in treated cell |
| ------------------ | ------------------ | ------------------ |
| 500                | ~3000              | ~1000              |
| 1000               | ~3500              | ~1500              |
| 1500               | ~5500              | ~2500              |
| 2000               | ~2500              | ~1500              |
| 2500               | ~2500              | ~1000              |
| 3000               | ~7000              | ~4000              |
</details>

d  
![](images/cb3cc1f5ed3841b0201ab469e4cc2337ab5161e88d0e2503ece69257746c08b7.jpg)

<details>
<summary>bar chart</summary>

| Days | Glucose | Glucose-d7 |
|---|---|---|
| 0 | 1.0 | 1.0 |
| 1 | 2.0 | 1.6 |
| 2 | 3.5 | 3.5 |
| 3 | 5.0 | 5.0 |
</details>

Figure 2 | Glucose- $\mathbf { \nabla } \cdot \mathbf { d } _ { 7 }$ is utilized for lipid synthesis in pancreatic cancer PANC1 cells. PANC1 cells were incubated with (a). 25 mM glucose-d or (b). 25 mM glucose in glucose-free DMEM media supplemented with 10% FBS for 3 days. SRS imaging was taken at C–D vibration (,2120 cm $^ { - 1 } ) _ { : }$ , offresonance $( \sim 2 6 0 0 ~ \mathrm { c m } ^ { - 1 } )$ ) or C–H vibration $( \sim 2 8 5 0 ~ \mathrm { c m } ^ { - 1 } )$ . (c). Raman spectra acquired from lipid droplets in control cells or glucose-d treated cells. (d). Nontoxicity test of glucose-d compared to regular glucose. Cell viability was determined by MTT assay. Data was represented as Mean 1 SD with n 5 6 for each group.

Raman spectra taken from the LDs in cells further confirmed the presence of C–D bonds in the cell treated with glucose-d , but not in the control cells (Fig. 2c). Collectively, our images and Raman spectra demonstrated that glucose was utilized in pancreatic cancer cells for lipogenesis and excess newly synthesized lipids were stored in LDs. Furthermore, the viability test showed that glucose-d shows no toxicity to the cells (Fig. 2d). Thus, isotope stably labeled glucose could be used as a tracer to visualize de novo lipogenesis in living cancer cells.

Dynamics of lipogenesis in living cells. The noninvasive property of SRS microscopy enabled us to monitor the dynamic lipogenesis process within the same plate of cells over time. Figure 3a–b showed that the level of de novo synthesized lipids kept increasing from 2 to 72 h and then maintained at a steady level after 3-day incubation. The donut shaped LDs were observed (Fig. 3a, inset of 72 h), indicating the newly synthesized lipids deposited at the outer layer of existing LDs. Longer incubation did not further increase the storage of newly synthesized lipids, indicating that lipid storage and lipolysis reached a balanced status after 3 days. To further confirm the deuterium labeled lipids are derived from glucose metabolism pathway, we used an inhibitor of glycolysis, 2-Deoxy-D-glucose (2-

DG). With inhibition of glycolysis, we observed reduced number of deuterium labeled LDs (Fig. 3c). Furthermore, to validate the newly synthesized lipids are from de novo lipogenesis pathway but not dietary lipids, an inhibitor of fatty acid synthase (FAS), C75, was applied to PANC1 cells. As a result, C75 dramatically reduced the number and intensity of newly synthesized LDs (Fig. 3d). The effect of C75 was further confirmed by knock-down of FAS in PANC1 cells with shRNA (Fig. 3e). Collectively, we verified that the deuterium labeled lipids were derived from glucose metabolism and synthesized through de novo lipogenesis pathway. In addition to glucose, glutamine plays as another important precursor for lipogenesis in cancer cells especially under certain conditions (e.g., hypoxia or defected mitochondria)8,9. To demonstrate the capability our method for broad applications, we also imaged deuterium labeled glutamine derived lipogenesis. As we expected, in normal culture condition PANC1 cells mainly rely on glucose as nutrition source for de novo lipogenesis, with negligible contribution from glutamine (Fig. S1).

Increased lipogenesis in pancreatic cancer cells compared to normal epithelial cells. Increased lipogenesis is being accepted as an important player in cancer metabolism. Here, with glucose-d

![](images/24b77d8630e05c260bf8bc277fe0def37082ee4bdc7b96b6fad8158189d44ce6.jpg)

<details>
<summary>text_image</summary>

a
2 h
20 h
48 h
72 h
96 h
C-D
C-H
10 µm
</details>

![](images/06390c25573d5ac484a6a86c8a27819935598b001b15cedfe0ea78a4c1328c8d.jpg)

<details>
<summary>line chart</summary>

| Incubation time (h) | Aera fraction (%) |
|---|---|
| 2 | 0.0 |
| 20 | 0.1 |
| 48 | 0.45 |
| 72 | 1.4 |
| 96 | 1.45 |
</details>

![](images/bd214018d4e3dd6036f188e859c1531e337beb14a097556f402b060021fa274e.jpg)

<details>
<summary>text_image</summary>

C
Control
10 mM 2-DG
C-D
C-H
10 µm
</details>

![](images/c7d12eed637de489a422ea5550e445189dcc1d9fa45d97236c1c6f069d02d5a4.jpg)

<details>
<summary>text_image</summary>

d
DMSO 20 µM C75
C-D
C-H
10 µm
</details>

![](images/08cb563cefdf518d8af772b9a9b1d1d3cab008cb4a546c4ddd620cf5bbd4fa43.jpg)

<details>
<summary>text_image</summary>

e
Control
FAS shRNA
C-D
C-H
10 µm
</details>

Figure 3 | Dynamics of glucose-d7 derived lipogenesis in PANC1 cells. (a). Monitoring de-novo lipogenesis in PANC1 cells over time by SRS imaging at C–D and C–H vibration. Inset of image at 72 h: zoom in image of marked area showing the donut-shaped newly synthesized LDs. (b). Quantification of SRS signal at C–D vibration per cell. Data were shown as Mean 6 SD. N 5 5 for each group. (c). SRS imaging of PANC1 cells incubated with 10 mM 2-DG and 25 mM glucose-d7 for 3 days. (d). SRS imaging of PANC1 cells incubated with glucose-d7 for 3 days and treated with DMSO or 20 mM FAS inhibitor C75 for 24 hours. (e). SRS imaging of PANC1 cells stably transfected with FAS shRNA and incubated with glucose-d for 3 days.

incubation, we compared the level of de novo lipogenesis in normal HPDE6 cell line (Fig. 4a) and two pancreatic cancer cell lines, PANC1 (Fig. 4b) and MIA PaCa2 (Fig. S2a). Generally, mammalian cells can acquire lipids from two sources, de novo lipogenesis or uptake from diet4 . To evaluate the contribution of de novo lipogenesis and dietary uptake in normal and cancer cells, we incubated the cells with 25 mM gluose-d in glucose-free medium supplemented with or without 10% FBS for 3 davs. The results (Fig. 4, S2) showed that without serum supplementation, both normal and cancerous cells utilize de novo lipogenesis and store the excess lipids in LDs. However, when the serum is supple mented, normal cells uptake exogenous lipids instead of employ de novo synthesis (Fig. 4a), whereas the pancreatic cancer cells use de novo synthesis regardless the presence of exogenous lipids (Fig. 4c, S2a). Based on the ratio of C–D signal over C–H signal, we showed that at presence of exogenous lipids, the de novo lipogenesis level in pancreatic cancer PANC1 $( 0 . 6 6 5 \pm 0 . 0 4 2 )$ and MIA PaCa2 cells $( 0 . 6 2 3 ~ \pm ~ 0 . 0 2 6 )$ is 2,3 folds higher than that in HPDE6 cells $( 0 . 2 4 9 \pm 0 . 0 8 7 )$ (Fig. 4b, 4d and Fig. S2b). Together, these results suggested the lipogenic pathway has been reprogrammed in pancreatic cancer cells compared to normal epithelial cells, which provides visual evidence for the previously reported up-regulation of de novo lipogenesis pathway in pancreatic cancer cells27,28.

Lipogenesis in prostate cancer. Though increased lipogenesis is accepted as a hallmark for cancers29, our live cell imaging study revealed that different cancer types might use distinct lipogenic pathways. With glucose- ${ \bf { \cdot } } { \bf { d } } _ { 7 }$ and SRS imaging, we measured the lipogenesis in multiple types of cancer cells, including breast cancer MCF7, lung cancer A549, prostate cancer PC3 and pancreatic cancer PANC1 (Fig. S3a). Interestingly, we found that PC3 cells have lower level of de novo lipogenesis compared to other types of cancers (Fig. S3b), although the PC3 cells contained large amount of LDs. Considering PC3 is an androgen independent prostate cancer cell line30, to fully unveil the lipogenic profiles in prostate cancer we included normal epithelial RWPE1 cell, androgen dependent LNCaP and androgen independent PC3 cancer cell. Firstly, glucose-d7 was applied to prostate cells supplemented with 10% FBS. Our results showed that both LNCaP and PC3 cells exhibited elevated level of de novo lipogenesis than RWPE1 cells (Fig. 5a). The ratio of C–D signal to C–H signal is $0 . 3 3 6 \pm \ : 0 . 0 7 0$ for LNCaP and $0 . 3 2 0 \pm 0 . 0 7 8$ for PC3 cell. Although they are much higher than RWPE1 $( 0 . 1 7 1 ~ \pm ~ 0 . 0 6 2 )$ cells, they are lower than pancreatic cancer PANC1 and MIA PaCa-2 cell (Fig. 5b, 4d and Fig. S2b). Furthermore, to investigate whether the fatty acid uptake contribute to the lipid accumulation in PC3 cells, deuterium labeled palmitic $\mathrm { \ a c i d - d } _ { 3 1 }$ was used. Similarly, cells were incubated with palmitic $\mathrm { a c i d - d } _ { 3 1 }$ for 24 hours and imaged at C–D vibration to visualize the deuterium labeled LDs derived from exogenous palmitic acid- $\mathbf { \nabla } \cdot \mathbf { d } _ { 3 1 } .$ . The results showed that under same condition, both RWPE1 and LNCaP cells uptake high level of free fatty acids (Fig. 5c). However, pancreatic cancer PANC1 cells have much reduced level of fatty acid uptake compared to normal HPDE6 cells (Fig. 5d). All together, these data suggest that prostate cancer cells, though with increased de novo lipogenesis, still remain the capability for high level of fatty acid uptake.

![](images/21ba3a4bb1fe01a4cc5a28355a18bd7733068506a42f323e38acc4f88013ff6d.jpg)

b  
![](images/4baf2f3c021d545f3fcf2d6eb90f14db810552f86caafedfdd0ec8a3df8796a2.jpg)

<details>
<summary>bar chart</summary>

| Group        | Ratio of C-D / C-H |
| ------------ | ------------------ |
| Glu-d7       | 0.78               |
| Glu-d7 + FBS | 0.25               |
</details>

![](images/6c0baf212a55825dd17ca3b471918af0ecd2976f2512aee5bcdef9eeb8cfbfff.jpg)

d  
![](images/aef6dbff5567c237702c3b87a74b278448e2bd53c9e496bbf065dbc28e58d6f7.jpg)

<details>
<summary>bar chart</summary>

| Group | Ratio of C-D / C-H |
|---|---|
| Glu-d7 | 0.7 |
| Glu-d7 + FBS | 0.65 |
</details>

Figure 4 | Increased lipogenesis in pancreatic cancer cells than normal pancreatic cells. (a). Normal immortalized pancreatic epithelial HPDE6 cells, and (c). pancreatic cancer PANC1 cells were treated with 25 mM glucose-d in glucose-free DMEM media supplemented without or with 10% FBS for 3 days. SRS imaging at C–D and C–H vibration were taken. The ratio of C–D/C–H was used to analyze the level of de-novo lipogenesis. Quantitative analysis of de-novo lipogenesis level in (b). HPDE6 and (d). PANC1 cells. The ratio of C–D signal to C–H signal intensity on single lipid droplets was measured. At least 10 lipid droplets were analyzed for each sample. The data was represented by Mean 1 SD. \*\*\* indicates p , 0.001 by student T test.

## Discussion

Visualizing metabolism in single living cells has been challenging due to the technical difficulties. By using deuterium labeled glucose and fatty acids, we have demonstrated the capability of SRS microscopy in imaging metabolic processes in temporal and spatial resolved manner. This method is well complementary to current techniques, like mass spectrometry or NMR spectroscopy. High spatial resolution, instead of ensemble measurement, is important for study of dynamic and complex metabolic networks. Currently, cancer heterogeneity in genetic aspect has been well accepted. However, heterogeneity in metabolism has not been well studied. Whether the variety in genetic mutations drives the metabolic heterogeneity or the diversity in metabolism affect the cancer heterogeneity remains an open question31,32. Our method would offer an avenue to address this question by imaging the metabolism in living cells or live tissues in situ. Another important question that can be pursued by our tech nology is whether there is a difference between cancer stem cell, progenitor cells, and regular cancer cells regarding to the metabolism aspect33,34. In general, the ability to visualize metabolism in single living cells would potentially be important to understanding cancer heterogeneity.

Besides imaging lipogenesis process, our method can potentially be used broadly on other aspects of metabolism. Isotope labeling is an ideal tracer for metabolism, especially for small molecules, because the labeling generally does not interfere their normal functions. Recently, isotope labeled amino acids have been demonstrated to monitor newly synthesized proteins20 and proteome degradation35.

to  
![](images/780a57f46da82e4886fbe89e14e59b40a0bf76c076b17e7cf50060ef76578738.jpg)

<details>
<summary>text_image</summary>

RWPE1
LNCaP
PC3
C-D
C-H
10 µm
</details>

b  
![](images/aeb1c51f4833322af65c40fc8669d9c7901cd683849efb594b2c374aa87c2e30.jpg)

<details>
<summary>bar chart</summary>

| Group  | Ratio of C-D/C-H |
| ------ | ---------------- |
| RWPE1  | 0.17             |
| LNCaP  | 0.33             |
| PC3    | 0.32             |
</details>

O  
![](images/2e2794e827d568b9430945c6651e196c92165c06dc6c5e095e89d3a01877b0a3.jpg)

<details>
<summary>text_image</summary>

C
RWPE1
LNCaP
C-D
C-H
10 µm
</details>

d  
![](images/752865d9d336070db2a2775c3503bc7cecda66e3741aa167c7342e6e66ca0576.jpg)

<details>
<summary>text_image</summary>

HDPE6
PANC1
C-D
C-H
10 µm
</details>

Figure 5 | Lipogenesis and fatty acid uptake in prostate and pancreatic cells. (a). Glucose-d derived lipogenesis were measured in prostate cell lines, including normal epithelial RWPE1 cell and cancerous LNCaP, PC3 cells by SRS imaging at C–D and C–H vibration. (b). Quantitative analysis of de-novo lipogenesis level in prostate cell lines. Data were shown as mean 1 SD. N \$ 10 for each group. \*\*\* indicates $\mathrm { p } < 0 . 0 0 1$ by student T test. (c). SRS imaging of prostate cells and (d). pancreatic cells treated with 100 mM palmitic acid-d for 24 hours.

Choline and its metabolites in living systems have been imaged by SRS with deuterium labeled choline36. In addition, isotope labeling could also be applied to small molecules, like drugs. Currently, drug metabolism in single cell level is still not fully understood. A recent paper demonstrates SRS imaging resolves the distribution of anticancer drugs in living cells37. To trace the fate of isotope labeled drugs in single cells with subcellular resolution will be important to under stand its metabolic pathway and further improve the efficiency of drug delivery.

In this work, we showed that compared to pancreatic cancer cells, prostate cancer cells exhibit lower level of de novo lipogenesis but higher level of fatty acid uptake. Our observation is consistent with previous report of dominant fatty acid uptake over glucose uptake in prostate cells38. The difference of lipogenic preference of prostate cancer may be related to its special metabolic demands. It has been reported that prostate cancer relies more on b-oxidation pathway as an energy source39. Increased b-oxidation process may require higher and faster demands of free fatty acids, which cannot be easily achieved by de novo lipogenesis. Our observation could be a result of this altered fatty acid metabolism pathway in prostate cancer. However, we are also aware of that different cell line model may have distinct metabolic profiles40. Further investigations are needed to fully understand the complexity of metabolic networks. Our imaging method could be a powerful tool to reveal the metabolic differences between different cell models in the future studies.

More applications of our method rely on further improvement of imaging sensitivity. Due to limited sensitivity at mM level, we could not detect other metabolites of glucose except lipids. Higher sensitivity would allow mapping the metabolic transformation by using glucose as precursor for other macromolecular synthesis, such as nucleotides and proteins. The other way to enhance the capability of this technique is to perform hyperspectral imaging instead of single-frequency imaging. As isotope-labeled molecules are converted to other metabolites, the vibration frequency of the C–D bond may shift due to environment change. Hyperspectral imaging would allow us to separate different metabolic species based on the spectral differences41. With higher detection sensitivity or spectral acquisition capability, SRS imaging would be fully appreciated for single cell metabolism study.

## Methods

SRS microscopy and Raman spectroscopy. SRS microscopy was performed with two femto-second laser system, as described previously23. Specifically, a Ti:Sapphire laser (Chameleon Vision, Coherent) with up to 4 W (80 MHz, ,140 fs pulse width) pumps an optical parametric oscillator (OPO, Chameleon Compact, Angewandte Physik & Elektronik GmbH). The pump and Stokes beams were tuned to 830 nm and 1004 nm, respectively, to be in resonance with the C–D vibration at 2120 cm21 . For imaging at C–H vibration, pump and Stokes beams were tuned to 830 nm and 1090 nm, respectively. The pump and Stokes pulse trains were collinearly overlapped and directed into a laser-scanning microscope (FV300, Olympus). A 60X waterimmersion objective lens (UPlanSApo, Olympus) was used to focus the laser into a sample. An oil condenser of 1.4 numerical aperture (NA) was used to collect the signal in a forward direction. The typical acquisition time for a 512 3 512 pixels SRL image was 1.12 second. Because most excitation power was carried by the Stokes beam at 1090 nm, with the pump beam power being as low as a few mW at the sample, photodamage to cells was not detected.

For spontaneous Raman spectroscopy, a 5-ps Ti:sapphire laser (Tsunami, Spectra Physics, Mountain View, CA) tuned to ,707 nm was used42. Each Raman spectrum was acquired in 20 seconds, and pump laser power at the specimen was maintained at 15 mW.

Chemicals and Reagents. Glucose-d , glutamine-d and palmitic acid-d were purchased from Cambridge Isotope Laboratories, Inc. Fatty acid synthase (FAS) inhibitor C75 was purchased from Cayman Chemical. 2-deoxy-D-glucose (2-DG) was purchased from Sigma (Cat# D8375). High glucose (4.5 g/ml), glucose free and glucose, glutamine free DMEM medium, RPMI 1640, Keratinocyte Serum Free Medium (K-SFM) with additives bovine pituitary extract (BPE) and human recombinant epidermal growth factor (rEGF) were purchased from Invitrogen Life Technologies. F-12K medium was purchased from ATCC. Fetal bovine serum (FBS) was purchased from Sigma.

Cell culture and imaging. All cells were cultured in 37uC moisture incubator with 5% CO supply. The following media were used for maintenance: DMEM high glucose medium supplemented with 10% FBS was used for PANC1 and A549 cell; RPMI 1640 supplemented with 10% FBS was used for MIA PaCa2, MCF7 and LNCaP cell; F-12K supplemented with 10% FBS was used for PC3 cell; K-SFM supplemented with 30 mg/ ml BPE and 0.2 ng/ml rEGF was used for HPDE6 and RWPE1 cell. For SRS imaging of glucose-d , around 0.3 M cells were seeded on glass-bottom dishes (In Vitro Scientific, Cat# D35-10-1.5-N) with 25 mM glucose-d in glucose-free DMEM media supplemented with or without 10% FBS. For the study of glutamine metabolism, the cells were incubated with 25 mM glucose-d and 4 mM glutamine-d in glucose, glutamine-free DMEM media supplemented with 10% FBS for 3 days. For the fatty acid uptake study, cells were incubated with 100 mM palmitic acid-d in DMEM high glucose media without 10% FBS for 24 hours. For cell dynamic study, living cells were used. For quantitative studies, cells were fixed in 10% neutral buffered formalin for 30 min.

Transfection of FAS shRNA. FAS shRNA plasmid was purchased from Santa Cruz (Cat# sc-29311-SH). Transfection of shRNA plasmid to PANC1 cells was performed using LipofectamineH 2000 (Invitrogen, Cat# 11668-019) by following the manufacturer’s protocol. Stable transfected colony was selected under 2 mg/ml puromycin for 10 days.

Cell toxicity test. Cells were seeded in 96-well plates (,5000 cells/well) and grown overnight. Then the medium was replaced with 25 mM glucose or glucose-d7 in glucose-free DMEM media supplemented with 10% FBS for 1,3 days. Cell viability was measured with the MTT colorimetric assay (Sigma) every day after treatment.

Data analysis. Quantification of LDs was analyzed with ImageJ software particle analysis function. Area fraction was used to present the amount of LDs in a single cell. For analysis of the C–D/C–H ratio, threshold was firstly applied to the C–D image to pick up the LDs. Then the ratio was obtained by dividing C–D images over C–H images. Statistical analysis was done with the C–D/C–H ratio of single LD.

1. Koppenol, W. H., Bounds, P. L. & Dang, C. V. Otto Warburg’s contributions to current concepts of cancer metabolism. Nat. Rev. Cancer 11, 325–337 (2011).  
2. Ward,Patrick, S. & Thompson,Craig, B. Metabolic Reprogramming: A Cancer Hallmark Even Warburg Did Not Anticipate. Cancer Cell 21, 297–308 (2012).  
3. Walther, T. C. & Farese, R. V., Jr. Lipid droplets and cellular lipid metabolism. Annu. Rey. Biochem. 81, 687714 (2012).  
4. Santos, C. R. & Schulze, A. Lipid metabolism in cancer. FEBS J. 279, 2610–2623 (2012).  
5. Zaidi, N., Swinnen, J. V. & Smans, K. ATP-Citrate Lyase: A Key Player in Cancer Metabolism. Cancer Res. 72, 37093714 (2012).  
6. Menendez, J. A. & Lupu, R. Fatty acid synthase and the lipogenic phenotype in cancer pathogenesis. Nat. Rev. Cancer 7, 763–777 (2007).  
7. Igal, R. A. Stearoyl-CoA desaturase-1: a novel key player in the mechanisms of cell proliferation, programmed cell death and transformation to cancer. Carcinogenesis 31, 1509–1515 (2010).  
8. Metallo, C. M. et al. Reductive glutamine metabolism by IDH1 mediates lipogenesis under hypoxia, Nature 481. 380384 (2011).  
9. Mullen, A. R. et al. Reductive carboxylation supports growth in tumour cells with defective mitochondria. Nature 481, 385–388 (2011).  
10. Yamamoto, N. et al. Measurement of glucose uptake in cultured cells. Curr Protoc Pharmacol 12, 1–22 (2011).  
11. Yamada, K. et al. Measurement of glucose uptake and intracellular calcium concentration in single, living pancreatic beta-cells. J. Biol. Chem. 275, 22278–22283 (2000).  
12. Zou, C., Wang, Y. & Shen, Z. 2-NBDG as a fluorescent indicator for direct glucose uptake measurement. J. Biochem. Biophys. Methods 64, 207–215 (2005).  
13. Vander Heiden, M. G., Cantley, L. C. & Thompson, C. B. Understanding the Warburg Effect: The Metabolic Requirements of Cell Proliferation. Science 324, 1029–1033 (2009).  
14. Gatenby, R. A. & Gillies, R. J. Why do cancers have high aerobic glycolysis? Nat Rev. Cancer 4, 891–899 (2004).  
15. Metallo, C. M., Walther, J. L. & Stephanopoulos, G. Evaluation of 13C isotopic tracers for metabolic flux analysis in mammalian cells. J. Biotechnol. 144, 167174 (2009).  
16. Kamphorst, J. J. et al. Hypoxic and Ras-transformed cells support growth by scavenging unsaturated fatty acids from lysophospholipids. Proc. Natl. Acad. Sci. U.S.A. 110, 8882–8887 (2013).  
17. Saar, B. G. et al. Video-Rate Molecular Imaging in Vivo with Stimulated Raman Scattering. Science 330, 1368–1370 (2010).  
18. Freudiger, C. W. et al. Label-Free Biomedical Imaging with High Sensitivity by Stimulated Raman Scattering Microscopy. Science 322, 1857–1861 (2008).  
19. Stender, A. S. et al. Single Cell Optical Imaging and Spectroscopy. Chem. Rev. 113, 24692527 (2013).  
20. Wei, L., Yu, Y., Shen, Y., Wang, M. C. & Min, W. Vibrational imaging of newly synthesized proteins in live cells by stimulated Raman scattering microscopy. Proc. Natl. Acad. Sci. U.S.A. 110, 11226–11231 (2013).  
21. Drutis, D. M. et al. Three-dimensional chemical imaging of skin using stimulated Raman scattering microscopy. J Biomed Opt 19, 111604 (2014).  
22. Saar, B. G., Contreras-Rojas, L. R., Xie, X. S. & Guy, R. H. Imaging Drug Delivery to Skin with Stimulated Raman Scattering Microscopy. Mol. Pharm. 8, 969–975 (2011).  
23. Zhang, D., Slipchenko, M. N. & Cheng, J.-X. Highly Sensitive Vibrational Imaging by Femtosecond Pulse Stimulated Raman Loss. J Phys Chem Lett 2, 1248–1253 (2011).  
24. Wei, L. et al. Live-cell imaging of alkyne-tagged small biomolecules by stimulated Raman scattering. Nat. Methods 11, 410–412 (2014).  
25. Hong, S. et al. Live-Cell Stimulated Raman Scattering Imaging of Alkyne-Tagged Biomolecules. Angew. Chem. 126, 5937–5941 (2014).  
26. Zhang, D., Slipchenko, M. N., Leaird, D. E., Weiner, A. M. & Cheng, J.-X. Spectrally modulated stimulated Raman scattering imaging with an angle-to wavelength pulse shaper. Opt Express 21, 13864–13874 (2013).  
27. Kuhajda, F. P. et al. Fatty acid synthesis: a potential selective target for antineoplastic therapy. Proc. Natl. Acad. Sci. U.S.A. 91, 6379–6383 (1994).  
28. Currie, E., Schulze, A., Zechner, R., Walther, Tobias, C. & Farese, Jr, Robert, V. Cellular Fatty Acid Metabolism and Cancer. Cell Metab. 18, 153–161 (2013).  
29. Hanahan, D. & Weinberg, R. A. Hallmarks of Cancer: The Next Generation. Cell 144, 646–674 (2011).  
30. Yue, S. et al. Cholesteryl Ester Accumulation Induced by PTEN Loss and PI3K AKT Activation Underlies Human Prostate Cancer Aggressiveness. Cell Metab. 19, 393–406 (2014).  
31. Visvader, J. E. Cells of origin in cancer. Nature 469, 314–322 (2011).  
32. Shackleton, M., Quintana, E., Fearon, E. R. & Morrison, S. J. Heterogeneity in Cancer: Cancer Stem Cells versus Clonal Evolution. Cell 138, 822–829 (2009).  
33. McGraw, T. E. & Mittal, V. Stem cells: Metabolism regulates differentiation. Nat. Chem. Biol. 6, 176–177 (2010).  
34. Folmes, Clifford, D. L., Park, S. & Terzic, A. Lipid Metabolism Greases the Stem Cell Engine. Cell Metab. 17, 153–155 (2013).  
35. Shen, Y., Xu, F., Wei, L., Hu, F. & Min, W. Live-cell quantitative imaging of proteome degradation by stimulated Raman scattering. Angew. Chem. Int. Ed. Engl. 53, 5596–5599 (2014).  
36. Hu, F., Wei, L., Zheng, C., Shen, Y. & Min, W. Live-cell vibrational imaging of choline metabolites by stimulated Raman scattering coupled with isotope-based metabolic labeling. Analyst 139, 2312–2317 (2014).  
37. Fu, D. et al. Imaging the intracellular distribution of tyrosine kinase inhibitors in living cells with quantitative hyperspectral stimulated Raman scattering. Nat Chem 6, 614–622 (2014).  
38. Liu, Y., Zuckier, L. S. & Ghesani, N. V. Dominant uptake of fatty acid over glucose by prostate cells: a potential new diagnostic and therapeutic approach. Anticancer Res. 30, 369374 (2010).  
39. Liu, Y. Fatty acid oxidation is a dominant bioenergetic pathway in prostate cancer Prostate Cancer Prostatic Dis. 9, 230–234 (2006).  
40. Higgins, L. H. et al. Hypoxia and the metabolic phenotype of prostate cancer cells Biochim. Biophys. Acta 12, 12 (2009).  
41. Wang, P. et al. Label-Free Quantitative Imaging of Cholesterol in Intact Tissues by Hyperspectral Stimulated Raman Scattering Microscopy. Angew. Chem. Int. Ed. Engl. 52, 13042–13046 (2013).  
42. Slipchenko, M. N., Le, T. T., Chen, H. & Cheng, J.-X. High-Speed Vibrational Imaging and Spectral Analysis of Lipid Bodies by Compound Raman Microscopy. J Phys Chem B 113, 7681–7686 (2009).

## Acknowledgments

We thank Zhiyu Li and Chunrui Hu for their generous help on the cell toxicity study and technical support, respectively.

## Author contributions

J.L. and J.X.C. conceived and designed the methods and experiments. J.L. conducted the experiments and data analysis. J.L. and J.X.C. wrote the manuscript.

## Additional information

Supplementary information accompanies this paper at http://www.nature.com/ scientificreports

Competing financial interests: The authors declare no competing financial interests.

How to cite this article: Li, J. & Cheng, J.-X. Direct Visualization of De novo Lipogenesis in Single Living Cells. Sci. Rep. 4, 6807; DOI:10.1038/srep06807 (2014).

![](images/47adc808884b1c5fb51bb976b63ffee371dd0f11dcaf5f5476ba87d93aaf6542.jpg)

This work is licensed under a Creative Commons Attribution 4.0 Internationa License. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder in order to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0