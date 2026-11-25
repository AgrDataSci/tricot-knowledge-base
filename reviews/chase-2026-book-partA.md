# Card review: chase-2026-book (part A)

- **Card:** papers/chase-2026-book.md
- **Source:** papers-pdf/chase-et-al-2026-tricot-book.pdf (315 pages). Part A pages: PDF 1 to 41. Whole-book claims checked against the full text (/home/claude/work/txt/chase-et-al-2026-tricot-book.txt).
- **Part A scope:** frontmatter (lines 1 to 32), Questions, Summary, intro of "Chapter by chapter", chapter sections 1 and 2, Methods in brief, Stated limitations, Key numbers, Notes. Also the whole-card template check.
- **Reviewed:** 2026-11-24, by an independent agent (pilot)
- **Verdict:** Minor fixes

Page note: PDF page = printed page number + 3 in this part (printed page 1 is PDF 4). All pages below are PDF pages.

## Overview

| Check | Result |
|---|---|
| Claims checked | 122 |
| Supported | 104 |
| Imprecise | 12 |
| Not in source | 5 |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 9 |
| Important omissions | 0 high, 2 medium |
| Metadata issues | 3 (gist, keywords, author spelling), plus questions count under template compliance |

The part A sections are accurate on almost every number. All 31 Key numbers rows check out against the PDF. The most important fix is the Summary sentence that explains the 30-replicate minimum with the information loss of rankings. The source gives 30 replicates for a measured trait and asks for about twice as many with rankings (PDF 57). The Summary also adds partner institutions and the learn.climmob.net URL, which the PDF does not give. One claim in chapter 1 is contradicted: the inclusivity outcome has no citation (PDF 8). The card is also well over the template limits for keywords (26 against 8 to 12) and questions (11 against 4 to 7).

## Fixes needed

1. **Summary, 30-replicate sentence (meaning changes).** Card: "Aim for at least 30 replicates per option, since rankings carry about half the information of measurements, and at least 10 replicates per location." Source (PDF 57): about 30 replicates per option detect a Cohen's d of 0.7 in average yield with 95% probability. Rankings need about twice as many for equal power. Rank-based estimates are unreliable when n is too small, so 30 is the minimum to aim for. The card makes 30 sound like a number that already allows for rankings, but it is the number for measurements. Replace with:
   "Aim for at least 30 replicates per option, which detects a 0.7 standard-deviation difference in a measured trait with 95% probability. Rank-based estimates are unreliable below that, and rankings need about twice as many replicates for equal power. Aim also for at least 10 replicates per location."

2. **Chapter 1, outcomes sentence (Contradicted).** Card: "the claimed outcomes are greater crop diversity, faster adoption and more inclusive innovation, each backed by a cited paper rather than by new evidence in the book." Source (PDF 8): crop diversity cites Gotor et al. 2021 and adoption cites Occelli et al. 2024. The inclusivity claim and the claim about sustainable, climate-adaptive agriculture have no citation. Replace the sentence "Scaling and adaptation rest on ... in the book." with:
   "Scaling and adaptation rest on the method's simplicity. The claimed outcomes are greater crop diversity (citing Gotor et al. 2021), faster adoption (citing Occelli et al. 2024) and more inclusive innovation (no citation). The book presents no new evidence for them."

3. **Summary, first paragraph (Not in source).** The PDF gives no author affiliations, so "partners from CGIAR, IDEMS, Wageningen University, MrBot Software Solutions and national programmes" is outside knowledge. The URL learn.climmob.net does not appear anywhere in the PDF (the PDF only shows "Download the ... chapter as a PDF" links and "Version: current"). "The most complete and current guide" is the card's own judgment. Replace the whole first paragraph with:
   "This book is the current guide to tricot, written by the tricot team and partners under the 1000FARMS project (Gates Foundation) and BOLD WP7 (Norad through the Crop Trust). Each chapter can be downloaded as a PDF, and the book is versioned on Zenodo."
   If the affiliations and URL are wanted, put them in Notes, labelled as outside the PDF (see fix 13).

