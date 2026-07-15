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


## Official SWAT+ Reference

- Official page: [nutrients.sol](https://swatplus.gitbook.io/io-docs/introduction-1/soils/nutrients.sol).
- Official index note: This file specifies the initial soil nutrient contents.
- Official field metadata available: 7 field row(s); matched to 7 of 13 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

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

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the soil nutrient record. | - | - | - | - | `soilnut1` | official GitBook |
| `exp_co` | Depth coefficient to adjust nutrient concentrations for depth. | - | - | - | - | `0.00050` | official GitBook |
| `lab_p` | Labile P in soil surface. | - | - | - | - | `5.00000` | official GitBook |
| `nitrate` | Nitrate N in soil surface. | - | - | - | - | `7.00000` | official GitBook |
| `fr_hum_act` | Fraction of soil humus that is active. | - | - | - | - | `0.02000` | official GitBook |
| `hum_c_n` | Humus C:N ratio. | - | - | - | - | `10.00000` | official GitBook |
| `hum_c_p` | Humus C:N ratio. | - | - | - | - | `80.00000` | official GitBook |
| `inorgp` | Phosphorus-related parameter or state value. | - | - | - | - | `3.50000` | demo/source inferred |
| `watersol_p` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.15000` | demo/source inferred |
| `h3a_p` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.25000` | demo/source inferred |
| `mehlich_p` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1.20000` | demo/source inferred |
| `bray_strong_p` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.85000` | demo/source inferred |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | - | demo/source inferred |

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
