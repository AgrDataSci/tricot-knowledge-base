---
id: brown-2022-cropsci
title: Rank-based data synthesis of common bean on-farm trials across four Central American countries
authors: Brown D, de Bruin S, de Sousa K, Aguilar A, Barrios M, Chaves N, Gómez M, Hernández JC, Machida L, Madriz B, Mejía P, Mercado L, Pavón M, Rosas JC, Steinke J, Suchini JG, Zelaya V, van Etten J
year: 2022
journal: Crop Science
journal_short: Crop Sci
article: 62(6), 2246-2266
type: research article
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1002/csc2.20817
open_copy: https://doi.org/10.1002/csc2.20817
license: CC BY
data: R code and data to replicate the results at https://github.com/AgrDataSci/Data_synthesis_bean_tricot_CA
software: PlackettLuce, gosset
crops: common bean
region: Costa Rica, El Salvador, Honduras, Nicaragua
keywords: data synthesis, rank aggregation, meta-analysis, Plackett-Luce trees, environmental covariates, WSDI, heat, planting date, survival analysis, area of applicability, variety maps
gist: Pools 14 tricot common bean trials from four Central American countries into one Plackett-Luce analysis, finding heat the main driver and mapping variety performance by season
not_established: that the environmental covariates greatly improve prediction of farmer rankings (cross-validated gains over the no-covariate model were small); that heat is the only factor driving bean variety performance in Central America; that the maps are direct variety recommendations for genotypes tested in only one country; that the planting-date models are accurate for the Postrera and Apante seasons; that predictions hold outside the area of applicability; that the maps were validated with new independent trials; that results for overall performance hold for single traits such as yield
relations:
  - extends: vanetten-2019-pnas  # pools the Nicaragua trials analysed there with trials from three more countries
---

## Questions this paper answers

- Can data from separate tricot trials, partners and seasons be combined into one analysis?
- How are environmental covariates selected and used to map variety performance?
- How do you predict planting dates for seasons and areas without trial data?
- Where are model predictions valid (area of applicability)?
- Which environmental factor drives common bean performance in Central America?
- Which bean genotypes are good candidates for testing or introduction in other Central American countries?

## Summary

The paper shows how to synthesize tricot data from heterogeneous sources into location-specific information for variety decisions. Rankings can be aggregated across trials without converting data from different scales or designs. The study pools 14 red common bean trials run between 2015 and 2018 by five organizations in Costa Rica, El Salvador, Honduras and Nicaragua, with 1,871 plots in total. Only the farmers' overall performance ranking was analyzed.

Genotype names were first translated into experimental line names. Genotypes tested in only one trial were then removed, which reduced the set from 27 to 17. The rankings were analyzed with Plackett-Luce trees, using spatially explicit climate and soil covariates. Forward selection with leave-one-trial-out cross-validation retained the warm spell duration index (WSDI), very heavy rain days (R20mm), the 10th percentile of night temperature and high-temperature stress at flowering. These covariates improved the cross-validated fit only slightly, and adding latitude and longitude made it worse. The pruned tree made a single split, on WSDI. Where warm spells lasted more than 4 days, IBC 308-24, MHC 2-13-49 and SX 14825-7-1 ranked highest, and BRT 103-182 went from good to poor. This matches knowledge that high temperature limits common bean.

To predict across the region, the authors needed planting dates for every grid cell and season. They modelled them with Cox survival models on rainfall and solar radiation, with season-specific start dates. The Primera model predicted well (c index 0.808), while the Postrera (0.563) and Apante (0.625) models were weak but better than a fixed planting date. Predictions for each cell of about 11 km, averaged over 2000 to 2019, produced maps of the top three genotypes per season, with entropy maps for uncertainty and an area of applicability flagging conditions not covered by the trials.

Seven genotypes make up the top three across seasons. The most reliable predictions, with the lowest entropy, are where SRC 2-18-1, SX 14825-7-1 and ALS 0532-6 form the top three. All three tolerate heat, and the last two also drought. Entropy is higher where a genotype tested in only one country enters the top three. EAP 9508-93, tested only in Honduras, is predicted in the top three in much of Costa Rica, which makes it a candidate for new trials there but not a direct recommendation. ALS 0532-6, tested in 10 of 14 trials, is a good candidate for introduction in Costa Rica, El Salvador and Nicaragua.

