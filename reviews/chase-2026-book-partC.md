# Card review: chase-2026-book (part C)

- **Card:** papers/chase-2026-book.md, part C only: chapter sections 4 (Recruitment) to 9 (Analysis), card lines 164 to 221
- **Source:** papers-pdf/chase-et-al-2026-tricot-book.pdf (315 pages), part C pages are PDF pages 136 to 187 (printed pages 133 to 184)
- **Reviewed:** 2026-11-24, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 59 |
| Supported | 57 |
| Imprecise | 2 |
| Not in source | 0 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 3 |
| Important omissions | 2 (medium) |
| Metadata issues | 0 (all six Authors lines and page ranges match) |

Part C of the card is accurate and close to the source. Every Authors line matches the chapter bylines, and every page range is correct (the PDF page is the printed page plus 3). The most important fix is in section 6 (Execution): the card says trial plots always get the usual management, but the source makes an exception when the options tested are themselves management practices (PDF p. 153).

## Fixes needed

1. **Section 6, usual management (Imprecise).** The card says the plot "receives exactly the usual management". The source adds an exception: same management as usual unless the technology tested is about crop management (PDF p. 153). This matters for tricot users who test practices.
   Replace:
   "The trial should reflect real production conditions, so the plot sits next to or within the regular field in an average spot and receives exactly the usual management, including intercropping, with neither extra care nor neglect."
   with:
   "The trial should reflect real production conditions, so the plot sits next to or within the regular field in an average spot and receives exactly the usual management, including intercropping, with neither extra care nor neglect, unless the options tested are themselves management practices."

2. **Section 4, registration examples (Imprecise).** The card says registration data can show "whether younger or female participants prefer certain options". The source gives two different examples: whether younger participants adopt a technology faster, and whether female participants prefer certain options (PDF p. 138).
   Replace:
   "such as whether younger or female participants prefer certain options."
   with:
   "such as whether younger participants adopt a technology faster or whether female participants prefer certain options."

3. **Section 8, closing a project (omission, medium).** The card does not say that a project can be closed at any time, that trial documentation is needed for analysis but not for closing, or that submission conflicts can no longer be resolved after closing (PDF pp. 168 to 169). The last point is a practical warning for users.
   Replace:
   "Only the owner can close it, ideally once data are verified and trial documentation is complete, because the analysis module needs completed documentation, enough data and no unresolved submission conflicts."
   with:
   "A project can be closed at any time, but only by the owner, and ideally once data are verified and trial documentation is complete. Documentation is not needed to close, but the analysis module needs it, along with enough data and no submission conflicts, and conflicts cannot be resolved after closing."

4. **Section 9, ranking plus measurement data (omission, medium).** The source says that when a trial has both rankings and measurements, the two are analysed in parallel and combined at the interpretation stage, while joint models are still being researched (PDF p. 173). The card gives only the second half.
   Replace:
   "with joint ordinal-continuous models under development."
   with:
   "with rankings and measurements analysed in parallel and combined at interpretation while joint ordinal-continuous models are under development."

5. **Section 9, optional wording.** The card says heterogeneity "is modelled with Plackett-Luce trees". The source calls recursive partitioning "one widely used approach" (PDF p. 172), and then describes Plackett-Luce regression as another. Not counted as an error.
   Optional replacement: "A widely used way to model heterogeneity is the Plackett-Luce tree (model-based recursive partitioning on environmental or social covariates), which reveals G×E and helps define target populations of environments, as in the Nicaragua bean example where maximum night temperature split the data."

## Metadata check

Frontmatter fields are checked by the other parts. Part C checked the "Authors" line and page range of each chapter section against the chapter bylines in the PDF.

