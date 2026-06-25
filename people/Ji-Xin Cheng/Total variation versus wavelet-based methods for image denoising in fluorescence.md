## FULL ARTICLE

# Total variation versus wavelet-based methods for image denoising in fluorescence lifetime imaging microscopy

Ching-Wei Chang1 and Mary-Ann Mycek\*; 1; 2; 3

1 Department of Biomedical Engineering, University of Michigan, Ann Arbor, MI 48109-2099, USA  
2 Comprehensive Cancer Center, University of Michigan, Ann Arbor, MI 48109-2099, USA  
3 Applied Physics Program, University of Michigan, Ann Arbor, MI 48109-2099, USA

Received 16 December 2011, revised 10 February 2012, accepted 23 February 2012 Published online 13 March 2012

Key words: Time-gated fluorescence lifetime imaging microscopy, precision improvement, image denoising, wavelet analysis, total variation

We report the first application of wavelet-based denoising (noise removal) methods to time-domain box-car fluorescence lifetime imaging microscopy (FLIM) images and compare the results to novel total variation (TV) denoising methods. Methods were tested first on artificial images and then applied to low-light live-cell images. Relative to undenoised images, TV methods could improve lifetime precision up to 10-fold in artificial images, while preserving the overall accuracy of lifetime and amplitude values of a single-exponential decay model and improving local lifetime fitting in live-cell images. Wavelet-based methods were at least 4-fold faster than TV methods, but could introduce significant inaccuracies in recovered lifetime values. The denoising methods discussed can poten tially enhance a variety of FLIM applications, including live-cell, in vivo animal, or endoscopic imaging studies, especially under challenging imaging conditions such as low-light or fast video-rate imaging.

![](images/b7d2ab535eab23e3af113e77cde3da43037f2776898422fbb25ea519ff6e061a.jpg)

<details>
<summary>natural_image</summary>

Three abstract shapes on a dark blue background, resembling stylized clouds or organic forms (no text or symbols)
</details>

Fluorescence lifetime map of HCT-116 live cells stained with BCECF, constructed from itensity images denoised with modified FWTV

Continuous Wavelet Transform

DWT: Discrete Wavelet Transform

FLIM: Florescence Lifetime Imaging Microscopy

FWTV: f-weighted Total Variation

RME: Relative Mean Error

RSD: Relative Standard Deviation

SWT: Stationary Wavelet Transform

TV: Total Variation

## 1. Introduction

Fluorescence lifetime imaging and fluorescence lifetime imaging microscopy (FLIM) are useful molecular imaging techniques for pre-clinical and clinical studies in living cells, tissues, small animals, and endoscopic samples, with fluorescence lifetime providing image contrast [1–10]. Fluorescence lifetime can be employed as an optical sensor to indicate microenvironmental conditions such as oxygen levels, the state of endogenous/exogenous fluorophores, and Fo¨ rster resonance energy transfer in live cells [11– 18].

The interest in biological FLIM is increasing, as commercial FLIM modules become available for confocal and multi-photon microscopes. However, low fluorescence signals from biological samples can be a challenge, causing poor lifetime precision. For endogenous fluorophores, low signals could result from low concentrations and/or unfavorable optical properties. For exogenous fluorophores, low signals could result from low concentrations desired to minimize the effects on sample physiology and/or low transfer efficiency. To increase measured fluorescence signals from biological samples, high-intensity light sources such as lasers can be used in FLIM, but this may cause unexpected cell responses and sample damage/ ablation [19, 20], and may also cause fluorophore photobleaching.

Image “denoising” (noise removal) [21, 22] has great potential to improve FLIM precision. Wavelet analysis is a commonly used method that has been used for restoring fluorescence microscopy images [23, 24] and for denoising frequency-domain confocal and full-field FLIM images [25, 26]. Other image denoising methods include total variation (TV) denoising, Tikonov denoising, Gaussian smoothing [27], non-parametric regression method [28], and multiframe SURE-LET (Stein’s unbiased risk estimate-linear expansion of thresholds) denoising [29]. Among these techniques, TV denoising has been reported to improve FLIM precision [30]. In this study, we report the first application of wavelet-based denoising methods to time-domain FLIM, and compare them with previously developed TV denoising methods [30, 31]. This is a new research area that, to our knowledge, has not yet been explored before, potentially aiding a variety of emerging in vivo and clinical applications.

## 2. Methods

## 2.1 Time-gated FLIM system and live-cell sample preparation

We designed and characterized a novel wide-field, time-domain box-car FLIM system for picosecond time-resolved biological imaging [32, 33]. A pulsed (repetition rate ¼ 1–20 Hz) nitrogen laser (337.1 nm, GL-3300, Photon Technology International, Lawrenceville, NJ) pumping a dye laser (GL-301, Photon Technology International, Lawrenceville, NJ) for UV-visible-NIR excitation offers a significantly less expensive, wide-field, and potentially portable alternative to multi-photon excitation for sub-nanosecond

