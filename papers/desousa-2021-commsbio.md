---
id: desousa-2021-commsbio
title: Data-driven decentralized breeding increases prediction accuracy in a challenging crop production environment
authors: de Sousa K, van Etten J, Poland J, Fadda C, Jannink JL, Kidane YG, Lakew BF, Mengistu DK, Pè ME, Solberg SØ, Dell'Acqua M
year: 2021
journal: Communications Biology
journal_short: Commun Biol
article: 4, 944
type: research article
doi: https://doi.org/10.1038/s42003-021-02463-w
open_copy: https://doi.org/10.1038/s42003-021-02463-w
license: CC BY 4.0
data: https://doi.org/10.7910/DVN/OEZGVP (Harvard Dataverse, genotypes, SNP calls and trial data)
software: PlackettLuce, gosset
crops: durum wheat
region: Ethiopia (Amhara and Tigray highlands)
keywords: 3D-breeding, genomic prediction, tricot, durum wheat, landraces, overall appreciation, G×E, decentralized breeding, prediction accuracy, reliability
gist: Combining genomics with tricot rankings from 1,165 Ethiopian farms (3D-breeding) predicted on-farm durum wheat performance far better than station-based genomic selection
---

## Questions this paper answers

- Can tricot data be combined with genomic data for selection?
- How well do research-station trials predict performance on farms?
- What is data-driven decentralized breeding (3D-breeding)?
- Is farmers' overall appreciation a useful breeding trait?
- What yield gains can locally adapted selections offer?

## Summary

The paper tests whether combining genomics, farmers' knowledge and environmental data, an approach the authors call data-driven decentralized breeding (3D-breeding), predicts crop performance in smallholder fields better than conventional centralized breeding. The setting is durum wheat in the Ethiopian highlands, a challenging and diverse production environment.

The benchmark was centralized genomic selection. 400 genotypes, mostly landraces, were genotyped and evaluated in replicated alpha-lattice trials at two stations over two seasons (3,200 plots), where 60 farmers also scored overall appreciation at flowering. A subset of 41 genotypes was then distributed as tricot packages of three plus one commercial variety to 1,165 farmers in the same breeding mega-environment, giving 4,660 farm plots ranked for grain yield and overall appreciation.

Station data predicted farm performance poorly. Using station grain yield to predict on-farm grain yield gave an average Kendall's tau of 0.046 per season, and station appreciation predicting farm appreciation gave 0.141. Station appreciation was more heritable than station yield and, interestingly, predicted on-farm yield and appreciation with consistently positive accuracy. Gender had little effect on scores, supporting their reliability.

3D-breeding used the farm rankings directly, modelled with Plackett-Luce and environmental covariates, with genomic relationships to predict untested genotypes. It consistently outperformed the benchmark, reaching tau of 0.109 for on-farm yield and 0.251 for on-farm appreciation. The best predictors split farms by minimum night temperature, separating cold- and warm-adapted genotypes. Genotypes selected by 3D-breeding beat the varieties currently recommended for the mega-environment (Asassa, Hitosa and Ude) in most farmer fields, with reliability of 0.83 to 0.91, including areas where centralized breeding failed, and with expected yield increases of about 20%.

The authors draw a parallel with dairy breeding, where farm records from many environments accelerated genetic evaluation. They argue 3D-breeding can serve the roughly 500 million smallholders in low-input environments, is more likely to produce adopted varieties, and could later stratify farmers by gender, age or income.

The authors argue that 3D-breeding embraces real-world genotype-by-environment interaction rather than treating it as noise, and that it rests on documented methods from trial design to data curation and analysis, which calls for good data management and sharing. Larger field designs and genomic datasets are feasible and would add power, as in livestock genetics, and more seasons and management conditions could reveal drivers of local performance beyond temperature. They suggest combining 3D-breeding with centralized breeding to train prediction models for local adaptation, and studying how varieties developed this way affect the conservation and use of traditional agrobiodiversity. Open-source digital tools make the approach transferable to new crops and contexts.

## Methods in brief

- **Centralized trials.** 400 genotypes, replicated alpha lattice, two stations, two seasons, 3,200 plots. Grain yield measured, overall appreciation scored by 60 farmers.
- **Decentralized trials.** 41 genotypes, tricot packages of three plus one commercial check, 1,165 farms, 4,660 ranked plots.
- **Genomics.** SNP genotyping, genomic relationship matrix for prediction.
- **Models.** Plackett-Luce with environmental covariates, covariate selection by Akaike weights across validation seasons, accuracy as Kendall's tau.
- **Reliability.** Probability that selected genotypes outperform the recommended checks.

## Stated limitations

- The design relied on one crop in one mega-environment.
- Overall appreciation mixes many traits, of which yield is only one.
- Participants were not stratified by socio-economic group, so the full range of farmer knowledge was not characterized.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 400 genotypes | Evaluated in centralized station trials | This paper |
| 3,200 plots | Station trials, two locations, two seasons | This paper |
| 60 farmers | Scored overall appreciation at stations | This paper |
| 41 genotypes | Distributed in tricot to farmers | This paper |
| 1,165 farms, 4,660 plots | Decentralized tricot trials | This paper |
| τ = 0.046 | Mean accuracy, station yield predicting farm yield per season | This paper |
| τ = 0.141 | Mean accuracy, station appreciation predicting farm appreciation | This paper |
| τ = 0.109 / 0.251 | 3D-breeding accuracy for farm yield / farm appreciation | This paper |
| 0.83–0.91 | Reliability of 3D-breeding selections vs recommended varieties | This paper |
| ~20% | Expected yield increase from 3D-breeding recommendations | This paper |
| ~500 million | Smallholder farmers who could benefit | Cited in this paper |

## Notes

- de Sousa et al. 2024 (desousa-2024-asd) cites this as 1,100 durum wheat on-farm trials. The paper itself reports 1,165 farms.
- Asassa, Hitosa and Ude are the checks recommended for the Ethiopian highland mega-environment, also discussed in vanetten-2019-pnas.
