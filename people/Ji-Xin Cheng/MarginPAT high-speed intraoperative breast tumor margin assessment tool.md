# MarginPAT: High-Speed Intraoperative Breast Tumor Margin Assessment Tool

Lu Lan1, Rui Li1, Pu Wang2, and Ji-Xin Cheng1,3,\*

1Weldon School of Biomedical Engineering, Purdue University, 206 S Martin Jischke Dr., West Lafayette, Indiana, 47907, USA

2Vibronix, Inc., 1281 Win Hentschel Blvd., West Lafayette, Indiana, 47906, USA

3Department of Chemistry, Purdue University, 560 Oval Drive, West Lafayette, Indiana, 47907, USA

Abstract: As lumpectomy is well accepted for the breast cancer treatment, a highly sensitive tool is critically needed for intraoperative margin assessment. We present a multi-modal photoacoustic/ultrasound imaging system for high-speed high-sensitivity intraoperative margin assessment.

OCIS codes: (110.5120) General; (000.0000) General

## 1. Introduction

Each year, there are \~240,000 newly breast cancer cases in United States, 70% of which are eligible and undergo breast-conserving surgery, or lumpectomy1. Due to a lack of a rapid and highly sensitive tool for intraoperative margin assessment, 20-40% of the patients require a second operation to completely remove all the tumor tissue2-6. The current cost of one lumpectomy procedure (physician cost excluded) for the provider is \~\$4200 7. Such problem causes additional surgical expense (\$800-\$1700 per case) and the emotional distress and physical pain of the patients. There are multiple intraoperative imaging tools existing or emerging for breast tumor margin assessment. Cytological examination and frozen section are widely applied clinically, but they suffer from long procedure time and low sensitivity (70%) owning to the sampling method8-11. Radio frequency spectroscopy reduces the procedure time, but still suffers from the sensitivity (70%) and specificity (68%) due to the lack of chemical selectivity12,13. Intraoperative x-ray is routinely used in lumpectomy and it provides fast whole tissue assessment (result comes in 1 min). But it has very low sensitivity (60%). Therefore, an unmet need exists in developing an intraoperative margin assessment device that is 1) rapid, 2) sensitive, 3) label-free, 4) able to measure the entire tissue surface, and 5) with 2 mm or more imaging depth.

We present a multi-modal photoacoustic/ultrasound imaging system, namely the MarginPAT system, for rapid and highly sensitive breast cancer margin assessment. This system will be used in an operating room (OR). After surgeon removes the tumor, the tissue will be transferred to a cartridge and inserted to the MarginPAT system. Through a <3 min automatic scanning, the MarginPAT system will provide a 3D images of the excised tissue, which provide the margin status. Surgeon can choose to have a reoperation immediately or let the patient go home based on the results from MarginPAT. With such immediate feedback, the MarginPAT can effectively reduce the re-operation rate. In our preliminary study on 40 patient samples, we showed 93% sensitivity and 90% specificity in margin assessment by precise localization of adipose tissue using PA imaging and further RF spectrum analysis of ultrasound signal. Other than the superior sensitivity and specificity, the unique features of MarginPAT include (1) deep tissue sensing (> 3 mm), (2) high speed (20 cm2 area per min), and (3) free from exogenous labeling. Those specifications exactly match the requirement of intraoperative margin assessment, which is beyond the reach by other emerging platforms like Raman spectroscopy. More importantly, MarginPAT inherently supports the conventional ultrasound imaging function, which is commonly used in pre-operation diagnosis and wire localization procedure 14. Therefore, the same MarginPAT system can be applied to multiple areas in the management of breast cancer diseases. This feature brings another key advantage over the other emerging technologies.

## 2. Results and Discussions

Fig. 1A shows the system configuration. Fig. 1B shows a Ba(NO ) Raman laser system. The system was able to generate an output at 1197 nm with the pulse energy of 120 mJ, which was 2 times higher than the OPO laser source reported 15,16, but 70% smaller in volume, and 70% cheaper. The laser was coupled into an optical fiber bundle which was stabilized in parallel with the ultrasound transducer (Fig. 1C). To enable the assessment of the entire excised tissue surface, we applied a two-axis translational stages for raster scanning (Fig. 1C). The US and PA signal were recorded by a transducer array with 128 elements and 18 MHz center frequency (50% bandwidth) (L22-14v, Verasonics Inc.), and then processed by a high-frequency US imaging system (Vantage, Verasonics Inc.). Data acquisition and laser pulse generation was synchronized, and a dual-mode b-scan US and PA images can be acquired in 0.1 s. Imaging of a tungsten wire phantom indicated that a resolution of \~100 µm and 150 µm for US and PA mode, respectively, was achieved. With this compact laser and the scanning system, we constructed a MarginPAT system (Fig. 1D) and transported this system to a surgical suite.

