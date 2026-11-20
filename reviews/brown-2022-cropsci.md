# Card review: brown-2022-cropsci

- **Card:** papers/brown-2022-cropsci.md
- **Source:** papers-pdf/brown-et-al-2022.pdf (21 pages, printed pages 2246 to 2266, so PDF page = printed page minus 2245)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 52 |
| Supported | 30 |
| Imprecise | 12 |
| Not in source | 0 |
| Contradicted | 10 |
| Source issues (problems in the source itself, not card errors) | 5 |
| Important omissions | 9 |
| Metadata issues | 3 |

The card gets the overall design and the main message right (pooled tricot trials, Plackett-Luce trees, heat as the main factor, planting-date models, maps with entropy and area of applicability). But several specific results are wrong. The card says EAP 9508-93 appears only where it was tested, while the source uses it as the main example of a genotype predicted outside its test country. It also names the wrong genotypes as winners under warm conditions, gives the Apante c index as 0.563 instead of 0.625, calls plots "participants" with the wrong minimum, and gives the wrong reason for the 27 to 17 reduction. The author list is in the wrong order and misses two authors. The most important fix is the EAP 9508-93 sentence (p. 2262, PDF 17), together with a corrected second summary paragraph.

## Fixes needed

1. **EAP 9508-93 claim reversed (Contradicted).** The card says: "Some genotypes, such as EAP 9508-93 released in Honduras as Cedrón, appear only where they were tested." The source says EAP 9508-93 was tested only in Honduras but is predicted in the top three in most parts of Costa Rica (Figure 4a). High entropy there means it is not a direct recommendation, but it is a candidate for future evaluation in Costa Rica (p. 2262, PDF 17). Replace with: "Entropy is higher where a genotype tested in only one country enters the top three. EAP 9508-93, tested only in Honduras, is predicted in the top three in much of Costa Rica, which makes it a candidate for new trials there but not a direct recommendation."

2. **Wrong genotypes named as winners under warm conditions (Contradicted).** The card says heat- and drought-tolerant genotypes "such as ALS 0532-6, SX 14825-7-1 and SRC 2-18-1 performed better under warmer conditions." The source says the top three in the warm node (more than 4 days above the 90th percentile) are IBC 308-24, MHC 2-13-49 and SX 14825-7-1 (p. 2256, PDF 11). In Figure 3 (p. 2257, PDF 12) ALS 0532-6 has a lower log-worth in the warm node (about -0.2) than in the less warm node (about -0.05). These are approximate values read off the chart. ALS 0532-6, SX 14825-7-1 and SRC 2-18-1 are discussed later as the most reliable top three in the maps (p. 2258, PDF 13), not as the tree result. Also, SRC 2-18-1 is listed as heat tolerant only, not drought tolerant (Table 10, p. 2261, PDF 16). Replace the sentence with: "The pruned tree made a single split, on WSDI. Where warm spells lasted more than 4 days, IBC 308-24, MHC 2-13-49 and SX 14825-7-1 ranked highest, and BRT 103-182 went from good to poor. This matches knowledge that high temperature limits common bean."

3. **Apante c index wrong (Contradicted, in Summary and Key numbers).** The card gives 0.563 for both Postrera and Apante. The source gives 0.563 (SE 0.012) for Postrera and 0.625 (SE 0.013) for Apante (p. 2257, PDF 12). Summary replacement: "The Primera model predicted well (c index 0.808), while the Postrera (0.563) and Apante (0.625) models were weak but better than a fixed planting date." Key numbers replacement rows:
   - `| 0.563 | c index, Postrera planting-date model | This paper |`
   - `| 0.625 | c index, Apante planting-date model | This paper |`

4. **Plots called participants, and wrong minimum (Contradicted, in Methods and Key numbers).** The card says "trial sizes from 17 to 714 participants". Table 1 gives the number of plots per trial, from 14 (CRI_05_2018) to 714 (HND_10_2017) (p. 2249, PDF 4). The source does not count participants. Methods replacement: "- **Data.** 14 tricot trials, 2015–2018, four countries, five organizations (INTA, UCR, CATIE, FIPAH, PRR), 14 to 714 plots per trial, 1,871 plots in total (sum of Table 1, card's own calculation, which matches the node sizes 1,264 + 607 in Figure 3). Farmers ranked the three genotypes on several traits, but only the overall performance ranking was analyzed." Key numbers replacement rows:
   - `| 14–714 | Plots per trial (Table 1) | This paper |`
   - `| 1,871 | Plots in total, sum of Table 1 (card's own calculation, matches Figure 3 node sizes 1,264 + 607) | This paper |`

