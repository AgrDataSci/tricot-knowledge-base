---
id: selby-2025-database
title: BrAPI v2. Real-world applications for data integration and collaboration in the breeding and genetics community
authors: Selby P, Abbeloos R, Adam-Blondon AF, Agosto-Pérez FJ, Alaux M, and ~70 co-authors including de Sousa K and Laporte MA, The BrAPI Consortium
year: 2025
journal: Database. The Journal of Biological Databases and Curation
journal_short: Database
article: 2025, baaf048
type: software paper
doi: https://doi.org/10.1093/database/baaf048
open_copy: https://doi.org/10.1093/database/baaf048
license: CC BY
data: none (no new data generated)
software: BrAPI specification v2.1, https://brapi.org. ClimMob, https://climmob.net. Other BrAPI-compatible tools described include Field Book, GridScore, Breedbase, BMS, DeltaBreed, Gigwa, Germinate, MGIS, FAIDARE, GLIS and the QBMS R package
crops: any
region: global
keywords: BrAPI, interoperability, data standards, API, breeding databases, ClimMob, germplasm, FAIR data, data integration, genebanks
gist: Overview of BrAPI v2, the open API standard for breeding data, with a showcase of compatible tools including ClimMob, which pulls germplasm from breeding databases and pushes tricot data back
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

Breeding programmes now produce large volumes of phenotypic, genotypic and germplasm data, but much of it sits in separate software built for single tasks, creating data silos. Under-resourced programmes struggle most, because extracting usable knowledge from fragmented data takes time. The Breeding Application Programming Interface (BrAPI) was set up in 2014 as a standardized web service specification for breeding and related agricultural data, so that databases and tools can exchange data without custom connections.

BrAPI follows the REST architecture over HTTP, with data represented in JSON, both of which are language agnostic and stable. Data repositories map their internal structures to BrAPI models and publish endpoints, and client tools built once against those endpoints work with any compatible repository. Small single-purpose tools built this way are called BrAPPs. The value of the standard grows as more databases and tools adopt it.

The specification has almost quadrupled in size, from 51 endpoints in version 1.0 (2017) to 201 in version 2.1, and is now organized into four modules (Core, Phenotyping, Genotyping and Germplasm). Minor versions stay backwards compatible within a major version. The community grew from fewer than ten people in 2014 to more than 200 members, with hackathons twice a year as its main working format.

The bulk of the paper is a showcase of BrAPI-compatible tools for phenotyping (Field Book, GridScore, PHIS, ImageBreed and others), genotyping (Gigwa, DArT sample submission), germplasm and genebank management (MGIS, the GLIS portal of the Plant Treaty, AGENT, Germinate, BMS), breeding data management (Breedbase, DeltaBreed), data discovery (FAIDARE) and analysis (QBMS, MrBean and ShinyBrAPPs for West African breeding programmes).

ClimMob is one of the showcased tools, described as a software suite for decentralized research through citizen science and choice experiments, where farmers rank varieties or practices. The paper notes that these data lack the detail of centralized experiments but give robust evidence across many environments with greater external validity. ClimMob uses BrAPI to retrieve curated germplasm information from breeding databases for trial design, to upload collected data automatically to a central breeding database, and to push analysed results back, giving breeders insight into likely adoption. Breedbase lists ClimMob among the projects it connects to through BrAPI.

Looking ahead, the community plans to extend the standard to new data types such as drone imaging, spectroscopy, metabolomics, agronomics and machine learning outputs, while reusing existing standards (GFF3, GeoTIFF, weather data standards) rather than reinventing them. For tricot, the paper is the reference for how on-farm ranking data enter the wider breeding data infrastructure.

## Methods in brief

- **Type.** Community overview and technical description of a data standard, not an experiment.
- **Content.** Specification growth, versioning and modules, community history, and short case descriptions of BrAPI-compatible tools written by their developers.

## Stated limitations

- The tool showcase is not exhaustive. The BrAPI website lists more compatible software.
- New data types (drone imaging, spectroscopy, omics, agronomics) still need community discussion before entering the standard.
- The paper notes that tricot data collected through ClimMob lack the detail of centralized experiments.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 2014 | Start of the BrAPI project | This paper |
| 51 → 201 endpoints | Growth from v1.0 (2017) to v2.1 | This paper |
| 4 modules | Core, Phenotyping, Genotyping, Germplasm | This paper |
| <10 → >200 | Community members, 2014 to publication | This paper |
| 2 per year | BrAPI hackathons | This paper |
| 40 databases | Federated plant research databases searchable through FAIDARE | This paper |
| >1.9 million | Germplasm accessions with DOIs in the Plant Treaty's GLIS | This paper |
| >16,000 | CRAN downloads of the QBMS R package | This paper |

## Notes

- ClimMob gets one short section. For ClimMob itself, use quiros-2024-compag.
- Marie-Angélique Laporte and Kauê de Sousa are the co-authors from Bioversity International. people.md records Laporte as leading the team's contribution.
- BrAPI is a live standard. Check brapi.org for the current version and compatible tools.
- Around 75 named authors plus the BrAPI Consortium. The card lists only the first five and the team's authors.
