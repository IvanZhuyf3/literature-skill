# A 20-year journey on the invention of vibrational photothermal microscopy

Ji-Xin Cheng

Check for updates

Vibrational microscopy opens a new window onto understanding life at the molecular level. Yet the vibrational signals from chemical bonds are weaker than the fuorescence signal from a dye by many orders of magnitude. Detecting such weak signal from a tight focus under a microscope is extremely challenging. I have devoted my career to overcoming such a daunting barrier through the development of advanced chemical microscopes over the past 25 years. In this historical Comment, I am honored to share my journey of serendipity-driven innovation and entrepreneurship in the growing feld of chemical imaging, with a focus on the invention of vibrational photothermal microscopy.

The journey toward inventing vibrational photothermal microscopy started in 2005, two years after I joined Purdue University as an assistant professor in the Weldon School of Biomedical Engineering. My team was interested in making nonlinear vibrational microscopes useful for bioimaging. In a specific project, we were investigating the mechanism of photodamage in coherent anti-Stokes Raman scattering (CARS) microscopy, of which I was a co-inventor through my postdoctoral work in Sunney Xie’s group. In 2007, we reported an unexpected result: we saw faster photodamage of samples in the presence of Raman resonance upon a prolonged excitation (Fig. 1). We further found that the enhanced photodamage was not due to CARS, but due to energy deposition into a sample through stimulated Raman gain and loss that occurs simultaneously with CARS1 .

Because energy deposition can induce photothermal and/or photoacoustic effects, this finding triggered us to build a stimulated Raman photoacoustic microscope. Because ultrasound waves encoun ter much less tissue scattering than photons, we expected to break the penetration depth limit of CARS microscopy, with the goal of in vivo detection of lipid-laden arterial plaques with this new approach. We received generous help from Song Hu in Lihong Wang’s research group and used a nanosecond optical parametric oscillator laser provided by my Purdue colleague Robert Luckt. Though we worked hard for two years, from 2007 to 2009, we found no photoacoustic signal. Accidentally, Han-Wei Wang, the first author of our Physical Review Letters paper2 , blocked the visible beam and got a photoacoustic signal from the near infrared beam. This signal made us realize that we had generated a photoacoustic signal from overtone vibrational transitions excited by the near infrared light. This study opened a new way of imaging intravascular lipids in vivo through the development of a catheter, funded by the US National Institutes of Health and American Heart Association.

