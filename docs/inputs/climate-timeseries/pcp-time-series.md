---
title: "*.pcp input file"
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `*.pcp`

## Purpose

Precipitation time-series file named by a precipitation gauge manifest.


## Official SWAT+ Reference

- Official page: [pcp.cli and pcp data files](https://swatplus.gitbook.io/io-docs/introduction-1/climate/pcp.cli-and-precipitation-data-files).
- Official index note: These files contain all information needed by the model about observed precipitation data.
- Official field metadata available: 11 field row(s); matched to 5 of 5 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Climate Timeseries.
- Usage class: `indirect input`.
- Activation: manifest file when `pcp.cli` is active.
- `Osu_1hru` status: `indirect`.
- Source inventory: indirect file family, resolved through a manifest rather than a fixed `input_file_module.f90` slot.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file family is not normally listed directly in `file.cio`. It is reached through a manifest, for example a climate `*.cli` file that names the time-series data file.

Local demo evidence from `VSProj/SWAT/Osu_1hru/Imsilpcp.pcp`:

- Title/comment line: `Imsilpcp.pcp: Precipitation data - file written by SWAT+ editor 2023-03-22 04:22:29.020522`.
- Observed header line: `nbyr     tstep       lat       lon      elev`.
- Nonblank records after the header: 15706.
- First demo data record: `42         0    35.610   127.290   247.900`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nbyr` | Length of the precipitation time series. | `integer` | `years` | - | - | `42` | official GitBook |
| `tstep` | Time step of the precipitation data. | `integer` | `n/a` | - | - | `0` | official GitBook |
| `lat` | Latitude of the precipitation station. | `real` | `Decimal Degrees` | - | - | `35.610` | official GitBook |
| `lon` | Longitude of the precipitation station. | `real` | `Decimal Degrees` | - | - | `127.290` | official GitBook |
| `elev` | Elevation of the precipitation station. | `real` | `m` | - | - | `247.900` | official GitBook |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `year` | Year of the observation. | `integer` | `n/a` |
| `jday` | Julian day of the observation. | `integer` | `n/a` |
| `pcp` | Observed precipitation. | `real` | `mm` |
| `mon` | Month of the observation. | `integer` | `n/a` |
| `day` | Day of the observation. | `integer` | `n/a` |
| `hr` | Time of the observation. | `integer` | `n/a` |

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
- Activation evidence: manifest file when `pcp.cli` is active.
- Local file evidence: `VSProj/SWAT/Osu_1hru/Imsilpcp.pcp`.

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
