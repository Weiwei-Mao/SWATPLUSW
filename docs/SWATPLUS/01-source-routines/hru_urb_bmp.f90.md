---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_urb_bmp.f90
note_file: hru_urb_bmp.f90
subroutine: hru_urb_bmp
module:
  - hru_module
calls: []
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#latno3
  - hru_module.f90#orgn_con
  - hru_module.f90#orgp_con
  - hru_module.f90#qdr
  - hru_module.f90#sed_con
  - hru_module.f90#sedminpa
  - hru_module.f90#sedminps
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#soln_con
  - hru_module.f90#solp_con
  - hru_module.f90#surqno3
  - hru_module.f90#surqsolp
input_variables: []
reads: []
writes: []
purpose: ""
---

# hru_urb_bmp

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_urb_bmp.f90`
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
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#latno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#orgn_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#orgp_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qdr]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sed_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminpa]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminps]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#soln_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#solp_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