5. **Reason for 27 to 17 reduction wrong (Contradicted, in Summary, Methods and Key numbers).** The card says harmonizing names reduced 27 genotypes to 17. The source says names were translated into experimental line names, and then genotypes tested in only one trial were removed to avoid highly unbalanced comparisons. That removal reduced 27 to 17 (p. 2248, PDF 3). Summary replacement: "Genotype names were first translated into experimental line names. Genotypes tested in only one trial were then removed, which reduced the set from 27 to 17." Methods replacement: "- **Harmonization.** Variety names translated into experimental line names (Table 2). Genotypes tested in only one trial were removed, which reduced 27 genotypes to 17." Key numbers replacement: `| 27 → 17 | Genotypes before and after removing those tested in only one trial (after name harmonization) | This paper |`

6. **"Height-related term" is wrong (Contradicted).** The fourth selected covariate is hts_mean_19_flo (p. 2256, PDF 11). Table 4 defines hts as high-temperature stress, here with daily mean temperature and a 19 °C threshold, at flowering (p. 2251, PDF 6). So two of the four selected covariates are heat indices. R20mm is "very heavy" rain days (20 mm or more), not "heavy" (Table 3). Replace with: "Forward selection with leave-one-trial-out cross-validation retained the warm spell duration index (WSDI), very heavy rain days (R20mm), the 10th percentile of night temperature and high-temperature stress at flowering."

7. **"Elevation" not among the covariates (Imprecise).** The source lists climate indices (Tables 3 and 4), SoilGrids soil variables (Table 5) and soil water content (p. 2250, PDF 5). Elevation is not a covariate. Replace "using spatially explicit covariates for climate, soil and elevation" with "using spatially explicit climate and soil covariates".

8. **"Split first on WSDI" implies more splits (Imprecise).** The AIC-pruned tree has only one split, on WSDI at more than 4 days (p = 0.019), giving two terminal nodes (Figure 3, p. 2257, PDF 12). Covered by the replacement in fix 2.

9. **Planting dates modelled only on rainfall (Imprecise, Summary and Methods).** The final Postrera model uses daily rainfall and daily solar radiation flux, the Apante model uses daily rainfall, and only Primera uses accumulated rainfall (Table 8, p. 2257, PDF 12). Summary replacement: "They modelled them with Cox survival models on rainfall and solar radiation, with season-specific start dates." Methods replacement: "- **Planting dates.** Cox models with time-dependent covariates, one per season, with observation starting 1 April (Primera), 1 August (Postrera) and 1 October (Apante). Final covariates: accumulated rainfall (Primera), daily rainfall and solar radiation (Postrera), daily rainfall (Apante)."

10. **SRC 2-18-1 pattern given for all seasons (Imprecise).** The source states the Costa Rica exception for the Primera season only (p. 2258, PDF 13). In the Apante map, SRC 2-18-1 leads the top three across most of the region, including Costa Rica (Figure 6a, p. 2260, PDF 15, read off the map). Covered by the new fourth summary paragraph below, which uses the source's own statement about the most reliable rankings across seasons.

11. **Stated limitation on one-country genotypes too strong (Imprecise).** The source does not say these genotypes "cannot be generalized". It says predictions for them carry higher entropy, so they point to candidates for evaluation, not direct recommendations (p. 2258 and p. 2262, PDF 13 and 17). Replace with: "- Genotypes tested in only one country get higher-entropy predictions elsewhere, so the maps point to candidates for new trials, not direct recommendations."

12. **Missing stated limitations (Omission).** Add these bullets:
    - "- A single Plackett-Luce tree can be unstable. The authors chose it for interpretability and suggest ensembles (Plackett-Luce forests) for future work."
    - "- The planting-date models are a first, ad hoc approximation. Start of the observation period, sample size and covariates need refinement."
    - "- No environmental factor besides heat (WSDI) was identified. More covariates and interactions may be found with machine-learning methods."

