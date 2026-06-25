# Accelerated Stimulated Raman Projection Tomography by Sparse Reconstruction from Sparse-View data

Xueli Chen\*, Member, IEEE, Shouping Zhu, Member, IEEE, Huiyuan Wang, Cuiping Bao, Defu Yang, Chi Zhang, Peng Lin, Ji-Xin Cheng, Yonghua Zhan, Jimin Liang, and Jie Tian, Fellow, IEEE

Abstract—Objective: Stimulated Raman projection tomography (SRPT), a recently developed label-free volumetric chemical imaging technology, has been reported to quantitatively reconstruct the distribution of chemicals in a three-dimensional (3D) complex system. The current image reconstruction scheme used in SRPT is based on a filtered back projection (FBP) algorithm that requires at least 180 angular-dependent projections to rebuild a reasonable SRPT image, resulting in a long total acquisition time. This is a big limitation for longitudinal studies on live systems. Methods: We present a sparse-view data-based sparse reconstruction scheme, in which sparsely sampled projections at 180 degrees were used to reconstruct the volumetric information. In the scheme, the simultaneous algebra reconstruction technique (SART), combined with total variation regularization, was used for iterative reconstruction. To better describe the projection process, a pixel vertex driven model (PVDM) was developed to act as projectors, whose performance was compared with those of the distance driven model (DDM). Results: We evaluated our scheme with numerical simulations and validated it for SRPT by mapping lipid contents in adipose cells. Simulation results showed that the PVDM performed better than the DDM in the case of using sparse-view data. Our scheme could

Manuscript received August 29, 2018; revised May 12, 2019; accepted August 10, 2019. This work was supported in part by the National Key R&D Program of China under Grant 2018YFC0910602, in part by the National Natural Science Foundation of China under Grant Nos. 81627807, 11727813, 81871397, and 81571725, in part by the Fok Ying-Tong Education Foundation of China under Grant 161104, in part by the Youth Talent Support Program in Shaanxi Province, in part by Research Fund for Young Star of Science and Technology in Shaanxi Province (2018KJXX- 018), in part by the Best Funded Projects of the Scientific and Technological Activities for Excellent Overseas Researchers in Shaanxi Province (2017017), in part by the Fundamental Research Funds for the Central Universities (JB181203), and in part by a Keck Foundation grant and a National Institutes of Health (NIH) R01 grant GM118471. Asterisks indicate corresponding authors. X. Chen and S. Zhu contributed equally to this work.

X. Chen, S. Zhu, H. Wang, C. Bao, and J. Liang are with the Engineering Research Center of Molecular and Neuro Imaging of Ministry of Education and School of Life Science and Technology, Xidian University, Xi’an, Shaanxi 710126, China (e-mail: xlchen@xidian.edu.cn).

D. Yang is with the Institute of Information and Control, Hangzhou Dianzi University, Hangzhou 310018, China

J. Tian is with the Engineering Research Center of Molecular and Neuro Imaging of Ministry of Education and School of Life Science and Technology, Xidian University, Xi’an, Shaanxi 710126, China. J. Tian is also with Institute of Automation, Chinese Academy of Science, Beijing 100190, China.

C. Zhang, P. Lin, and J.X. Cheng were with the Weldon School of Biomedical Engineering, Purdue University, West Lafayette, Indiana 47907, USA. They are now with the Department of Electrical and Computer Engineering/Biomedical Engineering, Boston University, Boston, MA 02215 USA.

maintain the quality of the reconstructed images even when the projection number was reduced to 15. The cell-based experimental results demonstrated that the proposed scheme can improve the imaging speed of the current FBP-based SRPT scheme by a factor of 9-12 without sacrificing discernible imaging details. Conclusion: Our proposed scheme significantly reduces the total acquisition time required for SRPT at a speed of one order of magnitude faster than the currently used scheme. This significant improvement in imaging speed would potentially promote the applicability of SRPT for imaging living organisms.

Index Terms—Sparse reconstruction, iterative reconstruction, stimulated Raman projection, tomography

## I. INTRODUCTION

HE ability to analyze the components in the whole volume of a three-dimensional (3D) system, such as a cell, tissue or a living organism, has great value for cell machinery, quantitative biology, and systems neuroscience [1]-[5]. Such ability enables volumetric imaging techniques to be applied for quantitative and global measurements in a living organism, and to facilitate consistency in observations for longitudinal imaging. A number of imaging techniques have been developed to image the 3D volume of an entire object. Fluorescence microscopy through a confocal or a multiphoton approach provides good sectioning capability with high axial resolution [6], [7]. Such sectioning method requires tightly focused laser beams to acquire an image stack for 3D reconstruction, which can be time-consuming [1]. Light-sheet microscopy (LSM) overcame this limitation by passing a thin plane of light through the sample to generate planar imaging slices [8], [9]. Providing high resolution images with high speed, LSM enables the dynamic, long-term, and 3D imaging of the specimens ranging from single cells to whole embryos [10]-[13]. However, this method has the potential degenerate the image quality when the distance between the sample surface and the objective increases [14]. Optical projection tomography (OPT) can eliminate the image quality deterioration induced in LSM by rotating the sample by 360 degrees around an axis perpendicular to the light path [14]. OPT can produce a 3D image of a specimen with high-isotropic spatial resolution, and the size of the specimen can be up to several millimeters [1], [15]-[19]. Although the abovementioned fluorescence based volumetric imaging techniques are powerful for quantifying cellular proteins or DNA, they are not suitable to analyze cellular metabolites. The fluorescent labeling has low specificity to label distinct metabolites and can strongly perturb biological functions [2]. Therefore, a label-free volumetric imaging approach that can image a 3D volume in a chemically-selective manner is needed.

Based on the Raman scattering effect that reflects fingerprint information of chemical bond vibrations, spontaneous Raman microscopy can map the chemical composition of a sample in a label-free manner [20], [21]. It possesses high-specificity to image cell metabolites in biological samples [21]. However, spontaneous Raman scattering is a weak process, preventing its applications on a large volume even when implemented via a light-sheet or tomography [2], [22]-[30]. The low signal levels block the imaging speed and the strong emission of autofluorescence might hamper or even overwhelm the weak Raman signals [22]. On the other hand, Raman tomography provides low spatial resolution at the scale of millimeters because of the physical nature of the diffused light transport in the medium [31]. Coherent Raman scattering microscopy, including coherent anti-Stokes Raman scattering (CARS) and stimulated Raman scattering (SRS) microscopy [2], [32]-[36], have been reported to enhance the low levels of the Raman signal and prevent strong autofluorescence. However, these Raman-mediated approaches are still subject to the same problems as with confocal-based sectioning imaging for the volumetric chemical imaging. Recently, we reported a stimulated Raman projection tomography (SRPT) method to enable high-speed volumetric chemical imaging of 3D complex systems [37]. This imaging technology utilized Bessel beams to excite molecular vibrations through the SRS process and provided identical spectral information as that of the spontaneous Raman spectroscopy while significantly improved the imaging speed. We have demonstrated that SPRT can be applied to perform 3D imaging of lipid contents in adipose cells within 3 min.

