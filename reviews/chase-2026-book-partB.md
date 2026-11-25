# Card review: chase-2026-book (part B, section 3 Design)

- **Card:** papers/chase-2026-book.md, lines 99 to 163 (section 3, Design, including its practical guidance)
- **Source:** papers-pdf/chase-et-al-2026-tricot-book.pdf (315 pages). Part B covers PDF pages 42 to 135 (printed pages 39 to 132, so PDF page = printed page + 3).
- **Reviewed:** 2026-11-24, by an independent agent (part B of four)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 73 |
| Supported | 67 |
| Imprecise | 5 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 9 |
| Important omissions | 6 (none high, see Completeness) |
| Metadata issues | 0 (Authors line of section 3 matches all seven bylines) |

Section 3 is accurate and close to the book. Every number in the trial-size part (30 replicates, d of 0.7, the seed calculator's 120 / 360 / 72 / 79.2 kg, 467 farms, 100 to 200 farms) is correct. The most important fix is the bean protocol ranking list, which includes vigor, a trait the bean protocol does not contain (PDF 133 to 135). A second fix is the Nigerian example, which has seven social groups, not eight (PDF 50 to 51). The card does not flag the book's mixed guidance on minimum replicates (30, 20, and about 47 from the calculator).

## Fixes needed

1. **Bean ranking traits (3f).** Card: ranking pairs cover "germination, vigor, pest, disease and abiotic stress tolerance, yield, seed size, marketability, taste, storability and comparison with the local variety". Source: bean Table 3 (PDF 133 to 135) and Table 1 (PDF 118 to 121) have no vigor trait. They do have germination time and rate, maturity, leaf quality for consumption, seed size for target use, storage problems and overall preference, which the card leaves out. Replace with:
   > and ranking pairs cover germination time and rate, pest, disease and abiotic stress tolerance, maturity, yield, seed size (also for the target use or market), leaf quality for consumption, taste, marketability, storage problems, storability, overall preference and comparison with the local variety.

2. **Nigerian worked example (3b).** Card: "a worked example shows eight local social groups in a southwest Nigerian village and the ten participants selected." Source: Table 1 (PDF 50 to 51) lists seven groups, numbered i to viii with vi missing. Table 2 (PDF 51 to 52) shows the ten participants come from four of them (Yoruba, Agatu, Makurdi, Cotonou). Replace with:
   > and a worked example shows seven local social groups in a southwest Nigerian village (numbered i to viii, with vi missing), of which four were involved in cassava and supplied the ten participants selected.

3. **Traditional knowledge and ABS (3b).** Card: "farmers' knowledge may fall under rules on traditional knowledge". Source (PDF 55): farmers' perception skills are often seen as traditional knowledge, but the new knowledge produced in trials would usually not fall under national ABS laws. Rules on working with indigenous and local communities may still apply. The card also drops two details: check varieties are usually outside ABS rules in most countries, and SMTA material must be passed on under the same terms (PDF 54 to 55). Replace the whole sentence beginning "Using traditional varieties as checks" with:
   > Using traditional varieties as checks is usually outside ABS rules but may fall under national ABS law, depending on how the country defines utilization, or under the Plant Treaty's multilateral system (SMTA, with no monetary benefit-sharing obligation if the varieties are not bred, but any onward transfer must follow SMTA terms). The new knowledge farmers produce in trials would usually fall outside national ABS laws but may still be subject to rules on working with indigenous and local communities, so the book recommends following CBD and Nagoya principles as best practice and returning non-monetary benefits.

4. **Opening sentence of section 3.** Card: "Design is the core of the book and the chapter users will consult most." This is the card writer's judgement. The book does not say it. Replace with:
   > Design spans PDF pages 42 to 135, nearly a third of the book. The subsections below follow its parts.

5. **Attribution of crop plot-size findings (3c).** The potato, cassava and sweetpotato statements and the 30 m² / 100 vines recommendation are cited by the book from other works (Connolly 1993, Elias 2018, Gruneberg 2019, PDF 66). Only the Ghana plots come from tricot. Replace the sentence beginning "Interplot competition" with:
   > Interplot competition seems unimportant for yield in potato ridges (Connolly 1993, as cited), extends beyond the first row in cassava (Elias 2018, as cited) and is thought to be substantial in sweetpotato, where Gruneberg 2019 (as cited) recommends 30 m² plots with 100 vine cuttings on farm, but a Ghana tricot used 6 m² plots with 20 vines.

6. **ClimMob SOP templates and languages (3d).** Card: "in up to several languages" is unclear. Source: multilingual support (PDF 78 to 79), up to four languages per project (PDF 82), forms deployed with ODK (PDF 78). Replace the sentence with:
   > In ClimMob, choosing an SOP template configures the registration form, growth-stage modules and ranking questions as ODK forms for field agents, with multilingual support (up to four languages per project).

7. **Suggested additions (medium importance).** Paste where shown.
   - 3c, after the seed calculator sentence:
     > With its default inputs (Cohen's d of 0.7, 12 options) the sample-size calculator returns 187 participants and 561 plots, which is about 47 replicates per option (card's calculation), reflecting the larger samples that rankings need.
   - 3c, end of the multi-area paragraph:
     > The chapter says this range matches earlier on-farm cereal trials and that future studies should give better guidance on trial dimensions. Simulations show that with 3 replicates per environment, ranking data cannot estimate option-by-environment variation, while 18 replicates per environment can (read from a chart, approximate).
   - 3b, after the practical sequence:
     > Participants should represent local social groups roughly in proportion to their presence in the community and are chosen for tasks and skills rather than age.
   - 3b, end of the ethics paragraph:
     > The chapter also lists features ClimMob should provide, such as an auto-generated IRB request, short consent forms (signature, photo or audio) and automatic detection of personal information before data export.
   - 3f: change "early agronomic performance, maturity" to "early agronomic performance at 15 days, maturity at 40 days".

8. **Suggested Notes text for the replicate guidance (source issue, see below).**
   > The Design chapter gives mixed minimum-replicate guidance: aim for at least 30 replicates per option (PDF 57), rank estimates unreliable below 20 (PDF 61), and its own calculator returns about 47 per option for d = 0.7 with 12 options (PDF 59, card's calculation). 100 farms with 12 entries gives only 25 replicates per option.

## Metadata check

The frontmatter is checked by part A. Only the section Authors line and page range fall in part B.

| Field | Card | Source (page) | Status |
|---|---|---|---|
| Authors, Product management | Harish Gandhi, Agnes Mbugua Gitonga | Same byline (PDF 42) | Supported |
| Authors, Sampling | Béla Teeken, Jill Cairns, Mainassara Zaman-Allah | Byline has "Mainassara Abdou Zaman-Allah" (PDF 48) | Supported (middle name dropped, acceptable) |
| Authors, Trial size | Joost van Heerwaarden, Marie-Angélique Laporte | Same (PDF 57) | Supported |
| Authors, SOPs | Almendra Cremaschi, Marie-Angélique Laporte | Same (PDF 68) | Supported |
| Authors, Create a project | Acuña, Manrow, Madriz, with de Sousa | Byline has all four (PDF 80) | Supported |
| Authors, Trial documentation | Acuña, Manrow, Madriz | Same (PDF 91) | Supported |
| Authors, Bean protocol | Kauê de Sousa | Same (PDF 116) | Supported |
| Page range | PDF pages 42 to 135 | Design starts PDF 42, Recruitment starts PDF 136 | Supported |
| crops (SOP list) | 11 SOP crops | Resources chapter list (PDF 214) | Supported |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | 3 Authors | Chapter bylines | Supported | PDF 42, 48, 57, 68, 80, 91, 116 | See metadata table |
| 2 | 3 intro | Design is the core of the book and most consulted | Not in source | None | Card writer's judgement. Fix 4 |
| 3 | 3a | TPP is a blueprint of traits and benchmarks for one market segment | Supported | PDF 42 to 43 | |
| 4 | 3a | Standard template contents | Supported | PDF 43 | All eight items match |
| 5 | 3a | Essential traits split into improve and threshold, nice-to-have add edge | Supported | PDF 43 to 44 | |
| 6 | 3a | TPPs guide advancement, parent selection, market differentiation | Supported | PDF 44 to 45 | |
| 7 | 3a | Iterative refinement, groundnut concept testing in Tanzania | Supported | PDF 45 | |
| 8 | 3a | Segment neither too broad nor too narrow, multidisciplinary team | Supported | PDF 46 to 47 | |
| 9 | 3a | TPPs published on GloMIP | Supported | PDF 47 | Book: TPPs "can be accessed on GloMIP" |
| 10 | 3b | Power from replication across space and seasons, sampling captures who farms where | Supported | PDF 48 | |
| 11 | 3b | Criticism of demographic categories, equal gender numbers, people comfortable with researchers | Supported | PDF 48 | |
| 12 | 3b | Purposive task-group sampling, gender analysed afterwards | Supported | PDF 48 to 49, 53 | |
| 13 | 3b | Practical sequence of six steps incl. elite capture, compensation | Supported | PDF 49 to 50 | |
| 14 | 3b | Nigeria cassava, ten per community under self-chosen lead farmer | Supported | PDF 49 | |
| 15 | 3b | Worked example of eight groups and ten participants | Imprecise | PDF 50 to 52 | Seven groups listed (vi missing). Fix 2 |
| 16 | 3b | Teams prepared one to two months before planting material | Supported | PDF 51 | |
| 17 | 3b | Drop-outs replaced from similar groups | Supported | PDF 51 | |
| 18 | 3b | Lead-farmer trainings after installation, state level, four to five farmer-defined parameters | Supported | PDF 52 | |
| 19 | 3b | Short RHoMIS for every participant | Supported | PDF 52, 53 | Book: shortened core social questionnaire |
| 20 | 3b | tricot analyses rarely show strong gender differences, gender interacts with other variables | Supported | PDF 53 | |
| 21 | 3b | IRB and national clearance, GDPR, consent, withdrawal, opt-in naming | Supported | PDF 54 | |
| 22 | 3b | Check varieties, ABS law, Plant Treaty, SMTA with no monetary obligation | Supported | PDF 54 to 55 | Drops "usually outside ABS" and onward-transfer duty. Folded into Fix 3 |
| 23 | 3b | Farmers' knowledge may fall under traditional-knowledge rules | Imprecise | PDF 55 | New knowledge usually outside ABS laws, community rules may apply. Fix 3 |
| 24 | 3b | CBD and Nagoya as best practice, non-monetary benefits | Supported | PDF 55 | Book cites CGIAR Nagoya guidelines |
| 25 | 3c | Power rises with replicates per option | Supported | PDF 57 | |
| 26 | 3c | d = 0.7 at 95% needs about 30 replicates for measurements | Supported | PDF 57 | |
| 27 | 3c | Rankings need about twice as many | Supported | PDF 57 | |
| 28 | 3c | 30 replicates as minimum to aim for | Supported | PDF 57 | See source issue 3 |
| 29 | 3c | Plots = farms x 3 = options x n | Supported | PDF 58 | |
| 30 | 3c | Calculator based on Talsma 2018, blocks of 3, alpha and beta 0.05, no return rate | Supported | PDF 58 to 59 | |
| 31 | 3c | Seed calculator defaults give 120, 360, 72 kg, 79.2 kg | Supported | PDF 59 to 60 | Recomputed: 12 x 30 / 3 = 120, 360 x 0.2 = 72, x 1.1 = 79.2 |
| 32 | 3c | Effect sizes 0.7 to 1.0 agronomic, 0.2 to 0.5 consumer | Supported | PDF 58 to 59 | |
| 33 | 3c | 10 to 20 replicates per area, at least 10 per location | Supported | PDF 61 to 62 | |
| 34 | 3c | ClimMob designs sequentially balanced with equal farms per location | Supported | PDF 61 | |
| 35 | 3c | Prototype tool, shortest routes, 20 options x 7 locations = 467 farms, 67 per location | Supported | PDF 61 to 62, 65 | Recomputed: 20 x 70 / 3 = 466.7. See source issue 4 |
| 36 | 3c | 12 entries, 100 to 200 farms, 95% for d 0.7 to 1 | Supported | PDF 67 | |
| 37 | 3c | More farms for more environments and for attrition | Supported | PDF 67 | |
| 38 | 3c | Small plots let more and smaller farms join, variation but no bias | Supported | PDF 65 to 66 | |
| 39 | 3c | Not so small that edge effects dominate or material lacks for processing | Supported | PDF 66 | |
| 40 | 3c | Potato, cassava, sweetpotato competition, 30 m² vs 6 m² | Imprecise | PDF 66 | Content right, cited sources not named. Fix 5 |
| 41 | 3c | Seed by number not weight | Supported | PDF 66 to 67 | |
| 42 | 3d | SOPs validated, developed with breeding teams, comparable data | Supported | PDF 68 to 69 | |
| 43 | 3d | Value as practical, methodological, attributional, communicational | Supported | PDF 69 | Matches the bullets. See source issue 6 |
| 44 | 3d | SOPs embed consent and PII handling, fewer trial-by-trial clearances | Supported | PDF 70 | |
| 45 | 3d | Four shared elements plus optional consumer evaluation | Supported | PDF 70 to 73 | |
| 46 | 3d | Universal ranking traits | Supported | PDF 72 | |
| 47 | 3d | Millet and forage crop-specific traits | Supported | PDF 72 | |
| 48 | 3d | Leafy vegetables repeated harvest modules | Supported | PDF 72 | |
| 49 | 3d | Four development steps | Supported | PDF 76 to 77 | |
| 50 | 3d | Linked to Crop Ontology | Supported | PDF 77 | |
| 51 | 3d | Template configures forms "in up to several languages" | Imprecise | PDF 78 to 79, 82 | Unclear wording. Fix 6 |
| 52 | 3d | SOPs listed for 11 crops | Supported | PDF 214 | List is in the Resources chapter |
| 53 | 3e | Naming with Bean_Honduras_2019_season1 | Supported | PDF 80 | |
| 54 | 3e | Participants better slightly too high | Supported | PDF 81 | |
| 55 | 3e | Three options fixed, labels renameable | Supported | PDF 81 to 82 | |
| 56 | 3e | Project type, optional SOP, up to four languages | Supported | PDF 82 | |
| 57 | 3e | Options from library, drag questions, generate packages | Supported | PDF 84 to 88 | |
| 58 | 3e | Equal packages by default, rebalance, confirm or lose | Supported | PDF 88 to 89 | |
| 59 | 3e | QR-code labels and randomized package list | Supported | PDF 89 | Book: list of packages with QR codes plus Excel list |
| 60 | 3e | Eight forms, complete before analysis | Supported | PDF 91 to 92 | |
| 61 | 3e | Contents of the eight forms | Supported | PDF 92 to 115 | All details match |
| 62 | 3e | Multi-select, Other, Non-applicable | Supported | PDF 91 to 92 | Book: "most fields" are multi-select |
| 63 | 3e | Entry types list | Supported | PDF 95 to 96 | |
| 64 | 3f | Data-collection moments and intervals | Supported | PDF 117 to 121 | 15 and 40 day intervals not given (addition 7) |
| 65 | 3f | Registration variables | Supported | PDF 117 to 118, 122 | |
| 66 | 3f | Later moments record plot conditions, management, loss, disease, inputs, yield | Supported | PDF 118 to 121, 125 to 131 | |
| 67 | 3f | Ranking pairs list | Imprecise | PDF 133 to 135 | Vigor not in bean protocol. Fix 1 |
| 68 | 3f | Separate bean consumer SOP planned | Supported | PDF 116 | For non-tricot farmer consumers |
| 69 | Guidance | Write or adopt a TPP first | Supported | PDF 43 to 47, 76 | Reasonable inference |
| 70 | Guidance | Task groups, like-for-like replacement, RHoMIS | Supported | PDF 49 to 52 | |
| 71 | Guidance | At least 30 per option and 10 per location | Supported | PDF 57, 62 | |
| 72 | Guidance | Equal seed numbers, small plots, skip border rows | Supported | PDF 65 to 67 | |
| 73 | Guidance | Reuse SOP questions, complete eight forms | Supported | PDF 76, 91 | |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| 1. Social-group table numbering skips vi (seven groups). Caption says grey rows are the included groups, but the shading alternates. Hausa and Fulani are shaded though not involved, and Yoruba is not shaded though included. | PDF 50 to 51 | No (card says eight groups) | The Nigerian social-group table numbers groups i to viii but lists seven, and its grey shading does not match the caption. |
| 2. Figure 1 caption gives red for both quantitative and ranking data. The figure sits above its caption on the previous page. | PDF 62 to 63 | No (card not affected) | None needed |
| 3. Mixed minimum-replicate guidance: at least 30 (PDF 57), unreliable below 20 (PDF 61), calculator default about 47 per option (PDF 59). 100 farms with 12 entries gives 25 per option, below 30. | PDF 57, 59, 61, 67 | No | See Fix 8 |
| 4. 467 farms and 67 per location do not multiply (7 x 67 = 469). The figure says "n = 10/location = 70". 467 comes from 20 x 70 / 3 = 466.7, and 67 is 66.7 rounded. | PDF 62, 65 | No (rounding only) | None needed |
| 5. The Ghana sweetpotato 6 m² plot is called two thirds of the on-station plot size, but no on-station size is given. 6 m² is one fifth of the 30 m² on-farm recommendation. | PDF 66 | No (card leaves the clause out, which is right) | None needed |
| 6. SOP benefits are introduced as practical, methodological, ethical and communicational, but the bullets give scientific attribution instead of ethical. Ethics follows in a separate paragraph. | PDF 69 to 70 | No (card follows the bullets) | None needed |
| 7. SOP section says four core elements plus a fifth (consumer), but the headings number consumer as 4 and socio-economic as 5. | PDF 70 to 73 | No | None needed |
| 8. The bean protocol asks for the date farmers "plant the tubers", includes leaf-quality traits and a "Leaves used" question, and writes "Tolerance to a biotic stress" for abiotic. This looks copied from another crop template. | PDF 118, 119, 125, 133 | No | The bean protocol example contains wording carried over from other crop templates (tubers, leaf quality), so check the current bean SOP before reuse. |
| 9. "Types of projects" points to examples in a box below, but the PDF shows only a video still and an empty page. | PDF 82 to 83 | No | None needed |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim and parts of the Design chapter | Yes | High | None |
| Sample-size rules (30 replicates, twice for rankings, formulas) | Yes | High | None |
| Calculator default output (187 participants, 561 plots at d 0.7, 12 options) | No | Medium | Fix 7, first bullet |
| Authors' own limitation: future studies should give better guidance. 100 to 200 matches earlier cereal work. | No | Medium | Fix 7, second bullet |
| G x E needs many replicates per environment (Figure 2, 3 vs 18 per environment) | No | Medium | Fix 7, second bullet |
| Proportional representation of social groups, tasks over age | No | Medium | Fix 7, third bullet |
| ClimMob ethics features (IRB document, consent forms, PII detection) | No | Medium | Fix 7, fourth bullet |
| Mixed minimum-replicate guidance | No | Medium | Fix 8 (Notes) |
| SMTA onward-transfer duty, checks usually outside ABS | No | Low | Fix 3 |
| Bean intervals of 15 and 40 days | No | Low | Fix 7, last bullet |
| Several SOPs may exist for one crop (breeding vs seed-system) | No | Low | Optional: "One crop can have several SOPs, for example one for breeding with yield measurements and one for seed-system work with simpler criteria." (PDF 78) |
| Lead farmer training asks best and worst per parameter, then overall rank, in local languages | Partly | Low | None needed |
| Farmer check is essential for win rates, genotype metadata does not affect statistics | No | Low | Optional |
| Free-listing limits and pairwise alternatives | No | Low | None needed |

## Template compliance

Not checked by part B. Part A checks the whole card's template. House style in section 3: tricot is lowercase throughout, and maniva does not appear.
