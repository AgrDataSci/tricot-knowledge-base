# Card review: vanetten-2023-pnas

- **Card:** papers/vanetten-2023-pnas.md
- **Source:** papers-pdf/van-etten-et-al-2023.pdf (10 pages, printed page numbers match PDF pages)
- **Reviewed:** 2026-11-23, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 38 |
| Supported | 27 |
| Imprecise | 9 |
| Not in source | 0 |
| Contradicted | 2 |
| Source issues (problems in the source itself, not card errors) | 1 |
| Important omissions | 9 (3 high, 6 medium) |
| Metadata issues | 5 |

The card captures the overall argument, the two-axis framework and the five investment priorities well. But its first stated limitation gives a FIGS (genebank) limitation to 3D breeding and tricot, which is the opposite of what the paper says about tricot. The card also leaves out the tricot results that matter most to tricot users: the GxE findings from tricot trials, the genomic selection result, and the reliability metric. The most important fix is the stated limitation on p. 3.

## Fixes needed

1. **Stated limitation misattributed (Contradicted, p. 3).** Card: "3D breeding and environmental covariate approaches have so far focused on climate and adaptation traits, not the full complexity of crop use contexts." Source p. 3 says this of FIGS (Focused Identification of Germplasm Strategy), which links genebank accessions to agroclimatic data. On p. 6 the paper says tricot addresses both complexity and representativeness. Replace with:
   `- Genebank approaches that link accessions to agroclimatic data, such as FIGS, have so far focused on climate and adaptation traits, not the full complexity of crop use contexts.`

2. **Wrong year for Mengistu et al. in Notes (Contradicted, p. 3 and reference 29).** The source cites the durum wheat release as refs 10 and 29. Ref 29 is Mengistu, Kidane, Fadda and Pè, Plant Genetic Resources 16, 39 to 49, dated 2016 in the reference list, not 2018. Replace the note with:
   `- The Ethiopian durum wheat landrace releases are cited to van Etten et al. 2019 (ref. 10, see vanetten-2019-pnas) and Mengistu et al. 2016 (ref. 29). Ref. 29 is a study of phenotypic diversity, so check whether it documents the releases before citing it for them.`

3. **Main tricot results missing (high, p. 6, Fig. 2 on p. 3).** The summary does not say what tricot trials found or what the 3D breeding example showed. The sentence "tricot predicts farmers' overall appreciation" also drops the comparison and the source of the example. Fig. 2 says tricot "achieves better predictions" than the benchmark, based on ref. 58 (de Sousa et al. 2021). See the replacement summary below.

4. **Reliability metric missing and composite index overstated (p. 7 to 8).** Card: "Breeding progress metrics should become composite indices weighted by socio-economic data." Source p. 7 offers a composite index as "one way forward" and calls it relatively resource-intensive. On p. 8 it proposes a second option: stakeholders rank products by overall appreciation (citing tricot, ref. 80), and progress is measured as reliability, the probability of outperforming a check. The paper gives two limitations of reliability. See the replacement summary.

5. **Genebank sentence more certain than the source (p. 3).** Card: "most are poorly described ... duplication occurs". Source: the figure "could be overestimated", the majority of accessions "are not described", and duplication "may occur". See the replacement summary.

6. **Genomic success stories (p. 4).** Card (summary and limitations): "genomic success stories have mostly concerned traits controlled by few genes". Source p. 4 speaks of gene-based innovations (transgenesis or introgression) and says they are "limited to oligogenic traits". This is not about genomic selection, which the paper presents as a response to that complexity. Replace the limitation with:
   `- Gene-based innovations (transgenesis or introgression) have succeeded only for oligogenic traits, such as submergence tolerance and disease resistance.`

7. **Portfolios (p. 7).** Card: "so portfolios matter more than single best varieties". Source suggests that genebanks and breeders "could attempt" to offer a "menu" of complementary varieties. Use the wording in the replacement summary.

8. **Complexity axis definition (p. 2, Fig. 1).** Card: "how many traits and interactions are captured". Fig. 1 defines complexity as the degree to which methods address the crop use context, with biological, environmental and human aspects. Fixed in the replacement summary.

9. **Add not_established (missing).** Suggested text:
   `not_established: that data-driven or 3D breeding has already raised genetic gain across breeding programmes (the genomic selection result comes from one Ethiopian durum wheat study, ref. 58); that on-farm genomic selection is feasible at programme scale (named as a next step to assess); that composite indices are the agreed breeding metric (offered as one option); that the low-cost smartphone phenotyping tool exists (it is being designed); that the placement of methods in Fig. 1 is measured (it is the authors' judgment)`

