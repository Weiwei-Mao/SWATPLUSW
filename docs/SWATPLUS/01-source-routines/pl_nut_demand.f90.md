---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_nut_demand.f90
note_file: pl_nut_demand.f90
subroutine: pl_nut_demand
module:
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
  - climate_module
calls:
  - pl_nupd
  - pl_pupd
uses_variables:
  - climate_module.f90#w
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#sum_no3
  - hru_module.f90#sum_solp
  - hru_module.f90#uapd
  - hru_module.f90#uapd_tot
  - hru_module.f90#uno3d
  - hru_module.f90#uno3d_tot
  - organic_mineral_mass_module.f90#soil1
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine predicts daily potential growth of total plant; biomass and roots and calculates leaf area index. Incorporates; residue for tillage functions and decays residue on ground"
---

# pl_nut_demand

> [!info] Summary
> this subroutine predicts daily potential growth of total plant; biomass and roots and calculates leaf area index. Incorporates; residue for tillage functions and decays residue on ground

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_nut_demand.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_nupd.f90]]
- [[pl_pupd.f90]]

**Called by:**

- [[pl_grow.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#sum_no3]] - `real`
- [[hru_module.f90#sum_solp]] - `real`
- [[hru_module.f90#uapd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uapd_tot]] - `real`
- [[hru_module.f90#uno3d]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uno3d_tot]] - `real`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