FLIM imaging of biological samples [33]. After a sample was illuminated by an excitation pulse, the fluorescence emission was recorded at different gate delays. The time interval between the starting points of two consecutive gates was denoted by $^ { \mathrm { s c } } d t ^ { \mathrm { s } }$ . At each gate delay, the emission intensities were integrated during a gate width (denoted by $^ { \ast } g ^ { \prime \prime } )$ controlled by the intensifier of an intensified chargecoupled device (ICCD) camera (microchannel size ¼ -10 mm, Picostar HR, LaVision, Germany). The gain of the ICCD is controllable and the gate width settings can vary from 200 ps to 10 ms for high-speed imaging applications [34]. The large temporal dynamic range (750 ps–1 ms), the 50 ps lifetime discrimination, and the spatial resolution of less than 1.4 mm of the system make it suitable for studying many endogenous and exogenous fluorophores that may transit through cells [35–37]. To create fluorescence lifetime maps rapidly, a four-gate protocol, based on single-exponential fluorescence decay, with an analytical least squares lifetime determination algorithm was used on a pixel-by-pixel basis. It is more precise than a two-gate protocol while still being easy to implement [38–40]. The fitting was implemented without any weighting and no particular form of variance distribution (such as Poisson distribution) was assumed. This is because, as mentioned later in Section 2.2, there was a combination of noise distributions in our real images and this kind of noise distribution was taken into consideration in the denoising process. The analytical solution can be derived by first linearizing the overdetermined system in log domain and then solving the normal equations, $\left( X ^ { T } X \right) a = X ^ { T } y$ , where a is the system parameters we are interested in, with X and y as the independent and dependent variables, respectively:

$$
\tau_ {p} = - \frac {N (\sum t _ {i} ^ {2}) - (\sum t _ {i}) ^ {2}}{N \sum t _ {i} \ln I _ {i , p} - (\sum t _ {i}) (\sum \ln I _ {i , p})} \tag {1}
$$

where $\tau _ { p }$ is the lifetime of pixel $p , I _ { i , p }$ is the intensity of pixel $p$ in image $i , t _ { i }$ is the gate delay of image i, and N is the number of images, which is four. All sums are over i. This time-gated method is generally inefficient in terms of signal detection as compared to time-correlated single photon counting (TCSPC) or even frequency-domain methods, since a large percentage of the signal is simply discarded. However, it enables much faster and sometimes videorate image recording (only four intensity values are needed for each pixel) and also very rapid lifetime determination due to the ability to evaluate all pixels simultaneously using the analytical solution (Eq. (1)).

HCT-116 live cells (purchased from ATCC, CCL-247TM) were cultured with modified McCoy’s 5a medium under $5 \% \mathrm { C O } _ { 2 }$ incubation. After removing the culture media and washing 3 times using phosphate buffered saline (PBS), cells at 80% confluence were incubated with 1 mM of the acetoxymethyl (AM) ester derivative of BCECF (20 ,70 - bis-(2-carboxyethyl)-5-(and-6)-carboxyfluorescein, a widely used fluorescent indicator for intracellular pH) (Invitrogen, CA) in PBS at 37 C for 1 hr for cell staining. The laser excitation wavelength was 434 nm and the fluorescence emission was collected at 480  20 nm with a 40, 1.3 NA objective. Five images were averaged for each gate in the FLIM imaging of the samples with dt ¼ 1 ns and g ¼ 0.2 ns.

## 2.2 Total variation denoising

The f-weighted TV (FWTV) model was described previously [30, 31, 41–43]. It has been demonstrated to have some advantages over other previously developed TV models, which are mostly based on the commonly known Rudin-Osher-Fatemi (ROF) model [44]. The FWTV model keeps the major advantage of TV denoising models, which are edgepreserving, but was specifically developed to remove Poisson noise, an inevitable form of noise occurring in image acquisition with photon counting devices, while still having high flexibility to be easily adapted for removing non-Poisson noise (described below). In our previous studies, we have demonstrated how the FWTV model can be used in time-gated FLIM and time-correlated single photon counting FLIM to improve lifetime precision [30, 31, 41–43].

The FWTV model has the following mathematical form:

$$
E = \int_ {\Omega} | \nabla u | \mathrm{d} x \mathrm{d} y + \lambda \int_ {\Omega} \frac {(f - u) ^ {2}}{f} \mathrm{d} x \mathrm{d} y \tag {2}
$$

where E denotes the energy, through minimization of which denoising was performed, W denotes the signal domain, l is the fidelity coefficient, u represents the processed image, f represents the input or noise-corrupted image, and the variables x and y represent the spatial location of the pixels. The values of l were determined by the “discrepancy rule” [45], which requires the fidelity term (the second term on the right hand side of Eq. (2)) evaluated with f and the final u to be the same as that evaluated with f and the estimated original image without noise corruption [41]. Equation (2) was designed for removing Poisson noise, since the data variance due to noise (the denominator of the integrand in the fidelity term, or, the “weighting”) is equal to the intensity, f, which is a characteristic of Poisson noise.

To minimize the defined energy, E, and to implement denoising, the gradient descent of E, with respect to time, t, along the direction of u was used with iterations to achieve the final stable, denoised u. Here, the “time” is just a dimension along the iterations towards the stable u and does not involve rea time. Mathematically, u evolves from f (the input of u) through iterations, and in this process the measurement f is selectively smoothed to a denoised state: the smoothing occurs only in the direction perpendicular to, but not in parallel with, local intensity gradient. This process, therefore, preserves the edges of objects delineated by intensity contrast.

