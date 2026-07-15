---
title: hru.con input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `hru.con`

## Purpose

Connection definition for full HRU objects. In QSWAT-style routing, HRUs may have no direct output and are wrapped by routing units.

## Role In SWAT+

- Category: Connectivity.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_con%hru_con = "hru.con"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/hru.con`:

- Title/comment line: `hru.con: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `id  name                gis_id          area           lat           lon          elev       hru               wst       cst      ovfl      rule   out_tot`.
- Nonblank records after the header: 1.
- First demo data record: `1  hru0001                  1           10       35.65311     127.36763     350.96629         1    s35610n127290e         0         0         0         0`.

## Fields And Parameters

The table below is generated from the demo header. Meanings are practical working descriptions from the header name, local scenario context, and SWAT+ conventions; verify units and storage against the reader before citing them as final.

| Field | Working meaning | Demo value |
| --- | --- | --- |
| `id` | Numeric record identifier. | `1` |
| `name` | Record name used by other input files to reference this parameter set. | `hru0001` |
| `gis_id` | GIS/source-project identifier retained for the object. | `1` |
| `area` | Area represented by the object or record. | `10` |
| `lat` | Latitude of the station or object. | `35.65311` |
| `lon` | Longitude of the station or object. | `127.36763` |
| `elev` | Elevation of the station or object. | `350.96629` |
| `hru` | HRU-related parameter or object reference. | `1` |
| `wst` | Field named in the demo/source header; trace the reader for exact units and storage. | `s35610n127290e` |
| `cst` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `ovfl` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `rule` | Field named in the demo/source header; trace the reader for exact units and storage. | `0` |
| `out_tot` | Number of output or receiving commands listed for the object. | `0` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_con%hru_con` defaulting to `hru.con`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/hyd_connect.f90`, `SWATPLUS/swatplus/src/swift_output.f90`.

## Downstream Consumers

Object routing and connection setup for moving water and constituent loads between SWAT+ objects.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/hru.con`.

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
