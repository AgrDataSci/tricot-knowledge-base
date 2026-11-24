# Card review: desousa-2023-joss

- **Card:** papers/desousa-2023-joss.md
- **Source:** papers-pdf/de-sousa-et-al-2023a.pdf (6 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 27 |
| Supported | 15 |
| Imprecise | 9 |
| Not in source | 3 (1 of these is outside information in Notes, not counted as a card error) |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 5 |
| Important omissions | 5 |
| Metadata issues | 2 |

The card is accurate on the package's purpose, its origin, the reproducibility framing and the data sources. The main weakness is the case study. The card describes the tree as if hot days and warm nights act together in one group, but Fig. 1c shows a first split at 49 summer days and a maxNT split only inside the branch with 49 or fewer summer days (p. 4). The card also leaves out that indices were computed over a season-average span and that summer days were added only to illustrate the method. The "Stated limitations" section lists two points the authors do not state. not_established is missing. All fixes are small and can be pasted from below.

## Fixes needed

1. **Tree result in the Summary (high).** The card says performance shifts "where more than 70% of growing days exceed 30 °C and night temperatures are above 18.7 °C". Fig. 1c (p. 4) shows the root split at SU 49 days. The maxNT split at 18.68 °C appears only in the branch with SU of 49 or less. No node combines both conditions. The authors' own interpretation sentence (p. 3) uses "and", which is the source of the confusion (see Source issues). Replace the third Summary paragraph with the version in fix 3.

2. **Season-average span and illustrative use of summer days are missing (high).** The source says the authors take the GDD span averaged per season "for simplicity" (p. 2) and compute indices over it (p. 3). The card says indices are computed "over that cycle", which suggests each plot's own cycle. The source also says van Etten et al. 2019 retained only maxNT by forward selection and that SU was added to show how trees grow in complexity (p. 3). Covered by fix 3 and fix 6.

3. **Replace the whole Summary** (fixes 1, 2, 4, 5, 7, 8 together, 498 words, no semicolons or em dashes):

```
climatrends computes climate variability indices for ecological and crop models in a reproducible way. It grew out of scripts written for earlier studies, including van Etten et al. 2019, and was packaged so research groups across CGIAR and partners could run the same analyses on new data.

The package computes indices over a growing period defined per observation, for example from each farm's planting date over a set number of days. Its eight main functions cover temperature indices (such as maximum night temperature and summer days, the days above 30 °C), precipitation indices, cumulative dry and wet spells, crop-sensitive indices, growing degree-days (GDD), reference evapotranspiration with the Blaney-Criddle method (ETo) and the occurrence of late spring frost. Input can be local data as a vector, matrix or array, or sites in a data.frame or sf object, for which the package fetches data through the nasapower and chirps packages. The authors state it was the first R package for agroclimatic indices that handles site heterogeneity and time series (on CRAN since February 2020), and describe it as complementary to packages limited to degree-days or to zoning.

The case study reuses tricot data from van Etten et al. 2019, where 11 common bean varieties were tested in incomplete blocks of three (842 blocks) over five seasons from 2015 to 2017 in Nicaragua. With MODIS land-surface temperature, the authors use GDD() to count the days each plot needed to reach 900 degree-days from planting (54 to 100 days). For simplicity they average this per season and compute temperature indices over that seasonal span. The earlier study had retained only maximum night temperature (maxNT) through forward selection. Here the authors add summer days (SU) to show how a Plackett-Luce tree grows with more indices. The tree first splits at 49 summer days. In the branch with 49 or fewer summer days, it splits again at a maxNT of 18.7 °C. The authors read this as bean performance on farm being driven by hot days (which they equate with more than 70% of growing days) and warmer nights.

The authors frame the package around reproducibility, the ability to repeat an analysis, and replicability, the ability to repeat an experiment, which they see as a gap in most agricultural and ecological studies. Making the same indices available to all groups lets peers validate analyses and apply them to new data. Possible further development includes integration with other datasets through API client packages and new physiology-based indices. Integration with daily high-resolution climate data and seasonal forecasts for East Africa from Tomorrow.io's CBAM model is under development. The authors direct users to CRAN for the latest functions, since the package evolves.

For tricot users, the package turns each farm's location and planting date into comparable climate covariates, which Plackett-Luce trees can use to explain where varieties win or lose. The example data ship with the package, so the case study can be rerun, although the printed code may need updating for current package versions (see Notes).
```

4. **Index examples not in the source (medium).** The card lists diurnal range, tropical nights, cold or warm spells, total rainfall and rainy days. The paper names none of these. It names only maxNT and SU (p. 3) and, in Table 1, MLDS and MLWS through cumdrought() and cumrain() (p. 2). It refers to the package documentation for the list of indices (p. 1). The replacement Summary in fix 3 keeps only indices named in the paper.

5. **"842 farms" (medium).** The source says 842 blocks (p. 1). Use "842 blocks" as in fix 3 and in the Key numbers row.

6. **Stated limitations are not the authors' (medium).** Neither point is stated in the paper. Replace the section with:

```
## Stated limitations

- For simplicity, the case study computes temperature indices over the season-average crop cycle, not each plot's own cycle.
- The case study only partly reproduces van Etten et al. 2019, with a slightly different approach (degree-days from planting to maturity, and new indices).
- Summer days were added to show how Plackett-Luce trees grow in complexity, not chosen by variable selection. The earlier forward selection retained only maxNT.
```

   and add to Notes:

```
- Card's own observations, not stated by the authors: the example uses MODIS land-surface temperature, not air temperature. The package computes indices but does not choose which ones suit a crop or question. The paper names only a few indices and refers to the package documentation for the full list.
```

7. **Further development worded too firmly, and said twice (low).** The short paragraph "The authors plan further development to add indices and data sources as user needs evolve" adds "as user needs evolve", which is not in the source, and repeats the later paragraph. The source says integration "can" be supported and new indices "could" be added. Only the CBAM work is "under development" (p. 4). Fix 3 deletes the short paragraph and softens the wording.

8. **"Can be rerun directly" (low).** The printed code appears to need extra steps to run (see Source issues), and the card's own Note says arguments changed across versions. Fix 3 softens this.

9. **Methods bullets (medium).** Replace the Functions and Example bullets with:

```
- **Functions.** Eight main functions (Table 1): temperature(), rainfall(), cumdrought(), cumrain(), GDD(), ETo(), late_frost(), crop_sensitive(). Methods exist for numeric vectors, matrix or array, data.frame and sf (POINT or POLYGON). The data.frame and sf methods fetch data through nasapower and chirps.
- **Example.** commonbean data with MODIS temperature. GDD() with 900 degree-days (de Medeiros et al. 2016) gives the days from planting to maturity, averaged per season. temperature() computes indices over that span. pltree() from PlackettLuce fits a tree on maxNT and SU with minsize = 50.
```

10. **Key numbers (medium).** Replace the table with:

```
| Number | Context | Primary source |
|---|---|---|
| 11 varieties, 842 blocks | Common bean tricot trial in Nicaragua, five seasons from 2015 to 2017, reused in the case study | van Etten et al. 2019, cited in this paper |
| 900 degree-days | Planting to maturity for common bean, used in GDD() | de Medeiros et al. 2016, cited in this paper |
| 54 to 100 days | Days needed to reach 900 degree-days across plots (Fig. 1a) | This paper |
| 49 summer days | First split in the Plackett-Luce tree (SU, days above 30 °C). The authors equate it with more than 70% of growing days | This paper |
| 18.7 °C (18.68 in Fig. 1c) | Maximum night temperature split, only in the branch with 49 or fewer summer days | This paper |
| 8 | Main functions in the package (Table 1) | This paper |
```

11. **Gist (metadata).** The current gist lists topics. Replace with (27 words):

```
gist: R package that computes climate indices over each plot's growing period. Its tricot bean example in Nicaragua shows variety rankings splitting by summer days and night temperature
```

12. **not_established is missing (metadata).** Add:

```
not_established: the 49 summer days and 18.7 °C splits are validated heat thresholds for common bean; hot days and warm nights act together in one tree node; the case study fully reproduces van Etten et al. 2019; the package chooses which indices suit a crop; MODIS land-surface temperature can replace air temperature without checking; the indices were validated in this paper
```

13. **Notes labelling (low).** The first Note about function names changing is outside information. Suggested wording:

```
- Outside information, not from the paper: function names and arguments have changed across versions. Check the current CRAN reference manual before reusing code from the paper.
```

   Also add the source-issue Notes from the table below.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Climate variability indices for ecological and crop models in R. The climatrends package | Same, with a colon (p. 1) | Supported (colon to period is expected) |
| authors | de Sousa K, van Etten J, Neby M, Solberg SØ | Kauê de Sousa, Jacob van Etten, Magne Neby, Svein Ø. Solberg (p. 1) | Supported |
| year | 2023 | Published 08 May 2023 (p. 1) | Supported |
| journal | Journal of Open Source Software | p. 1 footer | Supported |
| article | 8(85), 4405 | p. 1 footer | Supported |
| type | software paper | JOSS software paper | Supported |
| doi | https://doi.org/10.21105/joss.04405 | p. 1 | Supported |
| license | CC BY 4.0 | p. 1 margin | Supported |
| data | commonbean ships with the package, tricot trial in Nicaragua with MODIS temperature | p. 2 | Supported |
| software | climatrends on CRAN, v1.2, checked 2026-10-30 | Not in PDF | Not in source (outside information, not counted) |
| crops | common bean (example) | p. 2 | Supported |
| region | Nicaragua (example), global use | Nicaragua (p. 2). Expansion to other regions and global API data (p. 1) | Supported |
| gist | Lists topics | | Imprecise (lists topics instead of what the paper shows). See fix 11 |
| not_established | Missing | | Missing. See fix 12 |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Computes climate variability indices for ecological and crop models, reproducibly | Supported | Title, Summary and Statement of need (p. 1) | |
| 2 | Summary | Grew out of earlier scripts incl. van Etten 2019, for CGIAR and partners | Supported | p. 1 | Also de Sousa et al. 2018 |
| 3 | Summary | Indices over a per-observation growing period from planting date | Supported | p. 1, code on p. 3 (day.one, span) | |
| 4 | Summary | Lists diurnal range, tropical nights, cold or warm spells, total rainfall, dry and wet spells, rainy days, GDD, ETo, late frost | Imprecise | Table 1 (p. 2) names GDD, ETo Blaney-Criddle, late frost, MLDS, MLWS. Only maxNT and SU named in text (p. 3) | Several examples are outside information. Fix 4 |
| 5 | Summary | Input local or remote through chirps and nasapower | Supported | p. 2 | AgERA5 also mentioned (p. 1) |
| 6 | Summary | Complementary to packages limited to degree-days or zoning | Supported | p. 1 to 2 | |
| 7 | Summary | 11 varieties, blocks of three, 842 farms | Imprecise | "842 blocks" (p. 2) | Fix 5 |
| 8 | Summary | GDD to estimate each plot's cycle, then indices over that cycle | Imprecise | Per-plot GDD, then season average used as span (p. 2 to 3) | Fix 2 |
| 9 | Summary | Tree splits by summer days (>30 °C) and maxNT | Supported | p. 3, Fig. 1c (p. 4) | |
| 10 | Summary | Shift where >70% of days exceed 30 °C and nights >18.7 °C | Imprecise | Fig. 1c: SU split at 49 first, maxNT split only within SU ≤ 49 (p. 4) | Follows the authors' wording on p. 3 but misdescribes the tree. Fix 1 |
| 11 | Summary | Points to heat accumulation and warm nights as drivers | Supported | p. 3 | Card's "pointing to" keeps the hedge |
| 12 | Summary | Authors plan development as user needs evolve | Imprecise | p. 4 says "can" and "could" | Fix 7 |
| 13 | Summary | Reproducibility and replicability framing, gap in most studies | Supported | p. 1 | |
| 14 | Summary | Peers can validate analyses and use new data | Supported | p. 1 | |
| 15 | Summary | Planned development: API packages, physiology indices, CBAM East Africa | Imprecise | p. 4 | Only CBAM is "under development". Fix 7 |
| 16 | Summary | Directs users to CRAN for latest functions | Supported | p. 4 | |
| 17 | Summary | For tricot users, turns location and planting date into covariates for PL trees | Supported | p. 1 to 3 | Card's own synthesis, reasonable |
| 18 | Summary | Example data ship with package, case study can be rerun directly | Imprecise | Data on p. 2. Code issues p. 2 to 3 | Fix 8 |
| 19 | Methods | Functions: six named | Imprecise | Table 1 lists eight (p. 2) | Missing cumdrought(), cumrain(). Fix 9 |
| 20 | Methods | Own start date and span per observation | Supported | p. 1, p. 3 | |
| 21 | Methods | Example: commonbean, MODIS, GDD, indices per season, PL tree | Supported | p. 2 to 3 | |
| 22 | Limitations | Land-surface rather than air temperature | Not in source | Not stated by authors | Move to Notes. Fix 6 |
| 23 | Limitations | Index choice depends on crop, package does not select | Not in source | Not stated by authors | Move to Notes. Fix 6 |
| 24 | Key numbers | 11 varieties, 842 blocks, van Etten 2019 | Supported | p. 2 | Attribution correct |
| 25 | Key numbers | >30 °C on >70% of days | Imprecise | Tree split is 49 SU days (p. 3, Fig. 1c p. 4). 70% is the authors' gloss | Fix 10 |
| 26 | Key numbers | >18.7 °C maxNT split | Supported | p. 3, 18.68 in Fig. 1c (p. 4) | Add that it applies only within SU ≤ 49 |
| 27 | Notes | Function names and arguments changed across versions | Not in source (outside information) | Paper only points to CRAN for updates (p. 4) | Not counted as error. Label it. Fix 13 |

The Note that 18.7 °C matches vanetten-2019-pnas is a cross-reference and was not counted. That card does give 18.7 °C.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The interpretation sentence joins hot days and warm nights with "and", but the tree splits on maxNT only within the branch with 49 or fewer summer days. No node has both conditions | Text p. 3, Fig. 1c p. 4 | No | - The authors' reading (hot days and warmer nights) does not match the tree structure. Fig. 1c splits first at 49 summer days, and the 18.7 °C night split appears only in the branch with 49 or fewer summer days. |
| ">70% of the growing days" is not derived in the text. 49 days is 49% to 91% of the 54 to 100 day cycles, and 70% only for a cycle of about 70 days, near the peak of Fig. 1a (read from the chart, approximate) | p. 3, Fig. 1a p. 4 | No | - The ">70% of growing days" equals 49 summer days only for a 70-day cycle (card's own calculation). Over the 54 to 100 day range in Fig. 1a it would be 49% to 91%. |
| The code uses the magrittr assignment pipe %<>% but loads only climatrends, PlackettLuce and tidyverse. tidyverse does not appear to attach %<>%, so the code may fail as printed | p. 2 to 3 | Partly (Note on version changes) | - The printed code uses %<>% from magrittr without loading magrittr. Add library("magrittr") or use cbean <- cbean %>% ... when rerunning. |
| Fig. 1a x-axis is labelled "GDD" but shows days to reach 900 degree-days, as the caption says | Fig. 1a p. 4 | No | - Fig. 1a axis reads "GDD" but the values are days (54 to 100), as the caption says. |
| "incomplete blocks of three randomly allocated to 842 blocks" is unclear about the unit (blocks, plots or farms) | p. 2 | No | Low. No Note needed if the card uses "842 blocks". |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: reproducible and replicable climate indices across groups | Yes | High | |
| Origin in earlier scripts (de Sousa 2018, van Etten 2019) | Yes | Medium | |
| Indices computed over the season-average span, "for simplicity" | No | High | Fix 3, fix 6 |
| SU added for illustration, earlier forward selection kept only maxNT | No | High | Fix 3, fix 6 |
| Tree structure (SU 49 first, maxNT 18.68 within SU ≤ 49, minsize 50) | Partly, misdescribed | High | Fix 1, fix 9, fix 10 |
| 900 degree-days threshold and 54 to 100 days range | No | Medium | Fix 3, fix 9, fix 10 |
| Eight main functions incl. cumdrought() and cumrain() | No (six listed) | Medium | Fix 9 |
| Five seasons, 2015 to 2017, three named seasons (primera, postrera, apante) | No | Medium | Fix 3, fix 10 (season names optional) |
| Class methods: vector, matrix or array, data.frame, sf | Partly | Low | Fix 3, fix 9 |
| Authors' claim: first R package for agroclimatic indices, CRAN since February 2020, in CRAN Task View Agriculture | No | Low | Fix 3 |
| AgERA5 integration | No | Low | Optional: add AgERA5 next to nasapower and chirps in Notes |
| Time series over fixed periods and locations | No | Low | Optional |
| Further development, CBAM East Africa | Yes | Low | Fix 7 softens wording |
| Funding: Nordic Joint Committee for Agricultural and Food Research, AVISA and 1000FARMS (Gates Foundation) | No | Low | Optional Note |

Cross-card point to check (outside this PDF): this paper dates the Nicaragua trial to five seasons from 2015 to 2017 (p. 2). The vanetten-2019-pnas card gives 2012 to 2016 for its trials. A curator may want to confirm both cards against their sources.

## Template compliance

- Summary word count: 407 (target 400 to 500). Pass. The suggested replacement is 498.
- Gist: 20 words. Pass on length, but it lists topics (fix 11, 27 words).
- Keywords: 9. Pass.
- Questions: 4. Pass.
- House style: tricot and climatrends in lowercase. Pass. No em dashes or semicolons in the card prose.
- not_established: missing (optional in template, but advised for this card).
