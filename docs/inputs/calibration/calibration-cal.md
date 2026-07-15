---
title: calibration.cal input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `calibration.cal`

## Purpose

Calibration change/update file.


## Official SWAT+ Reference

- Official page: [calibration.cal](https://swatplus.gitbook.io/io-docs/introduction-1/calibration/calibration.cal).
- Official field metadata: the page is linked, but this pass did not extract a field table from it. Use the linked page and source reader for canonical definitions.
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Calibration.
- Usage class: `conditional input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_chg%cal_upd = "calibration.cal"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/calibration.cal`:

- Title/comment line: `hru-new.cal developed from soft data calibration`.
- Pre-header/count line(s): `13`.
- Observed header line: `NAME           CHG_TYP                  VAL   CONDS  LYR1  LYR2   YEAR1  YEAR2   DAY1   DAY2  OBJ_TOT`.
- Nonblank records after the header: 13.
- First demo data record: `cn2         pctchg                  7.714000E+00  0           0           0           0           0           0           0           0           0`.

## Fields And Parameters

The table is generated from the local demo header. Meanings are practical working descriptions and should be confirmed against the reader before final use.

| Field | Working meaning | Demo value | Basis |
| --- | --- | --- | --- |
| `NAME` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `cn2` | demo/source inferred |
| `CHG_TYP` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `pctchg` | demo/source inferred |
| `VAL` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `7.714000E+00` | demo/source inferred |
| `CONDS` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0` | demo/source inferred |
| `LYR1` | Calendar year or year-range value. | `0` | demo/source inferred |
| `LYR2` | Calendar year or year-range value. | `0` | demo/source inferred |
| `YEAR1` | Calendar year or year-range value. | `0` | demo/source inferred |
| `YEAR2` | Calendar year or year-range value. | `0` | demo/source inferred |
| `DAY1` | Day-of-month or Julian-day value, depending on the reader. | `0` | demo/source inferred |
| `DAY2` | Day-of-month or Julian-day value, depending on the reader. | `0` | demo/source inferred |
| `OBJ_TOT` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_chg%cal_upd` defaulting to `calibration.cal`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/cal_parmchg_read.f90`.

## Downstream Consumers

Calibration/update routines that alter parameters or apply soft-calibration changes.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/calibration.cal`.

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
