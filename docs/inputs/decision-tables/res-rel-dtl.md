---
title: res_rel.dtl input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `res_rel.dtl`

## Purpose

Reservoir release decision tables.


## Official SWAT+ Reference

No standalone official SWAT+ GitBook page was found for this exact filename in the current documentation index. Keep this page tied to the source inventory and local demo evidence until a reader-specific official page is identified.

## Role In SWAT+

- Category: Decision Tables.
- Usage class: `conditional input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cond%dtbl_res = "res_rel.dtl"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/res_rel.dtl`:

- Title/comment line: `res_rel.dtl: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Pre-header/count line(s): `5`.
- Observed header line: `NAME                  CONDS       ALTS       ACTS`.
- Nonblank records after the header: 45.
- First demo data record: `weir                     	 2         2         2`.

## Fields And Parameters

The table is generated from the local demo header. Meanings are practical working descriptions and should be confirmed against the reader before final use.

| Field | Working meaning | Demo value | Basis |
| --- | --- | --- | --- |
| `NAME` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `weir` | demo/source inferred |
| `CONDS` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `2` | demo/source inferred |
| `ALTS` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `2` | demo/source inferred |
| `ACTS` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `2` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cond%dtbl_res` defaulting to `res_rel.dtl`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/dtbl_res_read.f90`.

## Downstream Consumers

Decision-table evaluation for management, flow, scenario, or release decisions.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/res_rel.dtl`.

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
