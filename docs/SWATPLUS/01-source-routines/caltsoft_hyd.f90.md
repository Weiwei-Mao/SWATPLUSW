---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: caltsoft_hyd.f90
note_file: caltsoft_hyd.f90
subroutine: caltsoft_hyd
module:
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
calls:
  - ascrv
  - time_control
uses_variables:
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#ls_prms
  - calibration_data_module.f90#lscal_z
  - calibration_data_module.f90#lscalt
  - calibration_data_module.f90#lsu_reg
  - calibration_data_module.f90#plcal
  - calibration_data_module.f90#plcal_z
  - calibration_data_module.f90#region
  - hru_lte_module.f90#hlt
  - hru_lte_module.f90#hlt_init
  - maximum_data_module.f90#db_mx
input_variables: []
reads: []
writes: []
purpose: ""
---

# caltsoft_hyd

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `caltsoft_hyd.f90`
- **Modules used**:
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
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ascrv.f90]]
- [[time_control.f90]]

**Called by:**

- [[calsoft_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#cal_codes]] - `soft_calibration_codes`
- [[calibration_data_module.f90#ls_prms]] - `soft_calib_parms`
- [[calibration_data_module.f90#lscal_z]] - `soft_calib_ls_processes`
- [[calibration_data_module.f90#lscalt]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lsu_reg]] - `landscape_units`
- [[calibration_data_module.f90#plcal]] - `soft_data_calib_plant`
- [[calibration_data_module.f90#plcal_z]] - `soft_calib_pl_processes`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[hru_lte_module.f90#hlt]] - `swatdeg_hru_dynamic`
- [[hru_lte_module.f90#hlt_init]] - `swatdeg_hru_dynamic`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
