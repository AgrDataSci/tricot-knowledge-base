# Card review: schumann-2024-ux

- **Card:** papers/schumann-2024-ux.md
- **Source:** papers-pdf/schumann-et-al-2024.pdf (20 pages, slide deck)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

Page numbers: the slides carry no printed page numbers, so "p." below means the PDF page, which is the same as the slide number. All 20 pages were opened visually because the text extraction misses the prototype slides (pp. 14 to 16 and 19).

## Overview

| Check | Result |
|---|---|
| Claims checked | 39 body claims, plus 13 frontmatter fields |
| Supported | 24 |
| Imprecise | 12 |
| Not in source | 2 |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 4 |
| Important omissions | 3 high, 4 medium |
| Metadata issues | 6 |

The card is accurate on the problem statement, the implementer journey and most of the ideas. The prototype part is wrong in sequence and attribution. The card says the first prototypes were a separate feedback sheet and diploma, but the first round was three combined concepts (Diploma, Blackboard, Copy, pp. 13 to 16), and the separation came only in Prototypes 1.1 after an internal review (pp. 17 to 19). The card also credits insights from that internal design team review to farmer "feedback sessions" and to the implementer co-design session. Most of the implementer co-design insights are missing, and so is not_established. The deck gives no sample sizes and reports no direct input from farmers, and the card does not say so.

## Fixes needed

1. **Prototype sequence (Contradicted, main result).** Card, Summary paragraph 4: "First prototypes were a farmer feedback sheet and a separate participation diploma. Feedback sessions highlighted local equipment constraints (...) Implementers preferred simple letter codes over complicated variety numbers." Source: p. 13 "First prototypes for feedback sheets, Variants", then three concepts on pp. 14 to 16 (Diploma, Blackboard, Copy), each with variants, graphic codes and a pros-and-cons rating on 8 criteria. Separating the certificate from the feedback sheet is a suggestion from the "Feedback session (Inclusive Design Lever team)" on p. 17, an internal design review, not a farmer feedback session. The separate diploma and sheet are "Prototypes 1.1" (pp. 18 to 19). On p. 20 implementers suggest easy names "or use A.B.C", not a firm preference for letters. Replace the whole paragraph with:

   > The first prototypes were three feedback sheet concepts, shown on slides branded BOLDER. A formal Diploma used medals, an informal Blackboard used podium graphics, and a black-and-white Copy could be filled in by hand. Each was rated on eight pros-and-cons criteria, including ClimMob data extraction, printing cost and meeting time. An internal feedback session with the Inclusive Design Lever team raised questions about local equipment (sharing by WhatsApp, black-and-white printing, laminated sheets). It proposed separating a participation certificate from an informative feedback sheet, and stressed crop-specific icons and managing expectations about seed availability. The refined Prototypes 1.1 were therefore a separate diploma and feedback sheet. In a co-design session, implementers appreciated the diploma, preferred abstract leaf icons, and asked for easy variety names or letters instead of complicated numbers. They said farmers want a clear local recommendation of what to plant.

2. **Misattributed co-design details and outside knowledge in the Summary (Imprecise, Not in source).** Card, paragraph 5: "Co-design with implementers also tested practical details, such as whether sheets should show farmers how much data they contributed, whether to add management advice or information on where to obtain seed, and how to make results understandable without long explanations. These insights fed the prototypes later validated in the field (muller-2025-ux)." Source: the data-contributed, management-advice and seed-access questions come from the internal design team session (p. 17), not from implementers (p. 20). "Without long explanations" comes from the designers' pros and cons (pp. 14 to 16). Field validation is not in this deck. It is already in Notes. Replace with:

   > The internal design review also asked whether sheets should show farmers how much data they contributed, and whether to add management advice or information on where to obtain seed.

3. **Missing not_established (high).** Add to the frontmatter:

   > not_established: that farmers were consulted or tested the prototypes; how often implementers skip feedback (no counts are given); how many implementers were interviewed or joined the sessions; that the proposed ClimMob features (budget planner, reminders, single feedback sheet) exist; that the figures on the mock-up sheets (100 or 137 participants, 40, 35 and 25 votes) are trial data; that the redesigned sheets improve farmer understanding or participation

