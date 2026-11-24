# Change log: desousa-2021-commsbio

Applied all 17 review fixes and the imprecise and unsupported claims: Oromia added to region, on-farm yield now described as measured, model results now described as predictions, limitations replaced with the authors' own, not_established added, Key numbers extended and six source issues added to Notes. Summary trimmed to stay at 499 words.

## Applied

1. Fix 1, region now lists Amhara, Oromia and Tigray (p. 6: 471 / 399 / 295 farms).
2. Fix 2, claim 5: farmers ranked overall appreciation, technicians measured grain yield. Added 38 landraces + 3 cultivars, three regions, 2013 to 2015 (p. 6).
3. Fix 3, claim 10: Plackett-Luce trees, SNP data as prior, prediction in untested seasons and environments (p. 4, p. 7).
4. Fix 4: not_established added, using the review text (Table 1 p. 3, p. 2, p. 4, p. 5, p. 7).
5. Fix 5, claims 29 and 30: Stated limitations replaced with seven points taken from the authors' text (p. 1, p. 4, p. 5, p. 6, p. 7). Page references left out to match the card style.
6. Fix 6: gist rewritten, 26 words ("could double", p. 1. Table 1, p. 3).
7. Fix 7, claim 9: gender heritability 0.84 vs 0.67, consistent evaluations (p. 2).
8. Fix 8, claim 12: two covariates selected out of 110 (p. 7), 11.5 °C threshold (Fig. 2 caption, p. 5). Shortened wording.
9. Fix 9, claim 13: written as model predictions, 15 simulated seasons (p. 4, Fig. 2, p. 5). Shortened "varieties currently recommended for the mega-environment" to "recommended varieties" to stay within the word limit.
10. Fix 10, claim 15: "could potentially benefit", "challenging, low-input" (p. 2).
11. Fix 11, claim 4: "landraces and improved lines" (p. 6). Station years and the 2012-only scoring added to the Summary. Station names and the 15 + 15 split went in Methods only, for word count (p. 6).
12. Fix 12, claim 18: "rather than treating it as noise" removed (p. 6).
13. Fix 13: robustness sentence for 5% to 75% subsets added to Summary and Key numbers (p. 4).
14. Fix 14: data field now names SNP calls, provenance, trial data and code (p. 7, ref. 56 p. 8).
15. Fix 15: ~500 million sourced to Lowder et al. 2016 (ref. 7, p. 8). ~20% context relabelled (p. 4, Fig. 2c p. 5). Added Key numbers rows for farms by region and season, plot size, heritability, robustness tau, 110 covariates and 11.5 °C (p. 2, p. 4, p. 5, p. 6, p. 7).
16. Fix 16: Methods rewritten with Centralized, Decentralized, Benchmark and 3D-breeding model bullets. Genomics and Reliability bullets kept (p. 6, p. 7).
17. Fix 17 and source issues: added six "Problem in the source" lines to Notes. Table 1 weighting was recomputed and confirmed (benchmark 0.141 / 0.046 = simple means, 3D 0.251 = weighted, 0.109 close to weighted 0.110). The Dataverse title (ref. 56, p. 8), the Table 1 citation for appreciation vs yield (p. 4), Fig. 2c n = 1,165 vs 1,200 points (p. 5, p. 7), the "training dataset" label (p. 7) and the "3DD" legend (Fig. 2a image, p. 5) were all confirmed. The review called the last two low priority, but the instructions ask to add every source issue.
18. Relations (template compliance, optional): `extends: mancini-2017-scirep` changed to `usesDataFrom: mancini-2017-scirep` with a comment. The 41 genotypes were identified through the farmer evaluations of ref. 21, Mancini et al. 2017 (p. 6). The target card exists.

## Skipped

- Medium omission "Farms were colder than stations, the benchmark did better for cold-tolerant genotypes" (p. 3). Confirmed and added at first, then removed to keep the Summary under 500 words.
- Optional low-importance items: the station-to-station tau of 0.248, the Pearson vs Kendall note and the accuracy ratio row. Left out for length and because they are low priority.
- Software field CRAN URLs and versions (template compliance, low priority). Checking current CRAN versions needs web access, which was not allowed.
- Note on wording, not a skipped suggestion: paragraph 6 was shortened to meet the word limit. "as in livestock genetics" was dropped and the methods sentence was compressed. The meaning is unchanged, and the dairy parallel stays in paragraph 5.

## Final counts

- Summary words: 499
- Gist words: 26
- Keywords: 10
- Questions: 5
