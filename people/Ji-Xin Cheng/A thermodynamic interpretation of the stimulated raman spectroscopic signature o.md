# A Thermodynamic Interpretation of the Stimulated Raman Spectroscopic Signature of an Action Potential in a Single Neuron

Shamit Shrivastava1,2\*, Hyeon Jeong Lee3,4, and Ji-Xin Cheng3,4

1. Department of Engineering Science, University of Oxford, Oxford, UK  
2. Institute for Sound and Light, Rosalind Franklin Institute, Harwell, UK  
3. Department of Biomedical Engineering, Boston University, MA USA  
4. Department of Electrical and Computer Engineering, Boston University, MA USA

\*Corresponding Author: shamit.shrivastava@eng.ox.ac.uk

Draft: 15th October 2020

## Abstract

It has previously been suggested that the plasma membrane condenses and melts reversibly during an action potential in a neuron, analogous to an acoustic wave travelling in the compressive membrane region. If true it has fundamental consequences for our understanding of the regulation of biological functions during an action potential. It has long been known that the electrical dipoles in the neuronal membrane reorient during an action potential, observed through a variety of optical methods. However, this information has been insufficient to confirm if and how the collective thermodynamic state of the neuronal membrane changes during an action potential. Here, we show that hyperspectral stimulated Raman spectroscopy (SRS) can resolve the thermodynamic state of the neuronal membranes in a single neuron during an action potential. These measurements indicate that the system becomes ordered and compressed during the de-polarisation phase and disordered and expanded during hyper polarisation Therefore, the observation is consistent with the acoustic hypothesis and SRS provides a powerful tool to not only further validate the hypothesis in future, but also explore the role of membrane thermodynamics during an action potential.

## Introduction

Exciting a neuron causes all – or – none voltage spikes that can be measured between two electrodes that are placed across the neuronal membrane. These voltage spikes are known as action potentials and are generated in the neuronal membrane(1). The present understanding of the phenomenon of action potentials originated from extensive empirical studies on the electrochemical properties of nerves(2). However, these spikes can also be measured using nonelectrical methods such as changes in displacements(1, 3), turbidity, birefringence(4), fluorescence(1, 5), magnetic field(6), force(1), as well as temperature(1, 7). While these nonelectrical aspects of the action potential are well known, they are believed to be non – essential for the biological functions of the action potential. Moreover, the observations themselves are explained as epiphenomenon driven by the voltage spikes using empirical coupling coefficients(8). The model allows for mechanical wave-front to follow the ionic wave front, however a compression wave is the fastest displacement wave that can travel in a system as determined by the speed of sound (9). From a material perspective, changes in temperature and displacement are fundamental to the understanding of any spike or wave propagation phenomenon, as required by the conservation laws of mass, momentum, and energy(10). For example, the present understanding describes the action potential as a purely dissipative phenomenon in analogy to the burning of a fuse where the wavefront propagates as a result of irreversible and diffusive mass (ion) transfer. Hodgkin described in 1964, “The invariance of the action potential arises because the energy used in propagation does not come from stimulus but is released by the nerve fibre along its length. In this respect nervous conduction resembles the burning of a fuse of gunpowder and is unlike current in an electrical cable”(11). Disregarding the “energy of the stimulus” is equivalent to disregarding the role of reversible momentum transfer as seen, for instance, during a sound wave propagation. However, heat studies in nerves indicate that an action potentials is a substantially reversible process(7, 12). In fact, Lichtervelde et al.(13) recently showed that the magnitude of heats can be explained entirely if the process is assumed to be completely reversible and the redistribution of ions in the solvation layer is also accounted for. Such a description will be consistent with the coupling of the membrane’s ionic environment with a propagating acoustic wave as previously observed in a lipid monolayer(14). However, to address the question of reversibility it is important to address the efficiency of the process, or the ratio of irreversible to reversible heat. (12). The observed ratio of irreversible:reversible heat in nerves, is of the order of 1:10. Later measurements have observed this value to be even smaller at 6:230(15). Whereas the efficiency calculated on the basis of Hodgkin and Huxley models is of the order of 1:1, i.e. one order magnitude difference. Note that the calculation includes both the contribution from capacitive charging and entropic contribution of conformational changes in ionophores. Therefore, the electrochemical understanding of action potentials that ignores the role of heat and momentum transfer during the action potential has long been debated(1, 16–18).

Recent research has brought the thermodynamic underpinnings of the phenomenon at the centre of this debate by describing the nerve impulse as a material wave that propagates as a localized condensation of the membrane(19, 20). The theory incorporates all the non-electrical aspects of the nerve impulse as default thermodynamic couplings and explains the observed reversible heating and cooling as a default consequence of adiabatic compression and rarefaction of the medium during pulse propagation. A particular prediction of the theory is a change in the state of the matter so significant that the membrane’s thermodynamic susceptibilities, such as heat capacity and compressibility, change significantly. Such significant changes in the compressibility are observed during thermotropic transitions in biological(21, 22) as well as artificial lipid interfaces(23). Under such conditions the nonlinear properties of the action potentials, such as all – or – none excitation and annihilation of pulses upon collision, are also shown by compression waves in artificial lipid films(24, 25), indicating that the “invariance of action potentials” can arise also from momentum transfer. Therefore, the theory predicts a condensation (freezing) of the membrane during an action potential as it depolarises and a rarefaction (melting) as it polarises again. The hyperpolarisation is then a consequence of the inertia as the membrane relaxes(24, 26). However, a direct measurement of the membrane state to confirm its freezing during an action potential has remained elusive. Here, by observing the changes in a signature Raman peak of the plasma membrane, we confirm that the thermodynamic state of the membranes changes significantly, during an action potential in a single neuron.i.e. the collective order of the membrane undergoes cyclic change in a manner that is consistent with the acoustic hypothesis.

## Measuring thermodynamic state changes from light-matter interaction

Optical methods have a long history in measuring physical changes in the membrane during an action potential(5, 27). The electromagnetic nature of light allows probing the changes in the electric field around the dipoles, either extrinsic or intrinsic to the membrane, due to changes

Shrivastava, Lee, and Cheng

State change during action potential

in membrane potential. Thus changes in optical signals, in general, can be easily mapped to changes in membrane potentials, which form the basis for many important methods for studying action potentials. However, such light-matter interactions do not lie outside the purview of thermodynamics(28, 29), and the properties of light can indeed be used as thermodynamic observables of the system that they interact with(30, 31).

