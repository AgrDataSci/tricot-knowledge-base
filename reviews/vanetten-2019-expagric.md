# Card review: vanetten-2019-expagric

- **Card:** papers/vanetten-2019-expagric.md
- **Source:** papers-pdf/van-etten-et-al-2019a.pdf (22 pages, printed pages 275 to 296. PDF page = printed page minus 274)
- **Reviewed:** 2026-11-21, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 51 |
| Supported | 37 |
| Imprecise | 10 |
| Not in source | 1 |
| Contradicted | 3 |
| Source issues (problems in the source itself, not card errors) | 3 |
| Important omissions | 5 high (14 listed in total) |
| Metadata issues | 4 |

The card describes the design and the data-format lessons well, and most numbers are right. But it opens with a wrong start date for the pilots (2011, which is the year of the original proposal, while the source says testing ran 2013 to 2015) and an outside programme name that the source never uses. The crops field names two crops (bread wheat, rice) that were not pilot crops and misses barley and sorghum. Key results are missing: the Bradley–Terry model is never named, the finding of no gender differences in preferences is absent, and the weather-sensor results are not reported. The most important fix is the first summary sentence and the matching Key numbers row (source p. 277, PDF p. 3).

## Fixes needed

1. **Start date and programme name of the pilots (Contradicted, Not in source).**
   Card (Summary sentence 1): "based on pilots run from 2011 under the Seeds for Needs initiative". Key numbers: "2011 | Start of tricot pilots under Seeds for Needs".
   Source p. 277 (PDF p. 3): testing of the different elements was done in 2013 to 2015. 2011 is the year of van Etten's proposal (p. 276, 280). "Seeds for Needs" does not appear anywhere in the paper.
   Replace summary sentence 1 with: "This paper gives the first full account of tricot as a method, building on van Etten (2011), with early results from pilots run in 2013 to 2015."
   Replace the Key numbers row with two rows:
   `| 2013–2015 | Period when the tricot elements were tested in pilots | This paper |`
   `| 2011 | Original proposal that tricot elaborates | Van Etten 2011 (vanetten-2011-idsbull), cited in this paper |`
   If the Seeds for Needs link is wanted, put it in Notes: "The pilots are often associated with Bioversity's Seeds for Needs work. This is outside knowledge. The paper does not use the name."

2. **Crops field (Contradicted).**
   Card: "common bean, durum wheat, bread wheat, rice and others in pilots".
   Source p. 284 (PDF p. 10): the crops were barley and durum wheat in Ethiopia, sorghum in Kenya and Tanzania, and common bean in Central America. Bread wheat is never mentioned. Rice appears only in cited work on diversity kits in Nepal (p. 279). The India crop is not named.
   Replace with: `crops: common bean, barley, durum wheat, sorghum`

3. **Bradley–Terry model missing (high-importance omission, Methods Imprecise).**
   Card Methods: "Rankings aggregated statistically, with environmental covariates from geolocation." The Summary also never names the model.
   Source p. 282 to 283 (PDF p. 8 to 9) names the Bradley–Terry model as a novel feature and explains it in Box 1. Environmental covariates are a possibility ("could produce", p. 282), and the abstract lists integrating environmental analysis as an open issue (p. 276). No environmental analysis of crop trials is reported.
   Replace with: "- **Analysis.** Rankings aggregated with the Bradley–Terry model (Box 1). Geolocation makes it possible to add environmental covariates, but the pilots did not yet report such an analysis."
   Add "Bradley–Terry model" to keywords.

4. **Results missing from the Summary (high-importance omissions).** The card does not report: no statistically significant gender differences in preferences in any trial (p. 290), robust differences between varieties except in a few trials with 50 to 70 farmers (p. 287), the Nicaragua result (local variety best, biofortified INTA Ferroso worst, p. 287 to 288, Figure 2), agreement with parallel group PVS (p. 288), and the weather-sensor result (useful data, but sensors stolen or displaced and not yet suitable at scale, p. 288, 291). The last summary paragraph repeats content already given (interactive voice response appears twice) and can be dropped to make room. A full replacement summary is given at the end of this list (item 13).

5. **Gist lists topics (Imprecise).**
   Card: "The first full description of tricot as a method, with the design rationale and lessons from the first pilots on data formats, statistical design, farmer motivation, gender and cost". This lists topics instead of findings. "Cost" was not a pilot lesson. The paper gives no cost data.
   Replace with (28 words): `gist: First account of tricot: pilots in India, East Africa and Central America found it feasible with low-literacy farmers, giving robust rankings and wide acceptance after formats were simplified.`

