# Card review: muller-2025-ux

- **Card:** papers/muller-2025-ux.md
- **Source:** papers-pdf/muller-et-al-2025.pdf (26 pages, slide deck)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

Page numbers below are the printed slide numbers. They match the PDF page numbers except PDF page 24, which is also printed "23". This report writes that page as "p. 24 (printed 23)".

## Overview

| Check | Result |
|---|---|
| Claims checked | 42 |
| Supported | 33 |
| Imprecise | 8 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 6 |
| Important omissions | 8 |
| Metadata issues | 4 |

Most single claims in the card match the slides. But the card leaves out a main result: farmers found the sheet only moderately easy to understand (median 3 of 5, slide 19). It also presents the 48% icon figure as a share of farmers, when it comes from a 12-farmer icon test where matching reached 72 to 75%. It copies two numbers the slides themselves get wrong (34 of 44 is 77%, not 70%, and the farmers' NPS chart counts add up to 32, not 44). Summary paragraph 5 mostly repeats paragraph 4, and that space should hold the missing results. The most important fix is to add the understanding result and to restate the icon result with its 12-farmer basis (pp. 19, 23).

## Fixes needed

1. **Add the ease-of-understanding result and correct the icon claim (Summary, gist, Key numbers).** The card says only that farmers valued the sheet and that "only 48% of farmers decoded trait icons correctly". The source answers its question 3b "Do farmers understand the visualizations?" with "Partially": the median was 3, 14 farmers (32%) chose 3, 10 (23%) chose 1 or 2, and 20 (45%) chose 4 or 5, before any explanation (p. 19). The icon test used 12 farmers. Free description matched 50% (figurative) and 47.2% (abstract), and matching icons to labels succeeded 71.5% and 75.0% (p. 23). The 48% appears only in the conclusions (p. 24, printed 23). Replace the whole Summary with the text in fix 2, the gist with fix 3, and the Key numbers with fix 6.

2. **Rewrite the Summary so it covers the missing results and drops the repeated paragraph.** Paragraph 5 repeats the research questions, the trust conclusion and the next fixes already given in paragraph 4. Several statements are also imprecise: the design requirements omit trait and planting information, ClimMob extraction and short meeting time (p. 8), the sheet modules omit personal rankings and trait rankings (p. 11), and "trust in ... the trial" should be "quality of the data" (p. 24, printed 23). Suggested replacement (498 words):

   > The deck reports the redesign and field validation of tricot farmer feedback, following the 2024 review (schumann-2024-ux). Implementers had not used the old feedback form systematically. Co-design sessions set the requirements. Farmers needed the ranking of their own varieties, trait and planting information, next steps and seed availability, icons and visuals, room for discussion, and local languages. Implementers needed materials that are cheap and easy to produce, easy to extract from ClimMob data, and fit a short meeting.
   >
   > The tested feedback sheet had modules for the farmer's personal information, personal, regional and overall variety rankings, trait rankings, recommendations from implementers on planting and managing varieties, and contacts. A separate diploma recognized participation. Validation ran in Nigeria with NRCRI and IITA on a cassava trial of eight varieties, with 44 farmers in ten communities across five states (Oyo, Osun, Abia, Imo and Akwa Ibom) and sessions in Yoruba, Igbo and English.
   >
   > Before any explanation, 34 of 44 farmers rated the sheet's usefulness 4 or 5 out of 5 (the slides say about 70%), and no one chose 1. Ease of understanding was only partial. The median score was 3, 45% scored 4 or 5 and 23% scored 1 or 2. Overall, 67% could discuss at least one section accurately. After exploring the sheet and discussing it in groups, farmers gave a Net Promoter Score of 70.45 (excellent). The six implementers gave 33.3 (good), with four passives and no detractors. Icons were the weak point. In a test with 12 farmers, free descriptions matched the intended trait 47 to 50% of the time, and matching icons to labels succeeded 72 to 75% of the time. Icons for visible traits such as gari and eba quality scored above 4 out of 5, while root yield, disease resistance and early root formation scored below 3. Farmers had not expected a diploma, but once they received it they valued it and asked for larger, framed versions.
   >
   > Implementers said the sheet let them talk less, condensed twelve months of data, and could serve as documented proof for the variety release committee that farmers were at the center. In sessions, farmers grouped themselves by their top-ranked variety, recalled the trial in detail and treated the sheet as their own. Men spoke more than women, and talk about next steps drifted to past results, possibly because of the long gap since the trial. Sheets were damaged by folding, fonts were too small, machine translation of Yoruba and Igbo was not good enough, and printing and signatures caused budget and timing problems. Adding user research tasks made sessions tiring for implementers.
   >
   > The authors conclude that the redesigned sheet is largely effective, that the diploma matters, and that sessions strengthen trust in the institutions and in the quality of the data. Icons, durable materials and faster production need more work. Next steps are to polish the icons, translate sheets at scale, automate one-click sheet generation from ClimMob, train facilitators, and test the package in other countries and crops.

   Sources for the new content: p. 2 (old form not used), p. 8 (requirements), p. 11 (modules), p. 14 (fieldwork), pp. 18 and 19 (scales), p. 21 (session dynamics, gender, timing, durability), p. 22 (NPS, implementer fatigue), p. 23 (icons), p. 19 (translation, fonts), pp. 16 and 17 (printing, signatures), p. 24 printed 23 (conclusions), p. 25 (next steps).

3. **Replace the gist.** "Only half decoded the trait icons" reads as half of the 44 farmers, but the icon test had 12 farmers and matching reached 72 to 75% (p. 23). The gist also hides that understanding was only moderate (p. 19). Suggested gist (29 words):

   `gist: Nigerian cassava field test of a redesigned tricot feedback sheet and diploma, which 44 farmers found useful (NPS 70), though understanding was moderate and trait icons were often misread`

4. **Add a not_established field.** It is missing. Suggested text:

   `not_established: That farmers understand the sheet without facilitation; that 48% of all 44 farmers misread the icons (the icon test had 12 farmers); that the design works for other crops, countries or languages; that feedback sessions raise variety adoption or seed uptake; that a variety release committee has used the sheets as evidence; that the implementer score represents implementers in general (six implementers)`

5. **Relabel the Note on BOLD WP7 as outside knowledge.** The deck shows the Crop Trust, 1000FARMS, CGIAR and Alliance logos on every slide but never names BOLD, WP7 or opportunity crops (pp. 1 to 26). Suggested replacement:

   `- Outside the source: this work is understood to be part of the BOLD WP7 project supported by Crop Trust, which aims to increase adoption of opportunity crops in Africa. The deck itself shows only the Crop Trust, 1000FARMS, CGIAR and Alliance logos and does not name BOLD.`

6. **Correct and extend Key numbers.** Replace the 70%, 48% and 33.3 rows and add four rows:

   | Number | Context | Primary source |
   |---|---|---|
   | 34 of 44 (77%) | Farmers rating sheet usefulness 4 or 5 out of 5, before explanation. The slides print about 70%, but 34/44 is 77% (card's calculation) | This presentation |
   | Median 3, 45%, 23% | Ease-of-understanding scale before explanation: median score, share scoring 4 or 5, share scoring 1 or 2 (44 farmers) | This presentation |
   | 12 farmers | Participants in the trait icon test (free description, then matching icons to labels) | This presentation |
   | 47.2% and 50% | Icon free description matching the intended trait, abstract and figurative styles | This presentation |
   | 71.5% and 75.0% | Icon matching to trait labels, figurative and abstract styles | This presentation |
   | 48% | Trait icon decoding rate given in the conclusions, close to the free description rates above. Not a share of all 44 farmers | This presentation |
   | 33.3 | Implementers' Net Promoter Score, from 6 implementers (2 promoters, 4 passives, 0 detractors) | This presentation |

7. **Add a Notes item on the source's own number problems.** Suggested text:

   `- Number problems in the source. Slide 18 says 34 of 44 farmers (about 70%) rated usefulness 4 or 5, but 34/44 is 77%, and the 70% is repeated in the conclusions. The farmers' NPS chart on slide 22 shows counts that add up to 32 (2, 2, 1, 5, 5 and 17 for scores 5 to 10), while the printed shares (4.5%, 20.5%, 75%) and the score of 70.45 fit 44 farmers. With the chart counts the score would be 56.3. Slide 23 says elaborate pictograms beat simpler ones in every aspect, but the abstract style had the higher matching rate (75.0% versus 71.5%) and the lower-row icons scored higher for root yield and disease resistance. Read off the slides, these figures are approximate.`

8. **Fix the Methods "Design" bullet and the Metrics bullet.** The source says co-design sessions were held with colleagues and tricot implementers, after interviews with implementers (p. 4). It does not say farmers took part in co-design. Suggested replacements:

   `- **Design.** Human-centered design roadmap (scope, explore, create, validate, implement). Requirements from interviews and co-design sessions with colleagues and tricot implementers. Modular feedback sheet plus participation diploma.`

   `- **Metrics.** Usefulness and ease-of-use scales (dots on a wall chart, before explanation), share of farmers able to discuss a section, icon test with 12 farmers (free description, then matching icons to trait labels), Net Promoter Score for 44 farmers and 6 implementers (after discussion), qualitative observation and implementer interviews.`

9. **Rewrite Stated limitations.** The authors do not call the sample small. They list cross-context testing as a next step (p. 25). They also state several other limitations that the card leaves out. Suggested replacement:

   ```
   - Validation covered one crop (cassava) in one country. The authors plan tests in other countries and crops.
   - Icon comprehension was low for several traits and icons need redesign.
   - Producing durable materials quickly remains a constraint. Sheets were damaged by folding.
   - Adding user research tasks to the feedback meeting made it longer and tiring, which kept several implementers neutral.
   - The long gap between trial and session pushed discussion toward past results instead of next steps.
   - Participation was gender-skewed, with men speaking more.
   - Machine translation of Yoruba and Igbo was not accurate enough, and font size and accessibility need revision.
   ```

10. **Title.** The printed title capitalizes "Tricot" and uses "&" and a spaced hyphen (p. 1). The repository rule is to quote titles exactly as printed. The colon becoming a period is expected. Suggested:

    `title: Farmer Feedback in Tricot. Redesigning the Tricot feedback process & field validation 2024 - 2025`

11. **License wording.** No license is printed in the PDF. The template wording is "see CGSpace record". Suggested: `license: see CGSpace record`. The handle page could not be opened from this environment, so the license, year and title on the repository record were not checked.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Farmer feedback in tricot. Redesigning the tricot feedback process and field validation 2024–2025 | "Farmer Feedback in Tricot", "Redesigning the Tricot feedback process & field validation 2024 - 2025" (p. 1) | Imprecise (case, "&" and dash changed. Colon to period is expected) |
| authors | Müller A, Schumann C, Londoño JM | Dr. Anna Müller, Dr. Charlotte Schumann, Juan M. Londoño (p. 1) | Supported |
| year | 2025 | Title range 2024 to 2025, fieldwork May 2025 (pp. 1, 11). Repository date not checked | Supported |
| journal | Alliance ..., UX Research and Inclusive Design (presentation) | "UX Research & Inclusive Design, Alliance Bioversity-CIAT" (p. 1) | Supported |
| article | validation slides | Slide deck | Supported (descriptor only) |
| type | presentation | Slide deck (pp. 1 to 26) | Supported |
| doi | hdl.handle.net/10568/179807 | Not printed in the PDF. Handle page blocked from this environment | Not checked |
| license | see repository record | No license printed in the PDF | Issue: use template wording "see CGSpace record" |
| data | none | No dataset cited | Supported |
| crops | cassava (validation) | Cassava trial, diploma "new varieties of Cassava" (pp. 11, 12) | Supported |
| region | Nigeria (Oyo, Osun, Abia, Imo, Akwa Ibom) | Five states (p. 14) | Supported |
| gist | ... rated highly by 44 farmers (NPS 70) though only half decoded the trait icons | Icon test had 12 farmers, matching 72 to 75% (p. 23). Understanding only partial (p. 19) | Imprecise |
| not_established | missing | | Missing (metadata issue) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Deck reports redesign and field validation of tricot feedback, following the 2024 review | Supported | Title (p. 1), roadmap with prior research review (p. 4) | Cross-reference to schumann-2024-ux is fine |
| 2 | Summary | Design requirements: rankings and seed availability, icons, discussion, local languages, cheap and easy | Imprecise | p. 8 | Omits trait and planting information, next steps, ClimMob extraction and short meeting time. "Seed availability" is a fair reading of "availability issue" |
| 3 | Summary | Sheet modules: personal info, overall and regional rankings, recommendations, communication channels | Imprecise | p. 11 | Omits personal rankings and the traits ranking module |
| 4 | Summary | Separate participation diploma recognized contribution | Supported | pp. 12, 17 | |
| 5 | Summary | Validation in Nigeria with NRCRI and IITA, cassava trial of eight varieties | Supported | pp. 3, 11, 12 | "8 Varieties Tested" appears on the sample sheet |
| 6 | Summary | 44 participants, ten communities, five states, three languages | Supported | p. 14 | Community counts add to 44 (checked) |
| 7 | Summary | Farmers valued the sheet | Supported | pp. 18, 22 | |
| 8 | Summary | 70% rated usefulness 4 or 5 | Supported | p. 18, p. 24 (printed 23) | Matches the slide, but 34/44 is 77%. See Source issues |
| 9 | Summary | No one chose the lowest score | Supported | p. 18 | |
| 10 | Summary | 67% could accurately discuss at least one section | Supported | p. 24 (printed 23) | Only in the conclusions. No slide shows how it was measured |
| 11 | Summary | Farmers' NPS 70.45, excellent | Supported | p. 22 | See Source issues on chart counts |
| 12 | Summary | Implementers' NPS 33.3, good but room to improve | Supported | p. 22 | n = 6 not given in card |
| 13 | Summary | Icons remained the weak point | Supported | p. 24 (printed 23) | |
| 14 | Summary | Only 48% of farmers decoded trait icons correctly | Imprecise | pp. 23, 24 | Icon test had 12 farmers. 48% is a decoding rate, not a share of farmers. Matching reached 71.5 to 75% |
| 15 | Summary | Elaborate pictograms worked better than simple ones | Supported | p. 23 | Matches slide text, but the slide data do not fully support it. See Source issues |
| 16 | Summary | Icons for visible everyday traits clearest | Supported | p. 23 | Scores above 4 for gari, eba and canopy |
| 17 | Summary | Diploma not expected, then valued, larger framed versions requested | Supported | p. 17 | |
| 18 | Summary | Sheet let implementers talk less because farmers grasped information | Supported | p. 16 | One implementer quote |
| 19 | Summary | Condensed twelve months of data | Supported | p. 16 | Quote |
| 20 | Summary | Documented proof for the variety release committee that farmers were at the center | Supported | p. 16 | Merges two quotes and a heading. Acceptable |
| 21 | Summary | Sessions strengthened trust in the institutions and the trial | Imprecise | p. 24 (printed 23) | Source says trust in the institutions and in the quality of the data |
| 22 | Summary | Sheet largely effective, icons and robustness and speed need work | Supported | p. 24 (printed 23) | |
| 23 | Summary | Mixed methods, list of research questions | Supported | p. 15 | Omits question 5 (usability and usefulness). Minor |
| 24 | Summary | Single sheet simplified transport and reduced costs | Supported | p. 16 | |
| 25 | Summary | Sessions build trust in institutions and quality of the trial | Imprecise | p. 24 (printed 23) | Same issue as claim 21, and repeats it |
| 26 | Summary | Icon design and faster production of durable materials are next to fix | Supported | pp. 24, 25 | |
| 27 | Summary | Part of an inclusive design effort within the Alliance | Supported | pp. 1, 3 | |
| 28 | Methods | Requirements from co-design with farmers and implementers | Imprecise | p. 4 | Co-design was with colleagues and tricot implementers, after implementer interviews |
| 29 | Methods | 10 communities, 5 states, 44 farmers, 3 languages | Supported | p. 14 | |
| 30 | Methods | Usefulness and ease-of-use scales, comprehension and matching rates, NPS, observation | Supported | pp. 15, 18, 19, 22, 23 | Missing the 12-farmer icon test and timing of measures |
| 31 | Limitations | Small sample (44 farmers), one country and crop | Imprecise | p. 25 | Authors do not call the sample small. They plan tests in other countries and crops |
| 32 | Limitations | Icon comprehension low, needs redesign | Supported | pp. 23, 24 | |
| 33 | Limitations | Producing durable materials quickly is a constraint | Supported | pp. 21, 24 | |
| 34 | Key numbers | 44 farmers | Supported | p. 14 | |
| 35 | Key numbers | 10 communities, 5 states | Supported | p. 14 | |
| 36 | Key numbers | 8 varieties | Supported | p. 11 | |
| 37 | Key numbers | 70% usefulness 4 or 5 | Supported | p. 18 | Slide's own number. 34/44 = 77% |
| 38 | Key numbers | 67% discuss at least one section | Supported | p. 24 (printed 23) | |
| 39 | Key numbers | 48% farmers decoding icons | Imprecise | pp. 23, 24 | Context wrong: 12-farmer icon test, a decoding rate |
| 40 | Key numbers | Farmers' NPS 70.45 | Supported | p. 22 | |
| 41 | Key numbers | Implementers' NPS 33.3 | Supported | p. 22 | Add n = 6 |
| 42 | Notes | BOLD WP7, Crop Trust, opportunity crops in Africa | Not in source | Logos only (pp. 1 to 26) | Crop Trust logo is present. BOLD, WP7 and the goal are outside knowledge and must be labelled so |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| "34 of the 44 farmers (≈ 70 %)" but 34/44 = 77.3%. The 70% is repeated in the conclusions | p. 18, p. 24 (printed 23) | No | See fix 7 |
| Farmers' NPS chart counts (2, 2, 1, 5, 5, 17 for scores 5 to 10) add to 32, while the printed 4.5%, 20.5%, 75% and NPS 70.45 fit 44 farmers (2 detractors, 9 passives, 33 promoters). Chart counts would give 56.3. The axis also prints "4" where "1" belongs | p. 22 | No | See fix 7 |
| "Elaborate pictograms perform better than simpler ones in every aspect" is not borne out: abstract style matched better (75.0% vs 71.5%), and lower-row icons scored higher for root yield (1.9 vs 1.3) and disease resistance (2.8 vs 1.6). The slide does not say which row is "elaborate" | p. 23 | No | See fix 7 |
| Below-ground or abstract traits said to score 2 or less, but disease resistance scored 2.8 and early root formation 2.4 in one style | p. 23 | No | Optional: "Slide 23 says below-ground traits scored 2 or less, but two of those icons scored 2.4 and 2.8." |
| The 48% and 67% in the conclusions cannot be traced to a figure on earlier slides. 48% is near the mean of 50% and 47.2% (48.6%) | p. 24 (printed 23), p. 23 | No | Covered by the new Key numbers context (fix 6) |
| Minor layout errors: two slides printed "23". The sample sheet lists six states including Benue while fieldwork covered five, and it is labelled A4 with A5 dimensions (148 x 210 mm). "Shumann" misspelled on the team slide | pp. 3, 11, 14, 24 | No | Not needed in the card |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Ease-of-understanding result: "Partially", median 3, 45% scored 4 or 5, 23% scored 1 or 2 (p. 19) | No | High | Fix 2, fix 6 |
| Icon test design and results: 12 farmers, two styles, free description 47.2 to 50%, matching 71.5 to 75%, per-trait scores (p. 23) | Partly (48% only) | High | Fix 2, fix 6 |
| Implementers' NPS based on 6 people, and fatigue from added research tasks (p. 22) | No | High | Fix 2, fix 6, fix 9 |
| Timing of measures: scales before explanation, NPS after group discussion (pp. 18, 19, 22) | No | Medium | Fix 2, fix 8 |
| Session dynamics: self-sorting by top variety, memory trigger, ownership, gender-skewed talk, focus on past results due to delay (p. 21) | No | Medium | Fix 2, fix 9 |
| Practical challenges: printing and diploma budget, signature delays, poor LLM translation of Yoruba and Igbo, font size, paper durability (pp. 16, 17, 19, 21) | Partly (durability) | Medium | Fix 2, fix 9 |
| Next steps: ClimMob automation and one-click sheets, local-language translation, facilitator training, cross-context validation (p. 25) | Partly | Medium | Fix 2 |
| Problem statement and implementer journey: old form not used, sessions not budgeted, no guidance (pp. 2, 6) | No | Medium | Fix 2 (first paragraph) |
| Farmer journey: judgement tied to agronomic performance, gari and eba quality as main success metric, group work means individual diplomas overlook team effort (p. 20) | No | Low | Optional Notes line |
| Sample sheet text says two varieties (Biggie, Renewed Hope) were released in 2024 informed by this trial (p. 11) | No | Low | Optional Notes line, labelled as text printed on the prototype sheet |
| IITA and NRCRI teams felt farmers were heard, not just their data (p. 24, printed 23) | No | Low | None needed |

## Template compliance

- Summary word count: 406, within 400 to 500. The suggested replacement is 498.
- Gist: 26 words, under 30. The suggested replacement is 29.
- Keywords: 10, within 8 to 12.
- Questions: 4, within 4 to 7. Optional fifth question: "How well do farmers understand the sheet without explanation?"
- House style: tricot and maniva are lowercase throughout, except that the title should follow the printed capitalization (fix 10).
- not_established: missing (fix 4).
- Long-format sections are all present.
