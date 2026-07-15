---
title: snow.sno input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `snow.sno`

## Purpose

Snow parameter database.


## Official SWAT+ Reference

- Official page: [snow.sno](https://swatplus.gitbook.io/io-docs/introduction-1/hydrology/snow.sno).
- Official index note: This file controls the simulation of snowfall and snowmelt processes.
- Official field metadata available: 9 field row(s); matched to 9 of 9 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Databases.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_parmdb%snow = "snow.sno"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/snow.sno`:

- Title/comment line: `snow.sno: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                  fall_tmp      melt_tmp      melt_max      melt_min       tmp_lag      snow_h2o         cov50     snow_init`.
- Nonblank records after the header: 1.
- First demo data record: `snow001                1.00000       0.50000       4.50000       4.50000       1.00000       1.00000       0.50000       0.00000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the snow record. | - | - | - | - | `snow001` | official GitBook |
| `fall_tmp` | Snowfall temperature. | - | - | - | - | `1.00000` | official GitBook |
| `melt_tmp` | Snow melt base temperature. | - | - | - | - | `0.50000` | official GitBook |
| `melt_max` | Melt factor for snow on June 21. | - | - | - | - | `4.50000` | official GitBook |
| `melt_min` | Melt factor for snow on December 21. | - | - | - | - | `4.50000` | official GitBook |
| `tmp_lag` | Snowpack temperature lag factor. | - | - | - | - | `1.00000` | official GitBook |
| `snow_h2o` | Minimum snow water content that corresponds to 100% snow cover. | - | - | - | - | `1.00000` | official GitBook |
| `cov50` | Fraction of snow volume corresponding to 50% snow cover. | - | - | - | - | `0.50000` | official GitBook |
| `snow_init` | Initial snow water content at start of simulation. | - | - | - | - | `0.00000` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_parmdb%snow` defaulting to `snow.sno`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/snowdb_read.f90`.

## Downstream Consumers

Reusable parameter databases referenced by management, land-use, constituent, and operation records.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/snow.sno`.

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
