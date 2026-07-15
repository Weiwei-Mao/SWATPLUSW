---
title: soil_plant.ini input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `soil_plant.ini`

## Purpose

Initial soil/plant nutrient, pesticide, pathogen, metal, salt, and constituent pointer records.


## Official SWAT+ Reference

- Official page: [soil_plant.ini](https://swatplus.gitbook.io/io-docs/introduction-1/initialization/soil_plant.ini).
- Official index note: This file references several other files, which initialize nutrients and constituents in soils.
- Official field metadata available: 5 field row(s); matched to 5 of 7 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Initialization.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_init%soil_plant_ini = "soil_plant.ini"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/soil_plant.ini`:

- Title/comment line: `soil_plant.ini: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                   sw_frac         nutrients              pest              path              hmet              salt`.
- Nonblank records after the header: 1.
- First demo data record: `soilplant1             0.00000          soilnut1              null              null              null              null`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the soil and plant initialization. | - | - | - | - | `soilplant1` | official GitBook |
| `sw_frac` | Soil water fraction at the beginning of the simulation. | - | - | - | - | `0.00000` | official GitBook |
| `nutrients` | Pointer to the nutrient initialization file. | - | - | - | - | `soilnut1` | official GitBook |
| `pest` | Pointer to the pesticide initialization file. | - | - | - | - | `null` | official GitBook |
| `path` | Pathogen or bacteria-related value or parameter. | - | - | - | - | `null` | demo/source inferred |
| `hmet` | Heavy-metal related value or parameter. | - | - | - | - | `null` | demo/source inferred |
| `salt` | Pointer to the salt initialization file. | - | - | - | - | `null` | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_init%soil_plant_ini` defaulting to `soil_plant.ini`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/soil_plant_init.f90`.

## Downstream Consumers

Initial condition assignment for plants, soil/plant pools, water bodies, and constituents.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/soil_plant.ini`.

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
