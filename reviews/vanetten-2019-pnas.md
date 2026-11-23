# Card review: vanetten-2019-pnas

- **Card:** papers/vanetten-2019-pnas.md
- **Source:** papers-pdf/van-etten-et-al-2019b.pdf (6 pages, printed pages 4194 to 4199. PDF page n = printed page 4193 + n. The SI Appendix is not part of this PDF.)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 56 |
| Supported | 46 |
| Imprecise | 7 |
| Not in source | 3 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 4 (plus 4 of low importance) |
| Metadata issues | 2 (gist wording, not_established incomplete) |

The card is accurate on all numbers, and every Key numbers value matches the PDF. The main problems are wording. The card calls this the "first" large tricot test and says the results "laid the basis" for later work, and the source says neither. It also implies that the two Ethiopian farmer varieties were released because of tricot, while the paper says the release rested on other field trials. The most important fix is that release sentence (p. 4197).

**Trial years by country (question from the lead reviewer).** This paper does not give years for each country. The main text says only that trials ran between 2012 and 2016, over three seasons in Ethiopia, five in Nicaragua and four in India, and refers to SI Appendix Table S1 for details (p. 4198). Table S1 is not in our PDF. The map caption names one season per country (Apante for Nicaragua, Meher for Ethiopia, Rabi for India) and a 2002 to 2016 base period for predictions (p. 4197, Fig. 3). The year 2017 appears only for the Ethiopian release (March 2017) and the Indian IIWBR promotion of HD 2967 (2016 to 2017), never as a trial year. So the card's "2012–2016" is correct as an overall window, but nothing in this PDF supports any per-country year range. The de Sousa 2023 date for Nicaragua (2015 to 2017) cannot be confirmed or ruled out from this PDF. Its end year falls outside the 2012 to 2016 window stated here. One possible reason, not checkable here, is a season label that spans two calendar years. A curator should check SI Table S1 or the Dataverse files. See Fix 6 for a Notes line.

## Fixes needed

1. **Ethiopian release (Summary, paragraph 5).** Card: "and two farmer varieties went on to official release". Source: the tricot results confirmed the superiority of two farmer varieties that were approved for release in March 2017, and the approval was "on the basis of other field trials" (p. 4197). The card wording suggests tricot led to the release. Replace the full sentence with:
   "In Ethiopia, tricot gave location-specific choices where the CIMMYT Wheat Atlas treated the highlands as one mega-environment. The results agreed with the 2017 release approval of two farmer varieties, which rested on other field trials."

2. **"First large-scale test" (Summary, paragraph 1, and gist).** Card: "It is the first large-scale test of tricot." The source never says "first". It calls the dataset "unique" and of "large size and scope" (p. 4194, Significance) and builds on earlier tricot pilots (p. 4195). Replace with:
   "The authors call it a participatory variety evaluation dataset of large size and scope."
   Replace the gist with:
   "Large tricot trials (12,409 plots, 3 countries) show farmer rankings capture known climate effects on varieties and can improve variety recommendations" (21 words)

3. **Last Summary sentence is outside knowledge.** Card: "These results laid the basis for climate-informed recommendations from tricot." This is a claim about later work, which a 2019 paper cannot support. Delete it, or move it to Notes with a label such as "Team view, not stated in the paper". To keep the Summary above 400 words and add an omitted point (p. 4198), replace it with:
   "The authors concede that combining existing methods could arguably give similar results, but tricot joins them in one simple, scalable format."

4. **Climate versus design models (Summary, paragraph 3).** Card: climate explained rankings "better" and geolocation "added nothing". Source: climate models "slightly outperformed" design models, and adding geolocation "even slightly degraded" fit (p. 4195, Table 1). Replace with:
   "Climate variables explained rankings slightly better than design variables such as location, season or soil, and adding geolocation slightly lowered fit."

5. **Smaller wording fixes in the Summary.**
   - Heat-tolerant lines (p. 4196). Card: "heat-tolerant lines beat the local variety above it." Source: three heat-tolerant varieties did, but SJC 730-79, also heat tolerant, did not. Replace with: "and three known heat-tolerant varieties beat the local variety above it (a fourth, SJC 730-79, did not)."
   - Diversity and fit (p. 4195). Card: "Model fit tracked varietal diversity." Source says the country differences were "probably due to" diversity. Replace with: "The authors link model fit mainly to varietal diversity."
   - Nicaragua catalogue (p. 4197). Card: "catalogue varieties performed worse than local ones". Source: only the two varieties the catalogue recommends for the study area (INTA Rojo, INTA Matagalpa). Replace with: "In Nicaragua, the two catalogue varieties recommended for the study area performed worse than local ones,"
   - Add the reliability result after the India sentence (p. 4198): "The tricot-recommended variety beat the best earlier recommendation with a probability of 0.51 to 0.65."
   With all of fixes 1 to 5 applied, the Summary is 468 words (checked).

