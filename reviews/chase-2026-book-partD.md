# Card review: chase-2026-book (part D)

- **Card:** papers/chase-2026-book.md, lines 222 to 268 (sections 10 Feedback, 11 Evaluation, 12 Resources, FAQs and back matter, 13 African crop case studies)
- **Source:** papers-pdf/chase-et-al-2026-tricot-book.pdf (315 pages), part D = PDF pages 188 to 315
- **Reviewed:** 2026-11-24, by an independent agent (pilot)
- **Verdict:** Minor fixes

Page note: printed page numbers in this part are 3 lower than PDF page numbers (printed 185 = PDF 188). All pages below are PDF pages.

## Overview

| Check | Result |
|---|---|
| Claims checked | 80 |
| Supported | 72 |
| Imprecise | 8 |
| Not in source | 0 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 6 |
| Important omissions | 2 (medium) |
| Metadata issues | 0 (frontmatter is outside part D) |

Part D of the card is accurate and close to the source. Every number in the case studies (15 maize varieties, one to three candidates, 15 groundnut lines) and in the feedback and FAQ sections (half a day, 20 to 25 people, 75 to 110 minutes, 5 to 7 per group, 0 to 10 score, 10 to 20 growers, 480 in the Sikia test) matches the book. The most important fix is the source of the Dissemination section. The card says it comes from the 2020 guide, but the text is from the 2020 RTB working paper (vanetten-2020-rtbwp), printed page 13 (PDF page 18 of van-etten-et-al-2020b.pdf). The rest are small wording and attribution fixes.

## Fixes needed

1. **Dissemination is from the RTB working paper, not the 2020 guide (Imprecise, attribution).** Card line 224 says "Dissemination from the 2020 guide." The book says "Taken from van Etten et al. (2020), page 13" (PDF 195), and its reference list for that section gives the RTB working paper "The tricot citizen science approach applied to on-farm variety evaluation" (PDF 196 to 197), not the guide. I checked both 2020 PDFs in papers-pdf/. The file-drawer and Kool et al. text is on printed page 13 of the RTB working paper (van-etten-et-al-2020b.pdf, PDF page 18). The 2020 guide (van-etten-et-al-2020a.pdf) has no such passage. The Evaluation chapter, by contrast, is from the guide (its "Indicators of success" box is in van-etten-et-al-2020a.pdf).
   Replace: `Dissemination from the 2020 RTB working paper (van Etten et al. 2020, vanetten-2020-rtbwp).`
   Also consider adding `vanetten-2020-rtbwp` to the card's relations if it is not there, and to the Notes: `- The Dissemination section is labelled "van Etten et al. (2020)" but reproduces the 2020 RTB working paper (vanetten-2020-rtbwp, page 13), not the 2020 guide. It updates the working paper's "forthcoming" Valle citation to Valle (2021) and adds a list of places to share data.`

2. **Section 12 authors miss the spousal letter credit (Imprecise).** Card line 242 says "Other sections unattributed." The resources chapter says the Spousal Information Letter was "Prepared by Emily Amondo" (PDF 259).
   Replace: `**Authors.** Community of Practice by Rachel Chase. Spousal information letter prepared by Emily Amondo. Other sections unattributed. PDF pages 204 to 274 and 302 to 315.`

3. **Section 12 page range overlaps section 13 (Imprecise).** Card line 242 gives "PDF pages 204 to 314". The case studies (section 13) are PDF 275 to 301, inside that range. The FAQs end on PDF 274, "Coming soon" runs PDF 302 to 304, the glossary PDF 305 to 314, and the contact page is PDF 315. Use the replacement in fix 2.

4. **"Any number of options above three" is stronger than the FAQ (Imprecise).** Card line 248. The FAQ says only that you "can include more than three technology options" (PDF 271). The glossary recommends 8 to 12 options for a first experiment and mentions pools of "up to 20" varieties (PDF 307, 313).
   Replace: `More than three options can be tested, since each grower receives a randomized subset of three from a larger pool (the glossary recommends 8 to 12 for a first experiment).`

5. **Ongom: duplicate uploads are not tied to poor training in the source (Imprecise).** Card line 266 says "Poorly trained field agents caused data problems, including duplicate uploads." The source says poorly trained agents caused technical issues with software and data capture (PDF 295). It lists duplicate uploads of one farmer's data separately, as a "user side" problem that ClimMob can fix (PDF 297 to 298).
   Replace: `Poorly trained field agents caused technical problems, so early supervision is needed, and some farmers' data were uploaded twice, which ClimMob can correct.`

6. **Tuyishime: zone maps and the narrowing to one to three candidates are two separate results (Imprecise).** Card line 261 says "zone maps narrowed the list to one to three candidates." The source describes maps of variety prioritization by zone, then, as a separate point, filtering the list down to one to three strong candidates (PDF 281).
   Replace: `rankings exposed grain size as a driver, zone maps showed which varieties to recommend where, and the long list was narrowed to one to three candidates for scaling.`

