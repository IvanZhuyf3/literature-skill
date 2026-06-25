RESEARCH ARTICLE | AUGUST 08 2000

# Unified approach to the Bloch–Redfield theory and quantum Fokker–Planck equations √

YiJing Yan; Feng Shuang; Ruixue Xu; Jixin Cheng; Xin-Qi Li; Chen Yang; Houyu Zhang

![](images/3642b1b2f4c8ad5e0d9a5a717062afe2fe240a0d3418b048134d80891377eb17.jpg)

Check for updates

J. Chem. Phys. 113, 2068–2078 (2000)

https://doi.org/10.1063/1.482018

![](images/23eb7c841ebe49a07b6019ab97905e9835700bd1c50c4eff49200f369c189668.jpg)  
View Online

![](images/eefc1c8f69cdc5effaadfa453940a36d472160db6a35ed249cc851eaeed89256.jpg)  
Export Citation

## Articles You May Be Interested In

Surface hopping outperforms secular Redfield theory when reorganization energies range from small to moderate (and nuclei are classical)

J. Chem. Phys. (March 2015)

Calculation of coherences in Förster and modified Redfield theories of excitation energy transfer

J. Chem. Phys. (August 2019)

Bloch-Redfield equations for modeling light-harvesting complexes

J. Chem. Phys. (February 2015)

![](images/01974e6be449448bd13731118123e0da5409c4655e5bc44caad9b95127adea43.jpg)

<details>
<summary>natural_image</summary>

Abstract digital artwork with flowing light streaks against a dark background, no text or symbols present.
</details>

## AIP Advances

Why Publish With Us?

![](images/cdd78d3608ace25f3fd01811f1245685e020b91b00e1960529ec4a7fda83b3c1.jpg)  
21 DAYS
average time
to 1st decision

![](images/44b4f47d8c9f66a915d3ae4cb4fddc283d5a1eea2808b989a8742373f168604a.jpg)  
OVER 4 MILLION
views in the last year

![](images/429fe24f2da9174cebae8d9bfa84caf8114493185c895731e7f59b3fc8ddd5cb.jpg)  
INCLUSIVE
scope

Learn More

![](images/b6cc22bb27941575ff364c983da44dd77f73f2f11b1abe0a517daa358b832694.jpg)  
AIP Publishing

# Unified approach to the Bloch–Redfield theory and quantum Fokker–Planck equations

YiJing Yan, $^{a)}$ Feng Shuang, and Ruixue Xu

Department of Chemistry, Hong Kong University of Science and Technology, Kowloon, Hong Kong, and Open Laboratory of Bond-Selective Chemistry, University of Science and Technology of China, Hefei, China

Jixin Cheng, Xin-Qi Li, Chen Yang, and Houyu Zhang

Department of Chemistry, Hong Kong University of Science and Technology, Kowloon, Hong Kong

(Received 10 March 2000; accepted 9 May 2000)

By using a rather simple algebraic approach, we revisit and further bridge between two most commonly used quantum dissipation theories, the Bloch–Redfield theory and a class of Fokker–Planck equations. The nature of the common approximation scheme involving in these two theories is analyzed in detail. While the Bloch–Redfield theory satisfies the detailed-balance relation, we also construct a class of Fokker–Planck equations that satisfy the detailed-balance relation up to the second moments in phase-space. Developed is also a generalized Fokker–Planck equation that preserves the general positivity of the reduced density operator. Both $T_{1}$ -relaxation and pure- $T_{2}$ dephasing are considered, and their temperature dependence is shown to be very different. Provided is also an analogy between the quantum pure- $T_{2}$ dephasing and the classical heat transport.

© 2000 American Institute of Physics. [S0021-9606(00)50430-9]

## I. INTRODUCTION

Quantum dissipation plays crucial roles in many fields of science, such as nuclear magnetic resonance (NMR), $^{1-4}$ quantum optics, $^{5-8}$ mathematical physics, $^{9-12}$ and molecular dynamics in condensed phases. $^{13-23}$ The key theoretical quantity of interest is the reduced density operator whose dynamics is governed by the Liouville–von Neumann equation,

$$
\dot {\rho} = - \frac {i}{\hbar} [ H, \rho ] - \mathcal {R} \rho . \tag {1}
$$

Exact expressions for the dissipation term $R\rho$ can be constructed formally via Zwanzig–Mori's projection operator technique. $^{24,25}$ However, dissipations in almost all practical cases have to be treated with models and/or approximations. As a result, there are a variety of nonequivalent forms of $R\rho$ , such as those in the Bloch–Redfield theory $^{2-4}$ and the Fokker–Planck equations. $^{16-19}$ The commonly used approximation in various forms of quantum dissipation theory (QDT) is the weak system–bath interaction in which the second-order perturbation is justifiable. Various forms of QDT differ at the approximating schemes that partially incorporate the contributions of second- or higher-order system–bath interaction. There are also a variety of ways in approximating the quantum fluctuation-dissipation (or the detailed-balance) relation, especially in Fokker–Planck theories. $^{16-19}$

Despite certain unavoidable approximations involved, one would still like to arrive at a fully satisfactory QDT. It refers to a QDT that preserves the following five physical properties of a density operator—Hermitianity, trace invariance, detailed-balance, translational invariance, and positivity. A density operator $\rho(t)$ should be Hermitian. The trace invariance means that $\operatorname{Tr}\dot{\rho}=0$ , or the QDT satisfies the law of total population conservation. The detailed-balance assures the canonical ensemble distribution, $\rho_{eq}=e^{-\beta H}/\operatorname{Tr}e^{-\beta H}$ , be an asymptotic and stationary solution to the QDT. Note that here H is not the Hamiltonian for the bare (gas phase) system, but the renormalized one to the reduced system. The translational invariance arises from the physical requirement that an arbitrary observable described by the QDT, or more precisely $\operatorname{Tr}[\hat{A}\dot{\rho}(t)]=d\bar{A}(t)/dt$ , should not depend on the choice of coordinate origin $x_{0}$ . The positivity requirement relates to the probability interpretation of the density operator whose eigenvalues should be nonnegative. The positivity of QDT preserves this property of $\rho(t)$ for all times. We shall see that the aforementioned first two properties, i.e., being of Hermitian and traceless, can be easily incorporated. On the other hand, Lindblad has proved that in the Markovian regime the remaining three properties, the detailed-balance, the translational invariance, and the general positivity, are mutually exclusive. $^{10}$ In order to compensate this incompatibility, we shall in this work adopt an internal coordinate convention (cf. Sec. III C) to assure that for any physical observable, $\mathrm{Tr}[\hat{A}\dot{\rho}(t)]=d\overline{A}(t)/dt$ be described properly and unambiguously. Thus, a fully satisfactory QDT refers explicitly in the following only to its being simultaneously of detailed-balance and positivity.

In this work, we shall revisit two most used classes of QDT, i.e., the Bloch–Redfield theory (BRT) and the Fokker–Planck equation (FPE). We shall demonstrate that these two types of QDT cover actually almost all existing Markovian theories of quantum dissipation. The relations among six of such theories were analyzed recently by Kohen, Marson, and Tannor in a harmonic oscillator system. $^{26}$ This paper is going to answer the following two questions. (i) Is there a compact operator equivalent formulation to BRT or/and FPE, such that it constitutes formally a full satisfactory QDT, and meanwhile is numerically implementable in various representations? (ii) Is there a convenient and systematic way to bridge between these two seemingly different types of QDT? While elucidating these two questions, we shall also pay a special attention to classifying $T_{1}$ -energy relaxation and pure- $T_{2}$ dephasing processes in the resulting QDT. The temperature dependence of either the $T_{1}$ -or pure- $T_{2}$ dissipation process will be established via the spectral density formulation for the system–bath coupling.

The remainder of this paper is organized as follows: In Sec. II, a rather simple algebraic approach is used to reconstruct the formal Bloch–Redfield theory (BRT). The key step in formulating is the identification of dissipative modes and their spectrum conjugations that will be defined in due course. Despite its being equivalent to the conventional Redfield–tensor prescription (cf. Appendix A), the algebraic form of the BRT constructed in Sec. II offers an alternative (and more straight) way to analyze and simulate the dissipation dynamics as it describes. Moreover, it constitutes a convenient starting point to establish the relations among the BRT and a class of Fokker–Planck equations (FPE) that will be developed later in this paper. In Sec. III, we critically analyze the Redfield approximation and the resulting compact form of BRT. Included there are also the proof of its detailed-balance relation and the comments on its translational variance and its compatibility with the Lindblad's form of positivity. $^{9}$ Section III is concluded with a general description of pure-dephasing and how its rate depends on temperature. In Sec. IV, the BRT developed in Sec. II is used to construct a broad class of FPE, including that for a Brownian oscillator $^{14-17}$ and that commonly used in the laser physics community. $^{5-8}$ The most important result is a generalized FPE to be developed in Sec. IV E. The resulting generalized FPE is applicable to arbitrary systems in the presence of the $T_{1}$ -energy relaxation and/or the pure- $T_{2}$ dephasing. Presented there is also a case of almost fully satisfactory FPE formulation, in which the positivity is exact, while the detailed-balance is satisfied up to the second moments in phase-space and thus becomes exact in the harmonic limit. The Ehrenfest equations of motion associating with the generalized FPE in harmonic systems are presented in Appendix B. In Sec. V we demonstrate further by using the harmonic model the analogy between the quantum pure-dephasing and the classical heat transport in a ring defined by the phase-space angle. Finally, we conclude and summarize this paper in Sec. VI.

## II. BLOCH-REDFIELD THEORY

In this section, we shall revisit the Bloch–Redfield theory (BRT) via a rather simple algebraic approach. The final compact formulation of the BRT, together with the spectral density description of bath interaction, will be summarized in Sec. II C. The advantages of the present BRT over the conventional formulation in the eigenstate representation $^{2-4,27}$ will be elucidated throughout this paper.

