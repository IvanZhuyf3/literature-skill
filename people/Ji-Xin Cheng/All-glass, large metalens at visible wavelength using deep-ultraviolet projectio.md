# All-Glass, Large Metalens at Visible Wavelength Using Deep-Ultraviolet Projection Lithography

Joon-Suh Park,†,‡ Shuyan Zhang,†,§ Alan She,†,∥ Wei Ting Chen,† Peng Lin,⊥ Kerolos M. A. Yousef, Ji-Xin Cheng, -D

† Harvard John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, Massachusetts 02138, United States  
‡ Nanophotonics Research Center, Korea Institute of Science and Technology (KIST), Seoul 02792, Republic of Korea  
§ Laboratory of Bio-Optical Imaging, Singapore Bioimaging Consortium (SBIC), Agency for Science, Technology and Research (A\*STAR), Singapore 138667, Singapore  
∥ Singapore Heavy Engineering Pte. Ltd., Singapore 536562, Singapore  
⊥Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, United States  
# College of Biotechnology, Misr University of Science and Technology, Giza, Egypt

Supporting Information

![](images/280701377f19777f9ea6161d5938ec7eb6431b9f25f33b0cfd828e6cbd12a0aa.jpg)

<details>
<summary>text_image</summary>

4-inch glass wafer
</details>

![](images/f9fc07914cd7bdd2680be5d07ab6e8a81a78800bd5f00cea8101e9300aa08030.jpg)

<details>
<summary>scatterplot</summary>

| Lens Type         | Relative z (μm) Range | x (μm) Range |
| ----------------- | --------------------- | ------------ |
| Metalens          | -600 to 600           | -25 to 25    |
| Aspheric lens     | -600 to 600           | -25 to 25    |
| Plano-convex lens | -600 to 600           | -25 to 25    |
</details>

![](images/433a9fc9e96577e776a4b741651948f0fc3901e8ac2bd4fabbc6be66a4f0b292.jpg)

<details>
<summary>text_image</summary>

6
2 Ⅲ Ⅳ
3 Ⅲ Ⅱ
4 Ⅲ Ⅱ
5 Ⅲ Ⅱ
6 Ⅲ Ⅱ
7
Ⅲ Ⅰ 1
Ⅲ Ⅱ
Ⅲ Ⅲ Ⅱ
Ⅲ Ⅱ
Ⅲ Ⅱ
6
Ⅲ Ⅰ
50 µm
</details>

ABSTRACT: Metalenses, planar lenses realized by placing subwavelength nanostructures that locally impart lenslike phase shifts to the incident light, are promising as a replacement for refractive optics for their ultrathin, lightweight, and tailorable characteristics, especially for applications where payload is of significant importance. However, the requirement of fabricating up to billions of subwavelength structures for centimeter-scale metalenses can constrain size-scalability and mass-production for large lenses. In this Letter, we demonstrate a centimeter-scale, all-glass metalens capable of focusing and imaging at visible wavelength, using deep-ultraviolet (DUV) projection stepper lithography. Here, we show size-scalability and potential for massproduction by fabricating 45 metalenses of 1 cm diameter on a 4 in. fused-silica wafer. The lenses show diffraction-limited focusing behavior for any homogeneously polarized incidence at visible wavelengths. The metalens’ performance is quantified by the Strehl ratio and the modulation transfer function (MTF), which are then compared with commercial refractive spherical and aspherical singlet lenses of similar size and focal length. We further explore the imaging capabilities of our metalens using a color-pixel sCMOS camera and scanning-imaging techniques, demonstrating potential applications for virtual reality (VR) devices or biological imaging techniques.

KEYWORDS: Metalens, metasurface, DUV lithography, visible wavelength, all-glass

W ith the expansion of market demand for low-weight optical imaging systems such as virtual reality (VR), augmented reality (AR), and mixed reality (MR) devices; drone cameras; and even an orbital satellite’s imaging system, the need for compact, lightweight, cost-effective, and highquality large-aperture lenses is expanding.1−4 Especially for the AR/VR/MR industry, the development of lightweight, centimeter-scale lenses, larger than a human eye’s pupil, is of paramount importance.5−7 A large-aperture lens enables better imaging under low-light conditions and a larger field of view.

One of the main concerns in making large lenses in refractive optics is that their aberrations increase with diameter.8,9 For common spherical lenses, with the thickness of the lens varying from the center to the edge forming a spherical surface, the normal incident light travels through different optical path lengths and arrives at the focal plane with

Received: August 14, 2019

Revised: November 7, 2019

Published: November 14. 2019

![](images/977613cc14f1e999ce076d72943c47e4b9a9c20bde881a4996649d306a98fe2a.jpg)

<details>
<summary>line chart</summary>

| SiO₂ pillar diameter (nm) | H=1.5 µm, vertical sidewall (designed) | H=1.5 µm, tapered | H=2.0 µm, tapered (fabricated) |
| ------------------------- | -------------------------------------- | ----------------- | ------------------------------ |
| 0                         | 0                                      | 0                 | 0                              |
| 200                       | ~π/2                                   | ~π/2              | ~π/2                           |
| 400                       | ~3π/2                                  | ~3π/2             | ~3π/2                          |
| 600                       | ~6π/2                                  | ~6π/2             | ~6π/2                          |
</details>

![](images/7294fae378ec936f344b0afe132d6b61271b19e00512f525519164b5392a6ddd.jpg)

<details>
<summary>line chart</summary>

| Radial position of the lens (mm) | Ideal phase | H=1.5 µm, vertical sidewall | H=1.5 µm, tapered | H=2.0 µm, tapered |
| -------------------------------- | ----------- | -------------------------- | ----------------- | ----------------- |
| 0.0                              | 2π          | 2π                         | 2π                | 2π                |
| 0.25                             | 0           | 0                          | 0                 | 0                 |
| 0.5                              | π/2         | π/2                        | π/2               | π/2               |
| 0.75                             | π/2         | π/2                        | π/2               | π/2               |
| 1.0                              | π/2         | π/2                        | π/2               | π/2               |
</details>

![](images/ba7e2d65711cf77daafb7f806aa07c7445675963ec6a1324013718c9f5f5638a.jpg)

<details>
<summary>heatmap</summary>

| x (μm) | z (mm) | Value |
|--------|--------|-------|
| -25    | 1.9    | 0     |
| -12.5  | 2.1    | 0     |
| 0      | 2.3    | 1     |
| 12.5   | 2.5    | 0     |
| 25     | 2.7    | 0     |
| 25     | 2.9    | 0     |
| 25     | 3.1    | 0     |
</details>

![](images/1e22c0813c93fad3831e8508d098ff5b4d7b514f90660b83b635ad9c5d040e63.jpg)

<details>
<summary>line chart</summary>

| x (μm) | Normalized intensity |
| ------ | -------------------- |
| 0      | 1.0                  |
| 3.23   | 0.4                  |
</details>

