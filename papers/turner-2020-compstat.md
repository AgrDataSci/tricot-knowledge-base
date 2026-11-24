---
id: turner-2020-compstat
title: Modelling rankings in R. The PlackettLuce package
authors: Turner HL, van Etten J, Firth D, Kosmidis I
year: 2020
journal: Computational Statistics
journal_short: Comput Stat
article: 35, 1027-1057 (from the University of Warwick repository record, not checked against the PDF)
type: software paper
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1007/s00180-020-00959-3
open_copy: https://doi.org/10.1007/s00180-020-00959-3
license: CC BY 4.0
data: beans, nascar and pudding datasets ship with the package. Netflix, T-shirt and sushi benchmark data come from PrefLib. Benchmark and data-preparation code is in the appendix
software: PlackettLuce, https://CRAN.R-project.org/package=PlackettLuce (v0.4.5 on CRAN, published 2026-03-25, checked 2026-10-30)
crops: common bean (example)
region: Nicaragua (example)
keywords: Plackett-Luce model, rankings, partial rankings, ties, pseudo-rankings, worth, quasi-variance, Plackett-Luce trees, R package, tricot analysis
gist: The PlackettLuce R package fits Plackett-Luce models to subset rankings with ties, keeps sparse data estimable with pseudo-rankings, and finds covariate subgroups with model trees
not_established: that PlackettLuce is the fastest ranking software (PLMIX was faster on two of three benchmark data sets); that it fits top n rankings; that it models covariate effects on worth directly (covariates enter only through trees); that it was designed for or validated on tricot data (the Nicaragua bean trial is one worked example); that the bean tree identifies heat-tolerant varieties (it illustrates the method and makes no agronomic claim); that explicit tie modelling is practical beyond ties of order 4
---

## Questions this paper answers

- What does the Plackett-Luce model assume, and what does PlackettLuce add to it?
- How does PlackettLuce handle partial rankings, ties and disconnected comparison networks?
- How do I get standard errors and compare varieties fairly?
- How do I model the effect of climate or farmer covariates on rankings?
- How does PlackettLuce compare in speed with other ranking software?
- What are the practical limits of PlackettLuce on tie order and data size?

## Summary

The paper presents the PlackettLuce R package, which fits a generalized Plackett-Luce model to rankings. Under Luce's axiom, each item has a worth, and the probability of a ranking is the product of choosing each item in turn from those that remain. The paper's bean example shows that tricot data fit this model, because each farmer ranks a small subset of a larger set of varieties.

The package extends the standard model in three ways that matter for on-farm data. It handles partial rankings, where each ranking covers only a subset of items (top n rankings are not supported). It handles ties of any order, with tie parameters estimated alongside worths. By default it adds pseudo-rankings with a hypothetical item, which keeps the network of wins and losses connected so that every item has a finite worth estimate and standard error, even with sparse data. The pseudo-rankings also shrink all worths towards equal worth. This effect is weak when there are many rankings. The authors keep them on by default because this shrinkage typically reduces both bias and variance.

For inference, the package reports standard errors and quasi standard errors. Quasi standard errors do not change with the reference item, so they give approximately correct comparison intervals for any pair of items. Rankings can also be weighted and aggregated.

The package connects Plackett-Luce models with model-based recursive partitioning, producing Plackett-Luce trees. These split the rankings by covariates, such as season, year or night temperature, where item worths change, and fit a separate model in each node. The worked example uses a trial of ten bean varieties in Nicaragua, where farmers named the best and worst of three varieties and compared each with their local variety. The tree first splits at a maximum night temperature of 18.7 (the paper gives no unit). Where nights were cooler, the local variety was most preferred in the Postrera and Apante seasons, and INTA Rojo in the 2016 Primera season. Where nights were warmer, INTA Sequia was most preferred.

Run-time benchmarks against six other R packages on Netflix, T-shirt and sushi data show that PlackettLuce copes well with moderately sized data, but PLMIX was faster on the T-shirt and sushi data. On the NASCAR subset rankings (36 races, 83 drivers), PlackettLuce took 0.2 seconds against 36 seconds for hyper2. The full NASCAR data have 87 drivers.

The authors name two costs. Run time grows quickly with the order of ties, and standard errors are computed by expanding rankings into counts, which can be slow or exceed memory. They expect the package to work well with ties up to order 4 and moderate numbers of items and unique rankings.

