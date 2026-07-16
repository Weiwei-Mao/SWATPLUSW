---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_canal_div.f90
note_file: gwflow_canal_div.f90
subroutine: gwflow_canal_div
module:
  - gwflow_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
  - hru_module
  - res_salt_module
  - res_cs_module
  - salt_module
  - cs_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - cs_module.f90#hcsb_d
  - gwflow_module.f90#canal_out_conc
  - gwflow_module.f90#div_conc_cs
  - gwflow_module.f90#div_conc_salt
  - gwflow_module.f90#gw_canal_ncells_div
  - gwflow_module.f90#gw_canl_div_cell
  - gwflow_module.f90#gw_canl_div_info
  - gwflow_module.f90#gw_cp
  - gwflow_module.f90#gw_heat_flag
  - gwflow_module.f90#gw_heat_ss
  - gwflow_module.f90#gw_heat_ss_yr
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_mo
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_nsolute
  - gwflow_module.f90#gw_rho
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gwflag_flux
  - gwflow_module.f90#gwheat_state
  - gwflow_module.f90#gwsol_cons
  - gwflow_module.f90#gwsol_nm
  - gwflow_module.f90#gwsol_salt
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_ss_sum
  - gwflow_module.f90#gwsol_ss_sum_mo
  - gwflow_module.f90#gwsol_state
  - gwflow_module.f90#out_canal_bal
  - gwflow_module.f90#out_canal_sol
  - hru_module.f90#hru
  - hru_module.f90#mo
  - hydrograph_module.f90#irrig
  - res_cs_module.f90#wetcs_d
  - res_salt_module.f90#wetsalt_d
  - salt_module.f90#hsaltb_d
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the water exchange volume between irrigation canals and connected grid cells; for canals that are connected to a point source diversion (recall object); seepage water should be; removed from the diverted water volume."
---

# gwflow_canal_div

> [!info] Summary
> this subroutine calculates the water exchange volume between irrigation canals and connected grid cells; for canals that are connected to a point source diversion (recall object); seepage water should be; removed from the diverted water volume.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_canal_div.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[hru_module.f90]]
  - [[res_salt_module.f90]]
  - [[res_cs_module.f90]]
  - [[salt_module.f90]]
  - [[cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[gwflow_simulate.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[gwflow_module.f90#canal_out_conc]] - `real, allocatable`
- [[gwflow_module.f90#div_conc_cs]] - `real, allocatable`
- [[gwflow_module.f90#div_conc_salt]] - `real, allocatable`
- [[gwflow_module.f90#gw_canal_ncells_div]] - `integer`
- [[gwflow_module.f90#gw_canl_div_cell]] - `cell_canal_div_info`
- [[gwflow_module.f90#gw_canl_div_info]] - `canal_info`
- [[gwflow_module.f90#gw_cp]] - `real`
- [[gwflow_module.f90#gw_heat_flag]] - `integer`
- [[gwflow_module.f90#gw_heat_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_heat_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_nsolute]] - `integer`
- [[gwflow_module.f90#gw_rho]] - `real`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gwflag_flux]] - `integer`
- [[gwflow_module.f90#gwheat_state]] - `groundwater_heat_state`
- [[gwflow_module.f90#gwsol_cons]] - `integer`
- [[gwflow_module.f90#gwsol_nm]] - `character (len=16), allocatable`
- [[gwflow_module.f90#gwsol_salt]] - `integer`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_ss_sum]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_ss_sum_mo]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[gwflow_module.f90#out_canal_bal]] - `integer`
- [[gwflow_module.f90#out_canal_sol]] - `integer`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[res_cs_module.f90#wetcs_d]] - `res_cs_output`
- [[res_salt_module.f90#wetsalt_d]] - `res_salt_output`
- [[salt_module.f90#hsaltb_d]] - `object_salt_balance`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
