---
id: desousa-2021-commsbio
title: Data-driven decentralized breeding increases prediction accuracy in a challenging crop production environment
authors: de Sousa K, van Etten J, Poland J, Fadda C, Jannink JL, Kidane YG, Lakew BF, Mengistu DK, Pè ME, Solberg SØ, Dell'Acqua M
year: 2021
journal: Communications Biology
journal_short: Commun Biol
article: 4, 944
type: research article
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1038/s42003-021-02463-w
open_copy: https://doi.org/10.1038/s42003-021-02463-w
license: CC BY 4.0
data: https://doi.org/10.7910/DVN/OEZGVP (Harvard Dataverse, SNP calls, genotype provenance, trial data and code)
software: PlackettLuce, gosset
crops: durum wheat
region: Ethiopia (highlands of Amhara, Oromia and Tigray)
keywords: 3D-breeding, genomic prediction, tricot, durum wheat, landraces, overall appreciation, G×E, decentralized breeding, prediction accuracy, reliability
gist: Combining genomics, on-farm tricot data from 1,165 Ethiopian farms and climate covariates (3D-breeding) roughly doubled the accuracy of station-based genomic prediction of on-farm durum wheat performance
not_established: that 3D-breeding predicts on-farm yield with high accuracy (Kendall tau was 0.109 for yield and 0.251 for appreciation); that the about 20% yield gain was observed in farmers' fields (it is a model prediction over 15 simulated seasons); that 3D-breeding predicts the performance of genotypes never tested on farms (all 41 were tested); that 3D-breeding increases genetic gain (the paper measures prediction accuracy only, and the authors say accuracy is one of several factors in genetic gain); that 3D-breeding should replace centralized breeding (the authors propose it as a complement); that results hold for other crops or regions (one durum wheat proof-of-concept in the Ethiopian highlands); that farmer gender has no effect on scores (heritability of appreciation was 0.84 for men and 0.67 for women)
relations:
  - usesDataFrom: mancini-2017-scirep  # the 41 genotypes were chosen through the farmer evaluations reported there
  - extends: vanetten-2019-pnas
---

## Questions this paper answers

- Can tricot data be combined with genomic data for selection?
- How well do research-station trials predict performance on farms?
- What is data-driven decentralized breeding (3D-breeding)?
- Is farmers' overall appreciation a useful breeding trait?
- What yield gains can locally adapted selections offer?

## Summary

The paper tests whether combining genomics, farmers' knowledge and environmental data, an approach the authors call data-driven decentralized breeding (3D-breeding), predicts crop performance in smallholder fields better than conventional centralized breeding. The setting is durum wheat in the Ethiopian highlands, a challenging and diverse production environment.

The benchmark was centralized genomic selection. 400 genotypes, landraces and improved lines, were genotyped and evaluated in replicated alpha-lattice trials at two stations in 2012 and 2013 (3,200 plots). In 2012, 60 farmers also scored overall appreciation at flowering. A subset of 41 genotypes (38 purified landraces and 3 modern cultivars) was then distributed as tricot packages of three plus one commercial variety to 1,165 farmers in Amhara, Oromia and Tigray over three seasons (2013 to 2015), giving 4,660 farm plots. Farmers ranked the four entries for overall appreciation, and field technicians measured grain yield.

Station data predicted farm performance poorly. Station grain yield predicted on-farm grain yield with an average Kendall's tau of 0.046 per season, and station appreciation predicted farm appreciation with 0.141. Station appreciation was more heritable than station yield and predicted on-farm yield and appreciation with consistently positive accuracy. Men's and women's scores differed in heritability (0.84 and 0.67) but agreed with each other, showing, the authors argue, that farmer scores are reliable.

3D-breeding modelled the farm data directly with Plackett-Luce trees that split farms by environmental covariates, with SNP data added as a genomic prior, to predict genotype performance in untested seasons and environments. It consistently outperformed the benchmark, with tau of 0.109 for on-farm yield and 0.251 for on-farm appreciation. It kept this advantage when trained on only 5% to 75% of the farm data. Out of 110 climate covariates, model selection kept two: minimum night temperature during vegetative growth and maximum night temperature during reproductive growth. Top genotypes differed between farms below and above a minimum night temperature of 11.5 °C. The model predicted that genotypes selected by 3D-breeding, mostly derived from landraces, would beat the recommended varieties (Asassa, Hitosa and Ude) for overall appreciation in most farmer fields. Reliability was 0.83 to 0.91, including areas where centralized breeding failed, and expected yield increases were about 20% across 15 simulated seasons.

They draw a parallel with dairy breeding, where farm records from many environments accelerated genetic evaluation. They argue 3D-breeding could potentially benefit the roughly 500 million smallholders in challenging, low-input environments, is more likely to produce adopted varieties, and could later stratify farmers by gender, age or income.

The authors argue that 3D-breeding embraces the complexity of real-world genotype-by-environment interaction for the benefit of breeding. It rests on documented methods, from trial design to data analysis, and calls for good data management and sharing. Larger datasets would add power, and more seasons and management conditions could reveal drivers of local performance beyond temperature. They suggest combining 3D-breeding with centralized breeding to improve models for local adaptation, and studying its effect on traditional agrobiodiversity. Open-source digital tools make the approach transferable to new crops and settings.

## Methods in brief

