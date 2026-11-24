---
id: steinke-2019-plosone
title: Prioritizing options for multi-objective agricultural development through the Positive Deviance approach
authors: Steinke J, Mgimiloko MG, Graef F, Hammond J, van Wijk MT, van Etten J
year: 2019
journal: PLOS ONE
journal_short: PLOS ONE
article: 14(2), e0212926
type: research article
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1371/journal.pone.0212926
open_copy: https://doi.org/10.1371/journal.pone.0212926
license: CC BY (Creative Commons Attribution License, version not stated in the PDF)
data: S1 Dataset, anonymized RHoMIS survey of 521 households (supporting information), no code published
crops: mixed farming systems (maize, cassava, pigeon pea and others)
region: South-Eastern Tanzania (Mtwara, Lindi and Tunduru district of Ruvuma)
keywords: positive deviance, Pareto optimality, household heterogeneity, trade-offs, RHoMIS, livelihood practices, targeting, multi-objective development, resource homologues, Tanzania
gist: Positive Deviance with Pareto-optimal residual performance on five objectives found 54 of 521 Tanzanian households doing better than expected, and 14 uncommon practices that plausibly explain this
not_established: that the 14 practices cause better household performance (they were identified in interviews, not tested); that the practices will improve outcomes for the resource-homologue households they are matched to; that positive deviants do better than other households in absolute terms on all five objectives; that the approach finds options not already used locally; that the same positive deviants or practices would emerge with other indicators, sample sizes or seasons; that this is a tricot trial or an on-farm experiment
---

## Questions this paper answers

- How can local farmer innovation be found systematically in survey data?
- How do you prioritize practices when food security, income, nutrition, environment and equity trade off?
- How can recommendations be targeted to households with different resources?
- How can RHoMIS-type household data feed into on-farm research priorities?

## Summary

The paper adapts the Positive Deviance approach, known from child nutrition, to agricultural development with several objectives at once. Development practitioners must choose which practices to promote, but objectives such as food security, income and environmental sustainability trade off, and households differ in their resources. The authors argue that some of the answers already exist among households that do unusually well given their means.

They surveyed 521 rural households in South-Eastern Tanzania with the RHoMIS tool, sampling 12 households at random per village from extension officers' lists. Five performance indicators were computed per household (caloric food security, dietary diversity, cash income, greenhouse gas emissions and a gender-equity proxy from decision-making shares). Median regression on land, livestock, household size, region and market access gave the expected performance for each household, and the residuals measured how much better or worse it did than its peers.

Households on the first Pareto front of these residuals (not dominated by any other household), plus a second front found after removing the first, were labelled positive deviants. This gave 54 households (12 on rank 1 and 42 on rank 2), about 10% of the sample. They did not differ from others in gender ratio, age, household size, land or livestock, but they had more formal education. In absolute terms they had higher food security and dietary diversity, but also higher emissions and the same gender equity. Relative to similar households, their advantage was strongest for food security and weakest for gender equity, where they did slightly worse than expected on average.

The team then revisited 15 of 18 selected positive deviants for qualitative interviews and identified 14 uncommon practices that plausibly explain their outcomes. Examples include resource-efficient maize and pigeon pea intercropping and the production of cassava planting material. Each surveyed household was matched to the three interviewed positive deviants with the most similar endowments (its resource homologues), and their practices were suggested to it. This reached 8% to 100% of households, depending on the practice.

The authors present this as an empirical, locally grounded starting point for planning interventions. They suggest it may need fewer assumptions than methods that predict the effects of new practices from household data, and it names concrete practices rather than broad categories. Farm visits also helped to screen out households that may have over-reported performance. But the method only finds practices already in use locally, and other indicators or more visits would likely give other deviants and practices.

The authors suggest that seeing these practices on real farms may lead other farmers to test them, perhaps with systematic on-farm experimentation formats, citing tricot as one example.

Positive deviants were unevenly spread, with significantly fewer in Lindi region (Region 2). The authors link their higher formal education to innovation and lower risk aversion, as well as better off-farm work. The anonymized survey of 521 households is published as supporting information. The authors suggest the method may also suit fields beyond agriculture where goals trade off.

## Methods in brief

