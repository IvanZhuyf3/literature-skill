# SRS-FISH: High-Throughput Platform Linking Microbiome Function to Identity at the Single Cell Level

Xiaowei Gea,+, Fátima C. Pereirab,+, Matthias Mittereggerb,§, David Berryb, Meng Zhanga, Michael Wagnerb,c,\*, and Ji-Xin Chenga,d, \*

aDepartment of Electrical & Computer Engineering, Boston University, Boston, Massachusetts, USA  
bCentre for Microbiology and Environmental Systems Science, Department of Microbiology and Ecosystem Science, University of Vienna, 1090 Vienna, Austria  
c Department of Chemistry and Bioscience, Aalborg University, Aalborg, Denmark  
dDepartment of Biomedical Engineering, Photonics Center, Boston University, Boston, Massachusetts, USA  
+ These authors contributed equally  
§Current address: The Wallenberg Laboratory, Department of Molecular and Clinical Medicine, Sahlgrenska Academy, University of Gothenburg, 41345 Gothenburg, Sweden.

\*Correspondence to: jxcheng@bu.edu, michael.wagner@univie.ac.at

Keywords: chemical imaging, multimodal microscopy, microbiome heterogeneity, mucus degradation, single cell microbiology, stable-isotope probing

## Abstract

One of the biggest challenges in microbiome research in environmental and medical samples is to better understand functional properties of microbial community members at a single cell level. Single cell isotope probing has become a key tool for this purpose, but the currently applied detection methods for measuring isotope incorporation into single cells do not allow high throughput analyses. Here, we report on the development of an imaging-based approach termed stimulated Raman scattering - two-photon fluorescence in situ hybridization (SRS-FISH) for highthroughput structure-function analyses of microbial communities with single cell resolution. SRS-FISH has an imaging speed of 10 to 100 milliseconds per cell, which is two to three orders of magnitude faster than spontaneous Raman-FISH. Using this technique, we delineated metabolic responses of thirty thousand individual cells to various mucosal sugars in the human gut microbiome via incorporation of deuterium from heavy water as an activity marker. Application of SRS-FISH to investigate the utilization of host-derived nutrients by two major human gut microbiome taxa revealed that response to mucosal sugars tends to be dominated by Bacteroidales, with an unexpected finding that Clostridia can outperform Bacteroidales at foraging fucose.

## Main

With the rapid advances in both genotyping and phenotyping of single cells, bridging genotype and phenotype at the single cell level is becoming a new frontier of science1. Methods have been developed to shed light on the genotype-metabolism relationship of individual cells in a complex environment2,3 , which is especially relevant for an in-depth understanding of complex microbial communities in the environment and host-associated microbiomes. For functional analyses of microbial communities, single cell isotope probing is often performed with nanoscale secondary ion mass spectrometry (NanoSIMS)4–7, microautoradiography (MAR)8,9 , or spontaneous Raman microspectroscopy10–12 to visualize and quantify the incorporation of isotopes from labeled substrates. These methods can be combined with fluorescence in situ hybridization (FISH) using rRNA-targeted probes13 , enabling a direct link between function and identity of the organisms. In addition, recently Raman-activated cell sorting has been developed, using either optical tweezers or cell ejection for downstream sequencing of the sorted cells14–16 . While these approaches have expanded the possibilities for functional analyses of microbiome members17 , all of the aforementioned methods suffer from extremely limited throughput. Consequently, only relatively few samples and cells per sample are analyzed via single cell stable isotope probing, hampering a comprehensive understanding of the function of microbes in their natural environment.

To overcome the limited throughput of Raman spectroscopy, coherent Raman scattering microscopy based on coherent anti-Stokes Raman scattering (CARS) or stimulated Raman scattering (SRS), has been developed18,19 . Compared to CARS, the SRS signal is free of the nonresonant background and is linear to molecular concentration, thus permitting quantitative mapping of biomolecules20,21 . Both CARS and SRS microscopy have successfully been applied for studying single cell metabolism in eukaryotes22–25 . In a label-free manner, SRS imaging has led to the discovery of an aberrant cholesteryl ester storage in aggressive cancers26,27 , lipid-rich protrusions in cancer cells under starvation28, fatty acid unsaturation in ovarian cancer stem cells29 and more recently in melanoma30 . CARS and SRS have also been harnessed to explore lipid metabolism in live Caenorhabditis elegans31–34 . Combined with stable isotope probing, SRS microscopy has allowed the tracing of glucose metabolism in eukaryotic cells35,36 and the visualization of metabolic dynamics in living animals24 . Recently, SRS was successfully applied to infer antibiotic resistance patterns of bacterial pure cultures and D2O metabolism24,37 . Yet, SRS microscopy has not yet been adapted for studying functional properties of members of microbial communities through the integration with FISH analyses.

Here, we present an integrative platform that exploits the advantages of SRS for single cell stable isotope probing together with two-photon FISH for the identification of cells in a high-throughput manner. To deal with the challenges in detecting a small number of metabolites inside small cells with diameters around a micron, we have developed a protocol that maximizes the isotope levels in cells and the SRS signal from the Raman band used for isotope detection. SRS is generated by near-infrared pulses while FISH is conventionally implemented using one-photon confocal fluorescence. To address this incompatibility, we developed a procedure for highly sensitive SRS metabolic imaging and two-photon FISH using the same laser source. These efforts collectively led to a high-throughput approach that enables imaging cell identity and metabolism at a speed of 10-100 milliseconds per cell. In comparison, it takes about 20 seconds to record a Raman spectrum from a single cell in a conventional spontaneous Raman-FISH experiment38 .

In this work, we use the gut microbiome as a testbed for our technology. In the human body, microbes have been shown to modulate the host’s health39,40 . Techniques looking into their activities and specific physiologies (i.e. phenotype) as a result of both genotype and the environment provide key information on how microbes function, interact with and shape their host. As a proof-of-principle, we used SRS-FISH to track the incorporation of deuterium (D) from D2O into a mixture of two distinct gut microbiota taxa. We show that SRS-FISH provides fast and sensitive information on the D-content of individual cells while simultaneously unveiling their phylogenetic identity. Subsequently, we applied this technique to complex microbial communities by tracking in situ the metabolic responses of two major human gut microbiome taxa to supplemented host-derived nutrients. Our study revealed that (i) Clostridia spp. could actually outperform Bacteroidales spp. at foraging on the mucosal sugar fucose and showed (ii) a significant inter-individual variability of responses of these major microbiome taxa towards mucosal sugars. Together, our results demonstrate the ability of SRS-FISH to unveil the function of particular microbes in complex communities, with throughputs that are two to three orders of magnitude higher than Raman-FISH and other metabolism-identity bridging tools, therefore providing a valuable multimodal platform to the field of single cell analysis.

## Results

## An SRS-FISH platform to link cell metabolism and cell identity

To retrieve information on the activity of single bacterial cells in culture or complex samples, we employed the ${ \bf D } _ { 2 } { \bf O } _ { - }$ based stable-isotope probing approach10,37 . To this end, live cells present in simple (pure cultures) or complex (gut microbiome) samples were incubated in ${ \bf D } _ { 2 } { \bf O }$ containingmedia, to enable incorporation of D into biomolecules of metabolically-active cells (Fig. 1a). Cells were subsequently fixed and subjected to FISH using fluorescently labeled oligonucleotide probes targeting rRNA, in order to reveal their phylogenetic identity (Fig. 1a, b). Samples prepared in this way were sequentially imaged to retrieve i) fluorescence signals from hybridized samples; and ii) chemical information that enables quantification of cellular D levels for the different taxa targeted by FISH (Fig. 1b). Measurements of D levels were performed using a dual output femtosecond (fs) laser that provided the pump (tunable from 680 nm to 1300 nm) and the Stokes (fixed at 1045 nm) beams. To quantify D incorporation, the pump beam was tuned to 852 nm to target the center of the C-D vibrational peak (2168 cm-1). The limit of SRS detection was determined to be lower than 4.3 mM for unlabeled dimethyl sulfoxide (DMSO) and 8.5 mM for D-labeled DMSO (DMSO-d6) by three standard deviations at zero concentration and the slope of the linear relationship between the SRS signal level and the concentration. (Supplementary Fig. 1). The SRS imaging resolution was determined to be around 300 nm in lateral and $2 \mu \mathrm { m }$ in the axial direction, tested by 200 nm polymethyl methacrylate beads (Supplementary Fig. 1), and is thus suitable for measuring most bacteria. Taking into account the system sensitivity and SRS excitation volume, the minimum number of C-D and C-H bonds that can be detected by fs SRS are around five million and three million (Supplementary Fig. 1, see Methods). As bacterial cells have sizes that are comparable with the laser focus laterally and axially (Supplementary Fig. 1), the different volumes displayed by different bacterial species can influence the SRS intensity level. Therefore, in complex microbial communities, the C-D intensity of a cell alone cannot directly be translated into metabolic activity, especially when comparing between different groups of organisms. In order to normalize for the different volumes of cells in complex samples, the pump beam was tuned to 799 nm to target the center of the C-H bond vibrational peak $( 2 9 4 6 \mathrm { c m ^ { - 1 } } )$ in the C-H stretch region. As the fs pulsed lasers have rather broad bandwidths, fs SRS has a total covering range of $2 0 0 \mathrm { c m } ^ { - 1 }$ around the peak28 . Thus, in this study, the C-D and C-H signature peaks at $2 0 4 0 { - } 2 3 0 0 \ \mathrm { c m ^ { - 1 } }$ and $2 8 0 0 { - } 3 1 0 0 \ \mathrm { c m ^ { - 1 } }$ can be mostly covered by fs SRS. We have observed that some bacterial species seemingly display signals at the silent regions (from 1800 to $2 8 0 0 ~ \mathrm { { c m ^ { - 1 } } ) }$ that can be detected by SRS but not by spontaneous Raman spectroscopy (Supplementary Fig. 2). These signals may originate from processes other than SRS, such as transient absorption, photothermal lensing, and cross phase modulation41,42 . To address this issue, off-resonance images were recorded with the pump beam tuned to 830 nm, targeting $2 4 7 9 \mathrm { c m } ^ { - 1 }$ in the silent region, and subtracted from both C-D and C-H SRS images (Supplementary Fig. 2).

FISH signals have been mostly detected by one photon microscopy, typically using widefield or confocal microscopy43 . Since the near-infrared fs laser beams for SRS imaging fall into the excitation range of TPEF (Fig. 1c, right panel), we developed a two-photon FISH protocol. We focused on the detection of cyanine 3 (Cy3) and cyanine 5 (Cy5), two dyes that possess large twophoton cross sections44 and are commonly used in FISH studies due to their brightness and stability. Two silicon photomultipliers (SiPMs) mounted with 570 nm and 670 nm bandpass filters were used to selectively detect the fluorescence from Cy3 and Cy5, respectively (Fig. 1d). We confirmed that TPEF retrieves accurate fluorescence information with comparable imaging quality and speed as observed under a confocal microscope (discussed further below). Thus, twophoton FISH is a reliable tool for identity mapping, although with slightly lower resolution (\~300 nm) compared to confocal microscopy (usually \~200 nm) (Supplementary Fig. 1).

To identify the targeted taxa and quantify their metabolic activity, the fluorescence signals from cells labeled by the hybridized probes are first acquired using TPEF (Fig. 1b). Then the same cells are imaged with SRS in both the C-D region that measures the extent of D incorporation and the C-H region, which allows normalizing for the influence of the cell volume on C-D intensity (Fig. 1b). Next, off-resonance SRS images were recorded and subtracted from both C-D and C-H images (Supplementary Fig. 3). Subsequently, single cell masks were created in CellProfiler45 using fluorescence images (or C-H images, in the case of pure cultures), and applied to all other channels, to enable precise quantification of D incorporation in FISH-targeted populations (Supplementary Fig. 3; detailed in Methods Section). Quantification of metabolic activity in single bacterial cells was represented by %CDSRS, calculated based on SRS intensities at C-D, C-H, and off-resonance, according to the formula: % $\mathrm { \cdot C D _ { S R S } } { = } ( \mathrm { I _ { C D } } { - } \mathrm { I _ { o f f } } ) / ( \mathrm { I _ { C D } } { + } \mathrm { I _ { C H } } { - } 2 \mathrm { I _ { o f f } } )$ , where I stands for SRS intensity.

## SRS has sufficient sensitivity to track single metabolically-active bacteria tagged by FISH

