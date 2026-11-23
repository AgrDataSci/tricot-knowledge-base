---
id: tanaka-2021-tag
title: From gene banks to farmer's fields. Using genomic selection to identify donors for a breeding program in rice to close the yield gap on smallholder farms
authors: Tanaka R, Lui-King J, Mandaharisoa ST, Rakotondramanana M, Ranaivo HN, Pariasca-Tanaka J, Kajiya Kanegae H, Iwata H, Wissuwa M
year: 2021
journal: Theoretical and Applied Genetics
journal_short: Theor Appl Genet
article: 134, 3397-3410
type: research article
source: external
peer_reviewed: yes
curated_card: no
doi: https://doi.org/10.1007/s00122-021-03909-9
open_copy: https://doi.org/10.1007/s00122-021-03909-9
license: CC BY 4.0
data: genotypes of the IRRI 3K panel on SNP-Seek, https://snp-seek.irri.org/_snp.zul; no phenotype data or code availability statement
crops: rice
region: Madagascar (central highlands)
keywords: genomic selection, genebank accessions, donor selection, 3K rice genomes, on-farm phenotyping, low-input, phosphorus deficiency, GBLUP, expected improvement, prediction accuracy, smallholder farms
gist: Genomic prediction trained on unfertilized farmers' fields in Madagascar picked high-performing rice genebank accessions with accuracy similar to on-station studies, and two became breeding donors
not_established: that farmer-managed or participatory evaluation was used (trials were researcher-run plots on farmers' fields); that the donors have produced released varieties; that expected improvement beats predicted genotypic value (no difference found); that prediction ranks accessions well within the top group (year 3 accuracy among the selected was about 0.1); that grain yield was measured (total panicle dry weight per plant was the proxy); that the results hold outside phosphorus-deficient highland sites
---

## Questions this paper answers

- Can genomic prediction trained on smallholder fields identify promising genebank accessions?
- How accurate is genomic prediction for yield, biomass and heading date under low-input farm conditions?
- How does on-farm prediction accuracy compare with on-station studies?
- Does "expected improvement" select better accessions than predicted genotypic values?
- Is replication or a larger training set the better use of a limited phenotyping budget?

## Summary

Rice yields in sub-Saharan Africa are low because soils are poor, phosphorus is often limiting and farmers apply little fertilizer. In Madagascar, average yields stay below 3 t/ha though achievable on-farm yields exceed 7 t/ha. Breeding on high-input stations may miss the traits needed under these conditions, while genebanks hold traditional varieties that could help. Ryokei Tanaka, James Lui-King, Matthias Wissuwa and colleagues from JIRCAS, the University of Tokyo and FOFIFA tested whether genomic prediction could find useful donors among the 3,024 sequenced accessions of the IRRI genebank without testing them all in the field.

From 2016 to 2019 they ran trials in farmers' fields in the central highlands, with no fertilizer and only rain-fed water, as farmers practise. In year 1, 359 diverse accessions, chosen partly for origins in similar environments, were phenotyped without replication at two sites for heading date, straw weight and panicle weight. A GBLUP model then predicted all 3,024 accessions. In year 2, 234 new accessions were imported: top predicted accessions, a random control group and a set added to widen the training data. They were grown with 289 of the year 1 accessions at two sites, with two replicates. The updated model chose 52 more accessions for panicle weight, which were tested in year 3 against 23 control accessions from earlier years.

Prediction accuracy followed heritability. From year 1 to year 2 it was highest for heading date (about 0.71), intermediate for straw weight (0.25 to 0.63) and lowest for panicle weight, a yield proxy (0.10 to 0.30). The panicle weight values are in the range reported for yield in on-station rice studies at CIAT and IRRI. In year 2, accessions selected by prediction had significantly higher straw and panicle weight than the random control group at both sites. In year 3, selected accessions gave 22% more panicle weight than the controls at Ankazo, but the 14% gain at Anjiro was not significant. Accuracies were as high for newly tested accessions as for those in the training set. Within the top selected group in year 3, however, accuracy was low (about 0.1). Site effects appeared weak, which the authors expected because all sites were phosphorus-deficient, while year effects may have been strong in some cases. Even so, training on a different site picked almost entirely different accessions.

Selecting by expected improvement, a criterion designed to find superior accessions under uncertainty, gave nearly the same list as selecting by predicted genotypic value, probably because the training set was large. Unreplicated year 1 data predicted almost as well as replicated year 2 data. This agrees with an earlier simulation study, cited by the authors, which suggested that adding replicates may help less than a larger training set.

Two accessions, IRIS 313-11949 and IRIS 313-7832, have been adopted as donors in the Malagasy lowland rice breeding programme. The authors conclude that genomic selection can make genebank diversity accessible to breeding for low-input farms, provided genotypic data are public.

## Methods in brief

- **Sites.** Farmers' fields at 950-1,350 m in the Malagasy highlands (Anjiro, Behenjy, Ankazo), rainy season, no fertilizer, no supplementary irrigation.
- **Material.** 359 accessions from the IRRI 3K panel in year 1 (Madagascar, Sri Lanka, Nepal, Bhutan and a representative indica sample, 29 countries). In year 2, 289 of these plus 234 new accessions (79 selected by prediction, 68 random controls, 87 added to widen the training set). In year 3, 52 new selections plus 23 control accessions.
- **Plots.** Two-row micro-plots of 2 m, 22 hills, five plants sampled. Year 1 unreplicated, year 2 two replicates per site in RCBD, year 3 also replicated. Anjiro year 2 data were not used for year 3 selection because a cyclone flooded the field.
- **Traits.** Heading date, plant height, tiller number, straw weight, total panicle dry weight per plant.
- **Model.** GBLUP genomic prediction, ten-fold cross-validation and year-to-year validation, selection by predicted genotypic value and by expected improvement.

## Stated limitations

- Low prediction accuracy for panicle weight, the yield proxy, reflecting low heritability under variable farm conditions.
- The design could not test whether expected improvement helps with small training sets.
- Accessions with origins in similar environments were favoured in year 1, so the training set was not optimized statistically.
- Year 3 confirmed performance with only a small number of accessions.
- Accuracy within the top selected group was low in year 3 (r = 0.13 and 0.11), so prediction ranked the best accessions poorly among themselves.
- Predictions were made separately for each site, and scaling each environment assumed similar heritability across sites, which the authors call unlikely.
- The Anjiro field was flooded after a cyclone in year 2, so those data were excluded from the year 3 selection.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 3,024 | Sequenced IRRI genebank accessions predicted | This paper |
| 359 / 234 / 52 | Accessions tested in year 1 / added in year 2 / added in year 3 | This paper |
| 523 | Accessions grown in year 2 (289 repeated from year 1 plus 234 new) | This paper |
| ~0.71 | Prediction accuracy for heading date, year 1 to year 2 | This paper |
| 0.25-0.63 | Prediction accuracy for straw weight, year 1 training data predicting year 2 | This paper |
| 0.10-0.30 | Prediction accuracy for total panicle weight (yield proxy), year 1 training data predicting year 2 | This paper |
| 0.38 / 0.53 / 0.70 | Mean ten-fold cross-validation accuracy for panicle weight / straw weight / heading date across four year-by-site sets | This paper |
| 22% / 14% | Higher panicle weight of year 3 selected accessions than controls at Ankazo (significant) / Anjiro (not significant) | This paper |
| 0.13 / 0.11 | Year 3 accuracy for panicle weight within the 52 newly selected accessions at Anjiro / Ankazo (0.74 / 0.76 for the 23 controls) | This paper |
| 0.29 / up to 0.31 | Accuracy for yield traits in on-station rice studies at CIAT / IRRI | Grenier et al. 2015; Spindel et al. 2015, cited in this paper |
| 2 | Accessions adopted as donors in the Malagasy breeding programme | This paper |
| 2.3 vs 4.8 t/ha | Average rice yields in Africa vs Asia | FAOSTAT 2018, cited in this paper |

## Notes

- The PDF in this repository lists James Lui-King as joint first author with Ryokei Tanaka and names MBBISP among the funders. Its acknowledgements still thank James DM King for conceiving the study, and the PDF does not explain the relation. Outside this PDF (not checked here): the card review reports a 2024 correction notice that added James Lui-King as an author. Cite the current author list.
- Researcher-run plots on farmers' fields, not farmer evaluation. It is the external counterpart to the team's genebank-to-farm line, where farmer rankings feed genomic prediction (desousa-2021-commsbio, gesesse-2023-pnas). Both find that phenotyping in the target environment pays off.
- See vanetten-2023-pnas for the argument that data-driven methods let genebanks serve heterogeneous environments.
- Source problem: the subpopulation breakdown of the 359 year 1 accessions (p. 3399) sums to 349, so one count is wrong.
- Source problem: the abstract reports accuracies for "grain yield", but the trait measured was total panicle dry weight per plant.
- Source problem: the Discussion says year 2 was "replicated once" (p. 3407), but the Methods describe two replicates per site (p. 3399 to 3400).
- Source problem: the overview says the 234 year 2 accessions were selected ones plus a random control group, but the detail adds 87 accessions to widen the training set (p. 3399 to 3400).
- Data from the cooler Behenjy site generally predicted panicle weight better (p. 3406). The authors suggest testing different accessions at different sites (sparse testing) with multi-environment models, and stress accuracy among the best performers over overall accuracy (p. 3407).
