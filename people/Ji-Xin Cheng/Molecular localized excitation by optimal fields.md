# Molecular localized excitation by optimal fields

Chen Yang, Ji-xin Cheng \*, Qing-shi Zhu

Laboratory of Bond-selecti6e Chemistry, Department of Chemical Physics, Uni6ersity of Science and Technology of China, Hefei, Anhui, , China

Received 15 September 1998; received in revised form 27 January 1999; accepted 27 January 1999

## Abstract

With the optimal control theory, a general model is built up for selective excitation of a vibrational wave packet in the eigenstate representation. The control equation in terms of Hilbert-space wave function evolution is obtained and the form of the globally optimal field in the weak response regime is derived. Based on the intramolecular dynamics information obtained from high-resolution spectroscopy, numerical implementations for selective excitation of the C–H bond in the $\mathrm { C F } _ { 3 } \mathrm { H }$ molecule are carried out. © 1999 Elsevier Science B.V. All rights reserved.

Keywords Optimal control; Wave packet; CF H; Local mode; Bond-selective

A prerequisite of realizing bond-selective chemistry is to prepare a state that localizes energy in some part of the reagent molecule [1]. Selective breaking of chemical bonds has been achieved by localized vibrational excitation in a specific bond of HOD [2,3], or by localized electronic excitation in CH IBr and CH SH [4–6]. This method is, however, called passive control because it does not make use of the coherent property of light. In the last decade various scenarios for active control of molecular dynamics have been developed. Brumer and Shapiro proposed a coherent control theory based on the principle of quantum mechanical interference between competing reaction paths [7]. Tannor and Rice suggested a pumpdump control scheme that utilizes a sequence of light pulses to drive a molecule to a desired state [8,9]. The general optimal control theory was employed by Rabitz [10], Kosloff [11], Yan [12] and their co-workers in order to search for the optimal laser fields that maximize the control yield at a specific time under certain constraints. On the other hand, the high resolution and high sensitivity spectroscopy has provided rich information of isolated intramolecular dynamics in the high vibrational energy region [13,14]. The optimal control theory together with the spectroscopic information enables us to find suitable laser fields that excite a specific bond.

The aim of control in the present work is to produce a wave packet corresponding to single bond vibration (or so-called local mode vibration). We shall first present the general form of the optimal field for controlling a vibrational wave packet and then implement it in the selective excitation of the C–H bond in the $\mathrm { C F } _ { 3 } \mathrm { H }$ molecule.

Let us consider a molecular vibrational system which consists of the ground state $\left. \mathbf { g } \right.$ and n excited states $| \mathbf { e } _ { i } \rangle , \ i = 1 , \ 2 . . . n .$ . The molecule is initially in the ground state with energy $\hbar \omega _ { \mathrm { g } } .$ The field-molecule Hamiltonian in the presence of an external field $\varepsilon ( t )$ can be written as

$$
H (t) = H _ {\mathrm{m}} - D \varepsilon (t) \tag {1}
$$

Here, $H _ { \mathrm { m } }$ is the vibrational Hamiltonian,

$$
H _ {\mathrm{m}} = \hbar \omega_ {\mathrm{g}} | \mathbf {g} \rangle \langle \mathbf {g} | + \sum_ {i = 1} ^ {n} \hbar (\omega_ {i} + \omega_ {\mathrm{g}}) | \mathbf {e} _ {i} \rangle \langle \mathbf {e} _ {i} |, \tag {2}
$$

where $\omega _ { i }$ is the transition frequency from $\left. \mathbf { g } \right.$ to $\left. \mathrm { e } _ { i } \right.$ . The transition dipole operator assumes the following form,

$$
D = \sum_ {i = 1} ^ {n} \mu_ {i} | \mathrm{e} _ {i} \rangle \langle \mathrm{g} | + h. c. \tag {3}
$$

Our goal is to excite a desired wave packet, $\phi = \Sigma _ { i = 1 } ^ { n } \ a _ { i } | e _ { i } \rangle$ , at a specific time $t _ { \mathrm { f } } .$ The target operator can be written as $\hat { A } = | \phi \rangle \langle \phi |$ . In order to find the optimal excitation field, we consider the control functional [12],

$$
J (t _ {\mathrm{f}}) = A (t _ {\mathrm{f}}) - \frac {1}{2} \lambda \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \mathrm{d} \tau \varepsilon^ {2} (\tau) \tag {4}
$$

$A \left( t _ { \mathrm { f } } \right)$ is the expectation value of the target operator at time $t _ { \mathrm { f } } ,$

