---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: stor_surfstor.f90
note_file: stor_surfstor.f90
subroutine: stor_surfstor
module:
  - septic_data_module
  - basin_module
  - time_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - hru_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - hru_module.f90#brt
  - hru_module.f90#clayld
  - hru_module.f90#hhsedy
  - hru_module.f90#hhsurf_bs
  - hru_module.f90#ihru
  - hru_module.f90#lagyld
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#sedmcs
  - hru_module.f90#sedminpa
  - hru_module.f90#sedminps
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#silyld
  - hru_module.f90#surf_bs
  - hru_module.f90#surqcs
  - hru_module.f90#surqno3
  - hru_module.f90#surqsalt
  - hru_module.f90#surqsolp
  - hru_module.f90#urbqcs
  - hru_module.f90#urbqsalt
  - hru_module.f90#wetqcs
  - hru_module.f90#wetqsalt
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine stores and lags sediment and nutrients in surface runoff"
---

# stor_surfstor

> [!info] Summary
> this subroutine stores and lags sediment and nutrients in surface runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `stor_surfstor.f90`
- **Modules used**:
  - [[septic_data_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_ls_pesticide_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hru_module.f90#brt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hhsedy]] - `real, dimension(:,:), allocatable`
- [[hru_module.f90#hhsurf_bs]] - `real, dimension (:,:,:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedmcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#sedminpa]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminps]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surf_bs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#urbqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#urbqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wetqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wetqsalt]] - `real, dimension (:,:), allocatable`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
