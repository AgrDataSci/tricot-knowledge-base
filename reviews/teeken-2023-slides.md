# Card review: teeken-2023-slides

- **Card:** papers/teeken-2023-slides.md
- **Source:** papers-pdf/teeken-et-al-2023.pdf (30 pages, one slide per page)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

Page numbers below are PDF pages. The slides carry no printed numbers (except "23" on PDF p. 23), so PDF page and slide number are the same. All 30 slides were opened as images.

## Overview

| Check | Result |
|---|---|
| Claims checked | 49 |
| Supported | 31 |
| Imprecise | 14 |
| Not in source | 4 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 7 |
| Important omissions | 5 high, 6 medium or low |
| Metadata issues | 5 (authors, license, gist, not_established missing, doi not verifiable) |

The card describes the trial design (slides 4 to 11) accurately, and every number it gives is correct. But it leaves out the whole results section (slides 17 to 25) and the variety release section (slides 26 to 28), which are what the title and the outline promise. It also reads some slides too strongly: it turns a hub diagram into a time "sequence", makes one context slide the "central message", treats an ODK tutorial link as a project tool, and gives a plot unit the slide does not state. The most important fix is to replace the generic results sentence with the actual covariate results (p. 17 to 25) and the variety release outcome (p. 26).

## Fixes needed

1. **Results are missing (high).** The card says only "Results gave a final ranking of varieties overall and per trait, with social covariates showing how preferences differ among user groups." Slides 17 to 25 give concrete results. Gender of the listed participant splits preferences (p. 18, p = 0.058, men n = 119, women n = 100). Women favour Baba 70 (IITA-TMS-IBA000070), Obasanjo 2 (TMS-13F1343P0022), TMS13F1307P0016 and TMS14F1306P0015. Men favour TMSIBA30572 and TMS13F1343P0002. Sex of the processor (p = 0.012), sex of the farmer (p = 0.094) and processing by self or another person (p = 0.00056) split preferences (p. 21). Food security (HDDS bad season, split at 7.72, p = 0.0019) and male control (p = 0.0033) split preferences (p. 24). A climate split on maximum night temperature at 25.43 °C has p = 0.24 (p. 17). The final replanting choice correlates most with post-harvest and food quality traits (p. 19, 20). Use the replacement Summary below, which covers these.

2. **Variety release outcome is missing (high).** The source says the Nigerian variety release committee accepted tricot to try out as a new way of on-farm testing, and that current and next year's tricot trials are owned by the committee and the CSP programme (p. 26). It also shows a redesign meeting at NACGRAB with the goal of automated reporting by social segment and integration of ClimMob with BreedBase (p. 28), and a 2022 webinar on tricot as an alternative on-farm test (p. 27). SKILL.md lists this card under "variety release and institutionalization", but the card body says nothing on it. Covered in the replacement Summary. Also add a question: "Has Nigeria's variety release committee taken up tricot?"

3. **Summary reads a sequence into a hub diagram, and calls some work "earlier" (medium).** Card: "They trace a sequence of research ... from the IITA Cassava Monitoring Study ..., through gender-responsive mother-baby trials ..., to tricot" and "Earlier work included ... a 1000minds study ... and demand creation trials." Source p. 4 is a hub: six boxes with arrows into a central circle, with no order or dates. The cited dates (Balogun et al. 2022, ThankGod et al. 2023) are later than the first tricot season (2019 to 2020, p. 5), so "earlier" is not right for them. Paragraph 5 also repeats paragraph 1. Fixed in the replacement Summary.

4. **"Central message" overstates one context slide (medium).** Card: "The central message is that women largely dominate cassava processing and marketing and therefore determine which varieties suit the whole value chain." This is the side text of one value chain slide (p. 3). The title and the outline conclusion (p. 1, 2) put tricot's socially inclusive feedback and its integration in breeding at the centre. The same slide also shows that wholesalers are mostly men (gari 52% men, fufu 68% men) and smallholder farmers are 48% women. Replace with: "A value chain slide shows that women make up most small-scale processors and retailers of gari and fufu, and argues that they therefore determine which varieties suit the whole value chain."

