---
title: grassedww.str input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `grassedww.str`

## Purpose

Grassed-waterway structural parameter database.


## Official SWAT+ Reference

- Official page: [grassedww.str](https://swatplus.gitbook.io/io-docs/introduction-1/structural-practices/grassedww.str).
- Official index note: This file contains the grassed waterway parameters.
- Official field metadata available: 7 field row(s); matched to 7 of 9 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Structural.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_str%grassww_str = "grassedww.str"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/grassedww.str`:

- Title/comment line: `grassedww.str: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                  flag          mann        sed_co            dp            wd           len           slp  description`.
- Nonblank records after the header: 3.
- First demo data record: `grwway_high              0       0.05000       0.02000       1.00000       4.00000       0.50000       0.10000  Slope_>8`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the grassed waterway record. | - | - | - | - | `grwway_high` | official GitBook |
| `flag` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `mann` | Manning's n for grassed waterway. | - | - | - | - | `0.05000` | official GitBook |
| `sed_co` | Sediment transport coefficient. | - | - | - | - | `0.02000` | official GitBook |
| `dp` | Depth of grassed waterway. | - | - | - | - | `1.00000` | official GitBook |
| `wd` | Width of grassed waterway. | - | - | - | - | `4.00000` | official GitBook |
| `len` | Length of grassed waterway. | - | - | - | - | `0.50000` | official GitBook |
| `slp` | Slope of grassed waterway. | - | - | - | - | `0.10000` | official GitBook |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `Slope_>8` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_str%grassww_str` defaulting to `grassedww.str`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/scen_read_grwway.f90`.

## Downstream Consumers

Structural practice routines such as tile drains, filter strips, grassed waterways, septic systems, and BMP adjustments.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/grassedww.str`.

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
