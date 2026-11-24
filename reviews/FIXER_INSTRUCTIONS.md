# Instructions for applying a review to a card

You correct one summary card in the tricot knowledge base using an independent review of that card. A person will read your changes as a diff in a pull request, so make every change deliberate and traceable.

## Files

- Card to edit: /home/claude/kb-fixes/papers/<card-id>.md (edit this file in place, nothing else)
- Review of the card: /home/claude/work/reviews/<card-id>.md
- Source PDF: /home/claude/kb-fixes/papers-pdf/<pdf-file>
- Text extraction of the PDF: /home/claude/work/txt/<pdf-name>.txt
- Card template: /home/claude/kb-fixes/TEMPLATE.md
- Write your change log to: /home/claude/work/fixes/<card-id>.md

## What to apply

1. Every item under "Fixes needed" in the review.
2. Every claim the review marks Imprecise, Not in source or Contradicted, using the review's replacement text.
3. High-importance omissions. Medium-importance omissions too, as long as the Summary stays within 400 to 500 words. If space runs out, prefer the omissions a tricot user would most likely ask about.
4. Source issues: add each one the card does not already flag to Notes, as a short line that says it is a problem in the source.
5. Metadata fixes: authors, article, license, data, crops, region, gist, keywords, not_established, relations. Add a relation only if its target card exists in /home/claude/kb-fixes/papers/.
6. Outside knowledge that the review says is written into the Summary as if the source said it: move it to Notes and label it, or remove it if it adds nothing.

## Check before you apply

The reviewer can be wrong. Before you apply each change, confirm it in the source text or on the PDF page (use the Read tool with the pages parameter for tables and figures). If a suggested change is not supported by the source, do not apply it, and record it as skipped with the reason. If the review's replacement text is right in substance but badly worded, you may improve the wording.

## Keep

- The card's structure, section order, frontmatter field order and the id.
- `curated_card: no`. Never change it. The person sets it after reading the pull request.
- Correct text that the review does not question. Do not rewrite for style alone.

## Style

Follow TEMPLATE.md. Summary 400 to 500 words, in your own words. Gist under 30 words and saying what the source shows. 8 to 12 keywords. 4 to 7 questions. Plain English for readers whose first language may not be English. No em dashes. No semicolons except as separators inside not_established and in relation comments, where the template uses them. Write tricot and maniva in lowercase, except in titles quoted exactly. Keep quotes from the source under 15 words.

Count Summary words with a script before you finish, and check the frontmatter still parses as YAML (python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]).read().split('---')[1])" <card-path>).

## Change log

Write /home/claude/work/fixes/<card-id>.md with:

- A one-line summary of what changed.
- Applied: a numbered list, each item pointing to the review's fix or claim number, with the page that confirms it.
- Skipped: each review suggestion you did not apply, with the reason.
- Final counts: Summary words, gist words, keywords, questions.

## Do not

Do not edit any other file. Do not use git. Put temporary files only in /tmp/fx-<card-id>/.

## When done

Reply with three lines: how many changes were applied, how many were skipped and why in a few words, and the final Summary word count.
