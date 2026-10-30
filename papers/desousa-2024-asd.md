---
id: desousa-2024-asd
title: The tricot approach. An agile framework for decentralized on-farm testing supported by citizen science. A retrospective
authors: de Sousa K, van Etten J, Manners R, and ~84 co-authors (last author Zaman-Allah M)
year: 2024
journal: Agronomy for Sustainable Development
journal_short: Agron Sustain Dev
article: 44, 8
type: review (retrospective)
doi: https://doi.org/10.1007/s13593-023-00937-1
open_copy: https://edoc.hu-berlin.de/18452/32306
license: CC BY 4.0
data: Zenodo (de Sousa 2022), data and code
crops: maize, potato, sweetpotato, cowpea, cassava, common bean, durum wheat, bread wheat, soybean
region: Global (India, Ethiopia, Central America, Eastern, Southern and West Africa)
keywords: tricot, citizen science, incomplete block design, ClimMob, Plackett-Luce, validity, reliability, cost, adoption, mainstreaming, product design, gender
gist: Retrospective on tricot's development, validity, cost, mainstreaming in breeding and open challenges
---

## Questions this paper answers

- How many farmers and entries does a tricot trial need?
- Are aggregated farmer rankings valid and reliable?
- How much does tricot cost compared with RCBD trials or group PVS?
- Why do farmers take part, and should they be paid?
- How do I get yield data that release committees accept?
- How has tricot been used inside breeding pipelines (CIMMYT, IITA, One Acre Fund)?
- Can tricot test consumer preferences or product concepts?

## Summary

The retrospective traces how tricot grew from a 2011 pilot into the leading on-farm testing method in the CGIAR-NARES network. It frames the problem participatory breeding never solved, which is matching varieties to heterogeneous environments and users at scale, with valid data and at reasonable cost. Earlier approaches, from farmer-first trials to mother-and-baby designs, captured local relevance but struggled with scale, data robustness and representativeness.

Tricot answers with crowdsourced citizen science. Each farmer tests a blind package of three options drawn from an A-optimal incomplete block design, which stays connected even when blocks are lost, and ranks them best and worst for each trait. ClimMob handles design, data collection and reporting, and the Plackett-Luce model aggregates the rankings.

The proof-of-concept phase (2011–2015, India, Ethiopia, Central America) tested four questions. Farmers joined mainly to contribute to science and learn from experts, not for cash. Aggregated farmer rankings agreed with breeder evaluations, and low individual reliability was offset by sample size, with about 12 entries across 150 farms enough to detect large effects. In Rwanda, tricot cost about 27% less per equivalent experimental unit than RCBD trials, and about 40% less in Central America. Adoption after tricot matched group-based PVS but did not exceed it, which the authors read as a question about whether product profiles fit farmer needs.

The data-driven phase built the statistics. Plackett-Luce models replaced pairwise rank-breaking, and covariates such as climate, genomic relatedness and item traits turned rankings into spatial recommendations, genetic estimates and preference models.

Mainstreaming in breeding followed. CIMMYT's maize network in Eastern and Southern Africa grew from under 50 to over 800 farms in two years, with grain-yield heritability above 0.6 and better inclusion of women. IITA released a cowpea variety in Nigeria on tricot evidence, and One Acre Fund used tricot to scale potato and maize varieties.

The authors are frank about obstacles. Release authorities want absolute yields, not ranks, so teams now combine rankings with yields from subsets of plots or farmer-led measurement. Tricot also needs data-science capacity in NARES, reliable seed logistics, and a hands-off management style that accepts on-farm noise. Payment can crowd out farmers' intrinsic motivation, while recognition reinforces it.

Recent work extends tricot to consumer testing and product concepts, including video-based maize concepts with 2,400 farmers in Kenya and Uganda, and to sampling designs that represent gender and socio-economic segments. The paper closes with six open issues, from financing and partnerships to GxExM interactions and how breeders act on results.

## Methods in brief

