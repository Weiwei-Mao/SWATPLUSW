---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_rech.f90
note_file: gwflow_rech.f90
subroutine: gwflow_rech
module:
  - gwflow_module
  - hydrograph_module
  - maximum_data_module
  - calibration_data_module
  - soil_module
calls: []
uses_variables:
  - calibration_data_module.f90#lsu_out
  - gwflow_module.f90#gw_bound_near
  - gwflow_module.f90#gw_cp
  - gwflow_module.f90#gw_delay
  - gwflow_module.f90#gw_heat_flag
  - gwflow_module.f90#gw_heat_ss
  - gwflow_module.f90#gw_heat_ss_yr
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_mo
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_nsolute
  - gwflow_module.f90#gw_rech
  - gwflow_module.f90#gw_rechheat
  - gwflow_module.f90#gw_rechsol
  - gwflow_module.f90#gw_rho
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gwflow_perc
  - gwflow_module.f90#gwflow_percsol
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_ss_sum
  - gwflow_module.f90#gwsol_ss_sum_mo
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
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine determines the volume of groundwater that is added to the aquifer via recharge (soil percolation); (recharge volumes are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_rech

> [!info] Summary
> this subroutine determines the volume of groundwater that is added to the aquifer via recharge (soil percolation); (recharge volumes are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_rech.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[soil_module.f90]]
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
- [[gwflow_module.f90#gw_bound_near]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_cp]] - `real`
- [[gwflow_module.f90#gw_delay]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_heat_flag]] - `integer`
- [[gwflow_module.f90#gw_heat_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_heat_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_nsolute]] - `integer`
- [[gwflow_module.f90#gw_rech]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_rechheat]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_rechsol]] - `real, dimension (:,:), allocatable`
- [[gwflow_module.f90#gw_rho]] - `real`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gwflow_perc]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gwflow_percsol]] - `real, dimension (:,:), allocatable`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_ss_sum]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_ss_sum_mo]] - `object_solute_ss_sum`
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
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
