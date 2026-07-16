---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_control.f90
note_file: calsoft_control.f90
subroutine: calsoft_control
module:
  - sd_channel_module
  - hru_lte_module
  - maximum_data_module
  - calibration_data_module
  - time_module
  - basin_module
  - hru_module
  - hydrograph_module
  - soil_module
calls:
  - calsoft_hyd
  - calsoft_hyd_bfr
  - caltsoft_hyd
  - calsoft_plant
  - calsoft_sed
  - pl_write_parms_cal
uses_variables:
  - basin_module.f90#pco
  - basin_module.f90#pco_init
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#ch_prms
  - calibration_data_module.f90#chcal
  - calibration_data_module.f90#lscal
  - calibration_data_module.f90#lscalt
  - calibration_data_module.f90#lsu_reg
  - calibration_data_module.f90#region
  - hru_lte_module.f90#hlt
  - hru_lte_module.f90#hlt_db
  - hru_module.f90#cn2
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#sp_ob
  - maximum_data_module.f90#db_mx
input_variables: []
reads: []
writes: []
purpose: ""
---

# calsoft_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_control.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[hru_lte_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 6 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[calsoft_hyd.f90]]
- [[calsoft_hyd_bfr.f90]]
- [[caltsoft_hyd.f90]]
- [[calsoft_plant.f90]]
- [[calsoft_sed.f90]]
- [[pl_write_parms_cal.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#pco_init]] - `basin_print_codes`
- [[calibration_data_module.f90#cal_codes]] - `soft_calibration_codes`
- [[calibration_data_module.f90#ch_prms]] - `soft_calib_parms`
- [[calibration_data_module.f90#chcal]] - `soft_data_calib_channel`
- [[calibration_data_module.f90#lscal]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lscalt]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lsu_reg]] - `landscape_units`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[hru_lte_module.f90#hlt]] - `swatdeg_hru_dynamic`
- [[hru_lte_module.f90#hlt_db]] - `swatdeg_hru_data`
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
