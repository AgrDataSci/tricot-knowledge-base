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
license: CC BY (Creative Commons Attribution License, version not stated in the PDF)
data: sequencing reads on NCBI SRA (BioProject PRJNA758057); accessions from the Ethiopian Biodiversity Institute on request; scripts at https://github.com/mdellh2o/TeffDiversityPanel (archived at swh:1:rev:4935b0ef76f4c1631d323d39777ec375912e2f82); the farmer-rating workflow is curated in https://github.com/AgrDataSci/tricot-analysis-workflows (use-cases/can-farmer-ratings-be-analysed-as-rankings)
software: PlackettLuce (R package, https://CRAN.R-project.org/package=PlackettLuce, check the current CRAN version), ASReml-R, rMVP, gradientForest, adegenet
crops: teff
region: Ethiopia (collection across the teff cropping area; common gardens at Adet, Amhara, and Akaki, Oromia)
keywords: teff, farmer varieties, participatory variety selection, farmer appreciation, Likert scores, Plackett-Luce, gender, heritability, GWAS, genomic offset, climate change, Ethiopia
gist: Farmer scores of 366 Ethiopian teff accessions were highly heritable, women and men weighted traits differently but preferred one ideotype, and genomic offset peaked south of lake Tana
not_established: that candidate genes near QTNs are causal, since low-density genotyping and population structure confound associations; that the two common-garden locations represent the range of teff environments; that the genomic offset predicts yield loss; that women and men prefer different teff varieties, since both chose the same ideotype and gender is confounded with site; that the paper validates converting Likert scores to rankings; that farmer scores are more heritable than yield within a location
relations:
  - usesMethodIn: gesesse-2023-pnas  # the same farmer-rating to Plackett-Luce workflow, with scores converted to paired comparisons and worth linked to agronomic traits
  - agreesWith: desousa-2021-commsbio  # farmer appreciation is heritable and informative for breeding
  - citesAsDataSource: mancini-2017-scirep  # earlier participatory evaluation of durum wheat in Ethiopia showing gender differences
---

## Questions this paper answers

- How were farmer Likert scores analysed with a ranking model, and what do they add to agronomic data?
- Is farmer appreciation of teff varieties heritable?
- Do women and men farmers weigh traits differently when they score teff?
- Which traits drive farmers' overall appreciation of teff?
- How is teff genetic diversity distributed across Ethiopia, and where is it most vulnerable to climate change?
- Can farmer varieties outperform improved lines?

## Summary

Aemiro Bezabih Woldeyohannes, Sessen Daniel Iohannes and colleagues, in work led by Matteo Dell'Acqua's group at Scuola Superiore Sant'Anna with Kauê de Sousa among the authors, characterise the Ethiopian Teff Diversity Panel, 321 farmer varieties and 45 improved lines, with genomics, agronomy, farmer evaluation and climate data. Teff is a neglected and underutilized cereal that feeds much of Ethiopia and whose yields remain low despite decades of breeding, and the paper asks what a data-driven, participatory characterisation can reveal of its breeding potential.

Genotyping with 12,153 SNPs grouped the panel into ten genetic clusters with high admixture. Genetic distance between districts followed both geographic and environmental distance, and some clusters are associated with warmer or cooler and wetter sampling areas, with accessions from Tigray most separated. Improved varieties have a narrow genetic base compared with the farmer varieties.

The panel was grown in common gardens at Adet and Akaki in 2018, in an alpha lattice design with two replications, and phenotyped for phenology, morphology and yield. Thirty-five experienced teff farmers, fifteen women and twenty men, scored every plot for panicle appreciation and overall appreciation on a scale from one to five, in gender-homogeneous groups of five, near physiological maturity. Overall appreciation had a broad-sense heritability of 0.81 across genders and locations, higher than grain yield combined across locations (0.42), so farmer scores are highly heritable, at a level comparable to agronomic traits. Overall appreciation scores were analysed with a Plackett-Luce model linked to agronomic traits. Across all farmers, higher grain yield and a longer grain filling period went with higher worth, and taller plants with lower worth, once the other traits were accounted for (Table 3). The text reports that women's scores followed biomass and panicle weight and men's followed plant height and grain filling period, but the gender-specific estimates in Table 3 only partly support this (see Notes). Top-ranked varieties by women and men differed in genetic background but shared one trait combination: high yield, high biomass and fast maturity. Several farmer varieties matched or exceeded improved lines, and EBI 9551 combined a short grain filling period with high yield and appreciation. Improved lines also scored high, which the authors link to the high-potential trial sites.

A genome-wide association study found 91 QTNs, 43 of them for bioclimatic variables, with a region on chromosome 2A associated with grain yield, grain filling rate and overall appreciation. A gradient forest model of allele turnover along environmental gradients, projected to 2070 climates under four RCPs, located the highest genomic offset in the north-western highlands south of lake Tana, where rainfall is projected to decrease and hot nights to increase.

The paper matters for the knowledge base because it shows farmer scores on a short scale carrying strong genetic signal and feeding a ranking model, and because gender differences in trait weighting appear even when both groups prefer the same ideotype. The authors conclude that transdisciplinary characterisation may help bring untapped farmer varieties of neglected crops into breeding.

## Methods in brief

- **Panel.** 321 farmer varieties selected from a 3,850-accession EBI collection, all 45 improved varieties released up to the panel's assembly (from Ethiopian research centres), plus seven wild Eragrostis accessions. ddRAD sequencing, 12,153 SNPs, DAPC with ten clusters, ADMIXTURE.
- **Trials.** Two locations (Adet and Akaki), alpha lattice, two replications, 2018 main season. Phenology, morphology and yield traits. BLUPs and heritability with ASReml-R.
- **Farmer evaluation.** 35 farmers, 15 women and 20 men, scoring panicle and overall appreciation from one to five, simultaneous scoring in gender-homogeneous groups of five to reduce within-group bias. Farmers were recognised local experts chosen with agricultural officers, joined focus groups and training before scoring, worked with interpreters (Amharic and Oromo), and each score was recorded individually. Analysed with a Plackett-Luce model, agronomic traits linked to farmer worth with a linear model fitted by an alternating directions method of multipliers (ADMM) algorithm (the R package is not named in the paper).
- **Climate.** WorldClim 2 bioclimatic variables at sampling sites, VIF-pruned, HadGEM2-ES projections for 2070 under RCP2.6 to 8.5.
- **Genetics.** GWAS with FarmCPU (rMVP), FDR 5%, candidate genes from LD blocks. Gradient forest for genomic offset.

## Stated limitations

- Low-density genotyping and population structure may confound associations. Candidate genes are preliminary.
- Two locations cannot capture the full genotype by environment interaction in teff. The authors call for multilocation and decentralised testing.
- The design cannot fully separate the effects of geography, environment and social factors on genetic distance (p. 4).
- The causes of gender differences in teff trait preference need further study, including teff's double use as food and feed (p. 6).
- Candidate genes have not been validated, especially where signals may be confounded by population structure (p. 10).

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
| 0.92 and 0.93 | Broad-sense heritability of grain yield within Adet and within Akaki | This paper |
| 67% | Share of grain yield variance explained by location | This paper |
| 0.48 | Broad-sense heritability of panicle appreciation | This paper |
| 91 | Unique QTNs from the GWAS, 43 for bioclimatic variables | This paper |
| 2070 | Horizon of the climate projections | This paper |

## Notes

- Companion in method to gesesse-2023-pnas. The scripts kept at AgrDataSci/teff-breeding-elife are in fact the EtNAM durum wheat analysis of the PNAS paper. The teff scripts are in the Dell'Acqua lab repository listed under data.
- The Plackett-Luce coefficients for women in Table 3 are large (intercept 15.6, panicle weight 4.4) compared with men's, which suggests a different scaling of the covariates between groups. Check the original scripts before quoting them.
- Table 1 reports heritability of overall appreciation by gender and location, 0.53 to 0.88.
- The women's sample is small and unevenly spread across the two sites, 10 women and 15 men at Adet and 5 of each at Akaki (Methods). The gender and gender by location effects on the farmer scores are both significant (Supplementary file 1D), so a gender difference here is partly a site difference. Use it as evidence that trait weights can differ by gender, not as a measured gender gap in teff preference.
- Table 3 only partly matches the text (p. 6), which cites it. Men's plant height coefficient is significant but negative (shorter plants preferred), and their grain filling period is not significant (p = 0.149). Women's grain yield coefficient is negative (p = 0.003), although the text says appreciation went with yield regardless of gender. Women's positive biomass and panicle weight coefficients do match the text. Quote the pooled (All) estimates, not the gender claims.
- The paper does not describe how the one-to-five scores were turned into rankings for the Plackett-Luce model, or how ties were handled (Methods, p. 16). Check the scripts before reusing the approach.
- The gap between overall appreciation (H2 0.81) and grain yield (0.42) holds only for values combined across locations. Within location, grain yield H2 was 0.92 at Adet and 0.93 at Akaki, above overall appreciation at 0.71 and 0.87 (Tables 1 and 2). Location explained 67% of yield variance (p. 6). Do not quote the comparison as farmer scores being more heritable than yield in general.
- The farmers were recognised expert teff growers chosen with agricultural officers (p. 16). The paper does not claim they represent teff farmers in general (card writer's note).
- Problem in the source: in the text, references to Figures 2 and 3 are swapped. Farmer correlations, top-ranked genotypes and the Venn diagram are in Figure 3 (p. 9), and the Fst and bioclimatic panels are in Figure 2 (p. 7).
- Problem in the source: the star legend in Table 3 has reversed inequalities. Read it as one star for p < 0.05, two for p < 0.01, three for p < 0.001.