Though SRS has been used for imaging isotope incorporation in bacterial and mammalian cells24,37 , the impact of FISH on SRS measurements of hybridized bacterial cells has not been studied. For FISH, cells are fixed and subsequently hybridized at $4 6 \mathrm { { ^ \circ C } }$ and washed at $4 8 ^ { \circ } \mathrm { C } ,$ , and the buffers used in these steps contain formamide and detergent. These treatments have been previously shown to decrease both cellular material including lipids of the bacterial cells which can impact the D levels as assessed by spontaneous Raman4,10,38 . To evaluate the impact of FISH on the SRS detection of cellular D levels, SRS signals from hybridized (FISH) and non-hybridized (no FISH) Escherichia coli cells grown in M9 and LB media containing various percentages of ${ \bf D } _ { 2 } { \bf O }$ and therefore displaying a wide range of cellular D contents were determined (Fig. 2). As expected, cells grown in complex LB media display lower levels of D incorporation compared to cells grown in M9 minimal medium containing equivalent percentages of heavy water (Fig. 2). The higher levels of D incorporation observed for growth on M9 (where only a defined carbon source is present) compared to a complex medium has been documented46 . This is likely caused by the higher need for de novo biosynthesis of monomeric biomolecules, such as amino acids, nucleotides, or fatty acids, which are absent in minimal media but readily-available for direct uptake and incorporation from complex media. Despite these differences, for both media, we could observe a significant reduction of $1 9 . 7 2 \% \pm 2 . 7 9 \%$ in the CD levels of hybridized cells (FISH) compared to fixed but non-hybridized cells (no FISH) (Fig. 2b, e, $\mathsf { p } { < } 0 . 0 5$ , Mann-whitey U test). This reduction in %CD is smaller than reported for a similar comparison performed with spontaneous Raman measurements10 and might be explained by the fact that in the fixation and FISH protocols used here the contact time of cells with ethanol was reduced compared to the previously applied protocol (Fig. 2c, f).

Notwithstanding the impact of FISH on calculated $\% { \mathrm { C D } } _ { \mathrm { S R S } } .$ , SRS microscopy enabled efficient detection and discrimination of hybridized cells displaying a wide range of D levels, with mean $\% { \mathrm { C D } } _ { \mathrm { S R S } }$ varying from as low as 2%, and up to 38% (Fig. 2b, e; $\mathrm { p } { < } 0 . 0 5$ , two-sided Mann-Whitney U test). To validate the accuracy of fs SRS for bacterial activity quantification, we compared $\% { \mathrm { C D } } _ { \mathrm { S R S } }$ with %CD measured by spontaneous Raman microspectroscopy $( \% \mathrm { C D _ { R a m a n } } ^ { 1 0 } )$ . Under our conditions, SRS displayed similar sensitivity as spontaneous Raman (Fig. 2c, f).

However, SRS acquisition is two to three orders of magnitude faster than spontaneous Raman (10- 100 ms per cell vs $2 0 \mathrm { \ s \ p e r \ c e l l } ) ^ { 3 }$ 8 . This high speed enables SRS measurements of a much large number of cells, therefore increasing the power of statistical analysis and throughput. In addition, we obtained similar results using an additional bacterial species (Bacteroides thetaiotaomicron; Supplementary Fig. 4), indicating that SRS-FISH is a fast and versatile platform to track metabolic activity in FISH-targeted bacteria.

## SRS is compatible with two-photon FISH to link function and identity

Cellular tagging by fluorescent dyes can lead to background signals detected by SRS, impacting the %CDSRS. This can occur when a fluorophore absorbs one photon from the pump and one photon from the Stokes beam, instead of two photons with the same energy. The simultaneous absorption of photons from two different beams causes a transfer of modulation from the Stokes to the pump, and interference with the SRS signal through a phenomenon known as non-degenerate two-photon absorption (ND-TPA). Although two-photon absorption can be calculated according to the absorption cross-section of recorded dyes, there is scant data of ND-TPA to estimate its influence on SRS. In our setup, we could not detect any interference on SRS attributable to the fluorophores in the sample, as SRS signals recorded from hybridized and non-hybridized E. coli cells grown in the absence of ${ \bf D } _ { 2 } { \bf O }$ were at the same level (Fig. 2). Consistently, we did not observe any significant differences in %CDs of hybridized compared with non-hybridized cells grown in the absence of ${ \bf D } _ { 2 } { \bf O }$ for the two different media tested (Fig. 2b, $\mathbf { e } ; 0 \% \mathrm { D } _ { 2 } \mathrm { O } )$ . Therefore, the lower %CDs obtained after FISH is likely due solely to loss of cellular D during the FISH process, as proposed before10 , but not caused by interference of dyes used for FISH with SRS imaging.

We then evaluated the compatibility of using the 852 nm pump beam and the 1045 nm Stokes beam to excite the $\mathrm { C y 3 }$ and $\mathrm { C y } 5$ dyes coupled to the FISH probes (Fig. 3a). The two SiPMs integrated into the system efficiently detected the emission of single D-labeled E. coli cells hybridized with a Gam42a-Cy5 oligonucleotide probe and of D-labeled B. thetaiotaomicron cells hybridized with a Bac303-Cy3 probe (Fig. 3a, Supplementary Table 1). For particular biological samples, it has been shown that the fs beams used for SRS may generate signals in the visible range, and therefore interfere with TPEF imaging47 . However, only a negligible TPEF signal was detected from D-labeled bacterial cells that were not hybridized (Fig. 3a), and therefore we conclude that SRS does not significantly interfere with TPEF detection.

Having confirmed that SRS and two-photon FISH are compatible, we applied SRS-FISH to an artificial mixture of E. coli and B. thetaiotaomicron cells, each hybridized with taxa-specific oligonucleotide probes labeled with a different dye (Fig. 3b). In a first approach, both E. coli and B. thetaiotaomicron cells were grown in $\mathrm { H } _ { 2 } \mathrm { O } \cdot$ -containing medium. Under these conditions, both cell populations display equally strong C-H signals, but no C-D signals were detected (Fig. 3b, upper panel). When we analyzed a mixture of D-labeled E. coli and unlabeled B. thetaiotaomicron cells, D signal only originated from E. coli cells targeted with the Gam42a-Cy5 probe, while B. thetaiotaomicron targeted by the Bac303-Cy3 probe displayed no C-D signal (Fig. 3b, bottom panel, highlighted circles). Using the signal obtained with TPEF and CellProfiler, we generated masks for either of the FISH-targeted populations (Supplementary Fig. 3), enabling automatic $\% { \mathrm { C D } } _ { \mathrm { S R S } }$ calculation for each FISH-targeted population. While Cy5-tagged E. coli cells display %CDs of around 20, which reflects D incorporation from the ${ \bf D } _ { 2 } { \bf O }$ rich medium, Cy3- tagged B. thetaiotaomicron cells display %CDs close to 0, as expected (Fig. 3c). Collectively, these results demonstrate the feasibility of SRS-FISH to link metabolic active cells to their FISHdetermined identity.

## High-throughput SRS-FISH for identifying mucosal sugar utilizers in the human gut microbiome

To demonstrate the applicability of the SRS-FISH approach to identify active taxa within a complex microbial community, we examined the responses of specific taxa from the human gut microbiota to additions of sugars from the mucus layer48,49 (Fig. 4a). Gut commensals able to forage on mucin can play a pivotal role in resistance to pathogen colonization and in modulating the host immune response48,49 . In previous work, ${ \bf D } _ { 2 } { \bf O }$ combined with spontaneous Ramanactivated cell sorting revealed that members of the families Muribaculaceae, Bacteroidaceae, and Lachnospiraceae are major mucosal sugar foragers in the mouse gut17 . However, given the differences in microbiota composition of mice and humans, as well as differences in predominant types of mucus glycans that can be found in the two hosts50,51 , it remains to be clarified if the same taxa are efficient mucosal sugar utilizers in the human gut, and what are their substrate preferences.

For this purpose, freshly collected human fecal samples were incubated with the five different mucin O-glycan sugars (N-acetylneuraminic acid: NeuAc, N-acetylglucosamine: GlcNAc, Nacetylgalactosamine: GalNAc, fucose, and galactose) in M9 minimal medium (without glucose) containing 50% of ${ \bf D } _ { 2 } { \bf O }$ (Fig. 4a). Under these conditions, we observed that human gut microbes responded to the mucosal sugars amended by incorporating D into their biomass, as well as to glucose (used as a positive control), as revealed using spontaneous Raman (Fig. 4b). Of note, only negligible incorporation of D was detected for cells that had been incubated in the presence of ${ \bf D } _ { 2 } { \bf O }$ but in the absence of any amended sugar, reflecting low metabolic activity driven e.g. by storage products or substrates released from decaying bacteria (Fig. 4b).

Having confirmed that human gut microbes were stimulated by mucosal sugars, we proceeded to identify which taxa respond to specific sugars using the SRS-FISH platform. For this purpose, oligonucleotide probes targeting two major groups of organisms in the human gut were applied: Bac303-Cy3 targeting Bacteroides and Prevotella52 , among other Bacteroidales, and Erec482-Cy5 targeting members of the family Lachnospiraceae (also denominated Clostridium clusters XIVa and XIVb53 ) (Supplementary Table 1). These taxa were chosen because they constitute two of the most dominant and widespread phylogenetic groups of microbes in the human gut54,55 . Additionally, a large percentage of organisms identified as efficient mucosal sugar foragers in the mouse gut are targeted or are closely related to organisms targeted by these probes17 , and a large proportion of Bacteroidales spp. and Clostridia spp. have been shown to carry genes for mucosal sugar catabolism56 . A major challenge encountered while imaging complex gut microbiome samples by SRS-FISH was that the TPEF signal from fluorescently labeled cells bleached much faster than what we previously observed in pure cultures. This might be explained by the relatively lower activity of many members of the gut microbiome, leading to a lower ribosome content and FISH signal when compared with the analyzed bacterial cultures, or by the lower cell wall permeability of particular microbiome members to oligonucleotide probes. To overcome this limitation, we acquired the TPEF signals from microbiome samples in a dried state, without any liquid between the coverslips that carried the sample (Fig. 4c, bottom panel). Stronger and more stable fluorescence signals than in liquid conditions were obtained for both Cy3 and Cy5-labeled cells (Fig. 4d). However, the SRS signal under dried conditions is weaker due to numerical aperture degradation caused by the refractive index mismatch (Fig. 4c, bottom panel, Supplementary Fig. 1). We have therefore optimized our protocols to first acquire the TPEF signal from the sample in a dried form, followed by the addition of water to the sample and SRS imaging of the sample in the liquid environment (Fig. 4c, upper panel). Importantly, the percentage of the fluorescently labeled cells targeted by each of the probes in the samples, determined either by TPEF (under the dry conditions) or by confocal microscopy, was in close agreement (18.7% versus 22.9% for Bac303-Cy3, respectively, and 77.1% versus 81.3% for Erec482-Cy5, respectively; Supplementary Fig. 5). In addition, we did not detect any cell-specific fluorescent signals from samples that had been hybridized with a mixture of Cy3- and Cy5-labeled negative control probes (Supplementary Table 1, Supplementary Fig. 5). These data suggest that the TPEF signal detected from Bac303-Cy3- and Erec482-Cy5-hybridized microbiome samples under dried conditions is accurate.

Using the SRS-FISH protocol optimized for complex microbiome samples, we examined the response of cells targeted by the Bac303-Cy3 and Erec482-Cy5 probes to each mucosal sugar in fecal samples from three different volunteers (Fig. 5, Supplementary Fig. 6). A first observation from our study was that the response to mucosal sugars differs from sample to sample (One-Way Anova test, $\mathrm { p } { = } 7 . 8 6 3 { \times } 1 0 ^ { - 1 9 1 }$ ) (Supplementary Fig. 7), in both qualitative (discussed below), and quantitative terms. Quantitatively, we show that the overall microbiome response to the amended sugars (in terms of the number of active cells and their %CDs) was the highest for volunteer 2, while lowest cellular activity was detected for volunteer 3 (Supplementary Figs. 7, 8). This is not surprising, given that the human microbiome is highly individualized, and also that different fecal samples have been reported to contain different portions of viable cells57,58 . Nevertheless, across the 3 samples the highest average number of active cells (and higher %CDs) was recorded in response to the mucosal sugar GlcNAc, followed by the response to galactose (Supplementary Figs. 7, 8), which is in agreement with the results obtained by spontaneous Raman (Fig. 4b). Overall, for all the samples analyzed we could detect a significant response of both targeted taxa to the mucosal sugars, with the exception of Erec482-targeted taxa to GalNAc in the sample from volunteer 1 (Fig. 5 b-d, Supplementary Table 2). In none of the samples did the no amendment control lead to the stimulation of a significant number of cells (Fig. 5 b-d, Supplementary Table 2). Furthermore, the response of Bac303-targeted taxa was overall higher than the response from Erec482-targeted taxa across all volunteers for all sugars tested, with the exception of fucose, where the inverse was observed for two of the volunteers (Fig. 5; Supplementary Fig. 8). These findings hold even after taking into consideration that the no specific signals in the C-D region were higher in the control group (H2O) for Bac303-targeted cells than for Erec482-targeted cells (Fig. 5).

