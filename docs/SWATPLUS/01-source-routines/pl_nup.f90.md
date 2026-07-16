---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_nup.f90
note_file: pl_nup.f90
subroutine: pl_nup
module:
  - plant_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - output_landscape_module
calls:
  - pl_nfix
  - nuts
uses_variables:
  - basin_module.f90#bsn_prm
  - hru_module.f90#fixn
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#nplnt
  - hru_module.f90#rto_no3
  - hru_module.f90#un2
  - hru_module.f90#uno3d
  - hru_module.f90#uptake
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#pl_mass_up
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hnb_d
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "This subroutine calculates plant nitrogen uptake"
---

# pl_nup

> [!info] Summary
> This subroutine calculates plant nitrogen uptake

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_nup.f90`
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_nfix.f90]]
- [[nuts.f90]]

**Called by:**

- [[pl_biomass_gro.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[hru_module.f90#fixn]] - `real`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#nplnt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#rto_no3]] - `real`
- [[hru_module.f90#un2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uno3d]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uptake]] - `uptake_parameters`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#pl_mass_up]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
