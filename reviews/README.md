# Card reviews

Checks of the paper cards in `papers/` against their source PDFs in `papers-pdf/`. These files are working notes for the core team. They are not part of the knowledge base and assistants should not answer from them.

## Files

- `00-layer1-automated-check.md`. An automated check of all cards. It confirms that the DOI, title, author surnames and every number in each card appear in the source PDF.
- `01-pilot-summary.md`. Results of the pilot: a claim-by-claim review of five cards, the patterns found, and changes to the method before the full run.
- `REVIEW_TEMPLATE.md`. The format every card review follows.
- `<card-id>.md`. One review per card, with a verdict, a claim-by-claim table, omissions, and replacement text ready to paste.

## How a review works

An independent reviewer that did not write the card reads the whole source. It splits the card into individual claims and labels each one Supported, Imprecise, Not in source or Contradicted, with page numbers. It then lists important content the card leaves out. The main finding of each review is checked again by hand against the PDF. A card's `curated_card` field is set to yes only after a person has read the review and the fixes are in.

## Status

Review and correction done in November 2026.

- 68 cards reviewed claim by claim against their source PDFs, one review per card in this folder. The main finding of each review was checked again by hand (`02-spotcheck-log.md`).
- All 68 cards corrected in PR #19 to #26, with one change log per card in `changes/`. Each change was confirmed in the source before it was applied.
- All corrected cards set to `curated_card: yes` (PR #21 to #27), as decided by the curator.

Still open:

- howland-2025-report, vanetten-2011-idsbull and eskridge-1992-tag: the PDFs in `papers-pdf/` are one-page link stubs, so these cards wait for the full texts.
- chase-2026-book: not yet reviewed.
- Facts that cards state differently, listed in `03-crosscard-notes.md`.

## Other files

- `REVIEWER_INSTRUCTIONS.md` and `FIXER_INSTRUCTIONS.md`: the instructions given to the review and fix agents. They refer to working paths outside this repository.