6. **Notes: trial years and the 8208 issue.** Replace the first note and add two notes:
   - "The text names farmer varieties 8208 and 208304 as approved for release in March 2017 (p. 4197). 8208 appears nowhere else in the paper. Table 3 and Fig. 3B list 8034 instead. Check the SI or Dataverse before citing the variety name."
   - "The text says Table 3 confirms the 'superiority' of these farmer varieties, but in Table 3 both 208304 (0.041) and 8034 (0.030) have a lower probability of winning than 208279 (0.059) and the modern variety Hitosa (0.049). They rank above Ude and 222360 only (p. 4197)."
   - "The paper gives only an overall trial window (2012 to 2016) and the number of seasons per country (5 Nicaragua, 3 Ethiopia, 4 India). Years per country are in SI Appendix Table S1, which is not in our PDF. desousa-2023-joss dates the Nicaragua bean data to five seasons from 2015 to 2017, which does not fit this window. Check SI Table S1 or the Dataverse files before citing years for one country."

7. **Key numbers, trial period row.** Change the Context cell to:
   "Overall trial window for all three countries (5 seasons Nicaragua, 3 Ethiopia, 4 India). Years per country are in SI Table S1, not in this PDF"

8. **Key numbers, reliability row.** The card pools Nicaragua and Ethiopia into one range (0.58–0.65), which is the card's own combination. Give the source values separately (p. 4198):
   | 0.58–0.60 / 0.59–0.65 / 0.51–0.62 | Reliability (probability of beating the best variety from previous recommendations) of the tricot-recommended variety across locations, Nicaragua / Ethiopia / India (SI Fig. S4) | This paper |

9. **Methods, covariates bullet.** Card lists "rainfall". The main text names only "agroclimatic and soil variables" and land-surface temperature. Rainfall is not named as a covariate (it appears only as a correlate of low DTR, p. 4196). The full list is probably in the SI, which is not in our PDF. Replace with:
   "- **Covariates.** Seasonal agroclimatic variables (temperature from land-surface data) and soil variables, linked by coordinates and planting date. The full list is in the SI Appendix."
   Also extend the Trials bullet:
   "- **Trials.** tricot in Nicaragua (842 plots, 5 seasons), Ethiopia (1,090, 3 seasons) and India (10,477, 4 seasons), 2012–2016 overall. Varieties allocated at random as incomplete blocks with spatial balance, three per farm (four in Ethiopia). Field agents collected rankings by farm visits, first on paper and later through ClimMob."

10. **Stated limitations.** Add:
    "- The authors concede that a combination of existing approaches (environment characterization, multilocation trials, participatory selection, dissemination) could arguably give similar results.
    - Scaling needs new institutional arrangements and wide collaboration, not only more farmers."

