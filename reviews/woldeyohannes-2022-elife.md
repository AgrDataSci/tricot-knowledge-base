# Card review: woldeyohannes-2022-elife

- **Card:** papers/woldeyohannes-2022-elife.md
- **Source:** papers-pdf/woldeyohannes-et-al-2022.pdf (25 pages)
- **Reviewed:** 2026-11-23, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 58 |
| Supported | 48 |
| Imprecise | 7 |
| Not in source | 3 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 6 |
| Metadata issues | 3 |

The card is accurate on design, sample sizes, heritabilities, GWAS and genomic offset, and its Notes already catch the women's Table 3 coefficients and the uneven gender split by site. The most important fix is the Plackett-Luce sentence in the Summary. It states that scores were "converted to orderings within farmer", which the paper never describes (p. 16), and it presents Table 3 as support for the gender trait weights, although Table 3 partly disagrees with the text (p. 6 versus p. 12). Smaller fixes concern the ideotype ("tall" is not in the source), the origin of the improved lines, two stated limitations that the authors did not state, gist length and keyword count.

## Fixes needed

1. **Plackett-Luce sentence (Summary, paragraph 3).** The card says the scores were analysed "after the scores were converted to orderings within farmer" and that this "gave the gender-specific coefficients in Table 3". The source only says the Plackett-Luce model was used to analyse OA and that traits were linked to OA with a linear model fitted by an ADMM algorithm (p. 16). It does not say how one-to-five scores became rankings. The pooled result in Table 3 (p. 12) is the robust one: grain yield positive (p < 0.001), plant height negative (p < 0.001), grain filling period positive (p = 0.023). Replace with:
   > Overall appreciation scores were analysed with a Plackett-Luce model linked to agronomic traits. Across all farmers, higher grain yield and a longer grain filling period went with higher worth, and taller plants with lower worth, once the other traits were accounted for (Table 3).

   And add to Notes:
   > - The paper does not describe how the one-to-five scores were turned into rankings for the Plackett-Luce model, or how ties were handled (Methods, p. 16). Check the scripts before reusing the approach.

2. **Table 3 versus text on gender trait weights (Notes).** The text says plant height and grain filling period were very important for men and that appreciation went with yield regardless of gender (p. 6). In Table 3 (p. 12) the men's plant height coefficient is negative (−0.0114) and their grain filling period is not significant (p = 0.149). The women's grain yield coefficient is negative and significant (−0.00084, p = 0.003). The card's Note only covers the size of the women's coefficients. Add to Notes:
   > - Table 3 does not fully match the text. The text says plant height and grain filling period mattered most for men (p. 6), but in Table 3 men's plant height coefficient is negative and their grain filling period is not significant (p = 0.149). Women's grain yield coefficient is negative (p = 0.003), although the text says appreciation went with yield regardless of gender. The text's gender statements seem to rest on the correlations in Figure 3A rather than on Table 3.

3. **Ideotype (Summary, paragraph 3).** The card says top-ranked varieties shared the trait combination "tall, high-yielding and fast-maturing". The source says high yielding, high biomass and fast maturing (p. 6). "Tall" is not stated and sits badly with the negative plant height coefficient in Table 3. Replace "tall, high-yielding and fast-maturing" with:
   > high-yielding, high-biomass and fast-maturing

4. **Heritability interpretation (Summary, paragraph 3).** The card says "so farmer scores are a repeatable, genetically determined trait". The source says evaluations were highly heritable and fully comparable to agronomic traits (p. 6). "Genetically determined" is stronger. Also, grain yield is low only when combined across locations. Within location its H2 is 0.92 and 0.93, above OA at 0.71 and 0.87 (Tables 1 and 2, pp. 10 to 11). Replace "so farmer scores are a repeatable, genetically determined trait" with:
   > so farmer scores are highly heritable, at a level comparable to agronomic traits

   And add to Notes:
   > - The gap between overall appreciation (H2 0.81) and grain yield (0.42) holds only for values combined across locations. Within location, grain yield H2 was 0.92 at Adet and 0.93 at Akaki, above overall appreciation at 0.71 and 0.87 (Tables 1 and 2). Location explained 67% of yield variance (p. 6). Do not quote the comparison as farmer scores being more heritable than yield in general.

5. **Origin of improved lines (Methods, Panel).** The card says the 321 farmer varieties and 45 improved varieties came "from a 3,850-accession EBI collection". The source says improved varieties were obtained from Ethiopian agricultural research centres (p. 15). Replace the first sentence of the Panel bullet with:
   > 321 farmer varieties selected from a 3,850-accession EBI collection, all 45 improved varieties released up to the panel's assembly (from Ethiopian research centres), plus seven wild Eragrostis accessions.

