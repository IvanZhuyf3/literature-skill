# Bi-modal microwave neuromodulation via thermal and nonthermal mechanisms

Carolyn Marar\*, Feiyuan Yu\*, Guo Chen, Jen-Wei Lin, Chen Yang, Ji-Xin Cheng

\*These authors contributed equally

## Abstract

Electrical neuromodulation, the current clinical standard, is invasive, expensive, and prone to malfunction. Electromagnetic waves can perform noninvasive neuromodulation, but existing methods are limited by the tradeoff between penetration depth and spatial precision. Microwaves in the O.9 - 3 GHz range are widely used for telecommunications and can penetrate to the deep brain. Microwaves have been shown to nonthermally modulate neural activity, but the acute bioeffects remain unclear and under-studied. Here, we employ a microwave rod antenna (MRA) to demonstrate bi-modal neuromodulation via thermal and non-thermal mechanisms. The MRA enabled electrophysiological recordings of neurons exposed to microwaves, which elucidated the differential effects of pulsed and continuous microwaves on neurons. These findings build the foundation for developing microwavebased wireless neuromodulation devices for drug-free treatment of seizures and chronic pain.

## Introduction

Nervous system disorders are the leading cause of disability in the world, affecting 3.4 billion people globally. For conditions involving excessive neural activity, such as epilepsy and chronic pain, medication remains the primary treatment²3. Not only does medication carry the risk of addiction or desensitization, but in many cases, medication is ineffective due to the complex and heterogeneous pathologies of these conditions. Neuromodulation devices present a promising alternative to medication. Neuromodulation is a potentially more robust and precise method for treating neurological disorders by directly altering the firing patterns of target neurons and effecting long-term neuroplastic changes". While neural stimulation has been achieved through various techniques, neural inhibition is less common yet may be more effective at treating conditions involving excessive or synchronized neural firing.

changes . While neural stimulation has been achieved through various techniques, neural inhibition is less common yet may be more effective at treating conditions involving excessive or synchronized nerve stimulation (VNS), and spinal cord stimulation (SCS)3,5. Electrical impulses are delivered to target neurons with high spatial precision via an implanted electrode tethered to a subcutaneous stimulator. While electrical stimulation has been used for neural inhibition, its mechanisms remain unclear. Studies suggest electrical inhibition may be achieved via activation of inhibitory networks, depolarization block, or thermal effects-8. While electrical stimulation offers the most precise and reliable neuromodulation, many adverse effects have been reported related to the device and its implantation. Because the stimulator is subcutaneously implanted, any maintenance and repair require surgery and carries the associated risks. Additionally, the complex and tethered design of the device introduces potential for malfunction (cable fracture, lead malfunction, battery failure, etc.). Wireless neuromodulation methods aim to address these issues.

associated risks . Additionally, the complex and tethered design of the device introduces potential for malfunction (cable fracture, lead malfunction, battery failure, etc.). Wireless neuromodulation methods aim to address these issues. 10,11 is limited evidence for their effectiveness in treating disorders like chronic pain and epilepsy12,13. More recently, ultrasound has been explored for neuromodulation14,15. Wireless implementation via transcranial focused ultrasound (tFUS) suffers from major interference at the skull, limiting precision and penetration depth.

recently, ultrasound has been explored for neuromodulation . Wireless implementation via 24,25 transcranial focused ultrasound (tFUS) suffers from major interference at the skull, limiting precision and penetration depth. 16–18 cellular mechanisms of microwave neuromodulation are essential to understand due to the ubiquitous use of microwave frequencies, particularly 0.9 - 3 GHz, in telecommunications19. Existing studies on the bieffect  micowaves either focus n high-requency microwaves (>0 GHz, n the long-e effects of microwave exposure19. There is an alarming lack of studies on the acute cellular effects of 0.9 - 3 GHz microwaves on mammalian neurons. This is largely due to the interference of microwaves with electronics, making it difficult to study fast cellular current dynamics²1.

effects of microwave exposure . There is an alarming lack of studies on the acute cellular effects of 0.9 – 3 GHz microwaves on mammalian neurons. This is largely due to the interference of microwaves with22 electronics, making it difficult to study fast cellular current dynamics .

also enhance safety standards for all microwave applications. Recently, our team demonstrated wireless, high-precision neural inhibition via a microwave split-ring resonator (SRR)23. We further used this device to demonstrate proof-of-concept microwave treatment of epilepsy in an in vivo mouse model. Our data suggested that the neural inhibition is achieved via a non-thermal mechanism. However, the detailed biophysical mechanisms remain to be studied.

this device to demonstrate proof-of-concept microwave treatment of epilepsy in an in vivo mouse model. Our data suggested that the neural inhibition is achieved via a non-thermal mechanism. However, the detailed biophysical mechanisms remain to be studied. continuous). Because the MRA concentrates the microwave field similarly to the SRR, we are able to use much lower powers, effectively mitigating electrical artifacts in electrophysiological recordings. This allows us to measure acute changes in neuronal membrane properties. Using a combination of calcium fluorescence imaging and patch clamp recording, we present evidence that neural inhibition occurs through nonthermal perturbation of membrane properties by millisecond pulsed microwaves, while depolarization occurs via induction of thermal transients via 1-second continuous microwaves. In contrast to other neuromodulation techniques which require higher powers to achieve inhibition6,26, microwave inhibition occurs at lower powers than depolarization. This study has applications in wireless bimodal neuromodulation to treat disorders like chronic pain and epilepsy. Additionally, this work helps to elucidate the cellular mechanisms of microwave neuromodulation toward the goal of improving safety standards.

## Results

## The microwave rod antenna enables microwave neuromodulation at low dosages.

