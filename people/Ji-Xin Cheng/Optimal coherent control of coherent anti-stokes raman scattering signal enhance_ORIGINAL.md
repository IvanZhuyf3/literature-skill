RESEARCH ARTICLE | APRIL 13 2012

# Optimal coherent control of coherent anti-Stokes Raman scattering: Signal enhancement and background elimination

![](images/967c57fc41028a119303cff458da653dd1b15e4c9a13a8a9cf7dfd1d3098f171.jpg)

Fang Gao; Feng Shuang; Junhui Shi; Herschel Rabitz; Haifeng Wang; Ji-Xin Cheng

![](images/c0bd52b89f58e441e2a768afaa175e5e41d704caf36a4db04146ebe82457af37.jpg)

Check for updates

J. Chem. Phys. 136, 144114 (2012)

https://doi.org/10.1063/1.3703308

![](images/a6c4453d1cb33558c66cb3a8fc29b8584ba63fad0268336d7c79e4b1f459d8f4.jpg)  
View Online

![](images/23a684059c69b16761a13ddecf6102403ef5dca32dd66c9a42717dd0b525b6a0.jpg)  
Export Citation

## Articles You May Be Interested In

Enhanced pointing and charge properties of electron beams from few-TW laser wakefield acceleration with an asymmetric density profile in a sub-millimeter nitrogen gas jet

Phys. Plasmas (October 2024)

Molecular discrimination of a mixture with single-beam Raman control

J. Chem. Phys. (October 2007)

Coherent control of bond breaking in amino acid complexes with tailored femtosecond pulses

J. Chem. Phys. (November 2007)

![](images/e3f176e7079fd80ab40faa3a8c39affeb611455923f4f07054dd8dea5e18129b.jpg)

<details>
<summary>natural_image</summary>

Abstract digital artwork with flowing light streaks against a dark background, no text or symbols present
</details>

## AIP Advances

Why Publish With Us?

![](images/27bf108a8a82decd3dd7a89782f0c00f7cb930824578b1ee360ce11ab9ad3b30.jpg)  
21DAYS average time to 1 st decision

![](images/1a52d4945651faed7ba716f850823e082e7c78c6bba9936ae6a9a037cd7aa651.jpg)  
OVER 4 MILLION views in the last year

![](images/2a8a02a35f12296f41dc465bc309085722f2e1ce9c1788eb2b96d2608649f3a5.jpg)  
INCLUSIVE scope

Learn More

![](images/1652341cd9899d3194c1385db036ac012fee5a5058f378c9d170efaec8cc898f.jpg)  
AIP Publishing

# Optimal coherent control of coherent anti-Stokes Raman scattering: Signal enhancement and background elimination

Fang Gao,1 Feng Shuang,1,a) Junhui Shi,2 Herschel Rabitz,2 Haifeng Wang,3 and Ji-Xin Cheng4

1Institute of Intelligent Machines, Chinese Academy of Sciences, Hefei 230031, China

2Department of Chemistry, Princeton University, Princeton, New Jersey 08544, USA

3Department of Physics, National University of Singapore, Singapore 117542, Singapore

4Weldon School of Biomedical Engineering and Department of Chemistry, Purdue University, West Lafayette, Indiana 47907, USA

(Received 15 November 2011; accepted 28 March 2012; published online 13 April 2012)

