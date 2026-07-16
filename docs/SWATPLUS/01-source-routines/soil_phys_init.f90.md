---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_phys_init.f90
note_file: soil_phys_init.f90
subroutine: soil_phys_init
module:
  - soil_module
  - basin_module
  - time_module
calls: []
uses_variables:
  - soil_module.f90#sol
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine initializes soil physical properties"
---

# soil_phys_init

> [!info] Summary
> this subroutine initializes soil physical properties

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_phys_init.f90`
- **Modules used**:
  - [[soil_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[soils_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[soil_module.f90#sol]] - `soil_hru_database`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
