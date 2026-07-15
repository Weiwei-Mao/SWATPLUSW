---
title: water_allocation.wro input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `water_allocation.wro`

## Purpose

Input file for water-rights; source slot transfer_wro.


## Official SWAT+ Reference

- Official page: [water_allocation.wro](https://swatplus.gitbook.io/io-docs/introduction-1/water-allocation/water_allocation.wro).
- Official index note: This file contains water allocation tables.
- Official field metadata available: 21 field row(s); matched to 0 of 0 observed demo header field(s).

## Role In SWAT+

- Category: Water Allocation.
- Usage class: `conditional input`.
- Activation: module switch, object count, or inactive `file.cio` slot.
- `Osu_1hru` status: `inactive/null`.
- Source inventory slot(s): `in_watrts%transfer_wro = "water_allocation.wro"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence: the `Osu_1hru` scenario does not include a concrete `water_allocation.wro` file, or the file family is inactive there. Use another scenario or the reader routine for field-level confirmation.

## Fields And Parameters

No local demo header is available, but the official SWAT+ page provides field metadata. Demo value cells are therefore blank until an active scenario file is added.

| Field | Meaning | Type | Unit | Default | Range |
| --- | --- | --- | --- | --- | --- |
| `name` | Name of the water allocation table. | `string` | - | - | - |
| `rule_typ` | Rule type to allocate water. | `string` | - | - | - |
| `src_obs` | Number of source objects. | `integer` | - | - | - |
| `dmd_obs` | Number of demand objects. | `integer` | - | - | - |
| `cha_ob` | Channel as source object. | `string` | - | - | - |
| `num` | Source object number. | `integer` | - | - | - |
| `ob_typ` | Object type of the source object. | `string` | - | - | - |
| `ob_num` | ID of the source object. | `integer` | - | - | - |
| `limit_mon` | Monthly limits. | `real` | - | - | - |
| `withdr` | Withdrawal type. | `string` | - | - | - |
| `amount` | Withdrawal amount. | `real` | - | - | - |
| `right` | Water right. | `string` | - | - | - |
| `treat_typ` | Currently not functional. | `string` | - | - | - |
| `treatment` | Currently not functional. | `string` | - | - | - |
| `rcv_ob` | Object type of the receiving object. | `string` | - | - | - |
| `rcv_num` | ID of the receiving object. | `integer` | - | - | - |
| `rcv_dtl` | Currently not used. | `string` | - | - | - |
| `srcs` | Number of source objects available for the demand object. | `integer` | - | - | - |
| `src` | Source object ID. | `integer` | - | - | - |
| `frac` | Fraction of demand to be met by source object. | `real` | - | - | - |
| `comp` | Compensation from source object. | `string` | - | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_watrts%transfer_wro` defaulting to `water_allocation.wro`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/water_allocation_read.f90`.

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
