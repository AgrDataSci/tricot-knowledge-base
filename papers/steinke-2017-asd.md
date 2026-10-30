---
id: steinke-2017-asd
title: The accuracy of farmer-generated data in an agricultural citizen science methodology
authors: Steinke J, van Etten J, Mejía Zelan P
year: 2017
journal: Agronomy for Sustainable Development
journal_short: Agron Sustain Dev
article: 37, 32
type: research article
doi: https://doi.org/10.1007/s13593-017-0441-y
open_copy: https://doi.org/10.1007/s13593-017-0441-y
license: CC BY 4.0
data: supplementary material with the article
crops: common bean
region: Honduras
keywords: data quality, validity, reliability, wisdom of crowds, farmer observations, sample size, Kendall's tau, Kendall's W, Mallows-Bradley-Terry, tricot
gist: First test of tricot data quality, showing individual farmer rankings are unreliable but valid in aggregate, so 150 to 200 farmers suffice for 10 to 12 varieties
---

## Questions this paper answers

- Are farmer rankings in tricot accurate enough to use?
- What is the difference between reliability and validity of farmer observations?
- How many participants does a tricot trial need?
- Which traits are easy or hard for farmers to assess?
- Do women and men differ in the accuracy of their observations?

## Summary

The paper tests the core assumption of tricot, that many independent, lightly supervised farmer observations can be aggregated into valid results. Participatory approaches are hard to scale because they need trained staff, collective plots and sustained farmer engagement. Tricot instead relies on the "wisdom of crowds", where a diverse group of independent observers converges on the right answer even if each individual is often wrong.

At five sites in Honduras, 35 farmers (18 women and 17 men) evaluated sets of three common bean varieties grown side by side. They ranked the varieties for plant vigor, plant architecture, pest resistance and disease resistance, and an experienced agronomist ranked the same sets independently. The agronomist's ranking served as the reference for validity.

Individual reliability was low. Agreement among farmers (Kendall's W) ranged from 0.174 to 0.676 and was high only for plant vigor, a trait that is easy to see. Validity was adequate. Agreement between farmers and the agronomist (Kendall's tau) ranged from 0.33 to 0.76, and Mallows-Bradley-Terry models fitted to the pooled rankings recovered the correct order of varieties for most traits. Disease resistance was the exception, with too few observations to separate varieties. The authors found no difference in validity between women and men.

A simulation built on the empirical data then estimated how many participants are needed. More observers steadily increase the number of varieties that can be told apart from the best one, and harder traits need more observers. The discriminative ability reached for plant vigor with 50 participants required 200 participants for disease resistance.

The authors conclude that low individual reliability does not undermine accuracy when enough farmers take part. Assuming attrition of 20% or less, 150 to 200 participants are likely sufficient to evaluate 10 to 12 varieties. They also note that some disagreement reflects genuinely different criteria among farmers, for example on what good plant architecture means, rather than error. Tricot results therefore represent an average of farmer views, which later work addresses by modelling heterogeneity directly.

The simulation also showed that adding varieties to a trial of fixed size raises the number of varieties distinguishable from the best, within limits, and that traits needing closer inspection, such as plant architecture and pest resistance, call for more observers. The results agree with earlier ethnobiological work in Honduras, where farmers knew plants precisely, insects less well and plant diseases least, so ease of visual observation is a main factor in the accuracy of farmer data.

## Methods in brief

- **Design.** Five sites in Honduras, each with three common bean varieties in adjacent sub-plots of six 8 m rows. 35 farmers visited the plots at five points in the season and ranked best and worst for four traits.
- **Reference.** A local agronomist answered the same questions at each session, giving a "scientific ranking" per site.
- **Validity.** Kendall's tau between each farmer ranking and the reference, and Mallows-Bradley-Terry models on pooled rankings, judged valid if the three varieties separated at p < 0.05.
- **Reliability.** Kendall's W for agreement among farmers.
- **Sample size.** Simulation with Thurstone-Mosteller case V intervals estimated from the data, across 216 scenarios of variety-set size, number of observers and trait.
- **Gender.** Wilcoxon signed-rank test on tau values of women and men.

## Stated limitations

- Disease resistance had only 11 observations, giving very low statistical power.
- The simulation assumes regularly spaced performance differences between varieties, an idealization.
- Low agreement may reflect different farmer criteria rather than error, which the validity measure cannot separate.
- Results reflect an averaged view of farmers and can hide group-specific preferences.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 35 farmers (18 women, 17 men) | Participants evaluating the trials | This paper |
| 5 sites | Trial locations in Honduras | This paper |
| 0.174–0.676 | Kendall's W, reliability among farmers | This paper |
| 0.33–0.76 | Kendall's tau, validity against the agronomist ranking | This paper |
| 11 | Observations for disease resistance, too few to separate varieties | This paper |
| 216 | Simulation scenarios | This paper |
| 4 → 10 varieties | Distinguishable from the best, plant vigor, 12 entries, 10 vs 500 observers | This paper |
| 50 vs 200 | Observers needed for the same discrimination, plant vigor vs disease resistance | This paper |
| 150–200 participants | Sufficient for 10–12 varieties, assuming ≤20% attrition | This paper |
| <200 participants | Realistic sample producing meaningful results | This paper |

## Notes

- This is the validity study cited by de Sousa et al. 2024 (desousa-2024-asd) for the claim that aggregated farmer rankings are valid.
- The models used here (Mallows-Bradley-Terry) predate the Plackett-Luce approach now standard in tricot. See turner-2020-compstat.
