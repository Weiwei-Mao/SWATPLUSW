---
title: weather-sta.cli input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `weather-sta.cli`

## Purpose

Weather station list and links to precipitation, temperature, solar radiation, wind, and generator records.


## Official SWAT+ Reference

- Official page: [weather-sta.cli](https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-sta.cli).
- Official index note: This file lists the weather stations defined for a SWAT+ setup.
- Official field metadata available: 10 field row(s); matched to 9 of 9 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Climate.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cli%weat_sta = "weather-sta.cli"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/weather-sta.cli`:

- Title/comment line: `weather-sta.cli: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                           wgn                        pcp                        tmp                        slr                        hmd                        wnd           wnd_dir          atmo_dep`.
- Nonblank records after the header: 1.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the weather station. | `string` | - | - | - | - | official GitBook |
| `wgn` | Name of the weather generator station. | `string` | - | - | - | - | official GitBook |
| `pcp` | Name of the precipitation station. | `string` | - | - | - | - | official GitBook |
| `tmp` | Name of the temperature station. | `string` | - | - | - | - | official GitBook |
| `slr` | Name of the solar radiation station. | `string` | - | - | - | - | official GitBook |
| `hmd` | Name of the relative humidity station. | `string` | - | - | - | - | official GitBook |
| `wnd` | Name of the wind speed station. | `string` | - | - | - | - | official GitBook |
| `wnd_dir` | Name of the wind direction station (currently not used). | `string` | - | - | - | - | official GitBook |
| `atmo_dep` | Name of the atmospheric deposition station. | `string` | - | - | - | - | official GitBook |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `pet` | Name of the PET station. | `string` | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cli%weat_sta` defaulting to `weather-sta.cli`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/cli_staread.f90`.

## Downstream Consumers

Climate station assignment and daily/subdaily weather forcing used by hydrology and plant-growth routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/weather-sta.cli`.

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
