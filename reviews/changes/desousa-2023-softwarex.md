# Change log: desousa-2023-softwarex

The example and impact text is corrected (no validation was run in the example), the Kendall's tau and reliability results are added, the invented limitations are replaced, and gist, data, license, not_established, relations, key numbers and notes are updated.

## Applied

1. Fix 1 (Contradicted, claim 34): the model validation claim now refers to the cited studies, and the Summary says cross-validation, btpermute and regret are only next steps. Confirmed on p. 4 ("Next steps") and p. 5 ("In these studies"). Also confirmed by hand by the person.
2. Fix 2 (omission): Kendall's tau 0.749, 0.653, 0.639 and the lighter tricot design with no more than four traits added to the Summary. Table 1 and text, p. 3.
3. Fix 3 (claim 27): the single variety ALS 0532-6, the 193.82 mm split, p = 0.079 and alpha = 0.1. Text p. 4, code p. 4, Fig. 2 p. 5 (p = 7.9e-02).
4. Fix 4 (claim 28): compare() shows no full agreement, with the hedged explanation for SX 14825-7-1 including disease resistance. p. 4, Fig. 3 p. 5.
5. Fix 5 (claims 45, 46): Stated limitations replaced. No limitations section in the paper. "For simplicity" (rainfall only, reliability ≥ 0.5) on p. 3 to 4. Next steps on p. 4.
6. Fix 6: not_established added as given. Each item is consistent with p. 4 to 5 (alpha 0.1, p = 0.079, next steps, no benchmark).
7. Fix 7 (claim 12): gist replaced (26 words). Abstract, p. 1.
8. Fix 8 (claim 36): ecosystem "built around ClimMob", more than 10,000 farms per year, breeding teams in Sub-Saharan Africa. ClimMobTools removed (not in the paper). p. 5.
9. Fix 9 (claim 32): 1000FARMS direction corrected, and the community of practice is "in on-farm experimentation". p. 5.
10. Fix 10 (claim 15): Student's t-test removed. Pen name 'Student', Guinness, barley varieties. p. 2.
11. Fix 11 (claims 14, 16): scope and the three packages on equal terms, "researchers working on agricultural experiments". Abstract, p. 1 to 2.
12. Fix 12 (claim 26): one Plackett-Luce tree for yield, total rainfall over 45 days. p. 3 to 4.
13. Fix 13 (claims 38, 39): tutorial paragraph reduced to "from ranked data to reliability estimates". The CRAN advice stays only in Notes. Data pre-converted with rank_tricot, p. 3.
14. Claim 37: "keeps the toolkit aligned" replaced with "The authors expect ... to drive improvements". p. 5.
15. Fix 14: data field now names nicabean, code repository, v1.0, MIT licence and documentation site. Code metadata, p. 1, and p. 3.
16. Fix 14 optional: license changed to "CC BY 4.0", the URL printed on p. 1.
17. Fix 15: replacement Summary used, with fixes 1 to 4 and 8 to 13 combined. The fix 2 sentence on a lighter tricot design was added and a few phrases shortened to stay within 500 words.
18. Fix 16: Example bullet in Methods replaced, and node_labels, node_rules and top_items added to the Interpretation bullet. p. 2 to 4.
19. Fix 17: seven Key numbers rows added. Table 1 p. 3, Table 2 p. 4, Fig. 2 p. 5 (n = 393 and n = 164), p. 2 (five seasons, 2015 to 2016), p. 5 (10,000 farms). Table 2 reliabilities rechecked from worth (for example 0.123 / (0.123 + 0.114) = 0.519).
20. Fix 18 Notes: code version 1.0 merged into the existing CRAN note, the weak rainfall split flagged as a source issue, the Table 2 check, and the climatrends citation year ([25], p. 6).
21. Source issues 2 and 3 added to Notes as short lines: naming varies ("overall performance" vs "overall appreciation", "Amadeus" vs "Amadeus 77", p. 3), and the wrong journal for reference [23] (p. 6).
22. Fix 18 relations: usesMethodIn turner-2020-compstat (PlackettLuce [12], used throughout the example) and discusses for vanetten-2019-pnas [4], moyo-2021-fsufs [5], desousa-2021-commsbio [35], brown-2022-cropsci [7], alamu-2023-jsfa [6], gesesse-2023-pnas [31], woldeyohannes-2022-elife [32] and rutsaert-2023-mib [33], p. 4 to 6. All target cards exist. The existing usesMethodIn eskridge-1992-tag is kept ([24], p. 2).
23. Template check: a fifth question on trait prioritisation was added, and the keyword "Kendall tau" was added (now 12), to match the new Kendall's tau content.

## Skipped

- None of the review's suggestions were rejected. The review marked source issues 2 and 3 "Not needed", but the fixer instructions ask for every source issue to be flagged, so they were added (item 21).
- The question on regret (question 3) was kept. The function descriptions answer it, and the Summary and limitations now say the example does not run regret.

## Final counts

- Summary words: 500 (wc), 499 counting only tokens with letters or digits
- Gist words: 26
- Keywords: 12
- Questions: 5
