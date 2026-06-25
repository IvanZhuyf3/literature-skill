# Sparsely-sampled hyperspectral stimulated Raman scattering microscopy: A theoretical investigation

Haonan Lina, Chien-Sheng Liaoa, Pu Wanga, Kai-Chih Huanga, Charles A. Boumane, Nan Konga, and Ji-Xin Chenga,b,c,d,e

aWeldon Schoold of Biomedical Engineering, Purdue University, West Lafayette, Indiana, USA bDepartment of Chemistry, Purdue University, West Lafayette, Indiana, USA cPurdue University Center for Cancer Research, Purdue University, West Lafayette, Indiana, USA

dBirck Nanotechnology Center, Purdue University, West Lafayette, Indiana, USA eSchool of Electrical and Computer Engineering, Purdue University, West Lafayette, Indiana, USA

## ABSTRACT

A hyperspectral image corresponds to a data cube with two spatial dimensions and one spectral dimension. Through linear un-mixing, hyperspectral images can be decomposed into spectral signatures of pure components as well as their concentration maps. Due to this distinct advantage on component identification, hyperspectral imaging becomes a rapidly emerging platform for engineering better medicine and expediting scientific discovery. Among various hyperspectral imageing techniques, hyperspectral stimulated Raman scattering (HSRS) microscopy acquires data in a pixel-by-pixel scanning manner. Nevertheless, current image acquisition speed for HSRS is insufficient to capture the dynamics of freely moving subjects. Instead of reducing the pixel dwell time to achieve speed-up, which would inevitably decrease signal-to-noise ratio (SNR), we propose to reduce the tota number of sampled pixels. Location of sampled pixels are carefully engineered with triangular wave Lissajous trajectory. Followed by a model-based image in-painting algorithm, the complete data is recovered for linear unmixing. Simulation results show that by careful selection of trajectory, a fill rate as low as 10% is sufficient to generate accurate linear unmixing results. The proposed framework applies to any hyperspectral beam-scanning imaging platform which demands high acquisition speed.

Keywords: Hyperspectral imaging, sparse sampling, image in-painting, inverse problem, Markov random field, maximum a-posterior estimation

## 1. INTRODUCTION

Hyperspectral imaging is a novel imaging modality which originated from remote sensing.1 Compared with traditional imaging modalities, hyperspectral imaging acquires a series of two-dimensional images across a wide range of spectrum.2 In other words, a hyperspectral image is a collection of spatially correlated spectra. The extensive spectral information could provide specificity for identification of various pure components without prior knowledge. Such distinct advantage has been exploited in a broad variety of applications, such as those in mineral detection,3 food quality and safety control,4 tree species identification,5 surgical guidance,6 and crime scene detection.7

Among various hyperspectral imaging techniques, hyperspectral stimulated Raman scattering (HSRS) microscopy has become a power tool in basic biological science and medical diagnosis with unique advantages such as intrinsic optical sectioning ability and label-free characteristic. Since SRS is a nonlinear optical process, the signal intensity shows a quadratic or higher-order relationship with the input laser energy.8 Therefore, imaging

Further author information: (Send correspondence to N.K. and J.-X.C.)

N.K.: Email: nkong@purdue.edu, Telephone: 1 765 496 1459

J.-X.C.: E-mail: jcheng@purdue.edu, Telephone: 1 765 494 4335 acquisition by focusing the excitation laser at each pixel and scanning point-by-point on the sample is the popular approach among nonlinear optical sensing instruments. However, since each hyperspectral image consists of tens to hundreds of 2D images, the huge amount of pixels results in long total acquisition time. Up-to-date acquisition speed for HSRS microscopy is 3 seconds per data cube,9 which is insufficient to capture highly dynamic living samples. If image acquisition speed increased by 10 times, it is possible to observe the dynamics of chemical reactions in living subjects, e.g., metabolites during drug delivery process, which can greatly benefit the fundamental study of drug design.10 Nevertheless, pushing the limit of imaging speed by reducing pixel dwell time (i.e., integration time at each pixel) is challenging, because signal will decrease accordingly, and consequently, be overwhelmed by laser shot noise, thermal noise and electronic noise.

To push the limit of imaging speed, we propose to take an alternative route, which reduces the total number of sampled pixels while maintaining necessary pixel dwell time. In this work, we sparsely sample the raw hyperspectral data cubes, and recover the void pixels based on information from the adjacent pixels in both spatial and spectral domains.

Our approach includes two key innovations. First, to ensure that a limited number of sampled pixels are evenly dispersed within each data cube, we propose an innovative trajectory design, termed 3D triangular wave Lissajous trajectory with high least common multiplier (LCM). In this design, triangular wave makes sampling evenly distributed in the data cube, and high LCM ensures that the designed trajectory has a complicated pattern to cover all areas in the data cube. Moreover, 3D trajectory makes trajectory discrete at each spectral frame of each date cube, thus reducing spatial artifacts induced by the sampling trajectory. Second, an image in-painting algorithm is required to recover the complete image from the sparsely-sampled raw image. Given the unique properties of hyperspectral image, we present a model-based image in-painting algorithm which incorporates both spatial and spectral correlations among adjacent pixels in the data cubes. The algorithm models such correlations via maximum a-posterior (MAP) estimation with prior model being a Markov random field (MRF). Since original data is not directly observed, and the number of sampled pixels is far less than the total number of pixels, this image reconstruction problem is well known to be an ill-posed inverse problem, which is difficult in that it is difficult to derive a single stable solution. Our proposed algorithm addresses the problem via incorporating additional constraints as priors.

