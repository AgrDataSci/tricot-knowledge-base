# Building the tricot knowledge base

This folder is a Claude skill. It lets any user ask questions about tricot and on-farm testing and get answers grounded in the team's open-access papers, as if talking to someone who knows that literature well. It is the literature layer of our AI-ready documentation, next to the data (tricot, EBS, CHIRPS).

The skill must stay light because it travels between users. Only `SKILL.md` loads every time. Paper cards load one by one, only when a question needs them.

## Folder structure

```
tricot-knowledge-base/
├── SKILL.md              # instructions + index (generated, do not edit the table by hand)
├── TEMPLATE.md           # copy this to start a new card
├── README.md             # this file (not needed by Claude, safe to keep)
├── papers/               # one card per paper, named <id>.md
├── scripts/build_index.py
└── tests/                # format comparison; remove before packaging
```

## Short or long card

Every card has the metadata, a 400 to 500 word summary, key numbers and notes.

Use the **long format** for method-heavy and landmark papers. It adds three sections, "Questions this paper answers", "Methods in brief" and "Stated limitations". In our test (`tests/comparison-short-vs-long.md`) the long card answered all five expert questions better, mostly on the practical "how" side.

Use the **short format** for perspectives, commentaries and narrow case studies.

Target size is about 6 KB for a short card and about 10 KB for a long one.

## Workflow for each paper

1. **Extract the text from the PDF.** `pdftotext -layout paper.pdf paper.txt`. Cut everything after the reference list starts. Keep figure and table captions.
2. **Draft the card.** Copy `TEMPLATE.md` to `papers/<id>.md`. Giving Claude the PDF text and the template works well. Ask for the card in the template format, summary in its own words.
3. **Verify every number against the PDF.** This is the step that matters most. Check each value in the key-numbers table and in the summary. Record any text vs table mismatch in Notes.
4. **Fill the primary-source column.** If the paper reports a number from another study, name that study. Users must cite the original, not the paper that repeats it.
5. **Find a stable open copy.** Publisher pages often block automated reading (Springer and PNAS both did in our test). Prefer PMC, an institutional repository (CGSpace, HU Berlin edoc), or our GitHub markdown.
6. **Cross-check against other cards.** If two papers report the same fact differently, note it in both cards. Example, Cairns et al. 2026 cites ">150,000 farmers" where de Sousa et al. 2024 reports ~150,000 plots.
7. **Rebuild the index.** `python scripts/build_index.py`. It reads the front matter of every card, checks required fields, and rewrites the table in `SKILL.md`.

## Writing rules

- Summaries in your own words. Do not paste paragraphs from the paper, even for open-access articles.
- Plain, assertive prose. Concise paragraphs. No em-dashes.
- `gist` under 30 words. It is the only text from the card that loads every time, so make it count.
- `keywords` are the terms a user would type, not the paper's formal keyword list.
- Never add a number you cannot find in the PDF.

## Packaging

1. Delete `tests/` (and optionally `README.md` and `TEMPLATE.md`).
2. Run `python scripts/build_index.py` one last time.
3. Zip the folder and upload it as a skill.

At 50 papers expect `SKILL.md` around 15 KB and the whole folder around 400 KB unzipped.