4. **Problem statement drops "systematically" (Imprecise).** Card: "the existing feedback form was not used by implementers". Source p. 3: the form "has not been used systematically by Tricot trial implementers". Replace with:

   > the existing feedback form was not used systematically by tricot trial implementers

5. **Pain points at the last two journey stages (Imprecise).** Card: "the existing forms are hard to extract from ClimMob and do not feel like a fair return for farmers' effort." Source p. 5: forms are "not useful and difficult to extract", and the form is "difficult to understand" and not "a worthy return for farmers' participation". Replace with:

   > and the existing forms are seen as not useful, hard to extract and hard to understand, and do not feel like a worthy return for farmers' participation.

6. **Ideas list (Imprecise).** Card: "photos and videos to personalize feedback, reminders to implementers, a single easy feedback sheet in local languages generated by ClimMob, a workshop manual, and storytelling or gamified session formats. The team ranked ideas by impact and effort." Source: videos document farmers' experience and questions, and photos personalize the sheet (p. 8). The single sheet (p. 10) and reports in local languages are two separate ideas, and the second is a question, with a language-free report as the alternative (p. 10). Redesigned ranking graphics are on p. 11. The team also voted (p. 12). Replace with:

   > videos of farmers' experience and photos to personalize the feedback sheet, reminders to implementers, a single easy feedback sheet generated in ClimMob, individual reports in local languages or without text, a workshop manual, storytelling or gamified session formats, and new ranking graphics. The team placed the ideas on an impact-effort matrix and voted for the first ones to implement.

7. **Unsupported closing interpretation (Not in source).** Card: "The review sets the stage for treating farmer feedback as a designed product with its own requirements, users and evaluation, rather than an administrative report. It also names concrete changes that ClimMob could make to lower the workload of implementers." The deck never mentions evaluation. The nearest points are "Design Requirements" (p. 2) and a sheet that is "Not as a subreport of trial report" (p. 10). Replace both sentences with the one below. The workload point is already covered in paragraph 3.

   > The review treats the feedback sheet as a product to design for its users, generated in ClimMob on its own rather than as a subreport of the trial report.

   With fixes 1, 2, 4, 5, 6 and 7 applied, the Summary has 494 words (checked in Python).

8. **Gist (Imprecise).** Card: "UX review finding tricot implementers rarely run farmer feedback, ...". "Rarely" is stronger than "not systematically", and the gist lists topics. Replace with (27 words):

   > gist: Design review finding that tricot feedback to farmers breaks down long before feedback sessions, and proposing ClimMob support, implementer prompts and a separate diploma and feedback sheet

9. **Methods (Imprecise, incomplete).** The Prototype bullet hides the three-concept first round. The Scope stage (p. 2) is missing. Replace the Methods section with:

   > - **Scope.** Roles and responsibilities, a shared goal, a review of prior insights, and a problem statement.
   > - **Explore.** Desk research, design review, heuristic review, interviews with tricot implementers.
   > - **Create.** Ideation along the implementer journey, impact-effort prioritization with voting, feedback and co-design sessions with colleagues and implementers.
   > - **Prototype.** Three feedback sheet concepts (Diploma, Blackboard, Copy) rated on eight pros-and-cons criteria, then Prototypes 1.1, a separate participation diploma and feedback sheet, discussed with implementers.
   > - **Sample size.** Not reported. The deck gives no number of interviews or session participants.

10. **Stated limitations (Imprecise).** The deck states no limitations. The card's line is a fair inference but is presented as the authors' own, and the input came from designers and colleagues as well as implementers. Replace with:

    > - The deck states no limitations and gives no sample sizes. Farmers were not consulted directly. Getting feedback from lead farmers is listed as a possible next step (slide 20).

11. **Key numbers (Imprecise).** "2 prototype products" is true only for Prototypes 1.1. Replace the table rows with:

    > | 3 | Feedback sheet design concepts in the first round (Diploma, Blackboard, Copy) | This presentation |
    > | 8 | Criteria used to rate each concept in the pros and cons | This presentation |
    > | 2 | Products in Prototypes 1.1, a participation diploma and a separate feedback sheet | This presentation |
    > | 6 | Stages of the implementer journey, from learning about tricot to the feedback session | This presentation |

