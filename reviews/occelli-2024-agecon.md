# Card review: occelli-2024-agecon

- **Card:** papers/occelli-2024-agecon.md
- **Source:** papers-pdf/occelli-et-al-2024a.pdf (26 pages, journal pages 270 to 295, PDF page = journal page minus 269)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 50 |
| Supported | 38 |
| Imprecise | 8 |
| Not in source | 4 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 8 |
| Important omissions | 9 (3 high) |
| Metadata issues | 4 |

The summary follows the paper well on design, diversification, adoption and the authors' conclusions. Three problems need fixing before curation. First, the 28% cost figure has no basis attached. In the paper, 28% matches the total programme cost, while tricot-PVS reached almost twice as many farmers, so per farmer tricot-PVS was 62% cheaper. Second, all three "Stated limitations" are not in this paper. Two of them come from desousa-2024-asd. Third, the card leaves out main results: the much lower attrition under tricot-PVS (17% against 32%) and the absence of any food security gain for tricot-PVS. The author order is also wrong.

### What this paper reports about cost (answer to the caller's question)

- The only cost comparison in the paper is **tricot-PVS against group-PVS**, both run in the same study in the Trifinio area. There is **no comparison with RCBD**, researcher-managed or on-station trials anywhere in the paper. The number **40% does not appear** in the paper.
- Text, p. 275 (PDF p. 6): tricot-PVS costs 28% less than the group-PVS approach. The text also calls the cost "significantly lower", but no statistical test is reported.
- Table A7, p. 295 (PDF p. 26), checked on the page image:

| | Group-PVS | tricot-PVS |
|---|---|---|
| Cost per participant (USD) | 78.41 | 30.07 |
| Number of participants | 394 | 739 |
| Total cost of the approach (USD) | 30,893.54 | 22,221.73 |

- Recomputed: total cost ratio 22,221.73 / 30,893.54 = 0.719, so **28.1% lower total cost**. This is where the 28% comes from. Per participant, 30.07 / 78.41 = 0.383, so **61.7% lower cost per farmer** (tricot-PVS costs about 38% of group-PVS per farmer). Both are this review's calculations. The line items add up (78.42 and 30.06, rounding only).
- The appendix says the method is unit cost per participant, converted from local currency to USD. The text gives 28% without saying it is the total, not the per-farmer figure. So the source itself is unclear about the basis (see Source issues).
- tricot-PVS was higher than group-PVS for phone calls (1.33 against 0.27), seeds (6.08 against 4.62) and training materials (2.34 against 1.67). It had no cost for transport, preparation inputs or coordination and training.
- desousa-2024-asd (p. 7 of that paper) says tricot was about 40% cheaper **than RCBD** in Central America, with higher costs in phone calls and seed packaging, citing this paper. The phone call and seed lines match Table A7, so it seems to refer to this table, but the comparator is wrong (group-PVS, not RCBD) and neither 28% nor 62% is 40%. A possible origin is the per-farmer ratio of 38%, misread as "40% cheaper". This is a guess, not something either paper states.
- chase-2026-book says "about a quarter cheaper" and "nearly twice as many farmers". That fits this paper (28% lower total cost, 739 against 394 farmers, 1.88 times).

## Fixes needed

