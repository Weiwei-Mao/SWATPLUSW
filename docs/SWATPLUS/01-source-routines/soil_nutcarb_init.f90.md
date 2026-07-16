---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_nutcarb_init.f90
note_file: soil_nutcarb_init.f90
subroutine: soil_nutcarb_init
module:
  - hru_module
  - soil_module
  - soil_data_module
  - basin_module
  - organic_mineral_mass_module
  - carbon_module
  - tillage_data_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - carbon_module.f90#org_frac
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#isol
  - hru_module.f90#sol_plt_ini
  - organic_mineral_mass_module.f90#soil1
  - soil_data_module.f90#solt_db
  - soil_module.f90#soil
  - tillage_data_module.f90#bmix_depth
  - tillage_data_module.f90#bmix_eff
input_variables: []
reads: []
writes: []
purpose: "this subroutine initializes soil chemical properties; and intial soil layer bmix efficiency"
---

# soil_nutcarb_init

> [!info] Summary
> this subroutine initializes soil chemical properties; and intial soil layer bmix efficiency

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_nutcarb_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[soil_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[carbon_module.f90]]
  - [[tillage_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[carbon_module.f90#org_frac]] - `organic_fractions`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isol]] - `integer`
- [[hru_module.f90#sol_plt_ini]] - `soil_plant_initialize`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[soil_data_module.f90#solt_db]] - `soiltest_db`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#bmix_depth]] - `real`
- [[tillage_data_module.f90#bmix_eff]] - `real`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
