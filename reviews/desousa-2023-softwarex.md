# Card review: desousa-2023-softwarex

- **Card:** papers/desousa-2023-softwarex.md
- **Source:** papers-pdf/de-sousa-et-al-2023b.pdf (6 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot). Card read from the current main copy, which adds the relation `usesMethodIn: eskridge-1992-tag`.
- **Verdict:** Major fixes

Page numbers below are the printed journal page numbers. They are the same as the PDF page numbers (pages 1 to 6).

## Overview

| Check | Result |
|---|---|
| Claims checked | 51 |
| Supported | 33 |
| Imprecise | 12 |
| Not in source | 3 (plus 2 outside-information items, not counted as errors) |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 3 |
| Important omissions | 6 |
| Metadata issues | 3 |

The function descriptions, the frontmatter and the methods bullets are accurate. The problems sit in the example and impact paragraphs. The card says the example used gosset for model validation, but the paper lists cross-validation, btpermute and regret only as next steps, and the sentence the card draws on refers to earlier published studies (p. 4 to 5). The card also leaves out the Kendall's tau results (Table 1, p. 3), turns single-variety findings into plural ones, and has a "Stated limitations" section that the authors did not write. Most fixes are text replacements. A full replacement Summary is given in fix 15.

The verdict is at the border between Minor and Major. It is Major because one claim about what the paper demonstrates is Contradicted and one of the two result tables is missing.

## Fixes needed

1. **Contradicted: what the example demonstrates.** The card says: "In the example, gosset handled data preparation, model validation and presentation of results". The source says this about the cited studies: "In these studies, the gosset package supported data preparation, model validation and results presentation tasks" (p. 5). The example itself runs no validation. Forward selection with crossvalidation(), btpermute(), regret() and rank_numeric() for legacy data are listed as "next steps" (p. 4). Replace the sentence with:
   > The authors stress reproducible and efficient workflows. They report that gosset supported data preparation, model validation and results presentation in several published studies. The example itself does not run cross-validation, btpermute or regret. The authors list these as next steps. In the example, three varieties could marginally outperform the check variety Amadeus 77 under drier conditions (total rainfall of 193.82 mm or less over the first 45 days after planting), with reliability of 0.506 to 0.519.

2. **Omission: Kendall's tau results (Table 1, p. 3).** This is the first result of the example and the one most relevant to trait prioritisation in tricot. Add to the example paragraph:
   > Kendall's tau between overall appreciation and each of the eight traits was highest for yield (0.749), taste (0.653) and marketability (0.639), which the authors read as the traits farmers prioritised. They suggest this can help choose traits for a lighter tricot design with no more than four traits.

3. **Imprecise: "some varieties that rank low overall outperform others under higher rainfall".** The source names one variety, ALS 0532-6, which performs weakly "in the whole yield ranking" and outperforms all others under higher rainfall (p. 4). "Overall" is ambiguous here because "overall appreciation" is a trait in this paper. The split in Fig. 2 has p = 0.079 (p. 5), and the tree was fitted with alpha = 0.1 (code, p. 4). Replace with:
   > The tree splits at 193.82 mm (p = 0.079, with alpha set to 0.1). ALS 0532-6 performs weakly in the full yield ranking but outperforms all other varieties under higher rainfall (reliability 0.630 against Amadeus 77).

4. **Imprecise: "compares overall appreciation with yield to reveal varieties farmers value for traits beyond yield, such as taste and marketability".** The source shows no complete agreement between the two (Fig. 3, p. 5) and discusses one variety, SX 14825-7-1. For that variety the authors say "we can argue" that taste, marketability and disease resistance explain the gap (p. 4). Replace with:
   > compare() then shows that overall appreciation and yield do not fully agree. For SX 14825-7-1, the authors suggest that taste, marketability and disease resistance may explain its higher overall appreciation.

5. **Not in source / Imprecise: Stated limitations section.** The paper has no limitations section. The first bullet ("wraps other packages ... so results depend on them") is the card's own inference. The source says gosset "complements" these packages (p. 2). The second bullet is half supported: the example is called illustrative (p. 2), but the paper never says the results are not variety recommendations. Replace the section with:
   > - The paper has no limitations section.
   > - The authors call the example a simple illustration. For simplicity it uses only total rainfall as a covariate and shows only varieties with reliability of 0.5 or more (p. 3 to 4).
   > - Cross-validation, btpermute, regret and combining legacy data with rank_numeric are not run in the example. The authors list them as next steps that earlier studies implemented (p. 4).

