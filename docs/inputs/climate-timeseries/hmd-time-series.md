---
title: "*.hmd input file"
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `*.hmd`

## Purpose

Relative-humidity time-series file named by a humidity gauge manifest.

## Role In SWAT+

- Category: Climate Timeseries.
- Usage class: `indirect input`.
- Activation: manifest file when `hmd.cli` is active.
- `Osu_1hru` status: `inactive/null`.
- Source inventory: indirect file family, resolved through a manifest rather than a fixed `input_file_module.f90` slot.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file family is not normally listed directly in `file.cio`. It is reached through a manifest, for example a climate `*.cli` file that names the time-series data file.

Local demo evidence: the `Osu_1hru` scenario does not include a concrete `*.hmd` file, or the file family is inactive there. Use another scenario or the reader routine for field-level confirmation.

## Fields And Parameters

No local demo header is available for this file. The page currently documents role, activation, and source inventory only; field names, units, and storage should be added after tracing the reader or adding an active demo file.

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: not found as a direct default filename in the source inventory.
- Candidate reader/source files: not found by a simple source-slot or literal-filename search; use `rg` from the source inventory slot, parent module, or filename stem as the next tracing step.

## Downstream Consumers

Climate station assignment and daily/subdaily weather forcing used by hydrology and plant-growth routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `inactive/null`.
- Activation evidence: manifest file when `hmd.cli` is active.
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
- [Climate manifest files](../climate/pcp-cli.md)
- [Master input manifest](../simulation/file-cio.md)
