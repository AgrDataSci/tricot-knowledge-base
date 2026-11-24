# Card review: arnaud-2023-jsfa

- **Card:** papers/arnaud-2023-jsfa.md
- **Source:** papers-pdf/arnaud-et-al-2023.pdf (13 pages, printed pages 4514 to 4526. PDF page = printed page minus 4513)
- **Reviewed:** 2026-11-20, by an independent agent (pilot)
- **Verdict:** Minor fixes

## Overview

| Check | Result |
|---|---|
| Claims checked | 47 |
| Supported | 35 |
| Imprecise | 11 |
| Not in source | 1 |
| Contradicted | 0 |
| Source issues (problems in the source itself, not card errors) | 6 |
| Important omissions | 8 |
| Metadata issues | 5 |

The card describes the RTBfoods data workflow accurately, and every number it gives matches the paper. It also correctly flags the broken percentage column in Table 9. The most important fix is the gist, which says consumer data link to genotypes in Breedbase. The paper says the opposite: survey data with personal information went to a separate repository, and only sensory, lab and NIRS data were linked to plant records (p. 4514 abstract, PDF p. 2). The second fix is that the Summary (362 words, below the 400 minimum) leaves out the paper's main results: 163 sensory traits, 78 biophysical traits, 21,844 NIRS spectra and 13 gendered food product profiles.

## Fixes needed

1. **Gist (Imprecise, main point).** The card says SOPs, templates and Crop Ontology traits "let consumer, sensory, lab and NIRS data ... link to genotypes in Breedbase". The abstract says biochemical, texture and sensory data are connected to the plant record, while user survey data were anonymised and uploaded in a repository (p. 4514, PDF p. 2). The link from gendered food product profiles to target product profiles in Breedbase is shown as a planned flow (Fig. 5, p. 4521, PDF p. 8), and the paper says TPPs still "need to be integrated" (p. 4524, PDF p. 11). Replace with (29 words):

   `gist: RTBfoods used SOPs, data templates and Crop Ontology food quality traits to link sensory, lab and NIRS data to genotypes in Breedbase, with anonymized survey data in a repository`

2. **Summary is missing the main results and is too short (Omission, high).** The Summary has 362 words and gives no result counts. The paper reports 163 sensory traits in the Crop Ontology and crop databases (Table 6, p. 4522, PDF p. 9), 78 biophysical traits for six products (p. 4522), 21,844 NIRS spectra in CassavaBase and YamBase (p. 4522), 13 GFPPs in an open Dataverse repository (p. 4520, PDF p. 7), and processing-trial data not yet in Breedbase (p. 4522). Replace the sentence "The authors report that partner breeding programmes measured more quality traits after RTBfoods began in 2018." with the two paragraphs below. Together with fixes 3, 5 and 9, this brings the Summary to about 497 words.

   "In total, 163 sensory traits for ten food products went into the Crop Ontology and the crop databases. Teams also measured 78 biophysical traits for six products, and uploaded 21,844 NIRS spectra of cassava and yam to CassavaBase and YamBase. Processing-trial data were not yet in Breedbase, because teams still had to agree how to show processing steps shared by many products, such as boiling.

   The authors report that partner breeding programmes recorded more quality traits after RTBfoods began in 2018. In their before-and-after count (Table 9), quality traits rose in five of six programmes, for example from 25 to 34 at IITA and from 9 to 63 at CIAT (both cassava), but fell from 9 to 7 at NRCRI (cassava)."

3. **Summary, Table 9 sentence (Imprecise).** The card states without qualification that programmes "measured more quality traits". The authors do claim this in their lessons (p. 4525, PDF p. 12), but Table 9 shows NRCRI cassava fell from 9 to 7, the periods before and after 2018 differ greatly in length, there is no comparison group, and the counts are traits recorded in the databases. The replacement text in fix 2 covers this. Also add to not_established (see fix 4).

4. **not_established (incomplete).** The three current items are correct. Add the two most likely stretches: that RTBfoods caused the rise in quality traits, and that consumer survey data sit in Breedbase. Replace the field with:

   `not_established: that more quality traits in breeding databases led to more adopted varieties; that RTBfoods caused the rise in quality traits (Table 9 is a before-and-after count with periods of different length, no comparison group, and one programme, NRCRI cassava, fell from 9 to 7); that consumer survey data or gendered food product profiles are stored in or linked to genotypes in Breedbase (they are in a separate repository); that participatory processing-trial data are in Breedbase (not yet uploaded at the time of writing); that tricot data were part of this integration (the paper does not mention tricot); the percentage changes in Table 9 (see Notes)`

