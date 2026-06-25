The Balance between Saturated and Unsaturated Fatty Acids Regulates Ovarian Cancer Cell Fate

Guangyuan Zhao1, 2, Yuying Tan3&, Horacio Cardenas1&, David Vayngart4, Hao Huang1, Yinu Wang1, Russell Keathley1,2, Jian-Jun Wei 5,6, Christina R. Ferreira7, Ji-Xin Cheng3, 8, 9#, Daniela Matei1, 6, 10#

1 Department of Obstetrics and Gynecology, Feinberg School of Medicine, Northwestern University, Chicago, IL 60611, USA  
2 Driskill Graduate Program in Life Sciences, Feinberg School of Medicine, Northwestern University, Chicago, IL 60611, USA  
3 Department of Biomedical Engineering, Boston University, Boston, MA 02215, USA  
4 Feinberg School of Medicine, Northwestern University, Chicago, IL 60611, USA  
5 Department of Pathology, Feinberg School of Medicine, Northwestern University, Chicago, IL 60611, USA  
6 Robert H. Lurie Comprehensive Cancer Center, Chicago, IL 60611, USA  
7 Bindley Bioscience Center, Purdue University, West Lafayette, IN 47906, USA  
8 Department of Electrical and Computer Engineering, Boston University, Boston, MA 02215  
9 Photonics Center, Boston University, Boston, MA 02215, USA  
10 Jesse Brown VA Medical Center, Chicago, IL 60612, USA  
& these authors contributed equally

Corresponding authors:

Daniela Matei, MD

Professor, Department of Obstetrics and Gynecology

Northwestern University Feinberg School of Medicine

303 E Superior Street; Lurie 4-107

E-mail: daniela.matei@northwestern.edu

and

Ji-Xin Cheng, PhD

Professor; Department of Electrical and Computer Engineering,

And Photonics Center,

Boston University, Boston, MA 02215, USA

E-mail: jxcheng@bu.edu

## Abstract

Fatty acids are an important source of energy and a key component of phospholipids in membranes and organelles. Saturated (SFAs) are converted into unsaturated fatty acids (UFAs) by stearoyl Co-A desaturase (SCD), an enzyme highly active in cancer. Here we studied how the balance between SFAs and UFAs maintained by SCD impacts cancer cell survival and tumor progression. SCD depletion or inhibition caused lower levels of UFAs vs. SFAs and altered fatty acyl chain plasticity, as demonstrated by lipidomics and stimulated Raman spectroscopy (SRS). Further, the loss of equilibrium between UFAs and SFAs resulting from SCD knock down triggered endoplasmic reticulum (ER) stress response with brisk activation of IRE1α/XBP1 and PERK/eIF2α/ATF4 axes. Stiff and disorganized ER membrane was visualized by electron microscopy and SRS imaging in cells in which SCD was knocked down. The induction of longterm mild ER stress or short-time severe ER stress by the increased levels of SFAs and loss of UFAs led to cell death. However, ER stress and apoptosis could be readily rescued by supplementation with UFAs and re-equilibration of SFA/UFA levels. The effects of SCD knockdown or inhibition observed in vitro, translated into suppression of intraperitoneal tumor growth in xenograft models. Furthermore, a combined intervention using an SCD inhibitor and an SFA enriched diet, initiated ER stress in tumors growing in vivo and potently blocked their dissemination. In all, our data support SCD as a key regulator of the cancer cell fate under metabolic stress and point to new treatment strategies targeting the lipid balance.

## Keywords

Ovarian cancer, lipid metabolism, fatty acids, ER stress, SRS imaging

## Significance Statement

We show that the balance between saturated and unsaturated fatty acids tightly regulated by the desaturase SCD impacts the survival of cancer cells; increased levels of unsaturation being protective against ER stress induced apoptosis. Decreasing fatty acid unsaturation, either through SCD depletion or through SCD inhibition coupled with a dietary intervention blocks tumor progression in vivo. Our findings support the concept of targeting the lipid balance as a new target in cancer.

## Introduction

To keep up with the demands of limitless proliferation and metastatic spread, cancer cells thwart physiological metabolic pathways to meet their augmented energetic needs. When glucose and oxygen are in short supply, fat becomes convenient fuel. Whether taken up from the tumor microenvironment (TME) or newly synthesized, lipids function as alternative energy source for rapidly growing tumors. In addition, lipids are key constituents of membranes and intra-cellular organelles, enabling the smooth functioning of signaling circuitries and the homeostasis of cells proliferating under stressful conditions (1). A unique property of ovarian cancer (OC) is its tropism to the omentum, a fat-laden organ, which has been thought to function as feeding soil for rapidly expanding tumors (2, 3). While lipid uptake by cancer cells has been studied to some extent (2-4), the role of de novo lipogenesis and of the ensuing balance between unsaturated and saturated lipids remain not fully understood.

Within the de novo lipogenesis pathway, lipid desaturation is a key step required for the generation of unsaturated lipids to maintain the membrane fluidity, the integrity of cellular signaling, and the lipid pool for β-oxidation (5). Fatty acid (FA) desaturases catalyze the addition of double carbon bonds in acyl chains, regulating the formation of mono- and poly-unsaturated FAs (MUFA and PUFA, respectively). Stearoyl-CoA desaturase (SCD) converts saturated (SFA) to mono-unsaturated FAs, palmitic and stearic acid to palmitoleic and oleic acid, respectively. SCD is upregulated in cancer (6) and its inhibition was shown to suppress cancer cell proliferation, in conditions depleted of exogenous lipids (7). SCD was also shown to protect cancer cells from lipid peroxidation leading to ferroptosis, through a mechanism dependent on the anti-oxidant coenzyme CoQ10 (8). Using stimulated Raman spectroscopy (SRS) (9, 10), which enables analysis of lipid species in rare cell populations, we recently demonstrated that ovarian cancer stem cells (CSCs) are enriched in UFAs (11). We showed that SCD small molecule inhibitors or shRNA-mediated knock down eliminated ovarian CSCs, delaying tumor initiation (11). However, the mechanisms by which SCD regulates cancer cells’ and $\mathrm { C S C s ^ { \prime } }$ survival under stressful conditions are not elucidated.

Through a combined lipidomic, transcriptomic and single cell imaging approach, we zoom in on how the balance between UFAs and SFAs regulates cell survival and tumor progression in OC models. We observed that an increase in SFAs caused by addition of SFA to the media, or by SCD depletion or inhibition, led to significant endoplasmic reticulum (ER) stress inducing apoptosis of cancer cells. This ER stress is likely caused by direct effects of SFAs on the ER membrane fluidity, causing activation of the sensor proteins IRE1α and Protein Kinase R-like ER Kinase (PERK) and could be rescued by addition of UFAs and restoration of the required equilibrium. SCD knock-down inhibited tumor progression in vivo and pharmacological inhibition of the enzyme coupled with a diet enriched in SFAs had potent anti-tumorigenic effects. These results point to the role of SCD as a gate keeper ensuring the survival of ovarian cancer cells under the continuous metabolic stress imposed by non-stop proliferation and to the therapeutic potential of targeting the lipid balance in cancer.

## Results

SCD is highly expressed in OC cell lines and tumors: SCD expression was assessed by using representative cancer cell lines, an ovarian cancer TMA, and RNA sequencing data from human specimens profiled by The Cancer Genome Atlas (TCGA) (4) and the Genotype-Tissue Expression (GTEx) Project. SCD expression was significantly higher in high grade serous ovarian tumors (HGSOC) profiled by the TCGA (n= 427) compared to normal fallopian tube epithelium (FTE, n = 5, Fig. 1A). Further, SCD was highly expressed in OC cell lines as compared to immortalized fallopian tube epithelial cells at both mRNA and protein levels (Figs. 1B, C). IHC analysis demonstrated significant upregulation of SCD in HGSOC tumors (n = 12) vs. FTE (n = 6), with 7 of 12 tumors displaying intense staining vs. FTE (Fig. 1D, $\mathbf { p } = 0 . 0 3 7 7 )$ ). Other histological subtypes of OC also displayed increased SCD expression compared to FTE (p = 0.006), while non-malignant ovarian tumors (borderline tumors and cystadenoma) did not overexpress SCD (Supplementary Table S2).

SCD regulates the balance between SFAs and UFAs in OC cells: For functional studies, two shRNA sequences targeting SCD (shSCD-1 and shSCD-2) or control shRNA (shCtrl) were stably transduced in OVCAR-5, OVCAR-8, OVCAR-3 and PEO1 cells. SCD knockdown (KD) was verified by quantitative PCR and western blotting (Figs. 1E, F, Supplementary Figs. S1A-C). Next, lipidomics and isotopic hyperspectral stimulated Raman scattering (hSRS) assessed the abundance of SFAs and UFAs in OC cells transduced with shRNA targeting SCD vs. control shRNA and cultured under low serum conditions to limit the impact of exogenous lipid uptake. A significant reduction in UFAs (palmitoleic and oleic acids), but no difference in abundance of SFAs (palmitic and stearic acids, Fig. 1G) were recorded in cells transduced with shRNA targeting SCD vs. control shRNA. Further, isotopic hSRS imaging compared the levels of UFAs converted from newly imported SFAs in shSCD vs shCtrl transduced cells (Figs. 1H-J). After being maintained in low serum medium for 24 hours, cells were cultured with deuterated SFA (PA-d31) for 24 hours. The C-D bond signal, corresponding to UFAs was measured by hSRS imaging (Fig. 1I), and intracellular deuterated SFA and UFA levels were distinguished through a LASSO unmixing analysis using the distinctive Raman spectra of PA-d31 and OA-d34, as reference for SFA and UFA respectively (Fig. 1H). Images and quantitative analyses of UFA levels and UFA/SFA ratio (Fig. 1J) show that cells in which SCD was knocked down contain significantly less deuterated UFA synthesized from newly imported PA-d31, indicating that the efficiency of converting SFA to UFA is diminished in cells depleted of SCD compared to controls.

To understand which lipid species were most affected by the decrease of UFAs caused by SCD depletion, lipidomics by multiple reaction (MRM) profiling (12) measured the abundance of phosphatidylcholines (PC), phosphatidylethanolamine (PE), sphingomyelin (SM), and triglycerides (TAGs) in OVCAR-5 cells stably transduced with control or shRNA targeting SCD and cultured under low serum conditions for 48 hours. After data normalization, principal component analysis (PCA) confirmed the separation of the two groups (i.e. shCtrl and shSCD) and heatmaps for each lipid species generated by using unsupervised hierarchical clustering demonstrated separation and clustering of the two groups (Supplementary Figure S2). The most affected (fold-change) lipid species by SCD depletion were PC and SM, followed by triacylglycerol (TAG) and PE (Fig. 2A, Supplementary Table S3). A deeper examination of each lipid class revealed that both PC and SM phospholipids with 1° plasticity (one or two carboncarbon double bonds within the fatty acid tail) (13) were significantly less abundant in shSCD compared with shCtrl transduced cells $( \mathtt { p } < 0 . 0 0 0 1$ , Fig. 2B). Further, a significant reduction of 16:1 or 18:1 fatty acyl chains integrated TAGs was observed in OC cells stably transduced with shRNA targeting SCD compared to cells transduced with control shRNA (p= 0.0382, Fig. 2C) Combined, the lipidomics analyses coupled with hSRS imaging demonstrate that cells depleted of this key desaturase, contain less abundant UFAs, and less plastic lipid species, particularly PC and SM.

SCD knock down triggers ER Stress response: To further understand the global effects of UFA restriction in OC cells, RNA-seq compared the transcriptomic profiles of cells transduced with shRNA targeting SCD or control shRNA. Quality control of RNA-sequencing is included in Supplementary Fig. S3. Cells were cultured under low serum conditions for 48 hours. There were 1513 differentially expressed genes (DEGs; FDR < 0.05), of which 707 were upregulated and 806 downregulated between OVCAR-5 cells stably transduced with control or shRNA targeting SCD (Fig. 2D, Supplementary Table S4). Gene Ontology analysis of significantly upregulated genes revealed that the ER stress response was the top affected pathway by SCD KD (Fig. 2E). Gene Set Enrichment Analysis (GSEA) of all genes also indicated that ER stress response gene sets (Hallmark Unfolded Protein Response; Reactome\_IRE1α Activities Chaperones, Reactome PERK Regulates Gene Expression, Reactome ATF4 Activities Genes in Response to Endoplasmic Reticulum Stress) were upregulated in cancer cells in which SCD was knocked down (Fig. 2F). Several genes (DDIT3, ATF3, PPP1R15A, CEBPB) involved in ER stress response are highlighted in the volcano plot depicting DEGs between SCD KD and control cells (Fig. 2D). Furthermore, upstream regulator analysis performed with Ingenuity Pathway Analysis (IPA) software identified several transcription factors (ATF4, DDIT3, NUPR1) involved in the ER stress response pathway among the top ones predicted to be activated in OC cells transduced with shRNA targeting SCD vs control cells (Fig. 2G). A heatmap including significant genes in the ER stress response pathway (n = 64 genes) illustrates clear differences in expression levels for these transcripts between cells in which SCD was knocked down vs. control cells (Fig. 2H). Further, exploration of the transcriptomic dataset associated with the Cancer Dependence Map (14) and Cancer Cell Line Encyclopedia (15) shows that dependency score of key transcription regulators in the ER stress response pathway such as ATF4 and DDIT3 were positively correlated with that of SCD (r=0.3117 and 0.3878, respectively Supplementary Figs. S4A, B), indicating that OC cells that are highly dependent on SCD also have higher dependency on ATF4/DDIT3. Additionally, expression levels of several important ER stress response genes (IGFBP1, ERN1, TXNIP, NABP1) were negatively correlated with SCD (Supplementary Figs. S4C-F), corroborating the association between SCD and ER stress response found through transcriptomic analysis.

