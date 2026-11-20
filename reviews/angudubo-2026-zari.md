# Card review: angudubo-2026-zari

- **Card:** papers/angudubo-2026-zari.md
- **Source:** papers-pdf/angudubo-et-al-2026b.pdf (10 pages: cover, title page, then printed pages 1 to 8. Printed page N is PDF page N+2.)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 62 |
| Supported | 55 |
| Imprecise | 6 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 6 |
| Important omissions | 4 |
| Metadata issues | 2 |

The card is accurate and close to the source. Every figure from Table 1 and the scenario text was recomputed and matches within rounding. The most important fix concerns the headline combined scenario. The report says local delivery plus clustered engagement brings the cost to about USD 103 per farmer and saves about USD 4,270 (p. 7, PDF 9). The separate scenarios in the same report add up to only USD 3,451, which gives about USD 110.85 per farmer. The card repeats USD 103 in the gist, the summary and Key numbers without flagging this. The card also presents the travel (USD 128) and labour (USD 132) figures in a way that hides that they are two parts of one change, each computed alone from the baseline.

## Fixes needed

1. **Combined scenario figure cannot be rebuilt (summary, Key numbers, Notes).** The card says that combining local delivery and clustered engagement gives about USD 103 per farmer, saving about USD 4,270. The source says the same (p. 7, PDF 9), but its own scenario savings are USD 1,550 (travel), USD 1,106 (labour) and USD 795 (30% cut in participant support) (p. 6 to 7, PDF 8 to 9). These cut different Table 1 lines, so adding them is reasonable. Their sum is USD 3,451, or USD 110.85 per farmer. Even with the 70% support cut that the authors warn against, the sum is USD 4,510 (USD 101.22). USD 4,270 matches a support cut of about 61%, which the report does not describe. Separately, the card's sentence on local delivery gives USD 128 and USD 132 as if they were two outcomes. The source says both come from "the same operational shift" (p. 6, PDF 8). Each is computed alone from the USD 142.22 baseline, and the source never gives the joint figure (USD 2,656 saved, USD 118.07 per farmer).
   Replace the fifth summary paragraph with:
   > Scenarios show what delivery choices would save, each computed alone from the baseline. Leaving routine monitoring and data collection to trained field agents, with researcher spot checks and remote data verification, cuts travel expenses by about 24% and field labour by about half. Alone, the travel saving gives USD 128 per farmer and the labour saving USD 132. Together they give about USD 118 (card's calculation). A 30% cut in transport refunds and refreshments, through fewer meetings in cluster hubs of 10 to 20 farmers and lower refund levels, gives about USD 135. Larger cuts save more but risk lower participation. The authors state that local delivery and clustered engagement together bring the cost to about USD 103, saving about USD 4,270. The separate scenarios add up to only USD 3,451, about USD 111 per farmer (card's calculation), and the report does not explain the gap.

   With this paragraph and fix 7, the summary is 499 words.
   Replace the Key numbers row `~USD 103 (USD 4,270)` with:
   > | ~USD 103 (USD 4,270) | Cost per farmer and saving stated for local delivery and clustered engagement combined. Cannot be rebuilt from the separate scenarios (see Notes) | This paper |

   Add Key numbers rows:
   > | USD 118.07 (USD 2,656) | Cost per farmer and saving when the travel and labour savings of the same shift to field agents are added (card's calculation) | Card's calculation from this paper |
   > | USD 110.85 (USD 3,451) | Cost per farmer and saving when travel, labour and a 30% participant support cut are added (card's calculation) | Card's calculation from this paper |

   Add to Notes:
   > - The combined figure of about USD 103 per farmer (USD 4,270 saved) on p. 7 cannot be rebuilt from the report's own scenarios. Travel (USD 1,550), labour (USD 1,106) and a 30% participant support cut (USD 795) add up to USD 3,451, or USD 110.85 per farmer. A 70% cut would give USD 4,510 (USD 101.22). USD 4,270 implies a support cut of about 61%, or savings not described in the report (card's calculation). Quote USD 103 only as the authors' stated estimate.

2. **Gist relies on the unverified USD 103 and drops "marginal".** The gist says the trial "cost USD 142 per farmer" and "better delivery design could cut it to USD 103". USD 142 covers marginal costs only (p. 4, PDF 6), and USD 103 cannot be rebuilt (fix 1). Suggested gist (29 words):
   > A 110-farmer maize tricot trial in Zambia had marginal costs of USD 142 per farmer, driven by researcher travel and participant support, both of which delivery changes could reduce

3. **not_established is missing three likely stretches.** Add to the end of the field:
   > ; that combining the scenarios gives USD 103 per farmer (the report's separate scenario savings add up to about USD 111 per farmer); that researcher visits added nothing to data quality, which is asserted, not measured; trial completion or farmer retention rates, which are not reported

4. **Methods: UN rates attributed to vehicle costs.** The card says "UN travel reimbursement rates for vehicle costs". This source says UN standards are used for travel expenses (p. 3, PDF 5), which in Table 1 means per diem and travel allowance, not fuel and vehicle costs. The vehicle mileage reading comes from the guidelines card (angudubo-2026-guide), not from this report. Replace the Standard rates bullet with:
   > - **Standard rates.** UN travel reimbursement standards for travel expenses, ITU country-level ICT price baskets for communication (a low-consumption bundle of 70 minutes, 20 SMS and 500 MB a month per job role), market prices adjusted for inflation for materials, and daily and hourly rates from ZARI's official monthly salary scales for labour.

5. **Key numbers: base of the 48% is unclear in the source.** The card says 48% is the "share of monitoring" from research-team visits. The source says monitoring is 85% of labour costs, "with a significant portion (about 48%)" from two research-team visits (p. 5, PDF 7). It does not say whether 48% is of monitoring or of all labour. The labour scenario saving (49.5% of labour, see fix 6) fits the second reading slightly better. Replace the row with:
   > | 85% / ~48% | Monitoring as share of field labour costs / portion from two research-team visits to about 25% of farms (the source does not say whether 48% is of monitoring or of all labour) | This paper |

6. **Notes: label the arithmetic and add the 49.5% reading.** The third Note computes USD 1,564 and USD 1,129 without saying these are the card's own numbers. Replace it with:
   > - The 24% cut in travel expenses equals about USD 1,564 (card's calculation), close to the USD 1,550 scenario saving. The stated 50.50% cut in field labour equals about USD 1,129 (card's calculation), above the USD 1,106 saving reported. USD 1,106 is 49.5% of labour costs, so 50.5% may be the share that remains rather than the share cut.

7. **Summary first sentence: first name from outside the source.** "Stephen Angudubo and colleagues" uses a first name that the report does not print (it gives "Angudubo, S."). The name is in people.md and is fine in Notes, where it already appears. Replace the opening words with:
   > Angudubo and colleagues costed a maize tricot trial run by the Zambia Agricultural Research Institute (ZARI) as one of a series of 1000FARMS case studies on what drives the cost of on-farm testing.

8. **Methods scope: add what the 15% allocation does and does not change.** The source says the split of researcher time between on-farm testing and core breeding "does not change field implementation costs". It only makes budgets clearer and avoids double-counting (p. 6, PDF 8). It also gives a 10 to 15% range on p. 3 (PDF 5). Replace the Scope bullet with:
   > - **Scope.** Marginal costs only. Fixed costs are excluded. 10 to 15% of researcher staff costs is allocated to on-farm testing, and the costing applies 15% (10% is the share proposed by the ABI Transform team). The authors note that this split does not change field implementation costs but makes budgets easier to compare.

9. **Key numbers: add the scenario percentages that drive the savings.** Add rows:
   > | ~24% / 50.50% | Cut in travel expenses / in field labour costs when routine monitoring and data collection go to field agents | This paper |
   > | ~18% | Cut in material costs from a 30% cut in participant support | This paper |
   > | USD 13,227 (~85%) | Travel, materials and field labour together, share of total | This paper |

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Insights into the costing of on-farm testing. A case study of maize tricot trials by Zambia Agricultural and Research Institute (ZARI) | Cover (PDF 1) prints this wording with a colon. Title page and citation differ slightly (see Source issues) | Supported (colon to period is expected) |
| authors | Angudubo S, Benavente G, van Etten J, Sinyinda L | Cover (PDF 1), p. 8 citation | Supported |
| year | 2026 | Cover, p. 8 | Supported |
| journal | Case study report, Bioversity International and International Center for Tropical Agriculture, Kampala, Uganda (1000FARMS) | p. 8: Alliance of Bioversity International and CIAT, Kampala, Uganda. 1000FARMS logo on cover | Supported |
| article | 10 p. | 10 PDF pages | Supported |
| type | report | Case study report | Supported |
| doi | https://hdl.handle.net/10568/182411 | Not printed in the PDF. Matches papers-pdf/LICENSES.md and relations.jsonld | Not in source (not checkable from the PDF, no fix needed) |
| license | see CGSpace record | No licence printed | Supported (follows the template rule) |
| data | costing template, https://hdl.handle.net/10568/182169 | p. 3 (PDF 5) | Supported |
| crops | maize | p. 2 | Supported |
| region | Zambia (Central, Lusaka, Southern, Eastern and Luapula provinces) | p. 2 (PDF 4) | Supported |
| gist | USD 142 per farmer ... could cut it to USD 103 | p. 4, p. 7 | Imprecise (drops "marginal", rests on a figure that cannot be rebuilt, fix 2) |
| not_established | fixed costs excluded, scenario data quality assumed, no comparison with other designs, other crops | p. 4, p. 7 | Supported but incomplete (fix 3) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Stephen Angudubo and colleagues costed ZARI maize trial as one of a series of 1000FARMS case studies | Imprecise | p. 1 (PDF 3): series of case studies. Cover gives "Angudubo, S." | First name from people.md, not the source. Low importance (fix 7) |
| 2 | Summary | 8 options, intermediate-maturity profile, 110 farmers, 9 districts, 3 agro-ecological regions, Nov 2024 to Apr 2025 | Supported | p. 2 (PDF 4) | 21 Nov 2024 to 1 Apr 2025 is 131 days, as stated |
| 3 | Summary | Field agents 4 monitoring visits, research team 2 | Supported | p. 2 | |
| 4 | Summary | Central seed distribution, last-mile by field agents, digital data collection | Supported | p. 2 | |
| 5 | Summary | Used 1000FARMS costing template and guidelines | Supported | p. 3 (PDF 5) | |
| 6 | Summary | Only marginal costs that grow with farmer numbers | Supported | p. 4 (PDF 6) | |
| 7 | Summary | Office work (test lines, traits, ClimMob design, central training) is fixed and left out | Supported | p. 4 | |
| 8 | Summary | 15% of researcher staff cost charged to on-farm testing, rest to core breeding | Supported | p. 3 (10 to 15%), p. 6 (15% applied) | |
| 9 | Summary | USD 15,644, USD 142.22 per farmer | Supported | Table 1, p. 4 | Sum of lines 15,644. 15,644.23 / 110 = 142.22 |
| 10 | Summary | Travel 42%, materials 29%, labour 14% | Supported | p. 4 to 5 | 6,516 / 15,644 = 41.7% |
| 11 | Summary | Transport 9%, communication 6% | Supported | Table 1 | 9.24%, 6.22% |
| 12 | Summary | Research team travel about 61% of travel | Supported | p. 4 | About USD 3,975 (card's calculation, not needed in card) |
| 13 | Summary | Seed production about 10% of total | Supported | p. 4 | 35% x 4,474 = 1,566 = 10.0% |
| 14 | Summary | Participant support 59% of materials, about USD 24 per farmer, because of many small sessions | Supported | p. 4, p. 6 (PDF 8) | 0.59 x 4,474 = 2,640, / 110 = 24.0 |
| 15 | Summary | Two cost drivers identified | Supported | p. 5 to 6 | |
| 16 | Summary | Research roles on ~25% of farms duplicate field agents' work, add per diem and staff days without clearly better evidence | Supported | p. 5 (PDF 7) | "Without clear improvement" is the authors' view, not measured (fix 3) |
| 17 | Summary | Second driver is participant support over many small meetings | Supported | p. 6 | |
| 18 | Summary | Local delivery lowers cost per farmer to USD 128 via travel and USD 132 via labour | Imprecise | p. 6 | Both from one shift, each computed alone from baseline. Joint effect USD 118.07 not given (fix 1) |
| 19 | Summary | 30% support cut through hubs of 10 to 20 lowers cost to about USD 135 | Imprecise | p. 6 to 7 | Source says the 30% cut comes from fewer meetings and lower reimbursement levels. Hub size is an example (fix 1). 795 / 0.3 = 2,650, consistent with 59% of materials |
| 20 | Summary | Larger cuts save more but risk lower participation | Supported | p. 7 (PDF 9) | |
| 21 | Summary | Combined, about USD 103 per farmer, saving about USD 4,270 | Supported | p. 7 | Matches the source, but the source figure cannot be rebuilt (Source issue 1, fix 1). (15,644.23 − 4,270) / 110 = 103.40 |
| 22 | Summary | Trial feasible, cost depends more on delivery than data volume | Supported | p. 7 | |
| 23 | Summary | Four recommendations, including SOPs tracking cost per farmer, completion rates, audit findings | Supported | p. 7 | |
| 24 | Methods | Activity-based Excel template, following guidelines | Supported | p. 3 | |
| 25 | Methods | Standard rates: UN rates for vehicle costs, ITU basket, market prices, ZARI salary scales | Imprecise | p. 3, p. 5 | Source applies UN standards to travel expenses, not vehicle costs (fix 4) |
| 26 | Methods | Assumptions: ten tricot steps, research team leads preparation, field agents lead monitoring, researchers do yield and feedback, separate seed production | Supported | p. 3 | |
| 27 | Methods | Scope: marginal only, 15% share (10% ABI Transform) | Supported | p. 4, p. 6 | |
| 28 | Methods | Scenarios: delegation and 30/50/70% support cuts | Supported | p. 6 to 7 | |
| 29 | Limitations | Fixed costs excluded, so total understates full cost | Supported | p. 4 | Exclusion is stated. "Understates" is a fair inference |
| 30 | Limitations | Cutting support too far risks lower participation and incomplete trials | Supported | p. 7 | |
| 31 | Limitations | Delegation needs training and SOPs to keep data quality | Supported | p. 5 | |
| 32 | Key numbers | 110 farmers, 8 options, 9 districts, 131 days | Supported | p. 2 | |
| 33 | Key numbers | USD 15,644 / 142.22 | Supported | Table 1 | |
| 34 | Key numbers | 36.8% + 4.9% (USD 5,752, 764) | Supported | Table 1 | |
| 35 | Key numbers | 28.6% materials (USD 4,474) | Supported | Table 1 | |
| 36 | Key numbers | 14.3% / 9.2% / 6.2% (USD 2,236 / 1,445 / 973) | Supported | Table 1 | |
| 37 | Key numbers | ~61% research team travel | Supported | p. 4 | |
| 38 | Key numbers | ~10% seed (35% of materials) | Supported | p. 4 | |
| 39 | Key numbers | 59% / ~USD 24 / ~17% | Supported | p. 6 | 2,640 / 15,644 = 16.9% |
| 40 | Key numbers | 85% / 48% share of monitoring | Imprecise | p. 5 | Base of 48% not stated in source (fix 5) |
| 41 | Key numbers | ~70% communication from extension staff | Supported | p. 5 | |
| 42 | Key numbers | USD 128.13 (−10%, USD 1,550) | Supported | p. 6 | (15,644.23 − 1,550) / 110 = 128.13. 1,550 / 15,644 = 9.9% |
| 43 | Key numbers | USD 132.16 (−7.1%, USD 1,106) | Supported | p. 6 | Recomputed 132.17, rounding. 1,106 / 15,644 = 7.07% |
| 44 | Key numbers | ~USD 135 (−5%, USD 795), USD 1,324 at 50%, USD 1,854 at 70% | Supported | p. 7 | 134.99. 5.1%. 1,324 / 0.5 and 1,854 / 0.7 both give 2,648, consistent |
| 45 | Key numbers | ~USD 103 (USD 4,270) | Supported | p. 7 | Not reproducible (Source issue 1) |
| 46 | Key numbers | 15% (10%) | Supported | p. 6 | |
| 47 | Notes | Costs are marginal per farmer, not comparable with desousa-2024-asd cost per equivalent unit | Supported | p. 4 | Consistent with the desousa-2024-asd card |
| 48 | Notes | 24% travel cut ≈ USD 1,564 vs 1,550, 50.5% labour cut ≈ USD 1,129 vs 1,106 | Supported | p. 5 to 6 | Arithmetic correct. Not labelled as card's calculation (fix 6) |
| 49 | Notes | Guidelines set research visits at ~30%, ZARI reached ~25% | Supported | p. 5 | 30% comes from angudubo-2026-guide, correctly attributed |
| 50 to 62 | Frontmatter | 13 fields | See Metadata check | | 11 Supported, 1 Imprecise, 1 Not in source |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| 1. Combined scenario (about USD 103, USD 4,270 saved) cannot be rebuilt from the report's own scenarios. Travel + labour + 30% support = USD 3,451 (USD 110.85). 50% gives USD 3,980 (USD 106.04). 70% gives USD 4,510 (USD 101.22). USD 4,270 implies a support cut of about 61% | p. 6 to 7 (PDF 8 to 9) | No | See fix 1 |
| 2. Travel and labour savings come from "the same operational shift" but are each computed alone from USD 142.22. No joint figure is given (USD 2,656, USD 118.07 per farmer) | p. 6 (PDF 8) | No | Covered by fix 1 summary text and new Key numbers row |
| 3. Labour cut stated as 50.50%, but the USD 1,106 saving is 49.5% of labour (50.5% would be USD 1,129) | p. 6 | Partly (Note 3 gives the gap) | See fix 6 |
| 4. Base of "about 48%" (monitoring or all labour) is not stated | p. 5 (PDF 7) | No | See fix 5 |
| 5. Institution name differs. Cover title says "Zambia Agricultural and Research Institute". Body and suggested citation say "Zambia Agricultural Research Institute", and the citation adds "by the" | Cover, title page, p. 1, p. 8 | No (card title follows the cover, summary uses the correct name) | Optional: "- The cover title says 'Zambia Agricultural and Research Institute'. The body and the suggested citation use the institute's name, Zambia Agricultural Research Institute." |
| 6. Small rounding gaps in Table 1 and the text. Transport per farmer 1,445 / 110 = 13.14 (table 13.13). Communication 8.85 (table 8.84). Top three components sum to USD 13,226 (text 13,227). Labour scenario 132.17 (text 132.16). These come from unrounded inputs | p. 4, p. 6 | No | None needed |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: understand cost drivers and refine costing method (p. 1) | Yes | | |
| Design: 110 farmers, 8 options, 9 districts, visits, delivery model (p. 2) | Yes | | |
| Cost structure, Table 1 (p. 4) | Yes | | |
| Cost drivers: researcher field roles, participant support (p. 5 to 6) | Yes | | |
| Scenario savings and per-farmer costs (p. 6 to 7) | Yes | | |
| Joint effect of the single delegation shift (travel + labour, not given by the source) | No | Medium | Fix 1 |
| Scenario percentages: 24% travel, 50.50% labour, 18% materials (p. 5 to 6) | Notes only (24%, 50.5%), 18% missing | Medium | Fix 9 |
| Researcher time split does not change field implementation costs (p. 6) | No | Medium | Fix 8 |
| No completion, retention or data-quality data are reported, so "maintaining data quality" is asserted | Partly (not_established covers scenarios) | Medium | Fix 3 |
| Top three components = USD 13,227, about 85% (p. 4) | No | Low | Fix 9 |
| Transport drivers: seed distribution distances, training locations (p. 5) | No | Low | None needed |
| Four costing objectives (p. 2) | No | Low | None needed |
| Participant support matters for retention in a citizen-science model (p. 6) | Partly | Low | None needed |
| Authors' limitation: current operational decisions are the main limitation (p. 7) | Yes (conclusions) | | |
| Conclusions and four recommendations (p. 7) | Yes | | |

## Template compliance

- Summary word count: 447 (target 400 to 500). OK. With fixes 1 and 7 it becomes 499.
- Gist: 28 words. OK. Suggested gist is 29 words.
- Keywords: 12. OK.
- Questions: 6. OK.
- House style: tricot in lowercase throughout. maniva not used. OK.
- Long-format sections present. OK.