The ability to enhance resonant signals and eliminate the non-resonant background is analyzed for coherent anti-Stokes Raman scattering (CARS). The analysis is done at a specific frequency as well as for broadband excitation using femtosecond pulse-shaping techniques. An appropriate objective functional is employed to balance resonant signal enhancement against non-resonant background suppression. Optimal enhancement of the signal and minimization of the background can be achieved by shaping the probe pulse alone while keeping the pump and Stokes pulses unshaped. In some cases analytical forms for the probe pulse can be found, and numerical simulations are carried out for other circumstances. It is found that a good approximate optimal solution for resonant signal enhancement in two-pulse CARS is a superposition of linear and arctangent-type phases for the pump. The well-known probe delay method is shown to be a quasi-optimal scheme for broadband background suppression. The results should provide a basis to improve the performance of CARS spectroscopy and microscopy. © 2012 American Institute of Physics. [http://dx.doi.org/10.1063/1.3703308]

## I. INTRODUCTION

Coherent anti-Stokes Raman scattering (CARS), as a four-wave nonlinear process,1 has been widely used in the past few decades to study chemical systems in solutions, reactions in the gas phase, and vibrational dynamics in gas and condensed phases. CARS microscopy is a recently implemented technique for imaging biological species, which was pioneered by Duncan et al. using two dye lasers and developed2 by Xie et al. for high-sensitivity applications.3, 4 As a combination of ultrafast nonlinear spectroscopy and microscopy, CARS microscopy is a highly chemically selective and sensitive technique that employs a CARS signal of an unlabeled sample and provides higher spatial resolution than two-photon fluorescence microscopy.

When imaging biological samples, the typical width of Raman transitions is a few wave numbers, so picosecond pulses are widely used in CARS spectroscopy and microscopy.3, 5–7 Not only is the narrow bandwidth of the picosecond pulse adequate to detect specific Raman bands, it also produces low non-resonant background. On the other hand, when investigating broadband CARS spectra, 8, 9 especially in the Raman fingerprint region which spans from 800 to 1800 cm−1, it is necessary to bring in broadband femtosecond pulses. Femtosecond CARS can be employed not only for direct imaging but also as a tool to determine some microscopic and macroscopic parameters, such as molecular anharmonicity10 and temperature.10, 11 However, this situation creates a dilemma when the pulse bandwidth is ∼1000 cm−1, as the non-resonant background becomes significant to possibly submerge the resonant signal and the fine vibrational structure of CARS.12, 13 The large nonresonant contribution affects the shape of CARS spectra and complicates data analysis, which becomes an obstacle for femtosecond CARS. Hence, the study of signal enhancement and background suppression is important for effective Raman selective excitation in CARS, in which a broadband femtosecond pulse is employed to excite multiple Raman modes.13–17 Resonant signal enhancement and non-resonant background suppression of CARS have been studied for many years. Polarization CARS adjusts the polarization of the pump and Stokes pulses to suppress non-resonant background.18–21 Time-resolved CARS (Ref. 22) uses temporally overlapped pump and Stokes pulses along with a delayed probe pulse to generate a signal. This procedure can also eliminate the nonresonant background, which is essentially instantaneous while the resonant signal has a much longer decay time. Scully et al. proposed hybrid CARS,23 in which the broadband pump and Stokes pulses produce maximal Raman coherence and the narrow-band time-delayed probe pulse suppresses the non-resonant background. Cheng et al. reported that epidetected CARS microscopy can significantly reduce the solvent background.3 The advent of spatial light modulators (SLMs) has enabled coherent control and mode-selective excitation of CARS with femtosecond pulses.24–27 Background suppression without loss of the resonant signal has also been explored widely with the development of femtosecond phase shaping techniques. By using SLM phase modulation and a variable wave plate, Silberberg et al. combined phase and polarization control to yield background-free single-pulse multiplex CARS spectra with high spectral resolution.28 Leone et al. combined interferometric and polarization/phase control to demonstrate a method of single pulse interferometric CARS spectroscopy,29, 30 which could extract the imaginary and real parts of the background-free resonant CARS spectrum in a single experimental measurement. Offerhaus et al. employed vibrational phase contrast CARS, in which the measured phase components in the focal volume allows enhanced sensitivity and increased selectivity.31, 32 With the optical fields driving the CARS process and the local oscillator used for heterodyning both derived from a single beam by pulse shaping, Motzkus et al. proposed highly sensitive single-beam heterodyne CARS microspectroscopy,33 in which the sensitivity of chemically selective detection at microscopic resolution is dramatically increased. It has also to be mentioned here that while phase shaping is effective to suppress non-resonant background in broadband CARS, there are also post-processing approaches proposed by Bonn34–36 and Cicerone37, 38 to retrieve background-free and noise-reduced CARS spectra.

In this work, we explore the optimal control of the signal and background of CARS with various phase shaping schemes. The paper is organized as follows: Section II shows the optimal phase shaping schemes at a specific frequency. Section III investigates the control strategies for broadband CARS and the conclusions are given in Sec. IV.

## II. LOCAL OPTIMAL CONTROL

CARS is a four-wave nonlinear process as shown in Fig. 1. Three laser pulses are used to produce the CARS signal: the pump pulse $\tilde { E _ { p } } ( \tilde { \omega } _ { p } ) .$ the Stokes pulse $\tilde { E } _ { s } ( \tilde { \omega } _ { s } ) .$ , and the probe pulse $\tilde { E _ { p r } } ( \tilde { \omega } _ { p r } )$ . The CARS signal $I _ { \mathrm { C A R S } } ( \tilde { \omega } _ { a s } )$ is a coherent superposition of resonant third-order nonlinear polarization $P _ { r } ^ { ( 3 ) } ( \tilde { \omega } _ { a s } )$ and non-resonant third-order nonlinear polarization $P _ { n r } ^ { ( 3 ) } ( \tilde { \omega } _ { a s } )$ ,

$$
I _ {\mathrm{CARS}} (\tilde {\omega} _ {a s}) = \left| P _ {r} ^ {(3)} (\tilde {\omega} _ {a s}) + P _ {n r} ^ {(3)} (\tilde {\omega} _ {a s}) \right| ^ {2} \tag {1}
$$

![](images/08167ccd4e1d51479138fb2419bd755a4d4603c0334d4da20b6b345dffdb0eea.jpg)

<details>
<summary>text_image</summary>

ω̃p
ω̃s
ω̃pr
ω̃as
ΩR
v=1
v=0
</details>

![](images/26ba934baa15483b16683231d0d920f46c8a14431123d24d6059be6dba9bf36c.jpg)

<details>
<summary>text_image</summary>

ω̃p
ω̃s
ω̃pr
ω̃as
v=n
v=0
</details>

FIG. 1. Energy level diagram of the CARS process. The left panel corresponds to the resonant signal generation: pump and Stokes pulses generate coherence between two vibrational levels, when they have a frequency difference which coincides with the Raman resonance R. The probe pulse then induces the anti-Stokes signal. The right panel corresponds to the non-resonant background contribution: the non-resonant background is produced via an intermediate virtual state that does not reflect the resonant molecular energy level.

and

$$
\begin{array}{l} P _ {\mathrm{r}} ^ {(3)} (\tilde {\omega} _ {a s}) = \iiint_ {- \infty} ^ {+ \infty} d \tilde {\omega} _ {p} d \tilde {\omega} _ {s} d \tilde {\omega} _ {p r} \frac {C}{\Omega_ {R} - (\tilde {\omega} _ {p} - \tilde {\omega} _ {s}) - i \Gamma} \\ \times \tilde {E} _ {p} (\tilde {\omega} _ {p}) \tilde {E} _ {s} ^ {*} (\tilde {\omega} _ {s}) \tilde {E} _ {p r} (\tilde {\omega} _ {p r}) \delta (\tilde {\omega} _ {a s} - \tilde {\omega} _ {p} + \tilde {\omega} _ {s} - \tilde {\omega} _ {p r}), \tag {2} \\ \end{array}
$$

$$
P _ {\mathrm{nr}} ^ {(3)} (\tilde {\omega} _ {a s}) = \iiint_ {- \infty} ^ {+ \infty} d \tilde {\omega} _ {p} d \tilde {\omega} _ {s} d \tilde {\omega} _ {p r} \chi_ {n r}
$$

$$
\times \tilde {E} _ {p} \left(\tilde {\omega} _ {p}\right) \tilde {E} _ {s} ^ {*} \left(\tilde {\omega} _ {s}\right) \tilde {E} _ {p r} \left(\tilde {\omega} _ {p r}\right) \delta \left(\tilde {\omega} _ {a s} - \tilde {\omega} _ {p} + \tilde {\omega} _ {s} - \tilde {\omega} _ {p r}\right), \tag {3}
$$

here $\Omega _ { R }$ is the Raman frequency between energy levels 1 and $2 , 2 \Gamma$ is the level width, C is a constant which depends on the material property, and $\chi _ { n r }$ is the non-resonant thirdorder susceptibility. The resonant signal intensity at the frequency $\tilde { \omega } _ { a s }$ is $| \bar { P } _ { r } ^ { ( 3 ) } ( \tilde { \omega } _ { a s } ) | ^ { 2 }$ , the non-resonant background intensity is $| P _ { n r } ^ { ( 3 ) } ( \tilde { \omega } _ { a s } ) | ^ { 2 }$ , and the integrated CARS intensity is $\begin{array} { r } { I = \int _ { 0 } ^ { + \infty } | P _ { r } ^ { ( 3 ) } ( \tilde { \omega } _ { a s } ) + P _ { r } ^ { ( 3 ) } ( \tilde { \omega } _ { a s } ) | ^ { 2 } d \tilde { \omega } _ { a s } } \end{array}$ .

In our work, the carrier frequencies of the pump, Stokes, and probe pulses are denoted as $\Omega _ { p } , \Omega _ { s } ,$ and $\Omega _ { p r }$ , respectively. Then if all the pulses are transform limited pulses (TLPs), the peaks of the resonant and non-resonant signals in the spectrum are both located at the frequency $\Omega _ { a s } = \Omega _ { p } - \Omega _ { s } + \Omega _ { p r } .$

A Gaussian amplitude profile in the frequency domain is used for the pump, Stokes, and probe pulses in our theoretical treatment and simulations,

$$
\tilde {E} _ {k} \left(\tilde {\omega} _ {k}\right) = \frac {E _ {k}}{\Delta_ {k} ^ {1 / 2}} e ^ {- \left(\tilde {\omega} _ {k} - \Omega_ {k}\right) ^ {2} / \Delta_ {i} ^ {2}} e ^ {i \tilde {\Phi} _ {k} \left(\tilde {\omega} _ {k} - \Omega_ {k}\right)}, \quad k = \{P, S, P r \}, \tag {4}
$$

where $2 \sqrt { \ln { 2 } } \Delta _ { k }$ is the corresponding spectral full width at half-maximum (FWHM), and $\tilde { \Phi } _ { k } ( \tilde { \omega } _ { k } - \Omega _ { k } )$ is the frequencydomain phase profile. For simplicity, a frequency variable translation, $\omega _ { k } = \tilde { \omega } _ { k } - \Omega _ { k } ,$ , is made $( \mathrm { i } . \mathrm { e } . , \Phi _ { k } ( \omega _ { k } )$ $\mathbf { \tilde { \Phi } } = \tilde { \Phi } _ { k } ( \tilde { \omega } _ { k } { - } \Omega _ { k } )$ and $\begin{array} { r } { E _ { k } ( \omega _ { k } ) = \tilde { E } _ { k } ( \tilde { \omega } _ { k } ) = \frac { E _ { k } } { \Delta _ { k } ^ { 1 / 2 } } e ^ { - \omega _ { k } ^ { 2 } / \Delta _ { k } ^ { 2 } } e ^ { i \Phi _ { k } ( \omega _ { k } ) } ) } \end{array}$ and $P _ { r } ^ { ( 3 ) } ( \Omega _ { a s } )$ is written as $P _ { r } .$ .

There are several experimental configurations for CARS: single-pulse CARS (Ref. 8) (all three photons required are supplied by the same short optical pulse), two-pulse CARS (the pump pulse also acts as probe pulse in the experiment) and three-pulse CARS. In this section, optimal control at a single signal frequency is investigated in two-pulse and threepulse CARS. Optimal control strategies with the probe pulse are also explored. Only the intensity at a specific frequency $( \tilde { \omega } _ { a s } = \Omega _ { a s } )$ is considered throughout this section, and broadband optimal control will be discussed in Sec. III.

For simplicity, unless otherwise stated, $\Delta _ { p } = \Delta _ { p r } = \Delta _ { s }$ $= \Delta$ is assumed in the following without loss of generality, as the conclusions still hold when the bandwidths are different.

## A. Control of the signal or background by shaping the probe pulse in three-pulse CARS

Optimal control for signal enhancement or background suppression with the probe pulse has been discussed previously,12, 39, 40 s o only a brief description is given here.

![](images/1758e5c7316aac45c0b279dcc2d61a0921597c3e39fb5040e08f27ec730b2d90.jpg)

<details>
<summary>line chart</summary>

| x    | arctan(ω_pr / Γ) | π step | TLP  |
| ---- | ---------------- | ------ | ---- |
| -2   | 0.0              | 0.0    | 0.0  |
| 0    | 0.7              | 0.5    | 0.4  |
| 2    | 0.0              | 0.0    | 0.0  |
</details>

![](images/0c645e430f315372d96a0b6fbc644fb1ffcc1194c9f8ffd2ec7e448742794a3c.jpg)

<details>
<summary>line chart</summary>

| ω_as/Δ | arctan(ω_pr/Γ) | π step | TLP |
| ------ | -------------- | ------ | --- |
| -3.0   | 0.0            | 0.0    | 0.0 |
| -2.0   | 0.2            | 0.2    | 0.2 |
| -1.0   | 0.3            | 0.3    | 0.6 |
| 0.0    | 0.35           | 0.0    | 1.0 |
| 1.0    | 0.3            | 0.3    | 0.6 |
| 2.0    | 0.2            | 0.2    | 0.2 |
| 3.0    | 0.0            | 0.0    | 0.0 |
</details>

FIG. 2. The resonant signal and non-resonant background with different phase shaping schemes for the probe pulse while keeping the pump and Stokes pulses unshaped in three-pulse CARS. The arctan( $\omega _ { p r } / \Gamma )$ phase (red solid lines), π-step phase (blue dashed-dotted lines), and TLP (black dashed lines) shaping schemes are shown together for comparison. The bandwidths of the pump, Stokes, and probe pulses are the same: $\Delta _ { p } = \Delta _ { s } = \Delta _ { p r }$ $= \Delta = \mathrm { 5 0 ~ c m ^ { - 1 } }$ .

Figure 2 shows the optimal control strategies: when the phase of the probe pulse is either the arctan $( \omega _ { p r } / \Gamma )$ or a π step phase function, the resonant and non-resonant signals achieve their maximal and minimal values, respectively. The optimality condition can be gained analytically as following:

Equation (2) leads to

$$
\begin{array}{l} P _ {r} = C \sqrt {\frac {\pi}{2 \Delta}} \int_ {- \infty} ^ {\infty} d \omega_ {p r} \frac {1}{\omega_ {p r} - i \Gamma} \exp \left[ - \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}} \right] \exp [ i \Phi_ {p r} (\omega_ {p r}) ] \\ = C \sqrt {\frac {\pi}{2 \Delta}} \int_ {- \infty} ^ {\infty} d \omega_ {p r} \frac {1}{\sqrt {\omega_ {p r} ^ {2} + \Gamma^ {2}}} \exp \left[ - \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}} \right] \\ \times \exp [ i (\Phi_ {p r} (\omega_ {p r}) + \alpha (\omega_ {p r})) ], \tag {5} \\ \end{array}
$$

