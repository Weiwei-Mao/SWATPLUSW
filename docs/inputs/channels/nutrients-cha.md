---
title: nutrients.cha input file
kind: input-reference
status: partial
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, reference, demo-context]
---

# `nutrients.cha`

## Purpose

Channel nutrient and water-quality parameter database.


## Official SWAT+ Reference

- Official page: [nutrients.cha](https://swatplus.gitbook.io/io-docs/introduction-1/channels/nutrients.cha).
- Official index note: This file controls the channel nutrient properties.
- Official field metadata available: 39 field row(s); matched to 38 of 40 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Role In SWAT+

- Category: Channels.
- Usage class: `active scenario input`.
- Activation: `file.cio`.
- `Osu_1hru` status: `active`.
- Source inventory slot(s): `in_cha%nut = "nutrients.cha"`.

## File Format

SWAT+ input files use a plain-text, free-format layout with space-delimited values. GitBook documents the general convention as a title line first, then usually a header line, with exceptions such as `file.cio` and files that add count or block-header lines.
This file is controlled by the master `file.cio` manifest in normal runs. A non-`null` entry activates the selected filename; `null` means the file slot is intentionally unused for that scenario.

Local demo evidence from `VSProj/SWAT/Osu_1hru/nutrients.cha`:

- Title/comment line: `nutrients.cha: written by SWAT+ editor v2.2.0 on 2023-03-22 04:25 for SWAT+ rev.60.5.4`.
- Observed header line: `name                     plt_n         ptl_p       alg_stl      ben_disp      ben_nh3n      ptln_stl      ptlp_stl       cst_stl       ben_cst    cbn_bod_co        air_rt   cbn_bod_stl       ben_bod      bact_die     cst_decay     nh3n_no2n     no2n_no3n     ptln_nh3n     ptlp_solp    q2e_lt   q2e_alg      chla_alg         alg_n         alg_p   alg_o2_prod   alg_o2_resp       o2_nh3n       o2_no2n      alg_grow      alg_resp       slr_act         lt_co       const_n       const_p     lt_nonalg     alg_shd_l    alg_shd_nl      nh3_pref  description`.
- Nonblank records after the header: 1.
- First demo data record: `nutcha1                0.00000       0.00000       1.00000       0.05000       0.50000       0.05000       0.05000       2.50000       2.50000       1.71000      50.00000       0.36000       2.00000       2.00000       1.71000       0.55000       1.10000       0.21000       0.35000         2         2      50.00000       0.08000       0.01500       1.60000       2.00000       3.50000       1.07000       2.00000       2.50000       0.30000       0.75000       0.02000       0.02500       1.00000       0.03000       0.05400       0.50000`.

## Fields And Parameters

The table merges the local demo header with official SWAT+ metadata when an official field definition is available. Rows marked `demo/source inferred` still need reader-level confirmation.

| Field | Meaning | Type | Unit | Default | Range | Demo value | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | Name of the channel nutrient record. | - | - | - | - | `nutcha1` | official GitBook |
| `plt_n` | Channel organic N concentration. | - | - | - | - | `0.00000` | official GitBook |
| `ptl_p` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | `0.00000` | demo/source inferred |
| `alg_stl` | Local algal settling rate in the channel at 20deg C. | - | - | - | - | `1.00000` | official GitBook |
| `ben_disp` | Benthic source rate for dissolved P in the channel at 20deg C. | - | - | - | - | `0.05000` | official GitBook |
| `ben_nh3n` | Benthic source rate for NH3-N in the channel at 20deg C. | - | - | - | - | `0.50000` | official GitBook |
| `ptln_stl` | Organic N settling rate in the channel at 20deg C. | - | - | - | - | `0.05000` | official GitBook |
| `ptlp_stl` | Organic P settling rate in the channel at 20deg C. | - | - | - | - | `0.05000` | official GitBook |
| `cst_stl` | Arbitrary non-conservative constituent settling rate in the channel at 20deg C. | - | - | - | - | `2.50000` | official GitBook |
| `ben_cst` | Benthic source rate for arbitrary non-conservative constituents in the channel at 20deg C. | - | - | - | - | `2.50000` | official GitBook |
| `cbn_bod_co` | Carbonaceous biological oxygen demand deoxygenation rate in the channel at 20deg C. | - | - | - | - | `1.71000` | official GitBook |
| `air_rt` | Reaeration rate in accordance with Fickian diffusion in the channel at 20deg C. | - | - | - | - | `50.00000` | official GitBook |
| `cbn_bod_stl` | Rate of loss of carbonaceous biological oxygen demand due to settling in the reach at 20 deg C. | - | - | - | - | `0.36000` | official GitBook |
| `ben_bod` | Benthic oxygen demand rate in the channel at 20deg C. | - | - | - | - | `2.00000` | official GitBook |
| `bact_die` | Coliform die-off rate in the reach at 20deg C. | - | - | - | - | `2.00000` | official GitBook |
| `cst_decay` | Decay rate for arbitrary non-conservative constituents in the channel at 20deg C. | - | - | - | - | `1.71000` | official GitBook |
| `nh3n_no2n` | Biological oxidation rate of NH3 to NO2 in the channel at 20deg C in well-aerated conditions. | - | - | - | - | `0.55000` | official GitBook |
| `no2n_no3n` | Biological oxidation rate of NO2 to NO3 in the channel at 20deg C in well-aerated conditions. | - | - | - | - | `1.10000` | official GitBook |
| `ptln_nh3n` | Hydrolysis rate of organic N to ammonia in the channel at 20deg C. | - | - | - | - | `0.21000` | official GitBook |
| `ptlp_solp` | Mineralization rate of organic P to dissolved P in the channel at 20deg C. | - | - | - | - | `0.35000` | official GitBook |
| `q2e_lt` | Qual2E light averaging option. | - | - | - | - | `2` | official GitBook |
| `q2e_alg` | Qual2E option for calculating the local specific growth rate of algae. | - | - | - | - | `2` | official GitBook |
| `chla_alg` | Ratio of chlorophyll-a to algal biomass. | - | - | - | - | `50.00000` | official GitBook |
| `alg_n` | Fraction of algal biomass that is N. | - | - | - | - | `0.08000` | official GitBook |
| `alg_p` | Fraction of algal biomass that is P. | - | - | - | - | `0.01500` | official GitBook |
| `alg_o2_prod` | Oxygen production rate per unit of algal photosynthesis. | - | - | - | - | `1.60000` | official GitBook |
| `alg_o2_resp` | Oxygen uptake rate per unit of algae respiration. | - | - | - | - | `2.00000` | official GitBook |
| `o2_nh3n` | Oxygen uptake rate per unit of NH3-N oxidation. | - | - | - | - | `3.50000` | official GitBook |
| `o2_no2n` | Oxygen uptake rate per unit of NO2-N oxidation. | - | - | - | - | `1.07000` | official GitBook |
| `alg_grow` | Maximum specific algal growth rate at 20deg C. | - | - | - | - | `2.00000` | official GitBook |
| `alg_resp` | Algal respiration rate at 20deg C. | - | - | - | - | `2.50000` | official GitBook |
| `slr_act` | Fraction of solar radiation computed in the temperature heat balance that is photosynthetically active. | - | - | - | - | `0.30000` | official GitBook |
| `lt_co` | Half-saturation coefficient for light. | - | - | - | - | `0.75000` | official GitBook |
| `const_n` | Michaelis-Menton half-saturation constant for N. | - | - | - | - | `0.02000` | official GitBook |
| `const_p` | Michaelis-Menton half-saturation constant for P. | - | - | - | - | `0.02500` | official GitBook |
| `lt_nonalg` | Non-algal portion of the light extinction coefficient. | - | - | - | - | `1.00000` | official GitBook |
| `alg_shd_l` | Linear algal self-shading coefficient. | - | - | - | - | `0.03000` | official GitBook |
| `alg_shd_nl` | Nonlinear algal self-shading coefficient. | - | - | - | - | `0.05400` | official GitBook |
| `nh3_pref` | Algal preference factor for ammonia. | - | - | - | - | `0.50000` | official GitBook |
| `description` | Header field observed in the demo file; trace the reader for exact storage and constraints. | - | - | - | - | - | demo/source inferred |

Additional official field rows that are not part of the observed demo header:

| Field | Meaning | Type | Unit |
| --- | --- | --- | --- |
| `plt_p` | Channel organic P concentration. | - | - |

## Defaults And Conversions

- Defaults: use the source inventory filename and the `file.cio` slot state as the first default/activation check.
- Missing-file behavior: if the master file or upstream manifest uses `null`, SWAT+ treats that slot as inactive for the scenario.
- Numeric conversions: not yet traced for this page; inspect the reader for unit conversions, bounds checks, and derived runtime fields.

## Reader Path

- Source inventory: `SWATPLUS/swatplus/src/input_file_module.f90`.
- Source slot: `in_cha%nut` defaulting to `nutrients.cha`.
- Candidate reader/source files: `SWATPLUS/swatplus/src/ch_read_nut.f90`.

## Downstream Consumers

Channel or SWAT-DEG channel hydrology, sediment, nutrient, and initialization routines.

## Scenario Evidence

- Scenario: `VSProj/SWAT/Osu_1hru`.
- Scenario state: `active`.
- Activation evidence: `file.cio`.
- Local file evidence: `VSProj/SWAT/Osu_1hru/nutrients.cha`.

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
