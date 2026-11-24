---
id: dorado-2026-tag
title: Estimating on-farm genotypic performance and variability using ranking data
authors: Dorado-Betancourt H, van Eeuwijk F, van Etten J, Ramirez-Villegas J, de Sousa K, Daudi H, Ndegwa M, Mendes T, van Heerwaarden J
year: 2026
journal: Theoretical and Applied Genetics
journal_short: Theor Appl Genet
article: 139, 231
type: research article
source: team
peer_reviewed: yes
curated_card: yes
doi: https://doi.org/10.1007/s00122-026-05319-1
open_copy: https://doi.org/10.1007/s00122-026-05319-1
license: CC BY 4.0
data: groundnut and sweetpotato data in tricot-data, https://doi.org/10.5281/zenodo.17112492 (CC BY-SA 4.0); maize data on request (CIMMYT); code at https://github.com/hdorado/tricot-ranking-analysis, archived at https://doi.org/10.5281/zenodo.17942919 (MIT); supplementary information at https://doi.org/10.5281/zenodo.17941054 (CC BY 4.0)
software: PlackettLuce, https://CRAN.R-project.org/package=PlackettLuce (CRAN version not checked). The paper also used gosset, ClimMobTools and ASReml, and custom Thurstonian and Plackett-Luce code in the GitHub repository
crops: groundnut, maize, sweetpotato
region: Kenya, Mozambique, Tanzania (sub-Saharan Africa)
keywords: genetic parameters, heritability, variance components, Thurstonian model, Plackett-Luce, two-step analysis, mixed models, ranking data, quasi-variances, simulation, on-farm trials
gist: Shows, with simulations and four on-farm datasets, that tricot rankings fed into a two-step mixed model give reliable genotype means and heritability, given about 30 replicates per genotype
not_established: performance for taste, colour or other non-quantitative traits (only yield was tested); estimates of genetic gain or genotype × environment effects (left for future work); that raw Plackett-Luce estimates are on the same scale as yield-based means (they needed a scaling factor of about 0.85 to 0.90); that heritability from rankings equals heritability from measured yield (it was lower in three of four datasets); that 30 replicates per genotype are always enough (more are needed when genetic variation is high relative to residual variation); that rankings should replace yield measurement where farmers can measure yield (the authors say rankings may then be complementary or unnecessary)
---

## Questions this paper answers

- Can heritability and variance components be estimated from ranking data?
- Are genotype estimates from rankings linearly related to those from quantitative traits?
- How can ranking analyses plug into standard breeding analysis pipelines?
- How reliable are heritability estimates from tricot trials?
- How many replicates per genotype does a tricot trial need for reliable genetic parameters?
- Should I use the Plackett-Luce or the Thurstonian model to estimate heritability?

## Summary

On-station trials often fail to represent on-farm conditions and farmer preferences, which can lead to poorly defined breeding targets. On-farm trials with ranking data, such as tricot, are more representative, but scalable methods to quantify genetic differences and the strength of the genetic signal from rankings remained limited. This paper proposes and tests a two-step procedure.

The procedure follows the two-stage approach of quantitative genetics. In the first step, Thurstonian or Plackett-Luce models estimate genotypic means from rankings, with quasi-variances as their uncertainty, assuming rankings reflect an underlying continuous trait. In the second step, these estimates enter a mixed model weighted by the inverse quasi-variances to estimate the genetic standard deviation and Cullis heritability, as breeders do with yield trials.

The authors simulated 18,480 tricot trials of maize yield with 20 genotypes, varying the genetic and residual standard deviations and the replicates per genotype (3, 10, 30 or 100). Genotype means from rankings were linearly related to the true means, and their variances captured the uncertainty. The Thurstonian model was unbiased. The Plackett-Luce model was biased when the underlying trait is normal, but a scaling factor of about 0.85 to 0.90 aligned it, and after rescaling both models performed almost the same. Standard errors from rankings were larger than from yield measurements, and about 30% more replicates were needed for the same precision. In most scenarios, about 30 replicates per genotype gave accurate means, genetic standard deviation and heritability. More were needed when the ratio of genetic to residual standard deviation exceeded 2, a ratio the authors expect to stay lower on farms.

In 17% to 19% of simulated trials, some genotypes were repeatedly ranked best or worst, which made their estimates undefined and led to underestimated genetic standard deviation. Cullis heritability was negative in 17% to 19% of trials, and reference heritability below 0.25 was overestimated with both ranking and yield data. Heritability from rankings was lower than from yield, reflecting the information lost by ranking.

Four observed datasets with both farmer rankings and measured yield (groundnut in Tanzania, early- and intermediate-maturity maize in Kenya, sweetpotato in Mozambique) confirmed the approach. Genetic correlations between ranking-based and yield-based estimates were 0.961 to 0.997. In three of the four datasets, heritability from farmers' rankings was lower than from measured yield, for example 0.23 versus 0.36 in groundnut, but close to heritability from rankings derived from the measured yields. This suggests that farmers' ranking did not bias the estimates. In intermediate-maturity maize, genetic variation was so low that yield-based heritability was 0.001 while ranking-based heritability was 0.41, which the authors link to a limitation of Cullis heritability.

The authors argue that the procedure can handle rankings of non-quantitative traits such as flavour in the same way, but only yield was tested. They see it as a simple and flexible way to bring tricot data into standard breeding pipelines and multi-trial analyses. Genotype × environment effects, genetic gain and multi-trait analysis are left for future work.

