# Card review: tanaka-2021-tag

- **Card:** papers/tanaka-2021-tag.md
- **Source:** papers-pdf/tanaka-et-al-2021.pdf (14 pages, printed pages 3397 to 3410, so PDF page = printed page minus 3396)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 53 |
| Supported | 44 |
| Imprecise | 7 |
| Not in source | 1 |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 8 |
| Important omissions | 6 |
| Metadata issues | 2 |

The card is well written and most numbers are right, including the attribution of on-station accuracies to Grenier et al. 2015 and Spindel et al. 2015. But it misstates the main confirmatory result: it says selected accessions beat the random controls "at one site", while in year 2 they did so at both sites for both traits, and the year 3 effect sizes (22% at Ankazo, 14% not significant at Anjiro) are missing. It also says year 2 had one replicate, which contradicts the source and the card's own Methods bullet. The summary is 371 words, below the 400 minimum. A full replacement summary (475 words) is given in fix 1.

## Fixes needed

1. **Main selection result understated, year 2 replication wrong, summary too short.** The card says selected accessions "outperformed the random control group at one site" and that year 2 was grown "with one replicate". The source says that in year 2, straw and panicle weight were significantly higher in the selected group than in the control group at both sites (p. 3402, PDF 6, Fig. 1b). In year 3, the selected group had 22% higher panicle weight than the checks at Ankazo (significant), and 14% higher at Anjiro (not significant) (p. 3402, PDF 6, Fig. 2a). Year 2 had a second replication per site in an RCBD, with R = 2 in the heritability model (p. 3399 to 3400, PDF 3 to 4). The card also says the 234 year 2 accessions were top predicted plus random controls only, but they were 79 selected, 68 random controls and 87 added to widen the training set (p. 3399 to 3400, PDF 3 to 4). The summary also omits the low accuracy within the selected group in year 3 (r = 0.13 and 0.11, p. 3405, PDF 9), and states several points more firmly than the source (fixes 3 to 5). Replace the whole Summary with this text (475 words):

   > Rice yields in sub-Saharan Africa are low because soils are poor, phosphorus is often limiting and farmers apply little fertilizer. In Madagascar, average yields stay below 3 t/ha though achievable on-farm yields exceed 7 t/ha. Breeding on high-input stations may miss the traits needed under these conditions, while genebanks hold traditional varieties that could help. Ryokei Tanaka, James Lui-King, Matthias Wissuwa and colleagues from JIRCAS, the University of Tokyo and FOFIFA tested whether genomic prediction could find useful donors among the 3,024 sequenced accessions of the IRRI genebank without testing them all in the field.
   >
   > From 2016 to 2019 they ran trials in farmers' fields in the central highlands, with no fertilizer and only rain-fed water, as farmers practise. In year 1, 359 diverse accessions, chosen partly for origins in similar environments, were phenotyped without replication at two sites for heading date, straw weight and panicle weight. A GBLUP model then predicted all 3,024 accessions. In year 2, 234 new accessions were imported: top predicted accessions, a random control group and a set added to widen the training data. They were grown with 289 of the year 1 accessions at two sites, with two replicates. The updated model chose 52 more accessions for panicle weight, which were tested in year 3 against 23 checks.
   >
   > Prediction accuracy followed heritability. From year 1 to year 2 it was highest for heading date (about 0.71), intermediate for straw weight (0.25 to 0.63) and lowest for panicle weight, a yield proxy (0.10 to 0.30). The panicle weight values are in the range reported for yield in on-station rice studies at CIAT and IRRI. In year 2, accessions selected by prediction had significantly higher straw and panicle weight than the random control group at both sites. In year 3, selected accessions gave 22% more panicle weight than the checks at Ankazo, but the 14% gain at Anjiro was not significant. Accuracies were as high for newly tested accessions as for those in the training set. Within the top selected group in year 3, however, accuracy was low (about 0.1). Site effects appeared weak, which the authors expected because all sites were phosphorus-deficient, while year effects may have been strong in some cases.
   >
   > Selecting by expected improvement, a criterion designed to find superior accessions under uncertainty, gave nearly the same list as selecting by predicted genotypic value, probably because the training set was large. Unreplicated year 1 data predicted almost as well as replicated year 2 data. This agrees with an earlier simulation study, cited by the authors, which suggested that adding replicates may help less than a larger training set.
   >
   > Two accessions, IRIS 313-11949 and IRIS 313-7832, have been adopted as donors in the Malagasy lowland rice breeding programme. The authors conclude that genomic selection can make genebank diversity accessible to breeding for low-input farms, provided genotypic data are public.

