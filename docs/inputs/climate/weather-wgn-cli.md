---
title: weather-wgn.cli input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `weather-wgn.cli`

## Purpose

Weather generator station list.

## Role In SWAT+

- Category: Climate.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cli%weat_wgn = "weather-wgn.cli"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/weather-wgn.cli`:

- Title/comment line: `weather-wgn.cli: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Pre-header/count line(s): `Imsil                          35.61000     127.29000     247.90000        30`.
- Observed header line: `tmp_max_ave   tmp_min_ave    tmp_max_sd    tmp_min_sd       pcp_ave        pcp_sd      pcp_skew       wet_dry       wet_wet      pcp_days       pcp_hhr       slr_ave       dew_ave       wnd_ave`.
- Nonblank records after the header: 12.
- First demo data record: `3.79032      -8.02376       4.11179       4.74641       0.92032       2.93256       6.86696       0.15699       0.13441       9.16667       3.95000       8.59081       0.73338       1.20828`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `tmp_max_ave` | Maximum value or upper bound, depending on the reader. | `3.79032` |
| `tmp_min_ave` | Minimum value or lower bound, depending on the reader. | `-8.02376` |
| `tmp_max_sd` | Maximum value or upper bound, depending on the reader. | `4.11179` |
| `tmp_min_sd` | Minimum value or lower bound, depending on the reader. | `4.74641` |
| `pcp_ave` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.92032` |
| `pcp_sd` | Field named in the demo/source header; trace the reader for exact units and storage. | `2.93256` |
| `pcp_skew` | Field named in the demo/source header; trace the reader for exact units and storage. | `6.86696` |
| `wet_dry` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.15699` |
| `wet_wet` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.13441` |
| `pcp_days` | Field named in the demo/source header; trace the reader for exact units and storage. | `9.16667` |
| `pcp_hhr` | Field named in the demo/source header; trace the reader for exact units and storage. | `3.95000` |
| `slr_ave` | Field named in the demo/source header; trace the reader for exact units and storage. | `8.59081` |
| `dew_ave` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.73338` |
| `wnd_ave` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.20828` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cli%weat_wgn` defaulting to `weather-wgn.cli`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/cli_wgnread.f90`.

## Downstream Consumers

Climate station assignment and daily/subdaily weather forcing used by hydrology and plant-growth routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/weather-wgn.cli`.

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
- [Climate time-series file families](../climate-timeseries/pcp-time-series.md)
- [Master input manifest](../simulation/file-cio.md)
