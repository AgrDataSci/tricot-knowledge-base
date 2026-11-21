# Card review: dorado-2026-tag

- **Card:** papers/dorado-2026-tag.md
- **Source:** papers-pdf/dorado-betancourt-et-al-2026.pdf (18 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 48 |
| Supported | 37 |
| Imprecise | 7 |
| Not in source | 4 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 5 |
| Important omissions | 5 |
| Metadata issues | 5 |

Every number the card gives is correct, and nothing is contradicted. The problem is what is missing. The card reports no result from the observed data (Table 3, p. 13), and it leaves out three findings a tricot user needs most: Plackett-Luce estimates are biased on a normal scale and need a scaling factor (p. 8), rankings need about 30% more replicates than yield measurement for the same precision (p. 9, p. 14), and only yield was tested (p. 15). The Summary also says the method connects tricot to genetic gain, which the paper lists as future work (p. 16). The most important fix is to replace the Summary with the version in Fix 1, which adds these results and stays within 500 words.

## Fixes needed

1. **Summary: main results missing, some wording overstated (high).** The card has no observed-data results, no Plackett-Luce bias or scaling factor, no 30% replication cost, no simulation design, and no note on undefined estimates. It also has these imprecise sentences: "there was no scalable way" (source: methods "remain limited", p. 1), "connecting tricot to ... genetic gain" (genetic gain is future work, p. 16), "can analyze ... non-quantitative traits such as taste in the same way" (stated as fact, but only yield was tested, p. 15), "cost-effective" (the paper uses this word for tricot itself, p. 2, not for the procedure, p. 14), and "This links tricot directly to how breeding programmes already report progress" (the card's own interpretation, not in the source). Paragraphs 3 and 5 also repeat each other. Replace the whole Summary with (about 490 words):

   "On-station trials often fail to represent on-farm conditions and farmer preferences, which can lead to poorly defined breeding targets. On-farm trials with ranking data, such as tricot, are more representative, but scalable methods to quantify genetic differences and the strength of the genetic signal from rankings remained limited. This paper proposes and tests a two-step procedure.

   The procedure follows the two-stage approach of quantitative genetics. In the first step, Thurstonian or Plackett-Luce models estimate genotypic means from rankings, with quasi-variances as their uncertainty, assuming rankings reflect an underlying continuous trait. In the second step, these estimates enter a mixed model weighted by the inverse quasi-variances to estimate the genetic standard deviation and Cullis heritability, as breeders do with yield trials.

   The authors simulated 18,480 tricot trials of maize yield with 20 genotypes, varying the genetic and residual standard deviations and the replicates per genotype (3, 10, 30 or 100). Genotype means from rankings were linearly related to the true means, and their variances captured the uncertainty. The Thurstonian model was unbiased. The Plackett-Luce model was biased when the underlying trait is normal, but a scaling factor of about 0.85 to 0.90 aligned it, and both models put genotypes in the same order. Standard errors from rankings were larger than from yield measurements, and about 30% more replicates were needed for the same precision. In most scenarios, about 30 replicates per genotype gave accurate means, genetic standard deviation and heritability. More were needed when the ratio of genetic to residual standard deviation exceeded 2, a ratio the authors expect to stay lower on farms.

   In 17% to 19% of simulated trials, some genotypes were repeatedly ranked best or worst, which made their estimates undefined and led to underestimated genetic standard deviation. Cullis heritability was negative in 17% to 19% of trials, and reference heritability below 0.25 was overestimated with both ranking and yield data. Heritability from rankings was lower than from yield, reflecting the information lost by ranking.

   Four observed datasets with both farmer rankings and measured yield (groundnut in Tanzania, early- and intermediate-maturity maize in Kenya, sweetpotato in Mozambique) confirmed the approach. Genetic correlations between ranking-based and yield-based estimates were 0.961 to 0.997. In three of the four datasets, heritability from farmers' rankings was lower than from measured yield, for example 0.23 versus 0.36 in groundnut, but close to heritability from rankings derived from the measured yields. This suggests that farmers' ranking did not bias the estimates. In intermediate-maturity maize, genetic variation was so low that yield-based heritability was 0.001 while ranking-based heritability was 0.41, which the authors link to a limitation of Cullis heritability.

   The authors argue that the procedure can handle rankings of non-quantitative traits such as flavour in the same way, but only yield was tested. They see it as a simple and flexible way to bring tricot data into standard breeding pipelines and multi-trial analyses. Genotype × environment effects, genetic gain and multi-trait analysis are left for future work."

   Sources: p. 1 (abstract), p. 5 (two steps, weights), p. 6 (Cullis heritability), p. 7 (Table 1, 18,480 trials), p. 8 (Plackett-Luce bias, scaling factor 0.85 to 0.90), p. 9 (30% more replicates), p. 10 (undefined estimates, negative heritability, below 0.25), p. 12 to 13 (observed data, Table 3), p. 14 (about 30 replicates, ratio above 2, order the same), p. 15 (only yield tested, flavor), p. 16 (future work). If curators prefer a shorter edit, the minimum is to fix the five imprecise sentences listed above and add the Table 3 results.

2. **not_established missing (high).** The card has no not_established field, and this paper is easy to stretch. Add (semicolons are the template separator):

   `not_established: performance for taste, colour or other non-quantitative traits (only yield was tested); estimates of genetic gain or genotype × environment effects (left for future work); that raw Plackett-Luce estimates are on the same scale as yield-based means (they needed a scaling factor of about 0.85 to 0.90); that heritability from rankings equals heritability from measured yield (it was lower in three of four datasets); that 30 replicates per genotype are always enough (more are needed when genetic variation is high relative to residual variation); that rankings should replace yield measurement where farmers can measure yield (the authors say rankings may then be complementary or unnecessary)`

3. **Stated limitations: authors' own limitations missing (high).** The card lists results from the simulations, but not the two limitations the authors state on p. 15 to 16, nor the caveat on extreme genotypes (p. 15) or the scope limits (p. 5, p. 16). Replace the section with:

   "- Only yield was analysed, in both simulated and observed data. Traits with unknown distributions were not tested.
   - Cullis heritability can be imprecise, unstable or negative when the ratio of genetic to residual standard deviation is very low. It was negative in 17% to 19% of simulated trials, and gave a very low yield-based value for intermediate-maturity maize.
   - Heritability below 0.25 is overestimated, with both ranking-based and quantitative data.
   - Genotypes repeatedly ranked best or worst give undefined estimates and inflated variances. The authors advise more replicates, or using only the order of genotypes, rather than removing these genotypes.
   - More than 100 replicates may be needed when the true genetic standard deviation exceeds 2 (in units of residual standard deviation).
   - Genotype × environment and genotype × year effects were not modelled. Designs with more than three genotypes per farm, ties, or within-farm replication were not assessed.
   - Quasi-variances were used as weights instead of the full variance-covariance matrix, which may be less efficient.
   - The maize data were not yet open at publication."

4. **Key numbers: main effect sizes missing (high).** Add these rows, and change the 17%–19% row so readers do not confuse the two uses of this range (see Source issues):

   `| 17%–19% | Simulated trials with negative Cullis heritability (excluded from the heritability analysis). The paper gives the same range for trials with undefined estimates | This paper |`
   `| 17%–19% | Simulated trials with an undefined covariance matrix, mainly when the genetic SD was above 1.5 and replicates below 30 | This paper |`
   `| 18,480 | Simulated tricot trials with 20 genotypes each (11 genetic SDs × 14 residual SDs × 4 replicate levels × 30 runs) | This paper |`
   `| ~30% | Extra replicates needed with rankings to match the precision of yield measurement under typical on-farm conditions | This paper |`
   `| 0.85–0.90 | Scaling factor for Plackett-Luce estimates when the genetic to residual SD ratio is 0.71 or lower and replicates exceed 30 (about 0.9 in the Discussion) | This paper |`
   `| 0.961–0.997 | Genetic correlations between ranking-based and yield-based genotype effects in four observed datasets | This paper |`
   `| 0.229 vs 0.359 | Cullis heritability from farmer rankings vs measured yield, groundnut, Tanzania | This paper |`
   `| 0.407 vs 0.001 | Cullis heritability from farmer rankings vs measured yield, intermediate-maturity maize, Kenya, where genetic variation was very low | This paper |`

   Also change the >100 row context to: "Replicates possibly needed when the true genetic standard deviation exceeds 2 (in units of residual SD)".

5. **Methods in brief: no design details (medium).** Replace the five bullets with:

   "- **Step 1.** Thurstonian and/or Plackett-Luce models give genotype utility means and quasi-variances per trial, with a check variety as reference.
   - **Step 2.** A linear mixed model weighted by inverse quasi-variances estimates the genetic standard deviation (REML, ASReml) and Cullis broad-sense heritability.
   - **Validation.** 18,480 simulated tricot trials of maize yield with 20 genotypes, with parameters from published on-farm maize trials in Africa: 11 genetic SDs × 14 residual SDs × 4 replicate levels (3, 10, 30, 100 per genotype), each run 30 times. Ranking-based estimates were compared with true values and with yield-based estimates. Plackett-Luce estimates were rescaled to the Thurstonian scale.
   - **Application.** Four tricot datasets with farmer rankings and measured yield on the same farms: groundnut in Tanzania (54 genotypes, about 28.5 replicates each), early-maturity maize (12 genotypes, about 66.8) and intermediate-maturity maize (25 genotypes, about 58.7) in Kenya, and sweetpotato in Mozambique (8 genotypes, about 16.5). Technicians or trained lead farmers measured yield for groundnut and sweetpotato, and farmers measured it for maize. Groundnut and sweetpotato data are on Zenodo.
   - **Code.** R functions and simulation workflow shared on GitHub and archived on Zenodo."

6. **Gist (low to medium).** The gist is accurate in outline but omits the main condition (replication) and the observed-data evidence. In the observed data, all ranking estimates came from the Thurstonian model (Table 3 footnote, p. 13), and Plackett-Luce was used only after rescaling. Replace with (27 words):

   `gist: Shows, with simulations and four on-farm datasets, that tricot rankings fed into a two-step mixed model give reliable genotype means and heritability, given about 30 replicates per genotype`

7. **Region (low).** The card says "sub-Saharan Africa". The datasets come from three named countries (Table 2, p. 9). Replace with:

   `region: Kenya, Mozambique, Tanzania (sub-Saharan Africa)`

8. **Keywords (low).** "genetic gain" is not estimated in the paper (future work, p. 16). Replace it with "quasi-variances". Optionally add "on-farm trials" (11 keywords).

9. **Software (low).** The template asks for the CRAN URL and checked version. The paper also used gosset, ClimMobTools (randomize() for the design) and ASReml, and fitted both ranking models with the authors' own code (p. 8). Suggested text (curator to fill in the version and dates after checking CRAN):

   `software: PlackettLuce, https://CRAN.R-project.org/package=PlackettLuce (vX.Y on CRAN, published YYYY-MM-DD, checked YYYY-MM-DD). The paper also used gosset, ClimMobTools and ASReml, and custom Thurstonian and Plackett-Luce code in the GitHub repository`

10. **Notes: outside knowledge not labelled (low).** The PDF does not mention a VeriXiv preprint, so the preprint link and "the numbers used here are the same in both versions" cannot be checked from this source. The "tricot-data" label and "data layer of the AI-ready documentation" are also outside knowledge. Replace the first two Notes with:

    "- From outside the source: this is the published version of a VeriXiv preprint (https://doi.org/10.12688/verixiv.2606.1). The journal PDF does not mention the preprint, and this check did not compare the two versions. Cite the journal article.
    - From outside the source: the Zenodo dataset the paper cites for groundnut and sweetpotato (de Sousa et al. 2025, Global multi-crop agricultural trial data supported by citizen science) is tricot-data, the data layer of the AI-ready documentation, so users can rerun the analysis.
    - Source issue: the paper gives 17–19% both for trials with undefined covariance matrices and for trials with negative Cullis heritability (p. 10). These are two separate outcomes, and the identical range may be a coincidence or a copying error.
    - Source issue: the code archive DOI is 10.5281/zenodo.17942919 in the Data availability statement (p. 16) but 10.5281/zenodo.17943088 in the reference list (p. 17). One may be the concept DOI and the other a version DOI.
    - Source issue: the scaling factor for Plackett-Luce is 0.85 to 0.90 for a ratio of 0.71 or lower in the Results (p. 8), but about 0.9 for a ratio below 1 in the Discussion (p. 14)."

11. **Questions (optional, low).** Add two questions a tricot user will ask, making 6:

    "- How many replicates per genotype does a tricot trial need for reliable genetic parameters?
    - Should I use the Plackett-Luce or the Thurstonian model to estimate heritability?"

12. **data field (optional, low).** Add the supplementary information archive: "supplementary information at https://doi.org/10.5281/zenodo.17941054 (CC BY 4.0)" (p. 16).

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Estimating on-farm genotypic performance and variability using ranking data | Same (p. 1) | Supported |
| authors | Dorado-Betancourt H, van Eeuwijk F, van Etten J, Ramirez-Villegas J, de Sousa K, Daudi H, Ndegwa M, Mendes T, van Heerwaarden J | Same nine authors, same order (p. 1) | Supported |
| year | 2026 | Published online 18 August 2026 (p. 1) | Supported |
| journal | Theoretical and Applied Genetics | Same (p. 1) | Supported |
| article | 139, 231 | (2026) 139:231 (p. 1) | Supported |
| type | research article | "RESEARCH" (p. 1) | Supported |
| doi | https://doi.org/10.1007/s00122-026-05319-1 | Same (p. 1) | Supported |
| license | CC BY 4.0 | Open Access, CC BY 4.0 (p. 16) | Supported |
| data | Zenodo 17112492 (CC BY-SA 4.0), maize on request (CIMMYT), GitHub, Zenodo 17942919 (MIT) | Same (p. 16). Supplementary archive 17941054 not listed. Reference list gives 17943088 for the code (p. 17) | Supported (optional addition, see Fix 12) |
| software | PlackettLuce | PlackettLuce, gosset, ClimMobTools, ASReml, custom code (p. 8) | Metadata issue (template format, Fix 9) |
| crops | groundnut, maize, sweetpotato | Table 2 (p. 9) | Supported |
| region | sub-Saharan Africa | Tanzania, Kenya, Mozambique (p. 9) | Imprecise (Fix 7) |
| keywords | 10 terms incl. genetic gain | Genetic gain only as future work (p. 16) | Metadata issue (Fix 8) |
| gist | Two-step mixed models estimate heritability from rankings | p. 1, p. 13 | Imprecise (Fix 6) |
| not_established | missing | Several stretch risks (p. 8, 13, 15, 16) | Metadata issue (Fix 2) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | On-station trials represent on-farm conditions and preferences poorly, can misdirect targets | Supported | Abstract (p. 1) | Source says "often fail" and "potentially" |
| 2 | Summary | On-farm ranking trials more representative, but there was no scalable way | Imprecise | p. 1: scalable methods "remain limited" | Stronger than source. Fix 1 |
| 3 | Summary | This paper proposes and tests one | Supported | p. 1, p. 2 | |
| 4 | Summary | Follows the two-step approach of quantitative genetics | Supported | p. 1, p. 5 | |
| 5 | Summary | Step 1: Thurstonian or PL give tables of means and variances, rankings as continuous trait | Supported | p. 1, p. 5 | Uses quasi-variances, not plain variances |
| 6 | Summary | Step 2: weighted mixed models estimate variance components and heritability, as with yield | Supported | p. 2, p. 5 to 6 | |
| 7 | Summary | Ranking means linearly related to quantitative means, variances capture uncertainty | Supported | Abstract (p. 1), Fig. 2 to 4 (p. 9 to 10) | |
| 8 | Summary | Second-step models recovered variance components accurately | Supported | p. 1, p. 10, p. 14 | Genetic SD underestimated at high genetic SD and low replication (p. 10), not mentioned |
| 9 | Summary | Cullis heritability negative in 17% to 19% of simulated trials | Supported | p. 10 | Negative cases were excluded |
| 10 | Summary | Heritability below 0.25 overestimated with both data types | Supported | p. 10, Fig. 8 (p. 13) | |
| 11 | Summary | Applications to three crops show the approach works and is reliable | Supported | p. 1, p. 12 to 13, p. 15 | No numbers given, intermediate maize anomaly omitted |
| 12 | Summary | Framework can scale to multi-trial on-farm data | Supported | p. 1 | Stated as the authors' argument, correctly |
| 13 | Summary | Connects tricot to heritability and genetic gain | Imprecise | p. 16 | Genetic gain is future work, not done |
| 14 | Summary | Estimates accurate as long as replication compensates for uncertainty | Supported | p. 13 to 14 | |
| 15 | Summary | About 30 replicates usually enough, more when ratio exceeds 2 | Supported | p. 14 | |
| 16 | Summary | Authors argue such conditions realistic on farms, ratio expected low | Supported | p. 14, p. 15 | |
| 17 | Summary | Can analyse quantitative and non-quantitative traits such as taste in the same way | Imprecise | p. 14 (claim), p. 15 (only yield tested) | Authors' proposal, untested. Paper names flavor, color, marketability (p. 15) |
| 18 | Summary | Cost-effective, flexible, easy to implement, extendable, could encourage adoption | Imprecise | p. 14 | "cost-effective" is said of tricot (p. 2), not the procedure. Rest supported |
| 19 | Summary | Links tricot to how breeding programmes report progress | Not in source | none | Card's own interpretation, not labelled |
| 20 | Methods | Step 1: Thurstonian/PL give means and variances per trial | Supported | p. 5 | Quasi-variances |
| 21 | Methods | Step 2: weighted mixed models for variance components and heritability | Supported | p. 5 to 6 | |
| 22 | Methods | Validation by simulated trials, ranking vs quantitative | Supported | p. 6 to 7 | No design details |
| 23 | Methods | Observed data on three crops, groundnut and sweetpotato from public tricot-data | Imprecise | p. 8, p. 16 | Source names a Zenodo dataset, "tricot-data" is outside naming. Four datasets, not three |
| 24 | Methods | Code on GitHub and Zenodo | Supported | p. 16 | |
| 25 | Limitations | Cullis heritability can be negative | Supported | p. 10, p. 15 to 16 | |
| 26 | Limitations | Heritability below 0.25 overestimated with both data types | Supported | p. 10 | |
| 27 | Limitations | More than 100 replicates when true genetic SD exceeds 2 | Supported | p. 10 | Unit (residual SD) not stated |
| 28 | Limitations | Maize data not open at publication | Supported | p. 16 | Data availability note, not a stated limitation |
| 29 | Key numbers | 17%–19% negative Cullis heritability | Supported | p. 10 | Same range used for undefined estimates |
| 30 | Key numbers | <0.25 reference heritability overestimated | Supported | p. 10 | |
| 31 | Key numbers | 3 crops | Supported | p. 9 | Four datasets |
| 32 | Key numbers | ~30 replicates usually sufficient | Supported | p. 14, p. 15 | |
| 33 | Key numbers | >100 replicates when genetic SD exceeds 2 | Supported | p. 10 | Add unit |
| 34 | Notes | Published version of the VeriXiv preprint | Not in source | none | Outside knowledge, not labelled |
| 35 | Notes | Numbers the same in both versions | Not in source | none | Cannot be checked from this PDF |
| 36 | Notes | Groundnut and sweetpotato data come from tricot-data, data layer of AI-ready documentation | Not in source | p. 8 cites a Zenodo dataset only | Outside knowledge, label it |
| 37 to 48 | Frontmatter | title, authors, year, journal, article, type, doi, license, data, crops (10 Supported), region and gist (2 Imprecise) | see Metadata check | | |

Totals: 48 claims. Supported 37, Imprecise 7 (claims 2, 13, 17, 18, 23, region, gist), Not in source 4 (claims 19, 34, 35, 36), Contradicted 0.

Recomputed values: 11 × 14 × 4 × 30 = 18,480 simulated trials (matches p. 7). Summary word count 401 (in range). Gist 23 words. All Key numbers rows are the paper's own results and are correctly credited to "This paper". No derived numbers in the card.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The same range, 17–19%, is given for trials with undefined covariance matrices and for trials with negative Cullis heritability | p. 10 | No | See Fix 10, third bullet |
| Code archive DOI differs: 17942919 in Data availability, 17943088 in reference list | p. 16, p. 17 | No (card uses 17942919) | See Fix 10, fourth bullet |
| Plackett-Luce scaling factor: 0.85 to 0.90 at ratio 0.71 or lower in Results, about 0.9 at ratio below 1 in Discussion | p. 8, p. 14 | No (card omits scaling) | See Fix 10, fifth bullet |
| Discussion says farmer rankings agree with measurements "taken by technicians", but maize yield was measured by farmers. Another Discussion sentence says "technicians or farmers" | p. 8, p. 14, p. 15 | No | Low importance. Optional: "The Discussion attributes yield measurement to technicians (p. 15), but farmers measured maize yield (p. 8)." |
| Change of variables in Eq. (2) to (3) writes U2k = y2k − y1k, but the example needs y8k − y1k | p. 4 | No | Low importance for card users, no Notes text needed |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: two-step procedure, simulation test, comparison with quantitative data (three objectives) | Yes | high | none |
| Plackett-Luce biased on a normal scale, Thurstonian unbiased, scaling factor 0.85 to 0.90, same genotype order (p. 8, p. 14) | No | high | Fix 1, Fix 4 |
| About 30% more replicates needed with rankings for the same precision (p. 9, p. 14) | No | high | Fix 1, Fix 4 |
| Observed results: genetic correlations 0.961 to 0.997, lower ranking heritability, farmer vs derived rankings similar, intermediate maize anomaly (Table 3, p. 12 to 13) | No | high | Fix 1, Fix 4 |
| Undefined estimates when a genotype is repeatedly ranked best or worst, 17–19% of trials, advice not to drop genotypes (p. 10, p. 15) | No | high | Fix 1, Fix 3, Fix 4 |
| Authors' limitation: only yield tested (p. 15) | No | high | Fix 1, Fix 3 |
| Simulation design: 20 genotypes, 18,480 trials, parameter grid, maize on-farm literature (p. 7) | No | medium | Fix 5 |
| Observed datasets: countries, genotypes, replicates, who measured yield (Table 2, p. 8 to 9) | No | medium | Fix 5 |
| Quasi-variances as weights and why (reference-invariant, easy to share across decentralized teams), full matrix or C-NMA as alternative (p. 5, p. 14 to 15) | No | medium | Fix 3, Fix 5 |
| Standard errors from rankings not constant, larger for extreme genotypes (p. 9, p. 14) | No | medium | Optional Notes line: "Standard errors of ranking-based means are not constant. They are larger for genotypes far from the average (p. 9)." |
| 3 replicates insufficient for heritability, ranking heritability follows the expected curve with factor 1.3 (p. 10, p. 12) | No | medium | Optional Notes line: "With 3 replicates per genotype, heritability estimates from rankings were unreliable (p. 10)." |
| Broad-sense heritability chosen because tricot is used in late-stage trials (p. 6) | No | low | Optional |
| Future work: G × E, genetic gain, multi-trait, more than three genotypes per farm, ties, within-farm replication (p. 16) | Partly (genetic gain stated as done) | medium | Fix 1, Fix 3 |
| Practical point: farmers can measure yield, so rankings may be complementary or unnecessary for yield, and most useful for non-quantitative traits or other stakeholders (p. 15) | No | medium | Fix 2 (not_established) |
| Conclusions: framework enables breeders to analyse ranking data and decide in line with farmers' needs (p. 16) | Yes | medium | none |

## Template compliance

- Summary word count: 401 (target 400 to 500). In range but at the lower limit. The replacement in Fix 1 is about 490 words.
- Gist: 23 words (under 30). Proposed gist: 27 words.
- Keywords: 10 (8 to 12). One keyword ("genetic gain") is not supported.
- Questions: 4 (4 to 7). Two optional additions in Fix 11.
- House style: tricot in lowercase throughout. maniva not used. No em dashes. Semicolons only inside the data field.
- not_established: missing (Fix 2).
- software: not in the template format (Fix 9).
- Long format: all long-format sections present.
