# Pilot summary: claim-by-claim review of five cards

Run on 2026-11-20. Each card was checked by an independent agent that read the full source and did not write the card. The most important finding in each report was then checked again by hand against the PDF.

## Results

| Card | Type | Claims checked | Supported | Imprecise | Not in source | Contradicted | Important omissions | Verdict |
|---|---|---|---|---|---|---|---|---|
| desousa-2024-asd | research article | 69 | 50 | 16 | 2 | 1 | 12 | Minor fixes |
| occelli-2024-natplants | review | 59 | 47 | 10 | 0 | 2 | 7 | Major fixes |
| mancini-2017-scirep | research article | 59 | 50 | 6 | 3 | 0 | 10 | Minor fixes |
| angudubo-2026-naro | grey literature report | 67 | 60 | 7 | 0 | 0 | 7 | Minor fixes |
| mulatu-2024-slides | presentation | 42 | 29 | 11 | 2 | 0 | 7 | Major fixes |

Across the five cards, 236 of 296 claims (80%) are fully supported. None of the cards is badly wrong. All five need edits before `curated_card` can be set to yes.

## Most important finding per card (checked by hand)

- **occelli-2024-natplants.** The card says twice that the review places tricot under "direct experience". Fig. 2 (p. 404) places tricot in the "Questions" category, next to preference voting.
- **desousa-2024-asd.** The Key numbers row says tricot is about 40% cheaper "vs PVS". The paper says about 40% cheaper than RCBD (p. 6). The card's own summary and not_established already say RCBD, so the card contradicts itself.
- **mancini-2017-scirep.** The last summary paragraph presents later work (fadda-2020, vanetten-2019, gesesse-2023) as if the 2017 paper said it. The paper also has a text versus Table 1 conflict. The text gives the four end-use traits to women in Hagreselam, but Table 1 lists them under women in Geregera. The card does not flag it. The card has no not_established field.
- **angudubo-2026-naro.** The arithmetic is correct, but derived numbers are not labelled as the card's own. The two single scenarios save USD 3,393.7 and USD 1,001.8, which add up to USD 4,395.5. The combined scenario saves only USD 4,012.8 (p. 11), so "adding" the savings in the summary is misleading. The gist should say "marginal cost".
- **mulatu-2024-slides.** The card describes the methods but reports none of the results on slides 10 to 12. The summary is under the 400-word minimum. The slides give n = 383 and n = 354 with no unit, but the card calls them farmers.

## What the automated check missed

Layer 1 found none of the five findings above. It confirms that numbers exist in the source, not that they are used correctly. The claim-by-claim review is needed for every card.

## Patterns to expect in the remaining cards

1. **Wording more certain than the source.** "Shows" where the paper says "may" or "is being tested".
2. **Outside knowledge in the summary.** Links to later papers, programme names (Seeds for Needs) or names not in the source, written as if the paper said them. These belong in Notes.
3. **Derived numbers not labelled.** Sums, percentages and conversions computed by the card writer.
4. **Inconsistencies in the source not flagged.** Text versus table, or text versus caption (desousa-2024: maize versus potato in Rwanda).
5. **Missing or weak not_established.** Absent in two of five cards.
6. **Gist that lists topics** rather than saying what the paper shows.
7. **Secondhand numbers credited to the wrong source**, in either direction.

## Changes to the method before the full run

- Add a separate status for problems in the source itself, so they are not counted as card errors.
- Tell reviewers that semicolons are required as separators in not_established.
- Ask reviewers to mark values read from charts as approximate.
- Split chase-2026-book (315 pages) by chapter across several reviewers.
- Skip howland-2025-report and vanetten-2011-idsbull until the full PDFs are in the repo.
- Add a final cross-card pass for facts that several cards state differently, for example the 373 + 27 versus 400 with 25 modern varieties panel, and the 28% versus 40% cost figures.

## Effort

Each review took about five minutes and a full reading of the source. The remaining 65 cards can run in batches of about eight.