Mechanism studies of microwave neuromodulation are difficult to conduct due to the interference of 0.9-3 GHz microwaves with electronic detectors including, cameras and electrophysiology recorders. To minimize such electrical interference, very low microwave powers must be used, but the cellular effects in this range may not be detectable. We previously demonstrated that $0 . 6 6 ~ \mathsf { W } / \mathsf { c m } ^ { 2 }$ microwave at 2.05 GHz pulsed at 10 Hz for 10 s can inhibit neurons when used with a split-ring resonator (SRR)²³3. However, when the same microwave was applied without the SRR, no significant effect was observed (Figure 1A, Fig. S1). Therefore, in order to perform electrophysiology under microwave treatment, an antenna must be used to locally amplify the field to see neuromodulation effects at low powers. To this end, we designed a microwave rod antenna (MRA) with a geometry that is more compatible with recording setups than the SRR. The MRA acts as a dipole antenna, wirelessly coupling the microwave and producing concentrated electric fields at either end (Figure 1B). In simulations, a titanium MRA with length 7 mm and diameter 0.5 mm amplified the electric field over 36 times (Figure 1C). The length of the MRA is half the wavelength of the microwave in water, meaning its resonant frequency can be tuned by changing its length (Figure 1D). The strength of the electric field can also be enhanced by tapering the MRA tip. In simulations, a 7 mm MRA with a 0.5 mm long tapered tip amplified the electric field over 65 times (Figure 1E-F). This enhancement, however, comes with a tradeoff between field strength and spatial precision (Fig. S2). For this study, we chose a titanium MRA with a O.5 mm diameter blunt tip so that the field could reach cells within \~1 mm from the tip.

To validate electric field concentration, the MRA was exposed to continuous microwave and imaged with a thermal camera (Figure 1G). Hotspots formed at each end of the MRA with a peak at 2.1 GHz, making this the resonant frequency. Because the RMA amplifies the microwave field at its tips, we were able to perform experiments at power densities as low as $0 . 0 6 6 \mathrm { ~ W ~ / c m } ^ { 2 }$ At these power densities, the MRA can be used to perform electrophysiology with minimal electrical interference. For in vitro experiments, the rod was placed over neurons and nearby cells were imaged and/or patched with a glass micropipette (Figure 1 H-J).

![](images/b84d100119414cdb60594fedad0eef2e2caa7c920f038c6b82cc3240352415bc.jpg)

<details>
<summary>heatmap</summary>

| Neuron ID | Time (s) | ΔT/T   |
|-----------|----------|--------|
| 30        | 0        | 0.66   |
| 20        | 10       | -0.1   |
| 10        | 20       | -0.1   |
| 0         | 30       | -0.1   |
</details>

![](images/2c036611fa1cfee34cf38c31450127a5db26849edb030165e9f36847939823e2.jpg)

<details>
<summary>text_image</summary>

B Max
E-field amplitude
Min
E
k
250 µm
</details>

![](images/dbf675e03aabc2d31841e6c39ff6b8646146e722b9caaa203a6afe7866eea326.jpg)

<details>
<summary>line chart</summary>

| Position (mm) | E-field amplitude (V/m) |
| ------------- | ------------------------ |
| 0             | 0                        |
| 1             | ~10                      |
| 2             | ~10                      |
| 3             | 0                        |
</details>

![](images/56b71936fa1996407bc91c2ab3e43cd91944f44bc990fe2c8825b8984e3f25b7.jpg)

<details>
<summary>line chart</summary>

| Frequency (GHz) | 4 mm   | 6 mm   | 8 mm   | 9 mm   | 7 mm   | 10 mm  |
| --------------- | ------ | ------ | ------ | ------ | ------ | ------ |
| 1.0             | 1000   | 1500   | 2000   | 2500   | 3000   | 3500   |
| 1.5             | 1500   | 2000   | 3000   | 4000   | 4500   | 5000   |
| 2.0             | 2000   | 2500   | 3500   | 4500   | 5000   | 5500   |
| 2.5             | 2500   | 3000   | 4000   | 5000   | 5500   | 6000   |
</details>

![](images/4d67e18f552e8c3dcae74f735e631ecc54fa6c2dc7fc4c9834d711c51338b2f0.jpg)

<details>
<summary>text_image</summary>

E
Max
E-field amplitude
Min
E
k
250 µm
</details>

![](images/21a40dcd41c88c36d933a7f9e6e55b56941bcee3388af1fb8b6ad803f59399b9.jpg)

<details>
<summary>line chart</summary>

| Position (mm) | E-field amplitude (V/nm) |
| ------------- | ------------------------ |
| 0             | 0                        |
| 1             | ~5                       |
| 1.5           | ~20                      |
| 2             | ~5                       |
| 3             | 0                        |
</details>

![](images/852dbc11349330e1b558cfca0564496bb3646cfdb81fc86b966a743cfe5f6099.jpg)

<details>
<summary>natural_image</summary>

Thermal or heat map image showing two bright hotspots with a dashed line indicating a boundary (no text or symbols)
</details>

![](images/23f95d23a8cc5fe55612014eea85e0dc19305482f22983e1f865daf3a7dfe529.jpg)

<details>
<summary>text_image</summary>

H
Electrode
Dish holder
MWR
Patch clamp
Signal
Waveguide
k
H
E
Cultured
neurons
</details>

![](images/66f5c481dff852edaacea4b87aafd6c900fd6bd9ade31770a84f439af5b5f5cd.jpg)

<details>
<summary>text_image</summary>

Forceps
clamping MWF
Electrode
holder
</details>

![](images/363433afc47c19ce502932edcc58d0dc26bf8a64a2c29d78e654c52c0a73e084.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of a thin filament tip with 200 μm scale bar (no text or symbols on the object itself)
</details>

![](images/4885fa0349f4258450d3e485c92cceb40141e676623431303e00c50c5e8794d1.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular or particulate structures with a 100 μm scale bar, no visible text or symbols beyond the scale indicator.
</details>

Figure 1: The MRA wirelessly couples and concentrates the microwave field. (A) Heat map of calcium fluorescence traces for neurons under 0.66 ${ \mathsf { W } } / { \mathsf { c m } } ^ { 2 }$ pulsed microwave; (B) Simulation of a titanium rod antenna with blunt ends; (C) Profile of electric field amplitude at the cross section in $\mathsf { B } ; ( \mathsf { D } )$ Frequency sweep of electric field amplitude for rod of varying length; (E) Simulation of a titanium rod antenna with tapered ends; (F) Profile of electric field amplitude at cross section in E; (G) Thermal image of blunt rod under a microwave field; outline indicates position of rod; (H) Schematic of patch clamp experiments using the microwave rod; J) Pictures of the patch clamp setup: i) closeup of rod tip under microscope, ii) closeup of patched neuron next to rod tip.

