---
id: gotor-2021-fsufs
title: Smallholder farmer engagement in citizen science for varietal diversification enhances adaptive capacity and productivity in Bihar, India
authors: Gotor E, Pagnani T, Paliwal A, Scafetti F, van Etten J, Caracciolo F
year: 2021
journal: Frontiers in Sustainable Food Systems
journal_short: Front Sustain Food Syst
article: 5, 726725
type: research article
source: team
peer_reviewed: yes
curated_card: yes
doi: https://doi.org/10.3389/fsufs.2021.726725
open_copy: https://doi.org/10.3389/fsufs.2021.726725
license: CC BY
data: Seeds for Needs India impact assessment survey, Harvard Dataverse, https://doi.org/10.7910/DVN/DW2W9J (Gotor et al. 2018, footnote 6 says data and questionnaire are available on request at this DOI), code not shared
crops: rice, wheat
region: India (Bihar; Saran, Samastipur and Vaishali districts)
keywords: impact assessment, varietal diversification, Seeds for Needs, citizen science, livelihoods, resilience, RHoMIS, doubly robust estimator, Simpson diversity, Bihar, adaptive capacity
gist: Survey of 600 households in Bihar finds that the Seeds for Needs crowdsourced intervention increased rice and wheat varietal diversity, perceived yields and recovery from shocks
not_established: measured yield gains (yield change is self-reported on a −4 to +4 scale, and the percent effects are not yield percentages); randomized causal effects (quasi-experimental, no baseline); effects of crowdsourced trials alone (the intervention also ran Farmer Field School training); benefits for every household (the recovery effect was negative for households with high prior recovery capacity); effects beyond rice and wheat in Bihar
relations:
  - extends: vanetten-2019-pnas  # household impact of the Bihar Seeds for Needs intervention
---

## Questions this paper answers

- Does a crowdsourced variety evaluation programme increase varietal diversity on farms?
- Does varietal diversity translate into livelihood benefits for households?
- How large were the effects of Seeds for Needs in Bihar?
- How can impact be estimated when participants were not randomly assigned?

## Summary

Growing two or more varieties of a crop can lower disease, raise productivity and reduce yield variability, but earlier evidence came from experiments or observation of existing systems, not from interventions that introduce new varieties. This study evaluates whether such an intervention works in practice, using Seeds for Needs in Bihar, India (2010 to 2017), which the authors describe as the largest citizen science intervention to date, with 25,000 farmers and 47,000 plot-seasons (figures for the whole initiative in India, not only Bihar). Besides on-farm variety trials, the intervention ran Farmer Field School trainings.

The analysis follows the sustainable rural livelihoods framework. The intervention is expected to build human capital (knowledge and skills), natural and physical capital (new seed) and social capital (connections among farmers), leading farmers to adopt promoted varieties, diversify their rice and wheat, and gain in productivity and in their ability to recover from shocks. In 2018, three enumerators surveyed 600 households in 21 villages of three districts using a questionnaire adapted from RHoMIS and collected on tablets with ODK. The questionnaire covered the wheat and rice varieties sown over five years, seed sources, preferred traits, harvests, sales and climate-related losses, alongside household assets and shocks. Half the households were participants drawn from project records. The other half were non-participants, 150 from the same villages and 150 from nine similar villages never reached by the programme.

Because participation was voluntary and no baseline existed, the authors used a doubly robust estimator, combining a model of who participated with a model of the outcome, and then a system of simultaneous equations estimated by generalized method of moments with inverse probability weights to test each link of the causal chain. Diversity was measured with the Simpson index, productivity as self-reported yield change over five years, and recovery capacity as a self-assessed index across four kinds of shock.

Participation increased varietal diversity, by 0.03 on the Simpson index for rice (5%) and 0.06 for wheat (11%). Perceived yield change rose by 0.185 points for rice (p = 0.053) and 0.245 for wheat, which the authors report as 3.94% and 4.80% gains, and recovery capacity rose by 0.40 points, about 7%. The equation system supported the chain. Adopting promoted varieties raised diversity, though participation alone had no significant direct effect. Diversity raised perceived yields of both crops, and higher perceived wheat yields improved recovery capacity, though rice yields did not. The gain in recovery capacity was largest for households with intermediate prior levels, and the most vulnerable also benefited, but the effect was negative for households with high prior levels. The authors note that the estimates are conservative because spillovers to non-participants were ignored.

