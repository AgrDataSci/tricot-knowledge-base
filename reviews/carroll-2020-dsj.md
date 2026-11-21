# Card review: carroll-2020-dsj

- **Card:** papers/carroll-2020-dsj.md
- **Source:** papers-pdf/carroll-et-al-2020.pdf (12 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 47 (13 frontmatter fields, 21 summary sentences, 2 methods bullets, 2 limitations, 4 key-number rows, 5 notes) |
| Supported | 39 |
| Imprecise | 6 |
| Not in source | 2 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 3 |
| Important omissions | 4 (1 high, 3 medium), plus 4 low |
| Metadata issues | 0 (1 optional note on type) |

The card is accurate on the core content: the four principles, the 2018 Gaborone workshop, the link with FAIR and the call for further work. The most important fix is the Open Data Charter passage (p. 7). The card credits the "open by default" refinement to the Charter's discussion, when it is the authors' own argument, and it leaves out what the paper actually found, so the card's own question on "open by default" has no real answer. Two Notes about tricot data practice (CC0 release, pseudonymization and masking in ClimMob) are not supported by this source or by the cards they cite. The summary is 394 words, just under the 400-word minimum, and the fixes below bring it to about 492.

## Fixes needed

1. **Open Data Charter and early adopters (Imprecise, attribution and certainty, p. 7).**
   - Card: "The Research Data Alliance affiliated with the Global Indigenous Data Alliance that hosts the principles, the Smithsonian is developing Collection CARE Notices, and the Open Data Charter discussed how CARE can refine its "open by default" principle."
   - Source: the Charter's working group discussed implementation mechanisms and the overlap between the Charter, FAIR and CARE. The Charter principles reflect all four FAIR principles but directly address only Collective benefit. "Open by default" maps to neither FAIR nor CARE and was hotly debated in a 2018 review. The idea that CARE can help refine "open by default" is the authors' own argument (pp. 7 to 8). For the Smithsonian, work on the Notices "is about to begin" (p. 7), so "is developing" is too advanced. The card sentence also joins three clauses with commas, which reads as a run-on.
   - Replace the last two sentences of the fifth summary paragraph ("The paper gives early adopters. The Research Data Alliance ... principle.") with a new paragraph:

   > The paper describes three early adopters. The Research Data Alliance affiliated with the Global Indigenous Data Alliance, which hosts the principles. At the Smithsonian, work was about to begin on Collection CARE Notices. The Open Data Charter held a discussion on CARE. Its principles reflect all four FAIR principles but directly address only Collective benefit from CARE, and its contested "Open by default" principle maps to neither. The authors argue that CARE can help define it, by giving Indigenous Peoples and other marginalized communities a role in open data decisions and by protecting access where they ask for it.

2. **Notes on tricot data practice (Not in source, and not supported by the cited cards).**
   - Card Note 1: "tricot data are released openly (CC0)". Card Note 2: "The tricot SOPs handle personal data with pseudonymization, masking and aggregation in ClimMob (chase-2026-book, quiros-2024-compag)."
   - Neither claim is in this source, which is expected for Notes. But I could not find CC0, pseudonymization or masking in chase-2026-book, quiros-2024-compag, their cards or their text extractions. The book (printed pp. 51 to 52) asks for prior informed consent, no publication of personally identifiable information and GDPR compliance. It lists automated privacy-preserving export in ClimMob as further development, and its dissemination chapter (printed p. 192) says anonymization "should be" automated. So "handle ... in ClimMob" is more certain than the cited source. Note 2 also says CARE is "a different question from individual privacy", but the paper lists privacy among the issues CARE addresses (p. 8), and Indigenous data include data about individual persons (p. 3).
   - Replace Notes bullets 1 and 2 with:

   > - Context for data ethics in the suite. CARE asks who benefits from and who controls data about communities. Use it with dumschott-2023-fps on making plant data FAIR.
   > - chase-2026-book (printed pp. 51 to 52) sets out ethics, privacy and access-and-benefit-sharing rules for tricot: prior informed consent, no publication of personally identifiable information, and following Nagoya Protocol principles for farmers' varieties and knowledge. It lists automated privacy-preserving export in ClimMob as further development. CARE centres collective rights and benefit. It names privacy as one issue it addresses (p. 8), but it is not a guide to individual data protection.

   If the team has a source for the CC0 claim, add it back with that source named.

3. **Workshop analysis and conclusion (Imprecise, pp. 4 to 5, Figure 1).**
   - Card: "Participants compared Indigenous and mainstream frameworks, including OCAP, the Māori data sovereignty principles and FAIR, and concluded that mainstream frameworks cover data-centric aspects well but neglect people and purpose. They then drafted and circulated four principles."
   - Source: the organizers prepared the analysis (p. 4). Both Indigenous and mainstream frameworks had data-centric principles, and the Indigenous ones emphasized people and purpose (p. 4). Participants felt mainstream frameworks adequately covered the data side (p. 5). The source does not say mainstream frameworks "neglect" people and purpose, and Figure 1 shows people- or purpose-oriented principles in the Open Data Charter and STREAM columns (shading read off the figure, approximate). The draft had four principles and sub-principles (p. 5, Figure 2 shows three per principle).
   - Replace with:

   > The organizers analysed Indigenous and mainstream frameworks, including OCAP, the Māori data sovereignty principles and FAIR. Both kinds had data-centric principles, but the Indigenous frameworks put more weight on people and purpose. Participants judged that mainstream frameworks already covered the data side, so they built CARE around people and purpose. They drafted four principles, each with three sub-principles, and circulated the draft for comment.

4. **Definition of Indigenous data (Imprecise, low, p. 3).**
   - Card: "data about Indigenous persons held by governments and institutions". Source: the second category is information about Indigenous persons, such as administrative, census, health, social, commercial and corporate data. Who holds or generates it is not the defining criterion (Indigenous data can be generated by Indigenous Peoples or by governments and other institutions). The card also drops "environment".
   - Replace the sentence with:

   > Indigenous data include information about the environment, lands, skies, resources and non-humans, information about Indigenous persons such as census and health data, and knowledge about Indigenous Peoples as collectives, such as oral histories and cultural sites.

5. **CARE Full (omission, medium, pp. 5 and 8).** The paper says one mechanism can address one or several principles, but governance must address all four to be "CARE Full", and calls being CARE Full a prerequisite for equitable data. In the fifth summary paragraph, before "CARE is meant to work with FAIR", insert:

   > Data governance must address all four principles to be "CARE Full".

6. **not_established is correct but thin.** Suggested replacement:

   > not_established: that CARE applies directly to on-farm trial data from non-Indigenous farmers (the authors say it may extend to other collectives, but it was written for Indigenous Peoples' data); specific tools or procedures for implementation, which the authors list as further work; that CARE has been tested or evaluated in practice (the paper describes early adoption, with no outcome data); that CARE requires community data to be closed (it aims for data sharing on Indigenous terms, alongside FAIR)

7. **Gist (optional).** The gist is accurate but says "the peoples the data come from" without naming Indigenous Peoples, and "open data serve" is narrower than the principles. Suggested (27 words):

   > First formal publication of the CARE Principles (Collective benefit, Authority to control, Responsibility, Ethics), which complement FAIR so that Indigenous Peoples control and benefit from their data

8. **Optional Notes addition (omission, medium, p. 6).** For tricot users who handle genetic resources:

   > - The Smithsonian example (p. 6) mentions an access and benefit-sharing policy on genetic resources issued in response to the Nagoya Protocol, covering benefit sharing, prior informed consent and mutually agreed terms. This is the closest link in the paper to plant genetic resources. See chase-2026-book on ABS in tricot.

9. **Optional Key numbers rows.**

   > | 12 | Sub-principles, three under each CARE principle (Figure 2) | This paper |
   > | 9 | Key documents analysed before the workshop (Table 1) | This paper |

With fixes 1, 3, 4 and 5 applied, the summary is about 492 words (checked by script), inside the 400 to 500 range.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | The CARE Principles for Indigenous Data Governance | Same (p. 1) | Supported |
| authors | Carroll SR ... Anderson J, Hudson M (14 names) | Same 14 names, same order (p. 1, p. 12) | Supported |
| year | 2020 | Published 4 November 2020 (p. 12) | Supported |
| journal | Data Science Journal | Same (p. 1) | Supported |
| article | 19, 43 | 19: 43, pp. 1 to 12 (p. 1) | Supported |
| type | perspective | Labelled "Practice paper" (p. 1) | Supported. Closest template category. Optional: say "practice paper" in Notes. |
| doi | https://doi.org/10.5334/dsj-2020-043 | Same (p. 1) | Supported |
| license | CC BY 4.0 | CC-BY 4.0 (p. 12) | Supported |
| data | none | No dataset | Supported |
| crops | none | No crops | Supported |
| region | global | Global scope, examples from US, Canada, NZ, Australia (pp. 2 to 4) | Supported |
| gist | First formal publication of the CARE Principles ... | Abstract (p. 1) | Supported. Optional wording fix 7. |
| not_established | Two items | p. 8 (other collectives, further research) | Supported. Could be stronger, fix 6. |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Open data, big data and machine learning made data a source of power, discovery, commercial value | Supported | pp. 1 to 2 | |
| 2 | Summary | Indigenous Peoples, subject to data exploitation, feel tension between rights and open science | Supported | p. 1 abstract, p. 2 | |
| 3 | Summary | Carroll and colleagues in the RDA interest group present first formal publication | Supported | p. 1 | |
| 4 | Summary | Grounded in 2007 UNDRIP and Indigenous data sovereignty | Supported | pp. 2 to 3 | |
| 5 | Summary | Three categories of Indigenous data, second "held by governments and institutions" | Imprecise | p. 3 | Fix 4 |
| 6 | Summary | Most Indigenous data held by non-Indigenous institutions | Supported | p. 3 | |
| 7 | Summary | Drafted at Indigenous-led workshop, Gaborone, International Data Week 2018 | Supported | p. 4, p. 8 (8 November 2018) | |
| 8 | Summary | Participants compared frameworks incl. OCAP, Māori principles, FAIR | Imprecise | p. 4, Table 1 | Organizers prepared the analysis. Fix 3 |
| 9 | Summary | Mainstream frameworks "neglect people and purpose" | Imprecise | pp. 4 to 5, Figure 1 | Stronger than source. Fix 3 |
| 10 | Summary | Drafted and circulated four principles | Supported | p. 5 | Sub-principles omitted |
| 11 | Summary | Collective benefit description | Supported | p. 6 | |
| 12 | Summary | Authority to control description | Supported | p. 6 | |
| 13 | Summary | Responsibility description | Supported | p. 6 | |
| 14 | Summary | Ethics description | Supported | p. 6 | |
| 15 | Summary | CARE works with FAIR, "Be FAIR and CARE" | Supported | p. 1, p. 5, p. 8 | |
| 16 | Summary | Paper gives early adopters | Supported | p. 6 | Three named |
| 17 | Summary | RDA affiliated with GIDA, which hosts the principles | Supported | p. 6 | |
| 18 | Summary | Smithsonian "is developing" Collection CARE Notices | Imprecise | p. 7 | Work "about to begin". Fix 1 |
| 19 | Summary | Open Data Charter discussed how CARE can refine "open by default" | Imprecise | p. 7 | Refinement is the authors' argument. Fix 1 |
| 20 | Summary | Call for mechanisms, tools, applications, joint use with FAIR | Supported | p. 8 | Source also lists institutional policies and practices |
| 21 | Summary | May guide data on other minority or distinct communities | Supported | p. 8 | |
| 22 | Methods | Indigenous-led workshop, Table 1 analysis, circulation for comment | Supported | pp. 4 to 5 | |
| 23 | Methods | Data, people, purpose framing; CARE people and purpose, FAIR data | Supported | p. 1, p. 4, Figure 1 | |
| 24 | Limitations | Implementation mechanisms, tools, policies need research | Supported | p. 8 | |
| 25 | Limitations | Application in repositories, co-production, existing databases open | Supported | p. 8 | |
| 26 | Key numbers | 4 principles | Supported | p. 5 | |
| 27 | Key numbers | 2018 Gaborone workshop | Supported | p. 4, p. 8 | |
| 28 | Key numbers | >370 million, >90 countries, >5,000 cultures, UN 2009 | Supported | p. 2 | Attribution correct |
| 29 | Key numbers | 2007 UNDRIP, UN 2007 | Supported | p. 2 | Attribution correct |
| 30 | Notes | tricot data released openly (CC0) | Not in source | Not in this paper or the cited cards | Fix 2 |
| 31 | Notes | CARE asks who benefits and who controls data about communities | Supported | p. 6 | |
| 32 | Notes | tricot SOPs handle personal data with pseudonymization, masking, aggregation in ClimMob | Not in source | chase book pp. 51 to 52 and p. 192 describe this as planned or "should be" | Fix 2 |
| 33 | Notes | CARE is a different question from individual privacy | Imprecise | p. 3, p. 8 | Paper lists privacy among CARE issues. Fix 2 |
| 34 | Notes | Not about agriculture or tricot | Supported | Whole paper | Only indirect link via Nagoya Protocol (p. 6) |

Frontmatter fields (13) are in the metadata table and all Supported.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Text names the "American Museum of Natural History at the Smithsonian", but the reference list gives the National Museum of American History, with a naturalhistory.si.edu link. The museum name is inconsistent inside the source. | p. 6, p. 11 (SI 2012) | No | Not needed unless the card cites this example. If fix 8 is used, write "the Smithsonian" only. |
| Text says Open Data Charter principles directly address only Collective benefit, but Figure 3 groups Collective benefit and Responsibility together in the block that faces the Charter's two purpose principles. | p. 7, Figure 3 | No | Optional: "Figure 3 places Responsibility next to Collective benefit in the overlap with the Open Data Charter, but the text says the Charter directly addresses only Collective benefit (p. 7)." |
| Minor citation inconsistencies: OCAP is cited as FNIGC 2019 in the text and FNIGC 2018 in Table 1 and the references. A 2020 document (USIDSN 2020) is listed as an input to the 2018 workshop. | p. 3, p. 4, p. 9 | No | Not needed. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: rationale, relation to FAIR, examples of use (p. 1) | Yes | | |
| Design: workshop, Table 1 analysis, drafting, circulation (pp. 4 to 5) | Yes | | |
| Sample size | Not applicable (no empirical data) | | |
| Open Data Charter mapping and "open by default" debate (p. 7) | Partly, and misattributed | High | Fix 1. The card's own question 4 depends on it. |
| Sub-principles, three per principle (Figure 2, p. 5) | No | Medium | Fix 3 and Key numbers row (fix 9) |
| CARE Full concept and conclusion that it is a prerequisite for equitable data (p. 5, p. 8) | No | Medium | Fix 5 |
| Smithsonian ABS policy under the Nagoya Protocol, and SD 609 sensitive content (pp. 6 to 7) | No | Medium | Fix 8. Most relevant link for germplasm and traditional knowledge in tricot. |
| Two primary goals: Indigenous self-determination through data use, and honouring FAIR with sharing on Indigenous terms (p. 3) | No | Low | Covered in part by fix 6 |
| Shift from regulated consultation to value-based relationships (p. 3) | No | Low | |
| Principles apply in research, government and institutional data settings (p. 5) | No | Low | |
| Developed with Indigenous Peoples, scholars, non-profits and governments, building on Te Mana Raraunga, USIDSN and Maiam nayri Wingara (p. 1) | No | Low | |
| Further research needs (p. 8) | Yes | | |
| Extension to other collectives (p. 8) | Yes | | |
| Authors' own limitations | Paper has no limitations section. Further research list is used, which is fair. | | |

## Template compliance

| Item | Result |
|---|---|
| Summary word count | 394. Below the 400 minimum. About 492 after fixes 1, 3, 4 and 5. |
| Gist | 28 words, under 30. Says what the paper presents, not only topics. |
| Keywords | 11, inside 8 to 12 |
| Questions | 5, inside 4 to 7. Question 4 ("open by default") is not answered until fix 1 is applied. |
| House style | tricot written in lowercase throughout. maniva not used. |
| Format | Long format, all sections present. No relations field (optional). |
