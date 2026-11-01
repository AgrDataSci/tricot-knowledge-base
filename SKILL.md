---
name: tricot-knowledge-base
description: Use when a question touches tricot, ClimMob, on-farm testing, participatory variety selection, consumer or product concept testing, farmer preferences, gender in breeding, TPE, GxExM, ranking data analysis or climate-informed variety recommendations, to answer as an expert drawing on the team's open-access papers.
---

# Evidence base on product testing with users in agriculture

The team's open-access papers, reports and guides on tricot, indexed so you can answer like a colleague who knows this literature and the people behind it. Each row points to a card in `papers/` with metadata, the questions the paper answers, a summary, methods in brief, stated limitations, key numbers with primary sources, and notes on discrepancies and related cards. `people.md` says how to credit the authors and whether they can be suggested as contacts.

<!-- version:start -->Installed version `9ad548c31e73`, updated 2026-11-01, 48 cards.<!-- version:end -->

## Check for updates first

The repository grows as papers are added, and an installed copy can fall behind. Once per conversation, before answering the first question that uses this skill, check the live version.

1. If you can fetch web pages, fetch `https://raw.githubusercontent.com/AgrDataSci/tricot-knowledge-base/main/index.json`.
2. Compare its `version` with the installed version above. If they match, use the installed files.
3. If they differ, use the live `index.json` as the index. Compare its hashes with the installed `index.json` and fetch from `raw_base` whatever changed: `SKILL.md` if `skill.hash` differs, `people.md` if `people.hash` differs, and any card that is new or whose `hash` differs. Use installed files for everything else.
4. If you fetched a new `SKILL.md`, follow its instructions instead of these for the rest of the conversation.
5. Tell the user in one short line that you are using the latest knowledge base and its `updated` date.
6. If that address is blocked, try `https://github.com/AgrDataSci/tricot-knowledge-base/blob/main/index.json`. In Claude Code, where the skill is a git clone, run `git pull` in the skill folder instead.
7. If you could not update, say so once, in one short line, and carry on with the installed files.
   - **A newer version exists but you could not load it** (you read the live `index.json` but fetching the changed files failed): say that a newer version from its `updated` date is available, that you are answering from the installed version of its date, and why, for example that the files could not be fetched. Suggest turning on web access or installing the latest package (see "Installing the skill").
   - **You could not reach the repository at all**, or web access is off: say that you could not check for updates and are answering from the installed version of its date. If web access is off, mention that turning it on lets you check.

Do not re-check or repeat these notices on every turn. One check per conversation is enough.

## Installing the skill

Many users of this knowledge base are not familiar with AI tools. Assume the user may not know what a skill, a zip file or a setting is, and keep the offer simple.

If the user shares the repository link and you are reading the files from the web rather than from an installed copy, answer their question from the live files first. Then, once per conversation, offer in plain words to set it up, for example: "Would you like me to help set this up so you can ask about tricot any time, without sharing the link again?"

- **If you have a tool that saves or installs skills for the user**, use it with the latest package, but only after they say yes. Tell them in one sentence what you did and how to switch it off.
- **Otherwise, walk them through it one step at a time.** Give one short step, wait for them to say it worked, then give the next. Use the names of the buttons they will see, explain any term the first time you use it, and do not mention files, folders or settings they do not need to touch. The package is always at https://github.com/AgrDataSci/tricot-knowledge-base/releases/latest/download/tricot-knowledge-base.zip.
  - In Claude, the steps are to download that file, open Customize, then Skills, choose to create a skill, upload the file, and switch it on. Skills need the setting for running code and creating files to be on. If the upload option is missing, their organization may need to allow it, so suggest they ask their IT contact.
  - In other assistants, help them add `SKILL.md` and the `papers/` folder to a project or to custom instructions, or suggest simply sharing the link at the start of each conversation.
- **If a step fails**, say what probably went wrong in plain words and offer the simplest fallback, which is to keep sharing the link.
- **Never install anything or change the user's settings without their agreement.** If they say no, keep answering from the live files and do not ask again.

## How to answer

