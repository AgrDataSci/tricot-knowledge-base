---
id: desousa-2020-joss
title: chirps. API client for the CHIRPS precipitation data in R
authors: de Sousa K, Sparks AH, Ashmall W, van Etten J, Solberg SØ
year: 2020
journal: Journal of Open Source Software
journal_short: JOSS
article: 5(51), 2419
type: software paper
doi: https://doi.org/10.21105/joss.02419
open_copy: https://doi.org/10.21105/joss.02419
license: CC BY 4.0
data: example dataset tapajos ships with the package
software: chirps, https://CRAN.R-project.org/package=chirps (v1.1 on CRAN, published 2025-11-24, now titled "API Client for CHIRPS and CHIRTS", checked 2026-10-30)
crops: none (climate data tool)
region: global, 50° S to 50° N
keywords: CHIRPS, rainfall, precipitation indices, IMERG, ESI, climate covariates, API client, R package, dry spell, environmental data for trials
gist: R client for CHIRPS daily rainfall (plus IMERG and ESI) that computes precipitation indices for trial locations and dates, a standard source of rainfall covariates for tricot
---

## Questions this paper answers

- How do I get rainfall data for my trial sites in R?
- Which precipitation indices can be computed for a growing season?
- What are the resolution and coverage of CHIRPS?
- How are rainfall covariates used in variety recommendation?

## Summary

chirps gives R users reproducible access to CHIRPS, the Climate Hazards Group's daily gridded rainfall dataset, and computes precipitation indices for chosen points and periods. CHIRPS blends satellite imagery at 0.05 arc-degree resolution with station data, covers latitudes 50° S to 50° N from 1981 to near present with about a 45-day lag, and is widely used for trend analysis and drought monitoring.

The package also provides API access to two related products. IMERG gives near-real-time global rainfall at 0.5 arc-degree resolution from 2015, useful for storm rainfall and flood impacts. The Evaporative Stress Index (ESI) gives weekly anomalies in evapotranspiration at 0.25 arc-degree resolution, a proxy for agricultural drought.

The main functions retrieve data for a set of coordinates and dates (get_chirps, get_imerg, get_esi) and compute indices such as total rainfall, maximum length of dry and wet spells, number of rainy days and extreme-rainfall measures (precip_indices), either for the whole period or in fixed-length intervals. The worked example samples 20 points in the Tapajós region of the Brazilian Amazon, retrieves ten years of daily rainfall and computes indices in 30-day intervals.

The authors point to applications in crop modelling and genotype-by-environment analysis, where indices such as maximum dry-spell length explain variety performance, and to improving variety recommendations for climate adaptation in marginal environments, as in van Etten et al. 2019. In the tricot workflow, chirps supplies rainfall covariates linked to each farm's coordinates and planting date, which then enter Plackett-Luce trees.

The paper situates the package within a wider set of uses for gridded rainfall indices. Beyond agronomy, rainfall records have been linked to public-health outcomes such as diarrheal disease, and the authors' own earlier work used climate data to study how climate awareness shapes farmers' adaptation decisions in Central America. In plant breeding, indices such as the maximum length of dry spell have explained wheat performance across decades of international yield trials. The package builds on established R infrastructure for spatial data (sf), web requests and JSON handling, so outputs fit standard workflows. For tricot users, the practical value is reproducibility. The same function call retrieves the same rainfall series for every farm and planting date, which lets different teams compute comparable covariates for Plackett-Luce trees across trials, countries and years, and makes analyses easier to repeat and audit. It is one of several open-source tools the team built to make tricot analyses reproducible across trials and partners.

## Methods in brief

- **Data access.** API clients for CHIRPS , IMERG and ESI, taking point or polygon geometries and a date range.
- **Indices.** precip_indices() for rainfall totals, spell lengths and rainy days, with optional time series in fixed intervals.
- **Integration.** Works with sf objects and tidyverse workflows.

## Stated limitations

- CHIRPS has about a 45-day lag, so it is not real-time.
- Coverage is limited to 50° S to 50° N.
- Indices are computed from gridded estimates, not station observations at the farm.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 0.05 arc-degree | CHIRPS spatial resolution | Funk et al. 2015, cited in this paper |
| 1981 to near present | CHIRPS temporal coverage, about 45-day lag | Funk et al. 2015, cited in this paper |
| 50° S to 50° N | CHIRPS latitudinal coverage | Funk et al. 2015, cited in this paper |
| 0.5 arc-degree, from 2015 | IMERG resolution and coverage | Huffman et al. 2014, cited in this paper |
| 0.25 arc-degree, weekly | ESI resolution | Anderson et al. 2011, cited in this paper |

## Notes

- The current CRAN version (1.1) also covers CHIRTS temperature data, which the 2020 paper does not describe. Check the CRAN reference manual for current functions and whether IMERG and ESI are still supported.
- Rainfall indices from chirps are computed alongside temperature indices from climatrends (desousa-2023-joss).
