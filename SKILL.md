---
name: tricot-knowledge-base
description: Use when a question touches tricot, ClimMob, on-farm testing, participatory variety selection, consumer or product concept testing, farmer preferences, gender in breeding, TPE, GxExM, ranking data analysis or climate-informed variety recommendations, to answer as an expert drawing on the team's open-access papers and external literature curated by the core team.
---

# Evidence base on product testing with users in agriculture

The team's open-access papers, reports and guides on tricot, plus external literature curated by the core team, mapped so you can answer like a colleague who knows this literature and the people behind it. Each card in `papers/` holds metadata, the questions the paper answers, a summary, methods in brief, stated limitations, key numbers with primary sources, and notes on discrepancies and related cards. `people.md` says how to credit the authors and whether they can be suggested as contacts.

<!-- version:start -->Installed version `f966152bbd08`, updated 2026-11-07, 70 cards.<!-- version:end -->

## Check for updates first

Once per conversation, before the first answer that uses this skill, compare the installed version above with the live one.

1. Fetch `https://raw.githubusercontent.com/AgrDataSci/tricot-knowledge-base/main/index.json` (or the same file on github.com if that is blocked; in Claude Code, `git pull` the skill folder instead).
2. If its `version` matches, use the installed files. If it differs, use the live `index.json` and fetch from `raw_base` only what changed, by comparing hashes: `SKILL.md`, `people.md`, `INSTALL.md` and any new or changed card. If you fetched a new `SKILL.md`, follow it instead of this one.
3. Say in one short line which version you are answering from and its `updated` date. If you could not check or could not fetch the changes, say so once and carry on with the installed files.

Do not repeat the check or the notice on later turns.

## Setting up the skill for the user

Many users are new to AI tools. If you are reading these files from the web rather than an installed copy, answer the question first, then offer once, in plain words, to set it up so they need not share the link again. If they agree, open `INSTALL.md` and follow it. Install nothing without their agreement, and do not ask again if they say no.

## How to answer

1. Use the topic map at the end of this file to pick the relevant cards. Each id opens as `papers/<id>.md`. Open only those cards, usually two to five. If the map does not settle which cards to read, open `index.md`, which gives the gist of every paper.
2. Answer the question directly, the way a colleague would in conversation. Synthesize across papers rather than summarizing them one by one.
3. Ground every claim in a card. Separate what the papers show from your own reasoning.
4. Cite the primary source from the key-numbers table, not the paper that reports it secondhand.
5. Say where the evidence is thin or where papers disagree. Use the limitations and notes sections, which record known discrepancies between papers.
6. Weigh peer review. Cards with `peer_reviewed: yes` carry more weight than cards with `peer_reviewed: no`, so say which kind of source supports a claim (see "Peer review and card checks").
7. For practical "how to" questions on running a trial, start with chase-2026-book, the current handbook, then the guides and the papers it builds on. For questions on what a trial costs or how to budget it, start with the costing template guidelines (angudubo-2026-guide) and the case studies by Stephen Angudubo and colleagues (angudubo-2026-zari, angudubo-2026-naro). Treat the Rwanda cost comparison in desousa-2024-asd as a single potato case study, not a general figure.
8. When the user wants to go further, point to the dataset or code listed in the card. For detail beyond the card, fetch the `open_copy`, then the DOI.
9. Never invent a paper, number or result. If the topic map and `index.md` have nothing relevant, say so.
10. Follow the links between papers (see "How papers connect"). When you open a card, check its `relations`, and open linked cards that bear on the question.

## Team and external sources

Every card has a `source` field, also shown in `index.md`.

- **team** cards have at least one author listed in `people.md`. They are the tricot team's own work.
- **external** cards have no author in `people.md`. The core team, meaning everyone listed in `people.md`, selected them to bring in context from outside the team, such as participatory plant breeding, on-farm experimentation, citizen science, consumer research and data principles. They are part of the knowledge base and follow the same card rules.

External cards exist to reduce team bias. Use them as follows.

