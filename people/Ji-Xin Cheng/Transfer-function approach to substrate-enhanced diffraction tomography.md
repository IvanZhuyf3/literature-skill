## OPTICA

# Transfer-function approach to substrate-enhanced diffraction tomography

Tongyu Li,1 Yi Shen,1 Dashan Dong,1 Danchen Jia,1 Jianpeng Ao,1 Ji-Xin Cheng,1,2 AND Lei Tian1,2,\*

1Department of Electrical and Computer Engineering, Boston University, Boston, Massachusetts 02215, USA

2Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, USA

\*leitian@bu.edu

Received 30 September 2025; revised 26 January 2026; accepted 23 February 2026; published 1 April 2026

Forward and backward scattering provide complementary volumetric and interfacial information, yet conventional three-dimensional (3D) imaging typically accesses only one. We present a substrate-enhanced diffraction tomography approach that simultaneously recovers both channels under multi-angle epi-illumination. This geometry captures one forward- and two backward-scattering bands in axially symmetric Fourier regions, where their complementary coverage enables phase–absorption separation in a non-Hermitian spectrum. Explicit 3D transfer functions are derived for both channels, and an axial Kramers–Kronig relation is established to incorporate substrate-induced boundary conditions in a unified framework. Our results establish a label-free, high-resolution 3D imaging modality that surpasses the limits of existing methods. © 2026 Optica Publishing Group under the terms of the Optica Open Access Publishing Agreement

https://doi.org/10.1364/OPTICA.580672

## 1. INTRODUCTION

3D imaging through a finite numerical aperture (NA) objective lens is fundamentally constrained by anisotropic spatial bandwidth, yielding high lateral but poor axial resolution. Forward scattering (FS) predominantly encodes volumetric information but suffers from the missing-cone problem, where high-axialfrequency components are inaccessible [1]. Backward scattering (BS), in contrast, carries high-frequency interfacial features but does not provide quantitative volumetric information [2,3]. These channels are inherently complementary, yet are conventionally probed in separate transmission or reflection geometries [4,5]. Extending the accessible 3D scattering spectrum is thus essential for accurate characterization, but existing solutions, such as dual opposing objective lenses [6], mechanical sample rotation [7–9], or engineered reflectors [10], remain impractical.

Among these strategies, a reflective substrate (e.g., a mirror) offers an efficient means of folding counter-propagating scattering fields into a common pupil, effectively emulating opposing objectives within a single-objective geometry [11]. Under appropriate NA conditions, such configurations can, in principle, approach 4Pi tomographic bandwidth [12]. Building on this concept, we advance a substrate-enhanced diffraction tomography technique that simultaneously captures FS and BS from intensity-only measurements [13,14] using a multi-angle epi-illumination configuration [12,15–17]. This configuration further eliminates the need for a dedicated interferometric path and effectively forms a dual-view acquisition [18], expanding the accessible 3D spatial frequency bandwidth threefold [Fig. 1(a)]. In this arrangement, both channels interfere with the reflected incidence, providing a natural self-reference that enables quantitative phase reconstruction from intensity-only measurements. This substrate-enhanced acquisition strategy provides access to axially symmetric Fourier bands—one corresponding to FS and two to BS—whose complementary coverage enables phase–absorption separation in a non-Hermitian spatial frequency spectrum. In contrast, conventional reflection geometries capture only a single BS band, which is insufficient for such separation [3,19].

A central challenge in recovery is that FS and BS contributions from different depths overlap in the recorded 2D intensity patterns. To disentangle them, we employ diffraction tomography with angle-diverse measurements [Figs. 1(b) and 1(c)], which reconstructs the 3D scattering potential by solving an inverse scattering problem. Our previous work employed the modified Born series (MBS) [20] for this task [17], and while effective, such rigorous models, including the discrete dipole approximation [12,21], require computationally intensive iterative reconstructions that obscure physical insight. To address this, we derive explicit 3D transfer functions under the first-Born approximation, which establish a linear relationship between the measured intensity and the underlying scattering potential. These transfer functions confine the reconstruction to the physical passbands, substantially reducing computational cost. Moreover, the Kramers–Kronig (KK) relation, originally established in the temporal domain, has recently been extended to the lateral spatial domain for efficient phase retrieval [22,23]. Here, we further exploit the spatial causality of scattering in the presence of a reflective substrate to establish a new axial KK relation, which constrains the inversion of the half-space scattering problem. Together, this transfer-function framework provides a clearer and more tractable alternative to the iterative MBS model, enabling efficient separation and recovery of 3D FS and BS information, as validated in simulation and experiment.

![](images/2288a23d7eb21b9409d947c9aab98012c8c8471566e1d42f6c9495e94411b043.jpg)

<details>
<summary>text_image</summary>

(a)
Transmission
Missing Cone
k_z
k_x
k_y
Substrate-Epi
k_z
k_x
k_y
</details>

![](images/33ed35338d789d5de24d1ee4073ec075608103a79ead864176325fbf361632d2.jpg)

<details>
<summary>text_image</summary>

(b)
k_{y,in} → k_{ll,in}
(c)
ψ_{0+} ← (~f~)²
BS
FS
BS
Δε(r)
ψ_{0-}
r_∥
z
(d)
x
l(r_∥, k_{ll,in})
y
k_{ll,in}
k_{ll,in}
(e)
k_z
B_z
∑_{k_z} k_x
k_y
B_x
⊗
k_z
k_x
k_y
Δε(k)
H(k; k_{ll,in})
\tilde{l}(k_∥, k_{ll,in})
</details>

Fig. 1. (a) Passbands in transmission and substrate-enhanced epi configurations; the latter simultaneously records FS and BS, expanding the accessible spectrum threefold. (b) Angle-diverse illumination with varying $\mathbf { k } _ { \parallel , \mathrm { i n } }$ enables retrieval of 3D FS and BS. (c) Substrate-enhanced epi-illumination schematic, the incident field and its substrate reflection act as dual illuminations generating FS and BS. (d) Representative intensity patterns measured under different illumination angles. (e) Linear scattering model expressed via the 3D transfer function.

## 2. THEORY AND METHOD

Consider a 3D weakly scattering object immersed in a medium permittivity $\epsilon _ { \mathrm { m } }$ above a reflective substrate, characterized by a permittivity perturbation $\Delta \epsilon ( { \bf r } ) = \epsilon ( { \bf r } ) - \epsilon _ { \mathrm { m } } .$ . The substrate surface is defined as the $z = 0$ plane, with its optical response described by a Fresnel coefficient $R ( \mathbf { k } _ { | | } )$ . An obliquely incident plane wave $\psi _ { 0 , + } = e ^ { i ( \mathbf { k } _ { \| , \mathrm { i n } } \cdot \mathbf { r } _ { \| } + k _ { z , \mathrm { i n } } z ) }$ with unit amplitude, propagating with $k _ { z , \mathrm { i n } }$ along the positive z-direction, illuminates the object and substrate, as illustrated in Fig. 1(c).

