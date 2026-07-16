---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_cs.f90
note_file: wet_cs.f90
subroutine: wet_cs
module:
  - reservoir_data_module
  - reservoir_module
  - water_body_module
  - hydrograph_module
  - hru_module
  - constituent_mass_module
  - res_cs_module
  - climate_module
  - cs_data_module
calls: []
uses_variables:
  - climate_module.f90#wst
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - constituent_mass_module.f90#obcs
  - constituent_mass_module.f90#wet_water
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#wetqcs
  - hru_module.f90#wtspcs
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#wet
  - res_cs_module.f90#res_cs_data
  - res_cs_module.f90#wetcs_d
  - water_body_module.f90#wet_wat_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes the wetland constituent mass balance"
---

# wet_cs

> [!info] Summary
> this subroutine computes the wetland constituent mass balance

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_cs.f90`
- **Modules used**:
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[water_body_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[res_cs_module.f90]]
  - [[climate_module.f90]]
  - [[cs_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[wetland_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wst]] - `weather_station`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#wet_water]] - `constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#wetqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wtspcs]] - `real, dimension (:,:), allocatable`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[res_cs_module.f90#res_cs_data]] - `reservoir_cs_data`
- [[res_cs_module.f90#wetcs_d]] - `res_cs_output`
- [[water_body_module.f90#wet_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
