---
type: module
tags:
  - swat/module
  - swat/to-read
file: carbon_module.f90
note_file: carbon_module.f90
module_name: carbon_module
defines_types:
  - carbon_inputs
  - manure_coef
  - organic_allocations
  - organic_controls
  - organic_fractions
  - organic_ratio
  - carbon_water_coef
  - organic_transformations
  - organic_flux
  - carbon_soil_transformations
  - carbon_soil_gain_losses
  - carbon_residue_gain_losses
  - carbon_plant_gain_losses
defines_vars:
  - carbz
  - man_coef
  - org_alloz
  - org_con
  - org_frac
  - org_ratio
  - org_ratio_zero
  - cb_wtr_coef
  - org_tran
  - org_tran_zero
  - org_flux
  - org_flux_zero
  - hscfz
  - bscf_d
  - bscf_m
  - bscf_y
  - bscf_a
  - hscz
  - bsc_d
  - bsc_m
  - bsc_y
  - bsc_a
  - hrcz
  - brc_d
  - brc_m
  - brc_y
  - brc_a
  - hpcz
  - bpc_d
  - bpc_m
  - bpc_y
  - bpc_a
  - cpool_vars
  - n_p_pool_vars
  - cflux_vars
  - carb_drv_vars
  - carb_dyn_vars
  - soil_snap_vars
purpose: ""
---

# carbon_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `carbon_inputs` |  |
| `manure_coef` |  |
| `organic_allocations` |  |
| `organic_controls` |  |
| `organic_fractions` |  |
| `organic_ratio` |  |
| `carbon_water_coef` |  |
| `organic_transformations` |  |
| `organic_flux` |  |
| `carbon_soil_transformations` |  |
| `carbon_soil_gain_losses` |  |
| `carbon_residue_gain_losses` |  |
| `carbon_plant_gain_losses` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `carbz` |  |  |
| `man_coef` |  |  |
| `org_alloz` |  |  |
| `org_con` |  |  |
| `org_frac` |  |  |
| `org_ratio` |  |  |
| `org_ratio_zero` |  |  |
| `cb_wtr_coef` |  |  |
| `org_tran` |  |  |
| `org_tran_zero` |  |  |
| `org_flux` |  |  |
| `org_flux_zero` |  |  |
| `hscfz` |  |  |
| `bscf_d` |  |  |
| `bscf_m` |  |  |
| `bscf_y` |  |  |
| `bscf_a` |  |  |
| `hscz` |  |  |
| `bsc_d` |  |  |
| `bsc_m` |  |  |
| `bsc_y` |  |  |
| `bsc_a` |  |  |
| `hrcz` |  |  |
| `brc_d` |  |  |
| `brc_m` |  |  |
| `brc_y` |  |  |
| `brc_a` |  |  |
| `hpcz` |  |  |
| `bpc_d` |  |  |
| `bpc_m` |  |  |
| `bpc_y` |  |  |
| `bpc_a` |  |  |
| `cpool_vars` |  |  |
| `n_p_pool_vars` |  |  |
| `cflux_vars` |  |  |
| `carb_drv_vars` |  |  |
| `carb_dyn_vars` |  |  |
| `soil_snap_vars` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
