---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lcu_read_softcal.f90
note_file: lcu_read_softcal.f90
subroutine: lcu_read_softcal
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - hru_module
  - hru_lte_module
  - output_landscape_module
  - basin_module
calls: []
uses_variables:
  - basin_module.f90#bsn
  - calibration_data_module.f90#cal_codes
  - calibration_data_module.f90#lscal
  - calibration_data_module.f90#lsu_elem
  - calibration_data_module.f90#lsu_reg
  - calibration_data_module.f90#region
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_chg
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#rls_a
  - output_landscape_module.f90#rls_d
  - output_landscape_module.f90#rls_m
  - output_landscape_module.f90#rls_y
  - output_landscape_module.f90#rnb_a
  - output_landscape_module.f90#rnb_d
  - output_landscape_module.f90#rnb_m
  - output_landscape_module.f90#rnb_y
  - output_landscape_module.f90#rpw_a
  - output_landscape_module.f90#rpw_d
  - output_landscape_module.f90#rpw_m
  - output_landscape_module.f90#rpw_y
  - output_landscape_module.f90#rwb_a
  - output_landscape_module.f90#rwb_d
  - output_landscape_module.f90#rwb_m
  - output_landscape_module.f90#rwb_y
input_variables:
  - calibration_data_module.f90#lscal
  - calibration_data_module.f90#region
reads:
  - in_chg%water_balance_sft
writes: []
purpose: ""
---

# lcu_read_softcal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lcu_read_softcal.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[hru_lte_module.f90]]
  - [[output_landscape_module.f90]]
  - [[basin_module.f90]]
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
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[calibration_data_module.f90#cal_codes]] - `soft_calibration_codes`
- [[calibration_data_module.f90#lscal]] - `soft_data_calib_landscape`
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#lsu_reg]] - `landscape_units`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_chg]] - `input_chg`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#rls_a]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_d]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_m]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_y]] - `regional_output_losses`
- [[output_landscape_module.f90#rnb_a]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_d]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_m]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_y]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rpw_a]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_d]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_m]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_y]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rwb_a]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_d]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_m]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_y]] - `regional_output_waterbal`

**Populated by file reads:**

- [[calibration_data_module.f90#lscal]]
- [[calibration_data_module.f90#region]]

## File I/O
- **Reads**:
  - [[water_balance.sft]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
