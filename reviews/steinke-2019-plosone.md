# Card review: steinke-2019-plosone

- **Card:** papers/steinke-2019-plosone.md
- **Source:** papers-pdf/steinke-et-al-2019.pdf (20 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 54 |
| Supported | 44 |
| Imprecise | 8 |
| Not in source | 2 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 7 |
| Important omissions | 9 |
| Metadata issues | 3 |

The card is accurate on design, sample sizes and the headline numbers, and every Key numbers row checks out. Its weak points are the stated limitations (one is not in the source and the authors' main limitations are missing), a tricot relevance sentence written into the Summary as if it came from the paper, a loose definition of the rank 2 Pareto front, and a missing not_established field. The most important fix is to replace the Stated limitations with the authors' own, above all that the method only finds practices already in use locally (p14 to 15).

## Fixes needed

1. **Stated limitations do not match the source.** The card says the qualitative step "only partly" filters self-report bias. The source says the farm visits filter out low-quality data and over-reporting households (p16), with no "partly". The card also says findings come from one region and need testing elsewhere. The authors never say this, and the study covers three regions of the Southern Agricultural Zone (p3). The authors' own limitations are missing (p14 to 16). Replace the whole section with:

   ```
   - Self-reported survey data can be biased. The authors argue that the farm visits filter out households that over-reported performance.
   - The method only finds practices already in use in the study area, so promising new technologies and institutional change may be missed.
   - Other indicator definitions, a different survey size, more follow-up visits or another season would likely give different positive deviants and practices.
   - Gender equity showed the weakest positive deviance, and households strong on gender equity tended to be weaker on other dimensions. This may reflect household priorities, a need for more radical innovation than farmer experimentation produces, or the narrow gender indicator used.
   - Indicators were chosen from development paradigms, not with local stakeholders, and may not match local priorities.
   - Limited demand may cap adoption of market-based practices (village shops, tree seedlings), and some practices may harm others (crop stockpiling can raise food prices, hired tractors cut wage work for landless people).
   - The method needs prior survey data collection, though a RHoMIS baseline can serve both impact assessment and the analysis.
   ```

2. **tricot relevance written into the Summary.** The card says the paper offers tricot users a way to choose technologies and is "an early example of linking RHoMIS household data with farmer-led innovation". The source does not say this. What the source does say is that promoting the observed practices may lead others to test them, perhaps supported by systematic on-farm experimentation formats, citing van Etten et al. 2016 on tricot (ref 54, p15). Replace the paragraph with the source-grounded sentence and move the card's own reading to Notes:

   Summary: `The authors suggest that seeing these practices on real farms may lead other farmers to test them, perhaps with systematic on-farm experimentation formats, citing tricot as one example.`

   Notes (add): `- Card's own reading, not stated in the paper: for tricot users the method is a possible way to choose which options to test and for which households, and an early link between RHoMIS household data and farmer-led innovation.`

3. **Pareto definition fits rank 1 only.** The card says positive deviants are households on the first two fronts, "those not outperformed on all objectives by any other household". Rank 2 households are by definition dominated by rank 1 households (p8). Replace with: `Households on the first Pareto front of these residuals (not dominated by any other household), plus a second front found after removing the first, were labelled positive deviants. This gave 54 households (12 on rank 1 and 42 on rank 2), about 10% of the sample.`

4. **Absolute performance missing and gender equity result softened.** The card says only that the advantage was weakest for social equity. On average positive deviants actually did slightly worse than expected for gender equity (p10, Table 4 p11), and in absolute terms they had significantly higher median food security and dietary diversity but also significantly higher GHG emissions and the same gender equity (Table 3, p11). Replace "Their advantage was strongest for food security and weakest for social equity." with: `In absolute terms they had higher food security and dietary diversity, but also higher emissions and the same gender equity. Relative to similar households, their advantage was strongest for food security and weakest for gender equity, where they did slightly worse than expected on average.`

5. **Resource-homologue mechanism imprecise.** The card says each practice was matched to households. In the source each surveyed household was matched, by Euclidean distance on six endowments, to its three most similar interviewed positive deviants, and their practices were suggested (p9 to 10, Table 7 p13). Replace the sentence with: `Each surveyed household was matched to the three interviewed positive deviants with the most similar endowments (its resource homologues), and their practices were suggested to it. This reached 8% to 100% of households, depending on the practice.`

6. **Wording more certain than the source.** The card says the method "needs fewer assumptions than model-based prioritization". The source says it "may require less assumptions" than methods that assess effects of new practices from household data (p14). The card also says the method "can be" extended beyond agriculture, where the source says it "may be extended" (p16 to 17). Replace with: `They suggest it may need fewer assumptions than methods that predict the effects of new practices from household data, and it names concrete practices rather than broad categories.` and `The authors suggest the method may also suit fields beyond agriculture where goals trade off.`

7. **Food security indicator described incompletely.** The Indicators bullet gives only the sufficiency part. The indicator is the first principal component (57% of variance) of capped food availability against 2,550 kcal per MAE and the number of food-secure months (p4). Replace the Indicators bullet with: `- **Indicators.** Caloric food security (first principal component, 57% of variance, of food availability against 2,550 kcal per male adult equivalent, capped at 100%, and the number of food-secure months), harmonic mean of good- and lean-season dietary diversity, cash income from farm sales and off-farm work, IPCC Tier 1 greenhouse gas emissions (sign reversed so lower emissions score higher), and a gender-equity proxy from women's and men's shares in decision-making.`

8. **Gist overstates and describes the procedure more than the finding.** "Locally proven practices" is stronger than the abstract, which says the practices "plausibly contributed" to outcomes (p1). The practices were not tested. Replace with (27 words): `Positive Deviance with Pareto-optimal residual performance on five objectives found 54 of 521 Tanzanian households doing better than expected, and 14 uncommon practices that plausibly explain this`

9. **not_established missing.** Add:

   `not_established: that the 14 practices cause better household performance (they were identified in interviews, not tested); that the practices will improve outcomes for the resource-homologue households they are matched to; that positive deviants do better than other households in absolute terms on all five objectives; that the approach finds options not already used locally; that the same positive deviants or practices would emerge with other indicators, sample sizes or seasons; that this is a tricot trial or an on-farm experiment`

10. **Methods bullets: small additions.** Replace three bullets:

    `- **Survey.** RHoMIS household survey in 44 randomly selected villages (20 in Mtwara, 20 in Lindi, 4 in Tunduru district of Ruvuma), 12 random households per village from extension officers' lists, 521 complete interviews.`

    `- **Expected performance.** Median regression per indicator on land, livestock, household size, region and village-level market orientation as a proxy for market access, with variables selected by AIC. Residuals give relative performance.`

    `- **Follow-up.** Sample split into 20 resource strata (land deciles by livestock above or below the median). One positive deviant per stratum for the 18 strata that had any, rank 1 preferred, chosen to maximize mean crowding distance. 15 interviewed in 12 villages with farm visits, plus 3 non-surveyed households as a comparison.`

    `- **Targeting.** Each surveyed household matched by Euclidean distance on six endowments (agro-ecology, labor, finance, land, livestock, social capital) to its three most similar interviewed positive deviants (resource homologues).`

11. **Remaining Summary edits.** Change "Regression on land" to `Median regression on land` (p6). Replace the last paragraph with: `Positive deviants were unevenly spread, with significantly fewer in Lindi region (Region 2). The authors link their higher formal education to innovation and lower risk aversion, as well as better off-farm work. The anonymized survey of 521 households is published as supporting information. The authors suggest the method may also suit fields beyond agriculture where goals trade off.` Also add after the over-reporting sentence: `But the method only finds practices already in use locally, and other indicators or more visits would likely give other deviants and practices.`

    A full replacement Summary with fixes 2 to 6 and 11 applied runs to 494 words. The changed paragraphs are given above. Paragraphs 1 and 2 stay as they are apart from "Median regression". In paragraph 5, "The qualitative follow-up also filters out households that over-reported performance." can be shortened to `Farm visits also helped to screen out households that may have over-reported performance.` to stay under 500 words.

12. **Key numbers: name the cited sources and add main results.** Change the Primary source of the 2,550 kcal row to `Pauw and Thurlow 2011 (ref 38), cited in this paper` and of the population density row to `Perfect and Majule 2010 (ref 29), cited in this paper`. Add rows:

    ```
    | 44 villages | Randomly selected, 20 in Mtwara, 20 in Lindi, 4 in Tunduru (Ruvuma) | This paper |
    | 0.65 SD | Mean scaled positive deviance for caloric food security, the strongest dimension (GHG 0.33, cash income 0.07) | This paper |
    | 0.67 vs 0.23 and 6.56 vs 4.00 | Median caloric food security and dietary diversity (food groups), positive deviants vs others, significant | This paper |
    | 395 vs 212 kg CO2-eq/year | Median GHG emissions, positive deviants vs others, significant (higher for deviants) | This paper |
    | r = -0.35 and -0.29 | Correlation of gender-equity deviance with cash income and food security deviance (significant) | This paper |
    | 323 households (62%) | Households whose three resource homologues were deviants I, VIII and XIII (labor scheduling, small shop, wage labor) | This paper |
    | 2.2 (max 5) | Mean number of deviant practices per interviewed household with any practice | This paper |
    ```


13. **Notes: add source issues and the tricot citation.** Add the Notes text from the Source issues table below, plus: `- The paper itself cites tricot (van Etten et al. 2016, ref 54) as a possible format for farmers to test the identified practices (p15).`

14. **License.** The PDF says "Creative Commons Attribution License" without a version (p1). Change to `CC BY (version not stated in the PDF, PLOS uses 4.0)` or keep 4.0 only if the curator confirms it on the journal page.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Prioritizing options for multi-objective agricultural development through the Positive Deviance approach | Same (p1) | Supported |
| authors | Steinke J, Mgimiloko MG, Graef F, Hammond J, van Wijk MT, van Etten J | Same, in this order (p1 citation) | Supported |
| year | 2019 | Published February 25, 2019 (p1) | Supported |
| journal | PLOS ONE | PLoS ONE (p1) | Supported |
| article | 14(2), e0212926 | 14(2): e0212926 (p1) | Supported |
| type | research article | "RESEARCH ARTICLE" header (p1) | Supported |
| doi | https://doi.org/10.1371/journal.pone.0212926 | Same (p1) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution License, no version given (p1) | Imprecise (fix 14) |
| data | S1 Dataset, anonymized RHoMIS survey of 521 households | S1 Dataset, 521 households, anonymized, XLSX (p17) | Supported. No code is published, which could be added ("no code published") |
| crops | mixed farming systems (maize, cassava, pigeon pea and others) | Maize, sorghum, cassava, pigeon pea, green grams, cashew, groundnut, sesame, chicken (p3) | Supported |
| region | South-Eastern Tanzania | Mtwara, Lindi and Tunduru district of Ruvuma, Southern Agricultural Zone (p3) | Supported. Could add the region names |
| gist | Adapts Positive Deviance ... 54 outlier households and 14 locally proven practices | 54 households, 14 practices that "plausibly contributed" (p1) | Imprecise ("proven" too strong, fix 8) |
| not_established | missing | n/a | Missing (fix 9) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Adapts Positive Deviance, known from child nutrition, to multi-objective agricultural development | Supported | Abstract and introduction (p1 to 2) | |
| 2 | Summary | Practitioners must choose practices, objectives trade off, households differ | Supported | Abstract (p1) | |
| 3 | Summary | Some answers already exist among households doing unusually well given their means | Supported | Abstract, existing diversity "may also bear solutions" (p1) | |
| 4 | Summary | 521 households, South-Eastern Tanzania, RHoMIS, 12 random per village from extension lists | Supported | p1, p4 | |
| 5 | Summary | Five indicators listed | Supported | Table 2 (p5), p4 to 6 | |
| 6 | Summary | Regression on land, livestock, household size, region, market access gives expected performance, residuals measure relative performance | Supported | p6 | Source uses median regression with AIC selection (fix 11) |
| 7 | Summary | First two Pareto fronts, "not outperformed on all objectives by any other household" | Imprecise | p8 | True for rank 1 only. Rank 2 is dominated by rank 1 (fix 3) |
| 8 | Summary | 54 households, about 10% | Supported | p10, p13. 54/521 = 10.4% | |
| 9 | Summary | No difference in gender ratio, age, household size, land, livestock, but more education | Supported | p10, Table 3 (p11) | Marital status also no difference. Livestock diversity was higher (Table 3, bold) |
| 10 | Summary | Advantage strongest for food security, weakest for social equity | Supported | p10, p15 to 16, Table 4 (p11) | Mean deviance for gender equity was slightly negative (fix 4) |
| 11 | Summary | Revisited 15 of 18 selected positive deviants | Supported | p9 | |
| 12 | Summary | 14 uncommon practices that plausibly explain outcomes | Supported | p1, p12 | |
| 13 | Summary | Examples: maize and pigeon pea intercropping, cassava planting material | Supported | Table 7 (p13), Fig 4 (p14) | |
| 14 | Summary | Each practice matched to households with similar endowments, 8% to 100% | Imprecise | p9 to 10, p13 | Households were matched to three nearest deviants, not practices to households (fix 5). 8% and 100% correct |
| 15 | Summary | Empirical, locally grounded starting point for planning interventions | Supported | p14, p16 | |
| 16 | Summary | Needs fewer assumptions than model-based prioritization | Imprecise | p14 | Source says "may require less assumptions", comparator is methods assessing effects from household data (fix 6) |
| 17 | Summary | Names concrete practices rather than broad categories | Supported | p15 | |
| 18 | Summary | Qualitative follow-up filters out over-reporting households | Supported | p16 | |
| 19 | Summary | For tricot users, a way to choose technologies and an early example of linking RHoMIS with farmer-led innovation | Not in source | Source only cites tricot as an on-farm experimentation format (p15) | Card interpretation, move to Notes (fix 2) |
| 20 | Summary | Unevenly spread, significantly fewer in one region | Supported | p10, Table 3 (p11) | Region 2 is Lindi (p3) |
| 21 | Summary | Education linked to innovation, lower risk aversion and off-farm opportunities | Supported | p14 | |
| 22 | Summary | Anonymized survey of 521 households in supporting information | Supported | S1 Dataset (p17) | |
| 23 | Summary | So the method can be reproduced or extended beyond agriculture | Imprecise | p16 to 17 | Source says "may be extended" (fix 6) |
| 24 | Methods | Survey: 12 per village, 521 complete interviews | Supported | p4 | 44 villages missing (fix 10) |
| 25 | Methods | Indicators: food availability vs 2,550 kcal capped, harmonic mean HDDS, cash income, IPCC Tier 1 GHG, gender proxy | Imprecise | p4 to 6 | Food security is a PCA composite with food-secure months (fix 7) |
| 26 | Methods | Expected performance: regression on five covariates, village market orientation as proxy | Supported | p6 to 7 | Add "median" and AIC (fix 10) |
| 27 | Methods | Pareto rank 1 and 2 in five dimensions, emoa R package | Supported | p8 | |
| 28 | Methods | 18 chosen by maximum crowding distance, 15 interviewed in 12 villages | Supported | p9 | Stratification step missing (fix 10) |
| 29 | Methods | Resource homologues on six endowments | Supported | p9 to 10 | Three nearest by Euclidean distance missing (fix 10) |
| 30 | Limitations | Self-report bias, "only partly" filtered by qualitative step | Imprecise | p16 | Source claims the visits filter it, no "partly" (fix 1) |
| 31 | Limitations | Gender equity smallest advantage, possibly needs more radical change | Supported | p16 | Other explanations given too (fix 1) |
| 32 | Limitations | One region of Tanzania, needs testing elsewhere | Not in source | p14 to 16 | Not stated by authors (fix 1) |
| 33 | Key numbers | 521 households | Supported | p4, p10 | |
| 34 | Key numbers | 12 per village | Supported | p4 | |
| 35 | Key numbers | 54 (12 + 42), about 10% | Supported | p10, p13 | 10.4% recomputed |
| 36 | Key numbers | 5 dimensions | Supported | p1, Table 2 (p5) | |
| 37 | Key numbers | 2,550 kcal, Tanzania national recommendation | Supported | p4, ref 38 Pauw and Thurlow 2011 | Name the cited source (fix 12) |
| 38 | Key numbers | 15 of 18 in 12 villages | Supported | p9 | |
| 39 | Key numbers | 14 practices | Supported | p12, Table 7 (p13) | |
| 40 | Key numbers | 8% to 100% | Supported | p13, Table 7 | Recomputed: 42/521 = 8.1%, 521/521 = 100% |
| 41 | Key numbers | ~1 to 5 persons/km², cited | Supported | p3, ref 29 Perfect and Majule 2010 | Name the cited source (fix 12) |
| 42 | Notes | Not a tricot trial | Supported | Whole paper | |

Frontmatter claims (12 checked: 10 Supported, 2 Imprecise) are in the Metadata check above and are included in the counts.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Table 3 gives 54 positive deviants and 476 other households, which sums to 530, not 521 (521 minus 54 is 467) | Table 3 (p11) vs p4, p10 | No | `- Table 3 lists 476 other households, but 521 minus 54 positive deviants is 467 (source inconsistency).` |
| Land strata n in Table 4 sum to 52, not 54 (livestock strata sum to 54) | Table 4 (p11) | No | `- In Table 4 the land size strata n add to 52, not 54.` |
| Scaled mean deviance in Table 4 has the opposite sign to the raw mean for dietary diversity (+2.1 food groups raw, -0.93 scaled) and a large negative value for gender equity (-1 raw, -1.52 scaled). Text ranks food security, GHG, then cash income from this row | Table 4 (p11), p10 | No | `- Table 4 scaled deviance is hard to reconcile with the raw means (dietary diversity +2.1 raw but -0.93 scaled), so the ranking of dimensions should be quoted with care.` |
| Abstract says deviants performed only slightly better for social equity, but Results say they did slightly worse than expected for gender equity | p1 vs p10 | No | `- The abstract says positive deviants did slightly better for social equity, but Results and Table 4 show slightly worse than expected.` |
| Table 7 gives the small shop practice (Ss) a frequency of 1, but Table 5 lists it for deviants V and XIII. The text count of seven single-household practices matches Table 5, not Table 7 | Table 5 (p12), Table 7 (p13), p12 | No | `- Small shop (Ss) is observed once in Table 7 but twice in Table 5 (deviants V and XIII).` |
| Text says 15 positive deviants were interviewed, Table 5 lists 14 (I to XIV) | p9, p12 vs Table 5 (p12) | No | `- Table 5 lists 14 interviewed positive deviants, while the text says 15.` |
| Text says deviants had higher absolute cash income and only "slightly worse" GHG, but in Table 3 the cash income difference (686 vs 281 US$) is not marked significant, and median GHG is almost double (395 vs 212) and significant | p10 vs Table 3 (p11) | No | `- Table 3 does not mark the cash income difference as significant, and median GHG emissions of positive deviants are almost twice those of other households, more than the "slightly worse" in the text.` |

Recomputed and consistent in the source: Table 5 homologue columns each sum to 521, and row totals match. Table 7 percentages match counts out of 521. Mean of 2.2 practices (29 practice uses over 13 households) matches Table 5. 323/521 = 62%.

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Method finds only practices already in use, so new technologies and institutional change may be missed (p14 to 15) | No | High | Fix 1 and fix 11 |
| Other indicators, sample size, more visits or another season would give other deviants and practices (p15) | No | Medium | Fix 1 |
| Absolute differences: deviants higher on food security and diet diversity, higher GHG, same gender equity (Table 3, p11) | No | Medium | Fix 4, fix 12 |
| Food security is a PCA composite of sufficiency and food-secure months (p4) | Partly | Medium | Fix 7 |
| 44 villages in Mtwara, Lindi and Tunduru (p3 to 4) | No | Medium | Fix 10, fix 12 |
| Effect sizes: scaled deviance and gender equity trade-off correlations (Tables 4 and 6, p11 to 12) | No | Medium | Fix 12 |
| Market saturation and negative externalities of some practices (p15) | No | Medium | Fix 1 |
| Source cites tricot as an on-farm experimentation format for testing the practices (p15) | No | Medium | Fix 2, fix 13 |
| Indicators not chosen with local stakeholders, more participatory agenda-setting suggested (p5, p16) | No | Medium | Fix 1 |
| 62% of households share homologues I, VIII, XIII, pointing to labor scheduling, small shop and wage labor (p13) | No | Low | Fix 12 |
| Resource strata patterns: low-livestock deviants stronger for food security, cash, diet, high-livestock for gender and GHG (p11 to 12) | No | Low | Optional Summary or Notes line |
| Higher livestock diversity among deviants, possibly a deviant practice itself (p10, p14) | No | Low | Optional |
| Seven practices at single households, up to six, one household with none, mean 2.2 and max 5 (p12) | No | Low | Fix 12 |
| Practices differ from literature "best-bets" such as rainwater harvesting and biochar (p15) | No | Low | Optional Notes line |
| Usable by NGOs or extension, quantitative step can be done by remote researchers (p15) | No | Low | Optional |
| Needs prior survey investment, RHoMIS can double as baseline (p16) | No | Low | Fix 1 |
| Aim, design, sample size, main deviant count, practice count, conclusions | Yes | High | Covered |

## Template compliance

- Summary word count: 408 (within 400 to 500). The suggested replacement is 494.
- Gist: 21 words (under 30). Suggested gist is 27 words.
- Keywords: 8 (within 8 to 12). Could add "resource homologues" and "Tanzania".
- Questions: 4 (within 4 to 7).
- House style: tricot written in lowercase throughout. maniva does not appear. No issues.
- Long-format sections all present. not_established is missing (fix 9).
