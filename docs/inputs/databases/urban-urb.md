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

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `name` | Record name used by other input files to reference this parameter set. | `urhd` |
| `frac_imp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.60000` |
| `frac_dc_imp` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.44000` |
| `curb_den` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.24000` |
| `urb_wash` | Field named in the demo/source header; trace the reader for exact units and storage. | `0.18000` |
| `dirt_max` | Maximum value or upper bound, depending on the reader. | `225.00000` |
| `t_halfmax` | Maximum value or upper bound, depending on the reader. | `0.75000` |
| `conc_totn` | Concentration value; verify constituent and units in the reader. | `550.00000` |
| `conc_totp` | Concentration value; verify constituent and units in the reader. | `223.00000` |
| `conc_no3n` | Nitrate-nitrogen concentration, mass, or parameter component; verify units in the reader. | `7.20000` |
| `urb_cn` | Curve-number or conservation-practice related value; verify in reader. | `98.00000` |
| `description` | Free-text description retained for reader/user context. | `Residential-High` |

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
