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
gist: Step-by-step guide to the 1000FARMS Excel template that costs a tricot trial by activity, from seed multiplication to labour, travel and communication, with sensitivity and scenario analysis
not_established: any actual cost of a tricot trial (the numbers are worked examples, not results); that tricot is cheaper than other designs (the template costs one design and does not compare); that the UN mileage rates and ITU baskets match local prices in every country
relations:
  - usesMethodIn: vanetten-2020-guide  # costs the ten tricot steps described in the guide
---

## Questions this paper answers

- How do I cost a tricot trial before committing to a budget?
- Which cost items does a tricot trial have, and how are they grouped?
- How do I estimate seed requirements and the cost of multiplying seed for the trial?
- How do I cost staff time, per diem, transport and phone bundles in a way that compares across countries?
- What is a fixed, variable or avoidable cost in a tricot trial?
- How do I find out which items drive the cost, and what a cheaper delivery model would save?

## Summary

Stephen Angudubo, Grecia Benavente and Jacob van Etten wrote this guide for the Excel costing template of the 1000FARMS platform. The template estimates the full cost of a tricot trial for one crop and splits it into components, so public and private breeding programmes can plan budgets, compare trials across countries, spot high-cost centres and drop unnecessary spending. It is the core documentation for costing tricot, and the case studies on maize in Zambia and common bean in Uganda apply it.

The workbook has 15 worksheets filled in order, since later sheets draw on earlier ones. Users enter data only in white cells. Light green cells hold protected formulas, and sheet colours mark guidance, main input, minimal input and automatic sheets.

Trial dimensions set the context for everything else. They hold crop, country, institution, product profile, trial dates, block size, planting layout, number of farmers and varieties, and the number of monitoring visits by researchers and by extension staff. Two seed sheets turn these into seed needs and the land needed to produce them, one for grains and legumes based on 100-grain weight and one for roots, tubers and bananas based on cuttings per bag. A seed multiplication sheet then costs every input, labour task, material and service of the multiplication cycle and returns a cost per kilogram or per bag, which feeds the unit price of trial seed.

Material sheets price seed, packaging, labels, agronomic inputs, data collection tools, training materials and participant support, then scale them by the number of farmers. A wages sheet converts monthly salaries into daily and hourly rates and records per diem and travel allowances by job role. Labour time records hours by role for each tricot activity, from trial preparation and field agent training to seed distribution, monitoring, data collection, yield measurement, product evaluation and farmer feedback. Travel, transport and communication sheets add per diem, fuel and vehicle costs and monthly phone bundles. An overview sheet sums all costs by category, per trial and per farmer.

Two choices make results comparable across countries. Vehicle costs use the UN mileage reimbursement rate, adjusted for inflation since 2019, rather than local fuel estimates. Communication uses the ITU low-consumption mobile basket of 70 minutes, 20 SMS and 500 MB per month, which covers ODK Collect and coordination calls.

The template also checks the design against the tricot protocol. Monitoring visits that exceed the planned number per farm trigger an alert, and research teams visit about 30% of trials for monitoring and yield measurement.

The last two sheets support planning. Sensitivity analysis changes one driver at a time, such as farmer numbers, visits, fuel, labour or materials, and ranks drivers by their dollar impact in a bar chart. Scenario analysis combines changes into best, base and worst cases without touching the baseline model.

## Methods in brief

- **Approach.** Activity-based costing tied to the ten tricot steps. Costs are classed as fixed (do not change with farmer numbers), variable (grow with scale) or avoidable (could be cut, for example travel replaced by remote support).
- **Inputs.** Project workplans, farmer registration forms, trial calendars, payroll or HR salary scales, market prices or supplier quotes, procurement records, travel policies and vehicle logs. Farmer numbers are cross-checked against seed distribution records or ClimMob enrolment.
- **Standard rates.** UN travel reimbursement rate per kilometre, inflation-adjusted from 2019. ITU ICT price basket for phone and data. Default 21 working days per month and 8 hours per day, editable.
- **Labour.** Hours per activity per role, multiplied by the number of staff in that role. Data collection hours are multiplied by the number of data collection moments (four for common bean).
- **Travel.** Per diem days by activity and role, plus single-day travel allowances. Researchers are assumed not to take part in routine data collection.
- **Sensitivity and scenarios.** Indices entered as whole numbers (110 for +10%). One driver changed at a time before combining. Assumptions dated in a comments column.

## Stated limitations

- Results depend on real, traceable inputs. Errors in the trial dimensions or the overview sheet carry into every later sheet and scenario.
- UN mileage rates date from 2019 and need inflation adjustment.
- Root, tuber, banana and vegetable crops may need adjusted seed sheets.
- Percentage changes in the sensitivity analysis must be informed, not arbitrary.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 15 | Worksheets in the costing template | This guide |
| 30% | Minimum share of trials visited by the research team for monitoring and yield measurement | This guide |
| 21 days, 8 hours | Default working days per month and hours per day, editable | This guide |
| 70 min, 20 SMS, 500 MB | ITU low-consumption monthly mobile basket used for communication costs | This guide; ITU ICT price baskets |
| USD 2.68 | ITU basket price, Tanzania 2024, worked example | This guide; ITU |
| USD 1.00 to 1.26 (25.7%) | US inflation 2019 to 2025, used to update UN mileage rates, worked example | This guide; usinflationcalculator.com |
| 300 farmers, 363 days, 70 m² blocks | Worked example of trial dimensions, cassava in Uganda with NARO | This guide |
| 500 and 700 | Stem cuttings per 100 kg bag for cassava and vine cuttings per bag for sweetpotato | This guide |

## Notes

- This is the main reference in the knowledge base for costing a tricot trial. Use it with the case studies angudubo-2026-zari (maize, Zambia) and angudubo-2026-naro (common bean, Uganda), and with the budgeting chapter of chase-2026-book, which Stephen Angudubo and Grecia Benavente wrote.
- The cost comparison in desousa-2024-asd is a single case study of potato trials in Rwanda. It compares tricot with RCBD per equivalent experimental unit, while this template costs one tricot trial per farmer and does not compare designs.
- The guide says to convert days after planting to months by dividing by 12. Dividing by about 30 is correct.
- The worked example gives a 70 m² block as 0.0175 acres; 70 m² is about 0.0173 acres.
- The sensitivity and scenario sheets refer to cell and column positions that may shift as the template is updated. Check them against the current Excel file.
