---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_pup.f90
note_file: pl_pup.f90
subroutine: pl_pup
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - output_landscape_module
  - utils
calls:
  - nuts
uses_variables:
  - basin_module.f90#bsn_prm
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#pplnt
  - hru_module.f90#rto_solp
  - hru_module.f90#uapd
  - hru_module.f90#up2
  - hru_module.f90#uptake
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#pl_mass_up
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hnb_d
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates plant phosphorus uptake"
---

# pl_pup

> [!info] Summary
> this subroutine calculates plant phosphorus uptake

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_pup.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[output_landscape_module.f90]]
  - [[utils.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

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
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#pplnt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#rto_solp]] - `real`
- [[hru_module.f90#uapd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#up2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uptake]] - `uptake_parameters`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#pl_mass_up]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
