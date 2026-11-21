# Card review: desousa-2021-commsbio

- **Card:** papers/desousa-2021-commsbio.md
- **Source:** papers-pdf/de-sousa-et-al-2021.pdf (9 pages, article pages printed 1 to 8 match the PDF pages, page 9 is references and back matter)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 56 |
| Supported | 43 |
| Imprecise | 12 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 6 |
| Important omissions | 4 |
| Metadata issues | 4 |

The card gets all the headline numbers right (400 genotypes, 3,200 plots, 41 genotypes, 1,165 farms, 4,660 plots, every Kendall tau in Table 1, reliability 0.83 to 0.91, about 20% yield gain). The most important fix is the region: the card says Amhara and Tigray only, but 399 of the 1,165 farms (34%) were in Oromia (p. 6). Other fixes: on-farm grain yield was measured by technicians, not ranked by farmers (p. 6). The 3D-breeding model predicted performance in untested environments, not of untested genotypes (p. 4). The "Stated limitations" section mostly does not reflect what the authors say. not_established is missing.

## Fixes needed

1. **Region leaves out Oromia.** Card frontmatter: `region: Ethiopia (Amhara and Tigray highlands)`. Source p. 6: decentralized fields were in Amhara (471), Oromia (399) and Tigray (295). Only the two research stations were in Amhara and Tigray. Replace with:
   `region: Ethiopia (highlands of Amhara, Oromia and Tigray)`

2. **On-farm grain yield was measured, not ranked by farmers.** Summary, paragraph 2: "giving 4,660 farm plots ranked for grain yield and overall appreciation." Source p. 6: farmers ranked the four entries for overall appreciation, and field technicians collected grain yield in the plots after harvest. Page 4 stresses that farm yield was measured objectively and independently of appreciation. Replace the last sentence of paragraph 2 with:
   "A subset of 41 genotypes (38 purified landraces and 3 modern cultivars) was then distributed as tricot packages of three plus one commercial variety to 1,165 farmers in Amhara, Oromia and Tigray over three seasons (2013 to 2015), giving 4,660 farm plots. Farmers ranked the four entries for overall appreciation, and field technicians measured grain yield in each plot."

3. **"to predict untested genotypes" is not what the 3D-breeding model did.** Summary, paragraph 4. All 41 genotypes were tested on farms. The model was validated across seasons (blocked cross-validation, p. 7), and the stated aim of both approaches is prediction in untested environments (p. 4). SNP data entered the Plackett-Luce trees as a prior through an additive matrix (p. 7). Replace the first sentence of paragraph 4 with:
   "3D-breeding used the farm data directly. It modelled them with Plackett-Luce trees that split farms by environmental covariates, with SNP data added as a genomic prior, to predict genotype performance in untested seasons and environments."

4. **not_established is missing.** The paper is easy to stretch. Add:
   `not_established: that 3D-breeding predicts on-farm yield with high accuracy (Kendall tau was 0.109 for yield and 0.251 for appreciation); that the about 20% yield gain was observed in farmers' fields (it is a model prediction over 15 simulated seasons); that 3D-breeding predicts the performance of genotypes never tested on farms (all 41 were tested); that 3D-breeding increases genetic gain (the paper measures prediction accuracy only, and the authors say accuracy is one of several factors in genetic gain); that 3D-breeding should replace centralized breeding (the authors propose it as a complement); that results hold for other crops or regions (one durum wheat proof-of-concept in the Ethiopian highlands); that farmer gender has no effect on scores (heritability of appreciation was 0.84 for men and 0.67 for women)`

5. **Stated limitations are mostly not the authors' own.** "The design relied on one crop in one mega-environment" is not stated as a limitation anywhere (Not in source). The abstract only calls the study a proof-of-concept (p. 1). "Overall appreciation mixes many traits" is in the source (p. 4), but the authors present it as a strength that links appreciation to adoption, not as a limitation. Replace the section with:
   - The study is a proof-of-concept with one crop over three seasons. More seasons and management conditions are needed to find drivers of local performance beyond temperature (p. 1, p. 6).
   - Farmers evaluated top-performing genotypes preselected from a larger set. Future studies could test larger germplasm collections through 3D-breeding (p. 5).
   - Prediction accuracy is only one factor in genetic gain, so the findings need to fit into the wider picture of modern breeding (p. 5).
   - Open questions remain on how to motivate new farmers, how much seed each farmer needs, the logistics of supplying seed, and how to share benefits from farmers' knowledge (p. 5).
   - Implementation needs extra investment in seed multiplication, seed distribution and telecommunications, although costs per data point are lower than in conventional on-farm trials (p. 6).
   - The benchmark and 3D-breeding used different statistical designs, methods and numbers of observations. The authors tested 3D-breeding with 5% to 75% of the farm data to address this (p. 4, p. 7).
   - Participants were not stratified by socio-economic group beyond gender, so the full range of farmer knowledge was not characterized (p. 6).