- **Survey.** RHoMIS household survey in 44 randomly selected villages (20 in Mtwara, 20 in Lindi, 4 in Tunduru district of Ruvuma), 12 random households per village from extension officers' lists, 521 complete interviews.
- **Indicators.** Caloric food security (first principal component, 57% of variance, of food availability against 2,550 kcal per male adult equivalent, capped at 100%, and the number of food-secure months), harmonic mean of good- and lean-season dietary diversity, cash income from farm sales and off-farm work, IPCC Tier 1 greenhouse gas emissions (sign reversed so lower emissions score higher), and a gender-equity proxy from women's and men's shares in decision-making.
- **Expected performance.** Median regression per indicator on land, livestock, household size, region and village-level market orientation as a proxy for market access, with variables selected by AIC. Residuals give relative performance.
- **Positive deviants.** Pareto-optimal residual performance in five dimensions, rank 1 and rank 2 fronts, computed with the emoa R package.
- **Follow-up.** Sample split into 20 resource strata (land deciles by livestock above or below the median). One positive deviant per stratum for the 18 strata that had any, rank 1 preferred, chosen to maximize mean crowding distance. 15 interviewed in 12 villages with farm visits, plus 3 non-surveyed households as a comparison.
- **Targeting.** Each surveyed household matched by Euclidean distance on six endowments (agro-ecology, labor, finance, land, livestock, social capital) to its three most similar interviewed positive deviants (resource homologues).

## Stated limitations

- Self-reported survey data can be biased. The authors argue that the farm visits filter out households that over-reported performance.
- The method only finds practices already in use in the study area, so promising new technologies and institutional change may be missed.
- Other indicator definitions, a different survey size, more follow-up visits or another season would likely give different positive deviants and practices.
- Gender equity showed the weakest positive deviance, and households strong on gender equity tended to be weaker on other dimensions. This may reflect household priorities, a need for more radical innovation than farmer experimentation produces, or the narrow gender indicator used.
- Indicators were chosen from development paradigms, not with local stakeholders, and may not match local priorities.
- Limited demand may cap adoption of market-based practices (village shops, tree seedlings), and some practices may harm others (crop stockpiling can raise food prices, hired tractors cut wage work for landless people).
- The method needs prior survey data collection, though a RHoMIS baseline can serve both impact assessment and the analysis.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 521 households | Completed RHoMIS interviews | This paper |
| 44 villages | Randomly selected, 20 in Mtwara, 20 in Lindi, 4 in Tunduru (Ruvuma) | This paper |
| 12 per village | Households sampled at random from extension lists | This paper |
| 54 (12 + 42) | Positive deviants on Pareto ranks 1 and 2, about 10% of sample | This paper |
| 5 | Performance dimensions | This paper |
| 2,550 kcal | Daily requirement per male adult equivalent used for food security | Pauw and Thurlow 2011 (ref 38), cited in this paper |
| 0.65 SD | Mean scaled positive deviance for caloric food security, the strongest dimension (GHG 0.33, cash income 0.07) | This paper |
| 0.67 vs 0.23 and 6.56 vs 4.00 | Median caloric food security and dietary diversity (food groups), positive deviants vs others, significant | This paper |
| 395 vs 212 kg CO2-eq/year | Median GHG emissions, positive deviants vs others, significant (higher for deviants) | This paper |
| r = -0.35 and -0.29 | Correlation of gender-equity deviance with cash income and food security deviance (significant) | This paper |
| 15 of 18 | Selected positive deviants interviewed, in 12 villages | This paper |
| 14 | Deviant practices identified | This paper |
| 2.2 (max 5) | Mean number of deviant practices per interviewed household with any practice | This paper |
| 8%–100% | Share of households targeted per practice by resource homologues | This paper |
| 323 households (62%) | Households whose three resource homologues were deviants I, VIII and XIII (labor scheduling, small shop, wage labor) | This paper |
| ~1–5 persons/km² | Rural population density in the study area | Perfect and Majule 2010 (ref 29), cited in this paper |

## Notes

- Not a tricot trial. Relevant to tricot for selecting technologies to test and for socio-economic characterization with RHoMIS, which de Sousa et al. 2024 recommends in a light version.
- The paper itself cites tricot (van Etten et al. 2016, ref 54) as a possible format for farmers to test the identified practices (p15).
- Card's own reading, not stated in the paper: for tricot users the method is a possible way to choose which options to test and for which households, and an early link between RHoMIS household data and farmer-led innovation.
- Table 3 lists 476 other households, but 521 minus 54 positive deviants is 467 (source inconsistency).
- In Table 4 the land size strata n add to 52, not 54 (source inconsistency).
- Table 4 scaled deviance is hard to reconcile with the raw means (dietary diversity +2.1 raw but -0.93 scaled), so the ranking of dimensions should be quoted with care (source issue).
- The abstract says positive deviants did slightly better for social equity, but Results and Table 4 show slightly worse than expected (source inconsistency).
- Small shop (Ss) is observed once in Table 7 but twice in Table 5 (deviants V and XIII) (source inconsistency).
- Table 5 lists 14 interviewed positive deviants, while the text says 15 (source inconsistency).
- Table 3 does not mark the cash income difference (686 vs 281 US$) as significant, and median GHG emissions of positive deviants are almost twice those of other households, more than the "slightly worse" in the text (source inconsistency).