Under the single-scattering approximation, the reflective substrate first reflects the incidence back toward the object, generating a secondary incidence, $\psi _ { 0 , - } = R ( { \bf k } _ { \parallel , \mathrm { i n } } ) e ^ { i ( { \bf k } _ { \parallel , \mathrm { i n } } \cdot { \bf r } _ { \parallel } - k _ { z , \mathrm { i n } } z ) }$ , forming a standing-wave illumination. Each incidence scatters at every depth, producing FS along the incidence (gray dashed line) and BS along the opposite direction (light blue dashed line). For $\psi _ { 0 , + }$ (purple arrows), FS $( \psi _ { \mathrm { F S , + } } )$ ) propagates along +z and BS $( \psi _ { \mathrm { { B S } , + } } )$ along −z. For $\psi _ { 0 , - }$ (blue arrows), FS $( \psi _ { \mathrm { F S , - } } )$ propagates along −z while BS $( \psi _ { \mathrm { { B S } , - } } )$ propagates along +z. Scattered fields propagating along −z are directly collected, while +z-propagating fields first reach the substrate, reflect at $z = 0$ to reverse the direction, and then enter the objective. In total, the model includes four scattered field components: $\psi _ { \mathrm { F S , - } }$ and $\psi _ { \mathrm { B S , + : } }$ corresponding to the FS and BS of the real image, and $\psi _ { \mathrm { F S , + } }$ and $\psi _ { \mathrm { { B S , - } } } ,$ corresponding to the FS and BS of the virtual image generated by substrate reflection.

Without loss of generality [17], the objective’s focal plane is set at $z = 0$ . The microscope effectively applies a Fourier filter to the field through its pupil function $P ( \mathbf { k } _ { | | } )$ . The secondary incidence $\psi _ { 0 , }$ − interferes with all four scattered field components to form the measured intensity pattern $I _ { { \bf k } _ { \parallel , \mathrm { i n } } } ( { \bf r } _ { \parallel } )$ . Under the weak-scattering condition, the cross terms provide the main interference contrast, establishing a linear relation between the permittivity contrast and the intensity spectrum [24]:

$$
\tilde {I} _ {\mathbf {k} _ {\parallel , \mathrm{in}}} (\mathbf {k} _ {\parallel}) \approx \tilde {I} _ {0, \mathbf {k} _ {\parallel , \mathrm{in}}} + \int_ {- \infty} ^ {0} \mathbf {H} _ {\parallel , \mathbf {k} _ {\parallel , \mathrm{in}}} (\mathbf {k} _ {\parallel}, z) \widetilde {\Delta \epsilon} _ {\parallel} (\mathbf {k} _ {\parallel}, z) \cdot \mathrm{d} z, \tag {1}
$$

where $\mathbf { H } _ { \parallel } = [ H _ { \parallel , \mathrm { R e } } , H _ { \parallel , \mathrm { I m } } ]$ denotes the slice-wise transfer function, $\widetilde { \Delta \star } _ { \parallel } = [ \widetilde { \Delta \epsilon } _ { \parallel , \mathrm { R e } } , \widetilde { \Delta \epsilon } _ { \parallel , \mathrm { I m } } ] ^ { \top }$ is the 2D spectrum of each slice, and $\tilde { I } _ { 0 , \mathbf { k } _ { \parallel , \mathrm { i n } } }$ is the direct current component, which can be removed by background subtraction [24].

Unlike transmission geometry, where scattering occurs throughout the space unless previously bounded, the epiconfiguration restricts the object to the upper half-space $( z < 0 )$ , leaving the region $\relax z > 0$ free of scatterers. This asymmetry prevents a direct definition of a full 3D transfer function. However, the substrate-imposed cutoff naturally enforces a spatial causality constraint, where the scattering potential is confined to one half-space in real space, and its Fourier dual is analyticity in $k _ { z }$ . This analyticity ensures that all scattered fields originate from the physical half-space and leads to an axial KK relation, linking the real and imaginary parts of $\widetilde { \Delta \epsilon }$ through a Hilbert transform $\mathcal { \bar { H } } _ { z }$ along $k _ { z }$ :

$$
\mathrm{Im} [ \widetilde {\Delta \epsilon} (\mathbf {k}) ] = \frac {1}{\pi} \mathrm{p.v.} \int_ {- \infty} ^ {\infty} \frac {\mathrm{Re} [ \widetilde {\Delta \epsilon} (\mathbf {k} _ {\parallel} , k _ {z} ^ {\prime}) ]}{k _ {z} - k _ {z} ^ {\prime}} \mathrm{d} k _ {z} ^ {\prime}, \tag {2}
$$

where p.v. denotes the Cauchy principal value, in direct analogy to the temporal KK relations that connect a material’s dispersive permittivity to causality.

We make this property explicit by expressing $\Delta \epsilon ( { \bf r } ) $ $S ( z ) \Delta \epsilon ( \mathbf { r } )$ , where $S ( z )$ is a step function enforcing analyticity [Figs. 2(a) and 2(b)]. This formalizes the causal nature of the scattering process and permits the integral in Eq. (1) to be extended over the entire space (−∞, ∞) without changing the physical content. Using the Parseval–Plancherel identity, scattering from an object above a reflective substrate can then be expressed linearly through a 3D transfer function:

$$
\tilde {I} _ {\mathbf {k} _ {\parallel , \mathrm{in}}} (\mathbf {k} _ {\parallel}) \approx \tilde {I} _ {0, \mathbf {k} _ {\parallel , \mathrm{in}}} + \int_ {- \infty} ^ {\infty} \mathbf {H} _ {\mathbf {k} _ {\parallel , \mathrm{in}}} (\mathbf {k}) \widetilde {\Delta \epsilon} (\mathbf {k}) \cdot \mathrm{d} k _ {z}, \tag {3}
$$

where

$$
H _ {\mathrm{Re}, \mathbf {k} _ {\parallel , \text { in }}} (\mathbf {k}) = \frac {i k _ {0} ^ {2}}{2} \left[ H _ {0, \mathbf {k} _ {\parallel , \text { in }}} (\mathbf {k}) - H _ {0, \mathbf {k} _ {\parallel , \text { in }}} ^ {*} (- \mathbf {k}) \right], \tag {4a}
$$

$$
H _ {\mathrm{Im}, \mathbf {k} _ {\parallel , \text { in }}} (\mathbf {k}) = - \frac {k _ {0} ^ {2}}{2} \left[ H _ {0, \mathbf {k} _ {\parallel , \text { in }}} (\mathbf {k}) + H _ {0, \mathbf {k} _ {\parallel , \text { in }}} ^ {*} (- \mathbf {k}) \right], \tag {4b}
$$

where $H _ { 0 , { \mathbf { k } _ { \parallel , \mathrm { i n } } } } ( \mathbf { k } )$ contains the essential contributions, consisting of two FS and two BS components:

