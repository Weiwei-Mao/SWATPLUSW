---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_pminrl.f90
note_file: nut_pminrl.f90
subroutine: nut_pminrl
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - output_landscape_module
calls: []
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hnb_d
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes p flux between the labile, active mineral; and stable mineral p pools."
---

# nut_pminrl

> [!info] Summary
> this subroutine computes p flux between the labile, active mineral; and stable mineral p pools.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_pminrl.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[output_landscape_module.f90]]
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
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
