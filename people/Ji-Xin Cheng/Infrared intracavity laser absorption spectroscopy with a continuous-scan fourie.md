# Infrared intracavity laser absorption spectroscopy with a continuous-scan Fourier-transform interferometer

Jixin Cheng, Hai Lin, Shuiming Hu, Shenggui He, Qingshi Zhu, and Alexander Kachanov

High-quality broadband infrared high-resolution spectra were obtained by use of the intracavity laser absorption spectroscopy technique with a Ti:sapphire laser in combination with a continuous-scan Fourier-transform \~FT! interferometer. With electronic filtering used to smooth out the fluctuations of the laser power, the absorption of atmospheric water vapor in the range of 12,450–12,700 cm21 was recorded at a resolution of 0.05 cm21 . A signal-to-noise ratio of greater than 300 was observed in this spectrum, corresponding to a minimum detectable absorption of approximately $2 \times 1 0 ^ { - 9 } \mathrm { c m } ^ { - 1 } .$ . Comparison with previous measurements by use of a conventional FT technique shows that this method gives absorption spectra with highly accurate line positions along with reasonable line intensities. Investigation of the evolution of intracavity laser absorption spectra with the generation time is also shown to be possible with a continuous-scan FT spectrometer by use of the interleave rapid-scan method. © 2000 Optical Society of America

OCIS codes: 140.3590, 300.6300, 300.6360, 300.6320, 300.6500.

## 1. Introduction

Intracavity laser absorption spectroscopy \~ICLAS! has been widely used for ultrasensitive measurements of weak absorption spectra since its introduction in the early 1970’s.1–3 The main idea is to place a sample cell inside the cavity of a broadband laser. In this case the sample absorption is significantly enhanced. The reason for this enhancement can be understood when we consider, in terms of rate equations, the transient dynamics of the laser mode intensities starting from the initial buildup, as explained in Refs. 4 and 5 and references therein. The resulting spectrum appears as absorption lines superimposed on the envelope of the broadband laser emission. Quantitative measurements of absorption spectra in ICLAS are based on the following equation, which describes the time evolution of the broadband laser intensity $I ( \nu _ { q } , t _ { g } )$ as a function of the frequency $\nu _ { q }$ of the qth lasing mode and the generation time $t _ { g } ^ { ^ { \star } } .$ The generation time is the interval elapsed from the instant when the gain in the cavity exceeds intracavity losses to the moment when the spectrum is observed. The evolution can be written in the following form5,6:

$$
\begin{array}{l} I (\nu_ {q}, t _ {g}) = I (t) \biggl (\frac {\gamma t _ {g}}{\pi \Gamma^ {2}} \biggr) ^ {1 / 2} \exp \biggl [ - \frac {(\nu_ {q} - \nu_ {o}) ^ {2}}{\Gamma^ {2}} \gamma t _ {g} \biggr ] \\ \times \exp [ - \alpha (\nu_ {q}) c t _ {g} ]. \tag {1} \\ \end{array}
$$

The first three terms in Eq. \~1! describe the properties of the laser, with $\gamma$ being the inverse photon lifetime in the cavity; $\nu _ { 0 }$ the gain center frequency; G the gain bandwidth; and $I ( t )$ the integrated laser intensity, which is generally time dependent. The final exponential term in Eq. \~1! describes the intracavity absorption in the form of the Beer–Lambert law with the sample absorption coefficient of $\alpha ( \nu _ { q } )$ and an equivalent absorption length of $c t _ { g } ,$ where c is the velocity of light. When an absorption cell of length l is placed in the cavity of length $L ,$ the equivalent optical path length should be expressed as $c t _ { \underline { { \sigma } } } ( l / L )$ instead of $c t _ { g } .$ For dye lasers the validity of $\operatorname { E q }$ . \~1! has been thoroughly checked by comparison of theoretical and experimental profiles and intensities of $\mathrm { O _ { 2 } }$ absorption lines.7,8 These measurements have demonstrated that the intensities and the line shapes can be measured by ICLAS with an uncertainty of less than 5%, if the apparatus function effects are carefully taken into account. For the Ti:sapphire laser first used for ICLAS by Gilmore et $a l . ^ { \mathrm { ~ 9 ~ } }$ Eq. \~1! has been verified up to a generation time of 3 ms.10 In a recent paper by Kalmar and O’Brien11 with a Ti: sapphire laser, accurate quantitative data have been obtained by use of the intracavity absorption technique.

Currently a state-of-the-art ICLAS system uses a CCD array to record the spectrum in the visible andyor the near infrared range, where highperformance silicon linear diode arrays are available. These arrays usually have 1000–4000 individual photosensitive elements \~pixels!, and therefore in one high-resolution measurement they can acquire only a small segment $( \sim 1 0 \mathrm { c m } ^ { - 1 } )$ of an absorption band several hundred wave numbers wide. In the near- and the mid-infrared range, there exist a large variety of broadband laser media \~such as color center lasers! for ICLAS. However, high-performance optical multichannel detectors with large numbers of pixels, such as silicon diode arrays, cannot be used at wavelengths greater than 1.1 mm. An InGaAs infrared array that can be used in the range as great as 2.2 mm contains only a small number of elements \~usually less than 600!. In such cases recording of a highresolution spectrum over a broad range might become time consuming.

The application of ICLAS to the infrared range can be made significantly easier with Fourier-transform \~FT! spectroscopy. These two methods can benefit from each other. With a FT spectrometer the interferogram of the entire broadband laser spectrum can be recorded by use of conventional infrared detectors at wavelengths that are inaccessible with linear CCD arrays and then be converted into the absorption spectra. In the currently used ICLAS system all the obtained spectral segments have to be individually calibrated in wave number with reference spectral lines recorded in the same experiment, and it is often difficult to find a suitable wavelength reference for every small segment recorded. However, the spectra in FT experiments are already calibrated in wave numbers. The sensitivity of a conventional FT spectrometer is rather good, in particular when multipass cells are used. However, with a multipass cell it is difficult to obtain an effective absorption path length longer than 1 km. ICLAS offers an equivalent path length as long as several hundred kilometers, or even more. This is one more reason why the combination of these two methods looks quite promising, especially if commercially available high-resolution FT spectrometers could be used.

Following from Eq. \~1!, ICLAS requires recording of time-resolved transient laser spectra, which should be synchronized with the sampling of the interferogram. The feasibility of FT-ICLAS has already been demonstrated by del Olmo et al.12,13 By combining a dye laser intracavity absorption system and a continuous-scan FT spectrometer, these authors recorded the $B  X$ transitions12 of $\mathrm { C l } _ { 2 }$ and the $6 \nu _ { 1 }$ band13 of $\mathrm { C H D } _ { 3 } .$ In these studies the interferogram of the He–Ne reference laser of the FT instrument was converted into a square wave and provided the clock for sampling the interferogram of the dye laser. The trigger signal for the electro-optical modulator was used to interrupt the pump, with a delay required for determining the generation time. The most natural way to perform time-resolved spectroscopy with a FT interferometer is to use a step-scan device. With this method a time-resolved interferogram can be recorded for fixed values of the optical path difference \~OPD! in the interferometer, providing a time-resolved spectrum, as was done recently by Strong et $a l . ^ { 1 4 }$ They demonstrated the ability of a step-scan FT spectrometer to measure time-resolved intracavity absorption spectra of a dye laser. Since a step-scan device can stay at any OPD for an arbitrarily long time, the averaging of multiple spectra is possible in a single scan.

