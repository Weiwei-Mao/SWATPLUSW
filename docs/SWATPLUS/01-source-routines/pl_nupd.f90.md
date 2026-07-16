---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_nupd.f90
note_file: pl_nupd.f90
subroutine: pl_nupd
module:
  - plant_data_module
  - hru_module
  - plant_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#un2
  - hru_module.f90#uno3d
  - organic_mineral_mass_module.f90#pl_mass
  - plant_data_module.f90#plcp
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "This subroutine calculates plant nitrogen demand"
---

# pl_nupd

> [!info] Summary
> This subroutine calculates plant nitrogen demand

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_nupd.f90`
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[pl_nut_demand.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#un2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uno3d]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_data_module.f90#plcp]] - `plant_cp`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
