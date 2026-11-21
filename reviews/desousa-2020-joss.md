# Card review: desousa-2020-joss

- **Card:** papers/desousa-2020-joss.md
- **Source:** papers-pdf/de-sousa-et-al-2020.pdf (5 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 41 |
| Supported | 23 |
| Imprecise | 11 |
| Not in source | 7 (2 of them are acceptable outside information in Notes, not counted as errors) |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 4 |
| Metadata issues | 4 |

The card describes the software correctly and the Key numbers are all supported. The main problem is that the gist and about one quarter of the Summary present tricot uses (covariates for Plackett-Luce trees, reproducibility across tricot trials, "a standard source of rainfall covariates for tricot") as if the paper said them. The 2020 paper never mentions tricot or Plackett-Luce. This outside knowledge must move to Notes, and the freed space should hold what the paper does report: the worked-example results, the ClimateSERV input logic and the citation guidance. Printed page numbers match PDF page numbers in this file.

## Fixes needed

1. **Outside tricot knowledge in the gist.** The card says chirps is "a standard source of rainfall covariates for tricot". The paper does not mention tricot (pages 1 to 5). Replace the gist with:

   `gist: R package chirps retrieves CHIRPS, IMERG and ESI data for chosen points and dates through the ClimateSERV API and computes rainfall indices, shown in a Brazilian Amazon example`

   (28 words)

2. **Outside tricot knowledge in the Summary (paragraphs 4 and 5).** These sentences are not in the source: "In the tricot workflow, chirps supplies rainfall covariates ... Plackett-Luce trees", "For tricot users, the practical value is reproducibility", "The same function call retrieves the same rainfall series ... easier to repeat and audit", and "It is one of several open-source tools the team built ...". The paper only says the package aims at a replicable and reproducible R workflow (pages 1 and 3 to 4). Removing them takes the Summary below 400 words, so replace the whole Summary with the text below (470 words). It keeps the card's first two paragraphs, fixes items 3 to 6, and adds the missing results.

   ```
   chirps gives R users reproducible access to CHIRPS, the Climate Hazards Group's daily gridded rainfall dataset, and computes precipitation indices for chosen points and periods. CHIRPS blends satellite imagery at 0.05 arc-degree resolution with station data, covers latitudes 50° S to 50° N from 1981 to near present with about a 45-day lag, and is widely used for trend analysis and drought monitoring.

   The package also provides API access to two related products. IMERG gives near-real-time global rainfall at 0.5 arc-degree resolution from 2015, useful for storm rainfall and flood impacts. The Evaporative Stress Index (ESI) gives weekly anomalies in evapotranspiration at 0.25 arc-degree resolution for the whole globe from 2001, estimated from satellite land surface temperature.

   The package has four main functions. get_chirps(), get_imerg() and get_esi() retrieve data through the ClimateSERV API for a date range and for points given as a data frame of coordinates, an sf object or a geojson object. ClimateSERV accepts one polygon per request, so the package draws a small buffer around each point and sends it as a geojson polygon. Results come back as a data frame, or as sf or geojson on request. precip_indices() computes precipitation variability indices following Aguilar et al. 2005, such as total rainfall (Rtotal), maximum length of dry and wet spells (MLDS, MLWS) and maximum 5-day rainfall (Rx5day), optionally as a time series in fixed-length intervals.

   The worked example takes 20 random points in the Tapajós National Forest, a protected area of about 527,400 ha in the Brazilian Amazon, retrieves about a decade of daily rainfall and computes indices in 30-day intervals. In this quick assessment the authors note longer dry spells, shorter wet spells, lower 30-day rainfall totals (below the long-term mean after 2014) and lower maximum 5-day rainfall. These trends are loess curves on a plot, with no statistical test. The text, code and figure give different study periods (see Notes).

   The authors point to applications in crop modelling and genotype-by-environment analysis. They cite Kehel et al. 2016, who used maximum dry-spell length to show how severe drought can affect wheat development and yield in CIMMYT international yield trials. Citing van Etten et al. 2019, they suggest that such indices can help improve variety recommendations for climate adaptation in marginal production environments.

   The same indices have served to evaluate climate variability, in the first author's earlier work on farmers' adaptation decisions in Central America, and climate change at continental scale. CHIRPS had over 800 citations at the time, in agriculture, hydrological modelling, drought monitoring and disease control, for example malaria and diarrheal disease. The package builds on sf, crul and jsonlite, and aims to let researchers bring CHIRPS into a replicable and reproducible R workflow. Users should cite Funk et al. 2015 for CHIRPS, Huffman et al. 2014 for IMERG and SERVIR Global 2019a for ESI.
   ```

   Then add this to Notes:

   `- Outside this paper: in tricot analyses, chirps is used to supply rainfall covariates linked to each farm's coordinates and planting date, which can then enter Plackett-Luce trees (see vanetten-2019-pnas). The 2020 paper itself does not mention tricot or Plackett-Luce.`

3. **Study period of the worked example (Summary paragraph 3).** The card says "ten years of daily rainfall". The source gives three periods: the text says Jan 2008 to Dec 2018, the code requests 2008-01-01 to 2018-01-31, and the Figure 1 caption says 01-Jan-2010 to 31-Dec-2018 (pages 2 and 3). The plotted axis runs from 2008 to about early 2018, which matches the code. "About a decade" is safe. The replacement Summary uses it. Add the Note given under Source issues.

4. **"number of rainy days" (Summary paragraph 3 and Methods bullet 2).** The source names only four indices: MLDS, MLWS, Rtotal and Rx5day (page 3, Figure 1 caption). It does not mention rainy days, and it does not say indices can be computed for the whole period. Replace the Methods bullet with:

   `- **Indices.** precip_indices() computes precipitation variability indices (Aguilar et al. 2005), shown in the paper as MLDS, MLWS, Rtotal and Rx5day, optionally as a time series in fixed-length intervals.`

5. **Stated limitations section.** The paper states no limitations. The 45-day lag and the 50° S to 50° N range are data descriptions (page 1), and the point about gridded estimates versus farm stations is not in the source. Replace the section with:

   ```
   - The paper states no limitations. The points below are the card's reading of the data descriptions on page 1.
   - CHIRPS normally has about a 45-day lag, so it is not real-time.
   - CHIRPS covers only 50° S to 50° N.
   - Not discussed in the paper: indices come from gridded estimates, not from rain gauges on the farm.
   - The worked-example trends are visual (loess curves) and not statistically tested.
   ```

6. **Data access bullet (Methods bullet 1).** The card says the clients take "point or polygon geometries". The source describes point inputs (data.frame, sf, geojson) that the package buffers into one polygon per ClimateSERV request (pages 1 to 2). It does not say users can supply their own polygons. There is also a stray space before the comma. Replace with:

   `- **Data access.** get_chirps(), get_imerg() and get_esi() query the ClimateSERV API for a date range and for points given as data.frame, sf or geojson objects. Each point is buffered into a small polygon, as ClimateSERV accepts one polygon per request.`

7. **Integration bullet (Methods bullet 3).** tidyverse is used only to draw the example figure (page 2). The package itself uses sf, crul and jsonlite, and can return sf or geojson. Replace with:

   `- **Integration.** Built on sf, crul and jsonlite. Outputs are data frames of class chirps_df, or sf or geojson objects with as.sf = TRUE or as.geojson = TRUE.`

8. **ESI as "a proxy for agricultural drought" (Summary paragraph 2).** The source does not say this. It says ESI describes anomalies in evapotranspiration, is based on land surface temperature, is global and runs from 2001 (page 1). The replacement Summary uses the source wording.

9. **Add not_established** (missing):

   `not_established: That CHIRPS indices match rainfall measured on individual farms; that the Tapajós example shows a statistically tested drying trend; that CHIRPS or the package was validated against station data in this paper; that chirps has been used in tricot trials (the paper does not mention tricot); that repeated calls return identical data over time`

10. **data field.** The PDF links the code repository and archive in the page 1 margin. Replace with:

    `data: example dataset tapajos ships with the package, code at https://github.com/ropensci/chirps (archive https://doi.org/10.5281/zenodo.3925143)`

11. **region field.** Replace with:

    `region: global (CHIRPS 50° S to 50° N, IMERG and ESI global), worked example in the Tapajós National Forest, Brazil`

12. **Key numbers (optional additions).**

    ```
    | 20 random points | Sample points in the Tapajós worked example | This paper |
    | ~527,400 ha | Area of the Tapajós National Forest | This paper |
    | 30 days | Interval for the index time series in the example | This paper |
    | 2001 to near present | ESI temporal coverage | This paper (data from SERVIR Global 2019a) |
    | over 800 | Citations of CHIRPS at the time of writing | This paper |
    ```

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | chirps. API client for the CHIRPS precipitation data in R | "chirps: API Client for the CHIRPS Precipitation Data in R" (p1) | Supported (colon to period is expected. Sentence case differs from the printed title case, so quote exactly if house style allows) |
| authors | de Sousa K, Sparks AH, Ashmall W, van Etten J, Solberg SØ | Same five authors in this order (p1) | Supported (the automated flag on SØ is only the special character) |
| year | 2020 | Published 01 July 2020 (p1) | Supported |
| journal | Journal of Open Source Software | Footer (p1 to p5) | Supported |
| article | 5(51), 2419 | Footer (p1) | Supported |
| type | software paper | JOSS software paper (p1) | Supported |
| doi | https://doi.org/10.21105/joss.02419 | p1 | Supported |
| license | CC BY 4.0 | Margin note (p1) | Supported |
| data | example dataset tapajos ships with the package | data("tapajos", package = "chirps") (p2). Repository and Zenodo archive linked (p1 margin) | Imprecise (code location missing, see fix 10) |
| software | CRAN v1.1, CHIRTS title, checked 2026-10-30 | Not in the 2020 paper | Not in source (outside information), not counted as error |
| crops | none (climate data tool) | No crop studied. Wheat appears only in a citation (p3) | Supported |
| region | global, 50° S to 50° N | CHIRPS 50° S to 50° N, IMERG and ESI global, example in Brazil (p1, p2) | Imprecise (see fix 11) |
| gist | ... a standard source of rainfall covariates for tricot | tricot not mentioned anywhere (p1 to p5) | Imprecise (outside claim, see fix 1) |
| not_established | missing | | Missing (see fix 9) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1-12 | Frontmatter | title to gist | 9 Supported, 3 Imprecise | See Metadata check | data, region, gist imprecise |
| 13 | Summary | chirps gives reproducible R access to CHIRPS daily gridded rainfall and computes indices for points and periods | Supported | p1, p2 | |
| 14 | Summary | CHIRPS 0.05 arc-degree satellite plus station data, 50° S to 50° N, 1981 to near present, ~45-day lag, used for trends and drought monitoring | Supported | p1, "over 800 citations" p3 | |
| 15 | Summary | IMERG near-real-time global, 0.5 arc-degree, from 2015, storm rainfall and flood impacts | Supported | p1 | See Source issues on IMERG resolution |
| 16 | Summary | ESI weekly ET anomalies, 0.25 arc-degree, proxy for agricultural drought | Imprecise | p1 | Drought proxy not stated. Global coverage and 2001 start omitted |
| 17 | Summary | get_chirps/get_imerg/get_esi for coordinates and dates. precip_indices gives totals, dry and wet spells, rainy days, extremes, whole period or intervals | Imprecise | p1 to p3 | Rainy days and whole-period option not in source |
| 18 | Summary | Example: 20 points, Tapajós region, ten years, 30-day intervals | Imprecise | p2, p3 | It is the Tapajós National Forest. Period differs between text, code and caption |
| 19 | Summary | Applications in crop modelling and GxE, MLDS explains performance, variety recommendations as in van Etten 2019 | Supported | p3 | Source wording is "can affect" and "can also be useful" |
| 20 | Summary | In the tricot workflow chirps supplies covariates for Plackett-Luce trees | Not in source | p1 to p5 | Outside knowledge. Move to Notes |
| 21 | Summary | Paper situates the package within wider uses | Supported | p3 | |
| 22 | Summary | Rainfall linked to public health such as diarrheal disease | Supported | p3, Horn et al. 2018 reference p4 | Malaria (Thomson 2017) also cited |
| 23 | Summary | Authors' earlier work used climate data to study climate awareness and adaptation in Central America | Imprecise | p3, reference p4 | Source cites it as evidence that CHIRPS-type indices evaluate climate variability. Card paraphrases the reference title instead |
| 24 | Summary | In plant breeding, MLDS explained wheat performance across decades of international yield trials | Imprecise | p3, reference p4 | Source says "In crop modelling", and drought "can affect" yield. Kehel et al. 2016 not named. Repeats claim 19 |
| 25 | Summary | Builds on sf, web requests and JSON handling, outputs fit standard workflows | Supported | p1, p2 | sf, crul, jsonlite |
| 26 | Summary | For tricot users the value is reproducibility | Not in source | | tricot not mentioned |
| 27 | Summary | Same call returns same series for every farm, comparable covariates across trials, countries, years | Not in source | | Outside knowledge and stronger than the source |
| 28 | Summary | One of several open-source tools the team built for tricot | Not in source | | Outside knowledge |
| 29 | Methods | API clients take point or polygon geometries and a date range | Imprecise | p1, p2 | Inputs are points that are buffered into polygons |
| 30 | Methods | precip_indices for totals, spell lengths, rainy days, optional intervals | Imprecise | p2, p3 | Rainy days not in source |
| 31 | Methods | Works with sf and tidyverse workflows | Imprecise | p1, p2 | tidyverse only used for the figure |
| 32 | Limitations | ~45-day lag, not real-time | Supported | p1 | Data description, not a limitation stated by the authors |
| 33 | Limitations | Coverage 50° S to 50° N | Supported | p1 | Same comment |
| 34 | Limitations | Indices from gridded estimates, not farm stations | Not in source | | Reasonable, but the card's own point |
| 35 | Key numbers | 0.05 arc-degree, Funk et al. 2015 | Supported | p1 | |
| 36 | Key numbers | 1981 to near present, ~45-day lag, Funk et al. 2015 | Supported | p1 | |
| 37 | Key numbers | 50° S to 50° N, Funk et al. 2015 | Supported | p1 | |
| 38 | Key numbers | IMERG 0.5 arc-degree from 2015, Huffman et al. 2014 | Supported | p1 | Matches source. See Source issues |
| 39 | Key numbers | ESI 0.25 arc-degree weekly, Anderson et al. 2011 | Supported | p1 | |
| 40 | Notes | CRAN v1.1 covers CHIRTS, not described in 2020 paper | Not in source (outside information) | | Correctly placed in Notes. Not counted as error. The part "the 2020 paper does not describe" CHIRTS is true |
| 41 | Notes | chirps rainfall indices computed alongside climatrends temperature indices | Not in source (outside information) | | Acceptable cross-reference in Notes. Not counted as error |

No derived numbers in the card need recomputing. Check of the example period: the text range (Jan 2008 to Dec 2018) is 11 years, the code range (2008-01-01 to 2018-01-31) is 10 years and 1 month, and the caption range (Jan 2010 to Dec 2018) is 9 years.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Study period differs: text Jan 2008 to Dec 2018, code 2008-01-01 to 2018-01-31, caption 01-Jan-2010 to 31-Dec-2018. The plotted axis runs 2008 to about early 2018 (read off the chart, approximate) | p2, p3 | No | `- The worked-example period differs in the source: the text says Jan 2008 to Dec 2018, the code requests 2008-01-01 to 2018-01-31, and the Figure 1 caption says Jan 2010 to Dec 2018. The plot axis starts in 2008, so the code range is most likely the one used.` |
| Coordinates given as "-55.4° and -54.8° E and -4.1° and -2.7° S", a double negative. Should read about 55.4° to 54.8° W and 4.1° to 2.7° S | p2 | No | `- The source gives the Tapajós coordinates with negative signs and E/S labels together. Read them as about 55.4° to 54.8° W and 4.1° to 2.7° S.` |
| Default buffer given as "0.0001 arc-sec", which is a few millimetres. The unit is probably arc-degrees | p1 | No | Low importance. No note needed unless the card cites the buffer |
| IMERG described as 0.5 arc-degree, daily, from 2015. Outside information (not checked against this PDF): IMERG's native grid is 0.1°, and the record now starts in 2000. The 2015 start may reflect what ClimateSERV served in 2020 | p1 | No | `- Outside information: IMERG's native resolution is 0.1°, not 0.5° as stated in the paper. Check current IMERG and ClimateSERV documentation before quoting resolution or start year.` |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: reproducible, replicable R workflow for CHIRPS | Yes | | |
| Design: four functions, ClimateSERV API, input classes, buffered polygons, output classes | Partly | Medium | Fix 2 (paragraph 3) and fixes 6 and 7 |
| Worked example: 20 random points, ~527,400 ha protected forest, 30-day intervals | Partly | Medium | Fix 2 (paragraph 4), fix 12 |
| Example results: longer dry spells, shorter wet spells, Rtotal below mean after 2014, lower Rx5day, a "quick assessment" with loess curves | No | Medium | Fix 2 (paragraph 4) |
| ESI coverage: global, from 2001, based on land surface temperature | No | Low | Fix 2 (paragraph 2), fix 12 |
| Citation guidance: cite Funk 2015, Huffman 2014, SERVIR Global 2019a | No | Medium (practical for users) | Fix 2 (paragraph 6) |
| CHIRPS over 800 citations, uses in agriculture, hydrology, drought, disease control (malaria, diarrhea) | Partly | Low | Fix 2 (paragraph 6) |
| Applications: Kehel et al. 2016 wheat and MLDS, van Etten et al. 2019 variety recommendation | Yes | | Name Kehel et al. 2016 (fix 2) |
| Code repository and archive | No | Medium | Fix 10 |
| Authors' stated limitations | None stated, card implies they are | Medium | Fix 5 |
| Funding (Nordic Joint Committee for Agricultural and Food Research) and origin in an NHH spatial-data course | No | Low | Optional |
| What a tricot user would ask: does the paper test chirps in tricot trials? | Card implies yes | High | It does not. Fixes 1, 2 and 9 |

## Template compliance

- Summary word count: 400 (at the lower limit). After removing the outside sentences it would fall below 400. The replacement in fix 2 has 470 words.
- Gist: 27 words (under 30), but it lists a use instead of what the paper shows. The replacement has 28 words.
- Keywords: 10 (within 8 to 12).
- Questions: 4 (within 4 to 7). The fourth question ("How are rainfall covariates used in variety recommendation?") is only lightly answered by the source (one sentence citing van Etten et al. 2019). Suggest replacing it with "Which R objects can I give chirps as input, and what does it return?"
- not_established: missing (fix 9).
- House style: tricot written lowercase throughout. maniva not used. Typo: stray space in "CHIRPS , IMERG" (Methods bullet 1).
