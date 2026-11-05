---
id: tanaka-2021-tag
title: From gene banks to farmer's fields. Using genomic selection to identify donors for a breeding program in rice to close the yield gap on smallholder farms
authors: Tanaka R, Lui-King J, Mandaharisoa ST, Rakotondramanana M, Ranaivo HN, Pariasca-Tanaka J, Kajiya-Kanegae H, Iwata H, Wissuwa M
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
data: genotypes of the IRRI 3K panel on SNP-Seek, https://snp-seek.irri.org; phenotypes not deposited
crops: rice
region: Madagascar (central highlands)
keywords: genomic selection, genebank accessions, donor selection, 3K rice genomes, on-farm phenotyping, low-input, phosphorus deficiency, GBLUP, expected improvement, prediction accuracy, smallholder farms
gist: Genomic prediction trained on unfertilized farmers' fields in Madagascar picked high-performing rice genebank accessions with accuracy similar to on-station studies, and two became breeding donors
not_established: that farmer-managed or participatory evaluation was used (trials were researcher-run plots on farmers' fields); that the donors have produced released varieties; that expected improvement beats predicted genotypic value (no difference found)
---

## Questions this paper answers

- Can genomic prediction trained on smallholder fields identify promising genebank accessions?
- How accurate is genomic prediction for yield, biomass and heading date under low-input farm conditions?
- How does on-farm prediction accuracy compare with on-station studies?
- Does "expected improvement" select better accessions than predicted genotypic values?
- Is replication or a larger training set the better use of a limited phenotyping budget?

## Summary

Rice yields in sub-Saharan Africa are low because soils are poor, phosphorus is often limiting and farmers apply little fertilizer. In Madagascar, average yields stay below 3 t/ha though achievable on-farm yields exceed 7 t/ha. Breeding on high-input stations may miss the traits needed under these conditions, while genebanks hold traditional varieties that could help. Ryokei Tanaka, James Lui-King, Matthias Wissuwa and colleagues from JIRCAS, the University of Tokyo and FOFIFA tested whether genomic prediction could find useful donors among the 3,024 sequenced accessions of the IRRI genebank without testing them all in the field.

From 2016 to 2019 they ran trials in farmers' fields in the central highlands, with no fertilizer and only rain-fed water, as farmers practise. In year 1, 359 diverse accessions, chosen partly for origins in similar environments, were phenotyped at two sites for heading date, straw weight and panicle weight. A GBLUP model then predicted all 3,024 accessions. Top predicted accessions, plus a random control group (234 in total), were imported and grown in year 2 at two sites with one replicate. The model was updated, and 52 more top accessions were tested in year 3.

Prediction accuracy followed heritability. It was highest for heading date (about 0.71), intermediate for straw weight (0.25 to 0.63) and lowest for panicle weight, a yield proxy (0.10 to 0.30). These values match those from on-station rice studies at CIAT and IRRI. Accessions selected by prediction outperformed the random control group at one site, and accuracies were as high for newly tested accessions as for those in the training set. Site effects were small because all sites were phosphorus-deficient, while year effects were sometimes strong.

Selecting by expected improvement, a criterion designed to find superior accessions under uncertainty, gave nearly the same list as selecting by predicted genotypic value, probably because the training set was large. Unreplicated year 1 data predicted almost as well as replicated year 2 data, consistent with simulations showing a larger training set beats more replications.

Two accessions, IRIS 313-11949 and IRIS 313-7832, have been adopted as donors in the Malagasy lowland rice breeding programme. The authors conclude that genomic selection can make genebank diversity accessible to breeding for low-input farms, provided genotypic data are public.

## Methods in brief

- **Sites.** Farmers' fields at 950-1,350 m in the Malagasy highlands (Anjiro, Behenjy, Ankazo), rainy season, no fertilizer, no supplementary irrigation.
- **Material.** 359 accessions from the IRRI 3K panel in year 1 (Madagascar, Sri Lanka, Nepal, Bhutan and a representative indica sample, 29 countries), 234 new accessions in year 2, 52 in year 3.
- **Plots.** Two-row micro-plots of 2 m, 22 hills, five plants sampled. Year 1 unreplicated, year 2 two replicates in RCBD.
- **Traits.** Heading date, plant height, tiller number, straw weight, total panicle dry weight per plant.
- **Model.** GBLUP genomic prediction, ten-fold cross-validation and year-to-year validation, selection by predicted genotypic value and by expected improvement.

## Stated limitations

- Low prediction accuracy for panicle weight, the yield proxy, reflecting low heritability under variable farm conditions.
- The design could not test whether expected improvement helps with small training sets.
- Accessions with origins in similar environments were favoured in year 1, so the training set was not optimized statistically.
- Year 3 confirmed performance with only a small number of accessions.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 3,024 | Sequenced IRRI genebank accessions predicted | This paper |
| 359 / 234 / 52 | Accessions tested in year 1 / added in year 2 / added in year 3 | This paper |
| ~0.71 | Prediction accuracy for heading date, year 1 to year 2 | This paper |
| 0.25-0.63 | Prediction accuracy for straw weight | This paper |
| 0.10-0.30 | Prediction accuracy for total panicle weight (yield proxy) | This paper |
| 0.29 / up to 0.31 | Accuracy for yield traits in on-station rice studies at CIAT / IRRI | Grenier et al. 2015; Spindel et al. 2015, cited in this paper |
| 2 | Accessions adopted as donors in the Malagasy breeding programme | This paper |
| 2.3 vs 4.8 t/ha | Average rice yields in Africa vs Asia | FAOSTAT 2018, cited in this paper |

## Notes

- The PDF in this repository is the publisher's current version, which lists James Lui-King as joint first author. An earlier version of the same DOI omitted him and thanked James DM King in the acknowledgements. Cite the current author list.
- Researcher-run plots on farmers' fields, not farmer evaluation. It is the external counterpart to the team's genebank-to-farm line, where farmer rankings feed genomic prediction (desousa-2021-commsbio, gesesse-2023-pnas). Both find that phenotyping in the target environment pays off.
- See vanetten-2023-pnas for the argument that data-driven methods let genebanks serve heterogeneous environments.
