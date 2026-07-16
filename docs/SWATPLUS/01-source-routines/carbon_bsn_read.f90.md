---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: carbon_bsn_read.f90
note_file: carbon_bsn_read.f90
subroutine: carbon_bsn_read
module:
  - carbon_module
  - basin_module
  - tillage_data_module
  - plant_data_module
  - input_file_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - carbon_module.f90#carbdb
  - carbon_module.f90#cb_wtr_coef
  - carbon_module.f90#cnr_cap
  - carbon_module.f90#cnr_ref
  - carbon_module.f90#cpr_cap
  - carbon_module.f90#cpr_ref
  - carbon_module.f90#man_coef
  - carbon_module.f90#n_act_frac
  - carbon_module.f90#org_allo
  - carbon_module.f90#org_con
  - carbon_module.f90#org_frac
  - input_file_module.f90#in_basin
  - plant_data_module.f90#photo_degrade_factor
  - tillage_data_module.f90#bio_consf
  - tillage_data_module.f90#bmix_a
  - tillage_data_module.f90#bmix_b
  - tillage_data_module.f90#bmix_c
  - tillage_data_module.f90#till_consf
  - tillage_data_module.f90#till_eff_days
  - tillage_data_module.f90#tillmix_a
  - tillage_data_module.f90#tillmix_b
  - tillage_data_module.f90#tillmix_c
input_variables: []
reads:
  - in_basin%carbon_bsn
  - carbon_lyr
writes: []
purpose: ""
---

# carbon_bsn_read

> [!info] Summary
> Reads the basin-wide dynamic carbon settings from [[carbon.bsn]] and the companion per-layer coefficients from [[carbon_lyr.bsn]] when `bsn_cc%cswat = 2`.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `carbon_bsn_read.f90`
- **Modules used**:
  - [[carbon_module.f90]]
  - [[basin_module.f90]]
  - [[tillage_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[input_file_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[carbon_module.f90#carbdb]] - `carbon_inputs`
- [[carbon_module.f90#cb_wtr_coef]] - `carbon_water_coef`
- [[carbon_module.f90#cnr_cap]] - `real`
- [[carbon_module.f90#cnr_ref]] - `real`
- [[carbon_module.f90#cpr_cap]] - `real`
- [[carbon_module.f90#cpr_ref]] - `real`
- [[carbon_module.f90#man_coef]] - `manure_coef`
- [[carbon_module.f90#n_act_frac]] - `real`
- [[carbon_module.f90#org_allo]] - `organic_allocations`
- [[carbon_module.f90#org_con]] - `organic_controls`
- [[carbon_module.f90#org_frac]] - `organic_fractions`
- [[input_file_module.f90#in_basin]] - `input_basin`
- [[plant_data_module.f90#photo_degrade_factor]] - `real`
- [[tillage_data_module.f90#bio_consf]] - `real`
- [[tillage_data_module.f90#bmix_a]] - `real`
- [[tillage_data_module.f90#bmix_b]] - `real`
- [[tillage_data_module.f90#bmix_c]] - `real`
- [[tillage_data_module.f90#till_consf]] - `real`
- [[tillage_data_module.f90#till_eff_days]] - `integer`
- [[tillage_data_module.f90#tillmix_a]] - `real`
- [[tillage_data_module.f90#tillmix_b]] - `real`
- [[tillage_data_module.f90#tillmix_c]] - `real`

## File I/O
- **Reads**:
  - [[carbon.bsn]]
  - [[carbon_lyr.bsn]] _(derived from `in_basin%carbon_bsn`; not listed separately in [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- If Line 46, [[basin_module.f90#bsn_cc]] %cswat != 2, pass
	- 0, static soil carbon, old mineralization routines
	- 1, C-FARM one carbon pool model
	- 2, dynamic CENTURY/SWAT-C model
- Else
	- Line 48-93, read [[carbon.bsn]]
	- Line 95-165, read [[carbon_lyr.bsn]]
	- The derived layer file currently expects two valid coefficient rows because `carbdb` and `org_allo` are `dimension(2)` in [[carbon_module.f90]].
- End


<!-- USER-NOTES-END -->