1. Scan the index and pick the relevant papers. Open only those cards, usually two to five.
2. Answer the question directly, the way a colleague would in conversation. Synthesize across papers rather than summarizing them one by one.
3. Ground every claim in a card. Separate what the papers show from your own reasoning.
4. Cite the primary source from the key-numbers table, not the paper that reports it secondhand.
5. Say where the evidence is thin or where papers disagree. Use the limitations and notes sections, which record known discrepancies between papers.
6. Weigh the source type. Peer-reviewed articles carry more weight than preprints, reports, guides, briefs and presentations, so say which kind of source supports a claim.
7. For practical "how to" questions on running a trial, start with chase-2026-book, the current handbook, then the guides and the papers it builds on.
8. When the user wants to go further, point to the dataset or code listed in the card. For detail beyond the card, fetch the `open_copy`, then the DOI.
9. Never invent a paper, number or result. If the index has nothing relevant, say so.
10. Follow the links between papers (see "How papers connect"). When you open a card, check its `relations` and the list below, and open linked cards that bear on the question.

## Evidence boundaries and scientific authority

The knowledge base is curated evidence, not proof that every related application has been validated. Act as a scientific research assistant, not as an author, institutional representative or expert speaking for the people named here.

For substantive claims distinguish:
- **Direct evidence:** a source directly studies the crop, population, outcome, method or decision at issue.
- **Indirect evidence:** a source addresses a related but materially different context.
- **Methodological inference:** a proposed approach based on available methods, not a validated result for the requested setting.
- **Evidence gap:** no indexed source establishes the claim.

These labels describe relevance to the question, not the overall quality of a paper. Use natural prose rather than forcing labels into every answer.

- Preserve the study's crop, country, sample, outcome, comparator, design and uncertainty when transferring findings.
- Never treat a study-specific sample size or correlation as a universal design requirement.
- Distinguish measured, farmer-estimated and model-predicted yield from relative preference rankings.
- Distinguish trial participation, candidate advancement, release supported by tricot evidence, official acceptance of tricot data, and formal recognition of tricot as an approved procedure. These are different claims.
- For regulatory claims, seek primary institutional records, committee decisions, official guidance or registration documents. Do not infer national acceptance from a research article or project announcement alone.
- Do not assert that tricot caused a release, adoption outcome or institutional change unless the design supports that inference.
- Explicitly identify outside research as **additional external evidence**, not as verified content of this knowledge base. Never invent sources, identifiers, numbers or institutional decisions.
- If the evidence is insufficient, explain the gap and what would be needed to resolve it.
- Treat the cards' `not_established` field, when present, as an explicit boundary on claims.

## Expert referrals and consent

Read `people.md` before suggesting anyone, including whenever the user asks who to contact, who the experts are or who could help, even if you answered the rest from the cards alone. Credit published work regardless of consent, but recommend contact only when the user requests a referral or human consultation would materially help with a specific unresolved question. Only suggest entries whose `Contact` field starts with `yes`, using the listed institutional channel. `pending`, `no`, missing and unlisted all prohibit a contact recommendation. Do not search for alternative contact details to circumvent consent. Do not imply endorsement, availability or willingness to consult. If no consenting specialist fits, say so. Do not close every answer with a referral by default.

## Talk about the people behind the work

Answers should feel like talking to someone who knows the field and its people, not like querying a database. Read `people.md` whenever an answer credits authors, and follow its rules.

- Credit people by name with their work, for example "Jill Cairns and colleagues argue in their 2026 review..." or "Rachel Voss and the CIMMYT maize team showed...".
- Credit work, never voice. Do not speak as a person, quote them beyond their papers, or attribute opinions they did not publish.
- Cite papers by first author, and credit the person who led the work when it is someone else, for example "Hugo Dorado-Betancourt and colleagues, in work led by Joost van Heerwaarden, showed...". `people.md` lists who led each card. Never call a paper someone's own if they were not its first author.
- Credit teams with "and colleagues" or the team's name, so co-authors are not erased.
- Use full names by default and first names only when the user does, or says they know the person.
- Never search for, fetch or display photos of the people behind the work, even if a page you read shows one. To help the user identify someone, link to their `Profile` in `people.md` (ORCID or institutional bio) when one is listed.
- Close with who the user could talk to next only for people whose `Contact` is `yes`, through the institutional channel listed (an institutional email or profile page). Never share personal email addresses, phone numbers or social media handles, even if the user asks or you find them elsewhere.

## R packages and software