4. **Template: keywords.** 26 keywords against 8 to 12. Replace with:
   `keywords: tricot handbook, ten steps, target product profile, task groups, sample size, seed calculator, plot size, SOPs, trial documentation, ClimMob, Plackett-Luce, case studies`

5. **Template: questions.** 11 questions against 4 to 7. Replace the list with:
   - What is the current, complete guidance on running a tricot trial, step by step?
   - How do I set objectives, choose options and traits, and cost a trial?
   - How should participants be sampled to represent social, gender and task groups?
   - How many participants, replicates and locations, and how much seed and plot space, does a trial need?
   - What SOPs, metadata and ethics rules apply to a tricot trial in ClimMob?
   - How are tricot rankings analysed, and how do I give results back to farmers?
   - What have breeders and seed-sector practitioners in Africa learned from using tricot?

6. **Gist lists topics.** The current gist lists what the book covers, not what it shows. Replace with (27 words):
   `gist: Step-by-step tricot handbook with planning defaults (8 to 12 options, at least 30 replicates per option, 100 to 200 farms), ClimMob workflows and eight African case studies`

7. **Chapter 1, Authors and pages (Imprecise).** The byline "Jacob van Etten, Jonathan Steinke, Kauê de Sousa" belongs to the Introduction only (PDF 4). The ten-steps section has no byline and follows the Tricot Short Guide (PDF 14). The chapter runs to PDF 19: the ten-steps text ends on PDF 17, its figure is on PDF 18 and its reference on PDF 19. Replace with:
   "**Authors.** Introduction by Jacob van Etten, Jonathan Steinke and Kauê de Sousa. The ten-steps section has no byline and follows the Tricot Short Guide (van Etten et al. 2020). PDF pages 4 to 19."

8. **Stated limitations, gender (wording more certain than the source).** Card: "likely because gender interacts with social variables that are rarely measured." Source (PDF 53): "One reason may be" that gender interacts with income, occupation, migration status or ethnicity. Replace with:
   "- tricot analyses have not consistently detected strong gender differences in preferences. One possible reason is that gender interacts with social variables such as income, occupation, migration status or ethnicity, which are rarely measured."
   Matching tweak in not_established: "(tricot analyses have not consistently detected them, and the book suggests unmeasured social variables as one possible reason)".

9. **Stated limitations, free-listing (Imprecise).** Card: "reflect salience in discourse more than real trade-offs." Source (PDF 53): salience in discourse rather than relative importance in real decision-making. Trade-offs appear only in the next sentence, about pairwise methods. Replace with:
   "- Free-listing exercises reflect what is salient in discourse more than the relative importance of traits in real decisions."

10. **Stated limitations, last bullet (Not in source).** "Several chapters reuse 2020 guide material, and ClimMob features described are those at the time of writing" is a reviewer caveat. The authors do not state it. Delete it from Stated limitations and add to Notes:
    "- Several chapters reuse 2020 guide material, and the ClimMob features described are those of this version. This is a curator caveat, not a limitation the authors state."

11. **Summary, Feedback sentence (Imprecise).** "Redesigned" is not in the source. The feedback chapter is new text by Muller and Londoño (PDF 188), but the book does not call the workshop redesigned. Replace "Feedback describes a redesigned results workshop" with "Feedback describes a results workshop".

12. **Methods in brief, Structure (Imprecise).** The book has 13 downloadable chapters, and resources and case studies are two of them (PDF 4, 20, 42, 136, 144, 152, 155, 159, 171, 188, 201, 204, 275). The card counts them twice. Replace with:
    "- **Structure.** Thirteen chapters (an introduction, ten chapters for the ten tricot steps, resources and African case studies), plus FAQs, a Community of Practice page, tools in development and a glossary, written by specialist authors and partly reused from the 2020 guide."

