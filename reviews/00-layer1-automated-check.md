# Layer 1: automated check of all cards

Checks every card against the text of its PDF in `papers-pdf/`. It confirms the DOI, title and author surnames appear in the PDF, and that each number in the card body appears in the PDF.
A number listed here was not found in the text extraction in that exact form. That can be a real error, a rounded or derived value, or a number shown only in a figure. Years that refer to other cards are left out. Title flags are mostly a colon in the original replaced by a period in the card.

Run on 2026-11-20. Two cards have no full source in the repo (one-page link stubs): howland-2025-report and vanetten-2011-idsbull.

| Card | Numbers checked | Numbers not found | Metadata flags |
|---|---|---|---|
| 1000farms-2025-report | 8 | 0 | 1 |
| alamu-2023-jsfa | 19 | 0 | 0 |
| angudubo-2026-guide | 25 | 5 | 0 |
| angudubo-2026-naro | 64 | 4 | 0 |
| angudubo-2026-zari | 58 | 3 | 0 |
| arnaud-2023-jsfa | 25 | 0 | 0 |
| beza-2017-plosone | 20 | 0 | 0 |
| brown-2022-cropsci | 20 | 0 | 0 |
| brown-2023-agronj | 37 | 3 | 0 |
| cairns-2025-ppp | 30 | 0 | 0 |
| cairns-2026-jxb | 45 | 0 | 0 |
| carroll-2020-dsj | 11 | 0 | 0 |
| chase-2026-book | 78 | 3 | 0 |
| daudi-2026-fes | 21 | 1 | 0 |
| desousa-2020-joss | 15 | 1 | 1 |
| desousa-2021-commsbio | 18 | 1 | 2 |
| desousa-2023-joss | 6 | 0 | 1 |
| desousa-2023-softwarex | 8 | 0 | 0 |
| desousa-2024-asd | 57 | 0 | 0 |
| donovan-2025-expagric | 12 | 0 | 0 |
| dorado-2026-tag | 10 | 1 | 0 |
| dumschott-2023-fps | 7 | 0 | 1 |
| fadda-2020-fps | 22 | 2 | 1 |
| gesesse-2023-pnas | 23 | 0 | 1 |
| goormachtigh-2026-flyer | 8 | 2 | 4 |
| gotor-2021-fsufs | 31 | 0 | 0 |
| hansson-2019-ejps | 15 | 1 | 0 |
| howland-2025-report | 44 | no source | |
| jorgensen-2026-gse | 14 | 0 | 0 |
| kadege-2026-fsufs | 42 | 0 | 1 |
| kang-2025-expagric | 14 | 0 | 0 |
| kool-2020-expagric | 36 | 0 | 0 |
| laajaj-2020-scirep | 23 | 0 | 0 |
| mancini-2017-scirep | 22 | 2 | 1 |
| mawia-2025-fsufs | 39 | 0 | 1 |
| mbugua-2024-mib | 12 | 0 | 0 |
| moyo-2021-fsufs | 13 | 0 | 0 |
| mulatu-2024-slides | 7 | 1 | 0 |
| muller-2025-ux | 12 | 0 | 1 |
| nabateregga-2025-eja | 19 | 0 | 0 |
| nanyonjo-2024-cropsci | 21 | 0 | 0 |
| occelli-2024-agecon | 12 | 0 | 1 |
| occelli-2024-natplants | 44 | 2 | 0 |
| occelli-2026-ahv | 23 | 1 | 0 |
| olaosebikan-2023-jsfa | 11 | 0 | 0 |
| quiros-2024-compag | 17 | 0 | 0 |
| rutsaert-2023-mib | 6 | 0 | 0 |
| schumann-2024-ux | 2 | 0 | 1 |
| selby-2025-database | 16 | 1 | 0 |
| sharma-2025-jafr | 13 | 0 | 0 |
| steinke-2016-guide | 10 | 0 | 0 |
| steinke-2017-asd | 22 | 0 | 0 |
| steinke-2019-plosone | 15 | 0 | 0 |
| tanaka-2021-tag | 30 | 0 | 1 |
| teeken-2021-fsufs | 21 | 0 | 0 |
| teeken-2023-slides | 16 | 0 | 0 |
| thiele-2021-ijfst | 18 | 0 | 0 |
| turner-2020-compstat | 11 | 0 | 0 |
| ulzen-2025-agrirxiv | 25 | 0 | 2 |
| vandegevel-2020-asd | 10 | 1 | 0 |
| vanetten-2011-idsbull | 7 | no source | |
| vanetten-2019-expagric | 15 | 0 | 0 |
| vanetten-2019-pnas | 36 | 0 | 1 |
| vanetten-2020-guide | 12 | 0 | 0 |
| vanetten-2020-rtbwp | 11 | 0 | 0 |
| vanetten-2023-pnas | 6 | 0 | 2 |
| voss-2021-outlook | 21 | 0 | 1 |
| voss-2023-fsoc | 16 | 0 | 1 |
| voss-2025-ppp | 9 | 0 | 0 |
| woldeyohannes-2022-elife | 27 | 0 | 0 |

