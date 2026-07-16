---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soils_init.f90
note_file: soils_init.f90
subroutine: soils_init
module:
  - hru_module
  - soil_module
  - plant_module
  - maximum_data_module
  - soil_data_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - hydrograph_module
  - time_module
  - basin_module
  - septic_data_module
calls:
  - soils_test_adjust
  - soil_phys_init
  - layersplit
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#i_sep
  - hru_module.f90#ihru
  - hru_module.f90#isep
  - hru_module.f90#iseptic
  - hru_module.f90#isol
  - hru_module.f90#mlyr
  - hru_module.f90#wfsh
  - hydrograph_module.f90#sp_ob
  - maximum_data_module.f90#db_mx
  - organic_mineral_mass_module.f90#soil1
  - organic_mineral_mass_module.f90#soil1_init
  - plant_module.f90#pcom
  - septic_data_module.f90#sep
  - soil_data_module.f90#soildb
  - soil_module.f90#soil
  - soil_module.f90#sol
  - soil_module.f90#sol_test
input_variables: []
reads:
  - soil_lyr_depths.sol
writes: []
purpose: ""
---

# soils_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soils_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[maximum_data_module.f90]]
  - [[soil_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[septic_data_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[soils_test_adjust.f90]]
- [[soil_phys_init.f90]]
- [[layersplit.f90]]

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isep]] - `integer`
- [[hru_module.f90#iseptic]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#isol]] - `integer`
- [[hru_module.f90#mlyr]] - `integer`
- [[hru_module.f90#wfsh]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[organic_mineral_mass_module.f90#soil1_init]] - `soil_profile_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[septic_data_module.f90#sep]] - `septic_system`
- [[soil_data_module.f90#soildb]] - `soil_database`
- [[soil_module.f90#soil]] - `soil_profile`
- [[soil_module.f90#sol]] - `soil_hru_database`
- [[soil_module.f90#sol_test]] - `soil_test`

## File I/O
- **Reads**:
  - [[soil_lyr_depths.sol]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