$$
A (t _ {\mathrm{f}}) = \left\langle \psi (t _ {\mathrm{f}}) | \phi \right\rangle \left\langle \phi | \psi (t _ {\mathrm{f}}) \right\rangle \tag {5}
$$

Here, $\vert \psi ( t _ { \mathrm { f } } ) \rangle = G ( t _ { \mathrm { f } } , t _ { 0 } ) \vert \psi ( t _ { 0 } ) \rangle$ , where the Hilbertspace propagator G is governed by the total Hamiltonian $H ( t )$ . The second term in the right side of Eq. (4) is the penalty function characterized by a constant weight l. In our case, the penalty is simply the constraint on the field energy. If a certain shape of control field is favored in the optimization process the constant l should be replaced by a time-dependent cost penalty function $\lambda ( \tau )$ [10,12,15]. The variation of $J ( t _ { \mathrm { f } } )$ with respect to o(t) is given by

$$
\delta J (t _ {\mathrm{f}}) = \delta A (t _ {\mathrm{f}}) - \lambda \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \mathrm{d} \tau \varepsilon (\tau) \delta \varepsilon (\tau) \tag {6}
$$

By exploiting variation of Green functions,

$$
\delta G (t _ {\mathrm{f}}, t _ {0}) = (- i / \hbar) \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} G (t _ {\mathrm{f}}, \tau) \delta H (\tau) G (\tau , t _ {0}) \mathrm{d} \tau , \tag {7}
$$

we have

$$
\delta A (t _ {\mathrm{f}}) = 2 \operatorname{Re} \left[ (- i / \hbar) \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \mathrm{d} \tau \left\langle \psi (t _ {\mathrm{f}}) \mid \phi \right\rangle \right.
$$

$$
\left. \left\langle \phi (| \tau t _ {\mathrm{f}}) | \delta H (\tau) | \psi (\tau) \right\rangle \right] \tag {8}
$$

According to the total Hamiltonian in Eq. (1), we have $\delta H ( \tau ) = - D \delta \mathfrak { s } ( \tau )$ . c(t) and $\phi ( \tau , \ t _ { \mathrm { f } } )$ is the forward- and backward-propagated wave functions for the system and target, respectively. By substituting Eq. (8) into Eq. (6) and applying the variation principle, $\delta J ( t _ { \mathrm { f } } ) = 0$ , we obtain the control equation for the optimal field as [16]

$$
2 \operatorname{Re} [ c ^ {*} (t _ {\mathrm{f}}) f (\tau ; t _ {\mathrm{f}}) ] = \lambda \varepsilon (\tau) \tag {9}
$$

Note that we have introduced the complex control yield $c ( t _ { \mathrm { f } } ) = \langle \phi | \psi ( t _ { f } ) \rangle$ , and the Hilbert-space control kernel, $f ( \tau ; \ t _ { \mathrm { f } } ) = i / \hbar \langle \phi ( \tau , \ t _ { \mathrm { f } } ) | D | \psi ( \tau ) \rangle$ .

In the weak response regime, we only consider the zero-order control kernel,

$$
f ^ {(0)} (\tau ; t _ {\mathrm{f}}) = (i / \hbar) \left\langle \phi^ {(0)} (\tau , t _ {\mathrm{f}}) \mid D \mid \psi^ {(0)} (\tau) \right\rangle
$$

$$
= (i / \hbar) \mathrm{e} ^ {- i \omega_ {\mathrm{g}} (t _ {\mathrm{f}} - t _ {0})} f _ {\mathrm{e}} (t _ {\mathrm{f}} - \tau), \tag {10}
$$

and the first-order control yield,

$$
\begin{array}{l} c ^ {(1)} (t _ {\mathrm{f}}) = \left\langle \phi \left| \psi^ {(1)} (t _ {\mathrm{f}}) \right. \right\rangle \\ = (i / \hbar) \mathrm{e} ^ {- i \omega_ {\mathrm{g}} (t _ {\mathrm{f}} - t _ {0})} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} f _ {\mathrm{e}} (t _ {\mathrm{f}} - \tau) \varepsilon (\tau) \mathrm{d} \tau \tag {11} \\ \end{array}
$$

$f _ { \mathrm { e } } ( t )$ in Eqs. (10) and (11) is given by

$$
f _ {\mathrm{e}} (t) = \left\langle \phi \right| \mathrm{e} ^ {- i \left(H _ {\mathrm{m}} - \hbar \omega_ {\mathrm{g}}\right) t / \hbar} D | \mathrm{g} \rangle \tag {12}
$$

