---
title: cs_hru.ini input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `cs_hru.ini`

## Purpose

Initial generic constituent setup for HRU soil/plant constituent simulation.


## Official SWAT+ Reference

No standalone official SWAT+ GitBook page was found for this exact filename in the current documentation index. Keep this page tied to the source inventory and local demo evidence until a reader-specific official page is identified.

## Role In SWAT+

- Category: Constituents Salt.
- Usage class: `fixed-name companion`.
- Activation: fixed-name or derived reader.
- `Osu_1hru` status: `fixed-name/conditional`.
- Source inventory: no direct default slot was found in `input_file_module.f90`; trace fixed-name or derived readers before treating the filename as mandatory.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is a fixed-name or derived companion rather than a primary `file.cio` selection. The reader may open it by convention when its parent workflow is active.

Local demo evidence: `VSProj/SWAT/Osu_1hru/cs_hru.ini` exists but is empty, so it proves presence only, not the data layout.

## Fields And Parameters

No local demo header or standalone official field table is available for this exact file. This page currently documents role, activation, source inventory, and demo presence only; field names, units, and storage should be added after tracing the reader or finding a scenario that activates the file.

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: not found as a direct default filename in the source inventory.
- Candidate reader/source files: `SWATPLUS/swatplus/src/cs_hru_read.f90`.

## Downstream Consumers

Optional constituent and salt initialization or composition workflows.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `fixed-name/conditional`.
- Activation evidence: fixed-name or derived reader.
- Local file evidence: `VSProj/SWAT/Osu_1hru/cs_hru.ini`.

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
