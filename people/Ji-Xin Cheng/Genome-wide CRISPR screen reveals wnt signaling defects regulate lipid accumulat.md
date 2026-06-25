Title: Genome-wide CRISPR screen reveals Wnt signaling defects regulate lipid accumulation in APOE4 oligodendrocytes

Authors: Leyla Anne Akay1,2, Anna Bright3, Carles A. Boix4,5, Kate Louderback1,2, Janine Medrano1,2 , Dingcheng Sun6,7, Haonan Lin6,7, Oisín King1,2, Gwyneth M. Welch1,2, Hiba Nawaid1,2, Emre Agbas1,2 , Alan Jiang1,2, Adele Bubnys1,2, Ji-Xin Cheng6,7, Joel Blanchard3, Li-Huei Tsai1,2,5,8

## Affiliations:

1. Picower Institute for Learning and Memory, MIT  
2. Department of Brain and Cognitive Sciences, MIT  
3. Icahn School of Medicine at Mount Sinai  
4. Department of Biomedical Informatics, Harvard Medical School  
5. The Broad Institute of MIT and Harvard  
6. Department of Biomedical Engineering, Boston University  
7. Photonics Center, Boston University  
8. Correspondence to: lhtsai@mit.edu

## Abstract

APOE4 is the largest genetic risk factor for late-onset Alzheimer’s disease, but the cellular mechanisms by which APOE variants influence risk of disease remain incompletely understood. We have previously found that APOE4 expression led to the intracellular accumulation of lipid droplets in oligodendrocytes, causing decreased myelination. However, the mechanisms by which APOE4 alters lipid metabolism are not fully understood. Here, we leveraged a genome-wide CRISPR screen and ATAC-sequencing in human induced pluripotent stem cell (iPSC)-derived oligodendrocytes to dissect APOE4’s lipid-associated mechanisms of action. Using these approaches, we identified decreased Wnt signaling, and overactive GSK3b activity, as regulators of lipid droplet accumulation in oligodendrocytes. Genetic and pharmacological inhibition of GSK3b reduced lipid droplets in APOE4 oligodendrocytes, and increased myelination in three-dimensional iPSC-derived brain organoids. Finally, we show that pharmacological inhibition of GSK3b reduces lipid droplets and improves myelination in APOE4;PS19 Tau transgenic mice. Together, our results provide a framework for understanding the mediation of APOE4-related changes to oligodendrocyte lipid metabolism and myelination.

## Introduction

Alzheimer’s disease (AD) is the most prevalent neurodegenerative disorder, affecting an estimated 7.2 million individuals in the United States1 . With limited treatment options available, there exists an urgent need for the identification of novel therapeutic targets. Large scale genetic association studies have identified hundreds of genes contributing to risk of developing late-onset AD, with the strongest associations consistently found in the APOE gene locus2 . APOE encodes Apolipoprotein E, a lipid transporter highly expressed in the brain. APOE exists across the human population largely as three variants: APOE3, the major allele; APOE2, a protective allele, and APOE4, a risk allele with regards to AD. One copy of APOE4 increases AD risk by an estimated 3-4 fold, whereas homozygosity increases risk by up to 12-fold2 .

APOE4 has previously been implicated in a diverse suite of cellular processes, ranging from amyloid-beta aggregation, inflammation, neurofibrillary tau pathology and blood-brain-barrier breakdown3 . However, an exact understanding of how APOE4 expression exerts its risk on AD remains elusive. We have previously performed single-nuclear RNA sequencing of the human post-mortem brain of individuals carrying the APOE4 allele, and found that APOE4 led to lipid and cholesterol dysregulation, most prominently in oligodendrocytes4 . Oligodendrocytes are the myelinating cells of the central nervous system, responsible for providing electrical insulation to neuronal axons. Dysfunction of oligodendrocytes and breakdown of myelin is increasingly recognized not only as a feature of Alzheimer’s disease, but potentially a pathologydriving mechanism5 . Therefore, understanding oligodendrocyte dysfunction and myelin maintenance within the contexts of aging and neurodegenerative disease is critical for the identification and development of new therapeutic opportunities.

## Results

## Genome-wide CRISPR screen reveals transcriptional programs underlying lipid accumulation in APOE4 oligodendrocytes

What are the molecular processes underlying the accumulation of lipid droplets in APOE4 oligodendrocytes? To gain a transcriptional handle on this disease-associated phenotype, we performed a genome-wide CRISPR knock-out screen in induced pluripotent stem cell (iPSC)-derived oligodendrocytes. We used a well-characterized iPSC line6 , homozygous for the APOE4 allele, to generate oligodendrocytes, as previously described7 . Upon differentiation, these iPSC-derived oligodendrocytes express canonical markers of mature oligodendrocytes, including transcription factor Olig2, and oligodendrocyte-specific surface antigen O4 (Extended data figure 1A).

We infected 90 million iPSC-derived APOE4 oligodendrocytes with an all-in-one guide RNA library containing Cas9 and targeting every protein-coding gene in the human genome, at a multiplicity of infection circa 0.3-0.5 (Figure 1A)8 . The viral construct contains a puromycin resistance cassette, enabling selection of infected oligodendrocytes8 . After antibiotic selection, oligodendrocytes were cultured for a further ten days, to allow enough time for the genomic lesion to affect protein turnover8 . After these ten days, live oligodendrocytes were stained for lipid droplets using the fluorescent dye BODIPY, harvested and FACsorted into two populations: cells with the top 15% of BODIPY fluorescence (“high lipid burden”) and cells with the lowest 15% of BODIPY fluorescence (“low lipid burden”) (Extended Data Figure 1B-F). Genomic DNA was extracted from both populations, subjected to PCR amplification, and sequenced for guide RNAs (Extended Data Figure 1G, H). The enrichment of individual guide RNAs in both sorted populations were calculated relative to the original library pool, using the tool Apron (Extended Data Figure 1I, J).

As expected, both sorted populations showed highly significant depletion of guide RNAs targeting essential genes, including genes necessary for sustaining the Golgi apparatus, ribosome, and ubiquitin machinery.

(Figure 1B, C). Among sorted populations, per-gene enrichments were calculated by averaging z-scored enrichments of individual guide RNAs (Figure 1D). In the “low lipid burden” population, significantly enriched genes included vesicular protein VAMP5, phospholipase PLA2G4C, two negative regulators of Wnt signaling, DKK1 and NKD1, as well as 336 other genes (Figure 1E, Supp. Table 1). As expected, canonical lipid-droplet associated gene PLIN3 was enriched, as were lipoprotein receptors LRP2 and VLDLR. In the “high lipid burden” population, enriched genes included tumor suppressor TP53, lipid sensor STARD10, Wnt signaling related genes APC2 and FZD10, and a further 401 additional genes (Figure 1E). Interestingly, APOE was also enriched, suggesting that loss of APOE-related lipoprotein function may provoke lipid droplet accumulation.

Several of our hits converged upon phospholipid metabolism (Figure 1F). Genes whose knockout were enriched in low lipid-burdened oligodendrocytes, i.e., genes likely to induce lipid accumulation, included phospholipases PLA2G4C, responsible for cleaving phosphatidylcholine to generate lysophosphatidic acid; AGPAT2, which converts lysophosphatidic acid to phosphatidic acid; PNPLA6, which cleaves phosphatidylcholine to generate glycerophosphorylcholine, and PNPLA7, which converts lysophosphatidylcholine to glycerophosphorylcholine. Notably, phospholipases have previously been reported to regulate lipid droplet formation9 .

Conversely, the enzymes responsible for converting diacylglycerol to phosphatidic acid (DGK1), and phosphatidic acid to CDP-diacylglycerol (CDS1) were enriched in the high-lipid droplet population (Figure 1F). CDP-diacylglycerol is a substrate for the generation of phosphatidylinositols, which are key components of the plasma membrane and myelin sheath10,11 . Together, these results suggests that enzymatic break-down of phosphatidylcholines and glycerophosphatdiylcholines by phospholipases may be a crucial step in lipid droplet formation in APOE4 oligodendrocytes, whereas the usage of diacylglycerols to generate phosphatidic acid, and potentially phosphatidylinositols, represents an alternative pathway.

To determine whether significantly enriched genes converged upon any known biological processes, we performed a gene set enrichment analysis. Among the “low lipid burden’ group, significantly enriched KEGG pathways included “basal cell carcinoma”, “glycerophospholipid metabolism,” and “viral-cytokine interaction” (Figure 1G, Supp. Table 2). Within the high lipid group, enriched pathways included “circadian rhythm,” “basal cell carcinoma,” and “Chagas disease.” (Figure 1G, Supp. Table 3). Several of the KEGG pathways were comprised of similar gene sets, including Wnt signaling genes (annotated as “basal cell carcinoma”, “Wnt signaling” and “Hippo signaling”), phospholipases, and immune-related genes. (Figure 1G). Crucially, although Wnt signaling was implicated in both high and low lipid populations, knock-out of the negative regulators of Wnt signaling (DKK1, NKD1) resulted in low lipid levels, whereas knock-out of canonical members of Wnt signaling (FZD10, WNT16) resulted in high lipid abundance.

To gain further insight into the transcriptional programs accompanying lipid burden in APOE4 oligodendrocytes, we next FAC-sorted naïve APOE4 oligodendrocytes (i.e., cells not subjected to any gene perturbations) based on lipid content (Figure 1H). We then performed bulk RNA-sequencing on the two sorted populations, comparing relative gene expression in low lipid-burdened versus high lipid-burdened oligodendrocytes. (Extended Data Figures 1K-P). APOE4 oligodendrocytes with increased lipid droplet burden upregulated a suite of lipid metabolic enzymes, including the cholesterol ester transferase protein CETP, ceramide synthase CERS2, and the enzyme CDIPT (CDP-diaclyglycerol transferase) (Figure 1H, Supp. Table 4). In contrast, oligodendrocytes with lower lipid burden had higher expression of diacylglycerol lipase alpha (DAGLA), an enzyme responsible for hydrolyzing diacylglycerols contained in lipid droplets. Notably, oligodendrocytes with lower lipid accumulation also had higher expression of Wntrelated genes WNT7B and TCF7L1, whereas oligodendrocytes with higher lipid accumulation upregulated DAB2, a negative regulator of Wnt signaling (Figure 1H, Supp. Table 4).

To validate our initial findings that Wnt signaling regulates lipid droplet accumulation in APOE4 oligodendrocytes, we next generated lentivirus to overexpress or knock-down (via shRNA) the Wnt signaling genes implicated in our CRISPR screen (WNT10A, FZD10, WNT16, DKK1), our RNA-sequencing (WNT7B), as well as the canonical master regulator of Wnt signaling, beta-catenin (CTNNB1) (Figure 1I). Ten days after infecting cultures of APOE4 oligodendrocytes, we labeled lipid droplets with BODIPY and used confocal microscopy to measure the number of lipid droplets per cell. We found that knock-down of DKK1 significantly (p value 0.0155) reduced lipid droplet accumulation, as did overexpression of betacatenin (CTNNB1) (p value 0.0031) (Figure 1J). Changes in gene expression were confirmed with RTqPCR (Extended Data Figure 1Q). Taken together, these results provide evidence that Wnt signaling regulates lipid accumulation in APOE4 oligodendrocytes.

## ATAC-sequencing reveals transcriptional programs depressed in APOE4

To further understand how APOE4 perturbs the epigenome of oligodendrocytes, and to identify putative master regulators of APOE4’s effects on lipid accumulation, we next used ATAC-sequencing to compare transposase-accessible regions of the genome between iPSC-derived oligodendrocytes, isogenic except for APOE genotype (Extended Data Fig. 2A, B). Data quality was confirmed by calculating transcription start site enrichment scores (Ext. Data Fig. 2C) and fraction of reads within peak (Ext. Data Fig. 2D), which were both well within ENCODE standards.

We identified a total of 47,999 differentially accessible regions between APOE3 and APOE4 oligodendrocytes, with the majority residing in introns and intergenic regions of the genome (Figure 2A, Supp. Table 5). After mapping the differentially accessible regions to genes, we identified a total of 9671 unique protein-coding genes with significant (false discovery rate-adjusted p value <0.05) differences in accessibility between APOE3 and APOE4 oligodendrocytes (Figure 2B). We observed decreased accessibility in genes related to Wnt signaling (WNT3, TCF4, CTNNB1, etc.), myelination (MOG, CNP, MBP), PI3K-Akt signaling (RPTOR, IGF1, FGF1), among others (Figure 2C). Genes with increased accessibility in APOE4 oligodendrocytes included phosphatidylcholine biosynthesis (PCYT1A, PCYT1B, CHKA), phospholipase metabolism (PLBD2, PLCZ1, PLA2G2A) and heparan sulfate biosynthesis (HS3ST1, HS3ST4, HS6ST1) among others (Figure 2C). Next, we used the tool HOMER to identify putative transcription factor binding domains enriched in differentially accessible regions (Figure 2D, Supp. Table 6). Motifs belonging to canonical Wnt transcription factors TCF7, LEF1 and c-MYC were among those significantly enriched in regions less accessible in APOE4, suggesting a depression of canonical Wnt signaling in APOE4 (Figure 2D).

Lipid droplets can form in response to nutritional, inflammatory and even thermal cues12 . Given that such distinct programs govern lipid droplet formation and breakdown across cell types, we wanted to narrow our focus onto APOE4-driven mechanisms. Therefore, we aimed to understand whether any of our CRISPR screen hits were also perturbed in APOE4 oligodendrocytes, relative to APOE3 oligodendrocytes. To test this, we compared differentially accessible regions between APOE3 and APOE4 with hits from our CRISPR screen, reasoning that the overlap would prioritize genes not only perturbed by APOE4, but also functionally related to lipid accumulation. We found 319 common genes (Figure 2E, Supp. Table 7), including members of the Wnt signaling family (WNT10A, WNT, NKD1) and several phospholipases (PNPLA6, PNPLA7, PLA2G2A, PLA2G4C). Pathway analysis of these overlapping genes again highlighted a significant enrichment of the terms “Basal cell carcinoma”, “Wnt signaling”, “Glycerophospholipids”, corresponding to canonical Wnt genes (WNT10A, WNT16, NKD1) and phospholipases (Figure 2E, Figure 2F, Supp. Table 8).

