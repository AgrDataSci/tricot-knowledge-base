# Card review: beza-2017-plosone

- **Card:** papers/beza-2017-plosone.md
- **Source:** papers-pdf/beza-et-al-2017.pdf (26 pages. Printed page numbers match PDF page numbers.)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 46 |
| Supported | 34 |
| Imprecise | 9 |
| Not in source | 1 |
| Contradicted | 2 |
| Source issues (problems in the source itself, not card errors) | 6 |
| Important omissions | 3 |
| Metadata issues | 4 |

The card gets the design, sample sizes and the main motivation ranking right, and most Key numbers match the source. The most serious error is that the card reports 24.5% of Ethiopian farmers as expecting production inputs in return. That figure comes from a different open question (additional motivations, Fig 6, p. 15). Fig 5 shows only about 4% of Ethiopian farmers expected inputs. The card also omits the phone-use results that matter most for tricot design (calls preferred to SMS, low SMS literacy in Ethiopia, the IVR recommendation) and the gamification conclusion. The gist is 30 words, so it is not under 30, and not_established is missing.

## Fixes needed

1. **24.5% production inputs is from the wrong question (Contradicted).** The card says (Summary and Key numbers) that 24.5% of Ethiopian farmers expected production inputs in return. The source gives 24.5% as the share of Ethiopian farmers who named production inputs as an *additional motivation* in an open question (p. 15, Fig 6, p. 16). For expected returns, Fig 5 (p. 15) shows Ethiopian production inputs at about 4% (read from a chart). Replace the Key numbers row with two rows:

   | 33% | Ethiopian farmers expecting agronomic advice in return for taking part (Fig 5) | This paper |
   | 24.5% | Ethiopian farmers naming production inputs (such as pesticides) as an additional motivation, open question (Fig 6) | This paper |

   In the Summary, use the replacement in fix 4, or at least change the sentence to: "In Ethiopia, 33% expected agronomic advice."

2. **"Pastime and community interaction mattered least everywhere" (Imprecise).** Pastime was lowest in all three countries (p. 8, p. 10, Fig 2 p. 9). Community interaction was not. In India it scored close to sharing, expectation, expert interaction and helping (4.38 to 4.52, p. 8). In Honduras it sat in the middle range (3.38 to 4.13, p. 10) and above expectation and helping in Fig 2. The Discussion (p. 20) does say community interaction was "valued less" in all three countries, which is a source issue (see below). Replace with: "Passing free time (pastime) was valued lowest in all three countries, below 2 on the 5-point scale in Ethiopia and Honduras (read from a chart) and 3.66 in India."

3. **Gist is 30 words and slightly overstates (Imprecise).** The template asks for under 30 words. "Expect advice, training or seed" reads as if all farmers expect a return, but the authors say about half did (p. 22). Replace with (28 words): "In 426 tricot farmers in India, Ethiopia and Honduras, contributing to science or sharing information motivated most, fun least, and those wanting returns sought advice, training or seed"

