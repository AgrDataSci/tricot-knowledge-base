# Card review: donovan-2025-expagric

- **Card:** papers/donovan-2025-expagric.md
- **Source:** papers-pdf/donovan-et-al-2025.pdf (18 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 48 |
| Supported | 37 |
| Imprecise | 7 |
| Not in source | 4 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 8 |
| Important omissions | 7 |
| Metadata issues | 4 |

The card gets the main finding right (resilience, drought escape and intercropping are the top concepts) and all eight Key numbers rows check out. But the whole "Stated limitations" section is not from the source: the paper has no limitations section and never makes either statement. The card also has no not_established field, and it leaves out results a tricot user would ask about: the full ranking, the near 50/50 head-to-head results among the top three, the subgroup results, and the intercropping recommendation. The most important fix is to replace the Stated limitations with the authors' own open points (p. 14 and 15).

## Fixes needed

1. **Stated limitations are not in the source.** The card says "Stated preferences for concepts may differ from purchase behavior once seed is available" and "Concepts with mixed interest may reflect weak understanding of new uses rather than low value". The paper has no limitations section and makes neither statement. For mixed interest, the source draws a different conclusion: these concepts would need investment in production and promotion besides breeding (p. 1, 15). The reviewer cautions are reasonable, so move them to not_established (fix 2). Replace the section with:

   ```
   ## Stated limitations

   - The paper has no limitations section. The points below are the open questions the authors name.
   - The traits, and their thresholds, needed for the promising concepts are still to be identified by breeders, social scientists, food technologists and agronomists (p. 15).
   - Home use, family nutrition and food and fodder would have short-term impact only if product development were matched by investment in seed systems, such as retailer engagement, marketing and public purchasing (p. 15).
   - Designing an intercropping product will need a better understanding of what farmers expect from maize grown in intercrops (p. 14).
   ```

2. **not_established is missing.** Add to the frontmatter:

   ```
   not_established: that farmers would buy these hybrids once available (preferences were stated after watching videos and no seed was offered); that early-maturity or intercropping hybrids yield more or reduce risk in farmers' fields (no hybrids were bred or tested); that the results hold outside wet mid-altitude zones of western Kenya and central Uganda; that gender and farm size significantly shape concept preference (the printed p-values for these tree splits are above 0.05); which traits and thresholds each concept needs
   ```

3. **Summary misses key results and has four imprecise sentences.** Missing: no clear leader among the top three (Table 5, p. 10 and 13), the order of the other five concepts, with livestock feed last everywhere (Fig. 1, p. 11 and 12), subgroup results (p. 11), the intercropping recommendation (p. 13 and 14) and the conclusion on seed system investment (p. 15). Imprecise: "Context explained differences between countries" (the source never says context explains the preference differences), "Kenyan farmers consumed about half" (Table 4 gives 44% consumed and 37% sold), "were willing to trade some yield" (the source frames this as what the results suggest, p. 13), and "market segments" (a term from the brief, not this paper). Replace the whole Summary with this version (491 words):

   ```
   Public crop breeding has made major contributions to food security through step-change innovation in seed product design, but the literature gives little guidance on how to find forward-looking opportunities. Drawing on the product innovation literature, the authors apply product concept testing to hybrid maize in western Kenya and central Uganda. The aim is to test ideas for future seed products with farmers before breeding resources are committed.

   Interviews with seed companies, retailers and breeding institutes, and 12 focus groups of 6 to 9 farmers (separate groups for women and men), led to eight concepts: resilience (the benchmark, matching the current breeding target), drought escape, food and fodder, home use, green maize, livestock feed, intercropping with beans, and family nutrition (provitamin A). In each video, an actor playing an agrodealer presented one concept as a hypothetical seed product, in Luganda for Uganda and Swahili for Kenya. The design was inspired by tricot. Each of 2,400 farmers (1,200 per country, in wet mid-altitude zones) watched three randomly assigned concept videos and chose the most and least preferred.

   Across both countries, resilience, drought escape and intercropping were the top three, with no clear leader among them. Each won about half of its head-to-head comparisons with the other two. Home use came next, followed by food and fodder and family nutrition, then green maize. Livestock feed was the least preferred in both countries, for men and women. Preferences differed most by country. Drought escape led among Ugandan men, and intercropping led among Kenyan women with small farms.

   The two samples farmed in different ways. Over 90% of Kenyan farmers bought seed at least once a year, compared with under 50% in Uganda. More than 80% of Kenyan farmers intercropped, mainly with beans. Ugandan farmers sold 88% of their harvest, while Kenyan farmers mainly consumed and sold theirs.

   The strong result for resilience confirms the current CGIAR and NARES priority of incremental yield gains under adverse smallholder conditions. Drought escape and intercropping suggest new opportunities for product design. Public programmes have focused on intermediate-maturity, drought-tolerant hybrids for mid-altitude areas and test early-maturing hybrids only for dryland zones. The authors suggest that, for many mid-altitude farmers, the flexibility to plant later and the lower risk of late-season drought would make up for a lower yield. They recommend that public programmes and seed companies test early-maturity hybrids in higher-rainfall zones, and they cite two other studies that point the same way (Kogo et al. 2022, Rutsaert et al. 2023). For intercropping, they recommend testing pre-commercial hybrids under common smallholder practices, intercropping first among them.

   The authors conclude that home use, family nutrition and food and fodder could have short-term impact only if product development is matched by investment in seed systems, such as retailer engagement and marketing. The traits and thresholds for each promising concept are still to be defined. They present the results as new entry points for discussions among transdisciplinary teams at regional and national levels.
   ```

4. **Methods: design and analysis bullets are imprecise, and sampling is missing.** "Balanced incomplete design" is not in the source: concepts were "randomly selected" (p. 7). Farmers chose the most and least preferred concept (p. 7). The only covariates were gender, country and farm size, not wider "farmer and household covariates" (p. 8). Replace Methods in brief with:

   ```
   - **Concept development.** Key informant interviews with seed companies (n = 4), retailers (n = 6) and plant breeding institutes (n = 5), and 12 focus groups (6 per country) of 6 to 9 farmers, with separate groups for women and men.
   - **Presentation.** Professionally produced videos of 90 to 120 seconds, in which an actor playing an agrodealer presents a hypothetical seed product. 18 videos per country (Luganda, Swahili): a male-actor and a female-actor version of each of the 8 concepts, plus an introduction and a closing video.
   - **Sample.** 1,200 maize-farming households per country, chosen by multi-stage stratified sampling in Kakamega and Bungoma counties (Kenya) and Mubende and Mityana districts (Uganda), November 2021 to April 2022. The respondent's sex in each household was set in advance.
   - **Design.** Each farmer watched three of the eight concept videos, selected at random (an incomplete block design inspired by tricot), and chose the most and least preferred. A 30-minute household survey followed, recorded in ODK with FormShare.
   - **Analysis.** Plackett-Luce model with pairwise win probabilities, and Plackett-Luce trees with country, gender and farm size as covariates (R packages PlackettLuce, gosset, multcompView). Open responses analysed by text mining and correspondence analysis.
   ```

5. **data field.** The card says "see the data availability statement in the article". There is no such statement. The article gives a GitHub link for data and code (p. 9). Replace with:

   ```
   data: data and code for the ranking analysis and text mining at https://github.com/AgrDataSci/maize-concept-testing/ (stated on p. 9)
   ```

6. **license.** The source links to the CC BY 4.0 licence (p. 1). Replace with `license: CC BY 4.0`.

7. **Key numbers: add rows for the main results.** Suggested rows:

   ```
   | 1,200 per country | Farmers sampled in Kenya and in Uganda | This paper |
   | 49–52% | Head-to-head win probabilities among the top three concepts (resilience, drought escape, intercropping), so no clear leader (Table 5) | This paper |
   | 87–88% | Probability that each top-three concept beats livestock feed, the least preferred concept (Table 5) | This paper |
   | 1.7 vs 7.4 acres | Average farm size managed, Kenya vs Uganda (Table 4) | This paper |
   | 44% / 37% | Share of maize harvest consumed / sold in Kenya (Table 4) | This paper |
   ```

8. **Keywords and gist (optional).** "market segments" comes from the brief (rutsaert-2023-mib), not this paper, and "tricot" (one of the article's own keywords, p. 1) is missing. Suggested keywords: `product concept testing, VPCT, videos, hybrid maize, tricot, Plackett-Luce, product design, seed products, intercropping, drought escape, resilience, demand-led breeding` (12). The gist is correct but could carry the country split (25 words): `Video concept testing with 2,400 farmers in Kenya and Uganda ranked resilience, drought escape (Uganda) and intercropping (Kenya) highest among eight future maize hybrid concepts`

9. **Notes: add the source issues** listed below (suggested text in the Source issues table).

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | "...hybrids. Application of product concept testing in Kenya and Uganda" | Colon, lowercase "application" (p. 1) | Supported (colon to period, expected) |
| authors | Donovan J, Rutsaert P, Mawia H, de Sousa K, van Etten J | Same five, same order (p. 1, 18) | Supported |
| year | 2025 | 2025 (p. 1) | Supported |
| journal | Experimental Agriculture | Experimental Agriculture (p. 1) | Supported |
| article | 61, e5, 1-18 | vol. 61, e5, 1–18 (p. 1) | Supported |
| type | research article | "RESEARCH ARTICLE" (p. 1) | Supported |
| doi | 10.1017/S001447972500002X | Same (p. 1) | Supported |
| license | CC BY | Creative Commons Attribution licence, link to by/4.0 (p. 1) | Imprecise (should be CC BY 4.0) |
| data | see the data availability statement | No such statement. GitHub link for data and code (p. 9) | Not in source |
| software | PlackettLuce | PlackettLuce, gosset, multcompView, plus tidytext, tm, FactoMineR, factoextra (p. 8 and 9) | Supported (incomplete. Template asks for CRAN version format) |
| crops | maize (hybrids) | Hybrid maize (p. 1) | Supported |
| region | Kenya, Uganda | Western Kenya (Kakamega, Bungoma), central Uganda (Mubende, Mityana) (p. 8) | Supported (could be more specific) |
| gist | resilience, drought escape, intercropping most preferred of eight | Abstract (p. 1), Fig. 1 (p. 11) | Supported |
| not_established | missing | | Missing (see fix 2) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Public breeding gave major gains via step-change design, little guidance on forward-looking opportunities | Supported | Abstract (p. 1), p. 2 | |
| 2 | Summary | Product innovation literature, concept testing of hybrid maize before breeding investment | Supported | p. 1, 3 | |
| 3 | Summary | Eight concepts from interactions with seed companies, breeders, farmers, resilience is the current target | Supported | p. 1, 4, 5 (Table 2), 9, 13 | Retailers also interviewed (p. 4) |
| 4 | Summary | Videos in Luganda and Swahili, 18 per country | Supported | p. 7 | 18 = 8 concepts x 2 actors + intro + closing |
| 5 | Summary | Following tricot logic, 2,400 farmers each watched three videos and ranked them | Supported | p. 1, 7 | Farmers chose most and least preferred (a full rank of three) |
| 6 | Summary | Focus groups of 6 to 9 farmers, separated by sex | Supported | p. 4 | 6 groups per country |
| 7 | Summary | Resilience (both), drought escape (Uganda), intercropping (Kenya) most likely chosen | Supported | Abstract (p. 1), p. 15 | |
| 8 | Summary | Mixed interest in home use, food and fodder, needs promotion and seed production besides breeding | Supported | Abstract (p. 1) | |
| 9 | Summary | "Context explained differences between countries" | Not in source | p. 9 describes context, does not link it causally to preferences | p. 11 notes home use ranked similarly in both countries despite very different consumption, which cuts against this |
| 10 | Summary | >90% Kenya vs <50% Uganda buy seed at least yearly | Supported | p. 9, Table 4 (p. 10) | Recomputed: 97.6% vs 49.0% |
| 11 | Summary | >80% Kenyan farmers intercropped, mainly with beans | Supported | p. 9, 13 | Recomputed from Table 4: 84.3% |
| 12 | Summary | Uganda sold 88%, Kenya consumed about half | Imprecise | p. 9, 11, Table 4 (p. 10) | 88.43% sold is right. "About half" matches p. 11 text but Table 4 gives 44% consumed, 37% sold, and p. 9 says "consumption and sales" |
| 13 | Summary | Concept testing as entry point for transdisciplinary discussions on breeding priorities and market segments | Imprecise | Abstract (p. 1) | Source says the results give entry points on opportunities for breeding. "Market segments" is not in this paper |
| 14 | Summary | Resilience result confirms CGIAR and NARES priority | Supported | p. 13 | |
| 15 | Summary | Drought escape and intercropping point to new opportunities | Supported | p. 13 | Source: "suggest that new opportunities exist" |
| 16 | Summary | Public breeding focused on intermediate-maturity drought-tolerant hybrids, early hybrids only for drylands | Supported | p. 13, also p. 5 | |
| 17 | Summary | Many mid-altitude farmers "were willing to trade some yield" for early maturity | Imprecise | p. 13 | Source frames it as what the results suggest. Willingness to trade yield was not measured directly |
| 18 | Summary | Recommend testing early-maturity hybrids in higher-rainfall zones | Supported | p. 13 | |
| 19 | Summary | Other evidence: western Kenya adaptation, agrodealer sales data | Imprecise | p. 13 | Content right, but these are cited studies (Kogo et al. 2022, Rutsaert et al. 2023) and should be named as such |
| 20 | Summary | Concept testing tests ideas before breeding invests | Supported | p. 3 | |
| 21 | Methods | Concept development with seed companies, breeders, farmers, FGDs of 6 to 9 | Supported | p. 4 | Omits retailers and the n of each group |
| 22 | Methods | Videos in local languages, 18 per country | Supported | p. 7 | |
| 23 | Methods | Three concepts in a "balanced incomplete design" and ranked | Imprecise | p. 7 | Source says "randomly selected". Balance is not stated |
| 24 | Methods | Plackett-Luce with "farmer and household covariates" | Imprecise | p. 8 | Only gender, country and farm size. Pairwise probabilities and text mining not mentioned |
| 25 | Limitations | Stated preferences may differ from purchase behaviour | Not in source | No limitations section | Valid caution, belongs in not_established |
| 26 | Limitations | Mixed interest may reflect weak understanding of new uses | Not in source | p. 1, 15 give a different reading | Source links mixed interest to the need for seed system investment |
| 27 | Key numbers | 8 concepts | Supported | p. 1, Table 2 (p. 5) | |
| 28 | Key numbers | 2,400 farmers, three videos each | Supported | p. 1, 7 | |
| 29 | Key numbers | 18 videos per country, Luganda and Swahili | Supported | p. 7 | |
| 30 | Key numbers | 6–9 farmers per focus group, separate for women and men | Supported | p. 4 | |
| 31 | Key numbers | >90% vs <50% buy seed yearly | Supported | p. 9, Table 4 | |
| 32 | Key numbers | >80% Kenyan farmers intercrop | Supported | p. 9, 13 | |
| 33 | Key numbers | 88% of harvest sold in Uganda | Supported | p. 9, Table 4 (88.43%) | |
| 34 | Key numbers | 37% / 27% secondary or post-secondary education | Supported | p. 9 | Table 3 gives 37.75% and 27.17%. The text's 37% is truncated, not rounded (see Source issues) |
| 35 | Notes | Brief lists seven new concepts plus benchmark with different labels | Supported | Brief p. 1 (rutsaert-et-al-2023.pdf) | Checked: "drought avoidance", "nutritious", "feed (yellow)" |

The 13 metadata fields in the table above complete the 48 claims.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Text says country, gender and land size significantly influenced concept choice, but the printed split p-values in the tree are 0.89 (gender, Kenya), 0.34 (farm size) and 0.30 (gender, Uganda). Only the country split (p = 3.4e-13) is below 0.05 | p. 11 text vs Fig. 3 (p. 14) | No | The text (p. 11) says gender and land size significantly influenced concept choice, but the p-values printed in Fig. 3 for these splits are 0.89, 0.34 and 0.30. Only the country split is clearly significant (p = 3.4e-13). Treat subgroup results as indicative. |
| Fig. 3 node sizes give 607 Kenyan women (305 + 302) and 593 Kenyan men. Table 3 gives 607 men and 593 women | Fig. 3 (p. 14) vs Table 3 (p. 10) | No | Fig. 3 and Table 3 swap the numbers of Kenyan men and women (607 and 593). |
| Kenya harvest use by sex does not add up. The male column sums to 72.6%, and a total of 44.16% consumed cannot come from 33.91% (men) and 22.40% (women) | Table 4 (p. 10) | No | Table 4 figures for Kenyan harvest use by sex are internally inconsistent (the male column sums to 73%). Use the totals with care. |
| Kenyan consumption described as "approximately half" (p. 11) and as consumption and sales (p. 9), while Table 4 gives 44% consumed and 37% sold | p. 9, 11, Table 4 | No (card repeats "about half") | Kenyan farmers consumed 44% and sold 37% of their maize harvest (Table 4). The text (p. 11) rounds consumption to about half. |
| Text gives 37% of Kenyans with secondary or post-secondary schooling, Table 3 sums to 37.75% (about 38%) | p. 9 vs Table 3 (p. 10) | No | Optional: Table 3 gives 37.75% for Kenya (about 38%). |
| Uganda total area managed: total SD (5.80) is smaller than both the male (6.29) and female (8.18) SDs, which is not possible. Recomputed pooled SD is about 7.4 | Table 4 (p. 10) | No | Low importance for the card. No Notes text needed. |
| Text says drought escape clearly outperformed all other concepts in Uganda, but for Ugandan women drought escape and resilience share letter "a" | p. 13 vs Fig. 3 (p. 14) | No | Low importance. The card wording "drought escape in Uganda" is fine. |
| Table 5 caption uses "drought avoidance" while the table row is "Drought escape" | p. 13 | Partly (Notes mention label differences with the brief) | Low importance. |

Values I read from Fig. 1 and Fig. 3 are approximate. Fig. 1 log-worths read as roughly 0 for resilience, drought escape and intercropping, about -0.3 for home use, about -0.6 for food and fodder and family nutrition, about -1.1 for green maize and about -1.9 for livestock feed. A log-worth gap of 1.9 gives a win probability of 0.87, which matches Table 5. Table 5 is internally consistent: every pair of complementary cells sums to 100%.

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: find forward-looking product opportunities before breeding investment | Yes | high | |
| Design: 8 concepts, videos, 3 random concepts per farmer, most and least preferred | Partly (method "balanced", choice task not described) | high | Fix 4 |
| Sample: 1,200 per country, multi-stage stratified, counties and districts, Nov 2021 to Apr 2022, respondent sex set in advance | No | medium | Fix 4 (Sample bullet), Key numbers row |
| Top three with no clear leader (49–52% head-to-head) | No | high | Fix 3 and fix 7 |
| Full ranking: home use, then food and fodder and family nutrition, then green maize, livestock feed last | No | medium | Fix 3 |
| Subgroup results (Ugandan men favour drought escape, Kenyan women with ≤0.9 acre favour intercropping) | No | medium | Fix 3, with the p-value caveat in Notes |
| Intercropping recommendation: test pre-commercial hybrids under intercropping, possible selection for intercrop performance | No | high (core tricot and breeding message) | Fix 3 |
| Conclusion: home use, nutrition, food and fodder need seed system investment for short-term impact | Partly (abstract version only) | medium | Fix 3 |
| Authors' open points (traits and thresholds still to define) | No (replaced by invented limitations) | high | Fix 1 |
| Reasons from text mining (drought escape linked to "fast", "shorter", livestock feed rejected for its narrow use, not yellow colour) | No | low | Optional in Notes |
| Video details (agrodealer narrative, male and female actor, 90 to 120 s) | No | low | Fix 4 |
| Data and code on GitHub | No (wrong pointer) | medium | Fix 5 |

## Template compliance

- Summary word count: 406 (within 400 to 500). The suggested replacement is 491.
- Gist: 25 words (under 30). Says what the paper shows.
- Keywords: 11 (within 8 to 12). "market segments" is not a term from this paper, and "tricot" is missing.
- Questions: 4 (within 4 to 7).
- House style: "tricot" is lowercase throughout. maniva does not appear. No em dashes found. The card uses en dashes in "6–9" and "37% / 27%", which is fine.
- not_established: missing (fix 2).
- relations: `extends: rutsaert-2023-mib` is reasonable. The brief card itself calls this paper the full analysis.