## Details

### 1000farms-2025-report

- Metadata, author: `CIMMYT (CGIAR Dryland Crops Program) and Bioversity International (1000FARMS)`

### angudubo-2026-guide

- `1.26` in: / USD 1.00 to 1.26 (25.7%) / US inflation 2019 to 2025, used to update UN mileage rates, worked example / This guide; usinflationcalculator.com /
- `25.7` in: / USD 1.00 to 1.26 (25.7%) / US inflation 2019 to 2025, used to update UN mileage rates, worked example / This guide; usinflationcalculator.com /
- `363` in: / 300 farmers, 363 days, 70 m2 blocks / Worked example of trial dimensions, cassava in Uganda with NARO / This guide /
- `0.0175` in: - The worked example gives a 70 m2 block as 0.0175 acres; 70 m2 is about 0.0173 acres.
- `0.0173` in: - The worked example gives a 70 m2 block as 0.0175 acres; 70 m2 is about 0.0173 acres.

### angudubo-2026-naro

- `10,325.9` in: - The body says travel, labour and transport total USD 10,070.4 (about 91%). That sum leaves out the travel allowance. With it the three components total USD 10,325.9 (about 93%).
- `93` in: - The body says travel, labour and transport total USD 10,070.4 (about 91%). That sum leaves out the travel allowance. With it the three components total USD 10,325.9 (about 93%).
- `3,296` in: - An 81% cut in field labour is about USD 3,296, slightly below the USD 3,393.7 scenario saving.
- `142` in: - Compared with the Zambia maize case (USD 142 per farmer, travel and materials largest), costs here are lower per farmer and driven by labour and transport. Both reports attribute cost mainly to deli

### angudubo-2026-zari

- `1,564` in: - The 24% cut in travel expenses (about USD 1,564) roughly matches the USD 1,550 scenario saving. The stated 50.5% cut in field labour (about USD 1,129) is slightly above the USD 1,106 saving reported
- `50.5` in: - The 24% cut in travel expenses (about USD 1,564) roughly matches the USD 1,550 scenario saving. The stated 50.5% cut in field labour (about USD 1,129) is slightly above the USD 1,106 saving reported
- `1,129` in: - The 24% cut in travel expenses (about USD 1,564) roughly matches the USD 1,550 scenario saving. The stated 50.5% cut in field labour (about USD 1,129) is slightly above the USD 1,106 saving reported

### brown-2023-agronj

- `69` in: Climate for the evaluation period of each ranking came from AgERA5, with rainfall and temperature indices from climatrends and relative humidity at five times of day. A Plackett-Luce tree with climate
- `0.7` in: Climate for the evaluation period of each ranking came from AgERA5, with rainfall and temperature indices from climatrends and relative humidity at five times of day. A Plackett-Luce tree with climate
- `0.5` in: / 0.509 / Reliability of Saba in dry environments, the only one above 0.5 / This paper /

### chase-2026-book

- `315` in: Each section below gives the chapter authors, the PDF pages of the version checked (the 315-page PDF in `papers-pdf/`), the questions it answers, a summary and the practical guidance a user is most li
- `314` in: **Authors.** Community of Practice by Rachel Chase. Other sections unattributed. PDF pages 204 to 314.
- `469` in: - The trial-size chapter says rank-based estimates are unreliable when n is below 20 in one place and sets 30 as the minimum to aim for in another. The sampling-tool example gives 467 farms but 67 per

### daudi-2026-fes

- `878` in: Genotype, environment and their interaction all significantly affected kernel yield. ICGV-SM 05534 gave the highest mean kernel yield, about 927 kg/ha. A GGE biplot identified ICGV-SM 16645 and ICGV-S

### desousa-2020-joss

- Metadata, author: `Solberg SØ`
- `1.1` in: - The current CRAN version (1.1) also covers CHIRTS temperature data, which the 2020 paper does not describe. Check the CRAN reference manual for current functions and whether IMERG and ESI are still 

### desousa-2021-commsbio