## A. Background formulation

Let us start with a generalized Langevin description in which the total Hamiltonian, $H_{T}=H+H'(t)$ , consists of a deterministic part H for the coherent dynamics and a stochastic part $H'(t)$ for the system–bath coupling. We shall adopt the decomposition form of $H'(t)$ in terms of the generalized system coordinates and their associating Langevin forces,

$$
H ^ {\prime} (t) = - \hbar \sum_ {\alpha} Q _ {\alpha} F _ {\alpha} (t). \tag {2}
$$

The above decomposition form of $H'(t)$ was also adopted by Friesner and co-workers in their development of the Redfield theory that reduced the dissipation tensor algebra to the ordinary matrix multiplication. $^{27}$

In Eq. (2), $Q_{\alpha}$ is a Hermitian operator or a dynamic variable in the reduced system space. We shall hereafter call it as a dissipative mode. $F_{\alpha}(t)$ is a Hermitian operator in the stochastic bath space with $\langle F_{\alpha}(t)\rangle=0$ . Here, $\langle\cdots\rangle$ denotes the average over the stationary bath ensembles. For simplicity, we shall further assume that the generalized Langevin forces $F_{\alpha}$ acting on different dissipative modes $Q_{\alpha}$ are statistically independent. That is,

$$
\left\langle F _ {\alpha} (t) F _ {\alpha^ {\prime}} (\tau) \right\rangle = \delta_ {\alpha \alpha^ {\prime}} \widetilde {C} _ {\alpha} (t - \tau). \tag {3}
$$

In the standard second-order cumulant expansion formalism, the dissipation term in the Liouville–von Neumann equation, Eq. (1), takes the following form: $^{19}$

$$
\mathcal {R} (t) \rho (t) = \frac {1}{2} \sum_ {\alpha} \left\{\left[ Q _ {\alpha}, \tilde {Q} _ {\alpha} (t) \rho (t) \right] + \mathrm{H.c.} \right\}, \tag {4a}
$$

$$
\tilde {Q} _ {\alpha} (t) = 2 \int_ {t _ {0}} ^ {t} d \tau \tilde {C} _ {\alpha} (t - \tau) G (t, \tau) Q _ {\alpha} G ^ {\dagger} (t, \tau). \tag {4b}
$$

Here, $G(t,\tau)$ is the Hilbert-space propagator governed by the reduced system Hamiltonian. In the absence of the time-dependent field, $G(t,\tau)=\exp[-iH(t-\tau)/\hbar]$ .

Besides the approximation via the second-order system-bath interaction, Eq. (4) adopts also the initial factorization ansatz,

$$
\rho_ {T} (t _ {0}) = \rho (t _ {0}) \rho_ {B} (t _ {0}) \equiv \rho (t _ {0}) \rho_ {B} ^ {\mathrm{eq}}. \tag {5}
$$

Here, $\rho_{B}^{eq}$ is the bath canonical ensemble density operator. The above ansatz is physically self-consistent if the final formulation of QDT in the absence of external time-dependent field satisfies

$$
\mathcal {R} \rho_ {\mathrm{eq}} = 0. \tag {6}
$$

It is the detailed-balance relation, which should be checked for in the following derived QDT for the consistency of the initial factorization approximation. We shall return to the point in Sec. III.

## B. Redfield approximation

The Bloch–Redfield theory $^{2-4}$ (BRT) constitutes the most widely used formulation in the study of quantum dissipation processes involving some energy eigenstates. As its dissipative superoperator R does not depend on time, BRT is usually considered as of Markovian in nature. Before we present the final algebraic formulation of BRT, we shall provide in the following an alternative point of view on its approximation scheme.

Note that Eq. (4a) is a time-local prescription of quantum dissipation and equivalent to the memory kernel prescription up to the second-order system–bath interaction. $^{19,24,25}$ Consider a time-resolved experiment on molecular dynamics in a dissipative medium. The molecular system is initially $(t_{0}\rightarrow-\infty)$ at the thermal equilibrium. A time-dependent external field such as pulsed laser light should be employed to create a nonstationary density wave packet for the dynamics experiment. The time-dependent system–field coupling shall be included in the deterministic Hamiltonian H that governs both the first term of Eq. (1) and the Hilbert-space propagator $G(t,\tau)$ in the dissipation term as described by Eq. (4). The interplay between time-dependent coherent driving and dissipation may introduce a dramatic cooperative effect. It has been demonstrated in the case of quantum stochastic resonance at which the weak field response theory breaks down no matter how weak the periodic driving force is. $^{28-31}$

We shall be interested in the cases where either the external excitation fields are fast compared with the dissipation dynamics, or weak and operated away from the cooperative driving-dissipation regime. In this case, we may neglect time-dependent driving on the dissipation superoperator or $\widetilde{Q}_{\alpha}(t)$ of Eq. (4b). In other words, the Hilbert-space propagator in Eq. (4b) assumes the field-free form,

$$
G (t, \tau) = e ^ {- i H (t - \tau) / \hbar}. \tag {7}
$$

However, the initial time in Eq. (4b) should still remain as $t_{0} \rightarrow -\infty$ , instead of a peculiar value such as $t_{0}=0$ . As a result, we may recast Eq. (4b) as

$$
\widetilde {Q} _ {\alpha} = 2 \int_ {0} ^ {\infty} d \tau \widetilde {C} _ {\alpha} (\tau) e ^ {- i \mathcal {L} \tau} Q _ {\alpha}. \tag {8}
$$

Here, L is the reduced system Liouvillian, defined by its action on an arbitrary operator $\hat{O}$ as

$$
\mathcal {L} \hat {O} \equiv \hbar^ {- 1} [ H, \hat {O} ], \tag {9a}
$$

$$
e ^ {- i \mathcal {L} t} \hat {O} = e ^ {- i H t / \hbar} \hat {O} e ^ {i H t / \hbar}. \tag {9b}
$$

In Eq. (8), $\widetilde{Q}_{\alpha}$ does not depend on time. The above analysis concludes that the local-time dependence in $\widetilde{Q}_{\alpha}(t)$ [Eq. (4b)], or equivalently in the dissipation superoperator $\mathcal{R}(t)$ , is rather from the time-dependence in the Hamiltonian of the reduced system than the non-Markovian bath. More discussions on the correlated time-dependent driving and dissipation that lead to time-dependence in $\widetilde{Q}_{\alpha}(t)$ will be presented in Sec. VI.

In the regime of weak driving-dissipation correlation and weak system–bath interaction, the only approximation in the soon to-be-presented BRT is that [cf. Eq. (8)]

$$
\widetilde {Q} _ {\alpha} \approx \int_ {- \infty} ^ {\infty} d \tau \widetilde {C} _ {\alpha} (\tau) e ^ {- i \mathcal {L} \tau} Q _ {\alpha}. \tag {10}
$$

Equation (10) can be called the Redfield approximation. Its physical implication, together with that of the initial factorization ansatz [Eq. (5)], will be discussed in Sec. III A.

## C. Redfield theory in algebraic form

The final form of the BRT is summarized as follows [cf. Eqs. (1), (4a), (10), and (12)]:

$$
\dot {\rho} = - \frac {i}{\hbar} [ H, \rho ] - \frac {1}{2} \sum_ {\alpha} \left[ Q _ {\alpha}, \tilde {Q} _ {\alpha} \rho - \rho \tilde {Q} _ {\alpha} ^ {\dagger} \right], \tag {11a}
$$

$$
\tilde {Q} _ {\alpha} \equiv C _ {\alpha} (- \mathcal {L}) Q _ {\alpha}. \tag {11b}
$$

In Eq. (11b), $C_{\alpha}(-\mathcal{L})$ is a function of reduced system Liouvillian operator, defined by the bath interaction spectrum, or the Fourier transform of the random force-force correlation function as follows:

$$
C _ {\alpha} (\omega) \equiv \int_ {- \infty} ^ {\infty} d \tau e ^ {i \omega \tau} \widetilde {C} _ {\alpha} (\tau) \equiv e ^ {\beta \omega / 2} S _ {\alpha} (\omega). \tag {12}
$$

Obviously, Eq. (11b) is equivalent to Eq. (10). The detailed-balance relation, $C_{\alpha}(-\omega)=e^{-\beta\omega}C_{\alpha}(\omega)$ , with $\beta\equiv k_{B}T/\hbar$ , is equivalent to that $S_{\alpha}(\omega)$ defined in the last identity Eq. (12) is a symmetric function. We shall hereafter call $\widetilde{Q}_{\alpha}$ [Eq. (11b)] the spectrum conjugation to the dissipative mode $Q_{\alpha}$ .

In the commonly used system–bath coupling model, the bath consists of a collection of independent harmonic oscillators and the bath interaction force on the dissipative mode $Q_{\alpha}$ of the reduced system is given by $^{13,14,17}$

$$
F _ {\alpha} = \sum_ {j} c _ {\alpha j} x _ {j}. \tag {13}
$$

Here, $x_{j}$ is the dimensionless coordinate of the jth bath mode of frequency $\omega_{j}$ , and $c_{\alpha j}$ is its coupling strength to the system dissipative mode $Q_{\alpha}$ . The spectral density of this bath interaction is defined as $^{13,14,17}$

$$
J _ {\alpha} (\omega) \equiv \frac {\pi}{2} \sum_ {j} | c _ {\alpha j} | ^ {2} \delta (\omega - \omega_ {j}). \tag {14}
$$

Physically, the spectral density is only defined in the region of $\omega\geqslant0$ , with $J(0)=0$ . We should however extend its mathematical definition to the negative frequency domain via $J(-\omega)=-J(\omega)$ . By doing this, the detailed-balance symmetrized bath spectrum can be expressed in term of spectral density as

$$
S _ {\alpha} (\omega) \equiv S _ {\alpha} (- \omega) = J _ {\alpha} (\omega) / \sinh (\beta \omega / 2). \tag {15}
$$

