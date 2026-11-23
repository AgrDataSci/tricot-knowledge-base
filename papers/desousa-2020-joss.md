---
id: desousa-2020-joss
title: chirps. API client for the CHIRPS precipitation data in R
authors: de Sousa K, Sparks AH, Ashmall W, van Etten J, Solberg SØ
year: 2020
journal: Journal of Open Source Software
journal_short: JOSS
article: 5(51), 2419
type: software paper
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.21105/joss.02419
open_copy: https://doi.org/10.21105/joss.02419
license: CC BY 4.0
data: example dataset tapajos ships with the package, code at https://github.com/ropensci/chirps (archive https://doi.org/10.5281/zenodo.3925143)
software: chirps, https://CRAN.R-project.org/package=chirps (v1.1 on CRAN, published 2025-11-24, now titled "API Client for CHIRPS and CHIRTS", checked 2026-10-30)
crops: none (climate data tool)
region: global (CHIRPS 50° S to 50° N, IMERG and ESI global), worked example in the Tapajós National Forest, Brazil
keywords: CHIRPS, rainfall, precipitation indices, IMERG, ESI, climate covariates, API client, R package, dry spell, environmental data for trials
gist: R package chirps retrieves CHIRPS, IMERG and ESI data for chosen points and dates through the ClimateSERV API and computes rainfall indices, shown in a Brazilian Amazon example
not_established: That CHIRPS indices match rainfall measured on individual farms; that the Tapajós example shows a statistically tested drying trend; that CHIRPS or the package was validated against station data in this paper; that chirps has been used in tricot trials (the paper does not mention tricot); that repeated calls return identical data over time
---

## Questions this paper answers

- How do I get rainfall data for my trial sites in R?
- Which precipitation indices can be computed for a growing season?
- What are the resolution and coverage of CHIRPS?
- Which R objects can I give chirps as input, and what does it return?

## Summary

chirps gives R users reproducible access to CHIRPS, the Climate Hazards Group's daily gridded rainfall dataset, and computes precipitation indices for chosen points and periods. CHIRPS blends satellite imagery at 0.05 arc-degree resolution with station data, covers latitudes 50° S to 50° N from 1981 to near present with about a 45-day lag, and is widely used for trend analysis and drought monitoring.

The package also provides API access to two related products. IMERG gives near-real-time global rainfall at 0.5 arc-degree resolution from 2015, useful for storm rainfall and flood impacts. The Evaporative Stress Index (ESI) gives weekly anomalies in evapotranspiration at 0.25 arc-degree resolution for the whole globe from 2001, estimated from satellite land surface temperature.

The package has four main functions. get_chirps(), get_imerg() and get_esi() retrieve data through the ClimateSERV API for a date range and for points given as a data frame of coordinates, an sf object or a geojson object. ClimateSERV accepts one polygon per request, so the package draws a small buffer around each point and sends it as a geojson polygon. Results come back as a data frame, or as sf or geojson on request. precip_indices() computes precipitation variability indices following Aguilar et al. 2005, such as total rainfall (Rtotal), maximum length of dry and wet spells (MLDS, MLWS) and maximum 5-day rainfall (Rx5day), optionally as a time series in fixed-length intervals.

The worked example takes 20 random points in the Tapajós National Forest, a protected area of about 527,400 ha in the Brazilian Amazon, retrieves about a decade of daily rainfall and computes indices in 30-day intervals. In this quick assessment the authors note longer dry spells, shorter wet spells, lower 30-day rainfall totals (below the long-term mean after 2014) and lower maximum 5-day rainfall. The trends are shown as loess curves on a plot, with no statistical test. The text, code and figure give different study periods (see Notes).

The authors point to applications in crop modelling and genotype-by-environment analysis. They cite Kehel et al. 2016, who used maximum dry-spell length to show how severe drought can affect wheat development and yield in CIMMYT international yield trials. Citing van Etten et al. 2019, they suggest that such indices can help improve variety recommendations for climate adaptation in marginal production environments.

The same indices have served to evaluate climate variability, in the first author's earlier work on farmers' adaptation decisions in Central America, and climate change at continental scale. CHIRPS had over 800 citations at the time, in agriculture, hydrological modelling, drought monitoring and disease control, for example malaria and diarrheal disease. The package builds on sf, crul and jsonlite, and aims to let researchers bring CHIRPS into a replicable and reproducible R workflow. Users should cite Funk et al. 2015 for CHIRPS, Huffman et al. 2014 for IMERG and SERVIR Global 2019a for ESI.

## Methods in brief

- **Data access.** get_chirps(), get_imerg() and get_esi() query the ClimateSERV API for a date range and for points given as data.frame, sf or geojson objects. Each point is buffered into a small polygon, as ClimateSERV accepts one polygon per request.
- **Indices.** precip_indices() computes precipitation variability indices (Aguilar et al. 2005), shown in the paper as MLDS, MLWS, Rtotal and Rx5day, optionally as a time series in fixed-length intervals.
- **Integration.** Built on sf, crul and jsonlite. Outputs are data frames of class chirps_df, or sf or geojson objects with as.sf = TRUE or as.geojson = TRUE.

## Stated limitations

- The paper states no limitations. The points below are the card's reading of the data descriptions on page 1.
- CHIRPS normally has about a 45-day lag, so it is not real-time.
- CHIRPS covers only 50° S to 50° N.
- Not discussed in the paper: indices come from gridded estimates, not from rain gauges on the farm.
- The worked-example trends are visual (loess curves) and not statistically tested.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 0.05 arc-degree | CHIRPS spatial resolution | Funk et al. 2015, cited in this paper |
| 1981 to near present | CHIRPS temporal coverage, about 45-day lag | Funk et al. 2015, cited in this paper |
| 50° S to 50° N | CHIRPS latitudinal coverage | Funk et al. 2015, cited in this paper |
| 0.5 arc-degree, from 2015 | IMERG resolution and coverage | Huffman et al. 2014, cited in this paper |
| 0.25 arc-degree, weekly | ESI resolution | Anderson et al. 2011, cited in this paper |
| 2001 to near present | ESI temporal coverage | This paper (data from SERVIR Global 2019a) |
| 20 random points | Sample points in the Tapajós worked example | This paper |
| ~527,400 ha | Area of the Tapajós National Forest | This paper |
| 30 days | Interval for the index time series in the example | This paper |
| over 800 | Citations of CHIRPS at the time of writing | This paper |

## Notes

- The current CRAN version (1.1) also covers CHIRTS temperature data, which the 2020 paper does not describe. Check the CRAN reference manual for current functions and whether IMERG and ESI are still supported.
- Rainfall indices from chirps are computed alongside temperature indices from climatrends (desousa-2023-joss).
- Outside this paper: in tricot analyses, chirps is used to supply rainfall covariates linked to each farm's coordinates and planting date, which can then enter Plackett-Luce trees (see vanetten-2019-pnas). The 2020 paper itself does not mention tricot or Plackett-Luce.
- Problem in the source: the worked-example period differs. The text says Jan 2008 to Dec 2018, the code requests 2008-01-01 to 2018-01-31, and the Figure 1 caption says Jan 2010 to Dec 2018. The plot axis starts in 2008 and ends near early 2018, so the code range is most likely the one used.
- Problem in the source: the Tapajós coordinates are printed with negative signs and E/S labels together. Read them as about 55.4° to 54.8° W and 4.1° to 2.7° S.
- Outside information, not from this paper: IMERG's native resolution is usually given as 0.1°, not 0.5° as stated in the paper. Check current IMERG and ClimateSERV documentation before quoting resolution or start year.
