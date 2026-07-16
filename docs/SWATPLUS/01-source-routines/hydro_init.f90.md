---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hydro_init.f90
note_file: hydro_init.f90
subroutine: hydro_init
module:
  - hru_module
  - soil_module
  - plant_module
  - climate_module
  - plant_data_module
  - pesticide_data_module
  - basin_module
  - channel_module
  - time_module
  - organic_mineral_mass_module
  - hydrograph_module
  - constituent_mass_module
  - output_landscape_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - climate_module.f90#tmp
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - climate_module.f90#wst
  - hru_module.f90#dormhr
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#sdr
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - plant_module.f90#pcom
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "This subroutine computes variables related to the watershed hydrology:; the time of concentration for the subbasins, lagged surface runoff,; the coefficient for the peak runoff rate equation, and lateral flow travel"
---

# hydro_init

> [!info] Summary
> This subroutine computes variables related to the watershed hydrology:; the time of concentration for the subbasins, lagged surface runoff,; the coefficient for the peak runoff rate equation, and lateral flow travel

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hydro_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[climate_module.f90]]
  - [[plant_data_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[basin_module.f90]]
  - [[channel_module.f90]]
  - [[time_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#dormhr]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#sdr]] - `subsurface_drainage_parameters`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
