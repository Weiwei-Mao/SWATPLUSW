---
title: "*.tmp input file"
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `*.tmp`

## Purpose

Temperature time-series file named by a temperature gauge manifest.

## Role In SWAT+

- Category: Climate Timeseries.
- Usage class: `indirect input`.
- Activation: manifest file when `tmp.cli` is active.
- `Osu_1hru` status: `indirect`.
- Source inventory: indirect file family, resolved through a manifest rather than a fixed `input_file_module.f90` slot.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file family is not normally listed directly in `file.cio`. It is reached through a manifest, for example a climate `*.cli` file that names the time-series data file.

Local demo evidence from `VSProj/SWAT/Osu_1hru/Imsiltmp.tmp`:

- Title/comment line: `Imsiltmp.tmp: Temperature data - file written by SWAT+ editor 2023-03-22 04:22:29.141050`.
- Observed header line: `nbyr     tstep       lat       lon      elev`.
- Nonblank records after the header: 15706.
- First demo data record: `42         0    35.610   127.290   247.900`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `nbyr` | Number of years represented in the time-series file. | `42` |
| `tstep` | Time-step or aggregation code for the time-series values. | `0` |
| `lat` | Latitude of the station or object. | `35.610` |
| `lon` | Longitude of the station or object. | `127.290` |
| `elev` | Elevation of the station or object. | `247.900` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: not found as a direct default filename in the source inventory.
- Candidate reader/source files: not found by a simple source-slot or literal-filename search; use `rg` from the source inventory slot, parent module, or filename stem as the next tracing step.

## Downstream Consumers

Climate station assignment and daily/subdaily weather forcing used by hydrology and plant-growth routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `indirect`.
- Activation evidence: manifest file when `tmp.cli` is active.
- Local file evidence: `VSProj/SWAT/Osu_1hru/Imsiltmp.tmp`.

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
- [Climate manifest files](../climate/pcp-cli.md)
- [Master input manifest](../simulation/file-cio.md)