Given that Wnt signaling is known to play a role in neural development, we wanted to exclude the possibility that we were simply capturing differences in timing or development in our iPSC-derived models. Therefore, we next utilized a single-cell ATAC-sequencing dataset generated from human post-mortem prefrontal cortex, across 93 aged individuals13 . Using this dataset, we called differentially accessible peaks in individuals carrying one or more copies of the APOE4 allele, compared to APOE3 homozygotes (Figure 2G). We calculated the enrichment of Wnt-related transcription factor binding sites within these differentially accessible peaks, and found a significant enrichment of Wnt signaling-related motifs in regions less accessible in APOE4 carriers, particularly in oligodendrocyte lineage cells and neurons (Figure 2G, H). This suggests that APOE4-related decreases in Wnt signaling can be detected in the context of the aging human brain.

Finally, to more directly test the hypothesis that Wnt signaling was perturbed in APOE4 oligodendrocytes, we performed immunohistochemistry against the protein beta-catenin, which is prevented from degradation in the presence of Wnt signaling14 . We found a significant decrease in immunoreactivity to beta-catenin (p = 0.0159) in APOE4 oligodendrocytes compared to cultures of APOE3 oligodendrocytes, again suggesting that Wnt signaling was decreased in APOE4 oligodendrocytes (Figure 2I). In the absence of Wnt signaling, beta-catenin is phosphorylated by the kinase GSK3-beta, leading to its proteasomal degradation14 . To determine whether decreased beta-catenin observed in APOE4 oligodendrocytes could be due to increased activity of GSK3-beta, we performed immunohistochemistry against GSK3-beta. We found a significant increase in immunoreactivity to GSK3-beta in APOE4 oligodendrocytes relative to APOE3, suggestive of increased GSK3-beta expression (Figure 2J).

Together, these results suggest that canonical Wnt/beta-catenin signaling is decreased in APOE4 oligodendrocytes, whereas GSK3-beta protein expression is elevated relative to APOE3.

## The beta-catenin / GSK3b axis regulates lipid droplet formation in oligodendrocytes

Our CRISPR screen highlighted Wnt signaling as a potential regulator of lipid droplet accumulation, and our ATAC-sequencing data showed that Wnt signaling was decreased in APOE4 oligodendrocytes. Therefore, we wanted to understand whether manipulation of Wnt signaling could be a tractable handle to modulate lipid droplet accumulation in oligodendrocytes. Wnt signaling is complex, with different Wnt ligands able to activate, repress, or interfere with downstream effectors in context-specific manners. Given our findings that beta-catenin was decreased and GSK3b had increased expression in APOE4 oligodendrocytes, and that beta-catenin overexpression led to highly significant reduction in lipid droplets, we decided to target the GSK3-beta / beta-catenin axis. GSK3b and beta-catenin are mutually repressive; GSK3b phosphorylates beta-catenin, tagging it for ubiquitination and proteasomal degradation15 . Conversely, in the presence of beta-catenin-dependent Wnt signaling, GSK3b is rendered inactive by sequestration into multi-vesicular bodies16 .

To directly test whether overactive GSK3-beta could drive lipid accumulation in the absence of APOE4, we first pharmacologically stimulated GSK3-beta activity in APOE3 oligodendrocytes using the small molecule Dif317 . We found that activating GSK3-beta in APOE3 oligodendrocytes led to robust lipid droplet accumulation (p value 0.0093) (Figure 3A). To test whether inhibiting GSK3-beta could reduce lipid accumulation in APOE4 cells, we used the drug CHIR99021 to inhibit GSK3-beta activity, and found that GSK3b inhibition significantly (p value 0.0014) reduced lipid droplet accumulation in APOE4 oligodendrocytes (Figure 3B). We additionally performed Stimulated Raman Scattering (SRS) microscopy, which enables the identification and quantification of lipid species in single cells18 , on cultures of APOE4 oligodendrocytes with and without CHIR99021 treatment. Using this approach, we found that GSK3b inhibition led to a significant reduction in phospholipid and cholesterol content within individual lipid droplets (Extended Data Figure 3A).

To gain further insights into how GSK3-beta activity could be affecting lipid metabolism, we performed bulk RNA sequencing on cultures of APOE3 oligodendrocytes following GSK3-beta activation by Dif3 treatment. We observed broad upregulation of genes related to glycosphingolipid synthesis (B4GALT3, B4GALT1, ST3GAL5), glycerophospholipid metabolism (PLA2G2E, LPCAT1, LPGAT1) and cholesterol metabolism (CETP, LCAT, LDLR) (Figure 3C, Supp. Table 9). Notably, these results parallel the results from our initial CRISPR screen, which identified phospholipase enzymes as regulators of lipid droplet formation; LPCAT1 is responsible for re-acylation of lysophospholipids. Both CETP and LCAT are critical regulators of lipid droplet formation, responsible for esterifying free cholesterol and packaging it into lipoprotein-like particles19 .

Next, to determine how GSK3-beta inhibition could be decreasing lipid droplet burden in APOE4 oligodendrocytes, we performed bulk RNA-sequencing on APOE4 oligodendrocytes treated with CHIR99021. Among genes down-regulated after GSK3b inhibition, we noted a marked decrease of many genes involved in cholesterol biosynthesis: HMGS1, MVK, MVD, SQLE, LSS, SREBF1 and SREBF2, genes we previously found were aberrantly upregulated in APOE4 oligodendrocytes4 (Extended Data Figure 3B). The most positively enriched KEGG pathways corresponded to “Ribosome” and “Oxidative phosphorylation”, consisting of many genes encoding the mitochondrial NADH dehydrogenase, cytochrome oxidase, and ATPase units (Figure 3D, Supp. Table 10), in agreement with Wnt signaling’s known effects on mitochondrial biogenesis and oxidative phosphorylation20 . We additionally observed upregulation of NPC1, a transporter responsible for shuttling cholesterol to the lysosome, as well as upregulation of LIPA, a lysosomal lipase responsible for breaking down triglycerides and cholesterol esters. We also found broad upregulation of genes related to autophagy, including LAMP1, LAMP2, ATG4A, and ATG14 (Figure 3F). Together, these results suggest that inhibition of GSK3-beta might reduce lipid droplet burden by promoting mitochondrial bioenergetic use of stored lipids by oxidative phosphorylation, or potentially lipophagy.

To experimentally test the hypothesis that GSK3b inhibition could promote mitochondrial usage of lipid droplets, we performed a pulse-chase experiment, in which we labeled mitochondria in APOE4 oligodendrocytes using the fluorescent mitochondrial dye MitoTracker, and lipid droplets using BODIPY. We then inhibited GSK3-beta in cultures by treatment with CHIR99021. Using confocal microscopy in live cultures, we then measured lipid droplet association with mitochondria (Figure 3E). Intriguingly, we found that GSK3b inhibition led to a significantly increased (p value 0.0002) association of lipid droplets with mitochondria (Figure 3E). To test whether GSK3b inhibition could similarly lead to lysosomal degradation of lipid droplets, we performed a similar experiment using the lysosome-specific fluorescent dye LysoTracker. GSK3b inhibition did not affect lipid droplet-lyososomal colocalization (Extended Data Figure 3C).

Given that we had originally identified dysregulated phospholipase activity in our CRISPR screen, and that our SRS data demonstrated a decrease in phospholipid content within lipid droplets, we next tested whether GSK3b inhibition could affect phospholipase activity (Figure 3F). We incubated APOE4 oligodendrocytes with BODIPY-C11-glycerophosphocholine. This molecule is a glycerophosphocholine, with a fluorescent BODIPY tag at the site of phospholipase-directed cleavage. When phospholipases cleave this substrate, the BODIPY is liberated, and green fluorescence can be detected. After treating APOE4 oligodendrocytes with CHIR99021, we detected a significant decrease in BODIPY-PC fluorescence, indicating reduced phospholipase activity (Figure 3F).

Oligodendrocytes are primarily responsible for generating and maintaining the myelin sheath. Therefore, to test whether restoring Wnt signaling via GSK3b inhibition could improve myelination, we turned to a threedimensional iPSC-derived brain organoid model, containing myelinating oligodendrocytes (“myelinoids”)21 . We generated these iPSC-derived myelinoids as previously described21 . After 20 weeks in culture, myelinoids generated from APOE4 iPSCs had significantly reduced (p value 0.0012) myelination compared to those generated from isogenic APOE3 iPSC lines, as measured by immunoreactivity to myelin basic protein, suggesting that this model captures known APOE4-associated oligodendrocyte defects (Extended Data Figure 3D). After 18 weeks in culture, we began treating our APOE4 myelinoids with CHIR99021 (2 uM) (Figure 3G). After 2 weeks of CHIR99021 treatment, we performed immunohistochemistry on the myelinoids. We found that CHIR99021 treatment significantly (p value 0.0431) increased immunoreactivity to myelin basic protein (MBP) in APOE4 myelinoids (Figure 3H). We did not detect a significant difference in the number of Olig2-positive cells, indicating that this effect was likely not mediated through increases in oligodendrocyte proliferation, but potentially through increased myelin production from existing oligodendrocytes (Extended Data Figure 3E). We detected a significant (p value 0.0044) increase in immunoreactivity to neurofilament staining, indicative that GSK3b inhibition promoted axonal growth (Extended Data Figure 3F).

Together, this data suggests that GSK3b inhibition may reduce lipid droplet accumulation in APOE4 oligodendrocytes and promote myelination by suppressing dysregulated cholesterol synthesis, decreasing phospholipase activity, and engaging mitochondrial-lipid droplet interactions.

## Inhibition of GSK3b reduces lipid droplets and increases myelination in an APOE4;PS19 Tau mouse model

Our results suggest that dysregulated GSK3-beta could drive lipid accumulation in APOE4 iPSC-derived oligodendrocytes, and that inhibiting GSK3-beta can reduce lipid droplet burden, potentially by promoting mitochondrial usage of lipid droplets, suppression of phospholipase activity, as well as increasing myelination. To test whether inhibition of GSK3b would be sufficient to reduce lipid pathology in an in vivo context, we employed the Tau PS19 transgenic mouse line, crossed to humanized APOE3 or APOE4 mice22 . The expression of APOE4 has previously been shown to worsen tau pathology, exacerbate inflammation and lead to oligodendrocyte dysfunction in transgenic mice22,23 . In agreement with these previous findings, we detected significant (p value 0.0321) increases in phosphorylated tau pathology in APOE4;PS19 mice, compared to APOE3;PS19 mice at 6-7 months of age (Extended Data Figure 4A). We also detected a significant (p value 0.0273) decrease in immunoreactivity to myelin basic protein in the hippocampus of APOE4;PS19 mice as early as three months of age (Figure 4A). We did not detect any changes in Olig2-positive cell number in the hippocampus, suggesting that defects in myelination are not primarily driven by gross loss of oligodendrocytes (Extended Data Figure 4B).

To determine whether APOE4;PS19 mice also harbored brain lipid accumulation, we stained for lipid droplets in hippocampal brain slices using BODIPY (Figure 4B). We found detectable lipid droplets throughout the hippocampus of both APOE3; and APOE4;PS19 mice, most notably in the CA3 region (Figure 4B). Although there were no measurable differences in the amount or localization of lipid droplets between APOE genotypes at three or six months of age, we found that APOE4;PS19 mice had a striking increase in lipid accumulation around ten months of age (Figure 4C).

To determine whether activation of Wnt signaling via reduction of GSK3b activity could reduce lipid droplets in vivo, we first treated a cohort of five-month old APOE4;PS19 mice with CHIR99021 at a dose of 5 mg/kg via intraperitoneal injection for two weeks (Figure 5D), before the onset of detectable tau pathology. Staining hippocampal brain sections for lipid droplets using BODIPY revealed a significant (p value 0.0072) reduction in lipid droplets in the hippocampus of CHIR-treated APOE4;PS19 mice, compared to vehicletreated controls (Figure 5E). Next, to test whether restoring Wnt signaling over a longer time-course could increase myelination, we treated a cohort of eight-month old APOE4;PS19 mice with CHIR99021 for six weeks, and performed immunohistochemistry for myelin basic protein (Figure 4F). The longer-term treatment in older mice significantly increased hippocampal myelination (p value 0.0329), as measured by immunoreactivity to myelin basic protein (Figure 4G). We did not detect changes in Olig2-positive cell number (Extended Data Fig. 4C), immunoreactivity to GFAP (Extended Data Fig. 4D), number or morphology of microglia (Extended Data Fig. 4E-F), suggesting that the effects on myelination are primarily due to increased myelin production from existing oligodendrocytes. Given GSK3b’s well-documented role as a tau kinase, we also measured immunoreactivity to tau phosphorylated at Threonine 181 or Serine 396 residues, where GSK3b is known to phosphorylate tau. We did not detect a significant difference in immunoreactivity to tau phosphorylation at either residue (Extended Data Fig. 4G, H).

## Discussion

Here, we use a genome-wide genetic screen to identify regulators of lipid droplet accumulation in APOE4 oligodendrocytes, and find an unexpected role of the canonical Wnt signaling pathway. We find that Wnt signaling is depressed in APOE4 oligodendrocytes, both in iPSC-derived models and in the aged human post-mortem brain, and that deregulated Wnt / GSK3b kinase activity is involved in the development of lipid accumulation. Importantly, restoration of Wnt signaling via GSK3b inhibition reduced lipid droplet accumulation and increased myelination in both human iPSC-based models, as well as transgenic mouse models.

Aberrant lipid accumulation has been reported in a range of APOE4-related contexts, from transgenic mouse models24, to iPSC-derived microglia25,26, astrocytes27,28 and oligodendrocytes4 . Lipid accumulation in these cell types has been linked to a variety of phenotypes, including cellular growth defects28 , dysregulated neuronal activity25, defective oligodendrocyte maturation29 and decreased myelination4 . Importantly, APOE4-associated glial lipid accumulation is also closely associated with neuronal tau pathology. Conditioned media from iPSC-derived microglia with high lipid burden was shown to provoke tau hyperphosphorylation in iPSC-derived neurons26 . Promoting microglial cholesterol efflux by overexpression of lipid transporter ABCA1 or dietary treatment of LXR agonist was also found to reduce tau pathology in APOE4;PS19 mice24 . Therefore, identifying pathways regulating lipid burden in APOE4 glia may advance the development of therapeutics targeting neuronal tau pathology.

