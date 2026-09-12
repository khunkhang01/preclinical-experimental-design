# Statistical design and sample-size requirements

## Design before calculation

State the estimand or primary comparison before choosing a test. Identify the
experimental unit, observational unit, biological replicate, technical repeat,
cluster, repeated-measures structure, primary endpoint, effect size, variance
source, alpha, target power, attrition, and multiplicity plan.

Do not treat technical repeats as independent biological replicates. Do not
invent an effect size, standard deviation, event rate, correlation, or attrition
rate. If an input is unknown, use a sourced estimate, pilot, sensitivity range,
or mark `PILOT-REQUIRED`.

## Sample-size record

Include:

- primary endpoint and planned contrast;
- formula or software/method and version;
- effect size and its source/assumption;
- variance/event-rate and its source/assumption;
- alpha, sidedness, target power, multiplicity adjustment;
- attrition/invalid-assay allowance and justification;
- final analyzable n and planned enrollment n;
- biological versus technical replicate definition;
- clustering/repeated-measures assumptions; and
- sensitivity analysis over plausible inputs.

The bundled `scripts/sample_size.py` provides transparent approximations for
common two-group cases. It is not a universal power engine and does not replace
domain-specific design or statistical review.

## Analysis plan

Pre-specify the primary analysis, covariate adjustment, normalization, baseline
handling, repeated measures, multiplicity, missing-data rules, outlier policy,
assumption checks, effect estimates with uncertainty, and data-exclusion
criteria. Distinguish exploratory endpoints from confirmatory endpoints.

For PK/ADME, record sampling design, BLQ handling, exposure metric, model
assumptions, and whether inference is subject-level or sample-level. For plate
assays, account for plate/batch effects and avoid pseudoreplication.

## Randomization and blinding

Describe sequence generation, allocation concealment, stratification/blocking,
blinding of operators/assessors/analysts, code breaking, and deviations. The
bundled randomization utility only generates an auditable allocation from user
inputs; it does not establish an approved allocation plan.