Note that the unit of $J_{\alpha}(\omega)$ depends on the choice of its associating dissipative mode $Q_{\alpha}$ . In this paper, we shall choose the unit of $Q_{\alpha}$ to be dimensionless. In this case, $J_{\alpha}(\omega)$ is of the unit of frequency, and can be used directly to specify the dissipation rate [cf. Eq. (25) or (30a)].

Equation (11) that casts the BRT in a compact algebraic form constitutes one of the main results of this paper. Another is the generalized Fokker–Planck equation [cf. Eq. (48)] and will be developed in Sec. IV. Mathematically, Eq. (11) is equivalent to the conventional BRT represented in the eigenenergy representation (cf. Appendix A). However, Eq. (11) has some advantages due to its algebraic nature, leading to the clarity in discussing its physical properties, the implication of approximations involved, and its relation to other quantum dissipation theories such as Fokker–Planck equations. These advantages will be illustrated in the following sections.

## III. PROPERTIES OF THE BLOCH-REDFIELD THEORY AND COMMENTS

In this section, we shall first analyze the nature of the so-called Redfield approximation scheme that involves both the approximant, Eq. (10), and the initial factorization ansatz, Eq. (5). We then discuss the resulting BRT [Eq. (11)] about whether it satisfies the detailed-balance, translational invariance, and positivity. Obviously, Eq. (11a) is Hermitian and traceless, i.e., $Tr\dot{\rho}=0$ . This section will be concluded with a formal description of pure- $T_{2}$ dephasing dynamics, a special and important type of dissipation that involves no energy loss.

## A. Implication of the Redfield approximation

Traditionally, the BRT has been considered as a Markovian and second-order theory. $^{2-4}$ However, as the analysis presented in Sec. II B, the so-called Markovian nature of the BRT would rather refer to the neglect of cooperativity between the time-dependent driving and dissipation than to the nature of bath. The approximations Eqs. (5) and (10) suggest further that the BRT [Eq. (11)] be neither a complete second-order theory.

Let us start with the initial factorization ansatz [Eq. (5)]. In this approximation, the effect of the initial system–bath coupling is completely neglected. The second-order correction to the initial reduced density operator will result in an effective Hamiltonian that depends on bath temperature.

We now turn to the Redfield approximation, Eq. (10). Without this approximation, the resulting QDT formulation would be the same as Eq. (11) but with $C_{\alpha}(\omega)$ [Eq. (12)] being replaced by the complex spectrum,

$$
C _ {\alpha} (\omega) + i C _ {\alpha} ^ {\prime} (\omega) \equiv 2 \int_ {0} ^ {\infty} d \tau e ^ {i \omega \tau} \widetilde {C} _ {\alpha} (\tau). \tag {16}
$$

Thus, the Redfield approximation, Eq. (10), amounts actually to the neglect of the bath dispersion $C_{\alpha}^{\prime}(\omega)$ of Eq. (16). The bath dispersion affects not only on the dissipative dynamics but also on the asymptotic reduced density operator.

Both approximations described above make the BRT [Eq. (11)] incomplete in the second order system–bath interaction. However, both approximations lead to the asymptotic reduced density operator to be the zero-order canonical distribution,

$$
\rho_ {\mathrm{eq}} = e ^ {- \beta H} / \operatorname{Tr} e ^ {- \beta H}. \tag {17}
$$

In this sense, the BRT [Eq. (11)] is self-consistent, with its detailed-balance is defined by the zero-order canonical reduced density operator of Eq. (17).

## B. Detailed-balance relation

To prove that $\rho_{eq}$ [Eq. (17)] is a stationary solution to Eq. (11), and thus also the self-consistency in the BRT, we shall show that

$$
\tilde {Q} _ {\alpha} \rho_ {\mathrm{eq}} = \rho_ {\mathrm{eq}} \tilde {Q} _ {\alpha} ^ {\dagger}. \tag {18}
$$

To do that, let us re-examine the spectrum conjugation $\tilde{Q}_{\alpha}$ [Eq. (11b)]. By using Eqs. (12), we can recast Eq. (11b) as

$$
\tilde {Q} _ {\alpha} = e ^ {- \beta \mathcal {L} / 2} [ S _ {\alpha} (- \mathcal {L}) Q _ {\alpha} ] \equiv e ^ {- \beta H / 2} \tilde {Q} _ {\alpha} ^ {h} e ^ {\beta H / 2}. \tag {19}
$$

Here, $\widetilde{Q}_{\alpha}^{h}\equiv S_{\alpha}(-\mathcal{L})Q_{\alpha}$ is Hermitian since $S_{\alpha}(-\omega)$ $= S_{\alpha}(\omega)$ is a symmetric function. However, $\widetilde{Q}_{\alpha}$ is non-Hermitian. It satisfies

$$
\tilde {Q} _ {\alpha} e ^ {- \beta H} = e ^ {- \beta H} \tilde {Q} _ {\alpha} ^ {\dagger}. \tag {20}
$$

This is equivalent to Eq. (18). We have thus also proved the detailed-balance relation in the BRT [Eq. (11)] without invoking any specific representation.

## C. Translational invariance vs the internal-coordinate convention

