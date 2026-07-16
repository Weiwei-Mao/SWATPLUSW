---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_sum_output.f90
note_file: calsoft_sum_output.f90
subroutine: calsoft_sum_output
module:
  - sd_channel_module
  - hru_lte_module
  - hru_module
  - output_landscape_module
  - maximum_data_module
  - calibration_data_module
calls: []
uses_variables:
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#chcal
  - calibration_data_module.f90#chcal_z
  - calibration_data_module.f90#lscal
  - calibration_data_module.f90#lscal_z
  - calibration_data_module.f90#lscalt
  - calibration_data_module.f90#lsu_reg
  - calibration_data_module.f90#region
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ilu
  - hru_module.f90#latq
  - hru_module.f90#qtile
  - hru_module.f90#sedyld
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#hls_y
  - output_landscape_module.f90#hltls_y
  - output_landscape_module.f90#hltwb_y
  - output_landscape_module.f90#hwb_y
  - sd_channel_module.f90#chsd_y
  - sd_channel_module.f90#sd_ch
input_variables: []
reads: []
writes: []
purpose: ""
---

# calsoft_sum_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_sum_output.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[hru_lte_module.f90]]
  - [[hru_module.f90]]
  - [[output_landscape_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
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
- [[calibration_data_module.f90#chcal_z]] - `soft_calib_chan_processes`
- [[calibration_data_module.f90#lscal]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lscal_z]] - `soft_calib_ls_processes`
- [[calibration_data_module.f90#lscalt]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lsu_reg]] - `landscape_units`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ilu]] - `integer`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#hls_y]] - `output_losses`
- [[output_landscape_module.f90#hltls_y]] - `output_losses`
- [[output_landscape_module.f90#hltwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_y]] - `output_waterbal`
- [[sd_channel_module.f90#chsd_y]] - `sd_ch_output`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
