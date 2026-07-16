---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_depstor.f90
note_file: swr_depstor.f90
subroutine: swr_depstor
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - hru_module.f90#cumei
  - hru_module.f90#cumeira
  - hru_module.f90#cumrai
  - hru_module.f90#cumrt
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#itill
  - hru_module.f90#precip_eff
  - hru_module.f90#ranrns_hru
  - hru_module.f90#stmaxd
  - hru_module.f90#usle_ei
  - organic_mineral_mass_module.f90#soil1
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes maximum surface depressional storage depth based on; random and oriented roughness and slope steepness"
---

# swr_depstor

> [!info] Summary
> this subroutine computes maximum surface depressional storage depth based on; random and oriented roughness and slope steepness

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_depstor.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[swr_drains.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#cumei]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumeira]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumrai]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumrt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#itill]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#precip_eff]] - `real`
- [[hru_module.f90#ranrns_hru]] - `real, dimension (:), allocatable`
- [[hru_module.f90#stmaxd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#usle_ei]] - `real`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
