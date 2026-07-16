---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_hyd_bfr_et.f90
note_file: calsoft_hyd_bfr_et.f90
subroutine: calsoft_hyd_bfr_et
module:
  - hru_module
  - soil_module
  - plant_module
  - hydrograph_module
  - ru_module
  - aquifer_module
  - hru_lte_module
  - sd_channel_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - conditional_module
  - reservoir_module
  - organic_mineral_mass_module
  - time_module
calls:
  - re_initialize
  - time_control
uses_variables:
  - calibration_data_module.f90#ls_prms
  - calibration_data_module.f90#lscal
  - calibration_data_module.f90#lscal_z
  - calibration_data_module.f90#lsu_reg
  - calibration_data_module.f90#region
  - hru_module.f90#hru
  - hru_module.f90#hru_init
  - maximum_data_module.f90#db_mx
  - time_module.f90#cal_adj
  - time_module.f90#cal_sim
input_variables: []
reads: []
writes: []
purpose: ""
---

# calsoft_hyd_bfr_et

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_hyd_bfr_et.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[hydrograph_module.f90]]
  - [[ru_module.f90]]
  - [[aquifer_module.f90]]
  - [[hru_lte_module.f90]]
  - [[sd_channel_module.f90]]
  - [[basin_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[conditional_module.f90]]
  - [[reservoir_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[re_initialize.f90]]
- [[time_control.f90]]

**Called by:**

- [[calsoft_hyd_bfr.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#ls_prms]] - `soft_calib_parms`
- [[calibration_data_module.f90#lscal]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lscal_z]] - `soft_calib_ls_processes`
- [[calibration_data_module.f90#lsu_reg]] - `landscape_units`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#hru_init]] - `hydrologic_response_unit`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#cal_adj]] - `real`
- [[time_module.f90#cal_sim]] - `character (len=29)`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
