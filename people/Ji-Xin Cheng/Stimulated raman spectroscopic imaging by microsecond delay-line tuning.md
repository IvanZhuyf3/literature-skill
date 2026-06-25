# Stimulated Raman Spectroscopic Imaging by Microsecond Delay-line Tuning

Chien-Sheng Liao1, Kai-Chih Huang1, Weili Hong1, Jing Chen2, Karanja Caroline3, Gregory Eakins3, and Ji-Xin Cheng1,3,4,5,6

1Weldon School of Biomedical Engineering, 2Department of Biological Sciences, 3Department of Chemistry, 4Purdue University Center for Cancer Research, 5Birck Nanotechnology Center, 6School of Electrical and Computer Engineering, Purdue University, West Lafayette, IN 47907, USA jcheng@purdue.edu

Abstract: We report microsecond-scale acquisition of simulated Raman spectra by resonant delay-line tuning. Our scheme improved the spectral acquisition speed by 100 times compared to previous works by motorized translational-stage tuning. 4-D images (x-y-z-λ) from highly dynamic organelles in live C. elegans was demonstrated. OCIS codes: (170.5660) Raman spectroscopy; (180.4315) Nonlinear microscopy

Coherent Raman imaging techniques, including coherent anti-Stokes Raman scattering (CARS) and stimulated Raman scattering (SRS), are powerful tools to visualize the spatial distribution of molecules in cells or tissues [1, 2]. To resolve overlapped Raman bands in biological samples, there has been a great effort in developing spectroscopic coherent Raman imaging technology. Spectral scanning of a narrowband laser pulse and collection of images at a series of Raman shifts has been demonstrated to reach real-time imaging speed [3-7]. However, the limited temporal resolution of each spectroscopic stack on second scale tends to distort spectral profiles from highly dynamic organelles in live cells or animals. Multiplex CARS by a broadband excitation pulse and a narrowband probe pulse has been demonstrated to simultaneously excite multiple Raman bands and detect spectrally dispersed vibrational signals with a pixel dwell time as short as 3 milliseconds  [8]. Recently multiplex  [9] and frequencymultiplexing [10] SRS further reached microsecond spectral acquisition and enabled real-time spectroscopic imaging [9, 10]. Nevertheless, the use of the broadband pump and narrowband Stokes pulses requires sophisticated pulse shaping techniques in which most of bandwidth of a femtosecond pulse is not used for the narrowband Stokes pulses. One efficient way to utilize the bandwidth of femtosecond pulses for spectroscopic measurement is to linearly chirp the pump and Stokes pulses and focus their entire bandwidth into a narrow spectral region [11]. Therefore each temporal delay between the chirped pulses corresponds to a Raman shift (Fig. 1(a)). By scanning the delay-line of one pulse and recording a series of images, SRS spectroscopic imaging based on this spectral focusing scheme has been demonstrated with a total acquisition time of several tens of seconds [12, 13]. This imaging speed is mostly limited by the waiting time for stabilization and communication of a motorized translational stage used for delay-line tuning.

In this work, we demonstrate stimulated Raman spectroscopic imaging using a lab-built microsecond delay tuner (Fig. 1(b)). By directing the collimated light to the edge of a tilted resonant mirror with a few kHz central frequency, and focusing the reflected light with a lens on a flat mirror, the retroreflected light experienced a millimeter-scale difference in optical path when the resonant mirror was scanned in one cycle of tens of microseconds. This method was first demonstrated for optical coherence tomography  [14] and more recently applied to Fourier transform CARS spectroscopy  [15]. Here we implement a 12-kHz resonant mirror to scan the temporal delay between two chirped pulses for SRS spectroscopic imaging. By synchronization of the resonant mirror with galvo-mirrors used for imaging scan, we collected an SRS spectrum, covering \~200 cm-1 determined by the excitation pulse within 83 μs at each pixel of an image. Our scheme improved the SRS spectral acquisition speed by 100 times compared to previous work using motorized stage tuning [13]. We successfully acquired  4-D (x-y-z-) SRS spectroscopic images from highly dynamic organelles in live C. elegans.

![](images/5f46c2e83a4e38a7df982c740c3bc1d49210d4e4211212fa8b01bfe0c2dd4306.jpg)

Fig. 1. Concept and setup of SRS spectroscopic imaging by microsecond delay-line tuning. (a) Each temporal delay between the chirped pump and Stokes corresponds to a molecular vibrational mode. (b) Setup. AOM: Acousto-optic modulator; C: Condenser; F: Filter; HWP: Half waveplate; OBJ: Objective; PBS: Polarizing beam splitter; PD: Photodiode; QWP: Quarter waveplate; TAMP: Tuned amplifier

