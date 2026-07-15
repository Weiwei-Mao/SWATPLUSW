---
title: rout_unit.ele input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `rout_unit.ele`

## Purpose

Defines routing-unit member elements, such as HRUs, HRU-LTEs, or other spatial elements.


## Official SWAT+ Reference

- Official page: [rout_unit.ele](https://swatplus.gitbook.io/io-docs/introduction-1/routing-units/untitled-2).
- Official index note: This file lists all elements that are part of a Routing Unit.
- Official field metadata available: 6 field row(s); matched to 6 of 6 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Routing Units.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_ru%ru_ele = "rout_unit.ele"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/rout_unit.ele`:

- Title/comment line: `rout_unit.ele: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `id  name                   obj_typ    obj_id          frac               dlr`.
- Nonblank records after the header: 1.
- First demo data record: `1  hru0001                    hru         1            1                 0`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | ID of the element. | `integer` | - | - | - | `1` | official GitBook |
| `name` | Name of the element. | `string` | - | - | - | `hru0001` | official GitBook |
| `obj_typ` | Object type of the element. | `string` | - | - | - | `hru` | official GitBook |
| `obj_id` | Object ID of the element. | `integer` | - | - | - | `1` | official GitBook |
| `frac` | Fraction/ expansion factor of element in Routing Unit. | `real` | - | - | - | `1` | official GitBook |
| `dlr` | Currently not used. | `real` | - | - | - | `0` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_ru%ru_ele` defaulting to `rout_unit.ele`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/ru_read_elements.f90`, `SWATPLUS/swatplus/src/swift_output.f90`.

## Downstream Consumers

Routing-unit membership, parameterization, and delivery-ratio routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/rout_unit.ele`.

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