## Excess SFAs caused by depletion or pharmacological inhibition of SCD induces ER stress:

To further investigate how the imbalance between SFAs and UFAs caused by SCD depletion or inhibition in cancer cells activates the ER stress responses, we next evaluated the two key sensing mechanisms of this pathway: activation of IRE1α and PERK. ER-spanning transmembrane domain of IRE1α and PERK are critical sensors of the levels of lipid saturation in the cell and activate the ER stress response (16). IRE1α causes splicing of the X-box-binding protein 1 (XBP1) mRNA which leads to a spliced form (XBP1s) with potent transcriptional activity (17). PERK autophosphorylates itself upon ER stress and then phosphorylates the eukaryotic translation initiation factor 2α (eIF2α) to halt translation of proteins (18). Translation of ATF4 mRNA, due to its unique 5’ UTR sequence, is upregulated upon phosphorylation of eIF2α (19).

XBP1 splicing was assessed in OVCAR-5 cells stably transduced with shRNA targeting SCD or control shRNA or in cells treated with the SCD inhibitor CAY10566. Increased baseline XBP1s levels were noted in OVCAR-5 and OVCAR-8 cells transduced with shRNA targeting SCD vs control and cultured in low serum medium for 48 hours (Figs. 3A, B & Supplementary Fig. S5A). XBP1 splicing was increased in OVCAR-5 and OVCAR-8 cells transduced with shRNA targeting SCD vs control even under full serum conditions (containing exogenous lipids), but to a lesser degree (Supplementary Figs. S5B, C). Additionally, activation of PERK/CHOP was detected in shSCD vs shCtrl stably transduced OVCAR-8 cells (Supplementary Fig. S5D) under low serum conditions.

Likewise, a dose-dependent increase in XBP1s levels was observed in OVCAR-5 cells treated with CAY10566 (Figs. 3C, D). Having hypothesized that the major trigger of ER stress induced by SCD depletion is the excess of SFAs, XBP1 splicing and activation of PERK/eIF2α/ATF4 were measured in OC cells in which SCD was either knocked down or pharmacologically inhibited in the presence of exogenously added SFA (palmitic acid). We chose a concentration of palmitic acid (50μM) equivalent to that found in media supplemented by 10% FBS(20). Further, as the consequences of ER stress depend on both the length of exposure to cellular stress and the severity of the stress (21), time-dependency was assessed along both the IRE1α/XBP1 and the PERK/eIF2α/ATF4 axes in OC cells supplemented with palmitic acid. The XBP1 splicing signal was increased in OC cells in which SCD was knocked down compared with control cells after supplementation with 50μM of palmitic acid, peaking at approximately 8-12 hours and diminishing at 24 hours (Fig. 3E). Likewise, western blotting analysis of the PERK/eIF2α/ATF4 axis showed increased phosphorylation and corresponding decreased expression levels of eIF2α in OC cells in which SCD was knocked down, starting 2 hours after addition of palmitic acid and peaking at 8-12 hours (Fig. 3F). The downstream transcription factors ATF4 and CHOP were upregulated starting 4 hours after addition of palmitic acid and remaining persistently high up to 24 hours. To confirm these observations in human specimens, we used primary tumor cells dissociated from freshly obtained HGSOC tumors (Supplementary Table S5). Treatment with CAY10566 induced XBP1 splicing in primary HGSOC cells and the XBP1s levels were further augmented by addition of palmitic acid (Fig. 3G & Supplementary Fig. S5E).

Next, to visualize the status of the ER under these conditions, hSRS imaging was performed after treating OVCAR-5 cells stably transduced with control or shRNA targeting SCD with PA-d31 under low serum condition (Fig. 3H). Most of OVCAR-5 shCtrl cells displayed C-D signal derived from PA-d31 in lipid droplets (LD) (depicted as a dots, gray arrow), while a considerable portion of OVCAR-5 shSCD cells displayed the C-D signal on rigid ER (shown as a linear structure, yellow arrow), consistent with an ER stress related morphology (22). Both cell lines contained a small portion of cells harboring detectable C-D signal all over the cytoplasm (Fig. 3H, blue arrow). After PA-d31 treatment alone under low serum conditions, the cell population with rigid ER structures represented the major population of OVCAR-5 shSCD cells, while the cell population with detectable C-D signal in LD was the majority in OVCAR-5 shCtrl cells (Fig. 3H, I). Rescue treatment with UFA (OA or full serum medium) led to the disappearance of rigid ER and increased PA-d31 accumulation in lipid droplets for both shSCD and shCtrl OC cells (Fig. 3H, I), suggesting that supplementation with UFAs can rescue SFA-induced ER stress and facilitate SFA storage in LD. These data support that the balance of intracellular SFA and UFA is essential to prevent ER stress.

Further, examination of OVCAR-5 cells stably transduced with control or shRNA targeting SCD cultured in low serum medium for 48 hours by using transmission electron microscopy (TEM) demonstrated ER membrane disorganization and irregular and compromised ER structure in OVCAR-5 shSCD cells compared to shCtrl cells (Fig. 3J), confirming the biochemical and hSRS imaging results.

UFAs prevent ER stress in OC cells: To exclude the contribution of potential desaturaseindependent functions of SCD to the induction of ER stress in OC cells, we examined whether the effects of SCD depletion or inhibition could be rescued by oleic acid, its main enzymatic product. Supplementation with oleic acid reversed XBP1 splicing in OVCAR-5 cells in which SCD was knocked down (Fig. 4A) as well as in OVCAR-5 cells depleted of SCD and treated with palmitic acid (Fig. 4B). Likewise, supplementation with oleic acid reduced the up regulation of ATF4 and CHOP along the PERK/eIF2α/ATF4 axis observed in OVCAR-5 cells stably transduced with shRNA targeting SCD and maintained under low serum conditions (Figs. 4C, D). Similar rescue effects of oleic acid on XBP1 splicing were observed in OVCAR-8 and PEO1 cells stably transduced with shRNA targeting SCD (Supplementary Figs. S6A, B).

Likewise, the rescue effects of oleic acid on ER stress induced by CAY10566 were examined. Supplementation with oleic acid reduced XBP1s levels in OVCAR-5 cells treated with CAY10566 (Fig. 4E), as well as XBP1s levels in cells treated with CAY10566 and palmitic acid (Fig. 4F). Oleic acid also reduced the upregulation of ATF4 and CHOP induced by the SCD inhibitor in OVCAR-5 cells maintained under low serum conditions (Fig. 4G) or in cells additionally treated with 50μM palmitic acid (Fig. 4H).

Lastly, to test the sufficiency of SCD in regulating ER stress triggered by an imbalance of SFA and UFA in OC cells, the enzyme was overexpressed in OVCAR-5 cells. Increased SCD mRNA and protein levels were observed in OC cells stably transfected with pLenti-SCD compared to pLenti-Ctrl (Figs. 4I, J). XBP1 splicing induced by addition of palmitic acid in control cells was significantly reduced by SCD overexpression (Fig. 4K, L, p = 0.0277). Collectively, our data support the significance of the balance between SFAs and UFAs regulated by SCD in fine tuning the functions of the ER, likely mediated through direct effects on the ER membrane.

SCD depletion or inhibition induces apoptosis of OC cells: It is accepted that long-term exposure to mild ER stress or short-term exposure to severe ER stress leads to CHOP-mediated apoptosis (21). RNA-seq analysis of OVCAR-5 SCD KD cells indicated that DDIT3 (also known as CHOP, GADD153) was among the top up-regulated genes in shSCD cells cultured in low serum medium (Fig. 2D, Supplementary Table 4). We therefore hypothesized that OC cells depleted of SCD and cultured under low serum conditions over long period of time would undergo apoptosis. IncuCyte imaging examined Annexin V staining of OVCAR-5 SCD KD cells cultured in low serum medium alone with/without addition of extra palmitic acid in real time. A higher percentage of cells depleted of SCD underwent apoptosis compared with control cells under these conditions. Supplementation with $5 2 \mu \mathrm { M }$ oleic acid completely rescued the phenotype (Fig. 5A). Further, addition of palmitic acid $( 5 0 \mu \mathrm { M } )$ induced early onset of apoptosis in shSCD cells as compared to shCtrl cells, and supplementation with oleic acid reversed the phenotype (Fig. 5B). Likewise, CAY10566 induced apoptosis in OVCAR-5 cells grown under low serum conditions, starting at 48 hours; while oleic acid supplementation blocked this effect (Fig. 5C). Addition of palmitic acid to the CAY10566 treatment caused earlier onset of apoptosis (less than 24 hours) and augmented the phenotype (>20% apoptotic cells; Fig. 5D). Similarly, oleic acid supplementation rescued the phenotype (Figure 5D). On the other hand, stable SCD knock down did not affect proliferation of OVCAR-5 cells compared to controls when cells were maintained under full serum conditions. However, SCD KD decreased proliferation of cells cultured under low serum conditions (Supplementary Figs. S6C, D).

To confirm the apoptosis phenotype, we also examined the cleavage of caspase-3 in OVCAR-5 transduced with shRNA targeting SCD vs. control shRNA cultured under low serum conditions and treated with extra palmitic acid. Increased caspase-3 cleavage was observed in OVCAR-5 shSCD compared to shCtrl cells (Fig. 5E). Importantly, cleavage of caspase-3 in cells depleted of SCD and treated with palmitic acid could be reversed by supplementation with oleic acid (Fig.

5E). Caspase-3 cleavage was also induced by CAY10566, augmented by addition of extra palmitic acid and rescued by restoration of the SFA/UFA balance, through repletion of oleic acid (Fig. 5F).

Lastly, to test the sufficiency of SCD to this phenotype, OVCAR-5 cells in which SCD was overexpressed (pLenti-SCD) vs control cells (pLenti-Ctrl) were maintained under low serum conditions and were treated with 50μM palmitic acid for 72 hours. The percentage of apoptotic cells induced by exogenous palmitic acid was significantly reduced in cells in which SCD was overexpressed as compared to control cells (Fig. 5G), supporting that OC cells with higher SCD expression could survive the stress induced by SFA. Together, the data demonstrate that the balance between intracellular UFA and SFA regulated by the desaturase SCD is critical to determining the survival of OC cells.

SCD depletion or inhibition suppresses tumor growth in vivo: Whether the observed effects of SCD on cancer cell survival impact tumor progression in vivo remains unknown. Tumorigenicity of OC cells depleted of SCD was tested by using an intraperitoneal (ip) xenograft model in athymic nude mice. SCD knockdown compared to control OVCAR-5 cells led to significantly reduced tumor weight (234.3 mg vs. 360.1 mg, $\mathbf { p } = 0 . 0 3 4 3 )$ and tumor volume $( 2 0 9 . 2 \ : \mathrm { m m } ^ { 3 }$ vs. $4 0 4 . 8 \mathrm { m m } ^ { 3 }$ , $\mathbf { p } = 0 . 0 2 1 2 \colon$ Figs. 6A, B), although the numbers of peritoneal metastases (Fig 6C, 208.8 vs. 217.3, ${ \bf p } = 0 . 7 6 0 2 )$ ) and ascites volume (Supplementary Fig. S7A) were similar between shSCD and control groups. SCD knock down was maintained in vivo, as demonstrated by qRT-PCR measurement of SCD in RNA extracted from harvested tumors (Fig. 6D, p value = 0.0015). Furthermore, increased XBP1s levels were observed in xenografts derived from OVCAR-5 cells stably transduced with shRNA targeting SCD compared to controls (Figs. 6E, F, ${ \bf p } = 0 . 0 0 1 8 )$ , supporting that an increased susceptibility to ER stress is maintained in vivo in tumors depleted of the enzyme. Similar inhibitory effects on tumor growth were observed in a subcutaneous mouse xenograft model derived from OVCAR-3 cells stably transduced with shRNA targeting SCD vs. shRNA control (Supplementary Figs. S7B, C).

Our observations that ER stress and apoptosis are augmented in vitro by inhibition of the desaturase coupled with an excess of SFAs led us to hypothesize that the effects of a pharmacological inhibitor targeting this pathway would be enhanced through dietary modifications tilting the FA balance towards increased saturation levels. To test this hypothesis, we used an OC ip model fed a palmitic acid rich or control diet, and treatment with CAY10566 or diluent. While CAY10566 did not significantly alter the numbers of peritoneal metastases and the ascites volume in mice fed a control diet (Figs. 6G, H), the inhibitor significantly decreased both the ascites volume $( \mathfrak { p } < 0 . 0 0 0 1 )$ as well as the numbers of metastases $( \mathfrak { p } = 0 . 0 0 0 3 )$ in mice fed palmitic acid rich diet (Figs. 6G, H). Interestingly, an unanticipated, but significant increase in ascites volume was observed in the group receiving the SFA rich diet compared with the control diet (Fig. 6G, $\mathbf { p } = 0 . 0 2 5 2 )$ . No significant differences were observed in total tumor weights and total tumor volumes (Supplementary Figs. S8D, E). XBP1s levels were not significantly different in tumors derived from mice fed the control diet and treated with vehicle vs CAY10566 (Figs. 6I, J, $\mathsf { p } = 0 . 6 3 7 0 )$ , but were significantly increased in tumors derived from mice fed palmitic acid rich diet and treated with CAY10566 vs. control (Figs. 6K, L, $\mathrm { p } { = } 0 . 0 3 6 9 )$ ) The data support that inhibition or depletion of SCD exerts anti-tumorigenic effects through a mechanism dependent on ER stress induction likely caused by decreased levels of lipid desaturation.