We applied our technique to C. elegans, an intact multicellular animal that is extensively used for studying the impact of lipid metabolism on aging and disease. Single color CRS imaging using C-H vibrational region has been demonstrated to visualize the lipid storage. SRS spectroscopic imaging has been applied to identify and quantify lipid compartments at a cross-section of C. elegans based on the Raman region from 1620 to 1800 cm-1, where the ratio of acyl C=C bond at 1655 cm-1 to ester C=O bond at 1745 cm-1 were used to identify different compartments [16]. However, C. elegans usually has several tens of micrometers in thickness. Therefore 3-D chemical mapping of the lipid compartments is necessary to quantify the fat storage. Here we demonstrate 4-D (x-y-z-λ) SRS images of anesthetized C. elegans in fingerprint region and resolved fat storage from LROs and protein in fingerprint spectral window. Each spectroscopic image composed of 170x1700 pixels was collected within 25 seconds, and 12 depth-resolved images were acquired with a 2 μm step size tuned manually by the microscope stage. The 4-D spectroscopic image stack was denoised and decomposed by MCR analysis. Fig. 2(a) showed the depth-resolved chemical maps of fat storage, LROs and protein, with their corresponding MCR spectral outputs (Fig. 2(b)). Further 3-D chemical visualization of the C. elegans can resolve fat storage in intestinal cells over the whole worm body.

In conclusion, we have demonstrated real-time SRS spectroscopic imaging based on microsecond delay-line tuning. The SRS spectrum at each pixel was acquired within 83 μs, covering 200 cm  spectral window with 25 cm  spectral resolution. The speed advantage allows chemical imaging of highly dynamic systems and 3-D mapping of fat storage in live C. elegans. Collectively, the presented efforts pushes Raman spectroscopy that is conventionally used for chemical imaging of fixed specimens towards compositional mapping of live intracellular compartments.

![](images/09f303fff4eedd498f95252c5c58adaab943ecf9e0acbdba19d2d6edd29ca4e2.jpg)

<details>
<summary>natural_image</summary>

Microscopic fluorescence images of a biological sample at three different thicknesses (0 μm, 8 μm, 14 μm), showing red and green cellular structures with scattered yellow fluorescent spots.
</details>

![](images/5fe35963f80511bb1e2666269e710f17239422a1b1ed93dd1f0ccb46b64717a4.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | Fat droplet | LRO | Protein |
| ------------------ | ----------- | --- | ------- |
| 1800               | 0.0         | 0.0 | 0.0     |
| 1750               | 0.2         | 0.05| 0.0     |
| 1700               | 0.3         | 0.3 | 0.1     |
| 1650               | 0.35        | 0.35| 0.15    |
| 1600               | 0.0         | 0.0 | 0.0     |
</details>

Figure 2. SRS spectroscopic images of C. elegans at 0, 8 and 14 μm depths from the surface. (a) MCR output concentration map at the depth of 0, 8 and 14 μm from the surface. (b) MCR output spectra. Scale bar: 30 μm

## 4. References

1. A. Zumbusch, G. R. Holtom, and X. S. Xie, Phys. Rev. Lett. 82, 4142-4145 (1999).  
2. C. W. Freudiger, W. Min, B. G. Saar, S. Lu, G. R. Holtom, C. He, J. C. Tsai, J. X. Kang, and X. S. Xie, Science 322, 1857-1861 (2008).  
3. C. Y. Lin, J. L. Suhalim, C. L. Nien, M. D. Miljkovic, M. Diem, J. V. Jester, and E. O. Potma, J. Biomed. Opt. 16, 021104 (2011).  
4. E. T. Garbacik, J. L. Herek, C. Otto, and H. L. Offerhaus, J. Raman Spectrosc. 43, 651-655 (2012).  
5. Y. Ozeki, W. Umemura, Y. Otsuka, S. Satoh, H. Hashimoto, K. Sumimura, N. Nishizawa, K. Fukui, and K. Itoh, Nature Photon. 6, 844-850 (2012).  
6. D. L. Zhang, P. Wang, M. N. Slipchenko, D. Ben-Amotz, A. M. Weiner, and J. X. Cheng, Anal. Chem. 85, 98-106 (2013).  
7. F. Masia, A. Glen, P. Stephens, P. Borri, and W. Langbein, Anal. Chem. 85, 10820-10828 (2013).  
8. C. H. Camp, Y. J. Lee, J. M. Heddleston, C. M. Hartshorn, A. R. H. Walker, J. N. Rich, J. D. Lathia, and M. T. Cicerone, Nature Photon. 8, 627-634 (2014).  
9. C.-S. Liao, M. N. Slipchenko, P. Wang, J. Li, S.-Y. Lee, R. A. Oglesbee, and J.-X. Cheng, Light Sci. Appl. 4, e265 (2015).  
10. C.-S. Liao, P. Wang, P. Wang, J. Li, H. J. Lee, G. Eakins, and J.-X. Cheng, Sci. Adv. 1, e1500738 (2015).  
11. T. Hellerer, A. M. K. Enejder, and A. Zumbusch, Appl. Phys. Lett. 85, 25-27 (2004).  
12. D. Fu, G. Holtom, C. Freudiger, X. Zhang, and X. S. Xie, J. Phys. Chem. B 117, 4634-4640 (2013).  
13. B. Liu, H. J. Lee, D. L. Zhang, C. S. Liao, N. Ji, Y. Q. Xia, and J. X. Cheng, Appl. Phys. Lett. 106(2015).  
14. X. M. Liu, M. J. Cobb, and X. D. Li, Opt. Lett. 30, 1744-1744 (2005).  
15. K. Hashimoto, M. Takahashi, T. Ideguchi, and K. Goda, Sci Rep-Uk 6(2016).  
16. P. Wang, B. Liu, D. L. Zhang, M. Y. Belew, H. A. Tissenbaum, and J.-X. Cheng, Angew. Chem. Int. Edit 53, 11787-11792 (2014).