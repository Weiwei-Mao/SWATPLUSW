---
title: tiledrain.str input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `tiledrain.str`

## Purpose

Structural tile-drain parameter database.


## Official SWAT+ Reference

- Official page: [tiledrain.str](https://swatplus.gitbook.io/io-docs/introduction-1/structural-practices/tiledrain.str).
- Official index note: This file contains the tile drainage parameters.
- Official field metadata available: 9 field row(s); matched to 9 of 9 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Structural.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_str%tiledrain_str = "tiledrain.str"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/tiledrain.str`:

- Title/comment line: `tiledrain.str: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                        dp          t_fc           lag           rad          dist         drain          pump      lat_ksat`.
- Nonblank records after the header: 1.
- First demo data record: `mw24_1000           1000.00000      24.00000      96.00000     100.00000      30.00000      10.00000       1.00000       2.00000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the tile drain record. | - | - | - | - | `mw24_1000` | official GitBook |
| `dp` | Depth of drain tube from the soil surface. | - | - | - | - | `1000.00000` | official GitBook |
| `t_fc` | Time to drain soil to field capacity. | - | - | - | - | `24.00000` | official GitBook |
| `lag` | Drain tile lag time. | - | - | - | - | `96.00000` | official GitBook |
| `rad` | Effective radius of drains. | - | - | - | - | `100.00000` | official GitBook |
| `dist` | Distance between two drain tubes or tiles. | - | - | - | - | `30.00000` | official GitBook |
| `drain` | Drainage coefficient. | - | - | - | - | `10.00000` | official GitBook |
| `pump` | Pump capacity. | - | - | - | - | `1.00000` | official GitBook |
| `lat_ksat` | Multiplication factor to determine lateral saturated hydraulic conductivity. | - | - | - | - | `2.00000` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_str%tiledrain_str` defaulting to `tiledrain.str`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/sdr_read.f90`.

## Downstream Consumers

Structural practice routines such as tile drains, filter strips, grassed waterways, septic systems, and BMP adjustments.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/tiledrain.str`.

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