6. **not_established missing (metadata issue).** Add:
   `not_established: accuracy of farmer rankings for other crops and traits (checked only on four plant traits of common bean in Honduras); absence of gender differences in preferences in other settings; effect sizes or yield gains (rankings only); cost savings in figures (no cost data reported); suitability of iButton sensors at scale (judged not yet appropriate); reception by farmers without prior PVS experience; phone or IVR data collection (not used in these pilots)`

7. **Region field (Imprecise).**
   Card: "Central America (Honduras, Nicaragua), Ethiopia, India, East Africa". Source p. 284: India, East Africa (Kenya, Tanzania, Ethiopia), Central America (Honduras, Guatemala, Nicaragua), plus the weather-sensor pilot in Costa Rica (p. 284, Figure 3).
   Replace with: `region: India, East Africa (Kenya, Tanzania, Ethiopia), Central America (Honduras, Guatemala, Nicaragua), Costa Rica (weather-sensor pilot)`

8. **Evaluation bullet says data were collected by phone (Imprecise).**
   Source p. 285 (PDF p. 11): telephone interviews were not part of the pilots reported. Data were first on paper, then digitized by field agents through visits (p. 284).
   Replace with: "- **Evaluation.** Farmers rank the three varieties on about six to eight aspects by naming the best and the worst. In the pilots, field agents collected the data, first on paper and later on digital forms. Phone collection was planned but not used."

9. **Integration and facilitation (Imprecise).**
   Card: "Those approaches proved the value of farmer evaluation but stayed hard to integrate into breeding programmes because they need intensive facilitation." Source p. 276 says participatory approaches are still not fully integrated into many R&D programmes, but gives no cause. On p. 279 it calls IRD and diversity kits hands-off and highly cost-effective, so "intensive facilitation" does not apply to them.
   Replace with: "Farmer-participatory approaches have proved their value but are still not fully integrated into many R&D programmes. Group trials suffer from uneven participation and mother trials are costly, while IRD and diversity kits are cheap and hands-off."

10. **Why three varieties (Imprecise).**
    Card: "Diversity kits had shown that three varieties per farmer works well, which informed the triadic design." Source p. 281 (PDF p. 7): diversity kits worked well with three varieties, but the original choice of three was justified by Martin (2004) on triadic comparisons in ethnobiology. Collaborators also pushed for a local check as a fourth variety, and four-variety variants were tested (p. 281, 284).
    Replace with: "The choice of three varieties came from the original proposal, which drew on triadic comparisons in ethnobiology, and diversity kits had also worked well with three varieties. Collaborators asked for a local check as a fourth variety, and some pilots tested four."

11. **Cost and environment wording more certain than the source (Imprecise).**
    Card: "Staff time, not seed or materials, drove cost, and unit costs fell as more farmers joined." Source p. 292: staff time is a major driver of cost and unit costs tend to drop. No cost figures are given.
    Replace with: "The authors see staff time, not seed or materials, as the main cost driver and expect unit costs to drop as more farmers join, but they give no cost figures."
    Card: "the trials are linked to geographic and climate data so results can be analysed against the environment". Source p. 282: geolocation makes it possible, and the approach could produce G×E information. Replace with: "Geolocated trials could also be linked to environmental data."

12. **Key numbers and limitations (Imprecise, omissions).**
    - Row "50–70 farmers | Smallest pilot groups in a few cases" loses the point. Source p. 287: these were the few trials without statistically robust differences. Replace context with: "Trial size in the few cases that did not show statistically robust differences between varieties".
    - Limitation "The individual, low-contact design weakens the group learning that motivates farmers in other participatory methods" adds a mechanism the source does not state. Source p. 282 says only that the individual approach makes extra motivating elements desirable. Replace with: "- The individual, low-contact design needs extra elements, such as blind trials, to keep farmers motivated."
    - Add these stated limitations:
      "- Many pilot farmers had prior PVS or participatory research experience, so reception by new communities is untested (p. 291)."
      "- Rankings alone cannot give effect sizes without direct measurements (p. 287)."
      "- iButton sensors were often stolen or displaced, poorly georeferenced by field agents, and readable only with a laptop, so they are not yet suitable at scale (p. 288, 291)."
      "- The accuracy check covered one Honduras pilot and four plant traits. Other crops and variables are needed to generalise (p. 284, 290)."
      "- The latest format's pairwise comparison with the farmer's local variety had not been evaluated (p. 286)."
    - Add Key numbers rows:
      `| 6–8 | Variables typically ranked per trial | This paper |`
      `| 37% | Adoption of selected rice varieties after diversity kits in Nepal | Joshi et al. 1997, cited in this paper |`
      `| ~25 / ~60 US$ | Cost of an iButton with temperature sensor only / with temperature and humidity | This paper |`
      `| 80 | iButton sensors on a coffee farm in Turrialba, Costa Rica (Figure 3) | Van Duijvendijk 2015, reproduced in this paper |`

