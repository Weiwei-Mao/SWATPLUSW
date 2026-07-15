---
title: aqu_catunit.ele input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `aqu_catunit.ele`

## Purpose

Aquifer calibration/category-unit element file.


## Official SWAT+ Reference

No standalone official SWAT+ GitBook page was found for this exact filename in the current documentation index. Keep this page tied to the source inventory and local demo evidence until a reader-specific official page is identified.

## Role In SWAT+

- Category: Regions.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_regs%ele_aqu = "aqu_catunit.ele"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/aqu_catunit.ele`:

- Title/comment line: `aqu_catunit.ele: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `id  name                   obj_typ  obj_typ_no      bsn_frac      sub_frac      reg_frac`.
- Nonblank records after the header: 21.
- First demo data record: `1  aqu011                     aqu           1       0.00241       0.00000       0.00000`.

## Fields And Parameters

The table is generated from the local demo header. Meanings are practical working descriptions and should be confirmed against the reader before final use.

| Field | Working meaning | Demo value | Basis |
| --- | --- | --- | --- |
| `id` | Numeric record identifier. | `1` | demo/source inferred |
| `name` | Record name used by other SWAT+ inputs to reference this row. | `aqu011` | demo/source inferred |
| `obj_typ` | SWAT+ object type. | `aqu` | demo/source inferred |
| `obj_typ_no` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `1` | demo/source inferred |
| `bsn_frac` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0.00241` | demo/source inferred |
| `sub_frac` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0.00000` | demo/source inferred |
| `reg_frac` | Header field observed in the demo file; trace the reader for exact storage and constraints. | `0.00000` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_regs%ele_aqu` defaulting to `aqu_catunit.ele`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/aqu_read_elements.f90`.

## Downstream Consumers

Regionalization, category-unit, and element-membership mapping for calibration or reporting groups.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/aqu_catunit.ele`.

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
