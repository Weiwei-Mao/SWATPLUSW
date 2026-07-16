---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_percmain.f90
note_file: swr_percmain.f90
subroutine: swr_percmain
module:
  - hru_module
  - soil_module
  - septic_data_module
  - hydrograph_module
  - basin_module
calls:
  - gwflow_soil
  - swr_percmacro
  - swr_percmicro
  - swr_satexcess
  - swr_drains
  - swr_origtile
uses_variables:
  - basin_module.f90#bsn_cc
  - hru_module.f90#hru
  - hru_module.f90#i_sep
  - hru_module.f90#ihru
  - hru_module.f90#inflpcp
  - hru_module.f90#isep
  - hru_module.f90#latlyr
  - hru_module.f90#latq
  - hru_module.f90#lyrtile
  - hru_module.f90#qstemm
  - hru_module.f90#qtile
  - hru_module.f90#sepbtm
  - hru_module.f90#sepcrktot
  - hru_module.f90#sepday
  - hru_module.f90#sw_excess
  - hru_module.f90#wt_shall
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#irrig
  - septic_data_module.f90#sep
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine is the master soil percolation component."
---

# swr_percmain

> [!info] Summary
> this subroutine is the master soil percolation component.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_percmain.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[septic_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 6 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_soil.f90]]
- [[swr_percmacro.f90]]
- [[swr_percmicro.f90]]
- [[swr_satexcess.f90]]
- [[swr_drains.f90]]
- [[swr_origtile.f90]]

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#inflpcp]] - `real`
- [[hru_module.f90#isep]] - `integer`
- [[hru_module.f90#latlyr]] - `real`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#lyrtile]] - `real`
- [[hru_module.f90#qstemm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#sepbtm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sepcrktot]] - `real`
- [[hru_module.f90#sepday]] - `real`
- [[hru_module.f90#sw_excess]] - `real`
- [[hru_module.f90#wt_shall]] - `real`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[septic_data_module.f90#sep]] - `septic_system`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
