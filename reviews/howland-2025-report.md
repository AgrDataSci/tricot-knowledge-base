# Card review: howland-2025-report

- **Card:** papers/howland-2025-report.md
- **Source:** full report /home/claude/work/pdfs/howland-et-al-2025-full.pdf (117 pages), with text in /home/claude/work/txt/howland-et-al-2025-full.txt. The repo copy papers-pdf/howland-et-al-2025.pdf is a one-page stub and was not used.
- **Reviewed:** 2026-11-26, by an independent agent (pilot)
- **Verdict:** Major fixes

Page numbers below are PDF page numbers. From PDF page 22 onward the printed page number is the same. PDF pages 1 to 21 all carry the printed number "2" (a broken page field in the source).

## Overview

| Check | Result |
|---|---|
| Claims checked | 64 |
| Supported | 54 |
| Imprecise | 7 |
| Not in source | 0 |
| Contradicted | 3 |
| Source issues (problems in the source itself, not card errors) | 14 |
| Important omissions | 5 |
| Metadata issues | 4 |

The card is careful and well organised, and almost all survey numbers match the tables exactly. The main problem is how it explains the "weak" contribution rating for Ethiopia and Haiti. The report defines weak as too little evidence for the 1000FARMS causal pathway, with other externally funded programmes explaining the change. The card instead says weak means little direct support and that it shows national partners running tricot "on their own", which the report contradicts for Haiti (pp. 17, 39, 44, 49, 50). This error appears in the Summary, the Notes and, more softly, in the gist and not_established. The gist is also one word over the limit.

## Fixes needed

1. **Meaning of the "weak" rating (Summary, paragraph 5).**
   Card: "Weak here means these countries received little direct project support, yet national universities and institutes still implemented tricot, drawing on earlier Dutch-funded projects, Seeds for Needs and USAID Innovation Labs. This shows national partners able to run tricot on their own, and 1000FARMS reaching actors beyond its project scope, mainly through its webinars and online resources."
   Source: weak means insufficient evidence was found to support the 1000FARMS causal mechanism (Table 1, p. 17, and pp. 39, 44, 50). A direct rival mechanism explains the change: REALISE, ISSD, Seeds for Needs and AVISA in Ethiopia, and USAID Innovation Labs with Cornell, CIAT and CIP in Haiti (Table 15, p. 50). 1000FARMS did run training and webinars in Ethiopia (p. 40). In Haiti, implementation still depends on external budget (p. 49), and the spillover hypothesis was "partly rejected" (p. 44) or "not verified" beyond knowledge (pp. 10, 58). Only Ethiopia shows replication with own funds (p. 49).
   Replace with: "Weak here means too little evidence that the 1000FARMS pathway caused the change. Other programmes explain it better: Dutch-funded projects, Seeds for Needs and AVISA in Ethiopia, and USAID Innovation Labs with Cornell, CIAT and CIP in Haiti. In Haiti, 1000FARMS mainly added knowledge through its webinars, so the spillover hypothesis was only partly supported."
   (One word shorter than the current text. The Ethiopian own-funding point is already in paragraph 4.)

2. **Same error in Notes (third bullet).**
   Card: "It means the project gave little direct support, while national partners implemented tricot by themselves, which points to stand-alone national capacity and to 1000FARMS reaching beyond its scope."
   Source: as in fix 1 (pp. 17, 39, 44, 49, 50).
   Replace the whole bullet with: "A 'weak' contribution rating in Ethiopia and Haiti does not mean tricot failed there. It means the evaluators found too little evidence for the 1000FARMS causal pathway, while other programmes explain the observed use (REALISE, ISSD, Seeds for Needs and AVISA in Ethiopia, and USAID Innovation Labs with Cornell, CIAT and CIP in Haiti). Only in Ethiopia did universities and an institute fund tricot from their own resources. In Haiti the report says implementation still depends on external funding, and the spillover is shown for knowledge through webinars, not yet for implementation."

