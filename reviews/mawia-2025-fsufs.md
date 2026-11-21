# Card review: mawia-2025-fsufs

- **Card:** papers/mawia-2025-fsufs.md
- **Source:** papers-pdf/mawia-et-al-2025.pdf (14 pages)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 64 |
| Supported | 53 |
| Imprecise | 10 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 11 |
| Important omissions | 2 |
| Metadata issues | 3 (gist, license, not_established could be stronger) |

The summary body is accurate and most numbers match the source exactly. The main problem is the gist. It says farmers "chose" the market leader (the 70% is stated purchase intention, p. 4), credits drought tolerance as a driver (not significant in the model, p. 10, and valued most by low-cost buyers, p. 8), and says "few tried alternatives when it was out of stock", which the paper never reports. The gist is also over 30 words. The card also leaves out the strongest regression result (planting the same variety last season, p. 10) and blurs the question-asking result. Printed page numbers match the PDF page numbers throughout.

## Fixes needed

1. **Gist (frontmatter).** The card says: "In a mock agro-dealer experiment with about 590 Kenyan farmers, 70% chose the decades-old market leader hybrid, driven by familiarity and drought tolerance, and few tried alternatives when it was out of stock" (33 words). The source says farmers were grouped by the variety they *planned* to buy (p. 4). Duma 43 is about 20 years old (Table 1, p. 4, released 2003 in Table S1, p. 14). Drought tolerance has no significant coefficient in the model (Table 6, p. 10), and it was named most often by low-cost buyers (90%, p. 6 and Figure 2, p. 8). The paper does not report what farmers chose when their variety was out of stock. It reports that they took longer and asked more questions (Table 5, p. 9). Replace with (29 words):

   `gist: In a mock seed store with 587 Kenyan farmers, 70% planned to buy one 20-year-old market leader hybrid, a choice linked to repeat planting, narrow experience and food traits`

2. **Summary, store behaviour and regression sentences.** The card says "with market leader buyers taking about 50 seconds longer. Few asked questions, and most ignored posters and price offers when their preferred variety was in stock. A multinomial logit model found that trait preferences, prior experience and farm size drove seed choice." Problems: (a) "50 seconds longer" is longer than the in-stock condition, not longer than other groups (Table 5, p. 9). (b) "Few asked questions" holds only when the variety was in stock (3%). When it was out of stock, 59% asked (66% of market leader buyers, Table 5, p. 9). (c) The poster and price-offer claim comes only from the abstract (p. 1). No result by treatment cell is reported. (d) "drove" is causal, but the authors call the design correlational (p. 10 to 11). Farm size was significant only for competitor versus low-cost buyers (Table 6, p. 10). (e) The largest coefficient, planting the same variety last season (2.31, p < 0.01, market leader only), is missing. Replace the whole paragraph that starts "In the store" with:

   `In the store, farmers chose in 34 seconds when their variety was in stock and 78 seconds when it was not. The out-of-stock delay was about 50 seconds for market leader buyers and 20 for competitor buyers. Only 3% asked questions when their variety was in stock, against 59% when it was not. The authors say most farmers ignored posters and price offers when their variety was available, but report no results by treatment. A multinomial logit model, with low-cost buyers as the base, linked market leader preference most strongly to planting the same variety last season, and positively to valuing food and harvest traits. Valuing early maturity and having bought more varieties before were linked to lower odds of market leader or competitor preference. Drought tolerance, gender and education were not significant.`

   To stay under 500 words (this brings the summary to about 496 words with fixes 3 and 4), also shorten the first paragraph. Replace "Harriet Mawia, John Mburu and Evans Chimoita at the University of Nairobi, with Pieter Rutsaert of CIMMYT, studied" with `Researchers at the University of Nairobi and CIMMYT studied`.

3. **Summary, land sentence.** The card says "Low-cost buyers farmed more land and sold more of their harvest." Total land under farming did not differ significantly (2.89 against 2.25 and 2.26 acres, p = 0.25, Table 3, p. 7). Land planned for maize (2.20 against 1.67 and 1.49 acres, p = 0.05) and share sold to traders (33.6% against 25.0% and 28.7%, p = 0.04) did. Replace with:

   `Low-cost buyers planned more land under maize and sold a larger share of their harvest.`

