---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_rootfr.f90
note_file: pl_rootfr.f90
subroutine: pl_rootfr
module:
  - hru_module
  - soil_module
  - plant_module
calls: []
uses_variables:
  - hru_module.f90#ipl
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: ""
---

# pl_rootfr

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_rootfr.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[mgt_harvtuber.f90]]
- [[mgt_killop.f90]]
- [[pl_root_gro.f90]]
- [[plant_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ipl]] - `integer`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