| Field | Card | Source (page) | Status |
|---|---|---|---|
| 4. Recruitment, Authors | Recruitment from the 2020 guide. Field agents and registration by Acuña, Manrow, Madriz, de Sousa | "Taken from van Etten et al. (2020), page 15" (p. 136). "Assign field agents" (p. 139) and "Register participants" (p. 141) both by Acuña, Manrow, Madriz, de Sousa | Supported |
| 4. Recruitment, pages | 136 to 143 | Chapter starts p. 136, RHoMIS note ends p. 143 | Supported |
| 5. Distribution, Authors | Training workshop from the 2020 guide. Trial packages by Acuña, Manrow, Madriz, de Sousa | "Taken from van Etten et al. (2020), page 17" (p. 144). "Trial packages" by the four authors (p. 146) | Supported |
| 5. Distribution, pages | 144 to 151 | p. 144 to p. 151 (p. 151 is blank) | Supported |
| 6. Execution, Authors | From the 2020 guide | "Taken from van Etten et al. (2020), page 19" (p. 152) | Supported |
| 6. Execution, pages | 152 to 154 | p. 152 to 154 | Supported |
| 7. Observation, Authors | From the 2020 guide | "Taken from van Etten et al. (2020), page 21" (p. 155) | Supported |
| 7. Observation, pages | 155 to 158 | p. 155 to 158 | Supported |
| 8. Compilation, Authors | Data collection by Acuña, Manrow, Madriz, de Sousa. Closing a project by Acuña, Manrow, Madriz | Bylines on p. 159 and p. 168 match exactly | Supported |
| 8. Compilation, pages | 159 to 170 | p. 159 to 170 | Supported |
| 9. Analysis, Authors | Statistical models by de Sousa, van Heerwaarden, Dorado. ClimMob report by Acuña, Manrow, Madriz, de Sousa. R-Instat by Clements, Stern, Chase. Advanced analysis in R by de Sousa | Bylines on p. 171, p. 179, p. 183, p. 186 match exactly | Supported |
| 9. Analysis, pages | 171 to 187 | p. 171 to 187 (Feedback starts p. 188) | Supported |

