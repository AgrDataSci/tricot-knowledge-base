# Card review: turner-2020-compstat

- **Card:** papers/turner-2020-compstat.md
- **Source:** papers-pdf/turner-et-al-2020.pdf (31 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

Page numbers: the PDF is the online-first version and prints no page numbers, so all pages below are PDF pages (PDF page 1 is page 1027 of the published volume).

## Overview

| Check | Result |
|---|---|
| Claims checked | 47 (plus the missing not_established field) |
| Supported | 32 |
| Imprecise | 13 |
| Not in source | 2 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 6 (1 high, 5 medium) |
| Metadata issues | 4 (data, gist, not_established missing, article can be completed) |

The card gets the core features of the package right (subset rankings, ties, pseudo-rankings, quasi standard errors, trees) and all key numbers check out. Its main problems are framing that the paper does not support: the Summary says the authors call PlackettLuce the standard engine for tricot data and that it grew out of tricot needs, which the paper never says, and it overstates the benchmarks (PLMIX was faster on two of the three PrefLib data sets). The bean tree is also described with words the paper does not use ("heat-tolerant lines", "location"), and the authors' own stated limits on tie order and standard-error computation (PDF p. 24) are missing. The single most important fix is to replace the "standard analysis engine for tricot data" sentence with the authors' stated limitations (p. 24).

## Fixes needed

1. **Outside framing presented as the authors' position (Summary, paragraph 6).** Card: "The authors position PlackettLuce as general-purpose ranking software that grew out of tricot needs, and the standard analysis engine for tricot data." Source: the paper calls PlackettLuce a feature-rich package for ranking data in general (p. 24). The word tricot appears only in the title of the cited Van Etten et al. 2016 paper (p. 31). Nothing says it grew out of tricot needs or is the standard engine. Replace the sentence with the authors' own limitations:
   > The authors name two costs. Run time grows quickly with the order of ties, and standard errors are computed by expanding rankings into counts, which can be slow or exceed memory. They expect the package to work well with ties up to order 4 and moderate numbers of items and unique rankings.

   If the team wants the tricot link stated, put it in Notes, labelled: "Outside this paper: PlackettLuce is the model engine used in most tricot analyses, for example through gosset (desousa-2023-softwarex)."

2. **Benchmarks overstated (Summary, paragraph 5).** Card: benchmarks "show PlackettLuce is faster or more capable, especially for subset rankings of many items", and the package list leaves out mixedMem. Source, Table 1 (p. 6) and text (p. 5): PlackettLuce copes well and is comparable to mixedMem, but PLMIX is consistently fast and beat PlackettLuce on T-shirt (0.007 s vs 0.023 s) and sushi (0.135 s vs 1.384 s). mixedMem was also faster on T-shirt (0.006 s). The "many items" advantage is shown only against hyper2 on NASCAR (Table 3, p. 7: 0.199 s vs 36.123 s). Replace with:
   > Run-time benchmarks against six other R packages on Netflix, T-shirt and sushi data show that PlackettLuce copes well with moderately sized data, but PLMIX was faster on the T-shirt and sushi data. On the NASCAR subset rankings (36 races, 83 drivers), PlackettLuce took 0.2 seconds against 36 seconds for hyper2. The full NASCAR data have 87 drivers.

3. **Bean tree results reworded beyond the source (Summary, paragraph 4).** Card: "The tree shows the local variety preferred in normal seasons where night temperatures were not too high, with heat-tolerant lines doing better elsewhere." Source (p. 23): with lower night temperature, INTA Rojo was most preferred in the 2016 Primera season (local variety close behind) and the local variety was most preferred in Postrera and Apante (INTA Sequia close behind). With high night temperature, INTA Sequia was most preferred, then BRT 103-182 and INTA Centro Sur. The paper never calls any variety heat-tolerant. Also, "location" is not a covariate. The covariates are season, year and maxTN (p. 22). Replace the last two sentences of paragraph 4 and the covariate sentence with:
   > These split the rankings by covariates, such as season, year or night temperature, where item worths change, and fit a separate model in each node. The worked example uses a trial of ten bean varieties in Nicaragua, where farmers named the best and worst of three varieties and compared each with their local variety. The tree first splits at a maximum night temperature of 18.7 (the paper gives no unit). Where nights were cooler, the local variety was most preferred in the Postrera and Apante seasons, and INTA Rojo in the 2016 Primera season. Where nights were warmer, INTA Sequia was most preferred.

4. **"Eases adoption by agronomists" (Summary, last paragraph).** Not in source. The paper says only that the package has standard methods for model summary (p. 1) and that summary output includes Z tests as in many R model summaries (p. 14). Delete the sentence and the repeated "accepts weights and aggregated rankings" (already said in paragraph 3). If kept, use: "Summary methods report estimates, standard errors and Z tests in the same form as other regression models in R."

5. **Tie probability missing its condition (Summary, last paragraph).** Card: the tie probability for equal-worth items is δ2/(2+δ2). Source (p. 11): this holds given that first place is not a 3-way or higher tie. Replace with:
   > For two items of equal worth, the probability that they tie for first place, given that first place is not a tie of three or more, is the two-way tie parameter divided by two plus that parameter. The ties model is illustrated with a classic chocolate pudding tasting study.

6. **Shrinkage described as acting on rarely seen items, and listed as a limitation.** Card Summary: "a mild regularization, shrinking estimates for items seen in few rankings". Card Stated limitations: shrinkage "changes estimates for rarely observed items". Source (p. 19): pseudo-rankings shrink all worths towards 1/J (equal worth). The effect is weak with many rankings but large in the 5-ranking toy example. The authors keep them on by default because the shrinkage typically reduces both bias and variance. They present it as a benefit, not a limitation. Replace the Summary sentence with:
   > The pseudo-rankings also shrink all worths towards equal worth. This effect is weak when there are many rankings. The authors keep them on by default because this shrinkage typically reduces both bias and variance.

   Remove the second limitation bullet and add to Notes: "The default pseudo-rankings (npseudo = 0.5) shrink worths towards equal worth. With few rankings the shrinkage is strong (toy example with 5 rankings, p. 19), so check results with npseudo = 0 when the network is connected."

7. **Stated limitations: wrong remedy and missing main limits.** Card: trees "can be unstable with high-dimensional covariates, so splits need checking". Source (p. 23): trees can be quite unstable, especially with high-dimensional data, and the authors suggest bagging or random forests. The authors' main limitations (p. 24 and p. 25) are missing. Replace the Stated limitations section with:
   > - Modelling ties explicitly makes run time grow quickly with the tie order. Standard errors are computed by expanding rankings into counts, which can take as long as the model fit or exceed memory. The authors expect good performance with ties up to order 4 and moderate numbers of items and unique rankings.
   > - As a guide, 5,000 sub-rankings of 10 items out of 100, with ties up to order 4, took 18.1 s to fit and 14.8 s for the variance-covariance matrix.
   > - Only subset rankings are supported, not top n rankings. Covariates enter only through trees, not as linear predictors of worth.
   > - Tree models can be quite unstable, especially with high-dimensional data. The authors suggest ensemble methods such as bagging or random forests for more robust results.
   > - Some other packages offer features PlackettLuce lacks, such as Bayesian mixture models (PLMIX), covariates on worth (ROlogit) and team rankings (hyper2).

8. **Summary sentence 3 states the tricot link as the paper's own.** Card: "tricot produces exactly this kind of data, where each farmer ranks a small subset of a larger set of varieties." The paper never uses the word tricot in its text. It shows the data structure through the Nicaragua bean trial (p. 22). Replace with:
   > The paper's bean example shows that tricot data fit this model, because each farmer ranks a small subset of a larger set of varieties.

9. **Quasi standard errors give approximate comparisons (Summary, paragraph 3).** Card: quasi-variances "allow fair comparison of any pair of items regardless of the reference item". Source (p. 15): quasi standard errors do not change with the reference, and the comparisons are approximately correct. Replace with:
   > For inference, the package reports standard errors and quasi standard errors. Quasi standard errors do not change with the reference item, so they give approximately correct comparison intervals for any pair of items. Rankings can also be weighted and aggregated.

10. **Methods bullet on covariates names partykit.** partykit is not mentioned in the paper. The paper says Plackett-Luce trees extend the Bradley-Terry trees of psychotree (p. 21). Replace with:
    > - **Covariates.** pltree() combines the model with model-based recursive partitioning, extending the Bradley-Terry trees of the psychotree package. The bean example used up to three nodes and at least 5% of records per node.

11. **Key numbers: sushi attribution and missing rows.** The sushi data come from PrefLib (Mattei and Walsh 2013, Table 2, p. 6). Replace the row and add rows:
    > | 5,000 rankings (4,926 unique), 10 items | Sushi benchmark dataset | PrefLib (Mattei and Walsh 2013), cited in this paper |
    > | 0.199 s vs 36.123 s | Time to fit the NASCAR subset rankings (36 races, 83 drivers), PlackettLuce vs hyper2 | This paper |
    > | 842 (47, 489, 306) | Farmer records in the bean tree, total and per terminal node | This paper |
    > | 18.7 | Maximum night temperature at the first tree split (no unit given) | This paper |
    > | 0.5 | Default weight of each pseudo-ranking (npseudo) | This paper |
    > | 18.1 s and 14.8 s | Fit time and variance-covariance time for 5,000 sub-rankings of 10 of 100 items, ties up to order 4 | This paper |

    The 842 total is my sum of the three node sizes on p. 23 and should be marked "card's sum of node sizes" if added.

12. **Metadata fixes.** See the Metadata check table for exact text (data, gist, not_established, article).

A full revised Summary that applies fixes 1 to 9 (498 words) is given at the end of this report.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Modelling rankings in R. The PlackettLuce package | "Modelling rankings in R: the PlackettLuce package" (p. 1) | Supported (colon to period is the expected house convention) |
| authors | Turner HL, van Etten J, Firth D, Kosmidis I | Same four authors in this order (p. 1) | Supported |
| year | 2020 | Accepted 18 January 2020, © 2020 (p. 1) | Supported |
| journal | Computational Statistics | Computational Statistics (p. 1) | Supported |
| article | online first 2020 (volume and pages not in the PDF) | No volume or pages printed. The PDF has 31 pages. | Supported. Can be completed: the University of Warwick repository record (wrap.warwick.ac.uk/136798) gives volume 35, pages 1027-1057, which matches the 31 pages. Suggested: `article: 35, 1027-1057 (from the publisher record, not printed in the PDF)` |
| type | software paper | Labelled "Original paper", content is a package description (p. 1) | Supported |
| doi | https://doi.org/10.1007/s00180-020-00959-3 | Same (p. 1) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution 4.0 (p. 25) | Supported |
| data | example datasets ship with the package (beans, NASCAR, pudding and others) | beans, nascar and pudding are provided in PlackettLuce (p. 11, 19, 22). Netflix, T-shirt and sushi are downloaded from PrefLib (p. 25). "and others" is not shown in the paper. | Imprecise. Suggested: `data: beans, nascar and pudding datasets ship with the package. Netflix, T-shirt and sushi benchmark data come from PrefLib. Benchmark and data-preparation code is in the appendix` |
| software | v0.4.5 on CRAN, published 2026-03-25 | Paper cites v0.2-9 (p. 30) | Not checkable against the source (current CRAN status). Fine as metadata. |
| crops | common bean (example) | "ten different varieties of bean" (p. 22) | Supported |
| region | Nicaragua (example) | Trial in Nicaragua (p. 22) | Supported |
| gist | The R package behind tricot analysis, fitting Plackett-Luce models ... | "behind tricot analysis" is outside framing (see fix 1). Otherwise accurate. | Imprecise. Suggested (25 words): `gist: The PlackettLuce R package fits Plackett-Luce models to subset rankings with ties, keeps sparse data estimable with pseudo-rankings, and finds covariate subgroups with model trees` |
| not_established | (missing) | | Missing. Suggested below. |

Suggested not_established:

`not_established: that PlackettLuce is the fastest ranking software (PLMIX was faster on two of three benchmark data sets); that it fits top n rankings; that it models covariate effects on worth directly (covariates enter only through trees); that it was designed for or validated on tricot data (the Nicaragua bean trial is one worked example); that the bean tree identifies heat-tolerant varieties (it illustrates the method and makes no agronomic claim); that explicit tie modelling is practical beyond ties of order 4`

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Paper presents PlackettLuce, fits a generalized PL model | Supported | Abstract (p. 1) | |
| 2 | Summary | Luce's axiom, worth, ranking as product of sequential choices | Supported | Eq. 1 (p. 2) | |
| 3 | Summary | tricot produces exactly this kind of data | Imprecise | Bean trial, 3 of 10 varieties per farmer (p. 22) | Paper does not use the word tricot in its text. Fix 8. |
| 4 | Summary | Extends standard model in three ways | Supported | Abstract (p. 1) | |
| 5 | Summary | Handles partial (subset) rankings | Supported | p. 1, p. 6, Table 4 (p. 8) | Top n not supported, not said in card |
| 6 | Summary | Ties of any order, tie parameters estimated with worths | Supported | p. 1, Eq. 2 (p. 11) | Practical limit of order 4 (p. 24) missing |
| 7 | Summary | Pseudo-rankings by default, connected network, finite estimates and SEs | Supported | Abstract (p. 1), p. 19 | |
| 8 | Summary | Mild regularization shrinking estimates for items seen in few rankings | Imprecise | p. 19 | Shrinks all worths towards 1/J. Weak with many rankings. Fix 6. |
| 9 | Summary | Quasi-variances allow fair comparison regardless of reference | Imprecise | p. 15 | Comparisons are approximately correct. Fix 9. |
| 10 | Summary | Rankings can be weighted and aggregated | Supported | Weights (p. 12 to 13, p. 19), aggregated rankings (p. 5) | |
| 11 | Summary | Connects PL models with model-based recursive partitioning | Supported | p. 21 | |
| 12 | Summary | Splits by covariates such as night temperature, season or location, separate model per node | Imprecise | Covariates are season, year, maxTN (p. 22) | "location" is not a covariate. Fix 3. |
| 13 | Summary | Ten bean varieties in Nicaragua, best and worst plus comparison with local variety | Supported | p. 22 | "common bean" is not the paper's wording but is harmless |
| 14 | Summary | Local preferred in normal seasons with lower night temperature, heat-tolerant lines better elsewhere | Imprecise | p. 23 | INTA Rojo top in Primera 2016. "Heat-tolerant" not in source. Fix 3. |
| 15 | Summary | Benchmarks vs hyper2, pmr, PLMIX, StatRank, ROlogit show PlackettLuce faster or more capable | Imprecise | Table 1 (p. 6), p. 5, Table 3 (p. 7) | PLMIX faster on 2 of 3, mixedMem omitted. Fix 2. |
| 16 | Summary | NASCAR: 87 drivers over 36 races | Supported | p. 19 | Benchmark in Table 3 used 83 drivers |
| 17 | Summary | Authors position it as grown out of tricot needs and standard tricot engine | Not in source | p. 24 calls it a feature-rich package for ranking data | Fix 1 |
| 18 | Summary | Tie probability δ2/(2+δ2) for equal-worth items | Imprecise | p. 11 | Missing condition "first place not a 3-way or higher tie". Fix 5. |
| 19 | Summary | Ties illustrated with chocolate pudding study | Supported | p. 11 to 13 | |
| 20 | Summary | Package accepts weights and aggregated rankings | Supported | p. 5, p. 12 to 13 | Repeats claim 10 |
| 21 | Summary | SE and quasi-variance methods familiar from regression, ease adoption by agronomists | Not in source | p. 1, p. 14 | Agronomists not mentioned. Fix 4. |
| 22 | Methods | Model: worths, tie parameters up to chosen order, optional pseudo-rankings with ghost item | Supported | p. 11, p. 19 | Pseudo-rankings are on by default (npseudo = 0.5) |
| 23 | Methods | Iterative scaling, BFGS or L-BFGS, L-BFGS typically fastest | Supported | p. 13 | Iterative scaling is the default |
| 24 | Methods | Standard errors, Z tests, quasi-variances | Supported | p. 14 to 15 | |
| 25 | Methods | pltree() with model-based partitioning (psychotree, partykit) | Imprecise | p. 21 | partykit not in source. Fix 10. |
| 26 | Methods | Best-worst of three plus pairwise with local, grouped per farmer | Supported | p. 22, p. 28 to 29 | Grouped per record, four rankings each |
| 27 | Limitations | Trees unstable with high-dimensional covariates, splits need checking | Imprecise | p. 23 | Remedy in source is bagging or random forests. Fix 7. |
| 28 | Limitations | Pseudo-rankings slightly shrink estimates for rarely observed items | Imprecise | p. 19 | Authors present shrinkage as a benefit. Fix 6. |
| 29 | Limitations | Competitor packages offer Bayesian mixtures or other features | Supported | Table 4 (p. 8), p. 8 | |
| 30 | Key numbers | 10 bean varieties, Van Etten et al. 2016 cited | Supported | p. 22 | |
| 31 | Key numbers | 87 drivers, 36 races, Hunter 2004 cited | Supported | p. 19 | |
| 32 | Key numbers | 3,741 simple contrasts | Supported | p. 21 | Recomputed: 87 choose 2 = 3,741 |
| 33 | Key numbers | -0.7% to +6.7% quasi-variance error, NASCAR | Supported | p. 21 | |
| 34 | Key numbers | <0.8% error, pudding | Supported | p. 15 | Applies to simple contrasts. All contrasts: -1.7% to +1.7%. |
| 35 | Key numbers | 5,000 rankings, 10 items, sushi, "cited in this paper" | Imprecise | Table 2 (p. 6) | Attribution should name PrefLib (Mattei and Walsh 2013). Fix 11. |
| 36 to 47 | Frontmatter | title, authors, year, journal, article, type, doi, license, crops, region (Supported), data and gist (Imprecise) | See Metadata check | | |

Notes: the first note (check the CRAN version) is practical advice, not a claim about the paper, and is fine. The second is a cross-reference.

Derived numbers recomputed: 87 choose 2 = 3,741 (matches p. 21). Pudding tie2 = 0.7468 (p. 13) gives a tie probability of 0.7468 / 2.7468 = 0.27, not stated by the paper or the card. Node sizes 47 + 489 + 306 = 842 (my sum, p. 23).

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Wrong internal cross-references. Sect. 2.2.4 points to itself for more detail (should be Sect. 3.3). Sect. 3.1.1 says the log scale for inference is discussed in Sect. 2.2.3 (it is in Sect. 3.2.1). | p. 7, p. 13 | No | Not needed (does not affect any card claim) |
| Table 3 gives 83 items and 42 to 43 items per ranking for NASCAR, while the text says 43 drivers per race out of 87. Table 3 refers to the reduced data after Hunter dropped four drivers, but the table does not say so. | p. 7, p. 19 | No | "The NASCAR benchmark in Table 3 uses 83 drivers (four drivers who always finished last were dropped, as in Hunter 2004). The full data have 87." |
| Text lists BRT 103-182 before INTA Centro Sur in the high night temperature node, but the tree output gives INTA Centro Sur the higher log worth (0.438 vs 0.384). | p. 23 | No | "In the high night temperature node, INTA Centro Sur (0.44) has a slightly higher log worth than BRT 103-182 (0.38), although the text lists BRT 103-182 first." |
| maxTN split at 18.7175 is given without a unit. | p. 22 to 23 | No | "The paper gives no unit for maxTN (maximum night temperature)." |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: present the package and its features | Yes | | |
| Authors' limits: run time grows with tie order, SE computation by count expansion is slow or memory-bound, works well to tie order 4, 18.1 s and 14.8 s guide (p. 24) | No | High | Fix 7 and fix 1 |
| Only subset rankings supported, not top n (p. 6, Table 4, p. 25) | No | Medium | Fix 7 and not_established |
| No direct covariates on worth, only trees (Table 4, p. 8) | No | Medium | Fix 7 and not_established |
| Default npseudo = 0.5, shrinkage towards 1/J, lower bias and variance (p. 19) | Partly | Medium | Fix 6 |
| Bean tree details: 842 records in 3 nodes, split at maxTN 18.7, minsize 5%, maxdepth 3, node winners (p. 22 to 23) | Partly | Medium | Fix 3 and fix 11 |
| Benchmark results per package (Table 1, Table 3) | Partly, overstated | Medium | Fix 2 |
| Worths sum to one and equal the probability of coming first (p. 11) | No | Low | Optional: "Worths are scaled to sum to one, so each is the probability that the item comes first among all items, when first place is not tied." |
| Z tests against a reference item are usually not of interest, use log scale and quasi SEs (p. 14) | No | Low | Optional Methods note |
| Pudding: no significant brand differences (p. 14) | No | Low | Not needed |
| Iterative scaling is the default, with Steffensen acceleration (p. 13) | No | Low | Optional |
| Future work: online estimation, spatio-temporal heterogeneity, top n rankings (p. 24 to 25) | No | Low | Optional in Notes |
| Strong connectivity condition and connectivity() check (p. 17 to 18) | No | Low | Optional |

## Template compliance

- Summary word count: 402 (within 400 to 500). The suggested revision below is 498 words.
- Gist: 24 words (under 30). Suggested gist is 25 words.
- Keywords: 10 (within 8 to 12).
- Questions: 5 (within 4 to 7). The first question ("why Plackett-Luce?") is not answered by the paper for tricot specifically. Suggested: "What does the Plackett-Luce model assume, and what does PlackettLuce add to it?"
- House style: tricot is lowercase throughout. maniva does not appear.
- not_established: missing (see Metadata check).
- Long format: the card is long format and has all sections.

## Suggested full Summary (applies fixes 1 to 9, 498 words)

> The paper presents the PlackettLuce R package, which fits a generalized Plackett-Luce model to rankings. Under Luce's axiom, each item has a worth, and the probability of a ranking is the product of choosing each item in turn from those that remain. The paper's bean example shows that tricot data fit this model, because each farmer ranks a small subset of a larger set of varieties.
> 
> The package extends the standard model in three ways that matter for on-farm data. It handles partial rankings, where each ranking covers only a subset of items (top n rankings are not supported). It handles ties of any order, with tie parameters estimated alongside worths. By default it adds pseudo-rankings with a hypothetical item, which keeps the network of wins and losses connected so that every item has a finite worth estimate and standard error, even with sparse data. The pseudo-rankings also shrink all worths towards equal worth. This effect is weak when there are many rankings. The authors keep them on by default because this shrinkage typically reduces both bias and variance.
> 
> For inference, the package reports standard errors and quasi standard errors. Quasi standard errors do not change with the reference item, so they give approximately correct comparison intervals for any pair of items. Rankings can also be weighted and aggregated.
> 
> The package connects Plackett-Luce models with model-based recursive partitioning, producing Plackett-Luce trees. These split the rankings by covariates, such as season, year or night temperature, where item worths change, and fit a separate model in each node. The worked example uses a trial of ten bean varieties in Nicaragua, where farmers named the best and worst of three varieties and compared each with their local variety. The tree first splits at a maximum night temperature of 18.7 (the paper gives no unit). Where nights were cooler, the local variety was most preferred in the Postrera and Apante seasons, and INTA Rojo in the 2016 Primera season. Where nights were warmer, INTA Sequia was most preferred.
> 
> Run-time benchmarks against six other R packages on Netflix, T-shirt and sushi data show that PlackettLuce copes well with moderately sized data, but PLMIX was faster on the T-shirt and sushi data. On the NASCAR subset rankings (36 races, 83 drivers), PlackettLuce took 0.2 seconds against 36 seconds for hyper2. The full NASCAR data have 87 drivers.
> 
> The authors name two costs. Run time grows quickly with the order of ties, and standard errors are computed by expanding rankings into counts, which can be slow or exceed memory. They expect the package to work well with ties up to order 4 and moderate numbers of items and unique rankings.
> 
> Tie parameters have a direct interpretation. For two items of equal worth, the probability that they tie for first place, given that first place is not a tie of three or more, is the two-way tie parameter divided by two plus that parameter. The ties model is illustrated with a classic chocolate pudding tasting study.