In SRPT, the Bessel beams were scanned in two dimensions to obtain stimulated Raman projection (SRP) images. A series of projection images as a function of the sample rotation angle were used to recover the chemical distribution in a 3D sample volume. The current image reconstruction scheme used in SRPT is based on a filtered back projection (FBP) algorithm. The FBP requires a minimum of 180 angular-dependent projections to reconstruct a reasonable SRPT image. Such a high number of projection images prevent further improvement of the imaging speed. Therefore, it is highly desirable to reduce the required number of projections to decrease both the total acquisition time and the excitation light dose to the sample for longitudinal studies of living systems. In this work, we present a sparse-view data-based sparse reconstruction scheme to accelerate the imaging speed of SRPT by using the sparsely sampled projections at 180 degrees to reconstruct the volumetric information of a specimen. In the scheme, the simultaneous algebra reconstruction technique (SART), combined with total variation (TV) regularization, was used for iterative reconstruction. TV regularization-based reconstruction methods are popular in field of sparse-view or few-view computed tomography [38]-[42]. To better describe the projection process, a pixel vertex driven model (PVDM)

that was borrowed from the separable footprint model [43] was developed and used as the projectors. The PVDM was specially modified to make it more suitable for the parallel beam based SRPT, and its performance superiority was then demonstrated by comparing with the distance driven model (DDM). The performance of the proposed scheme was first evaluated with a series of numerical simulations and then its potential for SRPT application was exemplified by mapping lipid contents in adipose cells. Our results collectively demonstrate that the proposed scheme can reconstruct SRPT images with much fewer projections than using the FBP algorithm, and can improve the imaging speed by at least one order of magnitude. This significant improvement in imaging speed would potentially promote the applicability of SRPT for imaging living organisms.

## II. METHODOLOGY

## A. Forward modeling of SRPT

The SRPT imaging system has been described in our previous work [37]. Briefly, two Bessel beams generated by a pair of axicons and an objective lens were utilized as the pump and Stokes beams. Due to the considerable focal lengths of the Bessel beams [44], the detectable SRP signal may be an integration of SRS generation along with the Bessel beam Rayleigh length (or of the interaction length between the beams and the sample) [37].

$$
S _ {S R P} = B \int_ {0} ^ {\frac {d}{2}} \mathbf {r} ^ {\prime} J _ {0} ^ {2} \left(\beta_ {p} (\mathbf {r} ^ {\prime} - \mathbf {r} _ {0})\right) J _ {0} ^ {2} \bigl (\beta_ {S} (\mathbf {r} ^ {\prime} - \mathbf {r} _ {0}) \bigr) d \mathbf {r} ^ {\prime}
$$

$$
\int_ {L _ {1}} ^ {L _ {2}} C (\mathbf {r} _ {0}, \mathbf {z}) P _ {p} (\mathbf {r} _ {0}, \mathbf {z}) P _ {S} (\mathbf {r} _ {0}, \mathbf {z}) d \mathbf {z} \tag {1}
$$

in which $S _ { S R P }$ is the detected SRP signal by photodiode; ?? is the diameter of the Bessel beam’s central lobe; $\mathbf { r } _ { 0 }$ is the center of the Bessel beam’s central lobe; $J _ { 0 } ( \cdot )$ is the $0 ^ { \mathrm { t h } }$ order Bessel function; $B , \beta _ { p }$ and $\beta _ { S }$ are constants which can be found in existing literature [37]; $L _ { 2 } - L _ { 1 }$ indicates the thickness of the sample (within the Rayleigh length); $C ( \mathbf { r } _ { 0 } , \mathbf { z } )$ is the distribution of the imaginary element of the third-order nonlinear susceptibility $\chi ^ { ( 3 ) }$ at the center of the Bessel beam’s central lobe along the beam propagation direction of $\mathbf { z } ; P _ { p } ( \mathbf { r } _ { 0 } , \mathbf { z } )$ and $P _ { S } ( \mathbf { r } _ { 0 } , \mathbf { z } )$ are the powers of the pump and Stokes beams respectively. In SRPT, because the sizes of the pump and Stokes beams are very small, the powers can be regarded as the average power on the focusing plane. Moreover, the central lobe intensity of the Bessel beams passing through the sample can be constant if the sample is always within the depth of focus of the beams. In this case, $P _ { p } ( \mathbf { r } _ { 0 } , \mathbf { z } )$ and $P _ { S } ( \mathbf { r } _ { 0 } , \mathbf { z } )$ can be recorded as $P _ { p } ( \mathbf { r } _ { 0 } )$ and $P _ { S } ( { \bf r } _ { 0 } )$ .

In SRPT, both single point excitation and single point detection were employed, while the connection between the excitation and detection points were approximated as being perpendicular to the sample plane. Therefore, the SRPT can be considered as parallel beam imaging. By scanning the Bessel beams two-dimensionally on the lateral plane, we can generate a projection image at a certain rotation angle. This generated projection image can be calculated according to the following equation by changing the position of ??:

$$
S (\mathbf {r}) = B J (\mathbf {r}) \int_ {L _ {1}} ^ {L _ {2}} C (\mathbf {r}, \mathbf {z}) d \mathbf {z}. \tag {2}
$$

where ??(??) is the SRP signal at position of $\mathbf { r } : J ( \mathbf { r } ) =$ $\begin{array} { r l r } & { } & { P _ { p } ( { \bf r } ) P _ { S } ( { \bf r } ) \int _ { 0 } ^ { \frac { d } { 2 } } { \bf r } ^ { \prime } J _ { 0 } ^ { 2 } \left( \beta _ { p } ( { \bf r } ^ { \prime } - { \bf r } ) \right) J _ { 0 } ^ { 2 } \left( \beta _ { S } ( { \bf r } ^ { \prime } - { \bf r } ) \right) d { \bf r } ^ { \prime } ; C ( { \bf r } , { \bf z } ) } \end{array}$ is the imaginary element of the third nonlinear susceptibility at position of (??, ??) ; (??, ??) are coordinates for the lateral and propagation directions of the Bessel beams.

By rotating the sample with a step of a small angle, a number of angular-dependent projection images can be found and utilized to reconstruct the SRPT image:

$$
S (\mathbf {r}; \theta) = B J (\mathbf {r}; \theta) \int_ {L _ {1} (\theta)} ^ {L _ {2} (\theta)} C (\mathbf {r}, \mathbf {z}) d \mathbf {z}. \tag {3}
$$

where $S ( \mathbf { r } ; \theta ) , J ( \mathbf { r } ; \theta ) , L _ { 1 } ( \theta )$ and $L _ { 2 } ( \theta )$ are the corresponding values at different projection angles.

Equation (3) demonstrates the forward model of SRPT. Using this equation, we can determine angular-dependent projection images as long as we are aware of all the relevant information about the laser beams and the sample. The reconstruction of SRPT recovers the distribution of the imaginary element of the third-order nonlinear susceptibility $( C ( { \bf r } , { \bf z } ) )$ from the measured angular-dependent projection images $( S ( \mathbf { r } ; \theta ) )$ ). As can be seen in the following simulations, 180 angular-dependent projection images that were utilized for SRPT reconstruction were generated by projecting the sample to a specific plane while rotating it consecutively at one-degree steps along an axis, using Eq. (3).

## B. TV-regularized SART algorithm

Eq. (3) denotes a line integral of $C ( \mathbf { r } , \mathbf { z } )$ from $L _ { 1 }$ to $L _ { 2 }$ along the beam propagation direction. Such line integral represents the Radon transform of the unknown or reconstructed quantity. Thus, the forward model of SRPT can be described by the following matrix equation:

$$
S = R C \tag {4}
$$

where S is the measured SRP image; R is the Radon transform; C is the (unknown) distribution of the imaginary element of the third-order nonlinear susceptibility.

If we acquire a complete data set, the recovery of C from the noisy measurement S can be achieved by applying the FBP algorithm. If the measurements are incomplete, the SRPT images can be reconstructed by solving the following optimization problem:

$$
\tilde {C} = \arg \min \frac {1}{2} \| S - R C \| _ {2} ^ {2} + \lambda \Phi_ {T V} (C) \tag {5}
$$

