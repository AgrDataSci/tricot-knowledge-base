---
id: dumschott-2023-fps
title: Ontologies for increasing the FAIRness of plant research data
authors: Dumschott K, Dörpholz H, Laporte MA, Brilhaus D, Schrader A, Usadel B, Neumann S, Arnaud E, Kranz A
year: 2023
journal: Frontiers in Plant Science
journal_short: Front Plant Sci
article: 14, 1279694
type: review
source: team
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.3389/fpls.2023.1279694
open_copy: https://doi.org/10.3389/fpls.2023.1279694
license: CC BY 4.0
data: none
crops: all plants (Crop Ontology covers 37 crop-specific ontologies)
region: global
keywords: ontologies, FAIR data, metadata, Crop Ontology, ISA framework, Planteome, Plant Ontology, Trait Ontology, MIAPPE, PPEO, AgroPortal, DataPLANT, Swate, research data management
gist: Review guiding plant scientists through the ontologies, metadata frameworks (ISA) and lookup services that make plant research data FAIR, including the CGIAR Crop Ontology
not_established: that using ontologies makes datasets FAIR on its own (metadata frameworks and repositories are also needed); a single correct ontology for each term (the authors say there is no one-size-fits-all); anything specific to on-farm or tricot data, which the review does not cover
---

## Questions this paper answers

- What is an ontology and how does it make plant data FAIR?
- Which ontologies are most relevant to plant research, and how do they overlap?
- What is the Crop Ontology and how does it relate to the Plant and Trait Ontologies?
- How do ontologies fit into the ISA (Investigation-Study-Assay) metadata framework and MIAPPE?
- Where can researchers search for ontology terms?
- What tools help annotate spreadsheets with ontology terms?

## Summary

Plant research produces diverse data, from phenotypes and images to genomics and metabolomics, and plants respond strongly to their environment, so data are only reusable when their context is recorded. Kathryn Dumschott and Angela Kranz at Forschungszentrum Jülich, with Marie-Angélique Laporte, Elizabeth Arnaud and colleagues from Bioversity International and German DataPLANT partners, review how ontologies and metadata frameworks can make plant data findable, accessible, interoperable and reusable.

An ontology is a structured set of terms with unique identifiers and defined relations, which makes metadata readable by people and machines and lets datasets from different sources be combined. The authors argue that newcomers struggle because ontologies are scattered and overlap, so they map the landscape.

They describe repositories and lookup services for finding terms, including the OBO Foundry, AgroPortal, Ontobee, BioPortal and the EBI Ontology Lookup Service. They then review general scientific ontologies (such as OBI, EFO, ENVO, units and chemical ontologies) and plant-specific ones. The Planteome reference ontologies include the Plant Ontology, covering anatomy and development stages across green plants, and the Trait Ontology, which resolves different names for the same trait across species. The Plant Phenology Ontology and the Plant Phenotype Experiment Ontology, which implements MIAPPE, organize phenotyping metadata, and DataPLANT has a biology ontology of its own.

The Crop Ontology, developed by CGIAR centres, provides crop-specific trait ontologies, because traits, methods and scales differ between crops. Its terms are cross-referenced to the Plant and Trait Ontologies so users can search for a trait across species. At the time of writing it held 37 crop-specific ontologies, from wheat and maize to banana and several legumes.

Ontologies work best inside a metadata framework. In the ISA model, an Investigation holds Studies (design, growth conditions, samples) and Assays (measurements and data files), and ontology annotations are preferred over free text for required fields. Tools such as DataPLANT's Swate and ISA's OntoMaton help users annotate spreadsheets.

The authors close by stressing community engagement, since ontologies grow through open, Git-based collaboration and new term requests, and by noting that making data FAIR remains costly and time consuming. They see national infrastructures such as NFDI and ELIXIR as routes to integrated, semantically searchable repositories.

## Methods in brief

- **Design.** Narrative review of ontologies, repositories and metadata frameworks relevant to fundamental plant research.
- **Scope.** General scientific ontologies, plant-specific ontologies (Planteome, Crop Ontology, PPO, PPEO, DPBO), ontology lookup services and the ISA framework, illustrated with figures mapping ontologies to ISA entities.

## Stated limitations

- No one-size-fits-all choice of ontology or term; overlapping ontologies (for example OBI and EFO for instruments) leave choices to the user.
- Making data FAIR remains costly and time consuming, which slows adoption.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 37 | Crop-specific ontologies in the Crop Ontology at the time of writing | This paper |
| 26 | Consortia in the German National Research Data Infrastructure (NFDI) | This paper |
| 3 | ISA entities (Investigation, Study, Assay) | Sansone et al. 2012, cited in this paper |

## Notes

- Background for the suite's ontology work. The tricot SOPs map each question to a Crop Ontology variable (trait, method, scale), which Marie-Angélique Laporte leads (quiros-2024-compag, arnaud-2023-jsfa).
- Written for fundamental plant research. It does not discuss on-farm trials, farmer rankings or ClimMob. Do not cite it for those.
- See occelli-2024-natplants, which recommends linking trait preference studies to Crop Ontology terms, and carroll-2020-dsj on the CARE principles that complement FAIR.
