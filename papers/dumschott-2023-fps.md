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
license: CC BY
data: none
crops: all plants (Crop Ontology covers 37 crop-specific ontologies)
region: global
keywords: ontologies, FAIR data, metadata, Crop Ontology, ISA framework, Planteome, Plant Ontology, Trait Ontology, MIAPPE, AgroPortal, DataPLANT, research data management
gist: Ontology terms used within metadata frameworks such as ISA make plant data more FAIR, but overlapping ontologies leave no single right term, so portals like Planteome and AgroPortal help
not_established: that using ontologies makes datasets FAIR on its own (metadata frameworks and repositories are also needed); a single correct ontology for each term (the authors say there is no one-size-fits-all); that the ontologies, portals or tools were tested or compared for quality (the review describes them, it does not evaluate them); that the Crop Ontology still holds exactly 37 crop ontologies (the count is from 2023); anything specific to on-farm or tricot data, which the review does not cover
---

## Questions this paper answers

- What is an ontology and how does it make plant data FAIR?
- Which ontologies are most relevant to plant research, and how do they overlap?
- What is the Crop Ontology and how does it relate to the Plant and Trait Ontologies?
- How do ontologies fit into the ISA (Investigation-Study-Assay) metadata framework and MIAPPE?
- Where can researchers search for ontology terms?
- What tools help annotate spreadsheets with ontology terms?

## Summary

Plant research produces diverse data, from phenotypes and images to genomics and metabolomics, and the environment strongly shapes results in plants, so recording the context of an experiment is especially important. Kathryn Dumschott and Angela Kranz at Forschungszentrum Jülich, with Marie-Angélique Laporte and Elizabeth Arnaud of Bioversity International and colleagues from German universities and research institutes, review how ontologies and metadata frameworks can make plant data findable, accessible, interoperable and reusable.

An ontology is a structured set of terms with unique identifiers and defined relations, which makes metadata readable by people and machines and lets datasets from different sources be combined. The authors argue that newcomers struggle because ontologies are scattered and overlap, so they map the landscape.

They describe repositories and lookup services for finding terms, including the OBO Foundry, AgroPortal, Ontobee, BioPortal and the EBI Ontology Lookup Service. AgroPortal, founded by the Montpellier scientific community, is designed for agronomy, and the authors name it and Planteome as good starting points for plant data. They then review general scientific ontologies (such as OBI, EFO, ENVO, units and chemical ontologies) and plant-specific ones. The Planteome reference ontologies include the Plant Ontology, covering anatomy and development stages across green plants, the Trait Ontology, which resolves different names for the same trait across species, and the Plant Experimental Conditions Ontology for study types, growth conditions and treatments. The Plant Phenology Ontology standardizes phenology terms across repositories, and the Plant Phenotype Experiment Ontology implements MIAPPE, the minimum information standard for phenotyping experiments. DataPLANT has a biology ontology of its own. The review's table also lists the CGIAR Agronomy Ontology (AGRO) for agronomic practices and variables, without discussing it in the text.

The Crop Ontology, developed by CGIAR centres, provides crop-specific trait ontologies, because traits, methods and scales differ between crops. Its terms are cross-referenced to the Plant and Trait Ontologies so users can search for a trait across species. At the time of writing it held 37 crop-specific ontologies, from wheat and maize to banana and several legumes.

Ontologies work best inside a metadata framework. In the ISA model, an Investigation holds one or more Studies (design, growth conditions, samples), and each Study holds one or more Assays (measurements and data files). Ontology annotations are preferred over free text for required fields. Tools such as DataPLANT's Swate and ISA's OntoMaton help users annotate spreadsheets.

The authors close by stressing community engagement, since ontologies grow through open, Git-based collaboration and new term requests, and by noting that making data FAIR remains costly and time consuming. They see infrastructures such as the German NFDI and the European ELIXIR as possible routes to integrated, semantically searchable repositories. They present the review as a starting guide that covers only a subset of ontologies, not a complete one.

## Methods in brief

- **Design.** Narrative review of ontologies, repositories and metadata frameworks relevant to fundamental plant research.
- **Scope.** General scientific ontologies, plant-specific ontologies (Planteome, Crop Ontology, PPO, PPEO, DPBO), ontology lookup services and the ISA framework, illustrated with figures mapping ontologies to ISA entities.

## Stated limitations

- No one-size-fits-all choice of ontology or term. Overlapping ontologies (for example OBI and EFO for instruments) leave choices to the user.
- Making data FAIR remains costly and time consuming, which slows adoption.
- The review covers only a small subset of the ontologies available to plant scientists (for example, no food or nutrition ontologies), and the authors say a comprehensive guide is impossible.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 37 | Crop-specific ontologies in the Crop Ontology at the time of writing | This paper |
| 26 | Consortia in the German National Research Data Infrastructure (NFDI) in 2023 | This paper (background, in a passage citing Hartl et al. 2021 and Sasse et al. 2022) |
| 3 | Core entities of the ISA metadata model (Investigation, Study, Assay), with Assays nested in Studies and Studies nested in an Investigation | ISA specification (Sansone et al. 2016), cited in this paper |

## Notes

- Background for the suite's ontology work, outside this source. The tricot SOPs map each question to a Crop Ontology variable (trait, method, scale). Related cards: quiros-2024-compag (ClimMob links traits to Crop Ontology) and arnaud-2023-jsfa (SOPs and Crop Ontology variables in RTBfoods). Two co-authors, Marie-Angélique Laporte and Elizabeth Arnaud, were at Bioversity International in Montpellier when the review was written.
- Written for fundamental plant research. It does not discuss on-farm trials, farmer rankings or ClimMob. Do not cite it for those.
- See occelli-2024-natplants, which recommends linking trait preference studies to Crop Ontology terms, and carroll-2020-dsj on the CARE principles that complement FAIR.
- Problem in the source: the Figure 1 caption swaps panels B and C. In the image, B is the metadata sheet and C is the Plant Ontology excerpt, and the text cites 1B and 1C inconsistently (p. 3).
- Problem in the source: PPEO is named "Plant Phenotype Experiment Ontology" in Table 1 and the 4.2.4 heading, but "Plant Phenotyping Experiment Ontology" in the text (p. 6, p. 9). This card uses the first.
- Problem in the source: the text says ISA prefers ontology annotations over free text (p. 10), but the Figure 3 caption says they are required for some fields, such as study design type and assay measurement type (p. 11).
