---
title: soils.sol input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `soils.sol`

## Purpose

Soil profile database for full HRUs.

## Role In SWAT+

- Category: Soils.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_sol%soils_sol = "soils.sol"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/soils.sol`:

- Title/comment line: `soils.sol: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                            nly           hyd_grp        dp_tot    anion_excl      perc_crk  texture                              dp            bd           awc        soil_k        carbon          clay          silt          sand          rock           alb        usle_k            ec         caco3            ph`.
- Nonblank records after the header: 501.
- First demo data record: `SONGSAN                           5                 A    1200.00000       0.50000       0.50000  LS`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `SONGSAN` |
| `nly` | Field named in the demo/source header; trace the reader for exact units and storage. | `5` |
| `hyd_grp` | Hydrology-related parameter or reference. | `A` |
| `dp_tot` | Count of following records or related objects. | `1200.00000` |
| `anion_excl` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `perc_crk` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `texture` | Field named in the demo/source header; trace the reader for exact units and storage. | `LS` |
| `dp` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `bd` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `awc` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `soil_k` | Soil-related parameter or record reference. | - |
| `carbon` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `clay` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `silt` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `sand` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `rock` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `alb` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `usle_k` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `ec` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `caco3` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `ph` | Field named in the demo/source header; trace the reader for exact units and storage. | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_sol%soils_sol` defaulting to `soils.sol`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/soil_db_read.f90`.

## Downstream Consumers

Soil profile, soil nutrient pools, and soil-layer calculations.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/soils.sol`.

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