where C̃ is the reconstructed distribution of the imaginary element of $\chi ^ { ( 3 ) }$ ; ?? is the regularization parameter and $\phi _ { T V } ( \mathrm { C } )$ is the TV regularization term [38]:

$$
\Phi_ {T V} (\mathrm{C}) = \sum_ {s, t} \sqrt {\left(\mathrm{C} _ {s , t} - \mathrm{C} _ {s - 1 , t}\right) ^ {2} + \left(\mathrm{C} _ {s , t} - \mathrm{C} _ {s , t - 1}\right) ^ {2}} \tag {6}
$$

where the subscripts ??, ?? are the pixel indices in matrix C.

The minimization problem in Eq. (6) can be solved by using various optimization algorithms, such as the steepest descent method and the conjugate gradient method. Here, we used the steepest descent method to determine the steepest descent direction for the TV based minimization problem in Eq. (6) [38]:

$$
d _ {s, t} = \frac {2 C _ {s , t} - C _ {s - 1 , t} - C _ {s , t - 1}}{\sqrt {\mathcal {I} + (C _ {s , t} - C _ {s - 1 , t}) ^ {2} + (C _ {s , t} - C _ {s , t - 1}) ^ {2}}} -
$$

$$
\frac {C _ {s + 1 , t} - C _ {s , t}}{\sqrt {\mathcal {I} + \left(C _ {s , t} - C _ {s - 1 , t}\right) ^ {2} + \left(C _ {s , t} - C _ {s , t - 1}\right) ^ {2}}} - \frac {C _ {s , t + 1} - C _ {s , t}}{\sqrt {\mathcal {I} + \left(C _ {s , t} - C _ {s - 1 , t}\right) ^ {2} + \left(C _ {s , t} - C _ {s , t - 1}\right) ^ {2}}} (7)
$$

where  is a very small positive number. The steepest descent direction can be expressed by the vector d and its unit vector is denoted as d̂.

The solution to the minimization problem in Eq. (5) can be obtained using the SART, which is iterated as [45]:

$$
C _ {j} ^ {(k + 1)} = C _ {j} ^ {(k)} + \alpha \frac {\sum_ {i \in I _ {\varphi}} \left[ r _ {i j} \frac {S _ {i} - R _ {i} \cdot C ^ {(k)}}{\sum_ {n = 1} ^ {N} r _ {i n}} \right]}{\sum_ {i \in I _ {\varphi}} r _ {i j}} \tag {8}
$$

where $I _ { \varphi }$ represents the set of index of rays passing through the jth pixel of the reconstructed image when projecting from angle ??; $r _ { i j }$ denotes the weight of the jth pixel contributing to the ith ray; ?? is the total number of pixels in the reconstructed image; $R _ { i }$ is the ith row of the projector; ?? is the number of corresponding iterations; ?? is the relaxation factor.

The step-by-step procedure of the TV-regularized SART algorithm can be summarized as [42][46][47]:

1. Initialization: ${ \mathsf C } = 0 , { \mathsf C } _ { 0 } = { \mathsf C } ;$  
2. SART iteration reconstruction using a projection model;  
3. Positivity constraint is imposed on the reconstructed image:

$$
\mathrm{C} _ {j} = 0 \text {when} \mathrm{C} _ {j} <   0
$$

4. Compute the residual: $d _ { i m g } = | { \sf C } - { \sf C } _ { 0 } | ;$  
5. Compute TV minimization term by repeating the following operation $N _ { g r a d }$ times:

Computing d and d̂ by using Eq. (7);

$\begin{array} { r } { \mathrm { U p d a t e : \thinspace C \gets C - \lambda } d _ { i m g } \hat { \mathsf { d } } ; } \end{array}$

$6 . \mathrm { C } _ { 0 } = \mathrm { C } ;$

7. Repeat Step 2 to Step 6 until there is no considerable change between two adjacent iterations.

There are several parameters which are both crucial and essential, including regularization parameter ?? , relaxation factor $\alpha ,$ iteration number N of SART, and iteration number $N _ { g r a d }$ of TV. Existing research shows that we can empirically determine these parameters [38][39][46][47][48][49][50]. To conduct the comparisons under the same condition, parameters were set as: $\lambda = 0 . 0 8$ , $\alpha = 1 / \big ( 1 + 0 . 5 ( n - 1 ) \big )$ (n is the current iterative number of SART), N=50, and $N _ { g r a d } = 1 0$ in the simulations and experiments which follow.

## C. Pixel vertex driven projection model

In the TV-regularized SART algorithm, we needed to repeatedly calculate projectors during iterative process, as stated in Step 2. The accuracy and computational burden of such projectors are major challenges for iterative reconstruction. The pixel vertex driven model (PVDM) was deduced from the separable footprint (SF) projector by assuming that the parallel beam projection was performed in SRPT. The SF projector has been reported to be more accurate and efficient than that of the distance-driven model (DDM), as can be seen in Supplementary Figure S1, whose capability has been demonstrated in the cone-beam computed tomography [43]. Here, we made some modifications on the SF projector so that it can be applied to parallel beam SRPT. Such PVDM was used to determine the projector of R in Eq. (5) or (8).

Figure 1 shows the diagram of the PVDM projection model for the parallel beam illumination, where the red rectangle frames the projection of one pixel on the detector. In the forward projector, projecting four vertices of one pixel onto the detector along the beam illumination direction provides the ladder-shaped footprint. In some particular cases, the shape of the footprint can be a rectangle at the projection angles of 0o, 90o, 180o, and 270o, or it can be a triangle at the angles of 45°, 135°, 225°, and 315°. Such diverse projection shapes make the PVDM best approximate the actual physical process of parallel beam projection imaging. The footprint intersects with the detector, and the intersection area denotes the weight of the pixel to the detector. The whole area of one footprint is set to be unity. The weight and the coordinates of the pixel are then recorded for the subsequent back projection. There are ten kinds of intersections for the determination of weight values, as shown in Fig. 2. The calculation of weight values for the ten intersections are detailed in the Appendix.

![](images/188ec15bf3b19dbc387759aae69949ac0f50bfdf04b6f85e43c3ef6c67522d74.jpg)

<details>
<summary>text_image</summary>

w₁ = \u221a2X | sin(\u03cfrac4 - \u03b7) |
w₂ = \u221a2X | cos(\u03cfrac4 - \u03b7)
</details>

Fig. 1. Diagram of the pixel vertex driven projection model for the parallel beam illumination. w1 and w2 represent the lengths of the upper and lower edges of the trapezium, while h is the height of the trapezium.

## D. Assessment of image quality

Two evaluation indices, structural similarity (SSIM) and root mean square error (RMSE), were used to evaluate our sparsely reconstructed results. SSIM compares the local patterns of normalized pixel intensities in terms of luminance and contrast [51], [52]. The closer the SSIM is to unity, the better the sparsely reconstructed result is. The SSIM can be calculated as:

$$
S S I M (\mathrm{R}, \mathrm{A}) = \frac {(2 \mu_ {\mathrm{R}} \mu_ {\mathrm{A}} + c _ {1}) (2 \sigma_ {\mathrm{RA}} + c _ {1})}{(\mu_ {\mathrm{R}} ^ {2} + \mu_ {\mathrm{A}} ^ {2} + c _ {1}) (\sigma_ {\mathrm{R}} ^ {2} + \sigma_ {\mathrm{A}} ^ {2} + c _ {2})} \tag {9}
$$

