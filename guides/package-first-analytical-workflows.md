# Package-first analytical guidance

Status: proposed. Applies to scientific code generation, not to claims that software has been validated.

## Mandatory discovery before writing code

1. Define the scientific question, experimental design, input data structure, estimand and decision context.
2. Search CRAN documentation and maintained GitHub source for existing implementations, beginning with relevant ClimMob-suite packages (`gosset`, `ClimMobTools`, `climatrends`) and `PlackettLuce`. Also consider other domain-appropriate packages. Do not assume these packages solve every task.
3. Inspect the **actual function source, manual, examples and tests**. Record package version or Git commit, function signature, required data schema, output class, missing-value handling, assumptions, warnings and citation.
4. Prefer established functions over handwritten reimplementations. Adapt data to a documented interface; never invent a package input schema.
5. Only write custom methods when existing tools are unsuitable, and explain why. Validate custom methods against independent known examples.
6. Pin released versions or explicit Git commits for reproducibility; do not source mutable remote scripts during an analysis.
7. Run automated tests and inspect numerical results before declaring a workflow validated. Successful execution alone does not establish scientific validity.
8. Preserve historical scripts as provenance, not as authoritative code. Never expose participant-level personal information in examples.
9. Use `=` for assignment, per project convention. Distinguish `=` from `==` and formula syntax.

## Verified source observation (2026-10-31)

The source of `AgrDataSci/gosset` at `R/rank_tricot2.R` documents the call `rank_tricot2(data, id, items, input, ...)` and the `nicabean$trial` example. Its implementation builds an item-by-participant matrix, warns about missing id/item/value rows, warns that duplicate (id, item) records are overwritten by the last value, and converts with `PlackettLuce::as.rankings()`.

**Do not describe `rank_tricot2()` as a comprehensive validator.** The source does not establish checks for valid three-item assignments, consistent best/worst answers, correct rank ranges, or whether duplicate observations should be resolved rather than overwritten. Validate the scientific data-generating process separately.

The earlier handwritten ranking example failed an `identical()` assertion that could reflect integer/double type differences. That failure does not prove incorrect ranking values, but the example was released without R execution and is superseded.

## Evidence boundaries

- A parsed rankings object is not proof of a connected comparison graph or estimable worth parameters.
- Pseudo-rankings are modelling assumptions; examine sensitivity and identifiability.
- Preference worth is not directly yield, adoption, heritability, causal effect or recommendation suitability.
- Environmental extrapolation requires target-population-of-environments reasoning, support/analogue checks, uncertainty and independent validation.
- Socioeconomic clusters describe covariate structure; preference differences require separate inferential analysis. Consider operational 2–5 clusters without forcing a statistically indefensible solution.

## Required metadata for each generalized workflow

Scientific question; source scripts and locations; package/function/version; input and output schemas; design assumptions; transformations; diagnostics; uncertainty; alternatives; known limitations; tested environment; tests and results; intended decisions; supporting references; validation status.