Further modification of FWTV for removing non-Poisson noise (such as a combination of different forms of noise at low photon counts in real imaging systems) has been demonstrated to be quantitatively accurate when applied to FLIM [41]. In the modified FWTV, f in the weighting of FWTV was replaced with Gf, where G represented the ratio of the signal variance to the mean intensity counts and was a function of local mean intensity of the image [41]. This modified FWTV was also used here to denoise live-cell FLIM images.

## 2.3 Wavelet-based denoising

A wavelet is a waveform of effectively limited duration with an average value of zero. A wavelet transform is to describe a function by using wavelets, which can be scaled and translated (shifted). For example, the continuous wavelet transform (CWT) is defined as an integral over the dimension of the signal (a continuous, square-integrable function) multiplied by scaled, shifted versions of the wavelet function. The results of the CWT are the wavelet coefficients, which are a function of scale and position.

In this study, the first wavelet-based denoising method was based on Discrete Wavelet Transform (DWT). In DWT, the concept is to choose only a subset of scales and positions for the calculations of wavelet coefficients. Only scales and positions based on powers of two (the dyadic scales and positions) are chosen. To use DWT for image denoising, the resulting wavelet coefficients from DWT decomposition are thresholded before the image is reconstructed. The thresholding can be performed with either “hard thresholding”, which sets the coefficients that are less than or equal to the threshold to zero, or “soft thresholding”, where, in additional to hard thresholding, the threshold value is subtracted from all the coefficients with their values greater than the threshold. An efficient way to implement DWT is to use filters. This was developed in 1988 by Mallat [46]. In this case, each level of filtering produces approximation coefficients and detail coefficients, followed by a “decimation” process, which retains only even indexed elements. The approximation coefficients can then be further filtered into the next level of decomposition, and thresholding can be applied to the detail coefficients for denoising.

The second wavelet-based denoising method was based on Stationary Wavelet Transform (SWT). SWT was developed to remove the disadvantage of DWT being not time-invariant, meaning that when the input signal is translated, the DWT transform is not translated accordingly. SWT solves this problem by averaging some slightly different DWT, called epsilon-decimated DWT [47]. Epsilon-decimated DWT is generated by the decimation that chooses either even or odd indexed elements instead of choosing only even indexed elements, following DWT. This choice is involved in each level of decomposition.

DWT and SWT image denoising was implemented with four levels of decomposition and softthresholding, which makes smooth transitions between the values above and below the threshold, using Matlab’s Wavelet Toolbox version 4.4. The default threshold determination method (universal thresholding $s ( \log { ( n ) } ) ^ { 1 / 2 }$ , with n being the number of pixels in the image and s being the median absolute value of the detail wavelet coefficients divided by 0.6745) was not used due to the fact that s would be zero and hence no denoising would be performed for our artificial images (possibly because there are many zero-intensity background pixels, described in Section 2.4) corrupted by Poisson noise. Therefore, mean absolute value divided by 0.6745 was used as s in the expression $s ( \log { ( n ) } ) ^ { 1 / 2 } .$ Global thresholding (meaning the same threshold value is used for all decomposition levels) was used for all four levels of detail coefficients of each gate, but the threshold values were determined separately for different gates. Fixed threshold values of 100 and 500 were also used in SWT denoising for comparison. These values are comparable to and enclose the “appropriate” values (see below). The wavelet biorthogonal 3.7 (bior 3.7) was chosen, not only because it is a commonly used wavelet but also because it has been demonstrated to perform well in frequency-domain FLIM for background subtraction and denoising [26].

A more sophisticated wavelet-based algorithm [48, 49] employed in this study (denoted as “Poisson Wavelet” below) is a Bayesian approach to Poisson intensity estimation based on the translation invariant hereditary unnormalized Haar wavelet transform. This type of wavelet allows a simple formulation for Poisson data. Translation invariant Haar estimation for Poisson data includes thresholding decisions based not only on the magnitude of the coefficients, but also on the coefficients of the node’s descendants. Image estimation based on this method is near minimax optimal reconstruction techniques for photonlimited images. It reduces artifacts by averaging over all possible shifts of the underlying partition. Previous studies improved the robustness of this technique by including a hereditary constraint in the thresholding rule: a coefficient can only be thresholded if all its descendants are also thresholded [49].

Poisson Wavelet image denoising was implemented by using the Matlab function provided on the website of Dr. Rebecca Willett’s laboratory at Duke University. The penalty values (similar to the threshold values used in DWT and SWT) were determined using the default approach of log (summation of the values of all the pixels)/2.

The threshold values used in DWT (and SWT with “varying threshold”, see Section 3.1.2) were $4 5 8 . 5 0 \pm \bar { 1 . 8 7 , 3 1 9 . 8 6 } \pm 1 . 4 2 , 2 2 4 . 4 6 \pm 0 . 9 7 , 1 \dot { 5 } 9 . 0 4 \pm$ 0.63 (number of trials ¼ 20) for the first, second, third, and fourth gates, respectively. These values were not fixed and had distributions, because in each Monte Carlo simulation (Section 2.5), noise was randomly generated based on Poisson distribution. The penalty values used in Poisson Wavelet were 8.56  $^ { \dot { 0 } } _ { 0 . 0 7 9 } \times 1 0 ^ { - 3 } , \ 8 . 3 5 \pm 0 . 0 9 3 \times 1 0 ^ { - 3 } , \ 8 . 1 4 \pm 0 . 1 7 \times 1 0 ^ { - 3 } .$ , $7 . 9 4 \pm 0 . 1 8 \times 1 0 ^ { - 3 }$ (number of trials ¼ 20) for the first, second, third, and fourth gates, respectively.

