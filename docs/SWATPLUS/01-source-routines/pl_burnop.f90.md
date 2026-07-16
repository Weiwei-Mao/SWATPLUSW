---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_burnop.f90
note_file: pl_burnop.f90
subroutine: pl_burnop
module:
  - basin_module
  - mgt_operations_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - carbon_module
calls:
  - curno
uses_variables:
  - carbon_module.f90#hpc_d
  - carbon_module.f90#hrc_d
  - hru_module.f90#cn2
  - hru_module.f90#ipl
  - mgt_operations_module.f90#fire_db
  - organic_mineral_mass_module.f90#pl_burn
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#plt_mass_z
  - organic_mineral_mass_module.f90#soil1
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine performs all management operations"
---

# pl_burnop

> [!info] Summary
> this subroutine performs all management operations

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_burnop.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[carbon_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[curno.f90]]

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
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ipl]] - `integer`
- [[mgt_operations_module.f90#fire_db]] - `fire_operation`
- [[organic_mineral_mass_module.f90#pl_burn]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#plt_mass_z]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
