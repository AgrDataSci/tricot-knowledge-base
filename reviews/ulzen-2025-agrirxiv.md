# Card review: ulzen-2025-agrirxiv

- **Card:** papers/ulzen-2025-agrirxiv.md
- **Source:** papers-pdf/ulzen-et-al-2024.pdf (44 pages. Printed page numbers match PDF page numbers. Main text pp. 1 to 25, supplementary map and regression tables pp. 26 to 34, R script pp. 35 to 44.)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 54 (12 frontmatter fields, 42 body claims) |
| Supported | 45 |
| Imprecise | 8 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 8 |
| Important omissions | 3 high, 7 medium or low |
| Metadata issues | 3 (authors, data, missing not_established) |

The card is accurate on numbers. Every value in Key numbers matches Tables 4 and 5 and the text. The main weaknesses are emphasis and missing context. The Summary says weighing "was the most error-prone" without giving the trained weighing results, although trained farmers weighing cocoa came close to tin can accuracy (Table 5, p. 16). The card also has no not_established field, and the study has design caveats (prepared lots, not plot harvests, training confounded with community, exploratory regressions on 40 farmers) that a tricot user should see. "Tanzania" in the last Summary sentence is outside knowledge.

## Fixes needed

1. **Weighing results are overstated and the training effect has no numbers (Summary paragraph 3, Key numbers).** The card says weighing "was the most error-prone" and that untrained farmers "did no better than visual estimation (41.2% relative error for maize)". The source (Table 5, p. 16) shows the untrained maize figure is relative RMSD, and at 41.2% it is clearly worse than visual estimation (18.1%). Trained farmers reached a relative RMSD of 18.8% (maize) and 7.6% (cocoa), and their cocoa MAD (4.8%) beat the tin can (5.1%) (p. 16, lines 15 to 18). The authors' own summary is that weighing did not consistently beat visual estimation (p. 21, line 14). The same paragraph also mixes the literature review with this study's results, so a reader can take the 75% lifting result for a literature value. Replace paragraph 3 of the Summary with these two paragraphs (the full revised Summary is 497 words, within the 400 to 500 target):

   > The literature review sets expectations. Crop cuts are costly and tend to overestimate yield. In one five-country study, farmers' visual estimates after harvest overestimated output by only 3% on average. Aggregated farmer volumes in Kenya matched researcher data closely.
   >
   > In this study, lifting and visual comparison gave useful benchmarks. Farmers told the heavier of two bags apart correctly 75% of the time when the difference exceeded 6.3% to 8.5% of the reference weight. Visual estimates of absolute heap weight were less accurate but had little bias. Tin can measurement had the lowest error for almost every metric, with relative root mean squared deviations (RMSD) of 7.4% for maize and 6.7% for cocoa. In exploratory regressions, its accuracy showed no clear link to gender, education, eyesight or experience. The remaining bias came from how farmers filled the can, and it was consistent, so the authors suggest recalibration. With better reporting of can fractions, they expect a mean absolute deviation of 2% to 3% or lower. Weighing gave the largest errors among untrained farmers and did not consistently beat visual estimation. Untrained farmers had a relative RMSD of 41.2% for maize, worse than visual estimation, and none of them completed all weighing steps correctly. Training raised correct execution to 55% for cocoa and 45% for maize and cut the relative RMSD to 18.8% for maize and 7.6% for cocoa. Taring mistakes, such as forgetting to subtract the container weight, and confusing pounds with kilograms persisted.

   Add to Key numbers:

   > | 18.8% / 7.6% | Relative RMSD of trained weighing, maize / cocoa | This paper |
   > | 10% → 57% | Correct scale readings, before → after training | This paper |
   > | 2%–3% | MAD the authors expect for tin cans after recalibration and better reporting of fractions (a projection, not measured) | This paper |