## The MRA under 10 s microwave pulse train inhibits neurons via a nonthermal mechanism.

Previously, our team demonstrated that the microwave split-ring resonator (SRR) inhibits neural activity when the microwave was pulsed at 10 Hz with 10% duty cycle (Figure 2A). In the current work, the microwave is pulsed in this manner to minimize the rate of heating and therefore thermal stimulation effects. A 7.5 mm MRA with a 0.5 mm diameter blunt tip was fabricated from pure titanium (Figure 2B) and placed over primary rat cortical neurons in vitro. Neurons were dyed with Oregon green to visualize calcium activity. The neurons exhibited spontaneous baseline activity. When the 10 Hz pulsed wave (PW) microwave was applied, the neural activity was strongly inhibited before returning to baseline activity levels (Figure 1C). To determine the lower limit of the inhibition effect, microwave power density was decreased from 0.66 $\mathsf { W } / \mathsf { c m } ^ { 2 }$ to 0.066 $\mathsf { W } / \mathsf { c m } ^ { 2 }$ (Figure 2D-G). Calcium traces were normalized and baseline-corrected (Fig. S3) and area under the curve (AUC) was used to quantify neural activity before, during, and after microwave treatment (Figure 2H-K). Activity was decreased by 26.6%, 26.9%, 19.5%, and 3.6% during 0.66 $\mathsf { W } / \mathsf { c m } ^ { 2 }$ , 0.41 ${ \mathsf { W } } / { \mathsf { c m } } ^ { 2 } .$ , $0 . 2 5 \mathsf { W } / \mathsf { c m } ^ { 2 }$ , and $0 . 0 6 6 \mathsf { W } / \mathsf { c m } ^ { 2 }$ microwave treatment, respectively $( \mathsf { N } = 3$ dishes). 0.066 $\mathsf { W } / \mathsf { c m } ^ { 2 }$ was the lowest power density at which significant inhibition was observed, making it more effective than the SRR at lower power densities (Fig. S4). Extended calcium fluorescence recordings confirmed the neurons were not damaged after inhibition (Fig. S5).

![](images/867700672a48fb8a842bdbd8edae84551d92cd8ade40a7f1fdbc8151ab8345dd.jpg)

<details>
<summary>text_image</summary>

A 10 ms 90 ms ... 10 s
B 3 mm
</details>

![](images/21d9f8b10aa9f4f407e80d57832928b7889c1209b6aa935b1931a2b843b4f226.jpg)

<details>
<summary>line chart</summary>

| Time (s) | ΔE/F     |
| -------- | -------- |
| -10      | 0.08     |
| 0        | 0.03     |
| 10       | 0.02     |
| 20       | 0.06     |
| 30       | 0.09     |
| 40       | 0.05     |
</details>

![](images/7ba1b0ba2a88c27f6651d462276ff81b6028c0067ab266511165f05c757dc7d5.jpg)

<details>
<summary>heatmap</summary>

| Neuron ID | Time (s) | Value     |
|-----------|----------|-----------|
| 80        | -10      | 0.66 W/cm² |
</details>

![](images/3be6f04a8988b029f0654fbfa8c1dedacbe9c10318196b49d30318d5a025dbd9.jpg)

<details>
<summary>heatmap</summary>

| Time (s) | Value |
| -------- | ----- |
| 0        | 60    |
| 10       | 40    |
| 20       | 20    |
| 30       | 0     |
| 40       | 0     |
</details>

![](images/6d2c7edec76f87114fc035faabba757be23a22aec911d95284bd538076bab1dd.jpg)

<details>
<summary>heatmap</summary>

| Time (s) | Value     |
| -------- | --------- |
| -10      | 0.25 W/cm²|
| 0        | 0.25 W/cm²|
| 10       | 0.25 W/cm²|
| 20       | 0.25 W/cm²|
| 30       | 0.25 W/cm²|
| 40       | 0.25 W/cm²|
</details>

![](images/114da2b6b6839619370a1c3ed416a12495b8481edd62c88a4b5dbef536c3e9db.jpg)

<details>
<summary>heatmap</summary>

| Time (s) | 0    | 10   | 20   | 30   | 40   |
|----------|------|------|------|------|------|
| -10      | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 |
| 0        | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 |
| 10       | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 |
| 20       | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 |
| 30       | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 |
| 40       | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 |
</details>

![](images/5d2996d7a1a40197dc5c7bd1c11d2854bdc8b4c08e95c20c3fe9acc681736a91.jpg)

<details>
<summary>box plot chart</summary>

| Time (s) | AUC     |
| -------- | ------- |
| -10      | ~5      |
| 3        | ~5      |
| 10       | ~10     |
| 20       | ~15     |
| 30       | ~20     |
</details>

![](images/784ab8b6aa6de39efa4326c38c14591850c691cc6c6205b1e18a7b61be0ae991.jpg)

<details>
<summary>scatterplot</summary>

| Time Period | AUC Value |
| ----------- | --------- |
| -10-3s      | ~15       |
| 0-10s       | ~5        |
| 10-20s      | ~25       |
| 20-30s      | ~20       |
| 30-40s      | ~15       |
</details>

![](images/c9dbfa63320c43db24bb4df62eb81782bf6263a122d8adf358607a30a490ceb5.jpg)

<details>
<summary>scatterplot</summary>

| Time Point | AUC Value |
| ---------- | --------- |
| -10.08     | ~5        |
| 0-10h      | ~3        |
| 10-20h     | ~10       |
| 20-30h     | ~15       |
| 30-40h     | ~20       |
</details>

![](images/01e03cb5b02503801cbd8ffbd5a242452884f66d17132413e3b526f8bc75c1e8.jpg)

<details>
<summary>box plot</summary>

| Time Point | AUC Value |
| ---------- | --------- |
| -10-0s     | ~15       |
| 0-10s      | ~12       |
| 10-30s     | ~18       |
| 20-30s     | ~22       |
| 30-40s     | ~16       |
</details>

