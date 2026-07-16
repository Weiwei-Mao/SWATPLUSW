---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_sweep.f90
note_file: hru_sweep.f90
subroutine: hru_sweep
module:
  - hru_module
  - urban_data_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hru_module.f90#sweepeff
  - hru_module.f90#twash
  - hru_module.f90#ulu
  - urban_data_module.f90#urbdb
input_variables: []
reads: []
writes: []
purpose: "the subroutine performs the street sweeping operation"
---

# hru_sweep

> [!info] Summary
> the subroutine performs the street sweeping operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_sweep.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[urban_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hru_urbanhr.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#sweepeff]] - `real`
- [[hru_module.f90#twash]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ulu]] - `integer`
- [[urban_data_module.f90#urbdb]] - `urban_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