2. **not_established is missing.** The study has clear limits that users may stretch. Add to the frontmatter:

   > not_established: That farmer weighing is inherently inaccurate, since trained farmers weighing cocoa came close to tin can accuracy; that tin can accuracy holds for real plot harvests, very small yields or other crops, since the exercises used prepared 25 kg and 64.3 kg lots of maize and cocoa; that training alone caused the weighing gains, since trained and untrained farmers came from different communities; that farmer characteristics have no effect on volumetric accuracy, since the regressions were exploratory with 40 farmers and many predictors; that farmer volumes give dry-matter yield, since moisture was not measured

   Evidence: trained farmers were in Addaikrom and Kojofordjourkrom (p. 10, lines 14 to 18), and the untrained regressions use Bopa, Ched and Kojokrom (Tables S6 and S8, pp. 32, 34). The volumetric regressions have overall p = 0.227 and 0.297 with about 22 predictors (Tables S3 and S4, pp. 29 to 30).

3. **"Tanzania" is not in the source (Summary, last sentence).** The source only says a study was done in parallel with a more realistic setup (p. 5, lines 22 to 26). It does not name a country. Replace with:

   > The results agree with a parallel study of farmer volumetric yield measurement (nabateregga-2025-eja).

   If the country is wanted, put it in Notes: "The parallel study cited as Nabateregga et al. 2024 was done in Tanzania (see nabateregga-2025-eja). The preprint does not name the country."

4. **Nabateregga note compares different statistics (Notes, bullet 2).** The preprint's r² = 0.95 is between farmers' tin can estimates and researcher-determined weights (p. 5, lines 24 to 26). The nabateregga-2025-eja card gives r = 0.96 for farmer versus technician volumes and R² = 0.901 for predicting weight from farmer volumes. These are different comparisons, so "use the published value" is misleading. (I took the published values from the nabateregga card and did not check them against its PDF.) Replace with:

   > - The preprint cites Nabateregga et al. 2024 (SSRN preprint) as r² = 0.95 between farmers' tin can estimates and researcher-determined weights. The published paper (nabateregga-2025-eja) reports r = 0.96 for farmer versus technician volumes and R² = 0.901 for predicting weight from farmer volumes. These are different comparisons. Cite the published values with their own definitions.

5. **Volume-to-weight conversion is missing from the conclusions (Summary, last paragraph).** The authors stress that volumes need calibration to weights, possibly with variety effects, and suggest weighing a small subset of samples (p. 20, lines 20 to 22). Replace the last paragraph with:

   > The authors conclude that volumetric measurement with a container of known volume is the practical choice where training is limited. Volumes still need conversion to weight, for example by weighing a small subset of samples. Weighing could improve with electronic scales and procedures that avoid taring. They argue that farmer measurement can extend trial reach, reduce bias toward accessible communities, and free technician time, possibly with technicians measuring a subsample. The results agree with a parallel study of farmer volumetric yield measurement (nabateregga-2025-eja).

6. **Stated limitations: second bullet is framed as the authors' limitation but mixes scope choices, and two of the authors' own limitations are missing.** The source presents small quantities as a deliberate choice for small trial plots (p. 8, lines 8 to 10) and area estimation as less relevant for standardized planting (p. 4, lines 8 to 9). The authors do say the parallel study had a more realistic setup (p. 5). They also say training results may be optimistic (p. 20, lines 32 to 33) and that weighing small batches and adding by hand may add errors (p. 14, lines 8 to 13). Replace the second bullet and add two bullets:

   > - The exercises used prepared lots of known weight, not real plot harvests. The authors note that the parallel bean study used a more realistic setup. Area estimation and separating marketable product were left out.
   > - Training results may be optimistic, since in real trials farmers weigh harvests months after training.
   > - Scales were tested on single small samples (2.5 kg maize, 4 kg cocoa). Weighing a whole plot harvest in batches and adding the numbers by hand could add errors.

7. **Frontmatter data field is not filled in.** The source gives a dataset DOI and includes the R script (p. 22, lines 18 to 21, and pp. 35 to 44). Replace with:

   > data: Dataverse, https://doi.org/10.7910/DVN/6VTLGD (CC BY 4.0). The R script is in the supplementary material of the preprint.

