# Card review: eskridge-1992-tag

- **Card:** papers/eskridge-1992-tag.md
- **Source:** /home/claude/work/pdfs/eskridge-and-mumm-1992-full.pdf (7 pages, printed pages 494 to 500). The copy in papers-pdf/ is a one-page link stub and was not used.
- **Reviewed:** 2026-11-25, by an independent agent (pilot)
- **Verdict:** Minor fixes

Page references give the printed journal page first and the PDF page in brackets, for example p. 497 (PDF 4).

## Overview

| Check | Result |
|---|---|
| Claims checked | 75 (13 frontmatter fields, 62 body claims) |
| Supported | 68 |
| Imprecise | 3 |
| Not in source | 2 |
| Contradicted | 0 |
| Not checked (no web access) | 2 (doi, issue number in article) |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 4 (all medium, none high) |
| Metadata issues | 2 (gist is 30 words, summary is 505 words) |

The card is accurate and careful. Every number in Key numbers was recomputed or read off the tables and matches the source. The main fixes are one summary sentence that overstates how weakly reliability tracks the stability statistics (the Finlay-Wilkinson slope did correlate in three trials), a Summary paragraph on gosset and Plackett-Luce worth that is outside knowledge and belongs in Notes, and two small length overruns (summary 505 words, gist 30 words).

## Fixes needed

1. **Correlation with stability statistics is overstated (Summary, paragraph 5).** The card says reliability correlated "weakly with the stability statistics in five of them". The source says only the deviation mean square and Shukla's variance were poorly correlated (r < 0.39) in five of six trials. The regression coefficient was somewhat correlated (r > 0.35) with both reliabilities in EVTs 14B, 16A and 16B, which the authors trace to the slope being correlated with mean yield (p. 497, PDF 4, Table 3). Replace with:
   > Reliability correlated strongly with mean yield in all six trials. It correlated weakly with the deviation mean square and the stability variance in five trials, and somewhat with the slope in three, because the slope tracked mean yield.

2. **Outside knowledge in the Summary (paragraph 8).** The paragraph on gosset, Plackett-Luce worth and the team's analyses is not in the source. The card does say the ranking application is later work, but the template wants outside knowledge in Notes. Delete the whole paragraph from the Summary (this also brings the summary back under 500 words). Start the existing gosset note with this sentence:
   > Outside this paper: for tricot and maniva, this paper is the origin of the reliability reported by gosset and used across the team's analyses.

3. **"Close to zero" and the EVT 12 exception (Summary, paragraph 6).** The mean rank correlations of the deviation mean square and Shukla's variance between halves range from −0.17 to 0.21 (Table 4, p. 498, PDF 5). The source calls them "generally quite small (r < 0.2)", not close to zero. Also, in EVT 12 the regression coefficient (mean 0.459) was more repeatable than both reliabilities (0.295 and 0.251). Across all 24 runs, both reliabilities beat the slope in 16 runs (my count). Replace the sentence "Reliability was less repeatable than mean yield, but more repeatable ... which were close to zero." with:
   > Reliability was less repeatable than mean yield. It beat the regression coefficient in most runs, though not in EVT 12, and clearly beat the deviation mean square and the stability variance, whose mean correlations were near or below 0.2.

4. **Gist is 30 words (template: under 30) and leaves out that reliability was less repeatable than the mean.** Replace with (29 words):
   > Defines reliability as the probability that a cultivar beats a check, gives two estimators and tests, and finds it less repeatable than mean yield but more than stability statistics

5. **Missing point on how reliability differs from mean comparisons (Summary, paragraph 4).** This answers the card's own second question and is stated twice in the source (p. 495, PDF 2 and p. 499, PDF 6). After "The breeder no longer has to decide how to weigh yield against stability." add:
   > Reliability and mean comparisons agree when stability differs little, but can disagree when it differs a lot.

   With fixes 1, 2, 3 and 5 together, the summary is 499 words (checked).

6. **Wald test result missing from Key numbers.** Table 2 footnote b and the text (p. 497, PDF 4) give it. Add a row:
   > | W = 51.69, P = 1.5 × 10⁻⁶ | Wald test of equal reliabilities in EVT 13 (normal estimator), 14 test varieties | This paper |

   Optionally change the Q row to "Q = 36.72, P = 0.00046" and add "(the table footnote prints 0.00045)". See Source issues.