4. **Conclusions paragraph is more certain than the source, and adds "rather than cash" (Imprecise).** The card says the authors conclude citizen science is "viable", incentives should be advice, training or seed "rather than cash", and phones are "a realistic channel" for collecting data and returning results. The source says citizen science has "high potential" but needs easy-to-use mechanisms (p. 22). It names agronomic advice, capacity building and seed as the most needed incentives (p. 22) but does not contrast them with cash. Money was named by 1% of Indian farmers in Fig 5 (p. 15), but by 11% of Indian farmers who wanted a reward for sharing information (p. 16, Fig 7). Farmers had not yet used phones to report trial results (p. 22). The card's last paragraph also says the authors "argue that citizen science projects should design incentives" for each community, where the source says projects "might need to consider different approaches" (p. 18). That paragraph also repeats paragraph 3. Replace the whole Summary with this version (459 words), which also fixes items 1 and 2, adds the phone and gamification results, and removes the repetition:

   > Agricultural citizen science depends on volunteers who give time and skills, so knowing why they join is key to recruiting and keeping them. The paper surveys farmers taking part in Bioversity's Seeds for Needs initiative, which has run crowdsourced tricot trials since 2011, on their motivations and on how they use mobile phones.
   >
   > The authors built a questionnaire from motivational factors in the citizen science literature, grouped into collectivistic (contributing to science), altruistic (helping researchers), intrinsic egoistic (sharing information, pastime) and extrinsic egoistic (expecting something in return, networking with experts or community). In 2014 and 2015 they interviewed 426 farmers, 300 in India, 94 in Ethiopia and 32 in Honduras. Farmers rated each factor on a 5-point scale. The authors analyzed the answers with non-parametric tests, generalized linear models, redundancy analysis and principal component analysis.
   >
   > Motivations overlapped but differed by country. Indian farmers ranked contributing to scientific research highest. Ethiopian and Honduran farmers ranked sharing information highest. Passing free time (pastime) was valued lowest in all three countries, below 2 on the 5-point scale in Ethiopia and Honduras (read from a chart) and 3.66 in India. Country and education together explained only about 20% of the variation, with more educated farmers placing more weight on contributing to science. Two broad groups emerged, one driven by sharing, helping and contributing, and another by expectations of return and interaction with experts and other community members.
   >
   > The authors report that about half of the farmers expected something back. What they wanted differed by country. In Ethiopia, 33% expected agronomic advice. In Honduras, capacity building came first (50%). In India, 44% expected improved seed (seed innovation). Only 2% to 3% expected to receive research results, and money was named by only 1% of Indian farmers. Asked about rewards for sharing information in future (India and Ethiopia only), around half of farmers in India and 44% in Ethiopia expected none. Among Indian farmers who did want a reward, the paper reports that 11% named money.
   >
   > More than 90% of farmers in all three countries owned a mobile phone. Many already used it for agricultural advice (77% in Ethiopia, 37% in India, 21% in Honduras), but none had yet used it to report trial results. Most preferred calls to SMS, and only 21% of Ethiopian farmers could read SMS.
   >
   > The authors conclude that citizen science in agriculture has high potential but needs easy-to-use mechanisms, such as Interactive Voice Response. Agronomic advice, capacity building and seed were the incentives most wanted. On gamification, they note that pastime scored low and intrinsic motives scored high, so game elements that stress extrinsic rewards, such as scoreboards or badges, would likely be counterproductive. They suggest that projects might need different approaches in each country to attract and keep farmers.

5. **not_established is missing.** Add: `not_established: that farmers take part without wanting any return (about half expected something back); that phones were used to report trial results in these trials (they were not yet); that cash payments raise or lower participation (not tested); that the results represent all farmers in the three countries (exploratory, non-random sample); that women's motivations are well described (17% of respondents were women)`

6. **Instrument bullet omits the rating scale (Imprecise).** The card says farmers marked the factors that applied. They then rated each factor on a 5-point Likert scale (p. 7), and all results are based on those ratings. Replace with: "**Instrument.** Seven motivational factors read out one by one in the local language and rated on a 5-point Likert scale (1 = not important at all, 5 = very important), plus open questions on other motivations, expected returns and rewards (the reward question was asked only in India and Ethiopia), farmer characteristics and phone use."

7. **Analysis bullet is incomplete (Imprecise).** Within countries the authors used Friedman tests with Wilcoxon post-hoc tests, between countries Kruskal-Wallis with Dunn-Bonferroni tests, plus GLMs and qualitative content analysis (p. 7 to 8). Replace with: "**Analysis.** Friedman tests with Wilcoxon signed-rank post-hoc tests within countries, Kruskal-Wallis tests with Dunn-Bonferroni post-hoc tests between countries, generalized linear models and redundancy analysis linking motivations to farmer characteristics, PCA to group motivations, and qualitative content analysis of open answers."

