---
id: desousa-2023-joss
title: Climate variability indices for ecological and crop models in R. The climatrends package
authors: de Sousa K, van Etten J, Neby M, Solberg SØ
year: 2023
journal: Journal of Open Source Software
journal_short: JOSS
article: 8(85), 4405
type: software paper
source: team
peer_reviewed: yes
curated_card: yes
doi: https://doi.org/10.21105/joss.04405
open_copy: https://doi.org/10.21105/joss.04405
license: CC BY 4.0
data: example dataset commonbean ships with the package (tricot trial in Nicaragua with MODIS temperature)
software: climatrends, https://CRAN.R-project.org/package=climatrends (v1.2 on CRAN, published 2025-11-21, checked 2026-10-30)
crops: common bean (example)
region: Nicaragua (example), global use
keywords: climatrends, temperature indices, precipitation indices, growing degree-days, evapotranspiration, late spring frost, crop-sensitive indices, R package, climate covariates
gist: R package that computes climate indices over each plot's growing period. Its tricot bean example in Nicaragua shows variety rankings splitting by summer days and night temperature
not_established: the 49 summer days and 18.7 °C splits are validated heat thresholds for common bean; hot days and warm nights act together in one tree node; the case study fully reproduces van Etten et al. 2019; the package chooses which indices suit a crop; MODIS land-surface temperature can replace air temperature without checking; the indices were validated in this paper
---

## Questions this paper answers

- How do I compute crop-relevant climate indices for each trial plot?
- Which temperature and rainfall indices does climatrends provide?
- How do I compute growing degree-days or reference evapotranspiration?
- How does climate explain variety rankings in a tricot trial?

## Summary

climatrends computes climate variability indices for ecological and crop models in a reproducible way. It grew out of scripts written for earlier studies, including van Etten et al. 2019, and was packaged so research groups across CGIAR and partners could run the same analyses on new data.

The package computes indices over a growing period defined per observation, for example from each farm's planting date over a set number of days. Its eight main functions cover temperature indices (such as maximum night temperature and summer days, the days above 30 °C), precipitation indices, cumulative dry and wet spells, crop-sensitive indices, growing degree-days (GDD), reference evapotranspiration with the Blaney-Criddle method (ETo) and the occurrence of late spring frost. Input can be local data as a vector, matrix or array, or sites in a data.frame or sf object, for which the package fetches data through the nasapower and chirps packages. The authors state it was the first R package for agroclimatic indices that handles site heterogeneity and time series (on CRAN since February 2020), and describe it as complementary to packages limited to degree-days or to zoning.

The case study reuses tricot data from van Etten et al. 2019, where 11 common bean varieties were tested in incomplete blocks of three (842 blocks) over five seasons from 2015 to 2017 in Nicaragua. With MODIS land-surface temperature, the authors use GDD() to count the days each plot needed to reach 900 degree-days from planting (54 to 100 days). For simplicity they average this per season and compute temperature indices over that seasonal span. The earlier study had retained only maximum night temperature (maxNT) through forward selection. Here the authors add summer days (SU) to show how a Plackett-Luce tree grows with more indices. The tree first splits at 49 summer days. In the branch with 49 or fewer summer days, it splits again at a maxNT of 18.7 °C. The authors read this as bean performance on farm being driven by hot days (which they equate with more than 70% of growing days) and warmer nights.

The authors frame the package around reproducibility, the ability to repeat an analysis, and replicability, the ability to repeat an experiment, which they see as a gap in most agricultural and ecological studies. Making the same indices available to all groups lets peers validate analyses and apply them to new data. Possible further development includes integration with other datasets through API client packages and new physiology-based indices. Integration with daily high-resolution climate data and seasonal forecasts for East Africa from Tomorrow.io's CBAM model is under development. The authors direct users to CRAN for the latest functions, since the package evolves.

For tricot users, the package turns each farm's location and planting date into comparable climate covariates, which Plackett-Luce trees can use to explain where varieties win or lose. The example data ship with the package, so the case study can be rerun, although the printed code may need updating for current package versions (see Notes).

## Methods in brief

- **Functions.** Eight main functions (Table 1): temperature(), rainfall(), cumdrought(), cumrain(), GDD(), ETo(), late_frost(), crop_sensitive(). Methods exist for numeric vectors, matrix or array, data.frame and sf (POINT or POLYGON). The data.frame and sf methods fetch data through nasapower and chirps.
- **Periods.** Each observation can have its own start date and span, matching plot-level planting dates.
- **Example.** commonbean data with MODIS temperature. GDD() with 900 degree-days (de Medeiros et al. 2016) gives the days from planting to maturity, averaged per season. temperature() computes indices over that span. pltree() from PlackettLuce fits a tree on maxNT and SU with minsize = 50.

## Stated limitations

- For simplicity, the case study computes temperature indices over the season-average crop cycle, not each plot's own cycle.
- The case study only partly reproduces van Etten et al. 2019, with a slightly different approach (degree-days from planting to maturity, and new indices).
- Summer days were added to show how Plackett-Luce trees grow in complexity, not chosen by variable selection. The earlier forward selection retained only maxNT.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 11 varieties, 842 blocks | Common bean tricot trial in Nicaragua, five seasons from 2015 to 2017, reused in the case study | van Etten et al. 2019, cited in this paper |
| 900 degree-days | Planting to maturity for common bean, used in GDD() | de Medeiros et al. 2016, cited in this paper |
| 54 to 100 days | Days needed to reach 900 degree-days across plots (Fig. 1a) | This paper |
| 49 summer days | First split in the Plackett-Luce tree (SU, days above 30 °C). The authors equate it with more than 70% of growing days | This paper |
| 18.7 °C (18.68 in Fig. 1c) | Maximum night temperature split, only in the branch with 49 or fewer summer days | This paper |
| 8 | Main functions in the package (Table 1) | This paper |

## Notes

- Outside information, not from the paper: function names and arguments have changed across versions. Check the current CRAN reference manual before reusing code from the paper. The CRAN version in the software field was also checked outside the paper.
- Card's own observations, not stated by the authors: the example uses MODIS land-surface temperature, not air temperature. The package computes indices but does not choose which ones suit a crop or question. The paper names only a few indices and refers to the package documentation for the full list.
- The 18.7 °C night temperature threshold matches vanetten-2019-pnas.
- Problem in the source: the authors' reading (hot days and warmer nights) does not match the tree structure. Fig. 1c splits first at 49 summer days, and the 18.7 °C night split appears only in the branch with 49 or fewer summer days.
- Problem in the source: the ">70% of growing days" equals 49 summer days only for a 70-day cycle (card's own calculation). Over the 54 to 100 day range in Fig. 1a it would be 49% to 91%.
- Problem in the source: the printed code uses %<>% from magrittr without loading magrittr. Add library("magrittr") or use cbean <- cbean %>% ... when rerunning.
- Problem in the source: the Fig. 1a axis reads "GDD" but the values are days (54 to 100), as the caption says.
- To check across cards: this paper dates the Nicaragua trial to five seasons from 2015 to 2017 (p. 2), while vanetten-2019-pnas gives 2012 to 2016.
