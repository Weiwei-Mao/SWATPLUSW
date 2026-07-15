---
title: nutrients.sol input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `nutrients.sol`

## Purpose

Soil nutrient/soil-test initialization database.

## Role In SWAT+

- Category: Soils.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_sol%nut_sol = "nutrients.sol"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/nutrients.sol`:

- Title/comment line: `nutrients.sol: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                    exp_co         lab_p       nitrate    fr_hum_act       hum_c_n       hum_c_p        inorgp    watersol_p         h3a_p     mehlich_p  bray_strong_p  description`.
- Nonblank records after the header: 1.
- First demo data record: `soilnut1               0.00050       5.00000       7.00000       0.02000      10.00000      80.00000       3.50000       0.15000       0.25000       1.20000       0.85000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `soilnut1` |
| `exp_co` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00050` |
| `lab_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `5.00000` |
| `nitrate` | Field named in the demo/source header; trace the reader for exact units and storage. | `7.00000` |
| `fr_hum_act` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.02000` |
| `hum_c_n` | Field named in the demo/source header; trace the reader for exact units and storage. | `10.00000` |
| `hum_c_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `80.00000` |
| `inorgp` | Phosphorus-related component; verify units in the reader. | `3.50000` |
| `watersol_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.15000` |
| `h3a_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.25000` |
| `mehlich_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.20000` |
| `bray_strong_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.85000` |
| `description` | Free-text description retained for reader/user context. | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_sol%nut_sol` defaulting to `nutrients.sol`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/solt_db_read.f90`.

## Downstream Consumers

Soil profile, soil nutrient pools, and soil-layer calculations.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/nutrients.sol`.

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
