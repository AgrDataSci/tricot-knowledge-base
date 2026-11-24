# Card review: steinke-2017-asd

- **Card:** papers/steinke-2017-asd.md
- **Source:** papers-pdf/steinke-et-al-2017.pdf (12 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 60 (13 metadata fields, 47 body claims) |
| Supported | 46 |
| Imprecise | 10 |
| Not in source | 2 |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 5 |
| Important omissions | 8 (2 high) |
| Metadata issues | 3 (data, gist, not_established missing) |

The card is well organised and most numbers are correct. All 22 numbers in the body appear in the source. But the Summary gets the main validity result wrong. It says the Mallows-Bradley-Terry (MBT) models found the correct order "for most traits" with disease resistance as the exception. In fact the source says the order was correct for all four traits (p. 7). Disease resistance failed only on statistical separation. Under the review rules, a Contradicted claim on the main result means Major fixes, although the fix itself is one paragraph. Two Summary sentences also add content that is not in the source: "later work" on heterogeneity, and a plants, insects, diseases ranking credited to earlier Honduran work. not_established is missing.

## Fixes needed

1. **MBT result (Contradicted, high).** The card says the models "recovered the correct order of varieties for most traits. Disease resistance was the exception, with too few observations to separate varieties." The source says the MBT model gives the correct order for all variables. Only plant vigor separated all three varieties. For all traits except disease resistance, the best and worst varieties separated at p < 0.05 (p. 7, Table 3). The source also gives 77 to 100% of rankings matching or nearly matching the expert, against 50% expected by chance (p. 7). The gender sentence also needs a fix (see item 2). Replace the whole paragraph that starts "Individual reliability was low" with:

   > Individual reliability was low. Agreement among farmers (Kendall's W) ranged from 0.174 to 0.676 and was high only for plant vigor, a trait that is easy to see. Validity was adequate. Mean agreement between farmers and the agronomist (Kendall's tau) ranged from 0.33 for disease resistance to 0.76 for plant vigor, and 77 to 100% of farmer rankings matched or nearly matched the agronomist's. Mallows-Bradley-Terry models fitted to the pooled rankings recovered the agronomist's order for all four traits. All three varieties separated significantly only for plant vigor, and the best and worst varieties separated for every trait except disease resistance, which had only 11 observations. Wilcoxon tests found no significant difference in validity between women and men for any trait, although the groups were small (5 to 14 per trait).

2. **Gender (Imprecise, medium).** "The authors found no difference in validity between women and men" is stronger than the source. The test found no significant effect at p < 0.05 (p. 6, Table 2). Groups were 5 to 14 people per trait, and some mean differences were large (disease resistance: women 0.11, men 0.60). The replacement in item 1 already fixes this.

3. **Final Summary paragraph (Not in source and Imprecise, high).** "where farmers knew plants precisely, insects less well and plant diseases least" is not in the source. The source cites Bentley (1989) only for the idea that ease of visual observation drives accuracy (p. 7). Also, the simulation tested only plant vigor and disease resistance (p. 5). So the claim that the simulation showed plant architecture and pest resistance "call for more observers" credits the simulation with something it did not test. That point comes from the field reliability results (p. 7). Replace the last paragraph with:

   > The simulation also showed that adding varieties to a trial of fixed size raises the number of varieties distinguishable from the best, although the share of distinguishable varieties falls (for plant vigor with 50 observers, from 100% with 3 varieties to 84% with 20). In the field data, plant architecture and pest resistance needed closer inspection of plants than plant vigor, and disease resistance needed the most scrutiny and background knowledge. The authors link this to Bentley's (1989) argument from Honduras that ease of visual observation is a main factor in the accuracy of farmer observations.

4. **Disagreement and "later work" (Imprecise and Not in source, medium).** The source says divergent rankings "may indicate" different understanding of a concept (p. 8). It does not say they do. "which later work addresses by modelling heterogeneity directly" is outside knowledge. The source only says the authors were testing such methods in ongoing research (p. 10). Replace the last two sentences of the conclusions paragraph with:

   > They also note that some disagreement may reflect different criteria among farmers, for example on what good plant architecture means, rather than observation error. tricot results therefore represent an average of farmer views, and the authors were testing methods that treat this variation as information.

   If the link to later work is wanted, put it in Notes: "Outside this source: later tricot analysis models heterogeneity among farmers with Plackett-Luce model trees. See turner-2020-compstat."

5. **50 vs 200 participants (Imprecise, medium).** This comparison holds for a 12-variety trial (p. 9). The card leaves out the trial size in both places.
   - Summary: replace "The discriminative ability reached for plant vigor with 50 participants required 200 participants for disease resistance." with "With 12 varieties, the discriminative ability reached for plant vigor with 50 participants required 200 participants for disease resistance."
   - Key numbers row: `| 50 vs 200 | Observers needed for the same discriminative ability with 12 varieties, plant vigor vs disease resistance (simulation) | This paper |`

6. **Methods, Design bullet (Imprecise, medium).** "35 farmers visited the plots at five points in the season" suggests each farmer came back five times. The source says there were five sessions across the season. Each farmer evaluated the varieties at one site, in groups of five to eight (p. 4). Replace with:

   > - **Design.** Five sites in Honduras, each with three common bean varieties, drawn from a pool of seven from the Zamorano bean breeding programme, in adjacent sub-plots of six 8 m rows. 35 farmers (18 women, 17 men) took part in five sessions across the season, in groups of five to eight, and each farmer evaluated one site. Each farmer named the best and worst variety for four traits. Pests and diseases could be observed at only two of the five sites.

7. **not_established missing (metadata, high).** Suggested text:

   > not_established: that individual farmer rankings are accurate on their own; that tricot is valid for yield, post-harvest, cooking or taste traits, which were not tested; that 150 to 200 participants is a tested minimum rather than a simulation-based order of magnitude under idealized, evenly spaced varieties; that women and men observe equally well in general, since groups were small and all participants grew beans; that disease resistance cannot be assessed by farmers, since its sample was 11 observations

8. **Stated limitations (Imprecise and incomplete, medium).** In the third bullet, "which the validity measure cannot separate" is not in the source. The authors suggest that disagreement could be detected statistically and used as a data-quality check (p. 8). Replace the third bullet and add the missing limitations:

   > - Rankings that differ from the expert may reflect different farmer criteria rather than error. The authors suggest detecting such disagreement statistically, as a data-quality check.
   > - The simulation considered only farmer observation error, not experimental errors such as mixed-up seeds or codes, and did not include attrition.
   > - Only pre-harvest traits were tested. Yield and post-harvest traits need a separate test.
   > - Farmers had only a short time on site, and pests and diseases were observed at only two of five sites.
   > - Pooling across sites assumes varieties were equally hard to tell apart at every site.

9. **Gist (Imprecise, low).** The source says 150 to 200 participants are "likely to be sufficient", assuming 20% attrition or less (p. 10). Replace with:

   > gist: First test of tricot data quality, showing individual farmer rankings are unreliable but valid in aggregate, so 150 to 200 farmers likely suffice for 10 to 12 varieties

   (28 words)

10. **data field (Imprecise, low).** The PDF says only that electronic supplementary material exists (p. 1). It does not say that it contains data or code. Replace with:

    > data: electronic supplementary material with the article (contents not described in the PDF), no code repository stated

11. **Key numbers, tau row (low).** 0.33 to 0.76 is the range of mean tau per trait. Individual tau values range from -1 to 1 (Table 1, p. 6). Replace the context with: "Mean Kendall's tau per trait, farmer rankings against the agronomist ranking (disease resistance to plant vigor)".

12. **Notes, models (Imprecise, low).** MBT was used for the field data. The simulation used Thurstone-Mosteller and the generalized Bradley-Terry-epsilon model (p. 5). Replace the second note with:

    > - The field data were analysed with Mallows-Bradley-Terry models and the simulation with Thurstone-Mosteller and generalized Bradley-Terry models. These predate the Plackett-Luce approach now standard in tricot (outside this source). See turner-2020-compstat.

13. **Methods, Validity bullet (low).** Add the multiple-testing correction, and note the gap between the stated criterion and the conclusion (see Source issues). Replace with:

    > - **Validity.** Kendall's tau between each farmer ranking and the reference, and Mallows-Bradley-Terry models on pooled rankings. The stated criterion was that the three varieties separate at p < 0.05 after Holm-Bonferroni correction.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | The accuracy of farmer-generated data in an agricultural citizen science methodology | Same (p. 1) | Supported |
| authors | Steinke J, van Etten J, Mejía Zelan P | Jonathan Steinke, Jacob van Etten, Pablo Mejía Zelan (p. 1) | Supported |
| year | 2017 | Published online 24 July 2017 (p. 1) | Supported |
| journal | Agronomy for Sustainable Development | Agron. Sustain. Dev. (header) | Supported |
| article | 37, 32 | (2017) 37: 32 (p. 1) | Supported |
| type | research article | "RESEARCH ARTICLE" (p. 1) | Supported |
| doi | https://doi.org/10.1007/s13593-017-0441-y | DOI 10.1007/s13593-017-0441-y (p. 1) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution 4.0 (p. 11) | Supported |
| data | supplementary material with the article | ESM exists, contents not described (p. 1) | Imprecise (fix 10) |
| crops | common bean | Phaseolus vulgaris (p. 1) | Supported |
| region | Honduras | Five sites in Honduras (p. 1, 4) | Supported |
| gist | ... so 150 to 200 farmers suffice for 10 to 12 varieties | "likely to be sufficient", 20% attrition or less (p. 10) | Imprecise, slightly too certain (fix 9) |
| not_established | missing | n/a | Missing (fix 7) |

source: team is consistent with people.md (Jacob van Etten is listed). peer_reviewed: yes fits a journal article. open_copy points to the DOI, and the article is open access (p. 1).

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Paper tests the core assumption that many independent farmer observations aggregate into valid results | Supported | Aim and abstract (p. 1, 2) | |
| 2 | Summary | Participatory approaches hard to scale: trained staff, collective plots, sustained engagement | Supported | p. 1 to 2 | |
| 3 | Summary | Wisdom of crowds: diverse independent observers converge even if individuals wrong | Supported | p. 2, 3 | |
| 4 | Summary | Five sites, 35 farmers (18 women, 17 men), sets of three bean varieties side by side | Supported | p. 4 | |
| 5 | Summary | Four traits ranked, agronomist ranked the same sets | Supported | p. 4 | |
| 6 | Summary | Agronomist ranking is the validity reference | Supported | p. 3 | |
| 7 | Summary | W 0.174 to 0.676, high only for plant vigor, easy to see | Supported | p. 1, 7, Table 1 | |
| 8 | Summary | Validity adequate, tau 0.33 to 0.76 | Supported | p. 1, Table 1 | These are mean tau per trait (fix 11) |
| 9 | Summary | MBT recovered correct order for most traits, disease resistance the exception | Contradicted | "For all variables, the MBT model gives the correct ranking order" (p. 7) | Fix 1 |
| 10 | Summary | No difference in validity between women and men | Imprecise | Not significant at p < 0.05, n 5 to 14 (p. 6, Table 2) | Fix 2 |
| 11 | Summary | Simulation built on empirical data estimated participants needed | Supported | p. 5, 8 | Order-of-magnitude only |
| 12 | Summary | More observers raise discriminative ability, harder traits need more | Supported | p. 8 to 9 | |
| 13 | Summary | Plant vigor with 50 equals disease resistance with 200 | Imprecise | With nvar = 12 (p. 9) | Fix 5 |
| 14 | Summary | Low individual reliability does not undermine accuracy with enough farmers | Supported | p. 9 | |
| 15 | Summary | 150 to 200 participants for 10 to 12 varieties, attrition 20% or less | Supported | p. 10 | |
| 16 | Summary | Disagreement reflects genuinely different criteria, rather than error | Imprecise | "may indicate" (p. 8), "possibly divergent views" (p. 10) | Too certain, fix 4 |
| 17 | Summary | tricot results represent an average of farmer views | Supported | p. 10 | |
| 18 | Summary | Later work addresses this by modelling heterogeneity | Not in source | Source says ongoing research (p. 10) | Outside knowledge, fix 4 |
| 19 | Summary | Adding varieties raises number distinguishable, within limits | Supported | p. 9 | |
| 20 | Summary | Simulation showed plant architecture and pest resistance need more observers | Imprecise | Simulation used only vigor and disease (p. 5). Inspection point is from field data (p. 7) | Wrong attribution, fix 3 |
| 21 | Summary | Agree with earlier ethnobiological work in Honduras | Supported | Bentley 1989 (p. 7, reference list) | |
| 22 | Summary | Farmers knew plants precisely, insects less well, diseases least | Not in source | Not stated anywhere | Fix 3 |
| 23 | Summary | Ease of visual observation is a main factor in accuracy | Supported | p. 7 | |
| 24 | Methods | Five sites, three varieties, sub-plots of six 8 m rows | Supported | p. 4 | |
| 25 | Methods | 35 farmers visited plots at five points in the season | Imprecise | Five sessions, each farmer at one site (p. 4) | Fix 6 |
| 26 | Methods | Ranked best and worst for four traits | Supported | p. 4 | |
| 27 | Methods | Local agronomist answered same questions each session | Supported | p. 4 | |
| 28 | Methods | Validity: tau plus MBT, valid if three varieties separate at p < 0.05 | Supported | p. 5 | Holm-Bonferroni missing, fix 13 |
| 29 | Methods | Reliability: Kendall's W | Supported | p. 5 | |
| 30 | Methods | Simulation, TM case V intervals, 216 scenarios | Supported | p. 5 | 18 x 6 x 2 = 216, 1000 runs each |
| 31 | Methods | Gender: Wilcoxon signed-rank on tau | Supported | p. 5 | See Source issues |
| 32 | Limitations | Disease resistance 11 observations, very low power | Supported | p. 6 to 7 | |
| 33 | Limitations | Simulation assumes regularly spaced differences | Supported | p. 9 | |
| 34 | Limitations | Different criteria, which the validity measure cannot separate | Imprecise | Source suggests detecting it statistically (p. 8) | Fix 8 |
| 35 | Limitations | Averaged view can hide group-specific preferences | Supported | p. 9 to 10 | |
| 36 | Key numbers | 35 farmers (18 women, 17 men) | Supported | p. 4 | |
| 37 | Key numbers | 5 sites | Supported | p. 4 | |
| 38 | Key numbers | W 0.174 to 0.676 | Supported | Table 1, p. 6 | |
| 39 | Key numbers | tau 0.33 to 0.76 | Supported | Table 1, p. 6 | Clarify "mean", fix 11 |
| 40 | Key numbers | 11 observations for disease resistance | Supported | Table 1, p. 7 | |
| 41 | Key numbers | 216 scenarios | Supported | p. 5 | |
| 42 | Key numbers | 4 to 10 varieties, plant vigor, 12 entries, 10 vs 500 observers | Supported | p. 8, also Fig. 2 | Chart values approximate, text is exact |
| 43 | Key numbers | 50 vs 200 observers | Imprecise | nvar = 12 (p. 9) | Fix 5 |
| 44 | Key numbers | 150 to 200 participants, 10 to 12 varieties, attrition 20% or less | Supported | p. 10 | |
| 45 | Key numbers | Fewer than 200 participants is a realistic sample | Supported | Abstract (p. 1) | |
| 46 | Notes | Cited by desousa-2024-asd as the validity study | Supported | desousa-2024-asd card, Notes | Cross-check of the other card |
| 47 | Notes | The models used here (MBT) predate Plackett-Luce | Imprecise | MBT for field data, TM and BT-epsilon in simulation (p. 5) | Outside knowledge, correctly placed in Notes, fix 12 |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The stated validity criterion is that MBT separates all three varieties at p < 0.05. Only plant vigor meets it. The authors still call the results valid in all cases, based on correct order plus separation of the best and worst variety. | p. 5 vs p. 7, Table 3 | No | - The stated MBT validity criterion (all three varieties separated at p < 0.05) is met only for plant vigor (Table 3). The authors' conclusion that results were valid in all cases rests on the correct order for every trait and on best-versus-worst separation for three of four traits. |
| A Wilcoxon signed-rank test, which is a paired test, is used to compare women and men. These are independent groups of unequal size (for example 13 vs 9). A rank-sum test would be the usual choice. | p. 5, Table 2 | No | - The gender comparison uses a Wilcoxon signed-rank test on independent groups of unequal size (Table 2). The groups had 5 to 14 people, so the test had little power. |
| Plant architecture: the gender means in Table 2 (women 0.67, n = 12, men 0.33, n = 14) pool to a mean tau of 0.49. Table 1 gives 0.51, which matches its own frequencies. The gap equals one observation (reviewer's calculation). | Tables 1 and 2, p. 6 | No | Optional, low importance |
| Table 3: the unadjusted p value for plant vigor X to Z is printed as 5.152, which is not a valid p value. It is probably 5.152e-5. | p. 7 | No | Optional, low importance |
| The tau formula text defines n as the total number of binaries. In the formula n(n-1)/2, n must be the number of ranked items (3). | p. 5 | No | Not needed in card |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: test accuracy of farmer observations, and order of magnitude of sample size | Yes | high | |
| MBT gives correct order for all four traits, separation pattern by trait | No (contradicted) | high | Fix 1 |
| Recommendation to run a preparatory order-of-magnitude study before a tricot trial, which can also detect semantic disagreement | No | high | Add to Summary conclusions: "They recommend that teams plan new tricot trials with a small preparatory study of this kind, since discriminative ability varies in practice." (adds 20 words, total about 503, so trim elsewhere if needed) |
| Scope: only pre-harvest, objectively observable traits. Not yield, post-harvest or taste | No | high | Fix 7 and fix 8 |
| 77 to 100% of rankings match or nearly match the expert, against 50% by chance | No | medium | Fix 1 |
| Varieties drawn from a pool of seven, groups of five to eight, pest and disease at only two of five sites | No | medium | Fix 6 |
| Other error sources and attrition not modelled, so real minimum sizes need these added | No | medium | Fix 8 |
| Practical options: staged selection starting with easy traits, training farmers on disease recognition, accepting less than maximum discrimination for early screening | No | medium | Could add to Notes: "The authors suggest staged selection starting with easy traits, training farmers on disease recognition, and accepting lower discrimination for early screening (p. 9)." |
| Gender context: all participants grew beans, stronger gender effects expected where tasks are more divided | No | medium | Could add to Notes (p. 6) |
| TM intervals 1.03 (plant vigor) and 0.37 (disease resistance), halved for the simulation, 1000 runs per scenario | No | low | Optional in Methods |
| Share of distinguishable varieties falls from 100% to 84% as varieties rise from 3 to 20 (plant vigor, 50 observers) | No | low | Fix 3 |

## Template compliance

- Summary word count: 409 (target 400 to 500). With fixes 1, 3, 4 and 5 it becomes about 483.
- Gist: 27 words (under 30). It says what the paper shows. The suggested gist has 28 words.
- Keywords: 10 (8 to 12).
- Questions: 5 (4 to 7).
- House style: tricot is lowercase throughout, including at the start of a sentence. No em dashes or semicolons in the body prose.
- Long format with all sections present. not_established is missing (fix 7).
