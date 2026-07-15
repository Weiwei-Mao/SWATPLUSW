---
title: tillage.til input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `tillage.til`

## Purpose

Tillage operation database.


## Official SWAT+ Reference

- Official page: [tillage.til](https://swatplus.gitbook.io/io-docs/introduction-1/databases/tillage.til).
- Official index note: The tillage database summarizes parameters used by the model to simulate the effects of different types of tillage equipment.
- Official field metadata available: 3 field row(s); matched to 3 of 7 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Databases.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_parmdb%till_til = "tillage.til"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/tillage.til`:

- Title/comment line: `tillage.til: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                   mix_eff        mix_dp         rough      ridge_ht      ridge_sp  description`.
- Nonblank records after the header: 79.
- First demo data record: `puddle                 0.980       150.000        00.000         0.000         0.000    rice_paddy_puddling_oprtn`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of tillage record. | - | - | - | - | `puddle` | official GitBook |
| `mix_eff` | Mixing efficiency of the tillage operation. | - | - | - | - | `0.980` | official GitBook |
| `mix_dp` | Depth of mixing caused by the tillage operation. | - | - | - | - | `150.000` | official GitBook |
| `rough` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `00.000` | demo/source inferred |
| `ridge_ht` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.000` | demo/source inferred |
| `ridge_sp` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.000` | demo/source inferred |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `rice_paddy_puddling_oprtn` | demo/source inferred |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_parmdb%till_til` defaulting to `tillage.til`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/till_parm_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/tillage.til`.

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
