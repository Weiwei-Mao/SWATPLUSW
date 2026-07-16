---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_transplant.f90
note_file: mgt_transplant.f90
subroutine: mgt_transplant
module:
  - hru_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
calls:
  - pl_root_gro
  - pl_seed_gro
  - pl_partition
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - organic_mineral_mass_module.f90#pl_mass
  - plant_data_module.f90#pcomdb
  - plant_data_module.f90#plcp
  - plant_data_module.f90#pldb
  - plant_data_module.f90#transpl
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: ""
---

# mgt_transplant

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_transplant.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_root_gro.f90]]
- [[pl_seed_gro.f90]]
- [[pl_partition.f90]]

**Called by:**

- [[actions.f90]]
- [[mgt_sched.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_data_module.f90#pcomdb]] - `plant_community_db`
- [[plant_data_module.f90#plcp]] - `plant_cp`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_data_module.f90#transpl]] - `plant_transplant_db`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
