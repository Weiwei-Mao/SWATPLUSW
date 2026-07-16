---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lsu_output.f90
note_file: lsu_output.f90
subroutine: lsu_output
module:
  - time_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - output_landscape_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - calibration_data_module.f90#lsu_elem
  - calibration_data_module.f90#lsu_out
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#hls_d
  - output_landscape_module.f90#hlsz
  - output_landscape_module.f90#hltls_d
  - output_landscape_module.f90#hltnb_d
  - output_landscape_module.f90#hltpw_d
  - output_landscape_module.f90#hltwb_d
  - output_landscape_module.f90#hnb_d
  - output_landscape_module.f90#hnbz
  - output_landscape_module.f90#hpw_d
  - output_landscape_module.f90#hpwz
  - output_landscape_module.f90#hwb_d
  - output_landscape_module.f90#hwbz
  - output_landscape_module.f90#ruls_a
  - output_landscape_module.f90#ruls_d
  - output_landscape_module.f90#ruls_m
  - output_landscape_module.f90#ruls_y
  - output_landscape_module.f90#runb_a
  - output_landscape_module.f90#runb_d
  - output_landscape_module.f90#runb_m
  - output_landscape_module.f90#runb_y
  - output_landscape_module.f90#rupw_a
  - output_landscape_module.f90#rupw_d
  - output_landscape_module.f90#rupw_m
  - output_landscape_module.f90#rupw_y
  - output_landscape_module.f90#ruwb_a
  - output_landscape_module.f90#ruwb_d
  - output_landscape_module.f90#ruwb_m
  - output_landscape_module.f90#ruwb_y
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# lsu_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lsu_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#lsu_out]] - `landscape_units`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#hls_d]] - `output_losses`
- [[output_landscape_module.f90#hlsz]] - `output_losses`
- [[output_landscape_module.f90#hltls_d]] - `output_losses`
- [[output_landscape_module.f90#hltnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#hltpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hltwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#hnbz]] - `output_nutbal`
- [[output_landscape_module.f90#hpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hpwz]] - `output_plantweather`
- [[output_landscape_module.f90#hwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwbz]] - `output_waterbal`
- [[output_landscape_module.f90#ruls_a]] - `output_losses`
- [[output_landscape_module.f90#ruls_d]] - `output_losses`
- [[output_landscape_module.f90#ruls_m]] - `output_losses`
- [[output_landscape_module.f90#ruls_y]] - `output_losses`
- [[output_landscape_module.f90#runb_a]] - `output_nutbal`
- [[output_landscape_module.f90#runb_d]] - `output_nutbal`
- [[output_landscape_module.f90#runb_m]] - `output_nutbal`
- [[output_landscape_module.f90#runb_y]] - `output_nutbal`
- [[output_landscape_module.f90#rupw_a]] - `output_plantweather`
- [[output_landscape_module.f90#rupw_d]] - `output_plantweather`
- [[output_landscape_module.f90#rupw_m]] - `output_plantweather`
- [[output_landscape_module.f90#rupw_y]] - `output_plantweather`
- [[output_landscape_module.f90#ruwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_y]] - `output_waterbal`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
