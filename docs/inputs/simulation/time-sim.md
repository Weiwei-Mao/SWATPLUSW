---
title: time.sim input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `time.sim`

## Purpose

Simulation dates, time step, and run period settings.


## Official SWAT+ Reference

- Official page: [time.sim](https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/time.sim).
- Official index note: This file controls the simulation time period and time step.
- Official field metadata available: 5 field row(s); matched to 5 of 5 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Simulation.
- Usage class: `core`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_sim%time = "time.sim"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/time.sim`:

- Title/comment line: `time.sim: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `day_start  yrc_start   day_end   yrc_end      step`.
- Nonblank records after the header: 1.
- First demo data record: `1      2010      365       2023         0`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `day_start` | Beginning day of the simulation. | - | - | - | - | `1` | official GitBook |
| `yrc_start` | Beginning year of the simulation. | - | - | - | - | `2010` | official GitBook |
| `day_end` | Ending day of the simulation. | - | - | - | - | `365` | official GitBook |
| `yrc_end` | Ending year of the simulation. | - | - | - | - | `2023` | official GitBook |
| `step` | Time step of the simulation. | - | - | - | - | `0` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_sim%time` defaulting to `time.sim`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/time_read.f90`.

## Downstream Consumers

Simulation setup, print controls, object allocation, or global runtime switches.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/time.sim`.

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
