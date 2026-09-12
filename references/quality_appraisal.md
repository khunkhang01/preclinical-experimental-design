# Quality appraisal and confidence calibration

## Principle

Appraise how trustworthy and applicable a study is before using it to influence
a parameter. Separate study quality/risk of bias from directness, consistency,
and confidence. A statistically significant result is not automatically a
reproducible method.

## Select domains by study type

Use only relevant domains and explain omissions.

### In vitro and ex vivo

- biological material identity, passage/age/sex or donor information;
- assay validation, dynamic range, normalization, and detection limits;
- independent biological replicates versus technical repeats;
- randomization/order/plate-position effects and blinding of readout;
- exposure identity, purity, vehicle, preparation, stability, and contamination;
- controls, baseline, positive/negative controls, and prespecified endpoints;
- exclusions, missing data, outliers, and multiplicity handling; and
- model relevance and transferability to the stated question.

### In vivo

- model selection, inclusion/exclusion, allocation, randomization, and blinding;
- animal characteristics, housing, sex, age, strain, and acclimation;
- intervention preparation, route, dose, schedule, and exposure verification;
- sample-size rationale, biological unit, repeated measures, and attrition;
- humane endpoints, monitoring, adverse events, euthanasia, and 3Rs;
- outcome measurement validity and assessor blinding;
- deviations, exclusions, missing data, and analysis transparency; and
- reporting completeness and applicability to the planned population.

### PK/ADME and analytical work

- bioanalytical validation, matrix, calibration, LLOQ/ULOQ, recovery, stability;
- sampling schedule relative to absorption/distribution/elimination;
- dosing records and exposure confirmation;
- compartment/noncompartment model assumptions and parameter identifiability;
- handling of BLQ, missing samples, carryover, and assay failure; and
- independent subjects/samples versus replicate measurements.

### Toxicity/safety

- hazard identity, dose justification, route and duration;
- clinical observations, pathology/biomarkers, severity grading, and timing;
- control groups, historical controls, sentinel procedures where applicable;
- reversibility/recovery, humane endpoints, and stopping rules;
- exposure-response interpretation and confounding; and
- applicable guidance and institutional approvals.

### Herbal, natural products, formulation, and delivery

- identity/authentication, batch/lot, extraction or manufacturing process;
- chemical fingerprint/marker content, purity, contaminants, and stability;
- excipients, vehicle, particle size, release/encapsulation and storage;
- dose basis (raw material, marker, active equivalent, or formulation amount);
- comparability across batches and analytical method suitability; and
- route/device compatibility, sterility/endotoxin where relevant, and safety.

## Confidence method

For each parameter or decision, write a short calibration statement covering:

1. directness to the planned model and endpoint;
2. quality and key bias concerns;
3. consistency across studies;
4. biological or mechanistic plausibility;
5. full-text/supplement verification; and
6. applicability under the actual constraints.

Then assign `HIGH`, `MODERATE`, `LOW`, or `INSUFFICIENT` as defined in
`source_provenance.md`. Do not calculate a pseudo-precise score unless the user
requests a validated scoring method and the scoring rules are sourced.

## Output

The appraisal table should include `study_id`, `design_type`, `domain`,
`judgement`, `supporting_detail`, `impact_on_design`, `source_locator`,
`reviewer`, and `reviewed_at`. Retain disagreements or unresolved judgements;
do not hide them in an aggregate score.
