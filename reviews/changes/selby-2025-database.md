# Change log: selby-2025-database

Applied all 14 review fixes and one medium omission (community libraries and QBMS) after checking each against the source. The Summary no longer calls the paper the tricot reference, hedges are restored, the tool grouping now follows the paper, and not_established is added.

## Applied

1. Fix 1, Notes on Alliance co-authors. Replaced with the review text. Confirmed on pp. 1 to 2: de Sousa, Guignon, Laporte and Rouard have affiliation 19 (Bioversity International), Aparicio has affiliation 7 (CIAT).
2. Fix 2, Summary last sentence. Replaced the "reference for tricot" claim with the review text. Confirmed that "tricot" does not appear in the paper (also confirmed by hand by the user). The ClimMob section is on pp. 5 to 6, with one mention under Breedbase on p. 10.
3. Fix 3, Summary sentence on ClimMob data detail. Restored "may lack" and "can give" (p. 5).
4. Fix 3, third Stated limitation. Replaced with the review text, which removes "tricot" and restores the hedge (p. 5).
5. Fix 4, gist. Replaced with the review's 29-word gist. 201 endpoints confirmed on p. 3, ClimMob data exchange on p. 6.
6. Fix 5, not_established added after gist (template field order). Each item checked: no ClimMob use examples (pp. 5 to 6), no evaluation of genetic gain (whole paper), GLIS v1.3 (p. 9), PIPPA v1.3 (p. 6), FAIDARE indexing of v1.3 and v1.2 (p. 10), BrAPI2ISA/MIRA v1.3 (p. 12), list not exhaustive (p. 4).
7. Fix 6, showcase sentence. Replaced with the review text. Section headings confirmed: ClimMob under Phenotyping (p. 5), Flapjack under Genotyping (p. 7), Florilège and Helium under Germplasm management (pp. 8 to 9), BMS, Germinate and FAIDARE under Breeding and genetics data management (pp. 9 to 10), BrAPIMapper, MIRA and GraphQL warehouse under General infrastructure (p. 12).
8. Fix 7, looking ahead. Replaced "plans to extend the standard to ... such as" with "intends to build standards ... possibly including" (p. 13, "potentially including").
9. Fix 8, Key numbers GLIS row. Primary source changed to "GLIS website (ref. 27), cited in this paper" (p. 8).
10. Fix 9, v2.0 changes added to Summary. Confirmed on p. 4: v1.X focused on read-only phenotype data, v2.0 allows read, write and update and aligns with GA4GH Variants Schema and MIAPPE.
11. Fix 10, hackathons. "a major staple" and twice a year confirmed on p. 4.
12. Fix 11, under-resourced programmes sentence. Confirmed on p. 2.
13. Fix 12, Methods content bullet. "short success stories", "vast majority ... independent of the BrAPI project" confirmed on p. 4.
14. Fix 13, license changed to CC BY 4.0 (p. 1, CC BY 4.0 link).
15. Fix 14, author count changed to 76 named authors plus the BrAPI Consortium. Counted from the author list on p. 1.
16. Medium omission, community libraries and QBMS. Added to Notes. Libraries for Java, JavaScript, Python, R and Drupal confirmed on p. 4. QBMS extracting data into an R data frame confirmed on p. 11. The review's wording "from any BrAPI server" was softened to "from BrAPI-compatible databases", since the source does not say "any". The line about tricot analysts is labelled as a curator's note, since the paper does not say it.

## Skipped

- Medium omission on tools still using v1.3 or v1.2: not added separately, because it is covered in not_established (as the review itself suggests).
- Low omissions (Figure 2 classification of ClimMob, digital data ecosystem conclusion, FAO 5.8 million accessions, funding): skipped as low importance. The review marks them optional.
- Source issues: the review found none, and none were found while checking.

## Final counts

- Summary words: 494
- Gist words: 29
- Keywords: 10
- Questions: 5
