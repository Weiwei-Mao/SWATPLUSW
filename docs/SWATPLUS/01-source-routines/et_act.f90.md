---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: et_act.f90
note_file: et_act.f90
subroutine: et_act
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - climate_module
  - hydrograph_module
  - water_body_module
  - reservoir_data_module
calls: []
uses_variables:
  - climate_module.f90#w
  - hru_module.f90#canev
  - hru_module.f90#canstor
  - hru_module.f90#ep_max
  - hru_module.f90#es_day
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#pet_day
  - hru_module.f90#snoev
  - hydrograph_module.f90#wet
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - plant_module.f90#pcom
  - reservoir_data_module.f90#wet_dat
  - reservoir_data_module.f90#wet_hyd
  - soil_module.f90#soil
  - water_body_module.f90#wet_wat_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates potential plant transpiration for Priestley-; Taylor and Hargreaves ET methods, and potential and actual soil; evaporation. NO3 movement into surface soil layer due to evaporation"
---

# et_act

> [!info] Summary
> this subroutine calculates potential plant transpiration for Priestley-; Taylor and Hargreaves ET methods, and potential and actual soil; evaporation. NO3 movement into surface soil layer due to evaporation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `et_act.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
  - [[water_body_module.f90]]
  - [[reservoir_data_module.f90]]
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
- [[hru_module.f90#canev]] - `real`
- [[hru_module.f90#canstor]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ep_max]] - `real`
- [[hru_module.f90#es_day]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#pet_day]] - `real`
- [[hru_module.f90#snoev]] - `real`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[reservoir_data_module.f90#wet_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#wet_hyd]] - `wetland_hyd_data`
- [[soil_module.f90#soil]] - `soil_profile`
- [[water_body_module.f90#wet_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
