# Card review: brown-2023-agronj

- **Card:** papers/brown-2023-agronj.md
- **Source:** papers-pdf/brown-et-al-2023.pdf (20 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

Page references give the printed journal page first and the PDF page in brackets. PDF page = printed page minus 2989.

## Overview

| Check | Result |
|---|---|
| Claims checked | 71 |
| Supported | 59 |
| Imprecise | 9 |
| Not in source | 1 |
| Contradicted | 2 |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 5 |
| Metadata issues | 3 |

The card is accurate on almost all numbers. Every Key numbers value matches the text, Table 6, Table 7 or Figure 4, and the main results are reported fairly. The two contradicted claims are both about where the data came from: the card says MGIS supplied a thesis (it came from AgTrials) and the Notes say Table 1 lists eight studies (it lists seven). The most important fix for meaning is in the Summary, which credits the approach to Brown et al. (2022) instead of Brown et al. (2020) and says no dry-environment genotype differed from the reference, when the source says this only for the top 10. The gist (37 words) and keywords (13) are over the template limits.

## Fixes needed

1. **Notes, second bullet (Contradicted).** Card: "The abstract says 110 evaluations and 31 trials, Table 1 lists the eight studies that provided them." Source: the abstract gives neither number. The Conclusions give 110 evaluations and 31 trials (p. 3006 (PDF 17)). Table 1 (p. 2994 (PDF 5)) lists seven studies. Replace with:
   "- The Conclusions (p. 3006) give 110 evaluations in 31 trials. The abstract does not give these numbers. Table 1 (p. 2994) lists the seven studies that provided them: IMTP-1 to IMTP-3 and Orlando Narváez (2004) from AgTrials, Irish et al. (2013, 2019) from MGIS, and the WP4-BBB project from MusaBase. Its rankings per study (4, 13, 26, 3, 2, 2, 60) add up to 110 and its locations per study (6, 8, 7, 3, 1, 1, 5) add up to 31, so each trial is one study location (card's calculation)."

2. **Methods in brief, Data bullet (Contradicted).** Card: "from AgTrials (IMTP 1 to 3), MGIS (a thesis and Irish et al.) and MusaBase (WP4-BBB project)." Source, Table 1 (p. 2994 (PDF 5)): the Orlando Narváez (2004) thesis is from AgTrials, and MGIS supplied Irish et al. (2013) and Irish et al. (2019). Replace with:
   "- **Data.** 31 trials, 22 locations, 1990 to 2019, 62 genotypes, from seven studies (Table 1): AgTrials (IMTP 1 to 3 and the thesis of Orlando Narváez 2004), MGIS (Irish et al. 2013 and 2019) and MusaBase (WP4-BBB project)."

3. **Summary, paragraph 1, last sentence (Imprecise attribution).** Card: "The paper extends the rank-based data synthesis of Brown et al. (2022), developed for tricot rankings, to data that were never collected as rankings." Source: "Here, we apply the data synthesis approach (Brown et al., 2020)" (p. 2991 (PDF 2)). Brown et al. (2022) is cited as the tricot common bean application. Replace with:
   "The paper applies the data synthesis approach of Brown et al. (2020), which Brown et al. (2022) used for tricot rankings of common bean, to data that were not collected as rankings."

4. **Summary, paragraph 3 (Imprecise, changes meaning).** Card: "In dry environments only the landrace Saba surpassed 50% reliability and no genotype differed significantly from the reference." Source: the differences are not significant for the top 10 genotypes, which did perform better than the rest (p. 3005 (PDF 16)). Lower genotypes may differ. Replace with:
   "In dry environments only the landrace Saba surpassed 50% reliability, and none of the top 10 differed significantly from the reference. FHIA-01 did well in both."

5. **Summary, paragraph 3 (Imprecise certainty, and omission of the humidity reading).** Card: "split the data on the maximum length of dry spell at 13 days. The humid node held 41 rankings and the dry node 69. Humid environments favour the disease, and there NARITA 8 ..." Source: humid environments are "assumed to be more favorable" for BLSD (p. 3003 (PDF 14)). The card also never says why a dry spell index gives "humid" and "dry" nodes. The source explains that MLDS is barely correlated with rainfall indices (r = −0.06 and −0.03) but strongly with relative humidity at 09:00 (r = −0.75) (p. 3000 (PDF 11)), and concludes that humidity is the main climatic factor (p. 3006 (PDF 17)). Replace with:
   "split the data on the maximum length of dry spell at 13 days. This index was barely correlated with rainfall totals but strongly and negatively with relative humidity at 09:00 (r = −0.75), so the authors read the two nodes as humid (41 rankings) and dry (69 rankings) environments. In humid environments, assumed to favour the disease, NARITA 8 ..."

6. **Summary, paragraph 4 (Imprecise).** Card: "It shows that decades of incompatible trial data can be reused when expert knowledge of the trait guides the choice of metrics". Source: expert knowledge of genotype reactions reduces the information lost when metrics become rankings (p. 3006 (PDF 17)). The metric choice was driven by data volume and homogeneity (p. 2992 (PDF 3)). Replace "The paper matters for two reasons. It shows that decades of incompatible trial data can be reused when expert knowledge of the trait guides the choice of metrics, and that" with:
   "The paper shows that trial data once seen as incompatible can be analysed together, with expert knowledge of the trait limiting the information lost in ranking, and that"

7. **Summary, paragraph 1 (Imprecise, small) and word count.** Card: "multi-environment trials of Musa are rare because the crop needs large plots and long cycles." Source: they are "complex to conduct" because of space and time needs (p. 2991 (PDF 2)). Replace with: "multi-environment trials of Musa are hard to run because the crop needs much space and time." To keep the summary at 500 words or fewer after fixes 3 to 6, also shorten the first sentence to "David Brown and colleagues ask whether ..." and the gosset sentence to: "Each metric was converted to a ranking with gosset, in the direction that means resistance (highest youngest leaf spotted first, lowest disease index first)." With all seven fixes the summary is 499 words (checked by script).

8. **Gist (too long, slightly imprecise).** The gist is 37 words. "different resistant genotypes" overstates the dry node, where no top genotype differs from the reference. Replace with (28 words):
   "gist: Turning five black leaf streak metrics from 31 Musa trials into rankings allows joint analysis, and dry spell length separates humid and dry environments where genotypes rank differently"

9. **Keywords (13, limit is 12).** Remove "rank aggregation", which overlaps with "data synthesis":
   "keywords: data synthesis, heterogeneous trials, Plackett-Luce trees, black leaf streak disease, black Sigatoka, Musa, AgERA5, dry spell, relative humidity, reliability, stability assessment, genotype by environment"

10. **Methods in brief, Reliability bullet (Imprecise).** Quasi-standard errors belong to the worth estimates. Reliability has its own standard error (relSE, Tables 6 and 7). The source also says reliability is conservative because of pseudo-ranking shrinkage (p. 3000 (PDF 11)). Replace with:
    "- **Reliability.** Probability of outperforming the reference Calcutta 4 (Eskridge and Mumm 1992), with its standard error. Worth estimates carry quasi-standard errors. Reliability estimates are conservative because pseudo-rankings shrink the worth estimates."

11. **Notes, first bullet (Imprecise).** Card: "This paper is the first application to non-ranking data (disease scores) and the first to Musa." Source: first application to BLSD data "originally collected in a non-ranking format" (p. 2991 (PDF 2)), and first to combine heterogeneous Musa trial data with climate covariates (p. 3006 (PDF 17)). Replace with:
    "- Successor to brown-2022-cropsci, which pooled tricot rankings. The authors call this the first application of the approach to black leaf streak data first collected in a non-ranking format (p. 2991), and the first to combine heterogeneous Musa trial data with climate covariates (p. 3006)."

12. **Key numbers, 22 locations row (Imprecise label).** The source does not state "14 countries". It is the card's count of Table 2, and Puerto Rico is a territory. Replace with:
    "| 22 locations | Unique trial locations, in 14 countries or territories by the card's count of Table 2 | This paper (country count is the card's own) |"

13. **not_established (weak).** Add the significance claim the Results text makes but Table 6 does not support, the explanatory-only status, and the drought hypothesis. Replace with:
    "not_established: that dry environments are disease-free; that the top genotypes in dry environments differ significantly from the reference Calcutta 4; that NARITA 8 outperforms Calcutta 4 with statistical significance (Table 6 gives p = 0.065); a causal mechanism for the humidity effect, or whether it acts on the host or the pathogen; that genotypes outperforming Calcutta 4 in one environment do so in the other; that the tree predicts genotype reactions at new sites, since it was fitted to explain and not validated for prediction; that drought predisposes Musa to BLSD, which the authors raise only as a hypothesis"

14. **Notes, third bullet (Not in source, label only).** The curated workflow in tricot-analysis-workflows is not in the paper. Start the bullet with "Outside the source:" so readers know it is repository knowledge.

15. **Notes, add source issues and two practical details.** See the Source issues and Completeness sections for the exact text.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Rank-based data synthesis of heterogeneous trials to identify the effects of climatic factors on the reaction of Musa genotypes to black leaf streak disease | Same (p. 2990 (PDF 1)) | Supported |
| authors | Brown D, de Bruin S, de Sousa K, Abadie C, Carpentier S, Machida L, van Etten J | Same order (p. 2990 (PDF 1)) | Supported |
| year | 2023 | Published online 9 October 2023, Agronomy Journal 2023 (p. 2990 (PDF 1)) | Supported |
| journal | Agronomy Journal | Agronomy Journal (p. 2990 (PDF 1)) | Supported |
| article | 115(6), 2990-3009 | 2023;115:2990–3009, issue 6 in the download line (p. 2990 (PDF 1)) | Supported |
| type | research article | "ORIGINAL ARTICLE" (p. 2990 (PDF 1)) | Supported |
| doi | https://doi.org/10.1002/agj2.21436 | DOI 10.1002/agj2.21436 (p. 2990 (PDF 1)) | Supported |
| license | CC BY | Creative Commons Attribution License, no version given (p. 2990 (PDF 1)) | Supported |
| data | GitHub repo Data_Synthesis_Musa_Trials_BLSD, plus curated workflow | Data availability statement gives the GitHub repo (p. 3006 (PDF 17)). The curated workflow is not in the paper. | Supported (workflow part is outside knowledge, acceptable in frontmatter) |
| crops | banana, plantain (Musa) | Table 4 includes plantain and banana genotypes (p. 2996 to 2998 (PDF 7 to 9)) | Supported |
| region | 22 locations in 14 listed countries | Table 2 and Figure 1 (p. 2993, 2995 (PDF 4, 6)) | Supported |
| gist | 37 words, "different resistant genotypes" | Dry node top 10 not different from reference (p. 3005 (PDF 16)) | Imprecise, and over 30 words |
| not_established | Four items | Items are correct but miss the NARITA 8 significance claim, explanatory-only status and the drought hypothesis | Supported, but weak (see fix 13) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Brown and colleagues, with de Sousa and van Etten, ask whether scattered BLSD evaluations can be analysed together | Supported | Author list and objectives (p. 2990, 2991 (PDF 1, 2)) | |
| 2 | Summary | BLSD caused by Pseudocercospora fijiensis | Supported | p. 2991 (PDF 2) | |
| 3 | Summary | Most destructive leaf disease of banana, control depends on fungicides, resistant varieties matter | Supported | p. 2991 (PDF 2) | |
| 4 | Summary | Multi-environment trials of Musa are rare because of large plots and long cycles | Imprecise | "complex to conduct" because of space and time (p. 2991 (PDF 2)) | "rare" is not said. Fix 7 |
| 5 | Summary | Extends rank-based data synthesis of Brown et al. (2022) | Imprecise | Approach cited to Brown et al. (2020) (p. 2991 (PDF 2)) | Attribution. Fix 3 |
| 6 | Summary | Data from AgTrials, MusaBase and MGIS | Supported | p. 2992 (PDF 3) | |
| 7 | Summary | Four inclusion criteria | Supported | p. 2992 (PDF 3) | |
| 8 | Summary | 31 trials, 22 locations, 1990 to 2019, 62 genotypes | Supported | p. 3006 (PDF 17), p. 2992 (PDF 3) | |
| 9 | Summary | Three kinds of genotype, wild relative Calcutta 4, landraces, improved | Supported | p. 2992 (PDF 3), Table 4 | |
| 10 | Summary | Five metrics YLS, DDT, DII, NSL, NFL | Supported | p. 2992 (PDF 3), Table 3 (p. 2995 (PDF 6)) | |
| 11 | Summary | Converted with gosset, YLS highest first, DII lowest first | Supported | p. 2992 (PDF 3) | |
| 12 | Summary | Each block gave a ranking, means gave one ranking per trial | Supported | p. 2992 (PDF 3) | |
| 13 | Summary | Each cycle its own ranking, ratoon starts at end of previous cycle | Supported | p. 2992, 2993 (PDF 3, 4) | |
| 14 | Summary | 110 rankings | Supported | p. 2992 (PDF 3) | |
| 15 | Summary | AgERA5, climatrends indices, relative humidity at five times | Supported | p. 2993 (PDF 4), Table 5 | |
| 16 | Summary | Explanatory tree, large nodes, Bonferroni alpha, split on MLDS at 13 days | Supported | p. 2994 (PDF 5), Figure 4 (p. 3002 (PDF 13)), p. 3003 (PDF 14) | |
| 17 | Summary | Humid node 41, dry node 69 rankings | Supported | Figure 4 panel labels n=41 and n=69 (p. 3002 (PDF 13)) | 41 + 69 = 110 |
| 18 | Summary | Humid environments favour the disease | Imprecise | "assumed to be more favorable" (p. 3003 (PDF 14)) | Stated as fact. Fix 5 |
| 19 | Summary | NARITA 8, FHIA-01, NARITA 2 highest, reliability above 0.7 | Supported | Table 6 (p. 3001 (PDF 12)) | |
| 20 | Summary | Dry: only Saba above 50%, no genotype differed significantly from reference | Imprecise | Statement covers the top 10 only (p. 3005 (PDF 16)) | Overgeneralised. Fix 4 |
| 21 | Summary | NARITA 8 and 24 opposite reactions, read as resistance expressed under different conditions | Supported | p. 3003, 3005 (PDF 14, 16) | Source hedges with "it might be". "read as" is acceptable |
| 22 | Summary | MLDS chosen in 855 of 1000 subsample trees, tree stable | Supported | p. 3000 (PDF 11), Figure 7 | |
| 23 | Summary | Decades of incompatible data reused when expert knowledge guides choice of metrics | Imprecise | Expert knowledge reduces information loss (p. 3006 (PDF 17)). Metric choice by data volume (p. 2992 (PDF 3)) | Fix 6 |
| 24 | Summary | Reliability and ranking probabilities give a basis to choose genotypes for new locations | Supported | p. 3006 (PDF 17) | |
| 25 | Summary | Authors call for data sharing in public repositories | Supported | p. 3006 (PDF 17) | |
| 26 | Methods | Data bullet: MGIS gave a thesis and Irish et al. | Contradicted | Table 1: thesis from AgTrials, MGIS gave Irish et al. 2013 and 2019 (p. 2994 (PDF 5)) | Fix 2 |
| 27 | Methods | Inclusion criteria | Supported | p. 2992 (PDF 3) | |
| 28 | Methods | rank_numeric per block or mean, per cycle, direction per trial, 110 rankings | Supported | p. 2992 (PDF 3) | |
| 29 | Methods | Weakly connected removed, 5% threshold by iteration, 37% discarded, npseudo = 2 | Supported | p. 2994, 2995, 2997 (PDF 5, 6, 8) | |
| 30 | Methods | Ties: one kept at random, choice did not change results | Supported | p. 2997 (PDF 8) | Source says "negligible influence" |
| 31 | Methods | Climate variables, climatrends indices, near-zero variance removed | Supported | p. 2993 (PDF 4), Table 5 footnote (TRa removed) (p. 2999 (PDF 10)) | |
| 32 | Methods | Alpha 0.05 Bonferroni, minimum node 35% | Supported | p. 2994 (PDF 5) | |
| 33 | Methods | stablelearner, 1000 subsamples of 80% without replacement | Supported | p. 2999 (PDF 10) | |
| 34 | Methods | Reliability with quasi-standard errors | Imprecise | Reliability has relSE. Quasi-SE are for worth (Tables 6, 7, p. 3000 (PDF 11)) | Fix 10 |
| 35 | Limitations | Ranking loses information, expert knowledge reduces it | Supported | p. 3006 (PDF 17) | |
| 36 | Limitations | Small data set, few Musa evaluations in public repositories | Supported | p. 3006 (PDF 17) | |
| 37 | Limitations | Dry not disease-free, mechanism not discriminated | Supported | p. 3003 (PDF 14) | Source: cannot tell host from pathogen effect |
| 38 | Limitations | Leaf-based metrics may be biased in dry environments | Supported | p. 3005 (PDF 16) | |
| 39 | Limitations | Not outperforming Calcutta 4 is not poor performance | Supported | p. 3005 (PDF 16) | |
| 40 | Key numbers | 31 trials | Supported | p. 3006 (PDF 17) | |
| 41 | Key numbers | 22 locations in 14 countries | Imprecise | 22 in Figure 1 (p. 2992 (PDF 3)). 14 is the card's count of Table 2 | Fix 12 |
| 42 | Key numbers | 1990–2019 | Supported | p. 2992 (PDF 3), Table 1 | |
| 43 | Key numbers | 62 genotypes | Supported | p. 2992 (PDF 3). Figure 4 shows 62 names (counted) | |
| 44 | Key numbers | 110 rankings | Supported | p. 2992 (PDF 3) | Table 1 sums to 110 |
| 45 | Key numbers | 5 metrics | Supported | p. 2992 (PDF 3) | |
| 46 | Key numbers | 33, 3, 41, 24, 9 | Supported | p. 2992 (PDF 3) | Sum 110 |
| 47 | Key numbers | 13 days | Supported | p. 3003 (PDF 14), Figure 4 | |
| 48 | Key numbers | 41 and 69 | Supported | Figure 4 (p. 3002 (PDF 13)) | |
| 49 | Key numbers | −0.75 with RH at 09:00 | Supported | p. 3000 (PDF 11) | |
| 50 | Key numbers | 855 of 1000 | Supported | p. 3000 (PDF 11) | |
| 51 | Key numbers | 0.817, 0.767, 0.722 | Supported | Table 6 (p. 3001 (PDF 12)) | |
| 52 | Key numbers | 0.509 Saba | Supported | Table 7 (p. 3001 (PDF 12)) | |
| 53 | Key numbers | 5% and 35% | Supported | p. 2994 (PDF 5) | |
| 54 | Key numbers | 37% discarded | Supported | p. 2995 (PDF 6) | |
| 55 | Notes | First application to non-ranking data and first to Musa | Imprecise | Narrower wording (p. 2991, 3006 (PDF 2, 17)) | Fix 11 |
| 56 | Notes | Abstract says 110 and 31, Table 1 lists eight studies | Contradicted | Numbers are in the Conclusions. Table 1 lists seven studies (p. 2994, 3006 (PDF 5, 17)) | Fix 1 |
| 57 | Notes | Curated workflow in tricot-analysis-workflows | Not in source | Not mentioned in the paper | Outside knowledge. Label it (fix 14) |
| 58 | Notes | David Brown is not in people.md | Supported | Checked in the repository people.md, not a source claim | |
| 59 to 71 | Frontmatter | 13 fields | 12 Supported, 1 Imprecise | See Metadata check | gist is the Imprecise one |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Results say only NARITA 8 outperforms Calcutta 4 with statistical significance in humid environments, but Table 6 gives p = 0.065 for NARITA 8 | Results p. 3000 (PDF 11), Table 6 p. 3001 (PDF 12) | No (card wisely makes no such claim) | "- Source check: the Results (p. 3000) say NARITA 8 outperforms Calcutta 4 with statistical significance in humid environments, but Table 6 (p. 3001) gives p = 0.065, above 0.05. Treat NARITA 8 as the best but not a significant winner." |
| Discussion lists NARITA 20 among humid-environment genotypes with more than 50% reliability, but NARITA 20 is not in the Table 6 top 10, and its worth in Figure 4 node 2 is below zero (read from the chart, approximate), which implies reliability below 0.5 | p. 3006 (PDF 17), Table 6, Figure 4 (p. 3002 (PDF 13)) | No | "- Source check: the Discussion (p. 3006) lists NARITA 20 among humid-environment genotypes above 50% reliability, but it is not in Table 6 and its worth in Figure 4 is below the reference. Table 6 gives six genotypes above 0.5: NARITA 8, FHIA-01, NARITA 2, EMB 403, NARITA 14 and NARITA 23." |
| Abstract says FHIA-01 was the best performing improved genotype in dry environments, but Table 7 ranks two other hybrids above it: FHIA-03 (−0.060) and NARITA 24 (−0.117) versus FHIA-01 (−0.294) | Abstract p. 2990 (PDF 1), Table 7 p. 3001 (PDF 12) | No | "- Source check: the abstract (p. 2990) calls FHIA-01 the best improved genotype in dry environments, but Table 7 (p. 3001) ranks FHIA-03 and NARITA 24, both hybrids, above it. None differ significantly from Calcutta 4." |
| Table 5 defines tropical nights by maximum temperature above 25 °C, which looks like a typo for minimum temperature. The variable was removed for near-zero variance, so results are not affected | p. 2999 (PDF 10) | No | Low importance. No Notes text needed. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim and three specific objectives (aggregate, assess climate effect, identify best genotypes) | Partly | Low | None needed |
| Explain rather than predict | Yes (Summary, "explanatory mode") | Medium | Add to not_established (fix 13) |
| Design: seven studies, 31 trials, 22 locations, RCBD mostly | Yes, but study list wrong | Medium | Fix 1 and fix 2 |
| MLDS read as humidity: weak correlation with rainfall (r = −0.06, −0.03), strong with RH (r = −0.75). Conclusion that humidity is the main factor | Partly (only −0.75 in Key numbers) | Medium | Fix 5 |
| Reference genotypes link the network: Williams and Gros Michel (susceptible), Pisang Ceylan (partially resistant). FHIAs and NARITAs never compared directly | No | Medium | Add to Methods, Network bullet: "Williams, Gros Michel and Pisang Ceylan act as common references that link genotypes never tested together. FHIAs and NARITAs were never compared directly in any trial (p. 2997, Figure 2)." |
| Metric choice when a trial had several metrics: the one with most data and the most homogeneous data set | No | Medium | Add to Rankings bullet: "Where a trial reported several metrics, the one with most data and giving the most homogeneous data set was used." |
| Reliability is conservative because of pseudo-ranking shrinkage | No | Medium | Fix 10 |
| FHIA-01 performed well in both environments, linked to its drought tolerance | No | Medium | Fix 4 adds a short sentence |
| 6 of the top 10 in dry environments carry the B genome, linked to drought tolerance | No | Low | Optional Notes line |
| Drought may predispose Musa to BLSD (hypothesis) | No | Low | In not_established (fix 13) |
| Model agrees with known susceptible genotypes (Grand Naine, Gros Michel, Niyarma Yik) | No | Low | Optional |
| AgERA5 lets trial climate be rebuilt where no station data exist | Partly | Low | Optional |
| 5% presence threshold in practice | No | Low | Optional Notes line: "With 31 trials, the 5% threshold means a genotype had to appear in at least 2 trials (card's calculation)." |
| Authors' limitations (information loss, small sample, leaf-metric bias, Calcutta 4 not a pass/fail line) | Yes | High | Present |
| Conclusions (use reliability with worth, share data) | Yes | High | Present |

## Template compliance

| Item | Result | Status |
|---|---|---|
| Summary word count | 478 (499 after the suggested fixes) | Pass |
| Gist length | 37 words | Fail (fix 8 gives 28) |
| Keywords | 13 | Fail (fix 9 gives 12) |
| Questions | 6 | Pass |
| House style | tricot written in lowercase 5 times, maniva not used | Pass |
| Long-format sections | All present | Pass |
