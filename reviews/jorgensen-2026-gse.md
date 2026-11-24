# Card review: jorgensen-2026-gse

- **Card:** papers/jorgensen-2026-gse.md
- **Source:** papers-pdf/jorgensen-et-al-2026.pdf (3 pages, printed pages 516 to 518 = PDF pages 1 to 3)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 50 (plus 1 field, doi, that cannot be checked from the PDF) |
| Supported | 44 |
| Imprecise | 4 |
| Not in source | 1 |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 5 |
| Important omissions | 4 |
| Metadata issues | 7 |

The summary, methods and key numbers follow the source closely, and every number in the body is correct. The card has one wrong claim: the Notes entry says each region has "10 forages + 1 regional check", but Table 1 (p. 518) gives 10 mixtures per region in total (8 common + 2 regional) and never mentions a check. Other fixes: the crops field names festulolium, which is not in Table 1, and misses meadow fescue and tall fescue. peer_reviewed: yes breaks the template rule for conference papers. not_established is missing. The summary is short (375 words) and does not say that the paper reports no results.

## Fixes needed

1. **Notes: wrong mixture count and an unsupported "regional check".** The card says: "There are two regional trails implemented with 12 mixtures. North with 10 forages + 1 regional check. South with 10 forages + 1 regional check." The source (Table 1, p. 518, PDF p. 3) lists 12 mixtures. Eight are labelled Common (1 to 7 and 10), two South/Central (8, 11) and two North/Mountain (9, 12). So each region draws on 10 mixtures in total. This matches the abstract's "three options out of the total ten options" (p. 516). The paper never calls any mixture a check. "10 + 1" gives 11 per region, which does not fit the table. "trails" is also a typo for "trials". If the curator knows from the project that one mixture is a regional check, write that as outside information and name the source. Suggested replacement:

   > - Table 1 (p. 518) lists 12 mixtures: 8 common to both regions (1 to 7 and 10), 2 for South/Central (8 and 11) and 2 for North/Mountain (9 and 12). Each regional pool therefore has 10 mixtures, which matches the "ten options" in the abstract (p. 516). The methods text speaks of twelve mixtures overall (p. 517). Mixtures 8 and 9 have the same species proportions (40% timothy, 50% meadow fescue, 10% red clover) and differ only in their region label. The paper does not say whether they differ in cultivars or serve as standard checks. [If confirmed by the project team, add here: "Outside information (source, date): mixtures 8 and 9 are the regional check mixtures."]

2. **crops: festulolium is not in the source, and two main species are missing.** The card says "timothy, ryegrass, festulolium, red and white clover, lucerne and others". Table 1 (p. 518) names 12 species by Latin name. None is festulolium (a Festuca × Lolium hybrid). *Lolium pratense* is meadow fescue and *Lolium arundinaceum* is tall fescue, both under their newer Lolium names. The common names below are the reviewer's translation of the Latin names, not words from the paper. Meadow fescue is a major component (up to 50%) and tall fescue reaches 70% in mixture 7. Suggested replacement:

   > crops: forage grass and legume seed mixtures (timothy, meadow fescue, tall fescue, perennial ryegrass, smooth meadow-grass, cocksfoot, smooth brome, red fescue, common bent, red clover, white clover, lucerne)

3. **peer_reviewed conflicts with the template.** TEMPLATE.md says peer_reviewed is "no" for conference papers. The card is typed "conference paper" and says "yes". The PDF says nothing about review. Suggested replacement:

   > peer_reviewed: no

   (If the maintainers decide that Grassland Science in Europe papers count as reviewed, change the template rule first, so the cards stay consistent.)

4. **not_established is missing.** This is a project-design paper with no results, so it is easy to over-read. Suggested text:

   > not_established: that tricot gives robust results for perennial forage mixtures in Norway (proposed, not yet tested); that any mixture outperforms another (no performance results reported); that farmer rankings can replace RCBD trials for feed quality or biomass yield (the authors say these need controlled trials); that the project has increased adoption or farmer engagement (expected, not yet measured); that the confirmatory Plackett-Luce model with covariates has been fitted (planned)

