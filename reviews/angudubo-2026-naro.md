# Card review: angudubo-2026-naro

- **Card:** papers/angudubo-2026-naro.md
- **Source:** papers-pdf/angudubo-et-al-2026c.pdf (15 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

Page numbers below are PDF page numbers (1 to 15). The printed page labels differ. PDF p1 is the cover, p2 is blank, p3 is the title and citation page, p4 to p5 are the executive summary (printed i and ii), and p6 to p15 are printed pages 1 to 10. Table 1 is on PDF p9. The report has no figures and only one table.

## Overview

| Check | Result |
|---|---|
| Claims checked | 67 |
| Supported | 60 |
| Imprecise | 7 |
| Not in source | 0 |
| Contradicted | 0 |
| Important omissions | 7 |
| Metadata issues | 2 |

The card is accurate. Every number in the Key numbers table matches the report, and I recomputed all cost shares, per-farmer costs, scenario savings and the card's derived figures from Table 1. All the arithmetic is correct. The main weaknesses are a gist that drops the word "marginal", a summary sentence that misdescribes the labour and travel scenarios, derived numbers in Notes that are not clearly labelled as the card's own calculations, and a few gaps (no fixed-cost figure, untested sensitivity claims, baseline deviating from the costing assumptions). The most important fix is the gist, because it is the field users read first and it can be stretched into "a tricot trial costs USD 92 per farmer".

## Fixes needed

1. **Gist omits "marginal" and presents the scenario as a fact about cost.** The card says the trial "cost USD 92 per farmer" and that better design "could cut it to USD 47". The source reports marginal costs only, with fixed costs excluded (PDF p9), and the USD 47.40 figure is a modelled scenario (PDF p13). Suggested replacement (29 words, no semicolon):

   `gist: A 120-farmer common bean tricot trial in Uganda had marginal costs of USD 92 per farmer, driven by researcher labour and transport, and scenarios cut this to USD 47`

2. **Summary misdescribes the delegation scenarios.** The card says delegation lowers cost "to USD 63.97, mostly through labour, and to USD 58.81 when the travel savings are added". In the source the USD 63.97 scenario counts labour savings only, a separate scenario counts travel savings only (USD 83.90), and USD 58.81 is both applied together (PDF p13). The word "added" also suggests the savings add up, which they do not (see fix 5). Replace the sentence with:

   `Delegating monitoring, data collection and yield measurement to trained field agents lowers the cost per farmer to USD 63.97 through labour savings alone and to USD 83.90 through travel savings alone. With both applied together it falls to USD 58.81.`

3. **Note on the executive summary is incomplete.** The card says the executive summary "calls travel expenses the largest operational item". The executive summary does call travel "the true heavyweight of the operational budget", but in the bullet just above it calls labour "the largest driver of trial expenditures" (PDF p4). It also never mentions transport (29%), and it gives materials as 7% where Table 1 gives 6.3% (PDF p4, p9). Replace the note with:

   `- The executive summary does not match Table 1. It calls labour (37%) the largest driver, but also calls travel expenses (27%) the true heavyweight of the operational budget. It does not mention transport (29%), which Table 1 and the body rank second. It gives materials as 7%, while Table 1 gives 6.3% (our calculation: 6.7% if communication is added, which may explain the 7%).`

4. **Derived numbers in Notes are correct but not labelled as derived.** I checked them. Per diem plus labour plus transport is 2,764.8 + 4,069.0 + 3,236.7 = USD 10,070.5, which matches the body's USD 10,070.4 within rounding (PDF p9). Adding the travel allowance gives USD 10,325.9, which is 93.3% of USD 11,070. 81% of USD 4,069 is USD 3,295.9. The scenario labour saving of USD 3,393.7 is 83.4% of field labour. Replace the two notes with:

   `- The body says travel expenses, labour and transport total USD 10,070.4 (about 91%). Our calculation from Table 1 (not in the report): per diem, labour and transport sum to USD 10,070.5, so the body figure leaves out the travel allowance (USD 255.4). With the allowance the three components total USD 10,325.9, or 93.3% of total marginal cost.`

   `- Our calculation (not in the report): the stated 81% cut in field labour (USD 4,069) is about USD 3,296. The labour-savings scenario saves USD 3,393.7, which is about 83% of field labour. The report does not explain the gap.`

5. **Add a note on the scenarios that do not add up.** Labour-only saving (USD 3,393.7) plus travel-only saving (USD 1,001.8) is USD 4,395.5, but the combined scenario saves USD 4,012.8 (PDF p13). The report says "the combined effect is larger", which holds only against each scenario alone. Also, USD 1,001.8 is almost exactly 31% of transport cost (USD 1,003.4), the transport cut stated on PDF p11, so the "travel savings" scenario seems to be that transport cut. Add to Notes:

   `- Our calculation (not in the report): the labour-only and travel-only savings sum to USD 4,395.5, but the combined scenario saves USD 4,012.8, so the savings are not additive. The travel-only saving (USD 1,001.8) is close to 31% of transport cost (USD 1,003), so it seems to be the transport cut that the report gives for the same shift.`

6. **Add notes on what the report does not show.** The executive summary claims sensitivity analyses on farmer numbers, monitoring frequency and fuel prices (PDF p4), but the body reports no results for them. The report gives no figure for fixed costs, and no underlying quantities (staff days, kilometres, number of sessions, daily rates), so the scenarios cannot be checked from the report. The costing assumptions say field agents lead all monitoring (PDF p8), while the baseline shows research-team visits taking 77% of monitoring labour (PDF p9). The report says it examines how deviations from the standard tricot steps affect cost (PDF p7). Add to Notes:

   `- The executive summary mentions sensitivity analyses on farmer numbers, monitoring frequency and fuel prices, but the body reports no results for them. The report gives no figure for fixed costs and no underlying quantities (staff days, kilometres, sessions, daily rates), so its scenarios cannot be recomputed from the report.`

   `- The costing assumptions describe the prescribed tricot model, in which field agents lead all monitoring and researchers do spot checks. The baseline costs record how the trial deviated from it, with research-team visits taking 77% of monitoring labour. The report frames its cost drivers as these deviations.`

7. **Methods bullet attributes UN rates to vehicle costs.** The card says "UN travel reimbursement rates for vehicle costs". This report says UN travel reimbursement standards are used for "travel expenses" (PDF p8). The guide card (angudubo-2026-guide) says the guidelines use the UN mileage rate for vehicle costs, so the card may be right in substance, but this report does not say so. It also says inflation adjustment is applied only "where needed". Replace the bullet with:

   `- **Standard rates.** UN travel reimbursement standards for travel costs (applied as a per-kilometre vehicle rate in the guidelines, see angudubo-2026-guide), ITU country price baskets for communication, market prices adjusted for inflation where needed for materials, and NARO salary scales for labour.`

8. **First stated limitation is the card's inference, not the authors' words.** The authors state that fixed costs are excluded from Table 1 (PDF p9). They do not say the total "understates" the full cost, and they give no fixed-cost figure. Replace with:

   `- Only marginal costs are reported. Fixed costs (trial preparation, coordination and central training of field agents) are excluded from Table 1, and the report gives no figure for them.`

9. **Data field names a tool, not data.** The handle 10568/182169 is the Excel costing template (PDF p8). No cost dataset for this trial is published. Replace with:

   `data: none published for this trial (costing template at https://hdl.handle.net/10568/182169 and guidelines at https://hdl.handle.net/10568/181933)`

10. **not_established can be extended.** The current items are fair. Three more stretches are likely: that the scenario savings were achieved in practice (they are modelled), that cost per farmer falls as farmer numbers grow (claimed in the executive summary with no numbers, PDF p4), and that the figures are audited spending (the report calls them estimates made with the template and standard rates, PDF p7 to p8). The template requires semicolons as separators in this field. Suggested replacement:

    `not_established: the full cost of the trial (fixed costs such as trial preparation and central training are excluded and not reported); that the lower-cost scenarios keep data quality, which is assumed, not measured; that the scenario savings were achieved in the field (they are modelled with the template); that cost per farmer falls as farmer numbers grow (the executive summary claims it but shows no numbers); that the figures are audited expenditure (the report presents template estimates using standard rates); that tricot is cheaper than other designs (no comparison was made); costs for other crops or countries`

11. **Optional summary additions (keeps the summary under 500 words).** The card asks "What should a lean research supervision protocol for tricot look like?" but the summary only says "with a quality checklist". The checklist content is on PDF p14. In the last summary paragraph, replace "a single trial manager auditing 20% to 30% of farms with a quality checklist" with:

    `a single trial manager auditing a sample of farms (for example 20% to 30%) with a checklist covering plot layout, variety allocation, seed packages, labels, farmer understanding, records and ClimMob data`

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Insights into the costing of on-farm testing. A case study of ... (NARO) | Same words, with a colon after "testing" (p1, p3) | Supported (period for colon is a minor style change) |
| authors | Angudubo S, Benavente G, van Etten J, Mugisa I | Same order (p1, p3) | Supported |
| year | 2026 | 2026 (p1, p3) | Supported |
| journal | Case study report, Alliance of Bioversity International and CIAT (1000FARMS) | Publisher is the Alliance (p3), 1000FARMS branding (p1), described as a case study (p6) | Supported |
| article | 15 p. | PDF has 15 pages (cover, blank page, i to ii, 1 to 10) | Supported |
| type | report | Report (p7) | Supported |
| doi | https://hdl.handle.net/10568/183339 | No handle printed in the PDF | Not checkable from source |
| license | see CGSpace record | No licence stated in the PDF | Supported (follows template rule) |
| data | costing template, https://hdl.handle.net/10568/182169 | Handle is the costing template, not trial data (p8) | Imprecise (fix 9) |
| crops | common bean | Common bean, Phaseolus vulgaris (p4) | Supported |
| region | Uganda (Lwengo, Nakaseke and Hoima districts) | Same districts, two zones (p7) | Supported |
| gist | USD 92 per farmer ... could cut it to USD 47 | Marginal costs only (p9), scenario (p13) | Imprecise (fix 1) |
| not_established | Four items | All four fair (p9, p13, no comparison anywhere) | Supported, could be extended (fix 10) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Angudubo and colleagues costed NARO's bean tricot trial run through NaCRRI | Supported | p1, p7 | |
| 2 | Summary | First season of 2025 | Supported | "first production season of 2025 (March – July)" (p7) | |
| 3 | Summary | Support from AVISA and 1000FARMS | Supported | p7 | |
| 4 | Summary | 24 varieties from four product profiles (yellow, sugars, red mottled and red, white) | Supported | 24 varieties (p4), four profiles (p7) | |
| 5 | Summary | 120 farms in Lwengo, Nakaseke, Hoima, two agro-ecological zones | Supported | p7 | |
| 6 | Summary | 360 plots | Supported | p4 | |
| 7 | Summary | Breeders, research officers, research assistants, technicians, extension field agents | Supported | p4, p15 | |
| 8 | Summary | Applied the 1000FARMS costing template and guidelines | Supported | p8 | |
| 9 | Summary | Only marginal costs that grow with farmer numbers are counted | Supported | p9 | "As in the Zambia maize case" agrees with angudubo-2026-zari |
| 10 | Summary | Office-based preparation and central training are fixed and left out | Supported | p9 | |
| 11 | Summary | USD 11,070, USD 92.25 per farmer | Supported | Table 1 (p9) | 11,070 / 120 = 92.25. Table rows sum to 11,070.1 (rounding) |
| 12 | Summary | Labour 37%, transport 29%, travel 27% | Supported | Table 1 (p9), p9 to p10 | Recomputed: 36.8, 29.2, 27.3 |
| 13 | Summary | Materials 6%, communication under 1% | Supported | Table 1 (p9) | Recomputed: 6.3, 0.4. Executive summary says 7% (p4) |
| 14 | Summary | Monitoring is 86% of labour costs | Supported | p9 | |
| 15 | Summary | Two research-team visits to about 25% of farms take 77% of monitoring labour | Supported | p9 | |
| 16 | Summary | Because breeder, research officer and assistant travelled together | Supported | p9 | |
| 17 | Summary | Research travel is 51% of travel expenses | Supported | p4, p10 | |
| 18 | Summary | Seed 16% and sisal about 35% of material costs | Supported | p10 | |
| 19 | Summary | Authors name two cost drivers | Supported | p11 | |
| 20 | Summary | Driver 1: multiple research roles on routine fieldwork, duplicating visits | Supported | p11 | |
| 21 | Summary | Driver 2: field training, parish-level seed points, many small sessions | Supported | p11 to p12 | |
| 22 | Summary | Random visits without clustered routes added distance | Supported | p10 | Stated under transport, not as a named driver. Card wording ("also") is fair |
| 23 | Summary | Delegation lowers cost to USD 63.97 "mostly through labour" | Imprecise | p13 | It is the labour-only scenario (fix 2) |
| 24 | Summary | USD 58.81 "when the travel savings are added" | Imprecise | p13 | Both changes together, savings not additive (fixes 2 and 5) |
| 25 | Summary | Central training, seed distribution and clustering give USD 81.32 | Supported | p13 | Recomputed saving 1,311.6 vs 1,311.2 stated (rounding) |
| 26 | Summary | All changes give USD 47.40, 49%, about USD 5,382 | Supported | p13 | Recomputed: 48.6%, 5,382.0 |
| 27 | Summary | Authors conclude tricot is cost-effective, constraint is delivery design | Supported | p13 | Attributed to authors. No comparison or benefit measure supports "cost-effective" (covered in not_established) |
| 28 | Summary | Recommendations (field agents, trial manager auditing 20% to 30%, central training, bulk seed to hubs, 10 to 20 farmer hubs, bundling, SOPs and MOUs) | Supported | p5, p13 to p14 | 20% to 30% is given as an example |
| 29 | Methods | 1000FARMS activity-based Excel template with guidelines | Supported | p8 | |
| 30 | Methods | UN rates "for vehicle costs" | Imprecise | p8 says "travel expenses" | Fix 7 |
| 31 | Methods | ITU baskets, inflation-adjusted market prices, NARO salary scales | Supported | p8 | Inflation adjustment "where needed" |
| 32 | Methods | Assumptions: ten steps, research team roles, about 30% yield measurement, field agents lead monitoring | Supported | p8 | These describe the prescribed model, not what happened (fix 6) |
| 33 | Methods | Marginal costs only, 10% to 15% researcher share, 15% applied | Supported | p8, p12 | |
| 34 | Methods | No fertilizer or pesticide, sisal strings supplied | Supported | p10 | |
| 35 | Methods | Scenario list (delegation, central training, 60% fewer km, 50% fewer sessions, combined) | Supported | p11 to p13 | |
| 36 | Limitations | Fixed costs excluded, so total understates full cost | Imprecise | p9 | Exclusion is stated. "Understates" is the card's inference (fix 8) |
| 37 | Limitations | Decentralization needs selection, training, spot checks, accountability, feedback | Supported | p11 | |
| 38 | Limitations | Farmers may already meet in groups of 15 to 20, hubs must be compact | Supported | p14 | |
| 39 | Key numbers | 120 farmers, 24 varieties, 360 plots, March to July 2025, three districts | Supported | p4, p7 | |
| 40 | Key numbers | USD 11,070 / USD 92.25 | Supported | p9 | |
| 41 | Key numbers | 36.8% (USD 4,069) | Supported | p9 | |
| 42 | Key numbers | 29.2% (USD 3,236.7) | Supported | p9 | |
| 43 | Key numbers | 25.0% + 2.3% (USD 2,764.8, USD 255.4) | Supported | p9 | |
| 44 | Key numbers | 6.3% / 0.4% (USD 702.8, USD 41.4) | Supported | p9 | |
| 45 | Key numbers | 86% / 77% | Supported | p9 | |
| 46 | Key numbers | 51% | Supported | p4, p10 | |
| 47 | Key numbers | 16% / ~35% | Supported | p10 | |
| 48 | Key numbers | ~81% / ~31% | Supported | p11 | |
| 49 | Key numbers | USD 63.97 (−31%, USD 3,393.7) | Supported | p13 | Recomputed: 30.7%, 3,393.6 |
| 50 | Key numbers | USD 83.90 (−9%, USD 1,001.8) | Supported | p13 | Recomputed: 9.0%, 1,002.0 |
| 51 | Key numbers | USD 58.81 (−36%, USD 4,012.8) | Supported | p13 | Recomputed: 36.2%, 4,012.8 |
| 52 | Key numbers | USD 81.32 (−12%, USD 1,311.2) | Supported | p13 | Recomputed: 11.8%, 1,311.6 |
| 53 | Key numbers | USD 47.40 (−49%, USD 5,382.2) | Supported | p13 | Recomputed: 48.6%, 5,382.0 |
| 54 | Key numbers | 10% / 13% from central training | Supported | p12 | |
| 55 | Key numbers | 8% / 11% from fewer seed km and fewer sessions | Supported | p12 | |
| 56 | Notes | Executive summary calls travel the largest operational item | Imprecise | p4 | It also calls labour the largest driver and omits transport (fix 3) |
| 57 | Notes | Body total USD 10,070.4 (about 91%) leaves out travel allowance, with it USD 10,325.9 (about 93%) | Supported | p9 | Arithmetic correct (10,070.5 and 93.3%). Not labelled as derived (fix 4) |
| 58 | Notes | 81% of field labour is about USD 3,296, below USD 3,393.7 | Supported | p11, p13 | Arithmetic correct (3,295.9). Not labelled as derived (fix 4) |
| 59 | Notes | Zambia case: USD 142 per farmer, travel and materials largest | Supported | angudubo-2026-zari card (42%, 29%) | Cross-card check, not this source |
| 60 | Frontmatter | gist | Imprecise | p9, p13 | Fix 1 |
| 61 | Frontmatter | not_established | Supported | p9, p13 | Fair, can be extended (fix 10) |
| 62 | Frontmatter | crops: common bean | Supported | p4 | |
| 63 | Frontmatter | region | Supported | p7 | |
| 64 | Frontmatter | data | Imprecise | p8 | Fix 9 |
| 65 | Frontmatter | license | Supported | none in PDF | |
| 66 | Frontmatter | article: 15 p. | Supported | PDF page count | |
| 67 | Frontmatter | authors | Supported | p1, p3 | |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: estimate costs, find cost drivers, examine how deviations from standard tricot steps affect cost (p7) | Partly | Medium | Fix 6, second note |
| Trial purpose: farmer evidence for variety advancement and dissemination in the legumes programme (p7) | No | Low | Optional phrase in the first summary paragraph |
| Design: three randomly assigned varieties per farmer, 120 farmers, 360 plots (p4, p7) | Yes | High | |
| Costs are estimates with template standard rates, from programme data inputs (p7, p8, p15) | Partly (Methods only) | Medium | Fix 10 |
| No fixed-cost figure and no underlying quantities (staff days, km, sessions, rates) | No | Medium | Fix 6, first note |
| Main cost shares and per-farmer cost (p9) | Yes | High | |
| Labour, transport and travel drivers (p9 to p12) | Yes | High | |
| Combined central delivery scenario: travel −10%, transport −32% (p12) | No | Medium | Add Key numbers row: `\| 10% / 32% \| Cut in travel / transport with fully centralized, cluster-based training, seed distribution and farmer sessions \| This paper \|` |
| Scenario savings are not additive (derived from p13) | No | Medium | Fix 5 |
| Executive summary sensitivity claims with no results in body (p4) | No | Medium | Fix 6, first note, and fix 10 |
| Baseline deviates from the costing assumptions (p8 vs p9) | No | Medium | Fix 6, second note |
| Quality-assurance checklist content (p14) | No | Medium | Fix 11 |
| Participant support (transport refunds for central meetings) as a material-related cost (p10) | No | Low | Optional |
| Seed delivery sometimes combined with planting support, adding km (p10) | No | Low | Optional |
| ClimMob seed calculator and separate seed production planning (p8, p10) | No | Low | Optional |
| Limit field-based training to exceptional cases, bundle farmer training, seed distribution and establishment support per hub (p14) | Partly | Low | Covered by "bundled activities" |
| Four costing objectives (p7) | No | Low | Not needed |
| Authors' conclusion and recommendations (p13 to p15) | Yes | High | |
| Authors' caveat on data quality under decentralization (p11) | Yes | High | |

Important omissions (high or medium, not in card): aim framed as deviations, no fixed-cost or quantity data, combined central scenario numbers, non-additive savings, sensitivity claims without results, baseline versus assumptions, checklist content. That is 7.

## Template compliance

- Summary word count: 419 (target 400 to 500). Compliant. Fixes 2 and 11 add about 30 words and keep it under 500.
- Gist: 28 words (under 30). Compliant in length, but see fix 1. The suggested replacement is 29 words.
- Keywords: 12 (target 8 to 12). Compliant.
- Questions: 6 (target 4 to 7). Compliant. The question on the lean supervision protocol is only thinly answered (fix 11).
- House style: tricot is lowercase throughout. maniva does not appear. No em dashes found in the card.
- Key numbers: all rows say "This paper", which is correct. The report cites no numbers secondhand.
- Relations: usesMethodIn angudubo-2026-guide (guidelines cited on p8, handle 10568/181933 matches that card) and usesMethodIn vanetten-2020-guide (The Tricot Guide cited on p8, handle 10568/109942 matches that card) are both correct.
