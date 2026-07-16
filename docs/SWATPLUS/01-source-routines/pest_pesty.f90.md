---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_pesty.f90
note_file: pest_pesty.f90
subroutine: pest_pesty
module:
  - hru_module
  - soil_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - pesticide_data_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#enratio
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#sedyld
  - organic_mineral_mass_module.f90#soil1
  - output_ls_pesticide_module.f90#hpestb_d
  - pesticide_data_module.f90#pestdb
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates pesticide transported with suspended sediment"
---

# pest_pesty

> [!info] Summary
> this subroutine calculates pesticide transported with suspended sediment

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_pesty.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_ls_pesticide_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[organic_mineral_mass_module.f90]]
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
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[hru_module.f90#enratio]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
