---
title: tmp.cli input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `tmp.cli`

## Purpose

Temperature gauge list; points to temperature time-series files.


## Official SWAT+ Reference

- Official page: [tmp.cli and tmp data files](https://swatplus.gitbook.io/io-docs/introduction-1/climate/tmp.cli-and-temperature-data-files).
- Official index note: These files contain all information needed by the model about observed temperature data.
- Official field metadata available: 9 field row(s); matched to 0 of 1 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Climate.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cli%tmp_cli = "tmp.cli"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/tmp.cli`:

- Title/comment line: `tmp.cli: Temperature file names - file written by SWAT+ editor 2023-03-22 04:22:29.141050`.
- Observed header line: `filename`.
- Nonblank records after the header: 1.
- First demo data record: `Imsiltmp.tmp`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `filename` | Referenced input file name, normally relative to the scenario folder. | - | - | - | - | `Imsiltmp.tmp` | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `nbyr` | Length of the temperature time series. | `integer` | `years` |
| `tstep` | Time step of the temperature data. | `integer` | `n/a` |
| `lat` | Latitude of the temperature station. | `real` | `Decimal Degrees` |
| `lon` | Longitude of the temperature station. | `real` | `Decimal Degrees` |
| `elev` | Elevation of the temperature station. | `real` | `m` |
| `year` | Year of the observation. | `integer` | `n/a` |
| `jday` | Julian day of the observation. | `integer` | `n/a` |
| `tmpmax` | Observed maximum temperature. | `real` | `deg C` |
| `tmpmin` | Observed minimum temperature. | `real` | `deg C` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cli%tmp_cli` defaulting to `tmp.cli`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/cli_tmeas.f90`.

## Downstream Consumers

Climate station assignment and daily/subdaily weather forcing used by hydrology and plant-growth routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/tmp.cli`.

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