Figure 1. Metalens design and simulation results. (a) Phase response library of $\mathrm { S i O } _ { 2 }$ nanopillars with different base diameters ranging from 250 to 600 nm on the $\mathrm { S i O } _ { 2 }$ substrate, and with an edge-to-edge gap of 250 nm for all calculated elements. The library is obtained for nanopillar heights (H) of 1.5 and 2.0 μm, and for sidewall tapering angles of $0 ^ { \circ }$ (vertical) and $2 . 8 5 ^ { \circ }$ obtained from fabrication results, respectively. (b) Ideal (line) phase profile for the designed metalens and the digitized (dots) phase profile realized by placing nanopillars with respect to the radial position of the lens. The areas with phase of 0 and 2π radians represent empty areas. (c) 2-dimensional reduced lens FDTD simulation of the designed metalens with simulation parameters of $\dot { \cdot } d = 5 0 0 \mu \mathrm { m } , f = \dot { 2 } . 5$ mm, $\bar { \mathrm { N A } } = 0 . 1 , \lambda _ { \mathrm { d } } = 6 3 3$ nm, and $H = 1 . 5$ μm with vertical sidewalls. Empty areas are included in the simulation to account for empty areas in the actual lens design. (d) Intensity distribution at the focal plane of part $\mathbf { c } , \mathbf { a t } \mathbf { z } = 2 . 5$ mm, showing diffraction-limited focusing behavior.

different phase delay. This leads to spherical aberration and results in an aberrated focal spot. Such aberration is present in all spherical lenses deviating from the aplanatic condition9 and is usually compensated with costly approaches such as exploiting aspheric surfaces, cascading different lenses, or using high-refractive-index materials.10,11 The weight of bulk refractive optics makes it even less advantageous in terms of low-weight optical systems.

Over the past few years, a different class of diffractive optical elements which can overcome certain limits of refractive optics have been introduced: metasurfaces.12−17 They are realized by placing subwavelength spaced structures on a planar surface to locally control phase, polarization, and amplitude of the transmitted light and are tailored by design optical effects such as the generalized Snell’s law.18 Recent works have shown that such metasurfaces can have features that any single refractive element cannot possess: broadband correction of bulk refractive optics,19,20 broadband achromatic focusing,7,21,22 polarization and wavelength dependent functions,23−26 polarization state generation,27−30 and polarimetry.31−34 A metasurface that works as a lens is referred to as a metalens.6,7,17,21 It has been shown that metalenses have larger angular transmission compared to Fresnel lenses, which suffer the unfavorable shadowing effect due to their sawtooth surface profile.35 Recent advanced topology optimization has shown that a metalens can exceed focusing efficiency of 93%.36

Most metalenses have so far been fabricated with e-beam lithography which, however, is not suitable for size-scalability and mass-production. Recently, stepper lithography and imprint lithography have been used to overcome these limitations.5,37−40 In a previous report, we introduced a data compression algorithm, coined METAC, for reticle writing of centimeter-scale radially symmetric metasurfaces and fabri cated amorphous silicon-based metalenses in near-infrared.37 We showed the possibility of large-area metalens mass manufacturing with conventional semiconductor fabrication tools, the 5× reduction i-line (λ = 365 nm) stepper lithography. In addition, we demonstrated that a single 2 cm diameter metalens working in near-infrared can fulfill the ideal thin-lens equation and therefore evade spherical aberration.41

Here, we present design, fabrication by deep-ultraviolet (DUV) lithography, and characterization of mass-producible, centimeter-scale metalenses made of the most common refractive lens material, glass, capable of focusing and imaging at visible wavelengths. Unlike previous studies which needed a separate deposition process of high-refractive-index dielectric materials, such as silicon,37,40 titanium dioxide $\left( \mathrm { T i O } _ { 2 } \right) , ^ { 2 1 , 4 2 }$ silicon nitride $\left( \mathrm { S i N } \right) , ^ { 3 7 }$ or gallium nitride $\left( \mathrm { G a N } \right) , ^ { 3 9 }$ on a transparent substrate to realize a metalens, here we use lowrefractive-index fused silica $\left( \mathrm { S i O } _ { 2 } \right)$ as both substrate and constituent material43 to demonstrate a single-material metal ens with obvious advantages in terms of mass-production time, simpler fabrication process, and cost.

We have designed a metalens of 1 cm diameter (d), 5 cm focal length (f), corresponding to a 0.1 numerical aperture (NA), optimized for diffraction-limited focusing in normal incidence at $\lambda _ { \mathrm { d } } ~ = ~ 6 3 3 ~ \mathrm { { \ n m } }$ . To achieve the required subwavelength structure sizes (a few hundred nanometers), we use DUV projection stepper lithography with source wavelength of 248 nm (KrF) to fabricate the metalens.