13. **Notes, online version (Not in source).** "edited online at learn.climmob.net" is not in the PDF. Replace the bullet with:
    "- The book is versioned ("Version: current" on each chapter), so wording and numbers can change. The online site and the latest version are not named in the PDF (the online edition is at learn.climmob.net, from outside the PDF). Check the live site or Zenodo for the latest version."

14. **Notes, 467 farms (Imprecise).** 467 divided by 7 is 66.7, so "67 per location" is a rounded figure, not a contradiction. Replace the second sentence with:
    "The sampling-tool example gives 467 farms and 67 per location across 7 locations. 467 divided by 7 is 66.7, so the per-location figure is rounded (7 times 67 would be 469)."

15. **Notes, English-only (Imprecise, speculation).** "multilingual support likely postdates that trial" is the card's guess. The case study says the platform was only available in English, so extension officers translated for farmers (PDF 277). The setup chapter allows participant forms in up to four languages (PDF 82). These may refer to different things (interface versus forms). Replace the second sentence with:
    "The groundnut case study says ClimMob was only available in English, so extension officers translated for farmers (PDF 277). The setup chapter allows participant forms in up to four languages (PDF 82). The case study may refer to the software interface or to an earlier version, so check before citing either as current."

16. **Chapter 1, Seeds for Needs (Imprecise).** Card: "first implemented between 2013 and 2016 in the Seeds for Needs initiative". Source (PDF 5): "Much of this work" was part of Seeds for Needs. Replace with:
    "The method was first implemented and tested between 2013 and 2016, much of it in the Seeds for Needs initiative on cereals and grain legumes, then spread ..."

17. **Chapter 1, who recruits (Imprecise).** Card: "Field agents recruit farmers and collect data with ODK Collect." Step 3 (PDF 15) says implementers recruit farmers, and field agents are assigned to groups of farmers for setup and data collection. The checklist (PDF 37) gives recruitment to field agents (see Source issues). Replace with:
    "Implementers recruit farmers, and field agents support groups of farmers and collect data with ODK Collect."

18. **Summary, "The case studies close the book" (Imprecise).** After the case studies (PDF 275 to 301) come tools in development (PDF 302 to 304), the glossary (PDF 305 to 314) and a contact page. Replace with "A case-study chapter comes near the end." With fixes 1, 3, 11 and 18 together the Summary is 499 words, inside the 400 to 500 range.

19. **Chapter-by-chapter intro (Imprecise, low).** "reproduce van Etten et al. (2020) with light updates" cannot be checked: the bylines say "Taken from van Etten et al. (2020)" with a page number (PDF 23, 136, 144, 152, 155, 195, 201). Replace with:
    "Chapters marked "from the 2020 guide" carry the byline "Taken from van Etten et al. (2020)" with a page number, so cite the book for current practice and the guide for the original wording."