where $\mu _ { \mathrm { R } }$ and $\mu _ { \mathrm { A } }$ are the average values of the reconstructed and reference images, respectively; $\sigma _ { \mathrm { R } }$ and $\sigma _ { \mathrm { A } }$ are the standard deviations of the reconstructed and reference images, respectively; $\sigma _ { \mathrm { R A } }$ is the covariance between them; $c _ { 1 }$ and $c _ { 2 }$ are the constants related to the dynamic ranges of the images.

The RMSE is a type of numerical index that can be used to measure the accuracy of an image restoration. The smaller the RMSE, the more accurate the sparsely reconstructed image. RMSE can be calculated as follows [53]:

$$
R M S E = \sqrt {\sum_ {x , y} \left(C _ {x , y} - C _ {x , y} ^ {*}\right) ^ {2} / N} \tag {10}
$$

in which $C _ { x , y }$ and $C _ { x , y } ^ { * }$ are the reconstructed and reference values of the imaginary element of $\chi ^ { ( 3 ) }$ on each pixel and ?? is the pixel number. Here, the original image was used as the reference image for simulation comparisons, and the image reconstructed by using 180 projections was selected as the reference image for the single cell experiment.

![](images/5451eb8c87afbd6784430422c4c484e204f730e11b7b0b9fbd3777f84b931d5a.jpg)  
(a)

![](images/f70ea373b8660b2aea705f5ef9c3919ddc00f1c762708808338c1b502258f338.jpg)  
(b)

![](images/85d9c3782fd733a106639fd98077053fa7503f504028c878396e01c9f4f9998a.jpg)  
(c)

![](images/5e5910f74dbe8a3a4931f7e88241056463a03b46bb40c9444913c69af54ff41b.jpg)  
(d)

![](images/c6e4460f03d48bc439264c58bad16cfa37959321956a8690cfa96b4e3a63a3ef.jpg)  
(e)

![](images/d90f8b603b7518a8336f67e11a806417cb9ed08ae8b8090f588f99de11753fc5.jpg)  
(f)

![](images/84c36781fa0c469f2f3e740c6af7e7a27ea84708ea13571c6f98918addde7458.jpg)  
(g)

![](images/c4d3c2f0129c87fdaf626dc2a2c89196be6b88783a54b560f2446784543f1588.jpg)  
(h)

![](images/ca552107f1be2c1f18334fd2a99498610b8c3ebe9ea17f187424b4689d625d6c.jpg)  
(i)

![](images/067c1491cf245e011add75a2cd746038ecf7735dc36a97f7dacd70745b39149f.jpg)  
()  
Fig. 2. Ten kinds of intersections for the determination of weight value.

## III. EXPERIMENTS AND RESULTS

In this section, we describe how the validity and the application potential of the proposed fast SRPT were evaluated with numerical simulations and a single cell based experiment. In the simulations, we compared the sparsely reconstructed images with the original image to determine the minimum number of projection images. A single adipose cell based experiment was also conducted to determine whether the imaging speed efficiency of the proposed SRPT is improved relative to that of the Gaussian beam based SRS sectioning imaging.

## A. Simulation verification

The validity of the proposed TV-regularized SART algorithm was evaluated with two groups of numerical simulations. In the evaluation, the data sets employed for sparse reconstruction were constructed by equally sampled complete projections in a half circle, consisting of 180, 90, 60, 45, 36, 30, 15, 9, and 6 projections respectively. For comparisons, the DDM based TV-regularized SART algorithm and the FBP algorithm were applied as the references. A Ramp filter was utilized in the FBP algorithm [54]. For a fair comparison, the same data set was utilized for all three algorithms. The data set was generated by using discrete form of Eq. (3), whose process was very similar to ray-driven model. The generation process can be described as follows. First, by fixing the position of ?? and the projection angle of ??, the SRP signal can be calculated by integrating Eq. (3) along a light ray. Second, by changing the position of ?? two-dimensionally, a SRP image can be generated by calculating the SRP signal at each position. Last, a data set of angular-dependent SRP images can be obtained by changing the projection angle of ?? and generating the SRP image at each projection angle. To ensure the accuracy of forward projection data, we discretized the detector into 1024 pixels.

First, a modified Shepp-Logan model was used to perform the evaluation simulations [17]. Figure 3(a) shows the original image of the modified Shepp-Logan model, and the reconstructed images by three algorithms using 180, 60, 30, 15, and 9 projections are presented in Fig. 4. Figure 4(a1-a5) depicts the reconstructed images of the PVDM based TV-regularized SART algorithm, Fig. 4(b1-b5) shows those of the DDM based TV-regularized SART algorithm, and Fig. 4(c1-c5) displays those of the FBP algorithm. We observed that almost the same performance was obtained by the PVDM and the DDM based TV-regularized SART algorithms, which were much better than that obtained by the FBP algorithm. Furthermore, we also found that good quality of the reconstructed images could be maintained even when the projection number was decreased to 30. When the number of projections was reduced to 15, there was some blur observed in the reconstructed images and small details could not be distinguished. Even worse, no acceptable images could be reconstructed when the number of projections was reduced to 9. To quantitatively evaluate the quality of the reconstructed images, we calculated the SSIM and RMSE values. Figure 5(a) and 5(b) show the changes of the SSIM and RMSE values as a function of the projection number respectively. Almost the same performance conclusions were drawn from the SSIM and RMSE curves. The SSIM and RMSE values changed slightly when the projection number was no smaller than 30 for iterative algorithms. However, it decreased (SSIM) or increased (RMSE) dramatically when the number of projections was smaller than 15. Importantly, the proposed PVDM based TV-regularized SART algorithm provided better results than the DDM based one in the sparse views case, for example the projection number was not larger than 60 in this simulation.

![](images/122fad7003f8b585dc47ca55b46de136a35e1db6f8bd772473f2f2e212c6a3e6.jpg)

<details>
<summary>natural_image</summary>

Circular diagram with two dark oval shapes inside, no text or symbols present
</details>

(a)

