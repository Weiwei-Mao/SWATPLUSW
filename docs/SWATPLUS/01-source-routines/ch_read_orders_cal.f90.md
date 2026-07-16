---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read_orders_cal.f90
note_file: ch_read_orders_cal.f90
subroutine: ch_read_orders_cal
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - sd_channel_module
calls: []
uses_variables:
  - calibration_data_module.f90#ccu_cal
  - calibration_data_module.f90#ccu_elem
  - calibration_data_module.f90#ccu_reg
  - calibration_data_module.f90#chcal
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_chg
  - maximum_data_module.f90#db_mx
  - sd_channel_module.f90#sd_ch
input_variables:
  - calibration_data_module.f90#chcal
reads:
  - in_chg%ch_sed_budget_sft
writes: []
purpose: ""
---

# ch_read_orders_cal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read_orders_cal.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cal.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#ccu_cal]] - `cataloging_units`
- [[calibration_data_module.f90#ccu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#ccu_reg]] - `landscape_units`
- [[calibration_data_module.f90#chcal]] - `soft_data_calib_channel`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_chg]] - `input_chg`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`

**Populated by file reads:**

- [[calibration_data_module.f90#chcal]]

## File I/O
- **Reads**:
  - [[ch_sed_budget.sft]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
