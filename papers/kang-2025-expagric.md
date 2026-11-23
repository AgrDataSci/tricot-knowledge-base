---
id: kang-2025-expagric
title: Integrating environmental, socio-economic, and biological data in a farmer-led potato trial for enhanced varietal assessment in Rwanda
authors: Kang G, de Sousa K, Manners R, van Etten J, Backes G, Rukundo P, Nduwumuremyi A, Ellison J, Tuyishime E, Mendes T, Griebel S
year: 2025
journal: Experimental Agriculture
journal_short: Exp Agric
article: 61, e18, 1-26
type: research article
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1017/S0014479725100100
open_copy: https://doi.org/10.1017/S0014479725100100
license: CC BY 4.0
data: data and R code on GitHub, https://github.com/AgrDataSci/potato-oft-genetic-gain
software: PlackettLuce, gosset, climatrends
crops: potato
region: Rwanda (Gicumbi, Nyamagabe)
keywords: potato, tricot, RHoMIS, socio-economic covariates, temperature, on-station vs on-farm, variety preference, market orientation, marketability, gender, Plackett-Luce trees, PLADMM
gist: In a 460-farmer potato tricot trial in Rwanda, old varieties ranked highest, yield ranks shifted with temperature, marketability with crop income, and on-station values predicted on-farm ranks poorly
not_established: that new potato varieties are worse than old ones in general (several did not differ significantly from Kirundo, and the old-variety lead may partly reflect the large warm-site group); that on-station trials cannot predict farm performance in general (one on-station season, nine varieties, two imputed); that temperature itself causes the yield rank changes (the biological causes were not identified); that crop income or gender cause the preference differences (associations in a subset of households); results for all of Rwanda (two districts, two seasons)
---

## Questions this paper answers

- How can tricot data be linked with socio-economic (RHoMIS), climate and station data?
- Which potato varieties do Rwandan farmers prefer, old or new?
- Which traits drive farmers' overall preference for potato varieties?
- Do market-oriented and subsistence farmers prefer different varieties?
- How well do on-station results align with on-farm rankings?

## Summary

Potato is central to food security in Rwanda but production growth has slowed, and improved varieties need to fit farmers' conditions and preferences to be adopted. The study tests the value of linking a tricot trial with environmental, socio-economic and on-station data.

In seasons 2021A and 2021B, 460 farmers in the main potato districts of Gicumbi and Nyamagabe each tested three of eleven varieties, allocated randomly in incomplete blocks (1380 plots). Farmers ranked 17 traits at five stages, from 45 days after planting to 60 days after harvest. Of all farmers, 283 were also surveyed with the RHoMIS household tool. The varieties included two released before 1990 (Cruza and Kirundo) and nine released in 2019 and 2020. On-station trials from season 2018B gave genotypic values for nine varieties. Values for Cruza and Gisubizo, which were not in these trials, were imputed as the average of the other nine.

Overall, Kirundo and Cruza ranked first and second in all three final evaluations (overall performance, willingness to plant, overall preference), and Ndeze and Nkunganire ranked last. Several newer varieties, such as Gisubizo and Kazeneza, were close behind. Against farmers' own varieties they did not differ significantly, so the authors see them as possible alternatives. Marketability after storage had the strongest link with the three final evaluations (Kendall τ 0.40 to 0.45), followed by yield (0.27 to 0.38).

A Plackett-Luce tree for yield split farmers at a 90th percentile of day temperature of 23.75 °C. In the warmer group (280 farmers), Kirundo ranked first but did not differ significantly from Cruza, Ndamira and Seka. In the cooler group (113 farmers), Twihaze ranked first, close to Seka and Kazeneza, and Ndamira ranked last. The authors suggest the large warm group may partly explain the old varieties' high overall ranks.

On-station values did not reliably predict on-farm rankings. In the cool group, varieties with lower on-station tuber weight ranked higher for yield. In the warm group, varieties with higher on-station virus severity ranked higher. Only tuber number per plant had the expected positive link. On-station bacterial wilt resistance showed no significant link with farmer rankings for bacterial wilt.

For marketability after storage, a tree with household covariates split farmers by annual crop income at 24.95 and 259.48 USD. Low-income farmers rated Cruza as highly marketable, and taste was linked most to marketability. High-income farmers rated Cruza below average, ranked Ndamira first, and linked marketability most to yield. In this group Ndamira did not differ significantly from Gisubizo, Izihirwe, Kazeneza, Kirundo, Seka and Twihaze. Supplementary trees linked tuber appearance rankings to gender and yield to input use.

The authors suggest that the old varieties may stay popular because of broad adaptability, stable yields and disease tolerance under the low-input conditions common among smallholders. They note that the trial covered only two seasons, that farmers may not judge disease accurately, and that on-station and on-farm data were hard to align. They conclude that combining these data sources can give breeding programmes targeted insights by environment and farm type.

## Methods in brief