where $\alpha ( \omega _ { p r } ) = - \arctan ( \omega _ { p r } / \Gamma ) + \pi / 2$ is confined in the domain $[ 0 , \pi ]$ . It is easy to see that $| P _ { r } | ^ { 2 }$ reaches its maximal value when the phase contribution to the integrand exp $[ i \Phi _ { p r } ( \omega _ { p r } ) + i \alpha ( \omega _ { p r } ) ]$ becomes a constant, i.e.,

$$
\Phi_ {p r} (\omega_ {p r}) = \arctan (\omega_ {p r} / \Gamma) + \text { constant }, \tag {6}
$$

with the resultant maximal peak intensity

$$
\left| P _ {r} \right| _ {\max} ^ {2} = C ^ {2} \frac {\pi}{2 \Delta} e ^ {\frac {3 \Gamma^ {2}}{2 \Delta^ {2}}} \mathrm{K} ^ {2} \left(0, \frac {3 \Gamma^ {2}}{4 \Delta^ {2}}\right). \tag {7}
$$

Here K is a modified Bessel function. The condition for maximal or minimal resonant signal intensity could also be established by using the variational method (see Appendix A), which may aid in exploring the control landscape41 for CARS.

The non-resonant background can be derived from Eq. (3),

$$
\begin{array}{l} P _ {n r} (\Omega_ {a s}) = \chi_ {n r} \sqrt {\frac {\pi}{2 \Delta}} \int_ {- \infty} ^ {+ \infty} d \omega_ {p r} \exp \left[ - \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}} \right] \\ \times \exp [ i \Phi_ {p r} (\omega_ {p r}) ]. \tag {8} \\ \end{array}
$$

Thus $| P _ { n r } ( \Omega _ { a s } ) | ^ { 2 }$ reaches its minimal value of zero when exp $[ i \Phi _ { p r } ( \omega _ { p r } ) ]$ is an anti-symmetric function, $\mathrm { e . g . } , \Phi _ { p r } ( \omega _ { p r } )$ i s the π step phase function about $\omega _ { p r } = 0$ (note that $\mathrm { e x p } [ - \frac { 3 \omega _ { p r } ^ { 2 } } { 2 \Delta ^ { 2 } } ]$ − 3ω2pr2 ] is a symmetric positive-definite function).

As seen in the bottom panel of Fig. 2, the π step phase function can only eliminate the local component of background around $\tilde { \omega } _ { a s } = \Omega _ { a s }$ to form a dip in the spectrum. Thus the phase function obtained by minimizing $| P _ { n r } ( \Omega _ { a s } ) | ^ { 2 }$ is locally optimal, but the background may still affect the resonant signal away from the position of $\tilde { \omega } _ { a s } = \Omega _ { a s }$ in the spectrum. Hence, a broadband background suppression method is necessary for CARS, which will be discussed in Sec. III.

## B. Control in two-pulse CARS

For practical considerations, in many CARS experiments, the pump pulse also operates as the probe pulse. In this subsection, we will concentrate on two-pulse CARS, in which only the pump pulse is phase shaped. From Eq. (2), it follows that

$$
\begin{array}{l} P _ {r} ^ {(3)} (\Omega_ {a s}) = \int_ {- \infty} ^ {\infty} \frac {C}{\omega_ {p r} - i \Gamma} E _ {p} (\omega_ {p r}) \\ \times \left[ \int_ {- \infty} ^ {\infty} E _ {p} (\omega_ {p}) E _ {s} ^ {*} (\omega_ {p} + \omega_ {p r}) d \omega_ {p} \right] d \omega_ {p r} \\ = \frac {1}{\Delta^ {3 / 2}} \int_ {- \infty} ^ {\infty} \frac {C}{\omega_ {p r} - i \Gamma} e ^ {- \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}} + i \Phi_ {p} (\omega_ {p r})} \\ \times \left[ \int_ {- \infty} ^ {\infty} e ^ {- \frac {2 (\omega_ {p} + \omega_ {p r} / 2) ^ {2}}{\Delta^ {2}} + i \Phi_ {p} (\omega_ {p})} d \omega_ {p} \right] d \omega_ {p r}. \tag {9} \\ \end{array}
$$

It is difficult to obtain an analytic optimal phase function for $| P _ { r } ^ { 2 } ( \Omega _ { a s } ) |$ . Instead, a numerical solution is presented in Fig. 3, and it shows that the optimal phase function is approximately a superposition of the linear and arctan $( \omega _ { p } / \Gamma ) / 2$ phases: the optimal phase is quasi-linear away from $\omega _ { p }$ $= 0$ and similar to arctan $\omega _ { p } / \Gamma ) / 2$ around $\omega _ { p } = 0$ . This behavior may be understood as follows: since the zero phase profile (a special case of linear phase) is optimal for $\begin{array} { r } { | \int _ { - \infty } ^ { \infty } e ^ { - \frac { 2 ( \omega _ { p } + \omega _ { p r } / 2 ) ^ { 2 } } { \Delta ^ { 2 } } + i \Phi _ { p } ( \omega _ { p } ) } d \omega _ { p } | } \end{array}$ +ip(ωp) dωp|, and the arctan(ωp/ ) phase $( \omega _ { p } / \Gamma )$ is optimal for $\begin{array} { r } { | \int _ { - \infty } ^ { \infty } \frac { C } { \omega _ { p r } - i \Gamma } e ^ { - \frac { 3 \omega _ { p r } ^ { 2 } } { 2 \Delta ^ { 2 } } + i \Phi _ { p } ( \omega _ { p r } ) } d \omega _ { p r } | } \end{array}$ 3ω2pr +ip(ωpr ) dωpr |, then an approximate superposition of the linear and arctan $( \omega _ { p } / \Gamma )$ phase functions form the optimal solution for $| P _ { r } ^ { ( 3 ) } ( \Omega _ { a s } ) |$ , which is the combination of these two integrals. With no explicit analytical solutions, optimal control in two-pulse CARS has to be studied numerically case by case. In an experiment, an approximate superposition of a step and a proper timedelayed phase could effectively produce a large resonant signal13 in the case of small .

![](images/2be7d24faee50a974816fda2d0865745e525fa7b84128ab91cd0b8f273d17d36.jpg)

<details>
<summary>line chart</summary>

| ω_p / Δ | Optimal | arctan(ω_p / Γ)/2 | Linear |
| ------- | ------- | ----------------- | ------ |
| -1.0    | 0.4     | -0.6              | 0.5    |
| -0.5    | -0.3    | -0.6              | 0.3    |
| 0.0     | -0.6    | -0.6              | 0.0    |
| 0.5     | 0.6     | 0.6               | -0.3   |
| 1.0     | 0.2     | 0.7               | -0.6   |
</details>

![](images/ffce38920187b8bccce9c36f68fe050ecae365c1cd9dfe41f060135a42d2732c.jpg)

<details>
<summary>line chart</summary>

| Time/ps | Optimal | TLP    |
| ------- | ------- | ------ |
| -2      | 0.0     | 0.0    |
| -1      | 0.1     | 0.0    |
| 0       | 0.9     | 1.0    |
| 1       | 0.2     | 0.0    |
| 2       | 0.0     | 0.0    |
</details>

