---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_canal_ext.f90
note_file: gwflow_canal_ext.f90
subroutine: gwflow_canal_ext
module:
  - gwflow_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - gwflow_module.f90#canal_out_conc
  - gwflow_module.f90#gw_canal_ncells_out
  - gwflow_module.f90#gw_canl_out_info
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
  - gwflow_module.f90#gwheat_state
  - gwflow_module.f90#gwsol_cons
  - gwflow_module.f90#gwsol_salt
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_ss_sum
  - gwflow_module.f90#gwsol_ss_sum_mo
  - gwflow_module.f90#gwsol_state
  - hydrograph_module.f90#ch_stor
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the water exchange volume between irrigation canals and connected grid cells; for canals that divert water from a source outside of the model domain."
---

# gwflow_canal_ext

> [!info] Summary
> this subroutine calculates the water exchange volume between irrigation canals and connected grid cells; for canals that divert water from a source outside of the model domain.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_canal_ext.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[gwflow_module.f90#canal_out_conc]] - `real, allocatable`
- [[gwflow_module.f90#gw_canal_ncells_out]] - `integer`
- [[gwflow_module.f90#gw_canl_out_info]] - `cell_canal_out_info`
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
- [[gwflow_module.f90#gwheat_state]] - `groundwater_heat_state`
- [[gwflow_module.f90#gwsol_cons]] - `integer`
- [[gwflow_module.f90#gwsol_salt]] - `integer`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_ss_sum]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_ss_sum_mo]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