6. **Gist undersells the method and oversells the result.** Card: "Combining genomics with tricot rankings ... predicted on-farm durum wheat performance far better than station-based genomic selection". 3D-breeding also uses environmental covariates (p. 1). The source says it "could double" accuracy (p. 1). Recomputed from Table 1, the ratio is about 2.4 for yield and 1.8 for appreciation, and absolute tau values stay low. Replace with (26 words):
   `gist: Combining genomics, on-farm tricot data from 1,165 Ethiopian farms and climate covariates (3D-breeding) roughly doubled the accuracy of station-based genomic prediction of on-farm durum wheat performance`

7. **Gender sentence oversimplifies.** Summary, paragraph 3: "Gender had little effect on scores, supporting their reliability." Source p. 2: heritability of station appreciation differed between men (0.84) and women (0.67), but their evaluations were consistent. Replace with:
   "Men's and women's scores differed in heritability (0.84 and 0.67) but agreed with each other, which the authors take as evidence that farmer scores are reliable."

8. **Covariate sentence is incomplete.** Summary, paragraph 4: "The best predictors split farms by minimum night temperature, separating cold- and warm-adapted genotypes." Source p. 7: from 110 covariates, selection kept maximum night temperature during reproductive growth and minimum night temperature during vegetative growth. Fig. 2a (p. 5) splits selections at a minimum night temperature of 11.5 °C. Replace with:
   "Out of 110 climate covariates, model selection kept two: minimum night temperature during vegetative growth and maximum night temperature during reproductive growth. The top genotypes differed between colder and warmer farms, split at a minimum night temperature of 11.5 °C."

9. **Model predictions written as observed results.** Summary, paragraph 4: "Genotypes selected by 3D-breeding beat the varieties currently recommended ..." Reliability and the yield increase are model predictions, and the yield gain was computed over 15 simulated seasons (p. 4, p. 7). Replace with:
   "The model predicted that genotypes selected by 3D-breeding, mostly derived from landraces, would beat the varieties currently recommended for the mega-environment (Asassa, Hitosa and Ude) for overall appreciation in most farmer fields. Reliability was 0.83 to 0.91, including areas where centralized breeding failed, and expected yield increases were about 20% across 15 simulated seasons."

10. **"can serve" is more certain than the source.** Summary, paragraph 5. Source p. 2: 3D-breeding "potentially ... could benefit" the about 500 million smallholders. Replace "They argue 3D-breeding can serve the roughly 500 million smallholders in low-input environments" with:
    "They argue 3D-breeding could potentially benefit the roughly 500 million smallholders in challenging, low-input environments"

11. **"mostly landraces" is not stated in this paper.** Summary, paragraph 2. Source p. 6 says the 400 genotypes came from landrace accessions at the Ethiopian Biodiversity Institute and improved lines grown in Ethiopia, with no proportion given. Replace "400 genotypes, mostly landraces," with "400 genotypes, landraces and improved lines,". Fix 2 covers the rest of that paragraph. Station names and years could also be added: "at two stations, Geregera (Amhara) and Hagreselam (Tigray), in 2012 and 2013 (3,200 plots). In 2012, 60 farmers (15 men and 15 women per station) also scored overall appreciation at flowering."

12. **"rather than treating it as noise" is added framing.** Summary, paragraph 6. Source p. 6 says only that 3D-breeding enables embracing real-world G × E for the benefit of breeding. Replace with:
    "The authors argue that 3D-breeding embraces the complexity of real-world genotype-by-environment interaction for the benefit of breeding, and that it rests on documented methods ..."

13. **Add the robustness result (important for tricot users planning sample size).** Source p. 4: with 5% to 75% of the farm data, 3D-breeding still beat the benchmark (tau 0.162 to 0.230 for appreciation, 0.076 to 0.106 for yield). Add after "...0.251 for on-farm appreciation." in paragraph 4:
    "It kept this advantage when trained on only 5% to 75% of the farm data."