Previous research has utilized both genome-wide and targeted CRISPR screens to identify regulators of lipid burden in APOE4 microglia, highlighting the contributions of triglyceride metabolism, lysosomal function and mTOR signaling26,30 . Intriguingly, our genome-wide CRISPR screen in APOE4 oligodendrocytes recovered an enrichment of phospholipase enzymes. As these enzymes are primarily involved in cleaving phosphatidylcholines, the majority of which reside within cellular membranes, it is tempting to speculate that lipid droplets in APOE4 oligodendrocytes may be generated by aberrant cleavage of membrane-associated phospholipids, rather than uptake of exogenous fatty acids and subsequent conversion to triacylglycerols.

We also find that a major upstream pathway driving lipid accumulation in APOE4 oligodendrocytes is disrupted Wnt/beta-catenin signaling. Previous research has highlighted an intriguing relationship between APOE variants and Wnt signaling, with exposure to ApoE4 protein demonstrated to reduce Wnt/betacatenin signaling in cell lines31 , and variants in LRP6 reported to increase Alzheimer’s disease risk in an APOE-genotype dependent manner32 . Of note, the rare protective APOE variant “Christchurch” was recently shown to increase Wnt / beta-catenin signaling in human iPSC-derived brain organoids33 . The potential convergence of rare protective variants and common risk variants in APOE onto changes in Wnt signaling certainly warrants further investigation.

The kinase GSK3b is a major inhibitor of Wnt signaling, and here we find that inhibition of GSK3b activity significantly lessens lipid droplet burden in APOE4 oligodendrocytes, both in human cells and transgenic mouse models. Given GSK3b’s established role as a major tau phosphorylating kinase, our work draws an interesting potential parallel between oligodendrocyte lipid accumulation and neuronal tau pathology. Recent work has demonstrated that reduced lithium bioavailability contributes to Alzheimer’s disease onset and progression in aged individuals, through activation of GSK3b34 . Notably, disrupting Wnt signaling by provoking lithium deficiency in a mouse model of AD not only exacerbated tau pathology, but also had profound consequences on oligodendrocyte function, including demyelination34 . Together, these findings implicate GSK3b as a shared pathological connection between glial lipid accumulation and neuronal tau pathology, highlighting its relevance to Alzheimer’s disease etiology.

## Acknowledgements

We thank David Root and members of the Broad Institute’s Genetic Perturbation Platform for assistance with CRISPR screening. We thank Stuart Levine, Duanduan Ma and members of the BioMicroCenter for assistance with RNA and ATAC sequencing and analysis. We thank Mat Victor for assistance with iPSC culture. We thank Ying Zhou, Ute Geigenmuller and Erica McNamara for administrative support and assistance with mouse colony management. This work was partially supported by NIH grants RF1AG075901, UH3NS115064 to L-H T, the Robert and Renee E Belfer Family Foundation, the Manthripragada McManama Alzheimer's Fund, CAMA Seed Fund, the Picower Institute for Learning and Memory, J. Crayton Pruitt Foundation, Joseph P. DiSabato and Nancy Sakamoto.

## Declaration of Interests

A patent application has been filed by LAA and LHT on the results of the CRISPR screen. LHT is a member of the scientific advisory board of 4M Therapeutics and TAC Therapeutics.

## References

1. Alzheimer’s Association 2025 Alzheimer’s Disease Facts and Figures.  
2. Jackson, R. J., Hyman, B. T. & Serrano-Pozo, A. Multifaceted roles of APOE in Alzheimer disease. Nat. Rev. Neurol. 20, 457–474 (2024).  
3. Blumenfeld, J., Yip, O., Kim, M. J. & Huang, Y. Cell type-specific roles of APOE4 in Alzheimer disease. Nat. Rev. Neurosci. 25, 91–110 (2024).  
4. Blanchard, J. W. et al. APOE4 impairs myelination via cholesterol dysregulation in oligodendrocytes. Nature 611, 769–779 (2022).  
5. Kedia, S. & Simons, M. Oligodendrocytes in Alzheimer’s disease pathophysiology. Nat. Neurosci. 28, 446–456 (2025).  
6. Lin, Y.-T. et al. APOE4 Causes Widespread Molecular and Cellular Alterations Associated with Alzheimer’s Disease Phenotypes in Human iPSC-Derived Brain Cell Types. Neuron 98, 1141- 1154.e7 (2018).  
7. Douvaras, P. & Fossati, V. Generation and isolation of oligodendrocyte progenitor cells from human pluripotent stem cells. Nat. Protoc. 10, 1143–1154 (2015).  
8. Doench, J. G. et al. Optimized sgRNA design to maximize activity and minimize off-target effects of CRISPR-Cas9. Nat. Biotechnol. 34, 184–191 (2016).  
9. Guijas, C., Rodríguez, J. P., Rubio, J. M., Balboa, M. A. & Balsinde, J. Phospholipase A2 regulation of lipid droplet formation. Biochim. Biophys. Acta 1841, 1661–1671 (2014).  
10. Nawaz, S. et al. Phosphatidylinositol 4,5-Bisphosphate-Dependent Interaction of Myelin Basic Protein with the Plasma Membrane in Oligodendroglial Cells and Its Rapid Perturbation by Elevated Calcium. J. Neurosci. 29, 4794–4807 (2009).  
11. Shen, H. & Dowhan, W. Regulation of phospholipid biosynthetic enzymes by the level of CDPdiacylglycerol synthase activity. J. Biol. Chem. 272, 11215–11220 (1997).  
12. Walther, T. C., Chung, J. & Farese, R. V. Lipid Droplet Biogenesis. Annu. Rev. Cell Dev. Biol. 33, 491–510 (2017).  
13. Xiong, X. et al. Epigenomic dissection of Alzheimer’s disease pinpoints causal variants and reveals epigenome erosion. Cell 186, 4422-4437.e21 (2023).  
14. Liu, J. et al. Wnt/β-catenin signalling: function, biological mechanisms, and therapeutic opportunities. Signal Transduct. Target. Ther. 7, 3 (2022).  
15. Ikeda, S. et al. Axin, a negative regulator of the Wnt signaling pathway, forms a complex with GSK-3β and β-catenin and promotes GSK-3β-dependent phosphorylation of β-catenin. EMBO J. 17, 1371– 1384 (1998).  
16. Taelman, V. F. et al. Wnt Signaling Requires the Sequestration of Glycogen Synthase Kinase 3 inside Multivesicular Endosomes. Cell 143, 1136–1148 (2010).  
17. Takahashi-Yanaga, F. et al. Dictyostelium Differentiation-inducing Factor-3 Activates Glycogen Synthase Kinase-3β and Degrades Cyclin D1 in Mammalian Cells\*. J. Biol. Chem. 278, 9663–9670 (2003).  
18. Yue, S. & Cheng, J.-X. Deciphering single cell metabolism by coherent Raman scattering microscopy. Curr. Opin. Chem. Biol. 33, 46–57 (2016).  
19. Mehta, N. et al. The evolving role of cholesteryl ester transfer protein inhibition beyond cardiovascular disease. Pharmacol. Res. 197, 106972 (2023).  
20. Yoon, J. C. et al. Wnt signaling regulates mitochondrial physiology and insulin sensitivity. Genes Dev. 24, 1507–1518 (2010).  
21. Feng, L. et al. Developing a human iPSC-derived three-dimensional myelin spheroid platform for modeling myelin diseases. iScience 26, 108037 (2023).  
22. ApoE4 markedly exacerbates tau-mediated neurodegeneration in a mouse model of tauopathy | Nature. https://www.nature.com/articles/nature24016.  
23. Koutsodendris, N. et al. Neuronal APOE4 removal protects against tau-mediated gliosis, neurodegeneration and myelin deficits. Nat. Aging 3, 275–296 (2023).  
24. Litvinchuk, A. et al. Amelioration of Tau and ApoE4-linked glial lipid accumulation and neurodegeneration with an LXR agonist. Neuron 112, 384-403.e8 (2024).  
25. Victor, M. B. et al. Lipid accumulation induced by APOE4 impairs microglial surveillance of neuronalnetwork activity. Cell Stem Cell 29, 1197-1212.e8 (2022).  
26. Haney, M. S. et al. APOE4/4 is linked to damaging lipid droplets in Alzheimer’s disease microglia. Nature 628, 154–161 (2024).  
27. Tcw, J. et al. Cholesterol and matrisome pathways dysregulated in astrocytes and microglia. Cell 185, 2213-2233.e25 (2022).  
28. Sienski, G. et al. APOE4 disrupts intracellular lipid homeostasis in human iPSC-derived glia. Sci. Transl. Med. 13, eaaz4564 (2021).  
29. Mok, K. K.-S. et al. Apolipoprotein E ε4 disrupts oligodendrocyte differentiation by interfering with astrocyte-derived lipid transport. J. Neurochem. 165, 55–75 (2023).  
30. Meier, S. et al. An efficient, non-viral arrayed CRISPR screening platform for iPSC-derived myeloid and microglia models. Stem Cell Rep. 20, 102420 (2025).  
31. Caruso, A. et al. Inhibition of the canonical Wnt signaling pathway by apolipoprotein E4 in PC12 cells. J. Neurochem. 98, 364–371 (2006).  
32. De Ferrari, G. V. et al. Common genetic variation within the Low-Density Lipoprotein Receptor-Related Protein 6 and late-onset Alzheimer’s disease. Proc. Natl. Acad. Sci. U. S. A. 104, 9434–9439 (2007).  
33. Perez-Corredor, P. et al. APOE3 Christchurch modulates β-catenin/Wnt signaling in iPS cell-derived cerebral organoids from Alzheimer’s cases. Front. Mol. Neurosci. 17, 1373568 (2024).  
34. Aron, L. et al. Lithium deficiency and the onset of Alzheimer’s disease. Nature 1–10 (2025) doi:10.1038/s41586-025-09335-x.  
35. Karimzadeh, M., Ernst, C., Kundaje, A. & Hoffman, M. M. Umap and Bismap: quantifying genome and methylome mappability. Nucleic Acids Res. 46, e120 (2018).  
36. Expanded encyclopaedias of DNA elements in the human and mouse genomes | Nature. https://www.nature.com/articles/s41586-020-2493-4.  
37. Model-based Analysis of ChIP-Seq (MACS) | Genome Biology | Full Text. https://genomebiology.biomedcentral.com/articles/10.1186/gb-2008-9-9-r137.  
38. Neph, S. et al. BEDOPS: high-performance genomic feature operations. Bioinforma. Oxf. Engl. 28, 1919–1920 (2012).  
39. edgeR: a Bioconductor package for differential expression analysis of digital gene expression data | Bioinformatics | Oxford Academic. https://academic.oup.com/bioinformatics/article/26/1/139/182458.  
40. GC-Content Normalization for RNA-Seq Data | BMC Bioinformatics | Full Text. https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-12-480.  
41. Fast motif matching revisited: high-order PWMs, SNPs and indels | Bioinformatics | Oxford Academic. https://academic.oup.com/bioinformatics/article/33/4/514/2726114.  
42. JASPAR 2018: update of the open-access database of transcription factor binding profiles and its web framework - PubMed. https://pubmed.ncbi.nlm.nih.gov/29140473/.  
43. Kulakovskiy, I. V. et al. HOCOMOCO: towards a complete collection of transcription factor binding models for human and mouse via large-scale ChIP-Seq analysis. Nucleic Acids Res. 46, D252–D259 (2018).  
44. Jolma, A. et al. DNA-binding specificities of human transcription factors. Cell 152, 327–339 (2013).  
45. Lin, H. et al. Label-free nanoscopy of cell metabolism by ultrasensitive reweighted visible stimulated Raman scattering. Nat. Methods 22, 1040–1050 (2025).  
46. Ding, G. et al. Self-supervised elimination of non-independent noise in hyperspectral imaging. Newton 1, (2025).  
47. Microsecond fingerprint stimulated Raman spectroscopic imaging by ultrafast tuning and spatialspectral learning | Nature Communications. https://www.nature.com/articles/s41467-021-23202-z.

Materials  
Key Resource Table