13. **Replacement summary (492 words, ready to paste).** It fixes items 1, 4, 9, 10 and 11, removes the repeated last paragraph, and keeps all supported content.

    > This paper gives the first full account of tricot as a method, building on van Etten (2011), with early results from pilots run in 2013 to 2015. It positions tricot within participatory variety selection (PVS), mother-and-baby trials, informal research and development (IRD), and diversity kits. Farmer-participatory approaches have proved their value but are still not fully integrated into many R&D programmes. Group trials suffer from uneven participation and mother trials are costly, while IRD and diversity kits are cheap and hands-off.
    >
    > tricot combines elements of these approaches with crowdsourcing. Each farmer receives three varieties assigned by a design the researcher makes, grows them on their own farm, and ranks them on about six to eight aspects. Trials are blind, so farmers learn the variety names only at the end, which may reduce bias and motivate them to finish. Rankings from many small, independent trials are combined with the Bradley–Terry model. Geolocated trials could also be linked to environmental data. The small, individual task eases scaling but needs extra elements to keep farmers motivated.
    >
    > Crop pilots ran in India, East Africa (Kenya, Tanzania, Ethiopia) and Central America (Honduras, Guatemala, Nicaragua), with barley and durum wheat in Ethiopia, sorghum in Kenya and Tanzania, and common bean in Central America. They tested five aspects, from data formats and statistical design to gender inclusion. Early formats assumed too much literacy. Ranking three test varieties plus the local variety, with packages labelled 1, 2 and 3, caused confusion, and most farmers needed field agents to fill in forms, often after harvest. Later versions used the letters A, B and C, best and worst questions, short statements with pictures, and a sequentially balanced, randomized assignment of varieties.
    >
    > Trials showed statistically robust differences between varieties, except a few with only 50 to 70 farmers. In Nicaragua (157 participants), farmers' own local varieties ranked best overall and the iron-biofortified INTA Ferroso ranked worst. In Honduras, the farmers' consensus ranking always matched expert rankings, with early vigour judged most consistently and pest resistance least. Results also agreed well with group-based PVS run in parallel.
    >
    > Reception was positive. In November 2014, 96% of Indian participants and all participants in the Ethiopian and Honduran pilots wanted to continue. Farmers had diverse motives, including learning and contact with field agents. Women made up 42% of participants in Honduras, where CIAL farmer research groups had a gender focus, while in India participation rose after working through women's self-help groups. No trial found statistically significant differences in variety preferences between men and women. iButton sensors gave useful temperature data but were often stolen or displaced, so the authors judge them not yet suitable at scale.
    >
    > The authors see staff time, not seed or materials, as the main cost driver and expect unit costs to drop as more farmers join, but they give no cost figures. They announce ClimMob, a digital platform for tricot due to launch in 2016, and are investigating interactive voice response by phone.

