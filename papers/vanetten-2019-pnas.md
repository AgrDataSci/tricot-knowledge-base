---
id: vanetten-2019-pnas
title: Crop variety management for climate adaptation supported by citizen science
authors: van Etten J, de Sousa K, Aguilar A, Barrios M, Coto A, Dell'Acqua M, Fadda C, Gebrehawaryat Y, van de Gevel J, Gupta A, Kiros AY, Madriz B, Mathur P, Mengistu DK, Mercado L, Mohammed JN, Paliwal A, Pè ME, Quirós CF, Rosas JC, Sharma N, Singh SS, Solanki IS, Steinke J
year: 2019
journal: Proceedings of the National Academy of Sciences (PNAS)
journal_short: PNAS
article: 116(10), 4194-4199
type: research article
source: team
peer_reviewed: yes
curated_card: yes
doi: https://doi.org/10.1073/pnas.1813720116
open_copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC6410884
license: CC BY-NC-ND 4.0
data: https://doi.org/10.7910/DVN/4ICF6W (Harvard Dataverse); code in SI Appendix
crops: common bean, durum wheat, bread wheat
region: Nicaragua, Ethiopia, India
keywords: tricot, citizen science, Plackett-Luce trees, climate adaptation, variety recommendation, seasonal forecast, worst regret, ClimMob
gist: Large tricot trials (12,409 plots, 3 countries) show farmer rankings capture known climate effects on varieties and can improve variety recommendations
not_established: effects on farmer income, food security or adoption; acceptance of tricot data in official variety release; that tricot trials caused the 2017 Ethiopian variety releases; gains from real (not perfect) seasonal forecasts; yield gains (farmers ranked relative performance, the paper reports no yield data); that tricot outperforms a combination of conventional trial methods
relations:
  - extends: mancini-2017-scirep  # Ethiopian case builds on the genebank-to-farm work, per the team
---

## Questions this paper answers

- Can farmer rankings from tricot reveal how varieties respond to climate?
- Which climate variables drive variety performance for bean and wheat?
- How can seasonal forecasts and risk (worst regret) improve recommendations?
- How do tricot-based recommendations compare with official ones?

## Summary

The paper asks whether crowdsourced citizen science can generate data good enough to characterize how crop varieties respond to climate, and to improve variety recommendations in marginal environments where conventional trials scale poorly. The authors call it a participatory variety evaluation dataset of large size and scope. Each farmer received three randomly assigned varieties and ranked them, a format low-literacy farmers can handle and mobile phones can capture.

The data cover 12,409 farmer-managed plots across three cases, common bean in Nicaragua, durum wheat in Ethiopia and bread wheat in India, collected from 2012 to 2016. Plots were linked to climate and soil data by coordinates and planting date and analyzed with Plackett-Luce trees, which split the data by the covariates that best explain shifts in variety rankings.

Climate variables explained rankings slightly better than design variables such as location, season or soil, and adding geolocation slightly lowered fit. In each case the model selected one temperature variable that matches known agronomy. Bean rankings shifted above 18.7 °C maximum night temperature, close to the published heat-stress threshold, and three known heat-tolerant varieties beat the local variety above it (a fourth, SJC 730-79, did not). Durum wheat responded to cold nights below 8.4 °C, consistent with vernalization thresholds, and cold-adapted varieties came from higher elevations. Bread wheat responded to diurnal temperature range. The authors link model fit mainly to varietal diversity. Fit was highest in Ethiopia, where farmer and modern varieties were mixed, and lowest in India, where the set was narrow and modern.

The authors show four ways climate analysis improves recommendations. Averaging predictions over a 15-year base period corrects for the climate of the trial seasons. Perfect seasonal forecasts raised predictive fit more than bias correction alone, though realistic forecast skill remains untested. Ranking varieties by worst regret instead of probability of winning gives different, risk-averse choices. Maps of predicted winners cut across administrative and agroecological boundaries.

The resulting recommendations departed from official ones. In Nicaragua, the two catalogue varieties recommended for the study area performed worse than local ones, and heat-tolerant lines recommended only for warmer zones fit the study area. In Ethiopia, tricot gave location-specific choices where the CIMMYT Wheat Atlas treated the highlands as one mega-environment. The results agreed with the 2017 release approval of two farmer varieties, which rested on other field trials. In India, the older K 9107 matched or beat the promoted HD 2967. The tricot-recommended variety beat the best earlier recommendation with a probability of 0.51 to 0.65.

