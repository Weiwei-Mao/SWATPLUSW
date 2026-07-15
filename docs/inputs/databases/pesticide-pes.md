---
title: pesticide.pes input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `pesticide.pes`

## Purpose

Pesticide parameter database.

## Role In SWAT+

- Category: Databases.
- Usage class: `conditional input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_parmdb%pest = "pesticide.pes"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/pesticide.pes`:

- Title/comment line: `pesticide.pes: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                  soil_ads     frac_wash    hl_foliage       hl_soil         solub      aq_hlife      aq_volat        mol_wt      aq_resus     aq_settle   ben_act_dep      ben_bury     ben_hlife  description`.
- Nonblank records after the header: 233.
- First demo data record: `245-tp              2600.00000       0.40000       5.00000      20.00000       2.50000       0.00700       0.00001       0.10000       0.00200       0.50000       0.30000       0.00200       0.05000  Silvex_Amine`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `245-tp` |
| `soil_ads` | Soil-related parameter or record reference. | `2600.00000` |
| `frac_wash` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.40000` |
| `hl_foliage` | Field named in the demo/source header; trace the reader for exact units and storage. | `5.00000` |
| `hl_soil` | Soil-related parameter or record reference. | `20.00000` |
| `solub` | Field named in the demo/source header; trace the reader for exact units and storage. | `2.50000` |
| `aq_hlife` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00700` |
| `aq_volat` | Volume-related value or parameter. | `0.00001` |
| `mol_wt` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.10000` |
| `aq_resus` | Reservoir-related parameter or object reference. | `0.00200` |
| `aq_settle` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.50000` |
| `ben_act_dep` | Depth, deposition, or dependency field; verify exact meaning in the reader. | `0.30000` |
| `ben_bury` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.00200` |
| `ben_hlife` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.05000` |
| `description` | Free-text description retained for reader/user context. | `Silvex_Amine` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_parmdb%pest` defaulting to `pesticide.pes`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/pest_parm_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/pesticide.pes`.

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
