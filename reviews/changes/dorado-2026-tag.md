# Change log: dorado-2026-tag

Rewrote the Summary to add simulation results, Plackett-Luce scaling, replication cost and the observed-data results. Fixed overstated claims. Expanded Methods, Limitations and Key numbers. Added not_established and source-issue Notes. Fixed region, gist, keywords, software, data and Questions.

## Applied

1. Fix 1 (Summary replaced with the review's text). This also covers claims 2, 13, 17, 18 and 19. Confirmed on p. 1 ("remain limited"), p. 5 to 6, p. 7 (Table 1, 18480 trials), p. 8 (bias, 0.85 to 0.90), p. 9 (30% more replicates), p. 10 (17–19% twice, <0.25, >100), p. 12 to 13 (Table 3), p. 14 to 16. One wording change: "both models put genotypes in the same order" became "after rescaling both models performed almost the same" (p. 10, Fig. 5 insight 4). The source does not say the order was identical in so many words.
2. Fix 2: not_established added. Confirmed p. 8, p. 13 (Table 3), p. 14 to 16 (only yield, future work, "complementary or, in some cases, unnecessary").
3. Fix 3: Stated limitations replaced. Confirmed p. 10, p. 14 to 16 (two limitations, caveat on extreme genotypes, future work list, quasi-variances vs C-NMA), p. 16 (maize data).
4. Fix 4: Key numbers. Split the 17%–19% row, added the 18,480, ~30%, 0.85–0.90, 0.961–0.997, 0.229 vs 0.359 and 0.407 vs 0.001 rows, and added the unit to the >100 row. Confirmed p. 7, p. 8, p. 9, p. 10, p. 13 (Table 3).
5. Fix 5: Methods in brief replaced. Confirmed p. 5 to 8 (check variety reference, qvcalc weights, REML, ASReml, Table 1, Table 2 genotypes and replicates, who measured yield, Zenodo). This also fixes claim 23 (four datasets, no outside "tricot-data" label in Methods).
6. Fix 6: gist replaced (28 words). Confirmed p. 1, p. 13 to 14.
7. Fix 7: region set to Kenya, Mozambique, Tanzania (sub-Saharan Africa). Confirmed Table 2, p. 9.
8. Fix 8: "genetic gain" replaced with "quasi-variances", and "on-farm trials" added. Genetic gain is future work only (p. 16).
9. Fix 9: software field expanded with the CRAN URL and the other packages (gosset, ClimMobTools, ASReml, custom code). Confirmed p. 8.
10. Fix 10 and claims 34 to 36: the preprint and tricot-data Notes are now labelled as outside the source. The preprint line no longer claims the numbers match. Added Notes for three source issues (17–19% range p. 10, code DOI p. 16 vs p. 17, scaling factor p. 8 vs p. 14).
11. Source issues table, rows 4 and 5: added Notes lines for the technicians vs farmers wording (p. 8, p. 15) and the Eq. (3) change of variables (p. 4). Instruction 4 asks for every source issue the card did not flag.
12. Fix 11: two questions added (6 in total).
13. Fix 12: supplementary information archive added to data (p. 16).

## Skipped

- Fix 9, version part: the CRAN version and dates were not filled in, because web access was not allowed for this task. The field says "CRAN version not checked" for the curator to complete.
- Optional Notes lines from the Completeness table (non-constant standard errors, 3 replicates insufficient, broad-sense heritability choice): not added. They are optional, and the Summary and Limitations already cover the main points.
- The data field still calls the Zenodo dataset "tricot-data". The review marked the data field Supported and did not ask for a change. The Notes now label that name as coming from outside the source.

## Final counts

- Summary words: 493
- Gist words: 28
- Keywords: 11
- Questions: 6