$$
H _ {0, \mathbf {k} _ {\parallel , \text {in}}} (\mathbf {k}) = \frac {R ^ {*} \left(\mathbf {k} _ {\parallel , \text {in}}\right) P ^ {*} \left(\mathbf {k} _ {\parallel , \text {in}}\right) P \left(\mathbf {k} _ {\parallel} + \mathbf {k} _ {\parallel , \text {in}}\right)}{k _ {\perp} \left(\mathbf {k} _ {\parallel} + \mathbf {k} _ {\parallel , \text {in}}\right)} \left(H _ {\mathrm{FS}} + H _ {\mathrm{BS}}\right), \tag {5}
$$

with the FS and BS components

$$
H _ {\mathrm{FS}} = R (\mathbf {k} _ {\parallel} + \mathbf {k} _ {\parallel , \text { in }}) \delta_ {\mathrm{FS}, +} + R (\mathbf {k} _ {\parallel , \text { in }}) \delta_ {\mathrm{FS}, -}, \tag {6a}
$$

$$
H _ {\mathrm{BS}} = \delta_ {\mathrm{BS}, +} + R (\mathbf {k} _ {\parallel , \text { in }}) R (\mathbf {k} _ {\parallel} + \mathbf {k} _ {\parallel , \text { in }}) \delta_ {\mathrm{BS}, -}, \tag {6b}
$$

where $k _ { \perp } ( { \bf k } _ { \parallel } + { \bf k } _ { \parallel , \mathrm { i n } } ) \equiv [ \epsilon _ { \mathrm { m } } k _ { 0 } ^ { 2 } - ( { \bf k } _ { \parallel } + { \bf k } _ { \parallel , \mathrm { i n } } ) ^ { 2 } ] ^ { 1 / 2 } , \quad \delta _ { \mathrm { F S } , + / - } \equiv$ $\delta [ k _ { z } \mp k _ { \perp } ( \mathbf { k } _ { \parallel } + \mathbf { k } _ { \parallel , \mathrm { i n } } ) \pm k _ { z , \mathrm { i n } } ] ,$ , and $\delta _ { \mathrm { B S , + / - } } \equiv \delta [ k _ { z } \pm k _ { \perp }$ ⊥(kk + $\mathbf { k } _ { \parallel , \mathrm { i n } } ) \pm k _ { z , \mathrm { i n } } ]$ . Details are shown in Supplement 1.

Equations (4a) and (4b) show that $\bar { \Delta \epsilon } _ { \mathrm { R e } } ( { \bf k } )$ and $\widetilde { \Delta \epsilon } _ { \mathrm { I m } } ( \mathbf { k } )$ are encoded asymmetrically in the Fourier domain: $H _ { \mathrm { R e } , \mathbf { k } _ { \parallel , \mathrm { i n } } }$ is imaginary and anti-symmetric, while $H _ { \mathrm { I m } , \mathbf { k } _ { \parallel , \mathrm { i n } } }$ is real and symmetric. The substrate effectively doubles the accessible Fourier domain along $k _ { z }$ by folding +z-propagating FS and BS components into the pupil, effectively forming a dual-view acquisition. This yields four $\delta _ { \mathrm { F S / B S , + / - } }$ terms that define Ewald spherical caps centered at $\mathbf { k } _ { \parallel , \mathrm { i n } } .$ , truncated by the NA, and separated symmetrically along $k _ { z } ,$ , forming Fourier pairs that enable separation of phase and absorption in both FS and BS from any non-Hermitian spectrum [Eqs. (6a) and (6b); Fig. 1(e)].

This asymmetry and separation imply that phase and absorption, as well as FS and BS contributions, are inherently decoupled and thus separable during retrieval. As the illumination angle varies, FS and BS caps sweep through the Fourier domain and fill their respective supports [Fig. 1(a)], yielding three isolated bands with lateral bandwidths $B _ { x } = B _ { \nu } = 4 \mathrm { N A } \cdot k _ { 0 }$ and axial bandwidth $B _ { z } = 2 \epsilon _ { \mathrm { m } } ^ { 1 / 2 } k _ { 0 } ( 1 - \sqrt { 1 - \mathrm { N A } ^ { 2 } / \epsilon _ { \mathrm { m } } } )$ [25]. Two BS bands (green) and the FS band (gray) are highlighted in Fig. 1(e).

The inverse scattering problem seeks to recover the unknown $\Delta \epsilon ( \mathbf { r } )$ of the object from a series of angle-diverse measurements. The forward model, defined in Eq. (3), is linear and decouples across in-plane spatial frequencies kk. In the discrete formulation, we assume sampling in all three dimensions meets the Nyquist criterion imposed by the respective bandwidths.

At a given kk, the key challenge is to disentangle FS and BS components, which are superimposed in the forward model. To address this, we collect the full stack of M angle-diverse measurements, leading to a discrete linear system [Fig. 1(e)]:

$$
\mathbf {A} (\mathbf {k} _ {\parallel}) \widetilde {\Delta \epsilon} (\mathbf {k} _ {\parallel}) = \tilde {\mathbf {I}} (\mathbf {k} _ {\parallel}), \tag {7}
$$

where $\tilde { \mathbf { I } } ( \mathbf { k } _ { \| } ) \in \mathbb { C } ^ { M \times 1 }$ is the column vector of measured intensity spectra at $\mathbf { k } _ { \| } , \widetilde { \Delta \epsilon } ( \mathbf { k } _ { \| } ) \in \mathbb { C } ^ { 2 N \times 1 }$ , given by $\begin{array} { r l } & { [ \widetilde { \Delta \epsilon } _ { \mathrm { R e } } ^ { \top } ( { \bf k } _ { \parallel } ) , \widetilde { \Delta \epsilon } _ { \mathrm { I m } } ^ { \top } ( { \bf k } _ { \parallel } ) ] ^ { \top } } \end{array}$ , contains the unknown Fourier components of the permittivity contrast within the passband (for N axial frequency components), and forward operator $ { \mathbf { A } } \in \mathbb { C } ^ { M \times 2 N }$ mapping 1 to the measurement spectra across all illuminations:

$$
\mathbf {A} \equiv (\mathbf {H} _ {\mathrm{Re}}, \mathbf {H} _ {\mathrm{Im}}) \left( \begin{array}{c c} (1 + i \mathcal {H} _ {z}) / 2 & 0 \\ 0 & (1 + i \mathcal {H} _ {z}) / 2 \end{array} \right), \tag {8}
$$

where the axial KK relation in Eq. (2) is imposed by invoking the identity $( 1 + i \mathcal { H } _ { z } ) \widetilde { \Delta \star } ( { \bf k } _ { \parallel } ) / 2 = \widetilde { \Delta \star } ( { \bf k } _ { \parallel } )$ . In practice, we apply discrete Fourier transforms (DFTs) to the discretized slice-wise transfer functions [Eq. (1)] to compute the 3D transfer function. This approach is numerically more stable than direct discretization of Eqs. (4a) and (4b), as it naturally enforces the Nyquist bandlimit and properly handles cases where delta locations fall off the Fourier sampling grid. Example 3D transfer functions are shown in Fig. 2(c), and details are shown in Supplement 1.

