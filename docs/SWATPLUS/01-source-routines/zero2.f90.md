---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: zero2.f90
note_file: zero2.f90
subroutine: zero2
module:
  - hru_module
calls: []
uses_variables:
  - hru_module.f90#bss_ex
  - hru_module.f90#cklsp
  - hru_module.f90#clayld
  - hru_module.f90#lagyld
  - hru_module.f90#ovrlnd
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#sedyld
  - hru_module.f90#silyld
  - hru_module.f90#smx
  - hru_module.f90#surf_bs
  - hru_module.f90#twash
  - hru_module.f90#wrt
input_variables: []
reads: []
writes: []
purpose: "this subroutine zeros all array values"
---

# zero2

> [!info] Summary
> this subroutine zeros all array values

## Basic Information
- **Type**: `subroutine`
- **Source file**: `zero2.f90`
- **Modules used**:
  - [[hru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[allocate_parms.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#bss_ex]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#cklsp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ovrlnd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#smx]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surf_bs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#twash]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wrt]] - `real, dimension (:,:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
