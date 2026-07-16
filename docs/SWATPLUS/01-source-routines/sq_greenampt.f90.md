---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_greenampt.f90
note_file: sq_greenampt.f90
subroutine: sq_greenampt
module:
  - urban_data_module
  - climate_module
  - basin_module
  - hydrograph_module
  - hru_module
  - soil_module
  - time_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - climate_module.f90#tmp
  - climate_module.f90#w
  - climate_module.f90#wst
  - hru_module.f90#cnday
  - hru_module.f90#hhqday
  - hru_module.f90#hhsurfq
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#luse
  - hru_module.f90#pet_day
  - hru_module.f90#rateinf_prev
  - hru_module.f90#smx
  - hru_module.f90#surfq
  - hru_module.f90#swtrg
  - hru_module.f90#ubnrunoff
  - hru_module.f90#ulu
  - hru_module.f90#urb_abstinit
  - hru_module.f90#wfsh
  - hru_module.f90#wrt
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ts
  - soil_module.f90#soil
  - time_module.f90#time
  - urban_data_module.f90#urbdb
input_variables: []
reads: []
writes: []
purpose: "Predicts daily runoff given breakpoint precipitation and snow melt; using the Green & Ampt technique"
---

# sq_greenampt

> [!info] Summary
> Predicts daily runoff given breakpoint precipitation and snow melt; using the Green & Ampt technique

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_greenampt.f90`
- **Modules used**:
  - [[urban_data_module.f90]]
  - [[climate_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[sq_volq.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#cnday]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hhqday]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hhsurfq]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#pet_day]] - `real`
- [[hru_module.f90#rateinf_prev]] - `real, dimension (:), allocatable`
- [[hru_module.f90#smx]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#swtrg]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ubnrunoff]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ulu]] - `integer`
- [[hru_module.f90#urb_abstinit]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wfsh]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wrt]] - `real, dimension (:,:), allocatable`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`
- [[urban_data_module.f90#urbdb]] - `urban_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
