---
title: nutrients.res input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `nutrients.res`

## Purpose

Reservoir nutrient and water-quality parameter database.

## Role In SWAT+

- Category: Reservoirs Wetlands.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_res%nut_res = "nutrients.res"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/nutrients.res`:

- Title/comment line: `nutrients.res: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name              mid_start   mid_end     mid_n_stl         n_stl     mid_p_stl         p_stl       chla_co     secchi_co       theta_n       theta_p     n_min_stl     p_min_stl`.
- Nonblank records after the header: 1.
- First demo data record: `nutwet1                  5        10       5.50000       5.50000      10.00000      10.00000       1.00000       1.00000       1.00000       1.00000       0.10000       0.01000`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `nutwet1` |
| `mid_start` | Field named in the demo/source header; trace the reader for exact units and storage. | `5` |
| `mid_end` | Field named in the demo/source header; trace the reader for exact units and storage. | `10` |
| `mid_n_stl` | Field named in the demo/source header; trace the reader for exact units and storage. | `5.50000` |
| `n_stl` | Field named in the demo/source header; trace the reader for exact units and storage. | `5.50000` |
| `mid_p_stl` | Field named in the demo/source header; trace the reader for exact units and storage. | `10.00000` |
| `p_stl` | Field named in the demo/source header; trace the reader for exact units and storage. | `10.00000` |
| `chla_co` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `secchi_co` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `theta_n` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `theta_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `n_min_stl` | Minimum value or lower bound, depending on the reader. | `0.10000` |
| `p_min_stl` | Minimum value or lower bound, depending on the reader. | `0.01000` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_res%nut_res` defaulting to `nutrients.res`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/res_read_csdb.f90`, `SWATPLUS/swatplus/src/res_read_nut.f90`, `SWATPLUS/swatplus/src/res_read_saltdb.f90`.

## Downstream Consumers

Reservoir, pond, and wetland hydrology, release, sediment, and nutrient routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/nutrients.res`.

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