![](images/32e674bb460e80bc6d8eb8e2a83c47c6d92eb9725c702f60baec3827a2e43b9a.jpg)  
Figure 1: Schematic of multispectral photoacoustic tomography system. (A) Experimental setup of multispectral photoacoustic tomography platform. (B) Photograph of a Raman laser system. PBS: Polarized beam splitter; HWP: Half wave plate. (C) Schematics of the scanning system. (D) The photograph of the compact MarginPAT system.

By PA imaging at 1200 nm excitation and RF spectrum analysis of US signal to differentiate normal and cancer tissue, we examined 40 samples (13 DCIS samples, 27 IDC samples) from tissue bank using MarginPAT device. Cross validation of these samples was performed by histopathology analysis. Fig. 2 shows 5 representative image sets with ultrasound images, PA images at 1200 nm, US images after RF analysis, and the histology images. The greyscale US images (first column) showed the morphology of the tissue. The PA images at 1200 nm clearly mapped the adipose tissue distribution inside tissue which is the direct marker of normal tissue. This contrast was confirmed by the histology. Although the PA signal disappeared after 3 mm, it is more than enough for margin assessment in excised tissue. To further enhance the US contrast, RF spectrum analysis of the US signal was applied. A Gaussian window (0.4mm width) was used to slide along each A-line of US images to extract the RF data, which was then Fourier transformed to produce RF spectra. Using K-means clustering classification method on such RF spectra, tissues were classified into three types in the US images: non-cancerous type 1, non-cancerous type 2 and cancerous tissue. We then combined the PA contrast as the primary classifier of the non-cancerous type, and generate a processed cancer map (the $3 ^ { \mathrm { r d } }$ column), where the green indicated the normal and the red indicates the cancerous tissue. This classification results correlated with the histology very well. By comparing with the histology reading of all 40 samples, the sensitivity of 93% and specificity of 90% is achieved  (Table 1). Specifically, the sensitivity and specificity for IDC is 96% and 100%, and that of DCIS is 86% and 83%, respectively. We have tested the MarginPAT system (Fig. 1D) in IU Health Simon cancer center. Fig. 3 shows the results for a freshly excised breast cancer tissue. The upper left image is the photograph of the excised tissue $( 6 \mathrm { ~ x ~ } 8 \mathrm { ~ x ~ } 3 \mathrm { ~ c m } ^ { 3 } )$ . It took 5 min to finish the scanning of one side of the surface. The lower left shows the processed 3D image where green indicates the normal tissue and red indicates the red (the red shade is due to the transparency setting in the rendering). By looking the orthogonal view of the image, we see a close margin (less than 1 mm) which exact match the histopathology report. This result suggests the feasibility of using MarginPAT for rapid margin assessment with high fidelity to the histopathology.

![](images/f2be663026efd7ee3fa8d65ab8b0ff41fffcfe3d2c31595d903c54f2765ff9b9.jpg)

<details>
<summary>text_image</summary>

Ultrasound
PA
RF analysis + PA
Histology
3 mm
3 mm
3 mm
2 mm
2 mm
Adipose tissue
Fibrosis tissue
Solid tumor
Cancer infiltration to adipose tissue
Negative
Positive
</details>

Figure 2: Representative MarginPAT imaging in 5 fresh breast tumor tissues excised from human patients.

Table 1: Sensitivity and specificity of MarginPAT

<table><tr><td>Breast tumor tissue #</td><td colspan="2">40</td></tr><tr><td></td><td>Histology positive</td><td>Histology negative</td></tr><tr><td>MarginPAT positive</td><td>28</td><td>1</td></tr><tr><td>MarginPAT negative</td><td>2</td><td>9</td></tr><tr><td colspan="3"></td></tr><tr><td>Invasive ductal carcinoma</td><td colspan="2">27</td></tr><tr><td></td><td>Histology positive</td><td>Histology negative</td></tr><tr><td>MarginPAT positive</td><td>22</td><td>0</td></tr><tr><td>MarginPAT negative</td><td>1</td><td>4</td></tr><tr><td colspan="3"></td></tr><tr><td>Ductal carcinoma in situ</td><td colspan="2">13</td></tr><tr><td></td><td>Histology positive</td><td>Histology negative</td></tr><tr><td>MarginPAT positive</td><td>6</td><td>1</td></tr><tr><td>MarginPAT negative</td><td>1</td><td>5</td></tr></table>

![](images/8ce397a0730e30db6e14648c60068e252c5126768b7a3703656c63c3c5699715.jpg)

<details>
<summary>natural_image</summary>

Close-up of a biological specimen with scale markings (8 cm and 6 cm) showing internal tissue structure (no text or symbols on the specimen itself)
</details>

![](images/2be0c20b7e9a6686abbea51ae8da48252f45c6f6dd2cf68b3e9bd90033eecdd6.jpg)

<details>
<summary>natural_image</summary>

3D medical image of a resected tissue with color-coded regions (no text or symbols)
</details>

![](images/5f73c71de17582a623dbc6e1a1a4fcbe0035386960004a85d0264c6e63bd578a.jpg)