## Discussion

Microbial communities are fundamental to the functioning of all ecosystems and the health of animals, plants, and humans. These microbiomes are typically investigated by meta-omic analyses that generate valuable annotation-based hypotheses regarding the metabolism of their members but are not suited for testing these hypotheses as gene annotations are often missing, wrong or incomplete59 . Furthermore, many microbes have cell cycles, show considerable phenotypic diversity within isogenic strains, and the activity of microbes is influenced by their spatial arrangement in their habitat. Thus, there is an urgent need for direct functional analyses of microbes within complex samples with single cell resolution.

SRS-FISH fills a gap among the available tools linking function and identity in complex microbial communities due to its exceptionally high-throughput (10-100 millisecond per cell) and a sensitivity comparable to conventional spontaneous Raman-FISH. Overall, SRS-FISH is at least two orders of magnitude faster than state-of-the-art methods: MAR-FISH (2-20 days per sample)60 , Raman-activated microbial cell sorting (>7.22 seconds per cell)14 , FISH-nanoSIMS (>10 seconds per cell)61 , which does not account for the long preconditioning time) and Raman-FISH (\~20 seconds per cell)38 . Furthermore, implementation of FISH by TPEF can be advantageous when imaging thick biological specimens or live organisms, as near-infrared excitation enables deeper penetration into biological samples and causes less damage to cells43 .

The application of SRS-FISH to the gut microbiome demonstrated the suitability of our approach to link identity to function within complex microbial communities, and at the same time revealed interesting new findings related to mucosal sugar foraging in the human gut. SRS-FISH measurements showed that Bacteroidales spp. tend to dominate the response to mucosal sugars over Clostridia spp. in all of the tested individuals (Fig. 5, Supplementary Fig. 8). Indeed, the notion that Bacteroides spp. are major mucus degraders has been demonstrated by several studies17,56,62 . However, our results revealed that organisms from the Clostridium clusters XIVa/XIVb also substantially contribute to mucosal sugar degradation. Further, we show that larger fractions of Clostridia cells can forage on fucose compared to Bacteroidales cells (Fig. 5, Supplementary Fig. 8). Fucose is an important sugar in the colon as it occupies a terminal position on host glycans, thus being at the interface of microbiota–mucus interactions63 . About 20% of human individuals naturally lack a functional copy of the FUT2 gene, and thus lack almost all gut fucosylation64 . Genome-wide association studies have shown that these individuals have increased susceptibility to inflammatory diseases linked to the gut microbiota, such as Crohn's disease65,66 . Additionally, mice that lack the Fut2 enzyme have simpler gut microbiomes that are accompanied by a decrease in unclassified Clostridiales66 . These findings, together with our results, suggest that Clostridia may have been overlooked as fucose degraders in the gut48 . Elucidating which particular Erec482-targeted organisms use fucose may be key to design individualized probiotic interventions aiming to restore the homeostasis in humans lacking FUT2, and therefore in reducing their predisposition to gastrointestinal disease.

Another interesting finding from our study is that the pattern of mucosal sugar foraging differs between the murine and human microbiome: human gut bacteria preferentially metabolize GlcNAc (Fig. 5, Supplementary Fig. 7), while the preferred sugar of the murine microbiome is galactose17 . This could reflect the different overall compositions of human and murine colonic mucins, i.e., while the human colonic mucin carries predominantly GlcNAc-containing core 3- and core 4- based O-glycans, the murine colonic mucin is mostly characterized by galactose-containing core 1- and 2- type structures50,51 . This finding may have important implications when translating results from mouse studies into humans.

There are several opportunities to further improve our SRS-FISH platform. These improvements include SRS-selective scanning of FISH targeted cells, which can even further improve the throughput of SRS-FISH when the taxa of interest appear in very low abundance. Besides, laser equipment with upgraded wavelength tuning speed will also provide the potential to gain higher throughput67 . Other than the throughput, the sensitivity and resolution of SRS-FISH can also be improved by implementing visible SRS68,69 . Of note, the excitation beam in visible SRS can efficiently excite fluorophores from cells targeted by FISH and help avoid the TPEF bleaching issue when imaging cells in a liquid environment. On the other hand, the number of taxa simultaneously tracked by SRS-FISH can be substantially increased using spectral unmixing and custom-designed FISH probes70–72 . Regarding metabolism probing, besides using D2O as an activity marker to induce C-H peak shifts, deuterium-labeled substrates and other stable isotopes, such as $^ { 1 3 } \mathrm { C }$ and $^ { 1 5 } \mathrm { N } ,$ , could be used to track the metabolism of particular compounds and provide information on major catabolic activities and pathways. By targeting peaks between 400-1800 cm-1, SRS could fingerprint major intracellular macromolecules that display shifts due to the incorporation of stable isotopes. This could potentially be achieved by the implementation of hyperspectrum SRS with ultrafast delay-line tuning and machine learning into the SRS-FISH platform16,73 . SRS-FISH would also be a useful tool to probe the distribution of several storage compounds and intrinsic biomolecules in diverse eukaryotic and prokaryotic cells74–77 .

In summary, we have developed an exceptionally high-throughput SRS-FISH platform and successfully applied this new tool to identify efficient mucosal sugar utilizers in the human gut microbiome. It is safe to assume that SRS-FISH can be applied to a broad range of environmental samples (e.g. marine sediments, soil) including those where some autofluorescence background is an issue because SRS is more resilient to sample autofluorescence than spontaneous Raman78,79 . Meanwhile, SRS-FISH is not limited to microbiome samples. With the state of art SRS metabolism imaging and versatile FISH techniques, such as probing abnormal proliferation of chromosomes or targeting mRNA, SRS-FISH will be broadly applicable to eukaryotes.By allowing the scanning of multiple samples in a fast and sensitive manner, SRS-FISH is well-suited to reveal fine-scale temporal, individual, and spatial patterns in a variety of specimens, which can otherwise be missed by existing methods due to their low-throughput.

## Methods

## SRS-FISH platform

A dual output, 80-MHz femtosecond (fs) pulsed laser (InSight X3, Spectra-Physics, USA) provides the pump beam (tunable from 680 nm to 1300 nm) and the Stokes beam (fixed at 1045 nm) for the fs SRS system (Fig. 1d, left panel). Stimulated Raman loss (SRL) provides the SRS intensity by detecting the modulation transfer from the Stokes to the pump beam. The Stokes beam was modulated by an acousto-optic modulator (1205c, Isomet Corporation, USA) at \~2.26 MHz. The two beams were then combined by the dichroic mirror and directed into a lab-built laser scanning microscope. A 60× water objective (UPlanApo 60XW, NA=1.2, Olympus, Japan)

focused the collinear beams on the sample. The power on the sample was \~6 mW for the pump beam and \~32 mW for the Stokes beam. The 2D galvo scanning unit (6215H, Cambridge Technique, USA) was conjugated to the back aperture by a 4f-system and scanned the laser focus to create the SRS image. An oil condenser (NA=1.4, Aplanat Achromat 1.4, Olympus, Japan) alleviated cross-phase modulation induced background in SRS by fully collecting laser beams. The collected beams were filtered by two filters (HA825/150m, Chroma, USA) and only the pump beam was detected by the silicon photodiode (PD, S3994-01, Hamamatsu, Japan). Then the photon-converted electric signal was first separated into alternating current (AC) readout and direct current (DC) readout. Then the AC signal was amplified by the lab-build resonant amplifier circuit centered at \~2.26 MHz. After that, the AC signal was further extracted by a lock-in amplifier (HF2LI, Zurich Instrument, Switzerland). The quantitative chemical maps were created when the energy difference between the pump and the Stokes beam matched the vibrational energy of the targeted chemical bond (C-D centered at $2 1 6 8 ~ \mathrm { c m ^ { - 1 } }$ and C-H centered at $2 9 4 6 \mathrm { c m ^ { - 1 } } )$ (Fig. 1 b). The off-resonance images were recorded when the pump beam was tuned to 830 nm (targeting $2 4 7 9 \mathrm { c m } ^ { - 1 } )$ for subsequent background subtraction in SRS (Supplementary Fig. 2).

To incorporate FISH visualization into the platform, we implemented TPEF in the fs SRS system (Fig. 1a, right panel). Forward detection with a higher collection efficiency of the condenser better preserved the fluorescence signal. With a flip mirror, the light was directed into the fluorescence collection devices. Two SiPMs (C14455-3050GA, Hamamatsu, Japan) modules were implemented to provide better quality fluorescence images compared to photomultiplier tubes (H7422-40, Hamamatsu, Japan) with an external pre-amplifier28 . A 75 mm focal length lens focused the emission light onto the SiPMs with a 605 nm cut-on dichroic mirror (DMLP605, Thorlabs, USA) that separated the emission into two paths. Two filters centered at 570 nm (ET570/20x, Chroma, USA) and 670 nm (ET670/50m, Chroma, USA) were used to detect the fluorescence from different FISH labeled cells with Cy3 or Cy5, which can be efficiently excited by the Stokes beam and the pump beam (for C-D, C-H or off-resonance due to the wide two photon absorption bandwidth) in SRS respectively. A data acquisition card (PCIe-6363, National Instruments, USA) collected the final output to construct the images.

To determine the SRS lateral resolution, 200 nm polymethyl methacrylate beads (MMA200, Degradex phosphorex, USA) were used. By deconvoluting the SRS image with simulated 200 nm size beads, we obtained the point spread function (PSF) of SRS80 , which was the product of pump and Stokes beam and had a FWHM around 242.3 nm (Supplementary Fig. 1). With 210 nm yellow green fluorescence beads (17151-10, Polysciences, USA), the spatial and axial resolution of non-degenerate (ND)-TPEF, pump beam TPEF, and Stokes beam TPEF were measured in the liquid or dry conditions. The ND-TPEF was also the product of pump and Stokes beam, thus it is similar to SRS PSF measurement. Then ND-TPEF images were obtained by subtracting fluorescence images with pump and Stokes both on by pump only TPEF images and Stokes only TPEF images. Due to the broad two photon absorption, we could detect fluorescence using different laser beams, under both liquid and dry imaging conditions, although signal from the 1045 nm TPEF beam in dry conditions was too weak to see the fluorescence beads. The resolution was calculated following the steps of SRS resolution calculation. In the liquid environment, the lateral resolutions of pump only TPEF, Stokes only TPEF, and ND-TPEF by pump and Stokes were 300\~400 nm while all of them degraded 1.5\~2 times to 500 nm\~600 nm when imaging in the dry conditions. The axial resolutions degraded by 3 times from \~1.8 µm in the liquid environment to \~6 µm in the dry conditions (Supplementary Fig. 1). This measurement further demonstrated the degraded sensitivity of SRS when imaging in the dry conditions. Meanwhile, TPEF degradation in the dry conditions did not impede the precision of generating FISH masks (Supplementary Fig. 1， Fig. 4c), which also has a lower requirement of signal level.

To determine the limit of SRS detection, DMSO (≥99.9%, D8418-500ML, Sigma-Alorich) and DMSO-d6 (99.96 atom % D, 156914-1G, Sigma-Alorich) were used as the standard samples to calibrate the system. The slopes between SRS intensity and solution concentration were acquired by fitting concentrations between 0.1 and 4 M, which were 8.123 arb. Unit per M for DMSO-d6 and 14.099 arb. unit per M for DMSO. The standard deviation of pure water measured at C-D and C-H regions were 0.023 and 0.02. The limits of detection were acquired by three standard deviations divided by the slope multiply by six, due to six C-D or C-H bonds in one DMSO-d6 or DMSO molecule. Then the limits of SRS detection of C-D and C-H were 51 mM and 25.8 mM, corresponding to around five million C-D bonds and three million C-H bonds inside the SRS excitation volume.

## Image acquisition

