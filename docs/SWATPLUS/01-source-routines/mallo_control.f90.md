---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mallo_control.f90
note_file: mallo_control.f90
subroutine: mallo_control
module:
  - manure_allocation_module
  - hru_module
  - basin_module
  - time_module
  - plant_module
  - soil_module
  - organic_mineral_mass_module
  - conditional_module
calls:
  - conditions
  - actions
  - pl_fert
uses_variables:
  - basin_module.f90#pco
  - conditional_module.f90#d_tbl
  - conditional_module.f90#dtbl_lum
  - hru_module.f90#fertnh3
  - hru_module.f90#fertno3
  - hru_module.f90#fertorgn
  - hru_module.f90#fertorgp
  - hru_module.f90#fertsolp
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#mo
  - hru_module.f90#phubase
  - hru_module.f90#sol_sumno3
  - hru_module.f90#sol_sumsolp
  - manure_allocation_module.f90#mallo
  - manure_allocation_module.f90#malloz
  - manure_allocation_module.f90#manure_amtz
  - organic_mineral_mass_module.f90#pl_mass
  - plant_module.f90#pcom
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# mallo_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mallo_control.f90`
- **Modules used**:
  - [[manure_allocation_module.f90]]
  - [[hru_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[plant_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[conditions.f90]]
- [[actions.f90]]
- [[pl_fert.f90]]

**Called by:**

- [[time_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[hru_module.f90#fertnh3]] - `real`
- [[hru_module.f90#fertno3]] - `real`
- [[hru_module.f90#fertorgn]] - `real`
- [[hru_module.f90#fertorgp]] - `real`
- [[hru_module.f90#fertsolp]] - `real`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumsolp]] - `real, dimension (:), allocatable`
- [[manure_allocation_module.f90#mallo]] - `manure_allocation`
- [[manure_allocation_module.f90#malloz]] - `source_manure_output`
- [[manure_allocation_module.f90#manure_amtz]] - `manure_demand_amount`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
