---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_withdraw.f90
note_file: wallo_withdraw.f90
subroutine: wallo_withdraw
module:
  - water_allocation_module
  - hydrograph_module
  - aquifer_module
  - reservoir_module
  - time_module
  - recall_module
  - basin_module
calls:
  - gwflow_pump_allo
reads: []
writes: []
purpose: ""
---

# wallo_withdraw

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_withdraw.f90`
- **Modules used**: [[water_allocation_module.f90]], [[hydrograph_module.f90]], [[aquifer_module.f90]], [[reservoir_module.f90]], [[time_module.f90]], [[recall_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_pump_allo.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