These demonstrations of FT-ICLAS have been done with dye lasers working in the visible range, whereas molecular vibrational absorption lies largely in the near- and the mid-infrared range. Moreover, with the narrow-bandwidth dye lasers used in these experiments, it was impossible to take advantage of the capability of FT spectrometers to record broadband spectra in a single experiment. In addition, despite the extensive use of step-scan interferometers in time-resolved FT spectroscopy,15 the majority of commercial FT spectrometers are continuously scanning instruments. It is therefore important to demonstrate that spectroscopic data of high quality can be obtained with ICLAS in the infrared range with conventional continuously scanning instruments.

In this study we combined a broadband Ti:sapphire intracavity laser absorption system with a Bruker Model IFS 120HR FT spectrometer. A Ti:sapphire laser has spectrotemporal properties similar to those of other solid-state lasers working at longer wavelengths, such as a chromium-doped forsterite $\left( \mathrm { C r ^ { 4 + } } \right)$ : $\mathrm { M g } _ { 2 } \mathrm { S i O } _ { 4 } )$ laser16 \~1.167–1.345 mm!, a $\mathrm { C r ^ { 4 + } { : } Y A G }$ laser17 \~1.38–1.55mm!, or a $\mathrm { C o 2 M g F _ { 2 } }$ laser18,19 \~1.75– 2.5 mm!. Our results therefore provide a good evaluation of the performance that can be achieved with ICLAS systems based on these materials as well as with other FT spectrometers.

The paper is organized as follows. In Section 2 we discuss the expected performance of the FT-ICLAS technique. Section 3 gives a detailed description of the continuous-scan FT-ICLAS setup. In Section 4 we examine the performance of our FT-ICLAS apparatus, using the absorption spectra of atmospheric water vapor recorded in the range of 12,450–12,700 $\mathrm { c m } ^ { - 1 }$ . Finally, the results are summarized in Section 5.

## 2. Quantum Noise in Fourier-Transform Intracavity Laser Absorption Spectroscopy

In FT experiments dealing with rapidly changing spectra it is generally required that the process under study be repetitive and reproducible. In this case if the process is initiated at each sampling point, and if the sampling \~or multiple sampling! is performed with appropriate delays, then a Fourier transformation of the interferograms would give a set of timeresolved spectra as if they were spectra of a stable source.

A specific feature of ICLAS is that the spectra are not reproducible in a strict sense. In a multimode laser used in ICLAS, each time the pump is switched on, different modes receive a seed from spontaneous photons at different moments during the initial stage of the spectral evolution. Each seeded mode then builds up exponentially until the total laser intensity reaches the stationary state. The photon distribution in the modes constitutes the quantum noise \~or seeding noise!. For the description of the laser noise it is convenient to express the mode intensities in terms of photon number $M _ { q } ( t _ { g } )$ in the mode q by substitution $I ( \nu _ { q } , t _ { g } )  M _ { q } ( t _ { g } ) ^ { 7 }$ in Eq. \~1!. The noise properties of broadband lasers used in ICLAS have been analyzed in Refs. 20–22. According to this analysis, the spectral evolution follows Eq. \~1!, but $M _ { q } ( t _ { g } )$ should be understood as a mathematical expectancy for individual mode intensities. The noise value can be calculated from the probability $P _ { q } ( m _ { q } , t _ { g } )$ of having $m _ { q }$ photons in the mode q at a generation time $t _ { g } ,$

$$
P _ {q} (m _ {q}, t _ {g}) = \frac {1}{M _ {q} (t _ {g})} \exp [ - m _ {q} / M _ {q} (t _ {g}) ]. \tag {2}
$$

The variance of the above exponential probability distribution is $[ M _ { q } ( t _ { g } ) ] ^ { 2 }$ , which means that the noise of any mode is as large as the intensity of this mode. This quantum noise has been observed experimentally,23,24 and a quantitative agreement with the distribution @cf. Eq. \~2!# has been obtained.24 To reduce the quantum noise, a large number of statistically independent laser pulses are averaged in conventional ICLAS. The remaining noise sets a physical limit on the minimum detectable absorption at a given generation time. A detection threshold equal to 10210 $1 0 ^ { - 1 0 } \mathrm { c m } ^ { - 1 }$ limited by the quantum noise has been reached.24

In FT-ICLAS the detected signal $J ( \Delta , t _ { g } )$ , as a function of OPD in the interferometer and of the generation time, is the sum of the intensities resulting from two-beam interference of all the laser modes,

$$
J (\Delta , t _ {g}) = \sum_ {q} M _ {q} (t _ {g}) \frac {1 + \cos (2 \pi \nu_ {q} \Delta)}{2}. \tag {3}
$$

The variance of $J ( \Delta , t _ { g } )$ can be calculated as a sum of the variance of each mode multiplied by the square of its coefficient. We can obtain the expression for the variance of the interferogram,

$$
\sigma_ {J (\Delta , t _ {g})} ^ {2} = \sum_ {q} \left[ M _ {q} (t _ {g}) \frac {1 + \cos (2 \pi \nu_ {q} \Delta)}{2} \right] ^ {2}. \tag {4}
$$

For a simple estimation of the noise in the interferogram we assume that the laser pulse has a rectangular spectral profile and that there is no absorption of the sample so that all the modes have the same intensity of $M _ { 0 } .$ The amplitude of the noise can be estimated from the variance of the interferogram at the large OPD values. The variance is related to the number of modes, N, by

$$
\begin{array}{l} \sigma_ {J (\Delta)} ^ {2} = M _ {0} ^ {2} \sum_ {q = 1} ^ {N} \left[ \frac {1 + \cos (2 \pi \nu_ {q} \Delta)}{2} \right] ^ {2}, \\ = M _ {0} ^ {2} \sum_ {q = 1} ^ {N} \frac {3 + 4 \cos (2 \pi \nu_ {q} \Delta) + \cos (4 \pi \nu_ {q} \Delta)}{8} \\ = M _ {0} ^ {2} \frac {3}{8} N. \tag {5} \\ \end{array}
$$

For a laser bandwidth of $1 0 0 \mathrm { c m } ^ { - 1 }$ corresponding to $t _ { g }$ $= 7 0$ ms and a cavity length of 100 cm, the number of lasing modes is $N = 2 \times 1 0 ^ { 4 }$ . The peak value of the interferogram is $M _ { 0 }$ at zero OPD. The corresponding ratio of the standard deviation @cf. Eq. \~5!# to the peak value is $[ 3 / ( 8 \mathrm { N } ) ] ^ { 1 / 2 } \simeq 4 \times \bar { 1 0 } ^ { - 3 }$ . We can see that the ratio of noise to signal in the interferogram is less than 1% and is inversely proportional to the square root of the number of lasing modes. Even though the mode distributions in the laser spectra for two subsequent sampling points of the interferogram are 100% different, the noise in the interferogram can be rather small, owing to the summation of all mode intensities. This is a manifestation of the multiplex advantage25 of FT spectroscopy in FT-ICLAS.

