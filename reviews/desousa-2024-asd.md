# Card review: desousa-2024-asd

- **Card:** papers/desousa-2024-asd.md
- **Source:** papers-pdf/de-sousa-et-al-2024.pdf (19 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 69 |
| Supported | 50 |
| Imprecise | 16 |
| Not in source | 2 |
| Contradicted | 1 |
| Important omissions | 12 |
| Metadata issues | 5 |

The card is careful and mostly accurate. Its numbers match the paper, and it already flags the two main traps (plots vs farmers, and the Rwanda crop). The most important fix is the Key numbers row for the ~40% Central America figure. The card says "vs PVS", but the paper says ~40% cheaper than RCBD (p. 6). Other fixes are about overstated certainty (payment and recognition, yield methods, validity), a wrong author count, and a few missing practical details that tricot users would want.

## Fixes needed

1. **Key numbers row "~40%" (Contradicted).** The card says "Lower cost of tricot vs PVS in Central America". The paper says tricot "has shown to be ~40% cheaper than RCBD", citing Occelli et al. 2024, and adds that tricot had higher costs for phone calls and seed packaging (p. 6). The card's own frontmatter says the cited source reports 28% against group PVS. That may be true, but it cannot be checked from this PDF, and the row should report what this paper says. Replace the row with:

   `| ~40% | Lower cost of tricot vs RCBD in Central America, as stated by this paper (p. 6), with higher costs for phone calls and seed packaging. The cited source reportedly gives 28% vs group PVS (see not_established) | Occelli et al. 2024 (cited secondhand) |`

2. **Summary, cost sentence (Imprecise).** The card says tricot cost 27% less "in a single case study of potato trials in Rwanda" and "the paper cites about 40% less in Central America". Problems: (a) the 40% has no comparator (the paper says RCBD, p. 6), (b) the PDF itself is inconsistent about the crop. The text says maize twice and the Table 1 caption says potato (p. 6), (c) the study ran over two seasons, and the paper says costs are country specific (p. 6). Replace the sentence with:

   "In one Rwanda case study over two seasons (Table 1 says potato, the text says maize), tricot cost about 27% less than RCBD per equivalent experimental unit. The paper also cites about 40% lower cost than RCBD in Central America and notes that costs are country specific."

3. **Frontmatter authors (Imprecise).** The card says "and ~84 co-authors". The byline lists 81 authors in total (p. 1 and p. 18), so there are 78 after the first three. Replace with:

   `authors: de Sousa K, van Etten J, Manners R, and 78 co-authors (last author Zaman-Allah M)`

4. **Methods, Incentives bullet (Not in source, overstated).** The card says recognition "(certificates, branded t-shirts in Kenya) works better than cash". Certificates do not appear anywhere in the paper. The paper reports that farmers in Uganda expected recognition, that the team considered offering co-authorship, and that farmers in Kenya suggested a t-shirt with a project logo (p. 5). On cash, it only says payments "may" crowd out intrinsic motivation and calls for more research (p. 12). Replace the bullet with:

   "- **Incentives.** Farmers keep the harvest, unless the entries are hybrids or national regulations forbid it. Farmers in Uganda expected recognition, and farmers in Kenya suggested t-shirts with a project logo. The team also considered co-authorship. The authors suggest that payment may crowd out intrinsic motivation, but they call for more research."

5. **Summary, validity sentence (Imprecise).** The card says aggregated rankings "agreed with breeder evaluations" and that low reliability "was offset by sample size". The paper says aggregated farmer assessments had "adequate validity" and that low reliability "should be compensated" with more samples (p. 6). The 12 entries and 150 farms figure is the authors' rule of thumb ("In our experience"), not a result of Steinke et al. Replace with:

   "In Honduras, aggregated farmer assessments showed adequate validity against breeders' evaluations, but individual reliability was low, so large samples are needed. As a rule of thumb, about 12 entries across about 150 farms can detect large effects."

6. **Summary, payment sentence (Imprecise).** The card states as fact that "Payment can crowd out farmers' intrinsic motivation, while recognition reinforces it." The paper presents this as a possibility based on an analogy with blood donors, and asks for more research (p. 12). Replace with:

   "The authors suggest that payment may crowd out farmers' intrinsic motivation and that local recognition may strengthen it, and they call for more research."

7. **Questions, third question (Not in source).** The card asks "How much does tricot cost compared with RCBD trials or group PVS?" This paper compares cost only with RCBD (p. 6). The group PVS comparison is about adoption (p. 7). Replace with:

   "- How much does tricot cost compared with RCBD trials?"

8. **Summary, yield sentence (Imprecise).** The card says "teams now combine rankings with yields from subsets of plots or farmer-led measurement". The paper says these approaches "have been proposed" and teams are "testing different approaches", with preliminary results only (p. 11). Replace with:

   "Breeding programmes and release authorities want absolute yields, not ranks, so teams are testing ways to combine rankings with yields measured on a subset of plots or by farmers."

9. **Summary, adoption sentence (Imprecise).** The card gives only one explanation. The paper raises two: whether target product profiles address farmer needs, and whether receiving a non-preferred variety in the package affects adoption (p. 7). Replace with:

   "Adoption after tricot was comparable to group-based PVS but not higher. The authors ask whether product profiles fit farmer needs, or whether a non-preferred variety in the package discouraged adoption."

10. **not_established, items 2 and 3 (Imprecise).** Item 2 reads as if the paper does not claim 40% against RCBD. It does (p. 6). The weakness is that the claim is secondhand. Item 3 states the crop as potato, but the PDF is inconsistent. Replace the field with (the semicolons are the field separator the template requires):

    `not_established: over 150,000 farmers (it reports about 150,000 plots); a 40% saving against RCBD as a primary result (the paper states it on p. 6 but cites Occelli et al. 2024, which reportedly reports 28% against group PVS); a general cost of tricot or a general 27% saving against RCBD (the cost comparison is one Rwanda case study over two seasons, and the authors say costs are country specific)`

11. **Key numbers row "0.73" (Imprecise attribution).** The formula comes from Bailey and Cameron 2009, but the value 0.73 is this paper's calculation for 11 varieties in blocks of three (p. 6). Check: 11/10 × 2/3 = 0.733, and 465 × 0.733 = 341 EEU, which matches Table 1. Replace the Primary source cell with:

    `This paper (formula from Bailey and Cameron 2009)`

12. **Key numbers row "<50 → >800 farms" (Imprecise attribution).** The farm numbers are reported in this paper without citation (p. 9). Voss et al. 2023 is cited only for the improved sampling and better representation of women. Replace the Primary source cell with:

    `This paper (Voss et al. 2023 for the gender sampling)`

13. **Frontmatter crops (Imprecise).** The paper also covers rice (India, p. 4) and groundnut (Tanzania, p. 11). It mentions bean in One Acre Fund trials and planned sorghum trials (p. 10). Replace with:

    `crops: maize, potato, sweetpotato, cowpea, cassava, common bean, durum wheat, bread wheat, rice, groundnut, soybean`

14. **Summary, sentence 2 (Imprecise).** The card adds "at reasonable cost" to the list of unsolved problems. The abstract lists scalability, data validity and reliability, and heterogeneity (p. 1). Replace "with valid data and at reasonable cost" with "with valid and reliable data".

15. **Summary, ClimMob sentence (Imprecise, low).** The paper says ClimMob supports design, data management and reporting, and that field agents register farmers with Open Data Kit (p. 3 to 4). Replace with:

    "ClimMob handles design, data management and reporting, field agents register farmers with Open Data Kit, and the Plackett-Luce model aggregates the rankings."

16. **Summary, motivation sentence (Imprecise, low).** The paper says farmers wanted to contribute to research and "to share information and interact with experts" (p. 5). Few expected money. Replace with:

    "Farmers said they joined mainly to contribute to research and to exchange information with experts, and few expected money."

17. **Summary, first sentence (Imprecise, low).** "the leading on-farm testing method" is the authors' own claim (p. 13). Replace "into the leading" with "into what the authors call the leading".

18. **Summary, cowpea sentence (low).** National authorities release varieties, not IITA. Replace "IITA released a cowpea variety in Nigeria on tricot evidence" with "A cowpea variety from IITA's tricot trials was released in Nigeria in 2022 with tricot data as on-farm evidence".

19. **Methods, Yield data bullet (Imprecise, low).** The paper does not say farmers are trained. It says farmers "can measure yields themselves", that teams are testing approaches in maize, common bean and cassava, and that preliminary results show relatively good agreement with measured yields (p. 11). Also, van Heerwaarden et al. 2023 is listed as submitted, not published (p. 17). Replace the bullet with:

    "- **Yield data.** Field agents measure yield on a subset of plots, and ranks can be combined with metric data (van Heerwaarden et al. 2023, submitted, groundnut in Tanzania). Farmers can also measure yield with volumetric tins for grain or spring scales for cassava. Teams are testing this in maize, common bean and cassava, and preliminary results show relatively good agreement with measured yields. Plackett-Luce log-worth tracks simulated yield BLUPs."

20. **gist (template).** The current gist lists topics but does not say what the paper shows. Replace with (29 words):

    `gist: Retrospective of 12 years of tricot: aggregated farmer rankings are adequately valid with large samples, one Rwanda case cost 27% less than RCBD, and breeding programmes now use it.`

21. **Key numbers rows "~17%" and "USD 283.04 vs 522.72" (label).** Both are correct, but the card computed them. The paper does not state them. Add "(computed from Table 1)" to the Context cell of each row. Also consider a new row: `| USD 390.58 vs 106.33 | Material cost, tricot vs RCBD, Rwanda, the one cost that was higher for tricot | This paper (Table 1) |`

22. **Frontmatter title and data (low).** The real title uses a colon after "The tricot approach" (p. 1). If YAML needs it, quote the title. The data field can add the Zenodo DOI given on p. 16:

    `title: "The tricot approach: an agile framework for decentralized on-farm testing supported by citizen science. A retrospective"`

    `data: Zenodo, data and code (de Sousa 2022), https://doi.org/10.5281/zenodo.6286006`

A full revised Summary that applies fixes 2, 5, 6, 8, 9 and 14 to 18 is given at the end of this report (495 words).

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | "The tricot approach. An agile framework ... A retrospective" | Colon after "approach", lowercase "an" (p. 1) | Imprecise (punctuation only) |
| authors | de Sousa K, van Etten J, Manners R, and ~84 co-authors, last Zaman-Allah M | 81 authors, so 78 co-authors after the first three, last Zaman-Allah M (p. 1, p. 18) | Imprecise |
| year | 2024 | Published online 25 January 2024, volume 2024 (p. 1) | Supported |
| journal | Agronomy for Sustainable Development | Same (p. 1) | Supported |
| article | 44, 8 | "(2024) 44:8" (p. 1) | Supported |
| type | review (retrospective) | "REVIEW ARTICLE" (p. 1) | Supported |
| doi | 10.1007/s13593-023-00937-1 | Same (p. 1) | Supported |
| open_copy | edoc.hu-berlin.de/18452/32306 | Not stated in PDF | Not checkable from PDF |
| license | CC BY 4.0 | Creative Commons Attribution 4.0 (p. 15) | Supported |
| data | Zenodo (de Sousa 2022), data and code | Data and code on Zenodo, de Sousa 2022 (p. 15), DOI 10.5281/zenodo.6286006 (p. 16) | Supported (DOI could be added) |
| crops | maize, potato, sweetpotato, cowpea, cassava, common bean, durum wheat, bread wheat, soybean | Also rice (p. 4) and groundnut (p. 11) | Imprecise |
| region | Global (India, Ethiopia, Central America, Eastern, Southern and West Africa) | India, Ethiopia, four Central American countries, Ghana, Rwanda, Nigeria, Kenya, Uganda, Tanzania, Cameroon and others (p. 4 to 13) | Supported |
| gist | Retrospective on development, validity, cost, mainstreaming and open challenges | Topics are correct | Supported (template issue, see fix 20) |
| not_established, item 1 | over 150,000 farmers | "~150,000 farmer-managed plots" (p. 3) | Supported |
| not_established, item 2 | 40% vs RCBD not established | Paper states ~40% vs RCBD, secondhand from Occelli et al. 2024 (p. 6). The 28% vs PVS cannot be checked here | Imprecise |
| not_established, item 3 | 27% is a single potato case in Rwanda | Rwanda, two seasons, crop inconsistent (text maize, Table 1 potato), costs "country specific" (p. 6) | Imprecise |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Frontmatter | ~84 co-authors | Imprecise | 81 authors in byline (p. 1, 18) | 78 co-authors |
| 2 | Frontmatter | article 44, 8 | Supported | p. 1 | |
| 3 | Frontmatter | license CC BY 4.0 | Supported | p. 15 | |
| 4 | Frontmatter | data on Zenodo, data and code | Supported | p. 15 to 16 | Add DOI |
| 5 | Frontmatter | crops list | Imprecise | Rice p. 4, groundnut p. 11 | Missing two crops |
| 6 | Frontmatter | region | Supported | p. 4 to 13 | |
| 7 | Frontmatter | gist | Supported | Whole paper | Describes topics, not findings |
| 8 | Frontmatter | not_established: farmers vs plots | Supported | p. 3 | |
| 9 | Frontmatter | not_established: 40% vs RCBD | Imprecise | p. 6 | Paper does state it, secondhand |
| 10 | Frontmatter | not_established: 27% single potato case | Imprecise | p. 6, Table 1 | Crop inconsistent in PDF |
| 11 | Questions | Cost vs RCBD or group PVS | Not in source | p. 6 to 7 | Cost compared only with RCBD |
| 12 | Summary | 2011 pilot to leading method in CGIAR-NARES network | Imprecise | p. 4, p. 13 | Authors' own claim, should be attributed |
| 13 | Summary | Unsolved problem includes "reasonable cost" | Imprecise | Abstract lists scalability, validity, reliability, heterogeneity (p. 1) | Cost is not in that list |
| 14 | Summary | Earlier approaches struggled with scale, robustness, representativeness | Supported | p. 2 to 3 | "farmer-first" is the card's label for Rhoades and Booth 1982 |
| 15 | Summary | tricot uses crowdsourced citizen science | Supported | p. 1 | |
| 16 | Summary | Blind package of three, A-optimal, best and worst per trait | Supported | p. 3 to 4, Fig. 1 to 2 | |
| 17 | Summary | ClimMob handles design, data collection and reporting | Imprecise | p. 3 to 4 | ClimMob does data management, collection via Open Data Kit |
| 18 | Summary | Proof of concept 2011 to 2015, three regions, four questions | Supported | p. 4 to 5 | |
| 19 | Summary | Farmers joined to contribute to science and learn from experts, not cash | Imprecise | p. 5 | Paper says share information and interact with experts. p. 12 also says seeds and information |
| 20 | Summary | Rankings agreed with breeders, reliability offset, 12 entries and 150 farms | Imprecise | p. 6 | "adequate validity", "should be compensated", rule of thumb |
| 21 | Summary | 27% less in potato case, ~40% less in Central America | Imprecise | p. 6, Table 1 | No comparator for 40%, crop inconsistent, two seasons |
| 22 | Summary | Adoption matched PVS, product profile question | Imprecise | p. 7 | Second explanation omitted |
| 23 | Summary | Plackett-Luce replaced pairwise rank-breaking | Supported | p. 7 | |
| 24 | Summary | Covariates gave spatial recommendations, genetic estimates, preference models | Supported | p. 7 to 9 | |
| 25 | Summary | CIMMYT under 50 to over 800 farms, H2 above 0.6, more women | Supported | p. 9 | Paper says "in 2022", adopted 2021 to 2022 |
| 26 | Summary | IITA cowpea release, One Acre Fund potato and maize | Supported | p. 10 | Released by national system, not IITA |
| 27 | Summary | Release authorities want yields, teams now combine | Imprecise | p. 10 to 11 | Approaches proposed and being tested |
| 28 | Summary | Needs data-science capacity, seed logistics, hands-off style | Supported | p. 11 to 12 | |
| 29 | Summary | Payment crowds out, recognition reinforces | Imprecise | p. 12 | Paper says "may", calls for more research |
| 30 | Summary | Consumer testing, 2,400 farmers video concepts, sampling designs | Supported | p. 12 to 13 | |
| 31 | Summary | Six open issues | Supported | p. 14 | |
| 32 | Methods | Design: blocks of three, random, A-optimal, masked, more than one check, TPP | Supported | p. 3 to 4, Fig. 1 to 2 | |
| 33 | Methods | Workflow: ClimMob, ODK, best and worst, consumer tests at registration | Supported | Fig. 2 (p. 4) | |
| 34 | Methods | 12 entries, 150 farms, 37 readings, d of 0.8, 95%, pilot 50 farmers | Supported | p. 6 | 150 × 3 / 12 = 37.5, matches |
| 35 | Methods | Analysis: Plackett-Luce, rank-breaking bias, trees, quasi-variances, genomic, item covariates | Supported | p. 7 to 8 | "Plackett-Luce trees" is not the paper's term, but Fig. 4 shows model nodes |
| 36 | Methods | Yield subset, combine ranks, train farmers with tins and scales | Imprecise | p. 11 | "train" not stated, approaches still being tested, van Heerwaarden submitted |
| 37 | Methods | Log-worth tracks BLUP yield in simulation | Supported | Fig. 6, p. 11 | |
| 38 | Methods | RHoMIS light, Nigeria cassava sampling, post-harvest by person doing the work | Supported | p. 13 | |
| 39 | Methods | Farmers keep harvest except hybrids or regulations | Supported | p. 5 to 6 | |
| 40 | Methods | Recognition (certificates, t-shirts) works better than cash | Not in source | p. 5, p. 12 | No certificates. Comparison with cash not shown |
| 41 | Limitations | No absolute yields | Supported | p. 10 | |
| 42 | Limitations | Low individual reliability, validity in aggregate | Supported | p. 6 | |
| 43 | Limitations | Adoption comparable, early data 2015 to 2018 | Supported | p. 7 | |
| 44 | Limitations | Limited data-science capacity in NARES | Supported | p. 12 | |
| 45 | Limitations | Seed supply, quality, bulky planting material | Supported | p. 11, p. 13 | |
| 46 | Limitations | Hands-off vs control and accountability | Supported | p. 11, p. 14 | |
| 47 | Limitations | Representativeness, GxExM, breeder response open | Supported | p. 14 | |
| 48 | Key numbers | ~150,000 plots, 16,000 in 2016 | Supported | p. 3 | |
| 49 | Key numbers | 426 farmers interviewed, Beza et al. 2017 | Supported | p. 5 | |
| 50 | Key numbers | 12 entries, 150 farms, d 0.8, pilot 50 | Supported | p. 6 | |
| 51 | Key numbers | 27%, USD 4.45 vs 6.10 | Supported | p. 6, Table 1 | 1 − 4.45/6.10 = 27.0%. Crop caveat as in Notes |
| 52 | Key numbers | ~17% lower total cost | Supported | Table 1 | 1 − 1517.18/1829.07 = 17.1%. Computed by card, label it |
| 53 | Key numbers | 155 vs 50 trials, 11 vs 6 varieties, 465 and 341 vs 300 units | Supported | p. 6, Table 1 | |
| 54 | Key numbers | Seed cost 283.04 vs 522.72, largest saving | Supported | Table 1 | Saving 239.68 is the largest. Material cost was higher for tricot |
| 55 | Key numbers | 0.73 relative efficiency, Bailey and Cameron 2009 | Imprecise | p. 6 | Value computed by this paper |
| 56 | Key numbers | ~40% lower cost vs PVS, Central America | Contradicted | p. 6 | Paper says vs RCBD |
| 57 | Key numbers | Adoption 20% (146/739) vs 18% (74/394) | Supported | p. 7 | Matches paper. Exact values are 19.8% and 18.8% |
| 58 | Key numbers | 1,268 farmers, 17 varieties, 93 agents, Ghana | Supported | p. 7 to 8 | Six regions |
| 59 | Key numbers | >200 partners trained since 2020 | Supported | p. 9 | |
| 60 | Key numbers | 1,100 durum wheat trials, de Sousa et al. 2021 | Supported | p. 9 | |
| 61 | Key numbers | <50 to >800 farms, This paper and Voss et al. 2023 | Imprecise | p. 9 | Voss cited for gender sampling only |
| 62 | Key numbers | LSD ~20% of mean, H2 > 0.6 | Supported | p. 9 | |
| 63 | Key numbers | 18 candidates, 320 farmers, 2022 release | Supported | p. 10 | Released as SAMPEA 21, 16 local government areas |
| 64 | Key numbers | One Acre Fund >30 trials, 3,289 farmers, >85 varieties | Supported | p. 10 | |
| 65 | Key numbers | 2,400 farmers, 8 concepts, Rutsaert et al. 2023 | Supported | p. 13 | |
| 66 | Notes | Reach reported as ~150,000 plots | Supported | p. 3 | The PDF does say plots, so the note can drop "unless the PDF says otherwise" |
| 67 | Notes | Table 1 says potato, text says maize | Supported | p. 6 | Author confirmation is outside the PDF. The paper's Rwanda potato case on p. 8 also has 11 varieties, which fits potato |
| 68 | Notes | Adoption rates early, authors call them conservative | Supported | p. 7 | "conservative" refers to the adopter definition |
| 69 | Notes | Validity evidence from Steinke et al. 2017, Honduras | Supported | p. 6 | |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: describe how tricot evolved, how it is used and modified in public breeding (p. 3) | Yes | High | None |
| Five development phases plus gender section (p. 3) | Yes | High | None |
| Core protocol for all trials: core traits (yield, overall appreciation, marketability), socio-economic indicators, plot characterization (p. 11) | No | High | Methods bullet: "- **Core protocol.** Trials follow a protocol agreed by breeders, socio-economists and other stakeholders, with core traits (for example yield, overall appreciation, marketability), socio-economic indicators and plot characterization collected in all trials, so data can be pooled." |
| Cost study context: two seasons, EEU assumes no plot heterogeneity (called conservative), costs country specific, tricot material costs higher (p. 6, Table 1) | Partly | High | Covered by fixes 2, 10 and 21. Add to Stated limitations: "- The cost comparison is one Rwanda case. It ignores plot heterogeneity, and the authors say costs are country specific." |
| Central America: higher costs for phone calls and seed packaging (p. 6) | No | Medium | Covered by fix 1 |
| Adoption details: adopter = planted and harvested three years later, 7 of 19 varieties not yet released by 2018, two possible explanations (p. 7) | Partly | Medium | Add to Notes: "In the adoption study, 7 of the 19 varieties were not yet released at the 2018 endline, which limits adoption." |
| van Etten et al. 2019a: 12,409 plots in Nicaragua, India and Ethiopia, climate effects, probability of outperforming a check (p. 7) | No | Medium | Key numbers row: `| 12,409 plots | Data used to show climate effects on variety performance, Nicaragua, India, Ethiopia | van Etten et al. 2019a |` |
| Spatial case studies: sweetpotato Ghana, potato Rwanda (11 varieties, 7 districts, 135 trials in first season) (p. 7 to 8) | Partly | Medium | Key numbers row: `| 11 varieties, 135 trials | Potato tricot in seven districts of Rwanda, first season, used for climate-based recommendations | This paper |` |
| CIMMYT: smaller plots let farmers with small fields and women take part, fewer "leadership effects" than group PVS, earlier RCBD of 20 to 30 hybrids × 3 reps per farm (p. 9 to 10) | Partly | Medium | Add to Notes: "In the CIMMYT network, smaller plots let farmers with very small fields and more women take part. Individual trials also reduce leadership effects seen in group PVS." |
| Farmer-led yield estimates in preliminary agreement with measured yields (p. 11) | No | Medium | Covered by fix 19 |
| Illustrated booklets in local language for illiterate farmers (Fig. 3, p. 5) | No | Medium | Add to Workflow bullet: "Data collection booklets use pictures and the local language so that farmers who cannot read can take part." |
| Nigeria: farmers plant their own local variety next to the three entries, now adopted (p. 13) | No | Medium | Add to Socio-economic data bullet: "In Nigeria, farmers also plant their own local variety next to the three entries." |
| Early-generation lines may give low yields and lower motivation, avoid farmer burnout by focusing data collection on key crop stages (p. 12) | No | Medium | Add to Stated limitations: "- Testing early breeding lines may give farmers low yields and reduce motivation. Too much data collection can cause farmer burnout." |
| Conclusions: standard routines key to scaling, more cost cuts if farmer networks are kept, shared channels, multiple crops, outsourcing to farmer-facing organisations, participants in decision roles (p. 13 to 14) | No | Medium | Add to Summary or Notes: "The authors conclude that standard routines made scaling possible, and that costs could fall further if farmer networks are kept and serve several crops." |
| Cohen's d of 0.8 acceptable because effects shrink over seasons (p. 6) | No | Low | Optional |
| ClimMob link with BreedBase through the Crop Ontology (p. 9) | No | Low | Optional |
| Goals and crops of proof of concept (rice and bread wheat in India, durum wheat genebank in Ethiopia, drought-tolerant bean in Central America) (p. 4 to 5) | Partly | Low | Covered partly by fix 13 |
| Packages distributed in ordinal sequence (Fig. 1, p. 3) | No | Low | Optional for Design bullet |
| Consumer studies: sweetpotato Ghana and Uganda, gari and eba in Nigeria and Cameroon (p. 12) | Partly | Low | Optional |
| Alternative business models, SeedLinked uses an approach inspired by tricot (p. 14) | No | Low | Optional |

## Template compliance

| Item | Result |
|---|---|
| Summary word count | 422 words. Within 400 to 500. The revised Summary below is 495 words |
| gist length | 13 words, under 30. But it lists topics rather than what the paper shows (see fix 20) |
| Keywords | 12. Within 8 to 12 |
| Questions | 7. Within 4 to 7. One question is not answered by the paper (fix 7) |
| House style | tricot is lowercase throughout, including at sentence start. No em dashes. Semicolons only in the not_established field and a relations comment, where the template uses them |
| id and file name | Match |
| curated_card | no, as expected before curation |

## Revised Summary, ready to paste (495 words)

The retrospective traces how tricot grew from a 2011 pilot into what the authors call the leading on-farm testing method in the CGIAR-NARES network. It frames the problem participatory breeding never solved, which is matching varieties to heterogeneous environments and users at scale, with valid and reliable data. Earlier approaches, from farmer-first trials to mother-and-baby designs, captured local relevance but struggled with scale, data robustness and representativeness.

tricot answers with crowdsourced citizen science. Each farmer tests a blind package of three options drawn from an A-optimal incomplete block design, which stays connected even when blocks are lost, and ranks them best and worst for each trait. ClimMob handles design, data management and reporting, field agents register farmers with Open Data Kit, and the Plackett-Luce model aggregates the rankings.

The proof-of-concept phase (2011–2015, India, Ethiopia, Central America) tested four questions. Farmers said they joined mainly to contribute to research and to exchange information with experts, and few expected money. In Honduras, aggregated farmer assessments showed adequate validity against breeders' evaluations, but individual reliability was low, so large samples are needed. As a rule of thumb, about 12 entries across about 150 farms can detect large effects. In one Rwanda case study over two seasons (Table 1 says potato, the text says maize), tricot cost about 27% less than RCBD per equivalent experimental unit. The paper also cites about 40% lower cost than RCBD in Central America and notes that costs are country specific. Adoption after tricot was comparable to group-based PVS but not higher. The authors ask whether product profiles fit farmer needs, or whether a non-preferred variety in the package discouraged adoption.

The data-driven phase built the statistics. Plackett-Luce models replaced pairwise rank-breaking, and covariates such as climate, genomic relatedness and item traits turned rankings into spatial recommendations, genetic estimates and preference models.

Mainstreaming in breeding followed. CIMMYT's maize network in Eastern and Southern Africa grew from under 50 to over 800 farms by 2022, with grain-yield heritability above 0.6 and better inclusion of women. A cowpea variety from IITA's tricot trials was released in Nigeria in 2022 with tricot data as on-farm evidence, and One Acre Fund used tricot to scale potato and maize varieties.

The authors are frank about obstacles. Breeding programmes and release authorities want absolute yields, not ranks, so teams are testing ways to combine rankings with yields measured on a subset of plots or by farmers. tricot also needs data-science capacity in NARES, reliable seed logistics, and a hands-off management style that accepts on-farm variation. The authors suggest that payment may crowd out farmers' intrinsic motivation and that local recognition may strengthen it, and they call for more research.

Recent work extends tricot to consumer testing and product concepts, including video-based maize concepts with 2,400 farmers in Kenya and Uganda, and to sampling designs that represent gender and socio-economic segments. The paper closes with six open issues, from financing and partnerships to GxExM interactions and how breeders act on results.
