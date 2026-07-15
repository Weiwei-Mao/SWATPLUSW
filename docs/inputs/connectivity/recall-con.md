---
title: recall.con input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `recall.con`

## Purpose

Recall-object connection file; defines routing for external time-series hydrographs.


## Official SWAT+ Reference

- Official page: ['object'.con](https://swatplus.gitbook.io/io-docs/introduction-1/connectivity/hru.con).
- Official index note: This file defines the connectivity of spatial objects.
- Official field metadata available: 17 field row(s); matched to 6 of 17 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Connectivity.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_con%rec_con = "recall.con"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/recall.con`:

- Title/comment line: `recall.con (2-stage)`.
- Observed header line: `NUMB    NAME    GIS_ID    AREA_HA      LAT     LONG       ELEV    RECALL     WST   CONSTIT  OVERFLOW  RULESET OUT_TOT OBTYP_OUT1 HTYPNO_OUT1  HTYP_OUT1  FRAC_OUT1`.
- Nonblank records after the header: 1.
- First demo data record: `1  inflow      1        0.000    31.734   -83.720     0.000      1    wea1         0         0        0       1         sdc          1        tot     1.0000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `NUMB` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1` | demo/source inferred |
| `NAME` | Name of the object. | - | - | - | - | `inflow` | official GitBook |
| `GIS_ID` | Object ID in QSWAT+. | - | - | - | - | `1` | official GitBook |
| `AREA_HA` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.000` | demo/source inferred |
| `LAT` | Latitude of the object. | - | - | - | - | `31.734` | official GitBook |
| `LONG` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `-83.720` | demo/source inferred |
| `ELEV` | Elevation of the object. | - | - | - | - | `0.000` | official GitBook |
| `RECALL` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1` | demo/source inferred |
| `WST` | Pointer to the weather station file. | - | - | - | - | `wea1` | official GitBook |
| `CONSTIT` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `OVERFLOW` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `RULESET` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0` | demo/source inferred |
| `OUT_TOT` | Total number of outgoing hydrographs. | - | - | - | - | `1` | official GitBook |
| `OBTYP_OUT1` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `sdc` | demo/source inferred |
| `HTYPNO_OUT1` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1` | demo/source inferred |
| `HTYP_OUT1` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `tot` | demo/source inferred |
| `FRAC_OUT1` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `1.0000` | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `id` | Unique ID of the object. | - | - |
| `area` | Area of the object. | - | - |
| `lon` | Longitude of the object. | - | - |
| `'obj'` | Pointer to the object data file. | - | - |
| `cst` | Pointer to the constituent file. | - | - |
| `ovfl` | Pointer to the overbank flooding file. | - | - |
| `rule` | Pointer to the decision table for hydrograph fractions. | - | - |
| `obj_typ` | Type of the receiving object. | - | - |
| `obj_id` | ID of the receiving object. | - | - |
| `hyd_typ` | Type of hydrograph that is sent to the receiving object. | - | - |
| `frac` | Fraction of hydrograph sent to the receiving object. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_con%rec_con` defaulting to `recall.con`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/hyd_connect.f90`, `SWATPLUS/swatplus/src/swift_output.f90`.

## Downstream Consumers

Object routing and connection setup for moving water and constituent loads between SWAT+ objects.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/recall.con`.

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