- **Centralized trials.** Geregera (Amhara) and Hagreselam (Tigray), 2012 and 2013. 400 genotypes, replicated alpha lattice, 3,200 plots. Grain yield measured. In 2012, 60 farmers (15 men and 15 women per station) scored overall appreciation on a 1 to 5 Likert scale at flowering.
- **Decentralized trials.** 41 genotypes (38 purified landraces and 3 modern cultivars). Each farmer received three genotypes plus a recommended variety (Asassa in Amhara and Tigray, Hitosa and Ude in Oromia). 1,165 farms over three seasons (2013 to 2015), 4,660 plots of 0.4 to 1.6 m². Farmers ranked the entries for overall appreciation, and technicians measured grain yield. No payment, and farmers kept the harvest.
- **Genomics.** SNP genotyping, genomic relationship matrix for prediction.
- **Benchmark.** Genomic prediction with rrBLUP on station BLUPs and marker-based relationship matrices. Accuracy was averaged over the three farm seasons with square-root-of-n weights.
- **3D-breeding model.** Plackett-Luce trees with 110 agroclimatic covariates from NASA POWER and an SNP additive matrix as prior. Blocked cross-validation by season with forward selection on Akaike weights. Accuracy as Kendall's tau.
- **Reliability.** Probability that selected genotypes outperform the recommended checks.

## Stated limitations

- The study is a proof-of-concept with one crop over three seasons. More seasons and management conditions are needed to find drivers of local performance beyond temperature.
- Farmers evaluated top-performing genotypes preselected from a larger set. Future studies could test larger germplasm collections through 3D-breeding.
- Prediction accuracy is only one factor in genetic gain, so the findings need to fit into the wider picture of modern breeding.
- Open questions remain on how to motivate new farmers, how much seed each farmer needs, the logistics of supplying seed, and how to share benefits from farmers' knowledge.
- Implementation needs extra investment in seed multiplication, seed distribution and telecommunications, although costs per data point are lower than in conventional on-farm trials.
- The benchmark and 3D-breeding used different statistical designs, methods and numbers of observations. The authors tested 3D-breeding with 5% to 75% of the farm data to address this.
- Participants were not stratified by socio-economic group beyond gender, so the full range of farmer knowledge was not characterized.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 400 genotypes | Evaluated in centralized station trials | This paper |
| 3,200 plots | Station trials, two locations, two seasons | This paper |
| 60 farmers | Scored overall appreciation at stations | This paper |
| 41 genotypes | Distributed in tricot to farmers | This paper |
| 1,165 farms, 4,660 plots | Decentralized tricot trials | This paper |
| 471 / 399 / 295 | Farms in Amhara / Oromia / Tigray | This paper |
| 179 / 651 / 335 | Farms in season 1 (2013) / 2 (2014) / 3 (2015) | This paper |
| 0.4–1.6 m² | Plot size of tricot trials, by season and location | This paper |
| H² = 0.55 / 0.42 | Broad-sense heritability of station grain yield, 2012 / 2013 | This paper |
| H² = 0.78 | Heritability of station overall appreciation (men 0.84, women 0.67) | This paper |
| τ = 0.046 | Mean accuracy, station yield predicting farm yield per season | This paper |
| τ = 0.141 | Mean accuracy, station appreciation predicting farm appreciation | This paper |
| τ = 0.109 / 0.251 | 3D-breeding accuracy for farm yield / farm appreciation | This paper |
| τ = 0.162–0.230 / 0.076–0.106 | 3D-breeding accuracy for farm appreciation / yield when trained on 5% to 75% of the data | This paper |
| 110 | Agroclimatic covariates screened for the Plackett-Luce trees | This paper |
| 11.5 °C | Minimum night temperature separating cold and warm areas for genotype selection | This paper |
| 0.83–0.91 | Reliability of 3D-breeding selections vs recommended varieties | This paper |
| ~20% | Expected yield increase from 3D-breeding selections, predicted over 15 simulated seasons (2001 to 2015), read from Fig. 2c | This paper |
| ~500 million | Smallholder farmers who could benefit | Lowder et al. 2016 (ref. 7), cited in this paper |

## Notes

- de Sousa et al. 2024 (desousa-2024-asd) cites this as 1,100 durum wheat on-farm trials. The paper itself reports 1,165 farms.
- Asassa, Hitosa and Ude are the checks recommended for the Ethiopian highland mega-environment, also discussed in vanetten-2019-pnas.
- Problem in the source: the combined tau values in Table 1 do not all follow the square-root-of-n weighting described in the methods. Recomputed from the season values (card's own calculation), the benchmark means match simple averages, and the 3D-breeding means are closer to weighted averages. The conclusion that 3D-breeding beats the benchmark holds either way.
- Problem in the source: the linked Dataverse dataset is titled "... increases genetic gain ...", but the article measures prediction accuracy, not genetic gain.
- Problem in the source: the claim that appreciation predicts yield better than yield does is cited to Table 1, but Table 1 does not show it. The supporting data are in Supplementary Figs. 3 and 5.
- Problem in the source: Fig. 2c gives n = 1,165, while the methods describe predictions at 1,200 random points across the trial area. The about 20% yield gain is a model prediction.
- Problem in the source: in the first benchmark scenario, the methods call the 2013 subset of 41 genotypes the "training dataset", but from context it is the test set.
- Problem in the source: the Fig. 2a legend reads "3DD Cold tolerant", while the caption says "3DB Cold tolerant".