5. **Summary does not say that no results are reported, and it is under the 400-word target (375 words).** The paper's results section (p. 518) only reports that the mini-trials were being sown and that interest was high. It expected first results in early autumn 2025. The Stated limitations section mentions this, but the summary does not. The summary also leaves out the stated aim to test whether tricot works across Norway's climates (p. 516). Suggested additions (about 476 words in total once all are added, including fix 6):

   - After "Its aim is a cost-effective, farmer-led testing framework ... promote their adoption." add:
     > The authors will evaluate whether tricot gives robust results across Norway's diverse climates, and how participatory research supports farmer engagement and knowledge sharing.
   - After "... targeted at southern and central or northern and mountain areas." add:
     > Each region draws on 10 mixtures, eight common and two regional (card's count from Table 1), which matches the ten options named in the abstract.
   - After "Primary outcomes are overall rank, winter survival and yield across mixture, region and year." add:
     > Secondary outcomes such as weed invasion, plant height and legume cover are analysed in an exploratory way.
   - At the end of the last paragraph add:
     > The paper reports no performance results. The mini-trials were being sown at the time of writing, and first results were expected in early autumn 2025.

6. **Summary adds a causal link that the source does not state.** The card says: "more than the planned 100 farmers wanting to join, so another 100 will be recruited in 2026". The source says, separately, that another 100 participants will be recruited in 2026 (p. 517) and that the extra interested farmers will be included in the 2026 round (p. 518). It does not say how many extra farmers asked or that they explain the 100. Suggested replacement:

   > Interest exceeded expectations, with more than the planned 100 farmers wanting to join. These extra farmers will join the 2026 round, when another 100 participants will be recruited, and mixtures may be adjusted from first-round feedback by farmers and advisers.

7. **Methods bullet "Evaluation" calls the spring step a best-worst question.** The source says that in spring farmers will report winter conditions, especially ice cover (p. 517). It does not describe this as a best-worst ranking. Suggested replacement:

   > - **Evaluation.** Best-worst questions in the establishment autumn and at harvest, a spring report on winter conditions such as ice cover, plus overall performance against the surrounding field and fertiliser type and amount.

8. **software field names a package the paper does not name.** The paper names ClimMob and the Plackett-Luce model. It says ClimMob includes R packages for analysis (p. 517, citing Quiros et al. 2024), but it does not name the PlackettLuce package. The template format for this field is also for a CRAN package with a version. Suggested replacement:

   > software: ClimMob (https://climmob.net/), which includes R packages for analysis and agro-climatic indices (packages not named in the paper)

9. **Question 1 implies an answer the paper cannot give yet, and "high-income" is not in the source.** The paper proposes to test whether tricot works in Norway (p. 516) but has no results. Suggested replacement, plus one optional new question (5 questions in total):

   > - How is tricot being set up to test whether it works in a high-latitude country like Norway?
   > - Which forage species and seed mixtures are being compared, and for which regions?

10. **gist reads as a description rather than a finding.** The current gist is accurate, but it does not say that this is a design paper without results. Suggested replacement (26 words):

    > gist: Sets out INNOFORAGE, the first tricot use in Norway: 12 forage seed mixtures in 100 on-farm mini-trials plus RCBD trials. No performance results are reported yet.

11. **type is outside the template's list.** "conference paper" is not one of the TEMPLATE.md types, and this is the only card in the knowledge base that uses it. The label is accurate for the source. Either add "conference paper" to the template list or ask the maintainers which existing type to use. No change to the card is needed if the template is updated.

12. **license wording (low).** The PDF states no licence. papers-pdf/LICENSES.md records "none stated (conference proceedings)". For consistency, suggested replacement:

    > license: none stated in PDF (see repository record)

13. **Optional key number.** Add a row for the regional pool size, which matters to tricot users designing incomplete blocks:

    > | 10 per region | Mixtures in each regional pool: 8 common + 2 regional (Table 1) | This paper (card's count from Table 1) |

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Improving forage production in Norway. Participatory evaluation of climate-adapted seed mixtures | Same, with a colon after "Norway" (p. 516) | Supported (colon to period is expected) |
| authors | Jørgensen M, Borchsenius R, Elverland E, Gillund F, Muradagha K, de Sousa K, Sturite I | Same seven authors in the same order (p. 516) | Supported |
| year | 2026 | Year not printed. Vol. 31 footer, PDF created April 2026. Text was written in 2025 (spring 2026 is in the future, p. 517) | Supported (indirect) |
| journal | Grassland Science in Europe | Footer, Vol. 31 (pp. 516 to 518) | Supported |
| article | 31, 516-518 | Printed pages 516, 517, 518 | Supported |
| type | conference paper | EGF proceedings volume | Supported for the source, but not in the template vocabulary (fix 11) |
| source | team | Jørgensen M and de Sousa K are in people.md | Supported |
| peer_reviewed | yes | Not stated in the PDF. Template says "no" for conference papers | Not in source, template conflict (fix 3) |
| doi | https://hdl.handle.net/11250/5574875 | No DOI or handle in the PDF. Matches papers-pdf/LICENSES.md. Could not open the record (site blocked) | Not checkable from PDF |
| license | see proceedings | No licence in PDF | Supported, wording differs from LICENSES.md (fix 12) |
| data | none yet (trials ongoing) | No data statement, no results yet (p. 518) | Supported |
| software | ClimMob, PlackettLuce | ClimMob and "Plackett-Luce model" named, R packages unnamed (p. 517) | Imprecise (fix 8) |
| crops | ... ryegrass, festulolium, ... | Table 1 species list (p. 518), no festulolium | Imprecise (fix 2) |
| region | Norway (about 59 to 70° N) | Farmers at about 59 to 67° N and 61 to 70° N (p. 518) | Supported |
| gist | Describes INNOFORAGE, the first tricot application in Norway ... | "new to Norway" (p. 516), 100 mini-trials (p. 517), RCBD at station and selected farms (p. 516) | Supported, style fix suggested (fix 10) |
| not_established | missing | Design paper with no results | Missing (fix 4) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Milk and meat are Norway's most important sectors and depend on stable high-quality forage | Supported | Abstract (p. 516) | |
| 2 | Summary | Choosing species, cultivars, mixtures is hard because conditions vary in latitude and altitude, and climate change shifts boundaries unpredictably | Supported | Abstract (p. 516) | |
| 3 | Summary | Without on-farm data, underperforming varieties or mixtures may be recommended | Supported | Abstract (p. 516) | |
| 4 | Summary | RCBD trials are labour-intensive, costly, limit sites, usually exclude farmers | Supported | Introduction (p. 516) | Source says "often", card says "usually". Fine. |
| 5 | Summary | INNOFORAGE (2025–2028) brings tricot to Norway for the first time | Supported | "it is new to Norway" (p. 516) | |
| 6 | Summary | Aim: cost-effective farmer-led framework to identify mixtures and promote adoption | Supported | p. 516 | |
| 7 | Summary | tricot combined with RCBD at a station and selected farms because feed quality and biomass yield need controlled trials | Supported | pp. 516 to 517, Figure 1 (p. 517) | Source uses future tense ("will ... integrate"). Card's present tense is acceptable. |
| 8 | Summary | Twelve mixtures developed with seed companies, advisers and researchers, some common, some regional | Supported | p. 517, Table 1 (p. 518) | |
| 9 | Summary | ClimMob assigned three mixtures per mini-trial in a balanced incomplete block design | Supported | p. 517 | Source adds "randomly". |
| 10 | Summary | 100 mini-trials established in summer 2025, three 3 by 7 m plots managed as part of the field | Supported | p. 517 | See source issue 2 on tense. |
| 11 | Summary | 30 northern-mountain trials to farmers at about 61 to 70° N, 70 to central-southern farmers at about 59 to 67° N | Supported | p. 518 | |
| 12 | Summary | Farmers evaluate with best and worst questions at set times | Supported | p. 517 | |
| 13 | Summary | Establishment autumn: sown-species and legume cover, weed invasion, plant height | Supported | p. 517 | |
| 14 | Summary | Spring: winter conditions such as ice cover | Supported | p. 517 | |
| 15 | Summary | Harvest: yield, legume and weed proportions, overall performance against the surrounding field, fertiliser use | Supported | p. 517 | Timing of the overall-performance and fertiliser questions is implied ("In addition"), not stated. Acceptable. |
| 16 | Summary | Management, soil and agro-climate indices are covariates in a confirmatory Plackett-Luce model | Supported | p. 517 | Source adds "to reduce confounding". |
| 17 | Summary | Primary outcomes: overall rank, winter survival, yield across mixture, region and year | Supported | p. 517 | Secondary outcomes omitted (see Completeness). |
| 18 | Summary | Trials run for at least two production years | Supported | p. 517 | |
| 19 | Summary | More than 100 farmers wanted to join, "so" another 100 will be recruited in 2026, mixtures may be adjusted | Imprecise | p. 517, p. 518 | Causal link added by the card (fix 6). |
| 20 | Summary | Advisers keen to use mini-trials at field days | Supported | p. 518 | |
| 21 | Summary | Engagement and learning studied with interviews, surveys, stakeholder meetings | Supported | pp. 517 to 518 | |
| 22 | Methods | 12 mixtures, 3 per farm, balanced incomplete blocks in ClimMob, plus station and on-farm RCBD | Supported | pp. 516 to 517 | |
| 23 | Methods | 100 mini-trials 2025, 3 × 7 m plots, at least two production years, another 100 farmers in 2026 | Supported | p. 517 | |
| 24 | Methods | Best-worst questions in autumn, spring and at harvest | Imprecise | p. 517 | Spring is a report of winter conditions, not a best-worst question (fix 7). |
| 25 | Methods | Plackett-Luce with management, soil, agro-climate covariates, mixed methods for engagement | Supported | pp. 517 to 518 | |
| 26 | Limitations | Feed quality and biomass yield need controlled RCBD trials | Supported | pp. 516 to 517 | |
| 27 | Limitations | No results yet, first results expected autumn 2025 | Supported | "early autumn 2025" (p. 518) | |
| 28 | Key numbers | 12 mixtures | Supported | p. 517, Table 1 | |
| 29 | Key numbers | 100 mini-trials, summer 2025 | Supported | p. 517 | |
| 30 | Key numbers | 3 × 7 m plots, three per mini-trial | Supported | p. 517 | Source prints "3 × 7 m2" (source issue 5). |
| 31 | Key numbers | 30 / 70 trials | Supported | p. 518 | 30 + 70 = 100, checked. |
| 32 | Key numbers | 61–70° N / 59–67° N | Supported | p. 518 | |
| 33 | Key numbers | 100 more farmers in 2026 | Supported | p. 517 | |
| 34 | Key numbers | 2025–2028 project period | Supported | p. 516 | |
| 35 | Notes | Two regional trials drawn from 12 mixtures | Supported | Table 1 (p. 518) | Typo "trails". |
| 36 | Notes | Each region has 10 forages + 1 regional check | Contradicted | Table 1 (p. 518), abstract (p. 516) | 10 per region in total (8 common + 2 regional). No check mentioned (fix 1). |

The other 14 checked claims are the frontmatter fields in the Metadata check above (11 Supported, 2 Imprecise, 1 Not in source). doi is listed there but not counted. Questions were reviewed for wording (fix 9) but are not counted as claims.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The abstract speaks of ten options in the trial. The methods and Table 1 give twelve mixtures. Table 1 explains the gap: each region draws on 10 (8 common + 2 regional). | p. 516 vs p. 517, Table 1 p. 518 | Partly. The Note tries but gives the wrong count | See fix 1. |
| Tense conflict. The methods say 100 mini-trials were established in summer 2025. The results say they are still being sown and call them planned for 2025. | p. 517 vs p. 518 | No | - The methods say 100 mini-trials were established in summer 2025 (p. 517), but the results say they were still being sown (p. 518). The paper was written during establishment. |
| Mixtures 8 and 9 have identical species proportions but different region labels, with no explanation (cultivars may differ). | Table 1, p. 518 | No | Included in the suggested Note in fix 1. |
| Ergon et al. (2018) is in the reference list but not cited in the text. | p. 518 | No | Not needed in the card. |
| Plot size printed as "3 × 7 m2", a unit typo for 3 × 7 m. | p. 517 | Card silently corrects it to 3 × 7 m | Not needed. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| No performance results are reported (design and early-uptake paper) | Only in Stated limitations, not in Summary | High | Fix 5, last addition. |
| Stated aim to evaluate whether tricot gives robust results across Norway's climates, and how participation supports engagement and knowledge sharing | No | Medium | Fix 5, first addition. |
| Each region draws on 10 of the 12 mixtures (8 common + 2 regional) | No (Note is wrong) | Medium | Fix 1, fix 5 second addition, fix 13. |
| Mixture composition (Table 1): timothy-, meadow fescue-, tall fescue-, cocksfoot- and ryegrass-based mixtures, legumes 10 to 20% in every mixture, lucerne only in mixture 10, mixture 11 is 90% perennial ryegrass with white clover | Partly (crops field, with an error) | Medium | Fix 2. Optional Note: "- In Table 1 every mixture contains 10 to 20% legumes (card's sum). Lucerne appears only in mixture 10 (10%). Mixture 11 is 90% perennial ryegrass with 10% white clover." |
| Secondary outcomes (weed invasion, plant height, legume cover) analysed in an exploratory way | No | Low to medium | Fix 5, third addition. |
| Farmers gave informed consent and agreed to focus groups and surveys | No | Low | Optional. |
| ClimMob gives rapid feedback and includes R packages for analysis and agro-climatic indices (Quiros et al. 2024) | Partly | Low | Covered by fix 8. |
| Figure 1 flow chart: RCBD and tricot data combined in an integration step | Partly | Low | None needed. |
| Funding: Agricultural Research Funds (FFL/JA), grant no 352917 | No | Low | Optional Note. |
| Authors' conclusion: the project will support adaptation of mixtures and improve adoption, ownership and engagement | Partly (aim only) | Low | Covered by not_established (fix 4), which marks this as expected, not shown. |

## Template compliance

- Summary word count: 375, below the 400 to 500 target. Fixes 5 and 6 bring it to about 476.
- Gist: 21 words, under 30. The suggested replacement is 26 words.
- Keywords: 10, within 8 to 12.
- Questions: 4, within 4 to 7 (5 with the optional addition in fix 9).
- House style: tricot is lowercase throughout. No em dashes or semicolons in the body. The en dashes in "2025–2028" and the latitude ranges are fine.
- Long-format sections are all present.
- type "conference paper" is not in the template vocabulary (fix 11). peer_reviewed: yes conflicts with the template rule for conference papers (fix 3).
- The card is already marked curated_card: yes. The Notes entry and the crops field are wrong, so it should be fixed before keeping that status.
