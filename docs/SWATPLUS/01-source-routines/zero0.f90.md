---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: zero0.f90
note_file: zero0.f90
subroutine: zero0
module:
  - hru_module
calls: []
uses_variables:
  - hru_module.f90#brt
  - hru_module.f90#bss
  - hru_module.f90#canstor
  - hru_module.f90#cn2
  - hru_module.f90#cumei
  - hru_module.f90#cumeira
  - hru_module.f90#cumrai
  - hru_module.f90#cumrt
  - hru_module.f90#dormhr
  - hru_module.f90#filterw
  - hru_module.f90#grz_days
  - hru_module.f90#igrz
  - hru_module.f90#isep_ly
  - hru_module.f90#iseptic
  - hru_module.f90#itb
  - hru_module.f90#latno3
  - hru_module.f90#orgn_con
  - hru_module.f90#orgp_con
  - hru_module.f90#phubase
  - hru_module.f90#ranrns_hru
  - hru_module.f90#rateinf_prev
  - hru_module.f90#sed_con
  - hru_module.f90#sepcrk
  - hru_module.f90#sol_sumsolp
  - hru_module.f90#soln_con
  - hru_module.f90#solp_con
  - hru_module.f90#sstmaxd
  - hru_module.f90#stmaxd
  - hru_module.f90#urb_abstinit
  - hru_module.f90#wt_shall
  - hru_module.f90#yr_skip
input_variables: []
reads: []
writes: []
purpose: "this subroutine initializes the values for some of the arrays"
---

# zero0

> [!info] Summary
> this subroutine initializes the values for some of the arrays

## Basic Information
- **Type**: `subroutine`
- **Source file**: `zero0.f90`
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
- [[hru_module.f90#brt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#bss]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#canstor]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumei]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumeira]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumrai]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumrt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#dormhr]] - `real, dimension (:), allocatable`
- [[hru_module.f90#filterw]] - `real, dimension (:), allocatable`
- [[hru_module.f90#grz_days]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#igrz]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#isep_ly]] - `integer`
- [[hru_module.f90#iseptic]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#itb]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#latno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#orgn_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#orgp_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ranrns_hru]] - `real, dimension (:), allocatable`
- [[hru_module.f90#rateinf_prev]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sed_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sepcrk]] - `real`
- [[hru_module.f90#sol_sumsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#soln_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#solp_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sstmaxd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#stmaxd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#urb_abstinit]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wt_shall]] - `real`
- [[hru_module.f90#yr_skip]] - `integer, dimension (:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
