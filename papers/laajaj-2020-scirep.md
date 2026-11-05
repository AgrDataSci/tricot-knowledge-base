---
id: laajaj-2020-scirep
title: Reconciling yield gains in agronomic trials with returns under African smallholder conditions
authors: Laajaj R, Macours K, Masso C, Thuita M, Vanlauwe B
year: 2020
journal: Scientific Reports
journal_short: Sci Rep
article: 10, 14286
type: research article
source: external
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1038/s41598-020-71155-y
open_copy: https://doi.org/10.1038/s41598-020-71155-y
license: CC BY 4.0
data: data and code on openICPSR, https://www.openicpsr.org/openicpsr/project/120430/version/V1/view (Stata 16)
crops: maize, soybean
region: Western Kenya
keywords: on-farm trials, yield gap, external validity, farmer selection, selection bias, behavioural response, attrition, value-cost ratio, fertilizer, input packages, adoption, smallholders
gist: In Kenyan fertilizer trials, correcting for farmer and plot selection, management and yield calculation wiped out the soybean package's gain but left the maize gain intact
not_established: that trial yield gains are always overestimated (adjustments went in opposite directions for the two crops); findings for variety trials; that labour costs would not change the profitability results (labour was not costed)
---

## Questions this paper answers

- Why do yield gains in on-farm trials often fail to appear when smallholders adopt the same inputs?
- How does choosing "good farmers" to host trials bias the results?
- Do farmers manage trial plots differently from their other plots?
- How much do yield calculation choices (plant density adjustment, dropping failed plots) change the estimated gain?
- Does farmer dropout in multi-season trials inflate results?
- How should trials be designed to predict real-world returns?

## Summary

Agronomic trials often promise large yield gains from new inputs, yet adoption stays low and gains on farmers' own fields fall short. Rachid Laajaj, Karen Macours and IITA colleagues quantify why, focusing on how trials are run and analysed rather than on market constraints.

They used IITA fertilizer and inoculant trials for maize and soybean with 336 farmers in 48 villages of Western Kenya, run over three seasons. Researchers designed the trials and supplied inputs, and farmers managed them. As is common, communities nominated five "good farmers" per village to host trials. The authors added a comparable number of randomly selected households and collected detailed data on soils, management, effort, skills and wealth on trial and non-trial plots.

They identify five discrepancies between trial estimates and real-life returns. Yield calculations correct for missing plants and drop failed plots. Management and effort differ on trial plots. Farmers choose plots that differ from their usual ones. Selected farmers differ in skills and assets. And in multi-season trials, those who stay may be those who do well.

They regress yield increments on these factors and predict the increment for representative farmers, weighting about 94% on the randomly selected ones. Reinserting failed plots and removing density adjustments cut average yields by 30% for maize and 52% for soybean. After all adjustments, the maize package's gain was nearly unchanged, while the soybean package's gain fell to not significantly different from zero. Soil adjustments moved the two crops in opposite directions, so a fixed rule-of-thumb discount would be wrong in both directions.

Profitability followed. The maize package kept a value-cost ratio around 4, with about 85% of farmers covering input costs. The soybean package looked highly profitable before adjustments (ratio about 12) but was profitable for only 47% of farmers afterwards. Attrition mattered too, as only 33% (maize) and 41% (soybean) of farmers stayed all three seasons, and keeping only them would have overstated gains by 28% and 64%.

The authors conclude that agronomists should be cautious in extrapolating from trials, should report yields without density corrections and with failed plots, document heterogeneity, and test innovations early under real-world conditions, with randomly selected farmers and without researcher interference, to identify which ones are likely to be taken up at scale.

## Methods in brief

- **Trials.** IITA researcher-designed, farmer-managed factorial trials comparing best-bet fertilizer and inoculant packages with control plots, three seasons, Western Kenya.
- **Sampling.** Five community-nominated farmers per village plus a comparable number drawn at random from village household lists. Non-trial plots near the trial plot, with the same crop, used to observe usual practice.
- **Data.** Surveys and direct observation by agronomists and local contacts on yields, management, effort, soils (soil samples), skills and assets.
- **Analysis.** Regressions of yield increment on management, soil and farmer characteristics, then predictions for representative farmers using village weights. Value-cost ratios from input costs (labour excluded).

## Stated limitations

- Labour costs are not included in value-cost ratios and profits.
- Observed variables explain only part of the variation in yield increment (R² roughly 19-35%).
- Any experiment that asks random farmers to grow a package also creates a trial, so real-life conditions cannot be observed directly. The paper uses a decomposition instead.
- The authors do not claim these factors are the only reason for low adoption.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 336 / 48 | Farmers / villages in the trials | This paper |
| 5 | Community-nominated farmers per village | This paper |
| ~94% | Average weight on randomly selected farmers in the representative predictions | This paper |
| 30% / 52% | Drop in maize / soybean yield after removing density adjustment and reinserting failed plots | This paper |
| 15% / 33% | Average missing stands in maize / soybean trials | This paper |
| ~11% / ~12% | Maize / soybean plots excluded as hazards in yield-potential calculations | This paper |
| ~4 / ~12 | Value-cost ratio of maize / best soybean package before adjustments | This paper |
| 85% vs 47% | Farmers whose adjusted gain covers input costs, maize vs soybean | This paper |
| 33% / 41% | Farmers completing all three seasons, maize / soybean | This paper |
| 28% / 64% | Overestimate of maize / soybean increment if only completers were kept | This paper |
| 5-30% | Rule-of-thumb gap between attainable and potential yield in trial guidelines | Cited in this paper |

## Notes

- An agronomy study, not a variety trial, but the mechanism (selected host farmers, researcher influence, dropout) applies to any on-farm testing. Use it with cairns-2025-ppp and cairns-2026-jxb on representative host-farmer sampling.
- Supports the tricot argument for testing under farmers' own management with many farms (vanetten-2019-expagric, desousa-2024-asd), but the paper does not discuss tricot.
- See kool-2020-expagric for a review of how rarely on-farm studies define their research population.
