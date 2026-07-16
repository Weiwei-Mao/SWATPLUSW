---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_urbanhr.f90
note_file: hru_urbanhr.f90
subroutine: hru_urbanhr
module:
  - hru_module
  - plant_module
  - urban_data_module
  - climate_module
  - time_module
calls:
  - hru_sweep
uses_variables:
  - hru_module.f90#etday
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#init_abstrc
  - hru_module.f90#ipl
  - hru_module.f90#isweep
  - hru_module.f90#luse
  - hru_module.f90#phubase
  - hru_module.f90#phusw
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#surfq
  - hru_module.f90#surqno3
  - hru_module.f90#surqsolp
  - hru_module.f90#twash
  - hru_module.f90#ubnrunoff
  - hru_module.f90#ubntss
  - hru_module.f90#ulu
  - plant_module.f90#pcom
  - time_module.f90#time
  - urban_data_module.f90#urbdb
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes loadings from urban areas using the; a build-up/wash-off algorithm at subdaily time intervals"
---

# hru_urbanhr

> [!info] Summary
> this subroutine computes loadings from urban areas using the; a build-up/wash-off algorithm at subdaily time intervals

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_urbanhr.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[urban_data_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[hru_sweep.f90]]

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#etday]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#init_abstrc]] - `real, dimension(:), allocatable`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#isweep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#phusw]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#twash]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ubnrunoff]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ubntss]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ulu]] - `integer`
- [[plant_module.f90#pcom]] - `plant_community`
- [[time_module.f90#time]] - `time_current`
- [[urban_data_module.f90#urbdb]] - `urban_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
