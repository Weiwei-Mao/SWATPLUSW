---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_subwq.f90
note_file: swr_subwq.f90
subroutine: swr_subwq
module:
  - basin_module
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - carbon_module
  - climate_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - carbon_module.f90#hsc_d
  - climate_module.f90#w
  - hru_module.f90#cbodu
  - hru_module.f90#chl_a
  - hru_module.f90#doxq
  - hru_module.f90#enratio
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#qdr
  - hru_module.f90#sedorgn
  - hru_module.f90#sedyld
  - hru_module.f90#surqno3
  - organic_mineral_mass_module.f90#soil1
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes HRU loadings of chlorophyll-a, CBOD,; and dissolved oxygen to the main channel"
---

# swr_subwq

> [!info] Summary
> this subroutine computes HRU loadings of chlorophyll-a, CBOD,; and dissolved oxygen to the main channel

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_subwq.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[carbon_module.f90]]
  - [[climate_module.f90]]
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
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[carbon_module.f90#hsc_d]] - `carbon_soil_gain_losses`
- [[climate_module.f90#w]] - `weather_daily`
- [[hru_module.f90#cbodu]] - `real, dimension (:), allocatable`
- [[hru_module.f90#chl_a]] - `real, dimension (:), allocatable`
- [[hru_module.f90#doxq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#enratio]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#qdr]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
