---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: et_pot.f90
note_file: et_pot.f90
subroutine: et_pot
module:
  - plant_data_module
  - basin_module
  - hydrograph_module
  - climate_module
  - hru_module
  - plant_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - climate_module.f90#co2y
  - climate_module.f90#w
  - climate_module.f90#wst
  - hru_module.f90#albday
  - hru_module.f90#ep_max
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#pet_day
  - hru_module.f90#vpd
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - plant_data_module.f90#plcp
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates potential evapotranspiration using one; of three methods. If Penman-Monteith is being used, potential plant; transpiration is also calculated."
---

# et_pot

> [!info] Summary
> this subroutine calculates potential evapotranspiration using one; of three methods. If Penman-Monteith is being used, potential plant; transpiration is also calculated.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `et_pot.f90`
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
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
- [[climate_module.f90#co2y]] - `real, dimension(:), allocatable`
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#albday]] - `real`
- [[hru_module.f90#ep_max]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#pet_day]] - `real`
- [[hru_module.f90#vpd]] - `real`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[plant_data_module.f90#plcp]] - `plant_cp`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