7. **Notes, author initials.** The first page (PDF 1, viewed as an image) prints "R. F. Mumm" legibly. Only the period after F is faint, which is why the text extraction reads "R. E Mumm". Replace the note with:
   > The first page prints the second author as R. F. Mumm. The text extraction misreads it as R. E Mumm.

8. **not_established, optional addition.** Append:
   > ; that reliability is more repeatable than the Finlay-Wilkinson slope in every trial (it was not in EVT 12)

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Choosing plant cultivars based on the probability of outperforming a check | Same (p. 494, PDF 1) | Supported |
| authors | Eskridge KM, Mumm RF | K. M. Eskridge and R. F. Mumm (p. 494, PDF 1, image) | Supported |
| year | 1992 | Theor Appl Genet (1992), received 1991, accepted Dec 1991 (p. 494) | Supported |
| journal | Theoretical and Applied Genetics | Theor Appl Genet, TAG logo (p. 494) | Supported |
| article | 84(3-4), 494-500 | 84:494-500 (p. 494). The issue number (3-4) is not printed | Volume and pages Supported. Issue Not checked (no web access) |
| type | research article | Original article with methods, results, discussion | Supported |
| doi | 10.1007/BF00229512 | Not printed | Not checked (no web access) |
| license | © Springer-Verlag 1992, no open licence | © Springer-Verlag 1992 (p. 494). No open licence printed | Supported |
| data | CIMMYT 1988 EVTs, CIMMYT 1988 report, no data deposited | Table 1 caption cites CIMMYT (1990), the 1988 testing programme report (p. 496, 500). No deposit mentioned | Supported |
| crops | maize | Maize throughout | Supported |
| region | international, tropical lowland and mid-altitude, 22 to 63 environments | Table 1 (p. 496, PDF 3). No countries given | Supported |
| gist | Defines reliability ... more repeatable than common stability statistics | Matches the source's conclusions (p. 499) | Supported, but 30 words (template issue) and omits "less than mean yield". See fix 4 |
| not_established | five items | All consistent with the source | Supported. Optional addition in fix 8 |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Programmes compare new cultivars with a check across environments | Supported | p. 494 (PDF 1) | |
| 2 | Summary | Usual analysis tests true mean differences | Supported | p. 494 | |
| 3 | Summary | Authors argue this is not what the breeder most needs | Supported | p. 494 | |
| 4 | Summary | Practical question: chance of beating check where check is grown | Supported | p. 494 | |
| 5 | Summary | True mean abstract for growers and sales managers | Supported | p. 494 | |
| 6 | Summary | Single index readable by all decision makers | Supported | p. 494 | |
| 7 | Summary | Reliability = P(difference > 0) | Supported | Eq. 1, p. 495 (PDF 2) | |
| 8 | Summary | Idea from safety-first models and engineering reliability | Supported | p. 494 to 495 | Source cites machine life testing and quality engineering |
| 9 | Summary | 0.5 is risky, loses in half of environments | Supported | p. 495 | |
| 10 | Summary | 0.9 loses one in ten | Supported | p. 495 | |
| 11 | Summary | Normal estimator from mean and SD | Supported | Eq. 2, p. 495 | |
| 12 | Summary | Nonparametric: share of environments won | Supported | p. 495 | |
| 13 | Summary | CIs, Wald test (normal), Cochran's Q (nonparametric) | Supported | p. 495 | |
| 14 | Summary | Combines performance and stability | Supported | p. 495, 499 | |
| 15 | Summary | SD of differences written via FW, ER, Shukla | Supported | p. 495 to 496, Appendix p. 500 | Source writes the variance. Fine |
| 16 | Summary | For a positive mean difference, less stable means lower reliability | Supported | p. 496 (PDF 3) | |
| 17 | Summary | Breeder need not weigh yield against stability | Supported | p. 499 (PDF 6) | |
| 18 | Summary | Six CIMMYT 1988 EVTs | Supported | Table 1, p. 496 | |
| 19 | Summary | EVT 13: 15 varieties, 58 environments, all > 0.65 | Supported | Table 2, p. 497 (PDF 4) | 15 includes the check, so 14 test varieties have reliabilities. Lowest Ri 0.690, RNi 0.666 |
| 20 | Summary | Two estimators agreed closely | Supported | p. 497 | |
| 21 | Summary | Highest-mean variety ranked 3rd or 4th | Supported | p. 497, Table 2 | Variety 6: 4th on Ri, 3rd on RNi, checked |
| 22 | Summary | Strong correlation with mean yield in all six | Supported | Table 3, p. 497 | Ri 0.70 to 0.85, RNi 0.76 to 0.96 |
| 23 | Summary | Weak correlation with stability statistics in five | Imprecise | p. 497, Table 3 | True for S²di and Shukla only. bi correlated (r > 0.35) in 14B, 16A, 16B. Fix 1 |
| 24 | Summary | Four trials split at random into two sets, six times | Supported | p. 496 | EVTs 16A and 16B left out for too few environments |
| 25 | Summary | Less repeatable than mean yield | Supported | Table 4, p. 498 (PDF 5) | |
| 26 | Summary | More repeatable than slope in most runs | Supported | p. 498 | Both reliabilities beat bi in 16 of 24 runs (my count). Not in EVT 12 on average |
| 27 | Summary | S²di and Shukla "close to zero" | Imprecise | Table 4, p. 498 | Means −0.17 to 0.21. Source says r < 0.2 generally. Fix 3 |
| 28 | Summary | Needs only test and check grown together | Supported | p. 499 | Source: within reasonable proximity |
| 29 | Summary | Tolerates unbalanced data, other programmes' trials | Supported | p. 499 | |
| 30 | Summary | Inference depends on check and test only | Supported | p. 499 | |
| 31 | Summary | Limits, above all the choice of check | Supported | p. 499 | |
| 32 | Summary | Origin of gosset reliability used by the team | Not in source | | Outside knowledge. Move to Notes. Fix 2 |
| 33 | Summary | In gosset computed from Plackett-Luce worth, later work | Not in source | | Correctly flagged as later work, but belongs in Notes |
| 34 | Methods | Definition P(Yi − Yc > 0) | Supported | Eq. 1, p. 495 | |
| 35 | Methods | Normal estimator, CIs, Wald test | Supported | Eq. 2, p. 495, Appendix | |
| 36 | Methods | Nonparametric proportion, CIs, Cochran's Q | Supported | p. 495 | |
| 37 | Methods | Variance via FW, ER, Shukla (appendix) | Supported | p. 496, 500 | |
| 38 | Methods | 10 to 19 varieties, 22 to 63 environments, lowland and mid-altitude | Supported | Table 1 | Recounted: 10, 15, 17, 19, 15, 16 varieties. 47, 58, 63, 43, 24, 22 environments |
| 39 | Methods | CV < 30% yield, < 20% plants harvested | Supported | p. 496 | |
| 40 | Methods | Local checks excluded | Supported | p. 496 | |
| 41 | Methods | Check = oldest reference entry, lowest mean | Supported | p. 496 | |
| 42 | Methods | Repeatability design and statistics | Supported | p. 496 | Source uses Kendall's tau (stated for Table 3, p. 497) |
| 43 | Limitations | Choice of check, narrowly adapted check unrealistic | Supported | p. 498 to 499 | |
| 44 | Limitations | Several checks may be needed | Supported | p. 499 | |
| 45 | Limitations | Assumes outperforming check is main aim, representative environments | Supported | p. 498 | Source calls these the two assumptions |
| 46 | Limitations | More environments than for a mean | Supported | p. 499 | |
| 47 | Limitations | Does not replace biology of G×E | Supported | p. 499 | |
| 48 | Limitations | Economic factors need research | Supported | p. 499 | |
| 49 | Key numbers | 0.5 / 0.9 | Supported | p. 495 | |
| 50 | Key numbers | 6 trials | Supported | Table 1 | |
| 51 | Key numbers | 22 to 63 environments | Supported | Table 1 | |
| 52 | Key numbers | EVT 13: 15 varieties, 58 environments | Supported | Tables 1, 2 | |
| 53 | Key numbers | > 0.65 for every test variety | Supported | p. 497 | |
| 54 | Key numbers | 55 of 58, 0.948 and 0.935 | Supported | Table 2 | Recomputed: 55/58 = 0.948. Φ(0.850/0.560) = 0.935 |
| 55 | Key numbers | Q = 36.72, P = 0.00045 | Supported | Table 2 footnote a | Recomputed P (χ², 13 df) = 0.000458, as in the text. See Source issues |
| 56 | Key numbers | > 0.70 with mean yield, all six | Supported | p. 497, Table 3 | |
| 57 | Key numbers | 0.34 to 0.75 for mean yield | Supported | Table 4 | Means 0.341, 0.752, 0.424, 0.532 |
| 58 | Key numbers | 0.25 to 0.54 for reliabilities | Supported | Table 4 | Ri 0.274 to 0.424, RNi 0.251 to 0.542 |
| 59 | Key numbers | < 0.2 for S²di and Shukla, in general | Supported | p. 498 | Matches the source's wording. Two means are 0.207 and 0.209 |
| 60 | Key numbers | About 16 environments for ± 0.15 at true 0.85 | Supported | p. 499 | Method and confidence level not stated in source. My delta-method check gives about 14 at 95%, so the order is right |
| 61 | Notes | papers-pdf holds only a one-page pointer | Supported | Caller's brief | |
| 62 | Notes | Initials printed unclearly | Imprecise | p. 494, PDF 1 image | Printed R. F. legibly. Fix 7 |

