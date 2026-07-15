---
title: nutrients.cha input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `nutrients.cha`

## Purpose

Channel nutrient and water-quality parameter database.

## Role In SWAT+

- Category: Channels.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cha%nut = "nutrients.cha"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/nutrients.cha`:

- Title/comment line: `nutrients.cha: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                     plt_n         ptl_p       alg_stl      ben_disp      ben_nh3n      ptln_stl      ptlp_stl       cst_stl       ben_cst    cbn_bod_co        air_rt   cbn_bod_stl       ben_bod      bact_die     cst_decay     nh3n_no2n     no2n_no3n     ptln_nh3n     ptlp_solp    q2e_lt   q2e_alg      chla_alg         alg_n         alg_p   alg_o2_prod   alg_o2_resp       o2_nh3n       o2_no2n      alg_grow      alg_resp       slr_act         lt_co       const_n       const_p     lt_nonalg     alg_shd_l    alg_shd_nl      nh3_pref  description`.
- Nonblank records after the header: 1.
- First demo data record: `nutcha1                0.00000       0.00000       1.00000       0.05000       0.50000       0.05000       0.05000       2.50000       2.50000       1.71000      50.00000       0.36000       2.00000       2.00000       1.71000       0.55000       1.10000       0.21000       0.35000         2         2      50.00000       0.08000       0.01500       1.60000       2.00000       3.50000       1.07000       2.00000       2.50000       0.30000       0.75000       0.02000       0.02500       1.00000       0.03000       0.05400       0.50000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `nutcha1` |
| `plt_n` | Plant-related parameter or record reference. | `0.00000` |
| `ptl_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `alg_stl` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `ben_disp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.05000` |
| `ben_nh3n` | Ammonia-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0.50000` |
| `ptln_stl` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.05000` |
| `ptlp_stl` | Phosphorus-related component; verify units in the reader. | `0.05000` |
| `cst_stl` | Field named in the demo/source header; trace the reader for exact units and storage. | `2.50000` |
| `ben_cst` | Field named in the demo/source header; trace the reader for exact units and storage. | `2.50000` |
| `cbn_bod_co` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.71000` |
| `air_rt` | Field named in the demo/source header; trace the reader for exact units and storage. | `50.00000` |
| `cbn_bod_stl` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.36000` |
| `ben_bod` | Field named in the demo/source header; trace the reader for exact units and storage. | `2.00000` |
| `bact_die` | Pathogen/bacteria-related value or parameter; verify units in the reader. | `2.00000` |
| `cst_decay` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.71000` |
| `nh3n_no2n` | Ammonia-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0.55000` |
| `no2n_no3n` | Nitrate-nitrogen concentration, mass, or parameter component; verify units in the reader. | `1.10000` |
| `ptln_nh3n` | Ammonia-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0.21000` |
| `ptlp_solp` | Phosphorus-related component; verify units in the reader. | `0.35000` |
| `q2e_lt` | Field named in the demo/source header; trace the reader for exact units and storage. | `2` |
| `q2e_alg` | Field named in the demo/source header; trace the reader for exact units and storage. | `2` |
| `chla_alg` | Field named in the demo/source header; trace the reader for exact units and storage. | `50.00000` |
| `alg_n` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.08000` |
| `alg_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.01500` |
| `alg_o2_prod` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.60000` |
| `alg_o2_resp` | Reservoir-related parameter or object reference. | `2.00000` |
| `o2_nh3n` | Ammonia-nitrogen concentration, mass, or parameter component; verify units in the reader. | `3.50000` |
| `o2_no2n` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.07000` |
| `alg_grow` | Field named in the demo/source header; trace the reader for exact units and storage. | `2.00000` |
| `alg_resp` | Reservoir-related parameter or object reference. | `2.50000` |
| `slr_act` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.30000` |
| `lt_co` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.75000` |
| `const_n` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.02000` |
| `const_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.02500` |
| `lt_nonalg` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `alg_shd_l` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.03000` |
| `alg_shd_nl` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.05400` |
| `nh3_pref` | Ammonia-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0.50000` |
| `description` | Free-text description retained for reader/user context. | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cha%nut` defaulting to `nutrients.cha`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/ch_read_nut.f90`.

## Downstream Consumers

Channel or SWAT-DEG channel hydrology, sediment, nutrient, and initialization routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/nutrients.cha`.

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
