---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_nrain.f90
note_file: nut_nrain.f90
subroutine: nut_nrain
module:
  - basin_module
  - organic_mineral_mass_module
  - hydrograph_module
  - hru_module
  - climate_module
  - output_landscape_module
calls: []
uses_variables:
  - climate_module.f90#atmodep
  - climate_module.f90#atmodep_cont
  - climate_module.f90#w
  - climate_module.f90#wst
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#mo
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ts
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hnb_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine adds nitrate from rainfall to the soil profile"
---

# nut_nrain

> [!info] Summary
> this subroutine adds nitrate from rainfall to the soil profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_nrain.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[climate_module.f90]]
  - [[output_landscape_module.f90]]
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
- [[climate_module.f90#atmodep]] - `atmospheric_deposition`
- [[climate_module.f90#atmodep_cont]] - `atmospheric_deposition_control`
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