12. **Question 3 (minor).** "What kinds of feedback materials do farmers and implementers want?" implies that farmers were asked, which they were not. Replace with:

    > - What feedback materials did designers and implementers propose for farmers?

13. **Frontmatter fields (minor).** Replace as follows:

    > title: Farmer Feedback in Tricot. 2024 review
    > journal: Alliance of Bioversity International and CIAT (presentation)
    > crops: any (mock-up sheets show amaranth)
    > region: general (mock-up sheets use Nossombougou, Kodian as an example site)

    If "UX Research and Inclusive Design" comes from the CGSpace record, keep it but check the record first. It is not in the PDF.

14. **Notes additions.** Add these lines to Notes:

    > - The deck's "Feedback session (Inclusive Design Lever team)" (slide 17) is an internal design review, not a farmer feedback session.
    > - The numbers on the mock-up sheets are placeholders, not trial data: 137 participants on the Diploma concept (slide 14) and 100 farmers with 40, 35 and 25 votes on Prototypes 1.1 (slide 19).
    > - The slide deck spells the second author "Londono". The card uses Londoño, as in other cards.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Farmer feedback in tricot. 2024 review | "Farmer Feedback in Tricot- 2024 review" (p. 1) | Imprecise (minor). Hyphen changed to a period, as expected, but capitals changed. AGENTS.md asks to quote titles exactly. |