- **tricot.** 460 farmers, 11 varieties, three per farmer, seasons 2021A (September 2020 to February 2021) and 2021B (March to July 2021).
- **Plot and traits.** Each variety in a subplot of 40 tubers in four rows of three metres, under the farmer's own practices. Farmers ranked 17 traits at five stages, from 45 days after planting to 60 days after harvest (1380 plots in total).
- **Data cleaning.** Five records without GPS and 23 with major inconsistencies were removed.
- **Socio-economic data.** RHoMIS survey of 283 participants.
- **Station data.** National performance and multi-location trials (randomized complete blocks, three replicates). Seasons 2018B and 2019A were run, but only 2018B was used because not all varieties were grown in 2019A. Nine of the eleven varieties were included. Genotypic values came from mixed models (lme4 BLUPs, cumulative link mixed models for ordinal traits, glmmTMB for disease traits) and were standardized. Cruza and Gisubizo received the average of the other nine.
- **Analysis.** Plackett-Luce model for overall rankings, with Kirundo as reference. Kendall τ between the 17 traits and three final evaluations. Plackett-Luce trees with environmental covariates (chirps, climatrends, SoilGrids) and, separately, RHoMIS covariates (α = 0.1, or 0.07 for bacterial wilt, minimum group size 25). PLADMM with standardized on-station genotypic values as item covariates, chosen by forward selection on AIC.

## Stated limitations

- Aligning on-station genotypic values with on-farm rankings was difficult.
- Only 283 of 460 participants had RHoMIS data, because of financial and time constraints, so socio-economic and environmental covariates were analysed separately (p. 6, 9).
- The trial ran for only two seasons, without follow-up trials, which may have influenced the results (p. 19).
- Farmers may not observe disease accurately, which may explain why on-station and on-farm bacterial wilt did not correlate. Multi-season data, image analysis or farm visits are suggested (p. 20).
- PLADMM could not identify the biological causes of the temperature effect on yield ranks (p. 19, 21).
- No in-depth interviews with high-income farmers to explain their choices (p. 19).
- The results do not show whether varietal differences explain the higher yields of market-oriented farmers. Trials of old and new varieties under low-input, stress-prone conditions are needed (p. 20).

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 460 farmers | tricot participants in Gicumbi and Nyamagabe | This paper |
| 11 varieties | Potato varieties tested, three per farmer | This paper |
| 283 farmers | Participants surveyed with RHoMIS | This paper |
| Season 2018B | On-station trials used for genotypic values (2019A data dropped), nine of 11 varieties, Cruza and Gisubizo imputed | This paper |
| 25 | Minimum group size in Plackett-Luce trees | This paper |
| 280 vs 113 | Farmers in warmer vs cooler nodes of the yield tree | This paper |
| 23.75 °C | 90th percentile of day temperature splitting the yield tree | This paper |
| Ndeze, Nkunganire | Ranked 10th and 11th on all three final evaluations (Table 3) | This paper |
| τ 0.454 / 0.414 / 0.398 | Kendall τ of marketability after storage (PH2) with overall performance, willingness to plant, overall preference | This paper |
| τ 0.376 / 0.345 / 0.271 | Same for yield (PH1) | This paper |
| p = 0.005, 0.002, 0.007 | PLADMM: on-station tuber weight (cool, negative), virus severity (warm, positive), tuber number (warm, positive) vs farmer yield ranks | This paper |
| 24.95 and 259.48 USD | Annual crop-income splits in the marketability tree (n = 60, 50, 109) | This paper |

## Notes

- de Sousa et al. 2024 (desousa-2024-asd) describes a Rwanda potato tricot with 11 varieties across seven districts (135 trials in the first season) and a cost case study with 155 tricot trials. This paper reports two districts (Gicumbi and Nyamagabe) and 460 farmers. Check whether it is the same trial network.
- Source issue: the text on p. 9 lists Cyerekezo among the nine varieties grown both on-station and on-farm. Table 1 shows Kirundo, not Cyerekezo, in these trials. Cyerekezo is likely an error for Kirundo.
- Source issue: for high-income farmers (node 5), Figure 5 and pp. 17 to 18 put Ndamira first. The six varieties listed on p. 19 are those that did not differ from Ndamira. The p. 19 list leaves Ndamira out.
- Source issue: the claim that Gisubizo and Kazeneza ranked third and fourth (p. 18) fits overall performance only (Table 3). For overall preference, Ndamira is third and Gisubizo sixth. In Table 3, Kazeneza is significantly below Kirundo for overall performance (p = 0.038). The discussion cites supplementary Table S4, which was not checked.
- Source issue: the text on p. 15 about the cool node is garbled. Figure 4A shows Twihaze first (letter a), Seka (ab) and Kazeneza (abc) sharing its letter group, and Ndamira lowest (d).
- Source issue: the discussion (p. 18) names Nyabihu and Nyamagabe for the cool-node result, but the on-farm trial districts are Gicumbi and Nyamagabe (p. 5).
- Source issue: p. 15 mentions only one season of data for yield, while the tricot trial ran two seasons. This probably refers to the single on-station season (2018B).
- Source issue: the paper does not explain the sample sizes per analysis: 432 records after cleaning, 393 in the yield tree, 309 or 228 in the trait correlations, and 219 in the crop-income tree (sums computed for this card).
- Source issue: in Table 3, use the Ranking column, not the row order. The note says rows are sorted by estimate, but they are not.