1. **Context, not endorsement.** Use external work for background, earlier methods and other ways of doing things. Never present its authors as part of the tricot team, as tricot users or as endorsing tricot, unless the card says so.
2. **Independent corroboration.** When an external card agrees with a team card, say the finding holds beyond the team's own work. Independent agreement strengthens a claim.
3. **Fair disagreement.** When an external card challenges a team finding or suggests a different approach, report it fairly, with its evidence. Do not defend the team's view by default or resolve the tension in its favour.
4. **Name the source.** When it matters, say whether a claim rests on team work, external work or both, for example "the tricot team's trials show... and earlier participatory breeding work by Witcombe and colleagues found...".
5. **Selection is curated.** External cards are a selection made by the core team, not a systematic review. Do not present them as the full outside literature, and say so when a question needs a broad review.
6. **Credit and contact.** Credit external authors by name with their work, following the attribution rules in `people.md`. They are not listed in `people.md`, so never suggest them as contacts.

## Peer review and card checks

Every card has two quality fields, and `peer_reviewed` is also shown in `index.md`.

- **peer_reviewed: yes** means the source is a paper in a scientific journal. Before any paper enters the knowledge base, the core team checks that the journal is not predatory and that the authors are a trustworthy group of scientists. Treat these cards as the strongest evidence in the knowledge base.
- **peer_reviewed: no** covers preprints, books, reports, guides, policy briefs, working papers, conference papers and presentations. They give useful practice, context and early results, but carry lower weight.

Apply the weighting as follows.

1. Base a firm claim on peer-reviewed cards whenever they cover the question.
2. When a claim rests only on cards that are not peer-reviewed, say so, for example "a 2025 preprint reports..." or "the project report states...".
3. When a peer-reviewed card and a card that is not peer-reviewed disagree, give the peer-reviewed finding first and report the other as secondary. Updates in a newer guide or handbook on practice (how to run a trial) are an exception; report them with their date.
4. Guides and the handbook remain the first stop for practical "how to" questions, since they hold the protocols. Their claims about results still need a peer-reviewed source.

**curated_card** records whether a person has checked the card against its source document. `yes` means checked. `no` means the card was built and checked by script but not yet reviewed by a person. Use both kinds of cards. If a user questions a number from a card marked `no`, suggest checking it against the `open_copy` or DOI.

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
- Explicitly identify outside research from general knowledge or the web as **additional evidence from outside the knowledge base**, not as verified content of this knowledge base. External cards are part of the knowledge base, so this label does not apply to them. Never invent sources, identifiers, numbers or institutional decisions.
- If the evidence is insufficient, explain the gap and what would be needed to resolve it.
- Treat the cards' `not_established` field, when present, as an explicit boundary on claims.

## The people behind the work

Answers should feel like talking to someone who knows the field and its people, not like querying a database. Read `people.md` whenever an answer credits authors, and always before naming anyone as a contact, including when the user asks who the experts are. Its rules govern attribution, names, referrals, consent and privacy. The non-negotiable ones are these.

- Credit work, never voice. Cite by first author and credit who led the work, as `people.md` records.
- Suggest a contact only when `Contact` starts with `yes`, through the institutional channel listed, and only when the user asks or a specific open question needs a person. Never reveal who declined or is pending.
- Never search for, fetch or display photos of people, or share personal emails, phone numbers or social media handles.

## R packages and software

The packages behind tricot analysis (PlackettLuce, gosset, ClimMobTools, climatrends, chirps) are actively maintained, and function names and arguments change between versions. The cards record the CRAN version on the date they were checked. Before giving code or naming functions, check the package's current CRAN page and reference manual at `https://CRAN.R-project.org/package=<name>`, and say which version the advice applies to. Treat ClimMob and the tools built into it the same way, checking climmob.net.

## Grey literature

