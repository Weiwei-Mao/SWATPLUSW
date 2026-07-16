---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_plant.f90
note_file: calsoft_plant.f90
subroutine: calsoft_plant
module:
  - hru_module
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
  - soil_module
  - plant_module
  - output_landscape_module
calls:
  - calsoft_plant_zero
  - time_control
  - re_initialize
uses_variables:
  - calibration_data_module.f90#pl_prms
  - calibration_data_module.f90#plcal
  - hru_module.f90#hru
  - hru_module.f90#hru_init
  - hru_module.f90#ipl
  - maximum_data_module.f90#db_mx
  - plant_module.f90#pcom
  - plant_module.f90#pcom_init
input_variables: []
reads: []
writes: []
purpose: ""
---

# calsoft_plant

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_plant.f90`
- **Modules used**:
  - [[hru_module.f90]]
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
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[calsoft_plant_zero.f90]]
- [[time_control.f90]]
- [[re_initialize.f90]]

**Called by:**

- [[calsoft_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#pl_prms]] - `pl_parm_region`
- [[calibration_data_module.f90#plcal]] - `soft_data_calib_plant`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#hru_init]] - `hydrologic_response_unit`
- [[hru_module.f90#ipl]] - `integer`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[plant_module.f90#pcom]] - `plant_community`
- [[plant_module.f90#pcom_init]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