8. **First limitation mixes the authors' words and the card's inference (Imprecise).** The selection facts are right (pp. 6 to 7). The authors' own limitation is that the study was exploratory and does not claim to represent farmers statistically, for example by age and gender (p. 21). They also call current participants an "already-motivated sub-sample" (p. 3). Replace with: "The study was exploratory and does not claim to represent farmers in the three countries statistically, for example by age or gender. Farmers were chosen by researchers, extension workers or NGO staff, and in India and Ethiopia preference went to those with more than one season in the trials, so respondents were an already motivated group."

9. **"Honduras had only 32 respondents" is not an author-stated limitation (Not in source as a limitation).** The number is correct (p. 6), but the authors never discuss it. Move it to Notes: "Card note: Honduras had only 32 respondents, and education data were missing for 9 of them (28%, Table 2, p. 9). The authors do not discuss this sample size."

10. **Add two author-stated limitations.** "Answers were self-reported in interviews. The authors suggest role-playing games to cross-check them in future studies." (p. 20) and "The authors note that farmers may have read 'pastime' as frivolous fun rather than enjoyment of work, which may explain its low score." (p. 21)

11. **Two-groups sentence drops community interaction (Imprecise, minor).** The second group is expectation, expert interaction and community interaction (pp. 11 to 12, p. 22). Use: "another by expectations of return and interaction with experts and other community members." (already in the replacement Summary)

12. **Phone use sentence overstates scope (Imprecise, minor).** "Already used it for extension advice" is from the Conclusions (p. 22), but Table 6 (p. 17) shows 77% in Ethiopia, 37% in India and 21% in Honduras used phones for agricultural advice. The replacement Summary gives these numbers. Add Key numbers rows:

   | 76% / 87% / 68% | Farmers preferring calls for future citizen science contact, India / Ethiopia / Honduras (SMS 1% / 8% / 7%) | This paper |
   | 87% / 21% / 85% | Farmers able to read and understand SMS, India / Ethiopia / Honduras | This paper |

13. **Crops field misses barley (Imprecise).** Ethiopia's Seeds for Needs work used durum wheat and barley accessions (p. 5). Replace with: `crops: rice and wheat (India), durum wheat and barley (Ethiopia), common bean (Honduras), from Seeds for Needs trials (the paper does not say which crop each respondent tested)`

14. **Add source-issue Notes** (texts in the Source issues table below).

