---
id: nabateregga-2025-eja
title: Accuracy of farmer-generated yield estimations of common bean in decentralised on-farm trials in sub-Saharan Africa
authors: Nabateregga M, Dorado-Betancourt H, Solberg SØ, van Etten J, van Heerwaarden J, Gregory T, de Sousa K
year: 2025
journal: European Journal of Agronomy
journal_short: Eur J Agron
article: 170, 127730
type: research article
source: team
peer_reviewed: yes
curated_card: yes
doi: https://doi.org/10.1016/j.eja.2025.127730
open_copy: https://doi.org/10.1016/j.eja.2025.127730
license: CC BY
data: data and code on Zenodo, https://doi.org/10.5281/zenodo.15591106
crops: common bean
region: Tanzania (Kilindi, Karatu)
keywords: farmer-generated yield, yield estimation, volumetric measurement, sado tins, data accuracy, genetic gain, moisture content, tricot, absolute yield
gist: In Tanzania, farmer tin-volume yield estimates for common bean agreed closely with technician measures (r = 0.96) and predicted weighed yield, so tricot can supply yield data
not_established: a universal sample size for yield measurement; accuracy for smaller-seeded crops such as wheat, sorghum or millet, or for crops with repeated or piecemeal harvests; accurate yield per hectare where plot area is uncertain; representative variety yields from this sample; acceptance of farmer-measured yield by a release committee; an effect of literacy, which could not be tested
relations:
  - discusses: ulzen-2025-agrirxiv  # cited in this paper as Ulzen et al. (2024)
---

## Questions this paper answers

- Can farmers measure yield accurately enough for breeding decisions?
- How can tricot produce absolute yields, not just rankings?
- Does grain moisture distort farmer volumetric measurements?
- How many farmers are needed for reliable farmer-generated yield data?
- Do farmer age, gender or experience affect how accurately they measure yield?

## Summary

tricot relies mainly on farmer rankings. Rankings give relative performance but not the absolute yields that breeders need to measure genetic gain or to estimate economic returns on breeding investment. The study tests whether farmers can generate accurate yield data for common bean in decentralized on-farm trials, and which seed traits and farmer characteristics affect that accuracy.

The yield determination survey took place in 2022 with 30 farmers (24 men and 6 women) in Kilindi and Karatu districts in northern Tanzania. They were a non-random subset of the 355 farmers in a tricot trial of common bean varieties grown in 6 × 8 m plots. Farmers received a protocol two weeks before harvest. They dried the beans in the pods for two days, shelled them and sun-dried the grain for two more days. Farmers and extension officers (technicians) then measured each variety separately with 1 L sado tins, a common local container, levelled and not heaped. A researcher weighed the grain and measured moisture content and seed size.

Farmer and technician volumes correlated strongly (r = 0.96, p < 0.001). Farmer volume also correlated with researcher-weighed yield (r = 0.954), slightly less than technician volume did (r = 0.991). The mean difference in log-yield between farmers and technicians was close to zero, with a small tendency for farmers to underestimate. Moisture content explained only 11.9% of differences in grain density and weight. Farmer age, gender, eyesight and experience with extension services, farmer field schools or measuring volumes had no significant effect. Seed thickness and width interacted significantly with variety, but removing seed traits and variety cost little fit, so the final model kept farmer volume alone. Market class was not significant.

The final model predicts researcher-weighed yield from the number of tins (intercept 0.043, slope 0.884), with a random farm effect. In cross-validation with three folds and 100 repetitions, it explained about 90% of the variability in observed yield (R² 0.901), with a root mean square error of 0.233 and a mean absolute error of 0.133. In a simulation of 1000 farms generated from this model, R² stayed between 0.98 and 0.99 for training sets of 5 to 100 farms, and prediction error stabilised at about 25 farms.

Farmer-led estimates differentiated between varieties. Sweet Violet yielded most and RCB 593 least, for both farmers and technicians. The authors note that earlier studies reported inconsistent performance for these varieties, which may reflect genotype-by-environment interaction.

The authors conclude that farmer-generated yield data, collected with a standard protocol, can reliably inform breeding decisions. They see a cost-effective and scalable way to add yield to on-farm trials and accelerate variety turnover in sub-Saharan Africa, with fewer field visits than technician-measured yield requires. They caution that the sample was not random, so the yields do not represent overall variety performance. Common bean has large seeds and well-established harvest methods, and smaller-seeded crops such as wheat, sorghum or millet may be harder to measure. Plot area estimation and drop-out also need attention.