FIG. 3. Optimal phase function (via the Covariance Matrix Adaptation - Evolutionary Strategy (CMA-ES) optimization method $^ { 1 4 2 , 4 3 } )$ for the pump pulse in two-pulse CARS. The parameters: $\Delta _ { p } = \Delta _ { s } = 5 0 \mathrm { c m } ^ { - 1 }$ , $\Gamma = 4 . 8 \mathrm { c m } ^ { - 1 }$ . In the top panel, the red solid line is the optimal phase function of the pump pulse for maximal resonant signal intensity, the magenta dotted line corresponds to the arctan $( \omega _ { p } / \Gamma ) / 2$ phase, and the blue dashed line is a linear phase profile. The bottom panel shows the outcome of optimal pulse (red solid line) and TLP (black dashed line) in the time domain.

To check the effect of this optimal phase scheme in two-pulse CARS, the resonant signal and non-resonant background spectra with other shaping schemes are shown together in Fig. 4 for comparison. As can be seen, $| P _ { r } |$ for the optimal scheme looks similar with that for the arctan $( \omega _ { p } / \Gamma )$ scheme. The resonant signal decreases a lot with the π step phase. Compared with the TLP scheme, all the other three schemes can suppress the background, but only the optimal phase scheme enhances the resonant signal. This is easy to understand since our optimized objective is the resonant peak signal at $\omega _ { a s } = 0$ .

## C. Control in three-pulse CARS

In Sec. II A, it was shown that the phase function arctan $( \omega _ { p r } / \Gamma )$ generates a maximal resonant signal intensity when only the probe pulse is shaped. In three-pulse CARS, all the three pulses can be shaped. Thus in this subsection, we will demonstrate if the three-pulse shaping scheme can achieve better performance than the probe-only shaping scheme in three-pulse CARS. The analytical and numerical results will show that the configuration of TLPs for the pump and Stoke pulses and an arctan $( \omega _ { p r } / \Gamma )$ phase profile for the probe pulse is optimal to maximize the resonant signal. The CARS spectra of $| P _ { r } |$ and $| P _ { n r } |$ with this optimal phase scheme and other schemes can be found in Fig. 2.

![](images/e8088feca66c7c28799add81a1879df89e582a1942c87254fde91696e7fd76e7.jpg)

<details>
<summary>line chart</summary>

| ω_as / Δ | Optimal | arctan(ω_p / Γ) | π step | TLP |
| -------- | ------- | --------------- | ------ | --- |
| -2       | 0.0     | 0.0             | 0.0    | 0.0 |
| 0        | 0.5     | 0.3             | 0.1    | 0.4 |
| 2        | 0.0     | 0.0             | 0.0    | 0.0 |
</details>

![](images/37e494ded13249b040774294c01119c22e9f47db1d6bbdec7f0c933099769bc3.jpg)

<details>
<summary>line chart</summary>

| ω_as/Δ | Optimal | arctan(ω_p/Γ) | π step | TLP |
| ------ | ------- | ------------- | ------ | --- |
| -2     | 0.1     | 0.1           | 0.1    | 0.1 |
| -1     | 0.6     | 0.3           | 0.2    | 0.7 |
| 0      | 0.8     | 0.4           | 0.3    | 0.9 |
| 1      | 0.6     | 0.3           | 0.2    | 0.7 |
| 2      | 0.1     | 0.1           | 0.1    | 0.1 |
</details>

FIG. 4. The resonant signal and non-resonant background spectra with different phase shaping schemes for the pump pulse in two-pulse CARS. The optimal phase (red solid lines), arctan( $\omega _ { p } / \Gamma )$ ) phase(blue dotted lines), π step phase (magenta dashed-dotted lines), and TLP (black dashed lines) schemes are shown together for comparison. The parameters are the same as in Fig. 3.

From Eq. (2), we have

$$
\begin{array}{l} P _ {r} ^ {(3)} (\Omega_ {a s}) = \int_ {- \infty} ^ {\infty} \frac {C}{\omega_ {p r} - i \Gamma} E _ {p r} (\omega_ {p r}) \\ \times \left[ \int_ {- \infty} ^ {\infty} E _ {p} (\omega_ {p}) E _ {s} ^ {*} (\omega_ {p} + \omega_ {p r}) d \omega_ {p} \right] d \omega_ {p r} \\ = \frac {1}{\Delta^ {3 / 2}} \int_ {- \infty} ^ {\infty} \frac {C}{\omega_ {p r} - i \Gamma} e ^ {- \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}} + i \Phi_ {p r} (\omega_ {p r})} A \left(\omega_ {p}, \omega_ {p r}\right) d \omega_ {p r}, \tag {10} \\ \end{array}
$$

where the Raman excitation term is

$$
A (\omega_ {p}, \omega_ {p r}) = \int_ {- \infty} ^ {\infty} e ^ {- \frac {2 (\omega_ {p} + \omega_ {p r} / 2) ^ {2}}{\Delta^ {2}}} e ^ {i \Phi_ {p} (\omega_ {p}) - i \Phi_ {s} (\omega_ {p} + \omega_ {p r})} d \omega_ {p}. \tag {11}
$$

It is easy to see that

$$
\left| A \left(\omega_ {p}, \omega_ {p r}\right) \right| \leq \int_ {- \infty} ^ {\infty} e ^ {- \frac {2 \left(\omega_ {p} + \omega_ {p r} / 2\right) ^ {2}}{\Delta^ {2}}} d \omega_ {p} = \sqrt {\frac {\pi}{2}} \Delta . \tag {12}
$$

The equality holds only when $\Phi _ { p } ( \omega _ { p } ) - \Phi _ { s } ( \omega _ { p } + \omega _ { p r } )$ does not depend on variable $\omega _ { p }$ for arbitrary $\omega _ { p r }$ . There are only two cases satisfying this condition: (1) $\Phi _ { p } ( \omega _ { p } )$ and $\Phi _ { s } ( \omega _ { p }$ $+ \omega _ { p r } )$ are both constant functions, i.e., the pump and Stokes pulse are TLPs; (2) $\Phi _ { p }$ and $\Phi _ { s }$ are both linear functions with the same slope: $\Phi _ { p } ( \omega _ { p } ) - \Phi _ { s } ( \omega _ { p } + \omega _ { p r } ) = k \omega _ { p r } +$ + constant, which is equivalent to linear phase shaping (or a time delay) scheme for the probe pulse. The first case is just the second one with zero slope (no delay).

Thus, the following equation can be derived:

$$
\begin{array}{l} \left| \frac {1}{\Delta^ {3 / 2}} \int_ {- \infty} ^ {\infty} \frac {C}{\omega_ {p r} - i \Gamma} e ^ {- \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}} + i \Phi_ {p r} (\omega_ {p r})} A (\omega_ {p}, \omega_ {p r}) d \omega_ {p r} \right| \\ \leq \left| \frac {1}{\Delta^ {3 / 2}} \int_ {- \infty} ^ {\infty} \left| \frac {C}{\omega_ {p r} - i \Gamma} e ^ {- \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}} + i \Phi_ {p r} (\omega_ {p r})} \right| | A (\omega_ {p}, \omega_ {p r}) | d \omega_ {p r} \right| \\ \leq \left| \frac {1}{\Delta^ {3 / 2}} \int_ {- \infty} ^ {\infty} \left| \frac {C}{\omega_ {p r} - i \Gamma} e ^ {- \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}} + i \Phi_ {p r} (\omega_ {p r})} \right| \cdot \sqrt {\frac {\pi}{2}} \Delta \cdot d \omega_ {p r} \right| \\ \end{array}
$$

(when $\Phi _ { p }$ and $\Phi _ { s }$ are constant)

$$
\leq C \sqrt {\frac {\pi}{2 \Delta}} e ^ {\frac {3 \Gamma^ {2}}{4 \Delta}} \text { BesselK } \left(0, \frac {3 \Gamma^ {2}}{4 \Delta^ {2}}\right)
$$

$$
\left(\text { when } \Phi_ {p r} (\omega_ {p r}) = \arctan (\omega_ {p r} / \Gamma)\right) \tag {13}
$$

and the equality only holds when $\Phi _ { p }$ and $\Phi _ { s }$ are constant and $\Phi _ { p r } ( \omega _ { p r } ) = \arctan ( \omega _ { p r } / \Gamma )$ . When $\Delta _ { p } , \Delta _ { p r } ,$ and $\Delta _ { s }$ are different, this conclusion still holds. Hence the maximal resonant signal is only achieved when the pump and Stoke pulse are unshaped TLPs, and the phase of the probe pulse takes the form $\Phi _ { p r } ( \omega _ { p r } ) = \arctan ( \omega _ { p r } / \Gamma )$ . This fact means that a two-pulse or three-pulse shaping scheme is not necessary to achieve an optimal resonant signal, which was also verified by numerical simulations as shown in Fig. 5. The CMA-ES algorithm, which is reliable for global optimization, is employed in the numerical optimization. In agreement with the above analytical result, it is found that the configuration of TLPs for the pump and Stoke pulses and the arctan $( \omega _ { p r } / \Gamma )$ phase profile for the probe pulse is optimal to maximize the resonant signal.