To demonstrate the viability of our approach, we use existing fully-sampled HSRS images to generate the corresponding sparsely-sampled raw data with each of the four candidate sampling trajectories. These images are then recovered by applying our proposed model-based image in-painting algorithm on the sparsely-sampled data. Finally, we decompose the reconstructed images into concentration maps of pure components using multivariate curve resolution-alternating least squares (MCR-ALS).11 Quality of the resultant concentration maps is assessed by the widely-accepted structural similarity (SSIM) index.12 Simulation results suggest that, for HSRS images of two types of mixed beads, sampling 10% of the pixels is necessary for reconstructing complete images without much spatial and spectral information loss. Therefore, through reducing the amount of pixels collected in the data cubes, we could improve the image acquisition speed by one order of magnitude.

The remainder of this paper is organized as follows. Section 2 explains the triangular wave Lissajous trajectory in detail. Specifically, properties of triangular wave Lissajous trajectory are presented, its comparison with sinusoidal Lissajous trajectory is discussed, the effects of frequency ratio on the property of the trajectory are described, and comparisons between 2D and 3D trajectories are made. Section 3 describes the model-based image in-painting algorithm in the context of sparsely-sampled hyperspectral imaging. In section 4, results and corresponding discussions are presented to evaluate various trajectory designs and establish the relationship between fill rate and image quality. We provide concluding remarks and outline future research in section 5.

## 2. SPARSE SAMPLING TRAJECTORY SELECTION

For beam-scanning imaging instruments, the sampling trajectory determines how to arrange the order of scanned pixels and thus influences the reconstruction of an image. Raster scan, a commonly used beam-scanning setup, samples pixels row by row from top left to bottom right. Due to its additional dimension, a hyperspectral image is scanned by raster order in a frame-by-frame manner, and each frame is a 2D image with identical spectral information. In such manner, a video stream of hyperspectral data cubes is created. Despite that raster scan is easy to achieve experimentally and directly provides a fully-sampled image, it unavoidably provides redundant information in the sense that each pixel may be highly correlated with its adjacent pixels, and thus many pixels are likely to follow similar intensity distributions.13 On the other hand, sampling pixels randomly provides more valuable information per pixel, because each sampled pixel provides intensity information that is hardly inferred from other distant pixels sampled. While complete random scan is impossible experimentally, reducing redundant information among pixels can be achieved to some extent via Lissajous trajectories.

A conventional 2D Lissajous trajectory is generated by controlling both x and y positions to follow sinusoidal waveforms, which are mathematically described as:

$$
x = A \sin (a t + \delta), \quad y = B \sin (b t), \tag {1}
$$

In equation 1, A and B represent the amplitudes of the sinusoids along x and y axes, δ indicates the phase difference between the two axes, and $^ { a , }$ b correspond to the frequencies of the two waves. Ratio of the two wave frequencies determines the trajectory pattern. A low least common multiplier (LCM) of the two frequencies results in a simple pattern which repeats itself rapidly and covers only a small portion of the pixels, such pattern is problematic since a huge amount of pixels are never sampled (see figure 1a). Therefore, a pattern complicated enough to cover every pixel in its trajectory is needed to capture enough information for image reconstruction. A high LCM for the two frequencies fulfills this requirement, which leads to a trajectory that guarantees every pixel to be sampled multiple times before the trajectory repeats, in other words, the data cube will be fully sampled if such trajectory runs long enough (see figure 1c). Consequently, fill rate selection becomes plausible through determining the number of sampled pixels in each frame and dividing the continuous trajectory into sub-trajectories. Thus, a video stream of data cubes is created, and each data cube is sparsely-sampled where only pixels along each sub-trajectory are sampled.

![](images/8ce0f53ba4fc780fccb35aa823ce1382bc80e31b9d2a43aa2ac0309ea951cc66.jpg)

<details>
<summary>line chart</summary>

| X   | Y   |
| --- | --- |
| 0   | 0   |
| 50  | 180 |
| 100 | 30  |
| 150 | 42  |
| 200 | 54  |
</details>

(a)

![](images/8799ace961152098aa08a76b5b684784789b66f021786284afcb0b48db08b621.jpg)

<details>
<summary>line chart</summary>

| X   | Y   |
|:----|:----|
| 0  | 0  |
| 10 | 10 |
| 20 | 20 |
| 30 | 30 |
| 40 | 40 |
| 50 | 50 |
| 60 | 60 |
| 70 | 70 |
| 80 | 80 |
| 90 | 90 |
| 100| 100|
| 110| 110|
| 120| 120|
| 130| 130|
| 140| 140|
| 150| 150|
| 160| 160|
| 170| 170|
| 180| 180|
| 190| 190|
| 200| 200|
</details>

(b)

![](images/752f8d98299e7f1b86db780c7d2012cabba3acf2e97e2eed20528579fbe0ad42.jpg)

<details>
<summary>heatmap</summary>

