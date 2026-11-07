---
id: woldeyohannes-2022-elife
title: Data-driven, participatory characterization of farmer varieties discloses teff breeding potential under current and future climates
authors: Woldeyohannes AB, Iohannes SD, Miculan M, Caproni L, Ahmed JS, de Sousa K, Desta EA, Fadda C, Pè ME, Dell'Acqua M
year: 2022
journal: eLife
journal_short: eLife
article: 11, e80009
type: research article
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.7554/eLife.80009
open_copy: https://doi.org/10.7554/eLife.80009
license: CC BY 4.0
data: sequencing reads on NCBI SRA (BioProject PRJNA758057); accessions from the Ethiopian Biodiversity Institute on request; scripts at https://github.com/mdellh2o/TeffDiversityPanel (archived at swh:1:rev:4935b0ef76f4c1631d323d39777ec375912e2f82); the farmer-rating workflow is curated in https://github.com/AgrDataSci/tricot-analysis-workflows (use-cases/can-farmer-ratings-be-analysed-as-rankings)
software: PlackettLuce (R package, https://CRAN.R-project.org/package=PlackettLuce, check the current CRAN version), ASReml-R, rMVP, gradientForest, adegenet
crops: teff
region: Ethiopia (collection across the teff cropping area; common gardens at Adet, Amhara, and Akaki, Oromia)
keywords: teff, farmer varieties, landraces, participatory variety selection, farmer appreciation, Likert scores, Plackett-Luce, gender, heritability, GWAS, genomic offset, climate change, neglected and underutilized species, Ethiopia
gist: Characterises 366 Ethiopian teff varieties with genomics, agronomy, farmer scores and climate, finding farmer appreciation highly heritable, gender-specific trait weights, and a lake Tana region most vulnerable to climate change
not_established: that candidate genes near QTNs are causal, since low-density genotyping and population structure confound associations; that the two common-garden locations represent the range of teff environments; that the genomic offset predicts yield loss
relations:
  - usesMethodIn: gesesse-2023-pnas  # the same farmer-rating to Plackett-Luce workflow, with scores converted to paired comparisons and worth linked to agronomic traits
  - agreesWith: desousa-2021-commsbio  # farmer appreciation is heritable and informative for breeding
  - citesAsDataSource: mancini-2017-scirep  # earlier participatory evaluation of durum wheat in Ethiopia showing gender differences
---

## Questions this paper answers

- Can farmer scores on a Likert scale be analysed with a ranking model, and what do they add to agronomic data?
- Is farmer appreciation of teff varieties heritable?
- Do women and men farmers weigh traits differently when they score teff?
- Which traits drive farmers' overall appreciation of teff?
- How is teff genetic diversity distributed across Ethiopia, and where is it most vulnerable to climate change?
- Can farmer varieties outperform improved lines?

## Summary

Aemiro Bezabih Woldeyohannes, Sessen Daniel Iohannes and colleagues, in work led by Matteo Dell'Acqua's group at Scuola Superiore Sant'Anna with Kauê de Sousa among the authors, characterise the Ethiopian Teff Diversity Panel, 321 farmer varieties and 45 improved lines, with genomics, agronomy, farmer evaluation and climate data. Teff is a neglected and underutilized cereal that feeds much of Ethiopia and has had little breeding investment, and the paper asks what a data-driven, participatory characterisation can reveal of its breeding potential.

Genotyping with 12,153 SNPs grouped the panel into ten genetic clusters with high admixture. Genetic distance between districts followed both geographic and environmental distance, and some clusters are associated with warmer or cooler and wetter sampling areas, with accessions from Tigray most separated. Improved varieties have a narrow genetic base compared with the farmer varieties.

The panel was grown in common gardens at Adet and Akaki in 2018, in an alpha lattice design with two replications, and phenotyped for phenology, morphology and yield. Thirty-five experienced teff farmers, fifteen women and twenty men, scored every plot for panicle appreciation and overall appreciation on a scale from one to five, in gender-homogeneous groups of five, near physiological maturity. Overall appreciation had a broad-sense heritability of 0.81 across genders and locations, higher than grain yield (0.42), so farmer scores are a repeatable, genetically determined trait. Farmer appreciation correlated with yield and its components regardless of gender, but women weighted biomass and panicle weight and men plant height and grain filling period. Top-ranked varieties by women and men differed in genetic background but shared the same trait combination, tall, high-yielding and fast-maturing. The farmer scores were analysed with a Plackett-Luce model, after the scores were converted to orderings within farmer, and linked to agronomic traits, which gave the gender-specific coefficients in Table 3. Several farmer varieties matched or exceeded improved lines, and EBI 9551 combined a short grain filling period with high yield and appreciation.

A genome-wide association study found 91 QTNs, 43 of them for bioclimatic variables, with a region on chromosome 2A associated with grain yield, grain filling rate and overall appreciation. A gradient forest model of allele turnover along environmental gradients, projected to 2070 climates under four RCPs, located the highest genomic offset in the north-western highlands south of lake Tana, where rainfall is projected to decrease and hot nights to increase.

The paper matters for the knowledge base because it shows farmer scores on a short scale carrying strong genetic signal and feeding a ranking model, and because gender differences in trait weighting appear even when both groups prefer the same ideotype. The authors conclude that transdisciplinary characterisation can bring untapped farmer varieties of neglected crops into breeding.

## Methods in brief

- **Panel.** 321 farmer varieties and 45 improved varieties from a 3,850-accession EBI collection, plus seven wild Eragrostis accessions. ddRAD sequencing, 12,153 SNPs, DAPC with ten clusters, ADMIXTURE.
- **Trials.** Two locations (Adet and Akaki), alpha lattice, two replications, 2018 main season. Phenology, morphology and yield traits. BLUPs and heritability with ASReml-R.
- **Farmer evaluation.** 35 farmers, 15 women and 20 men, scoring panicle and overall appreciation from one to five, simultaneous scoring in groups of five to reduce within-group bias. Analysed with a Plackett-Luce model, agronomic traits linked to farmer worth with an alternating directions method of multipliers (pladmm).
- **Climate.** WorldClim 2 bioclimatic variables at sampling sites, VIF-pruned, HadGEM2-ES projections for 2070 under RCP2.6 to 8.5.
- **Genetics.** GWAS with FarmCPU (rMVP), FDR 5%, candidate genes from LD blocks. Gradient forest for genomic offset.

## Stated limitations

- Low-density genotyping and population structure may confound associations; candidate genes are preliminary.
- Two locations cannot capture the full genotype by environment interaction in teff; the authors call for multilocation and decentralised testing.
- Farmers in the trials were expert growers from the two sites, not a representative sample of all teff farmers.
- The genomic offset is a measure of mismatch, not a prediction of yield.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 366 | Accessions in the Ethiopian Teff Diversity Panel, 321 farmer varieties and 45 improved | This paper |
| 12,153 | SNPs after filtering | This paper |
| 10 | Genetic clusters (DAPC) | This paper |
| 35 | Farmers in the participatory evaluation, 15 women and 20 men | This paper |
| 1 to 5 | Score scale for panicle and overall appreciation | This paper |
| 0.81 | Broad-sense heritability of overall appreciation across genders and locations | This paper |
| 0.42 | Broad-sense heritability of grain yield across locations | This paper |
| 0.48 | Broad-sense heritability of panicle appreciation | This paper |
| 91 | Unique QTNs from the GWAS, 43 for bioclimatic variables | This paper |
| 2070 | Horizon of the climate projections | This paper |

## Notes

- Companion in method to gesesse-2023-pnas. The scripts kept at AgrDataSci/teff-breeding-elife are in fact the EtNAM durum wheat analysis of the PNAS paper; the teff scripts are in the Dell'Acqua lab repository listed under data.
- The Plackett-Luce coefficients for women in Table 3 are large (intercept 15.6, panicle weight 4.4) compared with men's, which suggests a different scaling of the covariates between groups. Check the original scripts before quoting them.
- Table 1 reports heritability of overall appreciation by gender and location, 0.53 to 0.88.
- The women's sample is small and unevenly spread across the two sites, 10 women and 15 men at Adet and 5 of each at Akaki (Methods). The gender and gender by location effects on the farmer scores are both significant (Supplementary file 1D), so a gender difference here is partly a site difference. Use it as evidence that trait weights can differ by gender, not as a measured gender gap in teff preference.