14. **Data field leaves out the code.** Source p. 7: both data and code are on Dataverse. Ref. 56 (p. 8) lists SNP calls and genotype provenance as part of the dataset. Replace with:
    `data: https://doi.org/10.7910/DVN/OEZGVP (Harvard Dataverse, SNP calls, genotype provenance, trial data and code)`

15. **Key numbers: name the primary source for 500 million and label the chart value.** Change the Primary source of "~500 million" to "Lowder et al. 2016 (ref. 7), cited in this paper". Change the "~20%" context to "Expected yield increase from 3D-breeding selections, predicted over 15 simulated seasons (2001 to 2015), read from Fig. 2c". Add the rows listed under Completeness.

16. **Methods in brief: add the benchmark model and on-farm protocol.** Suggested replacements:
    - **Centralized trials.** Geregera (Amhara) and Hagreselam (Tigray), 2012 and 2013. 400 genotypes, replicated alpha lattice, 3,200 plots. Grain yield measured. In 2012, 60 farmers (15 men and 15 women per station) scored overall appreciation on a 1 to 5 Likert scale at flowering.
    - **Decentralized trials.** 41 genotypes (38 purified landraces and 3 modern cultivars). Each farmer received three genotypes plus a recommended variety (Asassa in Amhara and Tigray, Hitosa and Ude in Oromia). 1,165 farms over three seasons (2013 to 2015), 4,660 plots of 0.4 to 1.6 m². Farmers ranked the entries for overall appreciation, and technicians measured grain yield. No payment, and farmers kept the harvest.
    - **Benchmark.** Genomic prediction with rrBLUP on station BLUPs and marker-based relationship matrices. Accuracy was averaged over the three farm seasons with square-root-of-n weights.
    - **3D-breeding model.** Plackett-Luce trees with 110 agroclimatic covariates from NASA POWER and an SNP additive matrix as prior. Blocked cross-validation by season with forward selection on Akaike weights. Accuracy as Kendall's tau.

