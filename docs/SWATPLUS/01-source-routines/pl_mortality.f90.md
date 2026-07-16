---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_mortality.f90
note_file: pl_mortality.f90
subroutine: pl_mortality
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
  - soil_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: ""
---

# pl_mortality

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_mortality.f90`
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[carbon_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[soil_module.f90]]
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
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