The paper positions tricot as a scalable, demand-led way to track climate on farms, feed seasonal forecast services and variety portfolios, and support decentralized breeding, provided institutions and partners commit to it. The authors concede that combining existing methods could arguably give similar results, but tricot joins them in one simple, scalable format.

## Methods in brief

- **Trials.** tricot in Nicaragua (842 plots, 5 seasons), Ethiopia (1,090, 3 seasons) and India (10,477, 4 seasons), 2012–2016 overall. Varieties allocated at random as incomplete blocks with spatial balance, three per farm (four in Ethiopia). Field agents collected rankings by farm visits, first on paper and later through ClimMob.
- **Covariates.** Seasonal agroclimatic variables (temperature from land-surface data) and soil variables, linked by coordinates and planting date. The full list is in the SI Appendix.
- **Model.** Plackett-Luce trees, with 10-fold cross-validated pseudo-R² to compare covariate sets.
- **Recommendations.** Predictions over a 15-year base period, perfect-forecast scenario, probability of winning and worst regret, maps of top varieties.

## Stated limitations

- Perfect-forecast gains are an upper bound, as real forecast skill was not tested.
- Fit was low in India, where the variety set was narrow and modern.
- Land-surface temperature was used rather than air temperature, which shifts thresholds.
- The authors concede that a combination of existing approaches (environment characterization, multilocation trials, participatory selection, dissemination) could arguably give similar results.
- Scaling needs new institutional arrangements and wide collaboration, not only more farmers.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 12,409 plots | Total farmer-managed tricot plots analyzed | This paper |
| 842 / 1,090 / 10,477 | Plots in Nicaragua (bean) / Ethiopia (durum wheat) / India (bread wheat) | This paper |
| 2012–2016 | Overall trial window for all three countries (5 seasons Nicaragua, 3 Ethiopia, 4 India). Years per country are in SI Table S1, not in this PDF | This paper |
| 3 (4 in Ethiopia) | Varieties per farm | This paper |
| 0.1978 / 0.4870 / 0.0882 | Cross-validated pseudo-R² of best (climate) model, Nicaragua / Ethiopia / India | This paper |
| 18.7 °C | Max night temperature threshold shifting bean rankings (vs 20 °C air-temperature threshold) | This paper; Rainey and Griffiths 2005 |
| 8.4 °C | Min night temperature threshold for durum wheat, consistent with vernalization | This paper; Fowler 2008 |
| 2,483 ± 113 m vs 2,101 ± 485 m | Origin elevation of cold-adapted vs cold-sensitive durum varieties | This paper |
| 14.5 °C / 15.7 °C | Diurnal temperature range splits for bread wheat | This paper |
| 2002–2016 | 15-year base period for climate bias correction | This paper |
| 0.58–0.60 / 0.59–0.65 / 0.51–0.62 | Reliability (probability of beating the best variety from previous recommendations) of the tricot-recommended variety across locations, Nicaragua / Ethiopia / India (SI Fig. S4) | This paper |

## Notes

- The text names farmer varieties 8208 and 208304 as approved for release in March 2017 (p. 4197). 8208 appears nowhere else in the paper. Table 3 and Fig. 3B list 8034 instead. Check the SI or Dataverse before citing the variety name.
- Problem in the source: the text says Table 3 confirms the "superiority" of these farmer varieties, but in Table 3 both 208304 (0.041) and 8034 (0.030) have a lower probability of winning than 208279 (0.059) and the modern variety Hitosa (0.049). They rank above Ude and 222360 only (p. 4197).
- Trial years: the paper gives only an overall trial window (2012 to 2016) and the number of seasons per country (5 Nicaragua, 3 Ethiopia, 4 India). Years per country are in SI Appendix Table S1, which is not in our PDF. desousa-2023-joss dates the Nicaragua bean data to five seasons from 2015 to 2017, which does not fit this window. Check SI Table S1 or the Dataverse files before citing years for one country.
- Perfect-forecast gains are an upper bound. The paper does not test real forecast skill.
