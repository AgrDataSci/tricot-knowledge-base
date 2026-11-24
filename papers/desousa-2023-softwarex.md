---
id: desousa-2023-softwarex
title: gosset. An R package for analysis and synthesis of ranking data in agricultural experimentation
authors: de Sousa K, Brown D, Steinke J, van Etten J
year: 2023
journal: SoftwareX
journal_short: SoftwareX
article: 22, 101402
type: software paper
source: team
peer_reviewed: yes
curated_card: yes
doi: https://doi.org/10.1016/j.softx.2023.101402
open_copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC10212778/
license: CC BY 4.0
data: nicabean dataset (tricot common bean trials, Nicaragua) distributed with the package. Code for v1.0 at https://github.com/ElsevierSoftwareX/SOFTX-D-22-00199 (MIT licence). Documentation at https://agrdatasci.github.io/gosset/
software: gosset, https://CRAN.R-project.org/package=gosset (v1.5.1 on CRAN, published 2025-11-19, checked 2026-10-30)
crops: common bean (example)
region: Nicaragua (example)
keywords: gosset, R package, ranking data, rank_tricot, Plackett-Luce, Bradley-Terry, reliability, regret, worth map, cross-validation, Kendall tau, tricot workflow
gist: gosset adds R functions missing from PlackettLuce and related packages to prepare, model and present ranking data, demonstrated on a common bean tricot trial in Nicaragua.
not_established: that the Nicaragua example results are variety recommendations; that the rainfall split is significant at the 5% level; that cross-validation, btpermute or regret were demonstrated in the example; that gosset was benchmarked against other software; that all trials run through ClimMob are analysed with gosset
relations:
  - usesMethodIn: eskridge-1992-tag  # the reliability function
  - usesMethodIn: turner-2020-compstat  # Plackett-Luce models and trees in the example
  - discusses: vanetten-2019-pnas  # cited as a study that used the methods
  - discusses: moyo-2021-fsufs  # cited as a study that used the methods
  - discusses: desousa-2021-commsbio  # cited as a study that used the methods
  - discusses: brown-2022-cropsci  # cited as a study that used the methods
  - discusses: alamu-2023-jsfa  # cited as a study that used the methods
  - discusses: gesesse-2023-pnas  # cited as a study that used the methods
  - discusses: woldeyohannes-2022-elife  # cited among studies that implemented the next steps
  - discusses: rutsaert-2023-mib  # cited as a study that used the methods
---

## Questions this paper answers

- How do I turn tricot data into rankings for PlackettLuce?
- Which tools exist to select covariates and evaluate ranking models?
- How do I compute reliability against a check variety, or regret?
- How do I visualize worth across traits and compare two traits?
- How can I find which traits drive farmers' overall appreciation of varieties?

## Summary

gosset supports the analysis and synthesis of ranking data in agricultural experiments, such as tricot trials and data synthesis studies. It is named after William Sealy Gosset, known by the pen name 'Student', who as a brewer at Guinness developed practical ways to compare barley varieties. gosset fills gaps between general ranking packages (PlackettLuce, BradleyTerry2 and psychotree) and the full workflow that agricultural researchers need.

Functions cover three stages. For data preparation, rank_tricot converts tricot best and worst data into PlackettLuce rankings, rank_numeric converts numeric measurements such as yield into rankings, and set_binomialfreq and set_paircomp convert rankings for Bradley-Terry models and Bradley-Terry trees. For model selection and evaluation, gosset offers AIC, deviance-based forward variable selection for Bradley-Terry models (btpermute), k-fold cross-validation with custom folds, Kendall's tau, Kendall's W and McFadden's pseudo-R². For presentation of results, it computes reliability, the probability that an item outperforms a reference item, and regret, the loss under the worst possible outcome. It also offers worth bar plots, a worth heat map across traits, a Bland-Altman plot comparing two traits, and a ggplot2 tree plot.

The illustrative example uses the nicabean dataset from tricot trials in Nicaragua over five seasons in 2015 and 2016. Each farmer tested three of ten common bean varieties and named the best and worst for eight traits and for overall appreciation. Kendall's tau between overall appreciation and each trait was highest for yield (0.749), taste (0.653) and marketability (0.639), read by the authors as the traits farmers prioritised. The authors suggest using this to pick at most four traits for a lighter tricot design. The example then links the yield rankings to total rainfall over the first 45 days after planting, from the chirps and climatrends packages, and fits one Plackett-Luce tree. The tree splits at 193.82 mm (p = 0.079, with alpha set to 0.1). Under drier conditions, three varieties could marginally outperform the check variety Amadeus 77 (reliability 0.506 to 0.519). ALS 0532-6 performs weakly in the full yield ranking but outperforms all other varieties under higher rainfall (reliability 0.630). compare() then shows that overall appreciation and yield do not fully agree. For SX 14825-7-1, the authors suggest that taste, marketability and disease resistance may explain its higher overall appreciation.