5. **Summary, survey data sentence (Imprecise).** The card says survey data "were anonymized and placed in an open Dataverse repository". The abstract says only "uploaded in a repository" (p. 4514). Fig. 5 shows survey data first stored with restricted access (p. 4521, PDF p. 8). The paper names Dataverse only for the 13 GFPPs (p. 4520, PDF p. 7). Replace with:

   "Survey data containing personal information were anonymized and kept in a repository instead, and 13 gendered food product profiles are in an open Dataverse repository."

6. **Frontmatter authors (Imprecise).** The card lists 14 names "and 12 co-authors" (26 in total). The byline has 25 authors, so 11 remain after the 14 listed (p. 4514, PDF p. 1). Replace with:

   `authors: Arnaud E, Menda N, Tran T, Asiimwe A, Kanaabi M, Meghar K, Forsythe L, Kawuki R, Ellebrock B, Kayondo IS, Agbona A, Zhang X, Mendes T, Laporte MA, and 11 co-authors`

7. **Key numbers, "≥8" row (Imprecise, attribution).** The paper takes this from the RTBfoods sensory manual (ref. 12, Maraval et al. 2018) and adds that at least ten is "highly desirable" (p. 4518, PDF p. 5). Replace the row with:

   `| ≥8 (≥10 preferred) | Recommended minimum number of trained sensory panellists, with equal numbers of men and women aged 18 to 60 | RTBfoods sensory manual (Maraval et al. 2018), cited in this paper |`

   And add these rows for the main results:

   `| 163 | Sensory traits from trained panels for ten food products, put into the Crop Ontology and crop databases (Table 6) | This paper |`
   `| 78 | Biophysical traits measured by lab protocols for six products: boiled cassava 10, fufu 13, eba 13, pounded yam 13, boiled yam 15, boiled plantain 14 | This paper |`
   `| 21,844 | NIRS spectra of fresh grated cassava roots and fresh or boiled yam tubers uploaded to CassavaBase and YamBase | This paper |`
   `| 13 | Gendered food product profiles in an open Dataverse repository | This paper |`

8. **Stated limitations (incomplete, and one Imprecise item).** The second bullet says "method types" complicate harmonization. The paper says the problems were inconsistent naming and classification of attributes and different scales (p. 4522, PDF p. 9). "Method type" is a template field the teams filled (Measurement or Estimation), not a stated problem. Also, several of the authors' own limitations are missing. Replace the section with:

   "- Sensory traits, variables and scales differ by product and country, so cross-country comparison needs care.
   - Early lexicons named and classified attributes inconsistently and used different scales (0-10, 0-100), so several variable names were needed for one trait and method.
   - Ethical constraints require anonymization before open sharing of survey data, and the context of preferences is hard to capture in an ontology.
   - Processing-technique trait dictionaries were not yet in the Crop Ontology, so participatory processing data were not yet in Breedbase.
   - Mapping of gendered food product profiles to the Crop Ontology was tested only for matooke.
   - Material bought in markets under local names is not in Breedbase, and one variety can have several market names.
   - The cascading design, where each module passed validated data to the next, slowed uploads to the breeding databases.
   - Breedbase does not yet integrate target product profiles with thresholds."

9. **Summary, "Data came from a five-step ..." (Imprecise, low).** The five-step methodology produced the preference data only (p. 4517, PDF p. 4). Sensory, lab and NIRS data came from other protocols. Replace "Data came from a five-step, gender-inclusive methodology." with "Preference data came from a five-step, gender-inclusive methodology." Also in the first paragraph, replace "such as gari, eba, boiled cassava" with "such as gari-eba, boiled cassava", because Table 1 counts gari-eba as one of the 12 products (p. 4515, PDF p. 2). Optionally, after the lessons sentence, add: "They advise breeding teams to use the food scientists' SOPs, lexicons and templates in their own participatory consumer trials." (p. 4524, PDF p. 11). This is the passage most relevant to tricot users.

10. **Methods, Quality data bullet (Imprecise, low).** The card says "comparable equipment across partners". The paper says the project bought similar equipment for laboratories in Colombia, Guadeloupe and sub-Saharan Africa (p. 4516, PDF p. 3), but breeding programmes used various NIRS devices, such as Foss XDS and handheld SciO (p. 4518, PDF p. 5). Replace with:

    "- **Quality data.** Trained sensory panels with product lexicons, instrumental texture, biochemical analysis and NIRS. The project bought similar laboratory equipment for Colombia, Guadeloupe and sub-Saharan Africa, but breeding programmes used various NIRS devices."

