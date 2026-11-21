# Card review: gotor-2021-fsufs

- **Card:** papers/gotor-2021-fsufs.md
- **Source:** papers-pdf/gotor-et-al-2021.pdf (17 pages. Printed page numbers match PDF page numbers.)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 54 |
| Supported | 47 |
| Imprecise | 6 |
| Not in source | 0 |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 6 |
| Important omissions | 7 (2 high, 5 medium) |
| Metadata issues | 2 |

The card is accurate on the design and on all the main effect sizes. Every number in the Key numbers table matches Table 3, and all derived percentages recompute correctly. The most important fixes are these. The sentence on who gained most in recovery capacity follows one passage of the source (page 12) but is contradicted by the Discussion and by Figure 5 (pages 12 to 13). The "Stated limitations" section leaves out the authors' own Limitations section (page 13). The card also does not say that the intervention included Farmer Field School training, which matters for anyone who wants to credit the effects to crowdsourced trials alone. The verdict is at the upper end of "Minor fixes": no main result is wrong, but the card needs about ten small edits.

## Fixes needed

1. **Recovery capacity heterogeneity (Contradicted).** The card says: "Benefits for recovery were largest among households that started with the lowest recovery capacity." The Discussion (page 13) says the effect was largest for households with intermediate prior recovery capacity. It also says the most vulnerable households benefited, and that the effect was negative for households with high prior levels. Figure 5, bottom-right panel (page 12), agrees with the Discussion. Read off the chart (approximate), the largest bar is near the 35th percentile (about +0.25 SD). The bar at the 5th percentile is small and its interval includes zero. Bars from about the 75th percentile up are negative. The Results text on page 12 instead says lower percentiles benefited "in particular". This is a source inconsistency (see Source issues), but the card's word "largest" is not supported by either passage. Replace with:
   > The gain in recovery capacity was largest for households with intermediate prior levels, and the most vulnerable also benefited, but the effect was negative for households with high prior levels.

2. **Stated limitations leave out the authors' own Limitations section (high-importance omission).** Page 13 has a section called "Limitations of the study" that the card does not use. Also, the card's bullet "Productivity and recovery are self-reported" is true (page 7), but the authors do not present it as a limitation. Replace the whole section with:
   > - No baseline or randomized control, because the programme expanded in response to local demand.
   > - Floods affected village selection in Saran and Samastipur, skewing the sample toward Vaishali.
   > - Spillovers to non-participants were ignored, so estimates are conservative.
   > - Only one pathway of the sustainable livelihoods framework was analysed (institutional change acting through livelihood strategies), and only linear relationships were tested.
   > - Other livelihood outcomes could have been included.
   > - The distribution of effects across households is not well understood, and the authors have no plausible explanation for the different patterns in rice and wheat.
   > - The citizen science trial data were not linked directly to the econometric analysis, for example to test whether some varieties reduce vulnerability more than others.

   Then add this to Notes:
   > - Productivity and recovery capacity are self-reported (page 7). The authors describe these measures but do not discuss this as a limitation.

3. **Scale figures credited to Bihar (Imprecise, Summary and Key numbers).** The Summary links "25,000 farmers and 47,000 plot-seasons" to Seeds for Needs in Bihar from 2010 to 2017. The Key numbers row says "Scale of Seeds for Needs in Bihar, 2010–2017". The abstract (page 1) gives these figures for the intervention without naming a place. Page 4 says the 25,000 farmers come from 600 villages in 49 districts of 7 Indian states, in about 46,000 trials, and cites Bioversity International (2017) and van Etten et al. (2019) for this. The 2010 to 2017 period refers to the Bihar activities (pages 2 and 13). Replace the Summary sentence with:
   > This study evaluates whether such an intervention works in practice, using Seeds for Needs in Bihar, India (2010 to 2017), which the authors describe as the largest citizen science intervention to date, with 25,000 farmers and 47,000 plot-seasons (figures for the whole initiative in India, not only Bihar). Besides on-farm variety trials, the intervention ran Farmer Field School trainings.

   Replace the Key numbers row with:
   > | 25,000 farmers, 47,000 plot-seasons | Scale of Seeds for Needs in India as a whole (600 villages, 49 districts, 7 states), not only Bihar. Page 4 gives about 46,000 trials | This paper (abstract). Page 4 cites Bioversity International 2017 and van Etten et al. 2019 |

