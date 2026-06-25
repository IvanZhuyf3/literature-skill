# The Parkinson’s disease drug entacapone disrupts gut microbiome homeostasis via iron sequestration

Received: 29 November 2023

Accepted: 10 October 2024

Published online: 21 November 2024

![](images/f8d6201b51e459e84918ecb57609d524fdc419fe1c84df3eed3ae4b5b5750248.jpg)

Check for updates

Fátima C. Pereira  1,2,11 , Xiaowei Ge  3,11, Jannie M. Kristensen  1 , Rasmus H. Kirkegaard  1,4, Klara Maritsch1 , Dávid Szamosvári5 , Stefanie Imminger  1 , David Seki1 , Juwairiyah B. Shazzad  2 , Yifan Zhu6 , Marie Decorte1 , Bela Hausmann  5,7, David Berry  1 , Kenneth Wasmund1,10, Arno Schintlmeister  1 , Thomas Böttcher  1,5, Ji-Xin Cheng  3,8 & Michael Wagner  1,9

Many human-targeted drugs alter the gut microbiome, leading to implications for host health. However, the mechanisms underlying these efects are not well known. Here we combined quantitative microbiome profling, long-read metagenomics, stable isotope probing and single-cell chemical imaging to investigate the impact of two widely prescribed drugs on the gut microbiome. Physiologically relevant concentrations of entacapone, a treatment for Parkinson’s disease, or loxapine succinate, used to treat schizophrenia, were incubated ex vivo with human faecal samples. Both drugs signifcantly impact microbial activity, more so than microbial abundance. Mechanistically, entacapone can complex and deplete available iron resulting in gut microbiome composition and function changes. Microbial growth can be rescued by replenishing levels of microbiota-accessible iron. Further, entacapone-induced iron starvation selected for iron-scavenging gut microbiome members encoding antimicrobial resistance and virulence genes. These fndings reveal the impact of two under-investigated drugs on whole microbiomes and identify metal sequestration as a mechanism of drug-induced microbiome disturbance.

Drugs initially designed to specifically target human cells can often affect microbes as well1 . As a result of poor gastrointestinal absorption and/or biliary secretion, many of these drugs reach the large intestine where they encounter and potentially interact with hundreds to thousands of different microbial species that play important roles in various aspects of human physiology1–3 . Indeed, several cohort studies have reported significant associations between the use of medication and shifts in gut microbial composition and function4–6 . While the cross-sectional nature of these large cohort studies hinders the establishment of causality, in vitro studies have been pivotal for systematically evaluating direct effects of human-targeted drugs on gut microbes. A landmark study assessing the antimicrobial effect of 835 human-targeted drugs against a panel of 40 cultured gut microbes revealed that a substantial proportion (24%) of drugs could inhibit the growth of at least one gut bacterial strain in vitro1 . An additional study testing the effect of a smaller panel of drugs on faecal samples by metaproteomics demonstrated selective anti- and/or promicrobial activity for the great majority of drugs tested, with a considerable fraction of drugs also shifting microbiome composition7 . Of note, this study demonstrated that bacterial function could shift in response to drugs without a change in taxon abundance, thus highlighting the need for using metrics other than abundance when investigating the

A full list of affiliations appears at the end of the paper.  e-mail: f.c.pereira@soton.ac.uk; jxcheng@bu.edu; michael.wagner@univie.ac.at impact of drugs. Importantly, the interaction between the microbiome and drugs is bidirectional, with many studies clearly demonstrating that gut microbes can also actively metabolize8–10, and under certain circumstances bioaccumulate11, pharmaceutical drugs. While several studies so far have shed light on the nature and extent of microbe-driven drug transformations8,10, mechanistic details for human-targeted drug impact on the microbiome remain to be elucidated.

One hypothesis is that drugs can change intestinal microenvironments such as pH or osmolarity, and by doing so, directly affect bacterial growth12. Another explanation is that drugs interact with structural analogues of their human targets within bacteria, thus also interfering with cellular processes in microbes13. Drug–microbiome interactions have been shown to modulate the therapeutic effect of drugs, contribute to their side effects, or both14–17. Importantly, in certain cases, drug-induced microbiome changes might also contribute to other diseases. For instance, proton pump inhibitors (PPIs) cause major shifts in the gut microbiome18, leading to decreased resistance to colonization by enteric pathogens19. Among the human-targeted drugs tested in vitro, compounds that target the nervous system, such as antipsychotics and antidepressants, seem to exhibit stronger anti-commensal activity against gut bacteria compared with other tested drug classes1,20,21. This is concerning, given the growing number of studies implicating the microbiome in many neuropsychiatric disorders22 and the widespread and rising use of this class of pharmaceuticals worldwide23. Thus, a better mechanistic understanding of drug–microbiome interactions in the context of nervous system-targeted medications may facilitate innovative ways to improve efficacy and/or minimize side effects of therapies for such disorders.

Here we investigate the effects of two nervous system-targeted drugs on whole gut microbiomes using a suite of complementary functional microbiome approaches. These aimed at investigating the effects of the drugs in the context of whole microbial communities, which more closely resembles their effects in situ, and to therefore examine most key members of the gut microbiome. We studied two commonly used drugs: (1) entacapone, a catechol-O-methyltransferase (COMT) inhibitor that acts by preventing the degradation of levodopa, the main drug used in the treatment of Parkinson’s disease24; and (2) loxapine succinate, a tricyclic antipsychotic medication primarily used in the treatment of schizophrenia25. These drugs, whose yearly total prescription exceeds 30 million tablets in the United States alone26, belong to different therapeutic classes and were shown to be selective in their anti-commensal activity against a panel of 40 cultured gut strains, with entacapone predominantly targeting Gram-positive organisms of the phylum Firmicutes and loxapine succinate targeting only taxa within the Gram-negative order Bacteroidales1 . We demonstrate that the impact of either drug on microbiome composition and/or activity extends beyond the taxa initially detected in vitro in pure culture, with entacapone causing strong shifts in microbiome composition. This prompted us to look for the cause of these shifts. We identified microbial iron deprivation, driven by the ability of entacapone to complex iron, as the main mechanism behind entacapone’s strong modulatory effect.

# Results

# Nervous system-targeted drugs affect the microbiome

To evaluate the impact of entacapone (ENT) and loxapine succinate (LOX) on whole gut microbiome communities, we incubated freshly collected faecal samples from six healthy adult individuals with two drug concentrations, a low and a high (Hi) concentration (Fig. 1a and Methods). Supplementation of ENT-Hi significantly reduced the numbers of microbial cells over time when compared with all other tested conditions (Fig. 1b and Supplementary Table 1). Major shifts in the microbial community composition, as determined by 16S ribosomal RNA gene amplicon sequencing analyses, were detected in response to ENT-Hi, LOX-Hi and LOX-Low treatments (Fig. 1c), and in the case of ENT-Hi, these were also accompanied by shifts in alpha diversity (Extended Data Fig. 1a,b, and Supplementary Tables 2 and 3).

By integrating total microbial counts with 16S rRNA gene amplicon sequencing data27, we determined absolute abundances for all detected taxa (Fig. 1d). Importantly, absolute abundance data confirmed that the employed incubation conditions enabled an increase in abundance for nearly all the taxa initially present in faecal samples (Fig. 1e: No drug versus inoculum; Supplementary Table 4) and thus allowed tracking of drug-induced activity and abundance changes of microbiome members. Absolute abundances of genera such as Bacteroides or Clostridium sensu stricto 1 decreased in both ENT-Hi and LOX-Hi samples compared with the dimethylsulfoxide (DMSO) control (Fig. 1d). However, many of the detected effects were drug specific, with ENT-Hi decreasing and LOX-Hi increasing total abundances of the genera Anaerostipes, Fusicatenibacter, Ruminococcus torques group, Eubacterium hallii group, Erysipelotrichaceae group UG-003 and Roseburia. Abundances of several genera were significantly altered in response to ENT-Hi only: Escherichia-Shigella and Ruminococcus increased in abundance, and genera such as Alistipes, Streptococcus or Blautia decreased (Fig. 1d,e and Supplementary Table 5). A similar impact of ENT-Hi on microbial biomass accumulation and on the overall community composition could also be observed when we used a different, nutrient-rich medium (BHI) for the incubations with the same six donors (Extended Data Fig. 1c–g) as well as in additional incubations set up using samples from three additional individual donors (Extended Data Fig. 2 and Supplementary Table 6).

Differential abundance analysis indicated that the abundance of 29.4% of all 16S rRNA gene amplicon sequencing variants (ASVs) were significantly impacted by ENT-Hi after 24 h of incubation, 11.8% of ASVs were impacted by LOX-Hi, and only 3.6% and 6.0% of ASVs were impacted by ENT-Low and LOX-Low, respectively (Methods and Supplementary Table 5). Interestingly, LOX-Low resulted in growth inhibition patterns that differ from the ones observed when the same drug was supplemented to gut members grown in pure culture1 , where it only specifically inhibited growth of Bacteroidales strains. Our results show that other Gram-negative and several Gram-positive species are affected by LOX-Low in the context of whole microbiome communities. These include Erysipelotrichaceae spp., Oscillospiraceae spp. and Lachnospiraceae spp., suggesting a cross-sensitization to loxapine in the context of the community. For ENT-Low, only very few organisms were significantly impacted, most of which were Firmicutes, which agrees with previous reports1 .

Using long-read metagenomic sequencing of the starting faecal sample material, we retrieved a total of 1,049 metagenome-assembled genomes (MAGs) (Supplementary Tables 7 and 8). By linking ASVs to MAGs that contained 16S rRNA genes, we could follow drug-driven community shifts at a higher taxonomic resolution (Fig. 1e,f). This revealed that ASVs classified as Escherichia and Ruminococcus taxa thriving in ENT-Hi give exact hits to the 16S rRNA genes in genomes of E. coli and R. bromii. These analyses also indicated that LOX-Hi conditions selectively promoted the growth of taxa such as Mediterraneibacter faecis, Faecalibacillus faecis and Blautia\_A. Species such as Clostridium sp900539375 (Clostridium sensu stricto 1 based on SILVA taxonomy) and several Bacteroides species (B. uniformis, B. stercoris, Phocaeicola dorei (formerly B. dorei) and P. vulgatus (formely B. vulgatus)) were totally or partially inhibited by the presence of high concentrations of either drug, but the effect of ENT-Hi is much more pronounced than that of LOX-Hi (Fig. 1e,f). On the other hand, Prevotella sp900546535 and several Gram-positive organisms such as Streptococcus lutetiensis, Collinsella sp003487125, Bifidobacterium longum, Mediterraneibacter faecis or Faecalibacillus faecis showed growth inhibition by ENT-Hi only (Fig. 1e,f). All together, these results reveal a strong but distinct effect of entacapone and loxapine at physiological concentrations on microbiota composition and abundance in the short term, with entacapone having a much more pronounced effect than loxapine.

