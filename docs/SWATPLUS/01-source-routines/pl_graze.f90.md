---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_graze.f90
note_file: pl_graze.f90
subroutine: pl_graze
module:
  - mgt_operations_module
  - fertilizer_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - carbon_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - fertilizer_data_module.f90#fertdb
  - hru_module.f90#grazn
  - hru_module.f90#grazp
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - mgt_operations_module.f90#graze
  - organic_mineral_mass_module.f90#manure
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: ""
---

# pl_graze

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_graze.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[carbon_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[actions.f90]]
- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[fertilizer_data_module.f90#fertdb]] - `fertilizer_db`
- [[hru_module.f90#grazn]] - `real`
- [[hru_module.f90#grazp]] - `real`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[mgt_operations_module.f90#graze]] - `grazing_operation`
- [[organic_mineral_mass_module.f90#manure]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
