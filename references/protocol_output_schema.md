# Preferred artifact structure and schemas

## Preferred project layout

Use this layout when the environment can create files. Add only artifacts that
apply to the active mode.

```text
01_research_question.md
02_literature_review.md
03_search_saturation_log.md
04_evidence_matrix.csv
04_evidence_matrix.xlsx
05_quality_appraisal.csv
05_quality_appraisal.xlsx
06_source_manifest.csv
07_experimental_roadmap.md
08_phase_<name>_protocol.md
09_reagent_preparation.md
10_materials_equipment.csv
10_materials_equipment.xlsx
11_statistical_plan.md
12_protocol_flowchart.mmd
12_protocol_flowchart.svg       # optional rendered form
13_calculations.py              # optional; include when used
14_visualizations/              # optional
15_protocol_audit.md             # audit mode
16_audit_trail.md
17_gate_status.md
```

CSV is the inspection/interchange form. XLSX is a convenience form with the
same column schema. Never let a spreadsheet contain values that are absent from
the canonical CSV or Markdown record.

## Mandatory record sections

### Research question

Scope, mode, model/system, intervention/exposure, comparator, endpoint,
timepoint, hypothesis/decision, unit of experimentation, unit of analysis,
constraints, assumptions, and open questions.

### Protocol

Objective; design summary; groups and controls; inclusion/exclusion; materials;
reagent preparation; equipment and calibration; stepwise sequence and timing;
randomization/blinding; measurements; endpoints and acceptance rules;
replicates; sample size; statistics; deviations; stopping/humane endpoints;
data-recording fields; waste/safety; evidence links; and gate status.

### Flowchart

Show intake/material checks, preparation, allocation, exposure, sampling,
measurement, QC, failure handling, analysis, and decision gates. Each branch
must have an observable condition and an owner/decision record. Use Mermaid
source as the portable canonical form; render SVG/PNG only when available.

## Table schemas

### Quality appraisal

`study_id, design_type, domain, judgement, supporting_detail, impact_on_design,
source_locator, reviewer, reviewed_at`

### Source manifest

`source_id, citation_key, title, authors_or_issuer, year, doi_or_identifier,
url_or_location, source_type, provenance_status, full_text_checked,
retrieval_date, checksum_or_version, notes`

### Materials/equipment/consumables

`item_id, category, item_name, specification_or_grade, role, quantity,
unit, supplier_or_source, lot_or_serial, alternative, criticality,
calibration_or_expiry, storage, safety_or_disposal, evidence_id, status,
notes`

### Parameter-level design table

`parameter_id, phase, group_or_step, parameter_name, planned_value, unit,
allowed_range, source_or_calculation, locator_or_formula, provenance_status,
parameter_status, confidence, rationale, feasibility_delta, approval_needed,
audit_decision, unresolved_risk`

## File and provenance rules

Use stable, ASCII-safe filenames with numeric prefixes. Keep source files
immutable when possible. Record generated-file time, script version, input
hashes/checksums where available, and output schema version in the audit trail.
