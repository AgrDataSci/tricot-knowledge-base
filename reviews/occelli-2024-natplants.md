# Card review: occelli-2024-natplants

- **Card:** papers/occelli-2024-natplants.md
- **Source:** papers-pdf/occelli-et-al-2024b.pdf (18 pages)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Major fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 59 |
| Supported | 47 |
| Imprecise | 10 |
| Not in source | 0 |
| Contradicted | 2 |
| Important omissions | 7 |
| Metadata issues | 1 |

The card is accurate on almost every number, and the screening arithmetic checks out. The main problem is the claim that matters most for a tricot user. The card says twice that the review puts tricot under "direct experience", but Fig. 2 puts tricot inside the "Questions" (direct questions) category. Fixing the summary sentence and the tricot note is the most important change. The other fixes are small wording corrections and a few useful additions.

Page numbers below give the journal page and the PDF page, for example p. 404 (PDF 3). PDF pages 11 to 15 hold the Extended Data figures. PDF pages 16 to 18 hold the Nature Portfolio Reporting Summary, which has no text layer and was read as images.

**Pre-check numbers.** Both numbers are in the source, in a slightly different form:
- "49.5%" appears as "the median is 49.50%" in the Fig. 4 legend, with "the sample is 216 studies" (p. 406, PDF 5). The first quartile is 32% and the third quartile is 57%. The card row is Supported.
- "R 4.2.3" appears as "R (v.4.2.3)" in Methods, Data synthesis (p. 409, PDF 8), and as "R (version 4.2.3)" in the Reporting Summary (PDF 16). Supported.

## Fixes needed

1. **tricot is not under "direct experience" (Contradicted, summary paragraph 4).**
   Card: "Direct experience, such as PVS, demonstration plots and on-farm trials including tricot, comes second (24%)."
   Source: the text lists PVS and demonstration plots under direct experience (p. 403, PDF 2). In Fig. 2 (p. 404, PDF 3) "Tricot" is a very thin slice in the outer ring, coloured like the Questions category, between "Preference voting" and "Auction". The Experience category holds Demo plots, Field visit, On farm trial, On station trial, Other and PVS. I checked this on a 300 dpi crop of the figure.
   Replace with:
   "Direct experience, such as PVS, demonstration plots and on-farm trials, comes second (24%). In Fig. 2, tricot is a very small slice inside the direct questions category, not under direct experience."

2. **Same error in Notes, and the tricot count is not fully absent (Contradicted and Imprecise, Notes bullet 2).**
   Card: "tricot appears only as one tool among 21 under 'direct experience'. The review does not report how many studies used tricot."
   Source: Fig. 2 places tricot under Questions (p. 404, PDF 3). The Fig. 2 legend says full frequencies per category are in Supplementary Table 1, which is not in our PDF. The Discussion cites the first tricot paper (ref. 38, van Etten et al. 2019, Exp. Agric.) twice: direct elicitation "has been shown to produce questionable results", and on-farm testing "(direct experience)" may partly avoid these biases (p. 408, PDF 7). So the paper itself is not consistent about where tricot belongs.
   Replace with:
   "- In Fig. 2, tricot is one of 21 tools. It appears as a very thin slice inside the direct questions category, next to preference voting, not under direct experience. The main text gives no count of tricot studies. Supplementary Table 1 (not in our PDF) gives the frequency of each tool. The Discussion cites the first tricot paper (ref. 38, see vanetten-2019-expagric) twice: as evidence that direct elicitation gives questionable results, and as an example of on-farm testing (direct experience) that may reduce these biases. So the paper is not consistent about where tricot belongs."

3. **Key numbers row "58% / 24% / 7.4%" mixes two kinds of share (Imprecise).**
   Card context: "Studies eliciting traits by direct questions, direct experience, choice tools".
   Source: the text calls 58% and 24% shares of studies (p. 403, PDF 2). The 7.4% only appears in Fig. 2 (p. 404, PDF 3), where the four categories are 58.0%, 24.2%, 7.4% and 10.5% (Other). These four add up to 100%, although many studies use more than one tool. So they behave like shares of tool mentions, not of studies.
   Replace the row with:
   "| 58.0% / 24.2% / 7.4% / 10.5% | Shares of the four tool categories in Fig. 2: direct questions, direct experience, choices, other. The four add up to 100%, so they are shares of tool mentions, although the text calls 58% and 24% shares of studies | This paper |"

