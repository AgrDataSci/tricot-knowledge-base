# Card review: mancini-2017-scirep

- **Card:** papers/mancini-2017-scirep.md
- **Source:** papers-pdf/mancini-et-al-2017.pdf (11 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 59 (52 body claims + 7 frontmatter fields) |
| Supported | 50 |
| Imprecise | 6 |
| Not in source | 3 |
| Contradicted | 0 |
| Important omissions | 10 (3 high, 7 medium) |
| Metadata issues | 5 |

The card is accurate on almost every number and follows the paper closely. The main problem is the last summary sentence. It links this paper to later work (fadda-2020-fps, vanetten-2019-pnas, desousa-2021-commsbio, gesesse-2023-pnas) and calls it the "starting point", but none of this is in the 2017 paper. The paper also builds on Mengistu et al. 2016, which analysed the same collection. On the panel size: the paper says 400 accessions, of which 25 are improved (modern) varieties and "the remaining" are landraces (p. 2). The figure 375 is correct by subtraction but is never printed in the paper, in the text or in a table. The 373 + 27 split comes from Fadda et al. 2020 and cannot be checked or resolved from this paper. A second, smaller issue: the paper's text and its Table 1 disagree about which group of women used the most end-use traits, and the card follows the text without flagging this.

## Fixes needed

1. **Summary, last sentence: later work is not in the source.**
   Card: "This is the starting point of the genebank-to-farm line of work that leads to fadda-2020-fps, vanetten-2019-pnas, desousa-2021-commsbio and gesesse-2023-pnas."
   Source: the paper mentions no work after 2016. It only anticipates a NAM population (50 landraces crossed with an Ethiopian modern variety), more than 1,200 RILs evaluated by farmers, and crowdsourced redistribution, citing van Etten 2011 (ref. 44) (p. 8). It also says the agronomic data are analysed in ref. 14 (Mengistu et al. 2016), which used the same collection (p. 3). So "starting point" is the card authors' interpretation and is not quite right. The sentence also leaves out what the paper itself proposes as the next step: test fewer varieties across more environments (p. 8).
   Replace the whole last summary paragraph with:

   > The authors argue that eliciting traditional knowledge quantitatively is a step toward locally adapted ideotypes. They report that 50 of the evaluated landraces were crossed with an Ethiopian modern variety to build a nested association mapping population, and that a collection of more than 1,200 recombinant inbred lines was also evaluated by smallholder communities. Top-ranked varieties, including several landraces that ranked above modern varieties, were being redistributed to farmers through crowdsourcing, reaching more than 900 households in 24 villages by 2016. The authors propose testing fewer varieties across more environments as the next step.

   Then move the lineage to Notes (see fix 12).

2. **Summary, paragraph 3: text and Table 1 disagree on women's end-use traits.**
   Card: "Women in Hagreselam used more quality and end-use traits, and marketability mattered to women in one site and men in the other."
   Source: the text (p. 4) says Hagreselam women used the most traits and named four uses (enjera, bread, tella, kolo). Table 1 (p. 4, checked on the PDF image) lists these four uses under **Geregera** women (14 traits). Hagreselam women list 11 traits with only a single "Use" trait. The marketability part is consistent in text and table.
   Replace with:

   > Women in one site named the most end-use traits, and marketability mattered to women in one site and men in the other.

   Add a Note (see fix 12).

3. **Summary, paragraph 2, and `crops`: "durum wheat accessions" is not stated.**
   Card: "400 durum wheat accessions" and `crops: durum wheat (with some bread wheat among modern varieties)`.
   Source: the paper says "400 Ethiopian wheat accessions" (p. 2). Durum is implied by context (introduction on Ethiopian durum wheat and ref. 14 on durum landraces, p. 2) but never stated for the panel. The bread-wheat remark is about the varieties farmers brought to the focus groups, not the 400 trial accessions: "most varieties listed as MV were bread wheat" (p. 4).
   Replace in the summary: "400 durum wheat accessions" with "400 wheat accessions".
   Replace the field with:

   ```
   crops: wheat (Ethiopian landraces, durum by context, plus 25 modern varieties)
   ```

4. **`not_established` is missing.** The paper is likely to be stretched in several ways. Add (the template requires semicolons as separators in this field):

   ```
   not_established: farmer scores in these high-input trials predict performance on farmers' own fields; top-ranked landraces outyield modern varieties under farmer management; the gender differences hold beyond these two communities; the ranking is stable across seasons (one season only); outcomes of the crowdsourced redistribution (only its reach is reported); that this was a tricot trial
   ```

5. **Methods bullet "Material": 375 is derived, not reported.**
   Source: "twenty-five were improved varieties ... The remaining were Ethiopian wheat landraces" (p. 2). The arithmetic 400 minus 25 = 375 is correct.
   Replace with:

   > - **Material.** 400 genebank accessions from the Ethiopian Biodiversity Institute (25 released modern varieties, the remaining 375 landraces by subtraction), two locations, 20 × 20 partial lattice with two replications, 2012 season. Farmers had no previous knowledge of the accessions.

   Key numbers row: change "400 accessions (25 modern varieties)" context to "Genebank material evaluated. 375 landraces is derived (400 minus 25), not printed in the paper".

6. **Summary, paragraph 3: canonical correlation sentence misses the site difference.**
   Card: "Canonical correlation showed that overall scores combined yield, biomass, seeds per spike, grain weight and plant height, but metric traits only partly explained them."
   Source: these five traits "had a positive relation with overall in both locations", stronger in Hagreselam, and overall "was differently contributed in the two locations" (p. 6). The Fig. 3 legend says the combination differs across locations (p. 7).
   Replace with:

   > Canonical correlation showed that overall scores related positively to yield, biomass, seeds per spike, grain weight and plant height, in a different combination at each site. Metric traits only partly explained farmer scores.

7. **Trait weights for the ranking are missing.** This is what a tricot user would most want: how much each trait drove the final ranking. Source p. 6: overall fixed at 1, spike 0.654 (Hagreselam) and 0.675 (Geregera), tillering 0.507 and 0.479, earliness 0.091 and 0.283. Weights were the average of a variation weight (based on the coefficient of variation) and a correlation weight with overall (p. 3).
   In summary paragraph 4, after "Weighted farmer scores produced a ranking of all 400 accessions at each site.", add:

   > After overall (fixed weight 1), spike carried the most weight, then tillering, with earliness last.

   Add Key numbers rows:

   | Number | Context | Primary source |
   |---|---|---|
   | 0.654 / 0.675 | Ranking weight of spike, Hagreselam / Geregera (overall fixed at 1) | This paper |
   | 0.507 / 0.479 | Ranking weight of tillering, Hagreselam / Geregera | This paper |
   | 0.091 / 0.283 | Ranking weight of earliness, Hagreselam / Geregera | This paper |

   Methods bullet "Analysis": replace "weighted ranking" with "weighted ranking (each trait weight is the mean of a consistency weight and its correlation with overall)".

8. **`data` field is imprecise.** The paper has no data availability statement. The R scripts on request are for the climate analysis and graphics (p. 2, p. 3). Accession names are in Supplementary Table S9 (p. 9). Replace with:

   ```
   data: no dataset deposited. Accession names in Supplementary Table S9. Custom R scripts (climate analysis, graphics) available on request from the corresponding author
   ```

9. **`gist`: "rank landraces" is too narrow.** The ranking covered all 400 accessions, including modern varieties (p. 1, p. 6). Replace with:

   ```
   gist: 60 Ethiopian farmers scored 400 genebank wheat accessions, giving 192,000 data points that link farmer preferences to metric traits and rank all accessions for local breeding
   ```

   (26 words.)

10. **Question 5 and keyword "Seeds for Needs" are not in the source.** The paper never names Seeds for Needs and cannot answer a question about how that line of work developed.
    Replace question 5 with:

    > - What happened to the top-ranked varieties and landraces after this study?

    In `keywords`, replace "Seeds for Needs" with "crowdsourcing" (keeps 11 keywords).

11. **Methods and limitations miss two design points relevant to tricot users.**
    Add Methods bullet:

    > - **Blinding.** Plots had anonymous labels, each group's entry point into the field was randomized, and a rapporteur recorded scores and kept dominant personalities in check. Scoring took place during seed maturation.

    Add Stated limitation:

    > - The two sites were scored at different maturity stages (Zadoks about 85 in Hagreselam, 75 in Geregera), which may explain the non-normal earliness scores in Hagreselam.

    (Source p. 3 and p. 4.)

12. **Notes: replace the first note and add three.** Replace "Not a tricot trial. It is the pre-breeding foundation ..." with:

    > - Not a tricot trial. Farmers scored every plot of all 400 accessions on a 1 to 5 scale in researcher-managed trials. The paper cites van Etten 2011 (vanetten-2011-idsbull) for the crowdsourcing approach used to redistribute top varieties. The link to later work (fadda-2020-fps, vanetten-2019-pnas, desousa-2021-commsbio, gesesse-2023-pnas) comes from those cards, not from this paper.
    > - The agronomic data for the same 400 accessions are analysed in Mengistu et al. 2016 (Plant Biotechnol J, ref. 14), which has no card yet.
    > - The text (p. 4) says women in Hagreselam named the most traits and four end-use traits (enjera, bread, tella, kolo). Table 1 lists these four under women in Geregera (14 traits), while Hagreselam women list 11 traits. The card follows neither site for this point.
    > - The paper states 25 improved varieties among 400 accessions (p. 2). 375 landraces is derived and not printed. Fadda et al. 2020 describes the same panel as 373 farmer varieties and 27 improved varieties. This paper cannot resolve the difference.

    Optional: add `relations:` with `- usesMethodIn: vanetten-2011-idsbull  # crowdsourced redistribution of top varieties, ref. 44`.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Joining smallholder farmers' traditional knowledge with metric traits to select better varieties of Ethiopian wheat | Same (p. 1) | Supported |
| authors | Mancini C, Kidane YG, Mengistu DK, Melfa and Workaye Farmer Community, Pè ME, Fadda C, Dell'Acqua M | Same order (p. 1). The pre-check flag on "Dell'Acqua" is only a straight vs curly apostrophe | Supported |
| year | 2017 | Published online 22 August 2017 (p. 1) | Supported |
| journal | Scientific Reports | p. 1 | Supported |
| article | 7, 9120 | "7: 9120" (footer, every page) | Supported |
| type | research article | Original study | Supported |
| source | external | No author found in people.md | Supported |
| doi | https://doi.org/10.1038/s41598-017-07628-4 | Same (footer) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution 4.0 (p. 10) | Supported |
| data | custom R scripts available on request | Scripts for climate analysis and graphics on request (p. 2, 3). No dataset statement. Names in Suppl. Table S9 (p. 9) | Imprecise (fix 8) |
| crops | durum wheat (with some bread wheat among modern varieties) | "wheat accessions" (p. 2). Bread-wheat remark is about farmer-held varieties (p. 4) | Imprecise (fix 3) |
| region | Ethiopia (Hagreselam, Tigray; Geregera, Amhara) | Melfa village, Hagreselam, Tigray and Workaye village, Meket, Amhara (p. 2) | Supported |
| keywords | 11 terms | "Seeds for Needs" not in source. "pre-breeding" is a fair paraphrase of founder lines and NAM (p. 8) | Minor issue (fix 10) |
| gist | ... rank landraces for local breeding | Ranking covers all 400 incl. modern varieties (p. 1, 6) | Imprecise (fix 9) |
| not_established | absent | Several likely overreaches exist | Missing (fix 4) |

Also note: the PDF carries a "Change History" line saying a correction was published and fixed in this version (p. 10). No action needed.

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Centralized breeding fails smallholders in low-input, high-risk areas, landraces preferred for adaptation and end-use quality | Supported | p. 1 | Paper also names higher market value |
| 2 | Summary | Participatory methods tapped little of traditional knowledge quantitatively | Supported | p. 1 abstract, p. 7 | |
| 3 | Summary | Study asks if evaluations can be broken into measurable traits and used for selection | Supported | p. 1, p. 2 | |
| 4 | Summary | 2012 season | Supported | p. 2 | |
| 5 | Summary | 400 durum wheat accessions from EBI genebank | Imprecise | p. 2 says "wheat accessions" | Durum only implied (fix 3) |
| 6 | Summary | Mostly landraces plus 25 released modern varieties | Supported | p. 2 | |
| 7 | Summary | Replicated trials at two highland sites, Hagreselam (Tigray), Geregera (Amhara) | Supported | p. 2, p. 3 | 2,572 and 2,867 m |
| 8 | Summary | 30 farmers per site, 15 women and 15 men | Supported | p. 2 | |
| 9 | Summary | Gender-separated FGDs on climate change, local varieties, selection criteria | Supported | p. 2 | |
| 10 | Summary | Every plot scored for four traits on a five-point scale | Supported | p. 2, p. 3 | 192,000 = 60 × 4 × 400 × 2 reps, consistent |
| 11 | Summary | Secret ballot with seeds in a closed hand | Supported | p. 3 | |
| 12 | Summary | 192,000 data points | Supported | p. 1, p. 4 | |
| 13 | Summary | Technicians measured ten agronomic traits on same plots | Supported | p. 3 | 3 phenology + 7 agronomic |
| 14 | Summary | Trait priorities differed by gender and location | Supported | p. 4, Table 1 | |
| 15 | Summary | Women in Hagreselam used more quality and end-use traits | Imprecise | Text p. 4 vs Table 1 p. 4 | Table puts these traits under Geregera women (fix 2) |
| 16 | Summary | Marketability: women in one site, men in the other | Supported | p. 4, Table 1 | |
| 17 | Summary | Gender agreement higher for agronomic than quality traits | Supported | p. 4 to 5, Fig. 1a | |
| 18 | Summary | Spike explained most of overall, correlations above 0.9 | Supported | p. 5 | Both sites, Suppl. Table S6 |
| 19 | Summary | Earliness ranked important but contributed little to overall | Supported | p. 5 | |
| 20 | Summary | Earliness correlated with days to booting, flowering, maturity | Supported | p. 5 to 6 | Correlations are negative |
| 21 | Summary | Spike correlated with seeds per spike | Supported | p. 6 | "best indicator" |
| 22 | Summary | CCA: overall combined GY, BY, SPS, TGW, PH | Imprecise | p. 6, Fig. 3 p. 7 | Combination differs by site (fix 6) |
| 23 | Summary | Metric traits only partly explained farmer scores | Supported | p. 1 | |
| 24 | Summary | Weighted ranking of all 400 accessions at each site | Supported | p. 3, p. 6 | |
| 25 | Summary | 20 of top 50 shared, four modern varieties | Supported | p. 6, Fig. 4 p. 8 | Dinkinesh, Bichena, Tossa, Workaye |
| 26 | Summary | Same trait combination preferred, different varieties | Supported | p. 7 to 8 | |
| 27 | Summary | Blind evaluation consistent, Dinkinesh case | Supported | p. 6 | Workaye ranked 29th and 3rd, a weaker match |
| 28 | Summary | Step toward locally adapted ideotypes | Supported | p. 7 | |
| 29 | Summary | 50 landraces crossed with a modern variety for NAM | Supported | p. 8 | |
| 30 | Summary | Crowdsourced redistribution, >900 households, 24 villages by 2016 | Supported | p. 8 | |
| 31 | Summary | Starting point of line of work leading to 2020 to 2023 cards | Not in source | p. 8 has no later work. p. 3 points to Mengistu 2016 | Fix 1 |
| 32 | Methods | 400 accessions, 375 landraces, 25 modern | Supported | p. 2 | 375 derived by subtraction, correct (fix 5) |
| 33 | Methods | Two locations, 20 × 20 partial lattice, two reps, 2012 | Supported | p. 2, p. 3 | |
| 34 | Methods | 30 per site, FGD then PE in six groups of five with rapporteur | Supported | p. 2, p. 3 | Three men's, three women's groups |
| 35 | Methods | Five-point scale for four traits, seed ballot | Supported | p. 2, p. 3 | |
| 36 | Methods | Ten metric traits plus WorldClim | Supported | p. 2, p. 3 | |
| 37 | Methods | ANOVA, Spearman, CCA, weighted ranking, PCA | Supported | p. 3 | Also Tukey test |
| 38 | Limitations | More fertilizer and weeding, mother trials | Supported | p. 3, p. 8 | Seed rate was lower than in farmer fields |
| 39 | Limitations | Quality and end-use traits not evaluable in field | Supported | p. 5 | |
| 40 | Limitations | Only two locations, chosen to maximize varieties | Supported | p. 8 | Authors frame it as a design choice |
| 41 | Key numbers | 400 accessions (25 modern) | Supported | p. 2 | |
| 42 | Key numbers | 60 farmers, 30 per site, 15 + 15 | Supported | p. 2 | |
| 43 | Key numbers | 192,000 data points | Supported | p. 1, p. 4 | |
| 44 | Key numbers | 10 metric traits | Supported | p. 1, p. 3 | |
| 45 | Key numbers | >0.9 spike vs overall | Supported | p. 5 | |
| 46 | Key numbers | 20 of top 50 shared | Supported | p. 6, p. 7 ("40%"), p. 8 | |
| 47 | Key numbers | 75.7% in first two PCA axes | Supported | p. 7, Fig. 4b p. 8 | PC1 46.2% + PC2 29.5% = 75.7%. Traits averaged over sites |
| 48 | Key numbers | >900 households, 24 villages | Supported | p. 8 | |
| 49 | Notes | Not a tricot trial | Supported | p. 2 to 3 | Full-collection scoring, no triads |
| 50 | Notes | Pre-breeding foundation for genebank-to-farm work | Not in source | p. 8 | Interpretation (fix 12) |
| 51 | Notes | This paper reports 25 modern varieties among 400 | Supported | p. 2 | Fadda part not checkable here |
| 52 | Questions | How Seeds for Needs moved from genebank to farm | Not in source | None | Fix 10 |

Frontmatter claims (counted in the totals): authors, article, license, region Supported. gist, crops, data Imprecise.

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: break down farmer preferences into metric traits, rank varieties (p. 2) | Yes | high | |
| Design: two sites, 400 accessions, partial lattice, two reps, 2012 (p. 2 to 3) | Yes | high | |
| Sample: 60 farmers, 15 + 15 per site (p. 2) | Yes | high | |
| Trait weights in the ranking (spike 0.654/0.675, tillering 0.507/0.479, earliness 0.091/0.283) and weighting method (p. 3, p. 6) | No | high | Fix 7 |
| Several landraces ranked above modern varieties, 16 of the 20 shared top varieties are landraces (p. 6, p. 8) | No | high | Fix 1 wording |
| Authors' next step: fewer varieties across more environments, G×E studies (p. 8) | No | high | Fix 1 wording. This is the bridge to crowdsourced testing |
| Blinding: anonymous plot labels, randomized entry, rapporteur role (p. 3) | Partly (secret ballot only) | medium | Fix 11 |
| Scoring at different maturity stages, Zadoks 85 vs 75 (p. 4) | No | medium | Fix 11 |
| ANOVA: significant differences among farmer groups and genders, p < 0.001. Gender correlation lower in Hagreselam for all traits (p. 4) | Partly | medium | Optional: "Gender agreement was lower in Hagreselam for all traits." |
| Across sites: earliness and spike agreed most, tillering least. Tillering vs NET weak (rs > 0.2). SPL vs overall rs = −0.112 (p. 5 to 6) | No | medium | Optional sentence in paragraph 3 |
| Farmer-held FGD varieties (13 in Hagreselam, 24 in Geregera) ranked first, but PE varieties had a higher rank score distribution (p. 4, p. 6) | No | medium | Optional sentence in paragraph 4 |
| Farmer selection: volunteers balanced by gender, age, wealth, from different households, both communities experienced with participatory work (p. 2) | No | medium | Optional methods detail |
| Same collection analysed agronomically in Mengistu et al. 2016 (p. 3) | No | medium | Fix 12 |
| More than 1,200 RILs evaluated by farmers (p. 8) | No | low | Fix 1 wording |
| Site climate: Hagreselam drier with a shorter rainy season, shorter rains as a key threat (p. 4 to 6) | No | low | |
| Plant height valued for thatching and feed (p. 6) | No | low | |
| Geregera farmers used a wider range of scores, possibly from PE familiarity (p. 6) | No | low | |
| Text cites Fig. 3b for the top-50 PCA, but it is Fig. 4b (p. 7 to 8) | No | low | Optional note |

## Template compliance

- Summary word count: 434 (target 400 to 500). With the suggested replacements it is about 472. Within range.
- Gist length: 25 words (under 30). The suggested gist is 26 words.
- Keywords: 11 (target 8 to 12). OK.
- Questions: 5 (target 4 to 7). OK, but question 5 cannot be answered from the paper (fix 10).
- not_established: absent (optional in the template, but recommended here, fix 4).
- relations: absent (optional). One link suggested in fix 12.
- House style: "tricot" is lowercase. maniva does not appear. No em dashes found in the card. The only semicolon is inside the `region` field.
