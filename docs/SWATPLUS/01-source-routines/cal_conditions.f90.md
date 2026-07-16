---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cal_conditions.f90
note_file: cal_conditions.f90
subroutine: cal_conditions
module:
  - maximum_data_module
  - calibration_data_module
  - conditional_module
  - hru_lte_module
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - time_module
  - reservoir_module
  - climate_module
  - landuse_data_module
calls:
  - cal_parm_select
uses_variables:
  - calibration_data_module.f90#cal_parms
  - calibration_data_module.f90#cal_upd
  - climate_module.f90#pcp
  - climate_module.f90#tmp
  - conditional_module.f90#dtbl_res
  - hru_module.f90#hru
  - hru_module.f90#ipl
  - maximum_data_module.f90#db_mx
  - plant_data_module.f90#pl_class
  - plant_module.f90#pcom
  - reservoir_module.f90#res_ob
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# cal_conditions

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cal_conditions.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[conditional_module.f90]]
  - [[hru_lte_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[time_module.f90]]
  - [[reservoir_module.f90]]
  - [[climate_module.f90]]
  - [[landuse_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cal_parm_select.f90]]

**Called by:**

- [[proc_cal.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#cal_parms]] - `calibration_parameters`
- [[calibration_data_module.f90#cal_upd]] - `update_parameters`
- [[climate_module.f90#pcp]] - `climate_measured_data`
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[conditional_module.f90#dtbl_res]] - `decision_table`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ipl]] - `integer`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[plant_data_module.f90#pl_class]] - `character(len=25), dimension(:), allocatable`
- [[plant_module.f90#pcom]] - `plant_community`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
