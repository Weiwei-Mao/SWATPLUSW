---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_ovrsed.f90
note_file: ero_ovrsed.f90
subroutine: ero_ovrsed
module:
  - urban_data_module
  - basin_module
  - climate_module
  - time_module
  - hydrograph_module
  - hru_module
  - soil_module
  - plant_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - climate_module.f90#wst
  - hru_module.f90#cvm_com
  - hru_module.f90#hhqday
  - hru_module.f90#hhsedy
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#luse
  - hru_module.f90#ulu
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ts
  - organic_mineral_mass_module.f90#pl_mass
  - plant_module.f90#pcom
  - soil_module.f90#soil
  - time_module.f90#time
  - urban_data_module.f90#urbdb
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes splash erosion by raindrop impact and flow erosion by overland flow"
---

# ero_ovrsed

> [!info] Summary
> this subroutine computes splash erosion by raindrop impact and flow erosion by overland flow

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_ovrsed.f90`
- **Modules used**:
  - [[urban_data_module.f90]]
  - [[basin_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[surface.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#cvm_com]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hhqday]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hhsedy]] - `real, dimension(:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#ulu]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`
- [[urban_data_module.f90#urbdb]] - `urban_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