Note for part A: the chapter bylines say "Marilyn Manrow" and "Hugo Dorado", while the frontmatter authors list uses "Manrow-Villalobos M" and "Dorado-Betancourt H". The section lines follow the bylines, which is fine.

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | 4 Recruitment | Anyone may participate. Field agents and posters in shops and village halls help recruit volunteers who commit time, enjoy experimenting, women and men in roughly equal numbers | Supported | p. 136 | |
| 2 | 4 | Existing groups (committees, credit cooperatives, religious groups) can run a joint trial on a host farm | Supported | p. 137 | |
| 3 | 4 | Women's research groups can raise women's participation | Supported | p. 137 | |
| 4 | 4 | Trusted local networks, extension officers and a shared WhatsApp group linking lead farmers with researchers strengthen communication | Supported | p. 137 | Source also includes extension staff in the group. See source issue 1 |
| 5 | 4 | Farmers should take part over several cycles, newcomers learn from experienced peers, everyone tests new sets of options | Supported | pp. 137 to 138 | Source says "ideally" and "we would encourage" |
| 6 | 4 | Field agents added from the library, each needs a username and password for ODK Collect | Supported | p. 139 | |
| 7 | 4 | Registration form built from library questions, serving administration and analysis, e.g. whether younger or female participants prefer certain options | Imprecise | p. 138 | Younger example is about faster adoption. New questions can also be added. Fix 2 |
| 8 | 4 | RHoMIS can be added for deeper household data | Supported | p. 143 | |
| 9 | 5 Distribution | Workshop about four weeks before the trial, at most 20 farmers, men and women in equal numbers where possible | Supported | p. 144 | |
| 10 | 5 | Implementers and field agents explain purpose, benefits, responsibilities, show a demonstration plot or video, hand out a pictorial guide, practise the observation card | Supported | pp. 144 to 145 | |
| 11 | 5 | Package: QR code kept for whole trial, three bags with equal quantities (or instructions), observation card, brochure | Supported | p. 147 | |
| 12 | 5 | Registration uses ODK Collect, scanning the QR code, minimum QR code and participant name | Supported | p. 148 | |
| 13 | 5 | Paper registration then Excel upload possible but discouraged as slower and more error-prone | Supported | pp. 148 to 149 | |
| 14 | 5 | Finishing registration cannot be undone | Supported | p. 149 | |
| 15 | 6 Execution | Farmers plant and manage their own trial and deserve respect as experts | Supported | p. 152 | |
| 16 | 6 | Plot next to or within the regular field, average spot | Supported | pp. 152 to 153 | |
| 17 | 6 | Exactly the usual management, including intercropping, no extra care nor neglect | Imprecise | p. 153 | Omits the exception for management technologies. Fix 1 |
| 18 | 6 | Fair comparison: equal sub-plots side by side (e.g. six rows of 5 m), A left, B middle, C right, borders marked, never mixed | Supported | p. 153 | |
| 19 | 7 Observation | Farmers find it hard to rank on one criterion, so judge one criterion at a time | Supported | p. 155 | |
| 20 | 7 | Three evaluation stages (early, later, post-harvest), dates suggested by implementers | Supported | p. 156 | Source says this is common for fertilizers or varieties |
| 21 | 7 | Phone follow-up reminds, answers questions, can support data compilation | Supported | p. 156 | |
| 22 | 7 | Cards always ask best and worst in few words ("Best foliage?"), with images | Supported | pp. 156 to 157 | See source issue 2 |
| 23 | 7 | Card built from data-collection moments (beans: sowing, 30 days, harvest) and one question per observation | Supported | p. 157 | |
| 24 | 8 Compilation | ClimMob generates a form for each data-collection moment | Supported | p. 159 | |
| 25 | 8 | Field agents fill and send forms in ODK Collect (recommended), administrator checks and corrects, closes the moment and opens the next | Supported | pp. 159 to 160 | |
| 26 | 8 | Cancelling a form in ODK deletes it permanently | Supported | p. 160 | Source adds that existing data are also deleted |
| 27 | 8 | Excel upload possible but not recommended | Supported | p. 160 | |
| 28 | 8 | Enketo lets registered field agents submit from a browser, QR code replaced by owner username, package number, project code, ending with a tilde | Supported | pp. 161 to 166 | Code applies to the registration form (p. 166). Order matches the source pattern |
| 29 | 8 | Closing makes a permanent read-only record | Supported | p. 168 | |
| 30 | 8 | Only the owner can close | Supported | p. 168 | |
| 31 | 8 | Ideally after data verified and documentation complete, because analysis needs documentation, enough data, no conflicts | Supported | pp. 168 to 169 | Source says too little data means analysis "may not generate results". Missing details in Fix 3 |
| 32 | 8 | After closing, edits return an access-restricted message, owner and 1000FARMS administrators notified | Supported | p. 170 | Message is "Access Restricted (403)", notice is by email |
| 33 | 9 Analysis | Plackett-Luce derived from Luce's choice axiom, estimates a worth per item | Supported | p. 171 | |
| 34 | 9 | Suits tricot: partial rankings in incomplete, unbalanced designs, ordinal data, intuitive outputs, covariates and hierarchical extensions | Supported | pp. 171 to 172 | |
| 35 | 9 | Rankings fast, locally adaptable, little calibration | Supported | p. 171 | Source credits Coe (2002) |
| 36 | 9 | Plackett-Luce trees on environmental or social covariates reveal G×E and help define TPEs | Supported | p. 172 | Source calls this one widely used approach. Optional Fix 5 |
| 37 | 9 | Nicaragua bean example, maximum night temperature split the data | Supported | p. 173, Figure 1 | Covariate is maxNT in vegetative and flowering periods, from van Etten et al. (2019) |
| 38 | 9 | Plackett-Luce regression adds linear covariates, including option-level trait, genomic, food-lab data | Supported | p. 173 | |
| 39 | 9 | Continuous data go to LMMs or GLMMs that partition variance and estimate heritability | Supported | p. 173 | |
| 40 | 9 | Joint ordinal-continuous models under development | Supported | p. 173 | Source: research ongoing (Dorado-Betancourt et al., 2026). Fix 4 adds context |
| 41 | 9 | Link trials to seasonal climate for location-specific recommendations | Supported | pp. 173 to 174 | |
| 42 | 9 | Synthesize rankings across trials | Supported | p. 174 | Brown et al. (2020) |
| 43 | 9 | Genomic relatedness raises predictive accuracy | Supported | p. 174 | de Sousa et al. (2021) |
| 44 | 9 | Results as probability of superiority over checks | Supported | p. 174 | Source: over current standards (Eskridge and Mumm, 1992) |
| 45 | 9 | On-station genotypic values as item covariates (potato in Rwanda) | Supported | p. 175 | Kang et al. (2025) |
| 46 | 9 | Instrumental lab data as item covariates (gari, a cassava product) | Supported | p. 175 | Alamu et al. (2023) |
| 47 | 9 | Future work: multi-level, multi-environment, multi-trait and genomic models | Supported | p. 176 | |
| 48 | 9 | ClimMob automatic report ranks options and compares selected variables | Supported | pp. 179 to 181 | |
| 49 | 9 | R-Instat: graphical interface for Plackett-Luce analysis and visualization | Supported | pp. 183 to 185 | |
| 50 | 9 | R-Instat: daily climate data as covariates | Supported | p. 184 | |
| 51 | 9 | Supported by IDEMS eCampus courses | Supported | p. 184 | |
| 52 | 9 | R suite: ClimMobTools (API), gosset (ranking analysis, trait prioritization, synthesis), climatrends (agroclimatic indices), chirps (CHIRPS and CHIRTS), PlackettLuce | Supported | pp. 186 to 187 | |
| 53 | 9 | Worked examples on bean trait prioritization and gari consumer testing | Supported | p. 187 | Source says "gari/eba" |
| 54 to 59 | Authors lines | Six Authors lines with their page ranges | Supported | See Metadata check | |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| 1. The Recruitment chapter is labelled as taken from the 2020 guide, but its paragraph on extension officers, group solidarity and a shared WhatsApp group is not in the 2020 guide text (searched van Etten et al. 2020a and 2020b). The claim that farmers in organized groups showed greater solidarity has no citation. | p. 137 | No | "The Recruitment chapter is marked as taken from the 2020 guide, but its paragraph on extension officers and WhatsApp groups is new, and its claim about group solidarity has no reference (PDF p. 137)." |
| 2. The chapter says observation questions always ask for best and worst in as few words as possible, but its own examples on the next page are full questions asking only for the best ("Which variety grows tallest?"). | pp. 156 to 157 | No | "The Observation chapter's example questions (PDF p. 157) do not follow its own short best-and-worst format (PDF pp. 156 to 157)." |
| 3. In "Data synthesis across trials", a full sentence and the next subheading ("Integration of genomic and biological information") are set as bullet points. A layout slip, no effect on content. | p. 174 | No | Not needed in the card. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Exception to usual management when testing practices | No | Medium | Fix 1 |
| Closing: possible at any time, documentation needed only for analysis, conflicts cannot be resolved after closing | Partly | Medium | Fix 3 |
| Rankings and measurements analysed in parallel, combined at interpretation | No | Medium | Fix 4 |
| Package preparation from two ClimMob download lists (randomized package list and QR code labels) | No | Low | "Packages are assembled from two ClimMob downloads, the randomized package list and the QR code labels." (PDF pp. 146 to 147) |
| Packages can be handed out at a group meeting or on individual visits | No | Low | Optional |
| Group trial members may later run their own trials | No | Low | Optional |
| Field agents may help farmers evaluate at the plot | No | Low | Optional |
| Mixed models partition variance into genotype, environment, farmer or location, and residual | Partly | Low | Card says "partition variance", enough |
| Two-level strategy: predict under controlled conditions, then translate to farmer conditions | No | Low | Optional |
| R-Instat workflow table (design, data collection, analysis, reporting) | No | Low | Not needed |

Aim, design, sample sizes, effect sizes and author limitations apply to the book as a whole and are covered by other parts. Part C chapters are procedural and methodological, and the card covers their main steps well.

## Template compliance

Skipped for part C, as set out in the reviewer note. Only part A checks the whole card's template. House style in part C: tricot is lowercase throughout. maniva does not appear.
