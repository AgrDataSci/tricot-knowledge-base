---
id: voss-2025-ppp
title: Citizen science informs demand-driven breeding of opportunity crops
authors: Voss RC, de Sousa K, N'Danikou S, Shango A, Aglinglo LA, Laporte MA, Legba EC, Houdegbe AC, Diarra DY, Dolo A, Sidibe A, Ouedraogo CO, Coulibaly H, Achigan-Dako EG, Kileo A, Malulu D, Matumbo Z, Dinssa F, van Heerwaarden J, van Etten J, Riar A, van Zonneveld M
year: 2025
journal: Plants, People, Planet
journal_short: Plants People Planet
article: published 2025, e70035
type: research article
source: team
peer_reviewed: yes
curated_card: yes
doi: https://doi.org/10.1002/ppp3.70035
open_copy: https://doi.org/10.1002/ppp3.70035
license: CC BY
data: survey template, data and code on Zenodo, https://doi.org/10.5281/zenodo.15204183
software: PlackettLuce, gosset, ClimMobTools, cluster (R packages)
crops: leafy amaranth
region: Benin, Mali, Tanzania
keywords: opportunity crops, NUS, amaranth, tricot, farmer segmentation, cluster analysis, gender, market segments, demand-driven breeding, seed systems, World Vegetable Center, regret analysis
gist: tricot trials of 14 amaranth varieties with 2,063 farmers in Benin, Mali and Tanzania find four farmer segments with distinct preferences, yet A2004 is acceptable to all on marketability
not_established: that the segments come from the tricot rankings (they come from a cluster analysis of survey data, done independently of the rankings); that the segments or variety rankings hold in other countries or opportunity crops without new trials; that segments differ in overall performance or fourth-harvest rankings (not significant); that A2004 is best for every trait (it was assessed on marketability worth and regret only); that women and men differ in a simple gender split (the paper uses intersectional segments and contrasts with a study that found no gender difference)
---

## Questions this paper answers

- Can tricot support breeding of neglected and underutilized (opportunity) crops?
- What drives farmer preference for leafy amaranth varieties?
- How can farmers be segmented by gender and business orientation?
- How can segments guide breeders and seed enterprises?
- Which amaranth variety is acceptable to all farmer segments?

## Summary

Opportunity crops, also called neglected and underutilized species, can diversify food systems with nutritious, climate-resilient foods, but few improved varieties exist and farmers struggle to access quality planting material. The study tests whether citizen science can support demand-driven breeding and seed production of these crops, using leafy amaranth as a case.

The World Vegetable Center and partners ran tricot trials of 14 amaranth varieties with 2,063 farmers in Benin, Mali and Tanzania (794 in Benin, 969 in Mali and 300 in Tanzania), including trials in the Mtwara and Lindi regions of Tanzania in 2022. Women made up the majority of participants overall. Farmers ranked their three varieties for overall performance and traits, and the team collected household and farm characteristics, including household structure.

Overall preference was driven mainly by plant survival, yield, leaf size, taste and marketability. Cluster analysis of farmer characteristics identified four segments, older women generalists, young women specialists, older men generalists and young men specialists, which differed by gender, age and business orientation. These segments preferred different varieties, which the authors read as a sign of how varied the producers of neglected crops are.

The authors argue that the segments and their preferences give breeders and seed enterprises actionable information on market segments, and support demand-driven amaranth breeding and seed system development. They present the methods and lessons as applicable to other opportunity crops in Africa and elsewhere.

The study places amaranth within the renewed attention to neglected crops amid food insecurity, poor nutrition and climate change. African traditional leafy vegetables are increasingly demanded, can raise smallholder incomes and improve diets, but seed systems for them are weak and improved varieties scarce, so breeding needs clear information on what different users want. The wide variation in preferences across countries and farmer groups points to context-specific breeding strategies rather than a single target. The authors suggest that improved amaranth varieties that meet local needs could expand economic opportunities, especially for women. In this study, men mainly controlled amaranth production and sales in Benin and Tanzania, and women did so in Mali. The authors present the study as a model for participatory research on other opportunity crops, linking on-farm evidence directly to breeding and seed-enterprise decisions.

Across all farmers, preferences leaned toward Akeri, Poli and AM-NKGN, linked to marketability, leaf size, yield and taste at the fourth harvest. A likelihood-ratio test showed that the four segments ranked varieties differently for plant survival, yield and marketability up to the third harvest, but not for fourth-harvest traits or overall performance, when fewer observations were recorded. In a worth and regret analysis of marketability, A2004 was acceptable to all four segments. As a second variety, AC-NL had high overall worth but mainly suited older men generalists, while Poli gave the lowest regret and was preferred by the other three segments. The authors note that the gender balance of participants differed by country, that men may have overstated their role in amaranth, and that older men generalists gave inconsistent rankings.

