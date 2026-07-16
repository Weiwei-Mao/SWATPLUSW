---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_wetland.f90
note_file: gwflow_wetland.f90
subroutine: gwflow_wetland
module:
  - gwflow_module
  - hydrograph_module
  - hru_module
  - water_body_module
calls: []
uses_variables:
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
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_ss_sum
  - gwflow_module.f90#gwsol_ss_sum_mo
  - gwflow_module.f90#gwsol_state
  - gwflow_module.f90#hru_cells
  - gwflow_module.f90#hru_cells_fract
  - gwflow_module.f90#hru_num_cells
  - hru_module.f90#hru
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_in_d
  - water_body_module.f90#wet_wat_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine determines the volume of groundwater exchanged with wetlands; (exchange volumes are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_wetland

> [!info] Summary
> this subroutine determines the volume of groundwater exchanged with wetlands; (exchange volumes are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_wetland.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[water_body_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[wetland_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
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
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_ss_sum]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_ss_sum_mo]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[gwflow_module.f90#hru_cells]] - `integer, dimension (:,:), allocatable`
- [[gwflow_module.f90#hru_cells_fract]] - `real, dimension (:,:), allocatable`
- [[gwflow_module.f90#hru_num_cells]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_d]] - `hyd_output`
- [[water_body_module.f90#wet_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
