---
title: landuse.lum input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `landuse.lum`

## Purpose

Land-use-management database; links land-use names to plant cover, management schedule, curve-number table, and structural features.


## Official SWAT+ Reference

- Official page: [landuse.lum](https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/landuse.lum).
- Official index note: This file summarizes the main land use information and references several other files that specify the details.
- Official field metadata available: 14 field row(s); matched to 13 of 14 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Landuse Management.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_lum%landuse_lum = "landuse.lum"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/landuse.lum`:

- Title/comment line: `landuse.lum: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                         cal_group          plnt_com               mgt               cn2         cons_prac             urban            urb_ro           ov_mann              tile               sep               vfs              grww               bmp`.
- Nonblank records after the header: 15.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the land use and management record. | - | - | - | - | - | official GitBook |
| `cal_group` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | - | demo/source inferred |
| `plnt_com` | Pointer to the plant community file. | - | - | - | - | - | official GitBook |
| `mgt` | Pointer to the management schedule file. | - | - | - | - | - | official GitBook |
| `cn2` | Pointer to the Curve Number database. | - | - | - | - | - | official GitBook |
| `cons_prac` | Pointer to the conservation practice database. | - | - | - | - | - | official GitBook |
| `urban` | Pointer to the urban database. | - | - | - | - | - | official GitBook |
| `urb_ro` | Urban runoff simulation option. | - | - | - | - | - | official GitBook |
| `ov_mann` | Pointer to the overland Manning's n database. | - | - | - | - | - | official GitBook |
| `tile` | Pointer to the tile drain file. | - | - | - | - | - | official GitBook |
| `sep` | Pointer to the septic file. | - | - | - | - | - | official GitBook |
| `vfs` | Pointer to the filter strip file. | - | - | - | - | - | official GitBook |
| `grww` | Pointer to the grassed waterway file. | - | - | - | - | - | official GitBook |
| `bmp` | Pointer to the user BMP file. | - | - | - | - | - | official GitBook |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `cal_grp` | Calibration group. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_lum%landuse_lum` defaulting to `landuse.lum`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/landuse_read.f90`.

## Downstream Consumers

Land-use assignment, management schedules, conservation practices, and curve-number behavior.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/landuse.lum`.

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