13. **Emphasis on naming and ClimMob (Imprecise).** The source calls variety naming "a challenge", not the main obstacle, and supports coordinated regional releases plus an open database of harmonized variety names, not "coordinated regional naming" (p. 2262, PDF 17). ClimMob helped standardize the data, but curation was still needed (p. 2248, PDF 3). Replace with: "ClimMob's standardized data collection made the datasets compatible, though curation was still needed. A key challenge was that one variety carries different names in different countries, so the authors support coordinated regional releases and a shared database of harmonized names. They expect the method to apply to other crops and regions."

14. **"Yield data" not in source (Imprecise, low).** The source speaks of incompatible formats, scales and designs, not yield specifically (p. 2247, PDF 2). Replace with: "Rankings can be aggregated across trials without converting data from different scales or designs."

15. **Author list wrong order and incomplete (Metadata).** The card order does not match the PDF. It misses Leida Mercado and Jonathan Steinke, and "and co-authors" suggests more names when the list is complete at 18 (p. 2246 and "How to cite", p. 2266, PDF 1 and 21). Replace with: `authors: Brown D, de Bruin S, de Sousa K, Aguilar A, Barrios M, Chaves N, Gómez M, Hernández JC, Machida L, Madriz B, Mejía P, Mercado L, Pavón M, Rosas JC, Steinke J, Suchini JG, Zelaya V, van Etten J`. Then delete the Notes line "The author list in the PDF is long. Check the full list before citing."

16. **Data field (Metadata).** The data availability statement gives a repository (p. 2263, PDF 18). Replace with: `data: R code and data to replicate the results at https://github.com/AgrDataSci/Data_synthesis_bean_tricot_CA`

17. **not_established missing (Metadata).** Add: `not_established: that the environmental covariates greatly improve prediction of farmer rankings (cross-validated gains over the no-covariate model were small); that heat is the only factor driving bean variety performance in Central America; that the maps are direct variety recommendations for genotypes tested in only one country; that the planting-date models are accurate for the Postrera and Apante seasons; that predictions hold outside the area of applicability; that the maps were validated with new independent trials; that results for overall performance hold for single traits such as yield`

18. **Add key results to Key numbers (Omission).** Suggested rows:
    - `| > 4 days | WSDI split in the Plackett-Luce tree (p = 0.019), Node 2 n = 1,264 plots, Node 3 n = 607 plots | This paper |`
    - `| 6,183 vs 6,033 | Cross-validated deviance, no-covariate vs environmental-covariate model (pseudo-R2 0.6679 vs 0.6831, Kendall's W 0.5203 vs 0.5215) | This paper |`
    - `| 10 of 14 | Trials that tested ALS 0532-6, the genotype with the most certain top-three predictions | This paper |`
    - `| 2000–2019 | Years over which seasonal predictions were averaged, on a grid of about 11 × 11 km | This paper |`
    - `| r = 0.09 | Correlation between WSDI and maximum night temperature (p = 1 × 10−4) | This paper |`
    - Change the ~0.5% row context to: `| ~0.5% | Increase per mm of daily accumulated rainfall in the rate of planting, Primera (hazard ratio 1.005, see Notes) | This paper |`

19. **Notes and relations (Improvement).** Replace the first note with: "- Heat as the main driver agrees with vanetten-2019-pnas, which found maximum night temperature most important in the Nicaragua trials, a subset of this dataset. In this paper WSDI and maximum night temperature correlate only weakly (r = 0.09, p. 2256)." Add the source-issue notes listed below. Add to frontmatter:
    ```
    relations:
      - extends: vanetten-2019-pnas  # pools the Nicaragua trials analysed there with trials from three more countries
    ```

### Suggested full replacement Summary (497 words)

The paper shows how to synthesize tricot data from heterogeneous sources into location-specific information for variety decisions. Rankings can be aggregated across trials without converting data from different scales or designs. The study pools 14 red common bean trials run between 2015 and 2018 by five organizations in Costa Rica, El Salvador, Honduras and Nicaragua, with 1,871 plots in total. Only the farmers' overall performance ranking was analyzed.