## Discussion

Our data based on transcriptomic, lipidomic analyses, SRS and EM imaging demonstrate that the imbalance between saturated and unsaturated fatty acids caused by depletion or inhibition of the enzyme SCD has a key function in determining cancer cell survival or death and impacts tumor progression in vivo. These findings hone on a largely understudied metabolic process in cancer cells and suggest the possibility of using an intervention combining an SCD enzymatic inhibitor together with a dietary intervention to increase levels of lipid saturation in cancer cells and trigger a potent anti-tumor effect. Our findings have several important consequences.

First, our results point to the significance of the process of lipid unsaturation in cancer. Lipid synthesis includes the synthesis of FA from acetyl-coA mediated by fatty acid synthase (FASN) and acyl-CoA synthase (ACSL), followed by addition of double carbon bonds catalyzed by FA desaturases. Among the three desaturases, Δ9 (stearoyl-CoA desaturase-1, SCD) catalyzes the synthesis of monounsaturated fatty acids by adding one double bond to saturated fatty acids (mostly stearic acid), while the Δ6 and Δ5 desaturases are involved predominantly in the synthesis of polyunsaturated fatty acids (23). The current study builds on our previous observations that highly tumorigenic ovarian CSCs are enriched in UFAs, caused by SCD upregulation, which in turn, induce pro-survival NF-κB signaling allowing CSCs to proliferate as spheres and effectively initiate tumors in immunodeficient mice (11). Here we show that beyond the previously observed effects on CSCs, SCD knockdown, and to a lesser extent its inhibition, induces anti-tumor effects in intraperitoneal xenografts which closely resemble the pattern of dissemination of the human disease. Overexpression of ACSL and SCD leading to increased UFA levels was described in association with epithelial to mesenchymal transition and aggressive clinical prognosis in colon cancer, and SCD upregulation was observed in basal type breast cancer and aggressive prostate cancer (24, 25). Depletion of oleic acid (but not of palmitate) inhibited the proliferation of acute meylogenous leukemia and lymphoma cells (26). Unsaturated lipids also play a role in maintaining the membrane fluidity and support signaling through membrane receptor tyrosine kinases (27). Lipid saturation detectable in plasma or in tumor tissue was associated with cancer risk in several epidemiological studies (28, 29). For example, decreased risk of breast cancer was noted in women with high plasma stearic acid levels and low SCD activity, supporting that high lipid saturation is indirectly correlated with cancer risk (29). However, it remains not clear how the balance between UFAs and SFAs alter cancer predisposition or cancer progression, a concept we addressed here.

A powerful tool that allowed us to quantify UFAs and SFAs at the single cell level in this study was SRS microscopy, an innovative label-free chemical imaging technique which we have previously employed to characterize metabolic reprograming from glycolysis to fatty acid uptake and β-oxidation in platinum-resistant cancer cells (30), increased lipid desaturation in ovarian CSCs (11), and cholesteryl ester accumulation as a metabolic marker for multiple aggressive cancers (31, 32). Combined with post-processing methods such as least-square fitting, multivariate curve resolution and phasor segmentation, hSRS can distinguish different intracellular biomolecules such as protein and fatty acid (10, 33). Here, SRS imaging visualized SFA-induced ER stress in OC cells depleted of SCD and the rescue observed by manipulating the ratio between SFAs and UFAs. We recognize that highly spatially overlapping biomolecules with similar spectrum profile such as SFAs and UFAs are difficult to decompose by using conventional analysis methods. We propose that pixel-wise LASSO unmixing can resolve such shortcomings, enabling the simultaneous evaluation of multiple metabolites, facilitating better assessment of cancer cell metabolism and metabolic changes in response to gene modification and drug treatment. The innovative hSRS-LASSO imaging method utilized here provides a new way to explore cancer lipid metabolism in deeper detail.

Our findings demonstrate that the imbalance between SFAs and UFAs impedes cancer cell survival and in vivo tumor growth through induction of ER stress. We observed that two branches of ER stress response, regulated by the PERK and IRE1α were activated in response to SCD depletion or inhibition, that this activation was augmented in the presence of SFA supplementation and could be rescued by addition of UFAs. Interestingly, non-cancer cells, such as neural stem/progenitor cells were found to be susceptible to lipid accumulation and consequent ER stress (34) and palmitic acid was shown to induce ER stress and apoptosis in human bone marrow-derived mesenchymal stem cells(35). Other recent studies found that N-Myc driven hepatocellular cancer cell or glioma proliferation was dependent on lipid unsaturation through modulation of ER stress responses (36). While a definitive mechanistic explanation is still lacking, our hSRS and TEM imaging suggest that increased levels of lipid unsaturation in cancer cells alter the morphology of the ER, causing increased membrane rigidit and potentially direct activation of the sensor proteins.

The link between ER stress and tumor progression is emerging. In orthotopic cervical cancer xenografts, hypoxia-induced metastasis to lymph nodes was blocked by PERK inhibition (37). The PERK/eIF2α/ATF4 axis was also shown to be important for inducing epithelial-tomesenchymal transition of breast cancer cells (38), while the IRE1α/XBP1 pathway was involved in tumor initiation and breast cancer progression by activating the transcription factor HIF1α (39). Our study, together with previous reports, reveals the biphasic role of PERK/eIF2α/ATF4 axis of the ER stress response; with the initial response being implicated in salvaging the stressed cells, whereas prolonged activation of the pathway leads to apoptosis.

Future investigation of how lipid unsaturation triggers ER stress and modulates the ER stress response could provide new therapeutic opportunities to target cancer progression.

A starting point towards this goal is our attempt to combine SCD inhibition with a dietary intervention. We demonstrate that this intervention resulting in accumulation of toxic SFAs has potent anti-tumor effects and induces ER stress responses in tumors. The putative role of diet in cancer treatment has remained a “holy grail” and is based on the concept that altered metabolite levels in the tumor microenvironment could create metabolic challenges impeding tumor cells survival. A recent study found that severe caloric restriction led to inhibited tumor growth (40) and a proposed mechanism, was the downregulation of SCD, resulting in an imbalance between SFAs and UFAs, similar to what we achieved in our study through SCD pharmacological inhibition and supplementation with palmitic acid. The role of saturated lipids in cancer remains controversial, with the overwhelming belief that saturated fat is pro-tumorigenic. Indeed, a recent study showed that dietary palmitic acid promoted metastasis in oral carcinoma and melanoma models (41). Specifically, in vitro palmitic acid treatment primed tumor cells for metastasis after implantation in vivo, while a palmitic acid-rich diet promoted increased metastatic tumor burden. Consistent with these observations, we found that the palmitic acid-rich diet induced increased accumulation of malignant ascites, the main vehicle of OC intraperitoneal metastasis. However, combined palmitic acid-rich diet and the SCD inhibitor CAY10566, significantly reduced the volume of ascites as well as the numbers of metastases, with signals of ER stress response being detectable directly in tumor tissue.

Given the plasticity and redundancy of metabolic pathways, which have by and large thwarted prior attempts to use metabolic interventions to target cancer, our results highlight the importance of combination strategies. Taken together our findings support SCD’s key role in regulating cancer cell fate and tumorigenicity and point to new modalities to block OC progression.

## Materials and Methods