20. **Authors spelling (low).** The PDF spells "Muller, A." in the citation (PDF 3) and "Anna Muller" in the feedback byline (PDF 188). The card writes Müller. Keep Müller if that is the author's own spelling, but add to the first Notes bullet: "The PDF spells the name Muller, without the umlaut."

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Product testing with users in agriculture and food. Decentralized ... | Same, with a colon after "food" (PDF 3) | Supported (colon to period is expected) |
| authors | 22 names, Chase R first, van Etten J last | Citation lists 23 entries with Teeken twice, "Muller, A." (PDF 3) | Supported. Duplicate flagged in Notes. Umlaut differs (fix 20) |
| year | 2026 | 2026 (PDF 3) | Supported |
| journal | Bioversity International (book, 1st edition) | "1st ed., p. 298). Bioversity International" (PDF 3) | Supported |
| article | 1st ed., Montpellier, France | PDF 3 | Supported |
| type | book | Book with chapters (PDF 1 to 3) | Supported |
| peer_reviewed | no | No review statement | Supported |
| doi | 10.5281/zenodo.20042955 | PDF 3 | Supported |
| open_copy | https://learn.climmob.net | Not in PDF | Not checked (no web access) |
| license | see Zenodo record | No license statement in PDF | Supported (correct fallback). Not checked on Zenodo |
| data | none (links to calculators, SOPs, observation-card images, feedback package) | Calculators PDF 58 to 60, SOPs PDF 214, observation-card images and feedback package in Resources (PDF 256 to 261) | Supported |
| software | ClimMob 3, ODK Collect, Enketo, R-Instat, PlackettLuce, gosset, ClimMobTools, climatrends, chirps | PDF 27, 22, 183, 186 to 187 | Supported. CRAN versions not checked (no web access) |
| crops | many, with SOP list of 11 crops | SOP list PDF 214, crops PDF 5 | Supported |
| region | global, African case studies in 7 countries | Case-study list PDF 275 | Supported |
| keywords | 26 terms | Template asks 8 to 12 | Issue (fix 4) |
| gist | "The current tricot handbook, covering all ten steps ..." (25 words) | | Issue: lists topics (fix 6) |
| not_established | 4 items | Sample size defaults (PDF 58, 67), interviews (PDF 275), gender (PDF 53), practices (PDF 281) | Supported. Gender item slightly firmer than source (fix 8) |
| relations | updates vanetten-2020-guide, steinke-2016-guide, Occelli note | Bylines "Taken from van Etten et al. (2020)". FAQ cites Occelli (PDF 270) | Supported. The 28% figure needs the Occelli card, not checked here |

## Claim-by-claim check

### Summary

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| S1 | Summary | Most complete and current guide | Not in source | | Card's own judgment (fix 3) |
| S2 | Summary | Partners from CGIAR, IDEMS, WUR, MrBot, national programmes | Not in source | No affiliations in PDF | Outside knowledge (fix 3) |
| S3 | Summary | Under 1000FARMS (Gates) and BOLD WP7 (Norad via Crop Trust) | Supported | PDF 2 | |
| S4 | Summary | Online at learn.climmob.net, chapters downloadable as PDF | Not in source (URL) | Download links PDF 4, 20 etc. | URL not in PDF (fix 3) |
| S5 | Summary | Versioned on Zenodo | Supported | DOI and "Version: current" PDF 3 | |
| S6 | Summary | Conceived 2011, citizen science, use environments | Supported | PDF 4 | |
| S7 | Summary | Many small experiments with three random options answer a larger question | Supported | PDF 6, 7 | |
| S8 | Summary | Five defining features | Supported | PDF 6 | ClimMob named in next paragraph |
| S9 | Summary | Applications list incl. clonal crops, vegetables, cacao | Supported | PDF 5 | |
| S10 | Summary | Chapters follow the ten steps | Supported | PDF 14 | |
| S11 | Summary | Preparation contents incl. checklist | Supported | PDF 20 to 41 | |
| S12 | Summary | Design longest, its contents | Supported | PDF 42 to 135 (TPP 42, sampling 48, calculators 58 to 60, SOPs 68, setup 80, eight forms with DataCite, CRediT, GloMIP 92 to 94, bean 116) | Spot-checked. Details are parts B to D |
| S13 | Summary | Recruitment to observation reuse 2020 guide plus ClimMob how-tos | Supported | Bylines PDF 136 to 158 | |
| S14 | Summary | Compilation covers ODK, Enketo, closure | Supported | PDF 159 to 170 | |
| S15 | Summary | Analysis contents | Supported | PDF 171 to 187 | |
| S16 | Summary | "Redesigned" results workshop | Imprecise | PDF 188 | Fix 11 |
| S17 | Summary | Evaluation lists four indicators | Supported | PDF 202 | |
| S18 | Summary | Back matter contents | Supported | PDF 204, 262, 265, 302 to 303, 305 | |
| S19 | Summary | 8 to 12 options, at most ten criteria | Supported | PDF 20 to 21 | |
| S20 | Summary | At least 30 replicates "since rankings carry about half the information" | Imprecise | PDF 57, 63 | Fix 1 |
| S21 | Summary | At least 10 replicates per location | Supported | PDF 62 | |
| S22 | Summary | About 12 entries, 100 to 200 farms, 0.7 to 1 SD, 95% | Supported | PDF 67 | |
| S23 | Summary | Equal seed numbers, small plots, avoid edge effects | Supported | PDF 66 to 67 | |
| S24 | Summary | Workshops of at most 20 farmers about four weeks before planting | Supported | PDF 144 | Source says "before the start of the trial" |
| S25 | Summary | Case studies close the book | Imprecise | PDF 275 to 315 | Fix 18 |
| S26 | Summary | Eight practitioners from CIMMYT, One Acre Fund, TARI, Bayer, CIP, SARI, IITA, ISSD Ethiopia | Supported | PDF 275, 276, 279, 284, 287, 290, 292, 295, 298 | |
| S27 | Summary | Uses and constraints named | Supported | PDF 277 to 279, 281, 290 to 293, 297 to 298 | |

