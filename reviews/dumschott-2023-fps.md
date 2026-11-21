# Card review: dumschott-2023-fps

- **Card:** papers/dumschott-2023-fps.md
- **Source:** papers-pdf/dumschott-et-al-2023.pdf (15 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

Page numbers below are the numbers printed on the PDF pages. They match the PDF page numbers for this file (printed page 01 is PDF page 1).

## Overview

| Check | Result |
|---|---|
| Claims checked | 44 |
| Supported | 34 |
| Imprecise | 8 |
| Not in source | 2 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 3 |
| Important omissions | 3 |
| Metadata issues | 3 |

The card is accurate on the main content of this review: the ontology definition, the lookup services, the Planteome ontologies, the Crop Ontology (37 crop ontologies) and the ISA framework. Nothing is contradicted. The most important fix is the gist, which lists topics instead of saying what the review shows, and which says ontologies "make plant research data FAIR" although the card's own not_established says they do not do this alone. Other fixes: a Notes claim about Marie-Angélique Laporte that no source supports, a few imprecise summary sentences (ISA nesting, ELIXIR called national, PPO described as phenotyping metadata), a summary that is 40 words short of the template minimum, and 14 keywords instead of 8 to 12.

## Fixes needed

1. **Gist lists topics and overstates.** The card says: "Review guiding plant scientists through the ontologies, metadata frameworks (ISA) and lookup services that make plant research data FAIR, including the CGIAR Crop Ontology". This lists what the review covers. It also says these resources "make" data FAIR, while the source says ontologies increase FAIRness and that frameworks "further" increase it (p. 2, p. 12), and that there is no one-size-fits-all approach (p. 12). Replace with (29 words):

   `gist: Ontology terms used within metadata frameworks such as ISA make plant data more FAIR, but overlapping ontologies leave no single right term, so portals like Planteome and AgroPortal help`

2. **Notes credit Marie-Angélique Laporte with leading something that no source supports.** The card says: "The tricot SOPs map each question to a Crop Ontology variable (trait, method, scale), which Marie-Angélique Laporte leads (quiros-2024-compag, arnaud-2023-jsfa)." The source says only that Laporte and Arnaud were in the Digital Solutions Team of Bioversity International in Montpellier (p. 1). Neither cited card says Laporte leads the Crop Ontology or the SOP mapping. The antecedent of "which" is also unclear. Replace the first Notes bullet with:

   `- Background for the suite's ontology work. The tricot SOPs map each question to a Crop Ontology variable (trait, method, scale) (quiros-2024-compag, arnaud-2023-jsfa). This is outside the source. Two co-authors, Marie-Angélique Laporte and Elizabeth Arnaud, were at Bioversity International in Montpellier when the review was written.`

3. **Summary is 360 words, below the 400 to 500 target, and misses three useful points.** Missing: the CGIAR Agronomy Ontology (AGRO) in Table 1 (p. 6), the authors' advice that Planteome and AgroPortal are good starting points (p. 12), and the authors' own statement that the review covers only a small subset of ontologies and cannot be a comprehensive guide (p. 8, p. 13). The replacement summary under fix 8 adds these and fixes items 4 to 7. It is 460 words.

4. **ISA nesting is wrong.** The card says: "an Investigation holds Studies (design, growth conditions, samples) and Assays (measurements and data files)". The source says one investigation holds multiple studies, and one study holds multiple assays (Figure 3 caption, p. 11, and p. 10). Replace with:

   `In the ISA model, an Investigation holds one or more Studies (design, growth conditions, samples), and each Study holds one or more Assays (measurements and data files).`

5. **ELIXIR is called national, and the hedge is lost.** The card says: "They see national infrastructures such as NFDI and ELIXIR as routes to integrated, semantically searchable repositories." NFDI is German and ELIXIR is European. The source calls integrated repositories with semantic search "one potential outcome" (p. 12). Replace with:

   `They see infrastructures such as the German NFDI and the European ELIXIR as possible routes to integrated, semantically searchable repositories.`

6. **The Plant Phenology Ontology is not about phenotyping metadata.** The card says PPO and PPEO "organize phenotyping metadata". The source says PPO standardizes phenology terms so data from different repositories can be combined (p. 9). Only PPEO organizes phenotyping experiment metadata, by implementing MIAPPE (p. 9 to 10). Replace with:

   `The Plant Phenology Ontology standardizes phenology terms across repositories, and the Plant Phenotype Experiment Ontology implements MIAPPE, the minimum information standard for phenotyping experiments.`

7. **Author affiliations go beyond the source.** The card says "colleagues from Bioversity International and German DataPLANT partners". The source lists Bioversity International plus Jülich, Düsseldorf, Cologne, Halle and iDiv (p. 1). It acknowledges DataPLANT and NFDI4Chem funding (p. 13) but does not call the co-authors DataPLANT partners. Also "data are only reusable when their context is recorded" is stronger than the source, which says recording metadata is "especially important" for plants because the environment strongly affects them (p. 2). Replace the first paragraph with the first paragraph under fix 8.

8. **Full replacement Summary** (460 words, fixes 3 to 7):

   ```
   Plant research produces diverse data, from phenotypes and images to genomics and metabolomics, and the environment strongly shapes results in plants, so recording the context of an experiment is especially important. Kathryn Dumschott and Angela Kranz at Forschungszentrum Jülich, with Marie-Angélique Laporte and Elizabeth Arnaud of Bioversity International and colleagues from German universities and research institutes, review how ontologies and metadata frameworks can make plant data findable, accessible, interoperable and reusable.

   An ontology is a structured set of terms with unique identifiers and defined relations, which makes metadata readable by people and machines and lets datasets from different sources be combined. The authors argue that newcomers struggle because ontologies are scattered and overlap, so they map the landscape.

   They describe repositories and lookup services for finding terms, including the OBO Foundry, AgroPortal, Ontobee, BioPortal and the EBI Ontology Lookup Service. AgroPortal, founded by the Montpellier scientific community, is designed for agronomy, and the authors name it and Planteome as good starting points for plant data. They then review general scientific ontologies (such as OBI, EFO, ENVO, units and chemical ontologies) and plant-specific ones. The Planteome reference ontologies include the Plant Ontology, covering anatomy and development stages across green plants, the Trait Ontology, which resolves different names for the same trait across species, and the Plant Experimental Conditions Ontology for study types, growth conditions and treatments. The Plant Phenology Ontology standardizes phenology terms across repositories, and the Plant Phenotype Experiment Ontology implements MIAPPE, the minimum information standard for phenotyping experiments. DataPLANT has a biology ontology of its own. The review's table also lists the CGIAR Agronomy Ontology (AGRO) for agronomic practices and variables, without discussing it in the text.

   The Crop Ontology, developed by CGIAR centres, provides crop-specific trait ontologies, because traits, methods and scales differ between crops. Its terms are cross-referenced to the Plant and Trait Ontologies so users can search for a trait across species. At the time of writing it held 37 crop-specific ontologies, from wheat and maize to banana and several legumes.

   Ontologies work best inside a metadata framework. In the ISA model, an Investigation holds one or more Studies (design, growth conditions, samples), and each Study holds one or more Assays (measurements and data files). Ontology annotations are preferred over free text for required fields. Tools such as DataPLANT's Swate and ISA's OntoMaton help users annotate spreadsheets.

   The authors close by stressing community engagement, since ontologies grow through open, Git-based collaboration and new term requests, and by noting that making data FAIR remains costly and time consuming. They see infrastructures such as the German NFDI and the European ELIXIR as possible routes to integrated, semantically searchable repositories. They present the review as a starting guide that covers only a subset of ontologies, not a complete one.
   ```

9. **Key numbers: ISA row has the wrong primary source.** The card credits the three ISA entities to Sansone et al. 2012. Section 5, where the three entities are described, cites González-Beltrán et al. 2014 and Sansone et al. 2016, and the Figure 3 caption cites Sansone et al. 2016 (p. 10 to 11). Sansone et al. 2012 is cited only in the Introduction (p. 2). Replace the row with:

   `| 3 | Core entities of the ISA metadata model (Investigation, Study, Assay), with Assays nested in Studies and Studies nested in an Investigation | ISA specification (Sansone et al. 2016), cited in this paper |`

10. **Stated limitations: add the authors' scope limit.** Add this bullet:

    `- The review covers only a small subset of the ontologies available to plant scientists (for example, no food or nutrition ontologies), and the authors say a comprehensive guide is impossible.`

11. **Keywords: 14, above the 8 to 12 target.** Drop PPEO (covered by MIAPPE) and Swate (covered by DataPLANT):

    `keywords: ontologies, FAIR data, metadata, Crop Ontology, ISA framework, Planteome, Plant Ontology, Trait Ontology, MIAPPE, AgroPortal, DataPLANT, research data management`

12. **not_established can be stronger.** Readers may stretch a review into an evaluation, and the 37 count will date. Replace with:

    `not_established: that using ontologies makes datasets FAIR on its own (metadata frameworks and repositories are also needed); a single correct ontology for each term (the authors say there is no one-size-fits-all); that the ontologies, portals or tools were tested or compared for quality (the review describes them, it does not evaluate them); that the Crop Ontology still holds exactly 37 crop ontologies (the count is from 2023); anything specific to on-farm or tricot data, which the review does not cover`

13. **License (minor).** The PDF states "Creative Commons Attribution License (CC BY)" with no version (p. 1). The template says to use the license as stated in the PDF. Replace with `license: CC BY` (or keep CC BY 4.0 only if the curator confirms the version on the publisher page).

14. **Key numbers: NFDI row (optional).** The 26 consortia figure is background, stated in a sentence that cites Sasse et al. 2022, next to a sentence citing Hartl et al. 2021 (p. 2). Suggested row:

    `| 26 | Consortia in the German National Research Data Infrastructure (NFDI) in 2023 | This paper (background, in a passage citing Hartl et al. 2021 and Sasse et al. 2022) |`

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Ontologies for increasing the FAIRness of plant research data | Same (p. 1) | Supported. The automated flag only lists the title, no mismatch. |
| authors | Dumschott K, Dörpholz H, Laporte MA, Brilhaus D, Schrader A, Usadel B, Neumann S, Arnaud E, Kranz A | Same nine authors in the same order (p. 1) | Supported |
| year | 2023 | Published 30 November 2023 (p. 1) | Supported |
| journal | Frontiers in Plant Science | Same (p. 1) | Supported |
| article | 14, 1279694 | Front. Plant Sci. 14:1279694 (p. 1) | Supported |
| type | review | "TYPE Review" (p. 1) | Supported |
| doi | https://doi.org/10.3389/fpls.2023.1279694 | 10.3389/fpls.2023.1279694 (p. 1) | Supported |
| license | CC BY 4.0 | "Creative Commons Attribution License (CC BY)", no version (p. 1) | Imprecise (version not in PDF) |
| data | none | No dataset. Supplementary Table S1 gives an extended ontology list (p. 5, p. 13) | Supported |
| crops | all plants (Crop Ontology covers 37 crop-specific ontologies) | Fundamental plant sciences, 37 species-specific ontologies in CO (p. 2, p. 10) | Supported |
| region | global | No geographic focus, infrastructures discussed are German and European (p. 2, p. 12) | Supported |
| gist | Review guiding plant scientists ... that make plant research data FAIR ... | Ontologies increase FAIRness, frameworks further increase it, no one-size-fits-all (p. 2, p. 12) | Imprecise (lists topics, overstates) |
| not_established | three items | All three are consistent with the source (p. 2, p. 12, whole text) | Supported, but can be stronger (fix 12) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Plant research produces diverse data, phenotypes to omics | Supported | Phenotyping, imaging, genomics, transcriptomics, proteomics, metabolomics (p. 2) | |
| 2 | Summary | Plants respond strongly to environment, so data are only reusable when context is recorded | Imprecise | Metadata recording "especially important" because environment strongly affects sessile organisms (p. 2) | "only reusable" is stronger than the source |
| 3 | Summary | Dumschott and Kranz at Jülich, with Laporte, Arnaud, Bioversity and German DataPLANT partners | Imprecise | Affiliations (p. 1), DataPLANT and NFDI4Chem funding (p. 13) | "DataPLANT partners" not stated in source |
| 4 | Summary | Ontology = structured terms with unique IDs and relations, human and machine readable, allows combining data | Supported | p. 2 to 3 | |
| 5 | Summary | Newcomers struggle because resources are scattered and overlap, so authors map the landscape | Supported | "daunting and confusing to newcomers" (p. 2), overlap (p. 12) | |
| 6 | Summary | Repositories: OBO Foundry, AgroPortal, Ontobee, BioPortal, EBI OLS | Supported | Section 3 (p. 4) | TIB Terminology Service and Planteome also listed |
| 7 | Summary | General ontologies such as OBI, EFO, ENVO, units, chemical | Supported | Section 4.1 and Table 1 (p. 5 to 8) | |
| 8 | Summary | Plant Ontology covers anatomy and development stages across green plants | Supported | Broadened to all Viridiplantae, two branches (p. 8 to 9) | |
| 9 | Summary | Trait Ontology resolves different names for same trait across species | Supported | leaf versus frond example, TO addresses trait description discrepancies (p. 9) | |
| 10 | Summary | PPO and PPEO organize phenotyping metadata, PPEO implements MIAPPE | Imprecise | PPO is for phenology data interoperability (p. 9), PPEO implements MIAPPE (p. 9 to 10) | PPO is not about phenotyping metadata |
| 11 | Summary | DataPLANT has its own biology ontology | Supported | DPBO (p. 10) | |
| 12 | Summary | Crop Ontology developed by CGIAR centres, traits, methods and scales differ by crop | Supported | "several members of the CGIAR" (p. 9) | |
| 13 | Summary | CO terms cross-referenced to PO and TO, search traits across species | Supported | p. 10, also Planteome mapping (p. 4) | |
| 14 | Summary | 37 crop-specific ontologies, wheat, maize, banana, legumes | Supported | "37 species-specific ontologies" with these examples (p. 10) | |
| 15 | Summary | Ontologies work best inside a metadata framework | Supported | Frameworks with ontologies "further" increase FAIRness (p. 2, p. 12) | Fair paraphrase |
| 16 | Summary | Investigation holds Studies and Assays | Imprecise | Assays nest in Studies (Figure 3 caption, p. 11) | |
| 17 | Summary | Ontology annotations preferred over free text for required fields | Supported | p. 10 | Figure 3 caption says required for some fields (see Source issues) |
| 18 | Summary | Swate and OntoMaton help annotate spreadsheets | Supported | p. 12 | |
| 19 | Summary | Community engagement, Git-based collaboration, new term requests | Supported | p. 3, p. 10, p. 12 | |
| 20 | Summary | Making data FAIR remains costly and time consuming | Supported | p. 12 | |
| 21 | Summary | National infrastructures such as NFDI and ELIXIR as routes to integrated, searchable repositories | Imprecise | ELIXIR is European, outcome called "potential" (p. 12) | |
| 22 | Methods | Narrative review for fundamental plant research | Supported | "TYPE Review", aim (p. 1 to 2) | |
| 23 | Methods | Scope: general and plant ontologies, lookup services, ISA, figures mapping ontologies to ISA | Supported | Sections 3 to 5, Figure 4 (p. 4 to 11) | Table 1 and Supplementary Table S1 not mentioned |
| 24 | Limitations | No one-size-fits-all, OBI and EFO overlap on instruments | Supported | p. 7, p. 12 | |
| 25 | Limitations | FAIR costly and time consuming, slows adoption | Supported | "hindering progress" (p. 12) | |
| 26 | Key numbers | 37 crop ontologies, This paper | Supported | p. 10 | |
| 27 | Key numbers | 26 NFDI consortia, This paper | Supported | p. 2 | Background fact in a cited passage (optional fix 14) |
| 28 | Key numbers | 3 ISA entities, Sansone et al. 2012 | Imprecise | Section 5 cites González-Beltrán 2014 and Sansone 2016, Figure 3 cites Sansone 2016 (p. 10 to 11) | Wrong primary source |
| 29 | Notes | tricot SOPs map each question to a Crop Ontology variable | Not in source | Not in this review | Acceptable in Notes as outside knowledge with card references, but say it is outside the source |
| 30 | Notes | "which Marie-Angélique Laporte leads" | Not in source | p. 1 gives only her affiliation. Not in quiros-2024-compag or arnaud-2023-jsfa cards either | Remove (fix 2) |
| 31 | Notes | Written for fundamental plant research, no on-farm trials, farmer rankings or ClimMob | Supported | Aim (p. 2), conclusion (p. 13). No mention of farms, farmers, rankings or ClimMob in the text | |

The 13 frontmatter rows in the Metadata check bring the total to 44 claims.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Figure 1 caption labels do not match the figure. In the image, panel B is the metadata sheet and panel C is the Plant Ontology excerpt with imported terms. The caption describes them the other way round, and the text cites 1B and 1C inconsistently. | p. 3 | No | Not needed. The card does not use Figure 1. |
| PPEO is named "Plant Phenotype Experiment Ontology" in Table 1 and the 4.2.4 heading, but "Plant Phenotyping Experiment Ontology" in the text. | p. 6, p. 9 | No | Optional: `- The source names PPEO two ways ("Plant Phenotype Experiment Ontology" and "Plant Phenotyping Experiment Ontology"). This card uses the first.` |
| The text says ontology annotations are "preferred" over free text in ISA, while the Figure 3 caption says an ontology annotation is "the required input" for fields such as design type and measurement type. | p. 10, p. 11 | No | Optional: `- The text says ISA prefers ontology annotations over free text, but the Figure 3 caption says they are required for some fields, such as study design type and assay measurement type.` |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: overview of ontologies for fundamental plant sciences, their use within ISA, and where to find terms | Yes | high | |
| Design: narrative review, no systematic search | Yes (Methods) | medium | |
| Sample size | Not applicable (review) | | |
| Crop Ontology: CGIAR origin, crop-specific traits, cross-references to PO and TO, 37 ontologies | Yes | high | |
| Authors' advice that Planteome and AgroPortal are good starting points, both designed for plant and agronomy research (p. 12) | No | medium | In the replacement summary (fix 8) |
| CGIAR Agronomy Ontology (AGRO) for agronomic practices and variables, listed in Table 1 (p. 6) | No | medium | In the replacement summary (fix 8). Relevant to tricot users, who record agronomic context. |
| Authors' limitation: only a small subset of ontologies covered, a comprehensive guide is impossible (p. 8, p. 13) | No | medium | Fix 10 and the last sentence of fix 8 |
| PECO for study types, growth conditions and treatments (p. 9) | No | low | In the replacement summary (fix 8) |
| MIAPPE as the minimum information standard, organized by ISA sections (p. 9, p. 12) | Partly (named only) | low | In the replacement summary (fix 8) |
| ISA spreadsheets convert to ISA-Tab and ISA-JSON (p. 10) | No | low | Optional |
| Supplementary Table S1, extended ontology list (p. 5) | No | low | Optional, in data: `data: none (Supplementary Table S1 gives an extended list of ontologies)` |
| FAIRagro, PLANTdataHUB and the ARC registry as plant data infrastructures (p. 13) | No | low | Optional |
| Conclusion: annotation with ontology terms is every researcher's responsibility (p. 13) | No | low | Optional |
| Anything on on-farm, participatory or tricot data | Correctly flagged as absent in Notes and not_established | high | |

## Template compliance

- Summary word count: 360 words. Below the 400 to 500 target. The replacement in fix 8 is 460 words.
- Gist length: 24 words, under 30. But it lists topics (fix 1). The replacement is 29 words.
- Keywords: 14. Above the 8 to 12 target (fix 11).
- Questions: 6. Within 4 to 7. All six are answered by the source.
- House style: tricot is lowercase throughout. maniva does not appear.
- Long-format sections (Questions, Methods in brief, Stated limitations) are present, so the card is long format.
