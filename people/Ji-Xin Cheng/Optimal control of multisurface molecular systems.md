RESEARCH ARTICLE | AUGUST 01 1998

## Optimal control of multisurface molecular systems

![](images/df6d3f05d88c39fe9fdc3a8532c3e36d5d24060f913da20466cc5bf1f2bf039f.jpg)

Jixin Cheng; Zhenwen Shen; YiJing Yan

![](images/d048e2908889e3a41642ee60c15b24a2e64aa64e58b066ba4e92c9f342354a95.jpg)

Check for updates

J. Chem. Phys. 109, 1654–1662 (1998)

https://doi.org/10.1063/1.476740

![](images/acc68e1db3e479a99d35ade2e9193395d23c23af30e657bcd0b6b1768b58d72d.jpg)  
View Online

![](images/64e1bbd29932e5dbb40ebb1007a9191c0177df8099321bf00ba6721879306034.jpg)  
Export Citation

## Articles You May Be Interested In

Optimal control of curve-crossing systems

J. Chem. Phys. (February 1992)

The Hermite correction method for nonadiabatic transitions

J. Chem. Phys. (July 1999)

Quantum wavepacket ab initio molecular dynamics: Generalizations using an extended Lagrangian treatment of diabatic states coupled through multireference electronic structure

J. Chem. Phys. (November 2010)

![](images/fd9b0ced174a7d40c01844d904dbf7d2f4bea70fe89c190219a91bd8f8630a1c.jpg)

<details>
<summary>natural_image</summary>

Abstract digital artwork with flowing light streaks against a dark background, no text or symbols present
</details>

## AIP Advances

Why Publish With Us?

![](images/ad3d04aa68b678d40dcf01506c57b7952adf5e10b5c6edee1c0e7f78c5ba432f.jpg)  
21DAYS
average time
to 1st decision

![](images/411dcea69ceea83d2c7cebee9407ce8a17aa93d69eccae30f4adcde0b8361832.jpg)  
OVER 4 MILLION
views in the last year

![](images/c41a9f7d9971915f5d8a169cba59da87e07246d5e4c9b2eaea171b3effaea4c4.jpg)  
INCLUSIVE
scope

Learn More

![](images/4c02adf72e584f0741c3819fcd5e8b7bf770f2650727ecfc8e182c2aa534af7a.jpg)  
AIP Publishing

# Optimal control of multisurface molecular systems

Jixin Cheng

Department of Chemistry, Hong Kong University of Science and Technology, Kowloon, Hong Kong and Open Laboratory of Bond-Selective Chemistry, University of Science and Technology of China, Hefei, China

Zhenwen Shen

Department of Chemistry, Hong Kong University of Science and Technology, Kowloon, Hong Kong

YiJing Yan

Department of Chemistry, Hong Kong University of Science and Technology, Kowloon, Hong Kong and Open Laboratory of Bond-Selective Chemistry, University of Science and Technology of China, Hefei, China

(Received 7 April 1998; accepted 22 April 1998)

We report a theoretical framework for the study of the optimal control of multisurface molecular systems via a set of nondegenerate excitation fields. The resulting control equations in the strong response regime are presented in terms of both the Liouville-space density matrix dynamics and the Hilbert-space wave function evolution. We further derive a pair of eigenequations for the optimal pump-pump fields in the pure-state control of three-surface molecular systems in the weak response regime. The globally optimal pair of pump-pump fields in this case are identified. Application to the control of a rovibronic level on the final excited surface reveals a symmetry relation within the optimal pair of pump-pump fields in the weak response regime. For numerical demonstrations, we consider the control of the $I_{2}$ molecular system involving the initial ground X, the intermediate B, and the final E surface. The target is chosen as an outgoing vibrational wave packet in the bound region of the final E electronic state. The optimal control fields in both the strong and weak response regimes are calculated and further parameterized to fit simple experimentally realizable laser pulses.

© 1998 American Institute of Physics. [S0021-9606(98)01829-7]

## I. INTRODUCTION

Using light to actively control the molecular dynamic events has been one of the main activities in laser chemistry for decades. The central idea of active control is to exploit the coherence property of light to interfere with the quantum matter wave. Tannor and Rice $^{1}$ have proposed a time-domain active control scheme based on the sequential pump-dump excitation processes. In this control scheme, the reaction selectivity is achieved by the proper timing of the second (dump) pulse which synchronizes the evolution of the pump-excited wave packet into the desired product Franck-Condon region. $^{1-3}$ Brumer and Shapiro $^{4,5}$ have developed a frequency-domain active control scheme based on the direct consequence of matter-light interference. They have shown that, in a molecular system having a degenerate doorway to different products, the reaction selectivity can be controlled by varying the relative phases and amplitudes of several light fields which excite the molecule into the same doorway. $^{4-6}$ The experimental verifications of both the pump-dump (or pump-pump) $^{7-10}$ and coherent control $^{11-15}$ schemes have been carried out by several groups.

Rabitz and co-workers $^{16-18}$ have formulated a full version of active control by using the Schrödinger equation of motion as a dynamic constraint to the general optimal control theory (OCT). It is worth mentioning that most of the ingredients in the OCT has also developed independently but a little later by Kosloff et al. $^{19}$ in the context of an iterative procedure to optimize the control fields. Yan et al. $^{20}$ have rederived the OCT based on the variation principle in calculus and the Green function technique of density matrix dynamics in Liouville-space. Recently, Yan and co-workers $^{21-23}$ have further extended the general theory to the optimal pump-dump control via a pair of phase-unlocked fields. This work generalizes the original Tannor-Rice's pump-dump control scheme $^{1-3}$ to a simultaneous optimization of the pump and dump fields in both the weak and strong response regimes. In Tannor and Rice's original work, $^{1}$ the phase-unlocked pump-dump control was formulated in terms of the second-order perturbation of wave functions and the optimal dump field was obtained with respect to a given pump field.

In this article, we shall consider the general theory of nondegenerate excitation control of multisurface molecular systems. The nondegenerate excitation configuration is pretty common in experiment. Consider for example the resonant pump-pump control in a three-surface molecular system whose two optical resonant regions do neither overlap nor have a simple relation of harmonic generation. As the nondegenerate excitation implies the phase-unlocking condition, the present work could be considered as a natural extension of our previous phase-unlocked pump-dump control theory $^{21-23}$ to the case of controlling an $(N+1)$ -surface molecular system via N distinct fields. The remainder of this paper is organized as follows. In Sec. II, we develop the general theory of nondegenerate N-field excitation control of an $(N+1)$ -surface molecular system in terms of both the Liouville-space density matrix dynamics and the Hilbert-space wave function evolution. In Sec. III, we focus on the pump-pump control of a three surface molecular system in which the general Hilbert-space control formulation can be reduced into an eigenequation problem in the weak response regime. In this case, the optimal pairs of control fields are the eigenvectors and their corresponding control yields are the eigenvalues. The globally optimal pair of pump-pump fields can thus be identified unambiguously. In Sec. IV, we analyze the symmetry relation between the optimal pair of fields in the case of controlling a vibronic eigenlevel in the final target excited state. In Sec. V, we carry out the numerical implementation in a three-surface $I_{2}$ molecular system for controlling a localized outgoing Gaussian wave packet on the final excited surface. Finally, we summarize our result and conclude in Sec. VI.

## II. GENERAL THEORY OF NONDEGENERATE EXCITATION CONTROL

## A. Liouville-space formalism

Consider a nondegenerate excitation control scenario involving an $(N+1)$ -surface molecular system. The molecule system is initially stationary, such as at the thermal equilibrium or in a rovibronic level, in the ground electronic $|0\rangle$ state. The other N excited states are denoted as $|1\rangle$ , $\ldots$ , $|N\rangle$ , respectively. In the nondegenerate excitation scenario, we consider only the $\Delta n = \pm 1$ electronic transition between any pair of adjacent surfaces that are assumed to be optically coupled via a distinct external field $E_{n}$ . In this case, the total Hamiltonian for the coupled matter-field system in the rotating-wave-approximation (RWA) is given by:

