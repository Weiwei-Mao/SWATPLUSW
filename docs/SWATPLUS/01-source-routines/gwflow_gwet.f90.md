---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_gwet.f90
note_file: gwflow_gwet.f90
subroutine: gwflow_gwet
module:
  - gwflow_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
calls: []
uses_variables:
  - calibration_data_module.f90#lsu_out
  - gwflow_module.f90#etremain
  - gwflow_module.f90#gw_cp
  - gwflow_module.f90#gw_heat_flag
  - gwflow_module.f90#gw_heat_ss
  - gwflow_module.f90#gw_heat_ss_yr
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_mo
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_rho
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gwheat_state
  - gwflow_module.f90#hru_cells
  - gwflow_module.f90#hru_cells_fract
  - gwflow_module.f90#hru_num_cells
  - gwflow_module.f90#lsu_cells
  - gwflow_module.f90#lsu_cells_fract
  - gwflow_module.f90#lsu_cells_link
  - gwflow_module.f90#lsu_num_cells
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
input_variables: []
reads: []
writes: []
purpose: "this subroutine determines the volume of groundwater that is removed from the; aquifer via ET"
---

# gwflow_gwet

> [!info] Summary
> this subroutine determines the volume of groundwater that is removed from the; aquifer via ET

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_gwet.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[calibration_data_module.f90#lsu_out]] - `landscape_units`
- [[gwflow_module.f90#etremain]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_cp]] - `real`
- [[gwflow_module.f90#gw_heat_flag]] - `integer`
- [[gwflow_module.f90#gw_heat_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_heat_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_rho]] - `real`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gwheat_state]] - `groundwater_heat_state`
- [[gwflow_module.f90#hru_cells]] - `integer, dimension (:,:), allocatable`
- [[gwflow_module.f90#hru_cells_fract]] - `real, dimension (:,:), allocatable`
- [[gwflow_module.f90#hru_num_cells]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#lsu_cells]] - `integer, dimension (:,:), allocatable`
- [[gwflow_module.f90#lsu_cells_fract]] - `real, dimension (:,:), allocatable`
- [[gwflow_module.f90#lsu_cells_link]] - `integer`
- [[gwflow_module.f90#lsu_num_cells]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