In a general case in which the spectral envelope is described by Eq. \~1!, it is difficult to give an analytical expression for the noise evaluation. A numerical evaluation according to Eq. \~4! was carried out for any given generation time with Eq. \~1! for the mathematical expectancy $M _ { q } ( t _ { g } )$ . With $t g = 7 0 ~ \mu \mathbf { s }$ , the numerical result for the ratio of noise to signal is 3.9 3 1023 , $3 . 9 \times 1 0 ^ { - 3 }$ which is very close to our simple example calculation. Because every point of the interferogram is the sum of many statistically independent mode intensities, we can expect the noise in the interferogram to have a normal probability distribution and to be weakly dependent on OPD. The inverse Fourier transformation that transfers the interferogram into the absorption spectrum is linear. It can be expected, therefore, that the interferogram noise originating from quantum fluctuations in the laser would result in white noise in the final spectrum. According to Eq. \~1! the width of the Gaussian spectrum envelope and thus the effective number of the lasing modes decreases proportionally to $\sqrt { t _ { g } } .$ Then the noise in the interferogram will increase to $t _ { g } ^ { ~ 1 / 4 }$ g . Meanwhile, the absorption line depth of the intracavity species increases proportionally to $t _ { g } ;$ therefore the ratio of spectral signal to quantum noise will increase to tg3y4 . $t _ { g } ^ { 3 / 4 }$ We can thus expect that the effect of the quantum noise of a broadband laser can be significantly decreased and that reasonable intracavity absorption spectra can be obtained with the FT method, provided that the total laser intensity is stable.

