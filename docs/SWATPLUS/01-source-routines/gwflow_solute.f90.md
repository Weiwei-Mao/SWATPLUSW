---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_solute.f90
note_file: gwflow_solute.f90
subroutine: gwflow_solute
module:
  - gwflow_module
  - time_module
calls:
  - gwflow_chem
uses_variables:
  - gwflow_module.f90#gw_long_disp
  - gwflow_module.f90#gw_nsolute
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gw_time_step
  - gwflow_module.f90#gwsol_sorb
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_ss_sum
  - gwflow_module.f90#gwsol_ss_sum_mo
  - gwflow_module.f90#gwsol_state
  - gwflow_module.f90#mass_min
  - gwflow_module.f90#mass_rct
  - gwflow_module.f90#ncell
  - gwflow_module.f90#num_ts_transport
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates solute advection, dispersion, chemical; reactions, and sorption for groundwater solute transport. Called from; gwflow_lateral once per flow time step. Contains its own sub-timestep"
---

# gwflow_solute

> [!info] Summary
> this subroutine calculates solute advection, dispersion, chemical; reactions, and sorption for groundwater solute transport. Called from; gwflow_lateral once per flow time step. Contains its own sub-timestep

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_solute.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_chem.f90]]

**Called by:**

- [[gwflow_lateral.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[gwflow_module.f90#gw_long_disp]] - `real`
- [[gwflow_module.f90#gw_nsolute]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gw_time_step]] - `real`
- [[gwflow_module.f90#gwsol_sorb]] - `real, allocatable`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_ss_sum]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_ss_sum_mo]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[gwflow_module.f90#mass_min]] - `real, allocatable`
- [[gwflow_module.f90#mass_rct]] - `real, allocatable`
- [[gwflow_module.f90#ncell]] - `integer`
- [[gwflow_module.f90#num_ts_transport]] - `integer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
