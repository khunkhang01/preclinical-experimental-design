# Workflow, gates, stopping rules, and audit trail

## State rules

Each state has an entry condition, an observable output, and a stopping rule.
Only move forward when the output is present or the state is explicitly marked
blocked.

| State | Entry | Output | Stop/block when |
|---|---|---|---|
| Intake | User request received | Scope, mode, inputs, constraints | Scope is materially ambiguous |
| Research-question Gate | Intake recorded | Precise question or labelled open decisions | Model/intervention/comparator/endpoint cannot be bounded |
| Comprehensive review | Question bounded | Search log, screened corpus, review | Retrieval or eligibility rules are not recorded |
| Saturation check | Review corpus assembled | Saturation rationale and gaps | Critical source spaces remain unsearched |
| Evidence Gate | Matrix and appraisal exist | Usable evidence map and parameter statuses | Critical claims lack allowed provenance |
| Roadmap | Evidence map complete | Stages, dependencies, decision criteria | Phase cannot be selected responsibly |
| Phase-selection Gate | Roadmap exists | User/PI-selected phase | No phase or authorization to proceed |
| Feasibility Gate | Phase selected | Resource/timing/risk check, ideal-feasible deltas | Critical input/resource/safety unresolved |
| Protocol | Feasible phase | Protocol artifacts and calculations | Required input or unit is missing |
| Quality & Ethics Gate | Protocol drafted | Review record and approval blockers | Safety/ethics/reporting issue unresolved |
| Citation Integrity Gate | Final values assembled | Parameter-to-source audit | Any critical unsupported parameter remains |
| Finalize | Gates recorded | Manifest, audit trail, final response | Do not claim release if any blocker remains |

## Gate status

Use `PASS`, `PASS-WITH-BLOCKERS`, or `BLOCKED`. A passing artifact or script
validation cannot override a scientific, safety, ethics, or evidence blocker.

## Roadmap phase selection

For each phase record objective, hypothesis/decision, inputs, outputs,
dependencies, minimum viable design, ideal design, feasible design, go/no-go
criteria, stop criteria, risks, and evidence gaps. If a phase depends on an
unvalidated assay, reagent, formulation, or exposure, place qualification/range
finding before confirmatory work.

## Protocol Audit procedure

1. Preserve the submitted protocol verbatim in a read-only or hashed source
   record when possible.
2. Parse every executable parameter into one audit row.
3. Link each row to the evidence matrix and full-text locator.
4. Check controls, unit of analysis, replicates, sample size, statistics,
   randomization/blinding, materials, preparation, feasibility, and ethics.
5. Assign exactly one of `KEEP`, `MODIFY`, `ADD`, `REMOVE`, `UNRESOLVED`.
6. Produce a change log and revised design only after the user/PI decision point;
   never make a silent edit.

## Audit-trail record

Minimum fields: `event_id`, `timestamp`, `state`, `decision_or_action`,
`input_artifact`, `evidence_ids`, `source_locators`, `calculation_ids`,
`assumptions`, `alternatives`, `actor_or_approval`, `status`, `confidence`,
`downstream_artifact`, and `unresolved_risk`.