![](images/227a306ce139015e3950950b473bff18a35099cb157670691c51e69df07ab06f.jpg)

<details>
<summary>line chart</summary>

| ωk/cm⁻¹ | Phase/rad (Pump) | Phase/rad (Stokes) | Phase/rad (Probe) | Phase/rad (arctan(ωpr/Γ)) |
| ------- | ---------------- | ------------------ | ----------------- | -------------------------- |
| -100    | -1.5             | -1.5               | -1.5              | -1.5                       |
| -50     | -1.0             | -1.0               | -1.0              | -1.0                       |
| 0       | 0.0              | 0.0                | 0.0               | 0.0                        |
| 50      | 1.5              | 1.5                | 1.5               | 1.5                        |
| 100     | 1.5              | 1.5                | 1.5               | 1.5                        |
</details>

![](images/f4b9fd00e873c4998acbe51d7b10d6564fbdbbee085365c70ad9233b8927d94d.jpg)

<details>
<summary>line chart</summary>

| Time/ps | Pump | Stokes | Probe | arctan(ω_pr/Γ) |
| ------- | ---- | ------ | ----- | -------------- |
| -1      | 0    | 0      | 0     | 0              |
| 0       | 1    | 1      | 0     | 1              |
| 1       | 0    | 0      | 0     | 0              |
</details>

FIG. 5. Numerical optimal phase functions for achieving a maximal resonant signal with three-pulse CARS using different pulse bandwidths: $\Delta _ { p } = 1 2 5 \mathrm { c m } ^ { - 1 }$ , $\Delta _ { s } = 1 0 0 \mathrm { c m } ^ { - 1 }$ 1, $\Delta _ { p r } = 8 0 \mathrm { c m } ^ { - 1 }$ . The top and bottom panels correspond to the frequency and time domains, respectively. The arctan( $\omega _ { p r } / \Gamma )$ phase (black solid lines) is also shown for comparison.

## D. Control of the signal-background difference by shaping the probe pulse

In the subsections above, the optimization of the resonant signal and non-resonant background is treated separately. In the laboratory, however, the signal and background are always detected together. As they cannot simultaneously reach extreme values, it is necessary to study the balance between resonant signal enhancement and non-resonant background suppression, which is a multi-objective optimization problem. In this subsection, we will show how to achieve this goal by shaping the probe pulse.

For this multi-objective problem, it is natural to consider the optimization of the signal-to-background ratio. However, the ratio $( | P _ { r } | / | P _ { n r } | )$ is not a good choice: it could become infinite when $| P _ { n r } | = 0$ , no matter how small $| P _ { r } |$ is. In this work, the difference of the resonant signal and nonresonant background intensities is chosen as the objective functional

$$
J = | P _ {r} | ^ {2} - k   | P _ {n r} | ^ {2}, \tag {14}
$$

where k is the weight factor. This objective functional J is the balance of the minimization of $| P _ { n r } | ^ { 2 }$ and maximization of $| P _ { r } | ^ { 2 }$ . By maximizing the intensity difference, a large signal-to-background ratio can be achieved with significant resonant signal intensity.

According to the variational method, the necessary condition for a stationary point of J is

$$
\frac {\delta J}{\delta \Phi_ {p r} (\omega_ {p r})} = 0. \tag {15}
$$

Numerical results indicate that the optimal phase $\Phi _ { p r } ( \omega _ { p r } )$ is an odd function of $\omega _ { p r }$ . After a detailed analysis shown in Appendix B, it is found that the optimal phase for maximizing J is a modified arctan-type function,

$$
\Phi_ {p r} (\omega_ {p r}) = \arctan \left(\frac {\omega_ {p r}}{\Gamma - \lambda \gamma (\omega_ {p r} ^ {2} + \Gamma^ {2})}\right) + \theta , \tag {16}
$$

where $\lambda = k ( \chi _ { n r } / C ) ^ { 2 } , \omega _ { p r } = \tilde { \omega } _ { p r } - \Omega _ { p r } , \gamma$ (dependent on λ) is a parameter determined in Eq. (B9) of Appendix B, and θ is a trivial phase angle. When the weight factor $k = 0 .$ , the optimization of J reduces to the maximization of resonant signal, and its solution arctan $\langle \omega _ { p r } / \Gamma )$ is also consistent with the result in Eq. (6). With parameters $C = 1$ and $\chi _ { n r } = 0 . 1$ , the numerical optimal phases for maximizing $| P _ { r } | ^ { 2 } - k | P _ { n r } | ^ { 2 }$ with different $k$ are shown in the top panel of Fig. 6. It is easy to see that the Pareto surface of J in the bottom panel of Fig. $^ { 6 , }$ which is defined as the set of optimal points $( | P _ { r } ( k ) | ^ { 2 }$ , $| P _ { n r } ( k ) | ^ { 2 } )$ for maximal J with different $k ,$ has two limit points. In the first limit, the pure maximization of $| P _ { r } | ^ { 2 }$ without considering $| P _ { n r } | ^ { 2 }$ leads to $| P _ { r } | ^ { 2 }$ reaching its maximal value of 0.828 while $| P _ { n r } | ^ { 2 }$ has a considerable value of 0.19, and the phase function is arctan $\scriptstyle { | \omega _ { p r } / \Gamma ) }$ . If $\chi _ { n r }$ is large in this case, $| P _ { n r } | ^ { 2 }$ is large as well, e.g., when $\chi _ { n r } = 1 . 0$ , then $| P _ { n r } | ^ { 2 } = 1 . 9$ . Hence, the choice of $k = 0$ will not achieve an optimal balance of resonant signal enhancement and non-resonant background suppression in general cases with a large background. In the second case when k becomes large, then $| P _ { r } | ^ { 2 }$ approaches its lower limiting value of 0.765 while $| P _ { n r } | ^ { 2 }$ is very small, and the phase function also approaches a limiting curve as indicated with the red color in the top panel of Fig. 6. In this case, the background could almost be eliminated while keeping a considerable resonant signal intensity. Section II A showed the π step phase could also eliminate the background, but it produced a relatively small resonant signal intensity $| P _ { r } | ^ { 2 }$ $= ~ 0 . 4 5$ (with the same parameters as here). Hence, the π step phase is not a good Pareto optimal solution for the optimization of J, although it is widely used in experiments.

![](images/d95486b3bb002b9704766deb325c4d190c112eaac21d87148580fd361f632c81.jpg)  
FIG. 6. (Top panel): Numerical optimal phase function of the probe pulse for $| P _ { r } | ^ { 2 } - \dot { k } | P _ { n r } \dot { | } ^ { 2 }$ with different weights k. The color of the lines indicates the value of k, which is represented in the color bar on the right corresponding to log10 $( k + 0 . 1 )$ . All the phase functions in this figure could significantly suppress the background. (Bottom panel): The Pareto surface for the optimization of signal enhancement and background suppression. With different weights $k ,$ the value of $| P _ { r } | ^ { 2 }$ is bounded in [0.765, 0.828], while $| P _ { n r } | ^ { 2 }$ is always much smaller than $| P _ { r } | ^ { 2 }$ .

From the analysis above, a practical choice for k can be made: (1) when $\chi _ { n r } / C$ is large (i.e., a large background), it is better to choose a large value of k, which will give a solution close to the limit point on the right side of the Pareto surface; (2) when $\chi _ { n r } / C$ is small, a small value of k is appropriate. For example, when $\chi _ { n r } / C$ approaches zero, the $k = 0$ is the best choice, in which case there is no need to consider further reducing background.

## III. BROADBAND OPTIMAL CONTROL

In Sec. II, resonant signal enhancement and non-resonant background suppression at a specific frequency was studied. However, in many experiments, a large resonant signal and low non-resonant background over the entire spectrum is designed, so the local optimal control is not adequate. In this section, we will show how to achieve broadband optimal control. The π step phase, which achieves perfect local elimination of the background, will be investigated again, and a multi-π step phase scheme is further proposed to yield better broadband background suppression. Finally, a global numerical optimized phase profile for broadband background suppression will be shown by employing a specific objective functional.

![](images/006750a58ab27417edfc3420dc1decc15fc4161ed2263b4fef0f46bdd37ba3f7.jpg)  
FIG. 7. (Top panel): The resonant signal (red dashed line), background (blue dotted line), and the whole CARS signal (black solid line) with the π step phase scheme; (Bottom panel): The π step phase profile of the probe pulse which steps about $\omega _ { p r } = 0 .$ . Parameters: $\Delta = 5 0$ cm−1, $\Gamma = 4 . 8$ cm−1.

## A. Multi-π step phase scheme