Notes on later papers, the gosset formula and the 25% threshold are labelled outside knowledge or cross-references and were not counted.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Variety 15 mean difference printed as 0.797. Mean yield minus check (5.573 − 4.816) gives 0.757, and RNi 0.863 fits 0.757 (Φ(0.757/0.692) = 0.863), not 0.797 (which gives 0.875) | Table 2, p. 497 (PDF 4) | No | In Table 2 the mean difference for variety 15 should read 0.757, not 0.797. Its mean yield and normal reliability both fit 0.757 (reviewer's calculation). |
| Cochran's Q P value is 0.00045 in the table footnote and 0.000458 in the text. Recomputed (χ², 13 df) = 0.000458 | p. 497 | No | The Q test P value is 0.00045 in the Table 2 footnote and 0.000458 in the text. The text value is correct for 13 degrees of freedom (reviewer's calculation). |
| Text says S²di and Shukla repeatabilities were generally below 0.2, but Shukla's mean is 0.207 in EVT 12 and 0.209 in EVT 14B | p. 498, Table 4 | Partly ("in general") | Not needed if fix 3 is applied. |
| Discussion says reliability is more repeatable than the stability statistics, but in EVT 12 the slope (0.459) beat both reliabilities (0.295, 0.251). Results text says "in most runs", which is right (16 of 24) | p. 498, 499 | No | In EVT 12 the Finlay-Wilkinson slope was more repeatable than both reliabilities, so the paper's general claim holds for most runs but not every trial. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: three objectives (illustrate, relate to stability, compare repeatability) | Yes | | |
| Design: six EVTs, filters, check choice, split-half repeatability | Yes | | |
| Sample sizes per trial | Yes (range) | | |
| Main results EVT 13 (all > 0.65, best 0.948, top-mean not top-reliable) | Yes | | |
| Wald test W = 51.69, P = 1.5 × 10⁻⁶ | No | Medium | Fix 6 |
| bi correlated with reliability in 14B, 16A, 16B via mean, and S²di/Shukla correlated (r > 0.63) in 16A due to two variety groups | No (summary says weak in five) | Medium | Fix 1 covers bi. 16A grouping is low and optional |
| EVT 12 exception in repeatability | No | Medium | Fix 3 |
| Reliability agrees with mean comparisons when stability is similar, differs when not | No | Medium | Fix 5 |
| Kendall's tau used for rank correlations | No | Low | Optional in Methods: "rank correlations (Kendall's tau)" |
| t distribution would give only slightly different estimates | No | Low | |
| Stability statistics depend on the set of cultivars, reliability does not | Yes (paragraph 7) | | |
| Related pedigrees may stand in for the test cultivar | No | Low | |
| Fewer assumptions than expected utility indices, no disaster parameters, complete ranking unlike stochastic dominance | No | Low | |
| Check in EVT 13 was Across 7627 RE (entry 14, lowest mean 4.816 t/ha) | No | Low | |
| Authors' limitations | Yes, all six | | |
| Conclusions (easy, weighs performance and stability, repeatable) | Yes | | |
| For tricot users: works on measured yields, not rankings | Yes (not_established) | | |

## Template compliance

- Summary: 505 words, slightly over the 400 to 500 target. Fixes 1, 2, 3 and 5 together give 499 words.
- Gist: 30 words, needs to be under 30. Fix 4 gives 29.
- Keywords: 11 (within 8 to 12).
- Questions: 6 (within 4 to 7). All answered by the source.
- House style: tricot and maniva are lowercase throughout. No problems found.
