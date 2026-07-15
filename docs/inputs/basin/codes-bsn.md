---
title: codes.bsn basin control codes
kind: input-reference
status: partial
created: 2026-07-13
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, basin, control-codes, codes-bsn]
---

# `codes.bsn` Basin Control Codes

## Summary

`codes.bsn` contains basin-level control switches. Your understanding is right: these settings apply to the whole modeled study area, not to one individual HRU, channel, reservoir, or aquifer.

The file is selected by `file.cio` under the `basin` section. In `Osu_1hru`, that section points to `codes.bsn`.


## Official SWAT+ Reference

- Official page: [codes.bsn](https://swatplus.gitbook.io/io-docs/introduction-1/basin-1/codes.bsn).
- Official index note: This file contains control codes for the simulation of basin-level processes.
- Official field metadata available: 14 field row(s); matched to 11 of 26 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Reader Path

```text
file.cio
    -> in_basin%codes_bas = "codes.bsn"
    -> proc_bsn
    -> basin_read_cc
    -> bsn_cc
```

[`basin_read_cc.f90`](../../../SWATPLUS/swatplus/src/basin_read_cc.f90) reads the file:

- L16: checks `in_basin%codes_bas`.
- L19: opens the selected file on unit `107`.
- L20-22: reads title and header.
- L24: reads the full data row into `bsn_cc`.
- L30-40: if `bsn_cc%pet == 3`, opens `pet.cli` on unit `140`.

The storage object is [`bsn_cc`](../../../SWATPLUS/swatplus/src/basin_module.f90), an instance of `type basin_control_codes` in `basin_module.f90`.

## File Format

`codes.bsn` has three logical lines:

1. title/comment line;
2. header line;
3. one data line, read directly into `bsn_cc` by field order.

The header names do not always match the internal variable names. The source code reads the whole row into `bsn_cc`, so the order is the important contract.

The `do` wrapper in `basin_read_cc.f90` should not be interpreted as a supported multi-record basin format. The normal file has one active data line. The routine reads that data row and exits.

## Field Meaning

| `codes.bsn` header | Stored field | Meaning from source | `Osu_1hru` value |
| --- | --- | --- | --- |
| `pet_file` | `bsn_cc%petfile` | Optional potential ET filename. | `null` |
| `wq_file` | `bsn_cc%wwqfile` | Watershed stream water-quality filename. | `null` |
| `pet` | `bsn_cc%pet` | Potential ET method: `0` Priestley-Taylor, `1` Penman-Monteith, `2` Hargreaves, `3` read `pet.cli`. | `1` |
| `event` | `bsn_cc%nam1` | Historical/event-style input switch. Despite the source comment `not used`, it is checked by plant and soil-plant readers to choose a longer input format. | `0` |
| `crack` | `bsn_cc%crk` | Crack-flow switch: `1` computes flow in soil cracks. | `0` |
| `rtu_wq` | `bsn_cc%swift_out` | Source comment says SWIFT output switch: `0` no SWIFT input file, `1` write `swift_hru.inp`. Header name is historical. | `1` |
| `sed_det` | `bsn_cc%sed_det` | Peak-rate method: `0` NRCS dimensionless hydrograph with PRF, `1` half-hour rainfall-intensity method. | `0` |
| `rte_cha` | `bsn_cc%rte` | Channel water-routing method: `0` variable storage, `1` Muskingum. | `0` |
| `deg_cha` | `bsn_cc%deg` | Not used in current source comments. | `0` |
| `wq_cha` | `bsn_cc%wq` | Not used in current source comments. | `1` |
| `nostress` | `bsn_cc%nostress` | Plant stress switch: `0` all stresses applied, `1` turn off all plant stress, `2` turn off nutrient plant stress only. | `0` |
| `cn` | `bsn_cc%cn` | Not used in current source comments. | `0` |
| `c_fact` | `bsn_cc%cfac` | Not used as an input in current source comments; erosion code can set it internally. | `0` |
| `carbon` | `bsn_cc%cswat` | Soil carbon model: `0` static/legacy, `1` reserved C-FARM one-pool, `2` dynamic CENTURY/SWAT-C model. | `0` |
| `lapse` | `bsn_cc%lapse` | Precipitation and temperature lapse-rate control: `0` no elevation adjustment, `1` adjust for elevation. | `0` |
| `uhyd` | `bsn_cc%uhyd` | Unit hydrograph method: `0` triangular, `1` gamma function. | `1` |
| `sed_cha` | `bsn_cc%sed_ch` | Not used in current source comments. | `0` |
| `tiledrain` | `bsn_cc%tdrn` | Tile drainage equation: `0` drawdown-days equation, `1` DRAINMOD equations. | `0` |
| `wtable` | `bsn_cc%wtdn` | Shallow water-table algorithm: `0` original routine, `1` DRAINMOD water-table routine. | `0` |
| `soil_p` | `bsn_cc%sol_P_model` | Soil phosphorus model: `0` original SWAT soil P model, `1` Vadas and White model. | `0` |
| `gampt` | `bsn_cc%gampt` | Runoff/infiltration method: `0` curve number, `1` Green-Ampt. | `0` |
| `atmo_dep` | `bsn_cc%atmo` | Source comment says not used. | `a` |
| `stor_max` | `bsn_cc%smax` | Source comment says not used. | `0` |
| `i_fpwet` | `bsn_cc%qual2e` | In-stream nutrient routing: `0` QUAL2E, `1` QUAL2E with simplified nutrient transformations. Header name is historical. | `0` |
| `gw_flow` | `bsn_cc%gwflow` | Groundwater flow module switch: `0` inactive, `1` active. | `0` |
| `idc_till` | `bsn_cc%idc_till` | Tillage method when `carbon/cswat == 2`: `1` DSSAT, `2` EPIC, `3` Kemanian, `4` DNDC. | `3` |

## Important Consumers

Not every field has been traced to all downstream routines yet, but verified examples include:

| Field | Example downstream use |
| --- | --- |
| `bsn_cc%pet` | `et_pot.f90` selects the PET method; `basin_read_cc.f90` opens `pet.cli` if value is `3`. |
| `bsn_cc%cswat` | Carbon/nutrient routines and management operations choose legacy vs dynamic carbon behavior. |
| `bsn_cc%idc_till` | `cbn_zhang2.f90` selects the tillage mixing method when dynamic carbon is active. |
| `bsn_cc%rte` | Channel routing uses variable storage vs Muskingum logic. |
| `bsn_cc%lapse` | HRU/reservoir/channel controllers can apply climate lapse adjustments. |
| `bsn_cc%gampt` | Surface runoff and erosion paths choose curve number vs Green-Ampt behavior. |
| `bsn_cc%gwflow` | Groundwater-flow-aware routines enable/disable grid groundwater behavior. |
| `bsn_cc%nostress` | Plant growth can disable all stress or only nutrient stress. |

## How To Debug This File

Useful breakpoints:

1. `basin_read_cc.f90`, before line 24, to inspect `in_basin%codes_bas`.
2. `basin_read_cc.f90`, after line 24, to inspect the populated `bsn_cc`.
3. The first downstream consumer for the switch of interest, such as `et_pot.f90` for `pet` or `hru_control.f90` for `gampt`, `crack`, `lapse`, or `cswat`.

## Evidence

- [`VSProj/SWAT/Osu_1hru/codes.bsn`](../../../VSProj/SWAT/Osu_1hru/codes.bsn): active scenario values.
- [`basin_read_cc.f90`](../../../SWATPLUS/swatplus/src/basin_read_cc.f90): reader and `bsn_cc` assignment.
- [`basin_module.f90`](../../../SWATPLUS/swatplus/src/basin_module.f90): `type basin_control_codes` field definitions and comments.
- `rg "bsn_cc%" SWATPLUS/swatplus/src --glob "*.f90"`: downstream consumer search.

## Unresolved Boundaries

- Several fields are marked `not used` in `basin_module.f90`, but may still have historical meanings in editors or legacy file formats.
- The full downstream path for every control code has not been traced.
- Some `codes.bsn` header names are historical and do not match the internal field names; the mapping above should be treated as source-order verified.

## Related Notes

- [`parameters.bsn` basin parameters](parameters-bsn.md)
- [CO2 and carbon input readers](../../topics/co2-carbon-inputs.md)
- [`file.cio` master input file](../simulation/file-cio.md)
- [`object.cnt` and object concepts](../simulation/object-cnt.md)
- [Tracing guide](../../tracing-guide.md)
