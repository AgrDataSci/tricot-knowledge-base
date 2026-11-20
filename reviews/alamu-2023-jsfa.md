# Card review: alamu-2023-jsfa

- **Card:** papers/alamu-2023-jsfa.md
- **Source:** papers-pdf/alamu-et-al-2023.pdf (13 pages, printed pages 4573 to 4585. PDF page = printed page minus 4572.)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 52 (37 body claims, 15 frontmatter fields) |
| Supported | 41 |
| Imprecise | 8 |
| Not in source | 1 |
| Contradicted | 2 |
| Source issues (problems in the source itself, not card errors) | 11 |
| Important omissions | 4 high, 9 medium |
| Metadata issues | 4 |

Most numbers in the card are correct, and the instrumental, heritability and NIRS parts are well summarised. But the main tricot result is wrong: the card says city consumers converged on a check called "TMS6", while the Plackett-Luce tree split consumers by ethnic group only and the best genotype was TMS30572 (p. 4579 and Fig. 6, p. 4583). The card also misses gari solubility as a preference driver, the authors' warning that color was not measured on the eba used in consumer tests, and it lists hardness as a consumer-driven breeding target although hardness was not significant overall. The data field contradicts the data availability statement, and the author list drops two co-authors, including the tricot team member Kauê de Sousa.

## Fixes needed

1. **Contradicted tricot result (summary, paragraph 4).** The card says "city consumers converging on the breeders' check TMS6". The source tree has a single split, on ethnic group (p = 7.1e-05), into node 2 (Hausa, Ibo, Igbira, Tiv, n = 204) and node 3 (Idoma, Igede, Yoruba, n = 396) (Fig. 6, p. 4583, PDF 11). No split by city or region exists, and the authors say ethnic group mattered more than region (p. 4583). The best genotype was the improved check C6_BC, TMS30572 (p. 4579, PDF 7). "TMS6" is not a genotype in the paper (the closest label is TMEB1_MS6, a regional variety). Replace the paragraph with:

   > Across all consumers, eba was preferred when made from gari with higher L* and a* and lower b*, and when it was more cohesive (P < 0.001). Hardness had no significant effect overall. Plackett-Luce trees split consumers by ethnic group only. Hausa, Ibo, Igbira and Tiv participants (node 2, n = 204) preferred lower gari solubility and higher a*. Idoma, Igede and Yoruba participants (node 3, n = 396) also preferred higher L*, lower b*, higher cohesiveness and higher hardness. The authors link node 3's dislike of yellow gari to rare palm oil use in eba in the Yoruba-dominated southwest. They report the improved breeders' check TMS30572 as the best genotype overall and the local variety Akpu among the weakest.

2. **data field contradicts the source.** The card says "supporting information with the article". The Data Availability Statement says data are available from the corresponding author on reasonable request (p. 4584, PDF 12). The supporting information holds genotype lists (Tables S1, S2) and a cluster figure (Fig. S1), not the data. Replace with:

   > data: available from the corresponding author on reasonable request (data availability statement). Supporting information lists the genotypes (Tables S1, S2)

3. **Gist names hardness as a consumer-driven target and omits solubility.** Hardness was not significant in the overall consumer model (estimate 0.011, P = 0.23, Table 5, p. 4581, PDF 9) and only significant in node 3 (P = 0.022, Table 6, p. 4582). The authors' final conclusion names eba color, eba cohesiveness and gari solubility (p. 4583). Replace with (26 words):

   > gist: tricot rankings by 600 Nigerian consumers favor cohesive eba from brighter, redder, less yellow gari, traits that instrumental color and texture measures can screen in cassava breeding

4. **Heritability of color overstated (summary paragraph 3 and Key numbers).** The card says "Color traits were moderately heritable (above 30%)". This repeats the source text (p. 4577), but Table 4 (p. 4580, PDF 8) shows only three of eight color traits above 30% (a*_eba 0.59, b*_gari 0.42, b*_eba 0.32). L*_gari, a*_gari and ΔE_gari are 0.00, L*_eba is 0.29, ΔE_eba is 0.07. Replace the summary sentence with:

   > Three color traits had heritability above 30% (a* of eba 59%, b* of gari 42%, b* of eba 32%), while most texture traits were below 10%.

   Replace the Key numbers row with:

   > | 59% / 42% / 32% | Highest broad-sense heritability: a* of eba / b* of gari / b* of eba (40 genotypes). Other color traits 0% to 29% | This paper |
   > | <10% | Heritability of gumminess, hardness, adhesiveness, chewiness and cohesiveness | This paper |