6. **Missing not_established.** Add:
   > not_established: that the Nicaragua example results are variety recommendations; that the rainfall split is significant at the 5% level; that cross-validation, btpermute or regret were demonstrated in the example; that gosset was benchmarked against other software; that all trials run through ClimMob are analysed with gosset

7. **Gist lists topics.** It names functions but does not say what the paper shows. Replace with (26 words):
   > gist: gosset adds R functions missing from PlackettLuce and related packages to prepare, model and present ranking data, demonstrated on a common bean tricot trial in Nicaragua.

8. **Not in source: software ecosystem.** The card says the package sits in an ecosystem "around tricot, alongside ClimMob, ClimMobTools, PlackettLuce, climatrends and chirps". The source says gosset is part of an ecosystem "built around ClimMob", which runs trials on more than 10,000 farms per year (p. 5). ClimMobTools is not mentioned anywhere in the paper. Replace with:
   > gosset is part of a software ecosystem built around ClimMob, which runs trials on more than 10,000 farms per year. Insights from the package help several breeding teams in Sub-Saharan Africa select and advance breeding materials.

9. **Imprecise: 1000FARMS.** The card says gosset "supports a community of practice around tricot, including the Africa-wide 1000FARMS on-farm trial network". The source has the direction the other way. The 1000FARMS network supports refinement of methods and expansion of the approach in breeding programmes (p. 5). The community of practice is described as "in on-farm experimentation", and the authors expect it to push improvements to the package (p. 5). Replace with:
   > The authors note that the package enabled several published studies and that its code is open source. The Africa-wide 1000FARMS on-farm trial network supports further refinement of the methods, and the authors expect the community of practice in on-farm experimentation to drive improvements to the package.

10. **Imprecise: Gosset and the t-test.** "behind Student's t-test" is outside knowledge. The source says Gosset used the pen name 'Student', was a pioneer of small-sample experimental design, and compared barley varieties and brewing practices at Guinness (p. 2). Replace with:
    > It is named after William Sealy Gosset, known by the pen name 'Student', who as a brewer at Guinness developed practical ways to compare barley varieties and brewing practices.

11. **Imprecise: scope and positioning (sentences 1 and 3).** The source presents tricot as one approach that produces ranking data, next to data synthesis (abstract and p. 1), not as "the main use case". It lists PlackettLuce, BradleyTerry2 and psychotree on equal terms (p. 1 to 2), and the users are "researchers working on agricultural experiments" (abstract). Replace with:
    > gosset supports the analysis and synthesis of ranking data in agricultural experiments, such as tricot trials and data synthesis studies. ... gosset fills gaps between general ranking packages (PlackettLuce, BradleyTerry2 and psychotree) and the full workflow that agricultural researchers need.

12. **Imprecise: "fits Plackett-Luce trees".** The example fits one Plackett-Luce model per trait and one Plackett-Luce tree, for yield only (p. 3 to 4). Replace with:
    > The example then links the yield rankings to total rainfall over the first 45 days after planting, from the chirps and climatrends packages, and fits one Plackett-Luce tree.

13. **Imprecise and outside information: the tutorial paragraph.** "the full tricot analysis workflow, from raw data to reliability estimates" overstates it. The nicabean data were already converted with rank_tricot() (p. 3), and validation steps are skipped (p. 4). The CRAN advice is outside information and already sits in Notes. Replace the paragraph with:
    > The example data ship with the package, so the workflow can be practised from ranked data to reliability estimates.

14. **data field.** The template asks where the code lives. The paper gives the dataset name, the code repository, the code version and the licence (Code metadata, p. 1, and p. 3). Replace with:
    > data: nicabean dataset (tricot common bean trials, Nicaragua) distributed with the package. Code for v1.0 at https://github.com/ElsevierSoftwareX/SOFTX-D-22-00199 (MIT licence). Documentation at https://agrdatasci.github.io/gosset/

    Optional: change license to "CC BY 4.0", which matches the licence URL printed on p. 1.