<table><tr><td>Antibody</td><td>Source</td><td>Catalogue Number</td></tr><tr><td>Anti O4</td><td>Sigma Aldrich</td><td>MAB345</td></tr><tr><td>Anti Beta-catenin</td><td>Cell Signaling Technology</td><td>8480</td></tr><tr><td>Anti GSK3b</td><td>Cell Signaling Technology</td><td>9315T</td></tr><tr><td>Anti Neurofilament</td><td>BioLegend</td><td>837802</td></tr><tr><td>Anti Olig2</td><td>Millipore Sigma</td><td>AB9610</td></tr><tr><td>Anti Myelin Basic Protein</td><td>Millipore Sigma</td><td>AB9348</td></tr><tr><td>Anti Tau (phospho-Ser396)</td><td>Cell Signaling Technology</td><td>48856</td></tr><tr><td>Anti Tau (phospho-Thr181)</td><td>Cell Signaling Technology</td><td></td></tr><tr><td>Anti MBP</td><td>ThermoFisher</td><td>PA1-10008</td></tr><tr><td>Anti IBA1</td><td>Synaptic Systems</td><td></td></tr><tr><td>Anti GFAP</td><td>ThermoFisher</td><td>13-0300</td></tr><tr><td>Anti Olig2</td><td>Atlas Antibodies (Sigma-Aldrich)</td><td>HPA003254</td></tr><tr><td>Chemicals and proteins</td><td>Source</td><td>Catalogue Number</td></tr><tr><td>Dif3</td><td>MedChemExpress</td><td>HY-145669</td></tr><tr><td>CHIR99021</td><td>Tocris</td><td>4423</td></tr><tr><td>BODIPY</td><td>ThermoFisher</td><td>D3922</td></tr><tr><td>BODIPY C11-glycerophosphocholine</td><td>ThermoFisher</td><td>B7701</td></tr><tr><td>MitoTracker</td><td>ThermoFisher</td><td>M22425</td></tr><tr><td>LysoTracker</td><td>ThermoFisher</td><td>L7528</td></tr><tr><td>Human NT-3 Recombinant Protein</td><td>R&amp;D Systems</td><td>267-N3-005</td></tr><tr><td>All Trans Retinoic Acid</td><td>Sigma Aldrich</td><td>r2625-50mg</td></tr><tr><td>SB431542</td><td>R&amp;D Systems</td><td>1614/10</td></tr><tr><td>LDN-193189</td><td>Stem Cell Technologies</td><td>72147</td></tr><tr><td>Smoothened Agonist, SAG</td><td>Sigma Aldrich</td><td>566660</td></tr><tr><td>Recombinant Human PDGF-AA Protein, CF</td><td>R&amp;D Systems</td><td>221-AA-010</td></tr><tr><td>Recombinant Human IGF-I/IGF-1 Protein, CF</td><td>R&amp;D Systems</td><td>291G1200</td></tr><tr><td>Recombinant Human HGF Protein</td><td>R&amp;D Systems</td><td>294HG005</td></tr><tr><td>Biotin</td><td>Sigma Aldrich</td><td>B4501</td></tr><tr><td>N6,2'-O-Dibutyryladenosine 3',5'-cyclic monophosphate sodium salt (cAMP)</td><td>Sigma Aldrich</td><td>D0260-5MG</td></tr><tr><td>3,3',5-Triiodo-L-thyronine (T3)</td><td>Sigma Aldrich</td><td>T2877-100MG</td></tr><tr><td>L-Ascorbic Acid</td><td>Sigma Aldrich</td><td>a4403</td></tr><tr><td>Insulin</td><td>Sigma Aldrich</td><td>19278-5ml</td></tr><tr><td>GlutaMAX Supplement</td><td>ThermoFisher</td><td>35050061</td></tr><tr><td>OptiMEM</td><td>ThermoFisher</td><td>31985062</td></tr><tr><td>PEI</td><td>MedChemExpress</td><td>HY-K2014</td></tr><tr><td>Sodium Pyruvate</td><td>ThermoFisher</td><td>11360070</td></tr><tr><td>HEPES</td><td>ThermoFisher</td><td>15630130</td></tr><tr><td>Beta-mercaptoethanol</td><td>Sigma Aldrich</td><td>M6250</td></tr><tr><td>Non-essential amino acids</td><td>ThermoFisher</td><td>11140050</td></tr><tr><td>Fetal bovine serum</td><td>ThermoFisher</td><td>A5256801</td></tr><tr><td>Kits</td><td>Source</td><td>Catalogue Number</td></tr><tr><td>ATAC-Sequencing Kit</td><td>Active Motif</td><td>53150</td></tr><tr><td>RNEASY Mini Extraction Kit</td><td>Qiagen</td><td>74104</td></tr><tr><td>Bacteria and Virus Strains</td><td>Source</td><td>Catalogue Number</td></tr><tr><td>Human CRISPR knockout pooled library (All-in-one, Brunello)</td><td>Addgene</td><td>73179-LV</td></tr><tr><td>pLV-mCherry-EF1A&gt;hFZD10 E. coli stock</td><td>VectorBuilder</td><td>Ecoli(VB240827-1367zuk)</td></tr><tr><td>pLV-mCherry-EF1A&gt;hWNT16 E. coli stock</td><td>VectorBuilder</td><td>Ecoli(VB240827-1369rkt)</td></tr><tr><td>pLV-shRNA-mCherry-U6&gt;hDKK1 E. coli stock</td><td>VectorBuilder</td><td>Ecoli(VB240827-1370nzg)</td></tr><tr><td>pLV-shRNA-mCherry-U6&gt;hWNT10A E. coli stock</td><td>VectorBuilder</td><td>Ecoli(VB240827-1375dty)</td></tr><tr><td>pLV-mCherry-EF1A&gt;hTCF7L1 E. coli stock</td><td>VectorBuilder</td><td>Ecoli (VB240701-1266kxb)</td></tr><tr><td>pLV-mCherry-EF1A&gt;hCTNNB1 E. coli stock</td><td>VectorBuilder</td><td>Ecoli (VB240701-1362fat)</td></tr><tr><td>pLV-mCherry-EF1A&gt;hWNT7B E. coli stock</td><td>VectorBuilder</td><td>Ecoli (VB240702-1205vyd)</td></tr><tr><td>pLV[Exp]-mCherry-EF1A&gt;ORF_Stuffer E. coli stock</td><td>VectorBuilder</td><td>Ecoli (VB900151-4479mjt)</td></tr><tr><td>pMDLg/pRRE</td><td>Addgene</td><td>12251</td></tr><tr><td>pRSV-Rev</td><td>Addgene</td><td>12253</td></tr><tr><td>pMD2.G</td><td>Addgene</td><td>12259</td></tr></table>

## Methods

iPSC-derived oligodendrocyte differentiation

Oligodendrocytes were generated according to previously established protocols7 . Briefly, colonies from isogenic APOE3 and APOE4 induced pluripotent stem cells (iPSC) 6 were plated into 6-well plates, and cultured until colonies reached approximately 250 um in diameter. Cells were then cultured in “Neural Induction” media, mTSER containing 10 μM SB431542, 250 nM LDN193189 and 100 nM RA. Media was changed every day. On day 8, the media was changed to “N2 media”, or DMEM/F12 media containing non-essential amino acids, GlutaMAX, N2 supplement, 2-mercaptoethanol, Penicillin-Streptomycin, with 100 nM RA and 1 μM SAG added each day. On day 12, aggregated cells were mechanically lifted and replated into ultra-low-attachment 10 cm dishes. Cell aggregates were then cultured in N2B27 media. On day 30, the aggregates were plated into 6-well plates coated with Poly-L-orinthine and laminin, to enrich

for oligodendrocyte precursors. Oligodendrocyte precursors were then cultured in N2/B27 media containing PDGFaa (10 ng/ml), IGF-1 (10 ng/ml), HGF (5 ng/ml), NT3 (10 ng/ml), T3 (60 ng/ml), Biotin (100 ng/ml), cAMP (1 μM) and Insulin (25 μg/ml). On day 75, cells were then cultured in N2/B27 media containing HEPES (10 mM), T3 (60 ng/mL), Biotin (100 ng/mL), cAMP (1 uM), Insulin (25 ug/mL), and Ascorbic acid (20 ug/mL). After day 75, oligodendrocyte cell fate was validated by immunohistochemistry for canonical markers of lineage (Olig2) and maturity (O4).

## Genome-wide CRISPR knockout screen

90 million APOE4 iPSC-oligodendrocytes were plated into 150 mm dishes, at a density of approximately 9 million cells per dish. Cells were infected with the Brunello Human CRISPR Knockout pooled library, containing Cas9, at a multiplicity of infection between 0.3 and 0.5. After 36 hours, cells were treated with Puromycin to enable selection for infected oligodendrocytes. After a subsequent ten days in culture, cells were treated with BODIPY to label lipid droplets. 24 hours after BODIPY treatment, media was changed to remove excess BODIPY, and cells were lifted into FACS buffer and subjected to FAC-sorting based on green fluorescent signal. After gating for exclusion of dead cells, doublets and debris, single cells with the top 15% and the lowest 15% of green fluorescent signal were sorted separately and collected. Genomic DNA from each population was extracted using the NucleoSpin Blood XL Maxi kit, and guide RNAs were subjected to PCR amplification and sequencing. Guide RNA enrichment was calculated relative to the original library pool of DNA, using the Broad Institute’s tool “Apron”. Genes were deemed significantly “enriched” or “depleted” if the z-scored average of their corresponding guide RNAs’ log fold change had an adjusted p-value lower than 0.05.

## RNA-sequencing on sorted populations

APOE4 iPSC-oligodendrocytes were treated with BODIPY overnight. The next morning, media was changed and cells were collected and subjected to FAC-sorting based on BODIPY signal. The top 15% and the lowest 15% of green fluorescent signal were separately sorted, and cells were pelleted. The cell sorting was repeated in triplicate. RNA was extracted from all populations, using Qiagen’s RNeasy Kit, according to manufacturer’s instructions. Bulk RNA-sequencing was then performed on sorted populations of APOE4 iPSC-oligodendrocytes, using a 50 + 50 bases pair-end run with 8 + 8 nucleotide indexes, on a Singular 50PE run with 100m reads, at MIT’s BioMicroCenter core facility.

## Lentivirus generation and gene manipulation

HEK293T cells were plated in 10 cm tissue culture dishes, in DMEM media containing Glutamax, 10% Fetal Bovine Serum, 1% Non-essential amino acids, 1% Sodium Pyruvate, 1% HEPES buffer, 1% Pen/Strep solution, 0.1% beta-mercaptoethanol. The next day, 10 ug of each transfer vector, 5 ug pMDLg, 2.5 ug pRSV-Rev, 2.5 ug pMD2.G, 600 uL of OptiMEM, and 48 uL of PEI were added to Eppendorf tubes, inverted gently and incubated at room temperature for 20 minutes. This transfection solution was then added to HEK293T cells drop-wise. Media was changed the following day. Two days later, lentivirus-containing media was collected from dishes, and centrifuged at 1200 xg for 5 minutes at $4 ^ { \circ } \mathsf { C } .$ . The supernatant was poured into a Millex 0.45 um PES filter cup into ultracentrifuge tubes, and spun down in a Beckman ultracentrifuge for 2 hours at 25,000 rpm using a SW32Ti rotor. At the end of the spin, media was aspirated and the viral pellet was resuspended in 100 uL of phosphate-buffered saline. The lentiviral pellet was aliquoted and stored in $\mathfrak { - 8 0 \circ } \mathsf { C }$ . Viral aliquots were only used once, and never thawed and re-frozen. APOE4 oligodendrocytes were plated into 6-well plates at a density of 250,000 cells per well. Cells were treated with 10 uL of virus per well. 10 days after transfection, viral expression was assessed by mCherry expression. Cells were then treated with BODIPY, and re-plated into either 96- well plates for confocal imaging, or 6-well plates for RNA extraction.

## qPCR analysis of viral gene manipulation