| X    | Y    | Value |
|------|------|-------|
| 50   | 20   | 32    |
| 50   | 40   | 30    |
| 50   | 60   | 28    |
| 50   | 80   | 26    |
| 50   | 100  | 24    |
| 50   | 120  | 22    |
| 50   | 140  | 20    |
| 50   | 160  | 18    |
| 50   | 180  | 16    |
| 50   | 200  | 14    |
| 100  | 20   | 32    |
| 100  | 40   | 30    |
| 100  | 60   | 28    |
| 100  | 80   | 26    |
| 100  | 100  | 24    |
| 100  | 120  | 22    |
| 100  | 140  | 20    |
| 100  | 160  | 18    |
| 100  | 180  | 16    |
| 100  | 200  | 14    |
| 150  | 20   | 32    |
| 150  | 40   | 30    |
| 150  | 60   | 28    |
| 150  | 80   | 26    |
| 150  | 100  | 24    |
| 150  | 120  | 22    |
| 150  | 140  | 20    |
| 150  | 160  | 18    |
| 150  | 180  | 16    |
| 150  | 200  | 14    |
| 200  | 20   | 32    |
| 200  | 40   | 30    |
| 200  | 60   | 28    |
| 200  | 80   | 26    |
| 200  | 100  | 24    |
| 200  | 120  | 22    |
| 200  | 140  | 20    |
| 200  | 160  | 18    |
| 200  | 180  | 16    |
| 200  | 200  | 14    |
</details>

(c)

![](images/4da594f1c8b92e89831e5785067638ba41b297e4b242333b8d10d716ce230092.jpg)

<details>
<summary>heatmap</summary>

| X\Y | 200 | 180 | 160 | 140 | 120 | 100 |
|-----|-----|-----|-----|-----|-----|-----|
| 0   | 32  | 30  | 28  | 26  | 24  | 22  |
| 50  | 30  | 28  | 26  | 24  | 22  | 20  |
| 100 | 28  | 26  | 24  | 22  | 20  | 18  |
| 150 | 26  | 24  | 22  | 20  | 18  | 16  |
| 200 | 24  | 22  | 20  | 18  | 16  | 14  |
</details>

(d)  
Figure 1. Comparison between sinusoidal and triangular wave Lissajous trajectories. Example trajectories for 7 : 8 sinusoidal (1a) and triangular wave Lissajous (1b) with equal amplitudes. Pixel sampling density maps for 7.082 : 8.002 sinusoidal (1c) and triangular wave Lissajous (1d) given the same 1 million sampled pixels. It is clear that triangular wave pattern has much less biased sampling density.

We have witnessed pioneering applications of Lissajous trajectory in various fields, including beam-scanning two-photon excitation fluorescence (TPEF) microscopy14–17 and atomic force microscopy (AFM).18, 19 However, further image reconstruction is not applied to any of the above applications to recover the entire image from sparsely-sampled raw data, making visual perception of the data difficult under low fill rates. Unlike above applications, Sullivan et. al20 recently combined high LCM Lissajous with image in-painting for laser-scanning second harmonic generation (SHG). As a result, their work could achieve kHz imaging speed for SHG. In their work, a complex trajectory is divided into simple-pattern sub-trajectories, each of which represents a sparselysampled time frame. Adjacent sub-trajectories contain different pixels sampled, values of missed pixels can be statistically inferred by sampled pixels in adjacent time frames given time domain correlations. To the best of our knowledge, there are very few papers that attempt to harnesses high LCM Lissajous trajectory and embed its design into image in-painting. However, due to the nature of sinusoids, the sampling trajectory leads to biased sampling density, leading to less sampled pixels in the central region of the data cube, therefore, image quality in the central region is worse compared with edge, which is less satisfactory.

In this paper, we propose to implement triangular wave to design Lissajous trajectory with more uniformed sampling density; see figure 1. This figure of sampling density map shows the trajectories for 7 : 8 sinusoidal and triangular wave Lissajous trajectories, and compares the sampling density maps of the two trajectories with same frequencies (7.082 : 8.002) for the two axes. It is clear that sinusoidal Lissajous has higher sampling density at the edge of the image, indicating that a higher image quality is achieved at the edge. This bias likely leads to unsatisfying reconstruction as one usually requires higher image quality at the center of the image. Nevertheless, triangular wave could potentially address the above problem by generating more uniform sampling density than sinusoidal wave. Meanwhile, triangular wave is experimentally achievable by galvo mirrors or polygon mirrors.

![](images/4f6ccb24831b39ed008fd15c6801dc2ad5f1e4e6e664e70a41ebc7e582fda7d9.jpg)  
Figure 2. Comparison between 2D and 3D triangular wave Lissajous patterns. 2a shows one frame in the data cube with 7.082 : 8.002 and 10% sampling fill rate. 2b shows one frame in the data with 7.082 : 8.002 : 9.054 frequencies ratio and same fill rate. Comparison shows that 3D pattern has a more random sampling pattern.

Furthermore, we explore the potential advantage of using 3D sparse sampling for hyperspectral image inpainting. A 3D Lissajous trajectory can be constructed by setting all three axes $( x , y , \lambda )$ to follow some wave functions, e.g., either sinusoidal or triangular waves. Three frequencies are chosen so that they will have an even higher LCM, compared to the 2D cases. Choosing a 3D Lissajous trajectory has the following advantage; see figure 2. This figure shows part of the sub-trajectories in one spectral frame in the data cube for 3D and 2D trajectories, both with 10% fill rate. These sub-trajectories indicate that a 3D trajectory has advantage over a 2D trajectory in that the sampled pixels in each spectral frame are scattered discretely, rather than aligned along a continuous line. Hence, each spectral frame in the data cube contains less trajectory-induced artifacts. As randomness increases, lower sampling rate is sufficient to extract necessary information for image in-painting.

