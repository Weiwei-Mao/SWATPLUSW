---
title: channel-lte.cha input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `channel-lte.cha`

## Purpose

SWAT-DEG channel definition file; describes detailed channel objects used by `sdc` / `chandeg`.


## Official SWAT+ Reference

- Official page: [channel-lte.cha](https://swatplus.gitbook.io/io-docs/introduction-1/channels/channel-lte.cha).
- Official index note: This file summarizes the main channel information and references several other files that specify the details.
- Official field metadata available: 5 field row(s); matched to 2 of 6 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Channels.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cha%chan_ez = "channel-lte.cha"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/channel-lte.cha`:

- Title/comment line: `channel-lte.cha: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `id  name                       cha_ini           cha_hyd           cha_sed           cha_nut`.
- Nonblank records after the header: 57.
- First demo data record: `1  cha01                     initcha1          hydcha01              null           nutcha1`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | ID of the channel. | - | - | - | - | `1` | official GitBook |
| `name` | Name of the channel. | - | - | - | - | `cha01` | official GitBook |
| `cha_ini` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `initcha1` | demo/source inferred |
| `cha_hyd` | Hydrology-related parameter or record reference. | - | - | - | - | `hydcha01` | demo/source inferred |
| `cha_sed` | Sediment-related parameter or state value. | - | - | - | - | `null` | demo/source inferred |
| `cha_nut` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `nutcha1` | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `ini` | Pointer to the channel initialization file. | - | - |
| `hyd` | Pointer to the channel hydrology and sediment file. | - | - |
| `nut` | Pointer to the channel nutrient file. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cha%chan_ez` defaulting to `channel-lte.cha`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/sd_channel_read.f90`.

## Downstream Consumers

Channel or SWAT-DEG channel hydrology, sediment, nutrient, and initialization routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/channel-lte.cha`.

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
