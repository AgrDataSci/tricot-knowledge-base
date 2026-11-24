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
region: Western Kenya (Siaya County)
keywords: on-farm trials, yield gap, external validity, farmer selection, selection bias, behavioural response, attrition, value-cost ratio, fertilizer, input packages, adoption, smallholders
gist: In Kenyan on-farm trials, correcting for farmer and plot selection, management and yield calculation made the soybean package's gain non-significant but left the maize gain intact
not_established: that trial yield gains are always overestimated (adjustments went in opposite directions for the two crops); that the 30% and 52% yield drops from the calculation adjustment apply to yield gains (the maize gain barely changed); findings for variety comparisons (the maize variety contrasts were not analysed); that labour costs would not change the profitability results (labour was not costed, so ratios are upper bounds); that the soybean package fails for all farmers (47% still profited after adjustments)
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

They used IITA fertilizer and inoculant trials for maize and soybean with 336 farmers in 48 villages of Siaya County, Western Kenya, over three seasons. Researchers designed the trials, supplied inputs and led planting, fertilizing and harvest, while farmers managed the plots. As is common, communities nominated five "good farmers" per village to host trials. The authors added the same number of randomly selected households. They collected detailed data on management and effort on trial and neighbouring non-trial plots, soil samples from trial plots, and farmers' skills and wealth.

They identify five discrepancies between trial estimates and real-life returns: yield calculation choices, better management on trial plots, plot selection, farmer selection, and dropout in multi-season trials.

They regress yield increments on these factors and predict the increment for representative farmers, weighting about 94% on the randomly selected ones. Reinserting failed plots and removing density adjustments cut average yields by 30% for maize and 52% for soybean. The soybean gain fell by about the same share, but the maize gain hardly changed, because fertilized maize plots kept more plants (91% of stands against 79% in control plots). Trial plots were managed better than any other plot of the same farmers, and moving management to farmers' usual level always lowered the predicted gain. Soil adjustments raised the maize gain but lowered the soybean gain. Skills and wealth added no sizeable effect. After all adjustments, the maize package's gain was nearly unchanged, while the soybean package's gain fell to not significantly different from zero. A fixed rule-of-thumb discount could therefore wrongly keep some packages and wrongly drop others.

The maize package kept an average value-cost ratio around 4, with about 85% of farmers covering input costs. The best soybean package looked highly profitable before adjustments (ratio about 12) but fell to about 0.6 after all adjustments, and was profitable for only 47% of farmers. Labour was not costed, so these ratios are upper bounds. Attrition mattered too, as only 33% (maize) and 41% (soybean) of farmers stayed all three seasons, and keeping only them would have overstated gains by 28% and 64%.

The method assumes farmers would manage a new package like their best-managed other plot, so it cannot capture further changes after adoption. A review of 16 on-farm trial papers from 2018 found random farmer selection was rare and none corrected for dropout. The authors conclude that agronomists should be cautious in extrapolating from trials, report results with and without calculation adjustments, document heterogeneity, and state how farmers and plots were selected. Pointing to designs such as mother-baby trials, they suggest that testing innovations early under real-world conditions, without researcher interference, might help identify which ones are likely to be taken up at scale.

## Methods in brief

- **Trials.** IITA researcher-designed, farmer-managed trials in Siaya County, Western Kenya, over three seasons (2014 to 2015). Each farm had six 4.5 × 5 m plots, one replicate, in a full factorial design. Best-bet packages: Mavuno fertilizer, top dressing and Phymix for maize (with local, IR or hybrid seed), and rhizobia inoculant with Sympal or Minjingu P fertilizer for soybean. A researcher led planting, fertilizer application and harvest. Farmers did land preparation and weeding, checked weekly by a village contact person.
- **Sampling.** 48 villages drawn at random (stratified by sub-county), 10 farmers per village: five nominated by the community and five drawn at random from the village household list. Four farmers per village ran maize trials and three ran soybean trials (336 in total). The other three ran a maize-soybean intercrop trial that was contaminated and left out of the main analysis. Non-trial plots next to the trial plot, and farmers' best-managed other plots, were used to observe usual practice.
- **Data.** Surveys and direct observation by agronomists and local contacts on yields, management, effort, soils (soil samples), skills and assets.
- **Analysis.** Yield increments (package minus control plot) averaged over three seasons, with missed seasons imputed. Backward stepwise regressions of yield increment on management, soil, plot and farmer variables (adjusted R² as criterion, standard errors clustered by household), then predictions for representative farmers using village-size weights (about 94% on randomly selected farmers). Value-cost ratios from input costs and farmers' reported crop sale prices (labour excluded).