To validate the forward model, we simulated scattering from a synthetic object placed above a mirror under oblique illumination [Fig. 2(a)]. A mirror is used as the substrate to maximize collection efficiency, with the Fresnel coefficient $R ( { \bf k } _ { \parallel } ) = - 1$ . The object consists of randomly distributed beads confined to a thin spherical shell (radius 3 µm and thickness 100 nm) with volume fraction $\rho = 1 0 \% - 4 0 \%$ and permittivity contrast $\Delta \varepsilon = 0 - 0 . 2$ on a background of $\epsilon _ { \mathrm { m } } = 1 . 8 0$ , illuminated by a 632 nm plane wave with ${ \bf k } _ { \parallel , \mathrm { i n } } = ( 0 . 6 k _ { 0 } , 0 )$ . The normalized root-mean-square error (NRMSE) between the computed patterns using the transfer function approach and the rigorous MBS model [Fig. 2(d)] remains below 0.3 across all tested parameters, confirming that Eq. (3) accurately captures both forward- and backward-scattered fields. Representative patterns at $\Delta \epsilon = 0 . 0 5$ , 0.1, and 0.15 (inset) show that Eq. (3) reproduces the interference features of the rigorous MBS model with consistent contrast variations as 1 increases. The error grows nearly linearly with $\Delta \epsilon$ , reflecting stronger multiple scattering beyond the single-scattering regime, yet remains quantitatively reliable for typical biomedical imaging conditions.

![](images/8c7caa68bfee597d18bc574c979ff03ee8a40fa61589bdad1f3076d5c77a4025.jpg)

<details>
<summary>text_image</summary>

(a)
L=10 µm
y
x
z
εm=1.80
Δε
S(z)
×1
×0
z
</details>

2 (b)

![](images/93a3630478683772e8a21a9f3118eac9d044a081f80e93af2d7a05a2f6438ede.jpg)

<details>
<summary>line chart</summary>

| f_z    | Δξ     |
| ------ | ------ |
| -2/λ   | ~0     |
| 0      | ~1     |
| 2/λ    | ~0     |
</details>

![](images/8eb898060469e95046a5085381de544ee4d06ec5ac81e0e7869e15107e8c1979.jpg)

<details>
<summary>scatterplot</summary>

| k/km | Re(Hm) | Im(HRe) |
|------|--------|---------|
| -2   | 0      | 0       |
| 0    | 0      | 0       |
| 2    | 0      | 0       |
</details>

![](images/f10714395f9ecb0e2c4c079c49920f66db988298c175d32826fd1a798711189c.jpg)

<details>
<summary>line chart</summary>

| Δε   | NRMSE (kν/km = 0) | NRMSE (kν/km = 2.5) | NRMSE (kν/km = 40%) |
|------|-------------------|---------------------|---------------------|
| 0.00 | 0.00              | 0.00                | 0.00                |
| 0.05 | ~0.08             | ~0.10               | ~0.12               |
| 0.10 | ~0.12             | ~0.15               | ~0.18               |
| 0.15 | ~0.16             | ~0.20               | ~0.24               |
| 0.20 | ~0.20             | ~0.25               | ~0.30               |
</details>

Fig. 2. (a) Synthetic object above a mirror substrate. The mirror acts as a step function, enforcing causality in the scattering spectra. (b) Real and imaginary parts of the normalized object spectrum at $\mathbf { \tilde { k } } _ { | | } = ( 0 , 0 )$ ; yellow points show $\mathcal { H } _ { z } [ \mathrm { R e } ( \widetilde { \Delta \epsilon } ) ]$ matching Im(1) , demonstrating the axial KK relation. $\left( \mathrm { c } \right) k _ { x } - k _ { z }$ profile of the 3D transfer function for $\mathrm { _ { 4 0 . 9 5 N A } }$ under NA-matched incidence, $k _ { \mathrm { m } } = \epsilon _ { \mathrm { m } } ^ { 1 / 2 } k _ { 0 }$ . (d) NRMSE between the transfer function and MBS models as a function of 1 and volume fraction; insets show representative computed patterns at increasing 1.

For recovering 3D FS and BS information, the linear forward model enables efficient non-iterative inversion, while the axial KK relation enforces spatial causality as a physical prior, confining the solution to the upper half-space. For practical implementation, rather than discretizing the entire real space at the Nyquist limit as required by our previous MBS method [17], the axial separation of FS and BS components in the 3D Fourier space allows a band-limited reconstruction confined to the three Fourier domain supports illustrated in Fig. 1(e). This restriction reduces the dimensionality of the forward operator A to the axial passband, substantially lowering the memory cost of inversion. The inverse is computed using truncated singular value decomposition, with $\mathbf { A } ^ { + } \approx \mathbf { V } \mathbf { \bar { Z } } _ { \alpha } ^ { - 1 } \mathbf { U } ^ { \dagger }$ constructed by discarding singular values below a tunable threshold α, thereby suppressing low signal-tonoise (SNR) modes while preserving the dominant scattering components, providing regularization analogous to an $l _ { 2 } { \mathrm { - t y p e } }$ constraint.

## 3. NUMERICAL VALIDATION

## A. Complementary FS–BS Contrast and Phase–Absorption Separation

We first validate the method in simulation using an object with $| \Delta \epsilon | = 2 . 7 \times 1 0 ^ { - 2 }$ , consisting of three beads (radius 1 µm) embedded in a thin spherical shell (radius $6 . 5$ µm and thickness 100 nm) on a background of $\epsilon _ { \mathrm { m } } = 1 . 8 0$ , as shown in Fig. $3 ( \mathrm { a } )$ . The beads are used to evaluate the spatial elongation, while the shell interfaces provide strong sensitivity to BS. The top bead and upper half-shell are purely absorptive $( \Delta \epsilon _ { \mathrm { I m } } \neq 0$ and $\Delta \epsilon _ { \mathrm { R e } } = 0 )$ , whereas the bottom beads and lower half-shell are purely phase objects $( \Delta \epsilon _ { \mathrm { R e } } \neq 0$ and $\Delta \epsilon _ { \mathrm { I m } } = 0 )$ . Angle-diverse intensity measurements are simulated using the rigorous MBS model with 150 illumination angles at 632 nm, sampled along a Fermat’s spiral and spanning a maximum illumination angle of 0.95, with simulation details shown in Supplement 1. The reconstruction results under substrate-enhanced geometry using the proposed method are shown in Figs. 3(d)–3(f ). For comparison, the reflection-only reconstruction from simulations without the substrate is shown in Figs. 3(b) and 3(c).

In the substrate-enhanced geometry, three recovered bands are assembled into the 3D Fourier spectrum after inversion. Figure 3(d) shows the $k _ { x } { - } k _ { z }$ cross-section of the logarithmic Fourier spectrum, while the $k _ { x } = 0 . 5 k _ { \mathrm { m } }$ slice on the right confirms the axial KK relation of the recovered spectrum.

