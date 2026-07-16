---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_lateral.f90
note_file: gwflow_lateral.f90
subroutine: gwflow_lateral
module:
  - gwflow_module
  - time_module
calls:
  - gwflow_heat
  - gwflow_solute
uses_variables:
  - gwflow_module.f90#bc_type_array
  - gwflow_module.f90#gw_cell_chan_flag
  - gwflow_module.f90#gw_cell_chan_time
  - gwflow_module.f90#gw_cell_tile_time
  - gwflow_module.f90#gw_heat_flag
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gw_time_step
  - gwflow_module.f90#gw_transit
  - gwflow_module.f90#gw_transit_cells
  - gwflow_module.f90#gw_transit_num
  - gwflow_module.f90#gw_ttime
  - gwflow_module.f90#ncell
  - gwflow_module.f90#out_gw_transit
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates lateral groundwater flow between adjacent cells; using Darcy's Law, then updates head and storage; (extracted from gwflow_simulate)"
---

# gwflow_lateral

> [!info] Summary
> this subroutine calculates lateral groundwater flow between adjacent cells; using Darcy's Law, then updates head and storage; (extracted from gwflow_simulate)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_lateral.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_heat.f90]]
- [[gwflow_solute.f90]]

**Called by:**

- [[gwflow_simulate.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[gwflow_module.f90#bc_type_array]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_cell_chan_flag]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_cell_chan_time]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_cell_tile_time]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_heat_flag]] - `integer`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gw_time_step]] - `real`
- [[gwflow_module.f90#gw_transit]] - `groundwater_transit`
- [[gwflow_module.f90#gw_transit_cells]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_transit_num]] - `integer`
- [[gwflow_module.f90#gw_ttime]] - `integer`
- [[gwflow_module.f90#ncell]] - `integer`
- [[gwflow_module.f90#out_gw_transit]] - `integer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
