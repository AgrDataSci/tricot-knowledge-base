---
id: angudubo-2026-guide
title: Tricot costing template guidelines
authors: Angudubo S, Benavente G, van Etten J
year: 2026
journal: Guidelines, Alliance of Bioversity International and CIAT (1000FARMS)
journal_short: Guide
article: 24 p.
type: guide
source: team
peer_reviewed: no
curated_card: no
doi: https://hdl.handle.net/10568/181933
open_copy: https://hdl.handle.net/10568/181933
license: see CGSpace record
data: Excel costing template, https://hdl.handle.net/10568/182169
crops: any crop; grain and legume version, and a version for roots, tubers and bananas (cassava, sweetpotato, banana, yam)
region: Global; examples from Uganda and Tanzania
keywords: tricot costing, cost per farmer, trial budget, costing template, activity-based costing, cost drivers, seed multiplication cost, labour cost, per diem, transport cost, sensitivity analysis, scenario analysis
gist: The 1000FARMS Excel template costs a tricot trial by activity and per farmer, using standard UN mileage and ITU phone rates across countries, and ranks cost drivers
not_established: any actual cost of a tricot trial (the numbers are worked examples, not results); that tricot is cheaper than other designs (the template costs one design and does not compare); that the UN mileage rates and ITU baskets match local prices in every country; that a 15% rise in labour adds about USD 12,000 to any trial (an illustrative figure with no stated baseline); that 30% research visits or the planned visits per farm are an optimum (the guide sets them as protocol defaults without evidence); that the template has been checked against actual trial spending (the guide reports no test)
relations:
  - usesMethodIn: vanetten-2020-guide  # the guide links to it for the tricot steps; trial preparation is steps 1 to 3 and seed distribution step 4
---

## Questions this paper answers

- How do I cost a tricot trial before committing to a budget?
- Which cost items does a tricot trial have, and how are they grouped?
- How do I estimate seed requirements and the cost of multiplying seed for the trial?
- How do I cost staff time, per diem, transport and phone bundles in a way that compares across countries?
- What is a fixed, variable or avoidable cost in a tricot trial?
- How do I find out which items drive the cost, and what a cheaper delivery model would save?

## Summary

Stephen Angudubo, Grecia Benavente and Jacob van Etten wrote this guide for the Excel costing template of the 1000FARMS platform. The template estimates the full cost of a tricot trial for one crop and splits it into components. Public and private breeding programmes can use it to plan budgets, compare trials across countries, find high-cost centres and note unnecessary spending.

The workbook has 15 worksheets filled in order, since later sheets draw on earlier ones. Users enter data only in white cells. Light green cells hold protected formulas, and sheet colours mark guidance, main input, minimal input and automatic sheets.

Trial dimensions set the context for everything else. They hold crop, country, institution, product profile, trial dates, block size, planting layout, number of farmers and varieties, and the number of monitoring visits by researchers and by extension staff. Two seed sheets turn these into seed needs and the land needed to produce them, one for grains and legumes based on 100-grain weight and one for roots, tubers and bananas based on cuttings per bag. A seed multiplication sheet then costs every input, labour task, material and service of the multiplication cycle and returns a cost per kilogram or per bag, which feeds the unit price of trial seed. Depending on sample size, seed may need to be multiplied for the trial rather than taken from on-station trials, so the guide counts multiplication as a planning cost.

Material sheets price seed, packaging, labels, agronomic inputs, data collection tools, training materials and participant support, then scale them by the number of farmers. A wages sheet converts monthly salaries into daily and hourly rates and records per diem and travel allowances by job role. Labour time records hours by role for each tricot activity, from trial preparation and field agent training to seed distribution, monitoring, data collection, yield measurement, product evaluation and farmer feedback. Travel, transport and communication sheets add per diem, fuel and vehicle costs and monthly phone bundles. An overview sheet sums all costs by category, per trial and per farmer.

Two choices make results comparable across countries. Vehicle costs use the UN mileage reimbursement rate, adjusted for inflation since 2019, rather than local fuel estimates. Communication uses the ITU low-consumption mobile basket of 70 minutes, 20 SMS and 500 MB per month, which covers ODK Collect and coordination calls.

The template also checks the design against the tricot protocol. Monitoring visits that exceed the planned number per farm trigger an alert, and research teams visit about 30% of trials for monitoring and yield measurement.

The last two sheets support planning. Sensitivity analysis changes one driver at a time, such as farmer numbers, visits, fuel, labour or materials, and ranks drivers by their dollar impact in a bar chart. Scenario analysis combines changes into best, base and worst cases without touching the baseline model.

## Methods in brief

- **Approach.** Costing by tricot activity, from trial preparation (tricot steps 1 to 3) and seed distribution (step 4) through monitoring, data collection, yield measurement, product evaluation and feedback. The guide defines fixed costs (do not change with farmer numbers), variable costs (grow with scale) and avoidable costs (could be cut, for example travel replaced by remote support), but does not say which template items fall in each class.
- **Currency and seed delivery.** All costs in USD, with the exchange rate stated and salary sources documented. Seed goes to a central point and extension or field agents pass it to farmers, so only the hours of key staff (a driver and a scientist or technician) count for seed distribution.
- **Inputs.** Project workplans, farmer registration forms, trial calendars, payroll or HR salary scales, market prices or supplier quotes, procurement records, travel policies and vehicle logs. Farmer numbers are cross-checked against seed distribution records or ClimMob enrolment.
- **Standard rates.** UN travel reimbursement rate per kilometre, inflation-adjusted from 2019. ITU ICT price basket for phone and data. Default 21 working days per month and 8 hours per day, editable.
- **Labour.** Hours per activity per role, multiplied by the number of staff in that role. Data collection hours are multiplied by the number of data collection moments (four for common bean).
- **Travel.** Per diem days by activity and role, plus single-day travel allowances. Researchers are assumed not to take part in routine data collection.
- **Sensitivity and scenarios.** Indices entered as whole numbers (110 for +10%). One driver changed at a time before combining. Assumptions dated in a comments column.
- **Scenario formula.** Estimated total cost is material × farmers × material index, plus monitoring labour × farmers × visits × labour index, plus fuel × visits × fuel index, plus other variable costs × farmers (for example calls).

