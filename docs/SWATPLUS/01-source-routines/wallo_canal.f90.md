---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_canal.f90
note_file: wallo_canal.f90
subroutine: wallo_canal
module:
  - water_allocation_module
  - hydrograph_module
  - constituent_mass_module
  - basin_module
  - aquifer_module
  - gwflow_module
calls: []
uses_variables:
  - aquifer_module.f90#aqu_d
  - basin_module.f90#bsn_cc
  - gwflow_module.f90#gw_canal_ncells_div
  - gwflow_module.f90#gw_canl_div_cell
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_mo
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_state
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#canal_om_out
  - hydrograph_module.f90#canal_om_stor
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#outflo_om
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - water_allocation_module.f90#canal
  - water_allocation_module.f90#wallod_out
input_variables: []
reads: []
writes: []
purpose: "Routes water through a wallo canal: computes outflow, applies loss,; and distributes canal seepage to aquifer (gwflow grid cells or 1-D aquifer)."
---

# wallo_canal

> [!info] Summary
> Routes water through a wallo canal: computes outflow, applies loss,; and distributes canal seepage to aquifer (gwflow grid cells or 1-D aquifer).

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_canal.f90`
- **Modules used**:
  - [[water_allocation_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[basin_module.f90]]
  - [[aquifer_module.f90]]
  - [[gwflow_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[wallo_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[gwflow_module.f90#gw_canal_ncells_div]] - `integer`
- [[gwflow_module.f90#gw_canl_div_cell]] - `cell_canal_div_info`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#canal_om_out]] - `hyd_output`
- [[hydrograph_module.f90#canal_om_stor]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#outflo_om]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[water_allocation_module.f90#canal]] - `water_canal_data`
- [[water_allocation_module.f90#wallod_out]] - `water_allocation_output`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