a   
![](images/274d3a94294a6c330d56119e34eea1ab693c56b4c88949fe313a94193112005d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Faecal samples (×6)"] --> B["Nutrient rich conditions 50% D₂O ±Drugs"]
    B --> C["H₂O control no DMSO, no D₂O"]
    C --> D["No drug 2% DMSO"]
    D --> E["ENT-Low 20 μM ENT in DMSO"]
    E --> F["ENT-Hi 1,965 μM ENT in DMSO"]
    F --> G["LOX-Low 20 μM LOX in DMSO"]
    G --> H["LOX-Hi 100 μM LOX in DMSO"]
    H --> I["6, 24 h"]
    I --> J["Microbial loads"]
    I --> K["Amplicon sequencing"]
    I --> L["Long-read sequencing"]
    I --> M["Activity profiling"]
```
</details>

b   
![](images/5661938e1cd21799b92b68dad99d215ce436f9948363e4374e26771b15343df8.jpg)

<details>
<summary>line</summary>

| Time (h) | H₂O control | No drug | ENT-Low | ENT-Hi | LOX-Low | LOX-Hi |
| -------- | ----------- | ------- | ------- | ------ | ------- | ------ |
| 0        | 7.8         | 7.8     | 7.8     | 7.8    | 7.8     | 7.8    |
| 5        | 8.1         | 8.2     | 8.1     | 7.6    | 8.1     | 8.2    |
| 25       | 8.5         | 8.6     | 8.5     | 8.2    | 8.5     | 8.5    |
</details>

c   
![](images/4123b4e948af6c84ad187383f855b7eeea2d2cfbd5b011aabd9cee469effd063.jpg)

<details>
<summary>bar_stacked</summary>

| Time Point | Treatment     | Relative Abundance |
| ---------- | ------------- | ------------------ |
| t0         | Inoculum      | ~0.75              |
| t0         | H₂O control   | ~0.35              |
| t0         | No drug       | ~0.30              |
| t0         | ENT-Low       | ~0.25              |
| t0         | ENT-Hi        | ~0.20              |
| t0         | LOX-Low       | ~0.15              |
| t0         | LOX-Hi        | ~0.10              |
| 6 h        | Inoculum      | ~0.70              |
| 6 h        | H₂O control   | ~0.30              |
| 6 h        | No drug       | ~0.25              |
| 6 h        | ENT-Low       | ~0.20              |
| 6 h        | ENT-Hi        | ~0.15              |
| 6 h        | LOX-Low       | ~0.10              |
| 6 h        | LOX-Hi        | ~0.05              |
| 24 h       | Inoculum      | ~0.75              |
| 24 h       | H₂O control   | ~0.35              |
| 24 h       | No drug       | ~0.30              |
| 24 h       | ENT-Low       | ~0.25              |
| 24 h       | ENT-Hi        | ~0.20              |
| 24 h       | LOX-Low       | ~0.15              |
| 24 h       | LOX-Hi        | ~0.10              |
</details>

d   
![](images/f99c1fd7b1ead89eeed7690ee3bcc26f4caed19c2773efbd30ae947ac28a57ef.jpg)

<details>
<summary>bar_stacked</summary>

| Condition       | Absolute abundance (×10⁸ cells per ml) |
| --------------- | --------------------------------------- |
| Inoculum        | 0.5                                     |
| H₂O control     | 0.7                                     |
| No drug         | 0.8                                     |
| ENT-Low         | 0.9                                     |
| ENT-Hi          | 0.4                                     |
| LOX-Low         | 0.9                                     |
| LOX-Hi          | 1.0                                     |
| H₂O control     | 1.5                                     |
| No drug         | 1.8                                     |
| ENT-Low         | 1.6                                     |
| ENT-Hi          | 1.7                                     |
| LOX-Low         | 1.8                                     |
| LOX-Hi          | 1.9                                     |
| t₀              | 0.1                                     |
| 6 h             | 0.3                                     |
| 24 h            | 0.5                                     |
</details>

Genus   
![](images/067adb47da250580ca2d773a85c721aeb041bccb8c7f863342d70c18be1e80af.jpg)

<details>
<summary>geo</summary>

| Genus | Color |
|---|---|
| [Eubacterium] hallii group | Orange |
| [Ruminococcus] torques group | Red |
| Agathobacter | Light Blue |
| Alistipes | Green |
| Akkermansia | Dark Green |
| Anaerostipes | Dark Green |
| Bacteroides | Dark Green |
| Blautia | Dark Green |
| Bifidobacterium | Dark Green |
| Collinsella | Dark Green |
| Clostridium sensu stricto 1 | Dark Green |
| Eggerthella | Dark Green |
| Erysipelatoclostridium | Dark Green |
| Erysipelotrichaceae UCG-003 | Dark Green |
| Escherichia-Shigella | Yellow |
| Faecalibacterium | Light Blue |
| Fusicatenibacter | Light Blue |
| Gastranaerophilales unclass | Blue |
| Holdemanella | Dark Purple |
| Lachnospiraceae unclass | Dark Purple |
| Other | Teal |
| Prevotella 9 | Purple |
| Roseburia | Brown |
| Ruminococcus | Light Green |
| Streptococcus | Dark Purple |
| Subdoligranulum | Dark Purple |
| Uncultured unclass | Grey |
</details>

log (Cells per ml + 1) 4 4.5 5 5.5 6 6.5 7 7.5

![](images/6b5d2429074c98e42668c47b2cd9bd19c72a021dec907dcf7df6914cde39ac57.jpg)  
Fig. 1 | Drug supplementation of faecal samples impacts biomass accumulation and microbiota composition. a, Schematic representation of faecal sample incubations with the drugs entacapone (ENT) and loxapine (LOX). Samples from 6 different donors were mixed and supplemented with 2 different concentrations of each drug (Low and Hi). The H O control consisted of medium (in H O) without ${ \sf D } _ { 2 } { \sf O }$ or DMSO. After 6 or 24 h of incubation, samples were collected for further analyses (Methods). All incubations were performed in triplicates. b, Total microbial cell loads in faecal sample incubations described in a at the start of the incubation (time = 0 h) and after 6 and 24 h, in sM9 medium. Total cell loads were assessed by flow cytometry and are presented in Supplementary Table 1. \*\*P = 0.006, \*\*\*P = 0.00015, unpaired two-sided t-test with ‘No drug’ used as the reference. Data represent the mean ± s.e.m. of 3 incubation vials per condition. c,d, Relative (c) and absolute (d) genus abundance profiles of faecal microbial communities incubated   
for 6 or 24 h as described in b and assessed by 16S rRNA gene amplicon sequencing. Relative and absolute abundance data are presented in Supplementary Tables 3 and 4, respectively. The community composition at 0 h (inoculum) is also shown. All genera present at a relative abundance below 0.025 or absolute abundance below 6 × 106 cells per ml were assigned to the category ‘Other’. Unclass, unclassified. Each bar represents the mean of triplicates. e, Heat map showing the absolute abundance, expressed in log (cells per ml + 1), of the 25 most abundant ASVs detected across all samples. Each column displays data from one replicate. f, MAGs with 16S rRNA gene sequences matching ASVs shown in e. MAGs were retrieved by metagenomic sequencing of the initial faecal samples using Oxford Nanopore sequencing (Methods and Supplementary Table 8). NA indicates no match of the ASV sequence to each MAG 16S rRNA gene sequence.

![](images/c336db3b47245a4d51d8c299a4c9c2af1b359bd42ea57b4ecc5053e614263a0f.jpg)

<details>
<summary>text_image</summary>

H2O control
No drug
ENT-Low
LOX-Low
LOX-Hi
%CD
SRS
SRS C-H
10 µm
</details>

b   
![](images/628edeffd16117643cf52ebde393cbb26e29cc5b9ae4b9fa176389952a5c7ea5.jpg)

<details>
<summary>violin</summary>

| Cell n | 6 h - H₂O control | 6 h - No drug | 6 h - ENT-Low | 6 h - LOX-Low | 6 h - LOX-Hi | 24 h - H₂O control | 24 h - No drug | 24 h - ENT-Low | 24 h - LOX-Low | 24 h - LOX-Hi |
|--------|-------------------|---------------|---------------|---------------|--------------|--------------------|-----------------|----------------|----------------|---------------|
| 802    | ~1                | ~1            | ~1            | ~1            | ~1           | ~1                 | ~1              | ~1             | ~1             | ~1            |
| 629    | ~5                | ~10           | ~10           | ~10           | ~10          | ~5                 | ~10             | ~10            | ~10            | ~10           |
| 1,090  | ~5                | ~10           | ~10           | ~10           | ~10          | ~5                 | ~10             | ~10            | ~10            | ~10           |
| 634    | ~5                | ~10           | ~10           | ~10           | ~10          | ~5                 | ~10             | ~10            | ~10            | ~10           |
| 731    | ~5                | ~10           | ~10           | ~10           | ~10          | ~5                 | ~10             | ~10            | ~10            | ~10           |
| 744    | ~5                | ~5            | ~5            | ~5            | ~5           | ~5                 | ~5              | ~5             | ~5             | ~5            |
| 990    | ~5                | ~5            | ~5            | ~5            | ~5           | ~5                 | ~5              | ~5             | ~5             | ~5            |
| 510    | ~5                | ~5            | ~5            | ~5            | ~5           | ~5                 | ~5              | ~5             | ~5             | ~5            |
| 647    | ~5                | ~5            | ~5            | ~5            | ~5           | ~5                 | ~5              | ~5             | ~5             | ~5            |
| 900    | ~5                | ~5            | ~5            | ~5            | ~5           | ~5                 | ~5              | ~5             | ~5             | ~5            |
</details>

![](images/07653b226e30d1da2db2f31f2ee6e9ac946121eab71f93d1d8718cf9f99d8d12.jpg)

<details>
<summary>text_image</summary>

c
H2O control	No drug	ENT-Low	LOX-Low	LOX-Hi
Escherichia coli	Trans	FISH	%CDSRS
Streptococcus spp.
Clostridium sp900539375	Trans	FISH	%CDSRS
%CDSRS
</details>

![](images/28d7b59dc1d21abf5c9f87f26410222750791de2c23d7f4e74829e62b9367f28.jpg)

<details>
<summary>text_image</summary>

H2O control
No drug
ENT-Low
LOX-Low
LOX-Hi
Bacteroides uniformis
Trans
FISH
%CD5RS
Ruminococcus bromii
Trans
FISH
%CD5RS
Phocaecola dorei
Trans
FISH
%CD5RS
10 µm
</details>

d   
![](images/1772cfb706a5fc48cfa8d00804380a8af1a6c322511df606f74939eb2cb5c8fe.jpg)

<details>
<summary>bubble</summary>

| Species | ENT-Low | LOX-Low | LOX-Hi |
| --- | --- | --- | --- |
| Escherichia coli | 0.00005 | 0.00005 | 1.0 |
| Streptococcus spp. | 0.005 | 0.05 | 0.5 |
| Clostridium sp900539375 | -1.0 | 1.0 | 1.0 |
| Bacteroides uniformis | -1.0 | 0.0 | 0.5 |
| Ruminococcus bromii | -1.0 | 1.0 | 1.0 |
| Phocaeicola dorei | -1.0 | 1.0 | 1.0 |
</details>

e   
![](images/7a6cec87f5e9dbbc33f99dbed3160fe83ab7815b364c0a1a854a89c06800d127.jpg)

<details>
<summary>bubble</summary>

| Species | ENT-Low | LOX-Low | LOX-Hi |
| --- | --- | --- | --- |
| Escherichia coli | 0 | 0 | 0 |
| Streptococcus spp. | 1 | 0 | 0 |
| Clostridium sp900539375 | 0 | 0 | 1 |
| Bacteroides uniformis | 0 | 0 | 0 |
| Ruminococcus bromii | 0 | 0 | 0 |
| Phocaeicola dorei | 0 | 0 | 1 |
</details>

Fig. 2 | Metabolic activity of drug-incubated single-microbiome cells measured by deuterium incorporation via SRS. a, Representative SRS images of a mixture of 6 faecal samples incubated with the indicated drugs for 6 h, as depicted in Fig. 1. Top: $\% { \bf C D } _ { \mathrm { S R S } }$ distribution images. Bottom: C-H for biomass visualization (log scaled). $\% { \bf C D } _ { \mathrm { S R S } }$ scaling: minimum 0, maximum 20%. b, Singlecel $| \% { \bf C D } _ { \mathrm { S R S } }$ values in each analysed sample (see also Supplementary Table 9). Violin plots illustrate summary statistics (median, first and third quartiles, with whiskers representing the minimum and maximum values within 1.5× the interquartile ranges from the first and third quartiles). Number of measured cells per sample are indicated on the x axis (cell n). $^ { * * } P { = } 0 . 0 0 4 3 , ^ { * * * } P { = } 5 . 2 \times 1 0 ^ { - 1 2 }$ , \*\*\*\* $P { < } 2 \times 1 0 ^ { - 1 6 }$ , two-sided Wilcoxon test using ‘No drug’ as the reference. c, Drug-incubated faecal samples (at 6 h) were hybridized with fluorescently labelled oligonucleotide probes targeting E. coli (Ecol\_268), Streptococcus and Lactococcus species $\left( { \mathsf { S t r c } } \ 4 9 3 \right)$ , Clostridium sp900539375 (Clostridium sensu stricto 1, Clo\_648), Ruminococcus bromii (Brom\_2036), B. uniformis (Buni\_1001)   
and P. dorei (Bado\_374) (Supplementary Table 10). For each targeted group, top rows show representative images obtained by overlay of transmitted light (Trans) and fluorescence intensity (FISH). Bottom rows show the corresponding SRS images (displaying $\% { \bf C D _ { \mathrm { S R S } } } )$ for the FISH-targeted microbes $( \% 0 0 _ { 5 \mathrm { R S } }$ values of other microbes are not displayed for the sake of visibility). Scale bar, $1 0 \mu \mathrm { m } .$ . For a and c, we reproducibly detected analogous differences when measuring at least one additional batch of samples. d, Bubble plot denoting the fold change (FC, represented as log2FC) in activity levels (calculated as $\% { \bf C D } _ { \mathrm { S R S } } )$ for the taxa targeted by FISH and incubated with drugs relative to ‘No drug’ incubations at 6 h (Supplementary Table 11). e, Bubble plot denoting the FC in absolute abundances for the taxa targeted by FISH and incubated with drugs relative to ‘No drug’ incubations, as determined by DeSeq2 at 6 h (Supplementary Table 5). In d and e, P values were obtained using the Wald test and corrected for multiple testing using the Benjamini–Hochberg method.

# Nervous system-targeted drugs alter microbial metabolism

Next, we evaluated the effect of these drugs on microbial activity at the single-cell level. To determine drug-induced changes in microbial activity, we added heavy water (D O) as a universal metabolic tracer28,29 to our incubations (Fig. 1a and Methods). Detection and quantification of C-D bonds from deuterium (D) incorporation from ${ \bf D } _ { 2 } { \bf O }$ by single microbial cells can be achieved using stimulated Raman scattering spectroscopy (SRS)30,31. We have previously successfully combined SRS with fluorescence in situ hybridization (FISH) to determine gut microbiome response to sugars with high throughput32. Using an optimized SRS–FISH platform that provides even higher throughput and sensitivity than the previous setup (Supplementary Text, and Extended Data Figs. 3 and 4), we measured \~8,000 individual microbiota cells after 6 and 24 h of incubation in the presence of the drugs and in controls (Fig. 2a,b). An unexpected, non-vibrational signal was detected in samples incubated with ENT-Hi, so these samples were excluded from activity measurements and the origin of this signal was further explored as detailed in the next section. As expected, in the absence of the drugs, nearly all of the analysed cells were detected as active in the incubation medium, with 90% and 98% of cells displaying $\% { \bf C D } _ { \mathrm { S R S } }$ values above threshold after 6 h and 24 h of incubation, respectively (Fig. 2b and Supplementary Table 9). Addition of either ENT-Low, LOX-Low or LOX-Hi resulted in a significantly reduced fraction of total active cells, as well as in a significant reduction of single-cell metabolic activity. This reduction was more pronounced for LOX-Hi, followed by LOX-Low and ENT-Low (Fig. 2b). Thus, these drugs clearly impacted microbial activity within communities, even after short incubation times and under conditions where no impacts on their overall abundances were detected (Fig. 1b).

To examine the activity of specific populations of the microbiome within the complex communities, we targeted six distinct abundant taxa of interest using SRS–FISH, which enabled us to determine the activity of individual cells from these taxa (Supplementary Table 10). Targeted taxa included organisms whose abundances were both negatively and positively impacted by drugs. Both LOX-Low and LOX-Hi incubations significantly reduced the activity of all targeted gut microbiota members except for E. coli (Fig. 2d). Interestingly, Clostridium sp900539375, B. uniformis, Ruminococcus bromii and P. dorei showed reduced activity in LOX treatments, but only the abundance of P. dorei and Clostridium sp900539375 was negatively impacted (Fig. 2d,e and Supplementary Table 11). LOX-Low and LOX-Hi seem to strongly inhibit P. dorei growth within 6 h (Fig. 1e), probably rendering most cells of this taxon undetectable by FISH, as the low ribosome content of non-active cells hinders FISH detection. We speculate that only a few drug-resistant P. dorei cells remained active enough to be detected by FISH, and these cells were not strongly impacted in activity (Fig. 2c,d). This observation could be explained by either phenotypic heterogeneity33 within the P. dorei isogenic population, or the FISH probe used, which may target multiple P. dorei strains with different physiologies. A comparable decrease in activity was detected for Streptococcus spp., but in this case the decrease was surprisingly accompanied by a slight increase in abundance at 6 h (Fig. 2d,e). However, from 6 to 24 h, we detected a decrease of the population represented by the Clostridium sp900539375, B. uniformis and Streptococcus lutentiensis MAGs in the presence of LOX compared with the control (Fig. 1e,f and Extended Data Fig. 5), which could be an effect of the lower activities detected by SRS in the LOX conditions at 6 h. In summary, SRS–FISH provided unique insights into the impact of ENT and LOX on the activities of specific microbiome members, which are often masked when only considering abundance data from relatively short incubation experiments.

# Entacapone bioaccumulates in microbiota cells

Gut microbes have been shown to bioaccumulate some drugs, leading to depletion of the drug from the surrounding environment11. As ENT-Hi samples showed a strong, unspecific Raman signal during SRS pump-probe detection, we explored the origin of this signal and concluded that it is photothermal (PT), originating from entacapone bioaccumulation within microbial cells (Supplementary Text and Extended Data Fig. 6). By mapping the intensity of this PT signal from ENT-Hi samples and controls (Fig. 3a), we were able to show that the signal from entacapone occurred in a large fraction of microbial cells that had been incubated with the drug and washed before being fixed for analysis, but only in very few cells that had been fixed before incubation with the drug (that is, dead cells) (Fig. 3b,c and Supplementary Table 12). There was no strong correlation between entacapone accumulation and cellular activity when measured in the same cell (Extended Data Fig. 7), although the cellular activity tends to be lower for high entacapone accumulators (Fig. 3d).

To identify the main drug-accumulating taxa, we further looked at the entacapone distribution among populations targeted with the FISH probes described above (Fig. 3e). All of the targeted populations displayed entacapone signals to different intensities. While P. dorei and, to a lesser extent Streptococcus spp. and E. coli, seemed to be strong entacapone accumulators, only a small percentage of R. bromii and part of the B. uniformis population accumulated entacapone (Fig. 3e,f). High entacapone signals were also detected in cells not targeted by FISH (Fig. 3e,f). We further confirmed the ability of P. dorei to accumulate entacapone when grown in pure culture (Extended Data Fig. 8 and Supplementary Text). Interestingly, while entacapone accumulation drastically inhibited the growth of P. dorei as a microbiome community member and in pure culture, it did not affect Streptococcus growth in the community to the same extent and even showed growth promotion for E. coli (Fig. 3f,g). Thus, bioaccumulation of the drug correlated with growth inhibition for certain taxa, whereas others were unaffected or even stimulated in growth.

# Entacapone chelates iron and induces iron starvation

Entacapone’s nitrocatechol group can act as a bidentate ligand, chelating and forming stable tris complexes with the transition metal ion ferric iron (Fe(III)), through the catecholate oxygen atoms34. Using an assay widely applied to detect Fe-chelating agents in solution, we confirmed entacapone’s ability to chelate ferric iron (Fe(III)) (Fig. 4a). The stability constant of entacapone’s association with Fe (pFe(III) = 19.3)34 has been demonstrated to be similar to constants described for other known iron chelators such as $2 , 2 ^ { \prime } { \cdot } \mathrm { b i p y r i d y l } \left( \mathrm { p F e } ( \mathrm { I I I } ) = 2 1 . 5 \right) ^ { 3 5 }$ 5. Entacapone was also predicted to complex ferrous iron (Fe(II)) with rather high affinity, but was not predicted to form strong complexes with any other metal cations35. However, we demonstrate that entacapone does not bind ferrous iron (Extended Data Fig. 9a).

Iron is a limiting nutrient in the gut and essential for the growth of most gut microbes36. Iron concentrations in stool are estimated to be \~60 μM (ref. 37), and the sM9 medium used here for faecal sample incubations contained similar concentrations of iron (31 μM). As the estimated concentration of entacapone in the large intestine is approximately two orders of magnitude higher (1,965 μM), we postulated that the inhibitory effect of ENT-Hi on microbial growth could be directly related to its ability to deprive gut microbes of iron via chelation, similarly to what has been documented for other Fe(II) and Fe(III) chelators38,39. To test this hypothesis, we grew Bacteroides thetaiotaomicron, a gut commensal severely impacted by Ent-Hi (log -fold change: −4.16, adjusted $P { = } 0 . 0 1 6 ,$ Supplementary Table 5: ASV\_g1t\_iba) in the presence of ENT-Hi or Fe-loaded ENT-Hi (Fig. 4b and Methods). Of note, in pre-complexation reactions, Fe(II) from $\mathsf { F e S O } _ { 4 }$ was exposed to the drug solvent DMSO, which resulted in an instantaneous oxidation to Fe(III) (Extended Data Fig. 9b). Thus, both pre-complexation of ENT-Hi with FeCl3 or FeSO4 resulted in Fe(III)-loaded entacapone. While ENT-Hi inhibited the growth of B. thetaiotaomicron, ENT-Hi pre-complexed with iron did not, enabling B. thetaiotaomicron to grow normally (Fig. 4b). This is because iron-saturated chelators are no longer able to complex free Fe(II) (or Fe(III)) present in the medium (or intracellularly), thus enabling bacteria to access iron and grow normally39. Originally, we expected added iron to be mostly present in the lower oxidation state under anaerobic conditions. Surprisingly, quantification of Fe(II) in $\mathsf { F e S O } _ { 4 }$ -supplemented medium revealed that the Fe(II) added was quickly oxidized to Fe(III), probably by the presence of phosphates in the medium40, despite the anaerobic atmosphere and the presence of 0.1% (w/v) l-cystein as a reducing agent (Extended Data Fig. 9c). Supplementation of ENT-Hi alone followed by addition of increasing amounts of iron (FeSO4) alleviated the inhibitory effect of ENT-Hi on B. thetaiotaomicron (Fig. 4b). Addition of similar amounts of cupric ions (Cu(II)) did not reverse growth inhibition by ENT-Hi (Fig. 4b), confirming that the observed effect is specific for iron.

a   
![](images/00befd92adca0f51ecd7282402f3688b9cb6818dc1e1d8a5376dfbafd06c8145.jpg)

<details>
<summary>chemical</summary>

Chemical reaction diagram showing polymerization with PT and w/o PT conditions over time
</details>

b   
![](images/f830794b031f9513687615fb8d048f2efa945a74b43ae00c104b2216f1a5eb90.jpg)

<details>
<summary>text_image</summary>

Live - No drug
PT (Entacapone)
Live+ENT-Hi
Dead+ENT-Hi
SRS C-H
</details>

c   
![](images/1fa1f9425ec521b6404ecba358120502fdb20c43c9f524ccbffaafb182eea166.jpg)

<details>
<summary>scatter</summary>

| Group        | PT intensity (arbitrary units) |
| ------------ | ------------------------------ |
| No drug      | ~0.0                           |
| ENT-Hi       | ~0.2                           |
| Dead +ENT-Hi | ~0.1                           |
</details>

d   
![](images/3e22afb608572a9483cdbb3ffe705df7450ecb746939d252ff8a6686b405bd48.jpg)

<details>
<summary>scatter</summary>

| PT intensity (arbitrary units) | %CD5RS |
| ------------------------------ | ------ |
| 0.0                            | 14.0   |
| 0.1                            | 12.0   |
| 0.2                            | 8.0    |
| 0.3                            | 6.0    |
| 0.4                            | 4.0    |
| 0.5                            | 2.0    |
| 0.6                            | 0.0    |
| 0.7                            | -2.0   |
| 0.8                            | -4.0   |
</details>

e   
![](images/67b18543c45abc092592d9b7205dd6eac022435c14bcfaa1ce5c7da28af9e5b7.jpg)

<details>
<summary>text_image</summary>

Ecol
Strc
Buni
Rumi
Pdor
Trans
FISH
PT (Entacapone)
SRS C-H
</details>

f   
![](images/b0520070ca271212f3229bf6eac34cef398bc2dc51ea76ea33f89d33f7a21418.jpg)

<details>
<summary>bar</summary>

| Drug Group | All     | Ecol    | All     | Strc    | Buni    | Rumi    | Pdor    |
| ---------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| ENT-Hi     | 1.4 × 10⁻⁵ | 1.1 × 10⁻⁷ | 0.021   | 0.00027 | 2.1 × 10⁻⁴ | -       | -       |
</details>

g   
![](images/bf49ac258518a4d7313c253e1e0c2acf8bfb39b59044e347c19b681671c385e9.jpg)

<details>
<summary>line</summary>

| Time (h) | Ecol - No drug | Ecol - ENT-Low | Ecol - ENT-Hi | Strc - No drug | Strc - ENT-Low | Strc - ENT-Hi | Buni - No drug | Buni - ENT-Low | Buni - ENT-Hi | Rumi - No drug | Rumi - ENT-Low | Rumi - ENT-Hi | Pdor - No drug | Pdor - ENT-Low | Pdor - ENT-Hi |
|----------|----------------|----------------|---------------|----------------|----------------|---------------|----------------|----------------|---------------|----------------|----------------|---------------|----------------|----------------|---------------|
| 0        | 5.5            | 5.5            | 5.5           | 5.5            | 5.5            | 5.5           | 5.5            | 5.5            | 5.5           | 5.5            | 5.5            | 5.5           | 5.5            | 5.5            | 5.5           |
| 5        | 6.3            | 6.1            | 6.7           | 6.3            | 6.9            | 6.4           | 6.3            | 6.8            | 6.4           | 6.3            | 6.8            | 6.4           | 6.3            | 6.8            | 6.4           |
| 10       | 6.4            | 6.2            | 7.0           | 6.4            | 7.1            | 6.7           | 6.4            | 7.1            | 6.7           | 6.4            | 7.1            | 6.7           | 6.4            | 7.1            | 6.7           |
| 15       | 6.4            | 6.3            | 7.1           | 6.5            | 7.2            | 6.8           | 6.5            | 7.2            | 6.8           | 6.5            | 7.2            | 6.8           | 6.5            | 7.2            | 6.8           |
| 20       | 6.4            | 6.4            | 7.2           | 6.6            | 7.3            | 6.9           | 6.6            | 7.3            | 6.9           | 6.6            | 7.3            | 6.9           | 6.6            | 7.3            | 6.9           |
| 25       | 6.4            | 6.5            | 7.5           | 6.7            | 7.4            | 7.0           | 6.7            | 7.4            | 7.0           | 6.7            | 7.4            | 7.0           | 6.7            | 7.4            | 7.0           |
</details>

Fig. 3 | Photothermal imaging of entacapone bioaccumulation by microbiota cells. a, Schematic illustration of the time-dependent signal obtained from a solution of 10 mM entacapone in DMSO, with photothermal (w/ PT) and without photothermal (w/o PT) detection. b, Photothermal signal intensity distribution from entacapone (PT), and SRS C-H signal of live and dead (PFA fixed) microbiota cells incubated in the presence (+) or absence (−) of ENT-Hi for 6 h. Scale bar, 10 μm. c, Single-cell photothermal signal intensity distribution in samples shown in b. P values were determined using unpaired two-sided Wilcoxon test comparing groups ENT-Hi and No drug, or ENT-Hi and Dead+ENT-Hi (Supplementary Table 12). d, Correlation between activity $( \% { \bf C D _ { 5 R S } } )$ and PT signal intensity for microbiota cells exposed to ENT-HI for 6 h. Pearson correlation coefficient (R) and two-sided P value are indicated. Incubations were established using a new mixture of samples from two donors in sM9. e, Representative images of the original mixture of 6 faecal samples incubated with ENT-Hi for 6 h followed by hybridization with FISH   
probes targeting E. coli (Ecol), Streptococcus and Lactococcus (Strc), Ruminococcus bromii (Rumi), B. uniformis (Buni) and P. dorei (Pdor) (Supplementary Table 10). Top: FISH-probe signals from hybridized cells. Middle: PT signal maps from entacapone (cells targeted by FISH are shown with white contour lines). Bottom: entacapone PT signals overlayed with SRS C-H signals. Scale bar, 8 μm. In b and e, PT channel contrast is min 0 and max 1.8, and C-H signals are represented on a log scale. f, Single-cell photothermal signal distribution in samples shown in c. P values were determined using unpaired two-sided Wilcoxon test comparing ENT-Hi and No drug groups of targeted taxa only. g, Absolute abundance of taxa targeted by FISH in No drug, Ent-Low and ENT-Hi incubations (Supplementary Table 4). Data represent the mean ± s.d. of 3 incubation vials. In c and f, boxes represent the median, first and third quartile. Whiskers extend to the highest and lowest values that are within 1.5× the interquartile range.

In summary, these results demonstrate that supplementation of Fe(III) alone or of an ENT-Hi:Fe complex rescues the inhibitory effect of ENT-Hi on B. thetaiotaomicron, strongly indicating that entacapone drives iron limitation.

To determine whether the results above also apply to a complex microbiota, we incubated faecal samples under equivalent conditions as described in Fig. 1a. In agreement with the results obtained for B. thetaiotaomicron alone, supplementation of the whole microbiome with iron-loaded ENT-Hi or with ENT-Hi followed by iron resulted in a complete or near complete reversal of the inhibitory effect on microbial biomass accumulation (Fig. 4c,d and Supplementary Table 13). Supplementation of Fe(III) reverses the impact of ENT-Hi on the community alpha diversity metrics as well as on the growth of nearly all of the top 25 most affected taxa (exceptions are Firmicutes such as Anaerostipes and Blautia) (Fig. 4e,f, and Supplementary Tables 14 and 15). Iron supplementation does not only enable taxa negatively impacted by entacapone to grow, but it also seems to restrict the accelerated expansion of organisms such as E. coli, prompted by ENT-Hi (Fig. 1e and Fig. 5d). Importantly, we confirmed that this effect is not due to lower cellular uptake, as ENT-Hi:Fe(III) bioaccumulates in microbiota cells to the same level or higher than ENT-Hi alone (Extended Data Fig. 8e,f), thus suggesting that the ENT-Hi:Fe(III) complex behaves similarly to entacapone in terms of its ability to penetrate and accumulate in cells. Microbiota cells and the entacapone accumulator species P. dorei display significantly higher levels of iron when exposed to entacapone compared with non-exposed cells, strongly suggesting that ENT-Hi:Fe(III) complexes are stable and reach the cellular space (Fig. 5). Many of these cells may nevertheless starve due to an inability to release iron from the entacapone complex. All together, these results suggest that complexation of the limiting nutrient iron by entacapone is the primary mechanism causing the strong inhibitory effect of entacapone on the microbiome.

a   
![](images/05d710162068e214193d620d400bf77ddd405a4d296584cf23e4aa26e7c53e1e.jpg)

<details>
<summary>text_image</summary>

FeCl₃ (mM): - 0.1 0.5 1.0
Control (DMSO)
ENT (0.1 mM in DMSO)
</details>

b   
![](images/5b5193487f9d43d8cd9780424995e4efcf5c0484c9ee61e0780c02c950854695.jpg)

<details>
<summary>line</summary>

| Time (h) | Series 1 | Series 2 | Series 3 | Series 4 | Series 5 |
| -------- | -------- | -------- | -------- | -------- | -------- |
| 0        | 7.0      | 7.0      | 7.0      | 7.0      | 7.0      |
| 20       | 9.5      | 9.0      | 7.5      | 7.0      | 7.0      |
| 40       | 9.0      | 9.0      | 7.5      | 7.0      | 7.0      |
</details>

![](images/746c15dd426d588ad847b54c087cd72908b34b98787b59dff7de8fbd94338ada.jpg)

<details>
<summary>boxplot</summary>

| Group | Value |
|-------|-------|
| 1     | 9.5   |
| 2     | 9.3   |
| 3     | 9.1   |
| 4     | 8.9   |
| 5     | 8.7   |
| 6     | 8.5   |
| 7     | 8.3   |
| 8     | 8.1   |
| 9     | 7.9   |
| 10    | 7.7   |
| 11    | 7.5   |
| 12    | 7.3   |
| 13    | 7.1   |
| 14    | 6.9   |
| 15    | 6.7   |
| 16    | 6.5   |
| 17    | 6.3   |
| 18    | 6.1   |
| 19    | 5.9   |
| 20    | 5.7   |
| 21    | 5.5   |
| 22    | 5.3   |
| 23    | 5.1   |
| 24    | 4.9   |
</details>

![](images/79a3fc1c6a4b12c614c4bb1f53bfa6aa750a352d89c9ad7d1354867398dd03d6.jpg)

<details>
<summary>scatter</summary>

| Category | Value |
|---|---|
| Group 1 | ***(*) |
| Group 2 | **** |
| Group 3 | * |
| Group 4 | * |
| Group 5 | *** |
| Group 6 | **** |
| Group 7 | * |
| Group 8 | * |
| Group 9 | * |
| Group 10 | * |
| Group 11 | * |
| Group 12 | * |
| Group 13 | * |
| Group 14 | * |
| Group 15 | * |
| Group 16 | * |
| Group 17 | * |
| Group 18 | * |
| Group 19 | * |
| Group 20 | * |
| Group 21 | * |
| Group 22 | * |
| Group 23 | * |
| Group 24 | * |
| Group 25 | * |
| Group 26 | * |
| Group 27 | * |
| Group 28 | * |
| Group 29 | * |
| Group 30 | * |
| Group 31 | * |
| Group 32 | * |
| Group 33 | * |
| Group 34 | * |
| Group 35 | * |
| Group 36 | * |
| Group 37 | * |
| Group 38 | * |
| Group 39 | * |
| Group 40 | * |
| Group 41 | * |
| Group 42 | * |
| Group 43 | * |
| Group 44 | * |
| Group 45 | * |
| Group 46 | * |
| Group 47 | * |
| Group 48 | * |
| Group 49 | * |
| Group 50 | * |
| Group 51 | * |
| Group 52 | * |
| Group 53 | * |
| Group 54 | * |
| Group 55 | * |
| Group 56 | * |
| Group 57 | * |
| Group 58 | * |
| Group 59 | * |
| Group 60 | * |
| Group 61 | * |
| Group 62 | * |
| Group 63 | * |
| Group 64 | * |
| Group 65 | * |
| Group 66 | * |
| Group 67 | * |
| Group 68 | * |
| Group 69 | * |
| Group 70 | * |
| Group 71 | * |
| Group 72 | * |
| Group 73 | * |
| Group 74 | * |
| Group 75 | * |
| Group 76 | * |
| Group 77 | * |
| Group 78 | * |
| Group 79 | * |
| Group 80 | * |
| Group 81 | * |
| Group 82 | * |
| Group 83 | * |
| Group 84 | * |
| Group 85 | * |
| Group 86 | * |
| Group 87 | * |
| Group 88 | * |
| Group 89 | * |
| Group 90 | * |
| Group 91 | * |
| Group 92 | * |
| Group 93 | * |
| Group 94 | * |
| Group 95 | * |
| Group 96 | * |
| Group 97 | * |
| Group 98 | * |
| Group 99 | * |
| Group 100 | ***(*)
</details>

Growth condition   
No drug   
ENT-Hi   
ENT-Hi : Fe(III) (FeSO )   
ENT-Hi : Fe (III) (FeCl )   
ENT-Hi + 0.1 mM Fe(III)   
ENT-Hi + 0.5 mM Fe(III)   
ENT-Hi + 1.0 mM Fe(III)   
ENT-Hi + 0.5 mM Cu(II)   
• ENT-Hi + 1.0 mM Cu(II)

c   
![](images/b660bbe00fb4576c86205588784f9d76c1675d095347b274c31506dd75f8bb9d.jpg)

<details>
<summary>line</summary>

| Time (h) | No drug | ENT-Hi + 1.0 mM Fe | ENT-Hi : Fe | No drug + 1.0 mM Fe |
| -------- | ------- | ------------------ | ----------- | ------------------- |
| 0        | 7.5     | 7.5                | 7.5         | 7.5                 |
| 5        | 7.9     | 7.6                | 7.8         | 7.9                 |
| 25       | 8.1     | 7.7                | 8.3         | 8.4                 |
</details>

d   
![](images/1ca2cac1cbb098ebb43ead12f07d7963d5fe844a2eb0d2f1ec55475a1b86a4f9.jpg)

<details>
<summary>bar_stacked</summary>

| Condition | Time Point | Relative Abundance |
|-----------|------------|---------------------|
| Inoculum | 6 h        | ~0.50               |
| Inoculum | 24 h       | ~0.50               |
| No drug   | 6 h        | ~0.30               |
| No drug   | 24 h       | ~0.30               |
| ENT-Hi    | 6 h        | ~0.40               |
| ENT-Hi    | 24 h       | ~0.40               |
| ENT-Hi + 1.0 mM Fe | 6 h     | ~0.35              |
| ENT-Hi + 1.0 mM Fe | 24 h    | ~0.35              |
| ENT-Hi : Fe    | 6 h        | ~0.45               |
| ENT-Hi : Fe    | 24 h       | ~0.45               |
| No drug + 1.0 mM Fe | 6 h     | ~0.35              |
| No drug + 1.0 mM Fe | 24 h    | ~0.35              |
| ENT-Hi     | 6 h        | ~0.45               |
| ENT-Hi     | 24 h       | ~0.45               |
| ENT-Hi + 1.0 mM Fe | 6 h     | ~0.35              |
| ENT-Hi + 1.0 mM Fe | 24 h    | ~0.35              |
| ENT-Hi : Fe   | 6 h        | ~0.45               |
| ENT-Hi : Fe   | 24 h       | ~0.45               |
| No drug + 1.0 mM Fe | 6 h     | ~0.35              |
| No drug + 1.0 mM Fe | 24 h    | ~0.35              |
</details>

![](images/df51fa767e7732c0c741d9ddd8edb61508a9433432afd252e74e9e2f34ecefb9.jpg)

<details>
<summary>bar_stacked</summary>

| Condition | t0 | t0 (6 h) | t0 (24 h) |
| --- | --- | --- | --- |
| Inoculum | 0.3 | 0.3 | 0.3 |
| No drug | 0.25 | 0.25 | 0.25 |
| ENT-Hi | 0.2 | 0.2 | 0.2 |
| ENT-Hi + 1.0 mM Fe | 0.15 | 0.15 | 0.15 |
| ENT-Hi: Fe | 0.1 | 0.1 | 0.1 |
| No drug + 1.0 mM Fe | 0.15 | 0.15 | 0.15 |
| No drug | 0.35 | 0.35 | 0.35 |
| ENT-Hi | 0.25 | 0.25 | 0.25 |
| ENT-Hi + 1.0 mM Fe | 0.2 | 0.2 | 0.2 |
| ENT-Hi: Fe | 0.15 | 0.15 | 0.15 |
| No drug + 1.0 mM Fe | 0.15 | 0.15 | 0.15 |
| Other | 0.35 | 0.35 | 0.35 |
| Agathobacter | 0.35 | 0.35 | 0.35 |
| Alistipes | 0.35 | 0.35 | 0.35 |
| Akkermansia | 0.35 | 0.35 | 0.35 |
| Anaerostipes | 0.35 | 0.35 | 0.35 |
| Bacteroides | 0.35 | 0.35 | 0.35 |
| Blautia | 0.35 | 0.35 | 0.35 |
| Bifidobacterium | 0.35 | 0.35 | 0.35 |
| Butyricicoccus | 0.35 | 0.35 | 0.35 |
| Eggerthella | 0.35 | 0.35 | 0.35 |
| Erysipelatoclostridium | 0.35 | 0.35 | 0.35 |
| Escherichia-Shigella | 0.35 | 0.35 | 0.35 |
| Faecalibacterium | 0.35 | 0.35 | 0.35 |
| Fusicatenibacter | 0.35 | 0.35 | 0.35 |
| Holdemannella | 0.35 | 0.35 | 0.35 |
| Lachnospiraceae uncl | 0.35 | 0.35 | 0.35 |
| Parabacteroides | 0.35 | 0.35 | 0.35 |
| Prevotella 9 | 0.35 | 0.35 | 0.35 |
| Phascolarctobacterium | 0.35 | 0.35 | 0.35 |
| Ruminococcus | 0.35 | 0.35 | 0.35 |
| Subdoligranulum | 0.35 | 0.35 | 0.35 |
| Streptococcus | 0.35 | 0.35 | 0.35 |
| Sutterella | 0.35 | 0.35 | 0.35 |
| uncultured unclass | 0.35 | 0.35 | 0.35 |
| UCG-002 | 0.35 | 0.35 | 0.35 |
| UCG-004 | 0.35 | 0.35 | 0.35 |
</details>

![](images/21e7fdded1f8d50cbacd4dc4d172d2309337365e1d40b4149c476260c8b33764.jpg)

<details>
<summary>boxplot</summary>

| Group | Condition | Alpha diversity measure |
|-------|-----------|--------------------------|
| Observed species | No drug | ~310 |
| Observed species | ENT-Hi | ~335 |
| Observed species | ENT-Hi + 1.0 mM Fe | ~315 |
| Observed species | ENT-Hi : Fe | ~340 |
| Observed species | No drug + 1.0 mM Fe | ~315 |
| Shannon index | No drug | ~4.0 |
| Shannon index | ENT-Hi | ~3.5 |
| Shannon index | ENT-Hi + 1.0 mM Fe | ~3.8 |
| Shannon index | ENT-Hi : Fe | ~3.9 |
| Shannon index | No drug + 1.0 mM Fe | ~3.9 |
| Inv. Simpson | No drug | ~20 |
| Inv. Simpson | ENT-Hi | ~6 |
| Inv. Simpson | ENT-Hi + 1.0 mM Fe | ~18 |
| Inv. Simpson | ENT-Hi : Fe | ~17 |
| Inv. Simpson | No drug + 1.0 mM Fe | ~20 |
</details>

f   
![](images/70048e06ab89aad7a7269522f8d868ab3adb7dfa8af7afe0d8c8c119312bb5d4.jpg)  
Fig. 4 | Iron supplementation rescues the impact of entacapone on the gut microbiome. a, Siderophore detection assay showing the change in colour in the presence of 0.1 mM entacapone. The indicator complex changed back to its original colour (blue) after addition of excess ferric iron. b, Growth of B. thetaiotaomicron in the absence of drug or in the presence of: ENT-Hi; ENT-Hi preloaded with $\tt { \tt { e S O } _ { 4 } }$ (ENT-Hi: Fe(III)), ENT-Hi preloaded with FeCl (ENT-Hi: Fe(III)); or ENT-Hi supplemented with Fe(III) $\mathrm { ( F e S O _ { 4 } ) }$ or Cu(II) (CuCl2). No drug and ENT-Hi conditions: n = 6; all other conditions: n = 3 independent growths per condition. Data represent the mean ± s.e.m. The box plots in the middle and right refer to the same data as displayed on the left plot but split by incubation time. c. Total cell loads in faecal samples (mix from 5 donors) incubated with either ENT-Hi, $\mathsf { F e S O } _ { 4 }$ (No drug + 1.0 mM Fe), both (ENT-Hi + 1.0 mM Fe), or ENT-Hi pre-incubated with FeSO (ENT-Hi:Fe) in sM9 medium. In b and c, Fe(II) is oxidized to Fe(III), and thus Fe(III) is present. Data represent the mean ± s.e.m.   
of 3 incubation vials per condition (Supplementary Table 13). d, Relative (left) and absolute (right) genus abundance profiles of microbial communities incubated as described in c and assessed by 16S rRNA gene amplicon sequencing (Supplementary Tables 14 and 15). All genera present at relative abundances below 0.01 or absolute abundances below $1 . 5 \times 1 0 ^ { 6 }$ cells per ml were assigned to the category ‘Other’. Data are from triplicates per condition. e, Alpha diversity metrics in gut microbial communities at 24 h of incubation. f, Bubble plot denoting the fold change (log FC) in absolute abundance relative to control incubations for the 25 most abundant ASVs. P values (Wald test) were adjusted using the Benjamini–Hochberg method. In b and e, boxes represent the median, first and third quartiles. Whiskers extend to the highest and lowest values that are within 1.5× the interquartile range. In b, c and $\mathbf { e } { \cdot } ^ { * } P { < } 0 . 0 5 , ^ { * * } P { < } 0 . 0 1 , ^ { * * * } P { < } 0 . 0 0 1$ , \*\*\*\*P < 0.0001; unpaired two-sided t-test with ‘No drug’ used as the reference group. Only statistically significant differences are indicated.

a   
![](images/096bcc70fdbe79e1df622b52dc9a16b8051debe0f92715fde1f15abf58c772f3.jpg)

<details>
<summary>text_image</summary>

Max
Signal intensity
12C+
59Fe+
Signal intensity
Mln
Mln
</details>

b   
![](images/f629245525c9e82d33932e6fe2bcbc7bc340e63f4c481dae390ef39ff348769f.jpg)

<details>
<summary>natural_image</summary>

Microscopic view of cellular or particulate structures with fluorescent staining (no visible text or symbols)
</details>

c   
![](images/bc9cc1d36bdc76f3cc2ea84ded35afd7ec3148c6392eb24f9083c2eb0fa1c9db.jpg)

<details>
<summary>scatter</summary>

| Group    | ⁵⁶Fe⁺/¹²C⁺ in faecal sample |
| -------- | --------------------------- |
| No drug  | 0.1                         |
| No drug  | 0.2                         |
| No drug  | 0.3                         |
| No drug  | 0.4                         |
| No drug  | 0.5                         |
| No drug  | 0.6                         |
| No drug  | 0.7                         |
| No drug  | 0.8                         |
| No drug  | 0.9                         |
| No drug  | 1.0                         |
| No drug  | 1.1                         |
| No drug  | 1.2                         |
| No drug  | 1.3                         |
| Ent-Hi   | 0.1                         |
| Ent-Hi   | 0.2                         |
| Ent-Hi   | 0.3                         |
| Ent-Hi   | 0.4                         |
| Ent-Hi   | 0.5                         |
| Ent-Hi   | 0.6                         |
| Ent-Hi   | 0.7                         |
| Ent-Hi   | 0.8                         |
| Ent-Hi   | 0.9                         |
| Ent-Hi   | 1.0                         |
| Ent-Hi   | 1.1                         |
| Ent-Hi   | 1.2                         |
| Ent-Hi   | 1.3                         |
| Ent-Hi   | 1.4                         |
| Ent-Hi   | 1.5                         |
| Ent-Hi   | 1.6                         |
| Ent-Hi   | 1.7                         |
| Ent-Hi   | 1.8                         |
| Ent-Hi   | 1.9                         |
| Ent-Hi   | 2.0                         |
</details>

d   
![](images/ff7a841372d4518cfcbaa83fe09012f5dc9d47d694a1389d3088ca3dee5e0bc4.jpg)

<details>
<summary>text_image</summary>

Signal intensity
12C+
56Fe+
MIn
MIn
Max
Max
Signal intensity
Signal intensity
</details>

e   
![](images/8e17e8ba03bd20932da2877c9622e8bf0c5c23384fb4753d0b96a53f457f6b44.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing fluorescently labeled cellular structures against a dark background (no text or symbols visible)
</details>

f   
![](images/db36557724aed8e74f3f26b95d6af930688c37d1b5c63e251976520aa8a2af86.jpg)

<details>
<summary>scatter</summary>

| Group    | ⁵⁶Fe⁺/¹²C⁺ in P. dorei |
| -------- | ---------------------- |
| No drug  | ~0.1                   |
| Ent-Hi   | ~3.8                   |
</details>

Fig. 5 | Entacapone-exposed microbiota cells display higher iron content. a,b, NanoSIMS overlay images of the 56Fe+ (colour scale) and 12C+ (grey scale) signal intensities of a faecal sample incubated for 6 h without drug (a) or ENT-Hi (b) in sM9 medium. Scale bars, 10 μm. c, Evaluation of 56Fe+ /12C+ secondary ion signal intensity ratios in individual cells present in faecal samples. d,e, NanoSIMS overlay images of the 56Fe+ (colour scale) and $^ { 1 2 } { \bf C } ^ { + }$ (grey scale) signal intensities in P. dorei cells incubated for 24 h with no drug (d) or ENT-Hi (e) in BMM medium. In the individual 12C+ images used for merging, the minimum and maximum intensities (grey scale) are: 1–16 counts per pixel (a), 2–25 counts per pixel (b), 4–80 counts per pixel (d) and 0–25 counts per pixel (e). In the individua $^ { 5 6 } { \mathsf { F e } } ^ { + }$   
images used for merging, the minimum and maximum intensities (colour scale) are: 3–10 counts per pixel (a), 3–35 counts/ per pixel (b), 7–17 counts per pixel (d) and 4–80 counts per pixel (e). Scale bar, 10 μm. f, Evaluation of $^ { 5 5 6 } \mathrm { F e } ^ { + } / ^ { 1 2 } \mathrm { C } ^ { + }$ + intensity ratios in individual P. dorei cells. Levels of significance (P values) displayed in c and f were calculated using unpaired two-sided Wilcoxon test comparing the groups ‘Ent-Hi’ and ‘No drug’. Each dot represents a single cell and boxes represent the median, first and third quartiles. Whiskers extend to the highest and lowest values that are within 1.5× the interquartile range. Single-cell measurements and calculations are shown in Supplementary Table 18.

# Entacapone promotes growth of iron-scavenging E. coli

Next, we interrogated the capability of the few indigenous microbiome members to thrive under the iron-limiting conditions induced by ENT-Hi. Several commensal and pathogenic Enterobacteriaceae, including E. coli, are known to synthesize and release siderophores that bind to Fe(III) with high affinity, enhancing their gut colonization41. The most dominant organism in ENT-Hi incubations is an E. coli strain classified as E. coli\_D42, for which we were able to recover a complete MAG (bin.187, Supplementary Table 8). A search for genes involved in siderophore synthesis within the E. coli\_D MAG led us to identify an entire gene cluster coding proteins necessary for synthesis, export and import of the siderophore enterobactin (Fig. 6a). Thus, we postulate that the ability of E. coli to produce enterobactin enables it to grow under iron-limiting conditions induced by ENT-Hi. Indeed, after isolation of a highly similar E. coli strain from glycerol-preserved ENT-Hi incubations (isolate E2, see Methods), we could confirm its ability to grow in minimal medium in the presence of ENT-Hi (Fig. 6b). Similarly, ENT-Hi supplementation did not significantly impact the growth of wild-type E. coli K12 strain BW25113, but it significantly reduced growth of BW25113 deletion mutants encoding proteins required for enterobactin production (entB) or enterobactin uptake (fepA) (Fig. 6c and Supplementary Table 19). The fepA mutant grows to higher levels than the entB mutant in the presence of entacapone, probably due to uptake of enterobactin breakdown products in complex with iron, which may enter the cell via other receptors43. Supplementation of the growth medium with enterobactin rescued the entacapone-induced growth defect of entB, but not of the fepA mutant (Fig. 6c), as expected. These results

![](images/63d8a07e3bfc2cea9b9d38176b34252c652fd19f1e4146c2a0fbb5e1d2bb56d5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["entH"] --> B["entA"]
    B --> C["entB"]
    C --> D["entE"]
    D --> E["entC"]
    E --> F["fepB"]
    F --> G["entS"]
    G --> H["fepD"]
    H --> I["fepG"]
    I --> J["fepC"]
    J --> K["fepE"]
    K --> L["entF"]
    L --> M["ybdZ"]
    M --> N["fes"]
    N --> O["fepA"]
    O --> P["entD"]
    
    Q["Chorismate"] --> R["Dihydroxybenzoate"]
    R --> S["Serine"]
    S --> T["Enterobactin"]
    
    style Q fill:#f9f,stroke:#333
    style R fill:#ccf,stroke:#333
    style S fill:#cfc,stroke:#333
```
</details>

![](images/5462e7e734f1e695eedaf2bf96856f973e9f9955fd50d93eb184de03f99f3dfe.jpg)

<details>
<summary>line</summary>

| Time (h) | No drug, Fe | No drug, no Fe | ENT-Hi, Fe | ENT-Hi, no Fe |
| -------- | ----------- | -------------- | ---------- | ------------- |
| 0        | 0.0         | 0.0            | 0.0        | 0.0           |
| 5        | 1.3         | 0.9            | 1.3        | 0.8           |
| 25       | 1.6         | 1.1            | 1.6        | 1.1           |
</details>

![](images/7140102774e77c549202e1d1bef94aa299f371edc814e5a5b8fa6e7675d71c69.jpg)

<details>
<summary>line</summary>

| Time (h) | No drug E. coli wt | No drug E. coli ΔentB | No drug E. coli ΔfepA | ENT-Hi E. coli wt | ENT-Hi E. coli ΔentB | ENT-Hi E. coli ΔfepA | ENT-Hi + Enterobactin E. coli wt | ENT-Hi + Enterobactin E. coli ΔentB | ENT-Hi + Enterobactin E. coli ΔfepA |
|----------|--------------------|------------------------|------------------------|-------------------|----------------------|----------------------|----------------------------------|------------------------------------|------------------------------------|
| 0        | 0.0                | 0.0                    | 0.0                    | 0.0               | 0.0                  | 0.0                  | 0.0                              | 0.0                                | 0.0                                |
| 10       | 0.06               | 0.06                   | 0.06                   | 0.04              | 0.04                 | 0.04                 | 0.06                             | 0.06                               | 0.04                               |
| 20       | 0.17               | 0.17                   | 0.17                   | 0.15              | 0.15                 | 0.15                 | 0.15                             | 0.15                               | 0.15                               |
| 30       | 0.20               | 0.20                   | 0.16                   | 0.17              | 0.17                 | 0.17                 | 0.17                             | 0.17                               | 0.17                               |
</details>

![](images/64fc19e59698812b72b2b5e666ae9a75b432f94491b485cd3d29c289ffc6f230.jpg)

<details>
<summary>text_image</summary>

d
No drug
ENT-Hi
ENT: Fe
ENT: Fe
ENT: Fe
ENT: Fe
Siderophores:
</details>

![](images/f33dfe051a70256f034e85847443a7fb0d4ba1ff581c91e52c398fec671ec6bf.jpg)

<details>
<summary>scatter</summary>

| Time (h) | No drug | ENT-Hi |
| -------- | ------- | ------ |
| 6        | 0.5     | 2.0    |
| 24       | 0.5     | 3.0    |
</details>

Fig. 6 | The iron-limiting conditions induced by entacapone select for siderophore producers and drive an increase in AMR and virulence potential in the faecal microbiome. a, Genetic organization of the enterobactin biosynthesis locus in E. coli D bin.187. Genes encoding enzymes involved in enterobactin biosynthesis (entABCDEFH) and export (entS) are highlighted in orange. The steps of enterobactin synthesis catalysed by the products of these genes are shown at the bottom. Genes involved in enterobactin import and iron release are highlighted in blue. b, Growth of the E. coli isolate E2, highly identical to E. coli D bin.187 determined by optical density measurements of cultures supplemented or not with entacapone (ENT-Hi) and/or FeSO (Fe). Data represent the mean ± s.e.m. of 3 independent growths. c, Growth of E. coli K12 BW25113 wild-type (wt), entB (ΔentB) or fepA (ΔfepA) mutants determined by optical density measurements of cultures supplemented or not with ENT-Hi and/   
or enterobactin. Data represent the mean ± s.e.m. of 3 independent growths (Supplementary Table 19). $^ { * } P _ { } < 0 . 0 5 , ^ { * * } P _ { } < 0 . 0 1 ; ^ { * * * } P _ { } < 0 . 0 0 1$ ; unpaired two-sided t-test with ‘E. coli wt’ used as the reference. d, Schematic representation of the working hypothesis. In the absence of entacapone (left), enough iron is available to most gut microbiome members. Under ENT-Hi conditions, entacapone complexes available iron (ENT:Fe), and only organisms able to produce and/or import siderophores (represented by diamonds) for iron scavenging are able to grow and thrive (right). Created with Biorender.com. e, Increase in the AMR and virulence index (Methods) in no drug controls and entacapone (ENT-Hi)-treated samples. Boxes represent the median, first and third quartiles. Whiskers extend to the highest and lowest values that are within 1.5× the interquartile range. Indicated P values were obtained from unpaired two-sided t-test comparing the groups ‘Ent-Hi’ and ‘No drug’ at each indicated timepoint.

strongly support that enterobactin synthesis and/or import is required for optimal growth in the presence of entacapone, and thus, that the presence of entacapone drives iron limitation. Enterobactin chelates ferric iron with much higher affinity than entacapone $( \mathsf { p F e } ( \mathsf { I I I } ) = 4 9 ) ^ { 4 4 }$ , and our results suggest that it enables E. coli to scavenge and acquire enough iron to sustain its growth under the iron-limiting conditions induced by entacapone (Fig. 6d). Interestingly, we could not find any genes involved in the production of known siderophores in the MAG of the Ruminococcus strain thriving under ENT-Hi conditions, but we found a gene encoding an orthologue of the membrane protein YfeB required for chelated iron transport in Yersinia pestis45 (Supplementary Table 16). We therefore speculate that Ruminococcus expands in the entacapone-supplemented medium by importing iron-loaded siderophores or other iron-chelating molecules, or by producing other high-affinity iron binding proteins46 (Fig. 6d).

Siderophore production and iron scavenging are commonly observed in pathogenic or pathobiont strains that also tend to encode other virulence traits41. A screening of our MAG catalogue for the presence of virulence factors and antimicrobial resistance (AMR) genes47 identified a diversified panel of AMR and virulence genes to be present in the retrieved gut MAGs (Supplementary Table 17), even though these samples originated from healthy individuals. ENT-Hi drives an increase in the abundance of AMR and virulence within faecal microbiomes (Fig. 6e). This increase is driven in great part by the increase in abundance of E. coli\_D, whose genome encodes a total of 14 AMR and virulence genes, in addition to at least one siderophore production cluster, thus suggesting a pathogenic potential of this organism. While we cannot rule out the possibility that the increased AMR and virulence index is due to improved genomic characterization of E. coli compared with other taxa, these results reveal that ENT-Hi promotes the growth of iron scavenging organisms with an associated pathogenic potential.

# Discussion

Gaining a deeper insight into the interactions between drugs and the gut microbiome is essential for revealing and predicting how the microbiome might influence the availability, efficacy and toxicity of pharmaceuticals. Here we demonstrated that loxapine succinate and entacapone cause major shifts in microbial communities at physiologically relevant concentrations, inhibiting the growth of many taxa while stimulating others. Using single-cell activity measurements, we further revealed fine changes in the activity of specific community members even at low drug concentrations that were not captured by sequencing (Figs. 1e and 2d, and Extended Data Fig. 5). This is a major advantage of our SRS–FISH approach as it captures drug-induced changes in short incubation times, which are ideal for ex vivo systems such as the one used here. Importantly, our results show that loxapine succinate exerts an effect on a broader range of taxa in the context of the community than its effects on microbes grown in pure culture1 . This highlights the necessity of using complex microbial communities for a better assessment of drug–microbiota interactions. One way by which some taxa may sensitize or protect others to a particular drug is through chemical conversion or accumulation of the drug9 . However, previous studies have shown that the gut microbiota neither significantly bioaccumulates nor transforms loxapine succinate9 . Thus, we presume that cross-sensitization to loxapine is probably due to drug-induced changes in microbial metabolites that are involved in interspecies interactions. These differences may, however, not be entirely related to cross-sensitization, but instead due to variations in growth conditions or in the genomic content of strains present in the faecal sample compared with the type strains tested in previous studies1 , which may limit the conclusions from our study.

Entacapone has been shown to be metabolized by gut microbial species9 , mostly by means of nitroreduction. Here we demonstrate that entacapone is also bioaccumulated, which probably results in depletion of entacapone in the surrounding environment over time, explaining the slight alleviation of entacapone’s inhibitory effect between 6 and 24 h of incubation (Fig. 1b). In addition, we further show that entacapone bioaccumulation does not necessarily lead to growth inhibition (Fig. 3f,g), similar to what has been described before for other bioaccumulated drugs such as duloxetine11. It remains to be determined whether entacapone bioaccumulation can be linked to its biotransformation. Despite its bioaccumulation and extensive conversion9 , we demonstrate that entacapone exerts a strong effect on the gut community due to its ability to complex iron via the catechol group, which is not affected by nitroreduction.

Iron is an essential enzyme cofactor in most bacteria36. Ferric iron complexation by entacapone led to a decrease in biomass accumulation and in the abundance of most of the top abundant taxa detected in our samples, an effect that was reversed by supplementation of iron (Fig. 4c–f). Most iron is expected to enter the large intestine in Fe(III) form, as the increase in pH in the duodenum favours the oxidation of Fe(II) in the presence of oxygen48. In fact, ferric iron is an important source of iron for the gut microbiota49, and we expect Fe(III) chelation by entacapone to impact microbiome homeostasis in the colon. Taxa not found to be significantly impacted by entacapone were presumably able to grow by releasing iron from this complex, or by relying on intracellularly accumulated iron or on high-affinity surface-associated iron transporters that are common in bacteria46. Among stimulated taxa, the siderophore-producing E. coli\_D strain present in our incubations greatly benefitted from entacapone’s presence, but only in the context of the community, as entacapone supplementation to an isolate alone did not cause any significant boost in growth (Fig. 6b). Thus, taxa stimulated by entacapone probably acquired iron via the mechanisms mentioned above, or via siderophores, and expanded in the community at the cost of nutrients released by dead cells or supplied via cross-feeding from other species. An increased abundance of Enterobacteriaceae was previously reported for Parkinson’s disease (PD) patients taking entacapone50. An increase in Enterobacteriaceae may also help to explain diarrhoea experienced by some patients taking entacapone. Our results are consistent with these findings, although they are based on short-term incubations of drugs with microbiomes of healthy individuals, which is a limitation of our study. To better understand the long-term effects of entacapone on the microbiome, it would be important to follow a cohort of PD patients before and during entacapone treatment. Entacapone is always prescribed in combination with levodopa to inhibit its off-site metabolism24, and such a cohort would also enable investigating the impact of this drug combination on the microbiome.

The expansion of an organism with siderophore synthesis, AMR and virulence potential in the presence of entacapone is concerning. As most successful gut pathogens tend to encode siderophore production systems, it would be important to determine whether entacapone treatment increases the likelihood of intestinal infections, similar to what has been observed in patients taking PPIs18. As oral iron supplementation reduces levodopa and entacapone absorption in the small intestine51,52, we hypothesize that the effect of entacapone on the microbiome could be circumvented in the future by the oral administration of iron between entacapone doses or, alternatively, by delivering iron to the colon of patients taking the drug. If administered in appropriate amounts, this proposed adjuvant therapy could help preserve microbiome homeostasis for patients taking entacapone and/or other catechol-containing drugs that might reach relevant concentrations in the large intestine. Colon-targeted adsorbents, such as DAV132, could also be tested, as these have shown the ability to sequester some drugs53. Our results advance our understanding of the impact of antipsychotic and antidyskinetic drug therapies on microbiome homeostasis and their mechanisms of action, and can direct future optimization of such therapies.

# Methods

# Human faecal sample collection

The study protocol was approved by the University of Vienna Ethics Committee (reference no. 00161) and the University of Southampton Ethics and Research Governance Office (reference no. 78743). All meta(data) were 100% anonymized and compliant with the University’s regulations. Human faecal samples were collected from 9 healthy adult individuals (3 males and 6 females between 22 and 39 years old) who had not received antibiotics in the previous 3 months and had no history of digestive disease. All study participants provided written informed consent and self-sampled using an adhesive paper-based faeces catcher (FecesCatcher, Tag Hemi) and a sterile polypropylene tube with the attached sampling spoon (Sarstedt). The participants did not receive any compensation to participate in this study.

# Drug concentrations used for incubations

We used two drug concentrations (low and high) of each drug for our incubations. The low drug concentration (ENT-Low or LOX-Low: 20 μM) was previously used in a screening aimed at determining drug effects on pure culture isolates, while the high concentrations (ENT-Hi: 1,965 μM, LOX-Hi: 100 μM) were based on estimated colon concentrations for each drug and were included to better reflect the exposure of gut microbes to these drugs in the large intestine1 . The colon concentration estimated for entacapone is 1,965 μM (ref. 1), based on a typical oral dose of 200 mg, while for loxapine no estimate was available. We predicted that loxapine would reach similar colon concentrations as its chemical and therapeutic analogues amoxapine and clozapine, prescribed at similar doses (10–20 mg daily) and estimated to reach colon concentrations of 138 μM and 153 μM, respectively1 . Using these values as a reference, we predicted that loxapine succinate should be present in the colon at concentrations of at least 100 μM and chose it as the LOX-Hi concentration. Both drugs are found in their parent form in human plasma samples54,55. Some drug metabolites have also been shown to be present, but these are largely products of liver metabolism56, which is an indication of low levels of chemical transformation of these drugs in the upper gastrointestinal tract before absorption.

# Ex vivo gut microbiome incubations with drugs

For data shown in Figs. 1, 2 and 3, samples from 6 donors (2 males, 4 females, between 25 and 39 years old) were transferred into an anaerobic tent (Coy Laboratory Products) within 30 min after sampling, and all sample manipulation and incubations were performed under anaerobic conditions $( 5 \% \mathsf { H } _ { 2 } , 1 0 \% \mathsf { C O } _ { 2 } , 8 5 \% \mathsf { N } _ { 2 } )$ . Each sample was suspended in M9 mineral medium supplemented with $0 . 5 \mathrm { m g } \mathrm { m l ^ { - 1 } }$ d-glucose (Merck), 0.5% (v/v) vitamin solution (DSMZ Medium 461) and trace minerals, herein referred to as sM9. Samples were suspended in sM9 to yield a 0.05 g ml−1 faecal slurry. At this point, one aliquot of each sample was collected, pelleted and stored at $- 8 0 { } ^ { \circ } \mathrm { C }$ for metagenomic analysis. The homogenate was left to settle for 10 min, and the supernatant (devoid of any large faecal particles) was transferred into a different flask where supernatants from the 6 different donors were combined. This combined sample was further diluted 1:10 in sM9 medium (as described above) or in supplemented brain heart infusion (BHI) medium containing either 0% or 55% D O (99.9% atom % (at%) D, Merck) for a final 0% (control) or 50% D2O in the incubation medium (Fig. 1a). Supplemented BHI medium consisted of 37 g l−1 BHI broth (Oxoid), $5 \mathrm { g } \mathsf { I } ^ { - 1 }$ yeast extract (Oxoid), $\mathbf { 1 } \mathbf { g } \mathbf { l } ^ { - 1 } \mathbf { l }$ l-cysteine (Merck) and 1 g l−1 NaHCO3 (Carl Roth). Incubation tubes were supplemented with dimethylsulfoxide (DMSO, Merck), entacapone (Prestwick Chemicals) or loxapine succinate (Prestwick Chemicals) predissolved in DMSO. The final concentration was 2% (w/v) DMSO in all vials (except for the H O control, where water was added instead of DMSO). After short incubation times (6 and 24 h) under anaerobic conditions at $3 7 ^ { \circ } \mathrm { C }$ , samples were collected as detailed below and processed to determine: (1) changes in the total microbial loads; (2) microbial community profile dynamics based on 16S rRNA gene amplicon sequencing; (3) reconstructed microbial genomes based on long-read metagenomics and (4) single-cell microbial activity changes via tracing of the incorporation of deuterium from isotopically labelled heavy water $( \mathsf { D } _ { 2 } \mathbf { O } )$ into single cells of microbiota by chemical imaging based on ${ \mathsf { S R S } } ^ { 3 2 }$ (Fig. 1a).

At time 0 and after an incubation time of 6 or 24 h at $3 7 ^ { \circ } \mathrm { C }$ under anaerobic conditions, two sample aliquots from each incubation and from controls were collected by centrifugation. One aliquot was washed with 1× PBS and then fixed in 3% paraformaldehyde (PFA) solution for 2 h at 4 °C. Samples were finally washed twice with 1 ml PBS and stored in PBS:ethanol (50% v/v) at ${ } ^ { - 2 0 } { } ^ { \circ } \mathrm { C }$ until further use. The second pelleted aliquot was stored at $- 2 0 { } ^ { \circ } \mathrm { C }$ until further processing. A third aliquot was collected into sealed anaerobic vials containing 40% glycerol (Carl Roth) in PBS for a final 50% (v/v) cell suspension in 20% glycerol and stored at $- 8 0 { } ^ { \circ } \mathrm { C }$ until further use. In addition, amendment of ENT-Hi to 3 individual faecal samples (2 females and 1 male, average age: 26.3 years) and sample processing were carried out as described above, except that samples were not mixed before incubation (Extended Data Fig. 2).

For iron rescue experiments, fresh faecal samples received from 5 out of the 6 individuals that participated in the initial drug supplementation experiment (except for 1 male that was travelling at the time of the experiment) were collected and processed as described above. Donors were between 25 and 38 years old. To establish appropriate controls for imaging of entacapone bioaccumulation by microbiota cells, an aliquot of the freshly prepared 0.05 g ml−1 faecal slurry was immediately fixed with either 3% PFA solution or ethanol (50% v/v) at $4 ^ { \circ } \mathbb { C }$ for 2 h. Fixed faecal samples were washed with 1× PBS as described above and incubations with fixed samples and entacapone or entacapone:iron (see below) were conducted in parallel with incubations using live samples. Incubation vials were then supplemented with 2% (v/v) DMSO with or without 1,965 μM entacapone, in the presence or absence of supplemented iron (1 mM $\mathsf { F e S O } _ { 4 } ,$ Merck; Fig. 5). Additional incubation vials (triplicates) were treated with entacapone pre-complexed with iron: briefly, entacapone and iron $\mathrm { ( F e S O _ { 4 } ) }$ or $\mathsf { F e C l } _ { 3 } )$ powder were mixed and resuspended in 2 ml DMSO, yielding a final concentration of 1,965 μM entacapone and 1 mM FeSO4 (or FeCl3), and stored overnight under anaerobic conditions. The next day, 120 μl of monobasic sodium phosphate (0.5 M) was added and the samples were mixed well. After 20 min, samples were centrifuged at 14,000 g for 5 min to remove unbound iron precipitated by the addition of sodium phosphate57. The supernatant containing the iron-complexed entacapone was collected into a new Eppendorf tube and supplemented to the faecal incubation vials. Incubations were sampled as described above.