It can be proved that the phase of $c ^ { ( 1 ) } ( t _ { \mathrm { f } } )$ has no effect on the control dynamics and can be set as zero [16]. Combining Eqs. (9)–(11), we obtain the simple form of the globally optimal field in the weak response regime [8,17],

$$
\varepsilon (\tau) \propto \mathrm{Re} [ \left\langle \phi \right| \mathrm{e} ^ {- i (H _ {\mathrm{m}} - \hbar \omega_ {\mathrm{g}}) (t _ {\mathrm{f}} - \tau) / \hbar} D | \mathrm{g} \rangle ] \tag {13}
$$

Upon substitution of $\phi$ and $D$ with their expressions, we arrive at the final form of the optimal field for exciting the wave packet $\phi _ { ; }$ ,

$$
\varepsilon (\tau) \propto \sum_ {i = 1} ^ {n} a _ {i} \mu_ {i} [ \mathrm{e} ^ {- i \omega_ {i} (t _ {\mathrm{f}} - \tau)} + \mathrm{e} ^ {i \omega_ {i} (t _ {\mathrm{f}} - \tau)} ] \tag {14}
$$

Eq. (14) indicates that o(t) can be viewed as coherent superposition of n cw components. Each component excites a particular eigenstate $\left. \mathrm { e } _ { i } \right.$ and has defined intensity of $( a _ { i } \mu _ { i } ) ^ { 2 }$ and phase of $\omega _ { i } t _ { \mathrm { f } } .$ The field $\varepsilon ( \tau )$ in Eq. (14) drives the molecular system optimally to the target wave packet $\phi$ at time $t _ { \mathrm { f } } .$ Noted that Eq. (14) is similar to the previous results of Rabitz et al. [18,19], who derived the weak-response form of the optimal field for a d-target in the coordinate space.

The $\mathrm { C F } _ { 3 } \mathrm { H }$ molecule is a good example of rapid intramolecular vibrational relaxation via Fermi resonance between the CH stretching mode s and a bending mode b [20]. In a Hamiltonian block with the chromophore quantum number $N = v _ { s } +$ $v _ { b } / 2$ , we have $N + 1$ zero-order states, $\begin{array} { r } { { v _ { s } , v _ { b , \astrosun } l _ { b } = } } \end{array}$ 0, $v _ { s } = 0 ,$ , 1,… N, that are connected by Fermi coupling. By diagonalizing a triangle Hamiltonian, one can obtain N+1 eigenstates, $\left| N _ { m } \right.$ , $m = 0 , 1 . . . N .$ For the N=3 polyad, according to Du¨bal and Quack’s experiments and calculations [20], the C–H stretching state 3, 0, 0 can be written as

$$
\left| 3, 0, 0 \right\rangle = 0. 7 2 7 \left| 3 _ {0} \right\rangle - 0. 6 5 7 \left| 3 _ {1} \right\rangle + 0. 1 9 9 \left| 3 _ {2} \right\rangle
$$

$$
- 0. 0 3 0 \left| 3 _ {3} \right\rangle \tag {15}
$$

The transition frequencies and the relative intensities $( g _ { i } \propto \mu _ { i } ^ { 2 } )$ of the $3 _ { m } ~ ( m = 0 , 1 , 2$ and 3) bands are listed in Table 1.

With the information in Eq. (15) and Table 1, we can compute the optimal field for selective excitation of the C–H bond in $\mathrm { C F } _ { 3 } \mathrm { H }$ by Eq. (14). For the case of $t _ { \mathrm { f } } = 1 0 0 \ \mathrm { f s }$ , the form of the optimal field is shown in Fig. 1. In the presence of the external field, the population P in the wave packet $\phi = | 3 , 0 , 0 \rangle$ is determined by $P = \vert \langle \phi \vert \mathrm { e } ^ { - i H \hat { t } / \hbar } \vert \mathbf { g } \rangle \vert ^ { 2 }$ , here H is the time-dependent Hamiltonian in Eq. (1). The control quality is evaluated by the achievement function defined as [12]

Table 1 The band centers (v ) and relative intensities $( \mathbf { g } _ { i } ^ { \mathrm { e x p } } \propto \mu _ { i } ^ { 2 } )$ for the N=3 polyad of the $\mathrm { C F } _ { 3 } \mathrm { H }$ molecule

<table><tr><td> $j$ </td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td> $ω_{j} \text{ cm}^{-1}$ </td><td>8792.70</td><td>8589.28</td><td>8286.0</td><td>7890</td></tr><tr><td> $g_{j}^{\text{exp}}$ </td><td>0.52</td><td>0.45</td><td>0.03</td><td>&lt;0.01</td></tr></table>

