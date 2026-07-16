---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_seed_gro.f90
note_file: pl_seed_gro.f90
subroutine: pl_seed_gro
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
  - climate_module
  - hydrograph_module
calls: []
uses_variables:
  - climate_module.f90#wst
  - hru_module.f90#ep_day
  - hru_module.f90#ipl
  - hru_module.f90#pet_day
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: ""
---

# pl_seed_gro

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_seed_gro.f90`
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[carbon_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[mgt_transplant.f90]]
- [[pl_grow.f90]]
- [[plant_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#ep_day]] - `real`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#pet_day]] - `real`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
