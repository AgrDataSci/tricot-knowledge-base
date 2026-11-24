# Card review: goormachtigh-2026-flyer

- **Card:** papers/goormachtigh-2026-flyer.md
- **Source:** papers-pdf/goormachtigh-et-al-2026.pdf (2 pages, no printed page numbers, so page numbers below are PDF pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 45 |
| Supported | 31 |
| Imprecise | 6 |
| Not in source | 8 (4 are team information flagged in Notes, 2 are outside facts already in Notes, 2 need a fix) |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 2 |
| Important omissions | 3 (all medium) |
| Metadata issues | 2 (gist, year) |

The card describes the flyer accurately in almost every detail: the four steps, the output table, the language list, the countries and the ethics points all match both pages. The main problem is that it calls Sikia "integrated with ClimMob" (gist, Summary, Notes). The flyer only says the form builder "supports ODK .xls forms and ClimMob" (p. 1). It also never links voice answers to tricot rankings. The gist can also be read to mean that transcription and coding happen offline, but the flyer says they happen after the phone syncs (p. 1). The Summary is 331 words, below the 400-word target.

## Fixes needed

1. **ClimMob "integration" is stronger than the source (gist, Summary paragraph 1, Notes bullet 4).** The card says Sikia "is integrated with ClimMob, so ClimMob projects can collect voice answers alongside the usual rankings and questions". The flyer mentions ClimMob once, in step 1: "Sikia supports ODK .xls forms and ClimMob" (p. 1). It says nothing about rankings, tricot or combining voice answers with ClimMob data.
   - Summary, replace "It is integrated with ClimMob, so ClimMob projects can collect voice answers alongside the usual rankings and questions." with:
     > Its form builder supports ClimMob as well as ODK .xls forms. The flyer does not say how voice answers combine with tricot rankings.
   - Notes bullet 4, replace "This flyer documents it as integrated with ClimMob." with:
     > This flyer lists ClimMob as a supported form source for Sikia.

2. **Gist overstates ClimMob and blurs what runs offline.** The gist says Sikia "records, transcribes, translates and codes ... offline on ordinary smartphones". On p. 1, recording and probing run offline (step 3, "Works offline", "What makes Sikia different"). Transcription and coding happen "Once the phone syncs" (step 4). Suggested gist (28 words):
   > Flyer on Sikia, an AI tool that records and probes interviews offline on Android phones, transcribes, translates and codes local-language answers after sync, using ClimMob or ODK forms

3. **"Sikia means 'to listen' in Swahili" is outside knowledge in the Summary.** The flyer does not say this. It is in the Alliance story of 19 October 2026 (checked by the reviewer). Replace the second sentence of the Summary with nothing (delete "Sikia means "to listen" in Swahili."), and add to Notes:
   > The name Sikia means "to listen" in Swahili. This comes from the Alliance story of 19 October 2026, not from the flyer.

4. **Year and draft status are not flagged.** The flyer carries no authors and no date (pp. 1 to 2). Its only time reference is "In Q1 2027, we will use Sikia" (p. 2). The PDF's internal title is "Sikia, two-page summary (draft 23, editable)" (dash replaced by a comma). Add to Notes:
   > The flyer itself carries no author names and no date. The year 2026 comes from the team. The PDF's internal title calls it draft 23, so check that this is the final version before citing it.

5. **Summary wording more certain than the source (paragraph 2).** The card says translation and manual coding "add bias and lose local nuance". The flyer says they "can introduce bias and miss important local nuances" (p. 1). The card also says Sikia "targets people who speak only local languages". The flyer says Sikia is for anyone collecting evidence from such people, who "often" live with limited connectivity (p. 1). Replace the last two sentences of paragraph 2 with:
   > In under-resourced languages, translation and manual analysis can add bias and miss local nuance. Sikia is meant for anyone who needs evidence from people who speak only local languages and often live where connectivity is poor.

6. **Summary is 331 words (target 400 to 500), and two medium-importance points are missing.** Insert after the outputs paragraph (adds about 85 words):
   > The flyer's example shows one spoken answer in Swahili about a seed. Sikia transcribes it, translates it into English and codes it into two named categories, good germination (positive) and early leaf drying (negative). The flyer also claims that reports come in minutes instead of days and that Sikia runs quality checks on full transcripts. It gives no figures to support these claims. It says nothing in the platform is specific to one sector, and lists uses such as market intelligence, policy and evaluation, public health, education and conservation.

7. **Stated limitations are not limitations the flyer states.** The flyer lists no limitations. The language roadmap is presented as progress, and the second bullet is the card's own assessment. Also "not available before 2027" is an inference from "Committed before the end of 2027" (p. 2). Replace the section with:
   > - The flyer states no limitations of its own.
   > - Language coverage is still growing. Oromo is "supported, with further refinement underway", and Chichewa, Yoruba and Shona are committed before the end of 2027.
   > - The flyer is promotional and reports no accuracy, cost or data-quality figures (card's own observation).

8. **not_established can be stronger.** Add two items that users are likely to stretch the flyer to:
   > ; that transcription, translation and coding run offline (on the flyer they run after the phone syncs); that Sikia has been used in a tricot trial (the flyer names only product concept testing in Ethiopia and Tanzania and rice research evaluation in Colombia)

9. **Optional, Notes.** The Alliance story linked in `open_copy` gives early accuracy scores that the flyer does not, for example Amharic transcription around 9.5 to 10 out of 10 and Afaan Oromo transcription around 3 to 6 out of 10 (read by the reviewer through a web summary, so verify the exact figures). This fits the card's not_established item on accuracy. Suggested Notes text:
   > The Alliance story of 19 October 2026 reports early, informal accuracy scores by language (high for Amharic, low for Afaan Oromo). These are not in the flyer.

10. **Minor, Questions.** "Can farmers answer in their own language, by voice, during a tricot or ClimMob data collection?" The flyer never mentions tricot. Suggested:
    > Can farmers answer by voice, in their own language, in a survey designed in ClimMob?

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Sikia. Listening at scale | Heading "Listening at scale." with the Sikia logo (p. 1). PDF internal title "Sikia, two-page summary (draft 23, editable)" (dash replaced by a comma) | Supported (title built from logo and heading, acceptable) |
| authors | Goormachtigh L, Mutuvi S, Woltering L | No names on the flyer (pp. 1 to 2) | Not in source (team information). Flagged in Notes, not an error |
| year | 2026 | No date on the flyer. Only "Q1 2027" as a future plan (p. 2) | Not in source. Add a Note (Fix 4) |
| journal | Flyer, Alliance of Bioversity International and CIAT | Alliance logo on both pages | Supported |
| article | 2 p. | 2 pages | Supported |
| type | flyer | Two-page promotional summary ending with "Book a demo with us" (p. 2) | Supported |
| doi | empty | No DOI or handle | Supported (template allows empty for team flyers) |
| license | none stated (team flyer) | No license statement | Supported |
| data | none | No dataset | Supported |
| crops | not crop specific, used for product concept testing and rice research | "Nothing in the platform is specific to one sector", rice research in Colombia (p. 2) | Supported |
| region | Ethiopia, Tanzania, Colombia, Nigeria planned for 2027 | p. 2 "Where is it running" | Supported |
| gist | integrated with ClimMob ... offline on ordinary smartphones | Form builder supports ClimMob (p. 1). Transcripts made after sync (p. 1) | Imprecise (Fix 2) |
| not_established | accuracy, cost or quality in tricot, language parity | No evaluation figures anywhere. Oromo refining, three languages for 2027 (p. 2) | Supported. Could add two items (Fix 8) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Frontmatter | title | Supported | p. 1 heading and logo | |
| 2 | Frontmatter | authors | Not in source (team information) | No names on pp. 1 to 2 | Flagged in Notes |
| 3 | Frontmatter | year 2026 | Not in source | No date | Fix 4 |
| 4 | Frontmatter | journal | Supported | Alliance logo pp. 1 to 2 | |
| 5 | Frontmatter | article 2 p. | Supported | 2 pages | |
| 6 | Frontmatter | type flyer | Supported | pp. 1 to 2 | |
| 7 | Frontmatter | doi empty | Supported | none printed | |
| 8 | Frontmatter | license none stated | Supported | none printed | |
| 9 | Frontmatter | data none | Supported | | |
| 10 | Frontmatter | crops | Supported | p. 2 | |
| 11 | Frontmatter | region | Supported | p. 2 | |
| 12 | Frontmatter | gist | Imprecise | p. 1 steps 1 and 4 | ClimMob and offline wording (Fix 2) |
| 13 | Frontmatter | not_established | Supported | pp. 1 to 2 | Can add items (Fix 8) |
| 14 | Summary | Goormachtigh, Mutuvi and Woltering present Sikia in a two-page Alliance flyer | Not in source (team information) | No names in flyer | Notes explains the attribution, not an error |
| 15 | Summary | Sikia means "to listen" in Swahili | Not in source | Not in flyer. In the Alliance story | Move to Notes (Fix 3) |
| 16 | Summary | AI tool to collect open-ended spoken answers in own languages and turn them into structured data | Supported | p. 1 banner, "Insights in minutes" | |
| 17 | Summary | Integrated with ClimMob, voice answers alongside the usual rankings | Imprecise | p. 1 step 1, "supports ODK .xls forms and ClimMob" | Rankings not mentioned (Fix 1) |
| 18 | Summary | Problem framed as depth versus scale | Supported | p. 1 "No depth or scale trade-off" | |
| 19 | Summary | Interviews slow and costly, translation and manual coding add bias and lose nuance | Imprecise | p. 1 "can introduce bias and miss" | More certain than source (Fix 5) |
| 20 | Summary | Sikia targets people who speak only local languages where connectivity is poor | Imprecise | p. 1 "Who is Sikia for?" | Built for those collecting evidence from such people, who "often" have poor connectivity (Fix 5) |
| 21 | Summary | Four steps, AI form builder accepts ODK .xls and ClimMob | Supported | p. 1 "How it works" step 1 | |
| 22 | Summary | Open conversation, Sikia listens on ordinary Android phone or tablet | Supported | p. 1 step 2, "What makes Sikia different" | |
| 23 | Summary | Tracks what is missing, suggests next question in real time, on device, no connectivity | Supported | p. 1 step 3 and box | |
| 24 | Summary | After sync, transcripts, LLMs trained on local languages produce themes, coded answers, report | Supported | p. 1 step 4, figure caption | |
| 25 | Summary | Outputs: survey data with transcripts and translations (Excel, CSV, JSON, SPSS, Stata), transcripts, themes and sentiment, PDF report, audio | Supported | p. 2 "What you get back" | |
| 26 | Summary | Languages: live, off the shelf, Oromo refining, three committed for 2027 | Supported | p. 2 "Languages" | |
| 27 | Summary | Used in Ethiopia, Tanzania (concept testing), Colombia (rice), Hausa surveys in Nigeria early 2027 | Supported | p. 2 "Where is it running" | "early 2027" matches "Q1 2027" |
| 28 | Summary | Authenticated service, encryption, expiring links, scrambled personal data, consent text per language | Supported | p. 2 ethics box | Flyer says recordings and photos are "accessible" through expiring links, card says "shared". Fine |
| 29 | Methods | Design bullet | Supported | p. 1 step 1 | "questionnaires" is a small addition, fine |
| 30 | Methods | Collection bullet | Supported | p. 1 step 2 and box | |
| 31 | Methods | Probing bullet | Supported | p. 1 step 3 and box | |
| 32 | Methods | Processing bullet | Supported | p. 1 step 4 and box | Flyer does not say which model translates. Acceptable |
| 33 | Methods | Ethics bullet | Supported | p. 2 | |
| 34 | Limitations | Oromo refining, three languages not available before 2027 | Imprecise | p. 2 "Committed before the end of 2027" | Roadmap, not a stated limitation (Fix 7) |
| 35 | Limitations | Promotional, no accuracy, cost or quality figures | Supported | Whole flyer | Card's own observation, should be labelled (Fix 7) |
| 36 | Key numbers | 3 live languages | Supported | p. 2 | |
| 37 | Key numbers | 3 languages committed by end of 2027 | Supported | p. 2 | |
| 38 | Key numbers | 4 workflow steps | Supported | p. 1 | |
| 39 | Key numbers | 3 countries used so far | Supported | p. 2 | |
| 40 | Key numbers | Q1 2027 Nigeria | Supported | p. 2 | |
| 41 | Notes | Team flyer, not a CGSpace product, no handle or DOI | Not in source (team information) | No DOI printed | Fine as a Note |
| 42 | Notes | Authorship follows the team's attribution | Not in source (team information) | No names in flyer | Correctly flagged |
| 43 | Notes | Alliance story of 19 October 2026, its authors, CropConcept pilot | Not in source (outside, labelled) | Reviewer checked the story page: date, authors and CIMMYT CropConcept pilot match | Fine |
| 44 | Notes | Grew out of NDIZI, links to ARTEMIS | Not in source (outside) | Story says the NDIZI team ran the deployment and links an Artemis page without details | Fine as a Note. Consider "was developed by the Alliance's NDIZI team" if "grew out of" cannot be confirmed |
| 45 | Notes | "This flyer documents it as integrated with ClimMob" | Imprecise | p. 1 step 1 | Fix 1 |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The PDF's internal title reads "Sikia, two-page summary (draft 23, editable)" (dash replaced by a comma), so the file may be a draft rather than the final flyer | PDF metadata | No | See Fix 4 |
| The flyer has no author names and no date, so authors and year cannot be checked against it | pp. 1 to 2 | Partly (authorship yes, year no) | See Fix 4 |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: in-depth feedback from more people, in their own languages | Yes | High | |
| Design: four-step workflow, offline probing on device | Yes | High | |
| Sample sizes, results, effect sizes | Not applicable, none in the flyer | | Card correctly says none are reported |
| Swahili example coded into trait categories (good germination positive, early leaf drying negative) | No | Medium | Fix 6. Shows a tricot user how trait-level coding looks |
| Speed claim: reports "in minutes instead of days", quality checks on transcripts | No | Medium | Fix 6, with the note that no figures support it |
| No tricot use named among the deployments | No | Medium | Fix 8 (not_established) |
| Sector-agnostic, list of application areas | Partly (crops field) | Low | Fix 6 |
| Speech models not repurposed from global English, no hardware procurement needed | Partly (Methods) | Low | |
| Survey data keeps variable labels, transcripts in Word-style, CSV and Excel | Partly | Low | |
| Authors' own limitations | None in the flyer | | Fix 7 |
| Conclusion / call to action ("Book a demo") | No | Low | Not needed |

## Template compliance

- Summary word count: 331. Below the 400 to 500 target. Fix 6 brings it to about 415.
- Gist: 26 words, under 30. Suggested gist in Fix 2 is 28 words.
- Keywords: 12, within 8 to 12.
- Questions: 6, within 4 to 7.
- House style: tricot and maniva lowercase throughout. No em dashes or semicolons in card prose (semicolons only in not_established, as allowed).
- Key numbers rows all labelled "This flyer". No derived numbers to recompute.
