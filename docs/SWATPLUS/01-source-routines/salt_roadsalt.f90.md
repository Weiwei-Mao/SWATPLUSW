---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_roadsalt.f90
note_file: salt_roadsalt.f90
subroutine: salt_roadsalt
module:
  - basin_module
  - organic_mineral_mass_module
  - hydrograph_module
  - hru_module
  - climate_module
  - output_landscape_module
  - salt_module
  - constituent_mass_module
calls: []
uses_variables:
  - climate_module.f90#atmodep
  - climate_module.f90#atmodep_cont
  - climate_module.f90#rdapp_salt
  - climate_module.f90#wst
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#mo
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ts
  - salt_module.f90#hsaltb_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine adds salt from applied road salt to the soil profile"
---

# salt_roadsalt

> [!info] Summary
> this subroutine adds salt from applied road salt to the soil profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_roadsalt.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[climate_module.f90]]
  - [[output_landscape_module.f90]]
  - [[salt_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[climate_module.f90#rdapp_salt]] - `object_road_salt`
- [[climate_module.f90#wst]] - `weather_station`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[salt_module.f90#hsaltb_d]] - `object_salt_balance`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
