---
id: dorado-2026-tag
title: Estimating on-farm genotypic performance and variability using ranking data
authors: Dorado-Betancourt H, van Eeuwijk F, van Etten J, Ramirez-Villegas J, de Sousa K, Daudi H, Ndegwa M, Mendes T, van Heerwaarden J
year: 2026
journal: Theoretical and Applied Genetics
journal_short: Theor Appl Genet
article: 139, 231
type: research article
doi: https://doi.org/10.1007/s00122-026-05319-1
open_copy: https://doi.org/10.1007/s00122-026-05319-1
license: CC BY 4.0
data: groundnut and sweetpotato data in tricot-data, https://doi.org/10.5281/zenodo.17112492 (CC BY-SA 4.0); maize data on request (CIMMYT); code at https://github.com/hdorado/tricot-ranking-analysis, archived at https://doi.org/10.5281/zenodo.17942919 (MIT)
software: PlackettLuce
crops: groundnut, maize, sweetpotato
region: sub-Saharan Africa
keywords: genetic parameters, heritability, variance components, Thurstonian model, Plackett-Luce, two-step analysis, mixed models, ranking data, genetic gain, simulation
gist: Shows that genotype means and variances from Plackett-Luce or Thurstonian models can feed standard two-step mixed models to estimate heritability from tricot rankings
---

## Questions this paper answers

- Can heritability and variance components be estimated from ranking data?
- Are genotype estimates from rankings linearly related to those from quantitative traits?
- How can ranking analyses plug into standard breeding analysis pipelines?
- How reliable are heritability estimates from tricot trials?

## Summary

On-station trials represent on-farm conditions and farmer preferences poorly, which can misdirect breeding targets. Structured on-farm trials with ranking data, such as tricot, are more representative, but there was no scalable way to quantify genetic differences and the strength of the genetic signal from rankings. This paper proposes and tests one.

The procedure follows the familiar two-step approach of quantitative genetics. In the first step, Thurstonian or Plackett-Luce models produce tables of genotypic means and their variances from rankings, assuming rankings reflect an underlying continuous trait. In the second step, these estimates enter weighted mixed-effect models to estimate variance components and heritability, as breeders already do with yield data.

Simulations confirmed that genotype means from ranking analyses are linearly related to those from quantitative trait analyses, and that their variances capture the associated uncertainty. Second-step weighted mixed models recovered variance components accurately. Some limits appeared. Cullis heritability was negative in 17% to 19% of simulated trials, and heritability below 0.25 tended to be overestimated, with both quantitative and ranking-based estimates.

Applications to observed tricot data on groundnut, maize and sweetpotato showed the approach works on real trials and that ranking data provide reliable estimates of genetic parameters. The authors argue the framework can scale to estimate genotypic performance from multi-trial on-farm data, connecting tricot to standard breeding metrics such as heritability and genetic gain.

The simulations also defined when the method works. Estimates of genotypic means, their variances, the genetic standard deviation and heritability stayed accurate as long as replication compensated for uncertainty. In most scenarios about 30 replicates per genotype were enough, but more were needed when the ratio of genetic to residual standard deviation exceeded 2. The authors argue such conditions are realistic on farms, where this ratio is expected to be low. Because rankings are treated as reflecting continuous underlying utilities, a property of both Thurstonian and Plackett-Luce models, the procedure can analyze rankings for quantitative traits such as yield and for non-quantitative traits such as taste in the same way as conventional data. The authors stress that the approach is cost-effective, flexible and easy to implement in existing tools, and that it can be extended to multi-trial analyses following established two-step methods in plant breeding, which could encourage breeding programmes to adopt it in their pipelines. This links tricot directly to how breeding programmes already report progress, through heritability, variance components and genotype means with standard errors.

## Methods in brief

- **Step 1.** Thurstonian and/or Plackett-Luce models give genotype means and variances per trial.
- **Step 2.** Weighted mixed-effect models estimate variance components and heritability.
- **Validation.** Simulated trials comparing ranking-based and quantitative estimates.
- **Application.** Observed tricot data for groundnut, maize and sweetpotato, with groundnut and sweetpotato data from the public tricot-data collection.
- **Code.** R functions and simulation workflow shared on GitHub and archived on Zenodo.

## Stated limitations

- Cullis heritability can be negative in some simulated trials.
- Low heritability (below 0.25) is overestimated, with both ranking-based and quantitative data.
- More than 100 replicates may be needed when the true genetic standard deviation exceeds 2.
- The maize data were not yet open at publication.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 17%–19% | Simulated trials with negative Cullis heritability | This paper |
| <0.25 | Reference heritability below which estimates are inflated | This paper |
| 3 crops | Groundnut, maize and sweetpotato in the applications | This paper |
| ~30 | Replicates per genotype that were usually sufficient | This paper |
| >100 | Replicates possibly needed when the true genetic standard deviation exceeds 2 | This paper |

## Notes

- Published version of the VeriXiv preprint (https://doi.org/10.12688/verixiv.2606.1). The numbers used here are the same in both versions. Cite the journal article.
- The groundnut and sweetpotato data come from tricot-data, the data layer of the AI-ready documentation, so users can rerun the analysis.
- Complements desousa-2024-asd, which suggests Plackett-Luce worth can give direct estimates of genetic value.
