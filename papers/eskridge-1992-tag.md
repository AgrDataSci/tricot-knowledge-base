---
id: eskridge-1992-tag
title: Choosing plant cultivars based on the probability of outperforming a check
authors: Eskridge KM, Mumm RF
year: 1992
journal: Theoretical and Applied Genetics
journal_short: Theor Appl Genet
article: 84(3-4), 494-500
type: research article
source: external
peer_reviewed: yes
curated_card: yes
doi: https://doi.org/10.1007/BF00229512
open_copy:
license: © Springer-Verlag 1992, no open licence; papers-pdf holds only a one-page pointer to the DOI and the reference
data: CIMMYT 1988 experimental variety trials, reported in the CIMMYT international maize testing program 1988 report; no data or code deposited
crops: maize
region: international (CIMMYT tropical lowland and mid-altitude maize trials, 22 to 63 environments per trial)
keywords: reliability, probability of outperforming a check, check variety, stability analysis, safety-first, genotype by environment interaction, pairwise comparison, repeatability, Cochran Q test, cultivar selection, risk
gist: Defines reliability as the probability that a cultivar beats a check, gives two estimators and tests, and finds it less repeatable than mean yield but more than stability statistics
not_established: that reliability applies unchanged to farmer rankings or tricot data, which the paper does not cover; any threshold other than zero, such as a 25% yield gain; that reliability is as repeatable as the mean yield (it was less so); that a high reliability against one check holds against another check or outside the check's area of adaptation; any use of on-farm or farmer-managed trials (the data are researcher-run international variety trials); that reliability is more repeatable than the Finlay-Wilkinson slope in every trial (it was not in EVT 12)
---

## Questions this paper answers

- What is the reliability of a cultivar, and how is it computed?
- How does reliability differ from comparing mean yields?
- How does reliability relate to stability statistics such as the Finlay-Wilkinson slope or Shukla's stability variance?
- Is reliability repeatable across different sets of environments?
- How many environments are needed for a precise reliability estimate?
- How much does the choice of check matter?

## Summary

Breeding programmes compare new cultivars with a check across many environments. The usual analysis tests whether the true means differ. The authors argue that this is not what a breeder most needs to know. The practical question is how likely the new cultivar is to do better than the check where the check is normally grown. A true mean is also an abstract idea for growers and sales managers. The paper offers a single index that answers the practical question and that anyone involved in the decision can read.

The index is called reliability. It is the probability that the difference between the test cultivar and the check is positive. The idea comes from safety-first decision models and from reliability in engineering. A cultivar with a reliability near 0.5 is a risky choice, since it loses to the check in half of the environments. One at 0.9 loses in one environment out of ten.

Two estimators are given. If the differences are normally distributed across environments, reliability follows from their mean and standard deviation. Without that assumption, it is the share of environments where the test cultivar beat the check. The paper adds confidence intervals and tests of equal reliability among cultivars, a Wald test for the normal case and Cochran's Q for the nonparametric one.

Reliability combines performance and stability. The standard deviation of the differences can be written in terms of the Finlay-Wilkinson regression coefficient, the Eberhart-Russell deviation mean square or Shukla's stability variance. For a given positive mean difference, a less stable cultivar has a lower reliability. The breeder no longer has to decide how to weigh yield against stability. Reliability and mean comparisons agree when stability differs little, but can disagree when it differs a lot.

The method is illustrated with six CIMMYT maize experimental variety trials from 1988. In one trial of 15 varieties over 58 environments, every variety had a reliability above 0.65, and the two estimators agreed closely. The variety with the highest mean yield ranked only third or fourth on reliability. Reliability correlated strongly with mean yield in all six trials. It correlated weakly with the deviation mean square and the stability variance in five trials, and somewhat with the slope in three, because the slope tracked mean yield.

To test repeatability, the environments of four trials were split at random into two sets, six times, and the rankings of varieties compared between sets. Reliability was less repeatable than mean yield. It beat the regression coefficient in most runs, though not in EVT 12, and clearly beat the deviation mean square and the stability variance, whose mean correlations were near or below 0.2.

The authors list practical advantages. Reliability needs only the test cultivar and the check to be grown together, so it tolerates unbalanced data and can use trials from other programmes. Its inference depends on the check and the test cultivar, not on the other entries in the trial. They also list limits, above all the choice of check.

## Methods in brief