15. **Full replacement Summary (491 words, combines fixes 1 to 4 and 8 to 13).**
    > gosset supports the analysis and synthesis of ranking data in agricultural experiments, such as tricot trials and data synthesis studies. The package is named after William Sealy Gosset, known by the pen name 'Student', who as a brewer at Guinness developed practical ways to compare barley varieties. gosset fills gaps between general ranking packages (PlackettLuce, BradleyTerry2 and psychotree) and the full workflow that agricultural researchers need.
    >
    > Functions cover three stages. For data preparation, rank_tricot converts tricot best and worst data into PlackettLuce rankings, rank_numeric converts numeric measurements such as yield into rankings, and set_binomialfreq and set_paircomp convert rankings for Bradley-Terry models and Bradley-Terry trees. For model selection and evaluation, gosset offers AIC, deviance-based forward variable selection for Bradley-Terry models (btpermute), k-fold cross-validation with custom folds, Kendall's tau, Kendall's W and McFadden's pseudo-R². For presentation of results, it computes reliability, the probability that an item outperforms a reference item, and regret, the loss under the worst possible outcome. It also offers worth bar plots, a worth heat map across traits, a Bland-Altman plot comparing two traits, and a ggplot2 plot for Plackett-Luce trees.
    >
    > The illustrative example uses the nicabean dataset from tricot trials in Nicaragua over five seasons in 2015 and 2016. Each farmer tested three of ten common bean varieties and ranked them as best and worst for eight traits and for overall appreciation. Kendall's tau between overall appreciation and each trait was highest for yield (0.749), taste (0.653) and marketability (0.639), which the authors read as the traits farmers prioritised. The example then links the yield rankings to total rainfall over the first 45 days after planting, from the chirps and climatrends packages, and fits one Plackett-Luce tree. The tree splits at 193.82 mm (p = 0.079, with alpha set to 0.1). Under drier conditions, three varieties could marginally outperform the check variety Amadeus 77 (reliability 0.506 to 0.519). ALS 0532-6 performs weakly in the full yield ranking but outperforms all other varieties under higher rainfall (reliability 0.630). compare() then shows that overall appreciation and yield do not fully agree. For SX 14825-7-1, the authors suggest that taste, marketability and disease resistance may explain its higher overall appreciation.
    >
    > The authors stress reproducible and efficient workflows. They report that gosset supported data preparation, model validation and results presentation in several published studies. The example itself does not run cross-validation, btpermute or regret. The authors list these as next steps. gosset is part of a software ecosystem built around ClimMob, which runs trials on more than 10,000 farms per year. Insights from the package help several breeding teams in Sub-Saharan Africa, and the Africa-wide 1000FARMS on-farm trial network supports further refinement of the methods.
    >
    > The code is open source, so users can request new functions and developers can contribute. The authors expect the community of practice in on-farm experimentation to drive further improvements. The example data ship with the package, so the workflow can be practised from ranked data to reliability estimates.

16. **Methods in brief: Example bullet.** Replace with:
    > - **Example.** nicabean dataset: tricot trials of common bean in Nicaragua, five seasons (2015 to 2016), three of ten varieties per farmer, eight traits plus overall appreciation. Kendall's tau of each trait against overall appreciation. One Plackett-Luce tree for yield, with total rainfall over the first 45 days after planting (chirps, climatrends) as covariate and alpha = 0.1. Reliability against Amadeus 77. compare() of overall appreciation against yield.

    Optional: add node_labels, node_rules and top_items to the Interpretation bullet (p. 4).

17. **Key numbers: add rows.**
    > | 0.749, 0.653, 0.639 | Kendall's tau between overall appreciation and yield, taste and marketability (Table 1) | This paper |
    > | 193.82 mm | Total rainfall over the first 45 days after planting where the Plackett-Luce tree for yield splits (p = 0.079, alpha = 0.1) | This paper |
    > | 0.506 to 0.519 | Reliability of BRT 103-182, IBC 302-29 and SX 14825-7-1 against Amadeus 77, drier node (Table 2) | This paper |
    > | 0.630 and 0.565 | Reliability of ALS 0532-6 and SX 14825-7-1 against Amadeus 77, wetter node (Table 2) | This paper |
    > | 393 and 164 | Rankings in the drier and wetter nodes, read from Fig. 2 | This paper |
    > | 5 seasons | Nicaragua trials, 2015 to 2016 | This paper |
    > | >10,000 farms per year | Trials run through ClimMob | This paper |

