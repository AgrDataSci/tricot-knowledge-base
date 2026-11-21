# Card review: nanyonjo-2024-cropsci

- **Card:** papers/nanyonjo-2024-cropsci.md
- **Source:** papers-pdf/nanyonjo-et-al-2024.pdf (19 pages, printed pages 2679 to 2697, so PDF page = printed page minus 2678)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 60 |
| Supported | 43 |
| Imprecise | 14 |
| Not in source | 1 |
| Contradicted | 2 |
| Source issues (problems in the source itself, not card errors) | 8 |
| Important omissions | 4 |
| Metadata issues | 4 |

Most numbers in the card are correct and the main message (rank aggregation across cycles, district more important than sex or age, R20mm as the key climate variable, three release candidates) matches the source. But the card leaves out two main results that change how a reader should use the paper: no clone beat the check NAROCASS 1 for yield-related traits, and both Plackett-Luce trees were unstable (only 530 of 1,000 resampled district trees made a split). The Stated limitations section misses the authors' own limitations and wrongly says the cycles were linked through "shared clones" (only the check was shared). The district Note invents a discrepancy that does not exist. The single most important fix is to add the yield result and the stability result to the Summary (pp. 2688, 2690 to 2691, 2693, PDF 10, 12 to 13, 15).

## Fixes needed

1. **Main result missing: no clone beat the check on yield (omission, high).** The card lists only the traits where clones did well. The source says the check was better than the clones for yield-related traits at 12 MAP (fresh root yield, size and shape) (p. 2690 to 2691, PDF 12 to 13), and all clones had inferior reliability for yield-related traits including overall performance at harvest and preferred fresh roots (p. 2693, PDF 15). Figure 7 (p. 2692, PDF 14) shows all reliability values below 0.5 in these columns. This includes the three release candidates (overall performance at harvest about 0.36 for UG110164, 0.30 for UGC14170 and 0.36 for UG120193, read off the heatmap, approximate). The authors call this a major challenge for cassava breeding. Add to the Summary (see the full replacement Summary below): "No clone beat the check for fresh root yield, size, shape or overall performance at harvest." Add to Key numbers: `| < 0.5 | Reliability of every clone against NAROCASS 1 for fresh root yield, size, shape and overall performance at harvest (Figure 7) | This paper |`

2. **Stability results missing (omission, high).** The card says split stability "was checked" but not what was found. The source reports that only 530 of 1,000 resampled district models made a split, that district was chosen in almost 90% of splitting runs, and that R20mm was chosen in almost 55% (p. 2688, PDF 10, Figure 4, and p. 2689, PDF 11, Figure 6). The authors blame the small resampled data and the fragile link between cycles through one check. Add to the Summary: "Both trees were fragile. In 1,000 resampling runs on 80% of the data, only 530 district models made a split, though district was chosen in almost 90% of those. The authors link this to the single check connecting the two cycles." Add to Key numbers:
   - `| 530 of 1,000 | Resampled district-tree models (80% of data) that made any split | This paper |`
   - `| ~90% / ~55% | Share of splitting runs that chose district (sociodemographic tree) / R20mm (climate tree) | This paper |`

3. **"Shared clones" is wrong (Contradicted, Stated limitations).** The card says comparisons rely on "connections through the check and shared clones". Table 2 (p. 2683, PDF 5) and Figure 2 (p. 2684, PDF 6) show that NAROCASS 1 was the only entry in both cycles. The source says the connection relies on one common check (p. 2688, PDF 10). The section also misses the authors' own limitations (p. 2693, PDF 15, and p. 2685, PDF 7). Replace the whole Stated limitations section with:
   - "Only one check variety, NAROCASS 1, linked the two cycles. This fragile link, with the smaller data in resampling, made the tree splits unstable (only 530 of 1,000 resampled district models made a split)."
   - "With a single check, interpretation of the trial relies heavily on how that one variety responds to the environment."
   - "Trials were lost to drought, hailstorms and, in a few cases, poor farmer management, which reduced the sample size."
   - "The interaction between gender and location was not resolved and needs further study."

