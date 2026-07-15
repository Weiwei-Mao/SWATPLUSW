---
title: lum.dtl input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `lum.dtl`

## Purpose

Land-use/management decision tables, including growth-start and growth-end rules used by some routines.


## Official SWAT+ Reference

- Official page: ["name".dtl](https://swatplus.gitbook.io/io-docs/introduction-1/decision-tables/lum.dtl).
- Official index note: These files contain the Decision Tables.
- Official field metadata available: 14 field row(s); matched to 1 of 4 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Decision Tables.
- Usage class: `conditional input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cond%dtbl_lum = "lum.dtl"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/lum.dtl`:

- Title/comment line: `lum.dtl: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Pre-header/count line(s): `53`.
- Observed header line: `NAME   	 CONDS	ALTS	ACTS`.
- Nonblank records after the header: 497.
- First demo data record: `plow		  2       2      2`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `NAME` | Name of the action. | - | - | - | - | `plow` | official GitBook |
| `CONDS` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `2` | demo/source inferred |
| `ALTS` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `2` | demo/source inferred |
| `ACTS` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `2` | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `var` | Condition variable. | `string` | - |
| `obj` | Object type. | `string` | - |
| `obj_num` | Object ID. | `integer` | - |
| `lim_var` | Limit variable. | `string` | - |
| `lim_op` | Limit operator. | `string` | - |
| `lim_const` | Limit constant. | `real` | - |
| `alt` | Alternative. | `string` | - |
| `act_typ` | Official field row listed for this file. | - | - |
| `option` | Official field row listed for this file. | - | - |
| `const` | Official field row listed for this file. | - | - |
| `const2` | Official field row listed for this file. | - | - |
| `fp` | File pointer. | - | - |
| `outcome` | Outcome. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cond%dtbl_lum` defaulting to `lum.dtl`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/dtbl_lum_read.f90`.

## Downstream Consumers

Decision-table evaluation for management, flow, scenario, or release decisions.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/lum.dtl`.

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
