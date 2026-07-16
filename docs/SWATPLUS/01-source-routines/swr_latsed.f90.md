---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_latsed.f90
note_file: swr_latsed.f90
subroutine: swr_latsed
module:
  - hru_module
  - soil_module
calls: []
uses_variables:
  - hru_module.f90#clayld
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#lagyld
  - hru_module.f90#latq
  - hru_module.f90#qtile
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#silyld
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the sediment load contributed in lateral flow"
---

# swr_latsed

> [!info] Summary
> this subroutine calculates the sediment load contributed in lateral flow

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_latsed.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