## Stated limitations

- Results depend on real, traceable inputs. Errors in the trial dimensions or the overview sheet carry into every later sheet and scenario.
- UN mileage rates date from 2019 and need inflation adjustment.
- Root, tuber, banana and vegetable crops may need adjusted seed sheets.
- Percentage changes in the sensitivity analysis must be informed, not arbitrary.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 15 | Worksheets in the costing template | This guide |
| 30% | Share of trials the research team visits for monitoring and for yield measurement (definitions). The travel sheet says monitoring visits must cover at least 30% of trials | This guide |
| 21 days, 8 hours | Default working days per month and hours per day, editable | This guide |
| 70 min, 20 SMS, 500 MB | ITU low-consumption monthly mobile basket used for communication costs | This guide; ITU ICT price baskets |
| USD 2.68 | ITU basket price, Tanzania 2024, worked example | This guide; ITU |
| USD 1.00 to 1.26 (25.7%) | US inflation 2019 to 2025, used to update UN mileage rates, worked example | This guide; usinflationcalculator.com |
| 300 farmers, 363 days, 70 m² blocks | Worked example of trial dimensions, cassava in Uganda with NARO | This guide |
| 500 and 700 | Stem cuttings per 100 kg bag for cassava and vine cuttings per bag for sweetpotato | This guide |
| 0.30 × 200 × 2 = 120 | Worked example of total farm visits entered for two breeders who each visit 30% of 200 farms | This guide |
| about USD 12,000 | Illustrative change in total trial cost from a 15% rise in labour, sensitivity sheet note, baseline not given | This guide |

## Notes

- This is the main reference in the knowledge base for costing a tricot trial. Use it with the case studies angudubo-2026-zari (maize, Zambia) and angudubo-2026-naro (common bean, Uganda), and with the budgeting chapter of chase-2026-book, which Stephen Angudubo and Grecia Benavente wrote.
- The cost comparison in desousa-2024-asd is a single case study of potato trials in Rwanda. It compares tricot with RCBD per equivalent experimental unit, while this template costs one tricot trial per farmer and does not compare designs.
- The guide says to convert days after planting to months by dividing by 12. Dividing by about 30 is correct.
- The worked example gives a 70 m² block as 0.0175 acres; 70 m² is about 0.0173 acres.
- The sensitivity and scenario sheets refer to cell and column positions that may shift as the template is updated. Check them against the current Excel file.
- Source problem: the guide says to multiply the UN rate by the country's inflation rate (page 9). The factor to use is 1 plus the cumulative rate, as Figure 2 shows (USD 1.00 in 2019 is USD 1.26 in 2025). The example uses a US inflation calculator, not a country rate.
- Possible source problem: in the labour time sheet, the guide defines column E as the total number of farm visits. It then asks users to multiply hours per visit by the number of farms visited before entering column F, and column G multiplies column E by column F (page 13). If column E holds total visits, as defined, this counts the visits twice. Enter hours for a single visit in column F unless the current Excel file defines column E differently.
- Source problem: in the travel expenses sheet, the guide says monitoring days are farm visits multiplied by farms visited per day (page 14). Days should be visits divided by farms visited per day. Check the formula in the current Excel file.
- Possible source problem: per diem appears in the travel expenses sheet, with a rate by job role, and again in the transport sheet, with a single rate from trial dimensions cell B27 (pages 14 to 16). The guide does not say whether the overview adds both. Check that it does not count per diem twice.
- Source problem: the guide counts 15 worksheets but describes grain and RTB versions of the seed requirement and seed multiplication sheets, so the workbook may hold more sheets.
- Source problem: the definitions list three data collection moments for beans (page 3), while the labour time note counts four (page 13).
- Source problem: the definitions say research teams visit 30% of trials (page 3), while the travel sheet says monitoring visits must reach at least 30% (page 14).
- Source problem: a note on the unit prices sheet says to set the quantity in column D to one (page 8). Column D is the gross price and column E the quantity.
- Source problem: data analysis is defined as an activity (one person cleans and analyses all data, page 3), but the labour time sheet as described has no column for it.
- Source problem: the labour time text says costs come from daily wages (page 12), while the labour costs sheet multiplies hours by hourly rates (page 14).
- Source problem: the travel sheet assumes researchers do not take part in data collection (page 15), while the monitoring definition says the research team collects agronomic data on 30% of trials (page 3).
- Source problem: the example trial dimensions table is cut off (page 4), so cells B24 to B27 that later sheets use (planting units per trial, working days, hours, per diem) are not shown.
- Source problem: the seed sheet links say cell C5 feeds the land area of the same grain sheet, and the seed rate in cell C6 is not otherwise explained (page 5).