4. **Farmer Field Schools not mentioned (high-importance omission).** Page 4 describes a second component of the intervention: capacity building through Farmer Field Schools on sustainable production and diversification. The effects estimated are for the whole package, not for crowdsourced trials alone. The replacement sentence in fix 3 covers the Summary. Also add to not_established (fix 9).

5. **Number of villages (Imprecise).** The card says "600 households in 12 villages of three districts". The sample covers 21 villages: 12 project villages plus 9 comparison villages (page 5, Table 1). The next sentence of the card mentions the 9 villages, so the summary contradicts itself. Replace "In 2018, enumerators surveyed 600 households in 12 villages of three districts" with:
   > In 2018, three enumerators surveyed 600 households in 21 villages of three districts

6. **Participation had no direct effect in the equation system (medium omission).** Table 4 (page 10) shows that the participation term was not significant for rice or wheat diversity (p = 0.231 and 0.265). Only the number of adopted varieties was significant. The rice perceived yield effect in the DR estimator is borderline (p = 0.053, Table 3, page 9). Replace "Perceived yield change rose by 0.185 points for rice and 0.245 for wheat," with:
   > Perceived yield change rose by 0.185 points for rice (p = 0.053) and 0.245 for wheat,

   and replace "Adopting promoted varieties raised diversity, diversity raised perceived yields of both crops, and higher wheat yields improved recovery capacity, though not for rice." with:
   > Adopting promoted varieties raised diversity, though participation alone had no significant direct effect. Diversity raised perceived yields of both crops, and higher perceived wheat yields improved recovery capacity, though rice yields did not.

   With fixes 1, 3, 5 and 6 together the Summary is 469 words (reviewer count), inside the 400 to 500 range.

7. **Percent note applies the rescaling to all outcomes (Imprecise, Notes).** The card says every percent effect uses a benchmark rescaled by adding 4. Table 3 (page 9, footnotes a and b) shows this applies only to the three outcomes on the −4 to +4 scale. The Simpson index benchmark is the plain non-exposed mean (0.602 and 0.561). Replace the first Notes bullet with:
   > - Percent effects are the DR estimate divided by a benchmark (Table 3). For the Simpson index the benchmark is the non-exposed mean. For perceived yield change and recovery capacity it is the non-exposed mean plus 4, which shifts the −4 to +4 scale above zero. So 3.94% and 4.80% are not yield percentages. On the perceived yield scale one point means about a 25% change in yield (page 7).

8. **data field (Imprecise, metadata).** The card says data are "available on request (Gotor et al. 2018)" and gives no DOI. The Data Availability Statement (page 14) says the data are in an online repository, Gotor et al. (2018), Harvard Dataverse, doi 10.7910/DVN/DW2W9J (reference list, page 15). Footnote 6 (page 6) says the data and survey are available on request at this DOI. No code location is given. Replace with:
   > data: Seeds for Needs India impact assessment survey, Harvard Dataverse, https://doi.org/10.7910/DVN/DW2W9J (Gotor et al. 2018, footnote 6 says data and questionnaire are available on request at this DOI), code not shared

9. **not_established is correct but too thin (metadata).** Replace with:
   > not_established: measured yield gains (yield change is self-reported on a −4 to +4 scale, and the percent effects are not yield percentages); randomized causal effects (quasi-experimental, no baseline); effects of crowdsourced trials alone (the intervention also ran Farmer Field School training); benefits for every household (the recovery effect was negative for households with high prior recovery capacity); effects beyond rice and wheat in Bihar

10. **Add adoption and p-values to Key numbers (medium omission).** Suggested extra row and revised rows:
   > | 1.65 / 1.91 vs 0.20 / 0.31 | Mean number of initiative rice / wheat varieties adopted, exposed vs non-exposed households (Table 2) | This paper |
   > | +0.031 (5.15%) / +0.061 (10.87%) | Effect on Simpson diversity, rice / wheat (p = 0.042 / p < 0.001) | This paper |
   > | +0.185 (3.94%) / +0.245 (4.80%) | Effect on perceived yield change, rice / wheat (p = 0.053 / p = 0.016) | This paper |
   > | +0.401 (7.46%) | Effect on recovery capacity (p = 0.001) | This paper |

