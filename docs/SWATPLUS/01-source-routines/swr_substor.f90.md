---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_substor.f90
note_file: swr_substor.f90
subroutine: swr_substor
module:
  - pesticide_data_module
  - hru_module
  - constituent_mass_module
  - output_ls_pesticide_module
calls: []
uses_variables:
  - hru_module.f90#bss
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#latno3
  - hru_module.f90#latq
  - hru_module.f90#qtile
  - hru_module.f90#tileno3
input_variables: []
reads: []
writes: []
purpose: "this subroutine stores and lags lateral soil flow and nitrate"
---

# swr_substor

> [!info] Summary
> this subroutine stores and lags lateral soil flow and nitrate

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_substor.f90`
- **Modules used**:
  - [[pesticide_data_module.f90]]
  - [[hru_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[hru_module.f90#bss]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#latno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#tileno3]] - `real, dimension (:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
