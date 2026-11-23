# Card review: sharma-2025-jafr

- **Card:** papers/sharma-2025-jafr.md
- **Source:** papers-pdf/sharma-et-al-2025.pdf (13 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 38 |
| Supported | 24 |
| Imprecise | 9 |
| Not in source | 2 |
| Contradicted | 3 |
| Source issues (problems in the source itself, not card errors) | 9 |
| Important omissions | 7 |
| Metadata issues | 4 |

The card gets the overall genotype ranking, the sample and the discussion themes mostly right. But it misreports the main socio-economic results. The tree is described as splitting on share sold, when the first split is age (38.2 years) and the share-sold split applies to younger farmers only. It names the wrong clone for farmers who sell more. It also gives the 8% cohort the wrong description (8% is young farmers with small households, not large households) and labels the 8 km tree cutoff as a sample summary. The two "Stated limitations" are not in the source, the number of clones (six) is never given, and two of the six clones are missing from the results. The most important fix is the tree and cohort passage in the Summary (p. 7 and Fig. 7 and Table 2 on p. 9).

## Fixes needed

1. **Tree result (Summary, paragraph 3).** The card says Plackett-Luce trees split farmers by share sold at 42.4%, that low sellers kept CIP392797.22 on top, and that high sellers favored Marabel and CIP393371.157. The source says the first split is age at 38.2 years, and the 42.4% split happens only inside the younger group (p. 7, Fig. 7 p. 9). The text says high sellers "retained" Marabel and CIP393371.58, not CIP393371.157 (p. 7). In addition, the node plots in Fig. 7 show CIP392797.22 with the top letter "a" in all seven terminal nodes (approximate chart reading), so the text's "retained" genotypes do not look like the most preferred ones (see Source issues). The tree covers 132 farmers, not 295 (Fig. 7 root node). Replace "Plackett-Luce trees split farmers by the share of potatoes they sell, at 42.4%. Farmers selling less retained CIP392797.22 as their top choice, while those selling more favored Marabel and CIP393371.157. Splits held in over 93% of 1,000 bootstrap samples, and key traits were retained in over 90%." with:
   > A tree analysis on 132 farmers split first by age, at 38.2 years. Further splits used the share of potatoes sold (42.4%, younger farmers only), household size, distance to market and education. The authors report that splits held in over 93% of 1,000 bootstrap samples.

   And add to Notes:
   > - The text (p. 7) says each tree node "retained" certain genotypes, for example Marabel and CIP393371.58 for younger farmers selling 42.4% or more. The node plots in Fig. 7 (p. 9) show CIP392797.22 on top in all seven nodes (approximate chart reading). Use the tree text with care.

2. **Cohort sentence (Summary, paragraph 3).** The card says clustering found small segments "such as larger households engaged in the potato business (8% of the sample)". Table 2 (p. 9) gives 8% (24 farmers) for Cohort A, younger farmers with small households in business. Older farmers with large households in business are Cohort C, 108 farmers, 37%, the largest group. Only 189 of 295 farmers fall into the four cohorts. Replace "Cluster analysis also identified small farmer segments, such as larger households engaged in the potato business (8% of the sample)." with:
   > Clustering of 189 farmers gave four cohorts by age, household size and business involvement, from 17 to 108 farmers each. Business involvement mattered more than age or household size.

3. **Key number "8 km" (Key numbers).** The card calls 8 km a "sample summary". It is the distance-to-market cutoff found by CART and used in the tree (p. 5, p. 7, Fig. 7 p. 9). Replace the row with:
   > | 8 km | Distance-to-market cutoff in the tree and cohort analysis | This paper |

4. **Stated limitations.** Neither item is stated by the authors. The authors' own limits are about scaling: digital access, institutional inertia and system integration (Conclusion, p. 11 to 12), and digital infrastructure, digital literacy, mobile access and institutional resistance (Introduction, p. 2). Replace the section with:
   > - Scaling the approach will require overcoming limits in digital access, institutional inertia and integration with formal breeding systems.
   > - Limited digital infrastructure, uneven digital literacy, unequal access to mobile phones and institutional resistance to decentralized data can slow uptake of tricot in formal breeding.

   And add to Notes, labelled as the card's own observation:
   > - Card's observation, not stated by the authors: the trial covers one state, and the cohorts range from 17 to 108 farmers, so cohort-level results rest on small groups.

5. **Number of entries and missing clones (Summary, paragraphs 2 and 3).** The card never says that six CIP clones were tested and omits CIP393371.58 (log-worth 0.167, p = 0.028) and CIP381381.13 (0.050, p = 0.522) (p. 2, p. 5, Fig. 3 p. 6). CIP393371.58 is one of the three clones the authors call consistently favored (p. 10, p. 11). Replace "evaluated anonymized potato genotypes alongside the check variety Marabel." with:
   > evaluated six anonymized CIP potato clones alongside the check variety Marabel, three entries per farmer. Four of the clones were released in 2023.

   Replace "CIP clones CIP392797.22 and CIP393371.157 ranked top, with log-worth of 0.620 and 0.309 relative to the check, while CIP398208.29 and CIP398190.200 were least preferred (−0.085 and −0.465)." with:
   > CIP clones CIP392797.22 and CIP393371.157 ranked top, with log-worth of 0.620 and 0.311 relative to the check (the abstract gives 0.309). CIP393371.58 was also above the check (0.167), and CIP381381.13 did not differ from it. CIP398208.29 and CIP398190.200 were least preferred (−0.085 and −0.465), but only CIP398190.200 was significantly below Marabel.

6. **"Results suggest often not" (Summary, paragraph 5).** The source asks the question (p. 9) but does not answer "often not". It says the three most preferred clones are in the national release pipeline, a convergence with formal breeding, while CIP398190.200 shows a gap (p. 10). Replace "The discussion asks whether farmers are truly at the center of national breeding and release programmes, and the results suggest often not. CIP398190.200, despite being officially released," with:
   > The discussion asks whether farmers are truly at the center of national breeding and release programmes. The three most preferred clones are in the national release pipeline, but CIP398190.200, despite being officially released,

7. **Crop stages (Summary, paragraph 2, and Methods "Data").** The card follows the abstract's three stages and trait lists. The methods describe four rounds: vegetative 1, vegetative 2, harvest and postharvest, each with an overall ranking (p. 2, p. 3, Fig. 2 p. 4). The postharvest traits were ease of sale, dormancy and taste, not storability as such. Replace "Assessments covered three stages, vegetative (germination, disease resistance, drought tolerance), harvest (yield, tuber appearance, marketability) and post-harvest (cooking quality, storability)." with:
   > Farmers ranked the best and worst option for each trait in four rounds, two in the vegetative stage (germination, pest and disease resistance, drought and flood tolerance), one at harvest (yield, bacterial wilt damage, maturity, tuber size and appearance, marketability) and one after harvest (ease of sale, dormancy, taste after cooking).

8. **ClimMob sentence (Summary, last sentence).** The card credits ClimMob and ODK with real-time tracking that "helped validate" 295 farmers. The source credits ClimMob with real-time tracking (p. 1) and says ClimMob quality checks flagged five farmers for skipped rankings or missing required data (p. 2). Replace with:
   > ClimMob allowed real-time tracking of the trial, and its quality checks flagged five farmers with skipped rankings or missing data.

9. **Key traits missing (Summary, paragraph 3).** Add after the log-worth sentences:
   > Ease of sale after harvest, yield, disease resistance, taste and bacterial wilt damage were among the traits most linked to overall preference.

   (p. 7, Table 3 p. 10)

10. **Opening sentence wording (Summary, paragraph 1).** The card says top-down breeding produces varieties that "fit local conditions poorly". The source says such varieties "may not be suited" (p. 1). Replace "Potato is emerging as an important crop in Nigeria, but top-down breeding often ignores farmer input, producing varieties that fit local conditions poorly." with:
    > Potato is emerging as an important crop in Nigeria, but top-down breeding often overlooks farmer input, so released varieties may not suit local conditions.

11. **Small wording fix (Summary, paragraph 5).** Replace "Recognizing these dynamics, the authors conclude, explains why" with "Recognizing these dynamics, the authors conclude, can explain why" (p. 10).

12. **Full revised Summary.** Fixes 1, 2 and 5 to 11 together give this text (498 words, within 400 to 500):

    > Potato is emerging as an important crop in Nigeria, but top-down breeding often overlooks farmer input, so released varieties may not suit local conditions. The study evaluates whether tricot, combined with digital tools, better reflects farmer needs.
    >
    > Farmers in seven local government areas of Plateau State (Barikin Ladi, Bassa, Bokkos, Jos North, Jos South, Mangu and Pankshin) evaluated six anonymized CIP potato clones alongside the check variety Marabel, three entries per farmer. Four of the clones were released in 2023. Trial design and allocation ran on ClimMob, and data were collected through a mobile app and ODK. Of 300 farmers, 295 had validated data. Farmers ranked the best and worst option for each trait in four rounds, two in the vegetative stage (germination, pest and disease resistance, drought and flood tolerance), one at harvest (yield, bacterial wilt damage, maturity, tuber size and appearance, marketability) and one after harvest (ease of sale, dormancy, taste after cooking).
    >
    > CIP clones CIP392797.22 and CIP393371.157 ranked top, with log-worth of 0.620 and 0.311 relative to the check (the abstract gives 0.309). CIP393371.58 was also above the check (0.167), and CIP381381.13 did not differ from it. CIP398208.29 and CIP398190.200 were least preferred (−0.085 and −0.465), but only CIP398190.200 was significantly below Marabel. Ease of sale after harvest, yield, disease resistance, taste and bacterial wilt damage were among the traits most linked to overall preference. A tree analysis on 132 farmers split first by age, at 38.2 years. Further splits used the share of potatoes sold (42.4%, younger farmers only), household size, distance to market and education. The authors report that splits held in over 93% of 1,000 bootstrap samples. Clustering of 189 farmers gave four cohorts by age, household size and business involvement, from 17 to 108 farmers each. Business involvement mattered more than age or household size. Market-oriented farmers prioritized commercial traits, while subsistence farmers emphasized resilience.
    >
    > The authors conclude that participatory, data-driven breeding that integrates local knowledge can improve adoption, resilience and food security.
    >
    > The discussion asks whether farmers are truly at the center of national breeding and release programmes. The three most preferred clones are in the national release pipeline, but CIP398190.200, despite being officially released, was among the least preferred because dormancy-related poor germination undermined early establishment, a trait rarely examined in institutional trials. The check Marabel also ranked low. Farmers valued its early maturity for market timing, but its short dormancy, poor storability and limited post-harvest use reduced its appeal. The authors argue that farmer choices reflect behavioral factors, such as risk aversion and planning for storage, household consumption or sales, and not only field traits. Household size, age, market involvement and distance to markets shaped which traits farmers prioritized, in line with the idea that different farmer types need different options. Recognizing these dynamics, the authors conclude, can explain why officially endorsed varieties can diverge from what farmers adopt. ClimMob allowed real-time tracking of the trial, and its quality checks flagged five farmers with skipped rankings or missing data.

13. **Gist.** "ranks two CIP clones above the check" suggests only two were above it. Three clones were significantly above Marabel (Fig. 3, p. 5 to 6). Replace with (27 words):
    > tricot with 295 potato farmers in Plateau State, Nigeria, ranks three CIP clones significantly above the check Marabel and shows market-oriented and subsistence farmers value different traits

14. **not_established (missing).** Add:
    > not_established: that tricot improved adoption or uptake of these varieties, which was not measured; that CIP398208.29 is less preferred than Marabel, since the difference was not significant; that the four cohorts describe all farmers, since they cover 189 of 295 farmers and the tree covers 132; that gender and education do not matter for potato preference in general; that the results hold outside Plateau State

15. **data field.** The statement in the article says data will be made available on request (p. 12). Replace with:
    > data: available on request (data availability statement), supplementary tables S2 and S3 at https://doi.org/10.1016/j.jafr.2025.102135

16. **Methods in brief.** Replace the four bullets with:
    > - **Design.** Balanced incomplete block design set up in ClimMob. Each farmer got three of seven entries (six CIP clones and the check Marabel) as Options A, B and C, with 40 certified sprouted seed tubers per option, planted in three plots of 9 m² at 0.75 m × 0.3 m with a standard fertilizer protocol.
    > - **Data.** Extension agents recorded best and worst rankings in four rounds (two vegetative, harvest, postharvest), each with an overall ranking, plus socio-economic data and GPS, using ODK and ClimMob.
    > - **Sample.** 300 farmers in seven LGAs, 295 validated. The tree analysis covers 132 farmers and the cohort analysis 189, without explanation.
    > - **Analysis.** Plackett-Luce log-worth with Marabel as reference, Kendall tau and stepwise trait selection, a tree (called CART, with Plackett-Luce estimates per node) on socio-economic covariates, k-means clustering into four cohorts labelled with help from a large language model, PCA, likelihood-ratio tests, and 1,000 bootstrap samples for stability.

17. **Key numbers.** Replace the table with:
    > | Number | Context | Primary source |
    > |---|---|---|
    > | 300 / 295 farmers | Recruited / with validated data | This paper |
    > | 7 LGAs | Local government areas in Plateau State | This paper |
    > | 6 + 1 | CIP clones tested / check variety (Marabel) | This paper |
    > | 0.620 / 0.311 | Log-worth of CIP392797.22 / CIP393371.157 vs the check (abstract gives 0.309 for CIP393371.157) | This paper |
    > | 0.167 / 0.050 | Log-worth of CIP393371.58 (p = 0.028) / CIP381381.13 (not significant) | This paper |
    > | −0.085 / −0.465 | Log-worth of CIP398208.29 (not significant) / CIP398190.200 (p < 0.001) | This paper |
    > | 38.2 years / 42.4% | Tree cutoffs for age (first split) / share of potatoes sold (younger farmers only) | This paper |
    > | 6.7 members / 8 km | Cutoffs for household size / distance to market | This paper |
    > | 24 / 17 / 108 / 40 | Farmers in cohorts A to D (8, 6, 37 and 14% of 295) | This paper |
    > | 132 / 189 | Farmers in the tree / in the cohort analysis | This paper |
    > | >93% / >90% | Bootstrap stability of genotype splits / key traits (1,000 samples) | This paper |

18. **Questions.** "At which crop stages should tricot assessments be made for potato?" is not answered by the source, which does not compare assessment schedules. Replace with:
    > - Which traits drive potato farmers' overall preference in Plateau State?

19. **license.** Add the version: "CC BY-NC-ND 4.0" (p. 1).

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Understanding farmer preferences through citizen science. Insights on potato varieties in Nigeria | "Understanding Farmer preferences through citizen Science: Insights on potato varieties in Nigeria" (p. 1) | Supported. The colon to period change is expected. The print capitalizes "Farmer" and "Science". Optional: match the print casing. |
| authors | Sharma K, Atieno E, Mugo J, de Sousa K, van Etten J, Nyawade S | Same six authors, same order (p. 1) | Supported |
| year | 2025 | Available online 9 July 2025, volume 23 (2025) (p. 1) | Supported |
| journal | Journal of Agriculture and Food Research | Same (p. 1) | Supported |
| article | 23, 102135 | 23 (2025) 102135 (p. 1) | Supported |
| type | research article | Full research article with methods and results | Supported |
| doi | https://doi.org/10.1016/j.jafr.2025.102135 | Same (p. 1) | Supported |
| license | CC BY-NC-ND | CC BY-NC-ND 4.0 (p. 1) | Imprecise (version missing) |
| data | see the data availability statement in the article | "Data will be made available on request" (p. 12) | Imprecise. Say it directly. |
| software | ClimMob, PlackettLuce | ClimMob, PlackettLuce, also rpart, cluster, gosset, vegan, MASS, psych (p. 4 to 5) | Supported (partial) |
| crops | potato | Potato (p. 1) | Supported |
| region | Nigeria (Plateau State) | Seven LGAs of Plateau State (p. 1, p. 2) | Supported |
| gist | ranks two CIP clones above the check | Three clones significantly above Marabel, four numerically (p. 5, Fig. 3 p. 6) | Imprecise |
| not_established | missing | Uptake not measured, CIP398208.29 not significantly below check, cohorts cover 189 of 295 | Missing |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Potato is emerging as an important crop in Nigeria | Supported | Introduction (p. 1) | |
| 2 | Summary | Top-down breeding ignores farmer input, producing varieties that fit local conditions poorly | Imprecise | Abstract says varieties "may not be suited" (p. 1) | More certain than source. Fix 10. |
| 3 | Summary | Study evaluates whether tricot with digital tools better reflects farmer needs | Supported | Abstract (p. 1) | Source adds "and improves uptake", which was not measured. |
| 4 | Summary | Seven LGAs, named | Supported | Abstract (p. 1), 2.1 (p. 2) | |
| 5 | Summary | Anonymized genotypes evaluated with check Marabel | Supported | Abstract (p. 1), 2.2 (p. 2) | Number of clones (six) missing. Fix 5. |
| 6 | Summary | Design and allocation on ClimMob, data via mobile app and ODK | Supported | Abstract (p. 1), 2.4 (p. 3) | |
| 7 | Summary | 300 farmers, 295 validated | Supported | 2.2 (p. 2) | |
| 8 | Summary | Three assessment stages with listed traits | Imprecise | Abstract says three (p. 1), methods say four crop stages (p. 2, p. 3), Fig. 2 (p. 4) | Card copies abstract. Postharvest traits differ. Fix 7. |
| 9 | Summary | Log-worth 0.620 and 0.309 for top two clones | Imprecise | 0.309 in abstract (p. 1), 0.311 in results (p. 5) | Source issue, not flagged. Fix 5. |
| 10 | Summary | CIP398208.29 and CIP398190.200 least preferred (−0.085, −0.465) | Supported | Abstract (p. 1), 3.1 (p. 5 to 6), Fig. 3 (p. 6) | CIP398208.29 not significant (p = 0.259). |
| 11 | Summary | Plackett-Luce trees split farmers by share sold at 42.4% | Imprecise | First split is age 38.2, share-sold split only in younger group, n = 132 (p. 7, Fig. 7 p. 9) | Fix 1. |
| 12 | Summary | Farmers selling less retained CIP392797.22 as top choice | Supported | Text: retained CIP392797.22 and CIP393371.157 (p. 7). Fig. 7 nodes: CIP392797.22 top (approximate, p. 9) | |
| 13 | Summary | Farmers selling more favored Marabel and CIP393371.157 | Contradicted | Text says Marabel and CIP393371.58 (p. 7). Fig. 7 nodes show CIP392797.22 on top in these nodes too (approximate, p. 9) | Fix 1. |
| 14 | Summary | Splits held in >93% of 1,000 bootstraps, key traits in >90% | Supported | 3.2 and 3.4 (p. 7) | |
| 15 | Summary | Market-oriented farmers prioritize commercial traits, subsistence farmers resilience | Supported | Abstract (p. 1), Discussion (p. 10) | |
| 16 | Summary | Small segments such as larger households in potato business (8%) | Contradicted | Table 2: 8% is Cohort A, younger with small households in business. Large households in business are 37% (p. 9) | Fix 2. |
| 17 | Summary | Authors conclude participatory, data-driven breeding can improve adoption, resilience, food security | Supported | Abstract (p. 1) | |
| 18 | Summary | Discussion asks if farmers are at center, results suggest often not | Imprecise | Question posed (p. 9). Source notes convergence for top three clones (p. 10) | Overstated. Fix 6. |
| 19 | Summary | CIP398190.200 released but least preferred due to dormancy-related poor germination, rarely tested in institutional trials | Supported | Discussion (p. 10), Table 1 release 2023 (p. 5) | |
| 20 | Summary | Marabel also ranked low | Supported | Discussion (p. 10) | Marabel is 5th of 7 in Fig. 3 (p. 6). |
| 21 | Summary | Marabel valued for early maturity, but short dormancy, poor storability, limited postharvest use | Supported | Discussion (p. 10) | |
| 22 | Summary | Choices reflect behavioral factors such as risk aversion and planning | Supported | Discussion (p. 10) | Source says "market timing" where card says "sales". Acceptable. |
| 23 | Summary | Household size, age, market involvement, distance shaped trait priorities, different farmer types need different options | Supported | Discussion, citing Stringer et al. (p. 10) | |
| 24 | Summary | Recognizing dynamics explains divergence from endorsed varieties | Supported | Discussion (p. 10) | Source says "can explain". Fix 11. |
| 25 | Summary | ClimMob and ODK enabled real-time tracking, helped validate 295 of 300 | Imprecise | Tracking credited to ClimMob (p. 1). ClimMob quality checks flagged five records (p. 2) | Fix 8. |
| 26 | Methods | ClimMob allocation, anonymized genotypes plus check, three per farmer | Supported | 2.2 (p. 2 to 3) | |
| 27 | Methods | Mobile app and ODK, three assessment stages | Imprecise | Four rounds (p. 3) | Fix 7, Fix 16. |
| 28 | Methods | 300 farmers in seven LGAs, 295 validated | Supported | 2.2 (p. 2) | |
| 29 | Methods | PL log-worth, PL trees, 1,000 bootstraps, clustering | Supported | 2.5 (p. 4 to 5), 3.4 (p. 7) | Incomplete. Fix 16. |
| 30 | Limitations | One state in Nigeria | Not in source | Authors do not state this | True of the design, but not an author limitation. Fix 4. |
| 31 | Limitations | Segments small, limiting segment-specific recommendations | Not in source | Authors call segments "robust" (p. 7) | Fix 4. |
| 32 | Key numbers | 300 / 295 farmers | Supported | p. 2 | |
| 33 | Key numbers | 7 LGAs | Supported | p. 1, p. 2 | |
| 34 | Key numbers | 0.620 / 0.309 | Imprecise | 0.311 in results (p. 5) | Fix 17. |
| 35 | Key numbers | −0.085 / −0.465 | Supported | p. 1, p. 5 to 6 | |
| 36 | Key numbers | 42.4% tree split point | Imprecise | Applies to younger farmers only, second split (p. 7, Fig. 7 p. 9) | Fix 17. |
| 37 | Key numbers | >93% / >90% bootstrap stability | Supported | p. 7 | |
| 38 | Key numbers | 8 km, distance to market, sample summary | Contradicted | 8 km is the CART cutoff (p. 5, p. 7, Fig. 7 p. 9) | Fix 3. |

Derived numbers recomputed: cohort shares 24/295 = 8.1%, 17/295 = 5.8%, 108/295 = 36.6%, 40/295 = 13.6%, total 189/295 = 64.1%, matching Table 2. Tree terminal nodes sum to 132 (13 + 25 + 18 + 27 + 12 + 9 + 28), matching the root node. Business cohort 24 + 108 = 132 and non-business 17 + 40 = 57, matching p. 8. The card contains no derived numbers of its own.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Log-worth of CIP393371.157 is 0.309 in the abstract and 0.311 in the results | p. 1, p. 5 | No | - The log-worth of CIP393371.157 is 0.309 in the abstract and 0.311 in the results (p. 5). |
| Abstract says three crop stages, methods say four (two vegetative rounds, harvest, postharvest), and 2.5.4 lists four stages including "overall" | p. 1, p. 2, p. 3, p. 5 | No | - The abstract describes three assessment stages, but the methods describe four data rounds, with two in the vegetative stage (p. 3). |
| Tree text says nodes "retained" certain genotypes (for example Marabel and CIP393371.58, or CIP398190.200 for older large households), but the node plots show CIP392797.22 top in all seven nodes and CIP398190.200 near the bottom. The branch labels look like genotype codes, not preferences | p. 7, Fig. 7 p. 9 | No, and the card repeats a version of the text | See Fix 1 Notes text. |
| Sample sizes change without explanation: 295 validated, 132 in the tree, 189 in the cohorts. The tree puts 63% of farmers in the younger branch, but younger cohorts A and B are only 41 of 189 | Fig. 7 p. 9, Table 2 p. 9, p. 7 | No | - The tree covers 132 farmers and the cohort analysis 189, out of 295 with validated data. The paper does not explain the difference. |
| Cohorts pair young with small households and old with large households, so farmers outside these pairs are not counted. Household cutoff is 6.1 in the younger tree branch but 6.7 for cohorts. Table 2 uses "≥42.4%" and "≤42.4%", which overlap | p. 7, Table 2 p. 9 | No | - The four cohorts combine age and household size (young and small, old and large), so age and household effects cannot be separated. |
| Log-worth is defined as the negative log of a p-value. In Plackett-Luce models the log-worth is the log of the worth parameter | p. 4 to 5, 2.5.4 p. 5 | No | - The paper defines log-worth as the negative log of a p-value (p. 4 to 5). This is not the usual Plackett-Luce definition, which is the log of the estimated worth. |
| Section 3.2 says "six traits at harvest" but lists four | p. 7 | No | Low importance. No note needed. |
| Table 3 "Overall" lists High Yield and Disease Resistance twice with different values. Cohort D shows only Ease of Sale as significant, while 3.6 says Cohort D emphasized disease resistance and drought tolerance | p. 10, p. 8 | No | - Table 3 (p. 10) lists some traits twice in the overall rows, so its overall results should be read with care. |
| CIP398208.29 is called "least preferred" in the abstract but is not significantly different from Marabel (p = 0.259, same letter group) | p. 1, p. 5 to 6, Fig. 3 p. 6 | No | Covered by revised Summary and not_established. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Six CIP clones plus check, four released in 2023 (Unica, Juriya, Babban, Kyau), Marabel from Europlant 2016 | No | High | Fix 5. Local names optional in Notes. |
| Results for CIP393371.58 (0.167) and CIP381381.13 (0.050) | No | High | Fix 5, Fix 17. |
| Traits most linked to overall preference (ease of sale, yield, disease resistance, drought tolerance, taste, bacterial wilt, early maturity) | No | High | Fix 9. |
| Tree structure: first split age 38.2, 132 farmers | No | High | Fix 1. |
| Four cohorts, sizes 24, 17, 108, 40 (189 farmers), business 132 vs non-business 57 | Partly, wrong | High | Fix 2, Fix 17. |
| Convergence: top three clones are in the national release pipeline | No | High | Fix 6. |
| Authors' own limitations (scaling, digital access, institutional inertia) | No (card lists others) | High | Fix 4. |
| Aim also covers uptake and whether tricot complements release protocols, plus policy lessons | Partly | Medium | Optional. Add to not_established that uptake was not measured (Fix 14). |
| Trial protocol: BIBD, 40 sprouted tubers per option, three 9 m² plots, standard fertilizer, extension agent supervision, multi-channel recruitment | No | Medium | Fix 16. |
| Overall likelihood-ratio test: drought, pest resistance, dormancy, germination not significant | No | Medium | Optional Notes: "- In the pooled likelihood-ratio test, drought tolerance, pest resistance, dormancy and germination were not significant (Table 3, p. 10)." |
| Gender and education excluded from final CART model, education splits older farmers | No | Medium | Optional Notes: "- Gender and education showed no significant association in CART and were dropped, though education appears in one tree split (p. 5, p. 7)." |
| Cohort labels generated with a large language model, for interpretation only | No | Low | Covered in Fix 16. |
| CIP398190.200 and CIP398208.29 preferred in no cohort | No | Low | Optional. |
| Data available on request | No | Medium | Fix 15. |
| Funding includes BMZ, CGIAR, and 1000FARMS (Gates) for two authors | No | Low | Optional. |

## Template compliance

- Summary word count: 404 (within 400 to 500). The revised Summary in Fix 12 is 498.
- Gist: 26 words (under 30). Revised gist is 27.
- Keywords: 10 (within 8 to 12).
- Questions: 4 (within 4 to 7). One question is not answered by the source (Fix 18).
- House style: tricot in lowercase throughout. No em dashes in card prose.
- not_established is missing (Fix 14).
- License lacks version (Fix 19).
