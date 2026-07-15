---
title: irr.ops input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `irr.ops`

## Purpose

Irrigation operation definitions.


## Official SWAT+ Reference

- Official page: [irr.ops](https://swatplus.gitbook.io/io-docs/introduction-1/management-practices/irr.ops).
- Official index note: This file contains pre-defined irrigation operations.
- Official field metadata available: 8 field row(s); matched to 1 of 9 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Operations.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_ops%irr_ops = "irr.ops"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/irr.ops`:

- Title/comment line: `irr.ops: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                    amt_mm      eff_frac     sumq_frac       dep_sub      salt_ppm       no3_ppm       po4_ppm  description`.
- Nonblank records after the header: 7.
- First demo data record: `sprinkler_med         25.00000       0.85000       0.00000       0.00000     100.00000      20.00000       1.00000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Irrigation operation name. | - | - | - | - | `sprinkler_med` | official GitBook |
| `amt_mm` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `25.00000` | demo/source inferred |
| `eff_frac` | Removal efficiency or effect fraction/percent. | - | - | - | - | `0.85000` | demo/source inferred |
| `sumq_frac` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.00000` | demo/source inferred |
| `dep_sub` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.00000` | demo/source inferred |
| `salt_ppm` | Salt constituent value or parameter. | - | - | - | - | `100.00000` | demo/source inferred |
| `no3_ppm` | Nitrate-nitrogen value; verify storage and units in the reader. | - | - | - | - | `20.00000` | demo/source inferred |
| `po4_ppm` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1.00000` | demo/source inferred |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | - | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `irr_eff` | Irrigation in-field efficiency. | - | - |
| `surq_rto` | Surface runoff ratio. | - | - |
| `irr_amt` | Irrigation application amount. | - | - |
| `irr_dep` | Depth of application for subsurface irrigation. | - | - |
| `irr_salt` | Concentration of total salt in irrigation water. | - | - |
| `irr_no3n` | Concentration of total nitrate in irrigation water. | - | - |
| `irr_po4` | Concentration of phosphate in irrigation water. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_ops%irr_ops` defaulting to `irr.ops`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/mgt_read_irrops.f90`.

## Downstream Consumers

Scheduled management-operation routines such as planting, harvest, grazing, irrigation, fire, and treatment.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/irr.ops`.

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