8. **Author name.** The source writes "Hugo Andrés Dorado Betancourt" with no hyphen (p. 1 and authorship statement p. 22). The automated check flagged this. Replace the authors field with:

   > authors: Ulzen J, Osei-Bonsu NO, Bush G, Dorado Betancourt HA, van Etten J

   (If the knowledge base has a house spelling for this author in people.md, use that instead and ignore this fix.)

9. **Methods in brief lacks the practical protocol.** The template asks for any practical protocol, and tricot users will want the quantities and can size. Replace the Training bullet and add two bullets:

   > - **Training.** 20 farmers in Addaikrom and Kojofordjourkrom trained in weighing with a ten-step manual. 20 untrained controls came from the other three communities.
   > - **Quantities.** Sacks of 20 kg (cocoa) and 25 kg (maize), with others ±6% and ±15%. Heaps of 64.3 kg (cocoa) and 25 kg (maize), with others ±5% and ±10%. The same 64.3 kg and 25 kg lots were measured with a tin can 15 cm wide and 12 cm high. Scale samples were 4 kg (cocoa) and 2.5 kg (maize).
   > - **Setup.** One lot of each crop per community, so moisture was uniform within a community. Farmers waited 50 m away and came one at a time.

10. **Key numbers, Verma row.** The text cites Verma et al. 1991, but the reference list gives Verma, Marchant and Scott 1988 (p. 6 versus p. 24). Replace the Primary source cell with:

    > Verma et al., cited in this paper (1991 in the text, 1988 in the reference list)

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Accuracy in agricultural citizen science. Farmers' assessment of harvest output in Ghana | "...citizen science: farmers' assessment of harvest output in Ghana" (p. 1) | Supported (colon to period is expected) |
| authors | Ulzen J, Osei-Bonsu NO, Bush G, Dorado-Betancourt H, van Etten J | Jacob Ulzen, Nana Oduro Osei - Bonsu, George Bush, Hugo Andrés Dorado Betancourt, Jacob van Etten (p. 1) | Imprecise (hyphen added, middle initial dropped) |
| year | 2025 | DOI agriRxiv.2025.00295 (p. 1). No date printed | Supported |
| journal | agriRxiv (preprint) | DOI prefix, CABI Digital Library footer (all pages) | Supported |
| article | preprint 2025.00295 | DOI (p. 1) | Supported |
| type | preprint | agriRxiv | Supported |
| doi | https://doi.org/10.31220/agriRxiv.2025.00295 | p. 1 header | Supported |
| license | see preprint record | No license stated for the preprint text. Data are CC BY 4.0 (p. 22) | Supported |
| data | see the preprint | Dataverse DOI 10.7910/DVN/6VTLGD, CC BY 4.0 (p. 22). R script pp. 35 to 44 | Imprecise (should give the DOI) |
| crops | maize (shelled grain), cocoa (dried beans) | p. 7, lines 31 to 33 | Supported |
| region | Ghana (Western North and Ashanti regions) | p. 9, lines 9 to 14 | Supported |
| gist | Tin can most accurate and robust, weighing error-prone even after training, 40 farmers | Abstract p. 2. Table 5 p. 16 | Supported (28 words. States a finding, not a topic list) |
| not_established | absent | See fix 2 | Missing |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Decentralized trials reach remote areas and cut costs but need on-site presence at harvest | Supported | Abstract p. 2. p. 3, lines 7 to 9 | Source says "often" and "physical presence". Card's "usually needs technicians" is close enough |
| 2 | Summary | Researchers fall back on technicians because farmer accuracy is unknown | Supported | p. 2, lines 8 to 9. p. 3, lines 37 to 38 | |
| 3 | Summary | Motivated by adding metric yield to tricot, which relies on rankings. Tests measurement of output once in hand | Supported | p. 3, lines 23 to 29. p. 4, lines 7 to 8 | |
| 4 | Summary | 40 farmers, five communities, Western North and Ashanti, Kookoo Pa members in its tricot trials | Supported | p. 9, lines 9 to 21 | Source spells it both "Kookoo Pa" and "Kokoo Pa" |
| 5 | Summary | Four exercises with maize and cocoa | Supported | p. 8, lines 1 to 7 | |
| 6 | Summary | Lifting sacks, heaps by eye, tin cans, butcher's scale | Supported | pp. 11 to 14 | |
| 7 | Summary | 20 farmers in two communities trained with a manual, others controls | Supported | p. 10, lines 14 to 18. p. 14, lines 16 to 21 | Controls are from the other three communities (see fix 2) |
| 8 | Summary | Questionnaire and Snellen chart | Supported | p. 8, lines 12 to 19 | |
| 9 | Summary | Crop cuts costly and tend to overestimate | Supported | p. 5, lines 32 to 40. p. 6, lines 1 to 9 | |
| 10 | Summary | Farmers' post-harvest estimates came within a few percent of true weights "in earlier studies" | Imprecise | p. 6, lines 9 to 11 | One study (Verma et al.), and +3% is mean bias, not individual accuracy. Fix 1 |
| 11 | Summary | Aggregated farmer volumes in Kenya matched researcher data closely | Supported | p. 5, lines 12 to 20 (r = 0.98) | |
| 12 | Summary | Lifting and visual comparison gave useful benchmarks | Supported | p. 16, lines 1 to 2 | Placed in the literature paragraph, which blurs source of results. Fix 1 |
| 13 | Summary | 75% correct when difference exceeded 6.3% to 8.5% | Supported | p. 15, lines 30 to 32. Table 4 p. 16 | Cocoa 6.3%, maize 8.5% |
| 14 | Summary | Visual absolute estimates less accurate but little bias | Supported | p. 16, lines 9 to 13. Table 5 MSD -2.4%, -5.9% | |
| 15 | Summary | Tin can lowest error for almost every metric, RMSD 7.4% maize, 6.7% cocoa | Supported | p. 16, lines 15 to 18. Table 5 | |
| 16 | Summary | Tin can accuracy "did not differ" by gender, education, eyesight or experience | Imprecise | p. 19, lines 18 to 20. Tables S3, S4 | Source: no differences found "in this sample". Regressions were exploratory and not significant overall. Wording more certain than source. Fix 1 |
| 17 | Summary | Weighing was the most error-prone | Imprecise | Table 5 p. 16. p. 21, line 14 | True for untrained farmers only. Trained cocoa weighing RMSD 7.6% is close to tin can 6.7%. Fix 1 |
| 18 | Summary | Untrained farmers no better than visual estimation (41.2% relative error for maize) | Imprecise | Table 5 p. 16. p. 16, lines 20 to 21 | 41.2% is relative RMSD, and it is worse than visual (18.1%). Fix 1 |
| 19 | Summary | No untrained farmer completed all weighing steps correctly | Supported | p. 18, lines 1 to 2 | n = 20 per crop |
| 20 | Summary | Training raised correct execution to 55% cocoa, 45% maize and reduced errors | Supported | p. 18, lines 2 to 3. p. 16, lines 21 to 22 | |
| 21 | Summary | Taring mistakes persisted | Supported | p. 18, lines 6 to 9 | Reading errors (kg versus lb) also persisted and are omitted |
| 22 | Summary | Authors conclude volumetric is the practical choice where training is limited | Supported | Abstract p. 2, lines 18 to 19 | |
| 23 | Summary | Weighing could improve with electronic scales and avoiding taring | Supported | p. 2, lines 17 to 18. pp. 20 to 21 | Hedged correctly |
| 24 | Summary | Farmer measurement can extend reach, reduce bias, free technician time, technicians on a subsample | Supported | p. 2, lines 21 to 23. p. 6, lines 24 to 25. p. 21 | |
| 25 | Summary | Agrees with parallel study in Tanzania | Not in source | p. 5, lines 22 to 26 | "Parallel" and "similar findings" are supported. Country is not named. Fix 3 |
| 26 | Methods | 40 farmers, five communities, mobilized by Kookoo Pa agents from tricot trials | Supported | p. 9, lines 16 to 21 | |
| 27 | Methods | Four exercises, each for maize and cocoa | Supported | p. 8 | |
| 28 | Methods | 20 trained with a manual, 20 untrained controls | Supported | p. 10, lines 14 to 18 | |
| 29 | Methods | Thurstonian models for JND, RMSD, MAD, MSD, regressions | Supported | p. 15, lines 7 to 27. Table 5 | |
| 30 | Limitations | Moisture not measured, so no dry-matter conversion | Supported | p. 18, lines 21 to 23. p. 4, lines 13 to 14 | |
| 31 | Limitations | Small quantities, no area estimation or marketable product | Imprecise | p. 4, lines 7 to 14. p. 8, lines 8 to 10 | Small quantities were a design choice, not a stated limitation. The authors' real point is the less realistic setup. Fix 6 |
| 32 | Limitations | Preprint, not peer reviewed | Supported | agriRxiv preprint | Card's own caveat, not the authors' |
| 33 | Key numbers | 40 farmers, 5 communities | Supported | p. 9 | |
| 34 | Key numbers | 6.3%–8.5% lifting JND | Supported | Table 4 p. 16 | Estimated with a Thurstonian model |
| 35 | Key numbers | 7.4% / 6.7% tin can RMSD | Supported | Table 5 p. 16 | Recomputed: 1.85/25 = 7.4%, 4.29/64.3 = 6.7% |
| 36 | Key numbers | 18.1% / 15.6% visual RMSD | Supported | Table 5 p. 16 | 4.53/25 = 18.1%, 10.05/64.3 = 15.6% |
| 37 | Key numbers | 41.2% / 13.1% untrained weighing RMSD | Supported | Table 5 p. 16 | 1.03/2.5 = 41.2%, 0.52/4.0 = 13.0% (13.1% from unrounded kg) |
| 38 | Key numbers | 0% → 55% / 45% correct weighing | Supported | p. 18, lines 1 to 3 | |
| 39 | Key numbers | 9% / 3% overestimation, Verma et al. 1991 cited | Supported | p. 6, lines 9 to 11 | Attribution correct. Year differs in reference list (source issue) |
| 40 | Key numbers | r = 0.98, Ochieng et al. 2019 cited | Supported | p. 5, line 19 | Attribution correct |
| 41 | Notes | PDF filed as 2024, DOI from 2025 | Supported | File name. DOI p. 1 | |
| 42 | Notes | Preprint cites r² = 0.95. Published paper reports r = 0.96, use published value | Imprecise | p. 5, lines 24 to 26 | First half supported. The two values measure different comparisons. Fix 4 |

