---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_ysed.f90
note_file: ero_ysed.f90
subroutine: ero_ysed
module:
  - hru_module
  - soil_module
  - erosion_module
  - climate_module
calls: []
uses_variables:
  - climate_module.f90#w
  - erosion_module.f90#ero_output
  - hru_module.f90#cklsp
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#qp_cms
  - hru_module.f90#sedyld
  - hru_module.f90#surfq
  - hru_module.f90#usle
  - hru_module.f90#usle_cfac
  - hru_module.f90#usle_ei
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine predicts daily soil loss caused by water erosion; using the modified universal soil loss equation"
---

# ero_ysed

> [!info] Summary
> this subroutine predicts daily soil loss caused by water erosion; using the modified universal soil loss equation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_ysed.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[erosion_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[surface.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[erosion_module.f90#ero_output]] - `erosion_output`
- [[hru_module.f90#cklsp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#qp_cms]] - `real`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#usle]] - `real`
- [[hru_module.f90#usle_cfac]] - `real, dimension (:), allocatable`
- [[hru_module.f90#usle_ei]] - `real`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
