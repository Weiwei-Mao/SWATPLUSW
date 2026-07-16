---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_harvbiomass.f90
note_file: mgt_harvbiomass.f90
subroutine: mgt_harvbiomass
module:
  - organic_mineral_mass_module
  - soil_module
  - plant_module
  - plant_data_module
  - mgt_operations_module
  - constituent_mass_module
  - carbon_module
calls: []
uses_variables:
  - carbon_module.f90#hpc_d
  - carbon_module.f90#hrc_d
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_pl
  - constituent_mass_module.f90#cs_soil
  - mgt_operations_module.f90#harvop_db
  - organic_mineral_mass_module.f90#harv_leaf
  - organic_mineral_mass_module.f90#harv_left
  - organic_mineral_mass_module.f90#harv_seed
  - organic_mineral_mass_module.f90#harv_stem
  - organic_mineral_mass_module.f90#orgz
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#pl_yield
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine performs the harvest operation for above ground biomass (no kill)"
---

# mgt_harvbiomass

> [!info] Summary
> this subroutine performs the harvest operation for above ground biomass (no kill)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_harvbiomass.f90`
- **Modules used**:
  - [[organic_mineral_mass_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[carbon_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[actions.f90]]
- [[mgt_sched.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[carbon_module.f90#hpc_d]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hrc_d]] - `carbon_residue_gain_losses`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_pl]] - `plant_constituent_mass`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[mgt_operations_module.f90#harvop_db]] - `harvest_operation`
- [[organic_mineral_mass_module.f90#harv_leaf]] - `organic_mass`
- [[organic_mineral_mass_module.f90#harv_left]] - `organic_mass`
- [[organic_mineral_mass_module.f90#harv_seed]] - `organic_mass`
- [[organic_mineral_mass_module.f90#harv_stem]] - `organic_mass`
- [[organic_mineral_mass_module.f90#orgz]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#pl_yield]] - `organic_mass`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
