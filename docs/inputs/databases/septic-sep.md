---
title: septic.sep input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `septic.sep`

## Purpose

Septic-system parameter database.

## Role In SWAT+

- Category: Databases.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_parmdb%septic_sep = "septic.sep"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/septic.sep`:

- Title/comment line: `septic.sep: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                    q_rate           bod           tss         nh4_n         no3_n         no2_n         org_n         min_p         org_p         fcoli  description`.
- Nonblank records after the header: 26.
- First demo data record: `gcon                   0.22700     170.00000      75.00000      42.40000       0.00000       0.00000      10.00000       6.00000       1.00000  10000000.00000  1Generic`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `gcon` |
| `q_rate` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.22700` |
| `bod` | Field named in the demo/source header; trace the reader for exact units and storage. | `170.00000` |
| `tss` | Field named in the demo/source header; trace the reader for exact units and storage. | `75.00000` |
| `nh4_n` | Field named in the demo/source header; trace the reader for exact units and storage. | `42.40000` |
| `no3_n` | Nitrate-nitrogen concentration, mass, or parameter component; verify units in the reader. | `0.00000` |
| `no2_n` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00000` |
| `org_n` | Field named in the demo/source header; trace the reader for exact units and storage. | `10.00000` |
| `min_p` | Minimum value or lower bound, depending on the reader. | `6.00000` |
| `org_p` | Field named in the demo/source header; trace the reader for exact units and storage. | `1.00000` |
| `fcoli` | Field named in the demo/source header; trace the reader for exact units and storage. | `10000000.00000` |
| `description` | Free-text description retained for reader/user context. | `1Generic` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_parmdb%septic_sep` defaulting to `septic.sep`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/septic_parm_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/septic.sep`.

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
