# Change log: brown-2022-cropsci

Corrected the EAP 9508-93, warm-node genotype, Apante c index, plots, 27 to 17 and covariate errors, fixed authors and data, added not_established, relation, limitations, key numbers and source-issue notes, and adopted the review's replacement Summary.

## Applied

1. Fix 1, claim 27: EAP 9508-93 is predicted in the top three in much of Costa Rica though tested only in Honduras. It is a candidate for trials, not a direct recommendation (p. 2262, PDF 17, Figure 4a also checked by hand).
2. Fix 2 and fix 8, claims 19 and 21: single WSDI split at > 4 days. Warm-node top three are IBC 308-24, MHC 2-13-49 and SX 14825-7-1. BRT 103-182 goes from good to poor (p. 2256, PDF 11, Figure 3 on p. 2257, PDF 12, checked on the page image).
3. Fix 3, claims 24 and 49: c index 0.563 Postrera, 0.625 Apante (p. 2257, PDF 12, also confirmed by hand). Summary and Key numbers.
4. Fix 4, claims 35 and 47: 14 to 714 plots per trial, 1,871 in total. Sum checked against Table 1 (p. 2249, PDF 4) and Figure 3 node sizes 1,264 + 607. Only the overall ranking analyzed (p. 2248, PDF 3).
5. Fix 5, claims 16, 36 and 46: 27 to 17 came from removing single-trial genotypes after names were translated (p. 2248, PDF 3).
6. Fix 6, claim 18: covariates WSDI, R20mm (very heavy rain), T10p, hts_mean_19_flo (high-temperature stress at flowering) (p. 2256, Tables 3 and 4 on p. 2251).
7. Fix 7, claim 17: removed elevation, covariates are climate and soil (Tables 3 to 5, p. 2251 to 2252).
8. Fix 9, claims 22 and 38: final Cox covariates DAP (Primera), DP and DSRF (Postrera), DP (Apante), start dates 1 April, 1 August, 1 October (Table 8 p. 2257, text p. 2254).
9. Fix 10, claim 26: dropped the all-season SRC 2-18-1 statement, replaced by the lowest-entropy rankings across seasons (p. 2258, PDF 13).
10. Fix 11, claim 42: limitation reworded to higher entropy and candidates for trials (p. 2258 and p. 2262).
11. Fix 12: three new limitations, single-tree instability and forests (p. 2253), ad hoc planting-date models (p. 2258), no factor beyond heat found (p. 2256).
12. Fix 13, claims 31 to 33: ClimMob helped but curation still needed (p. 2248), naming is "a challenge", coordinated regional releases and a harmonized-name database (p. 2262).
13. Fix 14, claim 14: removed "yield data", now different scales or designs (p. 2247).
14. Fix 15, claim 2: full 18-author list in PDF order (p. 2246). Deleted the Notes line about the long author list.
15. Fix 16, claim 9: data field gives the GitHub repository (p. 2263, PDF 18).
16. Fix 17: added not_established as suggested. Each item checked against Table 7 (small gains), p. 2256 (no other factor), p. 2262 (one-country genotypes), p. 2257 (weak models), p. 2258 (AOA), p. 2248 (overall ranking only).
17. Fix 18: added Key numbers rows for the WSDI split, Table 7 deviance (p. 2256), r = 0.09 (p. 2256), 2000 to 2019 and 11 km grid (p. 2255), 10 of 14 trials (p. 2258), and reworded the ~0.5% row as a rate (Table 8).
18. Fix 19: replaced the first note with the vanetten-2019-pnas comparison and r = 0.09 (p. 2256). Added `extends: vanetten-2019-pnas` (target card exists).
19. Source issues 1 to 3 added to Notes: Apante proportional hazard p = .013 (Table 9, p. 2258, with the rule that a nonsignificant p passes, p. 2254), hazard ratio vs probability (p. 2256), WSDI defined two ways (Table 3 p. 2251, text p. 2256).
20. Medium omission: Notes line on areas outside the area of applicability (p. 2258, PDF 13).
21. Optional sixth question added, as suggested in Template compliance.
22. Summary replaced with the review's suggested replacement Summary. Every sentence checked against the pages above.

## Skipped

- Source issues 4 and 5 (Table 3 units for SU and TR, HND_10_2017 date vs ID): low importance, and the review suggests no Notes text.
- Low-importance omissions (Apante MHC 2-13-49 detail, future steps and gosset, data cleaning rules, first Cox application claim): low importance, and Notes already long.
- Software field CRAN links and versions: optional field, not part of the review's fixes, and would need a web check that this task does not allow.

## Final counts

- Summary: 497 words
- Gist: 26 words
- Keywords: 11
- Questions: 6
