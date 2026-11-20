# Card review: mulatu-2024-slides

- **Card:** papers/mulatu-2024-slides.md
- **Source:** papers-pdf/mulatu-et-al-2024.pdf (14 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 42 |
| Supported | 29 |
| Imprecise | 11 |
| Not in source | 2 |
| Contradicted | 0 |
| Important omissions | 7 |
| Metadata issues | 3 |

The card describes the background, sites, design and analysis methods correctly, and nothing in it contradicts the slides. But it reports none of the results. The biomass chart (slide 10), the Kendall correlations (slide 11) and the Plackett-Luce heatmap (slide 12) are named but not read, so the card cannot answer two of its own questions. The summary is also below the 400-word target (337 words). The most important fix is to replace summary paragraph 4 with the actual findings (Fix 1).

All slides were read visually, and the three result charts were enlarged to read values. Values marked "about" are read from bar or box positions. They are not printed on the slides.

## Fixes needed

1. **Summary reports no results (high).** The card says Kendall correlations "showed which traits were most linked" and log-worth "highlighted the best options", but never says which. The slides show the following:
   - Slide 10 (biomass): in Amhara only the four-way mixture Mombasa & Mulato II & Desmodium & Vetch is above 0.5 (about 0.57). In SNNP seven options are above 0.5: vetch and Mulato II (about 0.61 each), Mombasa & Vetch, the same four-way mixture, Mombasa & Lablab, Mombasa & Desmodium and Mombasa alone. Vetch and Mulato II are among the weakest in Amhara. No uncertainty intervals are drawn.
   - Slide 11 (Kendall): three traits are boxed in red. Ease of harvesting at the 2nd harvest is about 0.32 (Amhara), 0.39 (all) and 0.46 (SNNP). Transplanting at the 1st harvest is about 0.45 (Amhara), 0.38 (all) and 0.30 (SNNP). Ease of harvesting at the 1st harvest is about 0.19 to 0.25. Yield is 0.12 or lower in every group.
   - Slide 12 (log-worth, pooled data): red boxes mark Desho and the four-way mixture. Desho is darkest green for disease, pest and drought resistance and grass population. The mixture is green for yield, soil cover, plant population and co-benefits but brown for ease of harvesting.

   Replace the whole Summary with the text below. It fixes Fixes 1, 3, 4, 5, 6 and 7 at once and is 496 words (wc), inside the 400 to 500 target.

   ```
   Livestock support the livelihoods of about 70% of Ethiopia's population, but about 90% of feed comes from traditional grazing, mostly on poorly managed natural pastures. Land degradation is mainly linked to the livestock sector, through overgrazing and unsustainable farming practices. Improved forages can provide better feed and help restore land, and farmers' participation in choosing them is key to adoption. The team therefore used tricot to identify how forage mixtures perform and which traits farmers prefer.

   Sites were chosen in mid-altitude mixed farming systems across agroecologies with dairy potential, forage scarcity and earlier experience promoting improved forages. A map shows eight tricot woredas, and field photos show Dangla and Dera in Amhara and Bilate in Sidama. Woreda development agents were trained, and package labels are dated 2022. Each farmer received three separate options, drawn from 21 grasses, legumes and grass-legume mixtures. The grasses were Mombasa, Mulato II, Cayman and Desho, and the legumes were vetch, stylo, lablab, desmodium and crotalaria.

   Farmers answered best and worst questions for 19 traits plus overall preference. These covered establishment (ease of sowing), plant height, soil cover, plant, grass and legume populations, weeds, greenness, disease, pest and drought resistance, leaf-to-stem ratio, fertilizer needs, soil retention, soil fertility improvement, yield, ease of harvesting, livestock preference and ease of transplanting. The results slides show 17 of these traits, at the first and second harvest.

   Biomass (yield) results are shown separately for Amhara (n = 383) and SNNP (n = 354), as the probability of each option outperforming the reference forage Desho. The slides do not say whether n counts farmers and whether biomass was measured or ranked. In Amhara, only the four-way mixture of Mombasa, Mulato II, desmodium and vetch was above 0.5 (about 0.57). In SNNP, seven options were above 0.5, led by vetch and Mulato II (about 0.6 each), then Mombasa alone and four mixtures that contain Mombasa, including the same four-way mixture. Vetch and Mulato II were among the weakest options in Amhara. The chart shows no uncertainty intervals. Kendall correlations with overall preference were highest for ease of harvesting at the second harvest (about 0.3 to 0.5) and ease of transplanting at the first harvest (about 0.3 to 0.45). Yield was only weakly linked (about 0.1 or less). Plackett-Luce log-worth estimates on the pooled data highlighted Desho and the four-way mixture. Desho scored well on disease, pest and drought resistance, while the mixture scored well on yield and soil cover but poorly on ease of harvesting.

   The lessons point to scaling mixtures to similar suitable environments, and to the value of engaging farmers in technology selection for new insights and easier scaling. The final slide also lists the influence of familiar varieties on preferences, and the role of biophysical and socio-economic factors and of different niches in performance and preference. Next steps include studying the environmental and socio-economic impacts of replacing the traditional feed basket with improved forages. Availability of forage seed and extension services are key enabling factors.
   ```

2. **Gist overstates the Desho comparison and gives no finding (high).** The card says options were compared "with the local reference Desho across many farmer-assessed traits". The comparison with Desho is shown only for biomass (slide 10). The many-trait view (slide 12) compares all 21 options, not each one against Desho. "Local" is not in the slides. "About 740 farmers" adds 383 and 354 (sum 737, rounding is fine), but the slides do not say n counts farmers. The template asks what the paper shows. Replace with (29 words):

   ```
   gist: Slides on tricot trials of 21 forages in Ethiopia: one mixture outscored Desho for biomass in Amhara, seven options in SNNP, and preference tracked ease of harvest and transplanting
   ```

3. **Sample size unit (medium).** Summary, gist and Key numbers say "383 farmers" and "354 farmers". Slide 10 only shows "Amhara, n = 383" and "SNNP, n = 354". Slide 7 shows a design table with 14 options at 76 to 78 allocations each (1,080 slots, so 360 packages of three). Neither number is labelled as farmers. Replace the Key numbers row with:

   ```
   | n = 383 / n = 354 | Sample size in the Amhara / SNNP biomass charts (unit not stated on the slide) | This presentation |
   ```

4. **Kendall wording (medium).** The card says traits were linked to overall preference "at each harvest". Slide 11 correlates one variable called "Overall Preference" with traits from both harvests, split by All, Amhara and SNNP. The new summary in Fix 1 handles this.

5. **Role of development agents (low).** Summary says agents were "trained to run the trials", and Methods says trials were "run by trained woreda development agents". Slide 6 only says "Training of woreda development agents". Their role is not stated. Fixed in Fix 1 and Fix 8.

6. **Trait list (low).** "Establishment and ease of sowing" reads as two traits. Slide 9 has one trait, Establishment, asked as "Which option was easier to sow?". Fixed in Fix 1.

7. **Aim and background wording (low).** Slide 3 gives the aim as "Identifying performance of mixtures and preferred traits by farmers". The card says "identify farmer-preferred multipurpose forage options". Slide 2 links land degradation to overgrazing and "unsustainable agricultural practices", which the card drops. "Options suit different niches" reads a finding into the bare bullet "Performance and preference in different niches" (slide 13). Fixed in Fix 1.

8. **Methods bullets (medium).** "About 20 traits" is close but not exact. Slide 9 lists 20 rows: 19 traits plus overall preference. The results slides show only 17 traits per harvest (establishment and soil fertility improvement are absent). Replace the four Methods bullets with:

   ```
   - **Sites.** Mid-altitude mixed farming systems with dairy potential and forage scarcity, in eight woredas of Amhara and SNNP/Sidama.
   - **Design.** tricot packages of three separate options, drawn from 21 grasses, legumes and grass-legume mixtures. Woreda development agents were trained. Package labels are dated 2022.
   - **Evaluation.** Best-worst questions for 19 traits plus overall preference. The results show 17 traits at the first and second harvest.
   - **Analysis.** Probability of outperforming Desho for biomass, by region. Kendall correlation of each trait with overall preference, by region and pooled. Plackett-Luce log-worth by trait on the pooled data.
   ```

9. **Stated limitations contains a curator caveat (medium).** "Slides present results without full statistics..." is not said by the authors. It is a fair caveat, but the section is for the authors' own words. Replace the Stated limitations section with:

   ```
   - Familiar, well-known varieties influence farmers' preferences (listed under lessons and next steps).
   - Biophysical and socio-economic factors affect both performance and preference (listed under lessons and next steps).
   ```

   and add the caveat to Notes (Fix 11).

10. **not_established is missing (medium).** Slides are easy to stretch. Add this field. Semicolons are used here only because the template requires them as separators.

    ```
    not_established: That any option significantly outyields Desho, as no uncertainty is shown for biomass; measured biomass, forage quality or animal performance; that yield is what farmers value most; performance outside the tested woredas or seasons
    ```

11. **Notes and Key numbers are missing useful facts (medium).** Add these Notes bullets:

    ```
    - Slides only. The biomass chart shows no uncertainty intervals and does not define n. Look for a peer-reviewed paper before citing findings.
    - The design table on slide 7 lists 14 options at 76 to 78 allocations each (about 360 packages). The results slides show 21 options. The slides do not explain the difference.
    - Slide 11 plots "2nd Harvest Overall" as a trait with near-zero correlation with "Overall Preference", so the reference overall variable is not defined.
    - Slide 9 uses "contribute less" in both the best and the worst soil fertility question, probably a typo. Establishment and soil fertility improvement do not appear in the results.
    - Values marked "about" were read from the charts on slides 10 and 11.
    ```

    Add these Key numbers rows:

    ```
    | 21 | Options in the results: 4 grasses, 5 legumes, 12 mixtures | This presentation |
    | about 0.57 | Probability that Mombasa & Mulato II & Desmodium & Vetch outperforms Desho for biomass in Amhara, the only option above 0.5 (read from chart) | This presentation |
    | 7 | Options above 0.5 probability of outperforming Desho for biomass in SNNP | This presentation |
    | about 0.32 to 0.46 | Kendall correlation of 2nd-harvest ease of harvesting with overall preference, by region (read from chart) | This presentation |
    | 0.12 or less | Kendall correlation of yield with overall preference, all groups and harvests (read from chart) | This presentation |
    ```

12. **Software field (low).** The slides say "Plackett-Luce estimates" (slide 12) but never name the R package PlackettLuce. ClimMob is visible on slides 4, 6 and 7. Suggested:

    ```
    software: ClimMob, Plackett-Luce model (R package not named in the slides)
    ```

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Unlocking farmer-preferred multipurpose forage mixtures. A tricot approach in Ethiopia | Same words with a colon (p1) | Supported (period instead of colon matches house style, as in jorgensen-2026-gse) |
| authors | Mulatu K, de Sousa K, Ebrahim M, Notenbaert A, Abera W, Mwendia S, Girma E, Jørgensen M | Same eight names, same order (p1) | Supported |
| year | 2024 | September-12-2024 (p1) | Supported |
| journal | Presentation, Tropentag conference, 12 September 2024 | Tropentag conference, September-12-2024 (p1) | Supported |
| article | conference slides | Slide deck | Supported |
| type | presentation | Slide deck | Supported |
| source | team | de Sousa and Jørgensen are in people.md | Supported |
| peer_reviewed | no | Conference slides | Supported |
| doi | https://hdl.handle.net/10568/163542 | Not printed in the PDF. Same handle in papers-pdf/LICENSES.md. The handle did not resolve from this session | Not checkable from source |
| license | see repository record | No license on any slide. LICENSES.md says none stated | Supported (template wording is "see CGSpace record") |
| data | none | No dataset link on any slide | Supported |
| software | ClimMob, PlackettLuce | ClimMob (p4, p6, p7). Method named, R package not named (p12) | Imprecise (Fix 12) |
| crops | four grasses, five legumes, and mixtures | All named on p10 and p12 | Supported (grass and legume classes are general knowledge, not stated on slides) |
| region | Ethiopia (Amhara and SNNP/Sidama) | Amhara and SNNP (p10), Sidama (p8), eight woredas (p5) | Supported |
| gist | about 740 farmers, compared with local reference Desho across many traits | Desho comparison for biomass only (p10). n unit not stated. "Local" not in source | Imprecise (Fix 2) |
| not_established | Missing | Not applicable | Missing (Fix 10) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | About 70% of population rely on livestock | Supported | p2 | Slide gives no primary source |
| 2 | Summary | About 90% of feed from traditional grazing, mostly poor natural pasture | Supported | p2 | |
| 3 | Summary | Overgrazing makes livestock a main driver of land degradation | Imprecise | p2 | Slide also names unsustainable agricultural practices |
| 4 | Summary | Improved forages give better feed and help restore land | Supported | p3 | |
| 5 | Summary | Farmer participation is key to adoption | Supported | p3 | |
| 6 | Summary | Aim was to identify farmer-preferred multipurpose forage options | Imprecise | p1, p3 | Slide 3 aim is performance of mixtures and preferred traits |
| 7 | Summary | Site criteria: mid altitude, mixed farming, agroecology, dairy, scarcity, prior experience | Supported | p5, p6 | Slide 6 also lists forage production potential |
| 8 | Summary | Sites include Dangla, Dera (Amhara) and Bilate (Sidama) | Supported | p8 | Map on p5 shows eight woredas. Map spells "Dangila" |
| 9 | Summary | Development agents trained to run the trials | Imprecise | p6 | Only "Training of woreda development agents". Role not stated |
| 10 | Summary | Package of three separate treatments from grasses, legumes, mixtures | Supported | p6, p7, p10 | Photo label shows Crotalaria, Cayman & Lablab, Desho |
| 11 | Summary | Grasses Mombasa, Mulato II, Cayman, Desho, legumes vetch, stylo, lablab, desmodium, crotalaria, and combinations | Supported | p10, p12 | 21 options in total, not stated in card |
| 12 | Summary | Best and worst questions at first and second harvest | Supported | p9, p11, p12 | |
| 13 | Summary | List of traits assessed | Imprecise | p9 | "Establishment and ease of sowing" is one trait. Two traits absent from results |
| 14 | Summary | Biomass analysed for Amhara (383 farmers) and SNNP (354 farmers) as probability of beating Desho | Imprecise | p10 | n unit not stated. Slide title is "Biomass (yield)". Measurement method not stated |
| 15 | Summary | Kendall correlations showed traits linked to overall preference at each harvest | Imprecise | p11 | One overall variable, traits from both harvests, by region. Result not reported |
| 16 | Summary | Log-worth by trait highlighted the best options | Supported | p12 | Accurate but the options are not named (omission) |
| 17 | Summary | Scale mixtures to similar suitable environments | Supported | p13 | |
| 18 | Summary | Engaging farmers gives new insights and easier scaling | Supported | p13 | |
| 19 | Summary | Familiarity with existing varieties influences preferences | Supported | p13 | Bare bullet, may be a topic rather than a finding |
| 20 | Summary | Biophysical and socio-economic factors shape performance and preference | Supported | p13 | Same caveat as 19 |
| 21 | Summary | Options suit different niches | Imprecise | p13 | Slide says only "Performance and preference in different niches" |
| 22 | Summary | Next step: impacts of replacing traditional feed basket | Supported | p13 | Split into lessons and next steps is the card's reading |
| 23 | Summary | Seed availability and extension are key enabling factors | Supported | p13 | |
| 24 | Methods | Sites: mid-altitude mixed farming, Amhara and SNNP/Sidama, potential and scarcity | Supported | p5, p6, p8, p10 | |
| 25 | Methods | Packages of three options, run by trained agents | Imprecise | p6 | Same issue as 9 |
| 26 | Methods | Best-worst rankings for about 20 traits at both harvests | Imprecise | p9, p11, p12 | Exactly 19 traits plus overall on p9. 17 traits per harvest in results |
| 27 | Methods | Plackett-Luce, probability of beating Desho, Kendall with overall | Supported | p10, p11, p12 | |
| 28 | Limitations | Preferences influenced by familiarity with existing varieties | Supported | p13 | |
| 29 | Limitations | Slides lack full statistics, look for a paper | Not in source | none | Curator caveat, not the authors'. Move to Notes |
| 30 | Key numbers | 70% | Supported | p2 | |
| 31 | Key numbers | 90% | Supported | p2 | |
| 32 | Key numbers | 383 / 354 farmers | Imprecise | p10 | Unit not stated. Arithmetic in gist: 383 + 354 = 737, "about 740" is correct rounding |
| 33 | Key numbers | Grant 314916, Research Council of Norway | Supported | p14 | |
| 34 | Notes | Grey literature archived on CGSpace | Not in source | none | Consistent with handle prefix 10568 and LICENSES.md, but not in the PDF. No fix needed |
| 35 | Notes | Shares co-author Marit Jørgensen with jorgensen-2026-gse | Supported | p1 | Confirmed in that card's authors |
| 36 | Frontmatter | gist | Imprecise | p10, p12 | See Fix 2 |
| 37 | Frontmatter | authors | Supported | p1 | |
| 38 | Frontmatter | article | Supported | p1 | |
| 39 | Frontmatter | crops | Supported | p10 | |
| 40 | Frontmatter | region | Supported | p5, p8, p10 | |
| 41 | Frontmatter | data | Supported | all | No data link |
| 42 | Frontmatter | license | Supported | all | No license stated |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Biomass result by region: only the four-way mixture beats Desho in Amhara, seven options in SNNP, strong regional contrast (p10) | No | high | Fix 1, Fix 11 |
| Ease of harvesting and transplanting correlate most with overall preference, yield weakly (p11) | No | high | Fix 1, Fix 11 |
| Desho and the four-way mixture are the highlighted best options, with a trade-off on ease of harvesting (p12) | No | high | Fix 1 |
| 21 options: 4 grasses, 5 legumes, 12 mixtures, including two four-way mixtures (p10, p12) | No | medium | Fix 1, Fix 8, Fix 11 |
| Trial year: package labels "EthiopiaGrass 2022" (p7) | No | medium | Fix 1, Fix 8 |
| Design table: 14 options at 76 to 78 allocations, about 21% each (p7), not matching 21 options in results | No | medium | Fix 11 |
| Eight tricot woredas on map: Bahirdar Zuria, Bilate Zuria, Dangila, Dera, Doyogena, Hadero Tunto, Hulbareg, Lemmo (p5) | Partly (three named) | medium | Fix 1, Fix 8 |
| Analyses by region (p10, p11) and pooled (p11, p12) | Partly | low | Fix 8 |
| Overall preference reference variable undefined (p11) | No | low | Fix 11 |
| Soil fertility question typo, two traits not in results (p9) | No | low | Fix 11 |
| Aim, background, site criteria, lessons, enabling factors, funder (p2, p3, p5, p6, p13, p14) | Yes | | |

## Template compliance

- Summary word count: 337. Below the 400 to 500 target. The replacement in Fix 1 is 496.
- Gist: 26 words, under 30. But it states what was done, not what the slides show (Fix 2). The replacement is 29 words.
- Keywords: 10, inside 8 to 12.
- Questions: 4, inside 4 to 7. Questions 2 and 3 (which traits farmers value, how options compare with Desho) are not answered by the current card. Fix 1 answers them.
- not_established: missing. Optional in the template, but advised for a slide deck (Fix 10).
- Stated limitations: one item is the curator's view, not the authors' (Fix 9).
- License wording: "see repository record" instead of the template's "see CGSpace record". Optional change.
- House style: tricot is lowercase throughout. No em dashes. The only semicolon is in the crops field, which is metadata. The id matches the file name.