5. **Authors incomplete and misordered.** The card lists 15 names and ends with "Maziya-Dixon B, and co-authors", which suggests more authors after her. The source has 17 authors, with de Sousa K and Dufour D between Bouniol A and Maziya-Dixon B, who is last and corresponding (p. 4573, PDF 1). de Sousa K is in people.md, so the omission also affects crediting. Replace with:

   > authors: Alamu OE, Teeken B, Ayetigbo O, Adesokan M, Kayondo I, Chijioke U, Madu T, Okoye B, Abolore B, Njoku D, Rabbi I, Egesi C, Ndjouenkeu R, Bouniol A, de Sousa K, Dufour D, Maziya-Dixon B

6. **Missing not_established.** Add:

   > not_established: that hardness drives eba preference across all consumers (significant only in the Idoma, Igede and Yoruba node); that lab eba color predicts consumer liking (color was not measured on the eba used in consumer testing); that NIRS can screen cohesiveness (R² in prediction 0.23); that instrumental texture captures stretchability; that the preferences hold beyond Osun and Benue states or for more contrasting varieties; that a* of gari is heritable in this population (H² 0)

7. **Sentence not in source (summary, last paragraph).** "whose standard operating procedures make the measurements comparable across crops and laboratories" is not in the paper. The source only says breeding programs can adopt the SOPs (p. 4574). The sentence before it ("chain of evidence ... what demand-led breeding needs") is the card's own framing and overstates the result, since the key driver, cohesiveness, had weak NIRS prediction and eba color was not measured on consumer samples (p. 4583). Replace the whole last paragraph with:

   > The authors conclude that eba color, eba cohesiveness and gari solubility are crucial quality characteristics, and that gari and eba color with instrumental hardness and cohesiveness discriminate genotypes. They note that color was not measured on the eba used in consumer testing, and call for tests with more, and more contrasting, varieties. They suggest breeders could already select on a* and b* of eba, b* of gari, L* of eba, resilience and springiness.

8. **"so instrumental texture can reliably estimate sensory profiles" needs the stretchability exception.** No instrumental attribute related to sensory stretchability, which the authors call a key eba attribute (Table 3, p. 4578, and p. 4581 to 4582). Replace the sentence with:

   > Instrumental hardness correlated with sensory hardness, and the authors report a negative correlation between instrumental adhesiveness and sensory moldability. Instrumental cohesiveness was also negatively related to moldability (r = −0.69). The authors conclude that sensory texture can be estimated from instrumental measures, but no instrumental measure tracked sensory stretchability.

9. **Stated limitation 3 is not one the authors state.** Two states is true, but the authors' own limitation is that consumer tests need a larger number of more contrasting varieties (p. 4583). Replace with:

   > - Color was not measured on the eba used in consumer testing, so the link between lab eba color and consumer liking is untested.
   > - Consumer tests need more, and more contrasting, varieties to confirm which lab traits matter.
   > - No instrumental measure tracked sensory stretchability, a key eba trait.

10. **Opening rationale slightly too strong.** "New cassava genotypes are adopted only if they meet end-user food quality" is stronger than the source, which says defining product profiles is important for successful adoption (p. 4573). Replace with:

    > New genotypes are adopted more readily when breeders know which product traits drive acceptance.

11. **Methods bullet on consumers misses the trait-linking model.** Replace with:

    > - **Consumers.** tricot test with 600 consumers in Osun and Benue states, each ranking three of ten eba samples for overall liking, taste, moldability, smoothness and stretchability (ClimMob). Plackett-Luce trees with gender, age, ethnicity, region and consumption frequency as covariates, and an ADMM extension linking gari and eba traits to log-worth.

12. **Notes additions.** Add:

    > - The authors say the preference for higher gari redness was the opposite of what they expected, and the opposite of processors' preference for lower a* in Teeken et al. 2018 (p. 4582 to 4583).
    > - a* of gari drives consumer preference here, but its heritability was 0 in the 40-genotype population (Table 4).
    > - Source inconsistencies: see the review report (heritability text versus Table 4, adhesiveness-moldability correlation, NIRS R² in prediction for gari L*).