### Chapter-by-chapter intro and chapter 1

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| C1 | Ch intro | 2020-guide chapters reproduced "with light updates" | Imprecise | Bylines PDF 23, 136, 144, 152, 155, 195, 201 | Fix 19 |
| 1.1 | Ch 1 | Authors and PDF pages 4 to 17 | Imprecise | PDF 4, 14, 18, 19 | Fix 7 |
| 1.2 | Ch 1 | Citizen science, non-scientists generate and interpret data | Supported | PDF 4 | |
| 1.3 | Ch 1 | Addresses heterogeneity weakness of on-farm testing | Supported | PDF 4 | |
| 1.4 | Ch 1 | Use environments matter for external validity | Supported | PDF 5 | |
| 1.5 | Ch 1 | First implemented 2013 to 2016 in Seeds for Needs | Imprecise | PDF 5 | "Much of this work" (fix 16) |
| 1.6 | Ch 1 | Spread to sectors, applications and crops | Supported | PDF 5 | |
| 1.7 | Ch 1 | Novelty is the combination, supported by ClimMob | Supported | PDF 6 | |
| 1.8 | Ch 1 | Five uses listed | Supported | PDF 7 to 8 | |
| 1.9 | Ch 1 | On-farm testing links to environmental, socio-economic and DNA metadata | Supported | PDF 7 | |
| 1.10 | Ch 1 | Consumer testing of taste, cooking quality, shelf life | Supported | PDF 7 | |
| 1.11 | Ch 1 | Concept testing of practices, agroforestry designs | Supported | PDF 7 to 8 | Source also lists new varieties |
| 1.12 | Ch 1 | Scaling rests on simplicity | Supported | PDF 8 | |
| 1.13 | Ch 1 | Each outcome backed by a cited paper | Contradicted | PDF 8 | Inclusivity has no citation (fix 2) |
| 1.14 | Ch 1 | Ten steps listed | Supported | PDF 14 to 17 | |
| 1.15 | Ch 1 | Researchers set objectives, typically 8 to 12 options | Supported | PDF 14 | |
| 1.16 | Ch 1 | Implementers design in ClimMob, packages of three with QR codes | Supported | PDF 14 to 15 | |
| 1.17 | Ch 1 | Field agents recruit farmers | Imprecise | PDF 15, 37 | Fix 17 |
| 1.18 | Ch 1 | Blind planting, observation card, names, best options, certificates | Supported | PDF 15 to 17 | |
| 1.19 | Ch 1 | Joint evaluation each cycle | Supported | PDF 17 | |
| 1.20 | Ch 1 PG | Use ClimMob from the start | Supported | PDF 15 | |
| 1.21 | Ch 1 PG | Hide option names until data collected | Supported | PDF 15 | |
| 1.22 | Ch 1 PG | Iterative, refine option pool | Supported | PDF 17, 41 | |