## 2.4 Artificial images

Artificial images with predetermined parameters were employed to evaluate fluorescence lifetime determination accuracy and precision after denoising. The fluorescence decay model was single-exponential with the intensity profile $I ( t ) = \stackrel { \cdot } { \alpha } \exp \left( - t / \tau \right)$ , where t is fluorescence lifetime and a is a pre-exponential term, or amplitude. Geometry that we may encounter with live-cell FLIM was mimicked. It consisted of “the ring” (the large open circle shown in the upper-right panel of Figure 1) with t ¼ 5 ns and $a = 1 0 0 0 .$ , “the inner circle” (the centered solid circle inside the ring) with t ¼ 10 ns and $a = 1 0 0 0 .$ and “the satellite” (the small dot to the bottom right of the inner circle and the ring) with t ¼ 10 ns and $a = 5 0$ . The image size was 128  128 pixels. Note that total photon counts (at) here were kept relatively high, making the relative standard deviation (Section 2.5) low, for better characterizations of the denoising methods with minimized possible bias of Poisson distribution at low photon counts. A combination of different forms of noise including Poisson noise at low photon counts will be considered in livecell images (Section 3.2). As an example of the geometry mentioned here, a cell may have some fluorophores inside it with higher lifetime and others interacting in its membrane with lower lifetime, while in another smaller cell or organism the same fluorophores at lower concentration are present. The optimal gating scheme was determined to be g ¼ 16 ns and dt ¼ 4 ns [41]. It was an optimal gating scheme for a certain lifetime range in which the above setting was covered.

![](images/69c51265763a4a65f2a3c2073151c2f5f7158922debe656c45c5c4287d66987a.jpg)  
Figure 1 (online color at: www.biophotonics-journal.org) RSD (Relative Standard Deviation, in %), indicating the precision, of the lifetime map constructed with the undenoised and denoised artificial images using several different denoising methods. The precision improvement wa method- and geometry-dependent. The ring was the most difficult to denoise. SWT with threshold ¼ 500 generally had the best precision but it suffered from severe inaccuracy (see Figure 2 and Table 1).

## 2.5 Evaluation of accuracy and precision

To assess accuracy and precision, Monte Carlo (MC) simulations were used, along with the artificial images (Section 2.4), to construct the lifetime distribution determined from Poisson-noise-corrupted intensity images, either with or without denoising. First, the single-exponential decay model I(t) (Section 2.4), the correct values of lifetime t and pre-exponential term a, gate width g, and time interval dt between two consecutive gates were used to simulate the noise-free time-gated fluorescence intensity images. Then, Poisson noise was added to each pixel in each image, and denoising was applied to each image.

The lifetime values retrieved from the denoised images using Eq. (1) were recorded in each iteration to build up a histogram for each pixel over a number of iterations of noise addition, denoising, and lifetime determination. The number of simulations was 20 in each denoised or undenoised case. The mean and standard deviation (std.) of the lifetime distribution were used for the evaluation of accuracy and precision with RSD [relative standard deviation, in %, defined as (std./mean)  100, also known as coefficient of variation] and RME {relative mean error, in %, defined as [(mean – correct value)/correct value]  100}. In the undenoised case (see Section 3), the step of “denoising” was omitted.

## 3. Results and discussion

## 3.1 Artificial images

## 3.1.1 A comparison of DWT, Poisson Wavelet, and FWTV

FWTV has previously been tested on the artificial images (Section 5.2 in [41]). The results demonstrate that after FWTV denoising, the precision of lifetime determination was improved for all three objects (the RSD values were 0.14, 1.43, and 4.76% for the inner circle, the ring, and the satellite, respectively), while the accuracy was preserved (the RME values of all three objects were within 1% from zero).

Figure 1 and Table 1 show that precision improvement was method- and geometry-dependent. FWTV and Poisson Wavelet performed approximately equally well, with the ring being most difficult to denoise. In the undenoised image, the satellite had a much higher RSD value due to its much lower total photon counts. After denoising with the three methods (DWT, Poisson Wavelet, and FWTV [41]), all the three objects had lowered RSD and the precision improvement was most significant in the inner circle. However, DWT had the smallest improvement (averaged RSD ¼ 0.64%) and FWTV the greatest (averaged RSD ¼ 0.14% [41], precision improvement >10-fold when compared with the undenoised value of 1.80%), while Poisson Wavelet had slightly smaller improvement (averaged RSD ¼ 0.23%) than FWTV. The ring was most difficult to denoise for all the three methods, probably due to the fact that it had an edge-rich geometry. Still, FWTV produced the lowest RSD and improved the precision by about 1.3-fold [41]. Interestingly, for the satellite, DWT produced the best precision, but it caused inaccuracy (described below).

Table 1 Averaged RME and RSD (%), over the pixels in each of the three objects (the inner circle, the ring, and the satellite) in the undenoised and denoised artificial images using several different denoising methods