Based on the discussion in this section, we propose a novel design of 3D triangular wave Lissajous trajectory with high LCM for the three frequencies. Given a specific fill rate, the complex trajectory is divided into subtrajectories, each of which forms an individual hyperspectral data cube and contains a number of pixels specified by the fill rate. With reduced fill rate, this trajectory design can increase the speed of acquiring raw data cubes without much information loss and leads to hyperspectral imaging applications in studying the internal dynamics of living biological samples. However, as mentioned in section 1, acquired sparsely-sampled data cubes are not directly usable, since a huge number of pixels are missing and further segmentation is not applicable. Hence, a model-based 3D image in-painting algorithm is proposed in the following section to reconstruct a series of complete hyperspectral images efficiently and accurately.

## 3. MODEL-BASED IMAGE IN-PAINTING

A sparsely-sampled hyperspectral image leaves a large amount of un-sampled pixels. To increase imaging speed significantly, e.g., tenfold, only a small portion of pixels in each data cube will be sampled. Nevertheless, due to the nature of triangular wave Lissajours trajectory, sampled pixels are scattered within the resultant data cube more evenly. This property ensures that for each un-sampled pixel, there will be more accurate information about the intensities of spatially adjacent pixels in the same frame or spectrally adjacent frames. Hence, these intensity values can be utilized to provide more accurate inferences on those un-sampled pixels. This problem of inferring the complete image from sampling results is called an inverse problem. Since the number of samples is less than the total number of pixels, this inverse problem is ill-posed. For an ill-posed inverse problem, we apply maximum a-posterior (MAP) estimation since it is able to take into account both the underlying imaging process and the initial understanding on the correlation of neighboring pixels in a Bayesian manner. More specifically, we use a Markov random field (MRF) to specify the prior model. As a result, we can dramatically reduce the dimensionality of each unknown image, and consequently, improve the reconstruction of the images. We present the detailed mathematical treatment to the problem in the remainder of the section.

First of all, we model the underlying imaging process with the following equation:

$$
y = A x + w. \tag {2}
$$

In equation 2, y is the sparsely sampled data; x is the complete data to recover; w is assumed to be independent, identically distributed (i.i.d) zero-mean Gaussian noise $N ( 0 , \Lambda ^ { - 1 } )$ , modeling laser shot noise, thermal noise and electronic noise; and A is an $M \times N$ modulation matrix, representing how original data contributes to each sampled pixel, additionally, each column in A corresponds to a pixelated version of point spread function (PSF). The dimensions of y and w are both M, which equal the number of sampled pixels; while the dimension of x is $N$ , which is the total number of pixels in each hyperspectral data cube. The inverse problem aims at obtaining an estimate of x, that would best match the actual measurements given the prior model constraints. As convention, $y , x$ and w are reshaped as column vectors by arranging the 3D hyperspectral data in raster order. In current setup, no blurring effect is considered since we assume the scanning step size is larger than the laser spot size. Thus for A, there is only one non-zero element in each row. The location of the non-zero element is determined by the trajectory pattern.

Our proposed MAP-MRF estimation is established based on Bayesian theory, which is a general framework used to describe the conditional distribution of x given y:

$$
P (x | y) = \frac {P (y | x) P (x)}{P (y)}. \tag {3}
$$

In equation 3, $P ( x | y )$ is the conditional distribution of original image x given sampled data $y , P ( y | x )$ is the conditional distribution of sampled data y given original image x and $P ( x )$ is the assumption on the distribution of original image x. $P ( y )$ is independent of $x ,$ thus this term can be ignored for the task to find the best estimate of the original image, denoted by ˆx. If we have appropriate models for $P ( \boldsymbol { y } | \boldsymbol { x } )$ and $P ( x )$ , solving ˆx is equivalent to maximizing $P ( x | y )$ . To efficiently obtain the best estimate, three key issues need to be addressed: forward model, prior model, and optimization method.

The forward model, $P ( \boldsymbol { y } | \boldsymbol { x } )$ , is formulated based on the imaging equation. Given original data, the distribution of sampled image is determined by the distribution of noise, which is presented as:

$$
P (y | x) = \frac {1}{(2 \pi \sigma_ {w} ^ {2}) ^ {M / 2}} \exp \left\{- \frac {1}{2 \sigma_ {w} ^ {2}} \| y - A x \| ^ {2} \right\}. \tag {4}
$$

The above expression shows a multivariate Gaussian distribution for M i.i.d. zero-mean Gaussian noise, in which the variance is denoted by $\sigma _ { w } ^ { 2 }$ .

The prior model mathematically describes the assumption on the distribution of the original image. Using the fact that adjacent pixels are spectrally and spatially correlated, we can formulate the prior model using an MRF, which describes a random process with the following property:

$$
\mathbb {E} [ x _ {n} | x _ {i} \text {for} i \neq n ] = \mathbb {E} [ x _ {n} | x _ {i} \text {for} i \in \partial n ], \tag {5}
$$

where

