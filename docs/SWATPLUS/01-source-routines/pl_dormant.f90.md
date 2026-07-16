---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_dormant.f90
note_file: pl_dormant.f90
subroutine: pl_dormant
module:
  - climate_module
  - hydrograph_module
  - plant_data_module
  - organic_mineral_mass_module
  - hru_module
  - plant_module
calls: []
uses_variables:
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - climate_module.f90#wst
  - hru_module.f90#dormhr
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - organic_mineral_mass_module.f90#abgr_drop
  - organic_mineral_mass_module.f90#leaf_drop
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#plt_mass_z
  - organic_mineral_mass_module.f90#seed_drop
  - organic_mineral_mass_module.f90#stem_drop
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine checks the dormant status of the different plant types"
---

# pl_dormant

> [!info] Summary
> this subroutine checks the dormant status of the different plant types

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_dormant.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
  - [[plant_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[pl_grow.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#dormhr]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[organic_mineral_mass_module.f90#abgr_drop]] - `organic_mass`
- [[organic_mineral_mass_module.f90#leaf_drop]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#plt_mass_z]] - `organic_mass`
- [[organic_mineral_mass_module.f90#seed_drop]] - `organic_mass`
- [[organic_mineral_mass_module.f90#stem_drop]] - `organic_mass`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
