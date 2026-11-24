# Card review: selby-2025-database

- **Card:** papers/selby-2025-database.md
- **Source:** papers-pdf/selby-et-al-2025.pdf (15 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 46 |
| Supported | 33 |
| Imprecise | 10 |
| Not in source | 2 |
| Contradicted | 1 |
| Source issues (problems in the source itself, not card errors) | 0 |
| Important omissions | 4 (all medium, none high) |
| Metadata issues | 3 |

The card is accurate on the core facts of the BrAPI standard (2014 start, 51 to 201 endpoints, four modules, more than 200 members) and describes the ClimMob section faithfully. The main problems are a Notes line that names only two Bioversity co-authors when the paper lists four, a closing summary sentence that presents the paper as "the reference" for tricot data flows when ClimMob gets two short paragraphs, and lost hedging ("may lack", "potentially including"). The gist is 30 words (limit is under 30) and not_established is missing.

## Fixes needed

1. **Notes, Bioversity co-authors (Contradicted).** Card says Laporte and de Sousa "are the co-authors from Bioversity International". The affiliation list gives Bioversity International (affiliation 19) to four authors: Kauê de Sousa, Valentin Guignon, Marie-Angélique Laporte and Mathieu Rouard. Johan Steven Aparicio is at CIAT (affiliation 7) (pp. 1 to 2). Replace the note with:
   `- Kauê de Sousa and Marie-Angélique Laporte are the co-authors listed in people.md. people.md records Laporte as leading the team's contribution. Valentin Guignon and Mathieu Rouard (Bioversity International) and Johan Steven Aparicio (CIAT) are also co-authors from the Alliance.`

2. **Summary, last sentence (Not in source, overstated).** Card says "For tricot, the paper is the reference for how on-farm ranking data enter the wider breeding data infrastructure." The paper never mentions tricot. ClimMob gets two short paragraphs (pp. 5 to 6) and one mention under Breedbase (p. 10). It states what ClimMob does with BrAPI but not how ranking data are mapped. Replace with:
   `For tricot users, the paper confirms that ClimMob can exchange germplasm lists and trial results with BrAPI-compatible breeding databases. It does not describe how ranking data map onto BrAPI models or name programmes that use this link.`

3. **Summary and Stated limitations, ClimMob data detail (Imprecise, hedge lost).** Card says the data "lack the detail of centralized experiments". The source says these data "may lack the detail of centralized experiments" (p. 5). The limitation bullet also adds "tricot", which the source does not use. Replace the summary sentence with:
   `The paper notes that these data may lack the detail of centralized experiments but can give robust evidence across many environments with greater external validity.`
   Replace the third limitation with:
   `- The paper notes that data collected through ClimMob may lack the detail of centralized experiments, which it weighs against wider coverage of environments and greater external validity.`

4. **Gist (metadata).** The gist is exactly 30 words (template says under 30). It describes topics ("Overview of ... with a showcase of") rather than what the paper shows, and "pushes tricot data back" uses a term the source does not use. Replace with (29 words):
   `gist: BrAPI v2, an open community standard for breeding data, has grown to 201 endpoints and many compatible tools, including ClimMob, which exchanges germplasm and trial data with breeding databases`

5. **not_established missing (metadata).** Add:
   `not_established: That ClimMob's BrAPI link is in routine use with a named breeding database (the paper describes the capability without examples, users or numbers); that tricot rankings map onto BrAPI data models without loss of information (not discussed); that BrAPI adoption raises genetic gain or speeds variety release (no evaluation is reported); that every tool shown supports BrAPI v2 (GLIS, PIPPA, FAIDARE indexing and BrAPI2ISA still work with v1.3 or v1.2); that the tool list is complete (the authors say it is not)`

6. **Summary, showcase sentence (Imprecise grouping).** The card puts Germinate and BMS under germplasm management and makes FAIDARE a separate "data discovery" group. In the paper, BMS, Germinate and FAIDARE all sit under "Breeding and genetics data management" (pp. 9 to 10). ClimMob sits under Phenotyping (p. 5). The General infrastructure group (BrAPIMapper, MIRA and BrAPI2ISA, GraphQL data warehouse, p. 12) is left out. Replace with:
   `The bulk of the paper is a showcase of BrAPI-compatible tools for phenotyping (Field Book, GridScore, ClimMob, ImageBreed, PHIS and others), genotyping (Gigwa, DArT sample submission, Flapjack and others), germplasm management (MGIS, the GLIS portal of the Plant Treaty, AGENT, Florilège, Helium), breeding data management (Breedbase, BMS, DeltaBreed, Germinate and the FAIDARE discovery portal) and analytics (QBMS, MrBean and ShinyBrAPPs for West African breeding programmes). A last group of infrastructure tools (BrAPIMapper, MIRA and a GraphQL data warehouse) helps developers adopt the standard.`

7. **Summary, looking ahead (Imprecise, more certain than source).** Card says the community "plans to extend the standard to" new data types. The source says it is committed to building standards for new uses, "potentially including" these types, and that each needs substantial discussion first (p. 13). Replace the start of the sentence with:
   `Looking ahead, the community intends to build standards for new data types, possibly including drone imaging, spectroscopy, metabolomics, agronomics and machine learning outputs,`

8. **Key numbers, GLIS row (attribution).** The figure of more than 1.9 million accessions with DOIs is cited to the GLIS website, reference 27 (p. 8). Change the Primary source cell to:
   `GLIS website (ref. 27), cited in this paper`

9. **Summary, version 2.0 changes (omission, medium).** After "Minor versions stay backwards compatible within a major version." add:
   `Version 2.0 added write and update functions, where version 1 had been read-only for phenotypes, and aligned BrAPI with MIAPPE and the GA4GH Variants schema.`

10. **Summary, hackathons (Imprecise).** Card says hackathons are the community's "main working format". The source calls them "a major staple" (p. 4). Replace "with hackathons twice a year as its main working format." with:
    `and its twice-yearly hackathons are a major staple of its work.`

11. **Summary, under-resourced programmes (Imprecise).** The source says extracting knowledge is time-consuming and often prevents adoption of new methods, especially in under-resourced programmes (p. 2). Replace the sentence with:
    `Turning these complex datasets into usable knowledge takes time, which often stops programmes, especially under-resourced ones, from adopting new methods.`

12. **Methods, content bullet (Not in source).** "written by their developers" is not stated. The paper calls them short success stories from the community, mostly from organizations independent of the BrAPI project (p. 4). Replace with:
    `- **Content.** Specification growth, versioning and modules, community history, and short success stories of BrAPI-compatible tools from the community, most built by organizations independent of the BrAPI project.`

13. **License (metadata).** The PDF states the Creative Commons Attribution License with a CC BY 4.0 link (p. 1). Change to `license: CC BY 4.0`.

14. **Notes, author count (Imprecise).** The paper lists 76 named authors plus the BrAPI Consortium (pp. 1 to 2). Replace with:
    `- 76 named authors plus the BrAPI Consortium. The card lists only the first five and the team's authors.`

With fixes 6, 9, 10 and 11 applied together with 2, 3 and 7, the summary is 494 words, inside the 400 to 500 range. If the curator wants more room, drop fix 9 and add that point to Notes instead.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | BrAPI v2. Real-world applications ... community | "BrAPI v2: real-world applications ..." (p. 1) | Supported (colon to period is expected) |
| authors | Selby P ... Alaux M, and ~70 co-authors including de Sousa K and Laporte MA, The BrAPI Consortium | 76 named authors plus The BrAPI Consortium. First five match (p. 1) | Supported (71 others, so "~70" is fair) |
| year | 2025 | Accepted 13 June 2025, Database (2025) (p. 1, p. 2) | Supported |
| journal | Database. The Journal of Biological Databases and Curation | PDF shows "Database" only (p. 1). Full name is correct outside knowledge | Supported |
| article | 2025, baaf048 | Vol. 2025, article ID baaf048 (p. 2) | Supported |
| type | software paper | "Original Article", overview of a data standard and tool showcase (p. 1) | Supported (reasonable) |
| doi | https://doi.org/10.1093/database/baaf048 | Same (p. 1) | Supported |
| license | CC BY | Creative Commons Attribution License, CC BY 4.0 link (p. 1) | Imprecise (add 4.0) |
| data | none (no new data generated) | "No new data were generated or analysed" (p. 13) | Supported |
| crops | any | Software-agnostic standard (abstract, p. 1). Examples cover banana, barley, wheat, cassava, sugarcane | Supported |
| region | global | International community and tools (pp. 1 to 13) | Supported |
| gist | Overview of BrAPI v2 ... pushes tricot data back | 30 words, topic list, "tricot" not in source | Imprecise |
| not_established | missing | Several stretch risks (see fix 5) | Missing |

Other fields: software lists tools that all appear in the source. The ClimMob URL is outside knowledge and correct. The relation `discusses: quiros-2024-compag` matches reference 9 (Quirós et al. 2024, p. 14).

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Large data volumes in separate single-task software create silos | Supported | Introduction (p. 2) | |
| 2 | Summary | Under-resourced programmes struggle most because extraction takes time | Imprecise | Extraction is time-consuming and often prevents adoption of new methods, especially in under-resourced programmes (p. 2) | Fix 11 |
| 3 | Summary | BrAPI set up 2014 as standardized web service API spec | Supported | p. 2, June 2014 on p. 4 | |
| 4 | Summary | REST over HTTP, JSON, language agnostic and stable | Supported | How it works (p. 2) | |
| 5 | Summary | Repositories map to BrAPI models, clients built once work everywhere | Supported | p. 3 | |
| 6 | Summary | Small tools built this way are called BrAPPs | Supported | Simple tools, often a single web page (p. 3) | |
| 7 | Summary | Value grows as more adopt | Supported | p. 3 | |
| 8 | Summary | Almost quadrupled, 51 (v1.0, 2017) to 201 (v2.1), four modules | Supported | p. 3. 201/51 = 3.94 | |
| 9 | Summary | Minor versions backwards compatible | Supported | p. 3 | |
| 10 | Summary | <10 people in 2014 to >200, hackathons twice a year as main working format | Imprecise | "a major staple", twice a year (p. 4) | Fix 10 |
| 11 | Summary | Showcase groups and tool placement | Imprecise | Section headings pp. 4 to 12, Figure 2 (p. 5) | Germinate, BMS, FAIDARE misplaced, infrastructure group missing. Fix 6 |
| 12 | Summary | ClimMob is a suite for decentralized research via citizen science and choice experiments, farmers rank | Supported | p. 5 | Source says farmers and other stakeholders |
| 13 | Summary | These data lack the detail of centralized experiments | Imprecise | "may lack" (p. 5) | Fix 3 |
| 14 | Summary | ClimMob retrieves germplasm, uploads data, pushes analysed results, insight into adoption | Supported | p. 6 ("potential adoption") | |
| 15 | Summary | Breedbase lists ClimMob among projects it connects to via BrAPI | Supported | p. 10 | |
| 16 | Summary | Community plans to extend standard to new data types | Imprecise | "potentially including", needs discussion (p. 13) | Fix 7 |
| 17 | Summary | Reuse GFF3, GeoTIFF, weather standards rather than reinvent | Supported | p. 13 (NOAA CDO for weather) | |
| 18 | Summary | Paper is the tricot reference for ranking data entering breeding infrastructure | Not in source | Tricot not mentioned. ClimMob section is two paragraphs (pp. 5 to 6) | Fix 2 |
| 19 | Methods | Community overview and technical description, not an experiment | Supported | p. 2 | |
| 20 | Methods | Case descriptions written by their developers | Not in source | Success stories, tools mostly from independent organizations (p. 4) | Fix 12 |
| 21 | Limitations | Showcase not exhaustive, website lists more | Supported | p. 4, p. 13 | |
| 22 | Limitations | New data types need community discussion | Supported | p. 13 | |
| 23 | Limitations | Tricot data via ClimMob lack detail | Imprecise | "may lack", no mention of tricot (p. 5) | Fix 3 |
| 24 | Key numbers | 2014 start | Supported | p. 2, p. 4 | |
| 25 | Key numbers | 51 → 201 endpoints | Supported | p. 3 | |
| 26 | Key numbers | 4 modules | Supported | p. 3, Figure 1 | |
| 27 | Key numbers | <10 → >200 members | Supported | p. 4 | |
| 28 | Key numbers | 2 hackathons per year | Supported | p. 4 | |
| 29 | Key numbers | 40 databases in FAIDARE | Supported | p. 10 | |
| 30 | Key numbers | >1.9 million accessions with DOIs in GLIS, "This paper" | Imprecise | Cited to GLIS website, ref. 27 (p. 8) | Attribution. Fix 8 |
| 31 | Key numbers | >16,000 CRAN downloads of QBMS | Supported | p. 11 | No date given in source |
| 32 | Notes | ClimMob gets one short section | Supported | pp. 5 to 6 | |
| 33 | Notes | Laporte and de Sousa are the co-authors from Bioversity International | Contradicted | Guignon and Rouard also Bioversity (affil. 19), Aparicio at CIAT (pp. 1 to 2) | Fix 1 |
| 34 | Notes | Around 75 named authors | Imprecise | 76 named authors (pp. 1 to 2) | Fix 14 |

Metadata claims (12 checked, see Metadata check): 10 Supported, 2 Imprecise (license, gist). not_established is missing and counted as a metadata issue, not a claim.

## Source issues

None found that affect the card. Figure 1 (p. 3) matches the four modules in the text. Figure 2 (p. 5) matches the tools described in the text. The 51 to 201 growth (3.94 times) fits "almost quadrupled". The GLIS count reads "more than 1.9 million" on p. 8 and "1.9 million" on p. 9, which is consistent.

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: overview of BrAPI progress and showcase of compatible tools | Yes | high | |
| Design: technical description plus community success stories | Yes | high | |
| Spec growth, modules, versioning, community size | Yes | high | |
| ClimMob uses of BrAPI (germplasm in, data and results out) | Yes | high | |
| v2.0 moved from read-only phenotypes to read, write and update, aligned with MIAPPE and GA4GH (p. 4) | No | medium | Fix 9. Relevant to FAIR tricot data |
| Several showcased tools still use v1.3 or v1.2 (GLIS p. 9, PIPPA p. 6, FAIDARE p. 10, BrAPI2ISA p. 12). FAIDARE v2 indexing to start in 2025 | No | medium | Covered in not_established (fix 5) |
| Community libraries for Java, JavaScript, Python, R and Drupal, plus a BrAPI Test Server (p. 4). QBMS pulls BrAPI data into R dataframes (p. 11) | Partly (QBMS named) | medium | Notes: `- Community libraries exist for R, Python, Java, JavaScript and Drupal. The QBMS R package pulls data from any BrAPI server into an R data frame, which may help tricot analysts who work in R (p. 11).` |
| General infrastructure tools: BrAPIMapper, MIRA and BrAPI2ISA, GraphQL warehouse (p. 12) | No | medium | Fix 6 |
| Figure 2 classes ClimMob under Core and Phenotyping, for data generation and storage (p. 5) | No | low | Notes: `- Figure 2 classes ClimMob under the Core and Phenotyping modules, as a tool for data generation and storage (p. 5).` |
| Authors' conclusion: aim of a digital data ecosystem where data flow from collection to quality control, analysis and storage (p. 13) | No | low | Optional |
| Global ex situ context: about 5.8 million accessions in about 1750 collections, cited to FAO (p. 8) | No | low | Optional Key numbers row, Primary source `FAO (2025), cited in this paper` |
| Funding: USDA NIFA grant 2022-67021-37024 (p. 13) | No | low | Optional |

## Template compliance

- Summary word count: 417 (target 400 to 500). Pass. With the suggested fixes it becomes 494.
- Gist length: 30 words. Fail (must be under 30). Fix 4 gives 29.
- Keywords: 10. Pass.
- Questions: 5. Pass.
- House style: tricot and maniva are lowercase throughout. Pass.
- not_established: missing. Add (fix 5).