4. **The ~250 respondents and "habit" are linked more tightly than the paper does (Imprecise, summary paragraph 5).**
   Card: "Studies cluster around 250 respondents regardless of crop, country or method, which the authors read as habit rather than power calculation."
   Source: the paper describes a "normalized approach of sampling roughly 250 respondents" (p. 404, PDF 3). The "habit and practicality" remark is a separate, general point about overlooked sample size calculations (p. 406, PDF 5). It is not tied to the 250 figure. Extended Data Fig. 2 (PDF 12) shows a wide spread, up to about 6,000 farmers, by crop and year only.
   Replace with:
   "Many studies sample roughly 250 respondents regardless of crop, country or method. The authors add that sample size calculations were often overlooked, which may point to sampling by habit and practicality rather than robust design."

5. **Authorship and novelty claim overstated (Imprecise, summary paragraph 1).**
   Card: "Martina Occelli, Hale Ann Tufan and colleagues at Cornell University asked what tools and methods have underpinned trait prioritization studies, a question that had not been examined across crops and regions."
   Source: the paper gives "M. Occelli" only. The first name is not in the source. Hale Ann Tufan appears in the Reporting Summary (PDF 16). Most authors are at Cornell, but others are at IFPRI, Notre Dame and CIFOR-ICRAF (p. 402, PDF 1). The paper says the methods "are seldom examined", and an earlier rice-only review lacked focus on tools (p. 403, PDF 2). It does not say the question was never examined.
   Replace with:
   "M. Occelli, H. A. Tufan and colleagues, most of them at Cornell University, asked what tools and methods underpin trait prioritization studies. The authors say these methods are seldom examined, and an earlier review of stakeholder preference studies covered rice only."

6. **Methods "Design" bullet: the whole search was not rerun (Imprecise).**
   Card: "search rerun 23 June 2023 after peer review."
   Source: after reviewer input, the search was "broadened and updated" (p. 408, PDF 7). The final scholarly database searches were on 23 June 2023. Grey literature was searched from 12 March to 6 July 2022 (p. 409, PDF 8).
   Replace with:
   "- **Design.** Systematic scoping review under PRISMA-ScR. Protocol registered 11 March 2022 and finalized on OSF 8 July 2022. After peer review the search was broadened, and the scholarly databases were searched again on 23 June 2023. Grey literature was searched from 12 March to 6 July 2022."

7. **"52%" sentence drops "exclusively" (Imprecise, summary paragraph 5).**
   Source: 52% "exclusively involve farmers" without saying if they are also consumers or producers (p. 404, PDF 3).
   Replace the sentence with:
   "12% do not report how many people took part, 52% involve only farmers without saying whether they are also consumers or producers, and fewer than 19% include consumers, traders or other seed system actors."

8. **"A third" should be "more than a third" (Imprecise, summary paragraph 4).**
   Source: "More than a third of the studies report using only one tool", and another third use two (p. 404, PDF 3).
   Replace "A third of studies use a single tool." with:
   "More than a third of studies use a single tool, and another third use two."

9. **Gist wording (Imprecise).**
   "little sex-disaggregation" understates 37% of studies. The abstract says "lack of systematic sex disaggregation" (p. 402, PDF 1). The gist also leaves out uneven crop and regional coverage, which is a headline finding of the abstract.
   Replace with (28 words):
   "Scoping review of 657 trait prioritization studies finds uneven crop and regional coverage, weak sampling, unsystematic sex disaggregation and no shared trait taxonomy, so findings cannot be compared"

