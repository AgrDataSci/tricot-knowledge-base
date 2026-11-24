# Card review: angudubo-2026-guide

- **Card:** papers/angudubo-2026-guide.md
- **Source:** papers-pdf/angudubo-et-al-2026a.pdf (24 pages: cover, title page, contents, then printed pages 1 to 21. PDF page = printed page + 3.)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 64 (51 in the claim table, 13 frontmatter fields) |
| Supported | 57 |
| Imprecise | 4 |
| Not in source | 3 (1 in the Summary, plus doi and data, which the PDF does not contain and which could not be checked online) |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 15 (2 flagged in the card) |
| Important omissions | 4 (medium importance, none high) |
| Metadata issues | 2 (gist wording, not_established could be stronger) |

The card is accurate and well organised. Almost every sentence matches the guide, the Key numbers are correctly attributed to ITU and the US inflation calculator, and the two arithmetic slips it flags are real. The most important fix is to add Notes on source problems the card does not flag, mainly the monitoring formulas on printed pages 13 and 14 and the inflation step on page 9, because a user who follows the guide literally would get wrong costs. The Summary also carries one sentence of outside knowledge that belongs in Notes.

## Fixes needed

1. **Unflagged formula problems in the source (pages 9, 13, 14, 14 to 16).** The card does not warn users about several steps in the guide that would give wrong numbers if followed as written. See "Source issues" rows 3 to 6. Suggested Notes text, ready to paste:

   - The guide says to multiply the UN rate by the country's inflation rate (page 9). The factor to use is 1 plus the cumulative rate, as Figure 2 shows (USD 1.00 in 2019 is USD 1.26 in 2025). The example uses a US inflation calculator, not a country rate.
   - In the labour time sheet, the text asks users to multiply hours per farm by the number of farms visited before entering column F, but column G then multiplies column F by the number of visits again (page 13). Enter hours for a single visit in column F, and check the formula in the current Excel file.
   - In the travel expenses sheet, the guide says monitoring days are farm visits multiplied by farms visited per day (page 14). Days should be visits divided by farms visited per day. Check the formula in the current Excel file.
   - Per diem appears in the travel expenses sheet, with a rate by job role, and again in the transport sheet, with a single rate from trial dimensions cell B27 (pages 14 to 16). Check that the overview does not count it twice.

2. **Summary, sentence 3: outside knowledge in the Summary.** Card: "It is the core documentation for costing tricot, and the case studies on maize in Zambia and common bean in Uganda apply it." The guide does not mention these case studies or call itself the core documentation (pages 1 to 21). The first Notes bullet already says this, so delete the sentence from the Summary. Replacement: delete the sentence. No other change is needed (the Summary drops to about 441 words).

3. **Methods, Approach bullet: "ten tricot steps" and cost classes.** Card: "Activity-based costing tied to the ten tricot steps. Costs are classed as fixed ..., variable ... or avoidable ..." The guide never says "ten". It maps trial preparation to steps 1 to 3 and seed distribution to step 4, and links to the tricot guide for the steps (pages 1 and 3). It defines fixed, variable and avoidable costs (page 3) but does not say the template tags each item with a class. Replacement:

   - **Approach.** Costing by tricot activity, from trial preparation (tricot steps 1 to 3) and seed distribution (step 4) through monitoring, data collection, yield measurement, product evaluation and feedback. The guide defines fixed costs (do not change with farmer numbers), variable costs (grow with scale) and avoidable costs (could be cut, for example travel replaced by remote support), but does not say which template items fall in each class.

4. **Key numbers, 30% row.** Card: "Minimum share of trials visited by the research team for monitoring and yield measurement." The definitions say 30% for monitoring and for yield measurement, without "minimum" (page 3). Only the travel sheet says monitoring visits must be at least 30% (page 14). The Summary says "about 30%", so the card is also inconsistent with itself. Replacement row:

   | 30% | Share of trials the research team visits for monitoring and for yield measurement (definitions). The travel sheet says monitoring visits must cover at least 30% of trials | This guide |

5. **Summary, sentence 2: "drop unnecessary spending".** The guide says the tool helps in noting unnecessary additional expenses (page 1), which is weaker than dropping them. Replacement: "The template estimates the full cost of a tricot trial for one crop and splits it into components. Public and private breeding programmes can use it to plan budgets, compare trials across countries, find high-cost centres and note unnecessary spending."

