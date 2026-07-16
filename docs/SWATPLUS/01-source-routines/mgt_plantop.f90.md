---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_plantop.f90
note_file: mgt_plantop.f90
subroutine: mgt_plantop
module:
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - organic_mineral_mass_module.f90#orgz
  - organic_mineral_mass_module.f90#pl_mass
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - plant_module.f90#plstrz
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine performs the plant operation"
---

# mgt_plantop

> [!info] Summary
> this subroutine performs the plant operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_plantop.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[mgt_sched.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[organic_mineral_mass_module.f90#orgz]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[plant_module.f90#plstrz]] - `plant_stress`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
