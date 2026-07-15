---
title: hydrology.hyd input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `hydrology.hyd`

## Purpose

HRU hydrology parameter database, including ET, lateral flow, percolation, and related coefficients.


## Official SWAT+ Reference

- Official page: [hydrology.hyd](https://swatplus.gitbook.io/io-docs/introduction-1/hydrology/hydrology.hyd).
- Official index note: This file defines the hydrological characteristics of the HRUs.
- Official field metadata available: 15 field row(s); matched to 13 of 15 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Hydrology.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_hyd%hydrol_hyd = "hydrology.hyd"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/hydrology.hyd`:

- Title/comment line: `hydrology.hyd: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                 lat_ttime       lat_sed       can_max          esco          epco   orgn_enrich   orgp_enrich       cn3_swf       bio_mix         perco      lat_orgn      lat_orgp      harg_pet       latq_co`.
- Nonblank records after the header: 1.
- First demo data record: `hyd0001                0.00000       0.00000       1.00000       0.95000       0.50000       0.00000       0.00000       0.95000       0.20000       0.90000       0.00000       0.00000       0.00000       0.01000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the hydrology record. | `string` | `n/a` | `n/a` | `n/a` | `hyd0001` | official GitBook |
| `lat_ttime` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.00000` | demo/source inferred |
| `lat_sed` | Sediment concentration in lateral and groundwater flow. | `real` | `mg/L` | `0` | `0-5000` | `0.00000` | official GitBook |
| `can_max` | Maximum canopy storage. | `real` | `mm` | `1` | `0-100` | `1.00000` | official GitBook |
| `esco` | Soil evaporation compensation factor. | `real` | `none` | `0.5` | `0.01-1` | `0.95000` | official GitBook |
| `epco` | Plant uptake compensation factor. | `real` | `none` | `0` | `0.01-1` | `0.50000` | official GitBook |
| `orgn_enrich` | Organic nitrogen enrichment ratio for loading with sediment. | `real` | `none` | `0` | `0-1` | `0.00000` | official GitBook |
| `orgp_enrich` | Phosphorus enrichment ratio for loading with sediment. | `real` | `none` | `0` | `0-1` | `0.00000` | official GitBook |
| `cn3_swf` | Soil water adjustment factor for CN3. | `real` | `none` | - | `0-1` | `0.95000` | official GitBook |
| `bio_mix` | Biological mixing efficiency. | `real` | - | `0.2` | - | `0.20000` | official GitBook |
| `perco` | Percolation coefficient. | `real` | `none` | - | `0-1` | `0.90000` | official GitBook |
| `lat_orgn` | Organic nitrogen concentration in lateral flow. | `real` | `mg/L` | - | `0-200` | `0.00000` | official GitBook |
| `lat_orgp` | Organic phosphorus concentration in lateral flow. | `real` | `mg/L` | - | `0-200` | `0.00000` | official GitBook |
| `harg_pet` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.00000` | demo/source inferred |
| `latq_co` | Lateral flow coefficient. | `real` | `none` | - | `0-1` | `0.01000` | official GitBook |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `lat_time` | Lateral flow travel time. | `real` | `days` |
| `pet_co` | Linear adjustment factor for PET equations. | `real` | `none` |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_hyd%hydrol_hyd` defaulting to `hydrology.hyd`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/hydrol_read.f90`.

## Downstream Consumers

Land-phase hydrology, topography, field geometry, and runoff/infiltration calculations.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/hydrology.hyd`.

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
