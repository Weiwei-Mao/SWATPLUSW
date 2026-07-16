---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_community.f90
note_file: pl_community.f90
subroutine: pl_community
module:
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
  - time_module
  - climate_module
calls:
  - pl_waterup
uses_variables:
  - climate_module.f90#w
  - hru_module.f90#ep_max
  - hru_module.f90#epmax
  - hru_module.f90#htfac
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#par
  - hru_module.f90#translt
  - organic_mineral_mass_module.f90#orgz
  - organic_mineral_mass_module.f90#pl_mass
  - plant_data_module.f90#pl_db
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine predicts daily potential growth of total plant; biomass and roots and calculates leaf area index. Incorporates; residue for tillage functions and decays residue on ground"
---

# pl_community

> [!info] Summary
> this subroutine predicts daily potential growth of total plant; biomass and roots and calculates leaf area index. Incorporates; residue for tillage functions and decays residue on ground

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_community.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[time_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_waterup.f90]]

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[hru_module.f90#ep_max]] - `real`
- [[hru_module.f90#epmax]] - `real, dimension (:), allocatable`
- [[hru_module.f90#htfac]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#par]] - `real, dimension (:), allocatable`
- [[hru_module.f90#translt]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#orgz]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_data_module.f90#pl_db]] - `plant_db`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