All Table 5 percentages were recomputed from the kg values and reference weights. All match within rounding.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Table 4 row 2a gives 2.05 kg for maize visual ranking, which is 8.2% of 25 kg, not the 6.4% printed. The text repeats 6.4% | Table 4 p. 16. p. 15, line 33. p. 19, line 13 | No (card does not use this number) | - Table 4 gives 2.05 kg for the maize visual-ranking JND, which is 8.2% of the 25 kg reference, but the table and text print 6.4%. |
| Text says visual ranking gave larger relative errors than lifting, but for maize the printed visual JND (6.4%) is smaller than lifting (8.5%) | p. 15, lines 32 to 33 | No | Optional. Combine with the row above |
| Results say tin can accuracy was affected by location in one case (maize, Kojofordjourkrom, p = 0.028). Discussion says no difference by location | p. 18, lines 14 to 15. Table S4 p. 30. p. 19, lines 18 to 20 | Partly (card leaves out location, which matches Results) | - The Results report one location effect on tin can accuracy (maize, Table S4), but the Discussion says there were no location differences. |
| One outlier (more than 40 cans) was removed from the maize tin can data. This appears only in the R script, not in the Methods | R script p. 39, line 2. Table S4 N = 39 | No | - The maize tin can result (7.4%) excludes one outlier above 40 cans. This is stated only in the R script (p. 39), not in the Methods. |
| Table 1 age classes add to 36, not 40, and the 25 to 34 class is missing | Table 1 p. 10 | No | Low importance. Optional |
| Citation years differ between text and references: Verma et al. 1991 versus 1988, Casley and Kumar 1998 and 1989 versus 1988 | pp. 5, 6, 18 versus pp. 22, 24 | No | See fix 10 |
| Numbering and cross-reference errors: two sections numbered 2, subsection 2.2 repeated, no Figure 7, Exercise 3 cites Figure 4 (should be 5), Exercise 2 cites Table 1 (should be 3), Supplement cites Table 2 for farmer data (should be 1), captions of Tables S6 to S8 say "trained" and "cocoa" for untrained or maize models | pp. 7 to 13, 17, 27, 32 to 34 | No | Not needed in the card |
| Training is described as training "in weighing cocoa", but trained results are also reported for maize | p. 14, line 16. Table 5 | No | Not needed in the card |