Because the spectrum is non-Hermitian, regions symmetric about the axial frequency $k _ { z }$ must be combined to decouple phase and absorption. For the FS band, centered at zero frequency with support inherently symmetric about $k _ { z } = 0 ;$ , this symmetry alone suffices for decoupling, corresponding to $\Delta \epsilon _ { \mathrm { { F S } } }$ in real space. By contrast, BS bands occupy two distinct high-frequency regions symmetric about the $k _ { z }$ axis in substrate-enhanced geometry; both must be combined to achieve decoupling, with their real and imaginary parts (Re $\Delta \epsilon _ { \mathrm { B S } }$ and Im $\Delta \epsilon _ { \mathrm { B S } } )$ in real space encoding high ${ - } k _ { z }$ phase and absorption, respectively. The spectral gap between two BS bands introduces oscillations in z-profiles. To obtain smooth BS z-profiles, a single BS band is isolated, and its magnitude, $| \Delta \epsilon _ { \mathrm { B S } , s \mathrm { b } } |$ , gives the oscillation envelope. Accordingly, a single BS band is used for z-profiles, whereas both bands are combined for phase–absorption decoupling or for $x { - } y$ crosssections. In contrast, the reflection-only geometry without the substrate accesses only a single BS band [Fig. 3(b)] and therefore cannot separate the phase and absorption contributions in the reconstruction.

Figures 3(e) and 3(f ) show the $x { - } \mathcal { Z }$ cross-sections of reconstructed $\Delta \epsilon _ { \mathrm { F S } }$ and $\Delta \epsilon _ { \mathrm { B S } }$ obtained using substrate-enhanced geometry. Since the reconstructed spectra obey the axial KK relation along $k _ { z } ,$ both $\Delta \epsilon _ { \mathrm { F S } }$ and $\Delta \epsilon _ { \mathrm { B S } }$ are confined to the upper half-space $( z < 0 )$ ; for clarity, the $\relax z > 0$ regions, which are nearly zero, are truncated in Figs. 3(e) and 3(f ).

The reconstructed $\Delta \epsilon _ { \mathrm { F S } }$ reveals smooth volumetric features similar to transmission, offering high lateral resolution but suffering from axial elongation and blurred boundaries due to the missing-cone in the low-frequency region [white shading in Fig. 3(d)], with real and imaginary parts corresponding to phase (left) and absorption (right), respectively. The absence of high-kz components causes the top and bottom shell interfaces to vanish in $\Delta \epsilon _ { \mathrm { F S } } .$ . In contrast, the recovered $\Delta \epsilon _ { \mathrm { B S } }$ shows enhanced sensitivity to lateral interfaces, as shown in Fig. 3(f ) and its inset, effectively recovering the missing boundaries of the shell and thereby complementing the FS information.

Phase–absorption separation is evident in $\Delta \epsilon _ { \mathrm { F S } }$ and $\Delta \epsilon _ { \mathrm { B S } }$ under the substrate-enhanced geometry. In particular, for $\Delta \epsilon _ { \mathrm { B S } }$ , the real component predominantly captures phase interfaces, while the imaginary component captures absorptive interfaces. A continuous envelope combining both interfaces is shown in $| \Delta \epsilon _ { \mathrm { B S } , s \mathrm { b } } |$ . For comparison, the results from the reflection-only geometry without the substrate are shown in Fig. 3(c), confirming that the BS features reconstructed and separated by our method are consistent with the reflection measurements. However, only a single BS band is accessible in reflection-only geometry, analogous to optical coherence tomography (OCT). This band limitation causes phase and absorptive interfaces to appear in both the real and imaginary components of the reconstructed $\Delta \epsilon _ { \mathrm { B S } } ,$ , as shown in Fig. 3(c) and its inset, thereby precluding phase–absorption separation.

![](images/e54bd424c93030bb87b6bb877ab2b9e881846dbef11f43054c65b4c967437e03.jpg)  
Fig. 3. Simulation validation of the reconstruction framework. (a) Ground truth of the synthetic object, with the lower half purely phase and the upper half purely absorptive. (b) $k _ { x } - k _ { z }$ profile of the recovered $\widetilde { \Delta \epsilon }$ from reflection-only geometry. (c) x –z cross-sections of the reconstructed $\Delta \epsilon _ { \mathrm { B S } }$ from reflection-only geometry. (d) $k _ { x } - k _ { z }$ profile of the recovered $\widetilde { \Delta \epsilon }$ from substrate-enhanced geometry; right panel: cross-section at $k _ { x } = 0 . 5 k _ { \mathrm { m } }$ showing Re $\widetilde { \Delta \epsilon }$ and Im $\widetilde { \Delta \epsilon }$ satisfy the axial KK relation. (e) x –z cross-sections of the real and imaginary parts of 1FS obtained from the FS band. (f ) x –z cross-sections of the real and imaginary parts of $\Delta \epsilon _ { \mathrm { B S } }$ and $| \Delta \epsilon _ { \mathrm { B S } } ,$ sb| obtained from the combined BS bands and the single BS band, respectively. $\Delta { \epsilon } _ { \mathrm { F S } }$ reveals smooth volumetric features with blurred interfaces, while $\Delta \epsilon _ { \mathrm { B S } }$ complements FS by recovering lateral interfaces, with their real and imaginary parts corresponding to the decoupled phase and absorption, respectively. Figures are clipped to positive values for presentation.

Results from the proposed method are further validated by comparison with a rigorous MBS-based reconstruction (Supplement 1). While yielding consistent results, the MBS approach incurs a substantially higher computational cost (> 8 h), compared with the proposed framework, which requires approximately 100 s for inverse-matrix initialization and 5 s for reconstruction on an NVIDIA L40S GPU.

## B. Robustness Analysis

The robustness of the proposed reconstruction is numerically validated in Supplement 1 through systematic simulations assessing SNR, illumination pattern, temporal coherence, and multiple scattering, and is summarized here.

By adding white Gaussian noise to the scattering patterns to control the SNR, speckle-like artifacts gradually appear in the reconstructed $\Delta \epsilon _ { \mathrm { B S } }$ . These speckle-like artifacts are analogous to those observed in OCT. As the added noise propagates through the linear inverse operator, the reconstructed fluctuations are filtered by the system transfer function, resulting in an autocorrelation that reflects the NA-dependent lateral and axial resolutions. For variations in SNR and scanning density, the results show that FS–BS separation and phase–absorption decoupling remain stable down to an SNR of 23 dB and are largely insensitive to the specific illumination pattern, provided sufficient Fourier-space coverage is maintained. This behavior is consistent with the slow decay of the system’s singular values.

Analysis of different illumination strategies further reveals that scanning patterns produce distinct sampling densities in 3D Fourier space, particularly for the BS channel. Certain patterns introduce gaps in Fourier coverage, leading to reconstructions that preferentially emphasize specific structural features. Among the tested strategies, scanning schemes that approach a uniform distribution on a spherical cap, such as Fermat’s spiral, provide the most balanced overall performance [26].