### Chapter 2

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 2.1 | Ch 2 | Authors of each section | Supported | PDF 20, 23, 26, 27 | Checklist (PDF 36) has no byline, not mentioned. Fine |
| 2.2 | Ch 2 | PDF pages 20 to 41 | Supported | PDF 20 to 41 | |
| 2.3 | Ch 2 | Agronomic, social, climatic questions | Supported | PDF 20 | Source examples carry no citations |
| 2.4 | Ch 2 | Options solve local problems, focus groups | Supported | PDF 20 to 21 | |
| 2.5 | Ch 2 | Local check nearby or one of three, never fourth | Supported | PDF 21 | |
| 2.6 | Ch 2 | Aspects chosen with field agents and users, at most ten, overall plus open question | Supported | PDF 21 | |
| 2.7 | Ch 2 | ODK Collect on Android, Enketo as browser alternative | Supported | PDF 22 | |
| 2.8 | Ch 2 | Trial area matches target environment and TPP | Supported | PDF 22 | |
| 2.9 | Ch 2 | Who participates, subsistence vs market, processors and consumers | Supported | PDF 23 | |
| 2.10 | Ch 2 | Up to 25 farmers per field agent, 100 to 200 at first | Supported | PDF 23 to 24 | |
| 2.11 | Ch 2 | RHoMIS available in ClimMob | Supported | PDF 24 | |
| 2.12 | Ch 2 | Rewards, extra seed of preferred variety | Supported | PDF 24 | |
| 2.13 | Ch 2 | Two costing templates differ in seed multiplication | Supported | PDF 26 | |
| 2.14 | Ch 2 | Transparency, cross-country comparison, farm visits as cost driver | Supported | PDF 26 | |
| 2.15 | Ch 2 | Free, open-source, ClimMob 3 | Supported | PDF 27 | |
| 2.16 | Ch 2 | CBSE on ODK, ODK Tools, PyUtilib, R analysis | Supported | PDF 31 | |
| 2.17 | Ch 2 | Three user types | Supported | PDF 31 to 32 | |
| 2.18 | Ch 2 | Libraries, multilingual questions by 1000FARMS team | Supported | PDF 35 | |
| 2.19 | Ch 2 | Checklist assigns tasks to roles | Supported | PDF 36 to 41 | Also "All stakeholders" for planning next cycle |
| 2.20 | Ch 2 PG | 8 to 12 options, at most ten criteria with overall | Supported | PDF 20 to 21 | |
| 2.21 | Ch 2 PG | 100 to 200 farmers, within field-agent capacity | Supported | PDF 23 to 24 | |
| 2.22 | Ch 2 PG | Cost with the right template first | Supported | PDF 26 | Advice derived from text |

### Methods in brief, Stated limitations

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| M1 | Methods | Thirteen chapters plus resources, case studies ... | Imprecise | Chapter downloads PDF 4 to 275 | Double counts (fix 12) |
| M2 | Methods | Tools list | Supported | PDF 36, 58 to 60, 62, 214, 256 to 261 | |
| M3 | Methods | Crop Ontology, DataCite, CRediT, GloMIP, RHoMIS | Supported | PDF 76 to 77, 93 to 94, 53 | |
| M4 | Methods | Analysis list | Supported | PDF 171 to 187 | |
| L1 | Limitations | Rankings about half the information, unreliable with few replicates | Supported | PDF 57, 63 (effective sample size of half) | |
| L2 | Limitations | Calculator ignores return rates, numbers shrink over seasons | Supported | PDF 58, 67 | |
| L3 | Limitations | Better guidance awaits future studies | Supported | PDF 67 | |
| L4 | Limitations | Gender, "likely because" | Imprecise | PDF 53 ("One reason may be") | Fix 8 |
| L5 | Limitations | Free-listing vs "real trade-offs" | Imprecise | PDF 53 | Fix 9 |
| L6 | Limitations | Small plots do not suit every crop or trait | Supported | PDF 66 | |
| L7 | Limitations | Rankings hide trade-offs, software weaker on quantitative data | Supported | PDF 279, 290 to 291 | |
| L8 | Limitations | Practices harder than varieties in one case study | Supported | PDF 281 | |
| L9 | Limitations | Reused 2020 material, ClimMob at time of writing | Not in source | | Fix 10 |