4. **Methods, Experiment bullet.** "six cells crossing stock availability with information poster and price offer" suggests a poster-by-price factorial. The design is 2 by 3: in stock or out of stock, crossed with control, information poster, or a 10% price promotion on two randomly chosen products (Table 2, p. 5). Replace with:

   `- **Experiment.** Mock agro-dealer store in each village with nine real hybrids at market prices (KES 500, or KES 400 for the two low-cost Kenya Seed Company hybrids, per 2 kg). Six cells crossed stock availability (preferred variety in stock or out of stock) with three conditions (control, technical information poster, or 10% price promotion on two random products). 293 farmers in the in-stock treatment and 294 out of stock.`

5. **Key numbers, Kenya Seed Company row.** The card credits this "Cited in this paper", but the source gives no reference for it (p. 3). The paper's Table 1 also lists the market leader Duma 43 as a Seed Co product, not Kenya Seed Company (p. 4). Replace the row with:

   `| ~70% | Kenya Seed Company's share of the maize seed market, stated without a reference. Table 1 lists the market leader Duma 43 as a Seed Co product | This paper (no source given) |`

6. **Key numbers, 40-70% row.** The source cites three papers, not two (p. 2). Replace the source cell with:

   `Odame and Muange 2011, Simtowe et al. 2019 and Simtowe et al. 2021, cited in this paper`

7. **not_established (frontmatter).** The current list is good but misses the stretches most likely for this card. Replace with:

   `not_established: that 70% of farmers bought the market leader in the store (the categories are stated purchase intentions); causal effects of experience or traits on seed choice (correlational design); that drought tolerance explains loyalty to the market leader (not significant in the model); effects of the information poster or price promotion (not reported by treatment); what farmers chose when their variety was out of stock; preferences beyond one semi-arid county`

8. **License (frontmatter).** The PDF says "Creative Commons Attribution License (CC BY)" with no version number (p. 1). Replace with:

   `license: CC BY (version not stated in the PDF)`

9. **Notes, add source issues.** Add these bullets:

   `- Category shares differ across the paper: abstract 70/21/7 (sums to 98), Table 1 69.7/22.4/7.1, and the treatment counts 417/128/42 of 587, which give 71.0/21.8/7.2 (card's calculation).`
   `- Price attitude: the text says 67% saw price as important and 33% not, but Table 4 gives 62.9% (22.4 + 40.5) and 36.0%. Low-cost buyers were the least price-focused (68% said price is not important).`
   `- The discussion says low-cost buyers had less education and market leader buyers valued yield potential, but Table 3 shows no significant education differences and Table 6 shows no significant yield coefficient for the market leader.`
   `- The variety lists do not match: PHB 3253 is called excluded on p. 4 but is a competitor in Table 1. Table 1 has P2809W, which is missing from Table S1. Variety ages in Table 1 do not always match the release years in Table S1.`