![](images/9e106dff6a0def2d675116cb0533d2257b5ed85f7b3e06b9f8c64b62d17e10d2.jpg)

<details>
<summary>natural_image</summary>

3D illustration of a laboratory apparatus with a pipette inserted into a bowl containing pink liquid, no text or symbols present.
</details>

![](images/8d41e1dfd24d3b0bfa430c956554ba9cd9747ac4a30d4f6cb23027270e517461.jpg)

<details>
<summary>line chart</summary>

| Time (s) | MRA 10 s PW | Thermal control |
| -------- | ----------- | --------------- |
| 0        | ~0          | ~0              |
| 3.2      | ~3.2        | ~3.2            |
| 5        | ~3.2        | ~3.2            |
</details>

![](images/eb23a953e16a1153495e23c6ac4ea3d83491b411409355ef15f34f99e0680572.jpg)

<details>
<summary>heatmap</summary>

| Time (s) | Neuron D |
| -------- | -------- |
| 0        | 0.4      |
| 20       | 0.4      |
| 40       | 0.4      |
</details>

![](images/8b05c0c2c6169356a99e629f520cfb2e082a085d7abb4bd29cca1caf11cf0cd6.jpg)

<details>
<summary>scatterplot</summary>

| Time Interval | AUC Value |
| ------------- | --------- |
| -10s          | ~15       |
| 0-10s         | ~25       |
| 10-20s        | ~60       |
| 20-30s        | ~45       |
| 30-40s        | ~70       |
</details>

Figure 2: Pulsed microwave inhibits neurons via a nonthermal mechanism. (A) Schematic of microwave pulse modulation; (B) 7.5 mm blunt tip MRA used in experiments; (C) Example trace of calcium fluorescence under 0.66 $\mathsf { w } / \mathsf { c m } ^ { 2 }$ pulsed microwave; (D-G) Heat maps of calcium activity in neurons under pulsed microwave at $0 . 6 6 - 0 . 0 6 6$ ${ \mathsf { W } } / { \mathsf { c m } } ^ { 2 } ;$ (H-K) Area under the curve of calcium traces for neurons in D-G, respectively; (L) Schematic of thermal control experiments; (M) Change in temperature near the MRA tip (top) and thermal control trace (bottom); (N) Heat maps of calcium activity in neurons under thermal control heating; (O) AUC of calcium traces for neurons in N; Plots show mean and standard deviation; Statistical significance calculated using pair sample t test where $^ { * * * } \mathsf { p } { < } 0 . 0 5 , ^ { * * } \mathsf { p } { < } 0 . 0 1 , ^ { * * } \mathsf { p } { < } 0 . 0 0 1$ , n.s. not significant; Red bars indicate treatment periods.

To determine whether the neural inhibition effect of the microwave was thermal, a negative thermal control was performed. The tip of an optical fiber was coated with carbon and heated with a 1064 nm laser to produce heat without microwaves (Figure 2L). The laser was pulsed at 10 Hz with 10% duty cycle (same as the PW microwave) to reproduce the temperature profile as closely as possible (Figure 2M). Under 0.66 $\mathsf { W } / \mathsf { c m } ^ { 2 }$ PW, the MRA produced a $0 . 6 ^ { \circ } C$ change. For the negative thermal control, the temperature change was $0 . 5 3 ^ { \circ } \complement$ with a similar temperature profile. When heated in the absence of microwave, no significant change in neural activity was observed (N = 3 dishes) (Figure 2N-O, Fig. S6).

## Under 0.66 W/cm PW, the MRA produced a 0.6 C change. For the negative thermal

To determine how pulse modulation and thermal profile impact microwave neuromodulation, the MRA was placed over neurons in vitro (Figure 3A) and continuous (CW) microwave was delivered for 1 s. Techniques like infrared neural stimulation induce temporal temperature gradients (dT/dt) to depolarize neurons²7. Therefore, 1 s CW was used because it is the same total energy dosage as the $1 0 \textsf { s P W }$ condition but generates a much higher dT/dt. When $1 \ \mathsf { s } \ \mathsf { C W } \ 0 . 6 6 \ \mathsf { W / c m } ^ { 2 }$ microwave was delivered, neurons exhibited an increase in calcium fluorescence (Figure 3B). The microwave-stimulated peak, however, appeared to be a subthreshold depolarization. In contrast to the rapid rise time of spontaneous calcium peaks (blue arrow), the stimulated peak increased slowly until the microwave turned off, after which it decreased. This depolarization is likely due to an influx of ${ \mathsf { C a } } ^ { 2 + }$ current since an action potential was not induced. This depolarization was repeatable and non-toxic to the neurons (Fig. S7).

