# Change log: nanyonjo-2024-cropsci

Summary: Applied all 16 review fixes after checking them against the source. The card now adds the yield and tree-stability results, corrects the cycle link (the check only), rewrites limitations, the district note, the gist and the metadata, and flags six source issues.

## Applied

1. Fix 1 (yield omission): Summary sentence "No clone beat the check..." and Key numbers row "< 0.5". Confirmed p. 2690 to 2691 (PDF 12 to 13), p. 2693 (PDF 15), Figure 7 p. 2692 (PDF 14). All yield-column values are below 0.5, including the three release candidates.
2. Fix 2 (stability omission): Summary sentences on 530 of 1,000, almost 90% and the single check. Key numbers rows "530 of 1,000" and "~90% / ~55%". Confirmed p. 2688 (PDF 10, Figure 4) and p. 2689 (PDF 11). Matches the hand check (530 of 1,000, p. 2688).
3. Fix 3 / claim 34 (shared clones, Contradicted): replaced Stated limitations with four bullets. Confirmed p. 2681 (PDF 3), Table 2 p. 2683, p. 2688, p. 2685 (PDF 7), p. 2693 (PDF 15).
4. Fix 4 / claim 48 (district Note, Contradicted): replaced with the 6 + 4 new = 10 explanation. Confirmed p. 2681 (PDF 3), Table 1 and Figure 1 caption p. 2682 (PDF 4).
5. Fix 5 / claim 60 (gist): replaced, now 29 words. Confirmed separate trees p. 2686 (PDF 8), yield result p. 2693.
6. Fix 6 / claim 28 (Not in source): removed "recommendations should follow rainfall patterns" and added UG130007 as a parent for crosses plus genome-wide association studies. Confirmed p. 2692 (PDF 14).
7. Fix 7 / claims 1, 29 (clone origin): Summary and Methods now say four clones came from IITA and give the 11 + 9 split. Key numbers row "11 + 9". Confirmed p. 2681 (PDF 3), Table 2 p. 2683 (PDF 5).
8. Fix 8 / claim 14: "In one district node..." Confirmed p. 2687 (PDF 9), Figure 3 p. 2688.
9. Fix 9 / claim 9: two trees named, sex and age not selected. Confirmed pp. 2686 to 2688, Table 4 (30 variables, counted), Figure 3 caption.
10. Fix 10 / claims 8, 37: "after cleaning" replaced with losses to drought, hailstorms and poor management in Summary and Key numbers. Confirmed p. 2685 (PDF 7).
11. Fix 11 / claims 20, 21: conclusion now says end-users make an important contribution, and NAROCASS 1 or other clones from this study can keep the network connected. Confirmed p. 2679 (PDF 1), p. 2693 (PDF 15).
12. Fix 12 / claim 33: gender-location bullet removed from limitations. The authors' own point (needs further study) is in the new limitations. Confirmed p. 2691, p. 2693.
13. Fix 13 / claim 46: authorship Note now says the PDF states shared first authorship of Nanyonjo, Angudubo and Iragaba. Kawuki called last author. Confirmed p. 2679 (PDF 1).
14. Fix 14 / claim 23: "strongly shaped by the growing environment" removed. Summary now says the combined harvest score may explain why location mattered more. Confirmed p. 2691 (PDF 13).
15. Fix 15 (metadata): article "64(5), 2679-2697" (p. 2679), data field gives the GitHub repository (p. 2694, PDF 16), not_established added as proposed (Table 5 p = 0.064, p. 2690).
16. Fix 16 (R20mm threshold): ">20 mm" row replaced with "≥20 mm, ≤2 vs >2 days". Confirmed Table 4 p. 2687 (PDF 9), Figure 5 p. 2689 (PDF 11).
17. Full replacement Summary used, with small trims to fit 500 words ("four from IITA", "aims: to", "The authors blame the single check linking the two cycles", "for network connectivity").
18. Medium omissions added: Methods bullets for hosts per group (10 + 10, 12 + 12, p. 2683), plots and blind codes (p. 2683), 26 traits at four stages and kwon in five districts (pp. 2684 to 2685). Key numbers rows for node sizes 306 / 178 (Figure 3) and 99 / 385 (Figure 5), UG130007 0.819 (p = 0.064) (Table 5 p. 2690). Districts, zones and cycle dates in the Summary (p. 2681). Flour-meal result in the Summary (p. 2691).
19. High omission: boiled-product reliabilities as Key numbers rows (0.73 / 0.71 / 0.70, 0.66 / 0.64). Confirmed p. 2691 (PDF 13).
20. Low omission: analysis settings (α = 0.05 with Bonferroni, npseudo = 0.5, AgERA5) added to the Analysis bullet. Confirmed p. 2686 (PDF 8).
21. Source issues added to Notes: R20mm ≥ vs >, UG130007 "superior" vs p = 0.064, UG130016 p < 0.1 vs p = 0.278, district node 3 linked to rainfall, clone name spellings, Table 1 SD 47.5. Confirmed on the pages the review gives. Also added a Note that 26 traits and 30 climatic variables are the card's own counts.

## Skipped

- Approximate per-clone harvest reliabilities for the release candidates (0.36, 0.30, 0.36): read off a heatmap. The "< 0.5" row covers the point.
- Software field additions (ClimMobTools, stablelearner, ag5Tools, climatrends): low importance and not among the metadata fields the instructions list.
- Optional low-importance items: vigor and height reliabilities, other Discussion conclusions (UG110164 vs landraces, dry matter of UG120156 and UG120198, disease-tolerant substitutes). Left out to keep the Summary and table focused.
- Separate source issue on the aim wording (geographic vs climatic): handled by the Summary wording, no Note needed.
- Section 3.2 citing Figure 3 instead of Figure 5: minor, not added as its own Note.
- No relations added: the review proposed none.

## Final counts

- Summary: 497 words
- Gist: 29 words
- Keywords: 11
- Questions: 4