$$
\partial n = \{i \in [ 1,..., N ]: i \neq n a n d | i - n | \leq P \}. \tag {6}
$$

In equation 5, ∂n represents a set containing P neighbors on either side of $n ,$ as shown in equation 6, except for the boundary where neighbors exceeding the boundary are truncated. MRF is elegant in that it only describes the random process at each pixel by its neighbors while it is able to maintain global correlations among distant pixels.21 Such property of MRF keeps essential information for the hyperspectral images while maintaining computational tractability in the estimation.

Further, we elect to use a generalized Gaussian MRF (GGMRF) model22 to specify that adjacent pixel values follow non-Gaussian distributions with similar means. This prior model is formulated by replacing the quadratic relationship for the differences between adjacent pixel values in a Gaussian MRF model with a value p that is slightly larger than 1 so as to reduce large penalty for distinct pixel values. Such p value better preserves sharp edges in images and guarantees convergence as well. Specifically, p is chosen as 1.05 in this work. The GGMRF prior in the context of hyperspectral imaging is describes as:

$$
P (x) = \frac {1}{z} \exp \left\{- \frac {1}{p \sigma_ {x} ^ {p}} \sum_ {\{i, j \} \in C} g _ {i - j} \left| x _ {i} - x _ {j} \right| ^ {p} - \frac {1}{p \sigma_ {x} ^ {\lambda}} \sum_ {\{u, v \} \in \Lambda} r _ {u - v} \left| x _ {u} - x _ {v} \right| ^ {p} \right\}. \tag {7}
$$

Each pixel in the hyperspectral image possesses spatial and spectral neighbors. Spatial neighbors are spatially adjacent pixels in the same spectral frame whereas spectral neighbors are spectrally adjacent pixels at the same spatial location. In equation 7, C and Λ represent the collection of spatial and spectral cliques, $g _ { i - j }$ and $r _ { u - v }$ specify spatial and spectral neighborhood weights, which are considered separately due to their distinct physical meanings. In this work, specific neighborhood weights are chosen as shown in table 1:

Table 1. Spatial and spectral neighbors

<table><tr><td>1/12</td><td>1/6</td><td>1/12</td></tr><tr><td>1/6</td><td>0</td><td>1/6</td></tr><tr><td>1/12</td><td>1/6</td><td>1/12</td></tr></table>

<table><tr><td>1/2</td><td>0</td><td>1/2</td></tr></table>

In equation $7 , C$ is the set of spatial neighbors and Λ is the set of spectral neighbors. Combining equations 4 and 7, we can formulate a cost minimization problem by taking the logarithm of equation 3 and ignoring constant term $P ( y )$ :

$$
\hat {x} = \underset {x} {\arg \min} \left\{\frac {1}{2 \sigma_ {W} ^ {2}} \| y - A x \| ^ {2} + \frac {1}{p \sigma_ {x} ^ {p}} \sum_ {\{i, j \} \in C} g _ {i, j} | x _ {i} - x _ {j} | ^ {p} + \frac {1}{p \sigma_ {x} ^ {\lambda}} \sum_ {u, v \in \Lambda} r _ {u, v} | x _ {u} - x _ {v} | ^ {p} \right\}. \tag {8}
$$

The constraint for this optimization problem is that pixel values are between 0 and 255. Finally, to solve the above high-dimensional optimization problem, we use iterative coordinate descent (ICD) optimization method, which sequentially minimizes the cost function with respect to each pixel.23

## 4. RESULTS AND DISCUSSION

In this section, we first compare reconstruction results over the sampling trajectories discussed in section 2 to confirm better trajectory designs. Then we quantify the relationship between the sampling fill rate and reconstruction quality. To conduct these experiments, we chose the imaging samples to be polystyrene and poly(methyl methacrylate) beads with two distinct spectra, and acquired a fully sampled $2 0 0 \times 2 0 0 \times 1 0 0$ hyperspectral SRS image. One of the entire 100 frames in the hyperspectral data cube (namely frame 45) was chosen because the two types of beads are both visible in this frame but of different intensity values so the two types are expected to be distinguishable (see figure 3). The figure also shows the multivariate curve resolution (MCR) reconstruction results, including pure spectra of the two kinds of beads and their corresponding concentration maps. MCR is a spectral un-mixing technique which decomposes a hyperspectral image into the product of pure components spectra and their concentration maps. After performing MCR, concentration maps of the two species were then embedded into one false color image by assigning red and green to the two types of the components. Thus, it is easy to visually identify different types of components and their spatial distributions.

In our experiments, the aforementioned hyperspectral data cube was taken as the input to generate sparselysampled data by recording only pixel values along the specified trajectories. Next, image in-painting was performed to recover the complete image to be used for MCR. Finally, quality of the concentration maps was evaluated by a pair of structural similarity (SSIM) indexes calculated in terms of two components.

![](images/8c444ac2032e99f2df8f49c55292381aba742611214cc74cbb1ea7d80d5aadb5.jpg)

<details>
<summary>natural_image</summary>

Abstract pattern of scattered white dots on a black background, resembling a starry or pixelated graphic (no text or symbols)
</details>

(a)

