---
id: steinke-2017-asd
title: The accuracy of farmer-generated data in an agricultural citizen science methodology
authors: Steinke J, van Etten J, Mejía Zelan P
year: 2017
journal: Agronomy for Sustainable Development
journal_short: Agron Sustain Dev
article: 37, 32
type: research article
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1007/s13593-017-0441-y
open_copy: https://doi.org/10.1007/s13593-017-0441-y
license: CC BY 4.0
data: electronic supplementary material with the article (contents not described in the PDF), no code repository stated
crops: common bean
region: Honduras
keywords: data quality, validity, reliability, wisdom of crowds, farmer observations, sample size, Kendall's tau, Kendall's W, Mallows-Bradley-Terry, tricot
gist: First test of tricot data quality, showing individual farmer rankings are unreliable but valid in aggregate, so 150 to 200 farmers likely suffice for 10 to 12 varieties
not_established: that individual farmer rankings are accurate on their own; that tricot is valid for yield, post-harvest, cooking or taste traits, which were not tested; that 150 to 200 participants is a tested minimum rather than a simulation-based order of magnitude under idealized, evenly spaced varieties; that women and men observe equally well in general, since groups were small and all participants grew beans; that disease resistance cannot be assessed by farmers, since its sample was 11 observations
---

## Questions this paper answers

- Are farmer rankings in tricot accurate enough to use?
- What is the difference between reliability and validity of farmer observations?
- How many participants does a tricot trial need?
- Which traits are easy or hard for farmers to assess?
- Do women and men differ in the accuracy of their observations?

## Summary

The paper tests the core assumption of tricot, that many independent, lightly supervised farmer observations can be aggregated into valid results. Participatory approaches are hard to scale because they need trained staff, collective plots and sustained farmer engagement. tricot instead relies on the "wisdom of crowds", where a diverse group of independent observers converges on the right answer even if individuals often err.

At five sites in Honduras, 35 farmers (18 women and 17 men) evaluated sets of three common bean varieties grown side by side. They ranked the varieties for plant vigor, plant architecture, pest resistance and disease resistance, and an experienced agronomist ranked them independently. The agronomist's ranking served as the reference for validity.

Individual reliability was low. Agreement among farmers (Kendall's W) ranged from 0.174 to 0.676 and was high only for plant vigor, an easily seen trait. Validity was adequate. Mean agreement between farmers and the agronomist (Kendall's tau) ranged from 0.33 for disease resistance to 0.76 for plant vigor, and 77 to 100% of farmer rankings matched or nearly matched the agronomist's, against 50% expected by chance. Mallows-Bradley-Terry models fitted to the pooled rankings recovered the agronomist's order for all four traits. All three varieties separated significantly only for plant vigor, and the best and worst varieties separated for every trait except disease resistance, which had only 11 observations. Women and men did not differ significantly in validity for any trait (Wilcoxon tests), although the groups were small (5 to 14 per trait).

A simulation based on the field data then estimated how many participants are needed. More observers increase the number of varieties that can be told apart from the best one, and harder traits need more observers. With 12 varieties, the discriminative ability reached for plant vigor with 50 participants required 200 participants for disease resistance.

The authors conclude that low individual reliability does not undermine accuracy when enough farmers take part. Assuming attrition of 20% or less, 150 to 200 participants are likely sufficient to evaluate 10 to 12 varieties. They also note that some disagreement may reflect different criteria among farmers, for example on what good plant architecture means, rather than observation error. tricot results therefore represent an average of farmer views, and the authors were testing methods that treat this variation as information. They recommend planning new tricot trials with a small preparatory study of this kind, because discriminative ability varies in practice.

The simulation also showed that adding varieties to a trial of fixed size raises the number of varieties distinguishable from the best, although the share of distinguishable varieties falls (from 100% with 3 varieties to 84% with 20, for plant vigor and 50 observers). In the field data, plant architecture and pest resistance needed closer inspection of plants than plant vigor, and disease resistance needed the most scrutiny and background knowledge. The authors link this to Bentley's (1989) argument from Honduras that ease of visual observation is a main factor in the accuracy of farmer observations.

## Methods in brief

