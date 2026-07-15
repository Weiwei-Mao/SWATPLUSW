---
title: salt_hru.ini input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `salt_hru.ini`

## Purpose

Initial salt setup for HRU soil/plant salt simulation.


## Official SWAT+ Reference

- Official page: [salt_hru.ini](https://swatplus.gitbook.io/io-docs/introduction-1/initialization/salt_hru.ini).
- Official field metadata: the page is linked, but this pass did not extract a field table from it. Use the linked page and source reader for canonical definitions.

## Role In SWAT+

- Category: Initialization.
- Usage class: `conditional input`.
- Activation: module switch, object count, or inactive `file.cio` slot.
- `Osu_1hru` status: `inactive/null`.
- Source inventory slot(s): `in_init%salt_soil = "salt_hru.ini"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence: `VSProj/SWAT/Osu_1hru/salt_hru.ini` exists but is empty, so it proves presence only, not the data layout.

## Fields And Parameters

No local demo header or standalone official field table is available for this exact file. This page currently documents role, activation, source inventory, and demo presence only; field names, units, and storage should be added after tracing the reader or finding a scenario that activates the file.

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_init%salt_soil` defaulting to `salt_hru.ini`.
- Candidate reader/source files: not found by a simple source-slot or literal-filename search; use `rg` from the source inventory slot, parent module, or filename stem as the next tracing step.

## Downstream Consumers

Initial condition assignment for plants, soil/plant pools, water bodies, and constituents.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `inactive/null`.
- Activation evidence: module switch, object count, or inactive `file.cio` slot.
- Local file evidence: `VSProj/SWAT/Osu_1hru/salt_hru.ini`.

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
