---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_killop.f90
note_file: mgt_killop.f90
subroutine: mgt_killop
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - constituent_mass_module
  - carbon_module
calls:
  - pl_rootfr
  - plg_zero
uses_variables:
  - carbon_module.f90#hpc_d
  - carbon_module.f90#hrc_d
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_pl
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#ipl
  - organic_mineral_mass_module.f90#orgz
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#plt_mass_z
  - organic_mineral_mass_module.f90#soil1
  - plant_module.f90#pcom
  - plant_module.f90#plmz
  - plant_module.f90#plstrz
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine performs the kill operation"
---

# mgt_killop

> [!info] Summary
> this subroutine performs the kill operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_killop.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[carbon_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_rootfr.f90]]
- [[plant_module.f90#plg_zero]]

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
- [[hru_module.f90#ipl]] - `integer`
- [[organic_mineral_mass_module.f90#orgz]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#plt_mass_z]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[plant_module.f90#plmz]] - `plant_mass`
- [[plant_module.f90#plstrz]] - `plant_stress`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