11. **not_established.** Replace with:
    "effects on farmer income, food security or adoption; acceptance of tricot data in official variety release; that tricot trials caused the 2017 Ethiopian variety releases; gains from real (not perfect) seasonal forecasts; yield gains (farmers ranked relative performance, the paper reports no yield data); that tricot outperforms a combination of conventional trial methods"

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Crop variety management for climate adaptation supported by citizen science | Same (p. 4194) | Supported |
| authors | van Etten J, de Sousa K, ... Steinke J (24 names) | 24 authors, same order and initials (p. 4194). The pre-check flag on Dell'Acqua is only a curly versus straight apostrophe | Supported |
| year | 2019 | Published online 19 Feb 2019, issue 5 Mar 2019 (p. 4194) | Supported |
| journal | Proceedings of the National Academy of Sciences (PNAS) | PNAS (p. 4194) | Supported |
| article | 116(10), 4194-4199 | vol. 116, no. 10, 4194–4199 (p. 4194) | Supported |
| type | research article | Original research with Materials and Methods (pp. 4194–4198) | Supported |
| doi | 10.1073/pnas.1813720116 | Same (p. 4194 footer) | Supported |
| open_copy | PMC6410884 | Not in PDF | Not checked (no web access) |
| license | CC BY-NC-ND 4.0 | CC BY-NC-ND 4.0 (p. 4194) | Supported |
| data | Dataverse doi 10.7910/DVN/4ICF6W, code in SI Appendix | Same (p. 4194, p. 4198) | Supported |
| crops | common bean, durum wheat, bread wheat | Same (p. 4194) | Supported |
| region | Nicaragua, Ethiopia, India | Same (p. 4194, Fig. 1) | Supported |
| gist | "First large tricot test ... showing farmer rankings capture climate effects and improve variety recommendations" | "first" not stated. The rest matches the abstract (p. 4194) | Imprecise (Fix 2) |
| not_established | income, food security, adoption, official release acceptance | Fair, but misses the release causation, forecast skill and yield points | Supported, incomplete (Fix 11) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Aim: can crowdsourced citizen science characterize climate responses and improve recommendations in marginal environments | Supported | Abstract, Significance (p. 4194) | |
| 2 | Summary | First large-scale test of tricot | Not in source | Dataset called "unique" and of large size and scope (p. 4194). Pilots cited (p. 4195) | Fix 2 |
| 3 | Summary | Three random varieties per farmer, ranking suits low literacy and mobile phones | Supported | p. 4195 | In these trials field agents collected the data by visits (p. 4198). Four varieties in Ethiopia |
| 4 | Summary | 12,409 plots, three crop–country cases, 2012 to 2016 | Supported | p. 4194, p. 4198. 842 + 1,090 + 10,477 = 12,409 (checked) | Overall window only |
| 5 | Summary | Linked by coordinates and planting date, analyzed with Plackett-Luce trees | Supported | p. 4195, p. 4198 (recursive partitioning) | |
| 6 | Summary | Climate better than design, geolocation added nothing | Imprecise | "slightly outperformed", geolocation "slightly degraded" (p. 4195, Table 1) | Fix 4 |
| 7 | Summary | One temperature variable per case, matches known agronomy | Supported | One variable retained per case (p. 4195). Conclusions: known yield-determining factors (p. 4198) | |
| 8 | Summary | Bean shift at 18.7 °C maxNT, near published threshold, heat-tolerant lines beat local | Imprecise | 18.7 °C vs 20 °C (p. 4195). Three varieties beat local, SJC 730-79 did not (p. 4196) | Fix 5 |
| 9 | Summary | Durum responds to nights below 8.4 °C, vernalization, cold-adapted from higher elevations | Supported | p. 4196 | |
| 10 | Summary | Bread wheat responds to DTR | Supported | p. 4196 | |
| 11 | Summary | Model fit tracked varietal diversity | Imprecise | "probably due to" diversity (p. 4195) | Fix 5, certainty |
| 12 | Summary | Fit highest in Ethiopia (mixed set), lowest in India (narrow, modern) | Supported | p. 4195. India 0.04–0.09, Ethiopia 0.39–0.48 | Nicaragua also had a small modern set |
| 13 | Summary | Four ways climate analysis improves recommendations | Supported | p. 4194, p. 4196 | |
| 14 | Summary | 15-year base period averaging corrects for trial-season climate | Supported | p. 4196, Table 2. 2002–2016 = 15 years (checked) | Gains were small, e.g. 0.1533 to 0.1536 in Nicaragua |
| 15 | Summary | Perfect forecasts raised fit more than bias correction, realistic skill untested | Supported | p. 4196, Table 2 | |
| 16 | Summary | Worst regret gives different, risk-averse choices | Supported | p. 4196, Table 3 | |
| 17 | Summary | Maps cut across administrative and agroecological boundaries | Supported | p. 4197 | |
| 18 | Summary | Recommendations departed from official ones | Supported | p. 4194, p. 4197 | |
| 19 | Summary | Nicaragua: catalogue varieties worse than local, warm-zone heat-tolerant lines fit study area | Imprecise | Only INTA Rojo and INTA Matagalpa are named (p. 4197) | Fix 5 |
| 20 | Summary | Ethiopia: location-specific vs single mega-environment, two farmer varieties went on to release | Imprecise | Release approved March 2017 on the basis of other field trials (p. 4197) | Fix 1 |
| 21 | Summary | India: older K 9107 matched or beat HD 2967 | Supported | 0.077 vs 0.068 probability of winning, similar worst regret, released 1996 vs 2011 (p. 4197) | |
| 22 | Summary | Positions tricot as scalable, demand-led, for forecasts, portfolios, decentralized breeding, with institutional support | Supported | Conclusions (p. 4198) | |
| 23 | Summary | Results laid the basis for climate-informed recommendations from tricot | Not in source | Not stated | Fix 3 |
| 24 | Methods | Plot numbers, 2012–2016, three varieties (four in Ethiopia) | Supported | p. 4195, p. 4198 | |
| 25 | Methods | Covariates include land-surface temperature and rainfall | Not in source | Only "agroclimatic and soil variables" and land-surface temperature named (pp. 4195–4196) | Rainfall may be in the SI. Fix 9 |
| 26 | Methods | PLT with 10-fold cross-validated pseudo-R² | Supported | Table 1 (p. 4195) | |
| 27 | Methods | Base period, perfect forecast, probability of winning, worst regret, maps | Supported | pp. 4196–4197 | |
| 28 | Limitations | Perfect-forecast gains are an upper bound, real skill not tested | Supported | p. 4196 | "Upper bound" is the card's fair paraphrase |
| 29 | Limitations | Low fit in India with narrow modern set | Supported | p. 4195 | Source hedges with "probably" |
| 30 | Limitations | Land-surface temperature, not air temperature | Supported | p. 4195 | |
| 31 | Key numbers | 12,409 plots | Supported | p. 4194 | |
| 32 | Key numbers | 842 / 1,090 / 10,477 | Supported | p. 4195 | Fig. 2 nodes 501 + 341 = 842 (checked) |
| 33 | Key numbers | 2012–2016, 5 / 3 / 4 seasons | Supported | p. 4198 | Overall window, Fix 7 |
| 34 | Key numbers | 3 varieties (4 in Ethiopia) | Supported | p. 4198 | |
| 35 | Key numbers | 0.1978 / 0.4870 / 0.0882 | Supported | Table 1 (p. 4195) | |
| 36 | Key numbers | 18.7 °C vs 20 °C, Rainey and Griffiths 2005 | Supported | p. 4195, ref. 18 | Attribution correct |
| 37 | Key numbers | 8.4 °C, Fowler 2008 | Supported | p. 4196, ref. 19 | Attribution correct |
| 38 | Key numbers | 2,483 ± 113 m vs 2,101 ± 485 m | Supported | p. 4196, t(594) = 16.1 | |
| 39 | Key numbers | DTR splits 14.5 °C / 15.7 °C | Supported | p. 4196 | |
| 40 | Key numbers | 2002–2016 base period | Supported | Fig. 3 caption (p. 4197) | |
| 41 | Key numbers | Reliability 0.58–0.65 Nicaragua and Ethiopia, India 0.51–0.62 | Imprecise | Ethiopia 0.59–0.65, Nicaragua 0.58–0.60, India 0.51–0.62 (p. 4198) | Pooled range is the card's own. Fix 8 |
| 42 | Notes | Text names 8208 and 208304, Table 3 lists 8034 | Supported | p. 4197, Table 3, Fig. 3B | Fix 6 sharpens it |
| 43 | Notes | Perfect-forecast gains are an upper bound | Supported | p. 4196 | Repeats a limitation |

