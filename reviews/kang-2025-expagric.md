# Card review: kang-2025-expagric

- **Card:** papers/kang-2025-expagric.md
- **Source:** papers-pdf/kang-et-al-2025.pdf (26 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 45 |
| Supported | 31 |
| Imprecise | 14 |
| Not in source | 0 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 8 |
| Important omissions | 14 (5 high, 7 medium, 2 low) |
| Metadata issues | 3 (license, data, not_established missing) |

The card gets the design and the headline preference result right, and nothing is contradicted. But it leaves out two of the paper's main results: which traits drive farmer preference (marketability after storage, then yield), and the PLADMM finding that on-station genotypic values did not reliably predict on-farm rankings. It also describes the on-station data as if it covered all varieties over 2018 to 2019, when only season 2018B was used, for nine varieties, with Cruza and Gisubizo imputed. The most important fix is to add the on-station versus on-farm result and correct the on-station data description (pages 8, 9, 15). The card asks this question but never answers it.

## Fixes needed

1. **On-station data described too broadly (summary, methods bullet, key numbers).** The card says on-station trials "from 2018–2019 provided genotypic values for the varieties". The source says NPT ran in 2018B and 2019A and MT in 2018B, but the 2019A data were dropped because not all varieties were grown that season (p. 8 to 9). Only nine of the eleven varieties were in these trials. Cruza and Gisubizo were not, and their genotypic values were imputed as the average of the other nine (p. 5, 9).
   - Summary replacement: "On-station national performance and multi-location trials from season 2018B gave genotypic values for nine varieties. Values for Cruza and Gisubizo, which were not in these trials, were imputed as the average of the other nine."
   - Methods replacement: "- **Station data.** National performance and multi-location trials (randomized complete blocks, three replicates). Seasons 2018B and 2019A were run, but only 2018B was used because not all varieties were grown in 2019A. Nine of the eleven varieties were included. Genotypic values came from mixed models (lme4 BLUPs, CLMM for ordinal traits, glmmTMB for disease traits) and were standardized. Cruza and Gisubizo received the average of the other nine."
   - Key numbers replacement row: "| Season 2018B | On-station trials used for genotypic values (2019A data dropped), nine of 11 varieties, Cruza and Gisubizo imputed | This paper |"

2. **Main result on on-station versus on-farm is missing.** The card's fourth question asks how well on-station results align with on-farm rankings, but the summary only says alignment was challenging. The source (p. 15, Table 5) reports that, in the cool node, varieties with lower on-station tuber weight ranked higher for yield (p = 0.005). In the warm node, higher on-station virus severity (p = 0.002) and tuber number per plant (p = 0.007) went with higher yield ranks. Only tuber number had the expected sign. On-station bacterial wilt resistance showed no significant correlation with farmer rankings (p. 16, 20). Add this paragraph to the summary: "On-station values did not reliably predict on-farm rankings. In the cool group, varieties with lower on-station tuber weight ranked higher for yield. In the warm group, varieties with higher on-station virus severity ranked higher. Only tuber number per plant had the expected positive link. On-station bacterial wilt resistance showed no significant link with farmer rankings for bacterial wilt."

3. **Trait drivers of preference are missing.** Marketability after storage (PH2) had the highest Kendall τ with all three final evaluations (0.454, 0.414, 0.398), and yield was second (0.376, 0.345, 0.271) (p. 11, 13 to 14, Table 4). Add to the summary: "Marketability after storage had the strongest link with the three final evaluations (Kendall τ 0.40 to 0.45), followed by yield (0.27 to 0.38)."

4. **High-income node recommendation omits Ndamira.** The card lists Gisubizo, Izihirwe, Kazeneza, Kirundo, Seka and Twihaze for high-income farmers. In Figure 5 (p. 16) Ndamira ranks first in this node (letter "a"), and the text says high-income farmers prefer Ndamira (p. 17) and that Ndamira is best for them (p. 18). The six varieties are the ones that did not differ from Ndamira. The p. 19 sentence that the card follows leaves Ndamira out (see Source issues). The card also misses the Cruza pattern. Replacement: "For marketability after storage, a tree with household covariates split farmers by annual crop income at 24.95 and 259.48 USD. Low-income farmers rated Cruza as highly marketable, and taste was linked most to marketability. High-income farmers rated Cruza below average, ranked Ndamira first, and linked marketability most to yield. In this group Ndamira did not differ significantly from Gisubizo, Izihirwe, Kazeneza, Kirundo, Seka and Twihaze."

5. **Gisubizo and Kazeneza "ranked third and fourth".** This holds only for overall performance (Table 3, p. 10). For willingness to plant they are fourth and third, and for overall preference Ndamira is third and Gisubizo sixth. Table 3 also shows Kazeneza significantly below Kirundo for overall performance (p = 0.038). The source then says they "still can be potential" alternatives (p. 18), which the card hardens to "remain viable alternatives". Replacement: "Several newer varieties, among them Gisubizo and Kazeneza, were close behind the old ones. Against farmers' own varieties they did not differ significantly, so the authors see them as possible alternatives."

6. **Large warm group as a caveat on the headline.** The source says the many farmers in the warm node (280 against 113), together with the broad adaptation of Kirundo and Cruza, may have pushed up the old varieties' overall worth (p. 15). This matters for anyone quoting "old varieties preferred". Add: "The authors suggest that the large warm group may partly explain the high overall ranks of the old varieties."

7. **Temperature tree details.** The card gives the node sizes but not the split or the rankings within nodes. The split was at a 90th percentile of day temperature of 23.75 °C (p. 15). In the warm node Kirundo ranked first but did not differ from Cruza, Ndamira and Seka. In the cool node Twihaze ranked first, and Figure 4A (approximate, read from the chart) shows Seka and Kazeneza sharing its letter group and Ndamira lowest. Replacement for the card's sentence on trees and the Twihaze sentence: "A Plackett-Luce tree for yield split farmers at a 90th percentile of day temperature of 23.75 °C. In the warmer group (280 farmers), Kirundo ranked first but did not differ significantly from Cruza, Ndamira and Seka. In the cooler group (113 farmers), Twihaze ranked first, close to Seka and Kazeneza, and Ndamira ranked last."

8. **Hedges dropped in the discussion paragraph.** The source says the old-variety preference "may be explained" by adaptability and disease tolerance (p. 18), and the Twihaze result "may be because" of lower disease pressure (p. 18). The low-input conditions are cited from other studies, not measured here, and the source says stable performance is "especially valuable", not that it "matters most". Replacement: "The authors suggest that the old varieties may stay popular because of broad adaptability, stable yields and disease tolerance under the low-input conditions common among smallholders."

9. **"Instead of one national list".** This is the card's own framing. The source says understanding performance across conditions is crucial for targeted recommendations (p. 18) and that the approach gives breeding programmes new insights to target products (p. 21). Replacement: "They conclude that combining these data sources can give breeding programmes targeted insights by environment and farm type."

10. **Release years.** The card says recent releases "from 2018 onwards". The nine newer varieties were released in 2019 and 2020 (p. 5, Table 1). The authors call them "post-2018". Replacement: "nine released in 2019 and 2020".

11. **not_established is missing.** Suggested field: `not_established: that new potato varieties are worse than old ones in general (several did not differ significantly from Kirundo, and the old-variety lead may partly reflect the large warm-site group); that on-station trials cannot predict farm performance in general (one on-station season, nine varieties, two imputed); that temperature itself causes the yield rank changes (the biological causes were not identified); that crop income or gender cause the preference differences (associations in a subset of households); results for all of Rwanda (two districts, two seasons)`

12. **Stated limitations are incomplete.** The source names more limitations than the card lists. Add:
    - "- The trial ran for only two seasons, without follow-up trials, which may have influenced the results (p. 19)."
    - "- Farmers may not observe disease accurately, which may explain why on-station and on-farm bacterial wilt did not correlate. Multi-season data, image analysis or farm visits are suggested (p. 20)."
    - "- PLADMM could not identify the biological causes of the temperature effect on yield ranks (p. 19, 21)."
    - "- No in-depth interviews with high-income farmers to explain their choices (p. 19)."
    - "- The results do not show whether varietal differences explain the higher yields of market-oriented farmers. Trials of old and new varieties under low-input, stress-prone conditions are needed (p. 20)."
    - Replace the RHoMIS bullet with: "- Only 283 of 460 participants had RHoMIS data, because of financial and time constraints, so socio-economic and environmental covariates were analysed separately (p. 6, 9)."

13. **License and data fields.** See Metadata check. Use `license: CC BY 4.0` and `data: data and R code on GitHub, https://github.com/AgrDataSci/potato-oft-genetic-gain`.

14. **Note on de Sousa et al. 2024 is slightly off.** The card calls the trial "earlier", which is not shown. The 2024 retrospective describes a Rwanda potato case with 11 varieties across seven districts and 135 trials in the first season, plus a cost case study with 155 tricot trials of 11 varieties. Replacement: "- de Sousa et al. 2024 (desousa-2024-asd) describes a Rwanda potato tricot with 11 varieties across seven districts (135 trials in the first season) and a cost case study with 155 tricot trials. This paper reports two districts (Gicumbi and Nyamagabe) and 460 farmers. Check whether it is the same trial network."

15. **Smaller additions to Methods and Key numbers.** Add methods bullets: "- **Plot and traits.** Each variety in a subplot of 40 tubers in four rows of three metres, under the farmer's own practices. Farmers ranked 17 traits at five stages, from 45 days after planting to 60 days after harvest (1380 plots in total)." and "- **Data cleaning.** Five records without GPS and 23 with major inconsistencies were removed." Replace the Analysis bullet with: "- **Analysis.** Plackett-Luce model for overall rankings, with Kirundo as reference. Kendall τ between the 17 traits and three final evaluations. Plackett-Luce trees with environmental covariates (chirps, climatrends, SoilGrids) and, separately, RHoMIS covariates (α = 0.1, or 0.07 for bacterial wilt, minimum group size 25). PLADMM with standardized on-station genotypic values as item covariates, chosen by forward selection on AIC." Key number rows to add are listed under Completeness.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Integrating environmental, socio-economic, and biological data in a farmer-led potato trial for enhanced varietal assessment in Rwanda | Same (p. 1) | Supported |
| authors | Kang G, de Sousa K, Manners R, van Etten J, Backes G, Rukundo P, Nduwumuremyi A, Ellison J, Tuyishime E, Mendes T, Griebel S | Same 11 authors, same order (p. 1, 26) | Supported |
| year | 2025 | 2025 (p. 1) | Supported |
| journal | Experimental Agriculture | Same (p. 1) | Supported |
| article | 61, e18, 1-26 | vol. 61, e18, 1 to 26 (p. 1) | Supported |
| type | research article | "Research article" (p. 1) | Supported |
| doi | https://doi.org/10.1017/S0014479725100100 | Same (p. 1) | Supported |
| license | CC BY | Creative Commons Attribution licence, by/4.0 (p. 1) | Imprecise. Use "CC BY 4.0" |
| data | see the data availability statement in the article | Data and code on GitHub, AgrDataSci/potato-oft-genetic-gain (p. 12, 21) | Imprecise. Give the URL |
| crops | potato | Potato (p. 1) | Supported |
| region | Rwanda (Gicumbi, Nyamagabe) | On-farm trials in Gicumbi and Nyamagabe (p. 5). On-station trials elsewhere in Rwanda (Figure 2) | Supported |
| gist | tricot potato trial with 460 Rwandan farmers ... old varieties still preferred and temperature and market orientation shaping rankings | p. 1, 15, 16 to 18 | Supported, but leaves out the on-station result. Optional sharper gist (28 words): "In a 460-farmer potato tricot trial in Rwanda, old varieties ranked highest, yield ranks shifted with temperature, marketability with crop income, and on-station values predicted on-farm ranks poorly" |
| not_established | missing | | Metadata issue. See Fix 11 |

Other fields: `software` lists PlackettLuce, gosset, climatrends, all used (p. 12). The source also uses ClimMob, ClimMobTools, chirps, lme4, glmmTMB and ordinal. The field is optional and the template format (CRAN link and version) is not followed. Low priority. `source: team` fits, since de Sousa, van Etten and Mendes are in people.md.

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Potato central to food security, growth slowed, varieties must fit conditions and preferences | Supported | Abstract (p. 1), intro (p. 2) | |
| 2 | Summary | Study tests linking tricot with environmental, socio-economic and on-station data | Supported | p. 1, 2 | |
| 3 | Summary | 2021A and 2021B, 460 farmers, Gicumbi and Nyamagabe, three of eleven, random incomplete blocks | Supported | p. 5 | Balanced incomplete blocks, 1380 plots (p. 2) |
| 4 | Summary | 283 surveyed with RHoMIS | Supported | p. 6 | |
| 5 | Summary | On-station 2018 to 2019 trials gave genotypic values for the varieties | Imprecise | p. 8 to 9 | Only 2018B used, nine varieties, two imputed. Fix 1 |
| 6 | Summary | Recent releases "from 2018 onwards" | Imprecise | p. 5, Table 1 p. 4 | Released 2019 and 2020. Fix 10 |
| 7 | Summary | Farmers preferred Cruza and Kirundo, Gisubizo and Kazeneza competitive | Supported | Abstract p. 1, Table 3 p. 10 | |
| 8 | Summary | Seasonal temperature changed yield rankings across regions | Supported | p. 1, 14 to 15 | |
| 9 | Summary | Trees, minimum group 25, split by temperature, 280 warm vs 113 cool | Supported | p. 9, 15, Table 5 | This is the yield tree only. Split value missing. Fix 7 |
| 10 | Summary | Socio-economic factors and gender shaped preferences | Supported | p. 1, 18, 20 | Gender result is from supplementary Figure S4 (tuber appearance) |
| 11 | Summary | Taste for home consumption, yield for sales | Supported | p. 1, 17 to 18, Table 6 | |
| 12 | Summary | High-income node can be recommended six varieties, low variation | Imprecise | p. 16 to 19, Figure 5 | Follows p. 19 text, but Ndamira ranked first in this node and is left out. Fix 4 |
| 13 | Summary | Challenges aligning data, integrated approach gives actionable insights | Supported | p. 1 | |
| 14 | Summary | Gisubizo and Kazeneza third and fourth, not significantly different from old and farmer-grown varieties | Imprecise | p. 18, Table 3 p. 10 | Third and fourth only for overall performance. Kazeneza below Kirundo for overall performance (p = 0.038). Fix 5 |
| 15 | Summary | They "remain viable alternatives" | Imprecise | p. 18 | Source hedges ("still can be potential"). Fix 5 |
| 16 | Summary | Authors explain old-variety preference by adaptability, stable yield, disease tolerance | Imprecise | p. 18 | Source: "may be explained". Fix 8 |
| 17 | Summary | All smallholders, conditions far from optimal, limited fertilizer and pesticides, stability matters most | Imprecise | p. 18 to 19 | All smallholders is supported. Low-input conditions come from cited literature, not this study's data. "matters most" is stronger than "especially valuable". Fix 8 |
| 18 | Summary | Twihaze yielded better in cool conditions, likely because of lower disease pressure | Imprecise | p. 15, 18, Figure 4A | Farmers ranked Twihaze first for yield, not significantly above Seka and Kazeneza. Source: "may be because". Fix 7, 8 |
| 19 | Summary | Linking gives targeted recommendations instead of one national list | Imprecise | p. 18, 21 | "Instead of one national list" is the card's framing. Fix 9 |
| 20 | Summary | Integration can improve breeding efficiency and adoption | Supported | p. 1, 21 | Repeats claim 13 |
| 21 | Methods | tricot: 460 farmers, 11 varieties, three each, 2021A Sep 2020 to Feb 2021, 2021B Mar to Jul 2021 | Supported | p. 2, 5 | |
| 22 | Methods | RHoMIS survey of 283 | Supported | p. 6 | |
| 23 | Methods | Station trials 2018 to 2019 for genotypic values | Imprecise | p. 8 to 9 | Fix 1 |
| 24 | Methods | PL trees with climate and socio-economic covariates, 90% cut-off, minimum group 25 | Supported | p. 9 | Incomplete: α = 0.07 for bacterial wilt, PLADMM, Kendall τ missing. Fix 15 |
| 25 | Limitations | Aligning on-station and on-farm was difficult | Supported | p. 1, 20 | |
| 26 | Limitations | Only 283 of 460 had RHoMIS data | Supported | p. 6, 9 | Source gives reason (money and time) and consequence (separate analyses). Fix 12 |
| 27 | Key numbers | 460 farmers | Supported | p. 1, 5 | |
| 28 | Key numbers | 11 varieties, three per farmer | Supported | p. 1, 5 | |
| 29 | Key numbers | 283 RHoMIS | Supported | p. 6 | |
| 30 | Key numbers | 2018 to 2019 on-station | Imprecise | p. 8 to 9 | Fix 1 |
| 31 | Key numbers | 25 minimum group size | Supported | p. 9 | |
| 32 | Key numbers | 280 vs 113 | Supported | p. 15, Table 5 | Add split (T90p 23.75 °C) and "yield tree". The two sum to 393 (reviewer's calculation) |
| 33 | Notes | de Sousa 2024 mentions an earlier Rwanda potato tricot with 135 trials in its first season | Imprecise | de Sousa et al. 2024 text | 135 trials is correct. "Earlier" is not shown. Fix 14 |
| 34 to 45 | Metadata | 12 checkable fields | 10 Supported, 2 Imprecise | See Metadata check | |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The list of nine varieties grown both on-station and on-farm names Cyerekezo, which is not one of the 11 tricot varieties. Table 1 shows Kirundo in the multi-location and national trials instead. | p. 9 vs Table 1 p. 4 | No | "- The text on p. 9 lists Cyerekezo among the nine varieties grown both on-station and on-farm. Table 1 shows Kirundo, not Cyerekezo, in these trials. Cyerekezo is likely an error for Kirundo." |
| High-income node: the text says Ndamira is preferred (p. 17) and best (p. 18) for high-income farmers, but the p. 19 recommendation list for node 5 names six other varieties and leaves out Ndamira. | p. 17, 18, 19, Figure 5 p. 16 | No (card follows p. 19) | "- For high-income farmers (node 5), Figure 5 and pp. 17 to 18 put Ndamira first. The six varieties listed on p. 19 are those that did not differ from Ndamira. The p. 19 list leaves Ndamira out." |
| Gisubizo and Kazeneza "ranked third and fourth" holds only for overall performance. Table 3 also shows Kazeneza below Kirundo for overall performance (p = 0.038) and Gisubizo below Kirundo for willingness to plant (p = 0.036). The discussion says no significant difference from old varieties, citing supplementary Table S4, which was not checked. | p. 18 vs Table 3 p. 10 | No | "- The claim that Gisubizo and Kazeneza ranked third and fourth fits overall performance only (Table 3). For overall preference, Ndamira is third and Gisubizo sixth. In Table 3, Kazeneza is significantly below Kirundo for overall performance (p = 0.038)." |
| The cool-node sentence is garbled ("...Kazeneza, Ndamira, and Seka received the lowest worth"). Figure 4A shows Seka and Kazeneza close to Twihaze and Ndamira lowest. Values read off the chart are approximate. | p. 15, Figure 4A p. 14 | No | "- The text on p. 15 about the cool node is garbled. Figure 4A shows Twihaze first, Seka and Kazeneza in the same letter group, and Ndamira lowest (read from the chart)." |
| The discussion places the cool-node Twihaze result in "Nyabibu and Nayamagabe districts". The on-farm trial was in Gicumbi and Nyamagabe. Nyabihu is not named as a trial district. | p. 18 vs p. 5 | No | "- The discussion (p. 18) names Nyabihu and Nyamagabe for the cool-node result, but the on-farm trial districts are Gicumbi and Nyamagabe (p. 5)." |
| The text says "with just one season of data" for yield, while the tricot trial covered two seasons. It may refer to the single on-station season used. | p. 15 vs p. 5, 19 | No | "- p. 15 mentions only one season of data for yield, while the tricot trial ran two seasons. This probably refers to the single on-station season (2018B)." |
| Sample sizes are not reconciled. 460 minus 5 (no GPS) minus 23 (inconsistent) gives 432 records (reviewer's calculation). The yield tree has 393 (113 + 280). Table 4 uses n = 309 and 228. The marketability tree has 219 (60 + 50 + 109) of 283 RHoMIS households. | p. 6, 11, 15, 17 | No | "- The paper does not explain the sample sizes per analysis: 432 records after cleaning, 393 in the yield tree, 309 or 228 in the trait correlations, and 219 in the crop-income tree (the card's sums)." |
| The Table 3 note says rows are sorted by estimate, but the overall performance and willingness-to-plant rows are not. The Ranking column is correct. | Table 3 p. 10 | No | Low priority. "- In Table 3, use the Ranking column, not the row order." |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim and three objectives (preferences, covariates, on-station item covariates) | Yes, briefly | low | None needed |
| Design: 1380 plots, 40-tuber subplots, own practices, 17 traits at five stages (p. 2, 5 to 6) | Partly | medium | Methods bullet in Fix 15 |
| Data cleaning: 5 without GPS and 23 inconsistent records removed (p. 6) | No | medium | Methods bullet in Fix 15 |
| Overall ranks: Kirundo and Cruza first and second on all three final evaluations, Ndeze and Nkunganire last (Table 3, p. 10, 12) | Partly | medium | Summary sentence in the draft below. Key row: "| Ndeze, Nkunganire | Ranked 10th and 11th on all three final evaluations (Table 3) | This paper |" |
| Farmer-grown variety comparison (Table S4, p. 12) | Partly | low | Covered by Fix 5 |
| Trait drivers: marketability after storage then yield (Table 4, p. 11, 13 to 14) | No | high | Fix 3. Key rows: "| τ 0.454 / 0.414 / 0.398 | Kendall τ of marketability after storage (PH2) with overall performance, willingness to plant, overall preference | This paper |" and "| τ 0.376 / 0.345 / 0.271 | Same for yield (PH1) | This paper |" |
| Temperature tree split and node rankings (p. 15, Figure 4A) | Partly | medium | Fix 7. Key row: "| 23.75 °C | 90th percentile of day temperature splitting the yield tree | This paper |" |
| Large warm group may inflate old varieties' overall rank (p. 15) | No | high | Fix 6 |
| On-station data scope: 2018B only, nine varieties, Cruza and Gisubizo imputed (p. 8 to 9) | No (card says otherwise) | high | Fix 1 |
| PLADMM and bacterial wilt: on-station values do not reliably predict on-farm ranks (Table 5, p. 15 to 16, 20) | No | high | Fix 2. Key row: "| p = 0.005, 0.002, 0.007 | PLADMM: on-station tuber weight (cool, negative), virus severity (warm, positive), tuber number (warm, positive) vs farmer yield ranks | This paper |" |
| Crop-income tree, Cruza marketable for low-income but not high-income farmers, Ndamira first for high income (Figure 5, Table 6, p. 16 to 18) | Partly | high | Fix 4. Key row: "| 24.95 and 259.48 USD | Annual crop-income splits in the marketability tree (n = 60, 50, 109) | This paper |" |
| Supplementary: tuber appearance linked to gender, yield to input use (p. 18, 20) | Partly | low | Sentence in the draft summary below |
| Authors' limitations: two seasons, disease observation accuracy, causes unresolved, no interviews, need for low-input trials (p. 19 to 20) | Partly | medium | Fix 12 |
| Conclusion that many farmers may not be able to reach optimal yields from new varieties (p. 21) | No | medium | Optional summary sentence: "The authors suggest that many farmers may not be able to get optimal yields from the new varieties." |
| Data and code on GitHub (p. 12, 21) | No | medium | Fix 13 |

For a tricot user, the most useful missing points are the trait drivers, the on-station versus on-farm finding, the warm-group caveat on the headline, and the crop-income split.

Draft replacement summary, 489 words, which includes Fixes 1 to 10 and keeps the card's style:

> Potato is central to food security in Rwanda but production growth has slowed, and improved varieties need to fit farmers' conditions and preferences to be adopted. The study tests the value of linking a tricot trial with environmental, socio-economic and on-station data.
>
> In seasons 2021A and 2021B, 460 farmers in the main potato regions of Gicumbi and Nyamagabe each tested three of eleven varieties, allocated randomly in incomplete blocks (1380 plots). Farmers ranked 17 traits at five stages, from 45 days after planting to 60 days after harvest. Of the 460 farmers, 283 were also surveyed with the RHoMIS household tool. The varieties included two released before 1990 (Cruza and Kirundo) and nine released in 2019 and 2020. On-station national performance and multi-location trials from season 2018B gave genotypic values for nine varieties. Values for Cruza and Gisubizo, which were not in these trials, were imputed as the average of the other nine.
>
> Across all farmers, Kirundo and Cruza ranked first and second for overall performance, willingness to plant again and overall preference, and Ndeze and Nkunganire ranked last. Several newer varieties, among them Gisubizo and Kazeneza, were close behind. Marketability after storage had the strongest link with the three final evaluations (Kendall τ 0.40 to 0.45), followed by yield (0.27 to 0.38).
>
> A Plackett-Luce tree for yield split farmers at a 90th percentile of day temperature of 23.75 °C. In the warmer group (280 farmers), Kirundo ranked first but did not differ significantly from Cruza, Ndamira and Seka. In the cooler group (113 farmers), Twihaze ranked first, close to Seka and Kazeneza, and Ndamira ranked last. The authors suggest that the large warm group may partly explain the high overall ranks of the old varieties.
>
> On-station values did not reliably predict on-farm rankings. In the cool group, varieties with lower on-station tuber weight ranked higher for yield. In the warm group, varieties with higher on-station virus severity ranked higher. Only tuber number per plant had the expected positive link. On-station bacterial wilt resistance showed no significant link with farmer rankings for bacterial wilt.
>
> For marketability after storage, a tree with household covariates split farmers by annual crop income at 24.95 and 259.48 USD. Low-income farmers rated Cruza as highly marketable, and taste was linked most to marketability. High-income farmers rated Cruza below average, ranked Ndamira first, and linked marketability most to yield. In this group Ndamira did not differ significantly from Gisubizo, Izihirwe, Kazeneza, Kirundo, Seka and Twihaze. Supplementary trees linked tuber appearance rankings to gender and yield rankings to input use.
>
> The authors suggest that the old varieties may stay popular because of broad adaptability, stable yields and disease tolerance under the low-input conditions common among smallholders. They note that the trial covered only two seasons, that farmers may not judge disease accurately, and that on-station and on-farm data were hard to align. They conclude that combining these data sources can give breeding programmes targeted insights by environment and farm type.

## Template compliance

| Item | Result |
|---|---|
| Summary word count | 405, within 400 to 500. The draft replacement is 489 |
| Gist length | 26 words, under 30 |
| Keywords | 10, within 8 to 12. Optional: swap "Plackett-Luce trees" for "PLADMM" or add "marketability" |
| Questions | 4, within 4 to 7. The fourth question (on-station vs on-farm) is not answered by the current summary. Fix 2 answers it |
| House style | tricot written in lowercase throughout. maniva not used |
| Structure | The current summary puts the conclusion (paragraph 4) before the discussion details (paragraph 5) and repeats the efficiency and adoption point. The draft fixes the order |
| not_established | Missing. Fix 11 |