A possible further issue, not counted: the Discussion says farmers pack "more grains or fewer beans" into the can (p. 19, line 22), which would suggest fewer cans counted for maize, yet the maize tin can bias is positive (Table 5). The reference count used for maize ("level" fill) is not explained, so the direction cannot be checked. My suggested Summary text avoids stating the direction.

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: accuracy of farmer harvest measurement and its determinants | Yes | | |
| Design: four exercises, two crops, five communities, training versus control | Yes | | |
| Sample size: 40 farmers, 20 trained, 20 untrained | Yes | | |
| Main result: tin can most accurate (7.4%, 6.7%) | Yes | | |
| Trained weighing effect sizes (RMSD 18.8% maize, 7.6% cocoa, cocoa MAD better than tin can) | No | High | Fix 1 |
| Tin can bias is consistent, recalibration could give MAD of 2% to 3%, volumes need conversion to weight by weighing a subset | No | High | Fixes 1 and 5 |
| Design caveats: prepared lots not plot harvests, training confounded with community, exploratory regressions on small N | No | High | Fix 2 (not_established) |
| Reading errors: correct readings 10% before and 57% after training, kg and lb confusion | No | Medium | Fix 1 and Key numbers row |
| Authors' limitation: training gains may be optimistic months later | No | Medium | Fix 6 |
| Authors' limitation: scale tested on small single samples, adding batches by hand may add errors | No | Medium | Fix 6 |
| Practical protocol: quantities, can size 15 x 12 cm, 50 m separation, one lot per community | No | Medium | Fix 9 |
| Practical advice for tin cans: can size in proportion to expected yield, fraction lines inside cans, a large plus small can (p. 20) | No | Medium | Add to Notes: "- For tin cans, the authors suggest choosing can size in proportion to expected yield, drawing fraction lines inside the can, or using a large and a small can (p. 20)." |
| Visual heap estimates as a check against large outliers before tin can measurement (p. 21) | No | Medium | Add to Notes: "- The authors suggest farmers estimate heap size before counting cans, as a check against large outliers (p. 21)." |
| Spring scales with sacks as a low-tare alternative, from cassava trials in Nigeria (pers. comm., p. 21) | No | Low | Optional |
| Visual ranking JND 6.4% maize, 14.6% cocoa | No | Low | Optional, and see the Table 4 source issue |
| Funding: NWO-WOTRO cacao project, Gates 1000FARMS (p. 22) | No | Low | Optional |
| Authors' conclusions on trial design trade-offs and cost per data point | Yes | | |
| Agreement with parallel bean study | Yes | | Fix 3 for wording |

## Template compliance

- Summary word count: 415 now (within 400 to 500). The revised Summary from fixes 1, 3 and 5 is 497 words, still within range.
- Gist: 28 words (under 30). States a finding.
- Keywords: 12 (within 8 to 12).
- Questions: 5 (within 4 to 7).
- House style: tricot is lowercase throughout. maniva does not appear. No semicolons or em dashes in the card body.
- Long format card. All long-format sections are present. not_established is optional in the template but should be added here (fix 2).
