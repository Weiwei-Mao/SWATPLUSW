---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_pl_up.f90
note_file: pest_pl_up.f90
subroutine: pest_pl_up
module:
  - pesticide_data_module
  - output_ls_pesticide_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - plant_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_pl
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#uptake
  - output_ls_pesticide_module.f90#hpestb_d
  - pesticide_data_module.f90#pestdb
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of pesticide plant uptake; foliage and onto the soil"
---

# pest_pl_up

> [!info] Summary
> this subroutine calculates the amount of pesticide plant uptake; foliage and onto the soil

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_pl_up.f90`
- **Modules used**:
  - [[pesticide_data_module.f90]]
  - [[output_ls_pesticide_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[plant_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_pl]] - `plant_constituent_mass`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#uptake]] - `uptake_parameters`
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
