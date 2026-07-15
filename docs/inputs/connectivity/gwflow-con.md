---
title: gwflow.con input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `gwflow.con`

## Purpose

Input file for connect; source slot gwflow_con.


## Official SWAT+ Reference

- Official page: ['object'.con](https://swatplus.gitbook.io/io-docs/introduction-1/connectivity/hru.con).
- Official index note: This file defines the connectivity of spatial objects.
- Official field metadata available: 17 field row(s); matched to 0 of 0 observed demo header field(s).

## Role In SWAT+

- Category: Connectivity.
- Usage class: `conditional input`.
- Activation: module switch, object count, or inactive `file.cio` slot.
- `Osu_1hru` status: `inactive/null`.
- Source inventory slot(s): `in_con%gwflow_con = "gwflow.con"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence: the `Osu_1hru` scenario does not include a concrete `gwflow.con` file, or the file family is inactive there. Use another scenario or the reader routine for field-level confirmation.

## Fields And Parameters

No local demo header is available, but the official SWAT+ page provides field metadata. Demo value cells are therefore blank until an active scenario file is added.

| Field | Meaning | Type | Unit | Default | Range |
| --- | --- | --- | --- | --- | --- |
| `id` | Unique ID of the object. | - | - | - | - |
| `name` | Name of the object. | - | - | - | - |
| `gis_id` | Object ID in QSWAT+. | - | - | - | - |
| `area` | Area of the object. | - | - | - | - |
| `lat` | Latitude of the object. | - | - | - | - |
| `lon` | Longitude of the object. | - | - | - | - |
| `elev` | Elevation of the object. | - | - | - | - |
| `'obj'` | Pointer to the object data file. | - | - | - | - |
| `wst` | Pointer to the weather station file. | - | - | - | - |
| `cst` | Pointer to the constituent file. | - | - | - | - |
| `ovfl` | Pointer to the overbank flooding file. | - | - | - | - |
| `rule` | Pointer to the decision table for hydrograph fractions. | - | - | - | - |
| `out_tot` | Total number of outgoing hydrographs. | - | - | - | - |
| `obj_typ` | Type of the receiving object. | - | - | - | - |
| `obj_id` | ID of the receiving object. | - | - | - | - |
| `hyd_typ` | Type of hydrograph that is sent to the receiving object. | - | - | - | - |
| `frac` | Fraction of hydrograph sent to the receiving object. | - | - | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_con%gwflow_con` defaulting to `gwflow.con`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/basin_read_objs.f90`, `SWATPLUS/swatplus/src/hyd_connect.f90`.

## Downstream Consumers

Object routing and connection setup for moving water and constituent loads between SWAT+ objects.

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
