---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_leaf_gro.f90
note_file: pl_leaf_gro.f90
subroutine: pl_leaf_gro
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - plant_data_module.f90#plcp
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine adjusts plant biomass, leaf area index, and canopy height; taking into account the effect of water, temperature and nutrient stresses; on the plant"
---

# pl_leaf_gro

> [!info] Summary
> this subroutine adjusts plant biomass, leaf area index, and canopy height; taking into account the effect of water, temperature and nutrient stresses; on the plant

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_leaf_gro.f90`
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

- [[pl_grow.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[plant_data_module.f90#plcp]] - `plant_cp`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
