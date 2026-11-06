---
id: brown-2023-agronj
title: Rank-based data synthesis of heterogeneous trials to identify the effects of climatic factors on the reaction of Musa genotypes to black leaf streak disease
authors: Brown D, de Bruin S, de Sousa K, Abadie C, Carpentier S, Machida L, van Etten J
year: 2023
journal: Agronomy Journal
journal_short: Agron J
article: 115(6), 2990-3009
type: research article
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1002/agj2.21436
open_copy: https://doi.org/10.1002/agj2.21436
license: CC BY
data: code and data at https://github.com/AgrDataSci/Data_Synthesis_Musa_Trials_BLSD; curated workflow in https://github.com/AgrDataSci/tricot-analysis-workflows (use-cases/can-heterogeneous-trials-be-combined)
software: PlackettLuce, gosset, climatrends, ag5Tools, stablelearner, qvcalc, partykit
crops: banana, plantain (Musa)
region: 22 locations in Africa, Asia, Latin America, the Caribbean and the Pacific (Bangladesh, Cameroon, Colombia, Costa Rica, Ecuador, Honduras, Nicaragua, Nigeria, Philippines, Puerto Rico, Tanzania, Tonga, Uganda, Vietnam)
keywords: data synthesis, rank aggregation, heterogeneous trials, Plackett-Luce trees, black leaf streak disease, black Sigatoka, Musa, AgERA5, dry spell, relative humidity, reliability, stability assessment, genotype by environment
gist: Pools 31 Musa trials from 1990 to 2019 that scored black leaf streak with five different metrics by converting them to rankings, and finds that dry spell length separates humid from dry environments with different resistant genotypes
not_established: that dry environments are disease-free; that the top genotypes in dry environments differ significantly from the reference Calcutta 4; a causal mechanism for the humidity effect; that genotypes outperforming Calcutta 4 in one environment do so in the other
relations:
  - extends: brown-2022-cropsci  # applies rank-based data synthesis to non-ranking station data and disease scores instead of tricot rankings
  - usesMethodIn: desousa-2023-softwarex  # gosset for rank_numeric, reliability and model summaries
  - usesMethodIn: desousa-2023-joss  # climatrends indices over the evaluation period
---

## Questions this paper answers

- Can trial data that scored a trait in different ways, in different years and places, be analysed together?
- How are numeric measurements such as disease indices or days to symptoms turned into rankings, and in which direction?
- Which climatic factor changes how Musa genotypes react to black leaf streak disease?
- How can a Plackett-Luce tree be checked for stability when the data set is small?
- What is reliability, and how does it help choose genotypes for further testing?
- Which Musa genotypes resist black leaf streak in humid and in dry environments?

## Summary

David Brown and colleagues, in work with Kauê de Sousa and Jacob van Etten, ask whether the scattered field evaluations of Musa genotypes against black leaf streak disease (BLSD, caused by Pseudocercospora fijiensis) can be brought into one analysis. BLSD is the most destructive leaf disease of banana and its control depends on fungicides, so resistant varieties matter, but multi-environment trials of Musa are rare because the crop needs large plots and long cycles. The paper extends the rank-based data synthesis of Brown et al. (2022), developed for tricot rankings, to data that were never collected as rankings.

The authors retrieved trial data from AgTrials, MusaBase and MGIS, and kept trials with a BLSD evaluation, coordinates, planting and shooting or harvest dates, and genotypes that overlap with other trials. This gave 31 trials at 22 locations from 1990 to 2019, with 62 genotypes of three kinds, a crop wild relative (Calcutta 4), landraces and improved genotypes. The trials scored BLSD with five metrics, youngest leaf spotted, disease development time, disease infection index, number of standing leaves and number of functional leaves. Each metric was converted to a ranking with gosset, in the direction that means resistance, so genotypes with the highest youngest leaf spotted rank first and genotypes with the lowest disease index rank first. Where block data existed, each block gave a ranking. Where only means were reported, the trial gave one. Each cycle gave its own ranking, and a ratoon cycle started at the end of the previous cycle. This produced 110 rankings.