10. **Add relations.** The paper cites three tricot cards in the knowledge base:
   ```
   relations:
     - discusses: desousa-2021-commsbio   # ref. 58, 3D breeding and genomic selection, Fig. 2
     - discusses: vanetten-2019-pnas      # ref. 10, tricot GxE results and durum wheat releases
     - discusses: vanetten-2019-expagric  # ref. 80, tricot approach
   ```

11. **Smaller frontmatter fixes.**
    - crops: `general (examples in durum wheat, bread wheat, common bean, rice, cassava, maize, tomato, vegetables)`
    - keywords: add `tricot` (gives 10 keywords). It is the term a tricot user would search for.
    - gist (replace "let", which is more certain than the source's "can"): `Perspective arguing that data-driven approaches, including tricot and 3D breeding, can help genebanks and breeders serve heterogeneous environments and users, and setting out five investment priorities` (27 words)

12. **Key numbers.** Add rows for numbers the paper gives (see Completeness). Suggested rows:

    | Number | Context | Primary source |
    |---|---|---|
    | 5 | Investment priorities proposed | This paper |
    | >5.7 million accessions in 831 genebanks | Worldwide genebank holdings, may be overestimated | FAO WIEWS, as cited in this paper (no date given) |
    | >42,000 seed kits, >183,000 vegetable seed samples | World Vegetable Center distribution to smallholders in Tanzania, Kenya and Uganda, 2013 to 2017 | Ref. 27, as cited in this paper |
    | >40,000 farmers | Seeds for Needs participants in Africa, Asia and Latin America | Fadda et al. 2020 (ref. 28), as cited in this paper |
    | Less than half | Share of studies that disaggregated adoption of climate-adapted varieties by sex | Weltzien et al. 2019 (ref. 85), as cited in this paper |

**Replacement summary (443 words, fixes 3 to 8).** It keeps the card's style and moves the genebank paragraph before the closing priorities so the structure follows the paper.

> The perspective argues that large datasets and computational methods are changing how crop diversity is managed in the Global South, across genebanks, breeding programmes and farmers, which the authors treat as one field. Cheaper genomic and phenotypic data, faster breeding cycles and intensive analytics allow information-rich management that can handle the interactions between crop diversity, production environments and socio-economic heterogeneity.
>
> The authors place data-generating approaches on two axes, complexity (how far biological, environmental and human aspects of the use context are captured) and representativeness (how well test conditions reflect real use contexts). Conventional breeding favored broad adaptation, focusing on mean response and reducing genotype-by-environment interaction. Ecological theory instead predicts that more, narrowly adapted varieties are more productive. Data-driven approaches, such as environmental covariates in trial analysis, crop models and data-driven decentralized breeding (3D breeding) with tricot on-farm testing, can raise both complexity and representativeness. Linked to environmental covariates, tricot trials showed how common bean responded to heat, Ethiopian durum wheat to cold and Indian bread wheat to rainfall and radiation. In the Ethiopian 3D breeding example, tricot gave better predictions of farmers' overall appreciation of varieties, and adding on-farm and environmental data greatly enhanced genomic selection.
>
> Other examples include Ethiopian farmers identifying superior durum wheat landraces that were released directly as varieties, and upland rice crop modelling in Brazil. The authors note that gene-based success stories are limited to traits controlled by few genes.
>
> On genebanks, FAO WIEWS lists more than 5.7 million accessions in 831 genebanks, but this may be overestimated because most accessions are not described, backlogs are common and duplication may occur. Missing accession data reduce the value of genebanks, which farmer evaluation of accessions could address.
>
> On end users, demand-led breeding must look beyond the household, since trait preferences differ between individual decision-makers, notably women and men, and female-headed households are only a small share of households. Farmers also combine varieties for different purposes and risks, so the authors suggest offering a "menu" of complementary varieties.
>
> On accountability, breeding progress must be quantified for public investors, but not only through outputs such as varieties released or seed sales. One option is a composite index weighted by socio-economic data, which is resource-intensive. Another is reliability, the probability that a variety outperforms a check, based on stakeholders ranking overall appreciation. Reliability is hard to compare across stakeholder groups and does not suit entirely new product categories.
>
> The paper closes with five priorities for investment. These are helping genebanks link with farmers through data, designing low-cost phenotyping, generating more and better gender and socio-economic data, designing information products for decisions, and building data-science capacity. Coordinated policy is needed to avoid fragmented capacities.

**Suggested additions to Stated limitations** (from the authors, p. 6 to 8):

```
- Analysis tools for GxE are new, sometimes immature, and rarely used together in breeding programmes.
- Empirical on-farm studies of GxExM interactions are still rare, and most analyses ignore management.
- Trait-preference studies are mostly reactive and focus on a single new variety rather than portfolios.
- Reliability against a check is hard to compare across stakeholder groups and does not suit new product categories.
- Drones and rovers will have limited use in public breeding in the Global South for the foreseeable future.
```

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Data-driven approaches can harness crop diversity to address heterogeneous needs for breeding products | Same (p. 1) | Supported |
| authors | van Etten J ... Tufan HA (16 names) | Same 16 authors, same order (p. 1). Layer 1 flags on Dell'Acqua and Solberg SØ are character-encoding flags only. | Supported |
| year | 2023 | Published March 27, 2023 (p. 1) | Supported |
| journal | Proceedings of the National Academy of Sciences | PNAS (p. 1 footer) | Supported |
| article | 120(14), e2205771120 | Vol. 120, No. 14, e2205771120 (p. 1) | Supported |
| type | perspective | "PERSPECTIVE" header (p. 1) | Supported |
| doi | https://doi.org/10.1073/pnas.2205771120 | Same (p. 1). Landing page not checked (no web access). | Supported |
| license | CC BY 4.0 | "Creative Commons Attribution License 4.0 (CC BY)" (p. 1) | Supported |
| data | none | "There are no data underlying this work" (p. 8) | Supported |
| crops | general (examples in durum wheat, rice, cassava, maize) | Also bread wheat and common bean (p. 6), tomato (p. 4), vegetables (p. 3) | Imprecise |
| region | Global South | Defined on p. 1 | Supported |
| gist | Perspective arguing that data-driven methods let genebanks and breeders serve ... | Source says "can" (p. 1). 20 words, says what the paper argues. | Imprecise (minor) |
| not_established | missing | Several claims are easy to stretch (see fix 9) | Missing |
| keywords | 9 terms, no "tricot" | tricot is central to Fig. 2 and p. 6 | Metadata issue |
| relations | missing | Refs 10, 58, 80 have cards | Metadata issue |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Frontmatter | title | Supported | p. 1 | |
| 2 | Frontmatter | authors | Supported | p. 1 | |
| 3 | Frontmatter | year 2023 | Supported | p. 1 | |
| 4 | Frontmatter | journal | Supported | p. 1 | |
| 5 | Frontmatter | article | Supported | p. 1 | |
| 6 | Frontmatter | type perspective | Supported | p. 1 | |
| 7 | Frontmatter | doi | Supported | p. 1 | Landing page not checked (no web access) |
| 8 | Frontmatter | license CC BY 4.0 | Supported | p. 1 | |
| 9 | Frontmatter | data none | Supported | p. 8 | |
| 10 | Frontmatter | crops list | Imprecise | p. 3, 4, 6 | Misses bean, bread wheat, tomato, vegetables |
| 11 | Frontmatter | region Global South | Supported | p. 1 | |
| 12 | Frontmatter | gist | Imprecise | p. 1 | "let" more certain than "can" |
| 13 | Summary | Large data and computation change crop diversity management, treated as one field | Supported | p. 1 | "single field of work" |
| 14 | Summary | Three drivers allow information-rich management of interactions | Supported | p. 1, abstract | |
| 15 | Summary | Two axes, complexity defined as traits and interactions captured | Imprecise | p. 2, Fig. 1 | Source defines complexity as biological, environmental and human aspects of the use context |
| 16 | Summary | Conventional breeding favored broad adaptation, mean response, reducing GxE | Supported | p. 2, p. 5 | |
| 17 | Summary | Ecological theory predicts more, narrowly adapted varieties are more productive | Supported | p. 5 | Ref. 69 |
| 18 | Summary | Env covariates, crop models, 3D breeding with tricot raise both axes | Supported | p. 5 to 6, Fig. 2 | |
| 19 | Summary | tricot predicts farmers' overall appreciation, a complex trait | Imprecise | Fig. 2 (p. 3) | Source: "better predictions" than a benchmark, in the ref. 58 example |
| 20 | Summary | Examples: durum wheat landraces, genomic crop history, unbalanced designs, upland rice in Brazil | Supported | p. 3, 4, 5 | |
| 21 | Summary | Genomic success stories mostly for traits controlled by few genes | Imprecise | p. 4 | Gene-based innovations, "limited to" oligogenic traits |
| 22 | Summary | Look beyond the household, women and men differ, FHH small share | Supported | p. 6 to 7 | Refs 88 to 91 |
| 23 | Summary | Portfolios matter more than single best varieties | Imprecise | p. 7 | Source: breeders "could attempt" a menu |
| 24 | Summary | Five investment priorities, listed | Supported | p. 1 abstract | |
| 25 | Summary | Metrics should become composite indices weighted by socio-economic data | Imprecise | p. 7 to 8 | "One way forward", resource-intensive. Reliability option omitted |
| 26 | Summary | Coordinated policy needed to avoid fragmentation | Supported | p. 1, p. 9 | |
| 27 | Summary | >5.7 million accessions in 831 genebanks, poorly described, backlogs, duplication occurs | Imprecise | p. 3 | Source: may be overestimated, "not described", duplication "may occur" |
| 28 | Summary | High benefit to cost, missing data reduce value and raise search costs, farmer characterization could help | Supported | p. 3 | Ref. 23 |
| 29 | Summary | Progress must be quantified, not only output metrics that suit private profit | Supported | p. 7 | Refs 99, 100. Source hedges with "perhaps" |
| 30 | Methods | Perspective without new data | Supported | p. 1, p. 8 | |
| 31 | Methods | Two-axis framework | Supported | p. 2, Fig. 1 | Placement is the authors' judgment (Fig. 1 caption) |
| 32 | Methods | Case examples from genebanks, tricot, crop modelling, gender | Supported | p. 3 to 7 | |
| 33 | Limitations | 3D breeding and env covariates focused on climate and adaptation traits | Contradicted | p. 3, p. 6 | Said of FIGS. tricot is said to address complexity |
| 34 | Limitations | Gender and socio-economic data scarce and household-based | Supported | p. 6 | |
| 35 | Limitations | Genomic successes mostly oligogenic | Imprecise | p. 4 | Gene-based innovations, "limited to" |
| 36 | Key numbers | 5 priorities, This paper | Supported | p. 1 | |
| 37 | Notes | Perspective with few numbers | Supported | whole paper | |
| 38 | Notes | Durum wheat releases documented in Mengistu et al. 2018 | Contradicted | p. 3, ref. 29 | Ref. 29 is dated 2016. Releases cited to refs 10 and 29 |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| The FAO WIEWS figure (5.7 million accessions, 831 genebanks) has no reference entry or date. The nearby ref. 22 is the FAO Second Report on plant genetic resources, which supports the hedge on overestimation. | p. 3 | No | `- The genebank figure is credited to FAO WIEWS without a date or reference entry. Ref. 22 (FAO Second Report) supports only the caveats on description, backlogs and duplication.` |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: opportunities and challenges of data-driven crop diversity management in the Global South | Yes | High | |
| Design: perspective, two-axis framework (Fig. 1), 3D breeding example (Fig. 2) | Partly (Fig. 2 not described) | Medium | Covered by replacement summary |
| tricot linked to env covariates: bean and heat, durum wheat and cold, Indian bread wheat and rainfall and radiation (ref. 10) | No | High | In replacement summary |
| Ethiopian on-farm data linked to genomic data greatly enhanced genomic selection (ref. 58). Next step: test on-farm genomic selection at programme scale | No | High | In replacement summary and not_established |
| Reliability (probability of beating a check) from stakeholder rankings of overall appreciation, and its two limitations | No | High | In replacement summary |
| Authors' limitations: immature tools, rare GxExM on-farm studies, reactive and single-variety trait studies, drones and rovers | Partly | Medium | Suggested limitation bullets |
| Data synthesis needs open data, data citation, standards | No | Medium | Optional Notes bullet |
| Seeds for Needs (>40,000 farmers) and World Vegetable Center seed kits | No | Medium | Key numbers rows |
| Nigeria cassava (gari) study: gender interacts with poverty and food insecurity, poor and food-insecure women prioritize quality traits more | No | Medium | `- A Nigerian study cited here (ref. 9) found that women in food-insecure households prioritized gari quality traits more.` (Notes) |
| Phenotyping: drone and rover limits, smartphone tool being designed (Project Artemis) | No | Medium | Covered in limitations and not_established |
| Why data-driven integration beats factorial experiments or process-based crop models alone (narrow funnel argument) | No | Low | Optional |
| Leadership and next generation of professionals need data-science skills, information design undervalued | Partly (capacity priority) | Low | |
| Links to related cards (refs 10, 58, 80) | No | Medium | relations block (fix 10) |

## Template compliance

- Summary word count: 403 (target 400 to 500). Pass. The replacement summary is 443 words.
- Gist length: 20 words (under 30). Pass. Suggested gist is 27 words.
- Keywords: 9 (8 to 12). Pass. Suggest adding tricot.
- Questions: 5 (4 to 7). Pass.
- House style: tricot lowercase throughout, maniva not used. Pass.
- not_established: missing. Should be added.
- Summary order: the genebank and accountability paragraph comes after "The paper closes with", which reads oddly. The replacement summary fixes the order.
