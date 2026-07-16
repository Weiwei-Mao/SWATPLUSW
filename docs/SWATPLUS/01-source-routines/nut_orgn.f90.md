---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_orgn.f90
note_file: nut_orgn.f90
subroutine: nut_orgn
module:
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
calls: []
uses_variables:
  - hru_module.f90#enratio
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#sedorgn
  - hru_module.f90#sedyld
  - organic_mineral_mass_module.f90#soil1
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of organic nitrogen removed in; surface runoff"
---

# nut_orgn

> [!info] Summary
> this subroutine calculates the amount of organic nitrogen removed in; surface runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_orgn.f90`
- **Modules used**:
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
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
- [[hru_module.f90#enratio]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
