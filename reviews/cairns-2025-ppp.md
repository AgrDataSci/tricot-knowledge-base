# Card review: cairns-2025-ppp

- **Card:** papers/cairns-2025-ppp.md
- **Source:** papers-pdf/cairns-et-al-2025.pdf (18 pages, printed pages 259 to 276. PDF page = printed page minus 258)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 49 |
| Supported | 40 |
| Imprecise | 8 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 13 |
| Important omissions | 10 (4 high, 6 medium) |
| Metadata issues | 2 (author order, license version) |

The card gets the two main findings right: trial hosts matched the surveyed population's farm types, and women-headed households split into two very different types. Its numbers are accurate against the paper's text. The most important fix is the Summary's list of farm-type labels. These come from the figure legends, which contradict Table 4 and the results text, so a reader would wrongly take type 2 as a women-headed type and type 3 as the poorer women-associated type. The card's own Notes flag this, but the Summary does not follow its own advice. The second most important fix is the missing author-stated limitation that there was no control group, which matters because the card says gender targets "therefore" ensured representation. The Summary is also below the 400-word minimum (383 words), which leaves room for the missing results.

## Fixes needed

1. **Farm-type labels in the Summary (high).** The card lists the types as "average men-headed, average women-headed, resource-constrained women-headed, relatively prosperous, and primarily off-farm". These are the figure legend labels (Figure 1, p. 262, PDF p. 4, and Figures 4, 6, 7, Tables 5 and 6). Table 4 (p. 268, PDF p. 10) shows type 2 is only 4.4% women-headed and type 4 is 72% women-headed with the second-lowest equipment value. The results text (p. 267) and discussion (p. 270 to 271) call types 3 and 4 the women-associated types, and type 3 the wealthier. Replace the full Summary with the text in fix 2, or at minimum replace the sentence with:
   > Five farm types emerged. Types 1, 2 and 5 were mostly men-headed, with type 1 the best endowed and type 5 relying mainly on off-farm income. Types 3 and 4 were mostly women-headed. The paper's figure legends label the types differently (see Notes).

2. **Summary below 400 words, missing key results and the no-control-group caveat (high).** The Summary has 383 words. It omits the women-headed share in hosts and population (31.7% and 32.5%, Table 2, p. 265), the most discriminating variables (p. 267, Figure 5), the ex-ante use of the typology (p. 271) and the authors' limitation that there was no control group (p. 271). It also uses wording more certain than the source in three places (fixes 4, 5, 6). Suggested full replacement Summary (481 words):
   > On-farm testing only predicts how varieties will perform for farmers if the host farms represent the target population of environments, yet earlier studies found that host farmers can be more prosperous and better educated than their neighbours. Jill Cairns, Frédéric Baudron and colleagues at CIMMYT, CIRAD and Rothamsted checked, after the fact, whether host farmers in CIMMYT's participatory maize testing network in Zimbabwe represented the wider population, and piloted a typology approach for selecting hosts.
   >
   > In 18 randomly selected districts across five provinces, mostly in natural regions 3 and 4, extension agents randomly sampled 2,346 farms from village registries, with women and men in proportion to ward population. The 2021 survey covered maize production over two years, inputs, management, farm and livestock assets and demographics. Seventeen structural and functional variables fed a typology of 2,040 farms. A classification random forest found equipment value, sex of the household head, cattle numbers and maize production the most discriminating variables. Extension agents trained to include women and resource-constrained farmers chose the 191 trial hosts without CIMMYT input, and the hosts were part of the sample.
   >
   > Five farm types emerged. Types 1, 2 and 5 were mostly men-headed, with type 1 the best endowed and type 5 relying mainly on off-farm income. Types 3 and 4 were mostly women-headed. The paper's figure legends label the types differently (see Notes). About 32% of both hosts and other surveyed farms were women-headed. Host farms were distributed across the five types much like the surveyed population, with the off-farm type slightly under-represented. Hosts did not differ from the population in equipment or livestock, but the authors report almost 20% more maize production, which may partly reflect more hosts relying on farming for income. The authors conclude that gender-based targets ensured adequate representation of women, but with no control group they cannot say how much the training of extension agents helped.
   >
   > The typology also showed that gender alone hides important differences. The two women-associated types differed sharply. Type 3 owned more equipment and livestock and produced almost three times as much maize as type 4, which used less fertilizer and manure and intercropped more. Type 3 was closer to the men-headed type 1 than to type 4. Selecting hosts only by the sex of the household head would miss these differences in constraints and opportunities.
   >
   > The authors recommend sampling strategies that explicitly incorporate agronomic and socio-economic diversity. A typology could guide recruitment before trials, with hosts chosen in proportion to each farm type, extra hosts from types such as 3 and 4, and gender targets for plot managers within each type. Farming systems change quickly, so surveys may need repeating every year or two. Hosts were under 10% of those surveyed, so the authors call for research on the minimum survey size, which they expect to be much smaller, and expect key variables to differ by crop and region.