![](images/83832f7d111339bfb54acc53efa42bded869c567a2436b5891c59a77eb11ae85.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing red and green fluorescent particles on a black background (no text or symbols)
</details>

(b)

![](images/64c1735a82b917c16635455b786d990ff8f9576898e83b1a6d08b0c503813081.jpg)

<details>
<summary>line chart</summary>

| spectral channel | relative intensity (red) | relative intensity (green) |
| ---------------- | ------------------------ | -------------------------- |
| 0                | 0.0                      | 0.0                        |
| 10               | 0.0                      | 0.0                        |
| 20               | 0.0                      | 0.1                        |
| 30               | 0.0                      | 0.05                       |
| 40               | 0.1                      | 0.07                       |
| 50               | 0.3                      | 0.29                       |
| 60               | 0.1                      | 0.1                        |
| 70               | 0.0                      | 0.0                        |
| 80               | 0.0                      | 0.0                        |
| 90               | 0.0                      | 0.0                        |
| 100              | 0.0                      | 0.0                        |
</details>

(c)  
Figure 3. HSRS image $( 2 0 0 \times 2 0 0 \times 1 0 0 )$ of two types of beads with distinct spectra. 3a is frame 45 in the hyperspectral image, in which two types of beads are visible but of different luminance levels. 3b and 3c are MCR results of the hyperspectral image, including concentration maps and pure spectra for each pure component.

## 4.1 Sinusoidal versus Triangular Wave Lissajous Trajectory

As mentioned in section 2, sinusoidal trajectory provides biased sampling density, making more sampled pixels at the edge. Such problem is expected to make the reconstruction quality of the central region worse than desired. Triangular trajectory could solve the problem by providing unbiased sampling density. We thus compared the reconstruction results for these two 3D trajectories under 10% sampling density, and ratios for the frequencies in the three dimensions were 7.082 : 8.002 : 9.054 for both trajectories.

![](images/d0b3d90faa9250c2edfc66c7f4afefdaa05f965d30911c1086f238e3950cfb6c.jpg)

<details>
<summary>mixed chart</summary>

| Category | Relative Intensity |
| :--- | :--- |
| Sinusoidal Lissajous | 0.3 |
| Triangular Lissajous | 0.3 |
| MCR pure spectra & SSIM index | Relative Intensity |
| Pure spectra | Relative Intensity |
| SSIM index | Relative Intensity |
| Red | 0.4077 |
| Green | 0.4284 |
| SSIM index | Relative Intensity |
| Red | 0.5522 |
| Green | 0.5852 |
</details>

Figure 4. Comparison between sinusoidal and triangular Lissajous trajectories with the same frequencies ratio $( 7 . 0 8 2 : 8 . 0 0 2 : 9 . 0 5 4 )$ and fill rate (10%). The upper row contains the reconstruction result using sinusoidal trajectory whereas the lower row is the result for triangular trajectory. The frame in the hyperspectral image, MCR concentration maps, and SSIM index, all indicate that triangular trajectory achieves better performance than sinusoidal trajectory for the same fill rate.

Figure 4 shows the reconstructed data for frame 45 and its linear un-mixing results for the two different trajectories. Reconstructed frame clearly shows that for beads in the central part of the image, triangular trajectory provides more accurate luminance and more clear beads structure. Concentration maps of the two species further prove that with sinusoidal trajectory, the central part is distorted so severely that the two types of beads are not distinguishable. Such image quality is problematic, since we are usually more interested in the objects in the center of the image. Moreover, the SSIM index was calculated to assess the quality of obtained concentration maps via MCR. Triangular trajectory yields a higher value of SSIM index for both types of beads, which also verifies that triangular wave trajectory is advantageous over sinusoidal trajectory.

## 4.2 2D versus 3D Triangular Wave Lissajous Trajectory

Hyperspectral beam-scanning microscopy allows for sparse sampling along both spatial and spectral dimensions. Such property makes it possible to sample hyperspectral data cubes with 3D trajectories. To compare the difference between 2D and 3D trajectories, we generated two different sets of sparsely-sampled raw data based on 2D triangular wave Lissajous (7.082 : 8.002) and 3D triangular wave Lissajous $( 7 . 0 8 2 : 8 . 0 0 2 : 9 . 0 5 4 )$ , respectively, both with 10% fill rate.

Reconstruction results shown in figure 5 indicate that 3D trajectory introduces less trajectory-induced artifacts and better maintains the structure of the beads. Since both trajectories have complex patterns, spectrally adjacent frames have distinct sampling pixels in both cases, therefore, distortion on one spectral frame could be compensated by adjacent spectral frames. As a result, the two trajectories provide similar un-mixing quality. However, SSIM index results still suggest that 3D trajectory is slightly better than 2D trajectory in terms of the MCR results.

![](images/3bb0b2d9674d740866ac054ea550cfbee65c9e2078673cce0fc66751745f5042.jpg)

<details>
<summary>mixed chart</summary>

| Condition | Red Relative Intensity | Green Relative Intensity |
|-----------|------------------------|--------------------------|
| Frame 45 | 0.5376                 | 0.5577                   |
| 3D Lissajous | 0.5522                 | 0.5852                   |
</details>

Figure 5. Comparison between 2D and 3D triangular Lissajous trajectories with same frequencies ratio (7.082 : 8.002 : 9.054) and fill rate(10% fill rate). The upper row and lower row each represents results of 2D trajectory and 3D trajectory. The frame in the hyperspectral image shows that 3D trajectory has less distortion, the linear un-mixing results also show 3D trajectory is slightly better than 2D.

## 4.3 Fill Rate versus Reconstruction Quality

From the above two experiments, we conclude that 3D triangular wave Lissajous trajectory is a promising selection for sparsely-sampling of hyperspectral images. We then investigate the relationships between the sampling fill rate and spectral unmixing quality. Although it is intuitive that image reconstruction quality is positively correlated with sampling fill rate, this relationship is not simply linear. Frame 45 of the hyperspectral image reconstructed from the raw data with the fill rate ranging from 5% to 30% are shown in figure 6a; the corresponding MCR concentration maps are shown in figure 6b; and the curve for fill rate vs. SSIM index is displayed in figure 6c.

A fill rate as low as 5% can yield sufficient reconstruction quality for the general structure of the beads, but finer details appear as the fill rate increases. For MCR concentration maps, an SSIM value of 0.6 is sufficient to visually distinguish the two bead types and identify their structures. However, due to redundancy of the pixels in adjacent regions, increasing fill rate does not linearly improve the image quality, which can be seen in Figure 6c. The trend of the slope is determined by the structural complexity of the imaging sample. If the sample has a simple structure, e.g., the sample is the interface between water and oil, then a low fill rate ensures the reconstruction quality. On the contrary, for complex structures such as living C. Elegans, the fill rate needs to be relatively high to recover necessary information. Calculation of the theoretical upper bound on the fill rate has been seen in the compressive sensing literature, which is dependent on the sparsity of the image in the wavelet domain.24

Additionally, two less significant computational observations are also made during our experiments. First, the image in-painting algorithm is insensitive to the selection of the spatial and spectral neighborhood structures as long as the overall probability distribution of the MRF ensures that pixels within close proximity spatially and spectrally have sufficient correlations. Second, setting upper and lower bounds on the pixel intensity values significantly reduces the number of iterations needed in the optimization to reach satisfactory results.

![](images/9785166db72f4cf39bb8921a6ba03d19e1a823249cd6a4807603a520d8ca1ad0.jpg)

(b) MCR concentration maps  
![](images/574335b91404e9a2ec489cb2d27c96340b0504d03c7200d7a248f85619c6c931.jpg)

<details>
<summary>line chart</summary>

| fill rate (%) | SSIM index (green) | SSIM index (red) |
| ------------- | ------------------ | ---------------- |
| 5             | 0.3                | 0.3              |
| 10            | 0.6                | 0.55             |
| 15            | 0.67               | 0.66             |
| 20            | 0.74               | 0.67             |
| 30            | 0.8                | 0.75             |
</details>

(c)  
Figure 6. Reconstruction results using different fill rate from 5% to 30%, with the same 3D triangular Lissajous trajectory setup. 6a and 6b display the reconstructed hyperspectral images for the same frame and their corresponding MCR concentration maps. 6c shows the curves representing the relationship between the fill rate and image quality (measured by the SSIM index). Results show that the image quality is not linearly correlated to the fill rate, and a fill rate as low as 10% can generate MCR concentration maps with visually correct results.

## 5. CONCLUSIONS AND FUTURE WORK

In this paper, we use simulations to demonstrate that for HSRS imaging of two types of mixed beads, our nove 3D triangular wave Lissajous trajectory design could increase the imaging speed by about one order of magnitude without significant loss of spatial and spectral quality. Triangular wave alleviates biased pixel scanning as opposed to the sinusoidal wave, and the 3D trajectory design provides a higher level of randomness as opposed to its 2D counterpart. An MAP-MRF based image in-painting algorithm is applied to take the sparsely-sampled data and reconstruct the complete image efficiently and accurately. Furthermore, this design applies to any beam-scanning hyperspectral imaging system which can generate data in a frame-by-frame manner.

For actual implementation of the trajectory design, since each data cube is formed by dividing the continuous trajectory into sub-trajectories based on self-defined fill rate, the imaging speed is real-time adjustable, depending on how significant the motion of the imaging sample is. On one hand, finer details come with higher fill rates, while on the other hand, higher fill rates result in more severe motion artifacts for moving objects. Thus, a trade off between structural details and motion artifacts exists. Through real-time assessment, we can optimize the fill rate to achieve the best image quality according to different samples, which will be considered in our future work.

Due to the high dimensionality of hyperspectral images, ICD optimization takes a long time to complete. Thus, the image in-painting is slow compared to image acquisition, which means real-time analysis of imaging data is not achievable currently. In the future, we plan to adapt GPU parallel computing to speed up the in-painting. Additionally, since hyperspectral imaging aims at generating concentration maps of pure components, the development of more robust spectral un-mixing algorithms which is able to deal with highly sparse hyperspectral data is imperative.

## ACKNOWLEDGMENTS

This work is supported by a Keck Foundation Grant to J.-X.C.

## REFERENCES

[1] Goetz, A. F., “Three decades of hyperspectral remote sensing of the earth: A personal view,” Remote Sensing of Environment 113, S5–S16 (2009).  
[2] Chang, C.-I., [Hyperspectral Imaging: Techniques for Spectral Detection and Classification ], vol. 1, Springer Science & Business Media (2003).  
[3] Abrams, M. J., Ashley, R. P., Rowan, L. C., Goetz, A. F., and Kahle, A. B., “Mapping of hydrothermal alteration in the cuprite mining district, Nevada, using aircraft scanner images for the spectral region 0.46 to 2.36 µm,” Geology 5(12), 713–718 (1977).  
[4] Gowen, A. A., O’Donnell, C. P., Cullen, P. J., Downey, G., and Frias, J. M., “Hyperspectral imaging–an emerging process analytical tool for food quality and safety control,” Trends in Food Science & Technology 18(12), 590–598 (2007).  
[5] Wessman, C. A., Aber, J. D., Peterson, D. L., and Melillo, J. M., “Remote sensing of canopy chemistry and nitrogen cycling in temperate forest ecosystems,” Nature 335(8), 154–156 (1988).  
[6] Afromowitz, M. A., Callis, J. B., Heimbach, D. M., DeSoto, L. A., and Norton, M. K., “Multispectral imaging of burn wounds: A new clinical instrument for evaluating burn depth,” IEEE transactions on Biomedical Engineering 35(10), 842–850 (1988).  
[7] Kuula, J., P¨ol¨onen, I., Puupponen, H.-H., Selander, T., Reinikainen, T., Kalenius, T., and Saari, H., “Using VIS/NIR and IR spectral cameras for detecting and separating crime scene details,” in [Sensors, and Command, Control, Communications, and Intelligence (C3I) Technologies for Homeland Security and Homeland Defense XI], Proc. SPIE 8359 (2012).  
[8] Cheng, J.-X. and Xie, X. S., [Coherent Raman Scattering Microscopy], CRC press (2012).  
[9] Liao, C.-S., Slipchenko, M. N., Wang, P., Li, J., Lee, S.-Y., Oglesbee, R. A., and Cheng, J.-X., “Microsecond scale vibrational spectroscopic imaging by multiplex stimulated Raman scattering microscopy,” Light: Science & Applications 4(3), e265 (2015).  
[10] Pathania, D., Millard, M., and Neamati, N., “Opportunities in discovery and delivery of anticancer drugs targeting mitochondria and cancer cell metabolism,” Advanced Drug Delivery Reviews 61(14), 1250–1275 (2009).  
[11] Jaumot, J., Gargallo, R., de Juan, A., and Tauler, R., “A graphical user-friendly interface for MCR-ALS: A new tool for multivariate curve resolution in MATLAB,” Chemometrics and Intelligent Laboratory Systems 76(1), 101–110 (2005).  
[12] Wang, Z., Bovik, A. C., Sheikh, H. R., and Simoncelli, E. P., “Image quality assessment: From error visibility to structural similarity,” IEEE Transactions on Image Processing 13(4), 600–612 (2004).  
[13] Chen, T., Wu, H. R., and Qiu, B., “Image interpolation using across-scale pixel correlation,” in [2001 IEEE International Conference on Acoustics, Speech, and Signal Processing. Proceedings (Cat. No.01CH37221) ], 3, 1857–1860 (2001).  
[14] Hoy, C. L., Durr, N. J., and Ben-Yakar, A., “Fast-updating and nonrepeating Lissajous image reconstruction method for capturing increased dynamic information,” Applied Optics 50(16), 2376–2382 (2011).  
[15] Flusberg, B. A., Cocker, E. D., Piyawattanametha, W., Jung, J. C., Cheung, E. L., and Schnitzer, M. J., “Fiber-optic fluorescence imaging,” Nature Methods 2(12), 941–950 (2005).  
[16] Flusberg, B. A., Jung, J. C., Cocker, E. D., Anderson, E. P., and Schnitzer, M. J., “In vivo brain imaging using a portable 3.9 gram two-photon fluorescence microendoscope,” Optics Letters 30(17), 2272–2274 (2005).  
[17] Engelbrecht, C. J., Johnston, R. S., Seibel, E. J., and Helmchen, F., “Ultra-compact fiber-optic two-photon microscope for functional fluorescence imaging in vivo,” Optics Express 16(8), 5556–5564 (2008).  
[18] Tuma, T., Lygeros, J., Kartik, V., Sebastian, A., and Pantazi, A., “High-speed multiresolution scanning probe microscopy based on Lissajous scan trajectories,” Nanotechnology 23(18), 185501 (2012).  
[19] Bazaei, A., Yong, Y. K., and Moheimani, S. R., “High-speed Lissajous-scan atomic force microscopy: Scan pattern planning and control design issues,” Review of Scientific Instruments 83(6), 063701 (2012).  
[20] Sullivan, S. Z., Muir, R. D., Newman, J. A., Carlsen, M. S., Sreehari, S., Doerge, C., Begue, N. J., Everly, R. M., Bouman, C. A., and Simpson, G. J., “High frame-rate multichannel beam-scanning microscopy based on Lissajous trajectories,” Optics Express 22(20), 24224–24234 (2014).  
[21] Li, S. Z., [Markov Random Field Modeling in Image Analysis ], Springer Science & Business Media (2009).  
[22] Bouman, C. and Sauer, K., “A generalized Gaussian image model for edge-preserving MAP estimation,” IEEE Transactions on Image Processing 2(3), 296–310 (1993).  
[23] Bertsekas, D. P., [Nonlinear Programming], Athena scientific Belmont (1999).  
[24] Cand\`es, E. J. and Wakin, M. B., “An introduction to compressive sampling,” IEEE Signal Processing Magazine 25(2), 21–30 (2008).