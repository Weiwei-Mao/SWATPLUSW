---
title: cntable.lum input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `cntable.lum`

## Purpose

Curve-number lookup table by land use and soil/hydrologic condition.


## Official SWAT+ Reference

- Official page: [cntable.lum](https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/cntable.lum).
- Official index note: This file lists typical Curve Number values for different land use types.
- Official field metadata available: 5 field row(s); matched to 5 of 8 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Landuse Management.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_lum%cntable_lum = "cntable.lum"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/cntable.lum`:

- Title/comment line: `cntable.lum: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                      cn_a          cn_b          cn_c          cn_d  description                                                             treat                                     cond_cov`.
- Nonblank records after the header: 52.
- First demo data record: `fal_bare              77.00000      86.00000      91.00000      94.00000  Fallow                                                                  Bare_soil                                 ----`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Curve Number class name. | - | - | - | - | `fal_bare` | official GitBook |
| `cn_a` | Curve number for hydrologic soil group A. | - | - | - | - | `77.00000` | official GitBook |
| `cn_b` | Curve number for hydrologic soil group B. | - | - | - | - | `86.00000` | official GitBook |
| `cn_c` | Curve number for hydrologic soil group C. | - | - | - | - | `91.00000` | official GitBook |
| `cn_d` | Curve number for hydrologic soil group D. | - | - | - | - | `94.00000` | official GitBook |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `Fallow` | demo/source inferred |
| `treat` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `Bare_soil` | demo/source inferred |
| `cond_cov` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `----` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_lum%cntable_lum` defaulting to `cntable.lum`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/cntbl_read.f90`.

## Downstream Consumers

Land-use assignment, management schedules, conservation practices, and curve-number behavior.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/cntable.lum`.

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
