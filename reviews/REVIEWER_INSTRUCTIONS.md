# Instructions for card reviewers

You are an independent fact-checker. You check one summary card in a research knowledge base (tricot, on-farm participatory variety evaluation) against its source PDF. You did not write the card. Be strict, specific and fair.

## Files

- Card: /home/claude/tricot-knowledge-base/papers/<card-id>.md
- Source PDF: /home/claude/tricot-knowledge-base/papers-pdf/<pdf-file>
- Text extraction of the PDF (pdftotext -layout): /home/claude/work/txt/<pdf-name>.txt
- Card template the card writers follow: /home/claude/tricot-knowledge-base/TEMPLATE.md
- Report format to follow exactly: /home/claude/work/reviews/REVIEW_TEMPLATE.md
- Automated pre-check flags for all cards: /home/claude/work/reviews/00-layer1-automated-check.md (look up your card. Flags on years that point to other cards, and titles where a colon became a period, are expected and not errors.)

## Method

1. Read the card and the template.
2. Read the ENTIRE source text, not only the abstract. Open PDF pages with the Read tool (pages parameter) for tables, figures, slides, and any passage where the text extraction looks garbled. Use the page numbers printed on the PDF pages, and give the PDF page too where they differ.
3. Split the card into individual factual claims: each summary sentence, each methods bullet, each stated limitation, each Key numbers row, each factual statement in Notes, and the frontmatter fields title, authors, year, journal, article, type, doi, license, data, crops, region, gist, not_established. Label each one Supported, Imprecise (right idea but wrong number, scope, emphasis or attribution), Not in source, or Contradicted, with page numbers.
4. Recompute every derived number (sums, percentages, conversions, rounding). Use Python if useful. Check that derived numbers are labelled as the card's own calculation.
5. Check attribution. A number the source cites from another paper must say so in the "Primary source" column. A number the source computes itself must not be credited to another paper.
6. Watch for these patterns, which the pilot found often:
   - wording more certain than the source ("shows" where the source says "may", "proposed" or "being tested")
   - outside knowledge written into the Summary as if the source said it (later papers, programme names, people, places). These belong in Notes, clearly labelled.
   - problems in the source itself (text versus table, caption or figure). Put these under "Source issues", not as card errors, and say whether the card flags them.
   - missing or weak not_established
   - a gist that lists topics instead of saying what the source shows
7. Completeness: list the source's aim, design, sample sizes, main results and effect sizes, the authors' own stated limitations and conclusions. Say whether each is in the card and how important it is. Focus on what a tricot user would ask.
8. Template compliance: summary word count (400 to 500), gist under 30 words, 8 to 12 keywords, 4 to 7 questions, tricot and maniva in lowercase. Short-format cards without the long-format sections are allowed, so only flag missing sections if the card is clearly meant to be long format.
9. For every fix, give exact replacement text, ready to paste, in the style of the card.
10. Values you read off a chart are approximate. Say so.

## Verdict

- Ready to curate: no Imprecise claims that change meaning, nothing Contradicted, no high-importance omissions.
- Minor fixes: a few small corrections or additions.
- Major fixes: a Contradicted claim on a main point, results missing, or the gist or summary misleading.

## Writing rules for the report

Plain English for readers whose first language may not be English. No em dashes. No semicolons in your prose (semicolons are allowed only inside suggested not_established text, where the template uses them as separators). Write tricot and maniva in lowercase, except when quoting a title or label exactly. Keep any quote from the source under 15 words and paraphrase otherwise.

Do not edit the card or anything in /home/claude/tricot-knowledge-base. Only write your report file to /home/claude/work/reviews/<card-id>.md. Do not use git.

## When done

Reply with three lines: the verdict; the counts (supported / imprecise / not in source / contradicted / source issues / omissions); and the single most important fix with its page number.

## Scratch files

Other reviewers run at the same time. Put any temporary files (page images, scripts) only in /tmp/rv-<card-id>/, never in a shared folder such as /tmp/rv.