## Stated limitations

- Labour costs are not included in value-cost ratios and profits.
- Observed variables explain only part of the variation in yield increment (adjusted R² 19 to 26%, R² 23 to 35%), though many adjustments still lead to significant differences.
- Any experiment that asks random farmers to grow a package also creates a trial, so real-life conditions cannot be observed directly. The paper uses a decomposition instead.
- The authors do not claim these factors are the only reason for low adoption.
- The method assumes farmers would manage a new package like their best-managed other plot. It cannot capture further changes in practice, or deliberate choice of the most responsive plots, after real adoption. The estimates matter less where farmers can overcome their constraints, or in the long run.
- Soil samples exist only for trial plots, so differences between trial and non-trial plots are corrected only through survey plot characteristics, and parcel selection only partly.
- Causes of crop failure were known for only about half of the cases, so all failures were treated alike.
- Replicating the full approach needs particular selection rules, extra data and large samples. Reporting results with and without calculation adjustments is always feasible.
- The maize-soybean intercrop trial was contaminated (no plot received the best-bet package) and is reported only in the supplement.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 336 / 48 | Farmers / villages in the trials | This paper |
| 5 | Community-nominated farmers per village | This paper |
| ~94% | Average weight on randomly selected farmers in the representative predictions | This paper |
| 30% / 52% | Drop in maize / soybean yield after removing density adjustment and reinserting failed plots | This paper |
| 71% / 88% | Share of the maize / soybean yield drop due to the plant density adjustment | This paper |
| 91% / 79% | Maize stands surviving in fertilized / control plots, which is why the calculation adjustment barely changed the maize gain | This paper |
| 15% / 33% | Average missing stands in maize / soybean trials | This paper |
| ~11% / ~12% | Maize / soybean plots excluded as hazards in yield-potential calculations | This paper |
| 1,061 → 1,151 / 692 → 33 kg/ha | Predicted maize / soybean yield increment, agronomic calculation versus after all adjustments (data labels in Fig. 1) | This paper |
| ~4 / ~12 | Average value-cost ratio of maize / best soybean package before adjustments (Table 1: 3.9 / 12.5) | This paper |
| 3.9 / 4.0 / 4.2 | Maize value-cost ratio: agronomic calculation / without calculation adjustment / after all adjustments (Table 1) | This paper |
| 12.5 / 6.3 / 0.6 | Soybean value-cost ratio at the same three steps (Table 1, text gives 12 and 0.59) | This paper |
| 85% vs 47% | Farmers whose adjusted gain covers input costs, maize vs soybean | This paper |
| 33% / 41% | Farmers completing all three seasons, maize / soybean | This paper |
| 28% / 64% | Overestimate of maize / soybean increment if only completers were kept | This paper |
| 16 | On-farm trial papers from 2018 reviewed for the five discrepancies | This paper |
| 5-30% | Rule-of-thumb gap between attainable and potential yield in trial guidelines | Sadras et al. 2015 (FAO Water Report 41) and CIMMYT 1988, as cited in this paper (refs 12, 26) |

## Notes

- An agronomy study, not a variety trial. The authors say the same logic could be applied to other trials (p. 7). The mechanisms (selected host farmers, researcher influence, dropout) are likely relevant to variety testing too, but the paper does not test this. Use it with cairns-2025-ppp and cairns-2026-jxb on representative host-farmer sampling.
- Supports the tricot argument for testing under farmers' own management with many farms (vanetten-2019-expagric, desousa-2024-asd), but the paper does not discuss tricot.
- The paper discusses mother-baby trials (Snapp et al., ref. 39 of the paper) as participatory designs that measure returns under farmers' conditions, but does not mention tricot.
- The maize trials also compared local, IR and hybrid seed, but the authors did not analyse variety effects because differences between seeds were small and statistical power was low (p. 11).
- Source issue: the text gives the soybean value-cost ratio before adjustments as 12 for the best package (p. 5), while Table 1 shows 12.5 in a single soybean column (p. 6). This card uses about 12.
- Source issue: minor typos in the methods (p. 8 to 9). A potassium threshold is written as "pH < 0.160", Phymix pH is given as "6.7%", and the farmer allocation calls both groups "random" ("4 random farmers (2 random and 2 selected)"). The farmer numbers still add up to 336.
- See kool-2020-expagric for a review of how rarely on-farm studies define their research population.
