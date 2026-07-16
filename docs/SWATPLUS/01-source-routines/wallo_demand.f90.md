---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_demand.f90
note_file: wallo_demand.f90
subroutine: wallo_demand
module:
  - water_allocation_module
  - hru_module
  - hydrograph_module
  - conditional_module
  - recall_module
  - exco_module
calls:
  - conditions
  - actions
reads: []
writes: []
purpose: ""
---

# wallo_demand

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_demand.f90`
- **Modules used**: [[water_allocation_module.f90]], [[hru_module.f90]], [[hydrograph_module.f90]], [[conditional_module.f90]], [[recall_module.f90]], [[exco_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[conditions.f90]]
- [[actions.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
