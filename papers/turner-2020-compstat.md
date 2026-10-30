---
id: turner-2020-compstat
title: Modelling rankings in R. The PlackettLuce package
authors: Turner HL, van Etten J, Firth D, Kosmidis I
year: 2020
journal: Computational Statistics
journal_short: Comput Stat
article: online first 2020 (volume and pages not in the PDF)
type: software paper
doi: https://doi.org/10.1007/s00180-020-00959-3
open_copy: https://doi.org/10.1007/s00180-020-00959-3
license: CC BY 4.0
data: example datasets ship with the package (beans, NASCAR, pudding and others)
software: PlackettLuce, https://CRAN.R-project.org/package=PlackettLuce (v0.4.5 on CRAN, published 2026-03-25, checked 2026-10-30)
crops: common bean (example)
region: Nicaragua (example)
keywords: Plackett-Luce model, rankings, partial rankings, ties, pseudo-rankings, worth, quasi-variance, Plackett-Luce trees, R package, tricot analysis
gist: The R package behind tricot analysis, fitting Plackett-Luce models to partial and tied rankings, with pseudo-rankings for stable estimates and model trees for covariates
---

## Questions this paper answers

- Which statistical model analyzes tricot rankings, and why Plackett-Luce?
- How does PlackettLuce handle partial rankings, ties and disconnected comparison networks?
- How do I get standard errors and compare varieties fairly?
- How do I model the effect of climate or farmer covariates on rankings?
- How does PlackettLuce compare in speed with other ranking software?

## Summary

The paper presents the PlackettLuce R package, which fits a generalized Plackett-Luce model to rankings. Under Luce's axiom, each item has a worth, and the probability of a ranking is the product of choosing each item in turn from those that remain. Tricot produces exactly this kind of data, where each farmer ranks a small subset of a larger set of varieties.

The package extends the standard model in three ways that matter for on-farm data. It handles partial rankings, where each ranking covers only a subset of items. It handles ties of any order, with tie parameters estimated alongside worths. By default it adds pseudo-rankings with a hypothetical item, which keeps the network of wins and losses connected so that every item has a finite worth estimate and standard error, even with sparse data. The pseudo-rankings also act as a mild regularization, shrinking estimates for items seen in few rankings.

For inference, the package reports standard errors and quasi-variances, which allow fair comparison of any pair of items regardless of the reference item. Rankings can also be weighted and aggregated.

The package connects Plackett-Luce models with model-based recursive partitioning, producing Plackett-Luce trees. These split the data by covariates such as night temperature, season or location where variety rankings change, and fit a separate model in each node. The worked example uses a tricot trial of ten common bean varieties in Nicaragua, where farmers gave best and worst rankings plus comparisons with their local variety. The tree shows the local variety preferred in normal seasons where night temperatures were not too high, with heat-tolerant lines doing better elsewhere.

Benchmarks against other R packages (hyper2, pmr, PLMIX, StatRank, ROlogit) on Netflix, T-shirt, sushi and NASCAR data show PlackettLuce is faster or more capable, especially for subset rankings of many items. The NASCAR example has 87 drivers ranked over 36 races.

The authors position PlackettLuce as general-purpose ranking software that grew out of tricot needs, and the standard analysis engine for tricot data.

Tie parameters have a direct interpretation. For two items of equal worth, the probability that they tie for first place is the two-way tie parameter divided by two plus that parameter, illustrated with a classic chocolate pudding tasting study. The package also accepts weights and aggregated rankings, and its methods for standard errors and quasi-variances let users report results in forms familiar from other regression models, which eases adoption by agronomists.

## Methods in brief

- **Model.** Generalized Plackett-Luce with worth parameters, tie parameters up to a chosen order, and optional pseudo-rankings with a ghost item.
- **Fitting.** Iterative scaling, BFGS or L-BFGS. L-BFGS was typically fastest.
- **Inference.** Standard errors, Z tests and quasi-variances for contrasts.
- **Covariates.** pltree() combines the model with model-based recursive partitioning (psychotree, partykit).
- **Tricot example.** Best-worst rankings of three varieties plus pairwise comparisons with the local variety, grouped per farmer.

## Stated limitations

- Model trees can be unstable with high-dimensional covariates, so splits need checking.
- The pseudo-rankings slightly shrink estimates, which is intended but changes estimates for rarely observed items.
- Some competitor packages offer Bayesian mixtures or features PlackettLuce does not.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 10 | Common bean varieties in the Nicaragua tricot example | van Etten et al. 2016, cited in this paper |
| 87 drivers, 36 races | NASCAR benchmark data | Hunter 2004, cited in this paper |
| 3,741 | Simple contrasts in the NASCAR quasi-variance example | This paper |
| −0.7% to +6.7% | Quasi-variance approximation error for NASCAR standard errors | This paper |
| <0.8% | Quasi-variance approximation error in the pudding example | This paper |
| 5,000 rankings, 10 items | Sushi benchmark dataset | Cited in this paper |

## Notes

- The package is maintained and updated. Always check the CRAN version and changelog before relying on function names or defaults from the paper.
- For tricot data preparation and plotting, use gosset (desousa-2023-softwarex) on top of PlackettLuce.