2. **Key numbers missing the confirmatory effect sizes and year 3 accuracy.** Add these rows:

   | Number | Context | Primary source |
   |---|---|---|
   | 22% / 14% | Higher panicle weight of year 3 selected accessions than checks at Ankazo (significant) / Anjiro (not significant) | This paper |
   | 0.13 / 0.11 | Year 3 accuracy for panicle weight within the 52 newly selected accessions at Anjiro / Ankazo (0.74 / 0.76 for the 23 checks) | This paper |
   | 0.38 / 0.53 / 0.70 | Mean ten-fold cross-validation accuracy for panicle weight / straw weight / heading date across four year-by-site sets | This paper |
   | 523 | Accessions grown in year 2 (289 repeated from year 1 plus 234 new) | This paper |

   Also make the existing straw and panicle weight rows say where the ranges come from (p. 3405, PDF 9, Table 2):
   - `| 0.25-0.63 | Prediction accuracy for straw weight, year 1 training data predicting year 2 | This paper |`
   - `| 0.10-0.30 | Prediction accuracy for total panicle weight (yield proxy), year 1 training data predicting year 2 | This paper |`

3. **"These values match those from on-station rice studies at CIAT and IRRI."** The source compares only panicle weight with on-station yield accuracies, and says they are "comparable" or "in the range" (p. 3406 to 3407, PDF 10 to 11). On-station heading date accuracies at IRRI (0.54 and 0.63) were lower than here, so "these values" (all three traits) is too broad. Fixed in the replacement summary: "The panicle weight values are in the range reported for yield in on-station rice studies at CIAT and IRRI."

4. **"Site effects were small because all sites were phosphorus-deficient, while year effects were sometimes strong."** The source says consistent GxS effects "appear to have been weak", that this was expected given P-deficient sites, and that year effects "may have been strong" in some cases (p. 3406, PDF 10). Fixed in the replacement summary.

5. **"consistent with simulations showing a larger training set beats more replications."** The cited simulation (Lorenz 2013) concluded that adding replications "may not be as effective" as a larger training set (p. 3407, PDF 11). The card wording is more certain than the source and does not say the simulations come from another paper. Fixed in the replacement summary.

6. **Methods bullets.** Replace the Material and Plots bullets:
   - `- **Material.** 359 accessions from the IRRI 3K panel in year 1 (Madagascar, Sri Lanka, Nepal, Bhutan and a representative indica sample, 29 countries). In year 2, 289 of these plus 234 new accessions (79 selected by prediction, 68 random controls, 87 added to widen the training set). In year 3, 52 new selections plus 23 checks.`
   - `- **Plots.** Two-row micro-plots of 2 m, 22 hills, five plants sampled. Year 1 unreplicated, year 2 two replicates per site in RCBD, year 3 also replicated. Anjiro year 2 data were not used for year 3 selection because a cyclone flooded the field.`

7. **Stated limitations missing.** Add:
   - `- Accuracy within the top selected group was low in year 3 (r = 0.13 and 0.11), so prediction ranked the best accessions poorly among themselves.`
   - `- Genotype-by-site interaction was not modelled explicitly, and scaling each environment assumed similar heritability across sites.`
   - `- The Anjiro field was flooded after a cyclone in year 2, so those data were excluded from the year 3 selection.`