<table><tr><td rowspan="2"></td><td colspan="2">Undenoised</td><td colspan="2">DWT</td><td colspan="2">Poisson Wavelet</td></tr><tr><td>RSD</td><td>RME</td><td>RSD</td><td>RME</td><td>RSD</td><td>RME</td></tr><tr><td>Inner circle</td><td>1.80</td><td>0.035</td><td>0.64</td><td>-0.12</td><td>0.23</td><td>0.0028</td></tr><tr><td>Ring</td><td>1.91</td><td>-0.020</td><td>1.75</td><td>6.34</td><td>1.64</td><td>-0.0054</td></tr><tr><td>Satellite</td><td>7.90</td><td>0.031</td><td>2.49</td><td>-11.89</td><td>4.35</td><td>0.33</td></tr><tr><td rowspan="2"></td><td colspan="2">SWT</td><td colspan="2">SWT</td><td colspan="2">SWT</td></tr><tr><td colspan="2">threshold = 100</td><td colspan="2">varying threshold</td><td colspan="2">threshold = 500</td></tr><tr><td></td><td>RSD</td><td>RME</td><td>RSD</td><td>RME</td><td>RSD</td><td>RME</td></tr><tr><td>Inner circle</td><td>0.74</td><td>-0.16</td><td>0.52</td><td>-0.12</td><td>0.39</td><td>-0.74</td></tr><tr><td>Ring</td><td>1.62</td><td>3.24</td><td>1.57</td><td>5.80</td><td>1.15</td><td>19.24</td></tr><tr><td>Satellite</td><td>2.99</td><td>-9.19</td><td>2.23</td><td>0.62</td><td>1.64</td><td>-11.10</td></tr></table>

Figure 2 and Table 1 show that both FWTV [41] and Poisson Wavelet preserved the accuracy of lifetime determination after denoising, with Poisson Wavelet performing slightly better especially for the satellite. In this case, the undenoised image and its RME values served as the accuracy standard, since the noise was defined by Poisson random distribution. In other words, these RME values are not exactly zero simply due to randomness. Compared to the undenoised case, if denoising causes RME values to become farther away from zero (possibly due to unsuitable assumption of noise distribution), this is an evidence of producing a bias and making lifetime determination inaccurate. Our goal is therefore to find the denoising methods that can improve the precision to the best degree without causing inaccuracy.

![](images/92c1401d4c3eb4374adbba27fe30eaef0a2a206da4bc8137f9d88a59ad65a070.jpg)

<details>
<summary>heatmap</summary>

| Condition             | Value |
| --------------------- | ----- |
| Undenoised            | 0     |
| DWT                   | 0     |
| Poisson Wavelet       | 0     |
| SWT, threshold = 100   | 0     |
| SWT, varying threshold | 0     |
| SWT, threshold = 500   | 0     |
</details>

Figure 2 (online color at: www.biophotonics-journal.org) RME (Relative Mean Error, in %), indicating the accuracy, of the lifetime map constructed with the undenoised and denoised artificial images using several different denoising methods. FWTV [41] and Poisson Wavelet performed equally well and preserved the accuracy of lifetime determination after denoising.

On the other hand, DWT denoising suffered from severe inaccuracy for the ring (averaged RME >6%) and the satellite (averaged RME <10%) and even for the inner circle (negative RME on the edge but positive RME off-edge).

## 3.1.2 A comparison of SWT with different threshold values

With SWT, the RSD values for all the three objects decreased with increasing threshold values from 100 to varying values (between 100 and 500) to 500, because higher threshold caused greater smoothing and removed more noise. However, only SWT with varying threshold had both the inner circle and satellite accurate (absolute values of averaged RME <1%), although the RME of the ring was still high (5.80%), and higher than that from SWT with threshold ¼ 100. Also, SWT with varying threshold was better than DWT in terms of both precision and accuracy, especially for the accuracy of the satellite.

## 3.1.3 Overall performance of FLIM denoising methods

Overall, although DWT and SWT under current settings improved precision, they mostly suffered from severe inaccuracies. SWT with varying threshold could still be a good choice except that edge-rich objects such as the ring would have inaccurate lifetime values. Poisson Wavelet and FWTV appeared to be better choices for both improved precision and good accuracy. As for the running times for each 128  128 image, wavelet-based methods were faster (DWT, Poisson Wavelet, and SWT had running times -0.1, -0.2, and -0.6 sec, respectively) compared to FWTV (-2.4 sec), making Poisson Wavelet the best choice. However, as will be demonstrated in the next section, our FWTV could be further modified (Section 2.2) to remove non-Poisson distributed noise with good accuracy.

Another key point to make is that, after denoising, the edge of each object may become less definite or blurred due to intensity diffusion. Therefore, it is important to check if denoising causes any bias for segmentation after different types of denoising. This has been indirectly investigated with our artificial images and is presented in Figures 1, 2, and Table 1. When evaluating the accuracy and precision of lifetime determination of the three different objects (the inner circle, the ring, and the satellite), the same pixels were used for the mask for a certain object after different kinds of denoising (or no denoising).

In other words, any denoising that caused the object shape/size to slightly change could introduce a bias in the averaged lifetime value, since in this case the mask for that object could not exactly cover the entire object and/or included pixels in the background or in another object. On the other hand, further segmentation analysis will be considered as one of our future directions (Section 3.3).

## 3.2 Denoising live-cell FLIM images