7. **Supporting-material images are not described as observation-card images (Imprecise, low).** Card line 246 says "downloadable observation-card images for beans, cassava, cacao, ...". The book calls them downloadable images that "illustrate traits, symptoms, and conditions" (PDF 215) and labels the crop "Cocoa" (PDF 225 to 229).
   Replace: `downloadable trait illustration images for beans, cassava, cocoa, cowpea, millet, potato, sorghum and soybean`

8. **Sikia test is wider than one trial, and the unit of n is not stated (Imprecise, low).** Card line 250 says "tested on a Tanzanian bean trial with 480 participants". The source says Sikia was "Tested on 1000FARMS tricot trials, including Tanzania bean (n=480)" and does not say what n counts (PDF 303).
   Replace: `tested on 1000FARMS tricot trials, including a Tanzanian bean trial (n = 480), where it picked up gendered preferences (women stressing taste, men yield and climate)`
   The Key numbers row "480 | Participants in the Tanzanian bean trial used to test Sikia" (line 321, outside part D) could read `n in the Tanzanian bean trial used to test Sikia (unit not stated)`.

9. **Kadege bullet misses her ClimMob quantitative-data limitation (omission, medium).** The Stated limitations line 284 credits weak quantitative data handling to the "case studies", but the summary gives it only for Daudi. Kadege says the same at more length (PDF 286).
   Add to the Kadege bullet: `Collecting and managing quantitative data, such as disease levels, was harder in ClimMob than rankings.`

## Metadata check

Frontmatter fields are checked by part A. Part D checked only the section Authors lines against the chapter bylines.