14. **Notes additions (low).**
    - Add the Box 1 source issue (see Source issues).
    - Make the cross-reference dating clear: "The source cites the validity and motivation studies as Steinke et al. 2016 and Beza et al. 2016, both under review at the time. They were later published as steinke-2017-asd and beza-2017-plosone."
    - Suggested extra keywords (gives 11): add "Bradley–Terry model", "citizen science", "blind trials".

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | First experiences ... approach. Crowdsourcing ... (tricot) | Same, with a colon after "approach" (p. 275) | Supported (colon to period is expected) |
| authors | van Etten J ... Zimmerer KS (19 names) | Same 19 names in the same order (p. 275) | Supported |
| year | 2019 | Expl Agric (2019) 55(S1) (p. 275) | Supported |
| journal | Experimental Agriculture | Expl Agric. (p. 275) | Supported |
| article | 55(S1), 275-296 (first published online December 2016) | 55(S1), pp. 275–296, first published online 21 December 2016 (p. 275) | Supported |
| type | research article | Research paper with Results and Discussion | Supported |
| doi | 10.1017/S0014479716000739 | Same (p. 275) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution licence 4.0 (p. 275) | Supported |
| data | none | No data availability statement | Supported |
| crops | common bean, durum wheat, bread wheat, rice and others | barley, durum wheat, sorghum, common bean (p. 284) | Contradicted |
| region | Central America (Honduras, Nicaragua), Ethiopia, India, East Africa | India, Kenya, Tanzania, Ethiopia, Honduras, Guatemala, Nicaragua, Costa Rica (p. 284, 289) | Imprecise |
| gist | Lists topics | Should state findings | Imprecise |
| not_established | missing | Several clear limits exist (p. 285, 287, 291) | Missing |
| relations | extends vanetten-2011-idsbull | Further elaboration of Van Etten (2011) (p. 276, 280) | Supported |
| keywords | 8 terms | Bradley–Terry model, a central method, is not among them | Compliant, could improve |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | First full description of tricot, pilots run from 2011 | Contradicted | Testing done 2013–2015 (p. 277). 2011 is the proposal (p. 276, 280) | Fix 1 |
| 2 | Summary | Pilots ran under Seeds for Needs | Not in source | Name not in the paper | Outside knowledge. Move to Notes, labelled |
| 3 | Summary | Positions tricot within PVS, MBT, IRD, diversity kits | Supported | p. 278–279 | |
| 4 | Summary | Hard to integrate because they need intensive facilitation | Imprecise | p. 276 gives no cause. IRD and diversity kits are hands-off and cheap (p. 279) | Fix 9 |
| 5 | Summary | tricot combines these with crowdsourcing | Supported | p. 280 | |
| 6 | Summary | Three random varieties, own farm, few simple questions | Supported | p. 280–281, 287 | About 6 to 8 variables (p. 280–281) |
| 7 | Summary | Aggregated statistically, linked to geographic and climate data | Imprecise | p. 282 "could produce". Abstract lists environmental analysis as open (p. 276) | Fix 11. Bradley–Terry not named |
| 8 | Summary | Minimal, individual task scales but needs motivation effort | Supported | p. 275, 282 | |
| 9 | Summary | Pilots tested five aspects | Supported | p. 283–284 | |
| 10 | Summary | Early formats assumed too much literacy | Supported | p. 285 | |
| 11 | Summary | 3 varieties plus local, labels 1 2 3, confusion | Supported | p. 285 | |
| 12 | Summary | Most farmers needed field agents, often after harvest | Supported | p. 285 | |
| 13 | Summary | Later versions: letters, best/worst, sequentially balanced design | Supported | p. 285, 287 | Third iteration (short statements, pictures) missing |
| 14 | Summary | Reception was positive | Supported | p. 289 | |
| 15 | Summary | Nov 2014: 96% India, 100% Ethiopia and Honduras | Supported | p. 289 | |
| 16 | Summary | 42% women in Honduras (CIAL), India via self-help groups | Supported | p. 289–290 | |
| 17 | Summary | Expert comparison supports validity, plants easier than pests and diseases | Supported | p. 288, 290 | Source is stronger: consensus "invariably matched" |
| 18 | Summary | Staff time drove cost, unit costs fell | Imprecise | p. 292 "major driver", "tend to drop", no data | Fix 11 |
| 19 | Summary | Announce ClimMob, plan IVR | Supported | p. 293 | Source says "investigating" IVR |
| 20 | Summary | Draws on crowdsourcing, ethnobiology, environmental analysis | Supported | p. 277–280 | |
| 21 | Summary | Diversity kits informed the triadic design | Imprecise | p. 281: original justification was Martin (2004) | Fix 10 |
| 22 | Summary | Authors anticipate IVR (press a key) | Supported | p. 293 | Repeats claim 19 |
| 23 | Methods | Incomplete blocks of three, sequentially balanced, randomized labels | Supported | p. 286–287 | |
| 24 | Methods | Best/worst rankings, collected by field agents or phone | Imprecise | Phone not used in the pilots (p. 285) | Fix 8 |
| 25 | Methods | Aggregated statistically with environmental covariates | Imprecise | Bradley–Terry (p. 282–283). Covariates not reported | Fix 3 |
| 26 | Methods | Crop trials in several countries plus one weather pilot | Supported | p. 284 | Add countries, years, sensor count |
| 27 | Limitations | Early formats too complex, needed field-agent help | Supported | p. 285 | |
| 28 | Limitations | Individual design weakens group learning that motivates | Imprecise | p. 282 says only extra motivating elements are desirable | Fix 12 |
| 29 | Limitations | Women's participation depends on recruitment channels | Supported | p. 291 | |
| 30 | Limitations | Results in grey literature, peer-reviewed follow-ups to come | Supported | p. 284 | |
| 31 | Key numbers | 2011, start of pilots under Seeds for Needs | Contradicted | p. 277 | Fix 1 |
| 32 | Key numbers | 157 participants, Nicaragua postrera 2015 | Supported | Figure 2 caption (p. 287) | |
| 33 | Key numbers | 96% / 100% | Supported | p. 289 | |
| 34 | Key numbers | 42% women, Honduras | Supported | p. 289–290 | |
| 35 | Key numbers | 50–70 farmers, smallest pilot groups | Imprecise | p. 287: the cases without robust differences | Fix 12 |
| 36 | Key numbers | 2016, ClimMob launch | Supported | p. 293 | |
| 37 | Notes | Online 2016, volume 2019 | Supported | p. 275 | |
| 38 | Notes | Validity and motivation detailed in later cards | Supported | p. 284–285 cite Steinke 2016, Beza 2016 | Add dating note (fix 14) |