18. **Notes: add.**
    > - The paper describes code version 1.0 (Code metadata, p. 1). Function names and arguments may differ in later CRAN versions.
    > - The rainfall split in Fig. 2 has p = 0.079 and the tree was fitted with alpha = 0.1. The drier-node reliabilities (0.506 to 0.519, SE about 0.035) are close to 0.5. The authors call them marginal.
    > - Table 2 check (card's own calculation): reliability equals worth of the variety divided by the sum of its worth and the worth of Amadeus 77 in the same node. This reproduces all values in the table.
    > - The source cites climatrends as a 2020 CRAN entry [25]. The card desousa-2023-joss is the later JOSS paper on the same package.

    The card already has `usesMethodIn: eskridge-1992-tag` for the reliability function. This is correct (reference [24], p. 2). Optional further relations: usesMethodIn turner-2020-compstat, and discusses vanetten-2019-pnas, moyo-2021-fsufs, desousa-2021-commsbio, brown-2022-cropsci, alamu-2023-jsfa, gesesse-2023-pnas, woldeyohannes-2022-elife and rutsaert-2023-mib (all cited on p. 4 to 5 as studies that used the methods).

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | gosset. An R package for analysis and synthesis of ranking data in agricultural experimentation | Same, with a colon after gosset (p. 1) | Supported (colon to period is house style) |
| authors | de Sousa K, Brown D, Steinke J, van Etten J | Same four authors in this order (p. 1) | Supported |
| year | 2023 | SoftwareX 22 (2023), accepted 3 May 2023 (p. 1) | Supported |
| journal | SoftwareX | SoftwareX (p. 1) | Supported |
| article | 22, 101402 | SoftwareX 22 (2023) 101402 (p. 1) | Supported |
| type | software paper | "Original software publication" (p. 1) | Supported |
| doi | https://doi.org/10.1016/j.softx.2023.101402 | Same (p. 1) | Supported |
| license | CC BY | CC BY license, URL to version 4.0 (p. 1) | Supported. "CC BY 4.0" would be more exact |
| data | example tricot common bean data distributed with the package | nicabean dataset, "freely available within the software" (p. 3, p. 6). Code repository, v1.0 and MIT licence in Code metadata (p. 1) | Imprecise: no dataset name, no code location (fix 14) |
| software | CRAN v1.5.1, published 2025-11-19, checked 2026-10-30 | Paper describes code version 1.0 (p. 1) | Not in source (outside information), not counted |
| open_copy | PMC link | Not in PDF | Not checkable against the PDF, not counted |
| crops | common bean (example) | Common bean, Phaseolus vulgaris (p. 1, p. 2) | Supported |
| region | Nicaragua (example) | Nicaragua (p. 1, p. 2) | Supported |
| gist | R package covering the tricot analysis workflow ... | The paper presents functions and demonstrates them on one example | Imprecise: lists topics and says "tricot analysis workflow" though scope is ranking data generally (fix 7) |
| not_established | missing | | Missing (fix 6) |
| relations | usesMethodIn: eskridge-1992-tag (the reliability function) | reliability() cites Eskridge and Mumm 1992 as a common plant-breeding heuristic, reference [24] (p. 2, p. 6) | Supported |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Frontmatter | title | Supported | p. 1 | |
| 2 | Frontmatter | authors | Supported | p. 1 | |
| 3 | Frontmatter | year 2023 | Supported | p. 1 | |
| 4 | Frontmatter | journal SoftwareX | Supported | p. 1 | |
| 5 | Frontmatter | article 22, 101402 | Supported | p. 1 | |
| 6 | Frontmatter | type software paper | Supported | p. 1 | |
| 7 | Frontmatter | doi | Supported | p. 1 | |
| 8 | Frontmatter | license CC BY | Supported | p. 1 | Could read CC BY 4.0 |
| 9 | Frontmatter | data | Imprecise | p. 1, 3, 6 | Fix 14 |
| 10 | Frontmatter | crops | Supported | p. 2 | |
| 11 | Frontmatter | region | Supported | p. 2 | |
| 12 | Frontmatter | gist | Imprecise | whole paper | Lists topics. Fix 7 |
| 13a | Frontmatter | relations: usesMethodIn eskridge-1992-tag, the reliability function | Supported | p. 2, reference [24] p. 6 | Eskridge and Mumm (1992), Theor Appl Genet, matches the eskridge-1992-tag card |
| 13 | Frontmatter | software field, CRAN v1.5.1 | Not in source (outside information) | p. 1 gives v1.0 | Not counted as an error |
| 14 | Summary | Ranking data in agricultural experiments, tricot as main use case | Imprecise | Abstract, p. 1 | Source names tricot and data synthesis as sources of ranking data, not tricot as main use case. Fix 11 |
| 15 | Summary | Named after Gosset, behind Student's t-test, compared barley varieties | Imprecise | p. 2 | t-test is outside knowledge. Pen name, Guinness and barley are supported. Fix 10 |
| 16 | Summary | Fills gaps between ranking software, mainly PlackettLuce, and workflow agronomists and breeders need | Imprecise | p. 1 to 2 | Source lists three packages equally and speaks of researchers in agricultural experiments. Fix 11 |
| 17 | Summary | Functions cover three stages | Supported | p. 1 to 2 | |
| 18 | Summary | rank_tricot converts best and worst data to PlackettLuce rankings | Supported | p. 2 | |
| 19 | Summary | rank_numeric converts numeric data such as yield | Supported | p. 2 | |
| 20 | Summary | set_binomialfreq and set_paircomp for Bradley-Terry models and trees | Supported | p. 2 | |
| 21 | Summary | AIC, btpermute, k-fold CV with custom folds, Kendall tau, Kendall W, McFadden pseudo-R² | Supported | p. 2 | btpermute is for Bradley-Terry models only. The card does not say so. The replacement text adds it |
| 22 | Summary | Reliability is probability of outperforming a reference | Supported | p. 2 | |
| 23 | Summary | Regret is loss under worst outcome | Supported | p. 2 | |
| 24 | Summary | Worth bar plot, worth heat map, plot comparing two traits | Supported | p. 2 | compare() uses the Bland-Altman method (p. 4) |
| 25 | Summary | Example: farmers tested three of ten common bean varieties | Supported | p. 2 | |
| 26 | Summary | Links rankings to chirps rainfall and climatrends indices, fits Plackett-Luce trees | Imprecise | p. 3 to 4 | One tree, for yield only. Fix 12 |
| 27 | Summary | Some varieties that rank low overall outperform under higher rainfall | Imprecise | p. 4, Fig. 2 p. 5 | One variety (ALS 0532-6), weak in the yield ranking. "shows" is firmer than a split at p = 0.079. Fix 3 |
| 28 | Summary | compare reveals varieties valued for taste and marketability beyond yield | Imprecise | p. 4, Fig. 3 p. 5 | One variety, hedged ("we can argue"), also disease resistance. Fix 4 |
| 29 | Summary | Reliability against Amadeus 77 under drier and wetter conditions | Supported | p. 4, Table 2 | Values recomputed from worth. All match |
| 30 | Summary | Package enabled several published studies | Supported | p. 4 to 5 | |
| 31 | Summary | Package is open source | Supported | p. 5 | |
| 32 | Summary | Supports a community of practice around tricot, including 1000FARMS | Imprecise | p. 5 | Direction reversed. Fix 9 |
| 33 | Summary | Authors stress reproducible and efficient workflows | Supported | p. 4 to 5 | |
| 34 | Summary | In the example, gosset handled data preparation, model validation and presentation | Contradicted | p. 4 (next steps), p. 5 ("In these studies") | No validation in the example. Fix 1 |
| 35 | Summary | Three varieties marginally outperform Amadeus 77 under drier conditions, rainfall first 45 days | Supported | p. 4, Table 2 | Reliability 0.506 to 0.519, split at 193.82 mm |
| 36 | Summary | Ecosystem around tricot with ClimMob, ClimMobTools, PlackettLuce, climatrends, chirps | Not in source | p. 5 | ClimMobTools not in paper. Ecosystem is "built around ClimMob". Fix 8 |
| 37 | Summary | Open source lets users request functions and developers contribute, keeps toolkit aligned | Imprecise | p. 5 | First part supported. "keeps aligned" is firmer than "it is expected" |
| 38 | Summary | Paper doubles as tutorial on full tricot workflow from raw data to reliability | Imprecise | p. 3 to 4 | Data were pre-converted and validation skipped. Fix 13 |
| 39 | Summary | Function names should be checked against the current CRAN version | Not in source | none | Outside information placed in the Summary. Already in Notes. Fix 13 |
| 40 | Summary | Example data ship with the package | Supported | p. 3, p. 6 | |
| 41 | Methods | Data preparation functions | Supported | p. 2 | |
| 42 | Methods | Model selection functions, default 10-fold | Supported | p. 2 | |
| 43 | Methods | Interpretation functions | Supported | p. 2 | node_labels, node_rules, top_items (p. 4) not listed |
| 44 | Methods | Example: ten varieties, chirps and climatrends rainfall, Amadeus 77 reference | Supported | p. 2 to 4 | Thin. Fix 16 |
| 45 | Limitations | Package wraps other packages, so results depend on them | Not in source | p. 2 says "complements" | Not an authors' limitation. Fix 5 |
| 46 | Limitations | Example is illustrative, results not presented as variety recommendations | Imprecise | p. 2 | First half supported. Second half is the card's inference. Fix 5 |
| 47 | Key numbers | 3 of 10 varieties | Supported | p. 2 | |
| 48 | Key numbers | 10-fold default cross-validation | Supported | p. 2 | |
| 49 | Key numbers | Reliability ≥0.5 threshold for presenting varieties | Supported | p. 4 | |
| 50 | Notes | Function names change, check CRAN manual | Not in source (outside information) | none | Correctly placed in Notes. Not counted as an error |

Counted: 33 Supported, 12 Imprecise, 3 Not in source, 1 Contradicted (49 claims). Rows 13 and 50 are outside information and not counted. The cross-references in Notes were not counted. They point to existing cards (turner-2020-compstat, desousa-2020-joss, desousa-2023-joss). See fix 18 on the climatrends citation year.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The rainfall split that drives the "higher rainfall" result has p = 0.079, and the tree was fitted with alpha = 0.1. The authors do not discuss this. Drier-node reliabilities are close to 0.5 with SE about 0.035 | Fig. 2 (p. 5), code (p. 4), Table 2 (p. 4) | Partly. The card says "marginally" for the drier node but "shows" for the wetter node | See fix 18, second bullet |
| Naming varies: Table 1 caption says "overall performance", text says "overall appreciation". Fig. 1 caption says "Amadeus", elsewhere "Amadeus 77" | p. 3 | No | Not needed. Minor |
| Reference [23] (Loomes and Sugden, regret theory) gives the journal as "Econ J Nepal". It should be The Economic Journal | p. 6 | No | Not needed unless the card cites the regret source |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: tools for the whole data science workflow on ranking data (preparation, modelling and validation, presentation) | Yes | high | |
| Function list and what each does | Yes | high | |
| Kendall's tau of traits against overall appreciation: yield 0.749, taste 0.653, marketability 0.639. Use to pick traits for a lighter tricot design | No | high | Fix 2 |
| Which functions the example does not demonstrate (crossvalidation, btpermute, regret) | No, and the card says the opposite | high | Fix 1, fix 5 |
| Example design: Nicaragua, five seasons 2015 to 2016, eight traits plus overall appreciation | Partly (3 of 10 only) | medium | Fix 15, fix 16 |
| Tree split at 193.82 mm, p = 0.079, alpha = 0.1, node sizes 393 and 164 (read from Fig. 2) | No | medium | Fix 3, fix 17 |
| Reliability values (Table 2) | No | medium | Fix 17 |
| Software metadata: v1.0, MIT licence, code repository, documentation site | No | medium | Fix 14 |
| Impact: ClimMob runs trials on more than 10,000 farms per year. Package supports breeding teams in Sub-Saharan Africa | No | medium | Fix 8 |
| Studies that used the methods (van Etten 2019, Moyo 2021, de Sousa 2021, Brown 2022, Alamu 2023, Gesesse 2023, Rutsaert 2023) | No (only "several published studies") | low | Optional relations in fix 18 |
| compare() is based on Bland and Altman (1986) | No | low | In fix 15 |
| node_labels, node_rules, top_items | No | low | Fix 16 |
| Other covariates possible: temperature from ag5Tools or nasapower, socio-economic covariates for market segments | No | low | Optional |
| Authors' own limitations | The paper has none. The card invents two | medium | Fix 5 |
| Conclusions: new tools needed as ranking data grows, functions not in other packages, open source, community of practice | Yes | medium | |

Important omissions counted: 6 (the high and medium "No" rows that are not already covered by a Contradicted or Imprecise claim are Kendall's tau, example design, tree split, reliability values, software metadata and ClimMob scale).

## Template compliance

- Summary word count: 411. Within 400 to 500. The replacement in fix 15 is 491.
- Gist: 22 words. Under 30, but it lists topics (fix 7).
- Keywords: 11. Within 8 to 12.
- Questions: 4. Within 4 to 7. Question 3 ("How do I compute ... regret?") is answered only by the function description. The example does not run regret.
- House style: tricot is lowercase throughout. maniva does not appear.
- not_established: missing (fix 6).
- Long-format sections are all present.