(a)  
![](images/0697090039560b18ea55dd135af3dd4599b1b0d301c2f2698676e89251343502.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Cr deposition"] --> B["DUV lithography"]
  B --> C["Resist develop"]
  C --> D["Dry etch Cr (resist as etch mask)"]
  D --> E["Dry etch residual Cr"]
  E --> F["Dry etch SiO₂ (Cr as etch mask)"]
  F --> G["Strip resist"]
```
</details>

![](images/6b80662b05e0afd9c7608058f33f61e4a933b4534c2d882f22e90099024d2d6b.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of conical nanostructures with 1 μm scale bar (no text or symbols on structures)
</details>

![](images/c7fdcdd9d134037f6e7812f3eb2631f7598466fead646cc60977c2be50ce7252.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing a textured surface with a scale bar of 50 μm and an inset close-up of a patterned material (no text or symbols)
</details>

![](images/f67fd3fc8f3c9f5a102097acb8b57eb7370ba5200cd80b1a2858ba17d29f5f41.jpg)

<details>
<summary>natural_image</summary>

Close-up of a precision measurement tool interacting with a circular grid of transparent droplets (no text or symbols visible)
</details>

Figure 2. Fabrication process, SEM images of fabricated lens, and photograph of fabricated wafer. (a) Fabrication process of the designed metalens using the selective etching process. Deposited chrome (Cr) film is dry-etched on a 100 mm diameter SiO wafer with a patterned DUV resist as the etch mask using Cl . SiO is thermodynamically protected against chemical etching by $\mathrm { C l } _ { 2 }$ plasma. The $\mathrm { S i O } _ { 2 }$ wafer is then dry-etched using Cr as the etch mask with fluoride gas. Cr experiences a low etch rate under fluoride plasma. When the height of the etched pillars reaches 2.0 μm, residual Cr is again dry-etched using $\mathrm { C l } _ { 2 }$ leaving only $\mathrm { S i O } _ { 2 }$ structures. (b) Zoom-in SEM image (tiled) of nanopillars of the metalens. The top of the pillar exhibits lateral etching, and the bottom diameter of the pillar remains the same as designed; thus, there is a sidewall angle of 2.85°. (c) Top-view SEM image near the center, and the inset shows the image of the edge of the lens. Scale bar in the inset represents 10 μm. (d) Photograph of 45 fabricated 1 cm metalenses on a 100 mm (4 in.) diameter $\mathrm { S i O } _ { 2 }$ wafer, focusing incident light to a white sheet of paper.

Assuming infinitely corrected, normal incidence on the metalens, the propagation phase at the focal point f from radial po sition r of the metalens can be written as $\begin{array} { r } { \varphi ( r ) + \frac { 2 \pi } { \lambda _ { \mathrm { d } } } \sqrt { \left( r ^ { 2 } + f ^ { 2 } \right) } } \end{array}$ , where $\varphi ( r )$ is the local transmittance λ phase at r. To ensure constructive interference at $f , \varphi ( r )$ must compensate for the phase difference between the marginal ray and the chief ray $\bar { ( r \ : ) } = 0 )$ . Writing this in the form of an equation gives us the phase profile of the lens:6,19,35,37,39,40,42

$$
\varphi (r) = \varphi (0) - \frac {2 \pi}{\lambda_ {\mathrm{d}}} (\sqrt {(r ^ {2} + f ^ {2})} - f) \tag {1}
$$

where we arbitrarily set $\varphi ( 0 )$ as $2 \pi .$

To realize the target phase given by eq 1, we construct a library of phase-shifting structures that allows us to create a locally controlled metalens phase profile. We use cylindrical $\mathrm { S i O } _ { 2 }$ nanopillars of varying diameters to control phase delay. The rotationally symmetric elements ensure polarizationinsensitive focusing. To simulate the phase response of the nanopillars, we use the finite-difference time-domain (FDTD) simulation tool (Lumerical Inc.) to numerically obtain the relative phase of transmitted light for various pillar diameters with respect to the case of light propagation in air. We assume the minimal lithographically resolvable feature size to be nearly equal to 248 nm. Thus, to allow the densest distribution of the nanopillars, we maintain a 250 nm edge-to-edge gap between the nanopillars rather than a fixed center-to-center distance.37 In addition, we limit the minimum and maximum base diameters of the nanopillars to 250 and 600 nm, respectively, to remain above the lithographic tool resolution limit and below the design wavelength, respectively. We obtain the transmission phase library of $\mathrm { S i O } _ { 2 }$ nanopillars with height $H =$ 1.5 μm, as shown in Figure 1a, plotted in black circles, which is used for creating the CAD file for reticle writing. The phase shifts of the pillars are calculated relative to the area without pillars (reference phase assumed as zero). Note that, even with phase shifts by the empty areas being considered as zero, the library obtained does not fully cover the entire 0 to 2π phase, for which fulfillment is normally considered as a necessity to have a high-efficiency metalens.

During our fabrication process, we find that the fabricated SiO nanopillars have tapered sidewalls that differ from what we simulated for the library due to fabrication process imperfections. Through scanning electron microscope imaging, we find that the nanopillars retain the base diameters as designed, but the top of the pillars suffers an average tapering angle of $2 . 8 5 ^ { \circ }$ (0° being vertical, see Figure 2b). Such sidewall tapering inevitably results in a difference in phase response from the original design, which is also simulated and plotted in blue triangles in Figure 1a. We see that the tapering results in even lower phase coverage. Instead of redesigning the metalens and refabricating the photolithography mask (reticle), we try to compensate for such phase loss in the library by increasing the nanopillar height to $\mathbf { \bar { \rho } } _ { H } = 2 . 0 \ \mu \mathbf { m }$ . The calculated phase is plotted in red diamonds in Figure 1a. This height is used for fabrication of the metalenses.

The effect of such phase compensation by increasing the height becomes clear when we place the nanopillars on the design structure corresponding to the required spatial phase profile $\varphi ( r )$ . Figure 1b shows the phase of the nanopillars at each radial position r, designed to closely match the target phase $\varphi ( r )$ . Note that the required phase is plotted in modulus of 2π. When we use the initial “designed” library with $H = 1 . 5$ μm and vertical sidewalls to place the nanopillars at each radial position, while maintaining the constant edge-to-edge distance of 250 nm, we see that the phase of the nanopillars matches well with the target phase, except for the region not covered by the library. The regions that cannot be filled due to the incomplete library are left without any nanopillars. The phases of the empty areas are plotted as zero or 2π phase, whichever is closer to the required values. The area of the empty region is approximately 24.3% of the total lens area. This significantly reduces the CAD file size and reticle writing time. The phase of the tapered sidewall nanopillars with the same diameters as designed, but with heights of 1.5 and 2.0 μm, is plotted in blue triangles and red diamonds, respectively. As a result, we see that the phase loss by the tapering is partially compensated by the height increase.

We then investigate the effects of the empty areas on the focusing profile of the lens by simulating the metalens with empty spaces. Instead of simulating the entire 1 cm diameter metalens, which is not yet possible because of the limits of computational resources, we performed a calculation of a cylindrical metalens with parameters $d = 5 0 0 \ \mu \mathrm { m } , f = 2 . 5$ mm, and the same $\mathrm { N A } = 0 . 1$ using the $H = 1 . 5$ μm (vertical) library. The empty areas are present in the simulation. The results of simulation that show the focusing behavior of the simulated metalens along the optical axis and the normalized intensity across the focal plane are plotted in Figure 1c,d, respectively. In the simulation, the metalens is placed at $z = 0 ,$ along the x-axis. Light of wavelength $\lambda = 6 3 3$ nm is incident from along the $z -$ axis, propagating toward the positive z-direction. From Figure ${ \mathrm { 1 c } } ,$ we see that the intensity is maximum at the design focal point, $z = 2 . 5$ mm, showing that the metalens is focusing as intended.

From Figure 1d, the intensity distribution at the focal plane $z = 2 . 5$ mm, we see that the focusing profile closely resembles that of the theoretical focal spot shape, the Airy pattern. The Gaussian fitted full-width half-maximum (fwhm) of the center intensity is obtained as 3.23 μm. The fwhm of the ideal, diffraction-limited focal spot by an ideal lens of $\mathrm { N A } = 0 . 1$ at incidence wavelength $\lambda _ { \mathrm { d } } = 6 3 3$ nm is approximately 3.25 μm, which closely matches the simulation. The difference between the calculated and the ideal fwhm is due to the Gaussian fitting, which gives us a slightly reduced value from the ideal focal spot’s fwhm. This simulation result tells us that, even with the empty region, we can still create a metalens with diffractionlimited focusing but at the cost of focusing efficiency loss.

Figure 2a shows the schematics of the fabrication process of our metalens. On a 500 μm thick, 100 mm diameter fused silica (SiO ) wafer, we deposit 100 nm thick chrome $( \mathrm { C r } )$ , which will later act as a hard mask for etching $\mathrm { S i O } _ { 2 } .$ An antireflective coating (ARC) layer followed by a DUV photoresist layer is formed on the Cr-coated substrate by spin-coating and baking. The ARC layer suppresses back reflection from the substrate during DUV exposure, ensuring more accuracy in the lithography process. After coating of the resist, we perform DUV projection stepper lithography with the reticle written accordingly to the metalens design.

The reticle for the projection lithography is written using a Heidelberg DWL 2000 mask writer, with feature sizes of the lens magnified by 4 times to accommodate for the image reduction in the stepper. The computer-generated design for the reticle writing is obtained through our metasurface compression (METAC) algorithm employing rotational symmetry of the lens as we had previously demonstrated, in GDSII format (see the Supporting Information, SI, Figure $\mathrm { S 1 } ) . ^ { 3 7 }$ 45 dies of 1 cm metalens are exposed on the wafer, with the center-to-center distance being 1.1 cm, which is the maximum number of usable dies on the 100 mm diameter wafer with reasonable edge-to-edge spacing for dicing and handling.

The exposed substrate is then put through postexposure bake, water rinse, and spin-dry processes to have the resist form the metalens pattern on the substrate. The pattern is then transferred to the ARC layer and Cr layer sequentially by reactive ion etching (RIE) with argon/oxygen $\left( { \bf A r / O } _ { 2 } \right)$ and inductive-coupled plasma RIE (ICP-RIE) with chlorine $( \mathrm { C l } _ { 2 } ) ,$ respectively, with the resist pattern being the etch mask. As the chemical reaction of $\mathrm { S i O } _ { 2 }$ with $\mathrm { C l } _ { 2 }$ is an endothermic process, $\mathrm { S i O } _ { 2 }$ is thermodynamically protected from chemical etching by the $\mathrm { C l } _ { 2 }$ plasma; therefore, $\mathrm { C l } _ { 2 }$ provides high etch selectivity for $\mathrm { C r }$ over $\mathrm { S i O } _ { 2 } .$ This allows selective etching of the Cr layer, while etching of the $\mathrm { S i O } _ { 2 }$ substrate is minimized. After the metalens pattern is transferred to the Cr layer, we remove the ARC and the DUV resist using $\mathrm { O } _ { 2 }$ plasma, leaving only the Cr pattern on the substrate. The ARC and the DUV resist layers are removed to prevent the $\mathrm { S i O } _ { 2 }$ plasma etching process from being compromised by the formation of excessive carbon polymers.

The $\mathrm { S i O } _ { 2 }$ substrate is then etched using ICP-RIE with trifluoromethane/argon $\left( \mathrm { C H F } _ { 3 } / \mathrm { A r } \right)$ plasma until the etch depth reaches 2 μm, using the Cr pattern as the etch mask. After $\mathrm { S i O } _ { 2 }$ etching, we finally remove the remaining Cr using ICP-RIE with $\bar { \mathrm { C l } } _ { 2 }$ plasma. Although CHF has slow $\mathrm { C r }$ chemical etch speed compared to that of the $\mathrm { S i O } _ { 2 }$ so that Cr is suitable as an etch mask, the ionic bombardment from the plasma physically etches the Cr pattern in both the vertical and lateral direction during the $\mathrm { S i O } _ { 2 }$ etching process. This results in sidewall tapering of the nanopillars that was aforementioned. The shape of the tapered sidewall nanopillars observed with tilted imaging by scanning electron microscope (SEM) is shown in Figure 2b. Figure 2c shows zoomed out SEM images of the fabricated metalens near the center and at the edge (inset). Figure 2d shows the photograph of an entire fabricated 100 mm diameter wafer, consisting of 45 metalenses of 1 cm in diameter, each of which is focusing incident light to a white sheet of paper. More detailed SEM images of the fabricated metalens are provided in Figure S2. From the SEM images, we see that nanopillars smaller than 300 nm in diameter are destroyed from the lateral etching of the $\mathrm { C r }$ mask during the $\mathrm { S i O } _ { 2 }$ etching process: the $\mathrm { C r }$ mask for those pillars was etched away so that the $\mathrm { S i O } _ { 2 }$ pillars were exposed to ICP-RIE plasma and themselves were etched away. The destroyed area can be approximated as nearly planarized, so that they will only diffuse the incident light and provide scattered phase close to that of the empty areas.

![](images/7a629e8ffa4ee9536321a74ae0a9bc775f72faba950e68c380bd540538c18838.jpg)  
Figure 3. Comparison of a fabricated metalens with a commercial plano-convex lens. (a) Measured intensity distributions along the x−z plane of the metalens at $\lambda = 6 3 3$ nm. Dashed line at $z = 0$ represents the focal plane. (b) Focusing behavior of a commercial aspheric lens (Edmund Optics 33-944, $f = 5$ cm, $D = 2 . 5$ cm) at $\lambda = 6 3 3$ nm with a 1.15 cm diameter aperture stop. (c) Focusing behavior of a commercial plano-convex lens $( \mathrm { L A } 1 2 1 3 { \cdot } \mathrm { A } ,$ Thorlabs Inc., $f = 5$ cm, $D = 1 . 2 7$ cm) at $\lambda = 6 3 3$ nm. Dashed lines labeled 1−3 represent positions of paraxial ray focus, circle of least confusion, and marginal ray focus, respectively, resulting from spherical aberration of the lens. (d) Modulation transfer functions (MTFs) of ideal and measured lenses. Solid and dashed lines represent MTFs of ideal diffraction-limited lenses with NA of 0.1, 0.115, and 0.125 for the metalens, aspheric lens, and plano-convex lens, respectively. The MTFs were measured at the focal planes of the metalens, aspheric lens, and plano-convex lens, respectively, and at other planes of interest for the plano-convex lens, respectively. (e−i) Point-spread function images of the metalens, the aspheric lens, and the plano-convex lens, respectively, followed by the images of the plano-convex lens at other planes of interest, respectively. Intensity distribution of the focal spots. Dashed lines represent the ideal focal spot profile for (j) NA = 0.1, (k), $\mathrm { N A } = 0 . 1 1 5 ,$ and (l−n) NA = 0.125, respectively. The corresponding Strehl ratios (SRs) are 0.95, 0.49, 0.22, 0.17, and 0.15, respectively.

To quantify the quality of the fabricated metalens, we perform various characterizations: focusing efficiency, point spread function, modulation transfer function (MTF), and Strehl ratio measurements. To correctly measure the lens quality, one must ensure that the intensity distribution of incident light is uniform across the lens. As many of the collimating optical sources exhibit Gaussian intensity distribution, and if the intensity distribution upon the lens is as such, we obtain Gaussian focusing (Figure S3) instead of the diffraction-limited Airy disk profile. This issue does not typically arise for characterizing millimeter-scale lenses but becomes critical for larger lenses. Here, we use a near-uniform distribution of incidence intensity upon the lens by having a collimated beam in the order of few centimeters in diameter to evade such an effect.

Figure 3a−c shows the false-colored point spread functions of our metalens, an aspheric lens (33-944, Edmund Optics, d = 2.5 cm, $f = 5 \mathrm { c m } )$ , and a similar-sized plano-convex lens (LA1213-A-BK7, Thorlabs Inc., $d ~ = ~ 1 . 2 7$ cm, $f = 5$ cm) resembling our designed metalens, respectively. An aperture stop with a diameter of 1.15 cm was placed in front of the aspheric lens to match the NA to that of the metalens. All are measured along the propagation direction (z-axis) with 5 μm resolution at $\lambda = 6 3 3$ nm, unpolarized incidence. The designed focal planes of the two point-spread functions were recentered to $z = 0$ for comparison, where the lens is placed on the left of the image, and the incident beam is propagating in the positive z-direction. The dotted lines are drawn to mark significant focal planes. While the metalens shows incident light being focused to a single point along the propagation axis as shown in Figure 3a, void of spherical aberration, the aspheric lens shows elongation of point-spread function in the z-direction with its ring patterns appearing after the focus (Figure 3b) indicating a negative spherical aberration. The plano-convex lens (Figure 3c) exhibits a longer tail of focusing along the zaxis with highest-intensity focal spot being further away from the lens, which is a characteristic of a positive spherica aberration. Each of the marked focal planes on Figure 3c caused by the spherical aberration are typically referred to as (1) paraxial ray focus, (2) circle of least confusion, and (3) marginal ray focus, respectively, from ray-tracing diagrams.44 Detailed ray-tracing diagrams of the refractive lenses derived from the manufacturer data confirming such positive and negative spherical aberrations are provided in Figure S4.

From the intensity measurement at the focal plane of the metalens, we find that the focusing efficiency for unpolarized incidence is 45.6% for the designed wavelength. The focusing efficiency was measured by using an iris to only collect power contained in the region from the center to the first bright ring of the Airy disk focal spot, then divided by the power of the incident beam. The loss of low focusing efficiency can be attributed to mainly the incomplete phase coverage, empty areas in the metalens which contributed to strong zeroth order diffraction, fabrication imperfections such as sidewall tapering and destruction of smallest diameter nanopillars, diffraction to unwanted higher orders, and reflection from ${ \mathrm { S i O } } _ { 2 } { \mathrm { - } } { \mathrm { a i r } }$ and nanopillar−air boundaries. The measured diffraction efficiencies at the edge of the metalens (Figure S5), where the local nanopillars perform as a blazed grating (Figure S2c,d), also show similar results.

![](images/85f26871f1faf24c1129597b33f768ee3e9824a3c0d547aeb80966e9129eebaa.jpg)  
Figure 4. Wavelength-dependent focusing behavior. (a−d) Focal spot images of the metalens with incident wavelengths at 488, 532, 633, and 660 nm, respectively. The measured focal lengths (f) for each wavelength are 61.8, 56.9, 50.0, and 45.4 mm, respectively. (e−h) Theoretical focal spot images obtained from the Kirchoff integral. The NA values in the figures are calculated from the measured focal lengths for each wavelength. (i−l) Comparison of ideal intensity profile (dashed line) and measured focusing profile (solid line) for each incident wavelength. The Strehl ratios (SRs) are 0.91, 0.90, 0.95, and 0.88, respectively.

A common method of characterizing the performance of a lens in the camera industry is the modulation transfer function (MTF), a quantitative measure of a lens’ ability to transfer contrast information from the object plane to the image plane with respect to spatial frequency which is represented by the number of line pair per mm (lp/mm), where the line pair is a pair of opaque and transparent bars of equal width. The MTF measurement of a lens represents how much, in terms of percentage, the object’s contrast between the opaque and transparent can be reproduced at the image plane at a given spatial frequency. It represents therefore the image quality formed by the measured lens in terms of both spatial resolution and contrast in one graph.45,46

To measure the MTF, we use an industry-grade lens testing bench (LensCheck, Optikos Corp.), which obtains the MTF from the Fourier transform of the focal spot’s spatial intensity.45,46 Figure 3d shows MTF results for ideal diffraction-limited lenses, metalens, aspheric lens, and various focal planes of the plano-convex lens, respectively, at λ = 633 nm (HNL S008R, Thorlabs Inc.). The solid and dotted plots labeled as diffraction limits represent the ideal lens’ MTF, mathematically derived for NA = 0.1, 0.115, and 0.125 circular aperture lenses, respectively, with λ = 633 nm incidence.46 Each NA value corresponds to diffraction-limited metalens, aspheric, and plano-convex lens, respectively. The plot shows that the metalens’ MTF is very close to that of the diffractionlimited lens, and that of the aspheric lens (NA = 0.115) and the plano-convex lens (NA = 0.125) suffers severe contrast loss because of spherical aberration. The point where the diffraction-limited MTF contrast becomes zero is called the cutoff frequency (υ ), given by $\begin{array} { r } { \mathrm { \mathbf { 0 } } _ { 0 } = \frac { 2 \mathrm { N A } } { \lambda } . } \end{array}$ , which are calculated as 316, 363.3, and 395 lp/mm for metalens, aspheric lens, and plano-convex lens, respectively.46

In addition to determining the image quality, MTF information can be used for determining the alignment tolerance of the lens in an imaging system.11,46,47 From defocused MTF measurements (Figure S6a−d) and tilted incidence MTF (Figure S6e−h and Table S1), we can infer how much misalignment of the lens in the system can be allowed. From the MTF measurements, the depth of focus of metalens is found to be 31 μm, and the angular field of view is found to be 2° (see the Methods section and Figure S6). With this information on the lens and specifications of a given imaging sensor, one can determine how much misalignment in terms of defocus and tilt is tolerable, which is crucial information in mass-production of a camera system.

Another widely used characterization of a lens is the Strehl ratio,46 which is the comparison of the center peak intensity of a measured focal spot with that of an ideal focal spot. For a uniformly illuminated lens free of any aberration, its focal spot becomes the Fourier transform of the lens' aperture. The focal spot pattern by a diffraction-limited lens with a circular aperture is called the Airy pattern, constituting concentric rings around a bright spot at the center. In the presence of aberration, the intensity at the center, or the core intensity of an Airy pattern, becomes redistributed to outer Airy rings so that the center intensity becomes smaller than that of the ideal intensity. The Strehl ratio, the ratio between the aberrated and ideal core intensity, therefore, provides information on the relative quality of the lens performance in a single number. The Strehl ratio is 1 for a lens free of any aberration, and a lens with a Strehl ratio over 0.8 is conventionally considered as diffraction-limited by Marechal criterion.́ 48

![](images/784a4529be1701fa5aa5a974a3b97d042b605bf97580fd7e00dd523574415b33.jpg)

<details>
<summary>text_image</summary>

(a)
AMOLED screen (RGB)
Relay lens
1 cm metalens
Color
sCMOS camera
Chromatic
aberration
</details>

![](images/47f5df0451a29cb458d12b36265bed1f9c1eb4fc74da7aa86c4bc83f51647cca.jpg)

<details>
<summary>text_image</summary>

(b) AMOLED screen
VE RI
TAS
HARVARD
5 mm
</details>

![](images/feb61bacdafb87e0d51f4968d6171495163c8f41bc56c78a31a7ab7a7c459827.jpg)

<details>
<summary>text_image</summary>

(c) Color sCMOS camera
VE RI
TS
"HARVARD"
1 mm
</details>

![](images/3c7c0a4912e242bbc02351cc81a2f399dfd1f828f6076594f88f8473f53c3228.jpg)

<details>
<summary>text_image</summary>

(d)
He-Ne laser
(633 nm)
Beam
splitter
Reflected
beam
Lens 3
Iris
Photo
diode
Galvano mirror
scanner (2D)
Lens 1
Lens 2
Aperture stop
1 cm metalens
Focal length: 50 mm
Reflected beam
Scanning
Resolution target
</details>

![](images/d5dbba3e1b3464ecac442808e707e82915cb77464d83c30d64271a6ef1176495.jpg)

<details>
<summary>text_image</summary>

(e) 6
2 ≡ III ■ 7
3 ≡ III
4 ≡ III
5 ≡ III
6 ≡ III
III ≡ 1
III ≡ 2
III ≡ 3
III ≡ 4
III ≡ 5
III ≡ 6
III ≡ 7
50 µm
</details>

![](images/eb06c06b50af820def083a9862ac83c66d3c6b8538628fe4abdbc280dce9d515.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a circular pattern with radial lines, scale bar indicates 50 μm (no text or symbols)
</details>

Figure 5. Imaging with the metalens. (a) Schematic of VR-like AMOLED screen imaging. A relay lens is used to maintain image parity at the sCMOS camera. (b) Image of the Harvard logo on the AMOLED screen. (c) Image obtained from a color sCMOS camera at the metalens focal plane. Due to chromatic aberration, only red pixels are imaged at the sCMOS. The Harvard logos are trademarks of the University and are used with the permission of the President and Fellows of Harvard College. (d) Schematic of reflective scanning microscopy using the metalens. A twodimensional galvano mirror scans and deflects the incident He−Ne laser beam at a wavelength of 633 nm, and the deflected beam is expanded by a pair of lenses (Lens 1, 2). The expanded beam is then incident on the metalens at an angle and is focused by the metalens on the resolution target. The imaging target partially reflects the focused incidence back toward the metalens. The metalens then collects the reflection, and the reflected intensity at a deflected point is recorded by the photodiode. The intensity recording is performed point-by-point over a square area of 324.35 μm × 324.35 μm, with scanning resolution of 0.998 μm/pixel. (e, f) Recorded images of a USAF resolution chart and a Siemens star using scanning imaging, respectively.

Figure 3e−g shows focal spot images of the metalens, the aspheric lens, and the plano-convex lens, respectively, followed by Figure 3h,i showing focal spot images of the plano-convex lens at planes 2 and 3, respectively. The focal spot profile of the metalens shows distinct disks up to the first ring, whereas those of the aspheric and plano-convex lens show many more concentric rings. From the focal spot intensity profiles, we calculate the Strehl ratio by performing the following: We first normalize the experimental focal spot intensity profile followed by an integration to calculate power within the area up to the second dark ring for the metalens and fourth dark ring for the aspheric lens and the plano-convex lens, whose intensities are resolvable by the CCD without exceeding the saturation intensity. We do the same for their corresponding ideal Airy patterns, obtained for NA = 0.1, 0.115, and 0.125 for metalens, aspheric lens, and plano-convex lens, respectively. Subsequently, for instance, we multiplied a factor such that the obtained powers of the metalens and the ideal Airy disk are the same. After overlapping the normalized intensity profiles of the measured and the ideal one, the ratio of the central intensity values gives Strehl ratio. Figure 3j−n shows a comparison of the normalized ideal Airy function (dotted lines) with the measured intensity distribution (solid lines), respectively, from which we obtain a Strehl ratio of 0.95 for the metalens, 0.49 for the aspheric lens, and 0.22, 0.17, and 0.15 for the planes 1−3 of the plano-convex lens, respectively. This result also reasserts that the fabricated metalens is performing as a diffractionlimited lens.

Figure 4a−d shows the measured focal spot images, obtained for incidence wavelengths of 488, 532, 633, and 660 nm, respectively. Although the metalens was designed for 633 nm incidence and has chromatic aberration. we see that the metalens can still focus other visible wavelengths, and the focal spots are still diffraction-limited at their respective focal planes of wavelengths. The different focal lengths for each wavelength due to chromatic aberration are measured as 61.8, 56.9, 50.0, and 45.4 mm, respectively. The measured focal lengths translate to NA values of 0.081, 0.088, 0.10, and 0.11, respectively. Note that the focal spot sizes closely resemble each other even with different incidence wavelengths. For diffractive lenses, the focal length is inversely proportional to the angular frequency (ω) of light,21 resulting in the NA values being proportional to the wavelength. As the radius of the first dark ring in the Airy disk is 0.61λ/NA when aberrations are negligible, the wavelength-dependence of NA therefore cancels the wavelength factor in the numerator resulting in the constant focal spot sizes. A similar effect has been observed in 49 metasurface axicons.

Figure 4e−h shows the calculated focal spot images, obtained from performing the Kirchhoff integral for a perfect lens with the obtained NA values. We see that the focusing profile for each incident wavelength closely matches that of calculated ideal focusing profiles. By comparing the ideal Airy pattern for each NA with the measured focusing profile up to the second dark ring, as plotted in Figure 4i−l, we obtain Strehl ratios of 0.91, 0.90, 0.95, and 0.88, respectively, indicating that we have diffraction-limited focusing for other visible wavelengths as well. The reason for such a performance for nondesigned wavelengths can be attributed to the metalens’ low NA because the wavefront error mainly results in focal length shift.35

In addition to various metalens characterizations, we also showcase the imaging capability of the fabricated 1 cm metalens with two different methods: direct imaging of an AMOLED display, and reflective scanning imaging to show the application of the metalens to different imaging techniques. Figure 5a shows the schematic of our direct imaging of the AMOLED display setup.50 We first provide an image on the AMOLED screen of a mobile phone and have a relay lens collect and invert the image on the screen. Then, the collected image from the relay lens is passed through our 1 cm metalens, and the image is formed on a sCMOS color sensor camera placed near the metalens’ focal plane (see the Methods section for details). Figure 5b shows the image of the full-color Harvard logo displayed on the AMOLED screen, and Figure 5c shows the image on the color sCMOS camera. Although the image on the mobile phone is formed by combinations of red, green, and blue pixels (Figure S7b), as the metalens suffers chromatic aberration, the sCMOS camera only images what is visible on the focal plane for red color incidence. The chromatic aberration is still visible as the blurring of the obtained image, due to the red AMOLED pixels having a finite bandwidth. More direct imaging examples are provided in Figure S7 of the SI.

Figure 5d shows the schematic of our reflective scanning imaging apparatus, similar to a confocal scanning microscope,51 55 using a large metalens for simultaneous light focusing and collection. From incidence angle variation MTF results discussed above (Figure S6e−h), we see that we can tolerate a tilted incidence of ±1°, leading to a 2° field of view, while maintaining diffraction-limited focusing at the focal plane. The 2° angular field of view translates to a horizontal field of view with 1.75 mm diameter circle at the focal plane. Within such a region, the focal spot of the metalens is diffraction-limited. In the imaging setup, a collimated 633 nm laser beam is first deflected by a Galvano mirror scanner at an angle, which is in turn expanded by a pair of refractive lenses (Lens 1, 2). The expanded beam is then incident on a metalens at an angle. The metalens then focuses the incident beam to a target of interest. A portion of focused light is then reflected from the imaging target and is collected by the metalens. The collected light is sent back through the initial beam path but is reflected to a photodiode (PD) by a beam splitter. Lens 3 and an iris are placed before the PD to ensure that the PD only receives reflected light from the imaging target. The PD then records the reflected intensity from the target in a point-by point manner, while the Galvano mirror scanner deflects the beam, scanning the target of interest. The intensity recording is performed point-by-point over a square area of 324.35 μm × 324.35 um, smaller than the horizontal field of view, with deflection steps corresponding to the spatial resolution of 0.998 μm/pixel. The collected point-by-point reflection intensity is then used to reconstruct the image of the target of interest.

Figure 5e,f shows the reconstructed images of positive 1951 USAF resolution target group 6 and 7, and Siemens star sector 10D at its center (R1LiS1P. Thorlabs Inc.). where the bright areas are patterned with $\operatorname { C r } ,$ and dark areas are the glass substrate. From MTF results, we recall that the cutoff spatial frequency of the metalens is 316 lp/mm, which translates to individual line widths of 1.58 μm. However, due to the resolvable intensity levels the PD can discretize, combined with the spatial resolution derived from the Galvano mirror, highernumbered target elements are not well-resolved in the reconstructed image. Also, we note that as we are using the reflective scanning method, we see shadows of the corners in the pattern due to the Cr thickness. We also perform reflective scanning imaging with negative test target patterns, with the plano-convex lens instead of metalens, and transmissive scanning imaging with metalens for demonstration, which can be found in the SI, Figure S8 and Table S2. The present scanning method can be implemented for a low-cost biological sample imaging, and even for a fluorescence scanning imaging technique with some modifications to the apparatus. -55

In summary, we present a mass-producible, 1 cm diameter, single-material (fused silica), polarization-insensitive, chromatic metalens working in the visible wavelength. From MTF and Strehl ratio measurements, we find that the fabricated metalens’ focusing profile is diffraction-limited, even with incomplete 0 to 2π phase coverage in the design and fabrication imperfections, at the cost of focusing efficiency. We believe that the loss of focusing efficiency can be overcome by improving phase coverage using higher-resolution stepper lithography with a shorter wavelength source, such as 198 nm (ArF) DUV projection lithography, 198 nm DUV immersion lithography, or even 13.5 nm extreme-ultraviolet (EUV) lithography. In addition, optimizing the fabrication processes such as ICP-RIE etching conditions to ensure vertical sidewalls, or conversely, implementing detailed structure shapes derived from fabrication in the design step could also further improve the efficiency. We also demonstrate different imaging applications: direct imaging of an AMOLED display as a mock-up for VR imaging and scanning imaging technique applicable for biological imaging. Both techniques show consistent imaging results that agree with the metalens characterization results

Methods. The reticle of the designed lens is written on a photoresist and a Cr-coated 6 in. quartz mask using a DWL2000 laser pattern generator and direct write tool (Heidelberg). The photoresist layer with laser written pattern is developed using the AZ 300 MIF developer (Merck), whose developed pattern is then used as the etch mask for Cr wet etch. The resist layer is stripped and rinsed to ensure a clean surface. Chrome with 100 nm thickness is deposited on RCA cleaned 100 mm fused silica wafers using either sputter deposition or e-beam evaporation. ARC and DUV resist layers on the Cr-coated wafers are formed by spin-coating and baking DUV-24P ARC (Brewer Science) and UV210 resist (Shipley), respectively. The correct focus and dose conditions for the 248 nm wavelength (KrF) DUV exposure are initially predetermined using advanced lithography optimization software (PROLITH, KLA-Tencor), and later fine-tuned through iteration with actual projection lithography processes (PAS 5500/300C DUV Stepper, ASML). Projection lithography of 4:1 reduction is performed with a DUV lens column of 0.63 NA, conventional illumination condition. The exposed substrates are then processed through postexposure bake and develop (AZ 726 MIF, Merck). All coating, baking, and developing are performed using the Suss MicroTech gamma cluster tool to ensure consistent results. The plasma etchings of Cr and SiO are performed on a Trion Minilock III ICP etcher and Oxford PlasmaLab 100 ICP system, respectively.

Focal spot images and images for point Characterization.spread-functions are obtained by using a LensCheck instrument (Optikos Corp.), with fiber-coupled lasers as the light source. Lasers with emission wavelengths at 488 nm (OBIS-488-80LS, Coherent), 532 nm (Ventus 532, Laser Quantum),

633 nm (HNLS008R, Thorlabs), and 660 nm (ROUSB-658- PLR, Ondax) are coupled through a fiber collimator and are used as a light source for the metalens characterization, respectively.

An image of the Harvard logo is AMOLED Screen Imaging.displayed on an AMOLED screen (Galaxy Note 8, Samsung), and the screen is placed approximately at the focus of an infinity-corrected tube lens (TTL180-A, Thorlabs) which is used as a relay lens. The collimated light from the display is refocused to a sCMOS camera sensor array (PCO Panda 4.2, PCO-Tech Inc.) using our metalens. The sCMOS camera is placed on the approximate focal plane of 622 nm wavelength, which is the maximum intensity wavelength of a red pixel in the AMOLED display we used (see the Supporting Information).

Scanning imagings are performed with Scanning Imaging.a He−Ne laser (3225H-PC Laser Tube, 4020 Power Supply, Hughes Aircraft Co.) with a beam diameter of 1 mm, which is 3 times expanded before being deflected by the 2D Galvano mirror system (GVSM002-EC, Thorlabs Inc.). The deflected beam is 2 times expanded using a pair of 2 in. lenses with focal lengths of 125 and 250 mm, respectively, with A and AC coating, respectively. The reflected beam intensity is measured using a photodiode (DET100A2, Thorlabs Inc.), and image reconstruction is performed with a custom-made LabView program.

## ASSOCIATED CONTENT

## \*S Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.nanolett.9b03333.

Schematic, detailed SEM images, Gaussian beam focusing with the metalens, ray-tracing diagrams, diffraction efficiencies, focal spot images, MTF values, LensCheck industrial-quality lens testing instrument, imaging with metalens, scanning imaging apparatus, calculated point spread functions, wavefront map, and Zernike polynomials (PDF)

## AUTHOR INFORMATION

## Corresponding Author

\*E-mail: capasso@seas.harvard.edu.

## ORCID

Joon-Suh Park:

Wei Ting Chen: 0000-0001-8665-9241

Ji-Xin Cheng: 0000-0002-5607-6683

## Author Contributions

S.Z., A.S., and F.C. conceived the study. J.-S.P., S.Z., and A.S. performed the design, simulation, and fabrication process development of the metalens. J.-S.P. fabricated and performed SEM imaging of the metalens. J.-S.P., W.T.C., and K.M.A.Y. performed metalens characterization and developed analysis codes. J.-S.P., W.T.C., P.L., and J.-X.C. performed scanning imaging, and J.-S.P. and W.T.C. performed OLED screen imaging. J.-S.P. and F.C. wrote the manuscript, and all authors discussed the results and commented on the manuscript.

## Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

The authors would like to thank G. Bordonaro, J. Treichler, J. Clark, V. Genova, A. Windsor, and J. Drumheller for their generous help in using CNF facilities. J.-S.P. gratefully acknowledges support from the Korean Government Scholarship Program for Study Overseas. This research was supported by the Defense Advanced Research Projects Agency (Grant no. HR00111810001). This work was performed in part at the Cornell NanoScale Science & Technology Facility (CNF), a member of the National Nanotechnology Coordinated Infra structure (NNCI), which is supported by the National Science Foundation (Grant no. NNCI-1542081). This work was also performed in part at the Center for Nanoscale Systems (CNS), a member of the National Nanotechnology Coordinated Infrastructure Network (NNCI), which is supported by the National Science Foundation under NSF Award no. 1541959. CNS is part of Harvard University.

## REFERENCES

(1) Lan, S.; Zhang, X.; Taghinejad, M.; Rodrigues, S.; Lee, K.-T.; Liu, Z.; Cai, W. ACS Photonics 2019, 6, 864−870.  
(2) Hsiao, H.-H.; Chu, C. H.; Tsai, D. P. Small Methods 2017, 1, 1600064.  
(3) Cheng, D.; Wang, Y.; Hua, H.; Sasian, J. Opt. Lett. 2011, 36, 20982100.  
(4) Sandri, P.; Mazzinghi, P.; Deppo, V. D. Appl. Opt. 2018, 57, 30783087.  
(5) Lee, G.-Y.; Hong, J.-Y.; Hwang, S.; Moon, S.; Kang, H.; Jeon, S.; Kim, H.; Jeong, J.-H.; Lee, B. Nat. Commun. 2018, 9, 1−10.  
(6) She, A.; Zhang, S.; Shian, S.; Clarke, D. R.; Capasso, F. Science Advances 2018, 4, No. eaap9957.  
(7) Shrestha, S.; Overvig, A. C.; Lu, M.; Stein, A.; Yu, N. Light Sci. Appl. 2018, 7, 1−11.  
(8) Smith, T. T. Bur. Stand., Sci. Pap. 1922, 18, 559−584.  
(9) Kidger, M. J. Aberrations. In Fundamentals of Optical Design; SPIE Press: Bellingham, WA, 2001; pp 74−76, Chapter 4.  
(10) Hecht, E. More on Geometrical Optics. In Optics, 5th ed.; Pearson Education, Inc., 2017; pp 258−263, Chapter 6.  
(11) Smith, W. J. Improving a Design. In Modern Lens Design, 2nd ed.; SPIE Press, McGraw-Hill Companies, Inc., 2004; pp 47−69, Chapter 3.  
(12) Yu, N.; Capasso, F. Nat. Mater. 2014, 13, 139−150.  
(13) Genevet, P.; Capasso, F.; Aieta, F.; Khorasaninejad, M.; Devlin, R. Optica 2017, 4, 139−152.  
(14) Arbabi, A.; Horie, Y.; Bagheri, M.; Faraon, A. Nat. Nanotechnol. 2015, 10, 937−943.  
(15) Kildishev, A. V.; Boltasseva, A.; Shalaev, V. M. Science 2013, 339, 1232009.  
(16) Sun, S.; He, Q.; Hao, J.; Xiao, S.; Zhou, L. Adv. Opt. Photonics 2019, 11, 380−479.  
(17) Khorasaninejad, M.; Capasso, F. Science 2017, 358, No. eaam8100.  
(18) Yu, N.; Genevet, P.; Kats, M. A.; Aieta, F.; Tetienne, J.-P.; Capasso, F.; Gaburro, Z. Science 2011, 334, 333−337.  
(19) Chen, W. T.; Zhu, A. Y.; Sisler, J.; Huang, Y.-W.; Yousef, K. M. A.; Lee, E.; Qiu, C.-W.; Capasso, F. Nano Lett. 2018, 18, 7801-7808  
(20) Sawant, R.; Bhumkar, P.; Zhu, A. Y.; Ni, P.; Capasso, F.; Genevet. P. Adv. Mater. 2019. 31. 1805555.  
(21) Chen, W. T.; Zhu, A. Y.; Sanjeev, V.; Khorasaninejad, M.; Shi, Z.; Lee, E.; Capasso, F. Nat. Nanotechnol. 2018, 13, 220−226.  
(22) Wang, S.; Wu, P. C.; Su, V.-C.; Lai, Y.-C.; Chu, C. H.; Chen, J.- W.; Lu, S.-H.; Chen, J.; Xu, B.; Kuan, C.-H.; et al. Nat. Commun. 2017, 8, 1−9.  
(23) Ding, J.; An, S.; Zheng, B.; Zhang, H. Adv. Opt. Mater. 2017, 5, 1700079.  
(24) Shi, Z.; Khorasaninejad, M.; Huang, Y.-W.; Roques-Carmes, C.; Zhu, A. Y.; Chen, W. T.; Sanjeev, V.; Ding, Z.-W.; Tamagnone, M.; Chaudhary, K.; et al. Nano Lett. 2018, 18, 2420−2427.  
(25) Sun, S.; He, Q.; Xiao, S.; Xu, Q.; Zhou, L. Nat. Mater. 2012, 11, 426−431.  
(26) Chen, X.; Huang, L.; Mühlenbernd, H.; Li, G.; Bai, B.; Tan, Q.; Jin, G.; Qiu, C.-W.; Zhang, S.; Zentgraf, T. Nat. Commun. 2012, 3, 1− 6.  
(27) Balthasar Mueller, J. P.; Rubin, N. A.; Devlin, R. C.; Groever, B.; Capasso, F. Phys. Rev. Lett. 2017, 118, 113901.  
(28) Rubin, N. A.; Zaidi, A.; Juhl, M.; Li, R. P.; Mueller, J. P. B.; Devlin, R. C.; Leosson, K.; Capasso, F.́ Opt. Express 2018, 26, 21455.  
(29) Devlin, R. C.; Ambrosio, A.; Rubin, N. A.; Mueller, J. P. B.; Capasso, F. Science 2017, 358, 896901.  
(30) Huang, Y.-W.; Rubin, N. A.; Ambrosio, A.; Shi, Z.; Devlin, R. C.; Qiu, C.-W.; Capasso, F. Opt. Express 2019, 27, 7469.  
(31) Balthasar Mueller, J. P.; Leosson, K.; Capasso, F. Optica 2016, 3, 42.  
(32) Juhl, M.; Mendoza, C.; Mueller, J. P. B.; Capasso, F.; Leosson, K. Opt. Express 2017, 25, 28697.  
(33) Arbabi, E.; Kamali, S. M.; Arbabi, A.; Faraon, A. ACS Photonics 2018, 5, 31323140.  
(34) Rubin, N. A.; D’Aversa, G.; Chevalier, P.; Shi, Z.; Chen, W. T.; Capasso, F. Science 2019, 365, No. eaax1839.  
(35) Decker, M.; Chen, W. T.; Nobis, T.; Zhu, A. Y.; Khorasaninejad, M.; Bharwani, Z.; Capasso, F.; Petschulat, J. ACS Photonics 2019, 6, 1493−1499.  
(36) Phan, T.; Sell, D.; Wang, E. W.; Doshay, S.; Edee, K.; Yang, J.; Fan, J. A. Light: Sci. Appl. 2019, 8, 48.  
(37) She, A.; Zhang, S.; Shian, S.; Clarke, D. R.; Capasso, F. Opt. Express 2018, 26, 1573.  
(38) Fan, Z.-B.; Shao, Z.-K.; Xie, M.-Y.; Pang, X.-N.; Ruan, W.-S.; Zhao, F.-L.; Chen, Y.-J.; Yu, S.-Y.; Dong, J.-W. Phys. Rev. Appl. 2018, 10, 014005.  
(39) Briere, G.; Ni, P.; Hè ron, S.; Chenot, S.; Vé zian, S.; Brá ndli, V.;̈ Damilano, B.; Duboz, J.-Y.; Iwanaga, M.; Genevet, P. Adv. Opt. Mater. 2019, 7, 1801271.  
(40) Hu, T.; Tseng, C.-K.; Fu, Y. H.; Xu, Z.; Dong, Y.; Wang, S.; Lai, K. H.; Bliznetsov, V.; Zhu, S.; Lin, Q.; et al. Opt. Express 2018, 26, 19548.  
(41) Aieta, F.; Genevet, P.; Kats, M.; Capasso, F. Opt. Express 2013, 21, 31530.  
(42) Devlin, R. C.; Khorasaninejad, M.; Chen, W. T.; Oh, J.; Capasso, F. Proc. Natl. Acad. Sci. U. S. A. 2016, 113, 10473−10478.  
(43) Li, Q.-T.; Dong, F.; Wang, B.; Chu, W.; Gong, Q.; Brongersma, M. L.; Li, Y. ACS Photonics 2017, 4, 2544−2549.  
(44) Geary, J. M. Petzval Lens. In Introduction to Lens Design with Practical ZEMAX Examples; Willmann-Bell, Inc.: Richmond, VA, 2011; pp 382−387, Chapter 33.  
(45) Goodman, J. W. Frequency Analysis of Optical Imaging Systems. In Introduction to Fourier Optics, 4th ed.; W.H. Freeman and Company; New York, NY, 2017; pp 185−230, Chapter 7.  
(46) Smith, W. J. Evaluation: How Good is This Design? In Modern Lens Design, 2nd ed.; SPIE Press, McGraw-Hill Companies, Inc., 2004; pp 71−84, Chapter 4.  
(47) Shannon, C. E. Proc. IRE 1949, 37, 10−21.  
(48) Andre, M.́ Rev. Opt. 1947, 2, 257−277.  
(49) Chen, W. T.; Khorasaninejad, M.; Zhu, A. Y.; Oh, J.; Devlin, R. C.; Zaidi, A.; Capasso, F. Light: Sci. Appl. 2017, 6, e16259−e16259.  
(50) Chen, W. T.; Zhu, A. Y.; Sisler, J.; Bharwani, Z.; Capasso, F. Nat. Commun. 2019. 10. 355.  
(51) Patil, C. A.; Arrasmith, C. L.; Mackanos, M. A.; Dickensheets, D. L.; Mahadevan-Jansen, A. Biomed. Opt. Express 2012, 3, 488.  
(52) Yin, C.; Glaser, A. K.; Leigh, S. Y.; Chen, Y.; Wei, L.; Pillai, P. C. S.; Rosenberg, M. C.; Abeytunge, S.; Peterson, G.; Glazowski, C.; et al. Biomed. Opt. Express 2016, 7, 251.  
(53) Chen, Y.; Wang, D.; Khan, A.; Wang, Y.; Borwege, S.; Sanai, N.; Liu, J. T. C. J. Biomed. Opt. 2015, 20, 106011.  
(54) Arrasmith, C. L.; Dickensheets, D. L.; Mahadevan-Jansen, A. Opt. Express 2010, 18, 3805−3819.  
(55) Wang, Y.; Raj, M.; McGuff, H. S.; Bhave, G.; Yang, B.; Shen, T.; Zhang, X. J. Micromech. Microeng. 2012, 22, 065001.