Temporal coherence effects are evaluated by synthesizing scattering patterns from four shell-shaped scatterers, which are more sensitive to BS, positioned at different depths, and illuminated over a finite spectral bandwidth. The results indicate that, in the proposed method, the axial extent of the BS reconstruction is primarily limited by the temporal coherence length of the illumination source.

Finally, performance beyond the single-scattering regime is examined by increasing both scatterer density and permittivity contrast. Rather than failing abruptly, the method degrades gradually as multiple scattering strengthens, introducing increasing random phase variations from higher-order scattering paths that manifest as speckle noise and interface distortion. Nevertheless, interface information remains resolvable up to $\Delta \epsilon = 0 . 0 5 4$ at a volume fraction of 15%.

## 4. EXPERIMENTAL VALIDATION

## A. System Setup and Resolution Characterization

The technique was validated experimentally using a reflectionmode LED microscope with a 10 × /0.28NA objective [Fig. 4(a)]. Illumination was provided by a 25 LED array, relayed by a 4 f system to the objective’s back focal plane, generating plane waves with NAs of 0.14 and 0.28. Each LED emitted at 632 or 515 nm (20 nm bandwidth), and the resulting intensities were recorded by a camera (2.74 µm pixel size), as shown in the inset of Fig. 4(a).

The setup was first validated using two-layer resolution targets and 3D randomly distributed beads (Supplement 1), demonstrating that FS and BS provide identical axial resolution and the same two-fold lateral resolution enhancement relative to normal incidence, yielding an overall threefold increase in accessible bandwidth compared with the transmission geometry.

## B. Imaging of a Moderately Scattering Biological Specimen

Next, experiments were performed on a fixed young C. elegans worm, green alga Chlamydomonas, breast cancer cells, and red blood cells, all placed on a silver mirror and immersed in water $( \epsilon _ { \mathrm { m } } = 1 . 8 0 ) $ , with results for the latter two provided in Supplement 1. Among these samples, the young C. elegans worm exhibits rich morphological features and operates slightly beyond the single-scattering regime, enabling validation of FS–BS imaging under moderate multiple scattering in a biological specimen. In contrast, the alga and red blood cells possess relatively simple structures and intrinsic absorption contrast, making them well suited for demonstrating phase–absorption separation.

The C. elegans specimen was measured at a wavelength of 632 nm, and the transfer-function-based reconstruction was applied to recover $\Delta \epsilon _ { \mathrm { F S } }$ and $\Delta \epsilon _ { \mathrm { B S } }$ . Representative x –y crosssections of the reconstructed phase (real part) and absorption (imaginary part) are shown in Figs. 4(b) and 4(c), together with depth-dependent contrast profiles and a zoomed-in z-stack in Fig. 4(d). Owing to the limited NA, the reported z values represent approximate depths and do not provide accurate thickness information.

For the BS reconstructions, both BS bands were combined to generate the x –y slices in Fig. 4(c), whereas only the upper BS band was used to compute the contrast profile in Fig. 4(d). This contrast profile, defined as $\sum _ { \mathbf { r } _ { \parallel } } | \Delta \epsilon | ^ { 2 }$ , decays rapidly beyond $z = 0$ , confirming that the axial KK relation confines the reconstruction to the upper half-space.

Near the worm’s top surface $( z = - 2 3 . 0 \mu \mathrm { m } )$ , the reconstructed $\Delta \epsilon _ { \mathrm { F S } }$ exhibits blurred, low-contrast interfaces due to the missing-cone effect, whereas $\Delta \epsilon _ { \mathrm { B S } } ,$ , arising from interfacial reflections, recovers high-frequency details and reveals pronounced, continuously varying surface features that complement the FS reconstruction. Deeper within the specimen $( \mathrm { z } = - 3 . 5 $ µm), 1FS delineates internal anatomical structures, including the pharynx, intestinal lumen, and nuclei, while the BS contrast diminishes but remains spatially correlated with FS.

Comparison with bright-field images acquired in both transmission and reflection (Supplement 1) shows good agreement with the reconstructed FS and BS features, demonstrating that the proposed method effectively separates internal volumetric structures from surface-reflection–dominated features. Although reconstruction quality degrades in the presence of multiple scattering or finite temporal coherence length, these results indicate that the method remains effective for moderately scattering biological samples, providing high-throughput, complementary FS–BS information and a robust initial solution suitable for high-speed imaging or subsequent multiple-scattering-based reconstruction.

![](images/564910b5f30185fa42352576dd51799343d938dfd741de7734cdfd4942848423.jpg)

<details>
<summary>text_image</summary>

(a) LED array
k₁₁ₙ
x
z
Objective
Lens
Beam
Splitter
Measurements
y
x
k₁₁ₙ
Mirror
Camera
</details>

![](images/65a335dda2e8764dad4b07519f3ccd80394375e426fbc598106b11999efdf0a8.jpg)

<details>
<summary>text_image</summary>

(b)
z = -23.0 µm
Pharynx
Intestine
lumen
20 µm
50 µm
Intestine
nuclei
z = -3.5 µm
-1×10⁻²
Forward Scatter, Re(ΔεFS)
1×10⁻²
</details>

![](images/07ca83dc4d454179f3aff5fa173cc784e9921760cf822efa4a9bf2cddeb02c88.jpg)

<details>
<summary>text_image</summary>

(c)
z = -23.0 µm
50 µm
z = -3.5 µm
-1×10⁻²
Forward Scatter, Im(ΔεFS)
1×10⁻²
</details>

![](images/9a9a4f77cde72bddc913afd4c4feb47cf45f085e1c75ae37101a90570f9c9af9.jpg)

<details>
<summary>line chart</summary>

| z (μm) | FS Contrast | BS Contrast |
|--------|-------------|-------------|
| -30    | ~0.5        | ~1.5        |
| -20    | ~0.8        | ~1.2        |
| -10    | ~0.6        | ~0.9        |
| 0      | ~2.0        | ~0.8        |
| 10     | ~0.5        | ~0.5        |
| 30     | ~0.0        | ~0.0        |
</details>

![](images/1758ecc3c0d860687ca76fbc581f6589ca7a83097ae575918629d55c6aa67c2c.jpg)

<details>
<summary>text_image</summary>

-1×10⁻²
Backward Scatter, Re(ΔεBS)
1×10⁻²
</details>

![](images/076ef217a66f990432a62bd6513dfb614b9ca259409d1dbb6614fa819e426f88.jpg)

<details>
<summary>text_image</summary>

-1x10^-2
Backward Scatter, Im(Δε_BS)
1x10^-2
</details>

