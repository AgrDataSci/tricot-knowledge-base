# Card review: nabateregga-2025-eja

- **Card:** papers/nabateregga-2025-eja.md
- **Source:** papers-pdf/nabateregga-et-al-2025.pdf (10 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 51 |
| Supported | 33 |
| Imprecise | 13 |
| Not in source | 2 |
| Contradicted | 3 |
| Source issues (problems in the source itself, not card errors) | 10 |
| Important omissions | 4 |
| Metadata issues | 2 |

The card gets the headline right (r = 0.96, near-zero mean difference, R² 0.901 in cross-validation). But one main result is attributed wrongly in both the Summary and Key numbers: the "less than 5%" loss is the drop in model fit when seed traits are removed (p. 5), not a loss under validation. The Summary also adds outside claims (release committees, researcher visits as the main expense, de Sousa et al. 2024 recommending a yield question), the Notes say desousa-2024-asd cites this study when it predates it, and the card omits the authors' key caveat that the 30 farmers were a non-random sample (p. 8). The Summary reads as two drafts joined together (the conclusion paragraph comes before more results and R² 0.901 appears twice), so a full replacement Summary is given below.

## Fixes needed

1. **"Less than 5%" attributed to validation (Contradicted).** Card Summary: "with a loss of performance under validation of less than 5%". Key numbers: "<5% | Loss of predictive performance under validation". Source p. 5: the reduced model had R²m 0.923 and R²c 0.956. A simpler model without the seed-trait (intrinsic) predictors gave R²m 0.898 and R²c 0.912, which the authors call a loss of less than 5%. Cross-validation (p. 6, Table 4) reports no "loss". Recomputed: (0.923 − 0.898)/0.923 = 2.7% and (0.956 − 0.912)/0.956 = 4.6%. Replace the Key numbers row with:
   `| <5% | Loss of goodness of fit when seed-trait predictors were dropped from the reduced model (R²m 0.923 to 0.898, R²c 0.956 to 0.912) | This paper |`
   The Summary fix is in item 2.

2. **Replace the whole Summary.** The present Summary has the error in item 1, outside knowledge (items 3 and 4), a moisture range stated at the wrong level (item 5), "subsampling" for what is a simulation (item 6), and it misses the non-random sample, the farmer-versus-weighed correlation and the drying and measuring protocol. It also repeats R² 0.901 and places the conclusion before more results. Suggested replacement (498 words, within 400 to 500):

   > tricot relies mainly on farmer rankings. Rankings give relative performance but not the absolute yields that breeders need to measure genetic gain or to estimate economic returns on breeding investment. The study tests whether farmers can generate accurate yield data for common bean in decentralized on-farm trials, and which seed traits and farmer characteristics affect that accuracy.
   >
   > The yield determination survey took place in 2022 with 30 farmers (24 men and 6 women) in Kilindi and Karatu districts in northern Tanzania. They were a non-random subset of the 355 farmers in a tricot trial of common bean varieties grown in 6 × 8 m plots. Farmers received a protocol two weeks before harvest. They dried the beans in the pods for two days, shelled them and sun-dried the grain for two more days. Farmers and extension officers (technicians) then measured each variety separately with 1 L sado tins, a common local container, levelled and not heaped. A researcher weighed the grain and measured moisture content and seed size.
   >
   > Farmer and technician volumes correlated strongly (r = 0.96, p < 0.001). Farmer volume also correlated with researcher-weighed yield (r = 0.954, Fig. 3A), slightly less than technician volume did (r = 0.991). The mean difference in log-yield between farmers and technicians was close to zero, with a small tendency for farmers to underestimate. Moisture content explained only 11.9% of differences in grain density and weight. Farmer age, gender, eyesight and experience with extension services, farmer field schools or measuring volumes had no significant effect. Seed thickness and width interacted significantly with variety, but removing seed traits and variety cost little fit, so the final model kept farmer volume alone. Market class was not significant.
   >
   > The final model predicts researcher-weighed yield from the number of tins (intercept 0.043, slope 0.884), with a random farm effect. In cross-validation with three folds and 100 repetitions, it explained about 90% of the variability in observed yield (R² 0.901), with a root mean square error of 0.233 and a mean absolute error of 0.133. In a simulation of 1000 farms generated from this model, R² stayed between 0.98 and 0.99 for training sets of 5 to 100 farms, and prediction error stabilised at about 25 farms.
   >
   > Farmer-led estimates differentiated between varieties. Sweet Violet yielded most and RCB 593 least, for both farmers and technicians. The authors note that earlier studies reported inconsistent performance for these varieties, which may reflect genotype-by-environment interaction.
   >
   > The authors conclude that farmer-generated yield data, collected with a standard protocol, can reliably inform breeding decisions. They see a cost-effective and scalable way to add yield to on-farm trials and accelerate variety turnover in sub-Saharan Africa, with fewer field visits than technician-measured yield requires. They caution that the sample was not random, so the yields do not represent overall variety performance. Common bean has large seeds and well-established harvest methods, and smaller-seeded crops such as wheat, sorghum or millet may be harder to measure. Plot area estimation and drop-out also need attention.

3. **Outside knowledge in the last Summary paragraph (Not in source).** Card: "adding a yield question to trial protocols, which de Sousa et al. 2024 and later guidance recommend". The source does not say this. It cites de Sousa et al. (2024) only for the point that fewer field visits help scaling (p. 8). De Sousa et al. 2024 itself (desousa-2024-asd) says teams are still testing farmer-led yield methods and have preliminary results. It does not recommend a yield question. The replacement Summary drops this. If a pointer is wanted, put it in Notes (see item 8).

4. **"Release committees" and "main expense" (Imprecise and Not in source).** Card Summary paragraph 1: "satisfy release committees", and later "researcher visits ... which are the main expense in on-farm testing" and "Farmer volumetric data could largely replace researcher visits". Source p. 1 and p. 2: absolute yields are needed to measure genetic gain and assess economic returns (return on investment). Release committees are not mentioned. Source p. 7 and p. 8: farmer data would reduce the cost of on-farm evaluation at scale and reduce the need for extensive field visits. The source never says visits are the main expense, and the simulation is designed to set a minimum number of field visits for calibration and quality checks (p. 4), so visits are reduced, not replaced. The replacement Summary uses the source's wording.

5. **Moisture range (Imprecise).** Card: "Moisture content ranged from 14.5% to 16.0%". Source p. 5 and Fig. 6 (p. 7): 14.5% to 16.0% is the spread across genotypes (one point per genotype). Fig. 5 (p. 7) shows individual readings from roughly 11.5% to 19.5% (read from chart, approximate). Replace the Key numbers row with:
   `| 14.5%–16.0% | Spread of genotype moisture content (Fig. 6). Individual readings ranged more widely, roughly 11.5% to 19.5% (Fig. 5, read from chart) | This paper |`

6. **"25 farmers" and "subsampling" (Imprecise).** Card: "Subsampling showed that data from as few as 25 farmers still gave highly accurate estimates" and Key numbers "25 farmers | Minimum sample still giving highly accurate yield data". Source p. 4: the sample-size test is a simulation of 1000 farms generated from the fitted model, not a subsample of real farmers. Source p. 6 to 7 and Fig. 7 (p. 8): R² was 0.98 to 0.99 at every training size from 5 to 100 farms, and RMSE stabilised at about 25 farms. The "as few as 25" wording is from the Discussion (p. 8). Replace the Key numbers row with:
   `| 25 farms | Training-set size at which prediction error (RMSE) stabilised in a simulation of 1000 farms generated from the model. R² was 0.98 to 0.99 from 5 farms upward | This paper |`

7. **Methods bullet "Analysis" (Imprecise).** It omits the Wilcoxon signed-rank test and the mixed model with step-down feature selection used to test seed and farmer factors, and it calls the simulation "subsampling" (p. 4). Replace with:
   `- **Analysis.** Pearson correlation, Wilcoxon signed-rank test and Bland-Altman agreement on log volumes. A linear mixed model with step-down feature selection tested seed traits (moisture, thickness, width, length) and farmer traits (age, gender, eyesight, literacy, experience). A mixed model with farm as random effect converted farmer volume to weighed yield, checked by farm-level cross-validation (3 folds, 100 repetitions). A simulation of 1000 farms tested training sizes from 5 to 100 farms.`
   Also add a protocol bullet:
   `- **Protocol.** Farmers got the protocol two weeks before harvest, harvested each plot separately, dried pods two days in the field, then shelled and sun-dried the grain two more days. Farmers and technicians measured separately with levelled 1 L sado tins on a flat surface.`
   And extend the Survey bullet:
   `- **Survey.** 30 farmers (24 men, 6 women), a non-random subset of 355 tricot farmers, in Kilindi and Karatu districts of northern Tanzania, 2022. Three 6 × 8 m variety plots per farm.`

8. **Notes: "which cite this study" (Contradicted for desousa-2024-asd).** desousa-2024-asd (2024) predates this paper and does not cite it. It mentions ongoing tests of farmer-led yield methods in maize, common bean and cassava, with preliminary results showing good agreement. cairns-2026-jxb does cite Nabateregga et al. (2025). Replace the note with:
   `- Answers the yield concern raised in desousa-2024-asd, which reports farmer-led yield methods as still being tested with preliminary results. cairns-2026-jxb cites this study. ulzen-2025-agrirxiv reports similar results for tin measurement of maize and cocoa in Ghana.`

9. **Stated limitations (Imprecise and incomplete).** "A small sample (30 farmers), mostly men" is close, but the authors' stated point is that only six women limited the test of gender effects (p. 8). "Moisture effects may be larger in other crops or seasons": seasons are not mentioned (p. 9). The main stated limitation, a non-random sample whose yields do not represent variety performance (p. 8), is missing. Replace the section with:
   `- The 30 farmers were a non-random sample from a larger trial, so the yields do not represent overall variety performance.`
   `- Only six women took part, which limits the test of gender effects.`
   `- Common bean has large seeds and well-established harvest methods. Smaller-seeded crops such as wheat, sorghum or millet may be harder to measure because of seed size, threshing and moisture variability.`
   `- Yield per hectare depends on accurate plot area, which is hard to estimate on irregular smallholder plots.`
   `- Researcher weighing can also be biased (scale intervals, faulty scales, taring), and drop-out of participants must be planned for.`

10. **Summary claim on seed traits (Imprecise).** Card: "variety and seed dimensions (thickness and width) had only minor effects". Table 3 (p. 7) shows variety × thickness (p = 0.017) and variety × width (p = 0.003) were significant. They were dropped because they added little fit, not because their effects were not significant. The replacement Summary says this.

11. **data field (Imprecise).** Card: "see the data availability statement in the article". Source p. 9: data and code are on Zenodo. Replace with:
   `data: data and code on Zenodo, https://doi.org/10.5281/zenodo.15591106`

12. **not_established (optional strengthening).** Suggested:
   `not_established: a universal sample size for yield measurement; accuracy for smaller-seeded crops such as wheat, sorghum or millet, or for crops with repeated or piecemeal harvests; accurate yield per hectare where plot area is uncertain; representative variety yields from this sample; acceptance of farmer-measured yield by a release committee; an effect of literacy, which could not be tested`

13. **Questions (optional).** Add one question a tricot user would ask:
   `- Do farmer age, gender or experience affect how accurately they measure yield?`

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Accuracy of farmer-generated yield estimations of common bean in decentralised on-farm trials in sub-Saharan Africa | Same (p. 1, en dash in "sub–Saharan" in print) | Supported |
| authors | Nabateregga M, Dorado-Betancourt H, Solberg SØ, van Etten J, van Heerwaarden J, Gregory T, de Sousa K | Same order (p. 1) | Supported |
| year | 2025 | Published online 6 June 2025, vol. 170 (2025) (p. 1) | Supported |
| journal | European Journal of Agronomy | p. 1 | Supported |
| article | 170, 127730 | p. 1 | Supported |
| type | research article | Original research (p. 1 to 9) | Supported |
| doi | https://doi.org/10.1016/j.eja.2025.127730 | p. 1 | Supported |
| license | CC BY | "CC BY license", link to 4.0 (p. 1). "CC BY 4.0" would match the template example | Supported |
| data | see the data availability statement | Zenodo 10.5281/zenodo.15591106 (p. 9) | Imprecise (fix 11) |
| crops | common bean | p. 1 | Supported |
| region | Tanzania (Kilindi, Karatu) | p. 2 | Supported |
| gist | Farmer volumes agree with technicians (r = 0.96) and predict absolute yield, so tricot can supply yield data | Abstract and conclusion (p. 1, p. 9) | Supported. 28 words. Optional: add "in a Tanzanian study" for scope |
| not_established | Three items | Consistent with source | Supported, could be stronger (fix 12) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | tricot relies on rankings, relative not absolute | Supported | Abstract (p. 1), intro (p. 2) | |
| 2 | Summary | Absolute yields needed for genetic gain, release committees, returns | Imprecise | p. 1, p. 2 mention genetic gain and ROI only | Release committees not in source (fix 4) |
| 3 | Summary | Study tests whether farmers can generate accurate yield data | Supported | p. 2 | Also tests seed and farmer factors (not stated) |
| 4 | Summary | 2022 survey, 30 farmers (24 men, 6 women), Kilindi and Karatu | Supported | p. 2 | |
| 5 | Summary | Farmers and technicians measured with sado tins after sun-drying | Supported | p. 3 | Technicians are extension officers |
| 6 | Summary | Researchers measured mass and moisture | Supported | p. 3 | |
| 7 | Summary | r = 0.96, p < 0.001 | Supported | Abstract (p. 1), p. 5, Fig. 3B r = 0.961 (p. 6) | |
| 8 | Summary | Mean log-yield difference close to zero | Supported | p. 1, p. 5, Fig. 4 (p. 6) | Fig. 4 mean line about −0.1 (chart read), farmers slightly lower |
| 9 | Summary | Moisture ranged 14.5% to 16.0% | Imprecise | Fig. 6 (p. 7) genotype level. Fig. 5 readings about 11.5% to 19.5% (approximate) | Fix 5 |
| 10 | Summary | Moisture explained 11.9% of density and weight differences | Supported | p. 5 | See source issue 8 |
| 11 | Summary | Model explained about 90% (R² 0.901) | Supported | p. 6, Table 4 (p. 7) | Cross-validated mean |
| 12 | Summary | Loss of performance under validation < 5% | Contradicted | p. 5 | Loss of fit when seed traits dropped (fix 1) |
| 13 | Summary | As few as 25 farmers, by subsampling | Imprecise | p. 4, p. 6 to 8, Fig. 7 | Simulation, high R² from 5 farms (fix 6) |
| 14 | Summary | Authors conclude reliable, cost-effective, scalable, faster turnover | Supported | p. 1, p. 9 | |
| 15 | Summary | Farmer estimates differentiated genotypes | Supported | p. 7 | |
| 16 | Summary | Earlier inconsistent results for Sweet Violet and RCB 593 attributed to G×E | Supported | p. 7 | Source hedges: "can be owed to" |
| 17 | Summary | G×E central to adoption, which on-farm data capture well | Imprecise | p. 7 | Source says G×E is critical for adoption. "capture well" is the card's addition |
| 18 | Summary | Variety, thickness and width had only minor effects | Imprecise | Table 3 (p. 7), p. 5 | Interactions significant, dropped for small fit gain (fix 10) |
| 19 | Summary | Intrinsic and extrinsic factors barely biased estimates | Supported | p. 1, p. 5, p. 8 | |
| 20 | Summary | CV 3 folds, 100 reps, RMSE 0.233, MAE 0.133, R² 0.901 | Supported | p. 6, Table 4 (p. 7) | Repeats R² 0.901 |
| 21 | Summary | Farmer data could largely replace researcher visits, the main expense | Not in source | p. 7, p. 8 say reduce cost and need for visits | Fix 4 |
| 22 | Summary | Absolute yields that breeders, release committees and investors need | Imprecise | p. 1, p. 2 | Release committees not in source |
| 23 | Summary | Yield question recommended by de Sousa et al. 2024 and later guidance | Not in source | p. 8 cites de Sousa 2024 only for scaling | Outside knowledge (fix 3) |
| 24 | Summary | Subsampling showed it holds with modest numbers | Imprecise | p. 4, Fig. 7 (p. 8) | Simulation, not subsampling |
| 25 | Methods | Survey: 30 farmers, two districts, 2022 | Supported | p. 2 | |
| 26 | Methods | Farmer and technician tins, researcher mass and moisture | Supported | p. 3 | |
| 27 | Methods | Analysis list | Imprecise | p. 4 | Missing Wilcoxon and feature selection, "subsampling" (fix 7) |
| 28 | Limitations | Small sample, mostly men | Imprecise | p. 8 | Authors flag six women for gender test, and non-random sample |
| 29 | Limitations | Common bean easy to measure by volume | Supported | p. 8, p. 9 | |
| 30 | Limitations | Moisture effects may be larger in other crops or seasons | Imprecise | p. 9 | Crops yes, seasons not stated |
| 31 | Key numbers | 30 farmers (24 men, 6 women) | Supported | p. 2 | |
| 32 | Key numbers | r = 0.96 | Supported | p. 1, p. 5 | |
| 33 | Key numbers | 14.5%–16.0% moisture | Imprecise | Fig. 5, Fig. 6 (p. 7) | Fix 5 |
| 34 | Key numbers | 11.9% | Supported | p. 5 | |
| 35 | Key numbers | R² 0.901 | Supported | Table 4 (p. 7) | Say "cross-validated" |
| 36 | Key numbers | <5% loss under validation | Contradicted | p. 5 | Fix 1 |
| 37 | Key numbers | 25 farmers minimum | Imprecise | p. 6 to 8, Fig. 7 | Fix 6 |
| 38 | Notes | desousa-2024-asd and cairns-2026-jxb cite this study | Contradicted | desousa-2024-asd does not cite it (it predates it). cairns-2026-jxb does | Fix 8 |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Simulation R² results are attributed to Fig. 6, but they are in Fig. 7 | p. 7 | No | - The simulation R² values (0.98 to 0.99) are cited to Fig. 6 in the text but shown in Fig. 7. |
| Bland-Altman limits: text says mean ± 0.5 SD and cites Fig. 3, caption of Fig. 4 says ± 2 SD | p. 5, p. 6 | No | - Text gives the agreement limits as mean ± 0.5 SD, but the Fig. 4 caption says ± 2 SD. |
| Table 5 caption says "model Eq. 1" but reports the final model (Eq. 2). Units are given as ton·ha⁻¹ while the response is weighed yield in kg per plot and the predictor is number of tins. RMSE 0.233 is given in unstated "units" | p. 4, p. 6, p. 8 | No | - Units of the final model are unclear. Table 5 says t/ha, but yield was weighed in kg per 6 × 8 m plot and volume counted in tins. Treat the slope (0.884) and RMSE (0.233) as per-plot values with uncertain units. |
| P-values printed as "p < 0" in text and figures, and Table 3 gives "> 0.001" for farmer volume where "< 0.001" is meant | p. 5, p. 6, p. 7 | No | Not needed in Notes (obvious typos) |
| Methods define R²c and R²M "respectively" in swapped order | p. 4 | No | Not needed |
| Table 1 "potential yield" values run 1.2, 1.3 ... 1.18, which look like numbering, not yields. Variety names in Table 1 do not match Fig. 2 and Fig. 5 (Boroto, Calima Uyole, Uyole 18 appear only in figures, Uyole 03 is listed twice in Table 1) | p. 3, p. 5, p. 7 | No | - Table 1 potential yields look like a numbering error, and variety names differ between Table 1 and the figures. Do not cite Table 1 yields. |
| Abstract sentence is garbled ("using farmer showing minimal influence") | p. 1 | No | Not needed |
| Moisture result (R² 0.119) is called a correlation coefficient, and Fig. 5 plots moisture by variety, so it is unclear what was regressed to give "11.9% of differences in density and weight" | p. 5, p. 7 | No | - The 11.9% moisture figure comes from an R² of 0.119 whose model is not clearly described. |
| Fig. 7 caption says 1000 runs, Methods say 100 replications per sample size | p. 4, p. 8 | No | Optional |
| Gloria and NUA 48 are said not to be in the yield sample, but Fig. 2 and Fig. 5 show values for them | p. 5, p. 7 | No | Optional |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: accuracy of farmer yield data, and effects of seed and farmer factors | Partly (factors only in passing) | Medium | In replacement Summary |
| Design: 30 farmers are a non-random subset of 355 tricot farmers, three 6 × 8 m plots per farm | No | High | Fix 2 and fix 7 |
| Authors' caveat that yields are not representative of variety performance | No | High | Fix 9 |
| Farmer volume vs researcher-weighed yield r = 0.954, technician r = 0.991 (Fig. 3A) | No | High | Fix 2. Also Key numbers row: `\| r = 0.954 \| Correlation between farmer tin volume and researcher-weighed yield (technician volume r = 0.991) \| This paper \|` |
| Drying and measuring protocol (two days in pods, two days shelled, levelled 1 L tins, separate measurement) | No | High | Fix 2 and fix 7 |
| Farmer age, gender, eyesight and experience had no effect, literacy could not be tested (no variation) | No (only "extrinsic factors barely biased") | Medium | Fix 2 and fix 12 |
| Final model coefficients (intercept 0.043, slope 0.884, farm random effect) and market class not significant (p = 0.292) | No | Medium | Fix 2. Key numbers row: `\| 0.884 \| Slope of weighed yield on farmer tin count in the final mixed model (units unclear, see Notes) \| This paper \|` |
| Wilcoxon test and slight farmer underestimation | No | Medium | Fix 2 and fix 7 |
| About 90 data points, three misreports linked to low volumes, difficulty with fractions | No | Low | Optional Notes line |
| Crop area estimation, researcher weighing bias, attrition, smaller-seeded crops | Partly | Medium | Fix 9 |
| Sweet Violet highest, RCB 593 lowest | No | Low | In replacement Summary |
| Accuracy expected to improve with repeated participation, farmer training helpful | No | Low | Optional |
| Funding: AVISA and 1000FARMS (Gates Foundation) | No | Low | Optional Notes line |

## Template compliance

- Summary word count: 402 (within 400 to 500). The replacement is 498.
- Gist: 28 words (under 30). It says what the paper shows.
- Keywords: 9 (within 8 to 12).
- Questions: 4 (within 4 to 7). One optional addition in fix 13.
- House style: tricot is lowercase throughout. maniva does not appear.
- Structure: the Summary places the conclusion paragraph in the middle and repeats R² 0.901, so it reads as two drafts joined together. The replacement fixes this.
