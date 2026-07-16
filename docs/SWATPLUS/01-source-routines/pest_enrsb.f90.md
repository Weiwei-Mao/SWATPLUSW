---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_enrsb.f90
note_file: pest_enrsb.f90
subroutine: pest_enrsb
module:
  - hru_module
calls: []
uses_variables:
  - hru_module.f90#clayld
  - hru_module.f90#enratio
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#lagyld
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#sedyld
  - hru_module.f90#silyld
  - hru_module.f90#surfq
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the enrichment ratio for nutrient and; pesticide transport with runoff"
---

# pest_enrsb

> [!info] Summary
> this subroutine calculates the enrichment ratio for nutrient and; pesticide transport with runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_enrsb.f90`
- **Modules used**:
  - [[hru_module.f90]]
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
- [[hru_module.f90#enratio]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
