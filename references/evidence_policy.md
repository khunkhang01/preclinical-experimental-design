# Evidence policy

## Purpose

This reference governs literature discovery, inclusion, full-text verification,
evidence-matrix construction, and search saturation. It is shared by all four
modes.

## Source hierarchy

Use the strongest source that directly answers the parameter question:

1. **Primary full-text study**: original Methods, supplementary methods, tables,
   figures, protocol, correction, or raw-data documentation. Preferred for
   experimental parameters and observed results.
2. **Official guideline, standard, or validated database**: appropriate for
   reporting, safety, nomenclature, assay definitions, or curated reference
   facts. Record issuing body, version/date, and scope.
3. **Systematic review or meta-analysis**: useful for landscape, consistency,
   and locating primary studies; follow critical methods back to primary text.
4. **Narrative review, thesis, protocol repository, or methods overview**:
   useful for discovery and context; not sufficient alone for a critical
   executable parameter when primary text can be obtained.
5. **Abstract, snippet, search result, press release, or secondary citation**:
   discovery only. Never use as verified parameter evidence.

If sources conflict, preserve the conflict in the matrix, assess directness and
quality, and explain the decision. Do not average incompatible methods by
intuition.

## Structured review record

Record:

- research question and eligibility scope;
- databases/repositories/search engines or local collections searched;
- exact query strings, controlled vocabulary, synonyms, and date searched;
- filters, language limits, date limits, and their rationale;
- inclusion/exclusion criteria and screening decisions;
- duplicate handling and citation-chasing (backward and forward);
- full-text retrieval status and reasons for unavailable text;
- study/model/parameter coverage map;
- search iterations and new decision-changing evidence per iteration; and
- saturation decision, reviewer/agent, date, and unresolved gaps.

Do not describe a review as "comprehensive" without this record.

## Full-text verification rule

For every parameter used in a protocol, open the source and verify the exact
value, unit, model, exposure, comparator, timing, and context in Methods,
supplementary methods, a table/figure, or an official technical document. Store
a locator such as page, section, table, figure, paragraph, DOI plus stable URL,
or repository record. If the parameter is derived, store the source inputs and
formula separately.

Abstract-only and secondary sources may remain in the evidence landscape, but
their provenance must remain `ABSTRACT ONLY` or `SECONDARY CITATION` and their
parameter evidence must be excluded from final executable recommendations.

## Search saturation

Saturation is a documented decision, not a fixed paper count. Continue until
the relevant source spaces and citation paths are covered and at least two
consecutive, meaningfully different search iterations yield no new
decision-changing study, parameter, safety issue, or contradiction. Re-open the
search when the model, intervention, endpoint, or phase changes. If the corpus
is sparse or retrieval is incomplete, report `NOT-SATURATED` and do not make
high-confidence parameter claims.

## Evidence matrix minimum columns

Use these names in CSV/XLSX outputs unless a project schema explicitly extends
them:

`evidence_id, citation_key, source_title, source_type, provenance_status,
full_text_checked, locator, study_design, model_system, intervention,
intervention_formulation, comparator, endpoint, timepoint, parameter_name,
parameter_value, unit, replicate_definition, statistical_method,
quality_domains, directness, consistency, applicability, confidence,
design_implication, limitations, review_decision, reviewer, reviewed_at`

One row is one study-parameter observation, not one paper summary. Keep empty
values empty and put the reason in `limitations` or `parameter_status`; never
insert `N/A` in a way that hides missing evidence.

## Review decisions

For included evidence use controlled values such as `INCLUDE`, `CONTEXT-ONLY`,
`PILOT-ONLY`, `EXCLUDE`, or `UNRESOLVED`, with a reason. A source can be useful
for context while still being ineligible for parameter-level support.
