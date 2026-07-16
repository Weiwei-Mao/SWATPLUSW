---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_nlch.f90
note_file: nut_nlch.f90
subroutine: nut_nlch
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - gwflow_module
  - soil_module
calls: []
uses_variables:
  - gwflow_module.f90#gw_solute_flag
  - hru_module.f90#gwsoiln
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#latno3
  - hru_module.f90#percn
  - hru_module.f90#qtile
  - hru_module.f90#surfq
  - hru_module.f90#surqno3
  - hru_module.f90#tileno3
  - organic_mineral_mass_module.f90#soil1
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine simulates the loss of nitrate via surface runoff,; lateral flow, tile flow, and percolation out of the profile"
---

# nut_nlch

> [!info] Summary
> this subroutine simulates the loss of nitrate via surface runoff,; lateral flow, tile flow, and percolation out of the profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_nlch.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[gwflow_module.f90]]
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
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[hru_module.f90#gwsoiln]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#latno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#percn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tileno3]] - `real, dimension (:), allocatable`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