![](images/d717167488a8583f200722f8bcb00c702c5e864f066fc128d78a4f58fcc6ab54.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological cell or tissue structure with two circular regions, no visible text or symbols.
</details>

(b)  
Fig. 3. Original images of the (a) Modified Shepp-Logan model and (b) a cross-section view of the Arabidopsis silique model.

![](images/ceef1ed3278bae035aec51c2942d68bc505ff04c8717af774e0187e6f5d3f1eb.jpg)

<details>
<summary>text_image</summary>

180
(a1)
(b1)
(c1)
60
(a2)
(b2)
(c2)
30
(a3)
(b3)
(c3)
15
(a4)
(b4)
(c4)
9
(a5)
(b5)
(c5)
Num
Algorithms
PVDM based SART
DDM based SART
FBP
</details>

Fig. 4. Reconstructed results of the modified Shepp-Logan model based simulation. The results reconstructed by the (a) PVDM based SART, (b) DDM based SART, and (c) FBP algorithms; Symbols (1)-(5) represent the number of projections used for reconstruction consisting of 180, 60, 30, 15, and 9 projections, respectively.

Second, an Arabidopsis silique model was utilized as a physical model in order to generate forward projection images and measure the performance of the proposed algorithm further. Figure 3(b) shows one cross-section of the original image of Arabidopsis silique model. Figure 6 presents the images reconstructed from the sparsely sampled data sets consisting of, respectively, 180, 60, 30, 15, and 9 projections, where the left column shows the results of the PVDM based TV-regularized SART algorithm, the middle column displays the DDM based results, and the right column shows those obtained from the FBP algorithm. Once again, better performance was obtained by applying the iterative algorithms than the FBP. The distribution and shape of the targeted objects could be well recovered by using as little as 30 projections. Even when the projection number was reduced to 15, the reconstructed image still showed little blur. A little distorted or displaying artifact interference was aroused when the number of projections was reduced to 9. The calculated SSIM and RMSE values shown in Fig. 5(c) and 5(d) also gave the same conclusion. It should be noted that the PVDM based TV-regularized SART algorithm provided better results than the DDM based one when the projection number was smaller than 30, showing the good ability in sparse reconstruction from sparse-view data. These results collectively indicate that our TV-regularized SART algorithm can provide satisfactory or acceptable reconstructed images (SSIM>0.9) even when the number of projections is reduced to 15, leading to a 12-fold improvement in imaging speed compared to the current SRPT scheme.

![](images/aaff3db6958af37f4a1eca2d30e02c9b6b2f176d82c6d09e8b2dda4ae1a8290b.jpg)

<details>
<summary>line chart</summary>

| Projection Number | PVDM-SART | DDM-SART | FBP  | Threshold |
| ----------------- | --------- | -------- | ---- | --------- |
| 180               | 1.0       | 1.0      | 0.92 | 1.0       |
| 150               | 1.0       | 1.0      | 0.91 | 1.0       |
| 120               | 1.0       | 1.0      | 0.90 | 1.0       |
| 90                | 1.0       | 1.0      | 0.88 | 1.0       |
| 60                | 1.0       | 1.0      | 0.84 | 1.0       |
| 30                | 0.98      | 0.98     | 0.75 | 1.0       |
| 0                 | 0.85      | 0.75     | 0.50 | 1.0       |
</details>

(a)

![](images/50b5bbba12ace26f4e959b8790a766dd4dfd0cf8de3aa814fa957c2c910241c2.jpg)

<details>
<summary>line chart</summary>

| Projection Number | PVDM-SART | DDM-SART | FBP   |
| ----------------- | --------- | -------- | ----- |
| 180               | 0.0       | 0.0      | 0.15  |
| 150               | 0.0       | 0.0      | 0.16  |
| 120               | 0.0       | 0.0      | 0.17  |
| 90                | 0.0       | 0.0      | 0.18  |
| 60                | 0.0       | 0.0      | 0.20  |
| 30                | 0.05      | 0.05     | 0.25  |
| 0                 | 0.15      | 0.25     | 0.65  |
</details>

(b)

![](images/42d32eb4df009a30011b8b506a5de5a8bde2f3077fa305660ba356e744b6ef9c.jpg)

<details>
<summary>line chart</summary>

| Projection Number | PVDM-SART | DDM-SART | FBP   | Threshold |
| ----------------- | --------- | -------- | ----- | --------- |
| 180               | 1.0       | 1.0      | 0.9   | 0.9       |
| 150               | 1.0       | 1.0      | 0.85  | 0.9       |
| 120               | 1.0       | 1.0      | 0.8   | 0.9       |
| 90                | 1.0       | 1.0      | 0.7   | 0.9       |
| 60                | 1.0       | 1.0      | 0.6   | 0.9       |
| 30                | 0.9       | 0.9      | 0.5   | 0.9       |
| 0                 | 0.7       | 0.7      | 0.3   | 0.9       |
</details>

(c)

![](images/5e00b301d841ae23a21b9fbe03d2f98d6f16def29793af7d0d11424c4eb6683c.jpg)

<details>
<summary>line chart</summary>

| Projection Number | PVDM-SART | DDM-SART | FBP     |
| ----------------- | --------- | -------- | ------- |
| 180               | 0.0000    | 0.0000   | 0.0000  |
| 90                | 0.0005    | 0.0005   | 0.0015  |
| 60                | 0.0010    | 0.0010   | 0.0030  |
| 30                | 0.0025    | 0.0025   | 0.0060  |
| 0                 | 0.0040    | 0.0040   | 0.0120  |
</details>

(d)  
Fig. 5. Comparison of SSIM and RMSE values between images reconstructed by three algorithms and the original image. (a)-(b) SSIM and RMSE values as a function of projection number in the modified Shepp-Logan model-based simulation; (c)-(d) SSIM and RMSE values as a function of projection number in the Arabidopsis silique model-based simulation. Blue asterisk lines represent results of the PVDM based SART algorithm, black circle lines are results of the DDM based SART algorithm, and magenta square lines are those of FBP algorithm. Here, the threshold (solid red lines) is defined as ninety-five percent of the best SSIM.

Although the TV-regularized iterative algorithms performed better than the FBP algorithm especially in the case of sparseview data, they have over-smoothing effects on tiny details. We can see that the images reconstructed by the FBP algorithm look quite sharp in the few-view cases. Even with 15 or nine views, when the images reconstructed by the TV-regularized SART algorithm have been blurred, the edges of the structures in the FBP images are still visible, despite the conspicuous streaks. In the modified Shepp-Logan phantom, there are six dots near to the right side of the skull that are still visible in 15- and nine-view reconstructions, as shown in Figs. 4(c4) and 4(c5). In order to observe this phenomenon more intuitively, we extracted a line across two of six dots in the modified Shepp-Logan phantom, as labeled in Fig. 7(a). Figures 7(b)-7(f) plot the extracted lines of the three reconstruction algorithms by using 180, 60, 30, 15, and 9 projections respectively. The same conclusion can be drawn; which is that the FBP algorithm had a better detail resolution ability in few-view cases. This may be caused by the use of TV regularization, which may over-smooth edges and details [42][55][56]. This smoothing effect was influenced by the parameters of the TV regularization. We investigated this potential influence by changing the parameter of $N _ { g r a d }$ . We discovered that the larger the $N _ { g r a d }$ , the more smoothing the effect would be. If the $N _ { g r a d }$ was too small, the quality of the reconstructed image would be worse (see Supplementary Figure S2).

![](images/5ed9848e5be6d61d69f9a6abe88dce798be59192dc120f0ad954d369cdfbd8f0.jpg)  
Fig. 6. Reconstructed results of the Arabidopsis silique model-based simulation. The results reconstructed by the (a) PVDM based SART, (b) DDM based SART, and (c) FBP algorithms; Symbols (1)-(5) represent the number of projections used for reconstruction consisting of 180, 60, 30, 15, and 9 projections, respectively.

## B. Applicability-potential demonstration

To further explore the potential of the proposed fast SRPT for live cell imaging, we three-dimensionally imaged lipid droplets (LDs) in adipose cells. Here, differentiated 3T3-L1 cells were used for testing [37]. As a mouse derived cell line, 3T3-L1 is widely used for adipogenesis studies [57], and can differentiate into adipose cells, which accumulate LDs in the cytosol under certain conditions. After the cells were cultured for some time, they were first mixed with 1.5% (w/v) agarose gel in PBS solution. The gel mixture was allowed to set in a cylindrical capillary tube with an inner diameter of \~50 microns. The tube was mounted onto a homemade sample holder for imaging during sample rotation [37]. The rotation was performed at 1o per step for acquisition of 180 projection images. The image pixel dwell time was set to 10 μs and each image contained 300 × 300 pixels. Other imaging parameters were setup as described in our previous publication [37].

![](images/fc2a1ee6d44eb6db93e84298dd9aa8484f513d72dd782a1bac972ef1c319da12.jpg)

![](images/fcd629f6cfcc497ee52f26f3db571da0a81d8baff2590cb4df2fc3428c3ba42f.jpg)

<details>
<summary>line chart</summary>

| Sample Points | Intensity (a.u.) |
| ------------- | ---------------- |
| 0             | 1.0              |
| 10            | 1.4              |
| 20            | 1.4              |
| 30            | 1.0              |
| 40            | 1.0              |
| 50            | 1.4              |
| 60            | 1.4              |
| 70            | 1.0              |
| 80            | 1.0              |
</details>

(c)

![](images/d254ca5193b3ba9ba39fd8519b6b50f7d47be6005639dc0805016255235e6b60.jpg)

<details>
<summary>line chart</summary>

| Sample Points | Intensity (a.u.) |
| ------------- | ---------------- |
| 0             | 1.0              |
| 20            | 1.4              |
| 40            | 1.0              |
| 60            | 1.4              |
| 80            | 1.2              |
</details>

(d)

![](images/f44185bba99429d487fc5e68d1b1b040f2a8cbdf62469e650a2f882b868cec88.jpg)

<details>
<summary>line chart</summary>

| Sample Points | Intensity (a.u.) |
| ------------- | ---------------- |
| 0             | 1.0              |
| 20            | 1.5              |
| 40            | 1.0              |
| 60            | 1.5              |
| 80            | 1.5              |
</details>

(e)

![](images/d8e6ef58d3de74a4dca0a9b2a557e9398b439d3d3aff4e38343ce35095a3f0a4.jpg)

<details>
<summary>line chart</summary>

| Sample Points | Intensity (a.u.) |
| ------------- | ---------------- |
| 0             | 1.0              |
| 20            | 1.5              |
| 40            | 1.3              |
| 60            | 1.4              |
| 80            | 1.3              |
</details>

(f)  
Fig. 7. Investigation of the detail-resolved ability of different algorithms. (a) Curve extraction position (marked with a red line); (b)-(f) Comparisons of different algorithms with the original line. Blue lines represent the results of the PVDM based SART algorithm, black lines are results of the DDM based SART algorithm, magenta lines are those of FBP algorithm, and red lines represent the curves of the original image. (b)-(f) show comparison results for 180, 60, 30, 15, and 9 projections, respectively.

The collected projection images were first pre-processed for de-noising and compensation, and then used for reconstructing the distribution of lipids in the cell. By comparing the simulation results with the original image, we had found that the image reconstructed by the iterative algorithms had much better quality than that reconstructed by the FBP algorithm, with the SSIM values being higher even when using 180 projections. Therefore, the image reconstructed by the PVDM based SART algorithm from 180 projections was used as the reference to evaluate the performance of the reconstruction from the sparsely sampled data. Figure 8(a) shows the image reconstructed by the FBP algorithm with 180 projection images, and Fig. 8(b)-(h) show the reconstructed cell and distribution of lipids inside the cell by using 180, 90, 60, 36, 30, 15, 9 projections, respectively. We observed that the quality of the reconstructed image was well maintained until the projection number was reduced to 30. A little distortion could still be seen when the number of the projection was decreased to 15, with little differences observed in the fine structures at the edge of the cell. Obvious differences were observed in morphology until the number of projections was reduced to 9. The SSIM and RMSE values as a function of the projection number were also calculated and shown in Fig. 9, and these results also indicated that a minimum projection number of 30 was required to remain a relatively good reconstruction fidelity. The SSIM value between the images which are reconstructed by the FBP and the PVDM based SART algorithms was 0.9551, and the RMSE between them was 0.3978. By combining the analysis results shown in Fig. 8 and Fig. 9, we could obtain an acceptable reconstructed image when the number of projections was set at around 20. These cell-based experimental results demonstrate the applicability potential of the proposed PVDM based SART algorithm for fast imaging of a single adipose cell. Currently, the image reconstruction scheme used in SRPT is based on the FBP algorithm that requires 180 projection images to rebuild a volumetric image [37]. Thus, the algorithm improved the imaging speed by a factor of 9-12 without sacrificing discernible imaging details.

![](images/ac87d5e1570904eb5d919216141a8b567aa04419b7eb60fc87c70b75aa6baeb7.jpg)  
(a)

![](images/55beef8ad5fda7f4f5a1e3881b61c1bbb4e9b5d180397e9b5ea717cf4a0d9472.jpg)  
(b)

![](images/a88c74ca14a76964c057efd7db5c0f4bc0323f1a4c0fd2d9ef8076cbd206e2fb.jpg)  
(c)

![](images/4ea3ac644bbd4ad9c1da696fba9ec5d32399c371df5eea892cd29544e45ac700.jpg)  
(d)

![](images/1ac07c827d5c5347ad67d6272686099709894d56480b902dd91621c7a9f8fb49.jpg)  
(e)

![](images/6009fd5163544d4c0fbeab454d24e6658084a73f90a1781d5eda4a39ae7cb38a.jpg)  
(f)

![](images/07e983ebc61092554fa45da43bb1b9bfc2cb588f36a2f40e2dbf6e6e17b22cda.jpg)  
(g)

![](images/d40a74787247ecb40b9043b6b0bce8672b748f9a1fce88c7d8b2056de59fbc9f.jpg)  
(h)

Fig. 8. Reconstructed results of the lipid content in a single adipose cell using the FBP algorithm and the proposed SRPT-based imaging scheme. (a) Image reconstructed by the FBP algorithm with 180 projection images; (b)-(h) One section of images reconstructed from sparsely sampled data sets consisting of 180, 90, 60, 36, 30, 15, and 9 projections, respectively.  
![](images/cdfc41be1c6e2ac6b0e3b551c13589e4a675bab7969f6f59eb92b9cbdb52adf9.jpg)

<details>
<summary>line chart</summary>

| Projection Number | PVDM-SART | Threshold |
| ----------------- | --------- | --------- |
| 180               | 1.0       | 0.9       |
| 150               | 0.98      | 0.9       |
| 120               | 0.96      | 0.9       |
| 90                | 0.94      | 0.9       |
| 60                | 0.92      | 0.9       |
| 30                | 0.88      | 0.9       |
| 0                 | 0.5       | 0.9       |
</details>

(a)

![](images/ce5154369392be84c698f9c5cd105ecab7012314b00f63cc4b79d7ada5df39e5.jpg)

<details>
<summary>line chart</summary>

| Projection Number | RSME  |
| ----------------- | ----- |
| 180               | 0.0   |
| 90                | 0.06  |
| 60                | 0.08  |
| 30                | 0.12  |
| 0                 | 0.37  |
</details>

(b)  
Fig. 9. SSIM (a) and RMSE (b) values obtained from the images reconstructed by the PVDM based SART algorithm and the reference image.

## IV. DISCUSSION

Due to the non-diffractive property of Bessel excitation beams, SRPT can resolve the 3D distribution of chemicals in a volume through projection imaging and tomographic image reconstruction. The label-free approach in SRPT provides indispensable advantages for imaging living systems. Although the FBP algorithm has been applied to reconstruct a 3D image by SRPT, the high number of projection images required is the bottleneck for improving imaging speed. The slowing down of speed also increases the sample exposure time under intense lasers, augmenting the photo-toxicity risk for living samples. Our newly developed sparse-view data-based sparse reconstruction scheme requires only 15-20 projections to reconstruct a 3D image with acceptable or satisfactory quality. This significant improvement in imaging speed would potentially promote the applicability of SRPT for imaging living organisms.

In the simulation, no obvious differences between the images reconstructed by our proposed scheme and the original image were observed until the number of projections was reduced to 30. As the number of projections was reduced to 15, the image quality was a little worse compared with the original image. This means that our proposed SRPT scheme is around 6\~12 times faster than the FBP based algorithm. For the adipose cell based experiment, the minimum number of projections required for reconstruction could also be reduced to 20 or less, which delivers a speed at least 9 times faster than the FBP algorithm. This meant that image acquisition time can be improved from 162 seconds (as in our previous study [37]) to \~16 seconds, which is crucial for longitudinal studies of live systems. In our previous study, [37] we have shown that the SRPT was four times faster than the Gaussian beams based SRS sectional imaging for imaging 3D volumes. Implemented with the sparse-view data-based sparse reconstruction, the SRPT provides at least an order of magnitude improvement in 3D imaging speed compared to the conventional Gaussian beams based SRS imaging.

Like reconstruction algorithm, the projection model is also an important part of iterative reconstruction method in SRPT. Accuracy and computational burden are the main factors we need to consider when choosing projection models. As can be seen from Supplementary Figure S1, PVDM that was deduced from the separable footprint projector has better accuracy than DDM. Especially when the number of projection images is relatively small, the PVDM based reconstruction method shows better image restoration ability (Figs. 4-6). However, the computation time of PVDM is longer than that of DDM. The computation time of PVDM based algorithms is approximately three times longer than the DDM based ones when using 180 projections; this factor decreased as the number of projections decreased (can be seen from Supplementary Figure S3).

Although the image acquisition time can be reduced by the fast SRPT scheme, reconstruction also takes extra time compared to the FBP based SRPT scheme. In the fast SRPT scheme, the calculation of the projectors introduced an additional time-consuming step as compared to the FBP based SRPT scheme. In addition, the cost of the total variation based iteration is slightly higher than that of the FBP reconstruction. Typical reconstruction time of the PVDM based TV-regularized SART algorithm is around 350 seconds, which is two orders of magnitude higher than the FBP algorithm (three seconds). Fortunately, both the calculation of projectors and the iteration reconstruction can be accelerated by applying the graphic processing unit technique. Furthermore, the quality of the images reconstructed by the fast SRPT scheme was much better than that obtained by the FBP algorithm, even when using 180 projections (Fig. 4 and Fig. 6).

## V. CONCLUSION

In conclusion, a sparse-view data-based sparse reconstruction scheme is proposed for SRPT, which combines the PVDM, TV regularization, and SART iteration to reconstruct the 3D distribution of chemicals at a speed of one order of magnitude faster than the FBP based SRPT. We believe that this work will facilitate basic and preclinical applications of the SRPT technique.

## APPENDIX

The calculation of the weight value for the ten kinds of intersections is detailed as follows.

Case shown in Fig. 2(a):

$$
\omega = \frac {1}{2} x ^ {2} \tan \beta \tag {A1}
$$

Case shown in Fig. 2(b):

$$
\omega = \frac {1}{2} (x + y) h \tag {A2}
$$

Case shown in Fig. 2(c):

$$
\omega = S - \frac {1}{2} x ^ {2} \tan \beta \tag {A3}
$$

Here, ?? is the whole area of one footprint.

Case shown in Fig. 2(d):

$$
\omega = S - \frac {1}{2} x _ {1} ^ {2} \tan \beta - \frac {1}{2} x _ {2} ^ {2} \tan \beta \tag {A4}
$$

Case shown in Fig. 2(e):

$$
\omega = d h \tag {A5}
$$

Here, ?? is the size of the detector.

Case shown in Fig. 2(f):

$$
\omega = \frac {1}{2} (d + x _ {2} + x _ {1}) h - \frac {1}{2} x _ {2} ^ {2} \tan \beta \tag {A6}
$$

Case shown in Fig. 2(g):

$$
\omega = \frac {1}{2} (d + x _ {2} + x _ {1}) h - \frac {1}{2} x _ {2} ^ {2} \tan \beta \tag {A7}
$$

Case shown in Fig. 2(h):

$$
\omega = S - \frac {1}{2} x ^ {2} \tan \beta \tag {A8}
$$

Case shown in Fig. 2(i):

$$
\omega = \frac {1}{2} (x + y) h \tag {A9}
$$

Case shown in Fig. 2(j):

$$
\omega = \frac {1}{2} x ^ {2} \tan \beta \tag {A10}
$$

## REFERENCES

[1] J. Sharpe, et al., “Optical projection tomography as a tool for 3D microscopy and gene expression studies,” Science, vol. 296, no. 5567, pp. 541-545, Apr. 2002.  
[2] J.X. Cheng, and X. Xie, “Vibrational spectroscopic imaging of living systems: an emerging platform for biology and medicine,” Science, vol. 350, no. 6264, Art. no. aaa8870, Nov. 2015.  
[3] E. Stelzer, “Light-sheet fluorescence microscopy for quantitative biology,” Nat. Methods, vol. 12, no. 1, pp. 23-26, Jan. 2015.  
[4] P. Keller, et al., “Light-sheet imaging for systems neuroscience,” Nat. Methods, vol. 12, no. 1, pp. 27-29, Jan. 2015.  
[5] Q. Fu, et al., “Imaging multicellular specimens with real-time optimized tiling light-sheet selective plane illumination microscopy,” Nat. Commun., vol. 7, Art. no. 11088, Mar. 2016.  
[6] G. Katona, et al., “Fast two-photon in vivo imaging with three-dimensional random-access scanning in large tissue volumes,” Nat. Methods, vol. 9, no. 2, pp. 201-208, Jan. 2012.  
[7] H. Dana, et al., “Hybrid multiphoton volumetric functional imaging of large-scale bioengineered neuronal networks,” Nat. Commun., vol. 5, Art. No. 3997, Jun. 2014.  
[8] P. Santi, “Light sheet fluorescence microscopy: a review,” J. Histochem. Cytochem., vol. 59, no. 2, pp. 129-138, 2011.  
[9] R. Power, J. Huisken, “A guide to light-sheet fluorescence microscopy for multiscale imaging,” Nat. Methods, vol. 14, no. 4, pp. 360-373, Mar. 2017.  
[10] P.F. Verveer, et al., “High-resolution three-dimensional imaging of large specimens with light sheet based microscopy,” Nat. Methods, vol. 4, no. 4, pp. 311-313, 2007.  
[11] P. Keller, et al., “Reconstruction of zebrafish early embryonic development by scanned light sheet microscopy,” Science, vol. 322, no. 5904, pp. 1065-1069, 2008.  
[12] M.B. Ahrens, et al., “Whole-brain functional imaging at cellular resolution using light-sheet microscopy,” Nat. Methods, vol. 10, no. 5, pp. 413-420, 2013.  
[13] B. Chen, et al., “Lattice light sheet microscopy: imaging molecules to embryos at high spatiotemporal resolution,” Science, vol. 346, no. 6208, Art. No. 1257998, Oct. 2014.  
[14] T. Bruns, et al., “Sample holder for axial rotation of specimens in 3D microscopy,” J. Microsc. Vol. 260, no. 1, pp. 30-36, 2015.  
[15] J. Shapes, “Optical projection tomography as a new tool for studying embryo anatomy,” J. Anat., vol. 202, no. 2, pp. 175-181, Feb. 2003.  
[16] M. Boot, et al., “In vitro whole-organ imaging: 4D quantification of growing mouse limb buds,” Nat. Methods, vol. 5, no. 7, pp. 609-612, Jul. 2008.  
[17] S. Zhu, et al., “Automated motion correction for in-vivo optical projection tomography,” IEEE Trans. Med. Imaging, vol. 31, no. 7, pp. 1358-1371, Feb. 2012.  
[18] C. Pardo-Martin, et al., “High-throughput hyperdimensional vertebrate phenotyping,” Nat. Commun., vol. 4, Art. No. 1467, 2013.  
[19] B.W. Lindsey, J. Kaslin, “Optical projection tomography as a novel method to visualize and quantitate whole-brain patterns of cell proliferation in the adult zebrafish brain,” Zebrafish, to be published. DOI:10.1089/zeb.2017.1418.  
[20] S. Stewart, et al., “Raman imaging,” Annu. Rev. Anal. Chem., vol. 5, no. 1, pp. 337-360, Apr. 2012.  
[21] H. Abramczyk, and B. Brozek-Pluska, “Raman imaging in biochemical and biomedical applications. Diagnosis and treatment of breast cancer,” Chem. Rev., vol. 113, no. 8, pp. 5766-5781, May 2013.  
[22] Y. Oshim, et al., “Light sheet-excited spontaneous Raman imaging of a living fish by optical sectioning in a wide field Raman microscope,” Opt. Express, vol. 20, no. 15, pp. 16195-16204, 2012.  
[23] Y. Oshima, et al., “Light sheet direct Raman imaging technique for observation of mixing of solvents,” Appl. Spectrosc., vol. 63, no. 10, pp. 1115-1120, 2009.  
[24] I. Barman, et al., “Optical sectioning using single-plane-illumination Raman imaging,” J. Raman Spectrosc., vol. 41, no. 10, pp. 1099-1101, 2010.  
[25] I. Rocha-Mendoza, et al., “Rapid spontaneous Raman light sheet microscopy using cw-lasers and tunable filters,” Biomed. Opt. Express, vol. 6, no. 9, pp. 3449-3461, Sep. 2015.  
[26] W. Müller, et al., “Light sheet Raman micro-spectroscopy,” Optica, vol. 3, no. 4, pp. 452-457, 2016.  
[27] M.V. Schulmerich, et al., “Noninvasive Raman tomographic imaging of canine bone tissue,” J. Biomed. Opt., vol. 32, no. 2, Art. no. 020506, 2008.  
[28] J. Demers, et al., “Multichannel diffuse optical Raman tomography for bone characterization in vivo: a phantom study,” Biomed. Opt. Express, vol. 3, no. 9, pp. 2299-2305, Sep. 2012.  
[29] S. Sil, S. Umapathy, “Raman spectroscopy explores molecular structural signatures of hidden materials in depth: universal multiple angle Raman spectroscopy,” Sci. Rep., vol. 4, No. 24, Art. no. 5308, 2014.  
[30] J. Demer, et al., “Next-generation Raman tomography instrument for non-invasive in vivo bone imaging,” Biomed. Opt. Express, vol. 6, no. 3, pp. 793-806, May 2015.  
[31] A. Konovalov, and V. Vlasov, “Theoretical limit of spatial resolution in diffuse optical tomography using a perturbation model,” Quant. Electron., vol. 44, no. 3, pp. 239–246, 2014.  
[32] C. Evans, X. Xie, “Coherent anti-Stokes Raman scattering microscopy: chemical imaging for biology and medicine,” Annu. Rev. Anal. Chem., vol. 1, no. 1, pp. 883-909, 2008.  
[33] S. Zaitsu, T. Imasaka, “Continuous-wave multifrequency laser emission generated through stimulated Raman scattering and four-wave Raman mixing in an optical cavity,” IEEE J. Quan. Electron., vol. 47, no. 8, pp. 1129-1135, 2011.  
[34] Y. Ozeki, et al., “High-speed molecular spectral imaging of tissue with stimulated Raman scattering,” Nat. Photonics, vol. 6, no. 12, pp. 845-851, 2012.  
[35] Jr. C. Camp, M. Cicerone, “Chemically sensitive bioimaging with coherent Raman scattering,” Nat. Photonics, vol. 9, no. 5, pp. 295–305, 2015.  
[36] C. Krafft, et al., “Developments in spontaneous and coherent Raman scattering microscopic imaging for biomedical applications” Chem. Soc. Rev., vol. 47, no. 21, pp. 1819–1849, 2016.  
[37] X. Chen, et al., “Volumetric chemical imaging by stimulated Raman projection microscopy and tomography,” Nat. Commun., vol. 8, Art. no. 15117, Apr. 2017.  
[38] E.Y. Sidky, et al., “Accurate image reconstruction from few-views and limited-angle data in divergent-beam CT,” J. X-ray Sci. Technol., vol. 14, no. 2, pp. 119-139, 2006.  
[39] Y. Lu, et al., “Few-view image reconstruction with dual dictionaries,” Phys. Med. Biol., vol. 57, no. 1, pp. 173-189, 2012.  
[40] B. Yan, et al., “NUFFT-based iterative image reconstruction via alternating direciton total variation minimization for sparse-view CT,” Comput. Math. Meth. Med., Article No. 691021, 2015.  
[41] V. Gopi, et al., “Iterative computed tomography reconstruction from sparse-view data,” J. Med. Imaging Health Informatics, vol. 6, no. 1, pp. 34-46, 2016.  
[42] X. Luo, et al., “An image reconstruction method based on total variation and wavelet tight frame for limited-angle CT,” IEEE Access, vol. 6, pp. 1461-1470, 2018.  
[43] Y. Long, et al., “3D forward and back-projection for X-ray CT using separable footprints,” IEEE Trans. Med. Imaging, vol. 29, no. 11, pp. 1839-1850, 2010.  
[44] M. Duocastella, C. Arnold, “Bessel and annular beams for materials process,” Laser Photonics Rev., vol. 6, no. 5, pp. 607-621, 2012.  
[45] A.H. Andersen, and A.C. Kak, “Simultaneous algebraic reconstruction technique (SART): a superior implementation of the ART algorithm,” Ultrason. Imaging, vol. 6, no. 1, pp. 81-94, 1984.  
[46] H. Yu, G. Wang, “Compressed sensing based interior tomography,” Phys. Med. Biol., vol. 54, no. 9, pp. 2791-2805, 2009.  
[47] T. Gomi, et al., “Evaluation of digital tomosynthesis reconstruction algorithms used to reduce metal artifacts for arthroplasty: a phantom study,” Phys. Medica, vol. 42, pp. 28-38, 2017.  
[48] M. Jiang, G. Wang, “Convergence of the simultaneous algebraic reconstruction technique (SART),” IEEE Trans. Image Process., vol. 12, no. 8, pp.957-961, 2003.  
[49] M. Jiang, G. Wang, “Convergence studies on iterative algorithms for image reconstruction,” IEEE Trans. Med. Imaging, vol. 22, no. 5, pp. 569-579, 2003.  
[50] Y. Du, et al., “Evaluation of hybrid SART+OS+TV iterative reconstruction algorithm for optical-CT gel dosimeter imaging,” Phys. Med. Biol., vol. 61, no. 24, pp. 8425-8439, 2016.  
[51] Z. Wang, et al., “Image quality assessment: from error visibility to structural similarity,” IEEE Trans. Image Processing, vol. 13, no. 4, pp. 600-612, Apr. 2004.  
[52] T. Correia, et al., “Accelerated optical projection tomography applied to in vivo imaging of zebrafish,” Plos One, vol. 10, no. 8, Article No. e0136213, 2015.  
[53] Q. Chen, et al., “A limited-angle CT reconstruction method based on anisotropic TV minimization,” Phys. Med. Biol., vol. 58, no. 7, pp. 2119-2141, Mar. 2013.  
[54] G. Zeng, Medical Imaging Reconstruction: A Conceptual Tutorial. Beijing and Berlin, China and Germany: 2010, pp. 21-30.  
[55] S. Hashemi, et al., “Simultaneous deblurring and iterative reconstruction of CBCT for image guided brain radiosurgery,” Phys. Med. Biol., vol. 62, pp. 2521-2541, 2017.  
[56] P. Bao, et al., “Few-view CT reconstruction with group-sparsity regularization,” Int. J. Numer. Meth. Biomed. Eng., vol. 34, Article No. e3101, 2018.  
[57] E. Kim, et al., “Recent advances in proteomic studies of adipose tissues and adipocytes,” Int. J. Mol. Sci., vol. 16, no. 3, pp. 4581-4599, 2015.