It is shown above that the π step phase $( \mathrm { H e a v i s i d e } ( \omega _ { p r } )$ · π) could completely eliminate the background at $\Omega _ { a s }$ ,which can also be achieved at another specific frequency by changing the π phase step position. The effects of the π step phase function are shown in Fig. 7. As can be seen, this phase scheme could not effectively eliminate the background at other frequency components at the same time, although it produces a good signal-to-background ratio at $\Omega _ { a s }$ , which means that the π step phase is not a good choice for broadband background elimination.

Since a single π step phase could eliminate the background locally and its effective region for background elimination is only about $\Delta / 2$ as shown in Fig. 7, it is natural to construct a multi-π step phase with jumps at several positions for broadband background suppression. Every π phase step corresponds to a local region for background suppression. Figure 8 illustrates a multi-π step phase scheme which consists of eight π steps with an equivalent spacing of $\Delta / 2$ . With this ladder-like multi-π step phase, the background is perfectly suppressed and the resonant signal remains large. The ladder shape of the multi-π step phase is close to a time delay scheme as shown by the two curves in the bottom panel of Fig. 8. In fact, similar CARS spectra are yielded by these two schemes as shown in the top panel of Fig. 8, which indicates that the time delay scheme may be good for broadband background elimination. This will be further demonstrated in Subsection III B by numerical global optimization.

![](images/ae975e335daf7162a89c32103149442743804636a14fdf23325ffbdb456c8517.jpg)

![](images/a1b4b446f5950af99d723b492c029dcb419b763fcdfb8fef4bd963033f2e8398.jpg)

<details>
<summary>line chart</summary>

| ω_pr/Δ | multi-π step phase | Time delay |
| ------ | ------------------ | ---------- |
| -2.0   | 0.0                | 0.0        |
| -1.5   | 1.0                | 1.0        |
| -1.0   | 2.0                | 2.0        |
| -0.5   | 3.0                | 3.0        |
| 0.0    | 4.0                | 4.0        |
| 0.5    | 5.0                | 5.0        |
| 1.0    | 6.0                | 6.0        |
| 1.5    | 7.0                | 7.0        |
| 2.0    | 8.0                | 8.0        |
</details>

FIG. 8. (Top panel): The resonant signal intensity $| P _ { r } |$ and non-resonant background $| P _ { n r } |$ intensity with the multi-π step phase scheme (red lines) and the time delay scheme (blue lines). (Bottom panel): The multi-π step phase profile (red solid line) and the time delay phase profile (blue dashed line).

## B. Numerical global optimization

Since it is difficult to obtain an analytical optimal phase function for broadband background suppression, a global numerical optimization of the phase profile with a specific objective functional is performed, which is defined as the difference of the integrated resonant and non-resonant signal intensities

$$
J [ \Phi_ {p r}, \Phi_ {p}, \Phi_ {s} ] = I _ {r} - I _ {n r}, \tag {17}
$$

$$
I _ {r} = \int_ {- \infty} ^ {+ \infty} | P _ {r} (\tilde {\omega} _ {a s}) | ^ {2} d \omega_ {a s}, \tag {18}
$$

$$
I _ {n r} = \int_ {- \infty} ^ {+ \infty} | P _ {n r} (\tilde {\omega} _ {a s}) | ^ {2} d \omega_ {a s}. \tag {19}
$$

The optimization of this objective functional aims for a large resonant signal while suppressing the background. Numerical optimization with respect to all three pulses is carried out with $\Delta = 5 0 \mathrm { c m } ^ { - 1 }$ and $\Gamma = 4 . 8 ~ \mathrm { c m } ^ { - 1 }$ . The optimal phase shaping configuration consists of unshaped pump and Stokes pulses and a shaped probe pulse as shown in Fig. 9. It can be seen that the optimal phase profile is quasi-linear. In other words, the time delay scheme, a well-known method for the background suppression, is quasi-optimal for broadband background elimination with the objective functional defined in Eq. (17).

To check exactly how much improvement can be made using the optimal phase scheme, the corresponding CARS spectra of resonant signal $| P _ { r } |$ and non-resonant background $| P _ { n r } |$ | with different phase shaping schemes are shown together in Fig. 10. Compared with the TLP phase scheme, both the optimal and time delay schemes can suppress the background to a low level across a broad frequency band and enhance the resonant signal around $\omega _ { a s } = 0$ . The spectra of $| P _ { r } |$ with the optimal and time delay phase schemes are almost the same except the tails away from $\omega _ { a s } = 0 ,$ , while the spectra of $| P _ { n r } |$ show that the background is suppressed more with the optimal phase scheme especially around $\omega _ { a s } = 0$ . However, this difference in the suppression of $| P _ { n r } |$ is small, which leads again to the conclusion that the time delay scheme is quasioptimal. For other types of objective functionals which place more importance on broadband background elimination, this conclusion still holds. Although the time delay scheme could not yield a narrow-band spectrum, it has almost the best performance in suppressing the broadband non-resonant background, which is especially advantageous when the background is very large. In practice, appropriate combinations of the time delay and other phase shaping schemes could achieve enhanced performance for signal-background control in CARS.

![](images/095d2b19488090a66a35389e309a6322440fe7ae6c05482bc3f1acd229fb1705.jpg)

<details>
<summary>line chart</summary>

| ω_pr/Δ | Optimal | Time delay |
| ------ | ------- | ---------- |
| -2.0   | -2.0    | -2.5       |
| -1.0   | -1.0    | -1.0       |
| 0.0    | 0.0     | 0.0        |
| 1.0    | 1.0     | 1.0        |
| 2.0    | 2.0     | 2.0        |
</details>

![](images/198d8a092e0b6245d1506fe8f1c997b937758f9212440ee1e9510484ba57f3e4.jpg)

<details>
<summary>line chart</summary>

| Time/ps | Optimal | TLP | Time delay |
| ------- | ------- | --- | ---------- |
| -2      | 0       | 0   | 0          |
| -1      | 0       | 0   | 0          |
| 0       | 1       | 1   | 1          |
| 1       | 0       | 0   | 0          |
| 2       | 0       | 0   | 0          |
</details>

FIG. 9. Optimal phase profile (with the CMA-ES algorithm) for the maximization of $I _ { r } - I _ { n r }$ . Because the numerical optimal phase function for the pump and Stokes pulses are zero phase, i.e., TLP, they are not shown in this figure. The top and bottom panels show the phase function and amplitude for the probe pulse (red solid lines) in the frequency and time domain, respectively. The unshaped TLP (blue dashed line) and quasi-optimal time delay (black dash dotted lines) schemes are also shown for comparison. Parameters: $\Delta = 5 0 \mathrm { c m } ^ { - 1 }$ and $\dot { \Gamma } = 4 . 8 ~ \mathrm { c m } ^ { - 1 }$ .

![](images/3b71656e2a395662ef35b4600453f61bba8ad58d4058d8e7f6940144980ccee3.jpg)

<details>
<summary>line chart</summary>

| ω_as / Δ | Optimal | Time delay | TLP |
| -------- | ------- | ---------- | --- |
| -2       | 0.0     | 0.0        | 0.0 |
| 0        | 0.6     | 0.6        | 0.4 |
| 2        | 0.0     | 0.0        | 0.0 |
</details>

![](images/aec0d3be836daf5db893b53f66974bdf16f38e78639ecf614b8653f02ec56618.jpg)

<details>
<summary>line chart</summary>

| ω_as / Δ | Optimal | Time delay | TLP |
| -------- | ------- | ---------- | --- |
| -2       | 0.0     | 0.0        | 0.1 |
| 0        | 0.1     | 0.15       | 1.0 |
| 2        | 0.0     | 0.0        | 0.1 |
</details>

FIG. 10. The resonant signal and non-resonant background with different phase shaping schemes for the probe pulse, while keeping pump and Stokes pulses unshaped. The optimal shaping scheme for maximal $I _ { r } - I _ { n r }$ (red solid lines), quasi-optimal time delay scheme (black dashed-dotted lines), and TLP scheme (blue dashed lines) are shown together for comparison. Parameters are the same as in Fig. 9.

## IV. CONCLUSIONS

Detailed investigations of coherent control for resonant signal enhancement and non-resonant background elimination of CARS via phase shaping schemes lead to the conclusion that the maximal resonant signal and minimal background at a specific frequency may be achieved by shaping the probe pulse only, while keeping pump and Stokes pulses unshaped. The optimal probe phase function in two-pulse CARS is approximately a superposition of linear and arctangent-type phases for the pump, which enhances the resonant signal more than other schemes. As a balance of resonant signal enhancement and non-resonant background suppression, the optimization of the objective functional $| P _ { r } ( \Omega _ { a s } ) | ^ { 2 } - k | P _ { n r } ( \Omega _ { a s } ) | ^ { 2 }$ could simultaneously generate a CARS signal with large resonant component and small background. To achieve broadband non-resonant background suppression, the difference of the integrated signal-background intensity over the entire spectrum is taken as the objective functional. It is found that the optimal phase shaping configuration consists of unshaped pump and Stokes pulses and a quasi-time-delay probe pulse. Numerical simulations show that the background is suppressed more especially around $\omega _ { a s } = 0$ with the optimal phase scheme than with the time-delay scheme. But the difference in the suppression of $| P _ { n r } |$ is small, which leads again to the conclusion that the well-known time delay scheme is a good approximation for optimal resonant signal enhancement and broadband background suppression. It is expected that performing coherent control of the resonant signal and background could help improve the performance of CARS spectroscopy and microscopy, especially when using femtosecond pulses.

