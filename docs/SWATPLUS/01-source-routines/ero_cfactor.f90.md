---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_cfactor.f90
note_file: ero_cfactor.f90
subroutine: ero_cfactor
module:
  - basin_module
  - hru_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
  - time_module
  - erosion_module
  - utils
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - erosion_module.f90#ero_output
  - hru_module.f90#cvm_com
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#usle_cfac
  - organic_mineral_mass_module.f90#pl_mass
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine predicts daily soil loss caused by water erosion; using the modified universal soil loss equation"
---

# ero_cfactor

> [!info] Summary
> this subroutine predicts daily soil loss caused by water erosion; using the modified universal soil loss equation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_cfactor.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[time_module.f90]]
  - [[erosion_module.f90]]
  - [[utils.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[surface.f90]]
- [[wetland_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[erosion_module.f90#ero_output]] - `erosion_output`
- [[hru_module.f90#cvm_com]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#usle_cfac]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
