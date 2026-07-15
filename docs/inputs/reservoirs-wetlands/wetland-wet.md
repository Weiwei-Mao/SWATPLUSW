---
title: wetland.wet input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `wetland.wet`

## Purpose

Wetland object parameter file.


## Official SWAT+ Reference

- Official page: [wetland.wet](https://swatplus.gitbook.io/io-docs/introduction-1/wetlands/wetland.wet).
- Official index note: This file contains pointers referencing several files that specify the wetland properties.
- Official field metadata available: 7 field row(s); matched to 7 of 8 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Reservoirs Wetlands.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_res%wet = "wetland.wet"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/wetland.wet`:

- Title/comment line: `wetland.       wet: written by SWAT+ edi############for SWAT+ rev.60.5.4`.
- Observed header line: `id                name        init         hyd         rel         sed         nut        WEIR`.
- Nonblank records after the header: 1.
- First demo data record: `1          paddy0001    initwet1       paddy        weir     sedwet1     nutwet1       weir1`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | ID of the wetland. | - | - | - | - | `1` | official GitBook |
| `name` | Name of the wetland. | - | - | - | - | `paddy0001` | official GitBook |
| `init` | Pointer to the reservoir and wetland initialization file. | - | - | - | - | `initwet1` | official GitBook |
| `hyd` | Pointer to the wetland hydrology file. | - | - | - | - | `paddy` | official GitBook |
| `rel` | Pointer to the reservoir and wetland release decision table file. | - | - | - | - | `weir` | official GitBook |
| `sed` | Pointer to the reservoir and wetland sediment file. | - | - | - | - | `sedwet1` | official GitBook |
| `nut` | Pointer to the reservoir and wetland nutrient file. | - | - | - | - | `nutwet1` | official GitBook |
| `WEIR` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `weir1` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_res%wet` defaulting to `wetland.wet`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/wet_read.f90`.

## Downstream Consumers

Reservoir, pond, and wetland hydrology, release, sediment, and nutrient routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/wetland.wet`.

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
