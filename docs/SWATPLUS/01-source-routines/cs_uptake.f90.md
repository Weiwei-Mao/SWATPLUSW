---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_uptake.f90
note_file: cs_uptake.f90
subroutine: cs_uptake
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - hydrograph_module
  - output_landscape_module
  - cs_module
  - constituent_mass_module
  - plant_data_module
  - plant_module
  - soil_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - cs_module.f90#cs_uptake_kg
  - cs_module.f90#hcsb_d
  - hru_module.f90#ihru
  - hydrograph_module.f90#ob
  - organic_mineral_mass_module.f90#pl_mass
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine simulates constituent uptake in the root zone"
---

# cs_uptake

> [!info] Summary
> this subroutine simulates constituent uptake in the root zone

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_uptake.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_landscape_module.f90]]
  - [[cs_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[plant_data_module.f90]]
  - [[plant_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[pl_biomass_gro.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[cs_module.f90#cs_uptake_kg]] - `real, dimension(:,:), allocatable`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
