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

Pilot done on 2026-11-20 for five cards: desousa-2024-asd, occelli-2024-natplants, mancini-2017-scirep, angudubo-2026-naro, mulatu-2024-slides. No card has been edited yet.
