---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mallo_control.f90
note_file: mallo_control.f90
subroutine: mallo_control
module:
  - manure_allocation_module
  - hru_module
  - basin_module
  - time_module
  - plant_module
  - soil_module
  - organic_mineral_mass_module
  - conditional_module
calls:
  - conditions
  - actions
  - pl_fert
reads: []
writes: []
purpose: ""
---

# mallo_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mallo_control.f90`
- **Modules used**: [[manure_allocation_module.f90]], [[hru_module.f90]], [[basin_module.f90]], [[time_module.f90]], [[plant_module.f90]], [[soil_module.f90]], [[organic_mineral_mass_module.f90]], [[conditional_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[conditions.f90]]
- [[actions.f90]]
- [[pl_fert.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
