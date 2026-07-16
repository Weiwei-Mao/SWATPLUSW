---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_decay.f90
note_file: pest_decay.f90
subroutine: pest_decay
module:
  - pesticide_data_module
  - hru_module
  - constituent_mass_module
  - soil_module
  - plant_module
  - output_ls_pesticide_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_pl
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - output_ls_pesticide_module.f90#hpestb_d
  - pesticide_data_module.f90#pestcp
  - pesticide_data_module.f90#pestdb
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates degradation of pesticide in the soil and on; the plants"
---

# pest_decay

> [!info] Summary
> this subroutine calculates degradation of pesticide in the soil and on; the plants

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_decay.f90`
- **Modules used**:
  - [[pesticide_data_module.f90]]
  - [[hru_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[output_ls_pesticide_module.f90]]
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
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[pesticide_data_module.f90#pestcp]] - `pesticide_cp`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