A full revised Summary that combines fixes 1, 4, 7, 8 and 10 (496 words) follows. Paste it in place of the current Summary.

> The study aimed to define the critical quality traits of gari and eba, measure their heritability, identify instrumental methods breeders can use at medium to high throughput, and link the traits to consumer preferences. New genotypes are adopted more readily when breeders know which product traits drive acceptance.
>
> Eighty cassava genotypes in three sets (30, 40 and 10), grown at IITA sites in Nigeria in 2019–2021 and harvested at 12 months, were processed into gari and eba following RTBfoods standard operating procedures. The team measured color (L*, a*, b*) and instrumental texture (hardness, adhesiveness, cohesiveness, springiness, gumminess, chewiness, resilience). For 13 selected genotypes, 16 trained panelists also scored sensory texture on a 0 to 10 scale. Ten genotypes (advanced lines, released, regional and processor-chosen local varieties) went to tricot consumer testing with 600 consumers from rural and urban areas in Osun and Benue states. Each consumer ranked three of the ten eba samples. A Plackett-Luce extension (ADMM) linked gari and eba traits to preference.
>
> Instrumental hardness correlated with sensory hardness, and the authors report a negative correlation between instrumental adhesiveness and sensory moldability. Instrumental cohesiveness was also negatively related to moldability (r = −0.69). The authors conclude that sensory texture can be estimated from instrumental measures, but no instrumental measure tracked sensory stretchability. The first two principal components explained 85.3% of the variation in eba texture. Three color traits had heritability above 30% (a* of eba 59%, b* of gari 42%, b* of eba 32%), while most texture traits were below 10%. NIRS calibrations for eba color were good for L* (R² 0.80), fair for a* (0.66) and weak for b* (0.35). In validation, NIRS predicted chewiness (R² 0.59), hardness (0.54) and adhesiveness (0.40) reasonably, but cohesiveness poorly (0.23). The authors see screening value and call for more genotypes with wider texture variation.
>
> Across all consumers, eba was preferred when made from gari with higher L* and a* and lower b*, and when it was more cohesive (P < 0.001). Hardness had no significant effect overall. Plackett-Luce trees split consumers by ethnic group only. Hausa, Ibo, Igbira and Tiv participants (node 2, n = 204) preferred lower gari solubility and higher a*. Idoma, Igede and Yoruba participants (node 3, n = 396) also preferred higher L*, lower b*, higher cohesiveness and higher hardness. The authors link node 3's dislike of yellow gari to rare palm oil use in eba in the Yoruba-dominated southwest. They report the improved breeders' check TMS30572 as the best genotype overall and the local variety Akpu among the weakest.
>
> The authors conclude that eba color, eba cohesiveness and gari solubility are crucial quality characteristics, and that gari and eba color with instrumental hardness and cohesiveness discriminate genotypes. They note that color was not measured on the eba used in consumer testing, and call for tests with more, and more contrasting, varieties. They suggest breeders could already select on a* and b* of eba, b* of gari, L* of eba, resilience and springiness.

