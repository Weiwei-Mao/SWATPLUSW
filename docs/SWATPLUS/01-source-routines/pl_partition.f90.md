---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_partition.f90
note_file: pl_partition.f90
subroutine: pl_partition
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - hru_module.f90#ipl
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#pl_mass_up
  - plant_data_module.f90#pldb
  - plant_module.f90#c_frac
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: ""
---

# pl_partition

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_partition.f90`
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[carbon_module.f90]]
  - [[organic_mineral_mass_module.f90]]
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
- [[hru_module.f90#ipl]] - `integer`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#pl_mass_up]] - `organic_mass`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#c_frac]] - `plant_carbon`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