| Field | Card | Source (page) | Status |
|---|---|---|---|
| Section 10 authors, trial feedback | Anna Müller and Juan Manuel Londoño | Byline "Anna Muller, Juan Manuel Londoño" (PDF 188). The book spells her "Müller" in other reference lists, and people.md uses Müller | Supported (byline drops the umlaut, see Source issues) |
| Section 10 authors, dissemination | From the 2020 guide | "Taken from van Etten et al. (2020), page 13", text matches the RTB working paper (PDF 195) | Imprecise (fix 1) |
| Section 10 authors, project sharing | Sofía Acuña, Marilyn Manrow, Brandon Madriz | Same (PDF 199) | Supported |
| Section 10 pages | 188 to 200 | Feedback 188 to 194, Dissemination 195 to 198, Sharing 199 to 200 | Supported |
| Section 11 authors and pages | From the 2020 guide, 201 to 203 | "Taken from van Etten et al. (2020), page 27" (PDF 201), matches the guide | Supported |
| Section 12 authors | CoP by Rachel Chase, others unattributed | CoP byline Rachel Chase (PDF 262), spousal letter "Prepared by Emily Amondo" (PDF 259) | Imprecise (fix 2) |
| Section 12 pages | 204 to 314 | 204 to 274 and 302 to 315 | Imprecise (fix 3) |
| Section 13 authors | Daudi, Tuyishime, Kadege, Mwathi, Reuben Ssali, Oteng-Frimpong, Ongom, Hassena | Same eight names (PDF 275), byline spells "Reuban", interview heading "Reuben" (PDF 289) | Supported (source typo) |
| Section 13 pages | 275 to 301 | Chapter runs PDF 275 to 301 | Supported |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | 10 Authors | Trial feedback by Müller and Londoño | Supported | 188 | Byline lacks umlaut |
| 2 | 10 Authors | Dissemination from 2020 guide | Imprecise | 195 to 197, RTB WP p. 13 | Fix 1 |
| 3 | 10 Authors | Sharing by Acuña, Manrow, Madriz | Supported | 199 | |
| 4 | 10 Authors | PDF pages 188 to 200 | Supported | 188 to 200 | |
| 5 | 10 | Farmers are data producers and partners | Supported | 188 | |
| 6 | 10 | Feedback workshop of at least half a day | Supported | 188 | |
| 7 | 10 | About 20 to 25 people | Supported | 192 | |
| 8 | 10 | Agenda 75 to 110 min, welcome and recap of trial | Supported | 188 to 189 | Excludes travel and set-up |
| 9 | 10 | Feedback sheets handed over and explained | Supported | 189 | 20 to 25 min |
| 10 | 10 | Small groups of 5 to 7 by preferred option | Supported | 189 | |
| 11 | 10 | Group results stress no single best option | Supported | 189 | |
| 12 | 10 | Certificates and optional 0 to 10 usefulness score | Supported | 189 to 190 | Source calls it NPS |
| 13 | 10 | Next steps | Supported | 190 | |
| 14 | 10 | Field agents note farmers' comments | Supported | 190 | |
| 15 | 10 | ClimMob generates the feedback sheet | Supported | 190 | |
| 16 | 10 | Feedback package: templates, data frames, icons, manuals | Supported | 260 to 261 | |
| 17 | 10 | IITA state-level handbooks from Nigeria | Supported | 193 | |
| 18 | 10 | Open publication against file-drawer problem and poor documentation | Supported | 195 | |
| 19 | 10 | Standardized metadata including plot history, automated anonymization | Supported | 195 to 196 | |
| 20 | 10 | Repositories Dataverse, Zenodo, CGSpace | Supported | 196 | Also Fairgrounds, journals, 1000FARMS |
| 21 | 10 | Sharing with admin, editor, read-only member roles | Supported | 199 | Owner fixed |
| 22 | 11 Authors | From 2020 guide, PDF 201 to 203 | Supported | 201 | |
| 23 | 11 | Implementers, researchers, field agents review, farmers first | Supported | 201 | |
| 24 | 11 | Aim to include more farmers each cycle | Supported | 201 | |
| 25 | 11 | Lowest-ranked or poorly adapted options replaced | Supported | 202 | Source says "can discard" |
| 26 | 11 | Four indicators tracked in ClimMob | Supported | 202 | |
| 27 | 11 | Completed trials, weather vs management such as QR errors | Supported | 202 | |
| 28 | 11 | Gender balance relative to crop growers | Supported | 202 | |
| 29 | 11 | Share of returning farmers | Supported | 203 | |
| 30 | 11 | Intention to keep using an option | Supported | 203 | |
| 31 | 12 Authors | Others unattributed | Imprecise | 259 | Fix 2 |
| 32 | 12 Authors | PDF pages 204 to 314 | Imprecise | 204 to 274, 302 to 315 | Fix 3 |
| 33 | 12 | Main publications with links | Supported | 204 to 212 | |
| 34 | 12 | Video playlists: intro, ClimMob, R analysis | Supported | 213 to 214 | |
| 35 | 12 | Costing templates and guidelines | Supported | 214 | |
| 36 | 12 | Crop SOPs | Supported | 214 | |
| 37 | 12 | Observation-card images for eight crops | Imprecise | 215 to 256 | Fix 7 |
| 38 | 12 | tricot guidance sheet for farmers | Supported | 256 | |
| 39 | 12 | Spousal letter helps reach women in dual-adult households | Supported | 259 | |
| 40 | 12 | Farmer feedback package | Supported | 260 to 261 | |
| 41 | 12 | CoP is open Discourse forum with webinars, announcements, methods space | Supported | 262 to 263 | |
| 42 | 12 | Farmers need no smartphone, field agents do | Supported | 265 to 266 | |
| 43 | 12 | Ties not allowed, look again | Supported | 266 | |
| 44 | 12 | Disaggregation by GPS and environmental layers | Supported | 267 | |
| 45 | 12 | Local control by extra question or blind in pool | Supported | 267 to 268 | |
| 46 | 12 | Field agents care for 10 to 20 growers | Supported | 268 | Source says "might" |
| 47 | 12 | Any number of options above three | Imprecise | 271 | Fix 4 |
| 48 | 12 | Projects merge when they share at least one option | Supported | 273 | Also must test the same technology |
| 49 | 12 | ODK Collect offline, not on iOS | Supported | 273 to 274 | |
| 50 | 12 | Quarter cheaper than PVS, nearly twice the farmers | Supported | 270 | Source cites Occelli et al. 2024, card handles this in Key numbers and Notes |
| 51 | 12 | Open online course with certificate | Supported | 302 | |
| 52 | 12 | Sikia offline-first speech and image analysis of open-ended interviews | Supported | 302 to 303 | ASR and VLMs |
| 53 | 12 | Sikia tested on a Tanzanian bean trial, 480 participants | Imprecise | 303 | Fix 8 |
| 54 | 12 | Browser-based ClimMob registration app | Supported | 303 to 304 | PWA |
| 55 | 12 | Glossary terms listed | Supported | 305 to 314 | |
| 56 | 13 | Chapter consists of interviews | Supported | 275 | |
| 57 | 13 Daudi | CIMMYT, release proposal, product profile | Supported | 276 to 277 | |
| 58 | 13 Daudi | On-farm genetic gain, traits differ by zone | Supported | 278 | Zones in Tanzania |
| 59 | 13 Daudi | Seed, English-only software, weak quantitative data | Supported | 277, 279 | |
| 60 | 13 Tuyishime | One Acre Fund, up to 15 varieties in one season, fewer visits | Supported | 279 to 280 | |
| 61 | 13 Tuyishime | Blind testing raised curiosity, grain size as driver | Supported | 280 to 281 | |
| 62 | 13 Tuyishime | Zone maps narrowed list to one to three | Imprecise | 281 | Fix 6 |
| 63 | 13 Tuyishime | Practices harder than varieties | Supported | 281 | |
| 64 | 13 Kadege | TARI, yield, market acceptance, disease resistance | Supported | 283 to 285 | |
| 65 | 13 Kadege | Anthracnose varied by zone | Supported | 285 | |
| 66 | 13 Kadege | Women post-harvest, men agronomic, youth marketability | Supported | 285 | |
| 67 | 13 Kadege | Real-time ODK data, in-season corrections | Supported | 284 | |
| 68 | 13 Mwathi | Bayer, grain size and colour beyond yield | Supported | 287 | |
| 69 | 13 Mwathi | Farmers preferred a hybrid breeders rated lower, it entered the programme | Supported | 287 to 288 | Source: not "the best by their own internal criteria" |
| 70 | 13 Mwathi | Two areas assumed similar proved different | Supported | 288 | |
| 71 | 13 Ssali | CIP, more farmers regardless of education | Supported | 289 | |
| 72 | 13 Ssali | Validated survey-based priorities, mealiness accepted | Supported | 290 to 291 | |
| 73 | 13 Ssali | Multiply before trial, trade-offs not revealed | Supported | 290 | |
| 74 | 13 Oteng-Frimpong | SARI, 15 lines, previously inaccessible farmers | Supported | 292 | 15 lines is the current trial |
| 75 | 13 Oteng-Frimpong | Women prefer early maturity, seed size, colour, fast maturity in profiles | Supported | 293 | |
| 76 | 13 Oteng-Frimpong | Off-season seed multiplication, translation by field agents | Supported | 293 to 294 | |
| 77 | 13 Ongom | IITA, grain colour, seed size, pest and disease resistance, release, market classes | Supported | 295 to 296 | |
| 78 | 13 Ongom | Poor training caused duplicate uploads | Imprecise | 295, 297 to 298 | Fix 5 |
| 79 | 13 Hassena | ISSD Ethiopia, isolated farmers, local partners, familiarity before release | Supported | 275, 298 to 300 | Ethiopia is only in the chapter's link list |
| 80 | 13 Hassena | Companies may resist, renaming confuses farmers | Supported | 299 to 300 | |