5. **Stated limitations are not the authors' (medium).** Neither bullet appears in the source. The authors present selection by expertise as intended (p. 13, 29), so the second bullet is a reviewer's view, not theirs. The one weakness the authors name is that evaluation should involve two people (dyads) at all moments (p. 25, 29). Replace the section with:

   ```
   - The authors plan to evaluate all moments with two people (dyads) in each tricot household. This suggests that so far one person per household gave most evaluations (card's inference from p. 25 and 29).
   - Card's caveat, not stated by the authors: the slides show trees and correlations without full statistics. The analysed sample sizes (219 to 316) differ from the 320 trials and are not explained. Use the peer-reviewed papers for evidence.
   ```

6. **Tools: ODK Collect is only a tutorial link (low to medium).** Card Summary: "with ClimMob and ODK Collect for registration and data collection", and Methods: "Tools. ClimMob and ODK Collect." Slide 8 says design, package generation, data storage and analysis are managed on ClimMob. ODK Collect appears only in the title of a YouTube tutorial in a list of links. The slides do not say which app was used in Nigeria. Replace the Methods bullet with:

   ```
   - **Tools.** ClimMob for design, package generation, data storage and analysis. RHoMIS household survey for social covariates. Plackett-Luce trees for analysis. The slide also links tutorial videos on ODK Collect.
   ```

7. **Plot size unit is not given on the slide (low).** Card: "small plots of five by six plants", Methods "plots of 5 × 6 plants", Key numbers "Plot size per variety". Slide 5 only says "Total of 320 Trials (5 x 6 plants)". It does not say whether this is per variety plot, and "small" is not in the source. Replace the Design bullet with:

   ```
   - **Design.** 3 of 30 varieties per farmer by sequentially balanced randomization, each variety appearing about 32 times. The slide gives "5 x 6 plants" without saying whether this is per variety plot.
   ```

   and the Key numbers row with:

   ```
   | 5 × 6 plants | Plot size as given on the slide. The unit (per variety plot or per trial) is not stated | This presentation |
   ```

8. **Consumers and "clonal crop" are not in the source (low).** Card: "while keeping processors and consumers involved" and "adapted for a clonal crop processed into food". Slide 4 says tricot upscales the baby-trial approach "with farmers and processors". Consumers are not mentioned for tricot, and "clonal" is not in the slides. Fixed in the replacement Summary.

9. **Frontmatter fixes.** See the Metadata check. Paste-ready lines:

   ```
   authors: Teeken B, Olaosebikan O, Bello A, and 13 co-authors
   license: CC BY (licence icon on each slide, version not stated)
   gist: Slides on 320 cassava tricot trials in Nigeria showing that gender, who processes and food security split variety preferences, and that Nigeria's release committee is trying tricot
   not_established: that the climate split on night temperature is reliable (p = 0.24 on the slide); that the gender and food security preferences hold beyond these 4 states and seasons; that tricot has replaced standard on-farm testing in Nigerian variety release (it was accepted to try out); that women and men in each household both evaluated every moment (dyads are only planned); that the analyses shown used all 320 trials (node sizes sum to 219, 273 and 316)
   ```

