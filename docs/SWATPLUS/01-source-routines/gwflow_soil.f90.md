---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_soil.f90
note_file: gwflow_soil.f90
subroutine: gwflow_soil
module:
  - gwflow_module
  - soil_module
  - hydrograph_module
  - hru_module
  - time_module
calls: []
uses_variables:
  - gwflow_module.f90#cells_fract
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
  - gwflow_module.f90#hru_cells
  - gwflow_module.f90#hru_num_cells
  - hru_module.f90#gwsoilq
  - hydrograph_module.f90#ob
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the water exchange volume between the aquifer and the soil profile; (exchange volumes are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_soil

> [!info] Summary
> this subroutine calculates the water exchange volume between the aquifer and the soil profile; (exchange volumes are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_soil.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[soil_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[swr_percmain.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[gwflow_module.f90#cells_fract]] - `real, dimension (:,:), allocatable`
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
- [[gwflow_module.f90#hru_cells]] - `integer, dimension (:,:), allocatable`
- [[gwflow_module.f90#hru_num_cells]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#gwsoilq]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
