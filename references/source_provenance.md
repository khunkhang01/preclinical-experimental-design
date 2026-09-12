# Provenance, parameter status, and confidence taxonomy

Use these controlled values exactly in machine-readable artifacts. Additional
project-specific values may be added only with a definition and version note.

## Source provenance

| Value | Meaning | Allowed use |
|---|---|---|
| `FULL-TEXT VERIFIED` | Original full text and relevant Methods/context checked | Parameter evidence and synthesis |
| `SUPPLEMENT VERIFIED` | Parameter checked in supplementary methods/data | Parameter evidence when locator is recorded |
| `ABSTRACT ONLY` | Only abstract was available | Discovery/context only; never parameter evidence |
| `SECONDARY CITATION` | Found through a review or another source, primary not checked | Discovery/context only |
| `DATABASE VERIFIED` | Checked against a validated curated database | Database-appropriate facts only |
| `GUIDELINE VERIFIED` | Checked against an official guideline/standard | Guidance/reporting/safety claims in scope |
| `UNVERIFIED` | Could not verify source or claim | Cannot support design |

Source provenance is not a quality grade. A full-text study can still have high
risk of bias; record both.

## Parameter status

| Value | Meaning | Required next action |
|---|---|---|
| `EVIDENCE-SUPPORTED` | Directly supported in a sufficiently applicable verified source | Retain with locator and confidence |
| `INDIRECT-EVIDENCE` | Extrapolated across model, formulation, endpoint, or context | State extrapolation; lower confidence; assess pilot |
| `PILOT-REQUIRED` | Range, feasibility, stability, or measurement needs a pilot | Do not treat as confirmatory parameter |
| `ASSUMPTION` | Explicit working assumption not established by evidence | Seek decision/verification before execution |
| `USER-DECISION` | Chosen by PI/instructor/user within the stated scope | Record actor, rationale, and approval need |
| `UNRESOLVED` | Evidence or input is insufficient/conflicting | Block affected executable work |
| `NOT-APPLICABLE` | Parameter does not apply to this design | Explain why |

## Confidence

| Grade | Interpretation |
|---|---|
| `HIGH` | Direct, methodologically sound, consistent, full-text verified evidence applicable to the context |
| `MODERATE` | Relevant evidence with some heterogeneity, minor extrapolation, or quality limitation |
| `LOW` | Sparse, indirect, inconsistent, or materially limited evidence |
| `INSUFFICIENT` | Evidence cannot justify a parameter or decision; pilot or resolution is required |

Confidence must consider directness, methodological quality, consistency,
biological plausibility, full-text verification, and applicability. Record a
short reason rather than emitting a bare grade.

## Audit decisions

Protocol Audit uses:

- `KEEP`: retain existing item; evidence and feasibility are adequate;
- `MODIFY`: change a value, wording, sequence, control, or analysis with reason;
- `ADD`: add a missing control, parameter, record, or gate;
- `REMOVE`: remove an unsupported, unsafe, redundant, or out-of-scope item;
- `UNRESOLVED`: do not change silently; missing evidence or decision blocks it.

Every audit row must include the original text/value, audit decision, evidence
IDs/locators, recommendation, rationale, confidence, and approval needed.
