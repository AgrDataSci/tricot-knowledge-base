# Card review: daudi-2026-fes

- **Card:** papers/daudi-2026-fes.md
- **Source:** papers-pdf/daudi-et-al-2026.pdf (15 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 44 |
| Supported | 31 |
| Imprecise | 9 |
| Not in source | 2 |
| Contradicted | 2 |
| Source issues (problems in the source itself, not card errors) | 12 |
| Important omissions | 2 |
| Metadata issues | 3 |

The card describes the design and sample sizes correctly. It follows the abstract closely, but the abstract disagrees with the paper's own Table 4 and Figure 5 on two main results, and the card repeats the abstract without a flag. The most serious problem: the card says ICGV-SM 05534 had the highest kernel yield (about 927 kg/ha), but in the next sentence it gives ICGV-SM 16645 a higher yield (about 936 kg/ha). Table 4 (p. 7) and Section 3.4 (p. 9) both make ICGV-SM 16645 the top yielder. The gender sentence also overstates the differences between women and men. Both stated limitations are not in the source, and the authors' own limitations are missing. not_established is missing.

**Pre-check flag (878 kg/ha).** This number is correct. The abstract gives 877.67 kg/ha (p. 1) and Table 4 gives 877.669 kg/ha in the "Overall" column for ICGV-SM 10014 (p. 7). I checked the table on the PDF page image. 878 is the rounded value. The automated check missed it only because of rounding.

## Fixes needed

1. **Top yielder (Contradicted).** The card says: "ICGV-SM 05534 gave the highest mean kernel yield, about 927 kg/ha. A GGE biplot identified ICGV-SM 16645 and ICGV-SM 10014 as the most stable genotypes, with mean yields of about 936 and 878 kg/ha." Only the abstract (p. 1) supports the first sentence. In Table 4 (p. 7), ICGV-SM 16645 has 936.393 kg/ha and ICGV-SM 05534 has 927.232 kg/ha. Section 3.4 (p. 9) calls ICGV-SM 16645 the highest yielder. The GGE result in the paper is "closest to the ideal genotype" (mean plus stability, pp. 9, 13), not only stability. Replace with:

   > Mean kernel yield across environments was about 832 kg/ha. In Table 4, ICGV-SM 16645 had the highest mean kernel yield, about 936 kg/ha, followed by ICGV-SM 05534 at about 927 kg/ha, although the abstract names ICGV-SM 05534 as the top yielder. In the GGE biplot, ICGV-SM 16645 and ICGV-SM 10014 (about 878 kg/ha) were closest to the ideal genotype, combining high mean yield with stability.

   Key numbers. Replace the two yield rows with:

   ```
   | ~832 kg/ha | Mean kernel yield across 16 genotypes and 18 environments (Table 3, Table 4) | This paper |
   | ~936 / ~878 kg/ha | Mean kernel yield of ICGV-SM 16645 / ICGV-SM 10014, the two genotypes closest to the ideal genotype in the GGE biplot. ICGV-SM 16645 is also the top yielder in Table 4 | This paper |
   | ~927 kg/ha | Mean kernel yield of ICGV-SM 05534, second highest in Table 4 (the abstract calls it the highest) | This paper |
   | 73.7% | Broad-sense heritability of kernel yield across the 18 environments (Table 3) | This paper |
   ```

2. **Gender preferences (Imprecise, high importance).** The card says: "Women valued early maturity, ease of harvesting and ease of shelling most, while men valued haulm yield." This follows the abstract (p. 1). But Figure 5 (p. 11) and the results text (pp. 9 to 10) show that marketability, kernel color and kernel size are the traits most closely linked to overall preference for both men and women (Kendall correlation about 0.7 to 0.8, read from the chart). Early maturity, harvest labor and shelling are mid- to low-ranked for women (about 0.35 to 0.40) and rank only higher than for men. Haulm yield is weak for men (about 0.3, read from the chart). Replace with:

   > For both women and men, marketability, kernel color and kernel size were the traits most closely linked to overall preference (Kendall correlation, 549 men and 654 women). Women gave more weight than men to early maturity, ease of harvesting and ease of shelling. The abstract says men preferred haulm yield, but in the figure haulm yield is only weakly linked to men's overall preference.

3. **Stated limitations (Not in source, both bullets).** The source does not say that low absolute yields are a limitation, and it does not say that the varying farmer numbers are one. Replace the section with the authors' own limitations:

   ```
   - The breakdown of farmer preferences by agro-ecological zone ignores possible segmentation of preferences within zones (p. 10).
   - More years of data are needed to understand which test locations in Tanzania give the same results and could be dropped (p. 13).
   - Farmer preferences need further segmentation, including young men and young women (p. 13).
   - The pathway from on-farm data to faster adoption and food security is diffuse (p. 13).
   ```

4. **not_established missing.** Add to the frontmatter:

   ```
   not_established: that station kernel yields and tricot rankings were analysed jointly or agree with each other (they were analysed separately); that ICGV-SM 05534 is the top-yielding genotype (Table 4 shows ICGV-SM 16645 higher); that any genotype was released on the basis of these results; that the gender differences were tested statistically (they are descriptive correlations); that women and men differ on the top traits (both rank marketability, kernel color and kernel size highest); that the four mega-environments hold over more than two seasons; that young farmers' preferences were assessed
   ```

5. **Methods, preference analysis (Imprecise).** The card says: "Plackett-Luce models of trait and overall rankings by gender." The gender analysis uses Kendall correlation between each trait and overall preference (p. 6, Figure 5). Plackett-Luce log-worth is used by agro-ecological zone (Figure 6), with the local check as reference (p. 6). No Plackett-Luce model by gender is reported. Replace with:

   > - **Preference analysis.** Plackett-Luce models (log-worth, local check as reference) of trait and overall rankings by agro-ecological zone, and Kendall correlation between each trait and overall preference, separately for men and women.

6. **Notes (Imprecise) and missing source flags.** The note mixes the decimals of the abstract and the table, and the card flags none of the source inconsistencies. Replace the Notes section with:

   ```
   - The abstract gives 927.232, 936.39 and 877.67 kg/ha. Table 4 (p. 7) gives 927.232, 936.393 and 877.669 kg/ha. Round when citing.
   - Source inconsistency on the top yielder. The abstract calls ICGV-SM 05534 (927 kg/ha) the highest-yielding genotype. Table 4 (p. 7) shows ICGV-SM 16645 higher, at 936 kg/ha, and Section 3.4 (p. 9) calls ICGV-SM 16645 the highest yielder. Section 3.3 (p. 6) attaches 936.393 to ICGV-SM 16530 and 927.232 to ICGV-SM 03707, which does not match Table 4 (761 and 882 kg/ha). Its list of the five lowest genotypes also does not match Table 4. This card follows Table 4.
   - Source inconsistency on gender traits. The abstract says early maturity, ease of harvesting and shelling were the traits women preferred most, and haulm yield the trait men preferred. Figure 5 (p. 11) shows marketability, kernel color and kernel size at the top for both, with haulm yield weak for men.
   - Genotype names. The text names ICGV-SM 16445 (pp. 9, 13), and Figures 6 and 7 show ICGV-SM 16630. Neither is in Table 1. They are probably ICGV-SM 16645 and ICGV-SM 16530. Figures 6 and 7 show 14 of the 16 station genotypes plus the local check (ICGV-SM 05702 and ICGV-SM 16519 are absent), although Methods says all 16 were used on-farm (p. 4).
   - Table 3 (p. 6) gives identical values for Environment and Block (replication), which looks like a copy error.
   - The mega-environment text counts fourteen plus five environments (19), but 18 were tested (p. 13).
   - Figure 6 panel sizes add up to 1,777 (our calculation), while 1,203 farmers took part (Figure 5, p. 11, and Methods, p. 4). The panels may count observations, not farmers.
   ```

7. **Summary, mega-environments (Imprecise, minor).** The card says the mega-environments "can guide targeted testing and release". The conclusion (p. 13) says they are useful for targeted evaluation, breeding and seed production, and the text says "at least four" (p. 13). Replace with:

   > The GGE analysis suggested at least four mega-environments, which the authors see as useful for targeted evaluation of genotypes, breeding and seed production.

8. **Summary, tricot validation (Imprecise, minor).** "an established way" is stronger than the source, which says such rankings have been shown to be useful (p. 13). Replace with:

   > They also note that rankings aggregated from many farmers have been shown to distinguish technology performance, citing earlier tricot validation work.

9. **Summary, last sentence (Imprecise, minor).** In the abstract, "vital" refers to the selected genotypes, test environments and preferred traits (p. 1), not to the approach. Paragraph 5 already says this. Also, the paper does not combine the two data sets in one analysis. Replace with:

   > The study thus runs conventional stability analysis and farmer evaluation side by side to inform release decisions, although it analyses the two data sets separately.

   With fixes 1, 2 and 7 to 9, the summary is about 481 words (checked), still within 400 to 500.

10. **Methods, station and on-farm bullets (completeness, medium).** Replace with:

    > - **Station trials.** 16 genotypes (14 ICRISAT elite lines and 2 released TARI checks, Mangaka 2009 and Mnanje 2009), randomized complete block design with four replications, nine locations in 2022 and 2023 (18 environments), covering six of seven agroecological zones.
    > - **On-farm trials.** tricot under natural rainfall and farmer management, 42 locations in 36 villages of 10 regions, with 154, 178 and 871 farmers in 2021, 2022 and 2023. Each farmer received three varieties, assigned with ClimMob, and a local check was added. Farmers ranked traits from the groundnut target product profile (for example yield, kernel color, maturity, harvest labor). Data were collected with ODK. The gender analysis used 549 men and 654 women.

11. **Frontmatter (Imprecise, minor).**
    - `article: 15(2), e70228`
    - `data: Not public. Available from the corresponding author on reasonable request (Data Availability Statement, p. 14). No code repository given.`
    - Optional: `software:` add ClimMobTools, which the source also names (p. 6).
    - Optional gist, because women and men share their top traits: `gist: Across 18 Tanzanian environments, ICGV-SM 16645 and 10014 were high-yielding and stable, and tricot farmers of both genders favored marketable tan small-medium kernels, with women valuing labor-saving traits more` (29 words).

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Analysis of genotype-by-environment interaction, ... triadic comparison of technologies | Same title, title case (p. 1) | Supported |
| authors | Daudi H, Bujiku AM, ... Shimelis H (11) | Same 11 authors, same order (p. 1) | Supported |
| year | 2026 | 2026 (p. 1) | Supported |
| journal | Food and Energy Security | Food and Energy Security (p. 1) | Supported |
| article | e70228 | 2026, 15:e70228, issue 2 (p. 1, download footer) | Imprecise (add volume and issue: 15(2), e70228) |
| type | research article | "Original article" (p. 1) | Supported |
| doi | https://doi.org/10.1002/fes3.70228 | Same (p. 1) | Supported |
| license | CC BY | Creative Commons Attribution License, open access (p. 1) | Supported |
| data | see the data availability statement in the article | Data available from the corresponding author on reasonable request (p. 14) | Imprecise (say what the statement says) |
| crops | groundnut | Groundnut (p. 1) | Supported |
| region | Tanzania | Tanzania (p. 1) | Supported |
| gist | Combines station and tricot trials ... women and men prioritize different traits | Abstract (p. 1) and Figure 5 (p. 11). Both genders share the top traits and differ on mid-ranked traits | Imprecise (minor) |
| not_established | missing | | Missing, see fix 4 |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Breeding needs yield and preferred traits, but yield and selection depend on GEI and management | Supported | Abstract (p. 1) | |
| 2 | Summary | Aim: assess GEI and preferences together to select genotypes and guide breeding with gender | Supported | Abstract (p. 1), Introduction (p. 2) | |
| 3 | Summary | 16 genotypes incl. 2 commercial checks, RCBD, 18 environments representing AEZs | Supported | Abstract (p. 1), Section 2.1 (p. 2) | Nine locations by two seasons, four replications, six of seven AEZs (p. 2) |
| 4 | Summary | tricot in 42 locations, 154 / 178 / 871 farmers in 2021 to 2023, 36 villages, 10 regions | Supported | Abstract (p. 1), Section 2.3 (p. 4) | Methods says tricot ran 2021 to 2024 (p. 4) |
| 5 | Summary | G, E and GEI all significant for kernel yield | Supported | Abstract (p. 1), Table 3 (p. 6) | G is p < 0.01 in Table 3, text says p < 0.001 |
| 6 | Summary | ICGV-SM 05534 had the highest mean kernel yield, about 927 kg/ha | Contradicted | Abstract (p. 1) only. Table 4 (p. 7): 16645 has 936.393. Section 3.4 (p. 9) | See fix 1. Card contradicts itself in the next sentence |
| 7 | Summary | GGE: ICGV-SM 16645 and 10014 most stable, about 936 and 878 kg/ha | Supported | Abstract (p. 1), Table 4 (p. 7): 936.393, 877.669 | Body text says closest to ideal genotype (pp. 9, 13), so fix 1 rewords |
| 8 | Summary | tricot analysis revealed gender differences | Supported | Abstract (p. 1), Section 3.7 (pp. 9 to 10) | Descriptive, not tested |
| 9 | Summary | Women valued early maturity, harvesting, shelling most, men haulm yield | Imprecise | Abstract (p. 1). Figure 5 (p. 11), text (pp. 9 to 10) | Top traits are shared. See fix 2 |
| 10 | Summary | Tan color and small to medium kernels drove overall preference, maturity matters for market segment | Supported | Abstract (p. 1), Conclusions (p. 13) | |
| 11 | Summary | Conclusion: preferences in TPP design stage, genotypes, environments, traits guide pipelines and release | Supported | Abstract (p. 1) | |
| 12 | Summary | Four mega-environments, guide targeted testing and release | Imprecise | Discussion and Conclusions (p. 13) | "At least four", and the use named is evaluation, breeding and seed production. Fix 7 |
| 13 | Summary | Convergence on marketability, size, color shows breeders must prioritise market phenotypes | Supported | Discussion (p. 13) | |
| 14 | Summary | Color and seed size not consistently priority traits in breeding | Supported | Discussion (p. 13) | |
| 15 | Summary | Build them into TPP from start, as CIMMYT Eastern and Southern Africa programme has begun | Supported | Discussion (p. 13) | |
| 16 | Summary | Divergence on labor and oil content, tailor pipelines, raise adoption and turnover | Supported | Discussion (p. 13) | |
| 17 | Summary | Aggregated rankings are an established way to distinguish performance | Imprecise | Discussion (p. 13), citing Steinke 2017 and Van Etten 2019 | Slightly stronger than the source. Fix 8 |
| 18 | Summary | Study combines stability analysis and farmer evaluation, approach presented as vital | Imprecise | Abstract (p. 1) | "Vital" refers to genotypes, environments and traits. The two analyses are separate. Fix 9 |
| 19 | Methods | Station: 16 genotypes, 2 checks, RCBD, 18 environments | Supported | Section 2.1 (p. 2) | Add detail, fix 10 |
| 20 | Methods | Combined ANOVA and GGE biplot for stability and mega-environments | Supported | Sections 2.5.1, 3.2 to 3.5 (pp. 5 to 10), Table 3 | Mixed model with random effects |
| 21 | Methods | tricot in 42 locations, 36 villages, 10 regions, 2021 to 2023, sex-disaggregated | Supported | Abstract (p. 1), Section 2.3 (p. 4), Figure 5 (p. 11) | |
| 22 | Methods | Plackett-Luce models of trait and overall rankings by gender | Imprecise | Section 2.5.2 (p. 6), Figures 5 and 6 (p. 11) | PL is by zone, gender uses Kendall correlation. Fix 5 |
| 23 | Limitations | Yields low in absolute terms, low-input conditions | Not in source | | Fix 3 |
| 24 | Limitations | On-farm trial numbers varied widely between years | Not in source | Numbers on p. 4, not stated as a limitation | Fix 3 |
| 25 | Key numbers | 16 genotypes (2 checks) | Supported | p. 1, Table 1 (p. 3) | |
| 26 | Key numbers | 18 environments | Supported | p. 1, p. 2, p. 5 | |
| 27 | Key numbers | 42 locations | Supported | Abstract (p. 1) | |
| 28 | Key numbers | 154 / 178 / 871 farmers | Supported | Section 2.3 (p. 4) | Sum 1,203 matches 549 men + 654 women in Figure 5 (our calculation) |
| 29 | Key numbers | 36 villages, 10 regions | Supported | Section 2.3 (p. 4) | |
| 30 | Key numbers | ~927 kg/ha, highest mean kernel yield, ICGV-SM 05534 | Contradicted | Table 4 (p. 7) | 927 is correct for ICGV-SM 05534 but it is second highest. Fix 1 |
| 31 | Key numbers | ~936 / ~878 kg/ha, most stable genotypes | Supported | Abstract (p. 1), Table 4 (p. 7): 936.393, 877.669 | Pre-check flag on 878 is a rounding effect |
| 32 | Notes | PDF gives 927.232, 936.39, 877.67 to three decimals | Imprecise | Abstract (p. 1) mixes two and three decimals. Table 4 (p. 7) gives 936.393, 877.669 | Fix 6 |
| 33 | Frontmatter | title | Supported | p. 1 | |
| 34 | Frontmatter | authors | Supported | p. 1 | |
| 35 | Frontmatter | year | Supported | p. 1 | |
| 36 | Frontmatter | journal | Supported | p. 1 | |
| 37 | Frontmatter | article | Imprecise | p. 1 | Add 15(2) |
| 38 | Frontmatter | type | Supported | p. 1 | |
| 39 | Frontmatter | doi | Supported | p. 1 | |
| 40 | Frontmatter | license | Supported | p. 1 | |
| 41 | Frontmatter | data | Imprecise | p. 14 | Fix 11 |
| 42 | Frontmatter | crops | Supported | p. 1 | |
| 43 | Frontmatter | region | Supported | p. 1 | |
| 44 | Frontmatter | gist | Imprecise | p. 1, Figure 5 (p. 11) | Minor. Optional replacement in fix 11 |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Top yielder differs. The abstract names ICGV-SM 05534 (927.232). Table 4 has ICGV-SM 16645 at 936.393. Section 3.3 gives 936.393 to ICGV-SM 16530 and 927.232 to ICGV-SM 03707 (Table 4: 761.320 and 882.423) | p. 1, p. 6, Table 4 p. 7, p. 9 | No | See fix 6, second bullet |
| The bottom-five list in Section 3.3 does not match Table 4. It gives 775.130 to ICGV-SM 16514 (Table 4: ICGV-SM 16519) and lists ICGIL 17105 (815.6) instead of ICGV-SM 16530 (761.3) | p. 6, p. 7 | No | Included in fix 6, second bullet |
| The abstract says women preferred early maturity, harvesting and shelling most, and men haulm yield. Figure 5 shows marketability, color and size on top for both | p. 1, p. 11 | No | See fix 6, third bullet |
| The text says women ranked oil content (r about 0.5) slightly above yield, but Figure 5 shows yield above oil for women (about 0.53 versus 0.46, read from the chart). The caption says bars are in descending order, but they are not. The text calls the same figure both Pearson and Kendall | pp. 9 to 11 | No | Low importance, no Notes text needed |
| Table 3 gives identical values for Environment and Block (replication). Replication df of 8 does not fit 18 environments with four replications. The text says G is p < 0.001, the table shows p < 0.01 | p. 6 | No | See fix 6, fifth bullet |
| Mega-environments: fourteen plus five environments makes 19, but 18 were tested | p. 13 | No | See fix 6, sixth bullet |
| Genotype names ICGV-SM 16445 (text) and ICGV-SM 16630 (Figures 6, 7) are not in Table 1. Figures 6 and 7 show 14 of 16 genotypes plus the local check, missing ICGV-SM 05702 and ICGV-SM 16519 | pp. 3, 9 to 13 | No | See fix 6, fourth bullet |
| Figure 6 panel sizes sum to 1,777 (our calculation), but 1,203 farmers took part | p. 4, p. 11 | No | See fix 6, last bullet |
| Methods says tricot ran 2021 to 2024, but farmer numbers are given for 2021 to 2023 only | p. 4 | No | Low importance |
| Lowest-yield sites. Text names Nakayaya as lowest overall, but the two-year mean of Chambezi (356 kg/ha) is slightly lower than Nakayaya (361 kg/ha) (our calculation from Table 4). Text names Kihinga as lowest in 2022, but Tumbi 2022 (97 kg/ha) is lower | pp. 6, 9, 13, Table 4 p. 8 | No | Low importance |
| Section 3.4 calls Mnanje 2009 outstanding in stability, but it sits far from the origin on PC2 in Figures 2 and 3, and ICGV-SM 16645 is named closest to ideal | pp. 9 to 10 | No | Low importance |
| Climate data cited as Table 1 but shown in Table 2 | p. 6 | No | Low importance |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: GEI and farmer and gender preferences for selection and release | Yes | | |
| Station design: 9 locations, 2 seasons, 4 replications, 6 of 7 AEZs | Partly | Medium | Fix 10 |
| tricot design: three varieties per farmer, local check, ClimMob, ODK, TPP traits, natural rainfall | No | Medium | Fix 10 |
| Gender sample: 549 men, 654 women | No | High | Fixes 2 and 10 |
| Main gender result: shared top traits, differences in mid-ranked traits | Wrong emphasis | High | Fix 2 |
| Correct top yielder from Table 4 | No (contradicted) | High | Fix 1 |
| Grand mean 832 kg/ha, H2 73.7%, CV 31.4% | No | Medium | Fix 1 key numbers |
| PC1 55.4% and PC2 9.47% of GGE variation | No | Low | Optional key number |
| Weak correlations between 2022 and 2023 environments, strong genotype by year interaction | No | Medium | Add to Summary: "Genotype rankings were consistent within 2023 but weakly correlated between the two seasons, pointing to strong genotype by year interaction." |
| Zone-level preferences (Figure 6), for example Mangaka 2009 preferred in Eastern, Southern highland and Western zones, and on-farm selection scores (Figure 7) | No | Medium | Add to Summary: "By agro-ecological zone, preferred varieties differed, with Mangaka 2009 preferred in several zones for its kernel color and size." |
| Tan small to medium kernels about 60% of the market (no reference given in the source) | No | Low | Optional |
| Authors' own limitations | No (replaced by others) | High | Fix 3 |
| Station and on-farm data not analysed together | No | Medium | Fixes 4 and 9 |
| Data on request only | No | Low | Fix 11 |
| Funding: AVISA and 1000FARMS, Gates Foundation | No | Low | Optional Note |

## Template compliance

- Summary word count: 408 (target 400 to 500). With fixes 1, 2 and 7 to 9: about 481.
- Gist: 23 words (under 30). Says what the paper shows, but overstates gender differences (optional fix 11).
- Keywords: 11 (8 to 12).
- Questions: 4 (4 to 7).
- House style: tricot is lowercase throughout. maniva is not used.
- not_established: missing (fix 4).
- Stated limitations section present but not from the source (fix 3).