Metadata claims (13) are in the Metadata check table: 10 Supported, 2 Imprecise (region, gist), 1 Contradicted (crops). Totals across both tables: 51 claims, 37 Supported, 10 Imprecise, 1 Not in source, 3 Contradicted.

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Box 1 worked example gives λB = −0.29. With λA = 0 and 0.75 = 1/(1 + e^λB), the correct value is λB = −ln 3 ≈ −1.10. The printed −0.29 equals ln(0.75) (reviewer's calculation) | Box 1, p. 283 (PDF p. 9) | No | "Box 1's worked example has an arithmetic error. With λA = 0 and P(A beats B) = 0.75, λB should be −ln 3, about −1.10, not −0.29 as printed (our calculation). The printed value equals ln(0.75)." |
| Figure 3 caption repeats "Figure 3." mid-sentence | p. 289 (PDF p. 15) | No | Not needed (typo only) |
| Reference list: Snapp (2002) is given the same page range as Coe (2002), 44–65. The motivation study is cited as Beza et al. 2016 and as "submitted" | p. 284–285, 294–295 | No | Not needed (low importance) |

## Completeness

| Item in the source | In card? | Importance | Suggested addition |
|---|---|---|---|
| Two aims: present the approach, separating validated and novel elements, and bring early findings together (p. 277) | Partly | Medium | Covered in replacement summary sentence 1 |
| Testing period 2013–2015 (p. 277) | No (wrong year given) | High | Fix 1 |
| Countries and crops of pilots (p. 284) | Partly, with errors | High | Fixes 2, 7, 13 |
| Bradley–Terry model and Box 1 (p. 282–283) | No | High | Fix 3 |
| No significant gender differences in preferences in any trial, and the hypothesis that group methods may create apparent gender differences (p. 290, 292) | No | High | In replacement summary. The hypothesis could go in Notes |
| Robust differences except trials with 50 to 70 farmers. Effect sizes not estimable (p. 287) | No | High | In replacement summary and limitations |
| Weather-sensor results: useful accuracy, but theft, displacement, poor georeferencing, laptop needed. Not yet suitable at scale. CHIRPS as alternative (p. 288, 291) | No | High | In replacement summary and limitations |
| Blind trials as a novel feature (p. 281–282) | No | Medium | In replacement summary |
| Nicaragua results: local variety best with narrow CI, INTA Ferroso worst (p. 287–288, Figure 2) | No | Medium | In replacement summary |
| High agreement with parallel group PVS in East Africa and India (p. 288) | No | Medium | In replacement summary |
| Farmer motives: learning, social interaction, contact with field agents (p. 289) | No | Medium | In replacement summary |
| Prior PVS exposure of pilot farmers as stated limitation (p. 291) | No | Medium | Fix 12 |
| Third format iteration: ultra-short statements and pictures (p. 285, Figure 1) | No | Medium | In replacement summary |
| Simple randomization caused imbalance between communities, which led to the sequentially balanced design (p. 286–287) | Partly | Medium | Add to Design bullet: "Simple randomization left some varieties rare or absent in single communities, so the pilots moved to a sequentially balanced design." |
| Ranking instead of scoring, so no scales or training are needed (p. 281) | No | Low | Optional |
| Future directions: data-quality filtering, gamification, other technologies, two-sided market business model (p. 293–294) | No | Low | Optional, Notes |

## Template compliance

| Check | Result |
|---|---|
| Summary word count | 430 (within 400 to 500). The replacement summary is 492 |
| Gist length | 29 words (under 30), but lists topics. Replacement is 28 words |
| Keywords | 8 (within 8 to 12). Suggest adding 3 |
| Questions | 5 (within 4 to 7). "What drives the cost of tricot?" is answered only by one general sentence in the source |
| House style | tricot written in lowercase throughout. No em dashes or semicolons in card prose |
| not_established | Missing (fix 6) |
