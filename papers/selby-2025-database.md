---
id: selby-2025-database
title: BrAPI v2. Real-world applications for data integration and collaboration in the breeding and genetics community
authors: Selby P, Abbeloos R, Adam-Blondon AF, Agosto-Pérez FJ, Alaux M, and ~70 co-authors including de Sousa K and Laporte MA, The BrAPI Consortium
year: 2025
journal: Database. The Journal of Biological Databases and Curation
journal_short: Database
article: 2025, baaf048
type: software paper
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1093/database/baaf048
open_copy: https://doi.org/10.1093/database/baaf048
license: CC BY 4.0
data: none (no new data generated)
software: BrAPI specification v2.1, https://brapi.org. ClimMob, https://climmob.net. Other BrAPI-compatible tools described include Field Book, GridScore, Breedbase, BMS, DeltaBreed, Gigwa, Germinate, MGIS, FAIDARE, GLIS and the QBMS R package
crops: any
region: global
keywords: BrAPI, interoperability, data standards, API, breeding databases, ClimMob, germplasm, FAIR data, data integration, genebanks
gist: BrAPI v2, an open community standard for breeding data, has grown to 201 endpoints and many compatible tools, including ClimMob, which exchanges germplasm and trial data with breeding databases
not_established: That ClimMob's BrAPI link is in routine use with a named breeding database (the paper describes the capability without examples, users or numbers); that tricot rankings map onto BrAPI data models without loss of information (not discussed); that BrAPI adoption raises genetic gain or speeds variety release (no evaluation is reported); that every tool shown supports BrAPI v2 (GLIS, PIPPA, FAIDARE indexing and BrAPI2ISA still work with v1.3 or v1.2); that the tool list is complete (the authors say it is not)
relations:
  - discusses: quiros-2024-compag  # ClimMob as a BrAPI-compatible tool
---

## Questions this paper answers

- What is BrAPI and how does it work?
- How has the BrAPI standard and its community grown since 2019?
- Which breeding, genotyping and genebank tools are BrAPI compatible?
- How does ClimMob connect tricot trials to breeding databases?
- Where is the standard heading next?

## Summary

Breeding programmes now produce large volumes of phenotypic, genotypic and germplasm data, but much of it sits in separate software built for single tasks, creating data silos. Turning these complex datasets into usable knowledge takes time, which often stops programmes, especially under-resourced ones, from adopting new methods. The Breeding Application Programming Interface (BrAPI) was set up in 2014 as a standardized web service specification for breeding and related agricultural data, so that databases and tools can exchange data without custom connections.

BrAPI follows the REST architecture over HTTP, with data represented in JSON, both of which are language agnostic and stable. Data repositories map their internal structures to BrAPI models and publish endpoints, and client tools built once against those endpoints work with any compatible repository. Small single-purpose tools built this way are called BrAPPs. The value of the standard grows as more databases and tools adopt it.

The specification has almost quadrupled in size, from 51 endpoints in version 1.0 (2017) to 201 in version 2.1, and is now organized into four modules (Core, Phenotyping, Genotyping and Germplasm). Minor versions stay backwards compatible within a major version. Version 2.0 added write and update functions, where version 1 had been read-only for phenotypes, and aligned BrAPI with MIAPPE and the GA4GH Variants schema. The community grew from fewer than ten people in 2014 to more than 200 members, and its twice-yearly hackathons are a major staple of its work.

The bulk of the paper is a showcase of BrAPI-compatible tools for phenotyping (Field Book, GridScore, ClimMob, ImageBreed, PHIS and others), genotyping (Gigwa, DArT sample submission, Flapjack and others), germplasm management (MGIS, the GLIS portal of the Plant Treaty, AGENT, Florilège, Helium), breeding data management (Breedbase, BMS, DeltaBreed, Germinate and the FAIDARE discovery portal) and analytics (QBMS, MrBean and ShinyBrAPPs for West African breeding programmes). A last group of infrastructure tools (BrAPIMapper, MIRA and a GraphQL data warehouse) helps developers adopt the standard.

ClimMob is one of the showcased tools, described as a software suite for decentralized research through citizen science and choice experiments, where farmers rank varieties or practices. The paper notes that these data may lack the detail of centralized experiments but can give robust evidence across many environments with greater external validity. ClimMob uses BrAPI to retrieve curated germplasm information from breeding databases for trial design, to upload collected data automatically to a central breeding database, and to push analysed results back, giving breeders insight into likely adoption. Breedbase lists ClimMob among the projects it connects to through BrAPI.

Looking ahead, the community intends to build standards for new data types, possibly including drone imaging, spectroscopy, metabolomics, agronomics and machine learning outputs, while reusing existing standards (GFF3, GeoTIFF, weather data standards) rather than reinventing them. For tricot users, the paper confirms that ClimMob can exchange germplasm lists and trial results with BrAPI-compatible breeding databases. It does not describe how ranking data map onto BrAPI models or name programmes that use this link.

## Methods in brief

- **Type.** Community overview and technical description of a data standard, not an experiment.
- **Content.** Specification growth, versioning and modules, community history, and short success stories of BrAPI-compatible tools from the community, most built by organizations independent of the BrAPI project.

## Stated limitations

- The tool showcase is not exhaustive. The BrAPI website lists more compatible software.
- New data types (drone imaging, spectroscopy, omics, agronomics) still need community discussion before entering the standard.
- The paper notes that data collected through ClimMob may lack the detail of centralized experiments, which it weighs against wider coverage of environments and greater external validity.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 2014 | Start of the BrAPI project | This paper |
| 51 → 201 endpoints | Growth from v1.0 (2017) to v2.1 | This paper |
| 4 modules | Core, Phenotyping, Genotyping, Germplasm | This paper |
| <10 → >200 | Community members, 2014 to publication | This paper |
| 2 per year | BrAPI hackathons | This paper |
| 40 databases | Federated plant research databases searchable through FAIDARE | This paper |
| >1.9 million | Germplasm accessions with DOIs in the Plant Treaty's GLIS | GLIS website (ref. 27), cited in this paper |
| >16,000 | CRAN downloads of the QBMS R package | This paper |

## Notes

- ClimMob gets one short section. For ClimMob itself, use quiros-2024-compag.
- Kauê de Sousa and Marie-Angélique Laporte are the co-authors listed in people.md. people.md records Laporte as leading the team's contribution. Valentin Guignon and Mathieu Rouard (Bioversity International) and Johan Steven Aparicio (CIAT) are also co-authors from the Alliance.
- BrAPI is a live standard. Check brapi.org for the current version and compatible tools.
- 76 named authors plus the BrAPI Consortium. The card lists only the first five and the team's authors.
- Community libraries exist for R, Python, Java, JavaScript and Drupal. The QBMS R package pulls data from BrAPI-compatible databases into an R data frame (p. 11). This may help tricot analysts who work in R (curator's note, not a claim of the paper).
