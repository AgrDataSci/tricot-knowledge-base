# Change log: turner-2020-compstat

Removed outside tricot framing and agronomist claim, corrected benchmarks, bean tree, shrinkage, quasi SEs and tie probability, replaced Stated limitations with the authors' own, added key numbers, source-issue notes, not_established, data, gist and article volume and pages (labelled as from the repository record).

All pages are PDF pages (online-first PDF, no printed page numbers). Each change was checked in /home/claude/work/txt/turner-et-al-2020.txt and with per-page pdftotext.

## Applied

1. Fix 1 / claim 17: removed "standard analysis engine for tricot data ... grew out of tricot needs" sentence. Replaced with the authors' two costs and the tie order 4 limit (p. 24, "feature-rich package for the analysis of ranking data"; tricot appears only in a reference title, p. 31). Added a Notes line labelled "Outside this paper" for the tricot link.
2. Fix 2 / claim 15: benchmark paragraph rewritten. PLMIX faster on T-shirt and sushi, mixedMem comparable, NASCAR 0.199 s vs 36.123 s with 83 drivers (Table 1 p. 6, text p. 5, Table 3 p. 7).
3. Fix 3 / claims 12, 14: covariates now season, year, night temperature (no "location"). Tree split at 18.7, node winners as printed (p. 22 to 23). "Heat-tolerant" removed.
4. Fix 4 / claims 20, 21: deleted "eases adoption by agronomists" sentence and the repeated weights/aggregation sentence (not in source, p. 1, p. 14).
5. Fix 5 / claim 18: added the condition "first place is not a tie of three or more" (p. 11).
6. Fix 6 / claims 8, 28: shrinkage now towards equal worth, weak with many rankings, reduces bias and variance (p. 19). Removed the shrinkage bullet from Stated limitations. Added npseudo = 0.5 note to Notes.
7. Fix 7 / claim 27: Stated limitations replaced with the five bullets (p. 23, p. 24 to 25, Table 4 p. 8, p. 8).
8. Fix 8 / claim 3: tricot link now attributed to the paper's bean example (p. 22).
9. Fix 9 / claim 9: quasi standard errors give approximately correct comparisons (p. 15).
10. Fix 10 / claim 25: Methods Covariates bullet. partykit removed, psychotree Bradley-Terry trees, minsize 5% and maxdepth 3 (p. 21, p. 22).
11. Fix 11 / claim 35: sushi row attributed to PrefLib with 4,926 unique (Table 2 p. 6). Added rows for NASCAR timings (p. 7), 842 records marked as card's sum of 47 + 489 + 306 (p. 23), 18.7 split (p. 22 to 23), npseudo 0.5 (p. 19), 18.1 s and 14.8 s (p. 24).
12. Fix 12 / metadata: data field rewritten (p. 11, 19, 22, 25). gist replaced with the review's 25-word version. not_established added (supported by Table 1 p. 6, Table 4 p. 8, p. 22 to 25).
13. Article field: set to "35, 1027-1057" labelled in the field and in Notes as from the University of Warwick repository record, not checked against the PDF (per caller instruction).
14. Template compliance: first question replaced with "What does the Plackett-Luce model assume, and what does PlackettLuce add to it?". Added a question on practical limits, answered by p. 24.
15. Source issues: added four "Problem in the source" lines to Notes. NASCAR 83 vs 87 drivers (p. 7, p. 19), INTA Centro Sur vs BRT 103-182 order (p. 23), no unit for maxTN (p. 22 to 23), wrong internal cross-references (p. 7, p. 13).

## Skipped

- Optional low-importance omissions (worths sum to one, Z tests against reference, iterative scaling default with Steffensen, future work, connectivity check, pudding no significant differences): Summary is at 498 words, and the review marks these optional.
- No new relations added: the review proposed none.

## Final counts

- Summary words: 498
- Gist words: 25
- Keywords: 10
- Questions: 6
- Frontmatter parses as YAML. No em dashes. No semicolons outside not_established.