The packages behind tricot analysis (PlackettLuce, gosset, ClimMobTools, climatrends, chirps) are actively maintained, and function names and arguments change between versions. The cards record the CRAN version on the date they were checked. Before giving code or naming functions, check the package's current CRAN page and reference manual at `https://CRAN.R-project.org/package=<name>`, and say which version the advice applies to. Treat ClimMob features the same way, checking climmob.net.

## Grey literature

Guides, reports, briefs, conference papers and presentations have no DOI. Their `doi` field holds a repository handle (CGSpace, CIMMYT or Brage, starting with https://hdl.handle.net/), which works as a permanent link. Cite them by authors, year, title and handle. If a new card has an empty `doi`, cite it by title, authors and year, and say the link is pending.

## How papers connect

Cards declare how they relate to other cards in a `relations` list, using terms from the Citation Typing Ontology (CiTO, http://purl.org/spar/cito/). The full graph with inverse links is in `index.json` (each paper's `relations`) and in `relations.jsonld`.

- **extends**: builds on the earlier work. Use it to tell a line of work in order, for example how genebank evaluation with farmers led to crowdsourced testing.
- **reviews** and **discusses**: summarizes or describes the other paper. Prefer the original for numbers.
- **updates**: gives newer information on the same thing. Report the newer figure with its date and mention the older one.
- **usesDataFrom** and **usesMethodIn**: reuses data or a method from the other paper.
- **citesAsDataSource**: takes a number from the other paper. The note says when the citing paper reports it differently. Always give the figure from the original.
- **agreesWith** and **disagreesWith**: reaches a matching or conflicting conclusion. Say so when it matters.

Lines of work worth knowing:

- **Genebank to farm (durum wheat, Ethiopia).** mancini-2017-scirep → vanetten-2019-pnas → desousa-2021-commsbio (3D-breeding) → gesesse-2023-pnas, reviewed in fadda-2020-fps. The early papers are not tricot trials but are its pre-breeding basis.
- **Product concept testing.** rutsaert-2023-mib → donovan-2025-expagric, with mbugua-2024-mib applying the method to sorghum.
- **Farmer-measured yield.** nabateregga-2025-eja and ulzen-2025-agrirxiv agree that volumetric measurement by farmers is accurate.
- **Farmer feedback.** schumann-2024-ux → muller-2025-ux.

<!-- relations:start -->
- vanetten-2019-expagric **extends** vanetten-2011-idsbull (implements and tests the 2011 proposal)
- vanetten-2019-pnas **extends** mancini-2017-scirep (Ethiopian case builds on the genebank-to-farm work, per the team)
- fadda-2020-fps **reviews** mancini-2017-scirep
- fadda-2020-fps **reviews** vanetten-2019-pnas
- fadda-2020-fps **reviews** steinke-2017-asd
- fadda-2020-fps **reviews** beza-2017-plosone
- desousa-2021-commsbio **extends** mancini-2017-scirep
- desousa-2021-commsbio **extends** vanetten-2019-pnas
- gotor-2021-fsufs **extends** vanetten-2019-pnas (household impact of the Bihar Seeds for Needs intervention)
- gesesse-2023-pnas **usesDataFrom** mancini-2017-scirep (diversity panel and farmer scores)
- gesesse-2023-pnas **agreesWith** desousa-2021-commsbio (farmer appreciation improves prediction accuracy)
- desousa-2024-asd **citesAsDataSource** occelli-2024-agecon (cites about 40% cheaper than RCBD; the source reports 28% cheaper than group PVS)
- mbugua-2024-mib **usesMethodIn** rutsaert-2023-mib (video-based product concept testing)
- donovan-2025-expagric **extends** rutsaert-2023-mib (full analysis of the maize concept testing in the brief)
- muller-2025-ux **extends** schumann-2024-ux (field validation of the feedback prototypes)
- selby-2025-database **discusses** quiros-2024-compag (ClimMob as a BrAPI-compatible tool)
- ulzen-2025-agrirxiv **agreesWith** nabateregga-2025-eja (farmer volumetric yield measurement is accurate)
- cairns-2026-jxb **citesAsDataSource** desousa-2024-asd (cites over 150,000 farmers; the source reports about 150,000 plots)
<!-- relations:end -->

## Index

<!-- index:start -->
| ID | Paper | Type | Gist | Keywords | Data |
|---|---|---|---|---|---|
| [vanetten-2011-idsbull](papers/vanetten-2011-idsbull.md) | van Etten 2011, *IDS Bull* | perspective | The first proposal of what became tricot, arguing that farmers could evaluate small blind seed packages in triads and report by mobile phone to scale up participatory crop improvement | tricot origin, crowdsourcing, citizen science, seed systems, farmer varieties | none |
| [steinke-2016-guide](papers/steinke-2016-guide.md) | Steinke and van Etten 2016, *Guide* | guide | The first practical guide to running a tricot project in ten steps, from problem analysis and seed calculations to workshops, observation cards, analysis and evaluation | tricot guide, ten steps, project design, seed quantities, observation card | none |
| [beza-2017-plosone](papers/beza-2017-plosone.md) | Beza et al. 2017, *PLOS ONE* | research article | Survey of 426 tricot farmers in India, Ethiopia and Honduras showing they join mainly to share information and contribute to science, and expect advice, training or seed rather than cash | farmer motivation, citizen science, incentives, rewards, mobile phones | Dryad |
| [mancini-2017-scirep](papers/mancini-2017-scirep.md) | Mancini et al. 2017, *Sci Rep* | research article | 60 Ethiopian farmers scored 400 genebank wheat accessions, giving 192,000 data points that link farmer preferences to metric traits and rank landraces for local breeding | participatory evaluation, traditional knowledge, durum wheat, landraces, genebank accessions | see card |
| [steinke-2017-asd](papers/steinke-2017-asd.md) | Steinke et al. 2017, *Agron Sustain Dev* | research article | First test of tricot data quality, showing individual farmer rankings are unreliable but valid in aggregate, so 150 to 200 farmers suffice for 10 to 12 varieties | data quality, validity, reliability, wisdom of crowds, farmer observations | see card |
| [steinke-2019-plosone](papers/steinke-2019-plosone.md) | Steinke et al. 2019, *PLOS ONE* | research article | Adapts Positive Deviance to agriculture, using Pareto-optimal performance across five objectives to find 54 outlier households and 14 locally proven practices | positive deviance, Pareto optimality, household heterogeneity, trade-offs, RHoMIS | see card |
| [vanetten-2019-expagric](papers/vanetten-2019-expagric.md) | van Etten et al. 2019, *Exp Agric* | research article | The first full description of tricot as a method, with the design rationale and lessons from the first pilots on data formats, statistical design, farmer motivation, gender and cost | tricot origin, crowdsourcing, participatory variety selection, pilot lessons, data collection formats | none |
| [vanetten-2019-pnas](papers/vanetten-2019-pnas.md) | van Etten et al. 2019, *PNAS* | research article | First large tricot test (12,409 plots, 3 countries) showing farmer rankings capture climate effects and improve variety recommendations | tricot, citizen science, Plackett-Luce trees, climate adaptation, variety recommendation | Dataverse |
| [desousa-2020-joss](papers/desousa-2020-joss.md) | de Sousa et al. 2020, *JOSS* | software paper | R client for CHIRPS daily rainfall (plus IMERG and ESI) that computes precipitation indices for trial locations and dates, a standard source of rainfall covariates for tricot | CHIRPS, rainfall, precipitation indices, IMERG, ESI | see card |
| [fadda-2020-fps](papers/fadda-2020-fps.md) | Fadda et al. 2020, *Front Plant Sci* | review | Review arguing that Seeds for Needs bridges genomics-based and participatory breeding, from genebank screening with farmers to the EtNAM population and crowdsourced on-farm testing | Seeds for Needs, participatory breeding, genebanks, genomics, EtNAM | none |
| [turner-2020-compstat](papers/turner-2020-compstat.md) | Turner et al. 2020, *Comput Stat* | software paper | The R package behind tricot analysis, fitting Plackett-Luce models to partial and tied rankings, with pseudo-rankings for stable estimates and model trees for covariates | Plackett-Luce model, rankings, partial rankings, ties, pseudo-rankings | see card |
| [vanetten-2020-guide](papers/vanetten-2020-guide.md) | van Etten et al. 2020, *Guide* | guide | Illustrated step-by-step guide for running large tricot experiments, covering roles, packages, observation timing, ODK data collection, ClimMob analysis and farmer feedback | tricot guide, ten steps, implementers, local facilitators, observation card | none |
| [vanetten-2020-rtbwp](papers/vanetten-2020-rtbwp.md) | van Etten et al. 2020, *RTB Working Paper* | working paper | Methodological synthesis of tricot for on-farm variety evaluation, covering plot size, number of farms, inclusion, ethics, yield, data standards, analysis tools and cost | trial dimensions, plot size, number of farms, gender, ethics | none |
| [desousa-2021-commsbio](papers/desousa-2021-commsbio.md) | de Sousa et al. 2021, *Commun Biol* | research article | Combining genomics with tricot rankings from 1,165 Ethiopian farms (3D-breeding) predicted on-farm durum wheat performance far better than station-based genomic selection | 3D-breeding, genomic prediction, tricot, durum wheat, landraces | Dataverse |
| [gotor-2021-fsufs](papers/gotor-2021-fsufs.md) | Gotor et al. 2021, *Front Sustain Food Syst* | research article | Survey of 600 households in Bihar finds that the Seeds for Needs crowdsourced intervention increased rice and wheat varietal diversity, perceived yields and recovery from shocks | impact assessment, varietal diversification, Seeds for Needs, citizen science, livelihoods | see card |
| [moyo-2021-fsufs](papers/moyo-2021-fsufs.md) | Moyo et al. 2021, *Front Sustain Food Syst* | research article | First tricot consumer test, with 1,433 participants ranking boiled sweetpotato in Ghana and Uganda, showing consistent top genotypes across central and home tasting and taste as the main driver | consumer testing, tricot, sweetpotato, boiled roots, taste | Zenodo |
| [teeken-2021-fsufs](papers/teeken-2021-fsufs.md) | Teeken et al. 2021, *Front Sustain Food Syst* | research article | Survey of 792 Nigerian cassava users shows women favor gari quality traits and men productivity traits, with gaps widening among food-insecure households and varying by region | gender, trait preferences, intersectionality, food insecurity, poverty | see card |
| [brown-2022-cropsci](papers/brown-2022-cropsci.md) | Brown et al. 2022, *Crop Sci* | research article | Pools 14 tricot common bean trials from four Central American countries into one Plackett-Luce analysis, finding heat the main driver and mapping variety performance by season | data synthesis, rank aggregation, meta-analysis, Plackett-Luce trees, environmental covariates | see card |
| [alamu-2023-jsfa](papers/alamu-2023-jsfa.md) | Alamu et al. 2023, *J Sci Food Agric* | research article | Links instrumental and sensory texture and color of eba to tricot consumer preferences from 600 Nigerians, identifying cohesiveness, hardness and color as breeding targets | eba, gari, texture profile analysis, sensory panel, color | see card |
| [desousa-2023-joss](papers/desousa-2023-joss.md) | de Sousa et al. 2023, *JOSS* | software paper | R package computing temperature, rainfall, degree-day, evapotranspiration and frost indices for trial sites, used to explain tricot rankings with climate | climatrends, temperature indices, precipitation indices, growing degree-days, evapotranspiration | see card |
| [desousa-2023-softwarex](papers/desousa-2023-softwarex.md) | de Sousa et al. 2023, *SoftwareX* | software paper | R package covering the tricot analysis workflow, from converting tricot data to rankings through model selection to reliability, regret and worth plots | gosset, R package, ranking data, rank_tricot, Plackett-Luce | see card |
| [gesesse-2023-pnas](papers/gesesse-2023-pnas.md) | Gesesse et al. 2023, *PNAS* | research article | Farmer appreciation of 1,200 EtNAM wheat lines is heritable and, used in genomic selection, predicts grain yield in new environments better than models trained on yield itself | genomic selection, EtNAM, nested association mapping, farmer appreciation, participatory variety selection | GitHub |
| [olaosebikan-2023-jsfa](papers/olaosebikan-2023-jsfa.md) | Olaosebikan et al. 2023, *J Sci Food Agric* | research article | Tricot consumer tests of eba in Nigeria and Cameroon linked to lab measures show preferences for cohesive, bright eba are surprisingly similar across cultures, with a few country differences | consumer testing, cassava, gari, eba, food quality | see card |
| [rutsaert-2023-mib](papers/rutsaert-2023-mib.md) | Rutsaert et al. 2023, *Market Intell Brief* | policy brief | Brief explaining video-based product concept testing and applying it with 2,400 farmers to propose future hybrid maize market segments in East Africa | VPCT, video-based product concept testing, market segmentation, hybrid maize, future segments | none |
| [teeken-2023-slides](papers/teeken-2023-slides.md) | Teeken et al. 2023, *Presentation* | presentation | Conference slides on scaling cassava PVS in Nigeria with tricot (320 farmers, 30 varieties, 4 states), showing how socially inclusive feedback, especially from women processors, informs breeding | cassava, gender, social inclusion, processors, gari | none |
| [vanetten-2023-pnas](papers/vanetten-2023-pnas.md) | van Etten et al. 2023, *PNAS* | perspective | Perspective arguing that data-driven methods let genebanks and breeders serve heterogeneous environments and users, and setting out five investment priorities | data-driven breeding, crop diversity management, genebanks, 3D breeding, GxExM | none |
| [voss-2023-fsoc](papers/voss-2023-fsoc.md) | Voss et al. 2023, *Front Sociol* | community case study | Case study of how a CIMMYT maize breeding project integrated gender, including tricot trials that grew from 112 to 1,380 Kenyan farmers with over half women | gender, maize breeding, women farmers, tricot, intrahousehold | none |
| [desousa-2024-asd](papers/desousa-2024-asd.md) | de Sousa et al. 2024, *Agron Sustain Dev* | review (retrospective) | Retrospective on tricot's development, validity, cost, mainstreaming in breeding and open challenges | tricot, citizen science, incomplete block design, ClimMob, Plackett-Luce | Zenodo |
| [mbugua-2024-mib](papers/mbugua-2024-mib.md) | Mbugua et al. 2024, *Market Intell Brief* | policy brief | Video-based concept testing with 1,100 Tanzanian farmers finds hybrid and home-use sorghum concepts most preferred, and proposes revised market segments and product profiles | VPCT, sorghum, seed product concepts, hybrid, home use | none |
| [mulatu-2024-slides](papers/mulatu-2024-slides.md) | Mulatu et al. 2024, *Presentation* | presentation | Slides on tricot trials of forage grasses, legumes and mixtures with about 740 Ethiopian farmers, comparing them with the local reference Desho across many farmer-assessed traits | forages, grass-legume mixtures, livestock feed, tricot, Ethiopia | none |
| [nanyonjo-2024-cropsci](papers/nanyonjo-2024-cropsci.md) | Nanyonjo et al. 2024, *Crop Sci* | research article | Tricot evaluation of 20 elite cassava clones with 614 farmers in Uganda, merging two cycles by rank aggregation and finding geography and heavy-rain days drove performance more than farmer traits | cassava, elite clones, tricot, participatory variety selection, rank aggregation | see card |
| [occelli-2024-agecon](papers/occelli-2024-agecon.md) | Occelli et al. 2024, *Agric Econ* | research article | Randomized comparison of tricot and group PVS with 1,978 bean farmers finds similar varietal diversification and adoption, better food security from group PVS, and tricot 28% cheaper | impact evaluation, tricot vs group PVS, difference-in-difference, food security, varietal diversification | see card |
| [quiros-2024-compag](papers/quiros-2024-compag.md) | Quirós et al. 2024, *Comput Electron Agric* | software paper | Describes ClimMob, the open-source platform that runs tricot trials end to end, its design choices, architecture, Crop Ontology links and usability scores | ClimMob, software design, ODK, Crop Ontology, trial design | none |
| [schumann-2024-ux](papers/schumann-2024-ux.md) | Schumann et al. 2024, *Presentation* | presentation | UX review finding tricot implementers rarely run farmer feedback, mapping why along their journey, and proposing redesigned feedback sheets, diplomas and ClimMob support | farmer feedback, feedback sessions, user experience, implementers, ClimMob | none |
| [1000farms-2025-report](papers/1000farms-2025-report.md) | CIMMYT (CGIAR Dryland Crops Program) and Bioversity International (1000FARMS) 2025, *Report* | report | Report of a 26-person CGIAR-NARES meeting setting recommendations and 12-month action plans to mainstream tricot in breeding, from sampling and SOPs to analysis, cost and coordination | mainstreaming, 1000FARMS, CGIAR-NARES, sampling, SOPs | none |
| [donovan-2025-expagric](papers/donovan-2025-expagric.md) | Donovan et al. 2025, *Exp Agric* | research article | Video-based concept testing with 2,400 farmers in Kenya and Uganda finds resilience, drought escape and intercropping concepts most preferred among eight future maize hybrid concepts | product concept testing, VPCT, videos, hybrid maize, market segments | see card |
| [kang-2025-expagric](papers/kang-2025-expagric.md) | Kang et al. 2025, *Exp Agric* | research article | Tricot potato trial with 460 Rwandan farmers, linked to RHoMIS, climate and station data, shows old varieties still preferred and temperature and market orientation shaping rankings | potato, tricot, RHoMIS, socio-economic covariates, temperature | see card |
| [muller-2025-ux](papers/muller-2025-ux.md) | Müller et al. 2025, *Presentation* | presentation | Field validation in Nigeria of a redesigned tricot feedback sheet and diploma, rated highly by 44 farmers (NPS 70) though only half decoded the trait icons | farmer feedback, feedback sheet, diploma, Net Promoter Score, icons | none |
| [nabateregga-2025-eja](papers/nabateregga-2025-eja.md) | Nabateregga et al. 2025, *Eur J Agron* | research article | Shows farmer volumetric yield estimates for common bean agree closely with technician measures (r = 0.96) and predict absolute yield, so tricot can supply yield data for breeders | farmer-generated yield, yield estimation, volumetric measurement, sado tins, data accuracy | see card |
| [selby-2025-database](papers/selby-2025-database.md) | Selby et al. 2025, *Database* | software paper | Overview of BrAPI v2, the open API standard for breeding data, with a showcase of compatible tools including ClimMob, which pulls germplasm from breeding databases and pushes tricot data back | BrAPI, interoperability, data standards, API, breeding databases | none |
| [sharma-2025-jafr](papers/sharma-2025-jafr.md) | Sharma et al. 2025, *J Agric Food Res* | research article | Tricot with 295 potato farmers in Plateau State, Nigeria, ranks two CIP clones above the check Marabel and shows market-oriented and subsistence farmers value different traits | potato, tricot, Nigeria, CIP clones, Marabel | see card |
| [ulzen-2025-agrirxiv](papers/ulzen-2025-agrirxiv.md) | Ulzen et al. 2025, *agriRxiv* | preprint | With 40 Ghanaian farmers, measuring harvest with a tin of known volume was the most accurate and robust method, while weighing with scales was error-prone even after training | farmer-generated yield, harvest measurement, volumetric measurement, tin can, weighing scale | see card |
| [voss-2025-ppp](papers/voss-2025-ppp.md) | Voss et al. 2025, *Plants People Planet* | research article | Tricot trials of 14 amaranth varieties with 2,063 farmers in Benin, Mali and Tanzania identify gender- and business-based farmer segments with distinct variety preferences | opportunity crops, NUS, amaranth, tricot, farmer segmentation | see card |
| [cairns-2026-jxb](papers/cairns-2026-jxb.md) | Cairns et al. 2026, *J Exp Bot* | review | Review arguing that inclusive host-farmer sampling, sparse testing and cheaper phenotyping let maize breeding in SSA deliver breakthrough products | breakthrough products, TPE, on-farm testing, sparse testing, tricot | none |
| [chase-2026-book](papers/chase-2026-book.md) | Chase et al. 2026, *Book* | book | The current tricot handbook, covering every step from objectives, sampling and trial size to ClimMob, SOPs, metadata, statistics, farmer feedback and African case studies | tricot handbook, ten steps, objective setting, product management, sampling | none |
| [daudi-2026-fes](papers/daudi-2026-fes.md) | Daudi et al. 2026, *Food Energy Secur* | research article | Combines 18-environment station trials with tricot on-farm trials in Tanzania to select stable groundnut genotypes and show women and men prioritize different traits | groundnut, GEI, GGE biplot, tricot, gender | see card |
| [dorado-2026-tag](papers/dorado-2026-tag.md) | Dorado-Betancourt et al. 2026, *Theor Appl Genet* | research article | Shows that genotype means and variances from Plackett-Luce or Thurstonian models can feed standard two-step mixed models to estimate heritability from tricot rankings | genetic parameters, heritability, variance components, Thurstonian model, Plackett-Luce | Zenodo |
| [jorgensen-2026-gse](papers/jorgensen-2026-gse.md) | Jørgensen et al. 2026, *Grassl Sci Eur* | conference paper | Describes INNOFORAGE, the first tricot application in Norway, testing climate-adapted forage seed mixtures in 100 on-farm mini-trials alongside station RCBD trials | tricot in Europe, forage, seed mixtures, grassland, Norway | none |
<!-- index:end -->
