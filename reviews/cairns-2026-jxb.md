# Card review: cairns-2026-jxb

- **Card:** papers/cairns-2026-jxb.md
- **Source:** papers-pdf/cairns-et-al-2026.pdf (15 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 62 |
| Supported | 49 |
| Imprecise | 13 |
| Not in source | 0 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 5 |
| Important omissions | 7 (1 high, 6 medium) |
| Metadata issues | 4 |

The card is accurate on numbers. All 20 Key numbers rows match the source, and attribution to cited papers is correct, with two rows missing a co-cited source. The main problems are tone and status. The gist and the first summary sentence are more certain than the review, several summary sentences turn "can", "may" or "potential" into fact, and the card does not say that early-stage on-farm sparse testing is still being piloted (p. 8). The most important fix is to add a not_established field and soften the gist and opening sentence.

## Fixes needed

1. **Add not_established (missing).** The template asks for it, and this review is easy to stretch. Suggested field:

   `not_established: that on-farm testing, tricot or sparse testing by themselves deliver breakthrough products (the review argues they can support the transition, it reports no breakthrough product from them); that early-stage genomic on-farm sparse testing is proven (it is being piloted in maize, sorghum and common bean); that tricot has involved over 150,000 farmers (the cited source, de Sousa et al. 2024, reports about 150,000 farmer-managed plots); that a minimum variable set for farm typologies is known (the authors say it still needs to be found); that satellite phenotyping is ready for routine on-farm use (the authors list resolution, calibration and cost barriers); that the Zimbabwe survey numbers are new data from this review (they come from Cairns et al. 2026 in Plants, People, Planet, card cairns-2025-ppp)`

2. **Gist is more certain than the source.** Card: sampling, sparse testing and cheaper phenotyping "let maize breeding in SSA deliver breakthrough products". Source: these advances "facilitate scaling of on-farm testing" (p. 1) and on-farm testing "can play a valuable role" (p. 1). Replace with:

   `gist: Review arguing that inclusive host-farmer sampling, sparse testing and cheaper phenotyping can help scale on-farm testing so maize breeding in SSA can move toward breakthrough products`

   (26 words.)

3. **Summary wording is too certain in several places, and it misses the pilot status of early-stage testing.** Details are in the claim table (rows 14, 15, 16, 19, 21, 23, 25, 30). Below is a full replacement summary of 499 words that fixes all of them, adds the pilot status (p. 8) and CGIAR Breeding for Tomorrow (pp. 5, 10), and hedges the 150,000 figure. Paste as is:

   > The review argues that on-farm testing can help public breeding programmes in sub-Saharan Africa move toward breakthrough products, defined as varieties with at least 25% higher productivity or value in farmers' fields. Climate change is accelerating shifts in the maize target population of environments (TPE), and drought and heat now co-occur more often, so managed-stress screening needs refining to keep sampling the TPE. Smallholder management is also highly diverse and hard to represent in managed selection environments, which is likely to reduce realized genetic gain.
   >
   > The authors build on CIMMYT's own history. Managed drought screening produced more than 450 drought-tolerant varieties and measurable genetic gain, but it was designed for a TPE that is now changing. The US AQUAMax hybrids are cited as breakthrough products built with aligned managed environments, extensive on-farm testing and genomic prediction. Participatory breeding has a strong adoption record, yet path dependency, cost and breeders' reluctance kept it project-based rather than institutional. CGIAR Breeding for Tomorrow is moving to institutionalize late-stage on-farm testing.
   >
   > The first argument concerns who hosts trials. Technicians, extension agents or community members often nominate host farmers, which can over-represent wealthier, better-educated farmers and under-represent women, and breeding papers rarely report how hosts were selected. The authors propose farm typologies as a sampling frame. A survey of randomly sampled farmers across the TPE feeds a typology, and host farmers are drawn by stratified sampling across region and farm type, proportionally or with oversampling of under-represented groups of interest. Within households, targets should cover women, men and jointly managed plots, with both spouses in the consent process to avoid tension. Random forest analysis can pick the variables that best separate farm types, and AI may help focus surveys on what matters for breeding.
   >
   > The second argument concerns trial design. Sparse testing evaluates only a subset of candidates per farm, so programmes cover far more of the TPE on the same budget and include land-poor farmers. At late stages, tricot drives most of this expansion, raising maize testing from fewer than 20 to almost 300 farms per pipeline and, by the review's count, reaching over 150,000 farmers across crops. At early stages, genomic relationship matrices link unreplicated genotypes across farms, a logic borrowed from animal breeding, so performance can be predicted across the whole TPE. This is being piloted in maize, sorghum and common bean. Trade-offs remain. Farmers see only part of the diversity, and researchers learn less about the reasons behind preferences.
   >
   > The third argument concerns phenotyping, a bottleneck because cost per data point limits the scale of on-farm testing. Researcher-led yield measurement is expensive, mostly because of travel. Trained farmers and extension agents using simple volumetric measures produce accurate yields, and smartphone images support disease and yield-component scoring. Very-high-resolution satellites offer scale but face mixed pixels, calibration problems and licensing costs that call for joint CGIAR-NARES acquisition. The paper closes by noting that on-farm networks can also capture genotype-by-management interactions, especially nitrogen response, and could support fertilizer recommendations that track volatile prices.

   If the curator prefers smaller edits, the key sentence changes are:
   - Sentence 1: replace "cannot deliver breakthrough products ... without moving more selection onto farms" with "on-farm testing can help ... move toward breakthrough products" (p. 1 says "can play a valuable role", p. 4 says moving selection on farm "could help").
   - AQUAMax: the source says they "provide a concrete example" and lists four components, including environment-type delineation and genomic prediction (p. 4). "Show that pairing ... yields breakthrough products" is a causal claim the source does not make.
   - Oversampling is an option for programmes that want to study specific under-represented groups. The default is proportional sampling (p. 7).
   - Random forest picks the variables that best separate farm types. Picking the variables that matter for breeding is a "potential" of AI (p. 7).
   - Phenotyping is "a bottleneck" (p. 5), not "the main bottleneck".

4. **Link the Zimbabwe survey to its card.** The review's "Cairns et al. 2026" is the Plants, People, Planet paper "Know your men and women farmers" (reference list, p. 12), which is in the repo as cairns-2025-ppp (2026 issue, online 2025). The card treats the survey as the review's own evidence in Methods. Replace the Methods bullet with:

   `- **Evidence.** Published trials and reviews, plus Zimbabwe survey data on maize management from about 2,000 farmers, cited from Cairns et al. 2026 (card cairns-2025-ppp) and shown in Fig. 1.`

   Add to relations:

   `  - citesAsDataSource: cairns-2025-ppp  # Zimbabwe survey (Fig. 1), cited in the review as Cairns et al. 2026`

   In Key numbers, change "Cairns et al. 2026" in the four Zimbabwe rows to `Cairns et al. 2026, Plants People Planet (cairns-2025-ppp)`.

5. **Two Key numbers rows miss a co-cited source.**
   - Row "~8 M ha, 9.7 M households": source cites Cairns and Prasanna 2018, Chivasa et al. 2022 and Boddupalli 2024 (p. 3). Replace the last cell with `Cairns and Prasanna 2018, Chivasa et al. 2022, Boddupalli 2024`.
   - Row "<20 → ~300 farms": source cites Setimela et al. 2012, 2017 and Worku et al. 2020 for fewer than 20, and Prasanna et al. 2022 and Boddupalli 2024 for almost 300 (pp. 7 to 8). Replace the last cell with `<20: Setimela et al. 2012, 2017 and Worku et al. 2020. ~300: Prasanna et al. 2022 and Boddupalli 2024`.

6. **License.** The PDF links to the CC BY 4.0 licence (p. 1). Replace with `license: CC BY 4.0`.

7. **Add Notes for source issues not yet flagged** (see Source issues table). Suggested text:

   `- The text cites Fig. 1D, 1E and 1F for the 41%, 37% and 25% intercropping rates of women-, jointly- and men-managed plots (p. 3). These rates are in Fig. 1C. Panels D to F show intercropping species, and the caption assigns D to male, E to women and F to jointly managed plots (p. 4).`

   `- The review gives the Zimbabwe survey as 2000 farmers in the text and "almost 2000" in the Fig. 1 caption. Card cairns-2025-ppp reports 2,346 farms sampled and 2,040 in the typology.`

8. **Optional, low priority.** Add `article: erag431 (advance access 4 September 2026, pp. 1-15)` since no volume exists yet. Consider adding relations to tricot cards the review cites as examples (pp. 6, 8): vanetten-2019-pnas, voss-2021-outlook, nanyonjo-2024-cropsci, kadege-2026-fsufs, daudi-2026-fes, voss-2025-ppp, kang-2025-expagric, sharma-2025-jafr. The curator should confirm each card matches the cited reference before adding.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Advancing inclusive on-farm testing approaches to facilitate maize breakthrough product development in sub-Saharan Africa | Same (p. 1) | Supported |
| authors | Cairns JE, Fisher M, Pinto F, de Sousa K, van Etten J, Zaman-Allah M, Daudi H, Nas TM, Werner CR | Jill E. Cairns ... Christian R. Werner, same order (p. 1) | Supported |
| year | 2026 | Advance Access 4 September 2026 (p. 1) | Supported |
| journal | Journal of Experimental Botany | Same (p. 1) | Supported |
| article | erag431 | DOI suffix erag431, Vol. 00 No. 0 pp. 1–15 (p. 1) | Supported (optional detail in Fix 8) |
| type | review | "REVIEW PAPER" (p. 1) | Supported |
| doi | https://doi.org/10.1093/jxb/erag431 | Same (p. 1) | Supported |
| license | CC BY | Creative Commons Attribution, link to licenses/by/4.0 (p. 1) | Imprecise (should be CC BY 4.0) |
| data | none (review) | No data availability statement. Fig. 1 data come from the cited Cairns et al. 2026 survey (pp. 3 to 4) | Supported |
| crops | maize, examples from cassava, common bean, groundnut, amaranth, potato, yam, sorghum | Same crops (pp. 5, 8). Also brief mentions of barley and rice (p. 5), cocoa (p. 9), canola (p. 10) | Supported |
| region | SSA (Eastern and Southern Africa, Zimbabwe case data) | pp. 2 to 4. Examples also from Tanzania and Ghana (p. 9) and the USA (p. 4) | Supported |
| funding | UK-CGIAR TEAM-AI | Funding section (p. 11) | Supported |
| gist | ... let maize breeding in SSA deliver breakthrough products | Advances "facilitate scaling of on-farm testing" (p. 1) | Imprecise (too certain, Fix 2) |
| not_established | missing | Several claims easy to stretch (pp. 7, 8, 10) | Missing (Fix 1) |
| relations | citesAsDataSource desousa-2024-asd | Correct. Missing cairns-2025-ppp (p. 12 reference list) | Incomplete (Fix 4) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Front | Title | Supported | p. 1 | |
| 2 | Front | Authors and order | Supported | p. 1 | |
| 3 | Front | Year 2026 | Supported | p. 1 | |
| 4 | Front | Journal | Supported | p. 1 | |
| 5 | Front | Article erag431 | Supported | p. 1 | |
| 6 | Front | Type review | Supported | p. 1 | |
| 7 | Front | DOI | Supported | p. 1 | |
| 8 | Front | License CC BY | Imprecise | p. 1 | Version 4.0 missing |
| 9 | Front | Data none | Supported | whole paper | |
| 10 | Front | Crops | Supported | pp. 5, 8 | |
| 11 | Front | Region | Supported | pp. 2 to 4 | |
| 12 | Front | Funding TEAM-AI | Supported | p. 11 | |
| 13 | Front | Gist | Imprecise | p. 1 | "let ... deliver" overstates "facilitate" |
| 14 | Summary | Programmes "cannot deliver" breakthrough products without moving selection on farm, ≥25% definition | Imprecise | pp. 1, 2, 4 | Definition correct. Source says on-farm testing "can play a valuable role" and "could help", not that it is required |
| 15 | Summary | Climate shifts TPE faster than managed-stress trials can track, drought and heat co-occur more | Imprecise | p. 3 | Co-occurrence supported. "Faster than trials can track" is the card's reading. Source says shifts "have implications for" screening protocols that need refining |
| 16 | Summary | Diverse management, station trials represent TPE poorly, realized gain "suffers" | Imprecise | p. 3 | Source: managed selection environments, and misalignment "likely to reduce" realized gain |
| 17 | Summary | Authors build on CIMMYT history | Supported | pp. 2 to 3 | |
| 18 | Summary | Managed drought screening gave >450 DT varieties and genetic gain, designed for a changing TPE | Supported | p. 3 | The 450 is attributed to CIMMYT and partners' breeding efforts overall |
| 19 | Summary | AQUAMax "show that" managed environments plus on-farm testing "yields" breakthrough products | Imprecise | p. 4 | Source: "concrete example". Omits environment-type delineation and genomic prediction |
| 20 | Summary | PPB strong adoption, path dependency, cost, reluctance kept it project-based | Supported | p. 5 | |
| 21 | Summary | Extension agents or leaders "usually choose" hosts, "skews" to wealthier, better-educated men, papers rarely report selection | Imprecise | pp. 5 to 6 | Source: nomination "can unintentionally introduce bias". Wealth and education evidence is from agronomic research. Reporting gap supported |
| 22 | Summary | Authors propose farm typologies as sampling frame | Supported | p. 6 | Proposed first in Cairns et al. 2026 (cairns-2025-ppp) |
| 23 | Summary | Survey feeds typology, stratified by region and farm type, "deliberate oversampling" | Imprecise | pp. 6 to 7, Fig. 2 | Proportional sampling is the default. Oversampling is an option for groups of interest |
| 24 | Summary | Targets for women, men, joint plots, both spouses in consent | Supported | pp. 6 to 7 | Source hedges ("may help ... reduce potential tensions") |
| 25 | Summary | ML can shrink survey to variables that matter most for breeding | Imprecise | p. 7 | Random forest found variables that separate farm types. Breeding relevance is a stated "potential" |
| 26 | Summary | Sparse testing covers more TPE on same budget, includes land-poor | Supported | p. 7 | |
| 27 | Summary | tricot drives most expansion, <20 to ~300 farms, >150,000 farmers | Supported | pp. 7 to 8, 10 | Matches source. The 150,000 is a source issue, flagged in Notes. Hedge suggested |
| 28 | Summary | GRM links unreplicated genotypes, animal-breeding logic, predict across TPE | Supported | p. 8 | Omits that this is being piloted |
| 29 | Summary | Trade-offs: partial diversity, less insight into reasons | Supported | p. 8 | |
| 30 | Summary | Phenotyping "now the main bottleneck" | Imprecise | pp. 5, 10 | Source: "a bottleneck" |
| 31 | Summary | Researcher yield measurement costly, mostly travel | Supported | pp. 8 to 9 | Fuel the main cost driver |
| 32 | Summary | Trained farmers and extension agents with volumetric measures give accurate yields | Supported | p. 9 | Based on two studies (common bean in Tanzania, maize and cocoa in Ghana) |
| 33 | Summary | Smartphone images for disease and yield components | Supported | p. 9 | |
| 34 | Summary | VHR satellites: mixed pixels, calibration, licensing, joint acquisition | Supported | pp. 9 to 10 | |
| 35 | Summary | Closing: G×M, nitrogen, price-tracking fertilizer recommendations | Supported | pp. 10 to 11 | Source says "could be determined". "Produce" is slightly strong, fixed in the replacement summary |
| 36 | Methods | Narrative review of CGIAR and NARES literature | Supported | whole paper | |
| 37 | Methods | Evidence: Zimbabwe survey of ~2,000 farmers | Imprecise | pp. 3 to 4 | Survey is cited from Cairns et al. 2026, not done for this review |
| 38 | Methods | Proposals list | Supported | pp. 5 to 10 | |
| 39 | Limitations | Typology surveys costly, minimum variable set unknown | Supported | p. 7 | |
| 40 | Limitations | Sparse testing: partial diversity, less insight | Supported | p. 8 | |
| 41 | Limitations | Satellites: mixed pixels, calibration, licensing | Supported | pp. 9 to 10 | |
| 42 | Key numbers | ≥25%, Coaldrake and Werner 2025 | Supported | p. 2 | |
| 43 | Key numbers | ~40% / ~25% drought area, Tesfaye 2016 | Supported | p. 2 | |
| 44 | Key numbers | 10–25% yield loss, Tesfaye 2016 | Supported | p. 2 | |
| 45 | Key numbers | 2× drought and heat, Heino 2023 | Supported | p. 3 | |
| 46 | Key numbers | >450 varieties, Chivasa 2022 | Supported | p. 3 | |
| 47 | Key numbers | ~8 M ha, 9.7 M households | Imprecise | p. 3 | Boddupalli 2024 also cited |
| 48 | Key numbers | 32.5 kg/ha/yr, 2000–2010, Masuka 2017 | Supported | p. 3 | |
| 49 | Key numbers | 45, 64, 54 kg/ha/yr, 2013–2020, Prasanna 2022 | Supported | p. 3 | Early S Africa, early E Africa, intermediate E Africa |
| 50 | Key numbers | >80% yield gap, Aramburu-Merlos 2024 | Supported | p. 3 | |
| 51 | Key numbers | ~2,000 farmers, Zimbabwe | Supported | pp. 3, 4 | Text "2000", caption "almost 2000" |
| 52 | Key numbers | 45.4 kg/ha fertilizer | Supported | p. 3, Fig. 1A | Attribution to the survey is implied by context, not by a citation next to the number |
| 53 | Key numbers | 2.12 weedings (0–5) | Supported | p. 3, Fig. 1B | |
| 54 | Key numbers | 41% / 37% / 25% intercropping | Supported | p. 3, Fig. 1C (approx. read) | Source cites wrong panels (source issue) |
| 55 | Key numbers | 0.49 / 0.9 ha vs 56 / 447 ha, Rapsomanikis 2015 | Supported | p. 7 | |
| 56 | Key numbers | <20 → ~300 farms | Imprecise | pp. 7 to 8 | Worku 2020 and Boddupalli 2024 missing |
| 57 | Key numbers | >150,000 farmers, 12 years, de Sousa 2024 | Supported | p. 10 | Correctly cited as the review states it. Discrepancy flagged in Notes and relation |
| 58 | Key numbers | USD 3,467, 20 locations, Hamadziripi 2025 | Supported | p. 9 | About USD 173 per location (card did not compute this, no fix needed) |
| 59 | Key numbers | >20 questions, This review | Supported | p. 7 | No citation in source, so "This review" is right. Strictly it is the number of questions used to delineate farm types, not total survey length |
| 60 | Key numbers | 8 → 18 kg N/ha, 50 kg Abuja target, Rasche and Vanlauwe 2025 | Supported | p. 10 | |
| 61 | Key numbers | 0.3–0.5 m/pixel, Pinto 2023 | Supported | p. 9 | SkySat, Pelican, WorldView-2 and -3, Pleiades Neo |
| 62 | Notes | Review cites >150,000 farmers, de Sousa 2024 reports ~150,000 plots | Supported | p. 10 | Confirmed in de Sousa et al. 2024 text ("~150,000 farmer-managed plots") |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| ">150,000 farmers" credited to de Sousa et al. 2024, which reports about 150,000 farmer-managed plots | p. 10 | Yes (Notes and relation comment) | None needed |
| Text cites Fig. 1D, 1E, 1F for the 41%, 37%, 25% intercropping rates. These are in Fig. 1C. The letter order in the text (women, joint, men) also does not match the caption (D male, E women, F joint) | pp. 3 to 4 | No | See Fix 7 |
| Survey size given as "2000" in text and "almost 2000" in Fig. 1 caption. The companion paper (card cairns-2025-ppp) gives 2,346 sampled and 2,040 in the typology | pp. 3 to 4 | No | See Fix 7 |
| Endelman et al. 2014 are called "the first to propose" sparse testing in crops, but the same paragraph cites Burgueño et al. 2012 for genomics-based sparse testing | p. 8 | No | Low importance. Optional: `- The review calls Endelman et al. 2014 the first to propose genomic sparse testing in crops, but also cites Burgueño et al. 2012 for the concept (p. 8).` |
| Fig. 1 caption names cucumber as *Cucumis metuliferus*, which is horned melon (cucumber is *C. sativus*), and misspells *Phaseolus* | p. 4 | No | Low importance. No Notes text needed |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: highlight advances in host sampling, sparse testing, phenotyping for on-farm testing | Yes | high | |
| Early-stage on-farm sparse testing is only being piloted (maize, sorghum, common bean) and complements on-station testing | No | high | In replacement summary and not_established (Fixes 1, 3) |
| CGIAR Breeding for Tomorrow moving to institutionalize late-stage on-farm testing, donor mandates | No | medium | In replacement summary (Fix 3) |
| How tricot works: block of three, ranking of agronomic, end-user and overall performance, aggregation, can include quantitative data | No | medium | Methods bullet: `- **tricot as described.** Incomplete blocks of three, farmers rank agronomic, end-user and overall performance, rankings aggregated across hundreds of farms, quantitative data can be added (p. 8).` |
| Report host-farmer characteristics and train recruiters to reduce bias (Fig. 2E) | No | medium | Add to Stated limitations or Methods: `- Recruiters should be trained on the aims of on-farm testing, and host-farmer characteristics should be reported to support replication (pp. 5, 6).` |
| Early-stage on-farm testing does not directly involve farmers in selection decisions, a key success factor of PPB | No | medium | Stated limitations: `- Early-stage genomic sparse testing evaluates traits on farm but does not involve farmers in selecting early candidates (p. 10).` |
| Phenotyping must align with target product profile traits | No | medium | Stated limitations: `- Satellite and digital phenotyping is useful only if the estimated traits match target product profile requirements (p. 10).` |
| Late-stage on-farm testing benefits: external validity, G×E×M, trait trade-offs, "spoiler criteria" for dis-adoption | Partly | medium | Optional sentence in Methods: `- Late-stage on-farm testing adds external validity and can reveal trait trade-offs and "spoiler criteria" that drive dis-adoption (p. 7).` |
| Women in men-headed households were neglected, women-managed plots get fewer inputs | Partly (targets only) | low | Optional |
| Sparse testing could be seen as undermining farmer agency (Oberson et al. 2024) | No | low | Optional |
| Satellite cost detail: several hundred USD per image, ~25 km² SkySat scene | No | low | Optional Key numbers row |
| Bean disease from phone images more accurate than hand scoring, stand and pod count tools in ~500 fields | No | low | Optional |
| TPE history, managed drought protocol, livelihood benefits of DT maize | Partly | low | None needed |
| Generative AI used for language editing (Acknowledgements) | No | low | Optional Notes line |

## Template compliance

- Summary word count: 435 (target 400 to 500). Pass. The replacement summary in Fix 3 is 499 words.
- Gist length: 19 words (under 30). Pass. The replacement gist is 26 words.
- Keywords: 11 (8 to 12). Pass.
- Questions: 4 (4 to 7). Pass. Optional fifth question: `- Is early-stage on-farm sparse testing ready to use?`
- House style: tricot lowercase throughout. Pass. maniva not used.
- not_established: missing. Fail (Fix 1).
- No em dashes or semicolons in card prose. Pass.
