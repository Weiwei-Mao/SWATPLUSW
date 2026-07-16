---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_ave_output.f90
note_file: calsoft_ave_output.f90
subroutine: calsoft_ave_output
module:
  - sd_channel_module
  - hru_lte_module
  - maximum_data_module
  - calibration_data_module
  - time_module
calls: []
uses_variables:
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#chcal
  - calibration_data_module.f90#lscal
  - calibration_data_module.f90#lscalt
  - calibration_data_module.f90#lsu_reg
  - calibration_data_module.f90#plcal
  - calibration_data_module.f90#plcal_z
  - calibration_data_module.f90#region
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# calsoft_ave_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_ave_output.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[hru_lte_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[time_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#cal_codes]] - `soft_calibration_codes`
- [[calibration_data_module.f90#chcal]] - `soft_data_calib_channel`
- [[calibration_data_module.f90#lscal]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lscalt]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lsu_reg]] - `landscape_units`
- [[calibration_data_module.f90#plcal]] - `soft_data_calib_plant`
- [[calibration_data_module.f90#plcal_z]] - `soft_calib_pl_processes`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