Metadata rows (13 checkable fields, see table above) make up the rest of the 56 claims: 12 Supported, 1 Imprecise.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Text names released variety "8208", but Table 3 and Fig. 3B list 8034, and 8208 appears nowhere else | p. 4197 | Yes, partly | See Fix 6, first note |
| Text says Table 3 confirms the "superiority" of 208304 and 8208, but both 208304 (0.041) and 8034 (0.030) score below 208279 (0.059) and Hitosa (0.049) | p. 4197, Table 3 | No | See Fix 6, second note |
| Per-country trial years are not in the main paper, only in SI Table S1. De Sousa 2023 dates Nicaragua to 2015 to 2017, outside the 2012 to 2016 window stated here | p. 4198 | No | See Fix 6, third note |
| Text gives Ethiopia fit as 0.39–0.48, but Table 1 top value 0.4870 rounds to 0.49 | p. 4195 | No (card does not use the range) | Not needed. Low importance |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim, design, sample size, main results, four improvement routes, comparisons with official recommendations | Yes | High | None |
| Reliability against previous best variety: 0.58–0.60 Nicaragua, 0.59–0.65 Ethiopia, 0.51–0.62 India (p. 4198) | Key numbers only | Medium | Fix 5 (Summary sentence) and Fix 8 |
| Authors' concession that combined existing approaches could arguably give similar results (p. 4198) | No | Medium | Fix 3 and Fix 10 |
| Trial logistics: incomplete blocks with spatial balance, three contacts with farmers, paper forms then ClimMob, field agents visited farms (p. 4198) | No | Medium | Fix 9 (Trials bullet) |
| Release of Ethiopian farmer varieties rested on other field trials (p. 4197) | No | Medium | Fix 1 |
| Seasons per country and season names (Apante, Meher, Rabi) (p. 4197, p. 4198) | Seasons in Key numbers only | Low | Optional: add season names to the trial period row |
| Table 2 values (e.g. India 0.0611 no covariates, 0.0694 average season, 0.1065 perfect forecast) | No | Low | Optional Key numbers row: "0.1533 / 0.1536 / 0.1749 (Nicaragua), 0.4280 / 0.4290 / 0.4442 (Ethiopia), 0.0611 / 0.0694 / 0.1065 (India) \| Cross-validated pseudo-R² of generalizable models: no covariates / average season / perfect forecast \| This paper" |
| India: HD 2733 beat HD 2967 in much of the area, and a broader set of varieties should be promoted (pp. 4197–4198) | No | Low | Optional |

## Template compliance

- Summary word count: 406 (within 400 to 500). With fixes 1 to 5 applied: 468.
- Gist: 18 words (under 30). Suggested gist: 21 words.
- Keywords: 8 (within 8 to 12).
- Questions: 4 (within 4 to 7).
- House style: tricot is lowercase throughout. maniva does not appear.
- Long format: all long-format sections are present.