Fig. 4. Experimental demonstration with a fixed C. elegans on a mirror. (a) Schematic of the substrate-enhanced epi-illumination LED microscope; inset: LED array and representative measured scattering patterns. (b) and (c) Real and imaginary part of $\scriptstyle { \dot { x } } - y$ cross-sections of $\Delta \epsilon _ { \mathrm { F S } }$ and $\Delta \epsilon _ { \mathrm { B S } }$ at $z = - 2 3 . 0$ µm (surface) and z = −3.5 µm (interior). (d) Depth-dependent feature contrast of $\Delta \epsilon _ { \mathrm { F S } }$ and $\Delta \epsilon _ { \mathrm { B S } } ,$ showing that the reconstruction is confined to the upper half-space. Inset, zoomed views at five depths.

## C. Phase–Absorption Separation in Biological Samples

To experimentally demonstrate phase–absorption separation, a cluster of Chlamydomonas, which appears visibly dark green under sunlight, was placed on a mirror substrate and sequentially imaged at wavelengths of 515 nm (green) and 632 nm (red), as shown in Fig. 5(a).

Representative x –y cross-sections at $z = - 2 . 2 \mu \mathrm { m }$ reconstructed at the two wavelengths are presented in Fig. 5(b), with the 515 nm reconstructions shown in the bottom-left panels and the 632 nm reconstructions in the top-right panels. FS reconstructions derived from the FS band are shown in the left column, while

BS reconstructions combining both BS bands are shown in the right column. Framed regions are enlarged as insets for detailed comparison, and their corresponding z-stack profiles are shown in Fig. 5(c).

The real part of the reconstructed 1 exhibits consistent phase contrast at both wavelengths, clearly resolving the spherical cell body and flagella. These phase features encode internal cellular morphology in FS and interfacial information in BS. In contrast, the imaginary part of 1 reveals pronounced absorption features that predominantly surround internal structures. The absorption contrast is distinct from the phase distribution and is consistent with incoherent-illumination bright-field images shown in Supplement 1. At 632 nm, both FS and BS reconstructions exhibit stronger absorption contrast, with mean values of Im $\overline { { \Delta \epsilon } } = 5 . 2 \times 1 0 ^ { - 4 }$ and $2 . 4 \times 1 0 ^ { - 4 }$ in the framed region, respectively. By comparison, reconstructions at 515 nm yield reduced absorption contrast, with corresponding values of $4 . 3 \times 1 0 ^ { - 4 }$ and $1 . 9 \times 1 0 ^ { - 4 }$ . This wavelength dependence is consistent with the dark green appearance of Chlamydomonas, which reflects green light while exhibiting stronger absorption at longer visible wavelengths associated with chlorophyll.