6. **Add the remaining source issues to Notes.** See "Source issues" rows 7 to 15 for ready-to-paste text. These are low importance but help users who fill in the template.

7. **Methods: add currency, seed delivery and the scenario formula (medium omissions).** Add these bullets:

   - **Currency and seed delivery.** All costs in USD, with the exchange rate stated and salary sources documented. Seed goes to a central point and extension or field agents pass it to farmers, so only the hours of key staff (a driver and a scientist or technician) count for seed distribution.
   - **Scenario formula.** Estimated total cost is material × farmers × material index, plus monitoring labour × farmers × visits × labour index, plus fuel × visits × fuel index, plus other variable costs × farmers (for example calls).

8. **Key numbers: add two worked examples.**

   | 0.30 × 200 × 2 = 120 | Worked example of total farm visits entered for two breeders who each visit 30% of 200 farms | This guide |
   | about USD 12,000 | Illustrative change in total trial cost from a 15% rise in labour, sensitivity sheet note, baseline not given | This guide |

9. **not_established: add three items.** Suggested full field:

   not_established: any actual cost of a tricot trial (the numbers are worked examples, not results); that tricot is cheaper than other designs (the template costs one design and does not compare); that the UN mileage rates and ITU baskets match local prices in every country; that a 15% rise in labour adds about USD 12,000 to any trial (an illustrative figure with no stated baseline); that 30% research visits or the planned visits per farm are an optimum (the guide sets them as protocol defaults without evidence); that the template has been checked against actual trial spending (the guide reports no test)

