---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cbn_rsd_decomp.f90
note_file: cbn_rsd_decomp.f90
subroutine: cbn_rsd_decomp
module:
  - septic_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - output_landscape_module
  - carbon_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - carbon_module.f90#cnr_cap
  - carbon_module.f90#cnr_ref
  - carbon_module.f90#cpr_cap
  - carbon_module.f90#cpr_ref
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - organic_mineral_mass_module.f90#decomp
  - organic_mineral_mass_module.f90#lig_frac
  - organic_mineral_mass_module.f90#rsd_meta
  - organic_mineral_mass_module.f90#rsd_str
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hnb_d
  - plant_data_module.f90#cswat_1_part_fracs
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine estimates daily nitrogen and phosphorus; mineralization and immobilization considering fresh organic; material (plant residue) and active and stable humus material"
---

# cbn_rsd_decomp

> [!info] Summary
> this subroutine estimates daily nitrogen and phosphorus; mineralization and immobilization considering fresh organic; material (plant residue) and active and stable humus material

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cbn_rsd_decomp.f90`
- **Modules used**:
  - [[septic_data_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[output_landscape_module.f90]]
  - [[carbon_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[carbon_module.f90#cnr_cap]] - `real`
- [[carbon_module.f90#cnr_ref]] - `real`
- [[carbon_module.f90#cpr_cap]] - `real`
- [[carbon_module.f90#cpr_ref]] - `real`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[organic_mineral_mass_module.f90#decomp]] - `organic_mass`
- [[organic_mineral_mass_module.f90#lig_frac]] - `real`
- [[organic_mineral_mass_module.f90#rsd_meta]] - `organic_mass`
- [[organic_mineral_mass_module.f90#rsd_str]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[plant_data_module.f90#cswat_1_part_fracs]] - `lignin_derived_partition_fracs`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
