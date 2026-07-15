---
title: management.sch input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `management.sch`

## Purpose

Management schedules that sequence operations over time.


## Official SWAT+ Reference

- Official page: [management.sch](https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/management.sch).
- Official index note: This file is used to schedule management operations.
- Official field metadata available: 5 field row(s); matched to 5 of 10 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Landuse Management.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_lum%management_sch = "management.sch"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/management.sch`:

- Title/comment line: `management.sch: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                       numb_ops  numb_auto            op_typ       mon       day        hu_sch          op_data1          op_data2      op_data3`.
- Nonblank records after the header: 21.
- First demo data record: `rice140_rot    					  1           7`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the management schedule. | - | - | - | - | `rice140_rot` | official GitBook |
| `numb_ops` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1` | demo/source inferred |
| `numb_auto` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `7` | demo/source inferred |
| `op_typ` | Type of management operation. | - | - | - | - | - | official GitBook |
| `mon` | Calendar month or monthly period value. | - | - | - | - | - | demo/source inferred |
| `day` | Day-of-month or Julian-day value, depending on the reader. | - | - | - | - | - | demo/source inferred |
| `hu_sch` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | - | demo/source inferred |
| `op_data1` | Operation data 1. | - | - | - | - | - | official GitBook |
| `op_data2` | Operation data 2. | - | - | - | - | - | official GitBook |
| `op_data3` | Operation data 3. | - | - | - | - | - | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_lum%management_sch` defaulting to `management.sch`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/mgt_read_mgtops.f90`.

## Downstream Consumers

Land-use assignment, management schedules, conservation practices, and curve-number behavior.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/management.sch`.

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