The authors stress reproducible and efficient workflows. They report that gosset supported data preparation, model validation and results presentation in several published studies. The example does not run cross-validation, btpermute or regret, which are listed as next steps. gosset is part of a software ecosystem built around ClimMob, which runs trials on more than 10,000 farms per year. Insights from the package help several breeding teams in Sub-Saharan Africa, and the Africa-wide 1000FARMS on-farm trial network supports further refinement of the methods.

The code is open source, so users can request new functions and developers can contribute. The authors expect the community of practice in on-farm experimentation to drive improvements. The example data ship with the package, so the workflow can be practised from ranked data to reliability estimates.

## Methods in brief

- **Data preparation.** rank_tricot, rank_numeric, set_binomialfreq, set_paircomp.
- **Model selection.** AIC, btpermute, crossvalidation (default 10-fold), pseudoR2, kendallTau, kendallW.
- **Interpretation.** reliability, regret, worth_map, worth_bar, compare, plot. node_labels, node_rules and top_items describe the splits and best items in a Plackett-Luce tree.
- **Example.** nicabean dataset: tricot trials of common bean in Nicaragua, five seasons (2015 to 2016), three of ten varieties per farmer, eight traits plus overall appreciation. Kendall's tau of each trait against overall appreciation. One Plackett-Luce tree for yield, with total rainfall over the first 45 days after planting (chirps, climatrends) as covariate and alpha = 0.1. Reliability against Amadeus 77. compare() of overall appreciation against yield.

## Stated limitations

- The paper has no limitations section.
- The authors call the example a simple illustration. For simplicity it uses only total rainfall as a covariate and shows only varieties with reliability of 0.5 or more (p. 3 to 4).
- Cross-validation, btpermute, regret and combining legacy data with rank_numeric are not run in the example. The authors list them as next steps that earlier studies implemented (p. 4).

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 3 of 10 | Varieties per farmer and total in the example trial | This paper |
| 10-fold | Default cross-validation | This paper |
| ≥0.5 | Reliability threshold used to present varieties in the example | This paper |
| 0.749, 0.653, 0.639 | Kendall's tau between overall appreciation and yield, taste and marketability (Table 1) | This paper |
| 193.82 mm | Total rainfall over the first 45 days after planting where the Plackett-Luce tree for yield splits (p = 0.079, alpha = 0.1) | This paper |
| 0.506 to 0.519 | Reliability of BRT 103-182, IBC 302-29 and SX 14825-7-1 against Amadeus 77, drier node (Table 2) | This paper |
| 0.630 and 0.565 | Reliability of ALS 0532-6 and SX 14825-7-1 against Amadeus 77, wetter node (Table 2) | This paper |
| 393 and 164 | Rankings in the drier and wetter nodes, read from Fig. 2 | This paper |
| 5 seasons | Nicaragua trials, 2015 to 2016 | This paper |
| >10,000 farms per year | Trials run through ClimMob | This paper |

## Notes

- The paper describes code version 1.0 (Code metadata, p. 1). Function names and arguments change between versions. Always check the current CRAN reference manual before quoting code from the paper.
- Uses PlackettLuce (turner-2020-compstat), chirps (desousa-2020-joss) and climatrends (desousa-2023-joss).
- The source cites climatrends as a 2020 CRAN entry [25]. The card desousa-2023-joss is the later JOSS paper on the same package.
- Source issue: the rainfall split in Fig. 2 has p = 0.079 and the tree was fitted with alpha = 0.1. The drier-node reliabilities (0.506 to 0.519, SE about 0.035) are close to 0.5. The authors call them marginal and do not discuss the weak split.
- Table 2 check (card's own calculation): reliability equals worth of the variety divided by the sum of its worth and the worth of Amadeus 77 in the same node. This reproduces all values in the table.
- Source issue: naming varies. Table 1 says "overall performance" where the text says "overall appreciation", and the Fig. 1 caption says "Amadeus" where the text says "Amadeus 77" (p. 3).
- Source issue: reference [23] (Loomes and Sugden, regret theory) gives the journal as "Econ J Nepal". It should be The Economic Journal (p. 6).
