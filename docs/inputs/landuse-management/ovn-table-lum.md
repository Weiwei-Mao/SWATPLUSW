---
title: ovn_table.lum input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `ovn_table.lum`

## Purpose

Overland Manning's `n` lookup table.


## Official SWAT+ Reference

- Official page: [ovn_table.lum](https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/ovn_table.lum).
- Official index note: This file lists overland Manning's n values for different tillage and land cover types.
- Official field metadata available: 4 field row(s); matched to 4 of 5 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Landuse Management.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_lum%ovn_lum = "ovn_table.lum"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/ovn_table.lum`:

- Title/comment line: `ovn_table.lum: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                  ovn_mean       ovn_min       ovn_max  description`.
- Nonblank records after the header: 20.
- First demo data record: `fallow_nores           0.01000       0.00800       0.01200  Fallow_no_residue`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Overland flow Manning's n class name. | - | - | - | - | `fallow_nores` | official GitBook |
| `ovn_mean` | Mean overland flow Manning's n value. | - | - | - | - | `0.01000` | official GitBook |
| `ovn_min` | Overland flow Manning's N minimum. | - | - | - | - | `0.00800` | official GitBook |
| `ovn_max` | Overland flow Manning's N maximum. | - | - | - | - | `0.01200` | official GitBook |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `Fallow_no_residue` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_lum%ovn_lum` defaulting to `ovn_table.lum`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/overland_n_read.f90`.

## Downstream Consumers

Land-use assignment, management schedules, conservation practices, and curve-number behavior.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/ovn_table.lum`.

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