- Metadata, author: `Solberg SØ`
- Metadata, author: `Dell'Acqua M`
- `1,100` in: - de Sousa et al. 2024 (desousa-2024-asd) cites this as 1,100 durum wheat on-farm trials. The paper itself reports 1,165 farms.

### desousa-2023-joss

- Metadata, author: `Solberg SØ`

### dorado-2026-tag

- `10.12688` in: - Published version of the VeriXiv preprint (https://doi.org/10.12688/verixiv.2606.1). The numbers used here are the same in both versions. Cite the journal article.

### dumschott-2023-fps

- Metadata, title: `Ontologies for increasing the FAIRness of plant research data`

### fadda-2020-fps

- Metadata, author: `Dell'Acqua M`
- `400` in: - The panel is 373 + 27 here, but 400 with 25 modern varieties in mancini-2017-scirep.
- `25` in: - The panel is 373 + 27 here, but 400 with 25 modern varieties in mancini-2017-scirep.

### gesesse-2023-pnas

- Metadata, author: `Dell'Acqua M`

### goormachtigh-2026-flyer

- Metadata, title: `Sikia. Listening at scale`
- Metadata, author: `Goormachtigh L`
- Metadata, author: `Mutuvi S`
- Metadata, author: `Woltering L`
- `19` in: - Authorship follows the team's attribution (Laurens Goormachtigh, Stephen Mutuvi, Lennart Woltering). The Alliance story of 19 October 2026 lists Laurens Goormachtigh, Stephen Mutuvi and Anastacia Wa
- `480` in: - chase-2026-book lists Sikia among tools in development and reports a test on a Tanzanian bean trial with 480 participants. This flyer documents it as integrated with ClimMob. See quiros-2024-compag 

### hansson-2019-ejps

- `3.3` in: / ~860 million / People working on farms worldwide (26% of a 3.3 billion workforce) / ILO 2018, cited in this paper /

### kadege-2026-fsufs

- Metadata, title: `Tanzanian farmers' preferred traits for common bean varieties. Breeding insights from the tricot approach`

### mancini-2017-scirep

- Metadata, author: `Dell'Acqua M`
- `375` in: - **Material.** 400 genebank accessions (375 landraces, 25 modern varieties), two locations, 20 × 20 partial lattice with two replications, 2012 season.
- `373` in: - Fadda et al. 2020 describes the same panel as 373 farmer varieties and 27 improved varieties, while this paper reports 25 modern varieties among 400.

### mawia-2025-fsufs

- Metadata, title: `Understanding seed selection decisions among small-scale maize farmers in Machakos County, Kenya. The dominance of market leader varieties`

### mulatu-2024-slides

- `20` in: - **Evaluation.** Best-worst rankings for about 20 traits at first and second harvest.

### muller-2025-ux

- Metadata, title: `Farmer feedback in tricot. Redesigning the tricot feedback process and field validation 2024–2025`

### occelli-2024-agecon

- Metadata, author: `Dell'Acqua M`

### occelli-2024-natplants

- `4.2` in: - **Synthesis.** Descriptive analysis in R 4.2.3, author and donor networks in VOSviewer, four crop groups (commodity and ornamental crops, 3% of studies, excluded).
- `49.5` in: / 49.5% / Median share of women respondents in the 216 sex-disaggregated studies / This paper /

### occelli-2026-ahv

- `1000` in: - Useful context for tricot institutionalization questions. It shows the gap between practice and codified policy that the team's own mainstreaming work faces (1000farms-2025-report, howland-2025-repo

### schumann-2024-ux

- Metadata, author: `Londoño JM`

### selby-2025-database

- `75` in: - Around 75 named authors plus the BrAPI Consortium. The card lists only the first five and the team's authors.

### tanaka-2021-tag

- Metadata, author: `Kajiya-Kanegae H`

### ulzen-2025-agrirxiv

- Metadata, author: `Osei-Bonsu NO`
- Metadata, author: `Dorado-Betancourt H`

### vandegevel-2020-asd

- `1000` in: - Its barriers to mainstreaming match those found in occelli-2026-ahv for Farmer First programmes and in howland-2025-report for 1000FARMS.

### vanetten-2019-pnas

- Metadata, author: `Dell'Acqua M`

### vanetten-2023-pnas

- Metadata, author: `Dell'Acqua M`
- Metadata, author: `Solberg SØ`

### voss-2021-outlook

- Metadata, title: `Gender inclusivity through maize breeding in Africa. A review of the issues and options for future engagement`

### voss-2023-fsoc

- Metadata, title: `Innovative approaches to integrating gender into conventional maize breeding. Lessons from the Seed Production Technology for Africa project`