Climate for the evaluation period of each ranking came from AgERA5, with rainfall and temperature indices from climatrends and relative humidity at five times of day. A Plackett-Luce tree with climate covariates, fitted in explanatory mode with large nodes and a Bonferroni-corrected alpha, split the data on the maximum length of dry spell at 13 days. The humid node held 41 rankings and the dry node 69. Humid environments favour the disease, and there NARITA 8, FHIA-01 and NARITA 2 ranked highest, with reliability above 0.7 of outperforming Calcutta 4. In dry environments only the landrace Saba surpassed 50% reliability and no genotype differed significantly from the reference. Some genotypes, such as NARITA 8 and NARITA 24, reacted in opposite ways in the two environments, which the authors read as resistance components expressed under different conditions. Refitting the tree on 1000 subsamples selected the dry spell variable in 855 of them, so the tree is stable.

The paper matters for two reasons. It shows that decades of incompatible trial data can be reused when expert knowledge of the trait guides the choice of metrics, and that reliability and ranking probabilities together give breeders a basis to choose genotypes for testing at new locations. The authors also call for trial data to be shared in public repositories so that such syntheses can be extended.

## Methods in brief

- **Data.** 31 trials, 22 locations, 1990 to 2019, 62 genotypes, from AgTrials (IMTP 1 to 3), MGIS (a thesis and Irish et al.) and MusaBase (WP4-BBB project).
- **Inclusion.** BLSD evaluation, coordinates, planting and end dates, genotype overlap.
- **Rankings.** gosset::rank_numeric per block or trial mean, per cycle, with the metric direction set per trial. 110 rankings.
- **Network.** Weakly connected genotypes removed. Genotypes kept when present in at least 5% of the trials, a threshold found by iterating to the least data loss that still allowed convergence, which discarded 37% of the genotypes. Pseudo-rankings (npseudo = 2) keep the network connected after splits.
- **Ties.** One genotype kept at random from each tied set, the rest dropped from that ranking. Which one was kept did not change the results.
- **Climate.** AgERA5 daytime maximum and nighttime minimum temperature, precipitation and relative humidity over each evaluation period, with climatrends indices. Variables with near-zero variance removed.
- **Model.** Plackett-Luce tree, alpha 0.05 with Bonferroni correction, minimum node size 35% of the data.
- **Stability.** stablelearner, 1000 subsamples of 80% without replacement.
- **Reliability.** Probability of outperforming the reference Calcutta 4, with quasi-standard errors.

## Stated limitations

- Converting metric data to rankings loses information. Expert knowledge of the trait reduces the loss.
- The aggregated data set is small because few Musa evaluations are in public repositories.
- Dry environments are not disease-free, and the data cannot discriminate the mechanism behind the humidity effect.
- Leaf-based metrics depend on plant growth, which drought slows, so some bias in dry environments is possible.
- Failure to outperform Calcutta 4, which has qualitative resistance, is not poor performance.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 31 trials | Heterogeneous trials pooled | This paper |
| 22 locations | Unique trial locations in 14 countries | This paper |
| 1990–2019 | Temporal range of the trials | This paper |
| 62 genotypes | Genotypes in the final data set | This paper |
| 110 rankings | Rankings after converting every evaluation | This paper |
| 5 metrics | YLS, DDT, DII, NSL, NFL used in the original trials | This paper |
| 33, 3, 41, 24, 9 | Rankings derived from YLS, DDT, DII, NSL, NFL | This paper |
| 13 days | Maximum length of dry spell at the split, humid at or below, dry above | This paper |
| 41 and 69 | Rankings in the humid and dry nodes | This paper |
| −0.75 | Correlation between dry spell length and relative humidity at 09:00 | This paper |
| 855 of 1000 | Subsample refits selecting the dry spell variable | This paper |
| 0.817, 0.767, 0.722 | Reliability of NARITA 8, FHIA-01 and NARITA 2 in humid environments | This paper |
| 0.509 | Reliability of Saba in dry environments, the only one above 0.5 | This paper |
| 5% and 35% | Minimum presence of a genotype across trials and minimum node size | This paper |
| 37% | Genotypes discarded by the presence threshold | This paper |

## Notes

- Successor to brown-2022-cropsci, which pooled tricot rankings. This paper is the first application to non-ranking data (disease scores) and the first to Musa.
- The abstract says 110 evaluations and 31 trials, Table 1 lists the eight studies that provided them.
- The curated workflow derived from this paper is in tricot-analysis-workflows, use case can-heterogeneous-trials-be-combined, with the original scripts in its archive.
- David Brown is not in people.md. Credit him as first author from the card.
