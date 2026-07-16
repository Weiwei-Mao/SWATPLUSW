---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_harvresidue.f90
note_file: mgt_harvresidue.f90
subroutine: mgt_harvresidue
module:
  - plant_module
  - carbon_module
  - mgt_operations_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - carbon_module.f90#hrc_d
  - mgt_operations_module.f90#harvop_db
  - organic_mineral_mass_module.f90#orgz
  - organic_mineral_mass_module.f90#pl_mass
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "this subroutine performs the harvest residue operation"
---

# mgt_harvresidue

> [!info] Summary
> this subroutine performs the harvest residue operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_harvresidue.f90`
- **Modules used**:
  - [[plant_module.f90]]
  - [[carbon_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[organic_mineral_mass_module.f90]]
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
- [[carbon_module.f90#hrc_d]] - `carbon_residue_gain_losses`
- [[mgt_operations_module.f90#harvop_db]] - `harvest_operation`
- [[organic_mineral_mass_module.f90#orgz]] - `organic_mass`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