Fixed cells were spotted onto a poly-L-lysine coated coverslip, and covered and sealed by another coverslip with a spacer in between37 . Samples were prepared in this way to reduce cross-phase modulation signal while keeping the sample in the liquid environment that matches the refractive index of the water objective used for imaging. For imaging in the dry conditions, fixed cells were spotted onto a poly-L-lysine coated coverslip, dried, and then covered by another coverslip with spacers at two opposite sides. For each sample, three fields of view (FOV) were scanned by a motorized stage, or manually for SRS-FISH analysis. Three channels of SRS images (C-D, C-H, and off-resonance) and two fluorescence images (Cy3 and Cy5) were collected as a full image set for analyzing two populations targeted with FISH. Although fluorescence images could be acquired simultaneously with SRS-CD by splitting the output beam in the forward direction or collecting epi-fluorescence signal, limitations in the data acquisition card do not provide higher sampling speed for multichannel sampling. So all the images were acquired sequentially. Each FOV was $4 2 . 8 ^ { 2 }$ or $8 5 . 6 ^ { 2 }$ μm2 with 214 nm per step and covered around 300\~400 or 1200\~1600 cells. Depending on the signal intensity level, 10 μs pixel dwell time with 1\~10 frames average was applied for either SRS or fluorescence images. The laser wavelength tuning and stabilizing time for changing between different SRS frames was around 10 s. The throughput of SRS-FISH analysis is around 10-100 ms per cell (\~10-100 cells per second) by taking into account the FOV moving time and laser wavelength switching time. For the microbiome test of 3 individuals’ samples in 8 different conditions, 3 randomly selected field of views were measured, which totally covered around thirty thousand cells.

## Image processing

For bacterial cultures, three SRS images at C-D, C-H, and off-resonance were collected without fluorescence reference as their identities were known beforehand. For applying FISH masks in two targeted populations in the artificial mix or gut microbiome samples, two fluorescence images of Cy3 and Cy5 were recorded along with three SRS images. After all images were acquired, SRS images were first subtracted by the mean background intensity respectively to eliminate the signal from the glass substrate. Then three channels were rescaled according to the DC readout from the PD with resonant amplifier circuit (Supplementary Fig. 3). The AC and DC signals were linear to the pump power inside the power range used in this experiment. Thus, the subtraction between the rescaled C-D, C-H with off-resonance channels can eliminate the other pump-probe background.

Fluorescence images acquired in the dry conditions were aligned to SRS images acquired after water immersion to reduce the mask measurement error from sample drift caused by water immersion. C-H channels or fluorescence channels were used to generate the single cell measuring masks depending on the need and availability of the fluorescence images. The created masks enabled the measurement of single cell average level in off-resonance subtracted C-D and C-H images. The $\% { \mathrm { C D } } _ { \mathrm { S R S } }$ of masked cells were then calculated as described in the Result. All statistical analyses were performed using MATLAB (The MathWorks, USA).

To circumvent the influence of food residues normally present in fecal samples on our results, the regions with overlapping signals in the Cy3 and Cy5 channels were removed from the measurement mask. Wide emission fluorescence is an indication of autofluorescence signal typically originated from food particles81 . Regions of abnormally strong intensity in the SRS image can be also attributed to the photothermal signal or transient absorption of the easily burned food residue. Therefore, intensity outliers $( > 2$ times of the average intensity) recorded for both C-D and C-H channels were also removed from the mask measurement results, such as the very bright spots in the negative control $\mathrm { ( H } _ { 2 } \mathrm { O } \mathrm { + G l c ) }$ C-D channel in Fig.5a.

## Growth and labeling of microbial pure cultures

Escherichia coli K12 (DSM 498) was grown aerobically at $3 7 ^ { \circ } \mathrm { C }$ in Luria-Bertani liquid medium (LB; DSMZ medium 381) or M9 minimal medium containing per L of medium: 7.5 g $\mathrm { N a _ { 2 } H P O _ { 4 } . 2 H _ { 2 } O }$ , 3 g ${ \mathrm { K H } } _ { 2 } { \mathrm { P O } } _ { 4 }$ , 0.5 g NaCl, 0.5 g $\mathrm { N H } _ { 4 } \mathrm { C l }$ , 1 mM $\mathrm { M g } \mathrm { S O } _ { 4 }$ , 0.3 mM CaCl2, 1 μg thiamine hydrochloride (Sigma-Aldrich), 1 μg biotin (Sigma-Aldrich), trace elements, 0.4% (w/v) D-Glucose (Carl Roth GmbH). For D labeling of E. coli cultures, 50 μl of a stationary-phase culture were used to inoculate 5mL of LB or M9 medium containing different percentages (vol/vol) of ${ \bf D } _ { 2 } { \bf O }$ (99.9% atom % (at%) D; Sigma Aldrich). Cells were grown until the late exponential phase (3 h in LB medium or 8-10 h in M9 medium), harvested by centrifugation and fixed in 4% formaldehyde in phosphate-buffered saline (PBS) for 2 h at $4 ^ { \circ } \mathbf { C } .$ . Cells were subsequently washed once with PBS and stored at $4 ^ { \circ } \mathbf { C }$ until further use. Bacteroides thetaiotaomicron (DSM 2079) cells were grown anaerobically (85% $\mathrm { N } _ { 2 } , 1 0 \% \mathrm { C O } _ { 2 } , 5 \% \mathrm { H } _ { 2 } )$ in BHI broth (DSMZ medium 215c) or in Bacteroides minimal medium82 containing different percentages (vol/vol) of ${ \bf D } _ { 2 } { \bf O }$ (99.9% atom % (at%) D; Sigma Aldrich). After 6 hours of growth at $3 7 ^ { \circ } \mathrm { C } ,$ cells were harvested by centrifugation, resuspended in PBS, and fixed by adding formaldehyde in PBS as described above. All cells were stored in a PBS solution at $4 ~ ^ { \circ } \mathbf { C }$ until further use.

## Gut microbiome incubations