Poisson Wavelet and a modified FWTV were used to denoise the gated fluorescence intensity images from our FLIM system before lifetime map construction. DWT and SWT were not used since they suffered from severe inaccuracies (Section 3.1). FWTV was modified because real imaging systems, especially at low photon counts, have forms of noise other than Poisson distribution. The total photon counts were around 600, which was in the appropriate range (approximately $1 0 ^ { 2 } – 1 0 ^ { 4 } )$ for the use of denoising for FLIM precision improvement [30]. Both denoising methods could reduce the uncertainties, as shown in Figure 3. However, the lifetime values were different when averaged, and were compared with the averaged undenoised lifetime value, which should remain almost constant pre- and post-denoising, due to the randomness of the uncertainties. Table 2 clearly demonstrates that the modified FWTV could better preserve the overall t and a values (<3.5% changes) while still improving local lifetime fitting with averaged $R ^ { 2 }$ increase ¼ -1.5% and averaged $\chi ^ { \overline { { 2 } } }$ decrease $= \sim 2 0 \%$ . This is due to the fact that the flexibility and modification of our FWTV rendered it the capability of removing a combination of different forms of noise that occur in real imaging systems. In addition, the accurate denoising results of the modified FWTV illustrated here are also consistent with our previous real-image denoising results [30, 31, 41–43].

Table 2 The averaged lifetime values (t, in ns), pre-expo nential terms (a), R-squared values (R2 ) and Chi-squared values $( \chi ^ { 2 } )$ over the non-zero pixels in the live-cell lifetime images shown in Figure 3, and their % changes compared to the undenoised image.

<table><tr><td></td><td>Undenoised</td><td>Poisson Wavelet</td><td>Modified FWTV</td></tr><tr><td> $\tau$ </td><td>2.38</td><td>2.08</td><td>2.30</td></tr><tr><td>%  $\tau$  change</td><td>0</td><td>-12.61</td><td>-3.32</td></tr><tr><td> $\alpha$ </td><td>190</td><td>183</td><td>186</td></tr><tr><td>%  $\alpha$  change</td><td>0</td><td>-3.68</td><td>-2.11</td></tr><tr><td> $R^{2}$ </td><td>0.93</td><td>0.96</td><td>0.94</td></tr><tr><td>%  $R^{2}$  change</td><td>0</td><td>2.91</td><td>1.51</td></tr><tr><td> $\chi^{2}$ </td><td>1.20</td><td>0.79</td><td>0.95</td></tr><tr><td>%  $\chi^{2}$  change</td><td>0</td><td>-34.31</td><td>-20.33</td></tr></table>

## 3.3 Future improvements

Future improvements of the current algorithms include local thresholding (different threshold values can be used for different decomposition levels) and more sophisticated approaches to threshold determination in DWT, SWT, and other wavelet-based methods for FLIM use. Newly developed methods for wavelet-based denoising of Poisson-corrupted images [50] will be further considered in the future. Also, high-speed FWTV may be developed by improving the code efficiency and adopting advanced algorithms [51, 52]. In addition, precision and accuracy evaluation of multi-exponential decay lifetime determination is also an important issue and will be investigated in combination with FLIM image denoising. Finally, since precise and accurate noise removal can enhance other image processing techniques including deconvolution (with 3D image slicing)/deblurring [53], segmentation, and object tracking, the combination of denoising and these techniques could be employed for FLIM use, as well.

![](images/7816a6fdb16e2ec9d1061dea53398808a12abeae4e4d7772d626d5ba8a018aa0.jpg)  
Figure 3 (online color at: www.biophotonics-journal.org) The lifetime maps (in ns) of HCT-116 live cells stained with BCECF. Each map was constructed from four gated intensity images that were either undenoised or denoised with one of the two methods: Poisson Wavelet and modified FWTV. Both denoising methods could reduce the uncertainties compared to the undenoised image. However, the lifetime values within the cell regions denoised with the two methods were different.

As a key future direction, we understand that segmentation analysis following denoising is an important issue. However, advanced segmentation methods need to be applied to the images for this kind of analysis, and this will inevitably introduce more uncertainties since the results will definitely depend on the choice of segmentation method. In this work, therefore, we focused more on preserving the accuracy of the lifetime determination while enhancing the precision, leaving segmentation analysis as one of our major future directions following this work.

## 4. Conclusions

In this study, TV-based and wavelet-based image denoising methods were characterized and compared for individual strengths and weaknesses with artificial images and live-cell images acquired from a gated time-domain FLIM system. With artificial images, FWTV and Poisson Wavelet performed almost equally well (precision improvement up to 10- fold, depending on the geometry of objects) and better than DWT and SWT in terms of mostly accuracy and partially precision, with wavelet-based methods running faster. For live-cell images, the modified FWTV better preserved the overall t and a values (<3.5% changes compared to the undenoised image) while still improving local lifetime fitting (averaged $R ^ { 2 }$ increase $\doteq \sim 1 . 5 \%$ and averaged $\chi ^ { 2 }$ decrease ¼ -20%). The methods proposed here can enhance both the precision and the accuracy of FLIM, especially under challenging imaging conditions, such as low-light or fast video-rate imaging. This approach should aid current and rapidly emerging FLIM applications, including live-cell, in vivo animal, or endoscopic imaging, and is potentially applicable to other biomedical imaging systems.

Acknowledgements This work was supported in part by National Institutes of Health grant R01-CA-114542 (to M.-A.M.).