10. **Replacement Summary (486 words, no em dashes or semicolons).**

   ```
   These slides, presented at a gender conference in New Delhi in October 2023, describe how IITA and NRCRI use tricot to bring socially inclusive user feedback into cassava breeding in Nigeria. A hub diagram links tricot to other research that informed the current breeding product profile for processed cassava food (gari and fufu). This research includes the IITA Cassava Monitoring Study of variety adoption (2,500 households), a state-representative survey with participatory processing and consumer testing, gender-responsive mother-baby trials with farmers and processors, a 1000minds study of the economic value of traits, and demand creation trials. A value chain slide shows that women make up most small-scale processors and retailers of gari and fufu, and argues that they therefore determine which varieties suit the whole value chain.

   tricot was introduced to upscale the baby-trial approach, because larger representativeness was needed. Trials ran in the 2019–2020 and 2021–2022 seasons in four states chosen for cassava cultivation and processing. In each state, the agricultural development programme (ADP) helped select the two most active of three senatorial zones and four communities per zone. In each community, a focus group identified local social groups, and ten farmers were selected for expertise, motivation, gender and social group. This gave 80 trials per state and 320 in total, testing 30 farmer-popular and new varieties, each appearing about 32 times. Each farmer ranked three varieties as best and worst, overall and for specific traits, at 1, 3, 6 and 9 months, at harvest, during gari processing, for gari and eba quality, and after storage. The processor of the farmer's household did and evaluated the processing, and the household together made the final choice of which variety to replant. A RHoMIS household survey gave social covariates such as food security and male control. ClimMob managed design, package generation, data storage and analysis, and Plackett-Luce trees linked the rankings to social and climate covariates.

   The results slides show several splits. Gender of the listed participant split preferences, with women favouring Baba 70, Obasanjo 2 and the advanced clones TMS13F1307P0016 and TMS14F1306P0015. The sex of the processor, and whether the woman farmer processed herself, also split preferences. Food-insecure households favoured Obasanjo 2, while food-secure households with low male control favoured TMS13F1307P0016. A climate tree split at a maximum night temperature near 25 °C, but the slide gives p = 0.24 for this split. The authors conclude that the final choice depends mainly on post-harvest traits, especially overall food product quality, although one chart also ranks some first-month traits high.

   The slides also report that the Nigerian variety release committee accepted tricot to try out as a new way of on-farm testing, and that current and next year's trials are owned by the committee and the CSP programme. The authors plan evaluation by two household members (dyads) at all moments. They call for automated social covariate analysis within breeding data and for crop users as stakeholders in breeding.
   ```

11. **Sampling bullet: add selection detail and states (low to medium).** Replace with:

   ```
   - **Sampling.** 4 states (Osun, Benue, Imo and, from the map shading, Akwa Ibom), 2 of 3 senatorial zones per state and 4 communities per zone, chosen with the ADP, and 10 farmers per community. A focus group per community identified local social groups. Participants were selected for expertise and motivation, in proportion to social groups, sex and age, with equal chances for men and women.
   ```

12. **Key numbers: add rows (medium).**

   ```
   | about 32 | Times each variety appears across the 320 trials | This presentation |
   | 189 men, 127 women | Participants in the correlation of traits with the replanting choice, by gender | This presentation (p. 20) |
   | p = 0.058 | Split by gender of the listed participant (men n = 119, women n = 100) | This presentation (p. 18) |
   | p = 0.24 | Climate split at maximum night temperature 25.43 °C (nodes n = 107 and 112) | This presentation (p. 17) |
   | 83%, 75%, 60% | Women's share of small-scale processors, gari processors and fufu processors | Value chain slide citing other sources (p. 3) |
   ```

