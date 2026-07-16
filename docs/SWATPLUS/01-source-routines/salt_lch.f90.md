---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_lch.f90
note_file: salt_lch.f90
subroutine: salt_lch
module:
  - hru_module
  - basin_module
  - constituent_mass_module
  - soil_module
  - gwflow_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gwflow_percsol
  - hru_module.f90#gwupsalt
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#latqsalt
  - hru_module.f90#percsalt
  - hru_module.f90#qtile
  - hru_module.f90#surfq
  - hru_module.f90#surqsalt
  - hru_module.f90#tilesalt
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine simulates the loss of salt via surface runoff,; lateral flow, tile flow, and percolation out of the profile"
---

# salt_lch

> [!info] Summary
> this subroutine simulates the loss of salt via surface runoff,; lateral flow, tile flow, and percolation out of the profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_lch.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[basin_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[soil_module.f90]]
  - [[gwflow_module.f90]]
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
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gwflow_percsol]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#gwupsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#latqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#percsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#tilesalt]] - `real, dimension (:,:), allocatable`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