turned off, after which it decreased. This depolarization is likely due to an influx of Ca current since an action potential was not induced. This depolarization was repeatable and non-toxic to the neurons ( depolarization appeared to decrease. More interestingly, some cells seemed to be inhibited at further distances from the MRA. Cells were classified into two groups based on whether the AUC increased (depolarized) or decreased (inhibited) during microwave treatment (Figure 3D). This analysis revealed that the fraction of cells depolarized decreased with distance, while the fraction of cells inhibited increased. This observation is consistent with a nonthermal mechanism for inhibition. as cells further from the MRA experience less heating, but may still be inhibited by a distinct mechanism. As further evidence, depolarization and inhibition fractions were measured at power densities ranging from O.066 $- 0 . 6 6 ~ \mathsf { W / c m } ^ { 2 }$ (Figure 3E). As expected, as power density decreased, depolarization decreased while inhibition increased.

evidence, depolarization and inhibition fractions were measured at power densities ranging from 0.066 – 0.66 W/cm ( ). As expected, as power density decreased, depolarization decreased while inhibition increased. $0 . 7 8 ^ { \circ } \mathsf C$ and the reproduced thermal profile had an increase of $0 . 6 0 ^ { \circ } \mathsf { C }$ . When the cells were heated by the carbon-coated fiber for 1 $\mathsf { S } ,$ the neurons were depolarized similarly to the 1 s CW microwave condition (Figure 3G). Just as in the microwave case, the stimulated peak had a slower rise time than the spontaneous calcium peaks (Figure 3H, blue arrow). As expected, microwave depolarization seems to be dependent on dT/dt. Although $0 . 6 6 \mathsf { W / c m } ^ { 2 } 1 0 \mathsf { s P W }$ has a higher absolute temperature increase than $0 . 4 1 W / { \mathsf { c m } } ^ { 2 } 1 { \mathsf { s c W } }$ (Fig. S8), the former inhibits neurons while the latter depolarizes neurons. This is likely because dT/dt for the CW case is higher than the PW case. These results suggest that microwave depolarization occurs through thermal mechanisms, consistent with the photothermal stimulation techniques.

![](images/12e2dad089aa50e802e0f20eef2198d9367d97f87e26cce6715d24dc47e13d59.jpg)  
Figure 3: Continuous microwave depolarizes neurons via a thermal mechanism. (A) Oregon Green fluorescence image of neurons near MRA tip (dashed outline); (B) Example trace of a neuron with spontaneous (blue arrow) and microwave-stimulated (red bar) peaks; (C) Heat map of fluorescence traces for neurons at varying distance from the MRA tip under 1 s continuous microwave treatment; (D-E) Fraction of cells depolarized and inhibited as a function of distance from the MRA tip (D) and microwave power density (E); (F) Temperature change traces for the RMA under $0 . 6 6 ~ \mathsf { W / c m } ^ { 2 } \texttt { 1 s C W }$ microwave (top) and recreated trace using laser heating; (G) Heat map of

fluorescence traces for neurons at under laser heating; (H) Example trace of spontaneous (blue arrow) and heat stimulated (red bar) calcium peaks.

## Real-time patch clamp recording reveals differential effects of continuous and pulsed microwave on neuronal membranes.

To elucidate the distinct thermal and nonthermal effects of microwave neuromodulation, the MRA was integrated into a patch clamp recording system as shown in Figure 1J. With the MRA, microwave effects were achieved at lower operational powers, reducing electrical artifacts (Fig. S9A). The MRA was held over the neurons and whole cell patch clamp recordings were performed on cells within 1 mm of the tip to measure changes in passive membrane properties and action potential (AP) characteristics. Positive current was injected into the cell every 1 s to induce an AP.

over the neurons and whole cell patch clamp $\mathsf { W / c m } ^ { 2 } \texttt { 1 s c W }$ performed on cells within 1 mm of the tip to measure changes in passive membrane properties and action potential (AP) characteristics. Positive current was injected into the cell every 1 s to induce an AP. mechanism. In some cases, $\mathsf { A P }$ amplitude decreased slightly during microwave (Figure 4Bi), but there were no other notable changes to $\mathsf { A P }$ characteristics (Figure 4C, Fig. S9B, Fig. S10). The decrease in AP amplitude can be explained by the microwave-induced depolarization, as there was a correlation between $\mathsf { A } / \mathsf { A } _ { 0 }$ and $\Delta \lor _ { \mathsf { r e s t } }$ (Fig. S11A). This indicates that the change in AP amplitude is likely due to mechanism. In some cases, AP amplitude decreased slightly during microwave ( ), but there decrease in membrane resistance $\left( \mathsf { R } _ { \mathsf { m } } \right)$ and a significant decrease in membrane capacitance $\{ { \mathsf { C } } _ { \mathsf { m } } \}$ (Figure 4Bi-C). Both parameters recovered after microwave exposure. In combination with the calcium influx between A/A and ΔV ( ). This indicates that the change in AP amplitude is likely due to nonspecific cationic current. Since it is thermally induced, the current likely comes from thermosensitive transient receptor potential (TRP) channels, which are nonspecific.

observed during calcium imaging, this data s $\mathsf { W } / \mathsf { c m } ^ { 2 }$ that the depolarization may be induced by nonspecific cationic current. Since it is thermally induced, the current likely comes from thermosensitive transient receptor potential (TRP) channels, which are nonspecific. This suggests a leaky $\nmathsf { K } ^ { + }$ current may be involved. Very weak correlation was found between $\mathsf { A } / \mathsf { A } _ { 0 }$ and $\Delta \lor _ { \mathsf { r e s t } }$ the neurons were exposed to 0.25-0.66 W/cm 10 s PW microwave ( ). During the include an increase in AP duration and a larger after-hyperpolarization (Figure 4F). When negative current was injected into the neuron, again, the membrane resistance decreased, suggesting the This suggests a leaky K current may be involved. Very weak correlation was found between A/A and mechanisms - thermal and nonthermal - are responsible for the differential effect of microwaves on neuronal activity.

![](images/b8db2bfc2b2e8a2e25cf74fa3b5160c22095d997c9ef8186b5386c3f251edf61.jpg)  
Figure 4: Patch clamp reveals distinct neuromodulation mechanisms. (A) Membrane potential of a neuron near the MRA tip (top) in response to the current injection protocol and 1 s CW microwave (red line); inset image shows zoomed in trace during microwave exposure; (B) Membrane potential in response to positive (i) and negative (ii) current injections for 1 s CW microwave; (C) Summary of neuron membrane and action potential features for 1 s CW microwave (N = 11 neurons); (D) Membrane potential of a neuron near the MRA tip (top) in response to the current injection protocol and 10 s PW microwave; inset image shows zoomed in trace during microwave exposure; (E) Membrane potential in response to positive (i) and negative (ii) current injections for 10 s PW microwave; (F) Summary of neuron membrane and action potential features for 10 s PW microwave (N = 27 neurons); Significance calculated using pair-sample t test \*p<0.05, \*\*p<0.01, \*p<0.001, n.s. not significant.

## Discussion

In this study, we developed a MRA that can wirelessly couple and amplify microwave fields to study the bioeffects of microwaves at low operational power densities. This study is timely and relevant as the public is increasingly exposed to microwaves, particularly O.9 - 3 GHz, via cellphones, Wi-Fi, and other devices1. The current standards for safe microwave exposure are primarily based on the thermal effects of microwaves which occur at higher powers²2. While several studies have reported thermal and nonthermal neural effects of microwaves16-19, almost nothing is known about the acute cellular mechanisms by which they occur.

Previously, there has been some debate around whether microwaves have an excitatory or inhibitory efuons y  l,ur sudy poi new nsiht ino hefential microwave neuromodulation and their distinct cellular mechanisms. When 1 s CW microwave is applied, neurons are depolarized. When the microwave is pulsed at 10 Hz with 10% duty cycle, an equivalent dosage to the CW condition, neurons are inhibited. We observed that microwave-induced depolarization is likely caused by a rapid temperature increase (dT/dt), while microwave inhibition occurs via a nonthermal mechanism. This result is significant because inhibition occurs at lower microwave intensities than excitation, as opposed to other neuromodulation methods for which the 6,26,31

occurs via a nonthermal mechanism. This result is significant because inhibition occurs at lower microwave intensities than excitation, as opposed to other neuromodulation methods for which the thermal activation of TRP channels, as confirmed via channel blocker experiments. Microwave-induced depolarization is therefore similar to conventional thermal stimulation techniques26,32. More interestingly, we discovered that nonthermal microwave inhibition is independent of membrane depolarization and occurs via a distinct mechanism. Or results suggest that leaky K+ currents are likely involved.

interestingly, we discovered that nonthermal microwave inhibition is independent of membrane depolarization and occurs via a distinct mechanism. Or results suggest that leaky K+ currents are likely molecular level. Microwave frequencies overlap with the rotational spectrum of water³. The orientation of water molecules at the neuronal membrane, around ions, and within ion channels has appreciable impact on neuron function34-39. Rotational excitation of water molecules may perturb these functions, altering membrane potential, ion solvation, and ion channel conductance. These mechanisms warrant further study to elucidate the bioeffects of microwaves and better inform exposure standards.

impact on neuron function . Rotational excitation of water molecules may perturb these functions, altering membrane potential, ion solvation, and ion channel conductance. These mechanisms warrant further study to elucidate the bioeffects of microwaves and better inform exposure standards. stimulation which induces a depolarization block6,40. When used to treat conditions such as chronic pain, electrical stimulation has been reported to induce AP at the onset of the stimulus41, likely because depolarization block occurs with extended depolarization. Extraneous stimulation may also occur if the threshold for a depolarization block is not reached. Additionally, since electrical inhibition requires higher intensity/frequency, it has a higher potential to exceed safety limits42,43. Microwave neural inhibition can avoid these issues, since it does not occur via depolarization block and requires lower powers with minimal heating. The MRA occupies a volume of \~2 mm²³ and can wirelessly couple with an external power source, making it much less invasive than electrical neuromodulation. We previously demonstrated seizure suppression in a mouse model using a microwave resonator²³. The MRA therefore has great potential for therapeutic neuromodulation.

external power source, making it much less invasive than electrical neuromodulation. We previously demonstrated seizure suppression in a mouse model using a microwave resonator . The MRA therefore has great potential for therapeutic neuromodulation. be leveraged to design highly effective and minimally invasive microwave neuromodulation devices.

## Materials and Methods

Titanium microwave rod antenna (MRA) fabrication. The MRA was fabricated from Grade 1 pure titanium wire (Nexmetal Corporation) with diameter 0.5 mm. The wire was cut to 7.5 mm in length and the ends were polished flat using sandpaper.

The MRA was fabricated from Grade 1 pure titanium wire (Nexmetal Corporation) with diameter 0.5 mm. The wire was cut to 7.5 mm in length and the ends were polished flat using sandpaper. titanium model in the COMsOL materials library. The physical field was simulated using the Electromagnetic Waves, Frequency Domain module. The input power was 1.0 W. The MRA was oriented in the z-plane. The microwave originated from a 50 $\mathsf { c m } ^ { 2 }$ port with a plane wave input that has E polarized in the z-direction. H was polarized perpendicular to the MRA plane in the y-direction. Scattering conditions were used at the boundaries of the simulated area.

in the z-plane. The microwave originated from a 50 cm port with a plane wave input that has polarized in the z-direction.  was polarized perpendicular to the MRA plane in the y-direction. Scattering conditions were used at the boundaries of the simulated area. bottom culture dishes in Dulbecco's Modified Eagle Medium (Thermofisher Scientific) with 10% fetal bovine serum (Thermofisher Scientific). After 24 hours, medium was replaced with feeding medium consisting of Neurobasal medium supplemented with 2% B-27 (Thermofisher Scientific), 1% N2, and 1% GlutaMAxTM (Thermofisher Scientific). Fresh feeding medium was added to the culture every 3-4 days. Experiments were performed on days 10-14.

consisting of Neurobasal medium supplemented with 2% B-27 (Thermofisher Scientific), 1% N2, and 1% GlutaMAXTM (Thermofisher Scientific). Fresh feeding medium was added to the culture every 3-4 days. Experiments were performed on days 10-14. (FBH520-40, Thorlabs), an excitation filter (MF469-35, Thorlabs), and a dichroic mirror (DMLP505R, Thorlabs). A scientific CMOs camera (Zyla 5.5, Andor) was used to collect images at 20 frames per second. One hour before calcium imaging, cells were incubated at $3 7 ^ { \circ } \mathsf { C }$ with 2 µM Oregon Green 488 BAPTA-1 dye (Invitrogen) for 30 minutes. The medium was then replaced with fresh medium, and cells were incubated at 37°C for another 30 minutes.

second. One hour before calcium imaging, cells were incubated at 37°C with 2 μM Oregon Green 488 BAPTA-1 dye (Invitrogen) for 30 minutes. The medium was then replaced with fresh medium, and cells were incubated at 37°C for another 30 minutes. at a frame rate of 30 Hz or 60 Hz.

microwave waveguide was oriented with  parallel to the MRA plane. Microwave was delivered at the resonant frequency. Imaging was performed using a thermal camera (A325sc, FLIR). Video was captured at a frame rate of 30 Hz or 60 Hz.

Precise thermal measurements were taken using an optical fiber temperature sensor (OpSens OTG-M220). The fiber tip was positioned toughing the MRA tip. Measurements were taken at a rate of 50 Hz. Next, in order to stabilize the coating, a layer of PDMS was added. To prepare the PDMs, the silicone elastomer (Sylgard 184, Dow Corning Corporation, USA) was carefully dispensed into a container to minimize air entrapment. Then, the curing agent was added for a weight ratio of ten to one (silicone elastomer to curing agent). A nanoinjector deposited the PDMS onto the tip of the candle-soot coated fiber. The position of the fiber and the nanoinjector were both controlled by 3D manipulators for precise alignment, and the PDMS coating process was monitored under a lab-made microscope in real time. The coated fiber was stored overnight in a temperature-controlled environment (200iC) for 12 h, to allow the PDMS to cure. A continuous 1064 nm laser was coupled into the optical fiber to heat up the carbon tip. The laser was applied for either 1 s continuously or pulsed at 10 Hz with a 10% duty cycle for 10 s. Laser pulsing was achieved using an optical chopper (Thorlabs).

PDMS to cure. A continuous 1064 nm laser was coupled into the optical fiber to heat up the carbon tip. The laser was applied for either 1 s continuously or pulsed at 10 Hz with a 10% duty cycle for 10 s. Laser pulsing was achieved using an optical chopper (Thorlabs). $6 0 . 5 ~ { \mathsf { c m } } ^ { 2 }$ rectangular aluminum waveguide (WR430, Pasternack) oriented with E field parallel to the MRA plane. Microwave was delivered for either 1 s continuous or 10 s pulsed at 10 Hz with 10% duty cycle. Pulse modulation was achieved using a function generator (33220A, Agilent). In calcium fluorescence experiments, the MRA was placed directly on the cells. The waveguide was placed over the dish, covering it completely from above. In electrophysiology experiments, the MRA was held in the bath solution over the neurons using plastic tweezers. A QUAD 4-axis motorized micromanipulator (Sutter Instrument, Novato, CA, USA) was used to control distance to the neurons and the microwave was delivered from below the dish.

solution over the neurons using plastic tweezers. A QUAD 4-axis motorized micromanipulator (Sutter Instrument, Novato, CA, USA) was used to control distance to the neurons and the microwave was delivered from below the dish. sampled at 20 kHz. All recordings were performed at room temperature. Recordings were conducted on cultured neurons at DIV 10-17, held at -70 mV in an external solution containing 140 mM NaCl, 3 mM KCI, 1.5 mM $\mathsf { M g C l } _ { 2 } ,$ 2.5 mM ${ \mathsf { C a C l } } _ { 2 } ,$ , 11 mM glucose, and 10 mM HEPES (pH 7.4). Recording electrodes were filled with a K+-based internal solution (135 mM K+-gluconate, 5 mM NaCl, 2 mM $\mathsf { M g C l } _ { 2 } ,$ 10 mM HEPES, 0.6 mM EGTA, 4 mM ${ \mathsf { M } } { \mathsf { g } } ^ { 2 + } { \mathsf { - G T P } } .$ ,and 0.4 mM $\mathsf { N a ^ { + } { - } A T P } )$ with a resistance of 5-10 MΩ. For nucleated outside-out patch recordings, whole-cell configuration was first established. In blocker experiments, 1 nM TTX or 5 nM Ruthenium Red was applied. Data were analyzed and visualized using MATLAB (MathWorks, Natick, MA, USA). AP parameters and membrane properties were analyzed only in neurons with resting membrane potentials between -60 and -70 mV and AP amplitudes greater than 40 mV. AP amplitude was measured as the difference between the average membrane potential 1 ms before current injection and the peak of the AP. After-hyperpolarization was determined by identifying the minimum membrane potential within 100 ms following an AP peak. AP latency was calculated based on the threshold potential, defined as the membrane potential at which dV/dt first exceeded 5 V/s.

before current injection and the peak of the AP. After-hyperpolarization was determined by identifying the minimum membrane potential within 100 ms following an AP peak. AP latency was calculated based on the threshold potential, defined as the membrane potential at which dV/dt first exceeded 5 V/s. and subtracting it from the raw image. Traces were analyzed in Python 3.11 using a custom script. First each trace was normalized to ΔF/F and filtered with a 40 Hz lowpass filter. The baseline of the trace was then calculated to correct for any fluctuations due to photobleaching or thermal artifacts. The baseline was calculated using an asymmetric least square smoothing algorithm with lambda = 1000 and ${ \mathsf { p } } ^ { \mathsf { \Delta } } =$

0.001. The baseline was subtracted from the filtered signal. Neural activity was quantified as the area under the curve (AUC) of the baseline-corrected trace. Plots were made using OriginPro 2021.

Statistical analysis. Statistical analyses were performed using OriginLab 2021. Data are expressed as the 0.001. The baseline was subtracted from the filtered signal. Neural activity was quantified as the area under the curve (AUC) of the baseline-correcte

## References

1. Steinmetz, J. D. et al. Global, regional, and national burden of disorders affecting the nervous system, 1990-2021: a systematic analysis for the Global Burden of Disease Study 2021. Lancet Neurol. 23, Steinmetz, J. D.  
1990–2021: a systematic analysis for the Global Burden of Disease Study 2021.  , 344–381 (2024).  
2. Cohen, S. P., Vase, L. & Hooten, W. M. Chronic pain: an update on burden, best practices, and new advances.  
3. Riva, A.  New Trends and Most Promising Therapeutic Strategies for Epilepsy Treatment. , (2021).  
4. Kricheldorff, J.  Evidence of Neuroplastic Changes after Transcranial Magnetic, Electric, and Brain Stimulation.  , 929 (202  
5. O’Connell, N. E.  Implanted spinal neuromodulation interventions for chronic pain depolarization in mouse hippocampus. Nat. Commun. 13, 7709 (2022).  
7. Chiken, S. & Nambu, A. Mechanism of Deep Brain Stimulation. The Neuroscientist 22, 313-322 depolar  
8. Xue, T. et al. Neuromodulation in drug-resistant epilepsy: A review of current knowledge. Acta (2016).  
8. Xue, T.  Neuromodulation in drug-resistant epilepsy: A review of current knowledge. , 786–797 (2022).  
10. Siebner, H. R. et al. Transcranial magnetic stimulation of the brain: What is stimulated? - A consensus and critical position paper. Clin. Neurophysiol. 140, 5997 (2022).  
10. Siebner, H. R.  Transcranial magnetic stimulation of the brain: What is stimulated? – A consensus and critical position paper.  , 59–97 (2022).  
11. Deng, Z.-D., Lisanby, S. H. & Peterchev, A. V. Electric field depth–focality tradeoff in transcranial magnetic stimulation: simulation comparison of 50 coil desi  
12. Walton, D., Spencer, D. C., Nevitt, S. J. & Michael, B. D. Transcranial magnetic stimulation  
t tment of epilepsy - Walton, D - 2021 | Cochrane Library. . Knotkova,  
15. Jiang, Y.  Optoacoustic brain stimulation at submillimeter spatial precision. , 881 (2020).  
15. Sigona, M. K. & Caskey, C. F. Ultrasound neuromodulation: planning and validating treatments , 101430 (202  
17. Romanenko, S., Siegel, P. H., Wagenaar, D. A. & Pikov, V. Effects of millimeter wave irradiation and equivalent thermal heating on the activity of individual neurons in the leech ganglion. J. Romanenko, S., Siegel, P. H., Wa  
a equivalent thermal heating on the activity of individual neurons in the leech ganglion. , 2423–2431 (2014). Neural Eng. 7, 045003 (2010).  
a plasma membrane properties with low-power millimeter waves in organotypic cortical slices. , 045003 (2010).  
19. Mumtaz, S., Rana, J. N., Choi, E. H. & Han, I. Microwave Radiation and the Brain: Mechanisms, Current Status, and Future Prospects.  
21. Platano, D. et al. Acute exposure to low-level CW and GSM-modulated 900 MHz radiofrequency does not affect Ba² currents through voltage-gated calcium channels in rat cortical neurons. . Platano, D.  Acute exposure to  
22. not affect Ba currents through voltage-gated calcium channels in rat cortical neurons. Electromagnetic Fields, 3 kHz to 300 GHz. IEEE Std C951-2005 Revis. IEEE Std C951-1991 1-238 (2006) doi:10.1109/IEEESTD.2006.99501.  
E romagnetic Fields, 3 kHz to 300 GHz.  1–238 (200 resonator. Sci. Adv. 10, eado5560 (2024).  
23. Ansari, M. A., Akhlaghipour, N., Zarei, M. & Niknam, A. R. Microwave reflection, transmission, and absorption by human brain tissue. in Saratov Fall Meeting 2017: Optical Technologies in . Ansari, M. A., Akhlaghipour, N., Zarei, M. & Niknam, A. R  
a absorption by human brain tissue. in brain and tissue stimulation. PL0S ONE 18, e0278765 (2023).  
25. Harid, V., Kim, H., Li, B.-Z. & Lei, T. A method for non-destructive microwave focusing for photonic microdevice. Microsyst. Nanoeng. 6, 1-12 (2020).  
26. Horváth, Á. C.  Infrared neural stimulation and inhibition using an implantable sil photonic microdevice.  ,  
27. Fekete, Z., Horváth, Á. C. & Zátonyi, A. Infrared neuromodulation: a neuroengineering perspective.  , 051003 (2020).  
28. Yaghmazadeh, O.  Neuronal activity under transcranial radio-frequency stimulation in metal-free rodent brains in-vivo.  , 15 (2022).  
29. Bawin, S. M., Gavalas-Medici, R. J. & Adey, W. R. Effects of modulated very high frequency fi on specific brain  
31. Neudorfer, C. et al. Kilohertz-frequency stimulation of the nervous system: A review of underlying mechanisms. Brain Stimulat. 14, 513530 (2021).  
31. Neudorfer, C.  Kilohertz-frequency stimulation of the nervous system: A review of underlying mechanisms.  , 513–530 (2021).  
32. Sousa-Valente, J., Andreou, A. P., Urban, L. & Nagy, I. Transient receptor potential ion channel in primary se  
33. Hall, R. T. & Dowling, J. M. Pure Rotational Spectrum of Water Vapor.  , Biochem. 81, 615635 (2012).  
34. Wang, L. Measurements and implications of the membrane dipole potential. tools for investigating ion channel formation and functioning. Int. Rev. Cell Mol. Biol. 315, 245-297 . Os  
36. Chen, H., Deng, J., Cui, Q., Chanda, B. & Henzler-Wildman, K. Mapping temperature-dependent conformational change in the voltage-sensing domain of an engineered heat-activated K+ channel. . Chen, H., Deng, J., Cui, Q., Chanda, B. & Henzler-W  
37. ormational change in the voltage-sensing domain of an engineered heat-activated K+ channel. , e2017280118 (20  
37. Chowdhury, S., Jarecki, B. W. & Chanda, B. A molecular framework for temperature-dependent gating of ion channels.  , 1148–1158 (2014).  
39. DoDlangün, M. et al. Hydrogen-Bond Networks near Supported Lipid Bilayers from Vibrational Sum Frequency Generation Experiments and Atomistic Simulations. J. Phys. Chem. B 122, 4870-4879 . Do  
S Lee, J.-I., Werginz, P., Kameneva, T., Im, M. & Fried, S. I. Membrane depolarization mediates both the inhibition of neural activity and cell-type-differences in response to high-frequency . Lee, J.-I., Werginz, P., Kameneva, T., I  
41. Caylor, J. et al. Spinal cord stimulation in chronic pain: evidence and theory for mechanisms of action. Bioelectron. Med. 5, 12 (2019).  
41. Caylor, J.  Spinal cord stimulation in chronic pain: evidence and theory for mechanis stimulation: review of the state of the art. J. NeuroEngineering Rehabil. 16, 13 (2019).  
43. Vatsyayan, R., Cleary, D., Martin, J. R., Halgren, E. & Dayeh, S. A. Electrochemical Safety Limits stimulation: review of the state of the art.  , 13 (2019). . Vatsyayan, R., Cleary, D., Martin, J.