## Methods in brief

- **Step 1.** Thurstonian and/or Plackett-Luce models give genotype utility means and quasi-variances per trial, with a check variety as reference.
- **Step 2.** A linear mixed model weighted by inverse quasi-variances estimates the genetic standard deviation (REML, ASReml) and Cullis broad-sense heritability.
- **Validation.** 18,480 simulated tricot trials of maize yield with 20 genotypes, with parameters from published on-farm maize trials in Africa: 11 genetic SDs × 14 residual SDs × 4 replicate levels (3, 10, 30, 100 per genotype), each run 30 times. Ranking-based estimates were compared with true values and with yield-based estimates. Plackett-Luce estimates were rescaled to the Thurstonian scale.
- **Application.** Four tricot datasets with farmer rankings and measured yield on the same farms: groundnut in Tanzania (54 genotypes, about 28.5 replicates each), early-maturity maize (12 genotypes, about 66.8) and intermediate-maturity maize (25 genotypes, about 58.7) in Kenya, and sweetpotato in Mozambique (8 genotypes, about 16.5). Technicians or trained lead farmers measured yield for groundnut and sweetpotato, and farmers measured it for maize. Groundnut and sweetpotato data are on Zenodo.
- **Code.** R functions and simulation workflow shared on GitHub and archived on Zenodo.

## Stated limitations

- Only yield was analysed, in both simulated and observed data. Traits with unknown distributions were not tested.
- Cullis heritability can be imprecise, unstable or negative when the ratio of genetic to residual standard deviation is very low. It was negative in 17% to 19% of simulated trials, and gave a very low yield-based value for intermediate-maturity maize.
- Heritability below 0.25 is overestimated, with both ranking-based and quantitative data.
- Genotypes repeatedly ranked best or worst give undefined estimates and inflated variances. The authors advise more replicates, or using only the order of genotypes, rather than removing these genotypes.
- More than 100 replicates may be needed when the true genetic standard deviation exceeds 2 (in units of residual standard deviation).
- Genotype × environment and genotype × year effects were not modelled. Designs with more than three genotypes per farm, ties, or within-farm replication were not assessed.
- Quasi-variances were used as weights instead of the full variance-covariance matrix, which may be less efficient.
- The maize data were not yet open at publication.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 17%–19% | Simulated trials with negative Cullis heritability (excluded from the heritability analysis). The paper gives the same range for trials with undefined estimates | This paper |
| 17%–19% | Simulated trials with an undefined covariance matrix, mainly when the genetic SD was above 1.5 and replicates below 30 | This paper |
| <0.25 | Reference heritability below which estimates are inflated | This paper |
| 3 crops | Groundnut, maize and sweetpotato in the applications | This paper |
| ~30 | Replicates per genotype that were usually sufficient | This paper |
| >100 | Replicates possibly needed when the true genetic standard deviation exceeds 2 (in units of residual SD) | This paper |
| 18,480 | Simulated tricot trials with 20 genotypes each (11 genetic SDs × 14 residual SDs × 4 replicate levels × 30 runs) | This paper |
| ~30% | Extra replicates needed with rankings to match the precision of yield measurement under typical on-farm conditions | This paper |
| 0.85–0.90 | Scaling factor for Plackett-Luce estimates when the genetic to residual SD ratio is 0.71 or lower and replicates exceed 30 (about 0.9 in the Discussion) | This paper |
| 0.961–0.997 | Genetic correlations between ranking-based and yield-based genotype effects in four observed datasets | This paper |
| 0.229 vs 0.359 | Cullis heritability from farmer rankings vs measured yield, groundnut, Tanzania | This paper |
| 0.407 vs 0.001 | Cullis heritability from farmer rankings vs measured yield, intermediate-maturity maize, Kenya, where genetic variation was very low | This paper |

## Notes

- From outside the source: this is the published version of a VeriXiv preprint (https://doi.org/10.12688/verixiv.2606.1). The journal PDF does not mention the preprint, and this check did not compare the two versions. Cite the journal article.
- From outside the source: the Zenodo dataset the paper cites for groundnut and sweetpotato (de Sousa et al. 2025, Global multi-crop agricultural trial data supported by citizen science) is tricot-data, the data layer of the AI-ready documentation, so users can rerun the analysis.
- Source issue: the paper gives 17–19% both for trials with undefined covariance matrices and for trials with negative Cullis heritability (p. 10). These are two separate outcomes, and the identical range may be a coincidence or a copying error.
- Source issue: the code archive DOI is 10.5281/zenodo.17942919 in the Data availability statement (p. 16) but 10.5281/zenodo.17943088 in the reference list (p. 17). One may be the concept DOI and the other a version DOI.
- Source issue: the scaling factor for Plackett-Luce is 0.85 to 0.90 for a ratio of 0.71 or lower in the Results (p. 8), but about 0.9 for a ratio below 1 in the Discussion (p. 14).
- Source issue: the Discussion says farmer rankings agree with yield measured by technicians (p. 15), but farmers measured maize yield (p. 8).
- Source issue: in the worked example for Eq. (3), the change of variables writes U2k = y2k − y1k, where the example needs y8k − y1k (p. 4).
- Complements desousa-2024-asd, which suggests Plackett-Luce worth can give direct estimates of genetic value.
