<!-- badges: start -->
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-%233182bd)](https://creativecommons.org/licenses/by/4.0/)
<!-- badges: end -->

# Evidence base on product testing with users in agriculture

*An AI-ready synthesis of the literature*

> Kauê de Sousa, Brayden Youngberg, Rachel Chase, Marie-Angélique Laporte

**AI assistants:** before answering any question from this repository, read [`SKILL.md`](SKILL.md) for the answering rules and paper index, and [`people.md`](people.md) before crediting or suggesting anyone. See also [`AGENTS.md`](AGENTS.md).

An AI-ready knowledge base of the open-access literature on tricot, on-farm testing and product testing with farmers and consumers. Each paper, report or guide is distilled into a verified markdown card with the questions it answers, its main argument, methods, stated limitations, key numbers with their primary sources, and links to the underlying data and code.

The repository works as a [Claude skill](SKILL.md), so an AI assistant can answer questions the way a colleague who knows this literature, and the people behind it, would. It credits the authors by name, reports numbers with their primary sources, says where the evidence is thin and, where authors agree, suggests who to talk to next. The cards are plain markdown, so people and other AI tools can read them directly.

This is the literature layer of [AI-ready documentation for tricot](https://github.com/AgrDataSci/ai-ready-documentation), alongside [tricot-protocols](https://github.com/AgrDataSci/tricot-protocols) and [tricot-data](https://github.com/AgrDataSci/tricot-data).

## What you can ask

- How many farmers and entries does a tricot trial need?
- Are farmer rankings valid compared with researcher measurements?
- How do I get yield data that a release committee will accept?
- How does tricot compare in cost and impact with RCBD trials or group PVS?
- What does the evidence say about climate effects on variety performance?
- How do I analyze tricot rankings in R, and with which packages?
- How can tricot test consumer preferences or new product concepts?
- How can I work with women in tricot trials?

## Status

| | Count |
|---|---|
| Source documents in `papers-pdf/` | 47 |
| Cards in `papers/` | 47 |
| Cards still waiting for a handle or DOI | 0 |
| People in `people.md` | 16 (3 contacts confirmed, 13 pending) |
| Links between cards | 17 |

Every source document has a long-format card. `python scripts/build_index.py` lists the cards that still need a handle, and `index.json` records the current version.

### What the cards cover

| Topic | Cards |
|---|---|
| Pre-breeding with genebanks (Seeds for Needs) | mancini-2017-scirep, fadda-2020-fps, gesesse-2023-pnas |
| Origins, guides and the handbook | vanetten-2019-expagric, steinke-2016-guide, vanetten-2020-guide, vanetten-2020-rtbwp, desousa-2024-asd, chase-2026-book |
| Data quality, motivation and impact | steinke-2017-asd, beza-2017-plosone, gotor-2021-fsufs, occelli-2024-agecon, nabateregga-2025-eja, ulzen-2025-agrirxiv |
| Climate, genomics and analysis methods | vanetten-2019-pnas, desousa-2021-commsbio, brown-2022-cropsci, dorado-2026-tag, vanetten-2023-pnas, cairns-2026-jxb |
| Software and data standards (R packages, ClimMob, BrAPI) | turner-2020-compstat, desousa-2023-softwarex, desousa-2020-joss, desousa-2023-joss, quiros-2024-compag, selby-2025-database |
| Crop applications | nanyonjo-2024-cropsci (cassava), daudi-2026-fes (groundnut), kang-2025-expagric and sharma-2025-jafr (potato), voss-2025-ppp (amaranth), mulatu-2024-slides and jorgensen-2026-gse (forages, Ethiopia and Norway) |
| Consumer and product concept testing | moyo-2021-fsufs, alamu-2023-jsfa, olaosebikan-2023-jsfa, donovan-2025-expagric, rutsaert-2023-mib, mbugua-2024-mib |
| Gender, inclusion and farmer feedback | teeken-2021-fsufs, voss-2023-fsoc, teeken-2023-slides, schumann-2024-ux, muller-2025-ux, steinke-2019-plosone |
| Mainstreaming in breeding | 1000farms-2025-report |

## Use it

**In Claude.** Download the [latest skill package](https://github.com/AgrDataSci/tricot-knowledge-base/releases/latest/download/tricot-knowledge-base.zip) and upload it under Customize > Skills. Code execution must be on, and on Team or Enterprise plans an owner may need to allow skills. Claude loads the index in `SKILL.md` whenever a question touches tricot or on-farm testing, and opens only the cards it needs.

**In Claude Code.** Clone the repository into your skills directory, or install it from the [AI-ready documentation](https://github.com/AgrDataSci/ai-ready-documentation) repository once its plugin marketplace is published.

**By sharing the link.** Paste the repository link into an assistant with web access. It reads [`AGENTS.md`](AGENTS.md) and [`SKILL.md`](SKILL.md), answers from the live files, and offers to install the skill so the link is not needed next time. It installs nothing without the user's agreement.

**With other AI tools or by hand.** Start from the index table in [`SKILL.md`](SKILL.md), then open the relevant cards in [`papers/`](papers/). Each card names an open full-text copy and, where available, the dataset behind the paper.

## What's inside

```
tricot-knowledge-base/
├── SKILL.md               # skill instructions, version and paper index (generated)
├── people.md              # who is behind the papers, naming and contact consent
├── AGENTS.md              # entry point for AI agents reading the repository
├── llms.txt               # short machine-readable map of the repository
├── index.json             # machine-readable index with version, card hashes and links (generated)
├── relations.jsonld       # links between cards as JSON-LD with the CiTO vocabulary (generated)
├── papers/                # one card per paper, named <id>.md
├── papers-pdf/            # source PDFs used to build the cards (not part of the skill)
│   └── LICENSES.md        # licence and source of every PDF
├── TEMPLATE.md            # template for new cards
├── scripts/build_index.py # rebuilds the index, version and index.json from the cards
├── .github/workflows/     # rebuilds the index automatically on every push to main
├── tests/                 # evaluation of card formats
├── CITATION.cff
└── LICENSE
```

## How papers connect

Papers build on each other. A card can declare its links in a `relations` list in its front matter, using terms from the [Citation Typing Ontology (CiTO)](http://purl.org/spar/cito/), for example:

```yaml
relations:
  - extends: mancini-2017-scirep
  - citesAsDataSource: desousa-2024-asd  # cites over 150,000 farmers; the source reports about 150,000 plots
```

The terms in use are `extends`, `reviews`, `discusses`, `updates`, `usesDataFrom`, `usesMethodIn`, `citesAsDataSource`, `agreesWith` and `disagreesWith`. `scripts/build_index.py` checks that every term and target is valid, adds the inverse links (for example `isExtendedBy`), lists every link in `SKILL.md`, and writes the graph to `index.json` and to [`relations.jsonld`](relations.jsonld) for ontology tools. The assistant follows these links to tell a line of work in order, for example from genebank evaluation with farmers (mancini-2017-scirep) to crowdsourced testing (vanetten-2019-pnas), 3D-breeding (desousa-2021-commsbio) and genomic selection with farmer scores (gesesse-2023-pnas), and to flag numbers that a later paper reports differently from the original.

Tagging keywords with AGROVOC terms and traits with Crop Ontology identifiers is a possible next step.

## People behind the papers

[`people.md`](people.md) lists the core team and the authors who agreed to be part of the knowledge base, with their preferred names, affiliations at the time of their latest paper, topics, the cards they led (as first author, senior author or the researcher responsible) and the cards they co-authored, and two consent fields. The skill uses it to credit people the way a colleague would ("Jill Cairns and colleagues argue..." or "in work led by Joost van Heerwaarden"), never to speak for them. It suggests a person as a contact only when they agreed, and only through an institutional email or profile page. Personal emails and phone numbers are never shared.

All consent fields start as `pending`. Update a row only after the person replies.

## Staying current

The repository is organic, so the installed skill can fall behind. Three pieces keep it current.

- **A version.** `scripts/build_index.py` computes a version from the content of every card, `people.md` and the instructions in `SKILL.md`, and writes it to `SKILL.md` and `index.json`. Unchanged content keeps the same version and date.
- **An automatic rebuild.** A GitHub Action reruns the script on every push to `main` that touches cards, `people.md` or `SKILL.md`, so the live repository always advertises its current version.
- **A check in the skill.** Once per conversation, the assistant fetches the live `index.json`, compares versions, and fetches only what changed, including the instructions in `SKILL.md`. If web access is off, it uses the installed copy.

The check needs the assistant to be able to fetch from `raw.githubusercontent.com` or `github.com`. Where that is blocked, reinstall the skill after major updates, or install it in Claude Code as a git clone and pull.

## Paper cards

Every card follows the long format in [`TEMPLATE.md`](TEMPLATE.md). It has YAML metadata (DOI, open copy, license, data, software, keywords, a one-line gist), questions the paper answers, a summary of 400 to 500 words in our own words (shorter for short sources such as slides and conference papers), methods in brief, stated limitations, a key-numbers table and notes. In our test the long format answered expert questions better than a summary alone (see [`tests/comparison-short-vs-long.md`](tests/comparison-short-vs-long.md)).

Four rules make the cards trustworthy.

- **Every number is checked against the PDF.** All numbers in all 42 cards were matched against the full text of their source by script. Mismatches between text and tables, or between papers, are recorded in the notes.
- **Numbers carry their primary source.** When a paper reports a figure from another study, the card names that study, so users cite the original.
- **R packages point to CRAN.** PlackettLuce, gosset, ClimMobTools, climatrends and chirps change over time, so cards record the CRAN version and date checked, and the skill tells the assistant to check the current version before giving code.
- **Grey literature is labelled.** Guides, reports, briefs and presentations have their type in the index, and items published on CGSpace have an empty `doi` until their handle is added.

PDF file names follow the first author and year of each source, and card IDs follow the same pattern.

## Contribute a card

1. Pick a PDF from `papers-pdf/` and extract its text with `pdftotext -layout file.pdf file.txt`. Drop everything after the reference list and keep figure and table captions.
2. Copy `TEMPLATE.md` to `papers/<id>.md`, with the id as `firstauthor-year-journalabbrev`, for example `vanetten-2019-pnas`.
3. Draft the card. Giving Claude the extracted text and the template works well. Ask for the summary in its own words.
4. Verify every number against the PDF and fill the primary-source column. For R packages, record the current CRAN version in `software`.
5. Add a stable open copy. Publisher pages often block automated reading, so prefer PMC or an institutional repository such as CGSpace. If there is no DOI, leave `doi` empty and add the CGSpace handle when it exists.
6. Cross-check against existing cards, note any disagreement in both, and add `relations` to the cards this one builds on, reviews, reuses or cites for a number.
7. Add the card's ID to the `Led` or `Also on` column of any author already in `people.md`. If the person who led the work is not listed, add a row with `pending` consent.
8. Open a pull request. The GitHub Action rebuilds the index and version when it is merged, or run `python scripts/build_index.py` yourself.

Writing rules for cards are plain, assertive prose in concise paragraphs, no pasted text from the papers, no em-dashes, a `gist` under 30 words, and `keywords` written as a user would search.

## Packaging

The skill must stay light because it travels between users. The GitHub Action builds the package on every change and publishes it as the [latest release](https://github.com/AgrDataSci/tricot-knowledge-base/releases/latest), so there is usually no need to package it by hand. To build it locally, package only what Claude needs.

```bash
python scripts/build_index.py
mkdir -p build/tricot-knowledge-base
cp -r SKILL.md people.md index.json AGENTS.md papers build/tricot-knowledge-base/
cd build && zip -r ../tricot-knowledge-base.zip tricot-knowledge-base
```

`papers-pdf/`, `tests/` and `scripts/` stay in the repository and out of the skill. The packaged skill is about 400 KB unzipped and 130 KB zipped.

## Cite

To cite the knowledge base, use [`CITATION.cff`](CITATION.cff).

> de Sousa K, Youngberg B, Chase R, Laporte MA (2026). Evidence base on product testing with users in agriculture. An AI-ready synthesis of the literature. Version 0.1.0. https://github.com/AgrDataSci/tricot-knowledge-base

Cite the original papers for any finding you use.

## License

Paper cards and documentation are released under [CC BY 4.0](LICENSE). The PDFs in `papers-pdf/` keep their original licenses, listed in [`papers-pdf/LICENSES.md`](papers-pdf/LICENSES.md). Three papers are CC BY-NC-ND and are shared unmodified for non-commercial use.
