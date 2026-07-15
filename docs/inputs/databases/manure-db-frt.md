---
title: manure_db.frt input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `manure_db.frt`

## Purpose

Optional manure database with extended manure composition information.

## Role In SWAT+

- Category: Databases.
- Usage class: `fixed-name companion`.
- Activation: fixed-name or derived reader.
- `Osu_1hru` status: `fixed-name/conditional`.
- Source inventory: no direct default slot was found in `input_file_module.f90`; trace fixed-name or derived readers before treating the filename as mandatory.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is a fixed-name or derived companion rather than a primary `file.cio` selection. The reader may open it by convention when its parent workflow is active.

Local demo evidence from `VSProj/SWAT/Osu_1hru/manure_db.frt`:

- Title/comment line: `manure_db.frt: manure database`.
- Observed header line: `name          org_min             pests  paths  hmets  salts  constit  description`.
- Nonblank records after the header: 1.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | - |
| `org_min` | Minimum value or lower bound, depending on the reader. | - |
| `pests` | Pesticide-related value or parameter; verify units in the reader. | - |
| `paths` | Pathogen/bacteria-related value or parameter; verify units in the reader. | - |
| `hmets` | Heavy-metal related value or parameter; verify units in the reader. | - |
| `salts` | Salt constituent value or parameter; verify units in the reader. | - |
| `constit` | Field named in the demo/source header; trace the reader for exact units and storage. | - |
| `description` | Free-text description retained for reader/user context. | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: not found as a direct default filename in the source inventory.
- Candidate reader/source files: `SWATPLUS/swatplus/src/manure_db_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `fixed-name/conditional`.
- Activation evidence: fixed-name or derived reader.
- Local file evidence: `VSProj/SWAT/Osu_1hru/manure_db.frt`.

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