# Cell counts from ex vivo microbiome incubations

Microbial loads in faecal incubation vials were determined using flow cytometry and counting beads as detailed below. Samples preserved in glycerol were diluted 200–800 times in 1× PBS (Supplementary Table 1). To remove any additional debris from the faecal incubations, samples were transferred into a flow cytometry tube by passing the sample through a snap cap containing a 35-μm-pore-size nylon mesh. Next, 500 μl of the microbial cell suspension was stained with the nucleic acid dye SYTO 9 (Thermo Fisher, 0.5 μM in DMSO) for 15 min in the dark. The flow cytometry analysis of the microbial cells present in the suspension was performed using a BD FACSMelody cell sorter (BD Biosciences), equipped with a BD FACSChorus software v.3.0 (BD Biosciences). Briefly, background signals from the instrument and the buffer solution (PBS) were identified using the operational parameters forward scatter (FSC) and side scatter (SSC). Microbial cells were then displayed with the same settings in a scatterplot using the forward scatter (FSC) and side scatter (SSC), and pre-gated on the basis of the presence of SYTO 9 signals (Extended Data Fig. 10). Singlets discrimination was performed. Absolute counting beads (CountBright, Thermo Fisher) added to each sample were used to determine the number of cells per ml of culture by following manufacturer instructions. Fluorescence signals were detected using the blue (488 nm, staining with SYTO 9 and CountBright beads) and yellow-green (561 nm, CountBright beads only) optical lasers. The gated fluorescence signal events were evaluated on the forward–sideways density plot to exclude remaining background events and obtain an accurate microbial cell count. Microsoft Excel v.16.87 was used for data sorting (Supplementary Table 1). Instrument and gating settings were identical for all samples (fixed staining–gating strategy), and gating strategy is exemplified in Extended Data Fig. 10.