10. **gist (optional).** The current gist is accurate but lists sheets. Suggested gist (27 words): "The 1000FARMS Excel template costs a tricot trial by activity and per farmer, using standard UN mileage and ITU phone rates across countries, and ranks cost drivers"

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Tricot costing template guidelines | "Tricot Costing Template Guidelines" (title page, PDF p. 2), same in suggested citation | Supported |
| authors | Angudubo S, Benavente G, van Etten J | Title page and citation (PDF p. 2) | Supported |
| year | 2026 | Title page and citation (PDF p. 2) | Supported |
| journal | Guidelines, Alliance of Bioversity International and CIAT (1000FARMS) | Cover says Guidelines with 1000FARMS logo (PDF p. 1). Template by the 1000FARMS Platform team (p. 1) | Supported |
| article | 24 p. | PDF has 24 pages (21 numbered) | Supported |
| type | guide | A user guide for an Excel template (pp. 1, 21) | Supported |
| doi | https://hdl.handle.net/10568/181933 | Not printed in the PDF. Online check blocked | Not in source (not an error, check CGSpace) |
| license | see CGSpace record | No licence statement in the PDF | Supported (correct fallback) |
| data | Excel costing template, https://hdl.handle.net/10568/182169 | PDF refers to the accompanying Excel worksheets (p. 21) but gives no link. Same handle is used in the zari and naro cards | Not in source (not an error, check CGSpace) |
| crops | any crop, grain and legume version, and an RTB version (cassava, sweetpotato, banana, yam) | Grain and RTB seed sheets (p. 5), cassava, sweetpotato, banana, yam (p. 6). Common bean also used as an example (pp. 3, 13). Vegetables may need separate sheets (p. 6) | Supported ("any crop" is slightly broad, since the guide says vegetables may need their own sheets) |
| region | Global, examples from Uganda and Tanzania | Uganda cassava example (p. 4), Tanzania ITU price (p. 9), cross-country use (p. 1) | Supported |
| gist | Step-by-step guide to the 1000FARMS Excel template ... | Matches content | Supported (lists sheets more than findings, optional rewrite in fix 10) |
| not_established | three items | All three are correct boundaries | Supported (could add three items, fix 9) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | The three authors wrote the guide for the 1000FARMS Excel template | Supported | p. 1, title page | |
| 2 | Summary | Full and component cost for one crop, for public and private programmes to plan, compare countries, spot high-cost centres, drop unnecessary spending | Imprecise | p. 1 | Source says noting unnecessary expenses, not dropping them. Fix 5 |
| 3 | Summary | Core documentation, applied by the Zambia maize and Uganda bean case studies | Not in source | pp. 1 to 21 | Outside knowledge. True per the zari and naro cards, but belongs in Notes. Fix 2 |
| 4 | Summary | 15 worksheets, filled in order | Supported | pp. 1, 3 | See source issue 7 on the count |
| 5 | Summary | White input cells, light green formulas, sheet colours by purpose | Supported | p. 3 | |
| 6 | Summary | Trial dimensions set the context for everything else | Supported | p. 5 | |
| 7 | Summary | Trial dimensions content (crop, country, institution, profile, dates, block, layout, farmers, varieties, visits by researchers and extension staff) | Supported | p. 4, text and example table | |
| 8 | Summary | Two seed sheets, grain by 100-grain weight, RTB by cuttings per bag | Supported | p. 5 | |
| 9 | Summary | Seed multiplication sheet costs inputs, labour, materials, services, returns cost per kg or bag, feeds unit price | Supported | pp. 6, 7 | Also per sucker or plantlet (banana) and per tuber cutting (yam), p. 6 |
| 10 | Summary | Material sheets price seed, packaging, labels, inputs, data tools, training, participant support, scaled by farmers | Supported | pp. 7, 8, 10 | |
| 11 | Summary | Wages sheet converts monthly to daily and hourly, records per diem and travel allowance | Supported | pp. 10, 11 | |
| 12 | Summary | Labour time records hours by role for each activity | Supported | pp. 12, 13 | |
| 13 | Summary | Travel, transport, communication sheets add per diem, fuel, vehicle costs, phone bundles | Supported | pp. 14 to 17 | |
| 14 | Summary | Overview sums costs by category, per trial and per farmer | Supported | p. 17 | |
| 15 | Summary | Two choices make results comparable across countries | Supported | pp. 8, 16 | |
| 16 | Summary | UN mileage rate, inflation-adjusted since 2019, rather than local fuel estimates | Supported | p. 9 | The guide's stated reason is to avoid overestimating fuel, operation and maintenance |
| 17 | Summary | ITU low-consumption basket 70 min, 20 SMS, 500 MB per month, covers ODK Collect and coordination | Supported | pp. 8, 9 | |
| 18 | Summary | Template checks the design against the tricot protocol | Supported | pp. 13, 14 | |
| 19 | Summary | Alert when monitoring visits exceed the planned number per farm | Supported | pp. 13, 14 | The check is total visits against farmers × planned visits per farm (B16 × B19 or B20) |
| 20 | Summary | Research teams visit about 30% of trials for monitoring and yield measurement | Supported | p. 3 | p. 14 says at least 30% for monitoring. See fix 4 |
| 21 | Summary | Last two sheets support planning | Supported | p. 2 | Both are marked optional |
| 22 | Summary | Sensitivity changes one driver at a time and ranks drivers by dollar impact in a bar chart | Supported | pp. 18, 19 | |
| 23 | Summary | Scenario combines changes into best, base and worst cases without touching the baseline | Supported | pp. 19 to 21 | |
| 24 | Methods | Activity-based costing tied to the ten tricot steps | Imprecise | pp. 1, 3 | "ten" is not in the source. Fix 3 |
| 25 | Methods | Costs classed as fixed, variable or avoidable | Imprecise | p. 3 | Only definitions. The guide does not say the template classifies items. Fix 3 |
| 26 | Methods | Input sources (workplans, registration forms, calendars, payroll, prices, procurement, travel policies, vehicle logs) | Supported | pp. 4, 10, 11, 15, 16 | |
| 27 | Methods | Farmer numbers cross-checked with seed distribution records or ClimMob enrolment | Supported | pp. 4, 18, 20 | |
| 28 | Methods | UN rate inflation-adjusted from 2019, ITU basket, 21 days and 8 hours editable | Supported | pp. 8, 9, 11 | |
| 29 | Methods | Hours per activity per role × number of staff | Supported | p. 12 | |
| 30 | Methods | Data collection hours × collection moments (four for common bean) | Supported | p. 13 | See source issue 8 |
| 31 | Methods | Per diem days by activity and role, plus single-day travel allowances | Supported | pp. 14, 15 | |
| 32 | Methods | Researchers assumed not to take part in routine data collection | Supported | p. 15 | "routine" is the card's word and sensibly handles the tension in source issue 13 |
| 33 | Methods | Indices as whole numbers (110 for +10%) | Supported | pp. 19, 21 | |
| 34 | Methods | One driver at a time before combining | Supported | pp. 19, 21 | |
| 35 | Methods | Assumptions dated in a comments column | Supported | p. 19 | |
| 36 | Limitations | Results depend on traceable inputs, errors in trial dimensions or overview carry forward | Supported | pp. 3, 5, 21 | |
| 37 | Limitations | UN rates date from 2019 and need inflation adjustment | Supported | p. 9 | |
| 38 | Limitations | RTB and vegetable crops may need adjusted seed sheets | Supported | pp. 5, 6 | |
| 39 | Limitations | Sensitivity percentages must be informed, not arbitrary | Supported | p. 18 | |
| 40 | Key numbers | 15 worksheets | Supported | p. 1 | |
| 41 | Key numbers | 30% minimum share for monitoring and yield measurement | Imprecise | pp. 3, 14 | "Minimum" applies only to monitoring in the travel sheet. Fix 4 |
| 42 | Key numbers | 21 days, 8 hours | Supported | p. 11 | |
| 43 | Key numbers | 70 min, 20 SMS, 500 MB, attributed to ITU | Supported | p. 8 | Attribution correct |
| 44 | Key numbers | USD 2.68, Tanzania 2024 | Supported | p. 9, text and Figure 1 | Attribution correct |
| 45 | Key numbers | USD 1.00 to 1.26 (25.7%), 2019 to 2025 | Supported | p. 9, Figure 2 | Attribution correct. 1.257 rounds to 1.26 |
| 46 | Key numbers | 300 farmers, 363 days, 70 m² blocks, cassava, Uganda, NARO | Supported | p. 4, example table | 1 Jan to 30 Dec 2025 is 363 days (checked). 10 m × 7 m = 70 m² |
| 47 | Key numbers | 500 and 700 cuttings per bag, cassava and sweetpotato | Supported | p. 6 | The source gives the bag as 100 kg for both |
| 48 | Notes | desousa-2024-asd compares designs, this template costs one tricot trial and does not compare | Supported | pp. 1 to 21 | Matches the desousa-2024-asd card |
| 49 | Notes | Guide says divide days after planting by 12, about 30 is correct | Supported | p. 4 | Correctly flagged source error (363 / 30.4 ≈ 12 months) |
| 50 | Notes | 70 m² given as 0.0175 acres, actually about 0.0173 | Supported | p. 4 | 70 / 4046.86 = 0.01730 (checked) |
| 51 | Notes | Cell and column positions may shift as the template is updated | Supported | p. 7 | Card's own advice. The guide says cell references may vary by item count |

