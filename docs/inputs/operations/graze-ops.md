---
title: graze.ops input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `graze.ops`

## Purpose

Grazing operation definitions.


## Official SWAT+ Reference

- Official page: [graze.ops](https://swatplus.gitbook.io/io-docs/introduction-1/management-practices/graze.ops).
- Official index note: This file contains pre-defined grazing operations.
- Official field metadata available: 6 field row(s); matched to 5 of 7 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Operations.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_ops%graze_ops = "graze.ops"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/graze.ops`:

- Title/comment line: `graze.ops: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                          fert        bm_eat      bm_tramp       man_amt    grz_bm_min  description`.
- Nonblank records after the header: 12.
- First demo data record: `dairy_high                dairy_fr      25.00000      10.00000       0.95000    3000.00000  High_Prod_Dairy-Fresh_Manure`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Grazing operation name. | - | - | - | - | `dairy_high` | official GitBook |
| `fert` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `dairy_fr` | demo/source inferred |
| `bm_eat` | Dry weight of biomass removed by grazing daily. | - | - | - | - | `25.00000` | official GitBook |
| `bm_tramp` | Dry weight of biomass removed by trampling daily. | - | - | - | - | `10.00000` | official GitBook |
| `man_amt` | Dry weight of manure deposited daily. | - | - | - | - | `0.95000` | official GitBook |
| `grz_bm_min` | Minimum plant biomass for grazing to occur. | - | - | - | - | `3000.00000` | official GitBook |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `High_Prod_Dairy-Fresh_Manure` | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `fertname` | Fertilizer name for manure deposited during grazing. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_ops%graze_ops` defaulting to `graze.ops`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/mgt_read_grazeops.f90`.

## Downstream Consumers

Scheduled management-operation routines such as planting, harvest, grazing, irrigation, fire, and treatment.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/graze.ops`.

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