6. **Stated limitations, items 3 and 4.** The authors do not say their farmers were unrepresentative, and they do not state that the genomic offset is not a yield prediction. Both are reasonable reviewer points but are already covered by not_established or belong in Notes. Replace the two bullets with limitations the authors do state:
   > - The design cannot fully separate the effects of geography, environment and social factors on genetic distance (p. 4).
   > - The causes of gender differences in teff trait preference need further study, including teff's double use as food and feed (p. 6).
   > - Candidate genes have not been validated, especially where signals may be confounded by population structure (p. 10).

   And move the first removed point to Notes as:
   > - The farmers were recognised expert teff growers chosen with agricultural officers (p. 16). The paper does not claim they represent teff farmers in general (card writer's note).

7. **Breeding investment (Summary, paragraph 1).** "has had little breeding investment" is stronger than the source, which says teff breeding has been underway for decades, but yields remain low and the potential of farmer varieties is undisclosed (p. 3). Replace "and has had little breeding investment" with:
   > whose yields remain low despite decades of breeding

8. **Conclusion hedge (Summary, last sentence).** The source says transdisciplinary approaches "may efficiently propel" farmer varieties into breeding (p. 1). Replace "can bring" with:
   > may help bring

9. **pladmm (Methods, Farmer evaluation).** The source names an ADMM algorithm (Yildiz et al. 2020) with a linear model, not the package "pladmm" (p. 16). Replace "with an alternating directions method of multipliers (pladmm)" with:
   > with a linear model fitted by an alternating directions method of multipliers (ADMM) algorithm (the R package is not named in the paper)

10. **Gist (30 words, must be under 30).** Replace with (28 words):
   > Farmer scores of 366 Ethiopian teff accessions were highly heritable, women and men weighted traits differently but preferred one ideotype, and genomic offset peaked south of lake Tana

11. **Keywords (14, maximum 12).** Replace with:
   > teff, farmer varieties, participatory variety selection, farmer appreciation, Likert scores, Plackett-Luce, gender, heritability, GWAS, genomic offset, climate change, Ethiopia

12. **License.** The PDF says Creative Commons Attribution License with no version (p. 1). Replace with:
   > CC BY (Creative Commons Attribution License, version not stated in the PDF)

13. **not_established.** Good but should cover the gender point and the Likert-to-ranking step. Replace with:
   > that candidate genes near QTNs are causal, since low-density genotyping and population structure confound associations; that the two common-garden locations represent the range of teff environments; that the genomic offset predicts yield loss; that women and men prefer different teff varieties, since both chose the same ideotype and gender is confounded with site; that the paper validates converting Likert scores to rankings; that farmer scores are more heritable than yield within a location

14. **Figure numbering (Notes).** See Source issues. Add:
   > - In the text, references to Figures 2 and 3 are swapped. Farmer correlations, top-ranked genotypes and the Venn diagram are in Figure 3 (p. 9), and the Fst and bioclimatic panels are in Figure 2 (p. 7).

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Data-driven, participatory characterization ... current and future climates | Same (p. 1) | Supported |
| authors | Woldeyohannes AB, Iohannes SD, ... Dell'Acqua M | Ten authors, same order (p. 1). First two contributed equally | Supported |
| year | 2022 | Published 2 September 2022 (p. 1) | Supported |
| journal | eLife | eLife (p. 1) | Supported |
| article | 11, e80009 | eLife 2022;11:e80009 (p. 1) | Supported |
| type | research article | "Research article" (p. 1) | Supported |
| doi | https://doi.org/10.7554/eLife.80009 | Same (p. 1) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution License, no version given (p. 1) | Imprecise (fix 12) |
| data | SRA PRJNA758057, EBI on request, GitHub mdellh2o/TeffDiversityPanel with swh id, tricot-analysis-workflows | First three match Data availability (p. 20). tricot-analysis-workflows link not in source | Supported. Workflow link: Not checked (no web access) |
| open_copy | DOI | Not checkable | Not checked (no web access) |
| software | PlackettLuce, ASReml-R, rMVP, gradientForest, adegenet | All cited in Methods (pp. 16 to 18). CRAN version note: Not checked (no web access) | Supported |
| crops | teff | Teff (p. 1) | Supported |
| region | Ethiopia, Adet (Amhara), Akaki (Oromia) | p. 16 | Supported |
| gist | 30 words, heritable appreciation, gender trait weights, lake Tana | pp. 6, 10 | Supported in content, too long (fix 10) |
| not_established | three items | Consistent with pp. 8, 10, 12, 13 | Supported, could be stronger (fix 13) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Dell'Acqua group at SSSA, de Sousa an author, panel of 321 farmer varieties and 45 improved lines with genomics, agronomy, farmer and climate data | Supported | pp. 1, 3 | |
| 2 | Summary | Teff is NUS, feeds much of Ethiopia, little breeding investment | Imprecise | pp. 1, 3 | Breeding underway for decades (fix 7) |
| 3 | Summary | 12,153 SNPs, ten clusters, high admixture | Supported | pp. 3 to 4 | |
| 4 | Summary | Genetic distance followed geographic and environmental distance | Supported | p. 4 (Mantel r 0.31 and 0.352) | Authors say design cannot untangle factors |
| 5 | Summary | Clusters linked to warmer or cooler and wetter areas, Tigray most separated | Supported | p. 4 | |
| 6 | Summary | Improved varieties narrow genetic base | Supported | p. 4 | |
| 7 | Summary | Adet and Akaki, 2018, alpha lattice, two reps, phenology, morphology, yield | Supported | p. 16 | |
| 8 | Summary | 35 farmers (15 women, 20 men), PA and OA 1 to 5, gender groups of five, near maturity | Supported | pp. 4, 16 | |
| 9 | Summary | OA H2 0.81, GY H2 0.42 | Supported | Tables 1 and 2, pp. 10 to 11 | |
| 10 | Summary | So farmer scores are a repeatable, genetically determined trait | Imprecise | p. 6 | Stronger than source, within-location GY higher (fix 4) |
| 11 | Summary | Appreciation correlated with yield and components regardless of gender | Supported | p. 6 | |
| 12 | Summary | Women weighted biomass and panicle weight, men plant height and GFP | Supported | p. 6 | Text only. Table 3 partly disagrees (Source issues, fix 2) |
| 13 | Summary | Top-ranked by women and men differ in background, same traits: tall, high-yielding, fast-maturing | Imprecise | p. 6 | Source: high biomass, not tall (fix 3) |
| 14 | Summary | PL model after conversion to orderings within farmer, gender coefficients in Table 3 | Not in source | p. 16, Table 3 p. 12 | Conversion step not described (fix 1) |
| 15 | Summary | Several farmer varieties matched or exceeded improved lines | Supported | p. 6 | |
| 16 | Summary | EBI 9551 short GFP with high yield and appreciation | Supported | p. 8 | |
| 17 | Summary | 91 QTNs, 43 bioclimatic, 2A locus for GY, GFR, OA | Supported | p. 8 | |
| 18 | Summary | GF to 2070, four RCPs, highest offset south of lake Tana, less rain, more hot nights | Supported | pp. 10 to 11, 13 | |
| 19 | Summary | Scores carry genetic signal and feed a ranking model, gender differences with same ideotype | Supported | pp. 6, 12 | Card's own framing, fine |
| 20 | Summary | Authors conclude transdisciplinary work can bring farmer varieties into breeding | Imprecise | p. 1 ("may efficiently propel") | Hedge lost (fix 8) |
| 21 | Methods | 321 + 45 from 3,850 EBI collection, plus seven wild | Imprecise | p. 15 | Improved lines from research centres (fix 5) |
| 22 | Methods | ddRAD, 12,153 SNPs, DAPC ten clusters, ADMIXTURE | Supported | pp. 3, 15, 17 | |
| 23 | Methods | Two locations, alpha lattice, two reps, 2018 main season, traits | Supported | p. 16 | |
| 24 | Methods | BLUPs and H2 with ASReml-R | Supported | p. 17 | |
| 25 | Methods | 35 farmers, PA and OA 1 to 5, simultaneous scoring in groups of five | Supported | p. 16 | |
| 26 | Methods | PL model, traits linked with ADMM (pladmm) | Imprecise | p. 16 | Package name not in source (fix 9) |
| 27 | Methods | WorldClim 2, VIF pruning, HadGEM2-ES, 2070, RCP2.6 to 8.5 | Supported | p. 16 | Rainfall and temperature trends used a 12-model ensemble (p. 18) |
| 28 | Methods | FarmCPU in rMVP, FDR 5%, LD-block candidate genes, GF | Supported | pp. 18 to 19 | |
| 29 | Limitations | Low-density genotyping and structure confound, candidates preliminary | Supported | pp. 8, 10 | |
| 30 | Limitations | Two locations cannot capture full G×E, call for multilocation and decentralised testing | Supported | p. 12 | |
| 31 | Limitations | Farmers were expert growers, not representative | Not in source | p. 16 | Not stated by authors (fix 6) |
| 32 | Limitations | Genomic offset is mismatch, not yield prediction | Not in source | p. 13 (caption calls it mismatch) | Not stated as a limitation (fix 6) |
| 33 | Key numbers | 366 accessions, 321 + 45 | Supported | pp. 1, 3 | |
| 34 | Key numbers | 12,153 SNPs | Supported | p. 3 | LD-pruned set |
| 35 | Key numbers | 10 clusters | Supported | p. 4 | |
| 36 | Key numbers | 35 farmers, 15 women, 20 men | Supported | pp. 3, 16 | |
| 37 | Key numbers | 1 to 5 scale | Supported | p. 16 | |
| 38 | Key numbers | OA H2 0.81 | Supported | Table 1, p. 10 | |
| 39 | Key numbers | GY H2 0.42 across locations | Supported | Table 2, p. 11 | |
| 40 | Key numbers | PA H2 0.48 | Supported | Table 1, p. 10 | |
| 41 | Key numbers | 91 QTNs, 43 bioclimatic | Supported | p. 8 | |
| 42 | Key numbers | 2070 horizon | Supported | pp. 10, 16 | |
| 43 | Notes | Women's PL intercept 15.6, panicle weight 4.4, suggests different scaling | Supported | Table 3, p. 12 | Inference is labelled as a suggestion |
| 44 | Notes | OA H2 by gender and location 0.53 to 0.88 | Supported | Table 1, p. 10 (0.53 men Adet, 0.88 men Akaki) | |
| 45 | Notes | 10 women and 15 men at Adet, 5 of each at Akaki, gender and gender by location significant | Supported | pp. 6, 16 | Interpretation as partly a site effect is fair |
| 46 to 58 | Frontmatter | 13 checkable fields | 12 Supported, 1 Imprecise (license) | See Metadata check | |

The Note that AgrDataSci/teff-breeding-elife holds the EtNAM durum wheat scripts cannot be checked against the source and is not counted.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Table 3 disagrees with the text on gender trait weights. Men's plant height is negative and GFP not significant. Women's grain yield is negative | Text p. 6, Table 3 p. 12 | Partly (only the size of women's coefficients) | See fix 2 |
| The paper does not describe how Likert scores were turned into rankings or how ties were handled | Methods p. 16 | No (the card asserts a conversion step instead) | See fix 1 |
| In-text references to Figures 2 and 3 are swapped (e.g. "Figure 2A" for the correlation heatmap and "Figure 2G" for the Venn diagram, which are Figure 3A and 3G) | pp. 4, 6, 8 | No | See fix 14 |
| Significance legend of Table 3 is garbled ("0.05 < p < 0.01", "0.01 < p < 0.001") | p. 12 | No | Low importance. Optional: "- The star legend in Table 3 has reversed inequalities. Read it as one star for p < 0.05, two for p < 0.01, three for p < 0.001." |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Within-location H2 of grain yield (0.92, 0.93) higher than OA (0.71, 0.87) | No | High | Notes text in fix 4 |
| Pooled Plackett-Luce result: yield and GFP positive, plant height negative | No | High | Summary text in fix 1 |
| Farmer protocol: selected with agricultural officers, focus groups and training before scoring, interpreters, scores recorded individually (p. 16) | Partly | Medium | Add to Methods, Farmer evaluation: "Farmers were recognised local experts chosen with agricultural officers, joined focus groups and training before scoring, worked with interpreters (Amharic and Oromo), and each score was recorded individually." |
| Variance partition: location explained 75% of biomass and 67% of yield variance, genotype explained 92% of days to heading and 86% of days to maturity (p. 6) | No | Medium | Add to Key numbers: "\| 67% \| Share of grain yield variance explained by location \| This paper \|" |
| Trial sites were high-potential areas, which helps explain the high OA of improved varieties (p. 6) | No | Medium | Add to Summary after the farmer varieties sentence: "Improved lines scored high, which the authors link to the high-potential trial sites." |
| Authors' own limitations on design, gender causes and candidate validation (pp. 4, 6, 10) | No | Medium | See fix 6 |
| Top-ranked defined as 90th percentile of OA. Farmer varieties benchmarked against the 75th percentile of improved lines. Venn counts read off Figure 3G are approximate (about 44 farmer varieties beat improved lines on GFP alone, 12 on PA alone) (pp. 9, 17) | No | Low | Optional Note |
| Allele turnover best predicted by geographic MEM variables, then bio19 and bio13. 3,049 SNPs in 521 LD blocks predictive (p. 8) | No | Low | Optional |
| Assisted migration suggested, with ecological and socioeconomic caveats (p. 11) | No | Low | Optional |

## Template compliance

- Summary word count: 448 (within 400 to 500). After fixes 1, 3, 4, 7 and 8 it will be about 460. Recount after editing.
- Gist: 30 words, must be under 30 (fix 10).
- Keywords: 14, must be 8 to 12 (fix 11).
- Questions: 6 (within 4 to 7). The first question ("Can farmer scores on a Likert scale be analysed with a ranking model") is answered only by use, not by test. Consider "How were farmer Likert scores analysed with a ranking model?"
- House style: tricot and maniva do not appear in capitalised form. No issues.