Let us first point out that Eq. (11) is of the dissipative-mode invariance in the following sense. In Eq. (11), two dissipative modes $Q_{\alpha}$ and $Q_{\alpha'} = Q_{\alpha} + r$ that differ only by a real c-number describe the same dissipation dynamics, i.e., $R_{\alpha} = R_{\alpha'}$ . This property of BRT [Eq. (11)] can be easily proved by noticing that $\widetilde{r}_{\alpha} \equiv C_{\alpha}(-\mathcal{L})r = C_{\alpha}(0)r = \widetilde{r}_{\alpha}^{*}$ remains as a real c-number. As a result, we have $R_{\alpha'} - R_{\alpha} = [Q_{\alpha}, \widetilde{r}_{\alpha}\rho - \rho \widetilde{r}_{\alpha}^{*}] = 0$ . Obviously, the dissipative-mode invariance reduces to the translational invariance if the dissipative mode $Q_{\alpha}$ is a linear function of the Cartesian coordinate, while to the zero-energy point invariance $Q_{\alpha}$ depends linearly on the Hamiltonian of the reduced system.

However, the dissipative-mode invariance in general is not equivalent to the translational invariance. Unless in the case of the single dissipative mode that is proportional to the coordinate q, the BRT [Eq. (11)] in general, violates the translational invariance.

In order to cure this defect, we shall use an internal coordinate-system to represent the reduced Hamiltonian and the dissipative mode, e.g.,

$$
H = H (\mathbf {p}, \mathbf {q} - \overline {{{\mathbf {q}}}} _ {\mathrm{eq}}), \tag {21a}
$$

$$
Q _ {\alpha} = Q _ {\alpha} (\mathbf {p}, \mathbf {q} - \overline {{\mathbf {q}}} _ {\mathrm{eq}}), \tag {21b}
$$

with $\overline{q}_{eq} \equiv Tr[q\rho_{eq}]$ . We shall hereafter adopt the convention of Eq. (21) to define the BRT [Eq. (11)] unambiguously.

## D. Compatibility to positivity

For the BRT to constitute a fully satisfactory QDT, it requires that Eq. (11) be also of the positivity. Lindblad showed that a Markovian-type QDT satisfying the general positivity should be of the following form: $^{9}$

$$
\dot {\rho} = - \frac {i}{\hbar} [ H, \rho ] - \frac {1}{2} \sum_ {\alpha} \{[ W _ {\alpha} ^ {\dagger}, W _ {\alpha} \rho ] + \mathrm{H.c.} \}. \tag {22}
$$

In general, Eq. (11) cannot be transformed into the Lindblad's form to assure the general positivity be preserved for arbitrary initial conditions. However, we shall present in Sec. IV D a special case of Eq. (11) that does have the Lindblad's form [cf. Eq. (38)]. This special case of Eq. (11), which relates closely to the conventional optical QDT, $^{5-8}$ satisfies simultaneously the detailed-balance and positively, and thus constitutes a fully satisfactory QDT.

## E. Description of pure-dephasing and its temperature-dependent rate

There are two types of dissipation. One is the $T_{1}$ -type involving energy relaxation, and another is the $T_{2}$ -type relating to dephasing. The concept of two types of dissipation was traditionally introduced via a specific level representation of the reduced density operator $\rho$ . The diagonal element $\rho_{aa}$ describes the level population, while the off-diagonal element $\rho_{ab}$ describes the coherence between two levels. In this case, the $T_{1}$ - and $T_{2}$ -processes may refer to the relaxation of levels $\{\rho_{aa}\}$ and coherences $\{\rho_{ab};a\neq b\}$ , respectively. $^{1-4}$ As $\rho$ is positive definite and satisfies the Schwartz inequality, $|\rho_{ab}|^{2}\leqslant\rho_{aa}\rho_{bb}$ , a population relaxation induces also the destruction of coherence. $^{32}$ On the other hand, one can have a pure- $T_{2}$ dephasing that involves only the destruction of coherence $\rho_{ab}$ but have no effect on the populations $\rho_{aa}$ and $\rho_{bb}$ . Note the above concept of two types of dissipation was introduced through a specific representation. In order to relate to whether the energy is dissipated or not, one should use the energy eigenstate representation. The rates of $T_{1}$ -relaxation and the $T_{2}$ -dephasing in the energy eigenstate representation are described in Appendix A in terms of Redfield dissipation tensor elements.

In this work, we shall adopt the dissipative mode description to classify the nature of dissipation processes without invoking any representation scheme. $^{33}$ We shall refer a pure- $T_{2}$ dephasing as a dissipation process that involves no energy loss. In other words, Eq. (11) should satisfy the property of $\operatorname{Tr}\{H\dot{\rho}\}=0$ , if all the involving dissipative modes are of pure-dephasing in nature. Let us denote $Q_{2}$ as a pure- $T_{2}$ dephasing mode. The necessary and sufficient condition for a pure-dephasing mode $Q_{2}$ can thus be described as $^{33}$

$$
[ H, Q _ {2} ] = 0. \tag {23}
$$

Obviously, a pure-dephasing mode $Q_{2}$ is diagonal in the eigenenergy representation. A general dissipative mode Q has both the diagonal and off-diagonal elements. They are responsible for the pure- $T_{2}$ dephasing and the $T_{1}$ -energy relaxation, respectively (cf. Appendix A).

In the following, we shall further use the spectral density formulation in Sec. II C to establish the temperature dependence on the pure-dephasing rate $\gamma_{2}$ . For a pure-dephasing mode $Q_{2}$ [Eq. (23)], its spectrum conjugation [Eq. (11b)] is given by

$$
\tilde {Q} _ {2} = C _ {2} (0) Q _ {2} \equiv 2 \gamma_ {2} Q _ {2}. \tag {24}
$$

Therefore, besides the positive constant, a pure-dephasing mode is self-spectrum-conjugated. As it was mentioned after Eq. (15), if $Q_{2}$ is chosen to be dimensionless, the spectral density $J_{2}(\omega)$ and $C_{2}(0)$ as well will be of the same dimension of the pure-dephasing rate. We may therefore obtain the pure-dephasing rate parameter in Eq. (24) as

$$
\gamma_ {2} \equiv C _ {2} (0) / 2 = (k _ {B} T / \hbar) \lim _ {\omega \to 0} [ J _ {2} (\omega) / \omega ]. \tag {25}
$$

The second identity was obtained by using Eqs. (12) and (15). Note that the pure-dephasing rate defined above is proportional to the temperature. By using Eq. (24) for the second term of Eq. (11a), we obtain that

$$
\mathcal {R} _ {2} \rho = \gamma_ {2} [ Q _ {2}, [ Q _ {2}, \rho ] ]. \tag {26}
$$

The above dissipation contribution is of the Lindblad's form [cf. Eq. (22)]. Obviously, in the case of pure-dephasing (with the absence of $T_{1}$ -energy relaxations; cf. Sec. V), the reduced density operator does not necessarily evolve toward the stationary solution $\rho_{\mathrm{eq}}$ of Eq. (17).

## IV. FOKKER-PLANCK EQUATIONS

In this section, we shall relate the BRT [Eq. (11)] to a class of quantum FPE involving $T_{1}$ -energy relaxation and/or pure- $T_{2}$ dephasing. The derivation presented in the following is exact for a single-surface harmonic system. However, the resulting FPE can also be served as approximations for an-harmonic systems. The most important FPE that satisfies simultaneously the detailed-balance and positivity, will be presented in Sec. IV D and also as a special case in Sec. IV E.

## A. Background algebra in harmonic systems

Let us consider a damped harmonic system. The Hamiltonian for the reduced system is given by

$$
H = \frac {p ^ {2}}{2 m} + \frac {1}{2} m \Omega^ {2} (q - \bar {q} _ {\mathrm{eq}}) ^ {2} \equiv \hbar \Omega \left(a ^ {\dagger} a + \frac {1}{2}\right). \tag {27}
$$

Here, m is the reduced mass, $\Omega$ the frequency, q and p the Cartesian coordinate and momentum of the oscillator, respectively. Included explicitly in Eq. (27) is the internal coordinate reference $\overline{q}_{eq}$ . Given in the second identity of Eq. (27) is also the Hamiltonian in terms of the creation operator $a^{\dagger}$ and the annihilation operator a,

$$
a \equiv \sqrt {\frac {m \Omega}{2 \hbar}} \left(q - \bar {q} _ {\mathrm{eq}} + i \frac {p}{m \Omega}\right). \tag {28}
$$

We have $[a, a^{\dagger}] = 1$ , $[a^{\dagger}a, a] = -a$ , and $[a^{\dagger}a, a^{\dagger}] = a^{\dagger}$ . In the harmonic system [Eq. (27)], the above identities lead to $g(\mathcal{L})a = g(-\Omega)a$ and $g(\mathcal{L})a^{\dagger} = g(\Omega)a^{\dagger}$ , respectively. Here, $g(\omega)$ is an arbitrary function of $\omega$ .

In relation to the BRT [Eq. (11)], we shall be interested in the spectrum conjugation [cf. Eq. (11b)] to a given dissipative mode. In the following subsections, we shall consider the cases in which the dissipative modes are the coordinate and momentum. Their spectrum conjugations will be easily obtained via the spectrum conjugations of a and $a^{\dagger}$ . By using the aforementioned properties of a harmonic system, we have [cf. also Eqs. (12) and (15)],

$$
C _ {\alpha} (- \mathcal {L}) a = C _ {\alpha} (\Omega) a = 2 \gamma_ {\alpha} (\bar {n} + 1) a, \tag {29a}
$$

$$
C _ {\alpha} (- \mathcal {L}) a ^ {\dagger} = C _ {\alpha} (- \Omega) a ^ {\dagger} = 2 \gamma_ {\alpha} \bar {n} a ^ {\dagger}. \tag {29b}
$$

Here, $\gamma_{\alpha}$ denotes the spectral density and $\bar{n}$ the thermal occupation number of the harmonic oscillator,

$$
\gamma_ {\alpha} \equiv J _ {\alpha} (\Omega), \tag {30a}
$$

$$
\bar {n} \equiv (e ^ {\beta \Omega} - 1) ^ {- 1}. \tag {30b}
$$

Equation (29) will be used later to construct the FPE for the case in which the dissipative mode is chosen to be coordinate or momentum. We shall also see that $\gamma_{\alpha}$ defined in Eq. (30a) amounts to the energy relaxation rate.

For the later use, we shall also denote the coordinate and momentum variances of the reduced system at the thermal equilibrium. They are given by

$$
\sigma_ {q q} ^ {\mathrm{eq}} \equiv \operatorname{Tr} \left[ (q - \bar {q} _ {\mathrm{eq}}) ^ {2} \rho_ {\mathrm{eq}} \right] = \hbar (\bar {n} + 1 / 2) / (m \Omega), \tag {31a}
$$

$$
\sigma_ {p p} ^ {\mathrm{eq}} \equiv \operatorname{Tr} \left[ (p - \bar {p} _ {\mathrm{eq}}) ^ {2} \rho_ {\mathrm{eq}} \right] = \hbar m \Omega (\bar {n} + 1 / 2). \tag {31b}
$$

The first identities in Eqs. (31a) and (31b) are definitions and will be used in both harmonic and anharmonic systems, while the second identities are only valid in the harmonic case.

## B. Dissipation via coordinate: Brownian oscillator

Let us first consider the case in which the dissipative mode assumes to be the dimensionless coordinate,

$$
Q _ {q} = \sqrt {\frac {m \Omega}{\hbar}} q = \frac {1}{\sqrt {2}} (a + a ^ {\dagger}). \tag {32}
$$

Its spectrum conjugation, $\widetilde{Q}_{q}=C_{q}(-\mathcal{L})Q_{q}$ [Eq. (11b)], can be obtained easily by using Eq. (29). We have

$$
\begin{array}{l} \widetilde {Q} _ {q} = \frac {1}{\sqrt {2}} [ C _ {q} (\Omega) a + C _ {q} (- \Omega) a ^ {\dagger} ] \\ = \frac {2}{\sqrt {2}} \gamma_ {q} [ (\bar {n} + 1) a + \bar {n} a ^ {\dagger} ] \\ = 2 \gamma_ {q} \sqrt {\frac {m \Omega}{\hbar}} \left[ \left(\bar {n} + \frac {1}{2}\right) q + i \frac {p}{2 m \Omega} \right]. \tag {33} \\ \end{array}
$$

By substituting Eqs. (31b)-(33) into Eq. (11), we obtain

$$
\dot {\rho} = - \frac {i}{\hbar} [ H, \rho ] - \gamma_ {q} \mathcal {R} _ {q} \rho , \tag {34a}
$$

$$
\mathcal {R} _ {q} \equiv \frac {1}{\hbar^ {2}} \sigma_ {p p} ^ {\mathrm{eq}} [ q, [ q, \rho ] ] + \frac {i}{2 \hbar} [ q, \{p, \rho \} ]. \tag {34b}
$$

Here, $\sigma_{pp}^{eq}$ [Eq. (31b)] is the momentum variance at the thermal equilibrium, and $\{\cdot,\cdot\}$ denotes the anticommutator,

$$
\{A, B \} \equiv A B + B A. \tag {35}
$$

In the harmonic system, Eq. (34) is equivalent to Eq. (11), and thus satisfies the detailed-balance (Sec. III B). In an anharmonic system, Eq. (34) however serves an approximation. In this case, $\sigma_{pp}^{eq}$ in Eq. (34) should be evaluated via the first identity of Eq. (31b) with the exact $\rho_{eq}$ [Eq. (17)]. As a result, Eq. (34) is expected to be a very good approximation in a single-well anharmonic system.

Equation (11) satisfies also the translational invariance but not the general positivity. By using Eq. (34), we have $\dot{\bar{q}}(t)=\bar{p}(t)/m$ . Therefore, the dissipative system described here is a quantum Brownian oscillator. The other Ehrenfest equations of motion for the Brownian oscillator will be presented as a special case in Appendix B.

## C. Dissipation via momentum

Let us now consider the case where the dimensionless momentum serves as a dissipative mode,

$$
Q _ {p} = (\hbar m \Omega) ^ {- 1 / 2} p = \frac {1}{i \sqrt {2}} (a - a ^ {\dagger}). \tag {36}
$$

Note that $d\langle\hat{A}\rangle/dt=i\langle[H_{T},\hat{A}]\rangle$ ; with $H_{T}$ being the total system–bath Hamiltonian, is valid for an any dynamic variable $\hat{A}$ . However, the system–bath coupling via momentum leads to that $\dot{\bar{q}}(t)\neq\bar{p}(t)/m$ . They are therefore not for a Brownian oscillator.

Following the same procedure used in Eqs. (32)-(34) we obtain the following FPE with the momentum coupling induced dissipation:

$$
\dot {\rho} = - \frac {i}{\hbar} [ H, \rho ] - \gamma_ {p} \mathcal {R} _ {p} \rho , \tag {37a}
$$

$$
\mathcal {R} _ {p} \rho = \frac {1}{\hbar^ {2}} \sigma_ {q q} ^ {\mathrm{eq}} [ p, [ p, \rho ] ] - \frac {i}{2 \hbar} [ p, \{q - \bar {q} _ {\mathrm{eq}}, \rho \} ]. \tag {37b}
$$

Here, $\sigma_{qq}^{eq}$ [Eq. (31a)] is the coordinate variance at the thermal equilibrium. Again, Eq. (37b) satisfies the detailed-balance exactly in a harmonic system but only approximately in an anharmonic case. Both the translational invariance and the general positivity are however not satisfied. The internal coordinate reference $\bar{q}_{eq}$ is explicitly included to specify Eq. (37b) unambiguously. The Ehrenfest equations of motion associating with the $Q_{p}$ dissipative mode will be presented as a special case in Appendix B.

## D. Some prescriptions of optical quantum dissipation theory

The QDT that has been widely used in the laser physics community is given by $^{5-8}$

$$
\dot {\rho} = - \frac {i}{\hbar} [ H, \rho ] - \gamma_ {1} \mathcal {R} _ {r} \rho , \tag {38a}
$$

$$
\mathcal {R} _ {r} \rho \equiv \frac {1}{2} (\bar {n} + 1) [ a ^ {\dagger}, a \rho ] + \frac {1}{2} \bar {n} [ a, a ^ {\dagger} \rho ] + \mathrm{H.c.} \tag {38b}
$$

Here, $\gamma_{1}$ denotes the energy relaxation rate [cf. Eq. (B4c)]. Obviously, the optical QDT is of the Lindblad's form of positivity [Eq. (22)]. In this subsection, we shall revisit the optical QDT [Eq. (38)] by making use of the Bloch–Redfield/Fokker–Planck formulation developed in this work. It will be shown that the optical QDT [Eq. (38)] satisfies the detailed-balance and positivity, but not the translational invariance. Provided in the following are also some prescriptions to the optical QDT [Eq. (38)].

To proceed, let us recast $R_{q}$ [Eq. (34b)] and $R_{p}$ [Eq. (37b)] in terms of creation and annihilation operators. We obtain

$$
\mathcal {R} _ {q} \equiv \mathcal {R} _ {r} + \mathcal {R} _ {n r}, \tag {39a}
$$

$$
\mathcal {R} _ {p} \equiv \mathcal {R} _ {r} - \mathcal {R} _ {n r}. \tag {39b}
$$

Here, $\mathcal{R}_r$ was given by Eq. (38b), while

$$
\mathcal {R} _ {n r} \rho \equiv \frac {1}{2} (\bar {n} + 1) [ a, a \rho ] + \frac {1}{2} \bar {n} [ a ^ {\dagger}, a ^ {\dagger} \rho ] + \mathrm{H.c.} \tag {40}
$$

Obviously, $R_{r}$ and $R_{nr}$ can be considered as the rotating-wave-approximation (RWA) and the anti-RWA contributions to $R_{q}$ (or $R_{p}$ ), respectively. Thus, the optical QDT [Eq. (38)] can be given as the RWA prescription via the single dissipative mode of either $Q_{q}$ [Eq. (32)] or $Q_{p}$ [Eq. (36)]. Moreover, the RWA term $R_{r}$ [Eq. (38b)] is of the Lindblad's form [Eq. (22)], while the anti-RWA term $R_{nr}$ [Eq. (40)] does not preserve the general positivity. It was also pointed out by Kohen, Marson and Tannor $^{26}$ that $R_{r}$ and $R_{nr}$ are the secular and the nonsecular contributions, respectively, to the Redfield tensor $R_{q}$ . In other words, the RWA is equivalent to the secular approximation in the system of study.

Besides the RWA (or secular approximation) prescription, Eq. (39) renders an alternative prescription to the optical QDT [Eq. (38)], considered as a special case of the BRT/FPE [Eq. (11) for the harmonic system] with the equally contributed dissipations via both $Q_{q}$ and $Q_{p}$ . In this case, $\gamma_{q} = \gamma_{p} = \gamma_{1}/2$ , and the total dissipation is described by $R = \gamma_{q} R_{q} + \gamma_{p} R_{p} = \gamma_{1} R_{r}$ , leading to the required optical QDT of Eq. (38).

In concluding this subsection, let us recast $R_{r}$ [Eq. (38b)] and $R_{nr}$ [Eq. (40)] in terms of coordinate and momentum. We have

$$
\begin{array}{l} \mathcal {R} _ {r} \rho = - \frac {i}{4 \hbar} [ \{q - \bar {q} _ {\mathrm{eq}}, p \}, \rho ] + \frac {i}{2 \hbar} [ q, \{p, \rho \} ] \\ + \frac {1}{2 \hbar^ {2}} \{\sigma_ {p p} ^ {\mathrm{eq}} [ q, [ q, \rho ] ] + \sigma_ {q q} ^ {\mathrm{eq}} [ p, [ p, \rho ] ] \}, (41a) \\ \mathcal {R} _ {n r} \rho = \frac {i}{4 \hbar} [ \{q - \bar {q} _ {\mathrm{eq}}, p \}, \rho ] + \frac {1}{2 \hbar^ {2}} \{\sigma_ {p p} ^ {\mathrm{eq}} [ q, [ q, \rho ] ] \\ - \sigma_ {q q} ^ {\mathrm{eq}} [ p, [ p, \rho ] ] \}. (41b) \\ \end{array}
$$

$$
\begin{array}{l} \mathcal {R} _ {n r} \rho = \frac {i}{4 \hbar} [ \{q - \bar {q} _ {\mathrm{eq}}, p \}, \rho ] + \frac {1}{2 \hbar^ {2}} \{\sigma_ {p p} ^ {\mathrm{eq}} [ q, [ q, \rho ] ] \\ - \sigma_ {q q} ^ {\mathrm{eq}} [ p, [ p, \rho ] ] \}. \tag {41b} \\ \end{array}
$$

Both the above two equations depend explicitly on the internal coordinate system or $\overline{q}_{eq}$ . They are therefore not translational invariance. In deriving Eq. (41), we have used the following identity:

$$
[ q, \{p, \rho \} ] + [ p, \{q - \bar {q} _ {\mathrm{eq}}, \rho \} ] = [ \{q - \bar {q} _ {\mathrm{eq}}, p \}, \rho ]. \tag {42}
$$

Equation (41), together with the formulation in Sec. III E, will be used in the following subsection to construct the generalized Fokker–Planck equation in the presence of both $T_{1}$ -relaxation and pure- $T_{2}$ dephasing.

## E. Generalized Fokker–Planck equation

We are in the position to summarize the generalized FPE theory involving both $T_{1}$ and pure- $T_{2}$ types of dissipation. We assume that there are a total of three independent dissipative modes. Two of them are chosen to be $Q_{q}$ [Eq. (32)] and $Q_{p}$ [Eq. (36)], respectively. These two dissipative modes are responsible for the $T_{1}$ -energy relaxation. The third dissipative mode that will be specified later is responsible for the pure- $T_{2}$ dephasing.

Let us start with the $T_{1}$ -energy relaxation involving both the $Q_{q}$ [Eq. (32)] and $Q_{p}$ [Eq. (36)] dissipative modes. We shall denote the overall $T_{1}$ -energy relaxation rate as $\gamma_{1}$ , and [cf. Eq. (30a)]

$$
\gamma_ {q} \equiv J _ {q} (\Omega) \equiv \frac {1}{2} (1 + \epsilon) \gamma_ {1}, \tag {43a}
$$

$$
\gamma_ {p} \equiv J _ {p} (\Omega) \equiv \frac {1}{2} (1 - \epsilon) \gamma_ {1}. \tag {43b}
$$

Here, $-1 \leqslant \epsilon \leqslant 1$ . Obviously, the ratio between the $Q_{q}$ and $Q_{p}$ 's contributions to the $T_{1}$ -relaxation rate is given by $(1 + \epsilon)/(1 - \epsilon) = \gamma_{q} / \gamma_{p}$ . Furthermore, we have

$$
\gamma_ {q} \mathcal {R} _ {q} + \gamma_ {p} \mathcal {R} _ {p} = \gamma_ {1} (\mathcal {R} _ {r} + \epsilon \mathcal {R} _ {n r}) \equiv \gamma_ {1} \mathcal {R} _ {1}. \tag {44}
$$

Here, $\mathcal{R}_r$ and $\mathcal{R}_{nr}$ are given by Eq. (41a) and (41b), respectively. Thus, the parameter $\epsilon$ relates directly to the contribution of the non-RWA contribution to the $T_{1}$ -relaxation.

The pure- $T_{2}$ dephasing mode [cf. Eq. (23)] is chosen to be

$$
Q _ {H} \equiv H / (\hbar \Omega) = a ^ {\dagger} a. \tag {45}
$$

In the second identity of the above equation, we removed the zero energy since it is irrelevant to the dissipative dynamics (cf. Sec. III C). The spectrum conjugation to $Q_{H}$ is given by [Eq. (24)]

$$
\tilde {Q} _ {H} = C _ {H} (0) Q _ {H} \equiv 2 \gamma_ {2} Q _ {H}. \tag {46}
$$

Here, $\gamma_{2} \equiv C_{H}(0)/2$ denotes the pure $T_{2}$ -dephasing rate and is given in term of spectral density as [cf. Eq. (25)]

$$
\gamma_ {2} \equiv C _ {H} (0) / 2 = (k _ {B} T / \hbar) \lim _ {\omega \to 0} J _ {H} (\omega) / \omega . \tag {47}
$$

Note that the pure- $T_{2}$ dephasing rate $\gamma_{2}$ [Eq. (47)] is proportional to the temperature, while the $T_{1}$ -energy relaxation rate $\gamma_{1}$ [cf. Eq. (43)] does not depend on the temperature.

The final Redfield–Fokker–Planck equation in the presence of both the $T_{1}$ -energy relaxation [Eq. (44)] and the pure $T_{2}$ -dephasing [Eq. (45)] is then given by

$$
\dot {\rho} = - \frac {i}{\hbar} [ H, \rho ] - \gamma_ {1} \mathcal {R} _ {1} \rho - \frac {\gamma_ {2}}{\hbar^ {2} \Omega^ {2}} [ H, [ H, \rho ] ], \tag {48}
$$

where $\mathcal{R}_1$ is given by Eq. (44) with (41); i.e.,

$$
\begin{array}{l} \mathcal {R} _ {1} \rho = \frac {i (\epsilon - 1)}{4 \hbar} [ \{q - \bar {q} _ {\mathrm{eq}}, p \}, \rho ] + \frac {i}{2 \hbar} [ q, \{p, \rho \} ] \\ + \frac {\epsilon + 1}{2 \hbar^ {2}} \sigma_ {p p} ^ {\mathrm{eq}} [ q, [ q, \rho ] ] - \frac {(\epsilon - 1)}{2 \hbar^ {2}} \sigma_ {q q} ^ {\mathrm{eq}} [ p, [ p, \rho ] ]. \tag {49} \\ \end{array}
$$

In the cases of $\epsilon = 0, 1$ , and $-1$ , the above $\mathcal{R}_1$ reduces to $\mathcal{R}_r$ [Eq. (41a) or (38b)], $\mathcal{R}_q$ [Eq. (34b)] and $\mathcal{R}_p$ [Eq. (37b) with (42)], respectively.

Again, Eq. (48) is completely equivalent to the BRT [Eq. (11)] in the harmonic system involving the three dissipative modes in consideration. It therefore satisfies the exact detailed-balance relation (cf. Sec. III B) for the harmonic system.

More importantly, Eq. (48) may also serve as the generalized FPE for anharmonic systems in which the detailed-balances are preserved approximately. The parameter $\Omega$ that appears in the last term of Eq. (48) and in determining the $T_{1}$ -relaxation rate $\gamma_{1}$ [Eq. (43)] is chosen to be the harmonic frequency, $\Omega = \sqrt{V''(\overline{q}_{\mathrm{eq}})/m}$ , of the system. The parameters, $\overline{q}_{\mathrm{eq}}, \sigma_{pp}^{\mathrm{eq}}$ , and $\sigma_{qq}^{\mathrm{eq}}$ , in Eq. (49) should be evaluated numerically by using their definitions [cf. Eq. (31)] with the exact $\rho_{\mathrm{eq}}$ [Eq. (17)]. It is thus expected that Eq. (48) renders an excellent semiclassical detailed-balance relation in a single-well anharmonic system. The $\gamma_{1}$ -term and $\gamma_{2}$ -term are responsible for the $T_{1}$ -relaxation and pure- $T_{2}$ dephasing, respectively. In the case of $\epsilon = 0$ , $\mathcal{R}_1$ reduces to $\mathcal{R}_r$ [Eq. (41a)], and the resulting FPE is of the Lindblad's form, no matter whether the system is harmonic or not! Therefore, Eq. (48) with $\epsilon = 0$ constitutes an almost fully satisfactory FPE for a general single-well anharmonic system.

Equation (48) constitutes the main result of this section. All the FPE developed in the previous subsections can be recovered from the generalized FPE Eq. (48) with setting $\gamma_{2}=0$ and the specific values for $\epsilon$ . Note that in a general anharmonic system, the generalized FPE Eq. (48) is not equivalent to the BRT [Eq. (11)]. The energy relaxation rate in the BRT [Eq. (11)] depends on the energy level space, while that in FPE [Eq. (48)] is however a constant $\gamma_{1}$ [Eq. (43)]. Thus, the FPE developed in this work is truly of Markovian. In a pure-dephasing case in which $\gamma_{1}$ , Eqs. (11) and (48) are identical.

## V. CLASSICAL ANALOGY TO QUANTUM PURE-DEPHASING

Dephasing (especially pure-dephasing) plays an important role in quantum dissipative dynamics. It is usually considered to be of pure quantum in nature, and analyzed via the eigenenergy representation. We shall in this section use the harmonic model [Eq. (27)] to provide a classical analogy to the quantum pure-dephasing dynamics.

Let us start with Eq. (48) in the absence of $T_{1}$ -relaxation ( $\gamma_{1}=0$ ),

$$
\dot {\rho} = - i \mathcal {L} \rho - \frac {\gamma_ {2}}{\Omega^ {2}} \mathcal {L} ^ {2} \rho . \tag {50}
$$

Here, $L \equiv \hbar^{-1}[H,\ldots]$ . We shall show that in the harmonic system the above equation can be mapped into a classical heat transfer problem [cf. Eq. (58)]. It is done by recognizing that the harmonic Liouvillian in the Wigner representation is given by

$$
- i \mathcal {L} _ {w} = \frac {\partial H _ {w}}{\partial q} \frac {\partial}{\partial p} - \frac {\partial H _ {w}}{\partial p} \frac {\partial}{\partial q} = m \Omega^ {2} q \frac {\partial}{\partial p} - \frac {p}{m} \frac {\partial}{\partial q}. \tag {51}
$$

We shall further introduce the polar coordinate $\{r,\phi\}$ for the phase-space,

$$
q \equiv [ 2 \hbar / (m \Omega) ] ^ {1 / 2} r \cos \phi , \tag {52a}
$$

$$
p \equiv (2 \hbar m \Omega) ^ {1 / 2} r \sin \phi . \tag {52b}
$$

Note that $\{p,q\}$ and $\{r,\phi\}$ in the above equation are not operators but the representation variables. In the Wigner polar phase-space representation, the harmonic Hamiltonian [Eq. (27)] is given by $H_{w}=\hbar\Omega r^{2}$ , while its Liouvillian [Eq. (51)] is by

$$
- i \mathcal {L} _ {w} = \Omega \frac {\partial}{\partial \phi}. \tag {53}
$$

Equation (50) for the harmonic system can therefore be recast in the Wigner polar-phase-space representation as

$$
\frac {\partial}{\partial t} \rho (r, \phi ; t) = \left(\Omega \frac {\partial}{\partial \phi} + \gamma_ {2} \frac {\partial^ {2}}{\partial \phi^ {2}}\right) \rho (r, \phi ; t). \tag {54}
$$

Obviously, r in the above equation can be taken as a constant parameter. This is consistent with the energy conservation in the absence of $T_{1}$ -relaxation. Without losing the generality, we may set

$$
\rho (r, \phi ; t) = R (r, t) \Phi (\phi , t). \tag {55}
$$

Equation (54) can now be recast as $R(r,t)=R(r,0)$ for energy conservation, together with

$$
\frac {\partial}{\partial t} \Phi (\phi , t) = \left(\Omega \frac {\partial}{\partial \phi} + \gamma_ {2} \frac {\partial^ {2}}{\partial \phi^ {2}}\right) \Phi (\phi ; t). \tag {56}
$$

The linear term in the above equation can be removed by setting

$$
\tilde {\phi} \equiv \phi + \Omega t. \tag {57}
$$

Equation (56) reduces now to

$$
\frac {\partial}{\partial t} \Phi (\tilde {\phi}, t) = \gamma_ {2} \frac {\partial^ {2}}{\partial \tilde {\phi} ^ {2}} \Phi (\tilde {\phi}; t), \tag {58}
$$

with the cyclic boundary condition of

$$
\Phi (\tilde {\phi} + 2 \pi , t) = \Phi (\tilde {\phi}, t). \tag {59}
$$

We have thus mapped the pure-dephasing into the classical problem of heat transport in a ring.

The heat transport equation can be solved analytically via the standard variable separation method together with the cyclic boundary condition. The normalized solution to Eq. (56) is given by

$$
\begin{array}{l} \Phi (\phi , t) = \frac {1}{2 \pi} + \frac {1}{\pi} \sum_ {n = 1} ^ {\infty} e ^ {- n ^ {2} \gamma_ {2} t} [ A _ {n} \cos n (\phi + \Omega t) \\ \left. + B _ {n} \sin n (\phi + \Omega t) \right]. \tag {60} \\ \end{array}
$$

The expansion parameters in the above equation can be determined by the initial condition,

$$
A _ {n} = \int_ {0} ^ {2 \pi} d \phi   \Phi (\phi , 0) \cos n \phi , \tag {61a}
$$

$$
B _ {n} = \int_ {0} ^ {2 \pi} d \phi   \Phi (\phi , 0) \sin n \phi . \tag {61b}
$$

Substituting Eq. (61) into Eq. (60), followed by some elementary algebra, the final solution to Eq. (56) can be written as

$$
\Phi (\phi , t) = \int_ {0} ^ {2 \pi} d \phi_ {0} G (\phi - \phi_ {0} + \Omega t, \gamma_ {2} t) \Phi (\phi_ {0}, 0). \tag {62}
$$

Here, $G(\phi, \tau)$ is the Green's function defined by

$$
G (\phi , \tau) \equiv \frac {1}{2 \pi} \sum_ {n = - \infty} ^ {\infty} e ^ {- n ^ {2} \tau} \cos n \phi . \tag {63}
$$

Note that

$$
G (\phi , \tau) = \left\{ \begin{array}{l l} (4 \pi \tau) ^ {- 1 / 2} e ^ {- \phi^ {2} / (4 \tau)}, & \tau \ll 1, \\ (2 \pi) ^ {- 1} + \pi^ {- 1} e ^ {- \tau} \cos \phi , & \tau \gg 1. \end{array} \right. \tag {64}
$$

Note that the Green's function in the final solution [Eq. (62)], i.e., $G(\phi - \phi_0 + \Omega t, \gamma_2 t)$ , assumes $G(\phi - \phi_0, 0) = \delta(\phi - \phi_0)$ at $t = 0$ . For $t \to \infty$ , $G \to (2\pi)^{-1}$ . The $\Omega t$ in $G(\phi - \phi_0 + \Omega t, \gamma_2 t)$ arises from the first term of Eq. (50) for the coherent dynamics. It describes a clockwise rotation of the reduced density operator $\rho$ in the phase-space with a constant angular velocity of $\Omega$ . In the rotation-frame, the angular variable is $\tilde{\phi}$ [Eq. (57)], and the Green's function in Eq. (62) becomes $G(\phi - \phi_0 + \Omega t, \gamma_2 t) = G(\tilde{\phi} - \phi_0, \gamma_2 t)$ , which is identical to that of heat transport in a ring. The pure-dephasing rate $\gamma_2$ thus maps into the heat diffusion constant. The above analogy is established via the harmonic system in which the iso-energy contours constitute circles with a common center in the phase-space. In general, the quantum pure-dephasing could be mapped into classical problems of heat transport in the iso-energy contours in phase-space.

## VI. SUMMARY AND CONCLUDING REMARKS

In summary, we have developed a unified algebraic approach to construct the BRT [Eq. (11)] and a generalized FPE [Eq. (48)]. The relation between these two theories of quantum dissipation is elucidated thoroughly.

The key step in deriving the compact form of the BRT [Eq. (11)] is to introduce the spectrum conjugation to a dissipative mode [cf. Eq. (11b)]. The resulting BRT is constructed in the operator level and enjoys the flexibility of implementation in comparing the conventional form of the BRT. For example, the spectrum conjugation operator $\widetilde{Q}$ [Eq. (11b)] can be evaluated in any representations via either the matrix transformation or the equation of motion method. $^{34}$ The new form of the BRT can even further be combined with quantum chemistry methods such as semi-empirical and ab initio LCAO-MO calculations to investigate the correlated quantum dynamics of the many-body interaction and dissipation in conjugated electronic systems. $^{34}$ In general, BRT satisfies the detailed-balance relation, but not the translational invariance. We shall therefore have to adopt an internal coordinate system such as Eq. (21) to specify the BRT unambiguously. Note that in the present work, the dissipative mode $Q_{\alpha}$ was chosen to be Hermitian. A generalized BRT based on the non-Hermitian dissipative modes description, which will be published elsewhere, can also be developed along the similar algebraic approach used in this work.

The generalized FPE [Eq. (48)] was derived from the BRT [Eq. (11)] via the harmonic system [Eq. (27)]. They are therefore equivalent in the harmonic system of study. In an anharmonic system, the generalized FPE [Eq. (48)] renders a semiclassical detailed-balance relation up to the second moments in phase space. It thus constitutes an excellent approximation especially in the case of single-well potentials. Both the $T_{1}$ -energy relaxation and the pure- $T_{2}$ -dephasing processes were considered. In deriving Eq. (48), we also adopted the commonly used system-bath interaction model $^{14}$ to relate both the $T_{1}$ -relaxation rate $\gamma_{1}$ [Eq. (43)] and the pure- $T_{2}$ dephasing rate $\gamma_{2}$ [Eq. (47)] to the bath spectral densities. These two distinct dissipation dynamics were shown to be of very different temperature dependence. Furthermore, an analogy was made between the quantum pure-dephasing dynamics and the classical heat transport problems (cf. Sec. V).

The present unified Bloch–Redfield/Fokker–Planck theory of quantum dissipation can be of the Lindblad's form of general positivity. This is achieved at a special case of Eq. (48) in which the parameter $\epsilon=0$ in Eq. (49). The resulting equation relates closely to the conventional optical quantum dissipation theory (cf. Sec. IV D) that has been widely used in laser physics community. $^{5-8}$ The generalized FPE [Eq. (48)] that includes also the pure- $T_{2}$ dephasing is however applicable to both optical problems and anharmonic systems of general interest.

The Redfield approximation involved in the present unified Bloch–Redfield/Fokker–Planck theory was analyzed in detail in Sec. III A. This approximation consists of Eq. (10) for the complete neglect of bath dispersion and Eq. (5) for the complete neglect of the system–bath interaction in the initial density operator. The resulting formulation, Eqs. (10) or (48) thus only partially accounts for the second-order system–bath interaction. This is the main drawback of the present theories of quantum dissipation. Note that a full second-order Taylor expansion formulation of quantum dissipation theory has recently been developed by Meier and Tannor. $^{35}$ In their work, the correlated dynamics of the external driving field and dissipation was also treated properly in terms of a dissipation kernel that contains memory. The non-Markovian dissipation was further mapped into a local-time evolution of the reduced density operator and a set of auxiliary density operators. $^{35}$ As it has been analyzed in Sec. III A, the correlation between the time-dependent driving and dissipation is the main source of the non-Markovian nature in a quantum dissipation theory based on the cumulant expansion formulation. For most of the spectroscopic experiments where the optical measurements are operated away from the driving-dissipation cooperativity regions, one would not expect dramatic correlated non-Markovian effects. A generalized Markovian quantum dissipation theory beyond the Redfield approximation may also need to be developed as it would greatly facilitate simulations of nonlinear spectroscopies in condensed phases.

## ACKNOWLEDGMENTS

This work was financially supported by the Research Grants Council of the Hong Kong Government and the National Natural Science Foundation of China.

## APPENDIX A: REDFIELD TENSOR

We shall demonstrate in this appendix that Eq. (11) is actually equivalent to the conventional Redfield theory. $^{4}$ To proceed, let us examine the Redfield dissipation tensor elements associated with Eq. (11) in the energy eigenstate $\{|a\rangle\}$ representation. Note that the effects from statistically independent dissipative modes are additive. For simplicity, we shall in the following consider explicitly only a single dissipative mode Q. In the eigenenergy $\{|a\rangle\}$ representation, $\widetilde{Q}_{ab}=C(\omega_{ba})Q_{ab}$ [cf. Eq. (11b)]. By using Eq. (11a) or (4), we obtain

$$
\mathcal {R} _ {a b, a ^ {\prime} b ^ {\prime}} = (\mathcal {K} _ {a b, a ^ {\prime} b ^ {\prime}} + \mathcal {K} _ {b a, b ^ {\prime} a ^ {\prime}} ^ {*}) / 2, \tag {A1a}
$$

$$
\mathcal {K} _ {a b, a ^ {\prime} b ^ {\prime}} = \delta_ {b ^ {\prime} b} (Q \widetilde {Q}) _ {a a ^ {\prime}} - Q _ {b ^ {\prime} b} \widetilde {Q} _ {a a ^ {\prime}}. \tag {A1b}
$$

It is easy to show that $R_{ab,a'b'} = R_{ba,b'a'}^{*}$ and $\Sigma_{a}K_{aa,a'b'} = 0$ . The latter identity leads to the matter conservation law: $\Sigma_{a}R_{aa,a'b'} = 0$ . Each individual Redfield relaxation element $R_{ab,a'b'}$ in Eq. (A1) is of clear physical meaning. $^{4}$ For example, $-R_{aa,bb}$ amounts to rate of $|b\rangle$ to $|a\rangle$ transition. It is given by [cf. Eq. (A1)]

$$
\mathcal {R} _ {a a, b b} = - \left| Q _ {a b} \right| ^ {2} C (\omega_ {b a}); \quad \text { for } a \neq b. \tag {A2}
$$

This is a $T_{1}$ -relaxation rate and is proportional to $|Q_{ab}|^{2}$ . Equation (A2) leads directly to the detailed-balance condition: $\mathcal{R}_{aa,bb}/\mathcal{R}_{bb,aa}=C(\omega_{ba})/C(\omega_{ab})=e^{-\beta\omega_{ab}}$ [Eq. (12)]. Another type of secular tensor elements $R_{ab,ab}$ describes the dephasing. We have

$$
\begin{array}{l} \mathcal {R} _ {a b, a b} = \frac {1}{2} (\Gamma_ {a} + \Gamma_ {b}) + \frac {1}{2} C (0) (Q _ {a a} - Q _ {b b}) ^ {2} \\ \equiv \mathcal {R} _ {a b, a b} ^ {(1)} + \mathcal {R} _ {a b, a b} ^ {(2)}. \tag {A3} \\ \end{array}
$$

Here, $\mathcal{R}_{ab,ab}^{(1)}=(\Gamma_{a}+\Gamma_{b})/2$ , with $\Gamma_{n}\equiv-\Sigma_{m}^{\prime}\mathcal{R}_{mm,nn}$ being the Bloch's $T_{1}$ -relaxation rate of level $|n\rangle$ . The second term in Eq. (A3), or $\mathcal{R}_{ab,ab}^{(2)}=C(0)(Q_{aa}-Q_{bb})^{2}/2$ , relates only to the diagonal elements of Q and is responsible for the pure $T_{2}$ -dephasing. Equation (A3) recovers the celebrated relation in which the dephasing rate as a sum of the $T_{1}$ -induced contribution and the pure-dephasing rate. $^{3}$

## APPENDIX B: EHRENFEST EQUATIONS IN DISSIPATIVE HARMONIC SYSTEMS

We shall apply the generalized FPE [Eq. (48)] for the harmonic oscillator [Eq. (27)] to construct the Ehrenfest equations of motion for the first and the second moments of the phase-space wave packet. By using the simple algebra for the harmonic system, we obtain

$$
\frac {d}{d t} \langle a \rangle = - i \Omega \langle a \rangle - \frac {\gamma_ {1} + 2 \gamma_ {2}}{2} \langle a \rangle + \frac {\epsilon \gamma_ {1}}{2} \langle a ^ {\dagger} \rangle , \tag {B1a}
$$

$$
\frac {d}{d t} \left\langle a ^ {2} \right\rangle = - (i 2 \Omega + \gamma_ {1} + 4 \gamma_ {2}) \left\langle a ^ {2} \right\rangle + \epsilon \gamma_ {1} \left[ \left\langle a ^ {\dagger} a \right\rangle - \bar {n} \right], \tag {B1b}
$$

$$
\frac {d}{d t} \langle a ^ {\dagger} a \rangle = - \gamma_ {1} [ \langle a ^ {\dagger} a \rangle - \bar {n} ] + \frac {\epsilon \gamma_ {1}}{2} \langle a ^ {2} + a ^ {\dagger 2} \rangle . \tag {B1c}
$$

The phase-space centers $\{\overline{q}(t),\overline{p}(t)\}$ and variance $\{\sigma_{qq}(t),\sigma_{pp}(t),\sigma_{pq}(t)\}$ can be evaluated via the following relations:

$$
\langle a \rangle \equiv \sqrt {\frac {m \Omega}{2 \hbar}} \left[ \bar {q} (t) + i \frac {\bar {p} (t)}{m \Omega} \right], \tag {B2a}
$$

$$
\langle a ^ {2} \rangle - \langle a \rangle^ {2} = \frac {m \Omega}{2 \hbar} \sigma_ {q q} (t) - \frac {1}{2 \hbar m \Omega} \sigma_ {p p} (t) + \frac {i}{\hbar} \sigma_ {p q} (t), \tag {B2b}
$$

$$
\langle a ^ {\dagger} a \rangle - \langle a ^ {\dagger} \rangle \langle a \rangle + \frac {1}{2} = \frac {m \Omega}{2 \hbar} \sigma_ {q q} (t) + \frac {1}{2 \hbar m \Omega} \sigma_ {p p} (t). \tag {B2c}
$$

Note that the last term of Eq. (48) is quadric. As a result, the reduced density operator in the Wigner phase-space representation, $\rho(p,q;t)$ , will not remain as a Gaussian even it was initially. However, Eq. (B1) shows that the equations of motion are closed not only for the first moments, but also for the second moments. In the absence of pure-dephasing ( $\gamma_{2}=0$ ), Eq. (48) is quadratic and $\rho(p,q;t)$ do remain as a Gaussian. The analytical solution to Eq. (B1) in the special case of $\{\epsilon=1,\gamma_{2}=0\}$ , i.e., the Brownian oscillator model described in Sec. IV B, was derived previously $^{36}$ in terms of $\{\overline{q}(t),\overline{p}(t),\sigma_{qq}(t),\sigma_{pp}(t),\sigma_{pq}(t)\}$ .

The solution to Eq. (B1) is particularly simple in the case of $\epsilon=0$ , in which Eq. (48) preserves the general positivity and is exact for harmonic systems. Note that Eq. (B1c) describes actually the mean energy evolution. Let us denote $\Delta\bar{E}(t)$ as the mean excess energy from the thermal equilibrium,

$$
\Delta \bar {E} (t) \equiv \left\langle E (t) - E _ {\mathrm{eq}} \right\rangle = \hbar \Omega \left[ \left\langle a ^ {\dagger} a \right\rangle - \bar {n} \right]. \tag {B3}
$$

The solution to Eq. (B1) in the special case of $\epsilon = 0$ can thus be expressed as

$$
\langle a (t) \rangle = e ^ {- (\gamma_ {1} + 2 \gamma_ {2}) t / 2} e ^ {- i \Omega t} \langle a (0) \rangle , \tag {B4a}
$$

$$
\langle a ^ {2} (t) \rangle = e ^ {- (\gamma_ {1} + 4 \gamma_ {2}) t} e ^ {- i 2 \Omega t} \langle a ^ {2} (0) \rangle , \tag {B4b}
$$

$$
\Delta \bar {E} (t) = e ^ {- \gamma_ {1} t} \Delta \bar {E} (0). \tag {B4c}
$$

Equation (B4c) shows clearly that the parameter $\gamma_{1}$ amounts to the energy relaxation rate.

Equation (B1) [or Eq. (B4)] also indicates the role of pure- $T_{2}$ dephasing in the first two moments of the reduced density wave packet $\rho(p,q;t)$ in phase-space. In the eigenenergy representation, the pure-dephasing tensor elements [cf. the last term of Eq. (48)] are given by $\mathcal{R}_{mn,m',n'}^{(2)} = \delta_{mm'}\delta_{nn'}\gamma_2(m-n)^2$ . This accounts for that the pure-dephasing rate in $\langle a\rangle$ is given by $\gamma_{2}$ [Eq. (B1a) or (B4a)], while that in $\langle a^{2}\rangle$ is by $4\gamma_{2}$ [Eq. (B1b) or (B4b)]. However, as mentioned earlier, $\rho(p,q;t)$ is not a Gaussian in the presence of pure-dephasing. The evolution of the first two moments in Eq. (B1) is insufficient in characterizing the non-Gaussian dynamics. The analytical solution directly to the non-Gaussian $\rho(p,q;t)$ with a pure-dephasing in the harmonic system is given in Sec. V.

$^{1}$ A. Abragam, The Principles of Nuclear Magnetism (Clarendon, Oxford, 1961).  
$^{2}$ R. K. Wangsness and F. Bloch, Phys. Rev. 89, 728 (1953).  
$^{3}$ F. Bloch, Phys. Rev. 105, 1206 (1957).  
$^{4}$ A. G. Redfield, Adv. Magn. Reson. 1, 1 (1965).  
$^{5}$ W. H. Louisell, Quantum Statistical Properties of Radiation (Wiley, New York, 1973).  
$^{6}$ In Quantum Statistics in Optics and Solid State Physics: Statistical Treatment of Open Systems by Generalized Master Equations, edited by F. Haake (Springer, Berlin, 1973), Springer Tracts in Modern Physics, Vol. 66.  
$^{7}$ H. Haken, Laser Theory (Springer, Berlin, 1970).  
$^{8}$ M. Sargent III, M. O. Scully, and J. W. E. Lamb, Laser Physics (Addison–Wesley, Reading, 1974).  
$^{9}$ G. Lindblad, Commun. Math. Phys. 48, 119 (1976).  
$^{10}$ G. Lindblad, Rep. Math. Phys. 10, 393 (1976).  
$^{11}$ V. Gorini, A. Kossakowski, and E. C. G. Sudarshan, J. Math. Phys. 17, 821 (1976).  
$^{12}$ R. Alicki and K. Lendi, Quantum Dynamical Semigroups and Applications: Lecture Notes in Physics 286 (Springer, New York, 1987).  
$^{13}$ R. P. Feynman and F. L. Vernon, Ann. Phys. (N.Y.) 24, 118 (1963).  
$^{14}$ U. Weiss, Quantum Dissipative Systems, 2nd ed. (World Scientific, Singapore, 1999), Series in Modern Condensed Matter Physics, Vol. 10.  
$^{15}$ N. G. van Kampen, Stochastic Processes in Physics and Chemistry (North-Holland, Amsterdam, 1992).  
$^{16}$ H. Dekker, Phys. Rep. 80, 1 (1981).  
$^{17}$ A. O. Caldeira and A. J. Leggett, Physica A 121, 587 (1983).  
$^{18}$ Y. Tanimura and P. G. Wolynes, Phys. Rev. A 43, 4131 (1991).  
$^{19}$ Y. J. Yan, Phys. Rev. A 58, 2721 (1998).  
$^{20}$ H. Grabert, P. Schranm, and G. L. Ingold, Phys. Rep. 168, 115 (1988).  
$^{21}$ B. J. Berne, in Physical Chemistry, An Advanced Treatise, edited by H. Eyring, W. Jost, and D. Henderson (Academic, New York, 1971), Vol. 8B, p. 539.  
22D. W. Oxtoby, Adv. Chem. Phys. 47, 487 (1981).  
23 P. Pechukas, Phys. Rev. Lett. 73, 1060 (1994).  
$^{24}$ R. W. Zwanzig, Annu. Rev. Phys. Chem. 16, 67 (1965).  
$^{25}$ H. Mori, Prog. Theor. Phys. 33, 423 (1965).  
$^{26}$ D. Kohen, C. C. Marson, and D. J. Tannor, J. Chem. Phys. 107, 5236 (1997).  
$^{27}$ W. T. Pollard, A. K. Felts, and R. A. Friesner, Adv. Chem. Phys. 93, 77 (1996).  
$^{28}$ L. Gammaitoni, P. Hänggi, P. Jung, and F. Marchesoni, Rev. Mod. Phys. 70, 223 (1998).  
$^{29}$ D. E. Makarov and N. Makri, Phys. Rev. B 52, R2257 (1995).  
30D. E. Makarov and N. Makri, Phys. Rev. E 52, 5863 (1995).  
$^{31}$ F. Shuang, C. Yang, H. Y. Zhang, and Y. J. Yan, Phys. Rev. E 61, 7192 (2000).  
$^{32}$ E. Merzbacher, Quantum Mechanics, 2nd ed. (Wiley, New York, 1970).  
$^{33}$ O. Kühn, Y. Zhao, F. Shuang, and Y. J. Yan, J. Chem. Phys. 112, 6104 (2000).  
$^{34}$ H. Zhang, X. Q. Li, S. Yokojima, G. H. Chen, and Y. J. Yan, J. Chem. Phys. (submitted).  
35C. Meier and D. J. Tannor, J. Chem. Phys. 111, 3365 (1999).  
36Y. J. Yan and S. Mukamel, J. Chem. Phys. 89, 5160 (1988).