Tie parameters have a direct interpretation. For two items of equal worth, the probability that they tie for first place, given that first place is not a tie of three or more, is the two-way tie parameter divided by two plus that parameter. The ties model is illustrated with a classic chocolate pudding tasting study.

## Methods in brief

- **Model.** Generalized Plackett-Luce with worth parameters, tie parameters up to a chosen order, and optional pseudo-rankings with a ghost item.
- **Fitting.** Iterative scaling, BFGS or L-BFGS. L-BFGS was typically fastest.
- **Inference.** Standard errors, Z tests and quasi-variances for contrasts.
- **Covariates.** pltree() combines the model with model-based recursive partitioning, extending the Bradley-Terry trees of the psychotree package. The bean example used up to three nodes and at least 5% of records per node.
- **tricot example.** Best-worst rankings of three varieties plus pairwise comparisons with the local variety, grouped per farmer.

## Stated limitations

- Modelling ties explicitly makes run time grow quickly with the tie order. Standard errors are computed by expanding rankings into counts, which can take as long as the model fit or exceed memory. The authors expect good performance with ties up to order 4 and moderate numbers of items and unique rankings.
- As a guide, 5,000 sub-rankings of 10 items out of 100, with ties up to order 4, took 18.1 s to fit and 14.8 s for the variance-covariance matrix.
- Only subset rankings are supported, not top n rankings. Covariates enter only through trees, not as linear predictors of worth.
- Tree models can be quite unstable, especially with high-dimensional data. The authors suggest ensemble methods such as bagging or random forests for more robust results.
- Some other packages offer features PlackettLuce lacks, such as Bayesian mixture models (PLMIX), covariates on worth (ROlogit) and team rankings (hyper2).

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 10 | Common bean varieties in the Nicaragua tricot example | van Etten et al. 2016, cited in this paper |
| 87 drivers, 36 races | NASCAR benchmark data | Hunter 2004, cited in this paper |
| 3,741 | Simple contrasts in the NASCAR quasi-variance example | This paper |
| −0.7% to +6.7% | Quasi-variance approximation error for NASCAR standard errors | This paper |
| <0.8% | Quasi-variance approximation error in the pudding example | This paper |
| 5,000 rankings (4,926 unique), 10 items | Sushi benchmark dataset | PrefLib (Mattei and Walsh 2013), cited in this paper |
| 0.199 s vs 36.123 s | Time to fit the NASCAR subset rankings (36 races, 83 drivers), PlackettLuce vs hyper2 | This paper |
| 842 (47, 489, 306) | Farmer records in the bean tree, total (card's sum of node sizes) and per terminal node | This paper |
| 18.7 | Maximum night temperature at the first tree split (no unit given) | This paper |
| 0.5 | Default weight of each pseudo-ranking (npseudo) | This paper |
| 18.1 s and 14.8 s | Fit time and variance-covariance time for 5,000 sub-rankings of 10 of 100 items, ties up to order 4 | This paper |

## Notes

- The package is maintained and updated. Always check the CRAN version and changelog before relying on function names or defaults from the paper.
- For tricot data preparation and plotting, use gosset (desousa-2023-softwarex) on top of PlackettLuce.
- Outside this paper: PlackettLuce is the model engine used in most tricot analyses, for example through gosset (desousa-2023-softwarex). The paper itself presents it as a general package for ranking data.
- The volume and pages in the article field (35, 1027-1057) come from the University of Warwick repository record. They were not checked against the PDF, which is the online-first version and prints no volume or page numbers.
- The default pseudo-rankings (npseudo = 0.5) shrink worths towards equal worth. With few rankings the shrinkage is strong (toy example with 5 rankings, p. 19), so it is worth checking results with npseudo = 0 when the network is connected.
- Problem in the source: the NASCAR benchmark in Table 3 uses 83 drivers (four drivers who always finished last were dropped, as in Hunter 2004), but the table does not say so. The full data have 87.
- Problem in the source: in the high night temperature node, INTA Centro Sur (0.44) has a slightly higher log worth than BRT 103-182 (0.38), although the text lists BRT 103-182 first.
- Problem in the source: the paper gives no unit for maxTN (maximum night temperature).
- Problem in the source: two internal cross-references are wrong. Sect. 2.2.4 points to itself instead of Sect. 3.3, and Sect. 3.1.1 points to Sect. 2.2.3 instead of Sect. 3.2.1 for the log scale.
