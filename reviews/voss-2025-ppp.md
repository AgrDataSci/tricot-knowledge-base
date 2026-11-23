# Card review: voss-2025-ppp

- **Card:** papers/voss-2025-ppp.md
- **Source:** papers-pdf/voss-et-al-2025.pdf (14 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-23, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 47 (13 frontmatter fields, 34 body claims) |
| Supported | 34 |
| Imprecise | 7 |
| Not in source | 4 |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 3 |
| Important omissions | 5 (high importance) |
| Metadata issues | 5 (authors order, data, software, missing not_established, article number not checked) |

The card gets the design, sample sizes and the four segments right, and every Key numbers row is correct. But it misses the paper's decision results (the likelihood-ratio test and the worth and regret analysis) and states the opposite of one of them: it says no single variety serves all users, while the source says A2004 would be acceptable to all four segments (p. 8). The "Stated limitations" are not the authors' own, and the last summary paragraph adds claims that are not in the source. The author order is also wrong.

## Fixes needed

1. **Contradicted main point (Summary, paragraph 3).** Card: "These segments preferred different varieties, so a single best variety would not serve all users." Source p. 8 (Table 6 and text): whether judged by worth or by regret, A2004 would be acceptable to all groups. For a second variety, AC-NL has high worth but mainly suits Older Men Generalists, while Poli minimizes regret for the other three. Replace with:
   > These segments preferred different varieties, which the authors read as a sign of how varied the producers of neglected crops are.

2. **Main results missing, and summary paragraph 6 not in source.** Card paragraph 6 says the trials show tricot "working at scale for a leafy vegetable, extending the method beyond the grain, legume and root crops where it was first developed", across countries "with different languages". None of this is in the source. The paper describes agroecological, socioeconomic and cultural contexts (p. 3), not languages, and does not compare with earlier tricot crops. The sentence on 1,159 women repeats paragraph 2. Replace the whole paragraph with:
   > Across all farmers, preferences leaned toward Akeri, Poli and AM-NKGN, linked to marketability, leaf size, yield and taste at the fourth harvest. A likelihood-ratio test showed that the four segments ranked varieties differently for plant survival, yield and marketability up to the third harvest, but not for fourth-harvest traits or overall performance, when fewer observations were recorded. In a worth and regret analysis of marketability, A2004 was acceptable to all four segments. As a second variety, AC-NL had high overall worth but mainly suited older men generalists, while Poli gave the lowest regret and was preferred by the other three segments. The authors note that the gender balance of participants differed by country, that men may have overstated their role in amaranth, and that older men generalists gave inconsistent rankings.

   This keeps the summary at about 460 words.

3. **Stated limitations are not the authors'.** "Segments ... may differ elsewhere" is not in the source. "Variety availability and seed supply constrain uptake" is background from the introduction (p. 3), not a limitation of the study. Replace the section with:
   > - Differences in who controls amaranth production and sales are likely, at least in part, a result of the different gender balance of participants in each country (p. 6).
   > - Women and men both tended to report themselves, not their partner, as controlling amaranth, and men may have overstated their role (pp. 6, 10).
   > - Older men generalists gave inconsistent rankings, which may reflect disagreement or uncertainty within the segment (p. 10).
   > - Fewer observations were recorded at the fourth harvest, and segment differences for fourth-harvest traits and overall performance were not significant (p. 8).
   > - Plot size and plant spacing were recommended but not enforced, and farmers used their own management (p. 4).
   > - Better varieties for producers must be paired with attention to consumer demand, policy, post-harvest handling and value chains (p. 11).

4. **Imprecise claim on women (Summary, paragraph 5).** Card: segments "show where improved amaranth varieties could expand economic opportunities, especially for women, who are central to vegetable production and trade in these countries." The source says improved varieties could expand opportunities, especially for women (p. 1), and cites literature that women are central to vegetable production and marketing in general (p. 2). But in this study men mainly controlled amaranth production and sales in Benin and Tanzania (Table 3, p. 6). Replace with:
   > The authors suggest that improved amaranth varieties that meet local needs could expand economic opportunities, especially for women. In this study, men mainly controlled amaranth production and sales in Benin and Tanzania, and women did so in Mali.

5. **Author order (frontmatter).** The card order differs from the byline (p. 1). Replace with:
   > authors: Voss RC, de Sousa K, N'Danikou S, Shango A, Aglinglo LA, Laporte MA, Legba EC, Houdegbe AC, Diarra DY, Dolo A, Sidibe A, Ouedraogo CO, Coulibaly H, Achigan-Dako EG, Kileo A, Malulu D, Matumbo Z, Dinssa F, van Heerwaarden J, van Etten J, Riar A, van Zonneveld M

6. **Add not_established.** Suggested:
   > not_established: that the segments come from the tricot rankings (they come from a cluster analysis of survey data, done independently of the rankings); that the segments or variety rankings hold in other countries or opportunity crops without new trials; that segments differ in overall performance or fourth-harvest rankings (not significant); that A2004 is best for every trait (it was assessed on marketability worth and regret); that women and men differ in preference in a simple gender split (the paper uses intersectional segments and contrasts with a study that found no gender difference)

7. **Methods in brief is thin.** Replace the three bullets with:
   > - **Trials.** tricot with a balanced incomplete block design: each farmer got three of 14 amaranth varieties (2 g seed each, coded A, B, C), from the WorldVeg genebank and breeding lines. Benin and Mali 2021 to 2022, Tanzania 2022. Data collected in ODK linked to ClimMob.
   > - **Evaluation.** Farmers ranked overall performance and traits (germination, vigor, plant survival, pest and disease tolerance, drought and flood tolerance, plant height, branching, yield, leaf size, marketability, taste) across four harvest periods. A baseline survey recorded household, land, market and institutional data.
   > - **Participants.** 2,063 farmers (794 Benin, 969 Mali, 300 Tanzania), 56.2% women.
   > - **Analysis.** Plackett-Luce models (PlackettLuce, ClimMobTools and gosset). Kendall tau with backward selection to keep the traits linked to overall preference. Principal component analysis of trait log-worths.
   > - **Segmentation.** Hierarchical cluster analysis (R package cluster) on seven survey variables, done independently of the rankings: gender, age, years growing amaranth, distance to market, gender controlling production, gender controlling sales, and income share from amaranth. ChatGPT helped draft segment descriptions, which the authors reviewed.
   > - **Validation and decision support.** Likelihood-ratio test (gosset) of whether segments rank varieties differently, and worth and minimum-regret analysis of marketability.

8. **Data and software fields.** The data availability statement (p. 11) gives a Zenodo DOI. Replace with:
   > data: survey template, data and code on Zenodo, https://doi.org/10.5281/zenodo.15204183
   > software: PlackettLuce, gosset, ClimMobTools, cluster (R packages)

9. **Notes.** The first note says the splits come from a table that extracts poorly. In fact the country splits are in the text (p. 3) and Table 2 (p. 5) extracts cleanly. All numbers are verified. The second note names "BOLD" and tricot-data, which are outside knowledge. The source names the BOLDER project (p. 11). Replace both notes with:
   > - Country and gender splits are verified against the text (p. 3) and Table 2 (p. 5). They add up to 2,063.
   > - Funding included the BOLDER project (Crop Trust) and 1000FARMS (Gates Foundation) (p. 11).
   > - Outside the source: the dataset may also appear in tricot-data. Check before linking.
   > - Source issue: Table 2 gives an overall average household size of 11, but the country values (16.7, 18.4, 3.9) give a weighted mean of about 15.6 (our calculation).

10. **Key numbers (optional additions).**
    > | 56.2% women | Share of participants, 33.1% in Benin, 83.1% in Mali, 30.3% in Tanzania | This paper |
    > | 0.2317 worth, 0.0011 regret | A2004 marketability, best on both measures, acceptable to all segments | This paper |
    > | 6 of 11 traits | Traits on which segments ranked varieties significantly differently (p < 0.05), all up to the third harvest | This paper |
    > | 34 to 45 years | Average age of segments (young men 34, young women 35, older women 43, older men 45) | This paper |

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Citizen science informs demand-driven breeding of opportunity crops | Same (p. 1) | Supported |
| authors | 22 names, order differs | 22 names, byline order (p. 1) | Imprecise (all names right, order wrong from position 5) |
| year | 2025 | 2025 (p. 1) | Supported |
| journal | Plants, People, Planet | Plants, People, Planet (p. 1) | Supported |
| article | published 2025, e70035 | PDF shows only "2025;1-14", no article number (p. 1) | Not checked (no web access). e70035 is consistent with the DOI suffix |
| type | research article | RESEARCH ARTICLE (p. 1) | Supported |
| doi | 10.1002/ppp3.70035 | Same (p. 1) | Supported |
| license | CC BY | Creative Commons Attribution License, version not stated (p. 1) | Supported |
| data | see the data availability statement | Zenodo 10.5281/zenodo.15204183 (p. 11) | Imprecise (give the DOI) |
| software | PlackettLuce, gosset | PlackettLuce, ClimMobTools, gosset, cluster (pp. 5, 6) | Imprecise (incomplete) |
| crops | leafy amaranth | Leafy amaranth (p. 1) | Supported |
| region | Benin, Mali, Tanzania | Same (p. 3) | Supported |
| gist | 14 varieties, 2,063 farmers, segments with distinct preferences | pp. 1, 8 | Supported (24 words). Could add the A2004 result |
| not_established | missing | | Metadata issue, see fix 6 |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Opportunity crops diversify food systems, few improved varieties, poor seed access | Supported | p. 1 summary | |
| 2 | Summary | Tests citizen science for demand-driven breeding and seed, amaranth case | Supported | p. 1 | |
| 3 | Summary | WorldVeg and partners, 14 varieties, 2,063 farmers, 794/969/300 | Supported | pp. 1, 3, Table 1 p. 4 | |
| 4 | Summary | Mtwara and Lindi, Tanzania, 2022 | Supported | p. 3 | Benin and Mali 2021 to 2022 not mentioned |
| 5 | Summary | Women the majority overall | Supported | 56.2%, Table 2 p. 5 | |
| 6 | Summary | Farmers ranked three varieties for overall performance and traits | Supported | p. 4 | |
| 7 | Summary | Household and farm data incl. household structure | Supported | pp. 4-5, Table 2 | |
| 8 | Summary | Preference driven by survival, yield, leaf size, taste, marketability | Supported | p. 6, Fig. 2 p. 7 | |
| 9 | Summary | Four named segments differing by gender, age, business orientation | Supported | p. 1, Table 4 p. 8 | |
| 10 | Summary | Single best variety would not serve all users | Contradicted | A2004 acceptable to all groups, p. 8, Table 6 p. 10 | Fix 1 |
| 11 | Summary | Segments give breeders and seed enterprises useful information | Supported | p. 1 | |
| 12 | Summary | Methods applicable to other opportunity crops | Supported | p. 1 | |
| 13 | Summary | Renewed attention amid food insecurity, poor nutrition, climate change | Supported | Societal Impact Statement p. 1 | |
| 14 | Summary | Traditional leafy vegetables in demand, raise incomes, improve diets | Supported | p. 2 | Cited literature |
| 15 | Summary | Weak seed systems, scarce improved varieties | Supported | p. 3 | |
| 16 | Summary | Variation points to context-specific breeding | Supported | p. 1 | |
| 17 | Summary | Segments "show where" varieties could expand opportunities for women | Imprecise | p. 1 says varieties could do so, not that segments show where | Fix 4 |
| 18 | Summary | Women central to vegetable production and trade "in these countries" | Imprecise | General literature p. 2. Men mainly control amaranth in Benin and Tanzania, Table 3 p. 6 | Fix 4 |
| 19 | Summary | Study as a model for participatory research on other crops | Supported | pp. 1, 11 | |
| 20 | Summary | tricot at scale extending beyond grain, legume and root crops | Not in source | | Outside knowledge, fix 2 |
| 21 | Summary | Countries with different languages, markets, farming systems | Not in source | p. 3 lists agroecological, socioeconomic, cultural contexts | Fix 2 |
| 22 | Summary | 1,159 of 2,063 women | Supported | Table 2 p. 5 | Repeats paragraph 2 |
| 23 | Methods | 14 varieties, three per farmer, three countries | Supported | p. 4 | |
| 24 | Methods | 2,063 farmers with gender and household data | Supported | Table 2 p. 5 | |
| 25 | Methods | PL models, Kendall correlations, cluster analysis | Supported | pp. 5-6 | Incomplete, fix 7 |
| 26 | Limitations | Segments may differ elsewhere | Not in source | | Fix 3 |
| 27 | Limitations | Seed supply constrains uptake | Not in source | Background only, p. 3 | Fix 3 |
| 28 | Key numbers | 14 varieties | Supported | Table 1 p. 4 | |
| 29 | Key numbers | 2,063 farmers | Supported | p. 1, Table 2 | |
| 30 | Key numbers | 794 / 969 / 300 | Supported | p. 3, Table 2 | Sum 2,063 checked |
| 31 | Key numbers | 904 men, 1,159 women | Supported | Table 2 p. 5 | 43.8% and 56.2% recomputed |
| 32 | Key numbers | 4 segments | Supported | Table 4 p. 8 | |
| 33 | Notes | Splits from a table that extracts poorly | Imprecise | Text p. 3 and Table 2 extract cleanly | Fix 9 |
| 34 | Notes | Relates to BOLD work and tricot-data | Imprecise | Source names BOLDER, p. 11. tricot-data is outside knowledge, not labelled | Fix 9 |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Overall average household size is 11, but the country values give a weighted mean of about 15.6 | Table 2, p. 5 | No | See fix 9 |
| Text says 10 traits were assessed, but the trait list has about 13 | pp. 4-5 | No | - Source issue: the text says 10 traits were assessed (p. 5), but the list on p. 4 names about 13. |
| Methods say Kendall tau correlation, the results text calls it "Kendall partial correlation" | pp. 5, 7 | No | Low importance, no note needed |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Worth and regret analysis: A2004 acceptable to all, Poli best second choice, AC-NL mainly for older men | No (contradicted) | High | Fix 2 |
| Likelihood-ratio test: segments differ on 6 of 11 traits, not at fourth harvest or overall | No | High | Fix 2, Key numbers |
| Aggregated preference for Akeri, Poli, AM-NKGN | No | High | Fix 2 |
| Authors' own limitations (gender balance, self-reporting, inconsistent older men, fewer fourth-harvest data) | No | High | Fix 3 |
| Segment-specific variety preferences (Fig. 4, p. 8) | No | High | Could add to Notes: older women preferred Akeri, Poli and AVAM1941, young women A2004, Akeri, AVAM1939, AM-NKGN and Poli, young men A2002 and A2004 |
| Segmentation done independently of the rankings, seven covariates, ChatGPT used for descriptions | No | Medium | Fix 7 |
| Contrast with a gender-disaggregated PVS in Tanzania that found similar preferences (Dinssa et al. 2022) | No | Medium | Add to Summary or Notes: "Unlike a gender-disaggregated variety selection study in Tanzania, this segment analysis found preferences that vary among women and among men (p. 10)." |
| Taste is a key driver but rarely a breeding priority | No | Medium | Add to Notes |
| Design details (2 g seed, plot sizes not enforced, four harvests, ODK and ClimMob) | No | Medium | Fix 7 |
| Zenodo data DOI | No | Medium | Fix 8 |
| Sample characteristics (84% sell amaranth, 58% of crop sold, 25% of income) | No | Low | Optional Key numbers |

## Template compliance

- Summary: 402 words (in range, near the lower limit). With fixes 1, 2 and 4 it will be about 460.
- Gist: 24 words (under 30). It says what the paper shows.
- Keywords: 11 (8 to 12).
- Questions: 4 (4 to 7). Optional fifth: "Which amaranth variety suits all farmer segments?"
- House style: tricot lowercase throughout. maniva not used.
