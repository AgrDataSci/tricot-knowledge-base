# Change log: gesesse-2023-pnas

Applied the review's fixes 1 to 12 and 14, added all source issues to Notes plus one new one (Methods sentence cut off), and moved the AgrDataSci repository pointers from data to a labelled Notes line. Fix 13 (CRAN version) was skipped.

## Applied

1. Fix 1: added not_established after gist, as suggested. Confirmed p. 4 (Kulumsa negative), p. 3 (farmers not representative), p. 6 (partial breakdown), p. 8 (on-station PVS, no candidate genes), p. 4 to 5 (accuracies 0.09 and 0.11).
2. Fix 2 / claim 21: rewrote the reverse-direction sentence so 0.02 applies only to yield, and added that men's scores gave higher accuracies. Confirmed p. 5 and Fig. 3C (p. 6, yield-trained model predicted panel appreciation at about 0.32).
3. Fix 3: added low absolute accuracies, the negative prediction at Kulumsa and the within-EtNAM improvement. Confirmed p. 4 and Fig. 3A and 3B (p. 6).
4. Fix 4: added a Ranking analysis bullet in Methods. Confirmed p. 9 (pairwise wins, ties dropped) and Fig. 2 (p. 5: tree by location then gender in Adet and Kulumsa, worth of Asassa set at 0, families on y-axis). Wording changed: the review says data were "aggregated by EtNAM family", but the Methods sentence breaks off after "aggregated by" in the PDF (p. 9, p. 10 starts with acknowledgements). The bullet says worth was estimated per family, which Fig. 2 shows, and the truncation is flagged in Notes.
5. Fix 5 / claim 17: replaced "outperformed ... everywhere" with "could reach a higher worth". Confirmed p. 4 ("could outperform") and Fig. 2 (p. 5).
6. Fix 6 / claim 5: EtNAM crossing now names 50 landraces, Bidi and Asassa. Confirmed p. 8 to 9.
7. Fix 7 / claim 37: Key numbers primary source now "Mausch et al. 2021 (ref. 17), cited in this paper". Confirmed p. 2 and ref. 17 (p. 10).
8. Fix 8 / claim 26: "do not reflect" changed to "are seldom representative of". Confirmed p. 8.
9. Fix 9: data field reduced to Dryad and EtNAM.GS. AgrDataSci pointers moved to a Notes line labelled as outside the source and not checked against the PDF. Confirmed p. 9 (only Dryad and EtNAM.GS listed).
10. Fix 10: replaced Trials and Farmer scoring bullets. Confirmed p. 9 (years, groups of five, half plots flowered), p. 2 ("expert wheat growers"), p. 5 (different groups per site and for the diversity panel). Wording changed slightly to "Expert local wheat growers".
11. Fix 11: added three limitations. Confirmed p. 3 (not representative of Ethiopian farming systems), p. 6 (partial deconstruction), p. 7 (other genetic backgrounds).
12. Fix 12: added the N45/N51 source issue to Notes. Confirmed p. 4 text against Fig. 2 (p. 5).
13. Fix 14 (optional): gist replaced with the review's version (27 words).
14. Source issues table: added Notes lines for the Fig. 2 caption Table S1/S3 mismatch (p. 4 to 5), "R2 = −0.29" (p. 4) and the R/qtl2 and JoinMap reference mismatches (p. 9 to 10). The instructions ask for every unflagged source issue, so these were added even though the review rated them low.
15. New source issue (not in the review): Methods sentence on aggregation breaks off after "aggregated by" (p. 9 to 10). Added to Notes.

## Skipped

- Fix 13 (software field version and dates): needs a check on CRAN, which was not allowed in this run (no web access). The source names no version. Left the field as it was.
- Optional completeness items (farmers favoured high-yielding, tall, early plants; yield component accuracies; GWAS 81 MTAs; tricot ref. 43 note): low or optional, and the Summary is already at 493 words. The "tall plants" wording also mixes DP PVS traits (p. 5) with EtNAM drivers.

## Final counts

- Summary words: 493
- Gist words: 27
- Keywords: 12
- Questions: 5
- Frontmatter parses as YAML. No em dashes. Semicolons only as separators in frontmatter and in the existing Key numbers row the review marked correct.
