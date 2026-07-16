---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_sed.f90
note_file: calsoft_sed.f90
subroutine: calsoft_sed
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
calls:
  - re_initialize
  - time_control
uses_variables:
  - calibration_data_module.f90#ls_prms
  - calibration_data_module.f90#lscal
  - calibration_data_module.f90#lscal_z
  - calibration_data_module.f90#region
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#tconc
  - hydrograph_module.f90#sp_ob
  - maximum_data_module.f90#db_mx
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: ""
---

# calsoft_sed

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_sed.f90`
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
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[re_initialize.f90]]
- [[time_control.f90]]

**Called by:**

- [[calsoft_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#ls_prms]] - `soft_calib_parms`
- [[calibration_data_module.f90#lscal]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lscal_z]] - `soft_calib_ls_processes`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
