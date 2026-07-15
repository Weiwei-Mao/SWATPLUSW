---
title: sediment.res input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `sediment.res`

## Purpose

Reservoir sediment parameter database.


## Official SWAT+ Reference

- Official page: [sediment.res](https://swatplus.gitbook.io/io-docs/introduction-1/reservoirs/sediment.res).
- Official index note: This file contains the reservoir and wetland sediment parameters.
- Official field metadata available: 7 field row(s); matched to 6 of 7 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Reservoirs Wetlands.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_res%sed_res = "sediment.res"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/sediment.res`:

- Title/comment line: `sediment.res: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                   sed_amt           d50        carbon            bd       sed_stl       stl_vel`.
- Nonblank records after the header: 1.
- First demo data record: `sedwet1                  10.00           5.00       0.04            0.8          0.15       0.0002`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the reservoir and wetland sediment record. | - | - | - | - | `sedwet1` | official GitBook |
| `sed_amt` | Sediment-related parameter or state value. | - | - | - | - | `10.00` | demo/source inferred |
| `d50` | Median particle size of suspended and benthic sediment. | - | - | - | - | `5.00` | official GitBook |
| `carbon` | Organic carbon in suspended and benthic sediment. | - | - | - | - | `0.04` | official GitBook |
| `bd` | Bulk density of benthic sediment. | - | - | - | - | `0.8` | official GitBook |
| `sed_stl` | Sediment settling rate. | - | - | - | - | `0.15` | official GitBook |
| `stl_vel` | Sediment settling velocity. | - | - | - | - | `0.0002` | official GitBook |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `nsed` | Equilibrium sediment concentration in the reservoir. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_res%sed_res` defaulting to `sediment.res`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/res_read_sed.f90`.

## Downstream Consumers

Reservoir, pond, and wetland hydrology, release, sediment, and nutrient routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/sediment.res`.

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
