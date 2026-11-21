# Card review: laajaj-2020-scirep

- **Card:** papers/laajaj-2020-scirep.md
- **Source:** papers-pdf/laajaj-et-al-2020.pdf (15 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 50 |
| Supported | 45 |
| Imprecise | 5 |
| Not in source | 0 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 11 |
| Metadata issues | 2 |

The card is accurate. Every number in Key numbers matches the source, and nothing is contradicted. The main problems are gaps and a few shifts in meaning. The summary is 374 words, below the 400 word minimum. It leaves out the soybean value-cost ratio after all adjustments (0.6, Table 1, p. 6). It also leaves out the fact that the calculation adjustment barely changed the maize gain (p. 5) and the authors' main stated limitation (p. 8). The most important fix is to add the 0.6 ratio and the maize stand result, using the replacement summary in fix 1. It also says the authors recommend reporting yields only without corrections. In fact they recommend reporting results both with and without calculation adjustments (p. 8).

Page numbers below are the printed journal page numbers. They are the same as the PDF page numbers for this file.

## Fixes needed

1. **Summary is too short and misses key results (high).** The summary has 374 words (target 400 to 500). It does not give the soybean value-cost ratio after all adjustments (0.6, Table 1, p. 6, "about 0.59" in the text, p. 6). It does not say that the calculation adjustment left the maize yield increment almost unchanged because fertilized plots had 91% of stands against 79% in control plots (p. 5). It does not say that the management adjustment always lowered the increment, or that skills and wealth had no sizeable effect (p. 5). It does not give the authors' main limitation (p. 8), the review of 16 papers (p. 13) or the mention of mother-baby trials (p. 8). It also has three imprecise sentences (fixes 2 to 4). Suggested replacement for the whole Summary (496 words):

   > Agronomic trials often promise large yield gains from new inputs, yet adoption stays low and gains on farmers' own fields fall short. Rachid Laajaj, Karen Macours and IITA colleagues quantify why, focusing on how trials are run and analysed rather than on market constraints.
   >
   > They used IITA fertilizer and inoculant trials for maize and soybean with 336 farmers in 48 villages of Siaya County, Western Kenya, over three seasons. Researchers designed the trials, supplied inputs and led planting, fertilizing and harvest, while farmers managed the plots. As is common, communities nominated five "good farmers" per village to host trials. The authors added the same number of randomly selected households. They collected detailed data on management and effort on trial and neighbouring non-trial plots, soil samples from trial plots, and farmers' skills and wealth.
   >
   > They identify five discrepancies between trial estimates and real-life returns: yield calculation choices, better management on trial plots, plot selection, farmer selection, and dropout in multi-season trials.
   >
   > They regress yield increments on these factors and predict the increment for representative farmers, weighting about 94% on the randomly selected ones. Reinserting failed plots and removing density adjustments cut average yields by 30% for maize and 52% for soybean. The soybean gain fell by about the same share, but the maize gain hardly changed, because fertilized maize plots kept more plants (91% of stands against 79% in control plots). Trial plots were managed better than any other plot of the same farmers, and moving management to farmers' usual level always lowered the predicted gain. Soil adjustments raised the maize gain but lowered the soybean gain. Skills and wealth added no sizeable effect. After all adjustments, the maize package's gain was nearly unchanged, while the soybean package's gain fell to not significantly different from zero. A fixed rule-of-thumb discount could therefore wrongly keep some packages and wrongly drop others.
   >
   > The maize package kept an average value-cost ratio around 4, with about 85% of farmers covering input costs. The best soybean package looked highly profitable before adjustments (ratio about 12) but fell to about 0.6 after all adjustments, and was profitable for only 47% of farmers. Labour was not costed, so these ratios are upper bounds. Attrition mattered too, as only 33% (maize) and 41% (soybean) of farmers stayed all three seasons, and keeping only them would have overstated gains by 28% and 64%.
   >
   > The method assumes farmers would manage a new package like their best-managed other plot, so it cannot capture further changes after adoption. A review of 16 on-farm trial papers from 2018 found random farmer selection was rare and none corrected for dropout. The authors conclude that agronomists should be cautious in extrapolating from trials, report results with and without calculation adjustments, document heterogeneity, and state how farmers and plots were selected. Pointing to designs such as mother-baby trials, they suggest that testing innovations early under real-world conditions, without researcher interference, might help identify which ones are likely to be taken up at scale.

   If the curator prefers to edit the existing text instead, fixes 2 to 4 give the sentence-level changes.

2. **Recommendation on reporting is reversed in part (medium).** Card: "should report yields without density corrections and with failed plots". Source, p. 8: reporting results with and without the calculation adjustments is always feasible and recommended. The paper itself reports both. The card also adds "with randomly selected farmers" as a recommendation, which the source does not state in those words (the source asks for designs that account explicitly for plot and farmer selection, p. 8). It also drops the hedge "might help" from the abstract (p. 1). Replace the last paragraph of the current summary with:

   > The authors conclude that agronomists should be cautious in extrapolating from trials, report results with and without calculation adjustments, document heterogeneity, and state how farmers and plots were selected. Pointing to designs such as mother-baby trials, they suggest that testing innovations early under real-world conditions, without researcher interference, might help identify which ones are likely to be taken up at scale.

3. **Soil data were collected only on trial plots (medium).** Card: "collected detailed data on soils, management, effort, skills and wealth on trial and non-trial plots". Source: soil samples exist only for trial parcels (p. 4, p. 10, p. 12). Skills and wealth are farmer-level, not plot-level. Replace with:

   > They collected detailed data on management and effort on trial and neighbouring non-trial plots, soil samples from trial plots, and farmers' skills and wealth.

4. **Rule-of-thumb sentence is compressed into a different claim (low).** Card: "Soil adjustments moved the two crops in opposite directions, so a fixed rule-of-thumb discount would be wrong in both directions." Source: the required adjustment can be larger than the rule of thumb for some technologies and of opposite sign for others, so rules of thumb can lead to keeping innovations not worth adopting and dropping profitable ones (p. 2, p. 7). The soil result is one example of this, not the only basis. Replace with:

   > Soil adjustments raised the maize gain but lowered the soybean gain. A fixed rule-of-thumb discount could therefore wrongly keep some packages and wrongly drop others.

5. **Gist overstates the soybean result (low).** "wiped out the soybean package's gain" is stronger than the source, which says the gain became not significantly different from zero (p. 1, p. 5). The point estimate stayed slightly positive (33 kg/ha, label in Fig. 1, p. 4). Replace the gist with (26 words):

   > In Kenyan on-farm trials, correcting for farmer and plot selection, management and yield calculation made the soybean package's gain non-significant but left the maize gain intact

6. **R² range mixes two statistics (low).** Card: "R² roughly 19-35%". Source, p. 5: adjusted R² of the full model is 19 to 26%, and R² is 23 to 35%. Replace the limitation with:

   > Observed variables explain only part of the variation in yield increment (adjusted R² 19 to 26%, R² 23 to 35%), though many adjustments still lead to significant differences.

7. **Main stated limitations are missing (high).** Add these bullets to Stated limitations:

   > - The method assumes farmers would manage a new package like their best-managed other plot. It cannot capture further changes in practice, or deliberate choice of the most responsive plots, after real adoption. The estimates matter less where farmers can overcome their constraints, or in the long run.
   > - Soil samples exist only for trial plots, so differences between trial and non-trial plots are corrected only through survey plot characteristics, and parcel selection only partly.
   > - Causes of crop failure were known for only about half of the cases, so all failures were treated alike.
   > - Replicating the full approach needs particular selection rules, extra data and large samples. Reporting results with and without calculation adjustments is always feasible.
   > - The maize-soybean intercrop trial was contaminated (no plot received the best-bet package) and is reported only in the supplement.

8. **Methods bullets lack design details a tricot user would want (medium).** Replace the Trials, Sampling and Analysis bullets with:

   > - **Trials.** IITA researcher-designed, farmer-managed trials in Siaya County, Western Kenya, over three seasons (2014 to 2015). Each farm had six 4.5 × 5 m plots, one replicate, in a full factorial design. Best-bet packages: Mavuno fertilizer, top dressing and Phymix for maize (with local, IR or hybrid seed), and rhizobia inoculant with Sympal or Minjingu P fertilizer for soybean. A researcher led planting, fertilizer application and harvest. Farmers did land preparation and weeding, checked weekly by a village contact person.
   > - **Sampling.** 48 villages drawn at random (stratified by sub-county), 10 farmers per village: five nominated by the community and five drawn at random from the village household list. Four farmers per village ran maize trials and three ran soybean trials (336 in total). The other three ran a maize-soybean intercrop trial that was contaminated and left out of the main analysis. Non-trial plots next to the trial plot, and farmers' best-managed other plots, were used to observe usual practice.
   > - **Analysis.** Yield increments (package minus control plot) averaged over three seasons, with missed seasons imputed. Backward stepwise regressions of yield increment on management, soil, plot and farmer variables (adjusted R² as criterion, standard errors clustered by household), then predictions for representative farmers using village-size weights (about 94% on randomly selected farmers). Value-cost ratios from input costs and farmers' reported crop sale prices (labour excluded).

9. **Key numbers: add the adjusted results and name the cited sources (medium).** Change the "~4 / ~12" row context to: "Average value-cost ratio of maize / best soybean package before adjustments (Table 1: 3.9 / 12.5)". Change the Primary source of the 5-30% row to: "Sadras et al. 2015 (FAO Water Report 41) and CIMMYT 1988, as cited in this paper (refs 12, 26)". Add these rows:

   > | 3.9 / 4.0 / 4.2 | Maize value-cost ratio: agronomic calculation / without calculation adjustment / after all adjustments (Table 1) | This paper |
   > | 12.5 / 6.3 / 0.6 | Soybean value-cost ratio at the same three steps (Table 1, text gives 12 and 0.59) | This paper |
   > | 91% / 79% | Maize stands surviving in fertilized / control plots, which is why the calculation adjustment barely changed the maize gain | This paper |
   > | 71% / 88% | Share of the maize / soybean yield drop due to the plant density adjustment | This paper |
   > | 1,061 → 1,151 / 692 → 33 kg/ha | Predicted maize / soybean yield increment, agronomic calculation versus after all adjustments (data labels in Fig. 1) | This paper |
   > | 16 | On-farm trial papers from 2018 reviewed for the five discrepancies | This paper |

10. **not_established can be stronger (low).** Replace with:

    > that trial yield gains are always overestimated (adjustments went in opposite directions for the two crops); that the 30% and 52% yield drops from the calculation adjustment apply to yield gains (the maize gain barely changed); findings for variety comparisons (the maize variety contrasts were not analysed); that labour costs would not change the profitability results (labour was not costed, so ratios are upper bounds); that the soybean package fails for all farmers (47% still profited after adjustments)

11. **Notes: soften one inference and add two points (low).** Replace the first Notes bullet's opening with: "An agronomy study, not a variety trial. The authors say the same logic could be applied to other trials (p. 7). The mechanisms (selected host farmers, researcher influence, dropout) are likely relevant to variety testing too, but the paper does not test this." Add:

    > - The paper discusses mother-baby trials (Snapp et al., ref. 39 of the paper) as participatory designs that measure returns under farmers' conditions, but does not mention tricot.
    > - The maize trials also compared local, IR and hybrid seed, but the authors did not analyse variety effects because differences between seeds were small and statistical power was low (p. 11).
    > - Source issue: the text gives the soybean value-cost ratio before adjustments as 12 for the best package (p. 5), while Table 1 shows 12.5 in a single soybean column (p. 6). This card uses about 12.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Reconciling yield gains in agronomic trials with returns under African smallholder conditions | Same (p. 1) | Supported |
| authors | Laajaj R, Macours K, Masso C, Thuita M, Vanlauwe B | Same order (p. 1) | Supported |
| year | 2020 | 2020 (p. 1 footer, received June, accepted Aug 2020, p. 13) | Supported |
| journal | Scientific Reports | Scientific Reports (p. 1) | Supported |
| article | 10, 14286 | 10:14286 (p. 1 footer) | Supported |
| type | research article | Original research with methods and data (p. 1 to 13) | Supported |
| doi | https://doi.org/10.1038/s41598-020-71155-y | Same (p. 1 footer) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution 4.0 (p. 15) | Supported |
| data | openICPSR project 120430 V1 (Stata 16) | Data and code at openICPSR 120430 V1 (p. 13). Stata 16 named in figure captions (p. 4, 6, 7) | Supported |
| crops | maize, soybean | Maize and soybean, plus a contaminated intercrop trial in the supplement (p. 3, p. 9) | Supported |
| region | Western Kenya | Siaya County, western Kenya (p. 8) | Supported (could add "(Siaya County)") |
| gist | ...wiped out the soybean package's gain... | Not significantly different from zero (p. 1, p. 5) | Imprecise (fix 5) |
| not_established | three clauses | All three are consistent with the source (p. 2, p. 7, p. 11, p. 12) | Supported, but weak (fix 10) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Trials promise large gains, adoption low, real gains fall short | Supported | p. 1 | |
| 2 | Summary | Laajaj, Macours and IITA colleagues, focus on how trials are run and analysed, not market constraints | Supported | p. 1 (affiliations, aim) | Masso, Thuita, Vanlauwe are IITA |
| 3 | Summary | IITA maize and soybean trials, 336 farmers, 48 villages, three seasons | Supported | p. 3, p. 8 | 336 = 48 × 7 (4 maize + 3 soybean farmers per village). Card's own check |
| 4 | Summary | Researchers designed and supplied inputs, farmers managed | Supported | p. 3, p. 9 | A researcher also led planting, fertilizer application and harvest (p. 9). Worth adding |
| 5 | Summary | Communities nominated five "good farmers" per village, as is common | Supported | p. 3, p. 8 | Also 5 substitutes, including two women (p. 8) |
| 6 | Summary | Comparable number of random households added | Supported | p. 3, p. 8 | Exactly five per village |
| 7 | Summary | Data on soils, management, effort, skills, wealth on trial and non-trial plots | Imprecise | p. 4, p. 10, p. 12 | Soil samples on trial plots only (fix 3) |
| 8 | Summary | Five discrepancies (calculation, management, plots, farmers, attrition) | Supported | p. 3 | Source says calculation adjustments are made "sometimes" |
| 9 | Summary | Regression and prediction for representative farmers, ~94% weight on random farmers | Supported | p. 5, p. 12 | 1 − 5/85 = 94%. Card's own check |
| 10 | Summary | 30% / 52% drop in maize / soybean yields after calculation change | Supported | p. 5 | Drop is in yields, not increments |
| 11 | Summary | Maize gain nearly unchanged, soybean not significantly different from zero | Supported | p. 1, p. 5, Fig. 1 p. 4 | Fig. 1 labels: maize 1,061 to 1,151, soybean 692 to 33 kg/ha |
| 12 | Summary | Soil adjustments opposite, so fixed rule-of-thumb wrong both ways | Imprecise | p. 2, p. 5 | Rule-of-thumb argument is general, not from soil alone (fix 4) |
| 13 | Summary | Maize value-cost ratio ~4, ~85% cover input costs | Supported | p. 5, Table 1 p. 6, p. 6 | Table 1: 3.9, 4.0, 4.2 |
| 14 | Summary | Soybean ratio ~12 before, profitable for 47% after | Supported | p. 5, p. 7 | Average after adjustments (0.6) missing |
| 15 | Summary | 33% / 41% stayed three seasons, 28% / 64% overstatement | Supported | p. 7, Fig. 3 caption | |
| 16 | Summary | Conclusion: report without density corrections, random farmers, test early to identify uptake | Imprecise | p. 1, p. 8 | Source says report with and without. "Might help" hedge lost (fix 2) |
| 17 | Methods | IITA researcher-designed, farmer-managed factorial trials, best-bet packages vs control, three seasons | Supported | p. 3, p. 9 | |
| 18 | Methods | Five nominated plus comparable random farmers, non-trial plots near trial plot with same crop | Supported | p. 3, p. 8, p. 10 | Farmer-reported management uses best-managed other plot (p. 10 to 11) |
| 19 | Methods | Surveys and observation by agronomists and contacts on yields, management, effort, soils, skills, assets | Supported | p. 3, p. 10 | |
| 20 | Methods | Regressions, then predictions with village weights, value-cost ratio without labour | Supported | p. 5, p. 11 to 12 | |
| 21 | Limitations | Labour not costed | Supported | p. 7, p. 12 | Source adds that ratios are upper bounds |
| 22 | Limitations | R² roughly 19 to 35% | Imprecise | p. 5 | Adjusted R² 19 to 26%, R² 23 to 35% (fix 6) |
| 23 | Limitations | Random-farmer experiment would itself be a trial, so decomposition used | Supported | p. 3 | |
| 24 | Limitations | Not the only reason for low adoption | Supported | p. 1 | |
| 25 | Key numbers | 336 / 48 | Supported | p. 3 | |
| 26 | Key numbers | 5 nominated per village | Supported | p. 3, p. 8 | |
| 27 | Key numbers | ~94% | Supported | p. 5 | |
| 28 | Key numbers | 30% / 52% | Supported | p. 5 | |
| 29 | Key numbers | 15% / 33% missing stands | Supported | p. 5 | |
| 30 | Key numbers | ~11% / ~12% plots excluded as hazards | Supported | p. 5 | |
| 31 | Key numbers | ~4 / ~12 value-cost ratio before adjustments | Supported | p. 5, Table 1 p. 6 | Table 1 shows 3.9 and 12.5 (source issue 1) |
| 32 | Key numbers | 85% vs 47% | Supported | p. 6, p. 7 | |
| 33 | Key numbers | 33% / 41% completers | Supported | p. 7 | 67% and 59% missed at least one season |
| 34 | Key numbers | 28% / 64% overestimate | Supported | p. 7 | |
| 35 | Key numbers | 5 to 30% rule of thumb, cited | Supported | p. 2 (refs 12, 26) | Secondhand flagged. Better to name the cited sources (fix 9) |
| 36 | Notes | Agronomy study, not a variety trial, mechanism applies to any on-farm testing | Supported | p. 7, p. 11 | Second half is the card's inference. Soften (fix 11) |
| 37 | Notes | Paper does not discuss tricot | Supported | whole text | It does discuss mother-baby trials (p. 8) |
| 38 to 50 | Frontmatter | 13 fields | 12 Supported, 1 Imprecise | see Metadata check | |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Soybean value-cost ratio before adjustments is "12" for the "best performing" package in the text but 12.5 in a single "Soya" column in Table 1. It is unclear whether Table 1 pools both soybean packages | p. 5, Table 1 p. 6 | No | See fix 11 |
| Potassium threshold written as "pH < 0.160", which should be a K value | p. 9 | No | Not needed for the card |
| Phymix pH given as "6.7%" | p. 9 | No | Not needed for the card |
| Farmer allocation says "4 random farmers (2 random and 2 selected)" and "3 random farmers", using "random" for both groups | p. 8 | No | Not needed. The numbers (4 + 3 per village, 336 total) are consistent |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: unpack why trial gains differ from real-life gains, with a method to quantify it | Yes | high | |
| Design: 48 random villages, 10 farmers each, 5 nominated and 5 random | Partly (no village randomisation, no allocation 4 / 3 / 3) | medium | Fix 8 |
| Soybean average value-cost ratio 0.6 after all adjustments (6.3 after calculation adjustment) | No | high | Fix 1, fix 9 |
| Calculation adjustment barely changed the maize increment (stands 91% vs 79%), soybean increment fell proportionally, 71% / 88% of drop from density | No | high | Fix 1, fix 9 |
| Authors' main limitation: best-managed-plot assumption, cannot capture further adaptation, less relevant in the long run | No | high | Fix 7 |
| Management on trial plots significantly better than any other plot, and management adjustment always lowers the increment. Skills and wealth no sizeable effect | No | medium | Fix 1 |
| Review of 16 papers from 2018: random selection rare, plots excluded in almost half, no paper accounts for attrition, none states plant density adjustment | No | medium | Fix 1 (short), and possibly a Key numbers row (fix 9) |
| Call for reporting guidelines (selection of farmers and plots, instructions, treatment of crop failures) and for reporting with and without calculation adjustments | No (reversed in part) | medium | Fix 2 |
| Mother-baby trials named as a participatory design to learn from | No | medium | Fix 1, fix 11 |
| Maize variety contrasts not analysed (low power) | No | medium | Fix 10, fix 11 |
| Soil samples only on trial plots, so parcel selection only partly corrected. Crop failure causes known in about half of cases | No | medium | Fix 7 |
| Missing seasons imputed using seasonal differences of completers | No | low | Fix 8 |
| 79% (maize) and 65% (soybean) of farmers above the 2:1 ratio with agronomic calculations | No | low | Optional Key numbers row |

## Template compliance

- Summary word count: 374 words, below the 400 to 500 target. The replacement in fix 1 has 496 words.
- Gist: 26 words, under 30. Suggested replacement also 26 words.
- Keywords: 12, within 8 to 12.
- Questions: 6, within 4 to 7.
- House style: no capitalised "Tricot" or "Maniva" found. tricot appears in lowercase in Notes.
- Long-format sections (Questions, Methods in brief, Stated limitations) are present, so the card is long format and the summary length rule applies.
