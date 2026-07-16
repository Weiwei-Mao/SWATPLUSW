---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: smp_filter.f90
note_file: smp_filter.f90
subroutine: smp_filter
module:
  - basin_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - time_module
  - output_ls_pesticide_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - hru_module.f90#clayld
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#lagyld
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#sedminpa
  - hru_module.f90#sedminps
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#silyld
  - hru_module.f90#surfq
  - hru_module.f90#surqno3
  - hru_module.f90#surqsolp
  - output_ls_pesticide_module.f90#hpestb_d
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the reduction of pollutants in surface runoff; due to an edge of field filter or buffer strip"
---

# smp_filter

> [!info] Summary
> this subroutine calculates the reduction of pollutants in surface runoff; due to an edge of field filter or buffer strip

## Basic Information
- **Type**: `subroutine`
- **Source file**: `smp_filter.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[time_module.f90]]
  - [[output_ls_pesticide_module.f90]]
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
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminpa]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminps]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