![](images/832353462c9509919baa2ffc2719b8fb406c29e4a3827588daf5ba6a482a4f4c.jpg)

<details>
<summary>line chart</summary>

| Time t / fs | ε(t) |
| ----------- | ---- |
| 0           | High |
| 10          | Low  |
| 20          | High |
| 30          | Low  |
| 40          | High |
| 50          | Low  |
| 60          | High |
| 70          | Low  |
| 80          | High |
| 90          | Low  |
| 100         | High |
</details>

Fig. 1. The globally optimal field for selective excitation of the C–H bond in the $\mathrm { \bar { C F } _ { 3 } H }$ molecule.

![](images/c8ccf86da439052886821bd65bdfc46b07b6597e3d72c8af88ce1afa35d86d9a.jpg)

<details>
<summary>line chart</summary>

| Time t / fs | α(t) |
| ----------- | ---- |
| 0           | 0.0  |
| 20          | 0.1  |
| 40          | 0.3  |
| 60          | 0.5  |
| 80          | 0.7  |
| 100         | 0.9  |
</details>

Fig. 2. The achievement a(t) versus time for the globally optimal field.

$$
\alpha^ {2} (t) = \left| \left\langle \phi \mid \psi_ {\mathrm{e}} (t) \right\rangle \right| ^ {2} / \left[ \left\langle \phi \mid \phi \right\rangle \left\langle \psi_ {\mathrm{e}} (t _ {\mathrm{f}}) \mid \psi_ {\mathrm{e}} (t _ {\mathrm{f}}) \right\rangle \right] \tag {16}
$$

Here, $\psi _ { \mathrm { e } } ( t )$ is the wave function in the excited states. Fig. 2 shows the achievement a(t) for the optimal field. It can be seen that a increases gradually with time and is close to 1.0 at the target time. This indicates that almost all the vibrational energy is localized in the C–H bond.

## Acknowledgements

The support of the National Natural Science Foundation of China is gratefully acknowledged. The authors thank Professor Yijing Yan in Hong

Kong University of Science and Technology for helpful discussions and a critical reading of the manuscript.

## References

[1] R.N. Zare, Science 279 (1998) 875.  
[2] A. Sinha, R.L. Vander Wal, F.F. Crim, J. Chem. Phys. 92 (1990) 401.  
[3] A. Sinha, J.D. Thoemke, F.F. Crim, J. Chem. Phys. 96 (1992) 372.  
[4] L.J. Butler, E.J. Hintsa, Y.T. Lee, J. Chem. Phys. 84 (1986) 4104.  
[5] L.J. Butler, E.J. Hintsa, S.F. Shane, Y.T. Lee, J. Chem. Phys. 86 (1987) 2051.  
[6] J.S. Keller, P.W. Kash, E. Jensen, L.J. Butler, J. Chem. Phys. 96 (1992) 4324.  
[7] M. Shapiro, P. Brumer, Int. Rev. Phys. Chem. 13 (1994) 187.  
[8] D.J. Tannor, S.A. Rice, J. Chem. Phys. 83 (1985) 5013.  
[9] D.J. Tannor, R. Kosloff, S.A. Rice, J. Chem. Phys. 85 (1986) 5805.  
[10] H. Rabitz, S. Shi, Adv. Mol. Vib. Collis. Dyn. 1A (1991) 187.  
[11] R. Kosloff, S.A. Rice, P. Gaspard, S. Tersigni, D.J. Tannor, Chem. Phys. 139 (1989) 201.  
[12] Y.J. Yan, R.E. Gillilan, R.M. Whitnell, K.R. Wilson, S. Mukamel, J. Phys. Chem. 97 (1993) 2320.  
[13] M. Quack, Annu. Rev. Phys. Chem. 41 (1990) 493.  
[14] K.K. Lehmann, G. Scoles, B.H. Pate, Annu. Rev. Chem. Phys. 45 (1994) 241.  
[15] S. Shi, H. Rabitz, Chem. Phys. 139 (1989) 185.  
[16] Y.J. Yan, Z.W. Shen, Y. Zhao, Chem. Phys. 233 (1998) 191.  
[17] Y.J. Yan, Annu. Rep. (R. Soc. Chem.) C94 (1998) 397.  
[18] V. Dubov, H. Rabitz, Chem. Phys. Lett. 235 (1995) 309.  
[19] V. Dubov, H. Rabitz, J. Chem. Phys. 103 (1995) 8412.  
[20] H.R. Dubal, M. Quack, J. Chem. Phys. 81 (1984) 3779.