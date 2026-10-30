<!-- badges: start -->
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-%233182bd)](https://creativecommons.org/licenses/by/4.0/)
<!-- badges: end -->

# Tricot knowledge base

> Kauê de Sousa, Rachel Chase, Brayden Youngberg

An AI-ready knowledge base of the open-access literature on tricot, on-farm testing and product testing with farmers and consumers. Each paper is distilled into a short, verified markdown card with its main argument, methods, stated limitations, key numbers and links to the underlying data and code.

The repository works as a [Claude skill](SKILL.md), so an AI assistant can answer questions the way a colleague who knows this literature would. It cites the papers, reports numbers with their primary sources, and says where the evidence is thin. The cards are plain markdown, so people and other AI tools can read them directly.

This is the literature layer of [AI-ready documentation for tricot](https://github.com/AgrDataSci/ai-ready-documentation), alongside [tricot-protocols](https://github.com/AgrDataSci/tricot-protocols) and [tricot-data](https://github.com/AgrDataSci/tricot-data).

## What you can ask

- How many farmers and entries does a tricot trial need?
- Are farmer rankings valid compared with researcher measurements?
- How do I get yield data that a release committee will accept?
- How does tricot compare in cost with RCBD trials or group PVS?
- What does the evidence say about climate effects on variety performance?

## Status

| | Count |
|---|---|
| Source documents in `papers-pdf/` | 34 |
| Paper cards in `papers/` | 3 |

Cards are being added in batches. The index in [`SKILL.md`](SKILL.md) lists every card available.

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
├── metadata/              # FAIR metadata for Zenodo releases
├── CITATION.cff
└── LICENSE
```

## Paper cards

Every card has YAML metadata (DOI, open copy, license, data, keywords, a one-line gist), a 400 to 500 word summary in our own words, a key-numbers table and notes on discrepancies.

Method-heavy and landmark papers use the **long format**, which adds "Questions this paper answers", "Methods in brief" and "Stated limitations". In our test the long card answered all five expert questions better than the short one (see [`tests/comparison-short-vs-long.md`](tests/comparison-short-vs-long.md)). Perspectives, commentaries, reports and narrow case studies use the **short format**.

Two rules make the cards trustworthy.

- **Every number is checked against the PDF.** Mismatches between text and tables, or between papers, are recorded in the card's notes.
- **Numbers carry their primary source.** When a paper reports a figure from another study, the card names that study, so users cite the original.

## Contribute a card

1. Pick a PDF from `papers-pdf/` and extract its text with `pdftotext -layout file.pdf file.txt`. Drop everything after the reference list and keep figure and table captions.
2. Copy `TEMPLATE.md` to `papers/<id>.md`, with the id as `firstauthor-year-journalabbrev`, for example `vanetten-2019-pnas`.
3. Draft the card. Giving Claude the extracted text and the template works well. Ask for the summary in its own words.
4. Verify every number against the PDF and fill the primary-source column.
5. Add a stable open copy. Publisher pages often block automated reading, so prefer PMC or an institutional repository such as CGSpace.
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

`papers-pdf/`, `tests/`, `scripts/` and `metadata/` stay in the repository and out of the skill.

## Cite

To cite the knowledge base, use [`CITATION.cff`](CITATION.cff).

> de Sousa K, Chase R, Youngberg B (2026). Tricot knowledge base. An AI-ready synthesis of the literature on decentralized on-farm testing. Version 0.1.0. https://github.com/AgrDataSci/tricot-knowledge-base

Cite the original papers for any finding you use.

## License

Paper cards and documentation are released under [CC BY 4.0](LICENSE). The PDFs in `papers-pdf/` keep their original licenses, listed in each paper's card.