When photons interact with a material, a small fraction of their population changes its wavelength due to the second-order effects of the thermal fluctuations in the material(32). These perturbed photons lie on a spectrum and the frequency distribution of the photons directly represents the partition of thermal energy among the conformational states. Raman and infrared spectroscopy-based methods are well known to characterize the conformational state of artificial and biological membranes (33–35). Here, we exploit this relationship to obtain new insights into the nature of physical changes in neuronal membranes during an action potential.

We start with fact that the entropy of a membrane complex can be written as a thermodynamic function of the form $S \equiv S ( x _ { i } ) ( 3 1 , 3 6 )$ , where $x _ { i } ^ { \prime } s$ are the extensive observables of the system that can be measured experimentally, e.g. volume, number of charges, number of photons, enthalpy, and energy of compartments etc.

Using this the Taylor expansion of the entropy potential can be written as:

$$
S - S _ {0} = \sum_ {i} \frac {\partial S}{\partial x _ {i}} \delta x _ {i} + \sum_ {i, j} \frac {\partial^ {2} S}{\partial x _ {i} \partial x _ {j}} \delta x _ {i} \delta x _ {j} + \dots \tag {1}
$$

We employ the equation under the assumption of local equilibrium where the state variables $\begin{array} { r } { \sum _ { i } \frac { \partial S } { \partial x _ { i } } \delta x _ { i } \approx 0 ( 3 7 , 3 8 ) } \end{array}$ ???? . Then using eq. (1) and the inversion of Boltzmann principle $w = e ^ { S / k }$ it can be shown that various observables must be coupled by the relation

$$
\left\langle \Delta x _ {i}, \Delta x _ {j} \right\rangle \propto - \left(\frac {\partial^ {2} S}{\partial x _ {i} \partial x _ {j}}\right) ^ {- 1} \tag {2}
$$

The approach previously explained the changes in the emission spectra of solvato-chromic dyes embedded lipid vesicles exposed to shock waves(31). In this case the entropy potential was described as a function of the emission spectra of the dye, representing the distribution of the ground state dye molecules in equilibrium with the system.

So how do these equations help us in understanding thermodynamic changes in membranes using Raman spectroscopy? If the Raman spectrum is represented by the function $I _ { n }$ , i.e. the number of photons at wavenumber ??, then as per the above, we propose the ansatz that the entropy of a complex membrane can also be written as $S = S ( I _ { n } , x _ { i } )$ (28, 39). Since all the arguments of the function are experimentally measurable, the function provides a general basis for designing experiments, where $x _ { i }$ are chosen depending on the phenomenon of interest. For example, $I _ { n }$ can be measured as a function of temperature, ??, and in that case eq.(2) gives;

$$
\left\langle \Delta I _ {n}, \Delta H \right\rangle \propto - \left(\frac {\partial^ {2} S}{\partial H \partial I _ {n}}\right) ^ {- 1} = - \left(\frac {\partial}{\partial I _ {n}} \frac {\partial S}{\partial H}\right) ^ {- 1} = \kappa T ^ {2} \left(\frac {\partial I _ {n}}{\partial T}\right) \tag {3}
$$

i.e. small changes in intensity at a given wavenumber $\Delta I _ { n }$ for a given change in the total enthalpy of the system, $\Delta H$ are required to obey $\mathsf { e q . } ( 3 )$ as per the second law of thermodynamics. Here ?? is the Boltzmann constant and $\left( { \frac { \partial I _ { n } } { \partial T } } \right)$ represents the derivative of the experimentally measured function $I _ { n } ( T )$ . Therefore, for conformational changes that occur during a process in the membrane, as observed from $\Delta { { I } _ { n } } .$ , an equivalent enthalpy change can be estimated from Eq. (3). Similarly, $I _ { n }$ can also be investigated as a function of pressure or electric field to reflect changes in volume or membrane potential.

## State changes during voltage-clamped experiments

A voltage-clamp experiment can be assumed to be a constant temperature or isothermal experiment (at the temperature of the sample chamber), while other variables are free to adjust (e.g. membrane pressure or interfacial pH). Then the changes in state as per eq. (2) are due to changes in the electrical field applied to the membrane. Recently, Lee and Cheng reported spatially and temporally resolved $I _ { n }$ measurements on single neurons using stimulated Raman scattering (SRS) spectroscopy(40). As discussed above, the data was interpreted by studying $I _ { n }$ as a function of membrane potential, showing that structural changes in a single neuron can be resolved during an action potential based on observed $\Delta I _ { n }$ . Figure 1c shows a typical SRS spectrum of a neuron at the resting potential, $I _ { n }$ for $n \in [ 2 8 0 0 , 3 0 0 0 ] c m ^ { - 1 }$ indicating the strongest contribution from a peak at $2 9 3 0 c m ^ { - 1 }$ . Figure 1e shows the changes in the SRS spectra $\Delta I _ { n }$ measured during somatic voltage clamp of a neuron $( - 8 0 m V t o + 3 0 m V )$ with respect to the resting potential of −60????. Thus, the intensity of $2 9 3 0 c m ^ { - 1 }$ peak decreases in response to membrane depolarisation and increase upon hyperpolarisation.

