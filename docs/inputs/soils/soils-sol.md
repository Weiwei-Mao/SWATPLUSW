---
title: soils.sol input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `soils.sol`

## Purpose

Soil profile database for full HRUs.


## Official SWAT+ Reference

- Official page: [soils.sol](https://swatplus.gitbook.io/io-docs/introduction-1/soils/soils.sol).
- Official index note: This file contains the physical soil properties.
- Official field metadata available: 19 field row(s); matched to 19 of 21 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Soils.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_sol%soils_sol = "soils.sol"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/soils.sol`:

- Title/comment line: `soils.sol: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                            nly           hyd_grp        dp_tot    anion_excl      perc_crk  texture                              dp            bd           awc        soil_k        carbon          clay          silt          sand          rock           alb        usle_k            ec         caco3            ph`.
- Nonblank records after the header: 501.
- First demo data record: `SONGSAN                           5                 A    1200.00000       0.50000       0.50000  LS`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the soil. | - | - | - | - | `SONGSAN` | official GitBook |
| `nly` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `5` | demo/source inferred |
| `hyd_grp` | Hydrologic soil group of the soil. | - | - | - | - | `A` | official GitBook |
| `dp_tot` | Maximum rooting depth. | - | - | - | - | `1200.00000` | official GitBook |
| `anion_excl` | Fraction of porosity (void space) from which anions are excluded. | - | - | - | - | `0.50000` | official GitBook |
| `perc_crk` | Potential or maximum crack volume of the soil profile expressed as a fraction of the total soil volume. | - | - | - | - | `0.50000` | official GitBook |
| `texture` | Texture of the soil layer. | - | - | - | - | `LS` | official GitBook |
| `dp` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | - | demo/source inferred |
| `bd` | Moist bulk density of the soil layer. | - | - | - | - | - | official GitBook |
| `awc` | Available water capacity of the soil layer. | - | - | - | - | - | official GitBook |
| `soil_k` | Saturated hydraulic conductivity of the soil layer. | - | - | - | - | - | official GitBook |
| `carbon` | Organic carbon content of the soil layer. | - | - | - | - | - | official GitBook |
| `clay` | Clay content of the soil layer. | - | - | - | - | - | official GitBook |
| `silt` | Silt content of the soil layer. | - | - | - | - | - | official GitBook |
| `sand` | Sand content of the soil layer. | - | - | - | - | - | official GitBook |
| `rock` | Rock fragment content of the soil layer. | - | - | - | - | - | official GitBook |
| `alb` | Moist soil albedo of the top layer. | - | - | - | - | - | official GitBook |
| `usle_k` | USLE equation soil erodibility (K) factor of the top layer. | - | - | - | - | - | official GitBook |
| `ec` | Electrical conductivity of the soil layer. | - | - | - | - | - | official GitBook |
| `caco3` | Calcium carbonate (CaCO3) content of the soil layer. | - | - | - | - | - | official GitBook |
| `ph` | pH value of the soil layer. | - | - | - | - | - | official GitBook |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_sol%soils_sol` defaulting to `soils.sol`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/soil_db_read.f90`.

## Downstream Consumers

Soil profile, soil nutrient pools, and soil-layer calculations.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/soils.sol`.

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