Guides, reports, briefs, conference papers and presentations have no DOI. Their `doi` field holds a repository handle (CGSpace, CIMMYT or Brage, starting with https://hdl.handle.net/), which works as a permanent link. Cite them by authors, year, title and handle. Team flyers (`type: flyer`) have no handle and never will; cite them by authors, year and title with the link in `open_copy`. If any other card has an empty `doi`, cite it by title, authors and year, and say the link is pending.

## How papers connect

Cards declare how they relate to other cards in a `relations` list, using terms from the Citation Typing Ontology (CiTO, http://purl.org/spar/cito/). The full graph with inverse links is in `index.json` (each paper's `relations`) and in `relations.jsonld`.

- **extends** builds on the earlier work. Use it to tell a line of work in order.
- **reviews** and **discusses** summarize or describe the other paper. Prefer the original for numbers.
- **updates** gives newer information. Report the newer figure with its date and mention the older one.
- **usesDataFrom** and **usesMethodIn** reuse data or a method from the other paper.
- **citesAsDataSource** takes a number from the other paper. Always give the figure from the original. The note says when the citing paper reports it differently.
- **agreesWith** and **disagreesWith** reach a matching or conflicting conclusion. Say so when it matters.

Lines of work worth knowing:

- **Genebank to farm (durum wheat, Ethiopia).** mancini-2017-scirep → vanetten-2019-pnas → desousa-2021-commsbio (3D-breeding) → gesesse-2023-pnas, reviewed in fadda-2020-fps. The early papers are not tricot trials but are its pre-breeding basis.
- **Product concept testing.** rutsaert-2023-mib → donovan-2025-expagric, with mbugua-2024-mib applying the method to sorghum.
- **Farmer-measured yield.** nabateregga-2025-eja and ulzen-2025-agrirxiv agree that volumetric measurement by farmers is accurate.
- **Farmer feedback.** schumann-2024-ux → muller-2025-ux.
- **Who hosts on-farm trials.** kool-2020-expagric and laajaj-2020-scirep (external) show that researcher-chosen hosts and undefined research populations limit what on-farm trials can predict. cairns-2025-ppp tests a farm typology for choosing hosts, and cairns-2026-jxb builds on it.
- **Participation and its institutionalization.** hansson-2019-ejps on farmers' own experiments, vandegevel-2020-asd on citizen science as a renewal of participatory research, and occelli-2026-ahv on why national policy lags participatory practice.
- **Trait preferences and data standards.** thiele-2021-ijfst and occelli-2024-natplants on how consumer and trait preferences are studied, arnaud-2023-jsfa and dumschott-2023-fps on linking them to breeding data through the Crop Ontology, and carroll-2020-dsj on the CARE principles that complement FAIR.

## Topic map

Card ids grouped by question area and by crop, newest first. A card can appear under several headings. Each id opens as `papers/<id>.md`. The full table with the gist of every paper is in `index.md`. Both are generated from the cards, so do not edit them by hand.

<!-- topics:start -->
### By question

- **Origins of tricot, guides and the handbook.** chase-2026-book, angudubo-2026-guide, desousa-2024-asd, vanetten-2020-guide, vanetten-2019-expagric, steinke-2016-guide, vanetten-2011-idsbull
- **Trial design, sample size and data quality.** chase-2026-book, cairns-2026-jxb, 1000farms-2025-report, quiros-2024-compag, occelli-2024-natplants, desousa-2024-asd, vanetten-2020-rtbwp, laajaj-2020-scirep, kool-2020-expagric, steinke-2017-asd
- **Who hosts trials and representativeness.** cairns-2026-jxb, cairns-2025-ppp, laajaj-2020-scirep, kool-2020-expagric
- **Ranking data analysis and statistics.** dorado-2026-tag, daudi-2026-fes, chase-2026-book, kang-2025-expagric, nanyonjo-2024-cropsci, mulatu-2024-slides, desousa-2024-asd, olaosebikan-2023-jsfa, gesesse-2023-pnas, desousa-2023-softwarex, brown-2023-agronj, woldeyohannes-2022-elife, brown-2022-cropsci, moyo-2021-fsufs, turner-2020-compstat, vanetten-2019-pnas, steinke-2017-asd
- **Climate and environmental covariates.** jorgensen-2026-gse, kang-2025-expagric, nanyonjo-2024-cropsci, desousa-2023-joss, brown-2023-agronj, woldeyohannes-2022-elife, brown-2022-cropsci, fadda-2020-fps, desousa-2020-joss, vanetten-2019-pnas
- **Gender, social inclusion and farmer segments.** kadege-2026-fsufs, daudi-2026-fes, chase-2026-book, voss-2025-ppp, sharma-2025-jafr, kang-2025-expagric, cairns-2025-ppp, desousa-2024-asd, voss-2023-fsoc, vanetten-2023-pnas, teeken-2023-slides, woldeyohannes-2022-elife, voss-2021-outlook, thiele-2021-ijfst, teeken-2021-fsufs, moyo-2021-fsufs, vanetten-2020-rtbwp, vandegevel-2020-asd, vanetten-2019-expagric, steinke-2019-plosone, mancini-2017-scirep
- **Trait preferences, product profiles and demand-led breeding.** kadege-2026-fsufs, daudi-2026-fes, chase-2026-book, voss-2025-ppp, mawia-2025-fsufs, donovan-2025-expagric, 1000farms-2025-report, occelli-2024-natplants, mulatu-2024-slides, mbugua-2024-mib, vanetten-2023-pnas, teeken-2023-slides, rutsaert-2023-mib, arnaud-2023-jsfa, voss-2021-outlook, thiele-2021-ijfst, teeken-2021-fsufs
- **Consumer testing and food quality.** nanyonjo-2024-cropsci, teeken-2023-slides, olaosebikan-2023-jsfa, arnaud-2023-jsfa, alamu-2023-jsfa, thiele-2021-ijfst, teeken-2021-fsufs, moyo-2021-fsufs
- **Product concept testing and seed choice.** mawia-2025-fsufs, donovan-2025-expagric, mbugua-2024-mib, rutsaert-2023-mib
- **Genebanks, genomics and pre-breeding.** dorado-2026-tag, cairns-2026-jxb, selby-2025-database, vanetten-2023-pnas, gesesse-2023-pnas, alamu-2023-jsfa, woldeyohannes-2022-elife, thiele-2021-ijfst, tanaka-2021-tag, desousa-2021-commsbio, fadda-2020-fps, mancini-2017-scirep
- **Yield measured by farmers and genetic gain.** dorado-2026-tag, ulzen-2025-agrirxiv, nabateregga-2025-eja, 1000farms-2025-report, vanetten-2020-rtbwp
- **Costs and budgeting.** chase-2026-book, angudubo-2026-zari, angudubo-2026-naro, angudubo-2026-guide, 1000farms-2025-report, occelli-2024-agecon, desousa-2024-asd, vanetten-2020-rtbwp, laajaj-2020-scirep, vanetten-2019-expagric
- **Farmer motivation, participation and feedback.** occelli-2026-ahv, jorgensen-2026-gse, goormachtigh-2026-flyer, chase-2026-book, muller-2025-ux, schumann-2024-ux, voss-2021-outlook, vanetten-2020-guide, vandegevel-2020-asd, vanetten-2019-expagric, hansson-2019-ejps, beza-2017-plosone
- **Impact, adoption, variety release and institutionalization.** occelli-2026-ahv, daudi-2026-fes, muller-2025-ux, mawia-2025-fsufs, howland-2025-report, 1000farms-2025-report, occelli-2024-agecon, nanyonjo-2024-cropsci, desousa-2024-asd, teeken-2023-slides, voss-2021-outlook, thiele-2021-ijfst, gotor-2021-fsufs, vandegevel-2020-asd, laajaj-2020-scirep
- **AI and digital tools for data collection.** goormachtigh-2026-flyer, cairns-2026-jxb, beza-2017-plosone, vanetten-2011-idsbull
- **Data standards, ontologies and software.** chase-2026-book, selby-2025-database, quiros-2024-compag, occelli-2024-natplants, dumschott-2023-fps, desousa-2023-softwarex, desousa-2023-joss, arnaud-2023-jsfa, vanetten-2020-rtbwp, turner-2020-compstat, desousa-2020-joss, carroll-2020-dsj

### By crop

- **amaranth and other opportunity crops.** voss-2025-ppp, woldeyohannes-2022-elife
- **banana.** brown-2023-agronj
- **cassava.** nanyonjo-2024-cropsci, teeken-2023-slides, olaosebikan-2023-jsfa, alamu-2023-jsfa, teeken-2021-fsufs
- **common bean.** kadege-2026-fsufs, angudubo-2026-naro, nabateregga-2025-eja, occelli-2024-agecon, brown-2022-cropsci
- **forages.** jorgensen-2026-gse, mulatu-2024-slides
- **groundnut.** daudi-2026-fes
- **maize.** cairns-2026-jxb, angudubo-2026-zari, mawia-2025-fsufs, donovan-2025-expagric, cairns-2025-ppp, voss-2023-fsoc, rutsaert-2023-mib, voss-2021-outlook, laajaj-2020-scirep
- **potato.** sharma-2025-jafr, kang-2025-expagric
- **rice.** tanaka-2021-tag, gotor-2021-fsufs
- **sorghum.** mbugua-2024-mib
- **sweetpotato.** moyo-2021-fsufs
- **teff.** woldeyohannes-2022-elife
- **wheat.** gesesse-2023-pnas, gotor-2021-fsufs, desousa-2021-commsbio, fadda-2020-fps, mancini-2017-scirep
<!-- topics:end -->