3. **Gist (over 30 words and same framing).**
   Card (31 words): "Independent evaluation of 1000FARMS (195-person survey, 21 interviews, four countries) finding tricot used for variety decisions, including in Ethiopia and Haiti, where national partners ran it with little direct 1000FARMS support"
   Source: p. 50 and fix 1.
   Replace with (27 words): "Independent evaluation (195-person survey, 21 interviews) finds tricot data used for variety decisions in four countries, with 1000FARMS' contribution rated commingled (Ghana, Uganda) or weak (Ethiopia, Haiti)"

4. **not_established, first item.**
   Card: "that 1000FARMS alone caused the uptake of tricot, since it acted with other programmes in Ghana and Uganda and gave little direct support in Ethiopia and Haiti"
   Replace with: "that 1000FARMS alone caused the uptake of tricot, since other programmes acted alongside it in Ghana and Uganda and the evaluators found too little evidence of its contribution in Ethiopia and Haiti"

5. **Denominator of the 64% use figure (Summary, paragraph 3).**
   Card: "64% of applicable respondents said their programme used tricot data for breeding decisions".
   Source: Table 7 (p. 29) gives 91 of 143, and the 143 include 26 "Not applicable" answers. Among applicable answers it would be 91 of 117 (78%, reviewer's calculation).
   Replace with: "64% of the 143 who answered (including 26 who said not applicable) said their programme used tricot data for breeding decisions".

6. **Notes on the 64% denominator.**
   Card: "The 64% use figure excludes respondents who skipped the question."
   Source: the report does not say why only 143 of 195 answered (p. 29).
   Replace with: "The 64% use figure is 91 of 143. The report does not say why only 143 of the 195 answered, and the 143 include 26 'not applicable' answers."

7. **Key numbers row "21".**
   The report never states 21. It is the sum of Table 2 (5 + 8 + 2 + 6, p. 20).
   Replace the Context cell with: "Key informant interviews (5 Ethiopia, 8 Ghana, 2 Haiti, 6 Uganda). Total is the card's sum of Table 2". Keep "This report" as primary source.

8. **Key numbers row "USD 20,000".**
   Source: "Grants of 20,000 USD have been awarded to NARO" (p. 47). The appendix presents USD 20,000 as the catalytic grant size in general (p. 64) and says two grants went to NARO-NaSARRI (p. 104).
   Replace the Context cell with: "Size of 1000FARMS catalytic grants, awarded to NARO, Uganda, for tricot pilots (staff report two grants to NARO-NaSARRI)".

9. **Notes on the date.**
   Card: "the PDF is dated February 2026".
   Source: no date is printed anywhere in the PDF. Only the file metadata give a creation date of 13 February 2026.
   Replace with: "The citation year is 2025, but fieldwork ran from July 2025 to January 2026 (p. 12) and the PDF carries no printed date. Its file metadata give 13 February 2026."

10. **Add a Notes bullet on a source inconsistency (EIAR versus Oromia).** See Source issues, row 3.
    Add: "The report credits EIAR breeders with recommending two wheat and two teff varieties (pp. 7, 40). Its Ethiopia appendix links this result to a researcher from the Oromia Agricultural Research Institute working in the ISSD project in 2019 (p. 68)."

11. **Add the impact trajectory ratings (Summary, paragraph 4).** Medium importance.
    Card: "Ethiopia was rated the most advanced, with universities and an agricultural institute funding tricot from their own resources, helped by an earlier start."
    Replace with: "Ethiopia was the only trajectory rated confirmed (the others initiated), with universities and an agricultural institute funding tricot from their own resources, helped by an earlier start." (Source: Table 15, p. 50, and p. 49.)

12. **Add practical points a tricot user would ask about (Notes).** Medium importance.
    Add: "Interviewees named practical risks. Unreleased seed left with farmers can break variety release law and spread disease (Uganda, p. 116). Farmers ranked varieties with higher code numbers higher (Uganda, p. 116). One breeder found more than 30 traits too many to collect (p. 108). In one Ghana trial a quarter of the data was removed after cleaning (p. 89). National researchers were often not involved in data analysis in Ethiopia and Ghana, which limits capacity building (p. 48)."

13. **Add the variety release enabler (Notes).** Medium importance.
    Add: "Informants saw national variety release rules that require on-farm data as a key enabler in Ghana and Uganda. Ethiopia and Haiti lack this mandate, so tricot there depends more on projects and individual leaders (Table 17, pp. 52 to 53)."

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | 1000FARMS. Scaling the use of tricot data for breeding decisions. An outcome study | "1000FARMS- Scaling the use of tricot data for breeding decisions- an outcome study" (p. 1) | Supported (hyphens turned into periods, house style) |
| authors | Howland F, Quintero Cano K, Caleño E, Moreno M | Fanny Howland, Katherine Quintero Cano, Edwin Caleño, Manuel Moreno (p. 1) | Supported |
| year | 2025 | No date printed. Work ran July 2025 to January 2026 (pp. 12, 56). File metadata: 13 February 2026 | Not checked (no web access). PDF evidence points to 2026. The card flags this in Notes |
| journal | Outcome study, Bioversity International and CIAT, Cali, Colombia | Affiliation "Alliance of Bioversity International and International Center for Tropical Agriculture (CIAT)" (p. 1). No place of publication in the PDF | Not checked (no web access). "Cali, Colombia" is not in the PDF |
| article | 117 p. | 117 pages | Supported |
| type | report | Outcome study report | Supported |
| doi | https://hdl.handle.net/10568/181675 | Not in PDF | Not checked (no web access) |
| license | see CGSpace record | No licence statement in PDF | Supported (matches template rule) |
| data | none | No data availability statement or shared dataset | Supported |
| crops | wheat, teff, sorghum, maize, rice, millet, fava bean, common bean, cowpea, groundnut, soybean, sweet potato, potato, cassava, yam, banana, cocoa | Table 2 (p. 20), pp. 39, 42, 44, 46, 48, 77 | Supported |
| region | Ethiopia, Ghana, Haiti, Uganda, online survey across many other countries | Four case countries, 146 survey respondents from other countries (p. 25) | Supported |
| gist | see fix 3 | p. 50 | Imprecise, and 31 words (limit is under 30) |
| not_established | five items | pp. 10, 33, 50, 60 | First item Imprecise (fix 4). Other items Supported |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Independent outcome study by PISA4i, July 2025 to January 2026 | Supported | pp. 12, 56 | |
| 2 | Summary | Two evaluation questions, Haiti as non-targeted country | Supported | pp. 6, 14 to 15 | |
| 3 | Summary | ToC reconstructed and tested against rivals via contribution analysis | Supported | p. 15 | |
| 4 | Summary | 195 of about 1,800, 21 remote interviews, project documents | Supported | pp. 18, 20 | 21 is a sum of Table 2 |
| 5 | Summary | Nigeria left out as already well documented | Supported | p. 15, footnote 2 | |
| 6 | Summary | Benin dropped out after a single reply | Supported | p. 16 | Single reply to the interview invitation |
| 7 | Summary | 96% / 94% / 88% aware of OFT, tricot, ClimMob | Supported | p. 25 | |
| 8 | Summary | 64% trust tricot data more | Supported | Table 4, p. 26 | 125 of 195 |
| 9 | Summary | 64% "of applicable respondents" used tricot data | Imprecise | Table 7, p. 29 | Denominator 143 includes 26 not applicable (fix 5) |
| 10 | Summary | 66% use ClimMob | Supported | Table 9, p. 31 | |
| 11 | Summary | Leadership decision top driver (60%), ahead of 1000FARMS evidence and training | Supported | Table 8, p. 30 | 53 of 89 |
| 12 | Summary | 42% report tricot-inspired protocols, interviews less clear | Supported | pp. 8 to 9, 33 | |
| 13 | Summary | Tricot data inform recommendations, release dossiers, seed promotion | Supported | pp. 7 to 8, 48 | |
| 14 | Summary | EIAR breeders recommended 2 wheat and 2 teff varieties | Supported | p. 40 | Source issue: appendix links it to Oromia researcher (p. 68) |
| 15 | Summary | Ghana north and south institutes tested same genotypes with farmers and consumers | Supported | p. 42 | |
| 16 | Summary | Haiti sweet potato varieties entered official technology packages | Supported | p. 44 | |
| 17 | Summary | Uganda breeders gained confidence and data for release dossiers | Supported | p. 46 | |
| 18 | Summary | Ethiopia most advanced, own funding, earlier start | Supported | pp. 10, 49, 57 | Mekelle invests staff and vehicles, not money. Trajectory rating not given (fix 11) |
| 19 | Summary | Commingled in Ghana and Uganda with CIP, CIAT, AVISA, RTB, NextGen Cassava | Supported | pp. 41, 46, 50 to 51 | |
| 20 | Summary | Weak in Ethiopia and Haiti | Supported | Table 15, p. 50 | |
| 21 | Summary | Weak means little direct project support | Contradicted | Table 1, p. 17. pp. 39, 44, 50 | Weak means insufficient evidence for the 1000FARMS mechanism. 1000FARMS did train in Ethiopia (p. 40) |
| 22 | Summary | Partners drew on Dutch-funded projects, Seeds for Needs, USAID Innovation Labs | Imprecise | Table 15, p. 50 | Omits AVISA (Ethiopia) and CIAT, CIP, Cornell (Haiti) |
| 23 | Summary | Shows national partners able to run tricot on their own | Contradicted | pp. 44, 49, 50 | Change explained by other external programmes. Haiti still depends on external budget (p. 49) |
| 24 | Summary | 1000FARMS reaching beyond its scope, mainly via webinars and online resources | Imprecise | pp. 10, 44, 48, 58 | Spillover "partly rejected" or "not verified" beyond knowledge. Ethiopia is a target country, so "beyond scope" fits only Haiti |
| 25 | Summary | Distinct role: awareness, training, ad hoc support, grants, links. Not all informants knew the project | Supported | pp. 10, 51, 58 | |
| 26 | Summary | Lessons: funding, directors, field agent incentives and formality, farmer feedback, weak seed systems | Supported | pp. 53 to 56, 58 | |
| 27 | Summary | ClimMob valued for design and data collection, data exported to R | Supported | p. 54 | |
| 28 | Summary | Gap between published claims (cost-effectiveness, data quality) and implementers | Supported | pp. 11, 60 | |
| 29 | Methods | Theory-based CA after Howland et al. (2024), six components | Supported | pp. 15 to 17 | |
| 30 | Methods | Survey to about 1,800, 195 responses by country, descriptive stats and bigrams | Supported | pp. 18, 20, 25 | |
| 31 | Methods | 21 interviews (5, 8, 2, 6), NARES, university, CGIAR, NGO | Supported | Table 2, p. 20 | Total is derived |
| 32 | Methods | Secondary data | Supported | p. 18 | |
| 33 | Methods | Case selection, Nigeria and Benin excluded, Haiti for spillover | Supported | pp. 15 to 16 | |
| 34 | Limitations | Purposive sampling may bias | Supported | p. 20 | |
| 35 | Limitations | Few informants per country, notably Haiti and Ghana | Supported | p. 20 | The Haiti and Ghana examples are the card's |
| 36 | Limitations | Low response rate, duplicates and one-off webinar participants | Supported | p. 18 | |
| 37 | Limitations | Attribution hard because 1000FARMS works through other programmes | Supported | pp. 11, 58 | |
| 38 | Limitations | May be too early to detect spillover | Supported | p. 48 | |
| 39 | Limitations | Enablers and barriers are perceptions | Supported | pp. 51 to 53 | |
| 40 | Key numbers | 195 of ~1,800 | Supported | p. 18 | Response rate about 11% (reviewer's calculation) |
| 41 | Key numbers | 21 interviews | Imprecise | p. 20 | Unlabelled sum of Table 2 (fix 7) |
| 42 | Key numbers | 96% / 94% / 88% | Supported | p. 25 | |
| 43 | Key numbers | 54.4% / 66.7% / 21.5% training, webinars, grants | Supported | Table 3, p. 25 | 106, 130, 42 of 195 |
| 44 | Key numbers | 64% (125 of 195) trust | Supported | Table 4, p. 26 | 64.1% |
| 45 | Key numbers | 64% (91 of 143) used for decisions | Supported | Table 7, p. 29 | 63.6% |
| 46 | Key numbers | 59.6% (53 of 89) leadership driver | Supported | Table 8, p. 30 | |
| 47 | Key numbers | 66% (128 of 195) use ClimMob | Supported | Table 9, p. 31 | 65.6% |
| 48 | Key numbers | 83% (135 of 163) reports useful | Supported | Table 5, p. 26 | 55 + 80 = 135. 82.8% |
| 49 | Key numbers | 42% (82 of 195), 19% under consideration | Supported | Table 10, p. 33 | 38 of 195 |
| 50 | Key numbers | 82% (159 of 195) facilitate collaboration | Supported | Table 12, p. 34 | 81.5% |
| 51 | Key numbers | USD 20,000 grant to NARO | Imprecise | pp. 47, 64, 104 | Plural grants, standard grant size (fix 8) |
| 52 | Key numbers | 2 + 2 wheat and teff varieties, EIAR | Supported | p. 40 | Source issue on attribution (p. 68) |
| 53 | Notes | papers-pdf copy is a one-page pointer | Supported | Caller's information | Card checked against full report |
| 54 | Notes | Authors are PISA4i evaluation team, external | Supported | p. 12 | Report calls itself an independent analysis |
| 55 | Notes | Weak means little direct support, stand-alone national capacity | Contradicted | pp. 17, 39, 44, 49, 50 | Fix 2 |
| 56 | Notes | Haiti spillover shown for knowledge via webinars, not implementation | Supported | pp. 44, 48 | |
| 57 | Notes | PDF is dated February 2026 | Imprecise | File metadata only | No printed date (fix 9) |
| 58 | Notes | Denominators 195, 163, 143, 89 | Supported | Tables 4, 5, 7, 8 | Table 11 also uses 136 |
| 59 | Notes | 64% excludes respondents who skipped | Imprecise | p. 29 | Reason for 143 not given. Includes not applicable (fix 6) |
| 60 | Notes | Ghana 12% vs 12.5%, rows over 100% | Supported | pp. 8, 9, 32, 33 | Uganda in Table 10 sums to 101% |
| 61 | Notes | BMGF "on-farm trial verification" another name for tricot, confusing | Supported | pp. 43, 51, 83 | Attributed to a CIP breeder |
| 62 | Notes | Ghana director disagreed, breeders stopped. NARO rice dropped tricot as too costly | Supported | pp. 7, 42, 46 | Rice still uses tricot for cooking tests (p. 115) |
| 63 | Relations | de Sousa 2024 cited for cost efficiency and decisions | Supported | pp. 14, 53 | |
| 64 | Relations | Nabateregga and Ulzen cited as 2024 for farmer data accuracy | Supported | p. 53 | |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| 1. The PDF has no licence statement. | Whole PDF | Yes, indirectly (license points to CGSpace) | "The full report PDF carries no licence statement. Check the CGSpace record before reuse." |
| 2. No publication date is printed. The work ended January 2026 and the file metadata give 13 February 2026, while the card year is 2025. | pp. 1, 12, 56 | Yes (fix 9 sharpens it) | See fix 9 |
| 3. The 2 wheat and 2 teff variety recommendations are credited to EIAR breeders in the text but to an Oromia Agricultural Research Institute researcher (ISSD project) in the appendix. | pp. 7, 40 vs p. 68 | No | See fix 10 |
| 4. Haiti spillover is described three ways: "partly rejected" with "partial spillover effect", "not verified" beyond knowledge, and "no clear spillover" yet. | pp. 10, 44, 48, 58 | Partly | "The report words the Haiti spillover result in different ways, from partly rejected to not verified beyond knowledge gains." |
| 5. Table 15 puts "weak" (a strength-of-contribution category) and "commingled" (a mechanism type) in the same column. The text alternates "combined" and "commingled". | Table 1 p. 17, Table 15 p. 50 | No | "The report mixes two scales in Table 15. 'Commingled' is a type of mechanism and 'weak' a strength rating. 'Combined' in the text means commingled." |
| 6. Ethiopia appendix shows impact trajectory "Initiated" for the primary mechanism row, while text and Table 15 say "Confirmed". | p. 63 vs pp. 39, 50 | No | Low priority, no Notes text needed |
| 7. Table 7 has 91 users, but Table 8 (drivers among users) has N = 89. The text says Haiti 100% "of applicable respondents" while the 143 total includes not applicable answers. | pp. 29, 30 | No | "Table 7 counts 91 users but Table 8 counts 89." |
| 8. Ghana guideline integration given as 12% and 12.5% (1 of 8). | pp. 9, 32 | Yes | |
| 9. Rounded percentages make some rows sum above 100% (for example Uganda, Table 10). | p. 33 | Yes | |
| 10. Grant counts conflict between survey and staff: Ethiopia 1 vs none, Ghana 3 vs 1, Uganda 6 vs 2. | pp. 64, 77, 83, 104 | No | "Survey respondents report more grants than 1000FARMS staff do (Ethiopia 1 vs 0, Ghana 3 vs 1, Uganda 6 vs 2)." |
| 11. The regional cowpea tricot protocol lists Ghana, Mali and Nigeria in one place, Ghana and Mali elsewhere. | p. 9 vs pp. 42, 48 | No (card does not use it) | None needed |
| 12. Pages 1 to 21 all print "2", and one cross-reference is broken ("Error! Reference source not found."). | pp. 1 to 21, p. 48 | No | "Cite this report by PDF page. Printed page numbers start working at p. 22." |
| 13. The total of 21 interviews is never stated. Only per-country counts appear. | Table 2, p. 20 | No | See fix 7 |
| 14. An informant's premise that tricot "is cost effective" sits in the Ghana appendix, while the conclusion says accounts contradict cost-effectiveness claims. | p. 87 vs p. 60 | Partly ("partly contests") | None needed. The card's "partly contests" fits |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim and evaluation questions | Yes | High | |
| Design (theory-based CA, survey, interviews, documents) | Yes | High | |
| Sample sizes | Yes | High | |
| Contribution ratings per country | Yes, but "weak" misexplained | High | Fixes 1 to 4 |
| Impact trajectory ratings (Ethiopia confirmed, others initiated) | No | Medium | Fix 11 |
| Variety release rules requiring on-farm data as an enabler (Ghana, Uganda, not Ethiopia, Haiti) | Partly (release dossiers mentioned) | Medium | Fix 13 |
| National researchers not involved in data analysis (Ethiopia, Ghana) | No | Medium | Fix 12 |
| Practical risks: unreleased seed, label number bias, too many traits, data loss after cleaning | No | Medium | Fix 12 |
| Authors' recommendations: engage breeding and NARES directors and ministries, prioritise crops and programmes with experience, avoid tree and vegetatively propagated crops at first, improve ClimMob usability | Partly | Medium | Add to Notes: "The authors recommend engaging breeding and NARES directors and ministries, starting with programmes that have experience and interest, and crops that are easier than tree and vegetatively propagated crops (p. 54)." |
| Self-rated technical knowledge, 77% good or very good (150 of 195) | No | Low | Optional Key numbers row |
| Collaboration partners (farmer organisations most cited, 101 of 136) | No | Low | Optional |
| Tricot seen to widen participation of women and youth | No | Low | Optional |
| Authors' limitations | Yes | High | |
| Conclusions including literature-practice gap | Yes | High | |

## Template compliance

- Summary word count: 480 (target 400 to 500). Fixes 1, 5 and 11 together add about 10 words, so it stays under 500.
- Gist: 31 words, over the limit of under 30. Fix 3 gives 27 words.
- Keywords: 12 (within 8 to 12).
- Questions: 7 (within 4 to 7).
- House style: tricot and maniva lowercase throughout. No em dashes or semicolons found in the card prose.
