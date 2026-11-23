---
id: sharma-2025-jafr
title: Understanding farmer preferences through citizen science. Insights on potato varieties in Nigeria
authors: Sharma K, Atieno E, Mugo J, de Sousa K, van Etten J, Nyawade S
year: 2025
journal: Journal of Agriculture and Food Research
journal_short: J Agric Food Res
article: 23, 102135
type: research article
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1016/j.jafr.2025.102135
open_copy: https://doi.org/10.1016/j.jafr.2025.102135
license: CC BY-NC-ND 4.0
data: available on request (data availability statement), supplementary tables S2 and S3 at https://doi.org/10.1016/j.jafr.2025.102135
software: ClimMob, PlackettLuce
crops: potato
region: Nigeria (Plateau State)
keywords: potato, tricot, Nigeria, CIP clones, Marabel, market orientation, subsistence farmers, bootstrap, farmer segments, decentralized variety testing
gist: tricot with 295 potato farmers in Plateau State, Nigeria, ranks three CIP clones significantly above the check Marabel and shows market-oriented and subsistence farmers value different traits
not_established: that tricot improved adoption or uptake of these varieties, which was not measured; that CIP398208.29 is less preferred than Marabel, since the difference was not significant; that the four cohorts describe all farmers, since they cover 189 of 295 farmers and the tree covers 132; that gender and education do not matter for potato preference in general; that the results hold outside Plateau State
---

## Questions this paper answers

- Which potato clones do Nigerian farmers prefer over the check variety?
- How do market orientation and household traits change variety preference?
- Which traits drive potato farmers' overall preference in Plateau State?
- How stable are Plackett-Luce tree splits under bootstrapping?

## Summary

Potato is emerging as an important crop in Nigeria, but top-down breeding often overlooks farmer input, so released varieties may not suit local conditions. The study evaluates whether tricot, combined with digital tools, better reflects farmer needs.

Farmers in seven local government areas of Plateau State (Barikin Ladi, Bassa, Bokkos, Jos North, Jos South, Mangu and Pankshin) evaluated six anonymized CIP potato clones alongside the check variety Marabel, three entries per farmer. Four of the clones were released in 2023. Trial design and allocation ran on ClimMob, and data were collected through a mobile app and ODK. Of 300 farmers, 295 had validated data. Farmers ranked the best and worst option for each trait in four rounds, two in the vegetative stage (germination, pest and disease resistance, drought and flood tolerance), one at harvest (yield, bacterial wilt damage, maturity, tuber size and appearance, marketability) and one after harvest (ease of sale, dormancy, taste after cooking).

CIP clones CIP392797.22 and CIP393371.157 ranked top, with log-worth of 0.620 and 0.311 relative to the check (the abstract gives 0.309). CIP393371.58 was also above the check (0.167), and CIP381381.13 did not differ from it. CIP398208.29 and CIP398190.200 were least preferred (−0.085 and −0.465), but only CIP398190.200 was significantly below Marabel. Ease of sale after harvest, yield, disease resistance, taste and bacterial wilt damage were among the traits most linked to overall preference. A tree analysis on 132 farmers split first by age, at 38.2 years. Further splits used the share of potatoes sold (42.4%, younger farmers only), household size, distance to market and education. The authors report that splits held in over 93% of 1,000 bootstrap samples. Clustering of 189 farmers gave four cohorts by age, household size and business involvement, from 17 to 108 farmers each. Business involvement mattered more than age or household size. Market-oriented farmers prioritized commercial traits, while subsistence farmers emphasized resilience.

The authors conclude that participatory, data-driven breeding that integrates local knowledge can improve adoption, resilience and food security.

The discussion asks whether farmers are truly at the center of national breeding and release programmes. The three most preferred clones are in the national release pipeline, but CIP398190.200, despite being officially released, was among the least preferred because dormancy-related poor germination undermined early establishment, a trait rarely examined in institutional trials. The check Marabel also ranked low. Farmers valued its early maturity for market timing, but its short dormancy, poor storability and limited post-harvest use reduced its appeal. The authors argue that farmer choices reflect behavioral factors, such as risk aversion and planning for storage, household consumption or sales, and not only field traits. Household size, age, market involvement and distance to markets shaped which traits farmers prioritized, in line with the idea that different farmer types need different options. Recognizing these dynamics, the authors conclude, can explain why officially endorsed varieties can diverge from what farmers adopt. ClimMob allowed real-time tracking of the trial, and its quality checks flagged five farmers with skipped rankings or missing data.