10. **English-only limitation lacks the authors' counterpoint (Imprecise, Stated limitations bullet 1).**
    Source: the bias "may reflect" the English-only choice, but similar gaps appear in reviews that did include Spanish-language studies (p. 406, PDF 5).
    Replace with:
    "- English-language studies only, which may explain part of the South American gap. The authors note that reviews which included Spanish-language studies found a similar gap."

11. **"incompatible lists" is stronger than the source (Imprecise, summary paragraph 6).**
    Source: the three studies "yielded separate trait priority lists" despite shared authorship and methods (p. 405, PDF 4).
    Replace with:
    "Trait descriptions vary so much that three Indian rice studies, with shared authors and similar methods, produced three different trait priority lists."

12. **Add high and medium omissions (see Completeness).** Ready-to-paste text:
    - End of summary paragraph 1: "They hypothesized that weak attention to methods produces poor, biased data and stops breeding programmes from making data-driven decisions."
    - End of summary paragraph 3: "Cereal, legume and RTB studies are almost all (96%) in South Asia, sub-Saharan Africa and South America, while 59% of fruit and vegetable studies are in North America and Europe."
    - Summary paragraph 5, after the 90% / 12.5% sentence: "Participation varies by crop: 54% of cereal studies are participatory, against 51% for legumes, 41% for RTB and 14% for vegetables and fruits. The authors warn that weak respondent sampling could give breeders misleading and unrepresentative results."
    - Summary paragraph 6, before the rice sentence: "High yield ranks high overall but less so in RTB and in vegetables and fruits. Taste ranks high in RTB, and early maturity, pest and disease resistance and drought tolerance have gained importance in cereals."
    - New Notes bullet: "- The paper does not say which denominator (564 or 657) each percentage uses. Fig. 4b uses 216 sex-disaggregated studies, which is 38% of 564, close to the 37% in the text."