$$
H (t) = \sum_ {n = 0} ^ {N} H _ {n} | n \rangle \langle n | - \sum_ {n = 1} ^ {N} \left[ D _ {n} ^ {+} E _ {n} (t) + D _ {n} ^ {-} E _ {n} ^ {*} (t) \right]. \tag {1}
$$

Here, $H_{n}; n=0, \ldots, N$ , denotes the molecular adiabatic Hamiltonian in the nth electronic surface. $D_{n}^{+}$ and $D_{n}^{-}$ are two conjugated electronic transition dipole operators defined as

$$
D _ {n} ^ {+} \equiv \mu_ {n} | n \rangle \langle n - 1 |, \tag {2a}
$$

$$
D _ {n} ^ {-} \equiv (D _ {n} ^ {+}) ^ {\dagger} = \mu_ {n} | n - 1 \rangle \langle n |. \tag {2b}
$$

In Eq. (2), $\mu_{n}$ is the transition dipole moment which in general depends on the nuclear degrees of freedom. As $D_{n}^{+}|n - 1\rangle = \mu_{n}|n\rangle$ and $D_{n}^{-}|n\rangle = \mu_{n}|n - 1\rangle$ , these two transition dipole operators can physically be viewed as the creation and annihilation operators of the $n$ th exciton. The optical reference frequency $\Omega_{n}$ of the $n$ th field, which is assumed to be substantially different from $\Omega_{n'}$ of any other field, is chosen to be the pure electronic transition frequency $\omega_{n,n-1}$ between the two adjacent electronic states. Thus, $E_{1}(t),\ldots,E_{N}(t)$ are the slowly varying envelopes that control the nuclear dynamics among surfaces.

The goal of control is to find an optimal set of fields, $\{E_{1},\ldots,E_{N}\}$ , that drive the $(N+1)$ -surface molecular system to a desired target $\hat{A}$ at a specified target time $t_{f}$ . Mathematically, it corresponds to the functional optimization of the target expectation value at the target time,

$$
A (t _ {f}) = \mathrm{Tr} [ \hat {A} \rho (t _ {f}) ], \tag {3}
$$

under certain constraints. We shall in this paper consider the simplest constraint that the incident intensity from each of the control fields must remain finite. We shall therefore introduce N independent Lagrangian multipliers to specify the finite intensity constraints on the N distinct fields. The final control functional is thus given as

$$
J (t _ {f}) = A (t _ {f}) - \sum_ {n = 1} ^ {N} \lambda_ {n} \int_ {t _ {0}} ^ {t _ {f}} d \tau | E _ {n} (\tau) | ^ {2}. \tag {4}
$$

To find the optimal fields $\{E_{1},\ldots,E_{N}\}$ , let us vary a representing one from $E_{n}(t)$ to $E_{n}(t)+\delta E_{n}(t)$ and its complex conjugate from $E_{n}^{*}(t)$ to $E_{n}^{*}(t)+\delta E_{n}(t)$ . The resulting variation in the control functional is then

$$
\delta J (t _ {f}) = \delta A (t _ {f}) - \lambda_ {n} \int_ {t _ {0}} ^ {t _ {f}} d \tau [ E _ {n} (\tau) \delta E _ {n} ^ {*} (\tau) + \text { c.c. } ]. \tag {5}
$$

By using the first order perturbation theory in the Liouville-space, we have

$$
\delta A (t _ {f}) = \int_ {t _ {0}} ^ {t _ {f}} d \tau [ K _ {n} (\tau ; t _ {f}) \delta E _ {n} ^ {*} (\tau) + \text { c.c. } ], \tag {6}
$$

with

$$
K _ {n} (\tau ; t _ {f}) \equiv (i / \hbar) \mathrm{Tr} [ \hat {A} (\tau ; t _ {f}) \mathcal {D} _ {n} ^ {-} \rho (\tau) ]. \tag {7}
$$

Here, $D_{n}^{-}$ is the commutator of $D_{n}^{-}$ . As shown in Eq. (6), $K_{n}$ can be considered as the control kernel responsible to the variation $\delta E_{n}^{*}$ . The time-dependent system density matrix and target in Eq. (7) can be expressed in terms of the Liouville-space propagator (or Green function) G as

$$
\rho (\tau) = \mathcal {G} (\tau , t _ {0}) \rho (t _ {0}), \tag {8a}
$$

$$
\hat {A} (\tau ; t _ {f}) = \hat {A} \mathcal {G} (t _ {f}, \tau). \tag {8b}
$$

The Liouville-space propagator $\mathcal{G}$ is governed by the total Hamiltonian $H(t)$ [Eq. (1)] in the presence of $N$ control fields. By expanding the commutator $\mathcal{D}_n^-$ in Eq. (7) explicitly and followed by using the properties of $D_n^- = (D_n^+)^\dagger$ and the trace cyclic invariance, we can recast the control kernel as

$$
K _ {n} (\tau ; t _ {f}) = \left[ K _ {n} ^ {+} (\tau ; t _ {f}) \right] ^ {*} + K _ {n} ^ {-} (\tau ; t _ {f}), \tag {9}
$$

with

$$
K _ {n} ^ {\pm} (\tau ; t _ {f}) = (i / \hbar) \mathrm{Tr} [ \hat {A} (\tau ; t _ {f}) D _ {n} ^ {\pm} \rho (\tau) ]. \tag {10}
$$

Substituting Eq. (6) into Eq. (5) followed by applying the variation principle $\delta J(t_{f})=0$ with respect to $\delta E_{n}^{*}(t)$ in each of the distinct fields, we obtain

$$
\left. K _ {n} ^ {+} \left(\tau ; t _ {f}\right) \right] ^ {*} + K _ {n} ^ {-} \left(\tau ; t _ {f}\right) = \lambda_ {n} E _ {n} (\tau); \quad n = 1, \dots , N. \tag {11}
$$

As mentioned in Eq. (8) that both the forward-propagated system density matrix $\rho(\tau)$ and backward-propagated target operator $\hat{A}(\tau;t_{f})$ are governed by the Hamiltonian $H(t)$ [Eq. (1)], the control kernel $K_{n}$ depends on all fields. Thus, Eq. (11) constitutes N coupled equations. These equations should be solved jointly and iteratively to obtain the optimal set of fields, $\{E_{1},\ldots,E_{n}\}$ , for the non-degenerate control of the $(N+1)$ -surface molecular system. In the N=1 case, Eq. (11) constitutes the well-established

Liouville-space formulation in the control of a two-surface molecular system via a single coherent field. $^{19-24}$

## B. Hilbert-space formalism

Let us now consider the case of pure state control in which both the initial system $\rho(t_{0})=\left|\psi(t_{0})\right\rangle\left\langle\psi(t_{0})\right|$ and the final target $\hat{A}=\left|\phi\right\rangle\left\langle\phi\right|$ are in pure states. We further assume that there is no dissipative force and thus the propagated density matrix and target will remain in pure states. We have

$$
\rho (\tau) = \big | \psi (\tau) \big \rangle \big \langle \psi (\tau) \big |, \tag {12a}
$$

$$
\hat {A} (\tau ; t _ {f}) = \left| \phi (\tau ; t _ {f}) \right\rangle \left\langle \phi (\tau ; t _ {f}) \right|. \tag {12b}
$$

Here, $\psi(\tau)$ and $\phi(\tau;t_{f})$ are the forward- and backward-propagated wave functions for the system and the target, respectively. They are formally given by

$$
\psi (\tau) \equiv G (\tau , t _ {0}) \psi (t _ {0}), \tag {13a}
$$

$$
\phi (\tau ; t _ {f}) \equiv \phi G (t _ {f}, \tau). \tag {13b}
$$

