---
title: hru-data.hru input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `hru-data.hru`

## Purpose

Full HRU database file; links each HRU definition to land use, soil, hydrology, topography, snow, and field records.


## Official SWAT+ Reference

- Official page: [hru-data.hru](https://swatplus.gitbook.io/io-docs/introduction-1/hydrologic-response-units/hru-data.hru).
- Official index note: This file contains pointers to several files that specify the HRU properties.
- Official field metadata available: 10 field row(s); matched to 10 of 10 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Hru.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_hru%hru_data = "hru-data.hru"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/hru-data.hru`:

- Title/comment line: `hru-data.hru: writteby SWAT+ editor v2.2on 2023-03-22 04:25     for SWAT+ rev.6               0.5.4`.
- Observed header line: `id        name                topo               hydro                soil              lu_mgt     soil_plant_init           surf_stor                snow               field`.
- Nonblank records after the header: 1.
- First demo data record: `1    hru0001         topohru0001             hyd0001           PadHOEGOG         rice140_lum          soilplant1           paddy0001             snow001                null`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | ID of the HRU. | `integer` | - | - | - | `1` | official GitBook |
| `name` | Name the of HRU. | `string` | - | - | - | `hru0001` | official GitBook |
| `topo` | Pointer to the topography file. | `string` | - | - | - | `topohru0001` | official GitBook |
| `hydro` | Pointer to the hydrology file. | `string` | - | - | - | `hyd0001` | official GitBook |
| `soil` | Pointer to the soil file. | `string` | - | - | - | `PadHOEGOG` | official GitBook |
| `lu_mgt` | Pointer to the land use and management file. | `string` | - | - | - | `rice140_lum` | official GitBook |
| `soil_plant_init` | Pointer to the soil and plant initialization file. | `string` | - | - | - | `soilplant1` | official GitBook |
| `surf_stor` | Pointer to the wetland file. | `string` | - | - | - | `paddy0001` | official GitBook |
| `snow` | Pointer to the snow file. | `string` | - | - | - | `snow001` | official GitBook |
| `field` | Pointer to the field file. | `string` | - | - | - | `null` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_hru%hru_data` defaulting to `hru-data.hru`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/hru_read.f90`.

## Downstream Consumers

HRU or HRU-LTE object setup and land-phase calculations.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/hru-data.hru`.

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