4. **District Note invents a discrepancy (Contradicted, Notes).** The card says the abstract reports 10 districts while the methods list eight. The methods list six districts in cycle 1 and eight in cycle 2 (p. 2681, PDF 3). Four districts are in both cycles (Arua, Dokolo, Luwero, Serere), four are new in cycle 2 (Buikwe, Busia, Kibaale, Tororo) and two were dropped (Kaberamaido, Mityana). The union is 10, which matches the abstract, Table 1 (p. 2682, PDF 4) and the Figure 1 caption (card's own check). Replace the Note with: "The study covered 10 districts in total (abstract, Table 1, Figure 1). Cycle 1 used six districts and cycle 2 used eight. Four districts were added in cycle 2 (Buikwe, Busia, Kibaale, Tororo) and two were dropped (Kaberamaido, Mityana). The methods sentence 'scaled out to four districts' means four new districts, not four in total."

5. **Gist makes an untested comparison and is 30 words (Imprecise).** The gist says heavy-rain days "drove performance more than farmer traits". The climate tree was fitted with climate variables only, so the paper does not compare rainfall with farmer traits (p. 2686, PDF 8). "Drove" is also stronger than the source's "influenced". The gist is 30 words, not under 30. It also leaves out the yield result. Replace with: "tricot trials of 20 cassava clones in Uganda, merged over two cycles, showed district shaped rankings more than sex or age, and no clone beat the check on yield" (29 words).

6. **"Recommendations should follow rainfall patterns" (Not in source, Summary).** The source does not say this. It proposes UG130007 as a source of drought-tolerance genes for future crosses and calls for genome-wide association studies (p. 2692, PDF 14). Replace "so recommendations should follow rainfall patterns" with: "and propose UG130007 as a parent for drought tolerance in future crosses, to be followed by genome-wide association studies."

7. **Clone origin (Imprecise, Summary and Methods).** The card says all clones are from the NextGen population at NaCRRI. Four clones (MM06/123, MM16/0707, MM16/1627, MM2018/0054) were supplied by the IITA breeding programme (p. 2681, PDF 3, and Table 2, p. 2683, PDF 5). The card also does not say that cycle 1 had 11 clones and cycle 2 had nine. Methods replacement: "- **Material.** 20 elite clones plus check NAROCASS 1, from uniform yield trials of cycles 0 and 1 of the NextGen population at NaCRRI. Four clones came from IITA. Cycle 1 tested 11 clones and cycle 2 tested nine, and NAROCASS 1 was the only entry in both cycles." Key numbers addition: `| 11 + 9 | Clones in cycle 1 and cycle 2, with NAROCASS 1 the only shared entry | This paper |`

8. **"In one node" does not say which tree (Imprecise, Summary).** The sentence follows the climate sentence, so it reads as the climate tree. It is node 2 of the district tree (Busia, Dokolo, Kaberamaido, Kibaale, Luwero, Serere) (p. 2687, PDF 9, Figure 3). Replace with: "In one district node, UG130016, UG110164 and UG130007 ranked highest but did not differ from NAROCASS 1."

9. **"Plackett-Luce trees were fitted with sociodemographic and climatic covariates" (Imprecise, Summary).** There were two separate trees, one with sex, age and district and one with 30 climatic variables (pp. 2686 to 2687, PDF 8 to 9, Table 4). District is the variable that split, so it should be named. Replace with: "Two Plackett-Luce trees were fitted on overall performance at harvest, one with sex, age and district and one with 30 climatic variables, with a minimum node size of 10%." (30 is the card's own count of Table 4.)

10. **"After cleaning" (Imprecise, Summary and Key numbers).** The source says trials were lost to drought, hailstorms and, in a few cases, poor management (p. 2685, PDF 7). It does not describe data cleaning. Key numbers replacement: `| 484 trials (207 + 277) | tricot trials remaining after losses to drought, hailstorms and poor management, cycles 1 and 2 | This paper |`

11. **Conclusion wording (Imprecise, Summary).** "Farmers' input on food quality traits is essential" is stronger than the source, which says the study emphasizes the important contribution of end-users to crop improvement (p. 2679, PDF 1, and p. 2693, PDF 15). The NAROCASS 1 recommendation is conditional: keeping it is recommended if the goal is to compare against the same reference, but other clones from this study can also keep the network connected (p. 2693, PDF 15). Use the wording in the replacement Summary below.

12. **Gender and location bullet (Imprecise, Stated limitations).** "Men's and women's trait preferences may depend on location, as also found in Nigeria" is not a limitation of this study. The source cites Iragaba et al. 2021 (Uganda) and Teeken et al. 2018 (Nigeria) for this finding (p. 2691, PDF 13). The authors' own point is that the gender by location interaction needs further study (p. 2693, PDF 15). Covered by the replacement in fix 3.

13. **Joint first authorship (Imprecise, Notes).** The card says Angudubo is joint first author "per the team". The PDF itself states that Nanyonjo, Angudubo and Paula Iragaba share first authorship (p. 2679, PDF 1). Replace with: "Ann Ritah Nanyonjo is first and corresponding author. The PDF states that Nanyonjo, Stephen Angudubo and Paula Iragaba share first authorship. Robert Kawuki is last author. Cite as Nanyonjo et al. 2024."

14. **"All strongly shaped by the growing environment" (Imprecise, Summary).** The source links the composite harvest score to the location effect ("Consequently") but does not say the traits are strongly shaped by the environment (p. 2691, PDF 13). Use the wording in the replacement Summary.

15. **Metadata.** See the Metadata check. Article: `64(5), 2679-2697`. Data: `Code and data at https://github.com/EQUAL-Lab/NextGen_Cassava_tricot_Uganda (data availability statement)`. Add not_established:
   `not_established: that any of the 20 clones out-yields NAROCASS 1 on-farm; that UG130007 is drought tolerant (a hypothesis, and its advantage in the dry node was not significant at p < 0.05); that gender does not affect cassava trait preferences; that the district and rainfall splits are stable; that UG110164, UGC14170 or UG120193 have been released as varieties`

16. **Key numbers threshold (source issue, see below).** Replace the ">20 mm" row with: `| ≥20 mm, ≤2 vs >2 days | R20mm (days with rainfall of 20 mm or more) and its split between drier and wetter nodes (Table 4, Figure 5) | This paper |`

**Full replacement Summary (498 words, card's own count), ready to paste:**

The study applies tricot to participatory variety selection of elite cassava clones from the NextGen population at Uganda's National Crops Resources Research Institute (NaCRRI), four of them supplied by IITA. It had three aims, namely to synthesize data from two cycles with different clone sets, to assess agronomic performance against sociodemographic, geographic and climatic factors, and to evaluate clones for agronomic and food quality traits.

Trials ran in 10 districts across six agroecological zones, in 2019 to 2020 and 2021 to 2022. Cycle 1 tested 11 clones and cycle 2 tested nine, and the check NAROCASS 1 was the only entry in both. Farmer groups of at least 30 men and women per parish supplied 294 men and 320 women as hosts. Farmers ranked the best and worst of their three clones for 26 traits, from vigor at 3 months after planting to harvest at 12 months, and for a boiled product and a flour-based meal. Drought, hailstorms and some poor management caused losses, leaving 484 trials (207 in cycle 1, 277 in cycle 2) for aggregation.

Two Plackett-Luce trees were fitted on overall performance at harvest, one with sex, age and district and one with 30 climatic variables, with a minimum node size of 10%. District split the data, while sex and age were not selected. In one district node, UG130016, UG110164 and UG130007 ranked highest but did not differ from NAROCASS 1. In the climate tree, the number of days with rainfall of 20 mm or more separated drier sites (2 days or fewer) from wetter ones, and in the wetter node no clone outperformed the check. Both trees were fragile. In 1,000 resampling runs on 80% of the data, only 530 district models made a split, though district was chosen in almost 90% of those. The authors link this to the single check connecting the two cycles.

Reliability, the probability of outperforming NAROCASS 1, was computed for every trait. No clone beat the check for fresh root yield, size, shape or overall performance at harvest. MM16/1627, UG110164 and MM20180054 had high reliability for lower disease susceptibility (0.74, 0.68 and 0.65), UG120198 and UG120156 for ease of drying (0.78 and 0.76), and UG110164 and UGC14170 for mealiness and preferred boiled food. No clone was significantly better for flour-meal traits. UG110164, UGC14170 and UG120193 were put forward as release candidates targeting food products.

The authors conclude that rank aggregation lets programmes merge cycles with different entries, saving time and resources, and that end-users make an important contribution to crop improvement. Overall performance at harvest combined yield, root shape and size and stem quality, which may explain why location mattered more than farmer characteristics. Citing other studies, they add that gender differences can depend on location and are too complex for binary models. They hypothesize that UG130007 is drought tolerant and propose it as a parent for future crosses. They recommend keeping NAROCASS 1, or other clones from this study, in future trials to keep the network connected.

(The counts "26 traits" and "30 climatic variables" are the reviewer's counts of Table 3 and Table 4. The curator may want to add "(card's own count)" in Key numbers if these are listed there.)

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | On-farm evaluation of cassava clones using the triadic comparison of technology options approach | Same (p. 2679, PDF 1) | Supported |
| authors | Nanyonjo AR, Angudubo S, Iragaba P, Brown D, Nuwamanya E, Esuma W, Ozimati A, Wembabazi E, Kanaabi M, Muhumuza N, Bayiyana I, van Etten J, de Sousa K, Tufan H, Kawuki RS | Same 15 authors in the same order (p. 2679, PDF 1, and citation p. 2697, PDF 19) | Supported |
| year | 2024 | Published online 3 July 2024, Crop Science 2024 (p. 2679, PDF 1) | Supported |
| journal | Crop Science | Crop Science (p. 2679, PDF 1) | Supported |
| article | 64(5) (published online July 2024) | Crop Science 2024, volume 64, pages 2679-2697, issue 5 (p. 2679, PDF 1, download banner) | Imprecise. Page range missing. Use `64(5), 2679-2697` |
| type | research article | "Original article", Crop Breeding & Genetics (p. 2679, PDF 1) | Supported |
| doi | https://doi.org/10.1002/csc2.21293 | 10.1002/csc2.21293 (p. 2679, PDF 1) | Supported |
| license | CC BY | Open access under the Creative Commons Attribution License, no version given (p. 2679, PDF 1) | Supported |
| data | see the data availability statement in the article | Code and data at https://github.com/EQUAL-Lab/NextGen_Cassava_tricot_Uganda (p. 2694, PDF 16) | Imprecise. Give the repository URL |
| crops | cassava | Cassava (Manihot esculenta) | Supported |
| region | Uganda | Uganda, 10 districts (p. 2679, PDF 1) | Supported |
| gist | tricot evaluation of 20 elite cassava clones with 614 farmers ... heavy-rain days drove performance more than farmer traits | 614 is a correct sum (294 + 320) of recruited hosts, but only 484 trials were analyzed. Climate and farmer traits were not compared in one model (p. 2686, PDF 8). 30 words | Imprecise (see fix 5) |
| not_established | missing | Several stretchable claims (yield, drought tolerance, gender, release status, tree stability) | Missing. Add (fix 15) |
| software (optional) | PlackettLuce, gosset | Also ClimMobTools, stablelearner, ag5Tools, climatrends (pp. 2685 to 2686, PDF 7 to 8) | Supported but incomplete, low importance |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | tricot applied to PVS of elite clones from NextGen population at NaCRRI | Imprecise | p. 2681 (PDF 3), Table 2 p. 2683 (PDF 5) | Four clones from IITA |
| 2 | Summary | Three aims (synthesis, sociodemographic and climatic factors, agronomic and food traits) | Supported | Abstract p. 2679 (PDF 1), p. 2681 (PDF 3) | Intro says "geographic" instead of "climatic" in aim 2 |
| 3 | Summary | Trials ran over two cycles | Supported | p. 2681 (PDF 3) | |
| 4 | Summary | Farmer group of at least 30 men and women per parish | Supported | p. 2683 (PDF 5) | |
| 5 | Summary | Second cycle scaled out to more districts | Supported | p. 2681 (PDF 3) | |
| 6 | Summary | 20 clones + NAROCASS 1, 294 men and 320 women | Supported | p. 2679 (PDF 1), Table 1 p. 2682 (PDF 4) | Table 1 totals recomputed: 122 + 172 = 294, 117 + 203 = 320 |
| 7 | Summary | Best and worst ranking from vigor to 12 MAP and food traits | Supported | p. 2684 (PDF 6), Table 3 p. 2685 (PDF 7) | |
| 8 | Summary | 484 trials after cleaning (207 + 277), aggregated | Imprecise | p. 2685 (PDF 7) | Sum correct. Trials were lost, not cleaned |
| 9 | Summary | PL trees with sociodemographic and climatic covariates | Imprecise | pp. 2686 to 2687 (PDF 8 to 9) | Two separate trees, district not named |
| 10 | Summary | Minimum node size 10% | Supported | p. 2686 (PDF 8) | |
| 11 | Summary | 1,000 resampling runs on 80% of data | Supported | p. 2686 (PDF 8) | Without replacement |
| 12 | Summary | Geographic more than sociodemographic factors | Supported | Abstract p. 2679 (PDF 1), p. 2688 (PDF 10) | Applies to overall performance at harvest |
| 13 | Summary | Days with rainfall above 20 mm most influential climate variable | Supported | Abstract p. 2679 (PDF 1), Figure 5 p. 2689 (PDF 11) | Threshold ≥ vs > inconsistent in source |
| 14 | Summary | In one node UG130016, UG110164, UG130007 best, no difference from check | Imprecise | p. 2687 (PDF 9), Figure 3 p. 2688 (PDF 10) | Node 2 of the district tree, not stated |
| 15 | Summary | Reliability = probability of outperforming NAROCASS 1, found trait advantages | Supported | p. 2686 (PDF 8), p. 2689 (PDF 11) | |
| 16 | Summary | Disease: MM16/1627, UG110164, MM20180054 (0.74, 0.68, 0.65) | Supported | p. 2690 (PDF 12), Figure 7 p. 2692 (PDF 14) | Bold (p < 0.05) in Figure 7 |
| 17 | Summary | Ease of drying: UG120198, UG120156 (0.78, 0.76) | Supported | p. 2691 (PDF 13), Figure 7 | |
| 18 | Summary | UG110164, UGC14170, UG120193 release candidates for food products | Supported | Abstract p. 2679 (PDF 1), conclusion p. 2693 (PDF 15) | |
| 19 | Summary | Rank aggregation merges cycles, saves time and resources | Supported | p. 2693 (PDF 15) | |
| 20 | Summary | Farmers' input on food quality traits is essential | Imprecise | pp. 2679, 2693 (PDF 1, 15) | Source says "important contribution" of end-users |
| 21 | Summary | Recommend keeping NAROCASS 1 as check for comparability | Imprecise | p. 2693 (PDF 15) | Source says not mandatory if other clones from this study are kept |
| 22 | Summary | Overall performance at harvest integrated yield, shape, size, stem quality | Supported | Table 3 p. 2685 (PDF 7), p. 2691 (PDF 13) | |
| 23 | Summary | These traits are all strongly shaped by the environment | Imprecise | p. 2691 (PDF 13) | Implied by "Consequently", not stated |
| 24 | Summary | Studies in Uganda and Nigeria: gender differences depend on location | Supported | p. 2691 (PDF 13) | Iragaba et al. 2021, Teeken et al. 2018 |
| 25 | Summary | Gender differences too complex for binary models, may explain no gender split | Supported | p. 2691 (PDF 13) | Source cites McDougall et al. 2022 |
| 26 | Summary | UG130007 hypothesized drought tolerant, good in drier node | Supported | p. 2691 to 2692 (PDF 13 to 14) | Advantage p = 0.064 (Table 5) |
| 27 | Summary | UG130016 better adapted to wetter conditions | Supported | p. 2691 to 2692 (PDF 13 to 14) | |
| 28 | Summary | So recommendations should follow rainfall patterns | Not in source | p. 2692 (PDF 14) | Source proposes UG130007 for crosses and GWAS |
| 29 | Methods | 20 clones from NaCRRI UYT (cycles 0 and 1) plus check | Imprecise | p. 2681 (PDF 3), Table 2 | Four IITA clones, 11 + 9 split missing |
| 30 | Methods | One farmer group of at least 30 per parish | Supported | p. 2683 (PDF 5) | |
| 31 | Methods | Best and worst rankings up to 12 MAP and food traits | Supported | p. 2684 (PDF 6), Table 3 | |
| 32 | Methods | Rank aggregation, PL trees, min node 10%, 1,000 runs on 80%, reliability | Supported | pp. 2685 to 2686 (PDF 7 to 8) | |
| 33 | Limitations | Men's and women's preferences may depend on location, as in Nigeria | Imprecise | p. 2691 (PDF 13), p. 2693 (PDF 15) | Cited finding of other studies, not a limitation of this study |
| 34 | Limitations | Cycles connected through the check and shared clones | Contradicted | Table 2 p. 2683 (PDF 5), Figure 2 p. 2684 (PDF 6), p. 2688 (PDF 10) | Only the check was shared |
| 35 | Key numbers | 20 clones + 1 check | Supported | p. 2679 (PDF 1) | 11 + 9 = 20 |
| 36 | Key numbers | 294 men, 320 women | Supported | p. 2679 (PDF 1), Table 1 | |
| 37 | Key numbers | 484 trials (207 + 277) after cleaning | Imprecise | p. 2685 (PDF 7) | "After losses", not cleaning. Node sizes 306 + 178 and 99 + 385 also give 484 |
| 38 | Key numbers | ≥30 farmers per group | Supported | p. 2683 (PDF 5) | |
| 39 | Key numbers | 12 MAP harvest | Supported | Table 3 | |
| 40 | Key numbers | 10% minimum node | Supported | p. 2686 (PDF 8) | |
| 41 | Key numbers | 1,000 runs, 80% | Supported | p. 2686 (PDF 8) | |
| 42 | Key numbers | >20 mm threshold | Supported | p. 2689 (PDF 11) | Table 4 and Figure 5 say ≥20 mm (source issue) |
| 43 | Key numbers | 0.74 / 0.68 / 0.65 disease | Supported | p. 2690 (PDF 12) | |
| 44 | Key numbers | 0.78 / 0.76 drying | Supported | p. 2691 (PDF 13) | |
| 45 | Notes | Nanyonjo first and corresponding author | Supported | p. 2679 (PDF 1) | |
| 46 | Notes | Angudubo joint first author "per the team" | Imprecise | p. 2679 (PDF 1) | PDF states it, and Iragaba also shares first authorship |
| 47 | Notes | Kawuki senior author | Supported | p. 2679 (PDF 1), p. 2693 to 2694 (PDF 15 to 16) | Last author, supervision and funding roles. "Senior" is an inference |
| 48 | Notes | Abstract 10 districts vs methods eight | Contradicted | p. 2681 (PDF 3), Table 1, Figure 1 | 6 + 4 new = 10. No discrepancy |
| 49 | Frontmatter | title | Supported | p. 2679 (PDF 1) | |
| 50 | Frontmatter | authors | Supported | p. 2679 (PDF 1) | |
| 51 | Frontmatter | year | Supported | p. 2679 (PDF 1) | |
| 52 | Frontmatter | journal | Supported | p. 2679 (PDF 1) | |
| 53 | Frontmatter | article | Imprecise | p. 2679 (PDF 1) | Pages missing |
| 54 | Frontmatter | type | Supported | p. 2679 (PDF 1) | |
| 55 | Frontmatter | doi | Supported | p. 2679 (PDF 1) | |
| 56 | Frontmatter | license | Supported | p. 2679 (PDF 1) | |
| 57 | Frontmatter | data | Imprecise | p. 2694 (PDF 16) | URL available |
| 58 | Frontmatter | crops | Supported | | |
| 59 | Frontmatter | region | Supported | | |
| 60 | Frontmatter | gist | Imprecise | p. 2686 (PDF 8) | Untested comparison, 30 words |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| R20mm defined as rainfall ≥20 mm in Table 4 and the Figure 5 caption, but as >20 mm in the abstract, Section 3.2 and the conclusion | Table 4 p. 2687 (PDF 9), p. 2689 (PDF 11), p. 2679 (PDF 1), p. 2693 (PDF 15) | No (card uses >20 mm) | "R20mm is defined as days with rainfall of 20 mm or more in Table 4, but the text says more than 20 mm. The table definition is used here." |
| Section 3.2 says UG130007 was "superior" to the check in the dry node, citing Figure 3 (should be Figure 5). Table 5 gives reliability 0.819 with p = 0.064, so not significant at the 0.05 level used elsewhere. The Discussion repeats "superior" | p. 2689 (PDF 11), Table 5 p. 2690 (PDF 12), p. 2692 (PDF 14) | No | "The text calls UG130007 superior to NAROCASS 1 in the dry climate node, but Table 5 gives p = 0.064 (reliability 0.819). Treat the drought-tolerance claim as a hypothesis." |
| Section 3.3 says UG130016 "did not significantly differ from the check (p < 0.1)", but Table 6 gives p = 0.278 | p. 2689 (PDF 11), Table 6 p. 2691 (PDF 13) | No | Low importance. Optional Note: "Section 3.3 cites p < 0.1 for UG130016 in the wet node, while Table 6 gives p = 0.278." |
| The Discussion uses "node 3 (Figure 3)", the district node with Arua, Buikwe, Mityana and Tororo, to argue about high rainfall, which mixes the district tree with the climate tree. UG130007 was also among the top clones in that district node, which sits uneasily with the drought-tolerance hypothesis | p. 2687 (PDF 9), p. 2692 (PDF 14) | No | "The Discussion links the district node with Mityana and Buikwe to high rainfall, mixing the district and climate trees. UG130007 ranked high in that district node too." |
| Clone names spelled two ways: UG15F265P001 (Table 2) vs UG15FF265P001 (Tables 5 and 6, Figures 3, 5 and 7, text), and MM2018/0054 (Methods, Table 2) vs MM20180054 (elsewhere) | Table 2 p. 2683 (PDF 5), Tables 5 to 6, Figure 7 | No | "Clone names vary in the source: UG15F265P001 is also written UG15FF265P001, and MM2018/0054 is also written MM20180054." |
| Table 1 gives an age SD of 47.5 for Serere in cycle 2 with a mean of 46.9, far above all other SDs (8.8 to 15.3). Probably a typo | Table 1 p. 2682 (PDF 4) | No | Low importance. Optional. |
| The phrase "scaled out to four districts and, consequently, ... eight districts" is easy to misread as a conflict with "10 districts" | p. 2681 (PDF 3) | Card misreads it as a conflict (fix 4) | Use the replacement Note in fix 4 |
| Aim 2 says "sociodemographic and climatic factors" in the abstract but "sociodemographic and geographic factors" in the Introduction | p. 2679 (PDF 1), p. 2681 (PDF 3) | No | Low importance. The replacement Summary uses "sociodemographic, geographic and climatic" |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: show usefulness of tricot for PVS in cassava, three specific aims | Yes | high | |
| Design: 10 districts, six agroecological zones near six ZARDIs, cycle dates (April 2019 to June 2020, September 2021 to October 2022) | Partly (no district count, zones or dates) | medium | In replacement Summary |
| 11 clones in cycle 1, nine in cycle 2, only the check shared, four clones from IITA | No | high (for anyone planning to merge cycles) | Fix 7 |
| Sample: 294 men, 320 women, 484 trials retained (207 + 277), 10 + 10 hosts per group in cycle 1 and 12 + 12 in cycle 2 | Mostly (host numbers per group missing) | medium | Methods: "- **Hosts.** 10 men and 10 women per farmer group in cycle 1, 12 men and 12 women in cycle 2." |
| Check beat all clones for yield-related traits, including the release candidates | No | high | Fix 1 |
| Tree stability: 530 of 1,000 split, district ~90%, R20mm ~55% | No | high | Fix 2 |
| District tree: node 2 n = 306 (Busia, Dokolo, Kaberamaido, Kibaale, Luwero, Serere), node 3 n = 178 (Arua, Buikwe, Mityana, Tororo), top clones in node 3 UG130007, UG120124, UGC14170, UG120024 lowest in both | Partly (node 2 top clones only) | medium | Key numbers: `| 306 / 178 | Trials in district-tree node 2 / node 3 (Figure 3) | This paper |` |
| Climate tree: node 2 (≤2 days R20mm, n = 99), node 3 (>2 days, n = 385), check best in wet node, UG130007 reliability 0.819 (p = 0.064) in dry node | Partly | medium | Key numbers: `| 99 / 385 | Trials in the drier (≤2 days with ≥20 mm rain) / wetter climate node (Figure 5) | This paper |` and `| 0.819 (p = 0.064) | Reliability of UG130007 against NAROCASS 1 in the drier climate node (Table 5) | This paper |` |
| Boiled-product results: mealiness UG110164 0.73, UGC14170 0.71, UG15F302P513 0.70, softness UG110164 0.69, less fibrous UG110164 and UG120193 0.68, preferred boiled food UG110164 0.66 and UGC14170 0.64 | No | high (basis for release candidates) | Key numbers: `| 0.73 / 0.71 / 0.70 | Reliability for boiled root mealiness, UG110164 / UGC14170 / UG15F302P513 | This paper |` and `| 0.66 / 0.64 | Reliability for preferred boiled food, UG110164 / UGC14170 | This paper |` |
| No clone significantly better than the check for flour-meal traits | No | medium | In replacement Summary |
| Vigor (UG110164 0.71, UG15F140P003 0.67, MM16/1627 0.66) and height (UG15FF265P001 0.75, UG15F140P003 0.75, UG15F302P513 0.72) | No | low | Optional Key numbers rows |
| Trial protocol: 9 m by 12 m plots, 1 m between plants, 2 m between plots, blind codes A, B, C, 26 traits at 3, 6, 9 and 12 MAP, boiled product in all locations and flour meal (kwon) in Serere, Arua, Tororo, Kaberamaido and Busia | No | medium (practical for tricot users) | Methods: "- **Plots.** 9 m by 12 m, 1 m between plants and 2 m between plots, clones blind-coded A, B and C. 26 traits at 3, 6, 9 and 12 MAP. Boiled roots evaluated in all locations, flour-based meal (kwon) in five districts." |
| Analysis settings: α = 0.05 with Bonferroni correction, npseudo = 0.5, AgERA5 climate data via ag5Tools, indices via climatrends, reliability via gosset | Partly | low | Add to the Analysis bullet: "α = 0.05 with Bonferroni correction, npseudo = 0.5, AgERA5 climate data from planting to harvest." |
| Authors' limitations: single check, trial losses, interpretation depends on the check | No | high | Fix 3 |
| Other conclusions: UG110164 as an alternative to landraces, UG120156 and UG120198 possibly high dry matter for the starch industry (to be confirmed), MM16/1627, UG110164 and MM20180054 as possible disease-tolerant substitutes for NAROCASS 1 | No | low to medium | Optional Notes |
| Recommendations: integrate new tricot data to update findings, study gender by location interaction | Partly | medium | Fix 3 covers gender by location |

## Template compliance

- Summary: 431 words, within 400 to 500. The replacement Summary is 498 words.
- Gist: 30 words, not under 30. Replacement is 29 words.
- Keywords: 11, within 8 to 12.
- Questions: 4, within 4 to 7. The question "Do farmer sociodemographics or environment matter more" is fine, but the card should then report the stability caveat (fix 2).
- House style: tricot is lowercase throughout. No em dashes or semicolons in the card body.
- not_established is missing (fix 15).
- Long format is used and all long-format sections are present.