# Nucleic acid isolation and 16S rRNA gene sequencing

Pellets of microbiome incubation samples were resuspended in 600 μl of lysis solution RL (InnuPREP DNA/RNA mini kit, Analytik Jena) and subjected to bead beating for 30 s at 6.5 m s−1 in lysis matrix E (MP Biomedicals) tubes. After pelleting cell debris for 10 min at 8,000 g, supernatants were transferred into the InnuPREP DNA/RNA mini kit spin filter tubes (Analytik Jena), and DNA and RNA were extracted according to manufacturer protocol. Amplification of bacterial and archaeal 16S rRNA genes from DNA extracts was performed with a two-step barcoding approach (UDB-H12)58

In the first-step PCR, the primers 515F59 (5′-GTGYCAGCMGCC GCGGTAA-3′) and 806R60 (5′-GGACTACNVGGGTWTCTAAT-3′), including a 5′-head sequence for 2-step PCR barcoding, were used. PCRs, barcoding, library preparation and Illumina MiSeq sequencing were performed by the Joint Microbiome Facility (Vienna, Austria) under project numbers JMF-2208-05 and JMF-2103-29. First-step PCRs were performed in triplicate (12.5 μl vol per reaction) with the following conditions: 1× DreamTaq buffer (Thermo Fisher), 2 mM MgCl2 (Thermo Fisher), 0.2 mM dNTP mix (Thermo Fisher), 0.2 μM of forward and reverse primer each, 0.08 mg ml−1 bovine serum albumin (Thermo Fisher), 0.02 U DreamTaq polymerase (Thermo Fisher) and 0.5 μl of DNA template. Conditions for thermal cycling were: $9 5 ^ { \circ } \mathrm { C }$ for 3 min, followed by 30 cycles of 30 s at $9 5 ^ { \circ } \mathrm { C } ,$ , 30 s at $5 2 ^ { \circ } \mathrm { C }$ and 50 s at $7 2 ^ { \circ } \mathrm { C }$ , and finally 10 min at $7 2 ^ { \circ } \mathbf { C }$ Triplicates were combined for barcoding (with 8 PCR cycles). Barcoded samples were purified and normalized over a SequalPrep Normalization Plate kit (Invitrogen) using a Biomek NXP Span-8 pipetting robot (Beckman Coulter), and pooled and concentrated on PCR purification columns (Analytik Jena). Indexed sequencing libraries were prepared with the Illumina TruSeq Nano kit according to manufacturer instructions61 and sequenced in paired-end mode (2× 300 bp, v3 chemistry) on an Illumina MiSeq system following manufacturer instructions. The workflow systematically included four negative controls (PCR blanks, that is, PCR-grade water as template) for each 90 samples sequenced. The 16S rRNA gene sequences were deposited in the NCBI Sequence Read Archive (SRA) as BioProject Accession PRJNA1033532.

# Analysis of 16S rRNA gene amplicon sequences

