---
title: cal_parms.cal input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `cal_parms.cal`

## Purpose

Calibration parameter definition file.


## Official SWAT+ Reference

- Official page: [cal_parms.cal](https://swatplus.gitbook.io/io-docs/introduction-1/calibration/cal_parms.cal).
- Official field metadata: the page is linked, but this pass did not extract a field table from it. Use the linked page and source reader for canonical definitions.
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Calibration.
- Usage class: `conditional input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_chg%cal_parms = "cal_parms.cal"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/cal_parms.cal`:

- Title/comment line: `cal_parms.cal: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Pre-header/count line(s): `226`.
- Observed header line: `name                       obj_typ       abs_min       abs_max             units`.
- Nonblank records after the header: 226.
- First demo data record: `cn2                            hru      35.00000      95.00000              null`.

## Fields And Parameters

The table is generated from the local demo header. Meanings are practical working descriptions and should be confirmed against the reader before final use.

| Field | Working meaning | Demo value | Basis |
| --- | --- | --- | --- |
| `name` | Record name used by other SWAT+ inputs to reference this row. | `cn2` | demo/source inferred |
| `obj_typ` | SWAT+ object type. | `hru` | demo/source inferred |
| `abs_min` | Minimum value or lower bound, depending on the reader. | `35.00000` | demo/source inferred |
| `abs_max` | Maximum value or upper bound, depending on the reader. | `95.00000` | demo/source inferred |
| `units` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `null` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_chg%cal_parms` defaulting to `cal_parms.cal`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/cal_parm_read.f90`.

## Downstream Consumers

Calibration/update routines that alter parameters or apply soft-calibration changes.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/cal_parms.cal`.

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
