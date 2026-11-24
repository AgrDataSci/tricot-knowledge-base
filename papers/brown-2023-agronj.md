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
curated_card: yes
doi: https://doi.org/10.1002/agj2.21436
open_copy: https://doi.org/10.1002/agj2.21436
license: CC BY
data: code and data at https://github.com/AgrDataSci/Data_Synthesis_Musa_Trials_BLSD; curated workflow in https://github.com/AgrDataSci/tricot-analysis-workflows (use-cases/can-heterogeneous-trials-be-combined)
software: PlackettLuce, gosset, climatrends, ag5Tools, stablelearner, qvcalc, partykit
crops: banana, plantain (Musa)
region: 22 locations in Africa, Asia, Latin America, the Caribbean and the Pacific (Bangladesh, Cameroon, Colombia, Costa Rica, Ecuador, Honduras, Nicaragua, Nigeria, Philippines, Puerto Rico, Tanzania, Tonga, Uganda, Vietnam)
keywords: data synthesis, heterogeneous trials, Plackett-Luce trees, black leaf streak disease, black Sigatoka, Musa, AgERA5, dry spell, relative humidity, reliability, stability assessment, genotype by environment
gist: Turning five black leaf streak metrics from 31 Musa trials into rankings allows joint analysis, and dry spell length separates humid and dry environments where genotypes rank differently
not_established: that dry environments are disease-free; that the top genotypes in dry environments differ significantly from the reference Calcutta 4; that NARITA 8 outperforms Calcutta 4 with statistical significance (Table 6 gives p = 0.065); a causal mechanism for the humidity effect, or whether it acts on the host or the pathogen; that genotypes outperforming Calcutta 4 in one environment do so in the other; that the tree predicts genotype reactions at new sites, since it was fitted to explain and not validated for prediction; that drought predisposes Musa to BLSD, which the authors raise only as a hypothesis
relations:
  - extends: brown-2022-cropsci  # applies rank-based data synthesis to non-ranking station data and disease scores instead of tricot rankings
  - usesMethodIn: desousa-2023-softwarex  # gosset for rank_numeric, reliability and model summaries
  - usesMethodIn: desousa-2023-joss  # climatrends indices over the evaluation period
  - usesMethodIn: eskridge-1992-tag  # reliability, the probability of outperforming the reference genotype
---

## Questions this paper answers

- Can trial data that scored a trait in different ways, in different years and places, be analysed together?
- How are numeric measurements such as disease indices or days to symptoms turned into rankings, and in which direction?
- Which climatic factor changes how Musa genotypes react to black leaf streak disease?
- How can a Plackett-Luce tree be checked for stability when the data set is small?
- What is reliability, and how does it help choose genotypes for further testing?
- Which Musa genotypes resist black leaf streak in humid and in dry environments?

## Summary

David Brown and colleagues ask whether the scattered field evaluations of Musa genotypes against black leaf streak disease (BLSD, caused by Pseudocercospora fijiensis) can be brought into one analysis. BLSD is the most destructive leaf disease of banana and its control depends on fungicides, so resistant varieties matter, but multi-environment trials of Musa are hard to run because the crop needs much space and time. The paper applies the data synthesis approach of Brown et al. (2020), which Brown et al. (2022) used for tricot rankings of common bean, to data that were not collected as rankings.

The authors retrieved trial data from AgTrials, MusaBase and MGIS, and kept trials with a BLSD evaluation, coordinates, planting and shooting or harvest dates, and genotypes that overlap with other trials. This gave 31 trials at 22 locations from 1990 to 2019, with 62 genotypes of three kinds, a crop wild relative (Calcutta 4), landraces and improved genotypes. The trials scored BLSD with five metrics, youngest leaf spotted, disease development time, disease infection index, number of standing leaves and number of functional leaves. Each metric was converted to a ranking with gosset, in the direction that means resistance (highest youngest leaf spotted first, lowest disease index first). Where block data existed, each block gave a ranking. Where only means were reported, the trial gave one. Each cycle gave its own ranking, and a ratoon cycle started at the end of the previous cycle. This produced 110 rankings.