### Key numbers

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| K1 | Key numbers | 2011 | Supported | PDF 4 | |
| K2 | Key numbers | 2013 to 2016 | Supported | PDF 5 | Book states the dates and cites van Etten 2019 for the progress report |
| K3 | Key numbers | 8 to 12 options | Supported | PDF 14, 21 | |
| K4 | Key numbers | At most 10 aspects, glossary 5 to 10 | Supported | PDF 21, 306 | |
| K5 | Key numbers | 4 to 5 parameters (Nigeria) | Supported | PDF 52 | Guide follows a Nigeria example. The link to Nigeria is by context |
| K6 | Key numbers | 10 participants per community | Supported | PDF 49 | |
| K7 | Key numbers | 1 to 2 months | Supported | PDF 51 | |
| K8 | Key numbers | About 30 replicates | Supported | PDF 57 | Could add "for a measured trait" |
| K9 | Key numbers | About 2 times with rankings | Supported | PDF 57 | |
| K10 | Key numbers | 0.7 to 1.0 / 0.2 to 0.5 | Supported | PDF 58, 59 | |
| K11 | Key numbers | 12 x 30, 120 participants, 360 plots | Supported | PDF 60 | Recomputed: 12 x 30 = 360, 360 / 3 = 120 |
| K12 | Key numbers | 72 kg (79.2 kg) | Supported | PDF 60 to 61 | Recomputed: 360 x 0.2 = 72, x 1.1 = 79.2 |
| K13 | Key numbers | 10 to 20 / at least 10 | Supported | PDF 61, 62 | |
| K14 | Key numbers | 467 farms, 67 per location | Supported | PDF 62 | 467 / 7 = 66.7 |
| K15 | Key numbers | 100 to 200 farms | Supported | PDF 24, 67 | |
| K16 | Key numbers | 6 m², 20 vines vs 30 m², 100 vines | Supported | PDF 66 | Grüneberg 2019 credited correctly |
| K17 | Key numbers | Up to 25 / 10 to 20 per field agent | Supported | PDF 24, 268, 307 | |
| K18 | Key numbers | 20 to 30 field agents | Supported | PDF 306 | |
| K19 | Key numbers | At most 20 farmers, about 4 weeks | Supported | PDF 144 | |
| K20 | Key numbers | 3 options fixed | Supported | PDF 81 | |
| K21 | Key numbers | Up to 4 languages | Supported | PDF 82 | |
| K22 | Key numbers | 8 documentation forms | Supported | PDF 92 | |
| K23 | Key numbers | 2 costing templates | Supported | PDF 26, 214 | |
| K24 | Key numbers | 60 to 90 / 90 to 150 days | Supported | PDF 120 | |
| K25 | Key numbers | 75 to 110 min, 20 to 25 people | Supported | PDF 188, 192 | |
| K26 | Key numbers | 5 to 7 per group | Supported | PDF 189 | |
| K27 | Key numbers | 4 indicators | Supported | PDF 202 | |
| K28 | Key numbers | About 25% cheaper, about 2 times farmers | Supported | PDF 270 | 28% from Occelli not checked here |
| K29 | Key numbers | 15 varieties and 15 lines | Supported | PDF 280, 292 | |
| K30 | Key numbers | 480 participants | Supported | PDF 303 | |
| K31 | Key numbers | About 170 USD vs 0.7 USD | Supported | PDF 302 | Source gives no citation for these costs |