13. **Questions section, item 2 (optional).** The card cannot answer "how often are on-farm trials or tricot used" for tricot. Replace with:
    "- Which tools are used most to elicit trait priorities, and where do on-farm trials and tricot fit?"

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | A scoping review on tools and methods for trait prioritization in crop breeding programmes | Same (p. 402, PDF 1) | Supported |
| authors | Occelli M, Mukerjee R, Miller C, Porciello J, Puerto S, Garner E, Guerra M, Gomez MI, Tufan HA | Same nine authors, same order (p. 402, PDF 1) | Supported |
| year | 2024 | Published online 22 February 2024, March 2024 issue (p. 402, PDF 1) | Supported |
| journal | Nature Plants | Nature Plants (p. 402, PDF 1) | Supported |
| article | 10, 402-411 | Volume 10, March 2024, 402 to 411 (footer, every page) | Supported. The PDF gives no issue number, so the template's "(issue)" cannot be checked here |
| type | review | Scoping review published as an Article (p. 402, p. 408) | Supported |
| doi | https://doi.org/10.1038/s41477-024-01639-6 | Same (header, every page) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution 4.0 (p. 411, PDF 10) | Supported |
| data | GitHub TufanLab/trait-priority-scoping-review, OSF ayw8q | Data and code on that GitHub repo (p. 410, PDF 9). Protocol at osf.io/ayw8q (p. 408, PDF 7) | Supported |
| crops | cereals, legumes, roots, tubers and bananas, vegetables and fruits | Four crop groups. Commodity and ornamental crops (3%) excluded (p. 409, PDF 8) | Supported |
| region | global (57% of studies in sub-Saharan Africa) | 57% in sub-Saharan Africa (p. 403, PDF 2) | Supported |
| source | external | No author is listed in people.md | Supported |
| gist | 29 words, see fix 9 | Abstract (p. 402, PDF 1) | Imprecise |
| not_established | Four items | All four are fair. The paper maps tool use and does not test validity. The claim about direct questions rests on ref. 38 (p. 408). The paper criticizes the 250 norm (p. 404, p. 406). It warns that trait lists cannot be pooled (p. 405) | Supported |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Frontmatter | gist | Imprecise | p. 402 (PDF 1) | See fix 9 |
| 2 | Frontmatter | not_established | Supported | p. 404, 405, 406, 408 | Fair. Optional addition: "how common tricot is in trait studies (no tricot count in the main text)" |
| 3 | Frontmatter | crops | Supported | p. 409 (PDF 8) | |
| 4 | Frontmatter | region | Supported | p. 403 (PDF 2) | |
| 5 | Frontmatter | data | Supported | p. 408, 410 | |
| 6 | Frontmatter | license | Supported | p. 411 (PDF 10) | |
| 7 | Frontmatter | article | Supported | footer | Issue number not in PDF |
| 8 | Frontmatter | authors | Supported | p. 402 (PDF 1) | |
| 9 | Summary P1 | Programmes becoming demand-led, product profiles | Supported | p. 402 (PDF 1) | |
| 10 | Summary P1 | Martina Occelli, Tufan, Cornell, question not examined | Imprecise | p. 402, 403 | First name not in source. "Seldom examined", not "not examined". See fix 5 |
| 11 | Summary P2 | PRISMA-ScR, OSF, 5 databases, 12 grey sources, no date limit, English only | Supported | p. 408 (PDF 7) | |
| 12 | Summary P2 | 17,786 records to 657 studies, 40-question framework | Supported | p. 409 (PDF 8), Fig. 6 | |
| 13 | Summary P2 | 564 original studies, 83% peer-reviewed, over half since 2016 | Supported | p. 403 (PDF 2) | |
| 14 | Summary P3 | Coverage is uneven | Supported | p. 402, 403 | |
| 15 | Summary P3 | Ethiopia and India most, 57% / 6% / 2% | Supported | p. 403 (PDF 2) | |
| 16 | Summary P3 | Cereals dominate, RTB and fruits and vegetables get less attention | Supported | p. 406 (PDF 5) | |
| 17 | Summary P4 | 58% use direct questions (surveys, focus groups) | Supported | p. 403 (PDF 2) | See row 50 on the denominator |
| 18 | Summary P4 | Direct experience incl. tricot, 24% | Contradicted | Fig. 2, p. 404 (PDF 3) | tricot sits under Questions. See fix 1 |
| 19 | Summary P4 | Analysis mostly frequency counts and hypothesis tests | Supported | p. 404, Fig. 3 p. 405 | Fig. 3: descriptive 33.0%, hypothesis testing 29.3% |
| 20 | Summary P4 | 5% qualitative analysis, focus groups common | Supported | p. 404 (PDF 3) | Fig. 3 shows 4.81% |
| 21 | Summary P4 | A third use a single tool | Imprecise | p. 404 (PDF 3) | "More than a third". See fix 8 |
| 22 | Summary P5 | Designs are weak | Supported | p. 406 (PDF 5) | |
| 23 | Summary P5 | 12% do not report respondent number | Supported | p. 404 (PDF 3) | |
| 24 | Summary P5 | 52% engage farmers without saying producers or consumers | Imprecise | p. 404 (PDF 3) | Drops "exclusively". See fix 7 |
| 25 | Summary P5 | Fewer than 19% include consumers, traders, seed actors | Supported | p. 404 (PDF 3) | |
| 26 | Summary P5 | ~250 respondents, read as habit | Imprecise | p. 404, p. 406, Ext. Data Fig. 2 (PDF 12) | Habit remark is general, not tied to 250. See fix 4 |
| 27 | Summary P5 | 90% formal-led, 12.5% own fields and management | Supported | p. 404 (PDF 3) | 12.5% are "formal-led collaborative" trials, as the Key numbers row says |
| 28 | Summary P6 | 37% sex-disaggregated, 1.7% intrahousehold | Supported | p. 404, 405 | |
| 29 | Summary P6 | 84% find differences, stereotyped roles | Supported | p. 405 (PDF 4) | |
| 30 | Summary P6 | 0.9% disaggregate by age | Supported | p. 405 (PDF 4) | |
| 31 | Summary P6 | Three Indian rice studies, incompatible lists | Imprecise | p. 405 (PDF 4) | Source says "separate" lists. See fix 11 |
| 32 | Summary P6 | ~10 isolated clusters, 5 donors fund nearly half | Supported | p. 406 (PDF 5) | |
| 33 | Summary P7 | Four recommendations | Supported | p. 408 (PDF 7) | |
| 34 | Summary P7 | On-farm and video testing may avoid some biases | Supported | p. 408 (PDF 7) | Source says "partially circumvent". On-farm testing cites the tricot paper (ref. 38) |
| 35 | Methods | Design: dates, search rerun | Imprecise | p. 408, 409 | Search broadened, only databases searched again. See fix 6 |
| 36 | Methods | Sources: 5 databases, 12 grey sources | Supported | p. 408, 409 | |
| 37 | Methods | Screening numbers, Covidence, peer screening | Supported | p. 409, Fig. 6 p. 408, PDF 18 | Arithmetic checks: 17,786 minus 5,808 = 11,978. 11,978 minus 10,653 = 1,325. 1,325 minus 668 = 657. Exclusion reasons add up to 668 |
| 38 | Methods | 40-question framework, variables, formal-led / farmer-led, consultative / collaborative | Supported | p. 404, p. 409 Table 1 | |
| 39 | Methods | R 4.2.3, VOSviewer, four crop groups, 3% excluded | Supported | p. 409 (PDF 8), PDF 16 | |
| 40 | Limitations | English only may explain South American gap | Imprecise | p. 406 (PDF 5) | Authors also give a counterpoint. See fix 10 |
| 41 | Limitations | Multiple categories, double counting | Supported | Table 1 footnote, p. 409 | |
| 42 | Limitations | Sample size calculations may be unreported | Supported | p. 406 (PDF 5) | |
| 43 | Limitations | Donor and policy drivers need further analysis | Supported | p. 406 (PDF 5) | |
| 44 | Key numbers | 17,786 / 11,978 / 1,325 / 657 | Supported | p. 409, Fig. 6 | |
| 45 | Key numbers | 564, 83% / 17% | Supported | p. 403 (PDF 2) | |
| 46 | Key numbers | 57% / 6% / 2% | Supported | p. 403 (PDF 2) | |
| 47 | Key numbers | 58% / 24% / 7.4% as shares of studies | Imprecise | p. 403, Fig. 2 p. 404 | 7.4% is only in Fig. 2, where shares sum to 100%. See fix 3 |
| 48 | Key numbers | 5% qualitative | Supported | p. 404 (PDF 3) | |
| 49 | Key numbers | 12% no respondent number | Supported | p. 404 (PDF 3) | |
| 50 | Key numbers | ~250 typical respondents | Supported | p. 404 (PDF 3) | Ext. Data Fig. 2 splits by crop and year only, not country or method |
| 51 | Key numbers | 90% / 12.5% | Supported | p. 404 (PDF 3) | |
| 52 | Key numbers | 37% / 84% | Supported | p. 404, 405 | |
| 53 | Key numbers | 1.7% / 0.9% | Supported | p. 405 (PDF 4) | |
| 54 | Key numbers | 49.5% median women share, 216 studies | Supported | Fig. 4 legend, p. 406 (PDF 5) | Printed as "49.50%". IQR 32% to 57% could be added |
| 55 | Key numbers | 25% sex-disaggregated, Weltzien et al. 2019 (ref. 14) | Supported | p. 403 (PDF 2), ref. 14 p. 410 | Primary source column is correct |
| 56 | Key numbers | ~10 clusters / 5 donors | Supported | p. 406 (PDF 5) | |
| 57 | Notes | 657 in abstract and Fig. 6, 564 in results | Supported | p. 402, 403, 408 | The paper does not explain the gap. Inclusion allowed reviews (p. 408), which may explain part of it, but the paper does not say so |
| 58 | Notes | tricot is under "direct experience" | Contradicted | Fig. 2, p. 404 (PDF 3) | See fix 2 |
| 59 | Notes | Review does not report how many studies used tricot | Imprecise | Fig. 2 legend, p. 404 | True for main text. Supplementary Table 1 has frequencies but is not in our PDF. See fix 2 |