The first Notes bullet (cross-references and the chase-2026-book budgeting chapter) is a cross-reference and was not counted. It matches the chase-2026-book card, which lists Budgeting by Stephen Angudubo and Grecia Benavente. The relation `usesMethodIn: vanetten-2020-guide` is supported: the guide links to hdl 10568/109942 for the tricot steps (p. 1), which is that card's handle.

## Source issues

| # | Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|---|
| 1 | Days after planting to months: divide by 12 | p. 4 | Yes | (already in card) |
| 2 | 70 m² given as 0.0175 acres | p. 4 | Yes | (already in card) |
| 3 | Inflation step says multiply by the inflation rate, and by the country rate, while the example uses a US calculator and a factor of 1.26 | pp. 9, 10 | No | See fix 1, first bullet |
| 4 | Column F (hours per visit): text says multiply by farms visited, then column G multiplies by visits again | p. 13 | No | See fix 1, second bullet |
| 5 | Travel sheet: monitoring days = visits × farms per day (should be divided) | p. 14 | No | See fix 1, third bullet |
| 6 | Per diem appears in both the travel expenses sheet (role rates) and the transport sheet (single rate in B27). Possible double count | pp. 1, 14 to 16 | No | See fix 1, fourth bullet |
| 7 | 15 worksheets counted, but grain and RTB versions of two seed sheets are described | pp. 1, 5, 6 | No | The guide counts 15 worksheets but describes grain and RTB versions of the seed requirement and seed multiplication sheets, so the workbook may hold more sheets. |
| 8 | Data collection moments for beans: three in the definitions (vegetative, reproductive, postharvest), four in the labour note (registration, vegetative, reproductive, socio-economic) | pp. 3, 13 | No | The definitions list three data collection moments for beans, while the labour time note counts four. |
| 9 | 30% of trials (definitions) versus at least 30% (travel sheet) | pp. 3, 14 | No (card uses both) | The definitions say research teams visit 30% of trials, while the travel sheet says monitoring visits must reach at least 30%. |
| 10 | Note on unit prices says set gross quantity in column D to one, but column D is gross price and column E is quantity | p. 8 | No | A note on the unit prices sheet says to set the quantity in column D to one. Column D is the gross price and column E the quantity. |
| 11 | Data analysis is defined as an activity but has no column in the labour time or travel sheets as described | pp. 3, 12 to 14 | No | Data analysis is defined as an activity (one person cleans and analyses all data), but the labour time sheet as described has no column for it. |
| 12 | Labour time text says costs come from daily wages, the labour costs sheet uses hourly rates | pp. 12, 14 | No | Low priority, optional |
| 13 | Travel sheet assumes researchers do no data collection, while monitoring is defined as the research team collecting agronomic data on 30% of trials | pp. 3, 15 | Partly (Methods says "routine" data collection) | The travel sheet assumes researchers do not take part in data collection, while the monitoring definition says the research team collects agronomic evaluation data on 30% of trials. |
| 14 | Example table cut off at row 21, so cells B24 to B27 that the text uses later (planting units per trial, working days, hours, per diem) are not shown | pp. 4, 5, 11, 16 | No | Low priority, optional |
| 15 | Seed sheet interlinkage says cell C5 feeds the land area of the same grain sheet, and cell C6 (seed rate) is not otherwise explained | p. 5 | No | Low priority, optional |

