---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_drains.f90
note_file: swr_drains.f90
subroutine: swr_drains
module:
  - basin_module
  - hydrograph_module
  - hru_module
  - soil_module
  - time_module
  - reservoir_module
calls:
  - swr_depstor
uses_variables:
  - hru_module.f90#etday
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#inflpcp
  - hru_module.f90#precip_eff
  - hru_module.f90#qtile
  - hru_module.f90#sdr
  - hru_module.f90#stmaxd
  - hru_module.f90#surfq
  - hru_module.f90#wnan
  - hru_module.f90#wt_shall
  - hydrograph_module.f90#wet
  - reservoir_module.f90#wet_ob
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine finds the effective lateral hydraulic conductivity; and computes drainage or subirrigation flux"
---

# swr_drains

> [!info] Summary
> this subroutine finds the effective lateral hydraulic conductivity; and computes drainage or subirrigation flux

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_drains.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[time_module.f90]]
  - [[reservoir_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[swr_depstor.f90]]

**Called by:**

- [[swr_percmain.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#etday]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#inflpcp]] - `real`
- [[hru_module.f90#precip_eff]] - `real`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#sdr]] - `subsurface_drainage_parameters`
- [[hru_module.f90#stmaxd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wnan]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wt_shall]] - `real`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