![](images/6bdce87bf109eaadebce8705480a2a3c4429b7f2dba29044411a309a0d7955f2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    PC2["PC2"] <--> Grating_spectrometer["Grating spectrometer"]
  AOM["AOM"] --> FM2["FM2"]
  FM2 --> Ti_sapphire["Ti-sapphire"]
  Ti_sapphire --> Cell["Cell"]
  Cell --> FM1["FM1"]
  FM1 --> OC["OC"]
  OC --> BeamSplitter["Beam splitter"]
  BeamSplitter --> IFS_120HR["IFS 120HR"]
  IFS_120HR --> Scanning_S_modulation_signal["Scanning modulation signal"]
  ScanningSModulationSignal["Scanning_S modulation_signal"] --> Pulse_Generator["Pulse generator"]
    PC1["PC1"] <--> Scanning_S modulation_signal
  ScanningSModulationSignal --> IFS_120HR
  IFS_120HR --> FM1
  FM1 --> P1["P1"]
  FM1 --> P2["P2"]
  FM1 --> HR["HR"]
  Air_Laser["Ar+ Laser"] --> FM2
  Cell --> FM1
```
</details>

Fig. 1. Schematic of the FT-ICLAS installation. FM, folding mirror; OC, output coupler; HR, high-reflection mirror; P, prism; PC, personal computer. The thin and the thick lines represent the laser beam and the electronic signals, respectively. The doubled lines denote the cables connecting the spectrometers and the computers.

## 3. Experiment

Figure 1 depicts the FT-ICLAS setup and the experimental configuration developed recently in our laboratory. A Bruker Model IFS 120HR FT spectrometer is used to record the intracavity absorption spectrum. A Ti:sapphire laser is pumped by a Coherent Innova Model 400 argon-ion laser. A sample cell is placed inside the Ti:sapphire standingwave cavity. As in the conventional ICLAS, the pump laser is chopped by an acousto-optic modulator \~AOM!.26 The broadband laser emission is focused into the emission port of the FT spectrometer. For convenience of the cavity alignment \~to avoid fringes, etc.!, a part of the Ti:sapphire laser output beam is split into a high-resolution multipass grating spectrometer equipped with a CCD of 1024 pixels \~both the grating spectrometer and the CCD camera were made by Science Solutions Inc., San Diego, California!. The data acquisition and the rotation of the grating are controlled by a personal computer. From the screen the spectral quality can be monitored with time, and optical adjustment can be easily carried out. In particular, we found that the laser radiation reflected from the moving mirror in the interferometer has no effect on either the Ti:sapphire laser power or the spectrum. Preliminary results obtained previously with this setup have been described in Ref. 27.

![](images/b970c11e68bf7f3165545b087b7fc077f731f66dcb0db9ae1ad9b01da7fe6f95.jpg)

<details>
<summary>line chart</summary>

| Time (ms) | Scanning modulation signal | Generator output | Laser emission | Sampling pulse |
|-----------|-----------------------------|------------------|----------------|----------------|
| 0.5       | High                        | Low              | Low            | Low            |
| 0.6       | High                        | Low              | Low            | Low            |
| 0.7       | High                        | Low              | Low            | Low            |
| 0.8       | High                        | Low              | Low            | Low            |
| 0.9       | High                        | Low              | Low            | Low            |
| 1.0       | High                        | Low              | Low            | Low            |
| 1.1       | High                        | Low              | Low            | Low            |
</details>

Fig. 2. Diagram showing the synchronization between triggering and sampling. The generation time $t _ { g }$ is measured as the sampling delay with respect to the scanning modulation signal. The laser emission signal was recorded by a digital oscilloscope.

Figure 2 shows the triggering scheme. The rectified fringes of the reference He–Ne laser, the socalled scanning modulation signal, is used to realize interferogram sampling at the equidistant points of OPD and at the same generation time of each pulse.13 Rising edges of this signal, which correspond to OPD values that are multiples of the He–Ne laser halfwavelength, are used to trigger a pulse generator. The generator drives the AOM so that the argon-ion laser pumping is switched on at the low value of the generator output. As a result, the multimode laser emission is a width-adjustable pulse. A short delay can be seen between the trigger of the generator and the start of the laser emission. This offset is due to the acoustic wave propagation delay from the piezoactuator of the AOM plus the initial buildup time of the laser radiation in the cavity. The generation time can be controlled by adjustment of the sampling delay in the FT spectrometer or of the pulse generator delay, which determines the start of the broadband laser evolution. In our experiment the delay of the generator with respect to the triggering is set to be zero \~Fig. 2!. As the linear spectral evolution starts during the initial cavity buildup,28 the generation time $t _ { g }$ is measured as the interval between the interferogram sampling pulse and the rising edge of the scanning modulation signal. In our FT spectrometer the integration time of the sample-and-hold device is 1.0 ms, and the uncertainty of the sampling delay time is better than 0.1 ms; therefore a time resolution of 1.0 ms can be achieved.

The control of $t _ { g }$ is realized with the method of interleave rapid-scan time-resolved spectroscopy29 provided by the Bruker Model IFS 120HR FT spectrometer. In this method the spectrometer generates a series \~#16! of equidistant sampling pulses. Both the time interval between the sampling pulses and the delay of the first sampling pulse with respect to the rising edge of the scanning modulation signal are adjustable. The interferograms with variable delays after the laser generation yield a series of spectra, with each corresponding to a certain $t _ { g } .$ It should be pointed out that, in contrast to the situation in a step-scan FT spectrometer,14 these interferograms are sampled at different $\mathrm { O P D ^ { \circ } s } ,$ because in a continuous-scan spectrometer the mirror keeps moving rather than being fixed at the zero-crossing position of the He–Ne laser interference fringes. This effect can however be eliminated by proper phasecorrection methods.30 However, the changing of OPD during the sampling may introduce some distortion in a time-evolving spectrum. In our case the sampling time is $1 . 0 ~ { \mu } { \mathbf { S } } ,$ whereas the sampling interval that equals the period of the laser pulse is not less than 100 ms; thus this effect is negligible. The scanning velocity jitter, though, caused by the external mechanical perturbations, might be an important source of noise andyor artifacts.31 If it is a stationary random Gaussian process, the velocity jitter will result in white noise uniformly distributed across the spectrum.32 A promising method to solve this problem was proposed by Weidner and $\mathrm { P e a l e ^ { 3 3 } }$ in 1997.

As shown in Fig. 2, the power of the broadband laser can have a slow variation from pulse to pulse and rapid irregular small fluctuations within one pulse. The power fluctuations might come from external perturbations to the laser cavity or from the pump power instability. Because the sampled points of the interferogram correspond to different laser pulses, the power instability will introduce extra noise in the spectrum. This noise can be reduced by averaging of the interferograms from multiple scans at the cost of measurement time. Such averaging is performed in our experiment. Another way is the use of the electronic filters in the FT spectrometer to smooth the interferometer output signals. This method is often used in FT experiments when the source has a constant power and spectral distribution. With filters applied, the signal sampled at a certain delay is actually an integrated result. It contains the contributions from the interferograms of the generation spectra in the current pulse and those in the previous pulses. The integrated spectra in conventional ICLAS were used widely34 before the timeresolved method was proposed. In this case, the absorption spectrum is still clearly visible, even though some distortion of line intensities can be introduced. The line intensity of the integrated spectrum can no longer be calculated from the recorded generation time or the equivalent absorption path length. An effective absorption path length should be used instead.

## 4. Results and Discussions

To test the performance of the FT-ICLAS technique, we recorded the absorption of atmospheric water in the range of $1 2 4 5 0 { - } 1 2 \mathsf { \bar { 7 } } 0 0 \mathsf { c m } ^ { - 1 }$ , where the $\nu _ { 1 } + \nu _ { 2 } +$

$2 \nu _ { 3 }$ and the $\nu _ { 2 } ~ + ~ 3 \nu _ { 3 }$ bands are located. The $_ \mathrm { H _ { 2 } O }$ transitions in this range were recorded by Toth,35 using a multipass cell FT spectrometer and were also included in the HITRAN 96 database.36

In the atmospheric water absorption measurements, we removed the sample cell and let the room air fill the 180-cm-long standing-wave Ti:sapphire laser cavity. The $\nu _ { 1 } ~ + ~ \nu _ { 2 } ~ + ~ 2 \nu _ { 3 }$ and the $\nu _ { 2 } ~ + ~ 3 \nu _ { 3 }$ bands of $\mathrm { \bar { H } _ { 2 } O }$ are located around the center of the free-running laser emission envelope; therefore no tuning elements were used. The lasing threshold was 0.48 W. The working pump power was set to be 0.65 W, because a higher pump power reduces fluctuations of the Ti:sapphire laser power, which are typical for operation near threshold. This relatively strong pumping does not introduce any nonlinear effects into the Ti:sapphire laser,10 at least for the range of the generation times used in our experiment. In the FT spectrometer, a $\mathrm { C a F _ { 2 } }$ beam splitter and a silicon diode detector were used. The diameter of the aperture was 0.5 mm. The temperature was 20.0 C, and the relative humidity was 46.0% in the Ti:sapphire laser chamber. In the following we present two sets of spectra, which are used to evaluate the performance of our FT-ICLAS apparatus and to demonstrate the feasibility and the advantage of this technique.

## A. Fourier-Transform Intracavity Laser Absorption Spectra with Filters Applied

When filters are used to smooth the laser power fluctuations, the interleave rapid-scan method does not add any value, and thus the spectrum can be recorded with the normal scan method. The scanning modulation frequency was chosen to be 10 kHz. The 3-dB cutoff frequencies of the low-pass filter and the highpass filter were chosen to be 10 and 6 kHz, corresponding to the spectral frequencies of $^ { 1 5 , 0 0 0 }$ and $\stackrel { \bullet } { 9 0 } 0 0 \quad \mathrm { c m } ^ { - 1 }$ , respectively. The Ti:sapphire laser pulse width was 80 ms, and the sampling delay with respect to the pumping was set to be 60 ms. The unapodized resolution was $0 . 0 5 ~ \mathrm { c m } ^ { - 1 } \mathrm { m }$ , and the apodization function of Norton–Beer–Weak37 was used. A total of 200 normal scans were averaged.

The resulting spectrum of atmospheric water vapor is shown in Fig. 3. The FWHM of the gain envelope is ;83 cm21 . The absorption lines in the range of $1 2 4 8 0 { - } 1 2 7 5 0 ~ \mathrm { c m } ^ { - 1 }$ are clearly seen. The signal-tonoise ratio \~SNR! is found to be 337 in the envelope center and 270 at the position of half-height. We observed all the lines listed in the HITRAN 96 database. For example, the very weak line at 12560.624 $\mathrm { c m } ^ { - 1 }$ with a line strength of $9 . 2 \times 1 0 ^ { - 2 7 }$ molecule21 z cm reported in HITRAN 96 was clearly detected \~see the upper panel of Fig. 5 below!.

To evaluate the accuracy of the measurements, we selected 13 isolated lines with moderate intensities from Fig. 3. The comparison of the line positions with the HITRAN data is shown in Table 1. The observed average wave-number difference is 20.019 $\mathrm { c m } ^ { - 1 }$ with a standard deviation of $5 \times 1 0 ^ { - 3 } \ \mathrm { c m } ^ { - 1 }$ The standard deviation value is comparable with the measurement uncertainty $( 1 0 ^ { - 4 } - 5 \times 1 0 ^ { - 3 } \mathrm { c m } ^ { - 1 } )$ of the spectral data of Toth.35 Therefore we can expect that the precision of line positions in FT-ICLAS is generally as good as that in ordinary FT spectroscopy. Because the line positions given in HITRAN correspond to measurements at low pressure, the observed wave-number difference is actually an addition of the calibration value of FT spectrometer and the pressure shift of line positions. We could not find the pressure shift data for the lines of the $\nu _ { 1 } + \nu _ { 2 }$ $+ ~ 2 \nu _ { 3 }$ and the $\nu _ { 2 } + 3 \nu _ { 3 }$ bands. However, the average pressure shift in the $^ { 1 2 , 1 9 0 - 1 2 , 2 9 1 - \mathrm { c m } ^ { - 1 } }$ range38 is $_ { - 0 . 0 1 3 }$ cm21 with a standard deviation of $4 ~ \times$ $1 0 ^ { - 3 } \mathrm { { c m } ^ { - 1 } . }$ . From this we can expect that our FT-ICLAS data indicate the correct direction of the pressure shift.

![](images/146df747faf65d1412ee33b3781059b978ff3748d602ee28e7ab745edb70f4af.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | Water absorption (arb. unit) |
| ------------------ | ----------------------------- |
| 12,450             | ~0                            |
| 12,500             | ~0.5                          |
| 12,550             | ~1.0                          |
| 12,600             | ~1.5                          |
| 12,650             | ~0.8                          |
| 12,700             | ~0                            |
</details>

Fig. 3. Absorption spectrum of atmospheric water vapor recorded by FT-ICLAS with electronic filters.

According to Eq. \~1!, the line transmission at a certain $t _ { g }$ can be calculated by the following equation8:

$$
I (\nu , t _ {g}) = I _ {0} (\nu , t _ {g}) \exp [ - K N \phi (\nu) c t _ {g} ] \otimes f _ {\text { app }} \tag {6}
$$

Table 1. Comparison of the Experimental Results for 13 Isolated Water Vapor Lines with the Corresponding HITRAN Data

<table><tr><td>HITRAN Line Position (cm-1)</td><td>Exp.-HITRAN (cm-1)</td><td>HITRAN Line Strength (10-25molecule-1cm)</td><td>Exp. Integrated Intensity (cm-1)</td></tr><tr><td>12595.8376</td><td>-0.0209</td><td>1.34</td><td>0.04333</td></tr><tr><td>12580.3020</td><td>-0.0182</td><td>1.64</td><td>0.05844</td></tr><tr><td>12565.4090</td><td>-0.0242</td><td>3.72</td><td>0.12602</td></tr><tr><td>12635.5460</td><td>-0.0189</td><td>4.47</td><td>0.11576</td></tr><tr><td>12588.1560</td><td>-0.0234</td><td>5.29</td><td>0.17956</td></tr><tr><td>12604.0680</td><td>-0.0238</td><td>6.22</td><td>0.19175</td></tr><tr><td>12569.1256</td><td>-0.0154</td><td>6.36</td><td>0.22043</td></tr><tr><td>12578.7400</td><td>-0.0133</td><td>7.89</td><td>0.26956</td></tr><tr><td>12637.6554</td><td>-0.0201</td><td>10.1</td><td>0.21040</td></tr><tr><td>12629.7597</td><td>-0.0273</td><td>13.3</td><td>0.28808</td></tr><tr><td>12667.7522</td><td>-0.0111</td><td>15.0</td><td>0.28244</td></tr><tr><td>12615.8656</td><td>-0.0194</td><td>19.0</td><td>0.43194</td></tr><tr><td>12561.7492</td><td>-0.0153</td><td>25.4</td><td>0.77050</td></tr></table>

a Ref. 36.

![](images/c36ab3fedc0ece3653bcced4974266688a20701c838a752aaf6917258567f68e.jpg)

<details>
<summary>scatterplot</summary>

| KNCT | Integrated intensity Iint (cm⁻¹) |
|------|----------------------------------|
| 0.0  | 0.0                              |
| 0.1  | 0.05                             |
| 0.2  | 0.1                              |
| 0.3  | 0.15                             |
| 0.4  | 0.2                              |
| 0.5  | 0.25                             |
| 0.6  | 0.2                              |
| 0.7  | 0.15                             |
| 0.8  | 0.25                             |
| 0.9  | 0.25                             |
| 1.0  | 0.25                             |
| 1.1  | 0.4                              |
| 1.2  | 0.4                              |
| 1.3  | 0.75                             |
| 1.4  | 0.8                              |
| 1.5  | 0.8                              |
| 1.6  | 0.8                              |
</details>

Fig. 4. Relation of the experimental integrated intensity versus the calculated absorption intensity from the HITRAN line strength for the 13 selected lines.

Here V denotes the convolution. $I _ { 0 } ( \nu , t _ { g } )$ is the laser intensity without sample absorption, or simply the baseline of the spectrum. K is the line strength. N is the molecular density of the atmospheric water vapor. According to the humidity and temperature in the Ti:sapphire laser cavity, N is computed to be $2 . 6 7 \% \times 1 0 ^ { 1 7 }$ moleculesycm3 . f\~n! is the normalized Voigt line profile given by a convolution of pressure broadening and Doppler broadening. $f _ { \mathrm { a p p } }$ denotes the apparatus function.

Since the spectrum recorded with filters is obtained from the interferogram averaged over the filter bandwidth, it is interesting to check the relative intensity in such a spectrum and to try finding an effective generation time,

$$
\int \ln [ I _ {0} ^ {\mathrm{fil}} (\nu , t _ {g}) / I ^ {\mathrm{fil}} (\nu , t _ {g}) ] \mathrm{d} \nu = K N c t _ {g} ^ {\mathrm{eff}} \tag {7}
$$

Here the generation time $t _ { g }$ is replaced with the effective time $\mathrm { t } _ { \mathrm { g } } ^ { \mathrm { \scriptsize ~ e f f } } ,$ , which is related to the laser pulse width $T = 8 0$ ms in our experiment. The superscript fil denotes the filters used in recording the spectra. The measured spectrum \~Fig. 3! is converted into the form of absorption, ln $[ I _ { 0 } ^ { \mathrm { \scriptsize ~ f i l } } ( \nu , t _ { \mathrm { g } } ) / I ^ { \mathrm { \scriptsize ~ f i l } } ( \nu , t _ { \mathrm { g } } ) ]$ . The integrated intensities for the 13 selected lines are obtained by a least-squares fit with the Lorentzian profile. The results are listed in the final column of Table 1. The relation between the observed line intensities and the KNcT values is plotted in Fig. 4. The satisfactory linearity can be seen for the lines near the envelope center \~cf. Table 1!. The linear fitting in Fig. 4 gives out the effective generation time $t _ { \sigma } ^ { \mathrm { { \scriptsize ~ e f f } } }$ \~7!#. A small deviation of the relative intensity can be seen for the four points marked with an asterisk, which have an absorption strength larger than $1 0 ^ { - 2 4 }$ molecules21 zcm and are located far from the envelope center \~cf. Table 1!. In general, the closer the line is to the envelope center and the smaller is its intensity, the smaller the relative intensity error. The intensity distortion of these lines occurs most likely because the spectrum in Fig. 3 was recorded with the integration method. Our numerical calculation shows that in such an integrated spectrum the same line appears with a smaller intensity if its position is far away from the envelope center.

![](images/d8ca88ce87b2eb1217f2c6d5ec64a9a9fd7862b91bf7ff72ee2f78c7370150b1.jpg)

<details>
<summary>line chart</summary>

| Wave number (cm⁻¹) | FT-ICLAS Transmittance | Simulation Transmittance |
| ------------------ | ---------------------- | ------------------------- |
| 12560              | ~0.9                   | ~0.9                      |
| 12580              | ~0.9                   | ~0.9                      |
| 12600              | ~0.9                   | ~0.9                      |
| 12620              | ~0.9                   | ~0.9                      |
</details>

Fig. 5. Upper panel, normalized spectrum from Fig. 3. The three lines marked with an asterisk do not belong to water transitions. Lower panel, simulation result with line intensities from the HITRAN 96 database.

A comparison between the spectrum computed from HITRAN linewidths and intensities and that obtained from the FT-ICLAS experiment is shown in Fig. 5 In the calculation the Lorentzian lines corresponding to the effective $t _ { g } ^ { \mathrm { ~ e f f } } \mathrm { ~ o f ~ } 0 . 5 7 \times 8 0 = 4 5 . 6$ ms were convolved with the Doppler profile; then the spectrum was converted into transmission. The convolution with the instrumental profile has also been performed. Figure 5 exhibits a good agreement in line position and intensity between the calculated spectrum shown in the lower panel and the normalized \~or baseline-corrected! experimental data shown in the upper panel. Careful examination shows, however, some deviations of the line intensities, as we expect for the integrated spectrum. It is found that the measured linewidths deviate from the simulation values within 610%. The reason for this linewidth uncertainty might be the spectral envelope drift. In a practical ICLAS system the envelope as well as its central wavelength of the spectral distribution may slowly drift during the recording of the interferogram. Possible reasons for this drift are slow variation of the pump power, progressing laser misalignment, and thermal drift of the broadband wavelength selector. The envelope drift will result in a wavelength-dependent \~or mode-dependent! intensity change. We can consider this effect separately for each laser mode, because the interferogram is a linear addition of the individual-mode interferograms. It is well known that the change of the source intensity during scanning is equivalent to apodization and results in the symmetrical change of the shape and the width of the apparatus function.39 As a result, the instrumental function in FT-ICLAS might have a wavelength-dependent shape. Since the final spectrum is the convolution of the molecular line broadening with the apparatus function, the line shape might be effected.

![](images/2b8130d5737289a2e219cc53779506d749f27b3b6b6756f1f527b89e78ec1826.jpg)

<details>
<summary>line chart</summary>

| v (cm⁻¹) | t_g = 35 μs | t_g = 45 μs | t_g = 75 μs | t_g = 105 μs | t_g = 135 μs |
| -------- | ----------- | ----------- | ----------- | ------------ | ------------ |
| 12,400   | ~0          | ~0          | ~0          | ~0           | ~0           |
| 12,500   | ~0          | ~0          | ~0          | ~0           | ~0           |
| 12,600   | ~0          | ~0          | ~0          | ~0           | ~0           |
| 12,700   | ~0          | ~0          | ~0          | ~0           | ~0           |
| 12,800   | ~0          | ~0          | ~0          | ~0           | ~0           |
</details>

Fig. 6. Time-resolved spectra recorded by FT-ICLAS at the generation time $\mathbf { t } _ { g }$ of 35, 45, 75, 105 and 135 $\mu \mathbf { s }$ .

According to the effective generation times obtained above, the effective absorption length, ${ c t } _ { g _ { \scriptscriptstyle - } } ^ { \mathrm { \scriptsize ~ e f f } } ,$ can be calculated to be ;13.7 km. If we take the SNR of 337 and the derived effective absorption length, the sensitivity in our FT-ICLAS experiment can be estimated as $( \mathrm { \bar { S } N R \ ^ { * } } L _ { \mathrm { e f f } } ) ^ { - 1 } = 2 . 2 \times \mathrm { i } \mathrm { \bar { 0 } ^ { - 9 } } \mathrm { c m } ^ { - 1 }$ .

## B. Time-Resolved Fourier-Transform Intracavity Laser Absorption Spectra

A series of time-resolved spectra at different generation times were recorded with the interleave rapidscan method. Although this method allows for as many as 16 time slices in one pulse, we used just one slice in the high-resolution measurement because of the memory limitation of our data acquisition processor board. The FT spectrometer scanning modulation frequency was chosen to be 5 kHz. The duration of the Ti:sapphire pulse was 150 ms. No electronic filters in the FT spectrometer were used. The unapodized resolution was $0 . 1 5 ~ \mathrm { c m } ^ { - 1 }$ , and the apodization function of the Blackman–Harris three term40 was used. We recorded a series of spectra with $t _ { g }$ of 30, 35, 45, 60, 75, 90, 105, 120, 135, and 150 ms. Twenty-five scans were averaged for each $t _ { g } .$

A subset of the time-resolved spectra is shown in Fig. 6 . The evolution of the spectral envelope and the absorption with the generation time can be clearly seen. The spectral noise in our experiment is determined by the laser intensity fluctuation and is almost the same for all the time-resolved spectra, except the first one, which corresponds to $t _ { \mathrm { { g } } } = 3 0 ~ \mu \mathrm { { s } }$ . The SNR at the center of the spectra recorded was estimated to be 51. The sampling at $t _ { \mathrm { g } } ~ = ~ 3 0$ ms occurs near the position of the first spike of laser intensity relaxation oscillations \~Fig. 2!, which is sensitive even to slight variations of the pump power, and thus unstable. In FT-ICLAS this introduces large sampling noise; therefore it is recommended that FT-ICLAS spectra not be sampled at generation times close to the cavity buildup time.

The above time-resolved spectra permit us to verify quantitatively the evolution of the FT-ICLAS spectra. According to the first exponential term in Eq. \~1!, the laser gain bandwidth decreases in proportion to $1 / \sqrt { t _ { \mathrm { g } } } .$ . The logarithm of the envelope width versus the logarithm of the generation time is plotted in Fig. $^ { 7 . }$ The linear fitting yields a slope of 20.59, which is in reasonable agreement with Eq. \~1!.

![](images/89dfd9e5ed5400ac91815084cecf5176bf074ecfeb9a003a428aed3016ca5b03.jpg)

<details>
<summary>scatterplot</summary>

| t_g (μs) | FWHM (cm⁻¹) |
| -------- | ----------- |
| 10       | 200         |
| 20       | 180         |
| 30       | 160         |
| 40       | 140         |
| 50       | 120         |
| 60       | 100         |
| 70       | 80          |
| 80       | 60          |
| 90       | 40          |
| 100      | 20          |
</details>

Fig. 7. Logarithm of the envelope width \~FWHM! versus the generation time $\mathbf { t } _ { g }$ for the time-resolved spectra.

It is interesting to check whether FT-ICLAS can correctly represent the evolution of an isolated absorption line with the increase of $t _ { g } .$ We perform baseline correction and transform the spectra from transmission to absorption. For demonstration we choose in the spectral center a line at 12595.838 $\mathrm { c m } ^ { - 1 }$ . The line strength is $1 . 3 4 \times 1 0 ^ { - 2 5 }$ molecules21 z cm according to the HITRAN database. Similar to Eq. \~7!, the integrated line intensity of the timeresolved spectra is related to the generation time by

$$
\int \ln [ I _ {0} (\nu , t _ {g}) / I (\nu , t _ {g}) ] \mathrm{d} \nu = K N c t _ {g}. \tag {8}
$$

The variation of \* $\mathrm { l n } [ I _ { 0 } ( \nu , t _ { g } ) / I ( \nu , t _ { g } ) ] \mathrm { d } \nu$ versus $t _ { g }$ is plotted in Fig. 8. It can be seen that the Beer– Lambert law is reasonably valid in the range of the generation time as great as 150 ms. From the slope of the linear fitting line, KNc, we can obtain the absorption strength of this line, $1 . 0 1 \times 1 0 ^ { - 2 5 }$ molecule21 $\mathrm { c u l e ^ { - 1 } \cdot \ c m } .$ , which is 33% smaller than the corresponding value given in HITRAN. Possible reasons for this discrepancy are that \~i! it is difficult to obtain accurate absolute intensities with the lines measured in open air, \~ii! some error might exist in the humidity measurement, \~iii! we did not perform the deconvolution of the observed spectrum with the FT instrument profile in calculating the integrated line intensities. The linear fitting line intersects the $t _ { g }$ axis at ;1.9 ms. This shift corresponds to the starting time $t _ { 0 }$ for the linear evolution.28 The obtained shift value is consistent with the numerical simulation and experimental results presented in Ref. 28.

![](images/5d8622aa2c9b814b55ba94d6027334ec2e07ab1fbd0442c433031f22764e3c2c.jpg)

<details>
<summary>scatterplot</summary>

| Generation time t_g (μs) | Integrated intensity (cm⁻¹) |
| ------------------------ | --------------------------- |
| 35                       | 0.02                        |
| 45                       | 0.04                        |
| 60                       | 0.05                        |
| 75                       | 0.06                        |
| 90                       | 0.08                        |
| 105                      | 0.09                        |
| 125                      | 0.10                        |
| 145                      | 0.12                        |
</details>

Fig. 8. Linear evolution of the integrated intensity over the line with the generation time $\mathbf { t } _ { g } .$

## 5. Conclusions

In the current study we have demonstrated that high-quality broadband infrared spectra can be obtained by intracavity absorption spectroscopy, using a Ti:sapphire laser and a continuous-scan Fouriertransform \~FT! interferometer. From comparison of the spectra of atmospheric water recorded in the $1 2 , 4 5 \hat { 0 } - 1 2 , 7 0 0 { \cdot } \mathrm { c m } ^ { - 1 }$ range at a resolution of 0.05 $\mathrm { c m } ^ { - 1 }$ with conventional FT measurements, we conclude that continuous-scan FT-ICLAS can be used to detect weak transitions, and it can provide accurate absorption line positions. This method can be directly applied to intracavity absorption spectroscopy with solid-state lasers in the near- and the midinfrared range, where there is a poor choice of multielement linear array detectors. Even though Ti: sapphire laser spectra can be well recorded with a conventional ICLAS with silicon diode arrays, the FT-ICLAS method provides significant time savings, because a time-consuming procedure of the wavenumber calibration of multiple spectral fragments is not required.

The interleave rapid-scan method has been found to be adequate for the study of the temporal evolution of intracavity absorption. We could not experimentally observe the expected reduction of the quantum noise, owing to the power instability of our multimode laser. As a result, the signal-to-noise ratios \~SNR’s! in time-resolved spectra were relatively poor.

We found that using electronic filters can effectively improve the SNR by smoothing the fluctuations in the laser source at the cost of some distortion of the absorption line intensities. The minimum detectable absorption of the FT-ICLAS with filters applied is found to be $2 \times 1 0 ^ { - 9 } \mathrm { c m } ^ { - 1 }$ . Research on a more efficient noise-reduction method that involves the normalization of the each sampled point of the interferogram by the total laser power is in progress.

This study was supported by the National Natural Science Foundation of China, Chinese Pandeng Project, Chinese Academic of Sciences and National Natural Science Youth Foundation of China.

## References and Notes

1. L. A. Pakhomycheva, E. A. Sviridenkov, A. F. Suchkov, L. V. Titova, and S. S. Churilov, “Line structure of generation spec-

tra of lasers with inhomogeneous broadening of the amplification line,” JETP Lett. 12, 43–45 \~1970!.  
2. A. C. Peterson, M. J. Kurilo, W. Braun, A. M. Bass, and R. A. Keller, “Enhancement of absorption spectra by dye-laser quenching,” J. Opt. Soc. Am. 61, 746–750 \~1971!.  
3. T. W. Ha¨nsh, A. L. Schawlow, and P. E. Toschek, “Ultrasensitive response of a CW dye laser to selective extinction,” IEEE J. Quantum Electron. QE-8, 802–804 \~1972!.  
4. V. M. Baev, T. Latz, and P. E. Toschek, “Laser intracavity absorption spectroscopy,” Appl. Phys. B 69, 171–202 \~1999!.  
5. A. Campargue, F. Stoeckel, and M. Chenevier, “Highsensitivity intracavity laser spectroscopy—applications to the study of overtone transitions in the visible range,” Spectrochim. Acta Rev. 13, 69–88 \~1990!.  
6. V. M. Baev, T. P. Belikova, E. A. Sviridenkov, and A. F. Suchkov, “Intracavity laser spectroscopy with continuously and quasicontinuously operating lasers,” Sov. Phys. JETP 47, 21–29 \~1978!.  
7. M. Chevenier, M. A. Me´lie\`res, and F. Stoeckel, “Intracavity absorption line shapes and quantitative measurements on $\mathrm { O _ { 2 } } , \mathrm { \Omega ^ { \mathrm { ~ } } }$ Opt. Commun. 45, 385 \~1983!.  
8. M. A. Me´lie\`res, M. Chenevier, and F. Stoeckel, “Intensity measurements and self-broadening coefficients in the g band of $\mathrm { O } _ { 2 }$ at 628 nm using intracavity laser-absorption spectroscopy \~ICLAS!,” J. Quant. Spectrosc. Radiat. Transfer 33, 337 \~1985!.  
9. D. A. Gilmore, P. V. Cvijin, and G. H. Atkinson, “Intracavity absorption spectroscopy with a titanium:sapphire laser,” Opt. Commun. 77, 385–388 \~1990!.  
10. A. Kachanov, A. Charvat, and F. Stoeckel, “Intracavity laser spectroscopy with vibronic solid-state lasers. II. Influence of the nonlinear mode coupling on the maximum sensitivity of a Ti:sapphire laser,” J. Opt. Soc. Am. B 12, 970–979 \~1995!.  
11. B. Kalmar and J. J. O’Brien, “Quantitative intracavity laser spectroscopy measurements with a Ti:sapphire laser: absorption intensities for water vapor lines in the 790–800 nm region,” J. Mol. Spectrosc. 192, 386–393 \~1998!.  
12. A. del Olmo, C. Domingo, J. M. Orza, and D. Bermejo, “FT intracavity laser spectroscopy: the B-X transition of $\mathrm { C l } _ { 2 } , \mathrm { } ^ { 5 } \mathrm { \bf J } .$ . Mol. Spectrosc. 145, 323–330 \~1991!.  
13. C. Domingo, A. del Olmo, R. Escribano, and J. M. Orza, “Fourier transform intracavity laser absorption spectra of $6 \nu _ { 1 }$ band of CDH3,” J. Chem. Phys. 96, 972–975 \~1991!.  
14. K. Strong, T. Johnson, and G. W. Harris, “Visible intracavity laser spectroscopy with a step-scan Fourier transform interferometer,” Appl. Opt. 36, 8533–8540 \~1997!.  
15. P. Biggs, G. Hancock, D. Heard, and R. P. Wayne, “A step-scan interferometer used for time-resolved FTIR emission spectroscopy,” Meas. Sci. Technol. 1, 630–636 \~1990!.  
16. V. Petricevic, S. K. Gayen, and R. R. Alfano, “Near infrared tunable operation of chromium doped forsterite laser,” Appl. Opt. 28, 1609–1611 \~1989!.  
17. D. A. Gilmore, P. V. Cvijin, and G. H. Atkinson, “Intracavity laser spectroscopy in the 1.38–1.55mm spectral region using a multimode $\mathrm { C r ^ { 4 + } { : } Y A G }$ laser,” Opt. Commun. 103, 370–374 \~1993!.  
18. D. Welford and P. F. Moulton, “Room-temperature operation of a Co:MgF laser,” Opt. Lett. 13, 975–977 \~1988!.  
19. M. P. Frolov and Y. P. Podmarkov, “Intracavity laser spectroscopy with a Co:MgF laser,” Opt. Commun. 155, 313–316 \~1988!.  
20. V. R. Mironenko and V. I. Yudson, “Quantum statistics of multimode lasing and noise in intracavity laser spectroscopy,” Sov. Phys. JETP 52, 594–602 \~1980!.  
21. V. R. Mironenko and V. I. Yudson, “Quantum noise in intracavity laser spectroscopy,” Opt. Commun. 34, 397–403 \~1980!.  
22. S. A. Kovalenko, “Quantum intensity fluctuations in multi-  
mode cw lasers and maximum sensitivity of intracavity laser spectroscopy,” Sov. J. Quantum Electron. 11, 759–762 \~1981!.  
23. V. M. Baev, G. Gaida, H. Schroder, and P. E. Toschek, “Quantum fluctuations of multi-mode laser oscillator,” Opt. Commun. 38, 309–313 \~1981!.  
24. A. A. Kachanov, V. R. Mironenko, and I. K. Pashkovich, “Quantum threshold of the sensitivity of an intracavity travelingwave laser spectrometer,” Sov. J. Quantum Electron. 19, 95–98 \~1989!.  
25. P. Fellgett, “Theory of multiplex interferometric spectrometry,” J. Phys. Radium 19, 187–191 \~1958!.  
26. F. Stoeckel, M. A. Me´lie\`res, and M. Chenevier, “Quantitative measurement of very weak $_ \mathrm { H _ { 2 } O }$ absorption lines by timeresolved intracavity laser spectroscopy,” J. Chem. Phys. 76, 2191–2196 \~1982!.  
27. H. Lin, X. G. Wang, S. F. Yang, S. M. Hu, and Q. S. Zhu, “Study of an intracavity laser absorption spectrometer incorporated with the Fourier transform spectrometer,” Chin. J. Lasers 25, 1008–1012 \~1998!.  
28. A. Kachanov, A. Charvat, and F. Stoeckel, “Intracavity laser spectroscopy with vibronic solid-state lasers. I. Spectrotemporal transient behavior of a Ti:sapphire laser,” J. Opt. Soc. Am. B 11, 2412–2421 \~1994!.  
29. J. J. Sloan and E. J. Kruus, “Time-resolved Fourier transform spectroscopy,” in Time Resolved Spectroscopy, R. J. H. Clark and R. E. Hester, eds. \~Wiley, New York, 1989!, pp. 219–253.  
30. P. R. Griffiths and J. A. de Haseth, “Chemical analysis,” in Fourier Transform Infrared Spectrometry, P. J. Elving and J. D. Winefordner, eds. \~Wiley, New York, 1986!, p. 15.  
31. H. Weidner and R. E. Peale, “Time-resolved Fourier spectroscopy for activated optical materials,” Appl. Opt. 35, 2849–2855 \~1996!.  
32. A. S. Zachor, I. Coleman, and W. G. Mankin, “Effect of drive nonlinearities in Fourier spectroscopy,” in Spectroscopic Techniques, G. A. Vanasse, ed. \~Academic, San Diego, Calif., 1981!, Vol. 2, Chap. 3, pp. 1–62.  
33. H. Weidner and R. E. Peal, “Event-locked time-resolved Fourier spectroscopy,” Appl. Spectrosc. 51, 1106–1112 \~1997!.  
34. E. N. Antonov and A. A. Kachanov, V. R. Mironenko, and T. V. Plankhotnik, “Dependence of the sensitivity of intracavity laser spectrometer on generation parameters,” Opt. Commun. 46, 126–130 \~1983!.  
35. R. A. Toth, “Measurement of H16O line positions and strengths: 11610 to 12861 $\mathrm { c m } ^ { - 1 } , \overline { { \mathbf { J } } } ,$ . Mol. Spectrosc. 116, 176–183 \~1994!.  
36. L. S. Rothman, C. P. Rinsland, A. Goldman, S. T. Massie, D. P. Edwards, J. M. Flaud, A. Perrin, C. Camy-Peyret, V. Dana, J.-Y. Mandin, J. Schroeder, A. McCann, R. R. Gamache, R. B. Wattson, K. Yoshino, K. V. Chance, K. W. Jucks, L. R. Brown, V. Nemtchinov, and P. Varanasi, “The HITRAN molecular spectroscopic database and HAWKS \~HITRAN atmospheric workstation!: 1996 edition,” J. Quant. Spectrosc. Radiat. Transfer 60, 665–710 \~1998!.  
37. The function form for Norton–Beer–Weak is $W ( \Delta ) = c _ { 0 } +$ $c _ { 1 } [ 1 - ( \Delta / \Delta _ { m } ) ^ { 2 } ] + c _ { 2 } \{ [ 1 - ( \Delta / \Delta _ { m } ) ^ { 2 } ] \} ^ { 2 }$ , where $c _ { 0 } = 0 . 3 4 8 0 9 , c _ { 1 } =$ 20.08758, and c 5 0.70348. D is the OPD value, and $\Delta _ { m }$ is the maximal OPD.  
38. P. L. Ponsardin and E. V. Browell, “Measurements of $\mathrm { H _ { 2 } } ^ { 1 6 } \mathrm { O }$ line strengths and air-induced broadenings and shifts in the 815-nm spectral region,” J. Mol. Spectrosc. 185, 58–70\~1997!.  
39. G. Guelachvili, “Distortions in Fourier spectra and diagnosis,” in Spectroscopic Techniques, G. A. Vanasse, ed. \~Academic, San Diego, Calif., 1981!, Vol. 2, Chap. 3, pp. 127–160.  
40. The function form for the Blackman–Harris three term is W\~D! $= a _ { 0 } + a _ { 1 }$ cos\~2pDyD ! 1 a cos\~4pDyD !, where $a _ { 0 } = 0 . 4 2 3 2 3$ , $a _ { 1 } = 0 . 4 9 7 5 5$ , and $a _ { 2 } = 0 . 0 7 9 2 2$ .