## Completeness

| Item in the source | In card? | Importance (high / medium / low) | Suggested addition |
|---|---|---|---|
| Aim and guiding question (p. 403, p. 408) | Yes | high | None |
| Authors' hypothesis: weak attention to methods causes poor, biased data (p. 403) | No | medium | Fix 12, paragraph 1 sentence |
| Design: PRISMA-ScR scoping review, 5 databases, 12 grey sources | Yes | high | None |
| Sample sizes: 17,786 / 11,978 / 1,325 / 657 / 564 | Yes | high | None |
| Where tricot sits in Fig. 2 (Questions, tiny slice) | Wrong | high | Fixes 1 and 2 |
| Discussion cites the tricot paper (ref. 38) for both the direct-question problem and on-farm testing (p. 408) | No | high | Fix 2 text |
| Fig. 2 category shares sum to 100% (tool mentions, not studies) | No | medium | Fix 3 |
| Participation by crop group: cereals 54%, legumes 51%, RTB 41%, fruits and vegetables 14% (p. 404) | No | medium | Fix 12, paragraph 5 sentence |
| Trait trends: yield, taste, pest and disease, drought, early maturity by crop group (p. 405, Ext. Data Fig. 3) | No | medium | Fix 12, paragraph 6 sentence |
| Crop by region split: 96% of RTB, cereal and legume studies in South Asia, sub-Saharan Africa, South America, 59% of fruit and vegetable studies in North America and Europe (p. 403) | No | medium | Fix 12, paragraph 3 sentence |
| Authors' warning that weak sampling may give misleading, unrepresentative results (p. 406) | No | medium | Fix 12, paragraph 5 sentence |
| Authors conflate "participation" with "participatory", consultative engagement only (p. 408) | No | low | Optional: "Many studies call themselves participatory but only consult end users." |
| Disaggregation by region 37%, region and gender 3% (p. 405) | No | low | Optional Key numbers row |
| Sex-disaggregated studies more recent (median year 2016 vs 2012), more women in fruit and vegetable studies, fewer in legumes (p. 404, 405) | No | low | Optional |
| 70% of studies explain sex differences with literature (40%), qualitative (31%) or quantitative (25%) methods (p. 405) | No | low | Optional |
| Mixed methods 13% and 6%, peer-reviewed median two tools vs one in grey literature (p. 404) | No | low | Optional |
| Stated limitations: English only, double counting, unreported sample size calculations, donor drivers | Yes | high | Fix 10 adds the counterpoint |
| Conclusions and four recommendations (p. 408) | Yes | high | None |
| Small inconsistencies in the paper: Ext. Data Fig. 3 caption says "six" traits but lists seven (PDF 13). Table 1 cites ref. 23 (a phenomics paper) for the formal-led / farmer-led framework, which may be meant as ref. 44, Sperling et al. 2001 (p. 409) | No | low | Optional Notes bullet: "Ext. Data Fig. 3 caption says six traits but lists seven. Table 1 cites ref. 23 for the participation framework, which looks like a citation error (check ref. 44)." |

## Template compliance

- **Summary word count:** 404 words (target 400 to 500). Compliant but near the lower limit. The fixes and additions above add about 110 words, which keeps it under 500.
- **Gist length:** 29 words (under 30). Compliant. The proposed replacement has 28 words.
- **Keyword count:** 11 (target 8 to 12). Compliant.
- **Questions count:** 6 (target 4 to 7). Compliant. Question 2 asks how often tricot is used, which the card cannot answer. See fix 13.
- **House style:** tricot is lowercase throughout. maniva does not appear. The card has no em dashes or semicolons in its prose. The not_established field uses semicolons as separators, which the template requires.
- **Frontmatter:** all required fields present. curated_card is "no", as expected before curation. The article field has no issue number, and the PDF does not give one.
- **Notes cross-references:** all named card ids exist in papers/. Consider adding vanetten-2019-expagric, the paper cited as ref. 38.
