---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_pminrl2.f90
note_file: nut_pminrl2.f90
subroutine: nut_pminrl2
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - output_landscape_module
  - soil_module
  - time_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hnb_d
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes p flux between the labile, active mineral; and stable mineral p pools.; this is the alternate phosphorus model described in Vadas and White (2010)"
---

# nut_pminrl2

> [!info] Summary
> this subroutine computes p flux between the labile, active mineral; and stable mineral p pools.; this is the alternate phosphorus model described in Vadas and White (2010)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_pminrl2.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[output_landscape_module.f90]]
  - [[soil_module.f90]]
  - [[time_module.f90]]
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
- [[hru_module.f90#ihru]] - `integer`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