17. **Notes: add the source issues** listed below.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Data-driven decentralized breeding increases prediction accuracy in a challenging crop production environment | Same (p. 1) | Supported |
| authors | de Sousa K, van Etten J, Poland J, Fadda C, Jannink JL, Kidane YG, Lakew BF, Mengistu DK, Pè ME, Solberg SØ, Dell'Acqua M | Same 11 authors in same order (p. 1). Layer 1 flags on Solberg SØ and Dell'Acqua M are character-encoding only | Supported |
| year | 2021 | 2021, accepted 16 July 2021 (p. 1, p. 7) | Supported |
| journal | Communications Biology | Same (p. 1) | Supported |
| article | 4, 944 | (2021)4:944 (p. 1) | Supported |
| type | research article | "ARTICLE" (p. 1) | Supported |
| doi | https://doi.org/10.1038/s42003-021-02463-w | Same (p. 1) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution 4.0 International (p. 8) | Supported |
| data | https://doi.org/10.7910/DVN/OEZGVP (Harvard Dataverse, genotypes, SNP calls and trial data) | DOI correct (ref. 56, p. 8). Code is also on Dataverse (p. 7) | Imprecise (minor, see fix 14) |
| software | PlackettLuce, gosset | Both used (p. 6, p. 7). rrBLUP, ASReml-R, climatrends and nasapower also used | Supported (template format not followed, see Template compliance) |
| crops | durum wheat | Triticum durum (p. 1) | Supported |
| region | Ethiopia (Amhara and Tigray highlands) | Farms in Amhara, Oromia and Tigray (p. 6) | Imprecise (see fix 1) |
| gist | Combining genomics with tricot rankings ... far better than station-based genomic selection | Omits environmental data. Source says "could double" (p. 1) | Imprecise (see fix 6) |
| not_established | Missing | Several likely stretches (see fix 4) | Missing |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Tests whether combining genomics, farmer knowledge and environmental data (3D-breeding) predicts better than centralized breeding | Supported | Abstract and introduction (p. 1, p. 2) | |
| 2 | Summary | Durum wheat in the Ethiopian highlands, a challenging environment | Supported | p. 1, p. 2 | |
| 3 | Summary | Benchmark was centralized genomic selection | Supported | Table 1 "Centralized GS" (p. 3), p. 7 | Source also says the benchmark was enriched with farmer evaluations (p. 7) |
| 4 | Summary | 400 genotypes, mostly landraces, two stations, two seasons, 3,200 plots, 60 farmers scored at flowering | Imprecise | p. 6, p. 7 | "mostly" not stated. Numbers correct. 800 plots × 2 locations × 2 seasons = 3,200. Farmers scored in 2012 only (see fix 11) |
| 5 | Summary | 41 genotypes, tricot packages of three plus one commercial variety, 1,165 farmers, 4,660 plots ranked for grain yield and appreciation | Imprecise | p. 2, p. 6 | Grain yield measured by technicians, not ranked by farmers. 1,165 × 4 = 4,660 checked (see fix 2) |
| 6 | Summary | Station data predicted farm performance poorly | Supported | p. 2 | |
| 7 | Summary | Tau 0.046 for yield, 0.141 for appreciation | Supported | Table 1 (p. 3), p. 2 | |
| 8 | Summary | Station appreciation more heritable than yield, consistently positive accuracy for farm yield and appreciation | Supported | H² 0.78 vs 0.55 and 0.42, "Interestingly ..." (p. 2) | |
| 9 | Summary | Gender had little effect on scores | Imprecise | p. 2 | Heritability differed (0.84 vs 0.67), evaluations were consistent (see fix 7) |
| 10 | Summary | Plackett-Luce with covariates and genomic relationships to predict untested genotypes | Imprecise | p. 4, p. 7 | Prediction targets untested environments. Genomics entered as a prior (see fix 3) |
| 11 | Summary | Consistently outperformed benchmark, tau 0.109 and 0.251 | Supported | Table 1 (p. 3), p. 3 to 4 | Season 2 yield is 0.078 vs 0.076, a near tie, but the source says "consistently" too |
| 12 | Summary | Best predictors split farms by minimum night temperature | Imprecise | p. 7, Fig. 2 (p. 5) | Two covariates selected, threshold 11.5 °C not given (see fix 8) |
| 13 | Summary | Selected genotypes beat recommended varieties in most fields, reliability 0.83 to 0.91, about 20% yield gain | Imprecise | p. 4, Fig. 2b and 2c (p. 5) | Numbers correct. Written as observed, but these are model predictions (see fix 9). Fig. 2b box plots span roughly 0.83 to 0.92 (read off chart, approximate) |
| 14 | Summary | Parallel with dairy breeding and farm records | Supported | p. 4 | |
| 15 | Summary | 3D-breeding can serve about 500 million smallholders | Imprecise | p. 2 | Source: "potentially ... could benefit" (see fix 10) |
| 16 | Summary | More likely to produce adopted varieties | Supported | p. 4 | |
| 17 | Summary | Could later stratify farmers by gender, age or income | Supported | p. 6 | |
| 18 | Summary | Embraces real-world G × E rather than treating it as noise | Imprecise | p. 6 | "rather than treating it as noise" added (see fix 12) |
| 19 | Summary | Rests on documented methods, calls for good data management and sharing | Supported | p. 6 | |
| 20 | Summary | Larger designs and genomic datasets feasible, add power, as in livestock | Supported | p. 6 | Source frames it as "we believe" |
| 21 | Summary | More seasons and management could reveal drivers beyond temperature | Supported | p. 6 | |
| 22 | Summary | Combine with centralized breeding, study impact on agrobiodiversity | Supported | p. 6 | |
| 23 | Summary | Open-source digital tools make the approach transferable | Supported | p. 6 | |
| 24 | Methods | Centralized trials: 400, alpha lattice, two stations, two seasons, 3,200 plots, 60 farmers | Supported | p. 6, p. 7 | Station names, years and Likert scale missing (see fix 16) |
| 25 | Methods | Decentralized: 41 genotypes, three plus one check, 1,165 farms, 4,660 ranked plots | Supported | p. 6, p. 7 | Seasons, regions, plot size missing |
| 26 | Methods | SNP genotyping, genomic relationship matrix | Supported | 90k Infinium chip (p. 6), rrBLUP and additive matrix (p. 7) | |
| 27 | Methods | Plackett-Luce with covariates, Akaike weights across validation seasons, Kendall's tau | Supported | p. 7 | Benchmark model (rrBLUP) not described |
| 28 | Methods | Reliability = probability selected genotypes outperform recommended checks | Supported | p. 7, Eq. 2 | |
| 29 | Limitations | One crop in one mega-environment | Not in source | Not stated as a limitation. Abstract says proof-of-concept (p. 1) | See fix 5 |
| 30 | Limitations | Overall appreciation mixes many traits, yield only one | Imprecise | p. 4 | In source, but presented as a strength, not a limitation |
| 31 | Limitations | No socio-economic stratification | Supported | p. 6 | Future studies "may opt to stratify" |
| 32 | Key numbers | 400 genotypes | Supported | p. 2, p. 6 | |
| 33 | Key numbers | 3,200 plots | Supported | p. 7 | |
| 34 | Key numbers | 60 farmers | Supported | p. 6 | 2012 season only |
| 35 | Key numbers | 41 genotypes | Supported | p. 6 | 38 landraces + 3 modern cultivars |
| 36 | Key numbers | 1,165 farms, 4,660 plots | Supported | p. 6, p. 7 | 179 + 651 + 335 = 1,165 and 471 + 399 + 295 = 1,165 checked |
| 37 | Key numbers | τ = 0.046 | Supported | Table 1 (p. 3) | Simple mean of the three seasons is 0.0457 |
| 38 | Key numbers | τ = 0.141 | Supported | Table 1 (p. 3) | Simple mean is 0.1407 |
| 39 | Key numbers | τ = 0.109 / 0.251 | Supported | Table 1 (p. 3) | See source issue 1 on how these were averaged |
| 40 | Key numbers | 0.83–0.91 reliability | Supported | p. 4 | Reliability for overall appreciation, top 3 genotypes |
| 41 | Key numbers | ~20% yield increase | Supported | p. 4, Fig. 2c (p. 5) | Predicted over 15 simulated seasons. Bars in Fig. 2c sit roughly between 0.18 and 0.27 (read off chart, approximate) |
| 42 | Key numbers | ~500 million smallholders, cited | Supported | p. 2, ref. 7 | Name Lowder et al. 2016 (fix 15) |
| 43 | Notes | desousa-2024-asd cites this as 1,100 trials, paper reports 1,165 farms | Supported | de-sousa-et-al-2024 text says 1100 durum wheat on-farm trials. This paper p. 6 says 1,165 | |
| 44 | Notes | Asassa, Hitosa and Ude are recommended checks, also in vanetten-2019-pnas | Supported | p. 7. van Etten et al. 2019 PNAS names Hitosa, Ude and Assassa | Note spelling "Assassa" in PNAS |
| 45 to 56 | Metadata | title, authors, year, journal, article, type, doi, license, data, crops, region, gist | 9 Supported, 3 Imprecise | See Metadata check | |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Table 1 combined accuracies are not computed in one consistent way. Methods say season values were averaged with square-root-of-n weights. The benchmark rows match simple means (0.046, 0.141), 3D-breeding appreciation matches the weighted mean (0.251), and 3D-breeding yield (0.109) is closest to the weighted mean (0.110) but far from the simple mean (0.119). The reported ± values match simple standard deviations | Table 1 (p. 3), methods (p. 7) | No | - The combined tau values in Table 1 do not all follow the square-root-of-n weighting described in the methods. Recomputed from the season values (card's own calculation), the benchmark means match simple averages, and the 3D-breeding means are closer to weighted averages. The conclusion that 3D-breeding beats the benchmark holds either way. |
| The Dataverse dataset title says "increases genetic gain", while the article title says "increases prediction accuracy". The paper measures accuracy, not genetic gain | Ref. 56 (p. 8) | No | - The linked Dataverse dataset is titled "... increases genetic gain ...", but the article measures prediction accuracy, not genetic gain. |
| The text says farmers' appreciation predicted yield better than yield itself in both trial types, citing Table 1. Table 1 shows only appreciation-to-appreciation and yield-to-yield accuracies. The support is in Supplementary Figs. 3 and 5 | p. 4 | No | - The claim that appreciation predicts yield better than yield does is cited to Table 1, but Table 1 does not show it. The supporting data are in Supplementary Figs. 3 and 5. |
| In the first benchmark scenario, the 2013 subset of 41 genotypes is called the "training dataset". From context it is the test set | p. 7 | No | (low priority, no Notes text needed) |
| Fig. 2a legend says "3DD Cold tolerant", the caption says "3DB Cold tolerant" | p. 5 | No | (low priority, no Notes text needed) |
| Fig. 2c caption gives n = 1,165 observations, but the methods say predictions were made for 1,200 random points | p. 5, p. 7 | No | - Fig. 2c gives n = 1,165, while the methods describe predictions at 1,200 random points across the trial area. The about 20% yield gain is a model prediction. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: test 3D-breeding against a genomic prediction benchmark | Yes | high | |
| Farm distribution: Amhara 471, Oromia 399, Tigray 295. Seasons 2013 (179), 2014 (651), 2015 (335) (p. 6) | No | high | Fix 1, fix 2, and Key numbers rows: "471 / 399 / 295 \| Farms in Amhara / Oromia / Tigray \| This paper" and "179 / 651 / 335 \| Farms in season 1 (2013) / 2 (2014) / 3 (2015) \| This paper" |
| How farm data were collected: farmers ranked appreciation, technicians weighed yield (p. 6) | Wrong in card | high | Fix 2 |
| Authors' own limitations and open questions (p. 5, p. 6) | Mostly no | high | Fix 5 |
| Robustness to data size: 5% to 75% subsets still beat benchmark (p. 4) | No | medium-high | Fix 13 and Key numbers row: "τ = 0.162–0.230 / 0.076–0.106 \| 3D-breeding accuracy for farm appreciation / yield when trained on 5% to 75% of the data \| This paper" |
| 41 = 38 purified landraces + 3 modern cultivars, preselected by farmer evaluation at stations (p. 6) | No | medium | Fix 2 |
| 3D-breeding selections were landrace-derived and genetically distinct from recommended varieties (p. 4, Fig. 2a) | No | medium | Fix 9 |
| Heritability: station yield 0.55 (2012) and 0.42 (2013), appreciation 0.78, men 0.84, women 0.67 (p. 2) | Partly | medium | Key numbers rows: "H² = 0.55 / 0.42 \| Broad-sense heritability of station grain yield, 2012 / 2013 \| This paper" and "H² = 0.78 \| Heritability of station overall appreciation (men 0.84, women 0.67) \| This paper" |
| Farms were colder than stations, and the benchmark did better for cold-tolerant genotypes (p. 3) | No | medium | Summary: "Farms could be colder than the stations, and the benchmark did better when restricted to cold-tolerant genotypes." |
| Tricot plot size 0.4 to 1.6 m², no payment, farmers kept the harvest, farmer selection criteria (p. 6) | No | medium | Fix 16 and Key numbers row: "0.4–1.6 m² \| Tricot plot size, by season and location \| This paper" |
| Costs: lower per data point, but need seed multiplication, distribution, telecoms (p. 6) | No | medium | Fix 5 |
| Farm appreciation gave higher accuracy than farm yield in all fields, and appreciation relates to adoption (p. 4) | Partly | medium | Already implied by the taus. Could add to Summary paragraph 4 |
| 110 covariates and 11.5 °C threshold (p. 5, p. 7) | No | medium | Fix 8 and Key numbers rows: "110 \| Agroclimatic covariates screened for the Plackett-Luce trees \| This paper" and "11.5 °C \| Minimum night temperature separating cold and warm areas for genotype selection \| This paper" |
| Station-to-station validation reached tau up to 0.248 (p. 2) | No | low | Optional Key numbers row |
| Pearson and Kendall gave similar results, and training on ranks or absolute values made no difference (p. 7) | No | low | Optional, Methods |
| Conclusion: 3D-breeding as a complement to centralized breeding (p. 1, p. 5, p. 6) | Yes | high | |
| Ratio of accuracies (about 2.4 for yield, 1.8 for appreciation) | No | low | Optional Key numbers row, labelled "This card (own calculation from Table 1)" |

## Template compliance

- Summary word count: 423 (target 400 to 500). Pass. The suggested fixes add about 60 words and stay under 500.
- Gist: 21 words. Pass on length, but see fix 6 on content.
- Keywords: 10. Pass.
- Questions: 5. Pass.
- House style: tricot and maniva lowercase throughout. Pass.
- not_established: missing (fix 4).
- software: the template asks for the CRAN URL, version and check date (for example "PlackettLuce, https://CRAN.R-project.org/package=PlackettLuce (vX.Y on CRAN, published YYYY-MM-DD, checked YYYY-MM-DD)"). The card gives package names only. Low priority.
- relations: `extends: mancini-2017-scirep` is reasonable, but the 41 genotypes were chosen through the farmer evaluations of Mancini et al. 2017 (ref. 21, p. 6), so `usesDataFrom: mancini-2017-scirep` may be more exact. Optional.
