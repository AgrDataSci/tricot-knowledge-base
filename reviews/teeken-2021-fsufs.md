# Card review: teeken-2021-fsufs

- **Card:** papers/teeken-2021-fsufs.md
- **Source:** papers-pdf/teeken-et-al-2021.pdf (13 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 48 (13 frontmatter, 35 body) |
| Supported | 36 |
| Imprecise | 9 |
| Not in source | 3 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 7 |
| Important omissions | 8 |
| Metadata issues | 2 |

The card is accurate on the main results. The numbers it reports match the paper's text, and the summary follows the paper's own argument closely. The most important fixes are these. The "Stated limitations" section lists two points that the authors never state and misses the limitations they do state (p4, p9). The 204% row should name the trait, which the paper gives on p7. The paper also has several internal inconsistencies that the card does not flag. The most serious is that it defines "poor" and "non-poor" in opposite ways in different places (p4, p6, p7, Table 4 on p8).

## Fixes needed

1. **Stated limitations are partly invented and miss the real ones.** The card lists "uses stated trade-offs ... not on-farm evaluation" and "results are specific to gari and cassava in Nigeria". These are true about the design, but the authors do not state them as limitations. The first bullet is also off target. On p6 the authors say the odds-ratio analysis reduces the risk of reading spurious correlations from the exploratory correlation analysis (traits against social variables). They do not say that correlations between traits are spurious, and the comparisons are not described as "planned". The limitations the authors do state are on p4 (merging the HFIAS categories "could potentially mask" more nuanced analysis) and on p9 (Figure 2 caption: no food-secure, non-poor men from the South South or South East). Replace the whole section with:

   ```
   - The authors treat the correlation analysis as exploratory and warn that it may contain spurious associations, so they base their main comparisons on odds ratios for gender, region, food security and poverty.
   - Food security and poverty were each reduced to two groups to keep the interaction analysis manageable. The authors note that merging the HFIAS categories into "food secure" and "food insecure" could mask more nuanced effects.
   - No food-secure, non-poor men from the South South or the South East were among the respondents, so these groups are missing from the gender comparisons in the heatmap.
   ```

   The two dropped points are already covered by not_established (see fix 7).

2. **204% row does not name the trait, and the note says to check the PDF.** The paper states it on p7 and in Table 3 (p7): root color was 204% more likely to be ranked low in the South South than in the North Central. This matches Table 2 (OR 3.043). Replace the row with:

   `| 204% | Higher odds of ranking root color low in the South South than in the North Central | This paper |`

   Delete the Notes bullet "The 204% figure refers to a single trait in the text. Check the PDF for which trait before citing." Replace it with the source-issue notes in the "Source issues" section below.

3. **North Central sentence is more certain than the source.** The card says: "More commercial markets in the North Central zone favored larger roots." The source (p10) says the priority on root size and maturity time in North Central "may equally be explained" by more commercial markets that demand larger roots. Replace with:

   `In the North Central zone, root size ranked higher, which the authors suggest may reflect more commercial markets that demand larger roots.`

4. **Conclusions paragraph is slightly overstated and leaves out key conclusions.** The source (p10) says the results "confirm the opportunity" to prioritize gari quality traits, and links this to gender equality goals, not to "more vulnerable users". The source's conclusions on p11 also name gari texture as the most cross-cutting trait, in-ground storability as a food security trait, the idea of "non-negotiable" traits, and regionally focused breeding pipelines. None of these is in the card. Replace the sentence "Breeding programmes should prioritize gari quality traits such as color, taste, texture and swelling, and invest in high-throughput phenotyping and genetic studies for them, so that new varieties serve more vulnerable users." with:

   `They see an opportunity to prioritize gari quality traits, especially color, taste, texture and swelling, supported by high-throughput phenotyping and genetic studies. Gari texture was the most cross-cutting trait. Quality traits and in-ground storability matter most for poor and food-insecure households, and regional trait groupings could support regionally focused breeding pipelines.`

   If space allows, add to Notes: `- The authors suggest labelling traits that matter across all groups, such as gari texture, as "non-negotiable" in product profiles (p11).`

5. **Notes bullet 1 states outside knowledge as fact.** "the trait preference evidence behind IITA's cassava product profiles and the tricot work in ..." is not in the source. The source only says the results "can inform" product profiles (p11). The three linked cards do not cite this paper. Replace with:

   `- Not a tricot trial. Curator's note, not from this paper: related IITA cassava work in Nigeria by overlapping authors uses tricot to test varieties and gari-eba with users. See teeken-2023-slides, olaosebikan-2023-jsfa and alamu-2023-jsfa.`

6. **data field is vague.** The paper's Data Availability Statement (p11) gives the IITA CKAN repository and a dataset DOI. Replace with:

   `data: IITA CKAN repository (data.iita.org), https://doi.org/10.25502/RHJ9-2228/D, code not stated`

7. **not_established is thin.** It misses the most likely over-readings: treating associations as causal, citing the poor versus non-poor result as if the groups were clearly defined, and assuming women everywhere rank quality over yield. Replace with:

   `not_established: results of a tricot trial or of on-farm variety testing (it is a 1000minds and RHoMIS stated-preference survey); trait preferences for crops other than cassava, for cassava products other than gari, or for places outside Nigeria; causal effects of gender, poverty or food security on trait preferences (the analyses show associations); a clear poor versus non-poor contrast (the paper defines the PPI groups inconsistently); that women in every region rank quality traits above yield (in the South South and South East women ranked fresh root yield higher than men)`

8. **"the main cassava food product" overstates.** The source calls gari "a major food product" (p1) and says gari and fufu are "the two major food products" (p2). Replace "with a focus on gari, the main cassava food product." with:

   `with a focus on gari, a major cassava food product.`

9. **Analysis bullet leaves out the trait-social correlations and the model.** Pearson correlations were run both among traits (Table 1A) and between traits and social characteristics (Table 1B). Odds ratios came from a cumulative logit model in SAS. Replace the Analysis bullet with:

   `- **Analysis.** Pearson correlations among the 11 trait ranks and between ranks and social characteristics (SPSS). Odds ratios of ranking a trait low from a cumulative logit model (SAS), comparing men and women, food insecure and food secure, poor and non-poor, and the four regions. Wilcoxon rank-sum tests of gender differences within each of these groups (R).`

10. **Recommended additions for completeness (see Completeness table).** Suggested text to add to the Summary. With fixes 3, 4 and 8 applied, the Summary comes to about 481 words, within the 500 limit:

   - After the sentence on women and root color and gari traits, add: `Men were 26% to 41% less likely to rank root size, in-ground storability, disease resistance and maturity time low.`
   - At the end of the Region paragraph, add: `Gender gaps also varied by region, and in the South South and South East women ranked fresh root yield higher than men.`

   Add to Methods: `- **Traits.** 11 traits (gari taste, texture, color and swelling, fresh root yield, root size, dry matter, in-ground storage, disease resistance, root color, maturity time), chosen from literature and expert input and checked in community focus groups.` and amend Sample to `792 respondents (310 men, 482 women), 16 communities in eight states across four zones of Nigeria, February to March 2020.`

   Add to Key numbers:

   ```
   | 35% / 28% / 26% / 41% | How much less likely men were to rank low root size / in-ground storage / disease resistance / maturity time | This paper |
   | 43% | Higher odds that non-poor respondents rank gari texture low compared with poor respondents (the only trait that differed by poverty) | This paper |
   | 11 | Traits ranked by each respondent | This paper |
   ```

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Beyond "women's traits". Exploring how gender, ... | Beyond "Women's Traits": Exploring How Gender, ... (p1) | Supported (colon to period is expected) |
| authors | Teeken B, Garner E, ... Tufan HA (11) | Same 11 authors in same order (p1) | Supported |
| year | 2021 | Published 14 December 2021 (p1) | Supported |
| journal | Frontiers in Sustainable Food Systems | Same (p1) | Supported |
| article | 5, 740926 | Vol 5, Article 740926 (p1) | Supported |
| type | research article | "Original Research" (p1) | Supported |
| doi | https://doi.org/10.3389/fsufs.2021.740926 | Same (p1) | Supported |
| license | CC BY | "Creative Commons Attribution License (CC BY)" (p13). Funding note names CC BY 4.0 (p11) | Supported. Optional: "CC BY 4.0" |
| data | see the data availability statement | IITA CKAN, DOI 10.25502/RHJ9-2228/D (p11) | Imprecise (fix 6) |
| crops | cassava (gari) | Cassava, gari value chain (p1, p3) | Supported |
| region | Nigeria (South West, South East, South South, North Central) | Four zones, eight states (p3, Figure 1 p4) | Supported. Optional: add states Ogun, Osun, Kogi, Benue, Delta, Akwa Ibom, Anambra, Imo |
| gist | Survey of 792 ... women favor gari quality traits and men productivity traits, with gaps widening among food-insecure households and varying by region | Abstract (p1), p6, p8 | Supported (26 words) |
| not_established | tricot trial, other crops or places | Design (p3) | Imprecise: correct but weak (fix 7) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Programmes need user-group data for customer and product profiles, yet many studies only compare women and men | Supported | Abstract (p1), Intro (p2) | |
| 2 | Summary | Paper asks how gender interacts with poverty, food security, household traits and region, focus on gari, "the main cassava food product" | Imprecise | p1 "a major food product", p2 gari and fufu are the two major products | Fix 8 |
| 3 | Summary | 1000minds pairwise trade-offs combined with adapted RHoMIS with HFIAS and PPI | Supported | p3 | Methods call it "Progress out of Poverty Index", results "Poverty Probability Index" |
| 4 | Summary | 792 people, 310 men and 482 women, four regions | Supported | p3 | |
| 5 | Summary | Most food insecure, 34% severe, 45% moderate | Supported | p6 | Counts sum to 785 (source issue 2) |
| 6 | Summary | Analysed with correlations, odds ratios and Wilcoxon tests | Supported | p3 to p4 | |
| 7 | Summary | Confirms women prioritize quality traits, men agronomic and productivity traits | Supported | p1, p9 to p10 | |
| 8 | Summary | Women prioritize root color, gari taste, texture, color, swelling, men 31% to 59% more likely to rank these low | Supported | p6 text, Table 3 (p7) | Matches text and Table 3, not Table 2 (source issue 3) |
| 9 | Summary | Gender differences grew among food-insecure households | Supported | p1, p8, Table 4, p10 | |
| 10 | Summary | Food-insecure: less likely to rank texture low, more likely to rank root size and dry matter low | Supported | p6, Table 3 (p7) | |
| 11 | Summary | Poor ranked like non-poor overall, but men and women within poor households differed | Supported | p1, p7 to p8, Table 4 | See source issue 1 on group definitions |
| 12 | Summary | Women heading households prioritized quality traits more than women with a spouse | Supported | p1, p5, p10 | Rows not shown in Table 1B (source issue 6) |
| 13 | Summary | Preferences shifted toward productivity when men controlled more value | Supported | p5, Table 1B (p6), p10 | Evidence is gari traits ranked lower and maturity time higher |
| 14 | Summary | South East: quality traits and in-ground storability ranked higher, weaker market links | Supported | p1, p7, p10 | |
| 15 | Summary | South South: taste and yield high, gari and root color low, possibly because fufu more central | Supported | p10 | Hedge kept correctly |
| 16 | Summary | More commercial North Central markets favored larger roots | Imprecise | p10 "may equally be explained" | Stated as fact. Fix 3 |
| 17 | Summary | Gender analysis must be central because preferences track sex, women's roles and control of resources | Supported | p10 | Source says "should". Acceptable |
| 18 | Summary | Programmes should prioritize gari quality traits and invest in phenotyping and genetics, so varieties serve vulnerable users | Imprecise | p10, p11 | Source says "opportunity", and its rationale is gender equality goals. Misses texture, storability, regional pipelines. Fix 4 |
| 19 | Summary | Stress heterogeneity among women and among men | Supported | p1, p11 | |
| 20 | Methods | 1000minds plus adapted RHoMIS | Supported | p3 | |
| 21 | Methods | 792 respondents, four regions | Supported | p3 | |
| 22 | Methods | HFIAS and PPI | Supported | p3 to p4 | |
| 23 | Methods | Pearson among traits, odds ratios, chi-square, Wilcoxon | Imprecise | p3 to p4 | Omits trait-social correlations (Table 1B) and the cumulative logit model. Fix 9 |
| 24 | Limitations | Correlations between traits can be spurious, so authors focus on a few planned comparisons | Imprecise | p6 | Concern is the exploratory trait-social correlations. Fix 1 |
| 25 | Limitations | Stated trade-offs, not on-farm evaluation | Not in source | none | True of the design but not stated by the authors. Fix 1 |
| 26 | Limitations | Results specific to gari and cassava in Nigeria | Not in source | none | Not stated by the authors. Fix 1 |
| 27 | Key numbers | 792 (310 men, 482 women) | Supported | p3 | Table 4 totals match |
| 28 | Key numbers | 34% / 45% / 8% / 13% | Supported | p6 | Percentages fit n = 785, not 792 (source issue 2) |
| 29 | Key numbers | 35% / 51% / 31% / 59% / 44% men rank low | Supported | p6, Table 3 (p7) | Source issue 3 |
| 30 | Key numbers | 33% food insecure, texture | Supported | p6, Table 3. OR 0.668 gives 33.2% | |
| 31 | Key numbers | 57% / 41% root size / dry matter | Supported | p6, Table 3. OR 1.574 and 1.410 | |
| 32 | Key numbers | 204% one trait, SS vs NC | Imprecise | p7, Table 3. Root color, OR 3.043 | Trait not named. Fix 2 |
| 33 | Key numbers | 66% south / ~30% North Central, FAOSTAT | Supported | p3 | Attribution correct |
| 34 | Notes | Evidence behind IITA product profiles and the tricot work in three cards | Not in source | p11 says results "can inform" profiles | Outside knowledge, not labelled. The three cards do not cite this paper. Fix 5 |
| 35 | Notes | 204% refers to a single trait, check PDF | Imprecise | p7 names root color | Fix 2 |

Frontmatter claims (13) are in the Metadata table: 11 Supported, 2 Imprecise (data, not_established).

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| 1. Poor and non-poor are defined in opposite ways. Methods: PPI index below 10% = "poor". Results: 575 people below 10% = "non-poor", 217 above = "poor". Correlation text: "<PPI 10% being non-poor". Table 4: Poor N = 575 (341 women, 234 men), Non-poor N = 217. | p4, p6, p7, Table 4 (p8) | No | `- The paper defines its PPI groups inconsistently. Methods (p4) call a PPI index below 10% "poor", the Results (p6, p7) call the same group "non-poor" (575 people), and Table 4 labels 575 people "poor". Treat the poor versus non-poor results with caution.` |
| 2. HFIAS counts (265 + 352 + 63 + 105) sum to 785, not 792. Table 4 gives 112 food-secure respondents (54 women, 58 men), not 105. The 680 food-insecure respondents match. | p6, Table 4 (p8) | No | `- HFIAS counts in the text (p6) sum to 785, not 792, and Table 4 lists 112 food-secure respondents where the text gives 105.` |
| 3. The men versus women percentages in Table 3 and the text do not all match the odds ratios in Table 2. Calculated as (OR - 1) x 100: gari taste 43% (Table 3: 51%), gari color 67% (59%), swelling 48% (44%), in-ground storage -25% (-28%), disease resistance -23% (-26%), root color 38% (35%). Texture, root size and maturity time match. My own calculation. | Tables 2 and 3 (p7), p6 | No | `- Several men versus women percentages in Table 3 and the text (p6) differ from those implied by the Table 2 odds ratios (for example gari taste 51% in Table 3 against 43% from OR 1.428). The card uses the text and Table 3 values.` |
| 4. Fresh root yield: Table 2 shows a significant men versus women odds ratio (0.768, p < 0.05), but the text says there is no difference between men and women for fresh root yield, and Table 3 shows no value. | p6, Tables 2 and 3 (p7) | No | `- Table 2 marks the men versus women difference in fresh root yield as significant (OR 0.768), while the text (p6) and Table 3 report no difference.` |
| 5. The 148% for root color, South East versus South West (text and Table 3), does not match Table 2, where root color is 1.199 (not significant). The 148% matches the maturity time odds ratio (2.477) in the same row, so Table 3 may have a row shift. Other South West comparisons also differ slightly (for example NC vs SW root color -38% from OR 0.615, Table 3 -35%). The 204% value is consistent. | p7, Tables 2 and 3 (p7) | No (card does not cite 148%) | `- The 148% figure for root color in the South East versus the South West (p7, Table 3) does not match Table 2, where root color is not significant and maturity time has OR 2.477 (about 148%). Do not cite this figure without checking.` |
| 6. The text cites Table 1B for the female-headed versus couple household result, but Table 1B has no household-type rows. | p5, Table 1B (p6) | No | `- The contrast between women in female-headed households and women in couples (p5) is cited to Table 1B, but the table does not show household-type rows.` |
| 7. Table 2 gives "ns" with no odds ratio for gari color, North Central versus South West. | Table 2 (p7) | No | Low importance, no note needed |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: move beyond women-versus-men comparisons, interactions with poverty, food security, household and region | Yes | high | |
| Design: 1000minds PAPRIKA pairwise trade-offs plus adapted RHoMIS | Yes | high | |
| The 11 traits and the rank 1 to 11 output | Partly (no number, no list) | high | Fix 10 (Methods bullet, Key numbers row) |
| Sampling: 8 states, 16 communities, FGDs to verify traits and set trade-off values, sampling by value chain role, gender and social group, Feb to Mar 2020 | No | medium | Fix 10 |
| Sample size and food security distribution | Yes | high | |
| Poverty split 575 / 217, only gari texture differs (43%) | Partly (direction only) | medium | Fix 10 Key numbers row, plus source issue 1 note |
| Women's priorities with effect sizes | Yes | high | |
| Men's priorities with effect sizes (root size, storage, disease, maturity), no difference for dry matter and yield | Partly (direction only) | medium | Fix 10 |
| Wilcoxon: food-secure men and women differ only in gari taste and maturity time | Partly ("gaps widen") | medium | Optional |
| Gender by region: big gaps in South West, few in North Central, women rank yield higher in South South and South East | No | high | Fix 10, and not_established in fix 7 |
| Correlation results: larger production and farm size go with output traits, home consumption with lower root size priority, dominant ethnicity with yield | No | low | Optional |
| Heatmap (Figure 2) as summary for product profiles | No | low | Optional |
| Authors' limitations: HFIAS merged, empty groups | No | medium | Fix 1 |
| Conclusions: texture most cross-cutting, "non-negotiable" traits, in-ground storability as food security trait, regionally focused pipelines | No | high | Fix 4 |
| Conclusion: gender analysis central, recognize heterogeneity | Yes | high | |
| Data availability (dataset DOI) | No | medium | Fix 6 |

## Template compliance

- Summary word count: 410 (target 400 to 500). Pass. With fixes 3, 4, 8 and the two Summary additions in fix 10, about 481 words. Check the final count after editing.
- Gist: 26 words. Pass. It says what the paper shows.
- Keywords: 11. Pass.
- Questions: 4. Pass.
- House style: tricot in lowercase throughout. maniva not used. No em dashes found in the card. Pass.
- Long-format sections are all present.
