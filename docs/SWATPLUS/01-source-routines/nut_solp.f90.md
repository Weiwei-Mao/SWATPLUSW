---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_solp.f90
note_file: nut_solp.f90
subroutine: nut_solp
module:
  - basin_module
  - organic_mineral_mass_module
  - gwflow_module
  - hru_module
  - soil_module
  - output_landscape_module
  - hydrograph_module
  - utils
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gwflow_percsol
  - hru_module.f90#gwsoilp
  - hru_module.f90#hru
  - hru_module.f90#i_sep
  - hru_module.f90#ihru
  - hru_module.f90#qtile
  - hru_module.f90#surfq
  - hru_module.f90#surqsolp
  - hydrograph_module.f90#ht1
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hls_d
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of phosphorus lost from the soil; profile in runoff and the movement of soluble phosphorus from the first; to the second layer via percolation"
---

# nut_solp

> [!info] Summary
> this subroutine calculates the amount of phosphorus lost from the soil; profile in runoff and the movement of soluble phosphorus from the first; to the second layer via percolation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_solp.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[gwflow_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[output_landscape_module.f90]]
  - [[hydrograph_module.f90]]
  - [[utils.f90]]
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
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gwflow_percsol]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#gwsoilp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hls_d]] - `output_losses`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
