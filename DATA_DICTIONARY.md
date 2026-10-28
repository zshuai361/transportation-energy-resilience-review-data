# Data dictionary
## Units and identifiers

The unit is a publication or a publication-indicator judgment. Frequencies are counts, and coverage is a percentage of the stated inventory. This is not a table of comparable intervention-effect units. DOI joins identify publications, not independent underlying studies.
## Decision states

- CONFIRMED: a qualifying source contribution is documented.
- NOT_IDENTIFIED: a bounded check did not establish the qualifying contribution; not evidence of absence.
- UNCERTAIN: attribution, provenance or scope is unresolved.
- NOT_APPLICABLE: the criterion does not apply to the source/design.
- YES/PARTIAL in appraisal fields concern documented support for that domain, not an overall quality score. Other descriptive categories retain the meanings recorded in their rationales.
- NOT_CONFIRMED_AS_DISASTER_PHASE distinguishes routine strategy relevance from an established disaster phase.
- Cross-phase statuses must not collapse unadjudicated basic records into negative cases.

Empty cells are unpopulated or inapplicable as explained by the instrument/status; never convert them to numeric zero.

## S11_indicator_decisions.csv

| Field | Definition |
|---|---|
| `reference_id` | Stable PUB identifier shared by the tables; do not infer a reference number from it. |
| `doi` | Publication DOI; normalize case and remove DOI URL prefixes when comparing identities. |
| `indicator` | Machine-readable indicator key. |
| `indicator_label` | Human-readable indicator name. |
| `decision` | CONFIRMED, NOT_IDENTIFIED, UNCERTAIN or NOT_APPLICABLE. |
| `numerator_contribution` | Recorded 1/0 contribution to confirmed-documentation count; zero is not proof of topic absence. |
| `denominator_population` | 189 for the defined publication-inventory coverage measure. |
| `denominator_definition` | Definition of the eligible population for that measure. |
| `coding_rule` | Indicator-specific positive decision rule. |
| `source_pages` | Page locators in the examined source; may be empty for basic/unadjudicated or non-page material. |
| `source_locator` | Public DOI/source URL; not a local file-system path. |
| `interpretation` | Required interpretive limitation. |

## S2_publication_register.csv

| Field | Definition |
|---|---|
| `reference_id` | Stable PUB identifier shared by the tables; do not infer a reference number from it. |
| `main_reference_number` | Reference-list number in the associated manuscript snapshot; order can change in later versions. |
| `citation_key` | Manuscript citation key, not a study-independence identifier. |
| `full_citation` | Bibliographic citation in the supplied snapshot. |
| `doi` | Publication DOI; normalize case and remove DOI URL prefixes when comparing identities. |
| `publication_type` | Publication design/type as recorded; determines the appropriate interpretation/appraisal. |
| `evidence_roles` | Semicolon-separated, potentially overlapping C/P/M/S contribution roles, or reporting-method use. |
| `role_scope` | Boundary of the source contribution. |
| `source_coverage` | Material available for the source check; full text and publisher/author records are distinct. |

## S4_design_specific_appraisal_register.csv

| Field | Definition |
|---|---|
| `reference_id` | Stable PUB identifier shared by the tables; do not infer a reference number from it. |
| `main_reference_number` | Reference-list number in the associated manuscript snapshot; order can change in later versions. |
| `doi` | Publication DOI; normalize case and remove DOI URL prefixes when comparing identities. |
| `publication_type` | Publication design/type as recorded; determines the appropriate interpretation/appraisal. |
| `appraisal_status` | Availability/type of the design-specific judgment record; see the source-specific instrument and evidence. |
| `boundary` | Judgment about documented system/outcome boundaries, not an overall study-quality score. |
| `parameter_provenance` | Judgment about documented origins of model parameters or data. |
| `event_comparator` | Judgment about a defined event/operational comparator; routine comparisons do not establish disaster effects. |
| `uncertainty` | Appraisal judgment about uncertainty/sensitivity reporting. |
| `validation_basis` | Descriptive basis of validation or case demonstration; input data do not equal independent event validation. |
| `reproducibility` | Reported detail/access category; an availability statement is not an independently executed replication. |
| `source_pages` | Page locators in the examined source; may be empty for basic/unadjudicated or non-page material. |
| `appraisal_rationale` | Review authors' rationale for design-domain judgments and boundaries. |
| `search_selection` | Review-specific assessment of search/selection reporting. |
| `quality_overlap` | Review-specific assessment concerning evidence appraisal or overlap handling. |
| `use_constraint` | Permitted synthesis use and limitation. |
| `basis` | Recorded basis of the judgment. |
| `inference_boundary` | Limit on what the evidence/record supports. |
| `appraisal_instrument` | Design-specific checklist/instrument used for this record. |
| `source_evidence` | Available source-material category, not a verbatim full-text release. |
| `sampling_frame` | Survey-specific assessment of sampling/population coverage. |
| `response_measurement` | Survey-specific assessment of response/measurement. |
| `model_specification` | Applicable empirical/survey model-specification assessment. |
| `coverage` | Design-specific coverage judgment. |
| `case_selection` | Qualitative-study case-selection assessment. |
| `data_provenance` | Qualitative/empirical data-origin assessment. |
| `analysis_transparency` | Qualitative/empirical analytical transparency assessment. |
| `triangulation` | Qualitative-study corroboration/triangulation assessment. |
| `transferability` | Contextual transfer/generalization boundary. |

## S5_strategy_membership_and_annotations.csv

| Field | Definition |
|---|---|
| `reference_id` | Stable PUB identifier shared by the tables; do not infer a reference number from it. |
| `main_reference_number` | Reference-list number in the associated manuscript snapshot; order can change in later versions. |
| `doi` | Publication DOI; normalize case and remove DOI URL prefixes when comparing identities. |
| `publication_type` | Publication design/type as recorded; determines the appropriate interpretation/appraisal. |
| `evidence_roles` | Semicolon-separated, potentially overlapping C/P/M/S contribution roles, or reporting-method use. |
| `S1` | Preparedness/planning-phase annotation directed at service continuity. |
| `S2` | Adaptation/response during active disruption. |
| `S3` | Restoration-phase annotation. |
| `operational_strategy` | Routine operational strategy contribution; does not automatically establish a disaster phase. |
| `cross_phase_link` | Recorded link-adjudication status; distinguish confirmed, absent, unestablished and basic-only records. |
| `source_pages` | Page locators in the examined source; may be empty for basic/unadjudicated or non-page material. |
| `adjudication_scope` | Boundary of the phase/link check. |

## Derived counts

`S11_indicator_counts.csv` groups the decision table by indicator. CONFIRMED, NOT_IDENTIFIED, UNCERTAIN and NOT_APPLICABLE counts sum to 189 in each row. `confirmed_coverage_percent` equals 100 × confirmed / denominator, rounded to one decimal place. Overlapping indicators do not form an exclusive partition. The `source_excerpt` field is intentionally absent from the public copy.