3. **Stated limitations miss the authors' own main limitation (high).** The authors say there was no control group of hosts chosen without training, which limits any claim about the benefit of training (p. 271, PDF p. 13). They also call the down-weighting of binary variables subjective, and say typologies can carry implicit and explicit bias. Add these bullets after "Typologies reduce a multidimensional continuum to discrete types.":
   > - No control group of hosts chosen by untrained extension agents, so the effect of training on representativeness cannot be quantified.
   > - The factor used to down-weight binary variables is a subjective choice, and typology construction can carry implicit and explicit bias.
   > - The share of men plot managers in men-headed households was higher than in earlier Zimbabwe research, perhaps because of the simplified definitions.
   > - Relying on local extension knowledge worked here, but local intermediaries elsewhere sometimes exclude under-represented groups.

4. **Host maize production wording (medium).** The card says hosts produced almost 20% more maize "partly because more of them relied on farming for income". The source says the difference "may be related, in part" to this and to fewer type 5 hosts (p. 269, PDF p. 11). Also, Table 2 gives 2,742.9 versus 2,103.2 kg, which is about 30% more (see Source issues). The replacement Summary in fix 2 uses "the authors report almost 20% more maize production, which may partly reflect more hosts relying on farming for income". Replace the Key numbers row with:
   > | ~20% (text) / ~30% (Table 2) | Higher maize production of host farms than the rest of the surveyed population. The text says almost 20%, but Table 2 means (2,742.9 vs 2,103.2 kg) give about 30% (card's calculation) | This paper, p. 264 to 265 and 269 |

5. **"Often" more prosperous (low).** The card says host farmers are "often" more prosperous and better educated. The source says earlier studies have shown they "can be" (p. 269, PDF p. 11). Fixed in the replacement Summary.

6. **Recommendations paragraph (medium).** The card says the authors recommend "guarding against elite capture and unconscious bias, and reporting the characteristics of host farmers". The source concludes that its retrospective check "confirmed minimal elite capture and unconscious bias" (p. 272). It does not frame this as a recommendation. On reporting, it only mentions ensuring (and reporting) women's participation (p. 269). The card also misses the concrete ex-ante proposal on p. 271 and the advice to repeat surveys every year or two. It also says key variables "will differ", where the source says "likely to change". Fixed in the replacement Summary.

7. **Methods "Comparison" bullet uses 186 (medium).** Section 2.3 and Tables 2 and 3 compare 191 hosts with the population and by gender. Only Table 6 (farm types) sums to 186 (p. 264 to 266, 270). Replace with:
   > - **Comparison.** 191 trial-hosting farms (stage 5 trials of one breeding pipeline, hosts chosen by extension agents with no CIMMYT input) compared with the other 1,846 surveyed farms on 17 characteristics. Women- and men-headed households compared within hosts and within the population. 186 hosts placed in the five farm types (Table 6).

8. **Author order (medium, metadata).** The card lists Baudron second and Euler and Amondo before Voss. The PDF title page (p. 259) and the "How to cite" box (p. 276) give a different order. Replace with:
   > authors: Cairns JE, Zaman-Allah M, Baudron F, Voss RC, Hassall KL, Euler M, Amondo E, Marenya PP, Prasanna BM

9. **Note says "not tricot trials" and "researcher-designed" (low, Not in source).** The paper never describes the design of the stage 5 trials and never says whether they are tricot or researcher-designed (p. 261, 264). If the card writers know this from outside the paper, label it. Replace the second Notes bullet with:
   > - The paper does not describe the design of the stage 5 on-farm trials or say whether they were tricot trials (p. 264). Outside this paper: the card writers understand these hosts are in CIMMYT's conventional participatory variety testing network, not tricot. The sampling argument applies to tricot, and cairns-2026-jxb builds on it for inclusive host-farmer sampling in maize breakthrough products.

10. **not_established is missing the biggest stretch (medium).** The paper is likely to be cited as proof that training extension agents produces representative hosts, but there was no control group. Replace with:
    > not_established: that representative host farmers change which hybrids are advanced (not tested); that training extension agents caused the good representation (no control group); that farm types differ in variety preferences (preferences not measured); that these five farm types or key variables hold for other crops, regions or years (the authors expect them to change); the minimum survey size needed for a typology (the authors call it an open question); that the hosts were tricot farmers (the paper does not describe the trial design)

11. **Key numbers to add (medium).** Add these rows:
    > | 191 | Trial hosts in the host versus population comparison (section 2.3, Tables 2 and 3). Table 6 places 186 of them in farm types | This paper |
    > | 31.7% / 32.5% | Women-headed households in the surveyed population / among hosts (P = 0.999) | This paper, Table 2 |
    > | 27.5% / 32.5% | Women plot managers in the surveyed population / among hosts (P = 0.403) | This paper, Table 2 |
    > | 0.24 / 0.42 | Distance between cluster centroids of types 1 and 3 / types 3 and 4 (about 1.7 times greater) | This paper, Table 5 |
    > | 41% / 55% / 47% | Lower equipment value, cattle and small ruminants in women-headed than men-headed host households | This paper, p. 265 |
    > | 37% / 20% | Women-headed households with more equipment value / more cattle than the average men-headed household | This paper, p. 265 and 267 |

    And change the 186 row context to: "Trial-hosting farms placed in farm types (39, 70, 26, 26 and 25 across types 1 to 5). The text and Tables 2 and 3 give 191 hosts".

12. **Notes additions (low).** Extend the first Notes bullet and add a source-issues bullet:
    > - The paper labels farm types inconsistently. Figure legends and the captions of Tables 5 and 6 call type 2 average women-headed, type 3 resource-constrained women-headed and type 4 relatively prosperous. Table 4 shows type 2 is 4.4% women-headed and type 4 is 72% women-headed with low assets, and the results and discussion name types 3 and 4 as the women-associated types, with type 3 the wealthier. This card describes the types by their data.
    > - Numbers to double-check in the source: 191 hosts in the text and Tables 2 and 3, but Table 6 sums to 186, and 1,846 + 191 = 2,037, not 2,040. Host maize production is "almost 20%" higher in the text but about 30% higher from Table 2 means. "Almost three times" more maize in type 3 than type 4 fits the previous-year figures (3.1 times) better than total production (2.4 times, Table 4). Intercropping of 59% (type 3) and over 91% (type 4) in the text differs from 36% and 51% in Table 4.

13. **License (low, metadata).** The PDF says "Creative Commons Attribution License" without a version (p. 259). Suggested: `license: CC BY (Creative Commons Attribution License, version not stated in the PDF)`. Keep CC BY 4.0 only if the team checked the version on the publisher page.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Know your men and women farmers. Ensuring host farmers ... | Colon after "farmers" (p. 259). Colon to period is expected | Supported |
| authors | Cairns JE, Baudron F, Zaman-Allah M, Euler M, Amondo E, Voss RC, Hassall KL, Marenya PP, Prasanna BM | Cairns, Zaman-Allah, Baudron, Voss, Hassall, Euler, Amondo, Marenya, Prasanna (p. 259, p. 276 "How to cite") | Imprecise (order wrong) |
| year | 2025 | Accepted 12 June 2025, © 2025 (p. 259). Issue 2026, and "How to cite" gives 2026 (p. 276). Card explains this in `article` | Supported |
| journal | Plants, People, Planet | p. 259 | Supported |
| article | 8(1), 259-276 (2026 issue, published online 2025) | Volume 8, pages 259 to 276, issue 1 (p. 259, 276) | Supported |
| type | research article | "RESEARCH ARTICLE" (p. 259) | Supported |
| doi | https://doi.org/10.1002/ppp3.70070 | p. 259 | Supported |
| license | CC BY 4.0 | Creative Commons Attribution License, no version (p. 259) | Imprecise (low) |
| data | survey data on CIMMYT Dataverse, https://data.cimmyt.org/ (no personally identifiable information) | Data availability (p. 272). No dataset DOI and no code location given | Supported |
| crops | maize | Throughout | Supported |
| region | Zimbabwe (five provinces) | p. 261 | Supported |
| gist | Typology of 2,040 farms, hosts matched farm types, women and men each form several types | p. 260, 267, 270 (Table 6). Accurate. "Several" for two women-associated types is loose. Optional tighter gist (27 words): "A typology of 2,040 surveyed Zimbabwean maize farms showed extension-selected trial hosts matched the population's farm types, and that women-headed households fall into two very different types" | Supported |
| not_established | three items | All three are fair. Misses the no-control-group stretch (see fix 10) | Supported (incomplete) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Frontmatter | title | Supported | p. 259 | Expected colon to period change |
| 2 | Frontmatter | authors | Imprecise | p. 259, 276 | Order wrong (fix 8) |
| 3 | Frontmatter | year 2025 | Supported | p. 259, 276 | Online 2025, issue 2026 |
| 4 | Frontmatter | journal | Supported | p. 259 | |
| 5 | Frontmatter | article 8(1), 259-276 | Supported | p. 259, 276 | |
| 6 | Frontmatter | type research article | Supported | p. 259 | |
| 7 | Frontmatter | doi | Supported | p. 259 | |
| 8 | Frontmatter | license CC BY 4.0 | Imprecise | p. 259 | Version not stated (fix 13) |
| 9 | Frontmatter | data on CIMMYT Dataverse | Supported | p. 272 | |
| 10 | Frontmatter | crops maize | Supported | throughout | |
| 11 | Frontmatter | region, five provinces | Supported | p. 261 | |
| 12 | Frontmatter | gist | Supported | p. 260, 267, 270 | Optional tightening |
| 13 | Frontmatter | not_established | Supported | p. 271 | Incomplete (fix 10) |
| 14 | Summary | Testing predicts only if hosts represent TPE, hosts often more prosperous | Imprecise | p. 261, 269 | Source says "can be" (fix 5) |
| 15 | Summary | Cairns, Baudron and colleagues at CIMMYT, CIRAD, Rothamsted checked ex post and piloted typology | Supported | p. 259, 260, 261 | Primary and secondary aims |
| 16 | Summary | 18 random districts, five provinces, mostly NR 3 and 4, 2,346 farms from registries, proportional to ward population | Supported | p. 261 to 262 | Provinces were chosen on biophysical criteria, wards by population and DAEO guidance |
| 17 | Summary | 2021 survey content | Supported | p. 262 | |
| 18 | Summary | 17 variables, 2,040 farms, random forest for discriminating variables | Supported | p. 263 to 264, 267, Figure 5 (PDF p. 10) | Figure 5 shows 17 variables |
| 19 | Summary | Hosts chosen by trained extension agents, part of sample, compared with typology | Supported | p. 261, 264 | |
| 20 | Summary | Five types with legend labels | Imprecise | Figure legends vs Table 4 (p. 268), p. 267, 270 to 271 | Labels contradict the paper's own data (fix 1) |
| 21 | Summary | Hosts distributed like population, off-farm type slightly under-represented | Supported | Table 6 (p. 270), p. 268 to 269 | 13% vs 18% |
| 22 | Summary | No difference in equipment or livestock, almost 20% more maize, partly because more relied on farming | Imprecise | p. 269, Table 2 (p. 265) | Source hedges ("may be related, in part"). Table 2 gives about 30% (fix 4) |
| 23 | Summary | Gender-based targets therefore ensured adequate representation of women | Supported | p. 259, 269 | Matches the authors. Add the no-control-group caveat (fix 2, 3) |
| 24 | Summary | Gender alone hides differences | Supported | p. 269 to 271 | |
| 25 | Summary | Two women-associated types differ, one has more equipment and livestock and almost 3x maize, other less fertilizer and manure, more intercropping | Supported | p. 271, Table 4 | Table 4 gives 2.4x for total production (source issue) |
| 26 | Summary | One women-associated type closer to a men-associated type | Supported | Table 5 (p. 270), p. 268, 271 | 0.24 vs 0.42, ratio 1.75 |
| 27 | Summary | Selecting by sex of head alone misses distinct needs | Supported | p. 271 | Source speaks of priorities, preferences and opportunities |
| 28 | Summary | Recommendations incl. guarding against elite capture, reporting host characteristics | Imprecise | p. 260, 269, 271, 272 | First part supported. Rest reframed (fix 6) |
| 29 | Summary | Hosts under 10%, minimum survey size, key variables will differ | Imprecise | p. 271 | 191/2,346 = 8.1%, 191/2,040 = 9.4%. Source says "likely to change" |
| 30 | Methods | Provinces, districts, wards, 2,346 farms, KoboCollect, Sept to Nov 2021, 10 to 15 agents, IREC 2024.005 | Supported | p. 261 to 262 | |
| 31 | Methods | 17 variables, five types from 2,040, random forest | Supported | p. 263 to 264, 267 | |
| 32 | Methods | 186 hosts compared by type and by gender | Imprecise | p. 264 to 266, 270 | Gender comparisons used 191 (fix 7) |
| 33 | Limitations | Plot manager binary, no joint management, one respondent | Supported | p. 271 | |
| 34 | Limitations | Typologies reduce a continuum to types | Supported | p. 271 | |
| 35 | Limitations | Key variables likely differ across crops and regions | Supported | p. 271 | |
| 36 | Limitations | Not stated: high rainfall areas excluded, plot manager age not recorded | Supported | p. 261, 262 | Correctly labelled as not stated |
| 37 | Key numbers | 2,346 / 2,040 | Supported | p. 261, 264 | |
| 38 | Key numbers | 18 / 5 | Supported | p. 261 | |
| 39 | Key numbers | 17 variables | Supported | p. 263, Figure 5 | Methods text lists 16 (source issue) |
| 40 | Key numbers | 5 farm types | Supported | p. 264, 267 | |
| 41 | Key numbers | 186 hosts (39, 70, 26, 26, 25) | Supported | Table 6 (p. 270) | Sum is 186. Text says 191 (source issue) |
| 42 | Key numbers | 19 / 34 / 15 / 14 / 18% | Supported | Table 6 | Recomputed from 384, 700, 302, 282, 372 of 2,040 |
| 43 | Key numbers | ~20% more maize | Supported | p. 269 | Matches text, not Table 2 (fix 4) |
| 44 | Key numbers | <10% hosts | Supported | p. 271 | |
| 45 | Key numbers | 40 farmers in 2010 to several hundred per pipeline in 2024 | Supported | p. 261 | Attribution correct (40 from Setimela et al. 2017) |
| 46 | Notes | Farm-type labels inconsistent | Supported | Figure legends, Table 4, p. 267, 271 | Can be extended (fix 12) |
| 47 | Notes | Hosts are in researcher-designed network, not tricot trials | Not in source | p. 261, 264 | Paper does not describe trial design (fix 9) |
| 48 | Notes | Cites Laajaj 2020 on host-farmer selection bias | Supported | p. 260, 269 | Kool 2020 and Voss 2021 and Voss, Cairns et al. 2023 are also cited in the paper |
| 49 | Relations | Nanyonjo 2024: hosts selected by weighting on gender and other factors in Uganda | Supported | p. 271 | Gender, age and market orientation, cassava |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Farm-type labels in figure legends and Table 5 and 6 captions contradict Table 4 and the text | Figures 1, 4, 6, 7, Tables 5, 6 vs Table 4 (p. 262 to 270) | Yes in Notes, but the Summary repeats the wrong labels | See fix 12 |
| 191 hosts in the text and Tables 2 and 3, but Table 6 sums to 186. Also 1,846 + 191 = 2,037, not 2,040 | p. 264, 265, 266, 270 | No | See fix 12 |
| Host maize production "almost 20%" higher in the text, but Table 2 means give about 30% (2,742.9 vs 2,103.2 kg). The text gives 2,105.5 kg for the population, which is Table 2's previous-year value | p. 264, 265, 269 | No | See fix 12 |
| Table 2 statistics look copied: the previous-year maize row repeats the maize area row (p 0.579, F 0.308), and maize production has F 0.579 with p 0.007. Cattle means are swapped between text (5.3 population, 5.1 hosts) and Table 2 | p. 264 to 265 | No | Low importance, optional |
| Type 3 "almost three times" more maize than type 4 fits previous-year values (3.1x) better than total production (2.4x) | p. 271, Table 4 | No | See fix 12 |
| Intercropping 59% (type 3) and over 91% (type 4), and manure 83% (type 3), in the text vs 36%, 51% and 81% in Table 4 | p. 267, Table 4 | No | See fix 12 |
| Maize production over "past two years" (p. 262, 264) vs "past three years" in the variable list (p. 264). The methods list gives 16 variables, Figure 5 shows 17 (adds previous-season production) | p. 262, 264, Figure 5 | No | Low, optional |
| Table 1 farms sum to 2,344, text says 2,346 | p. 261, Table 1 (p. 263) | No | Low, optional |
| Natural region 5 rainfall given as "<50 mm per annum", clearly a typo | p. 261 | No | Not needed |
| Methods describe hierarchical clustering only, results say "hierarchical clustering and k-means" | p. 264, 267 | No | Not needed |
| "Almost 70% of trials were hosted by men-headed households (Table 5)". Table 5 is the distance matrix. The figure matches Table 3 (131 of 191 = 69%) | p. 269 | No | Not needed |
| Conclusion says the check "confirmed minimal elite capture and unconscious bias", which is stronger than the design allows given the authors' own no-control-group limitation | p. 271, 272 | No | Covered by fixes 2, 3, 10 |
| Reviewer's outside knowledge, not from the source: Table 1 groups Murehwa under Mashonaland West and Chikomba under Midlands, but both districts are in Mashonaland East. Also, ethics approval IREC 2024.005 is coded 2024 for a 2021 survey, and the paper does not explain the timing | Table 1 (p. 263), p. 262, 272 | No | Not needed in the card. Check before mentioning |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: ex-post check of host representativeness, pilot typology for recruitment | Yes | high | |
| Design: random survey of 2,346 farms, 18 districts, 17 variables, typology of 2,040 | Yes | high | |
| No control group, so the benefit of training cannot be quantified (authors' limitation) | No | high | Fix 2, 3, 10 |
| Women-headed share 31.7% vs 32.5%, women plot managers 27.5% vs 32.5% | No | high | Fix 2, 11 |
| Most discriminating variables: equipment value, sex of head, cattle, total maize production | No | high (tells tricot users what to collect) | Fix 2 |
| Ex-ante use: recruit by farm-type proportions, add hosts from types 3 and 4, plot-manager gender targets within types | No | high | Fix 2 |
| Typology method: Hassall et al. 2023, Gower and simple matching distances, binary variables down-weighted by a factor of four, PCoA with six dimensions, complete-linkage clustering | Partly (random forest only) | medium | Add to Methods: "Typology built with the Hassall et al. (2023) method: mixed distances, binary variables down-weighted by a factor of four, principal coordinates (six dimensions) and complete-linkage hierarchical clustering." |
| Gender gap effect sizes among hosts (41%, 55%, 47%, 57% smaller maize area) and within-group overlap (37%, 20%) | No | medium | Fix 11 |
| Other host differences: more manure (71% vs 57%), intercropping (41% vs 32%), farming as main income (73% vs 63.5%) | No | medium | Optional Key numbers row |
| Hosts chosen by extension agents with no CIMMYT input, stage 5 trials of one pipeline, survey the year after selection | Partly | medium | Fix 2, 7 |
| Surveys may need repeating every year or two | No | medium | Fix 2 |
| Local intermediaries may exclude groups elsewhere | No | medium | Fix 3 |
| Subjective down-weighting and typology bias | No | medium | Fix 3 |
| Men plot-manager share higher than earlier research | No | low | Fix 3 |
| Wealth proxies may help define maize market segments | No | low | Optional Notes line |
| Type 5 profile: younger heads, 92% above primary education, 20% rely on farming for income | No | low | Optional |
| Minimum survey size open question, key variables vary by crop and region | Yes | medium | |

## Template compliance

- Summary word count: 383. Below the 400 to 500 target. The replacement in fix 2 has 481 words.
- Gist: 29 words. Under 30, but only just. The optional gist has 27 words.
- Keywords: 11. Within 8 to 12.
- Questions: 5. Within 4 to 7. The question on survey size is fine as long as answers say the paper leaves it open.
- House style: tricot and maniva are lowercase throughout. No capitalised forms found.
- Long-format sections are all present.
