---
id: brown-2022-cropsci
title: Rank-based data synthesis of common bean on-farm trials across four Central American countries
authors: Brown D, Barrios M, de Bruin S, Chaves N, Machida L, Pavón M, de Sousa K, Gómez M, Madriz B, Rosas JC, Suchini JG, Zelaya V, Aguilar A, Hernández JC, Mejía P, van Etten J, and co-authors
year: 2022
journal: Crop Science
journal_short: Crop Sci
article: 62(6), 2246-2266
type: research article
doi: https://doi.org/10.1002/csc2.20817
open_copy: https://doi.org/10.1002/csc2.20817
license: CC BY
data: see the data availability statement in the article
software: PlackettLuce, gosset
crops: common bean
region: Costa Rica, El Salvador, Honduras, Nicaragua
keywords: data synthesis, rank aggregation, meta-analysis, Plackett-Luce trees, environmental covariates, WSDI, heat, planting date, survival analysis, area of applicability, variety maps
gist: Pools 14 tricot common bean trials from four Central American countries into one Plackett-Luce analysis, finding heat the main driver and mapping variety performance by season
---

## Questions this paper answers

- Can data from separate tricot trials, partners and seasons be combined into one analysis?
- How are environmental covariates selected and used to map variety performance?
- How do you predict planting dates for seasons and areas without trial data?
- Where are model predictions valid (area of applicability)?
- Which environmental factor drives common bean performance in Central America?

## Summary

The paper shows how to synthesize tricot data from heterogeneous sources into location-specific information for variety decisions. Individual on-farm trials are expensive and local, but ranking data can be aggregated across trials without the scaling problems of yield data from different designs. The study pools 14 common bean trials run between 2015 and 2018 by several organizations in Costa Rica, El Salvador, Honduras and Nicaragua.

Harmonizing genotype names reduced the set from 27 to 17 genotypes. The combined rankings were analyzed with a Plackett-Luce model and model-based recursive partitioning using spatially explicit covariates for climate, soil and elevation. Forward selection retained the warm spell duration index (WSDI), heavy-rain days (R20mm), a low-temperature percentile and a height-related term, and the tree split first on WSDI. This matches knowledge that high temperature limits common bean, and heat- and drought-tolerant genotypes such as ALS 0532-6, SX 14825-7-1 and SRC 2-18-1 performed better under warmer conditions.

To predict across the region, the authors needed planting dates for every grid cell and season, so they modelled them with survival (Cox) analysis on rainfall, with season-specific start dates for Primera, Postrera and Apante. The Primera model predicted well (c index 0.808), while Postrera and Apante models were weaker (0.563). Predicted node membership for each cell and season produced maps of the top three genotypes, with entropy maps showing uncertainty, and an area-of-applicability analysis flagging regions with conditions not covered by the trials.

Maps show broad regional patterns, such as SRC 2-18-1 in the top three across most of the region except much of Costa Rica, and season-specific shifts. Some genotypes, such as EAP 9508-93 released in Honduras as Cedrón, appear only where they were tested. The authors conclude that rank-based synthesis can turn scattered tricot trials into variety recommendation maps and support release decisions, provided users respect the area of applicability.

Pooling trials let the analysis exploit the spread of locations and seasons that single trials cannot offer. The resulting maps can help breeding programmes target new testing locations and help extension agents generate recommendations, while entropy and the area of applicability quantify two separate kinds of uncertainty, in the rankings and in the environmental conditions. ClimMob's standardized data collection makes such synthesis feasible. The main obstacle was that the same released variety carried different names in different countries, so the authors call for coordinated regional naming of varieties to ease future synthesis, which they expect to apply to other crops and regions.

## Methods in brief

- **Data.** 14 tricot trials, 2015–2018, four countries, several partners (INTA, UCR, CATIE, FIPAH, PRR), trial sizes from 17 to 714 participants.
- **Harmonization.** Genotype names standardized, 27 reduced to 17.
- **Model.** Plackett-Luce trees with forward covariate selection and blocked cross-validation.
- **Planting dates.** Cox survival models of planting probability against daily accumulated precipitation.
- **Prediction.** Cell-wise node membership per season, top-three probability maps, normalized entropy, area of applicability.

## Stated limitations

- Planting-date models were weak for Postrera and Apante.
- Predictions are unreliable outside the area of applicability.
- Genotypes tested in only one country cannot be generalized across the region.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 14 trials | Tricot common bean trials pooled | This paper |
| 2015–2018 | Trial period | This paper |
| 4 countries | Costa Rica, El Salvador, Honduras, Nicaragua | This paper |
| 27 → 17 | Genotypes after name harmonization | This paper |
| 17–714 | Participants per trial | This paper |
| 0.808 | c index, Primera planting-date model | This paper |
| 0.563 | c index, Postrera and Apante planting-date models | This paper |
| ~0.5% | Increase in planting probability per mm of daily accumulated rainfall, Primera | This paper |

## Notes

- Heat as the main driver is consistent with the night-temperature thresholds in vanetten-2019-pnas.
- The author list in the PDF is long. Check the full list before citing.
