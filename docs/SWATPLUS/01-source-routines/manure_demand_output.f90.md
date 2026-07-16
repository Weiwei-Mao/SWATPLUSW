---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: manure_demand_output.f90
note_file: manure_demand_output.f90
subroutine: manure_demand_output
module:
  - time_module
  - hydrograph_module
  - manure_allocation_module
calls: []
uses_variables:
  - manure_allocation_module.f90#mallo
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# manure_demand_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `manure_demand_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[manure_allocation_module.f90]]
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
- [[manure_allocation_module.f90#mallo]] - `manure_allocation`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