Genotype names were first translated into experimental line names. Genotypes tested in only one trial were then removed, which reduced the set from 27 to 17. The rankings were analyzed with Plackett-Luce trees, using spatially explicit climate and soil covariates. Forward selection with leave-one-trial-out cross-validation retained the warm spell duration index (WSDI), very heavy rain days (R20mm), the 10th percentile of night temperature and high-temperature stress at flowering. These covariates improved the cross-validated fit only slightly, and adding latitude and longitude made it worse. The pruned tree made a single split, on WSDI. Where warm spells lasted more than 4 days, IBC 308-24, MHC 2-13-49 and SX 14825-7-1 ranked highest, and BRT 103-182 went from good to poor. This matches knowledge that high temperature limits common bean.

To predict across the region, the authors needed planting dates for every grid cell and season. They modelled them with Cox survival models on rainfall and solar radiation, with season-specific start dates. The Primera model predicted well (c index 0.808), while the Postrera (0.563) and Apante (0.625) models were weak but better than a fixed planting date. Predictions for each cell of about 11 km, averaged over 2000 to 2019, produced maps of the top three genotypes per season, with entropy maps for uncertainty and an area of applicability flagging conditions not covered by the trials.

Seven genotypes make up the top three across seasons. The most reliable predictions, with the lowest entropy, are where SRC 2-18-1, SX 14825-7-1 and ALS 0532-6 form the top three. All three tolerate heat, and the last two also drought. Entropy is higher where a genotype tested in only one country enters the top three. EAP 9508-93, tested only in Honduras, is predicted in the top three in much of Costa Rica, which makes it a candidate for new trials there but not a direct recommendation. ALS 0532-6, tested in 10 of 14 trials, is a good candidate for introduction in Costa Rica, El Salvador and Nicaragua.

Pooling trials exploits a spread of locations and seasons that single trials cannot offer. The maps can help breeders target new testing locations and help extension agents make recommendations, while entropy and the area of applicability capture two kinds of uncertainty, in the rankings and in the environment. ClimMob's standardized data collection made the datasets compatible, though curation was still needed. A key challenge was that one variety carries different names in different countries, so the authors support coordinated regional releases and a shared database of harmonized names. They expect the method to apply to other crops and regions.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Rank-based data synthesis of common bean on-farm trials across four Central American countries | Same (p. 2246, PDF 1) | Supported |
| authors | Brown D, Barrios M, de Bruin S, ... van Etten J, and co-authors | 18 authors in a different order. Mercado L and Steinke J missing (p. 2246 and p. 2266, PDF 1 and 21) | Imprecise. See fix 15 |
| year | 2022 | Published online 24 October 2022, volume 62 (p. 2246, PDF 1) | Supported |
| journal | Crop Science | Crop Science (p. 2246, PDF 1) | Supported |
| article | 62(6), 2246-2266 | Crop Science 2022, 62:2246–2266, issue 6 (download line) (p. 2246, PDF 1) | Supported |
| type | research article | "Original Research Article" (p. 2246, PDF 1) | Supported |
| doi | https://doi.org/10.1002/csc2.20817 | 10.1002/csc2.20817 (p. 2246, PDF 1) | Supported |
| license | CC BY | Creative Commons Attribution License, no version stated (p. 2246, PDF 1) | Supported |
| data | see the data availability statement | GitHub repository AgrDataSci/Data_synthesis_bean_tricot_CA (p. 2263, PDF 18) | Imprecise. See fix 16 |
| crops | common bean | Red common bean, Phaseolus vulgaris (p. 2247 and 2248, PDF 2 and 3) | Supported |
| region | Costa Rica, El Salvador, Honduras, Nicaragua | Same (p. 2247, PDF 2) | Supported |
| gist | Pools 14 tricot common bean trials ... heat the main driver and mapping variety performance by season | Conclusions name WSDI, a proxy for heat, as the main abiotic factor, and maps are per season (p. 2262, PDF 17) | Supported. 26 words, states findings |
| not_established | missing | Several stretchable claims exist (small model gains, weak Postrera and Apante planting models, one-country genotypes, no new validation trials) | Missing. See fix 17 |