11. **Source issues to add to Notes.** See the Source issues table for ready-to-paste text.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Smallholder farmer engagement in citizen science for varietal diversification enhances adaptive capacity and productivity in Bihar, India | Same title (p. 1) | Supported |
| authors | Gotor E, Pagnani T, Paliwal A, Scafetti F, van Etten J, Caracciolo F | Same six authors, same order (p. 1) | Supported |
| year | 2021 | Published 28 October 2021 (p. 1) | Supported |
| journal | Frontiers in Sustainable Food Systems | Same (p. 1) | Supported |
| article | 5, 726725 | Volume 5, Article 726725 (p. 1) | Supported |
| type | research article | "Original research" (p. 1) | Supported |
| doi | https://doi.org/10.3389/fsufs.2021.726725 | doi 10.3389/fsufs.2021.726725 (p. 1) | Supported |
| license | CC BY | Creative Commons Attribution License (CC BY) (p. 16) | Supported |
| data | survey data and questionnaire available on request (Gotor et al. 2018) | Online repository, Harvard Dataverse doi 10.7910/DVN/DW2W9J (p. 14, 15). Footnote 6 says on request (p. 6) | Imprecise (DOI missing, see fix 8) |
| crops | rice, wheat | Rice and wheat (p. 2, 6) | Supported |
| region | India (Bihar; Saran, Samastipur and Vaishali districts) | Same three districts (p. 5) | Supported |
| gist | Survey of 600 households ... increased rice and wheat varietal diversity, perceived yields and recovery from shocks | Table 3 (p. 9). Rice perceived yield p = 0.053 | Supported (26 words, says what the paper shows) |
| not_established | measured yield gains; randomized causal effects; effects beyond rice and wheat in Bihar | p. 5, 7 | Supported but thin (see fix 9) |