| authors | Schumann C, Londoño JM, Müller A | Dr. Charlotte Schumann, Juan Manuel Londono, Anna Müller (p. 1) | Supported. Order matches. The PDF has no tilde (see Source issues). The layer 1 flag is explained by this. |
| year | 2024 | "2024 review" (p. 1), mock-ups dated Nov 2024 (pp. 14 to 19). PDF file created 7 Jan 2025. | Supported |
| journal | Alliance of Bioversity International and CIAT, UX Research and Inclusive Design (presentation) | Alliance, CGIAR, 1000FARMS and Crop Trust logos (p. 1), "Inclusive Design Lever team" (p. 17). No "UX Research and Inclusive Design". | Not in source (may come from the repository record, which I could not open) |
| article | review slides | Slide deck | Supported |
| type | presentation | Slide deck | Supported |
| doi | https://hdl.handle.net/10568/169094 | No handle printed in the PDF. The handle page could not be fetched (request blocked). | Not verifiable here |
| license | see repository record | No licence in the PDF | Supported as a pointer. The template wording is "see CGSpace record". |
| data | none | No dataset | Supported |
| crops | any | Mock-ups are for amaranth ("new varieties of Amaranth", p. 19, amaranth outline, p. 15) | Imprecise (minor) |
| region | general | Mock-ups use Nossombougou, Kodian (pp. 14 to 19). The deck asks whether to design for West Africa first (p. 17). | Imprecise (minor) |
| gist | UX review finding tricot implementers rarely run farmer feedback, ... | "not used systematically" (p. 3) | Imprecise. Wording stronger than the source, and it lists topics. |
| not_established | missing | No sample sizes, no farmer testing, placeholder numbers on mock-ups | Missing (high) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Deck reviews why feedback, an integral part of tricot, is not delivered systematically | Supported | p. 3, p. 5 | |
| 2 | Summary | Existing form not used by implementers | Imprecise | p. 3, "not been used systematically" | Drops "systematically". Fix 4. |
| 3 | Summary | Participants not equal partners, undermines participatory promise | Supported | p. 3 | |
| 4 | Summary | Process of scoping, exploring (desk research, design and heuristic review, interviews), creating (co-design, prototypes) | Supported | p. 2 | |
| 5 | Summary | Journey mapping shows gap starts well before feedback sessions | Supported | pp. 4 to 5 | |
| 6 | Summary | Implementers unaware feedback is part of method | Supported | p. 5 | |
| 7 | Summary | Farmers do not understand their role or ask for feedback | Supported | p. 5 | |
| 8 | Summary | Sessions not budgeted | Supported | p. 5 | |
| 9 | Summary | Other trial duties take priority | Supported | p. 5 | |
| 10 | Summary | No guidance on running sessions | Supported | p. 5 | |
| 11 | Summary | Forms hard to extract from ClimMob, not a fair return | Imprecise | p. 5 | Drops "not useful" and "difficult to understand". The slide says "Forms from Tricot", with ClimMob marked at that stage. Fix 5. |
| 12 | Summary | Communicate feedback as a responsibility, with success stories | Supported | p. 6 | Also "Visualize feedback in ClimMob process design" (p. 6), not in card. |
| 13 | Summary | Training and recognizing field agents | Supported | p. 6 | Online training and a training day |
| 14 | Summary | Budget planner in ClimMob | Supported | p. 7 | |
| 15 | Summary | Info materials on citizen science for farmers | Supported | p. 8 | Posters and handouts during training |
| 16 | Summary | Photos and videos to personalize feedback | Imprecise | p. 8 | Videos document farmers' experience and questions. Only photos personalize the sheet. Fix 6. |
| 17 | Summary | Reminders to implementers | Supported | p. 9 | By SMS, email or ClimMob |
| 18 | Summary | Single easy feedback sheet in local languages generated by ClimMob | Imprecise | p. 10 | Two ideas merged. Local languages is posed as a question, with "language-free" as the alternative. Fix 6. |
| 19 | Summary | Workshop manual | Supported | p. 10 | |
| 20 | Summary | Storytelling or gamified session formats | Supported | p. 11 | |
| 21 | Summary | Team ranked ideas by impact and effort | Supported | p. 12 | Voting step omitted |
| 22 | Summary | First prototypes were a feedback sheet and a separate diploma | Contradicted | pp. 13 to 19 | The first round was three combined concepts. The separation came in Prototypes 1.1. Fix 1. |
| 23 | Summary | Feedback sessions highlighted equipment constraints (WhatsApp, black and white, laminate) | Imprecise | p. 17 | Internal design team session, not farmer feedback sessions. Points are posed as questions. Fix 1. |
| 24 | Summary | Value of recognizing farmers' contribution | Supported | p. 17 | |
| 25 | Summary | Managing expectations about seed availability | Supported | p. 17, p. 19 | The sheet notes that the varieties may not be released |
| 26 | Summary | Need for crop-specific, localized icons | Imprecise | p. 17 | Plant-specific icons are stated. Localization is an open question (West Africa first?). |
| 27 | Summary | Implementers preferred letter codes over variety numbers | Imprecise | p. 20 | Easy names "or use A.B.C". Fix 1. |
| 28 | Summary | Without feedback farmers contribute data but get little back, which weakens partnership | Supported | p. 3, p. 5 | Fair paraphrase |
| 29 | Summary | Ideas target implementers, feedback as a budgeted, planned step | Supported | pp. 5 to 11 | Card's synthesis, fair |
| 30 | Summary | Co-design with implementers tested data-contributed, management advice, seed info | Imprecise | p. 17 vs p. 20 | Wrong session. Fix 2. |
| 31 | Summary | Co-design tested how to make results understandable without long explanations | Imprecise | pp. 14 to 16 | From the designers' pros and cons, not co-design. Fix 2. |
| 32 | Summary | Insights fed prototypes later validated in the field (muller-2025-ux) | Not in source | none | First half fits p. 17 to p. 18. Field validation is outside knowledge. It belongs in Notes, where it already is. Fix 2. |
| 33 | Summary | Sets the stage for feedback as a designed product with requirements, users and evaluation | Not in source | p. 2, p. 10 (nearest) | Evaluation is never mentioned. Fix 7. |
| 34 | Summary | Names ClimMob changes to lower implementer workload | Supported | p. 7, p. 9, p. 10 | |
| 35 | Methods | Explore: desk research, design review, heuristic review, interviews | Supported | p. 2 | |
| 36 | Methods | Create: ideation along journey, impact-effort, co-design with colleagues and implementers | Supported | p. 2, pp. 5 to 12 | |
| 37 | Methods | Prototype: feedback sheet and diploma variants | Imprecise | pp. 13 to 19 | Misses the three-concept first round. Fix 9. |
| 38 | Limitations | Early-stage work on implementer input, before farmer field testing | Imprecise | p. 20 | Not stated by the authors. Fair inference, but input also came from designers and colleagues. Fix 10. |
| 39 | Key numbers | 2 prototype products | Imprecise | p. 18 vs pp. 14 to 16 | True only for Prototypes 1.1. Fix 11. |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The deck calls an internal design team review a "Feedback session", the same words used for farmer feedback sessions. The card falls into this ambiguity. | p. 17 | No | The deck's "Feedback session (Inclusive Design Lever team)" (slide 17) is an internal design review, not a farmer feedback session. |
| Mock-up numbers are placeholders and differ between designs: 137 participants (p. 14) vs 100 farmers with 40, 35 and 25 votes (p. 19). The Blackboard sheet repeats "Flowering" as a trait label (p. 15). Values were read off small images and are approximate. | pp. 14, 15, 19 | No (the card does not use them) | The numbers on the mock-up sheets are placeholders, not trial data: 137 participants on the Diploma concept (slide 14) and 100 farmers with 40, 35 and 25 votes on Prototypes 1.1 (slide 19). |
| Second author spelled "Londono" without a tilde | p. 1 | No | The slide deck spells the second author "Londono". The card uses Londoño, as in other cards. |
| The title says "2024 review", but the PDF file was created on 7 January 2025 and slide 20 plans fieldwork for "January?" | p. 1, p. 20, PDF metadata | No | Low importance. No Notes text needed unless the repository record gives 2025. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim and problem statement (p. 3) | Yes | high | Add "systematically" (Fix 4) |
| Design process: Scope, Explore, Create, with problem statement, design requirements, selected prototype (p. 2) | Partly (Scope missing from Methods) | medium | Fix 9 |
| Sample sizes: number of interviews, implementers, session participants | No. The source gives none, and the card does not say so. | high | Fix 3 (not_established) and Fix 9 |
| Implementer journey, 6 stages and 7 pain points (p. 5) | Yes | high | Fix 5 for wording |
| Ideas per stage (pp. 6 to 11) | Mostly | medium | Visualize feedback in ClimMob process design (p. 6), redesigned ranking graphics, photo review, co-designing formats such as a calendar (p. 11). Partly covered by Fix 6. |
| Impact-effort matrix and voting (p. 12) | Partly (voting missing) | low | Fix 6 |
| Three first-round concepts (Diploma, Blackboard, Copy) with graphic codes and 8-criterion pros and cons (pp. 14 to 16) | No | high | Fix 1, Fix 9, Fix 11 |
| Pros and cons findings: the Diploma needs colour printing and its decoration may complicate ClimMob extraction. The Blackboard is easy to populate from ClimMob. The Copy is cheap in black and white but may need more explanation. (pp. 14 to 16) | No | medium | Optional sentence in Summary paragraph 4 if word count allows |
| Content of Prototypes 1.1 sheet: own ranking, community ranking with votes, trait thumbs up or down, management recommendations, note that varieties may not be released, contact details, QR code (p. 19) | No | medium | Optional, for example: "The 1.1 sheet shows the farmer's own ranking, the community ranking, trait results, management advice and a note that the varieties may never be released." |
| Implementer co-design insights: abstract leaf icons, how to handle incomplete block design, results selectable by region, country or agro-ecological zone, farmers want a clear local recommendation of what to plant, diploma and logos appreciated, 3 certificates could make a lead farmer (p. 20) | Partly (only variety names) | high | Fix 1 adds the main ones |
| Next steps: talking points for field agents beyond the sheet, getting feedback from lead farmers, possibly in January (p. 20) | No | medium | Fix 10 covers the lead-farmer step. Optional: "A next step is talking points for field agents with the information not on the sheet." |
| Partners shown: Alliance, CGIAR, 1000FARMS, Crop Trust (p. 1), BOLDER on design slides (pp. 14 to 16) | No | low | Fix 1 mentions BOLDER |

## Template compliance

- Summary word count: 406 (within 400 to 500). With the suggested fixes it is 494.
- Gist: 23 words (under 30). The suggested gist has 27 words.
- Keywords: 10 (within 8 to 12).
- Questions: 4 (within 4 to 7).
- House style: tricot is lowercase throughout the card. maniva does not appear. The title field lowercases "Tricot", but AGENTS.md asks to quote published titles exactly (Fix 13).
- Long-format sections are all present.
- Not checked: the handle https://hdl.handle.net/10568/169094 could not be opened from this session (the permission request was not answered), so the DOI, licence, journal wording and year were not checked against the repository record.
