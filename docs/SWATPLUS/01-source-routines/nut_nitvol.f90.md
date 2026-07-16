---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_nitvol.f90
note_file: nut_nitvol.f90
subroutine: nut_nitvol
module:
  - septic_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
calls: []
uses_variables:
  - hru_module.f90#i_sep
  - hru_module.f90#ihru
  - hru_module.f90#isep
  - organic_mineral_mass_module.f90#soil1
  - septic_data_module.f90#sep
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine estimates daily mineralization (NH3 to NO3); and volatilization of NH3"
---

# nut_nitvol

> [!info] Summary
> this subroutine estimates daily mineralization (NH3 to NO3); and volatilization of NH3

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_nitvol.f90`
- **Modules used**:
  - [[septic_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
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
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isep]] - `integer`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[septic_data_module.f90#sep]] - `septic_system`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
