---
id: vanetten-2019-pnas
title: Crop variety management for climate adaptation supported by citizen science
authors: van Etten J, de Sousa K, Aguilar A, Barrios M, Coto A, Dell'Acqua M, Fadda C, Gebrehawaryat Y, van de Gevel J, Gupta A, Kiros AY, Madriz B, Mathur P, Mengistu DK, Mercado L, Mohammed JN, Paliwal A, Pè ME, Quirós CF, Rosas JC, Sharma N, Singh SS, Solanki IS, Steinke J
year: 2019
journal: Proceedings of the National Academy of Sciences (PNAS)
journal_short: PNAS
article: 116(10), 4194-4199
type: research article
doi: https://doi.org/10.1073/pnas.1813720116
open_copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC6410884
license: CC BY-NC-ND 4.0
data: https://doi.org/10.7910/DVN/4ICF6W (Harvard Dataverse); code in SI Appendix
crops: common bean, durum wheat, bread wheat
region: Nicaragua, Ethiopia, India
keywords: tricot, citizen science, Plackett-Luce trees, climate adaptation, variety recommendation, seasonal forecast, worst regret, ClimMob
gist: First large tricot test (12,409 plots, 3 countries) showing farmer rankings capture climate effects and improve variety recommendations
relations:
  - extends: mancini-2017-scirep  # Ethiopian case builds on the genebank-to-farm work, per the team
---

## Questions this paper answers

- Can farmer rankings from tricot reveal how varieties respond to climate?
- Which climate variables drive variety performance for bean and wheat?
- How can seasonal forecasts and risk (worst regret) improve recommendations?
- How do tricot-based recommendations compare with official ones?

## Summary

The paper asks whether crowdsourced citizen science can generate data good enough to characterize how crop varieties respond to climate, and to improve variety recommendations in marginal environments where conventional trials scale poorly. It is the first large-scale test of tricot. Each farmer received three randomly assigned varieties and ranked them, a format low-literacy farmers can handle and mobile phones can capture.

The data cover 12,409 farmer-managed plots across three cases, common bean in Nicaragua, durum wheat in Ethiopia and bread wheat in India, collected from 2012 to 2016. Plots were linked to climate and soil data by coordinates and planting date and analyzed with Plackett-Luce trees, which split the data by the covariates that best explain shifts in variety rankings.

Climate variables explained rankings better than design variables such as location, season or soil, and adding geolocation added nothing. In each case the model selected one temperature variable that matches known agronomy. Bean rankings shifted above 18.7 °C maximum night temperature, close to the published heat-stress threshold, and heat-tolerant lines beat the local variety above it. Durum wheat responded to cold nights below 8.4 °C, consistent with vernalization thresholds, and cold-adapted varieties came from higher elevations. Bread wheat responded to diurnal temperature range. Model fit tracked varietal diversity. It was highest in Ethiopia, where farmer and modern varieties were mixed, and lowest in India, where the set was narrow and modern.

The authors show four ways climate analysis improves recommendations. Averaging predictions over a 15-year base period corrects for the climate of the trial seasons. Perfect seasonal forecasts raised predictive fit more than bias correction alone, though realistic forecast skill remains untested. Ranking varieties by worst regret instead of probability of winning gives different, risk-averse choices. Maps of predicted winners cut across administrative and agroecological boundaries.

The resulting recommendations departed from official ones. In Nicaragua, catalogue varieties performed worse than local ones, and heat-tolerant lines recommended only for warmer zones fit the study area. In Ethiopia, tricot gave location-specific choices where the CIMMYT Wheat Atlas treated the highlands as one mega-environment, and two farmer varieties went on to official release. In India, the older K 9107 matched or beat the promoted HD 2967.

The paper positions tricot as a scalable, demand-led way to track climate on farms, feed seasonal forecast services and variety portfolios, and support decentralized breeding, provided institutions and partners commit to it. These results laid the basis for climate-informed recommendations from tricot.

## Methods in brief

- **Trials.** Tricot in Nicaragua (842 plots), Ethiopia (1,090) and India (10,477), 2012–2016, three varieties per farm (four in Ethiopia).
- **Covariates.** Climate (land-surface temperature, rainfall) and soil variables linked by coordinates and planting date.
- **Model.** Plackett-Luce trees, with 10-fold cross-validated pseudo-R² to compare covariate sets.
- **Recommendations.** Predictions over a 15-year base period, perfect-forecast scenario, probability of winning and worst regret, maps of top varieties.

## Stated limitations

- Perfect-forecast gains are an upper bound, as real forecast skill was not tested.
- Fit was low in India, where the variety set was narrow and modern.
- Land-surface temperature was used rather than air temperature, which shifts thresholds.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 12,409 plots | Total farmer-managed tricot plots analyzed | This paper |
| 842 / 1,090 / 10,477 | Plots in Nicaragua (bean) / Ethiopia (durum wheat) / India (bread wheat) | This paper |
| 2012–2016 | Trial period (5 seasons Nicaragua, 3 Ethiopia, 4 India) | This paper |
| 3 (4 in Ethiopia) | Varieties per farm | This paper |
| 0.1978 / 0.4870 / 0.0882 | Cross-validated pseudo-R² of best (climate) model, Nicaragua / Ethiopia / India | This paper |
| 18.7 °C | Max night temperature threshold shifting bean rankings (vs 20 °C air-temperature threshold) | This paper; Rainey and Griffiths 2005 |
| 8.4 °C | Min night temperature threshold for durum wheat, consistent with vernalization | This paper; Fowler 2008 |
| 2,483 ± 113 m vs 2,101 ± 485 m | Origin elevation of cold-adapted vs cold-sensitive durum varieties | This paper |
| 14.5 °C / 15.7 °C | Diurnal temperature range splits for bread wheat | This paper |
| 2002–2016 | 15-year base period for climate bias correction | This paper |
| 0.58–0.65 | Reliability (probability of beating the previous best check) of tricot-recommended varieties, Nicaragua and Ethiopia (India 0.51–0.62) | This paper |

## Notes

- Text names farmer varieties 8208 and 208304 as released in 2017, but Table 3 lists 8034. Check the PDF before citing.
- Perfect-forecast gains are an upper bound. The paper does not test real forecast skill.