15. **License (minor).** The PDF says "Creative Commons Attribution License" without a version (p. 1). Suggested: `license: CC BY (Creative Commons Attribution License, version not printed in the PDF)`. Keeping CC BY 4.0 is acceptable if the team checks it on the publisher page.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | What are the prospects for citizen science in agriculture? Evidence from three continents on motivation and mobile telephone use of resource-poor farmers | Same (p. 1) | Supported |
| authors | Beza E, Steinke J, van Etten J, Reidsma P, Fadda C, Mittra S, Mathur P, Kooistra L | Same 8 authors, same order (p. 1) | Supported |
| year | 2017 | Published May 4, 2017 (p. 1) | Supported |
| journal | PLOS ONE | PLoS ONE in citation, PLOS ONE in footer (p. 1) | Supported |
| article | 12(5), e0175700 | 12(5): e0175700 (p. 1) | Supported |
| type | research article | "RESEARCH ARTICLE" (p. 1) | Supported |
| doi | https://doi.org/10.1371/journal.pone.0175700 | Same (p. 1) | Supported |
| license | CC BY 4.0 | "Creative Commons Attribution License", no version (p. 1) | Imprecise (minor), see fix 15 |
| data | https://doi.org/10.5061/dryad.v51bv (Dryad) | Dryad, dx.doi.org/10.5061/dryad.v51bv (p. 1) | Supported |
| crops | wheat, rice, durum wheat, common bean | Rice and wheat (India), durum wheat and barley (Ethiopia), common bean (Honduras) (p. 5) | Imprecise, barley missing (fix 13) |
| region | India, Ethiopia, Honduras | Bihar (India), Oromia (Ethiopia), five departments (Honduras) (p. 5) | Supported |
| gist | Survey of 426 tricot farmers ... rather than cash | 30 words. "Rather than cash" and "expect" for all farmers go beyond the source (pp. 15 to 16, p. 22) | Imprecise (fix 3) |
| not_established | missing | Needed: phone reporting not tested, cash not tested, non-random sample | Missing (fix 5) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Citizen science depends on volunteers, so motivation matters for recruiting and keeping them | Supported | Abstract (p. 1) | |
| 2 | Summary | Seeds for Needs has run crowdsourced tricot trials since 2011 | Supported | p. 4 | |
| 3 | Summary | Questionnaire from literature, factors grouped as collectivistic, altruistic, intrinsic and extrinsic egoistic | Supported | Table 1 (p. 6) | |
| 4 | Summary | 2014 and 2015, 426 farmers: 300 India, 94 Ethiopia, 32 Honduras | Supported | Section 2.5 (p. 6) | |
| 5 | Summary | Non-parametric tests, RDA and PCA | Supported | pp. 7 to 8 | Omits GLM and qualitative analysis. Minor |
| 6 | Summary | Motivations overlapped but differed by country | Supported | Abstract (p. 1), Table 4 (p. 11) | |
| 7 | Summary | Indian farmers ranked contributing highest | Supported | 4.86 (p. 8), Fig 2 (p. 9) | |
| 8 | Summary | Ethiopian and Honduran farmers ranked sharing highest | Supported | pp. 8, 10 | |
| 9 | Summary | Pastime and community interaction mattered least everywhere | Imprecise | Pastime lowest everywhere (pp. 8, 10). Community interaction mid-range in India and Honduras (pp. 8, 10, Fig 2 p. 9) | Follows Discussion p. 20, which conflicts with Results. Fix 2 |
| 10 | Summary | Country and education explain about 20%, educated farmers weight contributing more | Supported | RDA 15% and 5% (p. 13), GLM B = 0.009 (p. 13), p. 21 | |
| 11 | Summary | Two groups: sharing, helping, contributing vs expectation and contact with experts | Imprecise | Second group also includes community interaction (pp. 11 to 12, p. 22) | Fix 11 |
| 12 | Summary | About half of farmers expected something back | Supported | Conclusions (p. 22) | Basis unclear in source (source issue 2) |
| 13 | Summary | Ethiopia 33% wanted agronomic advice | Supported | p. 15, Fig 5 | |
| 14 | Summary | Ethiopia 24.5% wanted production inputs | Contradicted | 24.5% is an additional motivation, Fig 6 (p. 15 to 16). Fig 5 shows about 4% expected inputs (read from chart) | Fix 1 |
| 15 | Summary | Honduras capacity building first (50%) | Supported | p. 15, Fig 5 | |
| 16 | Summary | India 44% wanted access to new seed | Supported | "Seed innovation (e.g., improved seed)" 44% (p. 15) | |
| 17 | Summary | Only 2% to 3% expected research results | Supported | p. 15 | |
| 18 | Summary | About half in India and 44% in Ethiopia expected no reward for sharing information | Supported | p. 15, Fig 7 (p. 16) | Question asked only in India and Ethiopia (p. 6). Worth saying |
| 19 | Summary | More than 90% owned a phone in all three countries | Supported | 91%, 93%, 93% (Table 6, p. 17) | |
| 20 | Summary | Already used phones for extension advice and market information | Imprecise | Conclusions (p. 22). Table 6: advice 37% India, 77% Ethiopia, 21% Honduras (p. 17) | True for a minority in India and Honduras. Fix 12 |
| 21 | Summary | Authors conclude citizen science is viable and incentives should be advice, training, seed rather than cash | Imprecise | "High potential" with easy-to-use mechanisms (p. 22). No contrast with cash. 11% of Indian reward seekers named money (p. 16) | Fix 4 |
| 22 | Summary | Phones are a realistic channel for collecting data and returning results | Imprecise | "High potential", but farmers had not yet used phones to send results (p. 22) | More certain than source. Fix 4 |
| 23 | Summary | India: contributing above expectation and sharing, then helping and expert interaction | Supported | pp. 17 to 18 | Most differences among these were not significant (Table 3, p. 10) |
| 24 | Summary | Ethiopia: sharing, then helping and contributing | Supported | p. 18 | |
| 25 | Summary | Honduras: sharing, then contributing and expert interaction | Supported | p. 18 | |
| 26 | Summary | Differences related mainly to country and education | Supported | p. 13, p. 18, p. 21 | |
| 27 | Summary | Authors argue projects should design incentives per community and use phones to collect and return | Imprecise | "Might need to consider different approaches" (p. 18), phones "have the potential" (p. 22) | More certain than source. Fix 4 |
| 28 | Methods | 426 structured face-to-face interviews 2014 to 2015, India 300, Ethiopia 94, Honduras 32 | Supported | p. 6 | |
| 29 | Methods | Factors read in local language, farmers marked those that applied | Imprecise | Also rated on 1 to 5 Likert scale (p. 7) | Fix 6 |
| 30 | Methods | Wilcoxon and Kruskal-Wallis, RDA, PCA | Imprecise | Friedman, Dunn-Bonferroni, GLM and content analysis also used (pp. 7 to 8) | Fix 7 |
| 31 | Limitations | Selected by researchers and extension staff, not random, may favor engaged participants | Imprecise | Selection (pp. 6 to 7). Authors' limitation is exploratory, not representative (p. 21), "already-motivated sub-sample" (p. 3) | Fix 8 |
| 32 | Limitations | Honduras had only 32 respondents | Not in source | Count correct (p. 6) but not stated as a limitation | Fix 9 |
| 33 | Limitations | Characteristics explained only about 20% | Supported | p. 21 | |
| 34 | Limitations | Phone use for trial data not tested | Supported | p. 22 | |
| 35 | Key numbers | 426 farmers, 2014 to 2015 | Supported | p. 6 | |
| 36 | Key numbers | 300 / 94 / 32 | Supported | p. 6, Table 2 (p. 9) | |
| 37 | Key numbers | about 20% (country 15%, education 5%) | Supported | p. 13 | |
| 38 | Key numbers | 21.5% variance on PC2 | Supported | p. 11 | PC1 explains 35%, could be added |
| 39 | Key numbers | 33% / 24.5% agronomic advice / production inputs, Ethiopia | Contradicted | 33% supported (p. 15). 24.5% is from Fig 6, not expectations | Fix 1 |
| 40 | Key numbers | 50% Honduras capacity building | Supported | p. 15 | |
| 41 | Key numbers | 44% India seed innovation | Supported | p. 15 | |
| 42 | Key numbers | 2% to 3% research results | Supported | p. 15 | |
| 43 | Key numbers | about 50% / 44% expect no reward, India / Ethiopia | Supported | p. 15, Fig 7 | |
| 44 | Key numbers | more than 90% own a phone | Supported | Table 6 (p. 17) | |
| 45 | Key numbers | 83% male | Supported | p. 8. Recomputed: 352/426 = 82.6% | |
| 46 | Notes | High male share means women under-represented | Supported | 83% male (p. 8), authors say sample not representative by gender (p. 21) | Card's own inference, consistent with source |