![](images/d75b51569301ddf8728ec61909e3fd2b583f8936ec476ccd939ea871436a79bf.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling man wearing a blue turtleneck sweater, standing in front of a display case (no visible text or symbols)
</details>

Ching-Wei Chang received his Ph.D. degree in biomedi cal engineering from the University of Michigan, Ann Arbor, in 2009. Currently, he is a postdoctoral research fellow at the University of California, Berkeley. His research interests include image processing (denoising, segmentation, and object

tracking) and the application of advanced optical methods (FRET, FLIM, 2-photon laser ablation) to cell biology.

![](images/54e56f57c5b3bf2b3871564daf6885a92207fbdce7c56484c7a4e88c3fc26d21.jpg)

<details>
<summary>natural_image</summary>

Portrait of a woman with shoulder-length brown hair against a solid blue background (no text or symbols visible)
</details>

Mary-Ann Mycek is an As sociate Professor of Biome dical Engineering at the University of Michigan. She received her Ph.D. in Phy sics from U.C. Berkeley, where she specialized in con densed matter physics and optical spectroscopy, before pursuing postdoctoral train ing in laser medicine at Har vard Medical School. Her translational research pro

gram in Biomedical Optics includes basic (pre-clinical), applied (clinical), and computational research toward quantitative, non-invasive, optical sensing and imaging in cells and tissues.

## References

[1] S. Bloch, F. Lesage, L. McIntosh, A. Gandjbakhche, K. X. Liang, and S. Achilefu, J. Biomed. Opt. 10, 054003 (2005).  
[2] S. Pelet, M. J. R. Previte, D. Kim, K. H. Kim, T. T. J. Su, and P. T. C. So, Microsc. Res. Techn. 69, 861–874 (2006).  
[3] D. Schweitzer, S. Schenke, M. Hammer, F. Schweitzer, S. Jentsch, E. Birckner, W. Becker, and A. Bergmann, Microsc. Res. Techn. 70, 410–419 (2007).  
[4] D. S. Elson, I. Munro, J. Requejo-Isidro, J. McGinty, C. Dunsby, N. Galletly, G. W. Stamp, M. A. A. Neil, M. J. Lever, P. A. Kellett, A. Dymoke-Bradshaw, J. Hares, and P. M. W. French, New J. Phys. 6, 1–13 (2004).  
[5] I. Munro, J. McGinty, N. Galletly, J. Requejo-Isidro, P. M. P. Lanigan, D. S. Elson, C. Dunsby, M. A. Neil, M. J. Lever, G. W. Stamp, and P. M. French, J. Biomed. Opt. 10, 051403 (2005).  
[6] J. Siegel, D. S. Elson, S. E. D. Webb, K. C. B. Lee, A. Vlanclas, G. L. Gambaruto, S. Leveque-Fort, M. J. Lever, P. J. Tadrous, G. W. H. Stamp, A. L. Wallace, A. Sandison, T. F. Watson, F. Alvarez, and P. M. W. French, Appl. Opt. 42, 2995–3004 (2003).  
[7] M. Y. Berezin, W. J. Akers, K. Guo, G. M. Fischer, E. Daltrozzo, A. Zumbusch, and S. Achilefu, Biophys. J. 97, L22–L24 (2009).  
[8] R. J. Goiffon, W. J. Akers, M. Y. Berezin, H. Lee, and S. Achilefu, J. Biomed. Opt. 14, 020501 (2009).  
[9] R. E. Nothdurft, S. V. Patwardhan, W. Akers, Y. Ye, S. Achilefu, and J. P. Culver, J. Biomed. Opt. , 024004 (2009).  
[10] D. Schweitzer, S. Quick, S. Schenke, M. Klemm, S. Gehlert, M. Hammer, S. Jentsch, and J. Fischer, Ophthal mologe 106, 714–722 (2009).  
[11] C. W. Chang, D. Sud, and M. A. Mycek, Methods Cell Biol. 81, 495–524 (2007).  
[12] D. Sud, G. Mehta, K. Mehta, J. Linderman, S. Takayama, and M. A. Mycek, J. Biomed. Opt. 11, 050504 (2006).  
[13] D. Sud and M. A. Mycek, J. Biomed. Opt. 14, 020506 (2009).  
[14] D. Sud, W. Zhong, D. G. Beer, and M. A. Mycek, Opt. Express 14, 4412–4426 (2006).  
[15] C. W. Chang, M. Wu, S. D. Merajver, and M. A. Mycek, J. Biomed. Opt. 14, 060502 (2009).  
[16] C. W. Chang and M. A. Mycek, Rev. Fluoresc. 2010, 173–198 (2012).  
[17] S. Pelet, M. J. Previte, and P. T. So, J. Biomed. Opt. 11, 34017 (2006).  
[18] P. R. Barber, S. M. Ameer-Beg, S. Pathmananthan, M. Rowley, and A. C. Coolen, Biomed. Opt. Express 1, 1148–1158 (2010).  
[19] K. Konig, T. W. Becker, P. Fischer, I. Riemann, and K. J. Halbhuber, Opt. Lett. 24, 113–115 (1999).  
[20] K. R. Rau, A. Guerra, A. Vogel, and V. Venugopalan, Appl. Phys. Lett. 84, 2940–2942 (2004).  
[21] L. W. Guo, O. C. Au, M. Y. Ma, and Z. Q. Liang, J. VSLI Signal Process. Systems Signal Image Video Technol. 60, 273–290 (2010).  
[22] L. W. Guo, O. C. Au, M. Y. Ma, and P. H. W. Wong, IEEE Trans. Circuits Syst. Video Technol. 20, 236–249 (2010).  
[23] C. Vonesch, Ph.D. thesis, E´ cole Polytechnique Fe´ de´ rale De Lausanne (2009).  
[24] C. Vonesch and M. Unser, IEEE Trans. Image Process. 18, 509–523 (2009).  
[25] B. Q. Spring and R. M. Clegg, J. Microsc. Oxford 235, 221–237 (2009).  
[26] C. Buranachai, D. Kamiyama, A. Chiba, B. D. Williams, and R. M. Clegg, J. Fluoresc. 18, 929–942 (2008).  
[27] A. Buades, B. Coll, and J. M. Morel, Multiscale Model. Simul. 4, 490–530 (2005).  
[28] J. Boulanger, J. B. Sibarita, C. Kervrann, and P. Bouthemy, 2008 IEEE Int. Symp. Biomed. Imag.: From Nano to Macro, Vol. 1–4 (2008), pp. 748–751.  
[29] S. Delpretti, F. Luisier, S. Ramani, T. Blu, and M. Unser, 2008 IEEE Int. Symp. Biomed. Imag.: From Nano to Macro, Vol. 1–4 (2008), pp. 149–152.  
[30] C. W. Chang and M. A. Mycek, Opt. Express 18, 8688– 8696 (2010).  
[31] C. W. Chang and M. A. Mycek, Proc. SPIE 7370, 7370091–7370096 (2009).  
[32] W. Zhong, M. Wu, C. W. Chang, K. A. Merrick, S. D. Merajver, and M. A. Mycek, Opt. Express 15, 18220– 18235 (2007).  
[33] P. Urayama, W. Zhong, J. A. Beamish, F. K. Minn, R. D. Sloboda, K. H. Dragnev, E. Dmitrovsky, and M. A. Mycek, Appl. Phys. B-Lasers and Optics 76, 483–496 (2003).  
[34] Z. Xu, M. Raghavan, T. L. Hall, C. W. Chang, M. A. Mycek, J. B. Fowlkes, and C. A. Cain, IEEE Trans. Ultrason. Ferroelectr. Freq. Control 54, 2091–2101 (2007).  
[35] P. K. Urayama, J. A. Beamish, F. K. Minn, E. A. Hamon, and M.-A. Mycek. A UV fluorescence lifetime imaging microscope to probe endogenous cellular fluorescence. in Conference on Lasers and Electro Optics (Optical Society of America, Washington D.C., 2002).  
[36] P. K. Urayama and M. A. Mycek, in: Handbook of Biomedical Fluorescence, M. A. Mycek and B. W. Po gue (Eds.) (Marcel Dekker, Inc., New York, 2003).  
[37] W. Zhong, P. Urayama, and M.-A. Mycek, J. Phys. D: Applied Physics 36, 1689–1695 (2003).  
[38] I. Bugiel, K. Ko¨ nig, and H. Wabnitz, Las. Life Sci. 3, 47–53 (1989).  
[39] X. F. Wang, T. Uchida, D. M. Coleman, and S. Minami Appl. Spectrosc. 45, 360–366 (1991).  
[40] K. K. Sharman, A. Periasamy, H. Ashworth, J. N. Demas, and N. H. Snow, Anal. Chem. 71, 947–952 (1999).  
[41] C. W. Chang, Ph.D. thesis, University of Michigan (http://deepblue.lib.umich.edu/bitstream/2027.42/ 63765/1/chingwei\_1.pdf) (2009).  
[42] C. W. Chang and M. A. Mycek, Proc. SPIE 7570, 757007 (2010).  
[43] C. W. Chang and M. A. Mycek, J. Biomed. Opt. 15, 056013 (2010).  
[44] L. I. Rudin, S. Osher, and E. Fatemi, Physica D 60, 259–268 (1992).  
[45] T. Le, R. Chartrand, and T. J. Asaki, J. Mathemat. Imag. Vision 27, 257–263 (2007).  
[46] S. Mallat, IEEE Pattern Anal. Machine Intell. 11, 674–693 (1989).  
[47] R. R. Coifman and D. L. Donoho, Lect. Notes Stat. 103, 125–150 (1995).  
[48] I. Rodrigues, J. Sanches, and J. Bioucas-Dias, 15th IEEE Int. Conf. Image Process., Vol. 1–5 (2008), pp. 1756–1759.  
[49] R. M. Willett and R. D. Nowak, 2nd IEEE Int. Symp. Biomed. Imaging: Macro to Nano, Vol. 1–2 (2004), pp. 1192–1195.  
[50] F. Luisier, C. Vonesch, T. Blu, and M. Unser, Signal Process. 90, 415–427 (2010).  
[51] A. Chambolle, Energy Minimization Methods Comput. Vis. Pattern Recognit., Proceedings, Vol. 3757 (2005), pp. 136–152.  
[52] M. A. T. Figueiredo, J. B. Dias, J. P. Oliveira, and R. D. Nowak, Proc. Int. Conf. Image Process., Vol. 1– (2006), pp. 2633–2636.  
[53] F. Rooms, W. Philips, and D. S. Lidke, J. Microsc. 218, 22–36 (2005).