8. **Notes, authorship.** The note says an earlier version omitted James Lui-King and "thanked James DM King in the acknowledgements". The repository PDF still thanks James DM King for conceiving the study (p. 3408, PDF 12), so the note implies a change that this PDF does not show. A web check found a correction notice (https://doi.org/10.1007/s00122-024-04622-z, published 10 May 2024) that added James Lui-King as co-author and added MBBISP funding. Replace the first note with:
   - `- The PDF in this repository is the corrected version. A correction published on 10 May 2024 (https://doi.org/10.1007/s00122-024-04622-z, not in this PDF) added James Lui-King as an author, joint first with Ryokei Tanaka, and added MBBISP funding. The acknowledgements still thank James DM King for conceiving the study. Cite the current author list.`

9. **not_established.** Good as far as it goes. Add three items. Replace with:
   `not_established: that farmer-managed or participatory evaluation was used (trials were researcher-run plots on farmers' fields); that the donors have produced released varieties; that expected improvement beats predicted genotypic value (no difference found); that prediction ranks accessions well within the top group (year 3 accuracy among the selected was about 0.1); that grain yield was measured (total panicle dry weight per plant was the proxy); that the results hold outside phosphorus-deficient highland sites`

10. **Frontmatter, minor.**
    - authors: the PDF spells the name "Hiromi Kajiya Kanegae" without a hyphen (p. 3397, PDF 1). Replace `Kajiya-Kanegae H` with `Kajiya Kanegae H` to match the source.
    - data: the source states only that genotypic data are public at SNP-Seek. It says nothing about phenotype deposition or code. Replace with `data: genotypes of the IRRI 3K panel on SNP-Seek, https://snp-seek.irri.org/_snp.zul; no phenotype data or code availability statement`

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | From gene banks to farmer's fields. Using genomic selection... | Same, with a colon after "fields" (p. 3397, PDF 1) | Supported (colon to period expected) |
| authors | Tanaka R, Lui-King J, Mandaharisoa ST, Rakotondramanana M, Ranaivo HN, Pariasca-Tanaka J, Kajiya-Kanegae H, Iwata H, Wissuwa M | Same order. "Hiromi Kajiya Kanegae", no hyphen (p. 3397, PDF 1) | Imprecise (hyphen) |
| year | 2021 | Published online 15 July 2021 (p. 3397) | Supported |
| journal | Theoretical and Applied Genetics | p. 3397 | Supported |
| article | 134, 3397-3410 | 134:3397-3410 (p. 3397) | Supported |
| type | research article | "ORIGINAL ARTICLE" (p. 3397) | Supported |
| doi | https://doi.org/10.1007/s00122-021-03909-9 | p. 3397 | Supported |
| license | CC BY 4.0 | Open Access, CC BY 4.0 (p. 3408, PDF 12) | Supported |
| data | genotypes on SNP-Seek; phenotypes not deposited | Only genotypic data availability is stated (p. 3408) | Imprecise (phenotype claim not stated) |
| crops | rice | throughout | Supported |
| region | Madagascar (central highlands) | p. 3399 | Supported |
| gist | Genomic prediction on unfertilized farmers' fields picked high-performing accessions, accuracy similar to on-station, two donors | Abstract and Conclusions (p. 3397, 3408) | Supported |
| not_established | three items | No farmer evaluation, no released varieties, no EI vs PGV difference (p. 3403, 3407) | Supported, but weak (fix 9) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | SSA yields low: poor soils, P limiting, little fertilizer | Supported | p. 3397 to 3398 (PDF 1 to 2) | |
| 2 | Summary | Madagascar below 3 t/ha, achievable above 7 t/ha | Supported | p. 3398 (PDF 2), Saito et al. 2017 cited | |
| 3 | Summary | On-station breeding may miss traits, genebanks hold useful varieties | Supported | p. 3398 | |
| 4 | Summary | Team from JIRCAS, Univ. Tokyo, FOFIFA tested genomic prediction on 3,024 accessions | Supported | p. 3397 to 3398 | |
| 5 | Summary | 2016 to 2019, farmers' fields, no fertilizer, rain-fed | Supported | p. 3399 (PDF 3) | |
| 6 | Summary | Year 1: 359 accessions, partly by origin, two sites, HD, straw, panicle weight | Supported | p. 3399 | Year 1 was unreplicated, worth saying |
| 7 | Summary | GBLUP predicted all 3,024 | Supported | p. 3399 | |
| 8 | Summary | Top predicted plus random control, 234 in total | Imprecise | p. 3399 to 3400 (PDF 3 to 4) | 234 = 79 selected + 68 controls + 87 training enhancement. The source overview simplifies too (Source issue 3) |
| 9 | Summary | Year 2 grown at two sites "with one replicate" | Contradicted | p. 3399 to 3400: second replication, RCBD, R = 2 | Also contradicts the card's Methods bullet. Probably taken from "replicated once" (p. 3407), see Source issue 4 |
| 10 | Summary | Model updated, 52 more in year 3 | Supported | p. 3400, 3402 | 23 checks not mentioned |
| 11 | Summary | Accuracy followed heritability | Supported | p. 3406 (PDF 10), H2 0.95 to 0.98 / 0.62 to 0.73 / 0.56 to 0.61 | |
| 12 | Summary | HD about 0.71, STW 0.25 to 0.63, TPW 0.10 to 0.30 | Supported | Table 2, p. 3405 (PDF 9). Mean of HD cells recomputed = 0.71 | |
| 13 | Summary | "These values match" on-station studies at CIAT and IRRI | Imprecise | p. 3406 to 3407 | Comparison is for panicle weight vs yield only. Source says "comparable" |
| 14 | Summary | Selected beat random controls "at one site" | Imprecise | Year 2 both sites, both traits (Fig. 1b, p. 3402). Year 3 Ankazo only (Fig. 2a) | Understates main result, changes meaning |
| 15 | Summary | Accuracies as high for new as for training-set accessions | Supported | Table 2, p. 3405 | "as high or even higher" |
| 16 | Summary | Site effects small "because" P-deficient, year effects "sometimes strong" | Imprecise | p. 3406 | Source hedges: "appear", "may have been" |
| 17 | Summary | EI gave nearly the same list as PGV, probably large training set | Supported | p. 3403, 3407 | "one likely outcome" (p. 3407) |
| 18 | Summary | Unreplicated year 1 almost as good, simulations "showing" larger training set beats replication | Imprecise | p. 3407 (PDF 11), Lorenz 2013 | First half supported. Simulation result is hedged in source and is from another paper |
| 19 | Summary | Two donors IRIS 313-11949 and IRIS 313-7832 adopted | Supported | p. 3408 (PDF 12) | |
| 20 | Summary | Conclusion: GS makes genebank diversity accessible if genotypic data public | Supported | p. 3408 | |
| 21 | Methods | Sites 950 to 1,350 m, Anjiro, Behenjy, Ankazo, rainy season, no fertilizer, no irrigation | Supported | p. 3399 | |
| 22 | Methods | Material: 359 (four countries plus indica sample, 29 countries), 234, 52 | Supported | p. 3399 | 57+44+37+18 = 156, 359-156 = 203 indica sample, recomputed |
| 23 | Methods | Plots: 2-row 2 m, 22 hills, five plants. Year 1 unreplicated, year 2 two reps RCBD | Supported | p. 3399 | Year 3 was also replicated (p. 3400) |
| 24 | Methods | Traits: HD, height, tillers, STW, TPW per plant | Supported | p. 3399 | |
| 25 | Methods | GBLUP, ten-fold CV, year-to-year validation, PGV and EI | Supported | p. 3400 to 3401 | |
| 26 | Limitations | Low accuracy for panicle weight, low heritability | Supported | p. 3406, 3408 | |
| 27 | Limitations | Could not test EI with small training sets | Supported | p. 3407 | |
| 28 | Limitations | Training set chosen by origin, not optimized statistically | Supported | p. 3407 to 3408 | |
| 29 | Limitations | Year 3 used a small number of accessions | Supported | p. 3401, 3405 | |
| 30 | Key numbers | 3,024 accessions predicted | Supported | p. 3397, 3400 | |
| 31 | Key numbers | 359 / 234 / 52 | Supported | p. 3399 to 3400 | |
| 32 | Key numbers | ~0.71 HD, year 1 to year 2 | Supported | p. 3406, Table 2 | Recomputed 0.7125 |
| 33 | Key numbers | 0.25 to 0.63 STW | Supported | Table 2 | Add "year 1 to year 2" (fix 2) |
| 34 | Key numbers | 0.10 to 0.30 TPW | Supported | Table 2 | Add "year 1 to year 2" (fix 2) |
| 35 | Key numbers | 0.29 / up to 0.31, CIAT / IRRI, Grenier 2015, Spindel 2015 | Supported | p. 3406 to 3407 | Attribution correct |
| 36 | Key numbers | 2 donors | Supported | p. 3408 | |
| 37 | Key numbers | 2.3 vs 4.8 t/ha, FAOSTAT 2018 | Supported | p. 3397 | Attribution correct |
| 38 | Notes | James Lui-King is joint first author in this PDF | Supported | p. 3397 footnote | |
| 39 | Notes | Earlier version omitted him and thanked James DM King | Not in source | This PDF still thanks James DM King (p. 3408). Omission confirmed only by the 2024 correction notice (outside source) | See fix 8 |
| 40 | Notes | Researcher-run plots on farmers' fields, not farmer evaluation | Supported | p. 3399 | |

The 13 frontmatter fields in the Metadata check bring the total to 53 claims.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Subpopulation counts sum to 349, not 359 (22 japonica + 15 aus + 12 aromatic + 2 admix + 298 indica). 298 should be 308 if the other counts are right | p. 3399 (PDF 3) | No | `- The subpopulation breakdown of the 359 year 1 accessions (p. 3399) sums to 349, so one count is wrong.` |
| "15 or 12 accessions ... (from Nepal, Madagascar, Bhutan, respectively)" is garbled: two numbers, three countries | p. 3399 | No | Not needed |
| The overview says the 234 year 2 accessions were selected ones plus a random control group. The detail adds 87 training-enhancement accessions | p. 3399 vs p. 3399 to 3400 | No (card repeats the overview) | Covered by fix 6 |
| Discussion says year 2 was "replicated once", Methods says a second replication was added (R = 2) | p. 3407 vs p. 3399 to 3400 | No (card took the Discussion wording) | Covered by fix 1 |
| Abstract calls the trait "grain yield", but the measured trait is total panicle dry weight per plant | p. 3397 vs p. 3399 | Partly (card says "yield proxy") | `- The abstract reports accuracies for "grain yield", but the trait measured was total panicle dry weight per plant.` |
| Fig. 2b ("Validation in Anjiro") has the y-axis labelled "Observed TPW in Ankazo" | p. 3403 (PDF 7) | No | Not needed |
| Typos: Fig. 3 caption "PGV weight (STW)" for straw weight, Discussion "total PWT" for TPW | p. 3404, 3406 | No | Not needed |
| Acknowledgements thank James DM King for conceiving the study, while James Lui-King is a co-first author who designed the study. The PDF does not explain the relation | p. 3408 | Partly (Notes, but wording implies the acknowledgement was removed) | Covered by fix 8 |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim and four objectives (GS model on farm, predict and import, EI vs PGV, second cycle) | Yes | High | |
| Design: three years, three sites, no fertilizer, rain-fed | Yes | High | |
| Year 2 selected vs control: significant for both traits at both sites (Fig. 1b) | No, misstated | High | Fix 1 |
| Year 3: 22% higher TPW at Ankazo (significant), 14% at Anjiro (not significant) | No | High | Fixes 1 and 2 |
| Year 3 accuracy within selected group low (0.13, 0.11) vs checks (0.74, 0.76) | No | High | Fixes 1, 2, 7, 9. Key point for anyone ranking only top candidates |
| Year 2 composition (79 / 68 / 87, plus 289 repeated, 523 total, 70 dropped for poor adaptation) | Partly | Medium | Fix 6 |
| Training site changes which accessions are selected (only 1 common accession between Anjiro and Behenjy for PGV), Behenjy data predicted TPW better | No | Medium | Optional Summary or Notes line: `Different training sites selected almost entirely different accessions, and data from the cooler Behenjy site predicted panicle weight better.` |
| Anjiro year 2 flooded after cyclone, data excluded | No | Medium | Fix 6 and 7 |
| Authors' point that accuracy at the top of the distribution matters more than overall accuracy, and that multi-environment models and sparse testing may beat testing the same set everywhere | No | Medium | Notes: `- The authors suggest testing different accessions at different sites (sparse testing) with multi-environment models, and stress accuracy among the best performers over overall accuracy (p. 3407).` |
| Cross-validation accuracies (means 0.38 / 0.53 / 0.70) | No | Low to medium | Fix 2 |
| Broad-sense heritability (HD 0.95 to 0.98, STW 0.62 to 0.73, TPW 0.56 to 0.61, data not shown) | No | Low | Optional Key numbers row |
| Marker data: 186,229 SNPs after filtering, Beagle imputation, rrBLUP and BGLR | No | Low | Optional Methods detail |
| Donor details (IRIS 313-11949 from China, ind1A, top 3% for TPW in year 2. IRIS 313-7832 from year 1 set, top 3 at Ankazo) | Names only | Low | Optional |
| Authors' conclusions | Yes | High | |

## Template compliance

- Summary word count: 371, below the 400 to 500 target. The replacement in fix 1 is 475 words.
- Gist: 25 words, under 30. It says what the paper shows. OK.
- Keywords: 11, within 8 to 12. OK.
- Questions: 5, within 4 to 7. OK.
- House style: no em dashes or semicolons in the prose sections. tricot and maniva do not appear. OK.