There are still many open questions to answer. In this work, only the pulse shaping in the time domain is considered. The spatial resolution of CARS microscopy is diffraction limited, without employing quantum effects. Potma et al. apply the concept of focus engineering44– 47 to enhance the sensitivity of CARS microscopy to “chemical interfaces.” However, coherent control strategies by pulse-shaping in the spatial domain to improve the spatial resolution of CARS microscopy have not been given much attention. Another point is chemical selectivity in CARS microscopy. Experiments have demonstrated that not only can the CARS signals from different vibrational modes in one molecule interfere but also from different molecules. By adjusting the pulse phases, the signal from one special molecule can be effectively enhanced while that of another molecule is suppressed.15 Thus, the simultaneous enhanced chemical selectivity and spatial resolution of CARS microscopy needs to be explored systematically in the future by phase shaping in the time and spatial domains.

## ACKNOWLEDGMENTS

This work is supported by National Natural Science Foundation of China (Grant Nos. 61074052 and 61072032), Open Foundation of State Key Laboratory of Precision Spectroscopy and Foundation of President of Hefei Institutes of Physical Science, Chinese Academy of Sciences. H. Rabitz acknowledges support from Chinese Academy of Sciences Visiting Professorship for Senior International Scientists and the US National Science Foundation.

## APPENDIX A: VARIATION OF RESONANT SIGNAL

In the Appendixes, the following notations are used for clarity:

$$
\frac {1}{\sqrt {\omega^ {2} + \Gamma^ {2}}} \sin (\Phi_ {p r} (\omega) + \alpha (\omega)) = a _ {2} (\omega),
$$

$$
\frac {1}{\sqrt {\omega^ {2} + \Gamma^ {2}}} \cos (\Phi_ {p r} (\omega) + \alpha (\omega)) = b _ {2} (\omega),
$$

$$
\left\{\int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \frac {1}{\sqrt {x ^ {2} + \Gamma^ {2}}} \sin (\Phi_ {p r} (x) + \alpha (x)) d x \right\} = A _ {2},
$$

$$
\left\{\int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \frac {1}{\sqrt {x ^ {2} + \Gamma^ {2}}} \cos (\Phi_ {p r} (x) + \alpha (x)) d x \right\} = B _ {2},
$$

and

$$
\sin (\Phi_ {p r} (\omega)) = a _ {1} (\omega), \tag {A1}
$$

$$
\cos (\Phi_ {p r} (\omega)) = b _ {1} (\omega), \tag {A2}
$$

$$
\left\{\int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \sin (\Phi_ {p r} (x)) d x \right\} = A _ {1}, \tag {A3}
$$

$$
\left\{\int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \cos (\Phi_ {p r} (x)) d x \right\} = B _ {1}. \tag {A4}
$$

The variational method is used to analyze all the stationary points for $| P _ { r } | ^ { 2 }$ with respect to the phase function $\Phi _ { p r } ( \omega _ { p r } )$ . The variational condition $\delta | P _ { r } | ^ { 2 } = 0$ requires

$$
\mathbf {R e} (P _ {r} ^ {*} \delta P _ {r}) = 0. \tag {A5}
$$

From this criterion, we have

$$
\operatorname{Re} \left[ \left\{\int_ {- \infty} ^ {\infty} d x \frac {e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}}}{\sqrt {x ^ {2} + \Gamma^ {2}}} \exp \left[ - i \left(\Phi_ {p r} (x) + \alpha (x)\right) \right] \right\} \right.
$$

$$
\left. \times i \frac {e ^ {- \frac {3 \omega_ {p r} ^ {2}}{2 \Delta^ {2}}}}{\sqrt {\omega_ {p r} ^ {2} + \Gamma^ {2}}} \exp [ i (\Phi_ {p r} (\omega_ {p r}) + \alpha (\omega_ {p r})) ] \right] = 0, \tag {A6}
$$

which is equivalent to

$$
A _ {2} b _ {1} - B _ {2} a _ {1} = 0, \tag {A7}
$$

so the general extremal phase functions $\Phi _ { p r } ( \omega _ { p r } )$ for all the critical points of $| P _ { r } | ^ { 2 }$ satisfy

$$
\Phi_ {p r} (\omega_ {p r}) = L [ \omega_ {p r} ] \pi + \arctan (\omega_ {p r} / \Gamma) + \text { constant },
$$

where $L [ \omega _ { p r } ] \ \in \ \{ 0 , 1 \}$ is the integer function of $\omega _ { p r }$ . It is easy to find that when $L [ \omega _ { p r } ] = 0 \mathrm { o r } 1$ , i.e., $\Phi _ { p r } ( \omega _ { p r } )$ $= \arctan ( \omega _ { p r } / \Gamma ) +$ constant, then $| P _ { r } | ^ { 2 }$ reaches its global maximal value. When $L [ \omega _ { p r } ] =$ Heaviside $( \omega _ { p r } ) , \mathrm { i . e . , } \Phi _ { p r } ( \omega _ { p r } )$ cYanmaGent.lowb $= \arctan ( \omega _ { p r } / \Gamma ) +$ Heaviside $( \omega _ { p r } ) \cdot \pi +$ constant, $| P _ { r } | ^ { 2 }$ has its minimal value 0. Hence, the arctan $( \omega _ { p r } / \Gamma )$ phase function is the optimal solution for maximizing the peak resonant signal intensity. For the other cases of $K [ \omega _ { p r } ]$ , the phase functions are either local extremal points or saddle points. However, numerical optimization did not reveal any local extremal points, which may indicate that the control landscape42 for the resonant signal intensity is trap-free in this pure phase shaping strategy. A detailed proof of the trap-free landscape for CARS signal needs to be investigated.

## APPENDIX B: VARIATION OF THE DIFFERENCEBETWEEN THE SIGNAL AND BACKGROUND

For simplicity in the proof, we set $P _ { r 0 } = P _ { r } / C$ and $P _ { n r 0 }$ $= { P _ { n r } } / { \chi _ { n r } }$ , and introduce a parameter $\lambda = k ( \chi _ { n r } / C ) ^ { 2 }$ , then the optimization of the objective functional

$$
J = \left| P _ {r 0} \right| ^ {2} - \lambda \left| P _ {n r 0} \right| ^ {2} \tag {B1}
$$

is equivalent to optimizing the original functional Eq. (14), because $| P _ { r } | ^ { 2 } - \bar { k | } \bar { P } _ { n r } | ^ { 2 } = \bar { C } ^ { 2 } ( | P _ { r 0 } | ^ { 2 } - \lambda | P _ { n r 0 } | ^ { 2 } )$ .

Following a similar procedure to optimizing $| \boldsymbol { P } _ { r } | ^ { 2 }$ in Appendix A, the optimal phase function for J satisfies

$$
\lambda (a _ {1} B _ {1} - A _ {1} b _ {1}) = a _ {2} B _ {2} - A _ {2} b _ {2} \tag {B2}
$$

hence

$$
\tan (\Phi_ {p r} (\omega)) = \frac {a _ {1} (\omega)}{b _ {1} (\omega)} = \frac {\lambda (\omega^ {2} + \Gamma^ {2}) A _ {1} - A _ {2} \omega + B _ {2} \Gamma}{\lambda (\omega^ {2} + \Gamma^ {2}) B _ {1} - B _ {2} \omega - A _ {2} \Gamma}. \tag {B3}
$$

According to the expressions for $| P _ { r } ^ { ( 3 ) } ( \tilde { \omega } _ { a s } ) | ^ { 2 }$ and $| P _ { n r } ^ { ( 3 ) } ( \tilde { \omega } _ { a s } ) | ^ { 2 }$ , the value of J will not change if a trivial phase constant is added to $\Phi _ { p r } ( \omega _ { p r } )$ . So the general solution for maximizing J can be expressed as the sum of one special solution and a trivial phase constant. The numerical simulation in Fig. 6 shows that the optimal phase is just an odd function of $\omega _ { p r } .$ . So $\Phi _ { p r } ( \omega _ { p r } )$ to optimize J just makes sin $( \Phi _ { p r } ( \omega _ { p r } ) )$ an odd function of $\omega _ { p r }$ and cos $( \Phi _ { p r } ( \omega _ { p r } ) )$ an even function of $\omega _ { p r } ,$ thus

$$
A _ {1} = \int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \sin (\Phi_ {p r} (x)) d x = 0, \tag {B4}
$$