They conclude that participatory programmes built on local varietal diversity strengthen rural livelihoods, and that the results offer policymakers evidence on the size of these effects.

## Methods in brief

- **Sample.** 600 households (300 participants, 300 non-participants) in 12 project villages and 9 comparison villages, three districts of Bihar, surveyed February to August 2018.
- **Survey.** 17-section questionnaire including RHoMIS modules, collected with ODK.
- **Outcomes.** Simpson diversity index, self-reported yield change (−4 to +4), recovery capacity index (−4 to +4).
- **Analysis.** Doubly robust estimator, then five simultaneous equations by GMM with inverse probability weighting.
- **Group differences.** Exposed households cultivated less land (1.29 vs 1.71 acres) and reported more trust, debt and formal credit (Table 2).

## Stated limitations

- No baseline or randomized control, because the programme expanded in response to local demand.
- Floods affected village selection in Saran and Samastipur, skewing the sample toward Vaishali.
- Spillovers to non-participants were ignored, so estimates are conservative.
- Only one pathway of the sustainable livelihoods framework was analysed (institutional change acting through livelihood strategies), and only linear relationships were tested.
- Other livelihood outcomes could have been included.
- The distribution of effects across households is not well understood, and the authors have no plausible explanation for the different patterns in rice and wheat.
- The citizen science trial data were not linked directly to the econometric analysis, for example to test whether some varieties reduce vulnerability more than others.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 25,000 farmers, 47,000 plot-seasons | Scale of Seeds for Needs in India as a whole (600 villages, 49 districts, 7 states), not only Bihar. Page 4 gives about 46,000 trials | This paper (abstract). Page 4 cites Bioversity International 2017 and van Etten et al. 2019 |
| 6,500 households | Participants in project records across the three districts | This paper |
| 600 households | Survey sample (300 exposed, 300 non-exposed) | This paper |
| 1.65 / 1.91 vs 0.20 / 0.31 | Mean number of initiative rice / wheat varieties adopted, exposed vs non-exposed households (Table 2) | This paper |
| +0.031 (5.15%) / +0.061 (10.87%) | Effect on Simpson diversity, rice / wheat (p = 0.042 / p < 0.001) | This paper |
| +0.185 (3.94%) / +0.245 (4.80%) | Effect on perceived yield change, rice / wheat (p = 0.053 / p = 0.016) | This paper |
| +0.401 (7.46%) | Effect on recovery capacity (p = 0.001) | This paper |

## Notes

- Percent effects are the DR estimate divided by a benchmark (Table 3). For the Simpson index the benchmark is the non-exposed mean. For perceived yield change and recovery capacity it is the non-exposed mean plus 4, which shifts the −4 to +4 scale above zero. So 3.94% and 4.80% are not yield percentages. On the perceived yield scale one point means about a 25% change in yield (page 7).
- The intervention is the crowdsourced evaluation approach of vanetten-2019-pnas (the India bread wheat case). Use this card for impact on households, and that card for variety performance.
- Occelli et al. 2024 (occelli-2024-agecon) is the randomized impact study of tricot. This one is quasi-experimental.
- Productivity and recovery capacity are self-reported (page 7). The authors describe these measures but do not discuss this as a limitation.
- Source issue: the source is inconsistent on who gained most in recovery capacity. The Results (page 12) stress the lower percentiles, the Discussion (page 13) says intermediate prior levels gained most and high prior levels lost. Figure 5 agrees with the Discussion.
- Source issue: for rice, the Results (page 12) and Figure 5 show the diversity effect rising with prior diversity and an inverse U for perceived yield, but the Discussion (page 13) says rice gains went to households with lower prior levels.
- Source issue: the text (page 9) calls the 7% recovery gain a share of the actual mean, but Table 3 divides by the non-exposed mean plus 4. Against the plain non-exposed mean (1.377) the gain would be about 29% (card's own calculation).
- Source issue: the source gives 47,000 plot-seasons (abstract) and about 46,000 trials (page 4) for the India programme, and its count of states is not consistent (7 on page 4, nine more in footnote 1, which lists eight names and counts Odisha and Orissa separately).
- Source issue: the non-exposed and exposed values in Table 3 differ from the raw means in Table 2 and are probably adjusted by the DR model, which the paper does not say. In the raw data, recovery capacity did not differ between groups (Table 2).
- Source issue: the Data Availability Statement (page 14) says the data are in an online repository, but footnote 6 (page 6) says they are available on request.
