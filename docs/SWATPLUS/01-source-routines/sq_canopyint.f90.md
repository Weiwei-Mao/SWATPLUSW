---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_canopyint.f90
note_file: sq_canopyint.f90
subroutine: sq_canopyint
module:
  - basin_module
  - time_module
  - climate_module
  - hru_module
  - plant_module
  - hydrograph_module
calls: []
uses_variables:
  - climate_module.f90#w
  - climate_module.f90#wst
  - hru_module.f90#canstor
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#precip_eff
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ts
  - plant_module.f90#pcom
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes canopy interception of rainfall; used for methods other than curve number"
---

# sq_canopyint

> [!info] Summary
> this subroutine computes canopy interception of rainfall; used for methods other than curve number

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_canopyint.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[climate_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#canstor]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#precip_eff]] - `real`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[plant_module.f90#pcom]] - `plant_community`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
