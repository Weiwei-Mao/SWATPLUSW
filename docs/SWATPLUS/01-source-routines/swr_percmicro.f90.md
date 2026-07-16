---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_percmicro.f90
note_file: swr_percmicro.f90
subroutine: swr_percmicro
module:
  - septic_data_module
  - hru_module
  - soil_module
calls: []
uses_variables:
  - hru_module.f90#bz_perc
  - hru_module.f90#hru
  - hru_module.f90#i_sep
  - hru_module.f90#ihru
  - hru_module.f90#isep
  - hru_module.f90#latlyr
  - hru_module.f90#lyrtile
  - hru_module.f90#sepday
  - hru_module.f90#sw_excess
  - septic_data_module.f90#sep
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes percolation and lateral subsurface flow; from a soil layer when field capacity is exceeded"
---

# swr_percmicro

> [!info] Summary
> this subroutine computes percolation and lateral subsurface flow; from a soil layer when field capacity is exceeded

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_percmicro.f90`
- **Modules used**:
  - [[septic_data_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[swr_percmain.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#bz_perc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isep]] - `integer`
- [[hru_module.f90#latlyr]] - `real`
- [[hru_module.f90#lyrtile]] - `real`
- [[hru_module.f90#sepday]] - `real`
- [[hru_module.f90#sw_excess]] - `real`
- [[septic_data_module.f90#sep]] - `septic_system`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
