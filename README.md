<!-- badges: start -->
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-%233182bd)](https://creativecommons.org/licenses/by/4.0/)
<!-- badges: end -->

# Tricot knowledge base

> Kauê de Sousa, Brayden Youngberg, Rachel Chase

An AI-ready knowledge base of the open-access literature on tricot, on-farm testing and product testing with farmers and consumers. Each paper, report or guide is distilled into a verified markdown card with the questions it answers, its main argument, methods, stated limitations, key numbers with their primary sources, and links to the underlying data and code.

The repository works as a [Claude skill](SKILL.md), so an AI assistant can answer questions the way a colleague who knows this literature would. It cites the papers, reports numbers with their primary sources, and says where the evidence is thin. The cards are plain markdown, so people and other AI tools can read them directly.

This is the literature layer of [AI-ready documentation for tricot](https://github.com/AgrDataSci/ai-ready-documentation), alongside [tricot-protocols](https://github.com/AgrDataSci/tricot-protocols) and [tricot-data](https://github.com/AgrDataSci/tricot-data).

## What you can ask

- How many farmers and entries does a tricot trial need?
- Are farmer rankings valid compared with researcher measurements?
- How do I get yield data that a release committee will accept?
- How does tricot compare in cost and impact with RCBD trials or group PVS?
- What does the evidence say about climate effects on variety performance?
- How do I analyze tricot rankings in R, and with which packages?
- How can tricot test consumer preferences or new product concepts?

## Status

| | Count |
|---|---|
| Source documents in `papers-pdf/` | 38 |
| Cards in `papers/` | 38 |
| Cards still waiting for a CGSpace handle | 9 |

Every source document has a long-format card. `python scripts/build_index.py` lists the cards that still need a handle.

### What the cards cover

| Topic | Cards |
|---|---|
| Origins, guides and the handbook | vanetten-2019-expagric, steinke-2016-guide, vanetten-2020-guide, vanetten-2020-rtbwp, desousa-2024-asd, chase-2026-book |
| Data quality, motivation and impact | steinke-2017-asd, beza-2017-plosone, occelli-2024-agecon, nabateregga-2025-eja |
| Climate, genomics and analysis methods | vanetten-2019-pnas, desousa-2021-commsbio, brown-2022-cropsci, dorado-2026-verixiv, vanetten-2023-pnas, cairns-2026-jxb |
| Software (R packages and ClimMob) | turner-2020-compstat, desousa-2023-softwarex, desousa-2020-joss, desousa-2023-joss, quiros-2024-compag |
| Crop applications | angudubo-2024-cropsci (cassava), daudi-2026-fes (groundnut), kang-2025-expagric and sharma-2025-jafr (potato), voss-2025-ppp (amaranth) |
| Consumer and product concept testing | moyo-2021-fsufs, alamu-2023-jsfa, olaosebikan-2023-jsfa, donovan-2025-expagric, rutsaert-2023-mib, mbugua-2024-mib |
| Gender, inclusion and farmer feedback | voss-2023-fsoc, teeken-2023-slides, schumann-2024-ux, muller-2025-ux, steinke-2019-plosone |
| Mainstreaming in breeding | 1000farms-2025-report |

## Use it

**In Claude.** Package the skill without the source PDFs (see [Packaging](#packaging)) and upload the zip as a skill. Claude loads the index in `SKILL.md` whenever a question touches tricot or on-farm testing, and opens only the cards it needs.

**In Claude Code.** Clone the repository into your skills directory, or install it from the [AI-ready documentation](https://github.com/AgrDataSci/ai-ready-documentation) repository once its plugin marketplace is published.

**With other AI tools or by hand.** Start from the index table in [`SKILL.md`](SKILL.md), then open the relevant cards in [`papers/`](papers/). Each card names an open full-text copy and, where available, the dataset behind the paper.

## What's inside

```
tricot-knowledge-base/
├── SKILL.md               # skill instructions and paper index (index is generated)
├── papers/                # one card per paper, named <id>.md
├── papers-pdf/            # source PDFs used to build the cards (not part of the skill)
├── TEMPLATE.md            # template for new cards
├── scripts/build_index.py # rebuilds the index in SKILL.md from the cards
├── tests/                 # evaluation of card formats
├── CITATION.cff
└── LICENSE
```

## Paper cards

Every card follows the long format in [`TEMPLATE.md`](TEMPLATE.md). It has YAML metadata (DOI, open copy, license, data, software, keywords, a one-line gist), questions the paper answers, a summary of about 450 words in our own words, methods in brief, stated limitations, a key-numbers table and notes. In our test the long format answered expert questions better than a summary alone (see [`tests/comparison-short-vs-long.md`](tests/comparison-short-vs-long.md)).

Four rules make the cards trustworthy.

- **Every number is checked against the PDF.** All numbers in all 38 cards were matched against the full text of their source by script. Mismatches between text and tables, or between papers, are recorded in the notes.
- **Numbers carry their primary source.** When a paper reports a figure from another study, the card names that study, so users cite the original.
- **R packages point to CRAN.** PlackettLuce, gosset, ClimMobTools, climatrends and chirps change over time, so cards record the CRAN version and date checked, and the skill tells the assistant to check the current version before giving code.
- **Grey literature is labelled.** Guides, reports, briefs and presentations have their type in the index, and items published on CGSpace have an empty `doi` until their handle is added.

Some PDF file names do not match the first author. Nanyonjo-et-al-2024 is Angudubo et al. 2024, van-Etten-et-al-2016 is Steinke and van Etten 2016, and Moyo-et-al-2020 was published in 2021. Each card notes this.

## Contribute a card

1. Pick a PDF from `papers-pdf/` and extract its text with `pdftotext -layout file.pdf file.txt`. Drop everything after the reference list and keep figure and table captions.
2. Copy `TEMPLATE.md` to `papers/<id>.md`, with the id as `firstauthor-year-journalabbrev`, for example `vanetten-2019-pnas`.
3. Draft the card. Giving Claude the extracted text and the template works well. Ask for the summary in its own words.
4. Verify every number against the PDF and fill the primary-source column. For R packages, record the current CRAN version in `software`.
5. Add a stable open copy. Publisher pages often block automated reading, so prefer PMC or an institutional repository such as CGSpace. If there is no DOI, leave `doi` empty and add the CGSpace handle when it exists.
6. Cross-check against existing cards and note any disagreement in both.
7. Run `python scripts/build_index.py` to rebuild the index, then open a pull request.

Writing rules for cards are plain, assertive prose in concise paragraphs, no pasted text from the papers, no em-dashes, a `gist` under 30 words, and `keywords` written as a user would search.

## Packaging

The skill must stay light because it travels between users. Package only what Claude needs.

```bash
python scripts/build_index.py
mkdir -p build/tricot-knowledge-base
cp -r SKILL.md papers build/tricot-knowledge-base/
cd build && zip -r ../tricot-knowledge-base.zip tricot-knowledge-base
```

`papers-pdf/`, `tests/` and `scripts/` stay in the repository and out of the skill. The packaged skill is about 340 KB unzipped and 110 KB zipped.

## Cite

To cite the knowledge base, use [`CITATION.cff`](CITATION.cff).

> de Sousa K, Youngberg B, Chase R (2026). Tricot knowledge base. An AI-ready synthesis of the literature on decentralized on-farm testing. Version 0.1.0. https://github.com/AgrDataSci/tricot-knowledge-base

Cite the original papers for any finding you use.

## License

Paper cards and documentation are released under [CC BY 4.0](LICENSE). The PDFs in `papers-pdf/` keep their original licenses, listed in each paper's card.
