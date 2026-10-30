---
id: firstauthor-year-journalabbrev          # must match the file name, e.g. vanetten-2019-pnas
title: Full article title
authors: Surname AB, Surname C, ...          # first author first; "and N co-authors" is fine for long lists
year: 2024
journal: Full journal name
journal_short: Short journal name            # used in the index, e.g. PNAS, J Exp Bot
article: volume(issue), pages or article number
type: research article | review | perspective | software paper | preprint | book | guide | working paper | report | policy brief | presentation
doi: https://doi.org/...                     # or the repository handle (https://hdl.handle.net/...) for grey literature
open_copy: stable open full-text URL (PMC, institutional repository, or our GitHub markdown); may be empty
license: CC BY 4.0                            # as stated in the PDF; otherwise "see CGSpace record"
data: dataset DOI or repository, and where the code lives; "none" if not applicable
software: R package, https://CRAN.R-project.org/package=<name> (vX.Y on CRAN, published YYYY-MM-DD, checked YYYY-MM-DD)   # optional; always check the current CRAN version
crops: crops covered
region: countries or regions
keywords: 8 to 12 comma-separated terms a user would search for
gist: One sentence, under 30 words, saying what the paper shows
not_established: Optional. Claims this paper is likely to be stretched to but does not support, separated by semicolons
relations:                                   # optional; one per line, CiTO terms, target is a card id
  - extends: other-card-id                   # extends | reviews | updates | usesDataFrom | usesMethodIn | citesAsDataSource | agreesWith | disagreesWith | discusses
  - citesAsDataSource: other-card-id  # a short note after a hash, e.g. when the number is reported differently
---

## Questions this paper answers

<!-- LONG FORMAT ONLY. 4 to 7 plain-language questions a user would actually ask. -->

## Summary

<!-- 400 to 500 words, in your own words. The argument, what was done, what was found, why it matters. -->

## Methods in brief

<!-- LONG FORMAT ONLY. Bullets on design, sample size, data collection, analysis, and any practical protocol. -->

## Stated limitations

<!-- LONG FORMAT ONLY. What the authors themselves say does not hold, was not tested, or remains open. -->

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| value | what it measures, where and when | "This paper", or the original source if the paper cites it secondhand |

## Notes

<!-- Discrepancies (text vs table, or vs another card), numbers to double-check, and pointers to related cards by id. -->