- **Design.** Incomplete blocks of three options per farmer, randomly assigned and A-optimal so the network stays connected if some blocks are lost. Entry names are masked. Use more than one check. Trials start from a target product profile.
- **Workflow.** Design and reporting on ClimMob. Farmers registered with Open Data Kit by field agents. Farmers name the best and worst option for each trait, and the third is ranked second. For consumer tests, assessment happens at registration.
- **Sample size.** About 12 entries across about 150 farms gives about 37 readings per entry, enough to detect a difference of 0.8 standard deviations (Cohen's d of 0.8) with 95% probability. Pilot with about 50 farmers in the first season.
- **Analysis.** Plackett-Luce model on full rankings (Turner et al. 2020), avoiding the biased p-values of pairwise rank-breaking. Covariates enter through recursive partitioning (Plackett-Luce trees). Quasi-variances and Bayesian bootstrapping give confidence intervals (de Sousa et al. 2023a). Genomic relatedness can enter as a covariance matrix in a Bayesian model (de Sousa et al. 2021), and item covariates link rankings to traits (Yildiz et al. 2020).
- **Yield data.** Measure yield on a subset of plots, combine ranks with metric data (van Heerwaarden et al. 2023, groundnut in Tanzania), or train farmers to measure yield with volumetric tins for grain or spring scales for cassava. Plackett-Luce log-worth tracks BLUP yield in simulation.
- **Socio-economic data.** A light version of RHoMIS for standard questions. For cassava in Nigeria, participant lists came from community leaders, snowball sampling and focus groups, followed by proportional sampling across user segments. Post-harvest traits are assessed by the person who does that work.
- **Incentives.** Farmers keep the harvest, unless the entries are hybrids or regulations forbid it. Recognition (certificates, branded t-shirts in Kenya) works better than cash.

## Stated limitations

- Rankings do not give absolute yields, which breeding programmes and release authorities still require.
- Individual farmer assessments have low reliability. Validity holds only in aggregate, so sample size matters.
- Adoption after tricot was comparable to group PVS, not higher, and adoption data are early (2015–2018).
- Data-science capacity in NARES programmes remains limited.
- Seed supply for breeding lines, seed quality assurance and logistics for bulky or perishable planting material are recurring bottlenecks.
- Hands-off management buys external validity at the cost of control and accountability.
- Participant representativeness, GxExM interactions and how breeders act on results remain open questions.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| ~150,000 plots | Tricot reach at time of writing (16,000 plots in 2016) | This paper; van Etten et al. 2016 |
| 426 farmers | Interviewed on motivation to join tricot | Beza et al. 2017 |
| ~12 entries, ~150 farms | ~37 readings per entry, detects Cohen's d of 0.8 with 95% probability; pilot with ~50 farmers | This paper |
| 27% | Lower cost per equivalent experimental unit, tricot vs RCBD, Rwanda maize (USD 4.45 vs 6.10) | This paper |
| ~17% | Lower total cost, same comparison (USD 1,517 vs 1,829) | This paper |
| 155 vs 50 trials | Tricot (11 varieties, 465 units, 341 equivalent units) vs RCBD (6 varieties, 300 units), Rwanda | This paper |
| USD 283.04 vs 522.72 | Seed cost, tricot vs RCBD, Rwanda, the largest saving | This paper |
| 0.73 | Relative efficiency of the incomplete block design | Bailey and Cameron 2009 |
| ~40% | Lower cost of tricot vs PVS in Central America | Occelli et al. 2024 |
| 20% vs 18% | Adoption after tricot (146/739) vs group PVS (74/394), Trifinio region | Occelli et al. 2024 |
| 1,268 farmers, 17 varieties | Sweetpotato tricot in Ghana, with 93 extension agents | This paper |
| >200 partners | Trained in tricot analysis since 2020 | This paper |
| 1,100 trials | Durum wheat on-farm trials in Ethiopia used with genomic data | de Sousa et al. 2021 |
| <50 → >800 farms | CIMMYT maize on-farm network, Eastern and Southern Africa, 2021–2022 | This paper; Voss et al. 2023 |
| ~20% / >0.6 | LSD as share of trial mean / broad-sense heritability for grain yield, CIMMYT network | This paper |
| 18 candidates, 320 farmers | IITA cowpea tricot, northern Nigeria, led to a 2022 release | This paper |
| >30 trials, 3,289 farmers, >85 varieties | One Acre Fund tricot since 2019 | This paper |
| 2,400 farmers, 8 concepts | Video-based maize product concept testing, Kenya and Uganda | Rutsaert et al. 2023 |

## Notes

- Reach is reported here as ~150,000 plots, while Cairns et al. 2026 cites the same source as >150,000 farmers. Use "plots" unless the PDF says otherwise.
- Table 1 caption says potato trials, but the text describes maize.
- Adoption rates are early and the authors call them conservative.
- Validity evidence comes from Steinke et al. 2017 (Honduras). Open that paper for the detailed comparison of farmer and breeder evaluations.