Following RNA extraction and purification, Bio-Rad’s iScript™ Reverse Transcription Supermix (#1708840) was used to create cDNA, per manufacturer’s instructions. cDNA was quantified using a NanoDrop Spectrophotometer ND-1000. The qPCR was carried out according to the protocol provided by Bio-Rad for the SsoFast™ EvaGreen® Supermix (#1725201), and the Bio-Rad CFX96 System was used to perform the cycling per the optimized conditions suggested in the protocol. The number of cycles was increased from 40 to 50 to ensure sufficient amplification of all samples. A final concentration of 500 nM was used per primer per replicate, and 50 ng of cDNA was used per replicate. Once the samples were run in triplicate, the average Cq was found. The expression fold change for each sample was found using the following formula, 2^-((test experimental Cq - house experimental Cq) - (test control Cq - house control Cq)), where test refers to the primer used being that of the gene in question and house being the primers of the reference gene- in this case GAPDH. Experimental means the cDNA used is from cells infected with a virus to overexpress a certain gene, and control means the cDNA used is from the stuffer control, where the cells were infected with a virus with a random sequence instead of one of the target genes.

## ATAC-sequencing on APOE oligodendrocytes

ATAC-sequencing was performed using the ActiveMotif ATAC-sequencing kit, according to manufacturer’s instructions with minor modifications. Briefly, isogenic APOE3 and APOE4 oligodendrocytes were harvested and pelleted into LoBind DNA Eppendorf tubes, with 250,000 cells per replicate, and two replicates per genotype. Media was aspirated, and cells were centrifuged in 100 uL of ice-cold phosphate-buffered saline for five minutes at 500 rcf at 4C. Supernatant was discarded and cells were resuspended in 100 uL of ice-cold ATAC lysis buffer, and centrifuged for 10 minutes at 500 rcf at 4C. 50 uL of transposomes and tagmentation buffer mastermix was then added to each sample, and cells were resuspended. The tagmentation reaction was incubated at 37 C for 30 minutes, shaking at 800 rpm. 250 uL DNA purification binding buffer with sodium acetate was added to each sample, and DNA was

purified and eluted. Tagmented DNA was then PCR amplified and subjected to SPRI size selection. Libraries were quantified and paired-end Illumina sequencing was performed by MIT’s BioMicroCenter. ATAC-sequencing data was first aligned to the human genome hg38 using the tool BowTie, and peaks were called using Macs2. The universal peakset was sorted and merged, and a peak count matrix was created using BedTools. The tool HOMER was used to assign peaks to nearest genes, using the “annotatePeaks.pl” command. Differentially accessible regions were calculated using DESeq2. Transcription factor binding motifs were identified using HOMER, with the “findMotifsGenome.pl” command, using parameters of size 200, and using the peak universe raw counts count matrix as the background.

## Analysis of ATAC-sequencing on post-mortem human brain

In order to find peaks in snATAC-seq of post-mortem samples of the prefrontal cortex of aged individuals, we aggregated snATAC-seq fragments from 93 individuals into fragment files for each of seven major cell groups (astrocytes, microglia, oligodendrocytes, OPCs, vascular cells, and excitatory and inhibitory neurons), keeping cells passing QC at each of two different TSS enrichment thresholds (TSS > 1 and TSS > 6), as previously reported13 . We then removed unmappable and problematic regions using the umap kmer=50 annotation35 and the hg38 ENCODE blacklist (ENCFF356LFX)36 . We called peaks with MACS337 using “--call-summits --nomodel --extsize 147 -g hs -B -q 0.05” and counted the reads in peaks at the individual level using bedmap38 with --fraction-map 0.2. We used edgeR39 to perform differential peak calling in two conditions, presence of the APOE e4 allele and dosage (0/1/2) of the e4 allele in an individual, controlling for age, post-mortem interval, and sex. For differential peaks, we normalized using between-lane normalization in EDASeq40 , filtered for expressed peaks, and estimated dispersion using estimateGLMCommonDisp in edgeR. We called differential peaks as all peaks with adjusted p-value < 0.05. To find motif instances in the hg38 genome, we applied MOODS 41 with parameters “--p-value 4^(- motif\_length) --lo-bg 2.977e-01 2.023e-01 2.023e-01 2.977e-01” for a set of 1,690 motifs comprised of JASPAR 2018 core non-redundant vertebrate motifs42, HOCOMOCO v115643 , and SELEX motifs by Jolma et al44. We partitioned the motifs into 286 previously identified motif archetypes38 . To annotate peaks with motif instances, we intersected peaks with motifs using bedmap with --fraction-map 0.2. To test for motif enrichment in differential peaks, we first separated out up-regulated and down-regulated peaks for a given covariate, cell type group, and TSS QC threshold. We used a hypergeometric test to assess enrichment by comparing the number of peaks with a given motif in the differential set, the number of peaks with a motif in the overall peak set, the number of peaks in the differential set, and the total number of peaks in that cell type and QC threshold. We tested enrichment both for motifs and motif archetype, counted when seeing any of its constituent motifs, and adjusted p-values using the Benjamini-Hochberg correction within a peakset across all motifs and archetypes. We plot the enrichment in either up or down-regulated peaks depending on which is more significant or has a greater effect size (in that order), and flipped the sign of the log2FC for an enrichment in down-regulated peaks.

## Immunohistochemistry on APOE oligodendrocytes

Oligodendrocytes were plated into clear-bottomed 96 well plates at a density of 10,000 cells per well. Cells were fixed with 4% paraformaldehyde for twenty minutes at $4 ^ { \circ } \mathsf { C } .$ Cells were washed with ice-cold phosphate buffered saline (PBS) twice for ten minutes, and then blocked in buffer (PBS containing 0.03% Triton X and 1% Bovine Serum Albumin) for two hours at room temperature, gently shaking. Cells were incubated in primary antibody solution (Rabbit anti-GSK3-b, 1:500, or Rabbit anti-beta-catenin, 1:500) overnight at 4°C, gently shaking. Cells were washed with ice-cold PBS three times for ten minutes, and then incubated in secondary antibody solution (Donkey anti-Rabbit Alexa Fluor 595, 1:1000; Hoechst, 1:10000) for two hours at room temperature, gently shaking. Cells were then washed three times with icecold PBS and imaged on a Zeiss LSM 900 confocal.

## Drug treatment on APOE oligodendrocytes

APOE3 and APOE4 oligodendrocytes were plated into separate clear-bottomed 96 well plates, at a density of 10,000 cells per well. APOE3 oligodendrocytes were treated either with Dif3 (10 uM) or vehicle control (DMSO). APOE4 oligodendrocytes were treated with the GSK3b inhibitor CHIR99021 (1 uM) or vehicle control (DMSO). Media containing drug was changed every other day. After one week of treatment, cells were treated with BODIPY to label lipid droplets. The following day, media was changed and cells were fixed with 4% paraformaldehyde, for 20 minutes at 4C. Cells were subsequently washed with ice-cold PBS twice for ten minutes, and then imaged with a Zeiss LSM 900 confocal microscopy.

## Organelle imaging in APOE4 oligodendrocytes

APOE4 oligodendrocytes were plated into a clear-bottomed 96-well plate at a density of 10,000 cells per well, and allowed to recover for three days. Cells were then treated with MitoTracker and BODIPY overnight. The following morning, media was changed, and cells were imaged using a live confocal microscopy system on the Zeiss LSM 900, with a heated stage supplying continuous CO2 at 5%. All conditions were imaged using the same laser power and microscopy settings.

## Organoid generation and immunohistochemistry

Oligodendrocyte-containing organoids (“myelinoids”) were generated as previously described, from isogenic iPSC lines (Parental KOLF2.1J, homozygous for APOE3, and an isogenic line, CRISPR edited to be APOE4 homozygous). Myelinoids were grown in culture for 18 weeks, at which point some APOE4 myelinoids began treatment with CHIR99021 (2 uM in media). Myelinoids were fixed in 4% PFA for 3 hours and submerged sequentially in 10%, 20%, and 30% sucrose overnight at 4 degrees. After full submersion in 30% sucrose, spheroids were embedded in the OCT compound and serially sectioned at 40 μm thickness using RWD Minux FS800 cryostat. Myelinoid sections were permeabilized in PBS with 0.1% Triton X-100 (PBST) for 15 min and then blocked with 5% donkey serum in PBS (blocking buffer) for

3 hours at room temperature. Sections were then incubated with primary antibodies in blocking buffer at $4 ^ { \circ } \mathsf { C }$ overnight. Following primary antibody incubation and three 10 minute washes, sections were incubated with secondary antibodies at room temperature for 2 hours, counterstained with Hoechst, washed three times for 10 minutes, and mounted with Fluoromount aqueous mounting medium.

## Visible hyperspectral SRS imaging

Visible hSRS system45 utilized a dual-output laser (Insight X3, Spectra Physics) where the output wavelengths of 906 nm and 1045 nm were used to obtain 453 nm and 523 nm through second harmonic generation. Hyperspectral imaging was achieved using the spectral focusing method45 . We acquired the hyperspectral imaging data for the cells in the CH wavenumber region with 523 nm Stokes beam at 30 mW and 453 nm Pump beam at 20 mW. Furthermore, we applied Self-Supervised Elimination of Non-Independent Noise (SPEND) denoising to the hyperspectral data. SPEND is a self-supervised deep learning denoising framework for removing non-independent noises in hyperspectral images. Details can be found in46 . Then, we used the LASSO method for the spectral unmixing of the hyperspectral stack into chemical maps of lipid, protein, cholesterol, and RNA47 , using a least square fitting problem with L1-norm regularization with the parameter λ used to control each chemical component's sparsity level.

## APOE4;PS19 mouse experiments

All experiments were done in accordance with MIT’s Institute for Animal Care and Usage Committee. All mice were housed in a 12-hour light/dark cycle room, with access to food and water ad libitum. All mice were housed with littermates. APOE4;PS19 male mice (five months old) were injected intraperitoneally with sterile CHIR99021 (5 mg/kg, 100 uL) or 10% DMSO twice a week for two weeks. Separately, APOE4;PS19 female mice (eight months old) were injected intraperitoneally with sterile CHIR99021 (5 mg/kg, 100 uL), or 10% DMSO twice a week for six weeks. One day after the final injection, mice were anesthetized with gaseous isoflurane and transcardially perfused with ice-cold phosphate-buffered saline (PBS). Brains were dissected out and drop-fixed in 4% paraformaldehyde for 16 hours. Brains were subsequently re-hydrated in PBS, and sliced on a Leica vibratome at a thickness of 40 um. Floating sections containing hippocampus were collected for immunohistochemistry in 24-well plates. For lipid droplet staining, to preserve lipid structures as much as possible, sections were not permeabilized with blocking buffer. Instead, brain sections were directly incubated in PBS containing BODIPY (1:1000) and Hoechst (1:10,000) for two hours at room temperature, and then washed three times with ice-cold PBS. Sections were mounted on Fisher Scientific Superfrost Plus glass slides, with VWR coverslips (22x30 mm No.1). Sections were then imaged on a Zeiss LSM 900 confocal. Lipid droplets were quantified using the “Analyze Particles” feature of ImageJ FIJI. Mean intensity of immunohistochemical stains was analyzed using the “Measure” feature of ImageJ FIJI. Microglial morphology was analyzed using the “filament” feature of IMARIS software. All experimenters were blinded to genotype and treatment condition of the mice.

![](images/8efb4dc5cfcc52679371a981eb2a7eb5b2c93f38976e3eeea15202b15e1bb52a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["APOE4 oligodendrocytes"] --> B["Deliver gRNAs + Cas9"]
  B --> C["Label lipid droplets with BODIPY"]
  C --> D["Sort cells: Top 15% and Bottom 15% Detect gRNAs"]
```
</details>

B  
![](images/c9ae17102de5c63587482bac1b160d0d80f194fba6dd7f16f8f9f616b182f1af.jpg)

<details>
<summary>scatter plot</summary>

| Gene    | Log Fold Change (z-scored) |
|---------|----------------------------|
| ANKRD31 | -7.5                       |
| CDK7    | -5.0                       |
| FAM151B | -2.5                       |
| FAM228B | -5.0                       |
| FAM98C  | -2.5                       |
| NAPG    | -5.0                       |
| RPS6    | -2.5                       |
| RPS13   | -5.0                       |
| RPS18   | -2.5                       |
| ZSCAN26 | -5.0                       |
</details>

C  
![](images/2d07bad1272d59ac3b42af9203b32a78e5415fa51e6c9c1aa6a5a6b42c2f422c.jpg)

<details>
<summary>scatterplot</summary>

| Gene    | Log Fold Change (z-scored) |
|---------|-----------------------------|
| AKIRIN  | -5.0                        |
| KPNB1   | -2.5                        |
</details>

![](images/f779d88ded8cd65def30f0270c9867087a376d44a17db64d335873d01501bbb0.jpg)

<details>
<summary>natural_image</summary>

Microscopic fluorescence image showing cellular structures with blue and pink fluorescent markers (no text or symbols)
</details>

![](images/7bbbda17e4af0676bcf8066350592a170c564815021f70cf3be5cac073eb8532.jpg)

<details>
<summary>scatterplot</summary>

| Gene    | Z-scored average log fold change | -log10 adjusted p value |
|---------|----------------------------------|--------------------------|
| XNDC1N  | -2.5                             | 4.0                      |
| VAMP5   | -2.5                             | 4.0                      |
| PLA2G4C | -2.5                             | 3.5                      |
| PJA1    | -2.5                             | 3.5                      |
| DKK1    | -2.5                             | 3.0                      |
| NKD1    | -2.5                             | 2.5                      |
| TP53    | 2.5                              | 4.0                      |
| NRGN    | 2.5                              | 3.5                      |
| LRATD2  | 2.5                              | 3.0                      |
| APC2    | 2.5                              | 2.5                      |
| APOE    | 2.5                              | 2.0                      |
| FZD10   | 2.5                              | 1.5                      |
</details>

![](images/c12e321164e8ee213da5fe76be7bc05ab847f66b0d88c7c09bcb9514fe928a60.jpg)

<details>
<summary>chemical</summary>

Chemical reaction pathway showing phosphorylation of PLA2G4C to form glycerol and its intermediates, with key components labeled.
</details>

KEGG pathways (low lipid droplets):F

F  
![](images/aa305d11b81f6bc2b4392cec62e81463b0657eb775d4b0967881909dae79c6ed.jpg)

<details>
<summary>bar chart</summary>

| Category | Pathway c | Pathway d | Pathway e |
|---|---|---|---|
| Basal cell carcinoma | 0 | 6 | 0 |
| Glycerophospholipid | 4 | 0 | 0 |
| Viral-cytokine interaction | 0 | 0 | 4 |
| Complement cascade | 0 | 0 | 4 |
| Hippo signaling | 0 | 3 | 0 |
| TRP channels | 4 | 0 | 0 |
| Spinocerebellar ataxia | 0 | 0 | 1 |
| Wnt signaling | 0 | 2 | 0 |
| Cytokine receptor | 0 | 0 | 3 |
| NOD-like receptor | 0 | 0 | 2 |
</details>

KEGG pathways (high lipid droplets):G  
![](images/100c73e1731fa8101d74a4c1683e5c020ce1fbfb7f72af21d0122dec719ebd23.jpg)

<details>
<summary>bar chart</summary>

| Category | Fold Enrichment |
|---|---|
| Circadian rhythm | 5.0 |
| Basal cell carcinoma | 4.5 |
| Chagas disease | 3.5 |
| Atherosclerosis | 3.5 |
| Relaxin signaling | 3.5 |
| Cushing syndrome | 3.5 |
| Wnt signaling pathway | 3.0 |
| Oxytocin signaling | 3.0 |
| mTOR signaling | 3.0 |
| Shigellosis | 2.5 |
Contains phospholipases; Contains Wnt genes; Contains immune-related genes
</details>

![](images/7fc100c4bd9f05ba4f96827f3dfceba92539fb78ee2a25cdcca3327382ea2e84.jpg)

<details>
<summary>scatterplot</summary>

| Category | Log Fold Change | -Log10 adjusted p Value |
| -------- | --------------- | ---------------------- |
| Bulk RNA-seq on lipid-burdened oligos | -4 to 4 | -log10 adjusted p value |
| APOE4 oligodendrocytes | -4 to 4 | -log10 adjusted p value |
| Label lipids with BODIPY | -4 to 4 | -log10 adjusted p value |
| Sort cells | -4 to 4 | -log10 adjusted p value |
| TCF7L1 | 0 to 4 | -log10 adjusted p value |
| WNT7B | 0 to 4 | -log10 adjusted p value |
</details>

Validation of screen hits in APOE4 oligodendrocytes:J  
![](images/a29c93d45af55ee5cdf999576a3ce9234d5b8faf59d2f409be7663fb1e8140ee.jpg)

<details>
<summary>bar chart</summary>

| Group    | Lipid droplets per cell |
| -------- | ------------------------ |
| Control  | 2                        |
| WNT10A   | 3                        |
| FZD10    | 5                        |
| TCF7L1   | 4                        |
| WNT16    | 2                        |
| WNT7B    | 1                        |
| CTNNB1   | 1                        |
| DKK1     | 1                        |
</details>

![](images/50255cbcaffeee316b9b5cbeddc479ba7a17fbe213a8fa1a01abaa7d06e5e2dc.jpg)

<details>
<summary>text_image</summary>

Control
WNT10A-kd
FZD10-oe
TCF7L1-oe
WNT16-oe
WNT7B-oe
CTNNB1-oe
DKK1-kd
mCherry
Hoechst
BODIPY
</details>

Figure 1: Genome-wide CRISPR knockout screen reveals regulators of lipid droplet burden inFigure 1: Genome-wide CRISPR knockout screen reveals regulators of lipid droplet burden in APOE4 oligodendrocytes. APOE4 oligodendrocytes. every protein-coding ge

A, Schematic illustrating the experimental design. 90 million iPSC-derived oligodendrocytes were infected with a guide RNA libraryfor lipid droplets and FAC-sorted. Genomic DNA was harvested from both populations and used to calculate guide RNA enrichment. B, Mantargeting every protein-coding gene in the genome at a multiplicity of infection circa 0.3-0.5. Ten days after infection,hattan plot illustrating the relative abundance of every gene knockout in oligodendrocytes with low lipid burden. Each dot repres oligodendrocytes were stained for lipid droplets and FAC-sorted. Genomic DNA was harvested from both populations and used toage abundance of all guide RNAs targeting an individual gene. Highly depleted genes are labeled. C, Manhattan plot illustrating the relative calculate guide RNA enrichment. B, Manhattan plot illustrating the relative abundance of every gene knockout in oligodendrocytes with low lipid burden. Each dot represents the average abundance of all guide RNAs targeting an individual gene. Highly depletedper gene. Genes highly enriched in the oligodendrocytes with low lipid droplets are shown on the left, and genes highly enriched in the oligogenes are labeled. C, Manhattan plot illustrating the relative abundance of every gene knockout in oligodendrocytes with high lipiddendrocytes with high lipid droplets are shown in the right. E, Schematic illustrating several of the screen hits whose enzymatic activity is burden. Each dot represents the averaged abundance of all guide RNAs targeting an individual gene. Highly depleted genes arerelated to phospholipid metabolism. F, Enriched KEGG pathways from significant hits in oligos with low lipid droplets. G, Enriched KEGG labeled. D, Volcano plot showing the z-scored enrichment of guide RNAs, averaged per gene. Genes highly enriched in thepathways from significant hits in oligos with high lipid droplets. Pathways are colored according to whether they contain genes relat oligodendrocytes with low lipid droplets are shown on the left, and genes highly enriched in the oligodendrocytes with high lipidphospholipases (purple), Wnt signaling (blue), or immune-related genes (pink). H, Schematic illustrating experimental design where APOE droplets are shown in the right. E, Schematic illustrating several of the screen hits whose enzymatic activity is related to phospholipid metabolism. F, Enriched KEGG pathways from significant hits in oligodendrocytes with low lipid droplets. G, Enrichedinclude Wnt-signaling related genes. J, Quantification and representative images of hit validation. APOE4 oligodendrocytes were infected KEGG pathways from significant hits in oligodendrocytes with high lipid droplets. Pathways are colored according to whether theywith lentivirus to overexpress (oe) or knockdown (kd) Wnt related genes. Lipid droplets are labeled with BODIPY (yellow). Virus expression contain genes related to phospholipases (purple), Wnt signaling (blue), or immune-related genes (pink). H, Schematic illustratingis shown with mCherry (pink). Nuclei labeled with Hoechst (blue). Each dot represents an individual experiment. This experiment was repeatexperimental design where APOE4 oligodendrocytes were labeled with BODIPY and FAC-sorted based on lipid content, anded several times. subjected to bulk RNA sequencing of both sorted populations. I, Volcano plot illustrating differentially expressed genes in oligodendrocytes with low (left) versus high (right) lipid burden. Labeled genes include Wnt-signaling related genes. J, Quantification and representative images of hit validation. APOE4 oligodendrocytes were infected with lentivirus to overexpress (oe) or knockdown (kd) Wnt related genes. Lipid droplets are labeled with BODIPY (yellow). Virus expression is shown with mCherry (pink). Nucle labeled with Hoechst (blue). Scale bar represents 20 um. Each dot represents an individual experiment. This experiment was repeated several times.

A  
![](images/ccb3670e048f794cfd7d0e38ecc272119b6cfd635c95225ccf696aa94d703156.jpg)

<details>
<summary>line chart</summary>

| Gene    | APOE3 oligodendrocytes | APOE4 oligodendrocytes |
|---------|------------------------|------------------------|
| WNT6    | 0                      | 0                      |
| WNT10A  | 0                      | 0                      |
| PLA2G2A | 0                      | 0                      |
</details>

B

Total = 47999 DARs  
![](images/1178c60f0afc2ce1876400ac1cdcc889ab361affdd9cb10c5d2bb730e3277540.jpg)

<details>
<summary>pie chart</summary>

| Category | Value |
|---|---|
| Intron | 40.0% |
| Intergenic | 28.0% |
| Promoter-TSS | 1.0% |
| TTS | 1.0% |
| Exon | 1.0% |
| 3' UTR | 1.0% |
| Non-coding | 1.0% |
| 5' UTR | 1.0% |
</details>

C  
![](images/c389f7477339e306f89a019915a9a359be42bb23ce165137c36e0c5aa7128a71.jpg)

<details>
<summary>scatterplot</summary>

| Gene    | Fold Change (Accessibility) | -log10 p value |
|---------|-----------------------------|----------------|
| RPTOR   | -2.5                        | 8              |
| MBP MOG WNT3 | -1.5                      | 12             |
| PLCZ1   | 1.5                         | 15             |
| PLBD2 PLA2G2A | 3.0                     | 25             |
</details>

D  
Decreased accessibility in APOE4  
![](images/8a6a9fea9913a5b231ed6b433374a5590a90838c8945cce16f1c4192aab7c97b.jpg)

<details>
<summary>text_image</summary>

TF binding motifs: p value:
c-MYC CCGCAGTCG 1 e-161
TCF7 CTTTGATGTGGT 1 e-94
LEF1 CCTTTGATCT 1 e-18
</details>

E  
![](images/1effb089d1dc43b024bcf4aa84cdd45f3fd1dc56d363683c37f692b6936ec838.jpg)

<details>
<summary>scatter plot</summary>

| Enriched pathways (KEGG) | -log10 P value |
| ------------------------ | -------------- |
| Basal cell carcinoma     | 3.5            |
| Wnt signaling            | 2.8            |
| Glycerophospholipids    | 2.2            |
| Cholesterol metabolism  | 1.5            |
</details>

![](images/6c274e6e2312f70de418a72c36c032aa6ed4a3508f5effb46a9614a58df80784.jpg)

<details>
<summary>heatmap</summary>

| TP53 | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CDKN1A | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| WNT10A | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| APC2 | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| WNT16 | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| JUN | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| FGF8 | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| NKD1 | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| FBXW11 | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| VANGL1 | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
| PLCB2 | Basal cell c... | Circadian in... | Glycerophio... | Armyrinmot... | Blacko con... | Hippo sigma... | Hypertrophin... | Alpha-1ind... | Breast can... |
</details>

G

Human brain ATAC-seq (Xiong et al, 2023)  
![](images/cdee84027a5aa7b90061c866107300d24fe077c983447b0513464359d79f3c24.jpg)

<details>
<summary>heatmap</summary>

| Gene | Has e4 | Has e4 | Has e4 | Has e4 | Has e4 | Has e4 | Has e4 | Has e4 | Has e4 |
|---|---|---|---|---|---|---|---|---|---|
| LEF1 (archetype) | * | * | * | * | * | * | * | * | * |
| LEF1_HUMAN.H11MO.0.A | * | * | * | * | * | * | * | * | * |
| ZN350_HUMAN.H11MO.0.C | * | * | * | * | * | * | * | * | * |
| TCF/LEF (archetype) | * | * | * | * | * | * | * | * | * |
| LEF1_HMG_1 | * | * | * | * | * | * | * | * | * |
| LEF1_MA0768.1 | * | * | * | * | * | * | * | * | * |
| TCF7_HUMAN.H11MO.0.A | * | * | * | * | * | * | * | * | * |
| Tcf7_MA0769.1 | * | * | * | * | * | * | * | * | * |
| TCF7L1_HMG_1 | * | * | * | * | * | * | * | * | * |
| TCF7L1_MA1421.1 | * | * | * | * | * | * | * | * | * |
| TCF7L2_MA0523.1 | * | * | * | * | * | * | * | * | * |
| TF7L2_HUMAN.H11MO.0.A | * | * | * | * | * | * | * | * | * |
| Log2FC (Up-reg difftl. peaks) - p-value < 0.05; adj. p-value < 0.1; <10 difftl. peaks containing motif - Down-reg difftl. peaks
</details>

H  
TF binding motifs:

![](images/5839d52268ee5f65339cf78bc3c5ff67a206f76c7aa3f605c69413b7ec0a859f.jpg)

Beta-catenin expression:I APOE3 oligodendrocytes  
![](images/84612b6d61ef872522bf74aa7a93131ded110a708a9d76911f1963637759063a.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of stained biological cells with purple and blue staining (no text or symbols visible)
</details>

Beta-catenin

![](images/53ed37218887c3cf49d3a22b2d0a18a20c0b49cc51f071fe5a1cea972652902e.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy image showing blue-stained cell nuclei against a purple background, labeled 'APOE4 oligodendrocytes' (no additional text or symbols)
</details>

![](images/3213eafff5b6dbb9ff4d0f4df798f2550dfbdfa8ff13cd3b3993677155e11a7f.jpg)

<details>
<summary>bar chart</summary>

| Group   | Beta-catenin (intensity) |
| ------- | ------------------------ |
| APOE3   | 6000                     |
| APOE4   | 4000                     |
</details>

J

![](images/8c7d7d690c877d7a471fef9c270420c9b8b5afab0f1e9e661f3804814c9376bc.jpg)

<details>
<summary>text_image</summary>

GSK3b expression:
APOE3 oligodendrocytes
GSK3b
</details>

![](images/cda574874e3842b5422c25da3402dd34986a87fea654435ea96c671643e6ef26.jpg)

<details>
<summary>text_image</summary>

APOE4 oligodendrocytes
</details>

![](images/7e0610fa29a3f97c487e400d14b32b8be23a6745e2831dac64fcbd42207ae0c4.jpg)

<details>
<summary>bar chart</summary>

| Group   | GSK3b (mean intensity) |
| ------- | ---------------------- |
| APOE3   | 16                     |
| APOE4   | 22                     |
</details>

Figure 2: ATAC-sequencing reveals Wnt signaling is depressed in APOE4 oligodendrocytes

A, Pie chart illustrating the differentially accessible regions between APOE3 and APOE4 isogenic oligodendrocytes. B, Representative traces illustrating differentially accessible regions between APOE3 and $\mathsf { A P O E 4 }$ isogenic oligodendrocytes. C, Volcano plot showing the differentially accessible regions mapped onto protein-coding genes. D, Transcription factor binding motifs significantly enriched in regions of the genome less accessible in APOE4 oligodendrocytes. P value calculated using False Discovery Rate. E, Overlap between genes that are CRISPR screen hits and differentially accessible between APOE genotypes. This set of genes was queried for enriched KEGG pathways. F, Overlapping genes associated with enriched KEGG pathways. Pathways containing Wnt related genes are shown in blue. Pathways containing phospholipases are shown in purple. G, Transcription factor motif enrichment from ATAC-seq of the human post-mortem brain, comparing enrichment of Wnt motifs in differential peaks across individuals, stratified by e4 carrier status or e4 dosage. Cell types were evaluated at two TSS enrichment thresholds, only cell types with results with nominal $\mathsf { p } < 0 . 0 5$ are shown. H, Logos for the enriched motifs, grouped into two archetypes. I, Representative images and quantification of immunoreactivity to beta-catenin (purple) n in cultures of isogenic APOE3 and APOE4 iPSC-derived oligodendrocytes. P value calculated using an unpaired, two-tailed student’s t-test. Each dot represents a separate culture. Scale bars represent 10 um. J, Representative images and quantification of immunoreactivity to GSK3b (cyan) in cultures of isogenic APOE3 and APOE4 iPSC-derived oligodendrocytes. P value calculated using an unpaired, two-tailed student’s t-test. Each dot represents a separate culture. Scale bars represent 20 um.

A  
![](images/b76eabd8b9e56a53ca73a350f6565ab84f8f9a815cc8373f1ea2550d0bd24961.jpg)

<details>
<summary>bar chart</summary>

| Condition | Lipid droplets per cell |
| --------- | ------------------------ |
| APOE3     | 0.0093                   |
| + DI3     | 8.0                      |
</details>

C

![](images/d18e49a19abd3333db88f3d765cb4fd22de7945bb31e643e91d175990836bf0d.jpg)

<details>
<summary>scatterplot</summary>

| Pathway | Enrichment Score | Category |
| --- | --- | --- |
| Colorectal cancer (TCF7L1, MTOR) | ~-5 | Downregulated |
| Lysosome (ABCA2, NAPSA) | ~-5 | Downregulated |
| Glycosphingolipids (B4GALT3; B4GALT1; ST3GAL5) | ~2 | Upregulated |
| Cholesterol metabolism (CETP; LCAT; LDLR) | ~1 | Upregulated |
| Glycerophospholipids (LPGAT1, LPCAT2) | ~1 | Upregulated |
</details>

E  
![](images/8b03c41c7c6659912eebae352e52e8dc8477d71aaa6a2acd7cdfbd4e8cc34759.jpg)

<details>
<summary>bar chart</summary>

| Cell Line | LDs in MitoTracker (%) |
| --------- | ---------------------- |
| POE4      | ~15                    |
| CHIR      | ~100                   |
</details>

![](images/b5b58f0ea132f75ad841ea88302082e095d9953d2f2629bd697eb5ccb4c742b2.jpg)

<details>
<summary>text_image</summary>

APOE4 myelinoid
20 weeks
+ GSK3b inhibition
20 weeks
Neurofilament
Hoechst
Olig2
Myelin Basic Protein
</details>

B  
![](images/a14c6d15895a5cee45ccd7aa8e301e54a92f157764c23b5e6d6323a86d471169.jpg)

<details>
<summary>bar chart</summary>

| Group | Hoechst (Lipid droplets count) |
|-------|-------------------------------|
| APOE4 + CHIR | 60 |
| + GSK3b inhibition | 20 |
</details>

D

![](images/6c6e8577f52088ba535bcf63d58d40b704bb23820d828818f907a8747451d7ed.jpg)

<details>
<summary>scatterplot</summary>

| Pathway | Gene/Pathway | Erichment score | Count |
|---------|--------------|-----------------|-------|
| Ribosome | (RPL5, RPL30) | ~0.5 | ~15 |
| Oxidative phosphorylation | (NDUFA11, NDUFA12) | ~0.8 | ~10 |
| Autophagy | (LAMP1, LAMP2, ATG4A) | ~1.2 | ~5 |
| Downregulated pathways | (RB1, TP53) | ~-6 to -2 | ~20 |
| Upregulated pathways | (RPL5, RPL30) | ~-2 to 3 | ~10 |
| Cell cycle | (RB1, TP53) | ~-7 to -3 | ~15 |
| Cholesterol synthesis | E, HMGCS1, MVK | ~-8 to -1 | ~5 |
</details>

F  
![](images/42d8f79ad314e4abd192a032e92fa5bcfa9ad50b359b3e853da9c970eb19e6a1.jpg)

<details>
<summary>scatterplot</summary>

| Group | BODIPY-PC (mean intensity) |
|-------|-----------------------------|
| BPOE4 | 60                          |
| CHIR  | 40                          |
</details>

H  
![](images/d31f5d8d704b63cff2d10233dec76b75bdbf481a3fc6eadd2de798af43e1c4b4.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Group | MYelin Basic Protein (MBP area/total area) | Olig2 (MBP area/total area) |
|-------|---------------------------------------------|-----------------------------|
| APOE4 | 0.3                                         | 0.7                         |
| + CHIR | 0.8                                         | 1.1                         |
</details>

Figure 3: GSK3b activity regulates lipid droplet burden and myelination in oligodendrocytes  
A, Treatment with GSK3b activator “Dif3” in APOE3 oligodendrocytes. Representative images and quantification of BODIPY (lipid droplet) staining in yellow; nuclei (Hoechst) in blue. Each dot represents an individual culture. P values calculated using two-tailed student’s t-test. Scale bar 10 microns. B, Treatment with GSK3b inhibitor CHIR99021 (1 uM) in APOE4 oligodendrocytes. Representative images and quantification of BODIPY (lipid droplet) staining in yellow; nuclei (Hoechst) in blue. Each dot represents an individual culture. P values calculated using two-tailed student’s t-test. Scale bar 10 microns. C, Volcano plot showing enriched KEGG pathways from bulk RNA-sequencing of APOE3 oligodendrocyte cultures treated with GSK3b activator “Dif3”. Relevant KEGG pathways are labeled. D, Volcano plot showing enriched KEGG pathways from bulk RNA-sequencing of APOE4 oligodendrocyte cultures treated with GSK3b inhibitor “CHIR99021”. Relevant KEGG pathways are labeled. E, Representative images of APOE4 oligodendrocytes treated with GSK3b inhibitor CHIR99021. Mitochondria are labeled with MitoTracker (magenta), lipid droplets are labeled with BODIPY (yellow) and nuclei with Hoechst (blue). Each dot represents and individual culture. P values calculated using two-tailed student’s t-test. F, Representative images and quantification of APOE4 oligodendrocyte cultures treated with GSK3b inhibitor CHIR99021. BODIPY C11-glycerophosphocholine is labeled in green fluorescence. Each dot represents an individual culture. P value calculated using two-tailed student’s t-test. G, Representative images of APOE4 myelinoids, showing control (left) and CHIR99021-treated (right). Axons are stained with neurofilament (magenta), myelin with Myelin Basic Protein (cyan), Olig2 (yellow) and nuclei with Hoechst (blue). Scale bar. H, Representative images and quantification of immunoreactivity to Myelin Basic Protein

(cyan) in APOE4 control and CHIR99021-treated myelinoids. Each dot represents the average of three images from individual myelinoids. P value calculated using two-tailed student’s t-test.

A  
![](images/0bbd0fb6a02c0c53d7c270ebc0bc9e9a4bba085c9a1b0392adae20f76653de19.jpg)

![](images/39d7e845ded4547fb34c4ed63aac9e151cb4be379dab38f74bc09ddfd1ac1337.jpg)  
Myelin Basic Protein

![](images/1d830017afa617666756db13568f9c7348f33fb42c8dfe15b6869acc0b42c338.jpg)

<details>
<summary>bar chart</summary>

| Group   | MBP (mean intensity) |
| ------- | -------------------- |
| APOE3   | 210                  |
| APOE4   | 220                  |
</details>

![](images/63e99c11bad5594d0b8e2e2f551f7217898332a09c9a05576f300029e4497431.jpg)

![](images/06bb63c14ff4ac9f148e102dfb91b68aa08528905ab9a640d5db89adeef88d83.jpg)  
Bodipy (neutral lipids)

![](images/e6d210c0438872f9ac7a11848ebf2f7ecfd839803cacb0c7c51484ed8b63af09.jpg)

![](images/07e3c728aeb5d570064008534c9f685c7e8ec0a851a7a6c04e87bcd5ec31695b.jpg)

![](images/f21c591297741136e7128d74cbf48c1aa22277fd19c1407afc7dcd487aea9d4f.jpg)

![](images/cbc6fdaf26e398392cd6ab7b147edf21c2111f2cf3786e888b9d55f0bdd321f8.jpg)

C  
![](images/f21f44fb2aa4dd96174f84487ba050cc7b128d71a22c5cf3677dd863448d1f34.jpg)

<details>
<summary>bar chart</summary>

| Time Point | Group   | Lipid droplets (count) |
| ---------- | ------- | ---------------------- |
| 3 months   | APOE3   | ~100                   |
| 3 months   | APOE4   | ~100                   |
| 6 months   | APOE3   | ~100                   |
| 6 months   | APOE4   | ~100                   |
| 10 months  | APOE3   | ~100                   |
| 10 months  | APOE4   | ~1000                  |
</details>

![](images/a453c4b083b48c926f2456fe7698db7e25b847fa0f2b5f93c4f39bf50bbbb98c.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological sample with blue staining, labeled 'APOE4;P301S (control)' and a white square marker (no readable text or symbols)
</details>

BODIPY (neutral lipids)

![](images/6c35df6f74c5925cea69469fbd353876aef16c70a05e913bde8a8281d0779d27.jpg)

<details>
<summary>text_image</summary>

APOE4;P301S + GSK3b inhibitor
</details>

![](images/e70e31e96ba2dbf51b06e8c9e1706902e3c0d65d1ef9747a0cb497c8df05847a.jpg)

<details>
<summary>natural_image</summary>

Microscopic tissue section stained purple, showing cellular structures with a highlighted region (no text or symbols present)
</details>

![](images/6444c3e94df2e8d52eb3116da1ce608d2139a946625f18521f7c99750d881756.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a biological sample with purple staining, labeled 'APOE4:P301S (control)' and a blue square marker (no text or symbols within the image content)
</details>

Myelin Basic Protein

E  
Hippocampus (5 month old mice, 2 weeks treatment)  
![](images/1a35c7cef89f475fb566588dba3b5cbed634b141f0a6af192494b7cbf25396ac.jpg)

<details>
<summary>natural_image</summary>

Microscopic image showing cellular structures with fluorescent markers, labeled 'APOE4;P301S (control)' in top left corner (no other text or symbols)
</details>

BODIPY (neutral lipids)

![](images/e51228c71e9e4cc2f9cf826de8c9c722f6ec43cbb139dfb4c1b6971530b86dbd.jpg)

<details>
<summary>text_image</summary>

APOE4;P301S + GSK3b inhibitor
</details>

![](images/859e7d0100925837b707ec44f9eb33f174947fc1180a5f408626f9b923d54625.jpg)

<details>
<summary>bar chart</summary>

| Group | Lipid droplets (count) |
|-------|------------------------|
| Control | 65 |
| +GSK3b inhibitor | 25 |
</details>

G  
Hippocampus (8 month old mice, 6 weeks treatment):  
![](images/9da21589e4f1270235dec8a1cc80dc90ca570dc084694bac9fd02beef68727e8.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of APOE4;P301S (control) tissue with purple staining, showing fibrous structures against a dark background (no text or symbols)
</details>

Myelin Basic Protein

![](images/d85a46e092f6f50cfc2f680797129047d558a9cad51f6c24483d2b34a9a7ccb8.jpg)

<details>
<summary>natural_image</summary>

Microscopic image of a neuron with visible dendrites and axon, labeled APOE4;P301S + GSK3b inhibitor (no text or symbols on the neuron itself)
</details>

![](images/99080a28ffded50983350cc10c8263298f1e6cc5dc12d73f8b6eafdefb68538f.jpg)

<details>
<summary>bar chart</summary>

| Group | MBP (mean intensity) |
|-------|----------------------|
| Control | 30 |
| +GSK3b inhibitor | 35 |
</details>

Figure 4. GSK3b inhibition reduces lipid droplets and increases myelination in an APOE4;Tau mouse model

A, Myelin basic protein immunohistochemistry (magenta) and nuclei with Hoechst (blue) in the hippocampus of APOE3;PS19 mice and APOE4;PS19 mice. Each dot represents an individual mouse. P value indicates two-tailed student’s t-test. B, Lipid droplet staining with BODIPY (yellow) and nuclei with Hoechst (blue) in the hippocampus of APOE3;PS19 and APOE4;PS19 mice at 3 months, 6 months and 10 months of age. C, Quantification of lipid droplet number in the hippocampus of APOE3;PS19 and APOE4;PS19 mice at 3, 6, and 10 months of age. Each dot represents an individual mouse. Statistical comparisons were performed by comparing genotypes at the same age using a two-tailed student’s t-test. D, Representative images showing lipid droplet staining (with BODIPY) in the hippocampus of control and treated APOE4;PS19 mice. E, Images and quantification of lipid droplets in the hippocampus of control (left) and treated (right) APOE4;PS19 mice. Each dot represents an individual mouse. P value was calculated using a two-tailed student’s t-test. F, Representative images showing immunoreactivity to myelin basic protein (magenta) in the hippocampus of control (left) and treated (right) APOE4;PS19 mice. G, Representative images and quantification of myelin basic protein immunoreactivity in control (left) and treated (right) APOE4;PS19 mice. Each dot represents and individual mouse. P value calculated using a two-tailed student’s t-test.

Extended Data, Figure 1  
A iPSC-derived oligodendrocytes:  
![](images/9340458aff9031f3fb36f4e56aaf5820886c76888e43fee03054dcea990b1b72.jpg)

![](images/20c7bb1f345e7975c60e202ab8fcea12d52df058ad69ac9dd615220eb4127797.jpg)

![](images/1e9efda53d80192bc58a4947f02c649fd86963ac374beb1bdc1141420f667e9d.jpg)

![](images/a4e3f65c787625dc03fc99306f3cc28e362c789dae3a9452c0fc7bc64350db10.jpg)

B  
![](images/783b0209c7d71f52ab68b5a03917554055eef12c0de6a026642e10b25704b022.jpg)

C  
![](images/b889ac46de9585cba51b399986990c70aa3253e84d41d476376f697623c48c30.jpg)

D  
![](images/69163b47016117f6ff08aec997610da977186ec2594e1f625264fd043ad85283.jpg)

E  
![](images/5e4eeb02ea74c90f725483891a4165239db700e6ae07773acf4215df76b0ea13.jpg)

F  
![](images/449dac3d7964a2ca50db9a64ead32ebfb78a89e604f4913dc46f8b9634180e9c.jpg)

<details>
<summary>scatterplot</summary>

| FSC-A | PTCA-A | BODIPY Status |
|-------|--------|---------------|
| 50    | 10^3   | BODIPY high   |
| 100   | 10^3   | BODIPY high   |
| 150   | 10^3   | BODIPY high   |
| 200   | 10^3   | BODIPY high   |
| 250   | 10^3   | BODIPY high   |
| 50    | 10^-3  | BODIPY low    |
| 100   | 10^-3  | BODIPY low    |
| 150   | 10^-3  | BODIPY low    |
| 200   | 10^-3  | BODIPY low    |
| 250   | 10^-3  | BODIPY low    |
</details>

G  
![](images/a6c9aec21ac490bde9638f0f659414841436d5b0a4b2e04ed378234766507f76.jpg)

<details>
<summary>histogram</summary>

| pDNA library z-scored lognorms | Count |
| ------------------------------ | ----- |
| -4 to -3                       | 0     |
| -3 to -2                       | 500   |
| -2 to -1                       | 1500  |
| -1 to 0                        | 3500  |
| 0 to 1                         | 5500  |
| 1 to 2                         | 4500  |
| 2 to 3                         | 2000  |
| 3 to 4                         | 500   |
</details>

H  
![](images/7ec9171f61c46978d786d4d43b411dae1234005d15dfb2fdbe0f5604694b8c18.jpg)

<details>
<summary>line chart</summary>

| Constructs ranked by abundance | Fraction of total represented |
| ----------------------------- | ---------------------------- |
| 0                             | 0                            |
| 0.5                           | 0.5                          |
| 1                             | 1                            |
</details>

I  
![](images/40391197927d63bae9b77b0f2caa8bd25e15f027e4c5954612e144ab0b6d2517.jpg)

<details>
<summary>scatterplot</summary>

| Target Gene | Enrichment (z-scored) |
|-------------|------------------------|
| XNDC1N      | 2.3                    |
| VAMP5       | 1.5                    |
| PLA2G4C     | 1.0                    |
| PJA1        | 1.0                    |
| PTPNB       | 1.0                    |
| LOC388R82   | 1.5                    |
| ASCL1       | 1.0                    |
| DKKY        | 1.0                    |
| CRTAC1      | 1.0                    |
| MSGN1       | 1.0                    |
</details>

J

![](images/2caa3460362657ecfef492087c26cadf63331942dc20c964f7fb0c7da388c0d6.jpg)

<details>
<summary>scatter plot</summary>

| Gene    | Enrichment (z-scored) |
|---------|------------------------|
| TP53    | 2.0                    |
| NRCN    | 1.5                    |
| LRAID2  | 1.0                    |
| MCRS1   | 1.0                    |
| BMAL2   | 1.0                    |
| ZFP57   | 1.0                    |
| IGFN1   | 1.0                    |
| C6orf118| 1.0                    |
| APC2    | 1.0                    |
</details>

![](images/fa763bedab44886d9d60f1661ab09108a64d55e9d7009a5e528c33bff6bbae67.jpg)

<details>
<summary>scatterplot</summary>

| FSC-A (x 1,000) | BODIPY A-AI Events (x 1,000) |
| --------------- | ---------------------------- |
| 50              | 200                          |
| 100             | 250                          |
| 150             | 300                          |
| 200             | 350                          |
| 250             | 400                          |
</details>

L  
![](images/a1fbb85daf113f35ad52d249b0365aecf5d04d428fe74de8e93e35ef3fca61d4.jpg)

M  
![](images/2099d06e4f4c61ad7d3711e14218afba7d053e318d46ec4657ded76afa9b9e08.jpg)

![](images/849524ea60cf05cafcc4c482425e48c9762e6a104b597be4a660fd706d04e529.jpg)

O  
![](images/81545be0ac49513713d0589881a994eb3751522566120ce7831f5ed0a9771053.jpg)

P  
![](images/5be9dcebde913350609ae8f3e87414458054119b1f01b46f2a514efd3c867a66.jpg)

<details>
<summary>histogram</summary>

| FITC-A Range | Count |
| ------------ | ----- |
| P6 - 10^2    | ~0    |
| P5 - 10^3    | ~200  |
</details>

Q  
RT-qPCR for WNT gene oe  
![](images/d8447574743dcf93921db773560d5ce393163f926a1d772b31c16940720eef6f.jpg)

<details>
<summary>bar chart</summary>

| GENE     | CQ        |
| -------- | --------- |
| WNT7B    | 10^12     |
| WNT16    | 10^0      |
| TCFZL1   | 10^0      |
| FZD10    | 10^0      |
| C7NNB1   | 10^0      |
| WNT10A   | 10^0      |
| DKK1     | 10^0      |
</details>

![](images/1f7e376679963b60267c529dec737887bfa33892eca6e94989bda530db57ae96.jpg)

<details>
<summary>natural_image</summary>

Fluorescent microscopy image showing stained cells with blue nuclei and purple cytoplasmic markers (no text or symbols)
</details>

## Extended Data Figure 1

A, Representative images showing immunoreactivity to oligodendrocyte lineage markers in iPSC-derived oligodendrocytes. B, FACS plots showing gating for live cells. C, Gating for debris. D, Gating for singlets. E, Distribution of BODIPY (FITC-A) signal in cells. F, Distribution of cells with high(top) and low (bottom) BODIPY signal. G, Distribution of plasmid DNA in reference library. H, Cumulative distribution of reference library. I, J, Guide RNA enrichment per target gene for the top ten most enriched genes in cells with low lipid droplets (top) and high lipid droplets (bottom). Each dot represents an individual guide RNA. K, FACS plots showing gating for cells. L, Gating for Debris. M. Gating for singlets. N, Gating for. P, FACS plot showing distribution of $B O D | \bar { \mathsf { P Y } }$ signal in sorted cells. Q, CQ values for $R \bar { \mathsf { T } } { \mathsf { - q P C R } }$ for gene expression of manipulated genes.

Extended Data, Figure 3  
![](images/715ccbb145bbc48b5cd90c17f83e76be26d7fde7cb706785e14efd7cd8a2f79f.jpg)

<details>
<summary>line chart</summary>

| Sites | APOE3 oligo | APOE4 oligo |
|-------|-------------|-------------|
| -1.5 kb | 0 | 0 |
| TSS 1.5 kb | 20 | 15 |
</details>

B PCA: APOE genotype  
![](images/f624e3255af5cc0126ef76fdd2b3a4178fc25d1d2e065d646564cb84169101f3.jpg)

<details>
<summary>scatterplot</summary>

| Principal Component | Principal Component #1 [92%] | Principal Component #2 [7%] |
| ------------------- | ---------------------------- | --------------------------- |
| -0.54               | -0.48                        | -0.48                       |
| -0.46               | -0.46                        | 0.50                        |
</details>

Transcription Start Site Enrichment scores:C  
Fraction of Reads in Peak:D

APOE3 (Replicate 1) | 23.7

APOE3 (Replicate 2) | 36.3

APOE4 (Replicate 1) | 18.4

APOE4 (Replicate 2) | 32.3

APOE3 (Replicate 1) | 0.61

APOE3 (Replicate 2) | 0.63

APOE4 (Replicate 1) | 0.53

APOE4 (Replicate 2) | 0.56

E  
![](images/38a53807fbb9eb1a2addaad3a473761357a7a22c24a50abd048b321e847bc8a9.jpg)

<details>
<summary>bar chart</summary>

| Category | Subgroup | Value |
|---|---|---|
| Inh TSS6 (e4 dose) | LEF1 | 228/2725 |
| OPC TSS6 (Has e4) | TCF7L1_MA1421.1 | 23/331 |
| OPC TSS6 (e4 dose) | TCF7L1_HMG_1 | 23/331 |
| Exc TSS1 (e4 dose) | LEF1_HUMAN.H11MO.0.A | 329/7528 |
| Ex_TSS1 (e4 dose) | LEF1 | 368/7528 |
| Inh TSS6 (e4 dose) | ZN350_HUMAN.H11MO.0.C | 164/2725 |
| Inh TSS6 (e4 dose) | TCF7_HUMAN.H11MO.0.A | 139/2725 |
| Exc TSS1 (e4 dose) | ZN350_HUMAN.H11MO.0.C | 215/7528 |
</details>

## Extended Data, Figure 2

A, Genome-wide accessibility in isogenic APOE3 (left) and APOE4 (right) iPSC-derived oligodendrocytes. B, PCA plot showing ATAC-sequencing. Replicates cluster by APOE genotype. C, Transcription start site enrichment scores of each replicate used for ATAC-sequencing. D, Fraction of reads in peaks calculated for each replicate used for ATAC-sequencing. E, Log2 fold change for significant enrichments of Wnt motifs in cell type-specific differential peaks for e4 dosage and carrier status. Bars are labeled with the number of differential peaks with a motif over the total number of differential peaks.

![](images/6fae8ac77d2ad6e158aeb3b2e6cf3c755b79e190e82c3168e603988edd535f8a.jpg)

<details>
<summary>text_image</summary>

ioRxiv preprint doi: https://doi.org/10.1101/2025.10
(which was not certified by peer review)
</details>

A

![](images/c24dacb472fd6ab074289c7def20f1dd35d6aa995c2404766606390eb6632343.jpg)

<details>
<summary>bar chart</summary>

| Condition | Phospholipids Raman Intensity (a.u.) | Cholesterol Raman Intensity (a.u.) |
| --------- | ----------------------------------- | --------------------------------- |
| APOE4 + GSK3b inhibition | 0.15 | 0.4 |
| APOE4 + CHIR | 0.12 | 0.2 |
</details>

B  
![](images/c88b5c2558953ba63e60ef2da1c8705a548eeb5ae74cd1d26a721c6de0523610.jpg)

<details>
<summary>bar chart</summary>

| Gene    | Log Fold Change |
|---------|-----------------|
| SREBF1  | -1.4            |
| HMGCS1  | -0.6            |
| SREBF2  | -0.3            |
| LSS     | -0.2            |
| SQLE    | -0.2            |
| MVD     | -0.2            |
| MVK     | -0.2            |
</details>

C  
BODIPY-LysoTracker colocalization  
![](images/99b7a3770bad8d4f9d5b59a4c3414950749821b028b9472c1b98467b723c684c.jpg)

<details>
<summary>bar chart</summary>

| Group   | Mean Intensity (LysoTracker) |
| ------- | ---------------------------- |
| APOE4   | 5                            |
| +CHIR   | 3                            |
</details>

D  
APOE3 myelinoids (week 20) APOE4 myelinoids (week 20)  
![](images/f4e1475f1155d4ecfebe79ce2b4238cc43199dc79ea467f363ad41e409c6c355.jpg)

<details>
<summary>natural_image</summary>

Fluorescence microscopy images comparing Hoechst and Myelin Basic Protein staining (no text or symbols present)
</details>

![](images/4b7269a8b7c2ddf2e7e0772c88a3ce7c64523af3740d4af3c75647e3b4fa7e65.jpg)

<details>
<summary>bar chart</summary>

| Group  | MBP area/total area |
| ------ | ------------------- |
| APOE3  | 1.0                 |
| APOE4  | 0.3                 |
</details>

E  
APOE4 myelinoids  
![](images/ccf8635d274fc7a281dba22530a871ddec26b7d54cf86fbf169aae2108923568.jpg)

<details>
<summary>bar chart</summary>

| Group   | OLIG2+Nuclei/Total Nuclei |
| ------- | -------------------------- |
| APOE4   | 0.3                        |
| +CHIR   | 0.5                        |
</details>

F  
![](images/38adffc48b8fc208d557f8a8de0cf8af1a62d583aa084085372c1567a33bceff.jpg)

<details>
<summary>bar chart</summary>

| Group        | Neurofilament (mean intensity) |
| ------------ | ------------------------------ |
| APOE4        | 750                            |
| APOE4 + CHIR | 1200                           |
</details>

## Extended Data, Figure 3

A, Stimulated Raman Scattering on cultures of APOE4 iPSC-derived oligodendrocytes, showing control (top) and CHIR99021-treated (bottom). SRS signal is shown for phospholipids (middle row) and cholesterol (right row). Raman intensity was calculated per lipid droplet. B, Gene expression (log fold change) of canonical cholesterol synthesis enzymes genes, in APOE4 oligodendrocytes with and without CHIR99021 treatment. C, Quantification of BODIPY (lipid droplet) and LysoTracker co-localization in APOE4 oligodendrocytes with and without CHIR99021 treatment. P value calculated using two-tailed student’s t-test. D, Myelin basic protein (cyan) staining in APOE3 myelinoids and APOE4 myelinoids after 20 weeks in culture. Scale bar represents 20 um. Each dot represents an individual myelinoid, P value calculated using a two-tailed student’s t-test. E, Number of Olig2-positive nuclei in APOE4 myelinoids with and without CHIR99021 treatment. Each dot represents an individual myelinoid. P value calculated using two-tailed student’s t-test. F, Neurofilament staining (mean intensity of immunoreactivity) in APOE4 myelinoids with and without CHIR99021 treatment. Each dot represents an individual myelinoid. P value calculated using twotailed student’s t-test

A  
![](images/49ef6acb05bd7024db747021b3145a0d91ebb19318876d6579dd9a2d1423c8a7.jpg)

<details>
<summary>scatterplot</summary>

| Group | pSec396 (mean intensity) |
|-------|--------------------------|
| APOE3;P301S | 0.0321 |
| APOE4;P301S | 0.0321 |
</details>

B

![](images/8a177b519cace7c1a4487262ac32fa8d7695592191931049ae9a7cdbea5f161a.jpg)

<details>
<summary>scatterplot</summary>

| Group | Olig2+ cell number |
|-------|---------------------|
| APOE3;P301S | 45 |
| APOE4;P301S | 55 |
</details>

C  
![](images/1d4d2583a05a8ab1f6620eb8b05b47de9040863f9d2a91d9f834234b7c7a78d4.jpg)

<details>
<summary>scatterplot</summary>

| Group    | Olig2 nuclei / total nuclei |
| -------- | --------------------------- |
| Control  | 0.9382                      |
</details>

D  
![](images/13c018c3b964726d1ea77e5e0c09f435801bc26bf7ddaf79978fc6efc5e724a9.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Group | Mean Intensity |
|-------|----------------|
| Control | 0.1932 |
| CHIR | 0.1932 |
</details>

E  
![](images/f5cf06a0702a42d004bd8f59ffb8cc22180f698adb371c810b1e1f06660c1cc3.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Group | IBA1 mean intensity | Microglia count |
|-------|---------------------|-----------------|
| Control | 5690 | 9211 |
| CHIR | 3421 | 9211 |
</details>

F

![](images/91f8cafab85ed24f30563d4299b55af19986d9426f0ceb49414756ea2d0bc91f.jpg)

<details>
<summary>bar chart</summary>

| Group   | Microglial soma volume | Microglia number end points |
|---------|------------------------|------------------------------|
| Control | 130                    | 35                           |
| CHIR    | 140                    | 45                           |
</details>

G  
![](images/a09b76aed1700282d0a56a414c63f0532b9e968ce8d34e0d31af2c2b4d560598.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Group | pSer396 (mean intensity) |
|-------|--------------------------|
| Control | 10.0 |
| +CHIR | 12.0 |
</details>

H  
![](images/5afe22e516c29307b68abe484752764006261e99ee6d4d822a6fda5e0d31286f.jpg)

<details>
<summary>scatterplot</summary>

| Group | pThr181 (mean intensity) |
|-------|--------------------------|
| Control | 0.5154 |
| CHIR | 0.5154 |
</details>

## Extended Data, Figure 4

A, Representative images and quantification of phospho-tau Ser396 immunoreactivity in the hippocampus of APOE3;PS19 (left) and APOE4;PS19 (right) mice. Each dot represents an individual mouse. P value calculated using two-tailed student’s t-test. B, Representative images and quantification of number of Olig2-positive cells in the hippocampus of APOE3;PS19 (left) and APOE4;PS19 (right) mice. Each dot represents an individual mouse. P value calculated using two-tailed student’s t-test. C, Representative images and quantification of number of Olig2-positive cells in the hippocampus of APOE4;PS19 mice treated with control (left) or CHIR99021 (right). Each dot represents an individual mouse. P value calculated using two-tailed student’s t-test. D, Representative images and quantification of number of immunoreactivity to GFAP the hippocampus of APOE4;PS19 mice treated with control (left) or CHIR99021 (right). Each dot represents an individual mouse. P value calculated using two-tailed student’s t-test. E, Representative images and quantification of immunoreactivity to IBA1 and number of microglia in the hippocampus of APOE4;PS19 mice treated with control (left) or CHIR99021 (right). Each dot represents an individual mouse. P value calculated using two-tailed student’s t-test. F, Representative images showing 3-D reconstruction of microglial morphology in control (top) and treated (bottom) mice. Quantifications of microglial soma volume and number of processes. Each dot represents the averaged values of microglia detected per individual mouse. P value calculated using two-tailed student’s t-test. G, Representative images and quantification of phospho-tau Ser396 immunoreactivity in the hippocampus of APOE4;PS19 mice treated with control (left) or CHIR99021 (right). Each dot represents an individual mouse. P value calculated using two-tailed student’s t-test. H, Representative images and

quantification of phospho-tau Thr181 immunoreactivity in the hippocampus of APOE4;PS19 mice treated with control (left) or CHIR99021 (right). Each dot represents an individual mouse. P value calculated using two-tailed student’s ttest.