source: team is consistent with people.md (Jacob van Etten is listed).

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Two or more varieties can lower disease, raise productivity, reduce yield variability | Supported | p. 1, 2 | |
| 2 | Summary | Earlier evidence came from experiments or observation, not interventions | Supported | p. 2, 12 | |
| 3 | Summary | Study evaluates S4N in Bihar, described as largest citizen science intervention to date | Supported | p. 1, 12, 13 | |
| 4 | Summary | 25,000 farmers and 47,000 plot-seasons from 2010 to 2017 (linked to Bihar) | Imprecise | p. 1, 4 | Figures are for India as a whole (fix 3) |
| 5 | Summary | Analysis follows the sustainable rural livelihoods framework | Supported | p. 3 | |
| 6 | Summary | Expected effects on human, natural/physical and social capital, then adoption, diversity, productivity, recovery | Supported | p. 5 | |
| 7 | Summary | 2018 survey of 600 households in 12 villages of three districts | Imprecise | p. 5, Table 1 | 21 villages (fix 5) |
| 8 | Summary | Questionnaire adapted from RHoMIS, tablets with ODK | Supported | p. 5, 6 | Three sections were S4N-specific, the rest from RHoMIS |
| 9 | Summary | Questionnaire covered varieties over five years, seed sources, preferred traits, harvests, sales, climate losses, assets, shocks | Supported | p. 6, 7 | |
| 10 | Summary | Half were participants drawn from project records | Supported | p. 5 | Drawn at random |
| 11 | Summary | 150 non-participants from same villages, 150 from nine similar villages never reached | Supported | p. 5 | |
| 12 | Summary | Voluntary participation, no baseline, so doubly robust estimator combining participation and outcome models | Supported | p. 5, 7 | |
| 13 | Summary | Simultaneous equations by GMM with inverse probability weights to test each link | Supported | p. 7, 8 | |
| 14 | Summary | Simpson index, self-reported yield change over five years, self-assessed recovery index across four shocks | Supported | p. 6, 7 | |
| 15 | Summary | Diversity +0.03 rice (5%), +0.06 wheat (11%) | Supported | p. 9, Table 3 | Rounded from 0.031 and 0.061 |
| 16 | Summary | Perceived yield change +0.185 rice, +0.245 wheat, reported as 3.94% and 4.80% | Supported | p. 9, Table 3 | Rice p = 0.053 not stated (fix 6) |
| 17 | Summary | Recovery capacity +0.40, about 7% | Supported | p. 9, Table 3 | See source issue on "actual mean value" |
| 18 | Summary | Equation system supported the chain | Supported | p. 11 | Authors' own wording is stronger ("causality") |
| 19 | Summary | Adopting promoted varieties raised diversity | Supported | Table 4, p. 10 | Participation term not significant (fix 6) |
| 20 | Summary | Diversity raised perceived yields of both crops | Supported | Table 4, p. 10 (rice 1.968, p = 0.009, wheat 3.006, p = 0.010) | |
| 21 | Summary | Higher wheat yields improved recovery, not rice | Supported | Table 4, p. 10, 11 (wheat 1.810, p = 0.049, rice 0.260, p = 0.746) | Should say "perceived" |
| 22 | Summary | Recovery benefits largest among households with lowest prior recovery | Contradicted | p. 13, Figure 5 p. 12 | p. 12 text partly supports it. Source issue (fix 1) |
| 23 | Summary | Estimates conservative because spillovers ignored | Supported | p. 9 | |
| 24 | Summary | Conclusion: participatory programmes using local varietal diversity strengthen livelihoods, evidence on effect size for policymakers | Supported | p. 13, 14 | |
| 25 | Methods | 600 households, 300/300, 12 project and 9 comparison villages, Feb to Aug 2018 | Supported | p. 5, Table 1 | |
| 26 | Methods | 17-section questionnaire with RHoMIS modules, ODK | Supported | p. 5, 6 | |
| 27 | Methods | Simpson index, yield change −4 to +4, recovery index −4 to +4 | Supported | p. 6, 7 | |
| 28 | Methods | DR estimator, then five equations by GMM with IPW | Supported | p. 7, 8 | |
| 29 | Limitations | No baseline or randomized control, programme expanded with local demand | Supported | p. 5 | |
| 30 | Limitations | Productivity and recovery are self-reported | Imprecise | p. 7 | True, but not stated as a limitation by the authors (fix 2) |
| 31 | Limitations | Floods skewed the sample | Supported | p. 5, footnote 3 | Skewed toward Vaishali |
| 32 | Limitations | Spillovers ignored, so conservative | Supported | p. 9 | |
| 33 | Key numbers | 25,000 farmers, 47,000 plot-seasons, Bihar 2010 to 2017, primary source "This paper" | Imprecise | p. 1, 4 | Scope and attribution (fix 3) |
| 34 | Key numbers | 6,500 participating households across three districts | Supported | p. 5, footnote 4 | 1,500 + 1,500 + 3,500 = 6,500 (recomputed) |
| 35 | Key numbers | 600 households, 300 exposed, 300 non-exposed | Supported | p. 5, Table 1 | Column totals recomputed: 39 + 82 + 179 = 300 and 111 + 70 + 119 = 300 |
| 36 | Key numbers | +0.031 (5.15%) / +0.061 (10.87%) | Supported | Table 3, p. 9 | Recomputed: 0.031/0.602 = 5.15%, 0.061/0.561 = 10.87% |
| 37 | Key numbers | +0.185 (3.94%) / +0.245 (4.80%) | Supported | Table 3, p. 9 | Recomputed: 0.185/4.690 = 3.94%, 0.245/5.102 = 4.80% |
| 38 | Key numbers | +0.401 (7.46%) | Supported | Table 3, p. 9 | Recomputed: 0.401/5.377 = 7.46% |
| 39 | Notes | All percent effects use benchmark rescaled by adding 4 | Imprecise | Table 3 footnotes, p. 9 | Only for the −4 to +4 outcomes (fix 7) |
| 40 | Notes | Intervention uses the crowdsourced evaluation approach of van Etten et al. 2019 | Supported | p. 2 | Source cites van Etten et al. 2016 and 2019. The intervention also included Farmer Field Schools (p. 4). "India bread wheat case" is a cross-reference, not checked here |
| 41 | Notes | This study is quasi-experimental | Supported | p. 2, 7 | |

