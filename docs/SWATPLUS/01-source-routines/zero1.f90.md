---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: zero1.f90
note_file: zero1.f90
subroutine: zero1
module:
  - hru_module
calls: []
uses_variables:
  - hru_module.f90#bio_bod
  - hru_module.f90#biom
  - hru_module.f90#bz_perc
  - hru_module.f90#fcoli
  - hru_module.f90#i_sep
  - hru_module.f90#plqm
  - hru_module.f90#qstemm
  - hru_module.f90#rbiom
  - hru_module.f90#sep_tsincefail
  - hru_module.f90#sweepeff
  - hru_module.f90#swtrg
  - hru_module.f90#t_ov
  - hru_module.f90#tconc
  - hru_module.f90#usle_cfac
  - hru_module.f90#usle_eifac
  - hru_module.f90#wfsh
input_variables: []
reads: []
writes: []
purpose: "this subroutine initializes the values for some of the arrays"
---

# zero1

> [!info] Summary
> this subroutine initializes the values for some of the arrays

## Basic Information
- **Type**: `subroutine`
- **Source file**: `zero1.f90`
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
- [[hru_module.f90#bio_bod]] - `real, dimension (:), allocatable`
- [[hru_module.f90#biom]] - `real, dimension (:), allocatable`
- [[hru_module.f90#bz_perc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#fcoli]] - `real, dimension (:), allocatable`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#plqm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qstemm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#rbiom]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sep_tsincefail]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#sweepeff]] - `real`
- [[hru_module.f90#swtrg]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#t_ov]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#usle_cfac]] - `real, dimension (:), allocatable`
- [[hru_module.f90#usle_eifac]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wfsh]] - `real, dimension (:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