## Methods in brief

- **Survey.** 30 farmers (24 men, 6 women), a non-random subset of 355 tricot farmers, in Kilindi and Karatu districts of northern Tanzania, 2022. Three 6 × 8 m variety plots per farm.
- **Protocol.** Farmers got the protocol two weeks before harvest, harvested each plot separately, dried pods two days in the field, then shelled and sun-dried the grain two more days. Farmers and technicians measured separately with levelled 1 L sado tins on a flat surface.
- **Measurements.** Farmer and technician volumes with sado tins, researcher mass and moisture.
- **Analysis.** Pearson correlation, Wilcoxon signed-rank test and Bland-Altman agreement on log volumes. A linear mixed model with step-down feature selection tested seed traits (moisture, thickness, width, length) and farmer traits (age, gender, eyesight, literacy, experience). A mixed model with farm as random effect converted farmer volume to weighed yield, checked by farm-level cross-validation (3 folds, 100 repetitions). A simulation of 1000 farms tested training sizes from 5 to 100 farms.

## Stated limitations

- The 30 farmers were a non-random sample from a larger trial, so the yields do not represent overall variety performance.
- Only six women took part, which limits the test of gender effects.
- Common bean has large seeds and well-established harvest methods. Smaller-seeded crops such as wheat, sorghum or millet may be harder to measure because of seed size, threshing and moisture variability.
- Yield per hectare depends on accurate plot area, which is hard to estimate on irregular smallholder plots.
- Researcher weighing can also be biased (scale intervals, faulty scales, taring), and drop-out of participants must be planned for.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 30 farmers (24 men, 6 women) | Yield determination survey, 2022 | This paper |
| r = 0.96 | Correlation between farmer and technician volumes | This paper |
| r = 0.954 | Correlation between farmer tin volume and researcher-weighed yield (technician volume r = 0.991) | This paper |
| 14.5%–16.0% | Spread of genotype moisture content (Fig. 6). Individual readings ranged more widely, roughly 11.5% to 19.5% (Fig. 5, read from chart) | This paper |
| 11.9% | Differences in density and weight explained by moisture | This paper |
| 0.901 | Cross-validated R² of the model predicting weighed yield from farmer volume | This paper |
| 0.884 | Slope of weighed yield on farmer tin count in the final mixed model (units unclear, see Notes) | This paper |
| <5% | Loss of goodness of fit when seed-trait predictors were dropped from the reduced model (R²m 0.923 to 0.898, R²c 0.956 to 0.912) | This paper |
| 25 farms | Training-set size at which prediction error (RMSE) stabilised in a simulation of 1000 farms generated from the model. R² was 0.98 to 0.99 from 5 farms upward | This paper |

## Notes

- Answers the yield concern raised in desousa-2024-asd, which reports farmer-led yield methods as still being tested with preliminary results. cairns-2026-jxb cites this study. ulzen-2025-agrirxiv reports similar results for tin measurement of maize and cocoa in Ghana. This paper cites Ulzen et al. (2024) as finding that location, eyesight, education and experience affected farmers' heap volume estimates, in contrast to its own tin results. The curator confirms that this reference is the agriRxiv preprint carded as ulzen-2025-agrirxiv and that the citation is in error.
- Source issue: the simulation R² values (0.98 to 0.99) are cited to Fig. 6 in the text but shown in Fig. 7.
- Source issue: the text gives the agreement limits as mean ± 0.5 SD, but the Fig. 4 caption says ± 2 SD.
- Source issue: units of the final model are unclear. Table 5 says t/ha, but yield was weighed in kg per 6 × 8 m plot and volume counted in tins. Treat the slope (0.884) and RMSE (0.233) as per-plot values with uncertain units.
- Source issue: Table 1 potential yields look like a numbering error, and variety names differ between Table 1 and the figures. Do not cite Table 1 yields.
- Source issue: the 11.9% moisture figure comes from an R² of 0.119 whose model is not clearly described.
- Source issue: the Fig. 7 caption says 1000 runs, but the Methods say 100 replications per sample size. Gloria and NUA 48 are said not to be in the yield sample, yet Fig. 2 and Fig. 5 show values for them.