(a)  
![](images/d0080fe8c709118a01f869812a545dea4d0ba23951685c29360ceb7b30b29206.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing spherical particles with a 515 nm scale bar (no text or symbols on particles)
</details>

![](images/5057afff9271bec875e2c772ba806646f1bb2663e2aab98d0992b50a5a1fd55d.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of nanoscale particles with scale bar indicating 632 nm (no text or symbols present)
</details>

(b)  
![](images/0d33ce04fcd0611dfb59f8e398788914e464e7361448d1a0962d338bd0091a18.jpg)

<details>
<summary>text_image</summary>

Forward Scatter
y
x
</details>

![](images/ae4cc5fe5aa7a21d5ac98e2a26e4dd3422f6a335983c917465046e01b3644d8a.jpg)

<details>
<summary>text_image</summary>

Back Scatter
10 µm
20 µm
</details>

3x10-3 -3x10-3

![](images/206266b61e93a8ce8b2ebc2b910b949af2d8876e1a2c1e27db710dab9398b794.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular or particulate structures with magnified insets (no visible text or symbols)
</details>

![](images/276777ac5ddd0848234db701292cace7d0837ea0190f3c3627aa088a94cc8eb7.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular structures with two highlighted regions and dashed lines indicating boundaries (no text or symbols present)
</details>

3×10-3

(c)  
Forward Scatter  
![](images/8dcb59853052646b4ddc7025fa4dc47285ce1e96af28347009ba52393f8fa9b8.jpg)

<details>
<summary>natural_image</summary>

Microscopic images of cellular or granular structures with diagonal lines indicating boundaries (no text or symbols)
</details>

Back Scatter  
![](images/aada63d7740673f767f678b130789578ef8318483628787ac6bc28b0e3c42fc7.jpg)

<details>
<summary>text_image</summary>

-15.0 µm
-10.0 µm
-7.0 µm
-3.5 µm
10 µm
</details>

Fig. 5. Experimental demonstration with a cluster of Chlamydomonas on a mirror. (a) Measured scattering patterns at 515 nm (left) and 632 nm (right). (b) Representative real and imaginary parts of x –y cross-sections of $\Delta \epsilon _ { : }$ , with reconstruction at 515 nm in bottom-left panels and that at 632 nm in top-right panels. Insets, zoomed views for detailed comparison. (c) z-stack profiles of the framed regions in (b).

The same experiments were performed on red blood cells, with results shown in Supplement 1. In contrast to Chlamydomonas, the reconstructed absorption contrast of red blood cells is higher at 515 nm than at 632 nm, consistent with their red appearance and the stronger absorption of green light by hemoglobin. Together, these results experimentally validate robust phase– absorption separation in both FS and BS channels using the proposed technique.

## 5. CONCLUSION AND DISCUSSION

In conclusion, we have introduced a substrate-enhanced diffraction tomography method that simultaneously retrieves FS and BS in epi-configuration, mitigating the missing-cone of transmission and tripling the accessible 3D Fourier bandwidth. FS resolves internal volumetric structures, while BS captures high-frequency surface interfaces, providing complementary contrast confirmed in simulations and experiments. We derive explicit 3D transfer functions for FS and BS and establish an axial KK relation that constrains inversion to the physical half-space. These transfer functions enable band-limited reconstruction restricted to the physical passbands, substantially reducing computational cost. The approach achieves high-resolution, label-free volumetric imaging, disentangles FS–BS mixing in epi-geometry, and extends the effective bandwidth of conventional configurations.

In future work, we anticipate several extensions of the proposed framework. First, for objectives with moderate NA, the substantial spectral separation between the FS and BS bands allows them to be analyzed independently. As the NA increases, this separation progressively diminishes, until the axial bandwidth satisfies $B _ { z } \geq 4 k _ { \mathrm { m } } / 3$ (corresponding to an illumination angle of approximately 71◦). At this point, the central FS band and the two BS bands merge to form a 4Pi bandwidth [12], theoretically enabling isotropic resolution in all spatial directions, as demonstrated in Supplement 1. This suggests that the proposed approach may provide a practical route to achieving 4Pi tomographic bandwidth using a single-objective lens and an interference-free optical path.

Second, the proposed technique exhibits a dependence on NA and temporal coherence length that is complementary to that of spectral-domain (SD) OCT [27]. In our framework, increasing the NA expands the axial BS spatial frequency support and improves axial resolution, while a relatively narrow spectral bandwidth enables an extended axial reconstruction range. Consequently, limitations imposed by finite temporal coherence length can be mitigated by employing laser illumination in the future. In contrast, SD-OCT relies on a broad bandwidth for high-axial resolution while favoring a low NA to maintain an extended axial imaging range. These complementary dependencies suggest that integrating multi-spectral illumination with anglediverse measurements could further enhance the recovery of BS information [28].

Finally, the substrate, present in nearly all reflection-mode imaging systems, can be treated as an additional controllable degree of freedom for engineering the scattering field. By tailoring its optical properties, the substrate may selectively suppress specific scattering components, enhance BS sensitivity, or generate passive structured illumination. Such substrate-assisted control offers a flexible strategy to optimize axial frequency support and scattering contrast without modifying the illumination or detection geometry, opening new avenues for high-resolution volumetric reconstruction in reflection-mode imaging.

Funding. National Science Foundation (1846784); Chan Zuckerberg Initiative (2023-321163).

Acknowledgment. The authors thank Boston University Shared Computing Cluster for providing the computational resources. The work was supported by National Science Foundation (1846784) and in part by grant number 2023 321163 from the Chan Zuckerberg Initiative DAF, an advised fund of Silicon Valley Community Foundation.

Disclosures. The authors declare no conflicts of interest.

Data availability. The reconstruction algorithm is available at [29].

Supplemental document. See Supplement 1 for supporting content.

## REFERENCES

1. Y. Park, C. Depeursinge, and G. Popescu, “Quantitative phase imaging in biomedicine,” Nat. Photonics 12, 578–589 (2018).  
2. D. Huang, E. A. Swanson, C. P. Lin, et al., “Optical coherence tomography,” Science 254, 1178–1181 (1991).  
3. S. Uttam and Y. Liu, “Fourier phase in Fourier-domain optical coherence tomography,” J. Opt. Soc. Am. A 32, 2286–2306 (2015).  
4. D. Jin, R. Zhou, Z. Yaqoob, et al., “Tomographic phase microscopy: principles and applications in bioimaging,” J. Opt. Soc. Am. B 34, B64–B77 (2017).  
5. L. Foucault, N. Verrier, M. Debailleul, et al., “Versatile transmission/reflection tomographic diffractive microscopy approach,” J. Opt. Soc. Am. A 36, C18–C27 (2019).  
6. S. W. Hell, E. H. Stelzer, S. Lindek, et al., “Confocal microscopy with an increased detection aperture: type-B 4Pi confocal microscopy,” Opt. Lett. 19, 222–224 (1994).  
7. A. Kus, M. Dudek, B. Kemper,´ et al., “Tomographic phase microscopy of living three-dimensional cell cultures,” J. Biomed. Opt. 19, 046009 (2014).  
8. B. Simon, M. Debailleul, M. Houkal, et al., “Tomographic diffractive microscopy with isotropic resolution,” Optica 4, 460–463 (2017).  
9. S. Moser, M. K. Løvmo, F. Strasser, et al., “Optical tomography reconstructing 3D motion and structure of multiple-scattering samples under rotational actuation,” Optica 12, 594–603 (2025).  
10. K. C. Zhou, R. P. McNabb, R. Qian, et al., “Computational 3D microscopy with optical coherence refraction tomography,” Optica 9, 593–601 (2022).  
11. B. Bailey, D. L. Farkas, D. L. Taylor, et al., “Enhancement of axial resolution in fluorescence microscopy by standing-wave excitation,” Nature 366, 44–48 (1993).  
12. E. Mudry, P. Chaumet, K. Belkebir, et al., “Mirror-assisted tomographic diffractive microscopy with isotropic resolution,” Opt. Lett. 35, 1857–1859 (2010).  
13. L. Tian and L. Waller, 3D intensity and phase imaging from light field measurements in an LED array microscope,” Optica 2, 104–111 (2015).  
14. S. Chowdhury, M. Chen, R. Eckert, et al., “High-resolution 3D refractive index microscopy of multiple-scattering samples from intensity images,” Optica 6, 1211–1219 (2019).  
15. G. Maire, F. Drsek, J. Girard, et al., “Experimental demonstration of quantitative imaging beyond Abbe’s limit with optical diffraction tomography,” Phys. Rev. Lett. 102, 213905 (2009).  
16. E. Mudry, E. L. Moal, P. Ferrand, et al., “Isotropic diffraction-limited focusing using a single objective lens,” Phys. Rev. Lett. 105, 203903 (2010).  
17. T. Li, J. Zhu, Y. Shen, et al., “Reflection-mode diffraction tomography of multiple-scattering samples on a reflective substrate from intensity images,” Optica 12, 406–417 (2025).  
18. C. A. Chacón Ávila, N. Verrier, M. Debailleul, et al., “Dual-view tomographic diffraction microscopy,” Opt. Express 33, 51444–51458 (2025).  
19. S. Kang, R. Zhou, M. Brelen, et al., “Mapping nanoscale topographic features in thick tissues with speckle diffraction tomography,” Light Sci. Appl. 12, 200 (2023).  
20. G. Osnabrugge, S. Leedumrongwatthanakun, and I. M. Vellekoop, “A convergent Born series for solving the inhomogeneous Helmholtz equation in arbitrarily large media,” J. Comput. Phys. 322, 113–124 (2016).  
21. T. Zhang, Y. Ruan, G. Maire, et al., “Full-polarized tomographic diffraction microscopy achieves a resolution about one-fourth of the wavelength,” Phys. Rev. Lett. 111, 243904 (2013).  
22. Y. Baek, K. Lee, S. Shin, et al., “Kramers–Kronig holographic imaging for high-space-bandwidth product,” Optica 6, 45–51 (2019).  
23. Y. Baek and Y. Park, “Intensity-based holographic imaging via spacedomain Kramers–Kronig relations,” Nat. Photonics 15, 354–360 (2021).  
24. R. Ling, W. Tahir, H.-Y. Lin, et al., “High-throughput intensity diffraction tomography with a computational microscope,” Biomed. Opt. Express 9, 2130–2141 (2018).  
25. M. Sarmis, B. Simon, M. Debailleul, et al., “High resolution reflection tomographic diffractive microscopy,” J. Mod. Opt. 57, 740–745 (2010).  
26. A. M. Taddese, N. Verrier, M. Debailleul, et al., “Optimizing sample illumination scanning for reflection and 4Pi tomographic diffractive microscopy,” Appl. Opt. 60, 7745–7753 (2021).  
27. K. C. Zhou, R. Qian, A.-H. Dhalla, et al., “Unified k-space theory of optical coherence tomography,” Adv. Opt. Photonics 13, 462–514 (2021).  
28. T. Zhang, K. Unger, G. Maire, et al., “Multi-wavelength multi-angle reflection tomography,” Opt. Express 26, 26093–26105 (2018).  
29. T. Li, Y. Shen, D. Dong, et al., “Python implementation of paper: Transferfunction approach to substrate-enhanced diffraction tomography,” GitHub, 2026, https://github.com/bu-cisl/TF\_rIDT.