---
title: urban.urb input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `urban.urb`

## Purpose

Urban land-use parameter database.


## Official SWAT+ Reference

- Official page: [urban.urb](https://swatplus.gitbook.io/io-docs/introduction-1/databases/urban.urb).
- Official index note: The urban database summarizes parameters used by the model to simulate different types of urban areas.
- Official field metadata available: 11 field row(s); matched to 10 of 12 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Databases.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_parmdb%urban_urb = "urban.urb"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/urban.urb`:

- Title/comment line: `urban.urb: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                  frac_imp   frac_dc_imp      curb_den      urb_wash      dirt_max     t_halfmax     conc_totn     conc_totp     conc_no3n        urb_cn  description`.
- Nonblank records after the header: 9.
- First demo data record: `urhd                   0.60000       0.44000       0.24000       0.18000     225.00000       0.75000     550.00000     223.00000       7.20000      98.00000  Residential-High Density`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the urban land type. | - | - | - | - | `urhd` | official GitBook |
| `frac_imp` | Fraction of total impervious area in urban land type. | - | - | - | - | `0.60000` | official GitBook |
| `frac_dc_imp` | Fraction of directly connected impervious area in urban land type. | - | - | - | - | `0.44000` | official GitBook |
| `curb_den` | Curb length density. | - | - | - | - | `0.24000` | official GitBook |
| `urb_wash` | Wash-off coefficient for removal of constituents from impervious surfaces. | - | - | - | - | `0.18000` | official GitBook |
| `dirt_max` | Maximum amount of solids allowed to build up on impervious surfaces. | - | - | - | - | `225.00000` | official GitBook |
| `t_halfmax` | Time for amount of solids on impervious areas to build up to 1/2 of maximum level. | - | - | - | - | `0.75000` | official GitBook |
| `conc_totn` | Concentration of total N in suspended solid load from impervious areas. | - | - | - | - | `550.00000` | official GitBook |
| `conc_totp` | Concentration of total P in suspended solid load from impervious areas. | - | - | - | - | `223.00000` | official GitBook |
| `conc_no3n` | Nitrate-nitrogen value; verify storage and units in the reader. | - | - | - | - | `7.20000` | demo/source inferred |
| `urb_cn` | Moisture condition II curve number for impermeable areas. | - | - | - | - | `98.00000` | official GitBook |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `Residential-High` | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `conc_no3` | Concentration of NO3-N in suspended solid load from impervious areas. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_parmdb%urban_urb` defaulting to `urban.urb`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/urban_parm_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/urban.urb`.

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