Cell culture: OVCAR-5 cells and OVCAR-8 cells were provided by Dr. Marcus Peter, Northwestern University, and Dr. Kenneth Nephew, Indiana University, respectively. PEO1 cell were purchased from MilliporeSigma (cat#: 10032308). OVCAR-3 cells were purchased from the American Type Culture Collection (ATCC) (cat#: HTB-161). FT-190 cells (immortalized human fallopian tube luminal epithelial cells) were provided by Dr. Ronny Drapkin, University of Pennsylvania. OVCAR-5, PEO1 and OVCAR-3 cells were cultured in RPMI-1640 with Lglutamine (Corning cat#: 10-040-CV), OVCAR-8 cells were cultured in DMEM (Corning cat#: 10-017-CV). Media was supplemented with 10% FBS (Corning cat#: 35011CV), 1% GlutaMAX (Gibco cat#: 35050-061), and 100μg/mL penicillin/streptomycin (Cytiva cat#: SV30010) and all cells were maintained at $3 7 ^ { \circ } \mathrm { C }$ in an incubator with 5% $\mathrm { C O } _ { 2 }$ and 100% humidity. For in vitro experiments, cells were cultured in low serum medium (1% FBS) unless otherwise stated. Treatment of 50μM palmitic acid (MilliporeSigma cat#: P0500) recapitulated the concentration of palmitic acid in 10% FBS media (20). Oleic acid (MilliporeSigma cat#: O3008) was added at different doses with the lowest dose of 13μM equivalent to that in media containing 10% FBS (20). All cell lines were authenticated by IDEXX BioAnalytics and were determined to be free of mycoplasma contamination by IDEXX BioAnalytics or Charles River Laboratories. In addition, cells were regularly tested for mycoplasma in our laboratory using a Universal Mycoplasma Detection Kit (ATCC cat#: 30-1012K).

Reagents: Palmitic acid (cat#: P0500), oleic acid (cat#: O3008), dimethyl sulphoxide (DMSO) (cat#: D2650) and Tween® 80 (cat#: P4780) were purchased from MilliporeSigma. CAY10566 (cat#: HY-15823) and PEG300 (cat#: HY-Y0873) were purchased from MedChemExpress. Saline (cat#: Z1376) was purchased from Intermountain Life Sciences.

Human specimens: An ovarian cancer tissue microarray (TMA) was obtained from the Cooperative Human Tissue Network (CHTN; $\mathrm { O v } ( \mathrm { a } 2 )$ , which contains different histological subtypes of ovarian cancer, benign ovarian tumors, and normal fallopian tube (see SM). Primary tumors or ascites from high grade serous ovarian cancer patients were collected at Northwestern Memorial Hospital from consenting donors. Tumor tissues were minced into small pieces and digested with in DMEM/F-12 medium (Gibco cat#: 11320-033) supplemented with 300U/mL collagenase (MilliporeSigma cat#: C7657) and 300U/mL hyaluronidase (MilliporeSigma cat#: H3506) at room temperature overnight. The next day, tissues were digested with trypsin (Corning cat#: 25054CI) at $3 7 ^ { \circ } \mathrm { C }$ for 10min, followed by treatment with 1X red blood cell lysis buffer (Biolegend cat#: 420301) on ice for 10min, and then with DNase I at $3 7 ^ { \circ } \mathrm { C }$ for 10min to produce a single-cell suspension. Cells were resuspended in RPMI-1640 with L-glutamine supplemented with 10% FBS, 1% GlutaMAX, and 1% Pen/Strep. For ascites, cells were spun down and resuspended in RPMI-1640 as described above.

Cell transfection; construction of SCD expression vector, RNA extraction and real-time qPCR, western blot and immunohistochemistry (IHC) were performed using protocols described previously (42-45) and detailed in the Supplementary Material (SM). Primers are included in Supplementary Table S1.

XBP1 splicing assay: Synthesized cDNA as described above was used to measure levels of unspliced and spliced XBP1mRNA were measured by regular PCR performed with GoTaq Green Master Mix (Promega cat#: M7123) on a T100 Thermo Cycler (Bio-Rad cat#: 186-1096). The primers targeting the spliced XBP1 region (116bp) (Supplementary Table S1) were designed according to a previous study (46). PCR products were resolved by agarose gel electrophoresis and visualized using GelGreen stain (Biotium cat#: 41005) on an ImageQuant LAS 4000 machine (GE Healthcare). Densitometric analysis of product bands was performed using the Gel Analyzer function in Fiji from NIH (47).

Lipidomics: Cell pellets were obtained from OVCAR-5 cells transduced with shRNA targeting SCD vs. control shRNA cells used for analysis at the Bindley Bioscience Center, Purdue University. Lipidomic analysis was performed using multiple reaction monitoring (MRM) profiling, as detailed in SM. For reporting of the relative amounts using normalization by the internal standards, the amount of each fatty acid was expressed as pg/1000 cells. For lipidomics profiling using the relative amounts, cells were lysed in ultrapure water for lipid extraction. Statistical analysis was performed utilizing MetaboAnalystR 3.0 (48). Data on the relative amounts from different lipid classes were scaled to obtain a normal distribution, and evaluated by univariate analysis, principal component analysis (PCA), and cluster analysis/heatmap. Informative lipids were analyzed according to class, fatty acyl residue chain unsaturation level.

SRS imaging: Stimulated Raman scattering (SRS) imaging was performed to measure isotope labelled cellular saturated/unsaturated fatty acids on a previously described lab-built system with a femtosecond laser source operating at 80MHz (InSight DeepSee, Spectra-Physics, Santa Clara, CA, USA) (11, 30). Briefly, the laser source provides two synchronized output beams, a tunable pump beam ranging from 680 nm to 1300 nm and a fixed 1040 nm Stokes beam, modulated at 2.3MHz by an acousto-optic modulator (1205-C, Isomet). SRS spectrum is obtained by controlling the temporal delay of two chirped femtosecond pulse. A 12.7cm long SF57 glass rod was used to chirped Stoke path to compensate for its longer wavelength. After combination, the path of both beams was further chirped by five 12.7cm long SF57 glass rods before sent to a laser-scanning microscope. A 60x water immersion objective (NA = 1.2, UPlanApo/IR, Olympus) was used to focus the light on the sample, followed by signal collection via an oil condenser (NA = 1.4, U-AAC, Olympus). For hyperspectral SRS (hSRS) imaging, a stack of 120 images was recorded at various pump-Stokes temporal delay, implemented by tuning the optical path difference between pump and Stokes beam through a translation delay stage. Pump beam was tuned to 798 nm for imaging at the C-H vibration region $( 2 8 0 0 \sim 3 0 5 0 \mathrm { c m } ^ { - 1 } )$ , and to 850 nm for imaging at C-D vibration region $( 2 1 0 0 \sim 2 3 0 0 ~ \mathrm { c m } ^ { - 1 } )$ . The power of pump and Stokes beam before microscope was 30mW and 200mW respectively. Raman shift was calibrated by standard samples, including DMSO, DMSO-d6, palmitic acid-d31 (PA-d31) and oleic acid-d34 (OA-d34). Hyperspectral SRS images were analyzed using ImageJ and previously described pixel-wise least absolute shrinkage and selection operator (LASSO) regression algorithm (49). In brief, LASSO can effectively decompose hSRS imaging into maps of different biomolecules by introducing a sparsity constraint to suppress the crosstalk between different chemical maps. PA d31 and OA-d34 was used to provide reference spectrum of SFA and USFA respectively for LASSO unmixing analysis. To study cellular uptake of fatty acids by SRS microscopy, cells were seeded on 35 mm glass-bottom dishes (Cellvis, D35-20-1.5-N) overnight, and then cultured in low serum medium for 24 hours, followed by treatment with 12.5μM PA-d31 (Cambridge Isotope Lab) for 24 hours. Rescue experiments were conducted by adding 52μM oleic acid to the low serum medium containing 12.5μM PA-d31 or changing to full serum medium with 12.5μM PA-d31. For quantitative SRS imaging, cells were fixed with 10% neutral buffered formalin for 30 min followed by 3 times of PBS wash.

Xenograft experiments: Athymic nude mice (strain: Foxn1nu), 6-8 weeks old, were obtained from Envigo (Indianapolis, IN, USA). For a subcutaneous model, mice were injected with $2 \times { 1 0 } ^ { 6 }$ OVCAR-3 cells stably transduced with shRNAs targeting SCD or control shRNA resuspended in 1/1 mix of RPMI 1640 basal medium and Matrigel (Corning cat#: 356234). Tumor length (L), width (W) and height (H) were measured every three days with digital calipers. Tumor volume was calculated using the formula $\mathbf { V } = \mathbf { L } \times \mathbf { H } \times \mathbf { W } / 2$ . For an intraperitoneal model, 5 million cells OVCAR-5 cells, or cells stably transduced with shRNAs targeting SCD or control shRNA were injected intraperitoneally (ip). Mice were euthanized 28 days after injection of cells to evaluate tumor growth and abdominal ascites. To determine the effects of a palmitic acid-enriched diet and SCD inhibitor combination, athymic nude mice were randomized to be fed with a palmitic acid-enriched or a control diet beginning one week before ip injection of OVCAR-5 cells, and continued for the duration of the experiment (28 days). Mice were treated ip with the SCD inhibitor CAY10566 (8 mg/kg body weight) or diluent (10% DMSO, 40% PEG300, 5% Tween-80, 45% saline), every other day during weekdays. The contents of palmitic acid in the palmitic acid-enriched diet and control were 30% and 11.7% of the total fatty acids, respectively. The levels of total fat (58g/kg) were the same, and levels of saturated fat, monounsaturated fat, polyunsaturated fat, stearic acid, and oleic acid were similar (< 2% difference) between the palmitic acid-enriched and control diets. The diets were custom-made by Teklad (Envigo).

RNA sequencing (RNA-seq) was performed as previously described (42, 43) and detailed in SM. Differentially expressed (DE) genes between experimental groups were determined and FDR corrected for multiple hypothesis testing with the edgeR package (50) in R. Pathway analysis based on the differentially expressed genes was performed using Ingenuity Pathway Analysis (IPA) software (QIAGEN).

The Genotype-Tissue Expression (GTEx) and The Cancer Genome Atlas (TCGA) ovarian cancer RNA-seq data analysis: Recomputed RSEM expected counts of fallopian tube samples (GTEx) and primary tumor samples from TCGA ovarian cancer patients were downloaded from UCSC Xena Browser. Expression of SCD (Ensembl ID: ENSG00000099194) was extracted from matrix of all genes and Student’s t test was performed on log2 transformed RSEM expected counts between fallopian tube samples and primary tumor samples. Data are deposited in GEO (GSE192442).

Cancer Dependency Map data analysis: Dependency score data from CRISPR screening in cancer cell lines was downloaded from Depmap Portal (14). Ovarian cancer cell lines were selected and Pearson correlation score was calculated between SCD and transcriptional regulators identified from IPA.

Apoptosis assay by IncuCyte imaging: Cells were seeded on 96-well plates at 500 per well and cultured in an IncuCyte S3 live-cell analysis system. Serum was reduced in the medium to 1% FBS, and Annexin V Green Dye (Sartorius cat#: 4642) was added for detection of apoptotic cells under different experimental conditions. Four images of bright field and green fluorescence were captured at three-hour intervals during a 72hr evaluation period. Cells were counted on the images and expressed as percentage of apoptotic cells (green cells/total cells under bright field).

Transmission Electron Microscopy: Cells were seeded at a density of 32,000 on glass bottom dishes (Cellvis cat#: D35-14-1.5-N) and cultured in regular medium for 48 hours. Culture conditions were changed to low serum medium (1% FBS) for an additional 48 hours. Cells were rinsed twice with PBS and fixed with 0.1M sodium cacodylate buffer, pH 7.3, containing 2% paraformaldehyde and 2.5% glutaraldehyde. Cells were post-fixed with 2% osmium tetroxide in unbuffered aqueous solution followed by rinsing with distilled water. Subsequently, cells were en-bloc stained with 3% uranyl acetate and rinsed with distilled water. Finally, cells were dehydrated in ascending grades of ethanol, transitioned with 1:1 mixture of ethanol and resin, and embedded in resin mixture of EMbed 812 Kit (Electron Microscopy Sciences cat#: 14120), cured in a $6 0 \%$ oven. Samples were sectioned on a Leica Ultracut UC6 ultramicrotome. Sections (70 nm) were collected on 200mesh copper grids and post stained with 3% uranyl acetate and

Reynolds lead citrate. Electron microscopic images were captured on a FEI Tecnai Spirit G2 transmission electron microscope.

Statistical Analyses: Data were analyzed by two-tailed Student t test. Two-way ANOVA was used for the analyses of the in vivo experiment with CAY10566 and palmitic acid-enriched diet. IHC staining analysis employed the Fisher exact test to compare the groups. Tumor weights and volumes from the subcutaneous mouse xenograft experiment were log transformed as paired samples before statistical analysis. $\mathrm { P } < 0 . 0 5$ was considered statistically significant. All statistical analyses except for RNA-seq and lipidomics were performed using GraphPad Prism v8.0.

## Data Availability

The RNA-sequencing data generated during the current study are available in the Gene Expression Omnibus repository with accession ID: GSE192442. OVCAR-5 SCD KD lipidomics profiling significant lipids species list and OVCAR-5 SCD KD RNA-seq significant genes list were included in the Supplementary Information Appendix. The datasets of all lipid species from untargeted lipidomics experiment during the current study are available from the corresponding author on reasonable request.

## Acknowledgements:

This work was supported by R01 CA224275 to DM and JXC, R33 CA223581 and NSF CHE1807106 grants to JXC. We thank Drs. Debabrata Chakravarti and Navdeep Chandel for valuable comments. Tumor specimens were procured through the Pathology Core and sequencing was performed in the NUSeq Core supported by NCI CCSG P30 CA060553 awarded to the Robert H Lurie Comprehensive Cancer Center. Lipidomics analysis was performed in Metabolite Profiling Facility at Bindley Bioscience Center, Purdue University. Transmission electron microscopy was performed in the Center for Advanced Microscopy/Nikon Imaging Center (CAM) at Northwestern University supported by NCI CA060553. This research was supported in part through the computational resources and staff contributions provided for the Quest high performance computing facility at Northwestern University which is jointly supported by the Office of the Provost, the Office for Research, and Northwestern University Information Technology.

## Author Contributions

JXC and DM designed this study. GZ, YT and DM drafted the manuscript. GZ, YT, HC, DV and JJW performed the experiments and collected the data. GZ, YT, HC, HH and YW conducted the statistical analysis. CRF performed the lipidomics experiment and initial analysis. RK contributed to TCGA and GTEx data analysis. HC, JXC and DM revised this manuscript. All authors read and approved the final manuscript.

## Ethics declarations

Human subject studies were conducted in accordance with the Declaration of Helsinki and approved by the IRB (Northwestern University IRB#: STU00202468). Animal studies were conducted according to a protocol approved by the Institutional Animal Care and Use Committee of Northwestern University (# IS00008973).

## Figure Legends

## Figure 1. SCD is highly expressed in ovarian cancer and is associated with increased levels

of free unsaturated fatty acids. (A) SCD expression from RNA-seq data in fallopian tube compared to ovarian cancer tumors in patients from the UCSC Xena Browser. Expression is shown as RSEM expected counts. (B, C) Real-time qRT-PCR analysis of SCD expression (mean ± SD, n = 3) (B), and western blot measurements of SCD protein levels (C) in immortalized fallopian tube luminal epithelial cells (FT190) and eleven ovarian cancer cell lines. (D) Representative images of IHC staining for SCD under 20X magnification in fallopian tube fimbriae (left panel), HGSOC specimens (middle panels). Negative control (IgG) is shown in right panel (tumor tissue). Scale bar corresponds to 50m. (E) SCD expression measured by $\mathrm { q R T - P C R }$ $\mathrm { \ m e a n } \pm \mathrm { \bf S D } .$ , n = 3) in OVCAR-5 cells transduced with shRNAs (1 or 2) targeting SCD (shSCD), or control shRNA (shCtrl). (F) Western blot of SCD in shCtrl and shSCD OVCAR-5 cells. (G) Lipidomics analysis of palmitic acid (16:0), palmitoleic acid (16:1), stearic acid (18:0), and oleic acid (18:1) in shCtrl and shSCD OVCAR-5 cells cultured in medium containing low serum (1% FBS) for 48 hours $( { \mathrm { m e a n s } } \pm { \mathrm { S D } }$ , n = 4). (H) Representative SRS images in C-H and C-D regions, and LASSO mappings of saturated fatty acid (SFA) and unsaturated fatty acids (USFA) in shSCD vs shCtrl OVCAR-5 cells treated with 12.5μM PA-d31 and cultured in low serum conditions. Scale bar: 10 µm. (I) Normalized SRS spectra of oleic acid-d34 (OA-d34) and palmitic acid-d31 (PA-d31) as reference spectrum of UFA and SFA respectively for LASSO analysis. (J) Quantitative analysis of LASSO mapped USFA and ratio between USFA and SFA in shSCD vs shCtrl OVCAR-5 cells. Each data point represents quantitative result from a single cell $( \mathtt { n } = 1 2 \AA - 1 4 )$ . \* $\mathsf { p } < 0 . 0 5$ , \*\* $\mathsf { p } < 0 . 0 1$ , \*\*\* $\mathbf { p } < 0 . 0 0 1$ , \*\*\*\* p < 0.0001.

## Figure 2. Restricting monounsaturated fatty acids activates the endoplasmic reticulum

stress response pathway. (A) Volcano plot of changes in phosphatidylcholine and sphingomyelin (PC & SM, green), phosphatidylethanolamine (PE, blue) and triacylglycerol (TAG, red) relative peak intensities measured by lipidomics profiling analysis in shSCD vs shCtrl OVCAR-5 cells cultured in low serum conditions for 48 hours. (B) Normalized peak intensities of phosphatidylcholine (PC) lipids with differing fatty chain plasticity (0°, no carboncarbon double bond; 1°, 1 or 2 carbon-carbon double bonds; 2°, more than 2 carbon-carbon double bonds) in shSCD vs shCtrl OVCAR-5 cells. ShSCD cells have significantly fewer $1 ^ { \circ } \mathrm { P C }$ lipids than shCtrl cells whereas no difference was observed for $0 ^ { \circ }$ or $2 ^ { \circ }$ PC lipids. (C) Fold change of triacylglycerol (TAG) lipids containing 16:0 or 18:0 fatty acyl chains integration and 16:1 or 18:1 fatty acyl chains integration determined by lipidomics profiling analysis in shSCD vs shCtrl OVCAR-5 cells. (D) Volcano plot of changes in gene expression measured by RNAseq in shSCD vs shCtrl OVCAR-5 cells. Red dots represent upregulated genes and blue dots, downregulated genes. Genes of the ER stress response pathway are indicated by lines. (E) Dot plot of the top 15 enriched Gene Ontology terms identified by analysis of upregulated genes (RNA-seq) in shSCD vs shCtrl OVCAR-5 cells. Dot size corresponds to ratio of genes on the pathway vs total number of upregulated genes. Background color corresponds to FDR q value. (F) Enrichment plots generated by Gene Set Enrichment Analysis of gene expression (RNA-seq normalized counts) in OVCAR-5 shSCD vs shCtrl using Hallmark and C2 gene sets from Molecular Signatures Database. (G) Top ten significant upstream regulators identified by Ingenuity Pathway Analysis using differentially expressed genes from RNA-seq analysis of OVCAR-5 shSCD vs shCtrl cells. Transcription factors involved in the ER stress response pathway are in bold characters. (H) Heatmap of expression (RNA-seq normalized counts) and supervised hierarchical clustering of significant genes of the ER stress response pathway in shCtrl and shSCD OVCAR-5 cells $( \mathbf { n } = 3 ) . ^ { \mathrm { ~ * ~ } } \mathbf { p } < 0 . 0 5 , ^ { \mathrm { ~ * * } } \ \mathbf { p } < 0 . 0 1 , ^ { \mathrm { ~ * * * } } \ \mathbf { p } < 0 . 0 0 1 , ^ { \mathrm { ~ * * * } } \ \mathbf { p } < 0 . 0 0 1 , ^ { \mathrm { ~ * * * * } } \ \mathbf { p } <$ 0.0001.

## Figure 3. The IRE1α/XBP1 and PERK/eIF2α/ATF4 axes of the ER stress response pathway are activated in ovarian cancer cells under restricted availability of unsaturated fatty acid.

(A) XBP1 splicing (u, unspliced transcript; s, spliced transcript) measured by RT-PCR and agarose-gel electrophoresis in OVCAR-5 cells transduced with control shRNA (shCtrl) or shRNAs (1 or 2) targeting SCD (shSCD) and cultured in low serum conditions (1% FBS) for 48 hours. (B) Densitometric analysis of XBP1 splicing products shown in A. Bars represent percent of spliced XBP1 relative to total XBP1 $( \mathrm { m e a n } \pm \mathrm { S D } , \mathrm { n } = 3 )$ . (C) XBP1 splicing (u, unspliced transcript; s, spliced transcript) in OVCAR-5 cells cultured in low serum conditions and treated with SCD inhibitor CAY10566 for 48 hours. (D) Percent of spliced XBP1 isoform measured by densitometric analysis of PCR products shown in C (mean ± SD, n = 3). (E, F) XBP1 splicing (u, unspliced transcript; s, spliced transcript) (E), and western blot of proteins of the PERK/eIF2α/ATF4 axis (F) in shCtrl and shSCD OVCAR-5 cells cultured under low serum conditions and treated with 50μM palmitic acid for the time periods indicated. (G) XBP1 splicing (u, unspliced transcript; s, spliced transcript) in primary cells from tumors of ovarian cancer patients cultured in low serum conditions and treated with 3μM CAY10566 for 48 hours, or with 1μM CAY10566 and 50μM palmitic acid for 12 hours. (H) Representative SRS images in the C-H and C-D regions of OVCAR-5 shCtrl and shSCD cells cultured in low serum conditions (1% FBS) and treated with 12.5μM palmitic acid-d31 (PA-d31), with or without 52μM oleic acid (OA), or cultured in medium with full serum (10% FBS) and treated with PA-d31 for 24 hr. Yellow arrows indicate rigid ER, gray arrows indicate lipid droplet (LD), and blue arrows indicate cytoplasm. Scale bar: 20 µm. (I) Percentages of shCtrl and shSCD OVCAR-5 cells treated as described in (H) showing C-D SRS signal mainly in rigid ER, lipid droplet (LD), and cytoplasm (n = 139-191). (J) Transmission electron microscopy imaging of smooth ER (red arrows) in OVCAR-5 shCtrl vs shSCD cells cultured in low serum conditions for 48 hours. \* p < 0.05, \*\* $\mathsf { p } < 0 . 0 1$ , \*\*\* $\mathrm { p } < 0 . 0 0 1$ , \*\*\*\* $\mathsf { p } < 0 . 0 0 0 1$ .

Figure 4. Unsaturated fatty acid-induced ER stress response is reversed by exogenous oleic acid. (A, B) XBP1 splicing (u, unspliced transcript; s, spliced transcript) measured by RT-PCR and agarose gel electrophoresis in OVCAR-5 cells transduced with control shRNA (shCtrl) or shRNAs (1 or 2) targeting SCD (shSCD), cultured in medium containing low serum, and treated with indicated doses of oleic acid for 48 hours (A), or with 50μM palmitic acid and indicated doses of oleic acid for 12 hours (B). (C, D) Western blot of SCD and proteins of the PERK/eIF2α/ATF4 axis in shCtrl and shSCD cells cultured in low serum medium, and treated with different doses of oleic acid for 48 hours (C), or with 50μM palmitic acid and indicated doses of oleic acid for 12 hours (D). (E, F) XBP1 splicing (u, unspliced transcript; s, spliced transcript) in OVCAR-5 cells cultured in medium containing low serum and treated with 21.6nM CAY10566 and indicated doses of oleic acid for 48 hours (E), or with 8.1nM CAY10566, 50μM palmitic acid and indicated doses of oleic acid for 12 hours. (G) Proteins of the PERK/eIF2α/ATF4 pathway measured by western blot in OVCAR-5 cells treated as described in (E). (H) Western blot of proteins of the PERK/eIF2α/ATF4 pathway in OVCAR-5 cells treated as described in (F). Arrows indicate the band of interest. (I, J) Verification of SCD overexpression by qRT-PCR (I) and western blotting (J) in OVCAR-5 cells transduced with a SCD expression vector (pLenti-SCD). Cells transduced with empty vector (pLenti-Ctrl) served as control. Bars represent means ± SD, n = 3. (K) XBP1 splicing (u, unspliced transcript; s, spliced transcript) in pLenti-SCD vs pLenti-Ctrl cells cultured in low serum conditions and treated with $5 0 \mu \mathrm { M }$ palmitic acid for 12 hours. (M) Percent of spliced isoform (mean ± SD, n = 3) calculated by densitometric analysis of PCR products shown in (L). $^ { * } \mathrm { ~ p } < 0 . 0 5 , ^ { * * } \mathrm { ~ p } < 0 . 0 1$ , \*\*\* $\mathfrak { p } < 0 . 0 0 1 , ^ { * * * * } \mathfrak { p } < 0 . 0 0 0 1$ .

Figure 5. Apoptosis induced by SCD inhibition, or treatment with palmitic acid, is attenuated by exogenous oleic acid or SCD overexpression. (A-B) Time-lapse imaging of Annexin V staining to measure apoptosis in OVCAR-5 cells transduced with control shRNA (shCtrl) or shRNA targeting SCD (shSCD), cultured in low serum conditions, and treated with 52μM oleic acid (A), or with 50μM palmitic acid alone or in combination with 52μM oleic acid (B). (C-D) Time-lapse of Annexin V imaging to measure apoptosis in OVCAR-5 cells cultured in low serum conditions and treated with 21.6nM CAY10566, 52μM oleic acid or combination (C), or with 8.1nM CAY10566, 50μM palmitic acid, 52μM oleic acid, or combinations (D). (E) Western blot of full-length and cleaved caspase-3 in shSCD vs shCtrl cells cultured under low serum medium and treated with 50μM palmitic acid and indicated doses of oleic acid for 12 hours. (F) Western blot of full-length and cleaved caspase-3 in OVCAR-5 cells cultured in low serum medium and treated with 8.1nM CAY10566, 50μM palmitic acid and indicated doses of oleic acid for 12 hours. (G) Time-lapse of Annexin V imaging to determine apoptosis in OVCAR-5 cells overexpressing SCD (pLenti-SCD) and control cells (pLenti-Ctrl), cultured in medium containing low serum and treated with 50μM palmitic acid. Values in panels A-D & G are $\mathrm { m e a n s \pm S D , n = 6 . ~ ^ { * } \mathtt { p } < 0 . 0 5 , ~ ^ { * * } \mathtt { p } < 0 . 0 1 , ~ ^ { * * * } \mathtt { p } < 0 . 0 0 1 , ~ ^ { * * * * } \mathtt { p } < 0 . 0 0 1 , ~ ^ { * * * * } \mathtt { p } < 0 . 0 0 0 1 }$ .

Figure 6. SCD knockdown inhibited growth of ovarian cancer xenografts in mice. (A-C) Total tumor weight (A), total tumor volume (B) and total number of metastases (C) in athymic nude mice intraperitoneally injected with OVCAR-5 cells transduced with control shRNA (shCtrl) or shRNA targeting SCD (shSCD), and evaluated after 28 days (values are means $\pm \mathrm { S E } ,$ , n = 14 per group). (D) qRT-PCR measurements of SCD expression (mean ± SD, n = 6) in a random sample of tumor xenografts described in (A). (E, F) Agarose gel electrophoresis of XBP1 splicing products (u, unspliced transcript; s, spliced transcript) (E), and percent spliced XBP1 isoform estimated by image analysis of transcript bands (mean ± SD, n = 6) (F) in a random sample of tumor xenografts described in (A). (G, H) Ascites volume (G) and total number of metastases (H) in athymic nude mice intraperitoneally injected with OVCAR-5 cells, fed with a palmitic acid-rich diet or control diet, and treated with SCD inhibitor CAY10566 or vehicle for 28 days. Values are means ± SE, n = 10. (I-L) XBP1 splicing products (u, unspliced transcript; s, spliced transcript) (I, K), and percent intensity of the spliced transcript estimated by image analysis (J, L) in a random sample (n = 5) of tumor xenografts described in (F). Values are $\mathrm { m e a n s \pm S D . ~ ^ { * } ~ p < 0 . 0 5 , ^ { * * } ~ p < 0 . 0 1 , ^ { * * * } ~ p < 0 . 0 0 1 , ^ { * * * * } ~ p < 0 . 0 0 1 , ^ { * * * * } ~ p < 0 . 0 0 0 1 }$ .

## Reference

1. Zhao G, Cardenas H, & Matei D (2019) Ovarian Cancer-Why Lipids Matter. Cancers (Basel) 11(12).  
2. Ladanyi A, et al. (2018) Adipocyte-induced CD36 expression drives ovarian cancer progression and metastasis. Oncogene 37(17):2285-2301.  
3. Nieman KM, et al. (2011) Adipocytes promote ovarian cancer metastasis and provide energy for rapid tumor growth. Nat Med 17(11):1498-1503.  
4. Cancer Genome Atlas Research N (2011) Integrated genomic analyses of ovarian carcinoma. Nature 474(7353):609-615.  
5. Peck B & Schulze A (2016) Lipid desaturation - the next step in targeting lipogenesis in cancer? FEBS J 283(15):2767-2778.  
6. Du X, et al. (2012) FGFR3 stimulates stearoyl CoA desaturase 1 activity to promote bladder tumor growth. Cancer research 72(22):5843-5855.  
7. Roongta UV, et al. (2011) Cancer cell dependence on unsaturated fatty acids implicates stearoyl-CoA desaturase as a target for cancer therapy. Molecular cancer research : MCR 9(11):1551- 1561.  
8. Tesfay L, et al. (2019) Stearoyl-CoA Desaturase 1 Protects Ovarian Cancer Cells from Ferroptotic Cell Death. Cancer research 79(20):5355-5366.  
9. Cheng JX & Xie XS (2015) Vibrational spectroscopic imaging of living systems: An emerging platform for biology and medicine. Science 350(6264):aaa8870.  
10. Zhang D, Wang P, Slipchenko MN, & Cheng JX (2014) Fast vibrational imaging of single cells and tissues by stimulated Raman scattering microscopy. Accounts of chemical research 47(8):2282- 2290.  
11. Li J, et al. (2017) Lipid Desaturation Is a Metabolic Marker and Therapeutic Target of Ovarian Cancer Stem Cells. Cell stem cell 20(3):303-314 e305.  
12. Xie Z, Ferreira CR, Virequ AA, & Cooks RG (2021) Multiple reaction monitoring profiling (MRM profiling): Small molecule exploratory analysis guided by chemical functionality. Chemistry and Physics of Lipids 235:105048.  
13. Surma MA, et al. (2021) Mouse lipidomics reveals inherent flexibility of a mammalian lipidome. Scientific reports 11(1):19364.  
14. Tsherniak A, et al. (2017) Defining a Cancer Dependency Map. Cell 170(3):564-576.e516.  
15. Ghandi M, et al. (2019) Next-generation characterization of the Cancer Cell Line Encyclopedia. Nature 569(7757):503-508.  
16. Volmer R, van der Ploeg K, & Ron D (2013) Membrane lipid saturation activates endoplasmic reticulum unfolded protein response transducers through their transmembrane domains. Proceedings of the National Academy of Sciences of the United States of America 110(12):4628- 4633.  
17. Calfon M, et al. (2002) IRE1 couples endoplasmic reticulum load to secretory capacity by processing the XBP-1 mRNA. Nature 415(6867):92-96.  
18. Harding HP, Zhang Y, & Ron D (1999) Protein translation and folding are coupled by an endoplasmic-reticulum-resident kinase. Nature 397(6716):271-274.  
19. Harding HP, et al. (2000) Regulated translation initiation controls stress-induced gene expression in mammalian cells. Molecular cell 6(5):1099-1108.  
20. Vriens K, et al. (2019) Evidence for an alternative fatty acid desaturation pathway increasing cancer plasticity. Nature 566(7744):403-406.  
21. Hetz C (2012) The unfolded protein response: controlling cell fate decisions under ER stress and beyond. Nature Reviews Molecular Cell Biology 13(2):89-102.  
22. Wikstrom JD, et al. (2013) AMPK regulates ER morphology and function in stressed pancreatic beta-cells via phosphorylation of DRP1. Molecular endocrinology 27(10):1706-1723.  
23. Nakamura MT & Nara TY (2004) Structure, function, and dietary regulation of delta6, delta5, and delta9 desaturases. Annu Rev Nutr 24:345-376.  
24. Doria ML, et al. (2014) Fatty acid and phospholipid biosynthetic pathways are regulated throughout mammary epithelial cell differentiation and correlate to breast cancer survival. FASEB journal : official publication of the Federation of American Societies for Experimental Biology 28(10):4247-4264.  
25. Fritz V, et al. (2010) Abrogation of de novo lipogenesis by stearoyl-CoA desaturase 1 inhibition interferes with oncogenic signaling and blocks prostate cancer progression in mice. Molecular cancer therapeutics 9(6):1740-1754.  
26. Southam AD, et al. (2015) Drug Redeployment to Kill Leukemia and Lymphoma Cells by Disrupting SCD1-Mediated Synthesis of Monounsaturated Fatty Acids. Cancer research 75(12):2530-2540.  
27. Vacaresse N, et al. (1999) Activation of epithelial growth factor receptor pathway by unsaturated fatty acids. Circ Res 85(10):892-899.  
28. Petrek JA, Hudgins LC, Ho M, Bajorunas DR, & Hirsch J (1997) Fatty acid composition of adipose tissue, an indication of dietary fatty acids, and breast cancer prognosis. Journal of clinical oncology : official journal of the American Society of Clinical Oncology 15(4):1377-1384.  
29. Chajes V, et al. (1999) Fatty-acid composition in serum phospholipids and risk of breast cancer: an incident case-control study in Sweden. International journal of cancer 83(5):585-590.  
30. Li J, et al. (2021) Metabolic Reprogramming from Glycolysis to Fatty Acid Uptake and beta-Oxidation in Platinum-Resistant Cancer Cells. bioRxiv:2021.2005.2017.444564.  
31. Yue S, et al. (2014) Cholesteryl ester accumulation induced by PTEN loss and PI3K/AKT activation underlies human prostate cancer aggressiveness. Cell metabolism 19(3):393-406.  
32. Li J, et al. (2016) Abrogating cholesterol esterification suppresses growth and metastasis of pancreatic cancer. Oncogene 35(50):6378-6388.  
33. Huang KC, Li J, Zhang C, Tan Y, & Cheng JX (2020) Multiplex Stimulated Raman Scattering Imaging Cytometry Reveals Lipid-Rich Protrusions in Cancer Cells under Stress Condition. iScience 23(3):100953.  
34. Bowers M, et al. (2020) FASN-Dependent Lipid Metabolism Links Neurogenic Stem/Progenitor Cell Activity to Learning and Memory Deficits. Cell stem cell 27(1):98-109 e111.  
35. Lu J, et al. (2012) Palmitate causes endoplasmic reticulum stress and apoptosis in human mesenchymal stem cells: prevention by AMPK activator. Endocrinology 153(11):5275-5284.  
36. Pinkham K, et al. (2019) Stearoyl CoA Desaturase Is Essential for Regulation of Endoplasmic Reticulum Homeostasis and Tumor Growth in Glioblastoma Cancer Stem Cells. Stem cell reports 12(4):712-727.  
37. Mujcic H, et al. (2013) Hypoxic activation of the PERK/eIF2alpha arm of the unfolded protein response promotes metastasis through induction of LAMP3. Clinical cancer research : an official journal of the American Association for Cancer Research 19(22):6126-6137.  
38. Feng YX, et al. (2014) Epithelial-to-mesenchymal transition activates PERK-eIF2alpha and sensitizes cells to endoplasmic reticulum stress. Cancer discovery 4(6):702-715.  
39. Chen X, et al. (2014) XBP1 promotes triple-negative breast cancer by controlling the HIF1alpha pathway. Nature 508(7494):103-107.  
40. Lien EC, et al. (2021) Low glycaemic diets alter lipid metabolism to influence tumour growth. Nature 599(7884):302-307.  
41. Pascual G, et al. (2021) Dietary palmitic acid promotes a prometastatic memory via Schwann cells. Nature 599(7885):485-490.  
42. Huang H, et al. (2020) FTO-Dependent N6-Methyladenosine Modifications Inhibit Ovarian Cancer Stem Cell Self-Renewal by Blocking cAMP Signaling. Cancer research 80(16):3200-3214.  
43. Wang Y, et al. (2021) Frizzled-7 Identifies Platinum-Tolerant Ovarian Cancer Cells Susceptible to Ferroptosis. Cancer Res 81(2):384-399.  
44. Condello S, et al. (2018) Tissue Tranglutaminase Regulates Interactions between Ovarian Cancer Stem Cells and the Tumor Niche. Cancer Research 78(11):2990-3001.  
45. Horacio Cardenas GJ, Jessica Thomes Pepin, J. Brandon Parker, Salvatore Condello, Kenneth P. Nephew, Harikrishna Nakshatri, Debabrata Chakravarti, Yunlong Liu, and Daniela Matei (2019) Interferon-γ Signaling is Associated with BRCA1 Loss-of-Function Mutations in High Grade Serous Ovarian Cancer. Npj Precision Oncology in press.  
46. Song M, et al. (2018) IRE1α–XBP1 controls T cell function in ovarian cancer by regulating mitochondrial activity. Nature 562(7727):423-428.  
47. Schneider CA, Rasband WS, & Eliceiri KW (2012) NIH Image to ImageJ: 25 years of image analysis. Nature methods 9(7):671-675.  
48. Pang Z, Chong J, Li S, & Xia J (2020) MetaboAnalystR 3.0: Toward an Optimized Workflow for Global Metabolomics. Metabolites 10(5).  
49. Lin H, et al. (2021) Microsecond fingerprint stimulated Raman spectroscopic imaging by ultrafast tuning and spatial-spectral learning. Nature communications 12(1):3052.

50. Robinson MD, McCarthy DJ, & Smyth GK (2010) edgeR: a Bioconductor package for differentia expression analysis of digital gene expression data. Bioinformatics 26(1):139-140.

A  
![](images/814635a8f6e61d649cadef5b60f91c33d1a3b83f1bfb7efb1d772ceb2284d92e.jpg)

<details>
<summary>bar chart</summary>

| Group        | RSEM expected counts |
| ------------ | -------------------- |
| Fallopian Tube | 0                    |
| Tumor        | 50000                |
</details>

B

![](images/58f2f52f5a33223901428661d6d93838746a5d8d47f9fba23978f28350b8fa27.jpg)

<details>
<summary>bar chart</summary>

| Gene      | Relative SOD mRNA level |
| --------- | ------------------------ |
| FT190     | 1                        |
| CAOV3     | 8                        |
| COV362    | 15                       |
| Hey A8    | 24                       |
| Kuramochi | 22                       |
| OVCAR-3   | 7                        |
| OVCAR-4   | 20                       |
| OVCAR-5   | 13                       |
| OVCAR-8   | 26                       |
| OV90      | 28                       |
| PEO1      | 13                       |
| PEO4      | 16                       |
</details>

c  
![](images/7eab38e5ae6738514e15ce421ea2245ae61fa8ac3f26aee58200711d0455e539.jpg)

<details>
<summary>text_image</summary>

FT190
CAOV3
COV362
Hey A8
Kuramochi
OVCAR-3
OVCAR-4
OVCAR-5
OVCAR-8
OV90
PEO1
PEO4
SCD
GAPDH
</details>

D  
![](images/8ae730e30d80ea8df634fe4871ba34ba5826855f144324cf3495840ed593ef40.jpg)

<details>
<summary>bar chart</summary>

| Group | Relative SCD mRNA level |
|-------|--------------------------|
| shCtrl | 1.0 |
| shSCD-1 | 0.3 |
| shSCD-2 | 0.4 |
</details>

G

![](images/612a5b16545f47df582b35823668d592b10e9a2c5eac4c4f719e6157181a42d1.jpg)

<details>
<summary>bar chart</summary>

| Group   | Free palmitic acid (pg/1000 cells) | Free palmitoleic acid (pg/1000 cells) | Free stearic acid (pg/1000 cells) | Free oleic acid (pg/1000 cells) |
|---------|--------------------------------------|----------------------------------------|------------------------------------|----------------------------------|
| shCtrl  | 300                                  | 150                                    | 700                                | 200                              |
| shSCD   | 280                                  | 250                                    | 600                                | 150                              |
</details>

![](images/d94236d837e5908b4d79527cdfea4bef255e8ebd6ea1b799d47d0aa2fe3ad0e9.jpg)

<details>
<summary>text_image</summary>

H
C-H	C-D	LASSO mapped SFA	LASSO mapped USFA
OVCAR-5 shCtrl
OVCAR-5 shSCD
</details>

-  
![](images/b8781bd062492526e8a43b0a6a8290b089476870b13f2d1cabf958536bfa0359.jpg)

<details>
<summary>line chart</summary>

| Raman shift (cm⁻¹) | OA-d34 | PA-d31 |
| ------------------ | ------ | ------ |
| 2100               | 0.0    | 0.0    |
| 2200               | 1.0    | 0.95   |
| 2300               | 0.1    | 0.1    |
</details>

J  
![](images/04234bc3f51a0d3fb7c9513a1daf658e3fbb7fc8fda125666bcf9ee05b11374c.jpg)

<details>
<summary>scatterplot</summary>

| Group   | UFA (a.u.) | UFA/SFA |
|---------|------------|---------|
| shCtrl  | ~900       | ~2.5    |
| shSCD   | ~100       | ~1.5    |
</details>

Figure 1

A  
![](images/0f6d7e60dccbe79d6c4393ca311b6317ebbbd2ab8a2ea81be0c16ae070748238.jpg)  
B

![](images/96fc87403345ee51a37da543e594e44f78821c201eceaf78bafe3e641451c643.jpg)

<details>
<summary>scatterplot</summary>

| Plasticity Level | shCtrl | shSCD |
| ---------------- | ------ | ----- |
| 0°               | -1.0   | -1.0  |
| 1°               | -1.0   | -1.0  |
| 2°               | -1.0   | -1.0  |
</details>

c  
![](images/55b6ab4e07d2b72c6ded0651d63e5a0201fe5cc89b2ad96b60883799f49ba41e.jpg)

<details>
<summary>scatterplot</summary>

| Integration Group | Fold change (shSCD/shCtrl) |
| ----------------- | --------------------------- |
| 16:0/18:0         | 1.4                         |
| 16:0/18:0         | 1.5                         |
| 16:0/18:0         | 1.6                         |
| 16:0/18:0         | 1.7                         |
| 16:0/18:0         | 1.8                         |
| 16:0/18:0         | 1.9                         |
| 16:0/18:0         | 2.0                         |
| 16:0/18:0         | 2.1                         |
| 16:0/18:0         | 2.2                         |
| 16:0/18:0         | 2.3                         |
| 16:0/18:0         | 2.4                         |
| 16:0/18:0         | 2.5                         |
| 16:0/18:0         | 2.6                         |
| 16:0/18:0         | 2.7                         |
| 16:0/18:0         | 2.8                         |
| 16:0/18:0         | 2.9                         |
| 16:0/18:0         | 3.0                         |
| 16:0/18:0         | 3.1                         |
| 16:0/18:0         | 3.2                         |
| 16:0/18:0         | 3.3                         |
| 16:0/18:0         | 3.4                         |
| 16:0/18:0         | 3.5                         |
| 16:0/18:0         | 3.6                         |
| 16:0/18:0         | 3.7                         |
| 16:0/18:0         | 3.8                         |
| 16:0/18:0         | 3.9                         |
| 16:0/18:0         | 4.0                         |
| 16:0/18:0         | 4.1                         |
| 16:0/18:0         | 4.2                         |
| 16:0/18:0         | 4.3                         |
| 16:0/18:0         | 4.4                         |
| 16:0/18:0         | 4.5                         |
| 16:0/18:0         | 4.6                         |
| 16:0/18:0         | 4.7                         |
| 16:0/18:0         | 4.8                         |
| 16:0/18:0         | 4.9                         |
| 16:0/18:0         | 5.0                         |
| 16:0/18:0         | 5.1                         |
| 16:0/18:0         | 5.2                         |
| 16:0/18:0         | 5.3                         |
| 16:0/18:0         | 5.4                         |
| 16:0/18:0         | 5.5                         |
| 16:0/18:0         | 5.6                         |
| 16:0/18:0         | 5.7                         |
| 16:0/18:0         | 5.8                         |
| 16:0/18:0         | 5.9                         |
| 16:0/18:0         | 6.0                         |
| 16:0/18:0         | 6.1                         |
| 16:0/18:0         | 6.2                         |
| 16:0/18:0         | 6.3                         |
| 16:0/18:0         | 6.4                         |
| 16:0/18:0         | 6.5                         |
| 16:0/18:0         | 6.6                         |
| 16:0/18:0         | 6.7                         |
| 16:0/18:0         | 6.8                         |
| 16:0/18:0         | 6.9                         |
| 16:0/18:0         | 7.0                         |
| 16:0/18:0         | 7.1                         |
| 16:0/18:0         | 7.2                         |
| 16:0/18:0         | 7.3                         |
| 16:0/18:0         | 7.4                         |
| 16:0/18:0         | 7.5                         |
| 16:0/18:0         | 7.6                         |
| 16:0/18:0         | 7.7                         |
| 16:0/18:0         | 7.8                         |
| 16:0/18:0         | 7.9                         |
| 16:0/18:0         | 8.0                         |
| 16:0/18:0         | 8.1                         |
| 16:0/18:0         | 8.2                         |
| 16:0/18:0         | 8.3                         |
| 16:0/18:0         | 8.4                         |
| 16:0/18:0         | 8.5                         |
| 16:0/18:0         | 8.6                         |
| 16:0/18:0         | 8.7                         |
| 16:0/18:0         | 8.8                         |
| 16:0/18:0         | 8.9                         |
| 16:0/18:0         | 9.0                         |
| 16:0/18:0         | 9.1                         |
| 16:0/18:0         | 9.2                         |
| 16:0/18:0         | 9.3                         |
| 16:0/18:0         | 9.4                         |
| 16:0/18:0         | 9.5                         |
| 16:0/18:0         | 9.6                         |
| 16:0/18:0         | 9.7                         |
| 16:0/18:0         | 9.8                         |
| 16:0/18:0         | 9.9                         |
| 16:0/18:0         | 10.0                        |
| 25-              | *                           |
</details>

D  
![](images/3a1987426f2b0dcc2dd12ec1bca7ec8ad9169e6dae9051c888ccc41a7fd01db0.jpg)

<details>
<summary>scatterplot</summary>

| Gene | -log10 FDR | log1 Fold Change |
| --- | --- | --- |
| DDIT3 | ~40 | ~3.5 |
| ATF3 | ~30 | ~2.5 |
| BHLHA15 | ~25 | ~2.5 |
| PPPR15A | ~20 | ~-1.5 |
| HERRUD1 | ~18 | ~-1.5 |
| CEBPB | ~15 | ~-1.5 |
| CHAC1 | ~12 | ~-1.5 |
| DNAJB9 | ~10 | ~-1.5 |
| ERMP4 | ~8 | ~-2.0 |
| FICD | ~6 | ~-2.0 |
| WEGFA | ~5 | ~-2.0 |
| BBC3 | ~4 | ~-2.0 |
| MTC2 | ~3 | ~-2.0 |
| CLGN | ~2 | ~-2.0 |
| PSAT1 | ~1 | ~-2.0 |
| WIPI1 | ~0.5 | ~-2.0 |
| ATF3 | ~30 | ~2.5 |
| BHLHA15 | ~25 | ~2.5 |
</details>

F

![](images/4282ba78ae14724e45a67536da1fc36a5354d5a1de36ce6d1b42314d5e0e379d.jpg)

<details>
<summary>line chart</summary>

| Dataset | Enrichment score (ES) | Ranked list metric (Signal/Noise) | NES (positive correlated) | q-value |
|---------|------------------------|----------------------------------|--------------------------|---------|
| HALLMARK | ~0.5 | ~0 | NES = 2.26, q = 1.42×10⁻⁴ | |
| REACTOME_IRE1Alpha_ACTIVATES_CHAPERONES | ~0.5 | ~0 | NES = 1.91, q = 0.026 | |
| REACTOME_PERK_REGULATES_GENE_EXPRESSION | ~0.7 | ~0 | NES = 2.21, q = 5.45×10⁻⁴ | |
| REACTOME_ATF4_ACTIVATES_GENES_IN_RESPONSE_TO_ENDOPLASMIC_RETICULUM_STRESS | ~0.6 | ~0 | NES = 2.24, q = 3.18×10⁻⁴ | |
</details>

G  
![](images/e50b4772cd99f4247a1cda2d6b5392a15f60b6c4d0868a8589d6750f1a721e70.jpg)

<details>
<summary>bar chart</summary>

| Transcription Regulators | Activation z-score | -log10(p value) |
| ------------------------ | ------------------ | --------------- |
| NUPR1                    | 5                  | 8               |
| DDIT3                    | 8                  | 6               |
| MEF2D                    | 9                  | 4               |
| ATF4                     | 10                 | 12              |
| BRCA1                    | 7                  | 5               |
| SREBF1                   | 6                  | 4               |
| FOSL2                    | 5                  | 3               |
| JUNB                     | 4                  | 2               |
| MYRF                     | 3                  | 2               |
| REL                      | 2                  | 1               |
</details>

H  
![](images/74a39a7a05afa8fcdc5d85bb42ec862030aa767229c43646c6f27d0282cdc0a9.jpg)

<details>
<summary>heatmap</summary>

|  | shCtrl.1 | shCtrl.2 | shCtrl.3 | shSCD.1 | shSCD.2 | shSCD.3 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.75 | -0.75 | 0 | 1.5 | 0 | -1.5 |
| 2 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 13 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 14 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 15 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 16 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 17 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 18 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 19 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 20 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 21 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 22 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 23 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 24 | 0 | 0 | 0 | 0.75 | 0 | 0 |
| 25 | 0 | 0 | 0 | -1.5 | -1.5 | -1.5 |
</details>

Figure 2

A  
![](images/e578ea8ed13f032417fbaa911566f24f9472b9e4c693adbb6d05b76c002c003f.jpg)  
B

![](images/3d289f45e9f3a28a57362d7fc3cba211624ef24e7ba74a8b485a16a66e5b2394.jpg)

<details>
<summary>bar chart</summary>

| Group     | Spliced XBP1 (%) |
| --------- | ----------------- |
| shCtrl    | 0                 |
| shSCD-1   | 30                |
| shSCD-2   | 35                |
</details>

c  
![](images/4e533f9e3286f2954d4432d8bc8bedab5cbc32f84c4ff2c3d804d78f45883971.jpg)

<details>
<summary>text_image</summary>

CAY10566 (nM)
0	8.1	13.5	21.6	24.3
XBP1
u
s
GAPDH
</details>

D

![](images/e1050368b38b16053f2802b89600b01422cebd1a27ae5fdf8d5a894209457168.jpg)

<details>
<summary>bar chart</summary>

| CAY10566 (nM) | Spliced XBP1 (%) |
| ------------- | ----------------- |
| 0             | 0                 |
| 8.1           | 10                |
| 13.5          | 40                |
| 21.6          | 75                |
| 24.3          | 80                |
</details>

G  
![](images/e454ddd38629a92f8f484ab316d3c870ad0aa7cbc71dc14a1d9fbaaa2810a797.jpg)

<details>
<summary>text_image</summary>

CAY10566 (µM)
0 3 0 1
XBP1
GAPDH
Palmitic
acid
0µM 50µM
</details>

![](images/21f305d11046b54fcbfb590666cc991d1d0df221a0319aae494e6c888a271d13.jpg)

<details>
<summary>text_image</summary>

E
XBP1
GAPDH
Palmitic
acid, 50µM
0hr	1hr	2hr	4hr	4hr	8hr	12hr	24hr
shCtrl	shSCD-1	shSCD-2	shCtrl	shSCD-1	shSCD-2	shCtrl	shSCD-1	shSCD-2	shCtrl	shSCD-1	shSCD-2
← u
← s
</details>

F  
![](images/235190ae45d08bd1874fd7695a187c23623f311d37e8ae49de26ed373dea6cc8.jpg)

<details>
<summary>text_image</summary>

PERK
p-eIF2α
eIF2α
ATF4
CHOP
SCD
GAPDH
Palmitic
acid, 50µM
0hr	1hr	2hr	4hr	4hr	8hr	12hr	24hr
</details>

I  
J

![](images/e479c44219ad65710dd335d1d6561dda92f733e2fbfa06574bd321633e65d7d3.jpg)

<details>
<summary>bar chart</summary>

| Group | LD | Cytoplasm | Rigid ER |
| --- | --- | --- | --- |
| shCtrl + PA-d31 | 100 | 20 | 20 |
| shCtrl + PA-d31 + OA | 100 | 20 | 20 |
| shCtrl + PA-d31 + 10% FBS | 100 | 20 | 20 |
| shSCD + PA-d31 | 100 | 20 | 60 |
| shSCD + PA-d31 + OA | 100 | 20 | 20 |
| shSCD + PA-d31 + 10% FBS | 100 | 20 | 20 |
</details>

![](images/76751fdf819300df0684e4bf0d0153c0fd97aae62a6c3fcd15ee7ce2e213829a.jpg)

<details>
<summary>text_image</summary>

shCtrl
shSCD
</details>

H  
![](images/fbec3e02245349f20dc05b35ac3c95567fbeb3580c55f158e93a4778cee9fead.jpg)

<details>
<summary>text_image</summary>

shCtrl
1% FBS +
PA-d31
1% FBS +
PA-d31 +
52µM OA
10% FBS +
PA-d31
C-D
LD
Rigid ER
Cytoplasm
C-F
</details>

![](images/f911a5f1d03b7d0548a679c3cc3ded036cfa2ab156f4328003c875fb08879702.jpg)

<details>
<summary>text_image</summary>

shSCD
1% FBS +
PA-d31
1% FBS +
PA-d31 +
52µM OA
10% FBS +
PA-d31
Rigid ER
Cytoplasm
LD
C-O
C-T
</details>

Figure 3

A  
![](images/10d864b1b2bd20a17acb2ecca48b5b78dcdd1af4035628a51d30ce0902e2063c.jpg)

<details>
<summary>other</summary>

| Oleic acid, µM | shCtrl | shSCD-1 | shSCD-2 | shCtrl | shSCD-1 | shSCD-2 | shCtrl | shSCD-1 | shSCD-2 |
| -------------- | ------ | ------- | ------- | ------ | ------- | ------- | ------ | ------- | ------- |
| XBP1           | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| GAPDH          | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| Oleic acid, µM  | 0      | 13      | 26      | 52     | -       | -       | -      | -       | -       |
</details>

D  
![](images/2f58765c0351cec4eedcea9cd16fb4e60f399bfc45668db27fcd6eb99b090871.jpg)

<details>
<summary>other</summary>

| Protein | shCtrl (μM) | shSCD-1 (μM) |
|---------|-------------|--------------|
| PERK    | 0           | 13           |
| p-eIF2α | 0           | 26           |
| eIF2α   | 0           | 52           |
| ATF4    | 0           | 0            |
| CHOP    | 0           | 13           |
| SCD     | 0           | 26           |
| GAPDH   | 0           | 52           |
</details>

H  
![](images/d80fbf81d4ccb0064702496e7d228072fb1df83f75524ce9a03a40b9a6405b8d.jpg)

<details>
<summary>other</summary>

| Treatment | 0μM | 50μM | Oleic acid, μM |
|-----------|-----|------|----------------|
| DMSO      | +   | -    | -              |
| CAY10566  | -   | +    | -              |
| PERK      | -   | -    | -              |
| p-eIF2α   | -   | -    | -              |
| eIF2α     | -   | -    | -              |
| ATF4      | -   | -    | -              |
| CHOP      | -   | -    | -              |
| GAPDH     | -   | -    | -              |
</details>

B  
![](images/d2daf2de9fb89036f178f3573059a65263cc914120fa38179b3c1a2659299992.jpg)

<details>
<summary>other</summary>

|        | shCtrl | shSCD-1 | shSCD-2 | shCtrl | shSCD-1 | shSCD-2 | shCtrl | shSCD-1 | shSCD-2 |
| ------ | ------ | ------- | ------- | ------ | ------- | ------- | ------ | ------- | ------- |
| XBP1   | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| GAPDH  | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| Palmitic acid (Oleic acid, μM) | 0      | 13      | 26      | 52     | 50μM    | 50μM    | 50μM   | 50μM    | 50μM    |
| Blue line (u)             | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| Blue line (s)             | -      | -       | -       | -      | -       | -       | -      | -       | -       |
The image displays a Western blot with the same axes and labels for 'XBP1' and 'GAPDH'. The color scale indicates '50μM' (blue) and '52' (red).
</details>

E  
![](images/f3b11a24189f3a071daaff7a9dcaa9c76e188d4125f1ddfe8d4577be04e86f88.jpg)

<details>
<summary>text_image</summary>

DMSO + - + - + - + -
CAY10566 - + - + - + - +
XBP1
GAPDH
Oleic acid, µM 0 13 26 52
← u
← s
</details>

F  
![](images/a24c431ae3970935e1a6e82a1183140337626bc4ec2ea34c192f70ad46b9ad54.jpg)

<details>
<summary>other</summary>

| Treatment | Palmitic acid 0μM | Palmitic acid 50μM | Oleic acid 0μM | Oleic acid 13μM | Oleic acid 26μM | Oleic acid 52μM |
|-----------|-------------------|--------------------|----------------|-----------------|-----------------|-----------------|
| DMSO      | +                 | -                  | -              | -               | -               | -               |
| CAY10566  | -                 | +                  | -              | -               | -               | -               |
| XBP1      | -                 | -                  | -              | -               | -               | -               |
| GAPDH     | -                 | -                  | -              | -               | -               | -               |
| Palmitic acid | 0μM             | 50μM               | 0              | 13              | 26              | 52              |
</details>

![](images/bbe124106edbc0a7df023c19334f608db0b073fc4765771b217721e09a49f871.jpg)

<details>
<summary>bar chart</summary>

| Group        | Relative SCD mRNA level |
| ------------ | ------------------------ |
| pLenti-Ctrl  | 1.0                      |
| pLenti-SCD   | 3.5                      |
</details>

J  
![](images/aaab58357de847175836759d2bbbcf7b78c6a9e11fa1f82c082429fdfbd03121.jpg)

C  
![](images/3a682eeff3755eccb3f2a876b785ff173c7a5213f8be5f63439b47596f1a727f.jpg)

<details>
<summary>other</summary>

| Protein | shCtrl | shSCD-1 | shSCD-2 | shCtrl | shSCD-1 | shSCD-2 | shCtrl | shSCD-1 | shSCD-2 | shCtrl | shSCD-1 | shSCD-2 |
|---------|--------|---------|---------|--------|---------|---------|--------|---------|---------|--------|---------|---------|
| PERK    | -      | -       | -       | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| p-eIF2α | -      | -       | -       | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| eIF2α   | -      | -       | -       | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| ATF4    | -      | -       | -       | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| CHOP    | -      | -       | -       | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| SCD     | -      | -       | -       | -      | -       | -       | -      | -       | -       | -      | -       | -       |
| GAPDH   | -      | 0       | 13      | 26     | 52      | 0       | 13     | 26      | 52      | 0      | 13      | 26      |
| Oleic acid, µM (0–52) | 0    | 13     | 26      | 52     | 0      | 13      | 26     | 52      | 0      | 13     | 26      | 52      |
</details>

G  
![](images/ee8522e1afae1cd7af417c90caf95f0889ab072cb14bcf00cde63532ddfec614.jpg)

<details>
<summary>text_image</summary>

DMSO + - + - + - + -
CAY10566 - + - + - + - +
PERK
p-eIF2α
eIF2α
ATF4
CHOP
GAPDH
Oleic
acid, µM 0 13 26 52
</details>

K  
![](images/1872c7ff47ea835e0a1d83b1a8e3df36b1189dc81c5e996ba163b73ecde25585.jpg)

<details>
<summary>text_image</summary>

XBP1
GAPDH
Palmitic
acid
50µM
</details>

L

![](images/12a43b1f6c572b48e81a4809c5823e772ad810bc0702a5b3ca9b497ad51475a7.jpg)

<details>
<summary>bar chart</summary>

| Group       | Spliced XBP1 (%) |
| ----------- | ---------------- |
| pLenti-Ctrl | 16               |
| pLenti-SCD  | 2                |
</details>

Figure 4

A  
![](images/ab16057a0318e814fa8a31931c69880d8538132fd66f5ac57e66d337746315b3.jpg)

<details>
<summary>line chart</summary>

| Time (hour) | shCtrl | shSCD | shCtrl + Oleic Acid | shSCD + Oleic Acid |
|-------------|--------|-------|---------------------|--------------------|
| 0           | 0      | 0     | 0                   | 0                  |
| 24          | ~0.5   | ~0.5  | ~0                  | ~0                 |
| 48          | ~3     | ~2    | ~0                  | ~0                 |
| 72          | ~7     | ~6    | ~0                  | ~0                 |
</details>

B

![](images/fe217c88450d54650ffb65063bcfe879927b460c825091ab274b6592a5441ea4.jpg)

<details>
<summary>line chart</summary>

| Time (hour) | shCtrl + Palmitic Acid | shSCD + Palmitic Acid | shCtrl + Palmitic Acid + Oleic Acid | shSCD + Palmitic Acid + Oleic Acid |
|-------------|------------------------|-----------------------|------------------------------------|------------------------------------|
| 0           | 0                      | 0                     | 0                                  | 0                                  |
| 24          | ~30                    | ~25                   | ~0                                 | ~0                                 |
| 48          | ~35                    | ~30                   | ~0                                 | ~0                                 |
| 72          | ~30                    | ~25                   | ~0                                 | ~0                                 |
</details>

C  
![](images/06efa742cd0ac772b4becf886ee9f8f9d73779076ed145314311c782f8435848.jpg)

<details>
<summary>line chart</summary>

| Time (hour) | DMSO | CAY10566 | DMSO + Oleic Acid | CAY10566 + Oleic Acid |
|-------------|------|----------|-------------------|------------------------|
| 0           | 0.5  | 0.5      | 0.5               | 0.5                    |
| 24          | 0.5  | 0.5      | 0.5               | 0.5                    |
| 48          | 1.5  | 1.5      | 0.5               | 0.5                    |
| 72          | 2.5  | 2.5      | 0.5               | 0.5                    |
</details>

D

![](images/b24fd3acbab2d3feb37d5e66241937f222e997e7bf3818d00e13b173dae9db44.jpg)

<details>
<summary>line chart</summary>

| Time (hour) | DMSO + Palmitic Acid | CAY10566 + Palmitic Acid | DMSO + Palmitic Acid + Oleic Acid | CAY10566 + Palmitic Acid + Oleic Acid |
|-------------|----------------------|--------------------------|----------------------------------|----------------------------------------|
| 0           | 0                    | 0                        | 0                                | 0                                      |
| 24          | ~18                  | ~15                      | ~1                               | ~0.5                                   |
| 48          | ~22                  | ~20                      | ~1.5                             | ~1                                     |
| 72          | ~25                  | ~23                      | ~2                               | ~1.5                                   |
</details>

E  
![](images/97b5bbdd2afb22929064d40f8a491078e8d64108c0adb78b4cb738ce6deba389.jpg)

<details>
<summary>other</summary>

| Condition | shCtrl | shSCD-1 | shCtrl | shSCD-1 | shCtrl | shSCD-1 | shCtrl | shSCD-1 | shSCD-2 |
|-----------|--------|---------|--------|---------|--------|---------|--------|---------|---------|
| Caspase 3 | -      | -       | -      | -       | -      | -       | -      | -       | -       |
| Cleaved Caspase 3 | -    | -       | -      | -       | -      | -       | -      | -       | -       |
| GAPDH     | -      | -       | -      | -       | -      | -       | -      | -       | -       |
| Palmitic acid | 0      | 50μM    | 0      | 13      | 26     | 52      | 0      | 13      | 26      |
| Oleic acid, µM | 0    | 50μM    | 0      | 13      | 26     | 52      | 0      | 13      | 26      |
</details>

F  
![](images/b2dda91b21b73b63fb8d730f0c06716d2771797755daed67ffffc8257652734a.jpg)

<details>
<summary>other</summary>

| Condition | Palmitic acid (0μM) | 0μM | 0μM | 13μM | 26μM | 52μM |
|-----------|---------------------|-----|-----|------|------|------|
| DMSO      | +                   | -   | +   | -    | -    | -    |
| CAY10566  | -                   | +   | -   | +    | -    | -    |
| Caspase 3 | -                   | -   | +   | -    | -    | -    |
| Cleaved Caspase 3 | -                  | -   | +   | -    | -    | -    |
| GAPDH     | -                   | -   | +   | -    | -    | -    |
| Oleic acid, 0μM | 0                 | 0   | 0   | 13   | 26   | 52   |
</details>

G

![](images/abd6e143b7640a00f498b1d62cb662a18aea722a448fd83adbec44a01fc64305.jpg)

<details>
<summary>line chart</summary>

| Time (hour) | pLenti-Ctrl | pLenti-SCD |
|-------------|-------------|------------|
| 0           | 0           | 0          |
| 24          | ~15         | ~10        |
| 48          | ~30         | ~25        |
| 72          | ~30         | ~25        |
</details>

Figure 5

A  
![](images/4a13edde00b20da3f1ca816e6f0228e5c7ce0eeb9c42051664e6cda3f9136855.jpg)

<details>
<summary>scatterplot</summary>

| Group  | Total tumor weight (mg) |
| ------ | ------------------------ |
| shCtrl | 300 - 600                |
| shSCD  | 200 - 500                |
</details>

B

![](images/6478dcdaf48bd696608f6b48abe9f576a4976ae4bec33b1aaaae2439e3354cc9.jpg)

<details>
<summary>scatterplot</summary>

| Group   | Total tumor volume (mm³) |
| ------- | ------------------------ |
| shCtrl  | 400                      |
| shCtrl  | 500                      |
| shCtrl  | 600                      |
| shCtrl  | 700                      |
| shCtrl  | 800                      |
| shCtrl  | 900                      |
| shSCD   | 200                      |
| shSCD   | 300                      |
| shSCD   | 400                      |
| shSCD   | 500                      |
| shSCD   | 600                      |
| shSCD   | 700                      |
| shSCD   | 800                      |
| shSCD   | 900                      |
</details>

c  
![](images/bfbff14396b7042ebeb12889d7a7b21510760df1c42700ecba40d02c00bf01ed.jpg)

<details>
<summary>scatterplot</summary>

| Group   | Total number of metastases |
|---------|----------------------------|
| shCtrl  | 250                        |
| shSCD   | 250                        |
</details>

D

![](images/5a9fccfc0ec16104c6db16edb24a2d7edbccf8a5133fb70f1bffc3cb99d04b3f.jpg)

<details>
<summary>bar chart</summary>

| Group   | Relative SCD mRNA level |
| ------- | ------------------------ |
| shCtrl  | 1.0                      |
| shSCD   | 0.6                      |
</details>

E  
![](images/9ee0bb73d648c51098bff603d21e53d0258cb21f4adccaae95204af8248cccff.jpg)

<details>
<summary>text_image</summary>

shCtrl
ladder
shSCD
XBP1
u
s
GAPDH
</details>

F  
![](images/2c550a64c217b7d85770bdc2891bec1b3b320fdd52e90e3b938875598717cf46.jpg)

<details>
<summary>scatterplot</summary>

| Group   | Spliced XBP1 (%) |
| ------- | ---------------- |
| shCtrl  | 10               |
| shCtrl  | 12               |
| shCtrl  | 14               |
| shCtrl  | 16               |
| shCtrl  | 18               |
| shCtrl  | 20               |
| shCtrl  | 22               |
| shCtrl  | 24               |
| shCtrl  | 26               |
| shCtrl  | 28               |
| shCtrl  | 30               |
| shCtrl  | 32               |
| shCtrl  | 34               |
| shCtrl  | 36               |
| shCtrl  | 38               |
| shCtrl  | 40               |
| shCtrl  | 42               |
| shCtrl  | 44               |
| shCtrl  | 46               |
| shCtrl  | 48               |
| shCtrl  | 50               |
| shSCD   | 10               |
| shSCD   | 12               |
| shSCD   | 14               |
| shSCD   | 16               |
| shSCD   | 18               |
| shSCD   | 20               |
| shSCD   | 22               |
| shSCD   | 24               |
| shSCD   | 26               |
| shSCD   | 28               |
| shSCD   | 30               |
| shSCD   | 32               |
| shSCD   | 34               |
| shSCD   | 36               |
| shSCD   | 38               |
| shSCD   | 40               |
| shSCD   | 42               |
| shSCD   | 44               |
| shSCD   | 46               |
| shSCD   | 48               |
| shSCD   | 50               |
</details>

G  
![](images/9323e5ea5589bbb39aa9f9c114f94ada0a5975fa393183b375e9a633c4654028.jpg)

<details>
<summary>bar chart</summary>

| Diet        | Vehicle | CAY10566 |
|-------------|---------|----------|
| Control Diet| 1.0     | 0.8      |
| PA Diet     | 2.0     | 0.2      |
</details>

H  
![](images/79b780e52402db9deb14f8d8ee43fe7ee7f347370029d38762d0d750182aaaa3.jpg)

<details>
<summary>bar chart</summary>

| Diet       | Vehicle | CAY10566 |
| ---------- | ------- | -------- |
| Control    | 90      | 80       |
| PA Diet    | 100     | 50       |
</details>

I  
![](images/353a740041698137ffa49a399c34c5cd105c1ed378df7a482a668b587678b9e2.jpg)

<details>
<summary>text_image</summary>

DMSO + CAY10566 +
Control Diet
Control Diet
XBP1
GAPDH
← u
← s
</details>

K

![](images/e2f4bf7bcdf1c80e7053102f54a7cdd7c241ea7fba3c534086bcfa37a0921419.jpg)

<details>
<summary>text_image</summary>

DMSO +
Palmitic Acid Diet
CAY10566 +
Palmitic Acid Diet
XBP1
GAPDH
← u
← s
</details>

J  
![](images/9c41a84cc635195cbb272ebc093cdf1c3ee75d37e1e6e3834c32534984cbb096.jpg)

<details>
<summary>scatterplot</summary>

| Group | Spliced XBP1 (%) |
|-------|------------------|
| DMSO + Control Diet | 20 |
| CAY10566 + Control Diet | 7 |
</details>

L

![](images/a753c073deaee6ce8eb36eeffded008f4cacf431bcf71fbe88a086086ede2ab2.jpg)

<details>
<summary>scatterplot</summary>

| Treatment Group       | Spliced XBP1 (%) |
| --------------------- | ----------------- |
| DMSO + PA Diet        | 4                 |
| CAY10566 + PA Diet    | 18                |
</details>

Figure 6