13. **Notes: add the source issues** (see the Source issues table for text), and a line on the release committee: "- Variety release: the Nigerian variety release committee accepted tricot to try out as on-farm testing (p. 26). See also cards under variety release in SKILL.md."

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Scaled citizen science ... within the breeding process | Same wording, with a final period (p. 1) | Supported |
| authors | Teeken B, and co-authors | 16 authors listed: Teeken, Olaosebikan, Bello, Tufan, Occelli, de Sousa, Madu, Onwuka, van Etten, Edughaen, Owoade, Agbona, van Heerwaarden, Iluebbey, Parkes, Kulakow (p. 30) | Imprecise. Use "Teeken B, Olaosebikan O, Bello A, and 13 co-authors" |
| year | 2023 | 9 to 12 October 2023 (p. 1) | Supported |
| journal | Presentation, Gender conference, New Delhi, 9–12 October 2023 (IITA) | "Gender conference New Delhi, 9 to 12 October 2023", IITA template (p. 1) | Supported |
| article | conference slides | 30 slides | Supported |
| type | presentation | Slide deck | Supported |
| doi | https://hdl.handle.net/10568/137005 | Not printed in the PDF. The CGSpace page could not be opened (request blocked), so not verified | Not in source (expected for a handle, check by hand) |
| license | see CGSpace record | CC BY icon in the footer of most slides (e.g. p. 2, 3, 5) | Imprecise. Template asks for the licence as stated in the PDF |
| data | none | No dataset cited | Supported |
| crops | cassava | Cassava throughout | Supported |
| region | Nigeria | Nigeria, 4 states (p. 5, 6) | Supported |
| gist | Conference slides on scaling cassava PVS ... showing how socially inclusive feedback, especially from women processors, informs breeding | Numbers correct (p. 5, 10). "Showing how ... informs breeding" names a topic, not a finding | Imprecise (topic list, no result) |
| not_established | absent | Results rest on trees with weak splits (p. 17, 18) and release use is a trial (p. 26) | Missing. Suggested text in Fix 9 |

