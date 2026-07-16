---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_dailycn.f90
note_file: sq_dailycn.f90
subroutine: sq_dailycn
module:
  - basin_module
  - hru_module
  - soil_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - hru_module.f90#cnday
  - hru_module.f90#ihru
  - hru_module.f90#smx
  - hru_module.f90#wrt
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "Calculates curve number for the day in the HRU"
---

# sq_dailycn

> [!info] Summary
> Calculates curve number for the day in the HRU

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_dailycn.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
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
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[hru_module.f90#cnday]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#smx]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wrt]] - `real, dimension (:,:), allocatable`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