1. **Cost figure without basis (Summary, Key numbers, gist).** Card: "A cost analysis found tricot-PVS 28% cheaper than group-PVS." Source: 28% less (p. 275), which equals the total cost of each approach in Table A7 (p. 295), with tricot-PVS covering 739 farmers and group-PVS 394. Per farmer the costs were USD 30.07 and 78.41. Replace the first sentence of Summary paragraph 4 with:

   > A cost analysis found that tricot-PVS cost 28% less in total than group-PVS ($22,222 against $30,894), while it reached almost twice as many farmers (739 against 394). Per farmer, tricot-PVS cost $30 against $78. Fewer tricot farmers dropped out (17% against 32%), which the authors link to higher external validity of the data.

   Replace the Key numbers row for 28% with these rows:

   > | 28% | Lower total programme cost of tricot-PVS vs group-PVS ($22,221.73 vs $30,893.54), with 739 vs 394 farmers | This paper |
   > | $30.07 vs $78.41 | Cost per farmer, tricot-PVS vs group-PVS, 62% lower per farmer (card's own calculation) | This paper |

2. **Stated limitations are not from this paper (p. 276, p. 279, p. 280, p. 290).** The "up to ten years" adoption point and the unreleased varieties point come from desousa-2024-asd (which cites Thiele et al. 2021). This paper does not say either, and it does not state a one region, one crop limitation. Replace the whole section with:

   > - Only three years passed between the end of the experiment and the endline survey, so farmers may still be testing the new varieties, in a transition stage when diversification is higher. The authors do not correct for this.
   > - Spillovers in the 77 villages where treated and control farmers lived together may break the conditions for the instrumental variable, so the authors read the treatment-on-the-treated effects with caution.
   > - Attendance could only be coded as yes or no, so different degrees of participation could not be analysed.
   > - The analyses of adoption, yield, seed delivery and attrition are descriptive and do not show causal relations.
   > - Farmers who completed the programmes differed from those who dropped out (larger households, more often female-headed, less land for beans).

3. **Missing main results on food security and attrition (Summary paragraph 3).** Card: "Group-PVS was significantly more effective at improving household food security". Source: abstract says "appears to be significantly more effective" (p. 270). The ITT effect is significant only against control farmers in treated villages (Table 3, p. 281: −1.05***), not against control villages (−0.33, not significant). tricot-PVS showed no gain, and against control villages its hunger score rose (p. 280, Table 3). Replace the second sentence of paragraph 3 and add one sentence after it:

   > Group-PVS appeared to be more effective at improving household food security, which the authors attribute to better agronomic management learned through group activities. This effect was significant against control farmers in treated villages but not against control farmers in control villages. tricot-PVS brought no food security gain.

   (Attrition is covered by the new text in fix 1.)

4. **Misread mechanism (Summary paragraph 6).** Card: group-PVS "had a stronger effect on food security than on variety adoption". Source (p. 284, Table A6 p. 295): the mechanism (attending agronomic meetings) has a stronger link with food security than variety adoption has. Replace the second sentence of paragraph 6 with:

   > That mechanism appears to explain the advantage of group-PVS. Among group-PVS farmers, attending agronomic meetings was more strongly linked to a lower hunger score than adopting a tested variety, although this analysis is descriptive.

   With fixes 1, 3 and 4 the summary is 489 words.

5. **Author order (frontmatter).** The card lists authors in column order. Byline (p. 270) and "How to cite" (p. 288) give: Occelli, Sellare, De Sousa, Dell'Acqua, Mercado, Paredes, Robalino, Rosas, van Etten. Replace with:

   > authors: Occelli M, Sellare J, de Sousa K, Dell'Acqua M, Mercado L, Paredes S, Robalino J, Rosas JC, van Etten J

   The automated flag on `Dell'Acqua M` is a straight versus curly apostrophe (the PDF prints Dell’Acqua). It is not an error.

6. **Gist.** Replace with (28 words):

   > Randomized trial with 1,978 bean farmers finds tricot and group PVS give similar varietal diversification and adoption, group PVS better food security, and tricot 28% lower total cost

7. **not_established.** Strengthen to:

   > cost savings against RCBD or researcher-managed trials (the only comparison is with group PVS); a 40% saving (no such figure in this paper); the 28% as a per-farmer saving (it is total programme cost, and tricot reached 739 farmers against 394, per farmer the saving is 62%); better food security from tricot (no gain, and a slightly higher hunger score than control villages); a food security gain from group PVS against all controls (significant only against control farmers in treated villages); effects outside bean in Central America

8. **article and data fields.** The article field should give volume and pages. There is no data availability statement in the PDF. Replace with:

   > article: 55(2), 270–295
   > data: none stated in the article

9. **Key numbers, adoption rows.** Add the condition to the 4% row and add attrition:

   > | 4% lower | Adoption probability, tricot-PVS vs group-PVS (descriptive model, negligible and not significant once delivery of the preferred variety is controlled) | This paper |
   > | 17% vs 32% | Self-induced attrition, tricot-PVS (128 of 739) vs group-PVS (126 of 394) | This paper |

10. **Methods, outcomes bullet.** Adoption is analysed as a mechanism, not a main outcome. Replace with:

    > - **Outcomes.** On-farm varietal diversification (variety count and variety richness index) and household food security (Household Hunger Scale). Adoption, yield, delivery of the preferred variety and attrition were analysed as mechanisms.

11. **Notes.** Replace the first note with:

    > - The only cost comparison in this paper is tricot-PVS against group-PVS in the same study (text p. 275, Table A7 p. 295). There is no comparison with RCBD and no 40% figure. The 28% matches total programme cost ($22,221.73 vs $30,893.54). Per farmer, tricot-PVS cost $30.07 against $78.41, which is 62% less (card's own calculation). No statistical test of the cost difference is reported.
    > - desousa-2024-asd cites this paper for tricot being about 40% cheaper than RCBD in Central America, with higher costs for phone calls and seed. Those two lines match Table A7, but the comparator here is group-PVS, not RCBD. Cite 28% (total cost) or $30.07 vs $78.41 (per farmer) from this paper, against group PVS.
    > - desousa-2024-asd also says adoption can take up to 10 years and that 7 of 19 varieties were unreleased at endline. Neither point is in this paper. Table A3 here lists 8 varieties as not released and 2 more released only in 2019.
    > - The source reports 74 of 394 as 18%. The exact value is 18.8%.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Group-based and citizen science on-farm variety selection approaches for bean growers in Central America | Same (p. 270) | Supported |
| authors | Occelli M, Mercado L, Sellare J, ... | Occelli, Sellare, De Sousa, Dell'Acqua, Mercado, Paredes, Robalino, Rosas, van Etten (p. 270, p. 288) | Imprecise (order wrong) |
| year | 2024 | 2024 (p. 270) | Supported |
| journal | Agricultural Economics | Agricultural Economics (p. 270) | Supported |
| article | published 2024 (accepted November 2023) | 55(2), 270–295, accepted 30 November 2023 (p. 270) | Imprecise (no volume, issue or pages) |
| type | research article | Original article (p. 270) | Supported |
| doi | https://doi.org/10.1111/agec.12819 | 10.1111/agec.12819 (p. 270) | Supported |
| license | CC BY-NC-ND | Creative Commons Attribution-NonCommercial-NoDerivs (p. 270) | Supported |
| data | see the data availability statement in the article | No data availability statement in the PDF | Not in source |
| crops | common bean | Phaseolus vulgaris (p. 270) | Supported |
| region | Trifinio area (Guatemala, Honduras, El Salvador) | p. 271 to 272 | Supported |
| gist | ... tricot 28% cheaper | 28% is total cost, 62% per farmer (p. 275, p. 295) | Imprecise |
| not_established | RCBD, food security from tricot, other crops | Correct items, but misses the 40% figure, per-farmer basis and the food security nuance | Supported (incomplete) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Impact evaluation of tricot vs group PVS on farmer outcomes, not only information quality | Supported | p. 271 | |
| 2 | Summary | Participatory approaches bring farmer knowledge but are rarely streamlined or scaled | Supported | Abstract p. 270 | |
| 3 | Summary | tricot effects on participants not tested against a strong benchmark | Supported | p. 271 (Gotor et al. 2021 the only prior study) | |
| 4 | Summary | Trifinio, where Guatemala, Honduras and El Salvador meet | Supported | p. 271 to 272 | |
| 5 | Summary | 1,978 farmers, 140 villages, randomized to three arms, baseline and follow-up | Supported | p. 270, p. 272 to 273 | Baseline 2015, endline 2018 |
| 6 | Summary | Outcomes diversification and food security, DiD with IPW and IV | Supported | p. 270, p. 279 | |
| 7 | Summary | Comparable diversification relative to control | Supported | Abstract p. 270 | See source issue 4 |
| 8 | Summary | Group-PVS significantly more effective at improving food security | Imprecise | p. 270 ("appears to be"), Table 3 p. 281 | Significant only vs control farmers in treated villages |
| 9 | Summary | Authors attribute it to agronomic management learned in groups | Supported | p. 270, p. 284 | Hedged in source ("can be attributed", "seems to confirm") |
| 10 | Summary | Adoption was similar | Supported | p. 284 | |
| 11 | Summary | 20% (146/739) tricot, 18% (74/394) group-PVS after three years | Supported | p. 284 | 146/739 = 19.8%, 74/394 = 18.8% (source issue 2) |
| 12 | Summary | Adoption probability 4% lower under tricot in the model | Supported | p. 283, Table 5 | See source issue 3 |
| 13 | Summary | tricot-PVS 28% cheaper | Imprecise | p. 275, Table A7 p. 295 | Total cost, not per farmer |
| 14 | Summary | Conclude similar diversification at lower cost, lacks learning effects, combine with agronomic training | Supported | p. 285 | Authors propose tricot for testing and separate group agronomy training |
| 15 | Summary | Framed as more inclusive, demand-driven variety selection | Supported | p. 270 | |
| 16 | Summary | Expected both to raise diversification, different exposure (three varieties intensively vs whole set) | Supported | p. 284 | |
| 17 | Summary | Both groups diversified more than control | Supported | p. 284 | Authors' statement, see source issue 4 |
| 18 | Summary | Adoption similar once delivery of preferred variety accounted for | Supported | p. 284, Table 5 p. 283 | |
| 19 | Summary | About 20% adoption in line with other estimates, promising as varieties were mostly new | Supported | p. 284 | |
| 20 | Summary | Expected group participants to gain from training and exchanges, raising yields | Supported | p. 284 | Source also hypothesized a tricot food security gain (p. 272, p. 284) |
| 21 | Summary | Group-PVS had a stronger effect on food security than on adoption | Imprecise | p. 284, Table A6 p. 295 | Source: meeting attendance has a stronger effect on food security than adoption has |
| 22 | Summary | Trade-off between tricot scale and lower cost and group learning benefits | Supported | p. 284 to 285 | |
| 23 | Methods | Villages randomly assigned to three arms | Supported | p. 273 | Households then allocated within villages |
| 24 | Methods | 1,978 farmers, 140 villages, baseline and endline | Supported | p. 273, p. 275 | |
| 25 | Methods | Outcomes include variety adoption | Imprecise | p. 276, p. 279 | Adoption is a mechanism variable |
| 26 | Methods | DiD with IPW plus IV | Supported | p. 279 | ITT and TOT |
| 27 | Methods | Itemized cost comparison in appendix table | Supported | Table A7 p. 295 | Per participant |
| 28 | Limitations | Adoption takes up to ten years, so rates conservative | Not in source | p. 276 says only three years elapsed | From desousa-2024-asd |
| 29 | Limitations | Some varieties unreleased at endline, limiting seed access | Not in source | Table A3 p. 290 lists release years, no such statement | From desousa-2024-asd |
| 30 | Limitations | One region, one crop | Not in source | Not stated by authors | Fair point, but belongs in not_established |
| 31 | Key numbers | 1,978 farmers, 140 villages | Supported | p. 270 | |
| 32 | Key numbers | 20% (146 of 739) | Supported | p. 284 | |
| 33 | Key numbers | 18% (74 of 394) | Supported | p. 284 | Exact 18.8% |
| 34 | Key numbers | 4% lower adoption probability | Supported | p. 283 | Add that it vanishes after control |
| 35 | Key numbers | 28% lower cost | Imprecise | p. 275, p. 295 | Basis missing |
| 36 | Notes | This paper reports 28%, not 40% | Supported | p. 275 | Should add that there is no RCBD comparison |
| 37 | Notes | Adoption figures match desousa-2024-asd | Supported | de Sousa et al. 2024 p. 7 | |

Metadata claims (13) are in the table above.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Text gives 28% without basis. It equals total cost, while the appendix says it computes cost per participant, which gives 62%. "Significantly lower" has no test. | p. 275, p. 295 | No | See fix 11, first note |
| 74 of 394 is 18.8%, printed as 18% | p. 284 | No | See fix 11, last note |
| Adoption coefficient −4.01 from a multinomial logit is read as "4% lower" probability. The unit is unclear. | p. 283, Table 5 | No | The 4% figure is the authors' reading of a logit coefficient (Table 5) and should not be read as a percentage-point difference. |
| Discussion says both groups diversified more than control, but most ITT diversification effects are not significant. Only the tricot variety count is significant (+0.14, Table 3). Group-PVS variety richness is significant only in TOT (Table 4). | p. 284, p. 281 to 282 | No | The diversification gains rest mainly on the tricot variety count (ITT) and the group-PVS variety richness index (TOT). Other diversification effects were not significant. |
| Text says tricot raised the hunger score with P < .1. Table 3 shows 0.68 (P < .05) without controls and 0.62 (P < .1) with controls. | p. 280, p. 281 | No | Low priority |
| Text cites Table A1 for the variety list and for new cultivars. The list is in Table A3. | p. 274, p. 284 | No | Low priority |
| Group-PVS described as six meetings and five field visits, later as four to five participatory steps | p. 275, p. 284 | No | Low priority |
| Control farmers split 521/324 before self-induced attrition but 487/358 after, although controls should not change | p. 276, p. 278 | No | Low priority |

## Completeness

| Item in the source | In card? | Importance | Suggested addition |
|---|---|---|---|
| Self-induced attrition 32% (126/394) group-PVS vs 17% (128/739) tricot-PVS, 95% higher chance in group-PVS, linked to external validity | No | High | Fix 1 and fix 9 |
| tricot-PVS had no food security gain, and a higher hunger score than control villages | No | High | Fix 3 and fix 7 |
| Cost per farmer $30.07 vs $78.41 and totals $22,222 vs $30,894 | No | High | Fix 1 |
| Group-PVS food security effect significant only vs control farmers in treated villages (ITT −1.05, TOT −0.13) | No | Medium | Fix 3 |
| Arm sizes 394 / 739 / 845, unbalanced design chosen because tricot was cheaper | Partly (in adoption figures) | Medium | Methods: "394 households in group-PVS, 739 in tricot-PVS and 845 controls. The design gave tricot-PVS more farmers because it was cheaper." |
| Treatment protocols: group-PVS 15 households per village, 19 varieties on a common plot, six meetings and five field visits over about 70 days. tricot-PVS 20 farmers per village, 3 of 19 varieties each, trial designed in ClimMob, two central meetings, four data collection moments by phone. Both received 1.5 kg seed of the preferred variety. | No | Medium | Add as a "Treatments" bullet in Methods with this text |
| Diversification effect sizes: tricot variety count 15% higher than control villages (1.37 vs 1.25) | No | Medium | Optional Key numbers row |
| Yield lower and preferred-variety delivery 3% lower for tricot-PVS (descriptive) | No | Medium | Optional sentence: "tricot-PVS farmers had lower yields and were 3% less likely to receive their preferred variety, in descriptive models." |
| Authors' own limitations (three-year window, spillovers and IV, binary attendance, descriptive mechanisms, completer bias) | No (replaced by other text) | Medium | Fix 2 |
| Aim, design, conclusions, hybrid recommendation | Yes | | |

## Template compliance

- Summary: 406 words (target 400 to 500). With fixes 1, 3 and 4: 489 words.
- Gist: 27 words (under 30). Proposed gist: 28 words.
- Keywords: 8 (8 to 12). Consider adding "attrition".
- Questions: 4 (4 to 7). Consider adding "Do farmers drop out less from tricot than from group PVS?"
- House style: tricot in lowercase throughout. "Group-PVS" capitalised at sentence start is fine. No em dashes found.
