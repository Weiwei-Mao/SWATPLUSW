---
title: water_rights.wro input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `water_rights.wro`

## Purpose

Input file for water-rights; source slot water_rights.

## Role In SWAT+

- Category: Water Allocation.
- Usage class: `conditional input`.
- Activation: module switch, object count, or inactive `file.cio` slot.
- `Osu_1hru` status: `inactive/null`.
- Source inventory slot(s): `in_watrts%water_rights = "water_rights.wro"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence: the `Osu_1hru` scenario does not include a concrete `water_rights.wro` file, or the file family is inactive there. Use another scenario or the reader routine for field-level confirmation.

## Fields And Parameters

No local demo header is available for this file. The page currently documents role, activation, and source inventory only; field names, units, and storage should be added after tracing the reader or adding an active demo file.

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_watrts%water_rights` defaulting to `water_rights.wro`.
- Candidate reader/source files: not found by a simple source-slot or literal-filename search; use `rg` from the source inventory slot, parent module, or filename stem as the next tracing step.

## Downstream Consumers

Water-rights and allocation routines when water allocation is enabled.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `inactive/null`.
- Activation evidence: module switch, object count, or inactive `file.cio` slot.
- Local file evidence: no concrete file found in the demo scenario.

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
