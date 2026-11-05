---
id: arnaud-2023-jsfa
title: Connecting data for consumer preferences, food quality, and breeding in support of market-oriented breeding of root, tuber, and banana crops
authors: Arnaud E, Menda N, Tran T, Asiimwe A, Kanaabi M, Meghar K, Forsythe L, Kawuki R, Ellebrock B, Kayondo IS, Agbona A, Zhang X, Mendes T, Laporte MA, and 12 co-authors
year: 2023
journal: Journal of the Science of Food and Agriculture
journal_short: J Sci Food Agric
article: 104(8), 4514-4526 (published online 2023)
type: review
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1002/jsfa.12710
open_copy: https://doi.org/10.1002/jsfa.12710
license: CC BY 4.0
data: sensory, biochemical and NIRS data in the crop Breedbase databases (CassavaBase, MusaBase, PotatoBase, SweetPotatoBase, YamBase); anonymized survey data and gendered food product profiles in the RTBfoods Dataverse (Supporting Information Table S3)
crops: cassava, yam, sweetpotato, potato, banana (matooke, plantain)
region: Nigeria, Uganda, Cameroon, Benin and Colombia as primary study countries, with spillover to Côte d'Ivoire, Ghana and Kenya
keywords: RTBfoods, consumer preferences, food quality, sensory panel, Crop Ontology, Breedbase, SOPs, data templates, NIRS, gendered food product profile, target product profile, data integration
gist: RTBfoods shows how SOPs, data templates and Crop Ontology food quality traits let consumer, sensory, lab and NIRS data on 12 RTB food products link to genotypes in Breedbase
not_established: that more quality traits in breeding databases led to more adopted varieties; that tricot data were part of this integration (the paper does not mention tricot); the percentage changes in Table 9 (see Notes)
---

## Questions this paper answers

- How can consumer preference and food quality data be linked to breeding data?
- How are sensory and food quality traits named in the Crop Ontology?
- What did the RTBfoods project put into Breedbase, and what went to an open repository?
- How should sensory panel data be checked before upload?
- How were gendered food product profiles developed?
- What lessons does RTBfoods offer for multi-country data standardization?

## Summary

Breeders increasingly target varieties with the food qualities that users want, summarized in target product profiles. The five-year RTBfoods project collected preferences of farmers, processors, traders and consumers for 12 root, tuber and banana food products, such as gari, eba, boiled cassava, pounded yam and matooke. Elizabeth Arnaud, Naama Menda, Thierry Tran, Amos Asiimwe and colleagues from Bioversity International, the Boyce Thompson Institute, CIRAD, IITA, CIP, NaCRRI and NRCRI describe how these diverse data were connected to breeding databases.

Data came from a five-step, gender-inclusive methodology. Teams reviewed knowledge, mapped food products, ran participatory processing diagnoses, tested products with up to 300 consumers per product (150 rural, 150 urban, equal numbers of women and men), and compiled gendered food product profiles. Trained sensory panels, texture analysis, biochemical assays and near-infrared spectroscopy then characterized genotypes.

Standardization came first. Teams wrote product-specific SOPs for surveys, processing trials, sensory panels and lab analysis, with lexicons of food attributes, and versioned every SOP. Traits and variables from the lexicons were added to the Crop Ontology following its trait dictionary template, where a variable combines a trait, a method and a scale. Because preferences vary by country and culture, one trait can carry several methods and scales. Data templates use Crop Ontology variable identifiers as column headers, so data map directly to the database.

Lab, sensory and NIRS data were uploaded to the crop-specific Breedbase databases and linked to the plant record, which required changes to the database model for sensory panel trials. Panel data were cleaned first, using rules such as a maximum difference of three between replicate scores and checks against the panel mean, with a recommended minimum of eight panellists. Survey data containing personal information were anonymized and placed in an open Dataverse repository instead.

The authors report that partner breeding programmes measured more quality traits after RTBfoods began in 2018. Lessons include the value of SOPs and templates agreed early, of recording accession, trial and plot identifiers in every file, of synonyms that bridge breeders' and food scientists' vocabularies, and of collecting gender- and culture-aware data. They propose that Breedbase hold target product profiles with thresholds so clones can be scored against them.

## Methods in brief

- **Project.** RTBfoods (Bill & Melinda Gates Foundation INV-008567), multidisciplinary teams in seven African, one Latin American and two European countries.
- **Preference data.** Five-step methodology (state of knowledge, food mapping, participatory processing diagnosis, consumer testing, gendered food product profile).
- **Quality data.** Trained sensory panels with product lexicons, instrumental texture, biochemical analysis and NIRS, with comparable equipment across partners.
- **Data integration.** Crop Ontology trait dictionaries (template version 5.2, guidelines version 2.1), Breedbase upload templates, NIRS templates with Waves for prediction, anonymized surveys in Dataverse.

## Stated limitations

- Sensory traits, variables and scales differ by product and country, so cross-country comparison needs care.
- Different scales (0-10, 0-100) and method types complicate harmonization.
- Ethical constraints require anonymization before open sharing of survey data.
- Breedbase does not yet integrate target product profiles with thresholds.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 12 | RTB food products studied | This paper |
| 5 years | Duration of RTBfoods | This paper |
| up to 300 (150 + 150) | Consumers per product test, rural + urban, half women | This paper |
| ≥8 | Recommended minimum number of trained sensory panellists | This paper |
| ≤3 | Maximum absolute difference between a panellist's scores on replicates | Guidelines cited in this paper |
| 25 → 34 | Quality traits in IITA cassava breeding data, 1974-2017 vs 2018-2022 (CassavaBase) | This paper, Table 9 |
| 9 → 63 | Quality traits in CIAT cassava breeding data, 1979-2017 vs 2018-2022 | This paper, Table 9 |

## Notes

- Table 9's percentage change column does not match its own counts (for example IITA cassava 25 to 34 is listed as 87.5%). Report trait counts, not the percentages.
- The approach (SOPs, templates, Crop Ontology variables, links to genotype records) is the one the suite's tricot SOPs follow. ClimMob and EBS share Crop Ontology trait IDs in the same way (quiros-2024-compag, dumschott-2023-fps).
- Companion RTBfoods papers on eba and gari connect lab texture with tricot consumer tests (alamu-2023-jsfa, olaosebikan-2023-jsfa). See thiele-2021-ijfst for the RTB review of consumer preferences and varietal change, and moyo-2021-fsufs for tricot consumer testing of sweetpotato.
