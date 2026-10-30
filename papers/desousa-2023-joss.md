---
id: desousa-2023-joss
title: Climate variability indices for ecological and crop models in R. The climatrends package
authors: de Sousa K, van Etten J, Neby M, Solberg SØ
year: 2023
journal: Journal of Open Source Software
journal_short: JOSS
article: 8(85), 4405
type: software paper
doi: https://doi.org/10.21105/joss.04405
open_copy: https://doi.org/10.21105/joss.04405
license: CC BY 4.0
data: example dataset commonbean ships with the package (tricot trial in Nicaragua with MODIS temperature)
software: climatrends, https://CRAN.R-project.org/package=climatrends (v1.2 on CRAN, published 2025-11-21, checked 2026-10-30)
crops: common bean (example)
region: Nicaragua (example), global use
keywords: climatrends, temperature indices, precipitation indices, growing degree-days, evapotranspiration, late spring frost, crop-sensitive indices, R package, climate covariates
gist: R package computing temperature, rainfall, degree-day, evapotranspiration and frost indices for trial sites, used to explain tricot rankings with climate
---

## Questions this paper answers

- How do I compute crop-relevant climate indices for each trial plot?
- Which temperature and rainfall indices does climatrends provide?
- How do I compute growing degree-days or reference evapotranspiration?
- How does climate explain variety rankings in a tricot trial?

## Summary

climatrends computes climate variability indices for ecological and crop models in a reproducible way. It grew out of scripts written for earlier studies, including van Etten et al. 2019, and was packaged so research groups across CGIAR and partners could run the same analyses on new data.

The package computes indices over a growing period defined per observation, for example from each farm's planting date over a set number of days. It covers temperature indices (such as maximum day and night temperature, diurnal range, summer days, tropical nights and cold or warm spells), precipitation indices (such as total rainfall, dry and wet spells and rainy days), growing degree-days (GDD), reference evapotranspiration with the Blaney-Criddle method (ETo) and the occurrence of late spring frost. Input can be local data or remote sources through packages such as chirps and nasapower. The authors describe it as complementary to packages limited to degree-days or to zoning.

The case study reuses tricot data from van Etten et al. 2019, where 11 common bean varieties were tested in incomplete blocks of three across 842 farms in Nicaragua. With MODIS land-surface temperature, the authors compute degree-days to estimate each plot's crop cycle and then temperature indices over that cycle. A Plackett-Luce tree splits the data by summer days (day temperature above 30 °C) and maximum night temperature. Variety performance shifts where more than 70% of growing days exceed 30 °C and night temperatures are above 18.7 °C, pointing to heat accumulation and warm nights as drivers of on-farm bean performance.

The authors plan further development to add indices and data sources as user needs evolve.

The authors frame the package around reproducibility, the ability to repeat an analysis, and replicability, the ability to repeat an experiment, which they see as a gap in most agricultural and ecological studies. Making the same indices available to all groups lets peers validate analyses and apply them to new data. Planned development includes integration with other datasets through API client packages, new physiology-based indices, and daily high-resolution climate data and seasonal forecasts for East Africa from Tomorrow.io's CBAM model. The authors direct users to CRAN for the latest functions, since the package evolves.

For tricot users, the package turns each farm's coordinates and planting date into comparable climate covariates, which is the input Plackett-Luce trees need to explain where varieties win or lose. The example data ship with the package, so the case study can be rerun directly.

## Methods in brief

- **Functions.** temperature(), rainfall(), GDD(), ETo(), late_frost(), crop_sensitive().
- **Periods.** Each observation can have its own start date and span, matching plot-level planting dates.
- **Example.** commonbean data with MODIS temperature, GDD to set the crop cycle, temperature indices per season, and a Plackett-Luce tree with PlackettLuce.

## Stated limitations

- The example uses land-surface temperature rather than air temperature.
- Index choice depends on the crop and question. The package computes indices but does not select them.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 11 varieties, 842 blocks | Common bean tricot trial reused in the case study | van Etten et al. 2019, cited in this paper |
| >30 °C on >70% of days | Summer-day split in the Plackett-Luce tree | This paper |
| >18.7 °C | Maximum night temperature split in the tree | This paper |

## Notes

- Function names and arguments have changed across versions. Check the current CRAN reference manual before reusing code from the paper.
- The 18.7 °C night temperature threshold matches vanetten-2019-pnas.