- **Design.** Five sites in Honduras, each with three common bean varieties, drawn from a pool of seven from the Zamorano bean breeding programme, in adjacent sub-plots of six 8 m rows. 35 farmers (18 women, 17 men) took part in five sessions across the season, in groups of five to eight, and each farmer evaluated one site. Each farmer named the best and worst variety for four traits. Pests and diseases could be observed at only two of the five sites.
- **Reference.** A local agronomist answered the same questions at each session, giving a "scientific ranking" per site.
- **Validity.** Kendall's tau between each farmer ranking and the reference, and Mallows-Bradley-Terry models on pooled rankings. The stated criterion was that the three varieties separate at p < 0.05 after Holm-Bonferroni correction.
- **Reliability.** Kendall's W for agreement among farmers.
- **Sample size.** Simulation with Thurstone-Mosteller case V intervals estimated from the data, across 216 scenarios of variety-set size, number of observers and trait.
- **Gender.** Wilcoxon signed-rank test on tau values of women and men.

## Stated limitations

- Disease resistance had only 11 observations, giving very low statistical power.
- The simulation assumes regularly spaced performance differences between varieties, an idealization.
- Rankings that differ from the expert may reflect different farmer criteria rather than error. The authors suggest detecting such disagreement statistically, as a data-quality check.
- Results reflect an averaged view of farmers and can hide group-specific preferences.
- The simulation considered only farmer observation error, not experimental errors such as mixed-up seeds or codes, and did not include attrition.
- Only pre-harvest traits were tested. Yield and post-harvest traits need a separate test.
- Farmers had only a short time on site, and pests and diseases were observed at only two of five sites.
- Pooling across sites assumes varieties were equally hard to tell apart at every site.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 35 farmers (18 women, 17 men) | Participants evaluating the trials | This paper |
| 5 sites | Trial locations in Honduras | This paper |
| 0.174–0.676 | Kendall's W, reliability among farmers | This paper |
| 0.33–0.76 | Mean Kendall's tau per trait, farmer rankings against the agronomist ranking (disease resistance to plant vigor) | This paper |
| 11 | Observations for disease resistance, too few to separate varieties | This paper |
| 216 | Simulation scenarios | This paper |
| 4 → 10 varieties | Distinguishable from the best, plant vigor, 12 entries, 10 vs 500 observers | This paper |
| 50 vs 200 | Observers needed for the same discriminative ability with 12 varieties, plant vigor vs disease resistance (simulation) | This paper |
| 150–200 participants | Sufficient for 10–12 varieties, assuming ≤20% attrition | This paper |
| <200 participants | Realistic sample producing meaningful results | This paper |

## Notes

- This is the validity study cited by de Sousa et al. 2024 (desousa-2024-asd) for the claim that aggregated farmer rankings are valid.
- The field data were analysed with Mallows-Bradley-Terry models and the simulation with Thurstone-Mosteller and generalized Bradley-Terry models. These predate the Plackett-Luce approach now standard in tricot (outside this source). See turner-2020-compstat.
- Outside this source: later tricot analysis models heterogeneity among farmers with Plackett-Luce model trees. See turner-2020-compstat.
- The authors suggest staged selection starting with easy traits, training farmers on disease recognition, and accepting lower discrimination for early screening (p. 9).
- All participants grew beans. The authors expect stronger gender effects where tasks are more divided between women and men (p. 6).
- Problem in the source: the stated MBT validity criterion (all three varieties separated at p < 0.05) is met only for plant vigor (Table 3). The conclusion that results were valid in all cases rests on the correct order for every trait and on best-versus-worst separation for three of four traits.
- Problem in the source: the gender comparison uses a Wilcoxon signed-rank test, a paired test, on independent groups of unequal size (Table 2). The groups had 5 to 14 people, so the test had little power.
- Problem in the source: for plant architecture, the gender means in Table 2 pool to a mean tau of about 0.49, while Table 1 gives 0.51 (reviewer's calculation).
- Problem in the source: in Table 3 the unadjusted p value for plant vigor X to Z is printed as 5.152, which is not a valid p value (probably 5.152e-5).
- Problem in the source: the tau formula text defines n as the number of binaries, but in n(n-1)/2 it must be the number of ranked items (p. 5).