![](images/c8e98c89435ec0f8decdc9cc5a09fffe37c4b4cf1144c0b1b4e46898a6105350.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing a neuron labeled SRS with a blue triangle marker and scale bar (no text or symbols beyond labels)
</details>

![](images/a5e987504bdaeb04cd40c92cd7a1cd8fadc1acee759b3bc7c5956b91dec105c2.jpg)

<details>
<summary>stacked bar chart</summary>

| Stage | Value |
|-------|-------|
| Voltage-clamp command | 1s |
| Recording | ... |
| SRS images | 2803 |
| Raman shift (cm⁻¹) | 2850 |
| Time sequential | 2930 |
| Time sequential | 2938 |
| Time sequential | 2990 |
| Time sequential | 3000 |
</details>

![](images/9e7f94bd52e900fb271057d46d497476ffc92639c91942231c810671accd4899.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Intensity (a.u.) |
| ------------------ | ---------------- |
| 2800               | 0.0              |
| 2850               | 1.0              |
| 2900               | 4.0              |
| 2950               | 8.0              |
| 3000               | 1.0              |
</details>

![](images/f5ebd179fcf15f199b0d5f98c87fd97a98857ae8ee0e7610d921de0c77897774.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | ΔI (a.u.) |
| ------------------ | --------- |
| 2800               | 0.0       |
| 2850               | -0.1      |
| 2900               | -0.3      |
| 2950               | -0.4      |
| 3000               | 0.0       |
</details>

![](images/c7bcd588418d22b9fedfe78ea5f120ebaa55a0f745541dbf7a87931607421a5e.jpg)

<details>
<summary>scatterplot</summary>

| Voltage (mV) | ΔI/I (%) |
| ------------ | -------- |
| -80          | 3        |
| -60          | 0        |
| -20          | -6       |
| 20           | -8       |
</details>

Figure 1 (a) SRS image of a patched neuron with micropipette position indicated. Scale bar: 10 μm. (b) Schematic of hyperspectral SRS imaging of neurons while holding different potentials. (c) Representative SRS spectrum of a patched neuron (dot), fitted using seven Lorentzian (colored lines) with major contributing bands filled, 2850 (orange) and 2930 cm-1 (green). Red: cumulative fitted curve. (d) SRS spectral change, ΔI (dots), of the neuron from −60 to +30 mV with fitted curve (line). (e) Percentage changes of SRS intensity (ΔI/I) of neurons at $2 9 3 0 c m ^ { - I }$ at various membrane potentials. Error bars: + standard error of the mean (SEM). Reprinted (adapted) with permission from (J. Phys. Chem. Lett. 2017, 8, 9, 1932-1936). Copyright (2017) American Chemical Society

A potential mechanism was previously provided in terms of interaction of the Fermi-resonance component of the $2 9 3 0 c m ^ { - I }$ peak with the changes in the ionic environment during depolarisation. However, the magnitude of the effect was significantly less than changes observed during the voltage clamp experiment. Here, we provide a mesoscopic, empirical, and thermodynamic interpretation of these changes based on eq. (3). A salient feature of the approach as discussed above is that many effects of microscopic origin, which might all possibly contribute to observed changes in the Raman spectra, are implicitly accounted for the macroscopic entropy potential, including the changes in ionic environment, polarity, or any other microscopic agents of change. The analytical and logical consistency exists between the empirical equations that are independent of any molecular models. For example, eq. (3) does not assume the underlying molecular structure of the membrane, i.e. it is invariant of the molecular origin of Raman signal which could be due to any protein, lipids, ion, etc. This invariance provides us with means to refer to model systems for simulating $\Delta I _ { n }$ (as observed in real neurons) and derive new insights from it. In this sense, changes in $I _ { 2 9 3 0 }$ as a function of the state has been measured in a variety of artificial as well as biological membranes. Both in lipids and proteins, the band represents a "melting marker" as the peak at $2 9 3 0 c m ^ { - 1 }$ appears in difference spectra $\Delta I _ { n }$ only when the corresponding state change involves a cooperative thermotropic transition or melting(41). These studies(42–45) usually measure intensity around $2 9 3 0 c m ^ { - 1 }$ relative to intensity at another wavenumber, which provides an internal reference that removes systematic errors. Note that thermotropic transitions are not exclusive to pure lipid membranes or proteins, the cooperativity during the transitions is long known to extend over domains or proto-mers consisting of both proteins and lipids(42, 46). Furthermore, $\Delta I _ { n }$ have been measured for thermotropic transitions in membranes and proteins induced by a variety of thermodynamic fields including temperature(41, 44, 47), pressure(45), as well as pH(42). Thus, the term “thermotropic transition” is employed in the most general sense, which is indicated by a nonlinearity or cooperativity in the functional relationship between the thermodynamic variables. For example, by observing nonlinearities in $I _ { 2 9 3 0 }$ as a function of pH and temperature in erythrocytes ghosts, others have previously concluded that $\Delta I _ { 2 9 3 0 }$ represents a “concerted process at apolar protein-lipid boundaries”(42, 43). Thus a change in $2 9 3 0 \ c m ^ { - I }$ peak can represent a change in the order of either lipids, proteins, or their combination.

Therefore, $\Delta I _ { 2 9 3 0 }$ in figure 1 shows that the membrane essentially undergoes a collective increase in order during voltage-clamped depolarisation. That is, just like temperature, pressure, and pH; membrane potential can also induce an ordering effect in the membrane. Furthermore, based on observed $\Delta I _ { 2 9 3 0 }$ in figure 1 the extent of ordering can also be estimated. For example, $( I _ { 2 9 3 0 } / I _ { 2 8 5 0 } )$ changes from 1.9 at −60???? (resting potential) to $1 . 6 ~ \mathrm { a t } + 3 0 m V$ (depolarised), i.e. \~18% change. Temperature dependence of Raman spectra has been measured previously in a variety of neuronal membranes(48, 49). For example, in unmyelinated garfish olfactory nerve, the ratio $( I _ { 2 9 5 0 } / I _ { 2 8 8 5 } )$ was measured as a function of temperature. The ratio changes from 1.22 at 25 to 1.09 at 6 , i.e. 12% change over $\Delta T =$ $1 9 ~ \mathcal { C } ,$ which as discussed in detail by the authors, represents a significant increase in order. On the other hand, based on the SRS study in primary neurons by Lee et al.(40), $( I _ { 2 9 5 0 } / I _ { 2 8 8 5 } )$ changes from 1.18 at −60???? (resting potential) to 1.04 at +30???? (depolarised), i.e. 13% change.. It is important that unlike other optical observables measured previously, where the sign of the signal could not be interpreted in absolute terms, a negative $\Delta I _ { 2 9 3 0 }$ has an absolute meaning which indicates an increase in order.

Using these numbers, we estimate the enthalpy of phase change as well as average heat capacity of neuronal membranes from $I _ { n } ( T )$ using the Van’t Hoff’s approximation (50) and equilibrium constant defined in terms of Raman intensities (51);

$$
\frac {d \ln K}{d T} = \frac {\Delta H}{R T ^ {2}} \tag {4}
$$

$$
\frac {\Delta K}{K} \approx \frac {\Delta \left(I _ {2 9 5 0} / I _ {2 8 8 5}\right)}{\left(I _ {2 9 5 0} / I _ {2 8 8 5}\right)} \tag {5}
$$

A 12% change in $( I _ { 2 9 5 0 } / I _ { 2 8 8 5 } )$ over $\Delta T = 1 9 \mathrm { ~ ‰ ~ }$ gives an average $\Delta H \approx 4 . 5 \ : k J / m o l$ and $c _ { P } =$ $2 2 4 J m o l ^ { - 1 } K ^ { - 1 }$ . These values are now employed to estimate state changes during an action potential.

## State changes during an action potential

Can the analysis be extended to state changes during an action potential? Raman spectroscopy has a long history of determining dynamic state changes within propagating wavefronts in fields like thermos-fluids(52–54). While the above discussion assumed equilibrium during voltage clamp, eq. (2) can be extended to an arbitrary macroscopic state (partial equilibrium)(38); by observing region so small that the corresponding relaxation time $( \approx l / c $ , ?? is the length of the region, and ?? is the speed of sound in the medium) is smaller than the fastest timescale of interest in the underlying process. SRS signal (fig. 2) obtained previously during an action potential in a single neuron satisfies these criteria and showed $\Delta I _ { 2 9 3 0 } \approx - 1 \%$ upon depolarisation and $\Delta I _ { 2 9 3 0 } \approx + 1 \%$ upon hyperpolarisation during an action potential.

![](images/b8644ec7a07bb21fcfb5a9aa025b8a25f76736b6ae88537c3f0acefcb6f8a32f.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing a red-stained vascular structure with a blue triangle marker and dotted line, labeled 'SRS' in top-left corner (no other text or symbols)
</details>

![](images/84caa4860ac6b0ccb46504dd63516cb8da544665c76f549579484a9de1307030.jpg)

<details>
<summary>line chart</summary>

| Signal Type       | Value     |
| ----------------- | --------- |
| 3-trial average   | Not labeled |
| Single trial      | 1%        |
| Blue waveform     | 20 mV     |
| Blue waveform     | 10 ms     |
</details>

Figure 2. (a) SRS image of a patched neuron. The dashed line indicates the scanning trace. (b) 3-trial average (black) and single-trial SRS time trace (red) of the neuron shown in panel a with simultaneous current clamp recording (blue), showing a single action potential. The SRS intensity was normalized by the SRS reference generated with the same pulses. Scale bar: 20 μm. Reprinted (adapted) with permission from (J. Phys. Chem. Lett. 2017, 8, 9, 1932-1936). Copyright (2017) American Chemical Society

Note that unlike the voltage-clamp experiments where the temperature is constant, there is no such requirement during an action potential, which represents a fundamentally different thermodynamic process. To compare the two, recall that there are quantities that can remain constant even during such dynamic process, most well-known being the entropy that remains constant, for example, during the propagation of sound waves. While an infinitesimal acoustic perturbation is completely reversible, finite amplitude sound waves, for example shock waves, are dissipative. However, even in the case of shock waves the entropy production depend on third order changes in volume and pressure. As a result, state change across a shock front is still adiabatic to second order. (55, 56). Furthermore, the observed temperature changes during a nerve impulse indicate a substantially reversible phenomenon, which led to the original suggestion that nerve impulse or action potentials emerge from the same underlying physics as sound waves(16).

## Relation to the thermodynamics of compression waves and fluctuations

So if the state changes during an action potential are indeed similar to those that might occur during sound waves, how do we reconcile (i) the membrane freezes, while (ii) the temperature increases, (iii) the entropy remains constant, and (iv) channel activity increases? Critical insights on this matter have been generated by studying 2D compression waves and fluctuations in artificial lipids films.

Let us first consider the compression waves. Remarkably, near an order-disorder transition in a lipid film, these waves show many key characteristic properties of action potentials including all-or-none excitation(20, 24) and annihilation upon collision(25). In the case of artificial lipid films, the characteristics emerge naturally from the underlying thermodynamic state changes. The picture that has emerged is plotted in figure 3. Note how the phase transition region can be traversed differently at a constant temperature, constant entropy, or constant pressure. Consider the initial state of the membrane represented by $( T _ { 0 } S _ { 0 } )$ , then $\Delta I _ { 2 9 3 0 } \approx - 9 \%$ during the voltage clamp represents condensation along a constant temperature path $( T = T _ { 0 } )$ , while $\Delta I _ { 2 9 3 0 } \approx - 1 \%$ during the action potential represents condensation along constant entropy path $( S = S _ { 0 } )$ . It is important to recall that conventionally the membrane state are velieved to be the same at the same voltage during a voltage clamp experiment and during an action potential, however this is inconsistent with the above changes in Raman spectra.

Therefore, the competition between the condensing effect of the electromechanical compression of the membrane and the fluidizing effect of the increase in temperature due to the release of latent heat is determined by the inclination of the co-existence region in the TS diagram, a parameter known as retrogradicity(20, 57). Another way to interpret the behaviour is in terms of heat capacity; if the heat capacity of a material is sufficiently high, the temperature rise due to the latent heat (released during condensation) will be small enough for the system to still condense under compression. For example, water vapour does not condense upon adiabatic compression. On the other hand, polymers with chain lengths greater than 4 carbon atoms, typically show retrograde behaviour and condense upon adiabatic compression $( c _ { P } >$ ${ \sim } 2 0 0 J m o l ^ { - 1 } K ^ { - 1 } )$ .(58)

Therefore, the observed $\delta I _ { 2 9 3 0 } \left( t \right)$ has thermal as well as electromechanical contributions that can be estimated to first order using;

$$
\delta I _ {2 9 3 0} (t) _ {\text {heat corrected}} = \delta I _ {2 9 3 0 V} + \delta I _ {2 9 3 0 T} \tag {6}
$$

$$
\delta I _ {2 9 3 0 T} \approx \left(\frac {\partial I _ {n}}{\partial T}\right) \delta T \tag {7}
$$

$$
\delta I _ {2 9 3 0 V} \approx \left(\frac {\partial I _ {n}}{\partial V}\right) \delta V \tag {8}
$$

To evaluate these equation we make following assumptions; (i) the resting state is close to the phase boundary, (ii) due to latent heat contributions ∆?? is assumed large compared to state changes that do not involve a phase change, (iii) $\delta V ( t )$ is assumed to span the phase change region completely, i.e. the fraction of membrane in condensed phase, $\alpha = 0 \mathrm { a t } \delta V ( t ) =$ $- 6 0 m V \quad { \mathrm { ~ a n d ~ } } \quad \alpha = 1 \quad \quad { \mathrm { a t } } \quad \quad \delta V ( t ) = 3 0 m V , \quad { \mathrm { ~ ( i v ) ~ } } \quad \quad \Delta H _ { f l u i d - c o n d e n s e d } _ { a d i a b a t i c } = 1$ and ?? = 1 at ????(??) = 30????, (iv) ∆????????????→?????????????????? $\beta \Delta H _ { f l u i d  c o n d e n s e d } _ { i s o b a r i c }$ , where is $\beta$ is a phenomenological parameter $< 1$ as adiabatic phase change is closer to the apex of the coexistence dome (enthalpy of transition decreases as the transition temperature approaches critical temperature) and we assume $\Delta H _ { f l u i d  c o n d e n s e d _ { i s o b a r i c } } = 4 . 5 k J / m o l$ ∆????????????→?????????????????? , i.e. the estimate obtained above. With these assumptions we get;

$$
\delta I _ {2 9 3 0 T} (t) \approx \left(\frac {\partial I _ {n}}{\partial T}\right) \frac {\alpha (t) \beta}{c _ {p}} \Delta H _ {f l u i d \rightarrow c o n d e n s e d _ {i s o b a r i c}} \tag {9}
$$

$$
\alpha (t) = \frac {\delta V (t) - 6 0}{9 0} \tag {10}
$$

$\delta I _ { 2 9 3 0 } \left( t \right) _ { h e a t c o r r e c t e d }$ thus calculated is plotted in figure3 for $\beta = 0 . 4$ . As shown the measured $\delta I _ { 2 9 3 0 _ { T } } ( t )$ is recovered from the voltage clamp data after accounting for the latent heat during an adiabatic phase change. It is interesting to note that during the rising phase the estimated and observed $\delta I _ { 2 9 3 0 } ( t )$ align correctly, the recovery in measured $\delta I _ { 2 9 3 0 } ( t )$ occurs before the recovery of $\delta I _ { 2 9 3 0 _ { V } } ( t )$ indicating that membrane relaxation occurs before the recovery in voltage.

That the orientation of dipoles in the membrane changes was long known through an extensive range of studies, however a change in dipole orientation is necessary but not sufficient to conclude an increase in order(30, 59). For that, changes in both the magnitude and the distribution of an observable are required as indicated by eq. (2). Few previous studies have performed such experiments on nerves however a corresponding thermodynamic interpretation was not provided. For example, measurements of difference in infrared spectra between resting and excited state of nerve bundles from several species indicated changes in the conformation of membrane phospholipids(60). Similarly, Raman peaks of carotenoids(61) in the membrane during an action potential indicated compression of the molecules, however, whether the compression corresponds to freezing could not be inferred. Tasaki et.al. measured the difference in the emission spectrum between the resting and excited state of solvatochromic fluorescent dyes(62). While the observed blue shift indicated an increase in order, the recent thermodynamic interpretation of the spectral width of these dyes(39) confirmed that an increase in order was indeed observed in Tasaki’s experiments. However, given the uncertainty regarding the specific environment of dyes, doubts remained. Similarly, an order-disorder transition during an action potential has been indicated by the measurements of membranefluidity sensitive dyes(63).

![](images/08ed1757140af05a4435fb31598cd8405914896d15953acbdbb29a062278a09e.jpg)

Figure 3. (Left) TS diagram as an aid to the eye, informed by experiments in artificial lipid films(9, 20). The hypothesized transition region is shaded. The region makes an acute angle with S axis for retrograde materials. Assuming that complete phase change takes place across the wavefront where the system is always in local equilibrium during an impulse, starting at $( T _ { 0 } S _ { 0 } )$ , the process across the wavefront is represented by the isentrope $S = S _ { 0 }$ . The threshold and amplitude scale with ?? ?????? ?? respectively, i.e. the distance between the initial state and the intersection of the isentrope with the phase boundary. Different isobars $p _ { i }$ have been overlaid where $p _ { 3 } > p _ { 2 } > p _ { 1 }$ . (Right) Purely electrochemical component $\delta I _ { 2 9 3 0 _ { V } } ( t ) ( b l u e$ curve) estimated from voltage clamp experiments (from fig.1), is overlaid on calculated heat corrected curve $\delta I _ { 2 9 3 0 }$ (??)ℎ?????? ??????????????????, and measured $\delta I _ { 2 9 3 0 }$ (??) (from fig.2)

Finally, a brief comment on the nature of fluctuations during the process which relates to channel activity during an action potential. Here, $\Delta I _ { 2 9 3 0 }$ represents first-order changes in the state during an action potential. However, fluctuations represent second-order changes, which have been proposed as the basis for the regulation of channels current (64–67) in the thermodynamic approach and can be accessed by measuring the second order changes $\Delta \Delta I _ { 2 9 3 0 }$ , e.g. by resolving changes in the width of the peak(31). The relation between fluctuation and temperature includes a material constant (see eq. (2) and eq. (3)), like heat capacity or compressibility (in general known as thermodynamic susceptibilities). Usually, susceptibilities are taken to be "constants" and fluctuations are assumed to be a function of temperature alone. However, the assumption breaks down near a phase transition where heat capacity and compressibility of the membrane have large peaks(21). As the membrane freezes, it goes through this intermediate peak in susceptibility (metastable states), which will increase fluctuations that should cause a spike in channel currents. Such transitions have also been referred as pseudocritical transitions in lipid membranes. Direct evidence of such a role of channel currents during an action potential remains to be seen.

## Challenges and Limitations

Here we have provided a thermodynamic interpretation of the changes in the phenomenological Raman intensities as a function of the state of the entire system.However, unveiling the material basis of these changes beyond the abstract lipid-protein protomers as hypothesised by Changeux et.al. (46) is challenging. The observed region of the spectrum (fig.1c) is dominated by the protein band at $2 9 3 0 c m ^ { - 1 }$ , which obfuscates information specific to lipid band at $2 8 5 0 c m ^ { - 1 }$ .(68) The interpretation in terms of thermotropic transition is mainly based on the Fermi resonance component of the chain terminal methyl C-H symmetric stretching mode. This is a known challenge that will requires characterising other regions, in particular, 1000 to $1 2 0 0 c m ^ { - 1 }$ region related to C-C skeletal stretching. However, this band may present other challenges, for example, the presence of strong resonance Raman bands of the carotenoid pigment.(48) Furthermore, the observed protein signal can be from both the membrane and the axo-plasm that lie within the optical focal spot. Here, it has been assumed based on the timescales, that the changes in the spectra during an action potential arise mainly from components in the plasma membrane that are directly involved in the excitation process. This assumption is consistent with the source of optical changes in nerve fibres, in general, which have been shown to lie within or close to the surface of the membrane and not in the axoplasm(69).

The quantitative assumptions made in above interpretation also underline the limitations of this study. The co-efficient $\left( { \frac { \partial I _ { n } } { \partial T } } \right)$ was estimated based on measurements in rat sciatic nerve and unmyelinated garfish olfactory nerve, assuming that it holds generally(49). However, ideally it needs to be measured within the same sample. Furthermore, we assumed that changing the temperature and the voltage of the clamp affect the same system as propagating action potential, and that local equilibrium can be assumed. These assumptions can been justified considering the objective was to estimate orders of magnitude of the enthalpy changes, which were tested against the condition $0 < \beta < 1$ . Also the same assumption is implicit when extrapolating coefficients of voltage clamp measurements to propagating action potentials in electrophysiology.

The nature of the observed thermotropic transition also needs to be firmly established to understand its material basis. Observing several other region of the spectra over a wider range of temperature and voltages, as well as other variables, such as pH and pressure, will be required to reveal the nonlinearities associated with the claimed thermotropic transition. Furthermore, a definite proof of phase transition during the action potential based on Raman spectra would also require observing time resolved changes in the shape of the spectra. Direct measurement of the changes in the width of the spectra can confirm the extent of phase change during the action potential. However, considering that even in pure lipid membrane, typical shifts in the spectra are of the order of $1 c m ^ { - 1 }$ , its presents a formidable technological challenge. There are other fundamental aspects of the phase transition as well that require further investigations. For example, phase boundaries appear as single points in single component systems when observed as a function of a single variable, but in multicomponent system phase-boundaries exist as hypersurfaces and it is important to approach these boundaries using multiple variables for a complete understanding(70–72). For example, using solvato-chromic dyes it was recently show that in Chara Alga, the state of the membrane may change in strongly nonlinear manner as function of pH even though it changes linearly as a function of temperature (73). Relative changes in $2 9 3 0 c m ^ { - 1 }$ band, both with respect to the temperature and voltage, have been found to change linearly in neurons over the limited range they have been tested. However, observed change in $1 2 9 3 0 c m ^ { - 1 }$ band are found to be significant based on the corresponding changes observed during transitions in a range of lipids, fatty acids(74), proteins(43), and membrane systems(42).

Finally, going back to the burning fuse analogy of action potential, the material in general expands during such a process where as this study shows a reversible compression (and a thermotropic condensation), making it highly unlikely that wave front propagation does not involve momentum transfer(75). However, answering that question completely will require systematic investigation of the entire phenomenon as a function of thermodynamic state (76). Most important would be to show the dependence of conduction velocity on a thermodynamic susceptibility. The Raman spectra as shown here provides access to a multi-dimensional internal state observable of the system, which will be critical for testing the hypothesis. Thermodynamics lays down strict conditions for supersonic or sonic vs subsonic propagation and thus provide a critical test for acoustic vs ionic hypothesis. While sonic or supersonic propagation requires a compression of the material across the wavefront; a subsonic propagation, as in ionic hypothesis, is only allowed under expansion across the wavefront(10). Therefore, the present observations are consistent with the acoustic hypothesis.

In conclusion, SRS measurements for the first time provide direct access to conformational changes in the membrane of a single neuron during an action potential. Therefore, it is now possible to test various predictions of the acoustic hypothesis regarding the role of the thermodynamic state of the membrane in the action potential phenomenon(1, 12, 16, 77, 78). In this study, we showed that the observations so far are consistent with these predictions, however as the technology improves, direct observation of changes in the width and peak positions during an action potential will allow further validation of the hypothesis. These observations will provide further validation of the cooperativity of the observed changes. While the nature of transition across the wave-front remains to be confirmed, the observations strongly suggest a compression and increase in order across the wavefront. Given that a compressive wave-front can propagate either at sonic or supersonic speeds, the observation supports the acoustic hypothesis(79). The observed changes are consistent with the behaviour of two-dimensional compression waves recently observed in artificial lipid films(24). At least in the case of artificial lipid films, the characteristics emerge naturally from the underlying thermodynamic state changes. Now, SRS provides a powerful technique with the spatiotemporal resolution required to investigate action potentials in single neurons as a thermodynamic phenomenon (1, 16, 19, 24).

## References

1. Tasaki, I. 1982. Physiology and electrochemistry of nerve fibers. .  
2. Hodgkin, A.L., and A.F. Huxley. 1952. A quantitative description of membrane current and its application to conduction and excitation in nerve. J. Physiol. 117:500–544.  
3. Tasaki, I. 1995. Mechanical and thermal changes in the Torpedo electric organ associated with its postsynaptic potentials. Biochem. Biophys. Res. Commun. 215:654–658.  
4. Cohen, L.B., B. Hille, and R.D. Keynes. 1969. Light scattering and birefringence changes during activity in the electric organ of Electrophorus electricus. J. Physiol. 203:489–509.  
5. Conti, F., and I. Tasaki. 1970. Changes in extrinsic fluorescence in squid axons during voltage clamp. Science (80-. ). 169:1322–1324.  
6. Barry, J.F., M.J. Turner, J.M. Schloss, D.R. Glenn, Y. Song, M.D. Lukin, H. Park, and R.L. Walsworth. 2016. Optical magnetic detection of single-neuron action potentials using quantum defects in diamond. Proc. Natl. Acad. Sci. 113:14133–14138.  
7. Howarth, J. V, and R.D. Keynes. 1975. The heat production associated with the passage of a single impulse in pike olfactory nerve fibres. J. Physiol. 249:349–368.  
8. El Hady, A., and B.B. Machta. 2015. Mechanical surface waves accompany action potential propagation. Nat. Commun. 6:6697.  
9. Shrivastava, S. 2018. Detonation of shock-waves and action potentials in lipid interfaces. In: Proceedings of Meetings on Acoustics. .  
10. Landau, L.D., and E.M. Lifshitz. 1987. Shock Waves. In: Sykes J, W Reid, editors. Fluid Mechanics. Pergamon Press Ltd. pp. 327–329.  
11. Hodgkin, A.L. 1964. The conduction of the nervous impulse. VII. Liverpool: Liverpool University Press.  
12. Margineanu, D.-G., and E. Schoffeniels. 1977. Molecular events and energy changes during the action potential. Proc Natl Acad Sci U S A. 74:3810–3813.  
13. de Lichtervelde, A.C.L., J.P. de Souza, and M.Z. Bazant. 2019. The Heat of Nervous  
Conduction: A Thermodynamic Framework. .  
14. Fichtl, B., S. Shrivastava, and M.F. Schneider. 2016. Protons at the speed of sound: Predicting specific biological signaling from physics. Sci. Rep. 6.  
15. Howarth, J. V., J.M. Ritchie, and D. Stagg. 1979. The initial heat production in garfish olfactory nerve fibres. Proc. R. Soc. London - Biol. Sci. 205:347–367.  
16. Kaufmann, K. 1989. Action Potentials and Electrochemical Coupling in the Macroscopic Chiral Phospholipid Membrane. Caruara, Brazil (https://sites.google.com/site/schneiderslab/research-group/literature).  
17. Fox, D. 2018. The Brain, Reimagined. Sci. Am. 318:60–67.  
18. Shrivastava, S. 2014. Non-Linear Solitary Sound Waves in Lipid Membranes and Their Possible Role in Biological Signaling. Boston, Massachussets, USA: Thesis and Disertation Collection 3917.  
19. Heimburg, T., and A.D. Jackson. 2005. On soliton propagation in biomembranes and nerves. Proc. Natl. Acad. Sci. U. S. A. 102:9790–9795.  
20. Shrivastava, S., K. Kang, and M.F. Schneider. 2015. Solitary Shock Waves and Adiabatic Phase Transitions Lipid Interfaces and Nerves. Phys. Rev. E. 91:12715.  
21. Mužić, T., F. Tounsi, S.B. Madsen, D. Pollakowski, M. Konrad, and T. Heimburg. 2019. Melting transitions in biomembranes. Biochim. Biophys. Acta - Biomembr. 1861:183026.  
22. Melchior, D.L., and J.M. Steim. 1976. Thermotropic transitions in biomembranes. Annu. Rev. Biophys. Bioeng. 5:205–238.  
23. Albrecht, O., and H. Gruler. 1978. Polymorphism of phospholipid monolayers. J. Phys. 39:301–324.  
24. Shrivastava, S., and M.F. Schneider. 2014. Evidence for two-dimensional solitary sound waves in a lipid controlled interface and its implications for biological signalling. J. R. Soc. Interface. 11:1–23.  
25. Shrivastava, S., K.H. Kang, and M.F. Schneider. 2018. Collision and annihilation of nonlinear sound waves and action potentials in interfaces. J. R. Soc. Interface. 15.  
26. Kappler, J., S. Shrivastava, M.F. Schneider, and R.R. Netz. 2017. Nonlinear fractional waves at elastic interfaces. Phys. Rev. Fluids.  
27. Cohen, L.B., and B.M. Salzberg. 1978. Optical measurement of membrane potential. Rev. Physiol. Biochem. Pharmacol. 83:35–88.  
28. Einstein, A. 1909. On the Present Status of the Problem of Radiation. Ann. Phys. 10:183–195.  
29. Einstein, A. 1910. Theory of the Opalescence of homogenous fluids and liquid mixtures near the critical state. Ann. Phys. 33:1275–1295.  
30. Shrivastava, S., and M.F. Schneider. 2013. Opto-Mechanical Coupling in Interfaces under Static and Propagative Conditions and Its Biological Implications. PLoS One. 8:2005–2007.  
31. Shrivastava, S., R.O. Cleveland, and M.F. Schneider. 2018. On measuring the acoustic state changes in lipid membranes using fluorescent probes. Soft Matter.  
32. Raman, C. V. 1928. Nature 121 (March 31, 1928) 501-502 - A new type of scecondary radiation.pdf. Nature. 501–502.  
33. Schultz, Z.D., and I.W. Levin. 2011. Vibrational spectroscopy of biomembranes. Annu. Rev. Anal. Chem. (Palo Alto. Calif). 4:343–366.  
34. Hazel, J.R., S.J. McKinley, and M.F. Gerrits. 1998. Thermal acclimation of phase behavior in plasma membrane lipids of rainbow trout hepatocytes. Am. J. Physiol. - Regul. Integr. Comp. Physiol. 275:861–869.  
35. Gaber, B.P., P. Yager, and W.L. Peticolas. 1978. Interpretation of biomembrane structure by Raman difference spectroscopy. Nature of the endothermic transitions in phosphatidylcholines. Biophys. J. 21:161–176.  
36. Kaufmann, K. 1989. On the role of the phospholipid membrane in free energy coupling. Caruaru, Brazil https://sites.google.com/site/schneiderslab/research-group/literature.  
37. Landau, L.D., and E.M. Lifshitz. 1980. Fluctuations of the fundamental thermodynamic quantities. In: Statistical Physics. Burlington,MA: Butterworth-Heinemann. p. 338.  
38. Landau, L.D., and E.M. Lifshitz. 1980. Entropy for Nonequilibrium. In: Statistical Physics. Burlington,MA: Butterworth-Heinemann. pp. 26–27.  
39. Shrivastava, S., R.O. Cleveland, and M.F. Schneider. 2018. On measuring the acoustic state changes in lipid membranes using fluorescent probes. Soft Matter.  
40. Lee, H.J., D. Zhang, Y. Jiang, X. Wu, P.Y. Shih, C.S. Liao, B. Bungart, X.M. Xu, R. Drenan, E. Bartlett, and J.X. Cheng. 2017. Label-Free Vibrational Spectroscopic Imaging of Neuronal Membrane Potential. J. Phys. Chem. Lett. 8:1932–1936.  
41. Gaber, B.P., P. Yager, and W.L. Peticolas. 1978. Interpretation of biomembrane structure by Raman difference spectroscopy. Nature of the endothermic transitions in phosphatidylcholines. Biophys. J. 21:161–176.  
42. Verma, S.P., and D.F.H. Wallach. 1976. Erythrocyte membranes undergo cooperative, pH sensitive state transitions in the physiological temperature range: Evidence from Raman spectroscopy. Proc. Natl. Acad. Sci. U. S. A. 73:3558–3561.  
43. Verma, S.P., and D.F.H. Wallach. 1977. Changes of Raman scattering in the CH-stretching region during thermally induced unfolding of ribonuclease. Biochem. Biophys. Res. Commun. 74:473–479.  
44. Levin, I.W., E. Keihn, and W.C. Harris. 1985. A Raman spectroscopic study on the effect of cholesterol on lipid packing in diether phosphatidylcholine bilayer dispersions. BBA - Biomembr. 820:40–47.  
45. Yager, P., and W.L. Peticolas. 1982. The kinetics of the main phase transition of aqueous dispersions of phospholipids induced by pressure jump and monitored by raman spectroscopy. BBA - Biomembr. 688:775–785.  
46. Changeux, J.-P., J. Thiery, Y. Tung, and C. Kittel. 1967. ON THE COOPERATIVITY OF BIOLOGICAL MEMBRANES. Proc. Natl. Acad. Sci. 57:335–341.  
47. Fox, C.B., G.A. Myers, and J.M. Harris. Temperature-Controlled Confocal Raman Microscopy to Detect Phase Transitions in Phospholipid Vesicles. .  
48. Savoie, R., M. Pigeon-Gosselin, M. Pézolet, and D. Georgescauld. 1986. Effect of the action potential on the Raman spectrum of the pike olfactory nerve. Biochim. Biophys. Acta - Biomembr. 854:329–333.  
49. Pézolet, M., and D. Georgescauld. 1985. Raman spectroscopy of nerve fibers. A study of membrane lipids under steady state conditions. Biophys. J. 47:367–372.  
50. Holzwarth, J. 1989. Structure and dynamic of phospholipid membranes from nanoseconds to seconds. In: Cooper A, J Houben, L Chien, editors. The Enzyme Catalysis Process Energetics, Mechanism and Dynamics. New York: Springer Science + Buisness Media, LLC. pp. 383– 410.  
51. Yellin, N., and I.W. Levin. 1977. Cooperative unit size in the gel-liquid crytalline phase transition of dipalmitoyl phosphatidylcholine-water multilayers: An estimate from raman spectroscopy. BBA - Biomembr. 468:490–494.  
52. Ramos, A., B. Maté, G. Tejeda, J.M. Fernández, and S. Montero. 2000. Raman spectroscopy of hypersonic shock waves. Phys. Rev. E. 62:4940–4945.  
53. Nagao, H., A. Matsuda, K.G. Nakamura, and K. Kondo. 2003. Nanosecond time-resolved Raman spectroscopy on phase transition of polytetrafluoroethylene under laser-driven shock compression. Appl. Phys. Lett. 83:249–250.  
54. and, J.M.W., and Y.M. Gupta\*. 1997. Shock-Induced Chemical Changes in Neat Nitromethane:  Use of Time-Resolved Raman Spectroscopy. .  
55. Lifshitz, L.D.L. and E.M. 1987. Second Viscosity. In: Sykes J, W Reid, editors. Fluid Mechanics. Pergamon Press Ltd. p. 308.  
56. Bethe, H.A. 1998. On the Theory of Shock Waves for an Arbitrary Equation of State. In: Johnson JN, R Cheret, editors. Classic Papers in Shock Compression Science. Springer New York. pp. 421–495.  
57. Kim, Y.G., G.C. Carofano, and P. a. Thompson. 1986. Shock waves and phase changes in a large-heat-capacity fluid emerging from a tube. J. Fluid Mech. 166:57–92.  
58. Thompson, P.A., and Y.G. Kim. 1983. Direct observation of shock splitting in a vapor-liquid system. Phys. Fluids. 26:3211–3215.  
59. Cohen, L.B., and B.M. Salzberg. 1978. Optical measurement of membrane potential. Rev. Physiol. Biochem. Pharmacol. 83:35–88.  
60. Sherebrin, M.H., B.A.E. MacClement, and A.J. Franko. 1972. Electric-Field-Induced Shifts in the Infrared Spectrum of Conducting Nerve Axons. Biophys. J. 12:977–989.  
61. Maksimov, G. V, A.A. Churin, V.Z. Paschenko, and A.B. Rubin. 1990. Raman Spectroscopy of the “Potential Sensor” of Potential-Dependent Channels. .  
62. Tasaki, I., E. Carbone, K. Sisco, and I. Singer. 1973. Spectral analyses of extrinsic fluorescence of the nerve membrane labeled with aminonaphthalene derivatives. BBA - Biomembr. 323:220–233.  
63. Georgescauld, D., and H. Duclohier. 1978. Transient fluorescence signals from pyrene labeled pike nerves during action potential possible implications for membrane fluidity changes. Biochem. Biophys. Res. …. 85:1186–1191.  
64. Micol, V., P. Sánchez-Piñera, J. Villalaín, a de Godos, and J.C. Gómez-Fernández. 1999. Correlation between protein kinase C alpha activity and membrane phase behavior. Biophys. J. 76:916–927.  
65. Seeger, H.M., L. Aldrovandi, A. Alessandrini, and P. Facci. 2010. Changes in single K(+) channel behavior induced by a lipid phase transition. Biophys. J. 99:3675–3683.  
66. Fenimore, P.W., H. Frauenfelder, B.H. McMahon, and F.G. Parak. 2002. Slaving: solvent fluctuations dominate protein dynamics and functions. Proc. Natl. Acad. Sci. U. S. A. 99:16047–16051.  
67. Wunderlich, B., C. Leirer, A. Idzko, U.F. Keyser, A. Wixforth, V.M. Myles, and T. Heimburg. 2009. Phase-State Dependent Current Fluctuations in Pure Lipid Membranes. Biophysj. 96:4592–4597.  
68. Pézolet, M., and D. Georgescauld. 1985. Raman spectroscopy of nerve fibers. A study of membrane lipids under steady state conditions. Biophys. J. 47:367–372.  
69. I, T., W. A, S. R, and C. L. 1968. Changes in Fluorescence, Turbidity, and Birefringence associated with nerve excitation. Proc. Natl. Acad. Sci. U. S. A. 61:883–888.  
70. Tisza, L. 1961. The thermodynamics of phase equilibrium. Ann. Phys. (N. Y). 13:1–92.  
71. Griffiths, R.B., and J.C. Wheeler. 1970. Critical points in multicomponent systems. Phys. Rev. A. 2:1047–1064.  
72. Groves, J.T., S.G. Boxer, and H.M. McConnell. 2000. Electric field effects in multicomponent fluid lipid membranes. J. Phys. Chem. B. 104:119–124.  
73. Fabiunke, S., C. Fillafer, A. Paeger, and M.F. Schneider. 2020. Optical Studies of Membrane State during Action Potential Propagation. Prog. Biophys. Mol. Biol. Accepted.  
74. Verma, S.P., and D.F.H. Wallach. 1977. Raman spectra of some saturated, unsaturated and deuterated C18 fatty acids in the HCH-deformation and CH-stretching regions. Biochim. Biophys. Acta (BBA)/Lipids Lipid Metab. 486:217–227.  
75. Von Neuman, J. 1942. Theory of Detonation Waves. In: Technical Report OSRD No. 549. .  
76. Fillafer, C., A. Paeger, and M.F. Schneider. 2019. The living state: how cellular excitability is controlled by the thermodynamic state of the membrane. .  
77. Kobatake, Y., I. Tasaki, and A. Watanabe. 1971. Phase transition in membrane with reference to nerve excitation. Adv. Biophys. 2:1–31.  
78. Inoue, I., Y. Kobatake, and I. Tasaki. 1973. Excitability, instability and phase transitions in squid axon membrane under internal perfusion with dilute salt solutions. BBA - Biomembr. 307:471–477.  
79. Zeldovich, Y.B. 1950. On the theory of the propagation of detonation in gaseous systems. Z. Exsperim. Theor. Fiz. 20:175–182.