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
- **Modules used**: [[gwflow_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