11. **Frontmatter data and region (Imprecise, low).** The paper's data availability statement points to Agritrop (p. 4525, PDF p. 12), where all SOPs have DOIs (p. 4516). The name "RTBfoods Dataverse" is not in the paper, and NIRS data went only to CassavaBase and YamBase. Replace with:

    `data: sensory and biophysical data in the crop Breedbase databases (CassavaBase, MusaBase, PotatoBase, SweetPotatoBase, YamBase) and NIRS spectra in CassavaBase and YamBase. Gendered food product profiles in an open Dataverse repository (Supporting Information Table S3). SOPs, guidelines and reports with DOIs in Agritrop (https://agritrop.cirad.fr/), named in the data availability statement`

    For region, Table 1 leaves the primary country of attiéké blank, but Table 6 gives Côte d'Ivoire (p. 4522). Replace with:

    `region: Nigeria, Uganda, Cameroon, Benin and Colombia as primary study countries, Côte d'Ivoire for attiéké, with spillover to Ghana and Kenya`

12. **Notes, second bullet (Not in source, acceptable placement).** The statement that the suite's tricot SOPs follow this approach is outside knowledge. It belongs in Notes, but should say so. Start the bullet with "Outside this paper:". Also add the source-issue notes in the Source issues table below.

## Metadata check

| Field | Card | Source (page) | Status |
|---|---|---|---|
| title | Connecting data for consumer preferences, food quality, and breeding ... | Same (p. 4514, PDF p. 1) | Supported |
| authors | 14 names and 12 co-authors | 25 authors in byline, so 11 after the 14 listed (p. 4514) | Imprecise |
| year | 2023 | Published online 2 June 2023, issue 2024 (p. 4514) | Supported |
| journal | Journal of the Science of Food and Agriculture | Same (footer) | Supported |
| article | 104(8), 4514-4526 (published online 2023) | J Sci Food Agric 2024, 104: 4514-4526, issue 8 in Wiley download stamp | Supported |
| type | review | Labelled "Review" (p. 4514) | Supported |
| doi | 10.1002/jsfa.12710 | Same (p. 4514) | Supported |
| license | CC BY 4.0 | Creative Commons Attribution License (p. 4514) | Supported |
| data | Breedbase databases, "RTBfoods Dataverse" | Breedbase, a Dataverse repository for GFPPs (p. 4520), data availability statement names Agritrop (p. 4525). NIRS only in CassavaBase and YamBase | Imprecise |
| crops | cassava, yam, sweetpotato, potato, banana (matooke, plantain) | Table 1 (p. 4515) | Supported |
| region | primary: Nigeria, Uganda, Cameroon, Benin, Colombia, and spillover: Côte d'Ivoire, Ghana, Kenya | Table 1 (p. 4515). Attiéké primary country blank in Table 1, Côte d'Ivoire in Table 6 (p. 4522) | Imprecise (minor) |
| gist | consumer, sensory, lab and NIRS data link to genotypes in Breedbase | Survey data went to a separate repository (abstract, p. 4514) | Imprecise |
| not_established | adoption, tricot, Table 9 percentages | All three correct. "tricot" does not appear in the text. Missing items on causal attribution and on where survey data are stored | Supported (incomplete) |

## Claim-by-claim check

