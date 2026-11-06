---
id: occelli-2024-natplants
title: A scoping review on tools and methods for trait prioritization in crop breeding programmes
authors: Occelli M, Mukerjee R, Miller C, Porciello J, Puerto S, Garner E, Guerra M, Gomez MI, Tufan HA
year: 2024
journal: Nature Plants
journal_short: Nat Plants
article: 10, 402-411
type: review
source: external
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1038/s41477-024-01639-6
open_copy: https://doi.org/10.1038/s41477-024-01639-6
license: CC BY 4.0
data: extracted data and code on GitHub, https://github.com/TufanLab/trait-priority-scoping-review; protocol on OSF, https://osf.io/ayw8q
crops: cereals, legumes, roots, tubers and bananas, vegetables and fruits
region: global (57% of studies in sub-Saharan Africa)
keywords: trait prioritization, trait preferences, scoping review, PRISMA-ScR, sex-disaggregated data, sampling, trait taxonomy, Crop Ontology, participatory plant breeding, research networks, demand-led breeding
gist: Scoping review of 40 years of trait prioritization studies finds weak designs, ad hoc sampling, little sex-disaggregation and no shared trait taxonomy, so findings cannot be compared or pooled
not_established: that any single elicitation tool, including tricot, gives the most valid trait priorities (the review maps use, not validity); that direct questions give wrong results (cited, not tested here); that roughly 250 respondents is an adequate sample; rankings of specific traits for a given crop and country
---

## Questions this paper answers

- How have crop breeding programmes collected and analysed farmers' trait preferences since 1980?
- Which tools are used most to elicit trait priorities, and how often are on-farm trials or tricot used?
- How often do trait preference studies disaggregate by sex, age or region?
- Why can't findings from different trait preference studies be pooled?
- What should a robust trait prioritization study include?
- Who funds and authors this literature, and is it siloed?

## Summary

Public breeding programmes are trying to become demand-led, which starts with knowing which traits growers, processors and consumers want and turning that into target product profiles. Martina Occelli, Hale Ann Tufan and colleagues at Cornell University asked what tools and methods have underpinned trait prioritization studies, a question that had not been examined across crops and regions.

They ran a systematic scoping review following PRISMA-ScR, registered on OSF, searching five scholarly databases and 12 grey literature sources with no date limit, English only. From 17,786 records, 657 studies entered data extraction with a 40-question framework. The results describe 564 original studies, 83% peer-reviewed, more than half published since 2016.

Coverage is uneven. Ethiopia and India have the most studies, 57% are in sub-Saharan Africa, only 6% in South America and 2% in the Middle East and North Africa. Cereals dominate, while roots, tubers, bananas, fruits and vegetables, which matter for nutrition, get less attention.

Most studies (58%) ask farmers directly through individual surveys or focus groups. Direct experience, such as PVS, demonstration plots and on-farm trials including tricot, comes second (24%). Analysis is mostly frequency counts and hypothesis tests. Only 5% analyse qualitative data, even though focus groups are among the most used tools. A third of studies use a single tool.

Designs are weak. 12% do not report how many people took part, 52% engage "farmers" without saying whether they are producers or consumers, and fewer than 19% include consumers, traders or other seed system actors. Studies cluster around 250 respondents regardless of crop, country or method, which the authors read as habit rather than power calculation. Of studies calling themselves participatory, 90% are formal-led and only 12.5% had farmers test varieties in their own fields with their own management.

Only 37% of studies collect sex-disaggregated data, and 1.7% intrahousehold data. Where they do, 84% find differences between women and men, often explained with stereotyped roles. Only 0.9% disaggregate by age. Trait names vary so much that even three Indian rice studies with shared authors produced incompatible lists. Co-authorship forms about ten isolated clusters, and five donors fund nearly half the studies.

The authors recommend more work on nutritious crops and neglected regions, linking trait studies to breeding databases and Crop Ontology terms, sex-disaggregating at collection and analysis, and rigorous designs with representative sampling and power calculations. They note that on-farm testing and video-based concept testing may avoid some biases of direct questions.

## Methods in brief

- **Design.** Systematic scoping review under PRISMA-ScR. Protocol registered 11 March 2022, finalized 8 July 2022, search rerun 23 June 2023 after peer review.
- **Sources.** Scopus, Web of Science, CAB Direct, AgEcon Search, BIOSIS, plus 12 grey literature sources (FAO, World Bank, IFAD, J-PAL/ATAI, GARDIAN and others).
- **Screening.** 17,786 records, 11,978 after deduplication, 1,325 full texts assessed, 657 included, in Covidence with peer screening.
- **Extraction.** 40-question framework covering crop, tools, analysis, sampling, disaggregation, donors and degree of farmer engagement, classified as formal-led or farmer-led and consultative or collaborative.
- **Synthesis.** Descriptive analysis in R 4.2.3, author and donor networks in VOSviewer, four crop groups (commodity and ornamental crops, 3% of studies, excluded).

## Stated limitations

- English-language studies only, which may explain part of the South American gap.
- Studies with several tools or methods were counted in several categories, which may double count.
- Sample size calculations may have been done but not reported.
- Whether donor and policy priorities drive the regional bias needs further analysis.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 17,786 / 11,978 / 1,325 / 657 | Records found, after deduplication, full texts assessed, studies included | This paper |
| 564 | Original studies described in the results (83% peer-reviewed, 17% grey literature) | This paper |
| 57% / 6% / 2% | Studies in sub-Saharan Africa, South America, Middle East and North Africa | This paper |
| 58% / 24% / 7.4% | Studies eliciting traits by direct questions, direct experience, choice tools | This paper |
| 5% | Studies using qualitative data analysis | This paper |
| 12% | Studies not reporting the number of respondents | This paper |
| ~250 | Typical respondent number across crops, countries and methods | This paper |
| 90% / 12.5% | Self-described participatory studies that are formal-led / formal-led collaborative trials on farmers' own fields | This paper |
| 37% / 84% | Studies collecting sex-disaggregated data / of those, studies finding sex-based differences | This paper |
| 1.7% / 0.9% | Studies with intrahousehold data / disaggregating by age | This paper |
| 49.5% | Median share of women respondents in the 216 sex-disaggregated studies | This paper |
| 25% | Share of studies reporting sex-disaggregated trait data in an earlier review | Weltzien et al. 2019 (ref. 14), cited in this paper |
| ~10 / 5 | Co-authorship clusters / donors funding nearly half the studies | This paper |

## Notes

- The abstract and Fig. 6 give 657 included studies, while the results describe 564 original studies. Use 564 for shares of original studies and say so.
- tricot appears only as one tool among 21 under "direct experience". The review does not report how many studies used tricot.
- The recommendation to link trait studies to Crop Ontology matches the team's data standards work (arnaud-2023-jsfa, dumschott-2023-fps, quiros-2024-compag).
- Different paper from occelli-2024-agecon, the same first author's randomized comparison of tricot and group PVS. See occelli-2026-ahv for the same Cornell group's policy review of farmer participation, and voss-2021-outlook and teeken-2021-fsufs on gender and trait preferences.