## Methods in brief

- **Trials.** tricot with a balanced incomplete block design: each farmer got three of 14 amaranth varieties (2 g seed each, coded A, B, C), from the WorldVeg genebank and breeding lines. Benin and Mali 2021 to 2022, Tanzania 2022. Data collected in ODK linked to ClimMob.
- **Evaluation.** Farmers ranked overall performance and traits (germination, vigor, plant survival, pest and disease tolerance, drought and flood tolerance, plant height, branching, yield, leaf size, marketability, taste) across four harvest periods. A baseline survey recorded household, land, market and institutional data.
- **Participants.** 2,063 farmers (794 Benin, 969 Mali, 300 Tanzania), 56.2% women.
- **Analysis.** Plackett-Luce models (PlackettLuce, ClimMobTools and gosset). Kendall tau with backward selection to keep the traits linked to overall preference. Principal component analysis of trait log-worths.
- **Segmentation.** Hierarchical cluster analysis (R package cluster) on seven survey variables, done independently of the rankings: gender, age, years growing amaranth, distance to market, gender controlling production, gender controlling sales, and income share from amaranth. ChatGPT helped draft segment descriptions, which the authors reviewed.
- **Validation and decision support.** Likelihood-ratio test (gosset) of whether segments rank varieties differently, and worth and minimum-regret analysis of marketability.

## Stated limitations

- Differences in who controls amaranth production and sales are likely, at least in part, a result of the different gender balance of participants in each country (p. 6).
- Women and men both tended to report themselves, not their partner, as controlling amaranth, and men may have overstated their role (pp. 6, 10).
- Older men generalists gave inconsistent rankings, which may reflect disagreement or uncertainty within the segment (p. 10).
- Fewer observations were recorded at the fourth harvest, and segment differences for fourth-harvest traits and overall performance were not significant (p. 8).
- Plot size and plant spacing were recommended but not enforced, and farmers used their own management (p. 4).
- Better varieties for producers must be paired with attention to consumer demand, policy, post-harvest handling and value chains (p. 11).

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 14 varieties | Leafy amaranth varieties tested | This paper |
| 2,063 farmers | Participants across Benin, Mali and Tanzania | This paper |
| 794 / 969 / 300 | Participants in Benin / Mali / Tanzania | This paper |
| 904 men, 1,159 women | Participants by gender | This paper |
| 56.2% women | Share of participants, 33.1% in Benin, 83.1% in Mali, 30.3% in Tanzania | This paper |
| 4 segments | Farmer segments by gender, age and business orientation | This paper |
| 34 to 45 years | Average age of segments (young men 34, young women 35, older women 43, older men 45) | This paper |
| 6 of 11 traits | Traits on which segments ranked varieties significantly differently (p < 0.05), all up to the third harvest | This paper |
| 0.2317 worth, 0.0011 regret | A2004 marketability, best on both measures, acceptable to all segments | This paper |

## Notes

- Country and gender splits are verified against the text (p. 3) and Table 2 (p. 5). They add up to 2,063.
- Segment preferences (Fig. 4, p. 8): older women generalists preferred Akeri, Poli and AVAM1941. Young women specialists preferred A2004, Akeri, AVAM1939, AM-NKGN and Poli. Young men specialists preferred A2002 and A2004 for marketability. Older men generalists showed little agreement.
- Unlike a gender-disaggregated variety selection study of amaranth in Tanzania (Dinssa et al. 2022), which found similar preferences for women and men, this segment analysis found that preferences vary among women and among men (p. 10).
- Taste was a key driver of preference, but the authors note it is rarely a priority trait in breeding programs (p. 9).
- Funding included the BOLDER project (Crop Trust) and 1000FARMS (Gates Foundation) (p. 11).
- Outside the source: the dataset may also appear in tricot-data. Check before linking.
- Source issue: Table 2 gives an overall average household size of 11, but the country values (16.7, 18.4, 3.9) give a weighted mean of about 15.6 (our calculation).
- Source issue: the text says 10 traits were assessed (p. 5), but the trait list on p. 4 names 12 or more.
- Source issue: the methods call the test Kendall tau correlation (p. 5), but the results call it Kendall partial correlation (p. 7).