Other fields: source: team is consistent with people.md (Kauê de Sousa, Jacob van Etten). software lists PlackettLuce and gosset, both used (p. 2248, PDF 3). The template asks for CRAN links and versions there, which are absent, but the field is optional.

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Metadata | title | Supported | p. 2246 (PDF 1) | |
| 2 | Metadata | authors | Imprecise | p. 2246, 2266 (PDF 1, 21) | Wrong order, 2 missing |
| 3 | Metadata | year 2022 | Supported | p. 2246 (PDF 1) | |
| 4 | Metadata | journal | Supported | p. 2246 (PDF 1) | |
| 5 | Metadata | article 62(6), 2246-2266 | Supported | p. 2246 (PDF 1) | |
| 6 | Metadata | type | Supported | p. 2246 (PDF 1) | |
| 7 | Metadata | doi | Supported | p. 2246 (PDF 1) | |
| 8 | Metadata | license CC BY | Supported | p. 2246 (PDF 1) | |
| 9 | Metadata | data | Imprecise | p. 2263 (PDF 18) | Repository URL available |
| 10 | Metadata | crops | Supported | p. 2247 (PDF 2) | |
| 11 | Metadata | region | Supported | p. 2247 (PDF 2) | |
| 12 | Metadata | gist | Supported | p. 2262 (PDF 17) | |
| 13 | Summary | Shows how to synthesize tricot data from heterogeneous sources into location-specific information | Supported | Abstract, p. 2247 (PDF 2) | |
| 14 | Summary | Trials expensive and local, rankings aggregate without scaling problems of yield data | Imprecise | p. 2246–2247 (PDF 1–2) | Source says formats, scales and designs, not yield. Fix 14 |
| 15 | Summary | 14 trials, 2015–2018, several organizations, four countries | Supported | p. 2248, Table 1 p. 2249 (PDF 3–4) | Five organizations in four teams |
| 16 | Summary | Harmonizing names reduced 27 to 17 genotypes | Contradicted | p. 2248 (PDF 3) | Reduction came from removing single-trial genotypes. Fix 5 |
| 17 | Summary | PL model and recursive partitioning with climate, soil and elevation covariates | Imprecise | p. 2248–2250, Tables 3–5 (PDF 3–7) | No elevation covariate. Fix 7 |
| 18 | Summary | Forward selection kept WSDI, heavy-rain days, low-temperature percentile, height-related term | Contradicted | p. 2256 (PDF 11), Table 4 p. 2251 (PDF 6) | hts = high-temperature stress at flowering. R20mm = very heavy rain. Fix 6 |
| 19 | Summary | Tree split first on WSDI | Imprecise | Figure 3, p. 2257 (PDF 12) | Only one split. Fix 8 |
| 20 | Summary | Matches knowledge that high temperature limits common bean | Supported | p. 2256 (PDF 11) | |
| 21 | Summary | ALS 0532-6, SX 14825-7-1, SRC 2-18-1 performed better under warmer conditions | Contradicted | p. 2256 (PDF 11), Figure 3 p. 2257 (PDF 12), Table 10 p. 2261 (PDF 16) | Warm-node top three: IBC 308-24, MHC 2-13-49, SX 14825-7-1. ALS lower in warm node (approx., from chart). SRC heat tolerant only. Fix 2 |
| 22 | Summary | Cox survival models on rainfall, season-specific start dates | Imprecise | p. 2254, Table 8 p. 2257 (PDF 9, 12) | Postrera model also uses solar radiation. Fix 9 |
| 23 | Summary | Primera c index 0.808 | Supported | p. 2257 (PDF 12) | SE 0.03 |
| 24 | Summary | Postrera and Apante weaker (0.563) | Contradicted | p. 2257 (PDF 12) | Apante is 0.625. Fix 3 |
| 25 | Summary | Node membership maps of top three, entropy maps, AOA | Supported | p. 2255, 2258 (PDF 10, 13) | |
| 26 | Summary | SRC 2-18-1 in top three across most of the region except much of Costa Rica | Imprecise | p. 2258 (PDF 13), Figures 4–6 | Stated for Primera only. Fix 10 |
| 27 | Summary | EAP 9508-93 appears only where tested | Contradicted | p. 2262 (PDF 17), Figure 4a p. 2259 (PDF 14) | Predicted in top three in most of Costa Rica, tested only in Honduras. Fix 1 |
| 28 | Summary | Authors conclude synthesis gives recommendation maps and supports release decisions, if AOA respected | Supported | Abstract p. 2247, p. 2255, 2258 (PDF 2, 10, 13) | "Provided" clause is a fair reading of the AOA role |
| 29 | Summary | Pooling exploits spread of locations and seasons | Supported | p. 2262 (PDF 17) | |
| 30 | Summary | Maps help breeders and extension, entropy and AOA give two kinds of uncertainty | Supported | p. 2262 (PDF 17) | |
| 31 | Summary | ClimMob's standardized collection makes synthesis feasible | Imprecise | p. 2248, 2262 (PDF 3, 17) | Curation was still needed. Fix 13 |
| 32 | Summary | Main obstacle was different variety names | Imprecise | p. 2262 (PDF 17) | Source says "a challenge". Fix 13 |
| 33 | Summary | Authors call for coordinated regional naming | Imprecise | p. 2262 (PDF 17) | Source: coordinated regional releases and a harmonized-name database. Fix 13 |
| 34 | Summary | Method expected to apply to other crops and regions | Supported | p. 2262 (PDF 17) | |
| 35 | Methods | 14 trials, partners, 17 to 714 participants | Contradicted | Table 1, p. 2249 (PDF 4) | 14 to 714 plots. Fix 4 |
| 36 | Methods | Names standardized, 27 reduced to 17 | Contradicted | p. 2248 (PDF 3) | Fix 5 |
| 37 | Methods | PL trees, forward selection, blocked cross-validation | Supported | p. 2253 (PDF 8) | Leave-one-trial-out |
| 38 | Methods | Cox models against daily accumulated precipitation | Imprecise | Table 8, p. 2257 (PDF 12) | DAP only in Primera. Fix 9 |
| 39 | Methods | Node membership per season, top-three maps, entropy, AOA | Supported | p. 2254–2255 (PDF 9–10) | |
| 40 | Limitations | Planting-date models weak for Postrera and Apante | Supported | p. 2257 (PDF 12) | |
| 41 | Limitations | Predictions unreliable outside AOA | Supported | p. 2255, 2258 (PDF 10, 13) | |
| 42 | Limitations | One-country genotypes cannot be generalized | Imprecise | p. 2258, 2262 (PDF 13, 17) | Source: higher entropy, candidates for testing. Fix 11 |
| 43 | Key numbers | 14 trials | Supported | Table 1, p. 2249 (PDF 4) | |
| 44 | Key numbers | 2015–2018 | Supported | Table 1, p. 2249 (PDF 4) | |
| 45 | Key numbers | 4 countries | Supported | p. 2247 (PDF 2) | |
| 46 | Key numbers | 27 → 17 after name harmonization | Contradicted | p. 2248 (PDF 3) | Fix 5 |
| 47 | Key numbers | 17–714 participants per trial | Contradicted | Table 1, p. 2249 (PDF 4) | Fix 4 |
| 48 | Key numbers | 0.808 Primera | Supported | p. 2257 (PDF 12) | |
| 49 | Key numbers | 0.563 Postrera and Apante | Contradicted | p. 2257 (PDF 12) | Fix 3 |
| 50 | Key numbers | ~0.5% per mm, Primera | Supported | p. 2256, Table 8 p. 2257 (PDF 11–12) | Matches source wording. See source issue 2 |
| 51 | Notes | Heat as main driver consistent with vanetten-2019-pnas | Supported | p. 2256 (PDF 11) | Add r = 0.09. Fix 19 |
| 52 | Notes | Author list is long | Supported | p. 2246 (PDF 1) | Delete once authors fixed |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| By the authors' own rule (test passed when p is nonsignificant), the Apante planting model violates the proportional hazard assumption (p = .013). The text does not discuss it. The Postrera global test (p = .0016) is called only a "moderate" violation. | Table 9 and text, p. 2257–2258 (PDF 12–13) | No | "- Table 9 shows that the Apante planting-date model also fails the proportional hazard test (p = .013), which the text does not discuss (p. 2258)." |
| The source reads the hazard ratio 1.005 per mm as a ~0.5% increase in the "probability of planting". Strictly it is a ~0.5% increase in the daily rate (hazard) of planting. | p. 2256, Table 8 p. 2257 (PDF 11–12) | No. The card repeats "planting probability". | "- The ~0.5% per mm figure for Primera is a hazard ratio (1.005). The source describes it as a change in planting probability (p. 2256), but it is a change in the daily rate of planting." |
| WSDI is defined as the maximum length of a warm spell (consecutive days above the 90th percentile) in Table 3, but as the number of days above the 90th percentile in the results text. | Table 3 p. 2251, text p. 2256 (PDF 6, 11) | No | "- The source defines WSDI as the longest warm spell in Table 3 (p. 2251) but as the number of days above the 90th percentile in the results (p. 2256). The tree split is at 4 days." |
| Table 3 gives °C as the unit for SU and TR, which are counts of days. TR is defined with maximum temperature above 25 °C, which is unusual for tropical nights. | Table 3, p. 2251 (PDF 6) | No | Low importance. No Notes text needed. |
| Trial HND_10_2017 has a median planting date of 20 September 2017, while its ID suggests October. | Table 1, p. 2249 (PDF 4) | No | Low importance. No Notes text needed. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: show applicability of rank-based synthesis, with four specific objectives (integrate, identify factors, predict per season, assess uncertainty) | Yes, broadly | Medium | None needed |
| Tree result: single WSDI split at > 4 days (p = 0.019), Node 2 n = 1,264, Node 3 n = 607, warm-node top three IBC 308-24, MHC 2-13-49, SX 14825-7-1, BRT 103-182 crossover | No, and wrong genotypes given | High | Fix 2 and Key numbers row in fix 18 |
| Model validation: environmental covariates improve deviance, pseudo-R2 and Kendall's W only slightly over no covariates, geolocation models worse (Table 7) | No | High | Summary sentence in replacement summary, Key numbers row in fix 18, not_established in fix 17 |
| Map results: seven genotypes in top three, most reliable rankings SRC 2-18-1, SX 14825-7-1, ALS 0532-6 with lowest entropy, ALS 0532-6 tested in 10 of 14 trials and a good candidate for Costa Rica, El Salvador, Nicaragua, EAP 9508-93 a candidate for Costa Rica | No (and EAP claim reversed) | High | Fourth paragraph of replacement summary |
| Only the overall performance ranking was analyzed, although farmers ranked several traits | No | High | Methods bullet in fix 4 and first paragraph of replacement summary |
| Sample size in plots (1,871 total) | No | Medium | Fix 4 |
| Predictions averaged over 20 years (2000–2019) on a grid of about 11 km | No | Medium | Replacement summary and Key numbers row |
| Authors' limitations: single-tree instability, ad hoc planting-date models, no factor beyond heat found | No | Medium | Fix 12 |
| Weak correlation of WSDI with maximum night temperature (r = 0.09), and WSDI may be more generalizable or capture more than heat | No | Medium | Notes in fix 19 |
| AOA: non-applicable areas are mostly unsuitable for beans (Talamanca, Indio Maíz, Honduran reserves), trials jointly cover most bean-growing conditions | No | Medium | Optional Notes line: "- Areas outside the area of applicability are mostly unsuitable for beans, such as the Talamanca range and Indio Maíz reserve. The trials jointly cover most bean-growing conditions in Central America (p. 2258)." |
| Apante season: MHC 2-13-49 third over a larger area, coastal areas applicable but high entropy | No | Low | None needed |
| Future steps: Plackett-Luce forests, combining tricot and non-tricot data, methods fed into gosset | No | Low | Optional Notes line: "- The authors propose Plackett-Luce forests and combining tricot with non-tricot trial data as next steps. Their methods are being added to gosset (p. 2262)." |
| Data cleaning: planting-date outliers beyond ±40 days replaced by trial median, growing periods outside 60–120 days dropped, missing coordinates set to community median | No | Low | Optional Methods addition |
| Authors' claim of first use of a Cox model with time-dependent covariates to predict planting dates | No | Low | None needed |

## Template compliance

- Summary word count: 407 (within 400 to 500). The suggested replacement has 497 words.
- Gist: 26 words (under 30). It states a finding, not only topics.
- Keywords: 11 (within 8 to 12).
- Questions: 5 (within 4 to 7). Optional sixth question: "Which bean genotypes are good candidates for testing or introduction in other Central American countries?"
- House style: tricot is lowercase throughout. maniva does not appear. No em dashes or semicolons in the card prose.
- not_established is missing (fix 17). relations is empty though vanetten-2019-pnas analysed a subset of the same trials (fix 19).
