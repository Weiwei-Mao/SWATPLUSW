---
title: topography.hyd input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `topography.hyd`

## Purpose

HRU topography parameter database, including slope, slope length, and related geometry.


## Official SWAT+ Reference

- Official page: [topography.hyd](https://swatplus.gitbook.io/io-docs/introduction-1/hydrology/topography.hyd).
- Official index note: This file defines the topographic characteristics of the HRUs and Routing Units.
- Official field metadata available: 5 field row(s); matched to 5 of 6 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Hydrology.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_hyd%topogr_hyd = "topography.hyd"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/topography.hyd`:

- Title/comment line: `topography.hyd: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                       slp       slp_len       lat_len      dist_cha         depos`.
- Nonblank records after the header: 1.
- First demo data record: `topohru0001            0.01078      10.00000      10.00000     121.00000       0.00000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the topography record. | - | - | - | - | `topohru0001` | official GitBook |
| `slp` | Average slope steepness. | - | - | - | - | `0.01078` | official GitBook |
| `slp_len` | Average slope length. | - | - | - | - | `10.00000` | official GitBook |
| `lat_len` | Average slope length for lateral subsurface flow. | - | - | - | - | `10.00000` | official GitBook |
| `dist_cha` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `121.00000` | demo/source inferred |
| `depos` | Deposition coefficient. | - | - | - | - | `0.00000` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_hyd%topogr_hyd` defaulting to `topography.hyd`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/topo_read.f90`.

## Downstream Consumers

Land-phase hydrology, topography, field geometry, and runoff/infiltration calculations.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/topography.hyd`.

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