Other fields: source "team" is correct (Teeken, van Etten, de Sousa are in people.md). peer_reviewed "no" is correct for slides. keywords: "demand-led breeding" is close to the slides' "demand driven" (p. 2), acceptable.

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Slides from a gender conference in New Delhi on IITA's move to demand-driven, gender-inclusive cassava breeding | Supported | p. 1, 2 | |
| 2 | Summary | Slides "trace a sequence" of research shaping the gari and fufu product profile | Imprecise | p. 4 | Hub diagram, no order or dates |
| 3 | Summary | IITA Cassava Monitoring Study on adoption, 2,500 households | Supported | p. 4 (Wossen et al. 2017) | |
| 4 | Summary | Gender-responsive mother-baby trials with farmers and processors | Supported | p. 4 (Teeken et al. 2021) | |
| 5 | Summary | tricot scales the baby-trial approach for greater representativeness | Supported | p. 4, 5 | |
| 6 | Summary | Trials in 2019–2020 and 2021–2022 seasons, NRCRI and IITA | Supported | p. 5 | |
| 7 | Summary | 4 states chosen for cultivation and processing activity | Supported | p. 5 | States not named in card |
| 8 | Summary | 2 most active of 3 senatorial zones | Supported | p. 5 | |
| 9 | Summary | 4 communities per zone identified with the ADP | Supported | p. 5 | |
| 10 | Summary | 10 farmers per community, purposive by expertise, gender, social group | Supported | p. 5 | |
| 11 | Summary | 80 per state, 320 in total | Supported | p. 5, 6, 10 | 2 × 4 × 10 = 80, × 4 = 320, recomputed |
| 12 | Summary | Each with small plots of five by six plants | Imprecise | p. 5 | Unit not stated, "small" not in source |
| 13 | Summary | 30 varieties, farmer-popular and new | Supported | p. 5, 9 | |
| 14 | Summary | Ranked 3 varieties best to worst, overall and by trait, planting to processing, no rating | Supported | p. 8, 10, 11 | |
| 15 | Summary | Sequentially balanced randomization | Supported | p. 9 | p. 8 also says BIBD |
| 16 | Summary | ClimMob and ODK Collect for registration and data collection | Imprecise | p. 8 | ODK only a tutorial link |
| 17 | Summary | Final ranking overall and per trait, with social covariates showing group differences | Supported | p. 9, 18 to 25 | Correct but generic. Real results omitted |
| 18 | Summary | Central message: women dominate processing and marketing and determine varieties | Imprecise | p. 3 | One context slide. Wholesale is mostly men |
| 19 | Summary | Argue for tricot as improved on-farm testing, automated social covariate analysis, users as stakeholders | Supported | p. 2, 28, 29 | |
| 20 | Summary | tricot placed in a longer research sequence informing IITA's product profile | Imprecise | p. 4 | Hub, not sequence. Repeats claim 2 |
| 21 | Summary | "Earlier work" included survey, mother-baby trials, 1000minds study, demand creation trials | Imprecise | p. 4 | 1000minds (2022) and demand creation (2023) are not earlier than tricot (2019) |
| 22 | Summary | tricot upscales baby trials, more participants, keeping processors and consumers involved | Imprecise | p. 4, 5 | Slide says farmers and processors. No consumers |
| 23 | Summary | Design adapted for a clonal crop processed into food, evaluation planting to processing | Imprecise | p. 8, 11 | "Clonal" not in source. Rest supported |
| 24 | Summary | Participants chosen to represent social and task groups | Supported | p. 13, 14 | |
| 25 | Methods | Sampling 4 × 2 × 4 × 10, purposive | Supported | p. 5 | |
| 26 | Methods | 3 of 30, SBR, plots 5 × 6 plants | Imprecise | p. 5, 8, 9 | Plot unit not stated |
| 27 | Methods | Best-to-worst, overall and by trait, planting to processing | Supported | p. 8, 11 | |
| 28 | Methods | Tools: ClimMob and ODK Collect | Imprecise | p. 8 | See Fix 6 |
| 29 | Limitations | Slides summarize results without full statistics | Not in source | p. 17 to 25 | Card's own caveat, fair, but must be labelled as such |
| 30 | Limitations | Purposive sampling of experienced farmers may not represent all users | Not in source | p. 13, 29 | Authors present expertise-based selection as intended |
| 31 | Key numbers | 320 trials and participants, 4 states | Supported | p. 5, 6 | |
| 32 | Key numbers | 80 per state | Supported | p. 5 | |
| 33 | Key numbers | 30 varieties | Supported | p. 5 | |
| 34 | Key numbers | 10 per community | Supported | p. 5 | |
| 35 | Key numbers | 5 × 6 plants, plot size per variety | Imprecise | p. 5 | "Per variety" not stated |
| 36 | Key numbers | 2,500 households, Wossen et al., cited in this presentation | Supported | p. 4 | Attribution correct |
| 37 | Notes | Grey literature archived on CGSpace | Not in source | not in PDF | Plausible, CGSpace page not checked (blocked) |