The Hilbert-space propagator $G(\tau, \tau')$ is governed by the total Hamiltonian $H(t)$ [Eq. (1)] in the presence of all fields.

As a result of pure state [Eq. (12)], the Liouville-space control kernel $K_{n}^{\pm}$ [Eq. (10)] can be factorized as $^{20-23}$

$$
K _ {n} ^ {\pm} (\tau ; t _ {f}) = c ^ {*} (t _ {f}) f _ {n} ^ {\pm} (\tau ; t _ {f}). \tag {14}
$$

Here, $c(t_{f})$ is the complex control amplitude defined by: [note $A(t_{f}) = |c(t_{f}|^{2}]$

$$
c (t _ {f}) = \big \langle \phi \big | \psi (t _ {f}) \big \rangle . \tag {15}
$$

In Eq. (14), $f_{n}^{+}$ and $f_{n}^{-}$ are the Hilbert-space pure-state control kernels, defined by [cf. Eq. (10)]

$$
f _ {n} ^ {\pm} (\tau ; t _ {f}) = (i / \hbar) \big \langle \phi (\tau ; t _ {f}) \big | D _ {n} ^ {\pm} \big | \psi (\tau) \big \rangle . \tag {16}
$$

The final $N$ coupled control equations for the nondegenerate excitation fields, $\{E_1, \ldots, E_N\}$ , are then obtained by substituting Eq. (11) with Eq. (10). We have

$$
c (t _ {f}) [ f _ {n} ^ {+} (\tau ; t _ {f}) ] ^ {*} + c ^ {*} (t _ {f}) f _ {n} ^ {-} (\tau ; t _ {f})
$$

$$
= \lambda_ {n} E _ {n} (\tau); \quad n = 1, \dots , N. \tag {17}
$$

Like its Liouville-space counterparts, Eq. (17) constitutes N nonlinear control equations which should be solved jointly and iteratively.

## III. TWO-PHOTON PURE-STATE CONTROL IN THE WEAK RESPONSE REGIME

In the last section, we derived the general formulas for the optimal control of an $(N+1)$ -surface molecular system in terms of both Liouville-space [cf. Eq. (11)] and Hilbert-space [cf. Eq. (17)] dynamics. The resulting equations are valid for the optimal control fields at arbitrary intensities. However, these equations must be solved iteratively. The final converged control fields are only locally optimal and depend in general on the initial guess of fields to start the iteration procedure. Moreover the locally optimal fields are often too complicated to be experimental realizable. To facilitate this problem, various linear versions of control equations have been developed. $^{20-30}$ It has been shown that in general the linear Liouville-space control formulation is only achievable in a one-photon process. $^{20,25}$ However, in the pure-state case the linearized control formalism is generally obtainable up to two-photon processes. $^{22,23,30}$

In this section, we shall present the linear equations for the two-photon pump-pump control of a molecular system involving three electronic states, the ground $|0\rangle$ , an excited intermediate $|1\rangle$ , and the final $|2\rangle$ . This is in parallel with the two-photon phase-unlocked pump-dump control $^{21-23}$ but the second field acts in this work as another pump field that couples $|2\rangle\leftarrow|1\rangle$ transition. The control target is a nuclear wave packet $\phi_{2}$ on the final $|2\rangle$ electronic surface. That is, $\hat{A}=|\phi\rangle\langle\phi|$ with

$$
\phi = \left[ \begin{array}{l} 0 \\ 0 \\ \phi_ {2} \end{array} \right]. \tag {18}
$$

The relevant quantities in the two-photon pure-state control are the first-order Hilbert-space control kernels and the second-order control amplitude. They are given by

$$
f _ {1} ^ {- (1)} (\tau ; t _ {f}) = f _ {2} ^ {- (1)} (\tau ; t _ {f}) = 0, \tag {19a}
$$

$$
f _ {1} ^ {+ (1)} (\tau , t _ {f}) = \int_ {\tau} ^ {t _ {f}} d \tau^ {\prime} B (\tau^ {\prime}, \tau) E _ {2} (\tau^ {\prime}), \tag {19b}
$$

$$
f _ {2} ^ {+ (1)} (\tau , t _ {f}) = \int_ {t _ {0}} ^ {\tau} d \tau^ {\prime} B (\tau , \tau^ {\prime}) E _ {1} (\tau^ {\prime}), \tag {19c}
$$

and

$$
c ^ {(2)} (t _ {f}) = \int_ {t _ {0}} ^ {t _ {f}} d \tau \int_ {t _ {0}} ^ {\tau} d \tau^ {\prime} E _ {2} (\tau) B (\tau , \tau^ {\prime}) E _ {1} (\tau^ {\prime}). \tag {20}
$$

In these equations, B is the two-photon pump-pump Hilbert-space response function, defined in $t \geqslant t'$ as

$$
B (t, t ^ {\prime}) \equiv \left\langle \phi_ {2} ^ {(0)} \left(t; t _ {f}\right) \mid \hat {T} \left(t - t ^ {\prime}\right) \mid \psi_ {0} ^ {(0)} \left(t ^ {\prime}\right) \right\rangle . \tag {21}
$$

Here,

$$
\hat {T} (t) \equiv (i / \hbar) ^ {2} \mu_ {2 1} e ^ {- i H _ {1} t / \hbar} \mu_ {1 0}, \tag {22}
$$

is the pump-pump $\hat{T}$ -operator, and

$$
\left| \psi_ {0} ^ {(0)} (t ^ {\prime}) \right\rangle \equiv e ^ {- i H _ {0} (t ^ {\prime} - t _ {0})} \big | \psi_ {0} (t _ {0}) \big \rangle , \tag {23a}
$$

$$
\left\langle \phi_ {2} ^ {(0)} (t; t _ {f}) \right| \equiv \left\langle \phi_ {2} \right| e ^ {- i H _ {2} (t _ {f} - t)}, \tag {23b}
$$

are the propagated wave functions for the system and the target in the absence of control fields. As $f_{n}^{-(1)} = 0$ [Eq. (19a)], the Hilbert-space control equation [Eq. (17)] can be simplified as $c^{(2)}(t_f)[f_n^{+(1)}(\tau; t_f)]^* \propto E_n(\tau)$ in the weak response regime. In this case, the phase of $c^{(2)}(t_f)$ becomes irrelevant to the control dynamics and can therefore be set to zero. By expressing $f_{n}^{+(1)}(\tau; t_f)$ explicitly, we obtain the following generalized eigenequations for the optimal pairs of pump-pump control fields $\{E_1, E_2\}$ :

$$
\int_ {\tau} ^ {t _ {f}} d \tau^ {\prime} B ^ {*} (\tau^ {\prime}, \tau) E _ {2} ^ {*} (\tau^ {\prime}) = \lambda_ {1} E _ {1} (\tau), \tag {24a}
$$

$$
\int_ {t _ {0}} ^ {\tau} d \tau^ {\prime} B (\tau , \tau^ {\prime}) E _ {1} (\tau^ {\prime}) = \lambda_ {2} E _ {2} ^ {*} (\tau). \tag {24b}
$$

Substituting the above equation into Eq. (20), we do obtain a real and positive control amplitude $c^{(2)}(t_{f})=|c^{(2)}(t_{f})|$ . This is consistent with that setting the phase of $c^{(2)}(t_{f})$ to zero in the derivation of above equations. We can further identify the physical meaning of the eigenvalues $\lambda_{n}(n=1,2)$ in Eq. (24) as $^{22,23}$

$$
\lambda_ {n} = \left| c ^ {(2)} (t _ {f}) \right| / I _ {n} \equiv \left| c ^ {(2)} (t _ {f}) \right| \Bigg / \int_ {t _ {0}} ^ {t _ {f}} d \tau \left| E _ {n} (\tau) \right| ^ {2}. \tag {25}
$$

Note that the Hilbert-space response function $B(t, t')$ [Eq. (21)] is only physically required for $t \geqslant t'$ . We shall however extend its definition to the region of $t < t'$ with $B(t, t') = 0$ . With this convention, we can recast Eq. (24) as

$$
\int_ {t _ {0}} ^ {t _ {f}} d \tau^ {\prime} [ B ^ {\dagger} B ] (\tau , \tau^ {\prime}) E _ {1} (\tau^ {\prime}) = \lambda_ {1 2} E _ {1} (\tau), \tag {26a}
$$

$$
\int_ {t _ {0}} ^ {t _ {f}} d \tau^ {\prime} [ B B ^ {\dagger} ] (\tau , \tau^ {\prime}) E _ {2} ^ {*} (\tau^ {\prime}) = \lambda_ {1 2} E _ {2} ^ {*} (\tau). \tag {26b}
$$

Here,

$$
[ B ^ {\dagger} B ] (\tau , \tau^ {\prime}) \equiv \int_ {t _ {0}} ^ {t _ {f}} d \tau^ {\prime \prime} B ^ {*} (\tau^ {\prime \prime}, \tau) B (\tau^ {\prime \prime}, \tau^ {\prime}), \tag {27}
$$

and $[BB^{\dagger}](\tau,\tau')$ is defined similarly. The eigenvalue $\lambda_{12}$ in Eq. (26) is the joint yield for pump-pump control. That is

$$
\lambda_ {1 2} = \lambda_ {1} \lambda_ {2} = \left| c ^ {(2)} (t _ {f}) \right| ^ {2} / (I _ {1} I _ {2}) = A ^ {(4)} (t _ {f}) / (I _ {1} I _ {2}). \tag {28}
$$

Therefore, the globally optimal pair of pump-pump fields are the eigenfunction $\{E_1,E_2\}$ that associate with the largest eigenvalue of $\lambda_{12}$ of Eq. (26).

It is interesting to have a formal comparison between Eq. (24) or (26) of this work for the optimal pair of pump-pump $\{E_{1}, E_{2}\}$ fields and Eq. (27) or (29) of Ref. 22 for the optimal pair of pump-dump $\{E_{p}, E_{d}\}$ fields in the weak response regime. Besides the different physical meanings in the Hilbert-space control response B functions, the equations in pump-pump and in pump-dump control schemes share the same mathematically structure under the mapping of $\{E_{1}, E_{2}\} \Leftrightarrow \{E_{p}, E_{d}^{*}\}$ . This feature is consistent with the physical pictures of pump-pump and pump-dump optical processes.

## IV. PUMP-PUMP EIGENSTATE CONTROL AND SYMMETRY RELATION

In this section, we consider a target in a vibronic eigenstate, $|\phi_{2}\rangle=|f\rangle$ , on the final electronic excited surface with $H_{2}|f\rangle=\varepsilon_{f}|f\rangle$ . The molecule assumes initially in a vibronic eigenstate, $|\psi_{0}(t_{0})\rangle=|i\rangle$ , on the ground surface with $H_{0}|i\rangle=\varepsilon_{i}|i\rangle$ . In this case, the two-photon pump-pump Hilbert-space control response function B [cf. Eq. (21)] assumes the form $(\tau\geqslant\tau')$ :

$$
B (\tau , \tau^ {\prime}) = e ^ {- i \varepsilon_ {f} (t _ {f} - \tau) / \hbar} T _ {f i} (\tau - \tau^ {\prime}) e ^ {- i \varepsilon_ {i} (\tau^ {\prime} - t _ {0}) / \hbar}. \tag {29}
$$

Here, $T_{fi}(t)=\langle f|\hat{T}(t)|i\rangle$ is the T-matrix [Eq. (22)] element for the two-photon $f\leftarrow i$ absorption processes.

Along the same procedure in Sec. IV of Ref. 22 for the (pump-dump) Raman pumping control, we obtain the following symmetry relation in the pair of optimal pump-pump $\{E_{1}, E_{2}\}$ fields [cf. Eq. (33) of Ref. 22]:

$$
e ^ {- i \varepsilon_ {i} (t _ {0} + t) / \hbar} E _ {1} (t _ {0} + t) = e ^ {i \varepsilon_ {f} (t _ {f} - t) / \hbar} E _ {2} (t _ {f} - t), \tag {30}
$$

or in the frequency domain [cf. Eq. (34) of Ref. 22]

$$
\hat {E} _ {1} (\omega) = e ^ {i \omega (t _ {0} + t _ {f})} \hat {E} _ {2} (\omega_ {f i} - \omega). \tag {31}
$$

Here, $\omega_{fi} \equiv (\varepsilon_f - \varepsilon_i) / \hbar$ , and $\hat{E}_n(\omega)$ is the Fourier transform of $E_n(t)$ :

$$
\hat {E} _ {n} (\omega) = \int_ {- \infty} ^ {\infty} d t e ^ {i \omega t} E _ {n} (t) \equiv | \hat {E} _ {n} (\omega) | e ^ {i \theta_ {n} (\omega)}. \tag {32}
$$

Note the jth order frequency chirp of $E_{n}$ is

$$
\varphi_ {n} ^ {(j)} = \frac {d ^ {j + 1} \theta_ {n} (\omega)}{d \omega^ {j + 1}} \Bigg | _ {\omega = \bar {\omega} _ {n}}, \tag {33}
$$

with $\overline{\omega}_n$ being the central frequency of the field.

An alternative way to visualize the time-frequency coherence in $E_{n}$ is its Wigner intensity:

$$
F _ {n} (\omega , t) = 2 \operatorname{Re} \int_ {0} ^ {\infty} d \tau e ^ {- i \omega \tau} E _ {n} ^ {*} \left(t + \frac {\tau}{2}\right) E _ {n} \left(t - \frac {\tau}{2}\right). \tag {34}
$$

The intensity profile of $|E_{n}(t)|^{2}$ or $|\hat{E}_{n}(\omega)|^{2}$ can be obtained by integrating $F_{n}(\omega,t)$ over the frequency or time region, respectively. The symmetry relations in Eqs. (30) and (31) can now be combined in the Wigner intensity as

$$
F _ {1} (\omega , t _ {0} + t) = F _ {2} (\omega_ {f i} - \omega , t _ {f} - t). \tag {35}
$$

Equations (30) and (31) [or Eq. (35)] lead to the following conclusions for the optimal pair of pump-pump fields, $\{E_{1}, E_{2}\}$ : (i) their temporal spectra, which satisfy the relation $|E_{1}(t_{c}+t)|^{2}=|E_{2}(t_{c}-t)|^{2}$ , are symmetric about the center, $t_{c}=(t_{0}+t_{f})/2$ , of the interaction time region $[t_{0}, t_{f}]$ with the $E_{1}$ field occurring earlier; (ii) their power spectra, which satisfy $|\hat{E}_{1}(\omega_{c}+\omega)|^{2}=|\hat{E}_{2}(\omega_{c}-\omega)|^{2}$ , are symmetric about $\omega_{c}=\omega_{fi}/2\equiv(\varepsilon_{f}-\varepsilon_{i})/(2\hbar)$ . Physically, for each chosen frequency $\omega_{1}$ -component in the $E_{1}$ field there is a corresponding frequency $\omega_{2}$ -component in the $E_{2}$ field such that the two-photon resonant excitation condition $\omega_{1}+\omega_{2}=\omega_{fi}$ holds; (iii) their frequency chirps are the same $\varphi_{1}^{(2k-1)}=\varphi_{2}^{(2k-1)}$ at an odd order, but opposite $\varphi_{1}^{(2k)}=-\varphi_{2}^{(2k)}$ at an even order. The above three properties of optimal pair of pump-pump fields hold for the control of the eigenstate in the absence of dephasing and relaxation processes.

## V. NUMERICAL RESULTS AND DISCUSSIONS

## A. An outgoing wave packet focusing control in $I_{2}$

As the numerical example, we consider an iodine molecular system involving the ground X, the excited B and the final E surfaces. The parameters for these three potential surfaces ( $V_{X}=V_{0}$ , $V_{B}=V_{1}$ and $V_{E}=V_{2}$ ) are listed in Table I. In the following calculation, we neglect the contribution of rotation. We further assume that the two electronic transition dipoles are independent of the nuclear coordinate and are set to be $\mu_{1}=\mu_{2}=1$ Debye for simplicity. Note the pure electronic transition frequencies for $X\leftrightarrow B$ and $B\leftrightarrow E$ are 15769 and 25642 cm $^{-1}$ , respectively. It is expected that the non-degenerated excitation condition considered in this work is satisfied. The $I_{2}$ molecule is initially at the $\nu=0$ vibronic level in the ground X electronic state. The target in the final E (i.e., $|2\rangle$ ) state is chosen to be a minimum uncertainty Gaussian wave packet:

TABLE I. Parameters for the ${\mathrm{I}}_{2}$ Morse potential surfaces.

<table><tr><td>I-I</td><td> $T_e$  (cm $^{-1}$ )</td><td> $D_e$  (cm $^{-1}$ )</td><td> $\beta$  (Å $^{-1}$ )</td><td> $R_e$  (Å)</td></tr><tr><td> $V_0$  (X)</td><td>0</td><td>12,550</td><td>1.871</td><td>2.666</td></tr><tr><td> $V_1$  (B)</td><td>15,769</td><td>4,381</td><td>1.876</td><td>3.016</td></tr><tr><td> $V_2$  (E)</td><td>41,411</td><td>12,536</td><td>0.8783</td><td>3.647</td></tr></table>

$$
\phi_ {2} (R) \propto \exp \left[ - \frac {(R - \bar {r}) ^ {2}}{4 \Delta_ {r} ^ {2}} - \frac {i \bar {p}}{\hbar} (R - \bar {r}) \right]. \tag {36}
$$

The target is centered at $\bar{r}=4.0\ \AA$ , with a width of $\Delta_{r}=0.03\ \AA$ and an outgoing momentum that corresponds to $\bar{p}^{2}/(2\mu)=0.05\ \text{eV}$ . This target is in the bound state region with the mean vibronic energy of $1360\ cm^{-1}$ . We may term this outgoing wave packet in the bound region as a “molecular paddleball.” Figure 1 shows schematically the pump-pump control of this three-surface molecular system. The target time is chosen to be $t_{f}=300\ fs$ . In the following calculations, the split-operator method $^{31}$ is employed for wave function propagations in both the weak and strong response regimes.

## B. The weak control response regime

We first calculate the optimal pairs of pump-pump fields in the weak response regime by using Eq. (26). The Hilbert-space pump-pump response function $B(t,t')$ [Eq. (21) for $t \geqslant t'$ and $B(t,t') = 0$ for $t < t'$ ] is discretized and evaluated in a time-grid as the matrix B. The eigenvector and eigenvalue of $B^{\dagger}B$ [cf. Eq. (26a)] are then the optimal $E_{1}$ field and its associating control yield, respectively. The optimal counterpart $E_{2}$ field can either be obtained from Eq. (26b) as the eigenvector of $BB^{\dagger}$ followed by taking the complex conjugate or from Eq. (24b) as the matrix product $E_{2}^{*}\propto BE_{1}$ . Presented in the following are both the globally optimal pump-dump field pair (i.e., the eigenvectors of Eq. (26) associating with the largest eigenvalue) and the second best pair (i.e., the eigenvectors associating with the second largest eigenvalue).

![](images/cd71da8f6b7daf490fd9ffe382b861b32b9c4c6630a8af02ba0f177e047a72a3.jpg)

<details>
<summary>line chart</summary>

| R (Å) | V(R) (10⁴ cm⁻¹) for X | V(R) (10⁴ cm⁻¹) for B | V(R) (10⁴ cm⁻¹) for E |
|-------|------------------------|------------------------|------------------------|
| 2.0   | ~0.0                   | ~0.0                   | ~8.0                   |
| 2.5   | ~0.0                   | ~2.0                   | ~4.0                   |
| 3.0   | ~0.0                   | ~2.0                   | ~4.0                   |
| 3.5   | ~0.5                   | ~2.0                   | ~4.0                   |
| 4.0   | ~1.0                   | ~2.0                   | ~4.0                   |
| 5.0   | ~1.5                   | ~2.0                   | ~4.5                   |
| 6.0   | ~2.0                   | ~2.0                   | ~5.0                   |
</details>

FIG. 1. Schematic diagram of pump-pump control scheme in a three-surface $I_{2}$ molecular system. The initial system lies on the ground X surface. The target on the final E surface can be achieved through a two-photon process via the intermediate B state.

![](images/f75fb5db7bf1c544a91debf8b96328b66ea2b8dadf80837c6712223ab3baa04d.jpg)

![](images/f21a290a79c6a8334f7028db4e5273fd92fa8d5515bc87bc135fa5a9d2f33dba.jpg)  
FIG. 2. The profiles of the globally optimal pump-pump field pair in the time (upper panel) and frequency (lower panel) domains. The target is an outgoing minimum-uncertainty Gaussian wave packet with the mean position of 4.0 Å with a width of 0.03 Å. The mean momentum $\bar{p}>0$ corresponds to $\bar{p}^{2}/(2\mu)=0.05\;\mathrm{eV}$ . The target time is 300 fs.

Figure 2 depicts the globally optimal pair of pump-pump $\{E_1,E_2\}$ fields in the weak response regime in terms of their temporal (upper panel) and spectral (lower panel) profiles. It can be seen that the globally optimal $E_{1}$ field consists of a simple-shaped pulse of about 40 fs in its temporal FWHM. Its peak frequency is around $19~100~\mathrm{cm}^{-1}$ , close to the peak of iodine $B\gets X$ absorption. About 80 fs after the peak of $E_{1}$ field, the globally optimal $E_{2}$ field starts to be switched on. The switching time lasts for about 30 fs and then the $E_{2}$ field stays. As shown in the lower panel of Fig. 2, the $E_{2}$ field carries primarily a center frequency of about $23~300~\mathrm{cm}^{-1}$ . The sum of the center frequencies in $E_{1}$ and $E_{2}$ fields amounts to about $42~400~\mathrm{cm}^{-1}$ which is closed to the mean energy difference between the target and the initial state. This is consistent with the two-photon resonant excitation picture and is essential for a high control efficiency.

In order to visualize the time-frequency coherence in each of the globally $E_{1}$ and $E_{2}$ fields, we present their Wigner intensities [Eq. (34)] in Fig. 3. In making the plots, we include a window function $W(\tau)=\exp(-\tau/t_{W})$ with $t_{W}=50$ fs in the integrand of Eq. (34) to remove the intrinsic self-interference in the Wigner field transformation. The globally optimal $E_{1}$ field contains also a positive linear chirp [cf. the upper panel of Fig. 3]. Note the target in consideration is an outgoing minimum uncertainty Gaussian wave packet (or a “molecular paddleball”) on the final surface. As we demonstrated previously, $^{24,25}$ the positively chirped $E_{1}$ field is favored for the prefocusing of an outgoing wave packet on the intermediate B surface. $^{21}$ The globally optimal

![](images/830b764698a5c08efe2b63817d52faca41531ec3e9ee8b7f6b216e1528237334.jpg)

<details>
<summary>contour plot</summary>

| t (fs) | ω (10³ cm⁻¹) |
| ------ | ------------ |
| 90     | 19           |
| 110    | 20           |
| 130    | 19           |
| 150    | 20           |
| 170    | 19           |
</details>

![](images/a7eb94a8cc7d1aa79a1a030d6976c217e8e55fb2ec5b1d6a8420bc8c080f2392.jpg)

<details>
<summary>contour plot</summary>

| t (fs) | ω (10³ cm⁻¹) |
| ------ | ------------ |
| 200    | 21           |
| 220    | 23           |
| 240    | 24           |
| 260    | 23           |
| 280    | 22           |
| 300    | 21           |
</details>

FIG. 3. Wigner representation of the $E_{1}$ (for $B \leftarrow X$ ) and the $E_{2}$ (for $E \leftarrow B$ ) fields as in Fig. 2.

$E_{2}$ field that is responsible to the $E\leftarrow B$ transition exhibits a visuable quadratic chirp. The center frequency first decreases and then increases as time evolves. This particular chirping style may relate to the relative shapes of B and E surfaces [cf. Fig. 1]. Consider the classical transition picture in which the center frequency of $E_{2}(t)$ field at time t amounts to $\langle\psi_{B}(R,t)|U_{EB}(R)|\psi_{B}(R,t)\rangle$ . Here, $U_{EB}(R)=V_{E}(R)-V_{B}(R)$ is the difference between two surfaces that are optically coupled via the $E_{2}$ pump field. As can be seen from Fig. 1, $U_{EB}(R)$ exhibits a minimum (23 186 cm $^{-1}$ ) at the internuclear distance about $R_{min}=3.82\mathring{A}$ . As $E_{2}$ field pumps the outgoing wave packet $\psi_{B}(R,t)$ on the B excited surface, it acquires a negative chirp when $\psi_{B}(R,t)$ moves towards the minimum of $U_{EB}(R)$ and a positive chirp as $\psi_{B}(R,t)$ moves outward further.

Figure 4 shows the evolution of iodine molecular wave packets on X, B and E surfaces, controlled by the globally optimal pair of pump-pump $\{E_{1}, E_{2}\}$ fields (Fig. 3) in the weak response regime. The ground state wave packet is depicted in terms of the “hole” $|\psi_{X}(0)|^{2}-|\psi_{X}(t)|^{2}$ evolution as shown in the bottom panel of this figure. This “hole” is created as the result of $E_{1}$ excitation. It remains roughly about the same shape as the initial wave function of $\nu=0$ on the ground X surface. At the same time, the $E_{1}$ pump field creates also $\psi_{B}(t)$ (the middle panel of Fig. 4) on the intermediate excited surface. It is clear that the wave packet $\psi_{B}(t)$ on the B surface is prefocused and further pumped by the second control field $E_{2}$ to form the wave packet $\psi_{E}(t)$ (the upper panel of Fig. 4) on the final E surface. In this sense, we may view the optimal pump-pump control as a combination of two one-photon processes. However, the prefocused “target” on the intermediate surface is optimally defined by the control equation, Eq. (26). Included in the upper panel of Fig. 4 is also the target (dotted line). It shows clearly that the final wave function overlaps very well with the target on the final E surface at the target time $t_{f}=300$ fs.

![](images/86a4c46de10dd2d4979b002f83493c8ce5deb848299186363d8bd59e91ff4122.jpg)

<details>
<summary>line chart</summary>

| 5.5 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 6.0 |  |  |  |  |  |
| 2.5 |  |  |  |  |  |
| 3.0 |  |  |  |  |  |
| 3.5 |  |  |  |  |  |
| 4.0 |  |  |  |  |  |
| 4.5 |  |  |  |  |  |
| 5.0 |  |  |  |  |  |
| 5.5 |  |  |  |  |  |
| 6.0 |  |  |  |  |  |
| 2.5 |  |  |  |  |  |
| 3.0 |  |  |  |  |  |
| 3.5 |  |  |  |  |  |
| 4.0 |  |  |  |  |  |
| 4.5 |  |  |  |  |  |
</details>

FIG. 4. Wave packet evolution on the three involving surfaces. The control fields are the globally optimal pair as in Fig. 3. Shown in the bottom panel is the evolution of the hole (wave packet difference) in the ground X state. The target is also depicted in the top panel to demonstrate the control quality.

We now turn to the second best pair of $\{E_1, E_2\}$ fields, the eigenvectors of Eq. (26) with the second largest eigenvalue. As the control yield at the target time relates to the eigenvalue [cf. Eq. (28)], we conclude that the second best pair achieve $\lambda_{12}'' / \lambda_{12}' = 0.47$ of the globally optimal yield in the weak response regime. Here $\lambda_{12}'$ and $\lambda_{12}''$ are the largest and the second largest eigenvalues in Eq. (26). Figure 5 shows the temporal (upper panel) and spectral profiles (lower panel) of the second best $\{E_{1}, E_{2}\}$ pair. Obviously, each of the fields in the second best pair has two coherent components, rather than a single component as in the globally optimal counterpart. The second best $E_{2}$ field also almost vanishes at the target time (cf. the upper panel of Fig. 5), which is in contrast with the globally optimal one (cf. the upper panel of Fig. 2). Despite of various differences, the second best pair fields share some similarities with the globally optimal pair. The sum-frequency from the $\{E_{1}, E_{2}\}$ in both optimal pairs are about the same to match with the mean energy difference between the target and the initial state. The relative delay time of $E_{2}$ with respect to $E_{1}$ in the second best pair is also about the same as that in the globally optimal pair.

![](images/94484a97a3ece14fb6392db9cb6577b7eb935451f2f25a720fd35527c90c40d6.jpg)

![](images/e463ffa7be84135399762fb7e66b5e86550b9db7567626f2f39a789bf1a9845a.jpg)  
FIG. 5. The profiles of the second best pump-pump field pair in time (upper panel) and frequency (lower panel) domains.

![](images/717ade6cc392b7c85a295d127ec97c4986a3b31f30a7f5bba4313b0422be23ab.jpg)

<details>
<summary>line chart</summary>

| Time (fs) | Achievement α(t) |
| --------- | ---------------- |
| 0         | 0.0              |
| 50        | 0.0              |
| 100       | 0.0              |
| 150       | 0.0              |
| 200       | 0.0              |
| 250       | 0.0              |
| 275       | 0.2              |
| 300       | 1.0              |
</details>

FIG. 6. The achievement $\alpha(t)$ [Eq. (37)] vs time for the globally optimal (solid) and the second best (dotted) pump-pump field pairs in the weak response regime.

In order to examine the control quality, we adopt the so-called achievement function $\alpha(t)$ , defined by $^{20}$

$$
\alpha^ {2} (t) = \frac {\left| \right.\left\langle \right. \phi_ {2} \left. \right| \psi_ {2} (t) \left. \right\rangle\left. \right| ^ {2}}{\left\langle \right. \phi_ {2} \left. \right| \phi_ {2} \rangle \left\langle \right. \psi_ {2} (t _ {f}) \left. \right| \psi_ {2} (t _ {f}) \rangle}. \tag {37}
$$

Obviously, $0 \leqslant \alpha(t) \leqslant 1$ . We shall refer the perfect control as $\alpha(t_f) = 1$ at the target time. Figure 6 shows the achievement $\alpha(t)$ for both the globally optimal (solid line) and the second best (dash line) pairs of $\{E_1, E_2\}$ fields. In each case, $\alpha(t)$ increases rapidly as the $E_2$ field is switched on and reaches its maximum at the target time $t_f = 300$ fs. The achievement at the target time $\alpha(t_f)$ is 0.96 for the globally optimal pair and 0.95 for the second best pair. In other words, these two fields pairs are about the same in terms of the quality of control. Note that the control yield from the second best field pair is only $\lambda_{12}'' / \lambda_{12}' = 0.47$ of that from the globally optimal pair.

To conclude this subsection, we shall point out that the globally optimal fields in Fig. 2 may be fitted in the following experimentally convenient forms:

$$
E _ {1} ^ {\text { fit }} (t) = \sqrt {A _ {1}} e ^ {- (t - \bar {t}) ^ {2} / (2 \Gamma_ {1} ^ {2})} e ^ {- i \varphi_ {1} (t - \bar {t} _ {1})}, \tag {38a}
$$

$$
E _ {2} ^ {\text {fit}} (t) = \sqrt {\frac {A _ {2}}{1 + e ^ {- 2 (t - t _ {c}) / \Gamma_ {2}}}} e ^ {- i \varphi_ {2} (t - \bar {t} _ {2})}, \tag {38b}
$$

with

$$
\varphi_ {n} (t) = \overline {{{{\omega}}}} _ {n} t + \frac {1}{2} c _ {n} ^ {\prime} t ^ {2} + \frac {1}{6} c _ {n} ^ {\prime \prime} t ^ {3}. \tag {39}
$$

TABLE II. Best-fit parameters for the $B \leftrightarrow X$ field $E_{1}$ and the $E \leftrightarrow B$ field $E_{2}$ in the weak response regime. $A_{2} / A_{1} = 0.53$ .

<table><tr><td></td><td> $\overline{t}$ (fs)</td><td> $\Gamma$ (fs)</td><td> $\overline{\omega }$ (cm $^{-1}$ )</td><td> $c'$ (cm $^{-1}$ /fs)</td><td> $c''$ (cm $^{-1}$ /fs $^2$ )</td><td> $t_c$ (fs)</td></tr><tr><td> $E_1^{\text{fit}}$ </td><td>124.2</td><td>20.8</td><td>19176</td><td>15.3</td><td>0.536</td><td>na</td></tr><tr><td> $E_2^{\text{fit}}$ </td><td>260.4</td><td>9.4</td><td>23245</td><td>-4.3</td><td>0.448</td><td>230</td></tr></table>

Here, the $E_{1}$ field that is responsible for the $B\leftrightarrow X$ transition is fitted by a Gaussian pulse and the $E_{2}$ for $E\leftrightarrow B$ by a simple switch-on field. Each parameterized field $E_{n}^{\mathrm{fit}}(t)$ is characterized by its peak power $A_{n}$ , carrier frequency $\overline{\omega}_{n}$ , linear chirp $c_{n}^{\prime}$ , quadratic chirp $c_{n}^{\prime\prime}$ and (effective) temporal center $\overline{t}_{n}$ . The parameter $\Gamma_{n}$ in $E_{1}$ represents the temporal width of the Gaussian pulse, while in $E_{2}$ is the duration for the field to be switched on. $t_{c}$ in $E_{2}$ [Eq. (38b)] is the time at which the switch-on field reaches 1/2 of its steady-state power intensity; that is $|E_{2}^{\mathrm{fit}}(t_{c})|^{2}=A_{2}/2$ . A nonlinear least-square fit is performed for finding the parameters in each field in the globally optimal pair in the weak response regime and the results are listed in Table II. The Wigner profiles of the best-fit fields, presented in Fig. 7, are almost identical to that of the globally optimal fields in Fig. 3.

## C. The strong response regime

The optimal fields pair beyond the weak response regime should be obtained by an iterative solution of Eq. (17). In this work, we adopt the following simple line-search approach: $^{19,32}$

$$
E _ {n} ^ {(i + 1)} (t) = (1 - a) E _ {n} ^ {(i)} (t) + a \xi_ {n} ^ {(i)} (t), \tag {40}
$$

to the iterative evaluation of optimal field pair at each of intensities in calculation. In Eq. (40), 0 < a < 1 is an adjustable parameter, and $\xi_{n}^{(i)}(t) = K_{n}(t)/\lambda_{n}$ with the control kernel $K_{n}(t)$ [Eqs. (10) and (14)] governed by $\{E_1^{(i)}, E_2^{(i)}\}$ . Other more elaborated methods such as conjugated gradient $^{17,19}$ and Krotov methods $^{33,34}$ can also be used. However, we found that the simple line-search approach is adequate at least up to $I_{1} = I_{2} = 5.24 \, \mathrm{mJ/cm^{2}}$ studied in this work in which the initial input fields for the iteration can be properly chosen. This is done by using the globally optimal fields as the initial guess at a low intensity. The converged optimal fields are then scaled up to a slightly higher intensity to initiate another loop of iteration for the optimal field pair at that higher intensity. Figures 8 and 9 summarize the achievement $\alpha(t_{f})$ and the populations $\{P_{B}(t_{f}), P_{E}(t_{f})\}$ on the $B$ and $E$ surfaces at the target time vs the control field intensity. Note $P_{X}(t_{f}) = 1 - P_{B}(t_{f}) - P_{E}(t_{f})$ . Compared in each of these two figures are the results from the iteratively improved optimal field pair (solid line), the parameterized fields $\{E_1^{\mathrm{fit}}, E_2^{\mathrm{fit}}\}$ [Eq. (38)] that best fit to the iteratively improved optimal pair (dotted line), and the amplitude-scaled globally optimal pair in the weak response regime (dashed line).

![](images/36729341e9be39b5be44473752a34f1711cd7c670b2dd5a8ebdd502efc02c5b3.jpg)

<details>
<summary>contour plot</summary>

| t (fs) | ω (10³ cm⁻¹) |
| ------ | ------------ |
| 110    | 19           |
| 130    | 20           |
</details>

![](images/1f051886477aa6eb33e0750e73d26483df47fefda65a57e832954a2cfff1dc05.jpg)

<details>
<summary>contour plot</summary>

| t (fs) | ω (10³ cm⁻¹) |
| ------ | ------------ |
| 200    | 21           |
| 220    | 23           |
| 240    | 24           |
| 260    | 23           |
| 280    | 22           |
| 300    | 21           |
</details>

FIG. 7. The Wigner intensity profiles of the best-fit fields for the globally optimal pair in the weak response regime (cf. Fig. 3). The fitted-parameters are listed in Table II.

![](images/4525f723cf4cf6a8fdf0a3611d999b564cae471e3e3676280df7db78685e8650.jpg)

<details>
<summary>line chart</summary>

| I (mJ/cm²) | iterative | fitted | scaled |
| ---------- | --------- | ------ | ------ |
| 1          | 0.955     | 0.952  | 0.953  |
| 2          | 0.956     | 0.953  | 0.951  |
| 3          | 0.957     | 0.954  | 0.948  |
| 4          | 0.958     | 0.955  | 0.945  |
| 5          | 0.965     | 0.960  | 0.940  |
</details>

FIG. 8. The achievement at the target time as a function of field intensity for the iteratively improved field pair (solid), the best-fit parameterized field pair (dotted), and the amplitude-scaled globally optimal pair in the weak response regime (dashed).

As an example of the strong response regime, we consider in detail the iteratively improved optimal field pair with $I_{1}=I_{2}=4.83\ mJ/cm^{2}$ . At this intensity, the achievement at the target time is $\alpha(t_{f})=0.96$ (cf. Fig. 8), with the final populations on X, B and E surfaces being about 0.6, 0.0 and 0.4, respectively (cf. Fig. 9). The population in the B state is almost completely suppressed, resulting in an effective 100% population inversion between the B and E surfaces. Note the Rabi flopping angle in this case is about $0.57\pi$ for the $B\leftrightarrow X$ field and $0.54\pi$ for the $E\leftrightarrow B$ field. The Wigner profiles of the iteratively improved optimal pair of $\{E_{1},E_{2}\}$ fields at this intensity show no significant difference compared with those in the weak response regime. Table III lists the best-fit parameters (cf. Eq. (38)) for the iteratively improved optimal fields pair. Figure 10 shows the wave packet evolutions controlled by the iteratively improved optimal fields at the intensity of $I_{1}=I_{2}=4.83~mJ/cm^{2}$ . The almost perfect control at the target time is evident. Figure 11 summarizes the controlled population changes on surfaces. Obviously, the second pump having the Rabi flopping angle of $0.54\pi$ is capable of a nearly complete inversion of the nonstationary wave packet on the intermediate B surface into the target on the final E surface.

![](images/e68114e56e18818006d04cb4b1f62eb579a3ef6f90764f955515a4af0b7d267c.jpg)

<details>
<summary>line chart</summary>

| I (mJ/cm²) | iterative | fitting | scaled |
| ---------- | --------- | ------- | ------ |
| 0          | 0.0       | 0.0     | 0.0    |
| 1          | 0.05      | 0.05    | 0.05   |
| 2          | 0.15      | 0.15    | 0.15   |
| 3          | 0.25      | 0.25    | 0.25   |
| 4          | 0.35      | 0.35    | 0.35   |
| 5          | 0.4       | 0.4     | 0.4    |
</details>

FIG. 9. The population at the target time on both E and B surfaces as a function of field intensity for the iteratively improved field pair (solid), the best-fit parameterized field pair (dotted), and the amplitude-scaled globally optimal pair in the weak response regime (dashed).

TABLE III. Best-fit parameters for the $B \leftrightarrow X$ field $E_{1}$ and the $E \leftrightarrow B$ field $E_{2}$ at $I_{1} = I_{2} = 4.83 \mathrm{~mJ/cm^{2}}$ , i.e., $A_{1} = 1.3 \times 10^{11} \mathrm{~W/cm^{2}}$ , $A_{2} = 8.2 \times 10^{10} \mathrm{~W/cm^{2}}$ .

<table><tr><td></td><td> $\overline{t}$ (fs)</td><td> $\Gamma$ (fs)</td><td> $\overline{\omega }$ (cm $^{-1}$ )</td><td> $c'$ (cm $^{-1}$ /fs)</td><td> $c''$ (cm $^{-1}$ /fs $^2$ )</td><td> $t_c$ (fs)</td></tr><tr><td> $E_1^{\text{fit}}$ </td><td>126.0</td><td>21.5</td><td>19235</td><td>15.6</td><td>0.488</td><td>na</td></tr><tr><td> $E_2^{\text{fit}}$ </td><td>262.0</td><td>9.6</td><td>23237</td><td>-3.6</td><td>0.412</td><td>240</td></tr></table>

## VI. SUMMARY

In this paper, we established a theoretical framework to study the optimal control of an $(N+1)$ -surface molecular system via N distinct or nondegenerate light fields. The final control equations in the strong response regime were ex-

![](images/9814371f48a1673d33fe9eb25d8190732d0d91c634abde18a160ce6633389e3a.jpg)  
FIG. 10. Wave packet evolution controlled by the optimal fields with the Rabi flopping angle of $0.57\pi$ in $E_{1}$ ( $B\leftrightarrow X$ ) and $0.54\pi$ in $E_{2}$ ( $E\leftrightarrow B$ ) field.

![](images/1edf91642758d5d77ae3388997c457b83814c11e651608b4ca6eddde0bc56ef7.jpg)

<details>
<summary>line chart</summary>

| Time (fs) | P_x  | P_B  | P_E  |
| --------- | ---- | ---- | ---- |
| 0         | 1.0  | 0.0  | 0.0  |
| 50        | 1.0  | 0.0  | 0.0  |
| 100       | 1.0  | 0.0  | 0.0  |
| 150       | 0.6  | 0.4  | 0.0  |
| 200       | 0.6  | 0.4  | 0.0  |
| 250       | 0.6  | 0.4  | 0.2  |
| 300       | 0.6  | 0.4  | 0.4  |
</details>

FIG. 11. Evolution of the population on the $X$ (dashed), $B$ (dotted) and $E$ (solid) surfaces, controlled by the same iteratively improved optimal field pair as those in Fig. 10.

pressed in terms of both Liouville-space density matrix dynamics [Eq. (11)] and Hilbert-space wave function evolution [Eq. (17)]. As a special case of N=1, the present control theory recovers the well-established formulations in the control of a two-surface molecular system via a single coherent field. $^{19-24}$ We further presented the linear theory [Eq. (26)] of optimal pump-pump control of three-surface molecular systems and identified the globally optimal solution [cf. Eqs. (25) and (26)] in the weak response regime. For the eigenstate control, we obtained a symmetry relation [Eq. (30), (31) or (35)] between two excitation fields in the optimal pair. As a preliminary implementation, we numerically investigated the focusing control of an outgoing wave packet in a model three-surface $I_{2}$ molecular system. We calculated both the globally optimal and the second best pump-pump fields pairs in the weak response regime by solving the control eigenequations [Eq. (26)]. The globally optimal fields are quite robust against the field intensity. Starting with the globally optimal solution in the weak response regime, we also searched for the iteratively improved optimal control field pairs [Eq. (17)] as the intensity increases adiabatically. Comparison of the resulting optimal fields with the best-fit parameterized fields and with the intensity scaled globally optimal weak-response fields were made to elucidate the control dynamics in the strong response regimes. Within the intensity range of study, the optimal fields are relatively simple and can be fitted very well with experimentally achievable pulse shapes [Eq. (38) and cf. Figs. 8 and 9]. Another interesting result from the calculation is that the optimal fields $\{E_{1}, E_{2}\}$ with the Rabi flopping angle about $\pi/2$ in each are able to completely invert the population on the middle surface to the final excited state (cf. Fig. 10). In summary, this paper to gether with our previous formulation of pump-dump control $^{21-23}$ constitute an integrated theory of optimal control via a pair of distinct fields.

## ACKNOWLEDGMENT

The support of the Research Grants Council of Hong Kong Government is gratefully acknowledged.

$^{1}$ D. J. Tannor and S. A. Rice, J. Chem. Phys. 83, 5013 (1985).  
$^{2}$ D. J. Tannor, R. Kosloff, and S. A. Rice, J. Chem. Phys. 85, 5805 (1986).  
$^{3}$ D. J. Tannor and S. A. Rice, Adv. Chem. Phys. 70, 441 (1988).  
$^{4}$ P. Brumer and M. Shapiro, Faraday Discuss. Chem. Soc. 82, 177 (1986).  
$^{5}$ M. Shapiro and P. Brumer, J. Chem. Phys. 84, 4103 (1986).  
$^{6}$ M. Shapiro and P. Brumer, Int. Rev. Phys. Chem. 13, 187 (1994).  
$^{7}$ T. Baumert, B. Buhler, M. Grosser, R. Thalweiser, V. Weiss, E. Wiedenmann, and G. Gerber, J. Phys. Chem. 95, 8103 (1991).  
$^{8}$ T. Baumert, V. Engel, C. Röttgermann, W. T. Strunz, and G. Gerber, Chem. Phys. Lett. 191, 639 (1992).  
$^{9}$ G. G. T. Baumert, Isr. J. Chem. 34, 103 (1994).  
$^{10}$ E. D. Potter, J. L. Herek, S. Pedersen, Q. Liu, and A. H. Zewail, Nature (London) 355, 66 (1992).  
$^{11}$ C. Chen, Y. Y. Yin, and D. S. Elliott, Phys. Rev. Lett. 64, 507 (1990).  
$^{12}$ C. Chen and D. S. Elliott, Phys. Rev. Lett. 65, 1737 (1990).  
$^{13}$ S. M. Park, S. P. Lu, and R. J. Gordon, J. Chem. Phys. 94, 8622 (1991).  
$^{14}$ L. C. Zhu, V. Kleiman, X. N. Li, S. P. Lu, K. Trentelman, and R. J. Gordon, Science 270, 77 (1995).  
$^{15}$ A. Shnitman, I. Sofer, I. Golub, A. Yogev, M. Shapiro, Z. Chen, and P. Brumer, Phys. Rev. Lett. 76, 2886 (1996).  
$^{16}$ A. P. Peirce, M. A. Dahleh, and H. Rabitz, Phys. Rev. A 37, 4950 (1988).  
$^{17}$ S. Shi, A. Woody, and H. Rabitz, J. Chem. Phys. 88, 6870 (1988).  
$^{18}$ H. Rabitz and S. Shi, Adv. Mol. Vibr. Collision Dyn. 1A, 187 (1991).  
$^{19}$ R. Kosloff, S. A. Rice, P. Gaspard, S. Tersigni, and D. J. Tannor, Chem. Phys. 139, 201 (1989).  
$^{20}$ Y. J. Yan, R. E. Gillilan, R. M. Whitenell, K. R. Wilson, and S. Mukamel, J. Phys. Chem. 97, 2320 (1993).  
21 Y. J. Yan, J. Che, and J. L. Krause, Chem. Phys. 217, 297 (1997).  
22 Y. J. Yan, J. S. Cao, and Z. W. Shen, J. Chem. Phys. 107, 3471 (1997).  
$^{23}$ Y. J. Yan, Z. W. Shen, and Y. Zhao, Chem. Phys. (in press).  
$^{24}$ J. L. Krause, R. M. Whitnell, K. R. Wilson, Y. J. Yan, and S. Mukamel, J. Chem. Phys. 99, 6562 (1993).  
$^{25}$ J. L. Krause, R. M. Whitnell, K. R. Wilson, and Y. J. Yan, in $Femtosecond\ Chemistry$ , edited by J. Manz and L. Wöste (VCH, Weinheim, 1995), p. 743.  
$^{26}$ Y. J. Yan, J. Chem. Phys. 100, 1094 (1994).  
27 I. Averbukh and M. Shapiro, Phys. Rev. A 47, 5086 (1993).  
$^{28}$ L. Y. Shen, S. H. Shi, and H. Rabitz, J. Phys. Chem. 97, 12114 (1993).  
$^{29}$ V. Dubov and H. Rabitz, J. Chem. Phys. 103, 8412 (1995).  
$^{30}$ V. Dubov and H. Rabitz, Phys. Rev. A 54, 710 (1996).  
$^{31}$ C. Leforestier, R. H. Bisseling, C. Cerjan, M. D. Feit, R. A. Friesner, A. Guldberg, A. Hammerich, G. Jolicard, W. Karrlein, H. Meyer, N. Lipkin, O. Roncero, and R. Kosloff, J. Comput. Phys. 94, 59 (1991).  
$^{32}$ J. L. Krause, M. Messina, K. R. Wilson, and Y. J. Yan, J. Phys. Chem. 99, 13736 (1995).  
33 J. Somlói, V. A. Kazakov, and D. J. Tannor, Chem. Phys. 172, 85 (1993).  
$^{34}$ D. J. Tannor, V. Kazakov, and V. Orlov, in Time Dependent Quantum Molecular Dynamics, NATO ASI Series, edited by J. Broeckhove and L. Lathouwers (Plenum, New York, 1992).