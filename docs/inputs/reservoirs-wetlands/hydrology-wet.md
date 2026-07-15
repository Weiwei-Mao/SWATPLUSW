---
title: hydrology.wet input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `hydrology.wet`

## Purpose

Wetland hydrology parameter database.

## Role In SWAT+

- Category: Reservoirs Wetlands.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_res%hyd_wet = "hydrology.wet"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/hydrology.wet`:

- Title/comment line: `hydrology.wet: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                    hru_ps         dp_ps        hru_es         dp_es             k          evap   vol_area_co      vol_dp_a      vol_dp_b      hru_frac`.
- Nonblank records after the header: 1.
- First demo data record: `paddy			          1.00        150.00         1.00        150.00           0.5           0.75          1.00         1.00         1.00          1.0`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `paddy` |
| `hru_ps` | HRU-related parameter or object reference. | `1.00` |
| `dp_ps` | Field named in the demo/source header; trace the reader for exact units and storage. | `150.00` |
| `hru_es` | HRU-related parameter or object reference. | `1.00` |
| `dp_es` | Field named in the demo/source header; trace the reader for exact units and storage. | `150.00` |
| `k` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.5` |
| `evap` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.75` |
| `vol_area_co` | Volume-related value or parameter. | `1.00` |
| `vol_dp_a` | Volume-related value or parameter. | `1.00` |
| `vol_dp_b` | Volume-related value or parameter. | `1.00` |
| `hru_frac` | HRU-related parameter or object reference. | `1.0` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_res%hyd_wet` defaulting to `hydrology.wet`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/wet_read_hyd.f90`.

## Downstream Consumers

Reservoir, pond, and wetland hydrology, release, sediment, and nutrient routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/hydrology.wet`.

## Open Questions

- Which exact reader routine stores each field, and in which derived type or module variable?
- Which units, valid ranges, and default substitutions are enforced in that reader?
- Which routines consume each parsed value after initialization?

## External References

- [SWAT+ Input File Format](https://swatplus.gitbook.io/io-docs/introduction-1/input-file-format)
- [SWAT+ master file `file.cio`](https://swatplus.gitbook.io/io-docs/introduction-1/master-file-file.cio)
- [SWAT+ simulation settings](https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings)

## Related Files

- [SWAT+ input files map](../../input-files.md)
- [SWAT+ tracing guide](../../tracing-guide.md)
- [Master input manifest](../simulation/file-cio.md)