The metadata rows add 12 claims (8 Supported, 3 Imprecise, 1 Not in source) to the 37 above.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Analysed sample sizes differ from 320 and from each other, without explanation | p. 17, 18, 21 (nodes sum to 219), p. 24 (273), p. 20 (189 men + 127 women = 316) | No | - Sample sizes in the analyses (219, 273, 316) are lower than the 320 trials and are not explained on the slides. |
| Weak splits described as strong. Climate split p = 0.24, described as explaining variance. Gender split p = 0.058, called the most important socio-economic driver. The significance level used is not stated | p. 17, 18 | No | - The climate tree split (maximum night temperature) has p = 0.24 and the gender split has p = 0.058 on the slides. Treat both as suggestive. |
| Text gives the threshold as 25 °C, the tree split is at 25.43 | p. 17 | No | Low importance. No Notes text needed if the card says "near 25 °C". |
| Text says the final choice is driven by post-harvest traits, especially food quality, but the chart's top Kendall tau is weed competitiveness in the first month (about 0.37, read from chart), and 5 of the top 12 traits are first-month traits. The by-gender chart (p. 20) fits the text better | p. 19, 20 | No | - Slide 19's chart ranks some first-month traits (weed competitiveness, germination) among the highest correlations with the final choice, which only partly fits the stated conclusion that post-harvest food quality dominates. |
| Food-secure, low-male-control households are linked to TMS13F1307P0016 on p. 24 but to TMS-14F1306P0015 on p. 25 | p. 24, 25 | No | - Slides 24 and 25 name different favourite varieties for food-secure, low-male-control households (TMS13F1307P0016 versus TMS-14F1306P0015). |
| Highest point in the men's node (TMS-14F1223P0007, about 0.14, read from chart) is not labelled as liked by men. Labels go to TMSIBA30572 and TMS13F1343P0002 | p. 18 | No | Low importance. Optional: "- The variety with the highest worth for men on slide 18 (TMS-14F1223P0007) is not among those labelled as liked by men." |
| Plot size "(5 x 6 plants)" has no stated unit. Slide 25 curves for men and women have no axis values and look schematic | p. 5, 25 | No | - The slides do not say whether "5 x 6 plants" is per variety plot. The men and women curves on slide 25 have no scale. |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim: socially inclusive feedback to breeding and empowering crop users (p. 1, 2) | Yes | high | |
| Design: 4 states, 320 trials, 30 varieties, SBR, ranking from planting to processing (p. 5, 8 to 11) | Yes | high | Add "about 32 times per variety" |
| Covariate results: gender of participant, processor sex and self-processing, food security and male control, climate (p. 17, 18, 21 to 25) | No | high | Replacement Summary, Key numbers rows |
| Trait drivers of final choice: food quality traits, root yield, peeling, and men versus women correlations (p. 19, 20) | No | high | Replacement Summary |
| Variety release: committee accepted tricot to try out, trials owned by committee and CSP, NACGRAB redesign, ClimMob and BreedBase integration (p. 26 to 28) | No | high | Replacement Summary, new question, Notes line |
| Authors' own improvement: dyads at all evaluation moments (p. 25, 29) | No | high | Stated limitations (Fix 5), not_established |
| Household processing protocol: household processor evaluates processing, household makes final choice, yield in local measures for release demands (p. 10) | No | medium | Replacement Summary covers the first two. Optional Methods line on local-measure yield |
| Participant selection: focus group, proportional by social group, sex and age, equal chances for men and women, RHoMIS survey, local social group table (p. 10, 13 to 15) | Partly | medium | Sampling bullet (Fix 11) |
| States named on the map: Osun, Benue, Imo, Akwa Ibom (p. 5, read from map shading) | No | medium | Sampling bullet |
| Value chain shares: women 83% of small-scale processors, 75% of gari processors, 60% of fufu processors, but men dominate wholesale (p. 3, cited from other sources) | No | medium | Key numbers row |
| Analysis tools: Plackett-Luce trees, R packages gosset, PlackettLuce, ClimMobTools, climatrends, chirps (p. 9, 17) | No | medium | Tools bullet |
| "tricot in sum": genetic gain in farmers' fields, network linking NARES, NGOs and private sector, performative rather than deliberative engagement (p. 29) | Partly | medium | Optional sentence in Notes |
| Lead farmer chosen by the 10 farmers of a community (p. 16) | No | low | Optional Methods line |
| Funder (Bill & Melinda Gates Foundation) and partners (p. 30) | No | low | Optional Notes line |

## Template compliance

- Summary word count: 405 (target 400 to 500). Passes, but about 100 words repeat paragraph 1 in paragraph 5. The replacement Summary is 486 words.
- Gist: 27 words (under 30). Passes on length but lists topics. Replacement gist in Fix 9 is 27 words.
- Keywords: 10 (target 8 to 12). Passes.
- Questions: 4 (target 4 to 7). Passes. Suggest adding "Has Nigeria's variety release committee taken up tricot?" and "Which cassava varieties did women and men prefer in the Nigerian tricot trials?"
- House style: tricot is lowercase throughout. maniva does not appear. No em dashes found in the card body.
- not_established: missing. Add (Fix 9).