Pooling trials exploits a spread of locations and seasons that single trials cannot offer. The maps can help breeders target new testing locations and help extension agents make recommendations, while entropy and the area of applicability capture two kinds of uncertainty, in the rankings and in the environment. ClimMob's standardized data collection made the datasets compatible, though curation was still needed. A key challenge was that one variety carries different names in different countries, so the authors support coordinated regional releases and a shared database of harmonized names. They expect the method to apply to other crops and regions.

## Methods in brief

- **Data.** 14 tricot trials, 2015–2018, four countries, five organizations (INTA, UCR, CATIE, FIPAH, PRR), 14 to 714 plots per trial, 1,871 plots in total (sum of Table 1, card's own calculation, which matches the node sizes 1,264 + 607 in Figure 3). Farmers ranked the three genotypes on several traits, but only the overall performance ranking was analyzed.
- **Harmonization.** Variety names translated into experimental line names (Table 2). Genotypes tested in only one trial were removed, which reduced 27 genotypes to 17.
- **Model.** Plackett-Luce trees with forward covariate selection and blocked cross-validation.
- **Planting dates.** Cox models with time-dependent covariates, one per season, with observation starting 1 April (Primera), 1 August (Postrera) and 1 October (Apante). Final covariates: accumulated rainfall (Primera), daily rainfall and solar radiation (Postrera), daily rainfall (Apante).
- **Prediction.** Cell-wise node membership per season, top-three probability maps, normalized entropy, area of applicability.

## Stated limitations

- Planting-date models were weak for Postrera and Apante.
- Predictions are unreliable outside the area of applicability.
- Genotypes tested in only one country get higher-entropy predictions elsewhere, so the maps point to candidates for new trials, not direct recommendations.
- A single Plackett-Luce tree can be unstable. The authors chose it for interpretability and suggest ensembles (Plackett-Luce forests) for future work.
- The planting-date models are a first, ad hoc approximation. Start of the observation period, sample size and covariates need refinement.
- No environmental factor besides heat (WSDI) was identified. More covariates and interactions may be found with machine-learning methods.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 14 trials | tricot common bean trials pooled | This paper |
| 2015–2018 | Trial period | This paper |
| 4 countries | Costa Rica, El Salvador, Honduras, Nicaragua | This paper |
| 27 → 17 | Genotypes before and after removing those tested in only one trial (after name harmonization) | This paper |
| 14–714 | Plots per trial (Table 1) | This paper |
| 1,871 | Plots in total, sum of Table 1 (card's own calculation, matches Figure 3 node sizes 1,264 + 607) | This paper |
| > 4 days | WSDI split in the Plackett-Luce tree (p = 0.019), Node 2 n = 1,264 plots, Node 3 n = 607 plots | This paper |
| 6,183 vs 6,033 | Cross-validated deviance, no-covariate vs environmental-covariate model (pseudo-R2 0.6679 vs 0.6831, Kendall's W 0.5203 vs 0.5215) | This paper |
| r = 0.09 | Correlation between WSDI and maximum night temperature (p = 1 × 10−4) | This paper |
| 0.808 | c index, Primera planting-date model | This paper |
| 0.563 | c index, Postrera planting-date model | This paper |
| 0.625 | c index, Apante planting-date model | This paper |
| ~0.5% | Increase per mm of daily accumulated rainfall in the rate of planting, Primera (hazard ratio 1.005, see Notes) | This paper |
| 2000–2019 | Years over which seasonal predictions were averaged, on a grid of about 11 × 11 km | This paper |
| 10 of 14 | Trials that tested ALS 0532-6, the genotype with the most certain top-three predictions | This paper |

## Notes

- Heat as the main driver agrees with vanetten-2019-pnas, which found maximum night temperature most important in the Nicaragua trials, a subset of this dataset. In this paper WSDI and maximum night temperature correlate only weakly (r = 0.09, p. 2256).
- Areas outside the area of applicability are mostly unsuitable for beans, such as the Talamanca range and Indio Maíz reserve. The trials jointly cover most bean-growing conditions in Central America (p. 2258).
- Source issue: Table 9 shows that the Apante planting-date model also fails the proportional hazard test (p = .013), which the text does not discuss (p. 2258).
- Source issue: the ~0.5% per mm figure for Primera is a hazard ratio (1.005). The source describes it as a change in planting probability (p. 2256), but it is a change in the daily rate of planting.
- Source issue: the source defines WSDI as the longest warm spell in Table 3 (p. 2251) but as the number of days above the 90th percentile in the results (p. 2256). The tree split is at 4 days.
