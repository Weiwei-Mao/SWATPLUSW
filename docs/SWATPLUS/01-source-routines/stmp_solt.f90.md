---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: stmp_solt.f90
note_file: stmp_solt.f90
subroutine: stmp_solt
module:
  - climate_module
  - septic_data_module
  - hru_module
  - soil_module
  - time_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - climate_module.f90#tmp
  - climate_module.f90#w
  - climate_module.f90#wgn_pms
  - hru_module.f90#albday
  - hru_module.f90#hru
  - hru_module.f90#i_sep
  - hru_module.f90#ihru
  - hru_module.f90#isep
  - hru_module.f90#iseptic
  - hru_module.f90#iwgen
  - organic_mineral_mass_module.f90#pl_mass
  - septic_data_module.f90#sep
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine estimates daily average temperature at the bottom; of each soil layer"
---

# stmp_solt

> [!info] Summary
> this subroutine estimates daily average temperature at the bottom; of each soil layer

## Basic Information
- **Type**: `subroutine`
- **Source file**: `stmp_solt.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[septic_data_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[time_module.f90]]
  - [[organic_mineral_mass_module.f90]]
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
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[hru_module.f90#albday]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isep]] - `integer`
- [[hru_module.f90#iseptic]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#iwgen]] - `integer`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[septic_data_module.f90#sep]] - `septic_system`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
