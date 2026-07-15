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


## Official SWAT+ Reference

- Official page: [weather-wgn.cli](https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli).
- Official index note: This file contains weather generator data to be used for a SWAT+ setup.
- Official field metadata available: 19 field row(s); matched to 14 of 14 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

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

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tmp_max_ave` | Average or mean daily maximum air temperature for month. | `real` | `deg C` | - | `-30 - 50` | `3.79032` | official GitBook |
| `tmp_min_ave` | Average or mean daily minimum air temperature for month. | `real` | `deg C` | - | `-40 - 40` | `-8.02376` | official GitBook |
| `tmp_max_sd` | Standard deviation for daily maximum air temperature in month. | `real` | `deg C` | - | `0.1 - 100` | `4.11179` | official GitBook |
| `tmp_min_sd` | Standard deviation for daily minimum air temperature in month. | `real` | `deg C` | - | `0.1 - 30` | `4.74641` | official GitBook |
| `pcp_ave` | Average or mean total monthly precipitation. | `real` | `mm` | - | `0 - 600` | `0.92032` | official GitBook |
| `pcp_sd` | Standard deviation for daily precipitation in month. | `real` | `mm/day` | - | `0.1 - 50` | `2.93256` | official GitBook |
| `pcp_skew` | Skew coefficient for daily precipitation in month. | `real` | `mm` | - | `-50 - 20` | `6.86696` | official GitBook |
| `wet_dry` | Probability of a wet day following a dry day in the month. | `real` | `n/a` | - | `0 - 0.95` | `0.15699` | official GitBook |
| `wet_wet` | Probability of a wet day following a wet day in the month. | `real` | `n/a` | - | `0 - 0.95` | `0.13441` | official GitBook |
| `pcp_days` | Average number of days of precipitation in month. | `real` | `n/a` | - | `0 - 31` | `9.16667` | official GitBook |
| `pcp_hhr` | Maximum 0.5-hour rainfall in month. | `real` | `mm` | - | `0 - 125` | `3.95000` | official GitBook |
| `slr_ave` | Average daily solar radiation for month. | `real` | `MJ/m^2/day` | - | `0 - 750` | `8.59081` | official GitBook |
| `dew_ave` | Average daily dew point temperature for each month (deg C) or relative humidity (fraction). | `real` | `deg C or fraction` | - | `-50 - 25` | `0.73338` | official GitBook |
| `wnd_ave` | Average daily wind speed in month. | `real` | `m/s` | - | `0 - 100` | `1.20828` | official GitBook |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `name` | Name of weather generator station. | `string` | `n/a` |
| `latitude` | Latitude of weather generator station. | `real` | `Decimal Degrees` |
| `longitude` | Longitude of weather generator station. | `real` | `Decimal Degrees` |
| `elevation` | Elevation of weather generator station. | `real` | `m` |
| `yrs_pcp` | Number of years of maximum monthly 0.5 h rainfall data used to define values for pcp_hhr. | `integer` | `years` |

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