![](images/f3d784821aa09829944cadcf05ab676f05f3b876021f2e096220dc1039687f60.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | CARS intensity (a.u.) |
| ------------------ | --------------------- |
| 2760               | 5.0                   |
| 2800               | 5.0                   |
| 2820               | 8.0                   |
| 2840               | 12.0                  |
| 2840               | 23.0                  |
| 2860               | 13.0                  |
| 2880               | 9.0                   |
| 2880               | 10.0                  |
| 2900               | 9.0                   |
</details>

![](images/00407d382a85639417c2aafae9ede564350cceab9e5a4eaa04094acecca3ae40.jpg)

<details>
<summary>bar chart</summary>

| Raman shift (cm⁻¹) | Time (s) |
| ------------------ | -------- |
| 2,780              | 9        |
| 2,800              | 8        |
| 2,820              | 11       |
| 2,840              | 5        |
| 2,860              | 7        |
| 2,880              | 13       |
</details>

Fig. 1 | Raman resonance-enhanced photodamage in CARS microscopy. a, CARS spectrum of a poly(ethyl-co-vinyl acetate) (PEVA) polymer film. b, Time used to induce photodamage. The pump and Stokes beam were focused onto a spot in the polymer film. Data from ref. 1.

Because of this experiment, I came to believe that the Raman effect, which relies on visible light, is not strong enough for photoacoustic or photothermal imaging. In the next few years, we started to “think out of the Raman box” — that is, we explored alternatives for a higher chance of success. The Raman scattering cross section is on the order of 10−30 cm2 per molecule, which limits the detection sensitivity to millimolar levels. Outside the box, mid-infrared absorption has a much bigger cross section: on the order of 10−20 cm2 per molecule. For certain groups, such as azide, the absorption cross section can be as large as that of the electronic absorption that generates fluorescence. Yet, unlike fluorescence emission, infrared excitation produces heat through vibrational relaxation on only the picosecond time scale. Meanwhile, heat diffusion occurs on the nanosecond to microsecond time scale following Newton’s heating and cooling law. Using a nanosecond infrared pulse train to repeatedly excite a chemical bond leads the heat to build up, causing a transient change in refractive index and thermal expansion of a particle. This photothermal effect can be probed with high sensitivity using optical detection techniques.

Though we demonstrated photoacoustic imaging of chemical bonds with near infrared light, it is sensitive only to lipid-rich plaques that are rich in C–H bonds. In the meanwhile, a 2010 Science paper by Michel Orrit’s group demonstrated visible photothermal detection of single dye molecules. Thus, we switched gears to vibrational photothermal imaging. At that time, the challenge was that we had no laser source for mid-infrared imaging, as the whole group was developing coherent Raman microscopy and near infrared photoacoustic microscopy. In 2014, while attending the SciX meeting, I was fortunate to meet founders of Block Engineering, who were looking for life science applications of their quantum cascade laser. I was also fortunate to have the strong team of Delong Zhang, Mikhail Slipchenko and Chi Zhang for the initial experiments. We built a photothermal microscope using the loaned quantum cascade laser (Fig. 2) in the corner of a table dedicated to coherent Raman microscopy. On 18 January 2015, at 2 a.m., Delong got the first signal. We then demonstrated a high-performance mid-infrared photothermal (MIP) microscope, published in 2016 in Science Advances3 . Our method, for the first time, allowed infrared mapping of specific chemical bonds inside a living cell with sub-micrometer spatial resolution.

In 2017, my group moved from Purdue to Boston University, where we have substantially expanded and matured this technology (for a review, see ref. 4) with a strong team of students and postdocs. One key project has been confocal laser-scanning MIP microscopy, in which we synchronously scan mid-infrared and photothermal probe laser beams. By a method called single pulse digitization, we realized video-rate imaging speeds5 , similar to those of confocal fluorescence. Another key focus has been wide-field MIP microscopy6 . In this camera-based method, we match the focal size between the infrared laser and the visible probe, so that all the energy can be used toward high-throughput measurement. By measuring interferometric scattering, we achieved the sensitivity to fingerprint a single virus in a wide-field manner. We further developed computational MIP microscopy via collaboration with my colleague Lei Tian. We used a technique called intensity diffraction tomography to create a 3D map of refractive indices; then, through infrared pulse modulation of the refractive indices, we achieved 3D mapping of chemical bonds in tissues and Caenorhabditis elegans.

There is a saying: your opponent can be your best friend. Though MIP was initially developed as a dye-free technique, fluorescence turns out to be a much more sensitive readout of the photothermal effect than scattering, owing to the strong temperature dependence of the fluorescence emission efficiency (quantum yield) of many common dyes. Fluorescence-detected MIP microscopy was simultaneously demonstrated by my group7 , demonstrated by Garth Simpson’s group at Purdue8 , and patented by Photothermal Spectroscopy Corp. This method opens a new door to life science applications using fluorescence as both guide and sensor.

![](images/21427e34f649746d0902e6ce27ca8af069f7d7bebefffe98d975bbb1b1faad48.jpg)

<details>
<summary>natural_image</summary>

Laboratory optical setup with mounted lenses and instruments on a perforated workbench (no visible text or symbols)
</details>

Fig. 2 | The 2014 MIP microscope in the Cheng lab based on a loaned quantum cascade laser. Behind the laser (blue box) is an optical parametric oscillator for coherent Raman microscopy.

In parallel, we have started to appreciate photothermal reporters for cell functional imaging. In the silent window (a spectral region void of biomolecular infrared absorption bands), chemical bonds like azide and nitrile give strong infrared absorption. Importantly, the diameter of a chemical bond is about one angstrom, leading to much smaller volumes than those of a fluorescent probe, and thus it can be used as a ‘GPS’ of biomolecules with minimal perturbation. In a recent article9 , we report nitrile ‘chameleons’ — chemical groups that change their color (vibration frequency) in response to the photothermal effect — as a substrate to map enzymatic activities inside living cells. Taking phosphatase as an example, when a phosphate group is removed, the peak of the nitrile vibration shifts to a new wavenumber. Thus, we can map both the substrate and the product to monitor biochemistry inside a live cell. In a separate study, we demonstrated click-chemistry-free MIP imaging of carbohydrate trafficking in live cells10. Using the strong MIP signal from azide, we were able to monitor in real time the cellular uptake of azido-trehalose, recycling to the membrane, and pole accumulation during cell division.

Though we failed in stimulated Raman photoacoustic imaging 15 years ago, we recently showed that the photothermal effect is substantial. In stimulated Raman scattering microscopy, we measure either intensity gain on the Stokes beam or intensity loss on the pump beam — but there is an energy difference between the gain and loss. In fact, stimulated Raman can be treated as a two-photon vibrational excitation process, depositing energy into the molecules. Stimulated Raman photothermal microscopy can visualize small features such as a single viral particle or a single membrane inside a cell11. More recently, we developed short-wave infrared photothermal microscopy, which extends the photothermal imaging depth to 1 mm (ref. 12). In this work, we designed an elegant experiment showing that, from the same sample, the photothermal signal can be larger than the photoacoustic signal by two orders of magnitude, partly because only 1% of the photon-induced thermal energy is further converted into the ultrasound wave for photoacoustic detection.

![](images/6d6c86d2de4c92abf27726e957ae4bd5db7f00be29943d8e06915df05350b2d6.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | Publications per year |
| :--- | :--- |
| 2016 | 23 |
| 2017 | 28 |
| 2018 | 36 |
| 2019 | 72 |
| 2020 | 116 |
| 2021 | 152 |
| 2022 | 227 |
| 2023 | 310 |
| 2024 | 441 |
</details>

Fig. 3 | Number of publications per year. Numbers are based on Google Scholar search using keywords (“mid-infrared photothermal” or “optical photothermal infrared”) and (“spectroscopy” or “imaging”). The 2016 Science Advances paper on MIP microscopy and the announcement of mIRage in 2017 trigged an exponential growth of publications. The red curve represents this growth fitted by y = 23e(x – 2016)/2.69.

Back in October 2015, I presented MIP microscopy in my Craver Award speech at the SciX meeting. I was fortunate to have Roshan Shetty and Dean Dawson (then CEO and marketing direc tor at Anasys Instruments) in the audience. After the speech, they invited me for coffee and told me that they wanted to convert our technique into a product. At the October 2017 SciX meeting, Anasys Instruments announced mIRage, an optical photothermal infra red microscope. In 2018, Photothermal Spectroscopy Corp. was founded to further develop and commercialize optical photothermal microscopy.

This entrepreneurial success has enabled broad applications far beyond my own research. For example, the Klementieva group at Lund University is using mIRage to study protein aggregation in Alzheimer’s disease. In China, Nanjing University used mIRage to detect nanoplastics. The Davis group at Yale is using mIRage to visualize metabolism in live cells. On the industrial side, leading companies are using mIRage to characterize contaminants and defects in semiconductor, data storage and display applications.

Photothermal spectroscopy appeared in the 1970s as an ultrasensitive absorption spectroscopy13. In 1983, a French group proposed the concept of photothermal imaging based on the change of refractive index — that is, the mirage effect14. The initial effort of photothermal infrared imaging with a quantum cascade laser was reported at a 2012 Society of Photo-Optical Instrumentation Engineers conference15. We were fortunate to enter the field at the right time. With over 10 years of experience in pushing the physical limits of coherent Raman microscopy, we had accumulated all the expertise needed to build a high-performance MIP microscope and demonstrate live-cell imaging with sub-micrometer spatial resolution. Meanwhile, the strong expertise in infrared nanospectroscopy at Anasys Instruments and the maturity of the quantum cascade laser technology allowed rapid commercialization of our method into a real mIRage product for worldwide use.

Looking back, I had never thought that the unexpected observation of photodamage back in 2005 and the initial development of MIP in the basement of a lab at Purdue University (which sits in the middle of a huge corn field) would grow vibrational photothermal microscopy into a rising technique in chemical imaging (Fig. 3). The developments were exclusively driven by curiosity and passion, and achieved with hard work and financial support. I am happy to summarize this journey in a poem for next-generation tool developers:

A small seed can grow into a big tree. It may take years and persistence is the key. How to find and grow a seed? Pay attention to unexpected scene, and with no fear to enter a new discipline.

## Ji-Xin Cheng

Department of Biomedical Engineering, Department of Electrical and Computer Engineering, Photonics Center, Boston University, Boston, MA, USA.

e-mail: jxcheng@bu.edu

Published online: 13 May 2025

## References

1. Wang, H., Fu, Y. & Cheng, J. X. J. Opt. Soc. Am. B 24, 544–552 (2007).  
2. Wang, H. W. et al. Phys. Rev. Lett. 106, 238106 (2011).  
3. Zhang, D. et al. Sci. Adv. 2, e1600521 (2016).  
4. Xia, Q., Yin, J., Guo, Z. & Cheng, J.-X. J. Phys. Chem. B 126, 8597–8613 (2022)  
5. Yin, J. et al. Sci. Adv. 9, eadg8814 (2023).  
6. Bai, Y. et al. Sci. Adv. 5, eaav7127 (2019).  
7. Zhang, Y. et al. J. Am. Chem. Soc. 143, 11490–11499 (2021).  
8. Li, M. et al. J. Am. Chem. Soc. 143, 10809–10815 (2021).  
9. He, H. et al. Nat. Methods 21, 342–352 (2024).  
10. Xia, Q. et al. Sci. Adv. 10, eadq0294 (2024)  
11. Zhu, Y. et al. Sci. Adv. 9, eadi2181 (2023).  
12. Ni, H. et al. Nat. Photonics 18, 944–951 (2024).  
13. Long, M. E., Swoford, R. L. & Albrecht, A. C. Science 191, 183–185 (1976).  
14. Fournier, D., Lepoutre, F. & Boccara, A. C. J. Phys. (Paris) 44, C6–C479 (1983).  
15. Furstenberg, R., Kendziora, C. A., Papantonakis, M. R., Nguyen, V. & McGill, R. A. Proc. SPIE 8374, 837411 (2012).

## Acknowledgements

I am grateful for the hard work by dedicated postdoctoral fellows and graduate students in my group over the past years. Many thanks to collaborators and industrial partners. Lacknowledge the NIH. NSE. DoD. DoE. Veterans Affairs. Kech Foundation. American Hear Association, Chan-Zuckerburg Initiative and DRS Daylight Solutions for their financial support

## Competing interests

J.-X.C. claims financial interests with Vibronix Inc and Photothermal Spectroscopy Corp, which did not fund this work.