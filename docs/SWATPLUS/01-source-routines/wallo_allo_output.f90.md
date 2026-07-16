---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_allo_output.f90
note_file: wallo_allo_output.f90
subroutine: wallo_allo_output
module:
  - time_module
  - hydrograph_module
  - water_allocation_module
calls: []
uses_variables:
  - time_module.f90#time
  - water_allocation_module.f90#wallo
  - water_allocation_module.f90#walloa_out
  - water_allocation_module.f90#wallod_out
  - water_allocation_module.f90#wallom_out
  - water_allocation_module.f90#walloy_out
  - water_allocation_module.f90#walloz
input_variables: []
reads: []
writes: []
purpose: ""
---

# wallo_allo_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_allo_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[water_allocation_module.f90]]
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
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_allocation_module.f90#walloa_out]] - `water_allocation_output`
- [[water_allocation_module.f90#wallod_out]] - `water_allocation_output`
- [[water_allocation_module.f90#wallom_out]] - `water_allocation_output`
- [[water_allocation_module.f90#walloy_out]] - `water_allocation_output`
- [[water_allocation_module.f90#walloz]] - `source_output`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