Optional Key numbers rows to add: `| 204 / 396 | Consumers in node 2 (Hausa, Ibo, Igbira, Tiv) / node 3 (Idoma, Igede, Yoruba) of the Plackett-Luce tree | This paper |` and `| 0.23 | NIRS R² in prediction for eba cohesiveness (validation, 10 genotypes) | This paper |`.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | "...consumer preferences. Implications for cassava breeding" | Same, with a colon before "implications" (p. 4573) | Supported (colon to period is expected) |
| authors | 15 names, then "Maziya-Dixon B, and co-authors" | 17 authors. de Sousa K and Dufour D are missing, and Maziya-Dixon B is last (p. 4573) | Imprecise |
| year | 2023 | Published online 16 March 2023. Issue is 2024 (p. 4573, footer) | Supported |
| journal | Journal of the Science of Food and Agriculture | Same (p. 4573) | Supported |
| article | 104(8), 4573-4585 (published online March 2023) | J Sci Food Agric 2024, 104: 4573–4585, issue 8 in the download stamp | Supported |
| type | research article | "Research Article" (p. 4573) | Supported |
| source | team | Teeken and de Sousa are in people.md | Supported |
| doi | 10.1002/jsfa.12518 | Same (p. 4573) | Supported |
| open_copy | doi link | Open access (p. 4573 footer) | Supported |
| license | CC BY | Creative Commons Attribution License (p. 4573 footer) | Supported |
| data | supporting information with the article | Data from the corresponding author on reasonable request (p. 4584) | Contradicted |
| crops | cassava (gari and eba) | Yes | Supported |
| region | Nigeria (Osun, Benue and IITA stations) | Ibadan for Experiments 1 and 2, Osun and Benue for Experiment 3 (p. 4574) | Supported |
| keywords | 12 terms | Fits the paper | Supported |
| gist | cohesiveness, hardness and color as breeding targets | Hardness not significant overall (Table 5). Solubility is in the authors' conclusion (p. 4583) | Imprecise |
| not_established | missing | | Missing (see fix 6) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Aims: define traits, heritability, instrumental methods, link to consumers | Supported | Abstract (p. 4573) | |
| 2 | Summary | Genotypes adopted "only if" they meet food quality | Imprecise | "important if new genotypes are to be adopted" (p. 4573) | Stronger than source. Fix 10 |
| 3 | Summary | 80 genotypes, three sets, IITA sites, 2019–2021, 12 months, RTBfoods SOPs | Supported | p. 4574 | Experiment 3 gari was made by three champion processors with regional methods (p. 4574). Fine to leave |
| 4 | Summary | Measured color and six instrumental texture traits | Supported | p. 4575 | Resilience is also measured and is among the most discriminating (p. 4577) |
| 5 | Summary | 13 genotypes, 16 panelists, 0 to 10 scale | Supported | p. 4575 | |
| 6 | Summary | Ten genotypes of four types to tricot, 600 consumers, Osun and Benue | Supported | p. 4574 to 4575 | 3 + 3 + 2 + 2 = 10 checked |
| 7 | Summary | Instrumental hardness correlated with sensory hardness, adhesiveness negatively with moldability | Supported | Text and abstract (p. 4573, 4577). Table 3 (p. 4578) | Source issue: adhesiveness r = −0.52 is not starred in Table 3 |
| 8 | Summary | So instrumental texture can reliably estimate sensory profiles | Imprecise | p. 4582 says so, but no instrumental measure relates to stretchability (p. 4577, 4581) | Fix 8 |
| 9 | Summary | First two PCs explain 85.3% of eba texture variation | Supported | p. 4577. Fig. 2: 52.3% + 33% = 85.3% (p. 4578) | |
| 10 | Summary | Consumers preferred higher L*, a*, lower b* of gari and higher cohesiveness | Supported | Table 5 (p. 4581), text p. 4577 | Correctly says gari color |
| 11 | Summary | Color traits above 30% heritability | Imprecise | Text p. 4577 vs Table 4 (p. 4580) | Only 3 of 8 color traits above 30%. Fix 4 |
| 12 | Summary | Most texture traits below 10% | Supported | Table 4 (p. 4580) | 5 of 7 below 10%. Resilience 29%, springiness 24% |
| 13 | Summary | NIRS calibration eba L* 0.80, a* 0.66, b* 0.35 | Supported | Table 1 (p. 4576), p. 4579 | Source says "moderately good" for L* and a* |
| 14 | Summary | Trees split by ethnic group, Idoma, Igede, Yoruba in one node | Supported | Fig. 6 (p. 4583), Table 6 (p. 4582) | |
| 15 | Summary | City consumers converged on breeders' check TMS6 | Contradicted | Single split on ethnic group, no region or city split. Best genotype TMS30572 (p. 4579, 4583) | Fix 1 |
| 16 | Summary | Authors conclude color plus instrumental hardness and cohesiveness are key discriminants | Supported | Abstract (p. 4573) | Final conclusion also names gari solubility (p. 4583) |
| 17 | Summary | NIRS R² in prediction 0.59 chewiness, 0.54 hardness, 0.40 adhesiveness | Supported | p. 4579, Table 1 (p. 4576) | Authors cite 0.50 as the minimum for rapid screening (p. 4579), so adhesiveness falls short |
| 18 | Summary | Models could serve screening, alternatives not cost effective, need more genotypes | Supported | p. 4579 | "at breeding scale" is a fair gloss |
| 19 | Summary | Chain of evidence from rankings to traits to screening tools | Imprecise | Card's own framing | Overstated given weak cohesiveness prediction and no eba color on consumer samples (p. 4583). Fix 7 |
| 20 | Summary | Work within RTBfoods | Supported | p. 4573, 4584 | |
| 21 | Summary | SOPs make measurements comparable across crops and laboratories | Not in source | p. 4574 says only that programs can adopt the SOPs | Fix 7 |
| 22 | Methods | 80 genotypes, three experiments, IITA, 2019–2020 and 2020–2021 | Supported | p. 4574 | |
| 23 | Methods | Gari and eba following RTBfoods SOPs | Supported | p. 4574 to 4575 | |
| 24 | Methods | Colorimetry, ITPA, STPA by 16 panelists, NIRS | Supported | p. 4575 | |
| 25 | Methods | BLUEs and broad-sense heritability | Supported | p. 4575, Eqn 1 and 2 | Mixed model in lme4 |
| 26 | Methods | tricot, 600 consumers, ten genotypes, PL trees with social covariates | Supported | p. 4575 to 4576 | ADMM trait model missing. Fix 11 |
| 27 | Limitations | Cohesiveness had low NIRS prediction in validation | Supported | p. 4583, Table 1 (R²pred 0.23) | |
| 28 | Limitations | Low heritability of texture traits limits selection gains | Supported | p. 4582 | Authors give two remedies: more contrasting germplasm and lower error |
| 29 | Limitations | Consumer testing covered two states | Imprecise | True (p. 4575), but not stated as a limitation | Authors' own limitation is different (p. 4583). Fix 9 |
| 30 | Key numbers | 80 genotypes | Supported | p. 4573, 4574 | 30 + 40 + 10 = 80 |
| 31 | Key numbers | 12 months | Supported | p. 4574 | |
| 32 | Key numbers | 16 panelists, 0 to 10 | Supported | p. 4575 | |
| 33 | Key numbers | 13 genotypes | Supported | p. 4574 | |
| 34 | Key numbers | 600 consumers | Supported | p. 4575. Fig. 6: 204 + 396 = 600 | |
| 35 | Key numbers | 85.3% | Supported | p. 4577 | |
| 36 | Key numbers | >30% / <10% heritability | Imprecise | Table 4 (p. 4580) | Fix 4 |
| 37 | Notes | Higher a* preferred here | Supported | Table 5, p. 4582 | Authors flag this as contrary to expectation and to processors' preference |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Text says color traits had heritability above 30%, but Table 4 shows L*_gari, a*_gari, ΔE_gari at 0.00, ΔE_eba 0.07 and L*_eba 0.29 | p. 4577 vs Table 4, p. 4580 | No, card repeats the text | "The text says color traits had heritability above 30%, but Table 4 shows this only for a* of eba, b* of gari and b* of eba." |
| Abstract and text call the adhesiveness-moldability correlation significant (P < 0.05), but Table 3 gives r = −0.52 without a star. With n = 13 this r gives P of about 0.07 (reviewer's calculation) | p. 4573, 4577 vs Table 3, p. 4578 | No, card repeats the claim | "The adhesiveness-moldability correlation (r = −0.52, 13 genotypes) is not marked significant in Table 3, although the text calls it significant." |
| Table 3 marks r values of 0.56 to 0.70 as P < 0.001. With n = 13 these give P of about 0.007 to 0.05 (reviewer's calculation) | Table 3, p. 4578 | No, card does not use these | Not needed |
| Discussion gives NIRS R² in prediction of 0.61 for gari L*, but Table 1 gives 0.07 (0.64 is eba L*) | p. 4581 vs Table 1, p. 4576 | No, card does not use it | Not needed, or "NIRS prediction for gari L* is 0.07 in Table 1, not 0.61 as in the discussion." |
| Coefficient of variation for cohesiveness given as 64.5%, but Table 4 gives SD 0.04 and mean 0.25 (16%). Adhesiveness 56.3% and chewiness 80.6% check out | p. 4582 vs Table 4, p. 4580 | No, card does not use it | Not needed |
| Text names Akpu and C4 as worst and C6_BC (TMS30572) best "within the nodes". In Fig. 6, node 2's highest point estimate is TMEB3 (C10_LC, wide interval), and TMEB1_MS6 sits lowest. Values read off the chart are approximate | p. 4579 vs Fig. 6, p. 4583 | No | "Fig. 6 shows TMS30572 on top in node 3, but in node 2 the local variety TMEB3 has a higher point estimate (wide interval). Read off the chart." |
| Conclusion says hardness, adhesiveness and cohesiveness relate positively to consumer preference, but Table 5 shows only cohesiveness as significant overall | p. 4583 vs Table 5, p. 4581 | No, gist echoes hardness | Covered by fix 3 and not_established |
| Conclusion names eba chromameter color as crucial, but consumer models used gari color and the authors say eba color was not measured on the consumer samples | p. 4583 | No | Covered by fix 9 and not_established |
| Methods say "40 genotypes (Experiment 1)" for heritability, but the 40-genotype set is Experiment 2 | p. 4575 | No | Not needed |
| Osun coordinates are identical to the Ibadan coordinates | p. 4574 | No | Not needed |
| Results cite Fig. 5 for the ethnic group split and node 3, but the tree is Fig. 6. Table 1 lists a training set of N = 30 although texture was measured on 13 Experiment 1 genotypes | p. 4577, 4578, Table 1 p. 4576 | No | Not needed |

## Completeness

| Item in the source | In card? | Importance | Suggested addition |
|---|---|---|---|
| Aim | Yes | High | |
| Design: three experiments of 30, 40, 10 genotypes | Partly (total only) | Medium | In revised summary |
| Gari solubility drives preference in both nodes and is in the final conclusion (Table 6, p. 4582, 4583) | No | High | Fix 1, fix 7 |
| Best and worst genotypes: TMS30572 best, Akpu and C4 weakest (p. 4579) | No (wrong genotype given) | High | Fix 1 |
| Color not measured on the eba used in consumer testing (p. 4583) | No | High | Fix 9, not_established |
| Node sizes 204 and 396, node-specific trait effects, palm oil explanation, ethnic group more important than region (p. 4582 to 4583) | Partly | High | Fix 1 |
| Hardness not significant overall (Table 5) | No (gist implies the opposite) | Medium | Fix 3 |
| ADMM model linking traits to log-worth (p. 4576) | No | Medium | Fix 11 |
| tricot design: three of ten samples, five traits, ClimMob (p. 4575) | Partly | Medium | Fix 11 |
| No instrumental measure tracks stretchability (p. 4581 to 4582) | No | Medium | Fix 8 |
| NIRS cohesiveness R²pred 0.23 and 0.50 screening threshold (p. 4576, 4579) | Partly (limitation only) | Medium | In revised summary |
| Traits breeders can use now: a*_eba, b*_eba, b*_gari, L*_eba, resilience, springiness (p. 4583) | No | Medium | Fix 7 |
| Redness preference contrary to expectation and to processors' preference (p. 4582 to 4583) | Partly (Notes compare with Cameroon only) | Medium | Fix 12 |
| a*_gari heritability 0 despite being a preference driver | No | Medium | Fix 12, not_established |
| Need for more, and more contrasting, varieties in consumer tests (p. 4583) | No | Medium | Fix 9 |
| ITPA repeatable: cooking replicate not significant except adhesiveness (Table 2, p. 4577) | No | Low | Optional |
| Gari color PCA, 86.5% (p. 4576) | No | Low | Optional |
| IRB approval and written consent (p. 4584) | No | Low | Optional |
| Funding BMGF via RTBfoods (p. 4584) | Partly | Low | |

## Template compliance

- Summary word count: 405 (current card), within 400 to 500. The suggested revised Summary is 496 words.
- Gist: 24 words, under 30. It lists traits as targets, which is close to saying what the paper shows, but hardness is wrong (fix 3).
- Keywords: 12, within 8 to 12.
- Questions: 4, within 4 to 7. The second question ("Can instrumental texture measures replace trained sensory panels?") is answered with an exception for stretchability, which the card should state.
- House style: tricot is lowercase throughout. maniva does not appear.
- not_established is missing (fix 6). relations is optional and absent. A `extends` or `discusses` link to olaosebikan-2023-jsfa could be added, as the Notes already pair the two cards.
- The current Summary repeats the conclusion before returning to NIRS results, so its order reads oddly. The revised Summary fixes this.
