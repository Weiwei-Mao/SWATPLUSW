---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_sw_init.f90
note_file: basin_sw_init.f90
subroutine: basin_sw_init
module:
  - time_module
  - hydrograph_module
  - calibration_data_module
  - output_landscape_module
  - basin_module
  - maximum_data_module
  - soil_module
  - hru_module
calls: []
uses_variables:
  - calibration_data_module.f90#lsu_elem
  - calibration_data_module.f90#lsu_out
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#sp_ob
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#bwb_a
  - output_landscape_module.f90#bwb_d
  - output_landscape_module.f90#bwb_m
  - output_landscape_module.f90#bwb_y
  - output_landscape_module.f90#hltwb_d
  - output_landscape_module.f90#hwb_a
  - output_landscape_module.f90#hwb_d
  - output_landscape_module.f90#hwb_m
  - output_landscape_module.f90#hwb_y
  - output_landscape_module.f90#ruwb_a
  - output_landscape_module.f90#ruwb_d
  - output_landscape_module.f90#ruwb_m
  - output_landscape_module.f90#ruwb_y
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: ""
---

# basin_sw_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_sw_init.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[calibration_data_module.f90]]
  - [[output_landscape_module.f90]]
  - [[basin_module.f90]]
  - [[maximum_data_module.f90]]
  - [[soil_module.f90]]
  - [[hru_module.f90]]
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
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#lsu_out]] - `landscape_units`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#bwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#bwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#bwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#bwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#hltwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_y]] - `output_waterbal`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
