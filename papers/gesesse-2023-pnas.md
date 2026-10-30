---
id: gesesse-2023-pnas
title: Genomics-driven breeding for local adaptation of durum wheat is enhanced by farmers' traditional knowledge
authors: Gesesse CA, Nigir B, de Sousa K, Gianfranceschi L, Gallo GR, Poland J, Kidane YG, Desta EA, Fadda C, Pè ME, Dell'Acqua M
year: 2023
journal: Proceedings of the National Academy of Sciences
journal_short: PNAS
article: 120(14), e2205774119
type: research article
doi: https://doi.org/10.1073/pnas.2205774119
open_copy: https://doi.org/10.1073/pnas.2205774119
license: CC BY 4.0
data: raw data on Dryad (https://doi.org/10.5061/dryad.w6m905qrv); scripts at https://github.com/mdellh2o/EtNAM.GS
software: Plackett-Luce model (R package PlackettLuce, https://CRAN.R-project.org/package=PlackettLuce, check the current CRAN version)
crops: durum wheat
region: Ethiopia (Adet, Geregera, Kulumsa; diversity panel also at Hagreselam)
keywords: genomic selection, EtNAM, nested association mapping, farmer appreciation, participatory variety selection, heritability, QTL, GWAS, durum wheat, traditional knowledge, Plackett-Luce, local adaptation
gist: Farmer appreciation of 1,200 EtNAM wheat lines is heritable and, used in genomic selection, predicts grain yield in new environments better than models trained on yield itself
relations:
  - usesDataFrom: mancini-2017-scirep  # diversity panel and farmer scores
  - agreesWith: desousa-2021-commsbio  # farmer appreciation improves prediction accuracy
---

## Questions this paper answers

- Is farmer preference a heritable trait that breeders can select on?
- Can farmer scores improve genomic selection for yield?
- Do women and men farmers choose the same lines?
- Which genomic loci are linked to farmer appreciation?
- How does participatory evaluation fit into genomics-driven breeding?

## Summary

Smallholder farmers in sub-Saharan Africa select varieties using traditional knowledge, and only about 40% of intended beneficiaries adopt new varieties from breeding. The study tests whether farmers' evaluations can be built into genomics-driven breeding, using Ethiopian durum wheat.

The team used two sets of material. A diversity panel of 400 mostly traditional varieties had been phenotyped and scored by farmers earlier (mancini-2017-scirep). Landraces from that panel were crossed with an elite line of international pedigree to create the Ethiopian nested association mapping population (EtNAM). Here, 1,200 recombinant inbred lines from 12 EtNAM families were grown in a replicated design at three Ethiopian sites (Adet, Geregera and Kulumsa), covering 10,400 plots. Separate groups of women and men farmers gave each line an overall appreciation score from one to five near flowering, and agronomic traits were measured. Both sets were genotyped.

Farmer appreciation behaved like a quantitative trait. Its broad-sense heritability (0.45) was close to that of grain yield (0.49), with higher heritability for men's scores (0.54) than women's (0.32). Women and men chose overlapping top lines, with 26 of the top 5% chosen by both. Appreciation correlated with grain yield in every location and farmer group (0.41 to 0.66), and in Geregera, the most limiting site, it also tracked yield stability across environments. Plackett-Luce models showed that drivers of choice differed by site and gender. Early maturity dominated in Geregera, while yield and biomass mattered more in Kulumsa. Some EtNAM families outperformed the reference modern variety everywhere.

The key result concerns genomic selection. A model trained on yield in the diversity panel could not predict yield in the EtNAM, but a model trained on farmer appreciation in the panel predicted EtNAM yield with an accuracy of 0.09, and predicted EtNAM appreciation with accuracies above 0.20 for combined data. In the reverse direction, appreciation measured on the EtNAM predicted panel yield at 0.11 and panel appreciation at 0.41, against 0.02 for a yield-trained model. The authors suggest farmers integrate heritable yield components and experience over many seasons. Association mapping found loci for appreciation on several chromosomes, some shared with yield and grain weight and one on 6B linked to no measured trait, and family-specific maps identified 382 partially overlapping QTL.

The authors propose combining on-station participatory evaluation with genomic selection at early breeding stages, then moving selected lines to decentralized on-farm testing through 3D-breeding (desousa-2021-commsbio). They stress that farmer scores cannot be the only selection driver and that on-station fields do not reflect farmers' input levels.

## Methods in brief

- **Material.** 1,200 EtNAM RILs from 12 families plus a 400-entry diversity panel, both genotyped.
- **Trials.** Three locations in Ethiopia, fully replicated, 10,400 plots.
- **Farmer scoring.** Overall appreciation on a 1 to 5 Likert scale by separate women and men groups.
- **Analysis.** BLUPs, heritability, Plackett-Luce models of farmer choice, genomic selection across panels and locations, GWAS and family-specific QTL mapping.

## Stated limitations

- The scoring design cannot capture subtle gender dynamics in communities.
- On-station trials use more fertilizer and weeding than farmers' fields, which may push scores toward yield potential.
- Centralized participatory evaluation has a high cost per data point and limited environmental coverage.
- Mapping resolution is too low to identify candidate genes.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 1,200 RILs, 12 families | EtNAM lines evaluated | This paper |
| 10,400 plots | Plots evaluated by farmers across three locations | This paper |
| ~40% | Adoption of new varieties by smallholder beneficiaries | Cited in this paper |
| H² 0.45 / 0.49 | Heritability of farmer appreciation / grain yield | This paper |
| H² 0.54 / 0.32 | Heritability of men's / women's appreciation | This paper |
| 26 | Lines in the top 5% chosen by both women and men | This paper |
| 0.41 to 0.66 | Correlation of appreciation with grain yield across sites and groups | This paper |
| 0.09 | Accuracy predicting EtNAM yield from panel appreciation (yield-trained model failed) | This paper |
| 0.11 / 0.41 / 0.02 | EtNAM appreciation predicting panel yield / panel appreciation; EtNAM yield predicting panel yield | This paper |
| 382 | Partially overlapping QTL from family-specific maps | This paper |

## Notes

- Not a tricot trial. On-station participatory evaluation that continues mancini-2017-scirep and points to on-farm testing via desousa-2021-commsbio.
- Kauê de Sousa is a co-author and contributed analytic tools.
