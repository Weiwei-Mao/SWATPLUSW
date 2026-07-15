---
title: object.prt input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `object.prt`

## Purpose

Input file for simulation; source slot object_prt.


## Official SWAT+ Reference

- Official page: [object.prt](https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/object.prt).
- Official index note: This file allows the user to print selected output for individual spatial objects.
- Official field metadata available: 3 field row(s); matched to 0 of 0 observed demo header field(s).

## Role In SWAT+

- Category: Simulation.
- Usage class: `conditional input`.
- Activation: module switch, object count, or inactive `file.cio` slot.
- `Osu_1hru` status: `inactive/null`.
- Source inventory slot(s): `in_sim%object_prt = "object.prt"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence: the `Osu_1hru` scenario does not include a concrete `object.prt` file, or the file family is inactive there. Use another scenario or the reader routine for field-level confirmation.

## Fields And Parameters

No local demo header is available, but the official SWAT+ page provides field metadata. Demo value cells are therefore blank until an active scenario file is added.

| Field | Meaning | Type | Unit | Default | Range |
| --- | --- | --- | --- | --- | --- |
| `obj_typ` | Type of object to print output for. | - | - | - | - |
| `obj_typ_no` | Number of the object to print output for. | - | - | - | - |
| `hyd_typ` | Type of hydrograph to print. | - | - | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_sim%object_prt` defaulting to `object.prt`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/object_read_output.f90`, `SWATPLUS/swatplus/src/swift_output.f90`.

## Downstream Consumers

Simulation setup, print controls, object allocation, or global runtime switches.

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