<details>
<summary>text_image</summary>

Image shows close margin
less than 1 mm
</details>

Figure 3: 3D image of the entire surface using MarginPAT. Green: the normal tissue. Red: tumor tissue.

## 3. References

(1) Brown, J. Q.; Bydlon, T. M.; Richards, L. M.; Yu, B.; Kennedy, S. A.; Geradts, J.; Wilke, L. G.; Junker, M. K.; Gallagher, J.; Barry, W. T.; Ramanujam, N. Optical Assesssment of Tumor Resection Margins in the Breast. Ieee J Sel Top Quant 2010, 16, 530-544.  
(2) Jacobs, L. Positive margins: The challenge continues for breast surgeons. Annals of surgical oncology 2008, 15, 1271-1272.  
(3) Atkins, J.; Al Mushawah, F.; Appleton, C. M.; Cyr, A. E.; Gillanders, W. E.; Aft, R. L.; Eberlein, T. J.; Gao, F.; Margenthaler, J. A. Positive margin rates following breast-conserving surgery for stage I-III breast cancer: palpable versus nonpalpable tumors. J Surg Res 2012, 177, 109- 115.  
(4) Balch, G. C.; Mithani, S. K.; Simpson, J. F.; Kelley, M. C. Accuracy of intraoperative gross examination of surgical margin status in women undergoing partial mastectomy for breast malignancy. The American surgeon 2005, 71, 22-27; discussion 27-28.  
(5) Fleming, F. J.; Hill, A. D.; Mc Dermott, E. W.; O'Doherty, A.; O'Higgins, N. J.; Quinn, C. M. Intraoperative margin assessment and reexcision rate in breast conserving surgery. European journal of surgical oncology : the journal of the European Society of Surgical Oncology and the British Association of Surgical Oncology 2004, 30, 233-237.  
(6) Huston, T. L.; Pigalarga, R.; Osborne, M. P.; Tousimis, E. The influence of additional surgical margins on the total specimen volume excised and the reoperative rate after breast-conserving surgery. American journal of surgery 2006, 192, 509-512.  
(7) Osborn, J. B.; Keeney, G. L.; Jakub, J. W.; Degnim, A. C.; Boughey, J. C. Cost-effectiveness analysis of routine frozen-section analysis of breast margins compared with reoperation for positive margins. Annals of surgical oncology 2011, 18, 3204-3209.  
(8) Riedl, O.; Fitzal, F.; Mader, N.; Dubsky, P.; Rudas, M.; Mittlboeck, M.; Gnant, M.; Jakesz, R. Intraoperative frozen section analysis for breast-conserving therapy in 1016 patients with breast cancer. European journal of surgical oncology : the journal of the European Society of Surgical Oncology and the British Association of Surgical Oncology 2009, 35, 264-270.  
(9) Cendan, J. C.; Coco, D.; Copeland, E. M., 3rd. Accuracy of intraoperative frozen-section analysis of breast cancer lumpectomy-bed margins. Journal of the American College of Surgeons 2005, 201, 194-198.  
(10) D'Halluin, F.; Tas, P.; Rouquette, S.; Bendavid, C.; Foucher, F.; Meshba, H.; Blanchot, J.; Coue, O.; Leveque, J. Intra-operative touch preparation cytology following lumpectomy for breast cancer: a series of 400 procedures. Breast 2009, 18, 248-253.  
(11) Creager, A. J.; Shaw, J. A.; Young, P. R.; Geisinger, K. R. Intraoperative evaluation of lumpectomy margins by imprint cytology with histologic correlation: a community hospital experience. Archives of pathology & laboratory medicine 2002, 126, 846-848.  
(12) Thill, M. MarginProbe®: intraoperative margin assessment during breast conserving surgery by using radiofrequency spectroscopy. Expert Review of Medical Devices 2013, 10, 301-315.  
(13) Thill, M.; Dittmer, C.; Baumann, K.; Friedrichs, K.; Blohmer, J. U. MarginProbe(R)--final results of the German post-market study in breast conserving surgery of ductal carcinoma in situ. Breast 2014, 23, 94-96.  
(14) Rahusen, F. D.; Bremers, A. J.; Fabry, H. F.; van Amerongen, A. T.; Boom, R. P.; Meijer, S. Ultrasound-guided lumpectomy of nonpalpable breast cancer versus wire-guided resection: a randomized clinical trial. Annals of surgical oncology 2002, 9, 994-998.  
(15) Li, R.; Slipchenko, M. N.; Wang, P.; Cheng, J. X. Compact high power barium nitrite crystal-based Raman laser at 1197 nm for photoacoustic imaging of fat. Journal of biomedical optics 2013, 18.  
(16) Wang, P.; Rajian, J. R.; Cheng, J. X. Spectroscopic Imaging of Deep Tissue through Photoacoustic Detection of Molecular Vibration. J Phys Chem Lett 2013, 4, 2177-2185.