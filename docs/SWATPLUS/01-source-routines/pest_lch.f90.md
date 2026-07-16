---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_lch.f90
note_file: pest_lch.f90
subroutine: pest_lch
module:
  - pesticide_data_module
  - basin_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#latq
  - hru_module.f90#qtile
  - hru_module.f90#surfq
  - organic_mineral_mass_module.f90#soil1
  - output_ls_pesticide_module.f90#hpestb_d
  - pesticide_data_module.f90#pestdb
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates pesticides leached through each layer,; pesticide transported with lateral subsurface flow, and pesticide; transported with surface runoff"
---

# pest_lch

> [!info] Summary
> this subroutine calculates pesticides leached through each layer,; pesticide transported with lateral subsurface flow, and pesticide; transported with surface runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_lch.f90`
- **Modules used**:
  - [[pesticide_data_module.f90]]
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_ls_pesticide_module.f90]]
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
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