Key numbers rows tied to part D pages (card lines 316 to 322, outside part D's line range) were also checked: 75 to 110 min for 20 to 25 people (PDF 188, 192), 5 to 7 per group (189), 4 indicators (202), 15 varieties and 15 lines (280, 292), ~170 USD vs 0.7 USD (302) are Supported. The 480 row is covered in fix 8. The PVS row is Supported, with the 28% figure from occelli-2024-agecon not checked here.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Dissemination says "van Etten et al. (2020), page 13" without saying which 2020 document. The text and reference list point to the RTB working paper, while the Evaluation chapter cites the guide under the same author-year | 195 to 197, 201, 203 | No | See fix 1 |
| ClimMob cost: free for CGIAR and NARES with a fee for private companies, versus free for anyone | 271, 273 | Yes (Notes) | None needed |
| Byline spells "Anna Muller", other references and people.md use "Müller" | 188 | No | Optional. The card's spelling is right |
| Byline spells "Reuban Ssali", the interview heading and text use "Reuben" | 275, 289 | No (card uses Reuben, correctly) | None needed |
| Kadege's associated paper is dated 2026 but given volume 9 and a 2025 DOI | 283 | No | Leave to the kadege-2026-fsufs card reviewer |
| TARI expanded as "Tanzania Research Institute" (usually Tanzania Agricultural Research Institute) | 284 | No | Low importance. Card uses only "TARI", which is safe |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Kadege: quantitative data (disease levels) hard to handle in ClimMob | No (only Daudi) | Medium | Fix 9 |
| Budget team time and money for feedback workshops from the start, and debrief afterwards | No | Medium | Add to section 10: `Teams should budget time and money for feedback workshops from the start and debrief afterwards to improve the next trials.` |
| Sikia result: women stressed taste, men yield and climate | No | Low | Included in fix 8 |
| Ongom: tricot used at both late and early breeding stages | No | Low | Optional: `tricot is used mainly at late stages but also earlier.` |
| Ssali: rankings give statistics release committees value and can show why released varieties are rejected | No | Low | Optional |
| Mwathi: grain size and colour were integrated into the breeding programme | Partly | Low | Optional: `and both traits were added to the breeding programme` |
| Hassena: farmer-led multiplication seen as a way to spread varieties, with quality monitored | No | Low | Optional |
| FAQ: ClimMob created by Jacob van Etten, now led by Kauê de Sousa | No | Low | None needed |

## Template compliance

Not checked for part D (part A checks the whole card's template). In part D, tricot and maniva are lowercase throughout, including the start of the Daudi bullet ("tricot data supported...").
