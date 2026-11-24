# Card review: 1000farms-2025-report

- **Card:** papers/1000farms-2025-report.md
- **Source:** papers-pdf/dcp-1000farms-meetingreport_2025.pdf (22 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

Page numbers below are the numbers printed on the PDF pages ("Page | N"). The PDF page is always the printed number plus one, because the cover has no number (for example, printed p. 10 is PDF page 11).

## Overview

| Check | Result |
|---|---|
| Claims checked | 47 |
| Supported | 36 |
| Imprecise | 7 |
| Not in source | 4 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 6 |
| Important omissions | 3 (high), plus 5 medium |
| Metadata issues | 5 |

The card is accurate. Nearly every sentence it contains can be traced to the report, and nothing is contradicted. The problem is coverage. The summary gives about 120 words to the advancement group but leaves out the main outputs of the data analysis session, the challenges that implementing teams reported (which the card's first question asks about), and the action plans of three of the four cross-cutting groups. The most important fix is to rewrite the summary so it covers all sessions and all four groups (text below, 498 words), and to add a not_established field.

## Fixes needed

1. **Summary leaves out main results (high).** The card summarizes the advancement group in detail but does not report: the session 3 outputs on reports and advancement meetings (p. 10 to 11), the challenges from the word clouds (p. 12), and the action plans of the coordination, digital ecosystem and SOP groups (p. 17 to 20). The sentence "Cross-cutting teams covered the advancement process, a cross-crop coordination network and the digital ecosystem" names only three of the four groups (the SOP group is missing, p. 16) and repeats the next paragraph. The card's first question ("main obstacles to mainstreaming tricot") is not answered anywhere in the card. Replace the whole Summary with:

   > The report summarizes a three-day meeting held at the CIMMYT campus in Nairobi on 3 to 5 December 2024. It was convened by the Dryland Crops Program and the 1000FARMS Platform to share tricot experience across the CGIAR-NARES network and to plan how to mainstream it. Twenty-six people attended, including funders and CGIAR and NARES partners, and 15 of them were listed under CIMMYT. Four breakout sessions on sampling, trial design, data analysis and operations each produced ten key takeaways. Four cross-cutting groups then drafted action plans for the next 12 months.
   >
   > Implementing teams named their main challenges as logistics and planning, communication and language barriers, data management and lack of resources, and weak NARES ownership of the approach.
   >
   > On sampling, participants recommended mapping national and sub-national production zones to guide site selection, using existing surveys and census data to define farmer typologies, and sampling across agro-ecologies and typologies while avoiding biases introduced by intermediaries. Women, youth and smallholders should be included on purpose, without over-sampling that raises costs. Farmers with a record of timely data submission should be prioritized, and sites should allow spatial replication.
   >
   > On trial design, they called for SOPs that set minimum and maximum numbers of entries, plot sizes, seed quantities and yield measurement strategies by crop and purpose. Traits should link to target product profiles, trials should carry mandatory metadata such as trial purpose and candidate versus check, and default check varieties by crop and market segment would allow cross-trial analysis. Participants asked for ClimMob tools for yield validation, trial classification, seed loss and attrition, and for early engagement with variety release authorities.
   >
   > On analysis, they asked for customizable reports with yield advantage, spatial patterns, comparisons with checks and willingness to replant. These reports should feed structured advancement meetings with product teams, with pre-agreed thresholds and documented decisions. Participants also wanted market research every two to three years and feedback to farmers before the next season. A framework to estimate on-farm genetic gain from tricot data was also presented.
   >
   > On operations, they advised starting preparations six to twelve months before trials, identifying cost drivers such as seed, transport, data tools and agent payments early, reducing traits, optimizing sample size, clustering trials, setting up community data submission points, building national multi-crop coordination teams and training field agents.
   >
   > The advancement group set six principles, from inclusivity and multi-year on-farm, on-station and laboratory data to pre-agreed thresholds and continuous improvement. It planned to define the data needed at each stage and to set up advancement teams per crop and country. The coordination group planned to map cross-crop networks in at least three countries per region. The digital ecosystem group planned a data warehouse, ClimMob and BioFlow integration and shared governance rules. The SOP group proposed that the Accelerated Breeding Initiative lead SOP development, with a community of practice and links to crop ontologies. In the report's framing, the aim is for tricot to evolve from a method into a system for on-farm variety testing at scale.

   Sources for the new content: challenges p. 12 (word clouds, terms read off the figure, so approximate), CIMMYT count p. 21, inclusivity and over-sampling p. 6 takeaways 4 and 9, default checks p. 8 takeaway 9, release authorities p. 8 takeaway 7, reports and advancement meetings p. 10 and p. 11 takeaways 1 to 4, advancement plan p. 17, coordination p. 18, digital p. 18 to 19, SOPs p. 19 to 20.

2. **not_established is missing (high).** A meeting report is easy to stretch into evidence. Add:

   > not_established: that these recommendations improve data quality, cost or decisions (they are participants' proposals, not tested); that the 12-month action plans were carried out; that on-farm genetic gain has been estimated from tricot data (a framework was only presented); that CGIAR or national variety release systems have adopted tricot or these SOPs; that the views represent all CGIAR-NARES teams (26 participants, 15 listed under CIMMYT)

3. **Gist lists topics (medium).** The gist says what the meeting covered, not what it concluded. Replace with (25 words):

   > gist: CGIAR-NARES breeding teams agreed that mainstreaming tricot needs representative sampling, harmonized SOPs, structured advancement decisions, cost control and cross-crop coordination, and set 12-month action plans

4. **Stated limitations are not from the source (medium).** The report states no limitations. The card's line is a fair description but reads as if the authors said it. Replace with:

   > - The report states no limitations. It records participants' recommendations and plans, which were not tested (card's own note).
   > - Most participants were CGIAR staff. Of 26 people, 15 were listed under CIMMYT and two under national research institutes, KALRO and CSIR-Savanna Agricultural Research Institute (card's own count from the participant list, p. 21).

5. **Notes give organizer and author information that is not in the PDF (medium).** The PDF prints no author names and no organizer roles. The four people named are in the participant list, but their roles are not stated. The PDF file metadata lists only Kauê de Sousa as author. Replace the second note with:

   > - The PDF names no authors. According to the team (not stated in the PDF), the meeting was organized and the report prepared by Ganga Rao Nadigatla, Kauê de Sousa, Jacob van Etten and Harish Gandhi, who chose to publish under institutional names because the report was part of an institutionalization effort. All four appear in the participant list (p. 21).

6. **authors field (low).** The cover shows the logos of CIMMYT, the Alliance of Bioversity International and CIAT, and CGIAR (cover, PDF p. 1). The card writes "Bioversity International", which is not the institution shown. The program names come from the introduction (p. 2), which says the two programs convened the meeting, not that they wrote the report. Replace with:

   > authors: CIMMYT and Alliance of Bioversity International and CIAT (for the Dryland Crops Program and the 1000FARMS Platform)

7. **crops field (low).** The report names the Dryland Crops Program crops (p. 2) and gives beans and maize as examples (p. 5). Replace with:

   > crops: sorghum, millet, finger millet, groundnut, cowpea, common bean, pigeon pea, chickpea (Dryland Crops Program), maize, multi-crop

8. **region field (low).** The report says "across Africa" and "Africa-wide" (p. 2), not sub-Saharan Africa. Replace with:

   > region: Africa (meeting in Nairobi, Kenya, with examples from Rwanda and Malawi)

9. **Advancement principles (low).** The card says "systems that scale across crops and regions". The source principle is scalability and multidisciplinarity, across regions, crops and disciplines (p. 16). If the current summary is kept, change to "systems that work across regions, crops and disciplines".

10. **Genetic gain framework placement (low).** The card puts the van Heerwaarden framework under "analysis and decision-making". In the report it appears as a photo caption in the trial design pages (p. 9) and as a day 2 presentation (p. 3), not as an output of the analysis breakout. The rewritten summary in fix 1 handles this. If the current summary is kept, change to "A framework to estimate on-farm genetic gain from tricot data, presented by Joost van Heerwaarden, was also shown during the meeting."

11. **Key numbers (low).** Add these rows:

   > | 3–5 years | Proposed interval for reviewing adoption and market feedback data (text, p. 10). The session takeaway box gives 2–3 years for adoption reviews and market research (p. 11) | This report |
   > | 15 of 26 | Participants listed under CIMMYT (card's own count, p. 21) | This report |
   > | 3 countries per region | Minimum for mapping existing cross-crop coordination networks in the next 12 months | This report |
   > | 12 months | Horizon of the action plans of the four cross-cutting groups | This report |

12. **Source issues not flagged (low).** Add to Notes:

   > - The takeaway boxes are mislabelled in the source. The session 2 box on trial design is titled "Sampling and characterization" (p. 8), and the session 4 box is titled "Session 5" (p. 14).
   > - The interval for adoption reviews differs within the source: 3–5 years in the text (p. 10), 2–3 years in the takeaway box (p. 11).
   > - The source expands OFVT both as on-farm verification trials and as on-farm variety trials (p. 3), and PDT both as product development teams (p. 10) and as product design teams (p. 16).
   > - The PDF prints no authors, date of issue or licence. The year 2025 comes from the PDF file metadata (created July 2025).
   > - The report cites de Sousa et al. 2024 for the tricot approach (desousa-2024-asd) and Donovan et al. 2025 for video-based product concept testing (donovan-2025-expagric).

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Mainstreaming the tricot approach into the CGIAR-NARES Breeding Initiative. Insights from the meeting held in Nairobi, 3–5 December 2024 | Same, with subtitle on a new line and "3-5" (cover) | Supported (period for subtitle break is expected) |
| authors | CIMMYT (CGIAR Dryland Crops Program) and Bioversity International (1000FARMS) | No authors printed. Logos of CIMMYT, Alliance Bioversity & CIAT, CGIAR (cover). Convened by DCP and 1000FARMS (p. 2). File metadata author: Kauê de Sousa | Imprecise |
| year | 2025 | Not printed. PDF metadata: created 15 July 2025 | Supported (metadata only) |
| journal | Meeting report | Meeting report format throughout | Supported |
| article | meeting report | No volume or number | Supported |
| type | report | Report | Supported |
| doi | https://hdl.handle.net/10568/175957 | Handle not printed in the PDF. Record could not be reached during review | Not in source (not checkable) |
| license | see CGSpace record | No licence printed | Supported (follows template rule) |
| data | none | No dataset | Supported |
| crops | dryland crops and others in the CGIAR-NARES network | DCP crops listed (p. 2), beans and maize (p. 5) | Imprecise (vague, see fix 7) |
| region | sub-Saharan Africa | "across Africa", "Africa-wide" (p. 2), Nairobi, Rwanda, Malawi (p. 2, 13) | Imprecise (see fix 8) |
| gist | Report of a 26-person ... meeting setting recommendations ... | Accurate but lists topics | Imprecise (see fix 3) |
| not_established | missing | Needed for a non-empirical report | Missing (see fix 2) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Meeting in Nairobi, Dec 2024, convened by DCP with 1000FARMS to mainstream tricot | Supported | p. 2 (convened by DCP and 1000FARMS Platform), title | Source says the two programs convened it jointly. "project" vs "Platform" is minor |
| 2 | Summary | 26 participants incl. funders, CGIAR and NARES partners | Supported | p. 3, 26 names on p. 21 | Recounted: 26 |
| 3 | Summary | Four breakout sessions, then cross-cutting teams with 12-month plans | Supported | p. 3 to 4, 16 | |
| 4 | Summary | Map national and sub-national production zones for site selection | Supported | p. 6 takeaway 1 | |
| 5 | Summary | Sample across agro-ecologies and typologies, avoid intermediary bias | Supported | p. 6 takeaway 3 | |
| 6 | Summary | Prioritize farmers with timely data submission | Supported | p. 6 takeaway 5 | |
| 7 | Summary | Sites that allow spatial replication | Supported | p. 6 takeaway 8 | |
| 8 | Summary | SOPs set min and max entries, plot sizes, seed, yield strategies by crop and purpose | Supported | p. 8 takeaway 1 | |
| 9 | Summary | Mandatory metadata and shared glossary | Supported | p. 8 takeaway 3 | |
| 10 | Summary | ClimMob tools for yield validation, trial classification, seed loss and attrition | Supported | p. 8 takeaway 8 | |
| 11 | Summary | Align with market segments and TPPs, embed in national release systems | Supported | p. 7, p. 8 takeaways 2, 7, 9 | |
| 12 | Summary | Genetic gain framework presented by van Heerwaarden, under analysis | Imprecise | Caption p. 9, day 2 presentation p. 3 | Not an output of the analysis breakout (fix 10) |
| 13 | Summary | Market research every 2–3 years | Supported | p. 10, p. 11 takeaway 6 | Source gives 3–5 years for adoption reviews in the text (source issue) |
| 14 | Summary | Feedback to farmers before next planting season | Supported | p. 10, p. 11 takeaway 10 | |
| 15 | Summary | Start preparations 6 to 12 months before trials | Supported | p. 13 | Takeaway 1 (p. 14) says start right after the advancement meeting. Compatible |
| 16 | Summary | Identify cost drivers early (seed, transport, data tools, agent payments) | Supported | p. 14 takeaway 2 | |
| 17 | Summary | Reduce traits, optimize sample size, cluster trials | Supported | p. 14 takeaway 2 | |
| 18 | Summary | Community data submission points | Supported | p. 14 takeaway 4 | |
| 19 | Summary | National multi-crop coordination teams | Supported | p. 14 takeaway 6 | |
| 20 | Summary | Train field agents and partners | Supported | p. 14 takeaway 9 | |
| 21 | Summary | Cross-cutting teams covered advancement, coordination, digital ecosystem | Imprecise | p. 16 lists four groups | SOP group missing. Redundant with next paragraph (fix 1) |
| 22 | Summary | Final session: four groups, steps for next 12 months | Supported | p. 16 | |
| 23 | Summary | Shared themes: ownership, interoperability, MS and TPP alignment, rigorous and user-friendly protocols | Supported | p. 16 | |
| 24 | Summary | Tricot to evolve from a method into a system | Supported | p. 16 | Correctly framed as the report's view |
| 25 | Summary | Six advancement principles as listed | Imprecise | p. 16 | Count of six is right. "Disciplines" dropped from the scalability principle (fix 9) |
| 26 | Summary | Priorities: role and weight of data types, earlier planning with PDTs, capacity | Supported | p. 16 | Advancement Process Toolkit (p. 17) not mentioned |
| 27 | Methods | Three-day in-person meeting, breakouts on four themes, then cross-cutting teams | Supported | p. 3 to 4 | |
| 28 | Methods | Outputs: recommendations per theme and 12-month plans | Supported | p. 4, 16 | |
| 29 | Limitations | A meeting report of participants' views, not an empirical study | Not in source | No limitations stated | Fair, but must be labelled as the card's own note (fix 4) |
| 30 | Key numbers | 26 participants | Supported | p. 3, p. 21 | |
| 31 | Key numbers | 3–5 Dec 2024 | Supported | Cover, p. 2 | |
| 32 | Key numbers | 6–12 months preparation | Supported | p. 13 | |
| 33 | Key numbers | 2–3 years market research | Supported | p. 10, 11 | |
| 34 | Notes | Organizers and report preparers named | Not in source | p. 21 lists them as participants only | Label as team information (fix 5) |
| 35 | Notes | Authors chose institutional names | Not in source | Not stated | Label as team information (fix 5) |
| 36 to 47 | Frontmatter | title, authors, year, journal, article, type, doi, license, data, crops, region, gist | See Metadata check | | 7 Supported, 4 Imprecise, 1 Not in source |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Session 2 takeaway box titled "Sampling and characterization" instead of trial design | p. 8 (PDF 9) | No | See fix 12 |
| Session 4 takeaway box titled "Session 5" | p. 14 (PDF 15) | No | See fix 12 |
| Adoption review interval 3–5 years in text, 2–3 years in takeaway box | p. 10 vs p. 11 | No | See fix 12 |
| OFVT expanded two ways (verification trials, variety trials) | p. 3 | No | See fix 12 |
| PDT expanded two ways (product development teams, product design teams) | p. 10 vs p. 16 | No | See fix 12 |
| No authors, issue date or licence printed. Year only in file metadata | Cover, p. 1 to 21 | Partly (Notes give authors without a source label) | See fix 12 |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim and objectives a to d (cross-learning, coordination, frameworks for scaling, strengthen tricot for OFVT) | Partly | Low | Covered in rewritten summary, sentence 2 |
| Design: three days, four breakouts with ten takeaways each, four cross-cutting groups | Yes | Medium | Ten takeaways added in fix 1 |
| Participants: 26, 15 under CIMMYT, two national institutes | Partly | Medium | Fix 1, fix 4, fix 11 |
| Challenges reported by implementing teams (logistics, language and communication, data and resources, NARES ownership) | No | High | Fix 1. Card question 1 depends on it |
| Session 3 outputs: report content, structured PDT advancement meetings, thresholds, decision documentation, calendar | No (only market research and farmer feedback) | High | Fix 1 |
| Action plans of coordination, digital ecosystem and SOP groups | No | High | Fix 1 |
| Inclusivity of women, youth, smallholders, and the cost trade-off of over-sampling | No | Medium | Fix 1 |
| Default check varieties by crop and market segment, debate on classifying trials | No | Medium | Fix 1 adds default checks |
| Sentinel network of trained farmers, incentives, catalytic funds, fewer field visits, random data audits | No | Medium | Optional. "Participants also suggested a core network of trained farmers, fewer field visits with random data quality audits, and pooled funds for multi-crop trials." |
| Digital principles: FAIR governance without assuming open access, hybrid data collection (ODK, USSD, IVR, paper) | No | Medium | Optional Notes line |
| Aligned initiatives (Market Intelligence, RTB Breeding, Seed Equal, CIMMYT maize team) | No | Low | Optional Notes line |
| Citation of Donovan et al. 2025 for video-based concept testing | No | Low | Fix 12, and consider a relations entry to donovan-2025-expagric |
| Authors' own limitations | None stated | n/a | Fix 4 |
| Conclusion: tricot from method to system | Yes | High | Kept |

## Template compliance

- Summary word count: 461 (target 400 to 500). Passes. The proposed rewrite is 498 words.
- Gist: 26 words (under 30). Passes on length, but lists topics (fix 3). Proposed gist is 25 words.
- Keywords: 12 (8 to 12). Passes.
- Questions: 5 (4 to 7). Passes. Question 1 is not answered by the current card body.
- House style: tricot in lowercase throughout. Passes. No maniva mentions.
- not_established: missing. Should be added for a report of this kind.
- relations: none. Optional. The source cites desousa-2024-asd and donovan-2025-expagric.
