---
id: desousa-2023-softwarex
title: gosset. An R package for analysis and synthesis of ranking data in agricultural experimentation
authors: de Sousa K, Brown D, Steinke J, van Etten J
year: 2023
journal: SoftwareX
journal_short: SoftwareX
article: 22, 101402
type: software paper
doi: https://doi.org/10.1016/j.softx.2023.101402
open_copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC10212778/
license: CC BY
data: example tricot common bean data distributed with the package
software: gosset, https://CRAN.R-project.org/package=gosset (v1.5.1 on CRAN, published 2025-11-19, checked 2026-10-30)
crops: common bean (example)
region: Nicaragua (example)
keywords: gosset, R package, ranking data, rank_tricot, Plackett-Luce, Bradley-Terry, reliability, regret, worth map, cross-validation, tricot workflow
gist: R package covering the tricot analysis workflow, from converting tricot data to rankings through model selection to reliability, regret and worth plots
---

## Questions this paper answers

- How do I turn tricot data into rankings for PlackettLuce?
- Which tools exist to select covariates and evaluate ranking models?
- How do I compute reliability against a check variety, or regret?
- How do I visualize worth across traits and compare two traits?

## Summary

gosset supports the analysis and synthesis of ranking data in agricultural experiments, with tricot as the main use case. It is named after William Sealy Gosset, the Guinness brewer behind Student's t-test, who developed practical experimental methods for comparing barley varieties. The package fills gaps between general ranking software, mainly PlackettLuce, and the workflow agronomists and breeders need.

Functions cover three stages. For data preparation, rank_tricot converts tricot best and worst data into PlackettLuce rankings, rank_numeric converts numeric measurements such as yield into rankings, and set_binomialfreq and set_paircomp convert rankings for Bradley-Terry models and Bradley-Terry trees. For model selection and evaluation, gosset offers AIC, deviance-based forward selection of covariates (btpermute), k-fold cross-validation with custom folds, Kendall's tau, Kendall's W and McFadden's pseudo-R². For interpretation, it computes reliability, the probability that an item outperforms a reference variety, and regret, the loss under the worst outcome. It also offers worth bar plots, a worth heat map across traits, and a plot comparing two traits.

The illustrative example uses a tricot trial where farmers tested three of ten common bean varieties. It links rankings to rainfall from the chirps package and indices from climatrends, fits Plackett-Luce trees, and shows that some varieties that rank low overall outperform others under higher rainfall. It then compares overall appreciation with yield to reveal varieties farmers value for traits beyond yield, such as taste and marketability, and computes reliability against the check variety Amadeus 77 under drier and wetter conditions.

The authors note the package enabled several published studies, is open source, and supports a community of practice around tricot, including the Africa-wide 1000FARMS on-farm trial network.

The authors stress reproducible and efficient workflows. In the example, gosset handled data preparation, model validation and presentation of results, and showed that three varieties could marginally outperform Amadeus 77 under drier conditions, based on rainfall over the first 45 days after planting. The package sits in a wider software ecosystem around tricot, alongside ClimMob, ClimMobTools, PlackettLuce, climatrends and chirps, so the same functions serve trials across crops and countries. Its open-source code lets users request new functions and developers contribute, which keeps the toolkit aligned with the growing community of practice.

For new users, the paper doubles as a short tutorial on the full tricot analysis workflow, from raw data to reliability estimates, although function names should be checked against the current CRAN version. The example data ship with the package so the workflow can be practised end to end.

## Methods in brief

- **Data preparation.** rank_tricot, rank_numeric, set_binomialfreq, set_paircomp.
- **Model selection.** AIC, btpermute, crossvalidation (default 10-fold), pseudoR2, kendallTau, kendallW.
- **Interpretation.** reliability, regret, worth_map, worth_bar, compare, plot.
- **Example.** Common bean tricot trial with ten varieties, rainfall covariates from chirps and climatrends, Amadeus 77 as reference.

## Stated limitations

- The package wraps other packages (PlackettLuce, BradleyTerry2, psychotree), so results depend on them.
- The example is illustrative and its results are not presented as variety recommendations.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 3 of 10 | Varieties per farmer and total in the example trial | This paper |
| 10-fold | Default cross-validation | This paper |
| ≥0.5 | Reliability threshold used to present varieties in the example | This paper |

## Notes

- Function names and arguments change between versions. Always check the current CRAN reference manual before quoting code from the paper.
- Uses PlackettLuce (turner-2020-compstat), chirps (desousa-2020-joss) and climatrends (desousa-2023-joss).
