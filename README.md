<!-- badges: start -->
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-%233182bd)](https://creativecommons.org/licenses/by/4.0/)
<!-- badges: end -->

# Tricot knowledge base

An AI-ready knowledge base of the open-access literature on tricot, on-farm testing and product testing with farmers and consumers. Each paper is distilled into a short, verified markdown card with its main argument, methods, stated limitations, key numbers and links to the underlying data and code.

The repository works as a [Claude skill](SKILL.md), so an AI assistant can answer questions the way a colleague who knows this literature would. It cites the papers, reports numbers with their primary sources, and says where the evidence is thin. The cards are plain markdown, so people and other AI tools can read them directly.

This is the literature layer of the team's AI-ready documentation, alongside these repositories.

| Repository | Layer | Content |
|---|---|---|
| **tricot-knowledge-base** | Literature | Paper cards and the expert skill (this repository) |
| [tricot-data](https://github.com/AgrDataSci/tricot-data) | Data | Harmonized tricot trial data in JSON, archived on Zenodo |
| [tricot-protocols](https://github.com/AgrDataSci/tricot-protocols) | Methods | Standard operating procedures, surveys and trait metadata |

## What you can ask

- How many farmers and entries does a tricot trial need?
- Are farmer rankings valid compared with researcher measurements?
- How do I get yield data that a release committee will accept?
- How does tricot compare in cost with RCBD trials or group PVS?
- What does the evidence say about climate effects on variety performance?

## Use it

**In Claude.** Download this repository as a zip and upload it as a skill. Claude loads the index in `SKILL.md` whenever a question touches tricot or on-farm testing, and opens only the paper cards it needs.

**In Claude Code.** Clone the repository into your skills directory, or install it from the AI-ready documentation marketplace once that is published.

**With other AI tools or by hand.** Start from the index table in [`SKILL.md`](SKILL.md), then open the relevant cards in [`papers/`](papers/). Each card names an open full-text copy and, where available, the dataset behind the paper.

## What's inside

```
tricot-knowledge-base/
├── SKILL.md               # skill instructions and paper index (index is generated)
├── papers/                # one card per paper, named <id>.md
├── TEMPLATE.md            # template for new cards
├── scripts/build_index.py # rebuilds the index in SKILL.md from the cards
├── tests/                 # evaluation of card formats
├── metadata/              # FAIR metadata for Zenodo releases
├── CITATION.cff
└── LICENSE
```

## Paper cards

Every card has YAML metadata (DOI, open copy, license, data, keywords, a one-line gist), a 400 to 500 word summary in our own words, a key-numbers table and notes on discrepancies.

Method-heavy and landmark papers use the **long format**, which adds "Questions this paper answers", "Methods in brief" and "Stated limitations". In our test the long card answered all five expert questions better than the short one (see [`tests/comparison-short-vs-long.md`](tests/comparison-short-vs-long.md)). Perspectives, commentaries and narrow case studies use the **short format**.

Two rules make the cards trustworthy.

- **Every number is checked against the PDF.** Mismatches between text and tables, or between papers, are recorded in the card's notes.
- **Numbers carry their primary source.** When a paper reports a figure from another study, the card names that study, so users cite the original.

## Contribute a card

1. Extract the text from the PDF with `pdftotext -layout paper.pdf paper.txt`, and drop everything after the reference list. Keep PDFs in `papers-pdf/`, which git ignores.
2. Copy `TEMPLATE.md` to `papers/<id>.md`, with the id as `firstauthor-year-journalabbrev`, for example `vanetten-2019-pnas`.
3. Draft the card. Giving Claude the PDF text and the template works well. Ask for the summary in its own words.
4. Verify every number against the PDF and fill the primary-source column.
5. Add a stable open copy. Publisher pages often block automated reading, so prefer PMC or an institutional repository such as CGSpace.
6. Cross-check against existing cards and note any disagreement in both.
7. Run `python scripts/build_index.py` to rebuild the index, then open a pull request.

Writing rules for cards are plain, assertive prose in concise paragraphs, no pasted text from the papers, no em-dashes, a `gist` under 30 words, and `keywords` written as a user would search.

## Cite

Cite the original papers for any finding you use. To cite the knowledge base itself, use [`CITATION.cff`](CITATION.cff).

## License

Paper cards and documentation are released under [CC BY 4.0](LICENSE). Each paper keeps its own license, listed in its card.
