# Change log: eskridge-1992-tag

Applied all eight review fixes, added three source issues to Notes, and brought the Summary to 499 words and the gist to 29 words.

Source used: /home/claude/work/pdfs/eskridge-and-mumm-1992-full.pdf and its text extraction. The papers-pdf/ stub was not touched. Pages: printed page first, PDF page in brackets.

## Applied

1. Fix 1 (claim 23): Summary paragraph 5 now says reliability correlated weakly with the deviation mean square and the stability variance in five trials, and somewhat with the slope in three (EVTs 14B, 16A, 16B), because the slope tracked mean yield. Confirmed p. 497 (PDF 4), Table 3 and text (r > 0.35, r < 0.39, r > 0.46).
2. Fix 2 (claims 32, 33): deleted the gosset and Plackett-Luce paragraph from the Summary. Its first sentence now starts the existing gosset note, marked "Outside this paper". Not in the source (checked the whole text).
3. Fix 3 (claim 27): Summary paragraph 6 replaced. It now gives the EVT 12 exception and says "near or below 0.2" instead of "close to zero". Confirmed Table 4, p. 498 (PDF 5): EVT 12 means are bi 0.459, Ri 0.295, RNi 0.251. Results text says "in most runs" and "generally quite small (r < 0.2)".
4. Fix 4: gist replaced (29 words). Confirmed p. 498 to 499 (PDF 5 to 6).
5. Fix 5: added the sentence on agreement with mean comparisons when stability differs little. Confirmed p. 499 (PDF 6).
6. Fix 6: added the Wald test row (W = 51.69, P = 1.5 × 10⁻⁶, normal estimator, 14 test varieties). Also took the optional change to the Q row: P = 0.00046, with both printed values noted. Confirmed Table 2 footnotes a and b and text, p. 497 (PDF 4). Recomputed chi-square P (13 df) = 0.000458.
7. Fix 7 (claim 62): author-initials note replaced. Confirmed on the PDF 1 image: "R. F. Mumm" is legible. The text extraction reads "R. E Mumm".
8. Fix 8: appended the EVT 12 slope item to not_established. Confirmed Table 4, p. 498 (PDF 5).
9. Source issue 1: Notes line on the variety 15 mean difference (0.797 printed, 0.757 fits). Confirmed Table 2, p. 497 (PDF 4): 5.573 − 4.816 = 0.757. Recomputed Φ(0.757/0.692) = 0.863, which matches the printed normal reliability, and Φ(0.797/0.692) = 0.875, which does not.
10. Source issue 2: Notes line on the Q P value (0.00045 in footnote, 0.000458 in text). Confirmed p. 497 (PDF 4).
11. Source issue 4: Notes line saying the Discussion's general repeatability claim does not hold in EVT 12. Confirmed p. 498 to 499 (PDF 5 to 6), Table 4.

## Skipped

- Source issue 3 (Shukla means 0.207 and 0.209, slightly above 0.2): not added to Notes, as the review says it is not needed once fix 3 is applied ("near or below 0.2").
- Low-importance omissions (Kendall's tau, t distribution, related pedigrees, comparison with expected utility and stochastic dominance, the EVT 13 check name, 16A two-group correlation): left out to keep the Summary within 500 words. None is a high or medium item.
- Metadata: no changes needed. doi and issue number were not checkable without web access. No relations added (none suggested by the review).

## Final counts

- Summary: 499 words
- Gist: 29 words
- Keywords: 11
- Questions: 6
- Frontmatter parses as YAML. curated_card unchanged (no).