Climate for the evaluation period of each ranking came from AgERA5, with rainfall and temperature indices from climatrends and relative humidity at five times of day. A Plackett-Luce tree with climate covariates, fitted in explanatory mode with large nodes and a Bonferroni-corrected alpha, split the data on the maximum length of dry spell at 13 days. This index was barely correlated with rainfall totals but strongly and negatively with relative humidity at 09:00 (r = −0.75), so the authors read the two nodes as humid (41 rankings) and dry (69 rankings) environments. In humid environments, assumed to favour the disease, NARITA 8, FHIA-01 and NARITA 2 ranked highest, with reliability above 0.7 of outperforming Calcutta 4. In dry environments only the landrace Saba surpassed 50% reliability, and none of the top 10 differed significantly from the reference. FHIA-01 did well in both. Some genotypes, such as NARITA 8 and NARITA 24, reacted in opposite ways in the two environments, which the authors read as resistance components expressed under different conditions. Refitting the tree on 1000 subsamples selected the dry spell variable in 855 of them, so the tree is stable.

The paper shows that trial data once seen as incompatible can be analysed together, with expert knowledge of the trait limiting the information lost in ranking, and that reliability and ranking probabilities together give breeders a basis to choose genotypes for testing at new locations. The authors also call for trial data to be shared in public repositories so that such syntheses can be extended.

## Methods in brief

- **Data.** 31 trials, 22 locations, 1990 to 2019, 62 genotypes, from seven studies (Table 1): AgTrials (IMTP 1 to 3 and the thesis of Orlando Narváez 2004), MGIS (Irish et al. 2013 and 2019) and MusaBase (WP4-BBB project).
- **Inclusion.** BLSD evaluation, coordinates, planting and end dates, genotype overlap.
- **Rankings.** gosset::rank_numeric per block or trial mean, per cycle, with the metric direction set per trial. Where a trial reported several metrics, the one with most data and giving the most homogeneous data set was used. 110 rankings.
- **Network.** Weakly connected genotypes removed. Genotypes kept when present in at least 5% of the trials, a threshold found by iterating to the least data loss that still allowed convergence, which discarded 37% of the genotypes. Pseudo-rankings (npseudo = 2) keep the network connected after splits. Williams, Gros Michel and Pisang Ceylan act as common references that link genotypes never tested together. FHIAs and NARITAs were never compared directly in any trial (p. 2997, Figure 2).
- **Ties.** One genotype kept at random from each tied set, the rest dropped from that ranking. Which one was kept did not change the results.
- **Climate.** AgERA5 daytime maximum and nighttime minimum temperature, precipitation and relative humidity over each evaluation period, with climatrends indices. Variables with near-zero variance removed.
- **Model.** Plackett-Luce tree, alpha 0.05 with Bonferroni correction, minimum node size 35% of the data.
- **Stability.** stablelearner, 1000 subsamples of 80% without replacement.
- **Reliability.** Probability of outperforming the reference Calcutta 4 (Eskridge and Mumm 1992), with its standard error. Worth estimates carry quasi-standard errors. Reliability estimates are conservative because pseudo-rankings shrink the worth estimates.

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
| 22 locations | Unique trial locations, in 14 countries or territories by the card's count of Table 2 | This paper (country count is the card's own) |
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

- Successor to brown-2022-cropsci, which pooled tricot rankings. The authors call this the first application of the approach to black leaf streak data first collected in a non-ranking format (p. 2991), and the first to combine heterogeneous Musa trial data with climate covariates (p. 3006).
- The Conclusions (p. 3006) give 110 evaluations in 31 trials. The abstract does not give these numbers. Table 1 (p. 2994) lists the seven studies that provided them: IMTP-1 to IMTP-3 and Orlando Narváez (2004) from AgTrials, Irish et al. (2013, 2019) from MGIS, and the WP4-BBB project from MusaBase. Its rankings per study (4, 13, 26, 3, 2, 2, 60) add up to 110 and its locations per study (6, 8, 7, 3, 1, 1, 5) add up to 31, so each trial is one study location (card's calculation).
- Outside the source: the curated workflow derived from this paper is in tricot-analysis-workflows, use case can-heterogeneous-trials-be-combined, with the original scripts in its archive.
- David Brown is not in people.md. Credit him as first author from the card.
- Source check: the Results (p. 3000) say NARITA 8 outperforms Calcutta 4 with statistical significance in humid environments, but Table 6 (p. 3001) gives p = 0.065, above 0.05. Treat NARITA 8 as the best but not a significant winner.
- Source check: the Discussion (p. 3006) lists NARITA 20 among humid-environment genotypes above 50% reliability, but it is not in the Table 6 top 10. Table 6 gives six genotypes above 0.5: NARITA 8, FHIA-01, NARITA 2, EMB 403, NARITA 14 and NARITA 23.
- Source check: the abstract (p. 2990) calls FHIA-01 the best improved genotype in dry environments, but Table 7 (p. 3001) ranks FHIA-03 and NARITA 24, both hybrids, above it. None differ significantly from Calcutta 4.