Amplicon pools were extracted from the raw sequencing data using the FASTQ workflow in BaseSpace (Illumina) with default parameters58. Demultiplexing was performed with the Python package demultiplex v.1.2.1 (Laros JFJ, github.com/jfjlaros/demultiplex) allowing one mismatch for barcodes and two mismatches for linkers and primers. DADA2 (ref. 62) R package v.1.16.0 (https://www.r-project.org/, R 4.0.2) was used for demultiplexing amplicon sequencing variants (ASVs) using a previously described standard protocol63. FASTQ reads were trimmed at 150 nt with allowed expected errors of 2. Taxonomy was assigned to 16S rRNA gene sequences on the basis of the SILVA taxonomy64 (release 138) using the DADA2 classifier.

Samples were analysed using the vegan (v.2.5-.6; https:// CRAN.R-project.org/package=vegan) and phyloseq65 (v.1.30.0) packages in R (https://www.r-project.org/, R 4.0.2). For samples subjected to different drug treatments, sequencing in parallel with two extraction controls (without adding faecal samples) yielded 10 (control 1) and 189 reads (control 2). In control 1, 9 of the 10 reads were assigned to Cyanobacteria or chloroplast and were not detected in the samples. Likewise, in control 2, more than 90% of the reads originated from either Cyanobacteria ASVs or a single Comamonadaceae (Aquabacterium) not detected in any of the samples. These ASVs were removed from analysis. The remaining negative control reads (control 1: 1 read, control 2: 8 reads) were assigned to taxa typically found in the gut that were also detected in the samples and were therefore retained for subsequent analyses. We assumed these low number of reads to originate from a low level of cross-contamination that can occur when multiple samples are handled in parallel. After quality filtering and removal of contaminant sequences, a total of 1,132 ASVs were retained. The average read number per sample was 11,176 ± 3,087 high-quality sequences and sample coverage was above 98% (Supplementary Table 2). For alpha and beta diversity analysis, sequence libraries were rarefied to 4,681 reads per sample. For samples referring to the entacapone and iron supplementation experiment, sequencing in parallel with two extraction controls yielded 2 (control 1) and 134 reads (control 2). After quality filtering and removal of contaminant sequences (using the rationale described above), a total of 716 ASVs were retained. The average read number per sample was 18,733 ± 4,427 high-quality sequences and the sample coverage was above 99% (Supplementary Table 2). For alpha diversity analysis, sequence libraries were rarefied to 9,729 reads per sample. For quantitative microbiome analyses, relative abundances of each taxon in a sample were calculated after correcting for the different number of copies of the 16S rRNA gene, according to rrnDB (v.5.7). For this correction, we classified ASVs using DADA2 and the RDP66 taxonomy 18, release 11.5 (https://doi.org/10.5281/zenodo.4310151), by applying default parameters. These corrected relative abundances were then multiplied by the total microbial loads obtained from flow cytometry (Supplementary Table 1), yielding the total abundance of each taxon per sample.

DESeq2 (v.1.26.0)67 implemented in phyloseq was used to identify significant differences in ASV abundances between drug treatments. Only ASVs that had in total ≥10 reads (relative abundance microbial profile) or $5 . 0 \times 1 0 ^ { 5 }$ reads (quantitative microbial profile) were considered for comparisons by DESeq2 analyses. All statistical analysis of microbiome data was carried out in R (R 4.0.2). The applied significance tests and obtained P values are referred to in the main text and figure legends.

# Long-read sequencing

DNA for long-read sequencing was isolated using the DNeasy PowerSoil Pro kit (Qiagen), according to manufacturer instructions. A pool of 6 DNA extracts was prepared for sequencing using the ligation sequencing kit (SQK-LSK112, Oxford Nanopore) following manufacturer protocol. The DNA was sequenced on a Promethion P24 sequencing device (Oxford Nanopore) on an R10.4 flow cell (FLO-PRO112, Oxford Nanopore). The DNA sequencing was carried out using Minknow (v.21.10.8, Oxford Nanopore).

# Shotgun metagenomic sequencing

The same 6 samples were individually sequenced in an Illumina Novaseq 6000 platform by the Joint Microbiome Facility (Vienna, Austria) under project number JMF-2110-04. The Illumina reads were trimmed using cutadapt $( \mathbf { v } . 3 . 1 ) ^ { 6 8 }$ . Illumina reads were mapped to the assemblies using Minimap2 (v.2.17)69.

# Metagenomic analysis

The Nanopore reads were assembled using flye70 (v.2.9-b1768) with ‘–nano-hq’, polished three times with Minimap2 (v.2.17)69 and Racon (v.1.4.3)71, followed by two rounds of polishing with Medaka (v.1.4.4, github.com/nanoporetech/medaka). Illumina and Nanopore reads (Supplementary Table 7) were mapped to the assemblies using Minimap2 (v.2.17) and read mappings were converted using SAMtools (v.1.12)72. Read coverage and automatic binning was performed using MetaBAT2 (v.2.15)73. Contigs labelled as circular by the assembler were extracted as independent bins before the automated binning process. The quality of the recovered MAGs was checked using QUAST $( \mathsf { v } . 5 . 0 . 2 ) ^ { 7 4 }$ and CheckM (v.1.1.1)75, and genomes were classified using GTDBtk (v.1.5.1)42. rRNA genes were detected using Barrnap (v.0.9, https://github.com/tseemann/barrnap) and transfer (t)RNA genes were detected using trnascan $( \mathsf { v } . 2 . 0 . 6 ) ^ { 7 6 }$ . MAGs with completeness >90% but where barrnap did not pick up a 5S rRNA gene were checked for 5S rRNA genes using INFERNAL (v.1.1.3)77. MAGs were searched for iron-related genes and gene neighbourhood protein orthologues using FeGenie (v.1.2)78.

All MAGs were searched for AMR and virulence genes using AMRFinderPlus $( \mathsf { v } . 3 . 1 0 . 2 1 ) \AA ^ { 4 7 }$ 7, which identified genes encoding resistance to, among others, beta-lactams, tetracyclines, macrolides and aminoglycosides, as well as more general antimicrobial resistance genes such as efflux pumps and virulence genes (Supplementary Table 17). The AMR and virulence index (Fig. 6e) was calculated as follows: the total copies of AMR and virulence genes found to be present in each MAG were multiplied by the absolute abundance of the MAG (abundance of the ASV matching the 16S rRNA gene of the MAG) in the sample. The same was repeated for all MAGs for which AMRFinderPlus identified AMR or virulence genes and by summing these, we were able to predict the total number of copies of AMR and virulence genes for each sample, per ml of culture. The resulting values were then normalized to the total biomass per ml of each sample to obtain an AMR and virulence index per sample.

# FISH probe design and optimization

Phylogenetic analysis and FISH probe design were performed using the software ARB $( \mathbf { v . } 7 . 0 ) ^ { 7 9 }$ . By analysis of the 16S and 23S rRNA gene, phylogenetic trees were calculated with IQ-TREE $( \mathbf { v . l . 6 . 1 2 } )$ using the RAxML GTR algorithm with 1,000 bootstraps in $\mathbf { A R B } ^ { 8 0 }$ . For abundant groups, 4 FISH probes were designed for this study and 2 additional published probes were used (Supplementary Table 10). The probes were validated in silico with mathFISH to test the in silico hybridization efficiency of target and non-target sequences81,82. The number of non-target sequences was assessed using the probe match function in ARB and the mismatch analysis function in mathFISH. All probes were purchased from biomers (Biomers.net) and were double labelled with indocarbocyanine (Cy3) or sulfo-cyanine5 (Cy5) fluorochromes.

Pure cultures of Escherichia coli K12, P. dorei 175 (DSM 17855) and B. thetaiotaomicron VPI-5482 (DSM 2079) were grown in supplemented BHI until the mid-exponential phase and collected by centrifugation. Pure cultures were fixed for 2 h by addition of 3 volumes of 4% (w/v) PFA solution at $4 ^ { \circ } \mathbb { C }$ . After washing once with PBS, cells were stored in a 1:1 mixture of PBS and 96% (v/v) ethanol at $- 2 0 { } ^ { \circ } \mathrm { C }$ . Where pure cultures were not available, fixed faecal samples with a high relative abundance (as determined by amplicon sequencing) of the specific target taxon were used.

To evaluate probe dissociation profiles, cells obtained from fixed pure cultures or faecal incubation samples (Supplementary Table 10) were spotted onto microscopy slides (Paul Marienfeld). FISH was performed as described before81, with 3 or 5 h hybridization to obtain fluorescence signals with sufficient intensity. The optimal hybridization formamide concentration was found using formamide dissociation curves, obtained by applying a formamide concentration series in the range of 0–70% in 5% increments83. After a stringent washing step and counterstaining using 4′,6-diamidino-2-phenylindole, samples were visualized using a Leica Thunder epifluorescence microscope with an APO ×100/1.40 Leica oil immersion objective and the Leica Application Suite X software (LAS X 5.1.0). Probe EUB338 (ref. 84), which is complementary to a region of the 16S rRNA conserved in many members of the domain Bacteria, was used as a positive control, and a nonsense NON-EUB probe was applied to samples as a negative control for binding. Images for inferring probe dissociation profiles were recorded using the same microscopy settings and exposure times. The probe dissociation profiles were determined on the basis of the mean fluorescence signal intensities of at least 100 probe-labelled cells and evaluated using the ImageJ software (v.1.53t). From the calculated average values, a curve was plotted and the respective value right before a decline on each curve was defined as the optimal formamide concentration.

# FISH in solution

Fixed cells (100 μl) were pelleted at 14,000 g for 10 min, resuspended in 100 μl 96% analytical grade ethanol and incubated for 1 min at room temperature for dehydration. Subsequently, the samples were centrifuged at 14,000 g for 5 min, the ethanol was removed and the cell pellet was air dried. For SRS–FISH analysis, cells were hybridized in solution (100 μl) for 3 h at $4 6 ^ { \circ } \mathrm { C } .$ . The hybridization buffer consisted of 900 mM NaCl, 20 mM Tris-HCl, 1 mM EDTA and 0.01% SDS, and contained 100 ng of the respective fluorescently labelled oligonucleotide as well as the required formamide concentration to obtain stringent conditions (Supplementary Table 10). After hybridization, samples were immediately transferred into a centrifuge with a rotor preheated at 46 °C and centrifuged at 14,000 g for 15 min at the maximum allowed temperature $( 4 0 ^ { \circ } \mathrm { C } )$ to minimize unspecific probe binding. Samples were washed in a buffer of appropriate stringency for 15 min at $4 8 ^ { \circ } \mathrm { C }$ , and cells were centrifuged for 15 min at 14,000 g and finally resuspended in 20 μl of PBS. Cells $( 5 \mu \mathrm { l } )$ were spotted on poly-l-lysine-coated cover glasses no. 1.5H (170 μm ± 5 μm thickness, Paul Marienfeld) and allowed to dry overnight at 4 °C under protection from light. Salt precipitates were removed by dipping the coverslips twice in ice-cold Milli-Q water and the coverslips allowed to dry at room temperature under protection from light.

# Picosecond SRS and microscopy

In complex microbial communities, all metabolically active cells will incorporate deuterium (D) from D2O present in the medium into their biomass during synthesis of new macromolecules29. The newly formed carbon-deuterium (C-D) bonds can then be used as a read-out of microbial activity. SRS efficiently excites the Raman active vibrational modes coherently with two synchronized ultrafast lasers and was employed to determine the presence of C-D bonds and thus, microbial activity. In the SRS set up employed, an 80-MHz pulsed laser (InSight DeepSee+, Spectra-Physics) emitting two synchronized femtosecond beams was used (Extended Data Fig. 3a). One beam was tunable in wavelength from 680 nm to 1,300 nm, while the other beam had a fixed wavelength of 1,040 nm. The time delay between single pulses of the two beams is adjustable by a motorized delay line on the 1,040 nm beam. To implement the picosecond (ps) SRS (Extended Data Fig. 3), the fixed beam (termed Stokes beam) was intensity modulated at 2.5 MHz by an acousto-optic modulator (1205c, Isomet Corporation) and co-aligned with the tunable beam (termed pump beam) by a dichroic mirror (DMLP1000, Thorlabs). Both beams were chirped by SF57 rods to 2-ps pulse width and directed towards the lab-built upright microscope frame. Then, a 4-focal system and a flip mirror conjugated a pair of galvo mirrors to the back aperture of a ×60 water objective (UPlanApo ×60W, 1.2 NA, Olympus) or a ×100 1.49 NA oil objective (UAPON 100XOTIRF, Olympus), allowing the collinear pump and Stokes beams to raster-scan the sample via synchronized movement of the galvo mirrors. A 1.4 numerical aperture oil condenser (Aplanat Achromat 1.4, Olympus) collected the output beams, which were then reflected by a flip mirror and filtered by a short-pass filter (DMSP950, Thorlabs). Finally, the filtered-out pump beam was focused onto a silicon photodiode connected to a resonant amplifier effective at a resonant frequency of \~2.5 MHz. The output alternative current signal was further amplified by a lock-in amplifier (UHFLI, Zurich Instrument) at the frequency and in phase (x channel detection) with the modulation. The output direct current signal was recorded for normalization. A data acquisition card (PCIe-6363, National Instruments) collected the output signal for image generation.

To perform widefield fluorescence imaging for FISH visualization of the identical sample areas analysed by SRS and photothermal imaging, two flip mirrors were flipped off (Extended Data Fig. 3a). A halogen lamp (12V100WHAL, Olympus) provided Kohler illumination of the sample from the condenser side. Then, the objective and the tube lens conjugated the sample plane to the camera (CS505CU, Thorlabs).

To enable imaging of various fluorophores, different excitation and emission filter sets were inserted between the lamp and condenser, and in front of the camera. For Cy3 imaging, two 530/10 nm bandpass filters (FBH530-10, Thorlabs) were used as excitation filters and two 570/20 nm bandpass filters (ET570/20x, Chroma) were used as emission filters. For Cy5 imaging, two 640 nm bandpass filters (FBH640-10, Thorlabs) were used as excitation filters and two 670/20 nm bandpass filters (ET670/50 m, Chroma) were used as emission filters.

# Photothermal imaging of entacapone accumulation

By utilizing the multiphoton absorption of entacapone at 10 mM, we detected the photothermal signal originating from optical absorption to generate entacapone distribution maps. A concentrated solution of entacapone was needed for a test and we chose 10 mM to provide a strong signal (Fig. 3a). The experimental setup was identical to picosecond SRS, but with detection of the lock-in signal by the y channel, which exhibits a π/2 phase delay relative to the intensity modulation by the acousto-optic modulator (Supplementary Text and Extended Data Fig. 6b). With this orthogonal phase detection, the interference of the photothermal signal with the signals emerging from cross-phase modulation and SRS was minimized (Extended Data Fig. 6d).

# Image acquisition and processing

Samples were prepared by drying fixed bacterial cells spotted onto poly-l-lysine-coated coverslips (VistaVision cover glasses, No. 1, VWR) in a 4 °C refrigerator and subsequent dipping into water three times to dissolve precipitates from the growth media. Then the bacteria were immersed in 5 μl of water and sandwiched by another coverslip with a 0.11-mm-thick spacer in between. To acquire deuterium incorporation profiles of microbiome members labelled by FISH probes, widefield fluorescence was performed first. For different fluorophores, corresponding excitation and emission filters were applied. The signal and colour gain of the camera were set to 5. Then the exposure time was adjusted to 0.5–5 s depending on the fluorescence signal intensity. The widefield transmission image was acquired by minimizing the condenser aperture and removing the filters.

To acquire the deuterium incorporation profile of the FISH-visualized cells, two flip mirrors were inserted into the beam path to guide the pump and Stokes lasers to the sample. Three SRS images, specific for Raman active vibrational modes of C-D bonds, carbon-hydrogen (C-H) bonds as well as the off-resonance background signal were recorded by tuning the wavelength of the pump beam to 849 nm, 796 nm and 830 nm, respectively. These wavelength values correspond to spectral wavenumbers of $\mathbf { \lambda } ^ { 2 } , \mathbf { 1 6 3 c m ^ { - 1 } ( C { \cdot } D ) } , 2 , 9 4 7 \mathbf { c m ^ { - 1 } }$ (C-H) and $2 , 4 3 3 { \mathsf { c m } } ^ { - 1 }$ (silent region). Signal intensities were accumulated over increments of 20 cm−1. Images were acquired sequentially within the identical field of view of $3 2 \times 3 2 \mu \mathrm { m } ^ { 2 }$ with a raster step size of 106.8 nm. The per-pixel dwell time was set to 10 μs and, depending on the signal intensity level, 1\~10 image cycles were recorded to achieve a signal-to-noise ratio (SNR) of >5 for single bacterial cells in the C-H spectral region.

For acquisition of entacapone distribution maps, the pump laser was tuned to 849 nm and the signal detection was switched to the y channel of the lock-in amplifier. All images were recorded utilizing the identical scanning parameters as applied for SRS.

To process the image data sets: first, the illumination patterns were corrected for both widefield images (FISH) and point-scan images (SRS and entacapone distribution). Then, the widefield images and point-scan images were co-localized via a calibrated projective transform matrix. The fluorescence images were utilized to generate a single-cell mask for inference of the single-cell activity and the drug accumulation level. The single-cell activity is expressed as $\mathrm { \% C D _ { S R S } = }$ $\left( I _ { \mathrm { C D } } { - } I _ { \mathrm { o f f } } \right) / \left( I _ { \mathrm { C D } } { + } I _ { \mathrm { C H } } { - } 2 I _ { \mathrm { o f f } } \right)$ , where the symbols $I _ { \mathrm { C D } } , I _ { \mathrm { C H } }$ and $I _ { \mathrm { o f f } }$ refer to the SRS signal intensities detected at the spectral positions assigned to C-D bonds, C-H bonds and the silent region (off-resonance background). All intensity values were normalized to the direct current intensity level detected at the photodiode. The relative entacapone accumulation level is expressed as the signal intensity level detected in the y channel of the lock-in amplifier. Intensity outliers (>mean ± 2s.d.) observed in the SRS signals and the photothermal signal of the human gut microbiome samples were rejected from the single-cell masks. This intensity threshold was set after testing and validation with independent samples32, as food residues can be distinguished on the basis of an irregular shape compared with cells, and by a stronger signal due to other absorption processes that will gradually decrease due to the degradation of the absorption component. All imaging data analysis was performed with CellProfiler v.4.2.6 and Matlab R2023a.

# Bleaching of entacapone photothermal signal

Entacapone has a contribution to the lock-in amplifier x channel measurement that affects accurate $\% { \bf C D } _ { \mathrm { S R S } }$ measurements. To measure the levels of entacapone signal and activity $( \% { \bf C D _ { \mathrm { S R S } } } )$ in the same cell, we implemented a protocol to bleach the photothermal signal of entacapone that enables subsequent accurate activity measurements $( \% { \bf C D _ { 5 R S } } )$ . After measuring the entacapone photothermal signal, cells in the same field of view were bleached by continuous laser scanning with the same power used for imaging (power on sample: 30 mW pump and 120 mW Stokes; dwell time: 10 μs; 800 frames scanned in 720 s). This resulted in a sharp drop of signal in the y channel, which plateaud at 500 s, indicating a drop in entacapone signal to levels below the limit of detection (Extended Data Fig. 7a). This bleaching resulted in a smaller but detectable drop in intensity in the x channel that reached a plateau at around the same time as the y channel (500 s; Extended Data Fig. 7b). SRS measured in the x channel signal in cells that were not exposed to entacapone remained constant throughout the entire bleaching process, indicating that the drop in the x channel in ENT-Hi cells is indeed driven by the entacapone bleaching (Extended Data Fig. 7c). After bleaching, the SRS intensity became independent of entacapone levels and could then be used to determine the levels of activity per cell $( \% { \bf C D _ { 5 R S } } )$ . Correlation between $\mathsf { P T a t \% C D } _ { \mathsf { S R S } }$ was done in a mix of faecal samples (from 2 donors, 1 male and 1 female, age range 22–39 years) incubated with Ent-Hi and 50% D O in sM9 medium.

# Nanoscale secondary ion mass spectrometry (NanoSIMS) sample preparation and analysis

After incubation, cell fractions of faecal samples and P. dorei were washed once in PBS, fixed in a 3% PFA solution at $4 ^ { \circ } \mathrm { C }$ for 2 h and then stored in a suspension of PBS and ethanol (1:1) $\mathsf { a t 4 } ^ { \circ } \mathsf C .$ . For sample preparation, each suspension was diluted in 150 µl ultrapure water and homogenized in a sonication bath (Sonorex-Super\_RK-31, Bandelin) at 35 kHz twice for 30 s to separate single cells from cellular aggregates. Cells were then collected and concentrated by filtration on gold coated (film thickness 150 nm, obtained by sputter deposition) polycarbonate filters (GTTP type, 0.2 µm pore size, Millipore) to a density of 200–300 cells per 65 × 65 µm2 . To remove PBS precipitates and residual ethanol, filters were washed with ultrapure water and air dried after spotting of the cell suspensions. The density and distribution of single cells was inspected by light microscopy utilizing air objectives. Appropriate regions for NanoSIMS analysis were marked by a laser microdissection microscope (Leica LMD 7000). Selected filter regions were attached to antimony-doped silicon wafer platelets (7.1 × 7.1 mm, Active Business) serving as sample carriers.

NanoSIMS measurements were conducted on a NanoSIMS 50L ion microprobe (Cameca) equipped with a Hyperion RF-Plasma O− ion source (Oregon Physics) at the Large-Instrument Facility for Environmental and Isotope Mass Spectrometry at the University of Vienna. Before data acquisition, analysis areas were presputtered by rastering of a high-intensity (500 pA beam current), defocused O− ion beam to an O− ion fluence of 2 $. 6 \times 1 0 ^ { 1 6 }$ ions cm−2. Data were acquired as multilayer image stacks by repeated scanning of a finely focused O− primary ion beam (\~100 nm probe size at 12 pA beam current) over areas between $5 0 \times 5 0 \mu \mathrm { m } ^ { 2 }$ and $6 5 \times 6 5 { \mu \mathrm { m } } ^ { 2 } { \mathrm { a t } } 5 1 2 \times 5 1 2$ pixel image resolution and a primary ion beam dwell time of 5 ms $\mathsf { p i x e l } ^ { - 1 }$ 1. The detectors of the multicollection assembly were positioned for simultaneous detection of 12C+ ,  23Na+ ,  31P+ ,  40Ca+ and $^ { 5 6 } { \mathsf { F e } } ^ { + }$ secondary ions. The mass spectrometer was tuned to achieve a mass resolving power of >8,000 (according to Cameca’s definition) for detection o $\mathsf { f } ^ { 5 6 } \mathsf { F e } ^ { + }$ + secondary ions.

NanoSIMS images were generated and analysed with the Open-MIMS85 plugin v.3.0.5 in the image processing package Fij $( \mathbf { 1 . 5 4 g } ) ^ { \mathbf { 8 \epsilon } }$ 6. All images were autotracked for compensation of primary ion beam and/ or sample stage drift, and secondary ion signal intensities were corrected for detector dead time. For visualization of the iron distribution pattern between cells from individual samples, overlay images of the secondary ion signal intensities o ${ \hat { \mathbf { \Gamma } } } ^ { 1 2 } \mathbf { C } ^ { + }$ (shown on a grey scale) and $^ { 5 6 } \mathsf { F e } ^ { + }$ (shown on a rainbow colour scale) were generated (Fig. 5). Region of interest (ROI) specific numerical data evaluation was applied to display the relative iron content of single cells via normalization of the $^ { 5 6 } { \mathsf { F e } } ^ { + }$ signal intensity to the respective 12C+ signal intensity (Supplementary Table 18). ROIs were defined utilizing carbon as a reference element indicating biomass, visualized by the 12C+ secondary ion signal intensity distribution images. The presence of single cells was confirmed via their morphological appearance in the 23Na+ and 40Ca+ secondary ion maps.

# Siderophore assay

The iron binding capacity of entacapone was tested using the SideroTec Assay (Accuplex Diagnostics), a colorimetric test for the detection of siderophores, following manufacturer instructions. Wells were read photographically and on a microplate reader at 630 nm wavelength (Multiskan GO microplate spectrophotometer, Thermo Fisher).

# Measurement of Fe(II) using ferrozine

The ferrozine chromogenic method, in which ferrozine reacts with free divalent Fe to form a stable magenta complex species with a maximum absorbance at 562 nm (ref. 87), was used to determine the ability of entacapone to complex Fe(II) and to follow the presence of Fe(II) in incubations with entacapone. All solutions were prepared in degassed solvents or buffers to prevent spontaneous iron oxidation. To determine the ability of entacapone to complex Fe(II), FeSO4·7H2O (Carl Roth) was dissolved in distilled water to produce a 183.3 µM Fe(II) working solution. Ferrozine (BLD Pharmatech) was dissolved in distilled water to produce a 246.3 µM ferrozine working solution. ${ \bf N a } _ { 2 } { \bf H } _ { 2 } { \bf E D T A }$ (Carl Roth) was dissolved in Tris-HCl buffer $\mathsf { p H } 7 . 5 \mathsf { t o }$ produce a 50 mM stock solution, and entacapone was dissolved in DMSO/water (1:1) to produce a 2 mM solution. Both ${ \bf N a } _ { 2 } { \bf H } _ { 2 } { \bf E D T A }$ and entacapone were further diluted to the final concentrations shown in Extended Data Fig. 9a. A volume of 50 µl of Fe(II) working solution was then added to a 96-well plate, followed by addition of 50 µl of a chelator solution (diluted in water as needed). Ferrozine working solution $( 1 0 0 \mu \mathrm { l } )$ was then added and the absorption was measured at 526 nm with a Tecan plate reader after 10 min of incubation. To determine the ability of pure DMSO to oxidize iron, $\mathrm { F e S O } _ { 4 } { \cdot } 7 \mathrm { H } _ { 2 } 0$ (Carl Roth) was dissolved in pure DMSO (Merck) or water to produce 50 µM Fe(II) working solutions. Each solution was aliquoted into a 96-well plate and an equal volume of a 0.2 M ferrozine solution (and respective dilutions) was added. Absorption was measured at 526 nm with a Tecan plate reader after 10 min of incubation. Finally, to determine the oxidation of Fe(II) in sM9 media, a 1 mM $\mathsf { F e S O } _ { 4 }$ stock solution was prepared by dissolving $\mathrm { F e S O } _ { 4 } { \cdot } 7 \mathrm { H } _ { 2 } 0$ in sM9 media or water. After 1, 5, 10, 15 and 30 min of incubation at room temperature, 50 µl was added to a 96-well plate and diluted with 50 µl water. Ferrozine solution (100 µl, 2 mM) was added and the absorption was measured at 526 nm with a microplate reader (Tecan). For the immediate timepoint, 48.75 µl of sM9 media was added to a 96-well plate. Subsequently, 1.25 µl of a 40 mM $\mathsf { F e S O } _ { 4 }$ solution, 50 µl degassed water and 100 µl of a 2 mM ferrozine solution were added and the absorption measured at 526 nm. A calibration curve was established using FeSO4 stock solutions (1, 0.5, 0.25, 0.125, 0.0625 and 0.03125 mM). For this, 50 µl of each $\mathsf { F e S O } _ { 4 }$ stock solution was added to a 96-well plate and diluted with 50 µl water. Ferrozine solution (100 µl, 2 mM) was added to each well and absorption was measured at 526 nm with a Tecan plate reader after 10 min of incubation at room temperature.

# Isolation and sequencing of an E. coli isolate

Escherichia coli isolate E2 was isolated from glycerol-preserved faecal samples (mix of samples from 6 donors, 4 females and 2 males aged 25–39 years; ethics reference no. 00161) after incubation in sM9 medium supplemented with 1,965 μM entacapone for 48 h under anaerobic conditions. An aliquot of the glycerol stock was serially diluted in PBS, and $1 0 ^ { - 4 }$ and $1 0 ^ { - 5 }$ dilutions were plated in BHI agar. Isolated colonies were restreaked 3 times to purity and submitted to colony PCR using the 16S rRNA gene primers 616V (5′-AGA GTT TGA TYM TGG CTC AG-3′) and 1492R (5′-GGT TAC CTT GTT ACG ACT T-3′). Single colonies were picked with an inoculation loop, resuspended in 50 μl of nuclease-free water and boiled at ${ 9 5 ^ { \circ } } \mathrm { C }$ for 10 min to lyse the cells and release cell contents. After a short spin to pellet cell debris, 2 μl of the supernatant was added to a PCR reaction mix (final concentrations; Green 1× DreamTaq buffer, dNTPs 0.2 mM, BSA 0.2 mg ml−1, Taq polymerase $0 . 0 5 \mathrm { U } \mu \mathrm { I } ^ { - }$ 1, primers 1 μM) prepared in a final volume of 50 μl per reaction. The amplification cycles were as follows: initial denaturation at 95 °C for 3 min, followed by 30 cycles at $9 5 ^ { \circ } \mathrm { C }$ for 30 s, 52 °C for 30 s, 72 °C for 1.5 min and a final elongation at $7 2 ^ { \circ } \mathrm { C }$ for 10 min. PCR products were visualized on 1.5% agarose gel electrophoresis, and subsequently cleaned and concentrated on columns (innuPREP PCRpure kit, Analytik Jena) according to manufacturer instructions. Concentrations were measured using Nanodrop and samples were sent for Sanger sequencing to Microsynth (Vienna, Austria). Sequencing results were analysed using BLASTn88 against the 16S rRNA gene sequences retrieved by metagenomics. The near full-length 16S rRNA gene sequences of isolate E2 obtained were 99% identical to the 16S rRNA copies of E. coli D bin.187 and 100% identical to ASV\_9ec\_9n4.

# Growth of microbial pure cultures

Bacteroides thetaiotaomicron (DSM 2079) cells were grown anaerobically $( 8 5 \% \mathrm { N } _ { 2 } , 1 0 \% \mathrm { C O } _ { 2 } , 5 \% \mathrm { H } _ { 2 } ) \mathrm { a t } 3 7 ^ { \circ } \mathrm { C }$ in Bacteroides minimal medium (BMM) containing $2 7 . 5 \mu \mathrm { M }$ of iron $( \mathsf { F e S O } _ { 4 } , \mathsf { M e r c k } ) ^ { \mathrm { 8 9 } }$ . Bacteroides and Phocaeicola (formerly Bacteroides) species do not grow well in sM9 medium when in isolation. Therefore, we used BMM, a defined medium tailored for Bacteroides spp.89 for which the concentration of iron is known and can be controlled. To test the effect of iron on rescuing the inhibitory effect of entacapone on B. thetaiotaomicron growth, entacapone-treated (1,965 μM) cultures were supplemented with $1 0 0 \mu \mathrm { M } , 5 0 0 \mu \mathrm { M }$ or 1 mM of iron. Growth rescue was observed when cultures were supplemented with either $5 0 0 \mu \mathrm { M F e S O } _ { 4 }$ (Fe(II)) or FeCl3 (Fe(III)), and for all subsequent experiments, only $\mathsf { F e S O } _ { 4 }$ was used. Cu(II)SO (500 μM or 1 mM, Merck) or entacapone preloaded with iron (1,965 μM, prepared as described above) were also supplemented to B. thetaiotaomicron cultures. Fe-loaded entacapone was obtained by addition of 1 mM of Fe(II) $\scriptstyle ( { \mathrm { F e S O } } _ { 4 } )$ or Fe(III) (FeCl3) to ENT-Hi, followed by removal of any excess iron cations via phosphate precipitation57. Samples for total cell counts were taken at $^ { 0 , }$ 24 and 48 h of growth under anaerobic conditions. Phocaeicola dorei (DSM 17855) was grown in BMM in the presence or absence of 1,965 μM entacapone. After 24 and 48 h of growth, an aliquot was collected and fixed with PFA as described above, and stored $\mathsf { a t } - 2 0 ^ { \circ } \mathsf C$ in PBS:ethanol 50% (v/v) until further analyses. To test whether the growth of the E. coli faecal isolate E2 was dependent on the presence of iron, the isolate was grown in MOPS medium with or without $1 0 \mu \mathrm { M F e S O _ { 4 } }$ in the presence or absence of entacapone for 24 h at $3 7 ^ { \circ } \mathrm { C } .$ MOPS medium was chosen as it enables the reduction of free-iron concentration to growth-limiting levels compared with media containing M9 salts90 (such as sM9). Wild-type E. coli K12 strain BW25113, entB mutant and fepA mutants (Keio collection strains OEC5042, OEC4987-213605695 and OEC4987-200829240, respectively) were purchased from Horizon discovery (https://horizondiscovery.com). Isolated colonies of BW25113 wild-type and mutant strains for entB (encoding the enterobactin synthase component B) and fepA (encoding a ferric enterobactin Ton-B-dependent outer membrane transporter) were grown anaerobically in MOPS medium with no additional iron. To avoid the transfer of any iron from the pre-inoculum, pre-inoculum cells were washed thoroughly in MOPS medium without iron before inoculation. Enterobactin (Merck) was dissolved in DMSO (2 mM) and supplemented to the medium to a final concentration of 2 μM, as needed.

# Determination of total cell loads in pure cultures

To determine microbial cell loads in pure culture, samples were collected at 0, 24 or 48 h of growth and stained (either undiluted or after a dilution of 10 times in 1× PBS) with the QUANTOM Total Cell Staining kit (Logos Biosystems). Total cell counts were determined using a QUANTOM Tx Microbial Cell Counter (Logos Biosystems) following manufacturer instructions.

# Study design and statistical analyses

No statistical methods were used to predetermine sample sizes, but our sample sizes are similar to those reported in previous publications7,32. Data distribution was assumed to be normal but this was not formally tested. For microcosm experiments, faecal samples were thoroughly mixed before allocation to microcosms, and allocations to microcosms were performed randomly. For flow cytometry, cell counts, SRS and photothermal measurements and analyses, both sample preparation and sample measurements were randomized. Preparation of samples for sequencing was randomized. For Nano-SIMS, we first analysed the entacapone-treated samples followed by the untreated controls to confirm that the observed Fe distribution patterns were not affected by measurement artefacts. Blinding during the microcosm and pure-culture experiments was not possible, as different samples had to receive a different treatment/drug. Sample preparation for sequencing was carried out by an independent investigator in a blinded manner. Initial steps of sequencing data processing were performed blindly. Bioinformatic analyses of sequencing data were performed using automated software but were not blinded to identify samples for direct comparisons. For all other experiments or assays, the investigators were not formally blinded because of the high demand for certain samples and timepoints, which required appropriate sample selection.

# Reporting summary

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

# Data availability

The 16S rRNA gene sequencing data, metagenomics data and retrieved MAGs have been deposited in the National Center for Biotechnology Information (NCBI) Sequence Read Archive under BioProject number PRJNA1033532. Databases used were: the Genome Taxonomy Database (GTDB) v.0.1.3 (https://gtdb.ecogenomic.org/); RDP taxonomy 18, release 11.5 (https://doi.org/10.5281/zenodo.4310151); Short Read Archive (https://www.ncbi.nlm.nih.gov/sra); SILVA taxonomy (release 138) using the DADA2 classifier (https://zenodo.org/records/4587955); and the SILVA 119 SSU NR99 database (https://www.arb-silva.de/ download/arb-files/).

# Code availability

CellProfiler pipelines and Matlab codes have been deposited in GitHub91.

# References

1. Maier, L. et al. Extensive impact of non-antibiotic drugs on human gut bacteria. Nature 555, 623–628 (2018).   
2. Weersma, R. K., Zhernakova, A. & Fu, J. Interaction between drugs and the gut microbiome. Gut 69, 1510–1519 (2020).   
3. Lynch, S. V. & Pedersen, O. The human intestinal microbiome in health and disease. N. Engl. J. Med. 375, 2369–2379 (2016).   
4. Zhernakova, A. et al. Population-based metagenomics analysis reveals markers for gut microbiome composition and diversity. Science 352, 565–569 (2016).   
5. Jackson, M. A. et al. Gut microbiota associations with common diseases and prescription medications in a population-based cohort. Nat. Commun. 9, 2655 (2018).   
6. Vich Vila, A. et al. Impact of commonly used drugs on the composition and metabolic function of the gut microbiota. Nat. Commun. 11, 362 (2020).   
7. Li, L. et al. RapidAIM: a culture- and metaproteomics-based Rapid Assay of Individual Microbiome responses to drugs. Microbiome 8, 33 (2020).   
8. Zimmermann, M., Zimmermann-Kogadeeva, M., Wegmann, R. & Goodman, A. L. Separating host and microbiome contributions to drug pharmacokinetics and toxicity. Science 363, eaat9931 (2019).   
9. Zimmermann, M., Zimmermann-Kogadeeva, M., Wegmann, R. & Goodman, A. L. Mapping human microbiome drug metabolism by gut bacteria and their genes. Nature 570, 462–467 (2019).   
10. van Kessel, S. P. et al. Gut bacterial tyrosine decarboxylases restrict levels of levodopa in the treatment of Parkinson’s disease. Nat. Commun. 10, 310 (2019).   
11. Klünemann, M. et al. Bioaccumulation of therapeutic drugs by human gut bacteria. Nature 597, 533–538 (2021).   
12. Tropini, C. et al. Transient osmotic perturbation causes long-term alteration to the gut microbiota. Cell 173, 1742–1754.e17 (2018).   
13. Fung, T. C. et al. Intestinal serotonin and fluoxetine exposure modulate bacterial colonization in the gut. Nat. Microbiol. 4, 2064–2073 (2019).   
14. van Kessel, S. P., Bullock, A., van Dijk, G. & El Aidy, S. Parkinson’s disease medication alters small intestinal motility and microbiota composition in healthy rats. mSystems 7, e01191-21 (2022).   
15. Bhatt, A. P. et al. Targeted inhibition of gut bacterial β-glucuronidase activity enhances anticancer drug eficacy. Proc. Natl Acad. Sci. USA 117, 7374–7381 (2020).   
16. Wu, H. et al. Metformin alters the gut microbiome of individuals with treatment-naive type 2 diabetes, contributing to the therapeutic efects of the drug. Nat. Med. 23, 850–858 (2017).   
17. Sun, L. et al. Gut microbiota and intestinal FXR mediate the clinical benefits of metformin. Nat. Med. 24, 1919–1929 (2018).   
18. Jackson, M. A. et al. Proton pump inhibitors alter the composition of the gut microbiota. Gut 65, 749–756 (2016).   
19. Bufie, C. G. & Pamer, E. G. Microbiota-mediated colonization resistance against intestinal pathogens. Nat. Rev. Immunol. 13, 790–801 (2013).   
20. Cussotto, S. et al. Diferential efects of psychotropic drugs on microbiome composition and gastrointestinal function. Psychopharmacology 236, 1671–1685 (2019).   
21. Zhang, W., Qu, W., Wang, H. & Yan, H. Antidepressants fluoxetine and amitriptyline induce alterations in intestinal microbiota and gut microbiome function in rats exposed to chronic unpredictable mild stress. Transl. Psychiatry 11, 131 (2021).   
22. Fang, P., Kazmi, S. A., Jameson, K. G. & Hsiao, E. Y. The microbiome as a modifier of neurodegenerative disease risk. Cell Host Microbe 28, 201–222 (2020).   
23. Pratt, L. A., Brody, D. J. & Gu, Q. Antidepressant use among persons aged 12 and over: United States, 2011–2014. NCHS Data Brief (283), 1–8 (2017).

24. Myllylä, V. V., Sotaniemi, K. A., Illi, A., Suominen, K. & Keränen, T. Efect of entacapone, a COMT inhibitor, on the pharmacokinetics of levodopa and on cardiovascular responses in patients with Parkinson’s disease. Eur. J. Clin. Pharm. 45, 419–423 (1993).   
25. Schiele, B. C. Loxapine succinate: a controlled double-blind study in chronic schizophrenia. Dis. Nerv. Syst. 36, 361–364 (1975).   
26. Rome, B. N., Egilman, A. C., Patel, N. G. & Kesselheim, A. S. Using multiple authorized generics to maintain high prices: the example of entacapone. Value Health 26, 370–377 (2023).   
27. Vandeputte, D. et al. Quantitative microbiome profiling links gut community variation to microbial load. Nature 551, 507–511 (2017).   
28. Kopf, S. H. et al. Trace incorporation of heavy water reveals slow and heterogeneous pathogen growth rates in cystic fibrosis sputum. Proc. Natl Acad. Sci. USA 113, E110–E116 (2016).   
29. Berry, D. et al. Tracking heavy water (D O) incorporation for identifying and sorting active microbial cells. Proc. Natl Acad. Sci. USA 112, E194–E203 (2015).   
30. Hong, W. et al. Antibiotic susceptibility determination within one cell cycle at single-bacterium level by stimulated Raman metabolic imaging. Anal. Chem. 90, 3737–3743 (2018).   
31. Heuke, S. et al. Shot-noise limited tunable dual-vibrational frequency stimulated Raman scattering microscopy. Biomed. Opt. Express 12, 7780 (2021).   
32. Ge, X. et al. SRS-FISH: a high-throughput platform linking microbiome metabolism to identity at the single-cell level. Proc. Natl Acad. Sci. USA 119, e2203519119 (2022).   
33. Gasperotti, A., Brameyer, S., Fabiani, F. & Jung, K. Phenotypic heterogeneity of microbial populations under nutrient limitation. Curr. Opin. Biotechnol. 62, 160–167 (2020).   
34. Orama, M., Tilus, P., Taskinen, J. & Lotta, T. Iron(III)-chelating properties of the novel catechol O-methyltransferase inhibitor entacapone in aqueous solution. J. Pharm. Sci. 86, 827–831 (1997).   
35. Tosato, M. & Di Marco, V. Metal chelation therapy and Parkinson’s disease: a critical review on the thermodynamics of complex formation between relevant metal ions and promising or established drugs. Biomolecules 9, 269 (2019).   
36. Mayneris-Perxachs, J., Moreno-Navarrete, J. M. & Fernández-Real, J. M. The role of iron in host–microbiota crosstalk and its efects on systemic glucose metabolism. Nat. Rev. Endocrinol. 18, 683–698 (2022).   
37. Lund, E. K., Wharf, S. G., Fairweather-Tait, S. J. & Johnson, I. T. Oral ferrous sulfate supplements increase the free radical-generating capacity of feces from healthy volunteers. Am. J. Clin. Nutr. 69, 250–255 (1999).   
38. Dostal, A., Fehlbaum, S., Chassard, C., Zimmermann, M. B. & Lacroix, C. Low iron availability in continuous in vitro colonic fermentations induces strong dysbiosis of the child gut microbial consortium and a decrease in main metabolites. FEMS Microbiol. Ecol. 83, 161–175 (2013).   
39. Rocha, E. R., de Uzeda, M. & Brock, J. H. Efect of ferric and ferrous iron chelators on growth of Bacteroides fragilis under anaerobic conditions. FEMS Microbiol. Lett. 84, 45–50 (1991).   
40. Mitra, A. K. & Matthews, M. L. Efects of pH and phosphate on the oxidation of iron in aqueous solution. Int. J. Pharm. 23, 185–193 (1985).   
41. Ellermann, M. & Arthur, J. C. Siderophore-mediated iron acquisition and modulation of host-bacterial interactions. Free Radic. Biol. Med. 105, 68–78 (2017).   
42. Chaumeil, P.-A., Mussig, A. J., Hugenholtz, P. & Parks, D. H. GTDB-Tk: a toolkit to classify genomes with the Genome Taxonomy Database. Bioinformatics 36, 1925–1927 (2020).   
43. Yang, T. et al. Specificity and mechanism of TonB-dependent ferric catecholate uptake by Fiu. Front. Microbiol. 15, 1355253 (2024).

44. Loomis, L. D. & Raymond, K. N. Solution equilibria of enterobactin and metal-enterobactin complexes. Inorg. Chem. 30, 906–911 (1991).   
45. Bearden, S. W., Staggs, T. M. & Perry, R. D. An ABC transporter system of Yersinia pestis allows utilization of chelated iron by Escherichia coli SAB11. J. Bacteriol. 180, 1135–1147 (1998).   
46. Hall, A. B. et al. A novel Ruminococcus gnavus clade enriched in inflammatory bowel disease patients. Genome Med. 9, 103 (2017).   
47. Feldgarden, M. et al. AMRFinderPlus and the Reference Gene Catalog facilitate examination of the genomic links among antimicrobial resistance, stress response, and virulence. Sci. Rep. 11, 12728 (2021).   
48. Jacobs, A. & Miles, P. M. Intraluminal transport of iron from stomach to small-intestinal mucosa. Br. Med. J. 4, 778–781 (1969).   
49. Pi, H. et al. Role of catecholate siderophores in Gram-negative bacterial colonization of the mouse gut. PLoS ONE 7, e50020 (2012).   
50. Weis, S. et al. Efect of Parkinson’s disease and related medications on the composition of the fecal bacterial microbiota. npj Parkinsons Dis. 5, 28 (2019).   
51. Campbell, N. R. & Hasinof, B. Ferrous sulfate reduces levodopa bioavailability: chelation as a possible mechanism. Clin. Pharmacol. Ther. 45, 220–225 (1989).   
52. Comtan® (entacapone) Tablets: Prescribing Information (US) (Novartis Pharmaceuticals Corporation, 2011).   
53. Vehreschild, M. J. G. T. et al. An open randomized multicentre Phase 2 trial to assess the safety of DAV132 and its eficacy to protect gut microbiota diversity in hospitalized patients treated with fluoroquinolones. J. Antimicrob. Chemother. 77, 1155–1165 (2022).   
54. Keränen, T. et al. Inhibition of soluble catechol-O-methyltransferase and single-dose pharmacokinetics after oral and intravenous administration of entacapone. Eur. J. Clin. Pharm. 46, 151–157 (1994).   
55. Simpson, G. M., Cooper, T. B., Lee, J. H. & Young, M. A. Clinical and plasma level characteristics of intramuscular and oral loxapine. Psychopharmacology 56, 225–232 (1978).   
56. Luo, J. P. et al. In vitro identification of the human cytochrome p450 enzymes involved in the oxidative metabolism of loxapine. Biopharm. Drug Dispos. 32, 398–407 (2011).   
57. Stintzi, A., Barnes, C., Xu, J. & Raymond, K. N. Microbial iron transport via a siderophore shuttle: a membrane ion transport paradigm. Proc. Natl Acad. Sci. USA 97, 10691–10696 (2000).   
58. Pjevac, P. et al. An economical and flexible dual barcoding, two-step PCR approach for highly multiplexed amplicon sequencing. Front. Microbiol. 12, 669776 (2021).   
59. Parada, A. E., Needham, D. M. & Fuhrman, J. A. Every base matters: assessing small subunit rRNA primers for marine microbiomes with mock communities, time series and global field samples. Environ. Microbiol. 18, 1403–1414 (2016).   
60. Apprill, A., McNally, S., Parsons, R. & Weber, L. Minor revision to V4 region SSU rRNA 806R gene primer greatly increases detection of SAR11 bacterioplankton. Aquat. Microb. Ecol. 75, 129–137 (2015).   
61. Herbold, C. W. et al. A flexible and economical barcoding approach for highly multiplexed amplicon sequencing of diverse target genes. Front. Microbiol. 6, 731 (2015).   
62. Callahan, B. J. et al. DADA2: high-resolution sample inference from Illumina amplicon data. Nat. Methods 13, 581–583 (2016).   
63. Callahan, B. J., Sankaran, K., Fukuyama, J. A., McMurdie, P. J. & Holmes, S. P. Bioconductor workflow for microbiome data analysis: from raw reads to community analyses. F1000Research 5, 1492 (2016).   
64. Quast, C. et al. The SILVA ribosomal RNA gene database project: improved data processing and web-based tools. Nucleic Acids Res. 41, D590–D596 (2012).

65. McMurdie, P. J. & Holmes, S. phyloseq: an R package for reproducible interactive analysis and graphics of microbiome census data. PLoS ONE 8, e61217 (2013).   
66. Cole, J. R. et al. Ribosomal Database Project: data and tools for high throughput rRNA analysis. Nucleic Acids Res. 42, D633–D642 (2014).   
67. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biol. 15, 550 (2014).   
68. Martin, M. Cutadapt removes adapter sequences from high-throughput sequencing reads. EMBnet J. 17, 10–12 (2011).   
69. Li, H. Minimap2: pairwise alignment for nucleotide sequences. Bioinformatics 34, 3094–3100 (2018).   
70. Kolmogorov, M., Yuan, J., Lin, Y. & Pevzner, P. A. Assembly of long, error-prone reads using repeat graphs. Nat. Biotechnol. 37, 540–546 (2019).   
71. Vaser, R., Sović, I., Nagarajan, N. & Šikić, M. Fast and accurate de novo genome assembly from long uncorrected reads. Genome Res. 27, 737–746 (2017).   
72. Li, H. et al. The Sequence Alignment/Map format and SAMtools. Bioinformatics 25, 2078–2079 (2009).   
73. Kang, D. D. et al. MetaBAT 2: an adaptive binning algorithm for robust and eficient genome reconstruction from metagenome assemblies. PeerJ 7, e7359 (2019).   
74. Gurevich, A., Saveliev, V., Vyahhi, N. & Tesler, G. QUAST: quality assessment tool for genome assemblies. Bioinformatics 29, 1072–1075 (2013).   
75. Parks, D. H., Imelfort, M., Skennerton, C. T., Hugenholtz, P. & Tyson, G. W. CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes. Genome Res. 25, 1043–1055 (2015).   
76. Lowe, T. M. & Eddy, S. R. tRNAscan-SE: a program for improved detection of transfer RNA genes in genomic sequence. Nucleic Acids Res. 25, 955–964 (1997).   
77. Nawrocki, E. P. & Eddy, S. R. Infernal 1.1: 100-fold faster RNA homology searches. Bioinformatics 29, 2933–2935 (2013).   
78. Garber, A. I. et al. FeGenie: a comprehensive tool for the identification of iron genes and iron gene neighborhoods in genome and metagenome assemblies. Front. Microbiol. 11, 37 (2020).   
79. Ludwig, W. et al. ARB: a software environment for sequence data. Nucleic Acids Res. 32, 1363–1371 (2004).   
80. Minh, B. Q. et al. IQ-TREE 2: new models and eficient methods for phylogenetic inference in the genomic era. Mol. Biol. Evol. 37, 1530–1534 (2020).   
81. Wagner, M., Horn, M. & Daims, H. Fluorescence in situ hybridisation for the identification and characterisation of prokaryotes. Curr. Opin. Microbiol. 6, 302–309 (2003).   
82. Yilmaz, L. S., Parnerkar, S. & Noguera, D. R. mathFISH, a web tool that uses thermodynamics-based mathematical models for in silico evaluation of oligonucleotide probes for fluorescence in situ hybridization. Appl. Environ. Microbiol. 77, 1118–1122 (2011).   
83. Manz, W., Amann, R., Ludwig, W., Wagner, M. & Schleifer, K.-H. Phylogenetic oligodeoxynucleotide probes for the major subclasses of Proteobacteria: problems and solutions. Syst. Appl. Microbiol. 15, 593–600 (1992).   
84. Daims, H., Brühl, A., Amann, R., Schleifer, K. H. & Wagner, M. The domain-specific probe EUB338 is insuficient for the detection of all Bacteria: development and evaluation of a more comprehensive probe set. Syst. Appl. Microbiol. 22, 434–444 (1999).   
85. Poczatek, C., Kaufman, Z. & Lechene, C. OpenMIMS ImageJ Plugin Guide (Harvard Univ., 2012).   
86. Schindelin, J. et al. Fiji: an open-source platform for biologicalimage analysis. Nat. Methods 9, 676–682 (2012).

87. Stookey, L. L. Ferrozine–a new spectrophotometric reagent for iron. Anal. Chem. 42, 779–781 (1970).   
88. Altschul, S. F., Gish, W., Miller, W., Myers, E. W. & Lipman, D. J. Basic local alignment search tool. J. Mol. Biol. 215, 403–410 (1990).   
89. Varel, V. H. & Bryant, M. P. Nutritional features of Bacteroides fragilis subsp. fragilis. Appl. Microbiol. 28, 251–257 (1974).   
90. Southwell, J. W., Wilson, K. S., Thomas, G. H. & Duhme-Klair, A.-K. Enhancement of growth media for extreme iron limitation in Escherichia coli. Access Microbiol. 6, 000735.v4 (2024).   
91. Ge, X. The Parkinson's disease drug entacapone disrupts gut microbiome homeostasis via iron sequestration. Zenodo https://doi.org/10.5281/zenodo.14027024 (2024).

# Acknowledgements

The research reported in this manuscript was funded by NIH Awards R35GM136223 (to J.-X.C.), R01EB032391 and R01AI141439 (to J.-X.C.) and supported by the Boston University Micro and Nano Imaging Facility and the Ofice of the Director, NIH Award S10OD024993. The content is solely the responsibility of the authors and does not necessarily represent the oficial views of the NIH. Funding for the presented research was also provided via the Young Independent Research Group Grant ZK-57 (to F.C.P.) of the Austrian Science Fund (FWF) and the FWF-Wittgensteinaward Z383-B (to M.W.), as well as the Austrian Science Fund (FWF)-funded Cluster of Excellence ‘Microbiomes drive Planetary Health’ (10.55776; COE 7; D.B., T.B., M.W.). The project was also supported by pilot funding from the Institute for Life Sciences, University of Southampton. We thank J. Schwarz, G. Kohl, P. Pjevac and J. S. Silva from the Joint Microbiome Facility of the Medical University of Vienna and the University of Vienna for assisting with amplicon and metagenomic sequencing, as well as repositing of sequencing data. We thank L. Guantai for assistance in setting up drug incubations.

# Author contributions

F.C.P., X.G., J.-X.C. and M.W. designed the study. F.C.P, X.G., J.M.K., K.M., J.B.S., D. Seki and M.D. performed the experiments with input from T.B., Y.Z., D.B. and A.S. F.C.P, J.M.K., R.H.K, B.H. and K.W. analysed sequencing data and performed bioinformatic analysis. A.S. and S.I. conducted NanoSIMS analysis and D. Szamosvari investigated iron binding and redox states. F.C.P. and X.G. wrote the manuscript with input from all co-authors, and all authors read and approved the final manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41564-024-01853-0.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41564-024-01853-0.

Correspondence and requests for materials should be addressed to Fátima C. Pereira, Ji-Xin Cheng or Michael Wagner.

Peer review information Nature Microbiology thanks Lisa Maier and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons. org/licenses/by/4.0/.

© Crown 2024

1 Centre for Microbiology and Environmental Systems Science, Department of Microbiology and Ecosystem Science, University of Vienna, Vienna, Austria. 2 School of Biological Sciences, University of Southampton, Southampton, UK. 3 Department of Electrical and Computer Engineering, Boston University, Boston, MA, USA. 4 Joint Microbiome Facility of the Medical University of Vienna and the University of Vienna, Vienna, Austria. 5 Department of Biological Chemistry, Faculty of Chemistry, University of Vienna, Vienna, Austria. 6 Department of Chemistry, Boston University, Boston, MA, USA. 7 Department of Laboratory Medicine, Medical University of Vienna, Vienna, Austria. 8 Department of Biomedical Engineering, Photonics Center, Boston University, Boston, MA, USA. 9 Department of Chemistry and Bioscience, Aalborg University, Aalborg, Denmark. 10Present address: School of Biological Sciences, University of Portsmouth, Portsmouth, UK. 11These authors contributed equally: Fátima C. Pereira, Xiaowei Ge.  e-mail: f.c.pereira@soton.ac.uk; jxcheng@bu.edu; michael.wagner@univie.ac.at

a   
![](images/4857addef60b8e19e109d95d448e3f237557fc04671dea1439c2993c9a1643a1.jpg)

<details>
<summary>scatter</summary>

| Time | Drug        | Axis 1 | Axis 2 |
|------|-------------|--------|--------|
| 6    | H₂O control | -0.05  | -0.12  |
| 6    | No drug     | -0.03  | -0.08  |
| 6    | ENT-Low     | -0.02  | -0.05  |
| 6    | ENT-Hi      | 0.35   | -0.05  |
| 6    | LOX-Low     | -0.01  | -0.03  |
| 6    | LOX-Hi      | -0.01  | -0.02  |
| 24   | H₂O control | -0.04  | -0.11  |
| 24   | No drug     | -0.02  | -0.07  |
| 24   | ENT-Low     | -0.01  | -0.04  |
| 24   | ENT-Hi      | 0.38   | -0.03  |
| 24   | LOX-Low     | -0.01  | -0.02  |
| 24   | LOX-Hi      | -0.01  | -0.01  |
</details>

b   
![](images/0c0d5107b56ca37193fab40045ac1465d5d8bdf8f5491fc35dc4957ec4144819.jpg)

<details>
<summary>boxplot</summary>

| Group | Observed Alpha diversity measure | Shannon Alpha diversity measure | Inv Simpson Alpha diversity measure |
|-------|-----------------------------------|----------------------------------|-------------------------------------|
| H₂O control | ~230–270 | ~4.15–4.30 | ~32 |
| No drug | ~230–260 | ~4.10–4.25 | ~30 |
| ENT-Low | ~230–250 | ~3.80–4.25 | ~30 |
| ENT-Hi | ~250–310 | ~3.75–4.10 | ~38 |
| LOX-Low | ~250–275 | ~3.75–4.25 | ~34 |
| LOX-Hi | ~250–260 | ~3.75–4.10 | ~38 |
</details>

C   
![](images/e6fa8c680917e31fb2c98e1793fdf3b0c0fb8016eef8849776b044542d4f5a2c.jpg)

<details>
<summary>scatter</summary>

| Time     | Drug        | Axis 1 [46.8%] | Axis 2 [23%] |
| -------- | ----------- | -------------- | ------------ |
| 6 hours  | H₂O control | -0.05          | -0.08        |
| 6 hours  | No drug     | 0.02           | -0.09        |
| 6 hours  | ENT-Low     | 0.03           | -0.07        |
| 6 hours  | ENT-Hi      | 0.25           | 0.18         |
| 6 hours  | LOX-Low     | 0.04           | -0.08        |
| 6 hours  | LOX-Hi      | 0.05           | -0.09        |
| 24 hours | H₂O control | -0.15          | 0.05         |
| 24 hours | No drug     | -0.12          | 0.08         |
| 24 hours | ENT-Low     | -0.18          | 0.03         |
| 24 hours | ENT-Hi      | 0.28           | 0.12         |
| 24 hours | LOX-Low     | 0.06           | -0.07        |
| 24 hours | LOX-Hi      | 0.07           | -0.08        |
</details>

d   
![](images/a4f5b5c1a079fcc18f67dd0d6852f7551134096a3db7d8c50f283bd17bc9d270.jpg)

<details>
<summary>boxplot</summary>

| Group       | Observed Alpha diversity measure | Shannon Alpha diversity measure | Inv Simpson Alpha diversity measure |
|-------------|-----------------------------------|----------------------------------|-------------------------------------|
| H₂O control | ~280                              | ~3.5                             | ~12                                 |
| No drug     | ~260                              | ~3.4                             | ~11                                 |
| ENT-Low     | ~270                              | ~3.6                             | ~12                                 |
| ENT-Hi      | ~250                              | ~3.0                             | ~7                                  |
| LOX-Low     | ~285                              | ~3.7                             | ~10                                 |
| LOX-Hi      | ~275                              | ~3.8                             | ~13                                 |
</details>

e   
![](images/d7cdeeea17df025a6e19fbfa51c6fcee55ac7b0da497eb70c7b7d660d4393b01.jpg)

<details>
<summary>line</summary>

| Time (h) | H₂O control | ENT-Low | LOX-Low | No drug | ENT-Hi | LOX-Hi |
| -------- | ----------- | ------- | ------- | ------- | ------ | ------ |
| 0        | 8.0         | 8.0     | 8.0     | 8.0     | 8.0    | 8.0    |
| 5        | 8.6         | 8.6     | 8.6     | 8.6     | 8.3    | 8.5    |
| 25       | 9.2         | 9.2     | 9.2     | 9.2     | 9.1    | 9.2    |
</details>

![](images/871dc9802251b56eb52ced795a474294016256962fa84215b90f75470ae2cd94.jpg)

<details>
<summary>bar_stacked</summary>

| Genus | t0 | t06 | t24 |
| --- | --- | --- | --- |
| [Eubacterium] hallii group | 0.15 | 0.35 | 0.35 |
| Alistipes | 0.05 | 0.25 | 0.25 |
| Akkermansia | 0.10 | 0.20 | 0.20 |
| Anaerostipes | 0.05 | 0.15 | 0.15 |
| Bacteroides | 0.05 | 0.15 | 0.15 |
| Bifidobacterium | 0.05 | 0.15 | 0.15 |
| Blautia | 0.10 | 0.25 | 0.25 |
| Collinsella | 0.15 | 0.25 | 0.25 |
| Coprococcus | 0.10 | 0.20 | 0.20 |
| Escherichia-Shigella | 0.15 | 0.25 | 0.25 |
| Faecalibacterium | 0.15 | 0.20 | 0.20 |
| Gastranaerophilales un | 0.10 | 0.15 | 0.15 |
| Holdemanella | 0.10 | 0.15 | 0.15 |
| Lachnoclostridium | 0.15 | 0.25 | 0.25 |
</details>

g   
![](images/0675ff6da31cc180ead3d7e0b82bfbee77e46a6446fe071d406b1157454b4cbe.jpg)

<details>
<summary>bar_stacked</summary>

| Group | t0 | t06 | t24 |
|-------|----|-----|-----|
| Inoculum | 0.0 | 0.3 | 0.1 |
| H₂O control | 0.1 | 0.3 | 0.8 |
| No drug | 0.1 | 0.3 | 0.7 |
| ENT-Low | 0.1 | 0.3 | 0.6 |
| ENT-Hi | 0.1 | 0.1 | 0.4 |
| LOX-Low | 0.1 | 0.3 | 0.5 |
| LOX-Hi | 0.1 | 0.3 | 0.5 |
| Lachnospiraceae unclass | 0.1 | 0.3 | 0.5 |
| Other | 0.1 | 0.3 | 0.5 |
| Prevotella 9 | 0.1 | 0.1 | 0.1 |
| Ruminococcus | 0.1 | 0.1 | 0.1 |
| Senegalimassilia | 0.1 | 0.1 | 0.1 |
| Streptococcus | 0.1 | 0.1 | 0.1 |
| Sutterella | 0.1 | 0.1 | 0.1 |
| Tyzzerella | 0.1 | 0.1 | 0.1 |
| Subdoligranulum | 0.1 | 0.1 | 0.1 |
| UCG-002 | 0.1 | 0.1 | 0.1 |
| UCG-005 | 0.1 | 0.1 | 0.1 |
| uncultured unclass | 0.1 | 0.1 | 0.1 |
</details>

Extended Data Fig. 1 | See next page for caption.

Extended Data Fig. 1 | Relative and absolute abundance profiles of faecal samples resuspended in sM9 or BHI and incubated with drugs. a. Ordination plot of Bray–Curtis distances of microbial communities (ASV-level composition) in faecal samples resuspended in sM9 medium (a) or BHI medium (c) and incubated in the presence of drugs (n = 3 incubation vials per condition). Samples are coloured according to the drug amended and shaped according to the time of incubation. Please note that in (a) at T6 ENT-Hi condition two of the data points show overlapping positions in the ordination plot. sM9 medium: PERMANOVA = 0.001, R2  = 0.64. BHI medium: PERMANOVA = 0.001, R2  = 0.45. b. Alpha diversity metrics (number of Observed ASVs, Shannon Index, and Inverse Simpson Index) of faecal samples resuspended in sM9 medium (b) or BHI medium (d) and incubated in the presence of drugs. Each data point represents a replicate and samples from both 6 and 24 h of incubation are shown. Significant differences (p-values) determined by two-sided Wilcoxon testing are indicated,

with “No drug” used as a reference group. Boxes represent the median, first and third quartile. Whiskers extend to the highest and lowest values that are within one and a half times the interquartile range. e. Total cell loads in faecal samples resuspended in BHI medium and incubated with drugs, as assessed by flow cytometry (Supplementary Table 1). \*\*p = 0.002; unpaired two-sided t-test with “No drug” used as a reference group. Data points represent the mean value +/- SEM from three incubation vials per condition. f, g. Relative (f) and absolute (g) genus abundance profiles of microbial communities originating from faecal samples resuspended in BHI medium and incubated in the presence of drugs at T0 and after 6 or 24 h of incubation. Each bar represents the mean from triplicate incubations. All genera present at relative abundances below 0.025 or absolute abundances below 2.5x107 cells.ml−1 were assigned into the category “Other” (“unclass”: unclassified). Complete relative and absolute abundance profiles can be found in Supplementary Tables 3 and 4.

![](images/846bdaf38709a9827c2fc0b9c812c762a4f212533a76c7909991d253eff530d1.jpg)

<details>
<summary>line</summary>

| Donor | Incubation | Time (h) | Cells.ml⁻¹ (log₁₀) |
|-------|------------|----------|---------------------|
| Donor 1 | No drug   | 0        | 7.9                 |
| Donor 1 | No drug   | 25       | 8.7                 |
| Donor 1 | ENT-Hi    | 0        | 7.9                 |
| Donor 1 | ENT-Hi    | 5        | 7.8                 |
| Donor 1 | ENT-Hi    | 25       | 8.4                 |
| Donor 2 | No drug   | 0        | 7.9                 |
| Donor 2 | No drug   | 5        | 8.2                 |
| Donor 2 | No drug   | 25       | 8.6                 |
| Donor 2 | ENT-Hi    | 0        | 7.9                 |
| Donor 2 | ENT-Hi    | 5        | 7.8                 |
| Donor 2 | ENT-Hi    | 25       | 8.3                 |
| Donor 3 | No drug   | 0        | 7.9                 |
| Donor 3 | No drug   | 5        | 8.3                 |
| Donor 3 | No drug   | 25       | 8.7                 |
| Donor 3 | ENT-Hi    | 0        | 7.9                 |
| Donor 3 | ENT-Hi    | 5        | 7.8                 |
| Donor 3 | ENT-Hi    | 25       | 8.2                 |
</details>

![](images/a9003ef552dc89b4ba30d39006c4377edc63d927abead06e0653fa19501410c4.jpg)

<details>
<summary>bar_stacked</summary>

| Time Point | Group   | No drug | ENT-Hi | No drug |
| ---------- | ------- | ------- | ------ | ------- |
| t0         | D1      | 0.05    | 0.10   | 0.05    |
| t0         | D2      | 0.05    | 0.10   | 0.05    |
| t0         | D3      | 0.05    | 0.10   | 0.05    |
| 6 hours    | D1      | 0.10    | 0.15   | 0.05    |
| 6 hours    | D2      | 0.10    | 0.15   | 0.05    |
| 6 hours    | D3      | 0.10    | 0.15   | 0.05    |
| 24 hours   | D1      | 0.15    | 0.20   | 0.05    |
| 24 hours   | D2      | 0.15    | 0.20   | 0.05    |
| 24 hours   | D3      | 0.15    | 0.20   | 0.05    |
</details>

![](images/c2a20eb8a8d534d8897636d7eec2367c194876cb650da3a173d67f099a79620c.jpg)

<details>
<summary>bar_stacked</summary>

| Genus | Time Point | D1 | D2 | D3 |
| --- | --- | --- | --- | --- |
| Agathobacter | t0 | 0.8 | 0.1 | 0.7 |
| Alloprevotella | t0 | 0.9 | 0.1 | 0.8 |
| Alistipes | t0 | 0.7 | 0.1 | 0.5 |
| Bacteroides | t0 | 1.3 | 0.2 | 0.8 |
| Other | t0 | 0.6 | 0.1 | 0.4 |
| Blautia | t0 | 0.7 | 0.1 | 0.5 |
| Parabacteroides | t0 | 0.1 | 0.1 | 0.1 |
| Bifidobacterium | t0 | 0.1 | 0.1 | 0.1 |
| Citrobacter | t0 | 0.1 | 0.1 | 0.1 |
| Catenibacterium | t0 | 0.1 | 0.1 | 0.1 |
| Enterobacteriaceae_unclassified | t0 | 0.1 | 0.1 | 0.1 |
| Erysipelotrichaceae UCG-003 | t0 | 0.1 | 0.1 | 0.1 |
| Escherichia-Shigella | t0 | 0.1 | 0.1 | 0.1 |
| Faecalibacterium | t0 | 0.1 | 0.1 | 0.1 |
| Fusicatenibacter | t0 | 0.1 | 0.1 | 0.1 |
| Holdemanella | t0 | 0.1 | 0.1 | 0.1 |
| Lachnospiraceae_unclassified | t0 | 0.1 | 0.1 | 0.1 |
| Agathobacter | 24 hours | 0.2 | 0.1 | 4.2 |
| Alloprevotella | 24 hours | 0.2 | 0.1 | 4.2 |
| Alistipes | 24 hours | 0.2 | 0.1 | 4.2 |
| Bacteroides | 24 hours | 0.2 | 0.1 | 4.2 |
| Other | 24 hours | 0.2 | 0.1 | 4.2 |
| Blautia | 24 hours | 0.2 | 0.1 | 4.2 |
| Parabacteroides | 24 hours | 0.2 | 0.1 | 4.2 |
| Bifidobacterium | 24 hours | 0.2 | 0.1 | 4.2 |
| Citrobacter | 24 hours | 0.2 | 0.1 | 4.2 |
| Catenibacterium | 24 hours | 0.2 | 0.1 | 4.2 |
| Enterobacteriaceae_unclassified | 24 hours | 0.2 | 0.1 | 4.2 |
| Erysipelotrichaceae UCG-003 | 24 hours | 0.2 | 0.1 | 4.2 |
| Escherichia-Shigella | 24 hours | 0.2 | 0.1 | 4.2 |
| Faecalibacterium | 24 hours | 0.2 | 0.1 | 4.2 |
| Fusicatenibacter | 24 hours | 0.2 | 0.1 | 4.2 |
| Holdemanella | 24 hours | 0.2 | 0.1 | 4.2 |
| Lachnospiraceae_unclassified | 24 hours | 0.2 | 0.1 | 4.2 |
| Agathobacter (Lachnospiraceae NK4A136 group) - No drug, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-HI, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-HH, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hii, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hi, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hii, ENT-Hiii, ENT-Bronella-3999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999988888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888886666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666<fcel>Genus
Genus (Lachnospiraceae NK4A136 group)
Lachnospiraceae NK4A136 group
Lachnoclostridium
Megasphaera
Other
Parabacteroides
Paraprevotella
Prevotella_9
Ruminococcus
Prevotella
Subdoligranulum
Streptococcus
Sutterella
Succinivibrio
UCG-003
uncultured
</details>

Extended Data Fig. 2 | Relative and absolute abundance profiles of individual faecal samples incubated with entacapone. a. Total microbial cell loads in incubations of samples from three different donors (compared to samples used in main text, for example, Fig. 1) with entacapone (ENT-Hi) and controls (No drug - DMSO only), at the start of the incubation (time=0 h, t0) and after 6 and 24 h in sM9 medium. Total cell loads were assessed by flow cytometry. Indicated P values are from an unpaired two-sided t-test with “No drug” as a reference group. Data points represent the mean value +/- SEM from three incubation   
vials per condition. b, c. Relative (b) and absolute (c) genus abundance profiles of faecal microbial communities (Donor 1: D1, Donor 2: D2 and Donor 3: D3) incubated with ENT-Hi and assessed by 16S rRNA gene amplicon sequencing. The community composition at 0 h (inoculum) is also shown. All genera present at a relative abundance below 0.025 or absolute abundance below 5x106 cells. ml-1 were assigned to the category “Other”. Each bar represents the mean from triplicate incubations.

![](images/35deb72f2ec80490f0e5baaeba7d02a03dd23397ad5ce8dcbc4fc1c9c9a8a6d3.jpg)

![](images/d1cecba6a8e019a60758422365a55f8574d62b47aa577ab6f0cb0493a281f215.jpg)

<details>
<summary>text_image</summary>

b
Virtual state
ħωp
ħωs
v=1
Ground state
v=0
Ω
</details>

![](images/7157d15bb9c3ec7644d9e4fa7492136241f1d64541224ecfa9ed966b39536d65.jpg)

<details>
<summary>line</summary>

| t    | ω (Ω₁) | ω (Ω₂) |
| ---- | ------ | ------ |
| 0    | Low    | Low    |
| T₀   | High   | High   |
</details>

Extended Data Fig. 3 | Pump probe microscopy combined with widefield fluorescence imaging for correlative chemical and fluorescence in situ hybridization imaging. a. Experimental setup. Left dashed box: laser point scanning mode for SRS/PT. DL: delay line; HWP: half waveplate; PBS: polarized beam splitter; AOM: acousto-optic modulator; DM: dichroic mirror; SM: scanning unit; FM: flip mirror; OBJ: objective; COND: condenser; SP: short pass filter;   
PD: photodiode; RA: resonant amplifier; Ex: excitation filter; Em: emission filter; TL: tube lens. b. Stimulated Raman scattering energy diagram. $\omega _ { p } \mathrm { : }$ : pump beam frequency; $\omega _ { S } \mathrm { : }$ Stokes beam frequency; ℏ: Planck’s constant; Ω: energy of the vibrational mode; v: vibrational level. c. Picosecond stimulated Raman scattering by spectral focusing.

a   
![](images/6ea731bdc35eb9288290a49459ff9aefc72fbf3eb43d61c58c56500d20a157c1.jpg)

<details>
<summary>text_image</summary>

SRS C-D
SRS C-H
SRS off-res
picosecond
femtosecond
10 µm
</details>

b

![](images/d137a60da878f579491d8909b7cd2361ad40fdb25b0332fed0de2cb3af3daef2.jpg)

<details>
<summary>text_image</summary>

Picosecond SRS
Vibrational peak
XPM
Femtosecond SRS
</details>

Extended Data Fig. 4 | Sensitive mapping of microbial activity by picosecond SRS. a. Picosecond SRS alleviates cross-phase modulation (XPM) and provides higher sensitivity for measuring the activity of microbial cells via deuterium incorporation with a laser power below the cell-damaging threshold. Picosecond SRS pump power: 30 mW, Stokes power: 120 mW. Femtosecond SRS: pump power: 15 mW, Stokes power: 70 mW. We reproducibly detected analogous   
differences when measuring at least one additional batch of samples. b. Picosecond and femtosecond SRS probing difference in the spectral domain. For picosecond SRS, the targeting bandwidth is 20 cm−1, which is much narrower than the femtosecond SRS which covers more than 200 cm−1. Thus, the ratio between the signal (vibrational feature) and the background (cross phase modulation, XPM) is improved in picosecond SRS.

![](images/688910d78879c715860a8bde93fd6df70a6c9cec42f057f7b3675e98a1dfef7c.jpg)

<details>
<summary>bubble</summary>

| Species | ENT-Low | LOX-Low | LOX-Hi |
| --- | --- | --- | --- |
| Escherichia coli | -1.5 | 0.5 | 1.2 |
| Streptococcus spp. | -1.0 | 0.8 | -0.5 |
| Clostridium sp900539375 | -2.0 | 1.0 | 2.5 |
| Bacteroides uniformis | -0.5 | 0.6 | 1.5 |
| Ruminococcus bromii | -0.3 | 0.4 | 0.2 |
| Phocaecicola dorei | -1.2 | 1.8 | 2.8 |
</details>

Extended Data Fig. 5 | Change in abundance of key taxa at 24 h of incubation.   
Bubble plot denoting the fold change in absolute abundances for the taxa targeted by FISH and incubated with drugs relative to “No drug” incubations,   
as determined by DeSeq2, at 24 h of incubation in sM9. Original data is from triplicates per condition. P values were attained using the Wald test and corrected for multiple testing using the Benjamini and Hochberg method.

a   
![](images/fc0e30dfe70a45120092ee0c0ce85bfbe758cb09264706173178b8e9ca5139ad.jpg)

<details>
<summary>line</summary>

| Wavelength (nm) | Optical density |
| --------------- | --------------- |
| 397             | 0.28            |
</details>

b   
![](images/73e2e19a719781bbc89b511fb791d339ea1a187f2c55a45cef1917f834455cce.jpg)

<details>
<summary>line</summary>

| Time (μs) | SRS/XPM | Photothermal |
| --------- | ------- | ------------ |
| 0.0       | High    | Low          |
| 0.2       | High    | Peak         |
| 0.4       | High    | Low          |
| 0.6       | High    | Peak         |
| 0.8       | High    | Low          |
| 1.0       | High    | Peak         |
| 1.2       | High    | Low          |
</details>

![](images/c0800203a721d1304de4d3f62a72843911b98776236b28be6557dd3150182295.jpg)

<details>
<summary>text_image</summary>

Y channel
Increasing photothermal decay time
X channel
</details>

d   
![](images/a515065db6d8aa57bfdf96eb397caaefebfbda1dec661b8b31ca130c2eee0457.jpg)

<details>
<summary>line</summary>

| Delay time (ps) | y channel | x channel |
| --------------- | --------- | --------- |
| -1.5            | 0.5       | 0.05      |
| -1.0            | 0.48      | 0.1       |
| -0.5            | 0.5       | 0.18      |
| 0.0             | 0.52      | 0.2       |
| 0.5             | 0.51      | 0.18      |
| 1.0             | 0.5       | 0.1       |
| 1.5             | 0.49      | 0.02      |
</details>

Extended Data Fig. 6 | Entacapone photothermal signal retrieved from modulation transfer detection. a. 10 mM Entacapone DMSO solution (under acidic pH conditions) measured by UV-VIS spectroscopy. b. Photothermal signal time trace exhibits a π/2 phase delay relative to the intensity modulation by the AOM and instantaneous signals, such as SRS and XPM. c. Pump probe signal phase upon increasing photothermal decay time. d. Entacapone accumulation   
in microbiota cells via pump probe detection with delay in time and x/y channel lock-in amplifier signal detection. As photothermal is not sensitive to picosecond level delay, the y channel showed a constant strong photothermal signal from the drug, while in the x-channel, the instantaneous cross phase modulation background showed up as a cross-correlation profile of two the pump and probe laser beams.

![](images/fce7a4bd383a5bbe81a0266a9a24cffb34dc2f3808d012df0d409899b7f47839.jpg)

<details>
<summary>line</summary>

| Time (s) | Intensity (arb. unit) |
| -------- | --------------------- |
| 0        | 0.3                   |
| 100      | 0.2                   |
| 200      | 0.15                  |
| 300      | 0.1                   |
| 400      | 0.07                  |
| 500      | 0.05                  |
| 600      | 0.04                  |
| 700      | 0.03                  |
</details>

![](images/8bba049fbb776e60b6de88828b2cc53cb8a4e4597b0c77d980caf8a4467b6d91.jpg)

<details>
<summary>line</summary>

| Time (s) | Intensity (arb. unit) |
| -------- | --------------------- |
| 0        | 0.25                  |
| 100      | ~0.23                 |
| 200      | ~0.22                 |
| 300      | ~0.21                 |
| 400      | ~0.20                 |
| 500      | ~0.20                 |
| 600      | ~0.20                 |
| 700      | ~0.20                 |
</details>

![](images/1aadddd237c6b2ffc15baaa66e7dd6defa219e5023ef038e283d842d4217f5dd.jpg)

<details>
<summary>scatter</summary>

| Time (s) | Intensity (arb. unit) |
| -------- | --------------------- |
| 0        | 0.65                  |
| 100      | 0.65                  |
| 200      | 0.65                  |
| 300      | 0.65                  |
| 400      | 0.65                  |
| 500      | 0.65                  |
| 600      | 0.65                  |
| 700      | 0.65                  |
</details>

Extended Data Fig. 7 | Recorded signal intensity of the lock-in amplifier x and y channels over time in faecal samples subjected to continuous bleaching of the entacapone photothermal signal. a. Signal intensity of the lock-in amplifier y channel (corresponding to photothermal signal) in samples incubated with ENT-HI and $\mathrm { { D } } _ { 2 } \mathrm { { O } } .$ b. Signal intensity of the x channel (corresponding to SRS signal   
and its background) in samples incubated with ENT-HI and $\mathsf { D } _ { 2 } \mathbf { O } . \mathbf { \mathsf { c } }$ . Signal intensity of the SRS x channel (corresponding to SRS signal and its background) in samples incubated with no drug, but with $\mathrm { D } _ { 2 } \mathrm { O } .$ Each dot represents the average signal intensity of 20 microbiota cells.

a   
![](images/9c776b70d23bbad524fda872647e43a8ac0dc20f1e07fb346855bf24d804b374.jpg)

<details>
<summary>text_image</summary>

Trans
FISH
PT in Pdor
PT
SRS-C-H
</details>

C   
![](images/6667e6e4650fe0cd3a7ea337b7b4eec400be1e87df7e4a9ea98694793260f870.jpg)

<details>
<summary>scatter</summary>

| Group   | Timepoint | Intensity (arbitrary units) |
|---------|-----------|------------------------------|
| T24     | No drug   | ~0.0                         |
| T24     | ENT-Hi    | ~0.1                         |
| T48     | No drug   | ~0.0                         |
| T48     | ENT-Hi    | ~0.2                         |
</details>

b   
![](images/78b2aab86598e893a97d8e84dd65e68d0d61d956b54011b4c4ea6175bb25d586.jpg)

<details>
<summary>text_image</summary>

T24
T48
No drug	ENT-Hi	No drug	ENT-Hi
PT
SRS C-H
PT
SRS C-H
</details>

d   
![](images/ca45baaa849dc909c0431de585a834fd04900a1040ed7af67f3dacddf848991e.jpg)

<details>
<summary>line</summary>

| Time (hours) | No drug | ENT-Hi |
| ------------ | ------- | ------ |
| 0            | 7.4     | 7.4    |
| 25           | 9.4     | 7.3    |
| 50           | 9.3     | 7.2    |
</details>

e   
![](images/1b101845bafd5289d14d3b2d2f105e6ecbe21d610995e65e85fb3d64d4b4df97.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images showing green-labeled PT and red-labeled SRSCH channels (no text or symbols present)
</details>

![](images/452d77c22fb3e3446fd42a0d5a33c0a9e92d18e35c294aa6f7d9039ac4337679.jpg)

<details>
<summary>scatter</summary>

| Group       | PT intensity (arbitrary units) |
| ----------- | ------------------------------ |
| No drug     | ~0                             |
| ENT-Hi:Fe   | ~0.5                           |
</details>

Extended Data Fig. 8 | Photothermal imaging of entacapone accumulation by Phocaeicola dorei and faecal samples. a. All columns show representative images of faecal samples incubated with ENT-Hi for 6 h followed by hybridization with a fluorescently-labelled oligonucleotide probe targeting Phocaeicola dorei (Pdor) (Supplementary Table 10). Top panel: fluorescence signals from hybridized cells (FISH). Middle panel: Photothermal signal intensity from entacapone (PT) in Pdor cells only (PT signals of other cells were removed to enhance clarity). Bottom panel: PT signals overlayed with the SRS C-H signals. PT channel contrast: min 0 max 1.8. C-H channel is represented on a log scale. We reproducibly detected analogous differences when measuring at least one additional batch of samples. b. Representative images of a pure culture of Phocaeicola dorei incubated anaerobically with entacapone for 24 or 48 h. Photothermal signal from entacapone (PT) in P. dorei cells is shown in the top panel, SRS C-H signal in the middle panel, and an overlay of both signals is   
shown in the bottom panel. c. Single-cell specific photothermal signal intensity detected in samples shown in b. p-values were determined by the unpaired two sided t-test comparing the groups “Ent-Hi:Fe” and “No drug”. d. Growth (assessed by microbial cell counts) of P. dorei in the presence or absence of entacapone. Data points represent the mean abundance values +/- SEM of three independent growths per condition. e. Accumulation of entacapone pre-complexed with Fe(III) by faecal samples anaerobically incubated for 6 h with ENT-Hi precomplexed with FeSO (ENT-Hi:Fe). Photothermal signal from entacapone (PT) is shown on top and the overlay with the SRS C-H biomass signal is shown in the bottom panel. f. Single-cell specific photothermal signal intensity in samples shown in e. p-value was determined with the unpaired two-sided Wilcoxon test comparing the groups “Ent-Hi:Fe” and “No drug”. In c and f, boxes represent median, first, and third quartile. Whiskers extend to the highest and lowest values that are within one and a half times the interquartile range.

![](images/fb84eab17e5772f95c45d97e464daffad80f57a0a94f66f6a2bf526e1e8d3eb9.jpg)

<details>
<summary>line</summary>

| [Chelator] µM | EDTA | Entacapone |
| ------------- | ---- | ---------- |
| 0             | 5    | 2          |
| 25            | 60   | 1          |
| 50            | 100  | 1          |
| 100           | 100  | 3          |
| 250           | 100  | 5          |
| 500           | 100  | 8          |
</details>

![](images/c5f81b6864ba37fbaee60a057e5c23e54c9909617624cd0ad666a189b97922a1.jpg)

<details>
<summary>line</summary>

| [Ferrozine] µM | water | DMSO |
| -------------- | ----- | ---- |
| 0              | 0.05  | 0.07 |
| 25             | 0.12  | 0.09 |
| 50             | 0.22  | 0.11 |
| 100            | 0.31  | 0.11 |
| 150            | 0.40  | 0.11 |
| 200            | 0.48  | 0.11 |
</details>

![](images/f996805c21381da5dd88540fd40707adc057c2add928cb66d26f1ee225ace606.jpg)

<details>
<summary>bar</summary>

| Time (min) | M9    | water |
| ---------- | ----- | ----- |
| 0          | 0.55  | 0.95  |
| 1          | 0.02  | 0.94  |
| 5          | 0.01  | 0.93  |
| 10         | 0.01  | 0.92  |
| 15         | 0.01  | 0.92  |
| 30         | 0.01  | 0.93  |
</details>

Extended Data Fig. 9 | Determination of Fe(II) concentrations by spectrophotometric measurements of the Fe(II)–ferrozine complex. The ferrozine reagent reacts with divalent Fe to form a stable magenta complex species with a maximum absorbance at 562 nm. a. Percentage of total Fe(II) in anaerobic solutions of FeSO containing increasing concentrations of Na H EDTA (a known Fe(II) chelator) or entacapone, as determined using the ferrozine method. b. Absorbance at 562 nm, indicating the presence of ferrozine-Fe(II) complexes in solutions of FeSO in degassed DMSO (100%) or degassed double distilled water, following reaction with increasing concentrations of ferrozine.   
c. Fe(II) concentrations in water or sM9 solutions of FeSO (1 mM FeSO ). FeSO was dissolved in degassed water or sM9 and incubated for 0, 1, 5, 10, 15 and 30 min, as indicated, before the ferrozine reagent was added. Concentrations of Fe(II) were determined using a calibration curve obtained by measuring absorbance at 562 nm in solutions of known Fe(II) concentration (see Methods) supplemented with 2 mM ferrozine. In a,b,c error bars denote standard deviation from triplicates per condition. Data are presented as mean values from three independent experiments +/- SD.

a   
![](images/6ce742ebab6629080612463a6930a578b6e3f8927298d7ea46fa5a9858e676fa.jpg)

<details>
<summary>scatter</summary>

| Syto9-Alexa488*-A | FSC-A |
| ----------------- | ----- |
| 10^2              | 10^3  |
| 10^3              | 10^4  |
| 10^4              | 10^5  |
| 10^5              | 10^5  |
</details>

b   
![](images/8f7d53c17ad37bebbc6b00c628e9ed347682b71ce9f023b338ff9081e37fa4ff.jpg)

<details>
<summary>scatter</summary>

| CountBright-Cy5*-A | FSC-H (x10³) |
| ------------------ | ------------ |
| 10²                | ~200         |
| 10³                | ~100         |
| 10⁴                | ~0           |
| 10⁵                | ~250         |
</details>

![](images/9ac1ddcfaacd9e775737e9e825e287426260b8c78a99078501a8b8b7e9df78ad.jpg)

<details>
<summary>scatter</summary>

| Syto9-Alexa488*-A | FSC-A |
| ----------------- | ----- |
| 10^5              | 10^5  |
</details>

![](images/f66beebaaf8090d7067aa49bfb679b067e65fc7a6f23923374e917bcfd26ac13.jpg)

<details>
<summary>scatter</summary>

| CountBright-Cy5*-A | FSC-H (x10³) |
| ------------------ | ------------ |
| 10²                | ~200         |
| 10⁴                | ~100         |
| 10⁵                | ~50          |
</details>

Extended Data Fig. 10 | Flow cytometry gating strategy to determine total cell counts. A fixed staining–gating strategy was used. a. Gating was performed on the Syto9-Alexa488-A channel to discriminate between debris or background and microbial events stained with SYTO™9. Gating was established by comparing colour density acquisition plots of the sample unstained (top panel) with plots from the same sample stained with SYTO™9 (bottom panel). Each panel reflects over 100,000 registered events. b. An additional gating was performed on the CountBright-Cy5-A channel to count in parallel the number of CountBrightTM beads (added to the sample). Gating was established by comparing acquisition plots of the sample without the addition of beads (top panel) with plots from the same sample with CountBrightTM beads added   
(bottom panel). Events pseudocolored red represent CountBrightTM bead events that fall within the FSC-H/CountBright-Cy5-A gate. The number of cell events were defined as events registered in the FSC-A/Syto9-Alexa488-A gating area, excluding number of bead events observed in the FSC-H/CountBright-Cy5-A gate (as CountBrightTM beads also display Alexa488-A signal). Concentration of cells in a sample was calculated as: number of cell events divided by the number of bead events, and then multiplied by the known concentration of beads in the sample, according to the assigned bead count of the lot. At least 2,000 bead events were recorded per sample, for accurate counting. The acquisition rate did not exceed 2,000 events per second.

# Reporting Summary

# Statistics

n/a Confirmed

p   
  
  
A description of allcovariates tested   
ali ltp   
  
  
al   
  
Estat  eect i Coen Pearon  indcatig how they were calcula

# Software and code

Policy information about availability of computer code

Data collection

B FAChorus™3.; Mi .0. Oor an Telgi; LiApplatn Suite X (  .).

Data analysis

T G .a  p.

# Policy information about availability of data

- Accession codes, unique identifiers, or web links for publicly available datasets   
- A description of any restrictions on data availability   
- For clinical datasets or third party data, please ensure that the statement adheres to our policy

Sequence Read Archive under BioProject number PRJNA1033532. records/4587955); SILVA 119 SSU NR99 database (https://www.arb-silva.de/download/arb-files/).

# Research involving human participants, their data, or biological material

and sexual orientation and race, ethnicity and racism.

<table><tr><td>Reporting on sex and gender</td><td>This study included participants of both sexes: 3 males and 6 females. In most of the analyses performed, samples from both sexes were combined (i.e. pooled), and therefore we could not perform analyses with sex as a factor. In experiments where samples were analysed separately (long-read sequencing of faecal samples), there was insufficient statistical power to perform analyses with sex as a factor.</td></tr><tr><td>Reporting on race, ethnicity, or other socially relevant groupings</td><td>N.a.</td></tr><tr><td>Population characteristics</td><td>Study participants (between 22 and 39 years old, average age 32.4 years old) had not received antibiotics in the prior 3 months and had no history of digestive disease.</td></tr><tr><td>Recruitment</td><td>Study participants were researchers of the University of Vienna and University of Southampton. Participants were recruited via email. Participants worked in the same building and were chosen based on their availability to provide a fresh faecal sample. All study participants provided written informed consent. Participants did not receive any compensation from participating in this study. Participants were all young adults, which can be considered a sampling bias.</td></tr><tr><td>Ethics oversight</td><td>University of Vienna Ethics Committee (reference #00161). University of Southampton Ethics and Research Governance Office (reference #78743).</td></tr></table>

# Field-specific reporting

Life sciences

Behavioural & social sciences

Ecological, evolutionary & environmental sciences

# Life sciences study design

<table><tr><td>Sample size</td><td>For microcosms experiments, faecal samples form 6 individuals were pooled and used per incubation, and each condition was run in triplicates. All triplicates were sequenced and analysed. Our rationale for mixing samples from 6 healthy donors was to assess the effect of drugs on a microbial community with greater microbial diversity than that of a single individual. For feasibility reasons (availability of freshly collected samples on the same day), this number was restricted to six donors. No statistical methods were used to pre-determine sample sizes, but our sample sizes are similar to those reported in previous publications. For SRS analyses, the number of cells analyzed was chosen based on feasibility.</td></tr><tr><td>Data exclusions</td><td>No other data was excluded from analyses, except for:-amplicon sequencing variants (ASVs, from 16S rRNA gene amplicon sequencing) assigned to Cyanobacteria or chloroplast were removed based on pre-established criteria: these ASVs were detected in negative controls but were not present in any of the faecal samples, and were therefore removed from analyses;-stimulated Raman scattering (SRS) analyses: during image acquisition and processing, outlier cells displaying abnormal intensity (&gt;mean±2 standard deviations) were rejected from the single cell masks. This intensity threshold was set after test and validation with independent samples, as food residues can be distinguished based on an irregular shape compared to cells, and by a stronger signal due to other absorption processes, that will gradually decrease due to the degradation of the absorption component.</td></tr><tr><td>Replication</td><td>Microcosm experiments with drugs were replicated (two times in total) and the results were successfully reproduced. Entacapone and iron rescue experiments using pure culture experiments were successfully reproduced one time. All other experiments were replicated at least one time. NanoSIMS analysis were only performed once based on feasibility, and was deemed successful because the iron levels in entacapone-exposed cells were very highly significant compared to control cells. For SRS measurements, we reproducibly detected analogous differences between treatments when sample analyses were repeated.</td></tr><tr><td>Randomization</td><td>For microcosms experiments, faecal samples were thoroughly mixed prior to allocation to microcosms, and allocations to microcosms were performed randomly. For flow cytometry, cell counts and SRS/photothermal analyses, both sample preparation and sample measurements were randomized. Preparation of samples for sequencing was randomized. For NanoSIMS, we first analysed the entacapone treated samples followed by the untreated controls to confirm that the observed Fe distribution patterns were not affected by measurement artifacts.</td></tr><tr><td>Blinding</td><td>Blinding during the microcosm and pure culture experiments was not possible, as different samples had to receive a different treatment/drug. Sample preparation for sequencing was carried out by an independent investigator in a blinded manner. Initial steps of sequencing data processing were performed blindly. Bioinformatic analyses of sequencing data was performed with automated software, but were not performed blindly, as we needed to know which samples to compare. For all other experiments or assays, the investigators were not formally blinded because of the high demand for certain sample/group samples at certain time points, which required appropriate selection of some of the samples.</td></tr></table>

# Reporting for specific materials, systems and methods

Materials & experimental systems 

<table><tr><td>n/a</td><td>Involved in the study</td><td>n/a</td><td>Involved in the study</td></tr><tr><td>☒</td><td>Antibodies</td><td>☒</td><td>ChIP-seq</td></tr><tr><td>☒</td><td>Eukaryotic cell lines</td><td>☐</td><td>Flow cytometry</td></tr><tr><td>☒</td><td>Palaeontology and archaeology</td><td>☒</td><td>MRI-based neuroimaging</td></tr><tr><td>☒</td><td>Animals and other organisms</td><td></td><td></td></tr><tr><td>☒</td><td>Clinical data</td><td></td><td></td></tr><tr><td>☒</td><td>Dual use research of concern</td><td></td><td></td></tr><tr><td>☒</td><td>Plants</td><td></td><td></td></tr></table>

Methods

Plants 

<table><tr><td>Seed stocks</td><td>N.a.</td></tr><tr><td>Novel plant genotypes</td><td>N.a.</td></tr><tr><td>Authentication</td><td>N.a.</td></tr></table>

# Flow Cytometry

# Plots

Confirm that:

The axis labels state the marker and fluorochrome used (e.g. CD4-FITC).

All plots are contour plots with outliers or pseudocolor plots.

A numerical value for number of cells or percentage (with statistics) is provided.

# Methodology

Sample preparation

UA , % ,%p s en  i ee i

<table><tr><td></td><td>(Merck), 0.5% v/v of vitamin solution (DSMZ Medium 461) and trace minerals, herein referred to as sM9. Samples were suspended in sM9 to yield a 0.05 g.mL-1 faecal slurry. At this point one aliquot of each sample was collected, pelleted, and stored at -80°C for metagenomic analysis. The homogenate was left to settle for 10 minutes, and the supernatant (devoid of any large faecal particles) was transferred into a new flask, where supernatants from the six different donors were combined. This combined sample was further diluted 1:10 in sM9 medium (as described above) or in supplemented Brain Heart Infusion (BHI) medium containing either 0% or 55% D2O (99.9% atom % (at%) D; Merck) for final 0% (control) or 50% D2O in incubation medium. Supplemented BHI medium consisted of 37 g.L-1 of brain heart infusion broth (Oxoid), 5 g.L-1 yeast extract (Oxoid), 1 g.L-1 L-cysteine (Merck) and 1 g.L-1 NaHCO3 (Carl Roth GmbH, Germany). Incubation tubes were supplemented with dimethylsulfoxide (DMSO, from Merck), entacapone (Prestwick Chemicals) or loxapine succinate (Prestwick Chemicals) pre-dissolved in DMSO. The final concentration was 2% w/v of DMSO in all vials (except for the H2O control, where water was added instead of DMSO). A subset of vials was supplemented with 20 μM or 1965 μM entacapone (ENT-Low and ENT-Hi, respectively) and another subset was supplemented with 20 μM or 100 μM loxapine succinate (LOX-Low and LOX-Hi, respectively). At time 0, and after an incubation time of 6 or 24 hours at 37°C under anaerobic conditions, two sample aliquots from each incubation and controls were collected by centrifugation. One aliquot was washed with 1× PBS and then fixed in 3% paraformaldehyde solution for 2 h at 4°C. Samples were finally washed two times with 1 ml of PBS and stored in PBS:Ethanol (50% v/v) at -20°C until further use. The second pelleted aliquot was stored at -20°C until further processing. A third aliquot was collected into sealed anaerobic vials containing 40% glycerol (Carl Roth GmbH, Germany) in PBS for a final cell 50% v/v cell suspension in 20% glycerol and stored at -80°C until further use. In addition, amendment of ENT-Hi to three individual faecal samples (two females and one male) and sample processing were carried as described above, except that samples were not mixed prior to incubation.Samples preserved in glycerol were diluted 200 to 800 times in 1× PBS. To remove any additional debris from the faecal incubations, samples were transferred into a flow cytometry tube by passing the sample through a snap cap containing a 35 μm pore size nylon mesh. Next, 500 μL of the microbial cell suspension was stained with the nucleic acid dye SYTOM 9 (Thermo Fisher Scientific, 0.5 μM in DMSO) for 15 min in the dark. The flow cytometry analysis of the microbial cells present in the suspension was performed using a BD FACSMelodyTM (BD Biosciences), equipped with a BD FACSChorusTM software v 3.0 (BD Biosciences).</td></tr><tr><td>Instrument</td><td>BD FACSMelodyTM (BD Biosciences)</td></tr><tr><td>Software</td><td>Collection: BD FACSChorusTM software v 3.0 (BD Biosciences).Analyses and visualisation: Microsoft Excel v 16.87 was used for data sorting and R v 4.0.2 was used for data visualization.</td></tr><tr><td>Cell population abundance</td><td>No cells were sorted.</td></tr><tr><td>Gating strategy</td><td>Briefly, background signals from the instrument and the buffer solution (PBS) were identified using the operational parameters forward scatter (FSC) and side scatter (SSC). Microbial cells were then displayed using the same settings in a scatter plot using the forward scatter (FSC) and side scatter (SSC) and pre-gated based on the presence of SYTOM 9 signals. Singlets discrimination was performed. Absolute counting beads (CountBrightTM, ThermoFisher Scientific) added to each sample were used to determine the number of cells per mL of culture by following the manufacturer&#x27;s instructions. Fluorescence signals were detected using the blue (488 nm – staining with SYTOM 9 and CountBrightTM beads) and yellow-green (561 nm - CountBrightTM beads only) optical lasers. The gated fluorescence signal events were evaluated on the forward-sideways density plot, to exclude remaining background events and to obtain an accurate microbial cell count. Instrument and gating settings were identical for all samples (fixed staining-gating strategy).</td></tr></table>