$$
B _ {1} = \int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \cos (\Phi_ {p r} (x)) d x \neq 0, \tag {B5}
$$

$$
\begin{array}{l} A _ {2} = \int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \frac {1}{x ^ {2} + \Gamma^ {2}} (x \cdot \sin (\Phi_ {p r} (x)) \\ + \Gamma \cos (\Phi_ {p r} (x))) d x \neq 0, \tag {B6} \\ \end{array}
$$

$$
B _ {2} = \int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \frac {1}{x ^ {2} + \Gamma^ {2}} (x \cdot \cos (\Phi_ {p r} (x))
$$

$$
- \Gamma \cdot \sin (\Phi_ {p r} (x))) d x = 0. \tag {B7}
$$

So we have

$$
\begin{array}{l} \tan (\Phi_ {p r} (\omega)) = \frac {a _ {1} (\omega)}{b _ {1} (\omega)} = \frac {- A _ {2} \omega}{\lambda (\omega^ {2} + \Gamma^ {2}) B _ {1} - A _ {2} \Gamma} \\ = \frac {\omega}{\Gamma - \lambda \frac {B _ {1}}{A _ {2}} (\omega^ {2} + \Gamma^ {2})}. \tag {B8} \\ \end{array}
$$

The special solution $\begin{array} { r } { \Phi _ { p r } ( \omega ) = \arctan ( \frac { \omega } { \Gamma - \lambda \frac { B _ { 1 } } { A _ { \gamma } } ( \omega ^ { 2 } + \Gamma ^ { 2 } ) } ) } \end{array}$ B ω1 (ω2+2) ) satisfies the assumption, so the general solution for maximal J is

$$
\Phi_ {p r} (\omega) = \arctan \left(\frac {\omega}{\Gamma - \lambda \frac {B _ {1}}{A _ {2}} \left(\omega^ {2} + \Gamma^ {2}\right)}\right) + \text { constant }.
$$

Here, we define $\gamma = B _ { 1 } / A _ { 2 }$ , which could not be determined analytically and was determined by iteratively solving the equation

$$
\frac {B _ {1}}{A _ {2}} = \frac {\left\{\int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \cos \left(\arctan \left(\frac {x}{\Gamma - \lambda \gamma (x ^ {2} + \Gamma^ {2})}\right)\right) d x \right\}}{\left\{\int_ {- \infty} ^ {\infty} e ^ {- \frac {3 x ^ {2}}{2 \Delta^ {2}}} \frac {1}{\sqrt {x ^ {2} + \Gamma^ {2}}} \sin \left(\arctan \left(\frac {x}{\Gamma - \lambda \gamma (x ^ {2} + \Gamma^ {2})}\right) + \alpha (x)\right) d x \right\}} = \gamma . \tag {B9}
$$

Given parameters λ, , and , we can always get the numerical value of $\gamma$ .

1P. Maker and R. Terhune, Phys. Rev. 137, A801 (1965).  
2M. Duncan, J. Reintjes, and T. Manuccia, Opt. Lett. 7, 350 (1982).  
3J.-X. Cheng, A. Volkmer, L. Book, and X. Xie, J. Phys. Chem. B 105, 1277 (2001).  
4A. Volkmer, J.-X. Cheng, and X. Xie, Phys. Rev. Lett. 87, 023901 (2001).  
5J.-X. Cheng and X. Xie, J. Phys. Chem. B 108, 827 (2004).  
6C. Evans and X. Xie, Annu. Rev. Anal. Chem. 1, 883 (2008).  
7E. O. Potma, X. S. Xie, L. Muntean, J. Preusser, D. Jones, J. Ye, S. R. Leone, W. D. Hinsberg, and W. Schade, J. Phys. Chem. B 108, 1296 (2004).  
8N. Dudovich, D. Oron, and Y. Silberberg, Nature (London) 418, 512 (2002).  
9N. Dudovich, D. Oron, and Y. Silberberg, J. Chem. Phys. 118, 9208 (2003).  
10T. Lang, M. Motzkus, H. M. Frey, and P. Beaud, J. Chem. Phys. 115, 5418 (2001).  
11T. Lang and M. Motzkus, J. Opt. Soc. Am. B 19, 340 (2002).  
12D. Oron, N. Dudovich, D. Yelin, and Y. Silberberg, Phys. Rev. Lett. 88, 063004 (2002).  
13D. Oron, N. Dudovich, D. Yelin, and Y. Silberberg, Phys. Rev. A 65, 043408 (2002).  
14J. Konradi, A. Singh, and A. Materny, Phys. Chem. Chem. Phys. 7, 3574 (2005).  
15J. Konradi, A. Singh, and A. Matemy, J. Photochem. Photobiol., A 180, 289 (2006).  
16J. Konradi, A. Singh, A. Scaria, and A. Materny, J. Raman Spectrosc. 37, 697 (2006).  
17S. Zhang, L. Zhang, X. Zhang, L. Ding, and G. Chen, Chem. Phys. Lett. 433, 416 (2007).  
18S. Akhmanov, A. Bunkin, and S. Ivanov, and N. Koroteev, JETP Lett. 25, 416 (1977).  
19J.-L. Oudar, R. Smith, and Y. Shen, Appl. Phys. Lett. 34, 758 (1979).  
20H.-G. Purucker, V. Tunkin, and A. Laubereau, J. Raman Spectrosc. 24, 453 (1993).  
21J.-X. Cheng, L. Book, and X. Xie, Opt. Lett. 26, 1341 (2001).  
22A. Materny, T. Chen, M. Schmitt, and T. Siebert, Appl. Phys. B 71, 299 (2000).  
23D. Pestov, R. Murawski, G. Ariunbold, X. Wang, M. Zhi, A. Sokolov, V. Sautenkov, Y. Rostovtsev, A. Dogariu, Y. Huang, and M. Scully, Science 316, 265 (2007).  
24M. Wefers and K. Nelson, Opt. Lett. 20, 1047 (1995).  
25H. Kawashima, M. Wefers, and K. Nelson, Annu. Rev. Phys. Chem. 46, 627 (1995).  
26A. Weiner, Rev. Sci. Instrum. 71, 1929 (2000).  
27D. Zeidler, S. Frey, W. Wohlleben, M. Motzkus, F. Busch, T. Chen, W. Kiefer, and A. Materny, J. Chem. Phys. 116, 5231 (2002)  
28D. Oron, N. Dudovich, and Y. Silberberg, Phys. Rev. Lett. 90, 213902 (2003).  
29S.-H. Lim, A. G. Caster, and S. R. Leone, Phys. Rev. A 72, 041803 (2005).  
30S.-H. Lim, A. G. Caster, O. Nicolet, and S. R. Leone, J. Phys. Chem. B 110, 5196 (2006).  
31M. Jurna, J. P. Korterik, C. Otto, J. L. Herek, and H. L. Offerhaus, Phys. Rev. Lett. 103, 043905 (2009).  
32M. Jurna, E. T. Garbacik, J. P. Korterik, J. L. Herek, C. Otto, and H. L. Offerhaus, Anal. Chem. 82, 7656 (2010).  
33B. von Vacano, T. Buckup, and M. Motzkus, Opt. Lett. 31, 2495 (2006).  
34E. M. Vartiainen, H. A. Rinia, M. Müller, and M. Bonn, Opt. Express 14, 3622 (2006).  
35H. A. Rinia, M. Bonn, and M. Müller, J. Phys. Chem. B 110, 4472 (2006).  
36J. P. R. Day, K. F. Domke, G. Rago, H. Kano, H. Hamaguchi, E. M. Vartiainen, and M. Bonn, J. Phys. Chem. B 115, 7713 (2011).  
37Y. Liu, Y. J. Lee, and M. T. Cicerone, Opt. Lett. 34, 1363 (2009).  
38Y. J. Lee, D. Moon, K. B. Migler, and M. T. Cicerone, Anal. Chem. 83, 2733 (2011).  
39B.-C. Chen and S.-H. Lim, J. Phys. Chem. B 112, 3653 (2008).  
40Y. Silberberg, Annu. Rev. Phys. Chem. 60, 277 (2009).  
41H. Rabitz, M. Hsieh, and C. Rosenthal, Science 303, 1998 (2004).  
42A. Ostermeier, A. Gawelczyk, and N. Hansen, Evol. Comput. 2, 369 (1994).  
43N. Hansen, Stud. Fuzziness Soft Comput. 192, 75 (2006).  
44V. V. Krishnamachari and E. O. Potma, J. Opt. Soc. Am. A 24, 1138 (2007).  
45V. V. Krishnamachari and E. O. Potma, Chem. Phys. 341, 81 (2007).  
46V. V. Krishnamachari and E. O. Potma, J. Raman Spectrosc. 39, 593 (2008).  
47V. V. Krishnamachari and E. O. Potma, Vib. Spectrosc. 50, 10 (2009).