| # | Section | Claim (short) | Status | Source evidence (page) | Comment |
|---|---|---|---|---|---|
| 1 | Summary | Breeders target food qualities users want, summarized in TPPs | Supported | p. 4514-4515 | "increasingly" is mild framing |
| 2 | Summary | Five-year RTBfoods, preferences of farmers, processors, traders, consumers for 12 products, e.g. gari, eba, boiled cassava, pounded yam, matooke | Imprecise | Abstract, Table 1 (p. 4514-4515) | Gari-eba is one product in Table 1. See fix 9 |
| 3 | Summary | Arnaud, Menda, Tran, Asiimwe and colleagues from Bioversity, BTI, CIRAD, IITA, CIP, NaCRRI, NRCRI | Supported | Affiliations (p. 4514) | CIAT and NRI also contribute. Not an error |
| 4 | Summary | Data came from a five-step, gender-inclusive methodology | Imprecise | p. 4517 | Applies to preference data only. Fix 9 |
| 5 | Summary | Five steps listed, up to 300 consumers (150 rural, 150 urban, equal women and men) | Supported | p. 4517 (PDF p. 4) | |
| 6 | Summary | Sensory panels, texture, biochemistry and NIRS characterized genotypes | Supported | p. 4515-4518 | |
| 7 | Summary | Standardization came first | Supported | Lessons, p. 4525 | Paraphrase of "prerequisite" |
| 8 | Summary | Product-specific SOPs for surveys, processing, panels, lab, with lexicons, all versioned | Supported | p. 4516 (PDF p. 3) | |
| 9 | Summary | Lexicon traits added to CO via TD template, variable = trait + method + scale | Supported | p. 4516-4517, 4519 | |
| 10 | Summary | One trait can carry several methods and scales because preferences vary | Supported | p. 4517, lessons p. 4525 | |
| 11 | Summary | Templates use CO variable IDs as column headers | Supported | p. 4518, p. 4522, Fig. 6 | |
| 12 | Summary | Lab, sensory, NIRS data uploaded to Breedbase, linked to plant record, database model changed for sensory panel trials | Supported | Abstract, p. 4520-4522 | |
| 13 | Summary | Cleaning rules: replicate difference ≤3, panel mean check, minimum eight panellists | Supported | p. 4518 (PDF p. 5) | Rules come from refs 12 and 13 |
| 14 | Summary | Survey data anonymized and placed in an open Dataverse repository | Imprecise | Abstract p. 4514, p. 4520, Fig. 5 p. 4521 | Dataverse named only for GFPPs. Fix 5 |
| 15 | Summary | Programmes measured more quality traits after 2018 | Imprecise | Lessons p. 4525, Table 9 p. 4525 | Authors' claim, but NRCRI cassava fell 9 to 7, and the count is before-and-after only. Fixes 2 to 4 |
| 16 | Summary | Lessons: SOPs early, IDs in every file, synonyms, gender- and culture-aware data | Supported | p. 4523-4525 | |
| 17 | Summary | Breedbase should hold TPPs with thresholds to score clones | Supported | p. 4524 (PDF p. 11) | Card's "propose" matches the source's "should" |
| 18 | Methods | RTBfoods, BMGF INV-008567, 7 African, 1 Latin American, 2 European countries | Supported | p. 4515, p. 4525 | Grant formerly OPP1178942 |
| 19 | Methods | Five-step methodology | Supported | p. 4517 | |
| 20 | Methods | Panels, texture, biochemistry, NIRS, comparable equipment across partners | Imprecise | p. 4516, p. 4518 | Similar lab equipment bought, but NIRS devices varied. Fix 10 |
| 21 | Methods | TD template 5.2, guidelines 2.1, Breedbase templates, NIRS with Waves, surveys in Dataverse | Supported | p. 4517-4518, p. 4520 | |
| 22 | Limitations | Traits, variables, scales differ by product and country | Supported | Lessons p. 4525, p. 4516 | |
| 23 | Limitations | Different scales (0-10, 0-100) and method types complicate harmonization | Imprecise | p. 4522 (PDF p. 9) | Paper names naming, classification and scales, not method types. Fix 8 |
| 24 | Limitations | Ethical constraints require anonymization | Supported | p. 4520 | |
| 25 | Limitations | Breedbase does not yet integrate TPPs with thresholds | Supported | p. 4524 | |
| 26 | Key numbers | 12 food products | Supported | Abstract, Table 1 | |
| 27 | Key numbers | 5 years | Supported | Abstract | |
| 28 | Key numbers | Up to 300 (150 + 150), half women | Supported | p. 4517 | |
| 29 | Key numbers | ≥8 panellists, "This paper" | Imprecise | p. 4518 | Cited from ref. 12. Paper adds ≥10 preferred. Fix 7 |
| 30 | Key numbers | ≤3 replicate difference, guidelines cited | Supported | p. 4518 (refs 12, 13) | |
| 31 | Key numbers | IITA cassava 25 to 34, 1974-2017 vs 2018-2022 | Supported | Table 9, p. 4525 (PDF p. 12, checked on image) | |
| 32 | Key numbers | CIAT cassava 9 to 63, 1979-2017 vs 2018-2022 | Supported | Table 9 | |
| 33 | Notes | Table 9 percentages do not match counts (IITA 25 to 34 listed as 87.5%) | Supported | Table 9 | Recomputed: 36.0% (see Source issues) |
| 34 | Notes | Suite's tricot SOPs follow this approach, ClimMob and EBS share CO trait IDs | Not in source | n/a | Outside knowledge in Notes. Acceptable, but label it. Fix 12 |
| 35 to 47 | Frontmatter | 13 fields | 9 Supported, 4 Imprecise | See Metadata check | |

## Source issues

