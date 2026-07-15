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

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `sprinkler_med` |
| `amt_mm` | Field named in the demo/source header; trace the reader for exact units and storage. | `25.00000` |
| `eff_frac` | Removal efficiency or effect fraction/percent used by a practice or treatment. | `0.85000` |
| `sumq_frac` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `dep_sub` | Depth, deposition, or dependency field; verify exact meaning in the reader. | `0.00000` |
| `salt_ppm` | Salt constituent value or parameter; verify units in the reader. | `100.00000` |
| `no3_ppm` | Nitrate-nitrogen concentration, mass, or parameter component; verify units in the reader. | `20.00000` |
| `po4_ppm` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `description` | Free-text description retained for reader/user context. | - |

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