10. **Methods, Analysis bullet (small).** The tables use one-way ANOVA, which the bullet leaves out (p. 4, Tables 3 to 5). Replace with:

   `- **Analysis.** Chi-square tests, t-tests and one-way ANOVA across the three groups. Multinomial logit with low-cost buyers as base category (pseudo R² 0.25, n = 587, Hausman test for IIA).`

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | "...Kenya. The dominance of market leader varieties" | Colon in original (p. 1). Expected house change | Supported |
| authors | Mawia H, Mburu J, Chimoita E, Rutsaert P | Same four authors (p. 1) | Supported |
| year | 2025 | Published 6 August 2025 (p. 1) | Supported |
| journal | Frontiers in Sustainable Food Systems | Same (p. 1) | Supported |
| article | 9, 1563538 | Front. Sustain. Food Syst. 9:1563538 (p. 1) | Supported |
| type | research article | "Original Research" (p. 1) | Supported |
| doi | https://doi.org/10.3389/fsufs.2025.1563538 | Same (p. 1) | Supported |
| license | CC BY 4.0 | "CC BY", no version given (p. 1) | Imprecise (fix 8) |
| data | in the article and supplementary material, inquiries to corresponding author | Data availability statement (p. 11) | Supported |
| crops | maize | Maize only | Supported |
| region | Kenya (Machakos County, semi-arid) | Machakos County, semi-arid (p. 3) | Supported |
| gist | see fix 1 | p. 4, 8, 9, 10 | Imprecise and Not in source, and 33 words (fix 1) |
| not_established | three items | Supported as far as it goes (p. 10 to 11) | Supported, but misses key stretches (fix 7) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Market competitive, old varieties dominate, slow turnover as climate stress grows | Supported | Abstract and intro (p. 1 to 2) | |
| 2 | Summary | Authors at University of Nairobi and CIMMYT | Supported | Affiliations (p. 1) | |
| 3 | Summary | Studied why semi-arid Machakos farmers stay loyal to market leaders | Supported | p. 1, 3 | |
| 4 | Summary | 20 villages randomly selected in three sub-counties | Supported | p. 3 | 3 of 8 sub-counties, stratified |
| 5 | Summary | Up to 32 eligible farmers per village, criteria, equal gender target | Supported | p. 3 | Men had more no-shows (omitted) |
| 6 | Summary | Mock store in each village with real hybrids suited to the zone | Supported | p. 3 to 4 | Nine hybrids, dry mid-altitude zone |
| 7 | Summary | Six cells, random, half in stock, half preferred variety out of stock | Supported | p. 4, Table 2 p. 5 | |
| 8 | Summary | Some cells added poster or price offer | Supported | Table 2 (p. 5) | Promotion is 10% on two random products |
| 9 | Summary | Surveys and focus groups on motivations and risk | Supported | p. 4 | |
| 10 | Summary | Market leader Duma 43, released 2003 | Supported | p. 4, Table S1 (p. 14) | |
| 11 | Summary | Competitors include Sungura 301, Bayer and Pioneer hybrids | Supported | p. 4, Table 1 | |
| 12 | Summary | Low-cost priced 20% lower | Supported | KES 400 vs 500 (p. 4) | 400/500 = 0.80, checked |
| 13 | Summary | 70% / 21% / 7% preferred each category | Supported | Abstract (p. 1) | See source issue 1 |
| 14 | Summary | Drought 72%, yield 70%, consumption 57%, grain 55% | Supported | p. 6 | |
| 15 | Summary | Group trait emphases, low-cost drought 90%, early maturity 64% | Supported | p. 6, Figure 2 (p. 8) | Figure values approximate |
| 16 | Summary | Low-cost buyers farmed more land and sold more harvest | Imprecise | Table 3 (p. 7) | Total land p = 0.25. Fix 3 |
| 17 | Summary | One third grew only one variety in past two years | Supported | p. 7, Table 4 (p. 8) | 33.2% |
| 18 | Summary | 2.5 vs 3.2 vs 3.5 varieties | Supported | Table 4 (p. 8) | |
| 19 | Summary | About two thirds said price mattered | Supported | p. 7 | Text 67%, table 62.9%. Source issue 2 |
| 20 | Summary | More saw price as quality than affordability signal | Supported | p. 7, Table 4 | 40% vs 22% |
| 21 | Summary | 34 s in stock, 78 s out of stock | Supported | p. 7, Table 5 (p. 9) | Table gives 34.95 s |
| 22 | Summary | Market leader buyers took about 50 s longer | Imprecise | Table 5 (p. 9) | Longer than in-stock, vs 20 s for competitors. Fix 2 |
| 23 | Summary | Few asked questions | Imprecise | Table 5 (p. 9) | 3% in stock, 59% out of stock. Fix 2 |
| 24 | Summary | Most ignored posters and price offers when in stock | Supported | Abstract (p. 1) | No treatment results shown. Source issue 8 |
| 25 | Summary | MNL: traits, experience and farm size drove choice | Imprecise | Abstract (p. 1), Table 6 (p. 10), p. 10 to 11 | Causal wording, farm size only for competitors. Fix 2 |
| 26 | Summary | Loyalty rests on brand familiarity, past performance, agronomic traits | Supported | Conclusion (p. 10) | |
| 27 | Summary | Breeding must go beyond performance | Supported | p. 10 | |
| 28 | Summary | Demo plots, field days, early adopter testimonials | Supported | p. 10 | |
| 29 | Summary | Regulation could set phase-out timelines | Supported | p. 10 | Source says "should also mandate" |
| 30 | Methods | Multistage, 3 of 8, 20 villages, up to 32, 50/50 target | Supported | p. 3 | |
| 31 | Methods | Fieldwork Feb to Mar 2021, follow-up Apr to May 2023 | Supported | p. 3 | Follow-up content not described. Source issue 9 |
| 32 | Methods | Real hybrids and prices | Supported | p. 3 to 4, Table 1 | |
| 33 | Methods | Six cells crossing availability with poster and price offer | Imprecise | Table 2 (p. 5) | 2 by 3 design. Fix 4 |
| 34 | Methods | 293 in stock, 294 out of stock | Supported | p. 4 | 210+60+23 = 293, 207+68+19 = 294, checked |
| 35 | Methods | Survey, focus groups, selection time, questions | Supported | p. 4, 7 | Also attention scale |
| 36 | Methods | Chi-square, t-tests, MNL with low-cost base | Supported | p. 4, 7 | ANOVA omitted. Fix 10 |
| 37 | Limitations | Correlational design, need experimental or longitudinal | Supported | p. 10 to 11 | |
| 38 | Limitations | Recall bias, short recall period | Supported | p. 7 | |
| 39 | Limitations | Gender, extension, social networks need study | Supported | p. 11 | |
| 40 | Key numbers | 293 / 294 | Supported | p. 4 | |
| 41 | Key numbers | 70 / 21 / 7% | Supported | p. 1 | |
| 42 | Key numbers | 72 / 70 / 57 / 55% | Supported | p. 6 | |
| 43 | Key numbers | 2.51 / 3.21 / 3.50 | Supported | Table 4 (p. 8) | |
| 44 | Key numbers | 34 s vs 78 s | Supported | p. 7 | |
| 45 | Key numbers | 2003 release of Duma 43 | Supported | Table S1 (p. 14) | |
| 46 | Key numbers | ~70% Kenya Seed Company share, cited | Imprecise | p. 3, Table 1 (p. 4) | No reference given. Fix 5 |
| 47 | Key numbers | 40-70% adoption, two sources | Imprecise | p. 2 | Third source missing. Fix 6 |
| 48 | Notes | Counts 210/207, 60/68, 23/19 give slightly different shares | Supported | p. 4 | Recomputed 71.0 / 21.8 / 7.2% |
| 49 | Gist | Mock store experiment with about 590 farmers | Supported | n = 587 (p. 4, Table 3) | |
| 50 | Gist | 70% chose the decades-old market leader | Imprecise | p. 4, Table 1 | Stated intention, about 20 years old. Fix 1 |
| 51 | Gist | Driven by familiarity and drought tolerance | Imprecise | Table 6 (p. 10), Figure 2 (p. 8), p. 10 | Drought tolerance not significant. Fix 1 |
| 52 | Gist | Few tried alternatives when out of stock | Not in source | Table 5 (p. 9) | Choices under stockout not reported. Fix 1 |
| 53 to 64 | Metadata | Remaining 12 frontmatter fields | 11 Supported, 1 Imprecise | See metadata table | License imprecise |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| 1. Three versions of the category shares: abstract 70/21/7 (sums to 98), Table 1 69.7/22.4/7.1, counts give 71.0/21.8/7.2 | p. 1, 4 | Partly (counts vs abstract, not Table 1) | See fix 9, first bullet |
| 2. Price attitude: text 67% important and 33% not, Table 4 62.9% and 36.0% | p. 7, 8 | No | See fix 9, second bullet |
| 3. In-stock selection time: text 34 s, Table 5 34.95 s | p. 7, 9 | No | Low importance, no note needed |
| 4. PHB 3253 said to be excluded as not preferred, but listed as a competitor with 4.0% preference | p. 4, Table 1 | No | See fix 9, fourth bullet |
| 5. Variety lists and ages disagree: P2809W in Table 1 but not Table S1, SAWA and WH101 only in Table S1, WE1101 in the text. Duma 43 and DK8031 both released 2003 but aged 20 and 21. DH02 released 1995 but aged 29 | p. 2, 4, 14 | No | See fix 9, fourth bullet |
| 6. About 70% market share given to Kenya Seed Company without a reference, while Table 1 lists Duma 43 as Seed Co. Possible conflation with the 69.7% sample preference | p. 3, 4 | No | Covered by fix 5 |
| 7. Discussion claims not backed by results: lower education of low-cost buyers (Table 3 p ≥ 0.22), yield valued by market leader buyers (coefficient 0.125, n.s.), income diversification of market leader buyers (other income 38.2% vs 38.3%) | p. 9 vs p. 7, 10 | No | See fix 9, third bullet |
| 8. Abstract says farmers ignored posters and price offers, but no result by treatment cell is reported | p. 1 vs p. 7 to 10 | No (card repeats the claim) | Covered by fix 2 and fix 7 |
| 9. The 2023 follow-up is mentioned but never described. It is unclear which data come from which round | p. 3 | No | `- A follow-up with the same farmers in 2023 is mentioned but not described.` |
| 10. Table typos: low-cost age SD equals the mean (47.38). Early maturity for market leader (−1.702, SE 0.413, z about 4.1) is marked ** instead of ***. Equation 8 has a term with no variable | p. 5, 7, 10 | No | Low importance, no note needed |
| 11. Simtowe et al. 2019, cited for Kenyan adoption rates, is a Uganda study in the reference list | p. 2, 13 | No | `- Simtowe et al. 2019, cited for the 40-70% Kenyan adoption range, is a Uganda study.` |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: drivers of seed choice (traits, experience, behaviour, profiles) | Yes | High | |
| Design: mock store, 2 by 3 cells, stated intention as grouping variable | Partly (intention not stated) | High | Fix 1 and fix 7 |
| Sample size 587, 293 / 294 split | Yes | High | |
| MNL results: same variety last season (2.31, market leader only), past varieties bought negative, early maturity negative, harvest traits positive, age positive, drought, gender and education n.s., pseudo R² 0.25 | Partly | High | Fix 2 and fix 10 |
| Questions asked: 3% in stock vs 59% out of stock (66% market leader) | No | Medium | Fix 2 |
| Over 40% of market leader buyers had grown only that variety | No | Medium | Add to Experience paragraph: `Over 40% of market leader buyers had grown only that one variety.` (p. 7, Table 4) |
| Low-cost buyers least price-focused (68% price not important) | No | Medium | Fix 9, second bullet |
| No significant sociodemographic differences between groups | No | Medium | Optional summary sentence: `The three groups did not differ in age, gender or education.` (Table 3, p. 7) |
| Women made up 57% of participants because more men did not show up | No | Medium | Add to Sampling bullet: `Men had more no-shows, so 57% of participants were women.` (p. 3, Table 3) |
| Low-cost hybrids are DH02 and DH04 of parastatal Kenya Seed Company, priced at 2.5 times grain price | Partly | Low | Fix 4 |
| Attention scale (1 to 5) rose from 2.6 to 3.7 when out of stock | No | Low | None needed |
| Other recommendations: subsidies, targeted promotions, performance guarantees, regular performance assessments | Partly | Low | None needed |
| Theory of Planned Behavior framing | No | Low | None needed |
| Authors' limitations (correlational, recall, gender and networks) | Yes | High | |
| Conclusions | Yes | High | |

## Template compliance

- Summary word count: 430 (within 400 to 500). With fixes 2 and 3 and the shortened author sentence it is about 496.
- Gist: 33 words, over the 30-word limit. Fix 1 gives 29 words.
- Keywords: 11 (within 8 to 12).
- Questions: 5 (within 4 to 7).
- House style: no tricot or maniva casing problems. The Notes mention of tricot is clearly the card's own pointer, which is fine.