## Completeness

| Item in the source | In card? | Importance | Suggested addition |
|---|---|---|---|
| Aim: full and component costs, transparency, cross-country comparison (p. 1) | Yes | High | |
| Structure of the 15 sheets and order of filling (pp. 1 to 3) | Yes | High | |
| Standard UN and ITU rates (pp. 8, 9, 16) | Yes | High | |
| Monitoring and yield visits on 30% of trials, visit alert (pp. 3, 13, 14) | Yes | High | |
| Sensitivity and scenario sheets (pp. 18 to 21) | Yes | High | |
| Scenario cost formula (p. 20) | No | Medium | Fix 7, scenario bullet |
| Costs in USD with the exchange rate stated, salary sources documented (pp. 3, 11, 12) | No | Medium | Fix 7, currency bullet |
| Seed delivery plan: central point, agents distribute, only key staff hours counted (p. 12) | No | Medium | Fix 7, seed delivery bullet |
| Seed may need separate multiplication rather than on-station seed, depending on sample size (p. 6) | No | Medium | Add to the Summary after the seed multiplication sentence: "Depending on sample size, seed may need to be multiplied for the trial, so the guide counts multiplication as a planning cost." |
| Worked monitoring example, 0.30 × 200 × 2 = 120 (p. 13) | No | Low | Fix 8 |
| Illustrative USD 12,000 for +15% labour (p. 18) | No | Low | Fix 8 and fix 9 |
| Activity definitions: one person does data analysis, food product evaluation is consumer testing, every farmer gets feedback (p. 3) | Partly | Low | Optional |
| Tips: version control, values-only copy before sharing, triangulate two price points (pp. 12, 20, 21) | No | Low | Optional |
| Conclusion: accurate, transparent, comparable budgeting (p. 21) | Yes, in spirit | Medium | |
| Authors' own limitations: the guide has no limitations section. The card's list is drawn fairly from its cautions | Yes | Medium | |

## Template compliance

- Summary word count: 466 (target 400 to 500). Pass. After deleting sentence 3 it is about 441, still in range.
- Gist: 27 words (under 30). Pass.
- Keywords: 12 (8 to 12). Pass.
- Questions: 6 (4 to 7). Pass.
- House style: tricot is lowercase throughout, except the title, which quotes the published title. Pass. maniva does not appear.
- Long-format sections are all present.