- **Definition.** Reliability of cultivar i is P(Yi − Yc > 0), with Yi and Yc the responses of the test cultivar and the check in the same environment.
- **Normal estimator.** P(Z > −mean difference / standard deviation of the differences), with the sample mean and standard deviation over environments. Approximate confidence intervals and a Wald test of equal reliabilities.
- **Nonparametric estimator.** The proportion of environments where the test cultivar outperformed the check. Confidence intervals for proportions and Cochran's Q test.
- **Link to stability.** The variance of the differences expressed through the Finlay-Wilkinson, Eberhart-Russell and Shukla parameters (appendix).
- **Data.** Six CIMMYT 1988 experimental variety trials of tropical lowland and mid-altitude maize, 10 to 19 varieties and 22 to 63 environments each. Locations entered only with a coefficient of variation below 30% for yield and below 20% for plants harvested. Local checks were excluded because they differed by location. The check was the oldest reference entry with the lowest mean yield.
- **Repeatability.** Environments of four trials split at random into two sets, six runs, with rank correlations between sets for mean yield, both reliabilities and three stability statistics.

## Stated limitations

- The choice of check can change the reliabilities substantially. A check adapted to a narrow range of environments gives unrealistic values in trials that cover a wide range.
- When several checks are available and none is clearly the right one, reliabilities may have to be computed against each.
- Reliability assumes the breeder cares most about outperforming the check, and that the trial environments represent where the check is well adapted.
- More environments are needed to estimate reliability precisely than to estimate a mean.
- Reliability does not replace understanding the biology of genotype by environment interaction.
- Economic factors such as production costs were not considered and need more research.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 0.5 / 0.9 | Reliability of a risky cultivar / of one that loses to the check in one environment out of ten | This paper |
| 6 | CIMMYT 1988 experimental variety trials analysed | This paper |
| 22 to 63 | Environments per trial | This paper |
| 15 varieties, 58 environments | Trial EVT 13, used for the worked example | This paper |
| >0.65 | Reliability of every test variety in EVT 13 | This paper |
| 55 of 58 | Environments where the most reliable variety in EVT 13 beat the check (reliability 0.948 nonparametric, 0.935 normal) | This paper |
| Q = 36.72, P = 0.00046 | Cochran's Q test of equal reliabilities in EVT 13, nonparametric estimator (the text gives 0.000458, the table footnote prints 0.00045) | This paper |
| W = 51.69, P = 1.5 × 10⁻⁶ | Wald test of equal reliabilities in EVT 13, normal estimator, 14 test varieties | This paper |
| >0.70 | Rank correlation between reliability and mean yield, all six trials | This paper |
| 0.34 to 0.75 | Mean rank correlation of mean yield between random halves of the environments, four trials | This paper |
| 0.25 to 0.54 | The same for the two reliability estimators | This paper |
| <0.2 | The same for the deviation mean square and Shukla's stability variance, in general | This paper |
| about 16 | Environments needed to be within 0.15 of a true reliability of 0.85, with normal responses | This paper |

## Notes

- `papers-pdf/eskridge-and-mumm-1992.pdf` is a one-page pointer to the DOI and the reference, not the article, because the article has no open licence. The card was drafted from the full published text supplied by Kauê de Sousa on 2026-11-20 and has not been checked by a person.
- The first page prints the second author as R. F. Mumm. The text extraction misreads it as R. E Mumm.
- Ten source documents in this knowledge base cite this paper, among them brown-2023-agronj and desousa-2023-softwarex, which now link to this card. The others (desousa-2021-commsbio, desousa-2024-asd, chase-2026-book and five more) can be linked by the curator.
- Outside this paper: for tricot and maniva, this paper is the origin of the reliability reported by gosset and used across the team's analyses. The reliability in gosset is computed from Plackett-Luce worth, as worth of the item over the sum of its worth and that of the check. This paper works with measured yields, not rankings. See desousa-2023-softwarex for the function and brown-2023-agronj for an application with a reference genotype.
- The draft use case on breakthrough products in tricot-analysis-workflows moves the threshold from zero to a 25% gain. That is an extension by the maniva team, not a result of this paper.
- A card for Dorado-Betancourt et al. (dorado-2026-tag) covers genetic parameters from rankings, published in the same journal.
- Source issue: in Table 2 the mean difference for variety 15 should read 0.757, not 0.797. Its mean yield (5.573 minus the check's 4.816) and its normal reliability (0.863) both fit 0.757 (reviewer's calculation, checked).
- Source issue: the Cochran's Q P value is 0.00045 in the Table 2 footnote and 0.000458 in the text. The text value is correct for 13 degrees of freedom (reviewer's calculation).
- Source issue: the Discussion says reliability is more repeatable than the stability statistics, but in EVT 12 the Finlay-Wilkinson slope (mean 0.459) was more repeatable than both reliabilities (0.295 and 0.251). The claim holds for most runs, not every trial.