The cross-reference to desousa-2024-asd was not checked as a claim. That card also gives 426 farmers, which agrees.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Discussion says community interaction was valued less in all three countries, but Results and Fig 2 show it close to other factors in India and above expectation and helping in Honduras | p. 20 vs pp. 8 to 10, Fig 2 (p. 9) | No. Card repeats the Discussion version | "Source issue: the Discussion (p. 20) says community interaction was valued less in all three countries, but Fig 2 and the Results (pp. 8 to 10) show it close to other factors in India and above expectation and helping in Honduras." |
| Conclusions say around half of farmers expected something in return, but no result gives this figure. Nearest is Fig 7 (India and Ethiopia only, future reward for sharing information) | p. 22 vs pp. 15 to 16 | No | "Source issue: the Conclusions (p. 22) say about half of farmers expected something in return. No single result gives this. The closest is Fig 7 (India and Ethiopia only), where about 50% and 44% expected no reward for sharing information." |
| Figs 5 and 7 do not state the denominator. Fig 5 bars sum to about 81% (India, Ethiopia) and about 100% (Honduras). Fig 7 India bars sum to about 118% (all read from charts) | pp. 15 to 16 | No | "Source issue: Figs 5 and 7 do not give a denominator, and bars do not sum to 100% (read from charts). Percentages may refer to different groups or allow several answers." |
| Interviews described as semi-structured (section 2.4) and as structured (section 2.5) | pp. 6 to 7 | No | Not needed (low importance) |
| Table 3, India: T values for pastime comparisons (5.39 to 12.23) look like z statistics, unlike other cells, and Contributing vs Expectation shows r = 0.02 with p = 0.000 | p. 10 | No | Not needed (low importance) |
| Hofstede "collectivism" is used to explain why Ethiopians and Hondurans valued sharing more, while India scored higher on the factor the paper itself labels collectivistic | p. 21 vs Table 1 (p. 6) | No (card does not use this point) | Not needed |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: farmers' motivations and phone use, to inform design of agricultural citizen science | Yes | High | |
| Design, countries, 426 respondents, selection by staff | Yes | High | |
| 5-point Likert rating of seven factors | No | Medium | Fix 6 |
| Mean scores, for example contributing 4.86 and pastime 3.66 in India, pastime below 2 in Ethiopia and Honduras (chart) | No | Medium | In replacement Summary |
| Main motivation ranking per country | Yes | High | |
| PCA two groups, PC1 35%, PC2 21.5% | Partly (PC2 only) | Low | Optional Key numbers row: "35% / 21.5% | Variance on PC1 (sharing, helping, contributing vs pastime) / PC2 (expectation, expert and community interaction) | This paper" |
| GLM: women and less educated farmers valued pastime more | No | Medium | "Women and less educated farmers valued pastime more than men and educated farmers (GLM, p = 0.004 and p < 0.001)." in Notes or Summary |
| RDA: country 15%, education 5% | Yes | Medium | |
| Expected returns (Fig 5) | Yes, with error | High | Fix 1 |
| Reward question asked only in India and Ethiopia, and Fig 7 detail (Ethiopia 42% want agronomic information, India seed 30%, capacity building 25%, money 11%) | Partly | Medium | In replacement Summary |
| Phone use: calls preferred to SMS (76% / 87% / 68%), SMS literacy (87% / 21% / 85%), low internet use, airtime | No | High | Fix 12 and replacement Summary |
| IVR recommended because of illiteracy | No | High | In replacement Summary |
| Gamification: extrinsic game elements likely counterproductive, intrinsic motives score high | No | High | In replacement Summary |
| Exploratory, not statistically representative | No (card gives its own version) | Medium | Fix 8 |
| Role-playing games suggested to cross-check self-reports | No | Low | Fix 10 |
| Low community interaction may reflect household-centred farming and on-farm testing | No | Low | Optional Notes |
| Seeds for Needs scale (over 20,000 farmers, 14 countries) | No | Low | Optional |

## Template compliance

- Summary word count: 407 (within 400 to 500, close to the lower limit). The suggested replacement is 459 words.
- Gist: 30 words, so not under 30. Fix 3 gives 28 words.
- Keywords: 8 (within 8 to 12). Consider adding "SMS" or "Interactive Voice Response" and "gamification", which are main topics of the paper.
- Questions: 4 (within 4 to 7).
- House style: tricot written in lowercase throughout. maniva not used. No issues.
- not_established: missing (optional in template, but the pilot asks for it). Fix 5.