### Notes

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| N1 | Notes | Teeken twice, 298 pages vs 315, concept DOI | Supported | PDF 3 | README version DOI not checked (no web access) |
| N2 | Notes | Versioned, edited at learn.climmob.net | Not in source (URL) | "Version: current" PDF 3 and each chapter | Fix 13 |
| N3 | Notes | Field agent load differs | Supported | PDF 24, 268, 307 | |
| N4 | Notes | n below 20 vs 30, and 467 vs 469 | Imprecise | PDF 57, 61, 62 | First half fine. Second half is rounding (fix 14) |
| N5 | Notes | Sweetpotato two thirds vs 30 m² on-farm | Supported | PDF 66 | 6 / 30 = one fifth |
| N6 | Notes | ClimMob cost differs, English-only "likely postdates" | Imprecise | PDF 271, 273, 277, 82 | Cost part fine. Language part is speculation (fix 15) |

Notes on Occelli 28% and Sikia integration rest on other cards. Not checked here.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Teeken listed twice in the citation | PDF 3 | Yes | |
| Citation gives 298 pages, PDF has 315 | PDF 3 | Yes | |
| Citation and byline spell "Muller" without umlaut | PDF 3, 188 | No | See fix 20 |
| Step 3 says implementers recruit farmers, the checklist gives recruitment to field agents | PDF 15, 37 | No | "The ten-steps overview gives recruitment to implementers, and the checklist gives it to field agents. In practice both are involved." |
| Field-agent load: up to 25 vs 10 to 20 | PDF 24, 268, 307 | Yes | |
| n below 20 vs minimum of 30 | PDF 57, 61 | Yes | |
| Figure 1 caption colours both series "red" | PDF 63 | No | "The trial-size Figure 1 caption gives the same colour (red) for quantitative and ranking data, so read the series from the plot." (part B may cover this) |
| Ghana sweetpotato plots called two thirds of the recommended size (6 m² is one fifth of 30 m²) | PDF 66 | Yes | |
| ClimMob free for anyone vs fee for private companies | PDF 271, 273 | Yes | |

## Completeness

For part A pages. Whole-book content is covered in parts B to D.

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim, structure, funding | Yes | high | |
| Five defining features, uses | Yes | high | |
| Ten steps and roles | Yes | high | |
| Number of farmers depends on the number of options (Step 3) | No | medium | Ch 1 summary: "The number of farmers needed depends on the number of options." (PDF 15) |
| ClimMob requirements: a computer to design, an Android phone or tablet for field data, and Excel-template upload as a fallback | Partly | medium | Ch 2 ClimMob paragraph: "Designing a trial needs a computer with internet, and field data collection needs an Android phone or tablet. Data can also be uploaded from Excel templates." (PDF 27 to 28) |
| Breeders value tricot for real-time market intelligence if participants are well characterized | No | low | Optional in Ch 1 (PDF 8) |
| Other data channels (interactive voice response, WhatsApp, Sikia coming) | No | low | Optional in Ch 2 (PDF 22) |
| ClimMob roadmap (audio, photos, sensor data, integration) | No | low | Optional (PDF 32) |
| Checklist extras: practical agronomy training at feedback, diffusion as an indicator | No | low | Optional (PDF 40 to 41) |
| Authors' own limitations | Yes | high | Wording fixes 8 to 10 |

## Template compliance

- Summary word count: 496 (target 400 to 500). With fixes 1, 3, 11 and 18 together: 499.
- Gist: 25 words, under 30, but lists topics instead of a finding (fix 6, 27 words).
- Keywords: 26, target 8 to 12 (fix 4).
- Questions: 11, target 4 to 7 (fix 5).
- House style: tricot and maniva lowercase throughout. No "Tricot" in the card. Long-format sections all present.
- Cross-part observation (not part A): the chapter 12 range "PDF pages 204 to 314" includes the case studies (PDF 275 to 301), which chapter 13 also claims.
