---
id: steinke-2019-plosone
title: Prioritizing options for multi-objective agricultural development through the Positive Deviance approach
authors: Steinke J, Mgimiloko MG, Graef F, Hammond J, van Wijk MT, van Etten J
year: 2019
journal: PLOS ONE
journal_short: PLOS ONE
article: 14(2), e0212926
type: research article
doi: https://doi.org/10.1371/journal.pone.0212926
open_copy: https://doi.org/10.1371/journal.pone.0212926
license: CC BY 4.0
data: S1 Dataset, anonymized RHoMIS survey of 521 households (supporting information)
crops: mixed farming systems (maize, cassava, pigeon pea and others)
region: South-Eastern Tanzania
keywords: positive deviance, Pareto optimality, household heterogeneity, trade-offs, RHoMIS, livelihood practices, targeting, multi-objective development
gist: Adapts Positive Deviance to agriculture, using Pareto-optimal performance across five objectives to find 54 outlier households and 14 locally proven practices
---

## Questions this paper answers

- How can local farmer innovation be found systematically in survey data?
- How do you prioritize practices when food security, income, nutrition, environment and equity trade off?
- How can recommendations be targeted to households with different resources?
- How can RHoMIS-type household data feed into on-farm research priorities?

## Summary

The paper adapts the Positive Deviance approach, known from child nutrition, to agricultural development with several objectives at once. Development practitioners must choose which practices to promote, but objectives such as food security, income and environmental sustainability trade off, and households differ in their resources. The authors argue that some of the answers already exist among households that do unusually well given their means.

They surveyed 521 rural households in South-Eastern Tanzania with the RHoMIS tool, sampling 12 households at random per village from extension officers' lists. Five performance indicators were computed per household (caloric food security, dietary diversity, cash income, greenhouse gas emissions and a gender-equity proxy from decision-making shares). Regression on land, livestock, household size, region and market access gave the expected performance for each household, and the residuals measured how much better or worse it did than its peers.

Households on the first two Pareto fronts of these residuals, those not outperformed on all objectives by any other household, were labelled positive deviants. This gave 54 households, about 10% of the sample. They did not differ from others in gender ratio, age, household size, land or livestock, but they had more formal education. Their advantage was strongest for food security and weakest for social equity.

The team then revisited 15 of 18 selected positive deviants for qualitative interviews and identified 14 uncommon practices that plausibly explain their outcomes. Examples include resource-efficient maize and pigeon pea intercropping and the production of cassava planting material. Using a resource-homologue approach, each practice was matched to other households with similar endowments, reaching between 8% and 100% of the sample depending on the practice.

The authors present this as an empirical, locally grounded starting point for planning interventions, which needs fewer assumptions than model-based prioritization and names concrete practices rather than broad categories. The qualitative follow-up also filters out households that over-reported performance.

For tricot users, the paper offers a way to choose which technologies to test and for whom, and an early example of linking RHoMIS household data with farmer-led innovation.

Positive deviants were unevenly spread, with significantly fewer in one of the three regions, and they had received more formal education, which the authors link to innovation and lower risk aversion as well as better off-farm opportunities. The anonymized survey of 521 households is published as supporting information, so the method can be reproduced or extended to other areas and objectives beyond agriculture where trade-offs between goals matter.

## Methods in brief

- **Survey.** RHoMIS household survey, 12 random households per village, 521 complete interviews.
- **Indicators.** Food availability against 2,550 kcal per male adult equivalent (capped at 100%), harmonic mean of good- and lean-season dietary diversity, cash income, IPCC Tier 1 greenhouse gas emissions, and a gender-equity proxy.
- **Expected performance.** Regression on land, livestock, household size, region and village-level market orientation as a proxy for market access.
- **Positive deviants.** Pareto-optimal residual performance in five dimensions, rank 1 and rank 2 fronts, computed with the emoa R package.
- **Follow-up.** 18 households chosen by maximum crowding distance, 15 interviewed in 12 villages.
- **Targeting.** Resource-homologue matching on six endowments (agro-ecology, labor, finance, land, livestock, social capital).

## Stated limitations

- Self-reported survey data can be biased, which the qualitative step only partly filters.
- Gender equity showed the smallest advantage, possibly because it needs more radical change than farmer experimentation produces.
- Findings come from one region of Tanzania and need testing elsewhere.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 521 households | Completed RHoMIS interviews | This paper |
| 12 per village | Households sampled at random from extension lists | This paper |
| 54 (12 + 42) | Positive deviants on Pareto ranks 1 and 2, about 10% of sample | This paper |
| 5 | Performance dimensions | This paper |
| 2,550 kcal | Daily requirement per male adult equivalent used for food security | Tanzania national recommendation, cited in this paper |
| 15 of 18 | Selected positive deviants interviewed, in 12 villages | This paper |
| 14 | Deviant practices identified | This paper |
| 8%–100% | Share of households targeted per practice by resource homologues | This paper |
| ~1–5 persons/km² | Rural population density in the study area | Cited in this paper |

## Notes

- Not a tricot trial. Relevant to tricot for selecting technologies to test and for socio-economic characterization with RHoMIS, which de Sousa et al. 2024 recommends in a light version.
