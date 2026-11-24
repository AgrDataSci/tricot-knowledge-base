# Card review: gesesse-2023-pnas

- **Card:** papers/gesesse-2023-pnas.md
- **Source:** papers-pdf/gesesse-et-al-2023.pdf (10 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 59 |
| Supported | 53 |
| Imprecise | 5 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 7 (2 high, 5 medium) |
| Metadata issues | 3 |

The card is accurate on almost every number and follows the paper's argument well. Page numbers printed on the PDF match the PDF page numbers. The most important fix is to add a not_established field and to say that the genomic selection accuracies are low and fail at Kulumsa (p. 4, Fig. 3, p. 6), because the gist and summary could otherwise be read as a strong, general prediction result. One summary sentence also pairs 0.41 with 0.02 in a way that mixes two different comparisons (p. 5, Fig. 3C).

## Fixes needed

1. **not_established is missing.** The paper is easy to stretch: absolute accuracies are low, the scores come from on-station plots, and the high-potential site was predicted negatively (p. 4, p. 6, p. 8). Add to the frontmatter after gist:

   `not_established: farmer appreciation scores can replace measured yield or multi-location yield trials; genomic prediction from farmer scores is accurate in absolute terms (accuracies for yield were 0.09 to 0.11); prediction from the diversity panel works in high-potential sites (Kulumsa was predicted negatively); these results come from tricot rankings or on-farm trials (scores were given on research-station plots); the farmers represent the full diversity of Ethiopian farming systems; the design explains gender differences in trait priorities; candidate genes for farmer preference were identified`

2. **Mixed comparison in the reverse-direction sentence (Imprecise).** The card says appreciation on the EtNAM predicted panel yield at 0.11 and panel appreciation at 0.41, "against 0.02 for a yield-trained model". The 0.02 is only for yield predicting panel yield. A yield-trained model predicted panel appreciation at roughly 0.32 (read off Fig. 3C, approximate), so the reader may wrongly think it scored 0.02 there too (p. 5, p. 6 Fig. 3C). Replace with:

   "In the reverse direction, appreciation measured on the EtNAM predicted panel yield at 0.11, against 0.02 for a model trained on EtNAM yield, and predicted panel appreciation at 0.41. Men's scores gave slightly higher accuracies than women's."

3. **Low accuracy and the Kulumsa failure are not mentioned (high-importance omission).** Fig. 3A and 3B show that diversity panel data predicted EtNAM performance at Kulumsa negatively, for both predictors (p. 4, p. 6). The authors call this a substantial inadequacy of the panel data for that site. Add after the sentence ending "for combined data.":

   "Accuracies were low in absolute terms and depended on the site. At Kulumsa, the high-potential site, the panel predicted EtNAM performance negatively, although the appreciation-trained model still did better than the yield-trained one. Accuracy for both traits improved when training and testing stayed within the EtNAM across locations."

4. **How scores became rankings is not described (high-importance omission for tricot users).** Each farmer's 1 to 5 scores were turned into pairwise wins, ties were dropped, and data were aggregated by EtNAM family before the Plackett-Luce model (p. 9). Fig. 2 is a Plackett-Luce tree that splits by location, then by gender in Adet and Kulumsa (p. 5). Add a Methods bullet after Farmer scoring:

   "- **Ranking analysis.** Each farmer's scores were converted to pairwise wins between lines (ties dropped) and aggregated by EtNAM family. A Plackett-Luce tree then estimated family worth by location and gender, against the reference variety Asassa, with trait BLUPs used to explain choices."

5. **"Some EtNAM families outperformed the reference modern variety everywhere" (Imprecise).** The source says that in all cases individual families "could outperform" Asassa (p. 4). In Fig. 2 the Geregera node shows family worths close to the reference, so "everywhere" reads stronger than the figure (p. 5, read off chart, approximate). Replace with:

   "In each location and farmer group, some EtNAM families could reach a higher worth than the reference modern variety, Asassa."

6. **EtNAM crossing (Imprecise).** The card says landraces were crossed with an elite line. The source says 50 Ethiopian landraces plus the Italian improved variety Bidi were crossed with Asassa (p. 8). One of the 12 families studied (N51) has no landrace parent (p. 9). Replace "Landraces from that panel were crossed with an elite line of international pedigree to create the Ethiopian nested association mapping population (EtNAM)." with:

   "Fifty landraces from that panel and one Italian variety (Bidi) were crossed with Asassa, a modern variety of international pedigree, to create the Ethiopian nested association mapping population (EtNAM)."

7. **~40% attribution (Imprecise).** The figure is cited to Mausch et al. 2021, ref. 17 (p. 2). The template asks for the original source. Replace the Primary source cell with:

   "Mausch et al. 2021 (ref. 17), cited in this paper"

8. **"on-station fields do not reflect farmers' input levels" (Imprecise, minor).** The source says experimental stations are "seldom representative" of farmer fields (p. 8). Replace with:

   "and that on-station fields are seldom representative of farmers' input levels."

9. **data field holds outside knowledge (Not in source).** The PDF lists only the Dryad DOI and the EtNAM.GS GitHub repository (p. 9). The pointers to AgrDataSci/teff-breeding-elife, the "mislabelled" remark and tricot-analysis-workflows are not in the source, and I could not open those repositories to check them. Replace the data field with:

   `data: raw data on Dryad (https://doi.org/10.5061/dryad.w6m905qrv); scripts at https://github.com/mdellh2o/EtNAM.GS`

   and add to Notes:

   "- Outside the source (team knowledge, not checked against the PDF): scripts that convert farmer ratings to Plackett-Luce rankings for this dataset are reported to sit in https://github.com/AgrDataSci/teff-breeding-elife and are curated in https://github.com/AgrDataSci/tricot-analysis-workflows (use-cases/can-farmer-ratings-be-analysed-as-rankings)."

10. **Farmer scoring and trial details (medium omissions).** Replace the Trials and Farmer scoring bullets with:

   "- **Trials.** Adet and Geregera in the 2016 main season and Kulumsa in 2017, fully replicated, 10,400 plots scored. The diversity panel was grown earlier in Geregera and Hagreselam (2012 and 2013).
   - **Farmer scoring.** Local expert wheat growers, split by gender into groups of five, scored each plot for overall appreciation on a 1 to 5 scale when half the plots had flowered. Different farmer groups scored at each site and on the diversity panel."

11. **Stated limitations (medium omissions).** Add:

   "- The farmers represent smallholders in the wheat-growing areas, not the full diversity of Ethiopian farming systems.
   - The design allows only a partial breakdown of farmers' appreciation into plant traits.
   - QTL positions found in one EtNAM family may not hold in other genetic backgrounds."

12. **Source issue on N45 and N51 not flagged.** Add to Notes:

   "- Source issue: the text (p. 4) says family N45 should be prioritized for Geregera and Adet but not Kulumsa, and that N51 had the highest worth in Geregera. Fig. 2 (p. 5) shows N45 and N51 with high worth in Kulumsa and close to the reference in Geregera. Check Fig. 2 before using these family recommendations."

13. **software field format (template).** Replace "check the current CRAN version" with the version and dates in template form, for example "(vX.Y on CRAN, published YYYY-MM-DD, checked YYYY-MM-DD)", after checking CRAN. The source cites the package paper (ref. 30) but does not name a version.

14. **Optional gist tweak.** The gist is supported but does not hint at the low accuracies. Optional replacement (27 words):

   `gist: Farmer appreciation of 1,200 EtNAM durum wheat lines is heritable and, in genomic selection, predicts grain yield across panels better than yield itself, though accuracies stay low`

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Genomics-driven breeding for local adaptation of durum wheat is enhanced by farmers' traditional knowledge | Same (p. 1), curly apostrophe in source | Supported |
| authors | Gesesse CA ... Dell'Acqua M (11 names) | Same 11 authors in same order (p. 1). Layer-1 flag on Dell'Acqua is only the apostrophe style | Supported |
| year | 2023 | Published March 27, 2023 (p. 1) | Supported |
| journal | Proceedings of the National Academy of Sciences | PNAS (p. 1) | Supported |
| article | 120(14), e2205774119 | Vol. 120, No. 14, e2205774119 (p. 1) | Supported |
| type | research article | "Research article" (p. 1) | Supported |
| doi | https://doi.org/10.1073/pnas.2205774119 | Same (p. 1) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution License 4.0 (p. 1) | Supported |
| data | Dryad, EtNAM.GS, plus AgrDataSci repos | Only Dryad and EtNAM.GS (p. 9) | Not in source (AgrDataSci part). See fix 9 |
| software | PlackettLuce R package | Plackett-Luce model citing the PlackettLuce package paper, ref. 30 (p. 4, p. 9). No version given | Supported (template format issue, fix 13) |
| crops | durum wheat | Durum wheat. The diversity panel also has some bread wheat landraces (p. 8) | Supported |
| region | Ethiopia (Adet, Geregera, Kulumsa; diversity panel also at Hagreselam) | p. 2, p. 9 | Supported |
| gist | Farmer appreciation ... heritable ... predicts grain yield in new environments better than models trained on yield | H2 0.45 (p. 2). OA beat GY as predictor of yield in both directions (p. 4 to 5). Accuracies are low | Supported (optional tweak, fix 14) |
| not_established | missing | Needed, see fix 1 | Missing |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Smallholders in SSA select varieties with traditional knowledge | Supported | Abstract (p. 1) | |
| 2 | Summary | Only about 40% of beneficiaries adopt new varieties | Supported | p. 2, ref. 17 | Cited figure, see fix 7 |
| 3 | Summary | Study tests integrating farmer evaluations into genomics-driven breeding, Ethiopian durum wheat | Supported | p. 1 to 2 | |
| 4 | Summary | Panel of 400 mostly traditional varieties phenotyped and scored earlier | Supported | p. 2, p. 8 (372 landraces, 28 improved) | |
| 5 | Summary | Landraces crossed with an elite international line to make EtNAM | Imprecise | p. 8 to 9 | Bidi omitted, N51 has no landrace parent. Fix 6 |
| 6 | Summary | 1,200 RILs, 12 families, replicated, three sites, 10,400 plots | Supported | p. 2 | |
| 7 | Summary | Separate women and men groups, OA 1 to 5 near flowering | Supported | p. 2, p. 9 | |
| 8 | Summary | Agronomic traits measured, both sets genotyped | Supported | p. 2, p. 9 | |
| 9 | Summary | Appreciation behaved like a quantitative trait | Supported | Section heading (p. 2) | |
| 10 | Summary | H2 0.45 for OA, 0.49 for GY | Supported | p. 2, Table 1 (p. 4) | |
| 11 | Summary | H2 men 0.54, women 0.32 | Supported | p. 2, Table 1 | |
| 12 | Summary | 26 of the top 5% chosen by both | Supported | p. 2 to 3 | |
| 13 | Summary | OA correlated with GY everywhere, 0.41 to 0.66 | Supported | p. 3 | |
| 14 | Summary | In Geregera OA also tracked yield stability | Supported | p. 4 | Source hedges with "suggesting" and "may" |
| 15 | Summary | Plackett-Luce showed drivers differ by site and gender | Supported | p. 4, Fig. 2 (p. 5) | |
| 16 | Summary | Early maturity in Geregera, yield and biomass in Kulumsa | Supported | p. 4 | Kulumsa also shorter flowering and heading |
| 17 | Summary | Some families outperformed the reference everywhere | Imprecise | p. 4 ("could outperform"), Fig. 2 | Fix 5 |
| 18 | Summary | GY-trained panel model could not predict EtNAM yield | Supported | p. 4, Fig. 3A (about −0.12, read off chart) | |
| 19 | Summary | OA-trained panel model predicted EtNAM yield at 0.09 | Supported | p. 4 | |
| 20 | Summary | OA-trained model predicted EtNAM OA above 0.20 on combined data | Supported | p. 4, Fig. 3B (about 0.24, approximate) | |
| 21 | Summary | Reverse: 0.11, 0.41, against 0.02 for yield-trained | Imprecise | p. 5, Fig. 3C | 0.02 applies only to yield. Fix 2 |
| 22 | Summary | Authors suggest farmers integrate heritable components and multi-season experience | Supported | p. 5 | Source frames these as hypotheses. "Suggest" fits |
| 23 | Summary | OA loci on several chromosomes, some shared with yield and grain weight, 6B linked to no trait | Supported | p. 7 | |
| 24 | Summary | Family-specific maps gave 382 partially overlapping QTL | Supported | p. 7 | QTL for all traits, not only OA |
| 25 | Summary | Propose on-station PVS plus GS early, then on-farm via 3D-breeding | Supported | p. 8 | |
| 26 | Summary | Farmer scores not the only driver, on-station fields do not reflect farmer inputs | Imprecise | p. 8 ("seldom representative") | Minor. Fix 8 |
| 27 | Methods | Material: 1,200 RILs, 12 families, 400-entry panel, both genotyped | Supported | p. 2, p. 8 to 9 | 100 RILs per family |
| 28 | Methods | Trials: three sites, fully replicated, 10,400 plots | Supported | p. 2 | |
| 29 | Methods | Farmer scoring 1 to 5 Likert, separate gender groups | Supported | p. 9 | |
| 30 | Methods | Analysis: BLUPs, H2, Plackett-Luce, GS, GWAS, family QTL | Supported | p. 9 | Stability indices also used |
| 31 | Limitations | Cannot capture subtle gender dynamics | Supported | p. 4 | |
| 32 | Limitations | More fertilizer and weeding on station, may push scores toward yield potential | Supported | p. 8 | |
| 33 | Limitations | High cost per data point, limited environmental coverage | Supported | p. 8 | Source cites the tricot paper (ref. 43) here |
| 34 | Limitations | Mapping resolution too low for candidate genes | Supported | p. 8 | |
| 35 | Key numbers | 1,200 RILs, 12 families | Supported | p. 2 | |
| 36 | Key numbers | 10,400 plots | Supported | p. 2 | |
| 37 | Key numbers | ~40% adoption, "Cited in this paper" | Imprecise | p. 2, ref. 17 | Name the original. Fix 7 |
| 38 | Key numbers | H2 0.45 / 0.49 | Supported | p. 2 | |
| 39 | Key numbers | H2 0.54 / 0.32 | Supported | Table 1 (p. 4) | |
| 40 | Key numbers | 26 lines in top 5% | Supported | p. 2 to 3 | |
| 41 | Key numbers | 0.41 to 0.66 | Supported | p. 3 | |
| 42 | Key numbers | 0.09 | Supported | p. 4 | |
| 43 | Key numbers | 0.11 / 0.41 / 0.02 | Supported | p. 5 | Row wording is correct |
| 44 | Key numbers | 382 QTL | Supported | p. 7 | |
| 45 | Notes | Not a tricot trial, on-station participatory evaluation | Supported | p. 8 (centralized, on-station PVS) | |
| 46 | Notes | de Sousa co-author, contributed analytic tools | Supported | p. 1 | He also analysed data |

Metadata rows (13 checkable fields, not counting the missing not_established) add 12 Supported and 1 Not in source to the totals above.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Text says N45 should be prioritized for Geregera and Adet but not Kulumsa, and N51 had the highest worth in Geregera. Fig. 2 shows N45 and N51 high in Kulumsa and close to the reference in Geregera (read off chart, approximate). The site names look swapped | p. 4 vs Fig. 2 (p. 5) | No (card does not cite these families) | See fix 12 |
| Fig. 2 caption sends readers to SI Table S1 for drivers of choice. The text uses Table S1 for the top 5% lines and Table S3 for drivers | p. 3 to 5 | No | Low importance, Notes text not needed |
| A correlation is reported as "R2 = −0.29". A coefficient of determination cannot be negative, and Methods say Spearman correlations were used | p. 4, p. 9 | No | Low importance, Notes text not needed |
| Reference mismatches: R/qtl2 is cited to a Collaborative Cross paper (ref. 64), and the text uses JoinMap 5 while ref. 63 is JoinMap 4 | p. 9 to 10 | No | Low importance, Notes text not needed |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: integrate farmer knowledge into genomics-driven breeding | Yes | High | |
| Design: DP plus 1,200 EtNAM RILs, three sites, 10,400 plots | Yes | High | |
| Conversion of 1 to 5 scores to pairwise rankings, ties dropped, Plackett-Luce tree | No | High | Fix 4 |
| Low absolute accuracies and negative prediction at Kulumsa | No | High | Fix 3 |
| Heritability, OA-yield correlation, top 5% overlap | Yes | High | |
| Main GS results 0.09, 0.11, 0.41, 0.02 | Yes | High | Fix wording, fix 2 |
| Farmer setup: groups of five, scoring each plot, different groups per site and for DP | No | Medium | Fix 10 |
| Trial years (2016, 2017, DP 2012 to 2013) | No | Medium | Fix 10 |
| Farmers not representative of all Ethiopian farming systems | No | Medium | Fix 11 |
| Within-EtNAM cross-location GS improved accuracy for GY and OA | No | Medium | Included in fix 3 |
| Farmers preferred high yielding, tall, thick, early plants (OA mostly negatively correlated with phenology) | Partly (Geregera only) | Medium | Optional: "Across sites, farmers favoured high-yielding, tall plants with early maturity." |
| Men's OA gave higher accuracies EtNAM to DP | No | Low | Included in fix 2 |
| OA predicted yield components (biomass 0.15, seeds per spike 0.15, plant height 0.26, grain weight 0.27) | No | Low | Optional Key numbers row |
| GWAS: 81 MTAs, 10 for OA | No | Low | Optional Key numbers row |
| Family-level advice (N45, N51) | No | Low | Only with the source-issue note, fix 12 |
| Authors' limitations | Mostly | Medium | Fix 11 |
| Conclusion: OA usable in GS and QTL mapping, EtNAM lines now in prebreeding trials | Mostly | Low | |
| Tricot (ref. 43) cited as the basis for the cost and coverage limitation of central PVS | No | Low | Optional Notes line |

## Template compliance

- Summary word count: 414 (target 400 to 500). Fixes 2, 3 and 5 add about 60 words, still under 500.
- Gist: 27 words, under 30. It says what the paper shows.
- Keywords: 12, within 8 to 12.
- Questions: 5, within 4 to 7.
- House style: tricot appears in lowercase. maniva does not appear. No problems.
- not_established is missing (fix 1). software field lacks version and dates in template form (fix 13).
