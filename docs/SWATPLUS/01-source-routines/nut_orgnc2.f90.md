---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_orgnc2.f90
note_file: nut_orgnc2.f90
subroutine: nut_orgnc2
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - carbon_module
  - plant_module
  - plant_data_module
calls: []
uses_variables:
  - carbon_module.f90#cb_wtr_coef
  - carbon_module.f90#hsc_d
  - hru_module.f90#enratio
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#sedorgn
  - hru_module.f90#sedyld
  - hru_module.f90#surfq
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of organic nitrogen removed in; surface runoff - when using CSWAT==2 it"
---

# nut_orgnc2

> [!info] Summary
> this subroutine calculates the amount of organic nitrogen removed in; surface runoff - when using CSWAT==2 it

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_orgnc2.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[carbon_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
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
- [[carbon_module.f90#cb_wtr_coef]] - `carbon_water_coef`
- [[carbon_module.f90#hsc_d]] - `carbon_soil_gain_losses`
- [[hru_module.f90#enratio]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