| Issue | Where (page) | Flagged in card? | Suggested Notes text |
|---|---|---|---|
| Table 9 percentage column does not match its counts. Recomputed changes: IITA cassava 36.0% (listed 87.5), NaCRRI cassava 88.9% (14.3), NRCRI cassava -22.2% (26.5), CIAT cassava 600% (47.1), IITA yam 50.0% (33.3), NRCRI yam 20.0% (16.7) | Table 9, p. 4525 (PDF p. 12) | Yes | Current note is fine. Optionally add: "Recomputed from the counts, the changes are +36% (IITA cassava), +89% (NaCRRI), -22% (NRCRI cassava), +600% (CIAT), +50% (IITA yam) and +20% (NRCRI yam) (card's own calculation)." |
| Table 9 caption says "percentage increase", but NRCRI cassava fell from 9 to 7 | Table 9, p. 4525 | No | "Table 9 is titled as an increase, but NRCRI cassava quality traits fell from 9 (2006-2017) to 7 (2018-2021)." |
| CNRA yam has only one period (2016-2017, 3 quality traits) but a 40% change | Table 9, p. 4525 | No | "The CNRA yam row has no 2018-2022 count, so its 40% change cannot be checked." |
| Attiéké has no primary study country in Table 1, but Table 6 lists Côte d'Ivoire | Table 1 p. 4515, Table 6 p. 4522 | No | "Table 1 leaves the attiéké study country blank. Table 6 gives Côte d'Ivoire." |
| Table 8 variable labels end "1to10" but the names say "scale 0-19" and "scale 0-10". Fig. 4 caption says 1-10, but the figure shows "scale 0-10" | Table 8 p. 4524, Fig. 4 p. 4521 | No | "Scale ranges in Table 8 and Fig. 4 are inconsistent (0-19, 0-10, 1-10). Check the Crop Ontology record before reusing these variables." |
| Dry matter threshold for biofortified cassava given as 0.3 g/kg of fresh weight, which is implausibly low (likely meant 30% or 300 g/kg) | p. 4524 (PDF p. 11) | No (card does not use it) | Optional: "The TPP example gives dry matter as 0.3 g/kg fresh weight, which looks like a unit error." |

## Completeness

| Item in the source | In card? | Importance | Suggested addition |
|---|---|---|---|
| Aim: standardize data collection for 12 products and connect survey, post-harvest and sensory data with agronomic and genetic data | Yes | high | none |
| 163 sensory traits in CO and databases (Table 6) | No | high | Fixes 2 and 7 |
| 78 biophysical traits for six products, means uploaded, raw data as extra files | No | high | Fixes 2 and 7 |
| 21,844 NIRS spectra in CassavaBase and YamBase | No | high | Fixes 2 and 7 |
| 13 GFPPs in an open Dataverse repository | No (Dataverse only) | high | Fixes 2, 5 and 7 |
| Processing data not yet in Breedbase, processing TDs not yet in CO | No | high | Fixes 2, 4 and 8 |
| Table 9 shows one decrease and is a before-and-after count | No | high | Fixes 2 to 4 |
| Authors' limitations: GFPP mapping tested only for matooke, market material not in Breedbase, cascading design slowed uploads, survey context hard to capture | No | medium | Fix 8 |
| Advice that breeding teams use food-science SOPs, lexicons and templates in participatory consumer trials | No | medium (most relevant to tricot users) | Fix 9 |
| Two ways to upload sensory data: raw data in a "sensory panel trial" record, or means attached to the field trial | No | medium | Optional Methods bullet: "- **Sensory upload.** Either raw panel data in a separate sensory panel trial, where Breedbase computes means and SDs, or means attached to the field trial record." |
| Post-composing of variables in Breedbase when a variable is missing from the CO | No | low | Optional, in Data integration bullet: "missing variables can be composed during upload and submitted to the CO" |
| NIRS stored by sample name in a separate section, not with ontology IDs per wavelength | Partly (Waves only) | low | none needed |
| Method type "Measurement" for trained panels and "Estimation" for hedonic tests | No | low | Optional |
| Panel gender balance and age range (18 to 60) | No | low | Covered in fix 7 row |
| TPP example with thresholds (beta-carotene above 15 ppm, fresh root yield 25 t/ha) | No | low | none needed |

## Template compliance

- Summary word count: 362, below the 400 minimum. With fixes 2, 3, 5 and 9 it becomes about 497 words.
- Gist: 29 words (under 30). The suggested replacement is also 29 words.
- Keywords: 12 (within 8 to 12).
- Questions: 6 (within 4 to 7).
- House style: tricot is lowercase throughout. maniva does not appear.
- Long format sections are all present.
