---
title: rout_unit.con input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `rout_unit.con`

## Purpose

Routing-unit connection file; defines where routing-unit hydrographs go.


## Official SWAT+ Reference

- Official page: ['object'.con](https://swatplus.gitbook.io/io-docs/introduction-1/connectivity/hru.con).
- Official index note: This file defines the connectivity of spatial objects.
- Official field metadata available: 17 field row(s); matched to 16 of 17 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Connectivity.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_con%ru_con = "rout_unit.con"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/rout_unit.con`:

- Title/comment line: `rout_unit.con: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `id  name                gis_id          area           lat           lon          elev       rtu               wst       cst      ovfl      rule   out_tot       obj_typ    obj_id       hyd_typ          frac`.
- Nonblank records after the header: 1.
- First demo data record: `1  rtu001                   1       10.0000      35.52014     127.32787     113.51276         1    s35610n127290e         0         0         0         2           sdc         1           tot       1.00000           aqu         1           rhg       1.00000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | Unique ID of the object. | - | - | - | - | `1` | official GitBook |
| `name` | Name of the object. | - | - | - | - | `rtu001` | official GitBook |
| `gis_id` | Object ID in QSWAT+. | - | - | - | - | `1` | official GitBook |
| `area` | Area of the object. | - | - | - | - | `10.0000` | official GitBook |
| `lat` | Latitude of the object. | - | - | - | - | `35.52014` | official GitBook |
| `lon` | Longitude of the object. | - | - | - | - | `127.32787` | official GitBook |
| `elev` | Elevation of the object. | - | - | - | - | `113.51276` | official GitBook |
| `rtu` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1` | demo/source inferred |
| `wst` | Pointer to the weather station file. | - | - | - | - | `s35610n127290e` | official GitBook |
| `cst` | Pointer to the constituent file. | - | - | - | - | `0` | official GitBook |
| `ovfl` | Pointer to the overbank flooding file. | - | - | - | - | `0` | official GitBook |
| `rule` | Pointer to the decision table for hydrograph fractions. | - | - | - | - | `0` | official GitBook |
| `out_tot` | Total number of outgoing hydrographs. | - | - | - | - | `2` | official GitBook |
| `obj_typ` | Type of the receiving object. | - | - | - | - | `sdc` | official GitBook |
| `obj_id` | ID of the receiving object. | - | - | - | - | `1` | official GitBook |
| `hyd_typ` | Type of hydrograph that is sent to the receiving object. | - | - | - | - | `tot` | official GitBook |
| `frac` | Fraction of hydrograph sent to the receiving object. | - | - | - | - | `1.00000` | official GitBook |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `'obj'` | Pointer to the object data file. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_con%ru_con` defaulting to `rout_unit.con`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/hyd_connect.f90`, `SWATPLUS/swatplus/src/swift_output.f90`.

## Downstream Consumers

Object routing and connection setup for moving water and constituent loads between SWAT+ objects.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/rout_unit.con`.

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
