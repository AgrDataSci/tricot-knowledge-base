# Card review: mbugua-2024-mib

- **Card:** papers/mbugua-2024-mib.md
- **Source:** papers-pdf/mbugua-et-al-2024.pdf (12 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 46 |
| Supported | 41 |
| Imprecise | 3 |
| Not in source | 2 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 7 |
| Important omissions | 7 (3 high, 4 medium) |
| Metadata issues | 2 |

The card is accurate. Nearly every sentence traces to the abstract, key points, Table 1 or Annex 1, and the automated check found all 12 numbers. Its weak point is that it follows the brief's headline wording and leaves out the results section. It does not say that the hybrid and home use concepts are statistically tied overall, that preferences split by region and gender, or that the analysis used Plackett-Luce models in ClimMob with a design inspired by tricot. A tricot user would ask about all three. The "Stated limitations" are the card's own and are not stated by the authors. The card also lacks not_established and has only 3 questions. The most important fix is to add the tie and the subgroup split (Figure 3 and Table 4 on p. 6 and 7, Figure 4 on p. 7).

## Fixes needed

1. **Add the statistical tie and the subgroup results (high).** The card says the full ranking ran hybrid, home use, intercropping, feed and food, food and fodder, malting, forage, as a strict order. The source's Figure 3 (p. 6) gives hybrid and home use the same letter "a", and feed and food and food and fodder the same letter "c". Table 4 (p. 7) shows the hybrid beat home use in only 54% of direct comparisons, and food and fodder against feed and food was 50/50. The Plackett-Luce tree (Figure 4, p. 7, text p. 6) splits by district (p = 1.9e-13), then gender in Dodoma. Shinyanga farmers (n = 550) prefer the hybrid ("a" versus "b" for home use). Dodoma women (n = 232) and Kongwa men (n = 177) place home use slightly above the hybrid, with no significant difference. The replacement summary below covers this.

2. **Replace "Stated limitations" (medium).** The brief states no limitations. "A brief rather than a full research paper, with limited statistical detail" and "Results cover two regions of Tanzania" are the card's own observations, and the section heading presents them as the authors'. Replace with:

   ```
   - The brief does not state limitations.
   - Card note: preferences are stated for hypothetical concepts shown on video, not observed seed purchases or adoption.
   - Card note: the sample covers four districts in two regions (Dodoma, Shinyanga), so results may not hold for other sorghum areas of Tanzania.
   - Card note: the brief reports little statistical detail. It gives no model fit statistics and no results for the other survey questions (similarity to current varieties, interest in trying, willingness to replace).
   ```

3. **Add not_established (medium).** Suggested frontmatter line:

   ```
   not_established: that farmers will buy or adopt hybrid sorghum seed (preferences were stated for hypothetical concepts); that the hybrid is preferred over home use across Tanzania (the two were not significantly different overall, and Dodoma differed from Shinyanga); that farmers accept a 20% yield penalty in practice; that brewing demand drives the hybrid preference (this is the authors' interpretation, and the hybrid concept was described as not designed for malting); results for regions other than Dodoma and Shinyanga
   ```

4. **Soften "shows" for the home use result (low).** The card says the 20% yield penalty "shows that sorghum's value in rural diets can outweigh yield". The source says the result "highlights" or "considers" that sorghum is important in rural diets (p. 1, p. 8). The 20% is also relative to other improved seed, and the concept still out-yields local varieties (Annex 1, p. 9). Covered by the replacement summary. As a standalone fix: "The authors read the strong ranking of home use, which was described as yielding 20% less than other improved seed but still more than local varieties, as a sign that sorghum's value lies in home use and rural diets."

5. **Make the export figure precise and attributed (low).** The card says "Tanzania's regional sorghum exports grew by 300% over five years". The key points (p. 1) and discussion (p. 8) say this, but p. 2 shows it is the export value from FAOSTAT, USD 2.4 million in 2012 to about 11.4 million in 2022. Replacement: "citing FAOSTAT data showing that the value of Tanzania's sorghum exports rose by more than 300%". Also add the source issue to Notes (see Source issues).

6. **Label the three current segments (medium).** The card gives the hectares and investment shares but not which segment is which. Table 1 (p. 3) shows segments 1 and 2 are OPV (white/cream and red/brown) and segment 3 is hybrid (white/cream, 8,742 ha, 20% of investment). This matters because the hybrid segment is the smallest by area. Replace the Key numbers row with:

   `| 561,989 / 312,216 / 8,742 ha and 60% / 20% / 20% | Size and share of 2023–2024 investment of current segments 1 (OPV, white/cream), 2 (OPV, red/brown) and 3 (hybrid, white/cream) | This brief (Table 1) |`

7. **Expand Methods in brief (medium).** The current three bullets omit the analysis and most of the design. Replacement:

   ```
   - **Concept development.** Eight focus-group discussions with smallholders, interviews with seed producers, traders, processors and TARI, a sorghum product design team meeting and consultations with CIMMYT breeders produced seven concepts. Early maturity, higher yield than local varieties, and drought and disease tolerance were held constant across concepts.
   - **Videos.** Nine studio videos in Swahili (an introduction, seven concepts of one to two minutes each, and a closing video), with an actor playing an agrodealer representative. Each concept video stated benefits and drawbacks. Scripts are in Annex 1.
   - **Design.** Inspired by tricot: each farmer watched three of the seven concepts, randomized so that each concept was shown equally often, and ranked them. Farmers also answered questions on similarity to current varieties, interest in trying, willingness to replace and preferred grain colour.
   - **Sample.** Household survey of 1,100 sorghum farmers in Kongwa and Kondoa districts (Dodoma Region) and Kishapu and Shinyanga districts (Shinyanga Region).
   - **Analysis.** Plackett-Luce model in ClimMob, a Plackett-Luce tree with region, district and gender as covariates, and pairwise win percentages.
   ```

8. **Add questions to reach 4 to 7 (template).** Add:

   ```
   - Do sorghum concept preferences differ by region, district or gender in Tanzania?
   - How was the tricot ranking design adapted to test seed product concepts by video?
   - Which grain colour do Tanzanian sorghum farmers prefer?
   ```

9. **Add Key numbers rows.**

   ```
   | 54% | Direct comparisons in which the hybrid concept was ranked above home use (Table 4) | This brief |
   | 70% | Farmers preferring white/cream grain across concepts (Figure 5) | This brief |
   | 20% lower / 30% higher | Yield stated in the home use and hybrid concept videos, relative to other improved seed | This brief (Annex 1) |
   | 232 / 141 / 177 / 550 | Farmers in the four Plackett-Luce tree nodes: Dodoma women, Kondoa men, Kongwa men, Shinyanga | This brief (Figure 4) |
   | >300% | Rise in value of Tanzanian sorghum exports, USD 2.4 million (2012) to about 11.4 million (2022) | FAOSTAT 2023, cited in this brief |
   ```

10. **Replacement summary.** It covers fixes 1, 4, 5 and 6 and the main omissions. It has 495 words, with no semicolons or em dashes. The current summary also repeats the segmentation proposal in two paragraphs and puts a methods sentence at the end of the segmentation paragraph. This version removes that repetition.

   ```
   The brief applies video-based product concept testing (VPCT) to sorghum in Tanzania, one of the largest sorghum producers in Eastern Africa. Its aim is to give CGIAR and national research partners farmer evidence for discussions on seed product market segments and target product profiles (TPPs).

   Through focus groups, stakeholder interviews and consultations with breeders and industry, the team developed seven seed product concepts. Five target an end use (home use, feed and food, industrial malting, food and fodder, forage), one targets the cropping system (intercropping with peas) and one targets the material type (a high-yielding hybrid). Each concept was presented in a short scripted Swahili video that stated its benefits and its drawbacks, such as lower yield or the need to buy seed every season. A household survey reached 1,100 sorghum farmers in four districts of the Dodoma and Shinyanga regions. In a design inspired by tricot, each farmer watched three of the seven concept videos and ranked them. The rankings were analysed with Plackett-Luce models in ClimMob, with region, district and gender as covariates.

   The hybrid and home use concepts formed the first tier. They were not significantly different from each other, and in head-to-head comparisons farmers ranked the hybrid above home use 54% of the time. Intercropping came next, then feed and food and food and fodder, which were tied. Industrial malting and forage were least preferred. Preferences differed by place and gender. In Shinyanga, men and women preferred the hybrid over home use. In Dodoma, women and men in Kongwa District placed home use above the hybrid, but the figure does not show these gaps as significant.

   The authors link the hybrid preference to growing interest in sorghum as a cash crop for brewing and export. They cite FAOSTAT data showing that the value of sorghum exports rose by more than 300%. The home use concept was described as yielding 20% less than other improved seed, though still more than local varieties. The authors read its strong ranking as a sign that sorghum matters in rural diets and that its value lies in home use. They call for work with farmers, processors and food scientists to define and measure good taste and cooking quality. Across concepts, 70% of farmers preferred white or cream grain, which the authors call a must-have for national and regional markets.

   The brief compares these results with the three current sorghum segments for Tanzania. Two are open-pollinated (white/cream on 561,989 ha and red/brown on 312,216 ha) and one is hybrid (white/cream on 8,742 ha). They received 60%, 20% and 20% of 2023–2024 investment. The authors recommend prioritizing the hybrid segment and adding home use as a new current segment. They see intercropping, food and feed, and food and fodder as near-term future segments, and forage as a possible long-term segment. They also recommend prioritizing white varieties.

   The results are stated preferences for hypothetical products. They show which product goals farmers favour, not what they will buy or adopt.
   ```

   The last paragraph is the card's own reading. If the curator prefers to keep the summary strictly to the source, drop it and keep the point in Stated limitations and not_established.

11. **Add the source issues to Notes.** See the suggested Notes text in the Source issues table.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Farmers' requirements for sorghum seed products in Tanzania | Same (p. 1) | Supported |
| authors | Mbugua M, Donovan J, Rutsaert P, Gandhi H, Nas TM, Templer N, de Sousa K, Mawia H, Ojiewo CO, Gichuru L, Mwenda E | Same 11 authors in same order (p. 1, p. 12) | Supported (the author bios on p. 11 name "Harriet Joel", see Source issues) |
| year | 2024 | Recommended citation, 2024 (p. 12) | Supported |
| journal | CGIAR Market Intelligence Brief 15 | Market Intelligence Brief Series 15, CGIAR (p. 12) | Supported |
| article | Market Intelligence Brief 15 | Page headers (all pages) | Supported |
| type | policy brief | Brief in the Market Intelligence Brief series (p. 12) | Supported |
| peer_reviewed | no | p. 12 calls the series a "peer-reviewed series" | Metadata issue (low). "no" follows the template rule for briefs, but add a Note so readers know the series claims peer review |
| doi | https://hdl.handle.net/10883/34683 | Link behind "Available here" in the recommended citation (p. 12) | Supported |
| license | see repository record | No licence stated in the PDF | Supported |
| data | none | No dataset cited. Analysis was in ClimMob (p. 6) | Supported |
| crops | sorghum | p. 1 | Supported |
| region | Tanzania (Dodoma, Shinyanga) | p. 1, p. 6 | Supported. Could add the districts Kongwa, Kondoa, Kishapu, Shinyanga |
| gist | Video-based concept testing with 1,100 Tanzanian farmers finds hybrid and home-use sorghum concepts most preferred, and proposes revised market segments and product profiles | p. 1, p. 6, p. 8 | Supported. 23 words, says what the source shows. "Most preferred" for both concepts is fair given the tie |
| not_established | missing | | Metadata issue. See fix 3 |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Applies VPCT to sorghum in Tanzania | Supported | Abstract (p. 1), Methods (p. 4) | |
| 2 | Summary | Tanzania one of the largest sorghum producers in Eastern Africa | Supported | Abstract (p. 1). p. 2 says Eastern and Southern Africa, seventh globally | |
| 3 | Summary | To inform CGIAR and national discussions on segmentation and TPPs | Supported | Abstract, CGIAR and NARES (p. 1) | |
| 4 | Summary | Concepts developed through engagements with breeders, farmers and industry | Supported | Abstract (p. 1), details p. 4 | |
| 5 | Summary | Five end-use, one cropping system, one material type concept | Supported | Abstract (p. 1) | |
| 6 | Summary | 1,100 farmers in Dodoma and Shinyanga | Supported | p. 1, p. 6 | |
| 7 | Summary | Each farmer viewed and ranked three concepts | Supported | p. 1, p. 6 | |
| 8 | Summary | Hybrid most likely chosen as most preferred, then home use | Supported | Abstract (p. 1) | Matches the source wording. See #11 for the tie |
| 9 | Summary | Proposes revisions to segments and TPPs | Supported | Abstract (p. 1), p. 8 | |
| 10 | Summary | Gives existing segment sizes and investment shares | Supported | Table 1 (p. 3) | |
| 11 | Summary | Full ranking as a strict order of seven | Imprecise | Key points (p. 1) and p. 8 give this order. Figure 3 (p. 6) and Table 4 (p. 7) show hybrid and home use tied ("a"), and feed and food and food and fodder tied ("c", 50/50) | The strict order hides two ties. Fix 1 |
| 12 | Summary | Authors link hybrid preference to cash crop for brewing and export | Supported | p. 1, p. 8 | Attributed correctly. See Source issue 2 |
| 13 | Summary | Regional sorghum exports grew by 300% over five years | Imprecise | p. 1 and p. 8 say this. p. 2 shows it is export value, USD 2.4 million (2012) to about 11.4 million (2022), from FAOSTAT | Metric (value) and secondary source (FAOSTAT) not given. Fix 5 |
| 14 | Summary | Home use concept described as yielding 20% less | Supported | Table 3 (p. 5), Annex 1 (p. 9) | Relative to other improved seed. Still above local varieties (p. 9) |
| 15 | Summary | "which shows that sorghum's value in rural diets can outweigh yield" | Imprecise | Source says "considers" (p. 1) and "highlights" (p. 8) | Wording more certain than the source and generalised. Fix 4 |
| 16 | Summary | Calls for work with farmers, processors, food scientists on taste | Supported | p. 1, p. 8 | p. 8 also adds "good cooking qualities" |
| 17 | Summary | 70% preferred white grain across concepts | Supported | p. 1, p. 7, p. 8, Figure 5 | Mean of the six bars read off Figure 5 is about 70% (approximate) |
| 18 | Summary | White is a must-have for national and regional markets and linked to better-tasting foods | Supported | p. 1, p. 8 | |
| 19 | Summary | Prioritize hybrid, consider new segments for home use, intercropping, food and fodder, food and feed, keep forage as future | Supported | Key points (p. 1), p. 8 | p. 8 separates home use (new current segment) from the three near-term future segments. Forage is long-term |
| 20 | Summary | Current segments cover 561,989, 312,216 and 8,742 ha | Supported | Table 1 (p. 3) | Segments not labelled. Fix 6 |
| 21 | Summary | 60%, 20%, 20% of 2023–2024 breeding investment | Supported | Table 1 (p. 3) | Table says "proportion of investment" without "breeding", but the context is breeding |
| 22 | Summary | Each concept presented through a scripted video with benefits and trade-offs | Supported | p. 4, p. 6 | |
| 23 | Summary | Scripts reproduced in an annex | Supported | Annex 1 (p. 9 and 10) | |
| 24 | Summary | Scripts make trade-offs explicit | Supported | p. 4 (product goals and potential shortcomings), Annex 1 | |
| 25 | Summary | Feed and food: improved protein for chickens and pigs, less attention to cooking quality | Supported | Annex 1 (p. 9) | |
| 26 | Summary | Home use: cooking quality priority, higher iron and zinc, good flour yield, sweet taste in uji or ugali | Supported | Annex 1 (p. 9) | |
| 27 | Methods | Seven concepts developed with breeders, farmers and industry | Supported | p. 1, p. 4 | |
| 28 | Methods | Each farmer ranked three concepts presented by video | Supported | p. 6 | |
| 29 | Methods | 1,100 farmers in Dodoma and Shinyanga | Supported | p. 6 | |
| 30 | Limitations | A brief rather than a full paper, with limited statistical detail | Not in source | No limitations stated in the brief | Card's own observation under an authors' heading. Fix 2 |
| 31 | Limitations | Results cover two regions | Not in source (as a stated limitation) | The fact is on p. 6, but the authors do not raise it as a limitation | Fix 2 |
| 32 | Key numbers | 7 concepts | Supported | p. 1, Table 3 (p. 5) | |
| 33 | Key numbers | 1,100 farmers | Supported | p. 1, p. 6. Tree nodes sum to 1,100 (232 + 141 + 177 + 550), Figure 4 (p. 7) | |
| 34 | Key numbers | 60% / 20% / 20% investment | Supported | Table 1 (p. 3) | Segments unlabelled. Fix 6 |

The 12 checkable frontmatter fields (title to gist, excluding peer_reviewed and not_established) are counted as Supported in the totals. Notes: "Same method as rutsaert-2023-mib and donovan-2025-expagric, applied to sorghum" is a cross-reference and was not scored. The brief itself cites neither paper. It describes the design as inspired by tricot (p. 6).

Recomputed numbers. Export value 2.4 to 11.4 million USD is +375%. Production 838,717 t to 1 million t is +19%, matching "about 20 percent" (p. 2). Demand projection 11.8 to 29.9 million t is +153%, matching p. 2. Segment areas sum to 882,947 ha, of which the hybrid segment is about 1.0% (card's own calculation, not stated in the source). All Table 4 pairs sum to 100 except the one blank cell.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| 1. Export growth time frame. The 300% figure is called growth "over the past five years", but the data given run 2012 to 2022 (ten years), and USD 2.4 to 11.4 million is +375%. The p. 2 figure also lacks the unit "million" for 11.4, and p. 1 and p. 8 call it "regional" exports while p. 2 says only exported value. | p. 1, p. 2, p. 8 | No | The brief says sorghum export value rose by 300% over five years (p. 1, p. 8), but its own figures (USD 2.4 million in 2012 to about 11.4 million in 2022, FAOSTAT) span ten years and give about +375% (card's calculation). |
| 2. Hybrid preference linked to brewing, but the hybrid concept video says the product is for selling to food-processing traders and is not designed for malting. | p. 1, p. 8 versus Annex 1 (p. 10) | No | The authors link the hybrid preference to brewing demand, but the hybrid concept shown to farmers was described as for food-processing traders and not designed for malting (Annex 1, p. 10). The link is the authors' interpretation. |
| 3. Kondoa District is placed in Shinyanga Region twice on p. 7. p. 6 and Figure 4 place it in Dodoma. | p. 7 versus p. 6 | No | p. 7 twice places Kondoa District in Shinyanga Region. p. 6 and Figure 4 place it in Dodoma. |
| 4. The text cites "Table 3" for the middle-tier comparison. The pairwise data are in Table 4. | p. 7 | No | Low importance, no Notes text needed. |
| 5. Table 4 has a blank cell (food for family versus grain for beer). The reverse cell is 9%, so the missing value is about 91%. | p. 7 | No | Table 4 leaves the food for family versus grain for beer cell blank. The reverse cell (9%) implies about 91%. |
| 6. Key points and discussion state a strict seven-place order, but Figure 3 shows two ties (hybrid and home use, and feed and food and food and fodder). | p. 1, p. 8 versus p. 6, p. 7 | No | The brief's strict ranking hides two statistical ties in Figure 3: hybrid and home use (both "a"), and feed and food and food and fodder (both "c", 50/50 in Table 4). |
| 7. The author list has Harriet Mawia, but the bio on p. 11 names "Harriet Joel". The Figure 4 caption is also garbled ("for male and female participants Different districts"). | p. 1, p. 11, p. 7 | No | Low importance. Optional Note: "The author bio on p. 11 names Harriet Joel. The author list gives Harriet Mawia." |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: farmer requirements as input to SPMS and TPP discussions | Yes | | |
| Design: 7 concepts, video, each farmer ranks 3 | Yes | | |
| Design inspired by tricot incomplete blocks, balanced randomization | No | High | Fix 7 and replacement summary |
| Analysis: Plackett-Luce model in ClimMob, Plackett-Luce tree by region, district, gender | No | High | Fix 7 and replacement summary |
| Hybrid and home use not significantly different overall (54% versus 46% in Table 4) | No | High | Fix 1 |
| Subgroups: Shinyanga prefers hybrid, Dodoma women and Kongwa men place home use first, n per node | No | High (counted with the row above) | Fix 1, Key numbers row |
| Hybrid concept trade-offs: 30% more yield, buy seed each season, less attention to cooking quality, for sale | No | Medium | In replacement summary (in part) and Key numbers row |
| Which current segment is hybrid, and its small area (8,742 ha) against 20% of investment. Hybrid pipeline supplies 2% of the market (p. 8) | Partly | Medium | Fix 6. Optional: "An existing hybrid pipeline supplies 2% of the market (p. 8)." |
| Concept development: 8 focus groups, stakeholder interviews, PDT meeting, CIMMYT breeders. Shared goals held constant | No | Medium | Fix 7 |
| Videos: nine, Swahili, one to two minutes, actor as agrodealer | No | Medium | Fix 7 |
| Other survey questions (similarity, interest, willingness to replace, colour, most and least preferred for purchase), with no results reported | No | Medium | Fix 2 and Fix 7 |
| Discussion: home use is a new current segment, three near-term future segments, forage long-term (drought resistant, possible silage substitute for maize). Intercropping not supported by current breeding | Partly | Low | In replacement summary (in part) |
| Colour by concept: grain for beer split about 50/50 white and red (read off Figure 5, approximate) | No | Low | Optional Note |
| Context: 18 improved varieties released by 2023, low adoption, TPPs with 29 essential traits, three discussion questions (end use, colour, production system) | No | Low | Optional |
| Authors' limitations | None stated | | Fix 2 |
| Conclusions and recommendations | Yes | | |
| Funding: Gates Foundation (AVISA) and CGIAR Market Intelligence Initiative (p. 11) | No | Low | Optional |

## Template compliance

| Item | Value | Status |
|---|---|---|
| Summary word count | 401 | Pass, at the lower edge. The replacement is 495 |
| Gist length | 23 words | Pass |
| Keywords | 9 | Pass. Could add "Plackett-Luce" and "product concept testing" (stays within 12) |
| Questions | 3 | Fail. Long format needs 4 to 7. Fix 8 |
| not_established | Missing | Add (fix 3) |
| Stated limitations | Card's own text under an authors' heading | Fix 2 |
| House style (lowercase tricot and maniva) | Neither word appears in the card. The replacement text uses lowercase tricot | Pass |
| Relations | usesMethodIn: rutsaert-2023-mib | Fine. The brief does not cite it, but the method link is reasonable |