Human fecal samples were collected from three healthy adult individuals (one male and two females between the ages of 25 to 38) who had not received antibiotics in the prior 3 months. Sampling of human fecal samples was approved by the University of Vienna Ethics Committee (reference #00161). Study participants provided informed consent and self-sampled using an adhesive paper-based feces catcher (FecesCatcher, Tag Hemi, Zeijen, NL) and a sterile polypropylene tube with the attached sampling spoon (Sarstedt, Nümbrecht, DE). Samples were transferred into an anaerobic tent (Coy Laboratory Products, USA) within 30 min after sampling. Samples were suspended in M9 medium (prepared with $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ and without glucose) to achieve a concentration of $0 . 1 \ \mathrm { g . m l ^ { - 1 } }$ , and further diluted 20 times in this medium. The homogenate was left to settle for 10 minutes, and the supernatant was then distributed into glass vials. An equal volume of M9 (without glucose) prepared with either ${ \bf D } _ { 2 } { \bf O }$ (99.9% atom % (at%) D; Sigma Aldrich) or $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ (for the negative control) was added to each tube, and each vial was finally supplemented with different concentrations of mucosal sugar monosaccharides (N-acetylneuraminic acid: 2 $\mathrm { { m g . m l ^ { - 1 } } }$ ; N-acetylglucosamine: 5 $\mathrm { { m g . m l ^ { - 1 } } }$ ; fucose: 2.5 $\mathrm { m g . m l ^ { - 1 } } ;$ ; galactose: 5 $\mathrm { m g . m l ^ { - 1 } } ;$ ; Nacetylgalactosamine: $2 . 5 ~ \mathrm { m g . m l ^ { - 1 } } )$ , D-glucose $( 5 ~ \mathrm { m g . m l ^ { - 1 } } )$ or nothing (no-amendment control) (all amendment chemicals were from Sigma–Aldrich, except D(+)-galactose which was purchased from Carl Roth GmbH). These concentrations were selected based on reported concentrations of the different monosaccharides in purified hog gastric mucin and mucin gels, as described $\mathrm { i n } ^ { 1 7 }$ . After incubation for 6 h at $3 7 ^ { \circ } \mathbf { C }$ under anaerobic conditions (5% H2, 10% $\mathrm { C O } _ { 2 } .$ , 85% N2), samples were pelleted, washed with $1 \times \mathrm { P B S }$ to remove ${ \bf D } _ { 2 } { \bf O }$ and then fixed in 3% formaldehyde for 2 h at $4 ^ { \circ } \mathbf { C } .$ . Samples were finally washed two times with 1 ml of PBS and stored in PBS at $4 ^ { \circ } \mathbf { C }$ until further use.

## Fluorescence in situ hybridization

Fixed cells (100 μl) were pelleted at 14000 g for 10 min, resuspended in 100 μl 96% analytical grade ethanol and incubated for 1 min at room temperature for dehydration. Subsequently, the samples were centrifuged at $1 4 0 0 0 g$ for 5 min, the ethanol was removed, and the cell pellet was air-dried. Cells were hybridized in solution $( 1 0 0 ~ \mu \mathrm { l } )$ for 3 h at $4 6 \mathrm { { } ^ { \circ } C }$ . The hybridization buffer consisted of 900 mM NaCl, 20 mM TRIS HCl, 1 mM EDTA, 0.01% SDS and contained 100 ng of the respective fluorescently labeled oligonucleotide as well as the required formamide concentration to obtain stringent conditions (Supplementary Table S1). After hybridization, samples were immediately transferred into a centrifuge with a rotor pre-heated at $4 6 \mathrm { { ^ \circ C } }$ and centrifuged at 14000 g for 15 min at maximum allowed temperature $( 4 0 ^ { \circ } \mathrm { C } )$ , to minimize unspecific probe binding. Samples were washed in a buffer of appropriate stringency83 for 15 min at $4 8 ^ { \circ } \mathrm { C } ,$ cells were centrifuged for 15 min at $1 4 0 0 0 \ \mathrm { g }$ and finally resuspended in 20 μl of PBS. Cells $( 5 \mu \mathrm { l } )$ were spotted on Poly-L-lysine coated cover glasses No. 1.5H (thickness of $1 7 0 ~ { \mu \mathrm { m } } \pm 5 ~ { \mu \mathrm { m } }$ , Paul Marienfeld EN) and allowed to dry overnight at $4 ^ { \circ } \mathrm { C } ,$ protected from light. Excess of salt was removed by dipping the coverslips $2 \times$ in ice-cold Milli-Q water and allowed to dry at room temperature protected from light.

## Confocal fluorescence microscopy

Samples were spotted onto microscope slides (Paul Marienfeld EN) with Poly-L-lysine coating and visualized using an Olympus scanning confocal microscope (FV3000) with a 60x oil objective (PLAPON60XO, 1.42 NA, 0.15 mm WD, Olympus) and two high-sensitivity photomultiplier tubes (PMTs). $\mathrm { C y 3 }$ double-labeled probe Bac303 was excited by a 514 nm solid state diode laser and its emission was collected between 530 nm and 630 nm. Cy5 double-labeled probe Erec482 was excited by a 640 nm solid state diode laser and its emission was collected between 650 nm and 750 nm. Transmission images were also collected for validating the focus and the distribution of the whole gut microbiome sample. The ideal spatial resolution limit is around 221 nm\~275 nm. The scanning step size of the confocal image was set to 103.58 nm, which was smaller than half of the diffraction limit of both beams and ensured sampling spatial frequency higher than the Nyquist frequency for both excitation wavelengths. Each acquired field of view is $2 1 2 ^ { 2 } \mu \mathrm { m } ^ { 2 }$ .

## Spontaneous Raman microspectroscopy

Fixed cells were spotted on aluminum-coated slides (Al136; EMF Corporation). Excess of salt was removed by dipping the slide twice into ice-cold Milli-Q water. Individual cells were observed under a 100×/0.75 NA microscope air objective Single microbial cell spectra were acquired using a LabRAM HR800 confocal Raman microscope (Horiba Jobin-Yvon) equipped with a 532-nm neodymium-yttrium aluminum garnet (Nd:YAG) laser and 300 grooves/mm diffraction grating. Spectra were acquired in the range of $4 0 0 { - } 3 2 0 0 \mathrm { c m } ^ { - 1 }$ for 30 s with 2.18 mW laser power. Spectra were then aligned according to the phenylalanine peak region and normalized by dividing the spectral intensity at each wavelength by the total spectral intensity. For quantification of the degree of D incorporation into the cells, %CD was calculated using the integration of the intensity of bands assigned to $\mathrm { C - D ~ } ( 2 0 4 0 { - } 2 , 3 0 0 ~ \mathrm { c m } ^ { - 1 } )$ and $\mathrm { C - H } ~ ( 2 , 8 0 0 { - } 3 , 1 0 0 ~ \mathrm { c m } ^ { - 1 } ) ^ { 1 0 }$ . For Raman‐FISH analyses, cells displaying signals originating from hybridized oligonucleotide probes were identified using epifluorescence imaging on the Raman confocal microscope equipped with a 100‐ W Xenon lamp, a standard Cy5 filter block and an F‐View camera (Soft Imaging Systems). Raman spectra of targeted cells were obtained by switching image acquisition to the inbuilt Raman CCD detector.

## Data and codes availability

The data and codes that supports the findings of this study are available from the corresponding author upon request.

## Acknowledgements

Research reported in this publication was funded by National Institutes of Health under award Number R35GM136223 and R01AI141439 to J.-X.C. and supported by the Boston University Micro and Nano Imaging Facility and the Office of the Director, National Institutes of Health of the National Institutes of Health under award Number S10OD024993. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institute of Health. Funding for the presented research was also provided by the Austrian Science Fund (FWF) via the Wittgensteinaward to M.W. (Z383-B) and via a Young Independent Research

Group grant to F.C.P. (ZK-57). We thank Arno Schintlmeister for valuable comments on the manuscript.

## Author contributions

X.G., F.C.P., M.W. and J.-X.C. conceived and designed the study. X.G., F.C.P. and M.M. performed the experiments and analyzed the data. X.G., F.C.P., M.W. and J.-X.C. wrote the manuscript. D.B. provided support and input to the microbiome experiments. M. Z. provided input on D labeling and cell fixation protocols. All authors have given approval to the final version of the paper.

## Competing Interests

The authors declare no competing interests.

## References

1. Camp, J. G., Platt, R. & Treutlein, B. Mapping human cell phenotypes to genotypes with single-cell genomics. Science 365, 1401–1405 (2019).  
2. Zenobi, R. Single-Cell Metabolomics: Analytical and Biological Perspectives. Science 342, (2013).  
3. Evers, T. M. J. et al. Deciphering Metabolic Heterogeneity by Single-Cell Analysis. Anal. Chem. 91, 13314–13323 (2019).  
4. Musat, N., Foster, R., Vagner, T., Adam, B. & Kuypers, M. M. M. Detecting metabolic activities in single cells, with emphasis on nanoSIMS. FEMS Microbiol. Rev. 36, 486–511 (2012).  
5. Berry, D. et al. Host-compound foraging by intestinal microbiota revealed by single-cell stable isotope probing. Proc. Natl. Acad. Sci. U. S. A. 110, 4720–5 (2013).  
6. Scheller, S., Yu, H., Chadwick, G. L., McGlynn, S. E. & Orphan, V. J. Artificial electron acceptors decouple archaeal methane oxidation from sulfate reduction. Science 351, 703–707 (2016).  
7. Reese, A. T. et al. Microbial nitrogen limitation in the mammalian large intestine. Nat. Microbiol. 3, 1441–1450 (2018).  
8. Lee, N. et al. Combination of fluorescent in situ hybridization and microautoradiography-a new tool for structure-function analyses in microbial ecology. Appl. Environ. Microbiol. 65, 1289–1297 (1999).  
9. Nierychlo, M. et al. The morphology and metabolic potential of the Chloroflexi in full-scale activated sludge wastewater treatment plants. FEMS Microbiol. Ecol. 95, (2019).  
10. Berry, D. et al. Tracking heavy water (D2O) incorporation for identifying and sorting active microbial cells. Proc. Natl. Acad. Sci. 112, E194–E203 (2015).  
11. Taubert, M. et al. Tracking active groundwater microbes with D2 O labelling to understand their ecosystem function. Environ. Microbiol. 20, 369–384 (2018).  
12. Huang, W. E. et al. Resolving Genetic Functions within Microbial Populations: In Situ Analyses Using rRNA and mRNA Stable Isotope Probing Coupled with Single-Cell Raman Fluorescence In Situ Hybridization. Appl. Environ. Microbiol. 75, 234–241 (2009).  
13. Olsen, G. J., Lane, D. J., Giovannoni, S. J., Pace, N. R. & Stahl, D. A. Microbial Ecology and Evolution: A Ribosomal RNA Approach. Annu. Rev. Microbiol. 40, 337–365 (1986).  
14. Lee, K. S. et al. An automated Raman-based platform for the sorting of live cells by functional properties. Nat. Microbiol. 4, 1035–1048 (2019).  
15. Fang, T., Shang, W., Liu, C., Liu, Y. & Ye, A. Single-Cell Multimodal Analytical Approach by Integrating Raman Optical Tweezers and RNA Sequencing. Anal. Chem. 92, 10433–10441 (2020).  
16. Wang, Y. et al. Raman Activated Cell Ejection for Isolation of Single Cells. Anal. Chem. 85, 10697–10701 (2013).  
17. Pereira, F. C. et al. Rational design of a microbial consortium of mucosal sugar utilizers reduces Clostridiodes difficile colonization. Nat. Commun. 11, 5104 (2020).  
18. Zumbusch, A., Holtom, G. R. & Xie, X. S. Three-Dimensional Vibrational Imaging by Coherent Anti-Stokes Raman Scattering. Phys. Rev. Lett. 82, 4142–4145 (1999).  
19. Ploetz, E., Laimgruber, S., Berner, S., Zinth, W. & Gilch, P. Femtosecond stimulated Raman microscopy. Appl. Phys. B 87, 389–393 (2007).  
20. Fu, D. et al. Quantitative Chemical Imaging with Multiplex Stimulated Raman Scattering Microscopy. J. Am. Chem. Soc. 134, 3623–3626 (2012).  
21. Ji, M. et al. Detection of human brain tumor infiltration with quantitative stimulated Raman scattering microscopy. Sci. Transl. Med. 7, 309ra163-309ra163 (2015).  
22. Yue, S. & Cheng, J.-X. Deciphering single cell metabolism by coherent Raman scattering microscopy. Curr. Opin. Chem. Biol. 33, 46–57 (2016).  
23. Zumbusch, A., Langbein, W. & Borri, P. Nonlinear vibrational microscopy applied to lipid biology. Prog. Lipid Res. 52, 615–632 (2013).  
24. Shi, L. et al. Optical imaging of metabolic dynamics in animals. Nat. Commun. 9, 2995 (2018).  
25. Wakisaka, Y. et al. Probing the metabolic heterogeneity of live Euglena gracilis with stimulated Raman scattering microscopy. Nat. Microbiol. 1, 1–4 (2016).  
26. Yue, S. et al. Cholesteryl Ester Accumulation Induced by PTEN Loss and PI3K/AKT Activation Underlies Human Prostate Cancer Aggressiveness. Cell Metab. 19, 393–406 (2014).  
27. Li, J. et al. Abrogating cholesterol esterification suppresses growth and metastasis of pancreatic cancer. Oncogene 35, 6378–6388 (2016).  
28. Huang, K.-C., Li, J., Zhang, C., Tan, Y. & Cheng, J.-X. Multiplex Stimulated Raman Scattering Imaging Cytometry Reveals Lipid-Rich Protrusions in Cancer Cells under Stress Condition. iScience 23, 100953 (2020).  
29. Li, J. et al. Lipid Desaturation Is a Metabolic Marker and Therapeutic Target of Ovarian Cancer Stem Cells. Cell Stem Cell 20, 303-314.e5 (2017).  
30. Du, J. et al. Raman-guided subcellular pharmaco-metabolomics for metastatic melanoma cells. Nat. Commun. 11, 4830 (2020).  
31. Hellerer, T. et al. Monitoring of lipid storage in Caenorhabditis elegans using coherent anti-Stokes Raman scattering (CARS) microscopy. Proc. Natl. Acad. Sci. 104, 14658–14663 (2007).  
32. Wang, M. C., Min, W., Freudiger, C. W., Ruvkun, G. & Xie, X. S. RNAi screening for fat regulatory genes with SRS microscopy. Nat. Methods 8, 135–138 (2011).  
33. Chen, W.-W. et al. Spectroscopic coherent Raman imaging of Caenorhabditis elegans reveals lipid particle diversity. Nat. Chem. Biol. 16, 1087–1095 (2020).  
34. Mutlu, A. S., Gao, S. M., Zhang, H. & Wang, M. C. Olfactory specificity regulates lipid metabolism through neuroendocrine signaling in Caenorhabditis elegans. Nat. Commun. 11, 1450 (2020).  
35. Li, J. & Cheng, J.-X. Direct Visualization of De novo Lipogenesis in Single Living Cells. Sci. Rep. 4, 6807 (2014).  
36. Zhang, L. et al. Spectral tracing of deuterium for imaging glucose metabolism. Nat. Biomed. Eng. 3, 402–413 (2019).  
37. Zhang, M. et al. Rapid Determination of Antimicrobial Susceptibility by Stimulated Raman Scattering Imaging of D 2 O Metabolic Incorporation in a Single Bacterium. Adv. Sci. 7, 2001452 (2020).  
38. Fernando, E. Y. et al. Resolving the individual contribution of key microbial populations to enhanced biological phosphorus removal with Raman–FISH. ISME J. 13, 1933–1946 (2019).  
39. Sender, R., Fuchs, S. & Milo, R. Revised Estimates for the Number of Human and Bacteria Cells in the Body. PLOS Biol. 14, e1002533 (2016).  
40. Gilbert, J. et al. Current understanding of the human microbiome. Nat. Med. 24, 392–400 (2018).  
41. Zhang, D., Slipchenko, M. N., Leaird, D. E., Weiner, A. M. & Cheng, J.-X. Spectrally modulated stimulated Raman scattering imaging with an angle-to-wavelength pulse shaper. Opt. Express 21, 13864–13874 (2013).  
42. Berto, P., Andresen, E. R. & Rigneault, H. Background-Free Stimulated Raman Spectroscopy and Microscopy. Phys. Rev. Lett. 112, 053905 (2014).  
43. Levsky, J. M. & Singer, R. H. Fluorescence in situ hybridization: past, present and future. J. Cell Sci. 116, 2833–2838 (2003).  
44. Albota, M. A., Xu, C. & Webb, W. W. Two-photon fluorescence excitation cross sections of biomolecular probes from 690 to 960 nm. Appl. Opt. 37, 7352–7356 (1998).  
45. McQuin, C. et al. CellProfiler 3.0: Next-generation image processing for biology. PLOS Biol. 16, e2005970 (2018).  
46. Matanfack, G. A. et al. Influence of Carbon Sources on Quantification of Deuterium Incorporation in Heterotrophic Bacteria: A Raman-Stable Isotope Labeling Approach. Anal. Chem. 92, 11429–11437 (2020).  
47. Cheng, J.-X. & Xie, X. S. Coherent Raman Scattering Microscopy. (CRC Press, 2016).  
48. Tailford, L. E., Crost, E. H., Kavanaugh, D. & Juge, N. Mucin glycan foraging in the human gut microbiome. Front. Genet. 6, (2015).  
49. Pereira, F. C. & Berry, D. Microbial nutrient niches in the gut. Environ. Microbiol. 19, 1366– 1378 (2017).  
50. Larsson, J. M. H., Karlsson, H., Sjövall, H. & Hansson, G. C. A complex, but uniform O glycosylation of the human MUC2 mucin from colonic biopsies analyzed by nanoLC/MSn. Glycobiology 19, 756–766 (2009).  
51. Thomsson, K. A. et al. Detailed O-glycomics of the Muc2 mucin from colon of wild-type, core 1- and core 3-transferase-deficient mice highlights differences compared with human MUC2. Glycobiology 22, 1128–1139 (2012).  
52. Manz, W., Amann, R., Ludwig, W., Vancanneyt, M. & Schleifer, K. H. Application of a suite of 16S rRNA-specific oligonucleotide probes designed to investigate bacteria of the phylum cytophaga-flavobacter-bacteroides in the natural environment. Microbiol. Read. Engl. 142 ( Pt 5), 1097–1106 (1996).  
53. Franks, A. H. et al. Variations of Bacterial Populations in Human Feces Measured by Fluorescent In Situ Hybridization with Group-Specific 16S rRNA-Targeted Oligonucleotide Probes. Appl. Environ. Microbiol. 64, 3336–3345 (1998).  
54. Rigottier-Gois, L., Rochet, V., Garrec, N., Suau, A. & Doré, J. Enumeration of Bacteroides Species in Human Faeces by Fluorescent in situ Hybridisation Combined with Flow Cytometry Using 16S rRNA Probes. Syst. Appl. Microbiol. 26, 110–118 (2003).  
55. Mueller, S. et al. Differences in Fecal Microbiota in Different European Study Populations in Relation to Age, Gender, and Country: a Cross-Sectional Study. Appl. Environ. Microbiol. 72, 1027–1033 (2006).  
56. Ravcheev, D. A. & Thiele, I. Comparative Genomic Analysis of the Human Gut Microbiome Reveals a Broad Distribution of Metabolic Pathways for the Degradation of Host-Synthetized Mucin Glycans and Utilization of Mucin-Derived Monosaccharides. Front. Genet. 8, (2017).  
57. Zmora, N., Zeevi, D., Korem, T., Segal, E. & Elinav, E. Taking it Personally: Personalized Utilization of the Human Microbiome in Health and Disease. Cell Host Microbe 19, 12–20 (2016).  
58. Maurice, C. F., Haiser, H. J. & Turnbaugh, P. J. Xenobiotics shape the physiology and gene expression of the active human gut microbiome. Cell 152, 39–50 (2013).  
59. Lobb, B., Tremblay, B. J.-M., Moreno-Hagelsieb, G. & Doxey, A. C. Y. 2020. An assessment of genome annotation coverage across the bacterial tree of life. Microb. Genomics 6, e000341.  
60. Nierychlo, M., Nielsen, J. L. & Nielsen, P. H. Studies of the Ecophysiology of Single Cells in Microbial Communities by (Quantitative) Microautoradiography and Fluorescence In Situ Hybridization (MAR-FISH). in Hydrocarbon and Lipid Microbiology Protocols: Ultrastructure and Imaging (eds. McGenity, T. J., Timmis, K. N. & Nogales, B.) 115–130 (Springer, 2016).  
61. Meyer, N. R., Fortney, J. L. & Dekas, A. E. NanoSIMS sample preparation decreases isotope enrichment: magnitude, variability and implications for single-cell rates of microbial activity. Environ. Microbiol. 23, 81–98 (2021).  
62. Desai, M. S. et al. A Dietary Fiber-Deprived Gut Microbiota Degrades the Colonic Mucus Barrier and Enhances Pathogen Susceptibility. Cell 167, 1339-1353.e21 (2016).  
63. Pickard, J. M. & Chervonsky, A. V. Intestinal fucose as a mediator of host-microbe symbiosis. J. Immunol. Baltim. Md 1950 194, 5588–5593 (2015).  
64. Kelly, R. J., Rouquier, S., Giorgi, D., Lennon, G. G. & Lowe, J. B. Sequence and Expression of a Candidate for the Human Secretor Blood Group α(1,2)Fucosyltransferase Gene (FUT2): HOMOZYGOSITY FOR AN ENZYME-INACTIVATING NONSENSE MUTATION COMMONLY CORRELATES WITH THE NON-SECRETOR PHENOTYPE (∗). J. Biol. Chem. 270, 4640–4649 (1995).  
65. Rausch, P. et al. Colonic mucosa-associated microbiota is influenced by an interaction of Crohn disease and FUT2 (Secretor) genotype. Proc. Natl. Acad. Sci. 108, 19030–19035 (2011).  
66. Kashyap, P. C. et al. Genetically dictated change in host mucus carbohydrate landscape exerts a diet-dependent effect on the gut microbiota. Proc. Natl. Acad. Sci. U. S. A. 110, 17059– 17064 (2013).  
67. Brinkmann, M. et al. Portable all-fiber dual-output widely tunable light source for coherent Raman imaging. Biomed. Opt. Express 10, 4437–4449 (2019).  
68. Bi, Y. et al. Near-resonance enhanced label-free stimulated Raman scattering microscopy with spatial resolution near 130 nm. Light Sci. Appl. 7, 81 (2018).  
69. Zhuge, M. et al. Ultrasensitive Vibrational Imaging of Retinoids by Visible Preresonance Stimulated Raman Scattering Microscopy. Adv. Sci. 2003136.  
70. Valm, A. M., Welch, J. L. M. & Borisy, G. G. CLASI-FISH: Principles of Combinatorial Labeling and Spectral Imaging. Syst. Appl. Microbiol. 35, 496–502 (2012).  
71. Lukumbuzya, M., Schmid, M., Pjevac, P. & Daims, H. A Multicolor Fluorescence in situ Hybridization Approach Using an Extended Set of Fluorophores to Visualize Microorganisms. Front. Microbiol. 10, (2019).  
72. Shi, H. et al. Highly multiplexed spatial mapping of microbial communities. Nature 588, 676– 681 (2020).  
73. Lin, H. et al. Fingerprint Spectroscopic SRS Imaging of Single Living Cells and Whole Brain by Ultrafast Tuning and Spatial-Spectral Learning. ArXiv200302224 Phys. (2020).  
74. Gruber-Vodicka, H. R. et al. Paracatenula, an ancient symbiosis between thiotrophic Alphaproteobacteria and catenulid flatworms. Proc. Natl. Acad. Sci. 108, 12078–12083 (2011).  
75. Majed, N., Chernenko, T., Diem, M. & Gu, A. Z. Identification of Functionally Relevant Populations in Enhanced Biological Phosphorus Removal Processes Based On Intracellular Polymers Profiles and Insights into the Metabolic Diversity and Heterogeneity. Environ. Sci. Technol. 46, 5010–5017 (2012).  
76. Wei, L. et al. Imaging Complex Protein Metabolism in Live Organisms by Stimulated Raman Scattering Microscopy with Isotope Labeling. ACS Chem. Biol. 10, 901–908 (2015).  
77. Lee, H. J. & Cheng, J.-X. Imaging chemistry inside living cells by stimulated Raman scattering microscopy. Methods 128, 119–128 (2017).  
78. Freudiger, C. W. et al. Label-Free Biomedical Imaging with High Sensitivity by Stimulated Raman Scattering Microscopy. Science 322, 1857–1861 (2008).  
79. Min, W., Freudiger, C. W., Lu, S. & Xie, X. S. Coherent Nonlinear Optical Imaging: Beyond Fluorescence Microscopy. Annu. Rev. Phys. Chem. 62, 507–530 (2011).  
80. Mertz, J. Introduction to Optical Microscopy. (Higher Education from Cambridge University Press, 2019).  
81. Welch, J. L. M., Hasegawa, Y., McNulty, N. P., Gordon, J. I. & Borisy, G. G. Spatial organization of a model 15-member human gut microbiota established in gnotobiotic mice. Proc. Natl. Acad. Sci. 114, E9105–E9114 (2017).  
82. Bacic, M. K. & Smith, C. J. Laboratory Maintenance and Cultivation of Bacteroides Species. Curr. Protoc. Microbiol. 9, 13C.1.1-13C.1.21 (2008).  
83. Daims, H. The Family Nitrospiraceae. in The Prokaryotes: Other Major Lineages of Bacteria and The Archaea (eds. Rosenberg, E., DeLong, E. F., Lory, S., Stackebrandt, E. & Thompson, F.) 733–749 (Springer, 2014).

## Figure legends

Figure 1 Stimulated Raman scattering (SRS)- fluorescence in situ hybridization (FISH) platform to bridge phylogenetic identity (genotype) and metabolic activity (phenotype) in microbes. a, Standard sample preparation process for SRS-FISH experiments. Pure bacterial cultures or complex microbiome samples are incubated in $\mathrm { D } _ { 2 } \mathrm { O - c o n t a i n i n g }$ media to enable D incorporation into metabolically active cells. Samples are subsequently fixed and submitted to FISH. After FISH, samples are deposited in a glass cover slide and analyzed by SRS-FISH either directly while in the liquid environment, or after drying. b, Schematic representation of SRS-FISH imaging results. Samples are hybridized with fluorescently labeled oligonucleotide probes (double-labeled with either cyan or red fluorophores) targeting taxa of interest present in the sample. Fluorescence signal originating from hybridized samples (cyan and red) is then overlaid with SRS C-D signal (yellow) and SRS C-H signal (green) to reveal the metabolic activity levels of each identified bacterial cell. Organisms not targeted by the probes will not display fluorescence (grey). c, SRS and two photon excited fluorescence (TPEF) mechanism. ES: excited state. VS: virtual state. GS: ground state. $\omega _ { P } \colon$ pump beam laser frequency. $\omega _ { S } \mathrm { : }$ Stokes beam laser frequency. $\omega _ { S R L }$ : stimulated Raman loss frequency. ??: vibrational energy. $\omega _ { T }$ : TPEF excitation beam frequency. $\omega _ { E }$ : fluorescence emission frequency. d, SRS-FISH system. M1-M4: mirrors. AOM: acousto-optic modulator. DM1-2: dichroic mirrors. SU: scanning unit. L1-4: lenses. OBJ: objective. COND: condenser. FM: flip mirror. PD: photo diode. SiPM1-2: silicon photomultiplier.

Figure 2 Sensitivity of the SRS-FISH platform to detect ${ \bf D } _ { 2 } { \bf O }$ metabolic incorporation into bacterial cells hybridized with oligonucleotide probes. SRS imaging of C-D (yellow) and C-H (green) intensities of single E. coli cells grown in LB (a) or M9 (d) media containing increasing percentages of ${ \bf D } _ { 2 } { \bf O } .$ . For each condition, both hybridized (FISH, top panels) and non-hybridized (no FISH, bottom panels) cells were analyzed. Scale bar: 10 µm. Image contrast: (a) C-D channel, min 0 max 5 (arb. unit); C-H channel, min 0 max 30 (arb. unit). (d) C-D channel, min 0 max 1.5 (arb. unit); C-H channel, min 0 max 30 (arb. unit). Pixel dwell time: 100 µs. For details regarding data processing please refer to Supplementary Figure 3. b, c, Single cell C-D level distribution in E. coli cultures grown under the conditions described in a, measured with either SRS (b) or with spontaneous Raman microspectroscopy (c). NS: non-significant, $\mathrm { p } { > } 0 . 0 5 ;$ \*: $1 0 ^ { - 5 } { < } \mathrm { p } { < } 0 . 0 5 ;$ \*\*: 10- $^ 7 < \mathsf { p } { < } 1 0 ^ { - 5 }$ ; \*\*\*: $\mathrm { p } { < } 1 0 ^ { - 7 }$ (two-sided Mann-whitney U test). e, f, Single cell C-D level distribution in E. coli cultures grown under the conditions described in b, measured with either SRS (e) or with Spontaneous Raman microspectroscopy (f). In b, c, e, f, each dot represents a cell. Boxes represent median, first and third quartile. Whiskers extend to the highest and lowest values that are within one and a half times the interquartile range. The white circle in the middle of the box represents the mean value of the data.

Figure 3 Genetic and chemical information can be acquired simultaneously by the SRS-FISH platform without interference. a, TPEF visualization of D-labeled B. thetaiotaomicron and E. coli cells hybridized (FISH) or not (no FISH) with Bac303-Cy3 (pseudo-coloured cyan) and Gam42a-$\mathrm { C y } 5$ (pseudo-coloured red) oligonucleotide probes. No background in TPEF channels is detected for D- labeled, non-hybridized cells. Imaging under the dry conditions. Scale bar, 15 µm. Image contrast: Cy3: min 0.02, max 0.07 (arb. unit); Cy5: min 0.02, max 0.13 (arb. unit). b, Simultaneous SRS and TPEF imaging of artificial mixtures of unlabeled B. thetaiotaomicron and E. coli cells (top panel) or of D-labeled E. coli $( 5 0 \% \ \mathrm { { D } } _ { 2 } \mathrm { { O } ) }$ and unlabeled B. thetaiotaomicron $( 0 \% \ \mathrm { { D } _ { 2 } \mathrm { { O } ) } }$ cells (bottom panel). Bac: B. thetaiotaomicron. Ecoli: E. coli. SRS C-D (yellow) and C-H (green) intensities after off-resonance subtraction are shown for both mixtures. In both cases, cells were hybridized with the taxa-specific probes Bac303-Cy3 (cyan) and Gam42a-Cy5 (red), enabling cells from the two populations to be distinguished by TPEF imaging. Depicted circles highlight the presence of C-H, but absence of C-D signal in B. thetaiotaomicron cells identified by TPEF signal from the Bac303-Cy3 probe (in cyan). Scale bar, 15 µm. Image contrast: C-D channel, min 0 max 5 (arb. unit); C-H channel, min 0 max 30 (arb. unit). c, Single-cell C-D level distribution in the two different populations of the artificial mixtures presented in b, whose identity is revealed by TPEF imaging.

Figure 4 SRS-FISH to resolve the utilization of mucosal sugars by different microbiome taxa. a, Representation of the experimental setup. Freshly collected fecal samples were diluted in M9 medium and supplemented with different mucus $O \mathrm { - }$ glycan sugars in the presence of ${ \bf D } _ { 2 } { \bf O }$ . Negative- and positive-control incubations were performed in parallel by incubating the samples with Glucose (Glc) in the presence of $_ \mathrm { H _ { 2 } O }$ (labeled Glc (-)) or ${ \bf D } _ { 2 } { \bf O }$ (labeled Glc). Mucus O-glycan sugars include NeuAc: N-Acetylneuraminic acid, GlcNAc: N-Acetylglucosamine, Fuc: Fucose, Gal: Galactose, GalNAc: N-Acetylgalactosamine. A no amendment (NA) control with D2O but no sugar added was also included. Cells from all microcosms were processed as depicted (described in detail in the Methods section), and subsequently probed for D incorporation using spontaneous Raman, or D incorporation into taxa of interest using SRS-FISH. b, Single cell C-D level distribution of randomly selected microbiome bacteria supplemented with the different mucosal sugars and controls as described in a, measured by spontaneous Raman microspectroscopy. Each dot represents a cell. Boxes represent median, first and third quartile. The white circle in the middle of the box represents the mean value of the data. Whiskers extend to the highest and lowest values that are within one and a half times the interquartile range. c, SRS imaging of C-D (yellow), C-H (green) and off-resonance (purple) frequencies of hybridized gut microbiome cells when imaged in the liquid environment (top panel) or dry (bottom panel). TPEF signal from cells hybridized with the oligonucleotide probes Bac303-Cy3 and Erec-Cy5 is shown in cyan and red, respectively. Scale bar, 15 µm. For details regarding data processing please refer to Supplementary Figure 3. d, Intensity distribution histogram of fluorescence signals originating from cells hybridized with Cy3- (i) and Cy5- (ii) labeled probes, when imaged in solution or dried on a cover slide with confocal microscopy.

Figure 5 SRS-FISH uncovers the ability of major gut microbiome taxa to forage on different mucosal sugars. a, Microbiome samples of volunteer 1 were incubated with different mucosal sugars and hybridized with the oligonucleotide probes Bac303-Cy3 (cyan) and Erec482-Cy5 (red), respectively. Representative images obtained by TPEF (top row) and SRS (C-D middle row, C-H bottom row) are shown. Negative control: $\mathrm { H } _ { 2 } \mathrm { O } \mathrm { - }$ +Glucose. Positive control: ${ \bf D } _ { 2 } { \bf O } _ { - }$ +Glucose. NA: no amendment. Scale bar, $1 0 \mu \mathrm { m }$ . For details regarding data processing please refer to Supplementary Figure 3. b, c, d, Single-cell C-D level distribution in the two different targeted taxa presented in a, measured by SRS for samples from 3 different volunteers. Box plots represent the median, first and third quartile with the extended lines represent the minimum and maximum value within 1.5 interquartile range from the first and third quartile. The white circle in the middle of the box represents the mean value of the data. The deeper grey blue line (mean +3SD of Bac303-Cy3 labeled cells in negative control) is the baseline over which Bac (Bac303-Cy3) cells are considered labeled. The lighter grey blue line (mean +3SD of Erec482-Cy5 labeled cells in negative control) is the baseline over which Erec (Erec482-Cy5) cells are considered labeled. The two-sided Mann-Whitney U-test was applied to compare the statistical significance between Bac and Erec bacteria for each amendment. NS: non-significant, p>0.05; \*: $1 0 ^ { - 5 } { < } \mathfrak { p } { < } 0 . 0 5$ ; \*\*: $1 0 ^ { - 7 } { < } \mathfrak { p } { < } 1 0 ^ { - 5 } ;$ ; \*\*\*: $\scriptstyle \mathrm { p < } 1 0 ^ { - 7 }$ (two-sided Mann-Whitney U test).

a  
![](images/440786dda0a6744f4aebb93055ec40c65822cea828ecd0e7d961421d6baf0546.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Untreated microbiome"] --> B["Isotope labeling"]
  B --> C["FISH"]
  C --> D["Drop onto PPL coated coversli"]
  D --> E["Ready for SRS-FISH"]
```
</details>

b  
![](images/953d7c84e688deb8a41b12e034a063e3998f205f7a2d5e1ac2c0f379f6bea949.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["TPEF FISH"] --> B["SRS C-D"]
  A --> C["SRS C-H"]
  B --> D["M4"]
  B --> E["OBJ"]
  B --> F["COND"]
  C --> G["L3"]
```
</details>

![](images/08db9ca2a26515b19cadccab58b385fd4ad7b9e73526bc47251baad0b9c5bc52.jpg)

<details>
<summary>chemical</summary>

Energy level diagram showing transitions between states ES, GS, and ωSRL with labeled transitions ωp, ωs, ωT, ωE
</details>

![](images/8a7d558569379e74d89895566e27151c96df4c6e5392e4f0b38f08cd02bd0799.jpg)

<details>
<summary>text_image</summary>

d
ωSRL = ωp
M4
L2
SUB
L1
M3
OBJ
Sample
SiPM1
SiPM2
M2
DM1
AOM
PD
L3
FM
L4
DM2
M1
Delay line
Pump
Stokes
</details>

Figure 1 Stimulated Raman scattering (SRS)- fluorescence in situ hybridization (FISH) platform to bridge phylogenetic identity (genotype) and metabolic activity (phenotype) in microbes. a, Standard sample preparation process for SRS-FISH experiments. Pure bacterial cultures or complex microbiome samples are incubated in $\mathsf { D } _ { 2 } \mathsf { O } \mathsf { - c o n t a i n i n g }$ media to enable D incorporation into metabolically active cells. Samples are subsequently fixed and submitted to FISH. After FISH, samples are deposited in a glass cover slide and analyzed by SRS-FISH either directly while in liquid environment, or after drying. b, Schematic representation of SRS-FISH imaging results. Samples are hybridized with fluorescently-labeled oligonucleotide probes (double-labeled with either cyan or red fluorophores) targeting taxa of interest present in the sample. Fluorescence signal originating from hybridized samples (cyan and red) is then overlaid with SRS C-D signal (yellow) and SRS C-H signal (green) to reveal the metabolic activity levels of each identified bacterial cell. Organisms not targeted by the probes will not display fluorescence (grey). c, SRS and two photon excited fluorescence (TPEF) mechanism. ES: excited state. VS: virtual state. GS: ground state. $\omega _ { P } \mathrm { . }$ pump beam laser frequency. $\omega _ { S }$ : Stokes beam laser frequency. $\omega _ { S R L }$ : stimulated Raman loss frequency. Ω: vibrational energy. $\omega _ { T } .$ : TPEF excitation beam frequency. $\omega _ { E } \mathrm { . }$ : fluorescence emission frequency. d, SRS-FISH system. M1-M4: mirrors. AOM: acousto-optic modulator. DM1-2: dichroic mirrors. SU: scanning unit. L1-4: lenses. OBJ: objective. COND: condenser. FM: flip mirror. PD: photo diode. SiPM1-2: silicon photomultiplier.

![](images/d062e3dee43892690637614cc7249b5833f7b54d58c15febeee3a69086deaa2f.jpg)

<details>
<summary>text_image</summary>

a
0% D₂O	30% D₂O	50% D₂O	70% D₂O
FISH
noFISH
C-D 2168 cm⁻¹
C-H 2946 cm⁻¹
</details>

![](images/af3acda05061ed48447149e544a27dcd619b75696219e932f1abe064cfae2743.jpg)

<details>
<summary>text_image</summary>

d
0% D₂O	30% D₂O	50% D₂O	70% D₂O
C-D 2168 cm⁻¹
C-H 2946 cm⁻¹
</details>

![](images/b3b19e2a28c761caef687aaa73fabfcbf97f290abb92db0a56a86ec7bd198f67.jpg)

<details>
<summary>box plot</summary>

| Group       | %CD50% SRS |
|-------------|------------|
| 0%_FISH     | ~2.5       |
| 0%_noFISH   | ~0.5       |
| 30%_FISH    | ~3.5       |
| 30%_noFISH  | ~4.5       |
| 50%_FISH    | ~4.5       |
| 50%_noFISH  | ~6.5       |
| 70%_FISH    | ~7.0       |
| 70%_noFISH  | ~8.5       |
</details>

![](images/5f2c1495606352b8728bf2e0a6eee0a4aa6668a3a673f36c0830286e98f89e67.jpg)

<details>
<summary>scatterplot</summary>

| Group       | Median | IQR Lower | IQR Upper | Whisker Min | Whisker Max |
|-------------|--------|-----------|-----------|-------------|-------------|
| 0%_FISH     | ~1     | ~0.5      | ~2        | ~0.2        | ~3          |
| 0%_noFISH   | ~1     | ~0.5      | ~2        | ~0.2        | ~3          |
| 30%_FISH    | ~10    | ~8        | ~12       | ~6          | ~14         |
| 30%_noFISH  | ~12    | ~10       | ~14       | ~8          | ~16         |
| 50%_FISH    | ~15    | ~12       | ~18       | ~10         | ~20         |
| 50%_noFISH  | ~18    | ~15       | ~22       | ~12         | ~25         |
| 70%_FISH    | ~25    | ~20       | ~30       | ~15         | ~35         |
| 70%_noFISH  | ~35    | ~28       | ~45       | ~25         | ~50         |
</details>

![](images/319732b79da0f4ce4870649e45d13f0f933391bb271ef8775bae497cf544ecdf.jpg)

<details>
<summary>box plot</summary>

| Group       | %CD_Raman |
| ----------- | --------- |
| 0%_FISH     | ~1.0      |
| 0%_noFISH   | ~1.2      |
| 30%_FISH    | ~2.8      |
| 30%_noFISH  | ~3.0      |
| 50%_FISH    | ~5.0      |
| 50%_noFISH  | ~6.0      |
| 70%_FISH    | ~7.5      |
| 70%_noFISH  | ~8.0      |
</details>

![](images/1b753474b0dd96c0ca8190e5e9676d7b2f3a8d2d5ef53b0a642f8a18f6b14d1c.jpg)

<details>
<summary>scatterplot</summary>

| Group       | %CD Raman |
| ----------- | --------- |
| 0%_FISH     | ~1        |
| 0%_noFISH   | ~1        |
| 30%_FISH    | ~14       |
| 30%_noFISH  | ~15       |
| 50%_FISH    | ~25       |
| 50%_nonFISH | ~28       |
| 70%_FISH    | ~38       |
| 70%_noFISH  | ~35       |
</details>

Figure 2 Sensitivity of the SRS-FISH platform to detect $\mathsf { D } _ { 2 } \mathsf { O }$ metabolic incorporation into bacterial cells hybridized with oligonucleotide probes. SRS imaging of C-D (yellow) and C-H (green) intensities of single E. coli cells grown in LB (a) or M9 (d) media containing increasing percentages of ${ \sf D } _ { 2 } { \sf O }$ . For each condition, both hybridized (FISH, top panels) and non-hybridized (no FISH, bottom panels) cells were analyzed. Scale bar: 10 µm. Image contrast: (a) C-D channel, min 0 max 1.5 (arb. unit); C-H channel, min 0 max 30 (arb. unit). (d) C-D channel, min 0 max 5 (arb. unit); C-H channel, min 0 max 30 (arb. unit). Pixel dwell time: 100 µs. For details regarding data processing please refer to Supplementary Figure 3. b, c, Single cell C-D level distribution in E. coli cultures grown under the conditions described in a, measured with either SRS (b) or with spontaneous Raman microspectroscopy (c). NS: non-significant, p>0.05; \*: $1 0 ^ { - 5 } { < p < } 0 . 0 5 ;$ \*\*: $1 0 ^ { - 7 } { < p < } 1 0 ^ { - 5 }$ ; \*\*\*: $\mathsf { p } { < } 1 0 ^ { - 7 }$ (two-sided Mann-Whitney U test). e, f, Single cell C-D level distribution in $E .$ coli cultures grown under the conditions described in b, measured with either SRS (e) or with Spontaneous Raman microspectroscopy (f). In b, c, e, f, each dot represents a cell. Boxes represent median, first and third quartile. Whiskers extend to the highest and lowest values that are within one and a half times the interquartile range. The white circle in the middle of the box represents the mean value of the data.

![](images/58c04f5823d61150e73b2602d7c8467cf5d50acae94c0318b80cbc6f05e46f71.jpg)

<details>
<summary>text_image</summary>

TPEF Bac303-Cy3
TPEF Gam42a-Cy5
noFISH
FISH
noFISH
FISH
Transmission
</details>

h  
![](images/8317e8a2b9491388d647af4512cff252c86a65dceb2f6043a2262a9f2c37f053.jpg)

<details>
<summary>text_image</summary>

C-D 2168 cm⁻¹
C-H 2946 cm⁻¹
TPEF Bac303-Cy3
Transmission
Ecoli: 0%
Bac: 0%
Ecoli: 50%
Bac: 0%
</details>

c

![](images/874eab17fa52cafcdfedc1739626db3ed200b571764c2a05070984ea6830882b.jpg)

<details>
<summary>box plot</summary>

| Group | %CD_SRS |
|-------|---------|
| 0% D2O Bac | ~1.5 |
| 0% D2O Ecoli | ~2.5 |
| 50% D2O Ecoli | ~21.0 |
</details>

Figure 3 Genetic and chemical information can be acquired simultaneously by the SRS-FISH platform without interference. a, TPEF visualization of D-labeled B. thetaiotaomicron and E. coli cells hybridized (FISH) or not (no FISH) with Bac303-Cy3 (pseudo-coloured cyan) and Gam42a-Cy5 (pseudo-coloured red) oligonucleotide probes. No background in TPEF channels is detected for Dlabeled, non-hybridized cells. Imaging under the dry conditions. Scale bar, 15 µm. Image contrast: Cy3: min 0.02, max 0.07 (arb. unit); Cy5: min 0.02, max 0.13 (arb. unit). b, Simultaneous SRS and TPEF imaging of artificial mixtures of unlabeled B. thetaiotaomicron and E. coli cells (top panel) or of D-labeled E. coli $( 5 0 \% \mathsf { D } _ { 2 } \mathsf { O } )$ and unlabeled B. thetaiotaomicron $( 0 \% \mathsf { D } _ { 2 } 0 )$ cells (bottom panel). Bac: B. thetaiotaomicron. Ecoli: E. coli. SRS C-D (yellow) and C-H (green) intensities after off-resonance subtraction are shown for both mixtures. In both cases, cells were hybridized with the taxa-specific probes Bac303-Cy3 (cyan) and Gam42a-Cy5 (red), enabling cells from the two populations to be distinguished by TPEF imaging. Depicted circles highlight the presence of C-H, but absence of C-D signal in B. thetaiotaomicron cells identified by TPEF signal from the Bac303-Cy3 probe (in cyan). Scale bar, 15 µm. Image contrast: C-D channel, min 0 max 5 (arb. unit); C-H channel, min 0 max 30 (arb. unit). c, Single-cell C-D level distribution in the two different populations of the artificial mixtures presented in b, whose identity is revealed by TPEF imaging.

a  
![](images/e5757eb8e77495e62890dc8e8c433b27b4938a5bff25b14ce3caef5aed8d7f89.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Fecal sample"] --> B["Incubation"]
  B --> C["Fixation FISH"]
  C --> D["Drop onto coverslip"]
  D --> E["SRS-FISH"]
    
    subgraph Inputs
        A1["Glc (-)"]
        A2["D2O Glc"]
        A3["D2O NeuAc"]
        A4["D2O GlcNAc"]
        A5["D2O Fuc"]
        A6["D2O Gal"]
        A7["D2O GalNAc"]
        A8["D2O NA"]
    end
    
    subgraph Products
        B1["NeuAc"]
        B2["GlcNAc"]
        B3["Fuc"]
        B4["Gal"]
        B5["GalNAc"]
        B6["Mucosal sugars"]
        B7["Mucin (MUC2)"]
    end
    
  A1 --> B1
  A2 --> B2
  A3 --> B3
  A4 --> B4
  A5 --> B5
  A6 --> B6
  A7 --> B7
  A8 --> B8
  B1 --> C
  B2 --> C
  B3 --> C
  B4 --> C
  B5 --> C
  B6 --> C
```
</details>

![](images/90920feb2e2fa4155a9de98c175a9cc9325df4c303d9c411708cd568e7264837.jpg)

<details>
<summary>text_image</summary>

C
C-D 2168 cm⁻¹
OFF 2479 cm⁻¹
C-H 2946 cm⁻¹
Transmission
Liquid
Dry
TPEF Erec482-Cy5
TPEF Bac303-Cy3
</details>

b  
![](images/67ddce24cd4f3ed7c51a017eda540ceaf32dd7a41083135129fafa996bba29cc.jpg)

<details>
<summary>box plot</summary>

| Cell Type | %CD_Raman |
| --------- | --------- |
| Glc (-)   | ~0        |
| Glc       | ~15       |
| NeuAc     | ~4        |
| GlcNAc    | ~21       |
| Fuc       | ~13       |
| Gal       | ~16       |
| GalNAc    | ~8        |
| NA        | ~1        |
</details>

d

![](images/02f86fbfd34f9360598ba518586c14fb0879df29776c643956d6fdcbb051b47c.jpg)

<details>
<summary>bar chart</summary>

(i)
| Fluorescence intensity (A.U.) | Dry | Solution |
|---|---|---|
| 0.0 | 0 | 18 |
| 0.05 | 0 | 25 |
| 0.1 | 0 | 5 |
| 0.25 | 2 | 0 |
| 0.3 | 4 | 0 |
| 0.35 | 2 | 0 |
| 0.4 | 8 | 0 |
| 0.45 | 12 | 0 |
| 0.5 | 9 | 0 |
| 0.55 | 24 | 0 |
| 0.6 | 20 | 0 |
| 0.65 | 22 | 0 |
| 0.7 | 17 | 0 |
| 0.75 | 11 | 0 |
| 0.8 | 7 | 0 |
Bacteria count
Fluorescence intensity (A.U.)
</details>

![](images/31cbc1b375e72661a4752479dc534068d00878d17f723988b9e480140fbd7a2a.jpg)

<details>
<summary>bar chart</summary>

(ii)
| Fluorescence intensity (A.U.) | Dry | Solution |
|---|---|---|
| 0.1 | 0 | 5 |
| 0.15 | 0 | 115 |
| 0.2 | 47 | 152 |
| 0.25 | 50 | 108 |
| 0.3 | 64 | 22 |
| 0.35 | 100 | 5 |
| 0.4 | 125 | 1 |
| 0.45 | 160 | 0 |
| 0.5 | 148 | 0 |
| 0.55 | 120 | 0 |
| 0.6 | 84 | 0 |
| 0.65 | 79 | 0 |
| 0.7 | 50 | 0 |
| 0.75 | 38 | 0 |
| 0.8 | 16 | 0 |
</details>

Figure 4 SRS-FISH to resolve the utilization of mucosal sugars by different microbiome taxa. a, Representation of the experimental setup. Freshly collected human fecal samples were diluted in M9 medium and supplemented with different mucus O-glycan sugars in the presence of $\mathsf { D } _ { 2 } \mathsf { O }$ . Negativeand positive-control incubations were performed in parallel by incubating the samples with Glucose (Glc) in the presence of ${ \sf H } _ { 2 } { \sf O }$ (labeled Glc (-)) or $\mathsf { D } _ { 2 } \mathsf { O }$ (labeled Glc). Mucus O-glycan sugars include NeuAc: N-Acetylneuraminic acid, GlcNAc: N-Acetylglucosamine, Fuc: Fucose, Gal: Galactose, GalNAc: N-Acetylgalactosamine. A no amendment (NA) control with $\mathsf { D } _ { 2 } \mathsf { O }$ but no sugar added was also included. Cells from all microcosms were processed as depicted (described in detail in the Methods section), and subsequently probed for D incorporation using spontaneous Raman, or D incorporation into taxa of interest using SRS-FISH. b, Single cell C-D level distribution of randomly selected microbiome bacteria supplemented with the different mucosal sugars and controls as described in a, measured by spontaneous Raman microspectroscopy. Each dot represents a cell. Boxes represent median, first and third quartile. The white circle in the middle of the box represents the mean value of the data. Whiskers extend to the highest and lowest values that are within one and a half times the interquartile range. c, SRS imaging of C-D (yellow), C-H (green) and off-resonance (purple) frequencies of hybridized gut microbiome cells when imaged in liquid environment (top panel) or dry (bottom panel). TPEF signal from cells hybridized with the oligonucleotide probes Bac303-Cy3 and Erec-Cy5 is shown in cyan and red, respectively. Scale bar, 15 µm. For details regarding data processing please refer to Supplementary Figure 3. d, Intensity distribution histogram of fluorescence signals originating from cells hybridized with Cy3- (i) and Cy5- (ii) labeled probes, when imaged in solution or dried on a cover slide with confocal microscopy.

a  
![](images/ff35464369e9b83e0e7cdad04e656109a0d4b30b3ade537be76ba92fecfe3d6f.jpg)

<details>
<summary>text_image</summary>

was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-NF 4.0 International license
I₂O+Glc D₂O+Glc D₂O+NeuA D₂O+GlcNA C-D-GalNAc D₂O (NA)
Bacc03-Cy3 Erec482-Oy5
C-D 2168 cm⁻¹
C-H 2946 cm⁻¹
</details>

b

![](images/dc7f95345b96eec99b210f70dc83e087b8db507d86b51d095c8d33c8989cff0d.jpg)

<details>
<summary>box plot chart</summary>

| Group        | %CD_SRS |
| ------------ | ------- |
| Glc (-).Bac  | ~2      |
| Glc (-).Erec  | ~1      |
| Glc.Bac      | ~15     |
| Glc.Erec     | ~9      |
| NeuAc.Bac    | ~4      |
| NeuAc.Erec   | ~2      |
| GlcNAc.Bac   | ~12     |
| GlcNAc.Erec  | ~6      |
| Fuc.Bac      | ~7      |
| Fuc.Erec     | ~12     |
| Gal.Bac      | ~9      |
| Gal.Erec     | ~8      |
| GalNAc.Bac  | ~7      |
| GalNAc.Erec  | ~2      |
| NA.Bac       | ~2      |
| NA.Erec      | ~1      |
</details>

c  
![](images/429035dec87469d691b194cdffa4208c5ed3db208548156e0c8b0b5ee24d3f87.jpg)

<details>
<summary>box plot chart</summary>

| Group        | %CD5RS |
| ------------ | ------ |
| Glc(-)-Bac   | ~1     |
| Glc(-)-Erec  | ~1     |
| Glc.Bac      | ~18    |
| Glc.Erec     | ~13    |
| NeuAc.Bac    | ~4     |
| NeuAc.Erec   | ~2     |
| GlcNAc.Bac   | ~20    |
| GlcNAc.Erec  | ~10    |
| Fuc.Bac      | ~11    |
| Fuc.Erec     | ~10    |
| Gal.Bac      | ~19    |
| Gal.Erec     | ~14    |
| GalNAc.Bac   | ~7     |
| GalNAc.Erec  | ~1     |
| NA.Bac       | ~2     |
| NA.Erec      | ~1     |
</details>

d  
![](images/446bdf497f5d2ea1804640e47f41932342a3c5fb2cf064b84dbf06267ac4c7c7.jpg)

<details>
<summary>box plot chart</summary>

| Group        | %CD_SRS |
| ------------ | ------- |
| Glc (-).Bac   | ~2      |
| Glc (-).Erec  | ~1      |
| Glc. Bac     | ~13     |
| Glc. Bac     | ~27     |
| Glc. Bac     | ~9      |
| Glc. Bac     | ~6      |
| NeuAc. Bac   | ~3      |
| NeuAc. Bac   | ~4      |
| NeuAc. Erec  | ~2      |
| GlcNAc. Bac  | ~8      |
| GlcNAc. Bac  | ~17     |
| GlcNAc. Bac  | ~26     |
| GlcNAc. Bac  | ~30     |
| Fuc. Bac     | ~3      |
| Fuc. Bac     | ~4      |
| Fuc. Bac     | ~5      |
| Gal. Bac     | ~10     |
| Gal. Bac     | ~20     |
| Gal. Bac     | ~24     |
| Gal. Bac     | ~32     |
| GalNAc. Bac  | ~8      |
| GalNAc. Bac  | ~18     |
| GalNAc. Bac  | ~24     |
| GalNAc. Bac  | ~30     |
| NA. Bac      | ~1      |
| NA. Bac      | ~2      |
| NA. Bac      | ~1      |
| NA. Bac      | ~2      |
</details>

Figure 5 SRS-FISH uncovers the ability of major gut microbiome taxa to forage on different mucosal sugars. a, Microbiome samples of volunteer 1 were incubated with different mucosal sugars and hybridized with the oligonucleotide probes Bac303-Cy3 (cyan) and Erec482-Cy5 (red), respectively. Representative images obtained by TPEF (top row) and SRS (C-D middle row, C-H bottom row) are shown. Negative control: $H _ { 2 } O + G | u \cos e$ . Positive control: $_ { \mathsf { D } _ { 2 } \mathsf { O } + \mathsf { G l u c o s e } }$ . NA: no amendment. Scale bar, 10 µm For details regarding data processing please refer to Supplementary Figure 3. b, c, d, Single-cell C-D level distribution in the two different targeted taxa presented in a, measured by SRS for samples from 3 different volunteers. Box plots represent the median, first and third quartile with the extended lines represent the minimum and maximum value within 1.5 interquartile range from the first and third quartile. The white circle in the middle of the box represents the mean value of the data. The deeper grey blue line (mean +3SD of Bac303-Cy3 labeled cells in negative control) is the baseline over which Bac (Bac303-Cy3) cells are considered labeled. The lighter grey blue line (mean +3SD of Erec482-Cy5 labeled cells in negative control) is the baseline over which Erec $( \mathsf { E r e c 4 8 2 – C y 5 } )$ cells are considered labeled. The two-sided Mann-Whitney U-test was applied to compare the statistical significance between Bac and Erec bacteria for each amendment. NS: non-significant, $\mathsf { p } { > } 0 . 0 5 ; \kappa : 1 0 ^ { - 5 } { < } \mathsf { p } { < } 0 . 0 5 ; \kappa { \star } : 1 0 ^ { - 7 } { < } \mathsf { p } { < } 1 0 ^ { - 5 }$ ; \*\*\*: $\mathsf { p } { < } 1 0 ^ { - 7 }$ (two-sided Mann-Whitney U test).