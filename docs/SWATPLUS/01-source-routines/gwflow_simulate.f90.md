---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_simulate.f90
note_file: gwflow_simulate.f90
subroutine: gwflow_simulate
module:
  - gwflow_module
  - hydrograph_module
  - hru_module
  - sd_channel_module
  - time_module
  - soil_module
calls:
  - gwflow_rech
  - gwflow_gwet
  - gwflow_phreatophyte
  - gwflow_pump_ext
  - gwflow_canal_ext
  - gwflow_pond
  - gwflow_canal_div
  - gwflow_lateral
  - gwflow_output_day
  - gwflow_output_mon
  - gwflow_output_yr
  - gwflow_output_aa
uses_variables:
  - gwflow_module.f90#gw_canl_div_info
  - gwflow_module.f90#gw_chan_dep
  - gwflow_module.f90#gw_chan_dep_flag
  - gwflow_module.f90#gw_chan_ndpzn
  - gwflow_module.f90#gw_cp
  - gwflow_module.f90#gw_heat_flag
  - gwflow_module.f90#gw_heat_ss
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_nsolute
  - gwflow_module.f90#gw_num_obs_wells
  - gwflow_module.f90#gw_num_output
  - gwflow_module.f90#gw_obs_cells
  - gwflow_module.f90#gw_obs_head
  - gwflow_module.f90#gw_obs_solute
  - gwflow_module.f90#gw_obs_temp
  - gwflow_module.f90#gw_output_day
  - gwflow_module.f90#gw_output_index
  - gwflow_module.f90#gw_output_yr
  - gwflow_module.f90#gw_rho
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gw_time_step
  - gwflow_module.f90#gwflag_flux
  - gwflow_module.f90#gwflag_pump
  - gwflow_module.f90#gwheat_state
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_state
  - gwflow_module.f90#mass_rct
  - gwflow_module.f90#ncell
  - gwflow_module.f90#out_gw
  - gwflow_module.f90#out_gwsw_chanobs_flow
  - gwflow_module.f90#out_gwsw_chanobs_no3
  - gwflow_module.f90#out_gwsw_groups
  - gwflow_module.f90#out_hru_pump_obs
  - gwflow_module.f90#out_tile_cells
  - hru_module.f90#hru
  - hru_module.f90#mo
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#sp_ob
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates new groundwater storage and solute mass for each gwflow grid cell;; also, computes and write out daily/annual/average annual fluxes and mass balance error"
---

# gwflow_simulate

> [!info] Summary
> this subroutine calculates new groundwater storage and solute mass for each gwflow grid cell;; also, computes and write out daily/annual/average annual fluxes and mass balance error

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_simulate.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[sd_channel_module.f90]]
  - [[time_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 12 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_rech.f90]]
- [[gwflow_gwet.f90]]
- [[gwflow_phreatophyte.f90]]
- [[gwflow_pump_ext.f90]]
- [[gwflow_canal_ext.f90]]
- [[gwflow_pond.f90]]
- [[gwflow_canal_div.f90]]
- [[gwflow_lateral.f90]]
- `gwflow_output_day`
- `gwflow_output_mon`
- `gwflow_output_yr`
- `gwflow_output_aa`

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[gwflow_module.f90#gw_canl_div_info]] - `canal_info`
- [[gwflow_module.f90#gw_chan_dep]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_chan_dep_flag]] - `integer`
- [[gwflow_module.f90#gw_chan_ndpzn]] - `integer`
- [[gwflow_module.f90#gw_cp]] - `real`
- [[gwflow_module.f90#gw_heat_flag]] - `integer`
- [[gwflow_module.f90#gw_heat_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_nsolute]] - `integer`
- [[gwflow_module.f90#gw_num_obs_wells]] - `integer`
- [[gwflow_module.f90#gw_num_output]] - `integer`
- [[gwflow_module.f90#gw_obs_cells]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_obs_head]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_obs_solute]] - `real, dimension (:,:), allocatable`
- [[gwflow_module.f90#gw_obs_temp]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_output_day]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_output_index]] - `integer`
- [[gwflow_module.f90#gw_output_yr]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_rho]] - `real`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gw_time_step]] - `real`
- [[gwflow_module.f90#gwflag_flux]] - `integer`
- [[gwflow_module.f90#gwflag_pump]] - `integer`
- [[gwflow_module.f90#gwheat_state]] - `groundwater_heat_state`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[gwflow_module.f90#mass_rct]] - `real, allocatable`
- [[gwflow_module.f90#ncell]] - `integer`
- [[gwflow_module.f90#out_gw]] - `integer`
- [[gwflow_module.f90#out_gwsw_chanobs_flow]] - `integer`
- [[gwflow_module.f90#out_gwsw_chanobs_no3]] - `integer`
- [[gwflow_module.f90#out_gwsw_groups]] - `integer`
- [[gwflow_module.f90#out_hru_pump_obs]] - `integer`
- [[gwflow_module.f90#out_tile_cells]] - `integer`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
