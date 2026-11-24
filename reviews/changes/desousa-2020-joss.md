# Change log: desousa-2020-joss

Removed tricot and Plackett-Luce claims the 2020 paper does not make (moved one to Notes as outside information), replaced the Summary with source-based text, and corrected the gist, Methods, limitations, data and region fields. Also added not_established, Key numbers and source-issue Notes.

## Applied

1. Fix 1: new gist with no tricot claim. The paper never mentions tricot (pp. 1 to 5).
2. Fix 2: Summary replaced with the review's 470-word text, with one small wording change ("The trends are shown as loess curves on a plot, with no statistical test"). Checked each statement: data descriptions and citation guidance on p. 1, functions, buffering and output classes on pp. 1 to 2, worked example and results on p. 2, loess and four indices in the Figure 1 caption on p. 3, Kehel 2016, van Etten 2019, de Sousa 2018, Aguilar 2005, over 800 citations, disease control and the reproducible-workflow aim on pp. 3 to 4, Kehel reference title (CIMMYT yield trials) on p. 4. Added the tricot note to Notes, labelled as outside this paper.
3. Fix 3: "ten years" changed to "about a decade". Text, code and caption periods differ (pp. 2 to 3). Plot axis checked on p. 3: 2008 to about early 2018.
4. Fix 4: "rainy days" and "whole period" removed. Methods Indices bullet replaced. Only MLDS, MLWS, Rtotal and Rx5day are named (pp. 2 to 3).
5. Fix 5: Stated limitations rewritten to say the paper states no limitations, with data descriptions (p. 1) and the card's own points labelled.
6. Fix 6: Data access bullet replaced, stray space before the comma removed. Point inputs buffered into one polygon per request (pp. 1 to 2).
7. Fix 7: Integration bullet replaced. sf, crul and jsonlite (p. 1), as.sf and as.geojson (p. 2). tidyverse only draws the figure (p. 2).
8. Fix 8: "proxy for agricultural drought" removed. ESI now described as global, from 2001, based on land surface temperature (p. 1).
9. Fix 9: not_established added as proposed.
10. Fix 10: data field now gives the repository and Zenodo archive. Confirmed from the link annotations in the page 1 margin.
11. Fix 11: region field replaced (pp. 1 to 2).
12. Fix 12: five Key numbers rows added (ESI 2001 on p. 1, 20 points, 527,400 ha and 30 days on p. 2, over 800 citations on p. 3).
13. Claims 16 to 18, 23, 24, 26 to 31, 34 (Imprecise or Not in source): all handled through fixes 2 and 4 to 8.
14. Source issue 1 (study period): Note added, labelled as a problem in the source (pp. 2 to 3).
15. Source issue 2 (coordinate signs): Note added, labelled as a problem in the source (p. 2).
16. Source issue 4 (IMERG resolution): Note added, labelled as outside information, not from this paper.
17. Template compliance: question 4 replaced with "Which R objects can I give chirps as input, and what does it return?" (answered on pp. 1 to 2).

## Skipped

- Source issue 3 (buffer unit "0.0001 arc-sec", p. 1): the review says no note is needed, and the card does not cite the buffer size.
- Funding and NHH course origin (low-importance omission, p. 4): optional, and not something a tricot user is likely to ask about.
- Title sentence case: the review marks it Supported and does not ask for a change.
- Relations: the review proposes none. Not added.

## Final counts

- Summary words: 472
- Gist words: 28
- Keywords: 10
- Questions: 4
