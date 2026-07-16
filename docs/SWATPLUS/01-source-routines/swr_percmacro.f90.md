---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_percmacro.f90
note_file: swr_percmacro.f90
subroutine: swr_percmacro
module:
  - hru_module
  - soil_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hru_module.f90#inflpcp
  - hru_module.f90#sepbtm
  - hru_module.f90#sepcrk
  - hru_module.f90#sepcrktot
  - hru_module.f90#volcrmin
  - hru_module.f90#voltot
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this surboutine computes percolation by crack flow"
---

# swr_percmacro

> [!info] Summary
> this surboutine computes percolation by crack flow

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_percmacro.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[swr_percmain.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#inflpcp]] - `real`
- [[hru_module.f90#sepbtm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sepcrk]] - `real`
- [[hru_module.f90#sepcrktot]] - `real`
- [[hru_module.f90#volcrmin]] - `real`
- [[hru_module.f90#voltot]] - `real`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
