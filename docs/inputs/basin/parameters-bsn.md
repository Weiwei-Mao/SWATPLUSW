---
title: parameters.bsn basin parameters
kind: input-reference
status: partial
created: 2026-07-13
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, basin, parameters-bsn]
---

# `parameters.bsn` Basin Parameters

## Summary

`parameters.bsn` contains basin-wide numeric parameters. Your understanding is right: these values apply at the whole-basin/model level, not to one individual HRU, channel, reservoir, or aquifer.

The important difference from `codes.bsn` is:

```text
codes.bsn       -> switches and method choices
parameters.bsn  -> numeric coefficients, default factors, calibration-style values
```

Examples:

- `codes.bsn` chooses whether Green-Ampt runoff is active.
- `parameters.bsn` gives numeric parameters used by hydrology, nutrients, erosion, routing, CO2, lapse rates, and other calculations.


## Official SWAT+ Reference

- Official page: [parameters.bsn](https://swatplus.gitbook.io/io-docs/introduction-1/basin-1/parameters.bsn).
- Official index note: This file contains basin-level parameters.
- Official field metadata available: 44 field row(s); matched to 43 of 44 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Reader Path

```text
file.cio
    -> in_basin%parms_bas = "parameters.bsn"
    -> proc_bsn
    -> basin_read_prm
    -> bsn_prm
    -> basin_prm_default
```

[`basin_read_prm.f90`](../../../SWATPLUS/swatplus/src/basin_read_prm.f90) reads:

1. title line;
2. header line;
3. one data line directly into `bsn_prm`.

The storage object is [`bsn_prm`](../../../SWATPLUS/swatplus/src/basin_module.f90), an instance of `type basin_parms`.

After the read, [`proc_bsn.f90`](../../../SWATPLUS/swatplus/src/proc_bsn.f90) calls [`basin_prm_default.f90`](../../../SWATPLUS/swatplus/src/basin_prm_default.f90). That routine sets defaults for some near-zero values, converts `petco_pmpt` from percent-style input to a multiplier, initializes nutrient uptake normalization values, and forces `bsn_prm%day_lag_mx = 2`.

## File Format

`parameters.bsn` has three logical lines:

1. title/comment line;
2. header line;
3. one data line, read by field order into `bsn_prm`.

The header names are the file-facing names. The internal names are the fields in `type basin_parms`. The read is positional, so column order is the contract.

## Difference From `codes.bsn`

| File | Storage | Main role | Example |
| --- | --- | --- | --- |
| `codes.bsn` | `bsn_cc` | Turns model options on/off or chooses methods. | `pet`, `gampt`, `gw_flow`, `carbon`, `tiledrain`. |
| `parameters.bsn` | `bsn_prm` | Supplies numeric coefficients used by selected processes. | `surq_lag`, `n_perc`, `msk_x`, `tlaps`, `co2`. |

Use this rule while debugging:

```text
If the value answers "which method / active or inactive?", check codes.bsn.
If the value answers "how much / what coefficient?", check parameters.bsn.
```

## Field Meaning

| `parameters.bsn` header | Stored field | Meaning from source |
| --- | --- | --- |
| `lai_noevap` | `bsn_prm%evlai` | Leaf area index at which no soil evaporation occurs. |
| `sw_init` | `bsn_prm%ffcb` | Initial soil water content as a fraction of field capacity. |
| `surq_lag` | `bsn_prm%surlag` | Surface runoff lag time, days. |
| `adj_pkrt` | `bsn_prm%adj_pkr` | Peak-rate adjustment factor. |
| `adj_pkrt_sed` | `bsn_prm%prf` | Peak-rate factor / sediment peak-rate adjustment. |
| `lin_sed` | `bsn_prm%spcon` | Source marks this as not used. |
| `exp_sed` | `bsn_prm%spexp` | Source marks this as not used. |
| `orgn_min` | `bsn_prm%cmn` | Rate factor for mineralization of active organic nitrogen. |
| `n_uptake` | `bsn_prm%n_updis` | Nitrogen uptake distribution parameter. |
| `p_uptake` | `bsn_prm%p_updis` | Phosphorus uptake distribution parameter. |
| `n_perc` | `bsn_prm%nperco` | Nitrate percolation coefficient. |
| `p_perc` | `bsn_prm%pperco` | Phosphorus percolation coefficient. |
| `p_soil` | `bsn_prm%phoskd` | Phosphorus soil partitioning coefficient. |
| `p_avail` | `bsn_prm%psp` | Phosphorus availability index. |
| `rsd_decomp` | `bsn_prm%rsdco` | Residue decomposition coefficient. |
| `pest_perc` | `bsn_prm%percop` | Pesticide percolation coefficient. |
| `msk_co1` | `bsn_prm%msk_co1` | Muskingum/channel storage calibration coefficient for bankfull-depth behavior. |
| `msk_co2` | `bsn_prm%msk_co2` | Muskingum/channel storage calibration coefficient for low-flow behavior. |
| `msk_x` | `bsn_prm%msk_x` | Muskingum weighting factor for inflow/outflow importance. |
| `nperco_lchtile` | `bsn_prm%nperco_lchtile` | Nitrogen concentration coefficient for tile flow and leaching from the bottom layer. |
| `evap_adj` | `bsn_prm%evrch` | Reach evaporation adjustment factor. |
| `scoef` | `bsn_prm%scoef` | Channel storage coefficient. |
| `denit_exp` | `bsn_prm%cdn` | Denitrification exponential rate coefficient. |
| `denit_frac` | `bsn_prm%sdnco` | Denitrification threshold fraction of field capacity. |
| `man_bact` | `bsn_prm%bact_swf` | Fraction of manure containing active colony forming units. |
| `adj_uhyd` | `bsn_prm%tb_adj` | Adjustment factor for subdaily unit-hydrograph base time. |
| `cn_froz` | `bsn_prm%cn_froz` | Frozen-soil adjustment parameter for infiltration/runoff. |
| `dorm_hr` | `bsn_prm%dorm_hr` | Hour threshold used to define plant dormancy. |
| `plaps` | `bsn_prm%plaps` | Precipitation lapse rate, mm/km. |
| `tlaps` | `bsn_prm%tlaps` | Temperature lapse rate, deg C/km. |
| `n_fix_max` | `bsn_prm%nfixmx` | Maximum daily nitrogen fixation, kg/ha. |
| `rsd_decay` | `bsn_prm%decr_min` | Minimum daily residue decay. |
| `rsd_cover` | `bsn_prm%rsd_covco` | Residue cover factor used in cover-factor calculations. |
| `urb_init_abst` | `bsn_prm%urb_init_abst` | Maximum initial abstraction for urban areas when Green-Ampt is used. |
| `petco_pmpt` | `bsn_prm%petco_pmpt` | PET adjustment input; converted by `basin_prm_default` to a multiplier. |
| `uhyd_alpha` | `bsn_prm%uhalpha` | Alpha coefficient for estimating the gamma-function unit hydrograph. |
| `splash` | `bsn_prm%eros_spl` | Splash erosion coefficient. |
| `rill` | `bsn_prm%rill_mult` | Rill erosion multiplier. |
| `surq_exp` | `bsn_prm%eros_expo` | Exponential coefficient for overland-flow erosion. |
| `cov_mgt` | `bsn_prm%c_factor` | Scaling parameter for cover/management factor in overland-flow erosion. |
| `cha_d50` | `bsn_prm%ch_d50` | Median particle diameter of the main channel, mm. |
| `co2` | `bsn_prm%co2` | CO2 concentration at the start of simulation, ppm. |
| `day_lag_max` | `bsn_prm%day_lag_mx` | Maximum days to lag hydrographs for HRU, routing-unit, and channel routing. Later forced to `2` by `basin_prm_default`. |
| `igen` | `bsn_prm%igen` | Random generator code. |

## `Osu_1hru` Values

In [`VSProj/SWAT/Osu_1hru/parameters.bsn`](../../../VSProj/SWAT/Osu_1hru/parameters.bsn), notable values include:

- `surq_lag = 1.0`
- `n_perc = 0.1`
- `p_perc = 10.0`
- `msk_co1 = 0.75`
- `msk_co2 = 0.25`
- `msk_x = 0.20`
- `evap_adj = 0.60`
- `tlaps = 0.0` in the file, but default handling may replace near-zero values for some fields.
- `co2 = 1.57` in the file, but `basin_prm_default` sets `bsn_prm%co2 = 400.` if it is less than `100.`
- `day_lag_max = 0` in the file, but `basin_prm_default` later forces `bsn_prm%day_lag_mx = 2`.

This means the file value is not always the final runtime value. When debugging, inspect `bsn_prm` both immediately after `basin_read_prm` and after `basin_prm_default`.

## Important Consumers

Examples of downstream use:

| Field | Example consumer |
| --- | --- |
| `surlag` | `time_conc_init.f90` computes runoff lag behavior. |
| `nperco`, `pperco`, `phoskd`, `psp`, `cmn` | `hrudb_init.f90`, nutrient routines, and plant uptake logic. |
| `msk_co1`, `msk_co2`, `msk_x` | `sd_hydsed_init.f90` and channel routing. |
| `evrch` | Channel and wetland evaporation calculations. |
| `plaps`, `tlaps` | `cli_lapse.f90` elevation adjustment. |
| `co2` | `co2_read.f90` and plant growth CO2 handling. |
| `day_lag_mx` | `hyd_connect.f90`, `flow_hyd_ru_hru.f90`, and unit hydrograph arrays. |

## Debugging Notes

Useful breakpoints:

1. `basin_read_prm.f90`, after the `read (... ) bsn_prm`, to inspect raw file values.
2. `basin_prm_default.f90`, after defaults are applied, to inspect final runtime values.
3. A downstream consumer for the parameter of interest, such as `time_conc_init.f90` for `surlag` or `cli_lapse.f90` for `plaps`/`tlaps`.

## Evidence

- [`VSProj/SWAT/Osu_1hru/parameters.bsn`](../../../VSProj/SWAT/Osu_1hru/parameters.bsn): active scenario values.
- [`basin_read_prm.f90`](../../../SWATPLUS/swatplus/src/basin_read_prm.f90): reader and `bsn_prm` assignment.
- [`basin_module.f90`](../../../SWATPLUS/swatplus/src/basin_module.f90): `type basin_parms` field definitions and comments.
- [`basin_prm_default.f90`](../../../SWATPLUS/swatplus/src/basin_prm_default.f90): default and conversion logic after file read.
- `rg "bsn_prm%" SWATPLUS/swatplus/src --glob "*.f90"`: downstream consumer search.

## Related Notes

- [`codes.bsn` basin control codes](codes-bsn.md)
- [CO2 and carbon input readers](../../topics/co2-carbon-inputs.md)
- [`object.cnt` and object concepts](../simulation/object-cnt.md)
- [`file.cio` master input file](../simulation/file-cio.md)
- [Tracing guide](../../tracing-guide.md)
