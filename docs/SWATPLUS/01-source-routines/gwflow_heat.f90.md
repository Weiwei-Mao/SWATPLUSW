---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_heat.f90
note_file: gwflow_heat.f90
subroutine: gwflow_heat
module:
  - gwflow_module
  - time_module
calls: []
uses_variables:
  - gwflow_module.f90#gw_cp
  - gwflow_module.f90#gw_heat_ss
  - gwflow_module.f90#gw_heat_ss_yr
  - gwflow_module.f90#gw_rho
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gw_time_step
  - gwflow_module.f90#gwheat_state
  - gwflow_module.f90#heat_cell
  - gwflow_module.f90#ncell
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates heat advection and dispersion for groundwater; heat transport. Called from gwflow_lateral once per flow time step, after; the Darcy head update. Uses cell_con%latl and cell_con%sat populated"
---

# gwflow_heat

> [!info] Summary
> this subroutine calculates heat advection and dispersion for groundwater; heat transport. Called from gwflow_lateral once per flow time step, after; the Darcy head update. Uses cell_con%latl and cell_con%sat populated

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_heat.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[gwflow_lateral.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[gwflow_module.f90#gw_cp]] - `real`
- [[gwflow_module.f90#gw_heat_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_heat_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_rho]] - `real`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gw_time_step]] - `real`
- [[gwflow_module.f90#gwheat_state]] - `groundwater_heat_state`
- [[gwflow_module.f90#heat_cell]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#ncell]] - `integer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
