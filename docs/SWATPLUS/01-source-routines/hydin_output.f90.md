---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hydin_output.f90
note_file: hydin_output.f90
subroutine: hydin_output
module:
  - hydrograph_module
  - time_module
  - basin_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine outputs hyd variables on daily, monthly and annual time steps"
---

# hydin_output

> [!info] Summary
> this subroutine outputs hyd variables on daily, monthly and annual time steps

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hydin_output.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