Claims 42 to 54 are the 13 frontmatter fields in the Metadata check above.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Who gained most in recovery capacity: Results text says lower percentiles benefited in particular, Discussion says intermediate prior levels gained most and high prior levels lost. Figure 5 (read off chart, approximate) peaks near the 35th percentile and turns negative above about the 75th | p. 12, 13, Figure 5 | No | - The source is inconsistent on who gained most in recovery capacity. The Results (page 12) stress the lower percentiles, the Discussion (page 13) says intermediate prior levels gained most and high prior levels lost. Figure 5 agrees with the Discussion. |
| Rice heterogeneity: Results say the rice diversity effect grows with prior diversity and the rice yield effect is inverse U-shaped. Discussion says rice gains went to households with lower prior levels. Figure 5 matches the Results | p. 12, 13, Figure 5 | No | - For rice, the Results (page 12) and Figure 5 show the diversity effect rising with prior diversity and an inverse U for perceived yield, but the Discussion (page 13) says rice gains went to households with lower prior levels. |
| Recovery percent: text says the 0.40 gain is about 7% "of the actual mean value", but Table 3 divides by the non-exposed mean plus 4 (5.377). Against the actual non-exposed mean (1.377) it would be about 29% (reviewer calculation) | p. 9, Table 3 | Partly (Notes explain the rescaling but not the text conflict) | - The text (page 9) calls the 7% a share of the actual mean, but Table 3 divides by the non-exposed mean plus 4. Against the plain non-exposed mean (1.377) the gain would be about 29% (card's own calculation). |
| Scale figures: abstract gives 47,000 plot-seasons, page 4 gives about 46,000 trials. Page 4 says 7 Indian states, footnote 1 says the initiative spread to nine more states but lists eight names, two of them the same state (Odisha and Orissa) | p. 1, 4 | No | - The source gives 47,000 plot-seasons (abstract) and about 46,000 trials (page 4) for the India programme, and its count of states is not consistent (7 on page 4, nine more in footnote 1). |
| Data access: Data Availability Statement says online repository, footnote 6 says available on request | p. 6, 14 | No (card repeats "on request") | Covered by the data field fix (fix 8). |
| Table 2 group means differ from the non-exposed and exposed values in Table 3 (for example rice perceived yield 0.67 / 0.92 vs 0.690 / 0.875, recovery 1.44 / 1.52 vs 1.377 / 1.778). Table 3 values are probably adjusted means, but the paper does not say so. Raw recovery means do not differ (t = −0.62) | p. 6, 9 | No | - The non-exposed and exposed values in Table 3 differ from the raw means in Table 2 and are probably adjusted by the DR model. In the raw data, recovery capacity did not differ between groups (Table 2). |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: effect of S4N on diversity, productivity and recovery from shocks | Yes | high | |
| Design: quasi-experimental, 300 exposed and 300 non-exposed, two types of non-exposed households | Yes | high | |
| Methods: DR estimator, GMM system with IPW, instruments, diagnostic tests | Yes (except instruments and tests) | low | Optional in Methods: "Participation and number of adopted varieties used as instruments, checked with Durbin–Wu–Hausman and weak instrument tests." |
| Main DR effects and percentages | Yes | high | |
| Equation system results | Yes | high | |
| Authors' Limitations section | No | high | Fix 2 |
| Intervention included Farmer Field School training as well as trials | No | high | Fixes 3 and 9 |
| Participation term not significant once adoption is in the model | No | medium | Fix 6 |
| Rice perceived yield DR effect borderline (p = 0.053) | No | medium | Fixes 6 and 10 |
| Negative recovery effect for households with high prior recovery capacity | No | medium | Fix 1 |
| Adoption numbers: exposed 1.65 rice and 1.91 wheat varieties vs 0.20 and 0.31 | No | medium | Fix 10 |
| Groups differed at baseline: exposed households had less land (1.29 vs 1.71 acres), more trust, more debt, more formal credit. Raw recovery capacity did not differ | No | medium | Add to Methods: "**Group differences.** Exposed households cultivated less land (1.29 vs 1.71 acres) and reported more trust, debt and formal credit (Table 2)." |
| Female-headed households had lower rice diversity and rice yield change but higher recovery capacity. Recovery was higher where households had faced shocks | No | low | Optional in Notes |
| Diversity peaks at about six adopted varieties (Figure 3) | No | low | Optional in Notes: "Simpson diversity rises with the number of adopted varieties up to about six, then falls (Figure 3, read off chart)." |
| Wheat Simpson index of 0.8 linked to a perceived wheat yield gain above 50% (Figure 4) | No | low | Optional |
| Authors call the findings "not surprising" because S4N was designed to promote diversity | No | low | Optional |
| S4N in 14 countries, in India 600 villages, 49 districts, 7 states | Partly | low | Covered by fix 3 |

## Template compliance

- Summary word count: 419 (target 400 to 500). With the suggested fixes it is about 469.
- Gist: 26 words (under 30). Says what the paper shows.
- Keywords: 11 (target 8 to 12).
- Questions: 4 (target 4 to 7).
- House style: no tricot or maniva in the card text. No style problems found.
- Long format is used and all long-format sections are present.
