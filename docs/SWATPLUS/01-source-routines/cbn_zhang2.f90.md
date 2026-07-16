---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cbn_zhang2.f90
note_file: cbn_zhang2.f90
subroutine: cbn_zhang2
module:
  - hru_module
  - soil_module
  - basin_module
  - organic_mineral_mass_module
  - carbon_module
  - output_landscape_module
  - tillage_data_module
calls:
  - nut_np_flow
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - carbon_module.f90#carbdb
  - carbon_module.f90#hrc_d
  - carbon_module.f90#hsc_d
  - carbon_module.f90#org_allo
  - carbon_module.f90#org_con
  - carbon_module.f90#org_flux
  - carbon_module.f90#org_flux_zero
  - carbon_module.f90#org_frac
  - carbon_module.f90#org_ratio
  - carbon_module.f90#org_ratio_zero
  - carbon_module.f90#org_tran
  - carbon_module.f90#org_tran_zero
  - hru_module.f90#ihru
  - hru_module.f90#tillage_days
  - hru_module.f90#tillage_depth
  - hru_module.f90#tillage_switch
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hnb_d
  - soil_module.f90#soil
  - tillage_data_module.f90#till_eff_days
input_variables: []
reads: []
writes: []
purpose: ""
---

# cbn_zhang2

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cbn_zhang2.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[carbon_module.f90]]
  - [[output_landscape_module.f90]]
  - [[tillage_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[nut_np_flow.f90]]

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[carbon_module.f90#carbdb]] - `carbon_inputs`
- [[carbon_module.f90#hrc_d]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hsc_d]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#org_allo]] - `organic_allocations`
- [[carbon_module.f90#org_con]] - `organic_controls`
- [[carbon_module.f90#org_flux]] - `organic_flux`
- [[carbon_module.f90#org_flux_zero]] - `organic_flux`
- [[carbon_module.f90#org_frac]] - `organic_fractions`
- [[carbon_module.f90#org_ratio]] - `organic_ratio`
- [[carbon_module.f90#org_ratio_zero]] - `organic_ratio`
- [[carbon_module.f90#org_tran]] - `organic_transformations`
- [[carbon_module.f90#org_tran_zero]] - `organic_transformations`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#tillage_days]] - `integer, dimension(:), allocatable`
- [[hru_module.f90#tillage_depth]] - `real, dimension(:), allocatable`
- [[hru_module.f90#tillage_switch]] - `integer, dimension(:), allocatable`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#till_eff_days]] - `integer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
