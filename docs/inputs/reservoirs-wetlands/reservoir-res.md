---
title: reservoir.res input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `reservoir.res`

## Purpose

Input file for reservoir; source slot res.


## Official SWAT+ Reference

- Official page: [reservoir.res](https://swatplus.gitbook.io/io-docs/introduction-1/reservoirs/reservoir.res).
- Official index note: This file contains pointers referencing several files that specify the reservoir properties.
- Official field metadata available: 7 field row(s); matched to 0 of 0 observed demo header field(s).

## Role In SWAT+

- Category: Reservoirs Wetlands.
- Usage class: `optional/default`.
- Activation: source default or inactive `file.cio` slot.
- `Osu_1hru` status: `inactive/null`.
- Source inventory slot(s): `in_res%res = "reservoir.res"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence: the `Osu_1hru` scenario does not include a concrete `reservoir.res` file, or the file family is inactive there. Use another scenario or the reader routine for field-level confirmation.

## Fields And Parameters

No local demo header is available, but the official SWAT+ page provides field metadata. Demo value cells are therefore blank until an active scenario file is added.

| Field | Meaning | Type | Unit | Default | Range |
| --- | --- | --- | --- | --- | --- |
| `id` | ID of the reservoir. | - | - | - | - |
| `name` | Name of the reservoir. | - | - | - | - |
| `init` | Pointer to the reservoir and wetland initialization file. | - | - | - | - |
| `hyd` | Pointer to the reservoir hydrology file. | - | - | - | - |
| `rel` | Pointer to the reservoir and wetland release decision table file. | - | - | - | - |
| `sed` | Pointer to the reservoir and wetland sediment file. | - | - | - | - |
| `nut` | Pointer to the reservoir and wetland nutrient file. | - | - | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_res%res` defaulting to `reservoir.res`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/res_read.f90`.

## Downstream Consumers

Reservoir, pond, and wetland hydrology, release, sediment, and nutrient routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `inactive/null`.
- Activation evidence: source default or inactive `file.cio` slot.
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
