# Transportation-energy resilience review: supporting data

Supporting data for **Failure Propagation and Resilience Enhancement in Coupled Transportation-Energy Networks under Disruptions: A Topology-Conditioned Review**.

Data snapshot: **28 October 2026**. This repository contains publication-level evidence records, not publisher full texts or an independent pooled-effects dataset.

## Files

| File | Rows | Purpose |
|---|---:|---|
| `data/S2_publication_register.csv` | 189 | Unified cited-publication identities, full citations, DOI, publication type and overlapping evidence roles. |
| `data/S4_design_specific_appraisal_register.csv` | 189 | Design-specific appraisal records, instruments, source coverage, page locators and judgment rationales. |
| `data/S5_strategy_membership_and_annotations.csv` | 143 | Original strategy-contribution publications, phase annotations and cross-phase adjudication status. |
| `data/S11_indicator_decisions.csv` | 1701 | Nine indicator decisions for each cited publication, with coding rules and DOI/page locators. |
| `data/S11_indicator_counts.csv` | 9 | Deterministic summary derived from the indicator-decision table. |

`DATA_DICTIONARY.md` defines the fields and decision states. `scripts/validate_and_summarize.py` checks identity links and recomputes the indicator counts using Python's standard library. `checksums.sha256` identifies the deposited data bytes.

## Evidence scope and interpretation

- The reference inventory contains 189 DOI-distinct **publications**; publications are not necessarily independent underlying studies, datasets or intervention effects.
- A publication may contribute to coupling (C), disruption/failure propagation (P), resilience assessment/metrics (M), or enhancement strategies (S), separately or jointly. It need not satisfy all components simultaneously. Reporting-method sources retain their own role.
- The 189-source denominator applies to the defined indicator-documentation coverage measure. It is not a universal denominator for strategy effects, quality or event validation.
- The 143 strategy contributors include routine and transferable strategy contributions. Phase labels can overlap. There are 32 confirmed documented links, 41 records adjudicated without a cross-phase link, two without an established link, one with phase labels but no confirmed link, and 67 basic phase records without completed link adjudication. These are record statuses, not an exhaustive prevalence estimate.
- The indicator table preserves 192 uncertain publication-indicator decisions, not 192 publications. NOT_IDENTIFIED, UNCERTAIN and NOT_APPLICABLE are not evidence that a topic does not exist or that a study is poor quality.
- Priority/critical-load energy outcomes refer to M3. They do not automatically establish completed transport missions (M2) or societal outcomes (M5).
- Reviews and policy/conceptual sources may support synthesis but are not counted as additional realizations of primary effects they describe.

## Public-copy preparation

The four supplied data tables form the source snapshot. The public indicator table omits the `source_excerpt` column containing third-party publication text. DOI links, source-page locators, coding rules, decisions and all remaining values are preserved. The other three supplied tables are copied without changing their bytes. The nine-row counts table is derived, not a new evidence classification.

The local source snapshot remains unchanged. This repository does not contain reviewer correspondence, manuscript drafts, source PDFs, private local paths or historical search exports. These four tables do not independently reproduce every screening-stage count or every source-specific numerical comparison in the manuscript.

## Reproduction

From the repository root:

```bash
python scripts/validate_and_summarize.py
```

No third-party Python packages are required. CSV files use UTF-8 with BOM for spreadsheet compatibility; the script reads them with `utf-8-sig`. Empty cells indicate fields not populated or not relevant to that record; they are never numeric zeros.

## Citation and versioning

Cite the accompanying paper when using its framework or interpretations. Cite this dataset using the repository URL and the exact commit or release corresponding to the files used. A DOI has not yet been assigned. If a permanent archive is later created, add its actual version-specific DOI and creator metadata rather than inventing an identifier.

## Rights

No repository-wide reuse licence has been assigned at this stage. Public visibility should not be interpreted as a CC BY, CC0 or software licence. Third-party publications retain their respective rights; source material should be consulted through its DOI. A data licence and a separate code licence can be selected by the rights holders before a formal archival release.