## Methods in brief

- **Design.** Balanced incomplete block design set up in ClimMob. Each farmer got three of seven entries (six CIP clones and the check Marabel) as Options A, B and C, with 40 certified sprouted seed tubers per option, planted in three plots of 9 m² at 0.75 m × 0.3 m with a standard fertilizer protocol.
- **Data.** Extension agents recorded best and worst rankings in four rounds (two vegetative, harvest, postharvest), each with an overall ranking, plus socio-economic data and GPS, using ODK and ClimMob.
- **Sample.** 300 farmers in seven LGAs, 295 validated. The tree analysis covers 132 farmers and the cohort analysis 189, without explanation.
- **Analysis.** Plackett-Luce log-worth with Marabel as reference, Kendall tau and stepwise trait selection, a tree (called CART, with Plackett-Luce estimates per node) on socio-economic covariates, k-means clustering into four cohorts labelled with help from a large language model, PCA, likelihood-ratio tests, and 1,000 bootstrap samples for stability.

## Stated limitations

- Scaling the approach will require overcoming limits in digital access, institutional inertia and integration with formal breeding systems.
- Limited digital infrastructure, uneven digital literacy, unequal access to mobile phones and institutional resistance to decentralized data can slow uptake of tricot in formal breeding.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 300 / 295 farmers | Recruited / with validated data | This paper |
| 7 LGAs | Local government areas in Plateau State | This paper |
| 6 + 1 | CIP clones tested / check variety (Marabel) | This paper |
| 0.620 / 0.311 | Log-worth of CIP392797.22 / CIP393371.157 vs the check (abstract gives 0.309 for CIP393371.157) | This paper |
| 0.167 / 0.050 | Log-worth of CIP393371.58 (p = 0.028) / CIP381381.13 (not significant) | This paper |
| −0.085 / −0.465 | Log-worth of CIP398208.29 (not significant) / CIP398190.200 (p < 0.001) | This paper |
| 38.2 years / 42.4% | Tree cutoffs for age (first split) / share of potatoes sold (younger farmers only) | This paper |
| 6.7 members / 8 km | Cutoffs for household size / distance to market in the tree and cohort analysis | This paper |
| 24 / 17 / 108 / 40 | Farmers in cohorts A to D (8, 6, 37 and 14% of 295) | This paper |
| 132 / 189 | Farmers in the tree / in the cohort analysis | This paper |
| >93% / >90% | Bootstrap stability of genotype splits / key traits (1,000 samples) | This paper |

## Notes

- Compare with kang-2025-expagric, where market orientation also splits potato preferences in Rwanda.
- The text (p. 7) says each tree node "retained" certain genotypes, for example Marabel and CIP393371.58 for younger farmers selling 42.4% or more. The node plots in Fig. 7 (p. 9) show CIP392797.22 on top in all seven nodes (approximate chart reading). Use the tree text with care.
- Problem in the source: the log-worth of CIP393371.157 is 0.309 in the abstract and 0.311 in the results (p. 5).
- Problem in the source: the abstract describes three assessment stages, but the methods describe four data rounds, with two in the vegetative stage (p. 3).
- Problem in the source: the tree covers 132 farmers and the cohort analysis 189, out of 295 with validated data. The paper does not explain the difference.
- Problem in the source: the four cohorts combine age and household size (young and small, old and large), so age and household effects cannot be separated.
- Problem in the source: the paper defines log-worth as the negative log of a p-value (p. 4 to 5). This is not the usual Plackett-Luce definition, which is the log of the estimated worth.
- Problem in the source: Table 3 (p. 10) lists some traits twice in the overall rows, so its overall results should be read with care.
- Problem in the source: the abstract calls CIP398208.29 least preferred, but it does not differ significantly from Marabel (p = 0.259).
- In the pooled likelihood-ratio test, drought tolerance, pest resistance, dormancy and germination were not significant (Table 3, p. 10).
- Gender and education showed no significant association in CART and were dropped, though education appears in one tree split (p. 5, p. 7).
- Card's observation, not stated by the authors: the trial covers one state, and the cohorts range from 17 to 108 farmers, so cohort-level results rest on small groups.
